# Four independent design-skill lanes

## Context

The user clarified that a request like `做4种不同设计方案` must not mean one design workflow producing several color/style variations. When the user names or implies `huashu-design`, `Product Design`, `open-design`, and `taste-skill`, the expected behavior is four independent design-method lanes.

## Adopted rule

- Route four-option design requests through `ui-product-design-router` four-lane comparison mode.
- Keep the lanes separate:
  - `huashu-design`: high-fidelity HTML visual artifact, bold visual direction, anti-slop exploration.
  - `Product Design`: brief/source gate first, then ideation/prototype/user-flow direction.
  - `open-design`: benchmark-backed design-system inheritance, tokens, density, components, state rules.
  - `taste-skill` / `design-taste-frontend`: anti-template taste correction, typography/layout/rhythm differentiation.
- Each option must label its skill lane and carry a distinct design thesis, information structure, and best-fit scenario. If all options share the same shell/card hierarchy and only differ by color, the comparison failed.

## Validation

Added a four-lane smoke artifact and reran `C:\Users\skzjc\.codex\design-skill-smoke\run-design-routing-smoke.ps1`.

Result on 2026-06-08 17:11 +08:00:
- `status`: passed
- `cases`: 6
- `skill_lane_count`: 4
- HTML: `C:\Users\skzjc\.codex\design-skill-smoke\four-skill-variants.html`
- Screenshot: `C:\Users\skzjc\.codex\design-skill-smoke\four-skill-variants.png`

## Boundary

This proves the routing rule and four-lane artifact structure, not that final production design quality is solved. Real project work still needs source inspection, actual user/task context, and screenshot/browser verification before claiming quality.
