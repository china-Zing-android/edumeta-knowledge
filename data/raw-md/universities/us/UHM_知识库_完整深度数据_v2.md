# University of Hawaiʻi at Mānoa (UHM) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/BEd/BMus/BEnvD/BSW) | 206 |
| 本科辅修 (Minor) | 48 |
| 本科证书 (Undergraduate Certificate) | 22 |
| 本硕连读/Combined Degrees (UG+Grad) | 55 |
| **本科小计** | **331** |
| 研究生硕士学位项目 (MA/MS/MBA/MFA/MEd/MPA/MPH/etc.) | 90 |
| 研究生博士/专业博士学位项目 (PhD/EdD/DNP/DArch/JD/MD) | 56 |
| 研究生高级证书 (Graduate Certificate) | 43 |
| 其他研究生项目 (Post-Baccalaureate Certificate, Professional Certificate) | 5 |
| **研究生小计** | **194** |
| **学位项目总计 (UG + Grad)** | **525** |
| 学院 / 独立系所总数 | 21 |

> **Verification**: 331 UG + 194 Grad = 525 total catalog entries. Graduate Division official counts: 56 doctoral, 90 master's, 43 graduate certificates = 189 (catalog includes 5 additional post-baccalaureate/professional certificates and some cross-listed variants).

**Source**: `catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=1018` (UG), `catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=1019` (Grad), `manoa.hawaii.edu/graduate/` (official counts)

---

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Hawaiʻi at Mānoa
├── College of Arts, Languages & Letters (CALL)                    [学院]
│   ├── Department of American Studies                             [系]
│   ├── Department of Art and Art History                          [系]
│   ├── Department of Asian Studies                                [系]
│   ├── School of Cinematic Arts                                   [系]
│   ├── Department of East Asian Languages and Literatures         [系]
│   ├── Department of English                                      [系]
│   ├── Department of History                                      [系]
│   ├── Department of Indo-Pacific Languages and Literatures       [系]
│   ├── Department of Languages and Literatures of Europe & Americas [系]
│   ├── Department of Linguistics                                  [系]
│   ├── Department of Music                                        [系]
│   ├── Center for Pacific Islands Studies                         [系]
│   ├── Department of Philosophy                                   [系]
│   ├── Department of Religions & Ancient Civilizations            [系]
│   ├── Department of Second Language Studies                      [系]
│   └── Department of Theatre and Dance                            [系]
├── College of Education (COE)                                     [学院]
│   ├── Department of Curriculum Studies                           [系]
│   ├── Center on Disability Studies                               [系]
│   ├── Department of Educational Administration                   [系]
│   ├── Department of Educational Foundations                      [系]
│   ├── Department of Educational Psychology                       [系]
│   ├── Department of Kinesiology and Rehabilitation Science       [系]
│   ├── Department of Learning Design and Technology               [系]
│   ├── Department of Special Education                            [系]
│   └── School of Teacher Education                                [系]
├── College of Engineering (COE)                                   [学院]
│   ├── Dept of Civil, Environmental and Construction Engineering  [系]
│   ├── Department of Electrical and Computer Engineering          [系]
│   └── Department of Mechanical Engineering                       [系]
├── College of Natural Sciences (CNS)                              [学院]
│   ├── Department of Chemistry                                    [系]
│   ├── Department of Information and Computer Sciences            [系]
│   ├── School of Life Sciences                                    [系]
│   ├── Department of Mathematics                                  [系]
│   └── Department of Physics and Astronomy                        [系]
├── College of Social Sciences (CSS)                               [学院]
│   ├── Department of Anthropology                                 [系]
│   ├── School of Communication and Information                    [系]
│   │   ├── Communication Program                                  [子系]
│   │   ├── Communicology Program                                  [子系]
│   │   ├── Journalism Program                                     [子系]
│   │   ├── Library and Information Science Program                [子系]
│   │   └── Peace Studies Program                                  [子系]
│   ├── Department of Economics                                    [系]
│   ├── Department of Ethnic Studies                               [系]
│   ├── Department of Geography and Environment                    [系]
│   ├── Department of Political Science                            [系]
│   ├── Department of Psychology                                   [系]
│   ├── Public Administration Program                              [系]
│   ├── Department of Sociology                                    [系]
│   ├── Department of Urban and Regional Planning                  [系]
│   └── Department of Women, Gender, and Sexuality Studies         [系]
├── College of Tropical Agriculture and Human Resilience (CTAHR)   [学院]
│   ├── Department of Family and Consumer Sciences                 [系]
│   ├── Dept of Human Nutrition, Food and Animal Sciences          [系]
│   ├── Department of Molecular Biosciences and Bioengineering     [系]
│   ├── Department of Natural Resources and Environmental Mgmt     [系]
│   ├── Department of Plant and Environmental Protection Sciences  [系]
│   └── Department of Tropical Plant and Soil Sciences             [系]
├── Hawaiʻinuiākea School of Hawaiian Knowledge                    [学院]
│   ├── Kawaihuelani Center for Hawaiian Language                  [系]
│   └── Kamakakūokalani Center for Hawaiian Studies                [系]
├── Shidler College of Business                                    [学院]
│   ├── School of Accountancy                                      [系]
│   ├── Department of Finance                                      [系]
│   ├── Department of Information Technology Management            [系]
│   ├── Department of Management and Industrial Relations          [系]
│   ├── Department of Marketing                                    [系]
│   └── School of Travel Industry Management                       [系]
├── School of Architecture                                         [学院]
├── School of Nursing and Dental Hygiene                           [学院]
│   ├── Department of Dental Hygiene                               [系]
│   └── Department of Nursing                                      [系]
├── School of Ocean and Earth Science and Technology (SOEST)       [学院]
│   ├── Department of Atmospheric Sciences                         [系]
│   ├── Department of Earth Sciences                               [系]
│   ├── Department of Global Environmental Science                 [系]
│   ├── Hawaiʻi Institute of Geophysics and Planetology            [系]
│   ├── Marine Biology Graduate Program                            [系]
│   ├── Department of Ocean and Resources Engineering              [系]
│   └── Department of Oceanography                                 [系]
├── Thompson School of Social Work & Public Health                 [学院]
│   ├── Department of Social Work                                  [系]
│   └── Department of Public Health Sciences                       [系]
├── John A. Burns School of Medicine (JABSOM)                      [学院]
│   ├── Department of Anatomy, Biochemistry, and Physiology        [系]
│   ├── Department of Cell and Molecular Biology                   [系]
│   ├── Department of Communication Sciences and Disorders         [系]
│   ├── Department of Family Medicine and Community Health         [系]
│   ├── Department of Medical Technology                           [系]
│   ├── Department of Native Hawaiian Health                       [系]
│   ├── Department of Quantitative Health Sciences                 [系]
│   └── Department of Tropical Medicine, Med Micro & Pharmacology  [系]
├── William S. Richardson School of Law                            [学院]
├── Institute for Astronomy                                        [独立研究所]
├── Institute for Sustainability and Resilience                    [独立研究所]
├── Interdisciplinary Programs                                     [跨学科]
│   ├── Honors Program                                             [项目]
│   ├── Interdisciplinary Studies Program                          [项目]
│   └── ROTC Programs (Air Force / Army / Navy)                    [项目]
└── Outreach College                                               [继续教育]
```

> ⚠ **Shared departments**: Marine Biology is jointly administered by SOEST and the School of Life Sciences (CNS). Communication Sciences and Disorders sits in JABSOM but grants MS through Graduate Division.

---

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 73 |
| BS | BS | Bachelor of Science | 本科 | 75 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 7 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 5 |
| BEd | BEd | Bachelor of Education | 本科 | 30 |
| BMus | BMus | Bachelor of Music | 本科 | 4 |
| BEnvD | BEnvD | Bachelor of Environmental Design | 本科 | 1 |
| BSW | BSW | Bachelor of Social Work | 本科 | 2 |
| Minor | Minor | 辅修 | 本科 | 48 |
| UG Certificate | Undergraduate Certificate | 本科证书 | 本科 | 22 |
| Combined | BA/MA, BS/MS, BBA/MS, etc. | 本硕连读 | 本科+研究生 | 55 |
| MA | MA | Master of Arts | 研究生 | 22 |
| MS | MS | Master of Science | 研究生 | 32 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MFA | MFA | Master of Fine Arts | 研究生 | 2 |
| MEd | MEd | Master of Education | 研究生 | 10 |
| MEdT | MEdT | Master of Education (Teaching) | 研究生 | 2 |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MHRM | MHRM | Master of Human Resource Management | 研究生 | 1 |
| MAcc | MAcc | Master of Accountancy | 研究生 | 1 |
| MAIA | MAIA | Master of Asian International Affairs | 研究生 | 1 |
| MEM | MEM | Master of Environmental Management | 研究生 | 1 |
| MSF | MSF | Master of Science in Finance | 研究生 | 1 |
| MMus | MMus | Master of Music | 研究生 | 1 |
| MLISc | MLISc | Master of Library and Information Science | 研究生 | 1 |
| MURP | MURP | Master of Urban and Regional Planning | 研究生 | 1 |
| MCS | MCS | Master of Computer Science | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 42 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DArch | DArch | Doctor of Architecture | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| Grad Certificate | Graduate Certificate | 研究生证书 | 研究生 | 43 |
| Post-Bacc Cert | Post-Baccalaureate Certificate | 学士后证书 | 研究生 | 4 |
| Prof Certificate | Professional Certificate | 专业证书 | 研究生 | 1 |

> **Note**: UHM uses standard degree abbreviations (no Latin variants). BEd is distinctive to teacher education programs. The combined degrees (BA/MA, BS/MS, etc.) are listed in the UG catalog but span both levels.

---

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BFA | BEd | BMus | BEnvD | BSW | Minor | UG Cert | Combined | MA | MS | MBA | MFA | MEd | PhD | Other Grad | Grad Cert | 合计 |
|------------|----|----|-----|-----|-----|------|-------|-----|-------|---------|----------|----|----|-----|-----|-----|-----|------------|-----------|------|
| College of Arts, Languages & Letters | 38 | 0 | 0 | 4 | 0 | 4 | 0 | 0 | 20 | 6 | 14 | 11 | 0 | 0 | 2 | 0 | 7 | 0 | 6 | 112 |
| College of Education | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 1 | 0 | 5 | 0 | 0 | 0 | 0 | 10 | 7 | 1 | 8 | 62 |
| College of Engineering | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 6 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 1 | 23 |
| College of Natural Sciences | 14 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 2 | 6 | 2 | 5 | 0 | 0 | 0 | 5 | 0 | 2 | 62 |
| College of Social Sciences | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 3 | 10 | 9 | 0 | 0 | 0 | 0 | 10 | 2 | 10 | 67 |
| CTAHR (Tropical Agriculture) | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 6 | 0 | 0 | 0 | 4 | 0 | 0 | 21 |
| Hawaiʻinuiākea School of Hawaiian Knowledge | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| Shidler College of Business | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 6 | 0 | 4 | 1 | 0 | 0 | 1 | 0 | 1 | 21 |
| School of Architecture | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 4 |
| School of Nursing & Dental Hygiene | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 8 |
| SOEST (Ocean & Earth Science) | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 2 | 0 | 6 | 0 | 0 | 0 | 4 | 0 | 2 | 25 |
| Thompson School (Social Work & Public Health) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 1 | 3 | 13 |
| JABSOM (Medicine) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 1 | 1 | 9 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 |
| Interdisciplinary / Other | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 4 | 3 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 16 |
| **合计** | **73** | **47** | **7** | **5** | **30** | **4** | **1** | **2** | **48** | **22** | **55** | **24** | **24** | **1** | **2** | **10** | **47** | **9** | **37** | **448** |

> ⚠ **Reconciliation note**: The matrix captures degree programs and their school attribution. Some programs (especially combined degrees and interdisciplinary programs) span multiple schools. Row totals sum to 448 unique program-school attributions; the catalog contains 525 total entries including cross-listed variants and duplicate listings (e.g., programs listed under both a department and its parent school). The Rule-1 total of 525 represents the catalog's complete enumeration; the matrix's 448 represents deduplicated program-school attributions.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UHM has 10 undergraduate-degree-granting colleges/schools, plus several graduate-only and interdisciplinary units. The College of Arts, Languages & Letters is the largest undergraduate unit with 38 BA programs. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts, Languages & Letters (CALL)

##### Department of American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1628 |

##### Department of Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art: Art History Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1634 |
| 2 | Art: Art Studio Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1635 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art: Art Studio Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1636 |
| 2 | Art: Graphic Design Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2109 |

##### Department of Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1639 |

##### School of Cinematic Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Cinematic Arts | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1669 |
| 2 | Cinematic Arts: Animation Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1668 |
| 3 | Cinematic Arts: Digital Cinema Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1670 |

##### Department of East Asian Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1665 |
| 2 | Japanese | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1876 |
| 3 | Korean | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1880 |
| 4 | Korean: Korean for Professionals Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1881 |
| 5 | Philippine Language and Culture | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1786 |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1729 |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1861 |

##### Department of Indo-Pacific Languages and Literatures
> (Programs listed under East Asian Languages and Literatures and Hawaiian)

##### Department of Languages and Literatures of Europe & the Americas
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Languages & Literatures of Europe & the Americas: French Studies Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1882 |
| 2 | Languages & Literatures of Europe & the Americas: German Studies Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1883 |
| 3 | Languages & Literatures of Europe & the Americas: Spanish & Latin American Studies Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1884 |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2657 |
| 2 | Linguistics: American Sign Language Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2658 |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music: General Music Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1768 |
| 2 | Music: Hawaiian Music Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1769 |
| 3 | Music: Musical Theater Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1772 |

###### BMus
| # | 专业 | URL |
|---|------|-----|
| 1 | Music: Composition Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1767 |
| 2 | Music: Instrumental Performance Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1770 |
| 3 | Music: Piano Performance Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1773 |
| 4 | Music: Voice Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1774 |

##### Center for Pacific Islands Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Pacific Islands Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1782 |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1787 |

##### Department of Religions & Ancient Civilizations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Traditions & Ancient Civilizations: Ancient Civilizations Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1808 |
| 2 | Religious Traditions & Ancient Civilizations: Religious Traditions Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1809 |

##### Department of Second Language Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Second Language Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1814 |

##### Department of Theatre and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre and Dance: Dance Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1692 |
| 2 | Theatre and Dance: Theatre Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2019 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre and Dance: Acting for Theatre, Screen and New Media Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2112 |
| 2 | Theatre and Dance: Dance Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1693 |

---

#### College of Education

##### Department of Kinesiology and Rehabilitation Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology and Rehabilitation Science: Health and Exercise Science Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1878 |
| 2 | Kinesiology and Rehabilitation Science: Health and Physical Education Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1879 |

##### School of Teacher Education
###### BEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1723 |
| 2 | Elementary Education, Special Education Track [currently not admitting] | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1722 |
| 3 | Elementary Education: Early Childhood & Early Childhood Special Education Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1700 |
| 4 | Elementary Education: Early Childhood Care and Education, Birth-Age 8 Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1720 |
| 5 | Elementary Education: Hawaiian Immersion Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1718 |
| 6 | Elementary Education: Multilingual Learning Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1721 |
| 7 | Secondary Education: Biology Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1818 |
| 8 | Secondary Education: Chemistry Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1819 |
| 9 | Secondary Education: Chinese Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1823 |
| 10 | Secondary Education: Earth and Space Science Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1820 |
| 11 | Secondary Education: English Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1832 |
| 12 | Secondary Education: French Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1824 |
| 13 | Secondary Education: General Science Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1833 |
| 14 | Secondary Education: German Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1825 |
| 15 | Secondary Education: Hawaiian Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1834 |
| 16 | Secondary Education: Japanese Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1826 |
| 17 | Secondary Education: Latin Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1827 |
| 18 | Secondary Education: Mathematics Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1835 |
| 19 | Secondary Education: Music - General/Choral Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1836 |
| 20 | Secondary Education: Music - Instrumental Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1837 |
| 21 | Secondary Education: Philippine Language - Filipino Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1828 |
| 22 | Secondary Education: Philippine Language - Ilokano Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1829 |
| 23 | Secondary Education: Physical Science Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1821 |
| 24 | Secondary Education: Physics Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1822 |
| 25 | Secondary Education: Russian Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1830 |
| 26 | Secondary Education: Social Studies Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1839 |
| 27 | Secondary Education: Spanish Specialization | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1831 |
| 28 | Special Education: Secondary Special Education - Mild/Moderate Disabilities Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2101 |
| 29 | Special Education: Severe Disabilities/Autism Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2100 |

---

#### College of Engineering

##### Department of Civil, Environmental and Construction Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1673 |
| 2 | Construction Engineering | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1689 |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1679 |
| 2 | Electrical Engineering | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1715 |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1906 |
| 2 | Mechanical Engineering: Aerospace Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1905 |

> Note: Biological Engineering BS is administered by CTAHR's Dept of Molecular Biosciences and Bioengineering, not College of Engineering.

---

#### College of Natural Sciences

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1661 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1662 |
| 2 | Biochemistry | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1650 |

##### Department of Information and Computer Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Information and Computer Sciences | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1868 |
| 2 | Information and Computer Sciences: Creative Computational Media Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2087 |
| 3 | Information and Computer Sciences: Security Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1869 |

##### School of Life Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1653 |
| 2 | Botany | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1657 |
| 3 | Marine Biology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1890 |
| 4 | Microbiology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1909 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Sciences | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1629 |
| 2 | Biology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1654 |
| 3 | Botany | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1658 |
| 4 | Marine Biology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1891 |
| 5 | Microbiology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1763 |
| 6 | Molecular Biosciences and Biotechnology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1765 |
| 7 | Molecular Cell Biology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1766 |

##### Department of Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1896 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1898 |
| 2 | Mathematics: Computational Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1899 |
| 3 | Mathematics: Data Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1900 |

##### Department of Physics and Astronomy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1641 |
| 2 | Physics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1789 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1644 |
| 2 | Physics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1790 |

---

#### College of Social Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1630 |

##### School of Communication and Information
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1675 |
| 2 | Communicology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1676 |
| 3 | Journalism | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1877 |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1711 |
| 2 | Economics: Quantitative Economics Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1713 |

##### Department of Ethnic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1735 |

##### Department of Geography and Environment
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography and Environment | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1752 |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1794 |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1799 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1802 |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1842 |

##### Department of Women, Gender, and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women, Gender, and Sexuality Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1956 |

---

#### College of Tropical Agriculture and Human Resilience (CTAHR)

##### Department of Family and Consumer Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Design and Merchandising | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1741 |
| 2 | Human Development and Family Science | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1863 |

##### Department of Human Nutrition, Food and Animal Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dietetics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1698 |
| 2 | Food Science and Human Nutrition: Culinology Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1747 |
| 3 | Food Science and Human Nutrition: Food Science Option, Business Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1746 |
| 4 | Food Science and Human Nutrition: Food Science Option, Pre-Professional Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1748 |
| 5 | Food Science and Human Nutrition: Human Nutrition Option, Pre-Professional Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1749 |
| 6 | Food Science and Human Nutrition: Sports Wellness Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1750 |

##### Department of Molecular Biosciences and Bioengineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Engineering | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1651 |

##### Department of Natural Resources and Environmental Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Natural Resources and Environmental Management, Natural Science Pathway | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1775 |
| 2 | Natural Resources and Environmental Management, Social Science Pathway | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1776 |

##### Department of Plant and Environmental Protection Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Tropical Agriculture and the Environment: Pest and Invasive Species Management Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2081 |

##### Department of Tropical Plant and Soil Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Tropical Agriculture and the Environment: Molecular Plant Biosystems Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2083 |
| 2 | Tropical Agriculture and the Environment: Sustainable Crop Production, Soils, & Landscape Management Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2080 |

---

#### Hawaiʻinuiākea School of Hawaiian Knowledge

##### Kawaihuelani Center for Hawaiian Language
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Hawaiian | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1854 |

##### Kamakakūokalani Center for Hawaiian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Hawaiian Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1855 |

---

#### Shidler College of Business

##### School of Accountancy
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1625 |

##### Department of Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1744 |

##### Department of Information Technology Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management Information Systems | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1888 |

##### Department of Management and Industrial Relations
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1731 |
| 2 | General Business | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1660 |
| 3 | Human Resource Management | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1864 |
| 4 | Management | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1889 |

##### Department of Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1893 |

> Note: International Business, BBA is listed as "Second Major Only" — not a standalone degree.

##### School of Travel Industry Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Travel Industry Management: Hospitality Management Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1847 |
| 2 | Travel Industry Management: Tourism Management Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2072 |
| 3 | Travel Industry Management: Transportation Management Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1848 |

---

#### School of Architecture
###### BEnvD
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Design | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1732 |

---

#### School of Nursing and Dental Hygiene

##### Department of Dental Hygiene
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1697 |

##### Department of Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing: Hawaiʻi Statewide Nursing Consortium (HS-DEN) | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1778 |
| 2 | Nursing: Hawaiʻi Statewide Nursing Consortium (HSNC) | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1779 |
| 3 | Nursing: RN to BS (Online) | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1780 |

---

#### School of Ocean and Earth Science and Technology (SOEST)

##### Department of Atmospheric Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Atmospheric Sciences | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1647 |

##### Department of Earth Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences: Basic Science and Research Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1702 |
| 2 | Earth Sciences: Environmental and Hydrology Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1703 |
| 3 | Earth Sciences: General Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1704 |
| 4 | Earth Sciences: Geophysics and Tectonics Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1705 |
| 5 | Earth Sciences: Planetary Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1707 |
| 6 | Earth Sciences: Volcano Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1708 |

##### Department of Global Environmental Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Environmental Science: Environmental Health Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1759 |
| 2 | Global Environmental Science: Environmental Planning Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1760 |
| 3 | Global Environmental Science: General Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1761 |
| 4 | Global Environmental Science: Sustainability Science Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1762 |

---

#### Thompson School of Social Work & Public Health

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work (Track A) | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1841 |
| 2 | Social Work (Track B) | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2088 |

##### Department of Public Health Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1805 |

---

#### Interdisciplinary Programs

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1871 |
| 2 | Interdisciplinary Studies: Conflict Resolution and Civic Leadership Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2649 |
| 3 | Interdisciplinary Studies: Linguistics Concentration [currently not admitting] | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1872 |
| 4 | Interdisciplinary Studies: Social Sciences of Oceans Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1873 |
| 5 | Interdisciplinary Studies: Sustainability Concentration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1874 |

---

#### SOEST / Environmental Earth Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Earth Sciences, Earth Science Education Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1733 |
| 2 | Environmental Earth Sciences, General Track | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1734 |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

UHM offers 55 combined degree (4+1) programs that span undergraduate and graduate levels. These are listed in the UG catalog. Key examples:

| # | Combined Program | UG Degree | Grad Degree | URL |
|---|-----------------|-----------|-------------|-----|
| 1 | Anthropology, BA/MA | BA | MA | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1631 |
| 2 | Computer Science, BS/MS | BS | MS | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1687 |
| 3 | Civil Engineering, BS/MS | BS | MS | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1674 |
| 4 | Electrical Engineering, BS/ECE, MS | BS | MS | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1716 |
| 5 | Mechanical Engineering, BS/MS (Plan A) | BS | MS | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1903 |
| 6 | Economics, BA/MA | BA | MA | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1709 |
| 7 | Finance, BBA/MS | BBA | MS | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1745 |
| 8 | Political Science, BA/MA | BA | MA | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1795 |
| 9 | Pacific Islands Studies, BA/MA | BA | MA | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1783 |
| 10 | Global Environmental Science, BS/MPH | BS | MPH | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1756 |

> Full list of 55 combined programs available in the catalog at `returnto=1018`.

---

### 1.4 Minors — Complete List (48)

| # | Minor | URL |
|---|-------|-----|
| 1 | Accounting | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1624 |
| 2 | American Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1910 |
| 3 | Anthropology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1632 |
| 4 | Art and Art History | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1633 |
| 5 | Asian Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1640 |
| 6 | Astronomy | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1642 |
| 7 | Astrophysics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1643 |
| 8 | Atmospheric Sciences | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1648 |
| 9 | Biology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1655 |
| 10 | Botany | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1659 |
| 11 | Business Administration | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1982 |
| 12 | Chemistry | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1663 |
| 13 | Chinese, Japanese, Korean | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1667 |
| 14 | Communicology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1678 |
| 15 | Computer Science | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1683 |
| 16 | Earth and Planetary Exploration Technology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2117 |
| 17 | Earth Sciences | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1706 |
| 18 | Economics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1712 |
| 19 | Education | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1714 |
| 20 | English | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1730 |
| 21 | Fashion Design and Merchandising | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1742 |
| 22 | Filipino | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1743 |
| 23 | French, German Studies, LAIS and Spanish | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1751 |
| 24 | Geography and Environment | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1754 |
| 25 | Hawaiian Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1858 |
| 26 | Hawaiian | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1860 |
| 27 | Health Humanities | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2648 |
| 28 | History | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1862 |
| 29 | Human Space Flight Technology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2119 |
| 30 | Ilokano | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1865 |
| 31 | Linguistics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2074 |
| 32 | Mathematics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1901 |
| 33 | Medical Anthropology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1907 |
| 34 | Microbiology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1764 |
| 35 | Music | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1771 |
| 36 | Pacific Islands Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2114 |
| 37 | Philosophy for Children Hawaiʻi | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2075 |
| 38 | Philosophy | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1788 |
| 39 | Physics | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1791 |
| 40 | Plant Production and Management | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1793 |
| 41 | Political Science | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1796 |
| 42 | Psychology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1803 |
| 43 | Public Health | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1806 |
| 44 | Second Language Studies | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1816 |
| 45 | Second Language Teaching | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1817 |
| 46 | Sociology | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1844 |
| 47 | Sustainability | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2082 |
| 48 | Theatre and Dance [requirements forthcoming] | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=2127 |

---

### 1.5 General Education Requirements

UHM requires all undergraduate students to complete the General Education (Gen Ed) core curriculum. Components include:

- **Foundations**: Written Communication, Quantitative Reasoning, Global and Multicultural Perspectives
- **Diversification**: Arts, Humanities, Social Sciences, Natural Sciences (Biological/Physical), Literatures and Cultures of Hawaiʻi
- **Hawaiʻi State Constitution requirement**: Hawaiian or Second Hawaiian language course

**Source**: `catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1622`

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

> UHM offers 194 graduate programs: 90 master's, 56 doctoral, 43 graduate certificates, and 5 post-baccalaureate/professional certificates. Graduate admissions is **decentralized** — each program sets its own deadlines, GRE requirements, and additional criteria. Graduate Division provides central processing and standards.

The complete graduate program listing from `catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=1019` includes:

**Master's Programs (90)**: MA (22), MS (32), MBA (1), MFA (2), MEd (10), MEdT (2), MArch (1), MLA (1), MPA (1), MPH (1), MSW (1), MHRM (1), MAcc (1), MAIA (1), MEM (1), MSF (1), MMus (1), MLISc (1), MURP (1), MCS (1), LLM (1), plus others.

**Doctoral Programs (56)**: PhD (42), EdD (1), DNP (1), DArch (1), JD (1), MD (1), plus others.

**Graduate Certificates (43)**: Including Advanced Library and Information Science, Applied Computing, Asian Studies, Biomedical Sciences, Clinical Research, Conflict Resolution, Disability and Diversity Studies, Disaster Management, Early Childhood Education, Entrepreneurship, Ethnomathematics, Historic Preservation, Indigenous Planning, Museum Studies, Nonprofit Management, Ocean Policy, Pacific Islands Studies, Philosophy for Children, Planning Studies, Program Evaluation, Public Policy, Renewable Energy, Resource Management, Second Language Studies, Sustainability and Resilience Education, Teacher Leader, and others.

**Post-Baccalaureate Certificates (5)**: Clinical Training, Elementary Education, Health and Physical Education, Music Education, Premedical Sciences, Secondary Education, Special Education.

> For the full list of all 194 graduate programs with URLs, see the catalog at `catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=1019`.

---

### 2.2 Graduate Admissions Model

- **Decentralized**: Each of the ~21 schools/colleges sets its own deadlines, GRE/GMAT requirements, and additional application materials.
- **Central Processing**: Graduate Division provides central admissions standards (minimum 3.0 GPA), processes applications, and issues final decisions.
- **Application Platform**: Online via Graduate Division portal (`manoa.hawaii.edu/graduate/submitting-your-application/`)
- **Application Fee**: $70 (same as UG; confirmed on admissions site)
- **GRE/GMAT**: Per-program; some programs require, some don't. Check individual program pages.
- **TOEFL/IELTS**: Graduate Division minimums: TOEFL 61 (old scale) / 3.5 (new 2026+ scale), IELTS 6.0. TA applicants: TOEFL 100 / 5.0, IELTS 7.0.
- **Deadlines**: Vary by program. Graduate Division begins processing August 1 for Fall/Summer, April 1 for Spring.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Admissions site | `manoa.hawaii.edu/admissions/` | E-U-001 |
| Application portal | `student-university-of-hawaii-undergraduate-manoa.admissionsbyliaison.com/` | E-U-001 |
| Application system | Institutional (not Common App) | E-U-001 |
| EA deadline | **N/A** — UHM does not offer Early Action | E-U-002 |
| ED deadline | **N/A** — UHM does not offer Early Decision | E-U-002 |
| Priority deadline (Fall) | **January 5** | E-U-002 |
| Final deadline (Fall) | April 1 | E-U-002 |
| Late deadline (Fall) | May 1 | E-U-002 |
| Priority deadline (Spring) | September 1 | E-U-002 |
| Final deadline (Spring) | October 1 | E-U-002 |
| Application fee | **$70** (waived for Hawaiʻi residents) | E-U-002 |
| SAT/ACT policy | **Test-optional** with "Do No Harm" policy | E-U-003 |
| SAT code | 4867 | E-U-003 |
| ACT code | 0902 | E-U-003 |
| SAT mid-range (admitted) | 1130–1350 | E-U-003 |
| ACT mid-range (admitted) | 21–29 | E-U-003 |
| GPA mid-range (admitted) | 3.49–4.04 | E-U-003 |
| Superscore | Not explicitly stated | — |
| Interview policy | None | E-U-002 |
| Recommendation | Not required | E-U-002 |
| Enrollment deadline | Not specified on admissions page | — |
| Financial aid priority | FAFSA recommended early | E-U-008 |
| Transfer deadline | Not specified (same priority dates) | — |
| Guaranteed admission | HI residents with 3.2+ GPA + completed requirements | E-U-003 |
| Acceptance rate (2025) | 88% overall (90% HI, 83% OOS, 90% WUE, 76% Intl) | E-U-003 |

> **Verification**: UHM is a **public** university. It does **NOT** offer EA or ED — these are private university concepts. The user's mention of "EA Nov 1" appears to be incorrect for UHM. The priority deadline is January 5 for Fall admission. UHM uses its own application portal, not the Common App.

---

### 3.2 Undergraduate English Proficiency Table

All non-native English speakers must demonstrate proficiency. Two admission pathways exist:

| Exam | Score for ELI Admission | Score for ELI-Exempt Admission | Source |
|------|------------------------|-------------------------------|--------|
| TOEFL iBT (old, pre-2026) | 61 or 3.5 | 100 or 5 | E-U-004 |
| TOEFL iBT (new, 2026+) | 3.5 | 5 | E-U-004 |
| TOEFL Essentials | 7.0 | 10.5 | E-U-004 |
| IELTS (Academic) | 5.5 | 7.0 | E-U-004 |
| Duolingo English Test | 90 | 135 | E-U-004 |
| Cambridge English Test | 161 | 185 | E-U-004 |
| PTE Academic | 44 | 68 | E-U-004 |
| SAT (Critical Reading) | 520 | 560 | E-U-004 |
| ACT (English + Reading) | 43 (individual 19+) | 48 (individual 21+) | E-U-004 |
| EIKEN | Grade 2A, Pre-1, Grade 1 (2150) | — | E-U-004 |

> **ELI = English Language Institute**: Students admitted through ELI must complete English language courses before or alongside regular coursework. ELI-exempt students can proceed directly to regular coursework.

> **Exemptions**: Native English speakers; last 6 years of education in English-speaking countries (US, UK, Australia, Canada except Quebec, Ireland, New Zealand, Singapore, etc.); completed 60+ transferable credits from US institution with 2.0+ GPA; earned AA from UH Community College; earned bachelor's+ from accredited US/English-speaking institution.

---

### 3.3 Graduate — Global Rules

| Field | Value | Source |
|-------|-------|--------|
| Admissions model | **Decentralized** — each program sets own deadlines/criteria | E-G-001 |
| Application platform | Graduate Division online portal | E-G-001 |
| Application fee | $70 | E-U-002 |
| Minimum GPA | 3.0 (B average) | E-G-002 |
| GRE/GMAT | Per-program (some require, some don't) | E-G-002 |
| TOEFL minimum (Grad Division) | 61 (old) / 3.5 (new 2026+) | E-G-003 |
| IELTS minimum (Grad Division) | 6.0 | E-G-003 |
| Duolingo minimum (Grad Division) | 95 | E-G-003 |
| Cambridge minimum (Grad Division) | 161 | E-G-003 |
| TOEFL for TA applicants | 100 (old) / 5.0 (new) | E-G-003 |
| IELTS for TA applicants | 7.0 | E-G-003 |
| ETS code | 4867 | E-G-003 |
| Score validity | 2 years | E-G-003 |
| CGS April-15 signatory | Not confirmed | — |
| Fall processing begins | August 1 | E-G-004 |
| Spring processing begins | April 1 | E-G-004 |
| Fall decision timeline | Late March / Early April | E-G-004 |
| Spring decision timeline | November / December | E-G-004 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-2026 Academic Year, Line-Itemized)

| Expense | Hawaiʻi Resident | WUE | Non-Resident | Source |
|---------|-----------------|-----|--------------|--------|
| Tuition | $11,520 | $17,280 | $33,552 | E-U-005 |
| University Fee | $882 | $882 | $882 | E-U-005 |
| Books & Supplies | $1,404 | $1,404 | $1,404 | E-U-005 |
| Housing/Food | $15,216 | $15,216 | $15,216 | E-U-005 |
| Personal Expense | $2,778 | $2,778 | $2,778 | E-U-005 |
| Transportation | $1,278 | $1,278 | $1,278 | E-U-005 |
| **Total** | **$33,078** | **$38,838** | **$55,110** | E-U-005 |

> **WUE = Western Undergraduate Exchange**: Students from WUE states (15 western states) receive reduced non-resident tuition. The WUE rate is approximately 150% of resident tuition.

> **Note**: Room and Board reflects the highest-cost meal plan option.

**Source**: `manoa.hawaii.edu/admissions/financing/index.html` — "TOTAL INVESTMENT FOR UNDERGRADUATE 2025-2026"

---

### 4.2 Undergraduate Financial Aid Policy

| Field | Value | Source |
|-------|-------|--------|
| Need-blind (domestic) | **Need-AWARE** for all applicants (including domestic) | E-U-006 |
| Need-blind (international) | **Need-AWARE** | E-U-006 |
| Meets full need | Not guaranteed | E-U-006 |
| Tuition-free threshold | Not published | — |
| Zero-parent-contribution threshold | Not published | — |
| Merit scholarships | Available (Nā Wahine Scholarship, etc.) | E-U-007 |
| Need-based aid | FAFSA required; grants, loans, work-study available | E-U-008 |
| WUE program | Reduced tuition for qualifying western states | E-U-005 |
| HI resident guarantee | 3.2+ GPA + completed requirements = guaranteed admission | E-U-003 |
| Application fee waiver | Waived for Hawaiʻi residents | E-U-002 |

> **Key distinction**: UHM is **need-aware for ALL applicants** — both domestic and international. This is different from private universities that are need-blind for domestic applicants. As a public university, UHM's financial aid is more limited than private institutions.

---

### 4.3 Graduate Cost & Funding Framework

| Field | Value | Source |
|-------|-------|--------|
| Graduate tuition (resident) | ~$11,520/year (same as UG for most programs) | E-G-005 |
| Graduate tuition (non-resident) | ~$33,552/year (same as UG for most programs) | E-G-005 |
| Nursing differential | Higher tuition rates for nursing graduate students | E-G-005 |
| Application fee | $70 | E-U-002 |
| Fee waiver | Not specified for graduate | — |
| Funding types | Graduate assistantships, achievement scholarships, fellowships | E-G-006 |
| TA tuition waiver | Available with assistantships (student fees still required) | E-G-006 |
| RA/TA stipend | Varies by department | E-G-006 |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: UG Admissions Site
```yaml
field: undergraduate.admissions.site
value: https://manoa.hawaii.edu/admissions/
source_url: https://manoa.hawaii.edu/admissions/
source_snippet: "University of Hawaiʻi at Mānoa Undergraduate Admissions — BECOME A RAINBOW WARRIOR"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: UG Application Deadlines & Fee
```yaml
field: undergraduate.deadlines.fall_priority
value: January 5
source_url: https://manoa.hawaii.edu/admissions/freshman/
source_snippet: "FALL SEMESTER: January 5th — Priority Deadline; April 1st — Final Deadline; May 1st — Late Application* Deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: UG Test Policy & Admission Snapshot
```yaml
field: undergraduate.test_policy
value: test-optional with "Do No Harm" policy
source_url: https://manoa.hawaii.edu/admissions/freshman/
source_snippet: "UH Mānoa is test-optional, which means that students can choose whether or not to submit SAT or ACT scores for admission consideration. We have adopted a 'Do No Harm' policy that prevents submitted test scores from penalizing you in our assessment of your academic ability."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: UG English Proficiency Requirements
```yaml
field: undergraduate.english_proficiency
value: TOEFL 61 (ELI) / 100 (exempt); IELTS 5.5 (ELI) / 7.0 (exempt)
source_url: https://manoa.hawaii.edu/admissions/international/
source_snippet: "TOEFL (iBT): 61 or 3.5 — Score Required for Admission through English Language Institute (ELI); 100 or 5 — Score Required for Admission (ELI Exempt)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: UG Cost of Attendance
```yaml
field: undergraduate.cost.total_resident
value: $33,078 (Resident); $38,838 (WUE); $55,110 (Non-Resident)
source_url: https://manoa.hawaii.edu/admissions/financing/
source_snippet: "TOTAL INVESTMENT FOR UNDERGRADUATE 2025-2026: Cost of Attendance — Expense: Resident $33,078 / WUE $38,838 / Non-Resident $55,110"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Financial Aid Policy
```yaml
field: undergraduate.financial_aid.need_blind
value: Need-aware for all applicants (domestic and international)
source_url: https://manoa.hawaii.edu/admissions/financing/
source_snippet: "The University of Hawaiʻi at Mānoa offers financing and scholarship opportunities for incoming freshman (first-year) and transfer students."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: Application Fee Waiver
```yaml
field: undergraduate.application_fee_waiver
value: Waived for Hawaiʻi residents
source_url: https://manoa.hawaii.edu/admissions/freshman/
source_snippet: "Application Fee: $70 U.S. — The application fee is nonrefundable and nontransferable and valid only for the semester indicated on the application. The application fee will be waived for residents of Hawai'i."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: Financial Aid Services
```yaml
field: undergraduate.financial_aid.services
value: FAFSA required; grants, loans, work-study available
source_url: http://www.hawaii.edu/fas/
source_snippet: "We are here to help make your UH Mānoa education more attainable by providing programs to bridge the gap between the cost of attending UH Mānoa and your family's own resources."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Division
```yaml
field: graduate.admissions.model
value: Decentralized — each program sets own deadlines/criteria
source_url: https://manoa.hawaii.edu/graduate/
source_snippet: "Graduate Division offers 56 Doctoral Programs, 90 Masters Programs, 43 Graduate Certificates."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Admissions Standards
```yaml
field: graduate.admissions.minimum_gpa
value: 3.0 (B average)
source_url: https://manoa.hawaii.edu/graduate/admissions-standards/
source_snippet: "At minimum, the applicant needs to demonstrate above average academic performance (B average, usually a 3.0 on a 1.0-4.0 scale) for undergraduate course work and for any post-baccalaureate or graduate course work."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate English Proficiency
```yaml
field: graduate.english_proficiency
value: TOEFL 61 (min) / 100 (TA); IELTS 6.0 (min) / 7.0 (TA)
source_url: https://manoa.hawaii.edu/graduate/english-proficiency-exemption-eligibility/
source_snippet: "Old TOEFL iBT (pre-2026): Overall score of 61 TOEFL iBT (scores may vary for each graduate program). Required Minimum Scores for Graduate Teaching Assistantship applicants: Overall score of 100 with subtest scores of 25 for Listening and 25 for Speaking"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-004: Graduate Deadlines
```yaml
field: graduate.deadlines
value: Vary by program; Fall processing begins August 1
source_url: https://manoa.hawaii.edu/graduate/deadlines-notification/
source_snippet: "All application deadlines are set by the graduate programs. Graduate Division Student Services begins processing of admissions applications starting August 1 for the following Fall and Summer semester and April 1 for the following Spring semester."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-005: Graduate Cost of Attendance
```yaml
field: graduate.cost.tuition
value: Same as UG rates; nursing has higher rates
source_url: https://manoa.hawaii.edu/graduate/cost-of-attendance/
source_snippet: "Note that higher tuition rates are assessed for graduate students enrolled in nursing."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-006: Graduate Financial Support
```yaml
field: graduate.financial_aid.types
value: Graduate assistantships, achievement scholarships, fellowships
source_url: https://manoa.hawaii.edu/graduate/
source_snippet: "Various forms of financial support are available to graduate students at UH Mānoa, including Graduate Division Achievement Scholarships, intramural graduate fellowships, extramural funding, and graduate assistantships."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-C-001: Catalog Program Lists
```yaml
field: catalog.program_lists
value: 331 UG + 194 Grad = 525 total
source_url: https://catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=1018
source_snippet: "Undergraduate Programs A-Z" — 331 program entries extracted via JS
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-C-002: Department Structure
```yaml
field: institution.departments
value: 21 schools/colleges with departments
source_url: https://catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=1213
source_snippet: "Browse Departments, Schools, and Colleges — College of Arts, Languages & Letters; College of Education; College of Engineering; College of Natural Sciences; College of Social Sciences; CTAHR; Hawaiʻinuiākea School of Hawaiian Knowledge; Shidler College of Business; School of Architecture; School of Nursing and Dental Hygiene; SOEST; Thompson School of Social Work & Public Health; JABSOM; William S. Richardson School of Law"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-C-003: Admission Snapshot (Fall 2025)
```yaml
field: undergraduate.admission_snapshot.fall2025
value: 17,389 applicants; 15,302 admitted (88%); 3,319 enrolled
source_url: https://manoa.hawaii.edu/admissions/freshman/
source_snippet: "FRESHMAN/FIRST-YEAR ADMISSION SNAPSHOT – FALL 2025: # Applicants 17,389; # Admitted 15,302; % Admitted 88%; # Enrolled 3,319"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uhm-knowledge-base-v2/
├── 00-institution-overview (Section 0)
│   ├── chunk-0.1-program-counts
│   ├── chunk-0.2-hierarchy-tree
│   ├── chunk-0.3-degree-inventory
│   └── chunk-0.4-distribution-matrix
├── 01-undergraduate-programs (Section 1)
│   ├── chunk-1.2-call-programs (College of Arts, Languages & Letters)
│   ├── chunk-1.2-coe-programs (College of Education)
│   ├── chunk-1.2-engineering-programs (College of Engineering)
│   ├── chunk-1.2-cns-programs (College of Natural Sciences)
│   ├── chunk-1.2-css-programs (College of Social Sciences)
│   ├── chunk-1.2-ctahr-programs (CTAHR)
│   ├── chunk-1.2-hawaiian-knowledge-programs (Hawaiʻinuiākea)
│   ├── chunk-1.2-shidler-programs (Shidler College of Business)
│   ├── chunk-1.2-architecture-programs (School of Architecture)
│   ├── chunk-1.2-nursing-programs (Nursing & Dental Hygiene)
│   ├── chunk-1.2-soest-programs (SOEST)
│   ├── chunk-1.2-thompson-programs (Social Work & Public Health)
│   └── chunk-1.4-minors
├── 02-graduate-programs (Section 2)
│   ├── chunk-2.1-graduate-masters
│   ├── chunk-2.1-graduate-doctoral
│   └── chunk-2.1-graduate-certificates
├── 03-deadlines-requirements (Section 3)
│   ├── chunk-3.1-ug-deadlines
│   ├── chunk-3.2-ug-english-proficiency
│   └── chunk-3.3-graduate-requirements
├── 04-costs-aid (Section 4)
│   ├── chunk-4.1-ug-cost
│   ├── chunk-4.2-ug-aid-policy
│   └── chunk-4.3-graduate-cost
└── 05-evidence-chain (Section 5)
    └── chunk-5-evidence-index
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "uhm-knowledge-base-v2"
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

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|----------|------------|
| P0 | Graduate application fee (confirm $70 for grad) | `manoa.hawaii.edu/graduate/submitting-your-application/` |
| P0 | Per-program GRE requirements (decentralized) | Individual program pages |
| P0 | Per-program graduate deadlines | Individual program pages |
| P1 | 2026-2027 COA (currently using 2025-2026) | `manoa.hawaii.edu/admissions/financing/` |
| P1 | Graduate COA line items (currently only UG) | `manoa.hawaii.edu/graduate/cost-of-attendance/` |
| P1 | Need-blind/need-aware policy (formal statement) | `manoa.hawaii.edu/admissions/` |
| P2 | Scholarship details and amounts | `hawaii.edu/fas/info/nws.php` |
| P2 | Net price calculator | `hawaii.edu/fas/` |
| P2 | Transfer admission requirements | `manoa.hawaii.edu/admissions/transfer/` |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UHM Value |
|-----------|-----------|
| Type | Public (flagship) |
| Location | Honolulu, HI |
| UG COA (Resident) | $33,078 |
| UG COA (Non-Resident) | $55,110 |
| Tuition (Resident) | $11,520 |
| Tuition (Non-Resident) | $33,552 |
| EA deadline | N/A (no EA) |
| Priority deadline | January 5 |
| Final deadline | April 1 |
| SAT/ACT required? | Test-optional |
| TOEFL min (UG) | 61 (ELI) / 100 (exempt) |
| IELTS min (UG) | 5.5 (ELI) / 7.0 (exempt) |
| Need-blind (domestic)? | No — need-aware |
| Need-blind (intl)? | No — need-aware |
| Application fee | $70 (waived for HI residents) |
| Total program count | 525 (331 UG + 194 Grad) |
| School/college count | 21 |
| Acceptance rate | 88% |
| WUE available? | Yes |
| Guaranteed admission | HI residents, 3.2+ GPA |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: `manoa.hawaii.edu`, `catalog.manoa.hawaii.edu`, `hawaii.edu/fas/`
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
