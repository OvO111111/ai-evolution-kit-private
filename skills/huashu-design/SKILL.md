---
name: huashu-design
description: Use when the user explicitly names huashu, 花叔, or huashu-design; when the UI/product-design router selects Huashu as a distinct high-fidelity design lane; or when the requested deliverable is a visual HTML artifact, motion demo, HTML slide, infographic-style page, or image-led interactive prototype. Do not select for generic product planning, ordinary H5 work, routine admin redesign, or an ugly-UI complaint by itself.
metadata:
  upstream: https://github.com/alchaincyf/huashu-design
  upstream_ref: v2.0
  upstream_commit: 8a8d87d83b8dec767f37c05077732edb3ce5f903
  last_upstream_check: 2026-06-09
---

# Huashu Design

Adapted local entry for `alchaincyf/huashu-design`. Use this as a visual-artifact skill, not as a generic frontend implementation skill.

## Upstream Status

- Local resources are synced from upstream `v2.0` tag `8a8d87d83b8dec767f37c05077732edb3ce5f903`.
- This `SKILL.md` is intentionally compressed and adapted for Codex. Do not replace it with the upstream 57KB entrypoint.
- Future update checks must compare `upstream_ref` / `upstream_commit` with `git ls-remote --tags` and report whether a newer tag exists.

Portable export note: large demos, showcases, SFX, and BGM media are omitted from
the evolution backup. If a workflow needs those optional assets, fetch the pinned
upstream version recorded above. Code assets, references, and scripts remain portable.

## What This Owns

- High-fidelity HTML prototypes and visual mockups.
- Three-direction design exploration when the visual direction is unclear.
- HTML slides/decks, infographic pages, motion demos, and app/iOS prototype boards.
- Anti-AI-slop design review when output looks generic, templated, or weak.
- Brand/product asset discipline for named brands or real products.
- v2.0 additions: fact-check concrete product/version claims before designing, use design-direction advisor mode for vague asks, treat logo/product/UI screenshots as first-class assets, use Tweaks for variants, run Playwright screenshot/click verification, and use motion/video/audio pipelines only for animation deliverables.

Do not use this as the primary skill for production web apps, backend logic, SEO sites, or ordinary CRUD implementation. For dense admin/internal tools, use `admin-platform-execution-gate` first; Huashu can provide visual direction or review after the admin task model is clear.

## Required Route

Before producing a visual artifact, state:

```text
Design route: huashu-design + <other selected skills> because <artifact type>.
```

Then choose one workflow:

| Situation | Workflow |
|---|---|
| vague "make it look good", no visual source | design-direction advisor: create 3 distinct directions before final build |
| app/H5/prototype board | use HTML prototype workflow; for mobile/app mockups reuse `assets/ios_frame.jsx` or matching frame assets |
| HTML slides/deck | use `assets/deck_stage.js`; avoid webpage-like slide layouts |
| motion/animation demo | use `assets/animations.jsx`; write timeline before components |
| visual review | use `references/critique-guide.md` and report concrete design defects |
| named brand/product | use `references/core-asset-protocol.md` before designing |
| vague visual request with no reference | use `references/design-styles.md` and show 3 directions before final build |
| variant tuning / live alternatives | use `references/tweaks-system.md` |
| app/iOS prototype | use `references/design-context.md`, real assets, device frame assets, and a click-test plan |
| HTML animation export | use `references/video-export.md` and `references/audio-design-rules.md`; MP4/GIF/audio is not the default for static UI |

## Source And Asset Rules

- Start from existing context: screenshot, Figma, codebase, product reference, brand assets, or examples. If none exists, show 3 directions instead of inventing one final answer.
- If a real brand/product appears, logo/product imagery/UI screenshots are required assets unless unavailable after search.
- Honest placeholder beats fake detail. Do not invent screenshots, product imagery, or data to fill space.
- Avoid AI slop: generic purple gradients, emoji-as-icons, three-card filler rows, Inter-only display type, fake stats, and decorative dashboards.

## References To Load Only When Needed

- `references/workflow.md` for the original end-to-end workflow.
- `references/design-styles.md` for direction exploration.
- `references/design-context.md` when no source material exists and a taste anchor is needed.
- `references/tweaks-system.md` for real-time variants.
- `references/core-asset-protocol.md` for real brands/products and required assets.
- `references/critique-guide.md` for review.
- `references/slide-decks.md` and `references/editable-pptx.md` for HTML decks/PPTX.
- `references/animations.md`, `references/video-export.md`, and `references/audio-design-rules.md` for motion/video/audio.
- `references/v2-adoption-summary.md` for the local adoption boundary and update policy.
- `references/verification.md` before claiming a visual artifact is ready.

## Completion Gate

Do not claim success from code existence. For visual work, verify with a rendered screenshot or exported artifact when the environment allows it, then report the visible result first.
