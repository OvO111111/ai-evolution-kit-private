# Huashu v2.0 update gap

## What happened

The user asked whether `huashu-design` had updated to `2.0` and whether the weekly updater detected it.

Live check found upstream tag `v2.0` at commit `8a8d87d83b8dec767f37c05077732edb3ce5f903`.

The prior weekly capability refresh did not detect this because the local `huashu-design` skill was an adapted copy without `.git` metadata or `upstream_ref` / `upstream_commit` metadata. The weekly check covered official plugins, npm global tools, and visible skills, but not manually adapted external skills with upstream tags.

## Fix applied

- Synced local `C:\Users\skzjc\.codex\skills\huashu-design` resources from upstream `v2.0`.
- Preserved the local compressed `SKILL.md` instead of replacing it with the upstream 57KB entrypoint.
- Added frontmatter metadata: `upstream`, `upstream_ref: v2.0`, `upstream_commit`, and `last_upstream_check`.
- Added `references/v2-adoption-summary.md` to capture what was adopted and constrained locally.
- Reran `C:\Users\skzjc\.codex\design-skill-smoke\run-design-routing-smoke.ps1`; result passed with `skill_lane_count: 4`.

## Durable rule

Weekly capability refresh must include manually adapted external skills that have `upstream` metadata. For each one, compare the local `upstream_ref` / `upstream_commit` against `git ls-remote --tags` or the source registry. Do not claim external skills are current unless this check ran.
