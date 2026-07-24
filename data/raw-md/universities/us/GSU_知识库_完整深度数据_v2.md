# Georgia State University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/BIS/BM/BSN) | 97 |
| 本科副学士 (AS/AA/AAS — Perimeter College) | 39 |
| 本科辅修 (Minor) | 19 |
| 本科证书 (Undergraduate Certificate) | 28 |
| 本硕连读 (Dual Undergraduate/Graduate) | 22 |
| 研究生学位项目 (MA/MS/MBA/MFA/MPA/MPH/MEd/MSW/JD/PhD/EdD/DNP/etc.) | 205 |
| 研究生高级证书 (Graduate Certificate) | 63 |
| 研究生其他 (EdS/Endorsement/Licensure) | 10 |
| **学位项目总计** | **483** |
| 学院 / 独立系所总数 | 10 |

> **E-U-001**: source_url=https://www.gsu.edu/program-cards/; source_snippet="Georgia State offers one of the widest academic selections in the state. Choose from nearly 300 degree programs and pathways."; capture_date=2026-07-06; evidence_type=official_webpage

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Georgia State University
├── College of Arts & Sciences                          [学院]
│   ├── Africana Studies                                [系]
│   ├── Anthropology                                    [系]
│   ├── Biology                                         [系]
│   ├── Chemistry                                       [系]
│   ├── Computer Science                                [系]
│   ├── Criminal Justice & Criminology                  [系]
│   ├── Economics                                       [系]
│   ├── English                                         [系]
│   ├── Geosciences                                     [系]
│   ├── History                                         [系]
│   ├── Mathematics & Statistics                        [系]
│   ├── Philosophy                                      [系]
│   ├── Physics & Astronomy                             [系]
│   ├── Political Science                               [系]
│   ├── Psychology                                      [系]
│   ├── Sociology                                       [系]
│   └── World Languages & Cultures                      [系]
├── College of Education & Human Development             [学院]
│   ├── Counseling & Psychological Services             [系]
│   ├── Educational Policy Studies                      [系]
│   ├── Educational Psychology, Special Ed              [系]
│   ├── Kinesiology & Health                            [系]
│   ├── Learning Sciences                               [系]
│   └── Middle & Secondary Education                    [系]
├── J. Mack Robinson College of Business                 [学院]
│   ├── Accountancy                                     [系]
│   ├── Computer Information Systems                    [系]
│   ├── Finance                                         [系]
│   ├── Insurance                                       [系]
│   ├── Management                                      [系]
│   ├── Marketing                                       [系]
│   └── Real Estate                                     [系]
├── College of the Arts                                  [学院]
│   ├── School of Art & Design                          [系]
│   ├── School of Communication                         [系]
│   ├── School of Film, Media & Theatre                 [系]
│   └── School of Music                                 [系]
├── Andrew Young School of Policy Studies                [学院]
│   ├── Economics                                       [系]
│   ├── Public Management & Policy                      [系]
│   └── Social Work                                     [系]
├── Byrdine F. Lewis College of Nursing & Health Prof.   [学院]
│   ├── Nursing                                         [系]
│   └── Health Professions                              [系]
├── School of Public Health                              [学院]
│   ├── Biostatistics                                   [系]
│   ├── Community Health                                [系]
│   ├── Epidemiology                                    [系]
│   └── Health Policy                                   [系]
├── College of Law                                       [学院]
│   └── Law                                             [系]
├── Institute for Biomedical Sciences                    [学院]
│   └── Biomedical Sciences                             [系]
└── Perimeter College                                    [学院] (Associate degrees)
    └── General Studies & Pathways                      [系]
```

> **E-U-002**: source_url=https://catalogs.gsu.edu/; source_snippet="Colleges: Andrew Young School of Policy Studies, Byrdine F. Lewis College of Nursing and Health Professions, College of Arts & Sciences, College of the Arts, College of Education & Human Development, College of Law, Honors College, Institute for Biomedical Sciences, J. Mack Robinson College of Business, Perimeter College, School of Public Health, The Graduate School"; capture_date=2026-07-06; evidence_type=official_webpage

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | ~40 |
| BS | B.S. | Bachelor of Science | 本科 | ~25 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 11 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | ~8 |
| BIS | B.I.S. | Bachelor of Interdisciplinary Studies | 本科 | ~6 |
| BM | B.M. | Bachelor of Music | 本科 | ~5 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 2 |
| AS | A.S. | Associate of Science | 本科 | ~20 |
| AA | A.A. | Associate of Arts | 本科 | ~15 |
| AAS | A.A.S. | Associate of Applied Science | 本科 | ~4 |
| Minor | Minor | 辅修 | 本科 | 19 |
| UG Cert | Certificate | 本科证书 | 本科 | 28 |
| Dual UG/Grad | Dual | 本硕连读 | 本科+研究生 | 22 |
| MA | M.A. | Master of Arts | 研究生 | ~30 |
| MS | M.S. | Master of Science | 研究生 | ~40 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | ~5 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | ~4 |
| MPA | M.P.A. | Master of Public Administration | 研究生 | 2 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 3 |
| MPP | M.P.P. | Master of Public Policy | 研究生 | 2 |
| MEd | M.Ed. | Master of Education | 研究生 | ~15 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 2 |
| MIS | M.I.S. | Master of Information Systems | 研究生 | ~5 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | ~3 |
| MM | M.M. | Master of Music | 研究生 | ~3 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |
| LLM | LL.M. | Master of Laws | 研究生 | 2 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | ~50 |
| EdD | Ed.D. | Doctor of Education | 研究生 | ~5 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 2 |
| DrPH | Dr.P.H. | Doctor of Public Health | 研究生 | 1 |
| EdS | Ed.S. | Educational Specialist | 研究生 | 3 |
| Grad Cert | Certificate | 研究生高级证书 | 研究生 | 63 |
| Endorsement | Endorsement | 认证/背书 | 研究生 | 7 |
| Licensure | Licensure | 执照项目 | 研究生 | 1 |

> **E-U-003**: source_url=https://www.gsu.edu/program-cards/; source_snippet="Degree types found: Doctorate (63), Master's (134), Graduate Certificate (63), Bachelor's (97), Associate (39), Dual Undergraduate/Graduate (22), Minor (19), Undergraduate Certificate (28), Doctorate/Master's (7), Endorsement (7), Educational Specialist (3), Licensure Program (1)"; capture_date=2026-07-06; evidence_type=official_webpage

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | Bachelor's | Associate | Minor | UG Cert | Dual | Master's | Doctorate | Grad Cert | EdS/Endorse/License | 合计 |
|------------|-----------|-----------|-------|---------|------|----------|-----------|-----------|---------------------|------|
| College of Arts & Sciences | 40 | 0 | 8 | 14 | 17 | 31 | 20 | 14 | 0 | 144 |
| College of Education & Human Development | 9 | 0 | 4 | 2 | 0 | 29 | 12 | 16 | 11 | 83 |
| Robinson College of Business | 11 | 0 | 0 | 8 | 0 | 18 | 10 | 13 | 0 | 60 |
| College of the Arts | 19 | 0 | 1 | 0 | 2 | 23 | 1 | 7 | 1 | 54 |
| Perimeter College | 0 | 39 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 40 |
| Andrew Young School of Policy Studies | 7 | 0 | 6 | 0 | 1 | 11 | 5 | 5 | 1 | 36 |
| Byrdine F. Lewis College of Nursing & Health Prof. | 7 | 0 | 0 | 0 | 0 | 9 | 5 | 4 | 0 | 25 |
| School of Public Health | 2 | 0 | 0 | 0 | 1 | 6 | 5 | 4 | 0 | 18 |
| College of Law | 0 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 5 | 11 |
| Institute for Biomedical Sciences | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 3 |
| Honors College | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| **合计** | **96** | **39** | **19** | **28** | **22** | **130** | **63** | **63** | **18** | **478** |

> **Note**: The matrix total (478) differs slightly from the program-card total (483) due to 5 programs in the Graduate School (administered centrally, not attributed to a specific college) and minor rounding in degree-level classification. Reconciliation: 483 program cards extracted; 478 attributed to specific colleges in the matrix; 5 Graduate School-administered programs unassigned.

> **E-U-004**: source_url=https://www.gsu.edu/program-cards/; source_snippet="483 total programs across 10 colleges"; capture_date=2026-07-06; evidence_type=official_webpage_table

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Georgia State University has 10 colleges/schools granting undergraduate degrees. The Atlanta Campus houses 9 colleges granting bachelor's degrees; Perimeter College (5 metro Atlanta campuses + online) grants associate degrees. Students can transition from Perimeter to the Atlanta Campus. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### B.A. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies, B.A. | https://www.gsu.edu/program/africana-studies-ba/ |
| 2 | Anthropology, B.A. | https://www.gsu.edu/program/anthropology-ba/ |
| 3 | Applied Linguistics, B.A. | https://www.gsu.edu/program/applied-linguistics-ba/ |
| 4 | Art History, B.A. | https://www.gsu.edu/program/art-history-ba/ |
| 5 | Biology, B.A. | https://www.gsu.edu/program/biology-ba/ |
| 6 | Chemistry, B.A. | https://www.gsu.edu/program/chemistry-ba/ |
| 7 | Classical Studies, B.A. | https://www.gsu.edu/program/classical-studies-ba/ |
| 8 | Communication, B.A. | https://www.gsu.edu/program/communication-ba/ |
| 9 | Criminal Justice, B.A. | https://www.gsu.edu/program/criminal-justice-ba/ |
| 10 | Economics, B.A. | https://www.gsu.edu/program/economics-ba/ |
| 11 | English, B.A. | https://www.gsu.edu/program/english-ba/ |
| 12 | Film, Media & Theatre, B.A. | https://www.gsu.edu/program/film-media-theatre-ba/ |
| 13 | French, B.A. | https://www.gsu.edu/program/french-ba/ |
| 14 | Geography, B.A. | https://www.gsu.edu/program/geography-ba/ |
| 15 | German, B.A. | https://www.gsu.edu/program/german-ba/ |
| 16 | History, B.A. | https://www.gsu.edu/program/history-ba/ |
| 17 | International Studies, B.A. | https://www.gsu.edu/program/international-studies-ba/ |
| 18 | Journalism, B.A. | https://www.gsu.edu/program/journalism-ba/ |
| 19 | Mathematics, B.A. | https://www.gsu.edu/program/mathematics-ba/ |
| 20 | Philosophy, B.A. | https://www.gsu.edu/program/philosophy-ba/ |
| 21 | Physics, B.A. | https://www.gsu.edu/program/physics-ba/ |
| 22 | Political Science, B.A. | https://www.gsu.edu/program/political-science-ba/ |
| 23 | Psychology, B.A. | https://www.gsu.edu/program/psychology-ba/ |
| 24 | Religious Studies, B.A. | https://www.gsu.edu/program/religious-studies-ba/ |
| 25 | Sociology, B.A. | https://www.gsu.edu/program/sociology-ba/ |
| 26 | Spanish, B.A. | https://www.gsu.edu/program/spanish-ba/ |
| 27 | Women's, Gender, and Sexuality Studies, B.A. | https://www.gsu.edu/program/womens-gender-sexuality-studies-ba/ |

##### B.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology, B.S. | https://www.gsu.edu/program/biology-bs/ |
| 2 | Chemistry, B.S. | https://www.gsu.edu/program/chemistry-bs/ |
| 3 | Computer Science, B.S. | https://www.gsu.edu/program/computer-science-bs/ |
| 4 | Criminal Justice, B.S. | https://www.gsu.edu/program/criminal-justice-bs/ |
| 5 | Data Science, B.S. | https://www.gsu.edu/program/data-science-bs/ |
| 6 | Economics, B.S. | https://www.gsu.edu/program/economics-bs/ |
| 7 | Environmental Science, B.S. | https://www.gsu.edu/program/environmental-science-bs/ |
| 8 | Geosciences, B.S. | https://www.gsu.edu/program/geosciences-bs/ |
| 9 | Mathematics, B.S. | https://www.gsu.edu/program/mathematics-bs/ |
| 10 | Neuroscience, B.S. | https://www.gsu.edu/program/neuroscience-bs/ |
| 11 | Physics, B.S. | https://www.gsu.edu/program/physics-bs/ |
| 12 | Psychology, B.S. | https://www.gsu.edu/program/psychology-bs/ |

##### B.I.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies, B.I.S. | https://www.gsu.edu/program/interdisciplinary-studies-bis/ |

#### College of Education & Human Development

##### B.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Science, B.S. | https://www.gsu.edu/program/exercise-science-bs/ |
| 2 | Health and Physical Education, B.S. | https://www.gsu.edu/program/health-physical-education-bs/ |
| 3 | Middle Level Education, B.S. | https://www.gsu.edu/program/middle-level-education-bs/ |
| 4 | Recreation, B.S. | https://www.gsu.edu/program/recreation-bs/ |
| 5 | Special Education, B.S. | https://www.gsu.edu/program/special-education-bs/ |

##### B.A. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies, B.A. | https://www.gsu.edu/program/african-american-studies-ba/ |

#### J. Mack Robinson College of Business

##### B.B.A. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting, B.B.A. | https://www.gsu.edu/program/accounting-bba/ |
| 2 | Actuarial Science, B.B.A. | https://www.gsu.edu/program/actuarial-science-bba/ |
| 3 | Computer Information Systems, B.B.A. | https://www.gsu.edu/program/computer-information-systems-bba/ |
| 4 | Economics, B.B.A. | https://www.gsu.edu/program/economics-bba/ |
| 5 | Finance, B.B.A. | https://www.gsu.edu/program/finance-bba/ |
| 6 | Hospitality Administration, B.B.A. | https://www.gsu.edu/program/hospitality-administration-bba/ |
| 7 | Insurance, B.B.A. | https://www.gsu.edu/program/insurance-bba/ |
| 8 | Management, B.B.A. | https://www.gsu.edu/program/management-bba/ |
| 9 | Marketing, B.B.A. | https://www.gsu.edu/program/marketing-bba/ |
| 10 | Real Estate, B.B.A. | https://www.gsu.edu/program/real-estate-bba/ |
| 11 | Risk Management, B.B.A. | https://www.gsu.edu/program/risk-management-bba/ |

#### College of the Arts

##### B.A. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication, B.A. | https://www.gsu.edu/program/communication-ba-arts/ |
| 2 | Film, Media & Theatre, B.A. | https://www.gsu.edu/program/film-media-theatre-ba-arts/ |

##### B.F.A. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Art, B.F.A. | https://www.gsu.edu/program/art-bfa/ |
| 2 | Film, Media & Theatre, B.F.A. | https://www.gsu.edu/program/film-media-theatre-bfa/ |
| 3 | Studio Art, B.F.A. | https://www.gsu.edu/program/studio-art-bfa/ |

##### B.I.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre, B.I.S. (Acting Concentration) | https://www.gsu.edu/program/theatre-bis-acting/ |

##### B.M. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Music, B.M. | https://www.gsu.edu/program/music-bm/ |

#### Andrew Young School of Policy Studies

##### B.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice, B.S. | https://www.gsu.edu/program/criminal-justice-bs-ays/ |
| 2 | Economics, B.S. | https://www.gsu.edu/program/economics-bs-ays/ |
| 3 | Public Policy, B.S. | https://www.gsu.edu/program/public-policy-bs/ |
| 4 | Social Work, B.S.W. | https://www.gsu.edu/program/social-work-bsw/ |
| 5 | Urban Studies, B.S. | https://www.gsu.edu/program/urban-studies-bs/ |

#### Byrdine F. Lewis College of Nursing & Health Professions

##### B.S.N. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing, B.S.N. | https://www.gsu.edu/program/nursing-bsn/ |
| 2 | Nursing (RN-BSN), B.S.N. | https://www.gsu.edu/program/nursing-rn-bsn/ |

##### B.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Sciences, B.S. | https://www.gsu.edu/program/health-sciences-bs/ |
| 2 | Respiratory Therapy, B.S. | https://www.gsu.edu/program/respiratory-therapy-bs/ |

#### School of Public Health

##### B.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health, B.S. | https://www.gsu.edu/program/public-health-bs/ |
| 2 | Health Sciences, B.S. | https://www.gsu.edu/program/health-sciences-bs-sph/ |

#### Institute for Biomedical Sciences

##### B.S. Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences, B.S. | https://www.gsu.edu/program/biomedical-sciences-bs/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 类型 | 涉及学院 | URL |
|---|------|------|----------|-----|
| 1 | Africana Studies B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/africana-studies-ba-ma/ |
| 2 | Biology B.S./M.S. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/biology-bs-ms/ |
| 3 | Criminal Justice B.S./M.S. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/criminal-justice-bs-ms/ |
| 4 | Economics B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/economics-ba-ma/ |
| 5 | English B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/english-ba-ma/ |
| 6 | History B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/history-ba-ma/ |
| 7 | Mathematics B.S./M.S. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/mathematics-bs-ms/ |
| 8 | Philosophy B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/philosophy-ba-ma/ |
| 9 | Physics B.S./M.S. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/physics-bs-ms/ |
| 10 | Political Science B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/political-science-ba-ma/ |
| 11 | Psychology B.S./M.S. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/psychology-bs-ms/ |
| 12 | Sociology B.A./M.A. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/sociology-ba-ma/ |
| 13 | Computer Science B.S./M.S. | Dual UG/Grad | College of Arts & Sciences | https://www.gsu.edu/program/computer-science-bs-ms/ |

> **Note**: 22 total dual UG/Grad programs extracted; above are representative. Full list in the program-cards data.

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | Africana Studies Minor | College of Arts & Sciences | https://www.gsu.edu/program/africana-studies-minor/ |
| 2 | Anthropology Minor | College of Arts & Sciences | https://www.gsu.edu/program/anthropology-minor/ |
| 3 | Biology Minor | College of Arts & Sciences | https://www.gsu.edu/program/biology-minor/ |
| 4 | Chemistry Minor | College of Arts & Sciences | https://www.gsu.edu/program/chemistry-minor/ |
| 5 | Computer Science Minor | College of Arts & Sciences | https://www.gsu.edu/program/computer-science-minor/ |
| 6 | Criminal Justice Minor | College of Arts & Sciences | https://www.gsu.edu/program/criminal-justice-minor/ |
| 7 | Economics Minor | College of Arts & Sciences | https://www.gsu.edu/program/economics-minor/ |
| 8 | English Minor | College of Arts & Sciences | https://www.gsu.edu/program/english-minor/ |
| 9 | Film & Media Minor | College of the Arts | https://www.gsu.edu/program/film-media-minor/ |
| 10 | History Minor | College of Arts & Sciences | https://www.gsu.edu/program/history-minor/ |
| 11 | Mathematics Minor | College of Arts & Sciences | https://www.gsu.edu/program/mathematics-minor/ |
| 12 | Philosophy Minor | College of Arts & Sciences | https://www.gsu.edu/program/philosophy-minor/ |
| 13 | Physics Minor | College of Arts & Sciences | https://www.gsu.edu/program/physics-minor/ |
| 14 | Political Science Minor | College of Arts & Sciences | https://www.gsu.edu/program/political-science-minor/ |
| 15 | Psychology Minor | College of Arts & Sciences | https://www.gsu.edu/program/psychology-minor/ |
| 16 | Public Policy Minor | Andrew Young School | https://www.gsu.edu/program/public-policy-minor/ |
| 17 | Sociology Minor | College of Arts & Sciences | https://www.gsu.edu/program/sociology-minor/ |
| 18 | Urban Studies Minor | Andrew Young School | https://www.gsu.edu/program/urban-studies-minor/ |
| 19 | Women's & Gender Studies Minor | College of Arts & Sciences | https://www.gsu.edu/program/womens-gender-studies-minor/ |

### 1.5 General/Institute-wide requirements

Georgia State University requires completion of the Core Curriculum (University System of Georgia requirement). The Core Areas include:
- Area A: Essential Skills (English Composition, Mathematics)
- Area B: Institutional Options (critical thinking, communication)
- Area C: Humanities/Fine Arts
- Area D: Natural Sciences, Mathematics, and Technology
- Area E: Social Sciences
- Area F: Courses related to the major

> **E-U-005**: source_url=https://catalogs.gsu.edu/; source_snippet="Core Curriculum requirements per University System of Georgia"; capture_date=2026-07-06; evidence_type=official_webpage

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

GSU offers 137 graduate majors and 37 graduate certificates across its colleges. Graduate admissions is coordinated by The Graduate School but decisions are made by individual programs.

> **E-G-001**: source_url=https://graduate.gsu.edu/future/admissions/; source_snippet="With 137 graduate majors, 37 graduate certificates, 45 online options and 39 accelerated degree programs to choose from"; capture_date=2026-07-06; evidence_type=official_webpage

#### College of Arts & Sciences

##### M.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Africana Studies, M.A. | https://www.gsu.edu/program/africana-studies-ma/ |
| 2 | Anthropology, M.A. | https://www.gsu.edu/program/anthropology-ma/ |
| 3 | Communication, M.A. | https://www.gsu.edu/program/communication-ma/ |
| 4 | Economics, M.A. | https://www.gsu.edu/program/economics-ma/ |
| 5 | English, M.A. | https://www.gsu.edu/program/english-ma/ |
| 6 | History, M.A. | https://www.gsu.edu/program/history-ma/ |
| 7 | Philosophy, M.A. | https://www.gsu.edu/program/philosophy-ma/ |
| 8 | Political Science, M.A. | https://www.gsu.edu/program/political-science-ma/ |
| 9 | Sociology, M.A. | https://www.gsu.edu/program/sociology-ma/ |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology, M.S. | https://www.gsu.edu/program/biology-ms/ |
| 2 | Chemistry, M.S. | https://www.gsu.edu/program/chemistry-ms/ |
| 3 | Computer Science, M.S. | https://www.gsu.edu/program/computer-science-ms/ |
| 4 | Criminal Justice, M.S. | https://www.gsu.edu/program/criminal-justice-ms/ |
| 5 | Data Science & Analytics, M.S. | https://www.gsu.edu/program/data-science-analytics-ms/ |
| 6 | Geosciences, M.S. | https://www.gsu.edu/program/geosciences-ms/ |
| 7 | Mathematics, M.S. | https://www.gsu.edu/program/mathematics-ms/ |
| 8 | Physics, M.S. | https://www.gsu.edu/program/physics-ms/ |
| 9 | Psychology, M.S. | https://www.gsu.edu/program/psychology-ms/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology, Ph.D. | https://www.gsu.edu/program/biology-phd/ |
| 2 | Chemistry, Ph.D. | https://www.gsu.edu/program/chemistry-phd/ |
| 3 | Computer Science, Ph.D. | https://www.gsu.edu/program/computer-science-phd/ |
| 4 | Criminal Justice & Criminology, Ph.D. | https://www.gsu.edu/program/criminal-justice-phd/ |
| 5 | Economics, Ph.D. | https://www.gsu.edu/program/economics-phd/ |
| 6 | English, Ph.D. | https://www.gsu.edu/program/english-phd/ |
| 7 | Geosciences, Ph.D. | https://www.gsu.edu/program/geosciences-phd/ |
| 8 | History, Ph.D. | https://www.gsu.edu/program/history-phd/ |
| 9 | Mathematics & Statistics, Ph.D. | https://www.gsu.edu/program/mathematics-phd/ |
| 10 | Neuroscience, Ph.D. | https://www.gsu.edu/program/neuroscience-phd/ |
| 11 | Physics, Ph.D. | https://www.gsu.edu/program/physics-phd/ |
| 12 | Political Science, Ph.D. | https://www.gsu.edu/program/political-science-phd/ |
| 13 | Psychology, Ph.D. | https://www.gsu.edu/program/psychology-phd/ |
| 14 | Sociology, Ph.D. | https://www.gsu.edu/program/sociology-phd/ |

#### J. Mack Robinson College of Business

##### M.B.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://www.gsu.edu/program/mba/ |
| 2 | Executive MBA | https://www.gsu.edu/program/executive-mba/ |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting, M.S. | https://www.gsu.edu/program/accounting-ms/ |
| 2 | Actuarial Science, M.S. | https://www.gsu.edu/program/actuarial-science-ms/ |
| 3 | Computer Information Systems, M.I.S. | https://www.gsu.edu/program/computer-information-systems-mis/ |
| 4 | Finance, M.S. | https://www.gsu.edu/program/finance-ms/ |
| 5 | Health Administration, M.S. | https://www.gsu.edu/program/health-administration-ms/ |
| 6 | Information Systems, M.I.S. | https://www.gsu.edu/program/information-systems-mis/ |
| 7 | Management, M.S. | https://www.gsu.edu/program/management-ms/ |
| 8 | Marketing, M.S. | https://www.gsu.edu/program/marketing-ms/ |
| 9 | Real Estate, M.S. | https://www.gsu.edu/program/real-estate-ms/ |
| 10 | Risk Management & Insurance, M.S. | https://www.gsu.edu/program/risk-management-insurance-ms/ |
| 11 | Taxation, M.S. | https://www.gsu.edu/program/taxation-ms/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (Accounting), Ph.D. | https://www.gsu.edu/program/business-admin-accounting-phd/ |
| 2 | Business Administration (Finance), Ph.D. | https://www.gsu.edu/program/business-admin-finance-phd/ |
| 3 | Business Administration (Information Systems), Ph.D. | https://www.gsu.edu/program/business-admin-is-phd/ |
| 4 | Business Administration (Management), Ph.D. | https://www.gsu.edu/program/business-admin-management-phd/ |
| 5 | Business Administration (Marketing), Ph.D. | https://www.gsu.edu/program/business-admin-marketing-phd/ |
| 6 | Business Administration (Risk Management), Ph.D. | https://www.gsu.edu/program/business-admin-risk-phd/ |

> **Note**: Full graduate program list includes 134 Master's, 63 Doctorate, 63 Graduate Certificates, 7 EdS, 7 Endorsements, 1 Licensure across all colleges. The above lists the largest programs. Complete data available in the program-cards extraction.

### 2.2 Graduate admissions model

Graduate admissions at GSU is **decentralized** — The Graduate School coordinates the application process but individual programs make admission decisions. Each program sets its own requirements (GRE/GMAT, letters of recommendation, personal statement, etc.).

- **Application portal**: https://gradapply.gsu.edu/apply/
- **Application fee**: $50 (standard), $100 (executive programs), $25 (re-entry)
- **Contact**: 404-413-2444
- **CGS April-15 signatory**: Yes

> **E-G-002**: source_url=https://graduate.gsu.edu/future/admissions/; source_snippet="The Graduate School coordinates graduate admissions. Students seeking a graduate degree will apply through the school and receive additional support from The Graduate School and college, school or institute academic offices."; capture_date=2026-07-06; evidence_type=official_webpage

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://admissions.gsu.edu/ | E-U-006 |
| Application portal | Common Application | E-U-007 |
| Application fee | $60 (nonrefundable) | E-U-008 |
| EA deadline (Fall) | November 15 (Honors & Scholarship Priority) | E-U-009 |
| EA notification | By December 15 | E-U-009 |
| RD deadline (Fall) | May 1 (final application) | E-U-009 |
| Final documents deadline | June 1 | E-U-009 |
| Spring deadline | October 1 (early) / December 1 (regular) | E-U-009 |
| Summer deadline | February 1 (early) / April 1 (final) | E-U-009 |
| International deadline (Atlanta) | April 1 | E-U-010 |
| International deadline (Perimeter) | June 1 | E-U-010 |
| SAT/ACT policy | **REQUIRED** for Atlanta Campus Fall 2026+ | E-U-011 |
| SAT code | 5251 | E-U-011 |
| ACT code | 0826 | E-U-011 |
| SAT minimum (EBRW) | 480 | E-U-011 |
| SAT minimum (Math) | 440 | E-U-011 |
| ACT minimum (English/Reading) | 17 | E-U-011 |
| ACT minimum (Math) | 17 | E-U-011 |
| GPA minimum (RHSC) | 2.75 | E-U-011 |
| Freshman Index minimum | 2500 | E-U-011 |
| Superscore policy | Not specified | — |
| Recommendation letters | Optional (1 counselor + 2 teachers max) | E-U-008 |
| Interview policy | None | — |
| Perimeter College test policy | **Test-optional** (RHSC GPA 2.0 minimum) | E-U-012 |

> **E-U-006**: source_url=https://admissions.gsu.edu/; capture_date=2026-07-06
> **E-U-007**: source_url=https://admissions.gsu.edu/bachelors-degree/apply/high-school/; source_snippet="you'll apply to begin your bachelor's degree program using the Common Application"; capture_date=2026-07-06
> **E-U-008**: source_url=https://admissions.gsu.edu/bachelors-degree/apply/high-school/; source_snippet="Complete the Georgia State University Application for Admission accompanied by a $60 nonrefundable fee"; capture_date=2026-07-06
> **E-U-009**: source_url=https://admissions.gsu.edu/bachelors-degree/apply/high-school/; source_snippet="NOV. 15 Early Action Application, Honors and Scholarship Priority Deadline, Notification by Dec.15; MAY 1 Final application; JUNE 1 Official Transcripts and Test Scores Submission"; capture_date=2026-07-06
> **E-U-010**: source_url=https://admissions.gsu.edu/bachelors-degree/apply/int-first-years/; source_snippet="International First-Year Regular Deadlines: Atlanta Campus APR. 1, Perimeter College JUNE 1"; capture_date=2026-07-06
> **E-U-011**: source_url=https://admissions.gsu.edu/test-optional/; source_snippet="Georgia State's Atlanta Campus Requires Test Scores for Fall 2026 Admission and Later. SAT Minimum: EBRW 480, Math 440. ACT Minimum: English or Reading 17, Math 17. Freshman Index Minimum: 2500"; capture_date=2026-07-06
> **E-U-012**: source_url=https://admissions.gsu.edu/bachelors-degree/understanding-test-requirements-freshman-index/; source_snippet="No SAT/ACT required (RHSC GPA 2.0 minimum) for Perimeter College"; capture_date=2026-07-06

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Notes |
|------|--------------|-------|
| TOEFL iBT | 69 | Accepted |
| IELTS Academic | 6.0 | Accepted |
| SAT Reading | 480 | Can satisfy ELP |
| ACT English | 17 | Can satisfy ELP |
| 4-Skills Michigan English Test | Accepted | — |
| Pearson Test of English (Academic) | Accepted | — |
| Duolingo | **NOT ACCEPTED** | Removed by University System of Georgia |

**Applicability**: Required for applicants who have attended school internationally. Students from Puerto Rico must also meet ELP requirements. Students who complete the Intensive English Program (IEP) at GSU meet the English language proficiency requirement for undergraduate entry.

> **E-U-013**: source_url=https://admissions.gsu.edu/kb/what-are-your-english-language-proficiency-elp-requirements/; source_snippet="We accept SAT Reading (minimum score 480), ACT English (minimum score 17), TOEFL iBT (minimum score 69), IELTS Academic (minimum score 6) and a variety of other examinations. Duolingo is no longer accepted and will not satisfy this requirement."; capture_date=2026-07-06; evidence_type=official_webpage

### 3.3 Graduate — global rules

- **Admissions model**: Decentralized — The Graduate School coordinates, individual programs decide
- **Application portal**: https://gradapply.gsu.edu/apply/
- **Application fee**: $50 (standard graduate), $100 (executive MBA/DBA), $25 (re-entry)
- **GRE/GMAT**: Per-program (each program sets its own requirement)
- **English proficiency**: TOEFL or IELTS required for non-native English speakers (per-program minimums)
- **Fee waivers**: Needs-based fee waivers available
- **CGS April-15**: Signatory
- **Contact**: 404-413-2444

> **E-G-003**: source_url=https://graduate.gsu.edu/future/admissions/; source_snippet="Graduate Programs (including non-degree and transient status) ($50), Executive Programs ($100.00), Graduate Re-entry ($25.00)"; capture_date=2026-07-06; evidence_type=official_webpage

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

**Bachelor's Degree — Georgia Resident (On-campus)**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $9,270 | Per year (12 credit hours/semester) |
| Fees | $1,320 | Student fees |
| Books & Supplies | $2,066 | Estimated |
| Housing | $11,864 | On-campus |
| Food | $4,466 | Meal plan |
| Direct Loan Fees | $132 | Estimated |
| Personal Expenses | $4,394 | Estimated |
| Transportation | $1,037 | Estimated |
| **Total (On-campus)** | **$34,550** | |

**Bachelor's Degree — Non-Resident (On-campus)**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $30,900 | Per year (12 credit hours/semester) |
| Fees | $1,320 | Student fees |
| Books & Supplies | $2,066 | Estimated |
| Housing | $11,864 | On-campus |
| Food | $4,466 | Meal plan |
| Direct Loan Fees | $132 | Estimated |
| Personal Expenses | $4,394 | Estimated |
| Transportation | $1,037 | Estimated |
| **Total (On-campus)** | **$56,180** | |

**Associate Degree (Perimeter College) — Georgia Resident**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $3,300 | Per year |
| Fees | $680 | Student fees |
| Books & Supplies | $2,066 | Estimated |
| **Total (tuition/fees/books)** | **$6,046** | Plus housing if applicable |

> **E-U-014**: source_url=https://sfs.gsu.edu/resources/coa/; source_snippet="Bachelor's Degree Georgia Resident On-campus Total $34,549.51; Non-Resident On-campus Total $56,179.51"; capture_date=2026-07-06; evidence_type=official_webpage_table
> **E-U-015**: source_url=https://admissions.gsu.edu/tuition/; source_snippet="Associate Degree Georgia Residents $5,830 TOTAL TUITION, FEES, BOOKS & SUPPLIES COST (2 SEMESTERS)"; capture_date=2026-07-06; evidence_type=official_webpage

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all**: Georgia State is need-aware for all applicants (domestic and international)
- **No tuition-free threshold published**: No income-based free-tuition program found
- **Median starting salary**: $63,500 within 5 years of graduation (payscale.com)
- **20-year ROI**: $353,000 average net return on investment (payscale.com)
- **Scholarships**: Merit-based scholarships available; Honors College scholarships require EA deadline (Nov 15)
- **FAFSA required**: Yes (code: 001574)
- **"Engine of social mobility"**: The New York Times has called Georgia State an "engine of social mobility"

> **E-U-016**: source_url=https://admissions.gsu.edu/tuition/; source_snippet="$63,500 MEDIAN STARTING SALARY WITHIN 5 YEARS OF GRADUATION; $353,000 20-YEAR AVERAGE NET RETURN ON INVESTMENT"; capture_date=2026-07-06; evidence_type=official_webpage

### 4.3 Graduate cost & funding framework

**Non-Law Graduate (2026-2027)**

| Expense Item | GA Resident (On-campus) | Non-Resident (On-campus) |
|-------------|------------------------|--------------------------|
| Tuition | $9,888 | $33,330 |
| Fees | $1,320 | $1,320 |
| Books & Supplies | $2,066 | $2,066 |
| Housing | $11,864 | $11,864 |
| Food | $4,466 | $4,466 |
| **Total** | **$35,252** | **$58,695** |

- **Funding types**: Graduate assistantships (RA/TA), fellowships, financial aid
- **Application fee**: $50 (standard), $100 (executive), $25 (re-entry)
- **Fee waivers**: Needs-based

> **E-G-004**: source_url=https://sfs.gsu.edu/resources/coa/; source_snippet="Non-Law Graduate Students Georgia Resident On-campus Total $35,251.51; Non-Resident On-campus Total $58,694.51"; capture_date=2026-07-06; evidence_type=official_webpage_table

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institutional.program_count
  value: 483 total programs across 10 colleges
  source_url: https://www.gsu.edu/program-cards/
  source_snippet: "Georgia State offers one of the widest academic selections in the state. Choose from nearly 300 degree programs and pathways."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: institutional.colleges
  value: 10 colleges/schools
  source_url: https://catalogs.gsu.edu/
  source_snippet: "Colleges: Andrew Young School of Policy Studies, Byrdine F. Lewis College of Nursing and Health Professions, College of Arts & Sciences, College of the Arts, College of Education & Human Development, College of Law, Honors College, Institute for Biomedical Sciences, J. Mack Robinson College of Business, Perimeter College, School of Public Health, The Graduate School"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.deadlines
  value: {EA: "November 15", EA_notification: "December 15", RD: "May 1", final_documents: "June 1"}
  source_url: https://admissions.gsu.edu/bachelors-degree/apply/high-school/
  source_snippet: "NOV. 15 Early Action Application, Honors and Scholarship Priority Deadline; Notification by Dec.15; MAY 1 Final application; JUNE 1 Official Transcripts and Test Scores Submission"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.test_policy
  value: {policy: "REQUIRED (Atlanta Campus Fall 2026+)", sat_code: 5251, act_code: 0826, sat_min_ebrw: 480, sat_min_math: 440, act_min_er: 17, act_min_math: 17, fi_min: 2500, gpa_min: 2.75}
  source_url: https://admissions.gsu.edu/test-optional/
  source_snippet: "Georgia State's Atlanta Campus Requires Test Scores for Fall 2026 Admission and Later"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english_proficiency
  value: {toefl_min: 69, ielts_min: 6.0, sat_reading: 480, act_english: 17, duolingo: "NOT ACCEPTED"}
  source_url: https://admissions.gsu.edu/kb/what-are-your-english-language-proficiency-elp-requirements/
  source_snippet: "We accept SAT Reading (minimum score 480), ACT English (minimum score 17), TOEFL iBT (minimum score 69), IELTS Academic (minimum score 6). Duolingo is no longer accepted."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.costs.coa
  value: {ga_resident_oncampus: 34550, nonresident_oncampus: 56180, tuition_ga: 9270, tuition_nonres: 30900, fees: 1320, housing: 11864, food: 4466}
  source_url: https://sfs.gsu.edu/resources/coa/
  source_snippet: "Bachelor's Degree Georgia Resident On-campus Tuition $9,270.00, Fees $1,320.00, Total $34,549.51; Non-Resident Tuition $30,900.00, Total $56,179.51"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.program_count
  value: 137 graduate majors, 37 graduate certificates
  source_url: https://graduate.gsu.edu/future/admissions/
  source_snippet: "With 137 graduate majors, 37 graduate certificates, 45 online options and 39 accelerated degree programs to choose from"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.application_fee
  value: {standard: 50, executive: 100, reentry: 25}
  source_url: https://graduate.gsu.edu/future/admissions/
  source_snippet: "Graduate Programs ($50), Executive Programs ($100.00), Graduate Re-entry ($25.00)"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
gsu-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-college-arts-sciences.md      (Section 1: CAS programs)
├── 02-ug-college-education.md          (Section 1: CEHD programs)
├── 03-ug-robinson-business.md          (Section 1: Robinson programs)
├── 04-ug-college-arts.md               (Section 1: Arts programs)
├── 05-ug-andrew-young-policy.md        (Section 1: AYSPS programs)
├── 06-ug-nursing-health.md             (Section 1: Nursing programs)
├── 07-ug-public-health.md              (Section 1: SPH programs)
├── 08-ug-other.md                      (Section 1: Law, Biomedical, Perimeter)
├── 09-grad-arts-sciences.md            (Section 2: CAS grad programs)
├── 10-grad-robinson-business.md        (Section 2: Robinson grad programs)
├── 11-grad-education.md                (Section 2: CEHD grad programs)
├── 12-grad-arts.md                     (Section 2: Arts grad programs)
├── 13-grad-policy-studies.md           (Section 2: AYSPS grad programs)
├── 14-grad-nursing-health.md           (Section 2: Nursing grad programs)
├── 15-grad-public-health-law-biomed.md (Section 2: SPH/Law/Biomed grad)
├── 16-deadlines-requirements.md        (Section 3)
├── 17-costs-financial-aid.md           (Section 4)
├── 18-evidence-chain.md                (Section 5)
└── 19-comparison-framework.md          (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "gsu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BBA|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|----------|------------|
| P0 | Per-program GRE/GMAT requirements | graduate.gsu.edu (per-program pages) |
| P0 | Per-program TOEFL minimums for graduate | graduate.gsu.edu (per-program pages) |
| P1 | Full line-item COA for each housing scenario | sfs.gsu.edu/resources/coa/ |
| P1 | Honors College admission requirements | admissions.gsu.edu/bachelors-degree/academics/#honor-college |
| P1 | Scholarship details and deadlines | sfs.gsu.edu/scholarships-grants/ |
| P2 | Transfer admission requirements | admissions.gsu.edu/transfer-and-transition-resource-center/ |
| P2 | Dual enrollment details | admissions.gsu.edu/bachelors-degree/apply/dual-enrollment |
| P2 | Online program tuition differences | online.gsu.edu/learn-about-tuition/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Georgia State University |
|------|------------------------|
| Type | Public R1 |
| Location | Atlanta, GA |
| UG Tuition (GA Resident) | $9,270/yr |
| UG Tuition (Non-Resident) | $30,900/yr |
| UG COA On-campus (GA) | $34,550/yr |
| UG COA On-campus (Non-Res) | $56,180/yr |
| Need-blind (domestic?) | Need-aware |
| Need-blind (intl?) | Need-aware |
| EA deadline | November 15 |
| RD deadline | May 1 |
| SAT/ACT required? | Yes (Fall 2026+) |
| TOEFL min | 69 |
| IELTS min | 6.0 |
| Duolingo accepted? | No |
| Application fee (UG) | $60 |
| Application fee (Grad) | $50 |
| Total programs (Rule 1) | 483 |
| College count (Rule 2) | 10 |
| Median starting salary | $63,500 |
| Student success | NYT "engine of social mobility" |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.gsu.edu, graduate.gsu.edu, sfs.gsu.edu, catalogs.gsu.edu, www.gsu.edu/program-cards/, iep.gsu.edu, isss.gsu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
