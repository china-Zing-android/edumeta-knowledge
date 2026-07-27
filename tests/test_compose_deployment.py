from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_root_compose_includes_the_canonical_stack() -> None:
    payload = yaml.safe_load((ROOT / "compose.yaml").read_text("utf-8"))

    assert payload["include"] == ["infra/docker-compose.yml"]


def test_server_compose_exposes_mcp_on_loopback_and_tailscale() -> None:
    text = (ROOT / "compose.server.yaml").read_text("utf-8")

    assert '127.0.0.1:${MCP_SERVER_PORT:-18765}:8765' in text
    assert '${MCP_TAILSCALE_HOST:-100.74.163.113}:${MCP_SERVER_PORT:-18765}:8765' in text
    assert "!override" in text


def test_compose_applies_migrations_before_router_and_starts_mcp_by_default() -> None:
    payload = yaml.safe_load((ROOT / "infra/docker-compose.yml").read_text("utf-8"))
    services = payload["services"]

    assert "bootstrap" in services
    assert services["bootstrap"]["restart"] == "no"
    assert "/app/scripts/apply_postgres_migrations.py" in services["bootstrap"]["command"]
    assert "/app/scripts/live_data_gate.py" not in services["bootstrap"]["command"]
    assert services["fast-router"]["depends_on"]["bootstrap"]["condition"] == "service_completed_successfully"
    assert "profiles" not in services["tool-gateway"]
    assert services["tool-gateway"]["depends_on"]["fast-router"]["condition"] == "service_healthy"


def test_postgres_has_enough_shared_memory_for_vacuuming_ingestion_tables() -> None:
    payload = yaml.safe_load((ROOT / "infra/docker-compose.yml").read_text("utf-8"))

    assert payload["services"]["postgres"]["shm_size"] == "256mb"


def test_only_api_services_have_configurable_private_bind_hosts() -> None:
    payload = yaml.safe_load((ROOT / "infra/docker-compose.yml").read_text("utf-8"))
    services = payload["services"]

    assert services["postgres"]["ports"] == ["127.0.0.1:${POSTGRES_PORT:-5432}:5432"]
    assert services["opensearch"]["ports"] == ["127.0.0.1:${OPENSEARCH_PORT:-9200}:9200"]
    assert services["fast-router"]["ports"] == [
        "${FAST_ROUTER_BIND_HOST:-127.0.0.1}:${FAST_ROUTER_PORT:-8000}:8000"
    ]
    assert services["tool-gateway"]["ports"] == [
        "${MCP_BIND_HOST:-127.0.0.1}:${MCP_PORT:-8765}:8765"
    ]


def test_fast_router_image_contains_runtime_and_migration_inputs() -> None:
    dockerfile = (ROOT / "apps/fast-router/Dockerfile").read_text("utf-8")

    for expected in (
        "COPY scripts /app/scripts",
        "COPY docs/schemas /app/docs/schemas",
        "COPY infra/postgres /app/infra/postgres",
    ):
        assert expected in dockerfile
    assert "COPY data/normalized /app/data/normalized" not in dockerfile


def test_batch_markdown_is_mounted_read_only_and_state_is_persistent() -> None:
    payload = yaml.safe_load((ROOT / "infra/docker-compose.yml").read_text("utf-8"))
    volumes = payload["services"]["fast-router"]["volumes"]

    assert "../data/raw-md/universities:/app/data/raw-md/universities:ro" in volumes
    assert "batch_import_state:/app/data/import-state" in volumes
    assert "batch_import_state" in payload["volumes"]


def test_docker_build_context_excludes_secrets_and_local_artifacts() -> None:
    patterns = set((ROOT / ".dockerignore").read_text("utf-8").splitlines())

    for expected in (".env", ".env.*", ".venv/", "**/node_modules/", "data/traces/", "data/raw-md/universities/"):
        assert expected in patterns
