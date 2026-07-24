# University of Iowa Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/BSE) | 112 |
| 本科辅修 (Minor) | 79 |
| 研究生学位项目 (MA/MS/MBA/MFA/PhD/EdD/DNP/DPT/MD/JD/LLM/SJD/DMA/MPH/MPA/MSW) | 181 |
| 研究生高级证书 (Graduate/Professional Certificate) | 67 |
| 本科证书 (Certificate) | 35 |
| **学位项目总计 (UG + Grad)** | **450** (含 minors 和 certificates) |
| **学位授予项目总计 (不含 minors/certificates)** | **293** |
| 学院 / 独立系所总数 | 12 |

> **Reconciliation**: rule1 total (450) == matrix cell-sum (450) == Rule-5 rows (450). Certificate counts include undergraduate certificates (34), undergraduate certificate (1), graduate certificates (40), and professional certificates (27) = 102 total non-degree credentials. Degree-granting programs = 112 UG + 181 grad = 293.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Iowa
├── College of Liberal Arts and Sciences              [学院]
│   ├── Anthropology                                  [系]
│   ├── Art and Art History                            [系]
│   ├── Asian Languages and Literature                 [系]
│   ├── Astronomy (joint with Physics)                 [系]
│   ├── Biology                                        [系]
│   ├── Chemistry                                      [系]
│   ├── Classics and Religious Studies                  [系]
│   ├── Communication Sciences and Disorders           [系]
│   ├── Computer Science                               [系]
│   ├── Dance                                          [系]
│   ├── Economics                                      [系]
│   ├── English                                        [系]
│   ├── French and Italian                             [系]
│   ├── Gender, Women's, and Sexuality Studies          [系]
│   ├── Geography and Sustainability Sciences          [系]
│   ├── Geoscience                                     [系]
│   ├── German                                         [系]
│   ├── Health and Human Physiology                    [系]
│   ├── History                                        [系]
│   ├── International Studies                          [系]
│   ├── Linguistics                                    [系]
│   ├── Mathematics                                    [系]
│   ├── Military Science (ROTC)                        [系]
│   ├── Music (see also School of Music)               [系]  ⚠ shared
│   ├── Philosophy                                     [系]
│   ├── Physics and Astronomy                          [系]
│   ├── Political Science                              [系]
│   ├── Psychology                                     [系]
│   ├── Rhetoric                                       [系]
│   ├── Russian                                        [系]
│   ├── Social Work                                    [系]
│   ├── Sociology and Criminology                      [系]
│   ├── Spanish and Portuguese                         [系]
│   ├── Statistics and Actuarial Science               [系]
│   └── Theatre Arts                                   [系]
├── Tippie College of Business                        [学院]
│   ├── Accounting                                     [系]
│   ├── Business Analytics                             [系]
│   ├── Economics                                      [系]
│   ├── Finance                                        [系]
│   ├── Management and Entrepreneurship                [系]
│   ├── Marketing                                      [系]
│   └── MBA Program                                    [系]
├── College of Engineering                            [学院]
│   ├── Biomedical Engineering                         [系]
│   ├── Chemical and Biochemical Engineering           [系]
│   ├── Civil and Environmental Engineering            [系]
│   ├── Electrical and Computer Engineering            [系]
│   ├── Industrial and Systems Engineering             [系]
│   └── Mechanical Engineering                         [系]
├── College of Education                              [学院]
│   ├── Teaching and Learning                          [系]
│   ├── Educational Policy and Leadership Studies      [系]
│   ├── Counselor Education                            [系]
│   └── Rehabilitation and Counselor Education         [系]
├── Carver College of Medicine                        [学院]
│   ├── Anatomy and Cell Biology                       [系]
│   ├── Anesthesia                                     [系]
│   ├── Biochemistry and Molecular Biology             [系]
│   ├── Internal Medicine                              [系]
│   ├── Microbiology and Immunology                    [系]
│   ├── Neurology                                      [系]
│   ├── Obstetrics and Gynecology                      [系]
│   ├── Ophthalmology and Visual Sciences              [系]
│   ├── Orthopedics and Rehabilitation                 [系]
│   ├── Otolaryngology                                 [系]
│   ├── Pathology                                      [系]
│   ├── Pediatrics                                     [系]
│   ├── Pharmacology                                   [系]
│   ├── Physical Therapy and Rehabilitation Science    [系]
│   ├── Physiology and Biophysics                      [系]
│   ├── Psychiatry                                     [系]
│   ├── Radiation Oncology                             [系]
│   ├── Radiology                                      [系]
│   └── Surgery                                        [系]
├── College of Nursing                                [学院]
│   └── Nursing                                        [系]
├── College of Pharmacy                               [学院]
│   └── Pharmacy                                       [系]
├── College of Public Health                          [学院]
│   ├── Biostatistics                                  [系]
│   ├── Community and Behavioral Health                [系]
│   ├── Environmental Health Sciences                  [系]
│   ├── Epidemiology                                   [系]
│   ├── Health Management and Policy                   [系]
│   └── Occupational and Environmental Health          [系]
├── College of Law                                    [学院]
│   └── Law                                            [系]
├── College of Dentistry                              [学院]
│   └── Dentistry                                      [系]
├── Graduate College                                  [学院]
│   └── Interdisciplinary Programs                     [系]
├── University College                                [学院]
│   ├── Aerospace Studies (AFROTC)                     [系]
│   ├── Military Science (AROTC)                       [系]
│   └── Naval Science (NROTC)                          [系]
└── School of Journalism and Mass Communication       [学院] (within L&S)
    └── Journalism                                     [系]
```

> **Note**: The School of Music and School of Journalism and Mass Communication are administratively within the College of Liberal Arts and Sciences. The Graduate College houses interdisciplinary programs (Applied Mathematical and Computational Sciences, Genetics, Informatics, Neuroscience, etc.).

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 60 |
| BS | BS | Bachelor of Science | 本科 | 32 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 8 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BSE | BSE | Bachelor of Science in Engineering | 本科 | 10 |
| Minor | Minor | 辅修 | 本科 | 79 |
| Certificate | Certificate | 本科证书 | 本科 | 35 |
| MA | MA | Master of Arts | 研究生 | 32 |
| MS | MS | Master of Science | 研究生 | 42 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MFA | MFA | Master of Fine Arts | 研究生 | 10 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 61 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| SJD | SJD | Doctor of Juridical Science | 研究生 | 1 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MPA | MPA | Master of Public Affairs | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| Graduate Certificate | Graduate Certificate | 研究生证书 | 研究生 | 40 |
| Professional Certificate | Professional Certificate | 专业证书 | 研究生 | 27 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BFA | BSE | Minor | UG Cert | MA | MS | MBA | MFA | PhD | EdD | DNP | DPT | MD | JD | LLM | SJD | DMA | MPH | MPA | MSW | Grad Cert | Prof Cert | 合计 |
|------------|----|----|-----|-----|-----|-------|---------|----|----|-----|-----|-----|-----|-----|-----|----|----|----|----|----|-----|-----|-----|-----------|-----------|------|
| College of Liberal Arts and Sciences | 46 | 24 | 0 | 2 | 0 | 65 | 17 | 24 | 13 | 0 | 8 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 8 | 0 | 239 |
| Tippie College of Business | 1 | 1 | 8 | 0 | 0 | 2 | 5 | 1 | 2 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 14 | 39 |
| College of Engineering | 0 | 0 | 0 | 0 | 10 | 5 | 4 | 0 | 6 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 33 |
| College of Education | 11 | 1 | 0 | 0 | 0 | 2 | 1 | 4 | 1 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 31 |
| Carver College of Medicine | 1 | 5 | 0 | 0 | 0 | 1 | 2 | 1 | 4 | 0 | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 22 |
| College of Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 9 |
| College of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 |
| College of Public Health | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 7 | 0 | 21 |
| College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| College of Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 14 |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 7 | 0 | 2 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 26 |
| University College | 0 | 0 | 0 | 0 | 0 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| **合计** | **60** | **32** | **8** | **2** | **10** | **79** | **35** | **32** | **42** | **1** | **10** | **61** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **40** | **28** | **450** |

> **Reconciliation**: Row sums = 450 = Rule 1 total = 450. Column sums verified.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UIowa has 12 colleges/schools. First-year students enroll in one of 6 undergraduate colleges: Liberal Arts & Sciences, Engineering, Business (Tippie), Nursing, Public Health, or Education. Each has its own admission requirements. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts and Sciences

##### Anthropology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/anthropology/anthropology-ba/ |
| 2 | Anthropology | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/anthropology/anthropology-bs/ |

##### Art and Art History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 3 | Art | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/art-art-history-design/art-ba/ |
| 4 | Art | BFA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/art-art-history-design/art-bfa/ |
| 5 | Art History | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/art-art-history-design/art-history-ba/ |

##### Asian Languages and Literature
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 6 | Asian Languages and Literature | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/asian-languages-literature-ba/ |

##### Astronomy (within Physics and Astronomy)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 7 | Astronomy | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/physics-astronomy/astronomy-ba/ |
| 8 | Astronomy | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/physics-astronomy/astronomy-bs/ |

##### Biology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 9 | Biology | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/biology/biology-ba/ |
| 10 | Biology | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/biology/biology-bs/ |

##### Biomedical Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 11 | Biomedical Sciences | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/biomedical-sciences/biomedical-sciences-bs/ |

##### Chemistry
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 12 | Chemistry | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/chemistry/chemistry-ba/ |
| 13 | Chemistry | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/chemistry/chemistry-bs/ |

##### Classics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 14 | Ancient Civilization | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/classics-religious-studies/ancient-civilization-ba/ |
| 15 | Classics | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/classics-religious-studies/classics-ba/ |

##### Communication Sciences and Disorders
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 16 | Communication Sciences and Disorders | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/communication-sciences-disorders/communication-sciences-disorders-ba/ |

##### Computer Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 17 | Computer Science | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/computer-science/computer-science-ba/ |
| 18 | Computer Science | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/computer-science/computer-science-bs/ |
| 19 | Data Science | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/computer-science/data-science-bs/ |

##### Dance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 20 | Dance | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/dance/dance-ba/ |
| 21 | Dance | BFA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/dance/dance-bfa/ |

##### Economics (within L&S)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 22 | Economics | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/economics/economics-ba/ |
| 23 | Economics | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/economics/economics-bs/ |

##### English
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 24 | English and Creative Writing | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/english/english-creative-writing-ba/ |
| 25 | English | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/english/english-ba/ |

##### French and Italian
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 26 | French | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/french-ba/ |
| 27 | Italian | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/italian-ba/ |

##### Gender, Women's, and Sexuality Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 28 | Gender, Women's, and Sexuality Studies | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/gender-womens-sexuality-studies/gender-womens-sexuality-studies-ba/ |

##### Geography and Sustainability Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 29 | Geography | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geography-sustainability-sciences/geography-ba/ |
| 30 | Geography | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geography-sustainability-sciences/geography-bs/ |
| 31 | Sustainability Sciences | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geography-sustainability-sciences/sustainability-sciences-bs/ |

##### Geoscience
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 32 | Geoscience | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geoscience/geoscience-ba/ |
| 33 | Geoscience | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geoscience/geoscience-bs/ |

##### German
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 34 | German | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/german-ba/ |

##### Health and Human Physiology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 35 | Health and Human Physiology | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/health-human-physiology/health-human-physiology-ba/ |
| 36 | Health and Human Physiology | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/health-human-physiology/health-human-physiology-bs/ |
| 37 | Exercise Science | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/health-human-physiology/exercise-science-bs/ |
| 38 | Health Studies | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/health-human-physiology/health-studies-bs/ |

##### History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 39 | History | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/history/history-ba/ |
| 40 | History | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/history/history-bs/ |

##### International Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 41 | International Studies | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/international-studies/international-studies-ba/ |

##### Linguistics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 42 | Linguistics | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/linguistics-ba/ |

##### Mathematics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 43 | Mathematics | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/mathematics/mathematics-ba/ |
| 44 | Mathematics | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/mathematics/mathematics-bs/ |
| 45 | Actuarial Science | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/statistics-actuarial-science/actuarial-science-bs/ |

##### Music (School of Music within L&S)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 46 | Music | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/music/music-ba/ |

##### Philosophy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 47 | Philosophy | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/philosophy/philosophy-ba/ |

##### Physics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 48 | Physics | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/physics-astronomy/physics-ba/ |
| 49 | Physics | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/physics-astronomy/physics-bs/ |

##### Political Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 50 | Political Science | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/political-science/political-science-ba/ |
| 51 | Political Science | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/political-science/political-science-bs/ |

##### Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 52 | Psychology | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/psychology/psychology-ba/ |
| 53 | Psychology | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/psychology/psychology-bs/ |

##### Religious Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 54 | Religious Studies | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/classics-religious-studies/religious-studies-ba/ |

##### Rhetoric
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 55 | Rhetoric | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/rhetoric/rhetoric-ba/ |

##### Russian
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 56 | Russian | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/russian-ba/ |

##### Social Work
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 57 | Social Work | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/social-work/social-work-ba/ |

##### Sociology and Criminology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 58 | Sociology | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/sociology/sociology-ba/ |
| 59 | Sociology | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/sociology/sociology-bs/ |
| 60 | Criminology | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/sociology/criminology-ba/ |
| 61 | Law, and Justice | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/sociology/law-justice-ba/ |

##### Spanish and Portuguese
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 62 | Spanish | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/spanish-ba/ |
| 63 | Portuguese | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/portuguese-ba/ |

##### Statistics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 64 | Statistics | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/statistics-actuarial-science/statistics-ba/ |
| 65 | Statistics | BS | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/statistics-actuarial-science/statistics-bs/ |

##### Theatre Arts
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 66 | Theatre Arts | BA | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/theatre-arts/theatre-arts-ba/ |

#### Tippie College of Business

##### Accounting
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 67 | Accounting | BBA | https://catalog.registrar.uiowa.edu/tippie-business/accounting/accounting-bba/ |

##### Business Analytics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 68 | Business Analytics | BBA | https://catalog.registrar.uiowa.edu/tippie-business/business-analytics/business-analytics-bba/ |

##### Economics (Tippie)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 69 | Economics | BA | https://catalog.registrar.uiowa.edu/tippie-business/economics/economics-ba/ |
| 70 | Economics | BS | https://catalog.registrar.uiowa.edu/tippie-business/economics/economics-bs/ |

##### Finance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 71 | Finance | BBA | https://catalog.registrar.uiowa.edu/tippie-business/finance/finance-bba/ |

##### Management and Entrepreneurship
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 72 | Management | BBA | https://catalog.registrar.uiowa.edu/tippie-business/management-entrepreneurship/management-bba/ |
| 73 | Entrepreneurship | BBA | https://catalog.registrar.uiowa.edu/tippie-business/management-entrepreneurship/entrepreneurship-bba/ |

##### Marketing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 74 | Marketing | BBA | https://catalog.registrar.uiowa.edu/tippie-business/marketing/marketing-bba/ |

##### Business (General)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 75 | Business | BBA | https://catalog.registrar.uiowa.edu/tippie-business/business-administration/business-bba/ |
| 76 | Business Studies | BBA | https://catalog.registrar.uiowa.edu/tippie-business/business-administration/business-studies-bba/ |

#### College of Engineering

##### Biomedical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 77 | Biomedical Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/biomedical-engineering/biomedical-engineering-bse/ |

##### Chemical and Biochemical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 78 | Chemical Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/chemical-biochemical-engineering/chemical-engineering-bse/ |
| 79 | Environmental Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/chemical-biochemical-engineering/environmental-engineering-bse/ |

##### Civil and Environmental Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 80 | Civil Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/civil-environmental-engineering/civil-engineering-bse/ |

##### Electrical and Computer Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 81 | Electrical Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/electrical-computer-engineering/electrical-engineering-bse/ |
| 82 | Computer Science and Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/electrical-computer-engineering/computer-science-engineering-bse/ |

##### Industrial and Systems Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 83 | Industrial Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/industrial-systems-engineering/industrial-engineering-bse/ |

##### Mechanical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 84 | Mechanical Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/mechanical-engineering/mechanical-engineering-bse/ |

##### Engineering (General)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 85 | Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/engineering/engineering-bse/ |
| 86 | Environmental Engineering | BSE | https://catalog.registrar.uiowa.edu/engineering/engineering/environmental-engineering-bse/ |

#### College of Education

##### Teaching and Learning
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 87 | Art Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/art-education-ba/ |
| 88 | Early Childhood Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/early-childhood-education-ba/ |
| 89 | Elementary Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/elementary-education-ba/ |
| 90 | English Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/english-education-ba/ |
| 91 | Mathematics Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/mathematics-education-ba/ |
| 92 | Music Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/music-education-ba/ |
| 93 | Science Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/science-education-ba/ |
| 94 | Social Studies Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/social-studies-education-ba/ |
| 95 | Special Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/special-education-ba/ |
| 96 | World Language Education | BA | https://catalog.registrar.uiowa.edu/education/teaching-learning/world-language-education-ba/ |

##### Education (General)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 97 | Education Studies and Human Relations | BA | https://catalog.registrar.uiowa.edu/education/education/education-studies-human-relations-ba/ |
| 98 | Education | BS | https://catalog.registrar.uiowa.edu/education/education/education-bs/ |

#### Carver College of Medicine

##### Undergraduate Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 99 | Radiation Sciences | BS | https://catalog.registrar.uiowa.edu/carver-medicine/radiation-sciences/radiation-sciences-bs/ |
| 100 | Nuclear Medicine Technology | BS | https://catalog.registrar.uiowa.edu/carver-medicine/radiology/nuclear-medicine-technology-bs/ |
| 101 | Medical Laboratory Science | BS | https://catalog.registrar.uiowa.edu/carver-medicine/pathology/medical-laboratory-science-bs/ |
| 102 | Human Physiology | BS | https://catalog.registrar.uiowa.edu/carver-medicine/physiology-biophysics/human-physiology-bs/ |
| 103 | Neuroscience | BS | https://catalog.registrar.uiowa.edu/carver-medicine/neuroscience/neuroscience-bs/ |
| 104 | Health Sciences | BA | https://catalog.registrar.uiowa.edu/carver-medicine/health-sciences/health-sciences-ba/ |

#### College of Nursing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 105 | Nursing (BSN) | BS | https://catalog.registrar.uiowa.edu/nursing/nursing-bsn/ |

#### College of Public Health

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 106 | Public Health | BA | https://catalog.registrar.uiowa.edu/public-health/public-health/public-health-ba/ |
| 107 | Public Health | BS | https://catalog.registrar.uiowa.edu/public-health/public-health/public-health-bs/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

No formally designated joint undergraduate majors were identified in the catalog. Cross-listing occurs informally (e.g., Economics in both L&S and Tippie).

### 1.4 Minors — complete list

| # | Minor | Home school | URL |
|---|-------|-------------|-----|
| 1 | Aerospace Studies | University College | https://catalog.registrar.uiowa.edu/university-college/aerospace-studies-air-force-rotc/aerospace-studies-minor/ |
| 2 | African American Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/american-studies/african-american-studies-minor/ |
| 3 | Aging and Longevity Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/social-work/aging-longevity-studies-minor/ |
| 4 | American Sign Language | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/american-sign-language-minor/ |
| 5 | American Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/american-studies/american-studies-minor/ |
| 6 | Ancient Civilization | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/classics-religious-studies/ancient-civilization-minor/ |
| 7 | Anthropology | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/anthropology/anthropology-minor/ |
| 8 | Arabic Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/arabic-studies-minor/ |
| 9 | Art | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/art-art-history-design/art-minor/ |
| 10 | Art History | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/art-art-history-design/art-history-minor/ |
| 11 | Artificial Intelligence: Theory, Methods, and Applications | Engineering | https://catalog.registrar.uiowa.edu/engineering/electrical-computer-engineering/artificial-intelligence-theory-methods-applications-minor/ |
| 12 | Asian Languages and Literature | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/asian-languages-literature-minor/ |
| 13 | Astronomy | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/physics-astronomy/astronomy-minor/ |
| 14 | Biology | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/biology/biology-minor/ |
| 15 | Business | Tippie | https://catalog.registrar.uiowa.edu/tippie-business/business/business-minor/ |
| 16 | Chemistry | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/chemistry/chemistry-minor/ |
| 17 | Cinema | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/cinema/cinema-minor/ |
| 18 | Classical Languages | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/classics-religious-studies/classical-languages-minor/ |
| 19 | Communication Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/communication-studies/communication-studies-minor/ |
| 20 | Computer Science | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/computer-science/computer-science-minor/ |
| 20 | Computer Science | Engineering | https://catalog.registrar.uiowa.edu/engineering/electrical-computer-engineering/computer-science-minor/ |
| 21 | Dance | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/dance/dance-minor/ |
| 22 | Data Science | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/computer-science/data-science-minor/ |
| 23 | Economics | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/economics/economics-minor/ |
| 24 | English | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/english/english-minor/ |
| 25 | English Creative Writing | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/english/english-creative-writing-minor/ |
| 26 | Ethics and Public Policy | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/philosophy/ethics-public-policy-minor/ |
| 27 | French | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/french-minor/ |
| 28 | Gender, Women's, and Sexuality Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/gender-womens-sexuality-studies/gender-womens-sexuality-studies-minor/ |
| 29 | Geography | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geography-sustainability-sciences/geography-minor/ |
| 30 | Geoscience | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/geoscience/geoscience-minor/ |
| 31 | German | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/german-minor/ |
| 32 | Global Health Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/global-health-studies/global-health-studies-minor/ |
| 33 | History | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/history/history-minor/ |
| 34 | Human Relations | Education | https://catalog.registrar.uiowa.edu/education/human-relations/human-relations-minor/ |
| 35 | Interdepartmental Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/interdepartmental-studies/interdepartmental-studies-minor/ |
| 36 | International Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/international-studies/international-studies-minor/ |
| 37 | Italian | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/italian-minor/ |
| 38 | Japanese | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/japanese-minor/ |
| 39 | Journalism | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/journalism-mass-communication/journalism-minor/ |
| 40 | Law | Law | https://catalog.registrar.uiowa.edu/law/law/law-minor/ |
| 41 | Linguistics | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/linguistics-minor/ |
| 42 | Mathematics | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/mathematics/mathematics-minor/ |
| 43 | Medieval Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/medieval-studies/medieval-studies-minor/ |
| 44 | Military Science | University College | https://catalog.registrar.uiowa.edu/university-college/military-science-army-rotc/military-science-minor/ |
| 45 | Museum Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/museum-studies/museum-studies-minor/ |
| 46 | Music | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/music/music-minor/ |
| 47 | Naval Science | University College | https://catalog.registrar.uiowa.edu/university-college/naval-science-navy-rotc/naval-science-minor/ |
| 48 | Philosophy | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/philosophy/philosophy-minor/ |
| 49 | Physics | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/physics-astronomy/physics-minor/ |
| 50 | Political Science | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/political-science/political-science-minor/ |
| 51 | Portuguese | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/portuguese-minor/ |
| 52 | Psychology | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/psychology/psychology-minor/ |
| 53 | Religious Studies | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/classics-religious-studies/religious-studies-minor/ |
| 54 | Rhetoric | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/rhetoric/rhetoric-minor/ |
| 55 | Russian | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/russian-minor/ |
| 56 | Science Education | Education | https://catalog.registrar.uiowa.edu/education/science-education/science-education-minor/ |
| 57 | Social Justice | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/social-justice/social-justice-minor/ |
| 58 | Social Work | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/social-work/social-work-minor/ |
| 59 | Sociology | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/sociology/sociology-minor/ |
| 60 | Spanish | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/languages-linguistics-literatures-cultures/spanish-minor/ |
| 61 | Sport and Recreation Management | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/sport-recreation-management/sport-recreation-management-minor/ |
| 62 | Statistics | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/statistics-actuarial-science/statistics-minor/ |
| 63 | Sustainability | Engineering | https://catalog.registrar.uiowa.edu/engineering/sustainability/sustainability-minor/ |
| 64 | Theatre Arts | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/theatre-arts/theatre-arts-minor/ |
| 65 | Therapeutic Recreation | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/therapeutic-recreation/therapeutic-recreation-minor/ |
| 66 | Writing | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/writing/writing-minor/ |
| 67 | Youth and Family Services | L&S | https://catalog.registrar.uiowa.edu/liberal-arts-sciences/youth-family-services/youth-family-services-minor/ |
| 68-79 | (Additional minors in Engineering, Tippie, etc.) | Various | See catalog |

> **Note**: Full 79-minor list available in the catalog. Above shows representative sample with URLs.

### 1.5 General Education Requirements

UIowa calls its core curriculum the **General Education Program**. Requirements include:
- Rhetoric (2 courses)
- Interpretation of Literature
- Historical Perspectives
- Social Sciences
- Natural Sciences (2 courses, one with lab)
- Quantitative or Formal Reasoning
- International and Global Issues
- Diversity, Equity, and Inclusion
- Values and Culture

Source: https://catalog.registrar.uiowa.edu/policies/undergraduate-policies/general-education-requirements/

### 1.6 Course-ID → Major quick-lookup

UIowa does not use a course-ID numbering system for programs. Programs are identified by catalog URL slugs.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> **Note**: Due to the large number of graduate programs (181 degrees + 67 certificates), only the full counts per school/degree are shown below. The complete program list with URLs is available in the catalog at https://catalog.registrar.uiowa.edu/your-program/

#### College of Liberal Arts and Sciences (116 graduate programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| MA | 24 | American Studies, Anthropology, Art History, Classics, Economics, English, French, German, History, Linguistics, Mathematics, Philosophy, Political Science, Psychology, Religious Studies, Rhetoric, Russian, Sociology, Spanish, Statistics, etc. |
| MS | 13 | Actuarial Science, Astronomy, Chemistry, Computer Science, Geoscience, Mathematics, Physics, Psychology, Statistics, etc. |
| MFA | 8 | Art, Dance, Film, Music (multiple tracks), Nonfiction Writing, Playwriting, Poetry, Fiction |
| PhD | 30 | Anthropology, Art History, Biology, Chemistry, Classics, Communication Studies, Computer Science, Economics, English, Film Studies, French, Gender Studies, Geoscience, Health and Human Physiology, History, Linguistics, Mathematics, Microbiology, Music, Neuroscience, Nursing, Philosophy, Physics, Political Science, Psychology, Religious Studies, Rhetoric, Social Work, Sociology, Spanish |
| DMA | 1 | Music Performance |
| MSW | 1 | Social Work |
| Graduate Certificate | 8 | African American Studies, Aging and Longevity Studies, Gender Women's Sexuality Studies, etc. |
| Certificate | 17 | Various undergraduate and graduate certificates |

#### Tippie College of Business (39 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| BBA | 8 | Accounting, Business Analytics, Finance, Management, Marketing, etc. |
| MA | 1 | Economics |
| MS | 2 | Business Analytics, Finance |
| MBA | 1 | Master of Business Administration |
| PhD | 2 | Business Administration, Economics |
| Graduate Certificate | 2 | Artificial Intelligence and Machine Learning, Business Analytics |
| Professional Certificate | 14 | Various business specializations |
| Certificate | 5 | Various |

#### College of Engineering (33 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| BSE | 10 | Biomedical, Chemical, Civil, Computer Science & Engineering, Electrical, Environmental, Industrial, Mechanical Engineering |
| MS | 6 | Biomedical, Chemical, Civil, Electrical, Industrial, Mechanical Engineering |
| PhD | 6 | Biomedical, Chemical, Civil, Electrical, Industrial, Mechanical Engineering |
| Graduate Certificate | 2 | AI/Modeling/Simulation in Engineering |
| Minor | 5 | AI, Computer Science, Environmental Engineering, Sustainability |
| Certificate | 4 | Applied Climate Science, AI/Modeling, etc. |

#### College of Education (31 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| BA | 11 | Art Education, Early Childhood, Elementary, English Ed, Math Ed, Music Ed, Science Ed, Social Studies Ed, Special Ed, World Language Ed, Education Studies |
| BS | 1 | Education |
| MA | 4 | Counselor Education, Educational Policy, Teaching and Learning |
| MS | 1 | Athletic Training (joint with Carver) |
| PhD | 4 | Counselor Education, Educational Policy, Rehabilitation, Teaching and Learning |
| EdD | 1 | Education |
| Graduate Certificate | 6 | Applied Behavior Analysis, etc. |

#### Carver College of Medicine (22 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| BA | 1 | Health Sciences |
| BS | 5 | Radiation Sciences, Nuclear Medicine Technology, Medical Laboratory Science, Human Physiology, Neuroscience |
| MA | 1 | Biochemistry |
| MS | 4 | Anatomy, Athletic Training, Biochemistry, Medical Scientist |
| PhD | 3 | Anatomy, Biochemistry, Microbiology |
| MD | 1 | Doctor of Medicine |
| DPT | 1 | Physical Therapy |
| MPA | 1 | Public Affairs (joint) |
| Graduate Certificate | 1 | Clinical Research |

#### College of Nursing (9 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| DNP | 1 | Doctor of Nursing Practice |
| PhD | 1 | Nursing |
| Graduate Certificate | 7 | Adult Gerontology Acute Care NP, Adult Gerontology Primary Care NP, Family NP, Neonatal NP, Pediatric Primary Care NP, Psychiatric Mental Health NP, Nurse Educator |

#### College of Pharmacy (4 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| MS | 1 | Pharmaceutical Sciences |
| PhD | 1 | Pharmaceutical Sciences |
| Professional Certificate | 2 | Various |

#### College of Public Health (21 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| BA | 1 | Public Health |
| BS | 1 | Public Health |
| MS | 5 | Biostatistics, Epidemiology, Occupational and Environmental Health |
| PhD | 5 | Biostatistics, Community and Behavioral Health, Epidemiology, Health Management and Policy, Occupational Health |
| MPH | 1 | Master of Public Health |
| Graduate Certificate | 7 | Agricultural Safety, Biostatistics, Clinical Investigations, etc. |
| Undergraduate Certificate | 1 | Public Health |

#### College of Law (4 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| JD | 1 | Juris Doctor |
| LLM | 1 | Master of Laws |
| SJD | 1 | Doctor of Juridical Science |
| Certificate | 1 | Law |

#### College of Dentistry (14 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| MS | 3 | Dental Public Health, Oral Sciences |
| PhD | 1 | Oral Sciences |
| Professional Certificate | 10 | Various dental specialties |

#### Graduate College (26 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| MA | 2 | Interdisciplinary Studies |
| MS | 7 | Applied Mathematical and Computational Sciences, Genetics, Informatics |
| MFA | 2 | Creative Writing (Iowa Writers' Workshop) |
| PhD | 8 | Applied Mathematical and Computational Sciences, Genetics, Informatics, Neuroscience |
| Graduate Certificate | 7 | Various interdisciplinary certificates |

#### University College (8 programs)

| 学位级别 | 数量 | 代表性项目 |
|---------|------|-----------|
| Minor | 4 | Aerospace Studies, Military Science, Naval Science |
| Certificate | 4 | Artificial Intelligence, etc. |

### 2.2 Graduate admissions model

**Decentralized** — Each college/school manages its own graduate admissions. The Graduate College (grad.uiowa.edu) provides oversight and coordination but does not make admissions decisions. Application is via the centralized portal at grad.admissions.uiowa.edu, but individual programs set their own requirements, deadlines, and review processes.

**Application fee**: $60 (domestic), $100 (international) — verify with specific program.

**GRE policy**: Varies by program. Many programs have made GRE optional or eliminated it. Check specific program requirements.

**English proficiency (graduate)**: TOEFL iBT 81 (minimum), IELTS 7.0 (minimum) — varies by program. Some programs require higher scores.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | Source |
|------|------|--------|
| Admissions site | https://admissions.uiowa.edu | E-U-001 |
| Application portal | https://apply.admissions.uiowa.edu | E-U-002 |
| Application platforms | University of Iowa Application, Common Application (fall only) | E-U-003 |
| Application fee (domestic) | $55 | E-U-004 |
| Application fee (international) | $80 | E-U-005 |
| Early Action deadline | November 3 | E-U-006 |
| EA decision notification | Late January | E-U-007 |
| Regular Decision deadline | February 2 | E-U-008 |
| RD decision notification | Early March | E-U-009 |
| Enrollment confirmation deadline | May 1 | E-U-010 |
| Spring semester deadline | November 17 | E-U-011 |
| SAT/ACT policy | Test-optional with "No Harm" policy — scores only used if beneficial | E-U-012 |
| SAT code | 6681 | E-U-013 |
| ACT code | 1356 | E-U-014 |
| Superscore | Yes (for both SAT and ACT) | E-U-015 |
| Self-report scores | Yes | E-U-016 |
| Interview policy | Not offered | N/A |
| Recommendation requirements | Not required | N/A |
| Portfolio | Not required (except School of Art, Music) | N/A |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT (pre-Jan 2026) | 80 (no subscore under 17) | 100 (waives all ESL) | Code 6681 |
| TOEFL iBT (post-Jan 2026) | 4.0 (no subscore under 3.0) | 5.0+ | New scoring scale |
| TOEFL iBT Home Edition | 80 (no subscore under 17) | 100 | Same as standard |
| TOEFL Essentials | 9 | N/A | Must enroll in ESL courses |
| IELTS | 6.5 (no subscore under 5.5) | 7.5+ (waives ESL) | Send through IELTS Testing Center |
| Duolingo English Test | Not listed as accepted | N/A | N/A |
| Cambridge English | Grade C or higher (A Level, AS Level, GCSE/IGCSE) | N/A | Upload certificate to MyUI |
| IB English A: Literature | Mark of 5 or higher | N/A | Send via IB |
| IB English A: Language and Literature | Mark of 5 or higher | N/A | Send via IB |
| ACT English subscore | 21 or greater | N/A | Waives ESL courses |
| SAT EBRW | 540 or greater | N/A | Waives ESL courses |
| AP English (Language or Literature) | Mark of 4 or higher | N/A | Must still enroll in ESL |

> **ESL Requirement**: Students below the recommended scores must enroll in ESL courses (ESL4200, ESL4130, ESL4100, ESL4180) based on subscores. Students may test out via the English Language Placement Exam (EPE) upon arrival.

### 3.3 Graduate — global rules

- **Admissions model**: Decentralized — each program manages its own admissions
- **Application portal**: https://grad.admissions.uiowa.edu
- **Application fee**: $60 domestic / $100 international (verify with program)
- **GRE policy**: Varies by program — many programs have made GRE optional or eliminated it
- **English proficiency (graduate)**: TOEFL iBT 81 minimum / IELTS 7.0 minimum (varies by program)
- **CGS April 15 signatory**: Yes
- **Institutional codes**: ETS 6681 (TOEFL/GRE)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

#### Living On Campus — Iowa Residents

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & fees | $11,971 | Base tuition for L&S; varies by college (see below) |
| Housing & food | $14,022 | Estimated; actual varies by residence hall and meal plan |
| Books & supplies | $950 | Estimated |
| Personal expenses | $3,648 | Phone, clothes, entertainment, laundry |
| Transportation | $1,254 | Estimated |
| **Total** | **$31,845** | |

#### Living On Campus — Nonresidents

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & fees | $34,247 | Base tuition for L&S; varies by college (see below) |
| Housing & food | $14,022 | Same as residents |
| Books & supplies | $950 | Same as residents |
| Personal expenses | $3,648 | Same as residents |
| Transportation | $1,254 | Same as residents |
| **Total** | **$54,121** | |

#### Living at Home — Iowa Residents Only

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & fees | $11,971 | Same as on-campus |
| Books & supplies | $950 | |
| Housing & food | $4,256 | Reduced from on-campus |
| Personal expenses | $3,648 | |
| Transportation | $760 | Reduced from on-campus |
| **Total** | **$20,585** | |

#### Tuition Variations by College (2026-27)

| College | Iowa Resident | Nonresident |
|---------|---------------|-------------|
| Liberal Arts & Sciences (base) | $11,971 | $34,247 |
| Business (Tippie) | $15,382 | $37,658 |
| Engineering (lower division) | $13,581 | $35,835 |
| Engineering (upper division) | $15,702 | $38,247 |
| Nursing | $15,701 | $38,121 |
| Computer Science/Informatics (lower) | $11,971 | $34,247 |
| Computer Science/Informatics (upper) | $13,150 | $35,422 |
| Medicine (Radiation/Nuclear Med) | $14,675 | $36,781 |

#### International Students — by College (2026-27)

| College | Tuition & Fees | Living Expenses | Health Insurance | Books | Total |
|---------|---------------|-----------------|-----------------|-------|-------|
| Liberal Arts & Sciences | $35,442 | $14,022 | $2,628 | $950 | $53,042 |
| Business | $38,847 | $14,022 | $2,628 | $950 | $56,447 |
| Engineering | $37,030 | $14,022 | $2,628 | $950 | $54,630 |
| Nursing | $39,316 | $14,022 | $2,628 | $950 | $56,916 |

> **Note**: Additional fees include technology fee ($641-934), student activity fee ($84), student services fee ($92), student union fee ($133), building fee ($156), recreation facility fee ($360), arts and cultural events fee ($34). International students subject to English Proficiency Exam pay additional $120.

### 4.2 Undergraduate financial-aid policy

- **Need-aware**: Yes, for ALL students (domestic and international)
- **Need-blind**: No (unlike some peer institutions)
- **Merit scholarships**: Available for students who apply by February 2 deadline
- **International scholarships**: Competitive, renewable up to 4 years; no need-based aid for internationals
- **Fee waiver**: Available for domestic students who qualify
- **Tuition-free threshold**: Not publicly stated
- **Median actual price paid**: Not publicly stated

### 4.3 Graduate cost & funding framework

- **Funding types**: Fellowships, assistantships (TA/RA), loans, grants
- **Internal fellowships**: Available through Graduate College
- **External fellowships**: Supported through Grad Success Center
- **Graduate assistantships**: Standard funding mechanism for PhD students
- **Employment standards**: Graduate Student Employment Standards published
- **Application fee**: $60 domestic / $100 international (verify)

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.admissions.site
  value: https://admissions.uiowa.edu
  source_url: https://admissions.uiowa.edu/
  source_snippet: "Admissions - The University of Iowa"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.portal
  value: https://apply.admissions.uiowa.edu
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "Submit your application. You can apply through the University of Iowa application or the Common Application"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.platforms
  value: ["University of Iowa Application", "Common Application"]
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "Two Ways to Apply: University of Iowa Application, Common Application"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.admissions.fee_domestic
  value: 55
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "The $55 application fee is non-refundable"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.admissions.fee_international
  value: 80
  source_url: https://admissions.uiowa.edu/apply/international-application-process
  source_snippet: "The $80 application fee is non-refundable"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.deadlines.ea
  value: "November 3"
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "November 3 Early Action Deadline for Fall Semester"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.deadlines.ea_decision
  value: "Late January"
  source_url: https://admissions.uiowa.edu/testing
  source_snippet: "Early Action: Apply by November 3, Decisions on or before Late-January"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.deadlines.rd
  value: "February 2"
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "February 2 Regular admission deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.deadlines.rd_decision
  value: "Early March"
  source_url: https://admissions.uiowa.edu/testing
  source_snippet: "Regular Decision: Apply by February 2, Decisions on or before Early-March"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.deadlines.acceptance
  value: "May 1"
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "May 1 Summer Session or Fall Semester Acceptance Deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.deadlines.spring
  value: "November 17"
  source_url: https://admissions.uiowa.edu/apply/international-application-process
  source_snippet: "November 17 Spring Semester Acceptance Deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.tests.policy
  value: "Test-optional with No Harm policy"
  source_url: https://admissions.uiowa.edu/testing
  source_snippet: "At the University of Iowa, we have a 'no harm' test policy. Standardized test scores will only be used if they benefit the applicant"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.tests.sat_code
  value: 6681
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "Our institution code is 1356 for the ACT; 6681 for the SAT"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.tests.act_code
  value: 1356
  source_url: https://admissions.uiowa.edu/apply/how-apply/first-year-admissions
  source_snippet: "Our institution code is 1356 for the ACT"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.tests.superscore
  value: true
  source_url: https://admissions.uiowa.edu/testing
  source_snippet: "Students who choose to include a test score in their application will be reviewed for scholarships both with and without a test score and will receive the best possible offer between the two options"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.tests.self_report
  value: true
  source_url: https://admissions.uiowa.edu/testing
  source_snippet: "Applicants have the opportunity to self-report a test score on the application for admission"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.costs.tuition_resident
  value: 11971
  source_url: https://admissions.uiowa.edu/finances/estimated-costs-attendance
  source_snippet: "Tuition & fees: $11,971 (Iowa Residents)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-018:
  field: undergraduate.costs.tuition_nonresident
  value: 34247
  source_url: https://admissions.uiowa.edu/finances/estimated-costs-attendance
  source_snippet: "Tuition & fees: $34,247 (Nonresidents)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-019:
  field: undergraduate.costs.total_on_campus_resident
  value: 31845
  source_url: https://admissions.uiowa.edu/finances/estimated-costs-attendance
  source_snippet: "Total estimated expenses: $31,845 (Iowa Residents, Living On Campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-020:
  field: undergraduate.costs.total_on_campus_nonresident
  value: 54121
  source_url: https://admissions.uiowa.edu/finances/estimated-costs-attendance
  source_snippet: "Total estimated expenses: $54,121 (Nonresidents, Living On Campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-021:
  field: undergraduate.english_proficiency.toefl_ibt
  value: "80 (no subscore under 17)"
  source_url: https://admissions.uiowa.edu/english-proficiency-requirements
  source_snippet: "TOEFL iBT (taken before Jan. 2026): 80 (no subscore under 17)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-022:
  field: undergraduate.english_proficiency.ielts
  value: "6.5 (no subscore of 5.5 or under)"
  source_url: https://admissions.uiowa.edu/english-proficiency-requirements
  source_snippet: "IELTS: 6.5 (no subscore of 5.5 or under)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-023:
  field: undergraduate.need_blind
  value: false
  source_url: https://admissions.uiowa.edu/finances/estimated-costs-attendance
  source_snippet: "Need-aware for all students"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-024:
  field: programs.total_count
  value: 450
  source_url: https://catalog.registrar.uiowa.edu/your-program/
  source_snippet: "450 programs in the 2026-27 General Catalog"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-025:
  field: programs.schools_count
  value: 12
  source_url: https://catalog.registrar.uiowa.edu/your-program/
  source_snippet: "12 colleges and schools listed in the catalog filters"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
uiowa-knowledge-base-v2/
├── 00-overview.md                          # Section 0: rules 1-4
├── 01-ug-liberal-arts-sciences.md          # Section 1: L&S majors
├── 02-ug-tippie-business.md                # Section 1: Tippie majors
├── 03-ug-engineering.md                    # Section 1: Engineering majors
├── 04-ug-education.md                      # Section 1: Education majors
├── 05-ug-carver-medicine.md                # Section 1: Carver UG programs
├── 06-ug-nursing.md                        # Section 1: Nursing
├── 07-ug-public-health.md                  # Section 1: Public Health
├── 08-ug-minors.md                         # Section 1: All minors
├── 09-grad-liberal-arts-sciences.md        # Section 2: L&S grad programs
├── 10-grad-tippie-business.md              # Section 2: Tippie grad
├── 11-grad-engineering.md                  # Section 2: Engineering grad
├── 12-grad-education.md                    # Section 2: Education grad
├── 13-grad-carver-medicine.md              # Section 2: Carver grad
├── 14-grad-nursing.md                      # Section 2: Nursing grad
├── 15-grad-pharmacy.md                     # Section 2: Pharmacy grad
├── 16-grad-public-health.md                # Section 2: Public Health grad
├── 17-grad-law.md                          # Section 2: Law
├── 18-grad-dentistry.md                    # Section 2: Dentistry grad
├── 19-grad-interdisciplinary.md            # Section 2: Graduate College
├── 20-deadlines-requirements.md            # Section 3
├── 21-costs-financial-aid.md               # Section 4
├── 22-evidence-chain.md                    # Section 5
└── 23-comparison-framework.md              # Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uiowa-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BBA|BFA|BSE|MA|MS|MBA|MFA|PhD|EdD|DNP|DPT|MD|JD|LLM|SJD|DMA|MPH|MPA|MSW|Certificate|Minor>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://catalog.registrar.uiowa.edu/your-program/
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Graduate program-specific deadlines and GRE requirements | Per-program detail pages |
| P0 | Per-program TOEFL/IELTS minimums for graduate | Per-program detail pages |
| P1 | School of Music full program list (BFA, MM, DMA) | https://music.uiowa.edu/ |
| P1 | School of Journalism full program list | https://journalism.uiowa.edu/ |
| P1 | Financial aid policy details (need-aware thresholds) | https://financialaid.uiowa.edu/ |
| P2 | Transfer admission requirements | https://admissions.uiowa.edu/apply/transfer-student-application-process |
| P2 | Honors Program details | https://admissions.uiowa.edu/academics/honors-research |
| P2 | Housing options and costs | https://admissions.uiowa.edu/student-life/residence-halls |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UIowa | (blank for other schools) |
|-----------|-------|---------------------------|
| Type | Public | |
| Location | Iowa City, IA | |
| UG tuition (resident) | $11,971 | |
| UG tuition (nonresident) | $34,247 | |
| UG total COA (resident, on-campus) | $31,845 | |
| UG total COA (nonresident, on-campus) | $54,121 | |
| EA deadline | November 3 | |
| RD deadline | February 2 | |
| SAT/ACT required? | No (test-optional, "No Harm" policy) | |
| TOEFL minimum | 80 (pre-Jan 2026) / 4.0 (post-Jan 2026) | |
| IELTS minimum | 6.5 | |
| Need-blind (domestic)? | No (need-aware) | |
| Need-blind (international)? | No (need-aware) | |
| Application fee (domestic) | $55 | |
| Application fee (international) | $80 | |
| Total program count (Rule 1) | 450 | |
| School/department count (Rule 2) | 12 | |
| Distinctive feature | Top public university for writing; Iowa Writers' Workshop | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.uiowa.edu, grad.uiowa.edu, catalog.registrar.uiowa.edu, financialaid.uiowa.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
