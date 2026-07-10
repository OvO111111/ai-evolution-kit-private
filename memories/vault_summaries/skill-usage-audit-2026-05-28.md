---
page_type: audit
created_at: "2026-05-28"
status: active
---

# Skill Usage Audit 2026-05-28

## Scope

- Sessions root: `%USERPROFILE%\.codex\sessions`
- Session files scanned: 16
- Records scanned: 26785
- Skills discovered: 65
- Cutoff: `2026-05-28T06:28:39.804Z`

Counting rule: `skill_file_reads` is strongest evidence because it means a historical turn opened or referenced a concrete `SKILL.md` path in tool arguments. Assistant/user mentions are secondary evidence and can include discussion rather than execution.

## Summary

- Active skills: 22
- Active skills with zero strong/assistant evidence: 0
- All skills with zero evidence: 29

## Top Evidence

| Skill | Tier | SKILL.md reads | Assistant mentions | Tool arg mentions |
|---|---:|---:|---:|---:|
| `pm-prd` | active | 7 | 37 | 67 |
| `open-design-design-systems` | active | 5 | 16 | 62 |
| `web-access` | active | 4 | 25 | 78 |
| `data-analysis-report` | active | 4 | 6 | 19 |
| `wechat-work-context` | active | 3 | 7 | 42 |
| `absorb-lessons` | active | 2 | 21 | 58 |
| `wechat-pay-product-design` | active | 2 | 4 | 21 |
| `agent-reach` | active | 1 | 26 | 99 |
| `desktop-control` | active | 1 | 9 | 36 |
| `design-taste-frontend` | active | 1 | 5 | 11 |
| `admin-platform-execution-gate` | active | 1 | 5 | 10 |
| `image-to-code` | active | 1 | 4 | 11 |
| `redesign-existing-projects` | active | 1 | 4 | 9 |
| `imagegen` | reference | 1 | 1 | 6 |
| `browser` | active | 0 | 30 | 159 |
| `docx` | active | 0 | 30 | 141 |
| `pdf` | active | 0 | 14 | 43 |
| `caveman` | reference | 0 | 10 | 24 |
| `xlsx` | active | 0 | 8 | 65 |
| `pptx` | active | 0 | 6 | 24 |

## Active Skills With Zero Strong/Assistant Evidence

- None

## All Skill Rows

| Skill | Folder | Tier | SKILL.md reads | Assistant | User | Tool args |
|---|---|---:|---:|---:|---:|---:|
| `absorb-lessons` | `absorb-lessons` | active | 2 | 21 | 9 | 58 |
| `admin-platform-execution-gate` | `admin-platform-execution-gate` | active | 1 | 5 | 0 | 10 |
| `agent-reach` | `agent-reach` | active | 1 | 26 | 13 | 99 |
| `browser` | `browser-harness` | active | 0 | 30 | 34 | 159 |
| `data-analysis-report` | `data-analysis-report` | active | 4 | 6 | 3 | 19 |
| `design-taste-frontend` | `design-taste-frontend` | active | 1 | 5 | 0 | 11 |
| `desktop-control` | `desktop-control` | active | 1 | 9 | 9 | 36 |
| `docx` | `docx` | active | 0 | 30 | 13 | 141 |
| `image-to-code` | `image-to-code` | active | 1 | 4 | 0 | 11 |
| `lark-doc` | `lark-doc` | active | 0 | 1 | 1 | 31 |
| `lark-drive` | `lark-drive` | active | 0 | 1 | 0 | 8 |
| `ocr-and-documents` | `ocr-and-documents` | active | 0 | 3 | 4 | 13 |
| `open-design-design-systems` | `open-design-design-systems` | active | 5 | 16 | 4 | 62 |
| `pdf` | `pdf` | active | 0 | 14 | 12 | 43 |
| `pm-prd` | `pm-prd` | active | 7 | 37 | 10 | 67 |
| `pptx` | `pptx` | active | 0 | 6 | 4 | 24 |
| `redesign-existing-projects` | `redesign-existing-projects` | active | 1 | 4 | 0 | 9 |
| `video-frames` | `video-frames` | active | 0 | 2 | 1 | 7 |
| `web-access` | `web-access` | active | 4 | 25 | 15 | 78 |
| `wechat-pay-product-design` | `wechat-pay-product-design` | active | 2 | 4 | 0 | 21 |
| `wechat-work-context` | `wechat-work-context` | active | 3 | 7 | 9 | 42 |
| `xlsx` | `xlsx` | active | 0 | 8 | 10 | 65 |
| `open-design-brand-guidelines` | `open-design-brand-guidelines` | candidate | 0 | 0 | 0 | 0 |
| `open-design-canvas-design` | `open-design-canvas-design` | candidate | 0 | 0 | 0 | 1 |
| `open-design-color-expert` | `open-design-color-expert` | candidate | 0 | 0 | 0 | 0 |
| `open-design-creative-director` | `open-design-creative-director` | candidate | 0 | 0 | 0 | 1 |
| `open-design-design-review` | `open-design-design-review` | candidate | 0 | 1 | 0 | 5 |
| `open-design-frontend-design` | `open-design-frontend-design` | candidate | 0 | 0 | 0 | 5 |
| `open-design-image-enhancer` | `open-design-image-enhancer` | candidate | 0 | 0 | 0 | 0 |
| `open-design-screenshots-marketing` | `open-design-screenshots-marketing` | candidate | 0 | 0 | 0 | 0 |
| `cavecrew` | `cavecrew` | reference | 0 | 1 | 0 | 6 |
| `caveman` | `caveman` | reference | 0 | 10 | 10 | 24 |
| `caveman-commit` | `caveman-commit` | reference | 0 | 1 | 0 | 3 |
| `caveman-compress` | `caveman-compress` | reference | 0 | 3 | 0 | 13 |
| `caveman-help` | `caveman-help` | reference | 0 | 1 | 0 | 3 |
| `caveman-review` | `caveman-review` | reference | 0 | 1 | 0 | 3 |
| `caveman-stats` | `caveman-stats` | reference | 0 | 1 | 0 | 4 |
| `imagegen` | `imagegen` | reference | 1 | 1 | 0 | 6 |
| `lark-approval` | `lark-approval` | reference | 0 | 0 | 0 | 1 |
| `lark-attendance` | `lark-attendance` | reference | 0 | 0 | 0 | 1 |
| `lark-base` | `lark-base` | reference | 0 | 0 | 0 | 20 |
| `lark-calendar` | `lark-calendar` | reference | 0 | 0 | 0 | 1 |
| `lark-contact` | `lark-contact` | reference | 0 | 0 | 0 | 1 |
| `lark-event` | `lark-event` | reference | 0 | 0 | 0 | 1 |
| `lark-im` | `lark-im` | reference | 0 | 0 | 1 | 2 |
| `lark-mail` | `lark-mail` | reference | 0 | 0 | 0 | 1 |
| `lark-markdown` | `lark-markdown` | reference | 0 | 0 | 0 | 1 |
| `lark-minutes` | `lark-minutes` | reference | 0 | 0 | 0 | 2 |
| `lark-okr` | `lark-okr` | reference | 0 | 0 | 0 | 1 |
| `lark-openapi-explorer` | `lark-openapi-explorer` | reference | 0 | 0 | 0 | 1 |
| `lark-shared` | `lark-shared` | reference | 0 | 0 | 1 | 6 |
| `lark-sheets` | `lark-sheets` | reference | 0 | 0 | 0 | 1 |
| `lark-skill-maker` | `lark-skill-maker` | reference | 0 | 0 | 0 | 1 |
| `lark-slides` | `lark-slides` | reference | 0 | 0 | 0 | 1 |
| `lark-task` | `lark-task` | reference | 0 | 0 | 0 | 1 |
| `lark-vc` | `lark-vc` | reference | 0 | 0 | 0 | 1 |
| `lark-vc-agent` | `lark-vc-agent` | reference | 0 | 0 | 0 | 1 |
| `lark-whiteboard` | `lark-whiteboard` | reference | 0 | 0 | 0 | 1 |
| `lark-wiki` | `lark-wiki` | reference | 0 | 0 | 0 | 3 |
| `lark-workflow-meeting-summary` | `lark-workflow-meeting-summary` | reference | 0 | 0 | 0 | 1 |
| `lark-workflow-standup-report` | `lark-workflow-standup-report` | reference | 0 | 0 | 0 | 1 |
| `openai-docs` | `openai-docs` | reference | 0 | 1 | 0 | 3 |
| `plugin-creator` | `plugin-creator` | reference | 0 | 0 | 0 | 2 |
| `skill-creator` | `skill-creator` | reference | 0 | 3 | 1 | 47 |
| `skill-installer` | `skill-installer` | reference | 0 | 2 | 0 | 8 |

