---
name: ui-product-design-router
description: Route UI and product-design work before implementation. Use for design, redesign, visual audit, prototypes, HTML mockups, H5 pages, admin/back-office screens, dashboards, internal tools, screenshot/URL/Figma recreation, multi-option design requests, explicit huashu or Product Design requests, and complaints that an interface is ugly, generic, structurally wrong, or ignored its references. Company H5 patterns are selected only when the company project family is explicitly named or the workspace matches it.
---

# UI Product Design Router

This skill chooses a design workflow. It is not another visual style and must not make every output look alike.

## Route Gate

Before editing UI:

1. Inspect the supplied sources, existing product, screenshots, PRD, or URL.
2. Classify the task by product surface and deliverable.
3. Select the smallest matching skill set below.
4. Continue through the selected workflow in the same turn unless a real product decision or an explicit review checkpoint requires the user.

Do not ask the user to name a skill or recite a trigger phrase. Natural requests must route correctly.

## Routes

### Company H5 Factory

Use `app-factory-h5-admin` only when at least one scope signal exists:

- the user names 声之境, 每周穿搭, 自营产品管理平台, 统一后台, or the company H5 factory;
- the workspace is part of that company project family;
- the user explicitly asks to reuse that company's H5/admin pattern.

Do not use it for generic, personal, client, open-source, or unrelated H5 work.

### Admin And Internal Tools

Use `admin-platform-execution-gate` first. It must establish the operator job, page model, reference family, decision metrics, interaction states, and verification plan, then continue into implementation in the same stage.

Use Product Design only when the main goal is visual exploration, flow audit, source cloning, or a selected visual implementation. Use `open-design-design-systems` as a reference system only when its benchmark fits the product; do not apply a generic dark Linear-like shell by default.

### Generic H5 And Product Screens

For generic, personal, client, open-source, or otherwise unrelated H5/product-screen work, use Product Design `index` as the primary route. With no visual target, continue through `get-context -> ideate`; after the user selects a direction, use `image-to-code` and `design-qa` as applicable.

Do not select `app-factory-h5-admin` or inherit company product facts. Do not select `huashu-design` as the primary route for an ordinary product H5 unless the user explicitly asks for a high-fidelity visual artifact, direction board, motion demo, or Huashu method.

After this router selects generic H5/product work, immediately load Product Design `index` and the focused skill it selects. Returning or implementing with only `ui-product-design-router` is an incomplete route.

### Product Design Plugin

Use Product Design `index` when Product Design is explicitly requested or the main goal is design exploration, UX audit, faithful source cloning, or prototype sharing. Let the current plugin index route to its focused skills:

- `audit` for an existing flow or experience;
- `get-context` then `ideate` when no visual target exists;
- `url-to-code` for a faithful live-URL clone;
- `image-to-code` for a selected screenshot, mockup, Figma frame, or generated option;
- `design-qa` after implementation when both target and rendered output exist;
- `share` only when the user asks to publish or share.

If the brief already contains a clear target and user outcome, play back assumptions briefly and continue. Do not create a question-only turn.

### Huashu

Use `huashu-design` for high-fidelity HTML visual artifacts, direction boards, motion demos, infographic-like pages, decks, or bold visual exploration. It does not replace product structure, admin information architecture, or production implementation.

### Public Sites And Frontend Taste

Use `design-taste-frontend` or `redesign-existing-projects` for public landing pages, portfolios, marketing sites, and visual polish. Do not route dense admin tooling through landing-page composition.

## Multi-Option Mode

When the user asks for several genuinely different design options, independent lanes are required. For a four-option request, use these four lanes when they fit:

| Lane | Method | Distinctive responsibility |
|---|---|---|
| A | `huashu-design` | authored composition and strong visual direction |
| B | Product Design | different flow, interaction, and state model |
| C | `open-design-design-systems` | different real benchmark, tokens, density, and component grammar |
| D | `design-taste-frontend` | typography, hierarchy, layout rhythm, and anti-template correction |

All lanes share the same confirmed business facts, but must differ in at least four of these: information architecture, primary interaction, navigation model, composition, density, typography, color system, content hierarchy, and state presentation. Recoloring one shell is a failed comparison.

For admin work, establish one page-task matrix first, then let each lane solve it differently. For company H5 work, keep the H5-before-admin-before-PRD stage order.

Load each lane's main `SKILL.md`, but use progressive disclosure: read only the references/assets required for that lane's artifact. Do not load every appendix from every design skill before producing the lane briefs.

## Completion Gate

Do not report a design as complete until:

- sources and selected references are named;
- the main user job is visible in the first viewport;
- primary actions and page relationships are coherent;
- empty, loading, error, permission, and long-content states are considered;
- visible controls are functional or explicitly unavailable;
- desktop and mobile screenshots were inspected where applicable;
- a source-target comparison or design QA was run for fidelity-sensitive work.

Build success and a single screenshot are evidence, not the acceptance result.
