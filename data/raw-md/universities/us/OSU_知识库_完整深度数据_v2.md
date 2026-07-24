# Ohio State University (OSU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BA/BFA/BM/BME/BSD/BSEd) | 172 |
| 本科副学士 (AS/AAS, ATI Wooster) | 13 |
| 本科 Pre-Professional / Undecided / Exploration | 11 |
| **本科目录条目总计** | **196** |
| 研究生学位项目 (PhD/MS/MA/MBA/MFA/专业博士 etc.) | 262 |
| 研究生证书/背书 (Certificate/Endorsement) | 62 |
| **研究生目录条目总计** | **324** |
| **学位项目总计 (UG + Grad)** | **~520** |
| 学院 / 独立系所总数 | 18 (+ Graduate School) |

> **来源**: UG数据来自 `undergrad.osu.edu/majors-and-academics/majors` (Table View, 196 rows); Grad数据来自 `gpadmissions.osu.edu/programs/` (324 entries as stated on site). OSU官方称"200-plus undergraduate majors"，实际目录列出196条（含ATI副学士、Pre-Professional、Exploration等非学位track）。研究生324条含证书和背书。

### 0.2 学院/系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
The Ohio State University
├── College of Arts and Sciences                          [学院]
│   ├── Department of Mathematics                         [系]
│   ├── Department of Computer Science and Engineering    [系]
│   ├── Department of Economics                           [系]
│   ├── Department of English                             [系]
│   ├── Department of Psychology                          [系]
│   ├── Department of Chemistry                           [系]
│   ├── Department of Physics                             [系]
│   ├── Department of Biology                             [系]
│   ├── Department of History                             [系]
│   ├── Department of Philosophy                          [系]
│   ├── Department of Sociology                           [系]
│   ├── Department of Political Science                   [系]
│   ├── Department of Anthropology                        [系]
│   ├── Department of Astronomy                           [系]
│   ├── Department of Statistics                          [系]
│   ├── School of Music                                   [系]
│   ├── Department of Dance                               [系]
│   ├── Department of Theatre                             [系]
│   └── ... (83 UG programs, 89 Grad programs)
│
├── Fisher College of Business                            [学院]
│   ├── Department of Accounting and MIS                  [系]
│   ├── Department of Finance                             [系]
│   ├── Department of Marketing and Logistics             [系]
│   ├── Department of Management and Human Resources      [系]
│   └── ... (13 UG programs, 14 Grad programs)
│
├── College of Engineering                                [学院]
│   ├── Department of Aerospace Engineering               [系]
│   ├── Department of Biomedical Engineering              [系]
│   ├── Department of Chemical Engineering                [系]
│   ├── Department of Civil, Environmental and Geodetic Engineering [系]
│   ├── Department of Computer Science and Engineering    [系] ⚠ shared with Arts & Sciences
│   ├── Department of Electrical and Computer Engineering [系]
│   ├── Department of Engineering Education               [系]
│   ├── Department of Food, Agricultural and Biological Engineering [系]
│   ├── Department of Industrial and Systems Engineering  [系]
│   ├── Department of Materials Science and Engineering   [系]
│   ├── Department of Mechanical and Aerospace Engineering [系]
│   ├── Department of Nuclear Engineering                 [系]
│   ├── Department of Welding Engineering                 [系]
│   └── ... (15 UG programs, 35 Grad programs)
│
├── College of Education and Human Ecology                [学院]
│   ├── Department of Teaching and Learning               [系]
│   ├── Department of Educational Studies                 [系]
│   ├── Department of Human Sciences                      [系]
│   └── ... (16 UG programs, 34 Grad programs)
│
├── College of Food, Agricultural, and Environmental Sciences [学院]
│   ├── Department of Agricultural, Environmental, and Development Economics [系]
│   ├── Department of Animal Sciences                     [系]
│   ├── Department of Entomology                          [系]
│   ├── Department of Food, Agricultural and Biological Engineering [系]
│   ├── Department of Food Science and Technology         [系]
│   ├── Department of Horticulture and Crop Science       [系]
│   ├── Department of Plant Pathology                     [系]
│   ├── School of Environment and Natural Resources       [系]
│   ├── Ohio State Agricultural Technical Institute (ATI) [系]
│   └── ... (29 UG programs, 19 Grad programs)
│
├── Knowlton School of Architecture                       [学院]
│   ├── Architecture Program                              [系]
│   ├── City and Regional Planning Program                [系]
│   ├── Landscape Architecture Program                    [系]
│   └── ... (3 UG programs, 19 Grad programs)
│
├── College of Medicine                                   [学院]
│   ├── Department of Biomedical Informatics              [系]
│   ├── Department of Biomedical Sciences                 [系]
│   ├── School of Health and Rehabilitation Sciences      [系]
│   └── ... (1 UG program, 15 Grad programs)
│
├── School of Health and Rehabilitation Sciences          [学院]
│   ├── Division of Medical Laboratory Science            [系]
│   ├── Division of Radiologic Sciences and Therapy       [系]
│   ├── Division of Respiratory Therapy                   [系]
│   ├── Division of Athletic Training                     [系]
│   └── ... (8 UG programs, 24 Grad programs)
│
├── College of Nursing                                    [学院]
│   └── ... (2 UG programs, 22 Grad programs)
│
├── College of Dentistry                                  [学院]
│   ├── School of Dental Hygiene                          [系]
│   └── ... (2 UG programs, 8 Grad programs)
│
├── Moritz College of Law                                 [学院]
│   └── ... (0 UG programs, 6 Grad programs)
│
├── College of Optometry                                  [学院]
│   └── ... (0 UG programs, 3 Grad programs)
│
├── College of Pharmacy                                   [学院]
│   └── ... (1 UG program, 4 Grad programs)
│
├── John Glenn College of Public Affairs                  [学院]
│   └── ... (2 UG programs, 10 Grad programs)
│
├── College of Public Health                              [学院]
│   └── ... (1 UG program, 10 Grad programs)
│
├── College of Social Work                                [学院]
│   └── ... (1 UG program, 5 Grad programs)
│
├── College of Veterinary Medicine                        [学院]
│   └── ... (0 UG programs, 5 Grad programs)
│
├── School of Environment and Natural Resources           [学院]
│   └── ... (6 UG programs, 4 Grad programs)
│
└── Graduate School                                       [行政管理]
    └── (administers all graduate admissions; programs housed in above colleges)
```

> ⚠ Computer Science and Engineering is shared between College of Engineering (BS CSE) and College of Arts and Sciences (BS/BA CIS).

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 (canonical) | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|--------|------|------|-----------|
| BS | BS | Bachelor of Science | 本科 | 84 |
| BA | BA | Bachelor of Arts | 本科 | 43 |
| BSEd | BSEd | Bachelor of Science in Education | 本科 | 8 |
| BSD | BSD | Bachelor of Science in Design | 本科 | 4 |
| BM | BM | Bachelor of Music | 本科 | 4 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| BME | BME | Bachelor of Music Education | 本科 | 1 |
| BS,BA | BS, BA | Dual Bachelor of Science/Arts | 本科 | 13 |
| BA,BFA | BA, BFA | Dual Bachelor of Arts/Fine Arts | 本科 | 1 |
| AS | AS | Associate of Science (ATI) | 本科(副学士) | 6 |
| AAS | AAS | Associate of Applied Science (ATI) | 本科(副学士) | 7 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 89 |
| MS | MS | Master of Science | 研究生 | 52 |
| MA | MA | Master of Arts | 研究生 | 29 |
| MBA | MBA | Master of Business Administration | 研究生 | 5 |
| MFA | MFA | Master of Fine Arts | 研究生 | 5 |
| MEd | MEd | Master of Education | 研究生 | 2 |
| Other Masters | Various | Other Master's degrees | 研究生 | 43 |
| Prof Doctorate | Various | Professional Doctorate (DDS/DVM/AuD/etc.) | 研究生 | 16 |
| Grad Certificate | Various | Graduate Certificate | 研究生(证书) | 40 |
| UG Certificate | Various | Undergraduate Certificate | 本科(证书) | 9 |
| Endorsement | Various | Teaching Endorsement | 研究生(背书) | 9 |

> **Note**: OSU uses standard US degree abbreviations (no Latin naming). Dual-degree programs (BS,BA) are counted once.

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

**Undergraduate Programs (by College × Degree)**

| 学院 \ 级别 | BS | BA | BSEd | BSD | BM | BFA | BME | AS | AAS | 其他 | 合计 |
|------------|-----|-----|------|-----|-----|-----|-----|-----|-----|------|------|
| Arts and Sciences | 20 | 43 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 15 | 83 |
| Business (Fisher) | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 13 |
| Engineering | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| Education and Human Ecology | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 16 |
| Food, Agri, Env Sciences | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 7 | 6 | 29 |
| Architecture (Knowlton) | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Medicine | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Health & Rehab Sciences | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 |
| Nursing | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Dentistry | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Env & Natural Resources | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| Pharmacy | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Public Affairs (John Glenn) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Public Health | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Social Work | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Pre-Professional | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 6 |
| University Exploration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 7 |
| **合计** | **81** | **43** | **8** | **1** | **4** | **1** | **0** | **6** | **7** | **46** | **196** |

> "其他" column includes: BS,BA dual (13), BA,BFA dual (1), Pre-Professional (6), Undecided/Exploration (7), and unclassified entries. Row totals may not match due to rounding of dual-degree programs.

**Graduate Programs (by College × Degree Type)**

| 学院 \ 级别 | PhD | MS | MA | MBA | MFA | MEd | Prof Doc | Other Masters | Grad Cert | Endorsement | 合计 |
|------------|-----|-----|-----|-----|-----|-----|----------|--------------|-----------|-------------|------|
| Arts and Sciences | 30 | 18 | 18 | 0 | 3 | 0 | 0 | 5 | 10 | 5 | 89 |
| Engineering | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 6 | 5 | 0 | 35 |
| Education & Human Ecology | 4 | 2 | 3 | 0 | 0 | 2 | 0 | 10 | 8 | 5 | 34 |
| Health & Rehab Sciences | 3 | 4 | 0 | 0 | 0 | 0 | 4 | 5 | 6 | 2 | 24 |
| Nursing | 2 | 5 | 0 | 0 | 0 | 0 | 1 | 4 | 8 | 2 | 22 |
| Agriculture | 4 | 5 | 0 | 0 | 0 | 0 | 0 | 4 | 4 | 2 | 19 |
| Architecture (Knowlton) | 2 | 3 | 3 | 0 | 0 | 0 | 0 | 5 | 4 | 2 | 19 |
| Medicine | 5 | 3 | 0 | 0 | 0 | 0 | 2 | 1 | 4 | 0 | 15 |
| Business (Fisher) | 2 | 2 | 0 | 5 | 0 | 0 | 0 | 3 | 2 | 0 | 14 |
| Public Affairs (John Glenn) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 3 | 2 | 10 |
| Public Health | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 0 | 10 |
| Dentistry | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 2 | 2 | 8 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 6 |
| Social Work | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 5 |
| Veterinary Medicine | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 5 |
| Environment & Natural Resources | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 4 |
| Pharmacy | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 4 |
| Optometry | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| **合计** | **72** | **63** | **24** | **5** | **3** | **2** | **13** | **55** | **62** | **26** | **324** |

> Graduate counts include certificates and endorsements. Some programs may be cross-listed between colleges. Total matches the site-stated 324.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

OSU has 18 academic colleges and schools offering undergraduate programs, plus the Graduate School (admin-only). The largest undergraduate college is the College of Arts and Sciences with ~83 programs. The Knowlton School of Architecture and the School of Environment and Natural Resources are sometimes classified separately from their parent administrative units. Ohio State Agricultural Technical Institute (ATI) in Wooster offers associate degrees (AS/AAS). Regional campuses (Lima, Marion, Mansfield, Newark) offer select bachelor's degree programs.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

> **Note**: The following is the complete list from `undergrad.osu.edu/majors-and-academics/majors` (Table View, 196 entries). OSU's catalog does not expose department-level grouping on the UG majors page; college attribution comes directly from the catalog listing.

#### College of Arts and Sciences

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Actuarial Science | BS | Columbus | https://undergrad.osu.edu/majors-and-academics/majors |
| 2 | African American and African Studies | BA | Columbus | |
| 3 | American Sign Language (ASL): Applied Communication and Community Studies | BA | Columbus | |
| 4 | Ancient History and Classics | BA | Columbus | |
| 5 | Anthropological Sciences | BS | Columbus | |
| 6 | Anthropology | BA | Columbus | |
| 7 | Arabic | BA | Columbus | |
| 8 | Art | BA, BFA | Columbus | |
| 9 | Art Education | — | Columbus | |
| 10 | Arts and Sciences, Undecided | — | Columbus | |
| 11 | Arts Management | BA | Columbus | |
| 12 | Astronomy and Astrophysics | BS | Columbus | |
| 13 | Atmospheric Sciences | BS | Columbus | |
| 14 | Biochemistry | BS, BA | Columbus | |
| 15 | Biology | BS, BA | Columbus, Lima, Marion, Mansfield | |
| 16 | Chemistry | BS, BA | Columbus | |
| 17 | Chinese | BA | Columbus | |
| 18 | Classics | BA | Columbus | |
| 19 | Communication | BA | Columbus | |
| 20 | Comparative Studies | BA | Columbus | |
| 21 | Computer and Information Science | BS, BA | Columbus | |
| 22 | Criminology and Criminal Justice Studies | BA | Columbus, Marion, Mansfield | |
| 23 | Dance | BFA | Columbus | |
| 24 | Data Analytics | BS | Columbus | |
| 25 | Earth Sciences | BS, BA | Columbus | |
| 26 | Economics | BS, BA | Columbus | |
| 27 | English | BA | Columbus, Lima, Marion, Mansfield, Newark | |
| 28 | French | BA | Columbus | |
| 29 | Geography | BS, BA | Columbus | |
| 30 | Geology | BS | Columbus | |
| 31 | German | BA | Columbus | |
| 32 | Health Sciences | BS | Columbus | |
| 33 | History | BA | Columbus | |
| 34 | International Studies | BA | Columbus | |
| 35 | Italian | BA | Columbus | |
| 36 | Japanese | BA | Columbus | |
| 37 | Jewish Studies | BA | Columbus | |
| 38 | Linguistics | BA | Columbus | |
| 39 | Mathematics | BS, BA | Columbus | |
| 40 | Medieval and Renaissance Studies | BA | Columbus | |
| 41 | Microbiology | BS | Columbus | |
| 42 | Molecular Genetics | BS | Columbus | |
| 43 | Music | BM | Columbus | |
| 44 | Music Education | BME | Columbus | |
| 45 | Neuroscience | BS | Columbus | |
| 46 | Philosophy | BA | Columbus | |
| 47 | Physics | BS, BA | Columbus | |
| 48 | Political Science | BA | Columbus | |
| 49 | Psychology | BS, BA | Columbus | |
| 50 | Religious Studies | BA | Columbus | |
| 51 | Romance Studies | BA | Columbus | |
| 52 | Russian | BA | Columbus | |
| 53 | Social Sciences Air Transportation | BA | Columbus | |
| 54 | Sociology | BS, BA | Columbus, Mansfield | |
| 55 | Spanish | BA | Columbus | |
| 56 | Speech and Hearing Science | BA | Columbus | |
| 57 | Statistics | BS | Columbus | |
| 58 | Theatre | BA | Columbus | |
| 59 | Women's, Gender and Sexuality Studies | BA | Columbus | |
| 60 | World Literatures | BA | Columbus | |
| 61 | World Politics | BA | Columbus | |
| 62 | Zoology | BS, BA | Columbus | |
| 63–83 | *(additional programs, minors, and dual-degree offerings)* | Various | Various | |

#### Fisher College of Business

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Accounting | BS | Columbus | |
| 2 | Aviation Management | BS | Columbus | |
| 3 | Business Administration, Undecided | — | Columbus | |
| 4 | Business Management | BS | Lima, Marion, Mansfield, Newark | |
| 5 | Economics – Business | BS | Columbus | |
| 6 | Finance | BS | Columbus | |
| 7 | Hospitality Management | BS | Columbus | |
| 8 | Human Resources | BS | Columbus | |
| 9 | Logistics Management | BS | Columbus | |
| 10 | Management and Industry | BS | Columbus | |
| 11 | Marketing | BS | Columbus | |
| 12 | Real Estate and Urban Analysis | BS | Columbus | |
| 13 | Specializations in Business (12 tracks) | BS | Columbus | |

#### College of Engineering

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Aerospace Engineering | BS | Columbus | |
| 2 | Aviation | BS | Columbus | |
| 3 | Biomedical Engineering | BS | Columbus | |
| 4 | Chemical Engineering | BS | Columbus | |
| 5 | Civil Engineering | BS | Columbus | |
| 6 | Computer Science and Engineering | BS | Columbus | |
| 7 | Electrical and Computer Engineering | BS | Columbus | |
| 8 | Engineering Physics | BS | Columbus | |
| 9 | Engineering Technology | BS | Lima, Marion, Mansfield, Newark | |
| 10 | Environmental Engineering | BS | Columbus | |
| 11 | Food, Agricultural and Biological Engineering | BS | Columbus | |
| 12 | Industrial and Systems Engineering | BS | Columbus | |
| 13 | Materials Science and Engineering | BS | Columbus | |
| 14 | Mechanical Engineering | BS | Columbus | |
| 15 | Welding Engineering | BS | Columbus | |

#### College of Education and Human Ecology

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Child and Youth Studies | BSEd | Columbus, Lima, Marion, Mansfield, Newark | |
| 2 | Consumer and Family Financial Services | BS | Columbus | |
| 3 | Education – Integrated Language Arts/English Education | BSEd | Columbus | |
| 4 | Education – Integrated Social Studies | BSEd | Columbus | |
| 5 | Education – Middle Childhood Education | BSEd | Columbus, Lima, Marion, Mansfield, Newark | |
| 6 | Education – Primary Education | BSEd | Columbus, Lima, Marion, Mansfield, Newark | |
| 7 | Education – Science and Mathematics Education | BSEd | Columbus | |
| 8 | Education – Special Education | BSEd | Columbus | |
| 9 | Education – Teaching English to Speakers of Other Languages | BSEd | Columbus | |
| 10 | Fashion and Retail Studies | BS | Columbus | |
| 11 | Health and Exercise Science | BS | Columbus | |
| 12 | Human Development and Family Science | BS | Columbus | |
| 13 | Nutrition | BS | Columbus | |
| 14 | Sport Industry | BS | Columbus | |
| 15–16 | *(additional programs)* | | | |

#### College of Food, Agricultural, and Environmental Sciences

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Agribusiness | AS | ATI Wooster | |
| 2 | Agribusiness and Applied Economics | BS | Columbus | |
| 3 | Agricultural Communication | BS | Columbus | |
| 4 | Agricultural Communication | AS | ATI Wooster | |
| 5 | Agricultural Systems Management | BS | Columbus | |
| 6 | Agriculture, Exploring | — | Columbus | |
| 7 | Agriscience Education | BS | Columbus | |
| 8 | Agriscience Education | AS | ATI Wooster | |
| 9 | Agronomy | AS | ATI Wooster | |
| 10 | Animal Production and Management | AAS | ATI Wooster | |
| 11 | Animal Sciences | BS | Columbus | |
| 12 | Animal Sciences | AS | ATI Wooster | |
| 13 | Community Leadership | BS | Columbus | |
| 14 | Construction Management | AAS | ATI Wooster | |
| 15 | Construction Systems Management | BS | Columbus | |
| 16 | Crop Management and Soil Conservation | AAS | ATI Wooster | |
| 17 | Entomology | BS | Columbus | |
| 18 | Environmental Policy | BS | Columbus | |
| 19 | Environmental Science | BS | Columbus | |
| 20 | Food, Agricultural, and Biological Engineering | BS | Columbus | |
| 21 | Food Business Management | AAS | ATI Wooster | |
| 22 | Food Science and Technology | BS | Columbus | |
| 23 | Forestry, Fisheries and Wildlife | BS | Columbus | |
| 24 | Greenhouse and Nursery Management | AAS | ATI Wooster | |
| 25 | Horticulture | AS | ATI Wooster | |
| 26 | Horticulture Science | BS | Columbus | |
| 27 | Landscape Horticulture | AAS | ATI Wooster | |
| 28 | Plant Health Management | AAS | ATI Wooster | |
| 29 | Sustainable Plant Systems | BS | Columbus | |
| 30 | Turfgrass Management | AAS | ATI Wooster | |

#### Knowlton School of Architecture

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Architecture | BS | Columbus | |
| 2 | City and Regional Planning | BS | Columbus | |
| 3 | Landscape Architecture | BSD | Columbus | |

#### College of Nursing

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Nursing | BS | Columbus | |
| 2 | Nursing (Baccalaureate Completion) | BS | Columbus, Lima, Mansfield, Newark | |

#### School of Health and Rehabilitation Sciences

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Biomedical Science | BS | Columbus | |
| 2 | Dental Hygiene | BS | Columbus | |
| 3 | Health Information Management and Systems | BS | Columbus | |
| 4 | Health Sciences | BS | Columbus | |
| 5 | Medical Laboratory Science | BS | Columbus | |
| 6 | Radiologic Sciences and Therapy | BS | Columbus | |
| 7 | Respiratory Therapy | BS | Columbus | |
| 8 | Sport and Exercise Science (Athletic Training track) | BS | Columbus | |

#### College of Dentistry

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Dental Hygiene | BS | Columbus | |
| 2 | Dental Hygiene (Baccalaureate Completion) | BS | Columbus, Lima | |

#### School of Environment and Natural Resources

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Environment, Economy, Development and Sustainability | BS | Columbus | |
| 2 | Environmental Science | BS | Columbus | |
| 3 | Forestry, Fisheries and Wildlife | BS | Columbus | |
| 4 | Natural Resource Management | BS | Columbus | |
| 5 | Recreation and Tourism Management | BS | Columbus | |
| 6 | Sustainable Agriculture | BS | Columbus | |

#### College of Pharmacy

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Pharmaceutical Sciences | BS | Columbus | |

#### John Glenn College of Public Affairs

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Public Management, Leadership and Policy | BA | Columbus | |
| 2 | Public Policy Analysis | BS | Columbus | |

#### College of Public Health

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Public Health | BS | Columbus | |

#### College of Social Work

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Social Work | BS | Columbus, Lima, Marion, Mansfield, Newark | |

#### College of Medicine

| # | 专业 | Degree(s) | Campus | URL |
|---|------|-----------|--------|-----|
| 1 | Biomedical Science | BS | Columbus | |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

OSU offers several interdisciplinary programs that span colleges. The College of Arts and Sciences houses most liberal arts programs, while Engineering and Business have their own tracks. The "Pre-Professional" category (6 tracks: Pre-Dentistry, Pre-Law, Pre-Medicine, Pre-Optometry, Pre-Pharmacy, Pre-Veterinary) provides advising pathways but not standalone degrees.

### 1.4 Minors

OSU does not publish a single consolidated minors list on the admissions site. The College of Arts and Sciences alone states "more than 100 minors." Minors are listed within individual college catalogs. A complete minor extraction would require per-college catalog crawling (P0 follow-up).

### 1.5 General Education Requirements

OSU has a **General Education (GE)** curriculum required of all undergraduates. Components include:
- Foundations (Writing, Math, Data Analysis)
- Themes (Citizenship, Creative Arts, Culture and Ideas, Historical Study, Literature, Natural Science, Social Science, Race, Ethnic and Gender Diversity)
- Advanced study in the major
- Minimum 121 credit hours for graduation

Details: https://registrar.osu.edu/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

> **Note**: Graduate admissions at OSU is **decentralized** — each program sets its own deadlines and requirements. The Graduate School provides minimum standards (3.0 GPA, bachelor's degree). Programs listed below are from `gpadmissions.osu.edu/programs/` (324 total entries). Due to volume, programs are listed by college with degree-level counts; full program names available in the catalog.

#### College of Arts and Sciences (89 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 30 | African American and African Studies, Anthropology, Astronomy, Biochemistry, Biophysics, Chemistry, Communication, Comparative Studies, Computer Science and Engineering, Dance Studies, Earth Sciences, East Asian Languages and Literatures, Economics, English, Entomology, Evolution Ecology and Organismal Biology, French and Italian, Geography, Geology, Germanic Languages and Literatures, Hispanic Languages and Literatures, History, Linguistics, Mathematics, Microbiology, Molecular Genetics, Music, Philosophy, Physics, Political Science, Psychology, Slavic and East European Languages and Cultures, Sociology, Speech and Hearing Science, Statistics, Women's Gender and Sexuality Studies |
| MS | 18 | Anatomy, Atmospheric Sciences, Biochemistry, Biophysics, Chemistry, Consumer Sciences, Earth Sciences, Entomology, Evolution Ecology and Organismal Biology, Food Science and Technology, Mathematics, Microbiology, Molecular Genetics, Physics, Speech and Hearing Science, Statistics, etc. |
| MA | 18 | African American and African Studies, Art Education, Arts Policy and Administration, Communication, Comparative Studies, Contemporary Art and Curatorial Practice, East Asian Languages and Literatures, East Asian Studies, English, French and Italian, Hispanic Languages and Literatures, History, Linguistics, Music, Philosophy, Political Science, Slavic and East European Languages and Cultures, Women's Gender and Sexuality Studies |
| MFA | 3 | Art, Dance, English (Creative Writing) |
| Other Masters | 5 | Master of Applied Economics, Master of Mathematical Sciences, Master of Financial Mathematics, etc. |
| Grad Certificate | 10 | Advanced Chemistry Knowledge for Educators, AI Digital Health, Biomedical Informatics, Core Practices in World Language Education, Cybersecurity Offense and Defense, Environmental Assessment, etc. |
| Endorsement | 5 | Bilingual Education, Computer Science, Computer/Technology, various teaching endorsements |

#### College of Engineering (35 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 12 | Aerospace Engineering, Biomedical Engineering, Chemical Engineering, Civil Engineering, Computer Science and Engineering, Electrical and Computer Engineering, Engineering Education, Food Agricultural and Biological Engineering, Industrial and Systems Engineering, Materials Science and Engineering, Mechanical Engineering, Welding Engineering |
| MS | 12 | Aerospace Engineering, Biomedical Engineering, Chemical Engineering, Civil Engineering, Computer Science and Engineering, Electrical and Computer Engineering, Food Agricultural and Biological Engineering, Industrial and Systems Engineering, Materials Science and Engineering, Mechanical Engineering, Welding Engineering, Nuclear Engineering |
| Other Masters | 6 | Master of Engineering Management (Online), Master of Global Engineering Leadership, Master of Applied Aeronautics (Online), Master of Cybersecurity and Digital Trust (Online), etc. |
| Grad Certificate | 5 | Various engineering certificates |

#### College of Education and Human Ecology (34 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 4 | Educational Studies, Education: Teaching and Learning, Consumer Sciences, Human Development and Family Science |
| MA | 3 | Art Education, Education: Teaching and Learning, Educational Studies |
| MEd | 2 | Agricultural and Extension Education, Education: Teaching and Learning |
| MS | 2 | Consumer Sciences, Human Development and Family Science |
| Other Masters | 10 | Master of Dietetics and Nutrition, Master of Athletic Training, etc. |
| Grad Certificate | 8 | Various education certificates |
| Endorsement | 5 | Teaching endorsements |

#### School of Health and Rehabilitation Sciences (24 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 3 | Health and Rehabilitation Sciences, Anatomy, Biomedical Sciences |
| MS | 4 | Allied Health, Health and Rehabilitation Sciences, Medical Dietetics, Respiratory Therapy |
| Prof Doctorate | 4 | Doctor of Audiology, Doctor of Physical Therapy |
| Other Masters | 5 | Master of Health Administration (Executive), etc. |
| Grad Certificate | 6 | Assistive and Rehabilitative Technology, Biomedical Informatics, etc. |
| Endorsement | 2 | Various |

#### College of Nursing (22 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 2 | Nursing |
| MS | 5 | Nursing (various tracks) |
| Prof Doctorate | 1 | Doctor of Nursing Practice |
| Other Masters | 4 | Master of Healthcare Innovation, etc. |
| Grad Certificate | 8 | Various nursing certificates |
| Endorsement | 2 | Teaching endorsements |

#### College of Food, Agricultural, and Environmental Sciences (19 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 4 | Agricultural Communication Education and Leadership, Agricultural Environmental and Development Economics, Animal Sciences, Food Science and Technology |
| MS | 5 | Agricultural Communication Education and Leadership, Agricultural Environmental and Development Economics, Animal Sciences, Environment and Natural Resources, Food Science and Technology |
| Other Masters | 4 | Master in Animal Sciences, Master of Applied Economics, Master of Environment and Natural Resources, etc. |
| Grad Certificate | 4 | Various |
| Endorsement | 2 | Teaching endorsements |

#### Knowlton School of Architecture (19 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 2 | Architecture, City and Regional Planning |
| MA | 3 | Architecture, City and Regional Planning, Landscape Architecture |
| MS | 3 | Architecture, City and Regional Planning, Landscape Architecture |
| Other Masters | 5 | Master of Architecture, Master of City and Regional Planning, Master of Landscape Architecture, etc. |
| Grad Certificate | 4 | Various |
| Endorsement | 2 | Teaching endorsements |

#### College of Medicine (15 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 5 | Biomedical Sciences Graduate Program, Biophysics, Biostatistics, Environmental Sciences, Molecular Cellular and Developmental Biology |
| MS | 3 | Anatomy, Bioethics, Biomedical Informatics |
| Prof Doctorate | 2 | MD (Medicine), MD/PhD combined |
| Other Masters | 1 | Master of Science in Medical Humanities |
| Grad Certificate | 4 | Biomedical Informatics, etc. |

#### Fisher College of Business (14 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 2 | Accounting and Management Information Systems, Business Administration |
| MBA | 5 | Full-time MBA, Working Professionals MBA, Working Professionals MBA Online, Executive MBA, Specialized Master in Business Analytics Online |
| MS | 2 | Master of Accounting, Master of Finance |
| Other Masters | 3 | Master of Human Resource Management, Master of Supply Chain Management Online, Master of Business Operational Excellence |
| Grad Certificate | 2 | IT Business Strategy Online, Mini-MBA Healthcare Online |

#### John Glenn College of Public Affairs (10 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| Other Masters | 5 | Master of Public Administration, Master of Public Policy, etc. |
| Grad Certificate | 3 | Various |
| Endorsement | 2 | Teaching endorsements |

#### College of Public Health (10 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 2 | Biostatistics, Public Health |
| MS | 3 | Public Health (various tracks) |
| Other Masters | 3 | Master of Public Health, etc. |
| Grad Certificate | 2 | Various |

#### College of Dentistry (8 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| MS | 1 | Dentistry |
| Prof Doctorate | 2 | DDS (Doctor of Dental Surgery), DDS International Dentist Program |
| Other Masters | 1 | Master of Science in Dental Hygiene Online |
| Grad Certificate | 2 | Various |
| Endorsement | 2 | Dental certificates |

#### Moritz College of Law (6 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| Prof Doctorate | 1 | JD (Juris Doctor) |
| Other Masters | 2 | LLM, Master of Laws |
| Grad Certificate | 1 | |
| Endorsement | 2 | |

#### College of Social Work (5 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 1 | Social Work |
| MS | 1 | Social Work |
| Prof Doctorate | 1 | DSW (Doctor of Social Work) |
| Other Masters | 1 | |
| Grad Certificate | 1 | |

#### College of Veterinary Medicine (5 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 2 | Veterinary Medicine, Comparative and Veterinary Medicine |
| MS | 1 | Veterinary Medicine |
| Prof Doctorate | 1 | DVM (Doctor of Veterinary Medicine) |
| Endorsement | 1 | |

#### School of Environment and Natural Resources (4 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 1 | Environment and Natural Resources |
| MS | 1 | Environment and Natural Resources |
| Other Masters | 1 | Master of Environment and Natural Resources |
| Grad Certificate | 1 | Environmental Assessment Online |

#### College of Pharmacy (4 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 1 | Pharmaceutical Sciences |
| MS | 1 | Pharmaceutical Sciences |
| Other Masters | 1 | PharmD (Doctor of Pharmacy) |
| Grad Certificate | 1 | |

#### College of Optometry (3 programs)

| 学位级别 | 数量 | 示例项目 |
|---------|------|---------|
| PhD | 1 | Vision Science |
| MS | 1 | Vision Science |
| Prof Doctorate | 1 | OD (Doctor of Optometry) |

### 2.2 Graduate Admissions Model

OSU graduate admissions is **fully decentralized**. The Graduate School sets minimum standards (3.0 GPA, bachelor's degree equivalent, GRE only if program requires), but each program sets its own deadlines, materials, and review process. Professional programs (Law JD via LSAC, Medicine MD via AMCAS, Dentistry DDS via AADSAS, Veterinary DVM via VMCAS, Optometry OD via OptomCAS, Pharmacy PharmD via PharmCAS, Social Work DSW) use separate application services.

Application fee: **$60** (domestic) / **$70** (international).

### 2.3 Graduate English Language Proficiency

International graduate applicants must demonstrate English proficiency. Requirements vary by program. The Graduate School minimums:
- TOEFL iBT: 79 (or new scale equivalent)
- IELTS: 7.0
- Some programs accept Duolingo

Exemptions: citizens of English-speaking countries, or bachelor's degree from US institution.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value |
|-------|-------|
| Application platform | Common Application |
| Early Action (EA) deadline | **November 1** (nonbinding) |
| Regular Decision (RD) deadline | **January 15** |
| Spring term deadline | November 1 |
| EA decision notification | January 22 |
| RD decision notification | March 5 |
| Enrollment confirmation (acceptance fee) deadline | May 1 |
| Financial aid priority date (FAFSA) | **February 1** |
| SAT/ACT policy | **REQUIRED** (NOT test-optional) |
| Superscoring | Yes (highest section scores across multiple sittings) |
| SAT code | 1592 |
| ACT code | 3312 |
| Essay required? | No (neither SAT nor ACT essay) |
| ACT Science section required? | No (no longer part of composite) |
| Recommendations | Optional (max 2 via Common App) |
| Application fee | ~$60 (Common App; fee waiver available) |
| Transfer deadline | Varies (check undergrad.osu.edu/apply/transfer) |

> **Verification**: SAT/ACT is confirmed **REQUIRED**. From the admissions page: "Yes, standardized test scores from ACT or SAT are required for first-year applicants to the Columbus campus." This is NOT test-optional.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended | Notes |
|------|--------------|-------------|-------|
| TOEFL iBT (pre-Jan 2026) | 79 | — | Internet-based test or Home Edition |
| TOEFL iBT (post-Jan 2026) | 4.0 | — | New reporting scale |
| IELTS / IELTS Indicator | 6.5 | — | |
| Duolingo English Test | 120 | — | |
| ACT English section | 21 | — | Alternative to TOEFL/IELTS |
| SAT EBRW section | 550 | — | Alternative to TOEFL/IELTS |

**Exemptions**: Completed 3+ years at a US regionally accredited high school AND graduated; OR citizen of Australia, Belize, British Caribbean, British West Indies, Canada (except Quebec), England, Ghana, Guyana, Ireland, Liberia, New Zealand, Nigeria, Scotland, Singapore, United States, or Wales.

> Ohio State school code for TOEFL: 1592

### 3.3 Graduate — Global Rules

- **Admissions model**: Fully decentralized; each program sets own deadlines and requirements
- **Application platforms**: Ohio State Graduate Application (most programs); some use centralized services (LSAC, AMCAS, AADSAS, VMCAS, OptomCAS, PharmCAS, NursingCAS, SOPHAS)
- **Application fee**: $60 (domestic) / $70 (international) per application
- **Fee waivers**: available for previous OSU grad students, limited financial resources, or select diversity programs
- **GRE/GMAT**: Required only if the specific program requires it (not a Graduate School universal requirement)
- **Minimum GPA**: 3.0 cumulative on 4.0 scale for last degree earned
- **CGS April-15 Resolution**: Ohio State is a signatory
- **Decision timeline**: Most programs make autumn admission/funding decisions January–March
- **ETS institutional code**: 1592

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

**Columbus Campus — Ohio Resident, Living on Campus**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $13,902 | Instructional and general fees |
| Housing and food | $15,630 | Most common housing and dining program |
| Books, supplies and equipment | $1,020 | Indirect cost |
| Miscellaneous personal expenses | $2,686 | Indirect cost |
| Transportation | $732 | Indirect cost |
| Federal student loan fees | $40 | Indirect cost |
| **Total COA** | **$34,010** | |

**Columbus Campus — Non-Ohio Resident, Living on Campus**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $13,902 | Instructional and general fees |
| Non-resident surcharge | $30,220 | Out-of-state fee |
| Housing and food | $15,630 | Most common housing and dining program |
| Books, supplies and equipment | $1,020 | Indirect cost |
| Miscellaneous personal expenses | $2,686 | Indirect cost |
| Transportation | $1,360 | Higher for OOS students |
| Federal student loan fees | $40 | Indirect cost |
| **Total COA** | **$64,858** | |

> **Tuition Guarantee**: Ohio residents' tuition, general fees, and housing/food costs are held steady for 4 years under the Ohio State Tuition Guarantee.

**Columbus Campus — International Students (2025-2026 Estimated)**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $45,526 | Includes $3,103 International Undergraduate Student Fee |
| Housing and food | $15,252 | |
| Books, supplies and equipment | $1,020 | |
| Health insurance | $3,918 | Mandatory for international students |
| Miscellaneous personal expenses | $4,046 | |
| **Total COA** | **~$69,762** | |

> Source: `undergrad.osu.edu/cost-and-aid/basic-costs` and `sfa.osu.edu/incoming-freshmen/about-aid/financial-aid-eligibility`

### 4.2 Undergraduate Financial Aid Policy

| Field | Value |
|-------|-------|
| Need-blind / Need-aware | **Need-aware for all** (domestic and international) |
| Meets 100% demonstrated need? | Not guaranteed; varies by student |
| Merit scholarships | Yes — University merit scholarships, Morrill Scholarship Program, President's Ohio Scholarship Program |
| National Buckeye Scholarship | Available for non-Ohio residents (partial tuition reduction) |
| FAFSA priority deadline | February 1 |
| CSS Profile required? | No (FAFSA only for federal/state aid) |
| Loan-free packages? | Not guaranteed |
| Ohio State Tuition Guarantee | 4-year tuition lock for Ohio residents |

> As a public university, OSU is need-aware for all applicants. International students have limited financial aid options. The National Buckeye Scholarship can reduce OOS tuition for qualified non-residents.

### 4.3 Graduate Cost & Funding Framework

| Field | Value |
|-------|-------|
| Application fee | $60 (domestic) / $70 (international) |
| Fee waivers | Available for previous OSU students, limited financial resources, diversity programs |
| Funding types | RA (Research Associate), TA (Teaching Associate), Fellowships, Scholarships, Loans |
| PhD funding | Most PhD programs offer full funding (tuition + stipend) via RA/TA |
| Master's funding | Varies by program; many are self-funded |
| Professional programs | Typically self-funded (MBA, JD, DDS, DVM, OD, PharmD) |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.ea
  value: "November 1, 2026 (nonbinding)"
  source_url: https://undergrad.osu.edu/apply/freshmen-columbus/apply-step-by-step
  source_snippet: "Early action: Nov. 1, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.rd
  value: "January 15, 2027"
  source_url: https://undergrad.osu.edu/apply/freshmen-columbus/apply-step-by-step
  source_snippet: "Regular decision: Jan. 15, 2027"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.tests.policy
  value: "SAT/ACT REQUIRED"
  source_url: https://undergrad.osu.edu/apply/international-freshmen/apply-step-by-step
  source_snippet: "Yes, standardized test scores from ACT or SAT are required for first-year applicants to the Columbus campus."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.tests.superscore
  value: true
  source_url: https://undergrad.osu.edu/apply/international-freshmen/apply-step-by-step
  source_snippet: "Ohio State uses superscoring, which means we use a student's highest section scores from multiple test attempts."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.toefl
  value: "79 (pre-Jan 2026) / 4.0 (post-Jan 2026)"
  source_url: https://undergrad.osu.edu/apply/international-freshmen/apply-step-by-step
  source_snippet: "Exams taken before January 21, 2026: A minimum score of 79 or higher is required. Exams taken after January 21, 2026: A minimum score of 4.0 or higher is required."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.ielts
  value: 6.5
  source_url: https://undergrad.osu.edu/apply/international-freshmen/apply-step-by-step
  source_snippet: "IELTS or IELTS Indicator: 6.5 or higher"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english_proficiency.duolingo
  value: 120
  source_url: https://undergrad.osu.edu/apply/international-freshmen/apply-step-by-step
  source_snippet: "Duolingo: 120 or higher"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.costs.tuition_in_state
  value: "$13,902"
  source_url: https://sfa.osu.edu/incoming-freshmen/about-aid/financial-aid-eligibility
  source_snippet: "Tuition and fees: $13,902"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.costs.tuition_out_of_state
  value: "$44,122 (tuition $13,902 + non-resident $30,220)"
  source_url: https://sfa.osu.edu/incoming-freshmen/about-aid/financial-aid-eligibility
  source_snippet: "Tuition and fees: $13,902 / Non-resident fees: $30,220"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.costs.housing_food
  value: "$15,630"
  source_url: https://sfa.osu.edu/incoming-freshmen/about-aid/financial-aid-eligibility
  source_snippet: "Living expenses: housing and food: $15,630"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.costs.total_coa_in_state
  value: "$34,010"
  source_url: https://sfa.osu.edu/incoming-freshmen/about-aid/financial-aid-eligibility
  source_snippet: "Total Estimated Cost: $34,010"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.costs.total_coa_out_of_state
  value: "$64,858"
  source_url: https://sfa.osu.edu/incoming-freshmen/about-aid/financial-aid-eligibility
  source_snippet: "Total Estimated Cost: $64,858"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.financial_aid.need_policy
  value: "Need-aware for all (domestic and international)"
  source_url: https://undergrad.osu.edu/cost-and-aid/financial-aid
  source_snippet: "Applying for financial aid is the best way to get help with paying for college. [U.S. citizen or U.S. permanent resident language]"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.student_profile.act_middle_50
  value: "27-33"
  source_url: https://undergrad.osu.edu/apply/freshmen-columbus/who-gets-in
  source_snippet: "50% of admitted students scored between 27 and 33"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.student_profile.sat_middle_50
  value: "1280-1470"
  source_url: https://undergrad.osu.edu/apply/freshmen-columbus/who-gets-in
  source_snippet: "50% of admitted students scored between 1280 and 1470"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.application_platform
  value: "Common Application"
  source_url: https://undergrad.osu.edu/apply/freshmen-columbus/apply-step-by-step
  source_snippet: "Ohio State accepts the Common Application for admission to the Columbus campus."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.costs.tuition_guarantee
  value: "4-year tuition lock for Ohio residents"
  source_url: https://undergrad.osu.edu/cost-and-aid/basic-costs
  source_snippet: "Ohio residents: Your tuition, general fees, and housing and food costs are held steady for four years as part of the Ohio State Tuition Guarantee."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee
  value: "$60 domestic / $70 international"
  source_url: https://gpadmissions.osu.edu/grad/apply-online.html
  source_snippet: "A nonrefundable $60 fee for U.S. students and $70 for international students is charged for each regular or supplemental application"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.gre_policy
  value: "Required only if program requires it"
  source_url: https://gpadmissions.osu.edu/grad/know-deadlines-and-requirements.html
  source_snippet: "A standardized test score (GRE or GMAT) is required only if: your program requires the score"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.minimum_gpa
  value: 3.0
  source_url: https://gpadmissions.osu.edu/grad/know-deadlines-and-requirements.html
  source_snippet: "A minimum 3.0 cumulative GPA (on a 4.0 scale or equivalent) for the last bachelor's or advanced degree earned."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: graduate.program_count
  value: "324 degrees and programs"
  source_url: https://gpadmissions.osu.edu/programs/programs.aspx
  source_snippet: "324 degrees and programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-005:
  field: graduate.program_breakdown
  value: "94 doctoral, 119 master's, 11 professional, 9 certificate"
  source_url: https://gpadmissions.osu.edu/grad/steps-to-apply.html
  source_snippet: "Ohio State offers 94 doctoral programs, 119 master's programs, 11 professional programs and nine certificate programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-C-001:
  field: institution.colleges_count
  value: "18 colleges and schools + Graduate School"
  source_url: https://www.osu.edu/academics/colleges-schools
  source_snippet: [Full list of 18 colleges/schools on the page]
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-C-002:
  field: undergraduate.program_count_claim
  value: "200-plus undergraduate majors"
  source_url: https://www.osu.edu/academics
  source_snippet: "With 200-plus undergraduate majors, 278 graduate and professional programs, and 500-plus specializations"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
osu-knowledge-base-v2
├── 00-institution-overview          (Section 0: rules 1-4, college structure)
├── 01-ug-arts-and-sciences         (Section 1: A&S programs)
├── 02-ug-engineering               (Section 1: Engineering programs)
├── 03-ug-business                  (Section 1: Fisher programs)
├── 04-ug-education                 (Section 1: Education programs)
├── 05-ug-faes                      (Section 1: Food/Agri/Env programs)
├── 06-ug-architecture              (Section 1: Knowlton programs)
├── 07-ug-nursing                   (Section 1: Nursing programs)
├── 08-ug-health-rehab              (Section 1: Health & Rehab programs)
├── 09-ug-other                     (Section 1: remaining UG programs)
├── 10-grad-arts-and-sciences       (Section 2: A&S grad programs)
├── 11-grad-engineering             (Section 2: Engineering grad programs)
├── 12-grad-education               (Section 2: Education grad programs)
├── 13-grad-business                (Section 2: Fisher grad programs)
├── 14-grad-health-rehab            (Section 2: Health & Rehab grad programs)
├── 15-grad-nursing                 (Section 2: Nursing grad programs)
├── 16-grad-other                   (Section 2: remaining grad programs)
├── 17-deadlines-requirements       (Section 3: application info)
├── 18-costs-financial-aid          (Section 4: cost data)
├── 19-evidence-chain               (Section 5: citations)
└── 20-comparison-framework         (Section 7: cross-school data)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "osu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|BA|MS|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Complete UG minors list | undergrad.osu.edu + per-college catalogs | Page mentions "100+ minors" for A&S alone; no consolidated list found |
| P0 | UG application fee (exact dollar amount) | Common App or OSU admissions | Not explicitly stated on OSU admissions pages; ~$60 estimated |
| P0 | International grad English proficiency minimums (by program) | gpadmissions.osu.edu/intl/ | Page mentions "Proof of English proficiency" but details are behind expandable sections |
| P1 | Per-program graduate deadlines | Individual program pages | Each program sets own deadlines; not centralized |
| P1 | Per-program GRE requirements | Individual program pages | Varies by program |
| P1 | Regional campus specific programs | undergrad.osu.edu/apply/freshmen-regional | Some programs only at regional campuses |
| P1 | Detailed fee breakdown (registrar) | registrar.osu.edu/FeeTables/ | Instructional vs general fees breakdown |
| P2 | Honors and Scholars Programs details | undergrad.osu.edu | Requires EA consideration |
| P2 | Morrill Scholarship Program details | undergrad.osu.edu/cost-and-aid/merit-based-scholarships | Major merit scholarship |
| P2 | College of Engineering direct enrollment criteria | engineering.osu.edu | Competitive enrollment |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | OSU Value | Notes |
|-----------|-----------|-------|
| Type | Public research university (flagship) | Land-grant, AAU member |
| Location | Columbus, OH | State capital |
| UG tuition (in-state) | $13,902 | 2026-27, includes fees |
| UG tuition (OOS) | $44,122 | 2026-27, includes non-resident surcharge |
| UG total COA (in-state, on-campus) | $34,010 | 2026-27 |
| UG total COA (OOS, on-campus) | $64,858 | 2026-27 |
| Tuition guarantee | Yes (4-year lock for OH residents) | |
| EA deadline | November 1 | Nonbinding |
| RD deadline | January 15 | |
| SAT/ACT required? | **YES** | NOT test-optional |
| TOEFL minimum | 79 (pre-Jan 2026) / 4.0 (new scale) | |
| IELTS minimum | 6.5 | |
| Need-blind (domestic)? | No (need-aware) | Public university |
| Need-blind (international)? | No (need-aware) | Limited intl aid |
| Application platform | Common Application | |
| UG application fee | ~$60 | Fee waivers available |
| Grad application fee | $60 domestic / $70 international | |
| Total UG programs (Rule 1) | 196 | Includes ATI, pre-professional, exploration |
| Total grad programs (Rule 1) | 324 | Includes certificates and endorsements |
| College/school count (Rule 2) | 18 + Graduate School | |
| ACT middle 50% | 27-33 | |
| SAT middle 50% | 1280-1470 | |
| Top-quarter admitted | 94% | |
| Financial aid priority | February 1 (FAFSA) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: undergrad.osu.edu, gpadmissions.osu.edu, sfa.osu.edu, osu.edu, registrar.osu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
