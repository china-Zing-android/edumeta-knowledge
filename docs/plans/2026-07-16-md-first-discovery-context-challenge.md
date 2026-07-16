# MD-First Discovery Context Challenge Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 在不改变现有 PostgreSQL + OpenSearch + WeKnora + Fast Router + 单 MCP 工具架构的前提下，让院校、专业和多专业首次检索返回来自 MD 的阶段性上下文，并确保只有用户明确请求具体细节且 L1 不足时才调用 WeKnora。

**Architecture:** 新增一个版本化的 `entity_contexts` 物化投影，使用现有 MD 解析结果生成院校/专业上下文、少量关联实体和可继续探索主题，发布到新的全局 OpenSearch alias。Fast Router 在原有 L1 `_msearch` 中同时读取该投影；发现阶段默认返回上下文且禁止调用 WeKnora，具体事实优先查 Fact Store，只有明确细节缺失时才执行 scoped WeKnora。

**Tech Stack:** Python 3.11、Pydantic/JSON Schema、PostgreSQL 16、OpenSearch 2.15、FastAPI、现有 TypeScript MCP Gateway、pytest、Node test runner。

---

## 1. Challenge Boundary

### 1.1 本次必须完成

- 用户只输入院校时，返回院校基本信息、MD 中可推导的结构特点、3-5 个代表院系/专业和可继续探索主题。
- 用户只输入一个专业时，返回主专业、所属学院/系、学位层级、MD 结构上下文、最多 2 个高相关专业和可继续探索主题。
- 用户输入多个专业时，返回多个已解析实体的并列结构，不要求用户提供 `entry_id`。
- 上述发现请求全部 `weknora_ms=0`，WeKnora 不得被预取。
- 学费、截止日期、语言成绩等具体事实先查 `quick_facts`；Fact Store 已满足时不得调用 WeKnora。
- 只有用户明确请求材料、课程细节、文化、资格政策等内容，且 L1 无足够内容时，才允许使用已有 `source_id/knowledge_id` scope 调 WeKnora。
- HTTP 与 MCP 保持一个工具、同一响应契约；Gateway 不增加业务逻辑。
- 同院校 MD 更新只重建该校受影响的 `entity_contexts`，不触发未变化 URL 的 WeKnora job。

### 1.2 明确不做

- 不增加图数据库、Redis、向量数据库、reranker 或新的 Gateway 服务。
- 不在 Fast Router 热路径调用大模型或远程意图分类模型。
- 不建设完整 Wiki 图谱，不复制全部 WeKnora chunk 到 OpenSearch。
- 不预生成自然语言答案；Router 继续只返回结构化数据。
- 不把“怎么样、介绍一下”直接视为 WeKnora 触发条件。
- 不做排名、录取概率、职业预测或模型主观推荐。
- 不一次性解决所有自然语言意图表达；语义分类器属于后续独立挑战。
- 不改变每校独立 KB、完整 MD 快照更新和 current-version 发布机制。

### 1.3 稳定性原则

- 默认策略是 **MD-first / no-L2**。无法判断时宁可返回 MD 上下文和 `available_topics`，也不隐式调用 WeKnora。
- 意图只控制上下文深度；命中院校/专业实体时始终返回最小上下文包。
- 所有上下文必须可追溯到 MD 结构、catalog、fact 或 source metadata，不允许生成无来源“优势”。
- 对外模式继续使用 `l1/l1_l2/range/upward/clarification/not_found/error`，不增加新的 mode。
- 允许基于结构化字段做确定性组合，但代码不得单独展示：例如使用 `14-2 Mathematical Economics（数学经济学）`，并解释其为 MIT Course 编号及确定性的院系/学位关系；MD 未明确说明时不得扩写为“更偏数学”等评价。
- Router 保持无状态；多轮 `university_id/entry_id` 由 Claude、Codex、Hermes 放入下一轮 `context`，Router 只验证 scope，不新增会话存储。
- `review_required/conflict` 事实返回原始值和 warning，不包装成确认事实，也不自动调用 WeKnora；只有用户明确要求核实时才允许 scoped evidence 查询。
- Agent 呈现规范纳入契约：直接答案、必要上下文、少量相关内容、可继续探索主题。Router 不生成散文答案。

## 2. Target Contract

在现有响应中增加向后兼容字段 `context`：

```json
{
  "trace_id": "tr_xxx",
  "mode": "l1",
  "scope": {
    "university_id": "mit",
    "dataset_version": "mit_xxx",
    "stage": "discovery",
    "requested_aspects": []
  },
  "matches": [],
  "context": {
    "primary_entities": [
      {
        "entity_type": "program",
        "entity_id": "ent_mit_undergraduate_sb_14_1_economics",
        "title": "Economics",
        "attributes": {
          "course_code": "14-1",
          "degree_level": "SB",
          "department": "Economics",
          "school": "School of Humanities, Arts, and Social Sciences"
        }
      }
    ],
    "highlights": [],
    "sample_children": [],
    "related_entities": [],
    "available_topics": [
      {"topic": "tuition", "availability": "l1"},
      {"topic": "curriculum", "availability": "weknora"}
    ],
    "presentation_hints": {
      "order": ["direct_answer", "context", "related_entities", "available_topics"],
      "explain_course_codes": true,
      "max_related_entities": 2,
      "max_available_topics": 4
    },
    "provenance": {
      "origin": "md_projection",
      "dataset_version": "mit_xxx"
    }
  },
  "evidence": [],
  "missing_slots": [],
  "warnings": [],
  "timings": {"total_ms": 0, "l1_ms": 0, "weknora_ms": 0}
}
```

约束：

- `context` 始终是对象；无上下文时使用空结构，不返回 `null`。
- `primary_entities` 最多 3 个，支持多专业查询。
- `related_entities` 最多 2 个/主实体，必须带 `relation_type` 和确定性 `relation_reason`。
- `sample_children` 院校查询最多 5 个，不能把完整专业清单塞入上下文。
- `highlights` 只能来自 MD 结构化数据或明确事实，不允许模型生成宣传性描述。
- `available_topics` 表示可以继续查询的主题，不触发对应数据检索。
- `presentation_hints` 只约束 Agent 如何使用结构化结果，不包含预生成答案。
- `evidence` 仍只表示真实 WeKnora chunk；MD 上下文不得伪装成 evidence。

## 3. Deterministic Context Rules

### 3.1 院校上下文

从 current MD 的 normalized records 生成：

- `primary_entity`：大学名称、国家、地区、tier。
- `highlights`：本科/研究生项目数量、学院/系数量、交叉学科项目数量等可验证结构数据。
- `sample_children`：按稳定排序选 3-5 个学院/系和代表项目；不是按 OpenSearch score 宣称“最好”。
- `available_topics`：由 current facts 和 source topics 汇总，标记 `l1` 或 `weknora`。

### 3.2 专业上下文

从 `catalog_entries`、`catalog_entry_disciplines`、`source_entry_links` 和 facts 生成：

- 主实体以现有 `entry_id` 为稳定实体 ID，本挑战不引入第二套 program ID。
- 关系优先级：显式 cross-school/cross-discipline > 同 department + 同 level > 同 discipline + 同 level。
- 同名专业的不同学位层级不得互相替代。
- 相关专业稳定排序：关系优先级、course code、entry_id；禁止用随机 score。
- `available_topics` 先看 entry-level facts，再看 source topics，最后才继承 university-level 通用主题。

### 3.3 WeKnora Trigger Gate

```text
discovery query
  -> always L1 + context
  -> never WeKnora

explicit fact query
  -> Fact Store hit: L1 + context
  -> Fact Store miss: only then consider scoped WeKnora

explicit deep aspect query
  -> resolved university + resolved entry/source required
  -> scoped WeKnora

ambiguous scope
  -> clarification
  -> never global WeKnora
```

`program_overview`、`university_overview`、`catalog_presence` 和多专业发现均属于 discovery。`application_materials`、`curriculum_detail`、`eligibility_policy`、`student_culture` 等才属于 deep aspect。

## 4. Implementation Tasks

### Task 1: Lock the entity-context schema with failing parser tests

**Files:**

- Create: `docs/schemas/entity_contexts.schema.json`
- Create: `pipelines/catalog-parser/src/catalog_parser/entity_contexts.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/mit_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/structured_markdown_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/deep_v2_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/validation.py`
- Test: `tests/test_entity_contexts.py`
- Test: `tests/test_parser_contracts.py`

**Steps:**

1. 写失败测试：MIT 解析结果产生 university context、Course 14-1 context，14-1 关联 14-2/6-14，所有记录通过 schema。
2. 运行：`.venv/bin/python -m pytest tests/test_entity_contexts.py tests/test_parser_contracts.py -q`；预期因缺少 `entity_contexts` 失败。
3. 定义最小 schema：`context_id/entity_type/entity_id/university_id/entry_id/title/attributes/highlights/sample_children/related_entities/available_topics/source_ids/md_section_paths/dataset_version/status`。
4. 用共享 builder 从 normalized catalog/facts/sources 构建上下文；不要在三个 parser 中复制关系规则。
5. 将 `entity_contexts.jsonl` 加入 ParseResult 输出和 validation cross-reference。
6. 再次运行测试，预期通过且 MIT catalog reconciliation 仍为 157。

### Task 2: Persist and diff entity contexts in the existing control plane

**Files:**

- Create: `infra/postgres/007_entity_contexts.sql`
- Modify: `infra/postgres/001_initial_schema.sql`
- Modify: `pipelines/catalog-parser/src/catalog_parser/postgres_loader.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/diff.py`
- Modify: `apps/fast-router/src/fast_router/ingestion.py`
- Test: `tests/test_postgres_loader.py`
- Test: `tests/test_diff_school.py`

**Steps:**

1. 写失败测试：context 进入 staging/current；只修改 Course 14-1 的 MD 结构时，affected context 仅包含 MIT 相关实体，`weknora_reimport_source_ids=[]`。
2. 运行目标测试并确认失败。
3. 新增一张版本化 `entity_contexts` 表，主键沿用 `(university_id, version_id, context_id)`；JSONB 保存小型 attributes/relations/topics，不拆图关系表。
4. 把 `entity_contexts` 加入 ingestion_records、publish、supersede 和 record_counts。
5. 扩展 diff：context 变化影响 L1 发布，但不自动生成 WeKnora job。
6. 运行：`.venv/bin/python -m pytest tests/test_postgres_loader.py tests/test_diff_school.py -q`；预期通过。

### Task 3: Publish one additional global OpenSearch projection

**Files:**

- Create: `infra/opensearch/l1_entity_contexts_mapping.json`
- Modify: `pipelines/indexer/src/indexer/opensearch_publisher.py`
- Test: `tests/test_opensearch_publisher.py`

**Steps:**

1. 写失败测试：publish plan 包含 `l1_entity_contexts_current`，MIT context 数量非零，同校更新不影响其他学校。
2. 运行目标测试并确认失败。
3. 添加第五个全局 alias；映射只包含 keyword、text、boolean、date 和 object/nested 必要字段。
4. `entity_contexts` 与 universities/catalog 一样维护 `is_current`，发布失败不得切 current version。
5. 运行：`.venv/bin/python -m pytest tests/test_opensearch_publisher.py -q`；预期通过。

### Task 4: Add discovery planning and the no-speculative-WeKnora gate

**Files:**

- Create: `apps/fast-router/src/fast_router/query_planning.py`
- Modify: `apps/fast-router/src/fast_router/opensearch_retrieval.py`
- Modify: `apps/fast-router/src/fast_router/retrieval.py`
- Modify: `apps/fast-router/src/fast_router/main.py`
- Test: `tests/test_discovery_context_retrieval.py`
- Test: `tests/test_cross_university_retrieval.py`
- Test: `tests/test_fast_router_api.py`

**Steps:**

1. 写失败测试覆盖：院校发现、单专业发现、多专业发现、L1 fact、明确 deep aspect、模糊 scope。
2. 明确断言 discovery case 的 mock WeKnora 调用次数为 0。
3. 增加轻量 `QueryPlan(stage, requested_aspects, resolved_entity_hints)`；本挑战只使用保守确定性规则，不引入模型。
4. 将 entity-context 查询并入同一次 OpenSearch `_msearch`，禁止 PostgreSQL 进入热路径。
5. 组装 `context.primary_entities/highlights/sample_children/related_entities/available_topics`，按契约限量和稳定排序。
6. 调整 WeKnora gate：只有 `stage=detail`、L1 不满足、source scope 非空时才能调用。
7. 运行：`.venv/bin/python -m pytest tests/test_discovery_context_retrieval.py tests/test_cross_university_retrieval.py tests/test_fast_router_api.py -q`；预期通过。

### Task 5: Preserve the one-tool MCP contract and update architecture docs

**Files:**

- Modify: `apps/tool-gateway/test/server.test.ts`
- Modify: `docs/schemas/mcp_tools.schema.md`
- Modify: `docs/architecture/00-overview.md`
- Modify: `docs/architecture/02-data-architecture.md`
- Modify: `docs/architecture/03-runtime-call-flow.md`
- Modify: `docs/architecture/06-integration-contracts.md`
- Modify: `docs/architecture/07-quality-gates-acceptance.md`

**Steps:**

1. 更新 Gateway fixture，验证新增 `context` 字段原样透传，工具数仍为 1。
2. 运行：`cd apps/tool-gateway && npm test`；预期通过。
3. 更新架构基线：OpenSearch 从四个 alias 变为五个；发现阶段 MD-first；WeKnora 按明确细节触发。
4. 文档明确 `context != evidence`，`available_topics` 不表示已执行深检索。

### Task 6: Run the MIT challenge acceptance gate

**Files:**

- Create: `qa/discovery-context-challenge-cases.jsonl`
- Create: `qa/manual/discovery-context-challenge-review-key.md`
- Modify: `scripts/retrieval_benchmark.py`
- Modify: `scripts/runtime_acceptance.py`
- Test: `tests/test_retrieval_benchmark.py`
- Test: `tests/test_runtime_acceptance.py`

**Required cases:**

1. `MIT`：返回院校 context、代表院系/专业，`weknora_ms=0`。
2. `MIT 有 Economics 本科专业吗？`：主实体 14-1，相关 14-2/6-14，`weknora_ms=0`。
3. `MIT 有 Economics 本科专业吗？这个专业怎么样？`：仍为 MD discovery，不调用 WeKnora。
4. `MIT Economics、Mathematical Economics 和 6-14 有什么关系？`：返回多个主实体，MD-only。
5. `计算机专业的院校有哪些？`：保持 upward 结果，附少量匹配项目，不调用 WeKnora。
6. `MIT 本科 2026-2027 学费是多少？`：Fact Store 命中，不调用 WeKnora。
7. `MIT EECS PhD 申请需要提交哪些材料？`：允许 scoped WeKnora，evidence 必须来自 EECS source。
8. `EECS PhD 申请材料有哪些？`：缺学校时 clarification，不调用 WeKnora。
9. WeKnora 关闭时重复 1-6：结果仍正确。
10. 修改一个无 URL 变化的 MIT MD context：只更新 MIT context，不创建 WeKnora job。

**Acceptance thresholds:**

- 所有 discovery/fact cases `weknora_ms=0`。
- 错学校、错项目、错学位层级为 0。
- related entities 符合确定性规则且无排名语义。
- MD context 有 provenance；无来源“优势”数量为 0。
- warm HTTP discovery p95 `< 500ms`；MCP discovery p95 `< 1s`。
- 原 MIT catalog/fact/deep acceptance 不回归。
- Python、PostgreSQL integration、TypeScript Gateway、challenge cases 全部通过。

## 5. Stop/Go Gates

### Gate A: Data usefulness

先只生成 MIT `entity_contexts.jsonl` 并人工查看。若院校和 14-1 上下文仍不足以支持比“有/没有”更丰富的回答，停止进入 Router 实现，先修正 MD contract；禁止靠 Agent 补内容掩盖数据不足。

### Gate B: No speculative L2

发现和 L1 fact case 中任一 WeKnora 调用即失败。不能以“提高回答丰富度”为理由绕过此闸门。

### Gate C: Performance

新增 context `_msearch` 后 HTTP discovery p95 必须低于 500ms。若超标，先优化投影大小和查询，不引入 Redis。

### Gate D: Incremental isolation

MD context 变化不得生成 URL import job；某校 context 更新不得改写其他学校 current 文档。

### Gate E: Human task completion

人工评审必须认为首次院校/专业回答足以决定是否继续追问，同时没有把未请求的深度信息全部展开。只返回“有”或倾倒完整目录都判失败。

## 6. Expected Adjustment Surface

改动范围为中等，但边界集中：

```text
Parser contract       +1 entity output
PostgreSQL control    +1 versioned table
OpenSearch            +1 global alias
Fast Router           +1 query planner + context assembly + stricter L2 gate
HTTP/MCP contract     +1 backward-compatible context field
QA                    +1 challenge suite
```

不修改：

```text
Docker Compose component list
WeKnora import worker architecture
per-university KB lifecycle
MCP tool count
Gateway business boundary
Agent framework
L0/ranking/recommendation
```

## 7. Completion Definition

本挑战完成不等于“自然语言理解最终完成”。完成标准是：

- 首次院校/专业/多专业查询已从扁平 matches 升级为 MD-first context package。
- 用户没有明确请求深度信息时，系统绝不调用 WeKnora。
- 用户明确追问时，Fact Store 优先，缺失才进入 scoped WeKnora。
- 同一结构可供 Claude、Codex、Hermes 生成一致且不生硬的回答。
- 后续语义分类器可以替换 `QueryPlan` 的识别实现，但不改变数据、检索和 Evidence Gate 契约。
