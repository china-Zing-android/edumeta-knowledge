from __future__ import annotations

import os
from contextlib import asynccontextmanager
from typing import Any, Literal

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

from .ingestion import IngestionService
from .opensearch_retrieval import CurrentVersionMap, OpenSearchRetrievalClient
from .retrieval import RetrievalEngine
from .tracing import write_trace
from .weknora_client import WeknoraSearchClient
from .weknora_worker import WeknoraJobWorker


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


version_map: CurrentVersionMap | None = None
retrieval_engine: RetrievalEngine | None = None
ingestion_service: IngestionService | None = None
weknora_worker: WeknoraJobWorker | None = None


def _initialize_services() -> None:
    global version_map, retrieval_engine, ingestion_service, weknora_worker
    postgres_dsn = os.getenv("POSTGRES_DSN", "").strip()
    opensearch_url = os.getenv("OPENSEARCH_URL", "").strip()
    if postgres_dsn and opensearch_url:
        version_map = CurrentVersionMap(postgres_dsn)
        version_map.refresh()
        version_map.start()
        retrieval_engine = RetrievalEngine(
            OpenSearchRetrievalClient(opensearch_url, version_map),
            WeknoraSearchClient.from_env(),
        )
        ingestion_service = IngestionService.from_env()
        if ingestion_service:
            ingestion_service.on_published = version_map.refresh
        weknora_worker = WeknoraJobWorker.from_env()
        if weknora_worker:
            weknora_worker.start()


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
        ingestion_service.executor.shutdown(wait=False, cancel_futures=False)
    if weknora_worker:
        weknora_worker.close()
    if version_map:
        version_map.close()


app = FastAPI(title="Edumeta L1 + WeKnora Retrieval", version="1.0.0", lifespan=lifespan)


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
