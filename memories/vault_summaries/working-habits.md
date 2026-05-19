---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-18"
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

## Execution

- Inspect real context before changing files or making claims.
- Preserve unrelated user changes.
- Run the cheapest meaningful verification after edits.
- If a tool fails, diagnose the failure mode and change strategy instead of repeating the same call.
- For self-evolution work, record the source, evaluation, adoption status, output location, and validation state.

## Export Preference

The user wants reusable habits, skills, and evolution decisions to be portable to other AI systems so they do not have to retrain another assistant from scratch.

Generic exports must exclude secrets, account state, raw work chats, raw customer/payment data, and large project files.
