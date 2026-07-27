Status: done

# Server Update Runbook Handoff

## Goal

Commit a complete server update procedure covering dual-address HTTP/MCP startup, migration order, quality quarantine, resumable batch ingestion, 30-question regression, and external Agent verification.

## Delivered

- `compose.server.yaml` now dual-binds Fast Router and MCP to loopback and the current Tailscale address.
- MCP uses host port `18765`, leaving the existing `8765` service untouched.
- The server profile defaults WeKnora URL upload to paused while preserving L1 ingestion and queued jobs.
- `docs/operations/server-update-and-validation.md` defines the authoritative server command order.
- Current quality-gate counts are normalized to 276 passed / 75 needs_review / 88 failed.

## Verification

- `docker compose -f compose.yaml -f compose.server.yaml config`: passed; both API services resolve to loopback and `100.74.163.113`, MCP maps host `18765` to container `8765`, and WeKnora import resolves to disabled.
- `tests/test_compose_deployment.py`: 8 passed.
- `git diff --check`: passed.
