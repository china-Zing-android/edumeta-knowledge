# University of North Carolina at Chapel Hill (UNC) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BSPH/BMUS/etc.) | 92 |
| 本科辅修 (Minor) | 106 |
| 研究生学位项目 (MA/MS/PhD/MBA/JD/MD/etc.) | 73+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | N/A |
| **学位项目总计 (UG + Grad)** | **271+** |
| 学院 / 独立系所总数 | 13 |

**Source**: catalog.unc.edu undergraduate programs-study page (205 total: 92 majors, 106 minors, 7 other); catalog.unc.edu graduate degree-programs page (73 departments); gradschool.unc.edu degree-programs/otherschools page (professional programs)

---

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of North Carolina at Chapel Hill
├── College of Arts and Sciences (General College)          [学院]
│   ├── Aerospace Studies                                   [系]
│   ├── African, African American, and Diaspora Studies      [系]
│   ├── American Studies                                    [系]
│   ├── Anthropology                                        [系]
│   ├── Archaeology                                         [系]
│   ├── Art History                                         [系]
│   ├── Asian Studies                                       [系]
│   ├── Biology                                             [系]
│   ├── Chemistry                                           [系]
│   ├── Classics                                            [系]
│   ├── Communication Studies                               [系]
│   ├── Computer Science                                    [系]
│   ├── Contemporary European Studies                       [系]
│   ├── Dramatic Art                                        [系]
│   ├── Economics                                           [系]
│   ├── English and Comparative Literature                  [系]
│   ├── Environment, Ecology and Energy                     [系]
│   ├── Exercise and Sport Science                          [系]
│   ├── Geography and Environment                           [系]
│   ├── Geological Sciences                                 [系]
│   ├── Germanic and Slavic Languages and Literatures       [系]
│   ├── Global Studies                                      [系]
│   ├── History                                             [系]
│   ├── Linguistics                                         [系]
│   ├── Mathematics                                         [系]
│   ├── Music                                               [系]
│   ├── Peace, War, and Defense                             [系]
│   ├── Philosophy                                          [系]
│   ├── Physics and Astronomy                               [系]
│   ├── Political Science                                   [系]
│   ├── Psychology                                          [系]
│   ├── Public Policy                                       [系]
│   ├── Religious Studies                                   [系]
│   ├── Romance Languages and Literatures                   [系]
│   ├── Sociology                                           [系]
│   ├── Statistics and Analytics                            [系]
│   ├── Studio Art                                          [系]
│   └── Women's and Gender Studies                          [系]
├── Kenan-Flagler Business School                           [学院]
│   └── Business Administration                             [系]
├── School of Civic Life and Leadership                     [学院]
├── School of Data and Information Sciences                 [学院]
│   ├── Information Science                                 [系]
│   └── Data Science                                        [系]
├── School of Education                                     [学院]
│   ├── Education                                           [系]
│   ├── Human Development and Family Science                [系]
│   └── Elementary Education                                [系]
├── School of Government                                    [学院]
├── Hussman School of Journalism and Media                  [学院]
│   └── Media and Journalism                                [系]
├── Adams School of Dentistry                               [学院]
│   └── Dental Hygiene                                      [系]
├── School of Medicine: Department of Health Sciences        [学院]
│   ├── Clinical Laboratory Science                         [系]
│   ├── Radiologic Science                                  [系]
│   └── Neurodiagnostics and Sleep Science                  [系]
├── School of Nursing                                       [学院]
│   └── Nursing                                             [系]
├── Eshelman School of Pharmacy                             [学院]
│   └── Pharmaceutical Sciences                             [系]
├── Gillings School of Global Public Health                 [学院]
│   ├── Biostatistics                                       [系]
│   ├── Community and Global Public Health                  [系]
│   ├── Environmental Health Sciences                       [系]
│   ├── Health Policy and Management                        [系]
│   └── Nutrition                                           [系]
└── School of Social Work                                   [学院] (graduate only)
```

**Note**: UNC has 13 schools/colleges. The College of Arts and Sciences is the largest, housing most undergraduate majors. Professional schools (Business, Education, Government, Journalism, Dentistry, Medicine, Nursing, Pharmacy, Public Health) offer specialized programs.

**Source**: catalog.unc.edu/undergraduate/schools-college/

---

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 45 |
| BS | Bachelor of Science | 本科 | 18 |
| BSPH | Bachelor of Science in Public Health | 本科 | 5 |
| BFA | Bachelor of Fine Arts | 本科 | 1 |
| BMus | Bachelor of Music | 本科 | 1 |
| BSBA | Bachelor of Science in Business Administration | 本科 | 1 |
| BA.Ed | Bachelor of Arts in Education | 本科 | 2 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| DDS | Doctor of Dental Surgery | 本科(专业) | 1 |
| PharmD | Doctor of Pharmacy | 本科(专业) | 1 |
| **本科小计** | | | **76+** |
| MA | Master of Arts | 研究生 | 20+ |
| MS | Master of Science | 研究生 | 25+ |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MAC | Master of Accounting | 研究生 | 1 |
| MCRP | Master of City and Regional Planning | 研究生 | 1 |
| MEd | Master of Education | 研究生 | 5+ |
| MAT | Master of Arts in Teaching | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MHS | Master of Health Sciences | 研究生 | 1 |
| MCLS | Master of Clinical Laboratory Sciences | 研究生 | 1 |
| MRS | Master of Radiologic Science | 研究生 | 1 |
| MAPS | Master of Applied Professional Studies | 研究生 | 1 |
| JD | Juris Doctor | 研究生(专业) | 1 |
| LLM | Master of Law | 研究生(专业) | 1 |
| MD | Doctor of Medicine | 研究生(专业) | 1 |
| AuD | Doctor of Audiology | 研究生(专业) | 1 |
| DPT | Doctor of Physical Therapy | 研究生(专业) | 1 |
| EdD | Doctor of Education | 研究生(专业) | 1 |
| PhD | Doctor of Philosophy | 研究生 | 50+ |
| **研究生小计** | | | **115+** |

**Source**: catalog.unc.edu undergraduate and graduate program listings

---

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSPH | BFA | BMus | BSBA | BA.Ed | BSN | DDS | PharmD | MA | MS | MFA | MBA | PhD | JD | MD | DPT | EdD | 其他 | 合计 |
|------------|----|----|------|-----|------|------|-------|-----|-----|--------|----|----|-----|-----|-----|----|----|-----|-----|------|------|
| College of Arts & Sciences | 42 | 16 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 18 | 15 | 2 | 0 | 40 | 0 | 0 | 0 | 0 | 0 | 135 |
| Kenan-Flagler Business School | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 5 |
| School of Civic Life & Leadership | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| School of Data & Info Sciences | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| School of Education | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 8 |
| School of Government | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Hussman School of Journalism | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Adams School of Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| School of Medicine | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 5 | 0 | 1 | 1 | 0 | 1 | 13 |
| School of Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| Eshelman School of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| Gillings School of Public Health | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 13 |
| School of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| **合计** | **42** | **21** | **5** | **1** | **1** | **1** | **2** | **1** | **1** | **1** | **21** | **24** | **2** | **1** | **53** | **1** | **1** | **1** | **2** | **7** | **189+** |

**Note**: Counts are approximate based on catalog extraction. Professional programs (JD, MD, DDS, PharmD, DPT, AuD) are counted separately.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UNC's undergraduate programs are housed in 13 schools and colleges. The College of Arts and Sciences (General College) is the primary undergraduate unit, where first-year students and sophomores typically enter. Students with junior standing may enter professional schools. See Section 0.2 for the complete hierarchy tree.

**Source**: catalog.unc.edu/undergraduate/schools-college/

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### African, African American, and Diaspora Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African, African American, and Diaspora Studies | https://catalog.unc.edu/undergraduate/programs-study/african-african-american-diaspora-studies-major-ba/ |

##### American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.unc.edu/undergraduate/programs-study/american-studies-major-ba/ |
| 2 | American Studies – American Indian and Indigenous Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/american-studies-major-ba-american-indian-indigenous-studies-concentration/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.unc.edu/undergraduate/programs-study/anthropology-major-ba/ |

##### Archaeology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology | https://catalog.unc.edu/undergraduate/programs-study/archaeology-major-ba/ |

##### Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.unc.edu/undergraduate/programs-study/art-history-major-ba/ |

##### Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies – Arab Cultures Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-arab-cultures-concentration/ |
| 2 | Asian Studies – Chinese Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-chinese-concentration/ |
| 3 | Asian Studies – Interdisciplinary Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-interdisciplinary-concentration/ |
| 4 | Asian Studies – Japanese Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-japanese-concentration/ |
| 5 | Asian Studies – Korean Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-korean-studies-concentration/ |
| 6 | Asian Studies – Persian Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-persian-studies-concentration/ |
| 7 | Asian Studies – South Asian Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-major-ba-south-asian-studies-concentration/ |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.unc.edu/undergraduate/programs-study/biology-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.unc.edu/undergraduate/programs-study/biology-major-bs/ |
| 2 | Biology – Quantitative Biology Track | https://catalog.unc.edu/undergraduate/programs-study/biology-major-bs-quantitative-biology-track/ |

##### Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.unc.edu/undergraduate/programs-study/chemistry-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.unc.edu/undergraduate/programs-study/chemistry-major-bs/ |
| 2 | Chemistry – Biochemistry Track | https://catalog.unc.edu/undergraduate/programs-study/chemistry-major-bs-biochemistry-track/ |
| 3 | Chemistry – Polymer Track | https://catalog.unc.edu/undergraduate/programs-study/chemistry-major-bs-polymer-track/ |

##### Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics – Classical Archaeology | https://catalog.unc.edu/undergraduate/programs-study/classics-major-ba-classical-archaeology/ |
| 2 | Classics – Classical Civilization | https://catalog.unc.edu/undergraduate/programs-study/classics-major-ba-classical-civilization/ |
| 3 | Classics – Greek, Latin, and Combined Greek and Latin | https://catalog.unc.edu/undergraduate/programs-study/classics-major-ba-greek-latin-combined-greek-latin/ |

##### Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://catalog.unc.edu/undergraduate/programs-study/communication-studies-major-ba/ |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.unc.edu/undergraduate/programs-study/computer-science-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.unc.edu/undergraduate/programs-study/computer-science-major-bs/ |

##### Contemporary European Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Contemporary European Studies | https://catalog.unc.edu/undergraduate/programs-study/contemporary-european-studies-major-ba/ |

##### Dramatic Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dramatic Art | https://catalog.unc.edu/undergraduate/programs-study/dramatic-art-major-ba/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.unc.edu/undergraduate/programs-study/economics-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.unc.edu/undergraduate/programs-study/economics-major-bs/ |

##### English and Comparative Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English and Comparative Literature | https://catalog.unc.edu/undergraduate/programs-study/english-comparative-literature-major-ba/ |

##### Environmental Science/Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.unc.edu/undergraduate/programs-study/environmental-science-major-bs/ |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.unc.edu/undergraduate/programs-study/environmental-studies-major-ba/ |

##### Exercise and Sport Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise and Sport Science – Fitness Professional | https://catalog.unc.edu/undergraduate/programs-study/exercise-sport-science-major-ba-fitness-professional/ |
| 2 | Exercise and Sport Science – General | https://catalog.unc.edu/undergraduate/programs-study/exercise-sport-science-major-ba-general/ |
| 3 | Exercise and Sport Science – Sport Administration | https://catalog.unc.edu/undergraduate/programs-study/exercise-sport-science-major-ba-sport-administration/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise and Sport Science | https://catalog.unc.edu/undergraduate/programs-study/exercise-sport-science-major-bs/ |

##### Geography and Environment
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography and Environment | https://catalog.unc.edu/undergraduate/programs-study/geography-environment-major-ba/ |

##### Geological Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geological Sciences – Earth Science Concentration | https://catalog.unc.edu/undergraduate/programs-study/geological-sciences-major-ba-earth-science-concentration/ |

##### Germanic and Slavic Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Germanic and Slavic Languages – German Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/germanic-slavic-languages-literatures-major-ba-german-studies-concentration/ |
| 2 | Germanic and Slavic Languages – Russian Language and Culture Concentration | https://catalog.unc.edu/undergraduate/programs-study/germanic-slavic-languages-literatures-major-ba-russian-language-culture-concentration/ |
| 3 | Germanic and Slavic Languages – Slavic and East European Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/germanic-slavic-languages-literatures-major-ba-slavic-east-european-studies-concentration/ |

##### Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Studies | https://catalog.unc.edu/undergraduate/programs-study/global-studies-major-ba/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.unc.edu/undergraduate/programs-study/history-major-ba/ |

##### Interdisciplinary Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.unc.edu/undergraduate/programs-study/interdisciplinary-studies-major-ba/ |

##### Latin American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American Studies | https://catalog.unc.edu/undergraduate/programs-study/latin-american-studies-major-ba/ |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.unc.edu/undergraduate/programs-study/linguistics-major-ba/ |

##### Management and Society
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management and Society | https://catalog.unc.edu/undergraduate/programs-study/management-society-major-ba/ |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.unc.edu/undergraduate/programs-study/mathematics-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.unc.edu/undergraduate/programs-study/mathematics-major-bs/ |

##### Medical Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Anthropology | https://catalog.unc.edu/undergraduate/programs-study/medical-anthropology-major-ba/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.unc.edu/undergraduate/programs-study/music-major-ba/ |
###### BMus
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.unc.edu/undergraduate/programs-study/music-major-bachelor-music-bmus/ |

##### Peace, War, and Defense
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Peace, War, and Defense | https://catalog.unc.edu/undergraduate/programs-study/peace-war-defense-major-ba/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.unc.edu/undergraduate/programs-study/philosophy-major-ba/ |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.unc.edu/undergraduate/programs-study/physics-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.unc.edu/undergraduate/programs-study/physics-major-bs/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.unc.edu/undergraduate/programs-study/political-science-major-ba/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.unc.edu/undergraduate/programs-study/psychology-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.unc.edu/undergraduate/programs-study/psychology-major-bs/ |

##### Public Policy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy | https://catalog.unc.edu/undergraduate/programs-study/public-policy-major-ba/ |

##### Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://catalog.unc.edu/undergraduate/programs-study/religious-studies-major-ba/ |
| 2 | Religious Studies – Jewish Studies Concentration | https://catalog.unc.edu/undergraduate/programs-study/religious-studies-major-ba-jewish-studies-concentration/ |

##### Romance Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Romance Languages – French and Francophone Studies | https://catalog.unc.edu/undergraduate/programs-study/romance-languages-major-ba-french-francophone-studies/ |
| 2 | Romance Languages – Hispanic Linguistics | https://catalog.unc.edu/undergraduate/programs-study/romance-languages-major-ba-hispanic-linguistics/ |
| 3 | Romance Languages – Hispanic Studies | https://catalog.unc.edu/undergraduate/programs-study/romance-languages-major-ba-hispanic-studies/ |
| 4 | Romance Languages – Italian | https://catalog.unc.edu/undergraduate/programs-study/romance-languages-major-ba-italian/ |
| 5 | Romance Languages – Portuguese | https://catalog.unc.edu/undergraduate/programs-study/romance-languages-major-ba-portuguese/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.unc.edu/undergraduate/programs-study/sociology-major-ba/ |

##### Statistics and Analytics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics and Analytics | https://catalog.unc.edu/undergraduate/programs-study/statistics-analytics-major-bs/ |

##### Studio Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art | https://catalog.unc.edu/undergraduate/programs-study/studio-art-major-ba/ |
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art | https://catalog.unc.edu/undergraduate/programs-study/studio-art-major-bachelor-fine-arts-bfa/ |

##### Women's and Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's and Gender Studies | https://catalog.unc.edu/undergraduate/programs-study/womens-gender-studies-major-ba/ |

---

#### Kenan-Flagler Business School

##### Business Administration
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.unc.edu/undergraduate/programs-study/business-administration-major-bsba/ |

---

#### School of Data and Information Sciences

##### Information Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Science | https://catalog.unc.edu/undergraduate/programs-study/information-science-major-bs/ |

##### Data Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.unc.edu/undergraduate/programs-study/data-science-major-ba/ |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.unc.edu/undergraduate/programs-study/data-science-major-bs/ |

---

#### School of Education

##### Education
###### BA.Ed
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.unc.edu/undergraduate/programs-study/elementary-education-major-baed/ |
| 2 | Human Development and Family Science | https://catalog.unc.edu/undergraduate/programs-study/human-development-family-science-major-baed/ |

---

#### Hussman School of Journalism and Media

##### Media and Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Media and Journalism | https://catalog.unc.edu/undergraduate/programs-study/media-journalism-major-ba/ |

---

#### Adams School of Dentistry

##### Dental Hygiene
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://catalog.unc.edu/undergraduate/programs-study/dental-hygiene-major-bs/ |
###### DDS
| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Dental Surgery | https://catalog.unc.edu/undergraduate/programs-study/doctor-dental-surgery-dds/ |

---

#### School of Medicine: Department of Health Sciences

##### Clinical Laboratory Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Laboratory Science | https://catalog.unc.edu/undergraduate/programs-study/clinical-laboratory-science-major-bs/ |

##### Radiologic Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Radiologic Science | https://catalog.unc.edu/undergraduate/programs-study/radiologic-science-major-bs/ |

##### Neurodiagnostics and Sleep Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neurodiagnostics and Sleep Science | https://catalog.unc.edu/undergraduate/programs-study/neurodiagnostics-sleep-science-major-bs/ |

---

#### School of Nursing

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.unc.edu/undergraduate/programs-study/nursing-major-bsn/ |

---

#### Eshelman School of Pharmacy

##### Pharmacy
###### PharmD
| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy | https://catalog.unc.edu/undergraduate/programs-study/doctor-pharmacy-pharmd/ |

---

#### Gillings School of Global Public Health

##### Biostatistics
###### BSPH
| # | 专业 | URL |
|---|------|-----|
| 1 | Biostatistics | https://catalog.unc.edu/undergraduate/programs-study/biostatistics-major-bsph/ |

##### Community and Global Public Health
###### BSPH
| # | 专业 | URL |
|---|------|-----|
| 1 | Community and Global Public Health | https://catalog.unc.edu/undergraduate/programs-study/community-global-public-health-major-bsph/ |

##### Environmental Health Sciences
###### BSPH
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Health Sciences | https://catalog.unc.edu/undergraduate/programs-study/environmental-health-sciences-major-bsph/ |

##### Health Policy and Management
###### BSPH
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Policy and Management | https://catalog.unc.edu/undergraduate/programs-study/health-policy-management-major-bsph/ |

##### Nutrition
###### BSPH
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition | https://catalog.unc.edu/undergraduate/programs-study/nutrition-major-bsph/ |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | Home School(s) | URL |
|---|------|----------------|-----|
| 1 | Applied Sciences, B.S. | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/applied-sciences-bs/ |
| 2 | Geospatial Data Science, B.S. | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/geospatial-data-science-major-bs/ |
| 3 | Human and Organizational Leadership Development, B.A. | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/human-organizational-leadership-development-major-ba/ |
| 4 | Neuroscience, B.S. | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/neuroscience-major-bs/ |
| 5 | Biomedical Engineering, B.S. | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/biomedical-engineering-major-bs/ |
| 6 | Earth and Marine Sciences, B.S. | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/earth-marine-sciences-major-bs/ |

---

### 1.4 Minors — Complete List

| # | Minor Name | Home School/Department | URL |
|---|------------|----------------------|-----|
| 1 | Aerospace Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/aerospace-studies-minor/ |
| 2 | African American and Diaspora Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/african-american-diaspora-studies-minor/ |
| 3 | African Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/african-studies-minor/ |
| 4 | American Indian and Indigenous Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/american-indian-indigenous-studies-minor/ |
| 5 | American Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/american-studies-minor/ |
| 6 | Anthropology (General) | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/anthropology-general-minor/ |
| 7 | Applied Sciences and Engineering | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/applied-sciences-engineering-minor/ |
| 8 | Arabic | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/arabic-minor/ |
| 9 | Archaeology | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/archaeology-minor/ |
| 10 | Art History | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/art-history-minor/ |
| 11 | Artificial Intelligence | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/artificial-intelligence-minor/ |
| 12 | Asian Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/asian-studies-minor/ |
| 13 | Astronomy | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/astronomy-minor/ |
| 14 | Baccalaureate Education in Science and Teaching (BEST) | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/baccalaureate-education-science-teaching-best-minor/ |
| 15 | Biology | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/biology-minor/ |
| 16 | Business Administration | Kenan-Flagler Business School | https://catalog.unc.edu/undergraduate/programs-study/business-administration-minor/ |
| 17 | Business of Health | Kenan-Flagler Business School | https://catalog.unc.edu/undergraduate/programs-study/business-health-minor/ |
| 18 | Chemistry | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/chemistry-minor/ |
| 19 | Chinese | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/chinese-minor/ |
| 20 | Civic Life and Leadership | School of Civic Life & Leadership | https://catalog.unc.edu/undergraduate/programs-study/civic-life-leadership-minor/ |
| 21 | Classical Humanities | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/classical-humanities-minor/ |
| 22 | Climate Change | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/climate-change-minor/ |
| 23 | Coaching Education | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/coaching-education-minor/ |
| 24 | Comparative Literature | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/comparative-literature-minor/ |
| 25 | Computer Science | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/computer-science-minor/ |
| 26 | Conflict Management | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/conflict-management-minor/ |
| 27 | Creative Writing | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/creative-writing-minor/ |
| 28 | Data Science | School of Data & Information Sciences | https://catalog.unc.edu/undergraduate/programs-study/data-science-minor/ |
| 29 | Dramatic Art | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/dramatic-art-minor/ |
| 30 | Economics | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/economics-minor/ |
| 31 | Education | School of Education | https://catalog.unc.edu/undergraduate/programs-study/education-minor/ |
| 32 | Engineering for Environmental Change, Climate, and Health | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/engineering-environmental-change-climate-health-minor/ |
| 33 | English | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/english-minor/ |
| 34 | Entrepreneurship | Kenan-Flagler Business School | https://catalog.unc.edu/undergraduate/programs-study/entrepreneurship-minor/ |
| 35 | Environmental Humanities | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/environmental-humanities-minor/ |
| 36 | Environmental Justice | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/environmental-justice-minor/ |
| 37 | Environmental Microbiology | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/environmental-microbiology-minor/ |
| 38 | Environmental Science and Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/environmental-science-studies-minor/ |
| 39 | Exercise and Sport Science | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/exercise-sport-science-minor/ |
| 40 | Food Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/food-studies-minor/ |
| 41 | French | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/french-minor/ |
| 42 | Geographic Information Sciences | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/geographic-information-sciences-minor/ |
| 43 | Geography | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/geography-minor/ |
| 44 | Geological Sciences | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/geological-sciences-minor/ |
| 45 | German Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/german-studies-minor/ |
| 46 | Global Cinema | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/global-cinema-minor/ |
| 47 | Greek | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/greek-minor/ |
| 48 | Health and Society | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/health-society-minor/ |
| 49 | Heritage and Global Engagement | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/heritage-global-engagement-minor/ |
| 50 | Hindi-Urdu | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/hindi-urdu-minor/ |
| 51 | Hispanic Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/hispanic-studies-minor/ |
| 52 | History | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/history-minor/ |
| 53 | Human Development, Sustainability, and Rights in Africa | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/human-development-sustainability-rights-africa-african-diaspora-minor/ |
| 54 | Hydrology | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/hydrology-minor/ |
| 55 | Information Systems | School of Data & Information Sciences | https://catalog.unc.edu/undergraduate/programs-study/information-systems-minor/ |
| 56 | Islamic and Middle Eastern Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/islamic-middle-eastern-studies-minor/ |
| 57 | Italian | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/italian-minor/ |
| 58 | Japanese | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/japanese-minor/ |
| 59 | Jewish Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/jewish-studies-minor/ |
| 60 | Korean | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/korean-minor/ |
| 61 | Latin | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/latin-minor/ |
| 62 | Latina/o Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/latinao-studies-minor/ |
| 63 | Law, Government, and Public Service | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/law-government-public-service-minor/ |
| 64 | Linguistics | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/linguistics-minor/ |
| 65 | Marine Sciences | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/marine-sciences-minor/ |
| 66 | Mathematics | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/mathematics-minor/ |
| 67 | Media and Journalism | Hussman School of Journalism | https://catalog.unc.edu/undergraduate/programs-study/media-journalism-minor/ |
| 68 | Medical Anthropology | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/medical-anthropology-minor/ |
| 69 | Medicine, Literature, and Culture | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/medicine-literature-culture-minor/ |
| 70 | Medieval and Early Modern Studies (MEMS) | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/medieval-early-modern-studies-mems-minor/ |
| 71 | Middle Eastern Languages | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/middle-eastern-languages-minor/ |
| 72 | Military Science and Leadership | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/military-science-leadership-minor/ |
| 73 | Modern Hebrew | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/modern-hebrew-minor/ |
| 74 | Music | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/music-minor/ |
| 75 | Musical Theatre Performance | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/musical-theatre-performance-minor/ |
| 76 | Naval Science | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/naval-science-minor/ |
| 77 | Neurodiagnostics and Sleep Science | School of Medicine | https://catalog.unc.edu/undergraduate/programs-study/neurodiagnostics-sleep-science-minor/ |
| 78 | Neuroscience | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/neuroscience-minor/ |
| 79 | Peace, War, and Defense | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/peace-war-defense-minor/ |
| 80 | Persian | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/persian-minor/ |
| 81 | Pharmaceutical Sciences | Eshelman School of Pharmacy | https://catalog.unc.edu/undergraduate/programs-study/pharmaceutical-sciences-minor/ |
| 82 | Philosophy | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/philosophy-minor/ |
| 83 | Philosophy, Politics, and Economics (PPE) | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/philosophy-politics-economics-ppe-minor/ |
| 84 | Physics | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/physics-minor/ |
| 85 | Portuguese | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/portuguese-minor/ |
| 86 | Public Policy | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/public-policy-minor/ |
| 87 | Real Estate | Kenan-Flagler Business School | https://catalog.unc.edu/undergraduate/programs-study/real-estate-minor/ |
| 88 | Religious Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/religious-studies-minor/ |
| 89 | Risk Management | Kenan-Flagler Business School | https://catalog.unc.edu/undergraduate/programs-study/risk-management-minor/ |
| 90 | Russian Culture | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/russian-culture-minor/ |
| 91 | Screenwriting | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/screenwriting-minor/ |
| 92 | Sexuality Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/sexuality-studies-minor/ |
| 93 | Slavic and East European Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/slavic-east-european-studies-minor/ |
| 94 | Social and Economic Justice | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/social-economic-justice-minor/ |
| 95 | Southeast Asian Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/southeast-asian-studies-minor/ |
| 96 | Spanish Minor for the Professions | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/spanish-minor-professions/ |
| 97 | Speech and Hearing Sciences | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/speech-hearing-sciences-minor/ |
| 98 | Sports Medicine | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/sports-medicine-minor/ |
| 99 | Statistics and Analytics | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/statistics-analytics-minor/ |
| 100 | Studio Art | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/studio-art-minor/ |
| 101 | Study of Christianity and Culture | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/study-christianity-culture-minor/ |
| 102 | Sustainability Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/sustainability-studies-minor/ |
| 103 | Translation and Interpreting | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/translation-interpreting-minor/ |
| 104 | Urban Studies and Planning | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/urban-studies-planning-minor/ |
| 105 | Women's and Gender Studies | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/womens-gender-studies-minor/ |
| 106 | Writing, Editing, and Digital Publishing | College of Arts & Sciences | https://catalog.unc.edu/undergraduate/programs-study/writing-editing-digital-publishing-minor/ |

---

### 1.5 General/Institute-Wide Requirements

UNC requires the **IDEAs in Action Curriculum** for all undergraduate students. This general education framework includes:
- First-Year Foundations (FY-SEMINAR, FY-LAUNCH, FY-RESEARCH)
- Focus Capacities (7 capacities: Aesthetic and Interpretive Analysis, Creative Expression, Engaged Learning, Ethical and Civic Values, Global Understanding and Engagement, Natural Science and Quantitative Reasoning, Social Inquiry and Analysis)
- Connections (3 courses that bridge disciplines)
- Research and Discovery (high-impact experiences)
- Reflection and Integration (capstone)

**Source**: catalog.unc.edu/undergraduate/ideas-in-action/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### American Studies
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | American Studies | https://catalog.unc.edu/graduate/schools-departments/american-studies/ |

##### Anthropology
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Anthropology | https://catalog.unc.edu/graduate/schools-departments/anthropology/ |

##### Art and Art History
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Art History | https://catalog.unc.edu/graduate/schools-departments/art/ |
| 2 | MFA | Studio Art | https://catalog.unc.edu/graduate/schools-departments/art/ |

##### Biology
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Biology | https://catalog.unc.edu/graduate/schools-departments/biology/ |

##### Chemistry
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Chemistry | https://catalog.unc.edu/graduate/schools-departments/chemistry/ |
| 2 | PhD | Chemistry | https://catalog.unc.edu/graduate/schools-departments/chemistry/ |

##### Classics
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Classics | https://catalog.unc.edu/graduate/schools-departments/classics/ |

##### Communication Studies
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Communication Studies | https://catalog.unc.edu/graduate/schools-departments/communication/ |

##### Computer Science
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Computer Science | https://catalog.unc.edu/graduate/schools-departments/computer-science/ |
| 2 | PhD | Computer Science | https://catalog.unc.edu/graduate/schools-departments/computer-science/ |

##### Dramatic Art
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MFA | Dramatic Art | https://catalog.unc.edu/graduate/schools-departments/dramatic-art/ |

##### Economics
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Economics | https://catalog.unc.edu/graduate/schools-departments/economics/ |
| 2 | PhD | Economics | https://catalog.unc.edu/graduate/schools-departments/economics/ |

##### English and Comparative Literature
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | English | https://catalog.unc.edu/graduate/schools-departments/english-comparative-literature/ |
| 2 | PhD | English | https://catalog.unc.edu/graduate/schools-departments/english-comparative-literature/ |

##### Environment, Ecology and Energy
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Environment, Ecology and Energy | https://catalog.unc.edu/graduate/schools-departments/environment-ecology/ |
| 2 | PhD | Environment, Ecology and Energy | https://catalog.unc.edu/graduate/schools-departments/environment-ecology/ |

##### Geography
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Geography | https://catalog.unc.edu/graduate/schools-departments/geography/ |
| 2 | PhD | Geography | https://catalog.unc.edu/graduate/schools-departments/geography/ |

##### History
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | History | https://catalog.unc.edu/graduate/schools-departments/history/ |
| 2 | PhD | History | https://catalog.unc.edu/graduate/schools-departments/history/ |

##### Linguistics
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Linguistics | https://catalog.unc.edu/graduate/schools-departments/linguistics/ |
| 2 | PhD | Linguistics | https://catalog.unc.edu/graduate/schools-departments/linguistics/ |

##### Mathematics
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Mathematics | https://catalog.unc.edu/graduate/schools-departments/mathematics/ |
| 2 | PhD | Mathematics | https://catalog.unc.edu/graduate/schools-departments/mathematics/ |

##### Music
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Musicology | https://catalog.unc.edu/graduate/schools-departments/music/ |

##### Philosophy
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Philosophy | https://catalog.unc.edu/graduate/schools-departments/philosophy/ |
| 2 | PhD | Philosophy | https://catalog.unc.edu/graduate/schools-departments/philosophy/ |

##### Physics and Astronomy
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Physics | https://catalog.unc.edu/graduate/schools-departments/physics-astronomy/ |
| 2 | PhD | Physics | https://catalog.unc.edu/graduate/schools-departments/physics-astronomy/ |

##### Political Science
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Political Science | https://catalog.unc.edu/graduate/schools-departments/political-science/ |

##### Psychology
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Psychology | https://catalog.unc.edu/graduate/schools-departments/psychology/ |

##### Public Policy
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MPP | Public Policy | https://catalog.unc.edu/graduate/schools-departments/public-policy/ |
| 2 | PhD | Public Policy | https://catalog.unc.edu/graduate/schools-departments/public-policy/ |

##### Religious Studies
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Religious Studies | https://catalog.unc.edu/graduate/schools-departments/religious-studies/ |
| 2 | PhD | Religious Studies | https://catalog.unc.edu/graduate/schools-departments/religious-studies/ |

##### Romance Languages and Literatures
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Romance Languages | https://catalog.unc.edu/graduate/schools-departments/romance-languages/ |
| 2 | PhD | Romance Languages | https://catalog.unc.edu/graduate/schools-departments/romance-languages/ |

##### Sociology
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PhD | Sociology | https://catalog.unc.edu/graduate/schools-departments/sociology/ |

##### Statistics and Operations Research
| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MS | Statistics | https://catalog.unc.edu/graduate/schools-departments/statistics-operations-research/ |
| 2 | PhD | Statistics | https://catalog.unc.edu/graduate/schools-departments/statistics-operations-research/ |

---

#### Kenan-Flagler Business School

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MAC | Master of Accounting | https://www.kenan-flagler.unc.edu/programs/mac/ |
| 2 | MBA | Master of Business Administration | https://www.kenan-flagler.unc.edu/programs/mba-portfolio |
| 3 | MS | Business Research | https://catalog.unc.edu/graduate/schools-departments/kenan-flagler-business-school/ |
| 4 | PhD | Business Administration | https://catalog.unc.edu/graduate/schools-departments/kenan-flagler-business-school/ |

---

#### School of Education

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MA | Education | https://catalog.unc.edu/graduate/schools-departments/education/ |
| 2 | MEd | Education | https://catalog.unc.edu/graduate/schools-departments/education/ |
| 3 | MAT | Teaching | https://catalog.unc.edu/graduate/schools-departments/education/ |
| 4 | EdD | Education | https://catalog.unc.edu/graduate/schools-departments/education/ |
| 5 | PhD | Education | https://catalog.unc.edu/graduate/schools-departments/education/ |
| 6 | MSA | School Administration | https://soe.unc.edu/services/apply/grad/ |

---

#### School of Government

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MPA | Public Administration | https://catalog.unc.edu/graduate/schools-departments/government/ |

---

#### School of Law

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | JD | Juris Doctor | https://law.unc.edu/academics/degree-programs/ |
| 2 | LLM | Master of Law for Foreign Lawyers | https://law.unc.edu/academics/degree-programs/ |

---

#### Adams School of Dentistry

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | DDS | Doctor of Dental Surgery | https://www.dentistry.unc.edu/academicprograms/dds/ |
| 2 | MS | Dental Hygiene Education | https://catalog.unc.edu/graduate/schools-departments/dentistry/ |
| 3 | MS | Various dental specialties | https://catalog.unc.edu/graduate/schools-departments/dentistry/ |
| 4 | PhD | Oral and Craniofacial Biomedicine | https://catalog.unc.edu/graduate/schools-departments/dentistry/ |

---

#### School of Medicine

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MD | Doctor of Medicine | https://www.med.unc.edu/md/ |
| 2 | AuD | Doctor of Audiology | https://www.med.unc.edu/healthsciences/sphs/prospective-students/doctor-of-audiology/ |
| 3 | DPT | Doctor of Physical Therapy | https://www.med.unc.edu/healthsciences/physical/Programs/DPT |
| 4 | MHS | Physician Assistant Studies | https://www.med.unc.edu/healthsciences/unc-pa/ |
| 5 | MCLS | Clinical Laboratory Sciences | https://www.med.unc.edu/healthsciences/clinical/ |
| 6 | MRS | Radiologic Science | https://www.med.unc.edu/healthsciences/radisci/ed-programs/ra/admissions |
| 7 | PhD | Various biomedical sciences | https://catalog.unc.edu/graduate/schools-departments/ (multiple departments) |

---

#### School of Nursing

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MSN | Nursing | https://catalog.unc.edu/graduate/schools-departments/nursing/ |
| 2 | PhD | Nursing | https://catalog.unc.edu/graduate/schools-departments/nursing/ |

---

#### Eshelman School of Pharmacy

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | PharmD | Doctor of Pharmacy | https://pharmacy.unc.edu/education/pharmd/ |
| 2 | MS | Pharmaceutical Sciences | https://catalog.unc.edu/graduate/schools-departments/pharmaceutical-sciences/ |
| 3 | PhD | Pharmaceutical Sciences | https://catalog.unc.edu/graduate/schools-departments/pharmaceutical-sciences/ |

---

#### Gillings School of Global Public Health

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MPH | Public Health | https://catalog.unc.edu/graduate/schools-departments/public-health/ |
| 2 | MS | Biostatistics | https://catalog.unc.edu/graduate/schools-departments/biostatistics/ |
| 3 | MS | Environmental Sciences and Engineering | https://catalog.unc.edu/graduate/schools-departments/environmental-sciences-engineering/ |
| 4 | MS | Nutrition | https://catalog.unc.edu/graduate/schools-departments/nutrition/ |
| 5 | PhD | Biostatistics | https://catalog.unc.edu/graduate/schools-departments/biostatistics/ |
| 6 | PhD | Epidemiology | https://catalog.unc.edu/graduate/schools-departments/epidemiology/ |
| 7 | PhD | Health Behavior | https://catalog.unc.edu/graduate/schools-departments/health-behavior/ |
| 8 | PhD | Health Policy and Management | https://catalog.unc.edu/graduate/schools-departments/health-policy-management/ |
| 9 | PhD | Environmental Sciences and Engineering | https://catalog.unc.edu/graduate/schools-departments/environmental-sciences-engineering/ |
| 10 | PhD | Maternal and Child Health | https://catalog.unc.edu/graduate/schools-departments/maternal-child-health/ |
| 11 | PhD | Nutrition | https://catalog.unc.edu/graduate/schools-departments/nutrition/ |
| 12 | DrPH | Public Health Leadership | https://catalog.unc.edu/graduate/schools-departments/public-health/ |

---

#### School of Social Work

| # | Degree | Program | URL |
|---|--------|---------|-----|
| 1 | MSW | Social Work | https://catalog.unc.edu/graduate/schools-departments/social-work/ |
| 2 | PhD | Social Work | https://catalog.unc.edu/graduate/schools-departments/social-work/ |

---

### 2.2 Graduate Admissions Model

**Decentralized admissions**: Each program sets its own deadlines and requirements. The Graduate School provides the application portal and general requirements.

**Application portal**: https://applynow.unc.edu/apply/
**Application fee**: $95 (non-refundable, per program)
**Fee waivers available**: Yes, for qualifying applicants

**General requirements**:
- Bachelor's degree from accredited institution
- Minimum GPA: 3.0 (B average)
- Official transcripts
- Letters of recommendation (varies by program)
- Statement of purpose
- GRE/GMAT (varies by program - check specific program requirements)
- English proficiency for international applicants

**Source**: gradschool.unc.edu/admissions/instructions/

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Dimension | Details |
|-----------|---------|
| **Application Portal** | Common Application (https://www.commonapp.org/explore/university-north-carolina-chapel-hill) |
| **Early Action (Non-Binding)** | October 15 |
| **Early Action Decision** | By December 20 for NC residents; by February 10 for all others |
| **Regular Decision** | January 15 |
| **Regular Decision Decision** | March 31 |
| **Enrollment Confirmation** | May 1 (both EA and RD) |
| **Financial Aid Deadline** | EA: December 1; RD: March 1 |
| **Residency Deadline** | EA: October 15; RD: February 21 |
| **Supporting Materials Deadline** | EA: November 7; RD: February 21 |
| **SAT/ACT Policy** | Optional with weighted GPA of 2.8 or above on 4.0 scale |
| **Superscore Policy** | Not specified |
| **Application Fee** | Not specified on admissions page (check Common App) |
| **Interview Policy** | Not required |
| **Recommendations** | 1 Letter of Recommendation required |
| **Transcript** | Official Transcript and School Report required |

**Source**: admissions.unc.edu/apply/types-of-applications/first-year/

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified on UG page | - | Required for international students |
| IELTS | Not specified on UG page | - | Required for international students |
| Duolingo | Not specified on UG page | - | May be accepted |

**Note**: International students must submit English proficiency exam scores as required materials. Specific minimums not listed on undergraduate admissions page; contact admissions office.

**Source**: admissions.unc.edu/apply/types-of-applications/international-first-year-students/

### 3.3 Graduate — Global Rules

| Dimension | Details |
|-----------|---------|
| **Application Platform** | UNC Graduate School Online Application |
| **Application Fee** | $95 (non-refundable, per program) |
| **GRE/GMAT Policy** | Varies by program; some require, some optional, some waived |
| **English Proficiency (TOEFL iBT)** | 90 (tests before Jan 26, 2026) or 5 (tests on/after Jan 26, 2026) |
| **English Proficiency (IELTS)** | 7 |
| **English Proficiency (Duolingo)** | 110 |
| **TOEFL Code** | #5816 (no department code) |
| **Score Validity** | No more than 2 years old as of application date |
| **Exemptions** | Degree from accredited US university; degree from English-sole-instruction university |
| **Fall Priority Deadline for Funding** | December 16, 2025 |
| **Final Deadlines** | Vary by program; some close as early as December, others as late as June 9 |
| **Spring Deadlines** | Residential: October 14; Summer: March 10 |

**Source**: gradschool.unc.edu/admissions/instructions/, gradschool.unc.edu/admissions/deadlines/

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

#### In-State Students (Living On Campus)

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $7,230 | Annual tuition |
| Fees | $2,130 | Mandatory fees |
| Housing | $9,168 | On-campus housing |
| Food | $6,702 | Meal plan |
| Books & Supplies | $638 | Course materials |
| Travel | $1,078 | Transportation |
| Loan Fees | $56 | If applicable |
| Personal | $1,950 | Personal expenses |
| **Total** | **$28,952** | |

#### Out-of-State Students (Living On Campus)

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $47,472 | Annual tuition |
| Fees | $2,130 | Mandatory fees |
| Housing | $9,168 | On-campus housing |
| Food | $6,702 | Meal plan |
| Books & Supplies | $638 | Course materials |
| Travel | $2,050 | Transportation |
| Loan Fees | $56 | If applicable |
| Personal | $1,950 | Personal expenses |
| **Total** | **$70,166** | |

**Source**: studentaid.unc.edu/incoming/costs/

### 4.2 Undergraduate Financial-Aid Policy

| Dimension | Details |
|-----------|---------|
| **Need-Blind Admissions** | Yes (for US citizens/permanent residents) |
| **Need-Aware for Internationals** | Yes |
| **Meets Demonstrated Need** | Yes, 100% |
| **Carolina Covenant** | Debt-free financial aid for students with demonstrated need |
| **Students Receiving Aid** | Nearly half of admitted students |
| **Graduate with No Federal Loan Debt** | 60% |
| **International Students** | Not eligible for need-based financial aid; must pay full OOS cost |

**Source**: admissions.unc.edu/afford/, studentaid.unc.edu/

### 4.3 Graduate Cost & Funding Framework

#### In-State Graduate (Living On Campus, 2026-2027)

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $10,764 | Annual tuition |
| Fees | $2,134 | Mandatory fees |
| Housing | $10,458 | On-campus housing |
| Food | $6,702 | Meal plan |
| Books & Supplies | $474 | Course materials |
| Travel | $1,448 | Transportation |
| Health Insurance | $3,606 | Required |
| Loan Fees | $262 | If applicable |
| Personal | $3,100 | Personal expenses |
| **Total** | **$39,882** | |

#### Out-of-State Graduate (Living On Campus, 2026-2027)

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $29,422 | Annual tuition |
| Fees | $2,134 | Mandatory fees |
| Housing | $10,458 | On-campus housing |
| Food | $6,702 | Meal plan |
| Books & Supplies | $474 | Course materials |
| Travel | $1,448 | Transportation |
| Health Insurance | $3,606 | Required |
| Loan Fees | $262 | If applicable |
| Personal | $3,100 | Personal expenses |
| **Total** | **$58,540** | |

**Funding types**: Fellowships, Research Assistantships (RA), Teaching Assistantships (TA), grants, loans

**Source**: studentaid.unc.edu/graduate/costs/, gradschool.unc.edu/funding/

---

## SECTION 5 — Evidence Chain Index

```yaml
---
field: undergraduate.deadlines.ea
value: October 15
source_url: https://admissions.unc.edu/apply/types-of-applications/first-year/
source_snippet: "Application Deadline – October 15"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: undergraduate.deadlines.rd
value: January 15
source_url: https://admissions.unc.edu/apply/types-of-applications/first-year/
source_snippet: "Application Deadline – January 15"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: undergraduate.test_policy
value: "Optional with weighted GPA of 2.8 or above on 4.0 scale"
source_url: https://admissions.unc.edu/apply/types-of-applications/first-year/
source_snippet: "SAT or ACT Scores (optional with a weighted GPA of 2.8 or above on a 4.0 scale)"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: undergraduate.cost.tuition_in_state
value: $7,230
source_url: https://studentaid.unc.edu/incoming/costs/
source_snippet: "Tuition $7230"
capture_date: 2026-07-05
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_out_of_state
value: $47,472
source_url: https://studentaid.unc.edu/incoming/costs/
source_snippet: "Tuition $47,472"
capture_date: 2026-07-05
evidence_type: official_webpage_table
---
field: undergraduate.cost.total_in_state_on_campus
value: $28,952
source_url: https://studentaid.unc.edu/incoming/costs/
source_snippet: "Total $28,952"
capture_date: 2026-07-05
evidence_type: official_webpage_table
---
field: undergraduate.cost.total_out_state_on_campus
value: $70,166
source_url: https://studentaid.unc.edu/incoming/costs/
source_snippet: "Total $70,166"
capture_date: 2026-07-05
evidence_type: official_webpage_table
---
field: undergraduate.aid.need_blind
value: Yes (US citizens/permanent residents)
source_url: https://admissions.unc.edu/afford/
source_snippet: "We are committed to meeting 100 percent of your family's demonstrated financial need."
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: undergraduate.aid.need_aware_intl
value: Yes
source_url: https://admissions.unc.edu/apply/types-of-applications/international-first-year-students/
source_snippet: "International students aren't eligible to receive need-based financial aid, so you'll want to be prepared to pay the full cost of attendance"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: graduate.application_fee
value: $95
source_url: https://gradschool.unc.edu/admissions/instructions/
source_snippet: "Application fee (non-refundable $95.00)"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: graduate.english_proficiency.toefl
value: 90 (before Jan 26, 2026) or 5 (after Jan 26, 2026)
source_url: https://gradschool.unc.edu/admissions/instructions/
source_snippet: "The internet-based TOEFL exam: TOEFL tests taken prior to January 26, 2026 = 90 TOEFL tests taken on or after January 26, 2026 = 5"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: graduate.english_proficiency.ielts
value: 7
source_url: https://gradschool.unc.edu/admissions/instructions/
source_snippet: "The IELTS exam = 7"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: graduate.english_proficiency.duolingo
value: 110
source_url: https://gradschool.unc.edu/admissions/instructions/
source_snippet: "Duolingo English Test = 110"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: graduate.cost.tuition_in_state
value: $10,764
source_url: https://studentaid.unc.edu/graduate/costs/
source_snippet: "Tuition $10,764"
capture_date: 2026-07-05
evidence_type: official_webpage_table
---
field: graduate.cost.tuition_out_of_state
value: $29,422
source_url: https://studentaid.unc.edu/graduate/costs/
source_snippet: "Tuition $29422"
capture_date: 2026-07-05
evidence_type: official_webpage_table
---
field: programs.undergraduate.total
value: 205 (92 majors, 106 minors, 7 other)
source_url: https://catalog.unc.edu/undergraduate/programs-study/
source_snippet: Extracted from page links
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: programs.graduate.departments
value: 73
source_url: https://catalog.unc.edu/graduate/degree-programs/
source_snippet: Extracted from "By Name" section
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: institution.schools_count
value: 13
source_url: https://catalog.unc.edu/undergraduate/schools-college/
source_snippet: Listed schools/colleges under Division of Academic Affairs and Division of Health Affairs
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: graduate.funding_priority_deadline
value: December 16, 2025
source_url: https://gradschool.unc.edu/admissions/deadlines/
source_snippet: "We recommend that individuals who wish to be considered for Graduate School funding submit complete applications by December 16, 2025"
capture_date: 2026-07-05
evidence_type: official_webpage
---
field: undergraduate.aid.carolina_covenant
value: Debt-free financial aid for students with demonstrated need
source_url: https://studentaid.unc.edu/incoming/what-aid-is-available/carolina-covenant/
source_snippet: "The Carolina Covenant"
capture_date: 2026-07-05
evidence_type: official_webpage
---
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
unc-knowledge-base-v2/
├── 00-overview/
│   ├── 01-program-counts.md (Section 0.1)
│   ├── 02-hierarchy-tree.md (Section 0.2)
│   ├── 03-degree-inventory.md (Section 0.3)
│   └── 04-distribution-matrix.md (Section 0.4)
├── 01-undergraduate/
│   ├── college-of-arts-sciences.md (Section 1.2)
│   ├── kenan-flagler-business.md (Section 1.2)
│   ├── school-of-education.md (Section 1.2)
│   ├── school-of-data-info-sciences.md (Section 1.2)
│   ├── hussman-journalism.md (Section 1.2)
│   ├── adams-dentistry.md (Section 1.2)
│   ├── school-of-medicine-health-sciences.md (Section 1.2)
│   ├── school-of-nursing.md (Section 1.2)
│   ├── eshelman-pharmacy.md (Section 1.2)
│   ├── gillings-public-health.md (Section 1.2)
│   └── minors-complete-list.md (Section 1.4)
├── 02-graduate/
│   ├── college-of-arts-sciences-grad.md (Section 2.1)
│   ├── kenan-flagler-grad.md (Section 2.1)
│   ├── school-of-education-grad.md (Section 2.1)
│   ├── school-of-law.md (Section 2.1)
│   ├── school-of-medicine-grad.md (Section 2.1)
│   ├── school-of-nursing-grad.md (Section 2.1)
│   ├── eshelman-pharmacy-grad.md (Section 2.1)
│   ├── gillings-public-health-grad.md (Section 2.1)
│   └── school-of-social-work-grad.md (Section 2.1)
├── 03-admissions/
│   ├── undergraduate-deadlines.md (Section 3.1)
│   ├── english-proficiency.md (Section 3.2)
│   └── graduate-admissions.md (Section 3.3)
├── 04-costs/
│   ├── undergraduate-costs.md (Section 4.1)
│   ├── financial-aid-policy.md (Section 4.2)
│   └── graduate-costs.md (Section 4.3)
└── 05-evidence/
    └── evidence-chain.md (Section 5)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "unc-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Specific application fee for undergraduate | https://admissions.unc.edu/apply/get-started/ |
| P0 | Detailed SAT/ACT score ranges (middle 50%) | https://admissions.unc.edu/explore/our-newest-class/ |
| P1 | Per-program graduate deadlines | https://gradschool.unc.edu/programs/ |
| P1 | Graduate funding details (fellowships, stipends) | https://gradschool.unc.edu/funding/ |
| P2 | Transfer admission requirements | https://admissions.unc.edu/apply/types-of-applications/transfer/ |
| P2 | Honors Carolina requirements | https://admissions.unc.edu/honors-carolina/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UNC Value | Notes |
|-----------|-----------|-------|
| **Total UG Programs** | 205 (92 majors, 106 minors) | |
| **Total Grad Departments** | 73+ | |
| **Schools/Colleges** | 13 | |
| **UG Tuition In-State** | $7,230/yr | |
| **UG Tuition OOS** | $47,472/yr | |
| **UG Total COA In-State** | $28,952/yr | Living on campus |
| **UG Total COA OOS** | $70,166/yr | Living on campus |
| **EA Deadline** | October 15 | Non-binding |
| **RD Deadline** | January 15 | |
| **SAT/ACT Required** | Optional (GPA 2.8+) | |
| **TOEFL Min (Grad)** | 90 (before 1/26/26) or 5 (after) | |
| **IELTS Min (Grad)** | 7 | |
| **Need-Blind (US)** | Yes | |
| **Need-Aware (Intl)** | Yes | |
| **Meets Demonstrated Need** | Yes, 100% | |
| **Grad Application Fee** | $95 | Per program |
| **Grad Funding Priority** | December 16 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.unc.edu, studentaid.unc.edu, catalog.unc.edu, gradschool.unc.edu, cashier.unc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
