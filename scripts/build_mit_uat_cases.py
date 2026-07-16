from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


FACT_QUESTION_BY_TYPE = {
    "deadline": "MIT {program} application deadline 是什么时候？",
    "application_fee": "MIT {program} application fee 是多少？",
    "english_requirement": "MIT {program} TOEFL/IELTS 要求是多少？",
    "gre_gmat_policy": "MIT {program} GRE/GMAT policy 是什么？",
    "funding_model": "MIT {program} funding/资助 模式是什么？",
    "tuition": "MIT {program} tuition 是多少？",
    "cost_of_attendance": "MIT {program} cost of attendance 是多少？",
    "financial_aid_policy": "MIT {program} financial aid policy 是什么？",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def program_label_from_url(url: str) -> str:
    parsed = urlparse(url)
    slug = parsed.path.strip("/").split("/")[-1]
    slug = re.sub(r"^mit-", "", slug)
    slug = re.sub(r"-course-[a-z0-9-]+$", "", slug)
    return slug.replace("-", " ").strip() or parsed.netloc


def catalog_question(row: dict[str, Any]) -> str:
    level = row.get("level")
    level_label = "本科" if level == "undergraduate" else "研究生" if level == "graduate" else "minor"
    course_code = row.get("course_code")
    code_part = f" Course {course_code}" if course_code else ""
    return f"MIT {row['program_name']}{code_part} {level_label} program 有哪些信息？"


def fact_question(row: dict[str, Any]) -> str:
    fact_type = row["fact_type"]
    program = program_label_from_url(row["source_url"])
    fact_key = str(row.get("fact_key") or "")
    if fact_type == "deadline" and "early_action" in fact_key:
        return "MIT undergraduate EA deadline 是什么时候？"
    if fact_type == "deadline" and "regular_action" in fact_key:
        return "MIT undergraduate regular action deadline 是什么时候？"
    return FACT_QUESTION_BY_TYPE[fact_type].format(program=program)


def base_case(
    *,
    qa_case_id: str,
    persona: str,
    question: str,
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
        "conversation_context": [],
        "expected_route": expected_route,
        "expected_behavior": expected_behavior,
        "must_include": must_include,
        "must_not_include": must_not_include or ["Stanford", "unsupported claim"],
        "required_source_url": required_source_url,
        "risk_level": risk_level,
        "reviewer_owner": reviewer_owner,
    }


def catalog_cases(entries: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    ordered = sorted(entries, key=lambda row: (row.get("level", ""), row.get("school", ""), row["entry_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(ordered[:limit], start=1):
        cases.append(
            base_case(
                qa_case_id=f"mvp_mit_catalog_{index:03d}",
                persona="undergraduate_applicant" if row.get("level") == "undergraduate" else "graduate_applicant",
                question=catalog_question(row),
                expected_route="catalog",
                expected_behavior="返回命中的 MIT 目录项，并包含官方 source_url。",
                must_include=[row["program_name"], row["source_url"]],
                required_source_url=row["source_url"],
                risk_level="P1",
                reviewer_owner="content",
            )
        )
    return cases


def fact_cases(facts: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    eligible = [
        row
        for row in facts
        if row.get("fact_type") in FACT_QUESTION_BY_TYPE and row.get("source_url") and row.get("raw_value")
    ]
    eligible.sort(key=lambda row: (row["fact_type"], row["source_id"], row["fact_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(eligible[:limit], start=1):
        cases.append(
            base_case(
                qa_case_id=f"mvp_mit_fact_{index:03d}",
                persona="graduate_applicant",
                question=fact_question(row),
                expected_route="fact",
                expected_behavior="返回结构化事实值，并包含该事实的官方来源。",
                must_include=[str(row["raw_value"]), row["source_url"]],
                required_source_url=row["source_url"],
                risk_level="P0" if row["fact_type"] in {"deadline", "application_fee", "english_requirement", "gre_gmat_policy"} else "P1",
                reviewer_owner="qa",
            )
        )
    return cases


def deep_cases(url_manifest: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    eligible = [
        row
        for row in url_manifest
        if row.get("import_status") == "success" and row.get("source_url") and row.get("url_type") in {"program_admission", "degree_chart"}
    ]
    eligible.sort(key=lambda row: (row.get("url_type", ""), row["source_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(eligible[:limit], start=1):
        program = program_label_from_url(row["source_url"])
        cases.append(
            base_case(
                qa_case_id=f"mvp_mit_deep_{index:03d}",
                persona="graduate_applicant" if row.get("url_type") == "program_admission" else "content_reviewer",
                question=f"MIT {program} 是否需要进一步查看政策或背景要求？",
                expected_route="deep",
                expected_behavior="进入 scoped deep search，并只返回当前 source scope 内 evidence。",
                must_include=[row["source_url"], row["source_id"]],
                required_source_url=row["source_url"],
                risk_level="P1",
                reviewer_owner="qa",
            )
        )
    return cases


def clarification_cases() -> list[dict[str, Any]]:
    questions = [
        "MIT CS master 怎么申请？",
        "MIT 学费是多少？",
        "MIT 研究生 deadline 是什么时候？",
        "MIT CS master 有哪些方向？",
        "MIT 费用是多少？",
        "MIT tuition 是多少？",
        "MIT 所有项目 deadline 是什么时候？",
        "MIT 全部项目申请截止日期是什么？",
        "MIT CS master 有哪些项目？",
        "MIT 研究生申请什么时候截止？",
    ]
    return [
        base_case(
            qa_case_id=f"mvp_mit_clarification_{index:03d}",
            persona="parent_advisor",
            question=question,
            expected_route="clarification",
            expected_behavior="问题缺少项目、学位层级或费用年份时必须反问，不直接编造统一答案。",
            must_include=["clarify"],
            required_source_url=None,
            risk_level="P0" if "deadline" in question.lower() or "截止" in question else "P1",
            reviewer_owner="qa",
        )
        for index, question in enumerate(questions, start=1)
    ]


def build_cases(data_dir: Path) -> list[dict[str, Any]]:
    entries = load_jsonl(data_dir / "catalog_entries.jsonl")
    facts = load_jsonl(data_dir / "quick_facts.jsonl")
    manifest = load_jsonl(data_dir / "url_manifest.jsonl")
    cases = [
        *catalog_cases(entries, 80),
        *fact_cases(facts, 80),
        *deep_cases(manifest, 30),
        *clarification_cases(),
    ]
    if len(cases) != 200:
        raise RuntimeError(f"Expected 200 generated UAT cases, got {len(cases)}")
    return cases


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate executable MIT MVP UAT QA cases from normalized MIT data.")
    parser.add_argument("--data-dir", default="data/normalized/mit")
    parser.add_argument("--output-path", default="qa/mvp-uat-cases.jsonl")
    args = parser.parse_args()

    rows = build_cases(Path(args.data_dir))
    write_jsonl(Path(args.output_path), rows)
    print(f"wrote {len(rows)} cases to {args.output_path}")


if __name__ == "__main__":
    main()
