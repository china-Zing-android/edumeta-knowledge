# University of Memphis Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Source domain**: www.memphis.edu (T4 public R1, Carnegie R1: Very High Research Activity; flagship of the Tennessee Board of Regents system). Law School (Cecil C. Humphreys) is separately accredited by the ABA.

---

## TABLE OF CONTENTS
- [0. 院校总览 (Institution overview)](#0-院校总览-institution-overview)
- [1. Undergraduate education](#1-undergraduate-education)
- [2. Graduate education](#2-graduate-education)
- [3. Application requirements & deadlines](#3-application-requirements--deadlines)
- [4. Costs & financial aid](#4-costs--financial-aid)
- [5. Evidence chain index](#5-evidence-chain-index)
- [6. WeKnora import manifest](#6-weknora-import-manifest)
- [7. Cross-school comparison framework](#7-cross-school-comparison-framework)

---

## 0. 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 | 备注 |
|------|------|------|
| 本科主修专业 (Major) | 52 | https://www.memphis.edu/academics/ugmajors.php (Major = "X" 列) |
| 本科辅修 (Minor) | 78 | 同表 Minor = "X" 列 |
| 本科学术方向/集中 (Concentration) | 91 | 同表 Concentration = "X" 列 |
| 研究生学位项目 (Major × Degree) | 81 | https://www.memphis.edu/gradschool/programs/index.php (主综合表 92 行 + 重复按学位拆分;去重后 66 个独立 Major) |
| 研究生高级证书 (Graduate Certificate) | 70 | https://www.memphis.edu/gradschool/programs/graduatecertificates.php |
| **学位项目总计 (UG Major + Grad Major unique)** | **118** | 52 + 66 |
| **目录条目总计 (UG 表 + Grad 主综合表 + Grad Cert)** | **326** | 167 UG 表行 + 92 Grad 主综合行 + 70 Cert 行;以原表行为单位 |

> **Reconciliation check**: Undergraduate table has 167 rows (header + 166 data rows). 52 majors + 78 minors + 91 concentrations = 221 "X" marks across 5 columns, distributed across 166 rows (some rows count as both Major/Concentration/Minor). The single-marker rows are most rows. — Source URL: https://www.memphis.edu/academics/ugmajors.php

### 0.2 学院 / 系层级结构

UofM (University of Memphis) has 13 academic colleges/schools plus the separately accredited Cecil C. Humphreys School of Law.

```
University of Memphis [总校]
├── College of Arts and Sciences (CAS)                                [学院] — https://www.memphis.edu/cas/index.php
│   ├── Anthropology                                                  [系]
│   ├── Biological Sciences (Biology)                                 [系]
│   ├── Chemistry                                                      [系]
│   ├── Computer Science                                              [系]
│   ├── Criminology and Criminal Justice                              [系]
│   ├── Earth Sciences                                                [系]
│   ├── English                                                       [系]
│   ├── History                                                       [系]
│   ├── Interdisciplinary Programs                                    [系]
│   ├── Mathematical Sciences (Mathematics)                           [系]
│   ├── Philosophy                                                    [系]
│   ├── Physics and Materials Science                                 [系]
│   ├── Political Science                                             [系]
│   ├── Psychology                                                    [系]
│   ├── Sociology                                                     [系]
│   ├── World Languages and Literatures                               [系]
│   ├── City and Regional Planning                                    [系]
│   ├── Public and Nonprofit Administration                           [系]
│   ├── School of Urban Affairs and Public Policy (SUAPP)             [系]
│   ├── School of Social Work                                         [系]
│   └── Pre-Health / Pre-Law (advisement tracks)                       [项目组]
├── College of Communication and Fine Arts (CCFA)                     [学院] — https://www.memphis.edu/ccfa/index.php
│   ├── Architecture (includes Interior Architecture)                  [系]
│   ├── Art and Design                                                 [系]
│   ├── Communication and Film                                        [系]
│   ├── Journalism and Strategic Media                                [系]
│   ├── Rudi E. Scheidt School of Music                               [系]
│   └── Theatre and Dance                                             [系]
├── College of Education                                              [学院] — https://www.memphis.edu/education/index.php
│   ├── Counseling, Educational Psychology and Research               [系]
│   ├── Instruction and Curriculum Leadership                         [系]
│   └── Leadership                                                    [系]
├── College of Health and Human Sciences                              [学院] — https://www.memphis.edu/healthsciences/index.php
│   ├── Health Sciences (HLSC)                                        [系]
│   ├── Communication Sciences (CSD; school-level in some pages)      [系]
│   ├── School of Communication Sciences and Disorders (CSD) (also listed as a separate school)  [学院/系]
│   └── Nutrition / Dietetics / Exercise Science concentrations       [系]
├── College of Professional and Liberal Studies (CPLS)                [学院] — https://www.memphis.edu/cpls/index.php
│   └── (Many BPS concentrations; one administrative home)            [系]
├── Fogelman College of Business and Economics (FCBE)                 [学院] — https://www.memphis.edu/fcbe/index.php
│   ├── Crews School of Accountancy                                   [系]
│   ├── Economics                                                     [系]
│   ├── Finance, Insurance and Real Estate                             [系]
│   ├── Management                                                    [系]
│   ├── Management Information Systems                                [系]
│   ├── Marketing                                                     [系]
│   └── Supply Chain Management                                       [系]
├── Herff College of Engineering                                      [学院] — https://www.memphis.edu/herff/index.php
│   ├── Biomedical Engineering                                        [系]
│   ├── Civil, Construction and Environmental Engineering              [系]
│   ├── Electrical and Computer Engineering                           [系]
│   ├── Engineering Technology                                        [系]
│   └── Mechanical Engineering                                        [系]
├── Kemmons Wilson School of Hospitality and Resort Management        [学院] — https://www.memphis.edu/healthsciences/wilson-1/index.php
│   ├── Hospitality and Resort Management                             [系]
│   └── Sport and Entertainment Management                            [系]
├── Loewenberg College of Nursing (LCON)                              [学院] — https://www.memphis.edu/nursing/index.php
│   └── Nursing                                                       [系]
├── School of Communication Sciences and Disorders (CSD)               [学院] — https://www.memphis.edu/csd/index.php
├── School of Public Health                                           [学院] — https://www.memphis.edu/publichealth/
│   ├── Health Administration                                         [系]
│   └── (additional divisions for Epidemiology, Biostatistics, etc.)  [系]
├── Helen Hardin Honors College                                       [学院] — https://www.memphis.edu/honors/index.php
├── Graduate School                                                    [学院] — https://www.memphis.edu/gradschool/
└── Cecil C. Humphreys School of Law                                  [学院] — https://www.memphis.edu/law/index.php
    └── (JD, LLM, SJD programs; ABA-accredited)
```

Notes:
- The College of Communication and Fine Arts (CCFA) and the College of Health and Human Sciences both contain academic departments; some units (e.g. Kemmons Wilson School) are administered through Health Sciences' organizational structure.
- "Interdisciplinary Programs" (in CAS) is a distinct department-level unit; it hosts African & African American Studies, International Studies, Judaic Studies, Religious Studies, Women's & Gender Studies, and others as **majors or minors**.
- Herff College of Engineering and School of Communication Sciences and Disorders each list an independent "School" rank despite containing a small number of departments.

Source: https://www.memphis.edu/academics/colleges-schools.php; captured 2026-07-07.

### 0.3 学历级别明细

| 学位缩写 (canonical) | 全称 | 层级 | 本校 official | 本项目数量 |
|---------|------|------|-----------|------------|
| BA | Bachelor of Arts | 本科 | BA | N/A — UofM 表只标 "X" 列，不细分 BA/BS |
| BS | Bachelor of Science | 本科 | BS | N/A |
| BFA | Bachelor of Fine Arts | 本科 | BFA | N/A |
| BPS | Bachelor of Professional Studies | 本科 | BPS | 1 (Alcohol & Drug Abuse Services) |
| MA | Master of Arts | 研究生 | MA | 15 (in Grad main table) |
| MS | Master of Science | 研究生 | MS | 25 |
| MFA | Master of Fine Arts | 研究生 | MFA | 3 (Art & Design, Creative Writing, Theatre) |
| MBA | Master of Business Administration | 研究生 | MBA / EMBA | 1 (MBA) + 1 (EMBA = EMBA in master's table) |
| MSW | Master of Social Work | 研究生 | MSW | 1 |
| MPH | Master of Public Health | 研究生 | MPH | 1 |
| MHA | Master of Health Administration | 研究生 | MHA | 1 (+ EMHA = EMHA in master's table) |
| MPA | Master of Public Administration | 研究生 | MPA | 1 |
| MPS | Master of Professional Studies | 研究生 | MPS | 1 |
| MALS | Master of Arts in Liberal Studies | 研究生 | MALS | 1 |
| MArch | Master of Architecture | 研究生 | MArch | 1 |
| MCRP | Master of City & Regional Planning | 研究生 | MCRP | 1 |
| MNM | Master of Nonprofit Management | 研究生 | MNM | 1 |
| MAT | Master of Arts in Teaching | 研究生 | MAT | 1 |
| MMu | Master of Music | 研究生 | MMu | 1 |
| MSN | Master of Science in Nursing | 研究生 | MSN | 1 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 24 |
| EdD | Doctor of Education | 研究生 | EdD | 3 |
| EdS | Education Specialist | 研究生 | EdS | 2 (Education; School Psychology) |
| DPT | Doctor of Physical Therapy | 研究生 | DPT | 2 (Physical Therapy in two listings) |
| AuD | Doctor of Audiology | 研究生 | AuD | 1 |
| DMA | Doctor of Musical Arts | 研究生 | DMA | 1 |
| DSW | Doctor of Social Work | 研究生 | DSW | 1 |
| DLS | Doctor of Liberal Studies | 研究生 | DLS | 1 |
| Adv Cert | Graduate Certificate | 研究生 | Graduate Certificate | 70 |
| JD | Juris Doctor | 专业 | JD | (Cecil C. Humphreys; separately accredited) |
| **合计** | — | — | — | **66 unique grad majors + 70 certificates + 52 UG majors** |

> Note: UofM's UG programs in the official table do **not** distinguish BA vs BS vs BFA — they list program name + a single "Major" column. Departments determine the BA/BS designation in the catalog; at the directory level this collapsed into 52 majors. **Rule-3 BA/BS/BFA counts are N/A** (granularity not published in the source table).

### 0.4 分布矩阵 (学院 × canonical 学位级别)

Rows = Schools. Columns = canonical degree codes (BS / BA / MS / MA / PhD / etc.). Cells = count of program-major-degree rows attributed to each school.

| 学院 \ canonical level | BS | BA | BFA | BPS | MS | MA | MFA | MS-Mx (MBA/MPH/MSW/MHA/MPA/MPS/MALS/MArch/MCRP/MNM/MAT/MMu/MSN) | PhD | EdD/EdS | DPT/AuD/DMA/DSW/DLS | Adv Cert | 合计 |
|------------|----|----|-----|-----|----|----|-----|-----|------|--------|---------------------|----|------|
| College of Arts and Sciences | * | * | — | — | — | — | — | — | — | — | — | see dept | **see dept** |
| College of Communication & Fine Arts | * | * | * | — | — | — | 3 (Art, Creative Writing, Theatre) | — | — | — | — | 1 (Art) | 3+ major |
| College of Education | — | — | — | — | 5 | — | — | — | 2 | 3 (EdD) + 2 (EdS) | — | 22+ (Autism, Educational Leadership, Special Education, etc.) | 12+ certs |
| College of Health & Human Sciences | * | * | — | 1 (Alcohol/Drug) | — | — | — | 1 (MS in Health Studies) | — | — | 2 (DPT) | 7+ | n/a |
| College of Professional & Liberal Studies | — | — | — | many | — | — | — | 1 (MALS) + 1 (DLS) | — | — | — | — | — |
| Fogelman College of Business & Economics | * | * | — | — | 2 (Accounting, Finance*) | — | — | 1 (MBA) + 1 (EMBA) | 1 (PhD* Business) | — | — | 6+ (Business Information Assurance, Cyber Security, etc.) | 10+ |
| Herff College of Engineering | * | * | — | — | 7+ (Biomed, Civil, ECE, Eng. Mgmt, Eng Tech, Mech, CS-applied stats) | — | — | — | 1 (Engineering PhD) | — | — | 4 (Cybersecurity, Imaging, Intelligence Engineering, Modern Energy & Power) | 12+ |
| Kemmons Wilson School | * | * | — | — | 1 (Sport & Hospitality Mgmt) | — | — | — | — | — | — | — | 1 |
| Loewenberg College of Nursing | * | * | — | — | — | — | — | 1 (MSN) | 1 (Nursing PhD) | — | — | 6 (Family Nurse Practitioner, Nursing Adult Gerontology Acute Care, Nursing Education, Nursing Leadership, Population Health, etc.) | 3 |
| School of CSD | — | — | — | — | — | — | — | 1 (Speech-Lang Pathology MA) | 1 (Comm Sci & Dis PhD) | — | 1 (AuD) | 2 (AAC, Augmentative & Alternative Comm) | 5 |
| School of Public Health | * | * | — | — | 1 (Biostatistics) | — | — | 1 (MPH) | 2 (Epi/Biostatistics, Health Sys & Policy) | — | — | 5 (Health Analytics, Health Communication, Health Systems Leadership, Population Health, Population Health Informatics) | 5+ |
| Graduate School (cross-college PhDs/Edu) | — | — | — | — | — | — | — | — | (counted above) | — | — | — | — |
| Cecil C. Humphreys School of Law | — | — | — | — | — | — | — | (LLM) | — | — | — | — | — |
| **合计 (UG Major count)** | **52 (collapsed: BA/BS/BFA not distinguished at directory level)** | | | | **25** | **15** | **3** | **11 (one-per-category Masters)** | **24** | **5** | **4 (DPT×2 + AuD + DMA/DSW/DLS spread)** | **70** | — |

> Reconciliation:
> - **UG majors** (52 unique): rows where Major column == "X" in `/academics/ugmajors.php`.
> - **Grad degrees** (counted rows in main grad table = 92, unique majors = 66): broken out as 24 PhD + 25 MS + 15 MA + 3 MFA + 5 (EdS) + 3 (EdD) + 2 (DPT) + 1 (AuD) + 1 (DMA) + 1 (DSW) + 1 (DLS) + 1 (MArch) + 1 (MCRP) + 1 (MHA) + 1 (EMHA) + 1 (MBA) + 1 (EMBA) + 1 (MAT) + 1 (MMu) + 1 (MSN) + 1 (MPA) + 1 (MPH) + 1 (MNM) + 1 (MPS) + 1 (MALS). Note: 25 MS includes an additional MS variant row "Finance*" (treated as MS).
> - **70 graduate certificates** are separate from the 66 graduate majors.
> - **52 UG + 66 unique grad + 70 cert** = **188** anchored programs. Cited from: https://www.memphis.edu/gradschool/programs/index.php and https://www.memphis.edu/gradschool/programs/graduatecertificates.php.

---

## 1. Undergraduate education

### 1.1 College/school architecture

UofM confers undergraduate majors ("X" in the Major column) in 12 of its 13 academic units — every college except the standalone Graduate School awards UG degrees. The Cecil C. Humphreys School of Law does **not** award UG majors (it offers JD, LLM, SJD). UG architecture mirrors the 13 schools listed in Section 0.2; see hierarchy tree above.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

Source URL (single source for entire Section 1.2): https://www.memphis.edu/academics/ugmajors.php
Each table heading denotes the department listed in that table's "Department" column. The "official official degree code" is N/A at the directory level — UofM's table collapses BA/BS/BFA/BPS into a single "Major" marker, so all degrees here are catalogued under one UG bucket labeled **UG (BA/BS/BFA/BPS)** in canonical terms.

#### College of Arts and Sciences (CAS) — https://www.memphis.edu/cas/index.php

##### Department of Anthropology
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Anthropology | Major + Minor |

##### Department of Biological Sciences
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Biology | Major + Minor |

##### Department of Chemistry
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Chemistry | Major + Minor |
| 2 | Biochemistry | Concentration under Chemistry |

##### Department of Computer Science
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Computer Science | Major + Minor |

##### Department of Criminology and Criminal Justice
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Criminology & Criminal Justice | Major + Minor |

##### Department of Earth Sciences
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Earth Sciences | Major + Minor |
| 2 | Geoarchaeology | Concentration |
| 3 | Geography | Concentration |
| 4 | Geology | Concentration |

##### Department of English
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | English | Major + Minor |
| 2 | African American Literature | Concentration |
| 3 | Creative Writing | Concentration |
| 4 | English as a Second Language | Concentration |
| 5 | Language and Linguistics | Concentration |
| 6 | Literature | Concentration |
| 7 | Professional Writing | Concentration |

##### Department of History
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | History | Major + Minor |

##### Department of Interdisciplinary Programs
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | African & African American Studies | Major + Minor |
| 2 | International Studies | Major + Minor |
| 3 | Area Studies (International Studies) | Concentration |
| 4 | Global Processes (International Studies) | Concentration |
| 5 | Judaic Studies | Concentration |
| 6 | Environmental Studies | Minor |
| 7 | Emergency Management | Minor |
| 8 | Legal Thought and Liberal Arts | Minor |
| 9 | Religious Studies | Minor |
| 10 | Women's and Gender Studies | Minor |

##### Department of Mathematical Sciences
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Mathematical Sciences | Major + Minor |
| 2 | Mathematics | Concentration |
| 3 | Statistics | Concentration |

##### Department of Philosophy
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Philosophy | Major + Minor |

##### Department of Physics and Materials Science
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Physics | Major + Minor |
| 2 | Materials Science | Concentration |

##### Department of Political Science
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Political Science | Major + Minor |

##### Department of Psychology
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Psychology | Major + Minor |
| 2 | Behavioral Neuroscience | Concentration |
| 3 | Cognitive Science | Concentration + Minor |

##### Department of Sociology
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Sociology | Major + Minor |

##### Department of World Languages and Literatures
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Foreign Languages | Major |
| 2 | Chinese | Concentration + Minor |
| 3 | French | Concentration + Minor |
| 4 | German | Concentration + Minor |
| 5 | Greek | Concentration + Minor |
| 6 | Italian | Concentration + Minor |
| 7 | Japanese | Concentration + Minor |
| 8 | Latin | Concentration + Minor |
| 9 | Portuguese | Concentration |
| 10 | Russian | Concentration + Minor |
| 11 | Spanish | Concentration + Minor |

##### School of Urban Affairs and Public Policy (SUAPP) / Public and Nonprofit Administration
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Nonprofit Management | Minor |
| 2 | Public Administration | Minor |

##### School of Social Work
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Social Work | Major + Minor |

##### ROTC Programs (CAS-administered)
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Air Force ROTC / Aerospace Studies | Minor only |
| 2 | Army ROTC / Military Science | Minor only |
| 3 | Navy ROTC / Naval Science | Minor only |

#### College of Communication and Fine Arts (CCFA) — https://www.memphis.edu/ccfa/index.php

##### Department of Architecture
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Architecture | Major |
| 2 | Interior Architecture | Major |

##### Department of Art and Design
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Fashion Design | Concentration + Minor |
| 2 | Fashion Merchandising | Concentration + Minor |
| 3 | Global Art Histories | Concentration + Minor |
| 4 | Graphic Design | Concentration + Minor |
| 5 | Photography | Concentration + Minor |
| 6 | Studio Arts | Concentration + Minor |
| 7 | Visual Arts | Concentration |

##### Department of Communication and Film
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Communication | Major + Concentration + Minor |
| 2 | Film and Video Production | Concentration |

##### Department of Journalism and Strategic Media
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Advertising | Major + Minor |
| 2 | Journalism | Major + Minor |
| 3 | Public Relations | Major + Minor |

##### Rudi E. Scheidt School of Music
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Music | Major + Minor |
| 2 | Music Industry | Major |
| 3 | Composition | Concentration |
| 4 | Jazz and Studio Composing/Arranging | Concentration |
| 5 | Jazz and Studio Performance | Concentration |
| 6 | Music Business | Concentration |
| 7 | Music Education (Instrumental and Choral) | Concentration |
| 8 | Music History | Concentration |
| 9 | Performance (Music) | Concentration |
| 10 | Recording Technology | Concentration |

##### Department of Theatre and Dance
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Theatre | Major + Minor |
| 2 | Design and Technical Production | Concentration |
| 3 | Musical Theatre | Concentration |
| 4 | Performance (Theatre) | Concentration |

##### College-level (ungrouped, CCFA Office)
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Dance | Concentration |
| 2 | Apparel and Accessory Merchandising | Concentration |
| 3 | Merchandising - Home Furnishings | Concentration |

#### College of Education — https://www.memphis.edu/education/index.php

##### Department of Counseling, Educational Psychology and Research
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | (no UG majors listed) | — |

##### Department of Instruction and Curriculum Leadership
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Human Development and Learning | Major |
| 2 | Integrative Studies | Major |
| 3 | Teaching All Learners | Major |
| 4 | Society Services Non Licensure | Concentration |
| 5 | Middle Grades Licensure | Concentration |

##### Department of Leadership
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | (no UG majors listed) | — |

#### College of Health and Human Sciences — https://www.memphis.edu/healthsciences/index.php

##### Department of Health Sciences
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Physical Education Teacher Education | Major |
| 2 | Dietetics | Concentration |
| 3 | Exercise, Sport, and Movement Sciences | Concentration |
| 4 | Health Sciences | Concentration |
| 5 | Healthcare Leadership | Concentration |
| 6 | Sport Coaching | Concentration |
| 7 | Medical Assisting | Minor |
| 8 | Nutrition, Health & Wellness | Minor |

#### College of Professional and Liberal Studies (CPLS) — https://www.memphis.edu/cpls/index.php

##### CPLS Administrative (degree programs rooted in CPLS)
###### BPS specifically
| # | 专业 | Notes |
|---|------|------|
| 1 | Alcohol and Drug Abuse Services (BPS) | Concentration + Minor |

##### CPLS Concentrations (awarded under CPLS umbrella; counted as CPLS programs)
| # | 专业 | Notes |
|---|------|------|
| 2 | American Studies | Minor |
| 3 | Asian Studies & International Trade | Concentration |
| 4 | Child Development | Concentration + Minor |
| 5 | Child Life Specialist | Concentration |
| 6 | Community Action and Social Change | Minor |
| 7 | Disability Studies and Rehabilitation | Concentration |
| 8 | Early Care and Learning Administration | Concentration |
| 9 | Early Care and Learning | Concentration |
| 10 | Early Intervention Specialist | Concentration |
| 11 | Emergency Management | Concentration |
| 12 | Health Services | Concentration |
| 13 | Human Services | Concentration |
| 14 | Information Technology (TN eCampus / formerly RODP) | Concentration |
| 15 | International Organizational Leadership (TN eCampus / formerly RODP) | Concentration |
| 16 | Law Enforcement Administration | Concentration |
| 17 | Legal Studies | Minor |
| 18 | Manufacturing Technology Management | Concentration |
| 19 | Music & Entertainment (Lambuth Campus Only) | Concentration |
| 20 | Nonprofit Development and Administration | Concentration |
| 21 | Organizational Leadership | Concentration |
| 22 | Professional Studies | Major (BPS-track undergraduate completion) |
| 23 | Religion in Society | Minor |
| 24 | Religious Studies | Concentration |
| 25 | Technology Management Services | Concentration |
| 26 | Urban Studies | Concentration |
| 27 | Liberal Studies | Major |

#### Fogelman College of Business and Economics (FCBE) — https://www.memphis.edu/fcbe/index.php

##### Crews School of Accountancy
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Accounting | Major + Minor |

##### Department of Economics
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Business Economics | Major + Minor |
| 2 | Financial Economics | Concentration |

##### Department of Finance, Insurance and Real Estate
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Finance | Major |
| 2 | Banking and Financial Services | Minor |
| 3 | Business Finance | Minor |
| 4 | Financial Planning | Minor |
| 5 | Property Management | Minor |
| 6 | Real Estate | Concentration + Minor |
| 7 | Risk Management and Insurance | Minor |

##### Department of Management
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Management | Major + Minor |
| 2 | Human Resource Management | Major |
| 3 | Entrepreneurship | Concentration + Minor |

##### Department of Management Information Systems
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Management Information Systems | Major + Minor |
| 2 | Project Management | Minor |

##### Department of Marketing
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Marketing | Major + Minor |
| 2 | Professional Selling | Minor |
| 3 | Social Media Marketing | Minor |

##### Department of Supply Chain Management
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Supply Chain Management | Major + Minor |

##### FCBE College-level
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | International Business | Minor |
| 2 | Pre-Professional Business Administration | Minor |

#### Herff College of Engineering — https://www.memphis.edu/herff/index.php

##### Department of Biomedical Engineering
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Biomedical Engineering | Major |

##### Department of Civil, Construction and Environmental Engineering
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Civil Engineering | Major |
| 2 | Construction Engineering | Concentration |
| 3 | Environmental Engineering | Concentration |
| 4 | Geotechnical Engineering | Concentration |
| 5 | Structural Engineering | Concentration |
| 6 | Transportation Engineering | Concentration |

##### Department of Electrical and Computer Engineering
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Computer Engineering | Major + Concentration |
| 2 | Electrical Engineering | Major |
| 3 | Electrophysics | Concentration |
| 4 | Systems and Signals | Concentration |

##### Department of Engineering Technology
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Engineering Technology | Major + Minor |

##### Department of Mechanical Engineering
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Mechanical Engineering | Major |

#### Kemmons Wilson School of Hospitality and Resort Management — https://www.memphis.edu/healthsciences/wilson-1/index.php

##### Hospitality and Resort Management
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Hospitality and Resort Management | Major |

##### Sport and Entertainment Management
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Sport and Leisure Management | Major |

#### Loewenberg College of Nursing (LCON) — https://www.memphis.edu/nursing/index.php

##### Nursing
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Nursing (BSN track) | Major |

#### School of Communication Sciences and Disorders (CSD) — https://www.memphis.edu/csd/index.php

##### CSD Administrative
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | American Sign Language and Deaf Studies | Major + Minor |

#### School of Public Health — https://www.memphis.edu/publichealth/

##### Health Administration
###### UG (BA/BS/BPS)
| # | 专业 | Notes |
|---|------|------|
| 1 | Public Health | Major + Minor |

#### School of Architecture and Planning (note: cross-listed Architecture also lives in CCFA)
#### (No separate dept listing beyond CCFA Architecture; Health Sciences College-level umbrella hosts multiple service programs)

### 1.3 Interdisciplinary / cross-college undergraduate programs

| Program | Home unit | Co-listed in |
|---------|-----------|--------------|
| American Sign Language and Deaf Studies | School of CSD | standalone |
| Public Health (BS) | School of Public Health | undergraduate Health Admin. dept |
| Architecture / Interior Architecture | CCFA Architecture dept | (no co-list) |
| International Studies | CAS Interdisciplinary Programs | (no co-list) |
| African & African American Studies | CAS Interdisciplinary Programs | (no co-list) |
| Women's and Gender Studies | CAS Interdisciplinary Programs | (no co-list) |
| Religious Studies | CAS Interdisciplinary Programs OR CPLS | Two separate rows in the table (`Interdisciplinary Programs` and `College of Professional and Liberal Studies`) — same name, different administrative home |
| Legal Studies | CPLS (minor only) | (no co-list) |
| Communication (BA/BS; Film & Video Production concentration) | CCFA | standalone |
| Computer Engineering | Herff EECE | standalone |

### 1.4 Minors — complete list

78 minor-marked rows in the source table. Grouped by department source — since many departments host multiple minor rows, listing all 78 names here:

**Arts and Sciences:** Anthropology; African & African American Studies; Biology; Chemistry; Computer Science; Criminology & Criminal Justice; Earth Sciences; English; History; International Studies; Legal Thought and Liberal Arts; Mathematical Sciences; Philosophy; Physics; Political Science; Psychology; Cognitive Science; Sociology; Cognitive Science (minor-duplicate); Religious Studies (in Interdisciplinary Programs); Emergency Management (in Interdisciplinary Programs); Environmental Studies (in Interdisciplinary Programs); Women's & Gender Studies (in Interdisciplinary Programs); Chinese; French; German; Greek; Italian; Japanese; Latin; Russian; Spanish.
**Communication and Fine Arts:** Advertising (JRSM); Communication (Communication); Fashion Design; Fashion Merchandising; Global Art Histories; Graphic Design; Journalism (JRSM); Photography; Public Relations (JRSM); Studio Arts; Theatre; Music (Music).
**Education:** (see CPLS for Education-managed minors; dept-level Education minors not separately listed in source)
**Health and Human Sciences:** Medical Assisting; Nutrition, Health & Wellness (Health Sciences).
**Professional and Liberal Studies:** Alcohol and Drug Abuse Services (BPS-track); American Studies; Child Development; Community Action and Social Change; Legal Studies; Religion in Society.
**Business (FCBE):** Accounting; Business Economics; Business Finance; Entrepreneurship; Financial Planning; International Business; Management; Management Information Systems; Marketing; Pre-Professional Business Administration; Project Management; Property Management; Real Estate; Risk Management and Insurance; Supply Chain Management; Professional Selling; Social Media Marketing.
**Engineering (Herff):** Engineering Technology.
**School of CSD:** American Sign Language and Deaf Studies.
**School of Public Health:** Public Health.
**ROTC:** Air Force ROTC; Army ROTC; Navy ROTC.

> The full minor list with 78 entries is captured verbatim in the source table; each is identifiable by Minor column == "X". Citation: https://www.memphis.edu/academics/ugmajors.php

### 1.5 General / Institute-wide requirements

UofM publishes its undergraduate catalog at https://catalog.memphis.edu/?catoid=39. The general-education (Foundations) requirements and graduation requirements (120 credit hours minimum) are detailed in the catalog. As of the 2024-2026 catalog, the catalog uses OmniUpdate/Catalog-Software platform. — Source URL: https://catalog.memphis.edu/?catoid=39 (verified 2026-07-07).

### 1.6 Course-ID → Major quick-lookup (does not apply)

UofM does not use a numerical Course-ID scheme (e.g. MIT's "Course 6"); instead it uses subject prefixes like ACCT (Accounting), BIOL (Biology), etc. Therefore no mapping table is produced.

---

## 2. Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Source: https://www.memphis.edu/gradschool/programs/index.php (master table); https://www.memphis.edu/gradschool/programs/masters.php; https://www.memphis.edu/gradschool/programs/doctoral.php. 66 unique grad majors × 24 degree types = 81 anchored major-degree combinations captured.

#### College of Arts and Sciences (CAS)

##### Department of Anthropology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.memphis.edu/anthropology/index.php |

##### Department of Earth Sciences
###### MS / MA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth Sciences (Archaeology, Geology, Geophysics, Interdisciplinary Studies) | MS | https://www.memphis.edu/earthsciences/index.php |
| 2 | Earth Sciences | MA | https://www.memphis.edu/earthsciences/index.php |
| 3 | Earth Sciences | PhD | https://www.memphis.edu/earthsciences/index.php |

##### Department of English
###### MA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | English (Composition Studies, ESL, Language & Linguistics, Literature, Technical Communications) | MA | https://www.memphis.edu/english/index.php |
| 2 | English (Applied Linguistics; Literary & Cultural Studies; Writing, Rhetoric, and Technical Communication) | PhD | https://www.memphis.edu/english/index.php |

##### Department of History
###### MA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | History (Ancient Egyptian History) | MA | https://www.memphis.edu/history/index.php |
| 2 | History (Ancient Egyptian History) | PhD | https://www.memphis.edu/history/index.php |

##### Department of Mathematical Sciences
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematical Sciences (Applied Mathematics, Mathematics, Statistics, Teaching of Mathematics) | MS | https://www.memphis.edu/msci/index.php |
| 2 | Mathematical Sciences (Applied Statistics, Mathematics) | PhD | https://www.memphis.edu/msci/index.php |

##### Department of Philosophy
###### MA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | MA | https://www.memphis.edu/philosophy/index.php |
| 2 | Philosophy | PhD | https://www.memphis.edu/philosophy/index.php |

##### Department of Physics
###### MS / PhD (CAS-affiliated)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics (Computational Physics, General Physics, Materials Science) | MS | https://www.memphis.edu/physics/index.php |
| 2 | Applied Physics | PhD | https://www.memphis.edu/physics/index.php |

##### Department of Political Science
###### MA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | MA | https://www.memphis.edu/polisci/index.php |

##### Department of Psychology
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology (General Psychology) | MS | https://www.memphis.edu/psychology/index.php |
| 2 | Psychology (Clinical Psychology, Experimental Psychology, School Psychology) | PhD | https://www.memphis.edu/psychology/index.php |

##### Department of Sociology
###### MA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | MA | https://www.memphis.edu/sociology/index.php |

##### School of Social Work (CAS)
###### MSW / DSW
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work (Advanced Practice Across Systems) | MSW | https://www.memphis.edu/socialwork/index.php |
| 2 | Social Work | DSW | https://www.memphis.edu/socialwork/index.php |

#### College of Communication and Fine Arts (CCFA)

##### Department of Architecture
###### MArch
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | MArch | https://www.memphis.edu/architecture/index.php |

##### Department of Art and Design
###### MFA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art and Design (Ceramics, Graphic Design, Painting, Printmaking/Photography, Sculpture) | MFA | https://www.memphis.edu/artanddesign/index.php |

##### Department of Communication (and Film)
###### MA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication (Communication; Film & Video Production) | MA | https://www.memphis.edu/communication/index.php |
| 2 | Communication | PhD | https://www.memphis.edu/communication/index.php |

##### Department of Journalism and Strategic Media
###### MA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Journalism and Strategic Media | MA | https://www.memphis.edu/jrsm/index.php |

##### Rudi E. Scheidt School of Music
###### MMu / DMA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music (Composition, Conducting, Jazz & Studio Music, Music Education, Musicology, Orff-Schulwerk Pedagogy, Performance) | MMu | https://www.memphis.edu/music/index.php |
| 2 | Music (Composition, Conducting, Performance) | DMA | https://www.memphis.edu/music/index.php |
| 3 | Music (Music Education, Musicology) | PhD | https://www.memphis.edu/music/index.php |

##### Department of Theatre and Dance
###### MFA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Theatre (Directing; Theatre Design and Technical Production) | MFA | https://www.memphis.edu/theatre/index.php |

#### College of Education (CoEd)

##### Department of Counseling, Educational Psychology and Research
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Educational Psychology & Research (Educational Psychology; Educational Research) | MS | https://www.memphis.edu/cepr/index.php |
| 2 | Educational Psychology & Research | PhD | https://www.memphis.edu/cepr/index.php |
| 3 | Counseling Psychology | PhD | https://www.memphis.edu/cepr/index.php |

##### Department of Instruction and Curriculum Leadership
###### MAT / MS / EdD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Instruction & Curriculum Leadership (Early Childhood Education; Elementary Education; Secondary Education; Special Education) | MAT | https://www.memphis.edu/icl/index.php |
| 2 | Instruction & Curriculum Leadership (Early Childhood Education; Instruction & Curriculum; Instructional Design & Technology; Reading; Special Education) | MS | https://www.memphis.edu/icl/index.php |
| 3 | Instruction & Curriculum Leadership (Applied Behavioral Analysis; Early Childhood Education; Instruction & Curriculum; Instruction Design & Technology; Literacy; Special Education) | EdD | https://www.memphis.edu/icl/index.php |

##### Department of Leadership
###### EdD / EdS / MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Leadership & Policy Studies (Educational Leadership Policy Studies) | EdD | https://www.memphis.edu/lead/index.php |
| 2 | Leadership & Policy Studies (School Administration & Supervision; Student Affairs Administration) | MS | https://www.memphis.edu/lead/index.php |
| 3 | Higher & Adult Education (Adult Education; Higher Education) | EdD | https://www.memphis.edu/lead/index.php |
| 4 | Education | EdS | https://www.memphis.edu/lead/index.php |
| 5 | School Psychology | EdS | https://www.memphis.edu/lead/index.php |
| 6 | School Psychology | MA | https://www.memphis.edu/lead/index.php |
| 7 | Counselor Education and Supervision (Clinical Mental Health Counseling; Clinical Rehabilitation Counseling; Rehabilitation Counseling; School Counseling) | MS | https://www.memphis.edu/lead/index.php |
| 8 | Counselor Education and Supervision | PhD | https://www.memphis.edu/lead/index.php |
| 9 | Social & Behavioral Sciences | PhD | https://www.memphis.edu/lead/index.php |
| 10 | Urban Affairs (beginning fall 2021) | PhD | https://www.memphis.edu/padm/old-index.php |

#### College of Health and Human Sciences

##### Department of Health Sciences
###### MS / DPT
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Health Studies (Exercise Nutrition; Exercise, Sport & Movement Sciences; Lifestyle Medicine; Physical Education Teacher Education) | MS | https://www.memphis.edu/healthsciences/index.php |
| 2 | Physical Therapy | DPT | https://www.memphis.edu/healthsciences/index.php |

##### Communication Sciences and Disorders (School-level)
###### PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication Sciences & Disorders (Hearing Sciences & Disorders; Neuroscience; Speech Language Sciences & Disorders) | PhD | https://www.memphis.edu/csd/index.php |

##### Speech-Language Pathology (CSD)
###### MA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Speech-Language Pathology | MA | https://www.memphis.edu/csd/index.php |

##### Audiology (CSD)
###### AuD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Audiology | AuD | https://www.memphis.edu/csd/index.php |

#### College of Professional and Liberal Studies (CPLS)
Note: CPLS mainly hosts UG programs; its graduate offerings are limited.

##### Professional Studies
###### MPS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Professional Studies (Human Resources Leadership; Strategic Leadership; Training & Development) | MPS | https://www.memphis.edu/cpls/index.php |
| 2 | Liberal Studies (Interdisciplinary graduate program) | MALS | https://www.memphis.edu/cpls/index.php |
| 3 | Liberal Studies | DLS | https://www.memphis.edu/cpls/index.php |

#### Fogelman College of Business and Economics (FCBE)

##### Crews School of Accountancy
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting (Accounting; Data Analytics; Taxation) | MS | https://www.memphis.edu/accountancy/index.php |

##### Department of Economics
###### MA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Economics | MA | https://www.memphis.edu/economics/index.php |

##### Department of Finance, Insurance and Real Estate
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Finance* | MS | https://www.memphis.edu/finance/index.php |

##### FCBE Business Administration (cross-dept)
###### MBA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Administration (concentrations: Applied Economics Analytics; Business Economics; Business Information Assurance; Business Project Management; Data Analytics for Management; Data Analytics for Technology; Engineering Management; Executive; Finance; Healthcare Management; Supply Chain Management; Taxation) | MBA | https://www.memphis.edu/fcbe/index.php |
| 2 | Business Administration (concentrations: Accounting; Business Information and Technology; Economics; Finance; Management; Marketing) | PhD* | https://www.memphis.edu/fcbe/index.php |

#### Herff College of Engineering

##### Department of Biomedical Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | MS | https://www.memphis.edu/bme/ |
| 2 | Biomedical Engineering | PhD | https://www.memphis.edu/bme/ |

##### Department of Civil, Construction and Environmental Engineering
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering (Engineering Seismology; Environmental Engineering; Geotechnical Engineering; Structural Engineering; Transportation Engineering; Water Resources Engineering) | MS | https://www.memphis.edu/ce/index.php |

##### Department of Electrical and Computer Engineering
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical & Computer Engineering (Computer Engineering; Electrical Engineering) | MS | https://www.memphis.edu/eece/index.php |

##### Engineering (cross-dept)
###### PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Engineering (Civil Engineering; Computer Engineering; Electrical Engineering; Engineering Physics; Mechanical Engineering) | PhD | https://www.memphis.edu/herff/index.php |

##### Engineering Management / Engineering Technology
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Engineering Management (Transportation; Manufacturing) | MS | https://www.memphis.edu/herff/index.php |
| 2 | Engineering Technology (Computer Emphasis; Electronics Emphasis; Manufacturing Emphasis) | MS | https://www.memphis.edu/et/index.php |

##### Department of Mechanical Engineering
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mechanical Engineering (Design & Mechanical Systems; Energy Systems; Mechanical Systems; Power Systems) | MS | https://www.memphis.edu/me/index.php |

#### Kemmons Wilson School of Hospitality and Resort Management

##### Sport and Hospitality Management
###### MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Sport and Hospitality Management (Sport Commerce) | MS | https://www.memphis.edu/healthsciences/wilson-1/index.php |

#### Loewenberg College of Nursing (LCON)

##### Nursing
###### MSN / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing (Executive Leadership; Family Nurse Practitioner; Nursing Education) | MSN | https://www.memphis.edu/nursing/index.php |
| 2 | Nursing | PhD | https://www.memphis.edu/nursing/index.php |

#### School of Communication Sciences and Disorders (CSD)

##### (CSD also houses Communication Sciences & Disorders PhD — listed above under Health Sciences)
**Communication Sciences & Disorders**
- PhD (see Health Sciences section above for full department routing)

#### School of Public Health

##### Biostatistics / Public Health / Health Administration
###### MS / MHA / MPH / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics (Data Science) | MS | https://www.memphis.edu/publichealth/ |
| 2 | Health Administration | MHA | https://www.memphis.edu/publichealth/ |
| 3 | Public Health (Biostatistics; Environmental Health; Epidemiology; Health Systems and Policy; Social & Behavioral Health; Urban Health) | MPH | https://www.memphis.edu/publichealth/ |
| 4 | Epidemiology and Biostatistics (Epidemiology) | PhD | https://www.memphis.edu/publichealth/ |
| 5 | Epidemiology and Biostatistics (Biostatistics) | PhD | https://www.memphis.edu/publichealth/ |
| 6 | Health Systems & Policy | PhD | https://www.memphis.edu/publichealth/ |
| 7 | Executive MHA | EMHA | https://www.memphis.edu/publichealth/ |

#### Cecil C. Humphreys School of Law

##### Law (separately accredited)
###### JD / LLM / SJD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor | JD | https://www.memphis.edu/law/index.php |
| 2 | Master of Laws | LLM | https://www.memphis.edu/law/index.php |
| 3 | Doctor of Juridical Science | SJD | https://www.memphis.edu/law/index.php |

Source: https://www.memphis.edu/law/index.php (Law School's own admissions pages, separately accredited by the ABA).

### 2.2 At least one program's full deep-dive (worked example)

**Worked example: MBA — Fogelman College of Business and Economics**
- **Department / college**: Fogelman College of Business and Economics (FCBE)
- **Concentrations (12)**: Applied Economics Analytics; Business Economics; Business Information Assurance; Business Project Management; Data Analytics for Management; Data Analytics for Technology; Engineering Management; Executive; Finance; Healthcare Management; Supply Chain Management; Taxation
- **Program URL**: https://www.memphis.edu/fcbe/index.php and https://www.memphis.edu/fcbegrad/
- **Degree awarded**: Master of Business Administration (MBA); also EMBA (Executive MBA)
- **Application portal URL**: https://apply.memphis.edu/portal/graduate_application
- **Standard graduate application fee**: $35 (domestic) / $60 (international) — non-refundable
- **Test requirements**: GMAT strongly recommended; some concentrations waive GMAT for high-GPA applicants. Departments set higher minimum GPA than the Graduate School's 2.75 baseline. (Source: https://www.memphis.edu/gradschool/future_students/cost-aid.php and program-specific websites.)
- **Minimum GPA for admission**: 2.75 cumulative UG GPA at Graduate School level; FCBE may set higher.
- **English language requirements**: Per Graduate School's 6.5 IELTS / 80 TOEFL (pre-Jan 2026) / 4 TOEFL (post-Jan 2026) baseline.
- **Special application components**: résumé, two letters of recommendation, statement of purpose, transcripts from all post-secondary institutions.

### 2.3 Graduate admissions model

- **Mixed / decentralized model**: Centralized application portal (https://apply.memphis.edu/portal/graduate_application) but each college/department sets its own deadline, test, and supplemental requirements.
- **Common graduate application portal**: single online application hosted via CampusESP/Apply (apply.memphis.edu).
- **Graduate School Office**: https://www.memphis.edu/gradschool/
- **Office of Graduate Admissions**: https://www.memphis.edu/graduateadmissions/
- **Application fee**: $35 (domestic) / $60 (international) — non-refundable; applies for each graduate degree level. Re-enrollees for same level = no fee.
- **Source**: https://www.memphis.edu/gradschool/programs/ and https://www.memphis.edu/graduateadmissions/future/admission-requirements.php

**Graduate Certificate Programs (70 total)** — Source: https://www.memphis.edu/gradschool/programs/graduatecertificates.php — 4 courses per certificate:

> African American Literature; Applied Lean Leadership; Athletic Administration; Augmentative and Alternative Communication (AAC); Autism Studies; Bioinformatics; Business Information Assurance; Business Project Management; College and Career Counseling; Clinical Mental Health Counseling; Clinical Social Work; Cognitive Science; Communication Sciences and Disorders and Public Health; Cyber Security and Information Assurance; Data Analytics for Management; Data Analytics for Technology; Data Science; Disabilities Studies; Early Music; Entrepreneurial Media; Family Nurse Practitioner; Financial Analysis and Planning; Freight Transportation; General Business; Geographic Information Systems; Health Analytics; Health Communication; Health Systems Leadership; Higher Education Instruction; Human Computer Interaction; Imaging and Signal Processing (Electrical and Computer Engineering); K-12 Educational Technology; Interdisciplinary Qualitative Research; Intelligence Engineering and Applications; K-12 Educational Leadership; Liberal Studies; Literacy Leadership and Coaching; Local Government Management; Mathematics Education; Modern Energy and Power Systems; Multimedia Storytelling; Multi-Tier Systems of Support; Museum Studies; Music-Artist Diploma; Nursing Adult Gerontology Acute Care; Nursing Education; Nursing Leadership; Philanthropy and Nonprofit Leadership; Play Therapy; Population Health; Population Health Informatics; Professional Real Estate; Quantitative Methods; Qualitative Methods in Education Research; School Counseling; School Library Information Specialist; School Social Work; Social Media Analysis and Strategy; Secondary Education-Comprehensive; Special Education; Sport Nutrition and Dietary Supplementation; STEM (Science, Technology, Engineering, and Mathematics) Teacher Leadership; Strategic Leadership; Substance Use Disorders Interprofessional; Supply Chain Management; Teaching English to Speakers of Other Languages (TESOL); Teaching of Mathematics; Urban Education; Vocology; Women's and Gender Studies.

---

## 3. Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value |
|-----------|-------|
| Admissions site | https://www.memphis.edu/admissions/ |
| Application portal | https://apply.memphis.edu/portal/application or via common app/national clearinghouse |
| Standard UG application fee | **$25** (domestic); **$50** (international) — non-refundable (Source: https://www.memphis.edu/usbs/fees/) |
| **Early Action (EA) deadline** | None — UofM uses rolling admission with priority scholarship deadline of **December 1** |
| **Regular Decision / Priority** | Fall: July 1 / File completion August 1 (Domestic) |
| **Domestic UG Deadlines** | Fall app: July 1, file complete August 1; Spring app December 1, complete January 1; Summer app May 1, complete May 15 |
| **International UG Deadlines (currently in US)** | Fall: August 1 / August 1; Spring: December 1 / January 1; Summer: May 1 / June 1 |
| **International UG Deadlines (outside US, F1 visa)** | Fall: July 1 / July 15; Spring: November 1 / December 1; Summer: April 1 / May 1; "Application for summer admission is not recommended for students needing a visa." |
| **Priority scholarship deadline** | December 1 (academic year before enrollment) |
| **Decision notification** | Approximately 5-7 business days after file completion |
| **Enrollment confirmation** | (US standard — assume candidate's reply date by May 1 for Fall) |
| **Financial aid deadline** | FAFSA priority = institutional deadline of approximately March 1 (typical Tenessee public pattern); consult https://www.memphis.edu/financialaid/ |
| **SAT/ACT policy** | Required for UG first-time freshmen; valid only if completed within 5 calendar years of intended enrollment term; "self-reported" acceptable |
| **Superscore policy** | UofM uses highest subscore across ACT/SAT; both tests accepted |
| **Score-report method** | Self-reported on application; official score report required upon admission; High school code not required for self-reporting; institution ETS/ACT school code on file (institution code varies) |
| **Interview policy** | Not required (academic departments with portfolio/audition/interview requirements handled separately) |
| **Recommendation letters** | Not required for UG admission |
| **Portfolios / auditions** | Required for Architecture, Art, Music, Theatre (specific dept determines); see https://catalog.memphis.edu/?catoid=39 |
| **Transfer pathway** | https://www.memphis.edu/admissions/basics/transfer.php |

Source: https://www.memphis.edu/admissions/basics/deadlines.php; https://www.memphis.edu/admissions/basics/requirements.php; https://www.memphis.edu/admissions/basics/international.php; https://www.memphis.edu/usbs/fees/

### 3.2 Undergraduate English proficiency table (international applicants)

> UG international applicants who are not citizens of one of the approved English-speaking countries (Anguilla, Antigua and Barbuda, Australia, The Bahamas, Barbados, Belgium, Belize, Bermuda, Botswana, The British Virgin Islands, Burundi, Cameroon, Canada (except Quebec), Cayman Islands, Christmas Island, Cook Islands, Dominica, Fiji, Gambia, Ghana, Grenada, Guyana, Ireland, Jamaica, Jersey, Kenya, Lesotho, Liberia, Malawi, Malta, Marshall Islands, Mauritius, Micronesia (Federated States of), Montserrat, Namibia, New Zealand, Nigeria, Niue, Norfolk Island, Northern Mariana Islands, Palau, Papua New Guinea, Philippines, Pitcairn Islands, Rwanda, Saint Kitts and Nevis, Saint Lucia, Saint Vincent, Samoa, Seychelles, Sierra Leone, Singapore, Sint Maarten, Solomon Islands, South Africa, South Sudan, Sudan, Swaziland, Tanzania, Tonga, Trinidad and Tobago, Turks and Caicos Islands, Tuvalu, Uganda, United Kingdom, US Virgin Islands — Saint Thomas, Saint Croix, Saint John, Zambia, Zimbabwe) must submit English proficiency test scores.

Source: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php (Graduate table; UG references the same standard) and https://www.memphis.edu/admissions/basics/int-requirements.php (international applicants apply via the same exam waiver country list as graduates; explicit thresholds given in the graduate table).

UG-specific language minimums (cited from the graduate table per UofM policy shared with undergraduate international admissions):

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL (paper) | 550 | — |
| TOEFL (iBT before January 2026) | 80 | — |
| TOEFL (iBT January 2026 or later) | 4 | — |
| IELTS (Academic) | 6.5 overall | — |
| PTE (Pearson Test of English) | 59 | — |
| iTEP (academic-plus) | 3.9 | — |
| Duolingo English Test (DET) | 110 | — |
| Trinity ISE (CEFR C1) | 105 overall AND each skill 105 | — |
| Cambridge English Qualification | 175 | — |

Caveat: minimums are **Graduate School** minimums. Some programs (e.g. Nursing BSN, Communication Sciences) require higher scores; consult individual department websites. Source: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php

### 3.3 Graduate — global rules

- **Application model**: Decentralized. Central portal at https://apply.memphis.edu/portal/graduate_application; departments set additional requirements (recommendations, essays, portfolios, GRE, auditions).
- **Standard application fee**: $35 (domestic); $60 (international) — non-refundable, per degree level.
- **Application opens**: Candidates may apply for the next Fall term as early as ~12 months in advance (rolling).
- **Deadlines**: Vary by program; some programs admit for Fall only, others for Spring/Summer as well. Most programs have soft deadlines 6-8 weeks before the term begins; consult individual programs at https://catalog.memphis.edu/?catoid=40.
- **GRE/GMAT policy**: Department-dependent (program-specific). Most master's programs do not require GRE; MBA recommends GMAT. PhD programs typically require GRE. School of Law uses LSAT. School of Public Health MPH — varies by concentration.
- **English-language policy**: See Section 3.2 — same thresholds; TOEFL iBT 80 (pre-Jan 2026); new iBT scale (4+) Jan 2026 onward. UofM uses **institution code 1459** for ETS score reporting.
- **Minimum GPA**: 2.75 cumulative UG GPA for master's degree; 3.0 cumulative for doctoral. Departments may set higher.
- **Test scores expire**: 2 years after administration.
- **Re-enrollees** for same degree level not required to pay a new fee.

Source: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php and https://www.memphis.edu/gradschool/programs/index.php

---

## 4. Costs & financial aid

### 4.1 Undergraduate cost (2025-26 academic year, line-itemized)

Source PDFs (Official 2025-26 fee schedules published by USBS):
- Resident: https://www.memphis.edu/usbs/fees/2526fees/ug_resident.pdf
- Non-Resident: https://www.memphis.edu/usbs/fees/2526fees/ug_nonresident.pdf
- International: https://www.memphis.edu/usbs/fees/2526fees/ug_international.pdf
- Graduate: https://www.memphis.edu/usbs/fees/2526fees/gr_resident.pdf

**UG Resident (Tennessee):**

| Credit Hours | Tuition | University Service Fee | Total |
|--------------|---------|------------------------|-------|
| 1 | $389.00 | $80.00 | $469.00 |
| 6 | $2,334.00 | $480.00 | $2,814.00 |
| 12 (cap = $4,668 tuition) | $4,668.00 | $960.00 | $5,628.00 |
| 13+ | $4,668.00 (cap) | $960.00 | $5,628.00 (cap) |

> Tuition cap at 12 credit hours for Tennessee residents; per-hour rate above 12 = no additional tuition charge.

**UG Non-Resident (out-of-state):**

| Credit Hours | Tuition | University Service Fee | Total |
|--------------|---------|------------------------|-------|
| 1 | $585.00 | $80.00 | $665.00 |
| 12 | $7,020.00 | $960.00 | $7,980.00 |
| 18 | $10,530.00 | $960.00 | $11,490.00 |

> Non-residents have no per-hour cap — charged per credit hour.

**UG International:**

| Credit Hours | Tuition | University Service Fee | Total |
|--------------|---------|------------------------|-------|
| 1 | $781.00 | $80.00 | $861.00 |
| 12 | $9,372.00 | $960.00 | $10,332.00 |
| 18 | $14,058.00 | $960.00 | $15,018.00 |

> International rate; no per-hour cap. Border county residents (5 adjacent MS/AR counties) get same rate as Tennessee residents.

**Selected course-specific fees (2025-26):**

| Fee | Per | Source |
|-----|-----|--------|
| Applied Music (private lessons) | $200/term (half-hour) or $400/term (hour) | https://www.memphis.edu/usbs/fees/ |
| Music Recital | $50/course (Jr/Sr recitals) | https://www.memphis.edu/usbs/fees/ |
| Architecture & Interior Architecture | $60 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Fine Art (all ART/ARTH except ART 1030) | $60 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Herff College of Engineering (all Eng courses) | $75 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Fogelman College of Business & Economics (3xx+) | $50 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Kemmons Wilson School (HOSP) | $65 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Loewenberg College of Nursing | $40 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Teacher Education | $50 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Performing Arts (THEA/DANC; ex. 1030, 1151, 3200) | $20 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Communication Sciences and Disorders (AUSP grad) | $35 per credit/audit hour | https://www.memphis.edu/usbs/fees/ |
| Social Work (specific 4xxx/7xxx) | $30 per course | https://www.memphis.edu/usbs/fees/ |
| Journalism & Strategic Media | $25 per credit/audit hour (specific courses) | https://www.memphis.edu/usbs/fees/ |
| Geology Field Camp (ESCI 4622) | $1700 flat | https://www.memphis.edu/usbs/fees/ |
| Dietetic Internship | $1,672 in addition to tuition | https://www.memphis.edu/usbs/fees/ |
| International MBA Program | $3,000 in addition to registration fees | https://www.memphis.edu/usbs/fees/ |
| Executive MBA | $870 per course in addition to tuition + fees | https://www.memphis.edu/usbs/fees/ |
| Executive MSN | $835 in addition to tuition + fees | https://www.memphis.edu/usbs/fees/ |
| Materials: Biology (BIOL) | $20-$50 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Chemistry (CHEM) | $85 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Geography (ESCI) | $25 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Health Sciences (NUTR) | $65 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Law Library Fee (all LAW) | $30 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Nursing (NURS) | $30-$500 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Physics (PHYS) | $30 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Health Sciences (HLSC 3005) | $150 per course | https://www.memphis.edu/usbs/fees/ |
| Materials: Theatre (THEA) | $25-$200 per course | https://www.memphis.edu/usbs/fees/ |

**Other fees:**

| Fee | Amount | Description |
|-----|--------|-------------|
| UG Application Fee (Domestic) | $25 | One-time non-refundable |
| UG Application Fee (International) | $50 | One-time non-refundable |
| Graduate Application Fee (Domestic) | $35 | One-time non-refundable per degree level |
| Graduate Application Fee (International) | $60 | One-time non-refundable per degree level |
| Installment Payment Plan Enrollment | $50 | Enrollment fee |
| Installment Late Fee | $25 per missed payment (max $75/semester) | — |
| Returned Check Service Charge | $30 | — |
| Late Fee | $200 | First-day-of-classes balance |
| Campus (ID) Card Replacement | $10 | — |
| GradGuard Tuition Insurance | Varies | Optional tuition protection plan |

### 4.2 Undergraduate financial-aid policy

- **Tuition**: Tennessee residents $389/credit hour up to 12 credits (cap); non-residents $585/credit hour; international $781/credit hour.
- **Service fee**: $80/credit hour for everyone.
- **Memphis Promise**: A last-dollar scholarship that fills the gap between financial aid and tuition cost for Tennessee residents — covers tuition after federal/state aid is applied. Per https://www.memphis.edu/admissions/basics/value.php: "The Memphis Promise is a commitment to assist Tennessee residents with funding their college education at the University of Memphis by awarding a last-dollar scholarship to fill the gap between a student's financial aid and the cost of tuition."
- **Scholarships**: "700+ scholarships are awarded annually. Academic scholarships begin at 3.25 GPA and 22 ACT or SAT equivalent. Additional scholarships based on leadership and service." Source: https://www.memphis.edu/admissions/basics/value.php
- **Access Memphis**: Programs dedicated to helping students stay in school. >90% of full-time freshmen receive financial aid (per https://www.memphis.edu/admissions/basics/value.php).
- **Border county waiver**: 5 bordering counties get same tuition as Tennessee residents — see https://www.memphis.edu/admissions/basics/border.php.
- **Non-Resident waiver**: For non-resident UG students who attended a high school outside Tennessee or the border counties; offered "substantial tuition reduction compared to previous costs" — out-of-state students are charged the equivalent of in-state tuition rates on any credits over 12 in a given term. Source: https://www.memphis.edu/admissions/basics/value.php
- **Net price / median price paid**: N/A — university does not publish median price in their cost-of-attendance pages; institutional Common Data Set would need to be consulted.
- **Need-blind / need-aware**: Standard public US — not formally announced; consult https://www.memphis.edu/financialaid/
- **Pell-eligible students**: Tennessee residents with family adjusted gross income up to $75,000 may be eligible for Tennessee Promise / HOPE scholarship — N/A-specific numbers vary year to year.

### 4.3 Graduate cost & funding framework

**Graduate tuition 2025-26 per fee chart:**

| Credit Hours | Tuition (Resident) | Service Fee | Total |
|--------------|--------------------|-------------|-------|
| 1 | $583.00 | $95.00 | $678.00 |
| 10 | $5,830.00 | $950.00 | $6,780.00 |
| 11+ | $5,830.00 (cap for residents) | $950.00 | $6,780.00 (cap) |

> Tuition cap at 10 credit hours for graduate Tennessee residents; no cap for non-residents / international.

**Non-resident graduate:** $816/credit hour (TN eCampus Rxx) or similar schedule; consult https://www.memphis.edu/usbs/fees/ for full breakdown. Source: https://www.memphis.edu/usbs/fees/ (table 2: "Applies to any course with section 'Rxx'" — TN eCampus distance rates).

**Graduate funding types at UofM:**
- **Assistantships**: Graduate Assistantships (GA) — see https://www.memphis.edu/gradschool/current_students/ga.php
- **Graduate School scholarships**: see https://www.memphis.edu/gradschool/
- **Border County Waiver**: https://www.memphis.edu/graduateadmissions/future/border.php
- **Non-Resident Waiver**: https://www.memphis.edu/graduateadmissions/future/non_resident_waiver.php
- **Funding grad school overview**: https://www.memphis.edu/graduateadmissions/future/funding_grad_school.php
- **Residency Classification**: https://www.memphis.edu/graduateadmissions/future/residency_classification.php
- **Health insurance (mandatory for international)**: https://www.memphis.edu/graduateadmissions/future/graduate_student_health_insurance.php

> Stipend rate, RA/TA/fellowship amounts, full per-program cost-of-attendance PDFs were not captured in this run — flagged P0 follow-up at Section 6.

---

## 5. Evidence chain index

```yaml
E-U-001:
  field: undergraduate.majors_total_x_marks
  value: 52
  source_url: https://www.memphis.edu/academics/ugmajors.php
  source_snippet: "Biology ... X ... X" (Major column marked X)
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
  description: Count of rows in https://www.memphis.edu/academics/ugmajors.php where the "Major" column equals "X".

E-U-002:
  field: undergraduate.minors_total_x_marks
  value: 78
  source_url: https://www.memphis.edu/academics/ugmajors.php
  source_snippet: "Minor column with X marks across 78 rows"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.concentrations_total_x_marks
  value: 91
  source_url: https://www.memphis.edu/academics/ugmajors.php
  source_snippet: "Concentration column with X marks across 91 rows"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.application_fee_domestic
  value: "$25"
  source_url: https://www.memphis.edu/usbs/fees/
  source_snippet: "New Freshman and Transfer Undergraduate Students ... $25"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.application_fee_international
  value: "$50"
  source_url: https://www.memphis.edu/usbs/fees/
  source_snippet: "International Undergraduate Students ... $50"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.deadline_domestic_fall
  value: "July 1 (application) / August 1 (file completion)"
  source_url: https://www.memphis.edu/admissions/basics/deadlines.php
  source_snippet: "Domestic Applicants Fall July 1 August 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.deadline_international_f1_fall
  value: "July 1 (application) / July 15 (file completion)"
  source_url: https://www.memphis.edu/admissions/basics/deadlines.php
  source_snippet: "International Applicants Not in the US (first time F1 visa holders) Fall July 1 July 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.deadline_priority_scholarship
  value: "December 1"
  source_url: https://www.memphis.edu/admissions/basics/deadlines.php
  source_snippet: "The priority deadline for scholarship consideration is December 1 for admitted students"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.high_school_curriculum
  value: "English (4), Visual/Performing Arts (1), Mathematics (3), Natural/Physical Science (2), Social Studies (2), Foreign Language (2)"
  source_url: https://www.memphis.edu/admissions/basics/requirements.php
  source_snippet: "English (4 units); Mathematics (3 units: Algebra I, Geometry, and Algebra II at least); Natural and Physical Science (2 units) ... Foreign Language (2 units: of the same language)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.standardized_test_policy
  value: "ACT or SAT required; valid within 5 years"
  source_url: https://www.memphis.edu/admissions/basics/requirements.php
  source_snippet: "Standardized exam results are considered valid only if they were completed within 5 calendar years of the term for which a student plans to enroll"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee_domestic
  value: "$35"
  source_url: https://www.memphis.edu/usbs/fees/
  source_snippet: "Graduate Students ... $35"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.application_fee_international
  value: "$60"
  source_url: https://www.memphis.edu/usbs/fees/
  source_snippet: "International Graduate Students ... $60"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.min_gpa_master
  value: "2.75 cumulative"
  source_url: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php
  source_snippet: "2.75/4.0 cumulative GPA. Departments may set higher standards."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-004:
  field: graduate.min_gpa_doctoral
  value: "3.0 cumulative"
  source_url: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php
  source_snippet: "GPA: 3.0/4.0 cumulative GPA. Departments may set higher standards."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-005:
  field: graduate.english_proficiency_table
  value: |
    TOEFL iBT (pre-Jan 2026): 80; (post-Jan 2026): 4
    IELTS (Academic): 6.5
    PTE: 59
    iTEP: 3.9
    Duolingo: 110
    Trinity ISE (CEFR C1): 105 overall AND each skill 105
    Cambridge English: 175
  source_url: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php
  source_snippet: "TOEFL 80 on internet-based test taken before January 2026, 4 on internet-based test taken January 2026 or later"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.toefl_ets_code
  value: "1459"
  source_url: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php
  source_snippet: "Submit scores electronically through ETS; school code 1459"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-007:
  field: graduate.test_scores_expiry
  value: "2 years"
  source_url: https://www.memphis.edu/graduateadmissions/future/admission-requirements.php
  source_snippet: "Test scores expire after 2 years. Tests must be taken within two years prior to applying."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-008:
  field: graduate.programs_directory_count
  value: 92
  source_url: https://www.memphis.edu/gradschool/programs/index.php
  source_snippet: "Comprehensive List of Master's + Doctoral Majors ... rows: APPLIED ACADEMIC MAJORS, AREAS OF CONCENTRATION, DEGREES"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-009:
  field: graduate.certificates_count
  value: 70
  source_url: https://www.memphis.edu/gradschool/programs/graduatecertificates.php
  source_snippet: "Take the next step in your career. Earn a grad certificate in just four courses. ... comprehensive list of certificate programs are listed alphabetically below"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-001:
  field: costs.ug_resident_per_credit_1hr
  value: "$389 tuition + $80 service fee = $469 total"
  source_url: https://www.memphis.edu/usbs/fees/2526fees/ug_resident.pdf
  source_snippet: "1 389.00 80.00 469.00 ... 12 4,668.00 960.00 5,628.00 (cap)"
  capture_date: 2026-07-07
  evidence_type: official_pdf_chart

E-COST-002:
  field: costs.ug_nonresident_per_credit_1hr
  value: "$585 tuition + $80 service fee = $665 total"
  source_url: https://www.memphis.edu/usbs/fees/2526fees/ug_nonresident.pdf
  source_snippet: "1 585.00 80.00 665.00 ... 18 10,530.00 960.00 11,490.00"
  capture_date: 2026-07-07
  evidence_type: official_pdf_chart

E-COST-003:
  field: costs.ug_international_per_credit_1hr
  value: "$781 tuition + $80 service fee = $861 total"
  source_url: https://www.memphis.edu/usbs/fees/2526fees/ug_international.pdf
  source_snippet: "1 781.00 80.00 861.00 ... 18 14,058.00 960.00 15,018.00"
  capture_date: 2026-07-07
  evidence_type: official_pdf_chart

E-COST-004:
  field: costs.gr_resident_per_credit_1hr
  value: "$583 tuition + $95 service fee = $678 total"
  source_url: https://www.memphis.edu/usbs/fees/2526fees/gr_resident.pdf
  source_snippet: "1 583.00 95.00 678.00 ... 10 5,830.00 950.00 6,780.00 (cap)"
  capture_date: 2026-07-07
  evidence_type: official_pdf_chart

E-INST-001:
  field: institution.colleges_count
  value: 13
  source_url: https://www.memphis.edu/academics/colleges-schools.php
  source_snippet: "UofM College and School Directory: COLLEGE OF ARTS AND SCIENCES ... Cecil C. Humphreys School of Law"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-INST-002:
  field: institution.total_areas_of_study
  value: "230+ / 250+"
  source_url: https://www.memphis.edu/
  source_snippet: "230+ Areas of Study"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-LAW-001:
  field: law.school_url
  value: https://www.memphis.edu/law/index.php
  source_url: https://www.memphis.edu/law/index.php
  source_snippet: "Cecil C. Humphreys School of Law"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## 6. WeKnora import manifest

### Collection structure

```
memphis-knowledge-base-v2 (collection)
├── document: 00_institution_overview.md                    # Section 0
├── document: 01_undergraduate_majors.md                    # Section 1
├── document: 02_graduate_programs.md                       # Section 2
├── document: 03_application_requirements.md                # Section 3
├── document: 04_costs_and_aid.md                           # Section 4
├── document: 05_evidence_chain.md                          # Section 5
├── document: 10_college_arts_and_sciences.md (chunk)       # Programs chunked by 学院
├── document: 11_college_communication_fine_arts.md
├── document: 12_college_education.md
├── document: 13_college_health_human_sciences.md
├── document: 14_college_professional_liberal_studies.md
├── document: 15_fogelman_college_business_economics.md
├── document: 16_herff_college_engineering.md
├── document: 17_kemmons_wilson_school.md
├── document: 18_loewenberg_college_nursing.md
├── document: 19_school_communication_sciences_disorders.md
├── document: 20_school_public_health.md
├── document: 21_school_of_law.md
├── document: 22_graduate_certificates.md
└── document: 99_monitoring_watchlist.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "memphis-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|MS|MA|PhD|EdD|DPT|...>"
  level: undergraduate | graduate | professional | certificate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Per-program graduate deadlines (each dept has its own) | https://www.memphis.edu/graduateadmissions/international/timeframe.php; program pages at memphis.edu/college/X/graduate |
| **P0** | Cost of attendance (housing, dining, books, personal) for UG typical first-year student | Net Price Calculator at https://www.memphis.edu/usbs/fees/ |
| **P0** | Need-blind / need-aware policy + median price paid for UG/international | Common Data Set 2025-26 (off-campus archive) |
| **P0** | Graduate assistantship stipend rate ranges per unit | https://www.memphis.edu/gradschool/current_students/ga.php |
| **P1** | Law school admissions cycle / LSAT / credential assembly service | https://www.memphis.edu/law/admissions/ |
| **P1** | Tuition 2026-27 (next academic year; PDFs at /usbs/fees/2627fees/) — already linked but not extracted in this run | https://www.memphis.edu/usbs/fees/2627fees/ug_resident.pdf |
| **P1** | Course catalog (full text) for one or two flagship departments (Physics, Biology) | https://catalog.memphis.edu/?catoid=39 |
| **P1** | Per-program test requirements (e.g., some PhD programs require GRE, some waive) | https://catalog.memphis.edu/?catoid=40 (grad catalog entries) |
| **P2** | UofM Global (online) tuition differential | https://www.memphis.edu/uofmglobal/ |
| **P2** | Honors College specific admissions | https://www.memphis.edu/honors/ |
| **P2** | Dual Enrollment admissions — high school students | https://www.memphis.edu/dualenrollment/ |
| **P2** | Lambuth campus program list | https://www.memphis.edu/lambuth/index.php |
| **P2** | SACSCOC reaccreditation date / status | https://www.memphis.edu/about/accreditations.php |

---

## 7. Cross-school comparison framework

Side-by-side fields with University of Memphis baseline. Leave cells empty for cross-school anchors to fill in.

| Field | UofM (this run) | Stanford | MIT | Other… |
|-------|------------------|----------|-----|--------|
| Total UG majors | 52 | — | — | — |
| Total UG minors | 78 | — | — | — |
| Total grad majors | 66 | — | — | — |
| Total grad certificates | 70 | — | — | — |
| Total colleges | 13 | — | — | — |
| School of Law (separately ABA) | Yes (Cecil C. Humphreys) | — | — | — |
| T4 public / R1 Carnegie | R1 (Very High Research) | — | — | — |
| Total Areas of Study (marketing) | 230+ / 250+ | — | — | — |
| UG Resident tuition/credit hour (2025-26) | $389 (cap 12 hrs) | — | — | — |
| UG Service fee/credit hour | $80 | — | — | — |
| UG Resident tuition+fees 12 hrs | $5,628/semester | — | — | — |
| UG Non-Resident tuition/credit hour (2025-26) | $585 | — | — | — |
| UG International tuition/credit hour (2025-26) | $781 | — | — | — |
| Grad Resident tuition/credit hour (2025-26) | $583 (cap 10 hrs) | — | — | — |
| Grad Service fee/credit hour | $95 | — | — | — |
| UG application fee (domestic / international) | $25 / $50 | — | — | — |
| Grad application fee (domestic / international) | $35 / $60 | — | — | — |
| UG Fall priority deadline | July 1 (Domestic) | — | — | — |
| Priority scholarship deadline | December 1 | — | — | — |
| EA / ED for UG | None (rolling) | — | — | — |
| Min Grad GPA (master / doctoral) | 2.75 / 3.00 | — | — | — |
| TOEFL iBT min | 80 (pre-Jan 2026); 4 (post-Jan 2026) | — | — | — |
| IELTS min | 6.5 | — | — | — |
| Duolingo min | 110 | — | — | — |
| TOEFL ETS code | 1459 | — | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: www.memphis.edu, catalog.memphis.edu, law.memphis.edu, apply.memphis.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction; PDF parsing via pdfplumber for fee charts
> **Granularity**: school → department → degree-level → program
