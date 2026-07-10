---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-18"
sensitivity: personal
source_ids: ["karpathy_llm_wiki", "gbrain_evaluation", "html_artifact_trend_research"]
confidence: high
status: active
---

# Knowledge Vault Design

## Goal

Build a private, portable, large-scale memory system that preserves enough context to answer future work questions without stuffing every raw source into the prompt.

## Architecture

```text
raw evidence
  -> metadata and source hashes
  -> entities, aliases, claims, decisions, events
  -> timelines and relationship maps
  -> Markdown/HTML compiled artifacts
  -> indexes and evidence packets for task context
```

## Ground Truth

Raw sources are ground truth. Wiki pages, HTML reports, SQLite indexes, vector indexes, and graph stores are derived artifacts or caches.

## Portability

Canonical storage should use open formats: original files, Markdown, HTML, YAML frontmatter, JSONL, CSV, and plain text logs.

SQLite, embeddings, graph databases, Obsidian metadata, MCP servers, or future tools must be rebuildable from canonical files.

## Retrieval Principle

RAG alone is insufficient. Use a combination of:

- exact search over raw/wiki
- metadata filters
- entity and alias resolution
- relationship expansion
- timeline ordering
- claim/decision status
- citations back to raw source
- vector search only as an auxiliary recall path

## Scope Boundary

The vault should know what projects were done and where to inspect them. It should not ingest full project code, build artifacts, dependency directories, or large private files unless a future task requires that material.
