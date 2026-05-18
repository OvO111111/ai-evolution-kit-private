# Skill Routing Audit And Reorganization

Date: 2026-05-18

## Trigger

The user questioned whether the accumulated self-evolution sources, skills, and plugins are actually improving performance or creating overlap and regression.

## Audit Result

The current system has gained useful task-specific capability, but the measurable improvement is uneven:

- Verified useful: WeChat article fallback through Camoufox/debug HTML, `browser-harness` installation and CDP endpoint checks, `wechat-work-context` read-only group-history POC, private GitHub evolution export.
- Not yet proven quantitatively: overall reasoning quality, routing latency, token efficiency, and whether newly installed design/self-evolution skills improve outputs across varied tasks.
- Main overlap zones: `web-access` vs `agent-reach` vs `browser-harness`; frontend rules vs `open-design-*`; `absorb-lessons` vs SkillClaw/self-improving-agent concepts; `caveman*` vs normal communication.

## Adopted Reorganization

Global routing was tightened in `C:\Users\skzjc\.codex\AGENTS.md`:

1. Use the smallest matching skill set.
2. Prefer structured local tools before browser or desktop control.
3. Use `web-access` as the default web router.
4. Use `agent-reach` only for public/social/video/article cases where its site-specific tooling helps.
5. Use `browser-harness` for rendered/login-state browser pages.
6. Use `desktop-control` only for non-browser desktop apps or explicit computer-control tasks.
7. Use one relevant `open-design-*` skill, not a stack of design skills by default.
8. Use `caveman*` only when compression is requested or clearly useful.
9. Use `absorb-lessons` as the self-evolution gate; treat SkillClaw as a workflow reference, not a traffic proxy.

## Measurement Plan

Future skill/rule additions must record one of:

- A realistic validation prompt and observed result.
- A command/tool validation result.
- A clear reason validation was skipped.

Recommended benchmark set:

1. WeChat article extraction: blocked static fetch -> Camoufox/debug HTML -> clean article summary.
2. WeChat work context: retrieve allowed group messages without leaking group allowlists or sending messages.
3. Browser login task: verify CDP endpoint, open a login-state page, extract target content, close only owned tab.
4. PRD task: generate a decision-ready PRD using `pm-prd` without generic filler.
5. Frontend/design task: produce or review UI with screenshots and no overlapping text.
6. Export task: update evolution notes, exclude sensitive data, commit and push private repo.

## Current Policy

The system should be treated as improved in coverage, not automatically improved in intelligence. Real improvement is only counted when the relevant benchmark passes with less confusion, fewer retries, or better final output.
