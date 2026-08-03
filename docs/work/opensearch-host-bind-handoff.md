Status: done

# OpenSearch Host Bind Handoff

## Goal

Allow containers outside the canonical Compose network to reach OpenSearch
through the host IP.

## Current decision

- `infra/docker-compose.yml` publishes OpenSearch as
  `0.0.0.0:${OPENSEARCH_PORT:-9200}:9200`.
- `compose.server.yaml` publishes OpenSearch as
  `0.0.0.0:${OPENSEARCH_SERVER_PORT:-19200}:9200`.
- Services already on the same Compose network should continue using
  `http://opensearch:9200`.
- OpenSearch Security Plugin is disabled, so the published host port must be
  restricted by firewall or trusted-network policy and must not be exposed
  directly to the public Internet.

## Relevant files

- `infra/docker-compose.yml`
- `compose.server.yaml`
- `tests/test_compose_deployment.py`
- `README.md`
- `docs/architecture/08-environment-deployment.md`
- `docs/operations/server-upload-and-retrieval-verification.md`
- `docs/operations/server-update-and-validation.md`

## Verification

- Red test run confirmed the two old OpenSearch binding assertions failed.
- The affected Compose contract tests pass: `2 passed, 9 deselected`.
- Full `tests/test_compose_deployment.py` has `10 passed, 1 failed`; the one
  failure is the pre-existing batch Markdown mount assertion and is unrelated
  to OpenSearch binding.
- Compose static resolution reports `host_ip: 0.0.0.0` for both the base
  `9200` mapping and the server-profile `19200` mapping.
- `git diff --check` passes.
- Docker daemon was unavailable in the local environment, so live container
  connectivity could not be checked here.

## Deployment note

Recreate the OpenSearch service on the target host so Docker applies the new
published binding; existing containers keep their old port mapping until
recreated.
