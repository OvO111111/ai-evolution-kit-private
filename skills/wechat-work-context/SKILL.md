---
name: wechat-work-context
description: Read local WeChat work-group history in a read-only, group-isolated way to summarize context and draft replies without sending messages. Use when the user asks for WeChat group context, work chat history, group reply drafting, or testing wx-cli/OpenCLI WeChat access.
---

# WeChat Work Context

Use this skill to help the user understand and reply to WeChat work groups from local chat history.

## Boundaries

- Read-only by default: never send, delete, like, forward, or modify WeChat messages.
- Use only the group the user names or the configured POC group. Do not mix groups.
- For POC, use at most two allowlisted groups and keep their outputs separate.
- Do not store chat content in global memory, skill files, commits, or exported docs.
- When drafting a reply, cite the source group and message times used for reasoning.

## Preferred Tool Path

Use `wx-cli` through `npx` unless a locally installed `wx` is already available:

```powershell
npx -y @jackwener/wx-cli sessions -n 20
npx -y @jackwener/wx-cli history "<group name>" -n 50 --type text --json
```

`wx-cli search --in` can miss recent results in some cases. Prefer `scripts/wechat_context.py search-local`, which pulls one group's history and filters locally.

## Helper

```powershell
python "$env:USERPROFILE\.codex\skills\wechat-work-context\scripts\wechat_context.py" list
python "$env:USERPROFILE\.codex\skills\wechat-work-context\scripts\wechat_context.py" history --chat "<group name>" --limit 30
python "$env:USERPROFILE\.codex\skills\wechat-work-context\scripts\wechat_context.py" search-local --chat "<group name>" --keyword "关键词" --limit 200
```

Private POC group names, if needed, belong outside the skill under:

`$env:USERPROFILE\.codex\private\wechat-work-context\poc-groups.json`

## Reply Workflow

1. Read only the selected group with `history`.
2. If the user asks about a topic, use `search-local` within that same group.
3. Summarize the immediate context, unresolved issue, owner, and risk.
4. Draft 1-3 reply options.
5. State that sending is manual.
