from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Literal

from fastapi import BackgroundTasks, Body, FastAPI, File, Form, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .admin import AdminControlPlane
from .ingestion import IngestionService
from .opensearch_retrieval import CurrentVersionMap, OpenSearchRetrievalClient
from .retrieval import RetrievalEngine
from .traceability import TraceabilityIndex
from .tracing import write_trace
from .weknora_client import WeknoraSearchClient
from .weknora_worker import WeknoraJobWorker, weknora_import_enabled


class RetrievalContext(BaseModel):
    level: str | None = None
    program_id: str | None = None
    entry_id: str | None = None


class RetrievalFilters(BaseModel):
    country_codes: list[str] = Field(default_factory=list)
    regions: list[str] = Field(default_factory=list)
    degree_levels: list[str] = Field(default_factory=list)
    levels: list[str] = Field(default_factory=list)
    school_tiers: list[str] = Field(default_factory=list)


class RetrieveRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    university_id: str | None = None
    context: RetrievalContext = Field(default_factory=RetrievalContext)
    direction: Literal["auto", "downward", "range", "upward"] = "auto"
    filters: RetrievalFilters = Field(default_factory=RetrievalFilters)
    max_results: int = Field(default=5, ge=1, le=20)


class RetrieveResponse(BaseModel):
    trace_id: str
    mode: Literal["l1", "l1_l2", "range", "upward", "clarification", "not_found", "error"]
    scope: dict[str, Any]
    matches: list[dict[str, Any]]
    context: dict[str, Any]
    evidence: list[dict[str, Any]]
    missing_slots: list[str]
    warnings: list[str]
    timings: dict[str, float]


class AdminBatchItem(BaseModel):
    item_id: str
    university_id: str
    university_name: str | None = None
    country_code: str | None = None
    region: str | None = None
    school_tier: Literal["core", "non_core"] = "core"
    aliases: list[str] = Field(default_factory=list)


class AdminBatchCommit(BaseModel):
    preview_id: str
    items: list[AdminBatchItem] = Field(min_length=1)


class AdminReasonRequest(BaseModel):
    reason: str = Field(min_length=1, max_length=2000)


class AdminRollbackRequest(AdminReasonRequest):
    version_id: str


version_map: CurrentVersionMap | None = None
retrieval_engine: RetrievalEngine | None = None
ingestion_service: IngestionService | None = None
weknora_worker: WeknoraJobWorker | None = None
admin_control: AdminControlPlane | None = None


def _initialize_services() -> None:
    global version_map, retrieval_engine, ingestion_service, weknora_worker, admin_control
    postgres_dsn = os.getenv("POSTGRES_DSN", "").strip()
    opensearch_url = os.getenv("OPENSEARCH_URL", "").strip()
    if postgres_dsn and opensearch_url:
        version_map = CurrentVersionMap(postgres_dsn)
        version_map.refresh()
        version_map.start()
        traceability = TraceabilityIndex(Path(os.getenv("INGESTION_DATA_ROOT", "data/ingestions")))
        retrieval_engine = RetrievalEngine(
            OpenSearchRetrievalClient(opensearch_url, version_map),
            WeknoraSearchClient.from_env(),
            traceability=traceability,
        )
        ingestion_service = IngestionService.from_env()
        if ingestion_service:
            ingestion_service.on_published = version_map.refresh
        weknora_worker = WeknoraJobWorker.from_env()
        if weknora_worker:
            weknora_worker.start()
        admin_control = AdminControlPlane(ingestion_service, weknora_worker=weknora_worker) if ingestion_service else None


@asynccontextmanager
async def lifespan(_: FastAPI):
    if retrieval_engine is None:
        try:
            _initialize_services()
        except Exception:
            # Health reports unavailable dependencies; the process remains inspectable.
            pass
    yield
    if retrieval_engine and retrieval_engine.weknora:
        retrieval_engine.weknora.close()
    if ingestion_service:
        ingestion_service.shutdown()
    if weknora_worker:
        weknora_worker.close()
    if version_map:
        version_map.close()


app = FastAPI(title="Edumeta L1 + WeKnora Retrieval", version="1.0.0", lifespan=lifespan)
_admin_cors_origins = [item.strip() for item in os.getenv("ADMIN_CORS_ORIGINS", "http://127.0.0.1:3000,http://localhost:3000").split(",") if item.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_admin_cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health() -> dict[str, Any]:
    versions = version_map.snapshot() if version_map else {}
    return {
        "status": "ok" if retrieval_engine else "degraded",
        "service": "fast-router",
        "postgres": {"configured": bool(os.getenv("POSTGRES_DSN")), "version_cache_size": len(versions)},
        "opensearch": {"configured": bool(os.getenv("OPENSEARCH_URL")), "ready": retrieval_engine is not None},
        "weknora": {
            "configured": bool(os.getenv("WEKNORA_BASE_URL")),
            "routing_mode": "per_source_knowledge_base",
            "import_enabled": weknora_import_enabled(),
            "template_knowledge_base_configured": bool(os.getenv("WEKNORA_KB_TEMPLATE_ID")),
            "legacy_fallback_knowledge_base_configured": bool(os.getenv("WEKNORA_KNOWLEDGE_BASE_ID")),
            "scope_filter": "knowledge_ids",
            "worker_alive": bool(weknora_worker and weknora_worker.alive),
            "worker_iterations": weknora_worker.iterations if weknora_worker else 0,
            "worker_last_run_count": weknora_worker.last_run_count if weknora_worker else 0,
            "worker_last_error": weknora_worker.last_error if weknora_worker else None,
        },
    }


@app.post("/v1/retrieve", response_model=RetrieveResponse)
def retrieve(request: RetrieveRequest) -> dict[str, Any]:
    if retrieval_engine is None:
        raise HTTPException(status_code=503, detail={"code": "RETRIEVAL_UNAVAILABLE", "message": "OpenSearch/version map is not ready"})
    payload = retrieval_engine.retrieve(
        query=request.query,
        university_id=request.university_id,
        context=request.context.model_dump(exclude_none=True),
        direction=request.direction,
        filters=request.filters.model_dump(exclude_none=True),
        max_results=request.max_results,
    )
    write_trace({
        "trace_id": payload["trace_id"],
        "endpoint": "/v1/retrieve",
        "query": request.query,
        "university_id": payload["scope"].get("university_id"),
        "mode": payload["mode"],
        "timings": payload["timings"],
        "source_ids": [row.get("source_id") for row in payload["matches"] + payload["evidence"] if row.get("source_id")],
    })
    return payload


def _parse_aliases(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


@app.post("/v1/ingestions", status_code=202)
@app.post("/v1/university-ingestions", status_code=202)
async def create_ingestion(
    university_id: str = Form(...),
    school_tier: str = Form(...),
    university_name: str | None = Form(None),
    country_code: str | None = Form(None),
    region: str | None = Form(None),
    aliases: str | None = Form(None),
    weknora_knowledge_base_id: str | None = Form(None),
    create_new_weknora_kb: bool = Form(False),
    file: UploadFile = File(...),
) -> dict[str, Any]:
    if ingestion_service is None:
        raise HTTPException(status_code=503, detail={"code": "INGESTION_UNAVAILABLE", "message": "PostgreSQL/OpenSearch ingestion is not ready"})
    try:
        content = await file.read()
        return ingestion_service.submit(
            university_id=university_id,
            school_tier=school_tier,
            filename=file.filename or "upload.md",
            content=content,
            university_name=university_name,
            country_code=country_code,
            region=region,
            aliases=_parse_aliases(aliases),
            weknora_knowledge_base_id=weknora_knowledge_base_id,
            create_new_weknora_kb=create_new_weknora_kb,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get("/v1/ingestions/{run_id}")
@app.get("/v1/university-ingestions/{run_id}")
def get_ingestion(run_id: str) -> dict[str, Any]:
    if ingestion_service is None:
        raise HTTPException(status_code=503, detail={"code": "INGESTION_UNAVAILABLE"})
    payload = ingestion_service.status(run_id)
    if payload is None:
        raise HTTPException(status_code=404, detail={"code": "INGESTION_NOT_FOUND"})
    return payload


def _require_admin() -> AdminControlPlane:
    global admin_control
    if admin_control is None and ingestion_service is not None:
        admin_control = AdminControlPlane(ingestion_service, weknora_worker=weknora_worker)
    if admin_control is None:
        raise HTTPException(status_code=503, detail={"code": "ADMIN_UNAVAILABLE", "message": "PostgreSQL/OpenSearch ingestion is not ready"})
    return admin_control


@app.get("/v1/admin/config/status")
def admin_config_status() -> dict[str, Any]:
    return _require_admin().config_status()


@app.get("/v1/admin/source-roots")
def admin_source_roots() -> dict[str, Any]:
    return {"items": _require_admin().source_roots()}


@app.get("/v1/admin/source-files")
def admin_source_files(
    source_root_id: str | None = Query(None),
    source_relative_path: str | None = Query(None),
    query: str | None = Query(None, max_length=200),
    status: str | None = Query(None, max_length=40),
    limit: int = Query(200, ge=1, le=500),
    offset: int = Query(0, ge=0),
    include_hash: bool = Query(False),
) -> dict[str, Any]:
    try:
        return _require_admin().source_files(
            source_root_id=source_root_id,
            source_relative_path=source_relative_path,
            query=query,
            status=status,
            limit=limit,
            offset=offset,
            include_hash=include_hash,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/v1/admin/ingestion-previews", status_code=200)
async def create_admin_preview(
    mode: Literal["upload", "directory"] = Form("upload"),
    source_root_id: str | None = Form(None),
    source_relative_path: str | None = Form(None),
    files: list[UploadFile] = File(default=[]),
) -> dict[str, Any]:
    control = _require_admin()
    try:
        uploaded = [(file.filename or "upload.md", await file.read()) for file in files]
        return control.create_preview(
            mode=mode,
            source_root_id=source_root_id,
            source_relative_path=source_relative_path,
            uploaded_files=uploaded,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/v1/admin/ingestion-batches", status_code=202)
def create_admin_batch(payload: AdminBatchCommit) -> dict[str, Any]:
    try:
        return _require_admin().commit_batch(payload.preview_id, [item.model_dump() for item in payload.items])
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get("/v1/admin/ingestion-batches")
def list_admin_batches(limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)) -> dict[str, Any]:
    return _require_admin().list_batches(limit=limit, offset=offset)


@app.get("/v1/admin/ingestion-batches/{batch_id}")
def get_admin_batch(batch_id: str) -> dict[str, Any]:
    try:
        return _require_admin().batch(batch_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/v1/admin/ingestion-runs")
def list_admin_runs(
    batch_id: str | None = Query(None),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
) -> dict[str, Any]:
    return _require_admin().list_runs(batch_id=batch_id, limit=limit, offset=offset)


@app.get("/v1/admin/ingestion-runs/{run_id}")
def get_admin_run(run_id: str) -> dict[str, Any]:
    payload = _require_admin().service.status(run_id)
    if payload is None:
        raise HTTPException(status_code=404, detail={"code": "INGESTION_NOT_FOUND"})
    return payload


@app.get("/v1/admin/ingestion-runs/{run_id}/diff")
def get_admin_diff(run_id: str) -> dict[str, Any]:
    try:
        return _require_admin().diff(run_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/v1/admin/ingestion-runs/{run_id}/artifacts")
def list_admin_artifacts(run_id: str) -> dict[str, Any]:
    try:
        return _require_admin().artifacts(run_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/v1/admin/ingestion-runs/{run_id}/artifacts/{artifact}/content")
def get_admin_artifact_content(
    run_id: str,
    artifact: str,
    offset: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
) -> dict[str, Any]:
    try:
        return _require_admin().artifact_page(run_id, artifact, offset=offset, limit=limit)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/v1/admin/ingestion-runs/{run_id}/provenance/{entity}/{record_id}")
def get_admin_provenance(run_id: str, entity: str, record_id: str) -> dict[str, Any]:
    try:
        return _require_admin().provenance(run_id, entity, record_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/v1/admin/ingestion-runs/{run_id}/artifacts/{artifact}/download")
def download_admin_artifact(run_id: str, artifact: str, background_tasks: BackgroundTasks) -> FileResponse:
    control = _require_admin()
    try:
        if artifact == "all":
            path = control.bundle_path(run_id)
            background_tasks.add_task(path.unlink, missing_ok=True)
            return FileResponse(path, media_type="application/zip", filename=f"{run_id}.zip")
        path = control.artifact_path(run_id, artifact)
        return FileResponse(path, media_type="text/plain", filename=path.name)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/v1/admin/ingestion-runs/{run_id}/force-publish", status_code=202)
def force_publish_admin_run(run_id: str, payload: AdminReasonRequest) -> dict[str, Any]:
    try:
        return _require_admin().force_publish(run_id, payload.reason)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@app.get("/v1/admin/universities/{university_id}/versions")
def list_admin_versions(university_id: str) -> dict[str, Any]:
    return _require_admin().versions(university_id)


@app.get("/v1/admin/versions")
def list_admin_version_catalog(
    query: str | None = Query(None, max_length=200),
    publication_state: str | None = Query(None, max_length=40),
    limit: int = Query(200, ge=1, le=500),
    offset: int = Query(0, ge=0),
) -> dict[str, Any]:
    return _require_admin().list_versions(
        query=query,
        publication_state=publication_state,
        limit=limit,
        offset=offset,
    )


@app.post("/v1/admin/universities/{university_id}/rollback")
def rollback_admin_version(university_id: str, payload: AdminRollbackRequest) -> dict[str, Any]:
    try:
        return _require_admin().rollback(university_id, payload.version_id, payload.reason)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@app.post("/v1/admin/universities/{university_id}/weknora/import-current", status_code=202)
def reimport_admin_current(university_id: str) -> dict[str, Any]:
    try:
        return _require_admin().reimport_current(university_id)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@app.get("/v1/admin/schema-catalog")
def admin_schema_catalog() -> dict[str, Any]:
    return _require_admin().schema_catalog()
