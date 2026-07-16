# MIT 人工盲测问题卷 v1

> 新的分层测试说明、L1/WeKnora 路由判断和“正确答不出来”场景见
> `qa/manual/md-first-l1-weknora-qa-guide.md`。本问题卷继续作为 30 题综合盲测集。

## 测试方法

1. 确认服务健康：

   ```bash
   curl http://127.0.0.1:8000/health
   curl http://127.0.0.1:8765/health
   ```

2. Claude/Codex MCP 地址使用 `http://127.0.0.1:8765/mcp`，工具名必须是
   `retrieve_university_knowledge`。
3. 单轮题每题使用一个新会话，避免上一题上下文影响结果。
4. 多轮题按题目顺序在同一会话连续追问。
5. 测试时只看本问题卷。全部回答完成后，再打开
   `qa/manual/mit-qa-review-key-v1.md` 评分。
6. 记录回答、引用 URL、工具返回的 `trace_id`、`mode`、`timings.total_ms`。

## A. L1 目录与事实

| ID | 用户问题 |
|---|---|
| Q01 | MIT 有 Economics 本科专业吗？ |
| Q02 | MIT Course 6-4 是什么专业？ |
| Q03 | MIT Course 6-9 学什么？ |
| Q04 | MIT 有没有把计算机、经济学和数据科学结合起来的本科专业？ |
| Q05 | MIT 有 Astronomy minor 吗？ |
| Q06 | MIT Course 16 对应什么本科专业？ |
| Q07 | MIT EECS PhD 的 TOEFL 和 IELTS 最低要求分别是多少？ |
| Q08 | MIT Biology PhD 的英语成绩要求是什么？ |
| Q09 | MIT Economics graduate application deadline 是什么时候？ |
| Q10 | MIT Microbiology 的申请费是多少？ |
| Q11 | MIT 本科 2026-2027 学费是多少？ |
| Q12 | MIT 本科 Early Action 和 Regular Action 的截止日期分别是什么？ |
| Q13 | MIT EECS PhD 一般如何资助？ |
| Q14 | MIT Economics PhD 要求 GRE 或 GMAT 吗？ |

## B. L2 证据检索

| ID | 用户问题 |
|---|---|
| Q15 | MIT EECS PhD 申请需要提交哪些材料？ |
| Q16 | MIT Sloan MBA 申请要求有哪些？ |
| Q17 | 我本科不是计算机专业，能申请 MIT EECS PhD 吗？ |
| Q18 | 非生物学本科背景能申请 MIT Biology PhD 吗？ |
| Q19 | MIT Microbiology PhD 的完整申请要求是什么？ |
| Q20 | MIT CS master 要求是什么？MIT 是否提供独立的 terminal CS master？ |

## C. 反问、缺失与错误范围

| ID | 用户问题 |
|---|---|
| Q21 | MIT 研究生申请 deadline 是什么时候？ |
| Q22 | MIT 的入学申请有什么要求？ |
| Q23 | 我国内大专毕业，能不能申请 MIT 本科？本科要求是什么？ |
| Q24 | EECS PhD TOEFL 要求是多少？ |
| Q25 | Unknown University 的 Economics 本科专业有哪些？ |
| Q26 | MIT 有 Quantum Basket Weaving 本科专业吗？ |

## D. 多轮上下文

### Q27：保持 EECS 项目范围

1. MIT EECS PhD 的 TOEFL 最低要求是多少？
2. 那申请截止日期呢？
3. 资助怎么样？

### Q28：保持 Biology 项目范围

1. MIT Biology PhD 的英语要求是什么？
2. 那截止日期呢？
3. GRE 要求呢？

### Q29：本科到研究生范围切换

1. MIT 有 Economics 本科专业吗？
2. 那 Economics 研究生申请截止日期是什么时候？

### Q30：切换学校后禁止默认回 MIT

1. MIT Course 6-4 是什么？
2. 换成 Unknown University，它有同名专业吗？

## 记录模板

```text
case_id:
answer:
trace_id:
mode:
source_urls:
total_ms:
review_notes:
```
