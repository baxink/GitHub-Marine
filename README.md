# GitHub-Maritime 海事法规知识库

> 摘要：内河/海船法定检验技术规则版本管理仓库，支持按年度修改通报追溯与版本切换。

## 定位

专注海事法规法定检验技术规则的版本管理，包括：
- 内河船舶法定检验技术规则
- 国内航行海船法定检验技术规则
- 船舶检验规则及相关修改通报

## 版本体系

### 内河船舶法定检验技术规则

| 版本 | 文件 | Git标签 |
|------|------|---------|
| 2019第5篇船舶安全（底座） | `raw/内河船舶法定检验技术规则 2019 第5篇 船舶安全.md` | `msa/inland-inspection/2019` |
| 2023年修改通报 | `raw/内河船舶法定检验技术规则（2023年修改通报）.md` | `msa/inland-inspection/2023-amend` |
| 2025年修改通报 | `raw/内河船舶法定检验技术规则2025年修改通报.md` | `msa/inland-inspection/2025-amend` |

### 现行适用版入口

通过总入口文件快速定位现行要求：
- [内河船舶法定检验技术规则-现行适用版总入口.md](knowledge/maritime-laws/indices/file-indices/内河船舶法定检验技术规则-现行适用版总入口.md)

检索顺序：**2019原章 → 2023修订 → 2025修订**

## 仓库结构

```
GitHub-Maritime/
├── knowledge/maritime-laws/
│   ├── raw/                          # 原始法规文件
│   │   ├── 内河船舶法定检验技术规则 2019 第5篇 船舶安全.md
│   │   ├── 内河船舶法定检验技术规则（2023年修改通报）.md
│   │   └── 内河船舶法定检验技术规则2025年修改通报.md
│   ├── processed/
│   │   ├── chapters/                 # 章节切片（按章拆分）
│   │   └── topic-index.md            # 主题索引
│   └── indices/
│       ├── maritime-index.md         # 总索引
│       └── file-indices/            # 文件级索引
│           ├── 内河船舶法定检验技术规则-现行适用版总入口.md
│           ├── 内河船舶法定检验技术规则2025年修改通报-关联索引.md
│           └── ...
└── README.md
```

## 使用方式

### 版本切换

```bash
# 克隆仓库
git clone https://github.com/baxink/GitHub-Maritime.git

# 查看2019基础版本
git checkout msa/inland-inspection/2019

# 查看2023修改通报后状态
git checkout msa/inland-inspection/2023-amend

# 查看2025修改通报后状态（现行）
git checkout main

# 对比两个版本的差异
git diff msa/inland-inspection/2019..msa/inland-inspection/2025-amend
```

### 检索现行要求

1. **快速入口**：从总入口文件按主题查对应的2019/2023/2025章节
2. **关联索引**：每个修改通报文件对应到2019底座的具体章节
3. **按时间顺序**：先读2019原章，再逐个核对修改通报的修订

## 分支策略

| 分支 | 用途 |
|------|------|
| `main` | 现行稳定版 |
| `amendment/规则名-年份` | 修改通报专用分支 |

### 新增修改通报流程

```bash
# 1. 创建分支
git checkout -b amendment/inland-inspection-2026

# 2. 添加修改通报文件
git add knowledge/maritime-laws/raw/内河船舶法定检验技术规则2026年修改通报.md
git commit -m "amend(msa): 内河船舶法定检验技术规则2026年修改通报"

# 3. 推送并创建PR
git push -u origin amendment/inland-inspection-2026

# 4. 合并后打标签
git tag -a msa/inland-inspection/2026-amend -m "2026年修改通报"
git push origin --tags
```

## 提交规范

```
feat(msa): 新增内河船舶法定检验技术规则2026年修改通报
amend(msa): 内河船舶法定检验技术规则2025年修改通报
fix(index): 修复索引链接
docs: 更新文档
```

## 版权声明

本知识库收录的法规文件均来自公开渠道，版权归中华人民共和国交通运输部/海事局所有。
本仓库提供的索引和组织服务仅供学习研究使用，不构成法律或技术咨询。

---

使用前请以官方发布的最新版本为准。