# 运行时调用链路

## 检索流（统一固定流，本地保守规划）

所有检索请求走同一条固定链路。`POST /v1/retrieve` 与 MCP `retrieve_university_knowledge` 完全一致。

```text
request (query / university_id / direction / filters / context / max_results)
  -> normalize request
  -> resolve direction
       range/upward -> OpenSearch current universities/catalog taxonomy -> grouped matches -> return
       downward     -> continue scoped university flow
  -> resolve local university/context（仅本地 alias index；未知 -> not_found）
  -> QueryPlan
       discovery -> MD context first，禁止 WeKnora
       fact      -> Fact Store first，命中即返回
       detail    -> 仅明确材料/课程细节/资格/文化等请求
  -> OpenSearch L1 _msearch
       (1) 精确 ID 与精确规范化 course_code
       (2) 目录 BM25（字段 boost + university/level/version 过滤）
       (3) 事实查找（fact type / review status / program / version 过滤）
       (4) source-scope（供 WeKnora 用）
       (5) entity context（院校/专业 MD 物化上下文）
  -> precision/fact gate
       - 精确标识符/course-code 命中压制弱匹配
       - min score 以下 omit，禁止用无关结果填 top_k
       - 冲突/未批准事实标记，不可提升为 confirmed
  -> L1/trigger gate
       discovery -> 返回 mode=l1 + context，weknora_ms=0
       fact hit  -> 返回 mode=l1 + raw fact + context，weknora_ms=0
       detail/fact miss + resolved entity/source scope
                  -> scoped WeKnora search（按 KB / knowledge_ids）
       ambiguous scope -> clarification，禁止 WeKnora
              -> evidence gate（真实 chunk + current source/version + scope 匹配）
              -> 返回 mode=l1_l2
  -> 每响应记录 timings{total_ms, l1_ms, weknora_ms}
```

返回契约字段：

```text
trace_id
mode          (l1 | l1_l2 | range | upward | clarification | not_found | error)
scope         {university_id, dataset_version, stage, requested_aspects, direction, discipline_id, filters}
matches       (结构化目录记录或原始事实值，含 match_reason / _score / source_id / source_url / dataset_version)
context       (MD 投影；primary/highlights/children/related/topics/presentation_hints/provenance，始终为对象)
evidence      (仅 L1+WeKnora 路径，含 evidence_id / source_id / knowledge_id / document_id / chunk_id / chunk_text / score / capture_date / dataset_version)
missing_slots
warnings      (如 evidence_timeout)
timings       {total_ms, l1_ms, weknora_ms}
```

规则：
- 服务不生成散文答案。
- Agent 按直接答案 -> context -> related_entities -> available_topics 呈现；裸 Course 编号必须补可读名称。
- `context != evidence`；`available_topics` 不触发数据检索。
- Router 无会话状态；Agent 将多轮 `entry_id/program_id/level` 回传到下一请求。
- `range/upward` 只查已入库 current L1 数据，不调用 WeKnora；`downward` 才解析具体大学 scope。
- `university_id` 缺失且问题是单校下钻时，仅通过本地大学 alias index 解析。
- 未知大学返回 `not_found`，**绝不默认 MIT**。
- 事实含 `review_status` / `conflict_status` / `capture_date` / source metadata；`review_required` 事实可返回但必须带 warning 且不可标 confirmed。
- WeKnora 超时返回 L1 结果并附 `warnings=["evidence_timeout"]`。
- 无运行时 LLM 调用、无 L0/country/ranking fallback、无请求时重试。

## 数据构建链路（ingestion）

```text
学校 MD (multipart 上传)
  -> POST /v1/university-ingestions -> 202 {run_id, university_id, operation, status:"accepted", input_hash}
  -> 先 upsert universities(status=pending)，再启动解析
  -> create ingestion_run + staging records
  -> validate schema 与交叉引用
  -> diff 当前 school version
  -> 事务写新版本（不改 current_version）
  -> 发布 OpenSearch L1（版本化文档 ID）
  -> 校验文档数与必需记录
  -> 单事务切换 school_versions.current_version
  -> 刷新 in-process version map
  -> resolve KB：新校 create；已有学校 reuse；显式 ID validate/rebind；force-new create/rebind
  -> 异步 WeKnora import（每 job 使用自身 knowledge_base_id；PG job queue，不阻塞上传）
  -> 保留旧版本用于回滚
```

规则：
- MD、parser contract 与请求元数据共同决定 input hash；三者均未变 → 标 `unchanged`。
- KB 目标也是 input identity 的一部分；切换 KB 会触发全量 URL 向新 KB 导入，不继承旧 KB 的成功状态。
- 同一 KB 内的完整快照更新继承未变 URL 的成功状态，并续接未完成 knowledge ID。
- 仅目录/事实变更 → 只发布受影响 L1 记录，不重导入未变更 URL。
- 新 URL → 创建 source + WeKnora job；canonical URL 或内容 hash 变 → supersede 旧 source + 替换 job。
- 移除 URL → 标记 inactive，不物理删除。
- 解析/引用校验失败 → 不发布该 school 任何部分，保留旧 current。
- 某校更新从不改写其他学校 current 版本。
- GET `/v1/university-ingestions/{run_id}` 返回 operation / stage status / counts / failures / OpenSearch 发布状态 / WeKnora job summary。

## Agent 入口

Agent 只通过 MCP `retrieve_university_knowledge`（经可选 TS Gateway 转发）或直接 HTTP `POST /v1/retrieve` 调用。两者输入输出完全一致；`trace_id` 可不同，但 `mode` / `scope` / `matches` / `evidence` / `timings` 语义一致。不存在 legacy `/mcp` 入口，不存在四入口一致性 gate。
