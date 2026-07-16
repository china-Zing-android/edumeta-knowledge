# WeKnora Import Runbook

Fast Router 内置 PG job worker。上传成功后，`weknora_import_jobs` 使用 `FOR UPDATE SKIP LOCKED` 领取任务，URL import 不阻塞上传请求。

必要配置：`WEKNORA_BASE_URL`、`WEKNORA_API_KEY`、`WEKNORA_KB_TEMPLATE_ID`。`WEKNORA_KNOWLEDGE_BASE_ID` 仅作旧数据 fallback。每校创建/复用独立 KB 和 `university:{university_id}` tag；每个 URL job 使用自身 `knowledge_base_id`。

检索使用 `knowledge_ids` 做服务端精确 scope。部署实测表明同时发送 `knowledge_ids` 与 `tag_ids` 会在当前远端版本返回空结果，因此已有 knowledge ID 时只发送 knowledge scope，tag 作为导入治理与无文档 ID 时的后备能力。

状态检查：

```sql
select status, count(*) from weknora_import_jobs group by status;
select source_url, status, knowledge_id, failure_reason
from weknora_import_jobs order by updated_at desc limit 20;
```

`success` 会回写 PG source 状态及 `l1_sources_current`。瞬时失败最多重试三次；终态失败必须保留 `failure_reason`。生产路径没有 mock evidence。

版本切换时，旧版本仍为 `queued/running` 的 job 会标记为 `superseded`；worker 只领取 current school version 的任务，避免历史增量版本继续轮询。
