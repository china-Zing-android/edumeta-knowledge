# L1 MD + WeKnora 真人 QA 操作手册

基线日期：2026-07-16

本手册用于验证两层能力：

```text
L1 = Markdown 解析后的目录、事实和 entity context，目标是快速、确定、weknora_ms=0
L2 = WeKnora 中 URL 页面正文，只有用户明确追问细节且 scope 已确定时调用
```

## 1. 测试前准备

确认服务健康：

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8765/health
```

预期：

- Fast Router：`status=ok`、`version_cache_size=5`。配置 L2 时 WeKnora `configured=true`；纯 L1 环境允许为 `false`。
- Tool Gateway：`status=ok`。

Claude/Codex MCP 配置保持不变：

```json
{
  "mcpServers": {
    "edumeta-local": {
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

工具名必须只有：

```text
retrieve_university_knowledge
```

Fast Router 和 MCP 服务已经更新，但 Claude/Codex 通常在会话启动时缓存 MCP tool schema 和 description。更新服务后应新建会话或重启客户端，使新版 Agent 呈现规范生效；MCP 地址不需要修改。

## 2. 推荐测试方法

分两轮测试同一问题：

1. **盲测回答**：像普通学生一样直接提问，不告诉 Agent 应走 L1 或 WeKnora。
2. **工程核查**：查看工具原始返回，记录 `trace_id/mode/scope/context/evidence/warnings/timings`。

每题记录：

```text
case_id:
question:
answer:
trace_id:
mode:
scope.stage:
primary_entities:
evidence_source_urls:
weknora_ms:
warnings:
pass/fail:
notes:
```

## 3. 如何判断走了哪条链路

| 场景 | 预期 mode | context | evidence | weknora_ms |
|---|---|---|---|---|
| L1 MD 目录/院校/专业发现 | `l1` | 有，`origin=md_projection` | 空 | `0` |
| L1 quick fact 命中 | `l1` | 有 | 空 | `0` |
| 明确细节且 L1 不足 | `l1_l2` | 有 | 有真实 chunk | `> 0` |
| 学校或项目范围模糊 | `clarification` | 空或仅大学 context | 空 | `0` |
| 学校/专业未入库或不存在 | `not_found` | 空或有限 | 空 | `0` |
| scope 正确但页面没有证据 | `not_found` 或 `l1_l2` 降级 | 有 | 空 | 可为 `> 0` | 

`context` 不是引用证据。只有 `evidence` 中带 `source_url/knowledge_id/document_id/chunk_id/chunk_text` 的内容才是 WeKnora 证据。

## 4. L1 Markdown 内容测试

这类问题只测试 MD 解析、目录检索和 entity context，**禁止调用 WeKnora**。

### L1-01：院校概览

```text
MIT
```

预期：

- `mode=l1`、`stage=discovery`、`weknora_ms=0`。
- 主实体是 Massachusetts Institute of Technology。
- 可列少量代表学院/专业和可继续探索主题，不能倾倒完整目录。
- 不生成“世界第一”“最强”等未提供的评价。

### L1-02：本科专业存在与上下文

```text
MIT 有 Economics 本科专业吗？这个专业怎么样？
```

预期：

- 主实体：`14-1 Economics`，SB，本科，Economics department。
- 相关实体包括 `14-2 Mathematical Economics` 和 `6-14 Computer Science, Economics, and Data Science`。
- 可继续主题优先包含 curriculum、application requirements 等。
- `evidence=[]`、`weknora_ms=0`。
- 不得编造课程优势、就业结果或“更偏数学”等 MD 未明确表达的结论。

### L1-03：多专业关系

```text
MIT Economics、Mathematical Economics 和 6-14 有什么关系？
```

预期：三个可读主实体；关系仅基于同校、同院系、同层级、交叉学科等确定性字段；primary 和 related 不重复；不调用 WeKnora。

### L1-04：Course 编号

```text
MIT Course 6-4 是什么专业？
```

预期：`6-4 Artificial Intelligence and Decision Making`；不能只返回裸 `6-4`。

### L1-05：向上检索

```text
计算机专业的院校有哪些？
```

预期：`mode=upward`，只返回当前已入库的 MIT、Stanford、Harvard、Princeton、Berkeley 中实际匹配者；不是全美国院校清单，也不是排名；`weknora_ms=0`。

## 5. L1 Quick Facts 测试

这些事实来自 MD 中已经拆出的 quick facts，不需要 WeKnora。

### FACT-01：学费

```text
MIT 本科 2026-2027 学费是多少？
```

预期原始值 `$66,720`；必须保留数据周期、source 和可能的 review warning；`mode=l1`、`stage=fact`、`weknora_ms=0`。

### FACT-02：英语成绩

```text
MIT EECS PhD 的 TOEFL 和 IELTS 最低要求分别是多少？
```

预期 EECS source；TOEFL 100、IELTS 7；不得混入其他项目标准；不调用 WeKnora。

### FACT-03：项目截止日期

```text
MIT Economics graduate application deadline 是什么时候？
```

预期 Economics graduate source 和 `December 15 at 11:59 PM Eastern Time`；`matches` 不得混入 DEDP/MASc deadline；不调用 WeKnora。DEDP 只允许出现在 `context.related_entities`，且 Agent 不应把它包装成本题答案。

### FACT-04：资助

```text
MIT EECS PhD 一般如何资助？
```

预期返回 MD fact 原始值和 review 状态。若为 `review_required`，Agent 应加提示，不包装成无条件保证；不自动调用 WeKnora 核验。

## 6. WeKnora 页面正文测试

只有用户明确要材料、课程细节、资格政策、完整要求等内容时才走 WeKnora。必须先解析学校和项目 scope。

### WK-01：申请材料

```text
MIT EECS PhD 申请需要提交哪些材料？
```

预期：

- `mode=l1_l2`、`stage=detail`、`weknora_ms>0`。
- evidence 只来自 EECS graduate source。
- 至少覆盖 online application、两篇 essay、三封推荐信、transcripts、英语成绩。
- 不得引用本科 Course 6-3 degree chart 作为主要证据。

再执行一条抗改写回归：

```text
MIT EECS PhD application requirements required materials transcripts letters CV GRE TOEFL IELTS
```

即使问题含 TOEFL/IELTS/GRE，仍必须是 `stage=detail`，不得只返回英语成绩和 GRE policy。无 WeKnora 配置时应返回 `mode=l1_l2`、`warnings=[weknora_unavailable]`、`matches=[]`。

### WK-02：专业课程正文

先问：

```text
MIT 有 Economics 本科专业吗？
```

在同一 Agent 会话追问：

```text
那课程设置呢？
```

预期第二轮 Agent 回传 `context.entry_id=ent_mit_undergraduate_sb_14_1_economics`；Router 只搜索 Economics 14-1 degree-chart source；`mode=l1_l2`。

如果手工调用 HTTP，可直接发送：

```json
{
  "query": "那课程设置呢？",
  "university_id": "mit",
  "context": {
    "entry_id": "ent_mit_undergraduate_sb_14_1_economics",
    "level": "undergraduate"
  }
}
```

### WK-03：terminal master 政策

```text
MIT CS master 要求是什么？MIT 是否提供独立的 terminal CS master？
```

预期使用 EECS graduate evidence，说明 EECS 不提供独立 terminal master's；MEng 仅面向 MIT 本科生；PhD 路径可先取得 SM。不得主要召回本科 degree chart。

### WK-04：背景资格边界

```text
我本科不是计算机专业，能申请 MIT EECS PhD 吗？
```

预期只使用 EECS evidence。若页面没有给出绝对资格结论，应说明证据边界，不能保证可以申请或可以录取。

### WK-05：完整项目要求

```text
MIT Microbiology PhD 的完整申请要求是什么？
```

预期只使用 Microbiology source，不能混入 Biology、EECS 或本科页面。

## 7. 正确的“答不出来”测试

以下问题不是要求系统硬答，而是验证它会正确拒绝、反问或声明证据不足。

### NO-01：缺具体研究生项目

```text
MIT 研究生申请 deadline 是什么时候？
```

预期：`clarification`，追问具体项目；不能选择一个全校 deadline；不调用 WeKnora。

### NO-02：缺学校

```text
EECS PhD 申请材料有哪些？
```

预期：`clarification`，`missing_slots` 包含 `university_id`；不能默认 MIT。

### NO-03：未入库学校

```text
Unknown University 的 Economics 本科专业有哪些？
```

预期：`not_found`；不能回退到 MIT 或其他学校。

### NO-04：不存在的专业

```text
MIT 有 Quantum Basket Weaving 本科专业吗？
```

预期：`not_found`；不能拿相似专业填充结果。

### NO-05：主观评价但来源不足

```text
MIT Economics 是不是最好的经济学专业？它最大的优势是什么？
```

当前系统测不出排名和“最好”。MIT MD 也没有 14-1 的优势、就业、适合人群等定性内容。正确行为是说明当前可确认的目录结构和来源边界，不生成排名或主观优势。

### NO-06：录取概率

```text
我的 GPA 3.5，申请 MIT EECS PhD 的录取概率是多少？
```

当前系统没有录取概率模型，也不做个性化录取预测。不得给出百分比或保证。

### NO-07：未收录的职业结果

```text
MIT Economics 本科毕业生平均工资是多少？
```

当前 MD/WeKnora scope 没有该事实时，应返回证据不足，不得从常识或外部数据补值。

### NO-08：全美前五排名

```text
美国大学前五名有哪些？
```

排名能力已明确移出当前子模块。系统只能检索已入库学校和专业，不能把 OpenSearch score 当排名。

## 8. 当前确实测不出的内容范围

下列内容只有补充 MD 或 URL 数据后才能验收：

- 14-1 Economics 的详细课程说明、项目优势、就业去向、适合人群。
- 未导入 URL 页面中的校园文化、学生体验、实验室细节。
- 未入库院校的目录、事实和页面正文。
- 院校排名、专业排名、推荐顺序。
- 个人录取概率、录取保证、职业薪资预测。
- 超出 `capture_date/dataset_version` 的最新政策；系统必须按当前数据版本回答，不能自动假设仍然有效。

## 9. 通过标准

- L1 discovery/fact：`weknora_ms=0`，错误学校/项目/层级为 0。
- WeKnora：evidence source 与学校/项目 scope 完全一致，chunk 文本真实存在。
- clarification/not_found：不默认 MIT，不用相似结果填充。
- Agent 表达：先直接回答，再补 context、少量 related entities、available topics；不倾倒原始 JSON。
- Course 编号必须带可读名称。
- `review_required/conflict` 事实保留 warning。
- 没有证据时不强答。
