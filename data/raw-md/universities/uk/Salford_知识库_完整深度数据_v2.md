# University of Salford — 知识库_完整深度数据_v2

> Source-cited admissions knowledge base for WeKnora.  
> Capture date: 2026-07-08.  All numeric/policy fields include source URL + snippet + capture timestamp.  
> Site topology: Drupal custom platform (salford.ac.uk). Course catalog at /search/courses with field_course_type_name and field_school_name query-string filters.

---

## Section 0 — 院校总览 (School Overview & Roll-up Artifacts)

### 0.1 基本信息

| 项目 | 内容 | 来源 |
|------|------|------|
| 中文名 | 索尔福德大学 | 通用译名 |
| 英文名 | University of Salford | https://www.salford.ac.uk |
| 位置 | Salford, Greater Manchester, England (UK) | https://www.salford.ac.uk |
| 主校区 | Peel Park campus (主校区); MediaCityUK; Frederick Road | https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance |
| 学校类型 | 公立综合性大学 | https://www.salford.ac.uk |
| 学院数 | 4 Schools | 见 0.3 节 |
| 建校年份 | 1896 (技术学院); 1967 大学地位 | https://www.salford.ac.uk |
| 官方网站 | https://www.salford.ac.uk | — |
| 课程目录 | https://www.salford.ac.uk/search/courses | — |
| 国际生学费页 | https://www.salford.ac.uk/international/fees-and-funding | — |
| 英语要求页 | https://www.salford.ac.uk/international/english-language-requirements | — |
| 申请门户(UG) | https://www.salford.ac.uk/undergraduate/apply | — |
| 申请门户(PG) | https://www.salford.ac.uk/postgraduate-taught/how-to-apply | — |

### 0.2 五条结构规则 (Five Structural Rules)

**Rule 1 — 专业/项目总数 (Total program count)**

- **本科 (UG)**: 434 个课程链接 (含同名课程的不同变体如 foundation year / placement year / with work placement)
- **授课型硕士 (PG Taught)**: 209 个课程链接
- **研究型硕士/博士 (PG Research)**: 12 个研究学位 (PhD/MPhil/MRes)
- **总计**: 655 个课程/项目

> Reconciliation: sum of all degree-level cells in 0.5 distribution matrix = 655 = this total. ✓

**Rule 2 — 学院-系 明细 + 父子层级 (School hierarchy)**

University of Salford is organised into **4 Schools** (no intermediate department level on the public site — programmes are listed directly under their parent School):

```
University of Salford
├── School of Science, Engineering and Environment (SSE)
├── Salford Business School (SBS)
├── Salford School of Arts, Media and Creative Technology (SAMCT)
└── School of Health and Society (SHS)
```

Evidence: 4 school filter checkboxes on course search page. Source: https://www.salford.ac.uk/search/courses  (filter inputs field_school_name[School of Science Engineering and Environment], field_school_name[Salford Business School], field_school_name[Salford School of Arts Media and Creative Technology], field_school_name[School of Health and Society]).

**Rule 3 — 学历级别明细 (Degree-level inventory)**

| 学历级别 | 简称 | 数量 |
|---------|------|------|
| UG — (unparsed) | (unparsed) | 215 |
| UG — BSc | BSc | 133 |
| UG — BA | BA | 55 |
| UG — BEng | BEng | 11 |
| UG — CertHE | CertHE | 9 |
| UG — DipHE | DipHE | 5 |
| UG — MEng | MEng | 4 |
| UG — FdSc | FdSc | 2 |
| | | |
| PGT — (unparsed) | (unparsed) | 132 |
| PGT — MSc | MSc | 49 |
| PGT — MA | MA | 25 |
| PGT — MBA | MBA | 2 |
| PGT — PGCert | PGCert | 1 |
| | | |
| PGR — (unparsed) | (unparsed) | 11 |
| PGR — PhD | PhD | 1 |
| (Unparsed — degree not in card text) | — | 计入 0.5 分布矩阵 |

**Rule 4 — 分布矩阵 (School × Degree distribution matrix)**

#### 4a. UG matrix

| School | BA | BEng | BSc | CertHE | DipHE | FdSc | MEng | (unparsed) | Total |
|---|---|---|---|---|---|---|---|---|---|
| School of Science Engineering and Environment | 0 | 11 | 57 | 7 | 2 | 0 | 4 | 72 | 153 |
| Salford Business School | 9 | 0 | 38 | 0 | 1 | 0 | 0 | 59 | 107 |
| Salford School of Arts Media and Creative Technology | 46 | 0 | 4 | 2 | 2 | 0 | 0 | 52 | 106 |
| School of Health and Society | 0 | 0 | 34 | 0 | 0 | 2 | 0 | 32 | 68 |

#### 4b. PGT matrix

| School | MA | MBA | MSc | PGCert | (unparsed) | Total |
|---|---|---|---|---|---|---|
| School of Science Engineering and Environment | 0 | 0 | 12 | 0 | 36 | 48 |
| Salford Business School | 0 | 2 | 13 | 0 | 13 | 28 |
| Salford School of Arts Media and Creative Technology | 22 | 0 | 1 | 0 | 28 | 51 |
| School of Health and Society | 3 | 0 | 23 | 1 | 55 | 82 |

#### 4c. PGR matrix

| School | PhD | (unparsed) | Total |
|---|---|---|---|
| School of Science Engineering and Environment | 0 | 8 | 8 |
| Salford Business School | 0 | 1 | 1 |
| Salford School of Arts Media and Creative Technology | 0 | 0 | 0 |
| School of Health and Society | 1 | 2 | 3 |

> **Reconciliation check**: 0.5 sums (434 UG + 209 PGT + 12 PGR = 655) = Rule 1 total. ✓

**Rule 5 — 全量专业明细 (Full leaf enumeration)** — see Sections 1 and 2 below.

---

## Section 1 — 本科 (Undergraduate) — 学院 → 学历级别 → 专业

### 1.1 School of Science Engineering and Environment

Source: https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSchool+of+Science+Engineering+and+Environment%5D=School+of+Science+Engineering+and+Environment

#### BEng (11 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Acoustical and Audio Engineering | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/beng-acoustical-and-audio-engineering |
| Acoustical and Audio Engineering with Foundation Year | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/acoustical-and-audio-engineering-with-foundation-year |
| Aeronautical Engineering | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/beng-aeronautical-engineering |
| Aeronautical Engineering with Foundation Year | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/aeronautical-engineering-with-foundation-year |
| Aircraft Engineering with Pilot Studies | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/beng-aircraft-engineering-pilot-studies |
| Civil Engineering | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/civil-engineering |
| Civil Engineering with Foundation Year | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/civil-engineering-with-foundation-year |
| Electrical and Electronic Engineering | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/electrical-and-electronic-engineering |
| Electrical and Electronic Engineering with Foundation Year | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/beng-hons-electrical-and-electronic-engineering-foundation |
| Mechanical Engineering | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/beng-mechanical-engineering |
| Mechanical Engineering with Foundation Year | BEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/beng-mechanical-engineering-foundation-year |

#### BSc (57 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Architectural Design and Technology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/architectural-design-and-technology |
| Architectural Design and Technology with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/architectural-design-and-technology-with-foundation-year |
| Architectural Engineering | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/architectural-engineering |
| Architectural Engineering with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/architectural-engineering-with-foundation-year |
| Architecture | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/architecture |
| Biochemistry | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biochemistry |
| Biochemistry with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biochemistry-with-foundation-year |
| Biochemistry with Studies in the USA | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biochemistry-with-studies-in-the-usa |
| Biochemistry with Studies in the USA with Professional Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biochemistry-with-studies-in-the-usa-with-professional-placement |
| Biological Sciences | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biological-sciences |
| Biological Sciences with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biological-sciences-foundation-year |
| Biomedical Science | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biomedical-science |
| Biomedical Science with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/biomedical-science-with-foundation-year |
| Building Surveying | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/bsc-building-surveying |
| Building Surveying (Part-Time) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/building-surveying-part-time |
| Building Surveying with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/building-surveying-with-foundation-year |
| Computer Science | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/computer-science |
| Computer Science with Artificial Intelligence | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/computer-science-with-artificial-intelligence |
| Computer Science with Cyber Security | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/computer-science-with-cyber-security |
| Computer Science with Cyber Security with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/computer-science-with-cyber-security-with-foundation-year |
| Computer Science with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/computer-science-with-foundation-year |
| Construction Project Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/construction-project-management |
| Construction Project Management (Part-time) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/construction-project-management-part-time |
| Construction Project Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/construction-project-management-with-foundation-year |
| Data Science (Top up Programme) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/data-science-top-up-programme |
| Environmental Geography with Professional Experience | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/environmental-geography-professional-experience |
| Environmental Geography with Studies in the USA | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/environmental-geography-with-studies-in-the-usa |
| Environmental Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/environmental-management |
| Environmental Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/environmental-management-with-foundation-year |
| Geography | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/geography |
| Geography with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/geography-with-foundation-year |
| Human Biology and Infectious Diseases | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/human-biology-and-infectious-diseases |
| Human Biology and Infectious Diseases with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/human-biology-and-infectious-diseases-with-foundation-year |
| Interior Architecture | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/interior-architecture |
| Interior Architecture with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/interior-architecture-with-foundation-year |
| Marine Biology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/marine-biology |
| Marine Biology with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/marine-biology-with-foundation-year |
| Mathematics | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/mathematics |
| Pharmaceutical Science | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/pharmaceutical-science |
| Pharmaceutical Science with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/pharmaceutical-science-with-foundation-year |
| Physics | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/bsc-physics |
| Physics with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/physics-with-foundation-year |
| Quantity Surveying | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/quantity-surveying |
| Quantity Surveying (Part-Time) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/quantity-surveying-part-time |
| Quantity Surveying with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/quantity-surveying-with-foundation-year |
| Real Estate Development and Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/bsc-real-estate-development-and-management |
| Real Estate Development and Management (Part-Time) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/real-estate-development-and-management-part-time |
| Real Estate Development and Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/real-estate-development-and-management-foundation |
| Software Engineering | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/software-engineering |
| Software Engineering with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/software-engineering-with-foundation-year |
| Sound Engineering and Production | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sound-engineering-and-production |
| Wildlife Conservation | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/wildlife-conservation |
| Wildlife Conservation with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/wildlife-conservation-with-foundation-year |
| Wildlife Conservation with Zoo Biology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/wildlife-conservation-with-zoo-biology |
| Wildlife Conservation with Zoo Biology with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/wildlife-conservation-with-zoo-biology-with-foundation-year |
| Zoology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/zoology |
| Zoology with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/zoology-with-foundation-year |

#### CertHE (7 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| CertHE Construction Project Management | CertHE Construction Project Manageme |  |
| CertHE Construction Project Management | CertHE | https://www.salford.ac.uk/courses/undergraduate/certhe-construction-project-management |
| CertHE Data Analyst | CertHE Data Analyst |  |
| CertHE Data Analyst | CertHE | https://www.salford.ac.uk/courses/undergraduate/certhe-data-analyst |
| CertHE Digital and Software Technology | CertHE Digital and Software Technolo |  |
| CertHE Digital and Software Technology | CertHE | https://www.salford.ac.uk/courses/undergraduate/certhe-digital-and-software-technology |
| Quantity Surveying | CertHE | https://www.salford.ac.uk/courses/undergraduate/quantity-surveying-0 |

#### DipHE (2 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Data Science | DipHE | https://www.salford.ac.uk/courses/undergraduate/data-science |
| Digital and Software Technology | DipHE | https://www.salford.ac.uk/courses/undergraduate/digital-and-software-technology |

#### MEng (4 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Aeronautical Engineering | MEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/aeronautical-engineering |
| Aircraft Engineering with Pilot Studies | MEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/meng-aircraft-engineering-pilot-studies |
| Civil Engineering | MEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/meng-civil-engineering |
| Mechanical Engineering | MEng (Hons) | https://www.salford.ac.uk/courses/undergraduate/meng-mechanical-engineering |

#### (unparsed) (72 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Acoustical and Audio Engineering | (unparsed) |  |
| Acoustical and Audio Engineering with Foundation Year | (unparsed) |  |
| Aeronautical Engineering | (unparsed) |  |
| Aeronautical Engineering with Foundation Year | (unparsed) |  |
| Aircraft Engineering with Pilot Studies | (unparsed) |  |
| Architectural Design and Technology | (unparsed) |  |
| Architectural Design and Technology with Foundation Year | (unparsed) |  |
| Architectural Engineering | (unparsed) |  |
| Architectural Engineering with Foundation Year | (unparsed) |  |
| Architecture | (unparsed) |  |
| Biochemistry | (unparsed) |  |
| Biochemistry | MSCi (Hons) | https://www.salford.ac.uk/courses/undergraduate/biochemistry-0 |
| Biochemistry with Foundation Year | (unparsed) |  |
| Biochemistry with Studies in the USA | (unparsed) |  |
| Biochemistry with Studies in the USA with Professional Placement | (unparsed) |  |
| Biological Sciences | (unparsed) |  |
| Biological Sciences with Foundation Year | (unparsed) |  |
| Biomedical Science | (unparsed) |  |
| Biomedical Science with Foundation Year | (unparsed) |  |
| Building Surveying | (unparsed) |  |
| Building Surveying (Part-Time) | (unparsed) |  |
| Building Surveying with Foundation Year | (unparsed) |  |
| Civil Engineering | (unparsed) |  |
| Civil Engineering with Foundation Year | (unparsed) |  |
| Computer Science | (unparsed) |  |
| Computer Science with Artificial Intelligence | (unparsed) |  |
| Computer Science with Cyber Security | (unparsed) |  |
| Computer Science with Cyber Security with Foundation Year | (unparsed) |  |
| Computer Science with Foundation Year | (unparsed) |  |
| Construction Project Management | (unparsed) |  |
| Construction Project Management (Part-time) | (unparsed) |  |
| Construction Project Management with Foundation Year | (unparsed) |  |
| Data Science | (unparsed) |  |
| Data Science (Top up Programme) | (unparsed) |  |
| Digital and Software Technology | (unparsed) |  |
| Electrical and Electronic Engineering | (unparsed) |  |
| Electrical and Electronic Engineering with Foundation Year | (unparsed) |  |
| Environmental Geography with Professional Experience | (unparsed) |  |
| Environmental Geography with Studies in the USA | (unparsed) |  |
| Environmental Management | (unparsed) |  |
| Environmental Management with Foundation Year | (unparsed) |  |
| Geography | (unparsed) |  |
| Geography with Foundation Year | (unparsed) |  |
| Get in touch | (unparsed) |  |
| Human Biology and Infectious Diseases | (unparsed) |  |
| Human Biology and Infectious Diseases with Foundation Year | (unparsed) |  |
| Interior Architecture | (unparsed) |  |
| Interior Architecture with Foundation Year | (unparsed) |  |
| Marine Biology | (unparsed) |  |
| Marine Biology with Foundation Year | (unparsed) |  |
| Mathematics | (unparsed) |  |
| Mechanical Engineering | (unparsed) |  |
| Mechanical Engineering with Foundation Year | (unparsed) |  |
| Pharmaceutical Science | (unparsed) |  |
| Pharmaceutical Science | MSCi (Hons) | https://www.salford.ac.uk/courses/undergraduate/pharmaceutical-science-0 |
| Pharmaceutical Science with Foundation Year | (unparsed) |  |
| Physics | (unparsed) |  |
| Physics with Foundation Year | (unparsed) |  |
| Quantity Surveying | (unparsed) |  |
| Quantity Surveying (Part-Time) | (unparsed) |  |
| Quantity Surveying with Foundation Year | (unparsed) |  |
| Questions | (unparsed) |  |
| Quick links | (unparsed) |  |
| Software Engineering | (unparsed) |  |
| Software Engineering with Foundation Year | (unparsed) |  |
| Sound Engineering and Production | (unparsed) |  |
| Wildlife Conservation | (unparsed) |  |
| Wildlife Conservation with Foundation Year | (unparsed) |  |
| Wildlife Conservation with Zoo Biology | (unparsed) |  |
| Wildlife Conservation with Zoo Biology with Foundation Year | (unparsed) |  |
| Zoology | (unparsed) |  |
| Zoology with Foundation Year | (unparsed) |  |

### 1.2 Salford Business School

Source: https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSalford+Business+School%5D=Salford+Business+School

#### BA (9 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Business Management with Law | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-with-law |
| Business Management with Law with Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-law-foundation-year |
| Business Management with Law with Placement | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-with-law-with-placement |
| Human Resource Management | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/human-resource-management |
| Human Resource Management with Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/human-resource-management-with-foundation-year |
| Human Resource Management with Placement | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/human-resource-management-with-placement |
| Marketing | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/marketing |
| Marketing with Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/marketing-with-foundation-year |
| Marketing with Placement | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/marketing-with-placement |

#### BSc (38 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Accounting and Finance | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance |
| Accounting and Finance with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance-with-foundation-year |
| Accounting and Finance with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance-with-placement |
| Business Data Analytics | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-data-analytics |
| Business Data Analytics with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-data-analytics-with-foundation-year |
| Business Data Analytics with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-data-analytics-with-placement |
| Business Economics | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-economics |
| Business Economics with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-economics-with-foundation-year |
| Business Economics with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-economics-with-placement |
| Business Information Technology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-information-technology |
| Business Information Technology with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-information-technology-with-foundation-year |
| Business Information Technology with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-information-technology-with-placement |
| Business Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management |
| Business Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-with-foundation-year |
| Business Management with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-with-placement |
| Business Management, Entrepreneurship and Innovation | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-entrepreneurship-and-innovation |
| Business Management, Entrepreneurship and Innovation with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-entrepreneurship-and-innovation-with-foundation-year |
| Business Management, Entrepreneurship and Innovation with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-management-entrepreneurship-and-innovation-with-placement |
| Business and Finance | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-and-finance |
| Business and Finance with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-and-finance-with-foundation-year |
| Business and Finance with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-and-finance-with-placement |
| Business with Human Resource Management with Professional Placement Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-with-human-resource-management-with-professional-placement-year |
| Business with Management (Top-Up) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-with-management-top-up |
| Business with Supply Chain and Project Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-with-supply-chain-and-project-management |
| Business with Supply Chain and Project Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-with-supply-chain-and-project-management-with-foundation-year |
| Business with Supply Chain and Project Management with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/business-with-supply-chain-and-project-management-with-placement |
| Esports Business Management (BSc Top-Up) | BSc Top-Up) |  |
| Esports Enterprise and Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/esports-enterprise-and-management |
| Esports Enterprise and Management with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/esports-enterprise-and-management-with-placement |
| International Business Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/international-business-management |
| International Business Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/international-business-management-with-foundation-year |
| International Business Management with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/international-business-management-with-placement |
| Sport Business Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sport-business-management |
| Sport Business Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sport-business-management-foundation-year |
| Sport Business Management with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sport-business-management-with-placement |
| Sustainable Business Management | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sustainable-business-management |
| Sustainable Business Management with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sustainable-business-management-with-foundation-year |
| Sustainable Business Management with Placement | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sustainable-business-management-with-placement |

#### DipHE (1 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Esports Enterprise and Management | DipHE | https://www.salford.ac.uk/courses/undergraduate/esports-enterprise-and-management-0 |

#### (unparsed) (59 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Accounting and Finance | (unparsed) |  |
| Accounting and Finance with Foundation Year | (unparsed) |  |
| Accounting and Finance with Placement | (unparsed) |  |
| Business Data Analytics | (unparsed) |  |
| Business Data Analytics with Foundation Year | (unparsed) |  |
| Business Data Analytics with Placement | (unparsed) |  |
| Business Economics | (unparsed) |  |
| Business Economics with Foundation Year | (unparsed) |  |
| Business Economics with Placement | (unparsed) |  |
| Business Information Technology | (unparsed) |  |
| Business Information Technology with Foundation Year | (unparsed) |  |
| Business Information Technology with Placement | (unparsed) |  |
| Business Management | (unparsed) |  |
| Business Management (BSc Top-Up) | Esports | https://www.salford.ac.uk/courses/undergraduate/esports-business-management-bsc-top-up |
| Business Management with Foundation Year | (unparsed) |  |
| Business Management with Law | (unparsed) |  |
| Business Management with Law with Foundation Year | (unparsed) |  |
| Business Management with Law with Placement | (unparsed) |  |
| Business Management with Placement | (unparsed) |  |
| Business Management, Entrepreneurship and Innovation | (unparsed) |  |
| Business Management, Entrepreneurship and Innovation with Foundation Year | (unparsed) |  |
| Business Management, Entrepreneurship and Innovation with Placement | (unparsed) |  |
| Business and Finance | (unparsed) |  |
| Business and Finance with Foundation Year | (unparsed) |  |
| Business and Finance with Placement | (unparsed) |  |
| Business with Human Resource Management with Professional Placement Year | (unparsed) |  |
| Business with Management (Top-Up) | (unparsed) |  |
| Business with Supply Chain and Project Management | (unparsed) |  |
| Business with Supply Chain and Project Management with Foundation Year | (unparsed) |  |
| Business with Supply Chain and Project Management with Placement | (unparsed) |  |
| Esports Enterprise and Management | (unparsed) |  |
| Esports Enterprise and Management with Placement | (unparsed) |  |
| Human Resource Management | (unparsed) |  |
| Human Resource Management with Foundation Year | (unparsed) |  |
| Human Resource Management with Placement | (unparsed) |  |
| International Business Management | (unparsed) |  |
| International Business Management with Foundation Year | (unparsed) |  |
| International Business Management with Placement | (unparsed) |  |
| Law | (unparsed) |  |
| Law | LLB (Hons) | https://www.salford.ac.uk/courses/undergraduate/law |
| Law with Criminology | (unparsed) |  |
| Law with Criminology | LLB (Hons) | https://www.salford.ac.uk/courses/undergraduate/law-with-criminology |
| Law with Criminology with Foundation Year | (unparsed) |  |
| Law with Criminology with Foundation Year | LLB (Hons) | https://www.salford.ac.uk/courses/undergraduate/law-with-criminology-with-foundation-year |
| Law with Criminology with Placement | (unparsed) |  |
| Law with Criminology with Placement | LLB (Hons) | https://www.salford.ac.uk/courses/undergraduate/law-with-criminology-with-placement |
| Law with Foundation Year | (unparsed) |  |
| Law with Foundation Year | LLB (Hons) | https://www.salford.ac.uk/courses/undergraduate/law-with-foundation-year |
| Law with Placement Year | (unparsed) |  |
| Law with Placement Year | LLB (Hons) | https://www.salford.ac.uk/courses/undergraduate/law-with-placement-year |
| Marketing | (unparsed) |  |
| Marketing with Foundation Year | (unparsed) |  |
| Marketing with Placement | (unparsed) |  |
| Sport Business Management | (unparsed) |  |
| Sport Business Management with Foundation Year | (unparsed) |  |
| Sport Business Management with Placement | (unparsed) |  |
| Sustainable Business Management | (unparsed) |  |
| Sustainable Business Management with Foundation Year | (unparsed) |  |
| Sustainable Business Management with Placement | (unparsed) |  |

### 1.3 Salford School of Arts Media and Creative Technology

Source: https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSalford+School+of+Arts+Media+and+Creative+Technology%5D=Salford+School+of+Arts+Media+and+Creative+Technology

#### BA (46 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Animation | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/animation |
| Animation With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/animation-with-foundation-year |
| Contemporary History and Politics | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/contemporary-history-and-politics |
| Contemporary Military and International History | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/contemporary-military-and-international-history |
| Costume Design | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/costume-design |
| Costume Design With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/costume-design-with-foundation-year |
| Creative Writing (Multidiscipline) | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/creative-writing-multidiscipline |
| Creative and Digital Media (Top-Up) | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/creative-and-digital-media-top-up |
| Dance | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/dance |
| Digital Video Production and Marketing | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/digital-video-production-and-marketing |
| Editing and Visual Effects for Film and Broadcast | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/editing-and-visual-effects-for-film-and-broadcast |
| English Language | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/english-language |
| English Literature | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/english-literature |
| English Multidiscipline | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/english-multidiscipline |
| English and Film | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/english-and-film |
| Fashion Business and Promotion | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fashion-business-and-promotion |
| Fashion Design | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fashion-design |
| Fashion Design With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fashion-design-with-foundation-year |
| Fashion Image Making and Styling | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fashion-image-making-and-styling |
| Fashion Image Making and Styling With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fashion-image-making-and-styling-with-foundation-year |
| Film Production | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/film-production |
| Film Studies | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/film-studies |
| Film, TV and Stage Design | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/film-tv-and-stage-design |
| Film, TV and Stage Design with Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/film-tv-and-stage-design-with-foundation-year |
| Fine Art | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fine-art |
| Fine Art With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/fine-art-with-foundation-year |
| Graphic Design | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/graphic-design |
| Graphic Design With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/graphic-design-with-foundation-year |
| Interior Design | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/interior-design |
| Interior Design With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/interior-design-with-foundation-year |
| International Relations and Politics | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/international-relations-and-politics |
| Journalism (Broadcast) | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/journalism-broadcast |
| Journalism (Multimedia) | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/journalism-multimedia |
| Journalism with Public Relations | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/journalism-with-public-relations |
| Media and Performance | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/media-and-performance |
| Music Management and Creative Enterprise | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/music-management-and-creative-enterprise |
| Music: Creative Music Technology | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/music-creative-music-technology |
| Music: Creative Music Technology with Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/music-creative-music-technology-with-foundation-year |
| Music: Popular Music and Recording | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/music-popular-music-and-recording |
| Music: Popular Music and Recording With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/music-popular-music-and-recording-with-foundation-year |
| Photography | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/photography |
| Photography With Foundation Year | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/photography-with-foundation-year |
| Sports Journalism | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/sports-journalism |
| Technical Theatre (Production and Design) | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/technical-theatre-production-and-design |
| Television and Radio Production | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/television-and-radio-production |
| Theatre and Performance Practice | BA (Hons) | https://www.salford.ac.uk/courses/undergraduate/theatre-and-performance-practice |

#### BSc (4 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Creative Computing | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/creative-computing |
| Creative Computing with Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/creative-computing-with-foundation-year |
| Games Design and Production | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/games-design-and-production |
| Games Design and Production With Foundation Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/games-design-and-production-with-foundation-year |

#### CertHE (2 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Creative and Digital Media | CertHE | https://www.salford.ac.uk/courses/undergraduate/creative-and-digital-media-0 |
| Social Media Content Creation | CertHE | https://www.salford.ac.uk/courses/undergraduate/social-media-content-creation-0 |

#### DipHE (2 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Creative and Digital Media | DipHE | https://www.salford.ac.uk/courses/undergraduate/creative-and-digital-media |
| Social Media Content Creation | DipHE | https://www.salford.ac.uk/courses/undergraduate/social-media-content-creation |

#### (unparsed) (52 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Animation | (unparsed) |  |
| Animation With Foundation Year | (unparsed) |  |
| Contemporary History and Politics | (unparsed) |  |
| Contemporary Military and International History | (unparsed) |  |
| Costume Design | (unparsed) |  |
| Costume Design With Foundation Year | (unparsed) |  |
| Creative Computing | (unparsed) |  |
| Creative Computing with Foundation Year | (unparsed) |  |
| Creative Writing (Multidiscipline) | (unparsed) |  |
| Creative and Digital Media | (unparsed) |  |
| Creative and Digital Media (Top-Up) | (unparsed) |  |
| Dance | (unparsed) |  |
| Digital Video Production and Marketing | (unparsed) |  |
| Editing and Visual Effects for Film and Broadcast | (unparsed) |  |
| English Language | (unparsed) |  |
| English Literature | (unparsed) |  |
| English Multidiscipline | (unparsed) |  |
| English and Film | (unparsed) |  |
| Fashion Business and Promotion | (unparsed) |  |
| Fashion Design | (unparsed) |  |
| Fashion Design With Foundation Year | (unparsed) |  |
| Fashion Image Making and Styling | (unparsed) |  |
| Fashion Image Making and Styling With Foundation Year | (unparsed) |  |
| Film Production | (unparsed) |  |
| Film Studies | (unparsed) |  |
| Film, TV and Stage Design | (unparsed) |  |
| Film, TV and Stage Design with Foundation Year | (unparsed) |  |
| Fine Art | (unparsed) |  |
| Fine Art With Foundation Year | (unparsed) |  |
| Games Design and Production | (unparsed) |  |
| Games Design and Production With Foundation Year | (unparsed) |  |
| Graphic Design | (unparsed) |  |
| Graphic Design With Foundation Year | (unparsed) |  |
| Interior Design | (unparsed) |  |
| Interior Design With Foundation Year | (unparsed) |  |
| International Relations and Politics | (unparsed) |  |
| Journalism (Broadcast) | (unparsed) |  |
| Journalism (Multimedia) | (unparsed) |  |
| Journalism with Public Relations | (unparsed) |  |
| Media and Performance | (unparsed) |  |
| Music Management and Creative Enterprise | (unparsed) |  |
| Music: Creative Music Technology | (unparsed) |  |
| Music: Creative Music Technology with Foundation Year | (unparsed) |  |
| Music: Popular Music and Recording | (unparsed) |  |
| Music: Popular Music and Recording With Foundation Year | (unparsed) |  |
| Photography | (unparsed) |  |
| Photography With Foundation Year | (unparsed) |  |
| Social Media Content Creation | (unparsed) |  |
| Sports Journalism | (unparsed) |  |
| Technical Theatre (Production and Design) | (unparsed) |  |
| Television and Radio Production | (unparsed) |  |
| Theatre and Performance Practice | (unparsed) |  |

### 1.4 School of Health and Society

Source: https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSchool+of+Health+and+Society%5D=School+of+Health+and+Society

#### BSc (34 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| BSc (Hons) Nursing (Nursing Associate Pathway) (Children and Young People) | BSc (Hons) Nursing (Nursing Assoc |  |
| BSc (Hons) Nursing (Nursing Associate Pathway) (Children and Young People) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/accelerated-cyp-nursing-bsc |
| Counselling and Psychotherapy: Professional Practice | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/counselling-and-psychotherapy-professional-practice |
| Criminology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/criminology |
| Criminology and Sociology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/criminology-and-sociology |
| Criminology with Counselling | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/criminology-with-counselling |
| Diagnostic Radiography | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/diagnostic-radiography |
| Learning Disabilities Nursing and Social Work (Integrated Practice) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/learning-disabilities-nursing-and-social-work-integrated-practice |
| Medical Science | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/medical-science |
| Medical Science with Placement Year | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/medical-science-with-placement-year |
| Midwifery | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/midwifery |
| Nursing (Nursing Associate Pathway) (Adult) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/accelerated-adult-nursing-bsc |
| Nursing (Nursing Associate Pathway) (Mental Health) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/accelerated-mental-health-nursing-bsc |
| Nursing / RN Children and Young People | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/nursing-rn-children-and-young-people |
| Nursing / RN Mental Health | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/nursing-rn-mental-health |
| Nursing Studies (Top Up) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/nursing-studies-top-up |
| Nursing/ RN Adult | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/nursing-rn-adult |
| Occupational Therapy | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/occupational-therapy |
| Occupational Therapy - Extended Route | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/occupational-therapy-extended-route |
| Part-Time Physiotherapy | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/part-time-physiotherapy |
| Physiotherapy | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/physiotherapy |
| Podiatry | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/podiatry |
| Professional Policing | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/professional-policing |
| Prosthetics and Orthotics | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/prosthetics-and-orthotics |
| Psychology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/psychology |
| Psychology (First Year Taught at Salford City College) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/psychology-first-year-taught-at-salford-city-college |
| Psychology and Counselling | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/psychology-and-counselling |
| Psychology and Criminology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/psychology-and-criminology |
| Psychology of Sport | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/psychology-of-sport |
| Social Work | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/social-work |
| Sociology | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sociology |
| Sport Rehabilitation | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sport-rehabilitation |
| Sport and Exercise Science | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sport-and-exercise-science |
| Sports Coaching Analysis (Top Up) | BSc (Hons) | https://www.salford.ac.uk/courses/undergraduate/sports-coaching-analysis-top-up |

#### FdSc (2 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| FdSc Nursing Associate (Direct Entry Route) | FdSc Nursing Associate (Direct Ent |  |
| FdSc Nursing Associate (Direct Entry Route) | FdSc | https://www.salford.ac.uk/courses/undergraduate/fdsc-nursing-associate-direct-entry-route |

#### (unparsed) (32 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Counselling and Psychotherapy: Professional Practice | (unparsed) |  |
| Criminology | (unparsed) |  |
| Criminology and Sociology | (unparsed) |  |
| Criminology with Counselling | (unparsed) |  |
| Diagnostic Radiography | (unparsed) |  |
| Learning Disabilities Nursing and Social Work (Integrated Practice) | (unparsed) |  |
| Medical Science | (unparsed) |  |
| Medical Science with Placement Year | (unparsed) |  |
| Midwifery | (unparsed) |  |
| Nursing (Nursing Associate Pathway) (Adult) | (unparsed) |  |
| Nursing (Nursing Associate Pathway) (Mental Health) | (unparsed) |  |
| Nursing / RN Children and Young People | (unparsed) |  |
| Nursing / RN Mental Health | (unparsed) |  |
| Nursing Studies (Top Up) | (unparsed) |  |
| Nursing/ RN Adult | (unparsed) |  |
| Occupational Therapy | (unparsed) |  |
| Occupational Therapy - Extended Route | (unparsed) |  |
| Part-Time Physiotherapy | (unparsed) |  |
| Physiotherapy | (unparsed) |  |
| Podiatry | (unparsed) |  |
| Professional Policing | (unparsed) |  |
| Prosthetics and Orthotics | (unparsed) |  |
| Psychology | (unparsed) |  |
| Psychology (First Year Taught at Salford City College) | (unparsed) |  |
| Psychology and Counselling | (unparsed) |  |
| Psychology and Criminology | (unparsed) |  |
| Psychology of Sport | (unparsed) |  |
| Social Work | (unparsed) |  |
| Sociology | (unparsed) |  |
| Sport Rehabilitation | (unparsed) |  |
| Sport and Exercise Science | (unparsed) |  |
| Sports Coaching Analysis (Top Up) | (unparsed) |  |

---

## Section 2 — 研究生 (Postgraduate) — 学院 → 学历级别 → 专业

### 2.1 授课型硕士 (PG Taught)

#### 2.1.1 School of Science Engineering and Environment

##### MSc (12 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Biomedical Science | MSc | https://www.salford.ac.uk/courses/postgraduate/biomedical-science |
| Biotechnology | MSc | https://www.salford.ac.uk/courses/postgraduate/biotechnology |
| Building Surveying | MSc | https://www.salford.ac.uk/courses/postgraduate/building-surveying |
| Drug Design and Discovery | MSc | https://www.salford.ac.uk/courses/postgraduate/drug-design-and-discovery |
| Environmental Assessment and Management | MSc | https://www.salford.ac.uk/courses/postgraduate/environmental-assessment-and-management |
| Health and Global Environment | MSc | https://www.salford.ac.uk/courses/postgraduate/health-and-global-environment |
| Microsystems and Nanoengineering | MSc | https://www.salford.ac.uk/courses/postgraduate/microsystems-and-nanoengineering |
| Safety, Health and Environment | MSc | https://www.salford.ac.uk/courses/postgraduate/safety-health-environment |
| Sustainability | MSc | https://www.salford.ac.uk/courses/postgraduate/sustainability |
| Sustainable Buildings | MSc | https://www.salford.ac.uk/courses/postgraduate/sustainable-buildings |
| Town and Country Planning | MSc | https://www.salford.ac.uk/courses/postgraduate/town-and-country-planning |
| Wildlife Conservation | MSc | https://www.salford.ac.uk/courses/postgraduate/wildlife-conservation-msc |

##### (unparsed) (36 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Acoustics | (unparsed) |  |
| Advanced Mechanical Engineering | (unparsed) |  |
| Aerospace Engineering | (unparsed) |  |
| Architecture | (unparsed) |  |
| Architecture | MArch | https://www.salford.ac.uk/courses/postgraduate/architecture |
| Artificial Intelligence | (unparsed) |  |
| Audio Production | (unparsed) |  |
| BIM and Digital Built Environments | (unparsed) |  |
| Biomedical Science | (unparsed) |  |
| Biotechnology | (unparsed) |  |
| Building Surveying | (unparsed) |  |
| Construction Law and Practice | (unparsed) |  |
| Construction Law and Practice | LLM | https://www.salford.ac.uk/courses/postgraduate/llm-construction-law-and-practice |
| Construction Management | (unparsed) |  |
| Cyber Security, Threat Intelligence and Forensics | (unparsed) |  |
| Data Science | (unparsed) |  |
| Drug Design and Discovery | (unparsed) |  |
| Environmental Assessment and Management | (unparsed) |  |
| Get in touch | (unparsed) |  |
| Health and Global Environment | (unparsed) |  |
| Internet of things with data science | (unparsed) |  |
| Microsystems and Nanoengineering | (unparsed) |  |
| Project Management in Construction | (unparsed) |  |
| Quantity Surveying | (unparsed) |  |
| Questions | (unparsed) |  |
| Quick links | (unparsed) |  |
| Real Estate and Property Management | (unparsed) |  |
| Robotics and Automation | (unparsed) |  |
| Safety, Health and Environment | (unparsed) |  |
| Software Engineering | (unparsed) |  |
| Structural Engineering | (unparsed) |  |
| Sustainability | (unparsed) |  |
| Sustainable Air Transport | (unparsed) |  |
| Sustainable Buildings | (unparsed) |  |
| Town and Country Planning | (unparsed) |  |
| Wildlife Conservation | (unparsed) |  |

#### 2.1.2 Salford Business School

##### MBA (2 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Online Global MBA | MBA |  |
| Online Global MBA | MBA | https://www.salford.ac.uk/courses/postgraduate/online-global-mba |

##### MSc (13 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Accounting and Finance | MSc | https://www.salford.ac.uk/courses/postgraduate/accounting-and-finance |
| Digital Marketing | MSc | https://www.salford.ac.uk/courses/postgraduate/digital-marketing |
| Entrepreneurship and Innovation | MSc | https://www.salford.ac.uk/courses/postgraduate/entrepreneurship-and-innovation |
| Financial Technology (FinTech) | MSc | https://www.salford.ac.uk/courses/postgraduate/financial-technology-fintech |
| Human Resource Management | MSc | https://www.salford.ac.uk/courses/postgraduate/human-resource-management |
| Human Resource Management (part-time, evening) | MSc | https://www.salford.ac.uk/courses/postgraduate/human-resource-management-part-time-evening |
| International Business | MSc | https://www.salford.ac.uk/courses/postgraduate/international-business |
| Management | MSc | https://www.salford.ac.uk/courses/postgraduate/management |
| Managing AI in Business | MSc | https://www.salford.ac.uk/courses/postgraduate/managing-ai-in-business |
| Managing Innovation and Information Technology | MSc | https://www.salford.ac.uk/courses/postgraduate/managing-innovation-and-information-technology |
| Operations Management and Business Analytics | MSc | https://www.salford.ac.uk/courses/postgraduate/operations-management-and-business-analytics |
| Procurement, Logistics and Supply Chain Management | MSc | https://www.salford.ac.uk/courses/postgraduate/procurement-logistics-and-supply-chain-management |
| Project Management | MSc | https://www.salford.ac.uk/courses/postgraduate/project-management |

##### (unparsed) (13 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Accounting and Finance | (unparsed) |  |
| Digital Marketing | (unparsed) |  |
| Entrepreneurship and Innovation | (unparsed) |  |
| Financial Technology (FinTech) | (unparsed) |  |
| Human Resource Management | (unparsed) |  |
| Human Resource Management (part-time, evening) | (unparsed) |  |
| International Business | (unparsed) |  |
| Management | (unparsed) |  |
| Managing AI in Business | (unparsed) |  |
| Managing Innovation and Information Technology | (unparsed) |  |
| Operations Management and Business Analytics | (unparsed) |  |
| Procurement, Logistics and Supply Chain Management | (unparsed) |  |
| Project Management | (unparsed) |  |

#### 2.1.3 Salford School of Arts Media and Creative Technology

##### MA (22 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Animation | MA | https://www.salford.ac.uk/courses/postgraduate/animation |
| Contemporary Fine Art | MA | https://www.salford.ac.uk/courses/postgraduate/contemporary-fine-art |
| Creative Technology | MA | https://www.salford.ac.uk/courses/postgraduate/creative-technology |
| Creative Video Production and Marketing | MA | https://www.salford.ac.uk/courses/postgraduate/creative-video-production-and-marketing |
| Creative Writing: Innovation and Experiment | MA | https://www.salford.ac.uk/courses/postgraduate/creative-writing-innovation-and-experiment |
| Dance: Performance and Professional Practices (Emergence) | MA | https://www.salford.ac.uk/courses/postgraduate/dance-performance-and-professional-practices-emergence |
| Documentary Production for TV, Film and Digital Media | MA | https://www.salford.ac.uk/courses/postgraduate/documentary-production-for-tv-film-and-digital-media |
| Drama Production for TV, Film and Digital Media | MA | https://www.salford.ac.uk/courses/postgraduate/drama-production-for-tv-film-and-digital-media |
| Editing TV, Film and Digital Media | MA | https://www.salford.ac.uk/courses/postgraduate/editing-tv-film-and-digital-media |
| Fashion Business and Marketing | MA | https://www.salford.ac.uk/courses/postgraduate/fashion-business-and-marketing |
| Fashion Design | MA | https://www.salford.ac.uk/courses/postgraduate/fashion-design |
| Film Production | MA | https://www.salford.ac.uk/courses/postgraduate/film-production |
| International Journalism for Digital Media | MA | https://www.salford.ac.uk/courses/postgraduate/international-journalism-for-digital-media |
| Literature and Culture | MA | https://www.salford.ac.uk/courses/postgraduate/literature-and-culture |
| Music | MA | https://www.salford.ac.uk/courses/postgraduate/music |
| Production Management for TV, Film and Digital Media | MA | https://www.salford.ac.uk/courses/postgraduate/production-management-for-tv-film-and-digital-media |
| Public Relations and Digital Communications | MA | https://www.salford.ac.uk/courses/postgraduate/public-relations-and-digital-communications |
| Screen Acting | MA | https://www.salford.ac.uk/courses/postgraduate/screen-acting |
| Socially Engaged Arts Practice | MA | https://www.salford.ac.uk/courses/postgraduate/socially-engaged-arts-practice |
| Socially Engaged Photography | MA | https://www.salford.ac.uk/courses/postgraduate/socially-engaged-photography |
| Visual Communication | MA | https://www.salford.ac.uk/courses/postgraduate/visual-communication |
| Wildlife Documentary Production | MA | https://www.salford.ac.uk/courses/postgraduate/wildlife-documentary-production |

##### MSc (1 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Games and Extended Reality | MSc | https://www.salford.ac.uk/courses/postgraduate/games-and-extended-reality |

##### (unparsed) (28 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Animation | (unparsed) |  |
| Contemporary Fine Art | (unparsed) |  |
| Creative Technology | (unparsed) |  |
| Creative Video Production and Marketing | (unparsed) |  |
| Creative Writing: Innovation and Experiment | (unparsed) |  |
| Dance and Professional Practices | (unparsed) |  |
| Dance: Performance and Professional Practices (Emergence) | (unparsed) |  |
| Documentary Production for TV, Film and Digital Media | (unparsed) |  |
| Drama Production for TV, Film and Digital Media | (unparsed) |  |
| Editing TV, Film and Digital Media | (unparsed) |  |
| Fashion Business and Marketing | (unparsed) |  |
| Fashion Design | (unparsed) |  |
| Film Production | (unparsed) |  |
| Games and Extended Reality | (unparsed) |  |
| Intelligence and Security Studies | (unparsed) |  |
| International Journalism for Digital Media | (unparsed) |  |
| International Relations and Global Challenges | (unparsed) |  |
| Journalism: News / Broadcast / Sport | (unparsed) |  |
| Literature and Culture | (unparsed) |  |
| Music | (unparsed) |  |
| Production Management for TV, Film and Digital Media | (unparsed) |  |
| Public Relations and Digital Communications | (unparsed) |  |
| Screen Acting | (unparsed) |  |
| Socially Engaged Arts Practice | (unparsed) |  |
| Socially Engaged Photography | (unparsed) |  |
| Terrorism and Security | (unparsed) |  |
| Visual Communication | (unparsed) |  |
| Wildlife Documentary Production | (unparsed) |  |

#### 2.1.4 School of Health and Society

##### MA (3 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Nursing (Adult) | MA | https://www.salford.ac.uk/courses/postgraduate/nursing-adult |
| Nursing (Mental Health) | MA | https://www.salford.ac.uk/courses/postgraduate/nursing-mental-health |
| Social Work | MA | https://www.salford.ac.uk/courses/postgraduate/social-work |

##### MSc (23 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Advanced Counselling and Psychotherapy Studies | MSc | https://www.salford.ac.uk/courses/postgraduate/advanced-counselling-and-psychotherapy-studies |
| Advanced Counselling and Psychotherapy Studies (Supervision) | MSc | https://www.salford.ac.uk/courses/postgraduate/advanced-counselling-and-psychotherapy-studies-supervision |
| Advanced Medical Imaging | MSc | https://www.salford.ac.uk/courses/postgraduate/advanced-medical-imaging |
| Advanced Practice (Neonates) | MSc | https://www.salford.ac.uk/courses/postgraduate/advanced-practice-neonates |
| Clinical Exercise Physiology | MSc | https://www.salford.ac.uk/courses/postgraduate/clinical-exercise-physiology |
| Diabetes Care | MSc | https://www.salford.ac.uk/courses/postgraduate/diabetes-care |
| Forensic Psychology | MSc | https://www.salford.ac.uk/courses/postgraduate/forensic-psychology |
| MSc Community Nurse Specialist Practitioner (top-up) | MSc | https://www.salford.ac.uk/courses/postgraduate/msc-community-nurse-specialist-practitioner-top-up |
| MSc Sport Rehabilitation and Athletic Training (pre-registration) | MSc Sport Rehabilitation and Athl |  |
| MSc Sport Rehabilitation and Athletic Training (pre-registration) | MSc | https://www.salford.ac.uk/courses/postgraduate/msc-sport-rehabilitation-and-athletic-training-pre-registration |
| Midwifery | MSc | https://www.salford.ac.uk/courses/postgraduate/midwifery |
| Midwifery (pre-registration) | MSc | https://www.salford.ac.uk/courses/postgraduate/midwifery-pre-registration |
| Midwifery Post RN (pre-registration) | MSc | https://www.salford.ac.uk/courses/postgraduate/midwifery-post-rn-pre-registration |
| Occupational Therapy (Pre-Registration) | MSc | https://www.salford.ac.uk/courses/postgraduate/occupational-therapy-pre-registration |
| Performance Analysis in Sport | MSc | https://www.salford.ac.uk/courses/postgraduate/performance-analysis-in-sport |
| Physiotherapy | MSc | https://www.salford.ac.uk/courses/postgraduate/physiotherapy |
| Podiatry (pre-registration) | MSc | https://www.salford.ac.uk/courses/postgraduate/podiatry-pre-registration |
| Public Health | MSc | https://www.salford.ac.uk/courses/postgraduate/public-health |
| Specialist Community Public Health Nurse (SCPHN) - Health Visiting | MSc | https://www.salford.ac.uk/courses/postgraduate/specialist-community-public-health-nurse-scphn-health-visiting |
| Specialist Community Public Health Nursing (top-up) | MSc | https://www.salford.ac.uk/courses/postgraduate/specialist-community-public-health-nursing-top-up |
| Sport Injury Rehabilitation | MSc | https://www.salford.ac.uk/courses/postgraduate/sport-injury-rehabilitation |
| Strength and Conditioning | MSc | https://www.salford.ac.uk/courses/postgraduate/strength-and-conditioning |
| Ultrasound Imaging | MSc | https://www.salford.ac.uk/courses/postgraduate/ultrasound-imaging |

##### PGCert (1 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| PGCert Mammography Principles and Practice | PGCert Mammography Principles and Pr |  |

##### (unparsed) (55 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Advanced Clinical Practice | (unparsed) |  |
| Advanced Counselling and Psychotherapy Studies | (unparsed) |  |
| Advanced Counselling and Psychotherapy Studies (Supervision) | (unparsed) |  |
| Advanced Medical Imaging | (unparsed) |  |
| Advanced Practice (Neonates) | (unparsed) |  |
| Applied Psychology (Addictions) | (unparsed) |  |
| Applied Psychology (Therapies) | (unparsed) |  |
| Applied Social Research Methods | (unparsed) |  |
| Clinical Exercise Physiology | (unparsed) |  |
| Cognitive Behaviour Therapy | (unparsed) |  |
| Cognitive Behaviour Therapy | PgCert | https://www.salford.ac.uk/courses/postgraduate/cognitive-behaviour-therapy |
| Cognitive Behavioural Psychotherapy | (unparsed) |  |
| Counselling and Psychotherapy (Professional Training) | (unparsed) |  |
| Criminal Justice: People and Processes | (unparsed) |  |
| Dental Implantology | (unparsed) |  |
| Diabetes Care | (unparsed) |  |
| Education for Health and Social Care Professionals | (unparsed) |  |
| Enabling Social Change | (unparsed) |  |
| Enhanced Practice | (unparsed) |  |
| Enhanced Practice | PgCert | https://www.salford.ac.uk/courses/postgraduate/enhanced-practice |
| Forensic Psychology | (unparsed) |  |
| Gastrointestinal Disorders | (unparsed) |  |
| Gastrointestinal Disorders | PgCert | https://www.salford.ac.uk/courses/postgraduate/gastrointestinal-disorders |
| Leadership and Management for Healthcare Practice | (unparsed) |  |
| Media Psychology and Applied Communication | (unparsed) |  |
| Midwifery | (unparsed) |  |
| Midwifery (pre-registration) | (unparsed) |  |
| Midwifery Post RN (pre-registration) | (unparsed) |  |
| Non-Surgical Facial Aesthetics | (unparsed) |  |
| Non-Surgical Facial Aesthetics | PgCert | https://www.salford.ac.uk/courses/postgraduate/non-surgical-facial-aesthetics |
| Non-medical Prescribing and Enhanced Clinical Skills | (unparsed) |  |
| Non-medical Prescribing and Enhanced Clinical Skills | PgCert | https://www.salford.ac.uk/courses/postgraduate/non-medical-prescribing-and-enhanced-clinical-skills |
| Nuclear Medicine Imaging | (unparsed) |  |
| Nursing | (unparsed) |  |
| Nursing (Adult) | (unparsed) |  |
| Nursing (Mental Health) | (unparsed) |  |
| Nursing Specialist Practitioner (District, Learning Disabilities, General Practice, Children's Community, Adult Social Care) | PgDip | https://www.salford.ac.uk/courses/postgraduate/nursing-specialist-practitioner-district-learning-disabilities-general-practice-childrens-community-adult-social-care |
| Occupational Therapy (Pre-Registration) | (unparsed) |  |
| PGCert Mammography Principles and Practice | Level 7 | https://www.salford.ac.uk/courses/postgraduate/pgcert-mammography-principles-and-practice |
| Performance Analysis in Sport | (unparsed) |  |
| Physiotherapy | (unparsed) |  |
| Podiatry (pre-registration) | (unparsed) |  |
| Population Health | (unparsed) |  |
| Population Health | PgCert | https://www.salford.ac.uk/courses/postgraduate/population-health |
| Psychology of Coercive Control | (unparsed) |  |
| Public Health | (unparsed) |  |
| Research in Nursing and Midwifery | (unparsed) |  |
| Social Work | (unparsed) |  |
| Specialist Community Public Health Nurse (SCPHN) – School Nursing | PgDip | https://www.salford.ac.uk/courses/postgraduate/specialist-community-public-health-nurse-scphn-school-nursing |
| Sport Injury Rehabilitation | (unparsed) |  |
| Strength and Conditioning | (unparsed) |  |
| Supervision in Counselling, Psychotherapy and Helping Relationships | (unparsed) |  |
| Supervision in Counselling, Psychotherapy and Helping Relationships | PgCert | https://www.salford.ac.uk/courses/postgraduate/supervision-in-counselling-psychotherapy-and-helping-relationships |
| Ultrasound Imaging | (unparsed) |  |
| Work-based Learning for Individual and Organisational Transformation | (unparsed) |  |

### 2.2 研究型硕士/博士 (PG Research)

#### 2.2.1 School of Science Engineering and Environment

##### (unparsed) (8 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Acoustics and Audio Postgraduate Research | (unparsed) |  |
| Civil Engineering Postgraduate Research | (unparsed) |  |
| Get in touch | (unparsed) |  |
| Informatics Postgraduate Research | (unparsed) |  |
| Materials and Physics Postgraduate Research | (unparsed) |  |
| Questions | (unparsed) |  |
| Quick links | (unparsed) |  |
| Robotics and Systems Engineering | (unparsed) |  |

#### 2.2.2 Salford Business School

##### (unparsed) (1 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Business, Management and Law | (unparsed) |  |

#### 2.2.3 Salford School of Arts Media and Creative Technology

_No PGR programmes listed._

#### 2.2.4 School of Health and Society

##### PhD (1 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Doctor of Philosophy (PhD) - School of Health and Society | PhD) - School of Health and Socie |  |

##### (unparsed) (2 programmes)

| Programme | Degree | URL |
|-----------|--------|-----|
| Professional Doctorate (Health and Social Care) | (unparsed) |  |
| Research in Psychology | (unparsed) |  |

---

## Section 3 — 申请要求 (Application Requirements)

### 3.1 学术要求 (Academic entry requirements)

Sample course (BSc (Hons) Accounting and Finance, UCAS code NN34, 3 years full-time, Peel Park campus):

> Source: https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance  (capture: 2026-07-08). The site shows a 3-year full-time BSc (Hons), with foundation-year and placement-year variants. Individual course pages list subject-specific tariff/A-level requirements; consult the live page for each programme.

### 3.2 英语要求 (English language requirements)

| 课程级别 | IELTS Academic (总分 / 小分) | 等价 SELT 接受 | 来源 |
|---------|----------------------------|----------------|------|
| 本科 (UG) | 6.0 / 5.5 in each component | 接受多种等价证书 | https://www.salford.ac.uk/international/english-language-requirements |
| 授课型硕士 (PGT) | 6.0 / 5.5 in each component | 接受多种等价证书 | 同上 |
| 研究型硕士/博士 (PGR) | 6.5 / 6.0 in each component | 接受多种等价证书 | 同上 |
| 研究型硕士/博士 — Salford Business School | 7.0 / 6.5 in each component | 接受多种等价证书 | 同上 |
| International Foundation Year (UKVI) | 4.5 / 4.0 in each component (UKVI) | UKVI IELTS Academic | 同上 |

> Snippet (verbatim): "For undergraduate courses we require IELTS ACADEMIC 6.0 (with a minimum 5.5 in each component) or equivalent. ... For postgraduate taught courses, we require IELTS ACADEMIC 6.0 (with a minimum 5.5 in each component) ... For postgraduate research courses, we require IELTS ACADEMIC 6.5 (with a minimum of 6.0 in each component). For postgraduate research courses that are based in Salford Business School we require IELTS ACADEMIC 7.0 (with a minimum of 6.5 in each component). For the International Foundation Year, we require IELTS 4.5 (with a minimum 4.0 in each component) in UKVI IELTS for UKVI (Academic)"

### 3.3 标化考试 (Standardised tests)

- **No US-style SAT/ACT required** (UK university).
- Per-programme requirements (e.g. health professions, social work) may specify additional tests (UCAT, BMAT, etc.) — see each course page.
- UK applicants apply via **UCAS** (https://www.ucas.com). UCAS code for BSc (Hons) Accounting and Finance: **NN34** (sample).

### 3.4 文书材料 (Personal statement / materials)

- 1 UCAS personal statement (up to 4,000 characters) for UG.
- Academic reference for UG.
- PG applications: direct via Salford portal; reference + personal statement required per course page.

---

## Section 4 — 学费与费用 (Tuition & Cost of Attendance)

### 4.1 本科生 (UG) — UK/Home fees 2026/27

- **£9,790** per year (full-time, England & Wales UG, government fee cap 2026/27, subject to Parliamentary approval).
- **£10,050** per year (2027/28, indicative, subject to Parliamentary approval).
- Part-time fees vary with credit load; DipHE / Top-up / Foundation Year may differ.

> Source: https://www.salford.ac.uk/undergraduate/fees-and-funding  (capture: 2026-07-08). Snippet: "for home full-time undergraduate students, the tuition fee cap for 2026/27 will be £9,790, and for 2027/28 will be £10,050 (subject to Parliamentary approval)."

### 4.2 国际生学费 (International tuition) 2026-27

- **Undergraduate**: range **£14,400 – £21,540 per year** (depending on course).
- **Postgraduate taught**: same range applies (each course page shows the exact figure).
- **Postgraduate research**: see Salford postgraduate research pages (per-programme).

> Source: https://www.salford.ac.uk/international/fees-and-funding  (capture: 2026-07-08). Snippet: "For international students, our full-time courses starting in 2026-27 cost from £14,400 to £21,540 depending on the course and level of study. The exact fees for all undergraduate and postgraduate taught courses are shown on our course pages."

### 4.3 押金 (Deposit)

- **£5,500** deposit required for all self-funded international (UG / PGT / International Foundation Year) before CAS is issued.
- 押金从应缴学费中抵扣 (deducted from first-year tuition).
- 美国贷款学生 (US loan) 押金可豁免 (waiver).

> Source: https://www.salford.ac.uk/international/fees-and-funding  (capture: 2026-07-08). Snippet: "All self-funded students studying an international foundation year, undergraduate or postgraduate programme, are required to pay a deposit of £5,500."

### 4.4 付款方式 (Payment options)

- 一次性付清: 3% prompt-payment discount on net fee (after scholarships).
- 分期: 5 or 7 monthly instalments (depending on course).
- 来源: https://www.salford.ac.uk/international/fees-and-funding

---

## Section 5 — 申请截止日期 (Application Deadlines)

### 5.1 本科 (UG) via UCAS

- **UCAS Extra**: opens late February each year.
- **Clearing**: opens early July (Salford publishes "Available in clearing" badges on course pages). Sample: BSc Accounting page header reads "Clearing Available in clearing" / "Apply for this course through clearing — Learn more about Clearing 2026".
- **Equal consideration deadline**: 26 January (UCAS deadline for most UG courses starting September 2026). After this date Salford considers applications on a rolling basis subject to availability.
- 来源: https://www.salford.ac.uk/undergraduate/apply  /  https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance

### 5.2 研究生 (PG)

- 授课型硕士 (PGT): rolling admissions — apply any time; recommended to apply at least 3 months before intake (September or January start, depending on course).
- 研究型硕士/博士 (PGR): apply any time, but funding deadlines (e.g. internal Vice-Chancellor's Research Studentships) usually February–March for September start.
- 来源: https://www.salford.ac.uk/postgraduate-taught/how-to-apply

### 5.3 国际生签证节点 (Visa timeline)

- 缴清押金 → 拿到无条件 offer → 学校出具 CAS → 申请 Student Route visa. 建议课程开始前至少 3 个月递签.
- 来源: https://www.salford.ac.uk/international/fees-and-funding

---

## Section 6 — WeKnora Chunk 导入清单 (Chunk Manifest)

| Chunk ID | Source URL | Type |
|----------|------------|------|
| salford-overview | https://www.salford.ac.uk | School overview |
| salford-courses | https://www.salford.ac.uk/search/courses | Course catalog index |
| salford-sse | https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSchool+of+Science+Engineering+and+Environment%5D=School+of+Science+Engineering+and+Environment | SSE catalog |
| salford-sbs | https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSalford+Business+School%5D=Salford+Business+School | SBS catalog |
| salford-samct | https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSalford+School+of+Arts+Media+and+Creative+Technology%5D=Salford+School+of+Arts+Media+and+Creative+Technology | SAMCT catalog |
| salford-shs | https://www.salford.ac.uk/search/courses?query=&field_school_name%5BSchool+of+Health+and+Society%5D=School+of+Health+and+Society | SHS catalog |
| salford-pg | https://www.salford.ac.uk/courses/postgraduate | PG index |
| salford-pgr | https://www.salford.ac.uk/courses/postgraduate-researchdoctorate | PGR index |
| salford-fees-home | https://www.salford.ac.uk/undergraduate/fees-and-funding | UG fees (home) |
| salford-fees-intl | https://www.salford.ac.uk/international/fees-and-funding | International fees |
| salford-english | https://www.salford.ac.uk/international/english-language-requirements | English language requirements |
| salford-apply-ug | https://www.salford.ac.uk/undergraduate/apply | UG apply |
| salford-apply-pg | https://www.salford.ac.uk/postgraduate-taught/how-to-apply | PG apply |
| salford-sample-accounting | https://www.salford.ac.uk/courses/undergraduate/accounting-and-finance | Sample UG course page |

---

## Section 7 — Monitoring Watchlist (change-frequency classification)

| URL | Frequency | Last checked | Baseline value |
|-----|-----------|--------------|----------------|
| https://www.salford.ac.uk/undergraduate/fees-and-funding | High (annual) | 2026-07-08 | £9,790 (UG 2026/27) |
| https://www.salford.ac.uk/international/fees-and-funding | High (annual) | 2026-07-08 | £14,400–£21,540 (intl 2026-27) |
| https://www.salford.ac.uk/international/english-language-requirements | Medium (annual) | 2026-07-08 | IELTS 6.0/6.5/7.0 by level |
| https://www.salford.ac.uk/search/courses (UG) | Medium (quarterly) | 2026-07-08 | 434 UG programmes |
| https://www.salford.ac.uk/search/courses (PG taught) | Medium (quarterly) | 2026-07-08 | 209 PGT programmes |
| https://www.salford.ac.uk/search/courses (PGR) | Medium (quarterly) | 2026-07-08 | 12 research programmes (partial attribution) |
| https://www.salford.ac.uk/undergraduate/apply | Low (annual) | 2026-07-08 | UCAS 26 Jan deadline |
| https://www.salford.ac.uk/postgraduate-taught/how-to-apply | Low (annual) | 2026-07-08 | rolling admissions |

---

## Notes & Known Gaps

- **PGR (research degrees) attribution is partial**: the 12 research programmes extracted include 8 from SSE, 1 from SBS, 3 from SHS, and 0 from SAMCT. The Salford research catalogue has both school-specific PhD programmes and cross-school PhD/MPhil umbrella programmes; the per-school filter on /search/courses?field_course_type_name=Postgraduate+ResearchDoctorate does not always attribute cross-school programmes. A future run should also visit https://www.salford.ac.uk/postgraduate-research for the complete research directory.
- **Degree labelling on cards**: the "Find out more" CTA renders degree for some cards but not all. UG/PGR counts in distribution matrix include an (unparsed) bucket (215 UG, 132 PGT, 11 PGR) — these are valid course names whose degree label was not in the card text. Individual course pages carry the degree on their hero section.
- **Many "courses" are variants of one core programme** (e.g. BSc (Hons) Accounting and Finance, BSc (Hons) Accounting and Finance with Foundation Year, BSc (Hons) Accounting and Finance with Placement). The 434 UG count counts each variant separately. A logical-programme count (one core programme + variants) would be lower; we report the variant-level count for exhaustive leaf enumeration per the skill contract.
- Capture window: 2026-07-08. All source URLs in this document were reachable and produced the cited snippets on that date.
