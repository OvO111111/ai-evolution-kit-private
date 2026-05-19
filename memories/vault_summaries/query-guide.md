# Query Guide

## Before Searching Everything

1. Identify whether the question is about a project, a reusable habit, a skill/tool, a payment/product topic, or work chat context.
2. Check `wiki/projects/project-registry.md` for where details live.
3. Check `wiki/topics/` and `wiki/decisions/` for compiled reusable knowledge.
4. Check `C:\Users\skzjc\.codex\memories\MEMORY.md` for rollout-specific references.
5. Only then open rollout summaries or raw task logs.

## Retrieval Pattern

Use exact search first:

```powershell
rg -n "<keyword>" C:\Users\skzjc\.codex\private\knowledge-vault C:\Users\skzjc\.codex\memories\MEMORY.md
```

Then expand by:

- project registry
- source map
- entity aliases
- time order
- source citations

## Context Packet Standard

When preparing context for a task, include:

- user goal
- relevant durable rules
- project lookup path
- source snippets or citations
- current uncertainty
- what must not be exported or shared

Do not include entire raw histories when a smaller evidence packet is enough.
