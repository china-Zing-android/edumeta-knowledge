# MD-First Discovery Context Gate A Report

**Date:** 2026-07-16

**Status:** conditional pass

## Scope

Gate A only validates the normalized MD context projection. It does not change PostgreSQL, OpenSearch, Fast Router, MCP responses, or WeKnora routing.

## Generated Artifact

- `data/challenge/md-first-discovery/mit/entity_contexts.jsonl`
- 1 university context
- 157 program contexts
- Total contexts: 158

## MIT University Context

The projection can return, without WeKnora:

- 55 undergraduate SB programs.
- 17 undergraduate minors.
- 85 graduate degree offerings.
- 7 explicitly cross-school catalog entries.
- Five sampled major schools, with limited department and program examples.
- Available follow-up topics marked as `l1` or `weknora` without executing them.

The school sample is selected deterministically by catalog coverage and includes Engineering, SHASS, Science, Architecture and Planning, and Sloan. It is not presented as a ranking.

## MIT Economics 14-1 Context

The projection resolves:

```text
Primary: 14-1 Economics
Course code meaning: MIT Course number
Level / degree: undergraduate / SB
Department: Economics
School: School of Humanities, Arts, and Social Sciences
Related:
  - 6-14 Computer Science, Economics, and Data Science
    relation: shared Economics discipline and explicit cross-school program
  - 14-2 Mathematical Economics
    relation: same university, department, study level, and degree level
Available L1 topics:
  cost of attendance, deadline, English requirement, financial aid, tuition
Available WeKnora topic:
  curriculum
```

`14-2` is never returned as a bare code. The structured label is `14-2 Mathematical Economics`; Agent presentation may translate the title, but may not infer that it is more mathematical unless evidence explicitly supports that claim.

## Example Allowed Agent Rendering

> 有。MIT 的 Economics 本科项目是 `14-1 Economics`，其中 `14-1` 是 MIT 的 Course 编号。该项目授予 SB 学位，隶属于 School of Humanities, Arts, and Social Sciences 的 Economics 系。
>
> 当前 MD 还显示两个相关方向：跨学院的 `6-14 Computer Science, Economics, and Data Science`，以及同属 Economics 系本科 SB 层级的 `14-2 Mathematical Economics`。
>
> 目前可以继续了解学费、就读成本、申请截止日期和英语要求；课程细节需要在你明确追问后再检索对应官方页面。

## Explicit Limitation

The current MIT MD does not contain a program-level description of 14-1 curriculum, educational focus, strengths, career outcomes, or student fit. It only contains catalog structure, relationships, institutional facts, and URL scope. Therefore:

- Gate A passes the goal of returning more than a bare yes/no answer.
- Gate A does not authorize claims about program strengths or what students study.
- `这个专业怎么样` can receive structure, related options, and exploration topics, but not a qualitative program review from MD alone.
- Curriculum or program-detail claims require an explicit user follow-up and scoped WeKnora evidence unless future MD versions add approved program summaries.

## Quality Corrections Made During Gate A

- Replaced ambiguous graduate labels such as `Architecture` with `Architecture (MArch)` / `Architecture (PhD)`.
- Removed duplicate related labels.
- Capped related programs at 2 and topic source samples at 5.
- Limited university section paths and source samples to prevent context dumping.
- Replaced the ambiguous combined undergraduate count with 55 SB + 17 Minor.
- Selected school samples by deterministic catalog coverage rather than alphabetical order or score.
- Avoided `advantage`, ranking, recommendation, and unsupported qualitative language.

## Verification

```text
Entity context tests: 6 passed
Focused parser tests: 35 passed, 8 subtests passed
Full Python suite: 146 passed, 7 skipped, 8 subtests passed
MIT reconciliation: 157 catalog entries
```

## Gate Decision

Proceed to PostgreSQL/OpenSearch/Router integration only after review accepts this product boundary:

```text
First response = MD structure + related entities + next-topic navigation
Not included = unsupported program-quality narrative
Explicit detail = L1 fact first, then scoped WeKnora if missing
```
