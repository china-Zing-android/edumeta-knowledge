# QA/UAT 真实问答验收

## 定位

QA/UAT 是发布阻断闸门，不是上线后的主观体验反馈。它验证真实用户问题下的正确性、证据匹配、时效、反问、缺失处理和任务完成度。

## Persona

- 本科申请者。
- 研究生申请者。
- 家长/顾问。
- 内容审核员。
- Agent 工具使用方。

## 场景

- 目录检索。
- 高频事实。
- 深度证据。
- 模糊反问。
- 跨项目比较。
- 多轮追问。
- 证据缺失。
- 事实冲突。
- URL 更新回归。

## QA Case 字段

```text
qa_case_id
university_id
persona
question
conversation_context
expected_route
expected_behavior
must_include
must_not_include
required_source_url/source_id
risk_level
reviewer_owner
case_source
human_review_required
```

`case_source=generated_from_normalized_data` 的样本只能作为自动化执行基线；发布验收必须经过人工 reviewer 复核、补充真实用户问题和评分。

## 评分维度

```text
answer_correctness: 0-2
evidence_match: 0-2
freshness_version_correctness: 0-2
clarification_quality: 0-2
task_completion: 0-2
hallucination_flag: true/false
unsafe_or_overconfident_flag: true/false
```

人工 review gate 使用 `qa/human-reviews.jsonl`，由 `scripts/human_qa_review_gate.py` 校验。自动 QA pass 不能替代人工 review pass。

## 阻断项

- P0 事实错误。
- 引用不支持结论。
- 错学校/错项目/错学位层级证据进入答案。
- 问题模糊但系统不反问。
- 证据缺失时强答。
- MCP/HTTP/CLI 返回结构不一致。
- 低分或 flag=true 但没有失败归因。

## 人工 Review 发布阈值

```text
reviewed UAT base cases >= 200
reviewed conversation base cases >= 50
P0 answer_correctness/evidence_match/freshness_version_correctness = 2
hallucination_flag = false for P0/P1 sampled cases
evidence_match_rate >= 95%
clarification_quality_rate >= 90%
task_completion_rate >= 85%
all failed/partial reviews have failure_category
```

## 输出物

```text
qa/mit-gold-cases.jsonl
qa/mvp-uat-cases.jsonl
qa/mvp-uat-conversations.jsonl
qa/human-reviews.jsonl
qa/review-rubric.md
qa/qa-report-YYYY-MM-DD.md
qa/failure-analysis-YYYY-MM-DD.md
```
