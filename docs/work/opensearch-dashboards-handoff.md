Status: done

# OpenSearch Dashboards Handoff

## Goal

Add a version-matched OpenSearch web console without changing the existing OpenSearch container, data volume, mappings, aliases, or security mode.

## Constraints

- Pin Dashboards to `2.15.0`; never use `latest`.
- Keep the existing OpenSearch service and `opensearch_data` volume unchanged.
- Connect over Docker internal HTTP because the OpenSearch Security Plugin is disabled.
- Make Dashboards optional through a Compose profile.
- Bind locally by default and expose only to the trusted Tailscale address in the server profile.
- Do not expose port 5601 to the public Internet.

## Previous Release Verification

- Server 30-question suite passed 5 runs with no failures or nondeterminism.
- L1 p95 `89.02 ms`, upward p95 `51.172 ms`, range p95 `24.172 ms`.

## Implementation

- Added optional `dashboards` Compose profile with OpenSearch Dashboards `2.15.0`.
- Kept the existing OpenSearch service and `opensearch_data` volume unchanged.
- Added localhost-only base binding and loopback/Tailscale dual binding for the server profile.
- Disabled the Dashboards security plugin to match the existing HTTP OpenSearch deployment.
- Added health check, memory ceiling, restart policy, deployment tests, and an operations runbook.

## Verification

- Compose deployment contract: 10 tests passed.
- Server profile resolves Dashboards to `127.0.0.1:5601` and `100.74.163.113:5601` without changing the OpenSearch volume declaration.
- Real OpenSearch Dashboards `2.15.0` container started healthy against the existing OpenSearch `2.15.0` service.
- `/api/status` returned overall state `green`; OpenSearch and saved-objects services were available.
- Counts for all five L1 aliases were identical before and after Dashboards startup, confirming no business-index mutation.
