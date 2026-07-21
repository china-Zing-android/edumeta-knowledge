Status: done

# Private Network Bind Handoff

## Goal

Allow Fast Router and MCP Gateway to be reached through a trusted private network while keeping data services local-only.

## Delivered

- Added `FAST_ROUTER_BIND_HOST` and `MCP_BIND_HOST` Compose variables, defaulting to `127.0.0.1`.
- PostgreSQL and OpenSearch remain hard-bound to localhost.
- Documented Tailscale binding with `100.74.163.113` and service recreation commands.
- Added a Compose contract test preventing accidental remote exposure of PostgreSQL/OpenSearch.

## Security Boundary

The HTTP ingestion and MCP endpoints currently have no application authentication. Bind them only to a trusted VPN address. Public binding or `0.0.0.0` requires a reverse proxy, TLS, authentication, and firewall policy first.

## Verification

- `tests/test_compose_deployment.py`: 5 passed.
- `git diff --check`: passed.
