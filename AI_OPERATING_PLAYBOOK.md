# AI Operating Playbook

This is the primary behavior-transfer document for another AI. Read it before the
source ledger. It explains what to do, when to do it, what counts as success, and
how to recover when one route fails.

No bundled script is required to understand or follow this playbook. Tool and
skill names are preferred implementations, not hard dependencies. If the target
AI has different tools, preserve the trigger, route order, failure semantics, and
success checks with equivalent capabilities.

## What Each Export Layer Is For

- `AI_OPERATING_PLAYBOOK.md`: portable behavior that another AI can apply now.
- `skills/*/SKILL.md`: detailed procedures for a matching task family.
- `memories/self-evolution-ledger.md`: source and decision audit; it is not an
  operating manual.
- `memories/vault_summaries/*`: concise evidence, boundaries, and prior outcomes.
- `scripts/` and skill `scripts/`: optional deterministic helpers for runtimes
  that can execute them.
- `tools/`: validation and maintenance; never a prerequisite for merely
  understanding the behavior.

## Universal Execution Rule

For a non-trivial request:

1. Identify the user's real outcome and the natural task signal.
2. Select the narrowest matching capability or skill.
3. Inspect the supplied source before drafting conclusions from it.
4. Use the lowest capable route, then escalate when concrete evidence shows that
   route failed.
5. Treat a failure or denial as scoped to the attempted route unless a durable
   user rule or genuine product policy explicitly says otherwise.
6. Verify the requested outcome, not merely tool availability or file presence.
7. Report `satisfied`, `partial`, `blocked`, `degraded`, or `unverified` plainly.

## Core Capability Index

| Natural task signal | Primary guidance | Minimum successful outcome |
|---|---|---|
| Public URL, article, social post, or "read/learn/summarize this" | `skills/web-access` and, for hostile/social/article pages, `skills/agent-reach` | Real source content was extracted and inspected |
| Login-state or dynamic browser task | Official Chrome/in-app browser when available; equivalent rendered browser otherwise | Requested logged-in content/action is visibly confirmed |
| Windows desktop app task | Official Computer Use when callable; equivalent desktop control otherwise | The actual app state changed or requested content was read |
| PRD, solution, product requirements | `skills/pm-prd` | Source-backed scope, decisions, acceptance criteria, and unresolved items |
| Generic UI/product design | `skills/ui-product-design-router` | A routed design workflow plus visible/browser-verified artifact |
| Company/work H5 under the unified-admin family | `skills/app-factory-h5-admin` | Scope confirmed, H5 first, admin second, PRD after experience/function confirmation |
| Data analysis report | `skills/data-analysis-report` or the target runtime's data-analysis capability | Source-backed metrics, method, findings, limits, and decision implications |
| Feishu/Lark document, board, sheet, or message | Matching Lark skill or native connector | Real editable native artifact or confirmed read/action |
| WeChat work-group history | `skills/wechat-work-context` | Read-only, group-isolated retrieval with message evidence; never auto-send |
| Self-evolution, skill absorption, global improvement | `skills/absorb-lessons` | Source logged, overlap judged, behavior card updated, and realistic validation recorded |

Project-derived capabilities are scoped. Company/work H5, unified-admin, payment,
Feishu operations, and WeChat work-context knowledge must not leak into unrelated
personal, open-source, client, or generic tasks.

## Capability Card: Public WeChat Article Reading

### Trigger

Use this card when the user supplies an `https://mp.weixin.qq.com/s/...` URL or
asks to read, inspect, learn from, summarize, evaluate, compare, or apply a public
WeChat article. Natural wording such as `看看这个`, `学习这个`, or `这个怎么样`
is sufficient. The user does not need to name `agent-reach`, Camoufox, Chrome, or
any other implementation.

### Required Outcome

Do not evaluate the article until its real body has been inspected. Success means:

- the actual title is available;
- substantive article body text is available, normally at least 200 characters;
- a title-only shell, guest page, verification page, search snippet, or error page
  is not reported as a successful read;
- conclusions are grounded in the extracted article, not its URL or promotional
  description.

### Route Ladder

Use the first route that can produce the required outcome. Tool names below are
examples; equivalent target-runtime tools are valid.

1. **Static public read:** ordinary fetch/search, reader endpoint, or page parser.
2. **Rendered browser:** official Chrome, in-app browser, CDP, Playwright, or an
   equivalent browser when the page is dynamic or static access is challenged.
3. **Site-specific public reader:** `agent-reach`, Camoufox, or another maintained
   WeChat article reader when generic browser/fetch routes are unreliable.
4. **Captured HTML recovery:** if a browser obtained HTML but parsing failed,
   extract the title from `h1#activity-name`, author from `span#js_name`, and body
   from `div#js_content`; preserve paragraph order.
5. **User-assisted input:** ask for pasted text, export, screenshot/OCR, or a file
   only after the available read-only routes above have been attempted or are
   genuinely unavailable.

Do not repeat the same failed fetch under a different label. Move to a more capable
route and preserve the concrete failure evidence.

### Failure And Denial Semantics

- `环境异常`, verification challenges, guest shells, timeouts, parser failures,
  and connection errors mean that route failed; they do not ban the article.
- A Chrome/browser policy denial ends only that browser action or route. Continue
  with another supported read-only route.
- A refusal, denied approval, or failure in one task must not become a permanent
  URL/domain ban in future tasks.
- Only an explicit durable user rule or genuine product safety policy may create a
  broader stop. Do not bypass product policy, but do not invent broader policy from
  a tool-specific failure.
- If every supported route is unavailable, report which distinct routes were
  attempted and ask for the smallest user-assisted input. Never claim the article
  was read.

### Reporting Contract

A successful response should make clear that the body was read, then answer the
user's actual request. It need not describe every tool attempt unless failures
matter to the result.

A blocked response must say `正文未读取`, name the distinct attempted routes, and
state the minimum next input needed. It must not say that the address is permanently
forbidden merely because one route was denied.

### Examples

Natural request:

> 这个怎么样？https://mp.weixin.qq.com/s/example

Expected behavior: read the article body through the route ladder, then evaluate
its useful ideas, overlap, adoption decision, and evidence. Do not ask the user to
name a skill.

Failed first route:

> Static fetch returned `环境异常`.

Expected behavior: continue to a rendered browser or site-specific reader. Do not
store or announce a permanent denial for `mp.weixin.qq.com`.

## Evolution Admission Rule

A capability is not portable merely because its source, repository, or installation
was recorded. Before an evolution item is marked adopted, it must provide or update
a capability card containing:

1. natural trigger signals;
2. required outcome and success checks;
3. preferred route and escalation ladder;
4. failure and denial semantics;
5. scope and non-goals;
6. equivalent-tool guidance for another runtime;
7. a realistic validation result.

If these are missing, the item remains `candidate` or `partial`, even when local
code, a skill folder, or a successful one-machine test exists.
