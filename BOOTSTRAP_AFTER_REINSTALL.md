# Bootstrap After Codex Reinstall

Use this file when Codex was reinstalled and has no local chat history, memories, skills, or global instructions.

## First Message To New Codex

Send this to the fresh Codex instance:

```text
请从我的私有进化仓库恢复 Codex 进化资料：
https://github.com/OvO111111/ai-evolution-kit-private

克隆或更新仓库，先读 README.md、AGENTS.md、BOOTSTRAP_AFTER_REINSTALL.md，再按文档运行同步脚本。完成后告诉我当前 commit、安装结果和是否有阻塞。
```

## Expected Recovery Steps

The new Codex should:

1. Clone the private repo:

```powershell
git clone https://github.com/OvO111111/ai-evolution-kit-private.git
```

2. Run the sync script from the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-evolution.ps1
```

3. Verify:

```powershell
git status --short --branch
git log -1 --oneline
Get-ChildItem C:\Users\hi\.codex\skills -Directory | Select-Object Name
Get-ChildItem C:\Users\hi\.codex\memories\evolution-kit-private\vault_summaries -File | Select-Object Name
```

## What Gets Restored

- `C:\Users\hi\.codex\AGENTS.md`
- `C:\Users\hi\.codex\skills\*`
- `C:\Users\hi\.codex\memories\evolution-kit-private\*`
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
