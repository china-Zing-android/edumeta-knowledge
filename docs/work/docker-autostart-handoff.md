Status: active

# Docker Autostart Handoff

## Goal

Make the persistent Compose services start again after Docker Engine or host
reboots, while keeping the PostgreSQL migration bootstrap one-shot.

## Current decision

- PostgreSQL, OpenSearch, Fast Router, MD Admin, Tool Gateway, and optional
  OpenSearch Dashboards use `restart: unless-stopped`.
- `bootstrap` keeps `restart: "no"`; it should finish as `Exited (0)` after
  applying migrations.
- Linux hosts must enable the Docker service with
  `sudo systemctl enable --now docker`.
- Docker Desktop hosts must enable start-at-login in Docker Desktop settings.
- The server profile should be started with
  `docker compose -f compose.yaml -f compose.server.yaml --profile dashboards up -d`.

## Relevant files

- `infra/docker-compose.yml`
- `tests/test_compose_deployment.py`
- `README.md`
- `docs/operations/server-update-and-validation.md`

## Verification

- Red test confirmed the persistent services had no restart policy.
- Green restart-policy contract test: `1 passed, 11 deselected`.
- Full Compose contract verification should be run before release; the
  repository still contains the unrelated pre-existing Markdown mount assertion.

## Deployment note

After pulling this commit on the target host, run one forced recreation so the
new restart policies are written into existing containers. Future Docker or
host restarts should then use the policy automatically.
