# 多院校 L1 + WeKnora 人工盲测问题卷 v1

## 使用规则

1. 本文件只给测试人员看；测试结束后再打开评审答案。
2. 单轮题每题使用新会话。多轮题必须在同一会话连续提问。
3. Agent 必须调用 MCP 工具 `retrieve_university_knowledge`，不得靠模型常识回答。
4. 记录工具原始返回，不只记录 Agent 整理后的自然语言。
5. HTTP 基线测试中，单院校题必须显式传 `university_id`；MCP 测试中检查 Agent 是否正确传入该字段。
6. L2 题只有在对应 `source_id` 的 `weknora_import_status=success` 后才进入正式验收。

## A. 单院校向下检索

| ID | 用户问题 | HTTP 测试范围 |
|---|---|---|
| D01 | MIT 有 Economics 本科专业吗？ | `university_id=mit` |
| D02 | MIT Course 6-4 是什么专业？ | `university_id=mit` |
| D03 | Caltech 有 Computer Science 本科专业吗？ | `university_id=caltech` |
| D04 | Duke 有 Computer Science 本科专业吗？ | `university_id=duke` |
| D05 | MIT 本科 2026-2027 学费是多少？ | `university_id=mit` |
| D06 | MIT EECS PhD 的 TOEFL 和 IELTS 最低要求分别是多少？ | `university_id=mit` |

## B. 专业向上与范围检索

| ID | 用户问题 | 检索方向 |
|---|---|---|
| U01 | 计算机专业的院校有哪些？ | `upward` |
| U02 | 物理专业的院校有哪些？ | `upward` |
| U03 | 医学专业的院校有哪些？ | `upward` |
| R01 | 加州已入库院校有哪些？ | `range`，US + California |
| R02 | 北卡罗来纳州已入库院校有哪些？ | `range`，US + North Carolina |
| R03 | 中国已入库院校有哪些？ | `range`，CN |

## C. 反问与不存在结果

| ID | 用户问题 |
|---|---|
| X01 | EECS PhD 的 TOEFL 要求是多少？ |
| X02 | Unknown University 的 Economics 本科专业有哪些？ |
| X03 | 哪些院校有这个专业？ |

## D. L2 页面证据检索

| ID | 用户问题 | 当前性质 |
|---|---|---|
| E01 | MIT EECS PhD 申请需要提交哪些材料？ | 已验证通过的 L2 基线 |
| E02 | MIT CS master 要求是什么？MIT 是否提供独立的 terminal CS master？ | MIT EECS 证据挑战题 |
| E03 | Caltech Computer Science PhD 申请要求有哪些？ | 已知失败诊断题，修复后转正式验收 |
| E04 | Duke Computer Science MS 申请要求有哪些？ | 已知失败诊断题，修复后转正式验收 |

## E. 多轮范围保持

### M01：跨学校切换

1. MIT Course 6-4 是什么专业？
2. 换成 Duke，它有哪些 Computer Science 本科专业？

### M02：向上结果继续缩小范围

1. 计算机专业的院校有哪些？
2. 只看加州。

### M03：L2 项目范围保持

1. MIT EECS PhD 申请需要提交哪些材料？
2. 那 TOEFL 最低要求是多少？

## F. 增量入库生命周期

这些不是自然语言问答，而是必须人工执行的工程验收项。

| ID | 操作 |
|---|---|
| I01 | 重复上传完全相同的院校完整 MD，确认返回 `operation=unchanged`，不创建新版本和新 WeKnora job。 |
| I02 | 修改同一院校完整 MD 后上传，确认生成新 current 版本、复用原 KB，且只为新增/变化 URL 创建 job。 |
| I03 | 上传新院校完整 MD，确认自动创建并绑定新 KB；再用显式 KB 参数和强制新 KB 参数分别验证目标选择。 |

## 记录模板

```text
case_id:
test_layer: HTTP | MCP+Agent | ingestion
question_or_operation:
request_scope:
answer:
trace_id:
mode:
matched_university_ids:
matched_entry_or_fact_ids:
source_urls:
evidence_ids:
warnings:
missing_slots:
total_ms:
l1_ms:
weknora_ms:
pass_or_fail:
failure_owner: data | parser | L1 | routing | WeKnora | evidence | MCP | Agent
review_notes:
```
