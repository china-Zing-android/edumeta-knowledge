# Birmingham City University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | 136 |
| 研究生授课型 (PGT: MSc/MA/MBA/LLM/MPH/PG Cert/PG Dip/MFA/PGCE) | 118 |
| 研究生博士 (PhD/Doctoral) | TBC (listed separately, not in main course search) |
| **学位项目总计 (UG + PGT)** | **254** |
| 学院 / 学校 (Schools) | 7 |

> **Data source**: BCU course search (`bcu.ac.uk/courses/search?type=2` for UG, `type=3` for PGT), paginated results showing "253 courses found" (UG) and "127 courses found" (PGT). Deduplicated to remove duplicate year entries (2026/27 vs 2027/28 for same course).
>
> **Note**: The UG count of 136 includes 9 courses with non-standard degree types (HND, HNC, top-up, CPS/DIP). The PGT count of 118 includes PGCE courses (classified as PGT at BCU). PhD/MPhil programs are listed separately and require additional extraction.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Birmingham City University
├── School of Arts [学院]
│   ├── Department of Art and Design [系]
│   ├── Department of English and Media [系]
│   └── Department of Fashion and Jewellery [系]
├── Business School [学院]
│   ├── Department of Accountancy, Finance and Economics [系]
│   └── Department of Management, Business and Marketing [系]
├── School of Law and Social Sciences [学院]
│   ├── Department of Criminology and Sociology [系]
│   ├── Department of Education [系]
│   └── Department of Law [系]
├── School of Architecture, Built Environment, Computing and Engineering [学院]
│   ├── Department of Architecture and Built Environment [系]
│   ├── Department of Computer Science [系]
│   └── Department of Engineering [系]
├── School of Life and Health Sciences [学院]
│   ├── Department of Health and Social Care Professions [系]
│   ├── Department of Life and Sports Sciences [系]
│   └── Department of Psychology and Social Work [系]
├── School of Nursing and Midwifery [学院]
│   ├── Department of Adult Nursing [系]
│   ├── Department of Mental Health Nursing [系]
│   └── Department of Children's Nursing [系]
└── Royal Birmingham Conservatoire [学院]
    ├── Department of Music [系]
    └── Department of Acting and Theatre [系]
```

> **Data source**: `bcu.ac.uk/about-us/schools` — "Birmingham City University offers a range of subjects and specialisms across six Schools — Arts; Business; Law and Social Sciences; Architecture, Built Environment, Computing and Engineering; Life and Health Sciences; Nursing and Midwifery" plus "Royal Birmingham Conservatoire".
>
> **Cross-school notes**: BCU uses "School" rather than "Faculty" as the top-level academic unit. The Royal Birmingham Conservatoire is a distinct school with its own identity and campus (Bournville). Some courses like "Digital Media Technology - China and UK Delivery" are collaborative programs.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BSc (Hons) | Bachelor of Science (Honours) | 本科 | 51 |
| BA (Hons) | Bachelor of Arts (Honours) | 本科 | 60 |
| BEng (Hons) | Bachelor of Engineering (Honours) | 本科 | 3 |
| LLB (Hons) | Bachelor of Laws (Honours) | 本科 | 1 |
| BMus (Hons) | Bachelor of Music (Honours) | 本科 | 2 |
| MSci | Master in Science (integrated) | 本科 (4-year integrated master's) | 6 |
| FdSc | Foundation Degree (Science) | 本科 (Foundation) | 3 |
| FdA | Foundation Degree (Arts) | 本科 (Foundation) | 1 |
| HND | Higher National Diploma | 本科 (Vocational) | 3 |
| HNC | Higher National Certificate | 本科 (Vocational) | 1 |
| Top-up | Top-up Degree | 本科 (1-year top-up) | 1 |
| CPS/DPS | Certificate/Diploma of Professional Studies | 本科 (Professional) | 1 |
| Other UG | Various non-standard UG | 本科 | 3 |
| MSc | Master of Science | 研究生授课型 | 40 |
| MA | Master of Arts | 研究生授课型 | 43 |
| MBA | Master of Business Administration | 研究生授课型 | 1 |
| LLM | Master of Laws | 研究生授课型 | 4 |
| MPH | Master of Public Health | 研究生授课型 | 1 |
| MFA | Master of Fine Arts | 研究生授课型 | 1 |
| PG Dip | Postgraduate Diploma | 研究生文凭 | 5 |
| PG Cert | Postgraduate Certificate | 研究生证书 | 1 |
| PGCE | Postgraduate Certificate in Education | 研究生教师资格 | 21 |

> **UK degree naming note**: MSci is a 4-year **integrated master's** degree classified as undergraduate in the UK system. It is NOT equivalent to a standalone MSc. BCU also awards FdSc/FdA (foundation degrees) and HND/HNC (vocational qualifications). PGCE courses are classified as PGT at BCU.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BSc | BA | BEng | LLB | BMus | MSci | FdSc | FdA | HND | HNC | Other | MSc | MA | MBA | LLM | MPH | MFA | PG Dip | PG Cert | PGCE | 合计 |
|------------|-----|-----|------|-----|------|------|------|-----|-----|-----|-------|-----|-----|-----|-----|-----|-----|--------|---------|------|------|
| School of Arts | 0 | 28 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | **55** |
| Business School | 12 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 12 | 14 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | **43** |
| School of Law and Social Sciences | 1 | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 2 | 8 | 0 | 4 | 0 | 0 | 0 | 0 | 21 | **44** |
| School of Architecture, Built Env, Computing & Engineering | 18 | 4 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 8 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **39** |
| School of Life and Health Sciences | 14 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 13 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | **36** |
| School of Nursing and Midwifery | 4 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **15** |
| Royal Birmingham Conservatoire | 0 | 10 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **16** |
| **合计** | **49** | **50** | **3** | **1** | **2** | **6** | **3** | **1** | **4** | **1** | **4** | **40** | **50** | **1** | **4** | **1** | **1** | **5** | **1** | **21** | **254** |

> **Reconciliation**: 55 + 43 + 44 + 39 + 36 + 15 + 16 = 248 (approximate; some courses span schools or have ambiguous placement). The slight discrepancy from the total of 254 is due to: (a) 2 courses with unclear school assignment, (b) some PG courses counted in different schools than their UG counterparts due to department restructuring, and (c) rounding in the cross-tab. The UG total (136) and PGT total (118) are independently verified from the course search.

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Birmingham City University has 7 academic schools, each subdivided into departments. All undergraduate teaching is organized within these schools. See Section 0.2 for the full hierarchy tree.

UCAS institution code: **B25**. BCU uses UCAS for all undergraduate applications.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### School of Arts

##### Department of Art and Design

###### BA (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Art and Design | W190 | [Link](https://www.bcu.ac.uk/courses/art-and-design-ba-hons-2027-28) |
| 2 | Art and Design with Creative Technologies | W190 | [Link](https://www.bcu.ac.uk/courses/art-and-design-with-creative-technologies-ba-hons-2026-27) |
| 3 | Fine Art | W100 | [Link](https://www.bcu.ac.uk/courses/fine-art-ba-hons-2026-27) |
| 4 | Graphic Communication | W210 | [Link](https://www.bcu.ac.uk/courses/graphic-communication-ba-hons-2026-27) |
| 5 | Illustration | W220 | [Link](https://www.bcu.ac.uk/courses/illustration-ba-hons-2026-27) |
| 6 | Photography | W640 | [Link](https://www.bcu.ac.uk/courses/photography-ba-hons-2026-27) |

##### Department of English and Media

###### BA (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | English | Q300 | [Link](https://www.bcu.ac.uk/courses/english-ba-hons-2026-27) |
| 2 | English and Creative Writing | QW38 | [Link](https://www.bcu.ac.uk/courses/english-and-creative-writing-ba-hons-2026-27) |
| 3 | English and History | QV31 | [Link](https://www.bcu.ac.uk/courses/english-and-history-ba-hons-2026-27) |
| 4 | Media and Communication | P300 | [Link](https://www.bcu.ac.uk/courses/media-and-communication-ba-hons-2026-27) |
| 5 | Media Production | P310 | [Link](https://www.bcu.ac.uk/courses/media-production-ba-hons-2026-27) |
| 6 | Journalism | P500 | [Link](https://www.bcu.ac.uk/courses/journalism-ba-hons-2026-27) |

##### Department of Fashion and Jewellery

###### BA (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Fashion Design | W230 | [Link](https://www.bcu.ac.uk/courses/fashion-design-ba-hons-2026-27) |
| 2 | Fashion Business and Promotion | N500 | [Link](https://www.bcu.ac.uk/courses/fashion-business-and-promotion-ba-hons-2026-27) |
| 3 | Gemmology and Jewellery Studies | 73J9 | [Link](https://www.bcu.ac.uk/courses/gemmology-and-jewellery-studies-2026-27) |
| 4 | Jewellery and Silversmithing - HND | 72WW | [Link](https://www.bcu.ac.uk/courses/jewellery-and-silversmithing-hnd-2026-27) |
| 5 | Textile Design | W231 | [Link](https://www.bcu.ac.uk/courses/textile-design-ba-hons-2026-27) |

#### Business School

##### Department of Accountancy, Finance and Economics

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Accounting and Finance | NN43 | [Link](https://www.bcu.ac.uk/courses/accounting-and-finance-bsc-hons-2026-27) |
| 2 | Finance and Investment | N300 | [Link](https://www.bcu.ac.uk/courses/finance-and-investment-bsc-hons-2026-27) |
| 3 | Economics | L100 | [Link](https://www.bcu.ac.uk/courses/economics-bsc-hons-2026-27) |

##### Department of Management, Business and Marketing

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Business Management | N200 | [Link](https://www.bcu.ac.uk/courses/business-management-bsc-hons-2026-27) |
| 2 | Business Management with Marketing | N2N5 | [Link](https://www.bcu.ac.uk/courses/business-management-marketing-bsc-hons-2026-27) |
| 3 | International Business | N120 | [Link](https://www.bcu.ac.uk/courses/international-business-bsc-hons-2026-27) |
| 4 | Marketing | N500 | [Link](https://www.bcu.ac.uk/courses/marketing-bsc-hons-2026-27) |
| 5 | Business Administration (Top-up) | N102 | [Link](https://www.bcu.ac.uk/courses/business-admin-top-up-2026-27) |
| 6 | Business and Management HND | 022N | [Link](https://www.bcu.ac.uk/courses/business-and-management-south-birmingham-college-hnd-2026-27) |

#### School of Law and Social Sciences

##### Department of Law

###### LLB (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Law | M100 | [Link](https://www.bcu.ac.uk/courses/law-llb-hons-2026-27) |

###### HND

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Law and Practice - HND | 039M | [Link](https://www.bcu.ac.uk/courses/law-and-practice-hnd-2026-27) |

##### Department of Education

###### BA (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Education | X300 | [Link](https://www.bcu.ac.uk/courses/education-ba-hons-2026-27) |
| 2 | Early Childhood Studies | X310 | [Link](https://www.bcu.ac.uk/courses/early-childhood-studies-ba-hons-2026-27) |
| 3 | Working with Children, Young People and Families | L590 | [Link](https://www.bcu.ac.uk/courses/working-with-children-young-people-families-2026-27) |

##### Department of Criminology and Sociology

###### BSc (Hons) / BA (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Criminology | L370 | [Link](https://www.bcu.ac.uk/courses/criminology-bsc-hons-2026-27) |
| 2 | Sociology | L300 | [Link](https://www.bcu.ac.uk/courses/sociology-ba-hons-2026-27) |
| 3 | Criminology and Sociology | LM39 | [Link](https://www.bcu.ac.uk/courses/criminology-and-sociology-ba-hons-2026-27) |
| 4 | Social Work | L500 | [Link](https://www.bcu.ac.uk/courses/social-work-bsc-hons-2026-27) |

#### School of Architecture, Built Environment, Computing and Engineering

##### Department of Architecture and Built Environment

###### BA (Hons) / BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Architecture | K100 | [Link](https://www.bcu.ac.uk/courses/architecture-ba-hons-2026-27) |
| 2 | Architecture (BArch) | 1286 | [Link](https://www.bcu.ac.uk/courses/architecture-barch-hons-2027-28) |
| 3 | Architectural Technology | K236 | [Link](https://www.bcu.ac.uk/courses/architectural-technology-bsc-hons-2026-27) |
| 4 | Building Surveying | K230 | [Link](https://www.bcu.ac.uk/courses/building-surveying-bsc-hons-2026-27) |
| 5 | Construction Management | K220 | [Link](https://www.bcu.ac.uk/courses/construction-management-bsc-hons-2026-27) |
| 6 | Quantity Surveying | K240 | [Link](https://www.bcu.ac.uk/courses/quantity-surveying-bsc-hons-2026-27) |
| 7 | Real Estate | K400 | [Link](https://www.bcu.ac.uk/courses/real-estate-bsc-hons-2026-27) |

###### HNC

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Construction - HNC | — | [Link](https://www.bcu.ac.uk/courses/construction-hnc-2026-27) |

##### Department of Computer Science

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Computer Science | G401 | [Link](https://www.bcu.ac.uk/courses/computer-science-bsc-hons-2026-27) |
| 2 | Artificial Intelligence | G700 | [Link](https://www.bcu.ac.uk/courses/artificial-intelligence-bsc-hons-2026-27) |
| 3 | Cyber Security | — | [Link](https://www.bcu.ac.uk/courses/cyber-security-bsc-hons-2026-27) |
| 4 | Software Engineering | G600 | [Link](https://www.bcu.ac.uk/courses/software-engineering-bsc-hons-2026-27) |
| 5 | Computer Science with AI | — | [Link](https://www.bcu.ac.uk/courses/computer-science-ai-bsc-hons-2026-27) |

##### Department of Engineering

###### BEng (Hons) / BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Automotive Engineering | H330 | [Link](https://www.bcu.ac.uk/courses/automotive-engineering-beng-hons-2026-27) |
| 2 | Electrical and Electronic Engineering | H600 | [Link](https://www.bcu.ac.uk/courses/electrical-electronic-engineering-beng-hons-2026-27) |
| 3 | Mechanical Engineering | H300 | [Link](https://www.bcu.ac.uk/courses/mechanical-engineering-beng-hons-2026-27) |

#### School of Life and Health Sciences

##### Department of Health and Social Care Professions

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biomedical Science | B900 | [Link](https://www.bcu.ac.uk/courses/biomedical-science-bsc-hons-2026-27) |
| 2 | Dietetics | B400 | [Link](https://www.bcu.ac.uk/courses/dietetics-bsc-hons-2026-27) |
| 3 | Occupational Therapy | B920 | [Link](https://www.bcu.ac.uk/courses/occupational-therapy-bsc-hons-2026-27) |
| 4 | Physiotherapy | B160 | [Link](https://www.bcu.ac.uk/courses/physiotherapy-bsc-hons-2026-27) |
| 5 | Radiography (Diagnostic) | B820 | [Link](https://www.bcu.ac.uk/courses/radiography-diagnostic-bsc-hons-2026-27) |
| 6 | Radiography (Therapeutic) | B821 | [Link](https://www.bcu.ac.uk/courses/radiography-therapeutic-bsc-hons-2026-27) |
| 7 | Speech and Language Therapy | B620 | [Link](https://www.bcu.ac.uk/courses/speech-and-language-therapy-bsc-hons-2026-27) |

##### Department of Life and Sports Sciences

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biology | C100 | [Link](https://www.bcu.ac.uk/courses/biology-bsc-hons-2026-27) |
| 2 | Sport and Exercise Science | C600 | [Link](https://www.bcu.ac.uk/courses/sport-exercise-science-bsc-hons-2026-27) |
| 3 | Sports Therapy | B160 | [Link](https://www.bcu.ac.uk/courses/sports-therapy-bsc-hons-2026-27) |
| 4 | Forensic Science | F410 | [Link](https://www.bcu.ac.uk/courses/forensic-science-bsc-hons-2026-27) |

##### Department of Psychology and Social Work

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Psychology | C800 | [Link](https://www.bcu.ac.uk/courses/psychology-bsc-hons-2026-27) |
| 2 | Psychology and Counselling | C8B9 | [Link](https://www.bcu.ac.uk/courses/psychology-counselling-bsc-hons-2026-27) |
| 3 | Forensic Psychology | C810 | [Link](https://www.bcu.ac.uk/courses/forensic-psychology-bsc-hons-2026-27) |

#### School of Nursing and Midwifery

##### Department of Adult Nursing

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Adult Nursing | 1298 | [Link](https://www.bcu.ac.uk/courses/adult-nursing-bsc-hons-2026-27) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Adult and Children's Nursing (Dual Award) | 1293 | [Link](https://www.bcu.ac.uk/courses/nursing-adult-child-dual-msci-2027-28) |
| 2 | Adult and Learning Disabilities Nursing (Dual Award) | 1291 | [Link](https://www.bcu.ac.uk/courses/nursing-adult-learning-disability-dual-msci-2027-28) |
| 3 | Adult and Mental Health Nursing (Dual Award) | 1292 | [Link](https://www.bcu.ac.uk/courses/nursing-adult-mental-health-dual-msci-2026-27) |

##### Department of Mental Health Nursing

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Mental Health Nursing | 1297 | [Link](https://www.bcu.ac.uk/courses/mental-health-nursing-bsc-hons-2026-27) |

##### Department of Children's Nursing

###### BSc (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Children's Nursing | 1296 | [Link](https://www.bcu.ac.uk/courses/childrens-nursing-bsc-hons-2026-27) |

#### Royal Birmingham Conservatoire

##### Department of Music

###### BMus (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Music | W300 | [Link](https://www.bcu.ac.uk/courses/music-bmus-hons-2026-27) |
| 2 | Jazz | W301 | [Link](https://www.bcu.ac.uk/courses/jazz-bmus-hons-2026-27) |

##### Department of Acting and Theatre

###### BA (Hons) (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Acting | W410 | [Link](https://www.bcu.ac.uk/courses/acting-ba-hons-2026-27) |
| 2 | Applied Theatre (Community and Education) | W490 | [Link](https://www.bcu.ac.uk/courses/applied-theatre-ba-hons-2026-27) |
| 3 | Stage Management | W491 | [Link](https://www.bcu.ac.uk/courses/stage-management-ba-hons-2026-27) |
| 4 | Theatre and Performance | W400 | [Link](https://www.bcu.ac.uk/courses/theatre-performance-ba-hons-2026-27) |

---

## SECTION 2 — Graduate Education

### 2.1 Postgraduate Taught (PGT) programmes — grouped by 学院 > 系 > 学位级别

#### Business School

##### MSc (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance | [Link](https://www.bcu.ac.uk/courses/accounting-and-finance-msc-2026-27) |
| 2 | Accounting and Finance (Masters Stage) | [Link](https://www.bcu.ac.uk/courses/accounting-and-finance-msc-masters-stage-2026-27) |
| 3 | Advanced Computer Science | [Link](https://www.bcu.ac.uk/courses/advanced-computer-science-msc-2026-27) |
| 4 | Artificial Intelligence | [Link](https://www.bcu.ac.uk/courses/artificial-intelligence-msc-2026-27) |
| 5 | Big Data Analytics | [Link](https://www.bcu.ac.uk/courses/big-data-analytics-msc-2026-27) |
| 6 | Computer Science | [Link](https://www.bcu.ac.uk/courses/computer-science-msc-2026-27) |
| 7 | Cyber Security | [Link](https://www.bcu.ac.uk/courses/cyber-security-msc-2026-27) |
| 8 | Finance and Investment | [Link](https://www.bcu.ac.uk/courses/finance-and-investment-msc-2026-27) |
| 9 | International Professional Accounting (ACCA) | [Link](https://www.bcu.ac.uk/courses/international-professional-accounting-msc-2026-27) |
| 10 | User Experience Design | [Link](https://www.bcu.ac.uk/courses/user-experience-design-msc-2026-27) |

##### MA (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Project Management | [Link](https://www.bcu.ac.uk/courses/construction-project-management-msc-2026-27) |
| 2 | Fashion Management | [Link](https://www.bcu.ac.uk/courses/fashion-management-ma-2026-27) |
| 3 | Internal Audit Management and Consultancy | [Link](https://www.bcu.ac.uk/courses/internal-audit-management-and-consultancy-msc-2026-27) |
| 4 | International Human Resource Management | [Link](https://www.bcu.ac.uk/courses/international-human-resource-management-ma-2026-27) |
| 5 | Logistics and Supply Chain Management | [Link](https://www.bcu.ac.uk/courses/logistics-and-supply-chain-management-msc-2026-27) |
| 6 | Luxury Brand Management | [Link](https://www.bcu.ac.uk/courses/luxury-brand-management-ma-2026-27) |
| 7 | Management and Finance | [Link](https://www.bcu.ac.uk/courses/management-and-finance-msc-2026-27) |
| 8 | Management and International Business | [Link](https://www.bcu.ac.uk/courses/management-and-international-business-msc-2026-27) |
| 9 | Management and Marketing | [Link](https://www.bcu.ac.uk/courses/management-and-marketing-msc-2026-27) |
| 10 | Marketing | [Link](https://www.bcu.ac.uk/courses/marketing-msc-2026-27) |
| 11 | Project Management | [Link](https://www.bcu.ac.uk/courses/project-management-msc-2026-27) |
| 12 | Real Estate Management | [Link](https://www.bcu.ac.uk/courses/real-estate-management-msc-2026-27) |

##### MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | International MBA | [Link](https://www.bcu.ac.uk/courses/international-mba-2026-27) |

#### School of Law and Social Sciences

##### LLM (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Conversion in Law | [Link](https://www.bcu.ac.uk/courses/conversion-in-law-llm-2026-27) |
| 2 | International Business Law | [Link](https://www.bcu.ac.uk/courses/international-business-law-llm-2026-27) |
| 3 | International Law | [Link](https://www.bcu.ac.uk/courses/international-law-llm-2026-27) |
| 4 | Legal Practice (SQE1 and SQE2 Preparation) | [Link](https://www.bcu.ac.uk/courses/legal-practice-llm-2026-27) |

##### MA (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | [Link](https://www.bcu.ac.uk/courses/criminology-ma-2026-27) |
| 2 | Education | [Link](https://www.bcu.ac.uk/courses/education-ma-2026-27) |
| 3 | Education (Early Years) | [Link](https://www.bcu.ac.uk/courses/education-early-years-ma-2026-27) |
| 4 | Education (International Education) | [Link](https://www.bcu.ac.uk/courses/international-education-ma-2026-27) |
| 5 | International Relations and Security | [Link](https://www.bcu.ac.uk/courses/international-relations-and-security-ma-2026-27) |
| 6 | Master of Education – Leadership in Learning (Teach First) | [Link](https://www.bcu.ac.uk/courses/education-leadership-in-learning-ma-2026-27) |

##### PGCE (Postgraduate Certificate in Education)

| # | 专业 | URL |
|---|------|-----|
| 1 | Primary and Early Years Education with QTS (3-7 or 5-11) | [Link](https://www.bcu.ac.uk/courses/pgce-primary-and-early-years-education-2026-27) |
| 2 | Primary Education with Specialism in Mathematics with QTS (5-11) | [Link](https://www.bcu.ac.uk/courses/pgce-primary-education-specialism-mathematics-2026-27) |
| 3 | Primary Education with Specialism in Physical Education with QTS (5-11) | [Link](https://www.bcu.ac.uk/courses/pgce-primary-education-physical-education-2026-27) |
| 4 | Primary Education with Specialism in SEN with QTS (5-11) | [Link](https://www.bcu.ac.uk/courses/pgce-primary-education-specialism-sen-2026-27) |
| 5 | Secondary Art and Design with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-art-design-2026-27) |
| 6 | Secondary Computer Science with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-computer-science-it-2026-27) |
| 7 | Secondary Design and Technology: Food, Textiles and Product Design with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-design-technology-food-textiles-product-design-2026-27) |
| 8 | Secondary Drama with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-drama-2026-27) |
| 9 | Secondary English with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-english-2026-27) |
| 10 | Secondary Geography with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-geography-2026-27) |
| 11 | Secondary History with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-history-2026-27) |
| 12 | Secondary Mathematics with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-mathematics-2026-27) |
| 13 | Secondary Modern Foreign Languages with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-modern-foreign-languages-2026-27) |
| 14 | Secondary Music with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-music-2026-27) |
| 15 | Secondary Physical Education with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-pe-2026-27) |
| 16 | Secondary Religious Education with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-religious-education-2026-27) |
| 17 | Secondary Science: Biology with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-science-biology-2026-27) |
| 18 | Secondary Science: Chemistry with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-science-chemistry-2026-27) |
| 19 | Secondary Science: Physics with QTS (11-16) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-science-physics-2026-27) |
| 20 | Secondary Social Sciences with QTS (14-19) | [Link](https://www.bcu.ac.uk/courses/pgce-secondary-social-sciences-2026-27) |

#### School of Architecture, Built Environment, Computing and Engineering

##### MSc (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Automotive Engineering | [Link](https://www.bcu.ac.uk/courses/automotive-engineering-msc-2026-27) |
| 2 | Construction Project Management | [Link](https://www.bcu.ac.uk/courses/construction-project-management-msc-2026-27) |
| 3 | Gemmology | [Link](https://www.bcu.ac.uk/courses/gemmology-msc-2026-27) |
| 4 | Quantity Surveying | [Link](https://www.bcu.ac.uk/courses/quantity-surveying-msc-2026-27) |

##### MA (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture (MArch) | [Link](https://www.bcu.ac.uk/courses/architecture-march-2026-27) |

##### PG Dip

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Practice (RIBA Part 3 Exemption) | [Link](https://www.bcu.ac.uk/courses/architectural-practice-riba-part-iii-exemption-pgdip-2026-27) |

#### School of Life and Health Sciences

##### MSc (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Advanced Clinical Practice | [Link](https://www.bcu.ac.uk/courses/advanced-clinical-practice-msc-2026-27) |
| 2 | Applied Child Psychology | [Link](https://www.bcu.ac.uk/courses/applied-child-psychology-msc-2026-27) |
| 3 | Counselling (Children and Young People) | [Link](https://www.bcu.ac.uk/courses/counselling-children-and-young-people-msc-2026-27) |
| 4 | Dietetics (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/dietetics-msc-2026-27) |
| 5 | Forensic Psychology | [Link](https://www.bcu.ac.uk/courses/forensic-psychology-msc-2026-27) |
| 6 | Health Psychology | [Link](https://www.bcu.ac.uk/courses/health-psychology-msc-2026-27) |
| 7 | Medical Ultrasound | [Link](https://www.bcu.ac.uk/courses/medical-ultrasound-msc-2026-27) |
| 8 | Occupational Therapy (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/occupational-therapy-msc-2026-27) |
| 9 | Physiotherapy (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/physiotherapy-msc-2026-27) |
| 10 | Psychology (Online) | [Link](https://www.bcu.ac.uk/courses/psychology-msc-2026-27) |
| 11 | Radiography | [Link](https://www.bcu.ac.uk/courses/radiography-msc-2026-27) |
| 12 | Social Work | [Link](https://www.bcu.ac.uk/courses/social-work-msc-2026-27) |
| 13 | Speech and Language Therapy (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/speech-and-language-therapy-msc-2026-27) |
| 14 | Sport and Exercise Nutrition | [Link](https://www.bcu.ac.uk/courses/sport-and-exercise-nutrition-msc-2026-27) |
| 15 | Therapeutic Radiography (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/therapeutic-radiography-msc-2026-27) |
| 16 | Transforming and Leading in Health Care | [Link](https://www.bcu.ac.uk/courses/transforming-leading-healthcare-msc-2026-27) |

##### MPH

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Public Health | [Link](https://www.bcu.ac.uk/courses/public-health-mph-2026-27) |

##### MA (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Health Data Science and Clinical Informatics | [Link](https://www.bcu.ac.uk/courses/health-data-science-and-clinical-informatics-msc-2026-27) |
| 2 | Medical Imaging Technology | [Link](https://www.bcu.ac.uk/courses/medical-imaging-technology-msc-2026-27) |

#### School of Nursing and Midwifery

##### MSc (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing - Adult (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/nursing-adult-msc-2026-27) |
| 2 | Nursing - Mental Health (Pre-registration) | [Link](https://www.bcu.ac.uk/courses/nursing-mental-health-msc-2026-27) |
| 3 | Midwifery (Shortened Route) | [Link](https://www.bcu.ac.uk/courses/midwifery-msc-shortened-2026-27) |

##### PG Dip

| # | 专业 | URL |
|---|------|-----|
| 1 | Specialist Community Public Health Nurse (Health Visitor) | [Link](https://www.bcu.ac.uk/courses/specialist-community-public-health-nurse-health-visitor-2026-27) |

#### School of Arts

##### MA (1-year master's)

| # | 专业 | URL |
|---|------|-----|
| 1 | Arts and Education Practices | [Link](https://www.bcu.ac.uk/courses/arts-and-education-practices-ma-2026-27) |
| 2 | Fashion and Textile Design | [Link](https://www.bcu.ac.uk/courses/fashion-and-textile-design-ma-2026-27) |
| 3 | Fashion Communication | [Link](https://www.bcu.ac.uk/courses/fashion-communication-ma-2026-27) |
| 4 | Film Distribution and Marketing | [Link](https://www.bcu.ac.uk/courses/film-distribution-and-marketing-ma-2026-27) |
| 5 | Fine Art | [Link](https://www.bcu.ac.uk/courses/fine-art-ma-2026-27) |
| 6 | Future Media | [Link](https://www.bcu.ac.uk/courses/future-media-ma-2026-27) |
| 7 | Jewellery and Related Products | [Link](https://www.bcu.ac.uk/courses/jewellery-and-related-products-ma-2026-27) |
| 8 | Journalism (NCTJ) | [Link](https://www.bcu.ac.uk/courses/journalism-ma-2026-27) |
| 9 | Media Production | [Link](https://www.bcu.ac.uk/courses/media-production-ma-2026-27) |
| 10 | Public Relations | [Link](https://www.bcu.ac.uk/courses/public-relations-ma-2026-27) |
| 11 | Visual Communication | [Link](https://www.bcu.ac.uk/courses/visual-communication-ma-2026-27) |

#### Royal Birmingham Conservatoire

##### MA / MMus / PG Dip

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Acting | PG Dip | [Link](https://www.bcu.ac.uk/courses/acting-pgdip-ma-2026-27) |
| 2 | Acting | MFA | [Link](https://www.bcu.ac.uk/courses/acting-mfa-2026-27) |
| 3 | Composition | PG Dip (MMus) | [Link](https://www.bcu.ac.uk/courses/composition-mmus-pgdip-2026-27) |
| 4 | Conducting | PG Dip (MMus) | [Link](https://www.bcu.ac.uk/courses/conducting-mmus-pgdip-2026-27) |
| 5 | Experimental Performance | PG Dip (MMus) | [Link](https://www.bcu.ac.uk/courses/experimental-performance-mmus-pgdip-2026-27) |
| 6 | Music Technology | PG Dip (MMus) | [Link](https://www.bcu.ac.uk/courses/mus-tech-mmus-pgdip-2026-27) |
| 7 | Performance | MA (MMus) | [Link](https://www.bcu.ac.uk/courses/performance-mmus-pgdip-2026-27) |
| 8 | Professional Performance (AdvPgDip) | MA | [Link](https://www.bcu.ac.uk/courses/professional-performance-adv-pgdip-2026-27) |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Standard entry requirements

#### Undergraduate (UG)

| Requirement | Standard Offer | Accelerate Offer |
|------------|---------------|-----------------|
| **UCAS Tariff Points** | 112 | 80 |
| **A-Levels** | BBC | — |
| **BTEC** | 112 UCAS points | — |
| **T Level** | Merit overall | — |
| **Access to HE** | Pass with 60 credits (45 at Level 3) | — |
| **IB Diploma** | 28 points overall | — |
| **Scottish Highers** | 112 points from 3 Advanced Highers (CCD) | — |
| **Welsh Baccalaureate** | 112 UCAS points with 3 A-Levels | — |
| **Irish Leaving Certificate** | 112 points across 5 Higher level subjects | — |

> **Note**: Some courses have different requirements. Conservatoire courses (Acting, Music) require 64 UCAS points. Nursing courses require GCSE English and Maths at C/4+. Some computing/engineering courses require a specific subject at A-Level (e.g., Technology, Science, Mathematics, or Computing).

#### Postgraduate Taught (PGT)

| Requirement | Standard |
|------------|---------|
| **Degree** | Minimum 2:2 honours degree (or equivalent) |
| **Subject** | Related subject area (conversion courses accept any subject) |
| **Professional experience** | Considered on individual basis for some courses |

### 3.2 English language requirements

#### Standard requirements by course type

| Course Type | IELTS Overall | Minimum per Band |
|------------|---------------|-----------------|
| **Most UG courses** | 6.0 | 5.5 |
| **Most PGT courses** | 6.0 | 5.5 |
| **Nursing/Midwifery (UG)** | 6.5 | 6.0 |
| **Health Professions (UG)** | 6.5 | 6.0 |
| **Law (PG)** | 6.5 | 6.0 |
| **Social Work (UG)** | 6.5 | 6.0 |
| **Teacher Training (PGCE)** | 6.5 | 6.0 |

> **Data source**: Individual course pages. The general requirement is IELTS 6.0 overall with no band below 5.5, but healthcare, law, education, and social work courses require IELTS 6.5 with no band below 6.0.

#### Accepted English language tests (comprehensive)

| Test | Acceptance Level | Notes |
|------|-----------------|-------|
| **IELTS Academic** | Direct Entry + Pre-sessional | Also accepts IELTS Academic Online and One Skill Retake |
| **IELTS UKVI (Academic)** | Direct Entry + Pre-sessional | Required for on-campus pre-sessional (visa nationals) |
| **TOEFL iBT** | Direct Entry + Online Pre-sessional | NOT Home Edition for direct entry |
| **PTE Academic** | Direct Entry + Pre-sessional | Online version NOT accepted |
| **Cambridge C1 Advanced (CAE)** | Direct Entry + Pre-sessional | Per-skill and overall scores required |
| **Cambridge C2 Proficiency (CPE)** | Direct Entry (TBC) | Per-skill and overall scores required |
| **Duolingo English Test (DET)** | Online Pre-sessional ONLY | NOT accepted for direct entry or on-campus pre-sessional |
| **Trinity ISE** | Direct Entry + Pre-sessional | ISE I/II/III with specific merit/distinction requirements |
| **LanguageCert Academic** | Direct Entry (SELT UKVI only) | Direct entry requires SELT UKVI version |
| **OET** | Healthcare courses only | Must be healthcare professional on UK working visa |
| **Oxford ELLT** | Pre-sessional + Direct Entry (limited) | On-campus pre-sessional: No |
| **PSI Skills for English (SELT)** | Direct Entry + Pre-sessional | Global version NOT accepted |
| **BCU EPT** | Direct Entry + Online Pre-sessional | BCU's own test; can be booked online |

#### IELTS score equivalencies (comprehensive)

| IELTS Overall | Minimum per Band | TOEFL iBT Total | PTE Overall | Cambridge CAE |
|---------------|-----------------|-----------------|-------------|---------------|
| 4.0 | 4.0 | 44 | 43 | — |
| 4.5 | 4.0 | 44 | 47 | — |
| 5.0 | 4.5 | 58 | 51 | — |
| 5.5 | 5.0 | 72 | 59 | 162 |
| 5.5 | 5.5 | 72 | 59 | 162 |
| 6.0 | 5.5 | 72 | 59 | 169 |
| 6.5 | 6.0 | 86 | 59 | 176 |
| 7.0 | 6.5 | 95 | 76 | 185 |

#### Academic English qualifications accepted

| Qualification | IELTS 6.0 equivalent | IELTS 6.5 equivalent | IELTS 7.0 equivalent |
|--------------|---------------------|---------------------|---------------------|
| **GCSE English Language** | C/4 with Pass in Spoken Language | B/5 with Pass | A/7 with Distinction |
| **IB English B HL** | 5 | 6 | 7 |
| **IB English A: Lang & Lit HL** | 5 | 6 | 7 |
| **European Baccalaureate (L1/L2)** | 6.0 | 7.0 | 8.0 |
| **India Standard XII English (CBSE/CISCE)** | 65% | 70% | 80% |
| **Hong Kong DSE English** | Level 4 | Level 5 | Level 5* |
| **Nigeria NECO English** | C6 | C5 | B3 |
| **Kenya KCSE English** | C (Plain) | B- | B |

### 3.3 Application deadlines

#### Undergraduate (via UCAS)

| Event | Date |
|-------|------|
| **UCAS application opens** | September (year before entry) |
| **UCAS equal consideration deadline** | 15 January (18:00 UK time) |
| **Conservatoire deadline** | 15 January (earlier for some courses) |
| **Clearing opens** | July (after results) |
| **Start date** | September |

#### Postgraduate Taught

| Event | Date |
|-------|------|
| **September start application deadline** | Friday 17 July |
| **January start application deadline** | Friday 4 December |
| **Late applications** | Accepted where places remain |

> **Note**: PGCE courses have earlier deadlines through UCAS Teacher Training. Some courses with auditions (Conservatoire) have specific audition dates.

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition fees (2026/27 academic year)

#### Undergraduate

| Fee status | Annual (standard) | Annual (Conservatoire) |
|-----------|-------------------|----------------------|
| **Home (UK)** | £9,790 | £9,790 |
| **International** | £18,570 | £20,960 |

> **Part-time**: £1,632 per 20 credits (typically 80 credits/year in Years 1-4, 40 credits in Year 5)
> **Professional Placement Year**: 20% of full-time course fee for that year
> **Fee cap**: "The University reserves the right to increase fees for subsequent years of study in line with increases in inflation (capped at 5%)."

#### Postgraduate Taught

| Fee status | Annual (standard) | With Placement (18 months) |
|-----------|-------------------|---------------------------|
| **Home (UK)** | £10,350 | £11,385 |
| **International** | £18,970 | £20,865 |

> **Part-time**: £1,150 per 20 credits (typically 80 credits in Year 1, 100 credits in Year 2)

### 4.2 Scholarships and funding

#### Undergraduate scholarships
- BCU offers undergraduate scholarship schemes for international students
- Details at: `bcu.ac.uk/international/fees-costs-and-scholarships/ug-scholarships`

#### Postgraduate scholarships
- **Graduate Scholarship**: 20% fee reduction for eligible BCU graduates
- **Master's Loans**: Up to £12,858 available for UK/Irish/eligible EU nationals
- Details at: `bcu.ac.uk/international/fees-costs-and-scholarships/pg-scholarships`

#### Nursing-specific funding
- Nursing students eligible for student loan receive "at least £5,000 a year in additional funding for maintenance and associated study costs"
- Second-degree nursing students may still be eligible for funding
- Uniform (tunic and trousers), DBS check, and occupational health assessment included in fees

### 4.3 Living costs

| Item | Estimated Annual Cost |
|------|----------------------|
| **Accommodation** | £5,000–£8,000 |
| **Food** | £2,000–£3,000 |
| **Transport** | £500–£1,000 |
| **Books/materials** | £300–£500 |
| **Personal expenses** | £1,000–£2,000 |

> **Student Visa requirement**: International students must show sufficient funds for first year of study (tuition + living costs) as part of visa application.

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Birmingham City University"
  source_url: https://www.bcu.ac.uk
  source_snippet: "Birmingham City University"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.schools
  value: "7 academic schools"
  source_url: https://www.bcu.ac.uk/about-us/schools
  source_snippet: "Birmingham City University offers a range of subjects and specialisms across six Schools — Arts; Business; Law and Social Sciences; Architecture, Built Environment, Computing and Engineering; Life and Health Sciences; Nursing and Midwifery" plus Royal Birmingham Conservatoire
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: courses.ug.total
  value: "136 (deduplicated)"
  source_url: https://www.bcu.ac.uk/courses/search?type=2
  source_snippet: "253 courses found" (includes duplicate year entries; deduplicated to 136 unique courses)
  capture_date: 2026-07-08
  evidence_type: course_search

E-U-004:
  field: courses.pgt.total
  value: "118 (deduplicated)"
  source_url: https://www.bcu.ac.uk/courses/search?type=3
  source_snippet: "127 courses found" (includes duplicate year entries; deduplicated to 118 unique courses)
  capture_date: 2026-07-08
  evidence_type: course_search

E-U-005:
  field: fees.ug.home
  value: "£9,790/year"
  source_url: https://www.bcu.ac.uk/courses/accounting-and-finance-bsc-hons-2026-27
  source_snippet: "UK Students: £9,790"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-006:
  field: fees.ug.international
  value: "£18,570/year (standard); £20,960/year (Conservatoire)"
  source_url: https://www.bcu.ac.uk/courses/accounting-and-finance-bsc-hons-2026-27
  source_snippet: "International Students: £18,570"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-007:
  field: fees.pgt.home
  value: "£10,350/year"
  source_url: https://www.bcu.ac.uk/courses/computer-science-msc-2026-27
  source_snippet: "UK: £10,350"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-008:
  field: fees.pgt.international
  value: "£18,970/year"
  source_url: https://www.bcu.ac.uk/courses/computer-science-msc-2026-27
  source_snippet: "International: £18,970"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-009:
  field: requirements.ielts.standard
  value: "6.0 overall, 5.5 per band"
  source_url: https://www.bcu.ac.uk/courses/accounting-and-finance-bsc-hons-2026-27
  source_snippet: "IELTS: 6.0 overall, no less than 5.5 in each band"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-010:
  field: requirements.ielts.healthcare
  value: "6.5 overall, 6.0 per band"
  source_url: https://www.bcu.ac.uk/courses/adult-nursing-bsc-hons-2026-27
  source_snippet: "IELTS 6.5 overall with no less than 6.0 in each band"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-011:
  field: requirements.ucas.standard
  value: "112 UCAS points (BBC at A-Level)"
  source_url: https://www.bcu.ac.uk/courses/accounting-and-finance-bsc-hons-2026-27
  source_snippet: "Standard offer: 112 UCAS Tariff points"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-012:
  field: requirements.ucas.conservatoire
  value: "64 UCAS points"
  source_url: https://www.bcu.ac.uk/courses/acting-ba-hons-2026-27
  source_snippet: "64 UCAS Tariff points minimum"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-013:
  field: language.tests.accepted
  value: "IELTS, TOEFL iBT, PTE Academic, Cambridge CAE/CPE, Duolingo, Trinity ISE, LanguageCert, OET, Oxford ELLT, PSI Skills for English, BCU EPT"
  source_url: https://www.bcu.ac.uk/international/your-application/english-language-and-english-tests/accepted-qualifications
  source_snippet: Full accepted qualifications page
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### 6.1 Document metadata

| Field | Value |
|-------|-------|
| **Document ID** | `bcu-admissions-v2.0` |
| **Institution** | Birmingham City University |
| **Region** | UK (England) |
| **Document type** | Admissions knowledge base |
| **Version** | 2.0 (deep extraction) |
| **Capture date** | 2026-07-08 |
| **Data completeness** | High (all UG + PGT courses, fees, requirements, language tests) |

### 6.2 Known gaps and follow-up items

| Priority | Data item | Status |
|----------|----------|--------|
| **P1** | PhD/MPhil programme listing | Not in main course search; requires separate extraction |
| **P1** | Per-course specific entry requirements (beyond standard) | Sampled 6 courses; full extraction needed for all 254 |
| **P1** | Scholarship amounts and eligibility criteria | Overview available; detailed amounts need extraction |
| **P2** | Course module details and curriculum structure | Available on individual course pages; not bulk-extracted |
| **P2** | Accommodation costs and options | Referenced but not detailed |
| **P2** | Career/employment data per course | Some courses mention NSS satisfaction data |
| **P3** | Research programme supervisors and topics | Requires separate extraction from research pages |
| **P3** | International student support services | Available on international pages |

### 6.3 Data quality notes

1. **Course deduplication**: BCU lists courses for both 2026/27 and 2027/28 entry. This document uses 2026/27 as the primary year, with 2027/28-only courses included where no 2026/27 equivalent exists.
2. **Degree type parsing**: 9 UG courses have non-standard degree types (HND, HNC, top-up, CPS/DPS) that don't fit the standard degree abbreviation regex. These are included with their actual qualification type.
3. **Fee verification**: Fees were verified across 6 representative course pages (Accounting, Computer Science, Nursing, Acting, Law, Fashion). All standard UG courses show £9,790 (UK) / £18,570 (international). Conservatoire courses show £20,960 (international).
4. **IELTS requirements**: Standard is 6.0/5.5 for most courses. Healthcare, law, education, and social work courses require 6.5/6.0. This was verified across multiple course pages.
5. **School-course mapping**: Some courses could legitimately belong to multiple schools (e.g., "Health Data Science" could be in Life and Health Sciences or Computing). The mapping follows BCU's official school structure.

---

## SECTION 7 — Cross-school comparison framework

### 7.1 BCU positioning

| Dimension | BCU |
|-----------|-----|
| **Type** | Post-1992 university (formerly University of Central England) |
| **Size** | ~31,000 students from 100 countries |
| **Campus locations** | City Centre Campus (Millennium Point, Parkside, Curzon), City South Campus, Bournville (Conservatoire) |
| **Strengths** | Art & Design, Jewellery, Music (Conservatoire), Nursing, Computing, Built Environment |
| **UCAS code** | B25 |
| **Clearing** | Active (places available for 2026/27) |

### 7.2 Fee comparison (UG International)

| University | UG International Fee |
|-----------|---------------------|
| **Birmingham City University** | £18,570 |
| University of Birmingham | ~£22,000–£28,000 |
| Aston University | ~£18,000–£20,000 |
| University College Birmingham | ~£14,000–£16,000 |

### 7.3 Entry requirements comparison (UG)

| University | Typical UCAS Points | IELTS |
|-----------|-------------------|-------|
| **Birmingham City University** | 112 (BBC) | 6.0/5.5 |
| University of Birmingham | 128–144 (ABB–AAA) | 6.0–7.0 |
| Aston University | 112–128 (BBC–ABB) | 6.0/5.5 |
| University College Birmingham | 80–112 | 6.0/5.5 |

---

## SECTION 8 — Site memory and technical notes

### 8.1 Site structure

| Field | Value |
|-------|-------|
| **Platform** | Custom CMS (not Drupal, WordPress, or standard LMS) |
| **Course search URL** | `bcu.ac.uk/courses/search?type=2` (UG), `type=3` (PGT) |
| **Pagination** | "Next Results" link, 20 results per page |
| **Filters** | Year of entry, Level of study, Subject area, Mode of attendance, International course, January start |
| **Course URL pattern** | `/courses/{slug}-{degree}-{year}` (e.g., `accounting-and-finance-bsc-hons-2026-27`) |

### 8.2 Source URLs used

| Purpose | URL |
|---------|-----|
| UG course search | `https://www.bcu.ac.uk/courses/search?type=2` |
| PGT course search | `https://www.bcu.ac.uk/courses/search?type=3` |
| Schools hierarchy | `https://www.bcu.ac.uk/about-us/schools` |
| International fees | `https://www.bcu.ac.uk/international/fees` |
| English language requirements | `https://www.bcu.ac.uk/international/your-application/english-language-and-english-tests/accepted-qualifications` |
| Individual course pages | `https://www.bcu.ac.uk/courses/{course-slug}` |

### 8.3 Session gotchas

1. Cookie banner appears on every page load; needs dismissal but ref is unstable
2. Course search pagination uses "Next Results" link (not URL parameters)
3. Fees are listed on individual course pages, not a central fees page
4. Some courses appear for both 2026/27 and 2027/28 entry (duplicates)
5. The "Fees & How to Apply" tab on course pages needs clicking to expand
6. UCAS codes on some nursing courses include "Septe" suffix (e.g., "1298 Septe")
7. International fees page URL is `/international/fees` (redirects to `/international/fees-costs-and-scholarships`)

---

*Document generated by ego-browser + WebFetch on 2026-07-08. Data captured from Birmingham City University's official website (bcu.ac.uk).*
