# 数据架构

## 权威层与查询层

```text
Markdown upload
  -> PostgreSQL control plane
  -> OpenSearch L1 query indexes
  -> WeKnora scoped URL evidence
```

PostgreSQL 保存 `universities`、`school_versions`、`ingestion_runs`、`ingestion_records`、`catalog_entries`、`entity_contexts`、`catalog_entry_disciplines`、`source_registry`、`source_entry_links`、`fact_store`、`weknora_import_jobs`。OpenSearch 和 WeKnora 都可由该控制面重建，不承担版本权威。

`universities.weknora_knowledge_base_id` 保存院校当前完整 MD 的 KB 绑定；`ingestion_runs.weknora_kb_operation` 记录 `create/reuse/explicit`。`source_registry` 与 `weknora_import_jobs` 继续保存每个 URL 实际所在 KB，允许历史版本和旧 KB 保留。

稳定实体 ID 在不同版本复用，但权威表主键包含 `university_id + version_id + entity_id`，旧版本不会被新版本覆盖。`school_versions` 每校最多一个 `current` 指针。

## 全局索引

```text
l1_universities_current
l1_catalog_entries_current
l1_quick_facts_current
l1_sources_current
l1_entity_contexts_current
```

文档 ID 为 `university_id:dataset_version:entity_id`。单校发布先删除同校同版本的残留文档，再写入并核对数量，不重建其他学校。

`entity_contexts` 是版本化 MD 物化投影，不是第二套实体真源。它以现有 `university_id/entry_id/source_id` 组合院校或专业的结构化上下文、最多两个确定性相关实体和可继续探索主题；同校 MD 更新只重建该校受影响 context，context-only 变化不创建 WeKnora 重导 job。

## Source 与 Evidence

每个合法 canonical URL 在一个学校版本内只出现一次。`source_entry_links` 保存 source 与 catalog/fact 的关系；WeKnora 的 knowledge/document/chunk/tag 状态保存在 `source_registry` 与 `weknora_import_jobs`。

WeKnora evidence 必须包含真实 `chunk_text`，并映射回当前版本的 `source_id/source_url`。Fact Store 文本和 `entity_contexts` 均不得伪装成 WeKnora evidence。

`universities` 是已入库院校注册表；`catalog_entry_disciplines` 是受控学科分类关系。向上与范围检索只查询这两类 L1 current 数据，不调用 WeKnora，也不把 OpenSearch score 解释为院校排名。
