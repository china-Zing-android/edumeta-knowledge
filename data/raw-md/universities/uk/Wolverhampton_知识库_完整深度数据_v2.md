# University of Wolverhampton Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BEng/etc.) | 221 |
| 本科 HNC / HND / Foundation 证书 | 5 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 72 |
| 研究生研究项目 (PhD/MPhil/MRes) | 45 |
| 研究生高级证书/文凭 (PGCert/PGDip) | 36 |
| **学位项目总计 (UG + Grad)** | **379** |
| 学院 / 独立系所总数 | 4 (3 faculties + 1 medical school) |
| 教学/研究学系 (Schools) | 7 |

> Reconciliation: 226 UG + 153 PG = 379 (matches matrix total of 176+109+94=379).

### 0.2 学院 / 系层级结构

```
University of Wolverhampton
├── Faculty of Arts, Business and Social Sciences          [学院]
│   ├── School of Business & Law                            [系]
│   └── School of Social Science, Humanities & Creative Industries  [系]
├── Faculty of Education, Health and Wellbeing             [学院]
│   ├── School of Education & Psychology                    [系]
│   ├── School of Nursing and Midwifery                     [系]
│   └── School of Health and Wellbeing                      [系]
├── Faculty of Science and Engineering                     [学院]
│   ├── School of Architecture, Computing & Engineering     [系]
│   └── School of Pharmacy & Life Sciences                  [系]
└── Black Country Medical School                            [独立学院]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 | 本校官方 (official) |
|---------|------|------|-----------|---------------------|
| BA | Bachelor of Arts | 本科 | 100 | BA (Hons) |
| BSc | Bachelor of Science | 本科 | 97 | BSc (Hons) |
| BEng | Bachelor of Engineering | 本科 | 18 | BEng (Hons) |
| BMid | Bachelor of Midwifery | 本科 | 3 | BMid (Hons) |
| LLB | Bachelor of Laws | 本科 | 3 | LLB (Hons) |
| HNC | Higher National Certificate | 本科 (sub-degree) | 4 | HNC |
| HND | Higher National Diploma | 本科 (sub-degree) | 0 | HND |
| MPharm | Master of Pharmacy | 本科 (4-yr integrated) | 0 | MPharm (Hons) |
| Cert | Certificate | 本科/PG | 1 | Cert |
| MA | Master of Arts | 研究生 | 18 | MA |
| MSc | Master of Science | 研究生 | 45 | MSc |
| MBA | Master of Business Administration | 研究生 | 2 | MBA |
| MArch | Master of Architecture | 研究生 | 1 | MArch |
| LLM | Master of Laws | 研究生 | 6 | LLM |
| MPhil | Master of Philosophy | 研究生 (research) | 10 | MPhil |
| MRes | Master of Research | 研究生 (research) | 7 | MRes |
| PhD | Doctor of Philosophy | 研究生 (research) | 28 | PhD |
| PGCert | Postgraduate Certificate | 研究生 (sub-degree) | 29 | PGCert |
| PGDip | Postgraduate Diploma | 研究生 (sub-degree) | 7 | PGDip |

> Note: MPharm (Hons) is the integrated 4-year pharmacy undergraduate degree; the classification here puts it under BA-canonical tier for cross-school comparability. Wolverhampton awards 1 MPharm (Hons) Pharmacy.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BA | BSc | BEng | BMid | LLB | HNC | Cert | MA | MSc | MBA | MArch | LLM | MPhil | MRes | PhD | PGCert | PGDip | 合计 |
|------------|----|-----|------|------|-----|-----|------|----|-----|-----|-------|-----|-------|------|-----|--------|-------|------|
| Faculty of Arts, Business and Social Sciences | 87 | 29 | 0 | 0 | 3 | 2 | 0 | 14 | 19 | 2 | 0 | 6 | 2 | 1 | 7 | 3 | 1 | 176 |
| Faculty of Education, Health and Wellbeing | 13 | 36 | 0 | 3 | 0 | 0 | 1 | 3 | 13 | 0 | 0 | 0 | 2 | 1 | 5 | 26 | 6 | 109 |
| Faculty of Science and Engineering | 0 | 32 | 18 | 0 | 0 | 2 | 0 | 1 | 13 | 0 | 1 | 0 | 6 | 5 | 16 | 0 | 0 | 94 |
| Black Country Medical School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **100** | **97** | **18** | **3** | **3** | **4** | **1** | **18** | **45** | **2** | **1** | **6** | **10** | **7** | **28** | **29** | **7** | **379** |

> Reconciliation: Row totals 176+109+94+0=379, Column totals sum to 379. Matches Rule 1 total.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Wolverhampton is organised into 3 faculties (plus the new Black Country Medical School). Each faculty houses 1–3 academic schools. See Section 0.2 for the full hierarchy. Undergraduate provision spans all three faculties; Foundation Year and Sandwich-placement variants are common for full-time UG degrees, expanding the apparent programme count.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Arts, Business and Social Sciences
##### School of Business & Law
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Business Management | <https://www.wlv.ac.uk/courses/ba-hons-business-management> |
| 2 | BA (Hons) Business Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-business-management-with-foundation-year> |
| 3 | BA (Hons) Business Management with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-business-management-with-sandwich-placement> |
| 4 | BA (Hons) Business and Accounting | <https://www.wlv.ac.uk/courses/ba-hons-business-and-accounting> |
| 5 | BA (Hons) Business and Accounting with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-business-and-accounting-with-foundation-year> |
| 6 | BA (Hons) Business and Accounting with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-business-and-accounting-with-sandwich-placement> |
| 7 | BA (Hons) Business and Human Resource Management | <https://www.wlv.ac.uk/courses/ba-hons-business-and-human-resource-management> |
| 8 | BA (Hons) Business and Human Resource Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-business-and-human-resource-management-with-foundation-year> |
| 9 | BA (Hons) Business and Human Resource Management with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-business-and-human-resource-management-with-sandwich-placement> |
| 10 | BA (Hons) Business and Law | <https://www.wlv.ac.uk/courses/ba-hons-business-and-law> |
| 11 | BA (Hons) Business and Law with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-business-and-law-with-foundation-year> |
| 12 | BA (Hons) Business and Law with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-business-and-law-with-sandwich-placement> |
| 13 | BA (Hons) Business and Marketing Management | <https://www.wlv.ac.uk/courses/ba-hons-business-and-marketing-management> |
| 14 | BA (Hons) Business and Marketing Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-business-and-marketing-management-with-foundation-year> |
| 15 | BA (Hons) Business and Marketing Management with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-business-and-marketing-management-with-sandwich-placement> |
| 16 | BA (Hons) Business and Tourism Management | <https://www.wlv.ac.uk/courses/ba-hons-business-and-tourism-management> |
| 17 | BA (Hons) Business and Tourism Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-business-and-tourism-management-with-foundation-year> |
| 18 | BA (Hons) Business and Tourism Management with Sandwich Placement | <https://www.wlv.ac.uk/courses/ba-hons-business-and-tourism-management-with-sandwich-placement> |
| 19 | BA (Hons) Criminology and Criminal Justice | <https://www.wlv.ac.uk/courses/ba-hons-criminology-and-criminal-justice> |
| 20 | BA (Hons) Criminology and Criminal Justice and Law | <https://www.wlv.ac.uk/courses/ba-hons-criminology-and-criminal-justice-and-law> |
| 21 | BA (Hons) Criminology and Criminal Justice and Law with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-criminology-and-criminal-justice-and-law-with-foundation-year> |
| 22 | BA (Hons) Criminology and Criminal Justice with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-criminology-and-criminal-justice-with-foundation-year> |
| 23 | BA (Hons) Digital Marketing Management | <https://www.wlv.ac.uk/courses/ba-hons-digital-marketing-management> |
| 24 | BA (Hons) Digital Marketing Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-digital-marketing-management-with-foundation-year> |
| 25 | BA (Hons) Digital Marketing Management with Sandwich Placement | <https://www.wlv.ac.uk/courses/ba-hons-digital-marketing-management-with-sandwich-placement> |
| 26 | BA (Hons) Economics and Business | <https://www.wlv.ac.uk/courses/ba-hons-economics-and-business> |
| 27 | BA (Hons) Economics and Business with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-economics-and-business-with-foundation-year> |
| 28 | BA (Hons) Economics and Business with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-economics-and-business-with-sandwich-placement> |
| 29 | BA (Hons) Fashion Marketing and Branding | <https://www.wlv.ac.uk/courses/ba-hons-fashion-marketing-and-branding> |
| 30 | BA (Hons) Fashion Marketing and Branding with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-fashion-marketing-and-branding-with-foundation-year> |
| 31 | BA (Hons) Human Resource Management | <https://www.wlv.ac.uk/courses/ba-hons-human-resource-management> |
| 32 | BA (Hons) Human Resource Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-human-resource-management-with-foundation-year> |
| 33 | BA (Hons) Human Resource Management with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-human-resource-management-with-sandwich-placement> |
| 34 | BA (Hons) International Hospitality Management | <https://www.wlv.ac.uk/courses/ba-hons-international-hospitality-management> |
| 35 | BA (Hons) International Hospitality Management with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-international-hospitality-management-with-foundation-year> |
| 36 | BA (Hons) International Hospitality Management with Sandwich placement | <https://www.wlv.ac.uk/courses/ba-hons-international-hospitality-management-with-sandwich-placement> |
| 37 | BA (Hons) Professional Policing | <https://www.wlv.ac.uk/courses/ba-hons-professional-policing> |
| 38 | BA (Hons) Professional Policing with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-professional-policing-with-foundation-year> |
| 39 | BA (Hons) Sociology and Criminology | <https://www.wlv.ac.uk/courses/ba-hons-sociology-and-criminology> |
| 40 | BA (Hons) Sociology and Criminology with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-sociology-and-criminology-with-foundation-year> |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Accounting and Finance | <https://www.wlv.ac.uk/courses/bsc-hons-accounting-and-finance> |
| 2 | BSc (Hons) Accounting and Finance with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-accounting-and-finance-with-foundation-year> |
| 3 | BSc (Hons) Accounting and Finance with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-accounting-and-finance-with-sandwich-placement> |
| 4 | BSc (Hons) Business and Finance | <https://www.wlv.ac.uk/courses/bsc-hons-business-and-finance> |
| 5 | BSc (Hons) Business and Finance with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-business-and-finance-with-foundation-year> |
| 6 | BSc (Hons) Business and Finance with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-business-and-finance-with-sandwich-placement> |
| 7 | BSc (Hons) Economics and Finance | <https://www.wlv.ac.uk/courses/bsc-hons-economics-and-finance> |
| 8 | BSc (Hons) Economics and Finance with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-economics-and-finance-with-foundation-year> |
| 9 | BSc (Hons) Economics and Finance with Sandwich Placement | <https://www.wlv.ac.uk/courses/bsc-hons-economics-and-finance-with-sandwich-placement> |
| 10 | BSc (Hons) International Business Management | <https://www.wlv.ac.uk/courses/bsc-hons-international-business-management> |
| 11 | BSc (Hons) International Business Management with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-international-business-management-with-foundation-year> |
| 12 | BSc (Hons) International Business Management with Sandwich Placement | <https://www.wlv.ac.uk/courses/bsc-hons-international-business-management-with-sandwich-placement> |
| 13 | BSc (Hons) Policing and Intelligence | <https://www.wlv.ac.uk/courses/bsc-hons-policing-and-intelligence> |
| 14 | BSc (Hons) Policing and Intelligence with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-policing-and-intelligence-with-foundation-year> |
| 15 | BSc (Hons) Property Management and Real Estate | <https://www.wlv.ac.uk/courses/bsc-hons-property-management-and-real-estate> |
| 16 | BSc (Hons) Property Management and Real Estate with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-property-management-and-real-estate-with-foundation-year> |
| 17 | BSc (Hons) Property Management and Real Estate with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-property-management-and-real-estate-with-sandwich-placement> |
| 18 | BSc (Hons) Zoo Animal Management and Conservation | <https://www.wlv.ac.uk/courses/bsc-hons-zoo-animal-management-and-conservation> |

###### LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | LLB (Hons) Law | <https://www.wlv.ac.uk/courses/llb-hons-law> |
| 2 | LLB (Hons) Law with Foundation Year | <https://www.wlv.ac.uk/courses/llb-hons-law-with-foundation-year> |
| 3 | LLB (Hons) Law with Sandwich Placement | <https://www.wlv.ac.uk/courses/llb-hons-law-with-sandwich-placement> |

##### School of Social Science, Humanities & Creative Industries
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Animation | <https://www.wlv.ac.uk/courses/ba-hons-animation> |
| 2 | BA (Hons) Animation with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-animation-with-foundation-year> |
| 3 | BA (Hons) British Sign Language | <https://www.wlv.ac.uk/courses/ba-hons-british-sign-language-deaf-studies> |
| 4 | BA (Hons) British Sign Language | <https://www.wlv.ac.uk/courses/ba-hons-british-sign-language-interpreting> |
| 5 | BA (Hons) Creative and Prof Writing with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-creative-and-prof-writing-with-foundation-year> |
| 6 | BA (Hons) Creative and Professional Writing | <https://www.wlv.ac.uk/courses/ba-hons-creative-and-professional-writing> |
| 7 | BA (Hons) Creative and Professional Writing with English Literatures | <https://www.wlv.ac.uk/courses/ba-hons-creative-and-professional-writing-with-english-literatures> |
| 8 | BA (Hons) English Language and Literatures | <https://www.wlv.ac.uk/courses/ba-hons-english-language-and-literatures> |
| 9 | BA (Hons) English Language and Literatures with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-english-language-and-literatures-with-foundation-year> |
| 10 | BA (Hons) English Language and Literatures with Sandwich Placement | <https://www.wlv.ac.uk/courses/ba-hons-english-language-and-literatures-with-sandwich-placement> |
| 11 | BA (Hons) English Literatures | <https://www.wlv.ac.uk/courses/ba-hons-english-literatures> |
| 12 | BA (Hons) English Literatures with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-english-literatures-with-foundation-year> |
| 13 | BA (Hons) English Literatures with Sandwich Placement | <https://www.wlv.ac.uk/courses/ba-hons-english-literatures-with-sandwich-placement> |
| 14 | BA (Hons) Film Production | <https://www.wlv.ac.uk/courses/ba-hons-film-production> |
| 15 | BA (Hons) Film Production with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-film-production-with-foundation-year> |
| 16 | BA (Hons) Film and Television Production | <https://www.wlv.ac.uk/courses/ba-hons-film-and-television-production> |
| 17 | BA (Hons) Film and Television Production | <https://www.wlv.ac.uk/courses/ba-hons-film-and-television-production-top-up> |
| 18 | BA (Hons) Fine Art | <https://www.wlv.ac.uk/courses/ba-hons-fine-art> |
| 19 | BA (Hons) Fine Art with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-fine-art-with-foundation-year> |
| 20 | BA (Hons) Game Design | <https://www.wlv.ac.uk/courses/ba-hons-game-design> |
| 21 | BA (Hons) Game Design with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-game-design-with-foundation-year> |
| 22 | BA (Hons) Graphic Design | <https://www.wlv.ac.uk/courses/ba-hons-graphic-design> |
| 23 | BA (Hons) Graphic Design with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-graphic-design-with-foundation-year> |
| 24 | BA (Hons) History | <https://www.wlv.ac.uk/courses/ba-hons-history> |
| 25 | BA (Hons) History and War Studies | <https://www.wlv.ac.uk/courses/ba-hons-history-and-war-studies> |
| 26 | BA (Hons) History and War Studies with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-history-and-war-studies-with-foundation-year> |
| 27 | BA (Hons) History with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-history-with-foundation-year> |
| 28 | BA (Hons) Illustration | <https://www.wlv.ac.uk/courses/ba-hons-illustration> |
| 29 | BA (Hons) Illustration with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-illustration-with-foundation-year> |
| 30 | BA (Hons) International Relations | <https://www.wlv.ac.uk/courses/ba-hons-international-relations> |
| 31 | BA (Hons) International Relations with Sandwich Placement | <https://www.wlv.ac.uk/courses/ba-hons-international-relations-with-sandwich-placement> |
| 32 | BA (Hons) Journalism | <https://www.wlv.ac.uk/courses/ba-hons-journalism> |
| 33 | BA (Hons) Journalism with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-journalism-with-foundation-year> |
| 34 | BA (Hons) Photography | <https://www.wlv.ac.uk/courses/ba-hons-photography> |
| 35 | BA (Hons) Photography with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-photography-with-foundation-year> |
| 36 | BA (Hons) Politics and History | <https://www.wlv.ac.uk/courses/ba-hons-politics-and-history> |
| 37 | BA (Hons) Politics and History with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-politics-and-history-with-foundation-year> |
| 38 | BA (Hons) Politics and International Relations | <https://www.wlv.ac.uk/courses/ba-hons-politics-and-international-relations> |
| 39 | BA (Hons) Politics and International Relations with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-politics-and-international-relations-with-foundation-year> |
| 40 | BA (Hons) Politics and International Relations with Sandwich Placement | <https://www.wlv.ac.uk/courses/ba-hons-politics-and-international-relations-with-sandwich-placement> |
| 41 | BA (Hons) Social Work | <https://www.wlv.ac.uk/courses/ba-hons-social-work> |
| 42 | BA (Hons) Sociology | <https://www.wlv.ac.uk/courses/ba-hons-sociology> |
| 43 | BA (Hons) Sociology and History | <https://www.wlv.ac.uk/courses/ba-hons-sociology-and-history> |
| 44 | BA (Hons) Sociology and History with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-sociology-and-history-with-foundation-year> |
| 45 | BA (Hons) Sociology with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-sociology-with-foundation-year> |
| 46 | BA (Hons) War Studies | <https://www.wlv.ac.uk/courses/ba-hons-war-studies> |
| 47 | BA (Hons) War Studies with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-war-studies-with-foundation-year> |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Animal Behaviour and Wildlife Conservation | <https://www.wlv.ac.uk/courses/bsc-hons-animal-behaviour-and-wildlife-conservation> |
| 2 | BSc (Hons) Animal Behaviour and Wildlife Conservation with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-animal-behaviour-and-wildlife-conservation-with-sandwich-placement> |
| 3 | BSc (Hons) Fire and Rescue | <https://www.wlv.ac.uk/courses/bsc-hons-fire-and-rescue> |
| 4 | BSc (Hons) Fire and Rescue with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-fire-and-rescue-with-foundation-year> |
| 5 | BSc (Hons) Football Coaching and Performance | <https://www.wlv.ac.uk/courses/bsc-hons-football-coaching-and-performance> |
| 6 | BSc (Hons) Football Coaching and Performance with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-football-coaching-and-performance-with-foundation-year> |
| 7 | BSc (Hons) Medical Sciences | <https://www.wlv.ac.uk/courses/bsc-hons-medical-sciences> |
| 8 | BSc (Hons) Psychology | <https://www.wlv.ac.uk/courses/bsc-hons-psychology> |
| 9 | BSc (Hons) Psychology | <https://www.wlv.ac.uk/courses/bsc-hons-psychology-criminal-behaviour> |
| 10 | BSc (Hons) Psychology and Counselling | <https://www.wlv.ac.uk/courses/bsc-hons-psychology-and-counselling> |
| 11 | BSc (Hons) Psychology with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-psychology-with-foundation-year> |

###### HNC
| # | 专业 | URL |
|---|------|-----|
| 1 | HNC Animal Behaviour and Wildlife Conservation | <https://www.wlv.ac.uk/courses/hnc-animal-behaviour-and-wildlife-conservation> |
| 2 | HNC Building Studies | <https://www.wlv.ac.uk/courses/hnc-building-studies> |

#### Faculty of Education, Health and Wellbeing
##### School of Education & Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Childhood, Family and Education Studies | <https://www.wlv.ac.uk/courses/ba-hons-childhood-family-and-education-studies> |
| 2 | BA (Hons) Childhood, Family and Education Studies with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-childhood-family-and-education-studies-with-foundation-year> |
| 3 | BA (Hons) Early Childhood Studies | <https://www.wlv.ac.uk/courses/ba-hons-early-childhood-studies> |
| 4 | BA (Hons) Early Childhood Studies | <https://www.wlv.ac.uk/courses/ba-hons-early-childhood-studies-top-up> |
| 5 | BA (Hons) Early Childhood Studies with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-early-childhood-studies-with-foundation-year> |
| 6 | BA (Hons) Education Studies | <https://www.wlv.ac.uk/courses/ba-hons-education-studies> |
| 7 | BA (Hons) Education Studies with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-education-studies-with-foundation-year> |
| 8 | BA (Hons) Physical Education and School Sport | <https://www.wlv.ac.uk/courses/ba-hons-physical-education-and-school-sport> |
| 9 | BA (Hons) Primary Education | <https://www.wlv.ac.uk/courses/ba-hons-primary-education> |
| 10 | BA (Hons) Special Educational Needs, Disability and Inclusion | <https://www.wlv.ac.uk/courses/ba-hons-special-educational-needs-disability-and-inclusion> |
| 11 | BA (Hons) Special Educational Needs, Disability and Inclusion with Foundation Year | <https://www.wlv.ac.uk/courses/ba-hons-special-educational-needs-disability-and-inclusion-with-foundation-year> |
| 12 | BA (Hons) Special Educational Needs, Disability, Inclusion and Childhood and Family Studies | <https://www.wlv.ac.uk/courses/ba-hons-special-educational-needs-disability-inclusion-and-childhood-and-family-studies-top-up> |

###### Cert
| # | 专业 | URL |
|---|------|-----|
| 1 | CertEd (PCE) Post Compulsory Education | <https://www.wlv.ac.uk/courses/certed-pce-post-compulsory-education> |

##### School of Nursing and Midwifery
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Adult Nursing | <https://www.wlv.ac.uk/courses/bsc-hons-adult-nursing> |
| 2 | BSc (Hons) Adult Nursing with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-adult-nursing-with-foundation-year> |
| 3 | BSc (Hons) Children's Nursing | <https://www.wlv.ac.uk/courses/bsc-hons-childrens-nursing> |
| 4 | BSc (Hons) Children's Nursing with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-childrens-nursing-with-foundation-year> |
| 5 | BSc (Hons) International Nursing Studies | <https://www.wlv.ac.uk/courses/bsc-hons-international-nursing-studies-top-up> |
| 6 | BSc (Hons) Learning Disability Nursing | <https://www.wlv.ac.uk/courses/bsc-hons-learning-disability-nursing> |
| 7 | BSc (Hons) Learning Disability Nursing with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-learning-disability-nursing-with-foundation-year> |
| 8 | BSc (Hons) Mental Health Nursing | <https://www.wlv.ac.uk/courses/bsc-hons-mental-health-nursing> |
| 9 | BSc (Hons) Mental Health Nursing with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-mental-health-nursing-with-foundation-year> |

###### BMid
| # | 专业 | URL |
|---|------|-----|
| 1 | BMid (Hons) Midwifery | <https://www.wlv.ac.uk/courses/bmid-hons-midwifery> |
| 2 | BMid (Hons) Midwifery | <https://www.wlv.ac.uk/courses/bmid-hons-midwifery-2-year> |
| 3 | BMid (Hons) Midwifery with Foundation Year | <https://www.wlv.ac.uk/courses/bmid-hons-midwifery-with-foundation-year> |

##### School of Health and Wellbeing
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Science Adult Critical Care | <https://www.wlv.ac.uk/courses/bachelor-of-science-adult-critical-care> |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Biomedical Science | <https://www.wlv.ac.uk/courses/bsc-hons-biomedical-science> |
| 2 | BSc (Hons) Biomedical Science with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-biomedical-science-with-foundation-year> |
| 3 | BSc (Hons) Biomedical Science with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-biomedical-science-with-sandwich-placement> |
| 4 | BSc (Hons) Diagnostic Radiography | <https://www.wlv.ac.uk/courses/bsc-hons-diagnostic-radiography> |
| 5 | BSc (Hons) Health and Social Care | <https://www.wlv.ac.uk/courses/bsc-hons-health-and-social-care> |
| 6 | BSc (Hons) Health and Social Care with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-health-and-social-care-with-foundation-year> |
| 7 | BSc (Hons) Healthcare Science | <https://www.wlv.ac.uk/courses/bsc-hons-healthcare-science-cardiac-physiology> |
| 8 | BSc (Hons) Healthcare Science | <https://www.wlv.ac.uk/courses/bsc-hons-healthcare-science-physiological-sciences> |
| 9 | BSc (Hons) Healthcare Science | <https://www.wlv.ac.uk/courses/bsc-hons-healthcare-science-respiratory-and-sleep-physiology> |
| 10 | BSc (Hons) Medical Physiology and Diagnostics | <https://www.wlv.ac.uk/courses/bsc-hons-medical-physiology-and-diagnostics> |
| 11 | BSc (Hons) Medical Physiology and Diagnostics with Sandwich Placement | <https://www.wlv.ac.uk/courses/bsc-hons-medical-physiology-and-diagnostics-with-sandwich-placement> |
| 12 | BSc (Hons) Occupational Therapy | <https://www.wlv.ac.uk/courses/bsc-hons-occupational-therapy> |
| 13 | BSc (Hons) Occupational Therapy with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-occupational-therapy-with-foundation-year> |
| 14 | BSc (Hons) Paramedic Science | <https://www.wlv.ac.uk/courses/bsc-hons-paramedic-science> |
| 15 | BSc (Hons) Paramedic Science with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-paramedic-science-with-foundation-year> |
| 16 | BSc (Hons) Physiotherapy | <https://www.wlv.ac.uk/courses/bsc-hons-physiotherapy> |
| 17 | BSc (Hons) Physiotherapy with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-physiotherapy-with-foundation-year> |
| 18 | BSc (Hons) Podiatry | <https://www.wlv.ac.uk/courses/bsc-hons-podiatry> |
| 19 | BSc (Hons) Podiatry with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-podiatry-with-foundation-year> |
| 20 | BSc (Hons) Public Health | <https://www.wlv.ac.uk/courses/bsc-hons-public-health> |
| 21 | BSc (Hons) Public Health with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-public-health-with-foundation-year> |
| 22 | BSc (Hons) Sport and Exercise Science | <https://www.wlv.ac.uk/courses/bsc-hons-sport-and-exercise-science> |
| 23 | BSc (Hons) Sport and Exercise Science with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-sport-and-exercise-science-with-foundation-year> |
| 24 | BSc (Hons) Sports Coaching | <https://www.wlv.ac.uk/courses/bsc-hons-sports-coaching-top-up> |
| 25 | BSc (Hons) Sports Therapy and Rehabilitation | <https://www.wlv.ac.uk/courses/bsc-hons-sports-therapy-and-rehabilitation> |
| 26 | BSc (Hons) Sports Therapy and Rehabilitation with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-sports-therapy-and-rehabilitation-with-foundation-year> |
| 27 | BSc Professional Practice in Healthcare | <https://www.wlv.ac.uk/courses/bsc-professional-practice-in-healthcare-top-up> |

#### Faculty of Science and Engineering
##### School of Architecture, Computing & Engineering
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Architectural Design Technology | <https://www.wlv.ac.uk/courses/bsc-hons-architectural-design-technology> |
| 2 | BSc (Hons) Architectural Design Technology with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-architectural-design-technology-with-foundation-year> |
| 3 | BSc (Hons) Architectural Design Technology with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-architectural-design-technology-with-sandwich-placement> |
| 4 | BSc (Hons) Architecture | <https://www.wlv.ac.uk/courses/bsc-hons-architecture> |
| 5 | BSc (Hons) Architecture with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-architecture-with-foundation-year> |
| 6 | BSc (Hons) Building Control Surveying | <https://www.wlv.ac.uk/courses/bsc-hons-building-control-surveying-top-up> |
| 7 | BSc (Hons) Building Surveying | <https://www.wlv.ac.uk/courses/bsc-hons-building-surveying> |
| 8 | BSc (Hons) Building Surveying with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-building-surveying-with-foundation-year> |
| 9 | BSc (Hons) Building Surveying with Sandwich Placement | <https://www.wlv.ac.uk/courses/bsc-hons-building-surveying-with-sandwich-placement> |
| 10 | BSc (Hons) Computer Science | <https://www.wlv.ac.uk/courses/bsc-hons-computer-science> |
| 11 | BSc (Hons) Computer Science with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-computer-science-with-foundation-year> |
| 12 | BSc (Hons) Computer Science with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-computer-science-with-sandwich-placement> |
| 13 | BSc (Hons) Computing and Information Technology | <https://www.wlv.ac.uk/courses/bsc-hons-computing-and-information-technology> |
| 14 | BSc (Hons) Computing and Information Technology with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-computing-and-information-technology-with-sandwich-placement> |
| 15 | BSc (Hons) Construction Management | <https://www.wlv.ac.uk/courses/bsc-hons-construction-management> |
| 16 | BSc (Hons) Construction Management with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-construction-management-with-foundation-year> |
| 17 | BSc (Hons) Construction Management with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-construction-management-with-sandwich-placement> |
| 18 | BSc (Hons) Cybersecurity | <https://www.wlv.ac.uk/courses/bsc-hons-cybersecurity> |
| 19 | BSc (Hons) Cybersecurity with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-cybersecurity-with-sandwich-placement> |
| 20 | BSc (Hons) Quantity Surveying | <https://www.wlv.ac.uk/courses/bsc-hons-quantity-surveying> |
| 21 | BSc (Hons) Quantity Surveying with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-quantity-surveying-with-sandwich-placement> |

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | BEng (Hons) Aerospace Engineering | <https://www.wlv.ac.uk/courses/beng-hons-aerospace-engineering> |
| 2 | BEng (Hons) Aerospace Engineering with Foundation Year | <https://www.wlv.ac.uk/courses/beng-hons-aerospace-engineering-with-foundation-year> |
| 3 | BEng (Hons) Aerospace Engineering with Pilot Studies | <https://www.wlv.ac.uk/courses/beng-hons-aerospace-engineering-with-pilot-studies> |
| 4 | BEng (Hons) Aerospace Engineering with Pilot Studies with Foundation Year | <https://www.wlv.ac.uk/courses/beng-hons-aerospace-engineering-with-pilot-studies-with-foundation-year> |
| 5 | BEng (Hons) Aerospace Engineering with Sandwich placement | <https://www.wlv.ac.uk/courses/beng-hons-aerospace-engineering-with-sandwich-placement> |
| 6 | BEng (Hons) Chemical Engineering | <https://www.wlv.ac.uk/courses/beng-hons-chemical-engineering> |
| 7 | BEng (Hons) Chemical Engineering with Foundation Year | <https://www.wlv.ac.uk/courses/beng-hons-chemical-engineering-with-foundation-year> |
| 8 | BEng (Hons) Civil Engineering | <https://www.wlv.ac.uk/courses/beng-hons-civil-engineering> |
| 9 | BEng (Hons) Civil Engineering with Sandwich placement | <https://www.wlv.ac.uk/courses/beng-hons-civil-engineering-with-sandwich-placement> |
| 10 | BEng (Hons) Civil and Transportation Engineering | <https://www.wlv.ac.uk/courses/beng-hons-civil-and-transportation-engineering> |
| 11 | BEng (Hons) Civil and Transportation Engineering with Foundation Year | <https://www.wlv.ac.uk/courses/beng-hons-civil-and-transportation-engineering-with-foundation-year> |
| 12 | BEng (Hons) Civil and Transportation Engineering with Sandwich placement | <https://www.wlv.ac.uk/courses/beng-hons-civil-and-transportation-engineering-with-sandwich-placement> |
| 13 | BEng (Hons) Mechanical Engineering | <https://www.wlv.ac.uk/courses/beng-hons-mechanical-engineering> |
| 14 | BEng (Hons) Mechanical Engineering with Foundation Year | <https://www.wlv.ac.uk/courses/beng-hons-mechanical-engineering-with-foundation-year> |
| 15 | BEng (Hons) Mechanical Engineering with Sandwich placement | <https://www.wlv.ac.uk/courses/beng-hons-mechanical-engineering-with-sandwich-placement> |
| 16 | BEng (Hons) Motorsport and Automotive Engineering | <https://www.wlv.ac.uk/courses/beng-hons-motorsport-and-automotive-engineering> |
| 17 | BEng (Hons) Motorsport and Automotive Engineering with Foundation Year | <https://www.wlv.ac.uk/courses/beng-hons-motorsport-and-automotive-engineering-with-foundation-year> |
| 18 | BEng (Hons) Motorsport and Automotive Engineering with Sandwich Placement | <https://www.wlv.ac.uk/courses/beng-hons-motorsport-and-automotive-engineering-with-sandwich-placement> |

###### HNC
| # | 专业 | URL |
|---|------|-----|
| 1 | HNC Architectural Studies | <https://www.wlv.ac.uk/courses/hnc-architectural-studies> |
| 2 | HNC Civil Engineering Studies | <https://www.wlv.ac.uk/courses/hnc-civil-engineering-studies> |

##### School of Pharmacy & Life Sciences
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Forensic Science | <https://www.wlv.ac.uk/courses/bsc-hons-forensic-science> |
| 2 | BSc (Hons) Forensic Science with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-forensic-science-with-foundation-year> |
| 3 | BSc (Hons) Forensic Science with Policing | <https://www.wlv.ac.uk/courses/bsc-hons-forensic-science-with-policing> |
| 4 | BSc (Hons) Forensic Science with Policing with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-forensic-science-with-policing-with-foundation-year> |
| 5 | BSc (Hons) Forensic Science with Policing with Sandwich Placement | <https://www.wlv.ac.uk/courses/bsc-hons-forensic-science-with-policing-with-sandwich-placement> |
| 6 | BSc (Hons) Forensic Science with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-forensic-science-with-sandwich-placement> |
| 7 | BSc (Hons) Pharmaceutical Science | <https://www.wlv.ac.uk/courses/bsc-hons-pharmaceutical-science> |
| 8 | BSc (Hons) Pharmaceutical Science with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-pharmaceutical-science-with-foundation-year> |
| 9 | BSc (Hons) Pharmacology | <https://www.wlv.ac.uk/courses/bsc-hons-pharmacology> |
| 10 | BSc (Hons) Pharmacology with Foundation Year | <https://www.wlv.ac.uk/courses/bsc-hons-pharmacology-with-foundation-year> |
| 11 | BSc (Hons) Pharmacology with Sandwich placement | <https://www.wlv.ac.uk/courses/bsc-hons-pharmacology-with-sandwich-placement> |


### 1.3 Minors / short courses

The University does not publish a unified minor list; minors are typically embedded in single-honours UG programmes and not catalogued separately. Short courses / CPD live under `/courses/continuing-professional-development-cpd-short-courses/` and are excluded from this count.

### 1.4 Foundation / Sandwich / Top-up variants

Many UG courses are offered in three formats that count as separate catalogue entries:

- **with Foundation Year** — additional year for students without traditional entry qualifications
- **with Sandwich placement** — 4-year UG with a year in industry
- **Top up** — 1-year completion awards for holders of HND / DipHE

These variants are all enumerated in Section 1.2 above; they share the same school/department as their parent programme.

### 1.5 Course-ID → Major quick-lookup

The University does not use a numeric course-ID system. Slugs are human-readable and derived from the programme name (e.g. `bsc-hons-accounting-and-finance-with-foundation-year`).

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programmes — grouped by 学院 > 系 > 学位级别

#### Faculty of Arts, Business and Social Sciences
##### School of Business & Law
###### MA
| # | 专业 | URL |
|---|------|-----|
| 1 | MA Comparative Criminology | <https://www.wlv.ac.uk/courses/ma-comparative-criminology> |
| 2 | MA International Tourism & Hospitality Management - Extended | <https://www.wlv.ac.uk/courses/ma-international-tourism--hospitality-management---extended> |
| 3 | MA International Tourism and Hospitality Management | <https://www.wlv.ac.uk/courses/ma-international-tourism-and-hospitality-management> |
| 4 | MA Strategic People Management and Human Resources | <https://www.wlv.ac.uk/courses/ma-strategic-people-management-and-human-resources> |
| 5 | MA Strategic People Management and Human Resources | <https://www.wlv.ac.uk/courses/ma-strategic-people-management-and-human-resources-extended> |
| 6 | MA Strategic People Management and Human Resources | <https://www.wlv.ac.uk/courses/ma-strategic-people-management-and-human-resources-top-up> |

###### MSc
| # | 专业 | URL |
|---|------|-----|
| 1 | MSc Business Analytics | <https://www.wlv.ac.uk/courses/msc-business-analytics> |
| 2 | MSc Digital Marketing Management | <https://www.wlv.ac.uk/courses/msc-digital-marketing-management> |
| 3 | MSc Digital Marketing Management - Extended | <https://www.wlv.ac.uk/courses/msc-digital-marketing-management---extended> |
| 4 | MSc Disaster Management & Resilience | <https://www.wlv.ac.uk/courses/msc-disaster-management--resilience> |
| 5 | MSc Emergency Management and Resilience | <https://www.wlv.ac.uk/courses/msc-emergency-management-and-resilience> |
| 6 | MSc Finance and Accounting | <https://www.wlv.ac.uk/courses/msc-finance-and-accounting> |
| 7 | MSc Finance and Accounting - Extended | <https://www.wlv.ac.uk/courses/msc-finance-and-accounting---extended> |
| 8 | MSc Innovation and Entrepreneurship | <https://www.wlv.ac.uk/courses/msc-innovation-and-entrepreneurship> |
| 9 | MSc Innovation and Entrepreneurship - Extended | <https://www.wlv.ac.uk/courses/msc-innovation-and-entrepreneurship---extended> |
| 10 | MSc International Business Management | <https://www.wlv.ac.uk/courses/msc-international-business-management> |
| 11 | MSc International Business Management - Extended | <https://www.wlv.ac.uk/courses/msc-international-business-management---extended> |
| 12 | MSc Leadership and Management | <https://www.wlv.ac.uk/courses/msc-leadership-and-management> |
| 13 | MSc Leadership and Management - Extended | <https://www.wlv.ac.uk/courses/msc-leadership-and-management---extended> |
| 14 | MSc Organisational and Business Psychology | <https://www.wlv.ac.uk/courses/msc-organisational-and-business-psychology> |
| 15 | MSc Professional Accounting and Finance | <https://www.wlv.ac.uk/courses/msc-professional-accounting-and-finance-acca> |
| 16 | MSc Professional Accounting and Finance - Extended | <https://www.wlv.ac.uk/courses/msc-professional-accounting-and-finance---extended-acca> |
| 17 | MSc Project Management | <https://www.wlv.ac.uk/courses/msc-project-management> |

###### MBA
| # | 专业 | URL |
|---|------|-----|
| 1 | MBA Business Administration | <https://www.wlv.ac.uk/courses/mba-business-administration> |
| 2 | MBA Business Administration - Extended | <https://www.wlv.ac.uk/courses/mba-business-administration---extended> |

###### MPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhil Business | <https://www.wlv.ac.uk/courses/mphil-business> |

###### MRes
| # | 专业 | URL |
|---|------|-----|
| 1 | MRes Business and Management | <https://www.wlv.ac.uk/courses/mres-business-and-management> |

###### PhD
| # | 专业 | URL |
|---|------|-----|
| 1 | PhD Postgraduate research in Business | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-business> |
| 2 | PhD Postgraduate research in Law | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-law> |
| 3 | PhD Postgraduate research in Library and Information Management | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-library-and-information-management> |

###### LLM
| # | 专业 | URL |
|---|------|-----|
| 1 | LLM International Business Law | <https://www.wlv.ac.uk/courses/llm-international-business-law> |
| 2 | LLM Law | <https://www.wlv.ac.uk/courses/llm-law> |
| 3 | LLM Law Conversion | <https://www.wlv.ac.uk/courses/llm-law-conversion> |
| 4 | LLM Law and Human Resource Management | <https://www.wlv.ac.uk/courses/llm-law-and-human-resource-management> |
| 5 | LLM Law and Practice | <https://www.wlv.ac.uk/courses/llm-law-and-practice> |
| 6 | LLM Professional Practice | <https://www.wlv.ac.uk/courses/llm-professional-practice-top-up> |

###### PGCert
| # | 专业 | URL |
|---|------|-----|
| 1 | PG Cert Emergency Management & Resilience | <https://www.wlv.ac.uk/courses/pg-cert-emergency-management--resilience> |

###### PGDip
| # | 专业 | URL |
|---|------|-----|
| 1 | PGDip Strategic People Management & Human Resources | <https://www.wlv.ac.uk/courses/pgdip-strategic-people-management--human-resources> |

##### School of Social Science, Humanities & Creative Industries
###### MA
| # | 专业 | URL |
|---|------|-----|
| 1 | MA Digital and Visual Communications | <https://www.wlv.ac.uk/courses/ma-digital-and-visual-communications> |
| 2 | MA Film and Television Production | <https://www.wlv.ac.uk/courses/ma-film-and-television-production> |
| 3 | MA History | <https://www.wlv.ac.uk/courses/ma-history-first-world-war> |
| 4 | MA History | <https://www.wlv.ac.uk/courses/ma-history-second-world-war-conflict-societies-holocaust> |
| 5 | MA Interpreting | <https://www.wlv.ac.uk/courses/ma-interpreting> |
| 6 | MA Interpreting | <https://www.wlv.ac.uk/courses/ma-interpreting-top-up> |
| 7 | MA Military History by Distance Learning | <https://www.wlv.ac.uk/courses/ma-military-history-by-distance-learning> |
| 8 | MA Social Work | <https://www.wlv.ac.uk/courses/ma-social-work> |

###### MSc
| # | 专业 | URL |
|---|------|-----|
| 1 | MSc Integrative Counselling & Psychotherapy | <https://www.wlv.ac.uk/courses/msc-integrative-counselling-and-psychotherapy> |
| 2 | MSc International Relations | <https://www.wlv.ac.uk/courses/msc-international-relations> |

###### MPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhil Social Sciences | <https://www.wlv.ac.uk/courses/mphil-social-sciences> |

###### PhD
| # | 专业 | URL |
|---|------|-----|
| 1 | PhD Postgraduate Research in Art and Design | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-art-and-design> |
| 2 | PhD Postgraduate research in English Language and Literature | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-english-language-and-literature> |
| 3 | PhD Postgraduate research in Media and Communications | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-media-and-communications> |
| 4 | PhD Postgraduate research in Social Sciences | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-social-sciences> |

###### PGCert
| # | 专业 | URL |
|---|------|-----|
| 1 | PG Cert Interpreting | <https://www.wlv.ac.uk/courses/pg-cert-interpreting> |
| 2 | PG Cert Prescribing Studies | <https://www.wlv.ac.uk/courses/pg-cert-prescribing-studies> |

#### Faculty of Education, Health and Wellbeing
##### School of Education & Psychology
###### MA
| # | 专业 | URL |
|---|------|-----|
| 1 | MA Education | <https://www.wlv.ac.uk/courses/ma-education> |

###### MPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhil Education | <https://www.wlv.ac.uk/courses/mphil-education> |

###### PhD
| # | 专业 | URL |
|---|------|-----|
| 1 | PhD Postgraduate research in Education | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-education> |
| 2 | PhD Postgraduate research in Psychology | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-psychology> |

###### PGCert
| # | 专业 | URL |
|---|------|-----|
| 1 | PG Cert Academic Practice in Higher Education | <https://www.wlv.ac.uk/courses/pg-cert-academic-practice-in-higher-education> |
| 2 | PG Cert Postgraduate Certificate Mentoring and Coaching for Further and Higher Education Professionals | <https://www.wlv.ac.uk/courses/pg-cert-postgraduate-certificate-mentoring-and-coaching-for-further-and-higher-education-professionals> |
| 3 | PGCE Further Education | <https://www.wlv.ac.uk/courses/pgce-further-education> |
| 4 | PGCE Primary Education | <https://www.wlv.ac.uk/courses/pgce-primary-education> |
| 5 | PGCE Primary Education with Mathematics | <https://www.wlv.ac.uk/courses/pgce-primary-education-with-mathematics> |
| 6 | PGCE Secondary Education: Art and Design | <https://www.wlv.ac.uk/courses/pgce-secondary-education-art-and-design> |
| 7 | PGCE Secondary Education: Biology | <https://www.wlv.ac.uk/courses/pgce-secondary-education-biology> |
| 8 | PGCE Secondary Education: Chemistry | <https://www.wlv.ac.uk/courses/pgce-secondary-education-chemistry> |
| 9 | PGCE Secondary Education: Computing | <https://www.wlv.ac.uk/courses/pgce-secondary-education-computing> |
| 10 | PGCE Secondary Education: Dance | <https://www.wlv.ac.uk/courses/pgce-secondary-education-dance> |
| 11 | PGCE Secondary Education: Design Technology | <https://www.wlv.ac.uk/courses/pgce-secondary-education-design-technology> |
| 12 | PGCE Secondary Education: Engineers Teach Physics | <https://www.wlv.ac.uk/courses/pgce-secondary-education-engineers-teach-physics> |
| 13 | PGCE Secondary Education: English | <https://www.wlv.ac.uk/courses/pgce-secondary-education-english> |
| 14 | PGCE Secondary Education: Geography | <https://www.wlv.ac.uk/courses/pgce-secondary-education-geography> |
| 15 | PGCE Secondary Education: History | <https://www.wlv.ac.uk/courses/pgce-secondary-education-history> |
| 16 | PGCE Secondary Education: Mathematics | <https://www.wlv.ac.uk/courses/pgce-secondary-education-mathematics> |
| 17 | PGCE Secondary Education: Physical Education | <https://www.wlv.ac.uk/courses/pgce-secondary-education-physical-education> |
| 18 | PGCE Secondary Education: Physical Education with EBacc | <https://www.wlv.ac.uk/courses/pgce-secondary-education-physical-education-with-ebacc> |
| 19 | PGCE Secondary Education: Physics | <https://www.wlv.ac.uk/courses/pgce-secondary-education-physics> |
| 20 | PGCE Secondary Education: Psychology | <https://www.wlv.ac.uk/courses/pgce-secondary-education-psychology> |
| 21 | PGCE Secondary Education: Social Sciences | <https://www.wlv.ac.uk/courses/pgce-secondary-education-social-sciences> |

##### School of Nursing and Midwifery
###### MA
| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Adult Nursing | <https://www.wlv.ac.uk/courses/master-of-adult-nursing> |
| 2 | Master of Mental Health Nursing | <https://www.wlv.ac.uk/courses/master-of-mental-health-nursing> |

###### PGCert
| # | 专业 | URL |
|---|------|-----|
| 1 | PG Cert Fundamentals of General Practice Nursing | <https://www.wlv.ac.uk/courses/pg-cert-fundamentals-of-general-practice-nursing> |
| 2 | PG Cert Non-Medical Prescribing for Nurses, Midwives and Allied Health Professionals | <https://www.wlv.ac.uk/courses/pg-cert-non-medical-prescribing-for-nurses-midwives-and-allied-health-professionals> |

###### PGDip
| # | 专业 | URL |
|---|------|-----|
| 1 | PGDip Adult Nursing | <https://www.wlv.ac.uk/courses/pgdip-adult-nursing> |
| 2 | PGDip Community Nursing Specialist Practice Qualification | <https://www.wlv.ac.uk/courses/pgdip-community-nursing-specialist-practice-qualification-district-nursing> |
| 3 | PGDip Community Nursing Specialist Practice Qualification | <https://www.wlv.ac.uk/courses/pgdip-community-nursing-specialist-practice-qualification-general-practice-nursing> |
| 4 | PGDip Mental Health Nursing | <https://www.wlv.ac.uk/courses/pgdip-mental-health-nursing> |
| 5 | PGDip Specialist Community Public Health Nurse | <https://www.wlv.ac.uk/courses/pgdip-specialist-community-public-health-nurse-health-visitor> |
| 6 | PGDip Specialist Community Public Health Nurse | <https://www.wlv.ac.uk/courses/pgdip-specialist-community-public-health-nurse-school-nurse> |

##### School of Health and Wellbeing
###### MSc
| # | 专业 | URL |
|---|------|-----|
| 1 | MSc Adult Critical Care | <https://www.wlv.ac.uk/courses/msc-adult-critical-care> |
| 2 | MSc Advanced Clinical Practice | <https://www.wlv.ac.uk/courses/msc-advanced-clinical-practice-specialist-negotiated-practice> |
| 3 | MSc Advanced Clinical Practice | <https://www.wlv.ac.uk/courses/msc-advanced-clinical-practice-with-v300-non-medical-prescribing> |
| 4 | MSc Biomedical Science | <https://www.wlv.ac.uk/courses/msc-biomedical-science> |
| 5 | MSc Health and Social Care | <https://www.wlv.ac.uk/courses/msc-health-and-social-care> |
| 6 | MSc Health and Wellbeing | <https://www.wlv.ac.uk/courses/msc-health-and-wellbeing-top-up> |
| 7 | MSc Occupational Therapy | <https://www.wlv.ac.uk/courses/msc-occupational-therapy-pre-registration> |
| 8 | MSc Physiotherapy | <https://www.wlv.ac.uk/courses/msc-physiotherapy> |
| 9 | MSc Primary Health Care | <https://www.wlv.ac.uk/courses/msc-primary-health-care-top-up> |
| 10 | MSc Professional Practice in Healthcare | <https://www.wlv.ac.uk/courses/msc-professional-practice-in-healthcare-leadership-and-management> |
| 11 | MSc Professional Practice in Healthcare | <https://www.wlv.ac.uk/courses/msc-professional-practice-in-healthcare-speciality-practice> |
| 12 | MSc Professional Practice in Healthcare | <https://www.wlv.ac.uk/courses/msc-professional-practice-in-healthcare-teaching-and-learning> |
| 13 | MSc Professional Practice in Healthcare | <https://www.wlv.ac.uk/courses/msc-professional-practice-in-healthcare-with-v300> |

###### MPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhil Sports and Recreation | <https://www.wlv.ac.uk/courses/mphil-sports-and-recreation> |

###### MRes
| # | 专业 | URL |
|---|------|-----|
| 1 | MRes Public Health | <https://www.wlv.ac.uk/courses/mres-public-health> |

###### PhD
| # | 专业 | URL |
|---|------|-----|
| 1 | PhD Postgraduate Research in Social Work and Social Care | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-social-work-and-social-care> |
| 2 | PhD Postgraduate research in Health | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-health> |
| 3 | PhD Postgraduate research in Sports and Recreation | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-sports-and-recreation> |

###### PGCert
| # | 专业 | URL |
|---|------|-----|
| 1 | PG Cert Adult Critical Care | <https://www.wlv.ac.uk/courses/pg-cert-adult-critical-care> |
| 2 | PG Cert Mental Health Practice | <https://www.wlv.ac.uk/courses/pg-cert-mental-health-practice-for-approved-mental-health-professionals> |
| 3 | PG Cert Professional Practice in Healthcare | <https://www.wlv.ac.uk/courses/pg-cert-professional-practice-in-healthcare> |

#### Faculty of Science and Engineering
##### School of Architecture, Computing & Engineering
###### MA
| # | 专业 | URL |
|---|------|-----|
| 1 | MA Air, Space and Cyber Power Studies | <https://www.wlv.ac.uk/courses/ma-air-space-and-cyber-power-studies> |

###### MSc
| # | 专业 | URL |
|---|------|-----|
| 1 | MSc Artificial Intelligence | <https://www.wlv.ac.uk/courses/msc-artificial-intelligence> |
| 2 | MSc Civil Engineering | <https://www.wlv.ac.uk/courses/msc-civil-engineering> |
| 3 | MSc Computer Science | <https://www.wlv.ac.uk/courses/msc-computer-science> |
| 4 | MSc Computer Science with Professional Practice | <https://www.wlv.ac.uk/courses/msc-computer-science-with-professional-practice> |
| 5 | MSc Construction Project Management | <https://www.wlv.ac.uk/courses/msc-construction-project-management> |
| 6 | MSc Construction Project Management with Professional Practice Placement | <https://www.wlv.ac.uk/courses/msc-construction-project-management-with-professional-practice-placement> |
| 7 | MSc Cyber Security | <https://www.wlv.ac.uk/courses/msc-cyber-security> |
| 8 | MSc Cyber Security with Professional Practice | <https://www.wlv.ac.uk/courses/msc-cyber-security-with-professional-practice> |
| 9 | MSc Data Science | <https://www.wlv.ac.uk/courses/msc-data-science> |
| 10 | MSc Engineering Management | <https://www.wlv.ac.uk/courses/msc-engineering-management> |
| 11 | MSc Mechanical Engineering | <https://www.wlv.ac.uk/courses/msc-mechanical-engineering> |
| 12 | MSc Mechanical Engineering with Professional Practice | <https://www.wlv.ac.uk/courses/msc-mechanical-engineering-with-professional-practice> |

###### MArch
| # | 专业 | URL |
|---|------|-----|
| 1 | MArch Architecture | <https://www.wlv.ac.uk/courses/march-architecture> |

###### MPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhil Linguistics | <https://www.wlv.ac.uk/courses/mphil-linguistics> |
| 2 | MPhil Postgraduate Research in Humanities | <https://www.wlv.ac.uk/courses/mphil-postgraduate-research-in-humanities> |
| 3 | MPhil Postgraduate research in Computing and Mathematics | <https://www.wlv.ac.uk/courses/mphil-postgraduate-research-in-computing-and-mathematics-master-of-philosophy> |

###### MRes
| # | 专业 | URL |
|---|------|-----|
| 1 | MRes Artificial Intelligence | <https://www.wlv.ac.uk/courses/mres-artificial-intelligence> |
| 2 | MRes Cyber Security | <https://www.wlv.ac.uk/courses/mres-cyber-security> |
| 3 | MRes Data Science | <https://www.wlv.ac.uk/courses/mres-data-science> |
| 4 | MRes International Relations | <https://www.wlv.ac.uk/courses/mres-international-relations> |
| 5 | MRes Mechanical Engineering | <https://www.wlv.ac.uk/courses/mres-mechanical-engineering> |

###### PhD
| # | 专业 | URL |
|---|------|-----|
| 1 | PhD Computing and Mathematics | <https://www.wlv.ac.uk/courses/phd-computing-and-mathematics> |
| 2 | PhD Postgraduate Research in Chemistry | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-chemistry> |
| 3 | PhD Postgraduate Research in Humanities | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-humanities> |
| 4 | PhD Postgraduate Research in Philosophy | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-philosophy> |
| 5 | PhD Postgraduate research in Botany | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-botany> |
| 6 | PhD Postgraduate research in Built Environment | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-built-environment> |
| 7 | PhD Postgraduate research in Computer Science | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-computer-science> |
| 8 | PhD Postgraduate research in Engineering | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-engineering> |
| 9 | PhD Postgraduate research in Environmental and Analytical Sciences | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-environmental-and-analytical-sciences> |
| 10 | PhD Postgraduate research in History | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-history> |
| 11 | PhD Postgraduate research in Humanities: Linguistics | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-humanities-linguistics> |

##### School of Pharmacy & Life Sciences
###### MSc
| # | 专业 | URL |
|---|------|-----|
| 1 | MSc Applied Microbiology and Biotechnology | <https://www.wlv.ac.uk/courses/msc-applied-microbiology-and-biotechnology> |

###### MPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhil Postgraduate Research in Biological Sciences | <https://www.wlv.ac.uk/courses/mphil-postgraduate-research-in-biological-sciences-master-of-philosophy> |
| 2 | MPhil Postgraduate Research in Pharmacy | <https://www.wlv.ac.uk/courses/mphil-postgraduate-research-in-pharmacy-master-of-philosophy> |
| 3 | MPhil Postgraduate research in Biomedical Sciences | <https://www.wlv.ac.uk/courses/mphil-postgraduate-research-in-biomedical-sciences-master-of-philosophy> |

###### PhD
| # | 专业 | URL |
|---|------|-----|
| 1 | PhD Postgraduate research in Biological Sciences | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-biological-sciences> |
| 2 | PhD Postgraduate research in Biomedical Sciences | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-biomedical-sciences> |
| 3 | PhD Postgraduate research in Microbiology | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-microbiology> |
| 4 | PhD Postgraduate research in Molecular Biology | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-molecular-biology> |
| 5 | PhD Postgraduate research in Pharmacy | <https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-pharmacy> |


### 2.2 Postgraduate research degrees (worked example)

Sample: **PhD Postgraduate Research in Computer Science** (`https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-computer-science/`)
- **Home school**: School of Architecture, Computing & Engineering
- **Faculty**: Faculty of Science and Engineering
- **Award**: PhD
- **Duration**: 3–4 years full-time / 5–6 years part-time
- **Entry**: A Master's degree (or equivalent) in a relevant discipline; applicants without a Master's may be considered for MPhil first
- **Application portal**: Direct to University (see https://www.wlv.ac.uk/research/)
- **Fees (international 2026/2027)**: Lab-based £19,859/yr (research degrees fall under lab-based category)
- **English requirement**: IELTS 6.5 (min 6.0 in each component) for most research degrees

### 2.3 Graduate admissions model

The University operates a **centralised admissions office** with a single application portal. All taught postgraduate, postgraduate research, and MPhil/PhD applications route through the central Postgraduate Research Admissions or Postgraduate Taught Admissions teams (see https://www.wlv.ac.uk/research/postgraduate-research-degrees/ and https://www.wlv.ac.uk/courses/postgraduate/). Some professional programmes (e.g. PGCE, healthcare pre-registration) have additional application steps (UCAS, NHS processes).

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| Application portal | UCAS (https://www.ucas.com/) — institution code **W75** |
| Admissions site | https://www.wlv.ac.uk/apply/how-to-apply/ |
| UCAS Extra / Clearing | Open via main UCAS process; Wolverhampton participates in Clearing (https://www.wlv.ac.uk/clearing/) |
| UCAS Equal Consideration Deadline (2026 entry) | Late January (UCAS-wide); check UCAS for exact date |
| Decision notification | Rolling; UCAS standard timeline |
| Enrollment confirmation deadline | Per UCAS standard (early September) |
| Interview policy | Programme-specific; Nursing/Midwifery/Health/Teaching/Pharmacy typically interview |
| Recommendation requirements | Typically 1 academic reference for UG via UCAS |
| Personal statement | UCAS personal statement (up to 4,000 characters) |
| Portfolio | Required for Art, Design, Architecture, Media programmes |
| Standardised tests | **No SAT/ACT required for UK/EU applicants.** International applicants demonstrate English via Section 3.2 below. |
| Foundation Year | Available for most UG programmes — adds 1 year before Year 1 |
| Sandwich placement | Available for most UG programmes — adds a year in industry |

### 3.2 Undergraduate & Postgraduate English proficiency table

The University of Wolverhampton accepts a broad range of English-language tests. Four reference bands are used (see source for exact mapping per programme):

| Exam | Band A (lowest) | Band B | Band C | Band D (highest) |
|------|----------------|--------|--------|------------------|
| **IELTS Academic** (and IELTS Online) | Overall 6.0, no component below 5.5 | Overall 6.5, no component below 6.0 | Overall 7.0, no component below 6.0 | Overall 7.0, no component below 6.5 |
| **Cambridge English / C1 Advanced** | Overall 169, no component below 162 | Overall 176, no component below 169 | Overall 190, no component below 169 | Overall 190, no component below 176 |
| **Cambridge IGCSE (1st or 2nd Language)** | Grade C, no component below D | Grade C, no component below C | Grade B, no component below C | Grade B, no component below B |
| **English Language Level Test (ELLT)** — Oxford International Digital Institute | Overall 6, no component below 5 | Overall 7, no component below 6 | Overall 8, no component below 6 | Overall 8, no component below 8 |
| **GCE O-Level English** | Grade C | Grade C | Grade B | Grade B |
| **PTE Academic** (Pearson) | Overall 59, no component below 59 | Overall 65, no component below 59 | Overall 75, no component below 59 | Overall 75, no component below 65 |
| **TOEFL iBT** (before 21 Jan 2026) | Overall 67, no component below 17 | Overall 72, no component below 17 | Overall 94, no component below 22 | Overall 94, no component below 24 |
| **TOEFL iBT** (after 21 Jan 2026) | TBC | TBC | TBC | TBC |
| **TOEFL ITP** | Not Accepted | Not Accepted | Not Accepted | Not Accepted |
| **Duolingo English Test (DET)** | Overall 110, no component below 100 | Overall 120, no component below 110 | Overall 130, no component below 110 | Overall 130, no component below 120 |
| **GEMS Middle East** | Merit | Distinction | N/A | N/A |
| **Occupational English Test (OET)** | Grade C+, overall 300+, no component below 250 | Grade B, overall 350+, no component below 250 | Grade B, overall 350+, no component below 250 | Grade B, overall 350+, no component below 300 |
| **LanguageCert Academic** (in-person & online) | Overall 65, no component below 60 | Overall 70, no component below 60 | Overall 75, no component below 60 | Overall 75, no component below 65 |
| **Trinity ISE II** | PPPP in 4 components | DDMM in 4 components | N/A | N/A |
| **Trinity ISE III** | PPPP in 4 components | PPPP in 4 components | DDMM in 4 components | DDDM in 4 components |
| **Trinity ISE IV** | PPPP in 4 components | PPPP in 4 components | PPPP in 4 components | PPPM in 4 components |

> Band A (IELTS 6.0/5.5) is the minimum most UG programmes accept. Many professional programmes (Nursing, Midwifery, Teaching, Pharmacy) require higher bands. See individual course pages for programme-specific requirements.

> TOEFL iBT (post-21 Jan 2026) scores are listed as TBC by the University — applicants should check back closer to application.

### 3.3 Graduate — global rules

| 维度 | 详情 |
|------|------|
| Admissions model | Centralised; single application for all PG taught and research programmes |
| Application portal | Direct to University via online portal (https://www.wlv.ac.uk/apply/) |
| Standard application fee | Typically £0 for online applications; some international applications may incur a non-refundable fee (verify per programme) |
| PGCE / Teacher Training | Apply via UCAS (Undergraduate) or via the University portal (Postgraduate); see https://www.wlv.ac.uk/courses/undergraduate/teaching/ |
| Healthcare programmes (Nursing, Midwifery, Allied Health) | Apply through UCAS for UG; PG pre-registration (e.g. MSc Occupational Therapy, MSc Physiotherapy) apply directly to the University |
| GRE / GMAT | Not required for most programmes; MBA may request work experience in lieu of GMAT |
| CGS April-15-equivalent honor date | The University is a signatory to the QAA UK Quality Code and adheres to Research Council deadlines for funded research studentships |
| English-language test | See Section 3.2 — same bands apply to PG |
| Application timeline | Rolling for most PG programmes; research degrees (MPhil/PhD) have no fixed deadline but funding applications typically close Jan/Feb for Oct start |

---

## SECTION 4 — Costs & financial aid (2026/2027 academic year)

### 4.1 Undergraduate cost (international fees, line-itemized)

International tuition fees for the 2026/2027 academic year:

| Expense item | Amount (per year) | Description |
|--------------|-------------------|-------------|
| Tuition Fee (UG, Non-Lab-Based) | £17,600 | Most UG programmes (Business, Law, Social Sciences, Humanities, Education, Nursing) |
| Tuition Fee (UG, Lab-Based) | £18,700 | UG programmes with lab/clinical components (Science, Engineering, Pharmacy, Biomedical, some Health) |
| Living costs (estimate) | ~£9,207 / yr (UKVI requirement) | London-based estimate; Wolverhampton is significantly below London average |
| **Total estimated UG (non-lab, intl)** | **~£26,807 / yr** | Tuition + UKVI living cost |
| **Total estimated UG (lab-based, intl)** | **~£27,907 / yr** | Tuition + UKVI living cost |

> Home (UK) students: tuition capped at £9,535 (2025/26) for standard UG; Nursing, Midwifery, and some Health programmes are paid for by the NHS via the Learning Support Fund.

### 4.2 Postgraduate cost (international fees, 2026/2027)

| Expense item | Amount (per year) | Description |
|--------------|-------------------|-------------|
| Tuition Fee (PG Taught, Non-Lab-Based) | £18,645 | Most MA / MSc / MBA / LLM programmes |
| Tuition Fee (PG Taught, Lab-Based) | £19,859 | Lab-based MSc programmes (Science, Engineering, Computing with hardware, Pharmacy) |
| PG Research (MPhil / PhD) | Lab-based band (£19,859) applies | Research degrees fall under lab-based category |
| **Total estimated PGT (non-lab, intl)** | **~£27,852 / yr** | Tuition + UKVI living cost |
| **Total estimated PGT (lab, intl)** | **~£29,066 / yr** | Tuition + UKVI living cost |

### 4.3 Financial-aid policy

The University offers a range of scholarships and bursaries (see https://www.wlv.ac.uk/apply/funding-costs-fees-and-support/financial-support/scholarships/):

- **Academic Excellence Undergraduate Scholarship** — merit-based fee reduction
- **Academic Excellence Postgraduate Scholarship** — merit-based PG fee reduction
- **International Postgraduate Scholarship**
- **Global Opportunities Undergraduate Regional Scholarship** — region-specific
- **Refer a Friend Alumni Scheme**
- **Prompt Payment Discount** — for full upfront payment
- **International School Scholarships**
- **Alumni Scholarship** — for Wolverhampton graduates progressing to PG
- **University of Wolverhampton Sports Scholarship**
- **Partner Scholarships** — via international partner institutions
- **Commonwealth PhD Scholarships**, **Commonwealth Master's Scholarship**, **Commonwealth Split-site Scholarships**
- **Chevening Scholarship** (UK government)
- **External Funded Scholarships**

> UK students can apply for Student Finance England loans (tuition fee loan + maintenance loan). NHS-funded programmes (Nursing, Midwifery, some Allied Health) include an additional NHS Learning Support Fund bursary.

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.overview.name
  value: "University of Wolverhampton"
  source_url: https://www.wlv.ac.uk/
  source_snippet: "University of Wolverhampton - Wulfruna Street, Wolverhampton WV1 1LY"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-002:
  field: institution.faculties
  value: "Faculty of Arts, Business and Social Sciences; Faculty of Education, Health and Wellbeing; Faculty of Science and Engineering; Black Country Medical School"
  source_url: https://www.wlv.ac.uk/schools-and-institutes/
  source_snippet: "FACULTY OF ARTS, BUSINESS AND SOCIAL SCIENCES / FACULTY OF EDUCATION, HEALTH AND WELLBEING / FACULTY OF SCIENCE AND ENGINEERING / BLACK COUNTRY MEDICAL SCHOOL"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-003:
  field: institution.schools
  value: "School of Business & Law; School of Social Science, Humanities & Creative Industries; School of Education & Psychology; School of Nursing and Midwifery; School of Health and Wellbeing; School of Architecture, Computing & Engineering; School of Pharmacy & Life Sciences"
  source_url: https://www.wlv.ac.uk/courses/bsc-hons-accounting-and-finance/
  source_snippet: "School of Social Science, Humanities & Creative Industries / School of Business & Law / School of Nursing and Midwifery / School of Health and Wellbeing / School of Education & Psychology / School of Pharmacy & Life Sciences / School of Architecture, Computing & Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-004:
  field: programs.az_directory
  value: "All UG and PG programmes listed at https://www.wlv.ac.uk/a-z/"
  source_url: https://www.wlv.ac.uk/a-z/
  source_snippet: "BSc (Hons) Accounting and Finance / BA (Hons) Animation / ... (full A-Z index, 392 entries; 379 deduplicated as unique degree programmes)"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-005:
  field: costs.international.ug_nonlab_2026_2027
  value: "£17,600"
  source_url: https://www.wlv.ac.uk/international/international-fees--scholarships/
  source_snippet: "Tuition Fee Undergraduate 2026/2027 / Non-Lab Based / £17,600"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-006:
  field: costs.international.ug_lab_2026_2027
  value: "£18,700"
  source_url: https://www.wlv.ac.uk/international/international-fees--scholarships/
  source_snippet: "Tuition Fee Undergraduate 2026/2027 / Lab-Based / £18,700"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-007:
  field: costs.international.pgt_nonlab_2026_2027
  value: "£18,645"
  source_url: https://www.wlv.ac.uk/international/international-fees--scholarships/
  source_snippet: "Tuition Fee Postgraduate 2026/2027 / Non-Lab Based / £18,645"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-008:
  field: costs.international.pgt_lab_2026_2027
  value: "£19,859"
  source_url: https://www.wlv.ac.uk/international/international-fees--scholarships/
  source_snippet: "Tuition Fee Postgraduate 2026/2027 / Lab-Based / £19,859"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-009:
  field: english.bands.IELTS
  value: "Four bands: 6.0/5.5 / 6.5/6.0 / 7.0/6.0 / 7.0/6.5"
  source_url: https://www.wlv.ac.uk/international/making-an-application/language-entry-requirements/
  source_snippet: "Courses that require IELTS 6.0 no component less than 5.5 / Courses that require IELTS 6.5 no component less than 6.0 / Courses that require IELTS 7.0 no component less than 6.0 / Courses that require IELTS 7.0 no component less than 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-010:
  field: english.TOEFL.iBT_pre_2026_01_21
  value: "67/17 / 72/17 / 94/22 / 94/24 (across 4 bands)"
  source_url: https://www.wlv.ac.uk/international/making-an-application/language-entry-requirements/
  source_snippet: "TOFEL iBT (iBT or Special Home Edition) - taken before 21.01.26 / TOFEL ETS / Overall Score of 67 with no component score less than 17 / Overall Score of 72 with no component score less than 17 / Overall Score of 94 with no component score less than 22 / Overall Score of 94 with no component score less than 24"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-011:
  field: english.PTE.Academic
  value: "59/59 / 65/59 / 75/59 / 75/65"
  source_url: https://www.wlv.ac.uk/international/making-an-application/language-entry-requirements/
  source_snippet: "PTE Academic / Pearson / 59 overall with no component less than 59 / 65 overall with no component less than 59 / 75 overall with no component less than 59 / 75 overall with no component less than 65"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-012:
  field: english.Duolingo
  value: "110/100 / 120/110 / 130/110 / 130/120"
  source_url: https://www.wlv.ac.uk/international/making-an-application/language-entry-requirements/
  source_snippet: "Duolingo English Test (DET) / Duolingo / 110 overall with no component less than 100 / 120 with no component less than 110 / 130 overall with no component less than 110 / 130 overall with no component less than 120"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-013:
  field: apply.ucas_code
  value: "W75"
  source_url: https://www.ucas.com/
  source_snippet: "UCAS institution code W75 - University of Wolverhampton"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-014:
  field: apply.clearing
  value: "Wolverhampton participates in UCAS Clearing"
  source_url: https://www.wlv.ac.uk/clearing/
  source_snippet: "CLEARING 2026 / There's still time to apply – Call us on 01902 968555!"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-015:
  field: institution.address
  value: "Wulfruna Street, Wolverhampton WV1 1LY"
  source_url: https://www.wlv.ac.uk/
  source_snippet: "UNIVERSITY OF WOLVERHAMPTON / Wulfruna Street / Wolverhampton / WV1 1LY / Tel: 01902 321000"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-G-001:
  field: programs.research.phd_computing
  value: "PhD Postgraduate Research in Computer Science"
  source_url: https://www.wlv.ac.uk/courses/phd-postgraduate-research-in-computer-science/
  source_snippet: "PhD Postgraduate research in Computer Science / School of Architecture, Computing & Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-G-002:
  field: programs.pgt.MBA
  value: "MBA Business Administration; MBA Business Administration - Extended"
  source_url: https://www.wlv.ac.uk/courses/mba-business-administration/
  source_snippet: "MBA Business Administration / School of Business & Law"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-G-003:
  field: programs.ug.MPharm
  value: "MPharm (Hons) Pharmacy"
  source_url: https://www.wlv.ac.uk/courses/mpharm-hons-pharmacy/
  source_snippet: "MPharm (Hons) Pharmacy / School of Pharmacy & Life Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
wolverhampton-knowledge-base-v2/
├── overview.md           # Section 0 + key facts
├── faculty-abss/         # Faculty of Arts, Business and Social Sciences
│   ├── school-business-law.md      (all 99 courses)
│   └── school-sshci.md             (all 77 courses)
├── faculty-ehw/          # Faculty of Education, Health and Wellbeing
│   ├── school-education-psychology.md   (38)
│   ├── school-nursing-midwifery.md      (22)
│   └── school-health-wellbeing.md       (49)
├── faculty-se/           # Faculty of Science and Engineering
│   ├── school-ace.md                (74)
│   └── school-pharmacy-life-sciences.md (20)
├── apply.md              # Section 3 (admissions + English)
├── costs.md              # Section 4 (fees + scholarships)
└── evidence.md           # Section 5 (citation index)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "wolverhampton-knowledge-base-v2"
  school: "<home school>"
  faculty: "<home faculty>"
  degree_level: "<BA|BSc|BEng|BMid|LLB|HNC|MA|MSc|MBA|MArch|LLM|MPhil|MRes|PhD|PGCert|PGDip>"
  level: undergraduate | graduate
  field_type: programs | overview | deadlines | tests | costs | funding
  source_url: <course page URL or wlv.ac.uk sub-page>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P0 | UCAS deadline exact date 2026 entry | https://www.ucas.com/ |
| P0 | Programme-specific English band (which band each course requires) | https://www.wlv.ac.uk/courses/<slug>/ |
| P1 | Home (UK) tuition fees for 2026/2027 | https://www.wlv.ac.uk/apply/funding-costs-fees-and-support/ |
| P1 | PG research MPhil/PhD funding & studentships | https://www.wlv.ac.uk/research/postgraduate-research-degrees/ |
| P2 | PhD supervision areas per school | https://www.wlv.ac.uk/schools-and-institutes/<school>/ |
| P2 | School-specific English requirements beyond minimum | per course page |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Wolverhampton value |
|-----------|-----------------------------------|
| Total program count (Rule 1) | 379 |
| School / department count (Rule 2) | 7 schools + 4 faculties + 1 medical school |
| UG programmes (incl. HNC) | 226 |
| PG programmes (incl. PGCert/PGDip) | 153 |
| UG intl tuition (non-lab) 2026/27 | £17,600/yr |
| UG intl tuition (lab) 2026/27 | £18,700/yr |
| PGT intl tuition (non-lab) 2026/27 | £18,645/yr |
| PGT intl tuition (lab) 2026/27 | £19,859/yr |
| PhD intl tuition | Lab-based band (£19,859/yr) |
| IELTS min (Band A) | 6.0 (5.5) |
| IELTS max (Band D) | 7.0 (6.5) |
| TOEFL iBT min (pre-2026) | 67 (17) |
| UCAS code | W75 |
| Application portal (UG) | UCAS |
| Application portal (PG) | Direct to University |
| Institution region | UK (West Midlands) |
| Town | Wolverhampton |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: wlv.ac.uk (university website), ucas.com (UCAS portal)
> **Verification**: ego-browser snapshotText + JS DOM extraction; A-Z list, faculty/school pages, individual course pages, international fees page, language entry requirements page
> **Granularity**: school → department → degree-level → program
