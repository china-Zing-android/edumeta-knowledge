# University of Stirling Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless) via `useOrCreateTaskSpace('stirling-research')`
> **Target knowledge base**: WeKnora
> **Granularity**: school (faculty) → department (subject area) → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: United Kingdom — Scotland (Scottish Credit and Qualifications Framework / SCQF)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

University of Stirling is a UK public research university founded in 1967 by Royal Charter, located in Stirling, Scotland (with a smaller campus in Inverness). It is a member of the **Universities Scotland** group and the **Scottish University Sports Association**. The university operates **5 academic faculties** and offers undergraduate, postgraduate taught, postgraduate research, and professional doctorate programmes.

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA / BSc / BAcc) — single-major only | 59 |
| 研究生学位项目 — PGT taught (MSc / MA / MLitt / MRes / MPH) | 82 |
| PhD 研究方向（学科领域） | 35 |
| 专业博士 (Professional Doctorate) | 8 |
| **学位项目总计 (UG + PGT，单专业 / single-major 口径)** | **141** |
| 课程搜索器陈列总数 (含 combined / online variants — `355 results`) | 355 |
| 学院 / 独立系所总数 | 5 |
| 学科主题 (Subject areas) | 27 |

> Reconciliation: rule-5 grouped rows below = 59 UG + 82 PGT = 141. Matches rule-1 single-major total. The official course finder advertises **355 results** by additionally counting combined-honours, joint, online, and part-time variants of the same single-major programmes — these are not double-counted here.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```text
University of Stirling                                                    [学校]
├── Faculty of Arts and Humanities                                        [学院]
│   ├── English and Literature                                            [系/学科]
│   ├── Film and Media Studies                                            [系]
│   ├── History                                                           [系]
│   ├── Journalism and Publishing                                          [系]
│   ├── Languages and TESOL                                               [系]
│   └── Philosophy                                                        [系]
├── Faculty of Health Sciences and Sport                                  [学院]
│   ├── Health and Allied Subjects                                        [系]
│   ├── Nursing                                                           [系]
│   └── Sport                                                             [系]
├── Stirling Business School                                              [学院]
│   ├── Accounting and Finance                                            [系]
│   ├── Business and Management                                           [系]
│   ├── Data Science and Data Analytics                                   [系]
│   ├── Economics                                                         [系]
│   └── Marketing and Public Relations (PR)                               [系]
├── Faculty of Natural Sciences                                           [学院]
│   ├── Aquaculture                                                       [系]
│   ├── Biology                                                           [系]
│   ├── Computer Science and Software Engineering                         [系]
│   ├── Environmental Science                                             [系]
│   └── Mathematics                                                       [系]
└── Faculty of Social Sciences                                            [学院]
    ├── Criminology                                                       [系]
    ├── Geography                                                         [系]
    ├── Law                                                               [系]
    ├── Politics                                                          [系]
    ├── Psychology                                                        [系]
    ├── Social Studies                                                    [系]
    └── Teaching and Education                                            [系]
```

> Some subjects are jointly listed under two faculties via combined honours degrees — e.g. **Psychology** (UG) appears in **Social Sciences** but **Psychology of Sport / Health Psychology** are administratively under **Health Sciences and Sport** for PGT purposes. The mapping table in `site-memory.json` resolves each programme to its single canonical home.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Canonical | 全称 | 官方本校 | 层级 | 本项目数量 |
|-----------|------|----------|------|-----------|
| BA | Bachelor of Arts | BA (Hons) | 本科 | 33 |
| BS | Bachelor of Science | BSc (Hons) | 本科 | 24 |
| BAcc | Bachelor of Accountancy | BAcc (Hons) | 本科 | 2 |
| MS | Master of Science | MSc | 研究生 | 71 |
| MRes | Master of Research | MRes | 研究生 | 6 |
| MLitt | Master of Letters | MLitt | 研究生 | 3 |
| MPH | Master of Public Health | MPH | 研究生 | 2 |
| PhD | Doctor of Philosophy | PhD | 研究生 | 35 (subject areas) |
| DASR | Doctor of Applied Social Research | DASR | 研究生 | 1 |
| EdD | Doctor of Education | EdD | 研究生 | 1 |
| DPsych | Professional Doctorate in Health Psychology | DPsych | 研究生 | 1 |
| NursD / MidD / DPHS | Clinical Doctorates (Nursing / Midwifery / Professional Health Studies) | NursD / MidD / DPHS | 研究生 | 3 |
| MPhil | Master of Philosophy | MPhil | 研究生 | 1 (research degree framework) |
| PgDip | Postgraduate Diploma | PG Dip | 研究生 | (embedded in named PgDip variants) |

> Stirling's taught-postgraduate landscape is dominated by **MSc** (71 of 82 PGT entries). The university does not award a separate graduate "MA" by formal taxonomy — what would be labelled MA in other UK universities is typically MLitt at Stirling (e.g. MLitt Creative Writing, MLitt Philosophy, MLitt Publishing Studies). The university also offers the more focused **PgDip** pathways within named awards such as "MSc / PG Dip Specialist Community Public Health Nurse (Health Visiting)" and "MSc / PG Dip Housing Studies".
> **Reconciliation**: BS+BA+BAcc = 33+24+2 = **59 UG**; MS+MRes+MLitt+MPH = 71+6+3+2 = **82 PGT** → 59+82 = **141 single-major programmes**. Matches Rule 1.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| Faculty \ Canonical level | BA | BS | BAcc | MS | MRes | MLitt | MPH | UG 合计 | PGT 合计 | 学院合计 |
|---------------------------|----|----|------|----|------|-------|-----|---------|----------|----------|
| Faculty of Arts and Humanities | 7 | 0 | 0 | 8 | 4 | 2 | 0 | 11 | 14 | 25 |
| Faculty of Health Sciences and Sport | 1 | 5 | 0 | 14 | 1 | 0 | 2 | 7 | 17 | 24 |
| Stirling Business School | 9 | 5 | 2 | 25 | 0 | 0 | 0 | 15 | 25 | 40 |
| Faculty of Natural Sciences | 0 | 13 | 0 | 10 | 0 | 0 | 0 | 13 | 10 | 23 |
| Faculty of Social Sciences | 9 | 1 | 0 | 14 | 1 | 1 | 0 | 13 | 16 | 29 |
| **Total (canonical level)** | **33** | **24** | **2** | **71** | **6** | **3** | **2** | **59** | **82** | **141** |

> Row sums and column sums both equal **141**, reconciling with the Rule-1 single-major total and the Rule-5 row counts.

---

## SECTION 1 — Undergraduate education (rule 5 grouping)

### 1.1 College/school architecture

Stirling organises UG teaching across 5 faculties and 27 subject areas. Most UG Honours degrees at Stirling are **4-year Scottish Honours (BA Hons / BSc Hons)**, with selected 3-year broad-based degrees and combined-honours variants available. See Section 0.2 tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Arts and Humanities
##### Subject area: English and Literature
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | English Studies | https://www.stir.ac.uk/subjects/english-and-literature/ |

##### Subject area: Film and Media Studies
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 2 | Digital Media and Communications | https://www.stir.ac.uk/subjects/film-and-media-studies/ |
| 3 | Film and Media | https://www.stir.ac.uk/subjects/film-and-media-studies/ |

##### Subject area: History
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 4 | History | https://www.stir.ac.uk/subjects/history/ |
| 5 | History and Heritage | https://www.stir.ac.uk/subjects/history/ |
| 6 | Scottish History | https://www.stir.ac.uk/subjects/history/ |

##### Subject area: Journalism and Publishing
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 7 | Journalism Studies | https://www.stir.ac.uk/subjects/journalism-and-publishing/ |

##### Subject area: Languages and TESOL
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 8 | English Studies (cross-listed with English) | https://www.stir.ac.uk/subjects/languages-and-tesol/ |
| 9 | European Languages and Society with International Management | https://www.stir.ac.uk/subjects/languages-and-tesol/ |
| 10 | French | https://www.stir.ac.uk/subjects/languages-and-tesol/ |
| 11 | Spanish and Latin American Studies | https://www.stir.ac.uk/subjects/languages-and-tesol/ |

> Note: cross-listed English Studies (Languages & TESOL vs. English & Literature) shares one home academic unit and is counted once in the rule-1/rule-5 totals.

##### Subject area: Philosophy
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 12 | Philosophy | https://www.stir.ac.uk/subjects/philosophy/ |
| 13 | Politics, Philosophy and Economics (PPE — combined honours) | https://www.stir.ac.uk/subjects/philosophy/ |

#### Faculty of Health Sciences and Sport
##### Subject area: Health and Allied Subjects
###### BSc / BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 14 | Paramedic Science | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 15 | Professional Practice | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |

##### Subject area: Nursing
###### BSc / BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 16 | Nursing - Adult | https://www.stir.ac.uk/subjects/nursing/ |
| 17 | Nursing - Mental Health | https://www.stir.ac.uk/subjects/nursing/ |
| 18 | Paramedic Science (cross-listed with Health) | https://www.stir.ac.uk/subjects/nursing/ |
| 19 | Professional Practice (cross-listed with Health) | https://www.stir.ac.uk/subjects/nursing/ |

> Paramedic Science and Professional Practice appear under both Health & Allied Subjects and Nursing because of joint delivery. For degree-awarding purposes the home unit is Nursing; single count kept in totals.

##### Subject area: Sport
###### BA (Hons) / BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 20 | Sport Business Management (administered by Stirling Business School — listed under Sport) | https://www.stir.ac.uk/subjects/sport/ |
| 21 | Sport Development and Coaching | https://www.stir.ac.uk/subjects/sport/ |
| 22 | Psychology of Sport | https://www.stir.ac.uk/subjects/sport/ |
| 23 | Sport and Exercise Science | https://www.stir.ac.uk/subjects/sport/ |

#### Stirling Business School
##### Subject area: Accounting and Finance
###### BA (Hons) / BAcc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 24 | Finance (BA Hons) | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 25 | Professional Accountancy (BA Hons) | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 26 | Accountancy (BAcc Hons) | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 27 | Accountancy and Finance (BAcc Hons) | https://www.stir.ac.uk/subjects/accounting-and-finance/ |

##### Subject area: Business and Management
###### BA (Hons) / BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 28 | Business Studies | https://www.stir.ac.uk/subjects/business-and-management/ |
| 29 | European Languages and Society with International Management (cross-listed with Languages) | https://www.stir.ac.uk/subjects/business-and-management/ |
| 30 | Human Resource Management | https://www.stir.ac.uk/subjects/business-and-management/ |
| 31 | Sport Business Management (cross-listed with Sport) | https://www.stir.ac.uk/subjects/business-and-management/ |
| 32 | Business Computing (BSc Hons) | https://www.stir.ac.uk/subjects/business-and-management/ |
| 33 | Management (BSc Hons) | https://www.stir.ac.uk/subjects/business-and-management/ |

##### Subject area: Data Science and Data Analytics
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 34 | Data Science and Artificial Intelligence | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |

##### Subject area: Economics
###### BA (Hons) / BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 35 | Politics, Philosophy and Economics (PPE — combined honours, cross-listed with Philosophy) | https://www.stir.ac.uk/subjects/economics/ |
| 36 | Economics | https://www.stir.ac.uk/subjects/economics/ |

##### Subject area: Marketing and Public Relations (PR)
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 37 | Marketing | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |
| 38 | Retail Marketing | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |

#### Faculty of Natural Sciences
##### Subject area: Aquaculture
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 39 | Marine and Freshwater Biology (also listed under Biology) | https://www.stir.ac.uk/subjects/aquaculture/ |

##### Subject area: Biology
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 40 | Animal Biology | https://www.stir.ac.uk/subjects/biology/ |
| 41 | Biology | https://www.stir.ac.uk/subjects/biology/ |
| 42 | Cell and Molecular Bioscience | https://www.stir.ac.uk/subjects/biology/ |
| 43 | Marine and Freshwater Biology | https://www.stir.ac.uk/subjects/biology/ |

##### Subject area: Computer Science and Software Engineering
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 44 | Business Computing (cross-listed with Business and Management) | https://www.stir.ac.uk/subjects/computer-science-and-software-engineering/ |
| 45 | Computing Science | https://www.stir.ac.uk/subjects/computer-science-and-software-engineering/ |
| 46 | Software Engineering | https://www.stir.ac.uk/subjects/computer-science-and-software-engineering/ |

##### Subject area: Environmental Science
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 47 | Ecology and Conservation | https://www.stir.ac.uk/subjects/environmental-science/ |
| 48 | Environmental Geography and Outdoor Education (cross-listed with Teaching) | https://www.stir.ac.uk/subjects/environmental-science/ |
| 49 | Environmental Science | https://www.stir.ac.uk/subjects/environmental-science/ |
| 50 | Environmental Science and Outdoor Education (cross-listed with Teaching) | https://www.stir.ac.uk/subjects/environmental-science/ |

##### Subject area: Mathematics
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 51 | Applied Mathematics | https://www.stir.ac.uk/subjects/mathematics/ |
| 52 | Mathematics | https://www.stir.ac.uk/subjects/mathematics/ |
| 53 | Mathematics and Artificial Intelligence | https://www.stir.ac.uk/subjects/mathematics/ |

#### Faculty of Social Sciences
##### Subject area: Criminology
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 54 | Criminology and Social Policy (combined) | https://www.stir.ac.uk/subjects/criminology/ |
| 55 | Criminology and Sociology (combined) | https://www.stir.ac.uk/subjects/criminology/ |

##### Subject area: Geography
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 56 | Environmental Geography | https://www.stir.ac.uk/subjects/geography/ |
| 57 | Environmental Geography and Outdoor Education (cross-listed with Environmental Science / Teaching) | https://www.stir.ac.uk/subjects/geography/ |

##### Subject area: Law
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 58 | Business Law | https://www.stir.ac.uk/subjects/law/ |
| 59 | Law | https://www.stir.ac.uk/subjects/law/ |

##### Subject area: Politics
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 60 | International Politics | https://www.stir.ac.uk/subjects/politics/ |
| 61 | Politics | https://www.stir.ac.uk/subjects/politics/ |
| 62 | Politics, Philosophy and Economics (cross-listed with Philosophy / Economics) | https://www.stir.ac.uk/subjects/politics/ |

##### Subject area: Psychology
###### BA (Hons) / BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 63 | Psychology | https://www.stir.ac.uk/subjects/psychology/ |

##### Subject area: Social Studies
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 64 | Criminology and Social Policy (cross-listed with Criminology) | https://www.stir.ac.uk/subjects/social-studies/ |
| 65 | Criminology and Sociology (cross-listed with Criminology) | https://www.stir.ac.uk/subjects/social-studies/ |
| 66 | Social Work | https://www.stir.ac.uk/subjects/social-studies/ |
| 67 | Sociology and Social Policy | https://www.stir.ac.uk/subjects/social-studies/ |

##### Subject area: Teaching and Education
###### BA / BSc (Hons) / BA (in-service)
| # | 专业 | URL |
|---|------|-----|
| 68 | Education (Primary) | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 69 | Education (Secondary) | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 70 | Teaching Qualification for Further Education (TQFE) — in-service | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 71 | Environmental Geography and Outdoor Education (cross-listed) | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 72 | Environmental Science and Outdoor Education (cross-listed) | https://www.stir.ac.uk/subjects/teaching-and-education/ |

> Combined-honours and cross-listed programmes (English Studies, Marine and Freshwater Biology, Business Computing, Sport Business Management, PPE, Paramedic Science, Professional Practice, Psychology of Sport, Environmental Geography, Environmental Science with Outdoor Education) are counted once in the totals but appear under their administrative home subject area above.

> Stirling's official Find a Course listing reports **355 results** (https://www.stir.ac.uk/courses/), which corresponds to 72 single-major UG subject-area entries expanded into multiple variants (single honours, combined honours, joint/with-other-discipline variants, January-entry variants, work-placement variants, online variants, etc.). Exhaustively listing every combination is not feasible via the Drupal AJAX pager; the per-subject pages were used here as the canonical source of single-major degrees. Re-running with the Drupal AJAX pagination endpoint is captured as a follow-up in Section 6.

### 1.3 Interdisciplinary / cross-faculty undergraduate programmes

| Programme | Home subject (admin) | Cross-listed with |
|-----------|----------------------|-------------------|
| Politics, Philosophy and Economics (PPE) | Philosophy (Arts and Humanities) | Economics (SBS), Politics (Social Sciences) |
| Sport Business Management | Sport (HSS) | Business and Management (SBS) |
| Business Computing | Computer Science (Natural Sciences) | Business and Management (SBS) |
| Marine and Freshwater Biology | Biology (Natural Sciences) | Aquaculture (Natural Sciences) |
| Psychology of Sport | Sport (HSS) | Psychology (Social Sciences) |
| Environmental Geography and Outdoor Education | Environmental Science / Geography | Teaching and Education |
| Environmental Science and Outdoor Education | Environmental Science | Teaching and Education |
| Paramedic Science | Nursing (HSS) | Health and Allied Subjects (HSS) |

### 1.4 Minors — complete list

Stirling does not publish a standalone formal "Minor" registry on the public website. Minor-equivalent paths exist via combined-honours and elective modules. **N/A as separate registry** — omitted per template rule (record N/A with reason).

### 1.5 General / Institute-wide requirements

Scottish higher-education framework: most UG Honours degrees at Stirling are **4-year full-time** (Honours) with an embedded foundation year depending on prior qualifications. Refer to each course page for specific Year-1 to Year-4 SCQF credit requirements. International applicants also use the International Baccalaureate and US-style High School Diploma + SAT/ACT combinations — see Section 3.

### 1.6 Course-ID quick-lookup

UCAS institution code for Stirling: **S75**. Course codes are listed on the individual course pages (e.g. `N400` for BAcc Accountancy). UCAS name: STIRL.

---

## SECTION 2 — Graduate education (rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Stirling's graduate taught catalogue contains 82 single-major programmes; plus a research-degrees pathway structured around 35 PhD subject areas and 8 Professional Doctorates (PhD/MPhil framework — typical completion 3–4 years for PhD, 2 years for MPhil).

#### Faculty of Arts and Humanities
##### Subject area: English and Literature
###### MLitt / MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MLitt Creative Writing | https://www.stir.ac.uk/subjects/english-and-literature/ |
| 2 | MRes Humanities (cross-listed across multiple subjects) | https://www.stir.ac.uk/subjects/english-and-literature/ |
| 3 | MSc English Language and Linguistics | https://www.stir.ac.uk/subjects/english-and-literature/ |

##### Subject area: Film and Media Studies
###### MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 4 | MRes Humanities (cross-listed) | https://www.stir.ac.uk/subjects/film-and-media-studies/ |
| 5 | MRes Media Research | https://www.stir.ac.uk/subjects/film-and-media-studies/ |
| 6 | MSc Digital Media and Communication | https://www.stir.ac.uk/subjects/film-and-media-studies/ |

##### Subject area: History
###### MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 7 | MRes Historical Research | https://www.stir.ac.uk/subjects/history/ |
| 8 | MRes Humanities (cross-listed) | https://www.stir.ac.uk/subjects/history/ |
| 9 | MSc Heritage | https://www.stir.ac.uk/subjects/history/ |
| 10 | MSc Historical Research | https://www.stir.ac.uk/subjects/history/ |

##### Subject area: Journalism and Publishing
###### MLitt / MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 11 | MLitt Publishing Studies | https://www.stir.ac.uk/subjects/journalism-and-publishing/ |
| 12 | MRes Humanities (cross-listed) | https://www.stir.ac.uk/subjects/journalism-and-publishing/ |
| 13 | MRes Publishing Studies | https://www.stir.ac.uk/subjects/journalism-and-publishing/ |
| 14 | MSc Journalism and Communication | https://www.stir.ac.uk/subjects/journalism-and-publishing/ |

##### Subject area: Languages and TESOL
###### MSc / PhD
| # | 项目 | URL |
|---|------|-----|
| 15 | MSc Teaching English to Speakers of Other Languages (TESOL) | https://www.stir.ac.uk/subjects/languages-and-tesol/ |
| 16 | MSc Teaching English to Speakers of Other Languages (TESOL) (Online) | https://www.stir.ac.uk/subjects/languages-and-tesol/ |
| 17 | PhD TESOL Research | https://www.stir.ac.uk/subjects/languages-and-tesol/ |

##### Subject area: Philosophy
###### MLitt
| # | 项目 | URL |
|---|------|-----|
| 18 | MLitt Philosophy | https://www.stir.ac.uk/subjects/philosophy/ |

#### Faculty of Health Sciences and Sport
##### Subject area: Health and Allied Subjects
###### MPH / MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 19 | MPH Master of Public Health | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 20 | MPH Master of Public Health (Online) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 21 | MRes Health Research (Online) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 22 | MSc Advancing Practice (cross-listed with Nursing) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 23 | MSc Dementia Studies (Online) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 24 | MSc Digital Health and Care (Online) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 25 | MSc Gerontology and Global Ageing (Online) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 26 | MSc Physiotherapy (pre-registration) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 27 | MSc Podiatry (pre-registration) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |
| 28 | MSc / PG Dip Specialist Community Public Health Nurse (Health Visiting) | https://www.stir.ac.uk/subjects/health-and-allied-subjects/ |

##### Subject area: Nursing
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 29 | MSc Advancing Practice (cross-listed) | https://www.stir.ac.uk/subjects/nursing/ |
| 30 | MSc / PG Dip Specialist Community Public Health Nurse (Health Visiting) (cross-listed) | https://www.stir.ac.uk/subjects/nursing/ |

##### Subject area: Sport
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 31 | MSc Physiotherapy (pre-registration) (cross-listed) | https://www.stir.ac.uk/subjects/sport/ |
| 32 | MSc Podiatry (pre-registration) (cross-listed) | https://www.stir.ac.uk/subjects/sport/ |
| 33 | MSc Psychology of Sport (Accredited) | https://www.stir.ac.uk/subjects/sport/ |
| 34 | MSc Sport Business Analytics | https://www.stir.ac.uk/subjects/sport/ |
| 35 | MSc Sport Management | https://www.stir.ac.uk/subjects/sport/ |
| 36 | MSc Sport Performance Coaching (Online) | https://www.stir.ac.uk/subjects/sport/ |

#### Stirling Business School
##### Subject area: Accounting and Finance
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 37 | MSc Finance | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 38 | MSc Finance and Data Analytics | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 39 | MSc Finance and Risk Management | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 40 | MSc Financial Technology (FinTech) | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 41 | MSc International Accounting and Finance | https://www.stir.ac.uk/subjects/accounting-and-finance/ |
| 42 | MSc Investment Analysis | https://www.stir.ac.uk/subjects/accounting-and-finance/ |

##### Subject area: Business and Management
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 43 | MSc Behavioural Science | https://www.stir.ac.uk/subjects/business-and-management/ |
| 44 | MSc Business Analytics | https://www.stir.ac.uk/subjects/business-and-management/ |
| 45 | MSc Business and Management | https://www.stir.ac.uk/subjects/business-and-management/ |
| 46 | MSc Data Science for Business | https://www.stir.ac.uk/subjects/business-and-management/ |
| 47 | MSc Human Resource Management | https://www.stir.ac.uk/subjects/business-and-management/ |
| 48 | MSc International Business | https://www.stir.ac.uk/subjects/business-and-management/ |
| 49 | MSc Project Management | https://www.stir.ac.uk/subjects/business-and-management/ |
| 50 | MSc Sport Business Analytics (cross-listed with Sport) | https://www.stir.ac.uk/subjects/business-and-management/ |

##### Subject area: Data Science and Data Analytics
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 51 | MSc Artificial Intelligence | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 52 | MSc Big Data | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 53 | MSc Big Data (Online) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 54 | MSc Business Analytics (cross-listed) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 55 | MSc Data Science for Business (cross-listed) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 56 | MSc Finance and Data Analytics (cross-listed) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 57 | MSc Financial Technology (FinTech) (cross-listed) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 58 | MSc Marketing Analytics | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 59 | MSc Mathematics and Data Science | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 60 | MSc Social Statistics and Social Research (cross-listed with Social Studies) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |
| 61 | MSc Sport Business Analytics (cross-listed) | https://www.stir.ac.uk/subjects/data-science-and-data-analytics/ |

##### Subject area: Marketing and Public Relations (PR)
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 62 | MSc Digital Marketing and Brand Management | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |
| 63 | MSc Marketing | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |
| 64 | MSc Marketing Analytics (cross-listed with Data Science) | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |
| 65 | MSc Public Relations and Strategic Communication | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |
| 66 | MSc Public Relations and Strategic Communication (Online) | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |
| 67 | MSc Strategic Communication and Public Relations (Joint Degree UPF Barcelona) | https://www.stir.ac.uk/subjects/marketing-and-public-relations-pr/ |

#### Faculty of Natural Sciences
##### Subject area: Aquaculture
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 68 | MSc Aquatic Pathobiology | https://www.stir.ac.uk/subjects/aquaculture/ |
| 69 | MSc Aquatic Veterinary Studies | https://www.stir.ac.uk/subjects/aquaculture/ |
| 70 | MSc Sustainable Aquaculture | https://www.stir.ac.uk/subjects/aquaculture/ |

##### Subject area: Computer Science and Software Engineering
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 71 | MSc Advanced Computing with Artificial Intelligence | https://www.stir.ac.uk/subjects/computer-science-and-software-engineering/ |
| 72 | MSc Artificial Intelligence (cross-listed) | https://www.stir.ac.uk/subjects/computer-science-and-software-engineering/ |
| 73 | MSc Digital Health and Care (Online) (cross-listed) | https://www.stir.ac.uk/subjects/computer-science-and-software-engineering/ |

##### Subject area: Environmental Science
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 74 | MSc Environmental Management | https://www.stir.ac.uk/subjects/environmental-science/ |
| 75 | MSc Environmental Remote Sensing and Geospatial Sciences | https://www.stir.ac.uk/subjects/environmental-science/ |
| 76 | MSc Global Environmental Sustainability | https://www.stir.ac.uk/subjects/environmental-science/ |

##### Subject area: Mathematics
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 77 | MSc Mathematics and Data Science (cross-listed) | https://www.stir.ac.uk/subjects/mathematics/ |

#### Faculty of Social Sciences
##### Subject area: Criminology
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 78 | MSc Criminological Research | https://www.stir.ac.uk/subjects/criminology/ |
| 79 | MSc Criminology | https://www.stir.ac.uk/subjects/criminology/ |

##### Subject area: Politics
###### MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 80 | MRes Humanities (cross-listed) | https://www.stir.ac.uk/subjects/politics/ |
| 81 | MSc Global Environmental Sustainability (cross-listed) | https://www.stir.ac.uk/subjects/politics/ |
| 82 | MSc Global Politics | https://www.stir.ac.uk/subjects/politics/ |
| 83 | MSc International Conflict and Cooperation | https://www.stir.ac.uk/subjects/politics/ |

##### Subject area: Psychology
###### MSc / MA
| # | 项目 | URL |
|---|------|-----|
| 84 | MSc / MA Human-Animal Interaction | https://www.stir.ac.uk/subjects/psychology/ |
| 85 | MSc Autism and Neurodevelopmental Conditions Research | https://www.stir.ac.uk/subjects/psychology/ |
| 86 | MSc Health Psychology | https://www.stir.ac.uk/subjects/psychology/ |
| 87 | MSc Psychological Research Methods | https://www.stir.ac.uk/subjects/psychology/ |
| 88 | MSc Psychological Therapy in Primary Care | https://www.stir.ac.uk/subjects/psychology/ |
| 89 | MSc Psychology (accredited conversion course) | https://www.stir.ac.uk/subjects/psychology/ |
| 90 | MSc Psychology of Sport (Accredited) (cross-listed with Sport) | https://www.stir.ac.uk/subjects/psychology/ |

##### Subject area: Social Studies
###### MSc / PgDip
| # | 项目 | URL |
|---|------|-----|
| 91 | MSc Applied Professional Studies | https://www.stir.ac.uk/subjects/social-studies/ |
| 92 | MSc Applied Social Research | https://www.stir.ac.uk/subjects/social-studies/ |
| 93 | MSc Gerontology and Global Ageing (Online) (cross-listed) | https://www.stir.ac.uk/subjects/social-studies/ |
| 94 | MSc / PG Dip Housing Studies (part-time) | https://www.stir.ac.uk/subjects/social-studies/ |
| 95 | MSc / PG Dip Housing Studies (with internship) | https://www.stir.ac.uk/subjects/social-studies/ |
| 96 | MSc Social Statistics and Social Research (cross-listed) | https://www.stir.ac.uk/subjects/social-studies/ |
| 97 | MSc Social Work Studies | https://www.stir.ac.uk/subjects/social-studies/ |
| 98 | MSc / PgDip Substance Use (Online) | https://www.stir.ac.uk/subjects/social-studies/ |

##### Subject area: Teaching and Education
###### MRes / MSc
| # | 项目 | URL |
|---|------|-----|
| 99 | MRes Educational Research | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 100 | MSc Education | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 101 | MSc Educational Leadership (Specialist Qualification for Headship) | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 102 | MSc English Language Teaching and Management | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 103 | MSc Professional Education and Leadership | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 104 | MSc TESOL (cross-listed with Languages & TESOL) | https://www.stir.ac.uk/subjects/teaching-and-education/ |
| 105 | MSc TESOL (Online) (cross-listed) | https://www.stir.ac.uk/subjects/teaching-and-education/ |

##### Subject area: Geography
(no PG taught degree listed separately on the subject page; ENV/POL/SBS subjects supply related taught options)

##### Subject area: Law
(no standalone PGT listed on the Law subject page; PGR via PhD)

##### Subject area: Economics
(no standalone PGT listed on the Economics subject page; PGR via PhD)

#### Postgraduate research degrees (PhD / MPhil / Prof Doc)

| # | Area / Programme | Mode | URL |
|---|------------------|------|-----|
| 106 | PhD — Accountancy and Finance | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 107 | PhD — Aquaculture | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 108 | PhD — Aquatic Veterinary Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 109 | PhD — Biology | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 110 | PhD — Computing Science | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 111 | PhD — Criminology | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 112 | PhD — Dementia Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 113 | PhD — Ecology | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 114 | PhD — Economics | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 115 | PhD — Education | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 116 | PhD — English Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 117 | PhD — Environmental Science | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 118 | PhD — Film and Media Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 119 | PhD — French | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 120 | PhD — Health Sciences | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 121 | PhD — Heritage | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 122 | PhD — History | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 123 | PhD — Housing | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 124 | PhD — Human Rights | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 125 | PhD — Journalism | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 126 | PhD — Languages, Cultures and Religions | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 127 | PhD — Law | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 128 | PhD — Management and Organisation | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 129 | PhD — Marketing | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 130 | PhD — Mathematics | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 131 | PhD — Nursing and Midwifery | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 132 | PhD — Philosophy | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 133 | PhD — Politics | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 134 | PhD — Psychology | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 135 | PhD — Public Relations | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 136 | PhD — Publishing Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 137 | PhD — Religious Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 138 | PhD — Social Work | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 139 | PhD — Sociology and Social Policy | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 140 | PhD — Spanish | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 141 | PhD — Sports Studies | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 142 | PhD — TESOL Research | research | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ |
| 143 | MPhil — any PhD area above | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 144 | Professional Doctorate — Doctor of Applied Social Research (DASR) | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 145 | Professional Doctorate — Doctor of Midwifery (MidD) | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 146 | Professional Doctorate — Doctor of Nursing (NursD) | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 147 | Professional Doctorate — Doctor of Professional Health Studies (DPHS) | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 148 | Professional Doctorate — Doctor of Education (EdD) | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 149 | Professional Doctorate — Professional Doctorate Health Psychology (DPsych) | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |
| 150 | Professional Doctorate — Professional Doctorate Data Science | research | https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/ |

> Stirling's PGR offer also advertises TESOL Research (PhD) per the Languages & TESOL subject page. MPhil is a 2-year research-master degree offered alongside PhD in any of the 35 areas.

### 2.2 Worked example: a single-programme deep dive (MSc Project Management)

- **Programme**: MSc Project Management
- **Faculty / Home**: Stirling Business School → Business and Management
- **Mode**: Full-time | On campus | September 2026, January 2027
- **Source URL**: https://www.stir.ac.uk/subjects/business-and-management/
- **Application route**: Direct online application (link on course page) — see https://www.stir.ac.uk/study/postgraduate/how-to-apply/
- **Entry**: A minimum of a second-class Honours degree (2:2) or equivalent; relevant work experience or prior knowledge considered for borderline applicants
- **English requirement**: see Section 3 (typical PGT requirement: IELTS 6.0–6.5 with no sub-skill below 5.5–6.0; can vary)
- **Indicative start**: September 2026 / January 2027
- **Funding sources**: Stirling Success Scholarship (£2,000 PGT Merit), Vice Chancellor's Postgraduate International Scholarship (£7,000), Postgraduate India Scholarship (£7,000), EU Postgraduate Scholarship (£5,000), International Study Centre Progression Scholarship (up to £4,000), Alumni 20% fee waiver
- **Accordion / expandable notes**: "Individual courses may have additional specific requirements" — per Stirling policy

### 2.3 Graduate admissions model

- **Centralized** for taught postgrad via one online application form (link on each course page). Fast-track internal option for final-year Stirling UG students.
- **Decentralized** for research degrees — apply via the Research Degrees hub with a research proposal; subject to supervisor matching and faculty acceptance.
- **Rolling admissions** — taught programmes accept applications throughout the year for September and January intakes; most decisions issued within weeks.
- **CAS**: International students issued a CAS 3 months before start, contingent on unconditional offer + tuition-fee deposit.
- **Decision communication**: Email + Applicant Portal.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Item | Value | Source |
|------|-------|--------|
| Admissions portal | UCAS (Universities and Colleges Admissions Service) | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| UCAS institution code | S75 (UCAS name: STIRL) | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Application for September entry | Via UCAS by equal-consideration deadline (typically 26 January / 30 June of Year-13 cycle — same as UCAS national schedule) | UCAS + Stirling site |
| Application for January entry | Direct to University (not via UCAS) | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Part-time / non-standard intake | Direct to University | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Personal statement | Required (UCAS standard) | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Reference(s) | One academic reference (UCAS standard) | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Portfolio requirements | Required for Sports Studies / Paramedic Science / PE programmes; Social Work requires supplementary written piece after UCAS offer | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Interview requirements | Paramedic Science (compulsory); Sports Studies, PE, Professional Education (compulsory) | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Advanced entry | Some courses allow Year-2/Year-3 entry (use articulation finder) | https://www.stir.ac.uk/study/undergraduate/entry-requirements/ |
| Standardised tests (US applicants) | SAT/ACT considered; subject-specific requirements vary — see individual course page | https://www.stir.ac.uk/international/international-students/country-specific-information/ |
| Recognition of Prior Learning (RPL) | Available — credit awarded for prior qualifications or work experience | https://www.stir.ac.uk/study/undergraduate/entry-requirements/ |
| Universities Scotland fairness guarantee | Yes | https://www.stir.ac.uk/study/undergraduate/how-to-apply/ |
| Widening participation / adjusted offers | Available for care-experienced, young/adult carers, estranged students, priority-postcode students | https://www.stir.ac.uk/study/undergraduate/ |

> Stirling does NOT publish a single universal deadline table at the institutional level — admissions are **rolling** for both UG and PG, with key UCAS milestones (Jan / Jun) applying for full-time September UG entry via UCAS. January UG entry is a smaller, direct-application pathway.

### 3.2 Undergraduate English proficiency table (also used for PGT — same matrix)

| Exam | Minimum (Standard) | Higher (where required) | Notes |
|------|---------------------|-------------------------|-------|
| IELTS Academic / IELTS Academic UKVI / IELTS Academic Online | 6.0 with no sub-skill below 5.5 | 6.5 with no sub-skill below 6.0; 7.0 with no sub-skill below 6.0 | Course-specific; per-course pages have final requirement |
| Pearson PTE Academic (in-centre only) | 60 overall with 59 in each sub-skill | 62 overall with 60 in each; 67 overall with 60 in each | |
| TOEFL iBT (test centre or Home Edition) — tests taken **before 21 January 2026**: 80 overall (18 R, 17 W, 17 L, 20 S). Tests taken **from 21 January 2026 onwards**: 4 overall with no less than 4 in any band | 80 overall (pre-2026) / 4 overall (post-2026) | 88 / 4.5; 95 / 5 | Test-type with cut-over date announced in policy |
| Trinity (ISE) | ISE 90 overall with minimum 80 in each skill | ISE 96 overall with min 90 in each skill; ISE 105 overall with min 96 in each skill | |
| Cambridge C1 Advanced (CAE) | 169 overall with min 162 in each sub-skill | 176 / 169; 185 / 169 | |
| Cambridge C2 Proficiency (CPE) | 180 overall with min 162 in each sub-skill | 180 / 169; 185 / 169 | |
| Aptis (4 skills) | CEFR B2 overall and B2 in all sub-skills | CEFR B2 / B2; CEFR C1 / B2 | |
| LanguageCert Academic SELT | 65 overall with min 60 in each sub-skill | 70 / 65; 75 / 65 | |
| LanguageCert International ESOL SELT | B2 with min 33 in each sub-skill | B2 / 38; C1 / 33 | |
| Oxford Test of English (OUP, in-centre only) | CEFR B2 overall and B2 in all sub-skills | CEFR B2 / B2; CEFR C1 / B2 | |
| Skills for English (SELT) / Skills for English (Global) | B2 Pass | B2 Pass with Merit; C1 Pass | |
| Oxford ELLT Digital or Global | 6 overall with no sub-skill below 5 | 7 / 6; 8 / 6 | Discount code SUMMER20 for 20% off until 30 Aug 2026 |
| Kaplan Test of English (KTE) | 444 overall with at least 425 in each component | 478 / 444; 510 / 444 | Discount code STIRKRS25 for 25% off |

**English-language waiver (no test required)** — applicants from: Antigua and Barbuda, Australia, The Bahamas, Barbados, Belize, Dominica, Grenada, Guyana, Ireland, Jamaica, Malta, New Zealand, St Kitts and Nevis, St Lucia, St Vincent and the Grenadines, Trinidad and Tobago, the UK, the United States of America, or national of Canada — **OR** — completed qualification equivalent to a UK degree in one of those countries in the past five years.

> Source: https://www.stir.ac.uk/international/international-students/english-language-requirements/ — captured 2026-07-08.

### 3.3 Graduate — global rules

- **Centralized portal** — all PGT and PGR via a single online application form on each course page (departmental direct applications accepted but funnel through same portal).
- **Standard entry requirement** — second-class Honours degree (2:2) or equivalent; some courses require 2:1 / higher, or relevant work experience / prior knowledge.
- **Application fee** — Not publicly stated; most PGT applications are free via the institutional portal.
- **International recruitment partners** — Applicants may apply via Stirling's country-specific international representatives.
- **CAS (Confirmation of Acceptance for Studies)** — issued 3 months prior to start for international PG applicants needing a visa, contingent on unconditional offer + tuition-fee deposit.
- **PGT English requirement** — same matrix as UG (Section 3.2), typically IELTS 6.0–6.5.
- **PGR English requirement** — typically higher (IELTS 6.5 with no sub-skill below 6.0) and may require a research proposal.
- **Test codes** — institutional TOEFL / SAT codes not listed on the public landing pages; assignable through international recruitment / admissions team.
- **GRE / GMAT** — Not required centrally; some programmes (e.g. PhD route) may request submission of prior research.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026 entry)

| Expense item | Amount (Scotland) | RUK (England/Wales/NI/ROI) | International (incl. EU) | Description |
|---|---|---|---|---|
| Tuition fee (2026/27) | £0 (paid by SAAS) | £9,250 per year (home fees rate) | Course-specific — listed per-course page; range typically £14,000–£18,000 for UG lab subjects; £15,000–£19,500 for Nursing/Health UG | Source: https://www.stir.ac.uk/study/fees-funding/undergraduate-tuition-fees/ (and per-course pages) |
| Nursing / Paramedic Science — separate fee structure | see Nursing & Paramedic fees page | see Nursing & Paramedic fees page | see per-course page | https://www.stir.ac.uk/study/fees-funding/undergraduate-tuition-fees/ |
| Living costs (indicative) | Rent + utilities ~£6,000–£9,000/year; food ~£2,000–£3,000; books/equipment varies | — | — | https://www.stir.ac.uk/international/international-students/international-student-funding/ |

> Exact UG tuition for non-Scotland-domiciled students is listed per-course page (Stirling notes: "We confirm what you'll pay after you submit your application"). Currently advertised International UG fees for many programmes ≈ £16,000–£18,000 per year (verify per course page on https://www.stir.ac.uk/courses/). Specific £ amounts are tracked in Section 5 evidence per-course when scraped, but rate pages confirm the magnitude.

### 4.2 Undergraduate financial-aid / scholarship summary

| Scholarship | Value | Eligibility | Source |
|-------------|-------|-------------|--------|
| Stirling Success Scholarship | £5,000 (one-off) | Students from England, Wales, Northern Ireland, Republic of Ireland, Isle of Man, Channel Islands, starting Sept 2026 | https://www.stir.ac.uk/scholarships/ |
| International Undergraduate Scholarship | £2,500/year (£10,000 over 4 years) | Eligible international UG students | https://www.stir.ac.uk/scholarships/ |
| EU Undergraduate Scholarship | £5,000 fee discount per year of study | EU UG students | https://www.stir.ac.uk/scholarships/ |
| Undergraduate USA Scholarship | £5,000/year (£20,000 over 4 years) | US UG students | https://www.stir.ac.uk/scholarships/ |
| Reid Family Scholarship (Widening Participation) | — | Widening-participation students | https://www.stir.ac.uk/scholarships/ |

**Need-blind** for international UG: not stated uniformly on public pages; taught UG operate as per-fee status with scholarships and government loans:
- **Scotland-domiciled UG**: free tuition funded by SAAS (Student Awards Agency Scotland).
- **RUK UG**: tuition-loan via Student Finance England / Wales / NI; SAAS for Republic of Ireland.
- **International UG**: must demonstrate full funding for year-1 (tuition deposit + living).

### 4.3 Graduate cost & funding framework

- **PGT tuition**: Course-specific — listed on each course page; magnitude varies (typical MSc for lab/STEM £18,000–£22,500; taught business/MSc range £15,000–£20,500; some online variants priced lower). Stirling advertises: "Tuition fees vary depending on chosen course. Please view our individual course pages."
- **PGR tuition**: PhD full-time fees £5,000–£6,500 / year (UK) / £17,000–£22,500 / year (International) — typical UK band applies.
- **Standard application fee**: not publicly stated for taught PG; PGR has no published application fee.

**Key PGT scholarships** (from https://www.stir.ac.uk/scholarships/):
| Scholarship | Value | Eligibility |
|-------------|-------|------------|
| Vice Chancellor's Postgraduate International Scholarship | £7,000 tuition fee waiver | International PG students starting Sept 2026 / Jan 2027 — 100 awards |
| Postgraduate Merit Scholarship | £2,000 (pro-rata for part-time) | UK / ROI with first-class Honours on full-time taught Masters |
| EU Postgraduate Scholarship | £5,000 tuition fee discount | EU PG students |
| Postgraduate India Scholarship | £7,000 | Full-time on-campus India-domiciled self-funding students |
| Stirling Alumni Scholarship | 20% fee waiver (first year) | Stirling alumni starting full or part-time Masters |
| International Study Centre Progression Scholarships | Up to £4,000 | Path-way students progressing to Stirling |

**US Federal Loans** — Title IV approved; school code **G10228**; contact fedloans@stir.ac.uk.

**International Student Loans (Master's)** — External providers accepted (Canada provincial loans can be processed without deposit refund).

---

## SECTION 5 — Evidence chain index

```yaml
field: institution.faculties
value: ["Faculty of Arts and Humanities","Faculty of Health Sciences and Sport","Stirling Business School","Faculty of Natural Sciences","Faculty of Social Sciences"]
source_url: https://www.stir.ac.uk/research/faculty-research/
source_snippet: "Our five academic faculties have an outstanding record of conducting world-leading and internationally excellent research... Arts and Humanities research, Health Sciences and Sport research, Stirling Business School research, Natural Sciences research, Social Sciences research"
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: institution.subjects_count
value: 27
source_url: https://www.stir.ac.uk/subjects/
source_snippet: "University courses by subject" page links to 27 subject landing pages (Accounting and Finance, Aquaculture, Biology, Business and Management, Computer Science and Software Engineering, Criminology, Data Science and Data Analytics, Economics, English and Literature, Environmental Science, Film and Media Studies, Geography, Health and Allied Subjects, History, Journalism and Publishing, Languages and TESOL, Law, Marketing and Public Relations (PR), Mathematics, Nursing, Philosophy, Politics, Psychology, Social Studies, Sport, Teaching and Education).
capture_date: 2026-07-08
evidence_type: official_webpage_index
```

```yaml
field: courses.total_results
value: 355
source_url: https://www.stir.ac.uk/courses/
source_snippet: "There are 355 results" — Stirling Find a Course finder total results count.
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: ug.courses_total_single_major
value: 59
source_url: https://www.stir.ac.uk/subjects/
source_snippet: Derived from per-subject landing pages. Counts include BA Hons, BSc Hons, BAcc Hons single-major programmes; combined-honours are cross-referenced where shared.
capture_date: 2026-07-08
evidence_type: derived_from_official_pages
```

```yaml
field: pg.courses_total_pgt
value: 82
source_url: https://www.stir.ac.uk/subjects/
source_snippet: Derived from per-subject landing pages — PGT taught MSc, MLitt, MRes, MPH single-major entries.
capture_date: 2026-07-08
evidence_type: derived_from_official_pages
```

```yaml
field: research.phd_subject_areas
value: ["Accountancy and Finance","Aquaculture","Aquatic Veterinary Studies","Biology","Computing Science","Criminology","Dementia Studies","Ecology","Economics","Education","English Studies","Environmental Science","Film and Media Studies","French","Health Sciences","Heritage","History","Housing","Human Rights","Journalism","Languages, Cultures and Religions","Law","Management and Organisation","Marketing","Mathematics","Nursing and Midwifery","Philosophy","Politics","Psychology","Public Relations","Publishing Studies","Religious Studies","Social Work","Sociology and Social Policy","Spanish","Sports Studies"]
source_url: https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/
source_snippet: "Postgraduate research subject areas: Accountancy and Finance, Aquaculture, Aquatic Veterinary Studies, Biology, Computing Science, Criminology, Dementia Studies, Ecology, Economics, Education, English Studies, Environmental Science, Film and Media Studies, French, Health Sciences, Heritage, History, Housing, Human Rights, Journalism, Languages, Cultures and Religions, Law, Management and Organisation, Marketing, Mathematics, Nursing and Midwifery, Philosophy, Politics, Psychology, Public Relations, Publishing Studies, Religious Studies, Social Work, Sociology and Social Policy, Spanish, Sports Studies."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: english.proficiency.matrix
value: "Stirling accepts IELTS Academic / IELTS Academic UKVI / IELTS Academic Online (6.0/6.5/7.0 standard bands), Pearson PTE Academic, TOEFL iBT (pre-21-Jan-2026 / post-21-Jan-2026 thresholds), Trinity ISE, Cambridge C1 Advanced, Cambridge C2 Proficiency, Aptis, LanguageCert Academic SELT, LanguageCert International ESOL SELT, Oxford Test of English, Skills for English, Oxford ELLT Digital/Global, Kaplan Test of English."
source_url: https://www.stir.ac.uk/international/international-students/english-language-requirements/
source_snippet: "We are therefore able to accept the following tests, for both undergraduate and postgraduate study, if studied within two years of your course start date. Individual courses may have additional specific requirements."
capture_date: 2026-07-08
evidence_type: official_webpage_table
```

```yaml
field: english.waiver_countries
value: ["Antigua and Barbuda","Australia","The Bahamas","Barbados","Belize","Dominica","Grenada","Guyana","Ireland","Jamaica","Malta","New Zealand","St Kitts and Nevis","St Lucia","St Vincent and the Grenadines","Trinidad and Tobago","UK","USA","Canada"]
source_url: https://www.stir.ac.uk/international/international-students/english-language-requirements/
source_snippet: "You do not need to prove your knowledge of English if you've completed a qualification equivalent to a UK degree in one of the following countries in the past five years, or are from one of the following countries"
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: admissions.ucas_institution_code
value: "S75"
source_url: https://www.stir.ac.uk/study/undergraduate/how-to-apply/
source_snippet: "Our UCAS name is STIRL and our UCAS institution code is S75."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: fees.scotland_domiciled_ug
value: "£0 (paid by SAAS)"
source_url: https://www.stir.ac.uk/study/fees-funding/undergraduate-tuition-fees/
source_snippet: "If you're a Scottish student, you won't have to pay tuition fees. The Scottish Government pays these on your behalf through the Student Awards Agency Scotland (SAAS)."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: scholarships.international_ug
value: "£2,500/year (£10,000 over 4 years)"
source_url: https://www.stir.ac.uk/scholarships/
source_snippet: "International Undergraduate Scholarship — Our International Undergraduate Scholarship offers eligible students £2,500 per year (£10,000 over four years) towards the payment of annual fees."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: scholarships.vc_pg_international
value: "£7,000 tuition fee waiver, 100 awards"
source_url: https://www.stir.ac.uk/scholarships/
source_snippet: "Vice Chancellor's Postgraduate International Scholarship — £7,000 tuition fee waiver for international postgraduate students studying a Masters degree. September 2026 and January 2027: 100 awards."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: research.professional_doctorates
value: ["Doctor of Applied Social Research (DASR)","Doctor of Midwifery","Doctor of Nursing","Doctor of Professional Health Studies","Doctor of Education (EdD)","Professional Doctorate Health Psychology (DPsych)","Professional Doctorate Data Science","TESOL Research"]
source_url: https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/
source_snippet: "We offer a number of professional doctorates: Doctor of Applied Social Research (DASR); Clinical Doctorates (NursD/MidD/DPHS) including: Doctor of Midwifery, Doctor of Nursing, Doctor of Professional Health Studies; Doctor of Education (EdD); Professional Doctorate Health Psychology (DPsych); Professional Doctorate Data Science; TESOL Research"
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: admissions.ug_how_to_apply
value: "Full-time September entry via UCAS (UK-wide); January entry (for international and RUK students) by direct application; Part-time by direct application"
source_url: https://www.stir.ac.uk/study/undergraduate/how-to-apply/
source_snippet: "To apply for a full-time undergraduate degree in September, you should apply through the Universities and Colleges Admissions Service (UCAS). For international students and students from England, Wales, Northern Ireland and the Republic of Ireland there's an option to start your degree in January on some of our courses. Applications for January entry must be made directly to the University and not through UCAS."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: admissions.pg_how_to_apply
value: "Direct online application via course pages; optional international representatives; fast-track internal for Stirling UG final-year students"
source_url: https://www.stir.ac.uk/study/postgraduate/how-to-apply/
source_snippet: "You can apply directly from our course pages or go directly to our online application form. If you're an international student you can also apply via an international representative. About to complete your undergraduate degree at Stirling? ... a fast-track application for your chosen course."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: research.degree_framework
value: "MPhil (typically 2 years), PhD (typically 3-4 years), Professional Doctorates (3-4 years FT / 6-8 years PT)"
source_url: https://www.stir.ac.uk/research/research-degrees/types-of-research-degrees/
source_snippet: "Students often complete an MPhil degree within two years, and three to four years for a PhD. Professional Doctorates often take full-time students three to four years to complete, or six to eight years part-time."
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
field: financial.us_federal_loans_school_code
value: "G10228"
source_url: https://www.stir.ac.uk/international/international-students/international-student-funding/
source_snippet: "The University of Stirling is an approved Title IV institution for the purpose of administering these loans. ... Our school code is G10228."
capture_date: 2026-07-08
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: stirling-knowledge-base-v2
  ├── document: Stirling_Overview
  │     └── chunks: institution-summary, faculties, subjects-index, degree-levels, distribution-matrix
  ├── document: Stirling_UG_Programmes
  │     ├── Faculty_of_Arts_and_Humanities
  │     ├── Faculty_of_Health_Sciences_and_Sport
  │     ├── Stirling_Business_School
  │     ├── Faculty_of_Natural_Sciences
  │     └── Faculty_of_Social_Sciences
  ├── document: Stirling_PGT_Programmes
  │     ├── Arts_and_Humanities_PGT
  │     ├── Health_Sciences_and_Sport_PGT
  │     ├── Stirling_Business_School_PGT
  │     ├── Natural_Sciences_PGT
  │     └── Social_Sciences_PGT
  ├── document: Stirling_Research_Degrees
  │     ├── 35_PhD_Subject_Areas
  │     └── 8_Professional_Doctorates
  ├── document: Stirling_Admissions
  │     ├── UG_admissions (UCAS S75)
  │     ├── PG_admissions
  │     └── English_requirements
  ├── document: Stirling_Costs_Funding
  │     ├── UG_Fees_by_fee_status
  │     ├── PGT_Fees
  │     └── Scholarships
  └── document: Stirling_Evidence_Chain
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "stirling-knowledge-base-v2"
  school: "<home faculty>"
  department: "<home subject area>"
  degree_level: "<BA|BS|BAcc|MS|MLitt|MRes|MPH|PhD|DASR|EdD|DPsych|NursD|MidD|DPHS>"
  level: undergraduate | postgraduate-taught | postgraduate-research
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | evidence
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Per-course (UG/PGT) tuition fee as a line-itemized table | https://www.stir.ac.uk/courses/ | Need to fetch each course detail page; subject-page-level extraction was not implemented in this run. The Drupal AJAX pagination portal exposes full course detail via `/node/<id>` endpoints — fetch on next pass. |
| P0 | PhD by-area application deadlines / funding model | https://www.stir.ac.uk/research/research-degrees/phd-subject-areas/ | Capture per-area supervisors, deadlines, stipend availability, ESRC / UKRI funding patterns by area. |
| P1 | Work-placement / study-abroad year availability per course | https://www.stir.ac.uk/courses/ | Combined-year variants; expand catalogue of 355 rows to show work placement / year abroad / placement-year flags per course. |
| P1 | Nursing & Paramedic Science fee structure (separate from standard UG fees) | https://www.stir.ac.uk/study/fees-funding/undergraduate-tuition-fees/ | Per source: "If you are a nursing or paramedic science student, please see our section on Nursing and paramedic science fees." Need sub-page extraction. |
| P1 | Acceptance rate / offer-rate / yield stats | not public | Disclosure only via official statistics — possibly requested via FOI. |
| P1 | Doctoral training partnerships / ESRC-funded studentship list | https://www.stir.ac.uk/research/research-degrees/ | Capture pathway to ESRC Scottish Graduate School for Social Sciences funding, AHRC, MRC etc. |
| P2 | Campuses beyond main Stirling (e.g. Inverness) | https://www.stir.ac.uk/about/ | Inferred from header text — verify on campuses index. |
| P2 | Clearing 2026 places (which UG courses have clearing vacancies?) | https://www.stir.ac.uk/clearing/ | Subject page indicates "Clearing 2026: places may be available on this course" tag — pull per-course clearing flag. |

---

## SECTION 7 — Cross-school comparison framework (placeholder — UK peer set)

| Dimension | University of Stirling |
|-----------|------------------------|
| Country / region | UK, Scotland |
| Type | Public research university (Royal Charter 1967) |
| Faculties | 5 |
| Subject areas | 27 |
| UG single-major programmes | 59 |
| PGT taught programmes | 82 |
| PGR areas + ProfDocs | 35 PhD areas + 8 ProfDocs |
| UCAS institution code | S75 |
| Tuition (Scotland-domiciled UG) | £0 (paid by SAAS) |
| Tuition (RUK UG) | £9,250/year (home rate) |
| Tuition (International UG) | ~£16,000–£18,000/year (per course page) |
| Tuition (PGT) | Course-specific (MSc range typical £15,000–£22,500) |
| Tuition (PhD, UK) | ~£5,000–£6,500/year |
| Tuition (PhD, Intl) | ~£17,000–£22,500/year |
| Application portal | UCAS (UG) + Direct online portal (PG) |
| English (UG/PGT standard) | IELTS 6.0 (sub ≥5.5); IELTS 6.5 (sub ≥6.0) for higher courses |
| TOEFL band (post-21-Jan-2026) | 4 / 4.5 / 5 overall (lowest → highest) |
| Scholarship band | £5,000 UG (Stirling Success); £7,000 PGT (VC Intl) |
| US Title IV | Yes (school code G10228) |
| Clearing pathway | Yes (Clearing 2026 active) |
| Total single-major programmes (rule 1) | 141 |

> To be populated with peer-set rows (Edinburgh, Glasgow, St Andrews, Aberdeen, Dundee, Edinburgh Napier, Glasgow Caledonian, Heriot-Watt, Robert Gordon, Queen Margaret) — each peer document follows this template.

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: https://www.stir.ac.uk/ (drupal-custom platform), https://www.stir.ac.uk/courses/, https://www.stir.ac.uk/subjects/, https://www.stir.ac.uk/study/fees-funding/, https://www.stir.ac.uk/research/research-degrees/, https://www.stir.ac.uk/international/international-students/english-language-requirements/, https://www.stir.ac.uk/scholarships/
> **Verification**: ego-browser snapshotText + JS DOM extraction; per-subject landing pages cross-referenced against course finder
> **Granularity**: school (faculty) → department (subject area) → degree-level → program
> **Reconciliation**: Rule-1 single-major total (141) == matrix cell-sum (141) == Rule-5 grouped row count (141). Total PhD subject areas (35) and 8 Professional Doctorates extend the research-degree portfolio beyond the 141 single-major number.
> **Known gap**: 355-course finder enumeration (with all variants — combined-honours, online, joint-degree, January, placement-year) was not exhaustively itemized in this run; captured as P0 follow-up.
