from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


FACT_QUESTION_BY_TYPE = {
    "deadline": "{school} {program} application deadline 是什么时候？",
    "application_fee": "{school} {program} application fee 是多少？",
    "english_requirement": "{school} {program} TOEFL/IELTS 要求是多少？",
    "gre_gmat_policy": "{school} {program} GRE/GMAT policy 是什么？",
    "funding_model": "{school} {program} funding/资助 模式是什么？",
    "tuition": "{school} {program} tuition 是多少？",
    "cost_of_attendance": "{school} {program} cost of attendance 是多少？",
    "financial_aid_policy": "{school} {program} financial aid policy 是什么？",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def normalized_school_ids(data_root: Path) -> list[str]:
    required = {"catalog_entries.jsonl", "quick_facts.jsonl", "url_manifest.jsonl", "source_registry.jsonl"}
    if not data_root.exists():
        return []
    return sorted(
        path.name
        for path in data_root.iterdir()
        if path.is_dir() and required.issubset({item.name for item in path.iterdir() if item.is_file()})
    )


def program_label_from_url(url: str) -> str:
    parsed = urlparse(url)
    slug = parsed.path.strip("/").split("/")[-1]
    slug = re.sub(r"^mit-", "", slug)
    slug = re.sub(r"-course-[a-z0-9-]+$", "", slug)
    return slug.replace("-", " ").strip() or parsed.netloc


def school_display_name(university_id: str, entries: list[dict[str, Any]]) -> str:
    marker = university_id.upper()
    for row in entries:
        search_text = str(row.get("search_text") or "")
        if marker in search_text:
            prefix = search_text.split(marker, 1)[0].strip()
            if 2 <= len(prefix) <= 80:
                return prefix
    return marker


def base_case(
    *,
    university_id: str,
    qa_case_id: str,
    persona: str,
    question: str,
    expected_route: str,
    expected_behavior: str,
    must_include: list[str],
    conversation_context: list[dict[str, Any]] | None = None,
    must_not_include: list[str] | None = None,
    required_source_url: str | None = None,
    risk_level: str = "P1",
    reviewer_owner: str = "qa",
) -> dict[str, Any]:
    return {
        "qa_case_id": qa_case_id,
        "university_id": university_id,
        "persona": persona,
        "question": question,
        "conversation_context": conversation_context or [],
        "expected_route": expected_route,
        "expected_behavior": expected_behavior,
        "must_include": must_include,
        "must_not_include": must_not_include or ["unsupported claim"],
        "required_source_url": required_source_url,
        "risk_level": risk_level,
        "reviewer_owner": reviewer_owner,
        "case_source": "generated_from_normalized_data",
        "human_review_required": True,
    }


def school_data(data_root: Path, university_id: str) -> dict[str, Any]:
    data_dir = data_root / university_id
    entries = load_jsonl(data_dir / "catalog_entries.jsonl")
    facts = load_jsonl(data_dir / "quick_facts.jsonl")
    manifest = load_jsonl(data_dir / "url_manifest.jsonl")
    return {
        "university_id": university_id,
        "display_name": school_display_name(university_id, entries),
        "entries": entries,
        "facts": facts,
        "manifest": manifest,
        "entry_by_id": {row["entry_id"]: row for row in entries},
    }


def catalog_candidates(school: dict[str, Any]) -> list[dict[str, Any]]:
    university_id = school["university_id"]
    display = school["display_name"]
    rows = sorted(school["entries"], key=lambda row: (row.get("level", ""), row.get("school", ""), row["entry_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        level_label = "本科" if row.get("level") == "undergraduate" else "研究生" if row.get("level") == "graduate" else "non-degree"
        course_code = f" Course {row['course_code']}" if row.get("course_code") else ""
        cases.append(
            base_case(
                university_id=university_id,
                qa_case_id=f"mvp_{university_id}_catalog_{index:03d}",
                persona="undergraduate_applicant" if row.get("level") == "undergraduate" else "graduate_applicant",
                question=f"{display} {row['program_name']}{course_code} {level_label} program 有哪些信息？",
                expected_route="catalog",
                expected_behavior="返回命中的学校目录项，并包含官方 source_url。",
                must_include=[row["program_name"], row["source_url"]],
                required_source_url=row["source_url"],
                risk_level="P1",
                reviewer_owner="content",
            )
        )
    return cases


def _program_for_fact(row: dict[str, Any], entry_by_id: dict[str, dict[str, Any]]) -> str:
    entry_id = row.get("entry_id")
    if entry_id and entry_id in entry_by_id:
        return entry_by_id[entry_id]["program_name"]
    return program_label_from_url(row["source_url"])


def fact_candidates(school: dict[str, Any]) -> list[dict[str, Any]]:
    university_id = school["university_id"]
    display = school["display_name"]
    entry_by_id = school["entry_by_id"]
    eligible = [
        row for row in school["facts"] if row.get("fact_type") in FACT_QUESTION_BY_TYPE and row.get("source_url") and row.get("raw_value")
    ]
    eligible.sort(key=lambda row: (row["fact_type"], row["source_id"], row["fact_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(eligible, start=1):
        program = _program_for_fact(row, entry_by_id)
        cases.append(
            base_case(
                university_id=university_id,
                qa_case_id=f"mvp_{university_id}_fact_{index:03d}",
                persona="graduate_applicant",
                question=FACT_QUESTION_BY_TYPE[row["fact_type"]].format(school=display, program=program),
                expected_route="fact",
                expected_behavior="返回结构化事实值，并包含该事实的官方来源。",
                must_include=[str(row["raw_value"]), row["source_url"]],
                required_source_url=row["source_url"],
                risk_level="P0" if row["fact_type"] in {"deadline", "application_fee", "english_requirement", "gre_gmat_policy"} else "P1",
                reviewer_owner="qa",
            )
        )
    return cases


def deep_candidates(school: dict[str, Any]) -> list[dict[str, Any]]:
    university_id = school["university_id"]
    display = school["display_name"]
    eligible = [
        row
        for row in school["manifest"]
        if row.get("import_status") == "success" and row.get("source_url") and row.get("url_type") in {"program_admission", "degree_chart", "catalog"}
    ]
    eligible.sort(key=lambda row: (row.get("url_type", ""), row["source_id"]))
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(eligible, start=1):
        program = program_label_from_url(row["source_url"])
        cases.append(
            base_case(
                university_id=university_id,
                qa_case_id=f"mvp_{university_id}_deep_{index:03d}",
                persona="graduate_applicant" if row.get("url_type") == "program_admission" else "content_reviewer",
                question=f"{display} {program} 是否需要进一步查看政策或背景要求？",
                expected_route="deep",
                expected_behavior="进入 scoped deep search，并只返回当前 source scope 内 evidence。",
                must_include=[row["source_url"], row["source_id"]],
                required_source_url=row["source_url"],
                risk_level="P1",
                reviewer_owner="qa",
            )
        )
    return cases


def clarification_candidates(school: dict[str, Any]) -> list[dict[str, Any]]:
    university_id = school["university_id"]
    display = school["display_name"]
    questions = [
        f"{display} CS master 怎么申请？",
        f"{display} 学费是多少？",
        f"{display} 研究生 deadline 是什么时候？",
        f"{display} 所有项目 deadline 是什么时候？",
        f"{display} tuition 是多少？",
        f"{display} 申请要求是什么？",
        f"{display} 录取难度是多少？",
    ]
    return [
        base_case(
            university_id=university_id,
            qa_case_id=f"mvp_{university_id}_clarification_{index:03d}",
            persona="parent_advisor",
            question=question,
            expected_route="clarification",
            expected_behavior="问题缺少项目、学位层级或费用年份时必须反问，不直接编造统一答案。",
            must_include=["clarify"],
            risk_level="P0" if "deadline" in question.lower() else "P1",
            reviewer_owner="qa",
        )
        for index, question in enumerate(questions, start=1)
    ]


def balanced_take(candidates_by_school: dict[str, list[dict[str, Any]]], target: int, route_name: str) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    offsets = defaultdict(int)
    school_ids = sorted(candidates_by_school)
    while len(selected) < target:
        progressed = False
        for school_id in school_ids:
            offset = offsets[school_id]
            candidates = candidates_by_school[school_id]
            if offset >= len(candidates):
                continue
            selected.append(candidates[offset])
            offsets[school_id] += 1
            progressed = True
            if len(selected) >= target:
                break
        if not progressed:
            raise RuntimeError(f"Not enough {route_name} candidates: expected {target}, got {len(selected)}")
    return selected


def build_single_turn_cases(
    data_root: Path,
    *,
    min_schools: int = 5,
    catalog_target: int = 60,
    fact_target: int = 60,
    deep_target: int = 50,
    clarification_target: int = 30,
) -> list[dict[str, Any]]:
    school_ids = normalized_school_ids(data_root)
    if len(school_ids) < min_schools:
        raise RuntimeError(f"Need at least {min_schools} normalized schools, got {len(school_ids)}")
    schools = [school_data(data_root, school_id) for school_id in school_ids]
    cases = [
        *balanced_take({school["university_id"]: catalog_candidates(school) for school in schools}, catalog_target, "catalog"),
        *balanced_take({school["university_id"]: fact_candidates(school) for school in schools}, fact_target, "fact"),
        *balanced_take({school["university_id"]: deep_candidates(school) for school in schools}, deep_target, "deep"),
        *balanced_take({school["university_id"]: clarification_candidates(school) for school in schools}, clarification_target, "clarification"),
    ]
    return cases


def conversation_candidates(school: dict[str, Any]) -> list[dict[str, Any]]:
    university_id = school["university_id"]
    display = school["display_name"]
    entry_by_id = school["entry_by_id"]
    cases: list[dict[str, Any]] = []

    by_source: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in school["facts"]:
        by_source[row["source_url"]][row["fact_type"]] = row
    for source_url, rows in sorted(by_source.items()):
        if "english_requirement" in rows and "application_fee" in rows:
            english = rows["english_requirement"]
            fee = rows["application_fee"]
            label = _program_for_fact(english, entry_by_id)
            cases.append(
                base_case(
                    university_id=university_id,
                    qa_case_id=f"mvp_{university_id}_conv_fact_{len(cases)+1:03d}",
                    persona="graduate_applicant",
                    question="那 application fee 呢？",
                    conversation_context=[
                        {
                            "role": "user",
                            "content": f"{display} {label} TOEFL/IELTS 要求是多少？",
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

    for row in sorted(school["entries"], key=lambda item: item["entry_id"]):
        cases.append(
            base_case(
                university_id=university_id,
                qa_case_id=f"mvp_{university_id}_conv_catalog_{len(cases)+1:03d}",
                persona="graduate_applicant",
                question="这个项目的官方 source_url 是哪个？",
                conversation_context=[
                    {
                        "role": "user",
                        "content": f"{display} {row['program_name']} program 有哪些信息？",
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

    for row in sorted(school["manifest"], key=lambda item: item["source_id"]):
        if (
            row.get("import_status") != "success"
            or not row.get("source_url")
            or row.get("url_type") not in {"program_admission", "degree_chart", "catalog"}
        ):
            continue
        cases.append(
            base_case(
                university_id=university_id,
                qa_case_id=f"mvp_{university_id}_conv_deep_{len(cases)+1:03d}",
                persona="graduate_applicant",
                question="这个判断的 evidence source 是什么？",
                conversation_context=[
                    {
                        "role": "user",
                        "content": f"{display} {program_label_from_url(row['source_url'])} 是否接受非相关背景？",
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

    cases.extend(
        [
            base_case(
                university_id=university_id,
                qa_case_id=f"mvp_{university_id}_conv_clarification_{index:03d}",
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
                risk_level="P0",
            )
            for index, (initial, final) in enumerate(
                [
                    (f"{display} 研究生申请 deadline 是什么时候？", "还是没有项目，可以直接给全部吗？"),
                    (f"{display} 学费是多少？", "不指定层级可以回答吗？"),
                ],
                start=1,
            )
        ]
    )
    return cases


def build_conversation_cases(data_root: Path, *, min_schools: int = 5, target: int = 50) -> list[dict[str, Any]]:
    school_ids = normalized_school_ids(data_root)
    if len(school_ids) < min_schools:
        raise RuntimeError(f"Need at least {min_schools} normalized schools, got {len(school_ids)}")
    schools = [school_data(data_root, school_id) for school_id in school_ids]
    candidates_by_route: dict[str, dict[str, list[dict[str, Any]]]] = {
        route: {} for route in ("fact", "catalog", "deep", "clarification")
    }
    for school in schools:
        school_id = school["university_id"]
        by_route: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for candidate in conversation_candidates(school):
            by_route[str(candidate.get("expected_route") or "unknown")].append(candidate)
        for route in candidates_by_route:
            candidates_by_route[route][school_id] = by_route.get(route, [])

    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()
    offsets: dict[str, dict[str, int]] = {
        route: {school_id: 0 for school_id in school_ids} for route in candidates_by_route
    }
    next_school_index: dict[str, int] = {route: 0 for route in candidates_by_route}

    def take_next(route: str) -> bool:
        start_index = next_school_index[route]
        for shift in range(len(school_ids)):
            school_index = (start_index + shift) % len(school_ids)
            school_id = school_ids[school_index]
            candidates = candidates_by_route[route][school_id]
            offset = offsets[route][school_id]
            while offset < len(candidates) and candidates[offset]["qa_case_id"] in selected_ids:
                offset += 1
            offsets[route][school_id] = offset
            if offset >= len(candidates):
                continue
            candidate = candidates[offset]
            offsets[route][school_id] += 1
            next_school_index[route] = (school_index + 1) % len(school_ids)
            selected.append(candidate)
            selected_ids.add(candidate["qa_case_id"])
            return True
        return False

    route_order = ("fact", "catalog", "deep", "clarification")
    if target >= len(route_order):
        for route in route_order:
            take_next(route)

    while len(selected) < target:
        progressed = False
        for route in route_order:
            if take_next(route):
                progressed = True
                if len(selected) >= target:
                    break
        if not progressed:
            raise RuntimeError(f"Not enough conversation candidates: expected {target}, got {len(selected)}")
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate multi-school MVP UAT cases from normalized school data.")
    parser.add_argument("--data-root", default="data/normalized")
    parser.add_argument("--single-output-path", default="qa/mvp-uat-cases.jsonl")
    parser.add_argument("--conversation-output-path", default="qa/mvp-uat-conversations.jsonl")
    parser.add_argument("--min-schools", type=int, default=5)
    parser.add_argument("--catalog-target", type=int, default=60)
    parser.add_argument("--fact-target", type=int, default=60)
    parser.add_argument("--deep-target", type=int, default=50)
    parser.add_argument("--clarification-target", type=int, default=30)
    parser.add_argument("--conversation-target", type=int, default=50)
    args = parser.parse_args()

    data_root = Path(args.data_root)
    single_turn = build_single_turn_cases(
        data_root,
        min_schools=args.min_schools,
        catalog_target=args.catalog_target,
        fact_target=args.fact_target,
        deep_target=args.deep_target,
        clarification_target=args.clarification_target,
    )
    conversations = build_conversation_cases(data_root, min_schools=args.min_schools, target=args.conversation_target)
    write_jsonl(Path(args.single_output_path), single_turn)
    write_jsonl(Path(args.conversation_output_path), conversations)
    print(f"wrote {len(single_turn)} single-turn cases to {args.single_output_path}")
    print(f"wrote {len(conversations)} conversation cases to {args.conversation_output_path}")


if __name__ == "__main__":
    main()
