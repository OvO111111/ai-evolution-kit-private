---
name: adversarial-review
description: Use for pure black-box product self-checks, first-time-user walkthroughs, red-team reviews, premortems, falsification tests, or requests to attack and disprove a plan before execution. Also use when a matching product/H5 or self-evolution skill invokes an adversarial gate for a high-impact workflow. Covers blind live-UI testing and plan stress-testing; do not use for routine unit tests, ordinary code review, small copy edits, or low-risk changes with an obvious reversible path.
---

# Adversarial Review

Challenge the work from outside its implementation assumptions. Select exactly one mode unless the user explicitly requests both.

## Mode Selection

- **Black-box walkthrough:** A runnable product, H5, admin, app, or website must be experienced as a first-time user without reading its implementation first.
- **Red-team plan review:** A consequential plan, architecture, rollout, product direction, or global Codex evolution change must be attacked before execution.

Read `references/review-contracts.md` for detailed evidence fields, severity definitions, and acceptance checks.

## Black-Box Walkthrough

1. Freeze a small test packet: user goal, live target, critical journeys, permitted test data, and action boundaries. Do not include source paths, implementation notes, intended fixes, or seeded defects.
2. Do not inspect source code, repository files, network internals, database state, or implementation plans before the first findings report is frozen. User-facing briefs and visible help text are allowed.
3. Use the real browser surface selected by `web-access`. Click, type, wait, navigate back, refresh, cancel, retry, and revisit through visible controls. Do not bypass the UI with direct state mutation.
4. Exercise the applicable first-use, primary-success, invalid-input, loading, empty, error, cancel, back, refresh, re-entry, and long-content paths. For H5, test a real `375px` or `390px` CSS viewport; `750px` is a handoff canvas, not the phone viewport.
5. Freeze findings before reading implementation. Each issue needs severity, exact reproduction, observed evidence, user impact, and a concrete correction direction. Distinguish a defect from an unverified path.
6. If the user requested fixes, only now inspect the implementation, diagnose root causes, make scoped changes, and rerun the exact frozen journeys. Report regressions and remaining unverified paths explicitly.

Do not call a page black-box verified because it rendered, a screenshot looked acceptable, or a scripted happy path passed.

## Red-Team Plan Review

Use this gate automatically only when failure would cause meaningful cost, privacy exposure, production impact, compliance risk, hard-to-reverse architecture, broad global behavior change, or substantial repeated-work overhead.

1. Restate the plan and its success condition accurately.
2. Assume the plan failed six months later. Identify at least three plausible causes grounded in the available sources.
3. Attack hidden assumptions, missing failure states, source or version drift, operational cost, scope optimism, reversibility, and whether a simpler path reaches the same goal.
4. For every material failure cause, provide its trigger, likely cost, earliest observable signal, and the smallest experiment that could disprove the plan.
5. End with one decision: `proceed`, `experiment first`, or `redesign`. Recommend one path instead of returning an option menu.

Do not manufacture objections to routine, low-cost, reversible work. A red-team review that cannot change the decision is ceremony, not quality control.

## Evaluation Integrity

- Record the baseline before changing the target skill, plan, or artifact.
- Keep the evaluator blind to the intended answer, suspected defect, author reasoning, and change diff.
- Compare baseline and variant on the same input and acceptance rubric.
- Treat route selection, static validation, artifact quality, and live behavior as separate evidence tiers.
- A passing validator cannot substitute for a fresh behavioral test.

## Completion

Black-box mode is complete only after journeys were actually exercised and evidenced. Red-team mode is complete only after a falsifiable recommendation is produced. When fixes follow a review, completion requires rerunning the same journeys or experiments and reporting the result.
