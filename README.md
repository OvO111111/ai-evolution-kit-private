# Codex Evolution Export

This package is a curated portability bundle for another AI agent.

## Current Access Model

This repository is the single public, redacted portability bundle. Cloud agents can clone it without inheriting the owner's local GitHub credentials. It is a curated projection of local Codex behavior, not a raw mirror of `%USERPROFILE%/.codex`.

Recommended setup:

1. Keep the full/private memory vault local and private.
2. Use this repository for portable working habits, evolution decisions, safe skills, and validators.
3. Keep project-derived skills as reviewed placeholder-based projections; never recursively overwrite them from private local source.
4. Run `python tools/check_export_safety.py` before every commit or push.

Do not publish raw work chats, account state, cookies, tokens, customer/payment data, local databases, private screenshots, or large project directories.

## Cloud Agent Bootstrap

For a hosted agent that can read public GitHub repositories:

```bash
git clone https://github.com/OvO111111/ai-evolution-kit-private.git
cd ai-evolution-kit-private
```

Then read these files in order:

1. `AGENTS.md`
2. `memories/self-evolution-ledger.md`
3. `memories/vault_summaries/working-habits.md`
4. `memories/vault_summaries/skill-routing.md`
5. `memories/vault_summaries/query-guide.md`

For skill installation, copy only the needed skill directories under `skills/` into the target runtime's skill directory. Do not blindly install every skill if the runtime has a small context window or weak skill routing.

The bundled sync script installs a curated project-derived skill only when that skill is absent. If the target machine already has a private/full local version, the script preserves it instead of overwriting it with the public placeholder projection.

Included:
- Self-evolution source ledger and adoption strategies
- Durable working preferences and skill rules
- Reusable skills and helper scripts that do not include secrets
- Web/WeChat article access workflow, design/product skills, browser capability notes

Excluded:
- WeChat work-group message bodies, search results, local indexes, and allowlists
- Account login state, cookies, tokens, API keys, OAuth grants, credential files
- Customer, payment, refund, complaint, merchant, and business-private data
- Large project files, generated artifacts, local database dumps, private screenshots, raw rollout logs

Use `memories/self-evolution-ledger.md` as the starting point.

After reinstalling Codex or starting from a blank machine, read `BOOTSTRAP_AFTER_REINSTALL.md` first. It contains the one-message bootstrap prompt and the exact sync commands needed to restore portable Codex evolution memory, skills, and global rules without syncing machine/runtime secrets.
