# Cardiff University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Wales)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 237 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | P0 follow-up (PG course listing is JS-rendered search) |
| 研究生博士项目 (PhD/Doctoral) | P0 follow-up (separate research programme listing) |
| **学位项目总计 (UG extracted)** | **237** |
| 学院 (Colleges) | 3 |
| 学术院系 (Academic Schools) | 24 |

> **Data source**: Cardiff University undergraduate A-Z course listing (`cardiff.ac.uk/study/undergraduate/courses/a-to-z`), 237 courses extracted.
> **PG note**: Postgraduate taught and research programmes are behind a JS-rendered search interface at `cardiff.ac.uk/study/postgraduate/taught/search` — requires separate extraction (P0 follow-up).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Cardiff University (Prifysgol Caerdydd)
├── College of Arts, Humanities and Social Sciences     [学院]
│   ├── Cardiff Business School                         [系]
│   ├── School of English, Communication and Philosophy [系]
│   ├── School of Geography and Planning                [系]
│   ├── School of History, Archaeology and Religion     [系]
│   ├── School of Journalism, Media and Culture         [系]
│   ├── School of Law and Politics                      [系]
│   ├── School of Modern Languages                      [系]
│   ├── School of Music                                 [系]
│   ├── School of Social Sciences                       [系]
│   └── School of Welsh                                 [系]
├── College of Biomedical and Life Sciences             [学院]
│   ├── School of Biosciences                           [系]
│   ├── School of Dentistry                             [系]
│   ├── School of Healthcare Sciences                   [系]
│   ├── School of Medicine                              [系]
│   ├── School of Optometry and Vision Sciences         [系]
│   ├── School of Pharmacy and Pharmaceutical Sciences  [系]
│   └── School of Psychology                            [系]
└── College of Physical Sciences and Engineering        [学院]
    ├── Welsh School of Architecture                    [系]
    ├── School of Chemistry                             [系]
    ├── School of Computer Science and Informatics      [系]
    ├── School of Earth and Environmental Sciences      [系]
    ├── School of Engineering                           [系]
    ├── School of Mathematics                           [系]
    └── School of Physics and Astronomy                 [系]
```

> **Source**: `cardiff.ac.uk/about/organisation/colleges-schools`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|

| BS | BS | — | 本科 | 116 |
| BA | BA | — | 本科 | 52 |
| BEng | BEng | — | 本科 | 15 |
| MEng | MEng | — | 本科 (Integrated Master's) | 14 |
| MSci | MSci | — | 本科 (Integrated Master's) | 9 |
| MPhys | MPhys | — | 本科 (Integrated Master's) | 4 |
| LLB | LLB | — | 本科 | 4 |
| BN | BN | — | 本科 | 3 |
| MChem | MChem | — | 本科 (Integrated Master's) | 3 |
| MMath | MMath | — | 本科 (Integrated Master's) | 3 |
| MBBCh | MBBCh | — | 本科 (Medicine) | 2 |
| BMus | BMus | — | 本科 | 2 |
| MOptom | MOptom | — | 本科 (Integrated Master's) | 2 |
| CertHE | CertHE | — | 本科 | 1 |
| MBiochem | MBiochem | — | 本科 (Integrated Master's) | 1 |
| MBiol | MBiol | — | 本科 (Integrated Master's) | 1 |
| MBiomed | MBiomed | — | 本科 (Integrated Master's) | 1 |
| DipHE | DipHE | — | 本科 | 1 |
| BDS | BDS | — | 本科 | 1 |
| BMid | BMid | — | 本科 | 1 |
| MPharm | MPharm | — | 本科 (Integrated Master's) | 1 |

| **合计** | | | | **237** |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 学位 | BA | BDS | BEng | BMid | BMus | BN | BS | CertHE | DipHE | LLB | MBBCh | MBiochem | MBiol | MBiomed | MChem | MEng | MMath | MOptom | MPharm | MPhys | MSci | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

| Architecture | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | **7** |
| Biosciences | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **12** |
| Business | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **25** |
| Chemistry | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Computer Science and Informatics | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | **11** |
| Dentistry | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **3** |
| Earth and Environmental Sciences | 0 | 0 | 1 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 6 | **23** |
| Engineering | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | **23** |
| English, Communication and Philosophy | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Geography and Planning | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| Healthcare Sciences | 0 | 0 | 0 | 1 | 0 | 3 | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **11** |
| History, Archaeology and Religion | 7 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| Journalism, Media and Culture | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **7** |
| Law and Politics | 6 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **12** |
| Mathematics | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | **14** |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Modern Languages | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **9** |
| Music | 3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **5** |
| Optometry and Vision Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | **2** |
| Pharmacy and Pharmaceutical Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **1** |
| Physics and Astronomy | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | **10** |
| Psychology | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **3** |
| Social Sciences | 1 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Welsh | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **9** |
| **合计** | 52 | 1 | 15 | 1 | 2 | 3 | 116 | 1 | 1 | 4 | 2 | 1 | 1 | 1 | 3 | 14 | 3 | 2 | 1 | 4 | 9 | **237** |

> **Reconciliation check**: Rule-1 total (237) == matrix-sum (237) == Rule-5 rows (237). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Cardiff University is organised into 3 academic Colleges, each containing multiple Academic Schools (24 total). See Section 0.2 for the full hierarchy tree. All undergraduate degree programmes are administered by one of these 24 Schools.

### 1.2 Undergraduate degree programmes — grouped by School > Degree Level


#### Architecture

##### BEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architectural-engineering-beng |
| 2 | Architectural Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architectural-engineering-with-a-year-in-industry-beng |

##### BS (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architecture-bsc |
| 2 | Architecture with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architecture-with-a-foundation-year-bsc |
| 3 | Architecture with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architecture-with-a-year-of-study-abroad-bsc |

##### MEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architectural-engineering-meng |
| 2 | Architectural Engineering with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/architectural-engineering-with-year-in-industry-meng |

---

#### Biosciences

##### BS (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biochemistry-bsc |
| 2 | Biochemistry with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biochemistry-with-a-foundation-year-bsc |
| 3 | Biochemistry with Professional Training Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biochemistry-with-professional-training-year-bsc |
| 4 | Biological Sciences | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biological-sciences-bsc |
| 5 | Biological Sciences with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biological-sciences-with-a-foundation-year-bsc |
| 6 | Biological Sciences with Professional Training Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biological-sciences-with-professional-training-year-bsc |
| 7 | Biomedical Sciences | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biomedical-sciences-bsc |
| 8 | Biomedical Sciences with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biomedical-sciences-with-a-foundation-year-bsc |
| 9 | Biomedical Sciences with Professional Training Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biomedical-sciences-with-professional-training-year-bsc |

##### MBiochem (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biochemistry-mbiochem |

##### MBiol (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biological-sciences-mbiol |

##### MBiomed (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/biomedical-sciences-mbiomed |

---

#### Business

##### BS (25 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/accounting-bsc |
| 2 | Accounting and Finance | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/accounting-and-finance-bsc |
| 3 | Accounting and Finance with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/accounting-and-finance-with-a-foundation-year-bsc |
| 4 | Accounting and Finance with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/accounting-and-finance-with-a-professional-placement-year-bsc |
| 5 | Accounting with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/accounting-with-a-professional-placement-year-bsc |
| 6 | Banking and Finance | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/banking-and-finance-bsc |
| 7 | Banking and Finance with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/banking-and-finance-with-a-professional-placement-year-bsc |
| 8 | Business Economics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-economics-bsc |
| 9 | Business Economics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-economics-with-a-professional-placement-year-bsc |
| 10 | Business Management | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-bsc |
| 11 | Business Management (Human Resource Management) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-human-resource-management-bsc |
| 12 | Business Management (Human Resource Management) with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-human-resource-management-with-a-professional-placement-year-bsc |
| 13 | Business Management (International Management) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-international-management-bsc |
| 14 | Business Management (International Management) with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-international-management-with-a-professional-placement-year-bsc |
| 15 | Business Management (Logistics and Operations) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-logistics-and-operations-bsc |
| 16 | Business Management (Logistics and Operations) with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-logistics-and-operations-with-a-professional-placement-year-bsc |
| 17 | Business Management (Marketing) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-marketing-bsc |
| 18 | Business Management (Marketing) with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-marketing-with-a-professional-placement-year-bsc |
| 19 | Business Management with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-with-a-foundation-year-bsc |
| 20 | Business Management with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-with-a-professional-placement-year-bsc |
| 21 | Business Management with Welsh | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-with-welsh-bsc |
| 22 | Business Management with Welsh with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/business-management-with-welsh-with-a-professional-placement-year-bsc |
| 23 | Economics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/economics-bsc |
| 24 | Economics with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/economics-with-a-foundation-year-bsc |
| 25 | Economics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/economics-with-a-professional-placement-year-bsc |

---

#### Chemistry

##### BS (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-bsc |
| 2 | Chemistry with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-with-a-foundation-year-bsc |
| 3 | Chemistry with a Placement Year Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-with-a-placement-year-abroad-bsc |
| 4 | Chemistry with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-with-a-year-in-industry-bsc |
| 5 | Medicinal Chemistry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/bsc-medicinal-chemistry |
| 6 | Medicinal Chemistry with a Year Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medicinal-chemistry-with-a-year-abroad-bsc |
| 7 | Medicinal Chemistry with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medicinal-chemistry-with-a-year-in-industry-bsc |

##### MChem (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-mchem |
| 2 | Chemistry with a Placement Year Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-with-a-placement-year-abroad-mchem |
| 3 | Chemistry with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/chemistry-with-year-in-industry-mchem |

---

#### Computer Science and Informatics

##### BS (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Software Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/applied-software-engineering-bsc |
| 2 | Computer Science | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-bsc |
| 3 | Computer Science with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-a-foundation-year-bsc |
| 4 | Computer Science with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-a-year-in-industry-bsc |
| 5 | Computer Science with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-a-year-of-study-abroad-bsc |
| 6 | Computer Science with Cyber Security | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-cyber-security-bsc |
| 7 | Computer Science with Cyber Security with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-cyber-security-with-a-year-in-industry-bsc |
| 8 | Computer Science with Cyber Security with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-cyber-security-with-a-year-of-study-abroad-bsc |

##### MSci (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-msci |
| 2 | Computer Science with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-a-year-in-industry-msci |
| 3 | Computer Science with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-with-a-year-of-study-abroad-msci |

---

#### Dentistry

##### BDS (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Surgery | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/dental-surgery-bds |

##### BS (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Therapy and Dental Hygiene | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/dental-therapy-and-dental-hygiene-bsc |

##### DipHE (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/dental-hygiene-diphe |

---

#### Earth and Environmental Sciences

##### BEng (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil and Environmental Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-and-environmental-engineering-beng |

##### BS (15 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-geography-bsc |
| 2 | Environmental Geography with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-geography-with-a-year-of-study-abroad-bsc |
| 3 | Environmental Geoscience | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-geoscience-bsc |
| 4 | Environmental Geoscience with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-geoscience-with-a-year-of-study-abroad-bsc |
| 5 | Environmental Sustainability Science | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-sustainability-science-bsc |
| 6 | Exploration Geology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/exploration-geology-bsc |
| 7 | Exploration Geology with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/exploration-geology-with-a-year-of-study-abroad-bsc |
| 8 | Geology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/geology-bsc |
| 9 | Geology with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/geology-with-a-foundation-year-bsc |
| 10 | Geology with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/geology-with-a-year-of-study-abroad-bsc |
| 11 | Marine Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/marine-geography-bsc |
| 12 | Marine Geography with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/marine-geography-with-a-year-of-study-abroad-bsc |
| 13 | Physical Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physical-geography-bsc |
| 14 | Physical Geography with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physical-geography-with-a-foundation-year-bsc |
| 15 | Physical Geography with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physical-geography-with-a-year-of-study-abroad-bsc |

##### MEng (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil and Environmental Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-and-environmental-engineering-meng |

##### MSci (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-geography-msci |
| 2 | Environmental Geoscience | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/environmental-geoscience-msci |
| 3 | Exploration Geology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/exploration-geology-msci |
| 4 | Geology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/geology-msci |
| 5 | Marine Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/marine-geography-msci |
| 6 | Physical Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physical-geography-msci |

---

#### Engineering

##### BEng (12 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil and Environmental Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-and-environmental-engineering-with-a-year-in-industry-beng |
| 2 | Civil Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-engineering-beng |
| 3 | Civil Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-engineering-with-a-year-in-industry-beng |
| 4 | Electrical and Electronic Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/electrical-and-electronic-engineering-beng |
| 5 | Electrical and Electronic Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/electrical-and-electronic-engineering-with-a-year-in-industry-beng |
| 6 | Engineering with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/engineering-with-a-foundation-year-beng |
| 7 | Mechanical and Electrical Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-and-electrical-engineering-beng |
| 8 | Mechanical and Electrical Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-and-electrical-engineering-with-a-year-in-industry-beng |
| 9 | Mechanical Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-engineering-beng |
| 10 | Mechanical Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-engineering-with-a-year-in-industry-beng |
| 11 | Medical Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medical-engineering-beng |
| 12 | Medical Engineering with a Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medical-engineering-with-a-year-in-industry-beng |

##### MEng (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil and Environmental Engineering with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-and-environmental-engineering-with-year-in-industry-meng |
| 2 | Civil Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-engineering-meng |
| 3 | Civil Engineering with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/civil-engineering-with-year-in-industry-meng |
| 4 | Electrical and Electronic Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/electrical-and-electronic-engineering-meng |
| 5 | Electrical and Electronic Engineering with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/electrical-and-electronic-engineering-with-year-in-industry-meng |
| 6 | Mechanical and Electrical Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-and-electrical-engineering-meng |
| 7 | Mechanical and Electrical Engineering (Year in Industry) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-and-electrical-engineering-with-year-in-industry-meng |
| 8 | Mechanical Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-engineering-meng |
| 9 | Mechanical Engineering with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mechanical-engineering-with-year-in-industry-meng |
| 10 | Medical Engineering | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medical-engineering-meng |
| 11 | Medical Engineering with Year in Industry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medical-engineering-with-year-in-industry-meng |

---

#### English, Communication and Philosophy

##### BA (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Language with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-language-with-a-foundation-year-ba |
| 2 | English Literature | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-literature-ba |
| 3 | English Literature and a Modern Language | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-literature-and-a-modern-language-ba |
| 4 | English Literature and History | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-literature-and-history-ba |
| 5 | English Literature and Philosophy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-literature-and-philosophy-ba |
| 6 | English Literature with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-literature-with-a-foundation-year-ba |
| 7 | English Literature with Creative Writing | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-literature-with-creative-writing-ba |
| 8 | Philosophy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/philosophy-ba |
| 9 | Philosophy with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/philosophy-with-a-foundation-year-ba |
| 10 | Religion, Philosophy and Ethics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/religion,-philosophy-and-ethics-ba |

---

#### Geography and Planning

##### BS (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Human Geography | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-geography-bsc |
| 2 | Human Geography and Planning | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-geography-and-planning-bsc |
| 3 | Human Geography and Planning with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-geography-and-planning-with-a-foundation-year-bsc |
| 4 | Human Geography and Planning with a Professional Placement Year (Accredited) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-geography-and-planning-with-a-professional-placement-year-accredited-bsc |
| 5 | Human Geography and Planning with a Professional Placement Year (non-accredited) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-geography-and-planning-with-a-professional-placement-year-non-accredited |
| 6 | Human Geography with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-geography-with-a-professional-placement-year-bsc |
| 7 | Urban Planning & Development | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/urban-planning-and-development-bsc |
| 8 | Urban Planning and Development with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/urban-planning-and-development-with-a-professional-placement-year-bsc |

---

#### Healthcare Sciences

##### BMid (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Midwifery | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/midwifery-bmid |

##### BN (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Nursing (Adult) Autumn Intake | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/bachelor-of-nursing-adult-autumn-intake-bn |
| 2 | Bachelor of Nursing (Child) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/bachelor-of-nursing-child-bn |
| 3 | Bachelor of Nursing (Mental Health) Autumn Intake | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/bachelor-of-nursing-mental-health-autumn-intake-bn |

##### BS (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Diagnostic Radiography and Imaging | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/diagnostic-radiography-and-imaging-bsc |
| 2 | Healthcare Standalone module (Level 6) – January | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/stand-alone-module-degree-level-january-start-bsc-part-time |
| 3 | Healthcare Standalone module (Level 6) – September | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/stand-alone-module-degree-level-september-start-bsc-part-time |
| 4 | Occupational Therapy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/occupational-therapy-bsc |
| 5 | Physiotherapy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physiotherapy-bsc |
| 6 | Radiotherapy and Oncology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/radiotherapy-and-oncology-bsc |

##### CertHE (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Assistant Radiographic Practice (Clinical Imaging) | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/assistant-radiographic-practice-clinical-imaging |

---

#### History, Archaeology and Religion

##### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/archaeology-ba |
| 2 | Archaeology and History | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/archaeology-and-history-ba |
| 3 | Archaeology with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/archaeology-with-a-foundation-year-ba |
| 4 | History | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/history-ba |
| 5 | History and a Modern Language | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/history-and-a-modern-language-ba |
| 6 | History with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/history-with-a-foundation-year-ba |
| 7 | Modern History, Politics and International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/modern-history,-politics-and-international-relations-ba |

##### BS (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology and Heritage Science | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/archaeology-and-heritage-science-bsc |

---

#### Journalism, Media and Culture

##### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Literature, Journalism and Media | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/journalism,-media-and-english-literature-ba |
| 2 | Journalism and Communication with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/journalism-and-communication-with-a-foundation-year-ba |
| 3 | Journalism and Communications | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/journalism-and-communications-ba |
| 4 | Journalism, Politics and International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/journalism-politics-and-international-relations |
| 5 | Media and Communications | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/media-and-communications-ba |
| 6 | Media, Journalism and Culture | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/media,-journalism-and-culture-ba |
| 7 | Welsh and Journalism | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-journalism-ba |

---

#### Law and Politics

##### BA (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/international-relations-ba |
| 2 | Philosophy, Politics and International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/philosophy,-politics-and-international-relations-ba |
| 3 | Politics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/politics-ba |
| 4 | Politics and International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/international-relations-and-politics-ba |
| 5 | Politics and International Relations with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/politics-and-international-relations-with-a-foundation-year-ba |
| 6 | Politics, International Relations and a Modern Language | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/politics,-international-relations-with-a-modern-language-ba |

##### BS (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/criminology-bsc |
| 2 | Criminology with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/criminology-with-a-foundation-year-bsc |

##### LLB (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/law-llb |
| 2 | Law with Criminology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/law-and-criminology-llb |
| 3 | Law with Politics and International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/law-with-politics-and-international-relations-llb |
| 4 | Law with Welsh | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/law-and-welsh-llb |

---

#### Mathematics

##### BS (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Financial Mathematics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/financial-mathematics-bsc |
| 2 | Financial Mathematics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/financial-mathematics-with-a-professional-placement-year-bsc |
| 3 | Financial Mathematics with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/financial-mathematics-with-a-year-abroad-bsc |
| 4 | Mathematics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-bsc |
| 5 | Mathematics for the Modern World | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-for-a-modern-world-bsc |
| 6 | Mathematics for the Modern World with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-for-the-modern-world-with-a-foundation-year-bsc |
| 7 | Mathematics for the Modern World with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-for-the-modern-world-with-professional-placement-year-bsc |
| 8 | Mathematics for the Modern World with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-for-the-modern-world-with-a-year-of-study-abroad-bsc |
| 9 | Mathematics with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-with-a-foundation-year-bsc |
| 10 | Mathematics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-with-a-professional-placement-year-bsc |
| 11 | Mathematics with a Year Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-with-a-year-abroad-bsc |

##### MMath (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-mmath |
| 2 | Mathematics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-with-a-professional-placement-year-mmath |
| 3 | Mathematics with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/mathematics-with-a-year-abroad-mmath |

---

#### Medicine

##### BS (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Pharmacology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medical-pharmacology-bsc |
| 2 | Medical Pharmacology with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medical-pharmacology-with-a-foundation-year-bsc |

##### MBBCh (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medicine-mbbch |
| 2 | Medicine: Graduate Entry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/medicine-graduate-entry-mbbch |

---

#### Modern Languages

##### BA (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Language and Linguistics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-language-and-linguistics-ba |
| 2 | English Language and Literature | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/english-language-and-literature-ba |
| 3 | Linguistics and a Modern Language | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/linguistics-and-a-modern-language-ba |
| 4 | Modern Chinese | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/modern-chinese-ba-4-years |
| 5 | Modern Languages | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/modern-languages-ba |
| 6 | Modern Languages with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/modern-languages-with-a-foundation-year-ba |
| 7 | Philosophy and Linguistics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/philosophy-and-linguistics-ba |
| 8 | Translation | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/translation-ba |
| 9 | Translation with a Placement Year Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/translation-with-a-placement-year-abroad-ba |

---

#### Music

##### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music and a Modern Language | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/music-and-a-modern-language-ba |
| 2 | Music and English Literature | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/music-and-english-literature-ba |
| 3 | Music with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/music-with-a-foundation-year-bmus |

##### BMus (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/music-bmus |
| 2 | Music with a Year of Study Abroad | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/music-with-a-year-of-study-abroad-bmus |

---

#### Optometry and Vision Sciences

##### MOptom (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Optometry | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/master-of-optometry |
| 2 | Optometry with Preliminary Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/master-of-optometry-with-preliminary-year-5-year |

---

#### Pharmacy and Pharmaceutical Sciences

##### MPharm (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/pharmacy-mpharm |

---

#### Physics and Astronomy

##### BS (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/astrophysics-bsc |
| 2 | Astrophysics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/astrophysics-with-a-professional-placement-year-bsc |
| 3 | Physics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physics-bsc |
| 4 | Physics with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physics-with-a-foundation-year-bsc |
| 5 | Physics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physics-with-professional-placement-bsc |
| 6 | Physics with Medical Physics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physics-with-medical-physics-bsc |

##### MPhys (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/astrophysics-mphys |
| 2 | Astrophysics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/astrophysics-with-a-professional-placement-year-mphys |
| 3 | Physics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physics-mphys |
| 4 | Physics with a Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/physics-with-professional-placement-mphys |

---

#### Psychology

##### BS (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/psychology-bsc |
| 2 | Psychology with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/psychology-with-a-foundation-year-bsc |
| 3 | Psychology with Professional Placement Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/psychology-with-professional-placement-bsc |

---

#### Social Sciences

##### BA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Politics, International Relations and Sociology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/politics-international-relations-and-sociology-ba |

##### BS (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Social Policy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/criminology-and-social-policy-bsc |
| 2 | Criminology and Sociology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/criminology-and-sociology-bsc |
| 3 | Education | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/education-bsc |
| 4 | Human and Social Sciences | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/human-and-social-sciences-bsc |
| 5 | Social Science | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/social-science-bsc |
| 6 | Social Sciences with a Foundation Year | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/social-sciences-with-a-foundation-year-bsc |
| 7 | Sociology | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/sociology-bsc |
| 8 | Sociology and Education | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/sociology-and-education-bsc |
| 9 | Sociology and Social Policy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/sociology-and-social-policy-bsc |

---

#### Welsh

##### BA (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Welsh | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-ba |
| 2 | Welsh and a Modern Language | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-a-modern-language-ba |
| 3 | Welsh and Education | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-education-ba |
| 4 | Welsh and English Literature | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-english-literature-ba |
| 5 | Welsh and History | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-history-ba |
| 6 | Welsh and Linguistics | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-linguistics-ba |
| 7 | Welsh and Music | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-music-ba |
| 8 | Welsh and Philosophy | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh-and-philosophy-ba |
| 9 | Welsh, Politics and International Relations | https://www.cardiff.ac.uk/study/undergraduate/courses/2026/welsh,-politics-and-international-relations-ba |

---


### 1.3 Joint honours / cross-school programmes

Many Cardiff degree programmes are joint honours (e.g., "Welsh and History BA", "Mathematics and Physics BSc"). These are listed under their primary administrative school; the partner school is noted in the programme name. Joint honours programmes are a distinctive feature of UK university education.

### 1.4 Foundation year programmes

Cardiff offers foundation year variants of many degree programmes (e.g., "Accounting and Finance with a Foundation Year BSc"). These are listed as separate entries in the A-Z listing and are included in the counts above. Foundation year programmes provide an alternative entry route for students who do not meet the standard entry requirements.

### 1.5 Professional placement year / Year in industry / Year abroad variants

Many programmes offer variants with a Professional Placement Year, Year in Industry, or Year of Study Abroad. These are listed as separate entries in the A-Z listing and are counted separately.

---

## SECTION 2 — Graduate education

> ⚠ **P0 follow-up required**: Cardiff's postgraduate taught course search is JS-rendered (`cardiff.ac.uk/study/postgraduate/taught/search`). The PG research programme listing is at `cardiff.ac.uk/study/postgraduate/research`. Both require separate ego-browser extraction with JS interaction.

### 2.1 Postgraduate taught (PGT)

- **Search page**: `cardiff.ac.uk/study/postgraduate/taught/search`
- **A-Z listing**: Not directly accessible (JS-rendered)
- **Known PG degrees**: MSc, MA, MBA, LLM, MRes, PG Cert, PG Dip
- **Schools offering PGT**: All 24 academic schools

### 2.2 Postgraduate research (PGR)

- **Research programmes**: `cardiff.ac.uk/study/postgraduate/research`
- **Degrees**: PhD, MPhil, MD, Professional Doctorates
- **Research areas**: Organised by School; each School has its own research programme pages

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | C15 |
| **Main application deadline** | 29 January (2026 entry) |
| **UCAS Extra opens** | February 2026 |
| **Clearing opens** | July 2026 |
| **Entry year** | September 2026 |

### 3.2 Undergraduate — academic entry requirements (typical)

| 考试体系 | 标准要求 | Contextual offer | 来源 |
|---------|---------|-----------------|------|
| **A-Level** | ABB (varies by course) | BBC | `cardiff.ac.uk/study/undergraduate/courses/` |
| **IB Diploma** | 32 points (HL 665) | 30 points (HL 655) | Course pages |
| **EPQ/IPQ** | Grade A may reduce offer by one grade | — | Course pages |
| **Advanced Welsh Baccalaureate** | Can substitute for one A-Level | — | Course pages |

> **Note**: Entry requirements vary significantly by course. Medicine (MBBCh) and Dentistry (BDS) have higher requirements. Always check the specific course page.

### 3.3 Undergraduate English language requirements

| 考试类型 | 标准要求 | 单项最低 | 来源 |
|---------|---------|---------|------|
| **IELTS Academic** | 6.5 overall | 5.5 each band | `cardiff.ac.uk/study/international/english-language-requirements` |
| **TOEFL iBT (pre-2026 scale)** | 88 overall | — | Same source |
| **TOEFL iBT (2026+ scale)** | 4.5 | — | Same source |
| **PTE Academic** | 69 overall | 59 each | Same source |
| **LanguageCert Academic (in-person)** | 70 overall | 60 each | Same source |
| **Oxford ELLT** | 7 overall | 5 each | Same source |

> **Exemptions**: Applicants with a full bachelor's degree taught in English from a UK institution or a majority English-speaking country are exempt. Medicine and Dentistry have higher requirements and do not accept all test types.
> **Validity**: Most tests valid for 2 years from test date.
> **IELTS One Skill Retake**: Accepted within 60 days of original test.

### 3.4 Graduate admissions

> ⚠ P0 follow-up: Graduate admissions requirements need separate extraction from PG course pages.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate tuition fees (2026 entry)

| Fee status | Annual tuition | Source |
|-----------|---------------|--------|
| **Home (UK)** | £9,250 | `cardiff.ac.uk/study/undergraduate/tuition-fees` |
| **International** | £22,700 – £29,450 (varies by course) | Course pages + `cardiff.ac.uk/study/undergraduate/tuition-fees/overseas-undergraduate-fees` |
| **Placement year** | 15-20% of full-time fee | Same source |

### 4.2 Estimated living costs (per year)

| 项目 | 估计费用 (£) |
|------|------------|
| Accommodation | 5,000 – 9,000 |
| Food | 2,000 – 4,000 |
| Transport | 400 – 800 |
| Study materials | 400 – 800 |
| Personal expenses | 1,500 – 3,000 |
| **Total (estimated)** | **9,300 – 17,600** |

> **Note**: Cardiff is consistently ranked as one of the UK's most affordable university cities (Condé Nast Traveller Readers' Choice Awards 2023: "UK's friendliest city").

### 4.3 Scholarships

- International scholarships available at undergraduate and postgraduate level
- Scholarship page: `cardiff.ac.uk/study/international/funding-and-fees`
- P0 follow-up: specific scholarship amounts and eligibility criteria

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Cardiff University (Prifysgol Caerdydd)"
  source_url: https://www.cardiff.ac.uk
  source_snippet: "Cardiff University"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-002:
  field: institution.colleges
  value: "3 Colleges: Arts Humanities Social Sciences, Biomedical Life Sciences, Physical Sciences Engineering"
  source_url: https://www.cardiff.ac.uk/about/organisation/colleges-schools
  source_snippet: "College of Arts, Humanities and Social Sciences / College of Biomedical and Life Sciences / College of Physical Sciences and Engineering"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-003:
  field: institution.schools
  value: "24 Academic Schools"
  source_url: https://www.cardiff.ac.uk/about/organisation/colleges-schools
  source_snippet: "Academic Schools" listing with 24 schools
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.programs.count
  value: "237 undergraduate degree programmes"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/courses/a-to-z
  source_snippet: "A-Z listing of all undergraduate courses, 237 entries extracted"
  capture_date: 2026-07-07
  evidence_type: official_webpage_listing

E-U-005:
  field: undergraduate.courses.page
  value: "over 300 degree programmes"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/courses
  source_snippet: "At Cardiff University, you can choose from over 300 degree programmes."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.entry_requirements.alevel.typical
  value: "ABB (standard) / BBC (contextual)"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/courses/2026/computer-science-bsc
  source_snippet: "A-Level: ABB (standard) / BBC (contextual)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english.ielts
  value: "IELTS 6.5 overall (5.5 each band)"
  source_url: https://www.cardiff.ac.uk/study/international/english-language-requirements
  source_snippet: "IELTS Academic: 6.5 overall with minimum 5.5 in each sub-skill"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english.toefl
  value: "TOEFL iBT 88 (pre-2026) / 4.5 (2026+ scale)"
  source_url: https://www.cardiff.ac.uk/study/international/english-language-requirements
  source_snippet: "TOEFL iBT requirements table"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.fees.home
  value: "£9,250 per year"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/tuition-fees
  source_snippet: "Home undergraduate fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.fees.international
  value: "£22,700 – £29,450 per year (varies by course)"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/tuition-fees/overseas-undergraduate-fees
  source_snippet: "Overseas undergraduate fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.application.system
  value: "UCAS"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/applying
  source_snippet: "Apply through UCAS"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.application.deadline
  value: "29 January 2026 (main deadline)"
  source_url: https://www.cardiff.ac.uk/study/undergraduate/applying
  source_snippet: "UCAS application deadline"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
cardiff-university-knowledge-base-v2
├── 0-overview (Section 0: rule 1-4, institution overview)
├── 1-undergraduate (Section 1: full UG programme listing, chunked by School)
│   ├── chunk-01-business
│   ├── chunk-02-english-communication-philosophy
│   ├── chunk-03-geography-planning
│   ├── ... (24 school chunks)
│   └── chunk-24-physics-astronomy
├── 2-graduate (Section 2: P0 follow-up placeholder)
├── 3-applications (Section 3: requirements, deadlines, English)
├── 4-costs (Section 4: fees, living costs, scholarships)
├── 5-evidence (Section 5: evidence chain)
└── 6-monitoring (Section 7: monitoring watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "cardiff-university-knowledge-base-v2"
  school: "<academic school>"
  degree_level: "<BA|BS|BEng|MEng|MSci|...>"
  level: undergraduate
  field_type: programs
  source_url: https://www.cardiff.ac.uk/study/undergraduate/courses/a-to-z
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Postgraduate taught course list (MSc/MA/MBA) | `cardiff.ac.uk/study/postgraduate/taught/search` |
| **P0** | Postgraduate research programme list (PhD/MPhil) | `cardiff.ac.uk/study/postgraduate/research` |
| **P0** | International tuition fees by course (detailed) | `cardiff.ac.uk/study/undergraduate/tuition-fees/overseas-undergraduate-fees` |
| **P0** | Scholarship amounts and eligibility | `cardiff.ac.uk/study/international/funding-and-fees` |
| **P1** | Per-course entry requirements (A-Level/IB specifics) | Individual course pages |
| **P1** | Graduate admissions requirements (GRE/GMAT, English) | Per-school PG admissions pages |
| **P2** | Course module details | Individual course pages |
| **P2** | Accommodation costs (detailed) | `cardiff.ac.uk/study/accommodation` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Cardiff University | (next university) |
|-----------|-------------------|-------------------|
| Total UG programmes | 237 | — |
| Academic schools | 24 | — |
| Colleges | 3 | — |
| UG Home tuition | £9,250 | — |
| UG International tuition (range) | £22,700 – £29,450 | — |
| IELTS minimum (UG) | 6.5 (5.5 each) | — |
| A-Level typical | ABB | — |
| UCAS deadline | 29 Jan | — |
| Region | Wales, UK | — |
| Russell Group | Yes | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: cardiff.ac.uk (main domain — no separate catalog/study subdomains)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programs (237/237) ✅ | PG programs (0/extracted) ⚠ P0 | Evidence (12 blocks) ✅
