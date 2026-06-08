---
name: huashu-design
description: Use when the user names huashu, 花叔, huashu-design, asks for high-fidelity HTML visual artifacts, interactive prototypes, HTML slides, motion demos, design variants, visual direction exploration, iOS/app mockups, infographic-style HTML, design review, anti-AI-slop critique, or says prior design output is generic, ugly, student-like, or did not use design skills.
---

# Huashu Design

Adapted local entry for `alchaincyf/huashu-design`. Use this as a visual-artifact skill, not as a generic frontend implementation skill.

## What This Owns

- High-fidelity HTML prototypes and visual mockups.
- Three-direction design exploration when the visual direction is unclear.
- HTML slides/decks, infographic pages, motion demos, and app/iOS prototype boards.
- Anti-AI-slop design review when output looks generic, templated, or weak.
- Brand/product asset discipline for named brands or real products.

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
| named brand/product | use `references/brand-asset-protocol.md` before designing |

## Source And Asset Rules

- Start from existing context: screenshot, Figma, codebase, product reference, brand assets, or examples. If none exists, show 3 directions instead of inventing one final answer.
- If a real brand/product appears, logo/product imagery/UI screenshots are required assets unless unavailable after search.
- Honest placeholder beats fake detail. Do not invent screenshots, product imagery, or data to fill space.
- Avoid AI slop: generic purple gradients, emoji-as-icons, three-card filler rows, Inter-only display type, fake stats, and decorative dashboards.

## References To Load Only When Needed

- `references/workflow.md` for the original end-to-end workflow.
- `references/design-styles.md` for direction exploration.
- `references/brand-asset-protocol.md` for real brands/products.
- `references/critique-guide.md` for review.
- `references/slide-decks.md` and `references/editable-pptx.md` for HTML decks/PPTX.
- `references/animations.md`, `references/video-export.md`, and `references/voiceover-pipeline.md` for motion/video.
- `references/verification.md` before claiming a visual artifact is ready.

## Completion Gate

Do not claim success from code existence. For visual work, verify with a rendered screenshot or exported artifact when the environment allows it, then report the visible result first.
