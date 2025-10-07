# GPT 协作说明

## 使用方式
- 在 `gpt/tasks/` 写清目标/范围/验收标准（Definition of Ready/Done）
- 在 `gpt/contexts/` 放目录树、依赖图、配置键说明等上下文
- 使用 `gpt/prompts/` 中的模板让 GPT 产出**可直接应用的 diff**
- 产出先放 `gpt/outputs/`，经人工检查再应用到主题目录

## 产出要求
1) 变更文件清单 + diff/patch
2) 受影响页面的自测点（引用 docs/checklists）
3) 必须给回滚方案
