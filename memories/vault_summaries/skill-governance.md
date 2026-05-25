---
page_type: decision
created_at: "2026-05-18"
updated_at: "2026-05-19"
sensitivity: personal
source_ids: ["evoskill_article", "evoskill_repo", "skill_routing_audit"]
confidence: high
status: active
---

# Skill Governance

## Decision

The skill library must be governed as an active portfolio, not a collection. More skills are not automatically better.

Current observed local count:

- `C:\Users\skzjc\.codex\skills`: 35 `SKILL.md` files
- `C:\Users\skzjc\.agents\skills`: 26 `SKILL.md` files

Plugins add more callable skills beyond those local folders, so routing noise is a real risk.

## Adopted From EvoSkill

Useful ideas:

- skill growth should face selection pressure
- failed trajectories should produce proposals
- proposals should decide create vs edit existing skill
- skill candidates need isolated validation
- keep an archive of rejected proposals to avoid repeated bad ideas
- merge non-duplicate high-scoring skills; do not keep redundant variants

Deferred:

- full automated EvoSkill loop
- multi-branch autonomous skill mutation
- model-driven wholesale rewriting of global skills

Reason: the current environment lacks a stable benchmark suite, and unsafe automatic mutation could degrade global behavior.

## Operating Policy

1. Default to editing or merging existing skills.
2. Install or activate a new skill only when it has a unique role.
3. Keep large external projects as `reference` until a benchmark proves value.
4. Maintain active/reference/candidate/deprecated tiers.
5. Evaluate skill changes against task families, not single anecdotes.

## Near-Term Action

Created a lightweight portfolio:

`C:\Users\skzjc\.codex\private\knowledge-vault\config\skill-portfolio.jsonl`

Current classification:

- active: 29
- reference: 25
- candidate: 8
- total: 62

Next step before any large cleanup: create a small benchmark matrix and demote/merge skills based on real task outcomes.

## Trigger Regression Check

Created a lightweight trigger test set:

`C:\Users\skzjc\.codex\private\knowledge-vault\config\skill-trigger-tests.jsonl`

Created a checker:

`C:\Users\skzjc\.codex\private\knowledge-vault\scripts\check_skill_routing.py`

Current validation result on 2026-05-22:

- test cases: 27
- failures: 0
- warnings: 8

Warnings mean the route is recognized but the skill is intentionally not fully active yet, usually because it is `reference` or `candidate`. This prevents reference skills and design candidates from being falsely treated as validated default behavior.

2026-05-20 update: `open-design-design-systems` was promoted to active only for backend/admin UI and design-system-gated prototype work, after adding a specific trigger test and global rule. Other Open Design skills remain candidate until separately validated.

2026-05-22 update: `data-analysis-report` was added as an active mandatory route for professional data analysis reports, after SenseNova-Skills showed the missing workflow layer between file processing and decision-grade report delivery.
