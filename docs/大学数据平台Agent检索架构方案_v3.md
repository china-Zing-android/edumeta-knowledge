# 大学数据平台 Agent 检索架构方案

> ⚠️ **HISTORICAL / SUPERSEDED（2026-07-15）**：本文档描述的 L0 + L1 + L2 Agent 平台方向已**不再是 active baseline**。当前实现基线已切换为聚焦的 **L1 + WeKnora 检索子系统**，见 `docs/architecture/00-overview.md` 与计划 `docs/plans/2026-07-15-l1-weknora-retrieval-correction.md`。本文档仅作历史设计参考保留，其中的 L0 客户端、Redis、Langfuse、五个 MCP 工具、四入口一致性等内容均已从活跃架构中移除。

> 版本：v3.0  
> 目标：用 L0 + L1 支持 3 秒内快速问答，用 L2 支持准确的深度证据检索和报告生成。  
> 语言约定：正文使用中文，技术名词保留英文原名，例如 OpenSearch、Redis、WeKnora、MCP、FastAPI、TypeScript、Python。

---

## 1. 方案结论

推荐采用三层能力，但不要把三层理解成三套主数据。

| 层级 | 定义 | 主要职责 | 技术栈 | 是否是主数据 |
|---|---|---|---|---|
| L0 | 权威结构化数据能力 | 国家、院校、校区、学院/系、学位层级、专业；通过 API/MCP 提供确定性查询 | 现有 DB + 现有 API/MCP | 是 |
| L1 | 轻量目录检索 + L0 到 L2 的地址簿 | 快速检索专业目录、专业 URL、topic、WeKnora knowledge_id；帮助 L2 限定检索范围 | OpenSearch + Redis + catalog parser | 不是主数据，是检索索引和路由层 |
| L2 | 深度证据知识库 | URL 原文、申请要求、课程、学费、政策、页面快照、chunk 证据 | WeKnora + object storage + metadata | 是证据库，不是目录主库 |

核心原则：

```text
非深度问题：Fast Router → L0 + L1 → 快速回答
复杂问题：Fast Router → L0 定范围 → L1 找 URL/knowledge_id → L2 深度检索 → 带证据回答
报告问题：Fast Router → Workflow → L0 + L1 + L2 多步编排
```

L1 的角色非常薄：它不是人工知识图谱，也不是复杂映射表，而是把院校目录 md 自动拆成可检索的 `catalog_entries`、`url_manifest` 和 `quick_facts`。

---

## 2. 为什么必须保留 L1

L0 已经有结构化实体，不需要重复抽实体。但 L0 和 L2 之间缺少一层“地址簿”。

L0 知道：

```text
MIT → School of Engineering → EECS → undergraduate → Computer Science and Engineering
```

L2 知道：

```text
某个 URL 的正文、chunk、申请要求、课程、学费、deadline、source_url、knowledge_id
```

中间需要知道：

```text
这个学校 / 学院 / 专业 / 学位 / topic，应该去 L2 的哪些 URL 或 knowledge_id 里查？
```

这就是 L1。

L1 解决两个问题：

1. **快速目录检索**：比如“MIT 有哪些 AI 相关本科专业？”不需要进 L2。
2. **深度检索路由**：比如“MIT EECS PhD 是否接受非 CS 背景？”先通过 L1 找到 EECS PhD 对应 URL / knowledge_id，再去 L2 限定范围检索。

---

## 3. 技术栈总览

### 3.1 组件选型

| 组件 | 推荐技术 | 用在哪里 | 为什么选它 | 可替代方案 |
|---|---|---|---|---|
| L0 主库 | 现有 DB，常见为 PostgreSQL / MySQL | 已有国家、院校、校区、学院/系、学位层级、专业 | 已经入库且有 API/MCP，不需要推倒重做 | 保留现有即可 |
| L0 API/MCP | 现有 API + MCP Server | 对 Agent 暴露结构化数据能力 | MCP 适合把数据库查询、API 调用暴露为 tool | REST / gRPC |
| Fast Router | Python FastAPI 优先 | 轻路由、L0/L1/L2 调用编排、置信度门禁 | Python 对 NLP、embedding、检索实验更快 | TypeScript NestJS，如果团队全栈统一 TS |
| Tool Gateway | TypeScript NestJS / Node.js | 对外提供 MCP tool、鉴权、限流、会话接入 | 和前端、Agent 网关集成更方便 | Python FastAPI 直接暴露 MCP |
| L1 搜索索引 | OpenSearch | catalog_entries、url_manifest、quick_facts 搜索 | 支持 keyword + semantic hybrid search、filter、boost、faceting | Elasticsearch、PostgreSQL FTS + pgvector |
| L1 缓存 | Redis | 热门 catalog、URL scope、低风险结果缓存 | 低延迟、适合 key-value、semantic cache | KeyDB、Dragonfly |
| L2 知识库 | WeKnora | URL 原文、chunk、RAG、Wiki、deep evidence search | 已在测试，支持 RAG、Agent、Wiki、knowledge_id/tag 范围检索 | Dify、RAGFlow、自研 RAG |
| 对象存储 | S3 / MinIO / OSS / COS | 原始 HTML、PDF、normalized markdown、catalog json | 保存可追溯快照和版本 | 本地文件系统，仅限 MVP |
| Embedding | bge-m3 / text-embedding-3-large / 内部 embedding 服务 | L1 semantic search、L2 chunk embedding | 提升自然语言召回 | 纯 BM25 起步 |
| Reranker | bge-reranker / Cohere Rerank / Jina Reranker | L2 深度问题和报告证据排序 | 深度问题准确性优先 | MVP 可先不用 |
| Observability | Langfuse | 记录 query、路由、工具调用、LLM、检索、成本、延迟 | 便于调试和评估 | OpenTelemetry + 自研日志 |

### 3.2 推荐语言

| 模块 | 推荐语言 | 原因 |
|---|---|---|
| Fast Router | Python + FastAPI | 检索、NLP、embedding、评估、实验迭代快 |
| L1 parser / data pipeline | Python | 解析 md、生成 JSONL、调用 OpenSearch/Redis/WeKnora 方便 |
| MCP / Tool Gateway | TypeScript + NestJS | 如果现有 Agent 网关、前端、MCP Server 是 TS，统一维护更好 |
| 后台任务 | Python Celery / Dramatiq / APScheduler | 处理解析、索引、重建、刷新 |
| 前端调用 | TypeScript | 常规 Web 产品栈 |

推荐落地方式：

```text
TypeScript Tool Gateway：负责 MCP、鉴权、会话、前端/Agent 接入
Python Fast Router：负责轻路由、检索编排、L0/L1/L2 调用
Python Data Pipeline：负责 md 解析、索引构建、WeKnora 导入
```

---

## 4. 数据结构设计

### 4.1 L0：保留现有结构化数据

L0 已有：

```text
国家 → 院校 → 校区 → 学院/系 → 学位层级 → 专业
```

L0 继续负责权威结构化能力，不重复建设实体库。

L0 必须至少能提供这些 API/MCP tool：

```yaml
resolve_university:
  input: { text: string }
  output: { university_id, name, aliases, confidence }

get_university_tree:
  input: { university_id }
  output: { campuses, schools, departments, degree_levels, programs }

search_l0_programs:
  input: { university_id?, school?, department?, degree_level?, keyword? }
  output: { programs }
```

### 4.2 L1：catalog_entries

从院校 md 自动解析出来，一条记录代表一个可检索目录项。

```json
{
  "entry_id": "mit_ug_6_4_sb",
  "university_id": "mit",
  "school": "School of Engineering",
  "department": "Electrical Engineering and Computer Science",
  "level": "undergraduate",
  "degree_level": "SB",
  "course_code": "6-4",
  "program_name": "Artificial Intelligence and Decision Making",
  "source_url": "https://catalog.mit.edu/degree-charts/artifical-intelligence-decision-making-course-6-4/",
  "topics": ["catalog", "curriculum", "degree_chart"],
  "version": "v2.0",
  "capture_date": "2026-07-04",
  "search_text": "MIT Artificial Intelligence Decision Making Course 6-4 undergraduate SB EECS AI computer science"
}
```

存储位置：

```text
OpenSearch index: l1_catalog_entries_current
Object storage: universities/{university_id}/catalog_entries.jsonl
Redis: catalog:{university_id}:{version}
```

### 4.3 L1：url_manifest

L1 到 L2 的地址簿。

```json
{
  "url_id": "mit_eecs_phd_oge",
  "university_id": "mit",
  "entry_id": "mit_grad_eecs_phd",
  "program_name": "Electrical Engineering and Computer Science",
  "degree_level": "PhD",
  "source_url": "https://oge.mit.edu/programs/electrical-engineering-and-computer-science/",
  "topics": ["admission_requirements", "english_requirement", "standardized_tests", "funding"],
  "weknora_knowledge_id": "wk_xxx",
  "last_crawled": "2026-07-04",
  "content_hash": "sha256_xxx"
}
```

存储位置：

```text
OpenSearch index: l1_url_manifest_current
Object storage: universities/{university_id}/url_manifest.jsonl
Redis: url_scope:{entry_id}:{topic}:{version}
```

### 4.4 L1：quick_facts

高频事实字段，能结构化就不要每次进 L2。

```json
{
  "fact_id": "mit_eecs_phd_english_requirement",
  "university_id": "mit",
  "entry_id": "mit_grad_eecs_phd",
  "program_name": "Electrical Engineering and Computer Science",
  "degree_level": "PhD",
  "fact_type": "english_requirement",
  "value": {
    "ielts_min": "7",
    "toefl_min": "100"
  },
  "source_url": "https://oge.mit.edu/programs/electrical-engineering-and-computer-science/",
  "capture_date": "2026-07-04",
  "confidence": 0.95
}
```

适合进入 quick_facts 的字段：

```text
deadline
application_fee
GRE/GMAT policy
IELTS/TOEFL/DET minimum
tuition
funding model
application platform
```

### 4.5 L2：WeKnora chunk metadata

WeKnora 中每个文档或 chunk 至少需要这些 metadata：

```yaml
metadata:
  university_id: mit
  entry_id: mit_grad_eecs_phd
  school: School of Engineering
  department: Electrical Engineering and Computer Science
  degree_level: PhD
  level: graduate
  topic: admission_requirements
  source_url: https://oge.mit.edu/programs/electrical-engineering-and-computer-science/
  capture_date: 2026-07-04
  content_hash: sha256_xxx
  version: v2.0
```

---

## 5. OpenSearch 索引设计

### 5.1 l1_catalog_entries_current

用途：目录类快速检索。

核心字段：

```text
entry_id: keyword
university_id: keyword
school: text + keyword
department: text + keyword
level: keyword
degree_level: keyword
course_code: keyword
program_name: text + keyword
program_name_zh: text
aliases: text + keyword
topics: keyword
source_url: keyword
search_text: text
embedding: knn_vector
version: keyword
capture_date: date
```

检索方式：

```text
1. filter: university_id / level / degree_level
2. exact match: course_code / program_name.keyword / aliases.keyword
3. BM25: program_name / aliases / school / department / search_text
4. semantic vector: embedding(search_text)
5. hybrid score: keyword + semantic 合并
6. rerank: 按 exact、degree、topic、URL 可靠性重排
```

### 5.2 l1_url_manifest_current

用途：从 L1 找 L2 检索范围。

核心字段：

```text
url_id
university_id
entry_id
source_url
topics
weknora_knowledge_id
content_hash
last_crawled
version
```

检索方式：

```text
filter: university_id, entry_id, topics
exact: source_url, weknora_knowledge_id
fallback: program_name / department / topic BM25
```

### 5.3 l1_quick_facts_current

用途：高频事实快速回答。

核心字段：

```text
fact_id
university_id
entry_id
fact_type
value
source_url
capture_date
confidence
version
```

检索方式：

```text
filter: university_id, fact_type, degree_level
keyword: program_name / department
exact: entry_id
fallback: L2 deep_search
```

---

## 6. Fast Router 设计

### 6.1 Fast Router 的职责

Fast Router 不重新建设实体库，也不做复杂知识图谱。它只做四件事：

```text
1. 判断问题属于 catalog / fact / deep / report / clarification
2. 调 L0 解析学校和基础范围
3. 调 L1 做目录、URL、quick facts 检索
4. 决定直接回答、反问，还是转 L2
```

### 6.2 Route 类型

| Route | 典型问题 | 主要数据源 | 是否进 L2 | 目标速度 |
|---|---|---|---|---|
| catalog | “MIT 有哪些 AI 相关本科专业？” | L0 + L1 catalog_entries | 否 | p95 < 3s |
| fact | “MIT EECS PhD 雅思多少？” | L1 quick_facts，缺失再 L2 | 视情况 | p95 < 3s，缺失后转深度 |
| deep | “是否接受非 CS 背景？” | L0 + L1 url_manifest + L2 | 是 | 准确优先 |
| report | “生成 MIT AI 方向申请报告” | L0 + L1 + L2 workflow | 是 | 准确优先 |
| clarification | “MIT CS master 要求？” | 先反问 | 否 | 快速反问 |

### 6.3 轻量意图识别策略

第一版不要用大模型做默认分类，使用规则 + 小模型/LLM fallback。

规则优先：

| 触发词 | Route |
|---|---|
| 有哪些、list、majors、programs、专业、学院、方向、related | catalog |
| deadline、截止、DDL、IELTS、TOEFL、GRE、GMAT、申请费、学费、tuition、fee | fact |
| 是否接受、背景、要求解释、课程偏向、适合、难度、policy、curriculum | deep |
| 报告、对比、推荐、选校、规划、timeline | report |
| 学校/项目不明确、多个候选接近 | clarification |

低置信时才调用 LLM fallback：

```json
{
  "input": "MIT CS master 要求是什么？",
  "output": {
    "route": "clarification",
    "reason": "MIT CS master 不对应一个唯一项目，可能指 EECS、CSE、IDSS、ORC 等"
  }
}
```

### 6.4 轻量实体解析策略

不重复建设实体库。只抽取三类必要信息：

```text
university：通过 L0 resolve_university
level / degree_level：通过少量词典归一化
keyword/topic：保留用户原始关键词，交给 OpenSearch 检索
```

例子：

```text
用户：MIT 有哪些 AI 相关本科专业？
Fast Router 输出：
route = catalog
university_id = mit
level = undergraduate
query_keywords = [AI, artificial intelligence, computer science]
```

不需要预先识别 `entry_id`，也不需要 L0-L1 program 强映射。

### 6.5 Confidence Gate

Fast Router 的结果分三种：

```text
fast：可以直接答
clarification：问题范围不清，需要反问
deep_required：需要 L2 证据检索
```

判断依据：

| 条件 | 处理 |
|---|---|
| university_id 明确，route=catalog，L1 命中高 | fast |
| route=fact，quick_facts 命中且有 source_url | fast |
| route=fact，但 quick_facts 缺失 | deep_required |
| route=deep/report | deep_required |
| 学校、项目、学位层级有多个候选 | clarification |

---

## 7. 不同场景如何检索

### 7.1 场景 A：目录类快速问答

问题：

```text
MIT 有哪些 AI 相关本科专业？
```

流程：

```text
Fast Router: route=catalog
L0: resolve_university("MIT") → mit
L1 OpenSearch: filter university_id=mit, level=undergraduate; query="AI artificial intelligence computer science"
Redis: 缓存结果
Answer Composer: 模板化回答
```

OpenSearch 检索：

```text
filter:
  university_id = mit
  level = undergraduate
should:
  course_code exact
  program_name BM25
  aliases BM25
  search_text BM25
  embedding semantic search
```

输出：

```text
专业列表 + 学院/系 + degree_level + source_url + 可继续深查的按钮
```

### 7.2 场景 B：结构化基础问题

问题：

```text
MIT 有哪些学院？
```

流程：

```text
Fast Router: route=catalog
L0: get_university_tree(mit)
Redis: catalog:mit:v2 命中则直接返回
```

不需要 OpenSearch，不需要 L2。

### 7.3 场景 C：高频事实快速问答

问题：

```text
MIT EECS PhD 雅思和托福要求是多少？
```

流程：

```text
Fast Router: route=fact
L0: resolve_university("MIT") → mit
L1 OpenSearch: 找 EECS PhD entry
L1 quick_facts: fact_type=english_requirement
如果命中：直接答，并附 source_url / capture_date
如果缺失：转 L2 deep_search
```

quick_facts 检索：

```text
filter:
  university_id = mit
  fact_type = english_requirement
should:
  program_name = EECS
  degree_level = PhD
```

### 7.4 场景 D：深度证据问题

问题：

```text
MIT EECS PhD 是否接受非计算机背景？
```

流程：

```text
Fast Router: route=deep
L0: resolve_university("MIT") → mit
L1: 找 EECS PhD 的 source_url / weknora_knowledge_id
L2 WeKnora: 限定 knowledge_id 或 source_url + topic=admission_requirements 检索
Reranker: 重排 evidence chunks
Evidence Gate: 检查 source_url、capture_date、topic、program 是否匹配
Answer Composer: 带引用回答，证据不足则反问或说明缺失
```

不允许全局搜索所有学校的知识库。

### 7.5 场景 E：模糊问题反问

问题：

```text
MIT CS master 要求是什么？
```

原因：

```text
MIT 的 “CS master” 不是一个唯一项目，可能指 EECS、CSE、IDSS、ORC、Sloan MBAn 等方向。
```

处理：

```text
Fast Router: route=clarification
返回候选：
1. Electrical Engineering and Computer Science
2. Computational Science and Engineering PhD
3. Institute for Data, Systems, and Society
4. Operations Research Center
5. MIT Sloan Master of Business Analytics
```

### 7.6 场景 F：报告生成

问题：

```text
帮我生成 MIT AI / Data 方向研究生申请报告。
```

流程：

```text
Fast Router: route=report
Workflow Step 1: L1 找候选项目
Workflow Step 2: quick_facts 查 deadline、test、fee、funding
Workflow Step 3: L2 查课程、背景要求、政策解释
Workflow Step 4: Rerank + Evidence Gate
Workflow Step 5: 生成报告，列出假设、缺失、引用
```

报告不追求 3 秒，准确性优先。

---

## 8. 调用流程

### 8.1 对外 MCP tool

建议只给 Agent 暴露少量高层 tool，避免 Agent 直接乱调底层工具。

```yaml
fast_university_answer:
  description: 快速回答目录、基础事实，并判断是否需要 L2
  input:
    query: string
    locale: zh-CN | en
  output:
    mode: fast | clarification | deep_required
    route: catalog | fact | deep | report
    answer: string
    structured_data: object
    next_actions: array

deep_university_search:
  description: 在限定学校、专业、URL、topic 范围内做 L2 证据检索
  input:
    university_id: string
    entry_id?: string
    topic?: string
    question: string
  output:
    answer: string
    evidence: array
    missing_evidence: array

generate_admission_report:
  description: 多步生成申请报告
  input:
    student_profile: object
    target_scope: object
  output:
    report: object
    citations: array
```

### 8.2 Fast Router 内部伪代码

```python
def fast_university_answer(query: str, locale: str = "zh-CN"):
    route = classify_route(query)
    university = l0.resolve_university(query)

    if not university or university.confidence < 0.7:
        return clarify("未能确认学校", candidates=university.candidates)

    if route == "catalog":
        results = l1.search_catalog_entries(
            university_id=university.id,
            query=query,
            filters=extract_light_filters(query)
        )
        if results.confidence >= 0.75:
            return compose_fast_answer(results)
        return clarify("目录范围不够明确", candidates=results.candidates)

    if route == "fact":
        entry_candidates = l1.search_catalog_entries(university.id, query)
        facts = l1.lookup_quick_facts(entry_candidates, query)
        if facts.complete:
            return compose_fact_answer(facts)
        return deep_required(scope=entry_candidates, missing=facts.missing)

    if route in ["deep", "report"]:
        scope = l1.find_url_scope(university.id, query)
        return deep_required(scope=scope)

    return clarify("问题需要进一步确认")
```

---

## 9. 延迟目标

| 链路 | p95 目标 | 说明 |
|---|---:|---|
| L0 Redis 命中 | < 100ms | 学校树、热门目录 |
| L1 OpenSearch catalog 查询 | 100–500ms | 目录类问题主路径 |
| quick_facts 查询 | 100–500ms | 高频事实主路径 |
| Fast Router 端到端 | < 3s | 包含轻量生成和网络耗时 |
| L2 deep_search | 3–10s+ | 证据准确优先，不强求 3 秒 |
| report workflow | 30s+ | 可异步或流式展示阶段结果 |

---

## 10. 更新策略

每次院校数据更新：

```text
1. 生成或更新院校 md
2. parser 输出 catalog_entries.jsonl、url_manifest.jsonl、quick_facts.jsonl
3. 写入 object storage 作为版本快照
4. 增量写入 OpenSearch 新索引或 current 索引
5. 更新 Redis cache key，按 version 失效
6. URL 原文进入 WeKnora，更新 knowledge_id / content_hash
7. 记录到 Langfuse / 日志系统，便于回溯
```

索引建议：

```text
l1_catalog_entries_v20260704
l1_catalog_entries_v20260715
l1_catalog_entries_current → alias 指向最新版本
```

不需要人工维护大映射表。

---

## 11. 权限、版本和证据要求

深度回答必须经过 Evidence Gate：

```text
source_url 必须存在
capture_date 必须存在
content_hash 必须存在
university_id 必须匹配
topic 必须匹配
如果有 program/entry，必须匹配或说明不确定
如果证据冲突，不强行合并
```

快速回答可以只返回目录，但要至少带：

```text
program_name
school / department
degree_level
source_url
version 或 capture_date
```

---

## 12. 推荐 MVP 范围

第一阶段只做 5–20 所学校，但按正式架构实现：

```text
L0：继续用现有 API/MCP
L1：OpenSearch + Redis + catalog parser
L2：WeKnora
Router：Python FastAPI
Gateway：TypeScript NestJS，可选
Storage：MinIO
Observability：Langfuse
```

MIT 样例适合作为第一所学校，因为它已经包含学校树、专业、项目、URL、高频事实和 WeKnora metadata 模板。

---

## 13. 参考依据

1. OpenSearch 官方文档：Hybrid search 结合 keyword search 和 semantic search，并通过 search pipeline 归一化和合并分数。  
2. WeKnora GitHub：WeKnora 定位为面向 RAG、Agent、Auto-Wiki 的企业级知识框架，并支持 knowledge base 检索和文档理解。  
3. RedisVL 文档：SemanticCache 使用 Redis 缓存和 vector search 复用相似问题答案。  
4. MCP 官方规范：MCP tools 允许服务端暴露可由模型调用的数据库查询、API 调用和计算能力。
