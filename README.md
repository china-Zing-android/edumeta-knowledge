# Edumeta University Knowledge Retrieval

L1 Markdown knowledge retrieval with optional scoped WeKnora evidence. The runtime stack contains PostgreSQL, OpenSearch, Fast Router, a one-shot bootstrap gate, and the TypeScript MCP Tool Gateway.

## One-Command Start

Requirements: Docker Desktop or Docker Engine with Docker Compose.

This Compose stack is a local/MVP deployment and binds every published port to `127.0.0.1`. Do not expose Fast Router or its ingestion endpoints to an untrusted network without adding authentication, TLS, and production database/search credentials.

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
WEKNORA_KNOWLEDGE_BASE_ID
```

Without those values, detail requests return `mode=l1_l2` with `weknora_unavailable`; they do not silently answer from unrelated quick facts.

## Stop

```bash
docker compose down
```

Use `docker compose down -v` only when the local PostgreSQL and OpenSearch data may be deleted.

See `qa/manual/md-first-l1-weknora-qa-guide.md` for manual QA and `docs/operations/data-ingestion-runbook.md` for incremental Markdown ingestion.
