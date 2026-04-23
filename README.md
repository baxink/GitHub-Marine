# GitHub-Marine 知识库管理方案

## 概述

在GitHub上创建`GitHub-Marine`仓库，用于管理海事法规知识库的版本控制，支持按年度修改通报进行增删改。

## 仓库结构

```
GitHub-Marine/                    # 对应 GitHub: fanxiaojun/GitHub-Marine
├── .github/
│   ├── workflows/
│   │   ├── validate-index.yml    # PR时检查索引一致性
│   │   ├── update-index.yml      # 自动更新索引
│   │   └── release.yml           # 版本发布
│   ├── CODEOWNERS                # 分类维护者
│   └── PULL_REQUEST_TEMPLATE.md  # PR模板
├── knowledge/                    # 正式知识库（对应knowledge_知识库/）
│   ├── ccs-rules/                # CCS规范
│   ├── maritime-laws/            # 海事法规
│   │   ├── raw/                  # 原始文件
│   │   ├── processed/            # 处理后文件
│   │   │   ├── chapters/         # 章节切片
│   │   │   └── consolidated/     # 合并版本
│   │   └── indices/              # 索引文件
│   ├── abs-rules/                # ABS规范
│   ├── design-manuals/           # 设计手册
│   ├── international-standards/  # 国际标准
│   ├── national-standards/       # 国标
│   └── knowledge-index.md        # 总索引
├── research/                     # 研究内容（探索性，与main分支隔离）
├── scripts/
│   ├── update-all-indices.sh     # 索引更新脚本
│   ├── validate-cross-refs.py    # 交叉引用验证
│   └── generate-consolidated.py  # 生成合并版本
├── docs/
│   ├── CONTRIBUTING.md           # 贡献指南
│   ├── VERSION_MANAGEMENT.md     # 版本管理规范
│   └── INDEX_SYSTEM.md           # 索引系统说明
├── .gitignore
├── .gitattributes
└── README.md                     # 含版权和免责声明
```

## 分支策略

| 分支 | 用途 | 保护规则 |
|------|------|----------|
| `main` | 稳定的知识库内容 | 需PR审核，禁止直接push |
| `research` | 探索性研究内容 | 独立演进，验证后cherry-pick到main |
| `feature/规范名-版本` | 新增规范 | 临时分支 |
| `amendment/规范名-年份` | 修改通报 | 临时分支 |
| `hotfix/问题描述` | 紧急修正 | 临时分支 |

## 版本管理

### Git标签体系
```
ccs/inland-construction/2016          # 基础版本
ccs/inland-construction/2019-amend    # 2019修改通报
msa/inland-inspection/2019            # 内河船舶法定检验技术规则2019
msa/inland-inspection/2023-amend      # 2023修改通报
msa/inland-inspection/2025-amend      # 2025修改通报
release/2026-Q1                       # 季度发布
```

### 修改通报处理（方案A：增量文件）
```
maritime-laws/
├── raw/
│   ├── 内河船舶法定检验技术规则2019第5篇船舶安全.md
│   ├── 内河船舶法定检验技术规则2023年修改通报.md
│   └── 内河船舶法定检验技术规则2025年修改通报.md
├── processed/
│   ├── chapters/
│   └── consolidated/
│       └── 内河船舶法定检验技术规则-2025合并版.md  # 自动生成
└── indices/
```

## 实施步骤

### 步骤1：本地初始化
```bash
cd /Users/fanxiaojun/Desktop/Workspace/GitHub-Marine
git init
git branch -M main
```

### 步骤2：配置remote并推送
```bash
git remote add origin https://github.com/fanxiaojun/GitHub-Marine.git
git add .
git commit -m "chore: initial commit - 知识库管理方案"
git push -u origin main
```

### 步骤3：创建research分支
```bash
git checkout -b research
git push -u origin research
```

### 步骤4：添加版本标签
```bash
git tag -a msa/inland-inspection/2019 -m "内河船舶法定检验技术规则2019"
git push origin --tags
```

## 协作规范

### 提交信息格式
```
feat(ccs): 新增船舶应用电池动力规范2025
amend(msa): 内河船舶法定检验技术规则2025年修改通报
fix(index): 修复CCS规范索引链接失效
docs(guide): 更新版本管理规范文档
chore(index): 自动更新索引 [skip ci]
```

### PR模板
```markdown
## 变更类型
- [ ] 新增规范
- [ ] 修改通报/变更通告
- [ ] 索引更新
- [ ] 错误修正

## 规范信息
- 规范名称：
- 版本/年份：
- 发布机构：
- 生效日期：

## 变更说明
<!-- 描述本次变更的内容和原因 -->

## 关联文件
<!-- 列出受影响的相关文件 -->

## 检查清单
- [ ] 已更新相关索引文件
- [ ] 已添加版本标签（如适用）
- [ ] 已验证交叉引用
- [ ] 已通过索引一致性检查
```

## 工作流自动化

### PR时索引检查
- 检查索引与内容一致性
- 验证交叉引用有效性
- 检查超大文件（>8000行建议切片）

### main分支push时自动更新索引
- GitHub Actions自动运行update-all-indices.sh
- 自动提交索引更新

### 手动触发版本发布
- 生成合并版本
- 创建Release Notes
- 打包下载

## 研究内容隔离

### 规则
- knowledge/目录不得引用research/内容
- 使用pre-commit hook检查
- research分支独立演进，验证后PR到main

### 验证流程
```
1. research分支开发探索性内容
2. 标记为"已验证"
3. 创建PR到main（审核来源和依据）
4. 合并后移入knowledge/
```

## 版权与免责声明

```markdown
## 免责声明

本知识库收录的规范法规技术标准均来自公开渠道，版权归原发布机构所有。
本仓库提供的索引、切片和关联服务仅供学习研究使用，不构成法律或技术咨询。
使用者应以官方发布的最新版本为准，本仓库不对内容的准确性、时效性承担责任。
```

## 关键文件清单

**需创建：**
- `.github/workflows/validate-index.yml`
- `.github/workflows/update-index.yml`
- `.github/workflows/release.yml`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.gitignore`
- `.gitattributes`
- `scripts/validate-cross-refs.py`
- `scripts/generate-consolidated.py`
- `docs/CONTRIBUTING.md`
- `docs/VERSION_MANAGEMENT.md`
- `docs/INDEX_SYSTEM.md`
- `README.md`

**待迁移：**
- `knowledge_知识库/` → `knowledge/`
- `scripts/update-all-indices.sh` → `scripts/`

## 验证场景

### 场景1：新增修改通报
```bash
# 1. 创建分支
git checkout -b amendment/inland-inspection-2026

# 2. 添加文件并提交
git add knowledge/maritime-laws/raw/内河船舶法定检验技术规则2026年修改通报.md
git commit -m "amend(msa): 内河船舶法定检验技术规则2026年修改通报"

# 3. 推送并创建PR
git push -u origin amendment/inland-inspection-2026

# 4. 合并后自动打标签
git tag -a msa/inland-inspection/2026-amend -m "2026年修改通报"
git push origin --tags
```

### 场景2：版本切换
```bash
# 查看2019基础版本
git checkout msa/inland-inspection/2019

# 查看2025现行版
git checkout main

# 对比差异
git diff msa/inland-inspection/2019..msa/inland-inspection/2025-amend
```

### 场景3：季度发布
1. 在GitHub页面手动触发`release.yml` workflow
2. 输入版本号（如2026-Q2）
3. 自动生成Release Notes和合并版本