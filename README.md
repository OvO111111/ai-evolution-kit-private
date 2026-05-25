# Codex Evolution Export

This package is a curated portability bundle for another AI agent.

## Current Access Model

This bundle is designed to be safe for a public or tokenless cloud-agent clone, but the original backup repository may still be private. If a cloud Hermes, OpenClaw, OpenClaw/Hermes-like runtime, or another hosted AI cannot access the GitHub URL, check the repository visibility first. A private repository requires that runtime to have GitHub credentials; most hosted agents do not inherit the owner's local GitHub login.

Recommended setup:

1. Keep the full/private memory vault local and private.
2. Publish this redacted export bundle to a separate public repository.
3. Point cloud agents at that public repository, not at the private backup.

Do not publish raw work chats, account state, cookies, tokens, customer/payment data, local databases, private screenshots, or large project directories.

## Cloud Agent Bootstrap

For a hosted agent that can read public GitHub repositories:

```bash
git clone https://github.com/<owner>/<public-evolution-export-repo>.git
cd <public-evolution-export-repo>
```

Then read these files in order:

1. `AGENTS.md`
2. `memories/self-evolution-ledger.md`
3. `memories/vault_summaries/working-habits.md`
4. `memories/vault_summaries/skill-routing.md`
5. `memories/vault_summaries/query-guide.md`

For skill installation, copy only the needed skill directories under `skills/` into the target runtime's skill directory. Do not blindly install every skill if the runtime has a small context window or weak skill routing.

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
