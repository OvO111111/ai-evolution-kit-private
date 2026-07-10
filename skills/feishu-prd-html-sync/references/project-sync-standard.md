# Project Sync Standard

## Naming

- Feishu display name follows the user's confirmed project name, not necessarily the local file name.
- Old names may remain in local file paths. Do not rename local files unless the user asks.
- If a source document title uses an old name, update the Feishu title/body to the confirmed name and mention the source file path.
- If old name and new name both appear in Feishu after sync, verify whether the old name should remain as an alias. Otherwise remove it from navigation/body.

## Ambiguity Handling

Do not upload first and explain later when project identity is unclear.

Ask before proceeding when:

- A candidate file is only loosely related by keyword.
- The PRD name and HTML page title point to different products.
- The same source folder contains two branded variants.
- A platform and a sub-tool both have materials.
- A project is listed in navigation but the local source suggests it was renamed or merged.
- The source folder contains upstream/reference projects plus a new H5 project. Sync only the new project's confirmed artifacts; do not archive reference PRDs as if they belonged to the new project.

Good question format:

```text
我找到两个候选：A 是独立 H5，B 是平台内工具。按资料看我建议把 B 并入 XX 平台，不单列。你确认这样处理吗？
```

## Merge And Split Rules

- Merge only when the user confirms or the source explicitly says one item is a tool/module inside another platform.
- Keep separate when they are separate merchants, products, H5s, admin systems, or delivery packages.
- Keep separate when one document is the H5/user product and another is the admin/self-operated product platform, even when the platform's first app is that H5.
- If a previously separate doc is now merged, do not delete it unless the user asks. Add a top/bottom note saying it has been merged and point to the canonical doc.
- Navigation should show only the canonical current project rows.

## PRD And HTML Rules

- PRD is source-of-truth for requirements. HTML is source-of-truth for visual/page coverage.
- This sync skill never creates the PRD or HTML. It only archives existing artifacts.
- HTML must be attached and rendered to an image preview when possible.
- If HTML cannot run/render, attach it and state preview generation failed.
- If only HTML exists, archive it as HTML-only and write "未找到独立 PRD".
- If only PRD exists, archive it as PRD-only and write "未找到 HTML 设计稿/原型".
- Never use an unrelated document because it has similar words in the file name.
- If the user needs a new H5/PRD generated first, switch to the relevant project-factory or PRD workflow, finish confirmation there, then return to this sync skill.

## Navigation Columns

Use these columns unless the existing Feishu navigation already has a better structure:

| 项目 | 飞书文档链接 | 已归档资料 | 待补充 |
|---|---|---|---|

Rules:

- "已归档资料" should say what actually exists: PRD, HTML, preview image, screenshots, code zip, deployment doc.
- "待补充" should say exactly what is missing or "无".
- Do not write fake completion such as "已完成" when a source is missing.

## Permission Default

Default sharing target:

- `external_access=true`
- `link_share_entity=anyone_readable`
- equivalent UI meaning: 获得链接的人可阅读

If the tool cannot verify because a read-only scope is missing, report the missing scope; do not claim verified permission.

## Verification Checklist

For each sync, verify the cheapest meaningful subset:

- target doc contains the confirmed project name
- target doc contains source file paths or source summary
- target doc contains missing-source notes when applicable
- navigation contains canonical row
- navigation does not contain stale duplicate row
- old names are absent unless intentionally kept as aliases
- media insert commands succeeded for preview image and HTML attachment
- share permission applied and verified where scope allows
