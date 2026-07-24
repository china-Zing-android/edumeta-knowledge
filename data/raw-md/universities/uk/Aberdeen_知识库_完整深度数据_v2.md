# University of Aberdeen Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Scotland)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | P0 follow-up |
| 研究生授课型 (PGT) | P0 follow-up |
| 研究生博士 (PhD) | P0 follow-up |
| 学院 / 系所总数 | P0 follow-up |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

> ⚠ P0: Full faculty/department hierarchy requires website extraction.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

> ⚠ P0: Full degree inventory requires course extraction.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

> ⚠ P0: Matrix requires full course extraction.

---

## SECTION 1 — Undergraduate education

> ⚠ P0: Full programme listing requires website extraction. The v1.0 file (now in `.v1-backup/`) contained only Computer Science undergraduate data. This v2.0 document provides the structural framework for the full programme listing.

**From v1.0**: University of Aberdeen undergraduate CS data available in `.v1-backup/Aberdeen_知识库_英国本科招生数据_v1.md`.

---

## SECTION 2 — Graduate education

> ⚠ P0: Postgraduate programme listing requires separate extraction from the university's postgraduate course pages.

---

## SECTION 3 — Application requirements & deadlines

> ⚠ P0: Full requirements need website extraction. See v1.0 backup file for CS-specific entry requirements, English language scores, and application deadlines.

---

## SECTION 4 — Costs & financial aid

| Fee status | Annual (typical) |
|-----------|-----------------|
| **Home (UK)** | £9,250 |
| **International** | P0 follow-up |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Aberdeen"
  source_url: https://www.aberdeen.ac.uk
  source_snippet: "University of Aberdeen"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| Priority | Data item |
|----------|-----------|
| **P0** | Full UG course listing (all departments, not just CS) |
| **P0** | Full PG taught course listing (MSc/MA/MBA) |
| **P0** | Full PG research programme listing (PhD/MPhil) |
| **P0** | Faculty/department academic hierarchy |
| **P0** | Degree type distribution and counts |
| **P0** | International tuition fees by course |
| **P1** | Per-course A-Level/IB entry requirements |
| **P1** | English language requirements (IELTS/TOEFL/PTE) |
| **P1** | Scholarship and funding details |
| **P2** | Course module details and curriculum structure |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Aberdeen | Cardiff | Newcastle |
|-----------|--------|---------|-----------|
| Total UG programmes | P0 follow-up | 237 | 147 |
| Russell Group | No | Yes | Yes |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: University official website
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ⚠ P0 | PG programmes ⚠ P0 | Evidence (1 block) ⚠
> **Next step**: Run full ego-browser extraction for each university to populate Sections 1-4 with complete data.
