---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-21"
sensitivity: personal
source_ids: ["memory_registry"]
confidence: high
status: active
---

# Working Habits

## Core Preference

The user wants execution over abstract explanation. When a concrete step can be taken safely, do it first and report what changed. Do not promise a future system when a small usable version can be created immediately.

## Communication

- Default to Chinese in conversation.
- Lead with conclusion, action, or recommendation.
- Avoid vague option lists. Give a recommended path, tradeoffs, and when to revisit.
- Do not ask the user to decide without explaining the decision surface.
- Avoid environment narrative unless it materially affects the result.

## Outcome-First Reporting

- Start final reports by answering the user's actual requirement, not by listing technical work.
- Use this order by default: requirement status, user-visible result, remaining gap, verification, changed files/artifacts.
- If the user asked for UI/prototype quality, describe visible screen and workflow changes before code, APIs, screenshots, or tests.
- If the user asked for product/PRD/workflow work, describe decisions, scope, user journey, acceptance result, and unresolved product risks before implementation notes.
- If the user asked for a bug fix, lead with root cause and whether the bug is fixed.
- Do not make file lists, endpoint status, compile output, screenshots, or generated reports the headline unless that was the user's actual request.
- If the result does not satisfy the user's requirement, say so directly and continue working unless a real blocker prevents it.

## Execution

- Inspect real context before changing files or making claims.
- Preserve unrelated user changes.
- Run the cheapest meaningful verification after edits.
- If a tool fails, diagnose the failure mode and change strategy instead of repeating the same call.
- For self-evolution work, record the source, evaluation, adoption status, output location, and validation state.

## End-To-End Execution

- Keep the user's original request as the completion target, not the latest substep.
- Treat intermediate steps as progress only. Do not report "done" when only one part of the request is done.
- Continue through obvious safe next steps without asking: inspection, focused local edits, formatting, validation, export sync, and status checks.
- Ask only when continuing would materially change cost, risk, privacy exposure, account action, data loss, production state, or product direction.
- If blocked, state the blocker, what was already tried, what exact user input or authorization is needed, and what will happen next after that input.
- Final answers should name the delivered outcome, verification run, remaining gaps, and whether anything was intentionally not pushed or published.

## Export Preference

The user wants reusable habits, skills, and evolution decisions to be portable to other AI systems so they do not have to retrain another assistant from scratch.

Generic exports must exclude secrets, account state, raw work chats, raw customer/payment data, and large project files.
