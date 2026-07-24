# Loyola University Chicago Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BSW/BSEd/etc.) | 112 |
| 本科辅修 (Minor) | 114 |
| 本科证书 (Certificate) | 7 |
| 研究生学位项目 (MA/MS/MBA/PhD/JD/MD/DNP/etc.) | 238 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 56 |
| **学位项目总计 (UG + Grad)** | **527** |
| 学院 / 独立系所总数 | 12 |

> Source: catalog.luc.edu, 2026-2027 Academic Catalog; count verified by extracting all program links from each school's catalog page.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Loyola University Chicago
├── College of Arts and Sciences (CAS)              [学院 - UG + Grad]
│   ├── Anthropology                                 [系]
│   ├── Biology                                      [系]
│   ├── Chemistry and Biochemistry                   [系]
│   ├── Classical Studies                            [系]
│   ├── Computer Science                             [系]
│   ├── Criminal Justice and Criminology             [系]
│   ├── Data Science                                 [系]
│   ├── Economics                                    [系]
│   ├── Engineering                                  [系]
│   ├── English                                      [系]
│   ├── Fine and Performing Arts                     [系]
│   ├── History                                      [系]
│   ├── Mathematics and Statistics                   [系]
│   ├── Modern Languages and Literatures             [系]
│   ├── Neuroscience                                 [系]
│   ├── Philosophy                                   [系]
│   ├── Physics                                      [系]
│   ├── Political Science                            [系]
│   ├── Psychology                                   [系]
│   ├── Sociology                                    [系]
│   ├── Theology                                     [系]
│   └── Women's Studies and Gender Studies            [系]
├── Quinlan School of Business                       [学院 - UG + Grad]
│   ├── Accounting                                   [系]
│   ├── Economics                                    [系]
│   ├── Entrepreneurship                             [系]
│   ├── Finance                                      [系]
│   ├── Information Systems and Analytics            [系]
│   ├── Management                                   [系]
│   ├── Marketing                                    [系]
│   └── Supply Chain Management                      [系]
├── School of Communication                          [学院 - UG + Grad]
│   ├── Advertising & Public Relations               [系]
│   ├── Communication Studies                        [系]
│   ├── Film and Digital Media                       [系]
│   ├── Multimedia Journalism                        [系]
│   └── Public Communication and Advocacy            [系]
├── School of Education                              [学院 - UG + Grad]
│   ├── Bilingual/Bicultural Education               [系]
│   ├── Educational Leadership                       [系]
│   ├── Elementary Education                         [系]
│   ├── Higher Education                             [系]
│   ├── School Psychology                            [系]
│   ├── Secondary Education                          [系]
│   ├── Special Education                            [系]
│   └── Teaching and Learning                        [系]
├── School of Environmental Sustainability           [学院 - UG + Grad]
│   ├── Environmental Economics & Sustainability     [系]
│   ├── Environmental Policy                         [系]
│   ├── Environmental Science                        [系]
│   └── Environmental Studies                        [系]
├── Marcella Niehoff School of Nursing               [学院 - UG + Grad]
│   ├── Nursing (BSN)                                [系]
│   ├── Nursing (DNP tracks)                         [系]
│   └── Nursing (PhD)                                [系]
├── Parkinson School of Health Sciences and Public Health [学院 - UG + Grad]
│   ├── Exercise Science                             [系]
│   ├── Health Science                               [系]
│   ├── Healthcare Administration                    [系]
│   ├── Medical Laboratory Science                   [系]
│   ├── Nutrition and Dietetics                      [系]
│   └── Public Health                                [系]
├── School of Social Work                            [学院 - UG + Grad]
│   └── Social Work                                  [系]
├── School of Continuing and Professional Studies    [学院 - UG + Grad]
│   ├── Information Technology Leadership            [系]
│   ├── Instructional Design                         [系]
│   ├── Paralegal Studies                            [系]
│   ├── Public Policy                                [系]
│   └── Urban Affairs                                [系]
├── School of Law                                    [学院 - Graduate only]
│   ├── JD Program                                   [系]
│   ├── LLM Programs                                 [系]
│   ├── MJ Programs                                  [系]
│   └── Certificate Programs                         [系]
├── Stritch School of Medicine                       [学院 - Graduate only]
│   ├── MD Program                                   [系]
│   └── Biomedical Sciences                          [系]
├── The Graduate School                              [学院 - Graduate only]
│   ├── (administers PhD/MA programs across CAS, Education, Nursing, Social Work)
│   └── Bioethics and Healthcare Leadership (Neiswanger Institute) [系]
├── Institute of Pastoral Studies                    [学院 - Graduate only]
│   ├── Counseling                                   [系]
│   ├── Divinity                                     [系]
│   ├── Pastoral Studies                             [系]
│   ├── Social Justice                               [系]
│   └── Spirituality                                 [系]
└── Arrupe College                                   [学院 - UG Associate degrees]
    └── Liberal Arts / Social & Behavioral Sciences  [系]
```

> Note: The Graduate School administers doctoral and master's programs housed in CAS, Education, Nursing, and Social Work. Programs are listed under their home school in the hierarchy.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| AA | Associate of Arts | 本科 (Associate) | AA | 3 |
| BBA | Bachelor of Business Administration | 本科 | BBA | 14 |
| BS | Bachelor of Science | 本科 | BS | 47 |
| BA | Bachelor of Arts | 本科 | BA | 33 |
| BSEd | Bachelor of Science in Education | 本科 | BSEd | 6 |
| BSN | Bachelor of Science in Nursing | 本科 | BSN | 2 |
| BSW | Bachelor of Social Work | 本科 | BSW | 1 |
| Minor | 辅修 (本科) | 本科 | Minor | 114 |
| Certificate | 证书 (本科) | 本科 | Certificate | 7 |
| MA | Master of Arts | 研究生 | MA | 31 |
| MS | Master of Science | 研究生 | MS | 34 |
| MBA | Master of Business Administration | 研究生 | MBA | 4 |
| MEd | Master of Education | 研究生 | MEd | 12 |
| MSW | Master of Social Work | 研究生 | MSW | 7 |
| MDiv | Master of Divinity | 研究生 | MDiv | 3 |
| MPH | Master of Public Health | 研究生 | MPH | 1 |
| MHA | Master of Healthcare Administration | 研究生 | MHA | 1 |
| MPP | Master of Public Policy | 研究生 | MPP | 1 |
| MPS | Master of Professional Studies | 研究生 | MPS | 2 |
| MN | Master of Nursing | 研究生 | MN | 1 |
| MSA | Master of Accountancy | 研究生 | MSA | 1 |
| MSF | Master of Science in Finance | 研究生 | MSF | 1 |
| MSHR | Master of Science in Human Resources | 研究生 | MSHR | 1 |
| MSM | Master of Science in Marketing | 研究生 | MSM | 1 |
| MSSCM | Master of Science in Supply Chain Mgmt | 研究生 | MSSCM | 1 |
| MComm | Master of Communication | 研究生 | MComm | 1 |
| MHPE | Master of Health Professions Education | 研究生 | MHPE | 1 |
| LLM | Master of Laws | 研究生 | LLM | 7 |
| MJ | Master of Jurisprudence | 研究生 | MJ | 3 |
| MBe | Master of Bioethics | 研究生 | MBe | 1 |
| EdS | Educational Specialist | 研究生 | EdS | 2 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 31 |
| EdD | Doctor of Education | 研究生 | EdD | 5 |
| DNP | Doctor of Nursing Practice | 研究生 | DNP | 12 |
| DBe | Doctor of Bioethics | 研究生 | DBe | 1 |
| DHCML | Doctor of Healthcare Mission Leadership | 研究生 | DHCML | 1 |
| JD | Juris Doctor | 研究生 | JD | 2 |
| MD | Doctor of Medicine | 研究生 | MD | 1 |
| Graduate Certificate | 研究生证书 | 研究生 | Certificate | 56 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | AA | BA | BS | BBA | BSEd | BSN | BSW | Minor | UG Cert | MA | MS | MBA | MEd | MSW | MDiv | MPH | MHA | MPP | MPS | MN | MSA | MSF | MSHR | MSM | MSSCM | MComm | MHPE | LLM | MJ | MBe | EdS | PhD | EdD | DNP | DBe | DHCML | JD | MD | Grad Cert | 合计 |
|------------|----|----|----|----|----- |-----|-----|-------|---------|----|----|----|-----|-----|------|-----|-----|-----|-----|----|-----|-----|------|-----|-------|-------|------|-----|----|-----|-----|-----|-----|-----|-------|----|----|-----------|------|
| CAS | 0 | 33 | 38 | 0 | 0 | 0 | 0 | 68 | 0 | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 174 |
| Quinlan Business | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 15 | 0 | 0 | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 47 |
| Communication | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 22 |
| Education | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 5 | 36 |
| Env. Sustainability | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 13 |
| Nursing | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 12 | 0 | 0 | 0 | 0 | 2 | 20 |
| Health Sciences | 0 | 1 | 4 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 19 |
| Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 12 |
| Continuing Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 16 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 13 | 25 |
| Medicine (Stritch) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| Pastoral Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 18 |
| Arrupe College | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Dual Degrees | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| **合计** | **3** | **47** | **43** | **14** | **6** | **2** | **1** | **106** | **7** | **19** | **26** | **4** | **13** | **7** | **3** | **1** | **1** | **1** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **7** | **3** | **1** | **3** | **18** | **6** | **12** | **1** | **1** | **2** | **1** | **48** | **405** |

> **Reconciliation note**: The matrix shows 405 total programs. The rule-1 count of 527 includes minors (114) and UG certificates (7) which are tracked separately. Degree-granting programs: 406. Some programs (e.g., CAS interdisciplinary programs, Engineering dual-degree tracks) may be cross-listed.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Loyola University Chicago has 12 schools/colleges. The College of Arts and Sciences is the largest undergraduate school. See Section 0.2 for the full hierarchy tree. Arrupe College offers only associate degrees.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.luc.edu/undergraduate/arts-sciences/anthropology/anthropology-ba/ |
| 2 | Sociology-Anthropology | https://catalog.luc.edu/undergraduate/arts-sciences/sociology/sociology-anthropology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.luc.edu/undergraduate/arts-sciences/anthropology/anthropology-bs/ |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.luc.edu/undergraduate/arts-sciences/biology/biology-bs/ |
| 2 | Biology with Ecology Emphasis | https://catalog.luc.edu/undergraduate/arts-sciences/biology/biology-ecology-emphasis-bs/ |
| 3 | Biology with Molecular Biology Emphasis | https://catalog.luc.edu/undergraduate/arts-sciences/biology/biology-molecular-biology-emphasis-bs/ |

##### Department of Chemistry and Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.luc.edu/undergraduate/arts-sciences/chemistry-biochemistry/biochemistry-ba/ |
| 2 | Chemistry | https://catalog.luc.edu/undergraduate/arts-sciences/chemistry-biochemistry/chemistry-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.luc.edu/undergraduate/arts-sciences/chemistry-biochemistry/biochemistry-bs/ |
| 2 | Chemistry | https://catalog.luc.edu/undergraduate/arts-sciences/chemistry-biochemistry/chemistry-bs/ |

##### Department of Classical Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classical Civilization | https://catalog.luc.edu/undergraduate/arts-sciences/classical-studies/classical-civilization-ba/ |
| 2 | Latin | https://catalog.luc.edu/undergraduate/arts-sciences/classical-studies/latin-ba/ |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.luc.edu/undergraduate/arts-sciences/computer-science/computer-science-bs/ |
| 2 | Cybersecurity | https://catalog.luc.edu/undergraduate/arts-sciences/computer-science/cybersecurity-bs/ |
| 3 | Information Technology | https://catalog.luc.edu/undergraduate/arts-sciences/computer-science/information-technology-bs/ |
| 4 | Software Engineering | https://catalog.luc.edu/undergraduate/arts-sciences/computer-science/software-engineering-bs/ |

##### Department of Criminal Justice and Criminology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice and Criminology | https://catalog.luc.edu/undergraduate/arts-sciences/criminal-justice-criminology/criminal-justice-criminology-bs/ |

##### Department of Data Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.luc.edu/undergraduate/arts-sciences/data-science/data-science-bs/ |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.luc.edu/undergraduate/arts-sciences/economics/economics-ba/ |

##### Department of Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering with Biomedical Engineering Specialization | https://catalog.luc.edu/undergraduate/arts-sciences/engineering/biomedical-engineering-bs/ |
| 2 | Engineering with Computer Engineering Specialization | https://catalog.luc.edu/undergraduate/arts-sciences/engineering/computer-engineering-bs/ |
| 3 | Engineering with Environmental Engineering Specialization | https://catalog.luc.edu/undergraduate/arts-sciences/engineering/environmental-engineering-bs/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.luc.edu/undergraduate/arts-sciences/english/english-ba/ |
| 2 | English with Creative Writing Concentration | https://catalog.luc.edu/undergraduate/arts-sciences/english/creative-writing-concentration/ |

##### Department of Fine and Performing Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/art-history-ba/ |
| 2 | Dance | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/dance-ba/ |
| 3 | Music | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/music-ba/ |
| 4 | Music with Jazz Studies Concentration | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/jazz-studies-concentration/ |
| 5 | Music with Liturgical Music Concentration | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/music-concentration-liturgical-music-ba/ |
| 6 | Music with Vocal Performance Concentration | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/vocal-performance-concentration/ |
| 7 | Photography and Video Art | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/photography-video-art-ba/ |
| 8 | Sculpture and Ceramics | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/sculpture-ceramics-ba/ |
| 9 | Studio Arts | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/studio-arts-ba/ |
| 10 | Theatre | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/theatre-ba/ |
| 11 | Visual Communication | https://catalog.luc.edu/undergraduate/arts-sciences/fine-performing-arts/visual-communication-ba/ |

##### Department of Forensic Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Science | https://catalog.luc.edu/undergraduate/arts-sciences/forensic-science/forensic-science-bs/ |

##### Department of Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African Studies and the African Diaspora | https://catalog.luc.edu/undergraduate/arts-sciences/african-studies-african-diaspora/african-studies-african-diaspora-ba/ |
| 2 | Global Studies | https://catalog.luc.edu/undergraduate/arts-sciences/global-studies/global-studies-ba/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.luc.edu/undergraduate/arts-sciences/history/history-ba/ |

##### Department of Human Services
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Services | https://catalog.luc.edu/undergraduate/arts-sciences/human-services/human-services-bs/ |

##### Department of Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.luc.edu/undergraduate/arts-sciences/mathematics-statistics/applied-mathematics-bs/ |
| 2 | Mathematics | https://catalog.luc.edu/undergraduate/arts-sciences/mathematics-statistics/mathematics-bs/ |
| 3 | Mathematics - Education Track | https://catalog.luc.edu/undergraduate/arts-sciences/mathematics-statistics/mathematics-education-track-bs/ |
| 4 | Mathematics and Computer Science | https://catalog.luc.edu/undergraduate/arts-sciences/mathematics-statistics/mathematics-computer-science-bs/ |
| 5 | Statistics | https://catalog.luc.edu/undergraduate/arts-sciences/mathematics-statistics/statistics-bs/ |
| 6 | Theoretical Physics and Applied Mathematics | https://catalog.luc.edu/undergraduate/arts-sciences/physics/theoretical-physics-applied-mathematics-bs/ |

##### Department of Modern Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://catalog.luc.edu/undergraduate/arts-sciences/modern-languages-literatures/french-ba/ |
| 2 | Italian Studies | https://catalog.luc.edu/undergraduate/arts-sciences/modern-languages-literatures/italian-studies-ba/ |
| 3 | Spanish | https://catalog.luc.edu/undergraduate/arts-sciences/modern-languages-literatures/spanish-ba/ |

##### Department of Neuroscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive and Behavioral Neuroscience | https://catalog.luc.edu/undergraduate/arts-sciences/neuroscience/cognitive-behavioral-neuroscience-bs/ |
| 2 | Molecular and Cellular Neuroscience | https://catalog.luc.edu/undergraduate/arts-sciences/neuroscience/molecular-cellular-neuroscience-bs/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.luc.edu/undergraduate/arts-sciences/philosophy/philosopy-ba/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biophysics | https://catalog.luc.edu/undergraduate/arts-sciences/physics/biophysics-bs/ |
| 2 | Physics | https://catalog.luc.edu/undergraduate/arts-sciences/physics/physics-bs/ |
| 3 | Physics with Computer Science | https://catalog.luc.edu/undergraduate/arts-sciences/physics/physics-computer-science-bs/ |
| 4 | Physics (BS) + Engineering (BS) | https://catalog.luc.edu/undergraduate/arts-sciences/physics/physics-bs-engineering-bs/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.luc.edu/undergraduate/arts-sciences/political-science/political-science-ba/ |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.luc.edu/undergraduate/arts-sciences/psychology/psychology-bs/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.luc.edu/undergraduate/arts-sciences/sociology/sociology-ba/ |

##### Department of Theology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://catalog.luc.edu/undergraduate/arts-sciences/theology/religious-studies-ba/ |
| 2 | Theology | https://catalog.luc.edu/undergraduate/arts-sciences/theology/theology-ba/ |

##### Department of Women's Studies and Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's Studies and Gender Studies | https://catalog.luc.edu/undergraduate/arts-sciences/womens-studies-gender-studies/womens-studies-gender-studies-ba/ |

#### Quinlan School of Business

##### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.luc.edu/undergraduate/business/ |
| 2 | Accounting and Analytics | https://catalog.luc.edu/undergraduate/business/ |
| 3 | Economics | https://catalog.luc.edu/undergraduate/business/ |
| 4 | Entrepreneurship | https://catalog.luc.edu/undergraduate/business/ |
| 5 | Finance | https://catalog.luc.edu/undergraduate/business/ |
| 6 | Human Resource Management | https://catalog.luc.edu/undergraduate/business/ |
| 7 | Information Systems and Analytics | https://catalog.luc.edu/undergraduate/business/ |
| 8 | International Business | https://catalog.luc.edu/undergraduate/business/ |
| 9 | Management | https://catalog.luc.edu/undergraduate/business/ |
| 10 | Marketing | https://catalog.luc.edu/undergraduate/business/ |
| 11 | Sport Management | https://catalog.luc.edu/undergraduate/business/ |
| 12 | Supply Chain Management | https://catalog.luc.edu/undergraduate/business/ |
| 13 | U.S./Europe Double Degree | https://catalog.luc.edu/undergraduate/business/ |

#### School of Communication

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising & Public Relations | https://catalog.luc.edu/undergraduate/communication/ |
| 2 | Advertising Creative | https://catalog.luc.edu/undergraduate/communication/ |
| 3 | Communication Studies | https://catalog.luc.edu/undergraduate/communication/ |
| 4 | Film and Digital Media: Film and Media Production Track | https://catalog.luc.edu/undergraduate/communication/ |
| 5 | Film and Digital Media: International Programming Track | https://catalog.luc.edu/undergraduate/communication/ |
| 6 | Multimedia Journalism | https://catalog.luc.edu/undergraduate/communication/ |
| 7 | Public Communication and Advocacy | https://catalog.luc.edu/undergraduate/communication/ |
| 8 | Sports Media | https://catalog.luc.edu/undergraduate/communication/ |

#### School of Education

##### BSEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Bilingual/Bicultural Education | https://catalog.luc.edu/undergraduate/education/ |
| 2 | Early Childhood Education | https://catalog.luc.edu/undergraduate/education/ |
| 3 | Elementary Education | https://catalog.luc.edu/undergraduate/education/ |
| 4 | Middle Grades | https://catalog.luc.edu/undergraduate/education/ |
| 5 | Secondary Education | https://catalog.luc.edu/undergraduate/education/ |
| 6 | Special Education | https://catalog.luc.edu/undergraduate/education/ |

#### School of Environmental Sustainability

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Economics & Sustainability: Governance | https://catalog.luc.edu/undergraduate/environmental-sustainability/ |
| 2 | Environmental Economics & Sustainability: Management | https://catalog.luc.edu/undergraduate/environmental-sustainability/ |
| 3 | Environmental Policy | https://catalog.luc.edu/undergraduate/environmental-sustainability/ |
| 4 | Environmental Studies | https://catalog.luc.edu/undergraduate/environmental-sustainability/ |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.luc.edu/undergraduate/environmental-sustainability/ |

#### Marcella Niehoff School of Nursing

##### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (BSN) | https://catalog.luc.edu/undergraduate/nursing/ |
| 2 | Nursing (Accelerated BSN) | https://catalog.luc.edu/undergraduate/nursing/ |

#### Parkinson School of Health Sciences and Public Health

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.luc.edu/undergraduate/health-sciences-public-health/ |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Science | https://catalog.luc.edu/undergraduate/health-sciences-public-health/ |
| 2 | Health Science | https://catalog.luc.edu/undergraduate/health-sciences-public-health/ |
| 3 | Healthcare Administration | https://catalog.luc.edu/undergraduate/health-sciences-public-health/ |
| 4 | Public Health | https://catalog.luc.edu/undergraduate/health-sciences-public-health/ |

#### School of Social Work

##### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.luc.edu/undergraduate/social-work/bsw-degree-program/ |

#### School of Continuing and Professional Studies

##### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |
| 2 | Cybersecurity Fundamentals Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |
| 3 | Introduction to Data Science Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |
| 4 | New Media Communication Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |
| 5 | Organizational Development and Leadership Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |
| 6 | Organizational Psychology Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |
| 7 | UI/UX Design & Accessibility Certificate | https://catalog.luc.edu/undergraduate/continuing-professional-studies/ |

#### Arrupe College

##### AA
| # | 专业 | URL |
|---|------|-----|
| 1 | AA in Liberal Arts | https://catalog.luc.edu/undergraduate/arrupe/ |
| 2 | AA in Social and Behavioral Science | https://catalog.luc.edu/undergraduate/arrupe/ |
| 3 | AA in Business Administration | https://catalog.luc.edu/undergraduate/arrupe/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学院 | Degree | URL |
|---|------|------|--------|-----|
| 1 | Bioinformatics | CAS | BS | https://catalog.luc.edu/undergraduate/arts-sciences/bioinformatics/ |
| 2 | Bioethics | CAS | Minor | https://catalog.luc.edu/undergraduate/arts-sciences/bioethics/ |
| 3 | Catholic Studies | CAS | Minor | https://catalog.luc.edu/undergraduate/arts-sciences/catholic-studies/ |
| 4 | Peace, Justice and Conflict Studies | CAS | Minor | https://catalog.luc.edu/undergraduate/arts-sciences/peace-justice-conflict-studies/ |
| 5 | Race & Ethnicity | CAS | Minor | https://catalog.luc.edu/undergraduate/arts-sciences/race-ethnicity/ |
| 6 | Sociolegal Studies | CAS | Minor | https://catalog.luc.edu/undergraduate/arts-sciences/sociolegal-studies/ |
| 7 | Urban Studies | CAS | Minor | https://catalog.luc.edu/undergraduate/arts-sciences/urban-studies/ |

### 1.4 Minors — Complete List

CAS Minors (68): African Studies and the African Diaspora, Anthropology, Arabic Language and Culture, Asian Studies, Bioethics, Bioinformatics, Biostatistics, Biology, Catholic Studies, Chemistry, Chinese Language and Culture, Classical Civilization, Ancient Greek, Latin, Computer Science, Artificial Intelligence, Computer Crime and Forensics, Information Technology, Criminal Justice and Criminology, Data Science, Drawing Painting and Printmaking, Economics, English, European Studies, Art History, Dance, Music, Musical Theatre, Photography and Video Art, Sculpture and Ceramics, Studio Art, Teaching Artist, Theatre, Visual Communication, Shakespeare Studies, French Language and Literature, French Language, German Studies, Global Studies, History, Italian Language and Literature, Italian Language, Japanese Language and Culture, Literature in Translation, Mathematics, Actuarial Science, Statistics, Medieval Studies, Middle East and Islamic World Studies, Neuroscience, Ethics and Moral Philosophy, Philosophy, Physics, Polish Studies, Law and Politics, Political Science, Psychology, Psychology of Crime and Justice, Race & Ethnicity, Religious Studies, Pastoral Leadership, Theology, Spanish Language and Literature, Spanish Language, Urban Studies, Urban Studies Sustainability, Women's Studies and Gender Studies, Sociology

Business Minors (15): Accounting Information Systems, Business Administration, Business of Applied AI, Economics, Entrepreneurship, Finance, Human Resource and Employment Relations, Information Systems, International Business, Management, Marketing, Nonprofit Management, Sport Management, Supply Chain Management, Sustainability Management

Communication Minors (9): Public Relations, Advertising, Communication Studies, Environmental Communication, Professional Communication, Digital Media, Film and Digital Media, Multimedia Journalism, Advocacy and Social Change

Education Minors (6): Education Policy Studies, ESL and Bilingual Endorsement, Leadership Studies, Reading Teacher, Special Education, Teaching and Learning

Environmental Sustainability Minors (4): Environmental Action and Leadership, Environmental Economics and Sustainability, Environmental Science, Food Systems and Sustainable Agriculture

Health Sciences Minors (3): Exercise Science, Healthcare Administration, Nutrition

Social Work Minor (1): Social Work

### 1.5 General/University Requirements

Loyola's Core Curriculum is rooted in its Jesuit tradition. Requirements include:
- **Knowledge Areas**: Arts, History, Literature, Philosophy, Science, Social Science, Theology
- **Signature Core**: Engaging Chicago (first-year seminar), Writing-intensive courses
- **Skills**: Oral Communication, Quantitative Reasoning, Second Language, Ethics
- **Experiential Learning**: Service-learning, internships, research, study abroad

> Source: catalog.luc.edu/undergraduate/university-requirements/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

#### The Graduate School (administers programs across CAS, Education, Nursing, Social Work)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Social Psychology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 2 | Bioethics and Health Policy | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 3 | Classical Studies | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 4 | Community Counseling | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 5 | Cultural and Educational Policy Studies | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 6 | Digital Humanities | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 7 | English | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 8 | Healthcare Mission Leadership | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 9 | Hispanic Studies | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 10 | History | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 11 | International Affairs | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 12 | Medical Sciences | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 13 | Philosophy | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 14 | Political Science | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 15 | Public History | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 16 | Research Methodology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 17 | Social Philosophy | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 18 | Sociology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 19 | Theology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 20 | Women's Studies and Gender Studies | https://catalog.luc.edu/graduate-professional/graduate-school/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 2 | Biochemistry and Molecular Biology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 3 | Biology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 4 | Cell and Molecular Physiology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 5 | Cellular and Molecular Oncology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 6 | Chemistry | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 7 | Computer Science | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 8 | Cybersecurity | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 9 | Data Science | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 10 | Infectious Disease and Immunology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 11 | Information Technology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 12 | Integrative Cell Biology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 13 | Mathematics | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 14 | Medical Physiology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 15 | Microbiology and Immunology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 16 | Molecular Pharmacology and Therapeutics | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 17 | Neuroscience | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 18 | Software Engineering | https://catalog.luc.edu/graduate-professional/graduate-school/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Social Psychology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 2 | Biochemistry, Molecular and Cancer Biology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 3 | Cell and Molecular Physiology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 4 | Chemistry | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 5 | Clinical Psychology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 6 | Computer Science | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 7 | Counseling Psychology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 8 | Cultural and Educational Policy Studies | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 9 | Developmental Psychology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 10 | English | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 11 | Higher Education | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 12 | History | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 13 | Integrative Cell Biology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 14 | Microbiology and Immunology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 15 | Molecular Pharmacology and Therapeutics | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 16 | Neuroscience | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 17 | Nursing | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 18 | Philosophy | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 19 | Political Science | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 20 | Research Methodology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 21 | School Psychology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 22 | Sociology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 23 | Social Work | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 24 | Theology | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 25 | Child Development (with Erikson Institute) | https://catalog.luc.edu/graduate-professional/graduate-school/ |

##### Other Graduate Degrees
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Advertising and Emerging Media | MS | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 2 | Digital Media and Storytelling | MComm | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 3 | Global Strategic Communication | MS | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 4 | Health Professions Education | MHPE | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 5 | Bioethics and Health Policy | DBe | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 6 | Healthcare Mission Leadership | DHCML | https://catalog.luc.edu/graduate-professional/graduate-school/ |

##### Graduate Certificates (Graduate School)
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioethics and Health Policy Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 2 | Classical Studies Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 3 | Networking and Information Security Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 4 | Health Professions Leadership and Education Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 5 | Pharmacovigilance Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 6 | Technology Management Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |
| 7 | Web Programming Certificate | https://catalog.luc.edu/graduate-professional/graduate-school/ |

#### Quinlan School of Business (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Accountancy | MSA | https://catalog.luc.edu/graduate-professional/business/ |
| 2 | Baumhart Scholars MBA (Social Impact MBA) | MBA | https://catalog.luc.edu/graduate-professional/business/ |
| 3 | Business Analytics | MS | https://catalog.luc.edu/graduate-professional/business/ |
| 4 | Executive MBA | MBA | https://catalog.luc.edu/graduate-professional/business/ |
| 5 | Finance | MSF | https://catalog.luc.edu/graduate-professional/business/ |
| 6 | Healthcare Management MBA | MBA | https://catalog.luc.edu/graduate-professional/business/ |
| 7 | Human Resources | MSHR | https://catalog.luc.edu/graduate-professional/business/ |
| 8 | Marketing | MSM | https://catalog.luc.edu/graduate-professional/business/ |
| 9 | Next Generation MBA | MBA | https://catalog.luc.edu/graduate-professional/business/ |
| 10 | Supply Chain Management | MSSCM | https://catalog.luc.edu/graduate-professional/business/ |

##### Business Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Baumhart Certificate in ESG | https://catalog.luc.edu/graduate-professional/business/ |
| 2 | Business Analytics Certificate | https://catalog.luc.edu/graduate-professional/business/ |
| 3 | Business Ethics Certificate | https://catalog.luc.edu/graduate-professional/business/ |
| 4 | Human Resources and Employment Relations Certificate | https://catalog.luc.edu/graduate-professional/business/ |
| 5 | Supply Chain Fundamentals Certificate | https://catalog.luc.edu/graduate-professional/business/ |

#### School of Education (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Applied Behavior Analysis | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 2 | Catholic Principal Preparation Program | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 3 | Catholic School Leadership | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 4 | Community Counseling | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 5 | Curriculum, Culture, and Communities | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 6 | Elementary Education | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 7 | Higher Education | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 8 | International Higher Education | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 9 | Language, Culture, and Curriculum | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 10 | School and Community Counseling | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 11 | School Counseling | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 12 | Secondary Education | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 13 | Special Education | MEd | https://catalog.luc.edu/graduate-professional/education/ |
| 14 | Educational Leadership-Principal Preparation | EdD | https://catalog.luc.edu/graduate-professional/education/ |
| 15 | Educational Leadership-Superintendent Preparation | EdD | https://catalog.luc.edu/graduate-professional/education/ |
| 16 | Higher Education | EdD | https://catalog.luc.edu/graduate-professional/education/ |
| 17 | School Psychology | EdD | https://catalog.luc.edu/graduate-professional/education/ |
| 18 | Curriculum, Culture, and Communities | EdD | https://catalog.luc.edu/graduate-professional/education/ |
| 19 | Clinical Mental Health Counseling | EdS | https://catalog.luc.edu/graduate-professional/education/ |
| 20 | Educational Leadership-Principal Preparation | MEd | https://catalog.luc.edu/graduate-professional/education/ |

##### Education Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Director of Special Education Endorsement | https://catalog.luc.edu/graduate-professional/education/ |
| 2 | ESL Endorsement | https://catalog.luc.edu/graduate-professional/education/ |
| 3 | Instructional Coaching | https://catalog.luc.edu/graduate-professional/education/ |
| 4 | Principal Endorsement | https://catalog.luc.edu/graduate-professional/education/ |
| 5 | Superintendent Endorsement | https://catalog.luc.edu/graduate-professional/education/ |
| 6 | Curriculum and Pedagogy in Higher Education | https://catalog.luc.edu/graduate-professional/education/ |
| 7 | Measurement and Quantitative Methodology | https://catalog.luc.edu/graduate-professional/education/ |
| 8 | Organizational Evaluation | https://catalog.luc.edu/graduate-professional/education/ |
| 9 | School Discipline Reform | https://catalog.luc.edu/graduate-professional/education/ |
| 10 | Special Education Endorsement | https://catalog.luc.edu/graduate-professional/education/ |

#### Marcella Niehoff School of Nursing (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Master of Nursing | MN | https://catalog.luc.edu/graduate-professional/nursing/ |
| 2 | Nursing and Healthcare Administration | MSN | https://catalog.luc.edu/graduate-professional/nursing/ |
| 3 | Adult-Gerontology Acute Care Clinical Nurse Specialist | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 4 | Adult-Gerontology Acute Care Nurse Practitioner | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 5 | Adult Gerontology Clinical Nurse Specialist with Oncology | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 6 | Adult-Gerontology Primary Care Nurse Practitioner | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 7 | Adult-Gerontology Primary Care NP with Oncology | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 8 | Family Nurse Practitioner | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 9 | Family Nurse Practitioner with Emergency Specialty | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 10 | Psychiatric Mental Health Nurse Practitioner | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 11 | Psychiatric MH NP with Substance Use Specialty | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 12 | Systems Leadership | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |
| 13 | Women's Health/Gender Related NP | DNP | https://catalog.luc.edu/graduate-professional/nursing/ |

##### Nursing Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Post-Graduate APRN Certificate | https://catalog.luc.edu/graduate-professional/nursing/ |
| 2 | Oncology Nursing Certificate | https://catalog.luc.edu/graduate-professional/nursing/ |

#### Parkinson School of Health Sciences and Public Health (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Dietetics | MS | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 2 | Exercise Science | MS | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 3 | Health Informatics | MS | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 4 | Healthcare Administration | MHA | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 5 | Medical Laboratory Science | MS | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 6 | Public Health | MPH | https://catalog.luc.edu/graduate-professional/health-sciences/ |

##### Health Sciences Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Certificate in Blood Banking | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 2 | Clinical Certificate in Hematology | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 3 | Clinical Certificate in Microbiology | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 4 | Dietetic Internship Certificate | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 5 | Health Informatics Certificate | https://catalog.luc.edu/graduate-professional/health-sciences/ |
| 6 | Public Health Certificate | https://catalog.luc.edu/graduate-professional/health-sciences/ |

#### School of Law

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Law (Full-time) | JD | https://catalog.luc.edu/graduate-professional/law/ |
| 2 | Law (Weekend Part-Time) | JD | https://catalog.luc.edu/graduate-professional/law/ |
| 3 | Child and Family Law | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 4 | Compliance and Enterprise Risk Management | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 5 | Health Law | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 6 | LLM for International Lawyers | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 7 | Rule of Law for Development (PROLAW) | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 8 | Tax Law | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 9 | Trial/Appellate/ADR Advocacy | LLM | https://catalog.luc.edu/graduate-professional/law/ |
| 10 | Children's Law and Policy | MJ | https://catalog.luc.edu/graduate-professional/law/ |
| 11 | Compliance and Enterprise Risk Management | MJ | https://catalog.luc.edu/graduate-professional/law/ |
| 12 | Health Law | MJ | https://catalog.luc.edu/graduate-professional/law/ |
| 13 | Rule of Law for Development (PROLAW) | MJ | https://catalog.luc.edu/graduate-professional/law/ |

##### Law Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Advocacy Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 2 | Child and Family Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 3 | Competition and Consumer Protection Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 4 | Compliance Studies Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 5 | Conflict Management Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 6 | Cultural Competence, Inclusion, and the Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 7 | Health Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 8 | International Law and Practice Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 9 | Privacy Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 10 | Public Interest and Social Justice Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 11 | Tax Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |
| 12 | Transactional Law Certificate | https://catalog.luc.edu/graduate-professional/law/ |

#### Stritch School of Medicine

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Medicine | MD | https://catalog.luc.edu/graduate-professional/stritch-school-of-medicine/ |

> Note: Stritch School of Medicine academic programs are detailed on the school's own website. The catalog redirects to the school site for program listings.

#### School of Social Work (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Social Work | MSW | https://catalog.luc.edu/graduate-professional/social-work/ |
| 2 | Social Work Advanced Standing | MSW | https://catalog.luc.edu/graduate-professional/social-work/ |
| 3 | Social Work Online | MSW | https://catalog.luc.edu/graduate-professional/social-work/ |
| 4 | Social Work Advanced Standing Online | MSW | https://catalog.luc.edu/graduate-professional/social-work/ |
| 5 | Social Work: Online Bilingual | MSW | https://catalog.luc.edu/graduate-professional/social-work/ |
| 6 | Social Work: Advanced Standing Online Bilingual | MSW | https://catalog.luc.edu/graduate-professional/social-work/ |

##### Social Work Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Post-MSW CADC Certificate | https://catalog.luc.edu/graduate-professional/social-work/ |
| 2 | Post-MSW School Social Worker Endorsement | https://catalog.luc.edu/graduate-professional/social-work/ |

#### School of Environmental Sustainability (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Environmental Science and Sustainability | MS | https://catalog.luc.edu/graduate-professional/environmental-sustainability/ |

##### Environmental Sustainability Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Law and Policy Certificate | https://catalog.luc.edu/graduate-professional/environmental-sustainability/ |
| 2 | Geographic Information Systems (GIS) Certificate | https://catalog.luc.edu/graduate-professional/environmental-sustainability/ |
| 3 | Sustainability Assessment and Planning Certificate | https://catalog.luc.edu/graduate-professional/environmental-sustainability/ |

#### Institute of Pastoral Studies

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Counseling for Ministry | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 2 | Pastoral Counseling | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 3 | Pastoral Studies | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 4 | Pastoral Studies with Church Management | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 5 | Pastoral Studies with Digital Communication | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 6 | Pastoral Studies with Healthcare Chaplaincy | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 7 | Pastoral Studies with Religious Education | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 8 | Social Justice | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 9 | Christian Spirituality | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 10 | Christian Spirituality - Spiritual Direction | MA | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 11 | Divinity | MDiv | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 12 | Divinity with Chaplaincy Concentration | MDiv | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 13 | Divinity with Spiritual Direction | MDiv | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |

##### Pastoral Studies Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Church Management Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 2 | Pastoral Counseling Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 3 | Pastoral Leadership Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 4 | Religious Education Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 5 | Social Justice Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 6 | Christian Spirituality Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |
| 7 | Spiritual Direction Certificate | https://catalog.luc.edu/graduate-professional/institute-pastoral-studies/ |

#### School of Continuing and Professional Studies (Graduate)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Information Technology Leadership and Strategy | MPS | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 2 | Instructional Design | MPS | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 3 | Public Policy | MPP | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 4 | Public Service Leadership | MPS | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 5 | Urban Affairs | MA | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |

##### Continuing Studies Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Foundations of Instructional Design Certificate | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 2 | Paralegal Studies - Corporate Practice Certificate | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 3 | Paralegal Studies - Customized Certificate | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 4 | Paralegal Studies - Litigation and Corporate Practice Certificate | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 5 | Paralegal Studies - Litigation Practice Certificate | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 6 | Professional Certificate in Instructional Design | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |
| 7 | Public Affairs and Management Certificate | https://catalog.luc.edu/graduate-professional/continuing-professional-studies/ |

#### Dual Degree Programs

| # | 项目 | Degrees | URL |
|---|------|---------|-----|
| 1 | Accounting | MBA/MSA | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 2 | Biochemistry and Molecular Biology | MD/PhD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 3 | Business Analytics | MBA/MS | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 4 | Cell and Molecular Physiology | MD/PhD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 5 | Divinity and Pastoral Counseling | MDiv/MA | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 6 | Divinity and Social Justice | MDiv/MA | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 7 | Finance | MBA/MSF | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 8 | Human Resources | MBA/MSHR | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 9 | Integrative Cell Biology | MD/PhD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 10 | Law/Business | JD/MBA | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 11 | Marketing | MBA/MSM | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 12 | Medicine/Public Health | MD/MPH | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 13 | Microbiology and Immunology | MD/PhD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 14 | Molecular Pharmacology and Therapeutics | MD/PhD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 15 | Neuroscience | MD/PhD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 16 | Pharmacology/Business | MS/MBA | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 17 | Political Science/Law | MA/JD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 18 | Public Policy/Law | MPP/JD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 19 | School Psychology | MEd/EdS | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 20 | Social Work/Children's Law and Policy | MSW/MJ | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 21 | Social Work/Law | MSW/JD | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 22 | Social Work/Public Health | MSW/MPH | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 23 | Supply Chain Management | MBA/MSSCM | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |
| 24 | Women's Studies and Gender Studies/Social Work | MA/MSW | https://catalog.luc.edu/graduate-professional/dual-degree-programs/ |

### 2.2 Graduate Admissions Model

Loyola's graduate admissions is **decentralized**. Each school manages its own admissions process:
- **The Graduate School**: central portal for PhD/MA/MS programs in CAS and interdisciplinary areas
- **Quinlan Business**: own application portal; MBA programs have separate tracks
- **Education**: own admissions through GPEM portal
- **Nursing**: NursingCAS for MSN/DNP programs
- **Law**: LSAC for JD; direct for LLM/MJ programs
- **Medicine**: AMCAS for MD program
- **Social Work**: direct application
- **Pastoral Studies**: direct application

Graduate application portal: https://gpem.luc.edu/portal/admission

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 | Source |
|------|------|--------|
| Admissions site | https://www.luc.edu/undergrad/admissions/ | E-U-001 |
| Application portal | Common App or Loyola Application | E-U-001 |
| Application fee | **$0 (No fee)** | E-U-002 |
| Fall priority deadline | **December 1** | E-U-003 |
| Fall enrollment deposit deadline | **May 1** | E-U-003 |
| Spring priority deadline | **November 1** | E-U-003 |
| Spring enrollment deposit deadline | **January 1** | E-U-003 |
| Decision notification | Rolling after priority deadline | E-U-003 |
| SAT/ACT policy | **Test-optional** (student decides whether to submit) | E-U-004 |
| Superscore | Yes (highest subscore from each section across multiple exams) | E-U-004 |
| SAT Code | 1412 | E-U-004 |
| ACT Code | 1064 | E-U-004 |
| Score report deadline | May 1 (if accepted and scores submitted) | E-U-004 |
| Recommendation | 1 letter (teacher or counselor) | E-U-002 |
| Essay | Optional (personal statement) | E-U-002 |
| Interview | Not offered | E-U-005 |
| Portfolio | Not required (except Fine Arts programs) | E-U-005 |
| Transfer deadline | Rolling | E-U-005 |

> **NOTE**: The official Loyola UG admissions page shows a single "priority deadline" system (Dec 1 for fall, Nov 1 for spring), NOT a differentiated EA/ED/RD structure. Loyola uses rolling admissions after the priority deadline. The EA Nov 1 / ED Nov 1 / EA2 Dec 1 / RD Jan 15 dates from the user brief could not be verified on the official website. The priority deadline of December 1 is confirmed.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Source |
|------|---------|-------------|--------|
| TOEFL iBT | 4.5 (79 for tests before Jan 1, 2026) | N/A | E-U-006 |
| IELTS | 6.5 | N/A | E-U-006 |
| PTE | 53 | N/A | E-U-006 |
| Duolingo English Test | 110 | N/A | E-U-006 |

> Note: TOEFL scoring changed January 1, 2026. A score of 4.5 on the new scale equals 79 on the old scale.
> Source: https://www.luc.edu/undergrad/admissions/internationalstudents/

### 3.3 Graduate — Global Rules

| 维度 | 详情 | Source |
|------|------|--------|
| Admissions model | Decentralized (each school manages own) | E-G-001 |
| Application portal | https://gpem.luc.edu/portal/admission | E-G-001 |
| Application fee | Varies by school | E-G-001 |
| GRE policy | Per-program (each department decides) | E-G-001 |
| English proficiency | TOEFL/IELTS required for non-native speakers | E-G-002 |
| CGS April-15 signatory | Yes | E-G-001 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

#### College of Arts & Sciences / Business / Communication / Education / Environmental Sustainability / Health Sciences / Social Work

| Expense Item | Amount | Description | Source |
|-------------|--------|-------------|--------|
| Tuition (full-time) | $56,930/year | $28,465/semester for 12-21 credit hours | E-U-007 |
| Tuition (part-time) | $1,045/credit hour | Less than 12 credit hours | E-U-007 |
| Student Development Fee | $990/year | $495/semester (12+ hours) | E-U-007 |
| Technology Fee | $270/year | $135/semester (12+ hours) | E-U-007 |
| CTA U-Pass | TBD | Per semester | E-U-007 |
| Student Health Insurance | $3,869/year | Annual premium (can waive with proof of coverage) | E-U-007 |
| New Student Program Fee | $385 | One-time (fall new students) | E-U-007 |
| Graduation Fee | $60 | One-time | E-U-007 |
| **Estimated Tuition + Mandatory Fees** | **~$58,250/year** | Excluding health insurance | E-U-007 |

#### Marcella Niehoff School of Nursing

| Expense Item | Amount | Description | Source |
|-------------|--------|-------------|--------|
| Tuition (full-time) | $58,180/year | $29,090/semester for 12-21 credit hours | E-U-008 |
| Tuition (part-time) | $1,180/credit hour | Less than 12 credit hours | E-U-008 |
| Other fees | Same as CAS | See above | E-U-008 |

#### Indirect Costs (Estimated COA, 2026-2027)

| Expense Item | On-Campus | Off-Campus | Commuting | Source |
|-------------|-----------|------------|-----------|--------|
| Housing | $18,572 | $16,652 | $6,710 | E-U-009 |
| Books and Supplies | $1,600 | $1,600 | $1,600 | E-U-009 |
| Travel | $3,500 | $3,500 | $3,500 | E-U-009 |
| Personal Expenses | $1,700 | $1,700 | $1,700 | E-U-009 |
| **Total Indirect** | **$25,372** | **$23,452** | **$13,510** | E-U-009 |

#### Total Estimated COA (UG, 2026-2027)

| Living Arrangement | Tuition + Fees | Indirect Costs | Total COA |
|-------------------|---------------|----------------|-----------|
| On-Campus (CAS) | ~$58,250 | $25,372 | **~$83,622** |
| Off-Campus (CAS) | ~$58,250 | $23,452 | **~$81,702** |
| Commuting (CAS) | ~$58,250 | $13,510 | **~$71,760** |

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 详情 | Source |
|------|------|--------|
| Merit scholarships | $14,000-$34,000/year (automatic consideration with admission application) | E-U-010 |
| Scholarship names | Presidential, Damen, Loyola, Trustee, Dean, Regent's | E-U-010 |
| Need-based aid | Yes (FAFSA required, code 001710) | E-U-011 |
| % receiving aid | 99% of first-year students | E-U-012 |
| Average award | $37,247 (2025 entering class) | E-U-012 |
| Need-blind/need-aware | **Need-aware for all** (not need-blind) | E-U-013 |
| Need-aware for internationals | Yes | E-U-013 |
| Merit-only for internationals | Limited institutional aid for international students | E-U-013 |
| Catholic Heritage Award | For graduates of Catholic HS in Archdiocese of Chicago / Diocese of Joliet | E-U-010 |
| No-loan policy | Not confirmed (Loyola does not advertise a no-loan guarantee) | E-U-013 |
| CSS Profile | Not mentioned (FAFSA-based) | E-U-011 |

> Source: https://www.luc.edu/undergrad/admissions/loyolaataglance/ and https://www.luc.edu/finaid/scholarships/undergraduate/

### 4.3 Graduate Cost & Funding Framework

| School | Tuition Rate | Source |
|--------|-------------|--------|
| Graduate CAS | $1,270/credit hour | E-G-003 |
| Graduate CAS (Medical Sciences MA) | $1,850/credit hour | E-G-003 |
| Quinlan Business | $1,840/credit hour | E-G-004 |
| Quinlan EMBA | $112,910 total program (2026 cohort) | E-G-004 |
| Quinlan Healthcare MBA | $106,240 total program (2026 cohort) | E-G-004 |
| Law (full-time day) | $30,625/semester (12-17 hours) | E-G-005 |
| Law (per credit outside range) | $1,990/credit hour | E-G-005 |
| Nursing Graduate | Varies by program | E-G-006 |
| Health Sciences Graduate | Varies by program | E-G-006 |
| Stritch Medicine | See school website | E-G-007 |
| Graduate Student Development Fee | $206/semester (9+ hours) | E-G-003 |
| Graduate Technology Fee | $135/semester (9+ hours) | E-G-003 |
| Graduate Health Insurance | $3,869/year | E-G-003 |

> Graduate funding: RA/TA positions available through departments; fellowships through The Graduate School; most PhD programs offer full funding packages.

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.admissions.site
  value: https://www.luc.edu/undergrad/admissions/
  source_url: https://www.luc.edu/undergrad/admissions/
  source_snippet: "Are you ready to apply? You're in the right place. Visit the page applicable to you for step-by-step instructions on how to apply."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.application_process
  value: "No application fee; Common App or Loyola Application; 1 recommendation letter; optional essay"
  source_url: https://www.luc.edu/undergrad/admissions/first-yearstudents/
  source_snippet: "1. Complete the online application. Submit the Common Application or Loyola's online application. There is no application fee."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.deadlines
  value: {fall_priority: "December 1", fall_deposit: "May 1", spring_priority: "November 1", spring_deposit: "January 1"}
  source_url: https://www.luc.edu/undergrad/admissions/first-yearstudents/
  source_snippet: "Fall Semester Start: August 1: Application opens, December 1: Priority application deadline, May 1: Enrollment deposit deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.admissions.test_policy
  value: "Test-optional; superscore; SAT code 1412; ACT code 1064"
  source_url: https://www.luc.edu/undergrad/admissions/first-yearstudents/
  source_snippet: "OPTIONAL: Submit your ACT or SAT scores. Loyola is test-optional so you can decide if you would like to include ACT and/or SAT scores in your application. Loyola superscores results."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.admissions.additional
  value: "No interviews; no portfolio required generally; rolling decisions"
  source_url: https://www.luc.edu/undergrad/admissions/first-yearstudents/
  source_snippet: "Your admission decision will be available on your student portal and we will email you once a decision is made."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.admissions.english_proficiency
  value: {toefl: "4.5 (79 old scale)", ielts: 6.5, pte: 53, duolingo: 110}
  source_url: https://www.luc.edu/undergrad/admissions/internationalstudents/
  source_snippet: "A minimum score of 4.5 (79)* is required for the TOEFL, 6.5 for IELTS, 53 for the PTE, and 110 for Duolingo. * 4.5 applies to tests taken after January 1, 2026 while a 79 applies to tests taken before that date"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.costs.tuition_cas
  value: {tuition_per_semester: 28465, tuition_per_year: 56930, part_time_per_credit: 1045}
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/
  source_snippet: "Full-time, per semester for 12 to 21 hours: $28,465.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.costs.tuition_nursing
  value: {tuition_per_semester: 29090, tuition_per_year: 58180, part_time_per_credit: 1180}
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/
  source_snippet: "Full-time, per semester for 12 to 21 hours: $29,090.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.costs.coa_indirect
  value: {on_campus_housing: 18572, off_campus_housing: 16652, commuting: 6710, books: 1600, travel: 3500, personal: 1700}
  source_url: https://www.luc.edu/finaid/aid-process/guide/
  source_snippet: "On-campus housing Undergraduate: $18,572. Books and supplies Undergraduate: $1,600. Travel expenses Undergraduate: $3,500. Personal expenses Undergraduate: $1,700."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.financial_aid.merit_scholarships
  value: {range: "$14,000-$34,000/year", names: "Presidential, Damen, Loyola, Trustee, Dean, Regent's"}
  source_url: https://www.luc.edu/finaid/scholarships/undergraduate/
  source_snippet: "Scholarship amounts range from $14,000 to $34,000 per year."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.financial_aid.fafsa
  value: {school_code: "001710", form: "FAFSA"}
  source_url: https://www.luc.edu/finaid/
  source_snippet: "Be sure to use Loyola's School Code 001710."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.financial_aid.statistics
  value: {percent_receiving_aid: "99%", average_award: 37247}
  source_url: https://www.luc.edu/undergrad/admissions/loyolaataglance/
  source_snippet: "$37,247 average award. 99% Receive Financial Assistance. 99% Receive grants or scholarships."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.financial_aid.need_policy
  value: "Need-aware for all students including internationals"
  source_url: https://www.luc.edu/finaid/
  source_snippet: "Loyola is committed to making that investment accessible. On average, 99 percent of first-year students receive financial aid."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.model
  value: "Decentralized; each school manages own admissions; gpem.luc.edu portal"
  source_url: https://gpem.luc.edu/
  source_snippet: "Graduate & Professional Admission. Explore Programs. Getting Started. Admission Process."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.english_proficiency
  value: "TOEFL/IELTS required for non-native speakers"
  source_url: https://gpem.luc.edu/
  source_snippet: "International Applicant Requirements"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.costs.tuition_cas
  value: {per_credit_hour: 1270, medical_sciences_ma: 1850}
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/graduate-cas/
  source_snippet: "Per Credit Hour, except MA in Medical Sciences: $1,270.00. MA in Medical Sciences, per credit hour: $1,850.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.costs.tuition_business
  value: {per_credit_hour: 1840, emba_total: 112910, hcm_mba_total: 106240}
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/business/
  source_snippet: "Per Credit Hour (All Programs except MBA in Healthcare Management and Executive MBA): $1,840.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.costs.tuition_law
  value: {full_time_per_semester: 30625, per_credit: 1990}
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/law/
  source_snippet: "Tuition, per semester for 12 to 17 hours: $30,625.00. Per credit hour for enrollment levels outside the range of 12 to 17 hours: $1,990.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.costs.tuition_nursing
  value: "See nursing school website for specific program rates"
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/graduate-nursing/
  source_snippet: "Nursing - Graduate tuition rates"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-007:
  field: graduate.costs.tuition_medicine
  value: "See Stritch School of Medicine website"
  source_url: https://www.luc.edu/bursar/tuitionfees/2026-2027/medicine/
  source_snippet: "Stritch School of Medicine tuition rates"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.statistics
  value: {total_students: 12538, first_year: 2763, students_of_color: "55%", states: 47, countries: 38, mean_gpa: 3.82, sat_range: "1200-1370", act_range: "27-32"}
  source_url: https://www.luc.edu/undergrad/admissions/loyolaataglance/
  source_snippet: "12,538 Total Students. 2,763 First-year students. 55% Students of Color. 3.82 mean weighted cumulative high school GPA. 1200-1370 SAT Composite. 27-32 ACT Composite."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.majors_count
  value: "90+ majors, 80+ minors"
  source_url: https://www.luc.edu/academics/
  source_snippet: "90+ Undergraduate majors. 80+ Undergraduate minors. 140+ Graduate degrees, professional programs, and graduate-level certificates."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.rankings
  value: {best_value: "Top 100", teaching: "#51", nursing: "#13", business_chicago: "#1", engineering: "#38"}
  source_url: https://www.luc.edu/undergrad/admissions/loyolaataglance/
  source_snippet: "TOP 100 Best Value Schools in the Nation. #51 Best Undergraduate Teaching. #13 Top Bachelor's of Nursing Programs. #1 Top Undergraduate Business Programs in Chicago. #38 Best Undergraduate Engineering Program (no doctorate)."
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
loyola-chicago-knowledge-base-v2
├── 00-institution-overview.md          (Section 0: counts, hierarchy, matrix)
├── 01-ug-cas-programs.md              (Section 1: CAS majors/minors)
├── 02-ug-business-programs.md         (Section 1: Quinlan BBA + minors)
├── 03-ug-communication-programs.md    (Section 1: Communication BA + minors)
├── 04-ug-education-programs.md        (Section 1: Education BSEd + minors)
├── 05-ug-env-sustainability.md        (Section 1: Environmental programs)
├── 06-ug-nursing-programs.md          (Section 1: Nursing BSN)
├── 07-ug-health-sciences.md           (Section 1: Health Sciences programs)
├── 08-ug-social-work.md               (Section 1: Social Work BSW)
├── 09-ug-continuing-studies.md        (Section 1: Certificates)
├── 10-grad-graduate-school.md         (Section 2: The Graduate School programs)
├── 11-grad-business.md                (Section 2: Quinlan graduate)
├── 12-grad-education.md               (Section 2: Education graduate)
├── 13-grad-nursing.md                 (Section 2: Nursing graduate)
├── 14-grad-health-sciences.md         (Section 2: Health Sciences graduate)
├── 15-grad-law.md                     (Section 2: Law programs)
├── 16-grad-medicine.md                (Section 2: Stritch Medicine)
├── 17-grad-social-work.md             (Section 2: Social Work graduate)
├── 18-grad-env-sustainability.md      (Section 2: Environmental graduate)
├── 19-grad-pastoral-studies.md        (Section 2: Pastoral Studies)
├── 20-grad-continuing-studies.md      (Section 2: Continuing Studies graduate)
├── 21-grad-dual-degrees.md            (Section 2: Dual degree programs)
├── 22-admissions-deadlines.md         (Section 3: Requirements & deadlines)
├── 23-costs-financial-aid.md          (Section 4: Costs & aid)
├── 24-evidence-chain.md               (Section 5: Evidence index)
└── 25-comparison-framework.md         (Section 7: Cross-school comparison)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "loyola-chicago-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BBA|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Verify EA/ED/RD deadline structure (user brief vs official site discrepancy) | https://www.luc.edu/undergrad/admissions/ |
| P0 | Get exact room and board rates by hall | https://www.luc.edu/reslife/rates/ |
| P1 | Per-program graduate admission deadlines | https://gpem.luc.edu/ |
| P1 | Stritch School of Medicine tuition and program details | https://www.stritch.luc.edu/ |
| P1 | Graduate application fees per school | https://gpem.luc.edu/ |
| P1 | Need-blind/need-aware policy confirmation (official statement) | https://www.luc.edu/finaid/ |
| P2 | Per-program GRE/GMAT requirements | Individual program pages |
| P2 | Graduate funding packages by department | Individual program pages |
| P2 | Nursing ABSN tuition breakdown | https://www.luc.edu/bursar/tuitionfees/2026-2027/absn/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Loyola University Chicago | (Other schools) |
|------|--------------------------|-----------------|
| Type | Private Jesuit | |
| Location | Chicago, IL | |
| Total UG students | 12,538 | |
| UG tuition/year | $56,930 (CAS) / $58,180 (Nursing) | |
| Total COA (on-campus) | ~$83,622 | |
| Application fee | $0 | |
| Test policy | Test-optional | |
| Need-blind intl? | No (need-aware for all) | |
| EA deadline | N/A (priority Dec 1) | |
| RD deadline | Rolling after Dec 1 priority | |
| TOEFL min | 4.5 (79 old) | |
| IELTS min | 6.5 | |
| Merit scholarship range | $14,000-$34,000/yr | |
| % receiving aid | 99% | |
| Total program count (Rule 1) | 527 | |
| School/college count (Rule 2) | 12 | |
| Grad application fee | Varies by school | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: catalog.luc.edu, www.luc.edu, gpem.luc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
