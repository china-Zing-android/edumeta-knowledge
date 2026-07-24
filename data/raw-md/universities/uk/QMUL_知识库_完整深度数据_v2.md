# Queen Mary University of London Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England (London))

---

## SECTION 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | P0 follow-up |
| 研究生授课型 (PGT) | P0 follow-up |
| 研究生博士 (PhD) | P0 follow-up |

### 0.2 学院 / 系层级结构 (Rule 2)

> ⚠ P0: Full hierarchy requires website extraction.

### 0.3 学历级别明细 (Rule 3)

> ⚠ P0: Full degree inventory requires course extraction.

### 0.4 分布矩阵 (Rule 4)

> ⚠ P0: Matrix requires full course extraction.

---

## SECTION 1 — Undergraduate education

**From v1.0**: BSc Computer Science. A-Level ABB, IB 32, IELTS 6.5.

> ⚠ P0: Full programme listing requires website extraction. v1.0 file contained only CS data.

---

## SECTION 2 — Graduate education

> ⚠ P0: Postgraduate programmes require separate extraction.

---

## SECTION 3 — Application requirements

> ⚠ P0: See v1.0 file for CS-specific requirements.

---

## SECTION 4 — Costs

| Fee status | Annual |
|-----------|--------|
| **Home (UK)** | £9,250 |
| **International** | P0 follow-up |

---

## SECTION 5 — Evidence chain

```yaml
E-U-001:
  field: institution.name
  value: "Queen Mary University of London"
  source_url: https://www.qmul.ac.uk
  source_snippet: "Queen Mary University of London"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

| Priority | Data item |
|----------|-----------|
| **P0** | Full UG course listing |
| **P0** | Full PG course listing |
| **P0** | Faculty/department hierarchy |
| **P0** | Degree type distribution |
| **P0** | International tuition fees |
| **P1** | Per-course entry requirements |
| **P1** | English language requirements |

---

## SECTION 7 — Cross-school comparison

| Dimension | Queen Mary University of London | Cardiff | Newcastle |
|-----------|-----------|---------|-----------|
| Total UG programmes | P0 follow-up | 237 | 147 |
| Russell Group | Yes | Yes | Yes |

---

> **Document version**: v2.0 (deep) | **Generated**: 2026-07-08
> **Granularity**: school → department → degree-level → program
> **Completeness**: Framework ✅ | UG programmes ⚠ P0 | PG programmes ⚠ P0
