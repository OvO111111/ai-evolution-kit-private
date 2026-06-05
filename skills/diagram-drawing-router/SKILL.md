---
name: diagram-drawing-router
description: Route diagram and visual-structure requests to the right drawing technology. Use when the user asks to draw a diagram, flowchart, architecture map, relationship map, process chart, whiteboard, editable Feishu/Lark board, report graphic, presentation graphic, or asks which drawing method/tool should be used.
---

# Diagram Drawing Router

Use this skill before drawing diagrams. Decide the real delivery surface first, then call the smallest matching tool/skill.

## Default Decision

If the user says "画图" and does not specify a format:

1. If the result should be editable in Feishu/Lark or reused in Feishu docs, use `lark-whiteboard`.
2. If the result is a quick structural explanation in chat or docs, use Mermaid.
3. If the result is a polished report/presentation/web image, create an SVG/HTML/canvas artifact first, verify visually, then optionally embed/export it.
4. If the result needs realistic imagery or visual art, use image generation or canvas/SVG design skills, not Mermaid.

## Technology Routing

| Need | Default technology | Why |
|---|---|---|
| Fast flowchart, sequence, state, class, ER, gantt, mind map | Mermaid | Low cost, editable text, good enough for structure |
| Editable Feishu/Lark board, collaborative process map | Feishu whiteboard + Mermaid | Fastest route into an editable Feishu document |
| More controlled editable Feishu board | Feishu whiteboard + DSL/raw OpenAPI | Coordinates, connectors, dashed lines, node sizing are controllable |
| Polished business/report diagram | SVG or HTML/CSS/SVG | Better typography, layout, color, and export control |
| Frontend prototype or dashboard diagram | Actual HTML/React UI | The diagram should match the eventual product surface |
| Poster, visual metaphor, image-first graphic | Raster image generation/canvas | Mermaid/whiteboard are wrong tools |
| Existing image/screenshot to recreate | `image-to-code` or redesign skill | Inherit visual reference instead of inventing |

## Feishu Whiteboard Rules

- Use the user's default whiteboard document when no target document is specified: `https://my.feishu.cn/docx/OPSMdhe4wotBfWxuFqMc0v6WnqV`.
- For fast editable skeletons: write Mermaid to the existing default whiteboard.
- For polished editable Feishu boards: create a new blank whiteboard block, generate DSL JSON, render/check locally with `@larksuite/whiteboard-cli`, convert to OpenAPI JSON without UTF-8 BOM, then write once with `lark-cli whiteboard +update --input_format raw`.
- Do not rely on repeated raw/DSL `--overwrite` on the same board; it has produced Feishu placeholder exports in validation.
- Avoid connector auto-labels when they may overlap; prefer fewer labels or independent text nodes.
- If `lark-cli` reports Hermes binding guard because `HERMES_HOME` is set, temporarily clear `HERMES_HOME` only for that command and restore it afterwards.

## Quality Gate

Before claiming a diagram is done:

- Verify the target artifact exists: Feishu doc/whiteboard, local image, HTML, PPT, or SVG.
- For Feishu boards, export a preview image and inspect it.
- For DSL/SVG/HTML, check for text overflow, node overlap, incoherent crossings, and unreadable labels.
- Report the result by outcome first: where the diagram is, whether it is editable, and what limitations remain.

## Tool Calls

- Feishu/Lark editable output: open `lark-whiteboard` and `lark-shared`, then use `lark-cli`.
- Local polished output: use SVG/HTML/canvas generation and browser/image preview.
- Web/product UI output: use frontend/admin/design skills as appropriate, then browser screenshot verification.
