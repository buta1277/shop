<!-- 提示词模板：多语言抽取 -->
目标：将给定 Liquid/JS 中的硬编码文案抽取到 locales。
约束：
- 生成 locales key：`<feature>.<component>.<purpose>`
- 保持插值/变量不变（如 {{ product.title }}）
- 仅改文案与引用，业务逻辑不变
输出：
1) 变更前后 diff
2) 新增/修改的 locale keys 列表（含默认中文）
3) 受影响页面的回归要点
