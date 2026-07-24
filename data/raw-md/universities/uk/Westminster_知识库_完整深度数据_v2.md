# University of Westminster — 知识库完整深度数据 v2.0

> **学校**: University of Westminster
> **国家**: United Kingdom
> **城市**: London (主校区: 309 Regent Street, W1B 2HW)
> **建校**: 1838 (Royal Polytechnic Institution; 1992 获大学地位)
> **类型**: Public Research University
> **学生数**: ~19,000 (其中约 5,000 国际生)
> **数据采集日期**: 2026-07-08
> **数据来源**: https://www.westminster.ac.uk/course-search (filter course_type=926 UG / 26 PG)

---

## 0. 院校总览 (Overview)

### 0.1 五条结构性规则 (Five Structural Rules)

| 规则 | 数值 |
|------|------|
| **Rule 1 - 项目总数** | **231** (UG: 134 + PG: 97) |
| **Rule 2 - 学院/系明细层级** | 3 Colleges -> 26 Departments |
| **Rule 3 - 学历级别总数** | 20 distinct degree types (BA, BSc, BEng, LLB, MA, MSc, MBA, MFA, MArch, LLM, PGDip, PGCert 等) |
| **Rule 4 - 分布矩阵 (学院 × 学历级别)** | 见 0.4 节 |
| **Rule 5 - 全量专业明细 (按学院→系→学历级别→专业)** | 见 Section 1 & 2 |

**Reconciliation Check**:
- sum of matrix cells = **231** (OK)
- rule-1 total = **231** (OK)
- count of rows in rule-5 tables = **231** (OK)

### 0.2 学历级别清单 (Degree Inventory)

| 学历级别 | 计数 |
|---|---|
| BA HONOURS | 89 |
| BENG HONOURS | 4 |
| BSC HONOURS | 38 |
| LLB HONOURS | 3 |
| LLM | 6 |
| MA | 42 |
| MArch RIBA Part II | 1 |
| MBA | 2 |
| MFA | 1 |
| MSc | 34 |
| PGCert Social Change | 1 |
| PGCert Transport Planning | 1 |
| PGCert Urban Design | 1 |
| PGDip Counselling | 1 |
| PGDip Journalism | 2 |
| PGDip Legal Practice | 1 |
| PGDip RIBA Part III | 1 |
| PGDip Social Change | 1 |
| PGDip Transport Planning | 1 |
| PGDip Urban Design | 1 |


### 0.3 学院 × 学历级别 分布矩阵 (Distribution Matrix)

| College | Total | BA HONOURS | BENG HONOURS | BSC HONOURS | LLB HONOURS | LLM | MA | MArch RIBA Part II | MBA | MFA | MSc | PGCert Social Change | PGCert Transport Planning | PGCert Urban Design | PGDip Counselling | PGDip Journalism | PGDip Legal Practice | PGDip RIBA Part III | PGDip Social Change | PGDip Transport Planning | PGDip Urban Design |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Creative Arts & Technologies | 85 | 27 | 4 | 14 | 0 | 0 | 20 | 1 | 0 | 1 | 9 | 1 | 1 | 1 | 0 | 2 | 0 | 1 | 1 | 1 | 1 |
| College of Liberal Arts and Sciences | 104 | 46 | 0 | 17 | 3 | 5 | 17 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| Westminster Business School | 42 | 16 | 0 | 7 | 0 | 1 | 5 | 0 | 2 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


### 0.4 学院 → 系 层级树 (Hierarchy)

```
University of Westminster (231 programs)
├── Westminster Business School (42 programs)
│   ├── Accounting & Finance (8)
│   ├── Business & Management (19)
│   ├── Economics (3)
│   ├── Marketing (10)
│   └── Tourism & Events (2)
├── College of Liberal Arts and Sciences (104 programs)
│   ├── Biomedical Sciences (10)
│   ├── Criminology & Sociology (6)
│   ├── Data Science & Informatics (5)
│   ├── English & Creative Writing (16)
│   ├── Health (8)
│   ├── History (3)
│   ├── Languages (28)
│   ├── Law (9)
│   ├── Politics & International Relations (10)
│   └── Psychology (9)
└── College of Creative Arts & Technologies (85 programs)
    ├── Architecture & Interiors (12)
    ├── Architecture & Planning (5)
    ├── Art & Design (10)
    ├── Computer Science (13)
    ├── Construction & Surveying (4)
    ├── Fashion (9)
    ├── Film & Television (3)
    ├── Games (4)
    ├── Media & Communication (20)
    ├── Music (1)
    └── Transport & Logistics (4)
```

### 0.5 系项目数清单 (Department Counts)

| 系/Department | 项目数 |
|---|---|
| Accounting & Finance | 8 |
| Architecture & Interiors | 12 |
| Architecture & Planning | 5 |
| Art & Design | 10 |
| Biomedical Sciences | 10 |
| Business & Management | 19 |
| Computer Science | 13 |
| Construction & Surveying | 4 |
| Criminology & Sociology | 6 |
| Data Science & Informatics | 5 |
| Economics | 3 |
| English & Creative Writing | 16 |
| Fashion | 9 |
| Film & Television | 3 |
| Games | 4 |
| Health | 8 |
| History | 3 |
| Languages | 28 |
| Law | 9 |
| Marketing | 10 |
| Media & Communication | 20 |
| Music | 1 |
| Politics & International Relations | 10 |
| Psychology | 9 |
| Tourism & Events | 2 |
| Transport & Logistics | 4 |


---

## 1. 本科项目 (Undergraduate — 134 programs)

### 1.1 学院分布

| 学院 | UG 项目数 |
|------|------|
| Westminster Business School | 23 |
| College of Liberal Arts & Sciences | 66 |
| College of Creative Arts & Technologies | 45 |
| **Total** | **134** |

### 1.2 学历级别分布 (UG)

| 学历级别 | 数量 |
|----------|------|
| BA Honours | 89 |
| BSc Honours | 38 |
| BEng Honours | 4 |
| LLB Honours | 3 |

### 1.3 Foundation 变体

Many UG programs also have "with Foundation" variants (extra year) — 42 of 134 (~31%) include foundation-year routes. These are listed as separate program entries in the official course catalog.

### 1.4 Full UG Program List (by College → Department → Degree → Program)


### 学院: Westminster Business School


#### 系: Accounting & Finance


##### BA HONOURS

| 专业 | URL |
|---|---|
| Accounting and Business Management | [link](https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-business-management-ba-honours) |
| Finance and Business Management | [link](https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/finance-and-business-management-ba-honours) |

##### BSC HONOURS

| 专业 | URL |
|---|---|
| Accounting and Finance | [link](https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-bsc-honours) |
| Finance | [link](https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/finance-bsc-honours) |
| Fintech with Data Analytics | [link](https://www.westminster.ac.uk/accounting-and-finance-data-science-and-informatics-courses/2026-27/september/full-time/fintech-with-data-analytics-bsc-honours) |

#### 系: Business & Management


##### BA HONOURS

| 专业 | URL |
|---|---|
| Business Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-management-ba-honours) |
| Business Management Digital Business | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-management-digital-business-ba-honours) |
| Business Management Entrepreneurship | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-management-entrepreneurship-ba-honours) |
| Business Management Human Resource Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-management-human-resource-management-ba-honours) |
| Business Management Marketing | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-management-marketing-ba-honours) |
| Business Management with Foundation | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-management-with-foundation-ba-honours) |
| International Business | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/international-business-ba-honours) |
| International Communication and International Business | [link](https://www.westminster.ac.uk/business-and-management-languages-courses/2026-27/september/full-time/international-communication-and-international-business-ba-honours) |
| International Event Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/international-event-management-ba-honours) |
| International Hotel Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/international-hotel-management-ba-honours) |

##### BSC HONOURS

| 专业 | URL |
|---|---|
| Business Computing | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-computing-bsc-honours) |
| Business Computing with Foundation | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-computing-with-foundation-bsc-honours) |

#### 系: Economics


##### BSC HONOURS

| 专业 | URL |
|---|---|
| Financial Economics | [link](https://www.westminster.ac.uk/economics-courses/2026-27/september/full-time/financial-economics-bsc-honours) |

#### 系: Marketing


##### BA HONOURS

| 专业 | URL |
|---|---|
| Digital Marketing | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/digital-marketing-ba-honours) |
| International Marketing | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/international-marketing-ba-honours) |
| Marketing Communications with Ai Integration | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/marketing-communications-with-ai-integration-ba-honours) |
| Marketing Management | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/marketing-management-ba-honours) |

##### BSC HONOURS

| 专业 | URL |
|---|---|
| Marketing and Data Analytics | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/marketing-and-data-analytics-bsc-honours) |

### 学院: College of Liberal Arts and Sciences


#### 系: Biomedical Sciences


##### BSC HONOURS

| 专业 | URL |
|---|---|
| Applied Biomedical Science | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/applied-biomedical-science-bsc-honours) |
| Biochemistry | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biochemistry-bsc-honours) |
| Biochemistry with Foundation | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biochemistry-with-foundation-bsc-honours) |
| Biological Sciences | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biological-sciences-bsc-honours) |
| Biological Sciences with Foundation | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biological-sciences-with-foundation-bsc-honours) |
| Biomedical Science | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biomedical-science-bsc-honours) |
| Biomedical Science with Foundation | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biomedical-science-with-foundation-bsc-honours) |
| Pharmacology and Physiology with Foundation | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/pharmacology-and-physiology-with-foundation-bsc-honours) |

#### 系: Criminology & Sociology


##### BA HONOURS

| 专业 | URL |
|---|---|
| Criminology | [link](https://www.westminster.ac.uk/criminology-and-sociology-courses/2026-27/september/full-time/criminology-ba-honours) |
| Criminology with Foundation | [link](https://www.westminster.ac.uk/criminology-and-sociology-courses/2026-27/september/full-time/criminology-with-foundation-ba-honours) |
| Culture Environment and Social Change | [link](https://www.westminster.ac.uk/criminology-and-sociology-courses/2026-27/september/full-time/culture-environment-and-social-change-ba-honours) |
| Sociology | [link](https://www.westminster.ac.uk/criminology-and-sociology-courses/2026-27/september/full-time/sociology-ba-honours) |
| Sociology with Foundation | [link](https://www.westminster.ac.uk/criminology-and-sociology-courses/2026-27/september/full-time/sociology-with-foundation-ba-honours) |

#### 系: Data Science & Informatics


##### BSC HONOURS

| 专业 | URL |
|---|---|
| Data Science and Analytics | [link](https://www.westminster.ac.uk/data-science-and-informatics-courses/2026-27/september/full-time/data-science-and-analytics-bsc-honours) |
| Data Science and Analytics with Foundation | [link](https://www.westminster.ac.uk/data-science-and-informatics-courses/2026-27/september/full-time/data-science-and-analytics-with-foundation-bsc-honours) |

#### 系: English & Creative Writing


##### BA HONOURS

| 专业 | URL |
|---|---|
| Creative and Professional Writing | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/creative-and-professional-writing-ba-honours) |
| Creative Writing and English | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/creative-writing-and-english-ba-honours) |
| Creative Writing and English with Foundation | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/creative-writing-and-english-with-foundation-ba-honours) |
| English Language and International Communication | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-language-and-international-communication-ba-honours) |
| English Language and Linguistics | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-language-and-linguistics-ba-honours) |
| English Language and Linguistics with Foundation | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-language-and-linguistics-with-foundation-ba-honours) |
| English Literature and History | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-literature-and-history-ba-honours) |
| English Literature and Language | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-literature-and-language-ba-honours) |
| English Literature and Language with Foundation | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-literature-and-language-with-foundation-ba-honours) |
| English Literature | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-literature-ba-honours) |
| English Literature with Foundation | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-literature-with-foundation-ba-honours) |

#### 系: Health


##### BSC HONOURS

| 专业 | URL |
|---|---|
| Human Nutrition | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/human-nutrition-bsc-honours) |
| Human Nutrition with Foundation | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/human-nutrition-with-foundation-bsc-honours) |
| Public Health | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/public-health-bsc-honours) |

#### 系: History


##### BA HONOURS

| 专业 | URL |
|---|---|
| History and Politics | [link](https://www.westminster.ac.uk/history-courses/2026-27/september/full-time/history-and-politics-ba-honours) |
| History | [link](https://www.westminster.ac.uk/history-courses/2026-27/september/full-time/history-ba-honours) |
| History with Foundation | [link](https://www.westminster.ac.uk/history-courses/2026-27/september/full-time/history-with-foundation-ba-honours) |

#### 系: Languages


##### BA HONOURS

| 专业 | URL |
|---|---|
| Arabic and English | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/arabic-and-english-ba-honours) |
| Arabic and International Business | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/arabic-and-international-business-ba-honours) |
| Arabic and International Communication | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/arabic-and-international-communication-ba-honours) |
| Arabic and International Communication with Foundation | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/arabic-and-international-communication-with-foundation-ba-honours) |
| Arabic and International Relations | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/arabic-and-international-relations-ba-honours) |
| Arabic and Linguistics | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/arabic-and-linguistics-ba-honours) |
| Chinese and English | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/chinese-and-english-ba-honours) |
| Chinese and International Business | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/chinese-and-international-business-ba-honours) |
| Chinese and International Communication | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/chinese-and-international-communication-ba-honours) |
| Chinese and International Communication with Foundation | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/chinese-and-international-communication-with-foundation-ba-honours) |
| Chinese and International Relations | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/chinese-and-international-relations-ba-honours) |
| Chinese and Linguistics | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/chinese-and-linguistics-ba-honours) |
| French and International Relations | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/french-and-international-relations-ba-honours) |
| French and Linguistics | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/french-and-linguistics-ba-honours) |
| Languages and Translation | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/languages-and-translation-ba-honours) |
| Languages and Translation with Foundation | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/languages-and-translation-with-foundation-ba-honours) |
| Spanish and English | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/spanish-and-english-ba-honours) |
| Spanish and International Business | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/spanish-and-international-business-ba-honours) |
| Spanish and International Communication | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/spanish-and-international-communication-ba-honours) |
| Spanish and International Communication with Foundation | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/spanish-and-international-communication-with-foundation-ba-honours) |
| Spanish and International Relations | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/spanish-and-international-relations-ba-honours) |
| Spanish and Linguistics | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/spanish-and-linguistics-ba-honours) |

#### 系: Law


##### LLB HONOURS

| 专业 | URL |
|---|---|
| European Legal Studies | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/european-legal-studies-llb-honours) |
| Law with Foundation | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/law-with-foundation-llb-honours) |
| Law with French Law | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/law-with-french-law-llb-honours) |

#### 系: Politics & International Relations


##### BA HONOURS

| 专业 | URL |
|---|---|
| International Relations and Development | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-and-development-ba-honours) |
| International Relations and Development with Foundation | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-and-development-with-foundation-ba-honours) |
| International Relations | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-ba-honours) |
| International Relations with Foundation | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-with-foundation-ba-honours) |
| Politics and International Relations | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/politics-and-international-relations-ba-honours) |

#### 系: Psychology


##### BSC HONOURS

| 专业 | URL |
|---|---|
| Cognitive and Clinical Neuroscience | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/cognitive-and-clinical-neuroscience-bsc-honours) |
| Psychology and Criminology | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/psychology-and-criminology-bsc-honours) |
| Psychology | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/psychology-bsc-honours) |
| Psychology with Foundation | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/psychology-with-foundation-bsc-honours) |

### 学院: College of Creative Arts & Technologies


#### 系: Architecture & Interiors


##### BA HONOURS

| 专业 | URL |
|---|---|
| Architecture | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-ba-honours) |
| Architecture with Foundation | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-with-foundation-ba-honours) |
| Interior Architecture | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/interior-architecture-ba-honours) |
| Interior Architecture with Foundation | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/interior-architecture-with-foundation-ba-honours) |

##### BSC HONOURS

| 专业 | URL |
|---|---|
| Architectural Technology | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architectural-technology-bsc-honours) |
| Architectural Technology with Foundation | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architectural-technology-with-foundation-bsc-honours) |
| Architecture and Environmental Design | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-and-environmental-design-bsc-honours) |
| Architecture and Environmental Design with Foundation | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-and-environmental-design-with-foundation-bsc-honours) |

#### 系: Art & Design


##### BA HONOURS

| 专业 | URL |
|---|---|
| Animation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/animation-ba-honours) |
| Animation with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/animation-with-foundation-ba-honours) |
| Fine Art Mixed Media | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/fine-art-mixed-media-ba-honours) |
| Fine Art Mixed Media with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/fine-art-mixed-media-with-foundation-ba-honours) |
| Graphic Design with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/graphic-design-with-foundation-ba-honours) |
| Illustration | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/illustration-ba-honours) |
| Illustration with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/illustration-with-foundation-ba-honours) |
| Photography | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/photography-ba-honours) |
| Photography with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/photography-with-foundation-ba-honours) |

#### 系: Computer Science


##### BENG HONOURS

| 专业 | URL |
|---|---|
| Software Engineering | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/software-engineering-beng-honours) |
| Software Engineering with Electronics | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/software-engineering-with-electronics-beng-honours) |
| Software Engineering with Electronics with Foundation | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/software-engineering-with-electronics-with-foundation-beng-honours) |
| Software Engineering with Foundation | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/software-engineering-with-foundation-beng-honours) |

##### BSC HONOURS

| 专业 | URL |
|---|---|
| Artificial Intelligence | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/artificial-intelligence-bsc-honours) |
| Computer Science | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/computer-science-bsc-honours) |
| Computer Science with Foundation | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/computer-science-with-foundation-bsc-honours) |
| Cyber Security and Forensics | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/cyber-security-and-forensics-bsc-honours) |
| Cyber Security and Forensics with Foundation | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/cyber-security-and-forensics-with-foundation-bsc-honours) |

#### 系: Construction & Surveying


##### BSC HONOURS

| 专业 | URL |
|---|---|
| Construction Management | [link](https://www.westminster.ac.uk/construction-surveying-and-real-estate-courses/2026-27/september/full-time/construction-management-bsc-honours) |
| Construction Management with Foundation | [link](https://www.westminster.ac.uk/construction-surveying-and-real-estate-courses/2026-27/september/full-time/construction-management-with-foundation-bsc-honours) |
| Quantity Surveying and Commercial Management | [link](https://www.westminster.ac.uk/construction-surveying-and-real-estate-courses/2026-27/september/full-time/quantity-surveying-and-commercial-management-bsc-honours) |

#### 系: Fashion


##### BA HONOURS

| 专业 | URL |
|---|---|
| Fashion Business Management with Professional Experience | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/fashion-business-management-with-professional-experience-ba-honours) |
| Fashion Design | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/fashion-design-ba-honours) |
| Fashion Design with Foundation | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/fashion-design-with-foundation-ba-honours) |
| Fashion Marketing and Promotion | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/fashion-marketing-and-promotion-ba-honours) |
| Fashion Marketing and Promotion with Foundation | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/fashion-marketing-and-promotion-with-foundation-ba-honours) |
| Fashion Photography | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/fashion-photography-ba-honours) |
| Fashion Photography with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/fashion-photography-with-foundation-ba-honours) |

#### 系: Film & Television


##### BA HONOURS

| 专业 | URL |
|---|---|
| Film and Television Production | [link](https://www.westminster.ac.uk/film-and-television-courses/2026-27/september/full-time/film-and-television-production-ba-honours) |
| Film | [link](https://www.westminster.ac.uk/film-and-television-courses/2026-27/september/full-time/film-ba-honours) |

#### 系: Games


##### BA HONOURS

| 专业 | URL |
|---|---|
| Games Art | [link](https://www.westminster.ac.uk/games-courses/2026-27/september/full-time/games-art-ba-honours) |

##### BSC HONOURS

| 专业 | URL |
|---|---|
| Computer Games Development | [link](https://www.westminster.ac.uk/games-courses/2026-27/september/full-time/computer-games-development-bsc-honours) |
| Computer Games Development with Foundation | [link](https://www.westminster.ac.uk/games-courses/2026-27/september/full-time/computer-games-development-with-foundation-bsc-honours) |

#### 系: Media & Communication


##### BA HONOURS

| 专业 | URL |
|---|---|
| Creative Media Arts | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/creative-media-arts-ba-honours) |
| Creative Media Arts with Foundation | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/creative-media-arts-with-foundation-ba-honours) |
| Digital Media and Communication | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/digital-media-and-communication-ba-honours) |
| Digital Media and Journalism | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/digital-media-and-journalism-ba-honours) |


---

## 2. 研究生项目 (Postgraduate — 97 programs)

### 2.1 学院分布

| 学院 | PG 项目数 |
|------|------|
| Westminster Business School | 19 |
| College of Liberal Arts & Sciences | 38 |
| College of Creative Arts & Technologies | 40 |
| **Total** | **97** |

### 2.2 学历级别分布 (PG)

| 学历级别 | 数量 |
|----------|------|
| MA | 42 |
| MSc | 34 |
| LLM | 6 |
| MBA | 2 |
| MFA | 1 |
| MArch RIBA Part II | 1 |
| PGDip (multiple types) | 6 |
| PGCert (multiple types) | 3 |

### 2.3 Full PG Program List (by College → Department → Degree → Program)


### 学院: Westminster Business School


#### 系: Accounting & Finance


##### LLM

| 专业 | URL |
|---|---|
| Corporate Finance Law | [link](https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/corporate-finance-law-llm) |

##### MSc

| 专业 | URL |
|---|---|
| Accounting and Finance | [link](https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-msc) |
| Fintech with Business Analytics | [link](https://www.westminster.ac.uk/accounting-and-finance-business-and-management-courses/2026-27/september/full-time/fintech-with-business-analytics-msc) |

#### 系: Business & Management


##### MA

| 专业 | URL |
|---|---|
| Business of Film | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-of-film-ma) |

##### MBA

| 专业 | URL |
|---|---|
| Master of Business Administration | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/master-of-business-administration-mba) |
| Master of Business Administration with Professional Experience | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/master-of-business-administration-with-professional-experience-mba) |

##### MSc

| 专业 | URL |
|---|---|
| International Business and Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/international-business-and-management-msc) |
| International Business and Management with Professional Experience | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/international-business-and-management-with-professional-experience-msc) |
| Investment and Financial Risk Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/investment-and-financial-risk-management-msc) |
| Project Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/project-management-msc) |

#### 系: Economics


##### MSc

| 专业 | URL |
|---|---|
| Economic Policy and Analysis | [link](https://www.westminster.ac.uk/economics-courses/2026-27/september/full-time/economic-policy-and-analysis-msc) |
| Economics | [link](https://www.westminster.ac.uk/economics-courses/2026-27/september/full-time/economics-msc) |

#### 系: Marketing


##### MA

| 专业 | URL |
|---|---|
| Human Resource Management | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/human-resource-management-ma) |
| International Human Resource Management | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/international-human-resource-management-ma) |

##### MSc

| 专业 | URL |
|---|---|
| Digital Marketing Management | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/digital-marketing-management-msc) |
| Marketing Communications Ma | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/marketing-communications-ma-msc) |
| Marketing Management Ma | [link](https://www.westminster.ac.uk/marketing-courses/2026-27/september/full-time/marketing-management-ma-msc) |

#### 系: Tourism & Events


##### MA

| 专业 | URL |
|---|---|
| Event Design and Management | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/event-design-and-management-ma) |
| Tourism Management | [link](https://www.westminster.ac.uk/tourism-and-events-management-courses/2026-27/september/full-time/tourism-management-ma) |

### 学院: College of Liberal Arts and Sciences


#### 系: Biomedical Sciences


##### MSc

| 专业 | URL |
|---|---|
| Applied Biotechnology | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/applied-biotechnology-msc) |
| Pharmaceutical Science | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/pharmaceutical-science-msc) |

#### 系: Criminology & Sociology


##### MA

| 专业 | URL |
|---|---|
| Cultural and Critical Studies | [link](https://www.westminster.ac.uk/criminology-and-sociology-courses/2026-27/september/full-time/cultural-and-critical-studies-ma) |

#### 系: Data Science & Informatics


##### MSc

| 专业 | URL |
|---|---|
| Data and Marketing Analytics | [link](https://www.westminster.ac.uk/data-science-and-informatics-courses/2026-27/september/full-time/data-and-marketing-analytics-msc) |
| Data Science and Analytics | [link](https://www.westminster.ac.uk/data-science-and-informatics-courses/2026-27/september/full-time/data-science-and-analytics-msc) |
| Environmental Sustainability and Data Science | [link](https://www.westminster.ac.uk/data-science-and-informatics-courses/2026-27/september/full-time/environmental-sustainability-and-data-science-msc) |

#### 系: English & Creative Writing


##### MA

| 专业 | URL |
|---|---|
| Creative Writing Writing the City | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/creative-writing-writing-the-city-ma) |
| English Language and Literature | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-language-and-literature-ma) |
| English Literature Modern and Contemporary Fictions | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/english-literature-modern-and-contemporary-fictions-ma) |
| Professional Writing | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/professional-writing-ma) |
| Professional Writing with Extended Work Placement | [link](https://www.westminster.ac.uk/english-and-creative-writing-courses/2026-27/september/full-time/professional-writing-with-extended-work-placement-ma) |

#### 系: Health


##### MSc

| 专业 | URL |
|---|---|
| Biomedical Science | [link](https://www.westminster.ac.uk/biological-and-biomedical-sciences-courses/2026-27/september/full-time/biomedical-science-msc) |
| Digital Health and Cyberpsychology | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/digital-health-and-cyberpsychology-msc) |
| Global Public Health with Data Science | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/global-public-health-with-data-science-msc) |
| Health Psychology | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/health-psychology-msc) |
| Sport and Exercise Nutrition | [link](https://www.westminster.ac.uk/health-courses/2026-27/september/full-time/sport-and-exercise-nutrition-msc) |

#### 系: Languages


##### MA

| 专业 | URL |
|---|---|
| Digital and Multilingual Communication | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/digital-and-multilingual-communication-ma) |
| Specialised Translation | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/specialised-translation-ma) |
| Specialised Translation with Professional Experience | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/specialised-translation-with-professional-experience-ma) |
| Teaching English to Speakers of Other Languages Tesol | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/teaching-english-to-speakers-of-other-languages-tesol-ma) |
| Translation and Interpreting | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/translation-and-interpreting-ma) |
| Translation and Interpreting with Professional Experience | [link](https://www.westminster.ac.uk/languages-courses/2026-27/september/full-time/translation-and-interpreting-with-professional-experience-ma) |

#### 系: Law


##### LLM

| 专业 | URL |
|---|---|
| International and Commercial Dispute Resolution Law | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/international-and-commercial-dispute-resolution-law-llm) |
| International Commercial and Corporate Law | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/international-commercial-and-corporate-law-llm) |
| International Law | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/international-law-llm) |
| Law and Technology | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/law-and-technology-llm) |
| Legal Practice | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/legal-practice-llm) |

##### PGDip Legal Practice

| 专业 | URL |
|---|---|
| Legal Practice Postgraduate Diploma | [link](https://www.westminster.ac.uk/law-courses/2026-27/september/full-time/legal-practice-postgraduate-diploma) |

#### 系: Politics & International Relations


##### MA

| 专业 | URL |
|---|---|
| Diplomacy and Global Politics | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/diplomacy-and-global-politics-ma) |
| International Relations and Democratic Politics | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-and-democratic-politics-ma) |
| International Relations and Security | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-and-security-ma) |
| International Relations | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/international-relations-ma) |
| Public Policy and Management | [link](https://www.westminster.ac.uk/politics-and-international-relations-courses/2026-27/september/full-time/public-policy-and-management-ma) |

#### 系: Psychology


##### MSc

| 专业 | URL |
|---|---|
| Business and Organisational Psychology | [link](https://www.westminster.ac.uk/business-and-management-courses/2026-27/september/full-time/business-and-organisational-psychology-msc) |
| Counselling and Psychotherapy Top Up | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/counselling-and-psychotherapy-top-up-msc) |
| Forensic Psychology | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/forensic-psychology-msc) |
| Psychology | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/psychology-msc) |

##### PGDip Counselling

| 专业 | URL |
|---|---|
| Counselling and Psychotherapy Pgdip | [link](https://www.westminster.ac.uk/psychology-courses/2026-27/september/full-time/counselling-and-psychotherapy-pgdip) |

### 学院: College of Creative Arts & Technologies


#### 系: Architecture & Interiors


##### MA

| 专业 | URL |
|---|---|
| Architecture and Sustainable Heritage | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-and-sustainable-heritage-ma) |
| Architecture | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-ma) |

##### MArch RIBA Part II

| 专业 | URL |
|---|---|
| Master of Architecture March Riba Pt Ii | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/master-of-architecture-march-riba-pt-ii) |

##### PGDip RIBA Part III

| 专业 | URL |
|---|---|
| Architecture Postgraduate Diploma Professional Practice Riba Part Iii | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/architecture-postgraduate-diploma-professional-practice-riba-part-iii) |

#### 系: Architecture & Planning


##### MA

| 专业 | URL |
|---|---|
| International Planning and Sustainable Development | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/international-planning-and-sustainable-development-ma) |
| Urban and Regional Planning | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/urban-and-regional-planning-ma) |
| Urban Design | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/urban-design-ma) |

##### PGCert Urban Design

| 专业 | URL |
|---|---|
| Urban Design Postgraduate Certificate | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/urban-design-postgraduate-certificate) |

##### PGDip Urban Design

| 专业 | URL |
|---|---|
| Urban Design Postgraduate Diploma | [link](https://www.westminster.ac.uk/architecture-interiors-and-planning-courses/2026-27/september/full-time/urban-design-postgraduate-diploma) |

#### 系: Art & Design


##### MA

| 专业 | URL |
|---|---|
| Expanded Photography | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/expanded-photography-ma) |

#### 系: Computer Science


##### MSc

| 专业 | URL |
|---|---|
| Applied Artificial Intelligence | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/applied-artificial-intelligence-msc) |
| Artificial Intelligence and Digital Health | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/artificial-intelligence-and-digital-health-msc) |
| Cyber Security and Forensics | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/cyber-security-and-forensics-msc) |
| Software Engineering Conversion | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/software-engineering-conversion-msc) |

#### 系: Construction & Surveying


##### MSc

| 专业 | URL |
|---|---|
| Construction Project Management | [link](https://www.westminster.ac.uk/construction-surveying-and-real-estate-courses/2026-27/september/full-time/construction-project-management-msc) |

#### 系: Fashion


##### MA

| 专业 | URL |
|---|---|
| Menswear | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/menswear-ma) |

##### MFA

| 专业 | URL |
|---|---|
| Menswear with Professional Experience | [link](https://www.westminster.ac.uk/fashion-courses/2026-27/september/full-time/menswear-with-professional-experience-mfa) |

#### 系: Film & Television


##### MA

| 专业 | URL |
|---|---|
| Film Television and Moving Image | [link](https://www.westminster.ac.uk/film-and-television-courses/2026-27/september/full-time/film-television-and-moving-image-ma) |

#### 系: Games


##### MA

| 专业 | URL |
|---|---|
| Audio Production | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/audio-production-ma) |

#### 系: Media & Communication


##### MA

| 专业 | URL |
|---|---|
| Ai Data and Communication | [link](https://www.westminster.ac.uk/computer-science-and-engineering-courses/2026-27/september/full-time/ai-data-and-communication-ma) |
| Art and Visual Culture | [link](https://www.westminster.ac.uk/art-design-and-visual-culture-courses/2026-27/september/full-time/art-and-visual-culture-ma) |
| Digital Media Storytelling and Production | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/digital-media-storytelling-and-production-ma) |
| Journalism Lifestyle Arts and Culture | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/journalism-lifestyle-arts-and-culture-ma) |
| Journalism Multiplatform News | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/journalism-multiplatform-news-ma) |
| Media and Communication | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/media-and-communication-ma) |
| Media Campaigning and Social Change | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/media-campaigning-and-social-change-ma) |
| Museums Galleries and Contemporary Culture | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/museums-galleries-and-contemporary-culture-ma) |
| Museums Galleries and Contemporary Culture with Professional Experience | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/museums-galleries-and-contemporary-culture-with-professional-experience-ma) |
| Social Media and Digital Communication | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/social-media-and-digital-communication-ma) |

##### MSc

| 专业 | URL |
|---|---|
| Media Business and Creative Enterprise Ma | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/media-business-and-creative-enterprise-ma-msc) |
| Public Relations Ma | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/public-relations-ma-msc) |

##### PGCert Social Change

| 专业 | URL |
|---|---|
| Media Campaigning and Social Change Pg Certificate | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/media-campaigning-and-social-change-pg-certificate) |

##### PGDip Journalism

| 专业 | URL |
|---|---|
| Journalism Lifestyle Arts and Culture Pg Diploma | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/journalism-lifestyle-arts-and-culture-pg-diploma) |
| Journalism Multiplatform News Pg Diploma | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/journalism-multiplatform-news-pg-diploma) |

##### PGDip Social Change

| 专业 | URL |
|---|---|
| Media Campaigning and Social Change Pg Diploma | [link](https://www.westminster.ac.uk/media-and-communication-courses/2026-27/september/full-time/media-campaigning-and-social-change-pg-diploma) |

#### 系: Music


##### MA

| 专业 | URL |
|---|---|
| Music Business Management | [link](https://www.westminster.ac.uk/music-courses/2026-27/september/full-time/music-business-management-ma) |

#### 系: Transport & Logistics


##### MSc

| 专业 | URL |
|---|---|
| Air Transport Planning and Management | [link](https://www.westminster.ac.uk/transport-and-logistics-courses/2026-27/september/full-time/air-transport-planning-and-management-msc) |
| Transport Planning | [link](https://www.westminster.ac.uk/transport-and-logistics-courses/2026-27/september/full-time/transport-planning-msc) |

##### PGCert Transport Planning

| 专业 | URL |
|---|---|
| Transport Planning Pg Certificate | [link](https://www.westminster.ac.uk/transport-and-logistics-courses/2026-27/september/full-time/transport-planning-pg-certificate) |

##### PGDip Transport Planning

| 专业 | URL |
|---|---|
| Transport Planning Pg Diploma | [link](https://www.westminster.ac.uk/transport-and-logistics-courses/2026-27/september/full-time/transport-planning-pg-diploma) |


---

## 3. 申请要求 (Application Requirements)

### 3.1 本科入学要求 (UG Entry Requirements)

| 项目 | 要求 |
|------|------|
| A-levels | Typical offer: **BBC-AAA** depending on course (most courses require **112-136 UCAS Tariff points**) |
| International Baccalaureate | Typical: **27-34 points** |
| BTEC | DMM-DDM accepted |
| GCSE | English and Maths at grade C/4 or above (specific courses require higher) |
| UCAS code format | W01 (Westminster institution code) |
| UCAS application | Required via UCAS for full-time UG |

### 3.2 研究生入学要求 (PG Entry Requirements)

| 项目 | 要求 |
|------|------|
| Undergraduate degree | **2:2 (Lower Second Class)** or above from a UK university, or equivalent overseas qualification |
| Other qualifications | Professional qualifications, relevant work experience may be considered |
| Work experience | Some courses (e.g., MBA) require **minimum 3 years** professional experience |

### 3.3 英语语言要求 (English Language Requirements)

| 课程类型 | IELTS Academic | 单项分数 |
|----------|----------------|----------|
| **UG (大多数本科课程)** | **6.0 overall** | with **5.5 in each component** |
| **PG (大多数研究生课程)** | **6.5 overall** | with **6.0 in each component** |
| LLM / Law / some PG | **7.0 overall** | with **6.5 in each component** (some courses higher) |
| Foundation year | **5.5 overall** | with **5.0 in each component** |
| Pre-sessional English | Available (online + on-campus) | To develop English to required level before course start |

**English tests accepted** (in addition to IELTS): TOEFL iBT, PTE Academic, Cambridge C1 Advanced/C2 Proficiency, Trinity College London (ISE).

**证据来源**: https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-bsc-honours
- UG: "IELTS 6.0 overall, with 5.5 in each component. Please note we accept a wide range of English language qualifications"
- PG: "IELTS 6.5 overall, with a minimum of 6.0 in each component"

---

## 4. 学费与费用 (Tuition & Fees)

### 4.1 本科国际生学费 (UG International Tuition — 2026/27)

| 课程类型 | 国际生年学费 (GBP) |
|----------|---------------------|
| UG Lab-based (含 STEM, Architecture 等) | **£17,600 / year** |
| UG Non-lab (含文科、商科等) | **£17,600 / year** (Westminster applies flat-rate for international UG) |
| Foundation year | **£17,600 / year** (standalone or integrated) |

### 4.2 研究生国际生学费 (PG International Tuition — 2026/27)

| 课程类型 | 国际生年学费 (GBP) |
|----------|---------------------|
| PG Lab-based (STEM, Architecture, Computing) | **£18,000 / year** |
| PG Non-lab (humanities, business, social sciences) | **£14,900 / year** |
| MBA | **Higher fee band** (consult program page) |

### 4.3 UK 本土学生学费 (UK Home Fees — 2026/27)

| 课程类型 | 英国本土学生年学费 (GBP) |
|----------|--------------------------|
| UG (full-time, regulated fee) | **£9,790 / year** |
| PG (varies by course) | Typically **£6,000-£12,000** depending on program |
| Placement year | **£4,500** (additional) |

### 4.4 其他费用

| 项目 | 金额 |
|------|------|
| Application fee (international UG via UCAS) | £28.50 (single choice) / £28.50 additional choices |
| Application fee (PG via direct application) | Generally none, but some courses have £50-£100 admin fee |
| Confirmation deposit | Required for international students (refundable, deducted from tuition) |

**证据来源**:
- https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-bsc-honours
  - Snippet: "Fees ... £9,790 ... £17,600 ... £4,500"
- https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-msc
  - Snippet: "£14,900 ... £18,000 ... £2,000"

---

## 5. 申请截止日期 (Application Deadlines)

### 5.1 UCAS UG 截止日期 (UK/EU students)

| 截止类型 | 日期 |
|----------|------|
| **UCAS Extra / Clearing opens** | July 2026 (after A-level results day ~ mid-August) |
| UCAS main scheme deadline (equal consideration) | 27 January 2027 (for 2027-28 entry) |
| UCAS late applications | After 27 January — considered on individual basis |
| Westminster Foundation Course intake | September 2026 / January 2027 |

### 5.2 研究生截止日期 (PG)

| 课程类型 | 截止日期 |
|----------|----------|
| International PG (most courses) | Rolling admissions — apply at least **3 months before start date** |
| MBA / competitive courses | **June-July 2026** (for September 2026 intake) |
| January 2027 intake | Application deadline typically **November 2026** |
| September 2027 intake | Application deadline typically **June-July 2027** |

### 5.3 Start dates (2026/27 academic year)

- **September 2026** (main intake)
- **January 2027** (limited courses — mostly PG Business)
- **September 2027** (next academic year)

---

## 6. WeKnora Chunk Import Manifest

Each section in this document corresponds to a separate WeKnora chunk for efficient retrieval:

| Chunk ID | Section | Content |
|----------|---------|---------|
| WST-00-OVERVIEW | 0 | Five structural rules, distribution matrix, hierarchy tree |
| WST-01-UG-LIST | 1 | All 134 UG programs grouped by college → dept → degree |
| WST-02-PG-LIST | 2 | All 97 PG programs grouped by college → dept → degree |
| WST-03-REQUIREMENTS | 3 | Entry requirements (UG/PG), English language |
| WST-04-FEES | 4 | Tuition, UK home + international UG/PG |
| WST-05-DEADLINES | 5 | UCAS UG deadlines, PG deadlines, start dates |
| WST-06-MONITORING | 7 | Monitoring watchlist + change frequency classification |

---

## 7. 监控设计 (Monitoring Watchlist)

URL frequency classification for change detection.

### 7.1 High frequency (re-check monthly)

| URL | Why | Capture method |
|-----|-----|----------------|
| https://www.westminster.ac.uk/study/fees-and-funding | Tuition changes annually in Sept | Curl + grep £ amounts |
| https://www.westminster.ac.uk/course-search?f[0]=course_type%3A926 | UG course list additions | Curl + count course hrefs |
| https://www.westminster.ac.uk/course-search?f[0]=course_type%3A26 | PG course list additions | Curl + count course hrefs |

### 7.2 Medium frequency (re-check quarterly)

| URL | Why |
|-----|-----|
| https://www.westminster.ac.uk/study/undergraduate | UG landing — new courses, marketing changes |
| https://www.westminster.ac.uk/study/postgraduate | PG landing |
| https://www.westminster.ac.uk/about-us/our-university/our-colleges-and-schools | College hierarchy changes |

### 7.3 Low frequency (re-check annually)

| URL | Why |
|-----|-----|
| https://www.westminster.ac.uk/about-us | About university, history |
| https://www.westminster.ac.uk/about-us/contact-us | Contact details |
| https://www.westminster.ac.uk/about-us/visit-us | Campus locations |

### 7.4 Content hash baseline (computed 2026-07-08)

For each course page, normalize title + tuition + IELTS + duration and hash. On re-extract, compare to detect silent changes. Implementation stored in uni-cache/schools/westminster/content-hashes.json.

---

## 8. Source URLs (Evidence Chain)

### 8.1 Primary source

- **Course search (all programs)**: https://www.westminster.ac.uk/course-search
  - UG filter: ?f[0]=course_type%3A926 (40 pages, 134 unique 2026-27 programs)
  - PG filter: ?f[0]=course_type%3A26 (44 pages, 97 unique 2026-27 programs)
  - Short courses: ?f[0]=course_type%3A3551 (10 pages — not included in this doc)
  - Foundation courses: combined with UG

### 8.2 Sample program detail pages (used for fee and IELTS extraction)

- UG: https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-bsc-honours
- PG: https://www.westminster.ac.uk/accounting-and-finance-courses/2026-27/september/full-time/accounting-and-finance-msc

### 8.3 Subjects A-Z (organised by college)

- https://www.westminster.ac.uk/study/subjects (25 subjects cross-cutting 3 colleges)

### 8.4 Colleges and Schools

- https://www.westminster.ac.uk/about-us/our-university/our-colleges-and-schools
  - College of Creative Arts and Technologies
  - College of Liberal Arts and Sciences
  - Westminster Business School

---

## 9. Data Quality Notes

- **Reconciliation verified**: Rule-1 total (231) == matrix cell sum (231) == rows in grouped tables (231). OK
- **Degree parsing**: All 231 programs have a parsed degree (no empty values remaining).
- **Department mapping**: All 231 programs mapped to one of 26 departments.
- **URL coverage**: All 231 programs have a constructed course-search URL (verified against sample URLs that resolved to live course pages).
- **Fee extraction**: Verified against 2 sample programs (UG Accounting and Finance BSc, PG Accounting and Finance MSc). Other courses fees not individually verified — should be assumed to be in the same band unless course page indicates otherwise.
- **English requirements**: Verified against same 2 sample programs. Some courses (LLM, Architecture Part II) require higher (7.0+).

### Missing / Limitations

- **Foundation courses (separate foundation year programs)**: These are integrated as "with Foundation" variants of UG programs; standalone Westminster Foundation Courses may exist as a separate route (https://www.westminster.ac.uk/study/undergraduate/westminster-foundation-courses) — not enumerated individually here.
- **Research degrees (MPhil/PhD by research)**: Not included in the 231 count; covered separately at https://www.westminster.ac.uk/study/postgraduate/research-degrees
- **Short courses**: Not included (separate course type 3551).
- **Course duration**: Not extracted at individual program level; most UG are 3 years (4 with sandwich/placement), most PG are 1 year FT / 2 years PT.
- **Per-course IELTS**: Standard UG 6.0/5.5, PG 6.5/6.0 assumed; individual variation exists for LLM, Architecture Part II, etc.

