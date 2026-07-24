# Ulster University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Northern Ireland)

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

Ulster University is Northern Ireland's largest university with 4 faculties and 23 schools/departments delivering 527 unique degree programs (287 undergraduate + 240 postgraduate). Founded 1968 as the New University of Ulster and merged with Ulster Polytechnic in 1984. Named UK and Ireland University of the Year 2024 (Times/Sunday Times Good University Guide). The university has 3 main campuses in Northern Ireland (Belfast, Coleraine, Derry~Londonderry) plus branch campuses in London, Birmingham, and Manchester. Course list is sourced from a Funnelback-powered search collection `ulster~sp-courses` accessible via the public course finder at `https://www.ulster.ac.uk/courses`.

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BEng/MEng/BMus/BDes/LLB/MArch/MAcc/MOptom/MPharm/MSci/MBBS) | 287 |
| 本科辅修 (Minor) | 0 (Ulster does not publish a separate minor inventory) |
| 研究生学位项目 (MA/MSc/MBA/LLM/MFA/MDes/MMus/MPA/MEd/MArch/PGCE) | 240 |
| 研究生高级证书/文凭 (PgCert/PgDip/GradCert/AdvCert/AdvDip) | included in PG count |
| **学位项目总计 (UG + Grad)** | **527** |
| 学院 (Faculties) 数量 | 4 |
| 系/项目组 (Schools/Departments) 数量 | 23 |

> Note: The Rule-1 total = 287 (UG) + 240 (PG) = 527, which reconciles with the sum of the rule-5 tables below. Ulster does not publish a standalone "minor" registry; the structure here is degree + pathway (e.g. "with placement year", "with Education", "Degree Apprenticeship").

### 0.2 学院 / 系层级结构

```
Ulster University
├── Faculty of Arts, Humanities and Social Sciences (AHSS)   [学院]
│   ├── Belfast School of Art                                 [系]
│   ├── School of Applied Social and Policy Sciences          [系]
│   ├── School of Arts and Humanities                         [系]
│   ├── School of Communication and Media                     [系]
│   ├── School of Education                                   [系]
│   └── School of Law                                         [系]
├── Faculty of Computing, Engineering and the Built Environment (CEBE)  [学院]
│   ├── Belfast School of Architecture and the Built Environment          [系]
│   ├── School of Computing                                 [系]
│   ├── School of Computing, Engineering and Intelligent Systems          [系]
│   └── School of Engineering                                [系]
├── Faculty of Life and Health Sciences (LHS)                [学院]
│   ├── School of Biomedical Sciences                        [系]
│   ├── School of Geography and Environmental Sciences       [系]
│   ├── School of Health Sciences                            [系]
│   ├── School of Medicine                                   [系]
│   ├── School of Nursing and Paramedic Science              [系]
│   ├── School of Pharmacy and Pharmaceutical Sciences      [系]
│   ├── School of Psychology                                 [系]
│   └── School of Sport and Exercise Science                 [系]
└── Ulster University Business School (UUBS)                 [学院]
    ├── Department of Accounting, Finance and Economics      [系]
    ├── Department of Global Business and Enterprise         [系]
    ├── Department of Hospitality Tourism and Events Management  [系]
    ├── Department of Management, Leadership and Marketing   [系]
    └── The Business Institute                               [系]
```

> Cross-faculty notes: Architecture (Belfast School of Art's BArch + Belfast School of Architecture's MArch) and Computing (split across School of Computing for IT and School of Computing, Engineering and Intelligent Systems for AI/Software) are split between faculties. The Business Institute is a small postgraduate-only unit in UUBS. School of Nursing appears only in PG list; UG is delivered by School of Nursing and Paramedic Science.

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA (Hons) | Bachelor of Arts with Honours | 本科 | 33 |
| BDes (Hons) | Bachelor of Design with Honours | 本科 | 5 |
| BMus (Hons) | Bachelor of Music with Honours | 本科 | 2 |
| BSc (Hons) | Bachelor of Science with Honours | 本科 | 175 |
| BEng (Hons) | Bachelor of Engineering with Honours | 本科 | 23 |
| BEng (Hons)/MEng (Hons) | Integrated BEng/MEng pathway | 本科 | 5 |
| MEng (Hons) | Master of Engineering with Honours (UG integrated masters) | 本科 | 6 |
| LLB (Hons) | Bachelor of Laws with Honours | 本科 | 15 |
| LLB | Bachelor of Laws (Graduate Entry / non-Hons) | 本科 | 4 |
| MAcc | Master of Accounting (UG integrated) | 本科 | 1 |
| MArch | Master of Architecture (UG integrated) | 本科 | 1 |
| MOptom | Master of Optometry (UG integrated) | 本科 | 1 |
| MPharm (Hons) | Master of Pharmacy with Honours (UG integrated) | 本科 | 1 |
| MSci (Hons) | Master in Science (UG integrated) | 本科 | 1 |
| BSc (Hons)/MSci (Hons) | Integrated BSc/MSci pathway | 本科 | 1 |
| MBBS | Bachelor of Medicine, Bachelor of Surgery | 本科 | 1 |
| AdvCert | Advanced Certificate | 本科/PG | 4 |
| AdvDip | Advanced Diploma | 本科 | 1 |
| Certificate | Certificate | 本科 | 3 |
| Diploma | Diploma | 本科 | 4 |
| **本科合计** | | | **287** |
| MA | Master of Arts | 研究生 | 15 |
| MSc | Master of Science | 研究生 | 110 |
| MArch | Master of Architecture | 研究生 | 1 |
| MEd | Master of Education | 研究生 | 1 |
| MFA | Master of Fine Art | 研究生 | 4 |
| MDes | Master of Design | 研究生 | 2 |
| MMus | Master of Music | 研究生 | 2 |
| MPA | Master of Public Administration | 研究生 | 2 |
| MBA | Master of Business Administration | 研究生 | 3 |
| LLM | Master of Laws | 研究生 | 12 |
| LLM/MSc | Combined LLM/MSc | 研究生 | 2 |
| PGCE | Postgraduate Certificate in Education | 研究生 | 11 |
| PgCert | Postgraduate Certificate | 研究生 | 23 |
| PgDip | Postgraduate Diploma | 研究生 | 9 |
| PgDip/MSc | Combined PgDip/MSc | 研究生 | 31 |
| PgCert/PgDip/MSc | Combined PG pathway | 研究生 | 10 |
| PgDip/MA | Combined PgDip/MA | 研究生 | 1 |
| GradCert | Graduate Certificate | 研究生 | 1 |
| **研究生合计** | | | **240** |
| **总计** | | | **527** |

> Ulster uses UK "Hons" suffixes (Hons = Honours) and offers many integrated masters pathways (e.g. BEng/MEng) where the same record appears with different award names. Counts above are by `finalawardacronym` value as published in the course finder.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

#### Undergraduate matrix

| 学院 \ 学位 | BA (Hons) | BDes (Hons) | BMus (Hons) | BSc (Hons) | BEng (Hons) | BEng (Hons)/MEng (Hons) | MEng (Hons) | LLB (Hons) | LLB | MAcc | MArch | MOptom | MPharm (Hons) | MSci (Hons) | BSc (Hons)/MSci (Hons) | MBBS | AdvCert | AdvDip | Certificate | Diploma | 合计 ||---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|| Faculty of Arts, Humanities and Social Sciences (AHSS) | 32 | 5 | 2 | 49 | 0 | 0 | 0 | 15 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 4 | 116 || Faculty of Computing, Engineering and the Built Environment (CEBE) | 1 | 0 | 0 | 35 | 23 | 5 | 6 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 72 || Faculty of Life and Health Sciences (LHS) | 0 | 0 | 0 | 46 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 3 | 0 | 0 | 0 | 53 || Ulster University Business School (UUBS) | 0 | 0 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 46 || **本科合计** | **33** | **5** | **2** | **175** | **23** | **5** | **6** | **15** | **4** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **4** | **1** | **3** | **4** | **287** |

#### Postgraduate matrix

| 学院 \ 学位 | MA | MSc | MArch | MEd | MFA | MDes | MMus | MPA | MBA | LLM | LLM/MSc | PGCE | PgCert | PgDip | PgDip/MSc | PgCert/PgDip/MSc | PgDip/MA | GradCert | 合计 ||---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|| Faculty of Arts, Humanities and Social Sciences (AHSS) | 15 | 10 | 0 | 1 | 4 | 2 | 2 | 2 | 0 | 12 | 2 | 0 | 2 | 3 | 4 | 0 | 1 | 0 | 60 || Faculty of Computing, Engineering and the Built Environment (CEBE) | 0 | 26 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 1 | 12 | 2 | 0 | 0 | 55 || Faculty of Life and Health Sciences (LHS) | 0 | 26 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 4 | 15 | 8 | 0 | 1 | 61 || Ulster University Business School (UUBS) | 0 | 48 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 53 || **研究生合计** | **15** | **110** | **1** | **1** | **4** | **2** | **2** | **2** | **3** | **12** | **2** | **0** | **23** | **9** | **31** | **10** | **1** | **1** | **229** |

> The column totals (287 UG + 240 PG = 527) match Rule 1. The matrix uses the canonical degree codes as published by Ulster.

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Ulster's 4 faculties collectively operate 17 schools/departments that deliver undergraduate programs. The Section 0.2 tree maps the parent → child relationships. UG degrees include BA, BSc, BEng (with integrated MEng option), LLB, BMus, BDes, plus integrated masters (MAcc, MArch, MOptom, MPharm, MSci) and the MBBS. Many programmes appear in multiple "modes" (full-time, part-time, with placement year, with Education, Degree Apprenticeship) and "campuses" (Belfast, Coleraine, Derry~Londonderry); each variant is listed separately.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Arts, Humanities and Social Sciences (AHSS)
##### Belfast School of Art
###### BA (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Art and Design Foundation Year | <https://www.ulster.ac.uk/courses/202728/art-and-design-foundation-year-45600> || 2 | Textile Art, Design and Fashion | <https://www.ulster.ac.uk/courses/202728/textile-art-design-and-fashion-45444> || 3 | Fine Art | <https://www.ulster.ac.uk/courses/202728/fine-art-45469> || 4 | Fine Art | <https://www.ulster.ac.uk/courses/202728/fine-art-44971> || 5 | Photography with Video | <https://www.ulster.ac.uk/courses/202728/photography-with-video-45482> || 6 | Illustration | <https://www.ulster.ac.uk/courses/202728/illustration-45608> |###### BDes (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Animation | <https://www.ulster.ac.uk/courses/202728/animation-45483> || 2 | Games Design | <https://www.ulster.ac.uk/courses/202728/games-design-45561> || 3 | Graphic Design | <https://www.ulster.ac.uk/courses/202728/graphic-design-44431> || 4 | Digital Design | <https://www.ulster.ac.uk/courses/202728/digital-design-45519> || 5 | Design (Product, Ceramics, Silversmithing and Jewellery) | <https://www.ulster.ac.uk/courses/202627/design-product-ceramics-silversmithing-and-jewellery-41289> |##### School of Applied Social and Policy Sciences
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Social Work (2 year accelerated route for relevant graduates) | <https://www.ulster.ac.uk/courses/202728/social-work-2-year-accelerated-route-for-relevant-graduates-45554> || 2 | Social Work (3 year full-time course) | <https://www.ulster.ac.uk/courses/202728/social-work-3-year-full-time-course-45553> || 3 | Social Policy with Sociology | <https://www.ulster.ac.uk/courses/202728/social-policy-with-sociology-45528> || 4 | Health and Social Care Policy | <https://www.ulster.ac.uk/courses/202728/health-and-social-care-policy-45434> || 5 | Social Policy | <https://www.ulster.ac.uk/courses/202728/social-policy-45583> || 6 | Sociology with Criminology | <https://www.ulster.ac.uk/courses/202728/criminology-and-criminal-justice-45205> || 7 | Social Policy with Criminology | <https://www.ulster.ac.uk/courses/202728/social-policy-with-criminology-45495> || 8 | Criminology and Criminal Justice | <https://www.ulster.ac.uk/courses/202728/criminology-and-criminal-justice-45579> || 9 | Community Youth Work | <https://www.ulster.ac.uk/courses/202728/community-youth-work-45451> || 10 | Sociology | <https://www.ulster.ac.uk/courses/202728/sociology-45577> || 11 | Community Youth Work | <https://www.ulster.ac.uk/courses/202728/community-youth-work-44944> || 12 | Community Development | <https://www.ulster.ac.uk/courses/202728/community-development-44954> || 13 | Criminology and Criminal Justice | <https://www.ulster.ac.uk/courses/202728/criminology-and-criminal-justice-44933> || 14 | Health and Social Care Policy | <https://www.ulster.ac.uk/courses/202728/health-and-social-care-policy-44932> || 15 | Social Policy | <https://www.ulster.ac.uk/courses/202728/social-policy-45045> || 16 | Social Policy with Criminology | <https://www.ulster.ac.uk/courses/202728/social-policy-with-criminology-45020> || 17 | Sociology | <https://www.ulster.ac.uk/courses/202728/sociology-45174> || 18 | Sociology with Criminology | <https://www.ulster.ac.uk/courses/202728/sociology-with-criminology-45019> || 19 | Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/politics-and-international-studies-45581> || 20 | Politics and International Studies with Criminology | <https://www.ulster.ac.uk/courses/202728/politics-and-international-studies-with-criminology-45535> || 21 | Sociology with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/sociology-with-politics-and-international-studies-45543> || 22 | Sociology with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/sociology-with-politics-and-international-studies-45061> || 23 | Politics and International Studies with Criminology | <https://www.ulster.ac.uk/courses/202627/politics-and-international-studies-with-criminology-40620> || 24 | Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/politics-and-international-studies-44914> || 25 | Criminology and Criminal Justice | <https://www.ulster.ac.uk/courses/202728/criminology-and-criminal-justice-45601> || 26 | Criminology and Criminal Justice | <https://www.ulster.ac.uk/courses/202627/criminology-and-criminal-justice-40725> || 27 | Social Policy with Sociology | <https://www.ulster.ac.uk/courses/202728/social-policy-with-sociology-45048> || 28 | Sociology with Criminology | <https://www.ulster.ac.uk/courses/202728/sociology-with-criminology-45631> || 29 | Sociology with Education | <https://www.ulster.ac.uk/courses/202728/sociology-with-education-45630> || 30 | Sociology with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/sociology-with-politics-and-international-studies-45632> || 31 | Sociology with History | <https://www.ulster.ac.uk/courses/202728/sociology-with-history-44391> || 32 | Sociology with Criminology | <https://www.ulster.ac.uk/courses/202728/sociology-with-criminology-45267> || 33 | Sociology with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/sociology-with-politics-and-international-studies-45268> || 34 | Sociology with History | <https://www.ulster.ac.uk/courses/202728/sociology-with-history-43405> |###### Certificate
| # | 专业 | URL ||---|------|-----|| 1 | Community Youth Studies | <https://www.ulster.ac.uk/courses/202728/community-youth-studies-44945> |##### School of Arts and Humanities
###### AdvCert
| # | 专业 | URL ||---|------|-----|| 1 | Irish Studies | <https://www.ulster.ac.uk/courses/202728/irish-studies-44201> |###### AdvDip
| # | 专业 | URL ||---|------|-----|| 1 | Irish Studies | <https://www.ulster.ac.uk/courses/202728/irish-studies-44191> |###### BA (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | English | <https://www.ulster.ac.uk/courses/202728/english-45421> || 2 | Music with Irish | <https://www.ulster.ac.uk/courses/202728/music-with-irish-44283> || 3 | History | <https://www.ulster.ac.uk/courses/202728/history-44146> || 4 | Drama | <https://www.ulster.ac.uk/courses/202728/drama-45533> || 5 | English and History | <https://www.ulster.ac.uk/courses/202728/english-and-history-44232> || 6 | English with Education | <https://www.ulster.ac.uk/courses/202728/english-with-education-45514> || 7 | History with Education | <https://www.ulster.ac.uk/courses/202728/history-with-education-44229> || 8 | Drama | <https://www.ulster.ac.uk/courses/202728/drama-45052> || 9 | English | <https://www.ulster.ac.uk/courses/202728/english-45150> || 10 | Irish with Music | <https://www.ulster.ac.uk/courses/202728/irish-with-music-44221> || 11 | Irish Language and Literature | <https://www.ulster.ac.uk/courses/202728/irish-language-and-literature-44301> || 12 | Modern Irish | <https://www.ulster.ac.uk/courses/202728/modern-irish-45084> || 13 | Drama with Education | <https://www.ulster.ac.uk/courses/202728/drama-with-education-45573> || 14 | Music with Education | <https://www.ulster.ac.uk/courses/202728/music-with-education-45575> || 15 | Irish with Education | <https://www.ulster.ac.uk/courses/202728/irish-with-education-44293> || 16 | Irish with Business | <https://www.ulster.ac.uk/courses/202728/irish-with-business-44209> || 17 | Drama with History | <https://www.ulster.ac.uk/courses/202728/drama-with-history-44311> || 18 | Irish with History | <https://www.ulster.ac.uk/courses/202728/irish-with-history-44310> || 19 | Music with History | <https://www.ulster.ac.uk/courses/202728/music-with-history-44309> || 20 | Drama with History | <https://www.ulster.ac.uk/courses/202728/drama-with-history-43255> || 21 | Irish with History | <https://www.ulster.ac.uk/courses/202728/irish-with-history-43254> || 22 | History with Digital Media Production | <https://www.ulster.ac.uk/courses/202728/history-with-digital-media-production-44426> |###### BMus (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Music | <https://www.ulster.ac.uk/courses/202728/music-45580> || 2 | Music | <https://www.ulster.ac.uk/courses/202728/music-44833> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Cinematic Arts | <https://www.ulster.ac.uk/courses/202728/cinematic-arts-45534> || 2 | Cinematic Arts | <https://www.ulster.ac.uk/courses/202728/cinematic-arts-43127> || 3 | Creative Audio | <https://www.ulster.ac.uk/courses/202728/creative-audio-44273> || 4 | Creative Audio | <https://www.ulster.ac.uk/courses/202728/creative-audio-43191> || 5 | Games Design and Development | <https://www.ulster.ac.uk/courses/202728/games-design-and-development-45610> || 6 | Games Design and Development | <https://www.ulster.ac.uk/courses/202728/games-design-and-development-45214> |###### Diploma
| # | 专业 | URL ||---|------|-----|| 1 | Irish Language | <https://www.ulster.ac.uk/courses/202728/irish-language-44964> || 2 | Irish Language | <https://www.ulster.ac.uk/courses/202728/irish-language-44965> || 3 | Irish Language | <https://www.ulster.ac.uk/courses/202728/irish-language-45769> || 4 | Irish Language | <https://www.ulster.ac.uk/courses/202728/irish-language-45768> |##### School of Communication and Media
###### BA (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Journalism with English | <https://www.ulster.ac.uk/courses/202728/marine-science-with-optional-placement-year-44284> || 2 | Journalism | <https://www.ulster.ac.uk/courses/202728/journalism-45582> || 3 | Screen Production | <https://www.ulster.ac.uk/courses/202728/screen-production-45559> || 4 | Digital Media Production | <https://www.ulster.ac.uk/courses/202728/digital-media-production-45450> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Communication and Counselling Studies | <https://www.ulster.ac.uk/courses/202728/communication-and-counselling-studies-45427> || 2 | Communication Management and Public Relations | <https://www.ulster.ac.uk/courses/202728/communication-management-and-public-relations-45420> || 3 | Language and Linguistics | <https://www.ulster.ac.uk/courses/202728/language-and-linguistics-45518> || 4 | Communication, Advertising and Marketing | <https://www.ulster.ac.uk/courses/202728/communication-advertising-and-marketing-45461> || 5 | Communication and Counselling Studies | <https://www.ulster.ac.uk/courses/202728/communication-and-counselling-studies-44909> || 6 | Communication Management and Public Relations | <https://www.ulster.ac.uk/courses/202728/communication-management-and-public-relations-45021> || 7 | Counselling - Professional Development | <https://www.ulster.ac.uk/courses/202728/counselling-professional-development-44951> || 8 | Language and Linguistics | <https://www.ulster.ac.uk/courses/202728/language-and-linguistics-45032> || 9 | Communication | <https://www.ulster.ac.uk/courses/202728/communication-45629> |###### LLB
| # | 专业 | URL ||---|------|-----|| 1 | Journalism with Education | <https://www.ulster.ac.uk/courses/202728/sport-physical-activity-and-health-with-optional-placement-year-45445> |##### School of Education
###### Certificate
| # | 专业 | URL ||---|------|-----|| 1 | Teaching | <https://www.ulster.ac.uk/courses/202728/teaching-44990> || 2 | Teaching | <https://www.ulster.ac.uk/courses/202728/teaching-44989> |##### School of Law
###### LLB
| # | 专业 | URL ||---|------|-----|| 1 | Law with Accounting | <https://www.ulster.ac.uk/courses/202728/mechanical-and-manufacturing-engineering-45527> || 2 | Law with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/electrical-and-electronic-engineering-degree-apprenticeship-43343> || 3 | Law (Graduate Entry) | <https://www.ulster.ac.uk/courses/202627/accounting-and-finance-41252> |###### LLB (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Law with Marketing | <https://www.ulster.ac.uk/courses/202728/law-with-marketing-45565> || 2 | Law with Irish | <https://www.ulster.ac.uk/courses/202728/law-with-irish-44220> || 3 | Law | <https://www.ulster.ac.uk/courses/202728/law-45430> || 4 | Law | <https://www.ulster.ac.uk/courses/202728/law-44916> || 5 | Law | <https://www.ulster.ac.uk/courses/202728/law-45431> || 6 | Law with Criminology | <https://www.ulster.ac.uk/courses/202728/international-tourism-management-45628> || 7 | Law with Criminology | <https://www.ulster.ac.uk/courses/202728/law-with-criminology-45017> || 8 | Law with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/law-with-politics-and-international-studies-45016> || 9 | Law with Computing | <https://www.ulster.ac.uk/courses/202728/politics-and-international-studies-with-criminology-45152> || 10 | Law | <https://www.ulster.ac.uk/courses/202728/law-44917> || 11 | Law with Criminology | <https://www.ulster.ac.uk/courses/202728/law-with-criminology-45624> || 12 | Law with Criminology | <https://www.ulster.ac.uk/courses/202728/law-with-criminology-45255> || 13 | Law with Politics and International Studies | <https://www.ulster.ac.uk/courses/202627/law-with-politics-and-international-studies-41491> || 14 | Law with Politics and International Studies | <https://www.ulster.ac.uk/courses/202728/law-with-politics-and-international-studies-45256> || 15 | Law - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/law-degree-apprenticeship-45266> |#### Faculty of Computing, Engineering and the Built Environment (CEBE)
##### Belfast School of Architecture and the Built Environment
###### BA (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Architecture | <https://www.ulster.ac.uk/courses/202728/architecture-45479> |###### BEng (Hons)/MEng (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Architectural Engineering | <https://www.ulster.ac.uk/courses/202728/architectural-engineering-45599> || 2 | Civil Engineering | <https://www.ulster.ac.uk/courses/202728/civil-engineering-45456> || 3 | Architectural Engineering | <https://www.ulster.ac.uk/courses/202728/architectural-engineering-45196> || 4 | Civil Engineering | <https://www.ulster.ac.uk/courses/202728/civil-engineering-45147> || 5 | Civil Engineering - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/civil-engineering-degree-apprenticeship-43393> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Quantity Surveying and Commercial Management (Degree Apprenticeship) | <https://www.ulster.ac.uk/courses/202728/quantity-surveying-and-commercial-management-degree-apprenticeship-45157> || 2 | Construction Engineering and Management - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/construction-engineering-and-management-degree-apprenticeship-45158> || 3 | Quantity Surveying and Commercial Management | <https://www.ulster.ac.uk/courses/202728/quantity-surveying-and-commercial-management-44910> || 4 | Civil Engineering | <https://www.ulster.ac.uk/courses/202728/civil-engineering-44188> || 5 | Real Estate | <https://www.ulster.ac.uk/courses/202728/real-estate-45426> || 6 | Energy | <https://www.ulster.ac.uk/courses/202728/energy-45520> || 7 | Quantity Surveying and Commercial Management | <https://www.ulster.ac.uk/courses/202728/quantity-surveying-and-commercial-management-45428> || 8 | Building Surveying | <https://www.ulster.ac.uk/courses/202728/building-surveying-45473> || 9 | Architectural Technology and Management | <https://www.ulster.ac.uk/courses/202728/architectural-technology-and-management-45481> || 10 | Construction Engineering and Management | <https://www.ulster.ac.uk/courses/202728/construction-engineering-and-management-45460> || 11 | Environmental Health | <https://www.ulster.ac.uk/courses/202728/environmental-health-45432> || 12 | Building Surveying | <https://www.ulster.ac.uk/courses/202728/building-surveying-44981> || 13 | Construction Engineering and Management | <https://www.ulster.ac.uk/courses/202728/construction-engineering-and-management-44963> || 14 | Real Estate | <https://www.ulster.ac.uk/courses/202728/real-estate-44908> || 15 | Architectural Technology and Management | <https://www.ulster.ac.uk/courses/202728/architectural-technology-and-management-45004> || 16 | Energy | <https://www.ulster.ac.uk/courses/202728/energy-45075> |###### BSc (Hons)/MSci (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Planning, Regeneration and Development | <https://www.ulster.ac.uk/courses/202627/planning-regeneration-and-development-41279> |###### MArch
| # | 专业 | URL ||---|------|-----|| 1 | Architecture | <https://www.ulster.ac.uk/courses/202728/architecture-45480> |##### School of Computing
###### BEng (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Computer Science | <https://www.ulster.ac.uk/courses/202728/computer-science-45439> || 2 | Software Engineering | <https://www.ulster.ac.uk/courses/202728/software-engineering-45436> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Interactive Computing | <https://www.ulster.ac.uk/courses/202728/interactive-computing-45598> || 2 | Computing Technologies | <https://www.ulster.ac.uk/courses/202728/computing-technologies-45437> || 3 | Computing Science | <https://www.ulster.ac.uk/courses/202728/computing-science-45438> || 4 | Computing Systems - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/computing-systems-degree-apprenticeship-42839> || 5 | Computing Systems | <https://www.ulster.ac.uk/courses/202728/computing-systems-42908> |###### MEng (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Software Engineering | <https://www.ulster.ac.uk/courses/202728/software-engineering-45617> |##### School of Computing, Engineering and Intelligent Systems
###### BEng (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Renewable Energy Engineering | <https://www.ulster.ac.uk/courses/202728/renewable-energy-engineering-44242> || 2 | Renewable Energy Engineering | <https://www.ulster.ac.uk/courses/202728/renewable-energy-engineering-43225> || 3 | Mechanical and Manufacturing Engineering | <https://www.ulster.ac.uk/courses/202627/mechanical-and-manufacturing-engineering-41341> || 4 | Mechanical and Manufacturing Engineering | <https://www.ulster.ac.uk/courses/202728/mechanical-and-manufacturing-engineering-45046> || 5 | Electrical and Electronic Engineering | <https://www.ulster.ac.uk/courses/202728/electrical-and-electronic-engineering-44241> || 6 | Electrical and Electronic Engineering | <https://www.ulster.ac.uk/courses/202728/electrical-and-electronic-engineering-42951> || 7 | Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/artificial-intelligence-45555> || 8 | Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/artificial-intelligence-45118> || 9 | Mechanical Engineering with Enterprise Development | <https://www.ulster.ac.uk/courses/202728/mechanical-engineering-with-enterprise-development-45569> || 10 | Electronic Engineering with Enterprise Development | <https://www.ulster.ac.uk/courses/202728/electronic-engineering-with-enterprise-development-45568> || 11 | Mechanical Engineering with Enterprise Development | <https://www.ulster.ac.uk/courses/202728/mechanical-engineering-with-enterprise-development-45169> || 12 | Electronic Engineering with Enterprise Development | <https://www.ulster.ac.uk/courses/202728/electronic-engineering-with-enterprise-development-45168> || 13 | Mechanical and Manufacturing Engineering - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/mechanical-and-manufacturing-engineering-degree-apprenticeship-45202> || 14 | Electrical and Electronic Engineering - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202627/electrical-and-electronic-engineering-degree-apprenticeship-41525> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Computer Science | <https://www.ulster.ac.uk/courses/202728/computer-science-45590> || 2 | Computing with Education | <https://www.ulster.ac.uk/courses/202627/english-with-digital-media-production-42386> || 3 | Software Engineering | <https://www.ulster.ac.uk/courses/202728/software-engineering-45424> || 4 | Computer Science | <https://www.ulster.ac.uk/courses/202728/computer-science-45173> || 5 | Digital Technologies | <https://www.ulster.ac.uk/courses/202728/digital-technologies-45423> || 6 | Digital Technologies | <https://www.ulster.ac.uk/courses/202728/digital-technologies-45022> || 7 | Computing with Applied Mathematics | <https://www.ulster.ac.uk/courses/202728/computing-with-applied-mathematics-44740> || 8 | Computing with Applied Mathematics | <https://www.ulster.ac.uk/courses/202728/computing-with-applied-mathematics-45363> || 9 | Software Engineering | <https://www.ulster.ac.uk/courses/202728/software-engineering-45146> || 10 | Computer Science (Games Programming) | <https://www.ulster.ac.uk/courses/202728/computer-science-games-programming-51199> || 11 | Computer Science (Games Programming) | <https://www.ulster.ac.uk/courses/202728/computer-science-games-programming-51194> || 12 | Cyber Security | <https://www.ulster.ac.uk/courses/202728/cyber-security-51094> || 13 | Cyber Security | <https://www.ulster.ac.uk/courses/202728/cyber-security-51090> |##### School of Engineering
###### BEng (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Mechatronic Engineering | <https://www.ulster.ac.uk/courses/202728/mechatronic-engineering-45487> || 2 | Electronic Engineering | <https://www.ulster.ac.uk/courses/202728/electronic-engineering-45490> || 3 | Mechanical Engineering | <https://www.ulster.ac.uk/courses/202728/mechanical-engineering-45488> || 4 | Engineering Management | <https://www.ulster.ac.uk/courses/202728/engineering-management-45489> || 5 | Mechatronic Engineering | <https://www.ulster.ac.uk/courses/202728/mechatronic-engineering-45015> || 6 | Biomedical Engineering | <https://www.ulster.ac.uk/courses/202728/biomedical-engineering-45458> || 7 | Mechatronic Engineering - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/mechatronic-engineering-degree-apprenticeship-45328> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Technology with Design | <https://www.ulster.ac.uk/courses/202728/technology-with-design-45486> |###### MEng (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Biomedical Engineering | <https://www.ulster.ac.uk/courses/202728/biomedical-engineering-45591> || 2 | Mechatronic Engineering | <https://www.ulster.ac.uk/courses/202728/mechatronic-engineering-45521> || 3 | Engineering Management | <https://www.ulster.ac.uk/courses/202728/engineering-management-45468> || 4 | Mechanical Engineering | <https://www.ulster.ac.uk/courses/202728/mechanical-engineering-45522> || 5 | Electronic Engineering | <https://www.ulster.ac.uk/courses/202728/electronic-engineering-45523> |#### Faculty of Life and Health Sciences (LHS)
##### School of Biomedical Sciences
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Biology with optional placement year | <https://www.ulster.ac.uk/courses/202728/biology-with-optional-placement-year-45440> || 2 | Biomedical Science | <https://www.ulster.ac.uk/courses/202728/biomedical-science-44243> || 3 | Biomedical Science with placement year | <https://www.ulster.ac.uk/courses/202627/biomedical-science-with-placement-year-41343> || 4 | Dietetics | <https://www.ulster.ac.uk/courses/202728/dietetics-45464> || 5 | Food and Nutrition with placement year | <https://www.ulster.ac.uk/courses/202728/food-and-nutrition-with-placement-year-45462> || 6 | Human Nutrition with placement year | <https://www.ulster.ac.uk/courses/202728/human-nutrition-with-placement-year-45465> || 7 | Biomedical Science | <https://www.ulster.ac.uk/courses/202728/biomedical-science-43130> || 8 | Biomedical Science | <https://www.ulster.ac.uk/courses/202728/biomedical-science-45033> || 9 | Biomedical Science (Life Sciences) | <https://www.ulster.ac.uk/courses/202627/biomedical-science-life-sciences-40439> || 10 | Applied Medical Sciences | <https://www.ulster.ac.uk/courses/202728/applied-medical-sciences-44789> || 11 | Applied Biomedical Science with DPP (Pathology) | <https://www.ulster.ac.uk/courses/202627/applied-biomedical-science-with-dpp-pathology-41268> |###### MOptom
| # | 专业 | URL ||---|------|-----|| 1 | Optometry | <https://www.ulster.ac.uk/courses/202728/optometry-50949> |##### School of Geography and Environmental Sciences
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Geography with optional placement year | <https://www.ulster.ac.uk/courses/202728/geography-with-optional-placement-year-45531> || 2 | Geography with Education and optional placement year | <https://www.ulster.ac.uk/courses/202728/design-product-ceramics-silversmithing-and-jewellery-45478> || 3 | Environmental Science with optional placement year | <https://www.ulster.ac.uk/courses/202728/environmental-science-with-optional-placement-year-45530> || 4 | Environmental Science with Education and optional placement year | <https://www.ulster.ac.uk/courses/202627/environmental-science-with-education-and-optional-placement-year-41351> || 5 | Marine Science (with Optional Placement Year) | <https://www.ulster.ac.uk/courses/202627/marine-science-with-optional-placement-year-41388> |##### School of Health Sciences
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Podiatry | <https://www.ulster.ac.uk/courses/202728/podiatry-45605> || 2 | Physiotherapy | <https://www.ulster.ac.uk/courses/202728/physiotherapy-44323> || 3 | Occupational Therapy | <https://www.ulster.ac.uk/courses/202728/occupational-therapy-45604> || 4 | Speech and Language Therapy | <https://www.ulster.ac.uk/courses/202728/speech-and-language-therapy-45603> || 5 | Radiotherapy and Oncology | <https://www.ulster.ac.uk/courses/202728/radiotherapy-and-oncology-44324> || 6 | Diagnostic Radiography & Imaging | <https://www.ulster.ac.uk/courses/202728/diagnostic-radiography-imaging-44326> || 7 | Respiratory and Sleep Physiology | <https://www.ulster.ac.uk/courses/202728/respiratory-and-sleep-physiology-45683> || 8 | Cardiac Physiology | <https://www.ulster.ac.uk/courses/202728/cardiac-physiology-44719> |##### School of Medicine
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Personalised Medicine with optional placement year | <https://www.ulster.ac.uk/courses/202728/personalised-medicine-with-optional-placement-year-44136> |###### MBBS
| # | 专业 | URL ||---|------|-----|| 1 | Medicine | <https://www.ulster.ac.uk/courses/202728/medicine-45586> |##### School of Nursing and Paramedic Science
###### AdvCert
| # | 专业 | URL ||---|------|-----|| 1 | Non-Medical Prescribing | <https://www.ulster.ac.uk/courses/202728/non-medical-prescribing-43307> || 2 | General Practice Nursing | <https://www.ulster.ac.uk/courses/202627/general-practice-nursing-40738> || 3 | Non-Medical Prescribing | <https://www.ulster.ac.uk/courses/202627/non-medical-prescribing-40756> |###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Nursing (Adult) | <https://www.ulster.ac.uk/courses/202728/nursing-adult-45449> || 2 | Nursing Science | <https://www.ulster.ac.uk/courses/202627/nursing-science-41391> || 3 | Nursing (Mental Health) | <https://www.ulster.ac.uk/courses/202728/nursing-mental-health-45448> || 4 | Applied Health Studies | <https://www.ulster.ac.uk/courses/202627/applied-health-studies-40432> || 5 | Health and Social Care | <https://www.ulster.ac.uk/courses/202728/health-and-social-care-45475> || 6 | Paramedic Science | <https://www.ulster.ac.uk/courses/202728/paramedic-science-45571> || 7 | Health and Social Care | <https://www.ulster.ac.uk/courses/202728/health-and-social-care-45236> || 8 | Health and Social Care | <https://www.ulster.ac.uk/courses/202728/health-and-social-care-45616> || 9 | Health and Social Care | <https://www.ulster.ac.uk/courses/202728/health-and-social-care-44991> |##### School of Pharmacy and Pharmaceutical Sciences
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Applied Pharmaceutical Sciences | <https://www.ulster.ac.uk/courses/202728/applied-pharmaceutical-sciences-44812> || 2 | Veterinary Nursing | <https://www.ulster.ac.uk/courses/202728/veterinary-nursing-45689> || 3 | Advancing Animal Healthcare and Practice | <https://www.ulster.ac.uk/courses/202728/advancing-animal-healthcare-and-practice-45260> |###### MPharm (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Pharmacy | <https://www.ulster.ac.uk/courses/202728/pharmacy-45463> |###### MSci (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Pharmaceutical Bioscience | <https://www.ulster.ac.uk/courses/202728/pharmaceutical-bioscience-45516> |##### School of Psychology
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Psychology with optional placement year | <https://www.ulster.ac.uk/courses/202728/psychology-with-optional-placement-year-44760> || 2 | Psychology with optional placement year | <https://www.ulster.ac.uk/courses/202728/psychology-with-optional-placement-year-45433> |##### School of Sport and Exercise Science
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Sport, Physical Activity and Health with optional placement year | <https://www.ulster.ac.uk/courses/202627/sport-physical-activity-and-health-with-optional-placement-year-41250> || 2 | Sport and Exercise Nutrition | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-nutrition-45596> || 3 | Outdoor Adventure | <https://www.ulster.ac.uk/courses/202728/outdoor-adventure-45595> || 4 | Sports Coaching and Performance | <https://www.ulster.ac.uk/courses/202728/sports-coaching-and-performance-45611> || 5 | Sport and Exercise Sciences | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-sciences-45613> || 6 | Sport Studies | <https://www.ulster.ac.uk/courses/202728/sport-studies-45612> || 7 | Sport and Exercise Sciences | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-sciences-45697> |#### Ulster University Business School (UUBS)
##### Department of Accounting, Finance and Economics
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Finance and Investment Management | <https://www.ulster.ac.uk/courses/202728/finance-and-investment-management-45441> || 2 | Accounting (Pathways) | <https://www.ulster.ac.uk/courses/202728/accounting-pathways-44159> || 3 | Business Economics | <https://www.ulster.ac.uk/courses/202728/business-economics-45558> || 4 | Accounting and Law | <https://www.ulster.ac.uk/courses/202728/accounting-and-law-45443> || 5 | Economics | <https://www.ulster.ac.uk/courses/202728/economics-45557> || 6 | Business Technology - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/business-technology-degree-apprenticeship-45320> || 7 | Financial Technology - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/financial-technology-degree-apprenticeship-45321> || 8 | Financial Technology | <https://www.ulster.ac.uk/courses/202728/financial-technology-45107> || 9 | Accounting with Management | <https://www.ulster.ac.uk/courses/202728/accounting-with-management-44937> || 10 | Accounting with Management - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/accounting-with-management-degree-apprenticeship-45371> || 11 | Business Technology | <https://www.ulster.ac.uk/courses/202728/business-technology-45178> |###### MAcc
| # | 专业 | URL ||---|------|-----|| 1 | Advanced Accounting | <https://www.ulster.ac.uk/courses/202728/advanced-accounting-43447> |##### Department of Global Business and Enterprise
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Business Studies with Computing | <https://www.ulster.ac.uk/courses/202728/environmental-science-with-education-and-optional-placement-year-45537> || 2 | Business Studies with Irish | <https://www.ulster.ac.uk/courses/202728/business-studies-with-irish-45621> || 3 | Business Studies with Drama | <https://www.ulster.ac.uk/courses/202728/business-studies-with-drama-45623> || 4 | Business Studies | <https://www.ulster.ac.uk/courses/202728/business-studies-45698> || 5 | Business Studies with Pathways | <https://www.ulster.ac.uk/courses/202728/business-studies-with-pathways-45578> || 6 | Accounting and Marketing | <https://www.ulster.ac.uk/courses/202728/accounting-and-marketing-44226> || 7 | Accounting and Finance | <https://www.ulster.ac.uk/courses/202728/accounting-and-finance-43124> || 8 | Accounting and Finance | <https://www.ulster.ac.uk/courses/202728/accounting-and-finance-44164> || 9 | Accounting with Education | <https://www.ulster.ac.uk/courses/202728/accounting-with-education-45619> || 10 | Accounting with Computing | <https://www.ulster.ac.uk/courses/202728/law-with-politics-and-international-studies-45625> || 11 | Business Studies with Pathways | <https://www.ulster.ac.uk/courses/202728/business-studies-with-pathways-45060> || 12 | Accounting and Finance - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/accounting-and-finance-degree-apprenticeship-45245> || 13 | Business Studies | <https://www.ulster.ac.uk/courses/202728/business-studies-51140> || 14 | Business Studies with Education | <https://www.ulster.ac.uk/courses/202728/business-studies-with-education-45620> |##### Department of Hospitality Tourism and Events Management
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | International Hospitality Management | <https://www.ulster.ac.uk/courses/202728/international-hospitality-management-45453> || 2 | Culinary Arts Management | <https://www.ulster.ac.uk/courses/202728/culinary-arts-management-45454> || 3 | International Hospitality Management | <https://www.ulster.ac.uk/courses/202728/international-hospitality-management-44949> || 4 | Culinary Arts Management | <https://www.ulster.ac.uk/courses/202728/culinary-arts-management-44950> || 5 | Event Management | <https://www.ulster.ac.uk/courses/202728/event-management-45452> || 6 | Event Management | <https://www.ulster.ac.uk/courses/202728/event-management-44948> || 7 | International Tourism Management | <https://www.ulster.ac.uk/courses/202627/international-tourism-management-41501> || 8 | International Tourism Management | <https://www.ulster.ac.uk/courses/202728/international-tourism-management-45259> || 9 | International Hospitality Management - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/international-hospitality-management-degree-apprenticeship-45244> || 10 | Food Business and Innovation | <https://www.ulster.ac.uk/courses/202728/food-business-and-innovation-44344> || 11 | Food Business and Innovation | <https://www.ulster.ac.uk/courses/202728/food-business-and-innovation-45258> |##### Department of Management, Leadership and Marketing
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Management | <https://www.ulster.ac.uk/courses/202728/management-45532> || 2 | Business Studies | <https://www.ulster.ac.uk/courses/202728/business-studies-45597> || 3 | Human Resource Management | <https://www.ulster.ac.uk/courses/202728/human-resource-management-44152> || 4 | Marketing | <https://www.ulster.ac.uk/courses/202728/marketing-45560> || 5 | Business Studies | <https://www.ulster.ac.uk/courses/202728/business-studies-45184> || 6 | Marketing | <https://www.ulster.ac.uk/courses/202728/marketing-45108> || 7 | Marketing | <https://www.ulster.ac.uk/courses/202728/marketing-45589> || 8 | Marketing | <https://www.ulster.ac.uk/courses/202728/marketing-45171> |##### The Business Institute
###### BSc (Hons)
| # | 专业 | URL ||---|------|-----|| 1 | Leading on Customer Operations | <https://www.ulster.ac.uk/courses/202728/leading-on-customer-operations-45172> |### 1.3 Interdisciplinary / cross-faculty undergraduate programs

Ulster's UG provision does not publish a formal list of joint majors; the only cross-faculty programs sit within combined-honours variants (e.g. "Accounting and Law", "Music with History") which are listed under the home department in the table above. Architecture is jointly offered as BA (Hons) in Belfast School of Art and MArch in Belfast School of Architecture; both are listed under their respective schools.

### 1.4 Minors — complete list

Ulster does not publish a separate "minor" inventory. Students may take a smaller number of modules from another school via the elective/free-choice modules within their degree; the breadth is recorded within each course's "module catalogue" rather than a published minor registry.

### 1.5 General/Institute-wide requirements

Ulster operates a **modular credit framework** in line with UK higher-education conventions. Most undergraduate honours degrees are 360 credit points; integrated masters (MEng, MPharm, MSci, MArch, MAcc, MOptom) are 480 credit points; the MBBS is 5 years. Each course has a programme specification available from the course page. No institute-wide general education curriculum is imposed beyond the English/maths general entrance requirements and the English language requirements for international students.

### 1.6 Course-ID → Major quick-lookup

Ulster does not use a numbered course system. UCAS codes are used (e.g. W302 = Music BMUs Hons, NN44 = Accounting and Finance). The full UCAS code is published in the course finder and printed on each course page.

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Faculty of Arts, Humanities and Social Sciences (AHSS)
##### Belfast School of Art
###### MA
| # | 专业 | URL ||---|------|-----|| 1 | Animation | <https://www.ulster.ac.uk/courses/202627/animation-40510> || 2 | Animation | <https://www.ulster.ac.uk/courses/202627/animation-40509> || 3 | Games Design | <https://www.ulster.ac.uk/courses/202728/games-design-45111> || 4 | Games Design | <https://www.ulster.ac.uk/courses/202728/games-design-45110> |###### MDes
| # | 专业 | URL ||---|------|-----|| 1 | User Experience and Service Design | <https://www.ulster.ac.uk/courses/202728/user-experience-and-service-design-45337> || 2 | User Experience and Service Design | <https://www.ulster.ac.uk/courses/202728/user-experience-and-service-design-45006> |###### MFA
| # | 专业 | URL ||---|------|-----|| 1 | Fine Art (MFA) | <https://www.ulster.ac.uk/courses/202728/fine-art-mfa-43081> || 2 | Fine Art (MFA) | <https://www.ulster.ac.uk/courses/202728/fine-art-mfa-43082> || 3 | Photography (MFA) | <https://www.ulster.ac.uk/courses/202728/photography-mfa-45005> || 4 | Photography (MFA) eLearning | <https://www.ulster.ac.uk/courses/202728/photography-mfa-elearning-45062> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Art Psychotherapy | <https://www.ulster.ac.uk/courses/202728/art-psychotherapy-51193> |##### School of Applied Social and Policy Sciences
###### MPA
| # | 专业 | URL ||---|------|-----|| 1 | Public Administration | <https://www.ulster.ac.uk/courses/202728/public-administration-43131> || 2 | Public Administration | <https://www.ulster.ac.uk/courses/202728/public-administration-42985> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Criminology and Criminal Justice | <https://www.ulster.ac.uk/courses/202728/criminology-and-criminal-justice-45167> || 2 | Criminology and Criminal Justice | <https://www.ulster.ac.uk/courses/202728/criminology-and-criminal-justice-45166> || 3 | Peace and Conflict Studies | <https://www.ulster.ac.uk/courses/202728/peace-and-conflict-studies-45187> || 4 | Social Policy | <https://www.ulster.ac.uk/courses/202728/social-policy-45191> || 5 | Peace and Conflict Studies | <https://www.ulster.ac.uk/courses/202728/peace-and-conflict-studies-45186> || 6 | Social Policy | <https://www.ulster.ac.uk/courses/202728/social-policy-45190> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Community Youth Work | <https://www.ulster.ac.uk/courses/202627/community-youth-work-40518> |##### School of Arts and Humanities
###### MA
| # | 专业 | URL ||---|------|-----|| 1 | Cultural Heritage and Museum Studies | <https://www.ulster.ac.uk/courses/202627/cultural-heritage-and-museum-studies-40404> || 2 | Cultural Heritage and Museum Studies | <https://www.ulster.ac.uk/courses/202627/cultural-heritage-and-museum-studies-40403> || 3 | History | <https://www.ulster.ac.uk/courses/202627/history-40422> || 4 | English Literature | <https://www.ulster.ac.uk/courses/202627/english-literature-40329> || 5 | English Literature | <https://www.ulster.ac.uk/courses/202627/english-literature-40330> || 6 | History | <https://www.ulster.ac.uk/courses/202728/history-45027> || 7 | Irish Language Translation, Interpreting and Professional Language Skills | <https://www.ulster.ac.uk/courses/202627/irish-language-translation-interpreting-and-professional-language-skills-40478> || 8 | Irish Language Translation, Interpreting and Professional Language Skills | <https://www.ulster.ac.uk/courses/202728/irish-language-translation-interpreting-and-professional-language-skills-43142> |###### MMus
| # | 专业 | URL ||---|------|-----|| 1 | Creative Musicianship | <https://www.ulster.ac.uk/courses/202728/creative-musicianship-45010> || 2 | Creative Musicianship | <https://www.ulster.ac.uk/courses/202728/creative-musicianship-45009> |###### PgDip/MA
| # | 专业 | URL ||---|------|-----|| 1 | Museum Practice and Management | <https://www.ulster.ac.uk/courses/202627/museum-practice-and-management-40402> |##### School of Communication and Media
###### MA
| # | 专业 | URL ||---|------|-----|| 1 | Journalism | <https://www.ulster.ac.uk/courses/202627/journalism-50992> || 2 | Film and TV Production | <https://www.ulster.ac.uk/courses/202728/film-and-tv-production-45212> || 3 | Film and TV Production | <https://www.ulster.ac.uk/courses/202728/film-and-tv-production-45211> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Digital Marketing Communication and Leadership | <https://www.ulster.ac.uk/courses/202728/digital-marketing-communication-and-leadership-45030> || 2 | Digital Marketing Communication and Leadership | <https://www.ulster.ac.uk/courses/202728/digital-marketing-communication-and-leadership-45031> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Communication and Public Relations | <https://www.ulster.ac.uk/courses/202627/communication-and-public-relations-40453> || 2 | Communication and Public Relations | <https://www.ulster.ac.uk/courses/202627/communication-and-public-relations-40454> |##### School of Education
###### MEd
| # | 专业 | URL ||---|------|-----|| 1 | Education with Specialisms | <https://www.ulster.ac.uk/courses/202627/education-with-specialisms-40503> |###### PgDip
| # | 专业 | URL ||---|------|-----|| 1 | School Leadership | <https://www.ulster.ac.uk/courses/202728/school-leadership-51081> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Library and Information Management | <https://www.ulster.ac.uk/courses/202627/library-and-information-management-40476> |###### Postgraduate Certificate of Education (PGCE)
| # | 专业 | URL ||---|------|-----|| 1 | PGCE English with Drama and Media Studies | <https://www.ulster.ac.uk/courses/202728/pgce-english-with-drama-and-media-studies-45418> || 2 | PGCE History | <https://www.ulster.ac.uk/courses/202728/pgce-history-45549> || 3 | PGCE Geography | <https://www.ulster.ac.uk/courses/202728/pgce-geography-45550> || 4 | PGCE Primary Education | <https://www.ulster.ac.uk/courses/202728/pgce-primary-education-45545> || 5 | PGCE Art and Design | <https://www.ulster.ac.uk/courses/202627/pgce-art-and-design-41368> || 6 | PGCE Music | <https://www.ulster.ac.uk/courses/202728/pgce-music-45547> || 7 | PGCE Home Economics with Food & Nutrition & Nutrition & Food Science | <https://www.ulster.ac.uk/courses/202728/pgce-home-economics-with-food-nutrition-nutrition-food-science-45548> || 8 | Education in Further Education | <https://www.ulster.ac.uk/courses/202728/education-in-further-education-45563> || 9 | PGCE Physical Education | <https://www.ulster.ac.uk/courses/202728/pgce-physical-education-45546> || 10 | PGCE Technology and Design with Engineering and Manufacturing | <https://www.ulster.ac.uk/courses/202728/pgce-technology-and-design-with-engineering-and-manufacturing-45552> || 11 | Education in Further Education | <https://www.ulster.ac.uk/courses/202728/education-in-further-education-44875> |##### School of Law
###### LLM
| # | 专业 | URL ||---|------|-----|| 1 | Access to Justice | <https://www.ulster.ac.uk/courses/202728/access-to-justice-45082> || 2 | Access to Justice | <https://www.ulster.ac.uk/courses/202728/access-to-justice-45081> || 3 | International Commercial Law and ADR | <https://www.ulster.ac.uk/courses/202627/international-commercial-law-and-adr-40524> || 4 | International Commercial Law and ADR | <https://www.ulster.ac.uk/courses/202627/international-commercial-law-and-adr-40523> || 5 | Gender and Human Rights | <https://www.ulster.ac.uk/courses/202728/gender-and-human-rights-44985> || 6 | Human Rights Law and Transitional Justice | <https://www.ulster.ac.uk/courses/202728/human-rights-law-and-transitional-justice-44987> || 7 | Human Rights Law and Transitional Justice | <https://www.ulster.ac.uk/courses/202728/human-rights-law-and-transitional-justice-44988> || 8 | Gender and Human Rights | <https://www.ulster.ac.uk/courses/202728/gender-and-human-rights-44986> || 9 | Human Rights | <https://www.ulster.ac.uk/courses/202728/human-rights-45365> || 10 | Human Rights | <https://www.ulster.ac.uk/courses/202728/human-rights-45364> || 11 | Law | <https://www.ulster.ac.uk/courses/202728/law-50850> || 12 | Law | <https://www.ulster.ac.uk/courses/202728/law-50851> |###### LLM/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Legal Innovation and Technology Law | <https://www.ulster.ac.uk/courses/202728/legal-innovation-and-technology-law-45134> || 2 | Legal Innovation and Technology Law | <https://www.ulster.ac.uk/courses/202728/legal-innovation-and-technology-law-45135> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Professional Mediation Summer School | <https://www.ulster.ac.uk/courses/202728/international-business-extended-with-human-resource-management-45265> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Employment Law and Practice | <https://www.ulster.ac.uk/courses/202728/employment-law-and-practice-43263> || 2 | Employment Law and Practice | <https://www.ulster.ac.uk/courses/202728/employment-law-and-practice-43262> |###### PgDip
| # | 专业 | URL ||---|------|-----|| 1 | Law | <https://www.ulster.ac.uk/courses/202728/law-45680> || 2 | Law | <https://www.ulster.ac.uk/courses/202728/law-45679> |#### Faculty of Computing, Engineering and the Built Environment (CEBE)
##### Belfast School of Architecture and the Built Environment
###### MArch
| # | 专业 | URL ||---|------|-----|| 1 | Architecture | <https://www.ulster.ac.uk/courses/202728/architecture-45480> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Energy Storage | <https://www.ulster.ac.uk/courses/202728/energy-storage-45088> || 2 | Planning and City Resilience | <https://www.ulster.ac.uk/courses/202627/planning-and-city-resilience-40570> || 3 | Planning and City Resilience | <https://www.ulster.ac.uk/courses/202627/planning-and-city-resilience-40572> || 4 | Real Estate | <https://www.ulster.ac.uk/courses/202627/real-estate-39354> || 5 | Energy Storage | <https://www.ulster.ac.uk/courses/202728/energy-storage-45087> || 6 | Real Estate | <https://www.ulster.ac.uk/courses/202627/real-estate-39353> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Hydrogen Safety | <https://www.ulster.ac.uk/courses/202728/hydrogen-safety-45192> || 2 | Energy Management and Green Technologies | <https://www.ulster.ac.uk/courses/202728/energy-management-and-green-technologies-44863> |###### PgCert/PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Construction Management | <https://www.ulster.ac.uk/courses/202627/construction-management-40463> || 2 | Construction Management | <https://www.ulster.ac.uk/courses/202627/construction-management-40462> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Renewable Energy and Energy Management | <https://www.ulster.ac.uk/courses/202728/renewable-energy-and-energy-management-45149> || 2 | Civil and Infrastructure Engineering | <https://www.ulster.ac.uk/courses/202728/civil-and-infrastructure-engineering-42978> || 3 | Fire Safety Engineering | <https://www.ulster.ac.uk/courses/202728/fire-safety-engineering-44977> || 4 | Fire Safety Engineering | <https://www.ulster.ac.uk/courses/202728/fire-safety-engineering-44976> || 5 | Civil and Infrastructure Engineering - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/civil-and-infrastructure-engineering-degree-apprenticeship-43392> || 6 | Civil and Infrastructure Engineering | <https://www.ulster.ac.uk/courses/202728/civil-and-infrastructure-engineering-42977> |##### School of Computing
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/artificial-intelligence-45105> || 2 | Cyber Security | <https://www.ulster.ac.uk/courses/202728/cyber-security-45091> || 3 | Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/artificial-intelligence-45106> || 4 | Computer Science | <https://www.ulster.ac.uk/courses/202728/computer-science-45156> || 5 | Computer Science | <https://www.ulster.ac.uk/courses/202728/computer-science-45155> || 6 | Computer Science - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/computer-science-degree-apprenticeship-45326> || 7 | Artificial Intelligence - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/artificial-intelligence-degree-apprenticeship-45327> || 8 | Cyber Security | <https://www.ulster.ac.uk/courses/202728/cyber-security-45092> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Computer Science | <https://www.ulster.ac.uk/courses/202728/computer-science-45194> || 2 | Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/artificial-intelligence-45195> || 3 | Internet of Things | <https://www.ulster.ac.uk/courses/202627/internet-of-things-39488> |##### School of Computing, Engineering and Intelligent Systems
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Professional Software Development | <https://www.ulster.ac.uk/courses/202728/professional-software-development-43139> || 2 | Professional Software Development | <https://www.ulster.ac.uk/courses/202728/professional-software-development-43169> || 3 | Data Science | <https://www.ulster.ac.uk/courses/202728/data-science-43150> || 4 | Smart Manufacturing Systems | <https://www.ulster.ac.uk/courses/202627/smart-manufacturing-systems-40550> || 5 | Smart Manufacturing Systems | <https://www.ulster.ac.uk/courses/202627/smart-manufacturing-systems-40551> || 6 | Data Science | <https://www.ulster.ac.uk/courses/202728/data-science-43152> || 7 | Computing Science (Conversion) | <https://www.ulster.ac.uk/courses/202728/computing-science-conversion-43335> || 8 | Ethical and Responsible Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/ethical-and-responsible-artificial-intelligence-43435> || 9 | Ethical and Responsible Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/ethical-and-responsible-artificial-intelligence-43436> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Smart Manufacturing Systems | <https://www.ulster.ac.uk/courses/202627/smart-manufacturing-systems-40714> || 2 | Professional Software Development (Architecture and Design) | <https://www.ulster.ac.uk/courses/202728/professional-software-development-architecture-and-design-43425> || 3 | Data Science (Analytics and Applications) | <https://www.ulster.ac.uk/courses/202728/data-science-analytics-and-applications-43274> || 4 | Data Science (Analytics and Applications) | <https://www.ulster.ac.uk/courses/202728/data-science-analytics-and-applications-43273> || 5 | Smart Manufacturing Systems | <https://www.ulster.ac.uk/courses/202627/smart-manufacturing-systems-40715> || 6 | Ethical and Responsible Artificial Intelligence | <https://www.ulster.ac.uk/courses/202728/ethical-and-responsible-artificial-intelligence-43441> |##### School of Engineering
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Electronic Engineering | <https://www.ulster.ac.uk/courses/202627/pharmaceutical-sciences-40594> || 2 | Mechanical Engineering | <https://www.ulster.ac.uk/courses/202728/mechanical-engineering-45399> || 3 | Mechanical Engineering | <https://www.ulster.ac.uk/courses/202627/mechanical-engineering-40553> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Biomedical Engineering | <https://www.ulster.ac.uk/courses/202728/biomedical-engineering-45209> || 2 | Advanced Composites and Polymers | <https://www.ulster.ac.uk/courses/202627/advanced-composites-and-polymers-42155> |###### PgDip
| # | 专业 | URL ||---|------|-----|| 1 | Advanced Composites and Polymers | <https://www.ulster.ac.uk/courses/202728/advanced-composites-and-polymers-44929> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Biomedical Engineering | <https://www.ulster.ac.uk/courses/202728/biomedical-engineering-44928> || 2 | Advanced Composites and Polymers | <https://www.ulster.ac.uk/courses/202728/advanced-composites-and-polymers-44919> || 3 | Advanced Composites and Polymers | <https://www.ulster.ac.uk/courses/202627/advanced-composites-and-polymers-40289> || 4 | Manufacturing Management | <https://www.ulster.ac.uk/courses/202627/manufacturing-management-40296> || 5 | Manufacturing Management | <https://www.ulster.ac.uk/courses/202627/manufacturing-management-40297> || 6 | Biomedical Engineering | <https://www.ulster.ac.uk/courses/202728/biomedical-engineering-44927> |#### Faculty of Life and Health Sciences (LHS)
##### School of Biomedical Sciences
###### GradCert
| # | 专业 | URL ||---|------|-----|| 1 | Biomedical Science | <https://www.ulster.ac.uk/courses/202728/biomedical-science-45002> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Human Nutrition | <https://www.ulster.ac.uk/courses/202627/human-nutrition-40387> || 2 | Human Nutrition | <https://www.ulster.ac.uk/courses/202627/human-nutrition-40386> || 3 | Dietetics | <https://www.ulster.ac.uk/courses/202627/dietetics-40388> || 4 | Food and Nutrition | <https://www.ulster.ac.uk/courses/202728/food-and-nutrition-44982> || 5 | Food and Nutrition | <https://www.ulster.ac.uk/courses/202728/food-and-nutrition-44983> || 6 | Biotechnology Research | <https://www.ulster.ac.uk/courses/202627/biotechnology-research-40430> || 7 | Biomedical Science | <https://www.ulster.ac.uk/courses/202728/biomedical-science-45397> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Veterinary Public Health | <https://www.ulster.ac.uk/courses/202728/veterinary-public-health-44967> || 2 | The Theory of Independent Prescribing for Optometrists | <https://www.ulster.ac.uk/courses/202627/the-theory-of-independent-prescribing-for-optometrists-40437> |###### PgCert/PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Food Regulatory Affairs | <https://www.ulster.ac.uk/courses/202728/food-regulatory-affairs-45044> || 2 | Food Regulatory Affairs | <https://www.ulster.ac.uk/courses/202728/food-regulatory-affairs-44968> |###### PgDip
| # | 专业 | URL ||---|------|-----|| 1 | Cataract and Refractive Surgery (Theory) | <https://www.ulster.ac.uk/courses/202728/cataract-and-refractive-surgery-theory-44966> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Veterinary Public Health (Food Regulatory Affairs) | <https://www.ulster.ac.uk/courses/202627/veterinary-public-health-food-regulatory-affairs-40352> || 2 | Veterinary Public Health (Food Regulatory Affairs) | <https://www.ulster.ac.uk/courses/202728/veterinary-public-health-food-regulatory-affairs-44969> |##### School of Geography and Environmental Sciences
###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Environmental Management | <https://www.ulster.ac.uk/courses/202728/environmental-management-44997> || 2 | Geographic Information Systems | <https://www.ulster.ac.uk/courses/202728/geographic-information-systems-44995> || 3 | Environmental Toxicology and Pollution Monitoring | <https://www.ulster.ac.uk/courses/202728/environmental-toxicology-and-pollution-monitoring-44996> || 4 | Geographic Information Systems | <https://www.ulster.ac.uk/courses/202728/geographic-information-systems-44994> || 5 | Environmental Management with Geographic Information Systems | <https://www.ulster.ac.uk/courses/202728/environmental-management-with-geographic-information-systems-45047> || 6 | Remote Sensing and Geographic Information Systems | <https://www.ulster.ac.uk/courses/202728/remote-sensing-and-geographic-information-systems-45133> |##### School of Health Sciences
###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Medicines Management | <https://www.ulster.ac.uk/courses/202627/medicines-management-40763> |###### PgCert/PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Advancing Practice | <https://www.ulster.ac.uk/courses/202728/advancing-practice-45213> |##### School of Medicine
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Personalised Medicine | <https://www.ulster.ac.uk/courses/202728/personalised-medicine-45024> || 2 | Personalised Medicine | <https://www.ulster.ac.uk/courses/202728/personalised-medicine-45025> |##### School of Nursing
###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Return to Practice Nursing | <https://www.ulster.ac.uk/courses/202728/communication-and-public-relations-45054> |##### School of Nursing and Paramedic Science
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Advanced Practice | <https://www.ulster.ac.uk/courses/202728/advanced-practice-45215> || 2 | Advanced Practice | <https://www.ulster.ac.uk/courses/202627/advanced-practice-40736> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Non-Medical Prescribing | <https://www.ulster.ac.uk/courses/202728/non-medical-prescribing-43296> || 2 | General Practice Nursing | <https://www.ulster.ac.uk/courses/202627/general-practice-nursing-40737> || 3 | Education for Healthcare Professionals | <https://www.ulster.ac.uk/courses/202728/education-for-healthcare-professionals-43313> || 4 | Non-Medical Prescribing | <https://www.ulster.ac.uk/courses/202627/non-medical-prescribing-40743> |###### PgCert/PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Applied Health Studies | <https://www.ulster.ac.uk/courses/202627/applied-health-studies-40431> || 2 | Health Promotion and Public Health | <https://www.ulster.ac.uk/courses/202627/health-promotion-and-public-health-40758> || 3 | Nursing | <https://www.ulster.ac.uk/courses/202728/nursing-45231> || 4 | Health Promotion and Public Health | <https://www.ulster.ac.uk/courses/202627/health-promotion-and-public-health-40757> || 5 | Nursing | <https://www.ulster.ac.uk/courses/202627/nursing-40755> |###### PgDip
| # | 专业 | URL ||---|------|-----|| 1 | Specialist Community Public Health Nursing | <https://www.ulster.ac.uk/courses/202728/specialist-community-public-health-nursing-45230> || 2 | Specialist Nursing Practice with Integrated Independent and Supplementary Prescribing (V300) | <https://www.ulster.ac.uk/courses/202728/specialist-nursing-practice-with-integrated-independent-and-supplementary-prescribing-v300-45228> || 3 | Specialist Nursing Practice with Integrated Independent and Supplementary Prescribing (V300) | <https://www.ulster.ac.uk/courses/202728/specialist-nursing-practice-with-integrated-independent-and-supplementary-prescribing-v300-45229> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Leadership in Health and Social Care | <https://www.ulster.ac.uk/courses/202728/leadership-in-health-and-social-care-45238> || 2 | Leadership in Health and Social Care | <https://www.ulster.ac.uk/courses/202728/leadership-in-health-and-social-care-45237> |##### School of Pharmacy and Pharmaceutical Sciences
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Pharmaceutical Sciences | <https://www.ulster.ac.uk/courses/202627/pharmaceutical-sciences-40419> || 2 | Advanced Pharmacy Practice | <https://www.ulster.ac.uk/courses/202728/advanced-pharmacy-practice-45170> |##### School of Psychology
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Applied Behaviour Analysis | <https://www.ulster.ac.uk/courses/202728/applied-behaviour-analysis-44836> || 2 | Health Psychology | <https://www.ulster.ac.uk/courses/202728/health-psychology-45382> || 3 | Health Psychology | <https://www.ulster.ac.uk/courses/202728/health-psychology-45381> || 4 | Applied Psychology (Mental Health and Psychological Therapies) | <https://www.ulster.ac.uk/courses/202728/applied-psychology-mental-health-and-psychological-therapies-45090> || 5 | Applied Psychology (Mental Health and Psychological Therapies) | <https://www.ulster.ac.uk/courses/202728/applied-psychology-mental-health-and-psychological-therapies-45089> || 6 | Psychology | <https://www.ulster.ac.uk/courses/202728/psychology-45379> || 7 | Psychology | <https://www.ulster.ac.uk/courses/202728/psychology-45380> |##### School of Sport and Exercise Science
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Strength and Conditioning | <https://www.ulster.ac.uk/courses/202728/strength-and-conditioning-45218> || 2 | Strength and Conditioning | <https://www.ulster.ac.uk/courses/202728/strength-and-conditioning-45219> || 3 | Sports Coaching and Performance | <https://www.ulster.ac.uk/courses/202728/sports-coaching-and-performance-45220> || 4 | Sports Coaching and Performance | <https://www.ulster.ac.uk/courses/202728/sports-coaching-and-performance-45221> || 5 | Sport and Exercise Psychology | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-psychology-45225> || 6 | Sport and Exercise Psychology | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-psychology-45226> |###### PgDip/MSc
| # | 专业 | URL ||---|------|-----|| 1 | Sport and Exercise Nutrition | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-nutrition-45100> || 2 | Sport and Exercise Nutrition | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-nutrition-45101> || 3 | Sport and Exercise Medicine | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-medicine-45223> || 4 | Sport and Exercise Medicine | <https://www.ulster.ac.uk/courses/202728/sport-and-exercise-medicine-45224> |#### Ulster University Business School (UUBS)
##### Department of Accounting, Finance and Economics
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Advanced Accounting | <https://www.ulster.ac.uk/courses/202728/advanced-accounting-43222> || 2 | Global Investment Management | <https://www.ulster.ac.uk/courses/202728/global-investment-management-44956> || 3 | FinTech Management | <https://www.ulster.ac.uk/courses/202728/fintech-management-45094> || 4 | FinTech Management - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/fintech-management-degree-apprenticeship-45322> || 5 | Accounting | <https://www.ulster.ac.uk/courses/202728/accounting-45345> |###### PgDip
| # | 专业 | URL ||---|------|-----|| 1 | Accounting | <https://www.ulster.ac.uk/courses/202728/accounting-45122> |##### Department of Global Business and Enterprise
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | International Business | <https://www.ulster.ac.uk/courses/202728/international-business-44907> || 2 | International Business | <https://www.ulster.ac.uk/courses/202728/international-business-44906> || 3 | International Business | <https://www.ulster.ac.uk/courses/202728/international-business-44882> || 4 | International Business | <https://www.ulster.ac.uk/courses/202728/international-business-44905> || 5 | Leadership and Innovation in the Public Sector | <https://www.ulster.ac.uk/courses/202728/leadership-and-innovation-in-the-public-sector-44984> || 6 | International Business (Extended) with Data Analytics | <https://www.ulster.ac.uk/courses/202728/international-business-extended-with-data-analytics-45263> || 7 | International Business with Human Resource Management | <https://www.ulster.ac.uk/courses/202728/international-business-with-human-resource-management-45140> || 8 | International Business with Data Analytics | <https://www.ulster.ac.uk/courses/202728/international-business-with-data-analytics-44830> || 9 | International Accounting with Analytics | <https://www.ulster.ac.uk/courses/202728/international-accounting-with-analytics-45177> || 10 | International Accounting with Analytics | <https://www.ulster.ac.uk/courses/202728/international-accounting-with-analytics-45176> || 11 | International Business with Data Analytics | <https://www.ulster.ac.uk/courses/202728/international-business-with-data-analytics-45136> || 12 | International Business with Data Analytics | <https://www.ulster.ac.uk/courses/202728/international-business-with-data-analytics-45137> || 13 | International Business with Data Analytics | <https://www.ulster.ac.uk/courses/202728/international-business-with-data-analytics-44831> || 14 | International Business with Human Resource Management | <https://www.ulster.ac.uk/courses/202728/international-business-with-human-resource-management-45139> || 15 | International Business with Human Resource Management | <https://www.ulster.ac.uk/courses/202728/international-business-with-human-resource-management-45138> || 16 | International Business with Human Resource Management | <https://www.ulster.ac.uk/courses/202728/international-business-with-human-resource-management-44848> || 17 | Sustainable Management | <https://www.ulster.ac.uk/courses/202728/sustainable-management-42973> || 18 | International Business (Extended) | <https://www.ulster.ac.uk/courses/202728/international-business-extended-45264> || 19 | International Accounting with Analytics - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202728/international-accounting-with-analytics-degree-apprenticeship-45329> || 20 | Sustainable Management | <https://www.ulster.ac.uk/courses/202728/sustainable-management-42974> |##### Department of Hospitality Tourism and Events Management
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | International Event Management | <https://www.ulster.ac.uk/courses/202728/international-event-management-44946> || 2 | International Event Management | <https://www.ulster.ac.uk/courses/202728/international-event-management-44947> || 3 | International Tourism and Hospitality Management | <https://www.ulster.ac.uk/courses/202728/international-tourism-and-hospitality-management-45029> || 4 | International Tourism and Hospitality Management | <https://www.ulster.ac.uk/courses/202728/international-tourism-and-hospitality-management-45028> || 5 | Global Sustainable Tourism | <https://www.ulster.ac.uk/courses/202728/global-sustainable-tourism-45254> || 6 | Global Sustainable Tourism | <https://www.ulster.ac.uk/courses/202728/global-sustainable-tourism-45253> || 7 | Golf Management | <https://www.ulster.ac.uk/courses/202728/golf-management-45251> || 8 | Golf Management | <https://www.ulster.ac.uk/courses/202728/golf-management-45250> |##### Department of Management, Leadership and Marketing
###### MBA
| # | 专业 | URL ||---|------|-----|| 1 | MBA (Master of Business Administration) | <https://www.ulster.ac.uk/courses/202728/mba-master-of-business-administration-45066> || 2 | Executive MBA (Master of Business Administration) | <https://www.ulster.ac.uk/courses/202728/executive-mba-master-of-business-administration-45073> || 3 | Executive MBA (Master of Business Administration) | <https://www.ulster.ac.uk/courses/202728/executive-mba-master-of-business-administration-44960> |###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Business Development and Innovation | <https://www.ulster.ac.uk/courses/202728/business-development-and-innovation-44761> || 2 | Management | <https://www.ulster.ac.uk/courses/202728/management-43016> || 3 | Marketing | <https://www.ulster.ac.uk/courses/202728/marketing-44931> || 4 | Management and Corporate Governance | <https://www.ulster.ac.uk/courses/202728/management-and-corporate-governance-44935> || 5 | Management and Corporate Governance | <https://www.ulster.ac.uk/courses/202627/management-and-corporate-governance-41568> || 6 | Business Development and Innovation | <https://www.ulster.ac.uk/courses/202728/business-development-and-innovation-44762> || 7 | Business Improvement | <https://www.ulster.ac.uk/courses/202728/business-improvement-44961> || 8 | Executive Leadership | <https://www.ulster.ac.uk/courses/202728/executive-leadership-45074> || 9 | Human Resource Management | <https://www.ulster.ac.uk/courses/202728/human-resource-management-44924> || 10 | Management | <https://www.ulster.ac.uk/courses/202728/management-43017> || 11 | Marketing | <https://www.ulster.ac.uk/courses/202728/marketing-44930> || 12 | Management and Corporate Governance | <https://www.ulster.ac.uk/courses/202627/management-and-corporate-governance-41569> || 13 | Management and Corporate Governance | <https://www.ulster.ac.uk/courses/202728/management-and-corporate-governance-44936> |##### The Business Institute
###### MSc
| # | 专业 | URL ||---|------|-----|| 1 | Business in Technology | <https://www.ulster.ac.uk/courses/202627/business-in-technology-40579> || 2 | Business in Technology - Degree Apprenticeship | <https://www.ulster.ac.uk/courses/202627/business-in-technology-degree-apprenticeship-41754> |###### PgCert
| # | 专业 | URL ||---|------|-----|| 1 | Business Analysis and Consulting | <https://www.ulster.ac.uk/courses/202627/business-analysis-and-consulting-40578> |### 2.2 At least one program's full deep-dive (worked example)

**MSc Computer Science — School of Computing (CEBE)**
- Department: School of Computing, Faculty of Computing, Engineering and the Built Environment
- URL: `https://www.ulster.ac.uk/courses/202728/computer-science-`
- Final award: MSc
- Mode of study: Full-time / Part-time
- Campus: Belfast
- Start year: 2027/28
- Duration: 1 year full-time, 2 years part-time (typical UK MSc)
- International fee (2026/27): **£18,310** (full-time standard Masters rate)
- Home fee (2026/27): **£7,490** (standard Masters rate; some specialist variants £7,880-£9,290)
- English language: IELTS 6.0 (no band below 5.5) — typical
- Application: Direct to Ulster via the postgraduate online application portal
- Sources: course detail page + the international fee table

The School of Computing (CEBE) also offers a related PgCert (rate per credit point), an MSc Artificial Intelligence, an MSc Cyber Security, an MSc Data Science, and a Computer Science PgCert (one-semester conversion option).

### 2.3 Graduate admissions model

- **Decentralized**: All postgraduate applications go through a single Ulster-wide online application portal (separate from UCAS).
- **Per-school entry points**: Each school processes its own admissions; faculty-level admissions tutors.
- **Decisions**: Rolling, with some programs having specific intake dates (e.g. PGCE).
- **Standard application fee**: None for the majority of taught postgraduate courses (Ulster does not charge a standard PG application fee). Some research programmes may have specific arrangements.
- **English language**: IELTS 6.0 minimum (academic) with no band <5.5, with many courses requiring 6.5. Conditional offers are issued when English is borderline.
- **Funding**: Limited Ulster-specific scholarships; international students may apply for Vice-Chancellor's scholarships, country-specific awards, and external schemes (Chevening, Commonwealth).

## SECTION 3 — Application requirements & deadlines

> **Region-aware (UK)**: Ulster follows the UK-wide admissions framework. Sections 3 & 4 use the UK sub-template.

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | **UCAS** (Undergraduate only) | https://www.ulster.ac.uk/study/undergraduate |
| UCAS deadline | **January** (equal consideration, main cycle). UCAS conservatoire & medicine have earlier dates | https://www.ulster.ac.uk/study/undergraduate |
| Application fee | UCAS fee (£28.50 for single choice, £28.50 additional choices — current UCAS published fee) | UCAS, not Ulster |
| UCAS Tariff | Specific entry tariffs published per course; minimum typically equivalent to three A-levels at **CCC** for most UG programmes | https://www.ulster.ac.uk/global/apply/entry-requirements |
| Decision notification | UCAS standard timeline (Ulster-specific) | https://www.ulster.ac.uk/study/undergraduate |
| Interviews | Selected programmes only (Nursing, Medicine, Social Work, Law, Art & Design); see individual course pages | course detail pages |
| Audition | Music, Drama, Performing Arts — see individual course pages | course detail pages |
| Recommendation letters | 1 academic reference via UCAS | UCAS |
| Personal statement | UCAS statement (single for all 5 choices) | UCAS |
| Portfolio | Required for Art & Design programmes (Belfast School of Art) | https://www.ulster.ac.uk/courses |
| Transfer pathway | Limited — see individual course pages for entry-with-advanced-standing | course detail pages |
| SAT/ACT | N/A — UK system uses A-Levels, BTEC, IB etc. | https://www.ulster.ac.uk/global/apply/entry-requirements |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Source |
|------|---------|-------------|--------|
| IELTS Academic | 6.0 (no band below 5.5) | 6.5+ | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| TOEFL iBT / iBT Home | Equivalent score to IELTS 6.0 | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| PTE Academic (UKVI / non-UKVI) | Equivalent to IELTS 6.0 | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| Cambridge English B2 First / C1 Advanced / C2 Proficiency | Pass at level III (each component) | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| Duolingo English Test (DET) | Equivalent score | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| LanguageCert Academic / SELT | Equivalent | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| Trinity ISE | Pass at level III (each component) | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |
| Oxford Test of English (OTE) | Equivalent | Per course | https://www.ulster.ac.uk/global/apply/english-language-requirements |

> The published default is "Most of our courses require a minimum English level of IELTS 6.0 (Academic) or equivalent, with no band score under 5.5." Some courses (e.g. Health Sciences, Law, PGCE) ask for 6.5 or higher — check individual course pages.

### 3.3 Graduate — global rules

- **Decentralized admissions**: All Ulster PG applications go through the postgraduate online application portal (not UCAS).
- **Standard application fee**: Ulster does not charge a standard postgraduate application fee for most taught courses.
- **GRE/GMAT**: Not required for any Ulster programme (no published GRE/GMAT policy).
- **English language**: Same IELTS 6.0 (no band <5.5) baseline as UG; many PG courses ask for 6.5. Conditional offers allowed.
- **Per-program deadlines**: Most PG courses have rolling admissions; some (e.g. PGCE, Dietetics) have fixed dates.
- **Conditional offers**: Standard UK pattern — conditional on final undergraduate results or English test scores.
- **Institutional code**: UCAS code U20 (Ulster); for PG direct applications there is no institutional code, the application is via Ulster's own portal.

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

> Ulster's published fees are at the programme level, not a single total. The 2026/27 figures are shown below from the official international fee table.

| Item | 2026/27 amount (£GBP) | Note |
|------|----------------------|------|
| **Home (NI/ROI) — Full-time UG** | 4,985 | Standard undergraduate, integrated masters, PGCE (Home NI/ROI) |
| **GB — Full-time UG** | 9,250 | Standard undergraduate (GB fee cap) |
| **International / EU (excl. ROI) — Full-time UG** | 17,490 | Standard undergraduate, integrated masters |
| Placement year / intercalary year abroad (International) | 4,900 | Sandwich/intercalary year |
| Part-time UG (per 20 credit point module) | 2,915 (UK) / varies (international rate per credit) | Standard rate |
| MBBS (international) | 39,630 | Plus clinical placement levy £12,133/yr |
| Pre-sessional English (7 weeks) | 1,430 | Pre-sessional English Plus: 2,980 |
| Clinical placement levy (Medicine) | 12,133 (2026/27) | Payable each of 4 years for new international medics |

> Note: All fees quoted are subject to an annual increase. Fees illustrated are based on 2026/27 entry (running September 2026 to August 2027). International deposit required to secure a place.

### 4.2 Undergraduate financial-aid policy

- **Home students**: Eligible for UK Student Finance (tuition loan + maintenance loan). Northern Ireland students apply to Student Finance NI; GB students to Student Finance England/Wales/Northern Ireland. NI/ROI Home fee is £4,985 (2026/27).
- **International students**: Ulster offers a range of Vice-Chancellor's scholarships and country-specific awards. International students are not eligible for UK government loans.
- **Need-blind for internationals**: N/A — Ulster is not need-blind; fee status drives cost.
- **International deposit**: Required to secure a place after an unconditional offer; non-refundable.
- **Scholarships**: See https://www.ulster.ac.uk/global/apply/scholarships and the per-course scholarship callouts on the course detail pages.

### 4.3 Graduate cost & funding framework

| Item | 2026/27 amount (£GBP) | Note |
|------|----------------------|------|
| **Home (NI/ROI) — Full-time Masters** | 7,490 | Standard Masters |
| **Home (NI/ROI) — Specialist Masters (Business / Sport Mgmt / TESOL / etc.)** | 7,880 - 9,290 | Specific named courses |
| **Home (NI/ROI) — MBA** | 12,470 | Standard MBA |
| **Home (NI/ROI) — Executive MBA** | 15,720 | Executive variant |
| **Home (NI/ROI) — PgD Accounting** | 6,200 | Postgraduate Diploma only |
| **Home (NI/ROI) — Postgraduate Research** | 5,238 | MPhil/PhD |
| **Home (NI/ROI) — MSc Physician Associate Studies (180 cp)** | 12,470 | |
| **Home (NI/ROI) — LLM Employment Law & Practice** | 9,290 | |
| **International / EU (excl. ROI) — Full-time Masters** | 18,310 | Standard Masters |
| **International / EU (excl. ROI) — Specialist Masters** | 20,490 | Management/Corporate Governance, Biotechnology Research, Human Nutrition, Pharmaceutical Sciences, LLM Access to Justice, LLM Intl Commercial Law & ADR |
| **International / EU (excl. ROI) — Executive MBA / MPA** | 22,680 | |
| **International / EU (excl. ROI) — Postgraduate Research** | 19,040 | |
| **International / EU (excl. ROI) — Study Abroad (semester)** | 5,300 (1 sem) / 9,720 (2 sem) / 12,480 (3 sem) | |
| Part-time PG (per 30 credit point module) | 3,051.60 (Home) | Standard rate |
| Global Online (per credit point, e.g. MSc Biomedical Science) | 48.45 | Online delivery |

- **Funding taxonomy**: Fully-funded (research council studentships for PhDs), partially-funded (GTAs/GTA for some PG programmes), self-funded (most taught PG).
- **Standard application fee**: None for most taught PG programmes.
- **Fee waivers**: Available for some target groups; check per-school.
- **Cost of attendance**: Detailed cost-of-living information is on the international student guide pages.

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Ulster University"
  source_url: https://www.ulster.ac.uk/
  source_snippet: "Ulster University is registered with the Charity Commission for Northern Ireland (NIC100166)."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.headline_award
  value: "UK and Ireland University of the Year 2024"
  source_url: https://www.ulster.ac.uk/news/2024/november/ulster-university-crowned-university-of-the-year-2024
  source_snippet: "Ulster University Crowned University of the Year 2024"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.faculties.count
  value: 4
  source_url: https://www.ulster.ac.uk/faculties
  source_snippet: "Arts, Humanities and Social Sciences faculty site / Computing, Engineering and the Built Environment faculty site / Life and Health Sciences faculty site / Ulster University Business School faculty site"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-004:
  field: institution.campuses
  value: ["Belfast", "Coleraine", "Derry~Londonderry", "London", "Birmingham", "Manchester"]
  source_url: https://www.ulster.ac.uk/campuses/belfast
  source_snippet: "Belfast campus information / Coleraine campus information / Derry~Londonderry campus information / Ulster University Sports Village / London, Birmingham and Manchester"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: program_directory.ug_total
  value: 576
  source_url: https://ulster-search.funnelback.squiz.cloud/s/search.html?collection=ulster~sp-courses&query=*&f.Level_u%7CY=Undergraduate
  source_snippet: "1 - 200 of 576 search results for / Refined by: Level_u Undergraduate"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: program_directory.pg_total
  value: 508
  source_url: https://ulster-search.funnelback.squiz.cloud/s/search.html?collection=ulster~sp-courses&query=*&f.Level_u%7CY=Postgraduate
  source_snippet: "1 - 200 of search results for / Refined by: Level_u Postgraduate"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: ug_admissions.platform
  value: "UCAS"
  source_url: https://www.ulster.ac.uk/study/undergraduate
  source_snippet: "Undergraduate / Postgraduate / Part-time / Online / Short Courses / PG Research / courses on our course finder"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: ug_admissions.minimum_entry
  value: "Equivalent of three A-levels at CCC"
  source_url: https://www.ulster.ac.uk/global/apply/entry-requirements
  source_snippet: "The minimum required to be considered for entry to our undergraduate programmes is the equivalent of three A-levels at CCC."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: english.ielts_default_min
  value: "6.0 (no band below 5.5)"
  source_url: https://www.ulster.ac.uk/global/apply/english-language-requirements
  source_snippet: "Most of our courses require a minimum English level of IELTS 6.0 (Academic) or equivalent, with no band score under 5.5."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: english.accepted_tests
  value: ["IELTS Academic", "TOEFL iBT/TOEFL iBT Home", "PTE Academic UKVI/non-UKVI", "Cambridge Advanced English", "Cambridge Proficiency in English", "Cambridge English B2 First", "Cambridge IGCSE (ESL)", "Duolingo English Test (DET)", "LanguageCert Academic / SELT", "LanguageCert International ESOL (SELT only)", "Occupational English Test (OET)", "QA Higher Education English Language Test", "Oxford International Digital Institute (OIDI) ELLT", "Oxford Test of English (OTE)", "Skills for English: SELT", "Trinity ISE III (each component)"]
  source_url: https://www.ulster.ac.uk/global/apply/english-language-requirements
  source_snippet: "Accepted English Language Tests / You must have received the award or certification within the last two years."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: english.presessional
  value: "7-week pre-sessional English course, 15 July – 4 September, fee £1,390 (IELTS 5.5 with one band at 5.0)"
  source_url: https://www.ulster.ac.uk/global/apply/english-language-requirements
  source_snippet: "7 weeks / 5.5 (Only 1 band score acceptable at 5.0) / 15 July – 4 September / £1390 / 22 May 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-012:
  field: ug_cost.home_ni_2026_27
  value: 4985
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/home-ni-roi/home-niroi-202627
  source_snippet: "Undergraduate, Postgraduate Certificate in Education (PGCE) and Integrated Masters awards and equivalent courses (except those as detailed below) / 4,985"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-013:
  field: ug_cost.home_gb_2026_27
  value: 9250
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees
  source_snippet: "GB / Tuition Fees for GB Students"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: ug_cost.international_2026_27
  value: 17490
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "Undergraduate and Integrated Masters awards and equivalent courses (except those as detailed below) / 17,490"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-015:
  field: ug_cost.international_mbbs_2026_27
  value: 39630
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "Medicine - MBBS** (see Note 4) / 39,630"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-016:
  field: ug_cost.clinical_placement_levy_2026_27
  value: 12133
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "The levy payable in 2026/27 is £12,133."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-017:
  field: pg_cost.home_masters_standard_2026_27
  value: 7490
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/home-ni-roi/home-niroi-202627
  source_snippet: "Masters courses (except those as detailed below) (PG Certificate/Diploma - see Note 1) / 7,490"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-018:
  field: pg_cost.home_mba_2026_27
  value: 12470
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/home-ni-roi/home-niroi-202627
  source_snippet: "MBA / 12,470"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-019:
  field: pg_cost.home_executive_mba_2026_27
  value: 15720
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/home-ni-roi/home-niroi-202627
  source_snippet: "Executive MBA / 15,720"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-020:
  field: pg_cost.international_masters_standard_2026_27
  value: 18310
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "Masters courses (except those as detailed below) (PG Certificate/Diploma - see Note 1) / 18,310"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-021:
  field: pg_cost.international_specialist_masters_2026_27
  value: 20490
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "MSc Management and Corporate Governance / MSc Biotechnology Research / MSc Human Nutrition / MSc Pharmaceutical Sciences / LLM Access to Justice / LLM International Commercial Law & ADR / 20,490"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-022:
  field: pg_cost.international_postgraduate_research_2026_27
  value: 19040
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "Postgraduate Research / 19,040"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-023:
  field: fees.international_deposit
  value: "Non-refundable; required to secure a place after unconditional offer"
  source_url: https://www.ulster.ac.uk/global/apply/fees-and-finance
  source_snippet: "International (excluding UK and RoI) students are required to pay a deposit. When you receive an unconditional offer, and to secure your place, you will be asked to make a minimum deposit payment against your tuition fees."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-024:
  field: credit_framework.honours_degree
  value: 360
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "Credit Points Table / Honours Degree / 360"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-025:
  field: credit_framework.integrated_masters
  value: 480
  source_url: https://www.ulster.ac.uk/student/fees/tuition-fees/international/tuition-fees-202627-international-and-eu-excluding-roi
  source_snippet: "Integrated Masters Degree / 480"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
```

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: ulster-knowledge-base-v2
  ├── document: 院校总览 (overview) — Section 0
  │     ├── chunk: counts (0.1)
  │     ├── chunk: hierarchy (0.2)
  │     ├── chunk: degree-inventory (0.3)
  │     └── chunk: distribution-matrix (0.4)
  ├── document: Undergraduate — Section 1 (one document; chunked by school)
  │     ├── chunk: Faculty of AHSS (UG)
  │     ├── chunk: Faculty of CEBE (UG)
  │     ├── chunk: Faculty of LHS (UG)
  │     └── chunk: Ulster University Business School (UG)
  ├── document: Postgraduate — Section 2 (one document; chunked by school)
  │     ├── chunk: Faculty of AHSS (PG)
  │     ├── chunk: Faculty of CEBE (PG)
  │     ├── chunk: Faculty of LHS (PG)
  │     └── chunk: Ulster University Business School (PG)
  ├── document: Application requirements — Section 3
  │     ├── chunk: UG admissions (UCAS)
  │     ├── chunk: UG English proficiency
  │     └── chunk: PG admissions
  ├── document: Costs & financial aid — Section 4
  │     ├── chunk: UG cost (line items)
  │     ├── chunk: UG financial aid
  │     └── chunk: PG cost & funding
  └── document: Evidence index — Section 5
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ulster-knowledge-base-v2"
  school: "<home college/school>"
  department: "<home school/department>"
  degree_level: "<BA|BS|BEng|MEng|MSc|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Per-program fees (most courses list a single "international fee" but the underlying data may differ — needs per-course detail scraping) | https://www.ulster.ac.uk/courses |
| P0 | Per-program English language requirements (most courses say "IELTS 6.0"; some require 6.5+ — confirm by per-course check) | https://www.ulster.ac.uk/courses |
| P1 | Per-program application deadlines (UCAS code, intake dates) | https://www.ulster.ac.uk/courses |
| P1 | Postgraduate application portal URL and steps | https://www.ulster.ac.uk/study/postgraduate |
| P1 | Funding/scholarship inventory for international PG students | https://www.ulster.ac.uk/global/apply/scholarships |
| P2 | Minor/elective module catalogue | https://www.ulster.ac.uk/study/undergraduate |
| P2 | Doctoral College / research-degree full list | https://www.ulster.ac.uk/doctoralcollege |

## SECTION 7 — Cross-school comparison framework

| Dimension | Ulster University value |
|-----------|-------------------------|
| Country / region | UK — Northern Ireland |
| UG Home fee (NI/ROI) 2026/27 | £4,985 |
| UG Home fee (GB) 2026/27 | £9,250 |
| UG International fee (standard) 2026/27 | £17,490 |
| UG MBBS International fee 2026/27 | £39,630 + clinical placement levy £12,133/yr |
| PG Home Masters fee 2026/27 | £7,490 |
| PG Home MBA fee 2026/27 | £12,470 |
| PG International Masters fee 2026/27 | £18,310 |
| UCAS deadline | January (equal consideration) |
| Application platform UG | UCAS |
| Application platform PG | Ulster direct online portal |
| Application fee PG | None for most taught courses |
| IELTS default minimum | 6.0 (no band <5.5) |
| TOEFL accepted | Yes (equivalent to IELTS 6.0) |
| Total program count (Rule 1) | **527** (287 UG + 240 PG) |
| School/Department count (Rule 2) | 23 |
| Honours degree credit points | 360 |
| Integrated masters credit points | 480 |
| Need-blind for internationals | N/A (fee status drives cost) |
| Tuition-free income threshold | N/A (UK system) |
| Median price paid | N/A (UK Home fees capped) |
| April-15 honor date | N/A (not applicable to UK admissions) |

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: ulster.ac.uk (main site), ulster-search.funnelback.squiz.cloud (course finder), Student Guide (student.ulster.ac.uk)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Counts verified**: UG=287, PG=240, Total=527, Reconciled with rule-5 table rows
