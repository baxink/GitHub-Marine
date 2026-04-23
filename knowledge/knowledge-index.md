# 知识库总索引

最后更新：2026-04-20

> 摘要：知识库约200个文件的轻量级目录。采用**分层索引**：总索引→分类索引→文件，避免一次性加载大量内容。

---

## 📊 知识库概览（约200文件）

| 分类 | 文件数 | 索引位置 | 核心内容 |
|-----|-------|---------|---------|
| **CCS规范** | 11 | [CCS索引](ccs-rules/index.md) | 入级、建造（含内河）、材料、电池动力、直流电力规范 |
| **ABS规范** | 2 | [ABS索引](abs-rules/index.md) | 谐波控制、混合动力指南 |
| **海事法规** | 6+ | [法规索引](maritime-laws/indices/maritime-index.md) | 内河/海船/游艇法定检验规则、SOLAS |
| **设计手册** | 4 | [设计手册索引](design-manuals/index.md) | 电气、轮机设计参考 |
| **国际标准** | 6 | [国际标准索引](international-standards/index.md) | IEC/ISO标准 |
| **国家标准** | 2 | [国家标准索引](national-standards_国家标准/index.md) | GB标准 |

---

## ⚡ 快速入口

### 按主题

| 主题 | 相关索引 | 关键词 |
|-----|---------|--------|
| **电池动力** | [CCS-电池动力](ccs-rules/index.md) + [CCS-混合动力](ccs-rules/index.md) + [MSA-氢燃料电池](maritime-laws/indices/file-indices/MSA%20《氢燃料电池动力船舶技术与检验暂行规则》2022-index.md) | 电池、电动船舶、氢燃料电池、混合动力 |
| **直流电力系统** | [CCS-直流电力](ccs-rules/index.md) | 直流配电、综合电力、固态开关 |
| **法定检验** | [海事法规索引](maritime-laws/indices/maritime-index.md) | 内河、海船、游艇、检验规则 |
| **内河建造** | [CCS-内河建造](ccs-rules/index.md) | 内河船舶、建造规范、入级 |
| **电气/EMC** | [设计手册-电气](design-manuals/index.md) + [IEC-EMC](international-standards/iec-standards/IEC%2060533-2015%20EMC.md) + [ABS-谐波](abs-rules/index.md) | 电力推进、电磁兼容、谐波控制 |
| **材料焊接** | [CCS-材料](ccs-rules/index.md) | 材料、焊接、管系 |
| **建造入级** | [CCS-建造](ccs-rules/index.md) | 船体、轮机、电气建造 |

### 超大文件（>8000行，必须先查索引）

| 文件 | 行数 | 索引 |
|-----|------|-----|
| **钢质内河船舶建造规范 2016** | 24,735 | [内河建造索引](ccs-rules/indices/钢质内河船舶建造规范%202016-index.md) |
| CCS材料与焊接规范 2025 | 16,478 | [材料索引](ccs-rules/indices/CCS%20材料与焊接规范%202025-index.md) |
| 国内航行海船法定检验技术规则（2020）第4篇 船舶安全 | 16,347 | [海船安全索引](maritime-laws/indices/file-indices/国内航行海船法定检验技术规则（2020）%20第4篇%20船舶安全-index.md) |
| IEC 61162-1-2024 | 11,494 | [IEC索引](international-standards/iec-standards/indices/IEC%2061162-1-2024-index.md) |
| 内河船舶法定检验技术规则 2019 第5篇 船舶安全 | 10,243 | [内河安全索引](maritime-laws/indices/file-indices/内河船舶法定检验技术规则%202019%20第5篇%20船舶安全-index.md) |
| 国内航行海船建造规范 2025 | 8,408 | [建造索引](ccs-rules/indices/国内航行海船建造规范%202025-index.md) |

### 大文件（3000-8000行，建议先查索引）

| 文件 | 行数 | 索引 |
|-----|------|-----|
| 钢质海船入级规范 第4篇 | 6,342 | [入级索引](ccs-rules/indices/CCS%20钢质海船入级规范%202025%20第4篇-index.md) |
| 船舶应用电池动力规范 2025 | 4,352 | [电池索引](ccs-rules/indices/CCS%20船舶应用电池动力规范%202025-index.md) |
| 钢质内河船舶建造规范 2019修改通报 | 4,168 | [内河2019索引](ccs-rules/indices/钢质内河船舶建造规范%202019修改通报-index.md) |

---

## 🔍 检索策略

1. **总索引**（本文件）：确定需要哪个分类索引
2. **分类索引**：确定需要哪个具体文件或章节
3. **章节文件**：从 `processed/chapters/` 按需加载

### Token效率对比

| 操作 | Token消耗 | 场景 |
|-----|-----------|------|
| 加载本索引 | ~1K | 每次会话1次 |
| 加载分类索引 | ~1-1.5K | 需要时加载 |
| 加载超大文件全文 | ~15-30K | 避免 |
| 加载章节文件 | ~1-3K | 推荐 |

---

## 🏷️ 主题标签速查

```
#电池动力    → ccs-rules/CCS 《船舶应用电池动力规范》2025.md
#电磁兼容    → international-standards/iec-standards/IEC 60533-2015 EMC.md
              → abs-rules/ABS electrical-harmonics-gn.md
              → national-standards_国家标准/GB_T 43527-2023.md
#材料焊接    → ccs-rules/CCS 材料与焊接规范 2025.md
#电力推进    → design-manuals/船舶设计手册 电气 第四篇 船舶电力推进.md
#直流电力    → ccs-rules/CCS 船舶直流综合电力系统检验指南 2023.md
#法定检验    → maritime-laws/processed/chapters/
#游艇检验    → maritime-laws/MSA 游艇法定检验暂行规定（2023年修改通报）.md
#内河建造    → ccs-rules/《钢质内河船舶建造规范》（2016）.md
#建造规范    → ccs-rules/《国内航行海船建造规范》2025
#入级规范    → ccs-rules/CCS 《钢质海船入级规范》2025
```

---

## 📖 引用格式

```
[KB:CCS-电池动力]        → 船舶应用电池动力规范
[KB:CCS-直流电力]        → 船舶直流综合电力系统检验指南
[KB:CCS-内河建造]        → 钢质内河船舶建造规范2016及修改通报
[KB:CCS-建造规范]        → 国内航行海船建造规范
[KB:CCS-入级规范]        → 钢质海船入级规范
[KB:ABS-谐波]           → ABS 电力系统谐波控制指南
[KB:ABS-混合动力]        → ABS Hybrid Advisory 17033
[KB:法规-游艇检验]       → 游艇法定检验暂行规定（2023年修改通报）
[KB:法规-内河检验]       → 内河船舶法定检验技术规则
[KB:法规-海船检验]       → 国内航行海船法定检验技术规则
[KB:IEC-EMC]            → IEC 60533 电磁兼容
[KB:设计手册-电力推进]    → 船舶电力推进设计手册
```

---

*本索引约 1.5K tokens，是知识库的唯一入口。详细索引按分类隔离，按需加载。*
