---
name: image-to-code-fallback
description: >
  Legacy fallback for implementing a visually important website from a supplied
  screenshot or reference image when the official Product Design image-to-code
  skill is unavailable. Do not use for ordinary frontend work, text-only briefs,
  admin-product planning, or when Product Design can be called.
---

# Image To Code Fallback

Use this only after confirming that the official `product-design:image-to-code`
route is unavailable or failed for a concrete technical reason.

## Required Inputs

- The actual reference image or screenshot.
- The target repository and runnable frontend entry point.
- Any existing design system, assets, fonts, and responsive constraints.

If the reference image is missing, ask for it. Do not invent a visual target and
call the result image-to-code.

## Workflow

1. Inspect the repository, existing UI conventions, and the reference at original
   resolution.
2. Decompose the reference into layout, spacing, typography, color, imagery,
   components, states, and responsive behavior.
3. Reuse existing assets and components when they match. Use real or generated
   bitmap assets when the reference depends on imagery.
4. Implement the smallest complete vertical slice, then render it at the reference
   viewport and at one narrow viewport.
5. Compare screenshots visually and check for clipping, overlap, blank media,
   missing states, and major spacing or type mismatches.
6. Iterate until the implementation is recognizably faithful, then run the
   repository's cheapest meaningful tests.

## Completion Evidence

Report the rendered result first, then the implementation files and tests. Do not
claim fidelity without screenshot evidence.

## Full Reference

Open `references/full-guide.md` only when the concise workflow is insufficient for
a specific implementation detail. Do not load it by default.
