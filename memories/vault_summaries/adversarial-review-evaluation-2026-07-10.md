# Adversarial Review Evaluation

## Source Decision

| Method | Decision | Reason |
|---|---|---|
| Pure black-box walkthrough | Adopt | Existing checks could prove routing, source contracts, and rendering, but not first-time-user success without implementation bias. |
| Red-team/premortem | Adopt conditionally | Valuable before costly or broad decisions; wasteful for routine reversible work. |
| Generic execution prompt | Do not duplicate | Current operating rules already require direct action, smallest sufficient work, evidence, limited pauses, and result-first reporting. |
| Four-model orchestration | Defer | No current comparison proves better quality after latency, token, context-isolation, and integration cost. |

## Before/After Evidence

| Layer | Baseline | After | Result |
|---|---|---|---|
| Natural black-box request | Model selected a browser and described a plausible walkthrough, but no reusable review contract owned evidence, severity, blind-state freeze, or same-journey retest. | `adversarial-review` selected and opened with `web-access`; ordered actions froze the test packet and findings before code, then required same-journey regression. | Pass |
| Evolution red team | `absorb-lessons` could reason adversarially, but the behavior was not a stable reusable gate. | Fresh session selected and opened both `adversarial-review` and `absorb-lessons`, produced a falsification comparison and `redesign` decision. | Pass |
| Low-risk control | No formal guarantee against over-triggering. | Reversible copy edit selected only `playwright`; `adversarial-review` remained excluded. | Pass |
| Company H5 checkpoint | H5 workflow required functional and screenshot checks but no implementation-blind user acceptance. | Fresh session opened `app-factory-h5-admin`, `adversarial-review`, and `web-access`, then stopped at H5 confirmation after blind freeze/fix/retest. | Pass |

## Blind H5 Artifact Test

The evaluator ran in an empty working directory and received only the URL, user goal, viewport, journey list, and output contract. It did not receive source paths, intended fixes, or seeded defects.

| Run | Browser calls | Result |
|---|---:|---|
| Broken fixture | 30+ | Found all five seeded defect families: incomplete success closure, delayed plan validation, weak contact validation, stale error state, and 390px overflow. |
| First fixed fixture | 58 | Confirmed the five fixes, then found a new P1: browser/system back exited the H5 because business steps did not enter history. |
| Final fixed fixture | 33 | Completed first-use, success, invalid-input, page-back, browser-back, refresh, re-entry, mobile layout, and keyboard journeys; `findings=[]`, `verdict=pass`. |

Network failure, empty-list, offline, real mobile soft-keyboard, and server-side idempotency remained explicitly unverified because the visible fixture could not trigger them.

## Cost Boundary

Full blind browser walkthroughs took several minutes per run. Keep them at H5/admin confirmation, release, major redesign, and serious regression gates. Do not run them for every small reversible edit.

## Export-Safety Regression

A mechanical copy of local project-derived skills into the public export produced 25 safety findings, including private paths, a document URL, and contact values. `check_export_safety.py` blocked the operation before staging. The public skills were converted back to placeholder-based projections, the scan returned zero findings, and weekly sync now forbids recursive overwrite of curated project-derived skill copies.

The scanner was then red-teamed against JSON serialization. Its Windows-path rule matched only normal backslashes and missed JSON/JSONL escaped paths. After the rule was corrected, it exposed 316 personal-path findings across four historical artifacts. Three superseded or project-specific detailed reports were removed; the skill portfolio was retained with portable `%USERPROFILE%` roots. The final corrected scan covered 286 candidate text files with zero findings.

The recovery script was also tested in a temporary Codex home. It installed the public projection on an empty target, then preserved a marker inside an existing private `app-factory-h5-admin` copy on the second run. This prevents public placeholders from replacing richer private local context.
