from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


def tokenize(text: str) -> set[str]:
    normalized = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", " ", text.lower())
    tokens = {t for t in normalized.split() if t}
    synonyms = {
        "ai": {"artificial", "intelligence", "decision"},
        "cs": {"computer", "science", "computing"},
        "eecs": {"electrical", "engineering", "computer", "science"},
        "course6": {"electrical", "engineering", "computer", "science"},
        "toefl": {"english", "requirement"},
        "ielts": {"english", "requirement"},
        "ea": {"early", "action", "deadline"},
        "need": {"financial", "aid", "need", "blind", "full"},
        "blind": {"financial", "aid", "need", "blind"},
        "needblind": {"financial", "aid", "need", "blind"},
        "need-blind": {"financial", "aid", "need", "blind"},
        "学费": {"tuition", "cost"},
        "资助": {"funding", "aid"},
        "国际生": {"international", "aid"},
        "背景": {"background", "requirement"},
    }
    for token in list(tokens):
        tokens.update(synonyms.get(token, set()))
    return tokens


CATALOG_STOP_TOKENS = {
    "a",
    "an",
    "and",
    "are",
    "for",
    "in",
    "list",
    "of",
    "program",
    "programs",
    "related",
    "the",
    "to",
    "what",
    "which",
}


def normalize_catalog_query(query: str) -> str:
    """Remove catalog-intent wording that is not a program attribute."""
    normalized = query.lower()
    for phrase in ["有哪些", "相关", "专业", "项目", "方向", "学校", "大学"]:
        normalized = normalized.replace(phrase, " ")
    for phrase in ["本科", "undergraduate", "bachelor"]:
        normalized = normalized.replace(phrase, " ")
    return normalized


PROGRAM_HINTS = [
    ("eecs", "electrical_engineering_and_computer_science"),
    ("electrical engineering and computer science", "electrical_engineering_and_computer_science"),
    ("chemical engineering", "chemical_engineering"),
    ("nuclear science and engineering", "nuclear_science_and_engineering"),
    ("nuclear engineering", "nuclear_science_and_engineering"),
    ("mechanical engineering", "mechanical_engineering"),
    ("architecture", "architecture"),
    ("biology", "biology"),
    ("sloan mba", "mit_sloan_mba_program"),
    ("sloan executive mba", "mit_sloan_executive_mba_program"),
    ("sloan master of finance", "mit_sloan_master_of_finance"),
    ("master of finance", "mit_sloan_master_of_finance"),
    ("aeronautics and astronautics", "aeronautics_and_astronautics"),
    ("materials science and engineering", "materials_science_and_engineering"),
    ("civil and environmental engineering", "civil_and_environmental_engineering"),
    ("economics", "economics"),
]


def phrase_in_query(query: str, phrase: str) -> bool:
    words = [re.escape(part) for part in re.split(r"[^a-z0-9]+", phrase.lower()) if part]
    if not words:
        return False
    pattern = r"(?<![a-z0-9])" + r"[^a-z0-9]+".join(words) + r"(?![a-z0-9])"
    return bool(re.search(pattern, query.lower()))


def detect_program_hints(query: str) -> list[str]:
    q = query.lower()
    hints: list[str] = []
    for phrase, slug_value in PROGRAM_HINTS:
        if phrase_in_query(q, phrase):
            hints.append(slug_value)
    return hints


def matches_program_hint(text: str, hint: str) -> bool:
    variants = {
        hint,
        hint.replace("_", "-"),
        hint.replace("_", " "),
    }
    for variant in variants:
        if re.search(rf"(?<![a-z0-9]){re.escape(variant)}(?![a-z0-9])", text):
            return True
    return False


def source_slug_tokens(source_url: str) -> set[str]:
    slug = urlparse(source_url).path.strip("/").split("/")[-1]
    slug = re.sub(r"^mit-", "", slug.lower())
    slug = re.sub(r"-course-[a-z0-9-]+$", "", slug)
    return tokenize(slug)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


@dataclass
class KnowledgeStore:
    data_root: Path

    @classmethod
    def from_env(cls) -> "KnowledgeStore":
        return cls(Path(os.getenv("KNOWLEDGE_DATA_ROOT", "data/normalized")))

    def school_dir(self, university_id: str) -> Path:
        return self.data_root / university_id

    def university_ids(self) -> list[str]:
        if not self.data_root.exists():
            return []
        return sorted(path.name for path in self.data_root.iterdir() if path.is_dir())

    def university_aliases(self, university_id: str) -> set[str]:
        aliases = {university_id.lower(), university_id.upper().lower()}
        for row in self.catalog_entries(university_id)[:10]:
            search_text = str(row.get("search_text") or "")
            marker = university_id.upper()
            if marker in search_text:
                prefix = search_text.split(marker, 1)[0].strip()
                if 2 <= len(prefix) <= 80:
                    aliases.add(prefix.lower())
            for field in ("university_name",):
                value = row.get(field)
                if isinstance(value, str) and value.strip():
                    aliases.add(value.strip().lower())
        return {alias for alias in aliases if alias}

    def catalog_entries(self, university_id: str) -> list[dict[str, Any]]:
        return load_jsonl(self.school_dir(university_id) / "catalog_entries.jsonl")

    def facts(self, university_id: str) -> list[dict[str, Any]]:
        return load_jsonl(self.school_dir(university_id) / "quick_facts.jsonl")

    def url_manifest(self, university_id: str) -> list[dict[str, Any]]:
        return load_jsonl(self.school_dir(university_id) / "url_manifest.jsonl")

    def source_registry(self, university_id: str) -> list[dict[str, Any]]:
        return load_jsonl(self.school_dir(university_id) / "source_registry.jsonl")

    def resolve_university(self, query: str, university_id: str | None = None) -> dict[str, Any]:
        if university_id:
            return {"university_id": university_id, "confidence": 1.0, "candidates": []}
        q = query.lower()
        candidates = self.university_ids() or ["mit"]
        matches: list[tuple[int, int, str, str]] = []
        for candidate in candidates:
            aliases = self.university_aliases(candidate)
            if candidate == "mit":
                aliases.add("massachusetts institute of technology")
            for alias in sorted(aliases, key=len, reverse=True):
                if not alias:
                    continue
                match = re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", q)
                if match:
                    matches.append((match.start(), -len(alias), candidate, alias))
        if matches:
            _, _, candidate, alias = sorted(matches)[0]
            return {"university_id": candidate, "confidence": 1.0, "candidates": [], "matched_alias": alias}
        return {"university_id": None, "confidence": 0.0, "candidates": candidates}

    def search_catalog(self, university_id: str, query: str, top_k: int = 10, level: str | None = None) -> list[dict[str, Any]]:
        effective_level = level
        if not effective_level and any(term in query.lower() for term in ["本科", "undergraduate", "bachelor"]):
            effective_level = "undergraduate"

        alias_tokens: set[str] = set()
        for alias in self.university_aliases(university_id):
            alias_tokens.update(tokenize(alias))
        q_tokens = tokenize(normalize_catalog_query(query)) - alias_tokens - CATALOG_STOP_TOKENS
        eligible_rows = [
            row
            for row in self.catalog_entries(university_id)
            if not effective_level or row.get("level") == effective_level
        ]

        # A scope-only request such as "MIT 本科专业" should browse the requested catalog
        # scope. A specific query must have an actual program/degree attribute match.
        if not q_tokens:
            return eligible_rows[:top_k]

        scored: list[tuple[float, dict[str, Any]]] = []
        for row in eligible_rows:
            haystack = " ".join(str(row.get(k) or "") for k in [
                "program_name",
                "canonical_program_name",
                "course_code",
                "degree_level",
                "department",
                "school",
            ])
            r_tokens = tokenize(haystack)
            score = len(q_tokens & r_tokens)
            if row.get("course_code") and str(row["course_code"]).lower() in query.lower():
                score += 5
            if row.get("program_name", "").lower() in query.lower():
                score += 6
            if score > 0:
                scored.append((score, row))
        scored.sort(key=lambda x: (-x[0], str(x[1].get("program_name") or ""), str(x[1].get("entry_id") or "")))
        return [row for _, row in scored[:top_k]]

    def lookup_facts(self, university_id: str, query: str, fact_types: list[str] | None = None, top_k: int = 10) -> list[dict[str, Any]]:
        q_tokens = tokenize(query)
        requested = set(fact_types or infer_fact_types(query))
        program_hints = detect_program_hints(query)
        scored: list[tuple[float, dict[str, Any]]] = []
        for row in self.facts(university_id):
            if requested and row.get("fact_type") not in requested:
                continue
            haystack = " ".join(str(row.get(k) or "") for k in [
                "fact_id",
                "fact_key",
                "fact_type",
                "raw_value",
                "source_url",
            ])
            score = len(q_tokens & tokenize(haystack))
            fact_id = row.get("fact_id", "")
            q_lower = query.lower()
            source_url = row.get("source_url", "").lower()
            slug_tokens = source_slug_tokens(source_url)
            if slug_tokens and slug_tokens <= q_tokens:
                score += 8 + len(slug_tokens)
            for hint in program_hints:
                if matches_program_hint(fact_id, hint) or matches_program_hint(source_url, hint):
                    score += 12
                elif "sloan_mba" in hint and "executive_mba" in fact_id and "executive" not in q_lower:
                    score -= 8
            if "eecs" in q_tokens and "electrical_engineering_and_computer_science" in fact_id:
                score += 10
            if "cs" in q_tokens and "computer_science" in fact_id:
                score += 4
            if "phd" in q_lower and "phd" in fact_id:
                score += 3
            if ("本科" in query or "undergraduate" in q_lower) and "undergraduate" in fact_id:
                score += 8
            if ("国际生" in query or "international" in q_lower) and "international" in haystack.lower():
                score += 6
            if row.get("fact_type") in requested:
                score += 2
            if score > 0:
                scored.append((score, row))
        scored.sort(key=lambda x: x[0], reverse=True)
        if not requested:
            return [row for _, row in scored[:top_k]]
        selected: list[dict[str, Any]] = []
        per_type_count: dict[str, int] = {}
        per_type_limit = 1 if len(requested) == 1 else max(1, min(3, top_k))
        for _, row in scored:
            fact_type = row.get("fact_type")
            if per_type_count.get(fact_type, 0) >= per_type_limit:
                continue
            selected.append(row)
            per_type_count[fact_type] = per_type_count.get(fact_type, 0) + 1
            if len(selected) >= top_k:
                break
        return selected

    def find_url_scope(
        self,
        university_id: str,
        query: str,
        entry_id: str | None = None,
        topic: str | None = None,
        source_id: str | None = None,
        top_k: int = 5,
    ) -> list[dict[str, Any]]:
        q_tokens = tokenize(" ".join([query, topic or ""]))
        q_lower = query.lower()
        program_hints = detect_program_hints(query)
        admission_terms = {"deadline", "截止", "toefl", "ielts", "det", "gre", "gmat", "申请费", "funding", "资助"}
        scored: list[tuple[float, dict[str, Any]]] = []
        exact_admission_rows: list[tuple[float, dict[str, Any]]] = []
        for row in self.url_manifest(university_id):
            if source_id and row.get("source_id") != source_id:
                continue
            if entry_id and entry_id not in row.get("entry_ids", []):
                continue
            if topic and topic not in row.get("topics", []):
                # Do not hard-fail: score lower because MIT source topics are coarse in MVP.
                pass
            haystack = " ".join([
                row.get("source_url", ""),
                row.get("url_type", ""),
                " ".join(row.get("topics", [])),
                " ".join(row.get("entry_ids", [])),
            ])
            score = len(q_tokens & tokenize(haystack))
            haystack_lower = haystack.lower()
            exact_program_match = False
            for hint in program_hints:
                if matches_program_hint(haystack_lower, hint):
                    exact_program_match = True
                    score += 12
                elif "sloan_mba" in hint and "executive_mba" in haystack_lower and "executive" not in q_lower:
                    score -= 8
            if row.get("url_type") == "program_admission" and any(term in q_lower for term in admission_terms):
                score += 4
            if source_id and row.get("source_id") == source_id:
                score += 8
            if entry_id and entry_id in row.get("entry_ids", []):
                score += 5
            if topic and topic in row.get("topics", []):
                score += 3
            if score > 0:
                scored.append((score, row))
                if exact_program_match and row.get("url_type") == "program_admission" and any(term in q_lower for term in admission_terms):
                    exact_admission_rows.append((score, row))
        scored.sort(key=lambda x: x[0], reverse=True)
        if exact_admission_rows:
            exact_admission_rows.sort(key=lambda x: x[0], reverse=True)
            return [row for _, row in exact_admission_rows[:top_k]]
        return [row for _, row in scored[:top_k]]

    def source_by_id(self, university_id: str, source_id: str) -> dict[str, Any] | None:
        for row in self.source_registry(university_id):
            if row.get("source_id") == source_id:
                return row
        return None


def infer_route(query: str) -> str:
    q = query.lower()
    q_tokens = tokenize(query)
    if "cs master" in q or ("cs" in q_tokens and "master" in q_tokens):
        return "clarification"
    if ("学费" in query or "费用" in query or "tuition" in q) and not any(x in q for x in ["undergraduate", "graduate", "2026", "2027"]) and not any(x in query for x in ["本科", "研究生"]):
        return "clarification"
    if (
        any(x in query for x in ["研究生", "所有项目", "全部项目"])
        and any(x in q for x in ["deadline", "截止"])
        and not detect_program_hints(query)
    ):
        return "clarification"
    if (
        "是否" in query
        and detect_program_hints(query)
        and any(term in q for term in ["toefl", "ielts", "det", "duolingo", "gre", "gmat", "funding", "资助", "奖学金", "require"])
    ):
        return "deep"
    if any(term in q for term in ["deadline", "截止", "toefl", "ielts", "det", "duolingo", "gre", "gmat", "申请费", "application fee", "学费", "tuition", "fee", "funding", "资助", "奖学金", "coa", "cost", "费用", "threshold", "tuition-free"]):
        return "fact"
    if any(term in q for term in ["是否", "接受", "适合", "背景", "need-blind", "need blind", "课程设置", "偏理论"]):
        return "deep"
    if any(term in q for term in ["有哪些", "list", "program", "专业", "项目", "学院", "方向"]):
        return "catalog"
    return "clarification"


def infer_fact_types(query: str) -> list[str]:
    q = query.lower()
    q_tokens = tokenize(query)
    result: list[str] = []
    if "deadline" in q or "截止" in q or "ea" in q_tokens or "ra" in q_tokens:
        result.append("deadline")
    if any(x in q for x in ["申请费", "application fee", "fee"]):
        result.append("application_fee")
    if any(x in q for x in ["toefl", "ielts", "det", "语言"]):
        result.append("english_requirement")
    if any(x in q for x in ["gre", "gmat", "标化"]):
        result.append("gre_gmat_policy")
    if any(x in q for x in ["funding", "资助", "奖学金"]):
        result.append("funding_model")
    if any(x in q for x in ["学费", "tuition"]):
        result.append("tuition")
    if any(x in q for x in ["cost", "coa", "费用"]):
        result.append("cost_of_attendance")
    if any(x in q for x in ["need-blind", "need blind", "full-need", "助学金", "income", "threshold", "tuition-free"]):
        result.append("financial_aid_policy")
    return result


def answer_from_facts(facts: list[dict[str, Any]]) -> str:
    parts = []
    for fact in facts:
        parts.append(f"{fact['fact_key']}: {fact['raw_value']} (source: {fact['source_url']}, captured {fact['capture_date']})")
    return "\n".join(parts)


def evidence_from_scope(store: KnowledgeStore, university_id: str, scopes: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    evidence: list[dict[str, Any]] = []
    for scope in scopes:
        source_id = scope["source_id"]
        if scope.get("import_status") != "success":
            continue
        source = store.source_by_id(university_id, source_id)
        if not source:
            continue
        if source.get("weknora_import_status") != "success":
            continue
        related_facts = [f for f in store.facts(university_id) if f.get("source_id") == source_id]
        snippet = "; ".join(f"{f['fact_key']}: {f['raw_value']}" for f in related_facts[:5])
        if not snippet:
            snippet = f"Source registered for topics: {', '.join(scope.get('topics', []))}."
        evidence.append({
            "evidence_id": f"ev_{source_id}",
            "source_id": source_id,
            "source_url": scope["source_url"],
            "capture_date": scope.get("capture_date"),
            "import_status": scope.get("import_status"),
            "weknora_document_id": scope.get("weknora_document_id"),
            "weknora_chunk_ids": scope.get("weknora_chunk_ids", []),
            "topics": scope.get("topics", []),
            "snippet": snippet,
        })
    return evidence
