---
aliases: [wechat, weixin, 微信, 微信公众号, 公众号, mp.weixin.qq.com]
---

# WeChat Public Articles

WeChat public articles are often readable in a real browser but blocked for static fetchers. Do not treat a Jina/curl "environment abnormal" response as proof that the article is unavailable.

## Preferred Ladder

1. If a quick summary is enough, try web search or Exa-style discovery first.
2. If the user needs the article body, use the local Camoufox-based helper:

```powershell
$wechatPython = "$env:USERPROFILE\.agent-reach\venvs\wechat-article\Scripts\python.exe"
$wechatTool = "$env:USERPROFILE\.agent-reach\tools\wechat-article-for-ai\main.py"
& $wechatPython $wechatTool "<URL>"
```

3. If the helper saves debug HTML but parser post-processing fails, extract manually from:

```text
$env:USERPROFILE\.agent-reach\tools\wechat-article-for-ai\output\debug\
```

Use BeautifulSoup selectors:

- title: `h1#activity-name`
- author: `span#js_name`
- content: `div#js_content`

Extract visible text from `p`, headings, `li`, `blockquote`, and `pre`; preserve code blocks and list order when relevant.

## Known Failure Modes

- Jina Reader commonly returns a WeChat environment verification page.
- Static `curl` commonly captures anti-bot scaffolding rather than article content.
- `wechat-article-for-ai` can succeed at browser capture but fail in its parser with `TypeError: 'NoneType' object is not callable`; the saved debug HTML is still useful.

## Safety

Do not request or store user cookies. If a browser login or verification is needed, ask the user to complete it in their own browser and continue from rendered/debug output.
