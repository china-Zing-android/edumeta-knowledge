from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import uuid
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

from .ingestion import MAX_MD_FILE_BYTES, IngestionService
from .weknora_worker import weknora_import_enabled


MAX_UPLOAD_FILES = 20
PREVIEW_TTL_MINUTES = 60
ARTIFACTS: dict[str, str] = {
    "raw_markdown": "input.md",
    "catalog_entries": "catalog_entries.jsonl",
    "quick_facts": "quick_facts.jsonl",
    "source_registry": "source_registry.jsonl",
    "url_manifest": "url_manifest.jsonl",
    "entity_contexts": "entity_contexts.jsonl",
}
JSONL_ARTIFACTS = tuple(name for name in ARTIFACTS if name != "raw_markdown")

JSONL_GUIDE: dict[str, dict[str, Any]] = {
    "catalog_entries": {
        "label": "专业与学位目录",
        "purpose": "记录学校有哪些专业、辅修和研究生项目，是 L1 专业检索的主体数据。",
        "why": "把专业身份、学位层级、院系和来源拆成稳定记录，支持结构化检索和版本差异。",
        "minimum": ["entry_id", "university_id", "school", "department", "level", "degree_level", "program_name", "source_id", "source_url", "dataset_version", "status"],
        "links": ["entry_id", "source_id", "university_id"],
    },
    "quick_facts": {
        "label": "关键事实",
        "purpose": "记录学费、截止日期、语言要求、申请费和资助等明确事实。",
        "why": "让确定性的数字和规则可以被单独校验、追踪来源并快速回答。",
        "minimum": ["fact_id", "university_id", "fact_type", "fact_key", "raw_value", "source_id", "source_url", "capture_date", "dataset_version", "review_status", "conflict_status"],
        "links": ["fact_id", "source_id", "entry_id", "university_id"],
    },
    "source_registry": {
        "label": "官网来源登记",
        "purpose": "管理被系统认可的官网来源、来源类型、校验状态和 WeKnora 导入状态。",
        "why": "集中管理来源生命周期，避免同一 URL 在不同数据记录中产生漂移。",
        "minimum": ["source_id", "university_id", "canonical_url", "url_type", "topics", "official_source", "priority", "status", "parser_status", "weknora_import_status", "capture_date", "last_verified", "dataset_version"],
        "links": ["source_id", "canonical_url", "university_id"],
    },
    "url_manifest": {
        "label": "URL 关联清单",
        "purpose": "连接 URL、专业、主题和 WeKnora 文档，是 L1 到 L2 的地址簿。",
        "why": "把来源本身和来源与业务实体的关系分开，支持精准范围检索和局部重导入。",
        "minimum": ["url_id", "source_id", "university_id", "entry_ids", "source_url", "canonical_url", "url_type", "topics", "official_source", "import_status", "capture_date", "dataset_version"],
        "links": ["url_id", "source_id", "entry_ids", "university_id"],
    },
    "entity_contexts": {
        "label": "学校与专业上下文",
        "purpose": "提供学校和专业的展示上下文、亮点、关联实体和可继续追问的主题。",
        "why": "把检索结果从单个匹配记录提升为可解释的学校或专业上下文。",
        "minimum": ["context_id", "entity_type", "entity_id", "university_id", "title", "display_label", "attributes", "highlights", "sample_children", "related_entities", "available_topics", "source_ids", "dataset_version", "status"],
        "links": ["context_id", "entity_id", "entry_id", "source_ids", "university_id"],
    },
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _valid_id(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,127}", value.strip().lower()))


def _normalise_relative_path(value: str) -> str:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("relative path must remain inside the configured source root")
    return path.as_posix()


def _json_value(value: Any) -> Any:
    if isinstance(value, (dict, list, str, int, float, bool)) or value is None:
        return value
    return str(value)


class AdminControlPlane:
    def __init__(self, service: IngestionService, *, weknora_worker: Any | None = None) -> None:
        self.service = service
        self.weknora_worker = weknora_worker
        self.roots = self._load_roots()

    def _connect(self):
        import psycopg

        return psycopg.connect(self.service.postgres_dsn)

    @staticmethod
    def _load_roots() -> dict[str, Path]:
        configured = os.getenv("INGESTION_ADMIN_ROOTS_JSON", "").strip()
        if configured:
            try:
                value = json.loads(configured)
                if isinstance(value, dict):
                    return {str(key): Path(str(path)).resolve() for key, path in value.items()}
                if isinstance(value, list):
                    return {f"root_{index}": Path(str(path)).resolve() for index, path in enumerate(value)}
            except json.JSONDecodeError as exc:
                raise RuntimeError("INGESTION_ADMIN_ROOTS_JSON must be valid JSON") from exc

        raw = os.getenv("INGESTION_ADMIN_ROOTS", "").strip()
        if raw:
            return {f"root_{index}": Path(item).resolve() for index, item in enumerate(raw.split(os.pathsep)) if item.strip()}

        default = os.getenv("INGESTION_SOURCE_ROOT", "data/raw-md/universities")
        return {"universities": Path(default).resolve()}

    def _root(self, root_id: str) -> Path:
        root = self.roots.get(root_id)
        if root is None:
            raise ValueError("unknown source root")
        return root

    def _safe_path(self, root: Path, relative_path: str, *, allow_missing: bool = False) -> Path:
        relative = _normalise_relative_path(relative_path)
        candidate = root / relative
        resolved = candidate.resolve(strict=not allow_missing)
        try:
            resolved.relative_to(root.resolve())
        except ValueError as exc:
            raise ValueError("path escapes the configured source root") from exc
        return resolved

    def config_status(self) -> dict[str, Any]:
        enabled = weknora_import_enabled()
        configured = bool(os.getenv("WEKNORA_BASE_URL", "").strip())
        ready = enabled and configured and bool(os.getenv("POSTGRES_DSN", "").strip()) and bool(os.getenv("OPENSEARCH_URL", "").strip())
        return {
            "enabled": enabled,
            "configured": configured,
            "worker_alive": bool(self.weknora_worker and self.weknora_worker.alive),
            "import_mode": "enabled" if ready else ("disabled" if not enabled else "misconfigured"),
            "last_error": self.weknora_worker.last_error if self.weknora_worker else None,
            "template_knowledge_base_configured": bool(os.getenv("WEKNORA_KB_TEMPLATE_ID", "").strip()),
            "api_key_configured": bool(os.getenv("WEKNORA_API_KEY", "").strip()),
        }

    def source_roots(self) -> list[dict[str, Any]]:
        return [
            {"root_id": root_id, "label": root_id, "exists": root.exists(), "relative_only": True}
            for root_id, root in sorted(self.roots.items())
        ]

    def _existing_universities(self) -> dict[str, dict[str, Any]]:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT university_id, university_name, country_code, region, school_tier, aliases FROM universities"
            )
            return {
                row[0]: {
                    "university_name": row[1],
                    "country_code": row[2],
                    "region": row[3],
                    "school_tier": row[4],
                    "aliases": row[5] or [],
                }
                for row in cursor.fetchall()
            }

    @staticmethod
    def _infer_metadata(path: Path, content: str) -> dict[str, Any]:
        stem = re.sub(r"(?:_知识库_完整深度数据)?_?v\d+$", "", path.stem, flags=re.IGNORECASE)
        candidate = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_").lower()
        heading = next((line[2:].strip() for line in content.splitlines() if line.startswith("# ")), "")
        heading = re.sub(r"\s+(?:Knowledge Base|知识库).*$", "", heading, flags=re.IGNORECASE).strip()
        country = path.parts[0].upper() if path.parts and re.fullmatch(r"[a-zA-Z]{2}", path.parts[0]) else None
        return {
            "university_id": candidate,
            "university_name": heading or candidate.replace("_", " ").title(),
            "country_code": country,
            "region": None,
            "school_tier": "core",
            "aliases": [],
        }

    @staticmethod
    def _read_manifest(root: Path) -> dict[str, dict[str, Any]]:
        path = root / "manifest.jsonl"
        if not path.exists():
            return {}
        rows: dict[str, dict[str, Any]] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("relative_path"):
                rows[Path(str(row["relative_path"])).as_posix()] = row
        return rows

    def _make_item(
        self,
        path: Path,
        *,
        root: Path,
        root_id: str,
        manifest: dict[str, Any] | None,
        existing: dict[str, dict[str, Any]],
        storage_name: str | None = None,
    ) -> dict[str, Any]:
        relative = path.relative_to(root).as_posix() if path.is_relative_to(root) else path.name
        size = path.stat().st_size
        content = path.read_text(encoding="utf-8", errors="replace")[:65536]
        metadata = dict(manifest or self._infer_metadata(path, content))
        metadata.setdefault("aliases", [])
        metadata.setdefault("school_tier", "core")
        metadata.setdefault("region", None)
        metadata.setdefault("country_code", None)
        metadata.setdefault("university_name", "")
        metadata["university_id"] = str(metadata.get("university_id") or "").strip().lower()
        issues: list[dict[str, Any]] = []
        if size > MAX_MD_FILE_BYTES:
            issues.append({"code": "file_too_large", "message": "单个 Markdown 文件超过 20 MiB"})
        if not content.strip() and size <= 65536:
            issues.append({"code": "empty_file", "message": "Markdown 文件为空"})
        if not _valid_id(metadata["university_id"]):
            issues.append({"code": "unmapped_university", "message": "无法推断合法的 university_id"})
        if path.suffix.lower() != ".md":
            issues.append({"code": "not_markdown", "message": "仅支持 .md 文件"})
        operation = "update" if metadata["university_id"] in existing else "create"
        item = {
            "item_id": f"item_{uuid.uuid4().hex}",
            "filename": path.name,
            "relative_path": relative,
            "source_root_id": root_id,
            "storage_name": storage_name,
            "size_bytes": size,
            "sha256": _sha256(path),
            "operation": operation,
            "issues": issues,
            "ready": not issues,
            **{key: metadata.get(key) for key in ("university_id", "university_name", "country_code", "region", "school_tier", "aliases")},
        }
        return item

    def _mark_duplicate_ids(self, items: list[dict[str, Any]]) -> None:
        grouped: dict[str, list[dict[str, Any]]] = {}
        for item in items:
            university_id = str(item.get("university_id") or "")
            if university_id and not any(issue["code"] == "unmapped_university" for issue in item["issues"]):
                grouped.setdefault(university_id, []).append(item)
        for university_id, matches in grouped.items():
            if len(matches) < 2:
                continue
            paths = [str(item["relative_path"]) for item in matches]
            for item in matches:
                item["issues"].append({
                    "code": "duplicate_university_id",
                    "message": f"{university_id} 在同一批次只能有一个 current 版本；若顺序提交，后一个版本会替换前一个版本，旧版本的 WeKnora 待处理任务可能被标记为 superseded。影响范围：该院校的 PostgreSQL current、OpenSearch current 数据和 WeKnora 导入队列。",
                    "impact": {
                        "university_id": university_id,
                        "conflicting_paths": paths,
                        "scope": ["该院校的 PostgreSQL current", "OpenSearch current 数据", "WeKnora 导入队列"],
                        "current_version_policy": "同一院校只能有一个 current 版本",
                        "submission_order": "后提交的版本会替换先提交的版本",
                        "weknora_impact": "旧版本 WeKnora 待处理任务可能被标记为 superseded",
                    },
                })
                item["ready"] = False

    def create_preview(
        self,
        *,
        mode: str,
        source_root_id: str | None = None,
        source_relative_path: str | None = None,
        uploaded_files: Iterable[tuple[str, bytes]] | None = None,
    ) -> dict[str, Any]:
        if mode not in {"upload", "directory"}:
            raise ValueError("mode must be upload or directory")
        existing = self._existing_universities()
        preview_id = f"preview_{uuid.uuid4().hex}"
        storage_dir = self.service.raw_root / "_previews" / preview_id
        items: list[dict[str, Any]] = []
        if mode == "upload":
            files = list(uploaded_files or [])
            if not files:
                raise ValueError("at least one Markdown file is required")
            if len(files) > MAX_UPLOAD_FILES:
                raise ValueError("normal upload accepts at most 20 files")
            storage_dir.mkdir(parents=True, exist_ok=False)
            for filename, content in files:
                safe_name = Path(filename).name
                item_path = storage_dir / f"{len(items):04d}_{safe_name}"
                item_path.write_bytes(content)
                item = self._make_item(
                    item_path,
                    root=storage_dir,
                    root_id="upload",
                    manifest=None,
                    existing=existing,
                    storage_name=item_path.name,
                )
                item["relative_path"] = safe_name
                item["source_root_id"] = None
                items.append(item)
            source_root_id = None
            source_relative_path = None
        else:
            if not source_root_id:
                raise ValueError("source_root_id is required for directory preview")
            root = self._root(source_root_id)
            if not root.exists() or not root.is_dir():
                raise ValueError("configured source root does not exist")
            target = self._safe_path(root, source_relative_path or "") if source_relative_path else root
            if not target.is_dir():
                raise ValueError("source path must be a directory")
            manifest_rows = self._read_manifest(root)
            for path in sorted(target.rglob("*.md")):
                if not path.is_file() or path.is_symlink():
                    continue
                relative = path.relative_to(root).as_posix()
                items.append(self._make_item(
                    path,
                    root=root,
                    root_id=source_root_id,
                    manifest=manifest_rows.get(relative),
                    existing=existing,
                ))
            if not items:
                raise ValueError("no Markdown files found in the selected directory")
        self._mark_duplicate_ids(items)
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=PREVIEW_TTL_MINUTES)
        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            from psycopg.types.json import Jsonb

            cursor.execute(
                """
                INSERT INTO admin_previews
                  (preview_id, mode, source_root_id, source_relative_path, storage_dir, items, expires_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (preview_id, mode, source_root_id, source_relative_path, str(storage_dir), Jsonb(items), expires_at),
            )
        return {
            "preview_id": preview_id,
            "mode": mode,
            "source_root_id": source_root_id,
            "source_relative_path": source_relative_path,
            "expires_at": expires_at.isoformat(),
            "total_count": len(items),
            "ready_count": sum(1 for item in items if item["ready"]),
            "blocked_count": sum(1 for item in items if not item["ready"]),
            "items": items,
        }

    def _load_preview(self, preview_id: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT preview_id, mode, source_root_id, source_relative_path, storage_dir, items, status, expires_at FROM admin_previews WHERE preview_id=%s",
                (preview_id,),
            )
            row = cursor.fetchone()
        if not row:
            raise ValueError("preview not found")
        if row[6] != "ready" or row[7] < datetime.now(timezone.utc):
            raise ValueError("preview expired or already submitted")
        return (
            {"preview_id": row[0], "mode": row[1], "source_root_id": row[2], "source_relative_path": row[3], "storage_dir": row[4]},
            list(row[5] or []),
        )

    def commit_batch(self, preview_id: str, selections: list[dict[str, Any]]) -> dict[str, Any]:
        preview, preview_items = self._load_preview(preview_id)
        by_id = {str(item["item_id"]): item for item in preview_items}
        if not selections:
            raise ValueError("at least one preview item must be submitted")
        selected_items: list[dict[str, Any]] = []
        for selection in selections:
            item = by_id.get(str(selection.get("item_id")))
            if item is None:
                raise ValueError("preview item not found")
            if not item["ready"]:
                raise ValueError(f"preview item is blocked: {item['relative_path']}")
            merged = {**item, **{key: selection[key] for key in ("university_id", "university_name", "country_code", "region", "school_tier", "aliases") if key in selection}}
            merged["university_id"] = str(merged.get("university_id") or "").strip().lower()
            if merged["school_tier"] not in {"core", "non_core"} or not _valid_id(merged["university_id"]):
                raise ValueError(f"invalid metadata for {merged['relative_path']}")
            selected_items.append(merged)
        self._mark_duplicate_ids(selected_items)
        duplicates = [item for item in selected_items if not item["ready"]]
        if duplicates:
            raise ValueError("selected files contain duplicate university mappings")

        batch_id = f"batch_{uuid.uuid4().hex}"
        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO ingestion_batches (batch_id, mode, source_root_id, source_relative_path, status, total_count, accepted_count) VALUES (%s, %s, %s, %s, 'processing', %s, 0)",
                (batch_id, preview["mode"], preview["source_root_id"], preview["source_relative_path"], len(selected_items)),
            )

        submitted: list[dict[str, Any]] = []
        rejected: list[dict[str, Any]] = []
        for item in selected_items:
            try:
                if preview["mode"] == "upload":
                    content_path = Path(preview["storage_dir"]) / str(item["storage_name"])
                    content = content_path.read_bytes()
                    source_root = None
                else:
                    source_root = self._root(str(item["source_root_id"]))
                    content_path = self._safe_path(source_root, str(item["relative_path"]))
                    if content_path.stat().st_size != int(item["size_bytes"]) or _sha256(content_path) != item["sha256"]:
                        raise ValueError(f"source changed after preview: {item['relative_path']}")
                    content = content_path.read_bytes()
                submitted.append(self.service.submit(
                    university_id=item["university_id"],
                    school_tier=item["school_tier"],
                    filename=item["filename"],
                    content=content,
                    university_name=item.get("university_name"),
                    country_code=item.get("country_code"),
                    region=item.get("region"),
                    aliases=item.get("aliases") or [],
                    batch_id=batch_id,
                    source_relative_path=item.get("relative_path"),
                    source_root_id=item.get("source_root_id"),
                    source_mode=preview["mode"],
                ))
            except Exception as exc:  # A bad source must not discard valid files in the same batch.
                rejected.append({
                    "item_id": item["item_id"],
                    "relative_path": item["relative_path"],
                    "filename": item["filename"],
                    "message": str(exc),
                })
        batch_status = "accepted" if submitted and not rejected else ("partial" if submitted else "failed")
        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            from psycopg.types.json import Jsonb

            cursor.execute("UPDATE admin_previews SET status='submitted' WHERE preview_id=%s", (preview_id,))
            cursor.execute(
                "UPDATE ingestion_batches SET status=%s, accepted_count=%s, rejected_count=%s, rejected_items=%s, updated_at=now() WHERE batch_id=%s",
                (batch_status, len(submitted), len(rejected), Jsonb(rejected), batch_id),
            )
            cursor.execute(
                "INSERT INTO admin_audit_events (event_id, action, reason, batch_id, metadata) VALUES (%s, 'batch_submit', %s, %s, %s)",
                (f"audit_{uuid.uuid4().hex}", "Markdown batch submitted", batch_id, Jsonb({"preview_id": preview_id, "accepted_count": len(submitted), "rejected_count": len(rejected), "rejected_items": rejected})),
            )
        return {"batch_id": batch_id, "mode": preview["mode"], "runs": submitted, "rejected": rejected, "total_count": len(selected_items), "accepted_count": len(submitted), "rejected_count": len(rejected)}

    def _batch_row(self, batch_id: str) -> dict[str, Any] | None:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT batch_id, mode, source_root_id, source_relative_path, status, total_count, accepted_count, published_count, failed_count, unchanged_count, weknora_disabled_count, created_at, updated_at, rejected_count, rejected_items FROM ingestion_batches WHERE batch_id=%s",
                (batch_id,),
            )
            row = cursor.fetchone()
            if not row:
                return None
            cursor.execute("SELECT run_id FROM ingestion_runs WHERE batch_id=%s ORDER BY created_at, run_id", (batch_id,))
            run_ids = [item[0] for item in cursor.fetchall()]
            cursor.execute(
                """
                SELECT count(*),
                       count(*) FILTER (WHERE status='published'),
                       count(*) FILTER (WHERE status='failed'),
                       count(*) FILTER (WHERE status='unchanged'),
                       count(*) FILTER (WHERE status IN ('published', 'unchanged'))
                  FROM ingestion_runs WHERE batch_id=%s
                """,
                (batch_id,),
            )
            counts = cursor.fetchone() or (0, 0, 0, 0, 0)
        return {
            "batch_id": row[0], "mode": row[1], "source_root_id": row[2], "source_relative_path": row[3], "status": row[4],
            "total_count": row[5], "accepted_count": int(counts[0]), "published_count": int(counts[1]), "failed_count": int(counts[2]),
            "unchanged_count": int(counts[3]), "weknora_disabled_count": int(counts[4]) if not (weknora_import_enabled() and os.getenv("WEKNORA_BASE_URL", "").strip()) else 0, "rejected_count": row[13] or 0,
            "rejected_items": row[14] or [], "created_at": row[11].isoformat(), "updated_at": row[12].isoformat(),
            "run_ids": run_ids,
        }

    def list_batches(self, *, limit: int = 50, offset: int = 0) -> dict[str, Any]:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT batch_id, mode, source_root_id, source_relative_path, status, total_count,
                       created_at, updated_at
                  FROM ingestion_batches
                 ORDER BY created_at DESC
                 LIMIT %s OFFSET %s
                """,
                (min(max(limit, 1), 200), max(offset, 0)),
            )
            rows = cursor.fetchall()
        batches: list[dict[str, Any]] = []
        for row in rows:
            batch = self._batch_row(row[0])
            if batch:
                batches.append(batch)
        return {"items": batches, "limit": limit, "offset": offset}

    def list_runs(self, *, batch_id: str | None = None, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        with self._connect() as connection, connection.cursor() as cursor:
            where = "WHERE batch_id=%s" if batch_id else ""
            params: tuple[Any, ...] = (batch_id, min(max(limit, 1), 500), max(offset, 0)) if batch_id else (min(max(limit, 1), 500), max(offset, 0))
            cursor.execute(
                f"""
                SELECT run_id FROM ingestion_runs {where}
                 ORDER BY created_at DESC
                 LIMIT %s OFFSET %s
                """,
                params,
            )
            run_ids = [row[0] for row in cursor.fetchall()]
        return {"items": [self.service.status(run_id) for run_id in run_ids], "limit": limit, "offset": offset}

    def batch(self, batch_id: str) -> dict[str, Any]:
        batch = self._batch_row(batch_id)
        if not batch:
            raise ValueError("batch not found")
        runs = [self.service.status(run_id) for run_id in batch["run_ids"]]
        statuses = [run["status"] for run in runs if run]
        if not statuses and batch["rejected_count"]:
            batch["status"] = "failed"
        elif statuses and all(status in {"published", "failed", "unchanged"} for status in statuses):
            if all(status in {"published", "unchanged"} for status in statuses):
                batch["status"] = "completed"
            elif all(status == "failed" for status in statuses):
                batch["status"] = "failed"
            else:
                batch["status"] = "partial"
        else:
            batch["status"] = "processing"
        return {**batch, "runs": runs}

    def _run_context(self, run_id: str) -> dict[str, Any]:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT run_id, university_id, version_id, status, source_filename, source_relative_path, source_root_id, batch_id, diff_summary FROM ingestion_runs WHERE run_id=%s",
                (run_id,),
            )
            row = cursor.fetchone()
        if not row:
            raise ValueError("run not found")
        return {
            "run_id": row[0], "university_id": row[1], "version_id": row[2], "status": row[3],
            "source_filename": row[4], "source_relative_path": row[5], "source_root_id": row[6], "batch_id": row[7], "diff_summary": row[8] or {},
        }

    def _run_dir(self, run: dict[str, Any]) -> Path:
        root = self.service.raw_root.resolve()
        path = (root / str(run["university_id"]) / str(run["run_id"])).resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise ValueError("run artifact path escaped ingestion root") from exc
        return path

    def artifacts(self, run_id: str) -> dict[str, Any]:
        run = self._run_context(run_id)
        run_dir = self._run_dir(run)
        items: list[dict[str, Any]] = []
        for artifact, filename in ARTIFACTS.items():
            path = run_dir / filename
            if not path.is_file():
                items.append({"artifact": artifact, "filename": filename, "available": False})
                continue
            lines = sum(1 for _ in path.open("r", encoding="utf-8", errors="replace"))
            items.append({"artifact": artifact, "filename": filename, "available": True, "size_bytes": path.stat().st_size, "sha256": _sha256(path), "line_count": lines})
        return {"run": run, "items": items}

    def artifact_path(self, run_id: str, artifact: str) -> Path:
        if artifact not in ARTIFACTS:
            raise ValueError("unknown artifact")
        run = self._run_context(run_id)
        path = self._run_dir(run) / ARTIFACTS[artifact]
        if not path.is_file():
            raise ValueError("artifact not available")
        return path

    def artifact_page(self, run_id: str, artifact: str, *, offset: int = 0, limit: int = 100) -> dict[str, Any]:
        path = self.artifact_path(run_id, artifact)
        offset = max(offset, 0)
        limit = min(max(limit, 1), 500)
        items: list[Any] = []
        total = 0
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for index, line in enumerate(handle):
                total = index + 1
                if index < offset or len(items) >= limit:
                    continue
                if artifact == "raw_markdown":
                    items.append({"line": index + 1, "text": line.rstrip("\n")})
                else:
                    try:
                        items.append({"line": index + 1, "record": json.loads(line)})
                    except json.JSONDecodeError:
                        items.append({"line": index + 1, "error": "invalid JSONL line", "text": line.rstrip("\n")})
        return {"artifact": artifact, "offset": offset, "limit": limit, "total": total, "items": items}

    def bundle_path(self, run_id: str) -> Path:
        run = self._run_context(run_id)
        run_dir = self._run_dir(run)
        if not run_dir.exists():
            raise ValueError("run artifacts are not available")
        output_dir = self.service.raw_root / "_downloads"
        output_dir.mkdir(parents=True, exist_ok=True)
        output = output_dir / f"{run_id}.zip"
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for artifact, filename in ARTIFACTS.items():
                path = run_dir / filename
                if path.is_file():
                    archive.write(path, arcname=filename)
        return output

    def versions(self, university_id: str) -> dict[str, Any]:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT v.version_id, v.dataset_version, v.publication_state, v.input_hash,
                       v.record_counts, v.created_at, v.published_at, v.superseded_at,
                       r.run_id, r.status, r.source_filename
                  FROM school_versions AS v
                  LEFT JOIN LATERAL (
                    SELECT run_id, status, source_filename
                      FROM ingestion_runs
                     WHERE university_id=v.university_id AND version_id=v.version_id
                     ORDER BY created_at DESC LIMIT 1
                  ) AS r ON true
                 WHERE v.university_id=%s
                 ORDER BY v.created_at DESC
                """,
                (university_id,),
            )
            rows = cursor.fetchall()
        cutoff = datetime.now(timezone.utc) - timedelta(days=90)
        version_items: list[dict[str, Any]] = []
        for row in rows:
            artifact_available = False
            if row[8] and row[7] and row[7] >= cutoff:
                artifact_available = (self.service.raw_root / str(university_id) / str(row[8]) / "normalized").is_dir()
            version_items.append({
                "version_id": row[0], "dataset_version": row[1], "publication_state": row[2], "input_hash": row[3],
                "record_counts": row[4] or {}, "created_at": row[5].isoformat(),
                "published_at": row[6].isoformat() if row[6] else None,
                "superseded_at": row[7].isoformat() if row[7] else None,
                "run_id": row[8], "run_status": row[9], "source_filename": row[10],
                "rollback_available": row[2] == "superseded" and artifact_available,
            })
        return {
            "university_id": university_id,
            "items": version_items,
        }

    def _load_dataset_dir(self, path: Path, university_id: str) -> dict[str, list[dict[str, Any]]]:
        from catalog_parser.postgres_loader import ENTITY_SPECS, read_jsonl

        return {
            spec.name: read_jsonl(path / spec.file_name) if (path / spec.file_name).exists() else []
            for spec in ENTITY_SPECS
        }

    def diff(self, run_id: str) -> dict[str, Any]:
        from catalog_parser.diff import diff_entity
        from catalog_parser.postgres_loader import ENTITY_SPECS

        run = self._run_context(run_id)
        target_dir = self._run_dir(run) / "normalized"
        if not target_dir.exists():
            summary = run.get("diff_summary") or {}
            if summary:
                return {"run_id": run_id, "university_id": run["university_id"], "version_id": run["version_id"], **summary}
            raise ValueError("normalized artifacts are not available")
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT r.run_id, r.version_id
                  FROM ingestion_runs AS r
                  JOIN school_versions AS v USING (university_id, version_id)
                 WHERE r.university_id=%s AND r.version_id<>%s AND v.publication_state IN ('current', 'superseded')
                 ORDER BY CASE WHEN v.publication_state='current' THEN 0 ELSE 1 END, r.created_at DESC
                 LIMIT 1
                """,
                (run["university_id"], run["version_id"]),
            )
            previous_row = cursor.fetchone()
        previous_dir = None
        if previous_row:
            previous_run = self._run_context(previous_row[0])
            candidate = self._run_dir(previous_run) / "normalized"
            previous_dir = candidate if candidate.exists() else None
        previous = self._load_dataset_dir(previous_dir, run["university_id"]) if previous_dir else {spec.name: [] for spec in ENTITY_SPECS}
        current = self._load_dataset_dir(target_dir, run["university_id"])
        entities = {spec.name: diff_entity(spec, previous[spec.name], current[spec.name]) for spec in ENTITY_SPECS}
        affected: dict[str, list[str]] = {}
        for key in ("source_ids", "entry_ids", "fact_ids", "url_ids", "context_ids"):
            values: set[str] = set()
            if key == "source_ids":
                values.update(entities["source_registry"]["added_ids"])
                values.update(entities["source_registry"]["changed_ids"])
                values.update(entities["source_registry"]["removed_ids"])
            elif key == "entry_ids":
                values.update(entities["catalog_entries"]["added_ids"])
                values.update(entities["catalog_entries"]["changed_ids"])
                values.update(entities["catalog_entries"]["removed_ids"])
            elif key == "fact_ids":
                values.update(entities["quick_facts"]["added_ids"])
                values.update(entities["quick_facts"]["changed_ids"])
                values.update(entities["quick_facts"]["removed_ids"])
            elif key == "url_ids":
                values.update(entities["url_manifest"]["added_ids"])
                values.update(entities["url_manifest"]["changed_ids"])
                values.update(entities["url_manifest"]["removed_ids"])
            elif key == "context_ids":
                values.update(entities["entity_contexts"]["added_ids"])
                values.update(entities["entity_contexts"]["changed_ids"])
                values.update(entities["entity_contexts"]["removed_ids"])
            affected[key] = sorted(values)
        affected_source_ids = set(affected["source_ids"])
        affected_source_urls: list[dict[str, str]] = []
        seen_urls: set[str] = set()
        for dataset in (previous, current):
            for source in dataset.get("source_registry", []):
                source_id = str(source.get("source_id") or "")
                if source_id not in affected_source_ids:
                    continue
                url = str(source.get("canonical_url") or source.get("source_url") or "")
                if not url or url in seen_urls:
                    continue
                seen_urls.add(url)
                affected_source_urls.append({"source_id": source_id, "url": url})
        affected["source_urls"] = sorted(affected_source_urls, key=lambda item: (item["source_id"], item["url"]))
        impact = {
            "scope": "university_current",
            "l1": {"entities": list(entities), "affected_stable_id_count": sum(len(affected[key]) for key in ("source_ids", "entry_ids", "fact_ids", "url_ids", "context_ids"))},
            "opensearch": "current documents for this university will use the published version after activation",
            "weknora": "only affected source URLs are candidates for import or supersession when WeKnora is enabled",
        }
        return {"run_id": run_id, "university_id": run["university_id"], "version_id": run["version_id"], "previous_run_id": previous_row[0] if previous_row else None, "entities": entities, "affected": affected, "impact": impact}

    def _audit(self, *, action: str, reason: str, run_id: str | None = None, university_id: str | None = None, version_id: str | None = None, batch_id: str | None = None, metadata: dict[str, Any] | None = None) -> None:
        from psycopg.types.json import Jsonb

        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO admin_audit_events (event_id, action, reason, batch_id, run_id, university_id, version_id, metadata) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (f"audit_{uuid.uuid4().hex}", action, reason, batch_id, run_id, university_id, version_id, Jsonb(metadata or {})),
            )

    def force_publish(self, run_id: str, reason: str) -> dict[str, Any]:
        reason = reason.strip()
        if not reason:
            raise ValueError("force publish reason is required")
        run = self._run_context(run_id)
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute("SELECT status, stage_failures, quality_audits FROM ingestion_runs WHERE run_id=%s", (run_id,))
            row = cursor.fetchone()
        if not row or row[0] != "failed":
            raise ValueError("only failed runs can be force-published")
        quality = row[2] or {}
        report = quality.get("quality_gate") or {}
        if report.get("quality_gate_status") != "needs_review":
            raise ValueError("only needs_review runs can be force-published")
        normalized_dir = self._run_dir(run) / "normalized"
        if not normalized_dir.exists():
            raise ValueError("normalized artifacts are unavailable for force publish")
        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            from psycopg.types.json import Jsonb

            cursor.execute(
                "UPDATE school_versions SET publication_state='staging' WHERE university_id=%s AND version_id=%s AND publication_state='failed'",
                (run["university_id"], run["version_id"]),
            )
            cursor.execute(
                "UPDATE ingestion_runs SET status='accepted', force_publish_requested=true, force_publish_reason=%s, error_message=NULL, stage_failures='[]'::jsonb, finished_at=NULL, updated_at=now() WHERE run_id=%s",
                (reason, run_id),
            )
            cursor.execute(
                "INSERT INTO admin_audit_events (event_id, action, reason, run_id, university_id, version_id, metadata) VALUES (%s, 'force_publish_requested', %s, %s, %s, %s, %s)",
                (f"audit_{uuid.uuid4().hex}", reason, run_id, run["university_id"], run["version_id"], Jsonb({"quality_gate_status": "needs_review"})),
            )
        return {"run_id": run_id, "status": "accepted", "force_publish_requested": True}

    def rollback(self, university_id: str, version_id: str, reason: str) -> dict[str, Any]:
        reason = reason.strip()
        if not reason:
            raise ValueError("rollback reason is required")
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT publication_state, dataset_version FROM school_versions WHERE university_id=%s AND version_id=%s",
                (university_id, version_id),
            )
            target = cursor.fetchone()
            cursor.execute("SELECT version_id FROM school_versions WHERE university_id=%s AND publication_state='current'", (university_id,))
            current = cursor.fetchone()
            cursor.execute("SELECT university_name, aliases, country_code, region, school_tier FROM universities WHERE university_id=%s", (university_id,))
            metadata_row = cursor.fetchone()
        if not target or target[0] != "superseded":
            raise ValueError("target version is not a superseded published version")
        if not current or current[0] == version_id:
            raise ValueError("target version is already current")
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT run_id FROM ingestion_runs WHERE university_id=%s AND version_id=%s AND status='published' ORDER BY created_at DESC LIMIT 1",
                (university_id, version_id),
            )
            run_row = cursor.fetchone()
        if not run_row:
            raise ValueError("target version has no published run")
        target_run = self._run_context(run_row[0])
        normalized_dir = self._run_dir(target_run) / "normalized"
        if not normalized_dir.exists():
            raise ValueError("target version artifacts expired and cannot be rolled back")
        from indexer.opensearch_publisher import activate_published_school, publish_school

        university_metadata = {
            "university_name": metadata_row[0] if metadata_row else university_id,
            "aliases": metadata_row[1] if metadata_row else [],
            "country_code": metadata_row[2] if metadata_row else None,
            "region": metadata_row[3] if metadata_row else None,
            "school_tier": metadata_row[4] if metadata_row else "core",
        }
        publish_school(normalized_dir, university_id, self.service.opensearch_url, university_metadata=university_metadata, activate=False)
        activate_published_school(normalized_dir, university_id, self.service.opensearch_url, university_metadata=university_metadata)
        from catalog_parser.postgres_loader import rollback_school_version

        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            rollback_school_version(connection, university_id=university_id, to_version_id=version_id)
            cursor.execute(
                "UPDATE weknora_import_jobs SET status='superseded', next_attempt_at=NULL, finished_at=COALESCE(finished_at, now()), failure_reason='l1_version_rollback', updated_at=now() WHERE university_id=%s AND version_id=%s AND status IN ('queued', 'running')",
                (university_id, current[0]),
            )
            from psycopg.types.json import Jsonb

            cursor.execute(
                "INSERT INTO admin_audit_events (event_id, action, reason, university_id, version_id, metadata) VALUES (%s, 'rollback', %s, %s, %s, %s)",
                (f"audit_{uuid.uuid4().hex}", reason, university_id, version_id, Jsonb({"previous_current_version": current[0], "run_id": run_row[0]})),
            )
        if self.service.on_published:
            self.service.on_published()
        return {"university_id": university_id, "current_version": version_id, "previous_version": current[0], "run_id": run_row[0]}

    def reimport_current(self, university_id: str) -> dict[str, Any]:
        if not weknora_import_enabled() or not os.getenv("WEKNORA_BASE_URL", "").strip():
            raise ValueError("WeKnora import is disabled or misconfigured")
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT version_id FROM school_versions WHERE university_id=%s AND publication_state='current'",
                (university_id,),
            )
            version_row = cursor.fetchone()
            cursor.execute("SELECT university_name, weknora_knowledge_base_id FROM universities WHERE university_id=%s", (university_id,))
            university_row = cursor.fetchone()
        if not version_row:
            raise ValueError("university has no current version")
        version_id = version_row[0]
        kb_id = university_row[1] if university_row else None
        if not kb_id:
            kb_id, kb_name = self.service._resolve_weknora_knowledge_base("create", None, university_id, university_row[0] if university_row else university_id)
            with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
                cursor.execute("UPDATE universities SET weknora_knowledge_base_id=%s, weknora_knowledge_base_name=%s, updated_at=now() WHERE university_id=%s", (kb_id, kb_name, university_id))
        with self._connect() as connection, connection.transaction(), connection.cursor() as cursor:
            from psycopg.types.json import Jsonb

            cursor.execute(
                """
                UPDATE source_registry
                   SET weknora_import_status='pending', weknora_knowledge_base_id=%s, updated_at=now()
                 WHERE university_id=%s AND version_id=%s AND status='active'
                RETURNING source_id, canonical_url, weknora_knowledge_id, weknora_document_id, weknora_chunk_ids, weknora_tag_ids
                """,
                (kb_id, university_id, version_id),
            )
            sources = cursor.fetchall()
            for source_id, source_url, knowledge_id, document_id, chunk_ids, tag_ids in sources:
                job_id = f"wkj_reimport_{hashlib.md5(f'{university_id}:{version_id}:{source_id}'.encode()).hexdigest()}"
                cursor.execute(
                    """
                    INSERT INTO weknora_import_jobs
                      (job_id, source_id, run_id, university_id, version_id, knowledge_base_id, knowledge_id, document_id, chunk_ids, status, source_url, tags)
                    VALUES (%s, %s, (SELECT run_id FROM ingestion_runs WHERE university_id=%s AND version_id=%s ORDER BY created_at DESC LIMIT 1), %s, %s, %s, %s, %s, COALESCE(%s, '[]'::jsonb), 'queued', %s, jsonb_build_array('university:' || %s))
                    ON CONFLICT (job_id) DO UPDATE SET status='queued', next_attempt_at=NULL, failure_reason=NULL, updated_at=now()
                    """,
                    (job_id, source_id, university_id, version_id, university_id, version_id, kb_id, knowledge_id, document_id, Jsonb(chunk_ids or []), source_url, university_id),
                )
        return {"university_id": university_id, "version_id": version_id, "queued_count": len(sources), "weknora_knowledge_base_id": kb_id}

    def cleanup_expired_artifacts(self, retention_days: int = 90) -> int:
        cutoff = datetime.now(timezone.utc) - timedelta(days=retention_days)
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT r.run_id, r.university_id
                  FROM ingestion_runs AS r
                  JOIN school_versions AS v USING (university_id, version_id)
                 WHERE r.status='published' AND v.publication_state='superseded'
                   AND r.updated_at < %s
                """,
                (cutoff,),
            )
            rows = cursor.fetchall()
        removed = 0
        root = self.service.raw_root.resolve()
        for run_id, university_id in rows:
            path = (root / str(university_id) / str(run_id)).resolve()
            try:
                path.relative_to(root)
            except ValueError:
                continue
            if path.exists():
                shutil.rmtree(path)
                removed += 1
        return removed

    def schema_catalog(self) -> dict[str, Any]:
        from catalog_parser.validation import load_schema

        items: list[dict[str, Any]] = []
        for entity, guide in JSONL_GUIDE.items():
            schema = load_schema(entity)
            items.append({"entity": entity, "schema": schema, **guide})
        return {"items": items, "relationships": [
            {"from": "catalog_entries", "field": "source_id", "to": "source_registry"},
            {"from": "quick_facts", "field": "source_id", "to": "source_registry"},
            {"from": "url_manifest", "field": "source_id", "to": "source_registry"},
            {"from": "catalog_entries", "field": "entry_id", "to": "entity_contexts"},
        ]}
