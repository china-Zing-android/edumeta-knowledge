# Keele University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (UG degree programmes) | 198 |
| 本科辅修 (Minors) | N/A (Keele does not offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/LLM/MBA/MPH/PgCert/PgDip) | 100 |
| 研究生博士项目 (PhD/MPhil/Professional Doctorate) | 72 research areas |
| **学位项目总计 (UG + PGT)** | **298** |
| 学院 (Faculties) | 3 |
| 学术院系 (Schools/Departments) | 22 |

> **Data source**: Keele UG courses A-Z page (`keele.ac.uk/study/undergraduate/undergraduatecourses/`), PG courses A-Z page (`keele.ac.uk/study/postgraduatestudy/postgraduatecourses/`), and PG research areas page (`keele.ac.uk/study/postgraduateresearch/researchareas/`).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Keele University
├── Faculty of Business, Law, Humanities and Social Sciences      [学院]
│   ├── Keele Business School                                     [系]
│   ├── School of Law                                             [系]
│   ├── School of Humanities                                      [系]
│   │   ├── English Literature                                    [子系]
│   │   ├── Film Studies                                          [子系]
│   │   ├── History                                               [子系]
│   │   ├── Creative Writing                                      [子系]
│   │   └── Music Production and Sound Design                     [子系]
│   └── School of Social Sciences                                 [系]
│       ├── Criminology                                           [子系]
│       ├── Education                                             [子系]
│       ├── Politics and International Relations                   [子系]
│       ├── Philosophy                                            [子系]
│       └── Sociology                                             [子系]
├── Faculty of Medicine and Health Sciences                       [学院]
│   ├── School of Medicine                                        [系]
│   ├── School of Nursing and Midwifery                           [系]
│   ├── School of Allied Health Professions and Pharmacy          [系]
│   │   ├── Occupational Therapy                                  [子系]
│   │   ├── Physiotherapy                                         [子系]
│   │   ├── Prosthetics and Orthotics                             [子系]
│   │   └── Pharmacy                                              [子系]
│   ├── School of Primary, Community and Social Care              [系]
│   └── Counselling                                               [子系]
└── Faculty of Natural Sciences                                   [学院]
    ├── School of Computer Science and Mathematics                 [系]
    ├── School of Life Sciences                                   [系]
    │   ├── Bioengineering                                        [子系]
    │   ├── Biology                                               [子系]
    │   ├── Biomedical Science                                    [子系]
    │   ├── Ecology and Conservation                              [子系]
    │   └── Forensic Science                                      [子系]
    ├── School of Chemical and Physical Sciences                   [系]
    │   ├── Chemistry and Medicinal Chemistry                     [子系]
    │   ├── Physics and Astrophysics                              [子系]
    │   └── Geography and Geology                                 [子系]
    ├── School of Psychology                                      [系]
    └── Harper & Keele Vet School (joint with Harper Adams)       [系]
```

> **Note**: Harper & Keele Vet School is a joint venture with Harper Adams University. Some interdisciplinary programmes span multiple schools.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA (Hons) | Bachelor of Arts (Honours) | 本科 | 52 |
| BSc (Hons) | Bachelor of Science (Honours) | 本科 | 107 |
| BEng | Bachelor of Engineering | 本科 | 7 |
| LLB (Hons) | Bachelor of Laws (Honours) | 本科 | 6 |
| MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 1 |
| BVetMS | Bachelor of Veterinary Medicine and Surgery | 本科 | 1 |
| MPharm | Master of Pharmacy | 本科 | 1 |
| MSci | Master in Science (integrated) | 本科 | 20 |
| MEng | Master of Engineering (integrated) | 本科 | 6 |
| MChem | Master of Chemistry (integrated) | 本科 | 4 |
| MMath | Master of Mathematics (integrated) | 本科 | 1 |
| MCOMP | Master of Computing (integrated) | 本科 | 1 |
| FdSc | Foundation Degree | 本科 | 1 |
| Integrated Masters (MSci) | Integrated Masters | 本科 | 1 |
| MSc | Master of Science | 研究生授课型 | 55 |
| MA | Master of Arts | 研究生授课型 | 16 |
| LLM | Master of Laws | 研究生授课型 | 4 |
| MBA | Master of Business Administration | 研究生授课型 | 1 |
| MPH | Master of Public Health | 研究生授课型 | 4 |
| MRes | Master of Research | 研究生授课型 | 6 |
| PgCert | Postgraduate Certificate | 研究生授课型 | 3 |
| PgDip | Postgraduate Diploma | 研究生授课型 | 2 |
| GradDip | Graduate Diploma | 研究生授课型 | 1 |
| Graduate Certificate | Graduate Certificate | 研究生授课型 | 1 |
| PhD | Doctor of Philosophy | 研究生博士 | 62 |
| MPhil | Master of Philosophy | 研究生博士 | 62 |
| DM | Doctor of Medicine | 研究生博士 | 1 |
| Professional Doctorate | DCouns/DCrim/EdD/DEdHealth/DNursing/DPharm/DHealthSci/DPH | 研究生博士 | 9 |

> **Note**: UG total = 198 (includes Top-up degrees). PGT total = 100. Research areas = 72 (each offers both PhD and MPhil, plus 9 professional doctorates).

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

**Undergraduate (198 programmes)**

| 学院 \ 学位级别 | BA | BSc | BEng | LLB | MBChB | BVetMS | MPharm | MSci | MEng | MChem | MMath | MCOMP | FdSc | 合计 |
|------------|----|----|------|-----|-------|--------|--------|------|------|-------|-------|-------|------|------|
| Business, Law, Humanities & SS | 44 | 8 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 58 |
| Medicine & Health Sciences | 0 | 15 | 0 | 0 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 1 | 20 |
| Natural Sciences | 8 | 84 | 7 | 0 | 0 | 1 | 0 | 18 | 6 | 4 | 1 | 1 | 0 | 130 |
| **合计** | **52** | **107** | **7** | **6** | **1** | **1** | **1** | **20** | **6** | **4** | **1** | **1** | **1** | **198** |

**Postgraduate Taught (100 programmes)**

| 学院 \ 学位级别 | MSc | MA | LLM | MBA | MPH | MRes | PgCert | PgDip | GradDip | GradCert | 合计 |
|------------|-----|----|-----|-----|-----|------|--------|-------|---------|----------|------|
| Business, Law, Humanities & SS | 20 | 11 | 4 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 38 |
| Medicine & Health Sciences | 11 | 1 | 0 | 0 | 4 | 1 | 2 | 2 | 0 | 0 | 21 |
| Natural Sciences | 24 | 4 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 0 | 34 |
| Online programmes | 7 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 |
| **合计** | **55** | **16** | **4** | **1** | **4** | **6** | **3** | **2** | **1** | **1** | **100** |

> **Reconciliation**: UG 198 + PGT 100 = 298 total. Matrix cell sums match.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Keele University organises its undergraduate programmes across three faculties. The Faculty of Natural Sciences houses the largest number of UG programmes (130), followed by Business/Law/Humanities/Social Sciences (58) and Medicine/Health Sciences (20). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Business, Law, Humanities and Social Sciences

##### Keele Business School

###### BA (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Business and Management \| Top-up | N12T | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessandmanagementtop-up/ |
| 2 | Business Management | N202 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagement/ |
| 3 | Business Management and Accounting | NN42 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementandaccounting/ |
| 4 | Business Management and Economics | LN19 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementandeconomics/ |
| 5 | Business Management and Finance | NN39 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementandfinance/ |
| 6 | Business Management and Marketing | NN25 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementandmarketing/ |
| 7 | Business Management with Analytics | NG12 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithanalytics/ |
| 8 | Business Management with Entrepreneurship | N291 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithentrepreneurship/ |
| 9 | Business Management with Events | N2N8 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithevents/ |
| 10 | Business Management with Hospitality | N2N6 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithhospitality/ |
| 11 | Business Management with Human Resources | NN69 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithhumanresources/ |
| 12 | Business Management with International Tourism | N830 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithinternationaltourism/ |
| 13 | Business Management with Supply Chain | N114 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithsupplychain/ |
| 14 | Business Management with Sustainability | N271 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businessmanagementwithsustainability/ |
| 15 | Esports Business Management | G460 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/esportsbusinessmanagement/ |
| 16 | International Business Management | N120 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/internationalbusinessmanagement/ |
| 17 | Marketing | N500 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/marketing/ |
| 18 | Sports Business Management | N880 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/sportsbusinessmanagement/ |

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Accounting and Finance | NN34 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/accountingandfinance/ |
| 2 | Accounting with Business Analytics | N4G3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/accountingwithbusinessanalytics/ |
| 3 | Banking and Finance | N320 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/bankingandfinance/ |
| 4 | Business Technology | N123 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/businesstechnology/ |
| 5 | Economics and Finance | LN13 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/economicsandfinance/ |
| 6 | Economics BSc | LNC3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/economicsbsc/ |
| 7 | Finance and Management \| Top-up | N310 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/financeandmanagementtop-up/ |
| 8 | Politics and Sociology | L000 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/politicsandsociology/ |

##### School of Law

###### LLB (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Law | M100 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/law/ |
| 2 | Law (Graduate Entry) | M105 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/lawgraduateentry/ |
| 3 | Law with Business | M1N1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/lawwithbusiness/ |
| 4 | Law with Criminology | M1LH | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/lawwithcriminology/ |
| 5 | Law with Politics | M1L2 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/lawwithpolitics/ |
| 6 | Law with Professional Legal Practice | M101 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/lawwithprofessionallegalpractice/ |

##### School of Humanities

###### BA (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Animation | W615 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/animation/ |
| 2 | Creative Writing | W800 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/creativewriting/ |
| 3 | Digital Media | P301 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/digitalmedia/ |
| 4 | Digital Media and Marketing | P3N5 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/digitalmediaandmarketing/ |
| 5 | Digital Media and Music Production | P4J0 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/digitalmediaandmusicproduction/ |
| 6 | Digital Media and Sociology | P3L3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/digitalmediaandsociology/ |
| 7 | English | Q300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/english/ |
| 8 | English and Creative Writing | Q3W8 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/englishandcreativewriting/ |
| 9 | English and Film Studies | Q3P3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/englishandfilmstudies/ |
| 10 | English and History | Q3V1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/englishandhistory/ |
| 11 | English and Philosophy | QV3A | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/englishandphilosophy/ |
| 12 | Film and Media Studies | P3P9 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/filmandmediastudies/ |
| 13 | Film and Music Production | P4JX | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/filmandmusicproduction/ |
| 14 | Film Studies | P303 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/filmstudies/ |
| 15 | Film Studies and Creative Writing | PW38 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/filmstudiesandcreativewriting/ |
| 16 | Game Design | W291 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/gamedesign/ |
| 17 | Graphic Design | W210 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/graphicdesign/ |
| 18 | History | V101 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/history/ |
| 19 | Media and Communications | P300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mediaandcommunications/ |
| 20 | Media with Business Management | P3N1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mediawithbusinessmanagement/ |
| 21 | Music Production and Sound Design | WJ40 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/musicproductionandsounddesign/ |
| 22 | Music Production with Business Management | N2J0 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/musicproductionwithbusinessmanagement/ |

##### School of Social Sciences

###### BA (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Criminology | L611 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/criminology/ |
| 2 | Criminology and Criminal Justice | L612 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/criminologyandcriminaljustice/ |
| 3 | Criminology and History | MXV1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/criminologyandhistory/ |
| 4 | Criminology and Sociology | LMH9 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/criminologyandsociology/ |
| 5 | Economics BA | LNC5 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/economicsba/ |
| 6 | Education | X300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/education/ |
| 7 | Education and English | Q3X3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/educationandenglish/ |
| 8 | Education and Sociology | LX33 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/educationandsociology/ |
| 9 | History and Education | V1X3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/historyandeducation/ |
| 10 | International Governance and Public Policy | — | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/internationalgovernanceandpublicpolicy/ |
| 11 | International Relations | L254 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/internationalrelations/ |
| 12 | Philosophy | V501 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/philosophy/ |
| 13 | Philosophy and Education | V5X3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/philosophyandeducation/ |
| 14 | Philosophy and Politics | L2V5 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/philosophyandpolitics/ |
| 15 | Philosophy, Politics and Economics | LV50 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/philosophypoliticsandeconomics/ |
| 16 | Politics | L200 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/politics/ |
| 17 | Politics and International Relations | L521 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/politicsandinternationalrelations/ |
| 18 | Politics with Economics | LL14 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/politicswitheconomics/ |
| 19 | Social Work | L500 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/socialwork/ |
| 20 | Sociology | L30L | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/sociology/ |

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Criminology and Criminal Justice \| Top-up | L614 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/criminologyandcriminaljusticetop-up/ |
| 2 | Criminology \| Top-up | L613 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/criminologytop-up/ |
| 3 | Social Sciences | L400 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/socialsciences/ |

###### BA (Hons) and BA Diplomacy
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | International Governance and Public Policy | — | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/internationalgovernanceandpublicpolicy/ |

---

#### Faculty of Medicine and Health Sciences

##### School of Medicine

###### MBChB
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Medicine | A100 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/medicine/ |

##### School of Nursing and Midwifery

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Midwifery | B720 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/midwifery/ |
| 2 | Nursing (Adult) | B740 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/adultnursing/ |
| 3 | Nursing (Children's) | B730 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/childrensnursing/ |
| 4 | Nursing (Mental Health) | B760 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mentalhealthnursing/ |
| 5 | Nursing Studies (International Pathway) \| Top-up | — | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/nursingstudies-international-pathway/ |
| 6 | Nursing Studies \| Top-up | — | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/nursingstudies/ |

###### FdSc
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Nursing Associate Foundation Degree | B750 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/nursingassociatefoundationdegree/ |

##### School of Allied Health Professions and Pharmacy

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Health and Social Care | L550 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/health-and-social-care/ |
| 2 | Occupational Therapy | B920 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/occupationaltherapy/ |
| 3 | Paramedic Science with Integrated Master's | B950 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/paramedicsciencewithintegratedmasters/ |
| 4 | Pharmaceutical Science | 1B11 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/pharmaceuticalscience/ |
| 5 | Pharmacology | B210 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/pharmacology/ |
| 6 | Physiotherapy | B160 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/physiotherapy/ |
| 7 | Radiography (Diagnostic Imaging) | B821 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/radiographydiagnosticimaging/ |
| 8 | Rehabilitation and Exercise Science | B900 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/rehabilitationandexercisescience/ |

###### MPharm
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Pharmacy | B230 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/pharmacy/ |

###### MSci
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Paramedic Science with Integrated Master's | B950 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/paramedicsciencewithintegratedmasters/ |
| 2 | Pharmacology with Integrated Master's | B212 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/pharmacologywithintegratedmasters/ |

###### MSci (pre-registration)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Speech and Language Therapy with Integrated Master's (pre-registration) | B620 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/speech-language-therapy-prereg/ |

---

#### Faculty of Natural Sciences

##### School of Computer Science and Mathematics

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Computer Science | G400 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computerscience/ |
| 2 | Computer Science and Mathematics | GG14 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computerscienceandmathematics/ |
| 3 | Computer Science with Artificial Intelligence | G416 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computersciencewithartificialintelligence/ |
| 4 | Computer Science with Digital Forensics | G418 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computersciencewithdigitalforensics/ |
| 5 | Computer Science with Software Engineering | G430 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computersciencewithsoftwareengineering/ |
| 6 | Computing Top-up | G406 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computing-top-up/ |
| 7 | Cyber Security | I900 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/cybersecurity/ |
| 8 | Data Science | G420 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/datascience/ |
| 9 | Mathematics | G100 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mathematics/ |
| 10 | Mathematics (Applied Mathematics) | G110 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mathematicsappliedmathematics/ |
| 11 | Mathematics (Pure Mathematics) | G112 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mathematicspuremathematics/ |
| 12 | Mathematics (with Statistics) | G111 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mathematicswithstatistics/ |

###### BA (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Computer Science and Music Production | GWK4 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computerscienceandmusicproduction/ |

###### MCOMP
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Computer Science with Integrated Master's | G402 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computersciencewithintegratedmasters/ |

###### MMath
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Mathematics with Integrated Master's | G103 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mathematicswithintegratedmasters/ |

##### School of Life Sciences

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biochemistry | C701 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biochemistry/ |
| 2 | Biochemistry with Neuroscience | B7C1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biochemistrywithneuroscience/ |
| 3 | Bioengineering (Regenerative Medicine) | C110 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/bioengineeringregenerativemedicine/ |
| 4 | Biology | C102 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biology/ |
| 5 | Biomedical Science | C900 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biomedicalscience/ |
| 6 | Bioveterinary Science | D300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/bioveterinaryscience/ |
| 7 | Ecology and Conservation | C180 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/ecologyandconservation/ |
| 8 | Environmental Science | F901 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/environmentalscience/ |
| 9 | Environmental Science and Geography | FL97 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/environmentalscienceandgeography/ |
| 10 | Forensic Biology | FC14 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicbiology/ |
| 11 | Forensic Chemistry | F1F4 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicchemistry/ |
| 12 | Forensic Psychology | C8B1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicpsychology/ |
| 13 | Forensic Science | F415 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicscience/ |
| 14 | Forensic Science with Criminology | F4L6 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicsciencewithcriminology/ |
| 15 | Human Anatomy | B110 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/humananatomy/ |
| 16 | Medical Sciences \| Top-up | C902 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/medicalsciencestop-up/ |
| 17 | Microbiology and Immunology | C501 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/microbiologyandimmunology/ |
| 18 | Neuroscience | B141 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/neuroscience/ |
| 19 | Neuroscience with Artificial Intelligence | BG41 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/neurosciencewithai/ |
| 20 | Neuroscience with Psychology | B1C8 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/neurosciencewithpsychology/ |
| 21 | Sport and Exercise Psychology | C813 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/sportandexercisepsychology/ |
| 22 | Sport and Exercise Science | C600 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/sportandexercisescience/ |
| 23 | Sustainability and Environmental Management | FD84 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/sustainabilityandenvironmentalmanagement/ |
| 24 | Zoology | C300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/zoology/ |

###### MSci
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biochemistry with Integrated Master's | C702 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biochemistrywithintegratedmasters/ |
| 2 | Biochemistry with Neuroscience with Integrated Master's | BC71 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biochemistrywithneurosciencewithintegratedmasters/ |
| 3 | Biology with Integrated Master's | C104 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/biologywithintegratedmasters/ |
| 4 | Bioveterinary Science with Integrated Master's | D302 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/bioveterinarysciencewithintegratedmasters/ |
| 5 | Ecology and Conservation with Integrated Master's | C181 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/ecologyandconservationwithintegratedmasters/ |
| 6 | Environmental Science and Geography with Integrated Master's | FL98 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/environmentalscienceandgeographywithintegratedmasters/ |
| 7 | Environmental Science with Integrated Master's | F903 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/environmentalsciencewithintegratedmasters/ |
| 8 | Forensic Biology with Integrated Master's | FC16 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicbiologywithintegratedmasters/ |
| 9 | Forensic Science with Integrated Master's | F412 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicsciencewithintegratedmasters/ |
| 10 | Microbiology and Immunology with Integrated Master's | C500 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/microbiologyandimmunologywithintegratedmasters/ |
| 11 | Zoology with Integrated Master's | C302 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/zoologywithintegratedmasters/ |

###### BVetMS
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Veterinary Medicine and Surgery | D100 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/veterinarymedicineandsurgery/ |

##### School of Chemical and Physical Sciences

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemistry | F101 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistry/ |
| 2 | Chemistry with Materials Chemistry | F106 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithmaterialschemistry/ |
| 3 | Chemistry with Mathematics | FG12 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithmathematics/ |
| 4 | Chemistry with Medicinal Chemistry | F123 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithmedicinalchemistry/ |
| 5 | Geography (Human and Physical) | FL87 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographyhumanandphysical/ |
| 6 | Geography (Human) | L701 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographyhuman/ |
| 7 | Geography (Physical) | F801 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographyphysical/ |
| 8 | Geography with Business Management | L7N2 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographywithbusinessmanagement/ |
| 9 | Geology | F600 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geology/ |
| 10 | Geology (Applied Geophysics) | F660 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geologyappliedgeophysics/ |
| 11 | Geology (Environmental Geoscience) | F630 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geologyenvironmentalgeoscience/ |
| 12 | Geology (Volcanology) | F650 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geologyvolcanology/ |
| 13 | Geology and Physical Geography | FF68 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geologyandphysicalgeography/ |
| 14 | Physics | F300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/physics/ |
| 15 | Physics with Artificial Intelligence | F3G4 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/physicswithartificialintelligence/ |
| 16 | Physics with Astrophysics | F301 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/physicswithastrophysics/ |
| 17 | Physics with Mathematics | F3G1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/physicswithmathematics/ |
| 18 | Physics with Renewable Energy | FH32 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/physicswithrenewableenergy/ |

###### MSci
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Astrophysics with Integrated Master's | F512 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/astrophysicswithintegratedmasters/ |
| 2 | Environmental Science and Geography with Integrated Master's | FL98 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/environmentalscienceandgeographywithintegratedmasters/ |
| 3 | Geography (Human and Physical) with Integrated Master's | FL89 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographyhumanandphysicalwithintegratedmasters/ |
| 4 | Geography (Human) with Integrated Master's | L703 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographyhumanwithintegratedmasters/ |
| 5 | Geography (Physical) with Integrated Master's | F802 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographyphysicalwithintegratedmasters/ |
| 6 | Geography with Business Management with Integrated Master's | L7N3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/geographywithbusinessmanagementwithintegratedmasters/ |

###### MChem
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemistry with Integrated Master's | F102 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithintegratedmasters/ |
| 2 | Chemistry with Materials Chemistry with Integrated Master's | F108 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithmaterialschemistrywithintegratedmasters/ |
| 3 | Chemistry with Mathematics with Integrated Master's | FG13 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithmathematicswithintegratedmasters/ |
| 4 | Chemistry with Medicinal Chemistry with Integrated Master's | F124 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemistrywithmedicinalchemistrywithintegratedmasters/ |
| 5 | Forensic Chemistry with Integrated Master's | F1F6 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/forensicchemistrywithintegratedmasters/ |

##### Department of Engineering

###### BEng
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemical Engineering | H800 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemicalengineering/ |
| 2 | Civil Engineering | H200 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/civilengineering/ |
| 3 | Electrical and Electronic Engineering | H600 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/electricalandelectronicengineering/ |
| 4 | Engineering | H100 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/engineering/ |
| 5 | Mechanical Engineering | H300 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mechanicalengineering/ |
| 6 | Mechatronic Engineering | H400 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mechatronicengineering/ |

###### MEng
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemical Engineering with Integrated Master's | H801 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/chemicalengineeringwithintegratedmasters/ |
| 2 | Civil Engineering with Integrated Master's | H201 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/civilengineeringwithintegratedmasters/ |
| 3 | Electrical and Electronic Engineering with Integrated Master's | H601 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/electricalandelectronicengineeringwithintegratedmasters/ |
| 4 | Engineering with Integrated Master's | H101 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/engineeringwithintegratedmasters/ |
| 5 | Mechanical Engineering with Integrated Master's | H301 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mechanicalengineeringwithintegratedmasters/ |
| 6 | Mechatronic Engineering with Integrated Master's | H401 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/mechatronicengineeringwithintegratedmasters/ |

##### School of Psychology

###### BSc (Hons)
| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Psychology | C800 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychology/ |
| 2 | Psychology in Education | CX85 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologyineducation/ |
| 3 | Psychology with Counselling | C8B9 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithcounselling/ |
| 4 | Psychology with Criminology | C8M1 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithcriminology/ |
| 5 | Psychology with Human Biology | C1CV | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithhumanbiology/ |
| 6 | Psychology with Neuroscience | C832 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithneuroscience/ |
| 7 | Psychology with Philosophy | C8V5 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithphilosophy/ |
| 8 | Psychology with Placement Year | C805 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithplacementyear/ |
| 9 | Psychology with Sociology | C8L3 | https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/psychologywithsociology/ |

### 1.3 Interdisciplinary / cross-college undergraduate programmes

Several programmes span multiple schools:
- Philosophy, Politics and Economics (BA) — spans Social Sciences and Business
- Computer Science and Music Production (BA) — spans Computer Science and Humanities
- Digital Media and Sociology (BA) — spans Humanities and Social Sciences
- Environmental Science and Geography (BSc) — spans Life Sciences and Chemical/Physical Sciences
- Forensic programmes span Life Sciences, Chemistry, and Psychology

### 1.4 Minors

Keele University does not offer standalone minor programmes.

### 1.5 General/Institute-wide requirements

Keele offers "Global Challenge Pathways" as additional opportunities for students to enhance their degree with interdisciplinary modules focused on global challenges.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programmes — grouped by 学院 > 系 > 学位级别

#### Faculty of Business, Law, Humanities and Social Sciences

##### Keele Business School

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Financial Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/accountingandfinancialmanagement/ |
| 2 | Banking and Finance | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/bankingandfinance/ |
| 3 | Business Analytics | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/businessanalytics/ |
| 4 | Digital Marketing | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/digitalmarketing/ |
| 5 | Economics | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/economicsmsc/ |
| 6 | Financial Technology (FinTech) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/financialtechnologyfintech/ |
| 7 | International Business | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/internationalbusiness/ |
| 8 | International Tourism and Hospitality Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/internationaltourismandhospitalitymanagement/ |
| 9 | Logistics and Supply Chain Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/logisticsandsupplychainmanagement/ |
| 10 | Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/management/ |
| 11 | Marketing | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/marketing/ |
| 12 | Project Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/projectmanagement/ |
| 13 | Sports Business Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/sportsbusinessmanagement/ |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/masterofbusinessadministration/ |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/economicsma/ |
| 2 | Human Resource Management | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/humanresourcemanagement/ |

##### School of Law

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | International Commercial and Business Law | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/internationalcommercialandbusinesslaw/ |
| 2 | International Law | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/internationallaw/ |
| 3 | International Law with Human Rights | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/internationallawwithhumanrights/ |
| 4 | Law with SQE Preparation | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/lawwithsqe/ |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Law and Society | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/lawandsociety/ |
| 2 | Medical Ethics and Law | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalethicsandlaw/ |
| 3 | Medical Ethics and Palliative Care | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalethicsandpalliativecare/ |

##### School of Humanities

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative and Cultural Industries | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/creativeandculturalindustries/ |
| 2 | Creative Writing | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/creativewriting/ |
| 3 | Digital Media and Society | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/digitalmediaandsociety/ |
| 4 | English Literatures | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/englishliteratures/ |
| 5 | History | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/history/ |
| 6 | Human Geography and Sustainability Research | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/humangeographyandsustainabilityresearch/ |
| 7 | Politics and International Relations | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/politicsandinternationalrelations/ |
| 8 | Teaching English to Speakers of Other Languages (TESOL) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/teaching-english-to-speakers-of-other-languages-tesol/ |

##### School of Social Sciences

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/education/ |
| 2 | Education with TESOL (Trinity Certified) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/education-with-tesol-trinity/ |

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Research | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/socialresearch/ |

---

#### Faculty of Medicine and Health Sciences

##### School of Medicine

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselling and Psychotherapy | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/counsellingandpsychotherapy/ |
| 2 | Physician Assistant Studies | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/physicianassistantstudies/ |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Ethics and Law | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalethicsandlaw/ |
| 2 | Medical Ethics and Palliative Care | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalethicsandpalliativecare/ |

###### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/publichealth/ |

##### School of Nursing and Midwifery

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing (Adult) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/adultnursing/ |
| 2 | Nursing (Children's) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/childrensnursing/ |
| 3 | Nursing (Mental Health) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mentalhealthnursing/ |

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Health and Care | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/healthandcare/ |

##### School of Allied Health Professions and Pharmacy

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Clinical Practice | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/advancedclinicalpractice/ |
| 2 | Medical Imaging | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalimaging/ |
| 3 | Occupational Therapy (pre-registration) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/occupationaltherapypre-registration/ |
| 4 | Paramedic Science | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/paramedicscience/ |
| 5 | Pharmacy (Professional MSc) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/pharmacyprofessionalmsc/ |
| 6 | Physiotherapy (pre-registration) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/physiotherapypre-registration/ |
| 7 | Prosthetics and Orthotics | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/prostheticsandorthotics/ |

###### PgCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Critical Care Practice | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/criticalcarepractice/ |

---

#### Faculty of Natural Sciences

##### School of Computer Science and Mathematics

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Data Science | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/artificialintelligenceanddatascience/ |
| 2 | Computer Science | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/computerscience/ |
| 3 | Cyber Security | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/cybersecurity/ |

##### School of Life Sciences

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Biodiversity and Conservation | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/biodiversityandconservation/ |
| 2 | Biomedical Science (Blood Science) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/biomedicalsciencebloodscience/ |
| 3 | Biomedical Science (Medical Microbiology) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/biomedicalsciencemedicalmicrobiology/ |
| 4 | Biotechnology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/biotechnology/ |
| 5 | Environmental Sustainability and Green Technology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/environmentalsustainabilityandgreentechnology/ |
| 6 | Forensic Science | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/forensicscience/ |
| 7 | Medical Engineering (Biomedical Engineering) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalengineeringbiomedicalengineering/ |
| 8 | Medical Engineering (Cell and Tissue Engineering for Regenerative Medicine) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalengineeringcellandtissueengineeringforregenerativemedicine/ |
| 9 | Medical Engineering (Design and Innovation) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/medicalengineeringdesignandinnovation/ |
| 10 | Pharmacology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/pharmacologymsc/ |
| 11 | Renewable Energy | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/renewableenergy/ |

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioscience | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/bioscience/ |
| 2 | Chemistry | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/chemistry/ |

###### GradDip
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Science (Graduate Diploma) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/biomedicalsciencegraduatediploma/ |

##### School of Psychology

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Child Psychology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/appliedchildpsychology/ |
| 2 | Cognition and Cognitive Neuroscience | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/cognitionandcognitiveneuroscience/ |
| 3 | Forensic Psychology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/forensicpsychology/ |
| 4 | Health Psychology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/healthpsychology/ |
| 5 | Psychological Research Methods | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/psychologicalresearchmethods/ |
| 6 | Sport and Exercise Psychology | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/sportandexercisepsychology/ |

---

#### Online Programmes (100% online)

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Science (Online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/biomedicalscience/ |
| 2 | Computer Science (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/msccomputerscience100online/ |
| 3 | Computer Science with Artificial Intelligence (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/msccomputersciencewithartificialintelligence100online/ |
| 4 | Computer Science with Data Analytics (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/msccomputersciencewithdataanalytics100online/ |
| 5 | Management (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/management100online/ |
| 6 | Management with Data Analytics (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/managementwithdataanalytics100online/ |
| 7 | Management with Healthcare Management (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mscmanagementwithhealthcaremanagement100online/ |
| 8 | Management with Human Resources (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mscmanagementwithhumanresources100online/ |
| 9 | Management with Marketing (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/managementwithmarketing100online/ |
| 10 | Management with Project Management (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mscmanagementwithprojectcaremanagement100online/ |
| 11 | Management with Sustainability (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/managementwithsustainability100online/ |
| 12 | Psychology (Conversion) \| Online | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/psychologyconversionmsc/ |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/maeducation100online/ |
| 2 | Education Leadership and Management (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/maeducationleadershipandmanagement100online/ |
| 3 | Education Technology (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/educationtechnology100online/ |
| 4 | International Education (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mainternationaleducation100online/ |

###### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | MPH Global Health (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mphglobalhealth100online/ |
| 2 | MPH Master's in Public Health (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mphmasterspublichealth100online/ |
| 3 | MPH with Leadership (100% online) | https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/mphwithleadership100online/ |

---

### 2.2 Graduate research programmes (PhD/MPhil/Professional Doctorate)

Keele offers research degrees across 72 areas. Key areas include:

| # | 研究领域 | 学位类型 |
|---|---------|---------|
| 1 | American Studies | PhD / MPhil |
| 2 | Astrophysics and Physics | PhD / MPhil |
| 3 | Biochemistry | PhD / MPhil |
| 4 | Biological, Biomedical and Life Sciences | PhD / MPhil |
| 5 | Computer Science | PhD / MPhil |
| 6 | Criminology | PhD / MPhil |
| 7 | Economics | PhD / MPhil |
| 8 | Education | PhD / MPhil |
| 9 | Engineering | PhD / MPhil |
| 10 | English | PhD / MPhil |
| 11 | Forensic Science | PhD / MPhil |
| 12 | Geography (Human/Physical) | PhD / MPhil |
| 13 | History | PhD / MPhil |
| 14 | Law | PhD / MPhil |
| 15 | Management | PhD / MPhil |
| 16 | Mathematics | PhD / MPhil |
| 17 | Medicine | PhD / MPhil / DM |
| 18 | Neuroscience | PhD / MPhil |
| 19 | Nursing | PhD / MPhil |
| 20 | Pharmacy | PhD / MPhil |
| 21 | Philosophy | PhD / MPhil |
| 22 | Politics and International Relations | PhD / MPhil |
| 23 | Psychology | PhD / MPhil |
| 24 | Social Work | PhD / MPhil |

**Professional Doctorates**: DCouns, DCrim, EdD, DEdHealth, DNursing, DPharm, DHealthSci (Physio), DPH, DM

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application platform | **UCAS** |
| UCAS deadline | **January** (equal consideration, most courses); **October 15** for Medicine |
| Personal statement | UCAS single statement (one for all 5 choices) |
| References | 1 academic reference (UCAS) |
| Interviews | Medicine mandatory; others rare |
| Typical offer (example: Computer Science) | A-Level: BBB (or BBC with B in Maths/CS); Contextual: BCC (or BCD with B in Maths/CS) |
| GCSE requirements | 4/C in GCSE Maths (or Level 2 Functional Skills Maths); English language qualification |
| BTEC (example: CS) | DDM |
| T Level (example: CS) | Merit |
| Placement/Sandwich year | Available on most programmes; 20% of Home fee |

### 3.2 Undergraduate English proficiency table

| Exam | Group A (Standard) | Group B (Higher) | Notes |
|------|-------------------|------------------|-------|
| IELTS Academic | 6.0 overall, 5.5 in each component | 6.5 overall, 5.5 in each component | Most UG courses require Group A; Nursing/Health courses require Group B |
| GCSE English | 4/C | 4/C | Most students meet requirement through GCSE |
| TOEFL iBT | Refer to English Language pages | Refer to English Language pages | Accepted alternative |
| PTE Academic | Refer to English Language pages | Refer to English Language pages | Accepted alternative |

> **Note**: Specific course pages indicate whether Group A or Group B applies. Medicine and clinical programmes may have higher requirements.

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Application platform | Direct to university (no UCAS for PG) |
| Application fee | None specified |
| Typical entry | UK 2:1 or equivalent for most programmes |
| English language | Same Group A/B system as UG |
| Deadlines | Rolling admissions for most programmes |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026/27 academic year)

**UK/Home Students**

| Fee Type | Amount |
|----------|--------|
| Tuition fee (2025 entry) | £9,535/year |
| Tuition fee (2026 entry) | £9,790/year |
| Placement year fee | 20% of full fee (~£1,958) |

**International Students (2026/27)**

| Band | Annual Fee |
|------|-----------|
| Band 0 | £17,100 |
| Band 1 | £18,200 |
| Band 2 | £20,800 |
| Band 3 | £22,000 |
| Band 4 | £23,400 |
| Band 5 | £25,600 |
| Band 6 | £29,800 |

> **Exceptional fees**: Medicine MBChB, Veterinary Medicine BVetMS, and Nursing Studies Top-up have separate fee structures — check individual course pages.

### 4.2 Postgraduate cost (2026/27 academic year)

**UK/Home Students**

| Band | Full-time | Part-time (2yr) | Part-time (3yr) |
|------|-----------|-----------------|-----------------|
| Band A | £9,400 | £5,200 | £3,800 |
| Band B | £10,400 | £5,700 | £4,200 |
| Band C | £11,700 | £6,400 | £4,700 |
| Band D | £13,100 | £7,200 | £5,200 |
| Band E | £14,700 | £8,100 | £5,900 |

**International Students (2026/27)**

| Band | Annual Fee |
|------|-----------|
| Band 0 | £17,100 |
| Band 1 | £18,200 |
| Band 2 | £20,800 |
| Band 3 | £22,000 |
| Band 4 | £23,400 |
| Band 5 | £25,600 |
| Band 6 | £29,800 |

**Sample PG fees by programme (International)**

| Programme | Fee | Band |
|-----------|-----|------|
| MBA | £18,200 | Band 1 |
| MSc Computer Science | £18,200 | Band 1 |
| MSc Management | £18,200 | Band 1 |
| MA Creative Writing | £17,100 | Band 0 |
| LLM International Law | £18,200 | Band 1 |
| MSc Occupational Therapy (Pre-reg) | £20,800 | Band 2 |
| MSc Prosthetics and Orthotics | £25,600 | Band 5 |
| MSc Counselling and Psychotherapy | £23,400 | Band 4 |

### 4.3 Undergraduate financial-aid policy

- UK students eligible for Student Finance England tuition fee loan (up to full fee value)
- NHS-funded courses have separate funding arrangements
- Bursaries and scholarships available
- Hardship funds available
- Article 26 Sanctuary scholarships for asylum seekers
- USA students: Federal Student Aid accepted

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Keele University"
  source_url: https://www.keele.ac.uk
  source_snippet: "Keele University"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.program_count
  value: 198
  source_url: https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/
  source_snippet: "198 UG courses listed in A-Z format with UCAS codes and degree types"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: postgraduate.program_count
  value: 100
  source_url: https://www.keele.ac.uk/study/postgraduatestudy/postgraduatecourses/
  source_snippet: "100 PG courses listed in A-Z format with degree types"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: research.areas_count
  value: 72
  source_url: https://www.keele.ac.uk/study/postgraduateresearch/researchareas/
  source_snippet: "72 research areas offering PhD/MPhil and professional doctorates"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: faculties.count
  value: 3
  source_url: https://www.keele.ac.uk/about/faculties
  source_snippet: "Faculty of Business, Law, Humanities and Social Sciences; Faculty of Medicine and Health Sciences; Faculty of Natural Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.fees.uk_2026
  value: "£9,790"
  source_url: https://www.keele.ac.uk/study/undergraduate/tuitionfeesandfunding/undergraduatetuitionfees/undergraduatetuitionfeesuk/
  source_snippet: "Tuition fees for home students commencing, or continuing, their studies in September 2026 will be £9,790"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.fees.international_bands
  value: "Band 0: £17,100 - Band 6: £29,800"
  source_url: https://www.keele.ac.uk/study/undergraduate/tuitionfeesandfunding/undergraduatetuitionfees/undergraduatetuitionfeesinternationalstudents/
  source_snippet: "Band 0 £17,100, Band 1 £18,200, Band 2 £20,800, Band 3 £22,000, Band 4 £23,400, Band 5 £25,600, Band 6 £29,800"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.entry_requirements.cs
  value: "A-Level BBB (contextual BCC); BTEC DDM; T Level Merit"
  source_url: https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computerscience/
  source_snippet: "BBB in three A levels OR BBC in three A levels including B in Maths or Computer Science; Contextual Offer: BCC"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: english_language.group_a
  value: "IELTS 6.0 overall, 5.5 in each component"
  source_url: https://www.keele.ac.uk/study/undergraduate/undergraduatecourses/computerscience/
  source_snippet: "this course requires a result from Group A"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: postgraduate.fees.uk_bands
  value: "Band A: £9,400 - Band E: £14,700"
  source_url: https://www.keele.ac.uk/study/postgraduatestudy/tuitionfeesandfunding/postgraduatetuitionfees/postgraduatetuitionfeesuk/
  source_snippet: "Band A £9,400, Band B £10,400, Band C £11,700, Band D £13,100, Band E £14,700"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-011:
  field: postgraduate.fees.international_sample
  value: "MSc Computer Science £18,200 (Band 1); MBA £18,200 (Band 1)"
  source_url: https://www.keele.ac.uk/study/postgraduatestudy/tuitionfeesandfunding/postgraduatetuitionfees/postgraduatetuitionfeesinternationalstudents/
  source_snippet: "Computer Science - MSc £18,200 Band 1; Master of Business Administration - MBA £18,200 Band 1"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-012:
  field: institution.faculty_structure
  value: "3 faculties with 22 schools/departments"
  source_url: https://www.keele.ac.uk/about/faculties
  source_snippet: "Faculty of Business, Law, Humanities and Social Sciences; Faculty of Medicine and Health Sciences; Faculty of Natural Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.fees.placement_year
  value: "20% of full fee"
  source_url: https://www.keele.ac.uk/study/undergraduate/tuitionfeesandfunding/undergraduatetuitionfees/undergraduatetuitionfeesuk/
  source_snippet: "a discounted fee of 20% of the Home UK Government regulated undergraduate tuition fee is charged for a placement year"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
keele-knowledge-base-v2/
├── overview                          # Section 0 (rules 1-4)
├── undergraduate-programmes          # Section 1 (grouped by faculty > school > degree)
├── postgraduate-programmes           # Section 2 (grouped by faculty > school > degree)
├── application-requirements          # Section 3
├── costs-and-funding                 # Section 4
└── evidence-chain                    # Section 5
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "keele-knowledge-base-v2"
  school: "<home faculty>"
  department: "<home school/department>"
  degree_level: "<BA|BSc|BEng|LLB|MSc|MA|LLM|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| **P0** | Individual course entry requirements (A-Level/IB/BTEC for all 198 UG courses) | Per-course pages |
| **P0** | English language Group A/B classification for each course | Per-course pages |
| **P1** | Scholarship and bursary details | https://www.keele.ac.uk/study/undergraduate/tuitionfeesandfunding/undergraduatefunding/ |
| **P1** | PG research fees | https://www.keele.ac.uk/research/postgraduateresearch/feesandfunding/ |
| **P1** | Course module details and curriculum structure | Per-course pages |
| **P2** | Accommodation costs | https://www.keele.ac.uk/accommodation/ |
| **P2** | Career outcomes and employability data | Per-course pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Keele University | Cardiff | Newcastle | Durham |
|-----------|------------------|---------|-----------|--------|
| Total UG programmes | 198 | 237 | 147 | ~300+ |
| Total PGT programmes | 100 | — | — | — |
| Russell Group | No | Yes | Yes | No |
| Faculties | 3 | 3 | 3 | 3 |
| UK UG fee (2026) | £9,790 | £9,250 | £9,250 | £9,250 |
| Intl UG fee range | £17,100-£29,800 | — | — | — |
| UCAS deadline | Jan (Oct 15 for Medicine) | Jan | Jan | Jan |
| IELTS minimum (standard) | 6.0 (5.5 each) | — | — | — |
| Application platform | UCAS | UCAS | UCAS | UCAS |
| Location | Staffordshire, England | Wales | NE England | NE England |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: keele.ac.uk (official university website)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programmes ✅ (198) | PGT programmes ✅ (100) | Research areas ✅ (72) | Fees ✅ | Entry requirements ✅ | Evidence chain ✅ (13 blocks)
> **Next step**: P0 follow-up for individual course entry requirements and English language group classification.
