# 大学数据平台 Agent 检索建设方案

> ⚠️ **HISTORICAL / SUPERSEDED（2026-07-15）**：本文档描述的 MVP/L0/L1/L2 Agent 平台建设方向已**不再是 active baseline**。当前实现基线已切换为聚焦的 **L1 + WeKnora 检索子系统**（先 MIT 验证，再增量验证若干所大学），见 `docs/architecture/00-overview.md` 与计划 `docs/plans/2026-07-15-l1-weknora-retrieval-correction.md`。本文档仅作历史设计参考保留。

> 版本：v3.0  
> 目标：明确需要准备什么环境、放什么数据、用什么技术、每一步怎么检索、如何建设 MVP。

---

## 1. 建设目标

建设一个支持两种产品体验的 Agent 数据能力：

```text
快速问答：3 秒内返回目录、专业、URL、高频事实
深度问答：允许慢一些，但必须准确、可追溯、可反问
```

最终能力：

```text
非深度问题 → L0 + L1 快速检索
复杂问题 → L0 + L1 定位范围 → L2 WeKnora 深度检索
报告问题 → Workflow 编排 L0 + L1 + L2
```

---

## 2. 环境准备

### 2.1 开发环境

推荐用 Docker Compose 搭 MVP 环境。

| 服务 | 推荐版本/技术 | 用途 |
|---|---|---|
| Fast Router | Python 3.11 + FastAPI | 轻路由、检索编排 |
| Tool Gateway | Node.js 20 + TypeScript + NestJS | MCP tool、对外 API、鉴权 |
| OpenSearch | OpenSearch 2.x/3.x | L1 catalog_entries、url_manifest、quick_facts 检索 |
| Redis | Redis 7.x + Redis Stack 可选 | catalog cache、query result cache、semantic cache |
| WeKnora | Docker 部署 | L2 RAG、Wiki、deep evidence search |
| Object Storage | MinIO | 原始 HTML、PDF、md、jsonl、快照 |
| L0 API | 现有服务 | 已有结构化数据能力 |
| Observability | Langfuse | trace、成本、延迟、检索日志 |
| Embedding 服务 | bge-m3 / OpenAI embedding / 内部模型 | L1 semantic search、L2 embedding |
| Reranker | bge-reranker / Jina / Cohere | L2 证据重排，可后置 |

### 2.2 目录结构

```text
university-agent-platform/
├── apps/
│   ├── fast-router/              # Python FastAPI
│   ├── tool-gateway/             # TypeScript NestJS / MCP
│   └── admin-console/            # 可选，后台管理
├── pipelines/
│   ├── catalog-parser/           # md → entries/url/facts
│   ├── opensearch-indexer/       # 写入 OpenSearch
│   ├── weknora-importer/         # URL 正文导入 WeKnora
│   └── cache-builder/            # Redis cache 生成
├── data/
│   ├── raw-md/                   # 院校 md
│   ├── normalized/               # catalog.json / jsonl
│   ├── snapshots/                # HTML/PDF 快照
│   └── eval/                     # 测试问题集
├── infra/
│   ├── docker-compose.yml
│   ├── opensearch/
│   ├── redis/
│   └── minio/
└── docs/
```

---

## 3. 数据准备

### 3.1 L0 数据

已经存在，保持现状。

必须确认 L0 API 至少能返回：

```text
university_id
university_name
aliases
country
campus
school
department
degree_level
program
```

需要新增或确认的 L0 tool：

```text
resolve_university(text)
get_university_tree(university_id)
search_l0_programs(university_id, filters)
```

### 3.2 L1 输入数据

输入是一所学校一个 md。

md 中至少需要：

```text
学校名称
学院/系层级
学位级别
专业/项目名称
URL
可选：deadline、申请费、GRE/GMAT、IELTS/TOEFL、tuition、funding
```

MIT 样例已经具备这些结构，可以作为 parser 第一版模板。

### 3.3 L1 输出数据

parser 输出三类 JSONL。

#### catalog_entries.jsonl

用于目录检索。

```json
{"entry_id":"mit_ug_6_4_sb","university_id":"mit","school":"School of Engineering","department":"Electrical Engineering and Computer Science","level":"undergraduate","degree_level":"SB","course_code":"6-4","program_name":"Artificial Intelligence and Decision Making","source_url":"https://catalog.mit.edu/degree-charts/artifical-intelligence-decision-making-course-6-4/","topics":["catalog","curriculum"],"search_text":"MIT AI Course 6-4 undergraduate EECS artificial intelligence computer science"}
```

#### url_manifest.jsonl

用于 L1 到 L2 路由。

```json
{"url_id":"mit_eecs_phd_oge","university_id":"mit","entry_id":"mit_grad_eecs_phd","source_url":"https://oge.mit.edu/programs/electrical-engineering-and-computer-science/","topics":["admission_requirements","english_requirement","funding"],"weknora_knowledge_id":"wk_xxx","content_hash":"sha256_xxx"}
```

#### quick_facts.jsonl

用于高频事实快速回答。

```json
{"fact_id":"mit_eecs_phd_deadline","university_id":"mit","entry_id":"mit_grad_eecs_phd","fact_type":"deadline","value":"December 1 at 11:59 PM Eastern Time","source_url":"https://oge.mit.edu/programs/electrical-engineering-and-computer-science/","capture_date":"2026-07-04"}
```

### 3.4 L2 输入数据

L2 不直接吃整校目录作为唯一来源。L2 主要吃：

```text
URL 正文
PDF 正文
课程页面
申请要求页面
费用页面
政策页面
FAQ 页面
normalized markdown
```

WeKnora 文档 metadata 必须包含：

```text
university_id
entry_id
source_url
topic
level
degree_level
capture_date
content_hash
version
```

---

## 4. OpenSearch 建设

### 4.1 Index 列表

| Index | 数据来源 | 用途 |
|---|---|---|
| l1_catalog_entries_current | catalog_entries.jsonl | 专业、项目、学院、方向快速检索 |
| l1_url_manifest_current | url_manifest.jsonl | 找 L2 URL / knowledge_id |
| l1_quick_facts_current | quick_facts.jsonl | deadline、fee、test、tuition 等快速事实 |

### 4.2 catalog 检索模板

适用问题：

```text
MIT 有哪些 AI 相关本科专业？
UCL 有哪些 Data Science 硕士？
某学院有哪些项目？
```

检索步骤：

```text
1. L0 resolve_university 得到 university_id
2. 从 query 中轻量识别 level / degree_level
3. OpenSearch filter university_id + level
4. keyword BM25 搜 program_name / school / department / search_text
5. semantic vector 搜 search_text embedding
6. hybrid 合并分数
7. 按 degree_level、exact match、source_url 存在性重排
```

简化 DSL 示例：

```json
{
  "query": {
    "bool": {
      "filter": [
        { "term": { "university_id": "mit" }},
        { "term": { "level": "undergraduate" }}
      ],
      "should": [
        { "match": { "program_name": { "query": "AI computer science", "boost": 3 }}},
        { "match": { "search_text": { "query": "AI computer science", "boost": 1 }}},
        { "term": { "course_code": { "value": "6-4", "boost": 5 }}}
      ]
    }
  },
  "size": 20
}
```

### 4.3 fact 检索模板

适用问题：

```text
MIT EECS PhD 雅思多少？
MIT MBAn 截止日是什么？
某专业申请费多少？
```

检索步骤：

```text
1. Fast Router 识别 route=fact，fact_type=english_requirement/deadline/application_fee
2. L0 解析 university_id
3. L1 catalog_entries 找候选 entry
4. quick_facts filter university_id + fact_type
5. 用 entry_id 或 program_name 过滤/排序
6. 命中且有 source_url：直接答
7. 缺失：转 deep_search
```

### 4.4 URL scope 检索模板

适用问题：

```text
课程怎么设置？
是否接受非相关背景？
申请要求有什么特殊点？
```

检索步骤：

```text
1. L0 解析学校
2. L1 catalog_entries 找候选专业/项目
3. L1 url_manifest 根据 entry_id + topic 找 source_url / knowledge_id
4. 把 knowledge_id / source_url / topic 传给 WeKnora
```

---

## 5. Redis 建设

### 5.1 Key 设计

```text
university_alias:{normalized_text} → university_id
catalog_tree:{university_id}:{version} → 整校目录树
catalog_search_result:{query_hash}:{scope_hash}:{version} → 目录检索结果
url_scope:{entry_id}:{topic}:{version} → URL / knowledge_id 列表
quick_fact:{entry_id}:{fact_type}:{version} → 高频事实
fast_answer:{query_hash}:{scope_hash}:{version}:{locale} → 低风险快速答案
```

### 5.2 缓存策略

| 数据 | 是否缓存 | 失效方式 |
|---|---|---|
| 学校别名 | 是 | L0 alias 更新 |
| 整校目录树 | 是 | catalog version 更新 |
| catalog 检索结果 | 是 | OpenSearch index version 更新 |
| quick facts | 是 | fact source_hash / version 更新 |
| L2 深度答案 | 谨慎 | 不建议长期缓存最终答案，只缓存 evidence scope |

### 5.3 Semantic Cache 使用边界

可以缓存：

```text
有哪些学院
有哪些专业
某方向有哪些项目
某专业官方 URL
```

谨慎缓存：

```text
deadline
学费
申请要求
政策解释
```

---

## 6. WeKnora 建设

### 6.1 知识库组织

建议按学校或国家拆知识库，MVP 先按学校：

```text
knowledge_base: mit-kb-v2
  doc: mit-ug-admissions
  doc: mit-grad-eecs
  doc: mit-sloan-mban
  doc: mit-costs-aid
```

每个文档必须带 metadata：

```yaml
university_id: mit
entry_id: mit_grad_eecs_phd
source_url: https://oge.mit.edu/programs/electrical-engineering-and-computer-science/
topic: admission_requirements
level: graduate
degree_level: PhD
capture_date: 2026-07-04
content_hash: sha256_xxx
version: v2.0
```

### 6.2 L2 检索方式

不要全局检索。必须先通过 L1 限定范围。

```text
输入：question + university_id + entry_id/topic
L1：找到 source_url / knowledge_id
WeKnora：限定 knowledge_ids / tag_ids / knowledge_base_ids 检索
Reranker：重排证据
Evidence Gate：过滤不匹配证据
Answer Composer：生成带引用答案
```

### 6.3 Evidence Gate

必须检查：

```text
source_url 存在
capture_date 存在
content_hash 存在
university_id 匹配
topic 匹配
entry_id 或 program_name 匹配
如果证据冲突，显示冲突，不强答
```

---

## 7. Fast Router 建设

### 7.1 API 设计

```http
POST /fast-answer
Content-Type: application/json

{
  "query": "MIT 有哪些 AI 相关本科专业？",
  "locale": "zh-CN"
}
```

返回：

```json
{
  "mode": "fast",
  "route": "catalog",
  "answer": "MIT 本科阶段与 AI / CS 相关的专业包括...",
  "structured_data": {
    "university_id": "mit",
    "results": []
  },
  "next_actions": [
    { "type": "deep_search", "label": "查看课程结构", "entry_id": "mit_ug_6_4_sb", "topic": "curriculum" }
  ]
}
```

### 7.2 路由策略

| 判断 | route | 下一步 |
|---|---|---|
| 有哪些、专业、项目、学院、方向 | catalog | L0 + L1 catalog search |
| deadline、IELTS、TOEFL、GRE、GMAT、学费、申请费 | fact | quick_facts，缺失再 L2 |
| 是否接受、适合、背景、课程偏向、政策解释 | deep | L1 找 URL，再 L2 |
| 报告、对比、推荐、规划 | report | workflow |
| 学校/项目/学位不明确 | clarification | 反问 |

### 7.3 什么时候反问

必须反问：

```text
学校不明确：Manchester 是 University of Manchester 还是 Manchester Metropolitan？
项目不明确：MIT CS master 不对应唯一项目。
学位不明确：本科还是研究生？
年份敏感：问 deadline/tuition 但没有申请季或数据版本不清。
证据不足：L2 找不到 official source。
```

---

## 8. MCP / Tool Gateway 建设

### 8.1 对 Agent 暴露的工具

不要暴露太多底层工具。先提供三个高层 tool：

```text
fast_university_answer
  用于 catalog/fact 快速问答，也能返回 deep_required

deep_university_search
  用于限定范围的 L2 证据检索

generate_admission_report
  用于报告 workflow
```

### 8.2 Tool Gateway 职责

```text
鉴权
限流
会话上下文
MCP tool schema
调用 Fast Router
记录 trace_id
返回结构化结果给 Agent
```

---

## 9. Workflow 报告建设

报告不是一次 RAG。

流程：

```text
1. 解析学生背景
2. L1 搜候选项目
3. quick_facts 查 deadline、fee、test、funding
4. L2 查课程、要求、背景适配、政策解释
5. Evidence Gate 校验
6. 生成报告：项目列表、匹配度、风险、费用、时间线、证据和缺失项
```

报告输出必须包含：

```text
结论
依据
引用
假设
缺失数据
下一步建议
```

---

## 10. MVP 实施步骤

### 10.1 第 1 周：基础环境

交付：

```text
Docker Compose: OpenSearch + Redis + MinIO + WeKnora + Langfuse
Fast Router 项目骨架
Tool Gateway 项目骨架
L0 API 连通测试
```

### 10.2 第 2 周：L1 parser

交付：

```text
MIT md → catalog_entries.jsonl
MIT md → url_manifest.jsonl
MIT md → quick_facts.jsonl
字段校验脚本
版本号和 content_hash
```

### 10.3 第 3 周：OpenSearch / Redis

交付：

```text
OpenSearch index mapping
catalog search API
fact lookup API
url scope API
Redis cache builder
```

### 10.4 第 4 周：Fast Router

交付：

```text
route classifier
L0 resolve_university 调用
L1 catalog/fact/url 调用
fast / clarification / deep_required 输出
```

### 10.5 第 5 周：WeKnora 深度检索

交付：

```text
URL 正文导入 WeKnora
metadata 写入
限定 knowledge_id / URL / topic 检索
Evidence Gate
```

### 10.6 第 6 周：测试和评估

交付：

```text
200 条测试问题
intent accuracy
catalog recall@10
fast path p95 latency
fact accuracy
L2 citation coverage
错误分析报告
```

---

## 11. 验收标准

### 11.1 快速问答

```text
目录类问题 Fast Path 覆盖率 ≥ 85%
Fast Path p95 < 3 秒
学校识别准确率 ≥ 95%
目录 recall@10 ≥ 90%
无 L2 调用比例 ≥ 80%（目录类）
```

### 11.2 高频事实

```text
quick_facts 命中时答案必须带 source_url / capture_date
事实缺失时必须转 L2 或反问
不得无证据强答
```

### 11.3 深度问答

```text
关键结论必须有证据
source_url、capture_date、topic 必须可追溯
证据冲突时必须展示冲突
低置信时允许反问
```

---

## 12. 团队分工建议

| 角色 | 工作内容 |
|---|---|
| 后端工程 | Fast Router、Tool Gateway、L0 API 接入 |
| 数据工程 | md parser、OpenSearch indexing、Redis cache、MinIO 快照 |
| RAG 工程 | WeKnora 导入、metadata、deep_search、Evidence Gate |
| 产品/内容 | 定义测试问题、审核低置信样例、验收答案质量 |
| 运维/SRE | Docker、部署、日志、监控、权限、安全 |

---

## 13. 技术取舍

### 13.1 为什么 Fast Router 用 Python

Python 更适合：

```text
NLP 规则和模型实验
embedding / rerank 调用
OpenSearch / Redis / WeKnora 编排
评估脚本
快速迭代
```

### 13.2 为什么 Tool Gateway 可以用 TypeScript

TypeScript 更适合：

```text
MCP schema
前端/Agent 网关集成
鉴权和会话
Node.js 生态
```

### 13.3 为什么 L1 用 OpenSearch

L1 要处理自然语言目录搜索，不只是 ID 查询。OpenSearch 适合：

```text
filter + BM25
course_code exact
aliases keyword
semantic vector search
hybrid scoring
faceting / sorting
```

### 13.4 为什么不用 L2 做所有事

L2 更慢，且全局 RAG 容易召回错误学校、错误专业、错误年份。目录和高频事实应走 L0 + L1。

---

## 14. 第一版测试问题集建议

目录类：

```text
MIT 有哪些 AI 相关本科专业？
MIT EECS 有哪些本科专业？
MIT Sloan 有哪些研究生项目？
MIT 有哪些 Data / Computing 方向项目？
```

事实类：

```text
MIT EECS PhD 雅思要求是多少？
MIT Sloan MBAn 截止日是什么？
MIT CSE PhD GRE 是否必须？
MIT 本科 EA 截止日是什么？
```

深度类：

```text
MIT EECS PhD 是否接受非计算机背景？
MIT Sloan MBAn 适合什么背景？
MIT 本科国际生是否 need-blind？
MIT 课程设置偏理论还是工程？
```

歧义类：

```text
MIT CS master 要求是什么？
MIT 学费多少？
MIT 数据科学怎么申请？
Manchester CS 有哪些？
```

---

## 15. 最终落地版本

建议第一个正式 MVP 就按长期架构的小规模版本建设：

```text
L0：现有结构化 API/MCP
L1：OpenSearch + Redis + catalog parser
L2：WeKnora
Router：Python FastAPI
Gateway：TypeScript NestJS，可选
Storage：MinIO
Trace：Langfuse
```

不要先做临时架构，也不要第一阶段做复杂知识图谱或人工映射表。
