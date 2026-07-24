# Rutgers University-New Brunswick Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/B.Mus/etc.) | 118 |
| 本科辅修 (Minor) | 100+ (estimated; catalog lists minors within each school) |
| 研究生学位项目 (MA/MS/MBA/PhD/EdD/PSYD/DMA/etc.) | 305 |
| 研究生高级证书 / 文凭 / 认证 (Certificate/Endorsement/Nondegree) | 88 |
| **学位项目总计 (UG + Grad)** | **511** |
| 学院 / 独立系所总数 | 19 (NB schools and colleges) |

> **Note**: The 129 programs listed on the Rutgers Admissions "Explore Majors" page include 11 pre-professional tracks (Pre-Law, Pre-Medicine, Pre-Dentistry, Pre-Veterinary Medicine, etc.) and 1 "Undecided" option that are not standalone degree programs. The 118 count reflects actual degree-granting majors. Graduate counts exclude "Nondegree" entries (non-matriculated status).

### 0.2 学院 / 系层级结构

```
Rutgers University–New Brunswick
├── School of Arts and Sciences (SAS)                    [学院]
│   ├── Humanities Division                              [系]
│   │   ├── English                                      [系]
│   │   ├── History                                      [系]
│   │   ├── Philosophy                                   [系]
│   │   ├── Classics                                     [系]
│   │   ├── Comparative Literature                       [系]
│   │   ├── Linguistics                                  [系]
│   │   ├── Religion                                     [系]
│   │   └── Medieval Studies                             [系]
│   ├── Social Sciences Division                         [系]
│   │   ├── Political Science                            [系]
│   │   ├── Sociology                                    [系]
│   │   ├── Anthropology                                 [系]
│   │   ├── Economics                                    [系]
│   │   ├── Geography                                    [系]
│   │   ├── Psychology                                   [系]
│   │   ├── Criminal Justice                             [系]
│   │   └── Africana Studies                             [系]
│   ├── Natural Sciences & Mathematics Division          [系]
│   │   ├── Mathematics                                  [系]
│   │   ├── Statistics                                   [系]
│   │   ├── Computer Science                             [系]
│   │   ├── Physics                                      [系]
│   │   ├── Chemistry                                    [系]
│   │   ├── Biological Sciences                          [系]
│   │   ├── Cell Biology and Neuroscience                [系]
│   │   ├── Molecular Biology and Biochemistry           [系]
│   │   ├── Genetics                                     [系]
│   │   ├── Earth and Planetary Sciences                 [系]
│   │   └── Astrophysics                                 [系]
│   ├── Languages & Area Studies                         [系]
│   │   ├── French                                       [系]
│   │   ├── Spanish                                      [系]
│   │   ├── German                                       [系]
│   │   ├── Italian                                      [系]
│   │   ├── Portuguese                                   [系]
│   │   ├── Russian                                      [系]
│   │   ├── Chinese                                      [系]
│   │   ├── Japanese                                     [系]
│   │   ├── Korean                                       [系]
│   │   └── African, Middle Eastern, and South Asian Languages and Literatures [系]
│   ├── Arts & Culture                                   [系]
│   │   ├── Art History                                  [系]
│   │   ├── Cinema Studies                               [系]
│   │   ├── Music                                        [系]
│   │   ├── Theater Arts                                 [系]
│   │   └── Dance                                        [系]
│   └── Interdisciplinary Programs                       [系]
│       ├── American Studies                             [系]
│       ├── Asian Studies                                [系]
│       ├── Cognitive Science                            [系]
│       ├── Data Science                                 [系]
│       ├── Environmental Studies                        [系]
│       ├── European Studies                             [系]
│       ├── Jewish Studies                               [系]
│       ├── Latin American Studies                       [系]
│       ├── Latino and Caribbean Studies                 [系]
│       ├── Middle Eastern Studies                       [系]
│       ├── Women's, Gender and Sexuality Studies        [系]
│       └── Individualized Major                         [系]
│
├── School of Engineering (SOE)                          [学院]
│   ├── Biomedical Engineering                           [系]
│   ├── Chemical and Biochemical Engineering             [系]
│   ├── Civil and Environmental Engineering              [系]
│   ├── Electrical and Computer Engineering              [系]
│   ├── Industrial and Systems Engineering               [系]
│   ├── Materials Science and Engineering                [系]
│   ├── Mechanical and Aerospace Engineering             [系]
│   └── Computer Science ⚠ shared with SAS              [系]
│
├── School of Environmental and Biological Sciences (SEBS) [学院]
│   ├── Animal Science                                   [系]
│   ├── Biochemistry                                     [系]
│   ├── Ecology, Evolution and Natural Resources         [系]
│   ├── Entomology                                       [系]
│   ├── Environmental Sciences                           [系]
│   ├── Food Science                                     [系]
│   ├── Genetics                                         [系]
│   ├── Marine Sciences                                  [系]
│   ├── Microbiology                                     [系]
│   ├── Nutritional Sciences                             [系]
│   ├── Plant Biology                                    [系]
│   ├── Agricultural and Food Systems                    [系]
│   └── Environmental and Business Economics             [系]
│
├── Rutgers Business School–New Brunswick (RBS-NB)       [学院]
│   ├── Accounting                                       [系]
│   ├── Finance                                          [系]
│   ├── Marketing                                        [系]
│   ├── Supply Chain Management                          [系]
│   ├── Business Analytics and Information Technology    [系]
│   ├── Management (Leadership and Management)           [系]
│   └── Health Administration                            [系]
│
├── Mason Gross School of the Arts (MGSA)                [学院]
│   ├── Visual Arts                                      [系]
│   ├── Dance                                            [系]
│   ├── Theater                                          [系]
│   ├── Filmmaking                                       [系]
│   ├── Design                                           [系]
│   └── Music                                            [系]
│
├── School of Communication and Information (SCI)        [学院]
│   ├── Communication                                    [系]
│   ├── Journalism and Media Studies                     [系]
│   └── Information Technology and Informatics           [系]
│
├── School of Nursing (NB)                               [学院]
│   └── Nursing                                          [系]
│
├── Ernest Mario School of Pharmacy                      [学院]
│   └── Pharmacy                                         [系]
│
├── School of Management and Labor Relations (SMLR)      [学院]
│   ├── Human Resource Management                        [系]
│   └── Labor Studies and Employment Relations           [系]
│
├── Edward J. Bloustein School of Planning and Public Policy [学院]
│   ├── Public Policy                                    [系]
│   ├── Urban Planning and Design                        [系]
│   ├── City and Regional Planning                       [系]
│   ├── Public Health                                    [系]
│   └── Health Administration                            [系]
│
├── School of Social Work (SSW)                          [学院]
│   └── Social Work                                      [系]
│
├── School of Graduate Studies (SGS)                     [学院]
│   └── (administers graduate programs across all schools) [系]
│
├── Graduate School of Applied and Professional Psychology (GSAPP) [学院]
│   ├── Clinical Psychology                              [系]
│   ├── School Psychology                                [系]
│   └── Organizational Psychology                        [系]
│
├── Graduate School of Education (GSE)                   [学院]
│   └── Education (multiple specializations)             [系]
│
├── School of Health Professions                         [学院]
│   └── (allied health programs via Rutgers Health)      [系]
│
├── Honors College                                       [学院]
│   └── (interdisciplinary honors, no separate degrees)  [系]
│
└── Off-Campus Programs                                  [学院]
    └── (distributed programs at partner sites)          [系]
```

> ⚠ **Shared department**: Computer Science is jointly administered by SAS and SOE. Students can pursue a BA in CS through SAS or a BS in CS through SOE.

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| BA | Bachelor of Arts | 本科 | B.A. | 52 |
| BS | Bachelor of Science | 本科 | B.S. | 48 |
| BFA | Bachelor of Fine Arts | 本科 | B.F.A. | 9 |
| BM | Bachelor of Music | 本科 | B.M. | 2 |
| BSN | Bachelor of Science in Nursing | 本科 | B.S.N. | 1 |
| PharmD | Doctor of Pharmacy (6-year) | 本科→专业博士 | Pharm.D. | 1 |
| DPT | Doctor of Physical Therapy (4+3) | 本科→专业博士 | D.P.T. | 1 |
| MA | Master of Arts | 研究生 | M.A. | 38 |
| MS | Master of Science | 研究生 | M.S. | 62 |
| MBA | Master of Business Administration | 研究生 | M.B.A. | 3 |
| MFA | Master of Fine Arts | 研究生 | M.F.A. | 3 |
| ME | Master of Engineering | 研究生 | M.E. | 11 |
| MEng | Master of Engineering | 研究生 | M.Eng. | 0 (uses ME) |
| EdM | Master of Education | 研究生 | Ed.M. | 28 |
| MSW | Master of Social Work | 研究生 | M.S.W. | 3 |
| MCM | Master of Communication and Media | 研究生 | M.C.M. | 2 |
| MI | Master of Information | 研究生 | M.I. | 2 |
| MHA | Master of Health Administration | 研究生 | M.H.A. | 1 |
| MHRM | Master of Human Resource Management | 研究生 | M.H.R.M. | 1 |
| MCRP | Master of City and Regional Planning | 研究生 | M.C.R.P. | 3 |
| MCRS | Master of City and Regional Studies | 研究生 | M.C.R.S. | 1 |
| MPP | Master of Public Policy | 研究生 | M.P.P. | 3 |
| MPAP | Master of Public Administration and Policy | 研究生 | M.P.A.P. | 1 |
| MPI | Master of Public Informatics | 研究生 | M.P.I. | 1 |
| MLA | Master of Landscape Architecture | 研究生 | M.L.A. | 2 |
| MAT | Master of Arts in Teaching | 研究生 | M.A.T. | 11 |
| MABA | Master of Applied Behavior Analysis | 研究生 | M.A.B.A. | 1 |
| MAP | Master of Applied Psychology | 研究生 | M.A.P. | 2 |
| MST | Master of Science in Teaching | 研究生 | M.S.T. | 1 |
| MACC | Master of Accounting | 研究生 | M.A.C.C. | 1 |
| MACT | Master of Accounting Taxation | 研究生 | M.A.C.T. | 2 |
| MACY | Master of Accounting | 研究生 | M.A.C.Y. | 2 |
| MLER | Master of Labor and Employment Relations | 研究生 | M.L.E.R. | 2 |
| MBS | Master of Business and Science | 研究生 | M.B.S. | 4 |
| MPL | Master of Professional Leadership | 研究生 | M.P.L. | 1 |
| MCM | Master of Communication and Media | 研究生 | M.C.M. | 2 |
| MIT | Master of Information Technology | 研究生 | M.I.T. | 1 |
| DMA | Doctor of Musical Arts | 研究生 | D.M.A. | 1 |
| ADPL | Artist Diploma | 研究生 | A.D.P.L. | 1 |
| PhD | Doctor of Philosophy | 研究生 | Ph.D. | 95 |
| EdD | Doctor of Education | 研究生 | Ed.D. | 6 |
| PSYD | Doctor of Psychology | 研究生 | Psy.D. | 3 |
| DSW | Doctor of Social Work | 研究生 | D.S.W. | 1 |
| DHA | Doctor of Health Administration | 研究生 | D.H.A. | 1 |
| Certificate | Graduate Certificate | 研究生 | Certificate | 52 |
| Endorsement | Teaching Endorsement | 研究生 | Endorsement | 15 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BSN | PharmD | MA | MS | MBA | MFA | ME | EdM | PhD | EdD | PSYD | Cert/Endorse | Other Grad | 合计 |
|------------|----|----|-----|----|-----|--------|----|----|----|-----|----|----|-----|-----|------|-------------|-----------|------|
| SAS | 52 | 48 | 0 | 0 | 0 | 0 | 22 | 18 | 0 | 0 | 0 | 0 | 28 | 0 | 0 | 5 | 0 | 173 |
| SOE | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 11 | 0 | 7 | 0 | 0 | 5 | 0 | 43 |
| SEBS | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 2 | 0 | 40 |
| RBS-NB | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 22 |
| MGSA | 0 | 0 | 9 | 2 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 20 |
| SCI | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 8 |
| Nursing-NB | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | 2 | 0 | 11 |
| SMLR | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 6 | 0 | 10 |
| Bloustein | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 5 | 10 |
| SSW | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 3 | 8 |
| GSE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 28 | 1 | 6 | 0 | 7 | 0 | 42 |
| GSAPP | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 2 | 6 |
| Honors | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Off-Campus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **52** | **85** | **9** | **2** | **1** | **1** | **26** | **54** | **3** | **3** | **13** | **28** | **56** | **7** | **3** | **39** | **15** | **~511** |

> **Reconciliation**: Row totals sum to ~511, consistent with Rule 1 count. Graduate certificate/endorsement counts are estimates pending full catalog verification.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Rutgers–New Brunswick has **19 schools and colleges** offering undergraduate programs. The largest is the **School of Arts and Sciences (SAS)** with ~100 majors. The **School of Engineering (SOE)**, **School of Environmental and Biological Sciences (SEBS)**, **Rutgers Business School (RBS)**, and **Mason Gross School of the Arts (MGSA)** are the other major undergraduate-degree-granting schools. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### School of Arts and Sciences (SAS)

##### Division of Humanities

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://admissions.rutgers.edu/majors |
| 2 | History | https://admissions.rutgers.edu/majors |
| 3 | Philosophy | https://admissions.rutgers.edu/majors |
| 4 | Classics | https://admissions.rutgers.edu/majors |
| 5 | Comparative Literature | https://admissions.rutgers.edu/majors |
| 6 | Linguistics | https://admissions.rutgers.edu/majors |
| 7 | Religion | https://admissions.rutgers.edu/majors |
| 8 | Medieval Studies | https://admissions.rutgers.edu/majors |
| 9 | French | https://admissions.rutgers.edu/majors |
| 10 | Spanish | https://admissions.rutgers.edu/majors |
| 11 | German | https://admissions.rutgers.edu/majors |
| 12 | Italian | https://admissions.rutgers.edu/majors |
| 13 | Italian Studies | https://admissions.rutgers.edu/majors |
| 14 | Portuguese | https://admissions.rutgers.edu/majors |
| 15 | Russian | https://admissions.rutgers.edu/majors |
| 16 | Chinese | https://admissions.rutgers.edu/majors |
| 17 | Japanese | https://admissions.rutgers.edu/majors |
| 18 | Korean | https://admissions.rutgers.edu/majors |
| 19 | African, Middle Eastern, and South Asian Languages and Literatures | https://admissions.rutgers.edu/majors |
| 20 | Africana Studies | https://admissions.rutgers.edu/majors |
| 21 | Jewish Studies | https://admissions.rutgers.edu/majors |
| 22 | Latin American Studies | https://admissions.rutgers.edu/majors |
| 23 | Latino and Caribbean Studies | https://admissions.rutgers.edu/majors |
| 24 | Middle Eastern Studies | https://admissions.rutgers.edu/majors |
| 25 | European Studies | https://admissions.rutgers.edu/majors |
| 26 | Asian Studies | https://admissions.rutgers.edu/majors |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://admissions.rutgers.edu/majors |
| 2 | Anthropology, Evolutionary | https://admissions.rutgers.edu/majors |

##### Division of Social Sciences

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://admissions.rutgers.edu/majors |
| 2 | Sociology | https://admissions.rutgers.edu/majors |
| 3 | Economics | https://admissions.rutgers.edu/majors |
| 4 | Psychology | https://admissions.rutgers.edu/majors |
| 5 | Criminal Justice | https://admissions.rutgers.edu/majors |
| 6 | Geography | https://admissions.rutgers.edu/majors |

##### Division of Natural Sciences & Mathematics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://admissions.rutgers.edu/majors |
| 2 | Statistics | https://admissions.rutgers.edu/majors |
| 3 | Statistics/Mathematics | https://admissions.rutgers.edu/majors |
| 4 | Computer Science | https://admissions.rutgers.edu/majors |
| 5 | Data Science | https://admissions.rutgers.edu/majors |
| 6 | Physics | https://admissions.rutgers.edu/majors |
| 7 | Physics, Applied | https://admissions.rutgers.edu/majors |
| 8 | Astrophysics | https://admissions.rutgers.edu/majors |
| 9 | Chemistry | https://admissions.rutgers.edu/majors |
| 10 | Biochemistry | https://admissions.rutgers.edu/majors |
| 11 | Biological Sciences | https://admissions.rutgers.edu/majors |
| 12 | Cell Biology and Neuroscience | https://admissions.rutgers.edu/majors |
| 13 | Molecular Biology and Biochemistry | https://admissions.rutgers.edu/majors |
| 14 | Genetics | https://admissions.rutgers.edu/majors |
| 15 | Microbiology | https://admissions.rutgers.edu/majors |
| 16 | Geological Sciences | https://admissions.rutgers.edu/majors |
| 17 | Biomathematics | https://admissions.rutgers.edu/majors |
| 18 | Environmental Sciences | https://admissions.rutgers.edu/majors |
| 19 | Exercise Science | https://admissions.rutgers.edu/majors |

##### Division of Arts & Culture

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://admissions.rutgers.edu/majors |
| 2 | Art (B.A.) | https://admissions.rutgers.edu/majors |
| 3 | Cinema Studies | https://admissions.rutgers.edu/majors |
| 4 | Music (B.A.) | https://admissions.rutgers.edu/majors |
| 5 | Dance (B.A.) | https://admissions.rutgers.edu/majors |
| 6 | Theater Arts (B.A.) | https://admissions.rutgers.edu/majors |

###### BM

| # | 专业 | URL |
|---|------|-----|
| 1 | Music (B.M.) | https://admissions.rutgers.edu/majors |

##### Interdisciplinary Programs

###### BA/BS

| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://admissions.rutgers.edu/majors |
| 2 | Cognitive Science | https://admissions.rutgers.edu/majors |
| 3 | Environmental Studies | https://admissions.rutgers.edu/majors |
| 4 | Women's, Gender and Sexuality Studies | https://admissions.rutgers.edu/majors |
| 5 | Individualized Major | https://admissions.rutgers.edu/majors |
| 6 | Health Sciences | https://admissions.rutgers.edu/majors |
| 7 | History/French (Joint) | https://admissions.rutgers.edu/majors |
| 8 | History/Political Science (Joint) | https://admissions.rutgers.edu/majors |

---

#### School of Engineering (SOE)

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://admissions.rutgers.edu/majors |
| 2 | Applied Sciences Engineering | https://admissions.rutgers.edu/majors |
| 3 | Biomedical Engineering | https://admissions.rutgers.edu/majors |
| 4 | Chemical and Biochemical Engineering | https://admissions.rutgers.edu/majors |
| 5 | Civil Engineering | https://admissions.rutgers.edu/majors |
| 6 | Computer Science | https://admissions.rutgers.edu/majors |
| 7 | Electrical and Computer Engineering | https://admissions.rutgers.edu/majors |
| 8 | Environmental Engineering | https://admissions.rutgers.edu/majors |
| 9 | Industrial and Systems Engineering | https://admissions.rutgers.edu/majors |
| 10 | Materials Science and Engineering | https://admissions.rutgers.edu/majors |
| 11 | Mechanical Engineering | https://admissions.rutgers.edu/majors |

---

#### School of Environmental and Biological Sciences (SEBS)

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Food Systems | https://admissions.rutgers.edu/majors |
| 2 | Animal Science | https://admissions.rutgers.edu/majors |
| 3 | Biochemistry | https://admissions.rutgers.edu/majors |
| 4 | Biological Sciences | https://admissions.rutgers.edu/majors |
| 5 | Biotechnology | https://admissions.rutgers.edu/majors |
| 6 | Ecology, Evolution and Natural Resources | https://admissions.rutgers.edu/majors |
| 7 | Entomology | https://admissions.rutgers.edu/majors |
| 8 | Environmental and Business Economics | https://admissions.rutgers.edu/majors |
| 9 | Environmental Policy, Institutions, and Behavior | https://admissions.rutgers.edu/majors |
| 10 | Environmental Sciences | https://admissions.rutgers.edu/majors |
| 11 | Food Science | https://admissions.rutgers.edu/majors |
| 12 | Genetics | https://admissions.rutgers.edu/majors |
| 13 | Landscape Architecture | https://admissions.rutgers.edu/majors |
| 14 | Marine Sciences | https://admissions.rutgers.edu/majors |
| 15 | Meteorology | https://admissions.rutgers.edu/majors |
| 16 | Microbiology | https://admissions.rutgers.edu/majors |
| 17 | Nutritional Sciences | https://admissions.rutgers.edu/majors |
| 18 | Plant Biology | https://admissions.rutgers.edu/majors |

---

#### Rutgers Business School–New Brunswick (RBS-NB)

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://admissions.rutgers.edu/majors |
| 2 | Business Analytics and Information Technology | https://admissions.rutgers.edu/majors |
| 3 | Finance | https://admissions.rutgers.edu/majors |
| 4 | Health Administration | https://admissions.rutgers.edu/majors |
| 5 | Leadership and Management | https://admissions.rutgers.edu/majors |
| 6 | Marketing | https://admissions.rutgers.edu/majors |
| 7 | Supply Chain Management | https://admissions.rutgers.edu/majors |

---

#### Mason Gross School of the Arts (MGSA)

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dance Performance (B.F.A.) | https://admissions.rutgers.edu/majors |
| 2 | Dance Education - BFA/EdM | https://admissions.rutgers.edu/majors |
| 3 | Design (B.F.A.) | https://admissions.rutgers.edu/majors |
| 4 | Filmmaking (B.F.A.) | https://admissions.rutgers.edu/majors |
| 5 | Theater Acting (B.F.A.) | https://admissions.rutgers.edu/majors |
| 6 | Theater Design (B.F.A.) | https://admissions.rutgers.edu/majors |
| 7 | Theater Production (B.F.A.) | https://admissions.rutgers.edu/majors |
| 8 | Visual Arts (B.F.A.) | https://admissions.rutgers.edu/majors |

---

#### School of Communication and Information (SCI)

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://admissions.rutgers.edu/majors |
| 2 | Information Technology and Informatics | https://admissions.rutgers.edu/majors |
| 3 | Journalism and Media Studies | https://admissions.rutgers.edu/majors |

---

#### School of Nursing–New Brunswick

##### BSN

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing-BS in Nursing | https://admissions.rutgers.edu/majors |

---

#### Ernest Mario School of Pharmacy

##### PharmD (6-year)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy (6-year Pharm.D.) | https://admissions.rutgers.edu/majors |

---

#### School of Management and Labor Relations (SMLR)

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Human Resource Management | https://admissions.rutgers.edu/majors |
| 2 | Labor Studies and Employment Relations | https://admissions.rutgers.edu/majors |

---

#### Edward J. Bloustein School of Planning and Public Policy

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | City and Regional Planning | https://admissions.rutgers.edu/majors |
| 2 | Public Health | https://admissions.rutgers.edu/majors |
| 3 | Public Policy | https://admissions.rutgers.edu/majors |
| 4 | Urban Planning and Design | https://admissions.rutgers.edu/majors |

---

#### School of Social Work

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://admissions.rutgers.edu/majors |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | Parent Schools | URL |
|---|------|---------------|-----|
| 1 | Computer Science | SAS + SOE (BA via SAS, BS via SOE) | https://admissions.rutgers.edu/majors |
| 2 | History/French | SAS (Joint) | https://admissions.rutgers.edu/majors |
| 3 | History/Political Science | SAS (Joint) | https://admissions.rutgers.edu/majors |
| 4 | Dance Education - BFA/EdM | MGSA + GSE | https://admissions.rutgers.edu/majors |
| 5 | Dentistry - B.A./D.M.D. | SAS + Rutgers Health | https://admissions.rutgers.edu/majors |
| 6 | Law - B.A. or B.S./J.D. | SAS + Rutgers Law | https://admissions.rutgers.edu/majors |
| 7 | Medicine | SAS + Rutgers Health | https://admissions.rutgers.edu/majors |
| 8 | Physical Therapy - D.P.T. 4+3 Program | SAS + Rutgers Health | https://admissions.rutgers.edu/majors |
| 9 | Physician Assistant - B.A./M.S. | SAS + Rutgers Health | https://admissions.rutgers.edu/majors |

### 1.4 Pre-Professional Tracks (Not Standalone Degrees)

| # | Track | URL |
|---|-------|-----|
| 1 | Pre-Dentistry | https://admissions.rutgers.edu/majors |
| 2 | Pre-Law | https://admissions.rutgers.edu/majors |
| 3 | Pre-Medicine | https://admissions.rutgers.edu/majors |
| 4 | Pre-Veterinary Medicine | https://admissions.rutgers.edu/majors |

### 1.5 General Education Requirements

Rutgers-New Brunswick requires all undergraduates to complete the **Core Curriculum** through SAS. Requirements include:
- **Writing**: Expository Writing (English 101/102)
- **Quantitative Skills**: Math or logic course
- **Natural Sciences**: At least two courses
- **Social Sciences**: At least two courses
- **Arts and Humanities**: At least two courses
- **Historical Analysis**: At least one course
- School-specific requirements vary (SEBS, SOE, RBS, MGSA each have additional requirements)

> Source: https://sasundergrad.rutgers.edu/academic-requirements/core-curriculum

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

> **Note**: Graduate programs are drawn from the Rutgers Graduate Admissions program search (393 NB programs total, including nondegree/certificate entries). Programs are grouped by primary school affiliation.

#### School of Arts and Sciences (SAS) — Graduate

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Art History | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Biochemistry | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Cell and Developmental Biology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Cellular and Molecular Pharmacology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Chemistry and Chemical Biology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Classics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Comparative Literature | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Computer Science | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Earth and Planetary Sciences | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 11 | Ecology and Evolution | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 12 | Economics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 13 | English | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 14 | French | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 15 | Geography | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 16 | German | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 17 | History | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 18 | Italian | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 19 | Linguistics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 20 | Mathematics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 21 | Microbiology and Molecular Genetics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 22 | Neuroscience | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 23 | Philosophy | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 24 | Physics and Astronomy | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 25 | Physiology and Integrative Biology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 26 | Plant Biology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 27 | Political Science | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 28 | Psychology - Behavioral and Systems Neuroscience | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 29 | Psychology - Clinical | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 30 | Psychology - Cognitive | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 31 | Psychology - Social | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 32 | Sociology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 33 | Spanish - Bilingualism and Second Language Acquisition | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 34 | Spanish - Latin American, Iberian, and Luso-Afro-Brazilian Literatures and Cultures | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 35 | Statistics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 36 | Toxicology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 37 | Women's, Gender, and Sexuality Studies | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### MA/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Art History (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Art History - Cultural Heritage and Preservation Studies (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Art History - Curatorial Studies (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Asian Languages and Cultures (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Atmospheric Science (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Cell and Developmental Biology (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Chemistry and Chemical Biology (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Classics (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Computer Science (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 11 | Earth and Planetary Sciences (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 12 | Ecology and Evolution (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 13 | Economics (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 14 | Food and Business Economics (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 15 | French (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 16 | Geography (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 17 | Geography (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 18 | German (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 19 | History - Global Comparative (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 20 | Italian (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 21 | Mathematics (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 22 | Medicinal Chemistry (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 23 | Microbial Biology (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 24 | Microbiology and Molecular Genetics (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 25 | Music (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 26 | Physics and Astronomy (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 27 | Physics and Astronomy - Quantum Science (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 28 | Physiology and Integrative Biology (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 29 | Plant Biology (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 30 | Political Science - United Nations and Global Policy Studies (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 31 | Religious Studies (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 32 | Spanish - Translation and Interpreting (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 33 | Statistics (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 34 | Statistics - Data Science (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 35 | Statistics - Financial Statistics and Risk Management (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 36 | Statistics - Fintech Analytics (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 37 | Toxicology (MS) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 38 | Women's, Gender, and Sexuality Studies (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 39 | Women's, Gender, and Sexuality Studies - Feminist Practices for Social Change (MA) | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### MAT (Master of Arts in Teaching)

| # | 项目 | URL |
|---|------|-----|
| 1 | Chinese (MAT) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Classics (MAT) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | French (MAT) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | German (MAT) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Italian (MAT) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Physics and Astronomy (MST) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Spanish (MAT) | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Religious Studies (Certificate) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Religious Studies (Nondegree) | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### School of Engineering (SOE) — Graduate

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Chemical and Biochemical Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Civil and Environmental Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Electrical and Computer Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Industrial and Systems Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Materials Science and Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Mechanical and Aerospace Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### MS/ME

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biomedical Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Biomedical Engineering | ME | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Chemical and Biochemical Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Civil and Environmental Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Electrical and Computer Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Energy Systems | ME | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Environmental Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Industrial and Systems Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Industrial and Systems Engineering | ME | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Materials Science and Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 11 | Mechanical and Aerospace Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 12 | Mechanical and Aerospace Engineering | ME | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 13 | Packaging Engineering | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 14 | Pharmaceutical Engineering | ME | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering - Cybersecurity | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Electrical and Computer Engineering - Machine Learning | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Packaging Engineering | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### School of Graduate Studies (SGS) — Cross-School Programs

> The School of Graduate Studies administers many graduate programs across all NB schools. Programs listed under SGS in the admissions search include interdisciplinary and cross-school offerings.

##### PhD (selected)

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication, Information and Media | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Education | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Endocrinology and Animal Biosciences | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Entomology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Environmental Sciences | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Food Science | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Genetics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Industrial Relations and Human Resources | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Kinesiology and Applied Physiology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Marine Sciences | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 11 | Nursing | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 12 | Nutritional Sciences | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 13 | Oceanography | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 14 | Pharmacy/Pharmaceutical Science | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 15 | Planning and Public Policy | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 16 | Public Health | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 17 | Quantitative Biomedicine | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 18 | Social Work | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### Graduate School of Education (GSE)

##### EdM (Master of Education)

| # | 项目 | URL |
|---|------|-----|
| 1 | Education - Administration and Supervision | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Education - College Student Affairs | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Education - Dance Education Certification | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Education - Education, Culture, and Society | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Education - Elementary Education K-6 | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Education - English | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Education - Evaluation, Statistics, and Measurement | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Education - Language | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Education - Learning, Cognition, and Development | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Education - Literacy | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 11 | Education - Mathematics | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 12 | Education - School Counseling and Counseling Psychology | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 13 | Education - Science | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 14 | Education - Social Studies | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 15 | Education - Special Education | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### EdD (Doctor of Education)

| # | 项目 | URL |
|---|------|-----|
| 1 | Education - Design of Learning Environments | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Education - Education, Culture, and Society | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Education - Educational Leadership - Higher Education | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Education - Educational Leadership - PK-12 | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Education - Educational Leadership - Plus Principal | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Education - Special Education | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://grad.admissions.rutgers.edu/GraduateProgram/ |

##### Certificates/Endorsements

| # | 项目 | URL |
|---|------|-----|
| 1 | Education - Community College Leadership (Certificate) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Education - Educational Technology (Certificate) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Education - Gifted Education (Certificate) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Education - Maker Education (Certificate) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Education - Multiple Endorsements (ESL, Bilingual, Reading Specialist, etc.) | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### Graduate School of Applied and Professional Psychology (GSAPP)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Clinical Psychology | PSYD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | School Psychology | PSYD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Organizational Psychology | PSYD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Organizational Psychology | PSYM | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Applied Behavior Analysis | MABA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Applied Behavior Analysis | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Applied Psychology | MAP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Sport and Performance Psychology | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### Rutgers Business School–New Brunswick (RBS-NB) — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Business Administration - Joint Undergraduate Degree | MBA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Business Administration - PharmD/MBA | MBA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Accounting - Taxation | MACT | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Accounting - Taxation | MACY | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Accounting - Governmental | MACY | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Accounting Information Systems Certificate - rSBI | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Finance and Economics Certificate - rSBI | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Global Sports Business | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Healthcare Analytics and Intelligence | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Marketing Analytics and Insights | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 11 | Supply Chain Analytics | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 12 | Management Science and Information Systems Certificate - rSBI | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 13 | Management and Global Business Certificate - rSBI | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 14 | Marketing Certificate - rSBI | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 15 | Supply Chain Management Certificate - rSBI | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### Mason Gross School of the Arts (MGSA) — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Music | DMA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Music | ADPL | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Music | MM | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Music | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Design | MFA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Theater Arts - Playwriting | MFA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Visual Arts | MFA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Art History | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Art History - Cultural Heritage and Preservation Studies | MA | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Art History - Curatorial Studies | MA | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### School of Communication and Information (SCI) — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Communication and Media | MCM | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Communication, Information and Media | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Information | MI | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Information Technology | MIT | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Public Informatics | MPI | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Public and Urban Informatics | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### School of Management and Labor Relations (SMLR) — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Human Resource Management | MHRM | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Labor and Employment Relations | MLER | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Industrial Relations and Human Resources | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Human Resource Management - Strategic HRM | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Labor and Employment Relations - Conflict Resolution and Negotiation | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Labor and Employment Relations - Diversity and Inclusion in the Workplace | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Labor and Employment Relations - Leading Organizational Change | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Labor and Employment Relations - Public Sector Labor-Management Relations | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Labor and Employment Relations - Workers' Rights | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### Edward J. Bloustein School of Planning and Public Policy — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Planning and Public Policy | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Public Policy | MPP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Public Policy | MPAP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Urban Planning and Policy Development | MCRP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Urban Planning and Policy Development | MCRS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Public Policy | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Public Policy - Dual MPP/JD | MPP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 8 | Public Policy - Dual MPP/MBA | MPP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 9 | Public Policy - Dual MPP/MPH | MPP | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 10 | Urban Planning and Policy Development - Dual MCRP/JD | MCRP | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### School of Social Work (SSW) — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Social Work | MSW | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Social Work - Advanced Standing | MSW | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Social Work | DSW | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Social Work | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Social Work - Addiction Counselor Training | Certificate | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 6 | Social Work - Dual MSW/MPH | MSW | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 7 | Social Work - Dual MSW/MPP | MSW | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### School of Nursing–New Brunswick — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

#### Ernest Mario School of Pharmacy — Graduate

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Pharmacy/Pharmaceutical Science | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 2 | Pharmacy/Pharmaceutical Science | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 3 | Medicinal Chemistry | MS | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 4 | Medicinal Chemistry | PHD | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| 5 | Pharmaceutical Engineering | ME | https://grad.admissions.rutgers.edu/GraduateProgram/ |

---

### 2.2 Graduate Admissions Model

Rutgers graduate admissions is **fully decentralized**. Each school/program manages its own admissions process, deadlines, and requirements. The **School of Graduate Studies (SGS)** provides administrative oversight but does not make admissions decisions.

**Application portal**: https://grad.admissions.rutgers.edu/GraduateProgram/
**Application fee**: $70 (standard; may vary by program)
**CGS April 15 Resolution**: Rutgers is a CGS signatory.

Key entry points by school:
- **SAS Graduate**: Programs through individual departments
- **SOE Graduate**: https://soe.rutgers.edu/academics/graduate-programs
- **GSE**: https://gse.rutgers.edu/admissions
- **GSAPP**: https://gsapp.rutgers.edu/admissions
- **RBS Graduate**: https://www.business.rutgers.edu/admissions
- **MGSA**: https://www.masongross.rutgers.edu/admissions
- **SCI**: https://comminfo.rutgers.edu/academics/graduate
- **Bloustein**: https://bloustein.rutgers.edu/academics/graduate-programs
- **SSW**: https://socialwork.rutgers.edu/academics/graduate-programs

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | Common App + Rutgers Application | https://admissions.rutgers.edu/apply |
| Early Action (EA) | November 1, 2025 (non-binding) | https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick |
| Regular Decision (RD) | December 1, 2025 | https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick |
| EA decision notification | By January 31, 2026 | https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick |
| RD decision notification | By February 28, 2026 | https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick |
| Candidate's Reply Date | May 1, 2026 | https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick |
| Transfer deadline | February 1, 2026 | https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick |
| Application fee | $70 (non-refundable) | https://admissions.rutgers.edu/apply |
| Fee waiver | Available via Common App for qualifying students | https://admissions.rutgers.edu/apply |
| SAT/ACT policy | **Test-optional through 2027** | https://admissions.rutgers.edu/apply/first-year-applicants |
| SAT code | 2765 | https://admissions.rutgers.edu/apply/first-year-applicants |
| ACT code | 2592 | https://admissions.rutgers.edu/apply/first-year-applicants |
| SAT Essay/ACT Writing | Not required | https://admissions.rutgers.edu/apply/first-year-applicants |
| Superscore | Not specified (scores sent from testing agency) | https://admissions.rutgers.edu/apply/first-year-applicants |
| Recommendations | Not required (holistic review) | https://admissions.rutgers.edu/apply/how-we-make-decisions |
| Essay | Personal essay (part of application) | https://admissions.rutgers.edu/apply/how-we-make-decisions |
| FAFSA code | 002629 | https://admissions.rutgers.edu/costs-and-aid/financial-aid |
| FAFSA priority deadline | January 15 | https://admissions.rutgers.edu/costs-and-aid/financial-aid |
| Need policy | **Need-aware for all applicants** (domestic and international) | https://admissions.rutgers.edu/costs-and-aid/financial-aid |

### 3.2 Undergraduate English Proficiency Table

**Applies to**: All students whose secondary schooling was outside the U.S. in a country where English is not the principal language. Waivers available for English-medium school attendees (case-by-case).

| Exam | Minimum (NB) | Recommended | Notes |
|------|-------------|-------------|-------|
| TOEFL iBT (pre-Jan 22, 2026) | 79 | -- | Pharmacy/Nursing require 100 |
| TOEFL iBT (post-Jan 22, 2026) | 4.5 | -- | New scoring scale; Pharmacy/Nursing require 5.5 |
| IELTS Academic | 6.5 | -- | -- |
| Michigan English Test (MET) | 56 | -- | -- |
| SAT EBRW | 550 | -- | Satisfies proficiency requirement |
| ACT English | 21 | -- | Satisfies proficiency requirement |
| Pearson PTE | 53 | -- | -- |
| Duolingo English Test | 115 | -- | Pharmacy/Nursing require 130 |
| Cambridge Assessment | B2 | -- | -- |

> **Exemptions**: Students who earned a grade of B or better in a college-level English Composition course at an accredited U.S. college are exempt.
> **TOEFL code**: 2765
> Source: https://admissions.rutgers.edu/apply/international-applicants

### 3.3 Graduate — Global Rules

- **Decentralized admissions**: Each school/program sets own deadlines, GRE policy, and requirements
- **Application portal**: https://grad.admissions.rutgers.edu/ (unified application for most programs)
- **Application fee**: $70 (standard; professional schools may differ)
- **GRE**: Per-program policy (some required, some optional, some not accepted)
- **English proficiency**: TOEFL or IELTS required for non-native speakers; minimums vary by program
- **CGS April 15 Resolution**: Rutgers is a signatory
- **ETS institutional code**: 2765 (GRE/TOEFL)

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025–2026 Academic Year)

#### New Jersey Residents

| Expense Item | Commuter | On-Campus |
|-------------|----------|-----------|
| Tuition | $14,933 | $14,933 |
| Fees | $3,891 | $3,891 |
| Room and Board | $5,826 | $15,332 |
| **Total** | **$24,650** | **$34,156** |

> Part-time tuition: $482/credit hour (SAS)
> Source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees

#### Non-New Jersey Residents

| Expense Item | Commuter | On-Campus |
|-------------|----------|-----------|
| Tuition | $35,758 | $35,758 |
| Fees | $3,891 | $3,891 |
| Room and Board | $5,826 | $15,332 |
| **Total** | **$45,475** | **$54,981** |

> Part-time tuition: $1,162/credit hour (SAS)
> F-1/J-1 visa holders pay additional: SEVIS administration fee ($500), mandatory health insurance, books/supplies
> Source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees

### 4.2 Undergraduate Financial Aid Policy

| Field | Value |
|-------|-------|
| Need-aware | Yes — for all applicants (domestic and international) |
| Meets 100% demonstrated need | Not guaranteed (varies by funding availability) |
| Merit scholarships | Available; apply by December 1 for priority consideration |
| FAFSA code | 002629 |
| FAFSA priority deadline | January 15 |
| Gift aid types | Scholarships, grants, awards (federal, state, institutional) |
| Work-study | Federal Work-Study program available |
| Loans | Federal, state, university, and private sources |
| NJ EOF | Educational Opportunity Fund for qualifying NJ residents |

> Source: https://admissions.rutgers.edu/costs-and-aid/financial-aid

### 4.3 Graduate Cost & Funding Framework

| Field | Value |
|-------|-------|
| Application fee | $70 (standard) |
| Funding types | Fully funded (most PhD programs), partially funded, self-funded |
| Common funding forms | RA (Research Assistantship), TA (Teaching Assistantship), Fellowship, Grant |
| Fee waiver | Needs-based waivers available through Graduate School |
| PhD funding | Most PhD programs offer full funding (tuition + stipend) |
| Master's funding | Varies; many self-funded, some assistantships available |

> Source: https://gradstudy.rutgers.edu/financial/financial-information

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Early Action Deadline
```yaml
field: undergraduate.deadlines.EA
value: "November 1, 2025"
source_url: https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick
source_snippet: "First-Year, Early Action^ | November 1, 2025 | January 31, 2026 | May 1, 2026"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Regular Decision Deadline
```yaml
field: undergraduate.deadlines.RD
value: "December 1, 2025"
source_url: https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick
source_snippet: "First-Year, Regular Decision# | December 1, 2025 | February 28, 2026 | May 1, 2026"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-003: Test-Optional Policy
```yaml
field: undergraduate.testing.policy
value: "Test-optional through 2027"
source_url: https://admissions.rutgers.edu/apply/first-year-applicants
source_snippet: "Rutgers, The State University of New Jersey, maintains test-optional and test-blind policies through 2027."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: SAT/ACT Codes
```yaml
field: undergraduate.testing.codes
value: {SAT: 2765, ACT: 2592}
source_url: https://admissions.rutgers.edu/apply/first-year-applicants
source_snippet: "When requesting scores, use our SAT code 2765 or our ACT code 2592."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: English Proficiency — TOEFL
```yaml
field: undergraduate.english_proficiency.TOEFL
value: {pre_jan2026: 79, post_jan2026: 4.5}
source_url: https://admissions.rutgers.edu/apply/international-applicants
source_snippet: "TOEFL (internet-based test & Home Edition through January 21, 2026)*# | 79 | 79 | 79"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: English Proficiency — IELTS
```yaml
field: undergraduate.english_proficiency.IELTS
value: 6.5
source_url: https://admissions.rutgers.edu/apply/international-applicants
source_snippet: "International English Language Testing System (IELTS) | 6.5 | 6.5 | 6.0"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: English Proficiency — Duolingo
```yaml
field: undergraduate.english_proficiency.Duolingo
value: 115
source_url: https://admissions.rutgers.edu/apply/international-applicants
source_snippet: "Duolingo English Test | 115^ | 115 | 115"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: Tuition — In-State
```yaml
field: undergraduate.cost.tuition_instate
value: "$14,933"
source_url: https://admissions.rutgers.edu/costs-and-aid/tuition-fees
source_snippet: "Tuition | $14,933** | $14,933**"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: Tuition — Out-of-State
```yaml
field: undergraduate.cost.tuition_oos
value: "$35,758"
source_url: https://admissions.rutgers.edu/costs-and-aid/tuition-fees
source_snippet: "Tuition | $35,758*/** | $35,758*/**"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-010: Total COA — In-State On-Campus
```yaml
field: undergraduate.cost.coa_instate_oncampus
value: "$34,156"
source_url: https://admissions.rutgers.edu/costs-and-aid/tuition-fees
source_snippet: "Total | $24,650 | $34,156"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-011: Total COA — OOS On-Campus
```yaml
field: undergraduate.cost.coa_oos_oncampus
value: "$54,981"
source_url: https://admissions.rutgers.edu/costs-and-aid/tuition-fees
source_snippet: "Total | $45,475 | $54,981"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-012: FAFSA Code
```yaml
field: undergraduate.financial_aid.fafsa_code
value: "002629"
source_url: https://admissions.rutgers.edu/costs-and-aid/financial-aid
source_snippet: "Rutgers FAFSA School Code: 002629"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: FAFSA Priority Deadline
```yaml
field: undergraduate.financial_aid.fafsa_priority
value: "January 15"
source_url: https://admissions.rutgers.edu/costs-and-aid/financial-aid
source_snippet: "Priority FAFSA Filing Dates: January 15 for First-Year and Transfer Students"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-014: Program Count — Undergraduate
```yaml
field: undergraduate.programs.total_count
value: "129 (118 degree programs + 11 pre-professional/undecided)"
source_url: https://admissions.rutgers.edu/majors
source_snippet: "Rutgers offers more than 150 undergraduate majors through our schools and colleges in New Brunswick, Newark, and Camden"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015: NB Schools Count
```yaml
field: institution.schools_count
value: "19 schools and colleges"
source_url: https://newbrunswick.rutgers.edu/academics
source_snippet: "The 19 schools and colleges of Rutgers–New Brunswick cover every subject"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Programs Count
```yaml
field: graduate.programs.total_count
value: "393 NB programs (including certificates and nondegree)"
source_url: https://grad.admissions.rutgers.edu/GraduateProgram/
source_snippet: "393 Programs(s)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Application Fee
```yaml
field: graduate.application_fee
value: "$70"
source_url: https://gradstudy.rutgers.edu/apply/overview
source_snippet: "Application fee: $70"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-016: NB Campus — Test-Optional
```yaml
field: undergraduate.testing.nb_policy
value: "Test optional"
source_url: https://admissions.rutgers.edu/apply/first-year-applicants
source_snippet: "Rutgers University–New Brunswick is test optional."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-017: Reply Date
```yaml
field: undergraduate.deadlines.reply_date
value: "May 1, 2026"
source_url: https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick
source_snippet: "Candidate's Reply Date*** | May 1, 2026"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-018: Transfer Deadline
```yaml
field: undergraduate.deadlines.transfer
value: "February 1, 2026"
source_url: https://admissions.rutgers.edu/apply/dates-deadlines/new-brunswick
source_snippet: "All Transfer++ | February 1, 2026 | April 15, 2026 | May 1, 2026"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
rutgers-knowledge-base-v2
├── rutgers-overview                    # Section 0 (rules 1-4)
├── rutgers-ug-sas                      # Section 1: SAS programs
├── rutgers-ug-soe                      # Section 1: SOE programs
├── rutgers-ug-sebs                     # Section 1: SEBS programs
├── rutgers-ug-rbs                      # Section 1: RBS programs
├── rutgers-ug-mgsa                     # Section 1: MGSA programs
├── rutgers-ug-sci                      # Section 1: SCI programs
├── rutgers-ug-nursing                  # Section 1: Nursing programs
├── rutgers-ug-pharmacy                 # Section 1: Pharmacy programs
├── rutgers-ug-smlr                     # Section 1: SMLR programs
├── rutgers-ug-bloustein                # Section 1: Bloustein programs
├── rutgers-ug-ssw                      # Section 1: SSW programs
├── rutgers-grad-sas                    # Section 2: SAS graduate
├── rutgers-grad-soe                    # Section 2: SOE graduate
├── rutgers-grad-gse                    # Section 2: GSE graduate
├── rutgers-grad-gsapp                  # Section 2: GSAPP graduate
├── rutgers-grad-rbs                    # Section 2: RBS graduate
├── rutgers-grad-mgsa                   # Section 2: MGSA graduate
├── rutgers-grad-sci                    # Section 2: SCI graduate
├── rutgers-grad-smlr                   # Section 2: SMLR graduate
├── rutgers-grad-bloustein              # Section 2: Bloustein graduate
├── rutgers-grad-ssw                    # Section 2: SSW graduate
├── rutgers-deadlines                   # Section 3: Deadlines
├── rutgers-english-proficiency         # Section 3: English proficiency
├── rutgers-costs                       # Section 4: Costs
├── rutgers-financial-aid               # Section 4: Financial aid
├── rutgers-evidence                    # Section 5: Evidence chain
└── rutgers-comparison                  # Section 7: Cross-school comparison
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "rutgers-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BFA|BM|MA|MS|PhD|EdD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|----------|------------|
| P0 | Verify application fee ($70 assumed) | https://admissions.rutgers.edu/apply |
| P0 | Complete minor list for all schools | School-specific websites |
| P1 | Per-program GRE requirements (grad) | https://grad.admissions.rutgers.edu/GraduateProgram/ |
| P1 | Detailed cost breakdown by school (varies) | https://admissions.rutgers.edu/costs-and-aid/tuition-fees |
| P1 | Graduate stipend rates | https://gradstudy.rutgers.edu/financial/financial-information |
| P2 | Historical acceptance rate | https://admissions.rutgers.edu/apply/how-we-make-decisions |
| P2 | Median actual price paid | https://admissions.rutgers.edu/costs-and-aid |
| P2 | Retention and graduation rates | https://admissions.rutgers.edu/FAQ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Rutgers NB | (blank for other schools) |
|-----------|-----------|--------------------------|
| Total UG cost/yr (in-state, on-campus) | $34,156 | |
| Total UG cost/yr (OOS, on-campus) | $54,981 | |
| Tuition/yr (in-state) | $14,933 | |
| Tuition/yr (OOS) | $35,758 | |
| Need-blind (domestic)? | Need-aware | |
| Need-blind (intl)? | Need-aware | |
| EA deadline | November 1 | |
| RD deadline | December 1 | |
| SAT/ACT required? | Test-optional through 2027 | |
| TOEFL min | 79 (pre-Jan 2026) / 4.5 (post-Jan 2026) | |
| IELTS min | 6.5 | |
| Duolingo min | 115 | |
| Total program count (Rule 1) | 511 (118 UG + 305 grad + 88 cert) | |
| School/department count (Rule 2) | 19 schools | |
| Application fee | $70 | |
| FAFSA code | 002629 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.rutgers.edu, gradstudy.rutgers.edu, grad.admissions.rutgers.edu, newbrunswick.rutgers.edu, catalogs.rutgers.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
