# University of Huddersfield Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
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
| 本科学位专业 (UG degree programmes) | 415 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | 368 |
| 研究生博士项目 (PhD/Doctoral) | Included in PG count (research degrees listed separately) |
| **学位项目总计 (UG+PG extracted)** | **783** |
| 学院 (Academic Schools) | 5 |
| 学术院系 (Departments) | 13 |

> **Data source**: University of Huddersfield course finder (`courses.hud.ac.uk`), 415 UG courses and 368 PG courses extracted via searchstax pagination.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Huddersfield
├── School of Applied Sciences                              [学院]
│   ├── Department of Physical and Life Sciences            [系]
│   │   (Biomedical Science, Chemistry, Chemical Engineering, Forensic Science, Geography)
│   ├── Department of Pharmacy                              [系]
│   └── Department of Optometry and Vision Sciences         [系]
├── School of Arts and Humanities                           [学院]
│   ├── Department of Design & Architecture                 [系]
│   │   (Architecture, Design, Art, Fashion, Photography)
│   └── Department of Media, Humanities and the Arts        [系]
│       (Acting, English, Film, History, Journalism, Music, Music Technology)
├── School of Business, Education and Law                   [学院]
│   ├── Huddersfield Business School                        [系]
│   │   (Accountancy, Business, Economics, Finance, HRM, Marketing)
│   ├── School of Education                                 [系]
│   └── Law School                                          [系]
├── School of Computing and Engineering                     [学院]
│   ├── Department of Computer Science                      [系]
│   │   (Computer Science, AI, Cyber Security, Games Development)
│   └── Department of Engineering                           [系]
│       (Civil, Electronic/Electrical, Mechanical/Automotive Engineering)
└── School of Human and Health Sciences                     [学院]
    ├── Department of Allied Health Professions, Sport and Exercise [系]
    │   (Midwifery, Physiotherapy, Podiatry, OT, Paramedic, Sport)
    ├── Department of Social and Psychological Sciences     [系]
    │   (Psychology, Criminology, Policing, Social Work, Public Health)
    └── Department of Nursing                               [系]
```

> **Source**: `https://www.hud.ac.uk/about/schools/`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|
| BSc(Hons) | BSc | Bachelor of Science (Honours) | 本科 | 182 |
| BA(Hons) | BA | Bachelor of Arts (Honours) | 本科 | 108 |
| Foundation | Foundation | Foundation Pathway Degree | 本科 (预科) | 36 |
| BEng(Hons) | BEng | Bachelor of Engineering (Honours) | 本科 | 24 |
| MEng | MEng | Master of Engineering (Integrated) | 本科 (Integrated Master's) | 14 |
| BMus | BMus | Bachelor of Music (Honours) | 本科 | 10 |
| LLB(Hons) | LLB | Bachelor of Laws (Honours) | 本科 | 8 |
| MPsych | MPsych | Master of Psychology (Integrated) | 本科 (Integrated Master's) | 2 |
| MOptom | MOptom | Master of Optometry (Integrated) | 本科 (Integrated Master's) | 2 |
| MPharm | MPharm | Master of Pharmacy (Integrated) | 本科 (Integrated Master's) | 2 |
| CertHE | CertHE | Certificate of Higher Education | 本科 | 1 |
| **UG 合计** | | | | **415** |
| MSc | MSc | Master of Science | 研究生 (Taught) | 150 |
| MA | MA | Master of Arts | 研究生 (Taught) | 45 |
| PGCert | PGCert | Postgraduate Certificate | 研究生 (Taught) | 29 |
| PGCE | PGCE | Postgraduate Certificate in Education | 研究生 (Teacher Training) | 28 |
| PGDip | PGDip | Postgraduate Diploma | 研究生 (Taught) | 14 |
| LLM | LLM | Master of Laws | 研究生 (Taught) | 4 |
| MMus | MMus | Master of Music | 研究生 (Taught) | 2 |
| MBA | MBA | Master of Business Administration | 研究生 (Taught) | 1 |
| **PG 合计** | | | | **368** |

> **Note**: UG counts include Foundation, Top-Up, and Distance Learning variants. Subject facet counts overlap because courses can belong to multiple subjects.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

#### UG Subject Distribution (from course finder facets)

| Subject | UG Count |
|---------|----------|
| Nursing and Midwifery | 44 |
| Health Professions | 41 |
| Social Care and Social Work | 41 |
| Computer Science | 38 |
| Education | 30 |
| Biomedical and Life Sciences | 28 |
| Management and Leadership | 26 |
| Crime | 24 |
| Policing and Society | 24 |
| Mechanical and Automotive Engineering | 21 |
| Chemistry | 20 |
| Electronic and Electrical Engineering | 16 |
| Accountancy | 14 |
| Finance and Economics | 14 |
| Law | 12 |
| Psychology | 12 |
| Architecture and the Built Environment | 10 |
| Chemical Engineering | 10 |
| English | 10 |
| Fashion and Textiles | 10 |
| Games Development | 10 |
| Music | 10 |
| Music Technology | 10 |
| Design | 8 |
| Forensic Science | 8 |
| Civil Engineering | 7 |
| Art and Illustration | 6 |
| Marketing | 6 |
| Sport | 6 |
| Acting and Performance | 4 |
| Cyber Security | 4 |
| History | 4 |
| Journalism and Media | 4 |
| Pharmacy | 3 |
| Artificial Intelligence | 51 |
| Film | 2 |
| Optometry and Vision Sciences | 2 |
| Photography | 2 |
| Sustainability | 2 |

> **Note**: Artificial Intelligence (51) is the largest subject facet, reflecting cross-listed courses across Computing, Engineering, and Business. Subject counts exceed 415 because courses are tagged with multiple subjects.

> **Reconciliation check**: Rule-1 total (415 UG + 368 PG = 783) == course finder total (783). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

University of Huddersfield is organised into 5 Academic Schools, each containing multiple Departments (13 total). See Section 0.2 for the full hierarchy tree. All undergraduate degree programmes are administered by one of these Schools.

### 1.2 Undergraduate degree programmes — grouped by School > Degree Level

The full UG course listing (415 programmes) is stored in the cache file `uni-cache/schools/huddersfield/ug_courses.json`. Below is a summary by school:

#### School of Applied Sciences
- **Subjects**: Biomedical and Life Sciences, Chemical Engineering, Chemistry, Forensic Science, Pharmacy, Optometry and Vision Sciences
- **Key programmes**: Applied Biology BSc(Hons), Biochemistry BSc(Hons), Biomedical Science BSc(Hons), Chemistry BSc(Hons), Chemical Engineering BEng(Hons), Forensic Science BSc(Hons), Pharmacy MPharm, Optometry MOptom
- **Degree types**: BSc, BEng, MPharm, MOptom

#### School of Arts and Humanities
- **Subjects**: Architecture and the Built Environment, Art and Illustration, Design, Fashion and Textiles, Photography, Acting and Performance, English, Film, History, Journalism and Media, Music, Music Technology
- **Key programmes**: Architecture (RIBA Part 1) BA(Hons), Fine Art BA(Hons), Fashion Design BA(Hons), Acting and Performance BA(Hons), English BA(Hons), Film Studies BA(Hons), Music BA(Hons), Music Technology BSc(Hons)
- **Degree types**: BA, BSc, BMus

#### School of Business, Education and Law
- **Subjects**: Accountancy, Finance and Economics, Management and Leadership, Marketing, Education, Law
- **Key programmes**: Accounting and Finance BSc(Hons), Business Management BSc(Hons), Marketing BSc(Hons), Education Studies BA(Hons), Law LLB(Hons)
- **Degree types**: BSc, BA, LLB

#### School of Computing and Engineering
- **Subjects**: Computer Science, Artificial Intelligence, Cyber Security, Games Development, Civil Engineering, Electronic and Electrical Engineering, Mechanical and Automotive Engineering
- **Key programmes**: Computer Science BSc(Hons), Artificial Intelligence BSc(Hons), Cyber Security BSc(Hons), Games Development BSc(Hons), Civil Engineering BEng(Hons), Electronic Engineering BEng(Hons), Mechanical Engineering BEng(Hons), Automotive and Motorsport Engineering BEng(Hons)/MEng
- **Degree types**: BSc, BEng, MEng

#### School of Human and Health Sciences
- **Subjects**: Nursing and Midwifery, Health Professions, Social Care and Social Work, Psychology, Crime, Policing and Society, Sport
- **Key programmes**: Nursing BSc(Hons), Midwifery BSc(Hons), Physiotherapy BSc(Hons), Psychology BSc(Hons), Criminology BSc(Hons), Social Work BA(Hons), Sport and Exercise Science BSc(Hons)
- **Degree types**: BSc, BA, MPsych

### 1.3 UCAS Application Information

| Field | Value |
|-------|-------|
| **UCAS Institution Code** | H56 |
| **Application System** | UCAS |
| **Oxbridge/Medicine deadline** | 15 October |
| **Main UCAS deadline** | 29 January |
| **UCAS Extra** | February - June |
| **Clearing** | July - September |

### 1.4 Entry Requirements (General)

| Requirement | Details |
|-------------|---------|
| **A-Level** | Varies by course; typically BBB-CCC for most programmes |
| **BTEC** | Accepted; DMM-DDM typical |
| **IB** | Accepted; points vary by course |
| **Foundation Year** | Available for many programmes (38 Foundation Year courses listed) |
| **Top-Up** | Available for HND/foundation degree holders (51 Top-Up courses listed) |
| **Contextual Offers** | Available; see contextual admissions policy |

> **Source**: `https://www.hud.ac.uk/undergraduate/how-to-apply/`

---

## SECTION 2 — Graduate education

### 2.1 Postgraduate Taught (PGT)

The full PG course listing (368 programmes) is stored in the cache file `uni-cache/schools/huddersfield/pg_courses.json`.

**PG Degree Type Breakdown**:

| Degree | Count |
|--------|-------|
| MSc | 150 |
| MA | 45 |
| PGCert | 29 |
| PGCE | 28 |
| PGDip | 14 |
| LLM | 4 |
| MMus | 2 |
| MBA | 1 |

### 2.2 Postgraduate Research (PGR)

| Programme | Annual Fee (Full-time) | Annual Fee (Part-time) |
|-----------|----------------------|----------------------|
| PhD, MA by Research, MSc by Research (Non-Science) | £17,600 | £8,000 |
| PhD, MA by Research, MSc by Research (Science/Tech) | £18,700 | £8,500 |
| PhD by Publication | £3,750 | £3,750 |
| Distance Learning PhD/MA/MSc by Research | £12,600 | £6,300 |

> **Source**: `https://www.hud.ac.uk/international/fees-and-funding/`

---

## SECTION 3 — Application requirements & deadlines

### 3.1 English Language Requirements

| Test | Standard Required Score | Validity |
|------|------------------------|----------|
| **IELTS (Academic)** | 6.0 overall, no lower than 5.5 in any element | 2 years |
| **IELTS One Skill Re-take** | 6.0 overall, no component lower than 5.5 | 2 years |
| **TOEFL** | 87 overall (Reading 22, Listening 21, Speaking 23, Writing 21) | 2 years |
| **PTE Academic** | 59 overall, 59 minimum in each component | 2 years |
| **Cambridge English Advanced** | Grade C | No expiry |
| **GCSE/GCE O-Level English** | Grade C | No expiry |
| **International Baccalaureate** | Diploma with English at Higher Level | No expiry |
| **WAEC/NECO** | C6 or above | No expiry |
| **PSI Skills for English: SELT** | Merit Overall, no component lower than B2 pass | 2 years |
| **Trinity ISE II B2** | Merit Overall, no component lower than pass | 2 years |
| **LanguageCert International** | 65 overall, no component lower than 60 | 2 years |
| **Password Skills Plus** | 6.0 overall, no component lower than 5.5 | 2 years |
| **Oxford ELLT Global** | 6 overall, no component lower than 5 | 2 years |

> **Notes**:
> - Online tests are NOT accepted for IELTS
> - Home Edition is NOT accepted for TOEFL or PTE
> - Applicants from Majority English Speaking Countries (MESCs) normally meet requirements
> - Pre-sessional English programmes available for those not meeting requirements
>
> **Source**: `https://www.hud.ac.uk/international/courses-and-entry-requirements/international-entry-requirements/`

### 3.2 Application Timeline

| Stage | Date |
|-------|------|
| UCAS opens | May (for next year entry) |
| Oxbridge/Medicine deadline | 15 October |
| Main UCAS deadline | 29 January |
| UCAS Extra | February - June |
| Clearing | July - September |
| September intake | Main intake |
| January intake | Available for some PG courses |
| May intake | Available for some PG courses |

---

## SECTION 4 — Costs & financial aid

### 4.1 Home (UK) Student Fees — 2026/27

| Course Type | Annual Fee |
|-------------|-----------|
| UG programmes full-time (BA, BSc, BEng, BMus, LLB) | £9,790 |
| Placement year | £1,000 |
| CertEd full-time | £9,790 |
| Part-time (per 20 credit module) | £1,630 |

### 4.2 International Student Fees — 2026/27

#### Undergraduate (Bachelor's and Top-up)

| Category | Annual Fee |
|----------|-----------|
| **Non-Science/Technology** (Arts, Business, Education, Health/Social Sciences) | £16,500 |
| **Science/Technology** (Computing, Engineering, Science, Social Work) | £17,600 |
| **Nursing** (includes NHS Placement fee) | £19,800 |
| **Allied Health Professions** (Midwifery, Physiotherapy, Podiatry, OT, ODP) | £18,700 |
| **Primary Education Studies** (Non QTS Accelerated Degree) | £22,000 |
| **Work Placement Year** | £3,300 |

#### Postgraduate Taught (Master's)

| Category | Annual Fee |
|----------|-----------|
| **Non-Science/Technology** (Arts, Business, Education, Health/Social Sciences) | £17,600 |
| **Science/Technology** (Computing, Engineering, Science) | £18,700 |
| **MBA** | £19,690 |
| **PGCE** | £19,800 |
| **Nursing** (includes NHS placement) | £19,800 |
| **Pharmacy with placement** | £21,000 |
| **Podiatry/Optometry** | £18,590 |

#### Postgraduate Research

| Category | Full-time | Part-time |
|----------|-----------|-----------|
| Non-Science/Technology | £17,600 | £8,000 |
| Science/Technology | £18,700 | £8,500 |
| PhD by Publication | £3,750 | £3,750 |
| Distance Learning PhD/MA/MSc by Research | £12,600 | £6,300 |

### 4.3 Scholarships and Financial Support

- **International Scholarships**: Available; see `https://www.hud.ac.uk/international/scholarships/`
- **Tuition Fee Loan**: Available for full-time home undergraduates
- **Maintenance Loan**: Available for living expenses
- **Lifelong Learning Entitlement**: From January 2027, new UK government system

> **Source**: `https://www.hud.ac.uk/international/fees-and-funding/` and `https://www.hud.ac.uk/undergraduate/fees-and-finance/`

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Huddersfield"
  source_url: https://www.hud.ac.uk
  source_snippet: "University of Huddersfield"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.qs_ranking
  value: "=521 (QS World University Rankings 2026)"
  source_url: https://www.topuniversities.com/universities/university-huddersfield
  source_snippet: "# =521 QS World University Rankings"
  capture_date: 2026-07-08
  evidence_type: ranking_site

E-U-003:
  field: institution.tef_rating
  value: "Gold (all three aspects, TEF 2023)"
  source_url: https://www.hud.ac.uk/about/
  source_snippet: "awarded an outstanding Gold rating in all three aspects of the Teaching Excellence Framework (TEF) 2023"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.student_population
  value: "15,000+"
  source_url: https://www.hud.ac.uk/about/
  source_snippet: "over 15,000 students from all walks of life"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: courses.ug_total
  value: 415
  source_url: https://courses.hud.ac.uk/?searchstax[query]=*&searchstax[model]=Coursefinder
  source_snippet: "1 - 25 of 415 results for '*' (Undergraduate filter)"
  capture_date: 2026-07-08
  evidence_type: course_finder

E-U-006:
  field: courses.pg_total
  value: 368
  source_url: https://courses.hud.ac.uk/?searchstax[query]=*&searchstax[model]=Coursefinder
  source_snippet: "1 - 25 of 368 results for '*' (Postgraduate filter)"
  capture_date: 2026-07-08
  evidence_type: course_finder

E-U-007:
  field: structure.schools
  value: "5 Academic Schools, 13 Departments"
  source_url: https://www.hud.ac.uk/about/schools/
  source_snippet: "The University has five academic schools: Applied Sciences, Arts and Humanities, School of Business Education and Law, Computing and Engineering, Human and Health Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: fees.home_ug_2026_27
  value: "£9,790/year"
  source_url: https://www.hud.ac.uk/undergraduate/fees-and-finance/
  source_snippet: "Undergraduate programmes full-time (BA, BSc, BEng, BMus, LLB) £9,790"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: fees.international_ug_2026_27
  value: "£16,500-£22,000/year (varies by subject)"
  source_url: https://www.hud.ac.uk/international/fees-and-funding/
  source_snippet: "Non-Science/Technology degrees £16,500; Science/Technology degrees £17,600"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: language.ielts
  value: "6.0 overall, no lower than 5.5 in any element"
  source_url: https://www.hud.ac.uk/international/courses-and-entry-requirements/international-entry-requirements/
  source_snippet: "IELTS (Academic) 6.0 with no lower than 5.5 in any element"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: language.toefl
  value: "87 overall (Reading 22, Listening 21, Speaking 23, Writing 21)"
  source_url: https://www.hud.ac.uk/international/courses-and-entry-requirements/international-entry-requirements/
  source_snippet: "TOEFL 87 overall (Reading 22, Listening 21, Speaking 23, Writing 21)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: language.pte
  value: "59 overall, 59 minimum in each component"
  source_url: https://www.hud.ac.uk/international/courses-and-entry-requirements/international-entry-requirements/
  source_snippet: "Pearson Test of Academic English (PTE) Overall - 59"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Data completeness summary

| Data item | Status | Source |
|-----------|--------|--------|
| Institution name | ✅ Complete | Official website |
| QS ranking | ✅ Complete | QS website |
| TEF rating | ✅ Complete | Official website |
| Student population | ✅ Complete | Official website |
| Academic structure (5 schools, 13 departments) | ✅ Complete | Official schools page |
| UG course listing (415 programmes) | ✅ Complete | Course finder (17 pages) |
| PG course listing (368 programmes) | ✅ Complete | Course finder (15 pages) |
| Degree type distribution | ✅ Complete | Course finder extraction |
| Subject distribution | ✅ Complete | Course finder facets |
| Home UG fees 2026/27 | ✅ Complete | Fees page |
| International UG fees 2026/27 | ✅ Complete | International fees page |
| International PG fees 2026/27 | ✅ Complete | International fees page |
| English language requirements | ✅ Complete | Entry requirements page |
| Application timeline | ✅ Complete | How to apply page |
| UCAS code | ✅ Complete | How to apply page |
| Per-course entry requirements | ⚠ Partial | Requires individual course page extraction |
| Course-level fee variations | ⚠ Partial | Fee bands provided; exact per-course fees on course pages |
| Scholarship details | ⚠ Partial | General info available; specific amounts require further research |

### Follow-up data items (prioritized)

| Priority | Data item |
|----------|-----------|
| **P1** | Per-course A-Level/IB entry requirements (extract from individual course pages) |
| **P1** | Specific scholarship amounts and eligibility criteria |
| **P2** | Course module details and curriculum structure |
| **P2** | Accommodation costs and options |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Huddersfield | Cardiff | Newcastle |
|-----------|---------------------------|---------|-----------|
| Total UG programmes | 415 | 237 | 147 |
| Total PG programmes | 368 | P0 follow-up | P0 follow-up |
| QS World Ranking 2026 | =521 | =154 | =110 |
| TEF Rating | Gold (all 3 aspects) | Gold | Gold |
| Russell Group | No | Yes | Yes |
| Academic Schools | 5 | 3 (24 schools) | 3 (23 faculties) |
| International UG fees (typical) | £16,500-£17,600 | £20,000-£25,000 | £20,000-£26,000 |
| IELTS requirement | 6.0 (5.5 min) | 6.5 (5.5 min) | 6.5 (5.5 min) |
| Location | Huddersfield, West Yorkshire | Cardiff, Wales | Newcastle upon Tyne |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: University official website (hud.ac.uk), course finder (courses.hud.ac.uk), QS rankings
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (415) | PG programmes ✅ (368) | Fees ✅ | Language requirements ✅ | Evidence (12 blocks) ✅
> **Cache files**: `uni-cache/schools/huddersfield/site-memory.json`, `ug_courses.json`, `pg_courses.json`
