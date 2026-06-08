# Design skill smoke test result

User asked whether the design-related skills were actually fixed and tested after repeated poor design output in other threads.

Result:
- Prior to this turn, the fix had only validated installation/frontmatter/routing files, not visual output quality.
- A smoke test was created and run under `C:\Users\skzjc\.codex\design-skill-smoke`.
- Test cases cover admin redesign, Huashu high-fidelity H5, Product Design screenshot prototype, company H5 factory, and landing anti-template routing.
- A rendered HTML smoke artifact was created: `admin-three-directions.html`.
- Chrome headless screenshot was created: `admin-three-directions.png`.
- Repeat script passed: `run-design-routing-smoke.ps1`.

What the smoke test proves:
- The corrected route can produce three structurally different admin design directions rather than three cosmetic variants.
- The route explicitly uses `ui-product-design-router + admin-platform-execution-gate + open-design-design-systems + huashu-design`.

What it does not prove:
- It does not guarantee all future design work will be good.
- It does not prove already-open old Codex windows see newly added skills; restart/new window may be needed.
- It does not fully exercise Product Design end-to-end because that requires a live brief confirmation and selected visual target.

Durable rule:
- When user challenges whether design skills are working, report the exact verification tier: installed, current-session visible, trigger-route, `SKILL.md` loaded, rendered artifact, screenshot/QA. Do not collapse these into a single "works".
