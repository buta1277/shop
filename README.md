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
## 发布与回滚流程

### 发布（到副本主题）
1. 在本地合并到 `main`，确认通过检查。
2. 打包 ZIP（排除 `.git/`, `node_modules/`, `dist/`, `build/`, `*.map` 等）。
3. Shopify 后台：**Online Store → Themes → Add theme → Upload zip**，上传到“开发副本主题”。
4. 预览并全路径回归测试（首页→集合→商品→购物车→结账入口）。
5. 确认无误后，再 **Publish** 到线上。

### 版本打 Tag（便于回滚）
```bash
# 上线前在 main 打版本号 tag（例：2025-10-07）
git checkout main
git pull
git tag v2025.10.07
git push origin v2025.10.07
