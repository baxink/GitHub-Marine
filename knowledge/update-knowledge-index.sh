#!/bin/bash

# 知识库索引更新辅助脚本
# 用于帮助用户维护 knowledge-index.md 文件

KNOWLEDGE_ROOT="/Users/fanxiaojun/Desktop/Workspace/knowledge_知识库"
INDEX_FILE="$KNOWLEDGE_ROOT/knowledge-index.md"
TIMESTAMP=$(date +%Y-%m-%d)

echo "🔍 知识库文件检查"
echo "=================="
echo ""

# 统计各分类文件数量
echo "📊 当前文件统计："
echo "----------------"

CCS_COUNT=$(find "$KNOWLEDGE_ROOT/ccs-rules" -type f \( -name "*.md" -o -name "*.json" \) 2>/dev/null | wc -l | tr -d ' ')
INTL_COUNT=$(find "$KNOWLEDGE_ROOT/international-standards" -type f \( -name "*.md" -o -name "*.json" \) 2>/dev/null | wc -l | tr -d ' ')
MANUAL_COUNT=$(find "$KNOWLEDGE_ROOT/design-manuals" -type f \( -name "*.md" -o -name "*.json" \) 2>/dev/null | wc -l | tr -d ' ')
MARITIME_COUNT=$(find "$KNOWLEDGE_ROOT/maritime-laws/raw" -type f \( -name "*.md" -o -name "*.json" \) 2>/dev/null | wc -l | tr -d ' ')
TOTAL=$((CCS_COUNT + INTL_COUNT + MANUAL_COUNT + MARITIME_COUNT))

echo "  CCS规范: $CCS_COUNT 个文件"
echo "  国际标准: $INTL_COUNT 个文件"
echo "  设计手册: $MANUAL_COUNT 个文件"
echo "  海事法规: $MARITIME_COUNT 个文件"
echo "  📈 总计: $TOTAL 个文件"
echo ""

# 检查是否有未在索引中记录的新文件夹
echo "📁 文件夹检查："
echo "--------------"
find "$KNOWLEDGE_ROOT" -mindepth 1 -type d ! -name "docs" ! -name "references" ! -name ".*" | while read -r dir; do
    dirname=$(basename "$dir")
    case "$dirname" in
        "ccs-rules"|"international-standards"|"design-manuals"|"maritime-laws"|"docs"|"references")
            # 已知文件夹，跳过
            ;;
        *)
            echo "  ⚠️  发现未分类文件夹: $dirname"
            echo "     位置: $dir"
            echo "     建议: 如果这是新分类，请在 knowledge-index.md 中添加对应部分"
            ;;
    esac
done
echo ""

# 查找最近7天内修改的文件
echo "🔄 最近更新文件（7天内）："
echo "--------------------------"
RECENT_FILES=$(find "$KNOWLEDGE_ROOT" -type f \( -name "*.md" -o -name "*.json" \) -mtime -7 2>/dev/null | grep -v "knowledge-index.md" | head -10)
if [ -n "$RECENT_FILES" ]; then
    echo "$RECENT_FILES" | while read -r file; do
        filename=$(basename "$file")
        filedir=$(dirname "$file" | sed "s|$KNOWLEDGE_ROOT/||")
        echo "  📄 $filename (位于 $filedir/)"
    done
else
    echo "  未发现最近修改的文件"
fi
echo ""

# 检查索引文件是否存在
if [ ! -f "$INDEX_FILE" ]; then
    echo "❌ 错误：索引文件不存在"
    echo "  请创建 $INDEX_FILE"
    exit 1
fi

# 检查索引文件最后更新日期
INDEX_DATE=$(grep -E "^最后更新：[0-9]{4}-[0-9]{2}-[0-9]{2}" "$INDEX_FILE" | head -1 | sed 's/最后更新：//')
if [ -n "$INDEX_DATE" ]; then
    echo "📅 索引文件最后更新：$INDEX_DATE"

    # 计算天数差（简单版本，假设日期格式正确）
    INDEX_TS=$(date -j -f "%Y-%m-%d" "$INDEX_DATE" "+%s" 2>/dev/null || date -d "$INDEX_DATE" "+%s" 2>/dev/null)
    NOW_TS=$(date "+%s")
    if [ -n "$INDEX_TS" ]; then
        DAYS_DIFF=$(( (NOW_TS - INDEX_TS) / 86400 ))
        if [ "$DAYS_DIFF" -gt 30 ]; then
            echo "  ⚠️  索引已超过 $DAYS_DIFF 天未更新"
        fi
    fi
else
    echo "⚠️  未找到索引文件更新日期"
fi
echo ""

# 提供更新建议
echo "💡 更新建议："
echo "------------"
echo "1. 如果有新文件，请："
echo "   a) 放入对应分类文件夹"
echo "   b) 编辑 $INDEX_FILE"
echo "   c) 在对应分类表格中添加新行"
echo "   d) 更新关键词索引"
echo ""
echo "2. 更新索引文件中的："
echo "   - 文件数量统计"
echo "   - '最后更新'日期（今天：$TIMESTAMP）"
echo ""
echo "3. 可选：更新workspace索引"
echo "   cd /Users/fanxiaojun/Desktop/Workspace/ai_context/index"
echo "   bash update-index.sh"
echo ""

echo "✅ 检查完成"
echo ""
echo "📝 快速添加新文件模板（复制到 knowledge-index.md 对应位置）："
echo "----------------------------------------------------------------"
echo "| \`新文件名.md\` | 年份 | 关键词1, 关键词2 | 简要描述 |"
echo ""
echo "📌 记住：保持索引简洁，仅包含元数据，不复制文件内容。"