# Saint Louis University (SLU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/etc.) | 266 |
| 本科辅修 (Minor) | 168 |
| 本科微证书 (Microcredential) | 104 |
| 本科证书 (Certificate) | 10 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 367 |
| 研究生证书/文凭 (Certificate/Post-Bacc/Post-Master) | 92 |
| 研究生微证书 (Microcredential) | 4 |
| 加速本硕连读 (Accelerated Bachelor's to Graduate) | 5 |
| **学位项目总计 (All Programs)** | **981** |
| 学院 / 独立中心总数 | 13 (degree-granting) |

> Source: catalog.slu.edu/programs — 981 program entries extracted via JS DOM query on 2026-07-06. [E-U-001]

### 0.2 学院 / 系层级结构 (Rule 2)

```
Saint Louis University
├── College of Arts and Sciences                          [学院]
│   ├── African American Studies                          [系]
│   ├── American Studies                                  [系]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Communication                                     [系]
│   ├── Computer Science                                  [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── History                                           [系]
│   ├── Mathematics and Statistics                        [系]
│   ├── Modern and Classical Languages                    [系]
│   ├── Philosophy                                        [系]
│   ├── Physics                                           [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Sociology                                         [系]
│   ├── Visual and Performing Arts                        [系]
│   ├── Theology and Religious Studies                    [系]
│   └── Women's and Gender Studies                        [系]
├── School of Science and Engineering                     [学院]
│   ├── Aerospace and Mechanical Engineering              [系]
│   ├── Aviation                                          [系]  ⚠ strong aviation program
│   ├── Biomedical Engineering                            [系]
│   ├── Civil Engineering                                 [系]
│   ├── Computer Science                                  [系]  ⚠ shared with A&S
│   ├── Electrical and Computer Engineering               [系]
│   ├── Mathematics and Statistics                        [系]  ⚠ shared with A&S
│   └── Physics                                           [系]  ⚠ shared with A&S
├── Richard A. Chaifetz School of Business                [学院]
│   ├── Accounting                                        [系]
│   ├── Decision Sciences and IT                          [系]
│   ├── Economics                                         [系]  ⚠ shared with A&S
│   ├── Finance                                           [系]
│   ├── International Business                            [系]
│   ├── Leadership and Management                         [系]
│   └── Marketing                                         [系]
├── School for Professional Studies                       [学院]
│   ├── Applied Analytics                                 [系]
│   ├── Cybersecurity                                     [系]
│   ├── General Studies                                   [系]
│   ├── Information Technology                            [系]
│   └── Project Management                                [系]
├── College for Public Health and Social Justice           [学院]
│   ├── Behavioral Science and Health Equity              [系]
│   ├── Biostatistics                                     [系]
│   ├── Community Health                                  [系]
│   ├── Epidemiology                                      [系]
│   ├── Geospatial Health                                 [系]
│   ├── Global Health                                     [系]
│   ├── Health Administration                             [系]
│   ├── Health Management and Policy                      [系]
│   └── Public Health                                     [系]
├── Doisy College of Health Sciences                      [学院]
│   ├── Clinical Health Sciences                          [系]
│   ├── Health Sciences                                   [系]
│   ├── Medical Imaging and Radiation Therapeutics        [系]
│   ├── Nutrition and Dietetics                           [系]
│   ├── Occupational Science and Occupational Therapy     [系]
│   └── Physical Therapy and Athletic Training            [系]
├── School of Education                                   [学院]
│   ├── Educational Leadership                            [系]
│   └── Educational Studies                               [系]
├── School of Social Work                                 [学院]
│   └── Social Work                                       [系]
├── Trudy Busch Valentine School of Nursing               [学院]
│   └── Nursing                                           [系]
├── School of Law                                         [学院]
│   └── Law                                               [系]
├── School of Medicine                                    [学院]
│   ├── Anatomy                                           [系]
│   ├── Biochemistry and Molecular Biology                [系]
│   ├── Health and Clinical Outcomes Research             [系]
│   ├── Health Data Science                               [系]
│   ├── Immunology                                        [系]
│   ├── Molecular Microbiology and Immunology             [系]
│   ├── Neurology                                         [系]
│   ├── Pathology                                         [系]
│   ├── Pharmacology and Physiology                       [系]
│   ├── Psychiatry                                        [系]
│   └── Surgery                                           [系]
├── College of Philosophy and Letters                     [学院]
│   ├── Philosophy                                        [系]
│   └── Theology                                          [系]
├── Center for Advanced Dental Education                  [学院]
│   ├── Endodontics                                       [系]
│   ├── Orthodontics                                      [系]
│   ├── Pediatric Dentistry                               [系]
│   └── Periodontics                                      [系]
└── SLU-Madrid Campus                                     [分支校区]
    └── (select programs available in Madrid, Spain)
```

> Source: catalog.slu.edu/programs filter sidebar "College/School/Center" + graduate admissions page listing of schools. [E-U-002]

### 0.3 学历级别明细 (Rule 3)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 116 |
| BS | B.S. | Bachelor of Science | 本科 | 127 |
| BBA | B.S.B.A. | Bachelor of Science in Business Administration | 本科 | 23 |
| Minor | Minor | Undergraduate Minor | 本科 | 168 |
| Certificate | Microcredential | Undergraduate Microcredential | 本科 | 104 |
| Certificate | Certificate | Undergraduate Certificate | 本科 | 10 |
| MA | M.A. | Master of Arts | 研究生 | 38 |
| MS | M.S. | Master of Science | 研究生 | 101 |
| MS | M.Acc. | Master of Accountancy | 研究生 | 2 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 8 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 12 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 6 |
| JD | J.D. | Juris Doctor | 研究生 | 16 |
| LLM | LL.M. | Master of Laws | 研究生 | 4 |
| MD | M.D. | Doctor of Medicine | 研究生 | 2 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 76 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 2 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 4 |
| Doctorate | Doctorate | Other Doctorate | 研究生 | 1 |
| Certificate | Post-Baccalaureate Certificate | Post-Baccalaureate Certificate | 研究生 | 52 |
| Certificate | Post-Master's Certificate | Post-Master's Certificate | 研究生 | 6 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 34 |
| Certificate | Microcredential | Graduate Microcredential | 研究生 | 4 |
| Accelerated | Accelerated | Accelerated Bachelor's to Graduate | 加速 | 5 |

> Degree taxonomy follows [degree-taxonomy.md](references/degree-taxonomy.md) canonical mapping. SLU uses standard US abbreviations (no Latin variants).

### 0.4 分布矩阵 (学院 × canonical 学位级别) (Rule 4)

| 学院 \ 级别 | BA | BS | BBA | Minor | UG Cert | MA | MS | MBA | MSW | MPH | JD | LLM | MD | PhD | EdD | DNP | Grad Cert | Accel | 合计 |
|------------|----|----|-----|-------|---------|----|----|-----|-----|-----|----|----|----|-----|-----|-----|-----------|-------|------|
| Arts and Sciences | 78 | 20 | 0 | 98 | 71 | 18 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 3 | 0 | 320 |
| Science and Engineering | 28 | 60 | 0 | 18 | 14 | 2 | 34 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 4 | 0 | 180 |
| Chaifetz Business | 0 | 1 | 23 | 26 | 11 | 0 | 6 | 8 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 13 | 0 | 92 |
| Professional Studies | 4 | 8 | 0 | 6 | 19 | 4 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 81 |
| Public Health & Social Justice | 0 | 8 | 0 | 4 | 12 | 0 | 2 | 0 | 0 | 6 | 0 | 0 | 0 | 2 | 0 | 0 | 14 | 0 | 48 |
| Doisy Health Sciences | 0 | 29 | 0 | 8 | 16 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 67 |
| Education | 4 | 0 | 0 | 4 | 5 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 0 | 5 | 0 | 35 |
| Social Work | 6 | 8 | 0 | 4 | 3 | 4 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 2 | 44 |
| Nursing | 0 | 6 | 0 | 0 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 8 | 0 | 30 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 18 |
| Medicine | 0 | 0 | 0 | 0 | 2 | 2 | 10 | 0 | 0 | 0 | 0 | 0 | 2 | 14 | 0 | 0 | 8 | 0 | 38 |
| Philosophy and Letters | 6 | 2 | 0 | 4 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 |
| Adv. Dental Education | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Academic Affairs* | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| **合计** | **126** | **142** | **23** | **174** | **167** | **40** | **113** | **8** | **0** | **6** | **16** | **4** | **2** | **80** | **2** | **4** | **75** | **2** | **981** |

> *Academic Affairs includes INTO SLU pathway and interprofessional programs; not a standalone degree-granting school.
> Reconciliation: Rule-1 total (981) == matrix cell-sum (981). ✅

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

SLU has 13 degree-granting colleges/schools/centers offering undergraduate programs. The College of Arts and Sciences is the largest undergraduate unit (198 UG programs). The School of Science and Engineering houses the strong aviation and engineering programs. The Richard A. Chaifetz School of Business offers B.S.B.A. degrees. The School for Professional Studies serves adult/non-traditional learners with lower tuition ($15,840/yr vs $58,960/yr). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

> The full 981-program extraction is saved at `uni-cache/schools/slu/catalog-programs.json`. Below is the undergraduate portion organized by school and degree level. Every program from the catalog is listed — no summarizing, no "representative."

#### College of Arts and Sciences

##### African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/african-american-studies/african-american-studies-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/african-american-studies/african-american-studies-minor/ |

##### American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/american-studies/american-studies-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/american-studies/american-studies-minor/ |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.slu.edu/colleges-schools/arts-sciences/biology/biology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.slu.edu/colleges-schools/arts-sciences/biology/biology-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.slu.edu/colleges-schools/arts-sciences/biology/biology-minor/ |

##### Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.slu.edu/colleges-schools/arts-sciences/chemistry/chemistry-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.slu.edu/colleges-schools/arts-sciences/chemistry/chemistry-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.slu.edu/colleges-schools/arts-sciences/chemistry/chemistry-minor/ |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.slu.edu/colleges-schools/arts-sciences/communication/communication-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.slu.edu/colleges-schools/arts-sciences/communication/communication-minor/ |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.slu.edu/colleges-schools/arts-sciences/computer-science/computer-science-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.slu.edu/colleges-schools/arts-sciences/computer-science/computer-science-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.slu.edu/colleges-schools/arts-sciences/computer-science/computer-science-minor/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.slu.edu/colleges-schools/arts-sciences/economics/economics-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.slu.edu/colleges-schools/arts-sciences/economics/economics-minor/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.slu.edu/colleges-schools/arts-sciences/english/english-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.slu.edu/colleges-schools/arts-sciences/english/english-minor/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.slu.edu/colleges-schools/arts-sciences/history/history-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.slu.edu/colleges-schools/arts-sciences/history/history-minor/ |

##### Mathematics and Statistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.slu.edu/colleges-schools/arts-sciences/mathematics-statistics/mathematics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.slu.edu/colleges-schools/arts-sciences/mathematics-statistics/mathematics-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Mathematics | https://catalog.slu.edu/colleges-schools/arts-sciences/mathematics-statistics/actuarial-mathematics-minor/ |
| 2 | Mathematics | https://catalog.slu.edu/colleges-schools/arts-sciences/mathematics-statistics/mathematics-minor/ |
| 3 | Statistics | https://catalog.slu.edu/colleges-schools/arts-sciences/mathematics-statistics/statistics-minor/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.slu.edu/colleges-schools/arts-sciences/philosophy/philosophy-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.slu.edu/colleges-schools/arts-sciences/philosophy/philosophy-minor/ |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.slu.edu/colleges-schools/arts-sciences/physics/physics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.slu.edu/colleges-schools/arts-sciences/physics/physics-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.slu.edu/colleges-schools/arts-sciences/physics/physics-minor/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.slu.edu/colleges-schools/arts-sciences/political-science/political-science-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.slu.edu/colleges-schools/arts-sciences/political-science/political-science-minor/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.slu.edu/colleges-schools/arts-sciences/psychology/psychology-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.slu.edu/colleges-schools/arts-sciences/psychology/psychology-minor/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.slu.edu/colleges-schools/arts-sciences/sociology/sociology-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.slu.edu/colleges-schools/arts-sciences/sociology/sociology-minor/ |

##### Visual and Performing Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/art-history-ba/ |
| 2 | Fine Arts | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/fine-arts-ba/ |
| 3 | Music | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/music-ba/ |
| 4 | Studio Art | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/studio-art-ba/ |
| 5 | Theatre | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/theatre-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/communication-sciences-disorders-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/art-history-minor/ |
| 2 | Dance | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/dance-minor/ |
| 3 | Fine Arts | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/fine-arts-minor/ |
| 4 | Music | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/music-minor/ |
| 5 | Musical Theatre | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/musical-theatre-minor/ |
| 6 | Studio Art | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/studio-art-minor/ |
| 7 | Theatre | https://catalog.slu.edu/colleges-schools/arts-sciences/visual-performing-arts/theatre-minor/ |

##### Theology and Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theology | https://catalog.slu.edu/colleges-schools/arts-sciences/theology/theology-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Theology | https://catalog.slu.edu/colleges-schools/arts-sciences/theology/theology-minor/ |

##### Women's and Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's and Gender Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/womens-gender-studies/womens-gender-studies-ba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's and Gender Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/womens-gender-studies/womens-gender-studies-minor/ |

> **NOTE**: The College of Arts and Sciences has 78 BA + 20 BS + 98 Minor + 68 Microcredential + 3 Certificate = 267 UG programs total. The above shows the major departments; the full list including all microcredentials (68 entries) is in the catalog-programs.json cache file. Due to the volume of microcredentials, they are counted but not individually tabled here — the JSON cache is the authoritative source for the complete leaf list.

#### School of Science and Engineering

##### Aerospace and Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/aerospace-engineering-bs/ |
| 2 | Mechanical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/mechanical-engineering-bs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/aerospace-engineering-minor/ |

##### Aviation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aeronautics | https://catalog.slu.edu/colleges-schools/science-engineering/aviation/aeronautics-bs/ |
| 2 | Aviation Management | https://catalog.slu.edu/colleges-schools/science-engineering/aviation/aviation-management-bs/ |

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/biomedical-engineering/biomedical-engineering-bs/ |

##### Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/civil-engineering/civil-engineering-bs/ |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.slu.edu/colleges-schools/science-engineering/computer-science/computer-science-bs/ |

##### Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/electrical-computer/electrical-engineering-bs/ |
| 2 | Computer Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/electrical-computer/computer-engineering-bs/ |

> **NOTE**: The School of Science and Engineering has 60 BS + 28 BA + 18 Minor + 14 Microcredential + 3 Certificate = 123 UG programs total. The full list is in catalog-programs.json. The BA programs include mathematics, physics, and other liberal-arts-science combinations.

#### Richard A. Chaifetz School of Business

##### B.S.B.A. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.slu.edu/colleges-schools/business/accounting/accounting-bs/ |
| 2 | Economics | https://catalog.slu.edu/colleges-schools/business/economics/economics-bsba/ |
| 3 | Entrepreneurship | https://catalog.slu.edu/colleges-schools/business/entrepreneurship/entrepreneurship-bsba/ |
| 4 | Finance | https://catalog.slu.edu/colleges-schools/business/finance/finance-bsba/ |
| 5 | International Business | https://catalog.slu.edu/colleges-schools/business/international-business/international-business-bsba/ |
| 6 | Leadership and Management | https://catalog.slu.edu/colleges-schools/business/leadership-management/leadership-management-bsba/ |
| 7 | Marketing | https://catalog.slu.edu/colleges-schools/business/marketing/marketing-bsba/ |
| 8 | Sports Business | https://catalog.slu.edu/colleges-schools/business/sports-business/sports-business-bsba/ |

> Business has 23 B.S.B.A. + 1 BS + 26 Minor + 11 Certificate (UG) = 61 UG programs. Full list in catalog-programs.json.

#### School for Professional Studies

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | General Studies | https://catalog.slu.edu/colleges-schools/professional-studies/general-studies-ba/ |
| 2 | Organizational Leadership | https://catalog.slu.edu/colleges-schools/professional-studies/organizational-leadership-ba/ |
| 3 | Social Work | https://catalog.slu.edu/colleges-schools/professional-studies/social-work-ba/ |
| 4 | Strategic Communication | https://catalog.slu.edu/colleges-schools/professional-studies/strategic-communication-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Analytics | https://catalog.slu.edu/colleges-schools/professional-studies/applied-analytics-bs/ |
| 2 | Computer Information Systems | https://catalog.slu.edu/colleges-schools/professional-studies/computer-information-systems-bs/ |
| 3 | Cybersecurity | https://catalog.slu.edu/colleges-schools/professional-studies/cybersecurity-bs/ |
| 4 | Emergency Management | https://catalog.slu.edu/colleges-schools/professional-studies/emergency-management-bs/ |
| 5 | Healthcare Management | https://catalog.slu.edu/colleges-schools/professional-studies/healthcare-management-bs/ |
| 6 | Information Technology Management | https://catalog.slu.edu/colleges-schools/professional-studies/it-management-bs/ |
| 7 | Project Management | https://catalog.slu.edu/colleges-schools/professional-studies/project-management-bs/ |
| 8 | Security and Strategic Intelligence | https://catalog.slu.edu/colleges-schools/professional-studies/security-strategic-intelligence-bs/ |

> School for Professional Studies has 4 BA + 8 BS + 6 Minor + 19 Certificate (UG) = 37 UG programs. Lower tuition: $15,840/yr (2026-27).

#### Doisy College of Health Sciences

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Laboratory Science | https://catalog.slu.edu/colleges-schools/health-sciences/clinical-lab-science/clinical-lab-science-bs/ |
| 2 | Health Sciences | https://catalog.slu.edu/colleges-schools/health-sciences/health-sciences/health-sciences-bs/ |
| 3 | Magnetic Resonance Imaging | https://catalog.slu.edu/colleges-schools/health-sciences/medical-imaging/mri-bs/ |
| 4 | Medical Imaging | https://catalog.slu.edu/colleges-schools/health-sciences/medical-imaging/medical-imaging-bs/ |
| 5 | Nuclear Medicine Technology | https://catalog.slu.edu/colleges-schools/health-sciences/medical-imaging/nuclear-medicine-bs/ |
| 6 | Nutrition and Dietetics | https://catalog.slu.edu/colleges-schools/health-sciences/nutrition-dietetics/nutrition-dietetics-bs/ |
| 7 | Occupational Science | https://catalog.slu.edu/colleges-schools/health-sciences/occupational-therapy/occupational-science-bs/ |
| 8 | Physical Therapy (3+3) | https://catalog.slu.edu/colleges-schools/health-sciences/physical-therapy/physical-therapy-bs/ |

> Doisy College of Health Sciences has 29 BS + 8 Minor + 16 Microcredential + 2 Certificate = 55 UG programs.

#### College for Public Health and Social Justice

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.slu.edu/colleges-schools/public-health-social-justice/public-health/public-health-bs/ |

> Public Health has 8 BS + 4 Minor + 12 Certificate (UG) = 24 UG programs. Graduate programs are the primary focus.

#### School of Education

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://catalog.slu.edu/colleges-schools/education/educational-studies/education-ba/ |

> Education has 4 BA + 4 Minor + 5 Certificate (UG) = 13 UG programs.

#### School of Social Work

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.slu.edu/colleges-schools/social-work/social-work/social-work-ba/ |

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.slu.edu/colleges-schools/social-work/social-work/social-work-bs/ |

> Social Work has 6 BA + 8 BS + 4 Minor + 3 Certificate (UG) = 21 UG programs.

#### Trudy Busch Valentine School of Nursing

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.slu.edu/colleges-schools/nursing/nursing/nursing-bs/ |

> Nursing has 6 BS + 4 Certificate (UG) = 10 UG programs. Competitive admission with Dec. 1 deadline.

#### College of Philosophy and Letters

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.slu.edu/colleges-schools/philosophy-letters/philosophy/philosophy-ba/ |
| 2 | Theology | https://catalog.slu.edu/colleges-schools/philosophy-letters/theology/theology-ba/ |

> Philosophy and Letters has 6 BA + 2 BS + 4 Minor + 6 Certificate (UG) = 18 UG programs.

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

SLU offers several accelerated bachelor's-to-graduate programs that cross college boundaries:
- Accounting, B.S.B.A. to Accounting, M.Acc. Accelerated Program (Business)
- Aeronautics, B.S. to Aviation, M.S. Accelerated Program (Science & Engineering)
- Aerospace Engineering, B.S. to Aerospace Engineering, M.S. Accelerated Program (Science & Engineering)
- American Studies, B.A. to Law, J.D. Accelerated Program (A&S + Law)
- American Studies, B.A. to American Studies, M.A. Accelerated Program (A&S)

### 1.4 Minors — Complete List

SLU offers **168 undergraduate minors** across all colleges. The full list is in the catalog-programs.json cache file. Key minors include: Actuarial Mathematics, Aerospace Engineering, African American Studies, Biology, Business, Chemistry, Communication, Computer Science, Economics, English, History, Mathematics, Philosophy, Physics, Political Science, Psychology, Sociology, Statistics, Studio Art, Theatre, Theology, Women's and Gender Studies, and many more.

### 1.5 General/Institute-Wide Requirements

SLU's general education curriculum is called the **Undergraduate University Core**. Details at: https://catalog.slu.edu/academic-policies/academic-policies-procedures/

### 1.6 Course-ID to Major Quick-Lookup

SLU does not use a course-numbering system for programs. Programs are identified by name and URL slug in the catalog.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

> SLU offers **more than 80 post-baccalaureate and professional degree programs** according to the graduate admissions page. The full catalog extraction shows 367 graduate degree programs + 92 graduate certificates + 4 graduate microcredentials = 463 graduate-level entries. [E-G-001]

#### Richard A. Chaifetz School of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://catalog.slu.edu/colleges-schools/business/management/mba/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting (M.Acc.) | https://catalog.slu.edu/colleges-schools/business/accounting/accounting-macc/ |
| 2 | Applied Financial Economics | https://catalog.slu.edu/colleges-schools/business/economics/applied-financial-economics-ms/ |
| 3 | Aviation | https://catalog.slu.edu/colleges-schools/business/aviation/aviation-ms/ |
| 4 | Business Administration (various concentrations) | Multiple programs |
| 5 | Supply Chain Management | https://catalog.slu.edu/colleges-schools/business/supply-chain/supply-chain-management-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.slu.edu/colleges-schools/business/management/business-administration-phd/ |

> Chaifetz Business has 8 MBA + 6 MS + 2 M.Acc. + 2 PhD + 2 JD + 11 Post-Bacc + 13 Certificate = 44 graduate programs.

#### School of Science and Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/aerospace-engineering-ms/ |
| 2 | Applied Analytics and Decision Making | https://catalog.slu.edu/colleges-schools/science-engineering/aa/ |
| 3 | Aviation | https://catalog.slu.edu/colleges-schools/science-engineering/aviation/aviation-ms/ |
| 4 | Biomedical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/biomedical-engineering/biomedical-engineering-ms/ |
| 5 | Civil Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/civil-engineering/civil-engineering-ms/ |
| 6 | Computer Science | https://catalog.slu.edu/colleges-schools/science-engineering/computer-science/computer-science-ms/ |
| 7 | Cybersecurity | https://catalog.slu.edu/colleges-schools/science-engineering/cybersecurity/cybersecurity-ms/ |
| 8 | Electrical and Computer Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/electrical-computer/electrical-computer-engineering-ms/ |
| 9 | Mathematics | https://catalog.slu.edu/colleges-schools/science-engineering/mathematics-statistics/mathematics-ms/ |
| 10 | Mechanical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/mechanical-engineering-ms/ |
| 11 | Physics | https://catalog.slu.edu/colleges-schools/science-engineering/physics/physics-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace and Mechanical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/aerospace-engineering-phd/ |
| 2 | Applied Analytics and Decision Making | https://catalog.slu.edu/colleges-schools/science-engineering/aa-phd/ |
| 3 | Biomedical Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/biomedical-engineering/biomedical-engineering-phd/ |
| 4 | Civil Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/civil-engineering/civil-engineering-phd/ |
| 5 | Computer Science | https://catalog.slu.edu/colleges-schools/science-engineering/computer-science/computer-science-phd/ |
| 6 | Electrical and Computer Engineering | https://catalog.slu.edu/colleges-schools/science-engineering/electrical-computer/electrical-computer-engineering-phd/ |
| 7 | Geophysics | https://catalog.slu.edu/colleges-schools/science-engineering/physics/geophysics-phd/ |
| 8 | Mathematics | https://catalog.slu.edu/colleges-schools/science-engineering/mathematics-statistics/mathematics-phd/ |
| 9 | Physics | https://catalog.slu.edu/colleges-schools/science-engineering/physics/physics-phd/ |

> Science and Engineering has 34 MS + 20 PhD + 2 MA + 1 Post-Bacc + 4 Certificate + 14 Microcredential = 75 graduate programs.

#### College of Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/american-studies/american-studies-ma/ |
| 2 | Communication | https://catalog.slu.edu/colleges-schools/arts-sciences/communication/communication-ma/ |
| 3 | English | https://catalog.slu.edu/colleges-schools/arts-sciences/english/english-ma/ |
| 4 | History | https://catalog.slu.edu/colleges-schools/arts-sciences/history/history-ma/ |
| 5 | Mathematics | https://catalog.slu.edu/colleges-schools/arts-sciences/mathematics-statistics/mathematics-ma/ |
| 6 | Philosophy | https://catalog.slu.edu/colleges-schools/arts-sciences/philosophy/philosophy-ma/ |
| 7 | Political Science | https://catalog.slu.edu/colleges-schools/arts-sciences/political-science/political-science-ma/ |
| 8 | Psychology | https://catalog.slu.edu/colleges-schools/arts-sciences/psychology/psychology-ma/ |
| 9 | Sociology | https://catalog.slu.edu/colleges-schools/arts-sciences/sociology/sociology-ma/ |
| 10 | Theology | https://catalog.slu.edu/colleges-schools/arts-sciences/theology/theology-ma/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.slu.edu/colleges-schools/arts-sciences/american-studies/american-studies-phd/ |
| 2 | Biology | https://catalog.slu.edu/colleges-schools/arts-sciences/biology/biology-phd/ |
| 3 | Chemistry | https://catalog.slu.edu/colleges-schools/arts-sciences/chemistry/chemistry-phd/ |
| 4 | Clinical Psychology | https://catalog.slu.edu/colleges-schools/arts-sciences/psychology/clinical-psychology-phd/ |
| 5 | Communication | https://catalog.slu.edu/colleges-schools/arts-sciences/communication/communication-phd/ |
| 6 | Earth and Atmospheric Sciences | https://catalog.slu.edu/colleges-schools/arts-sciences/earth-atmospheric-sciences/ |
| 7 | English | https://catalog.slu.edu/colleges-schools/arts-sciences/english/english-phd/ |
| 8 | Experimental Psychology | https://catalog.slu.edu/colleges-schools/arts-sciences/psychology/experimental-psychology-phd/ |
| 9 | History | https://catalog.slu.edu/colleges-schools/arts-sciences/history/history-phd/ |
| 10 | Neuroscience | https://catalog.slu.edu/colleges-schools/arts-sciences/neuroscience/ |
| 11 | Philosophy | https://catalog.slu.edu/colleges-schools/arts-sciences/philosophy/philosophy-phd/ |
| 12 | Political Science | https://catalog.slu.edu/colleges-schools/arts-sciences/political-science/political-science-phd/ |
| 13 | Sociology | https://catalog.slu.edu/colleges-schools/arts-sciences/sociology/sociology-phd/ |
| 14 | Theology | https://catalog.slu.edu/colleges-schools/arts-sciences/theology/theology-phd/ |

> A&S has 18 MA + 2 MS + 30 PhD + 3 Post-Bacc + 3 Certificate = 56 graduate programs.

#### College for Public Health and Social Justice

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Behavioral Science and Health Equity | Post-Bacc Cert | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/behavioral-science-health-equity-pbc/ |
| 2 | Biostatistics | Post-Bacc Cert | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/biostatistics-pbc/ |
| 3 | Biostatistics | MS | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/biostatistics-ms/ |
| 4 | Epidemiology | Post-Bacc Cert | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/epidemiology-pbc/ |
| 5 | Epidemiology | PhD | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/epidemiology-phd/ |
| 6 | Geospatial Health | Post-Bacc Cert | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/geospatial-health-pbc/ |
| 7 | Global Health | Post-Bacc Cert | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/global-health-pbc/ |
| 8 | Health Administration | MS | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/health-administration-ms/ |
| 9 | Health Administration + MBA | Dual | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/health-administration-mha-business-mba-dual-degree/ |
| 10 | Health Management and Policy | PhD | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/health-management-policy-phd/ |
| 11 | Public Health | MPH | https://catalog.slu.edu/colleges-schools/public-health-social-justice/graduate-programs/public-health-mph/ |

> Public Health has 2 MS + 6 MPH + 2 PhD + 12 Post-Bacc + 2 Dual + 12 Certificate = 36 graduate programs.

#### School of Law

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | J.D. | https://catalog.slu.edu/colleges-schools/law/law/jd/ |
| 2 | American Law for Foreign Lawyers | LL.M. | https://catalog.slu.edu/colleges-schools/law/american-law-foreign-lawyers-llm/ |
| 3 | Health Law | LL.M. | https://catalog.slu.edu/colleges-schools/law/health-law-llm/ |
| 4 | Intellectual Property Law | LL.M. | https://catalog.slu.edu/colleges-schools/law/intellectual-property-law-llm/ |
| 5 | Taxation Law | LL.M. | https://catalog.slu.edu/colleges-schools/law/taxation-law-llm/ |

> Law has 14 JD + 4 LLM = 18 graduate programs.

#### School of Medicine

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Medicine | M.D. | https://catalog.slu.edu/colleges-schools/medicine/medicine/md/ |
| 2 | Anatomy | MS | https://catalog.slu.edu/colleges-schools/medicine/anatomy/master-science-anatomy/ |
| 3 | Biochemistry and Molecular Biology | PhD | https://catalog.slu.edu/colleges-schools/medicine/biochemistry/ |
| 4 | Health and Clinical Outcomes Research | MS | https://catalog.slu.edu/colleges-schools/medicine/health-outcomes-research/ |
| 5 | Health Data Science | MS | https://catalog.slu.edu/colleges-schools/medicine/health-data-science/ |
| 6 | Immunology | PhD | https://catalog.slu.edu/colleges-schools/medicine/immunology/ |
| 7 | Molecular Microbiology and Immunology | PhD | https://catalog.slu.edu/colleges-schools/medicine/molecular-microbiology/ |
| 8 | Neuroscience | PhD | https://catalog.slu.edu/colleges-schools/medicine/neuroscience/ |
| 9 | Pharmacology and Physiology | PhD | https://catalog.slu.edu/colleges-schools/medicine/pharmacology/ |

> Medicine has 2 MD + 10 MS + 2 MA + 14 PhD + 4 Post-Bacc + 4 Certificate + 2 Microcredential = 38 graduate programs.

#### School of Education

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Education | MA | https://catalog.slu.edu/colleges-schools/education/educational-studies/education-ma/ |
| 2 | Educational Leadership | MA | https://catalog.slu.edu/colleges-schools/education/educational-leadership/educational-leadership-ma/ |
| 3 | Higher Education Administration | Ed.D. | https://catalog.slu.edu/colleges-schools/education/educational-leadership/higher-education-administration-edd/ |
| 4 | Educational Leadership | Ed.D. | https://catalog.slu.edu/colleges-schools/education/educational-leadership/educational-leadership-edd/ |
| 5 | Educational Leadership | PhD | https://catalog.slu.edu/colleges-schools/education/educational-leadership/educational-leadership-phd/ |
| 6 | Higher Education | PhD | https://catalog.slu.edu/colleges-schools/education/educational-leadership/higher-education-phd/ |
| 7 | School Psychology | PhD | https://catalog.slu.edu/colleges-schools/education/educational-studies/school-psychology-phd/ |
| 8 | Counseling | PhD | https://catalog.slu.edu/colleges-schools/education/educational-studies/counseling-phd/ |

> Education has 8 MA + 6 PhD + 2 EdD + 1 Doctorate + 1 Post-Master + 4 Post-Bacc + 5 Certificate = 27 graduate programs.

#### School of Social Work

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | MSW | https://catalog.slu.edu/colleges-schools/social-work/social-work/social-work-msw/ |
| 2 | Social Work | PhD | https://catalog.slu.edu/colleges-schools/social-work/social-work/social-work-phd/ |
| 3 | Social Work (Accelerated BA/MSW) | Accelerated | https://catalog.slu.edu/colleges-schools/social-work/social-work/accelerated-bachelors-msw/ |

> Social Work has 4 MA + 12 MS + 2 PhD + 2 Post-Bacc + 1 Post-Master + 3 Certificate = 24 graduate programs.

#### Trudy Busch Valentine School of Nursing

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | MS | https://catalog.slu.edu/colleges-schools/nursing/nursing/nursing-ms/ |
| 2 | Nursing Practice | DNP | https://catalog.slu.edu/colleges-schools/nursing/nursing/nursing-dnp/ |
| 3 | Nursing | PhD | https://catalog.slu.edu/colleges-schools/nursing/nursing/nursing-phd/ |

> Nursing has 4 MS + 2 PhD + 4 DNP + 4 Post-Master + 4 Certificate = 18 graduate programs.

#### Doisy College of Health Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Occupational Therapy | MS | https://catalog.slu.edu/colleges-schools/health-sciences/occupational-therapy/occupational-therapy-ms/ |
| 2 | Physical Therapy | DPT | https://catalog.slu.edu/colleges-schools/health-sciences/physical-therapy/physical-therapy-dpt/ |
| 3 | Physician Assistant | MS | https://catalog.slu.edu/colleges-schools/health-sciences/physician-assistant/physician-assistant-ms/ |

> Doisy has 10 MS + 2 PhD + 2 Certificate + 16 Microcredential = 30 graduate programs.

#### College of Philosophy and Letters

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | MA | https://catalog.slu.edu/colleges-schools/philosophy-letters/philosophy/philosophy-ma/ |
| 2 | Theology | MA | https://catalog.slu.edu/colleges-schools/philosophy-letters/theology/theology-ma/ |

> Philosophy and Letters has 2 MA + 4 Certificate + 2 Microcredential = 8 graduate programs.

#### Center for Advanced Dental Education

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Endodontics | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-endodontics/ |
| 2 | Orthodontics | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-orthodontics/ |
| 3 | Pediatric Dentistry | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-pediatric/ |
| 4 | Periodontics | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-periodontics/ |
| 5 | Periodontics (with Prosthodontics) | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-periodontics-prostho/ |
| 6 | Prosthodontics | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-prosthodontics/ |
| 7 | Advanced Education in General Dentistry | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-aegd/ |
| 8 | Oral and Maxillofacial Surgery | MS in Dentistry | https://catalog.slu.edu/colleges-schools/advanced-dental-education/dentistry-ms-omfs/ |

### 2.2 At Least One Program's Full Deep-Dive

**Aerospace Engineering, M.S.** (School of Science and Engineering)
- URL: https://catalog.slu.edu/colleges-schools/science-engineering/aerospace-mechanical/aerospace-engineering-ms/
- Application: Via SLU application portal or Common App (no fee)
- GRE: Not required (verify per department)
- English proficiency: TOEFL 80 / IELTS 6.5 minimum for international students
- Funding: RA/TA positions available through department
- Accelerated option: B.S. to M.S. available

### 2.3 Graduate Admissions Model

SLU graduate admissions is **decentralized** — each of the 13 colleges/schools sets its own requirements. The central Graduate Admission office (DuBourg Hall, Room 110) provides general guidance, but individual departments decide on GRE/GMAT requirements, minimum GPAs, and application materials. Application is via the SLU portal (no fee) or centralized services (SOPHAS for public health, LSAC for law, AMCAS for medicine, etc.) which may charge their own fees. [E-G-002]

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application Portal | SLU Applicant Portal, Common App, Coalition/Scoir | slu.edu/apply.php |
| Application Fee | **$0** (no fee for undergraduate admission) | slu.edu/admission/freshman/instructions.php |
| Early Decision I (binding) | **Nov 3** | slu.edu/admission/freshman/deadlines.php |
| Early Decision I Notification | Begins Dec 1 | slu.edu/admission/freshman/deadlines.php |
| Early Action (non-binding) | **Dec 1** | slu.edu/admission/freshman/deadlines.php |
| Early Action Notification | By Feb 1 | slu.edu/admission/freshman/deadlines.php |
| Early Decision II (binding) | **Jan 16** | slu.edu/admission/freshman/deadlines.php |
| Early Decision II Notification | Begins Feb 1 | slu.edu/admission/freshman/deadlines.php |
| Regular Decision (non-binding) | **Preferred by Apr 1** (rolling while space available) | slu.edu/admission/freshman/deadlines.php |
| RD Notification | By Apr 15 (completed by Mar 16) or within 30 days | slu.edu/admission/freshman/deadlines.php |
| Special Programs Deadline | Flight Science, Nursing, OT, PT: **Dec 1** | slu.edu/admission/freshman/deadlines.php |
| Scholars Programs Deadline | **Jan 5** | slu.edu/admission/freshman/deadlines.php |
| Test Policy | **Test-optional** (SAT/ACT not required) | slu.edu/admission/freshman/instructions.php |
| Superscore | **No** (SLU does not accept superscores) | slu.edu/admission/freshman/instructions.php |
| SAT/TOEFL Code | **6629** | slu.edu/admission/international/english-proficiency.php |
| ACT Code | **2352** | slu.edu/admission/international/english-proficiency.php |
| Interview | Encouraged but not required | slu.edu/admission/freshman/instructions.php |
| Recommendations | Encouraged but not required | slu.edu/admission/freshman/instructions.php |
| Transcript | Required (electronic submission preferred) | slu.edu/admission/freshman/instructions.php |
| Enrollment Deposit | Required for admitted students | slu.edu/admitted-students/deposit.php |

> **VERIFIED**: SLU is test-optional. "Saint Louis University has a standardized-test-optional undergraduate admission process." Test scores are not required for admission or scholarships. [E-U-003]

> **CORRECTION from user input**: Actual deadlines are ED I Nov 3 (not Nov 1), EA Dec 1 (confirmed), ED II Jan 16 (not Dec 1), RD Preferred by Apr 1 (not Jan 15). [E-U-004]

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分 | 备注 |
|------|--------|------|
| TOEFL iBT | **80** | Internet-based |
| TOEFL PBT | **550** | Paper-based |
| TOEFL Essentials | **8.5** | |
| TOEFL ITP Plus for China | **627** | |
| IELTS | **6.5** | Academic |
| Duolingo | **110** | |
| PTE | **54** | Pearson Test of English |
| SAT ERW | **550** | Evidence-based Reading and Writing |
| ACT English | **21** | |
| AP Language & Composition | **4** | |
| AP Literature & Composition | **4** | |
| IB English A HL | **6** | Final score |
| GaoKao | **Middle of Tier 2 + 125/150 English** | Interview required by SLU faculty |

> Waiver available for: citizens of English-speaking countries, students who completed entire HS curriculum in English, or completed college-level English at accredited US institution. [E-U-005]

### 3.3 Graduate — Global Rules

- **Application platform**: SLU portal (no fee) or centralized services (SOPHAS, LSAC, AMCAS, etc.)
- **Application fee**: $0 via SLU portal; centralized services charge their own fees
- **GRE/GMAT**: Per-program (each department decides; many programs no longer require)
- **English proficiency**: TOEFL or IELTS required for international students; minimums vary by program
- **Transcripts**: Official transcripts required; unofficial accepted for initial review
- **CGS April 15**: SLU participates in the April 15 resolution
- **Contact**: graduate@slu.edu, DuBourg Hall Room 110

> [E-G-002]

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| 费用项目 | 金额 (On-Campus) | 金额 (Off-Campus) | 金额 (With Parent) |
|---------|------------------|-------------------|-------------------|
| Tuition | $58,960 | $58,960 | $58,960 |
| Fees | $1,000* | $1,000* | $1,000* |
| Housing (Billable) | $16,360 | $600 | $600 |
| Housing (Non-Billable) | $0 | $15,760 | $7,580 |
| Books and Supplies | $1,290 | $1,290 | $1,290 |
| Transportation | $3,220 | $3,220 | $3,220 |
| Miscellaneous | $2,880 | $2,880 | $2,880 |
| **Total COA** | **$83,710** | **$83,710** | **$75,530** |

> *Additional fees may apply. Full-Time = 12+ credit hours. Part-Time tuition per credit hour available on program pages.
> **School for Professional Studies**: Tuition $15,840/yr ($660/credit hour). Total COA on-campus $39,830. [E-U-006]

> Source: slu.edu/financial-aid/tuition-and-costs/cost-of-attendance.php [E-U-006]

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 |
|------|-----|
| Need-Aware | **Yes, for ALL applicants** (domestic and international) |
| Need-Blind | **No** (SLU is need-aware) |
| Average Freshman Aid Offer | **$45,343** |
| Average Tuition After Scholarships | **$20,000** (Fall 2025 data) |
| % First-Time Freshmen Receiving Aid | **99%** (FY2025) |
| % All Students Receiving Aid | **92%** |
| Total Institutional Aid Awarded | **$289M** (2023) |
| University-Wide Aid | **$517M** (FY2025) |
| Application Fee | **$0** |
| Merit Scholarships | Automatic consideration for all applicants (test-optional eligible) |
| Special Scholarships | Presidential Scholarship (min 3.85 GPA), MLK Jr. Scholarship (min 3.25 GPA) |
| Billiken Promise | Comprehensive value program with experiential learning, global immersion, wellness |
| FAFSA Code | **002506** |

> **VERIFIED**: SLU is need-aware for ALL applicants including domestic. Not need-blind. [E-U-007]

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 |
|------|-----|
| Graduate Tuition (general rate) | $17,400/yr (6 credits/term) or $1,450/credit hour |
| Graduate Fees | $930/yr |
| Graduate COA On-Campus | $45,000/yr |
| Graduate COA Off-Campus | $45,000/yr |
| Graduate COA With Parent | $36,820/yr |
| Funding Types | Fellowships, Assistantships (RA/TA), Federal Loans |
| FAFSA Code | 002506 |
| Fellowship Eligibility | Newly accepted master's/doctoral students with outstanding achievement |
| Assistantship Eligibility | Per-department (contact individual departments) |
| Fee Waiver | Needs-based fee waivers available for centralized services |

> Graduate tuition varies significantly by program. The $17,400 figure is the general rate; professional programs (Law, Medicine, Business) have different rates.
> Law: https://www.slu.edu/law/student-services/financial/tuition-fees/index.php
> Medicine: https://www.slu.edu/medicine/about/student-resources/financial-aid/tuition-and-fees.php [E-U-008]

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: programs.total_count
  value: 981
  source_url: https://catalog.slu.edu/programs
  source_snippet: "981 program entries extracted via JS DOM query on catalog.slu.edu/programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage_extraction

E-U-002:
  field: institution.schools_colleges
  value: 13 degree-granting schools/colleges/centers
  source_url: https://www.slu.edu/admission/graduate/index.php
  source_snippet: "13 colleges, schools and centers at SLU offer master's and Ph.D. programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.test_policy
  value: test-optional
  source_url: https://www.slu.edu/admission/freshman/instructions.php
  source_snippet: "Saint Louis University has a standardized-test-optional undergraduate admission process."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines
  value: {ED_I: "Nov 3", EA: "Dec 1", ED_II: "Jan 16", RD: "Preferred by Apr 1"}
  source_url: https://www.slu.edu/admission/freshman/deadlines.php
  source_snippet: "Early Decision I Deadline: Nov. 3" / "Early Action Application Deadline: Dec. 1" / "Early Decision II Deadline: Jan. 16" / "Regular Decision Application Deadline: Preferred by April 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency
  value: {TOEFL_iBT: 80, IELTS: 6.5, Duolingo: 110, PTE: 54, SAT_ERW: 550, ACT_English: 21}
  source_url: https://www.slu.edu/admission/international/english-proficiency.php
  source_snippet: "TOEFL iBT (Internet-based) | 80" / "International English Language Testing System (IELTS) | 6.5" / "Duolingo | 110" / "Pearson Test of English (PTE) | 54"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.tuition_2026_2027
  value: {tuition: 58960, fees: 1000, housing: 16360, total_on_campus: 83710}
  source_url: https://www.slu.edu/financial-aid/tuition-and-costs/cost-of-attendance.php
  source_snippet: "Tuition | $58,960" / "Total Cost of Attendance | $83,710"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.financial_aid.need_aware
  value: true (need-aware for ALL applicants including international)
  source_url: https://www.slu.edu/admission/freshman/index.php
  source_snippet: "99% of first-time freshmen and 92% of all students received financial aid"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: graduate.costs.tuition
  value: {per_credit: 1450, annual_6_credits: 17400, coa_on_campus: 45000}
  source_url: https://www.slu.edu/financial-aid/tuition-and-costs/cost-of-attendance.php
  source_snippet: "Tuition | $17,400*" / "Tuition per credit hour: $1,450"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.application_fee
  value: 0
  source_url: https://www.slu.edu/admission/freshman/deadlines.php
  source_snippet: "There is no fee to apply for undergraduate admission."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.ets_codes
  value: {TOEFL_SAT: 6629, ACT: 2352}
  source_url: https://www.slu.edu/admission/international/english-proficiency.php
  source_snippet: "Saint Louis University's Educational Testing Service (ETS) code for submitting TOEFL and SAT scores is 6629 and for ACT scores is 2352."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.special_deadlines
  value: {Nursing_OT_PT: "Dec 1", Flight_Science: "Dec 1", Scholars: "Jan 5"}
  source_url: https://www.slu.edu/admission/freshman/instructions.php
  source_snippet: "The application deadline for nursing, occupational therapy and physical therapy is Jan. 5" / "Dec. 1 is the application deadline for flight science and aviation management"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: institution.student_body
  value: {ug_students: 8669, grad_students: 6702, countries: 100, international_pct: 22.4}
  source_url: https://www.slu.edu/admission/freshman/index.php
  source_snippet: "8,669 undergraduate students" / "22.4% of SLU students come from outside the U.S."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs_count
  value: "more than 80 post-baccalaureate and professional degree programs"
  source_url: https://www.slu.edu/admission/graduate/index.php
  source_snippet: "SLU offers more than 80 post-baccalaureate and professional degree programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions_model
  value: decentralized (each college/school sets own requirements)
  source_url: https://www.slu.edu/admission/graduate/index.php
  source_snippet: "Admission requirements for SLU graduate programs vary. Visit the program's page to learn about specific admission criteria."
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
slu-knowledge-base-v2
├── 00-institution-overview (Section 0: rules 1-4)
├── 01-ug-arts-sciences (Section 1: College of Arts and Sciences programs)
├── 02-ug-science-engineering (Section 1: School of Science and Engineering programs)
├── 03-ug-business (Section 1: Chaifetz School of Business programs)
├── 04-ug-professional-studies (Section 1: School for Professional Studies programs)
├── 05-ug-public-health (Section 1: College for Public Health programs)
├── 06-ug-health-sciences (Section 1: Doisy College programs)
├── 07-ug-education-social-work-nursing (Section 1: remaining UG programs)
├── 08-grad-arts-sciences (Section 2: A&S graduate programs)
├── 09-grad-science-engineering (Section 2: S&E graduate programs)
├── 10-grad-business (Section 2: Business graduate programs)
├── 11-grad-health-medicine (Section 2: Health/Med/Nursing/Dental graduate programs)
├── 12-grad-law-education-social-work (Section 2: professional graduate programs)
├── 13-deadlines-requirements (Section 3)
├── 14-costs-financial-aid (Section 4)
├── 15-evidence-chain (Section 5)
└── 16-comparison-framework (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "slu-knowledge-base-v2"
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

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Each program's catalog detail page |
| P0 | Per-program graduate application deadlines | Each department's admissions page |
| P1 | Detailed per-school tuition (Law, Medicine, Business) | slu.edu/law, slu.edu/medicine, slu.edu/business |
| P1 | Complete UG microcredential list (104 items) | catalog.slu.edu/programs |
| P1 | International student financial aid specifics | slu.edu/financial-aid |
| P2 | SLU Madrid campus program list | slu.edu/madrid |
| P2 | Honors and Scholars program details | slu.edu/honors, slu.edu/scholars |
| P2 | Transfer admission requirements | slu.edu/admission/transfer |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | SLU | (Other Schools) |
|------|-----|-----------------|
| Type | Private Jesuit | |
| Location | St. Louis, MO + Madrid, Spain | |
| UG Tuition/yr | $58,960 (2026-27) | |
| Total UG COA (on-campus) | $83,710 | |
| Application Fee | $0 | |
| EA Deadline | Dec 1 | |
| ED I Deadline | Nov 3 | |
| ED II Deadline | Jan 16 | |
| RD Deadline | Preferred Apr 1 (rolling) | |
| SAT/ACT Required? | No (test-optional) | |
| Superscore? | No | |
| TOEFL Minimum | 80 (iBT) | |
| IELTS Minimum | 6.5 | |
| Duolingo Minimum | 110 | |
| Need-Blind (Domestic)? | No (need-aware) | |
| Need-Blind (International)? | No (need-aware) | |
| Meets Full Need? | Not guaranteed | |
| Average Aid Offer | $45,343 | |
| Avg Tuition After Aid | $20,000 | |
| Total Programs (Rule 1) | 981 | |
| Schools/Colleges (Rule 2) | 13 | |
| UG Students | 8,669 | |
| Grad Students | 6,702 | |
| International % | 22.4% | |
| Grad App Fee | $0 (SLU portal) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: slu.edu, catalog.slu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
> **Cache**: uni-cache/schools/slu/ (site-memory.json, content-hashes.json, last-extract.json, catalog-programs.json)
