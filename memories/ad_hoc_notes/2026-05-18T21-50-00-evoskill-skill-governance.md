# EvoSkill skill governance

Source:

- WeChat article: `https://mp.weixin.qq.com/s/h8gsYACrt0mnBUT5BchaIw?scene=334`
- Project: `https://github.com/sentient-agi/EvoSkill`
- Local clone: `%USERPROFILE%\Developer\EvoSkill`

User concern:

- The skill library is growing too large; the assistant may not route or use skills well.

Findings:

- Article title: `垃圾Skill太多，有用的少？试试EvoSkill，用帕累托前沿让你的Skill库始终极简与高效`.
- EvoSkill is a governance/evolution framework, not just another skill.
- Key mechanism: executor/proposer/skill-builder loop, create-vs-edit decisions, fixed-size Pareto frontier, validation set, rejected-proposal history, skill merging, and zero-shot transfer tests.
- Repo README states it supports Claude Code, Codex CLI, OpenCode, OpenHands, Goose, Harbor, etc.; Codex CLI support is via `.agents/skills/` symlink.

Assessment:

- High-value concept for this user's environment because skill sprawl is already visible.
- Do not run full automated evolution yet. It needs a stable benchmark suite and could mutate global behavior unsafely.
- Adopt the governance policy now: active/reference/candidate/deprecated tiers, create-vs-edit check, validation before activation, rejected-proposal history, and benchmark matrix.

Applied:

- Updated `%USERPROFILE%\.codex\private\knowledge-vault\wiki\topics\skill-routing.md`.
- Added `%USERPROFILE%\.codex\private\knowledge-vault\wiki\decisions\skill-governance.md`.
