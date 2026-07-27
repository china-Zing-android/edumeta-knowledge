# Edumeta University Knowledge Retrieval

L1 Markdown knowledge retrieval with optional scoped WeKnora evidence. The runtime stack contains PostgreSQL, OpenSearch, Fast Router, a one-shot bootstrap gate, and the TypeScript MCP Tool Gateway.

## One-Command Start

Requirements: Docker Desktop or Docker Engine with Docker Compose.

This Compose stack binds every published port to `127.0.0.1` by default. PostgreSQL and OpenSearch always remain localhost-only. Fast Router and MCP Gateway can bind to a private VPN address through `FAST_ROUTER_BIND_HOST` and `MCP_BIND_HOST`. Do not expose the unauthenticated ingestion or MCP endpoints to the public Internet without authentication and TLS.

```bash
docker compose up -d --build
```

The first start automatically:

1. Applies every PostgreSQL migration.
2. Loads all schools under `data/normalized/`.
3. Publishes and verifies the global OpenSearch aliases.
4. Starts Fast Router only after bootstrap succeeds.
5. Starts the MCP Gateway only after Fast Router is healthy.

Check the stack:

```bash
docker compose ps -a
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8765/health
```

The `bootstrap` container should show `Exited (0)`. Fast Router and Tool Gateway should be `healthy`.

For access through a private Tailscale address, set the server address in `.env` and recreate only the two API services:

```text
FAST_ROUTER_BIND_HOST=100.74.163.113
MCP_BIND_HOST=100.74.163.113
```

```bash
docker compose up -d --force-recreate fast-router tool-gateway
```

Clients in the same tailnet can then use `http://100.74.163.113:8000` and `http://100.74.163.113:8765/mcp`.

## MCP

```json
{
  "mcpServers": {
    "edumeta-local": {
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

The server exposes one tool: `retrieve_university_knowledge`.

## Optional WeKnora

L1 works without WeKnora. Copy `.env.example` to `.env` and set the external WeKnora values only when L2 page evidence is required:

```text
WEKNORA_BASE_URL
WEKNORA_API_KEY
WEKNORA_KB_TEMPLATE_ID (optional configuration template for newly created school KBs)
```

Retrieval is multi-KB: every current source carries its actual knowledge-base ID, and deep search groups sources by that ID. `WEKNORA_KNOWLEDGE_BASE_ID` is an optional legacy fallback only and should normally remain empty. A template KB supplies chunking, embedding, wiki, and indexing settings when a new university KB is created; its documents are not copied or searched as part of that operation.

Set `WEKNORA_IMPORT_ENABLED=false` to pause URL uploads while keeping Markdown parsing, URL extraction, PostgreSQL/OpenSearch publication, and queued import jobs active. Set it back to `true` and recreate Fast Router to resume the backlog without re-uploading Markdown.

Without those values, detail requests return `mode=l1_l2` with `weknora_unavailable`; they do not silently answer from unrelated quick facts.

## Stop

```bash
docker compose down
```

Use `docker compose down -v` only when the local PostgreSQL and OpenSearch data may be deleted.

See `qa/manual/md-first-l1-weknora-qa-guide.md` for manual QA and `docs/operations/data-ingestion-runbook.md` for incremental Markdown ingestion.

## Batch University Markdown Import

The repository includes a country-organized 2026-07 batch under `data/raw-md/universities/`: 448 source documents and 439 enabled universities after duplicate resolution. Under quality ruleset `2026-07-24.1`, 276 pass automatic publication, 76 require review, and 87 are blocked.

With Compose running and `WEKNORA_IMPORT_ENABLED=false`, preview and import a small batch through the Fast Router container:

```bash
./scripts/import_universities.sh --dry-run --country US --limit 5
./scripts/import_universities.sh --country US --limit 5
```

The command is sequential and resumable. It imports only records whose manifest hash matches a `passed` preflight result. Every ingestion runs pre-publish static audit and post-index retrieval probes before activation. See `docs/operations/batch-university-md-ingestion.md` and `docs/operations/incremental-quality-audit-runbook.md`.
