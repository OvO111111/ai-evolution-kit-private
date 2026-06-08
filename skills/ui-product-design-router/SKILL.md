---
name: ui-product-design-router
description: Use when the user asks to design, redesign, audit, improve, prototype, or build UI, product screens, HTML mockups, H5 pages, admin/back-office pages, dashboards, internal tools, mentions huashu, 花叔, Product Design, design skills, or says an interface is ugly, generic, structurally wrong, not following references, or design skills did not trigger.
---

# UI Product Design Router

This is a router, not a design system. Its job is to prevent UI/product work from falling through to generic HTML or CSS edits.

## Required First Move

Before drafting, coding, or reporting completion, decide the route and say it in one short line:

```text
Design route: <selected skills> because <task family>.
```

Then open the selected skill files and follow them.

## Four-Lane Comparison Mode

When the user asks for `4种不同设计方案`, `四个设计方向`, `4 versions`, `four variants`, or asks whether `huashu-design`, Product Design, Open Design, and taste-skill can each produce a different option, do not merge the skills into one route.

Use four independent lanes:

| Lane | Skill | Owns | Must Look Different By |
|---|---|---|---|
| A | `huashu-design` | high-fidelity HTML visual artifact, bold direction board, anti-slop visual exploration | composition, visual temperature, artifact framing, stronger visual authorship |
| B | Product Design `index -> get-context -> ideate/prototype` | product-flow clarity, brief-confirmed prototype direction, user goal and interaction model | flow model, interaction assumptions, screen/state coverage |
| C | `open-design-design-systems` | benchmark-backed design system adaptation | chosen real reference, tokens, density, component rules |
| D | `design-taste-frontend` | anti-template taste correction for landing/redesign/frontend surfaces | typography, palette discipline, layout variance, cliché removal |

Output requirements:

- Label each option with its lane and skill source.
- Give each lane a distinct design thesis, not only a color change.
- If the task is admin/internal tooling, run `admin-platform-execution-gate` before all lanes and constrain every lane to the same page-task matrix.
- If the task is company H5/app factory, run `app-factory-h5-admin` first and constrain all lanes to H5-first sequence.
- Product Design lane may stop at brief/playback if missing visual target or user confirmation is required; do not fake completed Product Design output.
- If all four options share the same shell, card structure, typography scale, and information hierarchy, the comparison failed.

## Route Order

1. **Company H5/app-factory work**
   - Trigger words: `新H5`, `H5项目`, `项目工厂`, `声之境`, `每周穿搭`, company H5 prototype, reusable app factory.
   - Use `app-factory-h5-admin` first.
   - Sequence: inspect references -> analyze/split/ask blocking questions -> H5 750px prototype -> backend/admin scope -> PRD last.
   - Product Design is secondary only for visual exploration or selected visual implementation.

2. **Admin/internal tool/backend UI**
   - Trigger words: admin, backend, internal tools, dashboard, back-office, management console, table, permissions, monitoring, ugly admin UI.
   - Use `admin-platform-execution-gate` first.
   - If the user wants a new visual direction, also use Product Design `index` -> `get-context` before implementation.
   - Do not patch CSS repeatedly after strong rejection; reset from a reference packet.

3. **Product Design plugin workflow**
   - Trigger words: product UI, app screen, flow, prototype, redesign, clone, Figma, screenshot, URL-to-code, image-to-code, visual options, design QA.
   - Use Product Design `index` first, then `get-context`.
   - Do not build before the brief is confirmed unless the exact brief is already confirmed in the thread.
   - If there is no visual target, run ideation and show options before implementation.

4. **Huashu high-fidelity HTML visual artifacts**
   - Trigger words: huashu, 花叔, high-fidelity HTML, hi-fi design, HTML visual artifact, design variants, visual direction, iOS/app mockup board, HTML slides, motion demo, infographic, anti-AI-slop review.
   - Use `huashu-design` when the deliverable is a polished visual artifact, prototype board, HTML deck, motion demo, or design-direction exploration rather than production app code.
   - For admin/internal tools, keep `admin-platform-execution-gate` first, then use `huashu-design` only for visual direction/review after the page task model is clear.

5. **Landing/marketing/frontend taste**
   - Trigger words: landing page, portfolio, marketing page, homepage redesign, visual polish for a public site.
   - Use `design-taste-frontend` or `redesign-existing-projects`.
   - Do not use these as the main route for dense admin dashboards.

## Failure Checks

If any of these are true, routing failed:

- No skill name was announced before UI/product work.
- A design/build starts without reading source references or confirming a brief.
- A backend/admin page is treated like a marketing landing page.
- Product Design is discussed as "installed or not" instead of running `index` and `get-context`.
- Huashu is mentioned but `huashu-design` is not opened, or its assets/references are not used for visual artifacts.
- Final report lists files/tests first while the user asked whether the UI/product requirement was satisfied.

## Natural Trigger Examples

- "这个后台太丑，重新设计"
- "做一个 H5 HTML 原型"
- "照这个截图做页面"
- "这个页面结构不合理"
- "为什么 Product Design 没触发"
- "为什么 huashu skill 没用上"
- "你那些设计 skill 为什么没用上"
- "先看参考项目，再做类似的新项目"
