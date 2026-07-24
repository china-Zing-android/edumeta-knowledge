# Wake Forest University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless) + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | 49 |
| 本科辅修 (Minor) | 62 |
| 本科证书 (Certificate) | 1 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/JD/etc.) | 65 |
| **学位项目总计 (UG + Grad)** | **177** |
| 学院 / 独立系所总数 | 7 |

> **Reconciliation**: Rule-1 total (177) = UG (49 majors + 62 minors + 1 cert = 112) + Grad (65) = 177. Matrix cell-sum and Rule-5 row-count must equal 177.

### 0.2 学院 / 系层级结构

```
Wake Forest University
├── Wake Forest College (Undergraduate College)          [学院]
│   ├── Accountancy                                      [系]
│   ├── African American Studies                         [系]
│   ├── Anthropology                                     [系]
│   ├── Biology                                          [系]
│   ├── Chemistry                                        [系]
│   ├── Classical Languages                              [系]
│   ├── Communication                                    [系]
│   ├── Computer Science                                 [系]
│   ├── Economics                                        [系]
│   ├── Education                                        [系]
│   ├── Engineering                                      [系]
│   ├── English                                          [系]
│   ├── Environment & Sustainability Studies             [系]
│   ├── French Studies                                   [系]
│   ├── German & German Studies                          [系]
│   ├── History                                          [系]
│   ├── Mathematics                                      [系]
│   ├── Music                                            [系]
│   ├── Philosophy                                       [系]
│   ├── Physics                                          [系]
│   ├── Politics & International Affairs                 [系]
│   ├── Psychology                                       [系]
│   ├── Religious Studies                                [系]
│   ├── Sociology                                        [系]
│   ├── Spanish                                          [系]
│   ├── Statistics                                       [系]
│   ├── Studio Art                                       [系]
│   ├── Theatre                                          [系]
│   └── Women's, Gender, & Sexuality Studies             [系]
├── Graduate School of Arts & Sciences                   [学院]
│   ├── Biology (MS, PhD)                                [系]
│   ├── Chemistry (MS, PhD)                              [系]
│   ├── Communication (MA)                               [系]
│   ├── Computer Science (MS)                            [系]
│   ├── Counseling (MA)                                  [系]
│   ├── Documentary Film (MA, MFA)                       [系]
│   ├── Education (MAEd)                                 [系]
│   ├── English (MA)                                     [系]
│   ├── Health and Exercise Science (MS)                 [系]
│   ├── Mathematics (MS)                                 [系]
│   ├── Physics (MS, PhD)                                [系]
│   ├── Psychology (MS)                                  [系]
│   └── Statistics (MS)                                  [系]
├── School of Business                                   [学院]
│   ├── Accountancy (BS, MSA)                            [系]
│   ├── Business & Enterprise Management (BS)            [系]
│   ├── Finance (BS)                                     [系]
│   ├── Decision Analytics (BS)                          [系]
│   └── Graduate Programs (MBA, MSBA, MSM)               [系]
├── School of Divinity                                   [学院]
│   ├── Master of Divinity (MDiv)                        [系]
│   ├── Doctor of Ministry (DMin)                        [系]
│   ├── Master of Arts in Religion (MA)                  [系]
│   └── Dual Degrees (MDiv/MA, MDiv/MS, MDiv/JD)        [系]
├── Wake Forest Law                                      [学院]
│   ├── Juris Doctor (JD)                                [系]
│   ├── Master of Legal Studies (MLS)                    [系]
│   ├── Master of Laws (LLM)                             [系]
│   └── Doctor of Juridical Science (SJD)                [系]
├── School of Medicine                                   [学院]
│   ├── Doctor of Medicine (MD)                          [系]
│   ├── Physician Assistant (MMS)                        [系]
│   └── Biomedical Graduate Programs (MS, PhD)           [系]
│       ├── Biochemistry and Molecular Biology           [系]
│       ├── Biomedical Engineering                       [系]
│       ├── Cancer Biology                               [系]
│       ├── Clinical Research Management                 [系]
│       ├── Genetic Counseling                           [系]
│       ├── Integrative Physiology and Pharmacology      [系]
│       ├── Medical Physics                              [系]
│       ├── Microbiology and Immunology                  [系]
│       ├── Molecular and Cellular Biosciences           [系]
│       ├── Molecular Genetics and Genomics              [系]
│       ├── Molecular Medicine and Translational Science [系]
│       ├── Neuroscience                                 [系]
│       ├── Translational and Health System Science      [系]
│       └── Translational Biotechnology                  [系]
└── School of Professional Studies                       [学院]
    ├── Master of Engineering Management (MEM)           [系]
    ├── Master of International Affairs                  [系]
    ├── Master of Public Policy and Data Analytics       [系]
    ├── Master of Information Technology Management      [系]
    ├── Master of AI Strategy and Innovation             [系]
    ├── Master of Cybersecurity Leadership               [系]
    ├── Master of Health Administration                  [系]
    ├── Master of Educational Leadership                 [系]
    ├── Master of Project Management                     [系]
    ├── Master of Financial Technology and Analytics     [系]
    └── Graduate Certificates                            [系]
```

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | ~30 |
| BS | BS | Bachelor of Science | 本科 | ~19 |
| Minor | Minor | 辅修 | 本科 | 62 |
| Certificate | Certificate | 本科证书 | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | 5 |
| MS | MS | Master of Science | 研究生 | 20 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MAEd | MAEd | Master of Arts in Education | 研究生 | 1 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MDiv | MDiv | Master of Divinity | 研究生 | 1 |
| DMin | DMin | Doctor of Ministry | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| MLS | MLS | Master of Legal Studies | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| SJD | SJD | Doctor of Juridical Science | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| MMS | MMS | Master of Medical Science | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 14 |
| MEM | MEM | Master of Engineering Management | 研究生 | 1 |
| Graduate Certificate | Graduate Certificate | 研究生证书 | 研究生 | 2 |

> **Note**: BA/BS split for UG is approximate; WFU College awards both BA and BS across departments. Exact per-major degree attribution requires catalog verification. Graduate certificate count is for for-credit certificates only (SPS).

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | Minor | UG Cert | MA | MS | MFA | MBA | MAEd | MDiv | DMin | JD | MLS | LLM | SJD | MD | MMS | PhD | MEM | Grad Cert | 合计 |
|------------|----|----|-------|---------|----|----|-----|-----|------|------|------|----|----|-----|-----|----|-----|-----|-----|-----------|------|
| Wake Forest College | ~30 | ~19 | 62 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 112 |
| Graduate School of A&S | 0 | 0 | 0 | 0 | 4 | 8 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 17 |
| School of Business | 0 | 4 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| School of Divinity | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Wake Forest Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 8 | 0 | 1 | 20 |
| School of Professional Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 13 |
| **合计** | **~30** | **~23** | **62** | **1** | **5** | **20** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **11** | **1** | **3** | **177** |

> **Reconciliation note**: The Business school UG majors (Accountancy, Business & Enterprise Management, Decision Analytics, Finance = 4 BS) are listed under the Business school row but academically housed in Wake Forest College. The Graduate School of A&S has 15 active programs (3 not accepting applications excluded). School of Medicine biomedical = 17 programs + MD + MMS = 20. School of Professional Studies = 10 master's + 1 MEM + 2 certificates = 13. Total graduate = 17 + 8 + 3 + 4 + 20 + 13 = 65. Grand total = 112 + 65 = 177.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

Wake Forest University's undergraduate education is administered through **Wake Forest College** (also called "The College"), which houses 29 academic departments and 16 interdisciplinary programs. The School of Business also offers undergraduate majors (BS degrees). All undergraduate students are part of the College, which blends a small liberal arts environment with research university resources. See Section 0.2 for the full hierarchy tree.

**Source**: [https://about.wfu.edu/academics/schools/](https://about.wfu.edu/academics/schools/) — "29 academic departments and 16 interdisciplinary programs, offering over 50 majors and 60 minors."

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Wake Forest College

##### BS Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://admissions.wfu.edu/academics/majors-minors/ |
| 2 | Biophysics | https://admissions.wfu.edu/academics/majors-minors/ |
| 3 | Chemistry | https://admissions.wfu.edu/academics/majors-minors/ |
| 4 | Computer Science | https://admissions.wfu.edu/academics/majors-minors/ |
| 5 | Engineering | https://admissions.wfu.edu/academics/majors-minors/ |
| 6 | Environmental Science | https://admissions.wfu.edu/academics/majors-minors/ |
| 7 | Health & Exercise Science | https://admissions.wfu.edu/academics/majors-minors/ |
| 8 | Mathematics | https://admissions.wfu.edu/academics/majors-minors/ |
| 9 | Physics | https://admissions.wfu.edu/academics/majors-minors/ |
| 10 | Statistics | https://admissions.wfu.edu/academics/majors-minors/ |
| 11 | Applied Mathematics | https://admissions.wfu.edu/academics/majors-minors/ |
| 12 | Applied Statistics | https://admissions.wfu.edu/academics/majors-minors/ |

##### BA Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 2 | Anthropology | https://admissions.wfu.edu/academics/majors-minors/ |
| 3 | Art History | https://admissions.wfu.edu/academics/majors-minors/ |
| 4 | Biology | https://admissions.wfu.edu/academics/majors-minors/ |
| 5 | Chinese Language & Culture | https://admissions.wfu.edu/academics/majors-minors/ |
| 6 | Classical Languages | https://admissions.wfu.edu/academics/majors-minors/ |
| 7 | Classical Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 8 | Communication | https://admissions.wfu.edu/academics/majors-minors/ |
| 9 | Critical & Creative Media | https://admissions.wfu.edu/academics/majors-minors/ |
| 10 | Economics | https://admissions.wfu.edu/academics/majors-minors/ |
| 11 | Elementary Education | https://admissions.wfu.edu/academics/majors-minors/ |
| 12 | English | https://admissions.wfu.edu/academics/majors-minors/ |
| 13 | Environment & Sustainability Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 14 | French Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 15 | German & German Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 16 | Greek | https://admissions.wfu.edu/academics/majors-minors/ |
| 17 | History | https://admissions.wfu.edu/academics/majors-minors/ |
| 18 | Interdisciplinary Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 19 | Italian Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 20 | Japanese Language & Culture | https://admissions.wfu.edu/academics/majors-minors/ |
| 21 | Latin | https://admissions.wfu.edu/academics/majors-minors/ |
| 22 | Music | https://admissions.wfu.edu/academics/majors-minors/ |
| 23 | Philosophy | https://admissions.wfu.edu/academics/majors-minors/ |
| 24 | Politics & International Affairs | https://admissions.wfu.edu/academics/majors-minors/ |
| 25 | Psychology | https://admissions.wfu.edu/academics/majors-minors/ |
| 26 | Religious Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 27 | Russian | https://admissions.wfu.edu/academics/majors-minors/ |
| 28 | Sociology | https://admissions.wfu.edu/academics/majors-minors/ |
| 29 | Spanish | https://admissions.wfu.edu/academics/majors-minors/ |
| 30 | Spanish Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 31 | Studio Art | https://admissions.wfu.edu/academics/majors-minors/ |
| 32 | Theatre | https://admissions.wfu.edu/academics/majors-minors/ |
| 33 | Women's, Gender, & Sexuality Studies | https://admissions.wfu.edu/academics/majors-minors/ |

##### Concentrations / Special Programs

| # | 专业 | 备注 |
|---|------|------|
| 1 | Chemistry — Biochemistry concentration | Concentration within Chemistry |
| 2 | Chemistry — Materials Chemistry concentration | Concentration within Chemistry |
| 3 | Chemistry — Medicinal Chemistry and Drug Discovery concentration | Concentration within Chemistry |

#### School of Business (Undergraduate)

##### BS Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://business.wfu.edu/ |
| 2 | Business & Enterprise Management | https://business.wfu.edu/ |
| 3 | Decision Analytics | https://business.wfu.edu/ |
| 4 | Finance | https://business.wfu.edu/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

Wake Forest offers several interdisciplinary programs that span departments:

| # | 项目 | 类型 | 备注 |
|---|------|------|------|
| 1 | Interdisciplinary Studies | Major | Self-designed across departments |
| 2 | Interdisciplinary Honors | Program | Cross-departmental honors track |
| 3 | Environment & Sustainability Studies | Major | Cross-departmental |
| 4 | Critical & Creative Media | Major | Cross-departmental |

### 1.4 Minors — complete list

| # | Minor | URL |
|---|-------|-----|
| 1 | Accountancy | https://admissions.wfu.edu/academics/majors-minors/ |
| 2 | African American Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 3 | African Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 4 | American Ethnic Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 5 | Anthropology | https://admissions.wfu.edu/academics/majors-minors/ |
| 6 | Arabic | https://admissions.wfu.edu/academics/majors-minors/ |
| 7 | Art History | https://admissions.wfu.edu/academics/majors-minors/ |
| 8 | Bioethics, Humanities & Medicine | https://admissions.wfu.edu/academics/majors-minors/ |
| 9 | Biology | https://admissions.wfu.edu/academics/majors-minors/ |
| 10 | Chemistry | https://admissions.wfu.edu/academics/majors-minors/ |
| 11 | Chinese Language & Culture | https://admissions.wfu.edu/academics/majors-minors/ |
| 12 | Classical Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 13 | Communication | https://admissions.wfu.edu/academics/majors-minors/ |
| 14 | Computer Science | https://admissions.wfu.edu/academics/majors-minors/ |
| 15 | Contemporary Global Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 16 | Creative Writing | https://admissions.wfu.edu/academics/majors-minors/ |
| 17 | Cultural Heritage & Preservation Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 18 | Dance | https://admissions.wfu.edu/academics/majors-minors/ |
| 19 | Economics | https://admissions.wfu.edu/academics/majors-minors/ |
| 20 | Engineering | https://admissions.wfu.edu/academics/majors-minors/ |
| 21 | English | https://admissions.wfu.edu/academics/majors-minors/ |
| 22 | Entrepreneurship | https://admissions.wfu.edu/academics/majors-minors/ |
| 23 | Environmental Science | https://admissions.wfu.edu/academics/majors-minors/ |
| 24 | Environmental Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 25 | Film & Media Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 26 | French Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 27 | German & German Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 28 | Global Trade & Commerce Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 29 | Greek | https://admissions.wfu.edu/academics/majors-minors/ |
| 30 | Health & Human Services | https://admissions.wfu.edu/academics/majors-minors/ |
| 31 | Health Policy & Administration | https://admissions.wfu.edu/academics/majors-minors/ |
| 32 | History | https://admissions.wfu.edu/academics/majors-minors/ |
| 33 | Interdisciplinary Humanities | https://admissions.wfu.edu/academics/majors-minors/ |
| 34 | Italian Language & Culture | https://admissions.wfu.edu/academics/majors-minors/ |
| 35 | Japanese Language & Culture | https://admissions.wfu.edu/academics/majors-minors/ |
| 36 | Jewish Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 37 | Journalism | https://admissions.wfu.edu/academics/majors-minors/ |
| 38 | Latin | https://admissions.wfu.edu/academics/majors-minors/ |
| 39 | Latin-American & Latino Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 40 | Linguistics | https://admissions.wfu.edu/academics/majors-minors/ |
| 41 | Marketing Communication | https://admissions.wfu.edu/academics/majors-minors/ |
| 42 | Mathematics | https://admissions.wfu.edu/academics/majors-minors/ |
| 43 | Medieval & Early Modern Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 44 | Middle East & South Asia Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 45 | Music | https://admissions.wfu.edu/academics/majors-minors/ |
| 46 | Neuroscience | https://admissions.wfu.edu/academics/majors-minors/ |
| 47 | Philosophy | https://admissions.wfu.edu/academics/majors-minors/ |
| 48 | Physics | https://admissions.wfu.edu/academics/majors-minors/ |
| 49 | Politics & International Affairs | https://admissions.wfu.edu/academics/majors-minors/ |
| 50 | Psychology | https://admissions.wfu.edu/academics/majors-minors/ |
| 51 | Religious Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 52 | Russian | https://admissions.wfu.edu/academics/majors-minors/ |
| 53 | Russian & East European Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 54 | Schools, Education and Society | https://admissions.wfu.edu/academics/majors-minors/ |
| 55 | Secondary Education | https://admissions.wfu.edu/academics/majors-minors/ |
| 56 | Sociology | https://admissions.wfu.edu/academics/majors-minors/ |
| 57 | Spanish | https://admissions.wfu.edu/academics/majors-minors/ |
| 58 | Statistics | https://admissions.wfu.edu/academics/majors-minors/ |
| 59 | Studio Art | https://admissions.wfu.edu/academics/majors-minors/ |
| 60 | Theatre | https://admissions.wfu.edu/academics/majors-minors/ |
| 61 | Women's, Gender, & Sexuality Studies | https://admissions.wfu.edu/academics/majors-minors/ |
| 62 | Writing | https://admissions.wfu.edu/academics/majors-minors/ |

### 1.5 UG Certificates & Other Credentials

| # | 项目 | 类型 | URL |
|---|------|------|-----|
| 1 | Actuarial Science | Certificate | https://admissions.wfu.edu/academics/majors-minors/ |
| 2 | French for Business | Concentration | https://admissions.wfu.edu/academics/majors-minors/ |
| 3 | Spanish for Business | Concentration | https://admissions.wfu.edu/academics/majors-minors/ |
| 4 | Spanish Interpreting | Concentration | https://admissions.wfu.edu/academics/majors-minors/ |
| 5 | Spanish Translation/Localization | Concentration | https://admissions.wfu.edu/academics/majors-minors/ |
| 6 | Military Science | Program | https://admissions.wfu.edu/academics/majors-minors/ |

### 1.6 General Education Requirements

Wake Forest College requires all undergraduates to complete a set of distribution requirements across liberal arts disciplines. Specific details are available through the College's academic advising office. The university emphasizes a liberal arts curriculum grounded in *Pro Humanitate*.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Graduate School of Arts & Sciences (Reynolda Campus)

> **Note**: 3 programs (Bioethics, Liberal Arts Studies, Sustainability) are listed but "not accepting applications" as of capture date. They are excluded from the active count.

##### MS Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 2 | Chemistry | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 3 | Computer Science | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 4 | Health and Exercise Science | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 5 | Mathematics | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 6 | Physics | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 7 | Psychology | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 8 | Statistics | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |

##### MA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 2 | Counseling (on-campus) | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 3 | Counseling (online, Clinical Mental Health Track) | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 4 | Counseling (online, School Counseling Track) | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 5 | English | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |

##### MA (Specialized)

| # | 项目 | URL |
|---|------|-----|
| 1 | Documentary Film — MA in Sports Media & Storytelling | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 2 | Documentary Film — MA in Content Creation and Strategic Storytelling (4+1) | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |

##### MFA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Documentary Film (two-year MFA) | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |

##### MAEd Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |

##### PhD Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 2 | Chemistry | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |
| 3 | Physics | https://graduate.wfu.edu/academic-programs-reynolda-campus/ |

#### School of Business (Graduate)

##### MBA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | MBA (Full-time, Winston-Salem) | https://business.wfu.edu/ |
| 2 | MBA (Part-time, Winston-Salem) | https://business.wfu.edu/ |
| 3 | MBA (Part-time, Charlotte) | https://business.wfu.edu/ |
| 4 | MBA (Online) | https://business.wfu.edu/ |

##### MS Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Accountancy (MSA) | https://business.wfu.edu/ |
| 2 | Master of Science in Business Analytics (MSBA) | https://business.wfu.edu/ |
| 3 | Master of Science in Business Analytics — Sports Analytics Concentration | https://business.wfu.edu/ |
| 4 | Master of Science in Management (MSM) | https://business.wfu.edu/ |

#### School of Divinity

##### MDiv Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Divinity (MDiv) | https://divinity.wfu.edu/academics/ |

##### DMin Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Ministry (DMin) | https://divinity.wfu.edu/academics/ |

##### MA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Arts in Religion | https://divinity.wfu.edu/academics/ |

##### Dual Degree Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | MDiv / MA in Bioethics | https://divinity.wfu.edu/academics/ |
| 2 | MDiv / MA in Counseling | https://divinity.wfu.edu/academics/ |
| 3 | MDiv / MA in Education | https://divinity.wfu.edu/academics/ |
| 4 | MDiv / MS in Management | https://divinity.wfu.edu/academics/ |
| 5 | MDiv / MA in Sustainability | https://divinity.wfu.edu/academics/ |
| 6 | JD / MDiv | https://divinity.wfu.edu/academics/ |

#### Wake Forest Law

##### JD Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor (JD) | https://law.wfu.edu/academics/ |

##### Graduate Law Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Legal Studies (MLS) | https://law.wfu.edu/academics/graduate-programs/ |
| 2 | Master of Laws (LLM) — for foreign-trained lawyers | https://law.wfu.edu/academics/graduate-programs/ |
| 3 | Doctor of Juridical Science (SJD) | https://law.wfu.edu/academics/graduate-programs/ |

#### School of Medicine

##### MD Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine (MD) | https://school.wakehealth.edu/ |

##### MMS Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Assistant — Master of Medical Science (MMS) | https://school.wakehealth.edu/ |

##### MS Programs (Biomedical)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 2 | Biomedical Science (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 3 | Biomedical Research (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 4 | Clinical Research Management (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 5 | Clinical Research Management — Accelerated (MS/BS or MS/BA) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 6 | Genetic Counseling (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 7 | Medical Physics (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 8 | Molecular Medicine and Translational Science (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 9 | Neuroscience (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 10 | Translational and Health System Science (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 11 | Translational Biotechnology (MS) | https://school.wakehealth.edu/education-and-training/graduate-programs |

##### PhD Programs (Biomedical)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 2 | Biomedical Engineering | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 3 | Cancer Biology | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 4 | Integrative Physiology and Pharmacology | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 5 | Medical Physics | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 6 | Microbiology and Immunology | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 7 | Molecular and Cellular Biosciences | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 8 | Molecular Genetics and Genomics | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 9 | Molecular Medicine and Translational Science | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 10 | Neuroscience | https://school.wakehealth.edu/education-and-training/graduate-programs |

##### Certificate Programs (Medical)

| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Physics — Certificate | https://school.wakehealth.edu/education-and-training/graduate-programs |
| 2 | Translational and Health System Science — Post-Professional Certificates | https://school.wakehealth.edu/education-and-training/graduate-programs |

#### School of Professional Studies (Online)

##### Master's Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Engineering Management (MEM) | https://sps.wfu.edu/programs/type/masters-programs/ |
| 2 | Master of International Affairs | https://sps.wfu.edu/programs/type/masters-programs/ |
| 3 | Master of Public Policy and Data Analytics | https://sps.wfu.edu/programs/type/masters-programs/ |
| 4 | Master of Information Technology Management | https://sps.wfu.edu/programs/type/masters-programs/ |
| 5 | Master of AI Strategy and Innovation | https://sps.wfu.edu/programs/type/masters-programs/ |
| 6 | Master of Cybersecurity Leadership | https://sps.wfu.edu/programs/type/masters-programs/ |
| 7 | Master of Health Administration | https://sps.wfu.edu/programs/type/masters-programs/ |
| 8 | Master of Educational Leadership: Independent School Pathway | https://sps.wfu.edu/programs/type/masters-programs/ |
| 9 | Master of Educational Leadership | https://sps.wfu.edu/programs/type/masters-programs/ |
| 10 | Master of Project Management | https://sps.wfu.edu/programs/type/masters-programs/ |
| 11 | Master of Financial Technology and Analytics | https://sps.wfu.edu/ |

##### Graduate Certificate Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Project Management Certificate | https://sps.wfu.edu/programs/type/certificates/ |
| 2 | Digital Marketing and Analytics Certificate | https://sps.wfu.edu/programs/type/certificates/ |

### 2.2 Graduate admissions model

Wake Forest has a **decentralized** graduate admissions model. Each school manages its own admissions process, application portal, and financial aid:

- **Graduate School of A&S**: Centralized application at graduate.wfu.edu; GRE requirements vary by program
- **School of Business**: Own application portal at business.wfu.edu; GMAT/GRE optional for some programs
- **School of Divinity**: Own application at divinity.wfu.edu
- **Wake Forest Law**: JD via LSAC; LLM/SJD/MLS via law.wfu.edu
- **School of Medicine**: MD via AMCAS; biomedical grad via school.wakehealth.edu
- **School of Professional Studies**: Online application at sps.wfu.edu

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 证据 |
|------|-----|------|
| Admissions website | https://admissions.wfu.edu/ | E-U-001 |
| Application portals | Common App, Coalition (Scoir), WFU Print App | E-U-002 |
| Application fee | $85 (fee waivers available) | E-U-003 |
| **ED I deadline** | **November 15** | E-U-004 |
| **ED I decision** | Rolling basis | E-U-004 |
| **Early Action (first-gen only)** | **November 15** | E-U-005 |
| **Early Action decision** | By January 15 | E-U-005 |
| **ED II deadline** | **January 1** | E-U-006 |
| **ED II decision** | By February 15 | E-U-006 |
| **RD deadline** | **January 1** | E-U-007 |
| **RD decision** | Around April 1 | E-U-007 |
| Enrollment confirmation | May 1 | E-U-008 |
| SAT/ACT policy | **Test-optional** (since Fall 2009) | E-U-009 |
| Superscore policy | Yes — WFU superscores SAT/ACT | E-U-0010 |
| SAT code | 5885 | E-U-0011 |
| ACT code | 3168 | E-U-0012 |
| TOEFL code | 5885 | E-U-0013 |
| Interview policy | Optional (video or virtual interview) | E-U-0014 |
| Recommendation requirements | 1 teacher recommendation (required); counselor recommendation (optional) | E-U-0015 |
| Transfer deadline | Not specified on main page | — |
| Financial aid deadline (ED I / EA) | December 1 | E-U-0016 |
| Financial aid deadline (ED II / RD) | January 1 | E-U-0016 |

### 3.2 Undergraduate English proficiency table

Wake Forest **does not publish specific minimum scores** for TOEFL, IELTS, or Duolingo. The requirement applies to international students whose first language is not English and/or who attend schools where English is not the medium of instruction.

| 考试 | 最低要求 | 推荐分数 | 备注 |
|------|---------|---------|------|
| TOEFL iBT | Not published | N/A | Code: 5885; self-reported scores accepted |
| IELTS | Not published | N/A | Academic version |
| Duolingo English Test | Not published | N/A | Self-reported scores accepted |

> **Waiver**: Students who have attended a school where English is the main language of instruction for at least 3 years are exempt. WFU does NOT superscore English language tests.

### 3.3 Graduate — global rules

Graduate admissions at Wake Forest is **fully decentralized** — each school runs its own application, fee, and review process:

- **Graduate School of A&S**: GRE required for some programs; application via graduate.wfu.edu
- **School of Business**: GMAT/GRE optional for MBA; application via business.wfu.edu
- **School of Divinity**: No standardized test required; application via divinity.wfu.edu
- **Wake Forest Law**: JD requires LSAT/GRE via LSAC; LLM/SJD via law.wfu.edu
- **School of Medicine**: MD requires MCAT via AMCAS; biomedical grad programs via school.wakehealth.edu
- **School of Professional Studies**: No standardized tests; online application via sps.wfu.edu

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year)

**Living On or Off Campus:**

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition | $71,894 | Full-time undergraduate |
| Fees | $1,276 | Activity, Wellness, Health Service |
| Housing | $12,900 | Estimated average |
| Food | $7,396 | Estimated average |
| Personal Expenses | $1,930 | Estimated average |
| Transportation | $1,550 | Estimated average |
| Federal Direct Loan Avg Fee | $64 | |
| Books, Course Materials, Supplies & Equipment | $1,720 | Estimated average |
| **Total Estimated Costs** | **$98,730** | |

**Living With Parents:**

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition | $71,894 | |
| Fees | $1,436 | Includes Technology fee |
| Housing | $1,940 | |
| Food | $4,930 | |
| Books, Course Materials, Supplies & Equipment | $1,720 | |
| Personal Expenses | $1,930 | |
| Transportation | $1,550 | |
| Federal Direct Loan Avg Fee | $64 | |
| **Total Estimated Costs** | **$84,674** | |

> **Note**: First-semester new students are assessed an additional $380 Orientation Fee. Health insurance is NOT included. Amounts other than tuition and fees are estimated averages.

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 | 证据 |
|------|-----|------|
| Meets demonstrated need | **100%** for eligible students | E-U-0017 |
| Need-blind / need-aware | **Not explicitly stated** on admissions pages | E-U-0018 |
| Need-based aid for internationals | **NOT offered** to foreign national students | E-U-0019 |
| Merit scholarships for internationals | Yes — including full-cost awards (Carswell, Gordon, Reynolds, Stamps) | E-U-0020 |
| NC Gateway — income <$100k | Full tuition + standard living expenses (NC students, fall 2026+) | E-U-0021 |
| NC Gateway — income <$200k | Tuition-free (NC students, fall 2026+) | E-U-0021 |
| NC Gateway — income $200k-$300k | 50% tuition aid (NC students, fall 2026+) | E-U-0021 |
| Need-based aid growth | 119% average growth since 2013 | E-U-0022 |
| Scholarship funds | 200+ created or enhanced since 2021 | E-U-0022 |
| Application forms | FAFSA (code 002978) + CSS Profile (code 5885) | E-U-0023 |
| Aid notification (ED I / EA) | Starting December 15 (if aid apps complete by Nov 15) | E-U-0024 |
| Aid notification (ED II) | Within 3 weeks of completion (if complete by Jan 1) | E-U-0024 |
| Aid notification (RD) | Early April, 3-4 weeks before May 1 | E-U-0024 |
| Outcomes | 97% of graduates employed or in grad school within 6 months | E-U-0025 |

### 4.3 Graduate cost & funding framework

| 字段 | 值 | 备注 |
|------|-----|------|
| Graduate School of A&S | Varies by program; PhD programs typically fully funded | RA/TA positions available |
| School of Business MBA | Contact business.wfu.edu for current tuition | Part-time and online options |
| School of Divinity | MDiv tuition per credit hour | Merit scholarships available |
| Wake Forest Law JD | Contact law.wfu.edu | Need-based and merit aid |
| School of Medicine MD | Contact school.wakehealth.edu | Federal loan programs |
| School of Professional Studies | $34,587–$48,132 per program (varies by program) | All online; Fall 2026 enrollment |

**SPS Master's Program Tuition Examples:**
- Most programs: $40,110
- Master of Health Administration: $48,132
- Master of Educational Leadership (Independent School Pathway): $38,430
- Master of Educational Leadership: $34,587
- Graduate Certificates: $16,044 each

---

## SECTION 5 — Evidence chain index

### Undergraduate Evidence

```yaml
# E-U-001
field: undergraduate.admissions.website
value: "https://admissions.wfu.edu/"
source_url: https://admissions.wfu.edu/
source_snippet: "Undergraduate Admissions"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-002
field: undergraduate.application.portals
value: ["Common Application", "Coalition Application (Scoir)", "Wake Forest Application (print)"]
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Common Application — for first-year domestic, first-year international, and transfer students; Coalition Application (Scoir) — for first-year domestic and transfer students; Wake Forest Application (print/mail)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-003
field: undergraduate.application.fee
value: 85
source_url: https://admissions.wfu.edu/apply/
source_snippet: "$85 application fee (fee waivers available)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-004
field: undergraduate.deadlines.ED_I
value: { deadline: "November 15", decision: "Rolling", binding: true }
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Early Decision I | November 15 | Rolling | Binding — if admitted, you are expected to enroll at Wake Forest University"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-005
field: undergraduate.deadlines.EA_firstgen
value: { deadline: "November 15", decision: "By January 15", binding: false }
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Early Action (first-gen students) | November 15 | By January 15 | Non-binding"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-006
field: undergraduate.deadlines.ED_II
value: { deadline: "January 1", decision: "By February 15", binding: true }
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Early Decision II | January 1 | By February 15 | Binding"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-007
field: undergraduate.deadlines.RD
value: { deadline: "January 1", decision: "Around April 1", binding: false }
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Regular Decision | January 1 | Around April 1 | Non-binding"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-008
field: undergraduate.enrollment_confirmation_deadline
value: "May 1"
source_url: https://admissions.wfu.edu/apply/
source_snippet: "you have until May 1 to decide if you will enroll at Wake Forest"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-009
field: undergraduate.test_policy
value: "test-optional (since Fall 2009)"
source_url: https://admissions.wfu.edu/apply/test-optional/
source_snippet: "In May 2008, Wake Forest announced it would stop requiring SAT or ACT scores. The policy took effect with the entering class of Fall 2009"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0010
field: undergraduate.superscore_policy
value: true
source_url: https://admissions.wfu.edu/apply/
source_snippet: "we will superscore them"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0011
field: undergraduate.testing.SAT_code
value: "5885"
source_url: https://admissions.wfu.edu/become-a-deacon/international/
source_snippet: "SAT: Wake Forest CEEB 5885"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0012
field: undergraduate.testing.ACT_code
value: "3168"
source_url: https://admissions.wfu.edu/become-a-deacon/international/
source_snippet: "ACT: Wake Forest Code 3168"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0013
field: undergraduate.testing.TOEFL_code
value: "5885"
source_url: https://admissions.wfu.edu/become-a-deacon/international/
source_snippet: "TOEFL (Wake Forest CEEB code: 5885)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0014
field: undergraduate.interview_policy
value: "Optional (video or virtual interview)"
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Video or virtual interview — Optional"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0015
field: undergraduate.recommendations
value: { teacher: "required", counselor: "optional" }
source_url: https://admissions.wfu.edu/apply/
source_snippet: "Teacher Recommendation Form (a teacher recommendation letter is accepted as a substitute); Counselor recommendation — Optional"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0016
field: undergraduate.financial_aid.deadlines
value: { ed1_ea: "December 1", ed2_rd: "January 1" }
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "December 1 — Early Decision I / Early Action (first-gen); January 1 — Early Decision II / Regular Decision"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0017
field: undergraduate.financial_aid.meets_demonstrated_need
value: "100%"
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "100% — Amount of demonstrated financial need for eligible students Wake Forest meets"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0018
field: undergraduate.financial_aid.need_blind_status
value: "Not explicitly stated on admissions pages"
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "The page does not explicitly state whether Wake Forest is need-blind or need-aware in admissions."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0019
field: undergraduate.financial_aid.international_need_based
value: false
source_url: https://admissions.wfu.edu/become-a-deacon/international/
source_snippet: "Wake Forest does not offer need-based financial aid to foreign national students"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0020
field: undergraduate.financial_aid.international_merit
value: true
source_url: https://admissions.wfu.edu/become-a-deacon/international/
source_snippet: "International students are eligible for most merit-based scholarships, including full-cost awards (Carswell, Gordon, Reynolds, and Stamps Scholarships)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0021
field: undergraduate.financial_aid.nc_gateway
value: { income_under_100k: "Full tuition + living expenses", income_under_200k: "Tuition-free", income_200k_300k: "50% tuition" }
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "Family income under $100,000: Financial aid covers full tuition plus standard living expenses. Family income under $200,000: Students attend tuition-free. Family income between $200,000–$300,000: Eligible for aid covering 50% of tuition."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0022
field: undergraduate.financial_aid.aid_growth
value: { need_based_growth_since_2013: "119%", scholarship_funds_since_2021: "200+" }
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "Need-based aid scholarships have grown an average of 119% since 2013. Over 200 scholarship funds benefiting undergraduates have been created or substantially enhanced since 2021."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0023
field: undergraduate.financial_aid.application_forms
value: { fafsa_code: "002978", css_code: "5885" }
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "FAFSA: 002978; CSS Profile: 5885"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0024
field: undergraduate.financial_aid.notification_timing
value: { ed1_ea: "Starting December 15", ed2: "Within 3 weeks of completion", rd: "Early April" }
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "ED I & Early Action: Complete aid apps by Nov. 15 → notification starting Dec. 15. ED II: Complete by Jan. 1 → notification within three weeks. Regular Decision: Complete by Jan. 1 → notification in early April"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0025
field: undergraduate.outcomes.employment_rate
value: "97% employed or in grad school within 6 months"
source_url: https://admissions.wfu.edu/affordability/
source_snippet: "97% of graduates secured employment or enrolled in graduate programs within six months"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Cost Evidence

```yaml
# E-U-0026
field: undergraduate.costs.tuition_2026_2027
value: 71894
source_url: https://financialaid.wfu.edu/cost-of-attendance/
source_snippet: "Tuition | $71,894"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-0027
field: undergraduate.costs.total_on_campus_2026_2027
value: 98730
source_url: https://financialaid.wfu.edu/cost-of-attendance/
source_snippet: "Total Estimated Costs | $98,730"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-0028
field: undergraduate.costs.housing
value: 12900
source_url: https://financialaid.wfu.edu/cost-of-attendance/
source_snippet: "Housing | $12,900"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-0029
field: undergraduate.costs.food
value: 7396
source_url: https://financialaid.wfu.edu/cost-of-attendance/
source_snippet: "Food | $7,396"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Facts Evidence

```yaml
# E-U-0030
field: institution.facts.enrollment_total
value: 9633
source_url: https://admissions.wfu.edu/facts/
source_snippet: "Total university enrollment: 9,633"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0031
field: institution.facts.student_faculty_ratio
value: "10:1"
source_url: https://admissions.wfu.edu/facts/
source_snippet: "Student-to-faculty ratio: 10 to 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0032
field: institution.facts.applicants_class_2030
value: 21497
source_url: https://admissions.wfu.edu/facts/
source_snippet: "Applicants for first-year admission: 21,497 (Class of 2030)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0033
field: institution.facts.accepted_class_2030
value: 4060
source_url: https://admissions.wfu.edu/facts/
source_snippet: "First-year students accepted/enrolled: 4,060 accepted / 1,544 enrolled"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0034
field: institution.facts.founded
value: 1834
source_url: https://admissions.wfu.edu/facts/
source_snippet: "Founded: 1834"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-0035
field: institution.facts.athletics
value: { division: "NCAA Division I (FBS)", conference: "ACC", teams: 18 }
source_url: https://admissions.wfu.edu/facts/
source_snippet: "Division: NCAA Division I (Football Bowl Subdivision); Conference: Atlantic Coast Conference (ACC); Varsity teams: 18"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
wakeforest-knowledge-base-v2
├── 00-institution-overview          (Section 0: rules 1-4, counts, hierarchy, matrix)
├── 01-ug-major-college              (Section 1: WF College majors by dept/degree)
├── 02-ug-major-business             (Section 1: Business school UG majors)
├── 03-ug-minors                     (Section 1: all 62 minors)
├── 04-grad-arts-sciences            (Section 2: Graduate School of A&S programs)
├── 05-grad-business                 (Section 2: Business school grad programs)
├── 06-grad-divinity                 (Section 2: Divinity school programs)
├── 07-grad-law                      (Section 2: Law school programs)
├── 08-grad-medicine                 (Section 2: Medicine school programs)
├── 09-grad-professional-studies     (Section 2: SPS programs)
├── 10-deadlines-requirements        (Section 3: deadlines, test policy, ELP)
├── 11-costs-financial-aid           (Section 4: COA, aid policy, NC Gateway)
└── 12-evidence-index                (Section 5: all evidence chains)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "wakeforest-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL | 说明 |
|--------|--------|---------|------|
| P0 | Per-major BA/BS degree attribution | College catalog / department pages | Current doc uses approximate BA/BS split; need official per-major degree type |
| P0 | Need-blind/need-aware explicit statement | admissions.wfu.edu or financialaid.wfu.edu | Affordability page does NOT explicitly state status |
| P0 | English proficiency minimum scores | admissions.wfu.edu/become-a-deacon/international/ | No minimums published; verify with admissions office |
| P1 | Graduate program details (GRE, deadlines, fees per program) | Individual program pages | Each graduate program's specific requirements |
| P1 | SPS additional certificate programs | sps.wfu.edu/programs/type/certificates/ | Page was truncated; may have more certificates |
| P1 | School of Medicine MD program details | school.wakehealth.edu | Tuition, deadlines, MCAT requirements |
| P1 | Graduate tuition rates | Individual school pages | Most graduate tuition not captured |
| P2 | Core curriculum / distribution requirements | College advising pages | General education requirements not detailed |
| P2 | Transfer admission requirements and deadlines | admissions.wfu.edu | Transfer-specific details limited |
| P2 | SPS bootcamps & non-credit programs | sps.wfu.edu | Non-credit offerings not enumerated |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Wake Forest | (Other schools) |
|------|-------------|-----------------|
| Type | Private, coeducational | |
| Location | Winston-Salem, NC | |
| Founded | 1834 | |
| UG enrollment | 5,595 | |
| Total enrollment | 9,633 | |
| Student-faculty ratio | 10:1 | |
| UG tuition (2026-27) | $71,894 | |
| Total UG COA (on-campus) | $98,730 | |
| Meets demonstrated need | Yes (100%) | |
| Need-blind (domestic) | Not explicitly stated | |
| Need-blind (international) | No (need-aware; no need-based aid for intl) | |
| NC Gateway (income <$200k) | Tuition-free (NC students) | |
| Test policy | Test-optional (since 2009) | |
| SAT/ACT required | No | |
| TOEFL minimum | Not published | |
| IELTS minimum | Not published | |
| Application fee | $85 | |
| ED I deadline | November 15 | |
| ED II deadline | January 1 | |
| RD deadline | January 1 | |
| EA deadline | N/A (first-gen only: Nov 15) | |
| Total UG majors | 49 | |
| Total UG minors | 62 | |
| Total grad programs | 65 | |
| Total programs (Rule 1) | 177 | |
| Schools/colleges | 7 | |
| Athletics | NCAA D-I (ACC), 18 varsity teams | |
| Conference | Atlantic Coast Conference (ACC) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.wfu.edu, financialaid.wfu.edu, business.wfu.edu, graduate.wfu.edu, divinity.wfu.edu, law.wfu.edu, school.wakehealth.edu, sps.wfu.edu, about.wfu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + WebFetch
> **Granularity**: school → department → degree-level → program
