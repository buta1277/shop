# Shopify Theme - Dev

## 快速开始
- 主题结构：assets / blocks / config / layout / locales / sections / snippets / templates
- 不入库：`config/settings_data.json`（各环境在后台维护），请参考 `config/settings_data.json.sample`

## 本地校验（可选）
- Shopify CLI: `shopify theme check`
- 预览：`shopify theme dev`（仅用于本地开发，不改线上）

## 发布流程（不连线上）
1. 在本地合并到 `main`
2. 打包 zip（排除 node_modules、.git 等）
3. 后台 **Add theme → Upload zip** 到开发副本主题，预览自测
4. 验证通过后再 Publish
