from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


DEEP_SOURCE_HINTS = [
    "electrical_engineering_and_computer_science",
    "chemical_engineering",
    "nuclear_science_and_engineering",
    "mechanical_engineering",
    "architecture",
    "biology",
    "aeronautics_and_astronautics",
    "materials_science_and_engineering",
    "civil_and_environmental_engineering",
    "economics",
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def program_label_from_url(url: str) -> str:
    slug = urlparse(url).path.strip("/").split("/")[-1]
    slug = re.sub(r"^mit-", "", slug)
    slug = re.sub(r"-course-[a-z0-9-]+$", "", slug)
    return slug.replace("-", " ").strip()


def base_case(
    *,
    qa_case_id: str,
    persona: str,
    question: str,
    conversation_context: list[dict[str, Any]],
    expected_route: str,
    expected_behavior: str,
    must_include: list[str],
    must_not_include: list[str] | None = None,
    required_source_url: str | None = None,
    risk_level: str = "P1",
    reviewer_owner: str = "qa",
) -> dict[str, Any]:
    return {
        "qa_case_id": qa_case_id,
        "persona": persona,
        "question": question,
        "conversation_context": conversation_context,
        "expected_route": expected_route,
        "expected_behavior": expected_behavior,
        "must_include": must_include,
        "must_not_include": must_not_include or ["Stanford", "unsupported claim"],
        "required_source_url": required_source_url,
        "risk_level": risk_level,
        "reviewer_owner": reviewer_owner,
    }


def fact_conversations(facts: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    by_source: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in facts:
        by_source[row["source_url"]][row["fact_type"]] = row
    eligible = [
        (source_url, rows)
        for source_url, rows in by_source.items()
        if "english_requirement" in rows and "application_fee" in rows
    ]
    eligible.sort(key=lambda item: item[0])
    cases: list[dict[str, Any]] = []
    for index, (source_url, rows) in enumerate(eligible[:limit], start=1):
        label = program_label_from_url(source_url)
        english = rows["english_requirement"]
        fee = rows["application_fee"]
        cases.append(
            base_case(
                qa_case_id=f"mvp_mit_conv_fact_{index:03d}",
                persona="graduate_applicant",
                question="那 application fee 呢？",
                conversation_context=[
                    {
                        "role": "user",
                        "content": f"MIT {label} TOEFL/IELTS 要求是多少？",
                        "expected_route": "fact",
                        "must_include": [str(english["raw_value"]), source_url],
                        "risk_level": "P0",
                    }
                ],
                expected_route="fact",
                expected_behavior="多轮追问保持同一项目 scope，从语言要求追问到申请费，并附官方来源。",
                must_include=[str(fee["raw_value"]), source_url],
                required_source_url=source_url,
                risk_level="P0",
            )
        )
    return cases


def catalog_conversations(entries: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    ordered = sorted(entries, key=lambda row: (row.get("level", ""), row.get("school", ""), row["entry_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(ordered[:limit], start=1):
        level_label = "本科" if row.get("level") == "undergraduate" else "研究生"
        course_code = f" Course {row['course_code']}" if row.get("course_code") else ""
        cases.append(
            base_case(
                qa_case_id=f"mvp_mit_conv_catalog_{index:03d}",
                persona="undergraduate_applicant" if row.get("level") == "undergraduate" else "graduate_applicant",
                question="这个项目的官方 source_url 是哪个？",
                conversation_context=[
                    {
                        "role": "user",
                        "content": f"MIT {row['program_name']}{course_code} {level_label} program 有哪些信息？",
                        "expected_route": "catalog",
                        "must_include": [row["program_name"]],
                    }
                ],
                expected_route="catalog",
                expected_behavior="多轮追问保持目录项 scope，返回同一项目的官方目录或项目 URL。",
                must_include=[row["program_name"], row["source_url"]],
                required_source_url=row["source_url"],
                risk_level="P1",
                reviewer_owner="content",
            )
        )
    return cases


def deep_conversations(manifest: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for hint in DEEP_SOURCE_HINTS:
        for row in manifest:
            if hint in row.get("source_id", "") and row.get("import_status") == "success":
                candidates.append(row)
                break
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(candidates[:limit], start=1):
        label = program_label_from_url(row["source_url"])
        cases.append(
            base_case(
                qa_case_id=f"mvp_mit_conv_deep_{index:03d}",
                persona="graduate_applicant",
                question="这个判断的 evidence source 是什么？",
                conversation_context=[
                    {
                        "role": "user",
                        "content": f"MIT {label} 是否接受非 CS 背景？",
                        "expected_route": "deep",
                        "must_include": [row["source_url"]],
                    }
                ],
                expected_route="deep",
                expected_behavior="多轮追问保持 deep evidence scope，返回同一 source_id/source_url 的 evidence。",
                must_include=[row["source_url"], row["source_id"]],
                required_source_url=row["source_url"],
                risk_level="P1",
            )
        )
    return cases


def clarification_conversations() -> list[dict[str, Any]]:
    pairs = [
        ("MIT 研究生申请 deadline 是什么时候？", "还是没有项目，可以直接给全部吗？"),
        ("MIT 学费是多少？", "不指定层级可以回答吗？"),
        ("MIT CS master 怎么申请？", "只说 CS master 可以直接给吗？"),
        ("MIT 所有项目 deadline 是什么时候？", "不用项目名可以给统一答案吗？"),
        ("MIT tuition 是多少？", "不指定年份和层级可以答吗？"),
    ]
    return [
        base_case(
            qa_case_id=f"mvp_mit_conv_clarification_{index:03d}",
            persona="parent_advisor",
            question=final,
            conversation_context=[
                {
                    "role": "user",
                    "content": initial,
                    "expected_route": "clarification",
                    "must_include": ["clarification"],
                    "risk_level": "P0",
                }
            ],
            expected_route="clarification",
            expected_behavior="用户连续给出模糊范围时必须继续反问，不编造全校统一答案。",
            must_include=["clarification"],
            required_source_url=None,
            risk_level="P0",
        )
        for index, (initial, final) in enumerate(pairs, start=1)
    ]


def build_cases(data_dir: Path) -> list[dict[str, Any]]:
    facts = load_jsonl(data_dir / "quick_facts.jsonl")
    entries = load_jsonl(data_dir / "catalog_entries.jsonl")
    manifest = load_jsonl(data_dir / "url_manifest.jsonl")
    cases = [
        *fact_conversations(facts, 20),
        *catalog_conversations(entries, 15),
        *deep_conversations(manifest, 10),
        *clarification_conversations(),
    ]
    if len(cases) != 50:
        raise RuntimeError(f"Expected 50 generated conversation cases, got {len(cases)}")
    return cases


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate executable MIT MVP multi-turn UAT cases from normalized MIT data.")
    parser.add_argument("--data-dir", default="data/normalized/mit")
    parser.add_argument("--output-path", default="qa/mvp-uat-conversations.jsonl")
    args = parser.parse_args()

    rows = build_cases(Path(args.data_dir))
    write_jsonl(Path(args.output_path), rows)
    print(f"wrote {len(rows)} conversation cases to {args.output_path}")


if __name__ == "__main__":
    main()
