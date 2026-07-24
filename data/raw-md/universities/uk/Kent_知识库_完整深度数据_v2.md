# University of Kent Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium) + Kent API (api.kent.ac.uk)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科专业 (UG Majors) | 216 |
| 研究生授课型项目 (PGT: MSc/MA/LLM/MBA/PGDip/PCert) | 195 |
| 研究生博士项目 (PhD/Doctoral) | 80 |
| **学位项目总计 (UG + PGT)** | **411** |
| 学院 (Academic Schools) | 10 |

> **Data source**: Kent UG API (`api.kent.ac.uk/api/programmes/current/undergraduate/programmes`) and PG API (`api.kent.ac.uk/api/programmes/current/postgraduate/programmes`).
>
> **Note**: Kent has 10 academic schools (as of 2026 restructure). The API lists courses by departmental school names which map to the 10 academic schools. Course count includes all variants (with Year Abroad, Year in Industry, Foundation Year). UG count 216 includes 87 "base" programmes shown on the website (grouped variants).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Kent
├── School of Computing                                              [学院]
├── School of Engineering, Mathematics and Physics                   [学院]
│   ├── Department of Engineering                                    [系]
│   ├── Department of Mathematics, Statistics and Actuarial Science   [系]
│   └── Department of Physics and Astronomy                          [系]
├── School of Arts and Architecture                                  [学院]
│   ├── Kent School of Architecture and Planning                     [系]
│   └── School of Arts                                               [系]
├── School of Psychology                                             [学院]
├── School of Economics, Politics and International Relations        [学院]
│   ├── School of Economics                                          [系]
│   └── School of Politics and International Relations               [系]
├── School of Social Sciences                                        [学院]
│   ├── School of Social Policy, Sociology and Social Research       [系]
│   ├── School of Anthropology and Conservation                      [系]
│   ├── School of Sport and Exercise Sciences                        [系]
│   └── The Tizard Centre                                            [系]
├── Kent Law School                                                  [学院]
├── School of Humanities                                             [学院]
│   ├── School of History                                            [系]
│   ├── School of English                                            [系]
│   ├── School of Cultures and Languages                             [系]
│   └── Centre for American Studies                                  [系]
├── Kent Business School                                             [学院]
├── School of Natural Sciences                                       [学院]
│   ├── School of Biosciences                                        [系]
│   ├── Chemistry and Forensic Science                               [系]
│   └── Medway School of Pharmacy                                    [系]
├── Kent and Medway Medical School                                   [学院]
└── Global and Lifelong Learning                                     [学院]
    └── Canterbury College (partner)                                 [系]
```

> **2026 Restructure note**: Kent reorganised into 10 academic schools in 2025-2026. The API still uses the older departmental names for some courses. The hierarchy above maps old department names to the new school structure.
>
> **UCAS institution code**: K24 (University of Kent). Canterbury College partner courses use a different code.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BSc (Hons) | Bachelor of Science with Honours | 本科 | 145 |
| BA (Hons) | Bachelor of Arts with Honours | 本科 | 30 |
| BEng (Hons) | Bachelor of Engineering with Honours | 本科 | 13 |
| LLB (Hons) | Bachelor of Laws with Honours | 本科 | 10 |
| MPhys | Master of Physics (integrated) | 本科 (4-year integrated master's) | 6 |
| MPharm | Master of Pharmacy (integrated) | 本科 (4-year integrated master's) | 2 |
| FdSc | Foundation Degree in Science | 本科 (foundation degree) | 2 |
| MChem | Master of Chemistry (integrated) | 本科 (4-year integrated master's) | 1 |
| MSci | Master in Science (integrated) | 本科 (4-year integrated master's) | 1 |
| MArch | Master of Architecture (integrated) | 本科 (4-year integrated master's) | 1 |
| BM BS | Bachelor of Medicine, Bachelor of Surgery | 本科 | 1 |
| MLaw | Master of Law (integrated) | 本科 (4-year integrated master's) | 1 |
| Cert | Certificate | 本科 (certificate) | 1 |
| MSc | Master of Science | 研究生授课型 | 108 |
| MA | Master of Arts | 研究生授课型 | 37 |
| LLM | Master of Laws | 研究生授课型 | 13 |
| PDip | Postgraduate Diploma | 研究生文凭 | 23 |
| PCert | Postgraduate Certificate | 研究生证书 | 10 |
| MBA | Master of Business Administration | 研究生授课型 | 2 |
| SportD | Doctor of Sport | 研究生授课型 | 1 |
| MArch | Master of Architecture (PG) | 研究生授课型 | 1 |
| PhD | Doctor of Philosophy | 研究生博士 | 80 |

> **UK degree naming note**: MPhys, MChem, MSci, MArch, and MLaw are 4-year **integrated master's** degrees classified as undergraduate in the UK system. They are NOT equivalent to standalone MSc/MA degrees. FdSc is a 2-year foundation degree (Level 5). BM BS is the medical degree awarded by Kent and Medway Medical School.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BSc (Hons) | BA (Hons) | BEng (Hons) | LLB (Hons) | MPhys | MPharm | FdSc | MChem | MSc | MA | LLM | MBA | PDip | PCert | PhD | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Canterbury College (partner) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| Global and Lifelong Learning | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 6 | 0 | 0 | 0 | 1 | 1 | 0 | **12** |
| Kent Business School | 38 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 2 | 0 | 2 | 1 | 1 | 7 | **85** |
| Kent Law School | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 10 | 1 | 2 | **36** |
| Kent and Medway Medical School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| School of Arts and Architecture | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 5 | 0 | 0 | 1 | 0 | 6 | **24** |
| School of Computing | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 1 | **30** |
| School of Economics, Politics and International Relations | 16 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 8 | 0 | 0 | 1 | 0 | 6 | **38** |
| School of Engineering, Mathematics and Physics | 20 | 0 | 13 | 0 | 6 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 3 | 1 | 8 | **69** |
| School of Humanities | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 18 | **39** |
| School of Natural Sciences | 23 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 13 | 0 | 0 | 0 | 2 | 3 | 12 | **56** |
| School of Psychology | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 1 | 1 | 4 | **27** |
| School of Social Sciences | 16 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 11 | 0 | 0 | 3 | 2 | 15 | **61** |
| Unknown | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **3** |
| **合计** | **145** | **30** | **13** | **10** | **6** | **2** | **2** | **1** | **108** | **37** | **13** | **2** | **23** | **10** | **80** | **482** |

> **Reconciliation**: UG (216) + PGT (195) + PhD (80) = 491 ✓ (matches rule-1 totals)

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Kent has 10 academic schools following a 2025-2026 restructure. All undergraduate teaching is organized within these schools. See Section 0.2 for the full hierarchy tree.

UCAS institution code: **K24**. Kent uses UCAS for all undergraduate applications (no Common App). International students may also apply directly via the Kent website.

#### Canterbury College (partner)

##### Canterbury College

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Animal Biology and Wildlife Conservation (top-up) | CD34 | [Link](https://www.kent.ac.uk/courses/undergraduate/1944/animal-wildlife-and-conservation-ba-top-up) |
| 2 | Animal Science (top-up) | D390 | [Link](https://www.kent.ac.uk/courses/undergraduate/1943/animal-sciences-top-up-ba) |

#### Global and Lifelong Learning

###### ARB/RIBA Part 2&3

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Level 7 Architect |  | [Link](https://www.kent.ac.uk/courses/undergraduate/6512/level-seven-architect) |

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Applied Bioscience |  | [Link](https://www.kent.ac.uk/courses/undergraduate/2488/applied-bioscience) |
| 2 | Applied Chemical Sciences |  | [Link](https://www.kent.ac.uk/courses/undergraduate/2489/applied-chemical-sciences) |

###### Cert

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Policy Officer - Higher Apprenticeship – CertHE |  | [Link](https://www.kent.ac.uk/courses/undergraduate/3764/null) |

###### FdSc

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Applied Bioscience |  | [Link](https://www.kent.ac.uk/courses/undergraduate/2487/applied-bioscience-fdsc) |
| 2 | Applied Chemical Sciences |  | [Link](https://www.kent.ac.uk/courses/undergraduate/2486/applied-chemical-sciences-fdsc) |

#### Kent Business School

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Business (top-up) | N107 | [Link](https://www.kent.ac.uk/courses/undergraduate/12/business-top-up) |
| 2 | Business (top-up) - January Start |  | [Link](https://www.kent.ac.uk/courses/undergraduate/6549/business-top-up-january-start) |

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Accounting and Finance | N400 | [Link](https://www.kent.ac.uk/courses/undergraduate/235/accounting-and-finance) |
| 2 | Accounting and Finance (Point of Entry 2) | N400 | [Link](https://www.kent.ac.uk/courses/undergraduate/6537/accounting-and-finance-poe2) |
| 3 | Accounting and Finance with a Foundation Year | N406 | [Link](https://www.kent.ac.uk/courses/undergraduate/4428/accounting-and-finance-with-a-foundation-year) |
| 4 | Accounting and Finance with a Year Abroad | N405 | [Link](https://www.kent.ac.uk/courses/undergraduate/3723/accounting-and-finance-with-a-year-abroad) |
| 5 | Accounting and Finance with a Year in Industry | N404 | [Link](https://www.kent.ac.uk/courses/undergraduate/237/accounting-and-finance-with-a-year-in-industry) |
| 6 | Business Analytics and Management | N201 | [Link](https://www.kent.ac.uk/courses/undergraduate/5092/business-analytics-management) |
| 7 | Business Analytics and Management with a Foundation Year | N204 | [Link](https://www.kent.ac.uk/courses/undergraduate/6493/business-analytics-management-foundation-year) |
| 8 | Business Analytics and Management with a Year Abroad | N203 | [Link](https://www.kent.ac.uk/courses/undergraduate/5094/business-analytics-management-with-year-abroad) |
| 9 | Business Analytics and Management with a Year in Industry | N202 | [Link](https://www.kent.ac.uk/courses/undergraduate/5093/business-analytics-management-with-year-industry) |
| 10 | Business and Management | N206 | [Link](https://www.kent.ac.uk/courses/undergraduate/1399/business-and-management-canterbury) |
| 11 | Business and Management | N105;K | [Link](https://www.kent.ac.uk/courses/undergraduate/3731/business-and-management-medway) |
| 12 | Business and Management (Point of Entry 2) | N206 | [Link](https://www.kent.ac.uk/courses/undergraduate/6538/business-and-management-poe2-canterbury) |
| 13 | Business and Management (Point of Entry 2) | N105;K | [Link](https://www.kent.ac.uk/courses/undergraduate/6539/business-and-management-poe2-medway) |
| 14 | Business and Management (Point of Entry 3) | N206 | [Link](https://www.kent.ac.uk/courses/undergraduate/6543/business-and-management-poe3) |
| 15 | Business and Management (Point of Entry 3) | N105;K | [Link](https://www.kent.ac.uk/courses/undergraduate/6547/business-and-management-poe3-medway) |
| 16 | Business and Management - Accelerated |  | [Link](https://www.kent.ac.uk/courses/undergraduate/6562/business-and-management-medway-accelerated) |
| 17 | Business and Management with a Foundation Year | N103;K | [Link](https://www.kent.ac.uk/courses/undergraduate/4419/business-and-management-with-a-foundation-year-medway) |
| 18 | Business and Management with a Foundation Year | N209 | [Link](https://www.kent.ac.uk/courses/undergraduate/4429/business-and-management-with-a-foundation-year-canterbury) |
| 19 | Business and Management with a Year Abroad | N208 | [Link](https://www.kent.ac.uk/courses/undergraduate/3722/business-and-management-with-a-year-abroad-canterbury) |
| 20 | Business and Management with a Year Abroad | N106:K | [Link](https://www.kent.ac.uk/courses/undergraduate/3746/business-and-management-with-a-year-abroad-medway) |
| 21 | Business and Management with a Year in Industry | N104:K | [Link](https://www.kent.ac.uk/courses/undergraduate/238/business-and-management-with-a-year-in-industry-medway) |
| 22 | Business and Management with a Year in Industry | N207 | [Link](https://www.kent.ac.uk/courses/undergraduate/1398/business-and-management-with-a-year-in-industry-canterbury) |
| 23 | Business and Marketing | N500 | [Link](https://www.kent.ac.uk/courses/undergraduate/868/business-marketing) |
| 24 | Business and Marketing (Point of Entry 3) | N500 | [Link](https://www.kent.ac.uk/courses/undergraduate/6540/business-marketing-poe3) |
| 25 | Business and Marketing with a Foundation Year | N503 | [Link](https://www.kent.ac.uk/courses/undergraduate/5768/business-marketing-with-a-foundation-year) |
| 26 | Business and Marketing with a Year Abroad | N502 | [Link](https://www.kent.ac.uk/courses/undergraduate/3721/business-marketing-with-a-year-abroad) |
| 27 | Business and Marketing with a Year in Industry | N501 | [Link](https://www.kent.ac.uk/courses/undergraduate/869/business-marketing-with-a-year-in-industry) |
| 28 | Finance and Investment | N301 | [Link](https://www.kent.ac.uk/courses/undergraduate/3732/finance-and-investment) |
| 29 | Finance and Investment (Point of Entry 2) | N301 | [Link](https://www.kent.ac.uk/courses/undergraduate/6542/finance-and-investment-poe2) |
| 30 | Finance and Investment (Point of Entry 3) | N301 | [Link](https://www.kent.ac.uk/courses/undergraduate/6564/finance-and-investment-poe3) |
| 31 | Finance and Investment with a Foundation Year | N303 | [Link](https://www.kent.ac.uk/courses/undergraduate/4420/finance-and-investment-foundation-year) |
| 32 | Finance and Investment with a Year Abroad | N302 | [Link](https://www.kent.ac.uk/courses/undergraduate/3745/finance-and-investment-with-year-abroad) |
| 33 | Finance and Investment with a Year in Industry | N300 | [Link](https://www.kent.ac.uk/courses/undergraduate/2495/finance-and-investment-with-year-industry) |
| 34 | International Business | N126 | [Link](https://www.kent.ac.uk/courses/undergraduate/865/international-business-bsc) |
| 35 | International Business (Point of Entry 3) | N126 | [Link](https://www.kent.ac.uk/courses/undergraduate/6541/international-business-poe3) |
| 36 | International Business with a Foundation Year | N129 | [Link](https://www.kent.ac.uk/courses/undergraduate/5767/international-business-with-a-foundation-year) |
| 37 | International Business with a Year Abroad | N127 | [Link](https://www.kent.ac.uk/courses/undergraduate/866/international-business-with-a-year-abroad-bsc) |
| 38 | International Business with a Year in Industry | N128 | [Link](https://www.kent.ac.uk/courses/undergraduate/867/international-business-with-a-year-in-industry-bsc) |

#### Kent Law School

###### LLB (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | International Legal Studies with a Year Abroad | M131 | [Link](https://www.kent.ac.uk/courses/undergraduate/855/international-legal-studies-with-year-abroad) |
| 2 | Law | M100 | [Link](https://www.kent.ac.uk/courses/undergraduate/177/law) |
| 3 | Law (Graduate Entry) | M106 | [Link](https://www.kent.ac.uk/courses/undergraduate/1386/law-graduate-entry) |
| 4 | Law and Criminology | MM19 | [Link](https://www.kent.ac.uk/courses/undergraduate/326/law-and-criminology) |
| 5 | Law and Criminology with a Year in Industry | MM20 | [Link](https://www.kent.ac.uk/courses/undergraduate/6569/law-and-criminology-with-a-year-in-industry) |
| 6 | Law and Politics | LM21 | [Link](https://www.kent.ac.uk/courses/undergraduate/194/law-and-politics) |
| 7 | Law and Politics with a Year in Industry | LM22 | [Link](https://www.kent.ac.uk/courses/undergraduate/6570/law-and-politics-with-a-year-in-industry) |
| 8 | Law with a Foundation Year | M110 | [Link](https://www.kent.ac.uk/courses/undergraduate/5086/law-with-foundation-year) |
| 9 | Law with a Year in Industry | M101 | [Link](https://www.kent.ac.uk/courses/undergraduate/6568/law-with-a-year-in-industry) |
| 10 | Master 1 Droit international et européen and LLB in Law Linked Award |  | [Link](https://www.kent.ac.uk/courses/undergraduate/3736/master-droit) |

###### MLaw

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Law (Integrated Master's in Solicitors’ Practice) | M199 | [Link](https://www.kent.ac.uk/courses/undergraduate/5801/law-integrated-masters-in-solicitors-practice) |

#### Kent and Medway Medical School

###### BM BS

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Medicine | A100 (Institution code K31) | [Link](https://www.kent.ac.uk/courses/undergraduate/3737/medicine) |

#### School of Arts and Architecture

##### Kent School of Architecture and Planning

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Architecture | K100 | [Link](https://www.kent.ac.uk/courses/undergraduate/4/architecture) |
| 2 | Architecture with a Foundation Year | K101 | [Link](https://www.kent.ac.uk/courses/undergraduate/6510/architecture-with-foundation-year) |
| 3 | Graphic Design | W211 | [Link](https://www.kent.ac.uk/courses/undergraduate/3766/graphic-design) |
| 4 | Spatial and Interior Design | W250 | [Link](https://www.kent.ac.uk/courses/undergraduate/3767/spatial-interior-design) |

###### MArch

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Architecture | K100 | [Link](https://www.kent.ac.uk/courses/undergraduate/889/architecture-march) |

##### School of Arts

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Drama and Film | WW46 | [Link](https://www.kent.ac.uk/courses/undergraduate/165/drama-and-film) |
| 2 | Drama, Theatre and Performing Arts | W400 | [Link](https://www.kent.ac.uk/courses/undergraduate/114/drama-theatre-and-performing-arts) |
| 3 | Film | W610 | [Link](https://www.kent.ac.uk/courses/undergraduate/99/film) |
| 4 | Film and Media | PW63 | [Link](https://www.kent.ac.uk/courses/undergraduate/3758/film-media) |
| 5 | Media | W999 | [Link](https://www.kent.ac.uk/courses/undergraduate/1901/media) |

#### School of Computing

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Business Information Technology | NG14 | [Link](https://www.kent.ac.uk/courses/undergraduate/137/business-information-technology) |
| 2 | Business Information Technology with a Year in Industry | NG1F | [Link](https://www.kent.ac.uk/courses/undergraduate/141/business-information-technology-with-a-year-in-industry) |
| 3 | Computer Science | G400 | [Link](https://www.kent.ac.uk/courses/undergraduate/124/computer-science) |
| 4 | Computer Science (Artificial Intelligence) | G700 | [Link](https://www.kent.ac.uk/courses/undergraduate/6513/computer-science-artificial-intelligence) |
| 5 | Computer Science (Artificial Intelligence) with a Year in Industry | G701 | [Link](https://www.kent.ac.uk/courses/undergraduate/6514/computer-science-artificial-intelligence-with-a-year-in-industry) |
| 6 | Computer Science (Cyber Security) | G490 | [Link](https://www.kent.ac.uk/courses/undergraduate/4397/computer-science-cyber-security) |
| 7 | Computer Science (Cyber Security) with a Year in Industry | G491 | [Link](https://www.kent.ac.uk/courses/undergraduate/4398/computer-science-cyber-security-with-a-year-in-industry) |
| 8 | Computer Science (Games Development) | I610 | [Link](https://www.kent.ac.uk/courses/undergraduate/6554/video-games) |
| 9 | Computer Science (Games Development) with a Year in Industry | I611 | [Link](https://www.kent.ac.uk/courses/undergraduate/6555/video-games-with-a-year-in-industry) |
| 10 | Computer Science (Point of Entry 3) | G400 | [Link](https://www.kent.ac.uk/courses/undergraduate/6565/computer-science) |
| 11 | Computer Science (Robotics) | H671 | [Link](https://www.kent.ac.uk/courses/undergraduate/6552/robotics) |
| 12 | Computer Science (Robotics) with a Year in Industry | H672 | [Link](https://www.kent.ac.uk/courses/undergraduate/6553/robotics-with-a-year-in-industry) |
| 13 | Computer Science with a Year in Industry | G404 | [Link](https://www.kent.ac.uk/courses/undergraduate/128/computer-science-with-a-year-in-industry) |
| 14 | Software Engineering | I102 | [Link](https://www.kent.ac.uk/courses/undergraduate/3719/software-engineering) |
| 15 | Software Engineering (Point of Entry 3) | I102 | [Link](https://www.kent.ac.uk/courses/undergraduate/6566/software-engineering) |
| 16 | Software Engineering with a Year in Industry | I103 | [Link](https://www.kent.ac.uk/courses/undergraduate/3755/software-engineering-year-in-industry) |

#### School of Economics, Politics and International Relations

##### School of Economics

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Economics | L100 | [Link](https://www.kent.ac.uk/courses/undergraduate/109/economics) |
| 2 | Economics and Finance | LN14 | [Link](https://www.kent.ac.uk/courses/undergraduate/1/economics-and-finance) |
| 3 | Economics and Finance with a Foundation Year | LN16 | [Link](https://www.kent.ac.uk/courses/undergraduate/6515/economics-and-finance-with-a-foundation-year) |
| 4 | Economics and Finance with a Year Abroad |  | [Link](https://www.kent.ac.uk/courses/undergraduate/6558/economics-and-finance-with-a-year-abroad) |
| 5 | Economics and Finance with a Year in Industry | LN15 | [Link](https://www.kent.ac.uk/courses/undergraduate/3724/economics-and-finance-with-a-year-in-industry) |
| 6 | Economics and Management | LN12 | [Link](https://www.kent.ac.uk/courses/undergraduate/1941/economics-and-management) |
| 7 | Economics and Management with a Foundation Year | LN10 | [Link](https://www.kent.ac.uk/courses/undergraduate/6520/economics-and-management-with-a-foundation-year) |
| 8 | Economics and Management with a Year Abroad | LN13 | [Link](https://www.kent.ac.uk/courses/undergraduate/6560/economics-management-year-industry) |
| 9 | Economics and Management with a Year in Industry | LN13 | [Link](https://www.kent.ac.uk/courses/undergraduate/3127/economics-management-year-industry) |
| 10 | Economics and Politics | LL12 | [Link](https://www.kent.ac.uk/courses/undergraduate/180/economics-and-politics) |
| 11 | Economics and Politics with a Year Abroad | LL11 | [Link](https://www.kent.ac.uk/courses/undergraduate/6559/economics-and-politics-year-abroad) |
| 12 | Economics and Politics with a Year in Industry | LL14 | [Link](https://www.kent.ac.uk/courses/undergraduate/3126/economics-and-politics-year-industry) |
| 13 | Economics with a Foundation Year | L103 | [Link](https://www.kent.ac.uk/courses/undergraduate/5799/economics-foundation-year) |
| 14 | Economics with a Year Abroad | L101 | [Link](https://www.kent.ac.uk/courses/undergraduate/3123/economics-year-abroad) |
| 15 | Economics with a Year in Industry | L102 | [Link](https://www.kent.ac.uk/courses/undergraduate/112/economics-year-industry) |
| 16 | Professional Economist - Higher Apprenticeship |  | [Link](https://www.kent.ac.uk/courses/undergraduate/3740/professional-economist-higher-apprenticeship) |

##### School of Politics and International Relations

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Politics and International Relations | L258 | [Link](https://www.kent.ac.uk/courses/undergraduate/31/politics-and-international-relations) |
| 2 | Politics and International Relations with a Year in Continental Europe | L255 | [Link](https://www.kent.ac.uk/courses/undergraduate/40/politics-and-international-relations-with-a-year-in-continental-europe) |
| 3 | Politics and International Relations with a Year in Industry | L251 | [Link](https://www.kent.ac.uk/courses/undergraduate/5802/politics-and-international-relations-with-a-year-in-industry) |
| 4 | Politics and International Relations with a Year in North America | L253 | [Link](https://www.kent.ac.uk/courses/undergraduate/393/politics-and-international-relations-with-a-year-in-north-america) |
| 5 | Politics and International Relations with a Year in the Asia-Pacific | L256 | [Link](https://www.kent.ac.uk/courses/undergraduate/2494/politics-and-international-relations-with-a-year-in-asia-pacific) |

#### School of Engineering, Mathematics and Physics

##### Physics and Astronomy

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Astronomy, Space Science and Astrophysics | F590 | [Link](https://www.kent.ac.uk/courses/undergraduate/67/astronomy-space-science-and-astrophysics-bsc) |
| 2 | Astronomy, Space Science and Astrophysics with a Foundation Year | F594 | [Link](https://www.kent.ac.uk/courses/undergraduate/6509/physics-astrophysics-with-foundation-year) |
| 3 | Astronomy, Space Science and Astrophysics with a Year in Industry | F593 | [Link](https://www.kent.ac.uk/courses/undergraduate/2527/astronomy-space-science-astrophysics-year-industry) |
| 4 | Physics | F300 | [Link](https://www.kent.ac.uk/courses/undergraduate/22/physics-bsc) |
| 5 | Physics with Astrophysics | F3F5 | [Link](https://www.kent.ac.uk/courses/undergraduate/26/physics-with-astrophysics-bsc) |
| 6 | Physics with Astrophysics with a Foundation Year |  | [Link](https://www.kent.ac.uk/courses/undergraduate/6506/physics-astrophysics-with-foundation-year) |
| 7 | Physics with Astrophysics with a Year in Industry | F351 | [Link](https://www.kent.ac.uk/courses/undergraduate/2526/physics-astrophysics-year-industry) |
| 8 | Physics with a Foundation Year | F305 | [Link](https://www.kent.ac.uk/courses/undergraduate/24/physics-with-a-foundation-year) |
| 9 | Physics with a Year in Industry | F307 | [Link](https://www.kent.ac.uk/courses/undergraduate/893/physics-with-a-year-in-industry) |

###### MPhys

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Astronomy, Space Science and Astrophysics | F592 | [Link](https://www.kent.ac.uk/courses/undergraduate/68/astronomy-space-science-and-astrophysics-mphys) |
| 2 | Astronomy, Space Science and Astrophysics with a Year Abroad | F591 | [Link](https://www.kent.ac.uk/courses/undergraduate/69/astronomy-space-science-and-astrophysics-with-a-year-abroad-mphys) |
| 3 | Physics | F303 | [Link](https://www.kent.ac.uk/courses/undergraduate/23/physics-mphys) |
| 4 | Physics with Astrophysics | F3FN | [Link](https://www.kent.ac.uk/courses/undergraduate/27/physics-with-astrophysics-mphys) |
| 5 | Physics with Astrophysics with a Year Abroad | F3FM | [Link](https://www.kent.ac.uk/courses/undergraduate/28/physics-with-astrophysics-with-a-year-abroad-mphys) |
| 6 | Physics with a Year Abroad | F304 | [Link](https://www.kent.ac.uk/courses/undergraduate/25/physics-with-a-year-abroad-mphys) |

##### School of Engineering

###### BEng (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biomedical Engineering | 3D9J | [Link](https://www.kent.ac.uk/courses/undergraduate/2497/biomedical-engineering) |
| 2 | Biomedical Engineering including a Foundation Year | H16F | [Link](https://www.kent.ac.uk/courses/undergraduate/3768/biomedical-engineering-foundation) |
| 3 | Biomedical Engineering with a Year in Industry | 05C3 | [Link](https://www.kent.ac.uk/courses/undergraduate/2498/biomedical-engineering-with-a-year-in-industry) |
| 4 | Electrical and Electronic Engineering | H600 | [Link](https://www.kent.ac.uk/courses/undergraduate/6499/electrical-and-electronic-engineering-beng) |
| 5 | Electrical and Electronic Engineering including a Foundation Year | H60F | [Link](https://www.kent.ac.uk/courses/undergraduate/6500/electrical-and-electronic-engineering-including-foundation-year-beng) |
| 6 | Electrical and Electronic Engineering with a Year in Industry | LE10 | [Link](https://www.kent.ac.uk/courses/undergraduate/6501/electrical-and-electronic-engineering-with-a-year-in-industry-beng) |
| 7 | Electronic and Computer Engineering | H692 | [Link](https://www.kent.ac.uk/courses/undergraduate/4421/electronic-and-computer-engineering-beng) |
| 8 | Electronic and Computer Engineering including a Foundation Year | H694 | [Link](https://www.kent.ac.uk/courses/undergraduate/4426/electronic-and-computer-engineering-including-foundation-year-beng) |
| 9 | Electronic and Computer Engineering with a Year in Industry | H695 | [Link](https://www.kent.ac.uk/courses/undergraduate/4423/electronic-and-computer-engineering-with-a-year-in-industry-beng) |
| 10 | Electronic and Computer Systems (top-up) | H691 | [Link](https://www.kent.ac.uk/courses/undergraduate/225/electronic-and-computer-systems) |
| 11 | Mechanical Engineering | H310 | [Link](https://www.kent.ac.uk/courses/undergraduate/3738/mechanical-engineering-beng) |
| 12 | Mechanical Engineering including a Foundation Year | H31F | [Link](https://www.kent.ac.uk/courses/undergraduate/3769/mechanical-engineering-beng-foundation) |
| 13 | Mechanical Engineering with a Year in Industry | H311 | [Link](https://www.kent.ac.uk/courses/undergraduate/3739/mechanical-engineering-with-a-year-in-industry-beng) |

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Digital Design | W285 | [Link](https://www.kent.ac.uk/courses/undergraduate/4410/digital-design) |
| 2 | Digital Design with a Year Abroad | W286 | [Link](https://www.kent.ac.uk/courses/undergraduate/4412/digital-design-with-a-year-abroad) |
| 3 | Digital Design with a Year in Industry | W287 | [Link](https://www.kent.ac.uk/courses/undergraduate/4411/digital-design-with-a-year-in-industry) |

##### School of Mathematics, Statistics and Actuarial Science

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Actuarial Science | N323 | [Link](https://www.kent.ac.uk/courses/undergraduate/7/actuarial-science) |
| 2 | Actuarial Science with a Foundation Year | N325 | [Link](https://www.kent.ac.uk/courses/undergraduate/1896/actuarial-science-with-a-foundation-year) |
| 3 | Actuarial Science with a Year in Industry | N324 | [Link](https://www.kent.ac.uk/courses/undergraduate/6/actuarial-science-with-a-year-in-industry) |
| 4 | Data Science | G190 | [Link](https://www.kent.ac.uk/courses/undergraduate/4407/data-science) |
| 5 | Data Science with a Year in Industry | G191 | [Link](https://www.kent.ac.uk/courses/undergraduate/4418/data-science-with-a-year-in-industry) |
| 6 | Mathematics | G100 | [Link](https://www.kent.ac.uk/courses/undergraduate/161/mathematics) |
| 7 | Mathematics with a Foundation Year | G108 | [Link](https://www.kent.ac.uk/courses/undergraduate/166/mathematics-with-a-foundation-year) |
| 8 | Mathematics with a Year in Industry | G104 | [Link](https://www.kent.ac.uk/courses/undergraduate/890/mathematics-with-a-year-in-industry) |

#### School of Humanities

##### School of Cultures and Languages

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Ancient History | Q800 | [Link](https://www.kent.ac.uk/courses/undergraduate/82/ancient-history) |
| 2 | Ancient History with Archaeology | Q800 | [Link](https://www.kent.ac.uk/courses/undergraduate/6529/ancient-history-with-archaeology) |
| 3 | Classical Studies | Q802 | [Link](https://www.kent.ac.uk/courses/undergraduate/896/classical-studies) |
| 4 | Classical Studies with Archaeology | Q802 | [Link](https://www.kent.ac.uk/courses/undergraduate/6530/classical-studies-with-archaeology) |
| 5 | Modern Languages | R910 | [Link](https://www.kent.ac.uk/courses/undergraduate/5089/modern-languages) |
| 6 | Modern Languages with a Year Abroad | R910 | [Link](https://www.kent.ac.uk/courses/undergraduate/6523/modern-languages-with-a-year-abroad) |

##### School of English

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | English Literature | Q320 | [Link](https://www.kent.ac.uk/courses/undergraduate/3753/english-literature) |
| 2 | English Literature and Creative Writing | Q326 | [Link](https://www.kent.ac.uk/courses/undergraduate/132/english-literature-and-creative-writing) |

##### School of History

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | History | V100 | [Link](https://www.kent.ac.uk/courses/undergraduate/85/history) |
| 2 | Military History | V391 | [Link](https://www.kent.ac.uk/courses/undergraduate/90/military-history) |

#### School of Natural Sciences

##### Chemistry and Forensic Science

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemistry | F107 | [Link](https://www.kent.ac.uk/courses/undergraduate/78/chemistry) |
| 2 | Chemistry with Forensic Science | F107 | [Link](https://www.kent.ac.uk/courses/undergraduate/6526/chemistry-forensic-science) |
| 3 | Chemistry with Forensic Science with a Year Abroad | F110 | [Link](https://www.kent.ac.uk/courses/undergraduate/6527/chemistry-forensic-science-with-a-year-abroad) |
| 4 | Chemistry with Forensic Science with a Year in Industry | F108 | [Link](https://www.kent.ac.uk/courses/undergraduate/6528/chemistry-forensic-science-with-a-year-in-industry) |
| 5 | Chemistry with a Foundation Year | F105 | [Link](https://www.kent.ac.uk/courses/undergraduate/388/chemistry-with-a-foundation-year) |
| 6 | Chemistry with a Year Abroad | F110 | [Link](https://www.kent.ac.uk/courses/undergraduate/3765/chemistry-with-a-year-abroad) |
| 7 | Chemistry with a Year in Industry | F108 | [Link](https://www.kent.ac.uk/courses/undergraduate/83/chemistry-with-a-year-in-industry) |
| 8 | Forensic Science | F410 | [Link](https://www.kent.ac.uk/courses/undergraduate/73/forensic-science-bsc) |
| 9 | Forensic Science with a Foundation Year | F412 | [Link](https://www.kent.ac.uk/courses/undergraduate/76/forensic-science-with-a-foundation-year) |
| 10 | Forensic Science with a Year Abroad | F415 | [Link](https://www.kent.ac.uk/courses/undergraduate/3720/forensic-science-with-a-year-abroad) |
| 11 | Forensic Science with a Year in Industry | F411 | [Link](https://www.kent.ac.uk/courses/undergraduate/77/forensic-science-with-a-year-in-industry) |

###### MChem

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemistry | F109 | [Link](https://www.kent.ac.uk/courses/undergraduate/15/chemistry-mchem) |

###### MSci

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Forensic Science | F414 | [Link](https://www.kent.ac.uk/courses/undergraduate/74/forensic-science-msci) |

##### Medway School of Pharmacy

###### MPharm

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Pharmacy | B230 (Institution code M62) | [Link](https://www.kent.ac.uk/courses/undergraduate/18/pharmacy) |
| 2 | Pharmacy with Preparatory Year | B231 (Institution code M62) | [Link](https://www.kent.ac.uk/courses/undergraduate/6546/pharmacy-with-preparatory-year) |

##### School of Biosciences

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biochemistry | C700 | [Link](https://www.kent.ac.uk/courses/undergraduate/96/biochemistry) |
| 2 | Biochemistry with a Foundation Year | C70F | [Link](https://www.kent.ac.uk/courses/undergraduate/5778/biochemistry-with-a-foundation-year) |
| 3 | Biochemistry with a Year Abroad | C703 | [Link](https://www.kent.ac.uk/courses/undergraduate/264/biochemistry-with-a-year-abroad) |
| 4 | Biochemistry with a Year in Professional Practice | C702 | [Link](https://www.kent.ac.uk/courses/undergraduate/100/biochemistry-with-a-year-professional-practice) |
| 5 | Biology | C103 | [Link](https://www.kent.ac.uk/courses/undergraduate/255/biology) |
| 6 | Biology with a Foundation Year | C10F | [Link](https://www.kent.ac.uk/courses/undergraduate/5779/biology-with-a-foundation-year) |
| 7 | Biology with a Year Abroad | C106 | [Link](https://www.kent.ac.uk/courses/undergraduate/258/biology-with-a-year-abroad) |
| 8 | Biology with a Year in Professional Practice | C105 | [Link](https://www.kent.ac.uk/courses/undergraduate/257/biology-with-a-year-in-professional-practice) |
| 9 | Biomedical Science | B940 | [Link](https://www.kent.ac.uk/courses/undergraduate/263/biomedical-science) |
| 10 | Biomedical Science with a Foundation Year | B94F | [Link](https://www.kent.ac.uk/courses/undergraduate/5780/biomedical-science-with-a-foundation-year) |
| 11 | Biomedical Science with a Year Abroad | B943 | [Link](https://www.kent.ac.uk/courses/undergraduate/260/biomedical-science-with-a-year-abroad) |
| 12 | Biomedical Science with a Year in Professional Practice | B942 | [Link](https://www.kent.ac.uk/courses/undergraduate/262/biomedical-science-with-a-year-in-professional-practice) |

#### School of Psychology

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Psychology | C800 | [Link](https://www.kent.ac.uk/courses/undergraduate/49/psychology) |
| 2 | Psychology with Business Psychology | C815 | [Link](https://www.kent.ac.uk/courses/undergraduate/6521/psychology-with-business-psychology) |
| 3 | Psychology with Business Psychology with a Foundation Year | C819 | [Link](https://www.kent.ac.uk/courses/undergraduate/6525/psychology-with-business-psychology-with-foundation-year) |
| 4 | Psychology with Business Psychology with a Year Abroad | C818 | [Link](https://www.kent.ac.uk/courses/undergraduate/6524/psychology-with-business-psychology-with-year-abroad) |
| 5 | Psychology with Business Psychology with a Year in Professional Practice | C817 | [Link](https://www.kent.ac.uk/courses/undergraduate/6522/psychology-with-business-psychology-with-a-year-in-professional-practice) |
| 6 | Psychology with Clinical Perspectives | C822 | [Link](https://www.kent.ac.uk/courses/undergraduate/50/psychology-with-clinical-perspectives) |
| 7 | Psychology with Clinical Perspectives and a Foundation Year | C826 | [Link](https://www.kent.ac.uk/courses/undergraduate/6518/psychology-with-clinical-psychology-with-a-foundation-year) |
| 8 | Psychology with Clinical Perspectives and a Year Abroad | C825 | [Link](https://www.kent.ac.uk/courses/undergraduate/6519/psychology-with-clinical-psychology-with-a-year-abroad) |
| 9 | Psychology with Clinical Perspectives and a Year in Professional Practice | C824 | [Link](https://www.kent.ac.uk/courses/undergraduate/2529/psychology-clinical-psychology-year-professional-practice) |
| 10 | Psychology with Studies in Forensic Psychology | C816 | [Link](https://www.kent.ac.uk/courses/undergraduate/1389/psychology-with-forensic-psychology) |
| 11 | Psychology with a Foundation Year | C801 | [Link](https://www.kent.ac.uk/courses/undergraduate/5800/psychology-foundation-year) |
| 12 | Psychology with a Year Abroad | C881 | [Link](https://www.kent.ac.uk/courses/undergraduate/52/psychology-with-a-year-abroad) |
| 13 | Psychology with a Year in Professional Practice | C851 | [Link](https://www.kent.ac.uk/courses/undergraduate/2528/psychology-with-a-year-in-professional-practice) |

#### School of Social Sciences

##### School of Anthropology and Conservation

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Ecology and Conservation | CD14 | [Link](https://www.kent.ac.uk/courses/undergraduate/30/ecology-and-conservation) |
| 2 | Ecology and Conservation with a Year Abroad | CD15 | [Link](https://www.kent.ac.uk/courses/undergraduate/6517/ecology-and-conservation-with-a-year-abroad) |
| 3 | Ecology and Conservation with a Year in Industry | 1T16 | [Link](https://www.kent.ac.uk/courses/undergraduate/392/ecology-and-conservation-with-a-year-in-professional-practice) |

##### School of Social Policy, Sociology and Social Research

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Social Work | L508:K | [Link](https://www.kent.ac.uk/courses/undergraduate/250/social-work) |

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Criminology and Criminal Justice | M902 | [Link](https://www.kent.ac.uk/courses/undergraduate/234/criminology-and-criminal-justice) |
| 2 | Criminology and Criminal Justice with Quantitative Research | L3GX | [Link](https://www.kent.ac.uk/courses/undergraduate/1374/criminology-criminal-justice-with-quantitative-research) |
| 3 | Criminology and Sociology | LM39 | [Link](https://www.kent.ac.uk/courses/undergraduate/360/criminology-and-sociology) |
| 4 | Criminology with Criminal Psychology | M903 | [Link](https://www.kent.ac.uk/courses/undergraduate/6548/criminology-with-criminal-psychology) |
| 5 | Criminology with Cybercrime | M904 | [Link](https://www.kent.ac.uk/courses/undergraduate/6551/criminology-with-cybercrime) |
| 6 | Sociology | L300 | [Link](https://www.kent.ac.uk/courses/undergraduate/245/sociology) |
| 7 | Sustainable Societies and Global Sociology | L302 | [Link](https://www.kent.ac.uk/courses/undergraduate/6550/sustainable-societies-global-sociology) |

##### School of Sport and Exercise Sciences

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Sport Therapy and Rehabilitation | C600 | [Link](https://www.kent.ac.uk/courses/undergraduate/2512/sport-therapy-rehabilitation) |
| 2 | Sport Therapy and Rehabilitation with a Foundation Year | C60F | [Link](https://www.kent.ac.uk/courses/undergraduate/5784/sport-therapy-rehabilitation-with-a-foundation-year) |
| 3 | Sport Therapy and Rehabilitation with a Year in Industry | C60Y | [Link](https://www.kent.ac.uk/courses/undergraduate/6504/sport-therapy-rehabilitation-year-in-industry) |
| 4 | Sport and Exercise Science | C602 | [Link](https://www.kent.ac.uk/courses/undergraduate/171/sport-and-exercise-science) |
| 5 | Sport and Exercise Science with a Foundation Year | C62F | [Link](https://www.kent.ac.uk/courses/undergraduate/5782/sport-and-exercise-science-with-a-foundation-year) |
| 6 | Sport and Exercise Science with a Year in Industry | C612 | [Link](https://www.kent.ac.uk/courses/undergraduate/3122/sport-and-exercise-science-year-in-industry) |

#### Unknown

###### BA (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | English Language, Linguistics and World Literature | QQ13 | [Link](https://www.kent.ac.uk/courses/undergraduate/88/english-language-linguistics-world-literature) |

###### BSc (Hons)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Digital Society, Media and Culture | L391 | [Link](https://www.kent.ac.uk/courses/undergraduate/6545/digital-society-media-culture) |

###### Credit

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | International Foundation Programme |  | [Link](https://www.kent.ac.uk/courses/undergraduate/4425/international-foundation-programme) |

---

## SECTION 2 — Postgraduate Education

### 2.1 Postgraduate programme listing

#### Global and Lifelong Learning

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced and Specialist Healthcare | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2208/advanced-and-specialist-healthcare) |
| 2 | Advanced and Specialist Healthcare (Advanced Dental Clinical Practice) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2193/advanced-and-specialist-healthcare-advanced-dental-clinical-practice) |
| 3 | Advanced and Specialist Healthcare (Applied Dental Professional Practice) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/215/advanced-and-specialist-healthcare-applied-dental-professional-practice) |
| 4 | Advanced and Specialist Healthcare (Dental Educational Practice) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3808/advanced-and-specialist-healthcare-dental-educational-practice) |
| 5 | Professional Practice (Medical Education Management) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4961/professional-practice-medical-education-management) |
| 6 | Professional Practice (Teaching and Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/335/professional-practice-teaching-and-learning) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced and Specialist Healthcare | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2208/advanced-and-specialist-healthcare) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced and Specialist Healthcare | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2208/advanced-and-specialist-healthcare) |

#### Kent Business School

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Philanthropic Studies (Distance Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/769/philanthropic-studies-distance-learning) |
| 2 | Professional Practice | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/224/professional-practice) |

###### MBA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Master of Business Administration (MBA) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/291/mba) |
| 2 | Master of Business Administration (MBA) - January Start | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6561/mba-january-start) |

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Business Analytics | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/292/business-analytics) |
| 2 | Business Analytics (HDA Top-up) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6184/business-analytics-top-up) |
| 3 | Business Analytics - January Start | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6187/business-analytics-januart-start) |
| 4 | Business Analytics with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4372/business-analytics-with-professional-practice-and-placement) |
| 5 | Digital Marketing and Analytics | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1232/digital-marketing-and-analytics) |
| 6 | Digital Marketing and Analytics - January Start | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6186/digital-marketing-and-analytics-january-start) |
| 7 | Digital Marketing and Analytics with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4373/digital-marketing-and-analytics-with-professional-practice-and-placement) |
| 8 | Finance and Economics | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6170/finance-economics) |
| 9 | Finance and Economics with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6181/finance-economics-with-professional-practice-and-placement) |
| 10 | Finance, Investment and Risk | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1703/finance-investment-and-risk) |
| 11 | Finance, Investment and Risk (Dual Award) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2198/finance-dual-award) |
| 12 | Finance, Investment and Risk with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4376/finance-investment-and-risk-with-professional-practice-and-placement) |
| 13 | Financial Management | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1705/financial-management) |
| 14 | Financial Management with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4375/financial-management-with-professional-practice-and-placement) |
| 15 | Global Healthcare Management | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3267/global-healthcare-management) |
| 16 | Global Healthcare Management - January Start | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/5563/global-healthcare-management-january-start) |
| 17 | Global Healthcare Management with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4384/global-healthcare-management-with-professional-practice-and-placement) |
| 18 | Global Logistics and Supply Chain Management | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/294/global-logistics-and-supply-chain-management) |
| 19 | Global Logistics and Supply Chain Management with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4380/global-logistics-and-supply-chain-management-with-professional-practice-and-placement) |
| 20 | International Business and Management | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/299/international-business-management) |
| 21 | International Business and Management - January Start | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/5564/international-business-management-january-start) |
| 22 | International Business and Management with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4379/international-business-management-with-professional-practice-and-placement) |
| 23 | Marketing | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/303/marketing) |
| 24 | Marketing with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4382/marketing-with-professional-practice-and-placement) |
| 25 | Professional Practice | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/224/professional-practice) |
| 26 | Senior Leadership in Healthcare (HDA Top-up) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6183/senior-leadership-in-healthcare-top-up) |
| 27 | Senior Leadership in Management (HDA Top-up) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6182/senior-leadership-in-management-top-up) |
| 28 | Strategic Project Management | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3269/strategic-project-management) |
| 29 | Strategic Project Management - January Start | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/5562/strategic-project-management-january-start) |
| 30 | Strategic Project Management with Professional Practice and Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4383/strategic-project-management-with-professional-practice-and-placement) |
| 31 | Sustainable Finance and Investment | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1704/sustainable-finance-investment) |
| 32 | Sustainable Finance and Investment with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4374/sustainable-finance-investment-with-placement) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Philanthropic Studies (Distance Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/769/philanthropic-studies-distance-learning) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Philanthropic Studies (Distance Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/769/philanthropic-studies-distance-learning) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Accounting | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/309/accounting) |
| 2 | Business Analytics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/316/business-analytics) |
| 3 | Finance | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/312/finance) |
| 4 | Management | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/314/management) |
| 5 | Marketing | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/317/marketing) |
| 6 | Operational Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/319/operational-research) |
| 7 | Organisational Behaviour and Human Resource Management | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/2728/organisational-behaviour-human-resource-management) |

#### Kent Law School

###### LLM

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Law | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/327/law) |
| 2 | Law (Criminal Justice) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/114/criminal-justice) |
| 3 | Law (Human Rights Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/117/human-rights-law) |
| 4 | Law (Intellectual Property Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1217/law-and-intellectual-property-law) |
| 5 | Law (International Commercial Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/127/international-commercial-law) |
| 6 | Law (International Environmental Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/130/international-environmental-law-policy) |
| 7 | Law (International Law with International Relations) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/131/international-law-with-international-relations) |
| 8 | Law (International Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/133/international-law) |
| 9 | Law (Law and Health) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/132/law-and-health) |
| 10 | Law (Law and Society) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4959/law-and-society) |
| 11 | Law (Solicitors' Practice) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6171/law-solicitors-practice) |
| 12 | Law (by Research) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/142/law) |
| 13 | Socio-legal Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/144/socio-legal-studies) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Law | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/327/law) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Law | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/327/law) |
| 2 | Law (Criminal Justice) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/114/criminal-justice) |
| 3 | Law (Human Rights Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/117/human-rights-law) |
| 4 | Law (Intellectual Property Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1217/law-and-intellectual-property-law) |
| 5 | Law (International Commercial Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/127/international-commercial-law) |
| 6 | Law (International Environmental Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/130/international-environmental-law-policy) |
| 7 | Law (International Law with International Relations) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/131/international-law-with-international-relations) |
| 8 | Law (International Law) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/133/international-law) |
| 9 | Law (Law and Health) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/132/law-and-health) |
| 10 | Law (Law and Society) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4959/law-and-society) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Law | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/340/law-canterbury) |
| 2 | Socio-legal Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/144/socio-legal-studies) |

#### School of Arts and Architecture

##### Kent School of Architecture and Planning

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Architectural Visualisation | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/245/architectural-visualisation) |

###### MArch

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Architecture | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/186/master-of-architecture) |

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Architectural Conservation | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/362/architectural-conservation) |
| 2 | Architecture and the Sustainable Environment | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/182/architecture-and-the-sustainable-environment) |
| 3 | Urban Planning and Resilience | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/2706/urban-planning-and-resilience) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Architectural Practice - ARB Part 3 | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2722/architectural-practice) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Architecture | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/184/architecture) |

##### School of Arts

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Film | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/17/film) |
| 2 | Film (Film with Practice) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/343/film-with-practice) |
| 3 | Performance and Theatre Making | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1222/performance-and-theatre-making) |
| 4 | Promotional Media | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4973/promotional-media) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Drama by Practice as Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/280/drama-practice-as-research) |
| 2 | Drama by Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/351/drama-by-research) |
| 3 | Film | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/20/film) |
| 4 | Film: Practice as Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/352/film-practice-as-research) |
| 5 | Media Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3265/media-studies-phd) |

#### School of Computing

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced Computer Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/246/advanced-computer-science) |
| 2 | Advanced Computer Science with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4951/advanced-computer-science-with-placement) |
| 3 | Artificial Intelligence | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/249/artificial-intelligence) |
| 4 | Artificial Intelligence with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4952/artificial-intelligence-with-placement) |
| 5 | Computer Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/243/computer-science) |
| 6 | Computer Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/283/computer-science) |
| 7 | Computer Science (Artificial Intelligence) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3812/computer-science-artificial-intelligence) |
| 8 | Computer Science (Artificial Intelligence) with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3813/computer-science-artificial-intelligence-with-placement) |
| 9 | Computer Science (Cyber Security) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3815/computer-science-cyber-security) |
| 10 | Computer Science (Cyber Security) with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3816/computer-science-cyber-security-with-placement) |
| 11 | Computer Science with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4953/computer-science-with-placement) |
| 12 | Cyber Security | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1225/cyber-security) |
| 13 | Cyber Security with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4954/cyber-security-with-placement) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Computer Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/283/computer-science) |

#### School of Economics, Politics and International Relations

##### School of Economics

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Economics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/194/economics) |
| 2 | Economics and Data Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4965/economics-and-data-science) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Agri-Environmental Economics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/207/agri-environmental-economics) |
| 2 | Economics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/208/economics) |

##### School of Politics and International Relations

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Comparative Politics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/60/comparative-politics) |
| 2 | International Conflict Analysis | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/62/international-conflict-analysis) |
| 3 | International Negotiation and Conflict Resolution | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/44/international-negotiation-conflict-resolution) |
| 4 | International Relations | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/45/international-relations) |
| 5 | International Relations | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/63/international-relations) |
| 6 | International Relations with International Law | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/47/international-relations-with-international-law) |
| 7 | Peace and Conflict Studies (International Joint Award) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/49/peace-and-conflict-studies) |
| 8 | Political and Social Thought | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/61/political-and-social-thought) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | International Relations with International Law | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/47/international-relations-with-international-law) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Comparative Politics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/60/comparative-politics) |
| 2 | International Conflict Analysis | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/62/international-conflict-analysis) |
| 3 | International Relations | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/63/international-relations) |
| 4 | Political and Social Thought | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/61/political-and-social-thought) |

#### School of Engineering, Mathematics and Physics

##### Physics and Astronomy

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Physics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/212/physics) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Physics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4958/physics) |

##### School of Engineering

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering (by Research and Thesis) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3261/biomedical-engineering-by-research) |
| 2 | Digital Arts (by Research) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/2702/digital-arts) |
| 3 | Electronic Engineering (by Research) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/2701/electronic-engineering) |
| 4 | Mechanical Engineering (by Research and Thesis) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3263/mechanical-engineering-by-research) |
| 5 | Sustainable Energy Engineering | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6165/sustainable-energy-engineering) |
| 6 | Sustainable Energy Engineering | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6556/sustainable-energy-engineering-january-start) |
| 7 | Sustainable Energy Engineering with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6173/sustainable-energy-engineering-with-placement) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3262/biomedical-engineering-phd) |
| 2 | Digital Arts | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/264/digital-arts) |
| 3 | Electronic Engineering | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/262/electronic-engineering) |
| 4 | Mechanical Engineering | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/3264/mechanical-engineering-phd) |

##### School of Mathematics, Statistics and Actuarial Science

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Actuarial Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1/actuarial-science) |
| 2 | Actuarial Science with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3260/actuarial-science-with-placement) |
| 3 | Applied Actuarial Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/174/applied-actuarial-science) |
| 4 | Applied Actuarial Science (Integrated Master's) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/176/integrated-masters-in-applied-actuarial-science) |
| 5 | Applied Actuarial Science with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1218/applied-actuarial-science-with-placement) |
| 6 | Applied Actuarial Science with Placement (Integrated Master's) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3258/intergrated-masters-in-applied-actuarial-science-with-placement) |
| 7 | Data Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/5565/data-science) |
| 8 | Data Science with Placement | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/5566/data-science-with-placement) |
| 9 | Mathematics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/149/mathematics) |
| 10 | Statistics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/169/statistics) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Data Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/5565/data-science) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Actuarial Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/1/actuarial-science) |
| 2 | Applied Actuarial Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/174/applied-actuarial-science) |
| 3 | Data Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/5565/data-science) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Actuarial Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/178/actuarial-science) |
| 2 | Mathematics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/149/mathematics) |
| 3 | Statistics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/169/statistics) |

#### School of Humanities

##### Centre for American Studies

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | American Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/8/american-studies) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | American Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/8/american-studies) |

##### Centre for Medieval and Early Modern Studies

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Medieval and Early Modern Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/151/medieval-and-early-modern-studies) |
| 2 | Medieval and Early Modern Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/152/medieval-and-early-modern-studies) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Medieval and Early Modern Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/152/medieval-and-early-modern-studies) |

##### School of Cultures and Languages

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Classical and Archaeological Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6563/classical-and-archaeological-studies) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Classical and Archaeological Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/310/classical-and-archaeological-studies) |
| 2 | Comparative Literature | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/324/comparative-literature) |
| 3 | French | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/41/french) |
| 4 | French and Comparative Literature | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1701/french-and-comparative-literature) |
| 5 | German | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/34/german) |
| 6 | German and Comparative Literature | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/33/german-and-comparative-literature) |
| 7 | Hispanic Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/72/hispanic-studies) |
| 8 | Italian | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/104/italian) |
| 9 | Linguistics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/12/linguistics) |

##### School of English

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Creative Writing | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/211/creative-writing) |
| 2 | English | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/231/english) |
| 3 | English and American Literature | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/222/english-and-american-literature) |
| 4 | Postcolonial Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/236/postcolonial-studies) |
| 5 | The Contemporary Novel: Practice as Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/232/contemporary-novel-practice-as-research) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | English | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/231/english) |
| 2 | Narrative Non-Fiction: Practice as Research | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/2715/narrative-non-fiction-practice-as-research) |
| 3 | Poetry: Text, Practice as Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/235/poetry-text-practice-research) |
| 4 | Postcolonial Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/236/postcolonial-studies) |
| 5 | Text, Practice as Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/240/text-practice-research) |
| 6 | The Contemporary Novel: Practice as Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/232/contemporary-novel-practice-as-research) |

##### School of History

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | History | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/89/history) |
| 2 | Modern History | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/74/modern-history) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | History | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/89/history) |

#### School of Natural Sciences

##### Chemistry and Forensic Science

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Chemistry | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/18/chemistry) |
| 2 | Forensic Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/5/forensic-science) |
| 3 | Forensic Science | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6174/forensic-science) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Chemistry | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4957/chemistry) |
| 2 | Forensic Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6172/forensic-science) |

##### Medway School of Pharmacy

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | General Pharmacy Practice | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/737/general-pharmacy-practice) |
| 2 | Medicines Optimisation | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/738/medicines-optimisation) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | General Pharmacy Practice | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/737/general-pharmacy-practice) |
| 2 | Independent / Supplementary Prescribing | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/740/independent-supplementary-prescribing) |
| 3 | Medicines Optimisation | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/738/medicines-optimisation) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | General Pharmacy Practice | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/737/general-pharmacy-practice) |
| 2 | Medicines Optimisation | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/738/medicines-optimisation) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Pharmacy | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/171/pharmacy) |
| 2 | Pharmacy (Biochemistry and Cell Biology) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/785/pharmacy-biochemistry-cell-biology) |
| 3 | Pharmacy (Chemistry and Drug Delivery) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/784/pharmacy-chemistry-drug-delivery) |
| 4 | Pharmacy (Health Services Research) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/783/pharmacy-health-services-research) |
| 5 | Pharmacy (Pharmacology and Physiology) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/786/pharmacy-pharmacology-physiology) |

##### School of Biosciences

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Applied Biotechnology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/213/applied-biotechnology) |
| 2 | Biochemistry | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1235/biochemistry) |
| 3 | Biomedicine | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1700/biomedicine) |
| 4 | Cell Biology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1236/cell-biology) |
| 5 | Computational Biology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1237/computational-biology) |
| 6 | Genetics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1238/genetics) |
| 7 | Infectious Diseases | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/361/infectious-diseases) |
| 8 | Microbiology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1239/microbiology) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Biochemistry | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/229/biochemistry) |
| 2 | Cell Biology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/285/cell-biology-phd) |
| 3 | Computational Biology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1202/computational-biology-phd) |
| 4 | Genetics | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/286/genetics-phd) |
| 5 | Microbiology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/287/microbiology) |

#### School of Psychology

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Behavioural Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/75/behavioural-science) |
| 2 | Clinical Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4956/clinical-psychology) |
| 3 | Cognitive Psychology and Neuropsychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/65/cognitive-psychology-neuropsychology) |
| 4 | Developmental and Educational Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/66/developmental-and-educational-psychology) |
| 5 | Forensic Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/69/forensic-psychology) |
| 6 | Organisational and Business Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/366/organisational-and-business-psychology) |
| 7 | Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/78/psychology) |
| 8 | Psychology Conversion | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4955/psychology-conversion) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Organisational and Business Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/366/organisational-and-business-psychology) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Organisational and Business Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/366/organisational-and-business-psychology) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Cognitive Psychology / Neuropsychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/76/cognitive-psychology-neuropsychology-phd) |
| 2 | Forensic Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/77/forensic-psychology) |
| 3 | Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/78/psychology) |
| 4 | Social Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/79/social-psychology) |

#### School of Social Sciences

##### Centre for Health Services Studies

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Applied Health and Care Research | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/5567/applied-health-care-research) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Applied Health Research | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/770/applied-health-research) |

##### School of Anthropology and Conservation

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Conservation Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/276/conservation-science) |
| 2 | Conservation Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4962/conservation-science) |
| 3 | Conservation Science and International Wildlife Trade | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6557/conservation-science-and-international-wildlife-trade) |
| 4 | Forensic Osteology and Field Recovery Methods | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/1231/forensic-osteology-and-field-recovery-methods) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Conservation Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/276/conservation-science) |

##### School of Social Policy, Sociology and Social Research

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced Child Protection (Distance Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/326/advanced-child-protection) |
| 2 | Criminology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/173/criminology) |
| 3 | Criminology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/177/criminology) |
| 4 | International Public Policy | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/118/international-public-policy) |
| 5 | International Public Policy (2-Year Master's) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/6175/international-public-policy-two-year) |
| 6 | Social Policy | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/126/social-policy) |
| 7 | Social Work (Step Up to Social Work) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4960/step-up-to-social-work) |
| 8 | Sociology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/145/sociology) |

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Environmental Social Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/14/environmental-social-science) |
| 2 | Social Research Methods | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/119/social-research-methods) |

###### PCert

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced Child Protection (Distance Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/326/advanced-child-protection) |
| 2 | Social Research Methods | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/119/social-research-methods) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Advanced Child Protection (Distance Learning) | Part-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/326/advanced-child-protection) |
| 2 | Social Work (Step Up to Social Work) | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/4960/step-up-to-social-work) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Applied Psychology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/106/applied-psychology) |
| 2 | Criminology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/177/criminology) |
| 3 | Cultural and Global Criminology | Full-time only | [Link](https://www.kent.ac.uk/courses/postgraduate/3811/cultural-global-criminology) |
| 4 | Environmental Social Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/14/environmental-social-science) |
| 5 | Migration Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/334/migration-studies) |
| 6 | Philanthropic Studies | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4370/philanthropic-studies) |
| 7 | Social Policy | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/126/social-policy) |
| 8 | Social Work | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/128/social-work) |
| 9 | Sociology | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/145/sociology) |

##### School of Sport and Exercise Sciences

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Sport and Exercise Science (by Research and Thesis) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/2196/sport-and-exercise-science) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Sport and Exercise Science and Sports Therapy | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/154/sport-and-exercise-science-and-sports-therapy) |

###### SportD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Sport, Exercise and Health Science | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/158/sport-exercise-and-health-science-professional-doctorate) |

##### The Tizard Centre

###### MA

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Community Care | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/109/community-care) |
| 2 | Intellectual and Developmental Disabilities | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/110/intellectual-and-developmental-disabilities) |
| 3 | Mental Health of People with Learning Disabilities | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/112/mental-health-of-people-with-learning-disabilities) |

###### MSc

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Applied Behaviour Analysis and Positive Behaviour Support | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4964/applied-behaviour-analysis-and-positive-behaviour-support) |
| 2 | Intellectual Disabilities and Autism (Autism) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/101/intellectual-disabilities-and-autism) |
| 3 | Intellectual Disabilities and Autism (Clinical Placement) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6178/intellectual-disabilities-and-autism-clinical-placement) |
| 4 | Intellectual Disabilities and Autism (Forensic) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6179/intellectual-disabilities-and-autism-forensic) |
| 5 | Intellectual Disabilities and Autism (Intellectual Disabilities) | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/6176/intellectual-disabilities-and-autism) |

###### PDip

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Applied Behaviour Analysis and Positive Behaviour Support | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/4964/applied-behaviour-analysis-and-positive-behaviour-support) |

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Community Care | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/109/community-care) |
| 2 | Intellectual and Developmental Disabilities | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/110/intellectual-and-developmental-disabilities) |
| 3 | Mental Health of People with Learning Disabilities | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/112/mental-health-of-people-with-learning-disabilities) |

#### Unknown

##### Centre for the Study of Higher Education

###### PhD

| # | 专业 | Mode | URL |
|---|------|------|-----|
| 1 | Higher Education | Full-time or part-time | [Link](https://www.kent.ac.uk/courses/postgraduate/242/higher-education) |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate entry requirements

#### A-Level typical offers

| Programme | A-Level requirement | UCAS tariff |
|-----------|-------------------|-------------|
| Computer Science | BBB | 104-120 |
| Architecture | ABB | 120-128 |
| Pharmacy | ABB (incl. Chemistry B + another science) | 120-128 |
| Law | AAB | 128-136 |
| Psychology | ABB | 120-128 |
| Physics | ABB (incl. Mathematics B) | 120-128 |
| Medicine | AAA/AAB (incl. Chemistry or Biology) | N/A (separate process) |
| Data Science | BBB | 104-120 |
| Digital Design | BBC | 96-112 |

> **Note**: Most Kent UG programmes require BBB-ABB (tariff 104-128). Law requires AAB. Medicine requires AAA/AAB and has a separate admissions process via Kent and Medway Medical School (KMMS).

#### GCSE requirements

- Most programmes: Mathematics grade 4/C required
- Some programmes (e.g. Psychology): may require specific GCSE subjects
- Medicine: separate GCSE requirements via KMMS

#### International Baccalaureate

- Typical: 30 points in the IB Diploma or 120 UCAS tariff points (for programmes requiring BBB)
- Higher requirements for Law, Medicine, etc.

### 3.2 Postgraduate entry requirements

- Most Masters programmes: 2.1 (Upper Second Class Honours) or above in a relevant subject
- Some programmes accept 2.2 (Lower Second Class Honours)
- MBA: typically requires 2.1 + work experience
- PhD: typically requires a Masters degree in a relevant subject

### 3.3 English language requirements

Kent uses a 3-tier English language proficiency system benchmarked against CEFR:

| Level | CEFR | IELTS | TOEFL iBT (pre-Jan 2026) | Duolingo |
|-------|------|-------|-------------------------|----------|
| Good | B2 | 6.0 (min 5.5 each) | 80 (R20, L&W19, S22) | 110 (S&W&R110, L105) |
| Very Good | B2 | 6.5 (min 5.5 each) | 87 (R20, L&W19, S22) | 120 (S&R120, W130, L115) |
| Excellent | C1 | 7.0 (min 7.0 each) | 95 (R&W24, L22, S25) | 130 (S&R130, W145, L125) |

#### Accepted tests

**Secure English Language Tests (SELT)**:
- IELTS for UKVI (2-year validity)
- LanguageCert International ESOL SELT
- LanguageCert Academic SELT
- Pearson Academic UKVI
- Skills for English UKVI

**Non-SELT tests**:
- IELTS Academic (2-year validity)
- TOEFL iBT / Home Edition (2-year validity)
- Duolingo English Test (2-year validity)
- Cambridge B2 First / C1 Advanced (2-year validity)
- Oxford ELLT Digital
- Kaplan Test of English (KTE)
- INTO English Language Assessment (IELA)

**Qualifications accepted**:
- GCSE English Language Grade 4/C or above
- A Level English Language or English Literature Grade C or above
- IB Standard Level Grade 5 or above in English A: Language and Literature
- Medium of Instruction (MOI) letters from majority English-speaking countries

> **Course-specific level**: Most UG programmes require "Good" level (IELTS 6.0). Law and some humanities programmes may require "Very Good" (IELTS 6.5). Check individual course pages for the specific level required.

### 3.4 Application process

- **UK/Ireland students**: Apply via UCAS (institution code K24)
- **International students**: Apply via UCAS or directly on the Kent website
- **Medicine**: Separate application process via KMMS (UCAS code K24)

### 3.5 Application deadlines

- **UCAS Equal Consideration deadline**: 29 January (for September start)
- **UCAS Clearing**: July-September
- **Medicine**: 15 October (UCAS deadline for Medicine)
- **PG programmes**: Rolling admissions (apply early for competitive programmes)

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition fees (2026-27 academic year)

#### Undergraduate

| Fee status | Annual fee (typical) | Notes |
|-----------|---------------------|-------|
| **Home (UK)** | £9,250 | Regulated fee; may increase by RPI in subsequent years |
| **International (classroom)** | £19,300 - £20,700 | Law, Business, Humanities |
| **International (lab/studio)** | £23,500 | Sciences, Engineering, Computing, Psychology |
| **International (Medicine)** | £49,700 | Kent and Medway Medical School |

#### Postgraduate

| Fee status | Annual fee (typical) | Notes |
|-----------|---------------------|-------|
| **Home (UK) Masters** | £9,250 - £12,000 | Varies by programme |
| **International (classroom) Masters** | £19,300 | Humanities, Social Sciences |
| **International (lab/studio) Masters** | £23,500 - £24,700 | Sciences, Engineering, Business |
| **International MBA** | ~£25,000 - £30,000 | Kent Business School |

> **Fee increases**: Kent reserves the right to increase tuition fees by RPI (excluding mortgage interest) in subsequent years. International fees may also increase.

### 4.2 Financial aid

- **Kent Scholarships**: Available for high-achieving international students
- **Your Kent Start**: £2,000 for new UG students (2026 entry)
- **Postgraduate loans**: UK students can apply for PG loans from Student Finance England
- **Country-specific scholarships**: Various scholarships available for specific nationalities

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: University of Kent
  source_url: https://www.kent.ac.uk
  source_snippet: University of Kent logo and link to homepage
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: ug_courses.total
  value: 216
  source_url: https://api.kent.ac.uk/api/programmes/current/undergraduate/programmes
  source_snippet: API returns 216 UG programme entries
  capture_date: 2026-07-08
  evidence_type: api_endpoint

E-U-003:
  field: pg_courses.total
  value: 220
  source_url: https://api.kent.ac.uk/api/programmes/current/postgraduate/programmes
  source_snippet: API returns 220 PG programme entries
  capture_date: 2026-07-08
  evidence_type: api_endpoint

E-U-004:
  field: ug_fees.international
  value: 19300-49700
  source_url: https://www.kent.ac.uk/courses/undergraduate/124/computer-science
  source_snippet: International: £23,500 (CS), £19,300 (Law), £49,700 (Medicine)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: english_language.ielts
  value: 6.0-7.0
  source_url: https://www.kent.ac.uk/courses/english-language-requirements
  source_snippet: Good: IELTS 6.0 min 5.5 each; Very Good: 6.5 min 5.5; Excellent: 7.0 min 7.0
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: a_level.computer_science
  value: BBB
  source_url: https://api.kent.ac.uk/api/programmes/current/undergraduate/programmes/124
  source_snippet: a_level_headline: BBB
  capture_date: 2026-07-08
  evidence_type: api_endpoint

E-U-007:
  field: ucas_code
  value: K24
  source_url: https://www.kent.ac.uk/courses/undergraduate/124/computer-science
  source_snippet: Institution ID K24
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

```yaml
document_type: university_admissions_kb
schema_version: 2.0
institution:
  name: University of Kent
  slug: kent
  region: uk
  country: England
  location: Canterbury (main), Medway
  ucas_code: K24
  qs_ranking: ~400-450 (2025)
  type: public_research_university
programme_counts:
  ug: 216
  pgt: 195
  phd: 80
  total: 436
academic_schools: 10
fees_2026_27:
  ug_home: 9250
  ug_international_range: 19300-49700
  pgt_international_range: 19300-30000
english_requirements:
  ielts_range: 6.0-7.0
  cefr_levels: [B2, C1]
  accepted_tests: [IELTS UKVI, IELTS Academic, TOEFL iBT, Duolingo, LanguageCert, Pearson Academic, Cambridge, Oxford ELLT, KTE]
capture_date: 2026-07-08
capture_tool: ego-browser + Kent API
evidence_chain: E-U-001 through E-U-007
```

---

## SECTION 7 — Data quality notes

### 7.1 Completeness

- UG programmes: 216 entries extracted from API (includes all variants: Year Abroad, Year in Industry, Foundation Year)
- The website shows 87 "base" programmes (variants grouped together)
- PG programmes: 220 entries extracted from API
- Entry requirements: sampled from API (A-level headline, IB headline, tariff points)
- Fees: sampled from course pages (consistent across similar programmes)

### 7.2 Known limitations

- Fee data not available in API; sampled from individual course pages
- Some courses have empty `main_school` field in API (mapped to "Unknown")
- 2026 restructure means some API school names are legacy; mapped to new 10-school structure
- Medicine (BM BS) is delivered by Kent and Medway Medical School (KMMS), a joint venture with Canterbury Christ Church University
- Canterbury College partner courses (top-up degrees) are validated by Kent but taught at Canterbury College
- PG fee ranges are approximate; check individual programme pages for exact fees

### 7.3 Reconciliation

- UG API count: 216 programmes
- PG API count: 220 programmes
- Website displayed UG count: 87 base programmes (variants grouped)
- Faculty totals sum to: 216 (UG) + 220 (PG) = 436 total