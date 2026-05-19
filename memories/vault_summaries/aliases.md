# Alias Index

This file maps likely Chinese user queries to canonical vault pages.

## Chinese Query Aliases

| Query terms | Canonical page |
|---|---|
| 工作习惯, 做事习惯, 沟通习惯, 执行偏好, 少说废话 | `../wiki/topics/working-habits.md` |
| 自我进化, 进化台账, 吸收经验, 学习项目, 外部文章 | `../wiki/topics/self-evolution-system.md` |
| 技能路由, skill重叠, 工具选择, browser, agent-reach, web-access | `../wiki/topics/skill-routing.md` |
| 知识库, 记忆库, 私有记忆, 长期记忆, 精确检索, RAG | `../wiki/topics/knowledge-vault-design.md` |
| HTML, HTML产物, HTML artifact, 可交互报告, 可视化知识 | `../wiki/topics/html-artifacts.md` |
| 微信群, 工作群, 群消息, 微信上下文, 找群消息 | `../wiki/topics/wechat-work-context.md` |
| 微信支付, H5支付, JSAPI, 委托代扣, 扣款, 商户平台 | `../wiki/topics/payment-product-design.md` |
| 飞书, 周报, 甘特图, 多维表格, base, wiki, docx | `../wiki/projects/project-registry.md` |
| 多Agent, agent集群, 上下文隔离, 上下文共享, 子Agent | `../wiki/decisions/multi-agent-context-protocol.md` |
| 导出, 备份, 迁移到其他AI, GitHub备份, 敏感信息 | `../wiki/decisions/export-boundaries.md` |
| 做过什么项目, 项目在哪查, 历史项目, 项目索引 | `../wiki/projects/project-registry.md` |

## Retrieval Rule

If a Chinese query does not hit FTS because of tokenizer limits, search this alias index first, then open the canonical page.
