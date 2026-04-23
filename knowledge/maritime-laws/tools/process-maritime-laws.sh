#!/bin/bash

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARITIME_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RAW_DIR="$MARITIME_ROOT/raw"
PROCESSED_DIR="$MARITIME_ROOT/processed"
CHAPTERS_DIR="$PROCESSED_DIR/chapters"
INDICES_DIR="$MARITIME_ROOT/indices"
FILE_INDICES_DIR="$INDICES_DIR/file-indices"
MAIN_INDEX="$INDICES_DIR/maritime-index.md"
UPDATE_REPORT="$INDICES_DIR/update-report.txt"

printf "${BLUE}========================================${NC}\n"
printf "${BLUE}  海事法规知识库处理脚本 v2.0${NC}\n"
printf "${BLUE}========================================${NC}\n\n"

if [ ! -d "$RAW_DIR" ]; then
  printf "${RED}❌ 错误：原始文件目录不存在：%s${NC}\n" "$RAW_DIR"
  exit 1
fi

mkdir -p "$CHAPTERS_DIR" "$FILE_INDICES_DIR"

if [ -f "$MAIN_INDEX" ]; then
  cp "$MAIN_INDEX" "$MAIN_INDEX.backup.$(date +%Y%m%d_%H%M%S)"
fi

printf "${GREEN}📁 海事法规目录：%s${NC}\n" "$MARITIME_ROOT"
printf "${GREEN}📂 章节切片目录：%s${NC}\n" "$CHAPTERS_DIR"
printf "${GREEN}📝 单文件索引目录：%s${NC}\n\n" "$FILE_INDICES_DIR"

ROOT_MD_COUNT=$(find "$MARITIME_ROOT" -maxdepth 1 -name "*.md" | wc -l | tr -d ' ')
PROCESSED_ROOT_MD_COUNT=$(find "$PROCESSED_DIR" -maxdepth 1 -name "*.md" | wc -l | tr -d ' ')

{
  echo "# 海事法规更新报告"
  echo "生成时间: $(date '+%Y-%m-%d %H:%M:%S')"
  echo
  if [ "$ROOT_MD_COUNT" -gt 1 ]; then
    echo "## 提示"
    echo "- maritime-laws 根目录下仍有未纳入 raw/ 的法规 Markdown，请检查并归位。"
    echo
  fi
  if [ "$PROCESSED_ROOT_MD_COUNT" -gt 1 ]; then
    echo "## 提示"
    echo "- processed/ 根目录下仍有遗留 Markdown，请确认是否为半成品。"
    echo
  fi
  echo "## 已处理文件"
} > "$UPDATE_REPORT"

COUNT=0
for file in "$RAW_DIR"/*.md; do
  [ -f "$file" ] || continue
  filename="$(basename "$file")"
  basename="${filename%.md}"
  file_index="$FILE_INDICES_DIR/$basename-index.md"

  printf "${BLUE}🔧 处理文件：%s${NC}\n" "$filename"
  python3 "$SCRIPT_DIR/analyze-md.py" \
    "$file" \
    --output-index "$file_index" \
    --output-chapters "$CHAPTERS_DIR"

  chapter_dir="$CHAPTERS_DIR/$basename"
  chapter_count=0
  if [ -d "$chapter_dir" ]; then
    chapter_count=$(find "$chapter_dir" -maxdepth 1 -name "*.md" | wc -l | tr -d ' ')
  fi

  echo "- $filename → $chapter_count 个切片，索引：$(basename "$file_index")" >> "$UPDATE_REPORT"
  COUNT=$((COUNT + 1))
  echo
 done

cat > "$MAIN_INDEX" <<EOF
# 海事法规索引

最后更新：$(date +%Y-%m-%d)

本索引提供海事法规库的轻量级概览，支持快速检索和精准引用。法规优先按章节切片管理，章节文件统一位于 processed/chapters/，文件详细索引统一位于 indices/file-indices/。

## 📊 法规概览

| 分类 | 文件数量 | 说明 |
|------|----------|------|
| 国际公约 | 待人工复核 | IMO公约、MSC决议等 |
| 国内法规 | 待人工复核 | 中国海事局法规与实施指南 |
| 技术规范 | 待人工复核 | 专项技术规则和检验指南 |
| 总计 | $COUNT | 以 raw/ 目录下文件为准 |

## 🔍 快速查询指南

1. 先查看本文件确认法规范围
2. 再进入 indices/file-indices/ 查看单文件索引
3. 按需打开 processed/chapters/ 下的章节切片
4. 主题交叉问题优先查看 processed/topic-index.md

## 🔄 更新记录

- $(date +%Y-%m-%d)：按 processed/chapters/ 体系重建索引骨架

---

*本索引由处理脚本重建骨架，建议在此基础上人工补充分类表和主题入口。*
EOF

printf "${GREEN}✅ 已处理 %s 个原始文件${NC}\n" "$COUNT"
printf "${GREEN}📄 更新报告：%s${NC}\n" "$UPDATE_REPORT"
printf "${GREEN}📘 总索引骨架：%s${NC}\n" "$MAIN_INDEX"
