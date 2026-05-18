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

If mode is ambiguous and the wrong choice would change the output file, ask one concise question. Otherwise state the assumed mode and proceed.

## Core Workflow

1. **Gather context.** Read referenced files, notes, URLs, customer data, or screenshots before writing. Use web research when the user mentions market context, competitors, or external evidence.
2. **Frame the problem.** Identify the user, job-to-be-done, pain, business objective, constraints, and success signal.
3. **Separate what from how.** PRDs should define product behavior, user value, scope, and acceptance criteria. Include technical details only when they are product constraints or integration requirements.
4. **Make assumptions visible.** Use reasonable defaults when they are low-risk, but record them under Assumptions. Use `[NEEDS CLARIFICATION: ...]` only for unresolved choices that materially affect scope, risk, UX, data, or compliance. Keep these markers to 3 or fewer in a generated PRD.
5. **Write testable requirements.** Every functional requirement and user story must be independently verifiable.
6. **Keep scope controlled.** Include non-goals and release phasing so the PRD does not become a wishlist.
7. **Self-review before delivery.** Check for vague language, missing success metrics, untestable requirements, hidden technical implementation, and inconsistent terminology.

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

## Extend Mode

When adding to an existing PRD:

1. Preserve the document's structure, IDs, tone, terminology, and priority scheme.
2. Add new requirements only where they belong; do not rewrite unrelated sections.
3. Update impacted user stories, functional requirements, success metrics, non-goals, risks, and release scope.
4. If a new requirement conflicts with existing scope, state the conflict and ask before editing.

## Quality Checklist

Before reporting completion, verify:

- The PRD explains what and why before how.
- Requirements are numbered, unambiguous, and testable.
- User stories have concrete acceptance criteria.
- Success metrics are measurable.
- Non-goals and release boundaries are explicit.
- Assumptions are visible and limited.
- No implementation technology is forced unless the user or project constraints require it.
