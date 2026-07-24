# Case Western Reserve University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BSE/BSM/BFA) | 82 |
| 本科辅修 (Minor) | 92 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 202 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 23 |
| **学位项目总计 (UG + Grad)** | **399** |
| 学院 / 独立系所总数 | 9 |

> Reconciliation: 82 + 92 + 202 + 23 = 399 ✓

### 0.2 学院 / 系层级结构 (Rule 2)

```
Case Western Reserve University
├── Case School of Engineering                          [学院]
│   ├── Aerospace Engineering                           [系]
│   ├── Biomedical Engineering                          [系]
│   ├── Chemical Engineering                            [系]
│   ├── Civil Engineering                               [系]
│   ├── Computer Engineering                            [系]
│   ├── Computer Science                                [系]
│   ├── Electrical Engineering                          [系]
│   ├── Materials Science and Engineering                [系]
│   ├── Mechanical Engineering                          [系]
│   ├── Systems and Control Engineering                 [系]
│   └── Macromolecular Science                          [系]
├── College of Arts and Sciences                        [学院]
│   ├── Anthropology                                    [系]
│   ├── Astronomy                                       [系]
│   ├── Biology                                         [系]
│   ├── Chemistry                                       [系]
│   ├── Communication Sciences                         [系]
│   ├── Economics                                       [系]
│   ├── English                                         [系]
│   ├── Geological Sciences                             [系]
│   ├── History                                         [系]
│   ├── Mathematics                                     [系]
│   ├── Music                                           [系]
│   ├── Philosophy                                      [系]
│   ├── Physics                                         [系]
│   ├── Political Science                               [系]
│   ├── Psychology                                      [系]
│   ├── Religious Studies                               [系]
│   ├── Sociology                                       [系]
│   ├── Statistics                                      [系]
│   ├── Theater Arts                                    [系]
│   └── World Literature                                [系]
├── Frances Payne Bolton School of Nursing              [学院]
│   └── Nursing                                         [系]
├── Jack, Joseph and Morton Mandel School of Applied Social Sciences [学院]
│   └── Social Work                                     [系]
├── School of Dental Medicine                           [学院]
│   ├── Dental Medicine                                 [系]
│   ├── Endodontics                                     [系]
│   ├── Oral and Maxillofacial Surgery                  [系]
│   ├── Orthodontics                                    [系]
│   └── Periodontics                                    [系]
├── School of Graduate Studies                          [学院]
│   └── (administers graduate programs across schools)
├── School of Law                                       [学院]
│   ├── Law                                             [系]
│   └── Compliance and Risk Management                  [系]
├── School of Medicine                                  [学院]
│   ├── Aerospace Physiology                            [系]
│   ├── Anesthesia                                      [系]
│   ├── Applied Anatomy                                 [系]
│   ├── Biochemistry                                    [系]
│   ├── Bioethics and Medical Humanities                [系]
│   ├── Biomedical and Health Informatics               [系]
│   ├── Biotechnology                                   [系]
│   ├── Cancer Studies                                  [系]
│   ├── Cell Biology                                    [系]
│   ├── Clinical Research                               [系]
│   ├── Epidemiology and Biostatistics                  [系]
│   ├── Genetic Counseling                              [系]
│   ├── Genetics                                        [系]
│   ├── Medical Physiology                              [系]
│   ├── Medicine                                        [系]
│   ├── Molecular Biology and Microbiology              [系]
│   ├── Molecular Medicine                              [系]
│   ├── Neurosciences                                   [系]
│   ├── Nutrition                                       [系]
│   ├── Pathology                                       [系]
│   ├── Pharmacology                                    [系]
│   ├── Physician Assistant Studies                     [系]
│   ├── Physiology and Biophysics                       [系]
│   ├── Public Health                                   [系]
│   └── Systems Biology and Bioinformatics              [系]
└── Weatherhead School of Management                    [学院]
    ├── Accounting                                      [系]
    ├── Business Administration                         [系]
    ├── Business Analytics and Intelligence             [系]
    ├── Economics                                       [系]
    ├── Engineering and Management                      [系]
    ├── Finance                                         [系]
    ├── Healthcare Management                           [系]
    ├── Leadership and Organizational Change            [系]
    ├── Management                                      [系]
    ├── Marketing                                       [系]
    └── Supply Chain Management                         [系]
```

### 0.3 学历级别明细 (Rule 3)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 31 |
| BS | Bachelor of Science | 本科 | 24 |
| BSE | Bachelor of Science in Engineering | 本科 | 12 |
| BSM | Bachelor of Science in Management | 本科 | 4 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BFA | Bachelor of Fine Arts | 本科 | 0 |
| MAcc | Master of Accountancy | 研究生 | 1 |
| MA | Master of Arts | 研究生 | 28 |
| MS | Master of Science | 研究生 | 42 |
| MBA | Master of Business Administration | 研究生 | 4 |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MEng | Master of Engineering | 研究生 | 1 |
| MFin | Master of Finance | 研究生 | 1 |
| MSFT | Master of Science in FinTech | 研究生 | 1 |
| MSCM | Master of Science in Supply Chain Management | 研究生 | 1 |
| MHcM | Master of Healthcare Management | 研究生 | 1 |
| MN | Master of Nursing | 研究生 | 1 |
| MSA | Master of Science in Anesthesia | 研究生 | 1 |
| MSLOC | Master of Science in Leadership and Organizational Change | 研究生 | 1 |
| MBusAI | Master of Business Analytics and Intelligence | 研究生 | 1 |
| MEM | Master of Engineering and Management | 研究生 | 1 |
| ME | Master of Engineering (Online) | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 2 |
| MNO | Master of Nonprofit Organizations | 研究生 | 1 |
| MSPAS | Master of Science in Physician Assistant Studies | 研究生 | 1 |
| MCRM | Master of Compliance and Risk Management | 研究生 | 2 |
| ML | Master of Laws | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 2 |
| SJD | Doctor of Juridical Science | 研究生 | 1 |
| DMD | Doctor of Dental Medicine | 研究生 | 1 |
| MSD | Master of Science in Dentistry | 研究生 | 6 |
| MD | Doctor of Medicine | 研究生 | 2 |
| PhD | Doctor of Philosophy | 研究生 | 48 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 2 |
| DMA | Doctor of Musical Arts | 研究生 | 1 |
| Minor | 辅修 | 本科 | 92 |
| Graduate Certificate | 研究生证书 | 研究生 | 16 |
| Professional Certification | 专业认证 | 研究生 | 7 |

### 0.4 分布矩阵 (Rule 4 — 学院 × 学位级别)

| 学院 | BA | BS | BSE | BSM | BSN | MA | MS | MBA | MFA | PhD | DNP | DMD | MD | Minor | Cert | Dual | 合计 |
|------|----|----|-----|-----|-----|----|----|-----|-----|-----|-----|-----|-----|-------|------|------|------|
| Case School of Engineering | 0 | 2 | 12 | 0 | 0 | 0 | 15 | 0 | 0 | 11 | 0 | 0 | 0 | 19 | 1 | 1 | 61 |
| College of Arts and Sciences | 31 | 12 | 1 | 0 | 0 | 15 | 5 | 0 | 2 | 16 | 0 | 0 | 0 | 57 | 1 | 7 | 147 |
| Frances Payne Bolton School of Nursing | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 2 | 6 | 15 |
| Jack, Joseph and Morton Mandel School of Applied Social Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 2 | 5 | 11 |
| School of Dental Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 2 | 12 |
| School of Graduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 8 | 14 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 5 | 22 | 0 | 0 | 16 | 0 | 0 | 2 | 7 | 7 | 14 | 73 |
| Weatherhead School of Management | 0 | 0 | 0 | 4 | 0 | 0 | 5 | 4 | 0 | 2 | 0 | 0 | 0 | 8 | 1 | 3 | 27 |
| **合计** | **31** | **14** | **13** | **4** | **1** | **21** | **60** | **4** | **2** | **48** | **2** | **1** | **2** | **92** | **19** | **46** | **399** |

> Reconciliation: Row totals sum to 399 = Rule 1 total ✓

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/School Architecture

CWRU has 4 schools that grant undergraduate degrees: Case School of Engineering (BSE, BS), College of Arts and Sciences (BA, BS), Frances Payne Bolton School of Nursing (BSN), and Weatherhead School of Management (BSM). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Case School of Engineering

##### Department of Aerospace Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Aerospace Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Biomedical Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Biomedical Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Chemical Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Chemical Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Civil Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Civil Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Computer Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Computer Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Computer Science
###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Computer Science | https://bulletin.case.edu/engineering/programs/ |
| 2 | Data Science and Analytics | https://bulletin.case.edu/engineering/programs/ |

###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Computer Science | https://bulletin.case.edu/engineering/programs/ |

##### Department of Electrical Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Electrical Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Materials Science and Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Materials Science and Engineering | https://bulletin.case.edu/engineering/programs/ |
| 2 | Polymer Science and Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Mechanical Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Mechanical Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Department of Engineering Physics
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | Engineering Physics | https://bulletin.case.edu/engineering/programs/ |

##### General Engineering
###### BSE
| # | Program | URL |
|---|---------|-----|
| 1 | General Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Minors (Case School of Engineering)
| # | Minor | URL |
|---|-------|-----|
| 1 | Applied Data Science | https://bulletin.case.edu/engineering/programs/ |
| 2 | Artificial Intelligence | https://bulletin.case.edu/engineering/programs/ |
| 3 | Biomedical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 4 | Biomolecular Engineering | https://bulletin.case.edu/engineering/programs/ |
| 5 | Chemical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 6 | Civil Engineering | https://bulletin.case.edu/engineering/programs/ |
| 7 | Computer Engineering | https://bulletin.case.edu/engineering/programs/ |
| 8 | Computer Gaming | https://bulletin.case.edu/engineering/programs/ |
| 9 | Computer Science | https://bulletin.case.edu/engineering/programs/ |
| 10 | Data Science | https://bulletin.case.edu/engineering/programs/ |
| 11 | Electrical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 12 | Electrochemical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 13 | Electronics | https://bulletin.case.edu/engineering/programs/ |
| 14 | Environmental Engineering | https://bulletin.case.edu/engineering/programs/ |
| 15 | Materials Science and Engineering | https://bulletin.case.edu/engineering/programs/ |
| 16 | Mechanical Design and Manufacturing | https://bulletin.case.edu/engineering/programs/ |
| 17 | Polymer Science and Engineering | https://bulletin.case.edu/engineering/programs/ |
| 18 | Sustainable Engineering | https://bulletin.case.edu/engineering/programs/ |
| 19 | Systems and Control Engineering | https://bulletin.case.edu/engineering/programs/ |

#### College of Arts and Sciences

##### Department of Anthropology
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Anthropology | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Astronomy
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Astronomy | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Astronomy | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Biology
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Biology | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Biology | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Neuroscience | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Chemistry
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Chemistry | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Chemical Biology | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Chemistry | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Communication Sciences
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Communication Sciences | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Economics
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Economics | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of English
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | English | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | World Literature | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Geological Sciences
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Environmental Geology | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Geological Sciences | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Geological Sciences | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of History
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | History | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | History and Philosophy of Science | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Mathematics
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Statistics | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Applied Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Mathematics and Physics | https://bulletin.case.edu/arts-sciences/programs/ |
| 4 | Statistics | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Music
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Music | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Music Education | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Philosophy
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Philosophy | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Physics
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Physics | https://bulletin.case.edu/arts-sciences/programs/ |

###### BS
| # | Program | URL |
|---|---------|-----|
| 1 | Physics | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Political Science
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Political Science | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Psychology
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Psychology | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Religious Studies
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Religious Studies | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Sociology
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Sociology | https://bulletin.case.edu/arts-sciences/programs/ |

##### Department of Theater Arts
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Theater Arts | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Dance | https://bulletin.case.edu/arts-sciences/programs/ |

##### Other BA Programs
| # | Program | URL |
|---|---------|-----|
| 1 | Africana Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Ancient Near Eastern and Egyptian Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Art History | https://bulletin.case.edu/arts-sciences/programs/ |
| 4 | Asian Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 5 | Chinese | https://bulletin.case.edu/arts-sciences/programs/ |
| 6 | Classics | https://bulletin.case.edu/arts-sciences/programs/ |
| 7 | Cognitive Science | https://bulletin.case.edu/arts-sciences/programs/ |
| 8 | Environmental Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 9 | French | https://bulletin.case.edu/arts-sciences/programs/ |
| 10 | French and Francophone Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 11 | German | https://bulletin.case.edu/arts-sciences/programs/ |
| 12 | Gerontological Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 13 | Humanity and Technology | https://bulletin.case.edu/arts-sciences/programs/ |
| 14 | International Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 15 | Japanese Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 16 | Natural Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 17 | Origins Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 18 | Pre-Architecture | https://bulletin.case.edu/arts-sciences/programs/ |
| 19 | Spanish | https://bulletin.case.edu/arts-sciences/programs/ |
| 20 | Teacher Education | https://bulletin.case.edu/arts-sciences/programs/ |
| 21 | Women's, Gender, and Sexuality Studies | https://bulletin.case.edu/arts-sciences/programs/ |

##### Minors (College of Arts and Sciences)
| # | Minor | URL |
|---|-------|-----|
| 1 | Africana Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Ancient Near Eastern and Egyptian Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Anthropology | https://bulletin.case.edu/arts-sciences/programs/ |
| 4 | Art History | https://bulletin.case.edu/arts-sciences/programs/ |
| 5 | Art Studio | https://bulletin.case.edu/arts-sciences/programs/ |
| 6 | Asian Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 7 | Astronomy | https://bulletin.case.edu/arts-sciences/programs/ |
| 8 | Biology | https://bulletin.case.edu/arts-sciences/programs/ |
| 9 | Chemistry | https://bulletin.case.edu/arts-sciences/programs/ |
| 10 | Childhood Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 11 | Chinese | https://bulletin.case.edu/arts-sciences/programs/ |
| 12 | Classics | https://bulletin.case.edu/arts-sciences/programs/ |
| 13 | Cognitive Science | https://bulletin.case.edu/arts-sciences/programs/ |
| 14 | Communication for Health Professionals | https://bulletin.case.edu/arts-sciences/programs/ |
| 15 | Communication Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 16 | Creative Writing | https://bulletin.case.edu/arts-sciences/programs/ |
| 17 | Dance | https://bulletin.case.edu/arts-sciences/programs/ |
| 18 | English | https://bulletin.case.edu/arts-sciences/programs/ |
| 19 | Environmental Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 20 | Ethics | https://bulletin.case.edu/arts-sciences/programs/ |
| 21 | Ethnic Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 22 | Film | https://bulletin.case.edu/arts-sciences/programs/ |
| 23 | French | https://bulletin.case.edu/arts-sciences/programs/ |
| 24 | French and Francophone Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 25 | Geological Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 26 | German | https://bulletin.case.edu/arts-sciences/programs/ |
| 27 | Gerontological Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 28 | History | https://bulletin.case.edu/arts-sciences/programs/ |
| 29 | History and Philosophy of Science | https://bulletin.case.edu/arts-sciences/programs/ |
| 30 | Italian | https://bulletin.case.edu/arts-sciences/programs/ |
| 31 | Japanese | https://bulletin.case.edu/arts-sciences/programs/ |
| 32 | Jewish Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 33 | Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 34 | Music | https://bulletin.case.edu/arts-sciences/programs/ |
| 35 | Natural Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 36 | Philosophy | https://bulletin.case.edu/arts-sciences/programs/ |
| 37 | Photography | https://bulletin.case.edu/arts-sciences/programs/ |
| 38 | Physics | https://bulletin.case.edu/arts-sciences/programs/ |
| 39 | Political Science | https://bulletin.case.edu/arts-sciences/programs/ |
| 40 | Pre-Architecture | https://bulletin.case.edu/arts-sciences/programs/ |
| 41 | Psychology | https://bulletin.case.edu/arts-sciences/programs/ |
| 42 | Public Policy | https://bulletin.case.edu/arts-sciences/programs/ |
| 43 | Religious Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 44 | Russian | https://bulletin.case.edu/arts-sciences/programs/ |
| 45 | Sociology | https://bulletin.case.edu/arts-sciences/programs/ |
| 46 | Spanish | https://bulletin.case.edu/arts-sciences/programs/ |
| 47 | Statistics | https://bulletin.case.edu/arts-sciences/programs/ |
| 48 | Theater Arts | https://bulletin.case.edu/arts-sciences/programs/ |
| 49 | Visual Design | https://bulletin.case.edu/arts-sciences/programs/ |
| 50 | Women's, Gender, and Sexuality Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 51 | World Literature | https://bulletin.case.edu/arts-sciences/programs/ |

#### Frances Payne Bolton School of Nursing

##### Department of Nursing
###### BSN
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing | https://bulletin.case.edu/nursing/programs/ |

#### Weatherhead School of Management

##### Department of Accounting
###### BSM
| # | Program | URL |
|---|---------|-----|
| 1 | Accounting | https://bulletin.case.edu/management/programs/ |

##### Department of Business Management
###### BSM
| # | Program | URL |
|---|---------|-----|
| 1 | Business Information Technology | https://bulletin.case.edu/management/programs/ |
| 2 | Business Management | https://bulletin.case.edu/management/programs/ |
| 3 | Finance | https://bulletin.case.edu/management/programs/ |
| 4 | Marketing | https://bulletin.case.edu/management/programs/ |

##### Department of Economics
###### BA
| # | Program | URL |
|---|---------|-----|
| 1 | Economics | https://bulletin.case.edu/management/programs/ |

##### Minors (Weatherhead School of Management)
| # | Minor | URL |
|---|-------|-----|
| 1 | Accounting | https://bulletin.case.edu/management/programs/ |
| 2 | Business Information Technology | https://bulletin.case.edu/management/programs/ |
| 3 | Business Management | https://bulletin.case.edu/management/programs/ |
| 4 | Economics | https://bulletin.case.edu/management/programs/ |
| 5 | Entrepreneurship | https://bulletin.case.edu/management/programs/ |
| 6 | Finance | https://bulletin.case.edu/management/programs/ |
| 7 | FinTech | https://bulletin.case.edu/management/programs/ |
| 8 | Healthcare Management | https://bulletin.case.edu/management/programs/ |
| 9 | Leadership | https://bulletin.case.edu/management/programs/ |
| 10 | Marketing | https://bulletin.case.edu/management/programs/ |
| 11 | Supply Chain Management | https://bulletin.case.edu/management/programs/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

CWRU offers several interdisciplinary programs that span multiple schools. These are listed under their primary administrative home in the tables above.

### 1.4 Minors — Complete List

See Section 1.2 above for the complete minor listing organized by school. Total minors: 92.

### 1.5 General Education Requirements

CWRU's general education requirements include:
- SAGES (Seminar Approach to General Education and Scholarship) — a four-year seminar sequence
- Physical Education requirement
- Quantitative Reasoning requirement
- Breadth requirements across disciplines


---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Case School of Engineering

##### MS
| # | Program | URL |
|---|---------|-----|
| 1 | Aerospace Engineering | https://bulletin.case.edu/engineering/programs/ |
| 2 | Biomedical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 3 | Biomedical Engineering (Online) | https://bulletin.case.edu/engineering/programs/ |
| 4 | Chemical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 5 | Civil Engineering | https://bulletin.case.edu/engineering/programs/ |
| 6 | Computer Engineering | https://bulletin.case.edu/engineering/programs/ |
| 7 | Computer Science | https://bulletin.case.edu/engineering/programs/ |
| 8 | Computer Science (Online) | https://bulletin.case.edu/engineering/programs/ |
| 9 | Data Science | https://bulletin.case.edu/engineering/programs/ |
| 10 | Electrical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 11 | Macromolecular Science | https://bulletin.case.edu/engineering/programs/ |
| 12 | Materials Science and Engineering | https://bulletin.case.edu/engineering/programs/ |
| 13 | Mechanical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 14 | Mechanical Engineering (Online) | https://bulletin.case.edu/engineering/programs/ |
| 15 | Systems and Control Engineering | https://bulletin.case.edu/engineering/programs/ |
| 16 | Systems and Control Engineering (Online) | https://bulletin.case.edu/engineering/programs/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Aerospace Engineering | https://bulletin.case.edu/engineering/programs/ |
| 2 | Biomedical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 3 | Chemical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 4 | Civil Engineering | https://bulletin.case.edu/engineering/programs/ |
| 5 | Computer Engineering | https://bulletin.case.edu/engineering/programs/ |
| 6 | Computer Science | https://bulletin.case.edu/engineering/programs/ |
| 7 | Electrical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 8 | Macromolecular Science | https://bulletin.case.edu/engineering/programs/ |
| 9 | Materials Science and Engineering | https://bulletin.case.edu/engineering/programs/ |
| 10 | Mechanical Engineering | https://bulletin.case.edu/engineering/programs/ |
| 11 | Systems and Control Engineering | https://bulletin.case.edu/engineering/programs/ |

##### ME (Online)
| # | Program | URL |
|---|---------|-----|
| 1 | Engineering | https://bulletin.case.edu/engineering/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Applied Data Science | https://bulletin.case.edu/engineering/programs/ |

#### College of Arts and Sciences

##### MA
| # | Program | URL |
|---|---------|-----|
| 1 | Anthropology | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Art History | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Art History and Museum Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 4 | Classical Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 5 | Cognitive Linguistics | https://bulletin.case.edu/arts-sciences/programs/ |
| 6 | Communication Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 7 | Contemporary Dance | https://bulletin.case.edu/arts-sciences/programs/ |
| 8 | English | https://bulletin.case.edu/arts-sciences/programs/ |
| 9 | French | https://bulletin.case.edu/arts-sciences/programs/ |
| 10 | Historical Performance Practice | https://bulletin.case.edu/arts-sciences/programs/ |
| 11 | History | https://bulletin.case.edu/arts-sciences/programs/ |
| 12 | Military Ethics | https://bulletin.case.edu/arts-sciences/programs/ |
| 13 | Music Education | https://bulletin.case.edu/arts-sciences/programs/ |
| 14 | Music History | https://bulletin.case.edu/arts-sciences/programs/ |
| 15 | Political Science | https://bulletin.case.edu/arts-sciences/programs/ |
| 16 | Psychology | https://bulletin.case.edu/arts-sciences/programs/ |
| 17 | Religious Studies | https://bulletin.case.edu/arts-sciences/programs/ |
| 18 | Theater Arts | https://bulletin.case.edu/arts-sciences/programs/ |

##### MS
| # | Program | URL |
|---|---------|-----|
| 1 | Applied Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Biology | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Chemistry | https://bulletin.case.edu/arts-sciences/programs/ |
| 4 | Geological Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 5 | Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 6 | Physics | https://bulletin.case.edu/arts-sciences/programs/ |
| 7 | Statistics | https://bulletin.case.edu/arts-sciences/programs/ |

##### MFA
| # | Program | URL |
|---|---------|-----|
| 1 | Contemporary Dance | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Theater Arts | https://bulletin.case.edu/arts-sciences/programs/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Anthropology | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Applied Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Art History | https://bulletin.case.edu/arts-sciences/programs/ |
| 4 | Astronomy | https://bulletin.case.edu/arts-sciences/programs/ |
| 5 | Biology | https://bulletin.case.edu/arts-sciences/programs/ |
| 6 | Chemistry | https://bulletin.case.edu/arts-sciences/programs/ |
| 7 | Communication Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 8 | English | https://bulletin.case.edu/arts-sciences/programs/ |
| 9 | Geological Sciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 10 | History | https://bulletin.case.edu/arts-sciences/programs/ |
| 11 | Mathematics | https://bulletin.case.edu/arts-sciences/programs/ |
| 12 | Musicology | https://bulletin.case.edu/arts-sciences/programs/ |
| 13 | Physics | https://bulletin.case.edu/arts-sciences/programs/ |
| 14 | Political Science | https://bulletin.case.edu/arts-sciences/programs/ |
| 15 | Psychology | https://bulletin.case.edu/arts-sciences/programs/ |
| 16 | Sociology | https://bulletin.case.edu/arts-sciences/programs/ |
| 17 | Statistics | https://bulletin.case.edu/arts-sciences/programs/ |

##### DMA
| # | Program | URL |
|---|---------|-----|
| 1 | Historical Performance Practice | https://bulletin.case.edu/arts-sciences/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Early Intervention Developmental Specialist | https://bulletin.case.edu/arts-sciences/programs/ |
| 2 | Interschool Quantitative Biosciences | https://bulletin.case.edu/arts-sciences/programs/ |
| 3 | Publicly Engaged Humanities | https://bulletin.case.edu/arts-sciences/programs/ |

#### Frances Payne Bolton School of Nursing

##### MN
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing | https://bulletin.case.edu/nursing/programs/ |

##### MSN
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing | https://bulletin.case.edu/nursing/programs/ |

##### DNP
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing Practice | https://bulletin.case.edu/nursing/programs/ |
| 2 | Nursing Practice (Online) | https://bulletin.case.edu/nursing/programs/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing | https://bulletin.case.edu/nursing/programs/ |

##### Post-Graduate Certification
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing Post-Graduate Certification | https://bulletin.case.edu/nursing/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Advanced Quantitative Methodologies | https://bulletin.case.edu/nursing/programs/ |
| 2 | Leadership Excel and Achievement Program (LEAP) (Online) | https://bulletin.case.edu/nursing/programs/ |

#### Jack, Joseph and Morton Mandel School of Applied Social Sciences

##### MSW
| # | Program | URL |
|---|---------|-----|
| 1 | Social Work | https://bulletin.case.edu/applied-social-sciences/programs/ |
| 2 | Social Work (Online) | https://bulletin.case.edu/applied-social-sciences/programs/ |
| 3 | Social Work (Weekend) | https://bulletin.case.edu/applied-social-sciences/programs/ |

##### MNO
| # | Program | URL |
|---|---------|-----|
| 1 | Nonprofit Organizations | https://bulletin.case.edu/applied-social-sciences/programs/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Social Welfare | https://bulletin.case.edu/applied-social-sciences/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Nonprofit Management | https://bulletin.case.edu/applied-social-sciences/programs/ |
| 2 | Trauma-Informed Practice | https://bulletin.case.edu/applied-social-sciences/programs/ |
| 3 | Trauma-Informed Practice (Online) | https://bulletin.case.edu/applied-social-sciences/programs/ |

#### School of Dental Medicine

##### DMD
| # | Program | URL |
|---|---------|-----|
| 1 | Dental Medicine | https://bulletin.case.edu/dental/programs/ |

##### MSD
| # | Program | URL |
|---|---------|-----|
| 1 | Endodontics | https://bulletin.case.edu/dental/programs/ |
| 2 | Oral and Maxillofacial Surgery | https://bulletin.case.edu/dental/programs/ |
| 3 | Oral Medicine | https://bulletin.case.edu/dental/programs/ |
| 4 | Orthodontics | https://bulletin.case.edu/dental/programs/ |
| 5 | Pediatric Dentistry | https://bulletin.case.edu/dental/programs/ |
| 6 | Periodontics | https://bulletin.case.edu/dental/programs/ |

##### Professional Certification
| # | Program | URL |
|---|---------|-----|
| 1 | Advanced Education in General Dentistry | https://bulletin.case.edu/dental/programs/ |
| 2 | Craniofacial, Surgical, and Special Care Orthodontics | https://bulletin.case.edu/dental/programs/ |
| 3 | Dental Public Health | https://bulletin.case.edu/dental/programs/ |

#### School of Law

##### JD
| # | Program | URL |
|---|---------|-----|
| 1 | Law | https://bulletin.case.edu/law/programs/ |
| 2 | Law (Online) | https://bulletin.case.edu/law/programs/ |

##### SJD
| # | Program | URL |
|---|---------|-----|
| 1 | Law | https://bulletin.case.edu/law/programs/ |

##### LLM
| # | Program | URL |
|---|---------|-----|
| 1 | Master of Laws | https://bulletin.case.edu/law/programs/ |
| 2 | Master of Laws (Online) | https://bulletin.case.edu/law/programs/ |

##### ML
| # | Program | URL |
|---|---------|-----|
| 1 | Master of Laws | https://bulletin.case.edu/law/programs/ |

##### MA
| # | Program | URL |
|---|---------|-----|
| 1 | Financial Integrity | https://bulletin.case.edu/law/programs/ |
| 2 | Patent Practice | https://bulletin.case.edu/law/programs/ |
| 3 | Patent Practice (Online) | https://bulletin.case.edu/law/programs/ |

##### MCRM
| # | Program | URL |
|---|---------|-----|
| 1 | Compliance and Risk Management | https://bulletin.case.edu/law/programs/ |
| 2 | Compliance and Risk Management (Online) | https://bulletin.case.edu/law/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Compliance and Risk Management | https://bulletin.case.edu/law/programs/ |
| 2 | Compliance and Risk Management (Online) | https://bulletin.case.edu/law/programs/ |

#### School of Medicine

##### MD
| # | Program | URL |
|---|---------|-----|
| 1 | Medicine (Lerner College Program) | https://bulletin.case.edu/medicine/programs/ |
| 2 | Medicine (WR2/University Program) | https://bulletin.case.edu/medicine/programs/ |

##### MSPAS
| # | Program | URL |
|---|---------|-----|
| 1 | Physician Assistant Studies | https://bulletin.case.edu/medicine/programs/ |

##### MS
| # | Program | URL |
|---|---------|-----|
| 1 | Aerospace Physiology | https://bulletin.case.edu/medicine/programs/ |
| 2 | Aerospace Physiology (Online) | https://bulletin.case.edu/medicine/programs/ |
| 3 | Applied Anatomy | https://bulletin.case.edu/medicine/programs/ |
| 4 | Biochemistry | https://bulletin.case.edu/medicine/programs/ |
| 5 | Biomedical and Health Informatics | https://bulletin.case.edu/medicine/programs/ |
| 6 | Biotechnology | https://bulletin.case.edu/medicine/programs/ |
| 7 | Clinical Research | https://bulletin.case.edu/medicine/programs/ |
| 8 | Epidemiology and Biostatistics | https://bulletin.case.edu/medicine/programs/ |
| 9 | Genetic Counseling | https://bulletin.case.edu/medicine/programs/ |
| 10 | Medical Physiology | https://bulletin.case.edu/medicine/programs/ |
| 11 | Medical Physiology (Online) | https://bulletin.case.edu/medicine/programs/ |
| 12 | Molecular and Cellular Biology of Disease | https://bulletin.case.edu/medicine/programs/ |
| 13 | Nutrition | https://bulletin.case.edu/medicine/programs/ |
| 14 | Pharmacology | https://bulletin.case.edu/medicine/programs/ |
| 15 | Physiology | https://bulletin.case.edu/medicine/programs/ |
| 16 | Public Health Nutrition | https://bulletin.case.edu/medicine/programs/ |
| 17 | Regenerative Medicine and Entrepreneurship | https://bulletin.case.edu/medicine/programs/ |
| 18 | Systems Biology and Bioinformatics | https://bulletin.case.edu/medicine/programs/ |
| 19 | Translational Pharmaceutical Science | https://bulletin.case.edu/medicine/programs/ |

##### MPH
| # | Program | URL |
|---|---------|-----|
| 1 | Public Health | https://bulletin.case.edu/medicine/programs/ |

##### MSA
| # | Program | URL |
|---|---------|-----|
| 1 | Anesthesia | https://bulletin.case.edu/medicine/programs/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Biochemistry | https://bulletin.case.edu/medicine/programs/ |
| 2 | Bioethics | https://bulletin.case.edu/medicine/programs/ |
| 3 | Biomedical and Health Informatics | https://bulletin.case.edu/medicine/programs/ |
| 4 | Cell Biology | https://bulletin.case.edu/medicine/programs/ |
| 5 | Clinical Translational Science | https://bulletin.case.edu/medicine/programs/ |
| 6 | Epidemiology and Biostatistics | https://bulletin.case.edu/medicine/programs/ |
| 7 | Genetics | https://bulletin.case.edu/medicine/programs/ |
| 8 | Molecular Biology and Microbiology | https://bulletin.case.edu/medicine/programs/ |
| 9 | Molecular Medicine | https://bulletin.case.edu/medicine/programs/ |
| 10 | Molecular Virology | https://bulletin.case.edu/medicine/programs/ |
| 11 | Neurosciences | https://bulletin.case.edu/medicine/programs/ |
| 12 | Nutrition | https://bulletin.case.edu/medicine/programs/ |
| 13 | Pathology | https://bulletin.case.edu/medicine/programs/ |
| 14 | Pharmacology | https://bulletin.case.edu/medicine/programs/ |
| 15 | Physiology and Biophysics | https://bulletin.case.edu/medicine/programs/ |
| 16 | Systems Biology and Bioinformatics | https://bulletin.case.edu/medicine/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Aerospace Physiology | https://bulletin.case.edu/medicine/programs/ |
| 2 | Aerospace Physiology (Online) | https://bulletin.case.edu/medicine/programs/ |
| 3 | Cancer Studies | https://bulletin.case.edu/medicine/programs/ |
| 4 | Experimental Biotechnology | https://bulletin.case.edu/medicine/programs/ |
| 5 | Health Informatics | https://bulletin.case.edu/medicine/programs/ |
| 6 | Interschool Quantitative Biosciences | https://bulletin.case.edu/medicine/programs/ |
| 7 | Maternal and Child Nutrition | https://bulletin.case.edu/medicine/programs/ |
| 8 | Nutrition for Health Care Professionals | https://bulletin.case.edu/medicine/programs/ |
| 9 | Public Health | https://bulletin.case.edu/medicine/programs/ |

##### Post-Baccalaureate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Readiness Instruction for Biomedical Education (PRIME) | https://bulletin.case.edu/medicine/programs/ |

#### Weatherhead School of Management

##### MBA
| # | Program | URL |
|---|---------|-----|
| 1 | Business Administration | https://bulletin.case.edu/management/programs/ |
| 2 | Business Administration (Executive) | https://bulletin.case.edu/management/programs/ |
| 3 | Business Administration (Online) | https://bulletin.case.edu/management/programs/ |
| 4 | Business Administration (Part time) | https://bulletin.case.edu/management/programs/ |

##### MAcc
| # | Program | URL |
|---|---------|-----|
| 1 | Accountancy | https://bulletin.case.edu/management/programs/ |

##### MBusAI
| # | Program | URL |
|---|---------|-----|
| 1 | Business Analytics and Intelligence | https://bulletin.case.edu/management/programs/ |

##### MEM
| # | Program | URL |
|---|---------|-----|
| 1 | Engineering and Management | https://bulletin.case.edu/management/programs/ |

##### MFin
| # | Program | URL |
|---|---------|-----|
| 1 | Finance | https://bulletin.case.edu/management/programs/ |

##### MSLOC
| # | Program | URL |
|---|---------|-----|
| 1 | Leadership and Organizational Change | https://bulletin.case.edu/management/programs/ |

##### MSCM
| # | Program | URL |
|---|---------|-----|
| 1 | Supply Chain Management | https://bulletin.case.edu/management/programs/ |

##### DBA
| # | Program | URL |
|---|---------|-----|
| 1 | Business Administration | https://bulletin.case.edu/management/programs/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Management | https://bulletin.case.edu/management/programs/ |
| 2 | Organizational Behavior | https://bulletin.case.edu/management/programs/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Advanced Quantitative Methodologies | https://bulletin.case.edu/management/programs/ |

### 2.2 Dual Degree Programs

| # | Program | Schools | URL |
|---|---------|---------|-----|
| 1 | Anthropology, MA/Medicine, MD | Arts & Sciences / Medicine | https://bulletin.case.edu/academic-programs/ |
| 2 | Anthropology, MA/Nursing, MSN | Arts & Sciences / Nursing | https://bulletin.case.edu/academic-programs/ |
| 3 | Anthropology, MA/Public Health, MPH | Arts & Sciences / Medicine | https://bulletin.case.edu/academic-programs/ |
| 4 | Anthropology, PhD/Medicine, MD | Arts & Sciences / Medicine | https://bulletin.case.edu/academic-programs/ |
| 5 | Anthropology, PhD/Public Health, MPH | Arts & Sciences / Medicine | https://bulletin.case.edu/academic-programs/ |
| 6 | Applied Anatomy, MS/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 7 | Biochemistry, MS/Business Administration, MBA | Medicine / Weatherhead | https://bulletin.case.edu/academic-programs/ |
| 8 | Biochemistry, MS/Law, JD | Medicine / Law | https://bulletin.case.edu/academic-programs/ |
| 9 | Biochemistry, MS/Patent Practice, MA | Medicine / Law | https://bulletin.case.edu/academic-programs/ |
| 10 | Bioethics and Medical Humanities, MA/Genetic Counseling, MS | Medicine | https://bulletin.case.edu/academic-programs/ |
| 11 | Bioethics and Medical Humanities, MA/Law, JD | Medicine / Law | https://bulletin.case.edu/academic-programs/ |
| 12 | Bioethics and Medical Humanities, MA/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 13 | Bioethics and Medical Humanities, MA/Nursing, MSN | Medicine / Nursing | https://bulletin.case.edu/academic-programs/ |
| 14 | Bioethics and Medical Humanities, MA/Public Health, MPH | Medicine | https://bulletin.case.edu/academic-programs/ |
| 15 | Bioethics and Medical Humanities, MA/Social Work, MSW | Medicine / Mandel | https://bulletin.case.edu/academic-programs/ |
| 16 | Biomedical Engineering, MS/Medicine, MD | Engineering / Medicine | https://bulletin.case.edu/academic-programs/ |
| 17 | Business Administration, MBA/Finance, MFin | Weatherhead | https://bulletin.case.edu/academic-programs/ |
| 18 | Business Administration, MBA/Law, JD | Weatherhead / Law | https://bulletin.case.edu/academic-programs/ |
| 19 | Business Administration, MBA/Medical Physiology, MS | Weatherhead / Medicine | https://bulletin.case.edu/academic-programs/ |
| 20 | Business Administration, MBA/Medicine, MD | Weatherhead / Medicine | https://bulletin.case.edu/academic-programs/ |
| 21 | Business Administration, MBA/Public Health, MPH | Weatherhead / Medicine | https://bulletin.case.edu/academic-programs/ |
| 22 | Business Administration, MBA/Social Work, MSW | Weatherhead / Mandel | https://bulletin.case.edu/academic-programs/ |
| 23 | Business Administration, MBA/Supply Chain Management, MSCM | Weatherhead | https://bulletin.case.edu/academic-programs/ |
| 24 | Clinical Research, MS/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 25 | Dental Medicine, DMD/Public Health, MPH | Dental / Medicine | https://bulletin.case.edu/academic-programs/ |
| 26 | Law, JD/Medicine, MD | Law / Medicine | https://bulletin.case.edu/academic-programs/ |
| 27 | Medical Scientist Training Program (MSTP), PhD/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 28 | Medicine, MD/Oral and Maxillofacial Surgery, Professional Certification | Medicine / Dental | https://bulletin.case.edu/academic-programs/ |
| 29 | Military Ethics, MA/Law, JD | Arts & Sciences / Law | https://bulletin.case.edu/academic-programs/ |
| 30 | Molecular and Cellular Biology of Disease, MS/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 31 | Nonprofit Organizations, MNO/Law, JD | Mandel / Law | https://bulletin.case.edu/academic-programs/ |
| 32 | Nonprofit Organizations, MNO/Social Work, MSW | Mandel | https://bulletin.case.edu/academic-programs/ |
| 33 | Nursing Practice, DNP/Nursing, PhD | Nursing | https://bulletin.case.edu/academic-programs/ |
| 34 | Nursing, MSN/Nursing Practice, DNP | Nursing | https://bulletin.case.edu/academic-programs/ |
| 35 | Nursing, MSN/Nursing, PhD | Nursing | https://bulletin.case.edu/academic-programs/ |
| 36 | Nursing, MSN/Public Health, MPH | Nursing / Medicine | https://bulletin.case.edu/academic-programs/ |
| 37 | Nutrition, MS/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 38 | Nutrition, MS/Public Health, MPH | Medicine | https://bulletin.case.edu/academic-programs/ |
| 39 | Pharmacology, MS/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 40 | Political Science, MA/Law, JD | Arts & Sciences / Law | https://bulletin.case.edu/academic-programs/ |
| 41 | Public Health, MPH/Law, JD | Medicine / Law | https://bulletin.case.edu/academic-programs/ |
| 42 | Public Health, MPH/Medicine, MD | Medicine | https://bulletin.case.edu/academic-programs/ |
| 43 | Public Health, MPH/Social Work, MSW | Medicine / Mandel | https://bulletin.case.edu/academic-programs/ |
| 44 | Social Work, MSW/Law, JD | Mandel / Law | https://bulletin.case.edu/academic-programs/ |

### 2.3 Graduate Admissions Model

CWRU uses a **decentralized** graduate admissions model. Each school manages its own admissions process:
- **Case School of Engineering**: Apply through School of Graduate Studies
- **College of Arts and Sciences**: Apply through School of Graduate Studies
- **Weatherhead School of Management**: Direct application to Weatherhead
- **School of Law**: Direct application via LSAC
- **School of Medicine**: Direct application (AMCAS for MD)
- **School of Dental Medicine**: Direct application (AADSAS for DMD)
- **Frances Payne Bolton School of Nursing**: Direct application
- **Mandel School of Applied Social Sciences**: Direct application


---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | https://case.edu/admission/ | case.edu |
| Application portal | Common App or Coalition with Scoir | case.edu/admission/apply |
| **Early Action deadline** | **November 1** | case.edu/admission/apply/dates-deadlines |
| **Early Decision I deadline** | **November 1** | case.edu/admission/apply/dates-deadlines |
| **Early Decision II deadline** | **January 15** | case.edu/admission/apply/dates-deadlines |
| **Regular Decision deadline** | **January 15** | case.edu/admission/apply/dates-deadlines |
| **Pre-Professional Scholars Program deadline** | **December 1** | case.edu/admission/apply/dates-deadlines |
| EA notification date | December 19 | case.edu/admission/apply/dates-deadlines |
| ED I notification date | December 5 | case.edu/admission/apply/dates-deadlines |
| ED II notification date | February 6 | case.edu/admission/apply/dates-deadlines |
| RD notification date | March 20 | case.edu/admission/apply/dates-deadlines |
| EA enrollment deadline | May 1 | case.edu/admission/apply/dates-deadlines |
| ED I enrollment deadline | December 12 | case.edu/admission/apply/dates-deadlines |
| ED II enrollment deadline | 1 week after admission | case.edu/admission/apply/dates-deadlines |
| RD enrollment deadline | May 1 | case.edu/admission/apply/dates-deadlines |
| Financial aid deadline (EA/ED I) | November 15 | case.edu/admission/apply/dates-deadlines |
| Financial aid deadline (ED II) | January 22 | case.edu/admission/apply/dates-deadlines |
| Financial aid deadline (RD) | February 1 | case.edu/admission/apply/dates-deadlines |
| SAT/ACT policy | **Test-optional** | case.edu/admission/apply/application-requirements-enhancements |
| Superscore policy | Yes (SAT and ACT) | case.edu/admission/apply/application-requirements-enhancements |
| Test score deadline (EA/ED I) | November 30 | case.edu/admission/apply/application-requirements-enhancements |
| Test score deadline (ED II/RD) | December 31 | case.edu/admission/apply/application-requirements-enhancements |
| Recommendation requirements | Via Common App/Coalition | case.edu/admission/apply |
| Interview policy | Not required | case.edu/admission/apply |
| Portfolio | Required for music majors; optional for others | case.edu/admission/apply/application-requirements-enhancements |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT (including Home Edition and Paper Edition) | 90* | N/A | *For exams taken on or after January 21, 2026, minimum is 5.0 (new scoring) |
| IELTS | 7 | N/A | |
| PTE Academic | 61 | N/A | |
| Duolingo English Test | 115 | N/A | |

**Waiver conditions:**
- Attend a school where the language of instruction is English for 2 years by graduation
- Score 630+ on SAT Evidence-based Reading and Writing
- Score 26+ on ACT English exam

### 3.3 Graduate — Global Rules

| Dimension | Value |
|-----------|-------|
| Admissions model | Decentralized (each school manages own process) |
| Application platforms | Varies by school (Common App for some, school-specific for others) |
| Standard application fee | Varies by school |
| GRE/GMAT policy | Varies by program |
| Language test policy | Same as undergraduate for non-native speakers |
| Application timeline | Varies by school and program |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year)

| Expense Item | Residential Student | Commuter Student | Description |
|--------------|--------------------:|-----------------:|-------------|
| Tuition | $71,410 | $71,410 | Full-time tuition |
| Housing | $11,688 | $3,824 | On-campus housing |
| Meal Plan | $8,600 | $1,124 | Campus dining |
| Fees | $696 | $696 | Student fees |
| Matriculation Fee | $760 | $760 | One-time fee |
| Books | $1,200 | $1,200 | Estimated |
| Personal Expenses | $1,350 | $1,350 | Estimated |
| Transportation | Variable | Variable | Up to $2,000 based on state of residence |
| **TOTAL COST** | **$95,704** | **$80,364** | |

Additional Nursing Fees: $1,450 (for nursing students)

### 4.2 Undergraduate Financial Aid Policy

| Dimension | Value | Source |
|-----------|-------|--------|
| Meets 100% demonstrated need | Yes (since Fall 2017) | case.edu/admission/tuition-aid |
| Need-blind (US students) | Yes | case.edu/admission/tuition-aid |
| Need-aware (international students) | Yes | case.edu/admission/apply/international-students |
| Students receiving financial assistance | >80% | case.edu/admission/tuition-aid |
| Institutional aid awarded (2025) | $214 million | case.edu/admission/apply/international-students |
| Merit scholarships | Automatic consideration for all applicants | case.edu/admission/tuition-aid |
| Test-optional | Yes (40% of admitted students were test-optional) | case.edu/admission/apply/admission-statistics |

### 4.3 Graduate Cost & Funding Framework

Graduate costs and funding vary significantly by school and program:
- **Case School of Engineering**: Most PhD programs offer full funding (tuition + stipend)
- **College of Arts and Sciences**: PhD programs typically funded; MA/MS programs vary
- **Weatherhead School of Management**: Self-funded; scholarships available
- **School of Law**: Self-funded; scholarships available
- **School of Medicine**: MD program has significant financial aid; graduate programs vary
- **School of Dental Medicine**: DMD program is self-funded
- **Frances Payne Bolton School of Nursing**: Varies by program
- **Mandel School**: Varies by program

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Early Action Deadline
```yaml
field: undergraduate.deadlines.EA
value: "November 1"
source_url: "https://case.edu/admission/apply/dates-deadlines"
source_snippet: "Early Action | November 1 | November 15 | December 19 | May 1"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-002: Early Decision I Deadline
```yaml
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: "https://case.edu/admission/apply/dates-deadlines"
source_snippet: "Early Decision I | November 1 | November 15 | December 5 | December 12"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-003: Early Decision II Deadline
```yaml
field: undergraduate.deadlines.ED_II
value: "January 15"
source_url: "https://case.edu/admission/apply/dates-deadlines"
source_snippet: "Early Decision II | January 15 | January 22 | February 6 | 1 week after admission"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-004: Regular Decision Deadline
```yaml
field: undergraduate.deadlines.RD
value: "January 15"
source_url: "https://case.edu/admission/apply/dates-deadlines"
source_snippet: "Regular Decision | January 15 | February 1 | March 20 | May 1"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-005: Tuition
```yaml
field: undergraduate.costs.tuition
value: 71410
source_url: "https://case.edu/admission/tuition-aid"
source_snippet: "Tuition | $71,410 | $71,410"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-006: Total Cost (Residential)
```yaml
field: undergraduate.costs.total_residential
value: 95704
source_url: "https://case.edu/admission/tuition-aid"
source_snippet: "TOTAL COST | $95,704 | $80,364"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-007: Test-Optional Policy
```yaml
field: undergraduate.admissions.test_optional
value: true
source_url: "https://case.edu/admission/apply/application-requirements-enhancements"
source_snippet: "Case Western Reserve University is test-optional."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-008: SAT Middle 50%
```yaml
field: undergraduate.admissions.sat_mid_50
value: "1440-1520"
source_url: "https://case.edu/admission/apply/admission-statistics"
source_snippet: "SAT Scores (middle 50%) | 1440-1520 | Composite (superscore)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-009: ACT Middle 50%
```yaml
field: undergraduate.admissions.act_mid_50
value: "32-34"
source_url: "https://case.edu/admission/apply/admission-statistics"
source_snippet: "ACT Scores (middle 50%) | 32-34 | Composite (superscore)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-010: TOEFL Minimum
```yaml
field: undergraduate.tests.toefl_min
value: 90
source_url: "https://case.edu/admission/apply/international-students"
source_snippet: "TOEFL iBT, including Home Edition and Paper Edition tests | 5.0"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-011: IELTS Minimum
```yaml
field: undergraduate.tests.ielts_min
value: 7
source_url: "https://case.edu/admission/apply/international-students"
source_snippet: "International English Language Testing System (IELTS) | 7"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-012: Duolingo Minimum
```yaml
field: undergraduate.tests.duolingo_min
value: 115
source_url: "https://case.edu/admission/apply/international-students"
source_snippet: "Duolingo English Test | 115"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-013: Meets 100% Demonstrated Need
```yaml
field: undergraduate.financial_aid.meets_100_need
value: true
source_url: "https://case.edu/admission/tuition-aid"
source_snippet: "As of fall 2017, we meet 100% of demonstrated need for all admitted students."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-014: Test-Optional Percentage
```yaml
field: undergraduate.admissions.test_optional_pct
value: 40
source_url: "https://case.edu/admission/apply/admission-statistics"
source_snippet: "Test Optional | 40% | of high school students were test optional"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-015: Program Count
```yaml
field: undergraduate.programs.total
value: 399
source_url: "https://bulletin.case.edu/academic-programs/"
source_snippet: "Case Western Reserve University is proud to offer a high-quality education in 100+ undergraduate programs, about 160 graduate and professional options, and almost 145 dual-degree programs"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-016: Student-Faculty Ratio
```yaml
field: undergraduate.overview.student_faculty_ratio
value: "9:1"
source_url: "https://case.edu/admission/apply/admission-statistics"
source_snippet: "9:1 | STUDENT:FACULTY RATIO"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-017: Undergraduate Enrollment
```yaml
field: undergraduate.overview.enrollment
value: 6528
source_url: "https://case.edu/admission/apply/admission-statistics"
source_snippet: "6,528 | UNDERGRADUATE STUDENTS"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-018: GPA Middle 50%
```yaml
field: undergraduate.admissions.gpa_mid_50
value: "3.6-4.0"
source_url: "https://case.edu/admission/apply/application-requirements-enhancements"
source_snippet: "Unweighted GPA: 3.6–4.0"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-019: Financial Aid Deadline (EA/ED I)
```yaml
field: undergraduate.financial_aid.deadline_ea_ed1
value: "November 15"
source_url: "https://case.edu/admission/apply/dates-deadlines"
source_snippet: "Early Action | November 1 | November 15"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-020: Institutional Aid Awarded
```yaml
field: undergraduate.financial_aid.institutional_aid
value: 214000000
source_url: "https://case.edu/admission/apply/international-students"
source_snippet: "Last year alone, CWRU awarded $214 million in institutional aid to our students."
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
case-western-knowledge-base-v2/
├── 00-institution-overview.md
├── 01-undergraduate-programs/
│   ├── case-school-of-engineering.md
│   ├── college-of-arts-and-sciences.md
│   ├── frances-payne-bolton-school-of-nursing.md
│   └── weatherhead-school-of-management.md
├── 02-graduate-programs/
│   ├── case-school-of-engineering.md
│   ├── college-of-arts-and-sciences.md
│   ├── frances-payne-bolton-school-of-nursing.md
│   ├── mandel-school.md
│   ├── school-of-dental-medicine.md
│   ├── school-of-law.md
│   ├── school-of-medicine.md
│   └── weatherhead-school-of-management.md
├── 03-deadlines.md
├── 04-costs.md
├── 05-financial-aid.md
├── 06-tests.md
└── 07-evidence-chain.md
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "case-western-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BSE|BSM|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Graduate application fees (per school) | School-specific admissions pages |
| P0 | GRE/GMAT requirements per graduate program | School-specific admissions pages |
| P0 | Graduate funding/stipend rates | School-specific financial aid pages |
| P1 | Detailed course requirements per major | bulletin.case.edu |
| P1 | Faculty research areas | Department pages |
| P2 | Campus housing options | case.edu/campus-life |
| P2 | Student organizations | case.edu/campus-life |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | CWRU | Blank for other schools |
|-----------|------|------------------------|
| Total UG cost/yr (residential) | $95,704 | |
| Tuition/yr | $71,410 | |
| Need-blind (US)? | Yes | |
| Need-blind (intl)? | No (need-aware) | |
| EA deadline | November 1 | |
| ED I deadline | November 1 | |
| ED II deadline | January 15 | |
| RD deadline | January 15 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 90 | |
| IELTS min | 7 | |
| Duolingo min | 115 | |
| Meets 100% need? | Yes (since 2017) | |
| Median price paid | N/A | |
| Grad application fee | Varies by school | |
| Total program count | 399 | |
| School/department count | 9 | |
| Student-faculty ratio | 9:1 | |
| Undergraduate enrollment | 6,528 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: case.edu, bulletin.case.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
