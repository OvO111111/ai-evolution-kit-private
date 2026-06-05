# Shengzhijing Source Map

Use this as a compact map, not a replacement for source inspection.

## Confirmed Reference Files

- `D:\xiaochengxu\shengzhijing\声之境素材\方案\PRD-多应用管理平台.md`
- `D:\xiaochengxu\shengzhijing\声之境素材\方案\mockup-多应用管理平台.html`
- `D:\xiaochengxu\shengzhijing\H5-MIGRATION-PLAN.md`
- `D:\xiaochengxu\shengzhijing\h5-web\src\pages\Home.jsx`
- `D:\xiaochengxu\shengzhijing\h5-web\src\pages\Player.jsx`
- `D:\xiaochengxu\shengzhijing\h5-web\src\pages\Pay.jsx`
- `D:\xiaochengxu\shengzhijing\h5-web\src\pages\Mine.jsx`
- `D:\xiaochengxu\shengzhijing\admin-web\src\pages\AppList.jsx`
- `D:\xiaochengxu\shengzhijing\admin-web\src\pages\ContentMgmt.jsx`
- `D:\xiaochengxu\shengzhijing\admin-web\src\pages\Products.jsx`
- `D:\xiaochengxu\shengzhijing\admin-web\src\pages\Config.jsx`
- `D:\xiaochengxu\shengzhijing\admin-web\src\pages\Orders.jsx`
- `D:\xiaochengxu\shengzhijing\admin-web\src\pages\Accounts.jsx`

## Inherited Structure

- Product structure should be inferred from the H5 implementation and any current project brief, not from old non-H5 deliverables.
- Unified platform PRD has account/login, app list, app permission, app-specific content management, app-level configuration, order list, and phased expansion.
- H5 prototype output should use a `750px` single-image/mobile-design width.
- Admin mockup uses a `1280px` admin frame with a persistent `220px` left sidebar.
- Admin routes include app overview, content, products, config, orders, and accounts.

## Caveats

- Do not copy merchant numbers, AppIDs, env IDs, or payment secrets into skills, exports, PRDs, or examples.
- Some current React source text is mojibake in shell output. Use it for route/module/data structure; use PRD/mockup/new context for Chinese copy.
- The existing voice project is audio-centric. New projects should inherit structure and interaction patterns, not audio terminology.
- Do not create non-H5 pages, non-H5 payment assumptions, or narrow phone-frame outputs unless the user explicitly overrides the H5-only rule.
