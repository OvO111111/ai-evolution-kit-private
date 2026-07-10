# Adversarial review evolution

Source: `https://mp.weixin.qq.com/s/AabBvPiRxmfhHBX3oztZ_w`

The article was read in full through logged-in Chrome. Adopted: pure black-box first-time-user walkthroughs and red-team/premortem review with minimum falsification experiments. Not duplicated: the generic execution prompt already exists in current operating rules. Deferred: four-model orchestration until it wins a bounded cost, isolation, and quality comparison.

Implemented:

- `adversarial-review` with black-box and red-team modes.
- Conditional red-team and blind H5/operator checkpoints in `app-factory-h5-admin`.
- Live black-box readiness evidence in `project-prd-h5-audit`.
- Conditional red-team Solution Plan gate in `pm-prd`.
- Blind before/after and evidence-tier separation in `absorb-lessons`.
- No new skill registry text in global `AGENTS.md`.

Validation:

- Five skills passed `quick_validate.py`; 33 static contracts passed.
- Fresh sessions selected and opened the new skill for generic black-box review, global-evolution red team, and the company-H5 checkpoint; a low-risk copy edit did not select it.
- Blind H5 run 1 found five seeded defects without reading implementation.
- Blind H5 run 2 found a new P1 browser-back defect after the first fixes.
- Blind H5 run 3 passed the same journey family with zero findings; unreachable network/empty-list paths remained explicitly unverified.
- A raw project-skill copy reintroduced 25 private/company findings. The safety gate blocked upload, public copies were re-sanitized to placeholders, and weekly sync was changed from mirror behavior to curated project-skill projections.
- The scanner was also corrected for JSON/JSONL-escaped Windows paths. It then exposed 316 personal-path findings in four old artifacts; superseded/private-project reports were removed and the 78-item skill portfolio was converted to portable `%USERPROFILE%` roots. The final stronger scan covered 286 files with zero findings.

Scope: run heavyweight black-box review at meaningful product confirmation/release gates, not every small change. Skip red-team ceremony for low-cost reversible work.
