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
    "provenance": "provenance.jsonl",
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
        "role": "主体检索数据",
        "query_rule": "问有哪些专业、学科、学位或某个专业属于哪个学院时优先查询。",
        "minimum": ["entry_id", "university_id", "school", "department", "level", "degree_level", "program_name", "source_id", "source_url", "dataset_version", "status"],
        "links": ["entry_id", "source_id", "university_id"],
    },
    "quick_facts": {
        "label": "关键事实",
        "purpose": "记录学费、截止日期、语言要求、申请费和资助等明确事实。",
        "why": "让确定性的数字和规则可以被单独校验、追踪来源并快速回答。",
        "role": "按问题调用的事实分支",
        "query_rule": "只有问题涉及学费、截止日期、申请费、语言要求或资助时才查询。",
        "minimum": ["fact_id", "university_id", "fact_type", "fact_key", "raw_value", "source_id", "source_url", "capture_date", "dataset_version", "review_status", "conflict_status"],
        "links": ["fact_id", "source_id", "entry_id", "university_id"],
    },
    "source_registry": {
        "label": "来源与 URL 主登记",
        "purpose": "在当前 MD-first 流程里，一条官方 URL 本身就是一条来源主记录。这里管理 URL 的官方性、生命周期、解析状态和 WeKnora 导入状态。",
        "why": "你提供的课程页、费用页和索引页不需要再登记一个额外的官网入口。主登记只是给这条 URL 补上稳定 ID、版本和状态，避免同一 URL 的状态散落在多处。",
        "role": "URL 来源主文件",
        "query_rule": "需要确认答案的官方证据、来源是否有效或 WeKnora 导入状态时查询。普通专业筛选不需要先查它。",
        "minimum": ["source_id", "university_id", "canonical_url", "url_type", "topics", "official_source", "priority", "status", "parser_status", "weknora_import_status", "capture_date", "last_verified", "dataset_version"],
        "links": ["source_id", "canonical_url", "university_id"],
    },
    "url_manifest": {
        "label": "URL 关联投影（兼容产物）",
        "purpose": "它不是另一份官网来源登记，而是把主来源 URL 与 entry_ids、主题和 WeKnora 文档 ID 展开，供既有脚本和按 URL 范围的检索使用。",
        "why": "MIT 里它与 source_registry 是一对一的同 URL 记录。当前 PostgreSQL 发布会把它折叠进 source_registry，因此普通维护不需要同时修改两份；保留文件是为了兼容已有解析器、下载包和导入脚本。",
        "role": "来源主文件的关联投影",
        "query_rule": "只有需要回答某个 URL 覆盖哪些专业或主题，或需要读取 URL 级 WeKnora 文档关联时才使用。",
        "minimum": ["url_id", "source_id", "university_id", "entry_ids", "source_url", "canonical_url", "url_type", "topics", "official_source", "import_status", "capture_date", "dataset_version"],
        "links": ["url_id", "source_id", "entry_ids", "university_id"],
    },
    "entity_contexts": {
        "label": "学校与专业上下文",
        "purpose": "提供学校和专业的展示上下文、亮点、关联实体和可继续追问的主题。",
        "why": "把检索结果从单个匹配记录提升为可解释的学校或专业上下文。",
        "role": "发现和范围定位",
        "query_rule": "需要确认院校、学院、上下文或可继续追问的主题时查询；已知院校和意图时可以跳过。",
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

        configured_root = os.getenv("INGESTION_SOURCE_ROOT", "").strip()
        if configured_root:
            root = Path(configured_root)
        else:
            parent = Path(os.getenv("INGESTION_SOURCE_PARENT", "data/raw-md"))
            child = parent / "universities"
            root = child if child.is_dir() else parent
        return {"universities": root.resolve()}

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
        declared_country = AdminControlPlane._metadata_value(content, "country_code", "Country code", "country", "国家")
        if declared_country and re.fullmatch(r"[A-Za-z]{2}", declared_country):
            country = declared_country.upper()
        declared_region = AdminControlPlane._metadata_value(content, "region", "Region", "地区", "所在地区")
        declared_country_name = AdminControlPlane._metadata_value(content, "country", "Country", "国家")
        if (
            declared_country_name
            and not re.fullmatch(r"[A-Za-z]{2}", declared_country_name)
            and (not declared_region or (country and declared_region.upper() == country))
        ):
            declared_region = declared_country_name
        if declared_region and country and declared_region.upper() == country:
            declared_region = None
        return {
            "university_id": candidate,
            "university_name": heading or candidate.replace("_", " ").title(),
            "country_code": country,
            "region": declared_region,
            "school_tier": "core",
            "aliases": [],
        }

    @staticmethod
    def _metadata_value(text: str, *keys: str) -> str | None:
        """Read a small metadata declaration without requiring a YAML dependency.

        Source Markdown in the wild uses both ``**Region**: ...`` and YAML-like
        ``region: ...`` lines. The admin preview only needs these lightweight
        identity fields, so keep the reader deliberately tolerant and bounded
        to the metadata already loaded for the file.
        """
        alternatives = "|".join(re.escape(key) for key in keys)
        pattern = re.compile(
            rf"^\s*(?:[-*]\s*)?(?:\*\*)?(?:{alternatives})(?:\*\*)?\s*:\s*(.+?)\s*$",
            re.IGNORECASE | re.MULTILINE,
        )
        match = pattern.search(text)
        if not match:
            return None
        value = match.group(1).strip().strip("`\"'")
        value = re.sub(r"\s+#.*$", "", value).strip().strip("`\"'")
        return value or None

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
        compute_hash: bool = True,
    ) -> dict[str, Any]:
        relative = path.relative_to(root).as_posix() if path.is_relative_to(root) else path.name
        size = path.stat().st_size
        content = path.read_text(encoding="utf-8", errors="replace")[:256 * 1024]
        inferred = self._infer_metadata(path, content)
        metadata = dict(inferred)
        if manifest:
            metadata.update({
                key: value
                for key, value in manifest.items()
                if key in {"university_id", "university_name", "country_code", "region", "school_tier", "aliases"}
                and value not in (None, "", [])
            })
        metadata.setdefault("aliases", [])
        metadata.setdefault("school_tier", "core")
        metadata.setdefault("region", None)
        metadata.setdefault("country_code", None)
        metadata.setdefault("university_name", "")
        metadata["university_id"] = str(metadata.get("university_id") or "").strip().lower()
        existing_metadata = existing.get(metadata["university_id"], {})
        for key in ("country_code", "region"):
            if not metadata.get(key) and existing_metadata.get(key):
                metadata[key] = existing_metadata[key]
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
            "sha256": _sha256(path) if compute_hash else None,
            "operation": operation,
            "issues": issues,
            "ready": not issues,
            **{key: metadata.get(key) for key in ("university_id", "university_name", "country_code", "region", "school_tier", "aliases")},
        }
        return item

    def _latest_source_runs(self, source_root_id: str) -> dict[str, dict[str, Any]]:
        """Return the newest persisted run for each server-relative Markdown path."""
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT DISTINCT ON (r.source_relative_path)
                       r.source_relative_path, r.run_id, r.university_id, r.operation,
                       r.status, r.version_id, r.updated_at,
                       (v.publication_state = 'current') AS is_current,
                       u.university_name
                  FROM ingestion_runs AS r
                  LEFT JOIN school_versions AS v
                    ON v.university_id = r.university_id
                   AND v.version_id = r.version_id
                  LEFT JOIN universities AS u
                    ON u.university_id = r.university_id
                 WHERE r.source_root_id=%s
                   AND r.source_relative_path IS NOT NULL
                 ORDER BY r.source_relative_path, r.created_at DESC, r.run_id DESC
                """,
                (source_root_id,),
            )
            rows = cursor.fetchall()
        return {
            str(row[0]): {
                "run_id": row[1],
                "university_id": row[2],
                "operation": row[3],
                "status": row[4],
                "version_id": row[5],
                "updated_at": row[6].isoformat() if row[6] else None,
                "is_current": bool(row[7]),
                "university_name": row[8],
            }
            for row in rows
        }

    def _latest_university_runs(self) -> dict[str, dict[str, Any]]:
        """Return a fallback run map for imports created before source paths existed.

        The original catalog loader created ingestion_runs but did not populate
        source_relative_path/source_root_id. Those runs still represent the
        version currently stored in PostgreSQL, so source discovery can safely
        associate the newest run by university when an exact path match is not
        available.
        """
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT DISTINCT ON (r.university_id)
                       r.university_id, r.run_id, r.university_id, r.operation,
                       r.status, r.version_id, r.updated_at,
                       (v.publication_state = 'current') AS is_current,
                       u.university_name
                  FROM ingestion_runs AS r
                  LEFT JOIN school_versions AS v
                    ON v.university_id = r.university_id
                   AND v.version_id = r.version_id
                  LEFT JOIN universities AS u
                    ON u.university_id = r.university_id
                 ORDER BY r.university_id, r.created_at DESC, r.run_id DESC
                """
            )
            rows = cursor.fetchall()
        return {
            str(row[0]): {
                "run_id": row[1],
                "university_id": row[2],
                "operation": row[3],
                "status": row[4],
                "version_id": row[5],
                "updated_at": row[6].isoformat() if row[6] else None,
                "is_current": bool(row[7]),
                "university_name": row[8],
            }
            for row in rows
        }

    def _latest_university_versions(self) -> dict[str, dict[str, Any]]:
        """Return the authoritative version when no ingestion run is linked.

        Some older catalog loads persisted ``school_versions`` without an
        ``ingestion_runs`` row that contains source metadata. The version table
        is still authoritative for publication state, so source discovery must
        not label those Markdown files as ``not_submitted`` merely because the
        run-side association is missing.
        """
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT DISTINCT ON (v.university_id)
                       v.university_id, v.version_id, v.dataset_version,
                       v.publication_state, v.created_at, v.published_at,
                       v.superseded_at, u.university_name
                  FROM school_versions AS v
                  LEFT JOIN universities AS u
                    ON u.university_id = v.university_id
                 ORDER BY v.university_id,
                          CASE v.publication_state
                            WHEN 'current' THEN 0
                            WHEN 'staging' THEN 1
                            WHEN 'failed' THEN 2
                            ELSE 3
                          END,
                          v.created_at DESC, v.version_id DESC
                """
            )
            rows = cursor.fetchall()
        return {
            str(row[0]): {
                "university_id": row[0],
                "version_id": row[1],
                "dataset_version": row[2],
                "publication_state": row[3],
                "created_at": row[4].isoformat() if row[4] else None,
                "published_at": row[5].isoformat() if row[5] else None,
                "superseded_at": row[6].isoformat() if row[6] else None,
                "university_name": row[7],
            }
            for row in rows
        }

    @staticmethod
    def _source_status_from_version(version: dict[str, Any] | None) -> str:
        if not version:
            return "not_submitted"
        return {
            "current": "published",
            "staging": "accepted",
            "failed": "failed",
            "superseded": "superseded",
        }.get(str(version.get("publication_state")), "not_submitted")

    def source_files(
        self,
        *,
        source_root_id: str | None = None,
        source_relative_path: str | None = None,
        query: str | None = None,
        status: str | None = None,
        limit: int = 200,
        offset: int = 0,
        include_hash: bool = False,
    ) -> dict[str, Any]:
        """List Markdown files that exist in configured server source roots.

        A source file is deliberately not treated as an ingestion run. It stays
        visible with ``not_submitted`` until the operator creates a preview and
        commits it into the durable ingestion queue.
        """
        if source_root_id:
            root_ids = [source_root_id]
        else:
            root_ids = sorted(self.roots)
        existing = self._existing_universities()
        needle = (query or "").strip().lower()
        requested_status = (status or "").strip().lower()
        collected: list[dict[str, Any]] = []
        latest_university_versions = self._latest_university_versions()

        for root_id in root_ids:
            root = self._root(root_id)
            if not root.exists() or not root.is_dir():
                continue
            target = self._safe_path(root, source_relative_path) if source_relative_path else root
            if not target.is_dir():
                raise ValueError("source path must be a directory")
            manifest_rows = self._read_manifest(root)
            latest_runs = self._latest_source_runs(root_id)
            latest_university_runs = self._latest_university_runs()
            for path in sorted(target.rglob("*.md")):
                if not path.is_file() or path.is_symlink():
                    continue
                relative = path.relative_to(root).as_posix()
                item = self._make_item(
                    path,
                    root=root,
                    root_id=root_id,
                    manifest=manifest_rows.get(relative),
                    existing=existing,
                    compute_hash=include_hash,
                )
                run = latest_runs.get(relative) or latest_university_runs.get(item["university_id"])
                version = latest_university_versions.get(item["university_id"])
                source_status = run["status"] if run else self._source_status_from_version(version)
                searchable = " ".join(
                    str(value or "")
                    for value in (item["filename"], item["relative_path"], item["university_id"], item["university_name"])
                ).lower()
                if needle and needle not in searchable:
                    continue
                if requested_status and requested_status != source_status:
                    continue
                stat = path.stat()
                collected.append({
                    "filename": item["filename"],
                    "relative_path": item["relative_path"],
                    "source_root_id": root_id,
                    "size_bytes": item["size_bytes"],
                    "modified_at": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                    "sha256": item["sha256"],
                    "university_id": item["university_id"],
                    "university_name": item["university_name"],
                    "country_code": item["country_code"],
                    "region": item["region"],
                    "school_tier": item["school_tier"],
                    "operation": item["operation"],
                    "issues": item["issues"],
                    "ready": item["ready"],
                    "source_status": source_status,
                    "run_id": run["run_id"] if run else None,
                    "run_university_id": run["university_id"] if run else None,
                    "run_university_name": run["university_name"] if run else None,
                    "run_operation": run["operation"] if run else None,
                    "run_version_id": run["version_id"] if run else None,
                    "run_updated_at": run["updated_at"] if run else None,
                    "version_id": run["version_id"] if run else (version["version_id"] if version else None),
                    "dataset_version": version["dataset_version"] if version else None,
                    "version_state": version["publication_state"] if version else None,
                    "version_updated_at": (
                        version["published_at"] or version["created_at"]
                        if version
                        else None
                    ),
                    "is_current": run["is_current"] if run else bool(version and version["publication_state"] == "current"),
                })

        collected.sort(key=lambda item: (str(item["source_root_id"]), str(item["relative_path"])))
        safe_limit = min(max(limit, 1), 500)
        safe_offset = max(offset, 0)
        return {
            "items": collected[safe_offset:safe_offset + safe_limit],
            "total_count": len(collected),
            "limit": safe_limit,
            "offset": safe_offset,
            "source_root_id": source_root_id,
            "source_relative_path": source_relative_path,
        }

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

    def _artifact_path_for_run(self, run: dict[str, Any], artifact: str) -> Path:
        """Resolve the public artifact name to its immutable run snapshot path."""
        filename = ARTIFACTS[artifact]
        run_dir = self._run_dir(run)
        return run_dir / filename if artifact == "raw_markdown" else run_dir / "normalized" / filename

    def artifacts(self, run_id: str) -> dict[str, Any]:
        run = self._run_context(run_id)
        items: list[dict[str, Any]] = []
        for artifact, filename in ARTIFACTS.items():
            path = self._artifact_path_for_run(run, artifact)
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
        path = self._artifact_path_for_run(run, artifact)
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

    def provenance(self, run_id: str, entity: str, record_id: str) -> dict[str, Any]:
        if entity not in {"catalog_entries", "quick_facts"}:
            raise ValueError("provenance is available for catalog_entries and quick_facts only")
        mapping_path = self.artifact_path(run_id, "provenance")
        mapping: dict[str, Any] | None = None
        with mapping_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                candidate = json.loads(line)
                identity = candidate.get("jsonl") or {}
                if identity.get("entity") == entity and identity.get("record_id") == record_id:
                    mapping = candidate
                    break
        if mapping is None:
            raise ValueError("provenance mapping not found")

        jsonl_path = self.artifact_path(run_id, entity)
        jsonl_line: int | None = None
        jsonl_record: dict[str, Any] | None = None
        with jsonl_path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                candidate = json.loads(line)
                if candidate.get("entry_id") == record_id or candidate.get("fact_id") == record_id:
                    jsonl_line = line_number
                    jsonl_record = candidate
                    break
        if jsonl_record is None or jsonl_line is None:
            raise ValueError("JSONL record for provenance mapping not found")

        md_start = int(mapping["md"]["line_start"])
        md_end = int(mapping["md"]["line_end"])
        markdown = self.artifact_page(
            run_id,
            "raw_markdown",
            offset=max(0, md_start - 3),
            limit=max(1, min(20, md_end - md_start + 5)),
        )
        markdown["highlighted_range"] = {"line_start": md_start, "line_end": md_end}
        markdown["items"] = [
            {
                **item,
                "highlighted": md_start <= int(item.get("line", 0)) <= md_end,
            }
            for item in markdown["items"]
        ]
        return {
            "mapping": mapping,
            "jsonl": {"artifact": entity, "line": jsonl_line, "record": jsonl_record},
            "markdown": markdown,
        }

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
                path = self._artifact_path_for_run(run, artifact)
                if path.is_file():
                    archive.write(path, arcname=filename if artifact == "raw_markdown" else f"normalized/{filename}")
        return output

    def _version_items(self, university_id: str, rows: list[tuple[Any, ...]]) -> list[dict[str, Any]]:
        cutoff = datetime.now(timezone.utc) - timedelta(days=90)
        version_items: list[dict[str, Any]] = []
        for row in rows:
            version_university_id = str(row[16] or university_id) if len(row) > 16 else university_id
            publication_state = row[2]
            superseded_at = row[7]
            run_id = row[8]
            artifact_available = False
            if run_id:
                within_retention = publication_state in {"current", "failed", "staging"}
                if publication_state == "superseded":
                    within_retention = bool(superseded_at and superseded_at >= cutoff)
                if within_retention:
                    artifact_available = (self.service.raw_root / version_university_id / str(run_id) / "normalized").is_dir()
            version_items.append({
                "university_id": version_university_id,
                "university_name": row[13],
                "country_code": row[14],
                "region": row[15],
                "version_id": row[0],
                "dataset_version": row[1],
                "publication_state": publication_state,
                "input_hash": row[3],
                "record_counts": row[4] or {},
                "created_at": row[5].isoformat(),
                "published_at": row[6].isoformat() if row[6] else None,
                "superseded_at": superseded_at.isoformat() if superseded_at else None,
                "run_id": run_id,
                "run_status": row[9],
                "source_filename": row[10],
                "source_relative_path": row[11],
                "source_root_id": row[12],
                "artifact_available": artifact_available,
                "rollback_available": publication_state == "superseded" and artifact_available,
            })
        return version_items

    def _version_query(self, where_sql: str = "") -> str:
        return f"""
            SELECT v.version_id, v.dataset_version, v.publication_state, v.input_hash,
                   v.record_counts, v.created_at, v.published_at, v.superseded_at,
                   r.run_id, r.status, r.source_filename, r.source_relative_path,
                   r.source_root_id, u.university_name, u.country_code, u.region,
                   v.university_id
              FROM school_versions AS v
              LEFT JOIN universities AS u
                ON u.university_id = v.university_id
              LEFT JOIN LATERAL (
                SELECT run_id, status, source_filename, source_relative_path, source_root_id
                  FROM ingestion_runs
                 WHERE university_id=v.university_id AND version_id=v.version_id
                 ORDER BY created_at DESC LIMIT 1
              ) AS r ON true
             {where_sql}
             ORDER BY v.created_at DESC, v.university_id, v.version_id
        """

    def versions(self, university_id: str) -> dict[str, Any]:
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(self._version_query("WHERE v.university_id=%s"), (university_id,))
            rows = cursor.fetchall()
        return {
            "university_id": university_id,
            "items": self._version_items(university_id, rows),
        }

    def list_versions(
        self,
        *,
        query: str | None = None,
        publication_state: str | None = None,
        limit: int = 200,
        offset: int = 0,
    ) -> dict[str, Any]:
        clauses: list[str] = []
        params: list[Any] = []
        if query and query.strip():
            pattern = f"%{query.strip()}%"
            clauses.append("(v.university_id ILIKE %s OR u.university_name ILIKE %s OR v.dataset_version ILIKE %s OR COALESCE(r.source_filename, '') ILIKE %s)")
            params.extend([pattern, pattern, pattern, pattern])
        if publication_state and publication_state.strip():
            clauses.append("v.publication_state=%s")
            params.append(publication_state.strip())
        where_sql = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        safe_limit = min(max(limit, 1), 500)
        safe_offset = max(offset, 0)
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                f"{self._version_query(where_sql)} LIMIT %s OFFSET %s",
                (*params, safe_limit, safe_offset),
            )
            rows = cursor.fetchall()
        items = self._version_items("", rows)
        return {
            "items": items,
            "total_count": len(items),
            "limit": safe_limit,
            "offset": safe_offset,
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
