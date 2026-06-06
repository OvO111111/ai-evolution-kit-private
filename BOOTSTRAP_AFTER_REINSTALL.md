# Bootstrap After Codex Reinstall

Use this file when Codex was reinstalled and has no local chat history, memories, skills, or global instructions.

## First Message To New Codex

Send this to the fresh Codex instance:

```text
请从我的私有进化仓库恢复 Codex 记忆、skills 和全局配置：
https://github.com/OvO111111/ai-evolution-kit-private

目标：
1. 克隆或更新这个仓库到本机 Documents/Codex 下；
2. 阅读 README.md、AGENTS.md、BOOTSTRAP_AFTER_REINSTALL.md；
3. 运行 scripts/sync-codex-evolution.ps1，把 AGENTS.md、skills/、memories/evolution-kit-private/ 安装到 C:\Users\hi\.codex；
4. 不同步 auth.json、tokens、cookies、sessions、sqlite 日志；
5. 记住：导出记忆必须分作用域，global / personal-reusable / company-work / task-local。公司项目记忆，例如 声之境、每周穿搭、统一后台、Feishu、WeChat Work、支付/投诉/客户数据，只能用于匹配的公司项目或我明确引用时，不能影响普通个人项目、开源项目、通用 H5、通用 PRD 或通用设计任务；
6. 同步完成后告诉我当前 commit、安装了哪些关键 skills、全局规则是否已生效。
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
