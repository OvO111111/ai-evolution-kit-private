---
name: pm-prd
description: "Generate, clarify, review, and extend product requirement documents (PRDs) from product ideas, research notes, existing PRD files, or feature-change requests. Use when the user asks for PRD, product requirements, product specs, feature planning, PM documentation, user stories, acceptance criteria, release scope, or PRD review."
---

# PM PRD

Use this skill to turn product intent into a clear, reviewable PRD. It adapts the PM Skills Marketplace idea of reusable product-management frameworks, especially the `phuryn/pm-skills` `create-prd` 8-section template, into a Codex-friendly workflow.

## Modes

Choose one mode from the user's request:

- **Generate:** Create a new PRD from a natural-language idea, feature request, market opportunity, or research notes.
- **Clarify:** Review an existing PRD and ask targeted questions to resolve important gaps.
- **Extend:** Add a new feature or changed requirement to an existing PRD while preserving its structure, terminology, priorities, and numbering.
- **Solution Plan:** Produce a decision-ready product/implementation方案 before writing or editing code. Use this when the user asks "怎么做", "方案", "规划", "落地路径", "改之前先分析", or when execution risk is high.

If mode is ambiguous and the wrong choice would change the output file, ask one concise question. Otherwise state the assumed mode and proceed.

## Core Workflow

1. **Gather context.** Read referenced files, notes, URLs, customer data, or screenshots before writing. Use web research when the user mentions market context, competitors, or external evidence.
2. **Frame the problem.** Identify the user, job-to-be-done, pain, business objective, constraints, and success signal.
3. **Separate what from how.** PRDs should define product behavior, user value, scope, and acceptance criteria. Include technical details only when they are product constraints or integration requirements.
4. **Make assumptions visible.** Use reasonable defaults when they are low-risk, but record them under Assumptions. Use `[NEEDS CLARIFICATION: ...]` only for unresolved choices that materially affect scope, risk, UX, data, or compliance. Keep these markers to 3 or fewer in a generated PRD.
5. **Write testable requirements.** Every functional requirement and user story must be independently verifiable.
6. **Keep scope controlled.** Include non-goals and release phasing so the PRD does not become a wishlist.
7. **Close the loop.** For substantial work, produce or request the next artifact that validates the PRD: solution plan, prototype notes, test cases, rollout checklist, or recurring-task specification.
8. **Self-review before delivery.** Check for vague language, missing success metrics, untestable requirements, hidden technical implementation, and inconsistent terminology.

## Context-First Intake

Before writing a PRD or方案, build a compact context packet:

- **Source context:** files, chat/history notes, screenshots, URLs, customer feedback, current workflow, and known constraints.
- **Stakeholder lenses:** user/customer, sales/operations, support, product, design, engineering, QA, compliance/security, and whoever must approve the result.
- **Current-state map:** where the work starts, what data or systems are touched, who acts, where handoffs happen, and what currently breaks.
- **Decision target:** what decision the document should enable: approve MVP, choose an implementation path, align a team, estimate work, test a release, or automate a recurring process.

If context is missing but the task is low-risk, state assumptions and continue. If the missing context changes scope, risk, permissions, or cost, ask only the highest-impact question.

## Stakeholder Decomposition

For ambiguous or cross-team requests, first decompose the need by role before drafting:

```markdown
| Role | Goal | Action Needed | Required Info | Acceptance Standard | Priority |
|---|---|---|---|---|---|
```

This is not filler. Use it to expose conflicts early: sales wants speed, support wants traceability, engineering wants low-risk integration, QA wants testable states, compliance wants data boundaries.

## Solution Plan Mode

Write a方案 that can be reviewed before implementation. Prefer this structure:

1. **Conclusion / Recommended Path**
   - Start with the recommended option, not a menu of choices.
   - Say why it is the best path under current constraints.

2. **Problem And Context**
   - Current state, pain, trigger, affected users, systems, and constraints.

3. **Stakeholder / Role Breakdown**
   - Use the stakeholder table when more than one role or team is affected.

4. **Options Considered**
   - Usually 2-3 options.
   - For each: benefit, cost, risk, reversibility, and when it is appropriate.

5. **Scope**
   - MVP, later, and explicit non-goals.

6. **Implementation Plan**
   - Files/modules/systems to touch when known.
   - Phases, dependencies, owner assumptions, and rollback path.

7. **Risks And Controls**
   - Product risk, UX risk, data/security risk, operational risk, technical risk.

8. **Validation**
   - Acceptance criteria, test cases, analytics/metrics, review checkpoints, and launch checklist.

For code-related方案, include "do not edit yet" analysis when requested: project structure, files likely to change, exact change intent per file, risks, and smallest implementation path.

## Generate Mode Template

Write the PRD in Markdown. For substantial PRDs, save to the repo's existing PRD/docs location if one exists; otherwise use `prds/<short-name>.md`. Do not commit unless the user asks.

Use these sections:

1. **Summary**
   - Two or three sentences explaining the product change and why it matters.

2. **Contacts**
   - Stakeholders, owners, reviewers, and open ownership gaps. Use `TBD` only when genuinely unknown.

3. **Background**
   - Current context, why now, user pain, business motivation, and relevant research or market signals.

4. **Objective**
   - Product objective, strategic fit, and SMART success metrics or OKR-style key results.

5. **Market Segment(s) / Users**
   - Target users defined by jobs, pains, contexts, and constraints, not only demographics.

6. **Value Proposition(s)**
   - Jobs addressed, gains created, pains reduced, and why this is meaningfully better than alternatives.

7. **Solution**
   - User stories ordered by priority.
   - Functional requirements with stable IDs such as `FR-001`.
   - UX or workflow notes when relevant.
   - Data entities or policy constraints when relevant.
   - Assumptions and dependencies.

8. **Release**
   - MVP scope, later scope, non-goals, risks, rollout notes, and acceptance criteria.

9. **Validation Artifacts**
   - Test cases by priority, edge cases, analytics events, manual QA checklist, and open review questions.

## User Stories

Each story should be small enough to validate independently:

```markdown
### US-001: [Title] (P1)

As a [user/context], I want [capability] so that [benefit].

Acceptance criteria:
- [ ] [Specific observable behavior]
- [ ] [Error/edge case behavior]
- [ ] [Measurement or validation method]
```

For UI-facing stories, include browser or visual verification when applicable. Avoid vague criteria such as "works correctly" or "is intuitive".

## Clarify Mode

When reviewing an existing PRD:

1. Scan for gaps in scope, users, data, UX flow, non-functional constraints, dependencies, risks, acceptance criteria, and terminology.
2. Ask at most 5 questions total.
3. Ask one question at a time.
4. Prefer multiple-choice questions with a recommended option and rationale.
5. After each answer, update the PRD directly if the user asked you to edit files; otherwise summarize the exact patch recommendation.

Skip questions that do not change product scope, risk, implementation planning, or validation.

## Test Case Generation

When a PRD or方案 is meant for execution, add test coverage that would catch real failures:

- P0 happy path and critical business flow.
- Required-field and invalid-format validation.
- Duplicate submission, rate limit, idempotency, and retry behavior where relevant.
- Network/backend failure and user recovery.
- Permission/role boundaries.
- Data length, mobile/responsive, localization, and accessibility where relevant.
- Operational handoff: notification, audit trail, export, or owner follow-up.

Output as Markdown by default. If the user needs direct browser viewing or QA handoff, create an HTML table or spreadsheet only when requested.

## Recurring / Automated Workflow Specs

For scheduled tasks, file watchers, daily reports, or proactive agents, do not write a vague prompt. Specify:

- Trigger: schedule, event, file path, webhook, or manual command.
- Input contract: exact source files/fields, freshness, and permissions.
- Output contract: destination, format, naming, and owner.
- Failure handling: timeout, partial data, retry, escalation, and human confirmation.
- Observability: logs, heartbeat/status, last successful run, and alert conditions.
- Privacy: what must not be included in prompts, skills, logs, or exports.

## Extend Mode

When adding to an existing PRD:

1. Preserve the document's structure, IDs, tone, terminology, and priority scheme.
2. Add new requirements only where they belong; do not rewrite unrelated sections.
3. Update impacted user stories, functional requirements, success metrics, non-goals, risks, and release scope.
4. If a new requirement conflicts with existing scope, state the conflict and ask before editing.

## Quality Checklist

Before reporting completion, verify:

- The PRD explains what and why before how.
- The recommendation is explicit when the user needs a decision or方案.
- Stakeholder conflicts and tradeoffs are surfaced instead of hidden.
- Requirements are numbered, unambiguous, and testable.
- User stories have concrete acceptance criteria.
- Success metrics are measurable.
- Non-goals and release boundaries are explicit.
- Assumptions are visible and limited.
- No implementation technology is forced unless the user or project constraints require it.
- Validation artifacts are strong enough to catch likely business, UX, and integration failures.
