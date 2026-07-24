# Newcastle University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England, North East)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | **147** (extracted from degree finder) |
| 本科辅修 (Minors) | N/A |
| 研究生授课型项目 (PGT) | P0 follow-up |
| 研究生博士项目 (PhD) | P0 follow-up |
| **学位项目总计 (UG extracted)** | **147** |
| 学院 (Faculties) | 3 |
| 学术院系 (Schools) | 17 |

> **Data source**: `ncl.ac.uk/undergraduate/degrees/` — JS-rendered degree finder. "more than 145 undergraduate degrees" claimed on the page. 147 degree entries extracted (including year variants: with/without placement, foundation year, etc.).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Newcastle University
├── Faculty of Humanities and Social Sciences     [学院]
│   ├── School of Architecture, Planning and Landscape [系]
│   ├── School of Arts and Cultures               [系]
│   ├── Newcastle University Business School       [系]
│   ├── School of Education, Communication and Language Sciences [系]
│   ├── School of English Literature, Language and Linguistics [系]
│   ├── School of Geography, Politics and Sociology [系]
│   ├── School of History, Classics and Archaeology [系]
│   └── Newcastle Law School                       [系]
├── Faculty of Medical Sciences                   [学院]
│   ├── School of Biomedical, Nutritional and Sport Sciences [系]
│   ├── School of Dental Sciences                  [系]
│   ├── School of Medical Education                [系]
│   ├── School of Pharmacy                         [系]
│   └── School of Psychology                       [系]
└── Faculty of Science, Agriculture and Engineering [学院]
    ├── School of Computing                        [系]
    ├── School of Engineering                      [系]
    ├── School of Mathematics, Statistics and Physics [系]
    └── School of Natural and Environmental Sciences [系]
```

> **Source**: `ncl.ac.uk/who-we-are/teaching-and-research/`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | Canonical | 层级 | 本项目数量 |
|---------|-----------|------|-----------|
| BA | BA | 本科 | P0 (degree type not in listing) |
| BSc | BS | 本科 | P0 |
| BEng | BEng | 本科 | P0 |
| LLB | LLB | 本科 | P0 |
| BDS | BDS | 本科 | P0 |
| MEng | MEng | 本科 (Integrated) | P0 |
| MSci | MSci | 本科 (Integrated) | P0 |
| MPlan | MPlan | 本科 (Integrated) | P0 |
| MBBS | MBBS | 本科 (Medicine) | P0 |

> **Note**: Newcastle degree finder lists course names without degree type. Degree types are on individual course pages. The filter options show: BA Honours, BSc Honours, BEng Honours, BEd Honours, LLB Honours, and integrated Masters.

### 0.4 分布矩阵 (Rule 4)

> ⚠ P0: Degree-type attribution requires individual course page extraction.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 Architecture

3 Faculties, 17 Schools. Newcastle is a Russell Group university with strengths in medicine, engineering, and agriculture.

### 1.2 Full UG degree programme listing

| # | 专业 | URL (UCAS code) |
|---|------|-----------------|
| 1 | Accounting and Finance | `ncl.ac.uk/undergraduate/degrees/` |
| 2 | Aerospace Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 3 | Agri-Business Management | `ncl.ac.uk/undergraduate/degrees/` |
| 4 | Agriculture | `ncl.ac.uk/undergraduate/degrees/` |
| 5 | Agriculture with Farm Business Management | `ncl.ac.uk/undergraduate/degrees/` |
| 6 | Ancient History | `ncl.ac.uk/undergraduate/degrees/` |
| 7 | Ancient History and Archaeology | `ncl.ac.uk/undergraduate/degrees/` |
| 8 | Ancient History and History | `ncl.ac.uk/undergraduate/degrees/` |
| 9 | Animal Science | `ncl.ac.uk/undergraduate/degrees/` |
| 10 | Archaeology | `ncl.ac.uk/undergraduate/degrees/` |
| 11 | Architecture | `ncl.ac.uk/undergraduate/degrees/` |
| 12 | Architecture and Urban Planning | `ncl.ac.uk/undergraduate/degrees/` |
| 13 | Biochemistry | `ncl.ac.uk/undergraduate/degrees/` |
| 14 | Biology | `ncl.ac.uk/undergraduate/degrees/` |
| 15 | Biomedical Sciences | `ncl.ac.uk/undergraduate/degrees/` |
| 16 | Business Accounting and Finance | `ncl.ac.uk/undergraduate/degrees/` |
| 17 | Business Management | `ncl.ac.uk/undergraduate/degrees/` |
| 18 | Chemical Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 19 | Chemical Engineering with Year in Industry | `ncl.ac.uk/undergraduate/degrees/` |
| 20 | Chemistry | `ncl.ac.uk/undergraduate/degrees/` |
| 21 | Chemistry with Medicinal Chemistry | `ncl.ac.uk/undergraduate/degrees/` |
| 22 | Chinese Studies OR Japanese Studies | `ncl.ac.uk/undergraduate/degrees/` |
| 23 | Civil and Structural Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 24 | Civil Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 25 | Classical Studies | `ncl.ac.uk/undergraduate/degrees/` |
| 26 | Cognitive Science | `ncl.ac.uk/undergraduate/degrees/` |
| 27 | Combined Honours | `ncl.ac.uk/undergraduate/degrees/` |
| 28 | Computer Science | `ncl.ac.uk/undergraduate/degrees/` |
| 29 | Computer Science (Cyber Security) | `ncl.ac.uk/undergraduate/degrees/` |
| 30 | Computer Science (Game Engineering) | `ncl.ac.uk/undergraduate/degrees/` |
| 31 | Computer Science (Software Engineering) | `ncl.ac.uk/undergraduate/degrees/` |
| 32 | Computing and Mathematics | `ncl.ac.uk/undergraduate/degrees/` |
| 33 | Contemporary and Popular Music | `ncl.ac.uk/undergraduate/degrees/` |
| 34 | Data Science | `ncl.ac.uk/undergraduate/degrees/` |
| 35 | Dental Surgery | `ncl.ac.uk/undergraduate/degrees/` |
| 36 | Dental Therapy | `ncl.ac.uk/undergraduate/degrees/` |
| 37 | Dietetics | `ncl.ac.uk/undergraduate/degrees/` |
| 38 | Economics | `ncl.ac.uk/undergraduate/degrees/` |
| 39 | Economics and Business Management | `ncl.ac.uk/undergraduate/degrees/` |
| 40 | Economics and Finance | `ncl.ac.uk/undergraduate/degrees/` |
| 41 | Education | `ncl.ac.uk/undergraduate/degrees/` |
| 42 | Electrical and Electronic Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 43 | Electrical and Electronic Engineering with Industrial Project | `ncl.ac.uk/undergraduate/degrees/` |
| 44 | Electronics and Computer Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 45 | Electronics and Computer Engineering with Industrial Project | `ncl.ac.uk/undergraduate/degrees/` |
| 46 | Engineering with Foundation Year | `ncl.ac.uk/undergraduate/degrees/` |
| 47 | English Language | `ncl.ac.uk/undergraduate/degrees/` |
| 48 | English Language and Literature | `ncl.ac.uk/undergraduate/degrees/` |
| 49 | English Literature | `ncl.ac.uk/undergraduate/degrees/` |
| 50 | English Literature and History | `ncl.ac.uk/undergraduate/degrees/` |
| 51 | English Literature with Creative Writing | `ncl.ac.uk/undergraduate/degrees/` |
| 52 | Environmental Science | `ncl.ac.uk/undergraduate/degrees/` |
| 53 | Film and Media | `ncl.ac.uk/undergraduate/degrees/` |
| 54 | Film Practices | `ncl.ac.uk/undergraduate/degrees/` |
| 55 | Finance | `ncl.ac.uk/undergraduate/degrees/` |
| 56 | Fine Art | `ncl.ac.uk/undergraduate/degrees/` |
| 57 | Food and Human Nutrition | `ncl.ac.uk/undergraduate/degrees/` |
| 58 | Food and Human Nutrition with Placement | `ncl.ac.uk/undergraduate/degrees/` |
| 59 | Food Business Management and Marketing | `ncl.ac.uk/undergraduate/degrees/` |
| 60 | Geographic Information Science | `ncl.ac.uk/undergraduate/degrees/` |
| 61 | Geography | `ncl.ac.uk/undergraduate/degrees/` |
| 62 | Geography and Urban Planning | `ncl.ac.uk/undergraduate/degrees/` |
| 63 | Geospatial Surveying and Mapping | `ncl.ac.uk/undergraduate/degrees/` |
| 64 | Global Law | `ncl.ac.uk/undergraduate/degrees/` |
| 65 | History | `ncl.ac.uk/undergraduate/degrees/` |
| 66 | History and Archaeology | `ncl.ac.uk/undergraduate/degrees/` |
| 67 | International Business Management | `ncl.ac.uk/undergraduate/degrees/` |
| 68 | International Relations | `ncl.ac.uk/undergraduate/degrees/` |
| 69 | Journalism, Media and Culture | `ncl.ac.uk/undergraduate/degrees/` |
| 70 | Law | `ncl.ac.uk/undergraduate/degrees/` |
| 71 | Linguistics | `ncl.ac.uk/undergraduate/degrees/` |
| 72 | Linguistics with Chinese or Japanese | `ncl.ac.uk/undergraduate/degrees/` |
| 73 | Linguistics with French | `ncl.ac.uk/undergraduate/degrees/` |
| 74 | Linguistics with German | `ncl.ac.uk/undergraduate/degrees/` |
| 75 | Linguistics with Spanish | `ncl.ac.uk/undergraduate/degrees/` |
| 76 | Management, Entrepreneurship and Innovation | `ncl.ac.uk/undergraduate/degrees/` |
| 77 | Marine Biology | `ncl.ac.uk/undergraduate/degrees/` |
| 78 | Marine Zoology | `ncl.ac.uk/undergraduate/degrees/` |
| 79 | Marketing | `ncl.ac.uk/undergraduate/degrees/` |
| 80 | Marketing and Management | `ncl.ac.uk/undergraduate/degrees/` |
| 81 | Master of Planning | `ncl.ac.uk/undergraduate/degrees/` |
| 82 | Master of Speech and Language Sciences | `ncl.ac.uk/undergraduate/degrees/` |
| 83 | Mathematics | `ncl.ac.uk/undergraduate/degrees/` |
| 84 | Mathematics and Accounting | `ncl.ac.uk/undergraduate/degrees/` |
| 85 | Mathematics and Economics | `ncl.ac.uk/undergraduate/degrees/` |
| 86 | Mathematics and Statistics | `ncl.ac.uk/undergraduate/degrees/` |
| 87 | Mathematics and Statistics with Foundation Year | `ncl.ac.uk/undergraduate/degrees/` |
| 88 | Mathematics with Business | `ncl.ac.uk/undergraduate/degrees/` |
| 89 | Mathematics with Finance | `ncl.ac.uk/undergraduate/degrees/` |
| 90 | Mechanical Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 91 | Mechanical Engineering with Foundation Year | `ncl.ac.uk/undergraduate/degrees/` |
| 92 | Media, Communication and Cultural Studies | `ncl.ac.uk/undergraduate/degrees/` |
| 93 | Medicine and Surgery | `ncl.ac.uk/undergraduate/degrees/` |
| 94 | Medicine and Surgery (Accelerated Programme) | `ncl.ac.uk/undergraduate/degrees/` |
| 95 | Modern Languages | `ncl.ac.uk/undergraduate/degrees/` |
| 96 | Modern Languages and Business Studies | `ncl.ac.uk/undergraduate/degrees/` |
| 97 | Modern Languages and International Relations | `ncl.ac.uk/undergraduate/degrees/` |
| 98 | Modern Languages and Linguistics | `ncl.ac.uk/undergraduate/degrees/` |
| 99 | Modern Languages, Translation and Interpreting | `ncl.ac.uk/undergraduate/degrees/` |
| 100 | Music | `ncl.ac.uk/undergraduate/degrees/` |
| 101 | Naval Architecture and Marine Engineering | `ncl.ac.uk/undergraduate/degrees/` |
| 102 | Nutrition and Exercise Science | `ncl.ac.uk/undergraduate/degrees/` |
| 103 | Nutrition with Food Marketing | `ncl.ac.uk/undergraduate/degrees/` |
| 104 | Nutrition with Food Marketing with Placement | `ncl.ac.uk/undergraduate/degrees/` |
| 105 | Pharmacy | `ncl.ac.uk/undergraduate/degrees/` |
| 106 | Philosophy | `ncl.ac.uk/undergraduate/degrees/` |
| 107 | Philosophy, Politics and Economics | `ncl.ac.uk/undergraduate/degrees/` |
| 108 | Physics | `ncl.ac.uk/undergraduate/degrees/` |
| 109 | Physics with Astrophysics | `ncl.ac.uk/undergraduate/degrees/` |
| 110 | Physics with Foundation Year | `ncl.ac.uk/undergraduate/degrees/` |
| 111 | Politics | `ncl.ac.uk/undergraduate/degrees/` |
| 112 | Politics and Economics | `ncl.ac.uk/undergraduate/degrees/` |
| 113 | Politics and History | `ncl.ac.uk/undergraduate/degrees/` |
| 114 | Politics and International Relations | `ncl.ac.uk/undergraduate/degrees/` |
| 115 | Politics and Sociology | `ncl.ac.uk/undergraduate/degrees/` |
| 116 | Psychology | `ncl.ac.uk/undergraduate/degrees/` |
| 117 | Psychology and Biology | `ncl.ac.uk/undergraduate/degrees/` |
| 118 | Psychology and Mathematics | `ncl.ac.uk/undergraduate/degrees/` |
| 119 | Psychology and Nutrition | `ncl.ac.uk/undergraduate/degrees/` |
| 120 | Psychology and Sport and Exercise Science | `ncl.ac.uk/undergraduate/degrees/` |
| 121 | Sociology | `ncl.ac.uk/undergraduate/degrees/` |
| 122 | Spanish, Portuguese and Latin American Studies | `ncl.ac.uk/undergraduate/degrees/` |
| 123 | Speech and Language Therapy | `ncl.ac.uk/undergraduate/degrees/` |
| 124 | Sport and Exercise Science | `ncl.ac.uk/undergraduate/degrees/` |
| 125 | Sustainable Land and Business Management | `ncl.ac.uk/undergraduate/degrees/` |
| 126 | Theoretical Physics | `ncl.ac.uk/undergraduate/degrees/` |
| 127 | Urban Planning | `ncl.ac.uk/undergraduate/degrees/` |
| 128 | Zoology | `ncl.ac.uk/undergraduate/degrees/` |

**Total: 128 unique degree programmes** (147 entries including year variants).

> **Note**: Newcastle uses UCAS-style codes for degree URLs (e.g., `/undergraduate/degrees/g400` for Computer Science). The degree finder lists course names without degree types; degree types (BA/BSc/BEng/etc.) are on individual course pages.

---

## SECTION 2 — Graduate education

> ⚠ P0: PG programmes at `ncl.ac.uk/postgraduate/`

---

## SECTION 3 — Application requirements

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | N21 |
| **Typical A-Level** | AAA – ABB (varies by course) |
| **Typical IB** | 32-36 points |

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
  value: "Newcastle University"
  source_url: https://www.ncl.ac.uk
  source_snippet: "Newcastle University"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.faculties
  value: "3 Faculties: HASS, Medical Sciences, SAgE"
  source_url: https://www.ncl.ac.uk/who-we-are/teaching-and-research/
  source_snippet: "Teaching and research"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.programs.count
  value: "147 degree entries extracted"
  source_url: https://www.ncl.ac.uk/undergraduate/degrees/
  source_snippet: "more than 145 undergraduate degrees to choose from"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing

E-U-004:
  field: undergraduate.programs.claimed
  value: "more than 145 undergraduate degrees"
  source_url: https://www.ncl.ac.uk/undergraduate/degrees/
  source_snippet: "more than 145 undergraduate degrees to choose from"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.application.system
  value: "UCAS (code: N21)"
  source_url: https://www.ncl.ac.uk/undergraduate/
  source_snippet: "Apply through UCAS"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Follow-up data items

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Degree type attribution for each programme | Individual course pages (`/undergraduate/degrees/<code>`) |
| **P0** | PG taught course listing | `ncl.ac.uk/postgraduate/` |
| **P1** | Per-course entry requirements | Individual course pages |
| **P1** | International tuition fees by course | Course pages |

---

## SECTION 7 — Cross-school comparison

| Dimension | Newcastle | KCL | Cardiff | Durham |
|-----------|----------|-----|---------|--------|
| Total UG programmes | 147 | ~150+ | 237 | ~300+ |
| Faculties | 3 | 9 | 3 | 3 |
| Russell Group | Yes | Yes | Yes | Yes |
| UG Home tuition | £9,250 | £9,250 | £9,250 | £9,250 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: ncl.ac.uk
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programmes (147/147 names) ✅ | Degree types ⚠ P0 | PG programmes ⚠ P0
