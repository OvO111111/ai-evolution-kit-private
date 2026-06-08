---
name: feishu-prd-html-sync
description: "Use when the user asks to upload, sync, publish, archive, or update project materials into Feishu/Lark, including natural phrases like 上传飞书, 同步飞书, 飞书同步, 发布到飞书, 归档到飞书, 把资料放到飞书, or 更新飞书资料. Covers local project PRDs, Markdown specs, 方案 files, HTML prototypes, screenshots, handoff files, and project archive materials. For project-level sync, it must find local sources, resolve naming/alias conflicts, create or update Feishu docx archive pages, insert HTML preview images and attachments, update a navigation/index doc, set link-share read permissions, and verify no wrong merge or stale project name remains. Do not use for a simple one-off file upload with no project archive/navigation requirement; use lark-drive directly for that."
---

# Feishu PRD HTML Sync

Use this skill when the user wants existing local PRD,方案, Markdown, HTML prototype, screenshot, or project handoff materials published or synchronized to Feishu cloud documents.

This skill is source-first. Do not draft, upload, rename, or mark a project complete before inspecting the actual local source files and current Feishu target.

This is a sync/archive skill, not a project-generation skill. Do not create a new PRD, H5 prototype, admin prototype, module map, or product plan just because a source is missing. Missing source is a gap to report or clarify.

## Trigger Boundary

Trigger this skill for project-level Feishu upload/sync/archive requests, even when the user does not say "PRD" or "HTML" explicitly.

Natural triggers include:

- "上传飞书"
- "同步飞书"
- "飞书同步"
- "发布到飞书"
- "归档到飞书"
- "把资料放到飞书"
- "把这个项目同步/上传/发布到飞书"
- "更新飞书资料/项目资料/导航页"
- "把本地方案、PRD、HTML、原型、截图、交付包放到飞书"

Routing rule:

- If the request is about a project, project archive, PRD, 方案, HTML prototype, screenshot, handoff package, navigation/index doc, naming merge, or share-permission verification, use this skill first, then call `lark-doc`, `lark-drive`, and `lark-shared` as implementation skills.
- If the request is only "upload this one file to Feishu Drive" and there is no project archive, preview, navigation, naming, or verification requirement, use `lark-drive` directly and do not force this archive workflow.
- If the user says only "上传飞书" or "同步飞书" without enough context, inspect the current workspace and likely project sources first. Ask only if the target project/doc/folder cannot be inferred safely.

## Trigger Examples

- "把这个项目的 PRD 和 HTML 放到飞书"
- "上传飞书"
- "同步飞书"
- "发布到飞书"
- "归档到飞书"
- "把资料放到飞书"
- "把这个项目同步到飞书"
- "同步本地 PRD/HTML 到飞书"
- "更新项目资料导航页"
- "把 WorkBuddy 做的项目发布到飞书"
- "这个项目改名了，飞书里也同步一下"
- "HTML 也要能在飞书里看到页面效果"

## Required Companion Skills

- Use `pm-prd` before interpreting or rewriting PRD content.
- Use `lark-doc` for Feishu docx create/fetch/update/media insert.
- Use `lark-drive` for title, share permission, file metadata, and Drive-level actions.
- Use `lark-shared` when auth, scopes, identity, update notices, or permission errors appear.

## Core Rule

The Feishu archive must reflect real source material, not guessed project structure.

If local evidence is ambiguous, write a clear gap or ask the user. Never silently pick a random file and call it the PRD.

Fast path matters. Before doing Feishu writes, lock a small source map: project name, canonical Feishu doc, PRD path, HTML path, preview image path, navigation doc, and missing items. If this map cannot be built in two focused search passes, stop and ask with the candidate list.

## Workflow

1. **Lock The User Goal**
   - Identify whether this is a new archive, an update to an existing Feishu doc, a project rename, a merge/split correction, or navigation cleanup.
   - Treat the user's latest project name as the desired Feishu display name unless there is a conflict.
   - If the request mentions an H5/app-factory project whose HTML or PRD has not been confirmed, do not generate those artifacts here. Ask whether to sync only existing files or switch to the app-factory workflow.

2. **Inspect Current Feishu State**
   - Fetch the navigation/index doc if one exists.
   - Fetch any existing target project docs.
   - Check current project names, links, known gaps, and share status when possible.
   - If the target doc already has images or attachments, avoid full overwrite unless rebuilding the page and reinserting media is explicitly part of the plan.

3. **Find Local Sources**
   - Search likely roots first:
     - `C:\Users\skzjc\WorkBuddy`
     - `D:\xiaochengxu`
     - current workspace
   - Use bounded `rg --files` and then content search with project names, aliases, merchant names, page titles, and product display names.
   - Always exclude noisy/generated folders first: `node_modules`, `.git`, `dist`, `build`, `.next`, `coverage`, `__pycache__`, and large binary/media dumps unless the task is specifically about screenshots.
   - Search near known project folders before scanning all of `WorkBuddy` or all of `D:\xiaochengxu`.
   - Prefer source files over generated artifacts:
     - PRD/方案: `.md`, `.docx`, `.txt`, product specs
     - HTML prototype: `.html`
     - Handoff: README, deployment docs, code zip, screenshots

4. **Resolve Naming And Merge Boundaries**
   - The user's confirmed project name is the Feishu project name, even when file names use old names.
   - If old and new names both appear, sync to the user-confirmed name and record old names as aliases only when useful.
   - If two names may refer to the same project, platform, or tool, stop and ask before creating duplicate docs or merging docs.
   - If a project appears to be a tool inside a platform, ask whether to merge unless the source explicitly says it is part of that platform.
   - If multiple same-type projects share a template, do not merge them merely because they look similar. Keep separate docs unless the user confirms a merge.

5. **Build The Feishu Archive**
   - PRD/Markdown becomes Feishu正文.
   - HTML is attached as a file and also rendered to an image preview inserted into the doc.
   - Screenshots and code zips are inserted only when they are relevant handoff artifacts.
   - If a PRD is missing, say exactly what was searched and write "未找到独立 PRD" instead of inventing one.
   - If an HTML prototype is missing, write "未找到 HTML 设计稿/原型" instead of inserting an unrelated page.
   - Use `@file` content input for large Markdown/XML updates; do not paste long content into a shell command.
   - Use append or targeted replace for existing docs with media. Use overwrite only before media insertion or when the plan includes reinserting media.

6. **Update Navigation**
   - One independent product/system/H5/admin platform gets one row.
   - Tools inside a platform are merged into the platform row, not listed separately, once confirmed.
   - Keep columns practical: project, Feishu link, archived materials, missing items.
   - Remove stale standalone rows after confirmed merge.
   - Replace old display names in navigation after confirmed rename.

7. **Share Permissions**
   - Default target: "获得链接的人可阅读".
   - Apply and verify public/link share settings when the available scope allows it.
   - If permission verification needs a missing scope, report that specifically and continue validating body/link content.
   - Do not spend repeated cycles on the same missing scope. One failed verification plus the exact missing scope is enough unless the user completes auth.

8. **Verification**
   - Fetch target docs by keywords:
     - new project name
     - old project name
     - missing PRD/HTML note
     - inserted merge note
   - Fetch navigation by keyword to verify:
     - new name appears
     - stale standalone row is gone
     - old name is not present unless intentionally listed as alias
   - Verify HTML preview/image insertion and file attachment insertion by command result.
   - Verify share permissions where possible.
   - Stop verification after proving the user-visible result. Do not fetch entire docs repeatedly when keyword fetches prove the relevant rows/sections.

## Conflict Stop Conditions

Ask the user before uploading or changing navigation when any of these occur:

- Two or more candidate PRDs could plausibly belong to the project.
- The file name and product name disagree and there is no user-confirmed name.
- A project may be a platform sub-tool rather than an independent project.
- A similar project already exists in Feishu and the relation is unclear.
- The source only contains HTML, screenshots, or code docs, but no PRD.
- The project name changed and both old and new names still appear in active docs.
- Updating would delete, overwrite, or hide an existing Feishu doc rather than only adding a merge note or navigation correction.
- The user asks to "sync" but the only available next step would be generating a new PRD/HTML.
- A lark command fails twice with the same validation/auth/API error; diagnose or ask instead of retrying variants blindly.

When asking, ask one direct question with the exact candidates and the default recommendation.

## Output Standard

Final answer must state:

- whether the sync is complete, partial, or blocked
- which Feishu docs changed, with URLs
- which local sources were used
- which source files were missing or ambiguous
- what was verified
- any permission/scope limitation

Do not lead with command logs. Lead with the user-visible Feishu result.

## Efficient Lark Execution

Before running multiple Feishu writes, read `references/efficient-lark-runbook.md`. It contains the stable command patterns and known slow/error-prone areas: isolated Lark command execution, PowerShell JSON quoting, `docs +update --api-version v2`, media insertion, title patching, share permissions, and scoped verification.

## Detailed Standards

For project naming, merging, HTML previews, and navigation rules, read `references/project-sync-standard.md` when the task involves multiple projects, renamed projects, or any suspected duplicate/merge.
