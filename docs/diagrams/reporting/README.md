# 汇报流程图

1. `01-overall-architecture-flow.svg/png`：整体架构、MD 与 WeKnora 数据来源边界。
2. `02-fast-router-principle.svg/png`：Fast Router 的方向判断、意图分层、OpenSearch 匹配和 Evidence Gate。
3. `03-data-storage-architecture.svg/png`：PostgreSQL 权威层、OpenSearch 查询投影、WeKnora 网页证据层。

## 建议讲解顺序

### 图 1：整体架构

1. 先看上半部分：上传 Markdown 后，Parser 一次提取目录、事实、上下文和 URL。
2. 青色链路全部来自 MD，是 1 秒内快速检索的基础；琥珀色链路来自 URL 页面正文，是 WeKnora 深度证据。
3. 在线查询默认先走 OpenSearch L1。只有用户明确问申请材料、课程细节、资格政策等内容，才按 L1 选定的 URL scope 调 WeKnora。
4. 最终响应中 `matches/context` 来自 MD，`evidence` 才是 WeKnora 网页证据。

### 图 2：Fast Router

1. 先解析学校和搜索方向，显式学校范围优先，未知学校不会默认成 MIT。
2. QueryPlan 的优先级是 `detail > fact > discovery`，避免申请材料问题被 TOEFL/GRE 等事实词截断。
3. OpenSearch 一次并行查目录、事实、来源和实体上下文；专业定位后，再按精确 `source_id` 收敛一次。
4. discovery 或事实命中直接返回 L1；scope 模糊先反问；明确细节才进入 Scoped WeKnora。

### 图 3：数据存储

1. PostgreSQL 保存权威版本、来源生命周期、事实状态和 WeKnora Job，是系统真源。
2. OpenSearch 是面向查询的 L1 投影，热路径不查询 PostgreSQL。
3. WeKnora 保存 URL 页面和 chunk，不保存目录主数据。
4. 三层通过 `entry_id/fact_id -> source_id -> knowledge_id/chunk_id` 串联；OpenSearch 和 WeKnora 都可以从 PostgreSQL 控制面重建。
