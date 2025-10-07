# 主题发布/回滚 Playbook（简版）

## 发布（副本主题）
1. 合并到 `main` → 本地打包 ZIP（排除 .git、node_modules、dist、build、*.map 等）
2. 后台 Online Store → Themes → Add theme → Upload zip（上传到“开发副本主题”）
3. 预览并执行回归清单
4. 无问题后再 Publish

## 回滚
- 每次发布在 `main` 打 tag（例：`v2025.10.07`）
- 回滚：`git reset --hard v2025.10.07 && git push --force-with-lease`
