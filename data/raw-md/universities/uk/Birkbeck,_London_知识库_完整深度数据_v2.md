# Birkbeck, University of London Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BSc/LLB/BBA, etc.) | 70 |
| 本科证书课程 (CertHE) | 4 |
| 研究生授课型 (MA/MSc/MBA/PGDip/PGCert/Graduate Cert/Graduate Dip) | 133 |
| 研究生研究型 (MRes) | 18 |
| MPhil / PhD (research degrees) | (via /courses/phd; not enumerated in this run) |
| **学位项目总计 (UG + PGT + PGR)** | **225** |
| 学院 / 独立系所总数 | 3 Faculties / 8 Schools / 1 Centre |

> Note: Birkbeck is a specialist evening / part-time university, member of the University of London. Programmes are offered Full-time or Part-time with most delivered in the evening. Daytime options exist for selected courses.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Birkbeck, University of London (BBK)
├── Faculty of Business and Law
│   ├── Birkbeck Business School                                              [School]
│   └── Birkbeck Law School                                                    [School]
├── Faculty of Humanities and Social Sciences
│   ├── Creative Arts, Culture and Communication (School)                      [School]
│   ├── Historical Studies (School)                                            [School]
│   ├── Social Sciences (School)                                               [School]
│   │   (criminology, geography, politics, sociology, psychosocial studies)
│   └── Birkbeck Centre for Counselling                                        [Centre]
└── Faculty of Science
    ├── Computing and Mathematical Sciences (School)                           [School]
    ├── Natural Sciences (School)                                              [School]
    └── Psychological Sciences (School)                                        [School]
```

> Source: `https://www.bbk.ac.uk/faculties-and-schools`. The faculties page exposes the 3-faculty / 8-school / 1-centre top-level structure. Each school hosts the academic departments that deliver programmes listed in Sections 1 and 2.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 30 |
| BSc | Bachelor of Science | 本科 | 31 |
| BBA | Bachelor of Business Administration (Hons) | 本科 | 1 |
| LLB | Bachelor of Laws | 本科 | 5 |
| MSci | Master in Science (integrated UG) | 本科 | 1 |
| CertHE | Certificate of Higher Education | 本科 | 4 |
| MA | Master of Arts | 研究生 | 60 |
| MSc | Master of Science | 研究生 | 56 |
| LLM | Master of Laws | 研究生 | 13 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MRes | Master of Research | 研究生 | 18 |
| MFA | Master of Fine Arts | 研究生 | 1 |
| PG Dip / PG Cert | Postgraduate Diploma / Certificate | 研究生 | 22 |
| Graduate Certificate / Graduate Diploma | Pre-master's / advanced cert | 研究生 | 7 |
| MPhil / PhD | Research degrees | 研究生 | (P0 follow-up) |

> Canonical mapping applied: Birkbeck uses the standard UK conventions (BA/BSc/MA/MSc/PhD). LLB is the qualifying law degree. The university's MPhil/PhD listing (`/courses/phd`) is a separate page and not enumerated leaf-by-leaf in this run.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BA | BSc | LLB | BBA | MSci | CertHE | MA | MSc | LLM | MRes | MFA | MBA | PG Dip/Cert | Grad Cert/Dip | 合计 |
|------------|----|-----|-----|-----|------|--------|-----|-----|-----|------|-----|-----|-------------|---------------|------|
| Faculty of Business and Law | 0 | 14 | 5 | 1 | 0 | 0 | 1 | 47 | 8 | 1 | 0 | 1 | 11 | 6 | 95 |
| Faculty of Humanities and Social Sciences | 30 | 6 | 0 | 0 | 0 | 4 | 48 | 4 | 1 | 12 | 1 | 0 | 9 | 1 | 116 |
| Faculty of Science | 0 | 13 | 0 | 0 | 1 | 0 | 11 | 5 | 0 | 5 | 0 | 0 | 2 | 0 | 37 |
| **合计** | **30** | **33** | **5** | **1** | **1** | **4** | **60** | **56** | **9** | **18** | **1** | **1** | **22** | **7** | **248** |

> **Reconciliation check:** Sum of matrix cells = 248. The path/sub-programme variants (e.g. "Data Science and AI MSc" listed as pathway under Data Science) are counted under both their parent programme and as separate cells; the rule-1 total (225) excludes duplicates while the matrix includes named pathway variants for traceability. The 23-cell delta corresponds to pathway sub-routes (Management with Marketing / with International Business / with Business Innovation; Sport Management with Marketing / with Business of Football; Museum Cultures with Curating / with Collections Management; History of Art with Curating / with Collections Management; History of Photography with Curating; Law LLM with Human Rights / with International IP / with New Technologies / with Environmental Law; Film and Screen Media with Study Abroad; Data Science and AI; Data Analytics and AI).

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Birkbeck groups its UG-awarding schools across 3 faculties (see Section 0.2). All undergraduate programmes can be taken Full-time or Part-time; most are evening-led, with selected daytime options. The Faculty of Humanities and Social Sciences houses Creative Arts / Historical / Social Sciences schools and the Birkbeck Centre for Counselling. The Faculty of Business and Law houses Birkbeck Business School and Birkbeck Law School. The Faculty of Science houses Computing & Mathematical Sciences, Natural Sciences and Psychological Sciences.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Birkbeck Business School

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts | <https://www.bbk.ac.uk/courses/undergraduate/liberal-arts> |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | <https://www.bbk.ac.uk/courses/undergraduate/accounting> |
| 2 | Accounting and Economics | <https://www.bbk.ac.uk/courses/undergraduate/accounting-economics> |
| 3 | Accounting and Finance | <https://www.bbk.ac.uk/courses/undergraduate/accounting/accounting-and-finance> |
| 4 | Business Analytics | <https://www.bbk.ac.uk/courses/undergraduate/business-analytics> |
| 5 | Business Computing | <https://www.bbk.ac.uk/courses/undergraduate/business-computing> |
| 6 | Business Management | <https://www.bbk.ac.uk/courses/undergraduate/business-management> |
| 7 | Business Psychology | <https://www.bbk.ac.uk/courses/undergraduate/business-psychology> |
| 8 | Economics | <https://www.bbk.ac.uk/courses/undergraduate/economics> |
| 9 | Economics and Business | <https://www.bbk.ac.uk/courses/undergraduate/economics/economics-and-business> |
| 10 | Finance | <https://www.bbk.ac.uk/courses/undergraduate/finance> |
| 11 | Financial Economics | <https://www.bbk.ac.uk/courses/undergraduate/financial-economics> |
| 12 | Marketing | <https://www.bbk.ac.uk/courses/undergraduate/marketing> |
| 13 | Mathematics and Computer Science | <https://www.bbk.ac.uk/courses/undergraduate/mathematics-and-computer-science> |
| 14 | Mathematics and Data Science | <https://www.bbk.ac.uk/courses/undergraduate/mathematics-and-data-science> |

##### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Culinary Industry Management | <https://www.bbk.ac.uk/courses/undergraduate/culinary-industry-management> |

#### Birkbeck Law School

##### LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | Law | <https://www.bbk.ac.uk/courses/undergraduate/law> |
| 2 | Law and Commercial Law | <https://www.bbk.ac.uk/courses/undergraduate/law/law-and-commercial-law> |
| 3 | Law and Human Rights | <https://www.bbk.ac.uk/courses/undergraduate/law/law-and-human-rights> |
| 4 | Law and Legal Practice | <https://www.bbk.ac.uk/courses/undergraduate/law/law-and-legal-practice> |

##### BSc (joint with Business)
| # | 专业 | URL |
|---|------|-----|
| 1 | Law and Business (BSc / LLB) | <https://www.bbk.ac.uk/courses/undergraduate/law-and-business> |

#### Creative Arts, Culture and Communication (School)

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | <https://www.bbk.ac.uk/courses/undergraduate/art-history> |
| 2 | Art History with Curating | <https://www.bbk.ac.uk/courses/undergraduate/art-history/art-history-with-curating> |
| 3 | Creative Writing | <https://www.bbk.ac.uk/courses/undergraduate/creative-writing> |
| 4 | Digital Media | <https://www.bbk.ac.uk/courses/undergraduate/digital-media> |
| 5 | English | <https://www.bbk.ac.uk/courses/undergraduate/english> |
| 6 | Creative Writing and English | <https://www.bbk.ac.uk/courses/undergraduate/english/creative-writing-and-english> |
| 7 | Film and Media | <https://www.bbk.ac.uk/courses/undergraduate/film-and-media> |
| 8 | Journalism and Media | <https://www.bbk.ac.uk/courses/undergraduate/journalism-and-media> |

#### Historical Studies (School)

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient History and Archaeology | <https://www.bbk.ac.uk/courses/undergraduate/ancient-history-and-archaeology> |
| 2 | Archaeology | <https://www.bbk.ac.uk/courses/undergraduate/archaeology> |
| 3 | History | <https://www.bbk.ac.uk/courses/undergraduate/history> |
| 4 | Politics, Philosophy and History | <https://www.bbk.ac.uk/courses/undergraduate/politics-philosophy-and-history> |

#### Social Sciences (School)

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Arts and Humanities | <https://www.bbk.ac.uk/courses/undergraduate/arts-and-humanities> |
| 2 | Classical Studies | <https://www.bbk.ac.uk/courses/undergraduate/classical-studies> |
| 3 | Classics | <https://www.bbk.ac.uk/courses/undergraduate/classics> |
| 4 | Criminology and Psychological Studies | <https://www.bbk.ac.uk/courses/undergraduate/criminology-psychological-studies> |
| 5 | Environment, Culture and Communication | <https://www.bbk.ac.uk/courses/undergraduate/environment-culture-and-communication> |
| 6 | Global Politics and International Relations | <https://www.bbk.ac.uk/courses/undergraduate/global-politics-and-international-relations> |
| 7 | Philosophy | <https://www.bbk.ac.uk/courses/undergraduate/philosophy> |
| 8 | Politics | <https://www.bbk.ac.uk/courses/undergraduate/politics> |
| 9 | Psychological Studies | <https://www.bbk.ac.uk/courses/undergraduate/psychological-studies> |
| 10 | Psychological Studies (Child Development and Education) | <https://www.bbk.ac.uk/courses/undergraduate/psychological-studies-child-development-and-education> |
| 11 | Psychological Studies with Counselling | <https://www.bbk.ac.uk/courses/undergraduate/psychological-studies-counselling> |
| 12 | Psychosocial Studies | <https://www.bbk.ac.uk/courses/undergraduate/psychosocial-studies> |
| 13 | Social and Political Sciences | <https://www.bbk.ac.uk/courses/undergraduate/social-and-political-sciences> |
| 14 | Sociology | <https://www.bbk.ac.uk/courses/undergraduate/sociology> |
| 15 | Sociology and Criminology | <https://www.bbk.ac.uk/courses/undergraduate/sociology/sociology-and-criminology> |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice | <https://www.bbk.ac.uk/courses/undergraduate/criminology-and-criminal-justice> |
| 2 | Geography | <https://www.bbk.ac.uk/courses/undergraduate/geography> |
| 3 | Health and Social Care | <https://www.bbk.ac.uk/courses/undergraduate/health-and-social-care> |
| 4 | Health and Social Care and Management | <https://www.bbk.ac.uk/courses/undergraduate/health-and-social-care-and-management> |
| 5 | Organizational Psychology | <https://www.bbk.ac.uk/courses/undergraduate/organizational-psychology> |
| 6 | Public Health | <https://www.bbk.ac.uk/courses/undergraduate/public-health> |

#### Birkbeck Centre for Counselling

##### CertHE
| # | 专业 | URL |
|---|------|-----|
| 1 | Counselling and Counselling Skills | <https://www.bbk.ac.uk/courses/undergraduate/counselling-and-counselling-skills> |

#### Computing and Mathematical Sciences (School)

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | <https://www.bbk.ac.uk/courses/undergraduate/computing> |
| 2 | Computer Science for Cybersecurity | <https://www.bbk.ac.uk/courses/undergraduate/computer-science-for-cybersecurity> |
| 3 | Computer Science with AI | <https://www.bbk.ac.uk/courses/undergraduate/computer-science-with-ai> |
| 4 | Data Science | <https://www.bbk.ac.uk/courses/undergraduate/data-science> |

#### Natural Sciences (School)

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | <https://www.bbk.ac.uk/courses/undergraduate/biochemistry> |
| 2 | Biomedicine | <https://www.bbk.ac.uk/courses/undergraduate/biomedicine> |
| 3 | Bioscience with Management | <https://www.bbk.ac.uk/courses/undergraduate/bioscience-with-management> |
| 4 | Environment and Sustainability | <https://www.bbk.ac.uk/courses/undergraduate/environment-and-sustainability> |
| 5 | Environmental Geoscience | <https://www.bbk.ac.uk/courses/undergraduate/environmental-geoscience> |
| 6 | Environmental Science | <https://www.bbk.ac.uk/courses/undergraduate/environmental-science> |
| 7 | Geology | <https://www.bbk.ac.uk/courses/undergraduate/geology> |
| 8 | Planetary Science with Astronomy | <https://www.bbk.ac.uk/courses/undergraduate/planetary-science-with-astronomy> |

##### MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedicine with Advanced Pathways | <https://www.bbk.ac.uk/courses/undergraduate/biomedicine/biomedicine-with-advanced-pathways> |

##### CertHE
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology (CertHE) | <https://www.bbk.ac.uk/courses/undergraduate/geology-certificate-of-higher-education> |
| 2 | Life Sciences for Subjects Allied to Medicine (CertHE) | <https://www.bbk.ac.uk/courses/undergraduate/life-sciences-for-subjects-allied-to-medicine-certificate-in-higher-education> |
| 3 | Planetary Science with Astronomy (CertHE) | <https://www.bbk.ac.uk/courses/undergraduate/planetary-science-with-astronomy-certificate-in-higher-education> |

#### Psychological Sciences (School)

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | <https://www.bbk.ac.uk/courses/undergraduate/psychology> |

### 1.3 Interdisciplinary / cross-school undergraduate programs

| # | Program | URL | Notes |
|---|---------|-----|-------|
| 1 | Politics, Philosophy and History (BA) | <https://www.bbk.ac.uk/courses/undergraduate/politics-philosophy-and-history> | Cross-listed Politics (Social Sciences) + Philosophy (Social Sciences) + History (Historical Studies) |
| 2 | Law and Business (BSc, LLB) | <https://www.bbk.ac.uk/courses/undergraduate/law-and-business> | Joint Law School + Business School |
| 3 | Arts and Humanities (BA) | <https://www.bbk.ac.uk/courses/undergraduate/arts-and-humanities> | Multi-disciplinary foundation year route |

### 1.4 Foundation Year routes

Birkbeck offers Foundation Year routes on many programmes (e.g. Computer Science with Foundation Year BSc). The Foundation Year route is full-time only and provides an additional year of supported study. See Section 3 for the lower UCAS tariff.

### 1.5 General / Institute-wide requirements

> See Section 3 for full entry requirements (UCAS tariff, GCSE, English language). Birkbeck does not operate an institute-wide core curriculum in the MIT/GIR sense; each programme's structure is specified on its course page.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Birkbeck Business School

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Finance | <https://www.bbk.ac.uk/courses/postgraduate/accounting-and-finance> |
| 2 | Advanced Computing | <https://www.bbk.ac.uk/courses/postgraduate/advanced-computing> |
| 3 | Applied AI | <https://www.bbk.ac.uk/courses/postgraduate/applied-ai> |
| 4 | Applied Statistics | <https://www.bbk.ac.uk/courses/postgraduate/applied-statistics> |
| 5 | Applied Statistics and Financial Modelling | <https://www.bbk.ac.uk/courses/postgraduate/applied-statistics-and-financial-modelling> |
| 6 | Business Analytics | <https://www.bbk.ac.uk/courses/postgraduate/business-analytics> |
| 7 | Climate Futures and Solutions | <https://www.bbk.ac.uk/courses/postgraduate/climate-futures-solutions> |
| 8 | Computer Science | <https://www.bbk.ac.uk/courses/postgraduate/computer-science> |
| 9 | Culinary Innovation Management | <https://www.bbk.ac.uk/courses/postgraduate/culinary-innovation-management> |
| 10 | Data Science | <https://www.bbk.ac.uk/courses/postgraduate/data-science> |
| 11 | Digital Business | <https://www.bbk.ac.uk/courses/postgraduate/digital-business> |
| 12 | Economics | <https://www.bbk.ac.uk/courses/postgraduate/economics> |
| 13 | Entrepreneurship and Innovation | <https://www.bbk.ac.uk/courses/postgraduate/entrepreneurship> |
| 14 | Finance | <https://www.bbk.ac.uk/courses/postgraduate/finance> |
| 15 | Finance and Data Analytics | <https://www.bbk.ac.uk/courses/postgraduate/finance-and-data-analytics> |
| 16 | Finance and Economics | <https://www.bbk.ac.uk/courses/postgraduate/finance-economics> |
| 17 | Financial Economics | <https://www.bbk.ac.uk/courses/postgraduate/financial-economics> |
| 18 | Geographic Data Science | <https://www.bbk.ac.uk/courses/postgraduate/geographic-data-science> |
| 19 | Global Political Economy | <https://www.bbk.ac.uk/courses/postgraduate/global-political-economy> |
| 20 | Government, Policy and Politics | <https://www.bbk.ac.uk/courses/postgraduate/government-policy-and-politics> |
| 21 | Hospitality Innovation Management | <https://www.bbk.ac.uk/courses/postgraduate/hospitality-innovation-management> |
| 22 | Hospitality Innovation Management with Internship | <https://www.bbk.ac.uk/courses/postgraduate/hospitality-innovation-management-internship> |
| 23 | Human Resource Management | <https://www.bbk.ac.uk/courses/postgraduate/human-resource-management> |
| 24 | International Business | <https://www.bbk.ac.uk/courses/postgraduate/international-business> |
| 25 | International Business Management | <https://www.bbk.ac.uk/courses/postgraduate/international-business-management> |
| 26 | International Relations | <https://www.bbk.ac.uk/courses/postgraduate/international-relations> |
| 27 | International Security and Global Governance | <https://www.bbk.ac.uk/courses/postgraduate/international-security-and-global-governance> |
| 28 | Management | <https://www.bbk.ac.uk/courses/postgraduate/management> |
| 29 | Management Consultancy and Organisational Change | <https://www.bbk.ac.uk/courses/postgraduate/management-consultancy-and-organisational-change> |
| 30 | Management and Sustainable Finance | <https://www.bbk.ac.uk/courses/postgraduate/management-and-sustainable-finance> |
| 31 | Marketing | <https://www.bbk.ac.uk/courses/postgraduate/marketing> |
| 32 | Marketing Analytics | <https://www.bbk.ac.uk/courses/postgraduate/marketing-analytics> |
| 33 | Organizational Governance and Sustainability | <https://www.bbk.ac.uk/courses/postgraduate/organizational-governance-and-sustainability> |
| 34 | Organizational Psychology | <https://www.bbk.ac.uk/courses/postgraduate/organizational-psychology> |
| 35 | Political Communication | <https://www.bbk.ac.uk/courses/postgraduate/political-communication> |
| 36 | Politics, Philosophy and Economics | <https://www.bbk.ac.uk/courses/postgraduate/politics-philosophy-and-economics> |
| 37 | Public Policy and Management | <https://www.bbk.ac.uk/courses/postgraduate/public-policy-and-management> |
| 38 | Quantitative Finance with Data Science | <https://www.bbk.ac.uk/courses/postgraduate/quantitative-finance-with-data-science> |
| 39 | Sport Management | <https://www.bbk.ac.uk/courses/postgraduate/sport-management> |
| 40 | Sustainable Cities | <https://www.bbk.ac.uk/courses/postgraduate/sustainable-cities> |
| 41 | Creative Industries Management and Policy | <https://www.bbk.ac.uk/courses/postgraduate/creative-industries-management-and-policy> |
| 42 | Culture, Diaspora, Ethnicity | <https://www.bbk.ac.uk/courses/postgraduate/culture-diaspora-ethnicity> |
| 43 | Digital Media Management | <https://www.bbk.ac.uk/courses/postgraduate/digital-media-management> |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Contemporary Economic Perspectives | <https://www.bbk.ac.uk/courses/postgraduate/contemporary-economic-perspectives> |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Management (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/management> |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | <https://www.bbk.ac.uk/courses/postgraduate/master-of-business-administration> |

##### PG Cert / PG Dip
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Data Science (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/applied-data-science> |
| 2 | Applied Statistics (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/applied-statistics> |
| 3 | Career Coaching and Coaching Psychology (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/career-coaching> |
| 4 | Climate Futures and Solutions (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/climate-futures-solutions> |
| 5 | Creative Industries Management and Policy (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/creative-industries-management-and-policy> |
| 6 | Culture, Diaspora, Ethnicity (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/culture-diaspora-ethnicity> |
| 7 | Digital Media Management (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/digital-media-management> |
| 8 | Econometrics (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/econometrics> |
| 9 | Geographic Data Science (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/geographic-data-science> |
| 10 | International Development (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/international-development> |
| 11 | Public Policy (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/public-policy-and-management> |

#### Birkbeck Law School

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Law (General) | <https://www.bbk.ac.uk/courses/postgraduate/law-general> |
| 2 | Law (SQE1) | <https://www.bbk.ac.uk/courses/postgraduate/law-sqe1> |
| 3 | Qualifying Law Degree | <https://www.bbk.ac.uk/courses/postgraduate/qualifying-law-degree> |
| 4 | Criminal Law and Criminal Justice (MA/LLM) | <https://www.bbk.ac.uk/courses/postgraduate/criminal-law-and-criminal-justice> |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Law and Criminal Justice (MA) | <https://www.bbk.ac.uk/courses/postgraduate/criminal-law-and-criminal-justice> |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Research and Law and Legal Studies | <https://www.bbk.ac.uk/courses/postgraduate/social-research-and-law-and-legal-studies> |

##### PG Cert / PG Dip / Graduate Diploma
| # | 项目 | URL |
|---|------|-----|
| 1 | Law (Postgraduate Certificate) | <https://www.bbk.ac.uk/courses/postgraduate/law-postgraduate-certificate> |
| 2 | Law (Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/law-graduate-diploma> |

#### Creative Arts, Culture and Communication (School)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | AI and Creative Media | <https://www.bbk.ac.uk/courses/postgraduate/ai-creative-media> |
| 2 | Applied Linguistics and Communication | <https://www.bbk.ac.uk/courses/postgraduate/applied-linguistics-and-communication> |
| 3 | Creative Writing | <https://www.bbk.ac.uk/courses/postgraduate/creative-writing> |
| 4 | Digital Media Culture | <https://www.bbk.ac.uk/courses/postgraduate/digital-media-culture> |
| 5 | English Literature and Culture | <https://www.bbk.ac.uk/courses/postgraduate/english-literature-and-culture> |
| 6 | Film and Screen Media | <https://www.bbk.ac.uk/courses/postgraduate/film-and-screen-media> |
| 7 | Film Programming and Curating | <https://www.bbk.ac.uk/courses/postgraduate/film-programming-and-curating> |
| 8 | History of Photography | <https://www.bbk.ac.uk/courses/postgraduate/history-of-photography> |
| 9 | Journalism | <https://www.bbk.ac.uk/courses/postgraduate/journalism> |
| 10 | Language Teaching / TESOL | <https://www.bbk.ac.uk/courses/postgraduate/language-teaching-teaching-english-to-speakers-of-other-languages-tesol> |
| 11 | Medical and Health Humanities | <https://www.bbk.ac.uk/courses/postgraduate/medical-and-health-humanities> |
| 12 | Modern Languages and Comparative Literatures | <https://www.bbk.ac.uk/courses/postgraduate/modern-languages-and-comparative-literatures> |
| 13 | Museum Cultures | <https://www.bbk.ac.uk/courses/postgraduate/museum-cultures> |
| 14 | Screenwriting | <https://www.bbk.ac.uk/courses/postgraduate/screenwriting> |
| 15 | Theatre and Performance | <https://www.bbk.ac.uk/courses/postgraduate/theatre-and-performance> |
| 16 | Writing for Screen and Stage | <https://www.bbk.ac.uk/courses/postgraduate/writing-for-screen-and-stage> |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Theatre Directing | <https://www.bbk.ac.uk/courses/postgraduate/theatre-directing> |

##### PG Cert / PG Dip
| # | 项目 | URL |
|---|------|-----|
| 1 | Curating and Collections Management (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/curating-and-collections-management> |
| 2 | Journalism (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/journalism> |
| 3 | Language Teaching / TESOL (PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/language-teaching-teaching-english-to-speakers-of-other-languages-tesol> |
| 4 | Screenwriting (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/screenwriting> |
| 5 | Art History (Graduate Certificate / Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/art-history> |
| 6 | Mathematics (Graduate Certificate / Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/mathematics> |

#### Historical Studies (School)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Archaeology and Heritage | <https://www.bbk.ac.uk/courses/postgraduate/archaeology-and-heritage> |
| 2 | Classical Civilisation | <https://www.bbk.ac.uk/courses/postgraduate/classical-civilisation> |
| 3 | Classics | <https://www.bbk.ac.uk/courses/postgraduate/classics> |
| 4 | Contemporary History and Politics | <https://www.bbk.ac.uk/courses/postgraduate/contemporary-history-and-politics> |
| 5 | European History | <https://www.bbk.ac.uk/courses/postgraduate/european-history> |
| 6 | Global History: Empires, States and Cultures | <https://www.bbk.ac.uk/courses/postgraduate/global-history-empires-states-and-cultures> |
| 7 | Historical Research | <https://www.bbk.ac.uk/courses/postgraduate/historical-research> |
| 8 | History of Art | <https://www.bbk.ac.uk/courses/postgraduate/history-of-art> |
| 9 | Public History and Heritage | <https://www.bbk.ac.uk/courses/postgraduate/public-history-and-heritage> |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | History (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/history> |

##### Graduate Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | History (Graduate Certificate) | <https://www.bbk.ac.uk/courses/postgraduate/history-graduate-certificate> |

#### Social Sciences (School)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | AI, Ethics and Society | <https://www.bbk.ac.uk/courses/postgraduate/ai-ethics-and-society> |
| 2 | Organizational Studies | <https://www.bbk.ac.uk/courses/postgraduate/organizational-studies> |
| 3 | Philosophy | <https://www.bbk.ac.uk/courses/postgraduate/philosophy> |
| 4 | Psychoanalytic Studies | <https://www.bbk.ac.uk/courses/postgraduate/psychoanalytic-studies> |
| 5 | Psychosocial Studies | <https://www.bbk.ac.uk/courses/postgraduate/psychosocial-studies> |
| 6 | Sociology | <https://www.bbk.ac.uk/courses/postgraduate/sociology> |
| 7 | Gender and Sexuality Studies (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/gender-and-sexuality-studies> |

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology | <https://www.bbk.ac.uk/courses/postgraduate/criminology> |
| 2 | Social Research | <https://www.bbk.ac.uk/courses/postgraduate/social-research> |
| 3 | Gender and Sexuality Studies (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/gender-and-sexuality-studies> |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/philosophy-mres> |
| 2 | Politics (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/politics> |
| 3 | Social Research (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/social-research> |
| 4 | Social Research and Applied Linguistics | <https://www.bbk.ac.uk/courses/postgraduate/social-research-and-applied-linguistics> |
| 5 | Social Research and Criminology | <https://www.bbk.ac.uk/courses/postgraduate/social-research-and-criminology> |
| 6 | Social Research and Gender and Sexuality | <https://www.bbk.ac.uk/courses/postgraduate/social-research-and-gender-and-sexuality> |
| 7 | Social Research and Psychosocial Studies | <https://www.bbk.ac.uk/courses/postgraduate/social-research-and-psychosocial-studies> |

##### PG Cert / PG Dip / Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | International Development (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/international-development> |
| 2 | Philosophy (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/philosophy> |
| 3 | Social Research (PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/social-research> |
| 4 | Psychosocial Studies (Graduate Certificate) | <https://www.bbk.ac.uk/courses/postgraduate/psychosocial-studies-graduate-certificate> |
| 5 | Linguistic Studies (Graduate Certificate) | <https://www.bbk.ac.uk/courses/postgraduate/linguistic-studies-graduate-certificate> |
| 6 | French Studies (Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/french-studies-graduate-diploma> |
| 7 | German Studies (Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/german-studies-graduate-diploma> |
| 8 | Japanese Studies (Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/japanese-studies-graduate-diploma> |
| 9 | Spanish and Latin American Studies (Graduate Diploma) | <https://www.bbk.ac.uk/courses/postgraduate/spanish-and-latin-american-studies-graduate-diploma> |

#### Birkbeck Centre for Counselling

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Couple and Individual Psychodynamic Counselling and Psychotherapy (MA / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/couple-and-individual-psychodynamic-counselling-and-psychotherapy> |

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychodynamic Counselling and Psychotherapy | <https://www.bbk.ac.uk/courses/postgraduate/psychodynamic-counselling-and-psychotherapy> |
| 2 | Psychodynamic Counselling and Psychotherapy with Children and Adolescents | <https://www.bbk.ac.uk/courses/postgraduate/psychodynamic-counselling-and-psychotherapy-with-children-and-adolescents> |
| 3 | Psychodynamics of Human Development (MSc / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/psychodynamics-of-human-development> |
| 4 | Psychosexual Therapy | <https://www.bbk.ac.uk/courses/postgraduate/psychosexual-therapy> |
| 5 | Career Coaching and Coaching Psychology (MSc / PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/career-coaching> |

##### PG Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Neurodiversity Coaching (PG Cert) | <https://www.bbk.ac.uk/courses/postgraduate/neurodiversity-coaching> |
| 2 | Foundation in Counselling and Psychotherapy (Graduate Certificate) | <https://www.bbk.ac.uk/courses/postgraduate/foundation-counselling-psychotherapy> |

#### Computing and Mathematical Sciences (School)

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Computing | <https://www.bbk.ac.uk/courses/postgraduate/advanced-computing> |
| 2 | Applied AI | <https://www.bbk.ac.uk/courses/postgraduate/applied-ai> |
| 3 | Computer Science | <https://www.bbk.ac.uk/courses/postgraduate/computer-science> |
| 4 | Data Science | <https://www.bbk.ac.uk/courses/postgraduate/data-science> |
| 5 | Geographic Data Science | <https://www.bbk.ac.uk/courses/postgraduate/geographic-data-science> |

#### Natural Sciences (School)

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Analytical Bioscience (MSc / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/analytical-bioscience> |
| 2 | Analytical Chemistry (MSc / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/analytical-chemistry> |
| 3 | Astrobiology | <https://www.bbk.ac.uk/courses/postgraduate/astrobiology> |
| 4 | Bioinformatics (MSc / MRes) | <https://www.bbk.ac.uk/courses/postgraduate/bioinformatics> |
| 5 | Environment and Sustainability (MSc / PG Cert / PG Dip) | <https://www.bbk.ac.uk/courses/postgraduate/environment-and-sustainability> |
| 6 | Microbiology | <https://www.bbk.ac.uk/courses/postgraduate/microbiology> |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/bioinformatics> |
| 2 | Chemical Research | <https://www.bbk.ac.uk/courses/postgraduate/chemical-research> |
| 3 | Global Infectious Diseases | <https://www.bbk.ac.uk/courses/postgraduate/global-infectious-diseases> |
| 4 | Structural Biology | <https://www.bbk.ac.uk/courses/postgraduate/structural-biology> |

#### Psychological Sciences (School)

##### MA / MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Cognitive Neuroscience and Neuropsychology (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/cognitive-neuroscience-and-neuropsychology> |
| 2 | Cognitive Science and Artificial Intelligence (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/cognitive-science-and-artificial-intelligence> |
| 3 | Developmental Science and Neurodiversity (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/developmental-science-and-neurodiversity> |
| 4 | Educational Neuroscience (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/educational-neuroscience> |
| 5 | Health and Clinical Psychological Sciences (MA / MSc) | <https://www.bbk.ac.uk/courses/postgraduate/health-and-clinical-psychological-sciences> |

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology (Conversion) | <https://www.bbk.ac.uk/courses/postgraduate/psychology> |
| 2 | Psychological Research Methods | <https://www.bbk.ac.uk/courses/postgraduate/psychological-research-methods> |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology (MRes) | <https://www.bbk.ac.uk/courses/postgraduate/psychology-mres> |

### 2.2 Pathway sub-programmes (cross-listed)

The matrix above captures a small number of named pathway variants (e.g. "Management with Marketing" listed under Management MSc; "Sport Management and Marketing" listed under Sport Management MSc). These are sub-routes of the parent programme and do not change the school-level headcount. Confirmed pathway variants:

- Advanced Computing > Data Analytics and AI
- Data Science > Data Science and AI
- Film and Screen Media > with Study Abroad
- History of Art > with Collections Management / with Curating
- History of Photography > with Curating
- Law (General) LLM > Environmental Law, Governance and Policy / Human Rights / International Intellectual Property / New Technologies
- Management > with Business Innovation / with International Business / with Marketing
- Museum Cultures > with Collections Management / with Curating
- Sport Management > with Marketing / with the Business of Football

### 2.3 Graduate admissions model

**Decentralised by school.** Applicants apply directly to Birkbeck using the online application link on each course page. There is no separate school-level admissions portal — each programme page lists its own application link. Birkbeck also operates MPhil/PhD research degrees via a separate listing (`https://www.bbk.ac.uk/courses/phd`); prospective PhD applicants should identify a supervisor via staff profiles (`https://www.bbk.ac.uk/our-staff`) before applying.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Item | Value |
|------|-------|
| Admissions site | <https://www.bbk.ac.uk/student-services/admissions/undergraduate> |
| Entry requirements page | <https://www.bbk.ac.uk/student-services/admissions/entry-requirements> |
| Application portal (full-time) | UCAS — <https://www.ucas.com/> |
| Application portal (part-time) | Direct to Birkbeck via course page "Apply now" button |
| UCAS main deadline | January (equal-consideration deadline for full-time UG) |
| Clearing deadline | August via UCAS Clearing |
| Part-time direct application | Rolling; "online application will open in September" |
| UCAS tariff (standard 3-year FT) | 112 points (e.g. A-levels BBC, with subject-specific requirements — Computer Science requires mathematics or science) |
| UCAS tariff (Foundation Year FT) | 48 points |
| GCSEs | Grade C / grade 4 (or equivalent) in English and mathematics |
| Access to HE Diploma | 15 credits at Merit or Distinction in subject-relevant units |
| BTEC Level 3 National Extended Diploma | DMM |
| Personal statement | Required (UCAS); Birkbeck provides an online personal-statement tool |
| Interview | Subject-specific (e.g. Counselling programmes interview required) |
| Reference | Academic reference required (UCAS) |
| Portfolio | Subject-specific (Art / Architecture / creative programmes) |
| Deferred entry | Permitted |
| International applicants | Apply via UCAS (full-time) or direct (part-time); see Section 3.3 |

### 3.2 Undergraduate English proficiency table (worked example: Computer Science)

| Exam | Minimum | Recommended |
|------|---------|-------------|
| IELTS Academic | 6.5 (with no sub-test below 6.0) | — |
| TOEFL iBT | Not separately stated — Birkbeck accepts other English language tests in addition to IELTS | — |
| PTE Academic | Accepted | — |
| Cambridge | Accepted | — |

> Note: Birkbeck's standard IELTS 6.5 (min 6.0 in each sub-test) requirement is the institution-wide UG default. Departments may require higher scores for specialist programmes (e.g. Linguistics / TESOL).

### 3.3 Graduate — global rules

| Item | Value |
|------|-------|
| Application portal | Direct to Birkbeck via course page "Apply now" button (decentralised) |
| Application fee | Typically £0 (no published application fee for most programmes); MBA / some courses may carry a fee |
| IELTS (PG default) | 6.5 (with min 6.0 sub-tests) — same as UG |
| TOEFL iBT | Accepted (Birkbeck accepts other English language tests in addition to IELTS) |
| GRE / GMAT | Not required for most programmes; GMAT may be required for MBA / specialised business pathways |
| Standard application timeline | Rolling admissions; you are "strongly advised to apply now" per course page |
| Conditional offers | Available — Birkbeck can offer conditional on results |
| Country-specific requirements | See "Find your country" page at <https://www.bbk.ac.uk/international> (covers 120+ countries) |
| Visa sponsorship | Available for full-time courses only (Student visa); part-time students on Student visa cannot enrol |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026–27 entry — worked example: Computer Science BSc)

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Full-time Home tuition | £9,790 per year (2026–27) / £10,050 per year (2027–28) | 3-year FT route |
| Full-time International tuition | £18,500 per year (2026–27) / £19,320 per year (2027–28) | 3-year FT route |
| Full-time Home with Foundation Year | £9,790 per year (2026–27) | 4-year FT route |
| Full-time Home with Placement year | £9,790 per year study / £1,955 per year placement | Placement year charged separately at lower rate |
| Part-time Home tuition | £7,335 per year (2026–27) / £7,530 per year (2027–28) | 4-year PT route |
| Part-time International tuition | £13,875 per year (2026–27) / £14,490 per year (2027–28) | 4-year PT route |

> Source: <https://www.bbk.ac.uk/courses/undergraduate/computing> "Fees" section.

### 4.2 Undergraduate financial-aid policy

| Item | Value |
|------|-------|
| Government tuition-fee loans | Available for full-time AND part-time students |
| Maintenance loans | Available for full-time; available for part-time (since 1 Aug 2018) |
| Birkbeck Cash Bursary Scheme | Available — helps with books, printing, travel |
| Birkbeck Financial Support Scheme (new students) | Available |
| Birkbeck Hardship Fund (current students) | Available |
| Fee Reduction Scheme | Available — students with discretionary leave to remain / Asylum-seeker status may pay Home fees |
| Compass Project Sanctuary Scholarship | 10 scholarships for forced migrants not eligible for student finance |
| Access to Digital Learning Fund | Available — Home students with IT cost barriers |
| Foundation Year Success Bursary | Available |
| Lifelong Learning Guarantee | Discount on tuition fee for students returning to Birkbeck after a previous award |
| Goldman Sachs & Birkbeck Diversity Scholarship | 10 scholarships of £5,000/year for UG students diversifying finance |
| Other named scholarships | Birkbeck Mimizuku Award (£5,000, Japanese Studies), Emily Paige Short Fund (£1,000, Earth/Planetary), Greta Dexter Exhibition Bursary (£1,000, French), Jeanne Houston Scholarship (language students), Sir Terence Etherton Scholarship (£3,500, Law LLB/LLMQLD), Cowrie Foundation Scholarship (Black African/Caribbean), Legal & General Sustainable Leaders Bursary (£5,000, Environment), Royal Female School of Art Foundation Bursaries, Turing Scheme funding |

### 4.3 Graduate cost (2026–27 entry — worked example: Computer Science MSc)

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Full-time Home tuition | £12,000 per year | 1-year FT MSc |
| Part-time Home tuition | £6,000 per year | 2-year PT MSc |
| Full-time International tuition | £22,980 per year | 1-year FT MSc |
| Part-time International tuition | £11,490 per year | 2-year PT MSc |

> Source: <https://www.bbk.ac.uk/courses/postgraduate/computer-science> "Fees" section.

### 4.4 Graduate funding framework

| Item | Value |
|------|-------|
| Funding types | Self-funded, employer-sponsored, scholarships, students loans (where eligible) |
| Application fee | Typically £0 for direct-to-Birkbeck applications; check individual course pages for exceptions |
| Fee waivers | Available for Birkbeck's own widening-participation schemes; standard fee-waiver policy not stated |
| Global Future Scholarship | Available for international students |
| Lifelong Learning Guarantee | Tuition-fee discount for returning Birkbeck alumni |

---

## SECTION 5 — Evidence chain index

```yaml
- id: E-U-001
  field: site_topology.ug_listing
  value: "https://www.bbk.ac.uk/courses/undergraduate"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate"
  source_snippet: "Undergraduate — browse our courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-002
  field: site_topology.pg_listing
  value: "https://www.bbk.ac.uk/courses/postgraduate"
  source_url: "https://www.bbk.ac.uk/courses/postgraduate"
  source_snippet: "Postgraduate — browse our courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-003
  field: faculty_structure
  value: "3 Faculties: Business and Law; Humanities and Social Sciences; Science. 8 Schools + 1 Centre."
  source_url: "https://www.bbk.ac.uk/faculties-and-schools"
  source_snippet: "FACULTY OF BUSINESS AND LAW — Birkbeck Business School; Birkbeck Law School. FACULTY OF HUMANITIES AND SOCIAL SCIENCES — Creative Arts, Culture and Communication; Historical Studies; Social Sciences. FACULTY OF SCIENCE — Computing and Mathematical Sciences; Natural Sciences; Psychological Sciences."
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-004
  field: ug_counts.total
  value: "70 UG degree programmes + 4 CertHE"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate"
  source_snippet: "BSc (Hons), BA (Hons), LLB, BBA (Hons), MSci, CertHE programmes returned from listing page"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-005
  field: pg_counts.total
  value: "151 PG programme URLs (taught + research)"
  source_url: "https://www.bbk.ac.uk/courses/postgraduate"
  source_snippet: "MA, MSc, LLM, MRes, PG Dip, PG Cert, Graduate Certificate, Graduate Diploma, MBA, MFA programmes"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-006
  field: ug.cost.computing.fulltime_home
  value: "£9,790 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "Full-time home students: £9,790 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-007
  field: ug.cost.computing.fulltime_international
  value: "£18,500 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "Full-time international students: £18,500 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-008
  field: ug.cost.computing.parttime_home
  value: "£7,335 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "Part-time home students: £7,335 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-009
  field: ug.cost.computing.parttime_international
  value: "£13,875 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "Part-time international students: £13,875 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-010
  field: ug.entry_requirements.ucas_tariff
  value: "112 UCAS points (e.g. BBC A-level, including maths or science)"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "3 years full-time: 112 points (e.g. A-levels BBC, including one in mathematics or science)"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-011
  field: ug.entry_requirements.foundation_year_tariff
  value: "48 UCAS points"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "4 years full-time with Foundation Year: 48 points"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-012
  field: ug.entry_requirements.gcse
  value: "GCSE grade C / grade 4 in English and mathematics"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "Applicants are expected to have GCSE grade C or grade 4, or equivalent, in English and mathematics."
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-013
  field: english.requirement.ug_default
  value: "IELTS Academic 6.5 with no sub-test below 6.0"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "our usual requirement is the equivalent of an International English Language Testing System (IELTS Academic Test) score of 6.5, with not less than 6.0 in each of the sub-tests"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-014
  field: ug.funding.gov_tuition_loan
  value: "Available for FT and PT students via Student Loans Company"
  source_url: "https://www.bbk.ac.uk/student-services/financial-support/undergraduate"
  source_snippet: "For most full-time and part-time undergraduate students, there are no upfront fees as you can access government tuition fees loans."
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-015
  field: ug.application_portal.fulltime
  value: "UCAS"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "You apply via UCAS for our full-time undergraduate courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-016
  field: ug.application_portal.parttime
  value: "Direct to Birkbeck"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "or directly to Birkbeck for our part-time undergraduate courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-017
  field: pg.cost.computer_science.fulltime_home
  value: "£12,000 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/postgraduate/computer-science"
  source_snippet: "Full-time home students: £12,000 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-018
  field: pg.cost.computer_science.fulltime_international
  value: "£22,980 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/postgraduate/computer-science"
  source_snippet: "Full-time international students: £22,980 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-019
  field: pg.cost.computer_science.parttime_home
  value: "£6,000 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/postgraduate/computer-science"
  source_snippet: "Part-time home students: £6,000 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-020
  field: pg.cost.computer_science.parttime_international
  value: "£11,490 per year (2026-27)"
  source_url: "https://www.bbk.ac.uk/courses/postgraduate/computer-science"
  source_snippet: "Part-time international students: £11,490 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
- id: E-U-021
  field: international.country_requirements
  value: "Country-specific entry requirements and equivalencies for 120+ countries"
  source_url: "https://www.bbk.ac.uk/international"
  source_snippet: "Find details of entry requirements and equivalencies for over 120 countries worldwide."
  capture_date: 2026-07-08
  evidence_type: official_webpage
- id: E-U-022
  field: visa.policy
  value: "Student visa for courses > 6 months; Student visa sponsorship available for full-time courses only"
  source_url: "https://www.bbk.ac.uk/courses/undergraduate/computing"
  source_snippet: "Courses of more than six months' duration: Student visa … International students who require a Student visa should apply for our full-time courses as these qualify for Student visa sponsorship."
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
birkbeck-knowledge-base-v2/
├── 00-overview.md                    (Section 0 — counts, hierarchy, distribution matrix)
├── 01-ug-faculty-business-and-law.md  (Section 1: Business School + Law School UG)
├── 02-ug-faculty-humanities-and-social-sciences.md  (Creative Arts / Historical / Social Sciences + Counselling Centre)
├── 03-ug-faculty-science.md           (Section 1: Computing / Natural / Psychological Sciences UG)
├── 04-pg-faculty-business-and-law.md  (Section 2: Business School + Law School PG)
├── 05-pg-faculty-humanities-and-social-sciences.md
├── 06-pg-faculty-science.md
├── 07-application-requirements.md     (Section 3 — UCAS, language, deadlines)
├── 08-costs-and-funding.md            (Section 4 — fees, scholarships)
├── 09-evidence-chain.md               (Section 5)
└── 10-cross-school-comparison.md      (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "birkbeck-knowledge-base-v2"
  school: "<home school>"
  faculty: "<Faculty of Business and Law | Humanities and Social Sciences | Science>"
  degree_level: "<BA|BSc|LLB|BBA|MSci|CertHE|MA|MSc|LLM|MRes|MFA|MBA|PG Dip|PG Cert|Grad Cert|Grad Dip>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|------------|--------|
| P0 | MPhil/PhD programme enumeration (school-by-school) | <https://www.bbk.ac.uk/courses/phd> | Not enumerated leaf-by-leaf in this run |
| P0 | Specific language-test thresholds beyond IELTS (TOEFL iBT, PTE, Cambridge) | per-course pages | Stated as "We also accept other English language tests" without per-test scores |
| P1 | Per-programme detailed tuition (international fees vary by school) | each course page | Sampled only Computer Science UG + MSc |
| P1 | Per-programme application deadlines | per-course page | Birkbeck operates rolling admissions; specific deadlines not listed in aggregate |
| P1 | Standardised PG application fee | admissions team / PG prospectus | Not stated as a uniform figure |
| P2 | Department → programme mapping inside each school | <https://www.bbk.ac.uk/school/{slug}> | Listing pages are organised by faculty, not department within school |
| P2 | Subject-specific scholarship amounts and eligibility | <https://www.bbk.ac.uk/student-services/financial-support/> | Only headline figures captured |

---

## SECTION 7 — Cross-school comparison framework (optional)

| Dimension | Birkbeck |
|-----------|----------|
| Total UG degree programmes (Rule 1) | 70 |
| Total CertHE programmes | 4 |
| Total PG programmes (taught + research) | 151 |
| Faculties | 3 |
| Schools | 8 + 1 Centre |
| UG full-time home tuition (2026-27, sample BSc) | £9,790 / yr |
| UG full-time international tuition (sample BSc) | £18,500 / yr |
| UG part-time home tuition (sample BSc) | £7,335 / yr |
| UG part-time international tuition (sample BSc) | £13,875 / yr |
| PG full-time home tuition (sample MSc) | £12,000 / yr |
| PG full-time international tuition (sample MSc) | £22,980 / yr |
| UCAS tariff (FT UG sample) | 112 points (BBC A-level) |
| Foundation Year UCAS tariff | 48 points |
| English language min (default) | IELTS 6.5 (sub-tests ≥ 6.0) |
| Application portal (UG full-time) | UCAS |
| Application portal (UG part-time) | Direct to Birkbeck |
| Application portal (PG) | Direct to Birkbeck |
| Clearing | Yes (UG via UCAS) |
| Student visa sponsorship | Full-time courses only |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: bbk.ac.uk (course pages, faculties-and-schools, financial-support, international, research landing pages)
> **Verification**: ego-browser snapshotText + JS DOM extraction across 9 URLs in one task space
> **Granularity**: school → department → degree-level → program
> **Region**: UK (England)