# Comparative Validation Protocol

Date: 2026-05-18

## Trigger

The user stated that every overlapping or comparable skill/project should trigger an active proposal to create different versions and test them. Without validation, the agent does not truly evolve.

## Adopted Rule

When a new project, skill, plugin, or method overlaps with an existing capability, Codex must proactively propose a comparison test.

The proposal must include:

- Variants to compare.
- One realistic task.
- Success criteria.
- Cost/time/risk.
- Recommended default path.
- Whether the test can run immediately or needs user approval.

Low-cost, local, non-sensitive tests should be run. Tests that require installation, account login, paid API use, external publishing, sensitive data, or destructive changes require user approval first.

Untested comparisons remain candidates. They cannot be described as adopted improvements.

## Current Validation Backlog

| Area | Variants | Suggested test | Success criteria | Status |
|---|---|---|---|---|
| Design output | `open-design-*` vs `huashu-design` vs Open CoDesign | Same landing/product visual task, produce comparable HTML/image/PPT artifact | Less generic, real assets used, responsive, no text overlap, screenshot verified, user preference | Pending |
| PRD /方案 | Old `pm-prd` baseline vs CodeBanana-inspired `pm-prd` vs Moxt-style context packet | One rough business request -> stakeholder breakdown, recommendation, PRD, test cases, rollout plan | Clear recommendation, fewer gaps, testable requirements, useful tradeoffs | Pending |
| Web article reading | Jina/curl vs Camoufox/debug HTML vs Chrome CDP | Read one WeChat article and summarize with source title/author | Reliable extraction, low retries, no login leak, clean text | Partially validated; needs timed comparison |
| Browser control | in-app browser vs raw Chrome CDP vs `browser-harness` | Open login-state page, extract target text, close owned tab | Works with login state, minimal tab disruption, clear failure mode | Partially validated |
| WeChat work context | `wx-cli`/`wechat-work-context` vs desktop UI automation vs OpenCLI-style adapter | Search one allowlisted group for a topic and draft reply with citations | Group isolation, no auto-send, relevant evidence, no leakage | POC validated for `wx-cli`; alternatives pending |
| Memory/export/retrieval | Private GitHub bundle vs neuDrive/local/self-hosted style vs Moxt workspace idea vs GBrain graph/search vs Karpathy LLM Wiki | Redacted notes corpus -> export/import/query with citations and deletion boundaries | Portable, small, redacted, importable by another AI, searchable with stable citations, scoped access, measurable retrieval quality | Private GitHub validated for export; retrieval alternatives pending |
| Private full knowledge vault | Raw private archive + LLM Wiki compiled layer + qmd/GBrain-style retrieval/index | Ingest a small but realistic mixed corpus: chat excerpts, project notes, PDFs/docs, decisions, and one intentionally stale fact | Stores full raw material, compiles useful wiki pages, retrieves with citations, preserves sensitivity labels, avoids stale facts, excludes sensitive data from generic export | Pending; should use synthetic or explicitly approved data first |
| Self-evolution | `absorb-lessons` manual gate vs SkillClaw-style loop vs GenericAgent-style crystallization | Process one new source into rule/skill/backlog with validation | Dedupe, explicit adopt/reject, no unsafe proxying, validation recorded | Manual gate validated; automated loops pending |
| Multi-agent coding/planning | Codex native subagents vs ClawTeam-OpenClaw vs manual main-agent decomposition | One bounded toy repo task with 2 independent modules plus integration | Context isolation, worktree isolation, coordination clarity, merge quality, token/tool overhead, failure observability | Pending; requires user approval before ClawTeam spawn |
| Desktop/app control | `desktop-control` vs OpenCLI adapter vs browser/CDP where applicable | Read or manipulate a non-browser app surface without account action | Correct target app, reversible action, no secret capture, user-visible verification | Pending |
| Token compression | Normal style vs `caveman*` modes | Same summary/task report in both styles | Shorter without losing decisions, actions, paths, risks | Pending |

## Operating Policy

The main agent should look for validation opportunities during normal work. When it sees overlapping capabilities, it should say: "这里有可比方案，我建议做一个小测试", then give the test plan and default recommendation.

Do not run every benchmark immediately. Prioritize tests attached to real user work, because artificial benchmarks can overfit and waste time. Installing one project should not automatically force a test; queue it and wait for a real opportunity unless the test is cheap, local, and directly useful now.
