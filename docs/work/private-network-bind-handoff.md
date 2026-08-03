Status: superseded

# Private Network Bind Handoff

## Goal

Allow Fast Router and MCP Gateway to be reached through a trusted private network while keeping data services local-only.

## Delivered

- Added `FAST_ROUTER_BIND_HOST` and `MCP_BIND_HOST` Compose variables, defaulting to `127.0.0.1`.
- PostgreSQL and OpenSearch remain hard-bound to localhost.
- Documented Tailscale binding with `100.74.163.113` and service recreation commands.
- Added a Compose contract test preventing accidental remote exposure of PostgreSQL/OpenSearch.

## Superseded boundary

This handoff established the API-only private binding pattern. Its earlier
OpenSearch localhost-only boundary was superseded by
`docs/work/opensearch-host-bind-handoff.md`: OpenSearch is now published on
`0.0.0.0` so external containers can reach it through the host IP. PostgreSQL
remains loopback-only. Because OpenSearch Security Plugin is disabled, its
published port must be restricted by firewall or trusted-network policy.

The HTTP ingestion and MCP endpoints still have no application authentication;
bind them only to a trusted VPN address.

## Verification

- `tests/test_compose_deployment.py`: 5 passed.
- `git diff --check`: passed.
