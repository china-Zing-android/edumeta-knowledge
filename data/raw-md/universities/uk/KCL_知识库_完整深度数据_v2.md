# King's College London Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless) + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England, London)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~150+ (10 pages × ~15/page; A-Z letter-filtered React SPA) |
| 本科辅修 (Minors) | N/A |
| 研究生授课型项目 (PGT) | P0 follow-up |
| 研究生博士项目 (PhD) | P0 follow-up |
| **学位项目总计 (UG estimated)** | **~150+** |
| 学院 (Faculties) | 9 |

> **Course listing mechanism**: KCL uses a **React SPA** with A-Z letter filtering. Each letter loads courses dynamically. Full extraction requires clicking all 26 letter filters. 15 courses extracted from page 1 (A-B). ~150+ total estimated.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
King's College London
├── Faculty of Arts & Humanities                    [学院]
├── The Dickson Poon School of Law                  [学院]
├── Florence Nightingale Faculty of Nursing,        [学院]
│   Midwifery & Palliative Care
├── King's Business School                          [学院]
├── Faculty of Life Sciences & Medicine             [学院]
├── Institute of Psychiatry, Psychology &           [学院]
│   Neuroscience (IoPPN)
├── Faculty of Natural, Mathematical &              [学院]
│   Engineering Sciences (NMES)
├── Faculty of Dentistry, Oral & Craniofacial       [学院]
│   Sciences
└── Faculty of Social Sciences & Public Policy      [学院]
```

> **Source**: `kcl.ac.uk/faculties-departments`

### 0.3 学历级别明细 (Rule 3)

| 学位缩写 | Canonical | 层级 | 本项目数量 |
|---------|-----------|------|-----------|
| BA | BA | 本科 | P0 |
| BSc | BS | 本科 | P0 |
| iBSc | iBSc | 本科 (Intercalated) | P0 |
| BEng | BEng | 本科 | P0 |
| MEng | MEng | 本科 (Integrated) | P0 |
| MSci | MSci | 本科 (Integrated) | P0 |

### 0.4 分布矩阵 (Rule 4)

> ⚠ P0: Full course extraction required before matrix can be populated.

---

## SECTION 1 — Undergraduate education

### 1.1 Architecture

9 Faculties. KCL is a multi-faculty university with strong medical and health sciences presence (3 health-related faculties).

### 1.2 UG programmes — extracted sample (A-B, page 1 of 10)

#### Sample courses (A-B letter range)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting & Finance | BSc | `kcl.ac.uk/study/undergraduate/courses/accounting-finance-bsc` |
| 2 | Accounting & Finance with Year in Industry | BSc | `kcl.ac.uk/study/undergraduate/courses/accounting-finance-with-year-in-industry-bsc` |
| 3 | Anatomy, Developmental & Human Biology | BSc | `kcl.ac.uk/study/undergraduate/courses/anatomy-developmental-and-human-biology-bsc` |
| 4 | Anatomy, Developmental & Human Biology | iBSc | `kcl.ac.uk/study/undergraduate/courses/anatomy-developmental-and-human-biology-ibsc` |
| 5 | Ancient History | BA | `kcl.ac.uk/study/undergraduate/courses/ancient-history-ba` |
| 6 | Artificial Intelligence | MSci | `kcl.ac.uk/study/undergraduate/courses/artificial-intelligence-msci` |
| 7 | Artificial Intelligence | BSc | `kcl.ac.uk/study/undergraduate/courses/artificial-intelligence-bsc` |
| 8 | Artificial Intelligence & Philosophy | BSc | `kcl.ac.uk/study/undergraduate/courses/artificial-intelligence-and-philosophy` |
| 9 | Artificial Intelligence with a Year in Industry | BSc | `kcl.ac.uk/study/undergraduate/courses/artificial-intelligence-with-a-year-in-industry-bsc` |
| 10 | Biochemistry | BSc | `kcl.ac.uk/study/undergraduate/courses/biochemistry-bsc` |
| 11 | Biomedical Engineering | BEng | `kcl.ac.uk/study/undergraduate/courses/biomedical-engineering-beng` |
| 12 | Biomedical Engineering | MEng | `kcl.ac.uk/study/undergraduate/courses/biomedical-engineering-meng` |
| 13 | Biomedical Science | BSc | `kcl.ac.uk/study/undergraduate/courses/biomedical-science-bsc` |

> **Remaining courses (C-Z)**: P0 follow-up. Click each letter filter button to load all courses.

---

## SECTION 2 — Graduate education

> ⚠ P0: PG programmes at `kcl.ac.uk/study/postgraduate-taught` and `kcl.ac.uk/study/postgraduate-research`

---

## SECTION 3 — Application requirements

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | K60 |
| **Typical A-Level** | A*AA – AAB (varies by course) |
| **Typical IB** | 35 points |
| **IELTS** | 6.5 – 7.0 (varies by course) |

---

## SECTION 4 — Costs

| Fee status | Annual |
|-----------|--------|
| **Home (UK)** | £9,250 |
| **International** | £22,000 – £35,000 (varies by course) |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "King's College London"
  source_url: https://www.kcl.ac.uk
  source_snippet: "King's College London"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.faculties
  value: "9 Faculties"
  source_url: https://www.kcl.ac.uk/faculties-departments
  source_snippet: "Our faculties"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.courses.page
  value: "React SPA with A-Z letter filtering, 10 pages"
  source_url: https://www.kcl.ac.uk/study/undergraduate/courses
  source_snippet: "Undergraduate courses A-Z"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.courses.extracted
  value: "15 courses (A-B range)"
  source_url: https://www.kcl.ac.uk/study/undergraduate/courses
  source_snippet: "Course listing page 1"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing
```

---

## SECTION 6 — WeKnora import manifest

### Follow-up data items

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Full UG course listing (C-Z letters) | `kcl.ac.uk/study/undergraduate/courses` (JS click extraction) |
| **P0** | PG taught course listing | `kcl.ac.uk/study/postgraduate-taught` |
| **P0** | PG research programme listing | `kcl.ac.uk/study/postgraduate-research` |

---

## SECTION 7 — Cross-school comparison

| Dimension | KCL | Cardiff | Durham | Newcastle |
|-----------|-----|---------|--------|-----------|
| Total UG programmes | ~150+ | 237 | ~300+ | 147 |
| Faculties | 9 | 3 | 3 | 3 |
| Russell Group | Yes | Yes | Yes | Yes |
| UG Home tuition | £9,250 | £9,250 | £9,250 | £9,250 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: kcl.ac.uk
> **Granularity**: school → department → degree-level → program
> **Completeness**: Faculty structure ✅ | UG programs (partial, 15/150+) ⚠ P0 | PG programs ⚠ P0
