from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_root_compose_includes_the_canonical_stack() -> None:
    payload = yaml.safe_load((ROOT / "compose.yaml").read_text("utf-8"))

    assert payload["include"] == ["infra/docker-compose.yml"]


def test_compose_bootstraps_data_before_router_and_starts_mcp_by_default() -> None:
    payload = yaml.safe_load((ROOT / "infra/docker-compose.yml").read_text("utf-8"))
    services = payload["services"]

    assert "bootstrap" in services
    assert services["bootstrap"]["restart"] == "no"
    assert services["fast-router"]["depends_on"]["bootstrap"]["condition"] == "service_completed_successfully"
    assert "profiles" not in services["tool-gateway"]
    assert services["tool-gateway"]["depends_on"]["fast-router"]["condition"] == "service_healthy"


def test_fast_router_image_contains_bootstrap_inputs() -> None:
    dockerfile = (ROOT / "apps/fast-router/Dockerfile").read_text("utf-8")

    for expected in (
        "COPY scripts /app/scripts",
        "COPY data/normalized /app/data/normalized",
        "COPY docs/schemas /app/docs/schemas",
        "COPY infra/postgres /app/infra/postgres",
    ):
        assert expected in dockerfile


def test_docker_build_context_excludes_secrets_and_local_artifacts() -> None:
    patterns = set((ROOT / ".dockerignore").read_text("utf-8").splitlines())

    for expected in (".env", ".env.*", ".venv/", "**/node_modules/", "data/traces/"):
        assert expected in patterns
