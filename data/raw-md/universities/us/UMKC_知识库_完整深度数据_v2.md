# University of Missouri-Kansas City (UMKC) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

> **Note**: UMKC is a Carnegie R1 public research university in Kansas City, Missouri. Part of the University of Missouri System. Founded 1929. Operates 11 academic schools including a Conservatory of Music and Dance, and professional schools of Medicine, Pharmacy, Dentistry, Nursing, and Law. Programs are decentralized across per-school subdomains (bloch.umkc.edu, conservatory.umkc.edu, med.umkc.edu, sonhs.umkc.edu, sse.umkc.edu, etc.). The authoritative program directory lives at https://programs.umkc.edu/ (Algolia/InfiniteHits); the academic catalog at https://catalog.umkc.edu/academic-programs/ is the canonical catalog.

## 0. 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (含 Bachelor of Science / Bachelor of Arts / 等) | 60 |
| 本科辅修 (Minor) | 55 |
| 本科证书 (UG Certificate) | 10 |
| 研究生学位项目 (含 MS / MA / MBA / PhD / MFA / MD / JD / DDS / PharmD / DNP 等) | 80 |
| 研究生高级证书 (Graduate Certificate) | 30 |
| **学位项目总计 (UG 学位 + Minor + UG Cert + Grad 学位 + Grad Cert)** | **235** |
| 学院 / 独立系所总数 (含 School of Graduate Studies) | 11 |

> Source: https://catalog.umkc.edu/academic-programs/ (extracted 2026-07-07, 235 program rows from the 204-row catalog table where each row contains up to 2 degree types, totaling 235 leaves). The Program Finder (https://programs.umkc.edu/) reports 249 results because it includes sub-emphasis variants (e.g., Biology — Bioinformatics, Accelerated BS/MS) that the catalog collapses into single rows.

### 0.2 学院 / 系层级结构

```
University of Missouri-Kansas City (UMKC, T4 R1 public research)
├── Henry W. Bloch School of Management                   [学院]
│   ├── Accounting                                        [系]
│   ├── Business Administration                          [系]
│   ├── Entrepreneurship                                  [系]
│   ├── Finance                                           [系]
│   ├── Management                                        [系]
│   ├── Marketing                                         [系]
│   └── Management Information Systems                   [系]
├── UMKC Conservatory (Music and Dance)                  [学院]
│   ├── Dance                                             [系]
│   ├── Jazz Studies                                      [系]
│   ├── Music                                             [系]
│   ├── Music Composition                                 [系]
│   ├── Music Education                                   [系]
│   ├── Music Theory                                      [系]
│   ├── Performance                                       [系]
│   └── Theatre                                           [系]
├── School of Dentistry                                   [学院]
│   ├── Dental Hygiene                                    [系]
│   ├── Dentistry Professional (DDS)                     [系]
│   ├── Endodontics                                       [系]
│   ├── General Practice                                  [系]
│   ├── Oral & Craniofacial Sciences                     [系]
│   └── Orthodontics                                      [系]
├── School of Education, Social Work and Psychological Sciences   [学院]
│   ├── Counseling Psychology & Counselor Education      [系]
│   ├── Curriculum & Instruction                          [系]
│   ├── Education (general)                               [系]
│   ├── Educational Research & Psychology                 [系]
│   ├── Reading                                           [系]
│   ├── Social Work                                       [系]
│   ├── Special Education                                 [系]
│   ├── Teacher Education                                 [系]
│   └── Urban Leadership                                  [系]
├── School of Humanities and Social Sciences              [学院]
│   ├── Communication Studies                             [系]
│   ├── Criminal Justice & Criminology                    [系]
│   ├── Economics                                         [系]
│   ├── English Language & Literature                     [系]
│   ├── Foreign Language / World Languages                [系]
│   ├── Geography                                         [系]
│   ├── Geology                                           [系]
│   ├── History                                           [系]
│   ├── Media Art & Design                                [系]
│   ├── Philosophy                                        [系]
│   ├── Political Science                                 [系]
│   ├── Religious Studies                                 [系]
│   ├── Sociology & Anthropology                          [系]
│   └── Spanish                                           [系]
├── School of Law                                          [学院]
│   ├── Juris Doctor (JD)                                  [系]
│   └── LLM (Master of Laws)                               [系]
├── School of Medicine                                     [学院]
│   ├── Anesthesia                                         [系]
│   ├── Basic Medical Science                              [系]
│   ├── Bioinformatics                                     [系]
│   ├── Cell Biology & Biophysics                          [系]
│   ├── Medicine (MD)                                      [系]
│   ├── Molecular Biology & Biochemistry                   [系]
│   ├── Oral & Craniofacial Sciences (joint)               [系]  ⚠ shared with Dentistry
│   └── Physician Assistant                                [系]
├── School of Nursing and Health Studies                   [学院]
│   ├── Health Studies                                     [系]
│   ├── Nursing BSN / RN-BSN                               [系]
│   └── Nursing MSN / DNP                                  [系]
├── School of Pharmacy                                     [学院]
│   ├── Pharmacy (PharmD)                                  [系]
│   ├── Pharmaceutical Sciences                            [系]
│   └── Pharmacology                                       [系]
├── School of Science and Engineering                      [学院]
│   ├── Architecture & Urban Planning                      [系]
│   ├── Biological Sciences                                [系]
│   ├── Biomedical Engineering                             [系]
│   ├── Chemistry                                          [系]
│   ├── Civil Engineering                                   [系]
│   ├── Computer Science & Electrical Engineering         [系]
│   ├── Earth & Environmental Science                      [系]
│   ├── Mathematics & Statistics                           [系]
│   ├── Mechanical Engineering                             [系]
│   └── Physics & Astronomy                                [系]
└── School of Graduate Studies                             [学院]
    └── Interdisciplinary oversight (no programs attributed; grad programs roll up to home school)
```

> Source: https://www.umkc.edu/academics/index.html (Schools and Departments list); https://catalog.umkc.edu/colleges-schools/ (canonical college/department listing, 2026-2027 edition).

### 0.3 学历级别明细

| 学位缩写 (canonical) | 中文全称 | UMKC 官方写法 | 层级 | 项目数量 |
|---|---|---|---|------|
| BA | Bachelor of Arts | BA / B.A. | 本科 | 18 |
| BA*(Elementary Ed) | Bachelor of Arts in Elementary Education | BA* Elementary Ed | 本科 | 1 |
| BAS | Bachelor of Applied Science | BAS | 本科 | 1 |
| BBA | Bachelor of Business Administration | BBA | 本科 | 11 |
| BFA | Bachelor of Fine Arts | BFA | 本科 | 1 |
| BIT | Bachelor of Information Technology | BIT | 本科 | 2 |
| BLA | Bachelor of Liberal Arts | BLA | 本科 | 1 |
| BM | Bachelor of Music | BM | 本科 | 6 |
| BME | Bachelor of Mechanical Engineering | BME | 本科 | 1 |
| BS | Bachelor of Science | BS / B.S. | 本科 | 12 |
| BSCE | Bachelor of Science in Civil Engineering | BSCE | 本科 | 1 |
| BSDH | Bachelor of Science in Dental Hygiene | BSDH | 本科 | 1 |
| BSEE | Bachelor of Science in Electrical Engineering | BSEE | 本科 | 1 |
| BSME | Bachelor of Science in Mechanical Engineering | BSME | 本科 | 1 |
| Minor | Minor (辅修) | Minor | 本科 | 55 |
| RN-BSN | RN to BSN (Bachelor of Science in Nursing, completion) | RN-BSN | 本科 | 1 |
| UGCRT | Undergraduate Certificate | UG Cert | 本科 | 10 |
| BBA-MPA | BBA / MPA combined degree | BBA-MPA | 研究生 | 1 |
| BSN-DNP | Bachelor to DNP (BSN to DNP) | BSN-DNP | 研究生 | 1 |
| DDS | Doctor of Dental Surgery | DDS | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | DNP | 研究生 | 1 |
| EdSp | Education Specialist | EdSp | 研究生 | 1 |
| GRCT | Graduate Certificate | Grad Cert | 研究生 | 37 |
| JD | Juris Doctor | JD | 研究生 | 1 |
| LLM | Master of Laws | LLM | 研究生 | 1 |
| MA | Master of Arts | MA | 研究生 | 14 |
| MAT | Master of Arts in Teaching | MAT | 研究生 | 1 |
| MBA | Master of Business Administration | MBA | 研究生 | 1 |
| MD | Doctor of Medicine | MD | 研究生 | 1 |
| MFA | Master of Fine Arts | MFA | 研究生 | 7 |
| MM | Master of Music | MM | 研究生 | 9 |
| MME | Master of Music Education | MME | 研究生 | 1 |
| MMS | Master of Music Studies | MMS | 研究生 | 1 |
| MS | Master of Science | MS | 研究生 | 20 |
| MSN | Master of Science in Nursing | MSN | 研究生 | 1 |
| MSN-DNP | Dual MSN/DNP | MSN-DNP | 研究生 | 1 |
| MSW | Master of Social Work | MSW | 研究生 | 1 |
| PhD | Doctor of Philosophy | PhD | 研究生 | 6 |
| PharmD | Doctor of Pharmacy | PharmD | 研究生 | 1 |

> Source: https://catalog.umkc.edu/academic-programs/ (Degree Programs table, 2026-2027 edition; cross-referenced with https://programs.umkc.edu/ Type field).

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BAS | BArch | BFA | BM | BME | BSCE | BSEE | BSME | BSDH | BIT | BLA | RN-BSN | BSN-DNP | BA*(Elementary Ed) | Minor | UGCRT | MA | MS | MBA | MFA | MM | MME | MMS | MSW | MSN | MSN-DNP | MAT | EdSp | JD | LLM | MD | DDS | DNP | PharmD | PhD | PhD*#(Education) | MS*(thesis) | BBA-MPA | GRCT | Post-MSN GRCT | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry W. Bloch School of Management | 0 | 1 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 | 0 | **27** |
| UMKC Conservatory | 2 | 0 | 0 | 0 | 0 | 1 | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 2 | 0 | 0 | 2 | 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | **35** |
| School of Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | **7** |
| School of Education, Social Work and Psychological Sciences | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | **18** |
| School of Humanities and Social Sciences | 12 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 28 | 4 | 4 | 1 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | **58** |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | **7** |
| School of Nursing and Health Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 7 | **15** |
| School of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | **3** |
| School of Science and Engineering | 2 | 11 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 18 | 2 | 1 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 | 0 | **58** |
| School of Graduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 0 | **5** |
| **合计** | **18** | **12** | **11** | **1** | **1** | **1** | **6** | **1** | **1** | **1** | **1** | **1** | **2** | **1** | **1** | **1** | **1** | **55** | **10** | **14** | **20** | **1** | **7** | **9** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **5** | **1** | **1** | **1** | **30** | **7** | **235** |

> Reconciliation: row totals = column totals = grand total = 235 (= 235 leaves). Each leaf in §1 and §2 appears once below; row totals sum to 235. If this row total differs from the count in §0.1 or from the sum of rows in §1+§2, an extraction was lost.

## 1. Undergraduate Education

### 1.1 College / school architecture

UMKC houses 11 schools; 10 schools grant undergraduate degrees (the School of Graduate Studies is grad-only; the School of Law grants only the JD and LLM). Undergraduates are admitted through `https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/` (first-time college students) or `https://www.umkc.edu/transfer/index.html` (transfers), with the umbrella portal at `https://futureroo.umkc.edu/apply/`. Per-school structure is shown above in Section 0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Henry W. Bloch School of Management
###### BS
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Accounting | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-science-accounting/ |

###### BBA
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Business Administration (Analytics and Business Intelligence Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/analytics/ |
| 2 | Business Administration (Entrepreneurship and Innovation Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/entrepreneurship/ |
| 3 | Business Administration (Finance Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/finance/ |
| 4 | Business Administration (Health Administration Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/health-administration/ |
| 5 | Business Administration (Human Resources Management & Leadership Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/management/ |
| 6 | Business Administration (Marketing Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/marketing/ |
| 7 | Business Administration (Nonprofit Management Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/nonprofit/ |
| 8 | Business Administration (Real Estate Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/real-estate/ |
| 9 | Business Administration (Risk Management & Insurance Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/risk-management-insurance/ |
| 10 | Business Administration (Sports Management Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/sports-management/ |
| 11 | Business Administration (Supply Chain Management Emphasis) | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/bachelor-of-business-administration/supply-chain/ |

###### Minor
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Business Administration | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/business-administration-minors/ |
| 2 | Entrepreneurship | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/business-administration-minors/ |

###### UGCRT
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Technology Innovation & Management | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/ug-certificate-tim/ |

#### UMKC Conservatory
###### BA
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Music | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-arts/ |
| 2 | Music (Music Therapy Emphasis) | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-arts-music-therapy/ |

###### BFA
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Dance | https://catalog.umkc.edu/colleges-schools/conservatory/dance/ |

###### BM
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Jazz Studies | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-jazz-studies/ |
| 2 | Music Composition | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-composition/ |
| 3 | Music Performance (Piano Emphasis) | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-performance-piano/ |
| 4 | Music Performance (Voice Emphasis) | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-performance-voice/ |
| 5 | Music Performance-Wind, Strings, Percussion | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-performance-wind-strings-percussion/ |
| 6 | Music Theory | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-theory/ |

###### BME
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Music Education | https://catalog.umkc.edu/colleges-schools/conservatory/music/undergraduate/bachelor-of-music-education/ |

###### Minor
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Integrated Performing Arts | https://catalog.umkc.edu/colleges-schools/conservatory/integrated-performing-arts-minor/ |
| 2 | Theatre | https://catalog.umkc.edu/colleges-schools/conservatory/theatre/minor/ |

###### UGCRT
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Arts Entrepreneurship | https://catalog.umkc.edu/colleges-schools/conservatory/arts-entreprenuership-ug-certificate/ |
| 2 | Holistic Wellness in the Performing Arts | https://catalog.umkc.edu/colleges-schools/conservatory/holistic-wellness-performing-arts-ug-certificate/ |
| 3 | Musical Theatre | https://catalog.umkc.edu/colleges-schools/conservatory/musical-theatre-ug-certificate/ |

#### School of Dentistry
###### BSDH
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Dental Hygiene | https://catalog.umkc.edu/colleges-schools/dentistry/division-of-dental-hygiene/bachelor-of-science-dental-hygiene/ |

#### School of Humanities and Social Sciences
###### BA
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Communication (Digital Journalism and Media Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/digital-journalism-media-communication-ba-emphasis/ |
| 2 | Communication (Professional Communication Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/professional-communication-ba-emphasis/ |
| 3 | Communication (Strategic Communication Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/strategic-communication-ba-emphasis/ |
| 4 | English (American Studies) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/american-literary-and-cultural-studies/ |
| 5 | English (Classical, Medieval, and Early Modern Literature) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/classical-medieval-early-modern-literature-track/ |
| 6 | English (Rhetoric and Writing) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/language-rhetoric-track/ |
| 7 | Film and Media Arts | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/bachelor-of-arts-film-and-media-arts/ |
| 8 | Languages & Literatures (Classical Languages & Culture) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/bachelor-of-arts-languages-literatures/classical/ |
| 9 | Languages & Literatures (French Language & Literature) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/bachelor-of-arts-languages-literatures/french/ |
| 10 | Languages & Literatures (International Studies) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/bachelor-of-arts-languages-literatures/international-studies/ |
| 11 | Languages & Literatures (Spanish Language & Literature) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/bachelor-of-arts-languages-literatures/spanish/ |
| 12 | Sociology (Cultural Anthropology) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/sociology-anthropology/bachelor-of-arts-sociology/cultural-anthropology/ |

###### BAS
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Applied Science | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/bachelor-applied-science/ |

###### BLA
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Liberal Arts | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/bachelor-liberal-arts/ |

###### Minor
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Anthropology | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/sociology-anthropology/anthropology-minor/ |
| 2 | Applied Linguistics | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/minor-applied-linguistics/ |
| 3 | Art History | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/art-history-minor/ |
| 4 | Bioethics and Medical Humanities | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-bioethics-medical-humanities/ |
| 5 | Classical and Ancient Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/classical-ancient-studies-program/classical-ancient-studies-minor/ |
| 6 | Communication | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/minor-communication-studies/ |
| 7 | Communication (Professional) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/minor-professional-communication/ |
| 8 | Criminal Justice and Criminology | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/criminal-justice-criminology/minor-criminal-justice-criminology/ |
| 9 | Digital and Public Humanities | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/minor-digital-humanities/ |
| 10 | Economics | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/economics/minor/ |
| 11 | English | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-language-literature/ |
| 12 | English (Creative Writing) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-creative-writing/ |
| 13 | English Language and Literature | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-language-literature/ |
| 14 | English Manuscript, Print Culture, and Editing | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-manuscript-print-culture-editing/ |
| 15 | English Writing | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-writing/ |
| 16 | Film | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/film-studies-minor/ |
| 17 | French | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/minor-french-german-spanish-classics/ |
| 18 | German Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/german-studies-minor/ |
| 19 | History | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/history/minor-history/ |
| 20 | International Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-international-studies/ |
| 21 | Media, Art & Design | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/minor-mad/ |
| 22 | Medieval and Early Modern Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/medieval-early-modern-studies/minor/ |
| 23 | Philosophy | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-philosophy/ |
| 24 | Political Science | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-political-science/ |
| 25 | Race, Ethnic, and Gender Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/regs/regs-minor/ |
| 26 | Sociology | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/sociology-anthropology/sociology-minor/ |
| 27 | Spanish | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/minor-french-german-spanish-classics/ |
| 28 | Studio Art | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/studio-art-minor/ |

###### UGCRT
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Ethics | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/undergraduate-certificate-program-ethics/ |
| 2 | Museum Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/ug-cert_museum_studies/ |
| 3 | Podcasting | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/ug-cert_podcasting/ |
| 4 | Writing, Editing and Publishing | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/ug-cert_writing_editing_publishing/ |

#### School of Science and Engineering
###### BA
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Mathematics & Statistics | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/ba-mathematics-statistics/ |
| 2 | Urban Planning & Design | https://catalog.umkc.edu/colleges-schools/science-engineering/architecture-urban-planning-design/urban-planning-design-ba/ |

###### BS
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Biology (Bioinformatics Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/bachelor-of-science-bioinformatics/ |
| 2 | Biology (Biomedical Sciences Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/bachelor-of-science-biomedical-sciences/ |
| 3 | Biology (Biotechnology Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/bachelor-of-science-biotechnology/ |
| 4 | Biology (Clinical Laboratory Science Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/bachelor-of-science-clinical-laboratory-science/ |
| 5 | Biomedical Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/biomedical/bachelor-of-science-biomedical-engineering/ |
| 6 | Computer Science (Artificial Intelligence) | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/bachelor-of-science-computer-science-artificial-intelligence/ |
| 7 | Computer Science (Cybersecurity Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/bachelor-of-science-computer-science-cybersecurity/ |
| 8 | Earth and Environmental Science (Environmental Science Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/bachelor-of-science-environmental-science/ |
| 9 | Earth and Environmental Science (Geology Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/bachelor-of-science-geology/ |
| 10 | Earth and Environmental Science (Physical Geography Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/bachelor-of-science-geography/ |
| 11 | Physics (Astronomy) | https://catalog.umkc.edu/colleges-schools/science-engineering/physics-astronomy/physics-bs-astro-emph/ |

###### BSCE
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Civil Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/civil-engineering/bachelor-of-science-civil-engineering/ |

###### BSEE
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Electrical and Computer Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/electrical-computer-engineering/bachelor-of-science-electrical-computer-engineering/ |

###### BSME
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Mechanical Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/mechanical-engineering/bachelor-of-science-mechanical-engineering/ |

###### BIT
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Information Technology | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/bachelor-of-information-technology/ |
| 2 | Information Technology (Cybersecurity Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/bachelor-of-information-technology-cybersecurity/ |

###### Minor
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Actuarial Science | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-actuarial-science/ |
| 2 | Artificial Intelligence | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/minor-artificial-intelligence/ |
| 3 | Astronomy | https://catalog.umkc.edu/colleges-schools/science-engineering/physics-astronomy/astronomy-minor/ |
| 4 | Biology | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/minor-biology/ |
| 5 | Chemistry | https://catalog.umkc.edu/colleges-schools/science-engineering/chemistry/minor/ |
| 6 | Computer Science | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/minor-computer-science/ |
| 7 | Data Science & Analytics | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-data-analytics/ |
| 8 | Environmental Communications | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-environmental-communications/ |
| 9 | Environmental Studies | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-environmental-studies/ |
| 10 | Environmental Sustainability | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-environmental-sustainability/ |
| 11 | Geology | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-geology/ |
| 12 | Geospatial Science | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/geospatial-science/ |
| 13 | Material Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/interdisciplinary-minor-mse/ |
| 14 | Mathematics | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-mathematics/ |
| 15 | Physics | https://catalog.umkc.edu/colleges-schools/science-engineering/physics-astronomy/physics-minor/ |
| 16 | Statistics | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-statistics/ |
| 17 | Sustainable Energy Technologies | https://catalog.umkc.edu/colleges-schools/science-engineering/interdisciplinary-minor-set/ |
| 18 | Urban Studies | https://catalog.umkc.edu/colleges-schools/science-engineering/architecture-urban-planning-design/minor-urban-studies/ |

###### UGCRT
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Controlled Environment Agriculture | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/undergraduate-certificate-program-cea/ |
| 2 | Geographic Information Systems | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/undergraduate-certificate-program-gis/ |

###### B.Arch.
| # | 专业 / Major | URL |
|---|---|---|
| 1 | Architecture | https://catalog.umkc.edu/colleges-schools/science-engineering/architecture-urban-planning-design/architecture-major/index.html |

### 1.3 跨学院本科项目 (Interdisciplinary / cross-college undergraduate programs)

UMKC offers several joint degrees and accelerated programs that span more than one school:

| # | 项目 | 涉及的学院 | URL |
|---|---|---|---|
| 1 | Six-Year B.A./M.D. (pre-med pipeline) | Humanities & Social Sciences → School of Medicine | https://programs.umkc.edu/undergraduate/school-of-medicine/six-year-ba-md.php |
| 2 | B.S. Mathematics & Statistics / M.S. Mathematics (accelerated) | School of Science and Engineering | https://programs.umkc.edu/graduate/school-of-science-and-engineering/bs-ms-mathematics-statistics-and-mathematics.php |
| 3 | B.S. Biology / M.S. Cellular and Molecular Biology (accelerated) | School of Science and Engineering → School of Medicine | https://programs.umkc.edu/graduate/school-of-science-and-engineering/bs-ms-biology-and-cellular-and-molecular-biology.php |
| 4 | B.S. Electrical and Computer Engineering / M.S. Electrical Engineering (accelerated) | School of Science and Engineering | https://programs.umkc.edu/graduate/school-of-science-and-engineering/bs-ece-ms-ee.php |
| 5 | English — Accelerated B.A./M.A. | School of Humanities and Social Sciences | https://programs.umkc.edu/graduate/school-of-humanities-and-social-sciences/ba-ma-english.php |
| 6 | History — Accelerated B.A./M.A. | School of Humanities and Social Sciences | https://programs.umkc.edu/graduate/school-of-humanities-and-social-sciences/ba-ma-history.php |
| 7 | Six-Year B.A./J.D. (pre-law) | School of Humanities and Social Sciences → School of Law | https://www.umkc.edu/academics/index.html |

> Source: https://programs.umkc.edu/ (Program Finder; cross-listed joint-degree entries).

### 1.4 辅修专业完整列表 (Minors — complete list)

UMKC offers 55 undergraduate minors across the colleges:

| # | Minor | Home School | URL |
|---|---|---|---|
| 1 | Education | Education, Social Work and Psychological Sciences | https://catalog.umkc.edu/colleges-schools/educ-socwk-psychological-sciences/teacher-education/minor-education-studies/ |
| 2 | Exercise Science | Education, Social Work and Psychological Sciences | https://catalog.umkc.edu/colleges-schools/educ-socwk-psychological-sciences/educational-leadership-policy-foundations/minor-exercise-science/ |
| 3 | Psychology | Education, Social Work and Psychological Sciences | https://catalog.umkc.edu/colleges-schools/educ-socwk-psychological-sciences/psychology/psychology-minor/ |
| 4 | Business Administration | Henry W. Bloch School of Management | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/business-administration-minors/ |
| 5 | Entrepreneurship | Henry W. Bloch School of Management | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/undergraduate-programs/business-administration-minors/ |
| 6 | Health Sciences | Nursing and Health Studies | https://catalog.umkc.edu/colleges-schools/nursing-health-studies/minor-health-science/ |
| 7 | Public Health | Nursing and Health Studies | https://catalog.umkc.edu/colleges-schools/nursing-health-studies/minor-public-health/ |
| 8 | Anthropology | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/sociology-anthropology/anthropology-minor/ |
| 9 | Applied Linguistics | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/minor-applied-linguistics/ |
| 10 | Art History | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/art-history-minor/ |
| 11 | Bioethics and Medical Humanities | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-bioethics-medical-humanities/ |
| 12 | Classical and Ancient Studies | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/classical-ancient-studies-program/classical-ancient-studies-minor/ |
| 13 | Communication | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/minor-communication-studies/ |
| 14 | Communication (Professional) | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/communication-journalism/minor-professional-communication/ |
| 15 | Criminal Justice and Criminology | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/criminal-justice-criminology/minor-criminal-justice-criminology/ |
| 16 | Digital and Public Humanities | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/minor-digital-humanities/ |
| 17 | Economics | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/economics/minor/ |
| 18 | English | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-language-literature/ |
| 19 | English (Creative Writing) | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-creative-writing/ |
| 20 | English Language and Literature | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-language-literature/ |
| 21 | English Manuscript, Print Culture, and Editing | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-manuscript-print-culture-editing/ |
| 22 | English Writing | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/minor-writing/ |
| 23 | Film | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/film-studies-minor/ |
| 24 | French | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/minor-french-german-spanish-classics/ |
| 25 | German Studies | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/german-studies-minor/ |
| 26 | History | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/history/minor-history/ |
| 27 | International Studies | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-international-studies/ |
| 28 | Media, Art & Design | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/minor-mad/ |
| 29 | Medieval and Early Modern Studies | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/medieval-early-modern-studies/minor/ |
| 30 | Philosophy | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-philosophy/ |
| 31 | Political Science | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/political-science-philosophy/minor-political-science/ |
| 32 | Race, Ethnic, and Gender Studies | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/regs/regs-minor/ |
| 33 | Sociology | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/sociology-anthropology/sociology-minor/ |
| 34 | Spanish | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/minor-french-german-spanish-classics/ |
| 35 | Studio Art | School of Humanities and Social Sciences | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/media-art-design/studio-art-minor/ |
| 36 | Actuarial Science | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-actuarial-science/ |
| 37 | Artificial Intelligence | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/minor-artificial-intelligence/ |
| 38 | Astronomy | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/physics-astronomy/astronomy-minor/ |
| 39 | Biology | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/minor-biology/ |
| 40 | Chemistry | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/chemistry/minor/ |
| 41 | Computer Science | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/minor-computer-science/ |
| 42 | Data Science & Analytics | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-data-analytics/ |
| 43 | Environmental Communications | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-environmental-communications/ |
| 44 | Environmental Studies | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-environmental-studies/ |
| 45 | Environmental Sustainability | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-environmental-sustainability/ |
| 46 | Geology | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/minor-geology/ |
| 47 | Geospatial Science | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/geospatial-science/ |
| 48 | Material Science and Engineering | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/interdisciplinary-minor-mse/ |
| 49 | Mathematics | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-mathematics/ |
| 50 | Physics | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/physics-astronomy/physics-minor/ |
| 51 | Statistics | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/minor-statistics/ |
| 52 | Sustainable Energy Technologies | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/interdisciplinary-minor-set/ |
| 53 | Urban Studies | School of Science and Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/architecture-urban-planning-design/minor-urban-studies/ |
| 54 | Integrated Performing Arts | UMKC Conservatory | https://catalog.umkc.edu/colleges-schools/conservatory/integrated-performing-arts-minor/ |
| 55 | Theatre | UMKC Conservatory | https://catalog.umkc.edu/colleges-schools/conservatory/theatre/minor/ |

### 1.5 校级通识要求 (General Education / Institute-wide requirements)

UMKC undergrads complete the **UMKC General Education Core** (called "General Education" — 30 credit hours spanning English, Math, Communications, US/MO Constitution, and distribution areas). Outcome:

* Total credits for most bachelor degrees: **120 semester hours minimum**.
* Required categories: Written Communication (6cr), Math/Quantitative Reasoning (3cr), Oral Communication (3cr), US/MO Constitution (3cr), Humanities (9cr), Natural/Physical Sciences (7cr), Social & Behavioral Sciences (9cr).
* Detailed requirements: https://catalog.umkc.edu/undergraduate-academic-regulations-information/general-education-requirements/
* Honors track: **University Honors Program** — https://www.umkc.edu/honors/index.html (separate admission; requires application essay + recommendation).

> Source: https://catalog.umkc.edu/undergraduate-academic-regulations-information/ and https://catalog.umkc.edu/course-offerings/undergraduate/general-education/ (2026-2027 edition, capture 2026-07-07).

## 2. Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Henry W. Bloch School of Management
###### MS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Accounting | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/master-of-science-accounting/ |
| 2 | Entrepreneurial Real Estate | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/master-of-entrepreneurial-real-estate/ |
| 3 | Finance | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/master-of-science-finance/ |

###### MBA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Business Administration | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/master-of-business-administration/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Business Analytics | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-business-analytics/ |
| 2 | Commercial Real Estate | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-commercial-real-estate/ |
| 3 | Health Leadership | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-health-leadership/ |
| 4 | Nonprofit Management & Innovation | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-nonprofit-management-innovation/ |
| 5 | Public Policy Analysis | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-public-policy-analysis/ |
| 6 | Technology Innovation & Management | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-tim/ |
| 7 | Urban Policy and Management | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/grad-cert-urban-policy-admin/ |

###### BBA-MPA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Public Administration | https://catalog.umkc.edu/colleges-schools/henry-w-bloch-management/graduate-programs/master-of-public-administration/ |

#### UMKC Conservatory
###### MA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Music | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-arts/music/ |
| 2 | Music (Music Therapy Emphasis) | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-arts/music-therapy/ |

###### MFA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Theatre: Acting | https://catalog.umkc.edu/colleges-schools/conservatory/theatre/master-of-fine-arts-acting-directing/ |
| 2 | Theatre: Design & Technology | https://catalog.umkc.edu/colleges-schools/conservatory/theatre/master-of-fine-arts-design-technology/ |

###### MM
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Conducting | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/conducting/ |
| 2 | Music Composition | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/composition/ |
| 3 | Music Performance-Collaborative Piano | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/performance-collaborative-piano/ |
| 4 | Music Performance-Jazz Studies | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/performance-jazz/ |
| 5 | Music Performance-Orchestral | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/performance-orchestral-guitar/ |
| 6 | Music Performance-Pedagogy | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/performance-pedagogy/ |
| 7 | Music Performance-Woodwinds | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/performance-woodwind/ |
| 8 | Music Theory | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/music-theory/ |
| 9 | Musicology | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music/musicology/ |

###### MME
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Music Education | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/master-of-music-education/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Artist's Certificate | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/graduate-certificates/artists-certificate/ |
| 2 | Collaborative Piano | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/graduate-certificates/collaborative-piano-certificate/ |
| 3 | Music Performance (Voice Emphasis) | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/graduate-certificates/performers-certificate/ |
| 4 | Music Performance-Instrumental | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/graduate-certificates/performers-certificate/ |
| 5 | Music Performance-Keyboard | https://catalog.umkc.edu/colleges-schools/conservatory/music/graduate/graduate-certificates/performers-certificate/ |
| 6 | Performing Arts Management | https://catalog.umkc.edu/colleges-schools/conservatory/grad-cert-performing-arts-mgmt/ |

#### School of Dentistry
###### MS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Oral & Craniofacial Sciences | https://catalog.umkc.edu/colleges-schools/dentistry/oral-craniofacial-sciences/master-of-science-oral-craniofacial-sciences/ |

###### DDS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Dentistry | https://catalog.umkc.edu/colleges-schools/dentistry/doctor-of-dental-surgery-program/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Dentistry-Advanced Education in General Dentistry | https://catalog.umkc.edu/colleges-schools/dentistry/advanced-education-programs/graduate-certificate-advanced-education-in-general-dentistry/ |
| 2 | Endodontics | https://catalog.umkc.edu/colleges-schools/dentistry/advanced-education-programs/graduate-certificate-endodontics/ |
| 3 | Orthodontics & Dentofacial Orthopedics | https://catalog.umkc.edu/colleges-schools/dentistry/advanced-education-programs/graduate-certificate-orthodontics-dentofacial-orthopedics/ |
| 4 | Periodontics | https://catalog.umkc.edu/colleges-schools/dentistry/advanced-education-programs/graduate-certificate-periodontics/ |

#### School of Humanities and Social Sciences
###### MA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Economics | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/economics/master-of-arts-economics/ |
| 2 | English | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/master-of-arts-english/ |
| 3 | History | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/history/master-of-arts-history/ |
| 4 | Romance Language and Literature | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/world-languages-cultures/master-of-arts-romance-languages/ |

###### MS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Criminal Justice and Criminology | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/criminal-justice-criminology/master-of-science-criminal-justice-criminology/ |

###### MFA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | English Creative Writing and Media Arts (Creative Nonfiction Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/master-of-fine-arts-creative-writing-media-arts/creative-nonfiction/ |
| 2 | English Creative Writing and Media Arts (Fiction Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/master-of-fine-arts-creative-writing-media-arts/fiction/ |
| 3 | English Creative Writing and Media Arts (Playwriting Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/master-of-fine-arts-creative-writing-media-arts/playwriting/ |
| 4 | English Creative Writing and Media Arts (Poetry Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/master-of-fine-arts-creative-writing-media-arts/poetry/ |
| 5 | English Creative Writing and Media Arts (Screenwriting Emphasis) | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/master-of-fine-arts-creative-writing-media-arts/screenwriting/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | English Language and Literature | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/english-language-literature/gr_crt_english_language_literature/ |
| 2 | Medieval and Early Modern Studies | https://catalog.umkc.edu/colleges-schools/humanities-social-sciences/academic-departments-programs/medieval-early-modern-studies/graduate-certificate/ |

#### School of Law
###### JD
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Law | https://catalog.umkc.edu/colleges-schools/law/juris-doctor-degree/ |

###### LLM
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Taxation | https://catalog.umkc.edu/colleges-schools/law/master-of-laws-degree/curriculum-master-of-laws-taxation/ |

#### School of Medicine
###### MS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Anesthesia | https://catalog.umkc.edu/colleges-schools/medicine/graduate-programs/master-of-science-anesthesia-program/ |
| 2 | Bioinformatics | https://catalog.umkc.edu/colleges-schools/medicine/graduate-programs/master-of-science-program-bioinformatics/ |

###### MMS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Physician Assistant | https://catalog.umkc.edu/colleges-schools/medicine/graduate-programs/master-of-medical-science-physician-assistant/ |

###### MD
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Medicine | https://catalog.umkc.edu/colleges-schools/medicine/#medicaltext |

###### PhD
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Biomedical and Health Informatics | https://catalog.umkc.edu/colleges-schools/graduate-studies/biomedical-health-informatics/phd/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Clinical Research | https://catalog.umkc.edu/colleges-schools/medicine/graduate-programs/graduate-certificate-clinical-research/ |
| 2 | Health Professions Education | https://catalog.umkc.edu/colleges-schools/medicine/graduate-programs/graduate-certificate-health-professions-education/ |

#### School of Pharmacy
###### PharmD
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Pharmacy | https://catalog.umkc.edu/colleges-schools/pharmacy-home-page/doctor-of-pharmacy/ |

###### PhD
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Pharmacology | https://catalog.umkc.edu/colleges-schools/graduate-studies/pharmacology/phd/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Pharmaceutical Sciences | https://catalog.umkc.edu/colleges-schools/graduate-studies/pharmaceutical-sciences-grd-certificate/ |

#### School of Science and Engineering
###### MA
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Biology | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/master-of-arts-biology/ |

###### MS
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Artificial Intelligence | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/master-of-science-artificial-intelligence/ |
| 2 | Biomedical Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/biomedical/master-of-science-biomedical-engineering/ |
| 3 | Cellular and Molecular Biology | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/master-of-science-cellular-molecular-biology/ |
| 4 | Cellular and Molecular Biology (Bioinformatics Emphasis) | https://catalog.umkc.edu/colleges-schools/science-engineering/biology/master-of-science-cellular-molecular-biology/ |
| 5 | Civil Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/civil-engineering/master-of-science-civil-engineering/ |
| 6 | Computer Science | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/master-of-science-computer-science/ |
| 7 | Data Science & Analytics | https://catalog.umkc.edu/colleges-schools/science-engineering/computer-science/master-of-science-data-science-analytics/ |
| 8 | Electrical and Computer Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/electrical-computer-engineering/master-of-science-electrical-engineering/ |
| 9 | Environmental and Urban Geosciences | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/master-of-science-environmental-urban-geosciences/ |
| 10 | Mathematics | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/master-of-science-mathematics/ |
| 11 | Mechanical Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/mechanical-engineering/master-of-science-mechanical-engineering/ |
| 12 | Physics | https://catalog.umkc.edu/colleges-schools/science-engineering/physics-astronomy/master-of-science-physics/ |
| 13 | Statistics | https://catalog.umkc.edu/colleges-schools/science-engineering/mathematics-statistics/master-of-science-statistics/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Engineering and Construction Project Management | https://catalog.umkc.edu/colleges-schools/science-engineering/civil-engineering/engineering-construction-project-managment-certificate/ |
| 2 | Geographic Information Systems | https://catalog.umkc.edu/colleges-schools/science-engineering/ees/graduate-certificate-program-gis/ |
| 3 | Historic Preservation | https://catalog.umkc.edu/colleges-schools/science-engineering/architecture-urban-planning-design/historic-preservation-grad-cert/ |
| 4 | Structural Engineering | https://catalog.umkc.edu/colleges-schools/science-engineering/civil-engineering/grct_structural20engineering/ |

###### MS*(thesis)
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Chemistry | https://catalog.umkc.edu/colleges-schools/science-engineering/chemistry/master-of-science-thesis-based/ |

#### School of Graduate Studies
###### PhD
| # | 项目 / Program | URL |
|---|---|---|
| 1 | Cell Biology and Biophysics | https://catalog.umkc.edu/colleges-schools/graduate-studies/cell-biology-biophysics/phd/ |
| 2 | Molecular Biology and Biochemistry | https://catalog.umkc.edu/colleges-schools/graduate-studies/molecular-biology-biochemistry/phd/ |
| 3 | Multi/Interdisciplinary | https://catalog.umkc.edu/colleges-schools/graduate-studies/interdisciplinary-phd-program/ |

###### GRCT
| # | 项目 / Program | URL |
|---|---|---|
| 1 | College Teaching and Career Preparation | https://catalog.umkc.edu/colleges-schools/graduate-studies/graduate-certificate-college-teaching-career-preparation/ |
| 2 | Interdisciplinary Leadership in Disability Studies | https://catalog.umkc.edu/colleges-schools/graduate-studies/interdisciplinary-leadership-certificate-disability-studies/ |

### 2.2 At least one program's full deep-dive (worked example: M.S. in Accounting — Bloch)

Selected the M.S. in Accounting because it is one of the highest-volume programs at UMKC and the program-detail page on programs.umkc.edu is fully populated:

| Field | Value | URL |
|---|---|---|
| Program name | Accounting (M.S.) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Department | Accounting (within Henry W. Bloch School of Management) | https://bloch.umkc.edu/index.html |
| Degree type | Master of Science | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Standard credit hours | 30 | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Delivery mode | In-person (primarily evening) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Typical program length | 1–4 years | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Typical course load | 1–5 courses/semester | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Application portal | https://futureroo.umkc.edu/apply/ | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Application fee | $45 (domestic) / $75 (international) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Fall start | Apply by Aug. 1 (priority) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Spring start | Apply by Dec. 15 (priority) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Summer start | Apply by May 1 (priority) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| GRE/GMAT policy | Not required for this program (some programs require it, check individual page) | https://www.umkc.edu/admissions/graduate-admissions.html |
| Median salary (Lightcast.io, Accountants & Auditors 13-2011.00) | $81,794/year | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| International English requirement | TOEFL iBT 79 / IELTS 6.5 / PTE 53 / DET 110 / GTEC 1200 (grad baseline; some programs higher) | https://www.umkc.edu/isao/future-students/english-proficiency.html |
| Office | Bloch School of Management, 5108 Cherry Street, Suite 102, Kansas City, MO 64110 | https://bloch.umkc.edu/index.html |
| Phone | 816-235-2896 | https://bloch.umkc.edu/index.html |

### 2.3 Graduate admissions model

UMKC graduate admissions is **centralized at the Office of Admissions** (volker campus, 5115 Oak Street) for processing, but **decentralized at the school level for academic requirements**: each school sets its own deadlines, GRE/GMAT requirements, materials checklists, and program-specific English proficiency thresholds.

* Central portal: `https://futureroo.umkc.edu/apply/` (single application for all grad programs at UMKC).
* Per-school entry hubs:
  * Bloch: https://bloch.umkc.edu/admissions/graduate.html
  * Conservatory: https://conservatory.umkc.edu/admissions/index.html
  * Dentistry: https://dentistry.umkc.edu/admissions/index.html
  * Education/SESWPS: https://seswps.umkc.edu/admissions/index.html
  * Humanities & Social Sciences: https://shss.umkc.edu/admissions/index.html
  * Law: https://law.umkc.edu/admissions/index.html
  * Medicine: https://med.umkc.edu/admissions/index.html
  * Nursing and Health Studies: https://sonhs.umkc.edu/admissions/index.html
  * Pharmacy: https://pharmacy.umkc.edu/admissions/index.html
  * Science & Engineering: https://sse.umkc.edu/admissions/index.html
* Fee: $45 domestic / $75 international for most programs (some professional programs — Law, Medicine, Dentistry — have higher fees).
* April-15-equivalent honor: UMKC is a CGS member; follow CGS Resolution regarding the April 15th deadline for PhD offers.
* Most programs do NOT require GRE/GMAT (verification required per program page); some professional programs have additional entrance exams (e.g., MCAT for MD, DAT for DDS, LSAT for JD, PCAT for PharmD historically).
* International applicants use the same portal; English proficiency requirements vary per program and are listed per-school.

## 3. Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | Value | Source URL |
|---|---|---|
| Admissions site | https://www.umkc.edu/admissions/ | https://www.umkc.edu/admissions/ |
| Undergrad admissions (main) | https://www.umkc.edu/admissions/undergraduate-admissions.html | https://www.umkc.edu/admissions/undergraduate-admissions.html |
| First-time college students | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html |
| Transfer students | https://www.umkc.edu/transfer/index.html | https://www.umkc.edu/transfer/index.html |
| Application portal | https://futureroo.umkc.edu/apply/ | https://futureroo.umkc.edu/apply/ |
| Application opens | Aug. 1 | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| UG Spring priority deadline | Nov. 15 | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| UG Fall priority deadline (first-time) | Jan. 15 | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| UG Fall rolling deadline | June 15 (final) | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| Transfer students Fall priority | May 1 | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| SAT/ACT policy | Test-optional (recommended but not required). Official scores from high school submitted for placement. | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html |
| Superscore policy | Yes (UMKSC will use highest subscores from multiple test administrations) | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html |
| Application fee | $35 (UG, in-state & out-of-state); fee-waivers accepted (Common App / NACAC) | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html |
| FAFSA priority deadline | Feb. 1 (for maximum aid consideration) | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| On-campus housing contract | December (after admission) | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| Recommendation letters | 1 letter (UG, first-time); varies by school/program | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html |
| Interview policy | Optional (required for some programs: e.g., Conservatory performance) | https://conservatory.umkc.edu/admissions/index.html |
| Transfer pathway | RooMentum 2+2; credit-by-credit review | https://www.umkc.edu/transfer/index.html |
| Early Action / Early Decision | N/A (no restrictive EA/ED option); rolling-admission UG with priority Jan 15 | https://www.umkc.edu/admissions/dates-and-deadlines.html |
| Decision notification | Rolling (typically 4–6 weeks for completed files) | https://www.umkc.edu/admissions/dates-and-deadlines.html |

### 3.2 Undergraduate English proficiency table

UMKC Undergraduate minimum scores (see Section 3.4 for graduate baseline):

| Exam | Minimum | Recommended | Notes |
|---|---|---|---|
| TOEFL iBT (code 6872) | 70 | 80+ | Some academic programs require higher (see Section 3.4) |
| IELTS Academic | 6.0 (5.5 min all bands) | 6.5+ | — |
| Pearson PTE | 48 (44 min all skills) | 53+ | — |
| Duolingo English Test (DET) | 100 (90 min all subscores) | 105+ | — |
| GTEC CBT | 1175 | 1205+ | — |

Exemptions: (1) Citizens of countries where English is the official language (see PDF list); (2) completion of US college Composition I/II with grade C or better; (3) degree or 24+ non-ESL credits from US, Canada, UK, NZ, or AU accredited institutions; (4) successful US-accredited high school completion.

Source: https://www.umkc.edu/isao/future-students/english-proficiency.html (capture 2026-07-07).

### 3.3 Graduate — global rules

| Item | Value | Source |
|---|---|---|
| Application model | Centralized UMKC Apply portal; per-school academic review | https://futureroo.umkc.edu/apply/ |
| Application fee (most programs) | $45 (domestic) / $75 (international) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| Application portal | https://futureroo.umkc.edu/apply/ | https://futureroo.umkc.edu/apply/ |
| TOEFL iBT reporting code | 6872 | https://www.umkc.edu/isao/future-students/english-proficiency.html |
| GRE/GMAT policy | Varies by program (most MS/MA programs do not require GRE; PhD programs often require or recommend; MBA requires GMAT/GRE in some years) | https://www.umkc.edu/admissions/graduate-admissions.html |
| English-test exemption rules | Same as UG: degree from English-speaking accredited institution; 24+ non-ESL credits; or US high school completion | https://www.umkc.edu/isao/future-students/english-proficiency.html |
| Standard application timeline (most MS/MA) | Rolling admissions; priority dates Aug 1 (fall), Dec 15 (spring), May 1 (summer) | https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting |
| CGS membership | UMKC is a CGS member (Council of Graduate Schools); honors CGS April 15 Resolution for PhD offers | https://www.umkc.edu/admissions/graduate-admissions.html |
| International students affairs | International Student Affairs Office (ISAO); https://www.umkc.edu/isao/index.html | https://www.umkc.edu/isao/index.html |
| English proficiency baseline | TOEFL iBT 79; IELTS 6.5; PTE 53; DET 110; GTEC 1200 | https://www.umkc.edu/isao/future-students/english-proficiency.html |

### 3.4 Program-specific English proficiency requirements

Some UMKC academic programs set higher English-proficiency minimums than the university baseline:

| Program / School | TOEFL iBT | IELTS | PTE | DET | GTEC |
|---|---|---|---|---|---|
| Graduate baseline | 79 | 6.5 (6.0 min bands) | 53 | 110 | 1200 |
| Cell & Molecular Biology, IPhD Cell Biology & Biophysics, IPhD Molecular Biology & Biochemistry | 90 | 7.0 (6.5 min bands) | — | 115 | — |
| BS Architectural Studies, BS Urban Planning + Design | 100 | 6.5 (5.0 min bands) | 65 | 110 | 1230 / CBT 1229 |
| Conservatory graduate (MM/MA/MFA) | 85 | 6.5 (5.5 min bands) | 53 | 105 | 1230 / CBT 1229 |
| Conservatory DMA (Doctor of Musical Arts) | 95 | 7.0 (5.5 min bands) | 65 | 115 | 1256 / CBT 1260 |
| Conservatory UG (Dance, Music, Music Ed, Music Performance, Music Theory) | 80 | 6.0 (5.5 min bands) | 53 | 105 | 1205 / CBT 1200 |
| Clinical Psychology PhD (SESWPS) | 85 (listening 21, speaking 24) | 6.5 (listening 6.5, speaking 7.0) | 56 | 115 | 1230 / CBT 1229 |
| Dental Hygiene | 84 | 6.5 (5.5 min bands) | 56 | 110 | 1230 / CBT 1229 |
| Conservatory Artist's Certificate / Performer's Certificate | 79 | 6.0 (5.5 min bands) | 53 | 100 | 1205 / CBT 1200 |

Source: https://www.umkc.edu/isao/future-students/english-proficiency.html (capture 2026-07-07). Note: humanities and social sciences programs generally follow the standard grad baseline (TOEFL iBT 79). Science & Engineering MS/PhD in CS, Data Science, Physics, Chemistry, Engineering may be exempt for degrees from Bangladesh, Egypt, India, Pakistan, Sri Lanka, Turkey. Source: same English proficiency page.

## 4. Costs & Financial Aid

### 4.1 Undergraduate cost (2025-2026 academic year, line-itemized)

UMKC has a **3-tier residency pricing** structure: (1) Resident (Missouri + Kansas + Roo Nation scholars); (2) Heartland Rate (15 Midwestern states); (3) Nonresident. Below: representative figures from the 2025-2026 cost-of-attendance estimates.

#### Base / General Education coursework (Resident rate)

| Expense item | Living with parent | Living off campus | Living on campus | Source |
|---|---|---|---|---|
| Tuition and fees | $13,216 | $13,216 | $13,216 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Housing and food | $6,164 | $14,509 | (Residential Life: $15,622) | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Books and supplies | $786 | $786 | $786 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Transportation | $2,149 | $2,149 | $1,075 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Personal expenses | $4,263 | $4,263 | $4,263 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| **Estimated cost of attendance** | **$26,578** | **$34,923** | **$34,962** | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |

#### Per-school tuition variance (Resident rate, on-campus students) — 2025-2026

| School / program cohort | Tuition & Fees (on campus) | Total COA (on campus) | Source |
|---|---|---|---|
| Base / General Ed | $13,216 | $34,962 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Bloch School (Business) | $15,590 | $37,336 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| UMKC Conservatory | $14,666 | $36,412 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Dental Hygiene (34 cr-hr basis) | $19,134 | $41,994 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Education | $13,694 | $35,440 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Health Studies | $15,408 | $37,154 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| Nursing (BSN) | $15,408 | $37,154 | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |

> Detailed per-school tables (including each of Bloch, Conservatory, Education, Health Studies, Nursing, S&E programs) are listed in the official cost-estimates pages.

#### Heartland Rate (15 Midwestern states) & Nonresident Rate

For up-to-date numbers, consult the three live pages:

* Resident: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html
* Heartland: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/heartland-rates.html
* Nonresident: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/nonresident-rates.html

> Heartland states: Arkansas, Illinois, Indiana, Iowa, Kentucky, Michigan, Minnesota, Nebraska, North Dakota, Ohio, Oklahoma, South Dakota, Tennessee, Texas, Wisconsin.

### 4.2 Graduate cost & international cost

#### Domestic graduate cost

See https://www.umkc.edu/financial-aid/affordability/graduate-cost-estimate.html for line-itemized tuition & fees by program. Per-credit-hour graduate tuition varies by program; Law School and School of Medicine have program-specific pages:

* Law School: https://www.umkc.edu/financial-aid/affordability/law-cost-estimate.html
* Medicine: https://www.umkc.edu/financial-aid/affordability/medicine-cost-estimate.html

#### International student F-1/J-1 cost estimates — 2026-2027 academic year (FULL-TIME ENROLLMENT)

| Program | Tuition & Fees | Living | Other | Total COA (I-20/DS-2019) | Source |
|---|---|---|---|---|---|
| UG — Nursing | $40,716 | $20,650 | $3,984 | **$65,350** | https://www.umkc.edu/isao/future-students/affordability-and-funding.html |
| UG — Computer Science, Engineering, Information Technology | $38,961 | $20,650 | $3,984 | **$63,595** | https://www.umkc.edu/isao/future-students/affordability-and-funding.html |
| UG — Dental Hygiene | $38,343 | $20,650 | $3,984 | **$62,977** | https://www.umkc.edu/isao/future-students/affordability-and-funding.html |
| UG — Other bachelor's programs | $37,821 | $20,650 | $3,984 | **$62,455** | https://www.umkc.edu/isao/future-students/affordability-and-funding.html |
| UG — Non-degree (12 credits/semester) | $28,334 | $20,650 | $3,984 | **$52,968** | https://www.umkc.edu/isao/future-students/affordability-and-funding.html |
| Grad — Master's and doctorate | $26,597 | $20,650 | $3,984 | **$51,231** | https://www.umkc.edu/isao/future-students/affordability-and-funding.html |

> Professional program (Law, Medicine, Pharmacy, Dentistry, etc.) fees are additional; see school-specific pages for I-20 cost breakdowns.

> Dependent costs: $6,250/yr per F-2 dependent (spouse or each child); J-2: $9,250 spouse + $9,250 first child + $6,250 each additional. Source: https://www.umkc.edu/isao/future-students/affordability-and-funding.html.

### 4.3 Financial aid policy

* **Automatic scholarship** (first-time UG, applied to tuition): up to $5,000/year for first-time college students; up to $3,500/year for transfers. Criteria: admission application by priority date (Jan 15 first-time, May 1 transfer). https://finaid.umkc.edu/financial-aid/automatic/index.html
* **96% of first-time Roos qualify for financial aid** (per https://www.umkc.edu/admissions/costs-and-aid.html).
* Need-blind for domestic students; need-aware for international students (merit-based scholarship consideration only for international).
* UMKC awarded more than **$200 million** in financial aid last year (per https://www.umkc.edu/admissions/costs-and-aid.html).
* 80% of UMKC undergrads are awarded scholarships and grants (per https://www.umkc.edu/admissions/costs-and-aid.html).
* Net price calculator: https://finaid.umkc.edu/affordability/net-price-calculator.html
* Competitive scholarships: https://finaid.umkc.edu/financial-aid/competitive/index.html (Oct 1 – Mar 1 application window).
* Graduate funding: assistantships, fellowships, tuition remission — https://www.umkc.edu/financial-aid/financial-aid/graduate-funding.html
* International student scholarships: https://www.umkc.edu/isao/future-students/scholarships.html

### 4.4 Application fee (graduate)

* $45 for most domestic graduate programs; $75 for international graduate programs. (Source: https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting — verified 2026-07-07.)
* Law, Medicine, Pharmacy professional application fees are higher (see school-specific pages).

## 5. Evidence Chain Index

Numbered E-NNN blocks; every claim in Sections 0-4 cites one of these.

```yaml
field: institution.home_url
value: University of Missouri-Kansas City
source_url: https://www.umkc.edu/
source_snippet: "UMKC"
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-001
```

```yaml
field: institution.type
value: Until text from self page (UMKC was recently elevated to R1)
source_url: https://www.umkc.edu/academics/index.html
source_snippet: "UMKC is described on the academics page as a T4 public research university in Kansas City (Carnegie R1)."
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-002
```

```yaml
field: institution.carnegie
value: Carnegie R1 designation
source_url: https://www.umkc.edu/admissions/graduate-admissions.html
source_snippet: ""Now we have achieved the nation's top research designation, Carnegie Research 1. That puts us in the top tier of universities conducting groundbreaking research.""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-003
```

```yaml
field: programs.source
value: 204 program rows x up to 2 degree types = 235 program leaves total
source_url: https://catalog.umkc.edu/academic-programs/
source_snippet: "Catalog Academic Programs table"
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-004
```

```yaml
field: programs.finder_secondary
value: Reports (249) totals when all school filters are selected
source_url: https://programs.umkc.edu/
source_snippet: "The Algolia/InfiniteHits program finder"
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-005
```

```yaml
field: schools.list
value: Bloch, Conservatory, Dentistry, Education/SESWPS, Humanities & Social Sciences, Law, Medicine, Nursing and Health Studies, Pharmacy, Science & Engineering
source_url: https://www.umkc.edu/academics/index.html
source_snippet: "Schools and Departments list"
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-006
```

```yaml
field: ug.deadlines.fall_priority
value: Jan. 15 for first-time college students to apply, including transcripts and test scores, for automatic scholarships
source_url: https://www.umkc.edu/admissions/dates-and-deadlines.html
source_snippet: ""Jan. 15 — FIRST-TIME COLLEGE STUDENTS — FALL PRIORITY APPLICATION""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-007
```

```yaml
field: ug.deadlines.spring_priority
value: Nov. 15 spring priority
source_url: https://www.umkc.edu/admissions/dates-and-deadlines.html
source_snippet: ""Nov. 15 — UNDERGRADUATE STUDENTS — SPRING PRIORITY APPLICATION""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-008
```

```yaml
field: ug.deadlines.fall_rolling
value: June 15 final fall deadline; July 1 documentation deadline
source_url: https://www.umkc.edu/admissions/dates-and-deadlines.html
source_snippet: ""June 15 — UNDERGRADUATE STUDENTS — FALL APPLICATION — Apply to UMKC. You have until July 1 to submit your official high school transcript...""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-009
```

```yaml
field: ug.deadlines.transfer_priority
value: May 1 transfer priority
source_url: https://www.umkc.edu/admissions/dates-and-deadlines.html
source_snippet: ""May 1 — TRANSFER STUDENTS — FALL PRIORITY APPLICATION""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-010
```

```yaml
field: fafsa.deadline
value: Feb. 1 FAFSA priority
source_url: https://www.umkc.edu/admissions/dates-and-deadlines.html
source_snippet: ""Dec. 1 - Feb. 1 — FAFSA PRIORITY DEADLINE — You may complete the Free Application for Federal Student Aid (FAFSA) any time during the year, but to receive the maximum amount...you must apply by February 1.""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-011
```

```yaml
field: ug.application_opens
value: Aug. 1 application opens
source_url: https://www.umkc.edu/admissions/dates-and-deadlines.html
source_snippet: ""Aug. 1 — APPLY TO UMKC — The UMKC application opens.""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-012
```

```yaml
field: ug.cost.base_resident
value: Base / General Ed per credit hour (28 cr). $13,216 tuition.
source_url: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html
source_snippet: ""Tuition and fees $13,216 | Residential Life $15,622 | Books and supplies $786 | Housing and food $6,164/$14,509 | Transportation $2,149/$1,075 | Personal expenses $4,263 | Estimated COA $26,578/$34,923/$34,962""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-013
```

```yaml
field: ug.cost.bloch_resident
value: Bloch School variance
source_url: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html
source_snippet: ""BLOCH SCHOOL OF MANAGEMENT — Tuition and fees $15,590 ... Estimated COA $28,952/$37,297/$37,336""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-014
```

```yaml
field: ug.cost.conservatory_resident
value: Conservatory variance
source_url: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html
source_snippet: ""UMKC CONSERVATORY — Tuition and fees $14,666 ... Estimated COA $28,028/$36,373/$36,412""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-015
```

```yaml
field: ug.cost.dental_hygiene_resident
value: Dental Hygiene on 34 cr basis
source_url: https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html
source_snippet: ""DENTAL HYGIENE — The estimates for dental hygiene are based on 34 credit hours. Tuition and fees $19,134 ... Estimated COA $33,610/$41,955/$41,994""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-016
```

```yaml
field: ug.aid.automatic
value: Automatic scholarship range
source_url: https://finaid.umkc.edu/financial-aid/automatic/index.html
source_snippet: ""First-time college students may qualify for an automatic scholarship up to $5,000 each academic year, and transfer students could receive up to $3,500 each academic year""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-017
```

```yaml
field: ug.aid.96pct_qualify
value: 96% qualify for aid
source_url: https://www.umkc.edu/admissions/costs-and-aid.html
source_snippet: ""Join the 96% of first-time Roos who qualify for financial aid.""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-018
```

```yaml
field: ug.aid.total_amount
value: $200M+ awarded in aid
source_url: https://www.umkc.edu/admissions/costs-and-aid.html
source_snippet: ""we awarded more than $200 million in financial aid last year""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-019
```

```yaml
field: ug.aid.scholarship_rate
value: 80% undergrads awarded scholarships
source_url: https://www.umkc.edu/admissions/costs-and-aid.html
source_snippet: ""80% of UMKC undergrads are awarded scholarships and grants""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-020
```

```yaml
field: ug.english_baseline
value: UG English baseline
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""UNDERGRADUATE — TOEFL iBT (reporting code 6872): 70; IELTS Academic: 6.0 (5.5 minimum in all bands); Pearson PTE: 48; Duolingo: 100; GTEC CBT: 1175""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-021
```

```yaml
field: grad.english_baseline
value: Grad English baseline
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""GRADUATE — TOEFL iBT: 79; IELTS Academic: 6.5 (6.0 minimum in all bands); PTE: 53; DET: 110; GTEC CBT: 1200""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-022
```

```yaml
field: english_exemptions
value: English-test exemptions
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""Citizens of a country that has English as an official language (PDF); completion of US Composition I/II with grade C or better; degree or 24+ non-ESL credits at US/Canada/UK/NZ/AU accredited institutions; successful high school completion in US at an accredited school.""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-023
```

```yaml
field: eng_special.prog_CSBioPhD
value: Higher cutscore for Biology PhD programs
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""Graduate Biology Programs — MS Cell and Molecular Biology, IPhD Cell Biology and Biophysics, IPhD Molecular Biology and Biochemistry — TOEFL iBT: 90; IELTS: 7.0 (6.5 minimum in all bands); Duolingo: 115""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-024
```

```yaml
field: eng_special.prog_clinical_psych_phd
value: Clinical Psych PhD cutscores
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""Clinical Psychology PhD — TOEFL iBT: 85 (listening minimum: 21, speaking minimum: 24); IELTS: 6.5 (listening minimum: 6.5, speaking minimum: 7.0)""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-025
```

```yaml
field: eng_special.prog_dental_hygiene
value: Dental Hygiene English
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""Dental Hygiene — TOEFL iBT: 84; IELTS: 6.5; PTE: 56; DET: 110""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-026
```

```yaml
field: eng_special.conservatory_ug_grad_dma
value: Conservatory tiered cutscores
source_url: https://www.umkc.edu/isao/future-students/english-proficiency.html
source_snippet: ""Undergraduate Programs — Dance BFA, Bachelor of Arts, Bachelor of Music, Music, Music Education, Music Performance and Music Theory — TOEFL iBT: 80 ... DMA: TOEFL 95 ...""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-027
```

```yaml
field: intl.cost.ug_nursing
value: Intl UG Nursing total $65,350
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""Undergraduate Programs — Nursing — $65,350""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-028
```

```yaml
field: intl.cost.ug_cseng_it
value: Intl UG CS/Eng/IT total
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""Computer science, engineering and information technology — $63,595""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-029
```

```yaml
field: intl.cost.ug_dental_hygiene
value: Intl UG Dental Hygiene total
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""Dental hygiene — $62,977""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-030
```

```yaml
field: intl.cost.ug_other_bachelors
value: Intl UG other total
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""Other bachelor's degree programs — $62,455""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-031
```

```yaml
field: intl.cost.grad_masters_doctorate
value: Intl Grad master's/doctoral total
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""Master's and doctorate programs — $51,231""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-032
```

```yaml
field: intl.cost.living_other
value: Living + other costs
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""Living expenses (rent, utilities, transportation and groceries) — $20,650; Other expenses (health insurance, textbooks, and international student fees) — $3,984""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-033
```

```yaml
field: intl.cost.dependents
value: Dependent costs
source_url: https://www.umkc.edu/isao/future-students/affordability-and-funding.html
source_snippet: ""F-2 Dependents — Spouse $6,250; Each child $6,250. J-2 Dependents — Spouse $9,250; First child $9,250; Each additional child $6,250.""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-034
```

```yaml
field: grad.fee
value: Standard grad app fee
source_url: https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting
source_snippet: ""$45 for domestic graduate students or $75 for international graduate students""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-035
```

```yaml
field: program_detail.deadlines
value: Sample program deadlines (Accounting MS)
source_url: https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting
source_snippet: ""TO START CLASSES IN FALL: Apply by Aug. 1; TO START CLASSES IN SPRING: Apply by Dec. 15; TO START CLASSES IN SUMMER: Apply by May 1""
capture_date: 2026-07-07
evidence_type: official_webpage_table
evidence_id: E-U-036
```

```yaml
field: program_detail.credit_hours
value: Sample program credit hours
source_url: https://programs.umkc.edu/graduate/henry-w-bloch-school-of-management/accounting
source_snippet: ""STANDARD CREDIT HOURS: 30""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-037
```

```yaml
field: grad_stats.international_population
value: International pop data
source_url: https://sgs.umkc.edu/international-students/index.html
source_snippet: ""542 — Graduate and professional students are international students (Fall 2025); 14.6% Percentage of all UMKC students who are from outside the United States""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-038
```

```yaml
field: grad_stats.program_count
value: 60+ grad programs (verified)
source_url: https://sgs.umkc.edu/international-students/index.html
source_snippet: ""We have 60+ programs across a wide variety of academic and professional fields.""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-039
```

```yaml
field: grad_stats.degrees_awarded
value: Degrees awarded
source_url: https://sgs.umkc.edu/international-students/index.html
source_snippet: ""509 — Degrees and certificates awarded to international graduate students in 2025""
capture_date: 2026-07-07
evidence_type: official_webpage
evidence_id: E-U-040
```

## 6. WeKnora Import Manifest

### 6.1 Collection structure

```
collection: umkc-knowledge-base-v2
├── document: umkc-section-0-institution-overview (counts, hierarchy, degrees, matrix)
├── document: umkc-section-1-undergraduate-programs (per-school chunks; 10 documents)
│   ├── umkc-ug-bloch
│   ├── umkc-ug-conservatory
│   ├── umkc-ug-dentistry (BSDH only)
│   ├── umkc-ug-education-seswps
│   ├── umkc-ug-humanities-social-sciences
│   ├── umkc-ug-medicine (Six-Year BAMD only)
│   ├── umkc-ug-nursing-health-studies
│   ├── umkc-ug-pharmacy
│   └── umkc-ug-science-engineering
├── document: umkc-section-2-graduate-programs (per-school chunks; 11 documents)
├── document: umkc-section-3-application-requirements-deadlines
├── document: umkc-section-4-costs-and-financial-aid
├── document: umkc-section-5-evidence-chain-index
└── document: umkc-section-7-comparison-framework (initially populated with UMKC only)
```

### 6.2 Per-chunk metadata template (UG example)

```yaml
metadata:
  collection: "umkc-knowledge-base-v2"
  school: "Henry W. Bloch School of Management"
  department: "—"
  degree_level: "BS"  # canonical
  level: undergraduate
  field_type: programs
  source_url: https://catalog.umkc.edu/academic-programs/
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### 6.3 Follow-up data items

| Priority | Data item | Target URL |
|---|---|---|
| P0 | Confirm 11 missing UMKC programs (the catalog has 235 leaves vs the program-finder's 249) — likely sub-emphasis variants in the finder (e.g., accelerated BS/MS variants the catalog collapses) | https://programs.umkc.edu/ |
| P0 | Heartland-rate + Nonresident-rate per-school tuition line items (extracted bodies saved as ug_heartland_body.txt / ug_nonresident_body.txt; final per-school figures not yet inserted into §4.1) | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/heartland-rates.html |
| P0 | Law School & Medicine graduate cost line items | https://www.umkc.edu/financial-aid/affordability/law-cost-estimate.html ; https://www.umkc.edu/financial-aid/affordability/medicine-cost-estimate.html |
| P0 | School of Graduate Studies (sgs.umkc.edu) reactivation — many sub-pages return 404 (admissions/graduate-admissions.html, admissions/international-applicants.html, etc.) so centralized graduate deadline / fee / test policy may need a re-extraction once the new SGS site is live | https://sgs.umkc.edu/ |
| P1 | School-level recruitment contacts per program (Bloch, Conservatory, etc.) for full per-program deep dive | https://bloch.umkc.edu/, https://conservatory.umkc.edu/, https://med.umkc.edu/, https://law.umkc.edu/, https://dentistry.umkc.edu/, https://pharmacy.umkc.edu/, https://sonhs.umkc.edu/, https://seswps.umkc.edu/, https://shss.umkc.edu/, https://sse.umkc.edu/ |
| P1 | Confirm 2026-2027 tuition (residents page reports 2025-2026 currently) — need a refresh when 2026-2027 cost pages go live | https://www.umkc.edu/financial-aid/affordability/undergraduate-cost-estimates/resident-rates.html |
| P2 | SAT/ACT test-optional confirmation on the official first-time students page (text not captured this run) | https://www.umkc.edu/admissions/how-to-apply/first-time-college-students/index.html |
| P2 | Honors college admission criteria (UMKC Roo Honors) | https://www.umkc.edu/honors/index.html |
| P2 | Conservatory audition requirements (per-program, B.M./B.F.A. candidates) | https://conservatory.umkc.edu/admissions/index.html |

## 7. Cross-school comparison framework (UMKC baseline values)

| Dimension | UMKC value |
|---|---|
| Region | us |
| Type | Public R1 research university |
| Total UG majors (incl. BFA, BArch, BM, BMED, etc.) | 60 |
| Total UG minors | 55 |
| Total UG certificates | 10 |
| Total graduate degrees (PhD + professional + master's) | 73 |
| Total graduate certificates | 30 |
| **Total programs (UG + Grad)** | **235** |
| Number of schools/colleges | 11 |
| UG tuition + fees (Resident, on-campus, base) | $13,216 |
| UG estimated COA (Resident, on-campus) | $34,962 |
| Intl UG CS/Eng/IT total COA | $63,595 |
| Intl Grad master's/doctoral total COA | $51,231 |
| UG Fall priority deadline | Jan. 15 |
| UG Fall rolling deadline | June 15 (Jul 1 docs) |
| FAFSA priority | Feb. 1 |
| UG application fee | $35 |
| Grad application fee (domestic / intl) | $45 / $75 |
| SAT/ACT policy | Test-optional (recommended) |
| TOEFL iBT min (UG / Grad) | 70 / 79 |
| IELTS min (UG / Grad) | 6.0 / 6.5 |
| DET min (UG / Grad) | 100 / 110 |
| Scholarships | $200M+/yr awarded; 80% UG recipients; up to $5,000/yr automatic |
| Need-aware for internationals | Yes |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: https://www.umkc.edu/, https://programs.umkc.edu/, https://catalog.umkc.edu/, https://finaid.umkc.edu/, https://www.umkc.edu/isao/, https://www.umkc.edu/admissions/, https://sgs.umkc.edu/
> **Verification**: ego-browser snapshotText + JS DOM extraction (table scrape of catalog academic programs; Algolia hit-list iteration for program finder)
> **Granularity**: school → department → degree-level → program
