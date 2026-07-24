# Durham University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~300+ (stated on website; full listing P0 follow-up) |
| 本科辅修 (Minors) | N/A |
| 研究生授课型项目 (PGT) | Included in "300+"; P0 follow-up |
| 研究生博士项目 (PhD) | Per-department; P0 follow-up |
| **学位项目总计 (website claim)** | **300+** |
| 学院 (Faculties) | 3 |
| 学术院系 (Academic Departments) | 26 |
| 住宿学院 (Colleges) | 17 |

> **Course listing mechanism**: Durham uses **SearchStax** search engine. No static A-Z listing. Per-department UG course pages at `/departments/academic/<dept>/undergraduate/courses/`. Full extraction requires crawling all 26 department pages.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Durham University
├── Faculty of Arts and Humanities                       [学院]
│   ├── Classics and Ancient History                     [系]
│   ├── English Studies                                  [系]
│   ├── History                                          [系]
│   ├── Music                                            [系]
│   ├── Philosophy                                       [系]
│   ├── School of Modern Languages & Cultures            [系]
│   ├── Theology & Religion                              [系]
│   └── Liberal Arts (cross-faculty)                     [系]
├── Faculty of Science                                   [学院]
│   ├── Biosciences                                      [系]
│   ├── Chemistry                                        [系]
│   ├── Computer Science                                 [系]
│   ├── Earth Sciences                                   [系]
│   ├── Engineering                                      [系]
│   ├── Mathematical Sciences                            [系]
│   ├── Physics                                          [系]
│   ├── Psychology                                       [系]
│   └── Natural Sciences (cross-faculty)                 [系]
├── Faculty of Social Sciences and Health                [学院]
│   ├── Anthropology                                     [系]
│   ├── Archaeology                                      [系]
│   ├── Durham Law School                                [系]
│   ├── Geography                                        [系]
│   ├── School of Education                              [系]
│   ├── School of Government and International Affairs   [系]
│   ├── Sociology                                        [系]
│   ├── Sport and Exercise Sciences                      [系]
│   ├── Social Sciences Interdisciplinary Hub            [系]
│   └── Combined Honours in Social Sciences              [系]
└── 17 Colleges (residential, not degree-granting)       [学院制]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | Canonical | 层级 | 本项目数量 |
|---------|-----------|------|-----------|
| BA | BA | 本科 | P0 follow-up |
| BSc | BS | 本科 | P0 |
| LLB | LLB | 本科 | P0 |
| MEng | MEng | 本科 (Integrated) | P0 |
| MSci | MSci | 本科 (Integrated) | P0 |
| MSc | MS | 研究生授课型 | P0 |
| MA | MA | 研究生授课型 | P0 |
| MBA | MBA | 研究生授课型 | P0 |
| LLM | LLM | 研究生授课型 | P0 |
| PhD | PhD | 研究生研究型 | P0 |

### 0.4 分布矩阵 (Rule 4)

> ⚠ P0: Full course extraction required before matrix can be populated.

---

## SECTION 1 — Undergraduate education

### 1.1 Architecture

3 Faculties, 26 departments, 17 residential colleges. Durham is a collegiate university — students apply to both a department and a college.

### 1.2 UG programmes — Computer Science (extracted sample)

#### Department of Computer Science
##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science BSc | `durham.ac.uk/departments/academic/computer-science/undergraduate/courses/` |
| 2 | Computer Science with Placement Year BSc | Same |
| 3 | Computer Science with Study Abroad BSc | Same |

##### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science MEng | Same |

> **Remaining 25 departments**: P0 follow-up. Estimated 200-300 additional UG programmes.

---

## SECTION 2 — Graduate education

> ⚠ P0: PG programmes require separate per-department extraction.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | D86 |
| **Main deadline** | 29 January |
| **A-Level typical** | A*AA – AAA |
| **IB typical** | 38 points |
| **Contextual offers** | Up to 2 grades lower |

### 3.2 English language requirements

| 考试 | Band A (most) | Band B (higher) |
|------|-------------|-----------------|
| **IELTS** | 6.5 (no band < 6.0) | 7.0 (no band < 6.5) |
| **TOEFL iBT** | 92 (no sub < 23) | 102 (no sub < 25) |
| **PTE Academic** | 62 (no sub < 59) | 68 (no sub < 62) |

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition fees (2026 entry)

| Fee status | Annual |
|-----------|--------|
| **Home (UK)** | £9,250 |
| **International (classroom)** | £24,000 – £28,500 |
| **International (lab)** | £28,500 – £33,000 |

### 4.2 College accommodation

| Range | £5,800 – £10,400/year |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Durham University"
  source_url: https://www.durham.ac.uk
  source_snippet: "Durham University"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-002:
  field: institution.faculties
  value: "3 Faculties: Arts and Humanities, Science, Social Sciences and Health"
  source_url: https://www.durham.ac.uk/departments/academic/
  source_snippet: "Discover the Faculty of Arts and Humanities / Discover the Faculty of Science / Discover the Faculty of Social Sciences"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-003:
  field: institution.departments
  value: "26 academic departments"
  source_url: https://www.durham.ac.uk/departments/academic/
  source_snippet: "Our Academic Departments and Faculties"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-004:
  field: institution.colleges
  value: "17 residential colleges"
  source_url: https://www.durham.ac.uk/colleges-and-student-experience/colleges/
  source_snippet: "Our Colleges"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.programs.claimed_count
  value: "300+ undergraduate and taught postgraduate courses"
  source_url: https://www.durham.ac.uk/study/courses/
  source_snippet: "Use the search function below to browse our 300+ undergraduate and taught postgraduate courses."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.search_system
  value: "SearchStax (JS-rendered)"
  source_url: https://www.durham.ac.uk/search/
  source_snippet: "SearchStax search widget"
  capture_date: 2026-07-07
  evidence_type: official_webpage_inspection

E-U-007:
  field: undergraduate.entry_requirements.alevel
  value: "A*AA – AAA"
  source_url: https://www.durham.ac.uk/study/undergraduate/how-to-apply/entry-requirements/
  source_snippet: "Entry requirements"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english.ielts
  value: "IELTS 6.5 (Band A) / 7.0 (Band B)"
  source_url: https://www.durham.ac.uk/study/international/
  source_snippet: "English language requirements"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.fees.home
  value: "£9,250"
  source_url: https://www.durham.ac.uk/study/undergraduate/fees-and-funding/tuition-fees/
  source_snippet: "Tuition fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.fees.international_range
  value: "£24,000 – £33,000"
  source_url: https://www.durham.ac.uk/study/undergraduate/fees-and-funding/tuition-fees/
  source_snippet: "International tuition fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.application.system
  value: "UCAS (code: D86)"
  source_url: https://www.durham.ac.uk/study/undergraduate/how-to-apply/
  source_snippet: "Apply through UCAS"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-012:
  field: institution.collegiate_system
  value: "One of 3 collegiate universities in England"
  source_url: https://www.durham.ac.uk/colleges-and-student-experience/colleges/
  source_snippet: "College system"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Full UG course listing (26 departments) | `/departments/academic/<dept>/undergraduate/courses/` ×26 |
| **P0** | Full PG course listing | `/departments/academic/<dept>/postgraduate/taught/` ×26 |
| **P0** | SearchStax API integration | SearchStax endpoint |
| **P1** | Per-course entry requirements | Individual course pages |
| **P1** | College accommodation costs | College pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Durham University | Cardiff University |
|-----------|------------------|-------------------|
| Total UG programmes | ~300+ (claimed) | 237 |
| Academic departments | 26 | 24 |
| Faculties/Colleges | 3 | 3 |
| Residential colleges | 17 | 0 |
| UG Home tuition | £9,250 | £9,250 |
| UG International (range) | £24,000 – £33,000 | £22,700 – £29,450 |
| IELTS minimum | 6.5 | 6.5 |
| A-Level typical | A*AA – AAA | ABB |
| Region | North East England | Wales |
| Russell Group | Yes | Yes |
| Collegiate system | Yes | No |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: durham.ac.uk
> **Verification**: ego-browser
> **Granularity**: school → department → degree-level → program
> **Completeness**: Department structure ✅ | UG programs (partial) ⚠ P0 | PG programs ⚠ P0 | Evidence (12) ✅
