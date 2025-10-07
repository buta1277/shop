# gpt/contexts/overview.md

> 用途：为项目成员快速理解主题目录与首页装配逻辑，便于后续讨论而不触碰线上主题。  
> 仅产出资料与方法论，不包含任何可能改变模板行为的改动。

## 主题目录结构速览（作用与常见内容）

- **assets/**
  - 静态资源与打包产物（`*.css`、`*.js`、图片、字体、`theme.css`/`theme.js` 等）。
  - 命名建议：页面/区块作用前缀 + 内容，如 `home-hero.css`、`product-card.js`。
- **layout/**
  - 框架模版（`theme.liquid`、`checkout.liquid` 等），定义全局 `<head>`、页眉/页脚挂点、脚本注入顺序。
  - 依赖：会渲染 `sections/header`、`sections/footer` 等全局区块。
- **sections/**
  - 页面可拼装的“区块”，如 `slideshow.liquid`、`featured-collection.liquid`、`rich-text.liquid`。
  - 配置项来自 `schema` 块；可被 `templates/*.json` 引用。
- **snippets/**
  - 片段/组件（卡片、价格、分页、SVG 图标等），供 `sections`/`templates`/`layout` 复用。
  - 命名建议：功能型（`price`, `badge`, `pagination`），避免与 `sections` 重名。
- **templates/**
  - 页面入口与布局映射：
    - `*.json`（Online Store 2.0）：声明本页使用的 `sections` 及其顺序与设置。
    - `*.liquid`（传统或动态场景）：可直接包含逻辑与 `section`/`snippet`。
  - 典型：`index.json`（首页）、`collection.json`、`product.json`、`cart.json` 等。
- **locales/**
  - 语言包（`en.default.json`、`zh-CN.json` 等）；键来自 `settings_schema.json` 与各 `section schema` 文案。
  - 约定：新增 UI 文案务必绑定 key，避免写死字符串。
- **config/**
  - 主题设置定义：`settings_schema.json`（结构与控件），`settings_data.json`（各环境实时值，**不入库**）。
  - `settings_schema.json` 决定“自定义主题”面板出现哪些开关与默认值。
- **blocks/**
  - 可选目录（如定制脚本/构建产物分类存放）；若存在，注意与 `sections` 中的 block 定义区分命名。
  - 在本仓库中用于归档/脚手架时，**不可直接在模板里 include**，改由 `sections/snippets` 调用。

> 依赖图优先：`templates` → `sections`（可能包含 `snippets`）→ 读取 `config/settings_schema.json`/`locales`。任何改动需先画依赖图与回滚路径。

---

## 首页入口梳理（从 `templates/index.json` 推导）

> 说明：以下为标准化梳理流程与占位表，供本地打开 `templates/index.json` 后快速填充并评审；仅做准备，不改线上。

**步骤（只读核对，不做改动）：**
1. 打开 `templates/index.json`，定位顶层 `sections` 映射与 `order` 数组。
2. 逐个记录：
   - **Section 句柄**（如 `"hero"`, `"featured-collection"`, `"rich-text"`）。
   - **Section 文件**（映射到 `sections/<handle>.liquid`，也可能是 `<type>.liquid`）。
   - **Blocks**（如轮播项、卡片等的 `type` 与 `settings`）。
3. 搜索潜在 `snippets` / `assets` 依赖：
   - 在每个 `section` 文件中检索 `{% render %}`/`{% include %}` 引用的 `snippets/*`。
   - 检查是否引用特定样式/脚本（例如 `assets/section-*.css|js`，或在 schema `settings` 中出现 `icon_*` 与图片上传字段，暗示到 `assets`）。

**占位清单（拉平版，供填表）：**

| 顺序 | Section 句柄/类型 | sections 文件猜测 | 关键 blocks（type） | 直连 snippets（猜测） | 直连 assets（猜测） | 备注 |
|---|---|---|---|---|---|---|
| 1 | （待填） | `sections/（待填）.liquid` | （待填） | （如 `price`, `rating`, `media`） | （如 `home-hero.css`, `slider.js`） | （待填） |
| 2 | … | … | … | … | … | … |
| n | … | … | … | … | … | … |

**核对要点（自测清单·只读）：**
- `order` 中所有键都能在 `sections` 对象或主题目录找到对应文件。
- 每个 section 的 `settings` 与 block 的 `settings` 在主题编辑器中能对应出现。
- 若 section 依赖 snippet，snippet 是否存在且不与其他 section 同名。
- 若有图片/图标/视频上传字段，确认 `assets/` 下是否已有占位资源或将由内容团队上传。

**影响范围（若未来要调整首页结构）：**
- 改动 `index.json` 会影响**线上首页拼装**；需先复制为副本 template 测试。
- 涉及的 `sections`/`snippets` 与其 schema 文案将牵动 `locales` 与 `config`。

**回滚方案（规划）：**
- 以日期创建 `index.json` 备份副本（或在后台复制模板），失败时一键切回旧版。
- Git 上以标签点或分支保留旧模板版本。

---

**下一步建议（仍为准备，不做改动）**
- 在本地拉取仓库，打开 `templates/index.json`，按上表完成一次性清点。
- 生成“首页依赖图”（`index.json` → 具体 `sections` → `snippets/assets`），放入 `/gpt/contexts/`。
- 对每个 section 写 1 句“业务目的 + 风险点”（如依赖外部脚本、懒加载顺序等），用于评审会。
