# University of South Carolina Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 99 |
| 本科辅修 (Minor) | 108 |
| 本科证书 (Certificate) | 6 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 202 |
| 研究生高级证书 (Certificate) | 51 |
| **学位项目总计 (UG + Grad)** | **466** |
| 学院 / 独立系所总数 | 13 |

### 0.2 学院 / 系层级结构

```
University of South Carolina (Columbia)
├── McCausland College of Arts and Sciences          [学院]
│   ├── African American Studies                     [系]
│   ├── Anthropology                                 [系]
│   ├── Biological Sciences                          [系]
│   ├── Chemistry and Biochemistry                   [系]
│   ├── Communication Sciences and Disorders         [系]
│   ├── Criminology and Criminal Justice             [系]
│   ├── Dance                                        [系]
│   ├── Earth and Ocean Environment                  [系]
│   ├── Economics                                    [系]
│   ├── English Language and Literature              [系]
│   ├── Environmental Health Sciences                [系]
│   ├── Film and Media                               [系]
│   ├── Geography                                    [系]
│   ├── Geological Sciences                          [系]
│   ├── History                                      [系]
│   ├── Interdisciplinary Studies                    [系]
│   ├── Languages Literatures and Cultures           [系]
│   ├── Mathematics                                  [系]
│   ├── Philosophy                                   [系]
│   ├── Physics and Astronomy                        [系]
│   ├── Political Science                            [系]
│   ├── Psychology                                   [系]
│   ├── Religious Studies                            [系]
│   ├── Sociology                                    [系]
│   ├── Statistics                                   [系]
│   ├── Theatre and Dance                            [系]
│   └── Visual Art and Design                        [系]
├── Darla Moore School of Business                   [学院]
│   ├── Accountancy                                  [系]
│   ├── Business Administration                      [系]
│   ├── Business Analytics                           [系]
│   ├── Economics                                    [系]
│   ├── Finance                                      [系]
│   ├── Management                                   [系]
│   ├── Marketing                                    [系]
│   ├── Operations and Supply Chain                  [系]
│   ├── Real Estate                                  [系]
│   └── Risk Management and Insurance                [系]
├── College of Education                             [学院]
│   ├── Educational Developmental Science            [系]
│   ├── Educational Studies                          [系]
│   ├── Leadership Design Inquiry                    [系]
│   └── Teaching Education                           [系]
├── Molinaroli College of Engineering and Computing  [学院]
│   ├── Biomedical Engineering                       [系]
│   ├── Chemical Engineering                         [系]
│   ├── Civil and Environmental Engineering          [系]
│   ├── Computer Science and Engineering             [系]
│   ├── Electrical Engineering                       [系]
│   ├── Interprofessional Programs                   [系]
│   └── Mechanical Engineering                       [系]
├── College of Hospitality, Retail, and Sport Mgmt   [学院]
│   ├── Hotel Restaurant Tourism Management          [系]
│   ├── Retailing                                    [系]
│   └── Sport and Entertainment Management           [系]
├── College of Information and Communications        [学院]
│   ├── Information and Communications               [系]
│   └── Journalism Mass Communications               [系]
├── School of Medicine                               [学院]
│   ├── Biomedical Sciences                          [系]
│   └── Counseling and Rehabilitation                [系]
├── School of Music                                  [学院]
│   ├── Music Performance                            [系]
│   ├── Music Education                              [系]
│   └── Music Industry                               [系]
├── College of Nursing                               [学院]
│   └── Nursing Practice                             [系]
├── College of Pharmacy                              [学院]
│   ├── Pharmaceutical Sciences                      [系]
│   └── Pharmacy Practice                            [系]
├── Arnold School of Public Health                   [学院]
│   ├── Communication Sciences and Disorders         [系]
│   ├── Environmental Health Sciences                [系]
│   ├── Epidemiology and Biostatistics               [系]
│   ├── Exercise Science                             [系]
│   └── Health Promotion Education and Behavior      [系]
├── College of Social Work                           [学院]
│   └── Social Work                                  [系]
└── South Carolina Honors College                    [学院]
    └── Honors Programs                              [系]
```

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 28 |
| BS | B.S. | Bachelor of Science | 本科 | 22 |
| BSBA | B.S.B.A. | Bachelor of Science in Business Administration | 本科 | 12 |
| BSE | B.S.E. | Bachelor of Science in Engineering | 本科 | 8 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 3 |
| BAJMC | B.A.J.M.C. | Bachelor of Arts in Journalism and Mass Communications | 本科 | 6 |
| BM | B.M. | Bachelor of Music | 本科 | 1 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 2 |
| BSW | B.S.W. | Bachelor of Social Work | 本科 | 1 |
| BSPE | B.S.P.E. | Bachelor of Science in Physical Education | 本科 | 1 |
| BAIS | B.A.I.S. | Bachelor of Arts in Interdisciplinary Studies | 本科 | 1 |
| BSC | B.S.C. | Bachelor of Science in Chemistry | 本科 | 1 |
| BSCS | B.S.C.S. | Bachelor of Science in Computer Science | 本科 | 1 |
| BARSC | BARSC | Bachelor of Interdisciplinary Studies | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 108 |
| Certificate | Certificate | 本科证书 | 本科 | 6 |
| MS | M.S. | Master of Science | 研究生 | 37 |
| MA | M.A. | Master of Arts | 研究生 | 20 |
| MEd | M.Ed. | Master of Education | 研究生 | 9 |
| ME | M.E. | Master of Engineering | 研究生 | 7 |
| MSN | M.S.N. | Master of Science in Nursing | 研究生 | 8 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | 5 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 5 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 3 |
| MBA | P.M.B.A. / I.M.B.A. / E.I.M.B.A. | Master of Business Administration | 研究生 | 3 |
| MM | M.M. | Master of Music | 研究生 | 2 |
| MIB | M.I.B. | Master of International Business | 研究生 | 2 |
| MSL | M.S.L. | Master of Studies in Law | 研究生 | 2 |
| EdS | Ed.S. | Education Specialist | 研究生 | 2 |
| MACC | M.A.C.C. | Master of Accountancy | 研究生 | 1 |
| MAS | M.A.S. | Master of Applied Statistics | 研究生 | 1 |
| MEERM | M.E.E.R.M. | Master of Earth and Environmental Resources Management | 研究生 | 1 |
| MSEM | M.S.E.M. | Master of Science in Engineering Management | 研究生 | 1 |
| MHIT | M.H.I.T. | Master of Health Information Technology | 研究生 | 1 |
| MHA | M.H.A. | Master of Health Administration | 研究生 | 1 |
| MHR | M.H.R. | Master of Human Resources | 研究生 | 1 |
| MIHTM | M.I.H.T.M. | Master of International Hospitality and Tourism Management | 研究生 | 1 |
| MMC | M.M.C. | Master of Mass Communications | 研究生 | 1 |
| MLIS | M.L.I.S. | Master of Library and Information Science | 研究生 | 1 |
| MMEd | M.M.Ed. | Master of Music Education | 研究生 | 1 |
| MR | M.R. | Master of Rehabilitation | 研究生 | 1 |
| MT | M.T. | Master of Teaching | 研究生 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 59 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 6 |
| DPT | D.P.T. | Doctor of Physical Therapy | 研究生 | 1 |
| DNAP | D.N.A.P. | Doctor of Nurse Anesthesia Practice | 研究生 | 1 |
| MD | M.D. | Doctor of Medicine | 研究生 | 1 |
| Certificate | Certificate | 研究生证书 | 研究生 | 51 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSBA | BSE | BFA | BAJMC | BM | BSN | BSW | Minor | UG Cert | MS | MA | MEd | ME | MSN | MAT | MPH | MFA | MBA | PhD | EdD | DNP | Grad Cert | 合计 |
|------------|----|----|------|-----|-----|-------|----|-----|-----|-------|---------|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----------|------|
| Arts & Sciences | 18 | 10 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 42 | 2 | 8 | 12 | 0 | 0 | 0 | 0 | 2 | 0 | 25 | 0 | 0 | 3 | 124 |
| Business | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 4 | 0 | 0 | 6 | 32 |
| Education | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 6 | 0 | 0 | 4 | 0 | 0 | 4 | 1 | 0 | 1 | 24 |
| Engineering & Computing | 0 | 3 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 8 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 3 | 41 |
| Hospitality/Retail/Sport | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 9 |
| Info & Communications | 1 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 12 |
| Medicine | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 6 |
| Music | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 6 | 4 | 21 |
| Pharmacy | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| Public Health | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 3 | 0 | 0 | 6 | 23 |
| Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **25** | **23** | **12** | **8** | **2** | **6** | **1** | **2** | **1** | **61** | **3** | **29** | **14** | **6** | **7** | **8** | **4** | **5** | **3** | **46** | **1** | **6** | **29** | **302** |

> **Note**: This matrix captures the primary degree-granting programs. Some programs (e.g., dual degrees, certificates) may have additional counts not fully reflected. The total of 302 represents degree-granting programs; adding minors (108) and additional certificates brings the total closer to 466.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

USC Columbia has 13 undergraduate-degree-granting colleges/schools. The McCausland College of Arts and Sciences is the largest, offering 30+ majors. The Darla Moore School of Business is known for its #1-ranked international business program. The Molinaroli College of Engineering and Computing offers BSE degrees. The South Carolina Honors College provides enriched academic experiences across all majors.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### McCausland College of Arts and Sciences

##### African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/african-american-studies/african-american-studies-ba/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/anthropology/anthropology-ba/ |

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/biological-sciences/biological-sciences-bs/ |

##### Chemistry and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/chemistry-biochemistry/biochemistry-molecular-biology-bs/ |
| 2 | Chemistry | https://academicbulletins.sc.edu/undergraduate/arts-sciences/chemistry-biochemistry/chemistry-bs/ |
| 3 | Chemistry (B.S.C.) | https://academicbulletins.sc.edu/undergraduate/arts-sciences/chemistry-biochemistry/chemistry-bschem/ |

##### Criminology and Criminal Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice | https://academicbulletins.sc.edu/undergraduate/arts-sciences/criminology-criminal-justice/criminology-criminal-justice-ba/ |

##### Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://academicbulletins.sc.edu/undergraduate/arts-sciences/dance/dance-ba/ |

##### English Language and Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://academicbulletins.sc.edu/undergraduate/arts-sciences/english-language-literature/english-ba/ |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geography/geography-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geography/geography-bs/ |

##### Geological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geological Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geological-sciences/geological-sciences-bs/ |
| 2 | Marine Science | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geological-sciences/marine-science-bs/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://academicbulletins.sc.edu/undergraduate/arts-sciences/history/history-ba/ |

##### Interdisciplinary Studies
###### BARSC
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/interdisciplinary-studies-barsc/ |

##### Languages Literatures and Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Languages, Literatures and Cultures | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/languages-literatures-cultures-ba/ |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/mathematics/mathematics-bs/ |
| 2 | Statistics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/statistics/statistics-bs/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://academicbulletins.sc.edu/undergraduate/arts-sciences/philosophy/philosophy-ba/ |

##### Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/physics-astronomy/physics-bs/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://academicbulletins.sc.edu/undergraduate/arts-sciences/political-science/political-science-ba/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/psychology/psychology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/psychology/psychology-bs/ |
| 2 | Neuroscience | https://academicbulletins.sc.edu/undergraduate/arts-sciences/psychology/neuroscience-bs/ |

##### Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/religious-studies/religious-studies-ba/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/sociology/sociology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/sociology/sociology-bs/ |

##### Theatre and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://academicbulletins.sc.edu/undergraduate/arts-sciences/theatre-dance/theatre-ba/ |

##### Visual Art and Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://academicbulletins.sc.edu/undergraduate/arts-sciences/visual-art-design/art-history-ba/ |
| 2 | Art Studio | https://academicbulletins.sc.edu/undergraduate/arts-sciences/visual-art-design/art-studio-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | https://academicbulletins.sc.edu/undergraduate/arts-sciences/visual-art-design/art-education-bfa/ |
| 2 | Art Studio | https://academicbulletins.sc.edu/undergraduate/arts-sciences/visual-art-design/art-studio-bfa/ |

##### Other Arts & Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cardiovascular Technology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/cardiovascular-technology/cardiovascular-technology-bs/ |
| 2 | Data Science | https://academicbulletins.sc.edu/undergraduate/arts-sciences/data-science/data-science-bs/ |
| 3 | Environmental Science | https://academicbulletins.sc.edu/undergraduate/arts-sciences/environmental-science/environmental-science-bs/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/economics/economics-ba/ |
| 2 | Environmental Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/environmental-studies/environmental-studies-ba/ |
| 3 | Film and Media | https://academicbulletins.sc.edu/undergraduate/arts-sciences/film-and-media/film-and-media-ba/ |
| 4 | Global Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/global-studies/global-studies-ba/ |
| 5 | International Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/international-studies/international-studies-ba/ |
| 6 | Liberal Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/liberal-studies/liberal-studies-ba/ |
| 7 | Women's and Gender Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/womens-gender-studies/womens-gender-studies-ba/ |

---

#### Darla Moore School of Business

##### Accountancy
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://academicbulletins.sc.edu/undergraduate/business/accounting-bsba/ |

##### Business Administration
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Business | https://academicbulletins.sc.edu/undergraduate/business/international-business-bsba/ |
| 2 | Management | https://academicbulletins.sc.edu/undergraduate/business/management-bsba/ |
| 3 | Marketing | https://academicbulletins.sc.edu/undergraduate/business/marketing-bsba/ |
| 4 | Operations and Supply Chain | https://academicbulletins.sc.edu/undergraduate/business/operations-supply-chain-bsba/ |
| 5 | Real Estate | https://academicbulletins.sc.edu/undergraduate/business/real-estate-bsba/ |
| 6 | Risk Management and Insurance | https://academicbulletins.sc.edu/undergraduate/business/risk-management-insurance-bsba/ |

##### Economics
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://academicbulletins.sc.edu/undergraduate/business/economics/business-economics-bsba/ |

##### Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://academicbulletins.sc.edu/undergraduate/business/finance-bsba/ |

---

#### College of Education

##### Educational Developmental Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Sport Psychology and Counseling | https://academicbulletins.sc.edu/undergraduate/education/educational-developmental-science/applied-sport-psychology-counseling-bs/ |

##### Teaching Education
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://academicbulletins.sc.edu/undergraduate/education/teaching-education/early-childhood-education-ba/ |
| 2 | Elementary Education | https://academicbulletins.sc.edu/undergraduate/education/teaching-education/elementary-education-ba/ |
| 3 | Middle Level Education | https://academicbulletins.sc.edu/undergraduate/education/teaching-education/middle-level-education-ba/ |
| 4 | Special Education | https://academicbulletins.sc.edu/undergraduate/education/teaching-education/special-education-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Middle Level Education | https://academicbulletins.sc.edu/undergraduate/education/teaching-education/middle-level-education-bs/ |
| 2 | Physical Education | https://academicbulletins.sc.edu/undergraduate/education/teaching-education/physical-education-bspe/ |

---

#### Molinaroli College of Engineering and Computing

##### Biomedical Engineering
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/biomedical-engineering/biomedical-engineering-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/biomedical-engineering/biomedical-engineering-bs/ |

##### Chemical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/chemical-engineering/chemical-engineering-bse/ |

##### Civil and Environmental Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/civil-environmental-engineering/civil-engineering-bse/ |

##### Computer Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/computer-science-bscs/ |
| 2 | Computer Information Systems | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/computer-information-systems-bs/ |
| 3 | Cyber Intelligence | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/cyber-intelligence-bs/ |
| 4 | Cyber Policy and Ethics | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/cyber-policy-ethics-bs/ |
| 5 | Data Analytics | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/data-analytics-bs/ |
| 6 | Information Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/information-science-bs/ |
| 7 | Integrated Information Technology | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/integrated-information-technology-bs/ |

###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/computer-engineering-bse/ |

##### Electrical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/electrical-engineering/electrical-engineering-bse/ |

##### Mechanical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/mechanical-engineering/aerospace-engineering-bse/ |
| 2 | Industrial Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/industrial-engineering/industrial-engineering-bs/ |
| 3 | Mechanical Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/mechanical-engineering/mechanical-engineering-bse/ |

---

#### College of Hospitality, Retail, and Sport Management

##### Hotel Restaurant Tourism Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/hotel-restaurant-tourism-management/hospitality-management-bs/ |
| 2 | Tourism Management | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/hotel-restaurant-tourism-management/tourism-management-bs/ |

##### Retailing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Retailing | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/retailing/retailing-bs/ |

##### Sport and Entertainment Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport and Entertainment Management | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/sport-entertainment-management/sport-entertainment-management-bs/ |

---

#### College of Information and Communications

##### Information and Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://academicbulletins.sc.edu/undergraduate/information-communications/information-communication-studies/communication-ba/ |

##### Journalism Mass Communications
###### BAJMC
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/advertising-bajmc/ |
| 2 | Broadcast Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/broadcast-journalism-bajmc/ |
| 3 | Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/journalism-bajmc/ |
| 4 | Mass Communications | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/mass-communications-bajmc/ |
| 5 | Public Relations | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/public-relations-bajmc/ |
| 6 | Visual Communications | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/visual-communications-bajmc/ |
| 7 | Sports Media | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/sports-media-ba/ |

---

#### School of Medicine

##### Biomedical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://academicbulletins.sc.edu/undergraduate/medicine/pharmaceutical-sciences-bs/ |

---

#### School of Music

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://academicbulletins.sc.edu/undergraduate/music/music-ba/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://academicbulletins.sc.edu/undergraduate/music/music-bm/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Industry Studies | https://academicbulletins.sc.edu/undergraduate/music/music-industry-studies-bs/ |

---

#### College of Nursing

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing-Generic | https://academicbulletins.sc.edu/undergraduate/nursing/nursing-generic-bsn/ |
| 2 | Nursing-R.N. | https://academicbulletins.sc.edu/undergraduate/nursing/nursing-rn-bsn/ |

---

#### College of Pharmacy

##### Pharmaceutical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://academicbulletins.sc.edu/undergraduate/pharmacy/pharmaceutical-sciences-bs/ |

---

#### Arnold School of Public Health

##### Exercise Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Science | https://academicbulletins.sc.edu/undergraduate/public-health/exercise-science/exercise-science-bs/ |

##### Health Promotion Education and Behavior
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://academicbulletins.sc.edu/undergraduate/public-health/health-promotion-education-behavior/public-health-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://academicbulletins.sc.edu/undergraduate/public-health/health-promotion-education-behavior/public-health-bs/ |

---

#### College of Social Work

##### Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://academicbulletins.sc.edu/undergraduate/social-work/social-work-bsw/ |

---

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | URL | 主管学院 |
|---|------|-----|----------|
| 1 | Services Management, B.A.I.S. | https://academicbulletins.sc.edu/undergraduate/arts-sciences/ | Arts & Sciences |
| 2 | Interdisciplinary Studies, BARSC | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/interdisciplinary-studies-barsc/ | Arts & Sciences |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 | Actuarial Mathematics and Statistics | Arts & Sciences/Mathematics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/mathematics/actuarial-mathematics-statistics-minor/ |
| 2 | Advertising and Public Relations | Info & Communications/Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/advertising-and-public-relations-minor/ |
| 3 | Aerospace Engineering | Engineering/Mechanical Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/mechanical-engineering/aerospace-engineering-minor/ |
| 4 | Aerospace Studies | Arts & Sciences/ROTC | https://academicbulletins.sc.edu/undergraduate/arts-sciences/rotc/aerospace-studies-minor/ |
| 5 | African American Studies | Arts & Sciences/African American Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/african-american-studies/african-american-studies-minor/ |
| 6 | African Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/african-studies-minor/ |
| 7 | Ancient Greek Literature | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/ancient-greek-literature-minor/ |
| 8 | Anthropology | Arts & Sciences/Anthropology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/anthropology/anthropology-minor/ |
| 9 | Applied Computing | Engineering/Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/applied-computing-minor/ |
| 10 | Arabic Studies | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/arabic-studies-minor/ |
| 11 | Art History | Arts & Sciences/Visual Art | https://academicbulletins.sc.edu/undergraduate/arts-sciences/visual-art-design/art-history-minor/ |
| 12 | Art Studio | Arts & Sciences/Visual Art | https://academicbulletins.sc.edu/undergraduate/arts-sciences/visual-art-design/art-studio-minor/ |
| 13 | Asian Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/asian-studies-minor/ |
| 14 | Astronomy | Arts & Sciences/Physics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/physics-astronomy/astronomy-minor/ |
| 15 | Athletic Coaching | Education | https://academicbulletins.sc.edu/undergraduate/education/educational-developmental-science/-athletic-coaching-minor/ |
| 16 | Audio Recording | Music | https://academicbulletins.sc.edu/undergraduate/music/audio-recording-minor/ |
| 17 | Beverage Management | Hospitality | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/hotel-restaurant-tourism-management/beverage-management-minor/ |
| 18 | Biology | Arts & Sciences/Biological Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/biological-sciences/biology-minor/ |
| 19 | Business Administration | Business | https://academicbulletins.sc.edu/undergraduate/business/business-administration-minor/ |
| 20 | Chemical Engineering | Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/chemical-engineering/chemical-engineering-minor/ |
| 21 | Chemistry | Arts & Sciences/Chemistry | https://academicbulletins.sc.edu/undergraduate/arts-sciences/chemistry-biochemistry/chemistry-minor/ |
| 22 | Chinese Studies | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/chinese-studies-minor/ |
| 23 | Civics and Humanities | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/civics-and-humanities-minor/ |
| 24 | Classical Studies | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/classical-studies-minor/ |
| 25 | Climate and Society | Arts & Sciences/Geography | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geography/climate-society-minor/ |
| 26 | Comparative Literature | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/comparative-literature-minor/ |
| 27 | Computer Science | Engineering/Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/computer-science-minor/ |
| 28 | Counselor Education | Education | https://academicbulletins.sc.edu/undergraduate/education/counselor-education-minor/ |
| 29 | Creative Writing | Arts & Sciences/English | https://academicbulletins.sc.edu/undergraduate/arts-sciences/english-language-literature/creative-writing-minor/ |
| 30 | Criminal Justice | Arts & Sciences/Criminology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/criminology-criminal-justice/criminal-justice-minor/ |
| 31 | Cybersecurity Operations | Engineering/Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/cybersecurity-operations-minor/ |
| 32 | Dance | Arts & Sciences/Dance | https://academicbulletins.sc.edu/undergraduate/arts-sciences/dance/dance-minor/ |
| 33 | Data Science | Arts & Sciences/Data Science | https://academicbulletins.sc.edu/undergraduate/arts-sciences/data-science/data-science-minor/ |
| 34 | Economics | Arts & Sciences/Economics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/economics/economics-minor/ |
| 35 | Education | Education | https://academicbulletins.sc.edu/undergraduate/education/education-minor/ |
| 36 | Electrical Engineering | Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/electrical-engineering/electrical-engineering-minor/ |
| 37 | English | Arts & Sciences/English | https://academicbulletins.sc.edu/undergraduate/arts-sciences/english-language-literature/english-minor/ |
| 38 | Entrepreneurship | Business | https://academicbulletins.sc.edu/undergraduate/business/entrepreneurship-minor/ |
| 39 | Environmental and Sustainable Engineering | Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/environmental-sustainable-engineering-minor/ |
| 40 | Environmental Studies | Arts & Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/environmental-studies/environmental-studies-minor/ |
| 41 | European Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/european-studies-minor/ |
| 42 | Event Management | Hospitality | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/event-management-minor/ |
| 43 | Film and Media Studies | Arts & Sciences/Film | https://academicbulletins.sc.edu/undergraduate/arts-sciences/film-and-media/film-and-media-studies-minor/ |
| 44 | Foreign Language Education | Education | https://academicbulletins.sc.edu/undergraduate/education/foreign-language-education-minor/ |
| 45 | Forensics | Arts & Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/forensics-minor/ |
| 46 | Francophone Studies | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/francophone-studies-minor/ |
| 47 | Geography | Arts & Sciences/Geography | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geography/geography-minor/ |
| 48 | Geological Sciences | Arts & Sciences/Geology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geological-sciences/geological-sciences-minor/ |
| 49 | Geophysics | Arts & Sciences/Geology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geological-sciences/geophysics-minor/ |
| 50 | German | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/german-minor/ |
| 51 | German Studies | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/german-studies-minor/ |
| 52 | Health Promotion, Education, and Behavior | Public Health | https://academicbulletins.sc.edu/undergraduate/public-health/health-promotion-education-behavior/health-promotion-education-behavior-minor/ |
| 53 | History | Arts & Sciences/History | https://academicbulletins.sc.edu/undergraduate/arts-sciences/history/history-minor/ |
| 54 | Hospitality and Tourism Management | Hospitality | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/hospitality-tourism-management-minor/ |
| 55 | Informatics | Engineering/Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/informatics-minor/ |
| 56 | Integrated Information Technology | Engineering/Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/integrated-information-technology-minor/ |
| 57 | International Studies | Arts & Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/international-studies/international-studies-minor/ |
| 58 | Islamic World Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/islamic-world-studies-minor/ |
| 59 | Italian | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/italian-minor/ |
| 60 | Japanese | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/japanese-minor/ |
| 61 | Jewish Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/jewish-studies-minor/ |
| 62 | Latin American, Caribbean, and US Latinx Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/latin-american-caribbean-us-latinx-studies-minor/ |
| 63 | Latin | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/latin-minor/ |
| 64 | Law and Society Interdisciplinary | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/law-and-society-interdisciplinary-minor/ |
| 65 | Leadership Studies | Education | https://academicbulletins.sc.edu/undergraduate/education/leadership-studies-minor/ |
| 66 | Linguistics | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/linguistics-minor/ |
| 67 | Marine Science | Arts & Sciences/Geology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/geological-sciences/marine-science-minor/ |
| 68 | Mass Communications | Info & Communications/Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/mass-communications-minor/ |
| 69 | Mathematical Biology | Arts & Sciences/Mathematics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/mathematics/mathematical-biology-minor/ |
| 70 | Mathematics | Arts & Sciences/Mathematics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/mathematics/mathematics-minor/ |
| 71 | Mechanical Engineering | Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/mechanical-engineering/mechanical-engineering-minor/ |
| 72 | Media Arts | Arts & Sciences/Film | https://academicbulletins.sc.edu/undergraduate/arts-sciences/film-and-media/media-arts-minor/ |
| 73 | Medical Anthropology | Arts & Sciences/Anthropology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/anthropology/medical-anthropology-minor/ |
| 74 | Medical Humanities and Culture | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/medical-humanities-and-culture-minor/ |
| 75 | Middle East Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/middle-east-studies-minor/ |
| 76 | Military Science | Arts & Sciences/ROTC | https://academicbulletins.sc.edu/undergraduate/arts-sciences/rotc/military-science-minor/ |
| 77 | Music Entrepreneurship | Music | https://academicbulletins.sc.edu/undergraduate/music/music-entrepreneurship-minor/ |
| 78 | Music Industry Studies | Music | https://academicbulletins.sc.edu/undergraduate/music/music-industry-studies-minor/ |
| 79 | Music | Music | https://academicbulletins.sc.edu/undergraduate/music/music-minor/ |
| 80 | Naval Science | Arts & Sciences/ROTC | https://academicbulletins.sc.edu/undergraduate/arts-sciences/rotc/naval-science-minor/ |
| 81 | Neuroscience | Arts & Sciences/Psychology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/psychology/neuroscience-minor/ |
| 82 | Nuclear Engineering | Engineering | https://academicbulletins.sc.edu/undergraduate/engineering-computing/nuclear-engineering-minor/ |
| 83 | Nutrition and Food Systems | Public Health | https://academicbulletins.sc.edu/undergraduate/public-health/nutrition-food-systems-minor/ |
| 84 | Philosophy | Arts & Sciences/Philosophy | https://academicbulletins.sc.edu/undergraduate/arts-sciences/philosophy/philosophy-minor/ |
| 85 | Physics | Arts & Sciences/Physics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/physics-astronomy/physics-minor/ |
| 86 | Political Science | Arts & Sciences/Political Science | https://academicbulletins.sc.edu/undergraduate/arts-sciences/political-science/political-science-minor/ |
| 87 | Portuguese | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/portuguese-minor/ |
| 88 | Professional Writing and Communication | Arts & Sciences/English | https://academicbulletins.sc.edu/undergraduate/arts-sciences/english-language-literature/professional-writing-communication-minor/ |
| 89 | Psychology | Arts & Sciences/Psychology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/psychology/psychology-minor/ |
| 90 | Religious Studies | Arts & Sciences/Religious Studies | https://academicbulletins.sc.edu/undergraduate/arts-sciences/religious-studies/religious-studies-minor/ |
| 91 | Renaissance Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/renaissance-studies-minor/ |
| 92 | Retailing | Hospitality/Retailing | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/retailing/retailing-minor/ |
| 93 | Risk Management and Insurance | Business | https://academicbulletins.sc.edu/undergraduate/business/risk-management-insurance-minor/ |
| 94 | Russian | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/russian-minor/ |
| 95 | Slavic, East-Central European and Eurasian Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/slavic-east-central-european-eurasian-studies-minor/ |
| 96 | Social Media and Mass Communications | Info & Communications/Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/social-media-mass-communications-minor/ |
| 97 | Social Work | Social Work | https://academicbulletins.sc.edu/undergraduate/social-work/social-work-minor/ |
| 98 | Sociology | Arts & Sciences/Sociology | https://academicbulletins.sc.edu/undergraduate/arts-sciences/sociology/sociology-minor/ |
| 99 | Southern Studies | Arts & Sciences/Interdisciplinary | https://academicbulletins.sc.edu/undergraduate/arts-sciences/interdisciplinary-studies/southern-studies-minor/ |
| 100 | Spanish | Arts & Sciences/Languages | https://academicbulletins.sc.edu/undergraduate/arts-sciences/languages-literatures-cultures/spanish-minor/ |
| 101 | Speech Communication | Arts & Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/speech-communication-minor/ |
| 102 | Sport and Entertainment Management | Hospitality | https://academicbulletins.sc.edu/undergraduate/hospitality-retail-sport-management/sport-entertainment-management/sport-entertainment-management-minor/ |
| 103 | Sports Media | Info & Communications/Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/sports-media-minor/ |
| 104 | Statistics | Arts & Sciences/Statistics | https://academicbulletins.sc.edu/undergraduate/arts-sciences/statistics/statistics-minor/ |
| 105 | Theatre | Arts & Sciences/Theatre | https://academicbulletins.sc.edu/undergraduate/arts-sciences/theatre-dance/theatre-minor/ |
| 106 | User Experience and Design | Engineering/Computer Science | https://academicbulletins.sc.edu/undergraduate/engineering-computing/computer-science-engineering/user-experience-design-minor/ |
| 107 | Visual Communications | Info & Communications/Journalism | https://academicbulletins.sc.edu/undergraduate/information-communications/journalism-mass-communications/visual-communications-minor/ |
| 108 | Women's and Gender Studies | Arts & Sciences | https://academicbulletins.sc.edu/undergraduate/arts-sciences/womens-gender-studies/womens-gender-studies-minor/ |

### 1.5 General/Institute-wide requirements

**Carolina Core** — USC's general education curriculum requires courses in:
- Analytical Reasoning and Problem Solving
- Arts, Literature, and Philosophy
- Culture and Foreign Language
- History
- Social Sciences
- Science, Technology, and Mathematics
- English Composition
- Founding Documents (required for all degrees)

### 1.6 Course-ID → Major quick-lookup

USC does not use a course-ID numbering system for majors. Programs are identified by name and degree code (e.g., "Accounting, B.S.B.A.").

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### McCausland College of Arts and Sciences

##### Anthropology
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/anthropology/anthropology-ma/ |
| 2 | Anthropology | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/anthropology/anthropology-phd/ |

##### Biological Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Sciences | M.S. | https://academicbulletins.sc.edu/graduate/arts-sciences/biological-sciences/biological-sciences-ms/ |
| 2 | Biological Sciences | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/biological-sciences/biological-sciences-phd/ |

##### Chemistry and Biochemistry
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | M.S. | https://academicbulletins.sc.edu/graduate/arts-sciences/chemistry-biochemistry/chemistry-ms/ |
| 2 | Chemistry | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/chemistry-biochemistry/chemistry-phd/ |

##### Criminology and Criminal Justice
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Criminology and Criminal Justice | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/criminology-criminal-justice/criminology-criminal-justice-ma/ |
| 2 | Criminology and Criminal Justice | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/criminology-criminal-justice/criminology-criminal-justice-phd/ |

##### Economics
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Economics | M.A. | https://academicbulletins.sc.edu/graduate/business/economics/economics-ma/ |
| 2 | Economics | Ph.D. | https://academicbulletins.sc.edu/graduate/business/economics/economics-phd/ |

##### English Language and Literature
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | English | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/english-language-literature/english-ma/ |
| 2 | English | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/english-language-literature/english-phd/ |
| 3 | Creative Writing | M.F.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/english-language-literature/creative-writing-mfa/ |

##### History
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | History | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/history/history-ma/ |
| 2 | History | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/history/history-phd/ |

##### Languages Literatures and Cultures
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Comparative Literature | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/languages-literatures-cultures/comparative-literature-phd/ |

##### Mathematics
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | M.S. | https://academicbulletins.sc.edu/graduate/arts-sciences/mathematics/mathematics-ms/ |
| 2 | Mathematics | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/mathematics/mathematics-phd/ |

##### Philosophy
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/philosophy/philosophy-ma/ |
| 2 | Philosophy | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/philosophy/philosophy-phd/ |

##### Physics and Astronomy
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics | M.S. | https://academicbulletins.sc.edu/graduate/arts-sciences/physics-astronomy/physics-ms/ |
| 2 | Physics | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/physics-astronomy/physics-phd/ |

##### Political Science
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/political-science/political-science-ma/ |
| 2 | Political Science | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/political-science/political-science-phd/ |

##### Psychology
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/psychology/psychology-phd/ |

##### Sociology
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/sociology/sociology-ma/ |
| 2 | Sociology | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/sociology/sociology-phd/ |

##### Statistics
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Statistics | M.A.S. | https://academicbulletins.sc.edu/graduate/arts-sciences/statistics/applied-statistics-mas/ |
| 2 | Statistics | M.S. | https://academicbulletins.sc.edu/graduate/arts-sciences/statistics/statistics-ms/ |
| 3 | Statistics | Ph.D. | https://academicbulletins.sc.edu/graduate/arts-sciences/statistics/statistics-phd/ |
| 4 | Applied Statistics | Certificate | https://academicbulletins.sc.edu/graduate/arts-sciences/statistics/applied-statistics-certificate/ |

##### Theatre and Dance
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Dance Studies | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/theatre-dance/dance-studies-ma/ |

##### Visual Art and Design
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art Education | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/visual-art-design/art-education-ma/ |
| 2 | Art Education | M.A.T. | https://academicbulletins.sc.edu/graduate/arts-sciences/visual-art-design/art-education-mat-p-12-certification/ |
| 3 | Art History | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/visual-art-design/art-history-ma/ |
| 4 | Art Studio | M.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/visual-art-design/art-studio-ma/ |
| 5 | Art Studio | M.F.A. | https://academicbulletins.sc.edu/graduate/arts-sciences/visual-art-design/art-studio-mfa/ |

##### Earth and Ocean Environment
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth and Environmental Resources Management | M.E.E.R.M. | https://academicbulletins.sc.edu/graduate/arts-sciences/earth-ocean-environment/earth-environmental-resources-management-meerm/ |

---

#### Darla Moore School of Business

##### Accountancy
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | M.A.C.C. | https://academicbulletins.sc.edu/graduate/business/accountancy-macc/ |
| 2 | Accounting and Audit Analytics | Certificate | https://academicbulletins.sc.edu/graduate/business/accounting-audit-analytics-certificate/ |

##### Business Administration
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Administration | M.S. | https://academicbulletins.sc.edu/graduate/business/business-administration-ms/ |
| 2 | Business Administration (Professional MBA) | P.M.B.A. | https://academicbulletins.sc.edu/graduate/business/business-administration-pmba/ |
| 3 | Business Administration | Ph.D. | https://academicbulletins.sc.edu/graduate/business/business-administration-phd/ |
| 4 | Artificial Intelligence in Business | Certificate | https://academicbulletins.sc.edu/graduate/business/artificial-intelligence-business-certificate/ |
| 5 | Business Analytics | Certificate | https://academicbulletins.sc.edu/graduate/business/business-analytics-certificate/ |
| 6 | Business Analytics | M.S. | https://academicbulletins.sc.edu/graduate/business/business-analytics-ms/ |
| 7 | Cost Management | Certificate | https://academicbulletins.sc.edu/graduate/business/cost-management-certificate/ |
| 8 | Cybersecurity Management | Certificate | https://academicbulletins.sc.edu/graduate/business/cybersecurity-management-certificate/ |
| 9 | Enterprise Resource Planning Systems | Certificate | https://academicbulletins.sc.edu/graduate/business/enterprise-resource-planning-systems-certificate/ |

##### International Business
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | International Business | M.I.B. | https://academicbulletins.sc.edu/graduate/business/international-business-mib/ |
| 2 | International MBA | I.M.B.A. | https://academicbulletins.sc.edu/graduate/business/international-mba-imba/ |
| 3 | Executive International MBA | E.I.M.B.A. | https://academicbulletins.sc.edu/graduate/business/executive-international-mba-eimba/ |

---

#### College of Education

##### Educational Developmental Science
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Adapted Physical Education | M.S. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/adapted-physical-education-ms/ |
| 2 | Applied Behavior Analysis | M.Ed. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/applied-behavior-analysis-med/ |
| 3 | Coaching Education | M.S. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/coaching-education-ms/ |
| 4 | Counselor Education | Ed.S. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/counselor-education-eds/ |
| 5 | Counselor Education | Ph.D. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/counselor-education-phd/ |
| 6 | Educational Psychology and Research | M.Ed. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/educational-psychology-research-med/ |
| 7 | Educational Psychology and Research | Ph.D. | https://academicbulletins.sc.edu/graduate/education/educational-developmental-science/educational-psychology-research-phd/ |

##### Educational Studies
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Educational Practice and Innovation | Ed.D. | https://academicbulletins.sc.edu/graduate/education/educational-studies/curriculum-instruction-edd/ |

##### Leadership Design Inquiry
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Education Administration | Ed.S. | https://academicbulletins.sc.edu/graduate/education/leadership-design-inquiry/education-administration-eds/ |
| 2 | Education Administration | M.Ed. | https://academicbulletins.sc.edu/graduate/education/leadership-design-inquiry/education-administration-med/ |
| 3 | Education Administration | Ph.D. | https://academicbulletins.sc.edu/graduate/education/leadership-design-inquiry/education-administration-phd/ |

##### Teaching Education
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Early Childhood Education | M.Ed. | https://academicbulletins.sc.edu/graduate/education/teaching-education/early-childhood-education-med/ |
| 2 | Elementary Education | M.A.T. | https://academicbulletins.sc.edu/graduate/education/initial-teacher-certification-programs/elementary-education-mat-2-6-certification/ |

---

#### Molinaroli College of Engineering and Computing

##### Biomedical Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | M.E. | https://academicbulletins.sc.edu/graduate/engineering-computing/biomedical-engineering/biomedical-engineering-me/ |
| 2 | Biomedical Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/biomedical-engineering/biomedical-engineering-ms/ |
| 3 | Biomedical Engineering | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/biomedical-engineering/biomedical-engineering-phd/ |

##### Chemical Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | M.E. | https://academicbulletins.sc.edu/graduate/engineering-computing/chemical-engineering/chemical-engineering-me/ |
| 2 | Chemical Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/chemical-engineering/chemical-engineering-ms/ |
| 3 | Chemical Engineering | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/chemical-engineering/chemical-engineering-phd/ |

##### Civil and Environmental Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering | M.E. | https://academicbulletins.sc.edu/graduate/engineering-computing/civil-environmental-engineering/civil-engineering-me/ |
| 2 | Civil Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/civil-environmental-engineering/civil-engineering-ms/ |
| 3 | Civil Engineering | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/civil-environmental-engineering/civil-engineering-phd/ |

##### Computer Science and Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/computer-science-engineering/computer-engineering-ms/ |
| 2 | Computer Engineering | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/computer-science-engineering/computer-engineering-phd/ |
| 3 | Computer Science | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/computer-science-engineering/computer-science-ms/ |
| 4 | Computer Science | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/computer-science-engineering/computer-science-phd/ |
| 5 | Artificial Intelligence | Certificate | https://academicbulletins.sc.edu/graduate/engineering-computing/computer-science-engineering/artificial-intelligence-certificate/ |
| 6 | Cyber Security Studies | Certificate | https://academicbulletins.sc.edu/graduate/engineering-computing/computer-science-engineering/cyber-security-studies-certificate/ |

##### Electrical Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical Engineering | M.E. | https://academicbulletins.sc.edu/graduate/engineering-computing/electrical-engineering/electrical-engineering-me/ |
| 2 | Electrical Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/electrical-engineering/electrical-engineering-ms/ |
| 3 | Electrical Engineering | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/electrical-engineering/electrical-engineering-phd/ |

##### Mechanical Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | M.E. | https://academicbulletins.sc.edu/graduate/engineering-computing/mechanical-engineering/aerospace-engineering-me/ |
| 2 | Aerospace Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/mechanical-engineering/aerospace-engineering-ms/ |
| 3 | Mechanical Engineering | M.E. | https://academicbulletins.sc.edu/graduate/engineering-computing/mechanical-engineering/mechanical-engineering-me/ |
| 4 | Mechanical Engineering | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/mechanical-engineering/mechanical-engineering-ms/ |
| 5 | Mechanical Engineering | Ph.D. | https://academicbulletins.sc.edu/graduate/engineering-computing/mechanical-engineering/mechanical-engineering-phd/ |

##### Interprofessional Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Engineering Management | M.S. | https://academicbulletins.sc.edu/graduate/engineering-computing/interprofessional-programs/engineering-management-ms/ |

---

#### College of Hospitality, Retail, and Sport Management

##### Hotel Restaurant Tourism Management
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | International Hospitality and Tourism Management | M.I.H.T.M. | https://academicbulletins.sc.edu/graduate/hospitality-retail-sport-management/hotel-restaurant-tourism-management/international-hospitality-tourism-management-mihtm/ |
| 2 | Asset Management in Hospitality | Certificate | https://academicbulletins.sc.edu/graduate/hospitality-retail-sport-management/hotel-restaurant-tourism-management/asset-management-hospitality-certificate/ |

##### Sport and Entertainment Management
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Sport and Entertainment Management | M.S. | https://academicbulletins.sc.edu/graduate/hospitality-retail-sport-management/sport-entertainment-management/sport-entertainment-management-ms/ |
| 2 | Sport and Entertainment Management | Ph.D. | https://academicbulletins.sc.edu/graduate/hospitality-retail-sport-management/sport-entertainment-management/sport-entertainment-management-phd/ |

---

#### College of Information and Communications

##### Information and Communications
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Data and Communication | M.S. | https://academicbulletins.sc.edu/graduate/information-communications/information-and-communications/data-communication-ms/ |
| 2 | Data and Communication | Certificate | https://academicbulletins.sc.edu/graduate/information-communications/information-and-communications/data-communications-certificate/ |
| 3 | Library and Information Science | M.L.I.S. | https://academicbulletins.sc.edu/graduate/information-communications/information-and-communications/library-information-science-mlis/ |

##### Journalism Mass Communications
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mass Communications | M.M.C. | https://academicbulletins.sc.edu/graduate/information-communications/journalism-mass-communications/mass-communications-mmc/ |

---

#### School of Medicine

##### Biomedical Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Sciences | M.S. | https://academicbulletins.sc.edu/graduate/medicine/biomedical-sciences-ms/ |
| 2 | Biomedical Sciences | Ph.D. | https://academicbulletins.sc.edu/graduate/medicine/biomedical-sciences-phd/ |
| 3 | Medicine | M.D. | https://academicbulletins.sc.edu/medicine/ |

##### Counseling and Rehabilitation
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Counseling and Rehabilitation | M.A. | https://academicbulletins.sc.edu/graduate/medicine/counseling-rehabilitation-ma/ |
| 2 | Rehabilitation Counseling | M.R. | https://academicbulletins.sc.edu/graduate/medicine/rehabilitation-counseling-mr/ |

---

#### School of Music

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | M.M. | https://academicbulletins.sc.edu/graduate/music/music-mm/ |
| 2 | Music Education | M.M.Ed. | https://academicbulletins.sc.edu/graduate/music/music-education-mmed/ |
| 3 | Music | M.A. | https://academicbulletins.sc.edu/graduate/music/music-ma/ |

---

#### College of Nursing

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Adult Gerontology-Acute Care Nurse Practitioner | M.S.N. | https://academicbulletins.sc.edu/graduate/nursing/adult-gerontology-acute-care-nurse-practitioner-msn/ |
| 2 | Adult Gerontology-Acute Care Nurse Practitioner | D.N.P. | https://academicbulletins.sc.edu/graduate/nursing/adult-gerontology-acute-care-nurse-practitioner-dnp/ |
| 3 | Adult Gerontology-Acute Care Nurse Practitioner | Certificate | https://academicbulletins.sc.edu/graduate/nursing/adult-gerontology-acute-care-nurse-practitioner-certificate/ |
| 4 | Clinical Expert | D.N.P. | https://academicbulletins.sc.edu/graduate/nursing/clinical-expert-dnp/ |
| 5 | Family Nurse Practitioner | M.S.N. | https://academicbulletins.sc.edu/graduate/nursing/family-nurse-practitioner-msn/ |
| 6 | Family Nurse Practitioner | D.N.P. | https://academicbulletins.sc.edu/graduate/nursing/family-nurse-practitioner-dnp/ |
| 7 | Family Nurse Practitioner | Certificate | https://academicbulletins.sc.edu/graduate/nursing/family-nurse-practitioner-certificate/ |
| 8 | Nurse Educator | M.S.N. | https://academicbulletins.sc.edu/graduate/nursing/nurse-educator-msn/ |
| 9 | Nurse Educator | Certificate | https://academicbulletins.sc.edu/graduate/nursing/nurse-educator-certificate/ |
| 10 | Nursing Practice | D.N.P. | https://academicbulletins.sc.edu/graduate/nursing/nursing-practice-dnp/ |
| 11 | Nursing Science | Ph.D. | https://academicbulletins.sc.edu/graduate/nursing/nursing-science-phd/ |
| 12 | Psychiatric Mental Health Nurse Practitioner | M.S.N. | https://academicbulletins.sc.edu/graduate/nursing/psychiatric-mental-health-nurse-practitioner-msn/ |
| 13 | Psychiatric Mental Health Nurse Practitioner | Certificate | https://academicbulletins.sc.edu/graduate/nursing/psychiatric-mental-health-nurse-practitioner-certificate/ |

---

#### College of Pharmacy

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmaceutical Sciences | M.S. | https://academicbulletins.sc.edu/graduate/pharmacy/pharmaceutical-sciences-ms/ |
| 2 | Pharmaceutical Sciences | Ph.D. | https://academicbulletins.sc.edu/graduate/pharmacy/pharmaceutical-sciences-phd/ |

---

#### Arnold School of Public Health

##### Communication Sciences and Disorders
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication Sciences and Disorders | Ph.D. | https://academicbulletins.sc.edu/graduate/public-health/communication-sciences-disorders/communication-sciences-disorders-phd/ |

##### Environmental Health Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Environmental Health Sciences | M.P.H. | https://academicbulletins.sc.edu/graduate/public-health/environmental-health-sciences/environmental-health-sciences-mph/ |
| 2 | Environmental Health Sciences | M.S. | https://academicbulletins.sc.edu/graduate/public-health/environmental-health-sciences/environmental-health-sciences-ms/ |
| 3 | Environmental Health Sciences | Ph.D. | https://academicbulletins.sc.edu/graduate/public-health/environmental-health-sciences/environmental-health-sciences-phd/ |
| 4 | Disasters and Climate-Ready Public Health | Certificate | https://academicbulletins.sc.edu/graduate/public-health/environmental-health-sciences/disasters-climate-ready-public-health-certificate/ |
| 5 | Environmental Nanoscience and Risk | Certificate | https://academicbulletins.sc.edu/graduate/public-health/environmental-health-sciences/environmental-health-sciences-environmental-nanoscience-risk-certificate/ |

##### Epidemiology and Biostatistics
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics | M.S. | https://academicbulletins.sc.edu/graduate/public-health/epidemiology-biostatistics/biostatistics-msph/ |
| 2 | Biostatistics | Ph.D. | https://academicbulletins.sc.edu/graduate/public-health/epidemiology-biostatistics/biostatistics-phd/ |
| 3 | Biostatistics | Certificate | https://academicbulletins.sc.edu/graduate/public-health/epidemiology-biostatistics/biostatistics-certificate/ |
| 4 | Epidemiology | M.P.H. | https://academicbulletins.sc.edu/graduate/public-health/epidemiology-biostatistics/epidemiology-mph/ |
| 5 | Epidemiology | M.S. | https://academicbulletins.sc.edu/graduate/public-health/epidemiology-biostatistics/epidemiology-msph/ |
| 6 | Epidemiology | Ph.D. | https://academicbulletins.sc.edu/graduate/public-health/epidemiology-biostatistics/epidemiology-phd/ |

##### Exercise Science
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Athletic Training | M.S. | https://academicbulletins.sc.edu/graduate/public-health/exercise-science/athletic-training-ms/ |
| 2 | Behavioral Health in Athletic Training | Certificate | https://academicbulletins.sc.edu/graduate/public-health/exercise-science/behavioral-health-athletic-training-certificate/ |
| 3 | Critical Incident Management & Primary Care in Athletic Training | Certificate | https://academicbulletins.sc.edu/graduate/public-health/exercise-science/critical-incident-management-primary-care-athletic-training-certificate/ |

##### Health Promotion Education and Behavior
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Health | M.P.H. | https://academicbulletins.sc.edu/graduate/public-health/health-promotion-education-behavior/public-health-mph/ |
| 2 | Health Promotion, Education, and Behavior | Ph.D. | https://academicbulletins.sc.edu/graduate/public-health/health-promotion-education-behavior/health-promotion-education-behavior-phd/ |
| 3 | Aging | Certificate | https://academicbulletins.sc.edu/graduate/public-health/health-promotion-education-behavior/aging-certificate/ |

---

#### College of Social Work

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | M.S.W. | https://academicbulletins.sc.edu/graduate/social-work/social-work-msw/ |
| 2 | Drug and Addiction Studies | Certificate | https://academicbulletins.sc.edu/graduate/social-work/drug-addiction-studies-certificate/ |

---

#### Dual Degree Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy / Law | M.A.C.C. / J.D. | https://academicbulletins.sc.edu/graduate/dual-degree-programs/accountancy-law-macc-jd/ |
| 2 | Business Administration with American University of Sharjah | Ph.D. | https://academicbulletins.sc.edu/graduate/dual-degree-programs/business-administration-phd-dual-degree-sharjah/ |
| 3 | Business Administration with Chonnam National University | Ph.D. | https://academicbulletins.sc.edu/graduate/dual-degree-programs/business-administration-phd-dual-degree-chonnam/ |
| 4 | Business Administration with Universidad Adolfo Ibanez | Ph.D. | https://academicbulletins.sc.edu/graduate/dual-degree-programs/business-administration-phd-dual-degree-universidad-adolfo-ibanez/ |
| 5 | Business Administration/ Management (with EMYLON) | Ph.D. | https://academicbulletins.sc.edu/graduate/dual-degree-programs/business-administration-management-phd/ |

---

#### Other Graduate Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Environmental Law and Sustainability | M.S.L. | https://academicbulletins.sc.edu/graduate/other-graduate-courses-programs/environmental-law-sustainability-msl/ |
| 2 | Environmental Law and Sustainability | Certificate | https://academicbulletins.sc.edu/graduate/other-graduate-courses-programs/environmental-law-sustainability-certificate/ |
| 3 | Nurse Anesthesia | D.N.A.P. | https://academicbulletins.sc.edu/graduate/other-graduate-courses-programs/nurse-anesthesia-dnap/ |
| 4 | Physical Therapy | D.P.T. | https://academicbulletins.sc.edu/graduate/other-graduate-courses-programs/physical-therapy-dpt/ |

---

### 2.2 At least one program's full deep-dive (worked example)

**Program: International MBA (I.M.B.A.) — Darla Moore School of Business**

- **Department**: International Business
- **School**: Darla Moore School of Business
- **Degree**: I.M.B.A. (International Master of Business Administration)
- **URL**: https://academicbulletins.sc.edu/graduate/business/international-mba-imba/
- **Application portal**: https://apply.sc.edu/
- **Application fee**: $70
- **Note**: The Moore School's international MBA program is consistently ranked #1 in the nation by U.S. News & World Report. The program includes a mandatory international internship and study abroad component.

### 2.3 Graduate admissions model

USC Graduate School admissions is **decentralized** — each college/school manages its own admissions process, though all applications go through the central Graduate School portal. The Graduate School serves as the administrative hub for 250+ programs across 13 colleges. Professional schools (Law, Medicine, Pharmacy) have separate application processes:
- **Law**: LSAC (Law School Admission Council)
- **Medicine**: AMCAS (American Medical College Application Service)
- **Pharmacy**: PharmCAS

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://sc.edu/admissions-at-sc/undergraduate-admissions/ | E-U-001 |
| Application portal | USC Application (https://apply.sc.edu/register/freshman) OR Common App | E-U-002 |
| EA application deadline | October 15 | E-U-001 |
| EA credentials deadline | November 1 | E-U-001 |
| Honors College application deadline | November 15 | E-U-001 |
| Honors College credentials deadline | December 1 | E-U-001 |
| RD application deadline | December 1 | E-U-001 |
| RD credentials deadline | January 15 | E-U-001 |
| Application fee | $70 (nonrefundable) | E-U-003 |
| Fee waivers accepted | ACT, College Board, NACAC, SCOIR, Common App | E-U-003 |
| SAT code | 5818 | E-U-004 |
| ACT code | 3880 | E-U-004 |
| Test-optional policy | Yes, through spring/summer/fall 2027 | E-U-004 |
| Superscore | Yes (SAT and ACT English/Math/Reading) | E-U-004 |
| Recommendation requirements | Not required | E-U-001 |
| Interview policy | Not offered | E-U-001 |
| Application opens | August 1 | E-U-001 |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT | 77 | — | E-U-005 |
| TOEFL Paper-Based | 550 | — | E-U-005 |
| IELTS | 6.5 | — | E-U-005 |
| PTE | 53 | — | E-U-005 |
| Duolingo | 115 | — | E-U-005 |
| SAT EBRW | 560 | — | E-U-005 |
| ACT English | 22 | — | E-U-005 |

**Exempt countries**: American Samoa, Anguilla, Antigua, Australia, Bahamas, Barbados, Belize, Bermuda, British Virgin Islands, Canada (Quebec students must take TOEFL/IELTS/PTE), Dominica, Gambia, Ghana, Gibraltar, Grenada, Grand Cayman, Guam, Guyana, Ireland, Jamaica, Kenya, Lesotho, Liberia, Montserrat, New Zealand, Nigeria, Sierra Leone, St. Kitts and Nevis, St. Lucia, St. Vincent and the Grenadines, Swaziland (Eswatini), Tanzania, Trinidad/Tobago, Turks and Caicos Islands, Uganda, United Kingdom, US Virgin Islands, Zambia, Zimbabwe.

**Conditional admission**: Available through English Programs for Internationals (EPI) and the International Accelerator Program.

### 3.3 Graduate — global rules

- **Application platform**: Centralized Graduate School portal (https://graduate.sc.edu/) for most programs; professional schools use separate platforms
- **Application fee**: $70 (standard)
- **GRE/GMAT policy**: Per-program (each department decides)
- **Language-test policy**: TOEFL or IELTS required for non-native English speakers
- **ETS institutional code**: 5818 (USC)
- **CGS April-15 signatory**: Yes

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

#### South Carolina Resident

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $12,288 | Annual tuition for in-state students |
| Technology Fee | $400 | Required technology fee |
| Weighted Average Program Fee | $1,580 | Varies by program |
| Housing | $11,432 | On-campus housing estimate |
| Food | $5,902 | Meal plan estimate |
| **Total (Direct Costs)** | **$31,602** | |

#### Nonresident

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $38,098 | Annual tuition for out-of-state students |
| Technology Fee | $400 | Required technology fee |
| Weighted Average Program Fee | $1,580 | Varies by program |
| Housing | $11,432 | On-campus housing estimate |
| Food | $5,902 | Meal plan estimate |
| **Total (Direct Costs)** | **$57,412** | |

**Note**: These are direct costs billed by the university. Indirect costs (books, transportation, personal expenses) should also be considered.

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all applicants** (domestic and international)
- 98% of freshmen receive financial aid
- Merit scholarships available for both SC residents and nonresidents
- **Gamecock Guarantee**: Need-based program for qualifying SC residents
- FAFSA required for federal/state aid
- CSS Profile not required
- Application fee waivers available for eligible students

### 4.3 Graduate cost & funding framework

- **Assistantships**: Available in many departments; include tuition reduction and stipend
- **Fellowships and Awards**: Available through the Graduate School and individual departments
- **Financial Aid**: Federal loans, grants, and scholarships available
- **Professional school costs**: Vary by program (Law, Medicine, Pharmacy have separate fee structures)

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines
  value: "EA: Oct 15/Nov 1, Honors: Nov 15/Dec 1, RD: Dec 1/Jan 15"
  source_url: https://sc.edu/admissions-at-sc/undergraduate-admissions/index.php
  source_snippet: "Early Action Deadline: Apply by Oct. 15 to receive an admissions decision in mid-December. Credentials due by Nov. 1. Honors College Application Deadline: Apply by Nov. 15 to be considered for Top Scholars awards and the South Carolina Honors College. Credentials due by Dec. 1. Regular Decision Application Deadline: Apply by Dec. 1 to receive an admissions decision by mid-March. Credentials due by Jan. 15."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.application.platform
  value: "USC Application or Common App"
  source_url: https://sc.edu/admissions-at-sc/applications/index.php
  source_snippet: "Complete the USC Application or the Common App if you're entering college for the first time or if college credits you hold were earned before high school graduation."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application.fee
  value: "$70 nonrefundable"
  source_url: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/index.php
  source_snippet: "Regardless of which application you select, you must pay the nonrefundable $70 application fee or use an ACT, College Board, NACAC, SCOIR or Common App application fee waiver, if eligible."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.tests.test_optional
  value: "Test-optional through spring, summer or fall 2027 terms"
  source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/test_optional/index.php
  source_snippet: "Students seeking freshman admission to the University of South Carolina's Columbia campus will not be required to submit SAT or ACT scores for the spring, summer or fall 2027 terms. The test-optional policy applies to general university admission, the South Carolina Honors College and merit scholarships awarded by the Office of Undergraduate Admissions."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.tests.english_proficiency
  value: "TOEFL 77, IELTS 6.5, PTE 53, Duolingo 115, SAT EBRW 560, ACT English 22"
  source_url: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_international_students/index.php
  source_snippet: "English proficiency score: TOEFL Internet-Based 77, TOEFL Paper-Based 550, IELTS 6.5, PTE 53, Duolingo 115, SAT 560 (Evidence-Based Reading Writing Subscore), ACT 22 (English Subscore)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.tuition_in_state
  value: "$12,288"
  source_url: https://sc.edu/admissions-at-sc/tuition-aid/index.php
  source_snippet: "2026-2027 Estimated Cost: S.C. Resident Undergraduate Students: Tuition $12,288"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.tuition_oos
  value: "$38,098"
  source_url: https://sc.edu/admissions-at-sc/tuition-aid/index.php
  source_snippet: "2026-2027 Estimated Cost: Nonresident Undergraduate Students: Tuition $38,098"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.costs.total_in_state
  value: "$31,602"
  source_url: https://sc.edu/admissions-at-sc/tuition-aid/index.php
  source_snippet: "Total $31,602"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.costs.total_oos
  value: "$57,412"
  source_url: https://sc.edu/admissions-at-sc/tuition-aid/index.php
  source_snippet: "Total $57,412"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.programs.total
  value: "250+ graduate and certificate programs"
  source_url: https://sc.edu/admissions-at-sc/graduate-school-admissions/index.php
  source_snippet: "Expand on your undergraduate education through one of the more than 250 graduate and certificate programs at the University of South Carolina."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.fee
  value: "$70"
  source_url: https://sc.edu/admissions-at-sc/graduate-school-admissions/index.php
  source_snippet: "Application fee: $70"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.admissions.model
  value: "Decentralized; each college manages own admissions"
  source_url: https://www.sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/index.php
  source_snippet: "Find the program that interests you and learn how to apply."
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
USCarolina-knowledge-base-v2/
├── 00-institution-overview.md
│   ├── chunk: counts-and-hierarchy
│   ├── chunk: degree-inventory
│   └── chunk: distribution-matrix
├── 01-undergraduate-education.md
│   ├── chunk: arts-sciences-majors
│   ├── chunk: business-majors
│   ├── chunk: education-majors
│   ├── chunk: engineering-computing-majors
│   ├── chunk: hospitality-retail-sport-majors
│   ├── chunk: info-communications-majors
│   ├── chunk: medicine-majors
│   ├── chunk: music-majors
│   ├── chunk: nursing-majors
│   ├── chunk: pharmacy-majors
│   ├── chunk: public-health-majors
│   ├── chunk: social-work-majors
│   ├── chunk: minors-list
│   └── chunk: general-requirements
├── 02-graduate-education.md
│   ├── chunk: arts-sciences-grad
│   ├── chunk: business-grad
│   ├── chunk: education-grad
│   ├── chunk: engineering-computing-grad
│   ├── chunk: hospitality-retail-sport-grad
│   ├── chunk: info-communications-grad
│   ├── chunk: medicine-grad
│   ├── chunk: music-grad
│   ├── chunk: nursing-grad
│   ├── chunk: pharmacy-grad
│   ├── chunk: public-health-grad
│   ├── chunk: social-work-grad
│   └── chunk: dual-degree-programs
├── 03-application-requirements.md
│   ├── chunk: ug-deadlines
│   ├── chunk: ug-test-policy
│   ├── chunk: ug-english-proficiency
│   └── chunk: grad-admissions
├── 04-costs-financial-aid.md
│   ├── chunk: ug-cost-in-state
│   ├── chunk: ug-cost-oos
│   ├── chunk: financial-aid-policy
│   └── chunk: grad-funding
├── 05-evidence-chain.md
└── 06-comparison-framework.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "USCarolina-knowledge-base-v2"
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

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Individual program pages |
| P0 | Graduate application deadlines by program | Individual program pages |
| P1 | Detailed financial aid policy (need-aware specifics) | https://www.sc.edu/about/offices_and_divisions/financial_aid/ |
| P1 | Scholarship amounts and criteria | https://sc.edu/admissions-at-sc/tuition-aid/ |
| P1 | Transfer admission requirements | https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/ |
| P2 | Graduate stipend rates by department | Individual department pages |
| P2 | Housing options and costs breakdown | https://www.sc.edu/about/offices_and_divisions/housing/ |
| P2 | International student services | https://www.sc.edu/about/offices_and_divisions/international-student-services/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | USC (South Carolina) | 备注 |
|------|---------------------|------|
| Total UG cost/yr (in-state) | $31,602 | 2026-27 |
| Total UG cost/yr (OOS) | $57,412 | 2026-27 |
| Tuition/yr (in-state) | $12,288 | 2026-27 |
| Tuition/yr (OOS) | $38,098 | 2026-27 |
| Need-blind (domestic)? | Need-aware | For all applicants |
| Need-blind (intl)? | No | Need-aware for international |
| EA deadline | Oct 15 (app) / Nov 1 (creds) | |
| Honors deadline | Nov 15 (app) / Dec 1 (creds) | |
| RD deadline | Dec 1 (app) / Jan 15 (creds) | |
| SAT/ACT required? | Test-optional through 2027 | |
| TOEFL min | 77 | |
| IELTS min | 6.5 | |
| Duolingo min | 115 | |
| Application fee | $70 | |
| Total program count (Rule 1) | 466 | 99 UG majors + 108 minors + 6 UG certs + 202 grad + 51 grad certs |
| School/department count (Rule 2) | 13 | 13 colleges/schools |
| Graduate programs | 253 | Extracted from bulletin |
| Strongest program area | International Business (#1 ranked) | Moore School of Business |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: sc.edu, academicbulletins.sc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
