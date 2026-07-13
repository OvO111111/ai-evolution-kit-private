# Bootstrap After Codex Reinstall

Use this file when Codex was reinstalled and has no local chat history, memories, skills, or global instructions.

## First Message To New Codex

Send this to the fresh Codex instance:

```text
请从我的公开脱敏进化仓库恢复 Codex 进化资料：
https://github.com/OvO111111/ai-evolution-kit-private

克隆或更新仓库，先读 AI_OPERATING_PLAYBOOK.md、README.md、AGENTS.md、BOOTSTRAP_AFTER_REINSTALL.md。先恢复其中的工作方式；只有本机 Codex 需要安装仓库内 skills/辅助工具时才运行同步脚本。完成后告诉我当前 commit、行为规则是否已加载、工具安装结果（如有）和阻塞。
```

## No-Code Behavior Restore

If the target AI can read this repository but should not execute local code, it
only needs to read:

1. `AI_OPERATING_PLAYBOOK.md`
2. `AGENTS.md`
3. the matching `skills/*/SKILL.md` when a task requires more detail
4. `memories/self-evolution-ledger.md` only when provenance or a prior decision is
   relevant

This is enough to transfer the WeChat article route ladder, success criteria, and
failure semantics. The target AI should use its own equivalent browser, web,
connector, or document tools. Scripts below are optional local capability helpers,
not the meaning of the evolution ledger.

## Expected Recovery Steps

For a local Codex installation that should also receive the bundled skill files and
deterministic helpers, the new Codex should:

1. Clone the public redacted repo:

```powershell
git clone https://github.com/OvO111111/ai-evolution-kit-private.git
```

2. Run the sync script from the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-evolution.ps1
```

3. Verify installation and actual capability. Directory listing is not enough:

```powershell
git status --short --branch
git log -1 --oneline
Get-ChildItem "$env:USERPROFILE\.codex\skills" -Directory | Select-Object Name
Get-ChildItem "$env:USERPROFILE\.codex\memories\evolution-kit-private\vault_summaries" -File | Select-Object Name
powershell -ExecutionPolicy Bypass -File .\tools\verify_portable_capabilities.ps1
```

4. Certify live WeChat article reading with a real public article:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\verify_portable_capabilities.ps1 `
  -WechatUrl "https://mp.weixin.qq.com/s/r5aDx2ntV9E1QWM3oHe3kw"
```

The recovery is incomplete if the live test does not return `PORTABILITY_CHECK_PASSED`
and substantive article body extraction. A copied `SKILL.md`, installed command, title,
guest shell, or verification page is not a pass.

5. If Codex claims a URL or domain was permanently denied, audit user-editable rules:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\audit_access_denials.ps1 `
  -Domain "mp.weixin.qq.com"
```

A denial from one task, fetcher, Chrome action, or approval request is scoped to that
route. It must not be converted into a permanent domain ban. Do not bypass genuine
product safety policy; use another supported read-only route when only one path is
blocked.

## What Gets Restored

- `%USERPROFILE%\.codex\AGENTS.md`
- `%USERPROFILE%\.codex\skills\*`
- `%USERPROFILE%\.codex\memories\evolution-kit-private\*`
- Agent Reach's public WeChat reader checkout and isolated Python environment
- weekly sync automation can be recreated if the app lost automations

## What Does Not Get Restored

Do not restore these through GitHub:

- `auth.json`
- cookies
- tokens
- session files
- sqlite runtime logs/state
- browser profile/login state

These are machine/runtime state, not portable evolution memory. Re-login is expected after reinstall.

## Scope Rule

The most important correctness rule:

Company/work project memory is not global memory.

Examples of company/work context:

- 声之境
- 每周穿搭
- 多应用管理平台 / 统一后台
- WeChat Work group context
- Feishu operations reporting
- WeChat Pay/product rollout
- customer, complaint, merchant, payment data

These apply only when the task explicitly references that project family, workspace, domain, or asks to reuse that pattern.

Generic personal projects, open-source projects, public landing pages, generic H5 work, generic PRDs, and generic admin dashboards should use normal local/project-specific rules instead.
