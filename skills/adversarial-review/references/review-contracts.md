# Adversarial Review Contracts

## Black-Box Finding

| Field | Requirement |
|---|---|
| Journey | User goal and entry point |
| Severity | P0 blocking/data loss, P1 major failure, P2 confusion or recovery cost, P3 polish |
| Reproduction | Exact visible actions and test data |
| Evidence | Screenshot, visible state, timing, or repeatable result |
| Impact | What a first-time user cannot understand or complete |
| Correction | Product or interaction change, not speculative code unless implementation was inspected later |
| Retest | Passed, failed, or unverified on the same journey |

### Minimum Journey Set

- First entry and comprehension of the primary job.
- Primary successful flow from entry to result.
- Required input validation and recovery.
- Back, cancel, refresh, and re-entry state behavior.
- Empty, loading, error, timeout, and retry states when the product can reach them.
- Long text, small viewport, keyboard, fixed controls, and scrolling on H5/mobile.
- Permission, payment, destructive, or irreversible confirmation when applicable.

### Black-Box Acceptance

- No implementation inspection occurred before findings were frozen.
- Every promised critical journey has evidence or is explicitly unverified.
- Seeded P0/P1 defects are all detected in controlled tests.
- A fix pass reruns the exact same journey set.
- No claim of success is based only on rendering, screenshots, DOM presence, or code inspection.

## Red-Team Finding

| Field | Requirement |
|---|---|
| Assumption | The belief being treated as fact |
| Failure mechanism | How the assumption produces failure |
| Trigger | Observable condition that activates the failure |
| Cost | User, business, privacy, delivery, or maintenance consequence |
| Early signal | Evidence available before full investment |
| Falsification experiment | Smallest bounded test with a pass/fail threshold |
| Response | Proceed, narrow, pause, or redesign |

### Red-Team Acceptance

- The restated plan is accurate enough that its owner would recognize it.
- At least three material failure causes are source-backed or clearly labeled hypotheses.
- At least one simpler alternative is considered.
- Every blocking objection has a minimum falsification experiment and threshold.
- The final decision is singular and executable.
- A low-risk control prompt does not trigger a heavyweight review.
