#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海事法规Markdown文件分析工具
用于分析PDF转换的md文件结构，提取章节信息，生成索引和拆分文件
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import argparse

class MarkdownAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        self.basename = os.path.splitext(self.filename)[0]
        self.content = ""
        self.lines = []
        self.sections = []  # 章节列表
        self.metadata = {}  # 元数据
        self.stats = {}     # 统计信息

    def read_file(self):
        """读取文件内容"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            self.lines = self.content.split('\n')
            return True
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
            return False

    def extract_metadata(self):
        """从文件开头提取元数据"""
        # 常见的中文元数据模式
        metadata_patterns = {
            '发布机构': [r'发布机构[：:]\s*(.+)', r'机构[：:]\s*(.+)'],
            '生效日期': [r'生效日期[：:]\s*(.+)', r'日期[：:]\s*(.+)', r'(\d{4}年\d{1,2}月\d{1,2}日)'],
            '发布年份': [r'(\d{4})年'],
            '最新修正': [r'最新修正[：:]\s*(.+)', r'修正[：:]\s*(.+)'],
            '文号': [r'文号[：:]\s*(.+)', r'编号[：:]\s*(.+)'],
        }

        # 检查前50行
        for i, line in enumerate(self.lines[:50]):
            line = line.strip()
            for key, patterns in metadata_patterns.items():
                if key in self.metadata:
                    continue
                for pattern in patterns:
                    match = re.search(pattern, line)
                    if match:
                        self.metadata[key] = match.group(1).strip()
                        break

    def analyze_sections(self):
        """分析章节结构"""
        sections = []
        current_section = None
        section_stack = []  # 用于跟踪层级

        for i, line in enumerate(self.lines):
            line = line.rstrip()

            # 检查标题行
            if line.startswith('#') and ' ' in line:
                # 计算标题级别
                level = 0
                for char in line:
                    if char == '#':
                        level += 1
                    else:
                        break

                title = line[level:].strip()

                # 清理标题中的特殊字符
                clean_title = re.sub(r'[\[\]【】()（）]', '', title)

                section = {
                    'level': level,
                    'title': clean_title,
                    'original_title': title,
                    'line_number': i + 1,
                    'content_start': i + 1,
                    'content_end': None,
                    'children': [],
                    'parent': None
                }

                # 处理层级关系
                while section_stack and section_stack[-1]['level'] >= level:
                    section_stack.pop()

                if section_stack:
                    parent = section_stack[-1]
                    section['parent'] = parent['title']
                    parent['children'].append(clean_title)

                section_stack.append(section)
                sections.append(section)

                # 如果有上一个章节，设置其结束行
                if len(sections) > 1:
                    prev_section = sections[-2]
                    prev_section['content_end'] = i - 1

        # 设置最后一个章节的结束行
        if sections:
            sections[-1]['content_end'] = len(self.lines) - 1

        self.sections = sections
        self._build_section_tree()

    def get_chapters(self) -> List[Dict]:
        """提取用于切片的主章节。"""
        strict_patterns = [
            re.compile(r'^[第]\s*?[0-9IVX一二三四五六七八九十\-]+\s*?章'),
            re.compile(r'^附录\s*?[0-9IVX一二三四五六七八九十A-Za-z]+'),
        ]
        fallback_pattern = re.compile(r'^\d+\s+\S+')

        strict_matches = []
        seen = set()
        for s in self.sections:
            title = s['title'].strip()
            normalized_title = re.sub(r'\s+', '', title)
            if '..' in title or re.search(r'\.{2,}$', title):
                continue
            if '目录' in title:
                continue
            if ('修正案' in title and s['level'] <= 2 and strict_matches):
                continue
            if any(p.match(title) for p in strict_patterns) or ('修正案' in title and s['level'] <= 2):
                key = normalized_title
                if key not in seen:
                    seen.add(key)
                    strict_matches.append(s)

        if strict_matches:
            return strict_matches

        fallback_matches = []
        seen.clear()
        for s in self.sections:
            title = s['title'].strip()
            if '..' in title or re.search(r'\.{2,}$', title):
                continue
            if s['level'] <= 2 and fallback_pattern.match(title):
                key = (re.sub(r'\s+', '', title), s['level'])
                if key not in seen:
                    seen.add(key)
                    fallback_matches.append(s)

        return fallback_matches

    def split_by_chapters(self, output_dir: str) -> Dict[str, str]:
        """按章拆分文件（推荐方式）"""
        if not self.sections:
            return {}

        section_dir = os.path.join(output_dir, self.basename)
        os.makedirs(section_dir, exist_ok=True)

        section_files = {}

        # 使用get_chapters获取章级别章节
        chapters = self.get_chapters()
        if not chapters:
            print(f"⚠️ 未找到章级别章节，回退到普通章节拆分")
            return self.split_by_sections(output_dir, min_level=1)

        for i, chapter in enumerate(chapters):
            # 生成安全的文件名
            safe_title = re.sub(r'[^\w\u4e00-\u9fff\-]', '_', chapter['title'])
            if not safe_title or safe_title == '_':
                safe_title = f"chapter_{i+1}"

            filename = f"{self.basename}-{safe_title}.md"
            filepath = os.path.join(section_dir, filename)

            # 找到章节内容的结束位置：下一个章之前
            start_idx = chapter['content_start'] - 1
            end_idx = None
            for j in range(i + 1, len(chapters)):
                end_idx = chapters[j]['content_start'] - 1
                break

            if end_idx is None:
                end_idx = len(self.lines) - 1

            section_content = self.lines[start_idx:end_idx + 1]

            if len(section_content) < 3:
                continue

            header = [
                f"# {chapter['title']}",
                "",
                f"**来源文件**: {self.filename}",
                f"**章节级别**: 第{chapter['level']}级",
                f"**原始行号**: 第{chapter['line_number']}行",
                "",
                "---",
                ""
            ]

            full_content = '\n'.join(header + section_content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)

            section_files[chapter['title']] = filepath

        return section_files

    def _build_section_tree(self):
        """构建章节树形结构"""
        if not self.sections:
            return

        # 找出顶级章节（level=1或2）
        top_level = min(s['level'] for s in self.sections) if self.sections else 1
        self.top_sections = [s for s in self.sections if s['level'] == top_level]

    def extract_keywords(self):
        """提取关键词（简化版）"""
        keywords = set()

        # 从标题中提取关键词
        for section in self.sections:
            title = section['title']
            # 中文常见分隔符
            words = re.split(r'[、,，\.。\s\-—–]+', title)
            for word in words:
                if len(word) >= 2:  # 至少两个字符
                    keywords.add(word)

        # 从内容中提取常见术语（前100行）
        content_sample = '\n'.join(self.lines[:100])
        maritime_terms = [
            '船舶', '安全', '公约', '规范', '要求', '检验', '设备',
            '防火', '救生', '航行', '通信', '污染', '环保', '结构',
            '材料', '焊接', '电气', '轮机', '电池', '动力', '充电'
        ]

        for term in maritime_terms:
            if term in content_sample:
                keywords.add(term)

        self.keywords = sorted(list(keywords))

    def calculate_stats(self):
        """计算统计信息"""
        self.stats = {
            'total_lines': len(self.lines),
            'total_sections': len(self.sections),
            'top_level_sections': len([s for s in self.sections if s['level'] <= 2]),
            'deepest_level': max(s['level'] for s in self.sections) if self.sections else 0,
            'file_size': os.path.getsize(self.file_path),
            'estimated_pages': max(1, len(self.lines) // 50)  # 粗略估计
        }

    def analyze(self):
        """执行完整分析"""
        if not self.read_file():
            return False

        self.extract_metadata()
        self.analyze_sections()
        self.extract_keywords()
        self.calculate_stats()

        return True

    def generate_file_index(self) -> str:
        """生成文件索引markdown"""
        lines = []
        chapter_links = []

        for chapter in self.get_chapters():
            safe_title = re.sub(r'[^\w\u4e00-\u9fff\-]', '_', chapter['title'])
            if not safe_title or safe_title == '_':
                continue
            chapter_links.append((chapter['title'], f"processed/chapters/{self.basename}/{self.basename}-{safe_title}.md"))

        lines.append(f"# {self.filename} 索引")
        lines.append("")
        lines.append(f"> 摘要：{self.basename}，原文 {self.stats['total_lines']} 行。")
        lines.append("")

        lines.append("## 📋 基本信息")
        lines.append(f"- **文件**: {self.filename}")
        lines.append(f"- **原始位置**: raw/{self.filename}")
        lines.append(f"- **文件大小**: {self.stats['file_size']:,} 字节")
        lines.append(f"- **总行数**: {self.stats['total_lines']} 行")
        lines.append(f"- **估计页数**: 约 {self.stats['estimated_pages']} 页")
        if self.metadata:
            for key, value in self.metadata.items():
                lines.append(f"- **{key}**: {value}")
        lines.append("")

        lines.append("## 📖 章节简介（按需加载）")
        lines.append("")
        if chapter_links:
            for title, link in chapter_links:
                lines.append(f"### [{title}]({link})")
                lines.append("")
                lines.append("| 字段 | 内容 |")
                lines.append("|------|------|")
                lines.append("| **核心内容** | 待补充 |")
                lines.append(f"| **条款位置** | {title} |")
                lines.append("| **适用场景** | 待补充 |")
                lines.append("| **关联章节** | 待补充 |")
                lines.append("")
        else:
            lines.append("> 未识别到可切片的主章节，请结合原文人工补充。")
            lines.append("")

        lines.append("## 📑 完整章节结构")
        lines.append(f"共 {self.stats['total_sections']} 个章节，{self.stats['top_level_sections']} 个主要章节")
        lines.append("")

        for section in self.sections:
            indent = "  " * (section['level'] - 1)
            lines.append(f"{indent}- **{'#' * section['level']} {section['title']}** (第{section['line_number']}行)")

        lines.append("")

        if hasattr(self, 'keywords') and self.keywords:
            lines.append("## 🔑 关键词")
            lines.append(", ".join(self.keywords))
            lines.append("")

        lines.append("## 💡 使用说明")
        lines.append(f"1. **章节文件**: processed/chapters/{self.basename}/")
        lines.append(f"2. **引用格式**: `[海事法规：{self.basename}-章节名]`")
        lines.append("3. **快速定位**: 先查看章节简介，再按需打开章节切片")
        lines.append("")

        lines.append("---")
        lines.append("*本索引由海事法规分析工具自动生成，可在此基础上人工补充摘要与适用场景。*")

        return '\n'.join(lines)

    def split_by_sections(self, output_dir: str, min_level: int = 2) -> Dict[str, str]:
        """按章节拆分文件，返回章节文件路径列表

        Args:
            output_dir: 输出目录
            min_level: 最小拆分级别，1=篇/章都拆分，2=只拆章(默认)
        """
        if not self.sections:
            return {}

        # 创建输出目录
        section_dir = os.path.join(output_dir, self.basename)
        os.makedirs(section_dir, exist_ok=True)

        section_files = {}

        # 过滤需要拆分的章节（根据min_level）
        target_sections = [s for s in self.sections if s['level'] <= min_level]

        # 为每个目标章节查找其内容范围
        for i, section in enumerate(target_sections):
            # 生成安全的文件名
            safe_title = re.sub(r'[^\w\u4e00-\u9fff\-]', '_', section['title'])
            if not safe_title or safe_title == '_':
                safe_title = f"section_{i+1}"

            filename = f"{self.basename}-{safe_title}.md"
            filepath = os.path.join(section_dir, filename)

            # 找到章节内容的结束位置：下一个同级或更高级章节之前
            start_idx = section['content_start'] - 1  # 转换为0-based索引

            # 查找下一个同级或更高级章节的位置
            end_idx = None
            for j in range(i + 1, len(target_sections)):
                if target_sections[j]['level'] <= section['level']:
                    end_idx = target_sections[j]['content_start'] - 1
                    break

            if end_idx is None:
                end_idx = len(self.lines) - 1

            # 确保范围有效
            if start_idx < 0:
                start_idx = 0
            if end_idx >= len(self.lines):
                end_idx = len(self.lines) - 1

            section_content = self.lines[start_idx:end_idx + 1]

            # 跳过空章节
            if len(section_content) < 3:
                continue

            # 添加章节信息头部
            header = [
                f"# {section['title']}",
                "",
                f"**来源文件**: {self.filename}",
                f"**章节级别**: {'#' * section['level']}",
                f"**原始行号**: 第{section['line_number']}行",
                "",
                "---",
                ""
            ]

            full_content = '\n'.join(header + section_content)

            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)

            section_files[section['title']] = filepath

        return section_files

    def get_category(self) -> str:
        """自动判断文件分类"""
        filename = self.filename.lower()

        # 检查文件名中的关键词
        if any(word in filename for word in ['公约', 'convention', 'solas', 'marpol']):
            return '国际公约'
        elif any(word in filename for word in ['规范', '标准', 'guideline', 'code']):
            return '技术规范'
        elif any(word in filename for word in ['法规', '条例', '办法', '规定']):
            return '国内法规'
        else:
            # 检查内容中的关键词
            content_sample = self.content[:1000].lower()
            if any(word in content_sample for word in ['国际海事组织', 'imo', '缔约国']):
                return '国际公约'
            elif any(word in content_sample for word in ['中华人民共和国', '交通运输部', '海事局']):
                return '国内法规'
            else:
                return '技术规范'

def main():
    parser = argparse.ArgumentParser(description='分析海事法规Markdown文件')
    parser.add_argument('input_file', help='输入Markdown文件路径')
    parser.add_argument('--output-index', help='输出索引文件路径')
    parser.add_argument('--output-chapters', help='输出章节文件的目录')
    parser.add_argument('--output-sections', help='兼容旧参数，等同于 --output-chapters')
    parser.add_argument('--no-split', action='store_true', help='不拆分章节')
    parser.add_argument('--min-level', type=int, default=2, help='最小拆分级别(1=篇/章都拆,2=只拆章)')

    args = parser.parse_args()

    # 检查文件是否存在
    if not os.path.exists(args.input_file):
        print(f"❌ 文件不存在: {args.input_file}")
        return 1

    # 分析文件
    analyzer = MarkdownAnalyzer(args.input_file)

    print(f"🔍 分析文件: {analyzer.filename}")

    if not analyzer.analyze():
        print("❌ 分析失败")
        return 1

    print(f"✅ 分析完成")
    print(f"   章节数: {analyzer.stats['total_sections']}")
    print(f"   关键词: {', '.join(analyzer.keywords[:10])}...")

    # 生成索引文件
    if args.output_index:
        index_content = analyzer.generate_file_index()
        os.makedirs(os.path.dirname(args.output_index), exist_ok=True)
        with open(args.output_index, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"📝 索引文件已生成: {args.output_index}")

    output_chapters = args.output_chapters or args.output_sections

    # 拆分章节
    if not args.no_split and output_chapters:
        if args.min_level == 2:
            # 章级别拆分（推荐）
            section_files = analyzer.split_by_chapters(output_chapters)
        else:
            # 篇/章级别拆分
            section_files = analyzer.split_by_sections(output_chapters, min_level=args.min_level)
        print(f"📑 章节拆分完成: {len(section_files)} 个章节文件")

    # 输出分析结果摘要
    print("\n📊 分析摘要:")
    print(f"   文件分类: {analyzer.get_category()}")
    print(f"   元数据: {analyzer.metadata}")
    print(f"   主要章节: {[s['title'] for s in analyzer.sections[:5]]}")

    return 0

if __name__ == '__main__':
    sys.exit(main())