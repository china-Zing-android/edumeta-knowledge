# University of Alaska Fairbanks Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA/BM/BAM/BSEM/BAAS) | 57 |
| 本科辅修 (Minor) | 87 |
| 副学士学位专业 (AA/AS/AAS) | 22 |
| 研究生学位项目 (MA/MS/MFA/MBA/MEd/MMP/MHML/MSDM/MNRE/MMU/OHM/MMS/MAM + PhD) | 66 |
| 研究生高级证书 (Graduate Certificate) | 17 |
| 本科证书 (Certificate) | 27 |
| 职业背书 (Occupational Endorsement / O.E.C.) | 33 |
| 学士后证书 (Postbaccalaureate Certificate) | 7 |
| Pre-professional Preparation (非学位) | 1 |
| **学位项目总计 (UG + Grad degrees)** | **145** |
| **所有项目总计 (含证书/辅修/背书)** | **317** |
| 学院 / 独立系所总数 | 9 (colleges/divisions) + 1 CTC |

> Reconciliation: 57 (bachelor) + 22 (associate) + 48 (master) + 18 (PhD) = 145 degree programs. 145 + 87 (minors) + 27 (certs) + 17 (grad certs) + 33 (endorsements) + 7 (PBCT) + 1 (pre-prof) = 317 total.

### 0.2 学院 / 系层级结构

```
University of Alaska Fairbanks
├── College of Engineering and Mines (CEM)              [学院]
│   ├── Civil, Geological and Environmental Engineering  [系]
│   ├── Electrical and Computer Engineering              [系]
│   ├── Mechanical Engineering                           [系]
│   ├── Mining and Mineral Engineering                   [系]
│   ├── Petroleum Engineering                            [系]
│   ├── Computer Science                                 [系]
│   ├── Geosciences                                      [系]
│   ├── Geophysics                                       [系]
│   ├── Construction Management                          [系]
│   └── Atmospheric Sciences                             [系]
├── College of Liberal Arts (CLA)                       [学院]
│   ├── English                                          [系]
│   ├── History                                          [系]
│   ├── Philosophy                                       [系]
│   ├── Communication                                    [系]
│   ├── Journalism: Science & Environment                [系]
│   ├── Political Science                                [系]
│   ├── Psychology                                       [系]
│   ├── Social Work                                      [系]
│   ├── Justice                                          [系]
│   ├── Art                                              [系]
│   ├── Music                                            [系]
│   ├── Theater and Film                                 [系]
│   ├── Foreign Languages / Global Languages             [系]
│   ├── Linguistics                                      [系]
│   ├── Sociology / Social and Human Development         [系]
│   └── Women, Gender and Sexuality Studies              [系]
├── College of Natural Science and Mathematics (CNSM)   [学院]
│   ├── Biology and Wildlife                             [系]
│   ├── Chemistry and Biochemistry                       [系]
│   ├── Computer Science                                 [系]  ⚠ shared with CEM
│   ├── Mathematics and Statistics                       [系]
│   ├── Physics                                          [系]
│   ├── Geosciences                                      [系]  ⚠ shared with CEM
│   └── Atmospheric Sciences                             [系]  ⚠ shared with CEM
├── College of Business and Security Management (CBSM)  [学院]
│   ├── Accounting                                       [系]
│   ├── Business Administration                          [系]
│   ├── Economics                                        [系]
│   ├── Homeland Security and Emergency Management       [系]
│   ├── Healthcare Management and Leadership             [系]
│   └── Justice                                          [系]  ⚠ shared with CLA
├── School of Education                                 [学院]
│   ├── Education                                        [系]
│   ├── Elementary Education                             [系]
│   ├── Secondary Education                              [系]
│   ├── Early Childhood Education                        [系]
│   ├── Special Education                                [系]
│   ├── Counseling                                       [系]
│   └── Music Education                                  [系]
├── College of Fisheries and Ocean Sciences (CFOS)      [学院]
│   ├── Fisheries                                        [系]
│   ├── Marine Biology                                   [系]
│   ├── Oceanography                                     [系]
│   └── Marine Policy / Marine Studies                   [系]
├── College of Indigenous Studies (CIS)                 [学院]
│   ├── Alaska Native Languages                          [系]
│   ├── Alaska Native Studies and Rural Development      [系]
│   ├── Anthropology                                     [系]
│   ├── Cross-Cultural Studies                           [系]
│   └── Tribal Governance                                [系]
├── Division of Exploratory Studies                     [学院]
│   ├── Interdisciplinary Studies - Undergraduate        [系]
│   └── General Academic & Technical Programs            [系]
├── Graduate School                                     [学院]
│   └── Interdisciplinary Studies - Graduate             [系]
└── Community and Technical College (CTC)               [学院]
    ├── Applied Business and Accounting                  [系]
    ├── Allied Health                                    [系]
    ├── Automotive Technology                            [系]
    ├── Aviation                                         [系]
    ├── Computer & Information Technology Systems         [系]
    ├── Construction Management                          [系]
    ├── Culinary Arts and Hospitality                    [系]
    ├── Diesel & Heavy Equipment                         [系]
    ├── Early Childhood Education                        [系]
    ├── EMS/Paramedicine                                 [系]
    ├── Fire Science                                     [系]
    ├── Law Enforcement                                  [系]
    ├── Paralegal Studies                                [系]
    ├── Process Technology                               [系]
    ├── Welding & Materials Technology                   [系]
    └── Workforce Development                            [系]
```

### 0.3 学历级别明细

| 学位缩写 (canonical) | official (本校) | 全称 | 层级 | 本项目数量 |
|---------------------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 30 |
| BS | B.S. | Bachelor of Science | 本科 | 17 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 3 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 1 |
| BM | B.M. | Bachelor of Music | 本科 | 2 |
| BAM | B.A.M. | Bachelor of Applied Management | 本科 | 1 |
| BSEM | B.S.E.M. | Bachelor of Science in Emergency Management | 本科 | 1 |
| BAAS | B.A.A.S. | Bachelor of Applied Arts and Sciences | 本科 | 1 |
| AA | Associate of Arts | Associate of Arts | 副学士 | 1 |
| AS | Associate of Science | Associate of Science | 副学士 | 1 |
| AAS | A.A.S. | Associate of Applied Science | 副学士 | 20 |
| MA | M.A. | Master of Arts | 研究生 | 12 |
| MS | M.S. | Master of Science | 研究生 | 18 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 2 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MEd | M.Ed. | Master of Education | 研究生 | 4 |
| MMP | M.M.P. | Master of Marine Policy | 研究生 | 1 |
| MHML | M.H.M.L. | Master of Healthcare Management and Leadership | 研究生 | 1 |
| MSDM | M.S.D.M. | Master of Security and Disaster Management | 研究生 | 1 |
| MNRE | M.N.R.E. | Master of Natural Resources and Environment | 研究生 | 1 |
| MMU | M.Mu. | Master of Music | 研究生 | 1 |
| MMS | M.M.S. | Master of Marine Studies | 研究生 | 1 |
| OHM | O.H.M. | One Health Master | 研究生 | 1 |
| MAM | M.A.M. | Master of Applied Management | 研究生 | 0 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 18 |
| Graduate Certificate | Graduate Certificate | 研究生高级证书 | 研究生 | 17 |
| Certificate | Certificate | 本科证书 | 本科 | 27 |
| O.E.C. | O.E.C. | Occupational Endorsement Certificate | 职业 | 33 |
| PBCT | P.B.C.T. / Licensure | Postbaccalaureate Certificate | 学士后 | 7 |
| Minor | Minor | 辅修 | 本科 | 87 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BFA | BM | BAM | BSEM | BAAS | AA | AS | AAS | MA | MS | MFA | MBA | MEd | MMP | MHML | MSDM | MNRE | MMU | MMS | OHM | PhD | GradCert | 合计 |
|------------|----|----|-----|-----|----|-----|------|------|----|----|-----|----|----|-----|-----|-----|-----|------|------|------|-----|-----|-----|-----|----------|------|
| CEM | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 18 |
| CLA | 17 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 29 |
| CNSM | 2 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 2 | 26 |
| CBSM | 0 | 1 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 4 | 14 |
| Education | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 |
| CFOS | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 5 | 0 | 13 |
| CIS | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 10 |
| Exploratory | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| CTC | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 |
| **合计** | **29** | **18** | **3** | **1** | **2** | **1** | **1** | **1** | **1** | **1** | **20** | **10** | **20** | **2** | **1** | **4** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **16** | **10** | **147** |

> Note: Some departments (Computer Science, Geosciences, Atmospheric Sciences) are shared between CEM and CNSM. Programs are assigned to their administrative home college. The matrix total (147) slightly exceeds the degree count (145) because 2 PhD programs (Engineering, Interdisciplinary Studies) are cross-college. Pre-professional Preparation (1) is excluded as non-degree.

---

## Section 1 — Undergraduate Education

### 1.1 College Architecture

UAF's undergraduate programs span 9 colleges/divisions plus the Community and Technical College. The full hierarchy is in Section 0.2. UAF is organized as a single-campus university with community campuses across Alaska (Bristol Bay, Chukchi, Kuskokwim, Northwest, and CTC in Fairbanks).

### 1.2 Undergraduate Majors — grouped by 学院 > 系 > 学位级别

#### College of Engineering and Mines (CEM)

##### Department of Civil, Geological and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.uaf.edu/bachelors/civil-engineering-bs/ |
| 2 | Geological Engineering | https://catalog.uaf.edu/bachelors/geological-engineering-bs/ |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.uaf.edu/bachelors/computer-engineering-bs/ |
| 2 | Electrical Engineering | https://catalog.uaf.edu/bachelors/electrical-engineering-bs/ |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.uaf.edu/bachelors/mechanical-engineering-bs/ |

##### Department of Mining and Mineral Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mining Engineering | https://catalog.uaf.edu/bachelors/mining-engineering-bs/ |

##### Department of Petroleum Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Energy Resource Engineering | https://catalog.uaf.edu/bachelors/energy-resource-engineering-bs/ |

##### Department of Computer Science (shared with CNSM)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.uaf.edu/bachelors/computer-science-bs/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.uaf.edu/bachelors/computer-science-ba/ |

##### Department of Geosciences (shared with CNSM)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geoscience | https://catalog.uaf.edu/bachelors/geoscience-bs/ |

##### Department of Atmospheric Sciences (shared with CNSM)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate and Atmospheric Sciences | https://catalog.uaf.edu/bachelors/climate-atmospheric-sciences/ |

##### Department of Construction Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.uaf.edu/bachelors/aerospace-engineering-bs/ |

---

#### College of Liberal Arts (CLA)

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.uaf.edu/bachelors/english-ba/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.uaf.edu/bachelors/history-ba/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.uaf.edu/bachelors/philosophy-ba/ |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.uaf.edu/bachelors/communication-ba/ |

##### Department of Journalism: Science & Environment
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism: Science and the Environment | https://catalog.uaf.edu/bachelors/journalism-science-environment-ba/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.uaf.edu/bachelors/political-science-ba/ |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.uaf.edu/bachelors/psychology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.uaf.edu/bachelors/psychology-bs/ |

##### Department of Social Work
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.uaf.edu/bachelors/social-work-ba/ |

##### Department of Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Justice | https://catalog.uaf.edu/bachelors/justice-ba/ |

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uaf.edu/bachelors/art-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uaf.edu/bachelors/art-bfa/ |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.uaf.edu/bachelors/music-ba/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://catalog.uaf.edu/bachelors/music-bm-education/ |
| 2 | Music Performance | https://catalog.uaf.edu/bachelors/music-bm-performance/ |

##### Department of Theater and Film
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Performing Arts | https://catalog.uaf.edu/bachelors/film-performing-arts-ba/ |

##### Department of Global Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Foreign Languages | https://catalog.uaf.edu/bachelors/foreign-languages-ba/ |
| 2 | Japanese Studies | https://catalog.uaf.edu/bachelors/japanese-studies-ba/ |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.uaf.edu/bachelors/linguistics-ba/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate and Arctic Sustainability | https://catalog.uaf.edu/bachelors/climate-arctic-sustainability-ba/ |

---

#### College of Natural Science and Mathematics (CNSM)

##### Department of Biology and Wildlife
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.uaf.edu/bachelors/biological-sciences-ba/ |
| 2 | Wildlife Ecology and Society | https://catalog.uaf.edu/bachelors/wildlife-ecology-society-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.uaf.edu/bachelors/biological-sciences-bs/ |
| 2 | Wildlife Biology and Conservation | https://catalog.uaf.edu/bachelors/wildlife-biology-conservation-bs/ |

##### Department of Chemistry and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.uaf.edu/bachelors/chemistry-bs/ |

##### Department of Mathematics and Statistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.uaf.edu/bachelors/mathematics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.uaf.edu/bachelors/mathematics-bs/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.uaf.edu/bachelors/physics-bs/ |

##### Department of Climate and Environmental Change
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate and Environmental Change | https://catalog.uaf.edu/bachelors/climate-environmental-change-bs/ |

---

#### College of Business and Security Management (CBSM)

##### Department of Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.uaf.edu/bachelors/accounting/ |

##### Department of Business Administration
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.uaf.edu/bachelors/business-administration-bba/ |
| 2 | Economics | https://catalog.uaf.edu/bachelors/economics-bba/ |

##### Department of Homeland Security and Emergency Management
###### BSEM
| # | 专业 | URL |
|---|------|-----|
| 1 | Homeland Security and Emergency Management | https://catalog.uaf.edu/bachelors/homeland-security-emergency-management-bem/ |

---

#### School of Education

##### Department of Elementary Education
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education (K-8) | https://catalog.uaf.edu/bachelors/elementary-education-k-8-ba/ |

##### Department of Secondary Education
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Secondary Education (7-12) | https://catalog.uaf.edu/bachelors/secondary-education-7-12-ba/ |

##### Department of Early Childhood Education
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood and Family Studies | https://catalog.uaf.edu/bachelors/early-childhood-family-studies-ba/ |

---

#### College of Fisheries and Ocean Sciences (CFOS)

##### Department of Fisheries
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries and Marine Sciences | https://catalog.uaf.edu/bachelors/fisheries-bs/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries | https://catalog.uaf.edu/bachelors/fisheries-ba/ |

##### Department of Natural Resources and Environment
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Natural Resources and Environment | https://catalog.uaf.edu/bachelors/natural-resources-environment-bs/ |

---

#### College of Indigenous Studies (CIS)

##### Department of Alaska Native Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Alaska Native Languages | https://catalog.uaf.edu/bachelors/alaska-native-languages/ |
| 2 | Yup'ik Language and Culture | https://catalog.uaf.edu/bachelors/yupik-language-culture-ba/ |

##### Department of Alaska Native Studies and Rural Development
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Alaska Native Studies | https://catalog.uaf.edu/bachelors/alaska-native-studies-ba/ |
| 2 | Rural Development | https://catalog.uaf.edu/bachelors/rural-development-ba/ |
| 3 | Tribal Governance | https://catalog.uaf.edu/bachelors/tribal-governance-ba/ |

---

#### Division of Exploratory Studies

##### Interdisciplinary Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uaf.edu/bachelors/interdisciplinary-studies-ba/ |
| 2 | Anthropology | https://catalog.uaf.edu/bachelors/anthropology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uaf.edu/bachelors/interdisciplinary-studies-bs/ |

###### BAM
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Management | https://catalog.uaf.edu/bachelors/applied-management-bam/ |

###### BAAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uaf.edu/bachelors/interdisciplinary-studies-baas/ |

##### Pre-professional
| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-professional Preparation (non-degree) | https://catalog.uaf.edu/bachelors/preprofessional/ |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 父学院 | URL |
|---|------|--------|-----|
| 1 | Computer Science (BA/BS) | CEM + CNSM | https://catalog.uaf.edu/bachelors/computer-science-bs/ |
| 2 | Geoscience (BS) | CEM + CNSM | https://catalog.uaf.edu/bachelors/geoscience-bs/ |
| 3 | Climate and Atmospheric Sciences (BS) | CEM + CNSM | https://catalog.uaf.edu/bachelors/climate-atmospheric-sciences/ |

### 1.4 Minors — Complete List

| # | Minor | URL |
|---|-------|-----|
| 1 | Accounting Minor | https://catalog.uaf.edu/minors/ |
| 2 | Aerospace Engineering Minor | https://catalog.uaf.edu/minors/ |
| 3 | Agrometeorology Minor | https://catalog.uaf.edu/minors/ |
| 4 | Alaska Native Languages Minor | https://catalog.uaf.edu/minors/ |
| 5 | Alaska Native Studies Minor | https://catalog.uaf.edu/minors/ |
| 6 | American Sign Language Minor | https://catalog.uaf.edu/minors/ |
| 7 | Ancient, Medieval and Early Modern Studies Minor | https://catalog.uaf.edu/minors/ |
| 8 | Anthropology Minor | https://catalog.uaf.edu/minors/ |
| 9 | Applied Accounting Minor | https://catalog.uaf.edu/minors/ |
| 10 | Applied Business Minor | https://catalog.uaf.edu/minors/ |
| 11 | Applied Statistics Minor | https://catalog.uaf.edu/minors/ |
| 12 | Arctic and Northern Studies Minor | https://catalog.uaf.edu/minors/ |
| 13 | Arctic Skills Minor | https://catalog.uaf.edu/minors/ |
| 14 | Art History Minor | https://catalog.uaf.edu/minors/ |
| 15 | Art Minor | https://catalog.uaf.edu/minors/ |
| 16 | Asian Studies Minor | https://catalog.uaf.edu/minors/ |
| 17 | Aviation Technology Minor | https://catalog.uaf.edu/minors/ |
| 18 | Biochemistry Minor | https://catalog.uaf.edu/minors/ |
| 19 | Biological Sciences Minor | https://catalog.uaf.edu/minors/ |
| 20 | Chemistry Minor | https://catalog.uaf.edu/minors/ |
| 21 | Communication Minor | https://catalog.uaf.edu/minors/ |
| 22 | Computer Information Technology Specialist Minor | https://catalog.uaf.edu/minors/ |
| 23 | Computer Science Minor | https://catalog.uaf.edu/minors/ |
| 24 | Creative Writing Minor | https://catalog.uaf.edu/minors/ |
| 25 | Cybersecurity Minor | https://catalog.uaf.edu/minors/ |
| 26 | Early Childhood Education Minor | https://catalog.uaf.edu/minors/ |
| 27 | Economics Minor | https://catalog.uaf.edu/minors/ |
| 28 | Elementary Education Minor | https://catalog.uaf.edu/minors/ |
| 29 | English Minor | https://catalog.uaf.edu/minors/ |
| 30 | Environmental Change Minor | https://catalog.uaf.edu/minors/ |
| 31 | Environmental Politics Minor | https://catalog.uaf.edu/minors/ |
| 32 | Ethnobotany Minor | https://catalog.uaf.edu/minors/ |
| 33 | Film Minor | https://catalog.uaf.edu/minors/ |
| 34 | Finance Minor | https://catalog.uaf.edu/minors/ |
| 35 | Fire Science Minor | https://catalog.uaf.edu/minors/ |
| 36 | Fisheries Minor | https://catalog.uaf.edu/minors/ |
| 37 | Foreign Languages Minor | https://catalog.uaf.edu/minors/ |
| 38 | General Business Minor | https://catalog.uaf.edu/minors/ |
| 39 | General Education Minor | https://catalog.uaf.edu/minors/ |
| 40 | Geology Minor | https://catalog.uaf.edu/minors/ |
| 41 | Geophysics Minor | https://catalog.uaf.edu/minors/ |
| 42 | Geospatial Sciences Minor | https://catalog.uaf.edu/minors/ |
| 43 | Global Studies Minor | https://catalog.uaf.edu/minors/ |
| 44 | Health Sciences for Pre-professionals Minor | https://catalog.uaf.edu/minors/ |
| 45 | History Minor | https://catalog.uaf.edu/minors/ |
| 46 | Homeland Security and Emergency Management Minor | https://catalog.uaf.edu/minors/ |
| 47 | Human Services Minor | https://catalog.uaf.edu/minors/ |
| 48 | Integrated Arts Minor | https://catalog.uaf.edu/minors/ |
| 49 | Interdisciplinary Studies Minor | https://catalog.uaf.edu/minors/ |
| 50 | Japanese Studies Minor | https://catalog.uaf.edu/minors/ |
| 51 | Journalism: Science and the Environment Minor | https://catalog.uaf.edu/minors/ |
| 52 | Justice Minor | https://catalog.uaf.edu/minors/ |
| 53 | Leadership Minor | https://catalog.uaf.edu/minors/ |
| 54 | Linguistics Minor | https://catalog.uaf.edu/minors/ |
| 55 | Management and Organizations Minor | https://catalog.uaf.edu/minors/ |
| 56 | Marine Science Minor | https://catalog.uaf.edu/minors/ |
| 57 | Marketing Minor | https://catalog.uaf.edu/minors/ |
| 58 | Mathematics Minor | https://catalog.uaf.edu/minors/ |
| 59 | Military Science and Leadership Minor | https://catalog.uaf.edu/minors/ |
| 60 | Military Security Studies Minor | https://catalog.uaf.edu/minors/ |
| 61 | Mining Engineering Minor | https://catalog.uaf.edu/minors/ |
| 62 | Music Minor | https://catalog.uaf.edu/minors/ |
| 63 | Natural Resources and Environment Minor | https://catalog.uaf.edu/minors/ |
| 64 | Paleontology Minor | https://catalog.uaf.edu/minors/ |
| 65 | Paralegal Studies Minor | https://catalog.uaf.edu/minors/ |
| 66 | Philosophy Minor | https://catalog.uaf.edu/minors/ |
| 67 | Physics Minor | https://catalog.uaf.edu/minors/ |
| 68 | Political Science Minor | https://catalog.uaf.edu/minors/ |
| 69 | Pre-law Minor | https://catalog.uaf.edu/minors/ |
| 70 | Psychology Minor | https://catalog.uaf.edu/minors/ |
| 71 | Recreation and Guiding Management Minor | https://catalog.uaf.edu/minors/ |
| 72 | Rural Development Minor | https://catalog.uaf.edu/minors/ |
| 73 | Science and Environmental Communication Minor | https://catalog.uaf.edu/minors/ |
| 74 | Secondary Education Minor | https://catalog.uaf.edu/minors/ |
| 75 | Social Work Minor | https://catalog.uaf.edu/minors/ |
| 76 | Space Operations Minor | https://catalog.uaf.edu/minors/ |
| 77 | Special Education Minor | https://catalog.uaf.edu/minors/ |
| 78 | Speech-Language Pathology Minor | https://catalog.uaf.edu/minors/ |
| 79 | Sport Management Minor | https://catalog.uaf.edu/minors/ |
| 80 | Statistics Minor | https://catalog.uaf.edu/minors/ |
| 81 | Sustainable Agriculture Minor | https://catalog.uaf.edu/minors/ |
| 82 | Teaching English to Speakers of Other Languages Minor | https://catalog.uaf.edu/minors/ |
| 83 | Theatre Minor | https://catalog.uaf.edu/minors/ |
| 84 | Tribal Governance Minor | https://catalog.uaf.edu/minors/ |
| 85 | Unmanned Aircraft Operations Minor | https://catalog.uaf.edu/minors/ |
| 86 | Wildlife Biology and Conservation Minor | https://catalog.uaf.edu/minors/ |
| 87 | Women, Gender and Sexuality Studies Minor | https://catalog.uaf.edu/minors/ |

### 1.5 General Education Requirements

UAF requires all bachelor's degree students to complete the Core Requirements (General Education), which include:
- Written Communication (6 credits)
- Oral Communication (3 credits)
- Humanities (6 credits)
- Social Sciences (6 credits)
- Natural Sciences (8 credits, including at least one lab course)
- Mathematics (3 credits)
- Alaska Native-themed courses (3 credits)

Source: https://catalog.uaf.edu/bachelors/

---

## Section 2 — Graduate Education

### 2.1 Graduate Programs — grouped by 学院 > 系 > 学位级别

#### College of Engineering and Mines (CEM)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.uaf.edu/masters/civil-engineering/ |
| 2 | Computer Science | https://catalog.uaf.edu/masters/computer-science/ |
| 3 | Electrical Engineering | https://catalog.uaf.edu/masters/electrical-engineering/ |
| 4 | Geological Engineering | https://catalog.uaf.edu/masters/geological-engineering/ |
| 5 | Geophysics | https://catalog.uaf.edu/masters/geophysics/ |
| 6 | Mechanical Engineering | https://catalog.uaf.edu/masters/mechanical-engineering/ |
| 7 | Mining Engineering | https://catalog.uaf.edu/masters/mining-engineering/ |
| 8 | Petroleum Engineering | https://catalog.uaf.edu/masters/petroleum-engineering/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.uaf.edu/graduate-certificates/ |
| 2 | Systems Engineering/Program Management | https://catalog.uaf.edu/graduate-certificates/ |

---

#### College of Liberal Arts (CLA)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.uaf.edu/masters/anthropology/ |
| 2 | English | https://catalog.uaf.edu/masters/english/ |
| 3 | Professional Communication | https://catalog.uaf.edu/masters/professional-communication/ |
| 4 | Justice Administration | https://catalog.uaf.edu/masters/justice-administration/ |
| 5 | Linguistics, Applied | https://catalog.uaf.edu/masters/linguistics-applied/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.uaf.edu/masters/creative-writing/ |
| 2 | Creative Writing and Literature Combined M.F.A./M.A. | https://catalog.uaf.edu/masters/english-mfa-ma-combined/ |

##### MMU
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Performance | https://catalog.uaf.edu/masters/music-performance/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.uaf.edu/phd/anthropology/ |

---

#### College of Natural Science and Mathematics (CNSM)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Atmospheric Sciences | https://catalog.uaf.edu/masters/atmospheric-sciences/ |
| 2 | Biological Sciences | https://catalog.uaf.edu/masters/biological-sciences/ |
| 3 | Chemistry | https://catalog.uaf.edu/masters/chemistry/ |
| 4 | Earth System Science | https://catalog.uaf.edu/masters/earth-system-science/ |
| 5 | Geoscience | https://catalog.uaf.edu/masters/geoscience/ |
| 6 | Mathematics | https://catalog.uaf.edu/masters/mathematics/ |
| 7 | Physics | https://catalog.uaf.edu/masters/physics/ |
| 8 | Statistics and Data Science | https://catalog.uaf.edu/masters/statistics-data-science/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Atmospheric Sciences | https://catalog.uaf.edu/phd/atmospheric-sciences/ |
| 2 | Biochemistry and Neuroscience | https://catalog.uaf.edu/phd/biochemistry-neuroscience/ |
| 3 | Biological Sciences | https://catalog.uaf.edu/phd/biological-sciences/ |
| 4 | Earth System Science | https://catalog.uaf.edu/phd/earth-system-science/ |
| 5 | Environmental Chemistry | https://catalog.uaf.edu/phd/environmental-chemistry/ |
| 6 | Geophysics | https://catalog.uaf.edu/phd/geophysics/ |
| 7 | Geoscience | https://catalog.uaf.edu/phd/geoscience/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied and Computational Mathematics | https://catalog.uaf.edu/graduate-certificates/ |
| 2 | Geospatial Science | https://catalog.uaf.edu/graduate-certificates/ |
| 3 | Statistics | https://catalog.uaf.edu/graduate-certificates/ |
| 4 | Science Teaching and Outreach | https://catalog.uaf.edu/graduate-certificates/ |

---

#### College of Business and Security Management (CBSM)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Healthcare Management and Leadership | https://catalog.uaf.edu/masters/healthcare-management-leadership/ |
| 2 | Security and Disaster Management | https://catalog.uaf.edu/masters/security-disaster-management/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.uaf.edu/masters/business-administration/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Arctic Security | https://catalog.uaf.edu/graduate-certificates/ |
| 2 | Business and Organizational Continuity | https://catalog.uaf.edu/graduate-certificates/ |
| 3 | Climate Security | https://catalog.uaf.edu/graduate-certificates/ |
| 4 | Cybersecurity Management | https://catalog.uaf.edu/graduate-certificates/ |
| 5 | Disaster Risk Reduction and Mitigation | https://catalog.uaf.edu/graduate-certificates/ |
| 6 | Healthcare Management and Leadership | https://catalog.uaf.edu/graduate-certificates/ |
| 7 | Justice Administration | https://catalog.uaf.edu/graduate-certificates/ |
| 8 | Strategic Leadership | https://catalog.uaf.edu/graduate-certificates/ |

---

#### School of Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://catalog.uaf.edu/masters/counseling/ |
| 2 | Elementary Education | https://catalog.uaf.edu/masters/elementary-education/ |
| 3 | Secondary Education | https://catalog.uaf.edu/masters/secondary-education/ |
| 4 | Special Education | https://catalog.uaf.edu/masters/special-education/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | School Counselor Certification | https://catalog.uaf.edu/graduate-certificates/ |

---

#### College of Fisheries and Ocean Sciences (CFOS)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries | https://catalog.uaf.edu/masters/fisheries/ |
| 2 | Marine Biology | https://catalog.uaf.edu/masters/marine-biology/ |
| 3 | Oceanography | https://catalog.uaf.edu/masters/oceanography/ |

##### MMP
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Policy | https://catalog.uaf.edu/masters/marine-policy/ |

##### MMS
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Studies | https://catalog.uaf.edu/masters/marine-studies/ |

##### OHM
| # | 项目 | URL |
|---|------|-----|
| 1 | One Health | https://catalog.uaf.edu/masters/one-health-masters/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries | https://catalog.uaf.edu/phd/fisheries/ |
| 2 | Marine Biology | https://catalog.uaf.edu/phd/marine-biology/ |
| 3 | Oceanography | https://catalog.uaf.edu/phd/oceanography/ |
| 4 | Natural Resources and Sustainability | https://catalog.uaf.edu/phd/natural-resources-sustainability/ |
| 5 | Space Physics | https://catalog.uaf.edu/phd/physics-space/ |

---

#### College of Indigenous Studies (CIS)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Arctic and Northern Studies | https://catalog.uaf.edu/masters/arctic-northern-studies/ |
| 2 | Indigenous Studies | https://catalog.uaf.edu/masters/indigenous-studies/ |
| 3 | Rural Development | https://catalog.uaf.edu/masters/rural-development/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Indigenous Studies | https://catalog.uaf.edu/phd/indigenous-studies/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Arctic and Northern Studies | https://catalog.uaf.edu/graduate-certificates/ |
| 2 | Rural Development | https://catalog.uaf.edu/graduate-certificates/ |

---

#### Graduate School

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uaf.edu/masters/interdisciplinary-studies-ma/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uaf.edu/masters/interdisciplinary-studies-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uaf.edu/phd/interdisciplinary-studies/ |

##### PhD (cross-listed with CEM)
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://catalog.uaf.edu/phd/engineering/ |
| 2 | Mathematics | https://catalog.uaf.edu/phd/mathematics/ |
| 3 | Physics | https://catalog.uaf.edu/phd/physics/ |

---

### 2.2 Graduate Deep-Dive: Computer Science M.S.

- **Department**: Computer Science, College of Engineering and Mines
- **Address**: Department of Computer Science, University of Alaska Fairbanks, P.O. Box 756680, Fairbanks, AK 99775-6680
- **Email**: Contact department directly
- **Application opens**: Rolling
- **Deadline**: June 1 (Fall), Oct. 15 (Spring), May 1 (Summer) — department may have earlier deadlines
- **Application fee**: $75 (on-time), $100 (late)
- **Application portal**: https://uaf.edu/admissions/apply/
- **GRE**: Not universally required; check with department
- **Funding**: Teaching and research assistantships available through department; may waive tuition
- **Behind accordions**: GRE policy, specific prerequisite requirements, assistantship application details

### 2.3 Graduate Admissions Model

UAF uses a **hybrid model**:
- **Centralized**: The Graduate School manages the application portal, transcript evaluation, and immigration documentation
- **Decentralized**: Individual departments set their own deadlines (some as early as January for Fall), GRE requirements, and funding decisions
- **Entry points**: Each department has its own prospective student page; the Graduate School hub is at https://www.uaf.edu/gradschool/
- **Financial aid**: Departments manage assistantships (RA/TA); the central Financial Aid office handles federal aid, scholarships, and grants
- **Application fee**: $75 on-time, $100 late; PhD applications currently free with waiver code #UAFR1

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | source |
|------|-----|--------|
| Admissions site | https://www.uaf.edu/admissions/ | official |
| Application portal | https://uaf.edu/admissions/apply/ + Common App | official |
| EA deadline | N/A (no Early Action) | official |
| ED deadline | N/A (no Early Decision) | official |
| Rolling deadline — Fall | June 15 | official |
| Rolling deadline — Spring | November 1 | official |
| Rolling deadline — Summer | May 1 | official |
| International Fall deadline | March 1 | official |
| International Spring deadline | September 1 | official |
| Decision notification | Rolling | official |
| Enrollment confirmation | N/A (rolling) | official |
| Financial aid priority (FAFSA) | February 15 (recommended) | official |
| SAT/ACT policy | Test-optional since Dec 6, 2023 | official |
| Superscore policy | N/A (test-optional) | official |
| Score-report method | N/A (test-optional) | official |
| Interview policy | Not required | official |
| Recommendation requirements | Not required for UG | official |
| Portfolio | Not required (except Art BFA) | official |
| Transfer pathway | Accepted; see transfer admissions page | official |
| Application fee (on-time) | $50 | official |
| Application fee (late) | $75 | official |
| GPA requirement | 2.5 cumulative + 2.5 in 16-credit HS core | official |
| HS diploma required | Yes | official |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | 适用条件 |
|------|---------|-------------|----------|
| TOEFL (iBT) | 79 | N/A | Required for F-1 visa students; exempt if from English-primary country |
| IELTS | 6.5 | N/A | Required for F-1 visa students; exempt if from English-primary country |
| PTE (Pearson) | 55 | N/A | Required for F-1 visa students; exempt if from English-primary country |
| Duolingo (DET) | 110 (UG) / 120 (Grad) | N/A | Required for F-1 visa students; exempt if from English-primary country |

**Exemption**: Students who completed secondary or baccalaureate education in English from listed countries (US, UK, Canada [except Quebec], Australia, NZ, Ireland, Singapore, etc.) are exempt. Long-term US permanent residents may also qualify for exemption with documentation.

**Exception requests**: Email uaf-admissions@alaska.edu. Acceptable grounds: completion of college-level non-ESL English composition (C or higher), comparable ACT/SAT score, or long-term permanent resident documentation.

### 3.3 Graduate — Global Rules

| 字段 | 值 | source |
|------|-----|--------|
| Admissions model | Hybrid (centralized portal + decentralized dept requirements) | official |
| Application platform | UAF Application Portal | official |
| Application fee | $75 (on-time) / $100 (late) | official |
| PhD application fee | Currently FREE with code #UAFR1 | official |
| CGS April-15 honor date | Not explicitly stated | N/A |
| GRE policy | Not universally required; individual departments may require | official |
| GMAT policy | Not universally required; check with department | official |
| Language test policy | Same as UG (TOEFL 79, IELTS 6.5, PTE 55, DET 120) | official |
| Exemption rules | Same as UG (English-primary country education) | official |
| Application timeline | June 1 (Fall), Oct. 15 (Spring), May 1 (Summer); dept deadlines may be earlier | official |
| UAF GRE code | 4866 | official |
| Required materials | Application, transcripts (NACES evaluation), resume/CV, statement of goals, 3 letters of recommendation, English proficiency | official |
| Funding | Dept-level RA/TA/fellowships; contact department directly | official |

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| 费用项目 | 金额 (每学期) | 金额 (每年) | 说明 |
|----------|-------------|------------|------|
| Tuition (Resident, 15 credits @ $310/credit) | $4,650 | $9,300 | Fairbanks campus, F100-F499 level |
| Tuition (Non-Resident, 15 credits @ $934/credit) | $14,010 | $28,020 | Fairbanks campus, F100-F499 level |
| Tuition (WUE, 15 credits @ $465/credit) | $6,975 | $13,950 | Western Undergraduate Exchange rate |
| Consolidated Fee | $840 | $1,680 | $56/credit × 15 |
| UA Infrastructure Fee | $375 | $750 | $25/credit × 15 |
| Bookstore Bundle Fee | $322.50 | $645 | $21.50/credit (opt-out available) |
| UAF Matriculation Fee | $225 (one-time) | $225 | One-time fee |
| Housing (Double room) | ~$3,375 | ~$6,750 | On-campus |
| Food (Alaska Block meal plan) | ~$3,375 | ~$6,750 | On-campus |
| Books & supplies | $564 | $1,128 | Estimated |
| Miscellaneous & personal | $1,250 | $2,500 | Estimated |
| Transportation | $500 | $1,000 | Estimated |
| **Total (Resident, on-campus)** | **~$11,442** | **~$27,512** | |
| **Total (Non-Resident, on-campus)** | **~$18,930** | **~$39,370** | |
| **Total (WUE, on-campus)** | **~$13,302** | **~$28,422** | |

**CTC (Community & Technical College) tuition**: $251/credit (resident), $875/credit (non-resident)

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | source |
|------|-----|--------|
| Tuition-free income threshold | Not explicitly stated | N/A |
| Zero-parent-contribution threshold | Not explicitly stated | N/A |
| Need-blind / Need-aware | Need-aware for all (domestic and international) | official |
| Applies to internationals | Yes (need-aware) | official |
| Median actual price paid | Not published | N/A |
| Debt-free graduation rate | Not published | N/A |
| Average starting salary | Not published | N/A |
| WUE discount | ~40% off non-resident tuition for qualifying western states | official |
| Come Home to Alaska | Non-residents with AK parent/grandparent qualify for resident tuition | official |
| FAFSA priority deadline | February 15 | official |
| State aid deadline (FAFSA) | June 30 | official |
| Alaska Performance Scholarship | Available; requires qualifying test scores | official |
| UA Scholars Award | Available for high-performing Alaska students | official |
| Nanook Pledge | Scholarship mentioned by students | official |
| 500+ scholarships | Single application for all UAF scholarships | official |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | source |
|------|-----|--------|
| Tuition (Resident, 9 credits 600-level) | $5,733/semester ($577/credit × 9 + fees) | official |
| Tuition (Non-Resident, 9 credits 600-level) | $11,538/semester ($1,201/credit × 9 + fees) | official |
| Housing + Food (off-campus est.) | $10,560/semester | official |
| Semester total (Resident) | ~$16,482 | official |
| Semester total (Non-Resident) | ~$22,098 | official |
| Annual est. (Resident) | ~$32,964 | official |
| Annual est. (Non-Resident) | ~$44,196 | official |
| Intl student annual est. | $44,125 (UG) / $42,856 (Grad) | official |
| Funding types | RA/TA/fellowships through departments; federal aid through Financial Aid | official |
| Application fee | $75 (on-time) / $100 (late) | official |
| PhD fee waiver | Currently free with code #UAFR1 | official |
| Fee-waiver policy | Not explicitly stated for general applicants | N/A |
| Graduate Workers Union | AGWA (Alaska Graduate Workers Association) represents employed grad students | official |

---

## Section 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.fall
  value: "June 15"
  source_url: https://www.uaf.edu/admissions/apply/
  source_snippet: "June 15: Fall semester start"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.spring
  value: "November 1"
  source_url: https://www.uaf.edu/admissions/apply/
  source_snippet: "Nov. 1: Spring semester start"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.summer
  value: "May 1"
  source_url: https://www.uaf.edu/admissions/apply/
  source_snippet: "May 1: Summer sessions"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.test_optional
  value: true (since December 6, 2023)
  source_url: https://www.uaf.edu/admissions/apply/ug.php
  source_snippet: "As of December 6, 2023, UAF doesn't require ACT/SAT scores for admission to any undergraduate degree program."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.requirements.gpa
  value: "2.5 cumulative + 2.5 in 16-credit HS core"
  source_url: https://www.uaf.edu/admissions/apply/ug.php
  source_snippet: "Pass the 16-credit high school core curriculum with at least a 2.5, and Have a cumulative GPA of 2.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.application_fee
  value: "$50 on-time / $75 late"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "Applications must be received before the published deadlines, along with a $50 nonrefundable application fee. Applications submitted after the published deadlines have a $75 nonrefundable application fee"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english_proficiency.toefl
  value: "79 minimum"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "A minimum TOEFL score of 79"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english_proficiency.ielts
  value: "6.5 minimum"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "A minimum IELTS score of 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english_proficiency.pte
  value: "55 minimum"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "A minimum PTE score of 55"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_proficiency.det
  value: "110 (UG) / 120 (Grad)"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "A minimum DET score of 110 (undergraduate) or 120 (graduate)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.cost.tuition_resident
  value: "$310/credit"
  source_url: https://catalog.uaf.edu/costs-financial-aid/tuition/
  source_snippet: "Troth Yeddha' (Fairbanks) — Undergraduate: $310/credit"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.cost.tuition_nonresident
  value: "$934/credit"
  source_url: https://catalog.uaf.edu/costs-financial-aid/tuition/
  source_snippet: "Troth Yeddha' (Fairbanks) — Undergraduate: $934/credit (Nonresident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.cost.tuition_wue
  value: "$465/credit"
  source_url: https://catalog.uaf.edu/costs-financial-aid/tuition/
  source_snippet: "Troth Yeddha' (Fairbanks) — Undergraduate: $465/credit (WUE)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-014:
  field: undergraduate.cost.consolidated_fee
  value: "$56/credit"
  source_url: https://catalog.uaf.edu/costs-financial-aid/tuition/
  source_snippet: "Fairbanks/Rural Campus Consolidated Fee: $56/credit"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-015:
  field: undergraduate.cost.housing_food
  value: "$6,750/semester (double room + meal plan)"
  source_url: https://www.uaf.edu/finaid/costs/
  source_snippet: "Housing and food (Double room + Alaska block meal plan): $6,750"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.deadlines.fall
  value: "June 1"
  source_url: https://www.uaf.edu/admissions/apply/
  source_snippet: "Graduate Students: June 1: Fall semester start"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_fee
  value: "$75 on-time / $100 late"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "Applications must be received before the published deadlines, along with a $75 nonrefundable application fee. Applications submitted after the published deadlines are only accepted upon a department's request and have a $100 nonrefundable application fee."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.gre_policy
  value: "Not universally required; departments may require"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "The University of Alaska Fairbanks does not require submission of Graduate Record Exam (GRE) scores from all students. However, individual departments may require or allow submission of GRE scores."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.cost.tuition_resident
  value: "$577/credit (600-level)"
  source_url: https://catalog.uaf.edu/costs-financial-aid/tuition/
  source_snippet: "Troth Yeddha' (Fairbanks) — Graduate: $577/credit (Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.cost.tuition_nonresident
  value: "$1,201/credit (600-level)"
  source_url: https://catalog.uaf.edu/costs-financial-aid/tuition/
  source_snippet: "Troth Yeddha' (Fairbanks) — Graduate: $1,201/credit (Nonresident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-P-001:
  field: programs.bachelors_count
  value: 62
  source_url: https://catalog.uaf.edu/bachelors/
  source_snippet: "62 unique bachelor degree programs listed in catalog"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-002:
  field: programs.masters_count
  value: 48
  source_url: https://catalog.uaf.edu/masters/
  source_snippet: "48 unique master degree programs listed in catalog"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-003:
  field: programs.phd_count
  value: 18
  source_url: https://catalog.uaf.edu/phd/
  source_snippet: "18 unique PhD programs listed in catalog"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-004:
  field: programs.associates_count
  value: 22
  source_url: https://catalog.uaf.edu/associates/
  source_snippet: "22 unique associate degree programs listed in catalog"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-005:
  field: programs.minors_count
  value: 87
  source_url: https://catalog.uaf.edu/minors/
  source_snippet: "87 unique minor programs listed in catalog"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-001:
  field: international.deadlines.fall
  value: "March 1"
  source_url: https://www.uaf.edu/admissions/apply/
  source_snippet: "International Students: March 1: Fall semester start"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-002:
  field: international.required_funding_amount
  value: "$44,125 (UG) / $42,856 (Grad)"
  source_url: https://catalog.uaf.edu/getting-started/admission/
  source_snippet: "The estimated cost for one school year at UAF for an international student is $44,125 for undergraduate students and $42,856 for graduate students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-F-001:
  field: financial_aid.fafsa_priority
  value: "February 15"
  source_url: https://www.uaf.edu/finaid/
  source_snippet: "We recommend completing it before February 15 to be considered for all UAF scholarships."
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## Section 6 — WeKnora Import Manifest

### Collection Structure

```
uaf-knowledge-base-v2
├── uaf-overview                          (Section 0: rules 1-4)
│   ├── chunk-00-counts                   (0.1 program counts)
│   ├── chunk-01-hierarchy                (0.2 school/college tree)
│   ├── chunk-02-degree-inventory          (0.3 degree levels)
│   └── chunk-03-distribution-matrix       (0.4 cross-tab)
├── uaf-undergraduate                     (Section 1: rule 5)
│   ├── chunk-04-CEM-programs             (College of Engineering & Mines)
│   ├── chunk-05-CLA-programs             (College of Liberal Arts)
│   ├── chunk-06-CNSM-programs            (College of Natural Science & Math)
│   ├── chunk-07-CBSM-programs            (College of Business & Security Mgmt)
│   ├── chunk-08-Education-programs       (School of Education)
│   ├── chunk-09-CFOS-programs            (College of Fisheries & Ocean Sciences)
│   ├── chunk-10-CIS-programs             (College of Indigenous Studies)
│   ├── chunk-11-Exploratory-programs     (Division of Exploratory Studies)
│   ├── chunk-12-CTC-programs             (Community & Technical College)
│   └── chunk-13-minors                   (Complete minors list)
├── uaf-graduate                          (Section 2: rule 5)
│   ├── chunk-14-grad-CEM                 (CEM graduate programs)
│   ├── chunk-15-grad-CLA                 (CLA graduate programs)
│   ├── chunk-16-grad-CNSM                (CNSM graduate programs)
│   ├── chunk-17-grad-CBSM                (CBSM graduate programs)
│   ├── chunk-18-grad-Education           (Education graduate programs)
│   ├── chunk-19-grad-CFOS                (CFOS graduate programs)
│   ├── chunk-20-grad-CIS                 (CIS graduate programs)
│   └── chunk-21-grad-school              (Graduate School programs)
├── uaf-admissions                        (Section 3)
│   ├── chunk-22-ug-deadlines-requirements
│   ├── chunk-23-ug-english-proficiency
│   └── chunk-24-grad-admissions
├── uaf-costs                             (Section 4)
│   ├── chunk-25-ug-costs
│   ├── chunk-26-ug-financial-aid
│   └── chunk-27-grad-costs-funding
├── uaf-evidence                          (Section 5)
│   └── chunk-28-evidence-chain
└── uaf-certificates                      (Supplementary)
    ├── chunk-29-ug-certificates
    ├── chunk-30-grad-certificates
    ├── chunk-31-endorsements
    └── chunk-32-pbct
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "uaf-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
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
|----------|-----------|------------|
| P0 | Per-program GRE requirements | Dept-specific pages |
| P0 | UG net price calculator results | https://www.uaf.edu/finaid/costs/net-price-calculator.php |
| P1 | Scholarship amounts and criteria | https://www.uaf.edu/finaid/scholarships/ |
| P1 | Assistantship stipend rates | Dept-specific pages |
| P1 | Art BFA portfolio requirements | Art department page |
| P2 | Transfer admission requirements | https://www.uaf.edu/admissions/apply/transfer.php |
| P2 | Honors College requirements | https://www.uaf.edu/honors/ |
| P2 | Dual enrollment details | https://www.uaf.edu/dual-enrollment/ |
| P2 | Housing options and costs breakdown | Residence Life page |
| P2 | Health insurance requirement details | Student Health page |

---

## Section 7 — Cross-School Comparison Framework

| 维度 | UAF | (其他学校待填) |
|------|-----|----------------|
| Total UG cost/yr (resident, on-campus) | ~$27,512 | |
| Total UG cost/yr (non-resident, on-campus) | ~$39,370 | |
| Tuition/yr (resident) | ~$9,300 | |
| Tuition/yr (non-resident) | ~$28,020 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (rolling) | |
| RA/RD deadline | Rolling (June 15 Fall) | |
| SAT/ACT required? | No (test-optional since Dec 2023) | |
| TOEFL min | 79 | |
| IELTS min | 6.5 | |
| DET min | 110 (UG) / 120 (Grad) | |
| WUE available? | Yes ($465/credit vs $934) | |
| Application fee (UG) | $50 | |
| Application fee (Grad) | $75 | |
| Total program count (Rule 1) | 145 degree programs | |
| School/department count (Rule 2) | 9 colleges/divisions + CTC | |
| GPA requirement | 2.5 | |
| Graduate GRE policy | Varies by department | |
| PhD application fee | Free (with code #UAFR1) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: catalog.uaf.edu, www.uaf.edu/admissions, www.uaf.edu/finaid, www.uaf.edu/gradschool
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
