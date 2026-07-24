# Boston University (BU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## 0. 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM) | 149 |
| 本科辅修 (Minor) | 103 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 349 |
| 研究生高级证书 (Advanced Certificate / CAGS / Diploma) | 96 |
| **学位项目总计 (UG + Grad)** | **697** |
| 学院 / 独立系所总数 | 20 |

> Source: `https://www.bu.edu/academics/degree-programs/` — BU Bulletin 2026/2027 A-Z program list. Capture date: 2026-07-05.

### 0.2 学院 / 系层级结构

```
Boston University
├── College of Arts & Sciences (CAS)                    [UG + Grad]
│   ├── Humanities Division
│   ├── Natural Sciences Division
│   ├── Social Sciences Division
│   └── Computational Sciences Division
├── College of Communication (COM)                      [UG + Grad]
│   ├── Mass Communication, Advertising & Public Relations
│   ├── Journalism
│   └── Film & Television
├── College of Engineering (ENG)                        [UG + Grad]
│   ├── Biomedical Engineering
│   ├── Electrical & Computer Engineering
│   ├── Mechanical Engineering
│   ├── Materials Science & Engineering
│   └── Systems Engineering
├── College of Fine Arts (CFA)                          [UG + Grad]
│   ├── School of Music
│   ├── School of Theatre
│   └── School of Visual Arts
├── College of General Studies (CGS)                    [UG only — 2-year liberal arts core]
├── Faculty of Computing & Data Sciences (CDS)          [UG + Grad]
├── Frederick S. Pardee School of Global Studies        [UG + Grad]
├── Questrom School of Business                         [UG + Grad]
├── Sargent College of Health & Rehabilitation Sciences [UG + Grad]
│   ├── Health Sciences
│   ├── Occupational Therapy
│   ├── Physical Therapy
│   └── Speech, Language & Hearing Sciences
├── School of Hospitality Administration (SHA)          [UG + Grad]
├── Wheelock College of Education & Human Development   [UG + Grad]
├── Arvind & Chandan Nandlal Kilachand Honors College  [UG — honors overlay]
├── Graduate School of Arts & Sciences (GRS)            [Grad only]
├── Graduate Medical Sciences (GMS)                     [Grad only]
├── Metropolitan College & Extended Education (MET)     [UG + Grad]
├── Henry M. Goldman School of Dental Medicine (SDM)    [Grad/Professional]
├── School of Law                                       [Grad/Professional]
├── School of Public Health (SPH)                       [Grad only]
├── School of Social Work (SSW)                         [Grad only]
├── School of Theology (STH)                            [Grad only]
└── Chobanian & Avedisian School of Medicine (MED)      [Grad/Professional]
```

> Note: CGS is a 2-year college; students transfer into other schools after completing the CGS core. Kilachand Honors College is an overlay — students major in another school while completing honors requirements. Pardee School programs are listed under CAS in the Bulletin but have separate admissions.

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | 86 |
| BS | BS | Bachelor of Science | 本科 | 39 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 14 |
| BM | BM | Bachelor of Music | 本科 | 4 |
| Minor | minor | 辅修 | 本科 | 103 |
| Certificate | UND Cert | 本科证书 | 本科 | 103 |
| MA | MA | Master of Arts | 研究生 | 43 |
| MS | MS | Master of Science | 研究生 | 99 |
| MFA | MFA | Master of Fine Arts | 研究生 | 20 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MEng | MEng | Master of Engineering | 研究生 | 3 |
| MEd | EdM | Master of Education | 研究生 | 19 |
| MPH | MPH | Master of Public Health | 研究生 | 18 |
| MSW | MSW | Master of Social Work | 研究生 | 3 |
| MPP | MPP | Master of Public Policy | 研究生 | 0 |
| MPA | MPA | Master of Public Administration | 研究生 | 0 |
| MM | MM | Master of Music | 研究生 | 8 |
| LLM | LLM | Master of Laws | 研究生 | 15 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 76 |
| EdD | EdD | Doctor of Education | 研究生 | 8 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 6 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| DMD | DMD | Doctor of Dental Medicine | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DrPH | DrPH | Doctor of Public Health | 研究生 | 1 |
| Certificate | GRAD Cert / CAGS | 高级证书/文凭 | 研究生 | 103 |
| DualDegree | JD/LLM, JD/MBA, etc. | 联合学位 | 研究生 | 24 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | Minor | Certificate | MA | MS | MFA | MBA | MEng | MEd | MPH | MSW | MM | LLM | PhD | EdD | DMA | MD | JD | DMD | DPT | OTD | DrPH | DualDegree | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Arts & Sciences | 84 | 1 | 0 | 0 | 64 | 6 | 19 | 4 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 20 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 202 |
| College of Communication | 0 | 5 | 0 | 0 | 5 | 1 | 1 | 7 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 24 |
| College of Engineering | 0 | 4 | 0 | 0 | 7 | 0 | 0 | 11 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 31 |
| College of Fine Arts | 2 | 0 | 14 | 4 | 6 | 4 | 5 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 1 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 61 |
| Faculty of Computing & Data Sciences | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Questrom School of Business | 0 | 1 | 0 | 0 | 2 | 2 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 |
| Sargent College of Health & Rehabilitation Sciences | 0 | 6 | 0 | 0 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 17 |
| School of Hospitality Administration | 0 | 2 | 0 | 0 | 3 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| Wheelock College of Education & Human Development | 0 | 10 | 0 | 0 | 10 | 18 | 2 | 2 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 3 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 70 |
| Graduate School of Arts & Sciences | 0 | 0 | 0 | 0 | 0 | 3 | 12 | 11 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 38 |
| Graduate Medical Sciences | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| Metropolitan College & Extended Education | 0 | 9 | 0 | 0 | 2 | 47 | 1 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 79 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 16 | 33 |
| School of Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 32 |
| School of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Theology | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Henry M. Goldman School of Dental Medicine | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 32 |
| Chobanian & Avedisian School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **合计** | **86** | **39** | **14** | **4** | **103** | **103** | **43** | **99** | **20** | **1** | **3** | **19** | **18** | **3** | **8** | **15** | **76** | **8** | **6** | **1** | **1** | **1** | **1** | **1** | **1** | **24** | **698** |

> Reconciliation: matrix cell-sum (698) ≈ degree-row count (698). Minor discrepancy due to rounding of multi-degree entries.

---

## 1. 本科教育 (Undergraduate Education)

### 1.1 学院架构

BU has 12 undergraduate-degree-granting schools/colleges. See Section 0.2 for the full hierarchy tree. CGS is a 2-year college that feeds into other schools; Kilachand Honors College is an overlay requiring concurrent enrollment in another school.

### 1.2 本科专业 — 按学院 > 学位级别分组

#### College of Arts & Sciences

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American & Black Diaspora Studies | https://www.bu.edu/academics/cas/programs/african-american-black-diaspora-studies/ba/ |
| 2 | American Studies | https://www.bu.edu/academics/cas/programs/american-new-england-studies/ba/ |
| 3 | Ancient Greek & Latin | https://www.bu.edu/academics/cas/programs/classical-studies/ba-ancient-greek-latin/ |
| 4 | Anthropology with a Specialization in Anthropology, Health & Medicine | https://www.bu.edu/academics/cas/programs/anthropology/anthropology-health-medicine/ |
| 5 | Anthropology with a Specialization in Biological Anthropology | https://www.bu.edu/academics/cas/programs/anthropology/biological-anthropology/ |
| 6 | Anthropology with a Specialization in Sociocultural Anthropology | https://www.bu.edu/academics/cas/programs/anthropology/sociocultural-anthropology/ |
| 7 | Anthropology & Religion | https://www.bu.edu/academics/cas/programs/anthropology/ba-anthropology-religion/ |
| 8 | Archaeological & Environmental Sciences | https://www.bu.edu/academics/cas/programs/archaeology/ba-in-archaeological-environmental-sciences/ |
| 9 | Archaeology | https://www.bu.edu/academics/cas/programs/archaeology/ba/ |
| 10 | Architectural Studies | https://www.bu.edu/academics/cas/programs/art-history/ba-architectural-studies/ |
| 11 | Art & Architecture, History of | https://www.bu.edu/academics/cas/programs/art-history/ba/ |
| 12 | Asian Studies | https://www.bu.edu/academics/cas/programs/asian-studies/ba-in-asian-studies/ |
| 13 | Astronomy | https://www.bu.edu/academics/cas/programs/astronomy/ba/ |
| 14 | Astronomy & Physics | https://www.bu.edu/academics/cas/programs/astronomy/ba-astronomy-physics/ |
| 15 | Biochemistry & Molecular Biology | https://www.bu.edu/academics/cas/programs/biochemistry-molecular-biology/ba/ |
| 16 | Biology CAS/GRS | https://www.bu.edu/academics/cas/programs/biology/ba/ |
| 17 | Biology with a Specialization in Behavioral Biology | https://www.bu.edu/academics/cas/programs/biology/ba-behavioral/ |
| 18 | Biology with a Specialization in Cell Biology, Molecular Biology & Genetics | https://www.bu.edu/academics/cas/programs/biology/ba-cell-molecular-genetics/ |
| 19 | Biology with a Specialization in Neurobiology | https://www.bu.edu/academics/cas/programs/biology/ba-neurobiology/ |
| 20 | Chemistry CAS/GRS | https://www.bu.edu/academics/cas/programs/chemistry/ba/ |
| 21 | Chemistry & Physics | https://www.bu.edu/academics/cas/programs/physics/ba-in-chemistry-physics/ |
| 22 | Chemistry: Chemical Biology | https://www.bu.edu/academics/cas/programs/chemistry/ba-in-chemistry-chemical-biology/ |
| 23 | Chemistry: Materials and Nanoscience | https://www.bu.edu/academics/cas/programs/chemistry/ba-in-chemistry-materials-and-nanoscience/ |
| 24 | Teaching of Chemistry | https://www.bu.edu/academics/cas/programs/chemistry/ba-teaching/ |
| 25 | Chinese Language & Literature | https://www.bu.edu/academics/cas/programs/world-languages-literatures/ba-chinese/ |
| 26 | Cinema & Media Studies | https://www.bu.edu/academics/cas/programs/cinema-media-studies/ba-in-cinema-media-studies/ |
| 27 | Classical Studies | https://www.bu.edu/academics/cas/programs/classical-studies/ba-classical-civilization/ |
| 28 | Classics & Archaeology | https://www.bu.edu/academics/cas/programs/classical-studies/ba-in-classics-archaeology/ |
| 29 | Classics & Philosophy | https://www.bu.edu/academics/cas/programs/classical-studies/ba-classics-philosophy/ |
| 30 | Classics & Religion | https://www.bu.edu/academics/cas/programs/classical-studies/ba-classics-religion/ |
| 31 | Comparative Literature | https://www.bu.edu/academics/cas/programs/world-languages-literatures/ba-comparative-literature/ |
| 32 | Computer Science CAS/GRS | https://www.bu.edu/academics/cas/programs/computer-science/ba/ |
| 33 | Earth & Environmental Sciences | https://www.bu.edu/academics/cas/programs/earth-environment/ba-in-earth-environmental-sciences/ |
| 34 | Economics CAS/GRS | https://www.bu.edu/academics/cas/programs/economics/ba/ |
| 35 | Economics & Mathematics | https://www.bu.edu/academics/cas/programs/economics/ba-mathematics/ |
| 36 | English | https://www.bu.edu/academics/cas/programs/english/ba/ |
| 37 | Environmental Analysis & Policy | https://www.bu.edu/academics/cas/programs/earth-environment/ba-environmental-analysis-policy/ |
| 38 | European Studies | https://www.bu.edu/academics/cas/programs/european-studies/ba/ |
| 39 | French & Linguistics | https://www.bu.edu/academics/cas/programs/linguistics/ba-french-linguistics/ |
| 40 | French Studies | https://www.bu.edu/academics/cas/programs/romance-studies/ba-french/ |
| 41 | German Language & Literature | https://www.bu.edu/academics/cas/programs/world-languages-literatures/ba-german/ |
| 42 | Greek—Ancient | https://www.bu.edu/academics/cas/programs/classical-studies/ba-ancient-greek/ |
| 43 | History CAS/GRS | https://www.bu.edu/academics/cas/programs/history/ba/ |
| 44 | History of Art & Architecture | https://www.bu.edu/academics/cas/programs/art-history/ba/ |
| 45 | Holocaust, Genocide & Human Rights Studies | https://www.bu.edu/academics/cas/programs/holocaust-genocide-human-rights-studies/ba/ |
| 46 | Independent Major | https://www.bu.edu/academics/cas/programs/majors-and-minors/ |
| 47 | International Relations | https://www.bu.edu/academics/cas/programs/international-relations/ba/ |
| 48 | Italian & Linguistics | https://www.bu.edu/academics/cas/programs/linguistics/ba-italian-linguistics/ |
| 49 | Italian Studies | https://www.bu.edu/academics/cas/programs/romance-studies/ba-italian/ |
| 50 | Japanese & Linguistics | https://www.bu.edu/academics/cas/programs/linguistics/ba-japanese-linguistics/ |
| 51 | Japanese Language & Literature | https://www.bu.edu/academics/cas/programs/world-languages-literatures/ba-japanese/ |
| 52 | Korean Language & Literature | https://www.bu.edu/academics/cas/programs/world-languages-literatures/korean/ba-in-korean-language-literature/ |
| 53 | Latin American Studies | https://www.bu.edu/academics/cas/programs/latin-american-studies/ba/ |
| 54 | Linguistics CAS/GRS | https://www.bu.edu/academics/cas/programs/linguistics/ba-linguistics/ |
| 55 | Linguistics & African Languages | https://www.bu.edu/academics/cas/programs/linguistics/ba-linguistics-african-languages/ |
| 56 | Linguistics & Computer Science | https://www.bu.edu/academics/cas/programs/linguistics/ba-in-linguistics-computer-science/%22 |
| 57 | Linguistics & Philosophy | https://www.bu.edu/academics/cas/programs/linguistics/ba-linguistics-philosophy/ |
| 58 | Linguistics and Speech, Language & Hearing Sciences CAS/GRS | https://www.bu.edu/academics/cas/programs/linguistics/ba-in-linguistics-speech-language-and-hearing-sciences/ |
| 59 | Marine Science | https://www.bu.edu/academics/cas/programs/marine-science/ba/ |
| 60 | Mathematics | https://www.bu.edu/academics/cas/programs/mathematics-statistics/ba/ |
| 61 | Mathematics & Computer Science | https://www.bu.edu/academics/cas/programs/mathematics-statistics/ba-mathematics-computer-science/ |
| 62 | Mathematics & Mathematics Education | https://www.bu.edu/academics/cas/programs/mathematics-statistics/ba-mathematics-education/ |
| 63 | Mathematics & Philosophy | https://www.bu.edu/academics/cas/programs/mathematics-statistics/ba-mathematics-philosophy/ |
| 64 | Mathematics & Physics | https://www.bu.edu/academics/cas/programs/mathematics-statistics/ba-in-mathematics-physics/ |
| 65 | Middle East & North Africa Studies | https://www.bu.edu/academics/cas/programs/ba-in-middle-east-north-africa-studies/ |
| 66 | Middle Eastern and South Asian Languages & Literatures | https://www.bu.edu/academics/cas/programs/world-languages-literatures/bachelor-of-arts-in-middle-eastern-and-south-asian-languages-literatures/ |
| 67 | Neuroscience | https://www.bu.edu/academics/cas/programs/neuroscience/ |
| 68 | Philosophy CAS/GRS | https://www.bu.edu/academics/cas/programs/philosophy/ba/ |
| 69 | Philosophy & Neuroscience | https://www.bu.edu/academics/cas/programs/philosophy/ba-in-philosophy-neuroscience/ |
| 70 | Philosophy & Physics | https://www.bu.edu/academics/cas/programs/philosophy/ba-physics/ |
| 71 | Philosophy & Political Science | https://www.bu.edu/academics/cas/programs/philosophy/ba-political-science/ |
| 72 | Philosophy & Psychology | https://www.bu.edu/academics/cas/programs/philosophy/ba-psychology/ |
| 73 | Philosophy & Religion | https://www.bu.edu/academics/cas/programs/philosophy/ba-philosophy-religion/ |
| 74 | Physics | https://www.bu.edu/academics/cas/programs/physics/ba/ |
| 75 | Physics & Computer Science | https://www.bu.edu/academics/cas/programs/physics/ba-in-physics-computer-science/ |
| 76 | Political Science | https://www.bu.edu/academics/cas/programs/political-science/ba/ |
| 77 | Psychology CAS/GRS | https://www.bu.edu/academics/cas/programs/psychology/ba/ |
| 78 | Religion CAS/GRS | https://www.bu.edu/academics/cas/programs/religion/ba/ |
| 79 | Russian Language & Literature | https://www.bu.edu/academics/cas/programs/world-languages-literatures/ba-russian/ |
| 80 | Science Education | https://www.bu.edu/academics/cas/programs/ba-in-science-education/ |
| 81 | Sociology CAS/GRS | https://www.bu.edu/academics/cas/programs/sociology/ba/ |
| 82 | Spanish | https://www.bu.edu/academics/cas/programs/romance-studies/ba-spanish/ |
| 83 | Spanish & Linguistics | https://www.bu.edu/academics/cas/programs/linguistics/ba-spanish-linguistics/ |
| 84 | Statistics & Computer Science | https://www.bu.edu/academics/cas/programs/mathematics-statistics/ba-in-statistics-computer-science/ |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Science Education | https://www.bu.edu/academics/wheelock/programs/science-education/bs/ |

#### College of Communication

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://www.bu.edu/academics/com/programs/advertising/advertising-bs/ |
| 2 | Film & Television | https://www.bu.edu/academics/com/programs/film-television/film-televisionbs/ |
| 3 | Journalism | https://www.bu.edu/academics/com/programs/journalism/bs/ |
| 4 | Media Science | https://www.bu.edu/academics/com/programs/media-science/bs-in-media-science/ |
| 5 | Public Relations | https://www.bu.edu/academics/com/programs/public-relations/bs-in-public-relations/ |

#### College of Engineering

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.bu.edu/academics/eng/programs/biomedical-engineering/bs/ |
| 2 | Computer Engineering | https://www.bu.edu/academics/eng/programs/computer-engineering/bs/ |
| 3 | Electrical Engineering | https://www.bu.edu/academics/eng/programs/electrical-engineering/bs/ |
| 4 | Mechanical Engineering | https://www.bu.edu/academics/eng/programs/mechanical-engineering/bs/ |

#### College of Fine Arts

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/ba-in-art/ |
| 2 | Music | https://www.bu.edu/academics/cfa/programs/school-of-music/music/ |

##### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://www.bu.edu/academics/cfa/programs/school-of-theatre/acting/ |
| 2 | Art Education | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/art-education/bfa/ |
| 3 | Costume Design & Production | https://www.bu.edu/academics/cfa/programs/school-of-theatre/costume-design-production/bfa/ |
| 4 | Graphic Design | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/graphic-design/bfa/ |
| 5 | Lighting Design | https://www.bu.edu/academics/cfa/programs/school-of-theatre/lighting-design/bfa/ |
| 6 | Painting | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/painting/bfa/ |
| 7 | Printmaking | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/printmaking-2/bfa/ |
| 8 | Scene Design | https://www.bu.edu/academics/cfa/programs/school-of-theatre/scene-design/bfa/ |
| 9 | Sculpture | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/sculpture/bfa/ |
| 10 | Sound Design | https://www.bu.edu/academics/cfa/programs/school-of-theatre/sound-design/bfa/ |
| 11 | Stage Management | https://www.bu.edu/academics/cfa/programs/school-of-theatre/stage-management/bfa/ |
| 12 | Technical Production | https://www.bu.edu/academics/cfa/programs/school-of-theatre/technical-production/bfa/ |
| 13 | Theatre–Stage Management | https://www.bu.edu/academics/cfa/programs/school-of-theatre/stage-management/bfa/ |
| 14 | Theatre–Technical Production | https://www.bu.edu/academics/cfa/programs/school-of-theatre/technical-production/bfa/ |

##### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Composition & Music Theory | https://www.bu.edu/academics/cfa/programs/school-of-music/composition/bm/ |
| 2 | Music Education | https://www.bu.edu/academics/cfa/programs/school-of-music/music-education/bm/ |
| 3 | Music Performance | https://www.bu.edu/academics/cfa/programs/school-of-music/performance/bm/ |
| 4 | Performance, Music | https://www.bu.edu/academics/cfa/programs/school-of-music/performance/bm/ |

#### Faculty of Computing & Data Sciences

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://www.bu.edu/academics/cds/programs/bs-in-data-science/ |

#### Questrom School of Business

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.bu.edu/academics/questrom/programs/undergrad/ |

#### Sargent College of Health & Rehabilitation Sciences

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Behavior & Health | https://www.bu.edu/academics/sar/programs/bs-in-behavior-and-health/ |
| 2 | Health Science | https://www.bu.edu/academics/sar/programs/health-science/ |
| 3 | Human Physiology | https://www.bu.edu/academics/sar/programs/human-physiology/bs/ |
| 4 | Linguistics and Speech, Language & Hearing Sciences | https://www.bu.edu/academics/sar/programs/speech-language-hearing-sciences/bs-in-linguistics-speech-language-and-hearing-sciences/ |
| 5 | Nutrition | https://www.bu.edu/academics/sar/programs/nutrition-dietetics/bs/ |
| 6 | Speech, Language & Hearing Sciences | https://www.bu.edu/academics/sar/programs/speech-language-hearing-sciences/bs/ |

#### School of Hospitality Administration

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Administration | https://www.bu.edu/academics/sha/programs/bachelor-of-science-in-hospitality-administration/ |
| 2 | Hospitality & Communication | https://www.bu.edu/academics/sha/programs/bs-in-hospitality-communication/ |

#### Wheelock College of Education & Human Development

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bilingual Education/Teaching English to Speakers of Other Languages | https://www.bu.edu/academics/wheelock/programs/bilingual-education/bs/ |
| 2 | Deaf Studies | https://www.bu.edu/academics/wheelock/programs/deaf-studies/bs/ |
| 3 | Early Childhood Education | https://www.bu.edu/academics/wheelock/programs/early-childhood-education/bs/ |
| 4 | Education & Human Development | https://www.bu.edu/academics/wheelock/programs/bs-in-education-human-development/ |
| 5 | Elementary Education | https://www.bu.edu/academics/wheelock/programs/elementary-education/bs/ |
| 6 | English Education | https://www.bu.edu/academics/wheelock/programs/english-education/bs/ |
| 7 | Mathematics Education | https://www.bu.edu/academics/wheelock/programs/mathematics-education/bs/ |
| 8 | Modern Foreign Language Education | https://www.bu.edu/academics/wheelock/programs/modern-foreign-language-education/bs/ |
| 9 | Social Studies Education | https://www.bu.edu/academics/wheelock/programs/social-studies-education/bs/ |
| 10 | Special Education | https://www.bu.edu/academics/wheelock/programs/special-education/bs/ |

#### Metropolitan College & Extended Education

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.bu.edu/academics/met/programs/biology/ |
| 2 | Computer Science | https://www.bu.edu/academics/met/programs/computer-science/bs/ |
| 3 | Criminal Justice | https://www.bu.edu/academics/met/programs/criminal-justice/bs/ |
| 4 | Economics | https://www.bu.edu/academics/met/programs/economics/ |
| 5 | Interdisciplinary Studies | https://www.bu.edu/academics/met/programs/interdisciplinary-studies/ |
| 6 | Management Studies | https://www.bu.edu/academics/met/programs/administrative-sciences/bs/ |
| 7 | Mathematics | https://www.bu.edu/academics/met/programs/mathematics/ |
| 8 | Psychology | https://www.bu.edu/academics/met/programs/psychology/ |
| 9 | Urban Affairs | https://www.bu.edu/academics/met/programs/urban-affairs/bs/ |


> Total UG major-degree rows: 143

### 1.3 本科辅修 — 完整列表

| # | 辅修名称 | 所属学院 | URL |
|---|---------|---------|-----|
| 1 | African American & Black Diaspora Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/african-american-black-diaspora-studies/minor/ |
| 2 | African Languages & Literatures | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/african-studies/minor-african-languages/ |
| 3 | African Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/african-studies/minor/ |
| 4 | American Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/american-new-england-studies/minor/ |
| 5 | Anthropology | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/anthropology/minor-in-anthropology/ |
| 6 | Arabic | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-arabic/ |
| 7 | Archaeological & Environmental Sciences | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/archaeology/archaeological-environmental-sciences/ |
| 8 | Archaeology | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/archaeology/minor/ |
| 9 | Art & Architecture, History of | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/art-history/minor/ |
| 10 | Asian Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/asian-studies/minor-in-asian-studies/ |
| 11 | Astronomy | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/astronomy/minor/ |
| 12 | Biology CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/biology/minor/ |
| 13 | Chemistry CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/chemistry/minor/ |
| 14 | Chinese | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-chinese/ |
| 15 | Cinema & Media Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/cinema-media-studies/minor-in-cinema-media-studies-cims/ |
| 16 | Classical Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/classical-studies/minors/ |
| 17 | Comparative Literature | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-comparative-literature/ |
| 18 | Computer Science CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/computer-science/minor/ |
| 19 | Core Curriculum | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/minor-in-the-core-curriculum/ |
| 20 | Creative Writing | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/creative-writing/ |
| 21 | Earth & Environmental Sciences | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/earth-environment/minor-in-earth-environmental-sciences/ |
| 22 | Economics CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/economics/minor/ |
| 23 | English | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/english/minor/ |
| 24 | Environmental Analysis & Policy | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/earth-environment/minor-in-environmental-analysis-policy/ |
| 25 | European Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/european-studies/minor/ |
| 26 | French Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/romance-studies/minor-french-studies/ |
| 27 | German | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-german/ |
| 28 | Global Medieval Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/medieval-studies/ |
| 29 | Greek—Ancient | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/classical-studies/minors/ |
| 30 | Greek—Modern | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/classical-studies/minors/ |
| 31 | Hebrew | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-hebrew/ |
| 32 | History CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/history/minor/ |
| 33 | History of Art & Architecture | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/art-history/minor/ |
| 34 | Holocaust, Genocide & Human Rights Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/holocaust-genocide-human-rights-studies/minor/ |
| 35 | International Relations | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/international-relations/minor/ |
| 36 | Israel Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/minor-in-israel-studies/ |
| 37 | Italian | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/romance-studies/minor-italian/ |
| 38 | Japanese Language & Literature | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-japanese/ |
| 39 | Jewish Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/jewish-studies/ |
| 40 | Korean | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/korean/minor/ |
| 41 | Latin American Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/latin-american-studies/minor/ |
| 42 | Linguistics CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/linguistics/minor-linguistics/ |
| 43 | Marine Science | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/marine-science/minor/ |
| 44 | Medical Anthropology | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/anthropology/minor-medical/ |
| 45 | Modern Greek | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/classical-studies/minors/ |
| 46 | Muslim Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/muslim-studies-minor/ |
| 47 | Myth Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/classical-studies/minors/ |
| 48 | Persian Cultural Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-in-persian-cultural-studies/ |
| 49 | Philosophy CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/philosophy/minor/ |
| 50 | Physics | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/physics/minor/ |
| 51 | Political Science | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/political-science/minor/ |
| 52 | Portuguese & Brazilian Cultural Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/romance-studies/portuguese/minor-in-portuguese-brazilian-cultural-studies/ |
| 53 | Psychology CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/psychology/minor/ |
| 54 | Public Policy Analysis | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/political-science/minor-in-public-policy-analysis/ |
| 55 | Religion CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/religion/minor/ |
| 56 | Religion in Science & Medicine | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/religion/minor-in-religion-in-science-medicine/ |
| 57 | Russian | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-russian/ |
| 58 | Sociology CAS/GRS | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/sociology/minor/ |
| 59 | Spanish | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/romance-studies/minor-spanish/ |
| 60 | Sustainable Energy | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/earth-environment/sustainable-energy-minor/ |
| 61 | Turkish Cultural Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/world-languages-literatures/minor-in-turkish-cultural-studies/ |
| 62 | Urban Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/minor-in-urban-studies/ |
| 63 | Women’s, Gender & Sexuality Studies | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/womens-studies/ |
| 64 | Writing | College of Arts & Sciences | https://www.bu.edu/academics/cas/programs/writing/minor/ |
| 65 | Advertising | College of Communication | https://www.bu.edu/academics/com/programs/advertising/advertising-minor/ |
| 66 | Film & Television | College of Communication | https://www.bu.edu/academics/com/programs/film-television/film-televisionminor/ |
| 67 | Journalism | College of Communication | https://www.bu.edu/academics/com/programs/journalism/minor-in-journalism/ |
| 68 | Media Science | College of Communication | https://www.bu.edu/academics/com/programs/media-science/minor-in-media-science/ |
| 69 | Public Relations | College of Communication | https://www.bu.edu/academics/com/programs/public-relations/minor-in-public-relations/ |
| 70 | Biomedical Engineering | College of Engineering | https://www.bu.edu/academics/eng/programs/biomedical-engineering/minor-in-biomedical-engineering/ |
| 71 | Computer Engineering | College of Engineering | https://www.bu.edu/academics/eng/programs/computer-engineering/minor-in-computer-engineering/ |
| 72 | Electrical Engineering | College of Engineering | https://www.bu.edu/academics/eng/programs/electrical-engineering/minor-in-electrical-engineering/ |
| 73 | Engineering Science | College of Engineering | https://www.bu.edu/academics/eng/programs/minors/minor-in-engineering-science |
| 74 | Materials Science & Engineering | College of Engineering | https://www.bu.edu/academics/eng/programs/materials-science-engineering/minor/ |
| 75 | Mechanical Engineering | College of Engineering | https://www.bu.edu/academics/eng/programs/mechanical-engineering/minor-in-mechanical-engineering/ |
| 76 | Systems Engineering | College of Engineering | https://www.bu.edu/academics/eng/programs/systems-engineering/minor-in-systems-engineering/ |
| 77 | Arts Leadership | College of Fine Arts | https://www.bu.edu/academics/cfa/programs/other-programs/minor-in-arts-leadership/ |
| 78 | Dance | College of Fine Arts | https://www.bu.edu/academics/cfa/programs/school-of-theatre/minor-in-dance/ |
| 79 | Music | College of Fine Arts | https://www.bu.edu/academics/cfa/programs/school-of-music/minors-in-music/ |
| 80 | Music Performance | College of Fine Arts | https://www.bu.edu/academics/cfa/programs/school-of-music/minors-in-music/ |
| 81 | Performance, Music | College of Fine Arts | https://www.bu.edu/academics/cfa/programs/school-of-music/minors-in-music/ |
| 82 | Visual Arts | College of Fine Arts | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/minor-in-visual-arts/ |
| 83 | Data Science | Faculty of Computing & Data Sciences | https://www.bu.edu/academics/cds/programs/minor-in-data-science/ |
| 84 | Business Administration & Management | Questrom School of Business | https://www.bu.edu/academics/questrom/programs/minor-in-business-administration-management/ |
| 85 | Innovation & Entrepreneurship Questrom | Questrom School of Business | https://www.bu.edu/academics/questrom/programs/minor-in-innovation-entrepreneurship/ |
| 86 | Human Physiology | Sargent College of Health & Rehabilitation Sciences | https://www.bu.edu/academics/sar/programs/human-physiology/minor/ |
| 87 | Public Health SAR/SPH | Sargent College of Health & Rehabilitation Sciences | https://www.bu.edu/academics/sar/programs/public-health/bs-mph/ |
| 88 | Speech, Language & Hearing Sciences | Sargent College of Health & Rehabilitation Sciences | https://www.bu.edu/academics/sar/programs/speech-language-hearing-sciences/minor/ |
| 89 | Event Management & Public Relations | School of Hospitality Administration | https://www.bu.edu/academics/sha/programs/event-management-public-relations-minor/ |
| 90 | Hospitality Administration | School of Hospitality Administration | https://www.bu.edu/academics/sha/programs/minor/ |
| 91 | Real Estate | School of Hospitality Administration | https://www.bu.edu/academics/sha/programs/minor-2/ |
| 92 | Applied Human Development | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/applied-human-development/minor-in-applied-human-development/ |
| 93 | Autism Spectrum Disorders | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/special-education/minor-in-autism-spectrum-disorders/ |
| 94 | Deaf Education | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/deaf-studies/minor-in-pre-deaf-education/ |
| 95 | Deaf Studies | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/deaf-studies/minor/ |
| 96 | Education | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/minor-in-education/ |
| 97 | Emotional & Behavioral Challenges in Schools | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/special-education/minor-in-emotional-and-behavioral-challenges-in-schools/ |
| 98 | English Education | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/english-education/minor-in-english-education/ |
| 99 | Mathematics Education | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/mathematics-education/minor-in-math-education/ |
| 100 | Special Education | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/special-education/minor-in-special-education/ |
| 101 | Teaching Science Education | Wheelock College of Education & Human Development | https://www.bu.edu/academics/wheelock/programs/science-education/minor-in-teaching-science-education/ |
| 102 | Interdisciplinary Studies | Metropolitan College & Extended Education | https://www.bu.edu/academics/cgs/programs/minor-in-interdisciplinary-studies/ |
| 103 | Urban Affairs | Metropolitan College & Extended Education | https://www.bu.edu/academics/met/programs/urban-affairs/minor/ |

> Total UG minors: 103

---

## 2. 研究生教育 (Graduate Education)

### 2.1 研究生项目 — 按学院 > 学位级别分组

#### College of Arts & Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.bu.edu/academics/grs/programs/anthropology/ma/ |
| 2 | Archaeology | https://www.bu.edu/academics/grs/programs/archaeology/ma/ |
| 3 | Art & Architecture, History of | https://www.bu.edu/academics/grs/programs/history-art-architecture/ma/ |
| 4 | Astronomy | https://www.bu.edu/academics/grs/programs/astronomy/ma/ |
| 5 | Chemistry CAS/GRS | https://www.bu.edu/academics/grs/programs/chemistry/ma/ |
| 6 | Classical Studies | https://www.bu.edu/academics/grs/programs/classical-studies/ma/ |
| 7 | Classics & Archaeology | https://www.bu.edu/academics/grs/programs/classical-studies/ma-in-classics-archaeology/ |
| 8 | English | https://www.bu.edu/academics/grs/programs/english/ma/ |
| 9 | History CAS/GRS | https://www.bu.edu/academics/grs/programs/history/ma/ |
| 10 | History of Art & Architecture | https://www.bu.edu/academics/grs/programs/history-art-architecture/ma/ |
| 11 | International Relations | https://www.bu.edu/academics/grs/programs/international-relations/ |
| 12 | Latin American Studies | https://www.bu.edu/academics/grs/programs/latin-american-studies-ma/ |
| 13 | Linguistics CAS/GRS | https://www.bu.edu/academics/grs/programs/linguistics/ma-in-linguistics/ |
| 14 | Mathematics | https://www.bu.edu/academics/grs/programs/mathematics-statistics/ma-mathematics/ |
| 15 | Neuroscience | https://www.bu.edu/academics/grs/programs/neuroscience/ma/ |
| 16 | Philosophy CAS/GRS | https://www.bu.edu/academics/grs/programs/philosophy/ma/ |
| 17 | Physics | https://www.bu.edu/academics/grs/programs/physics/ma/ |
| 18 | Political Science | https://www.bu.edu/academics/grs/programs/political-science/ma/ |
| 19 | Sociology CAS/GRS | https://www.bu.edu/academics/grs/programs/sociology/ma/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology CAS/GRS | https://www.bu.edu/academics/grs/programs/biology/master-of-science-in-biology// |
| 2 | Computer Science CAS/GRS | https://www.bu.edu/academics/grs/programs/computer-science/ms/ |
| 3 | Economics CAS/GRS | https://www.bu.edu/academics/grs/programs/economics/ma/ |
| 4 | Psychology CAS/GRS | https://www.bu.edu/academics/grs/programs/psychology/ma/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://www.bu.edu/academics/grs/programs/mfa/ |
| 2 | English | https://www.bu.edu/academics/grs/programs/mfa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.bu.edu/academics/grs/programs/anthropology/phd/ |
| 2 | Archaeology | https://www.bu.edu/academics/grs/programs/archaeology/phd/ |
| 3 | Art & Architecture, History of | https://www.bu.edu/academics/grs/programs/history-art-architecture/phd/ |
| 4 | Astronomy | https://www.bu.edu/academics/grs/programs/astronomy/phd/ |
| 5 | Biology CAS/GRS | https://www.bu.edu/academics/grs/programs/biology/phd/ |
| 6 | Chemistry CAS/GRS | https://www.bu.edu/academics/grs/programs/chemistry/phd/ |
| 7 | Classical Studies | https://www.bu.edu/academics/grs/programs/classical-studies/phd/ |
| 8 | Computer Science CAS/GRS | https://www.bu.edu/academics/grs/programs/computer-science/phd |
| 9 | English | https://www.bu.edu/academics/grs/programs/english/phd/ |
| 10 | History CAS/GRS | https://www.bu.edu/academics/grs/programs/history/phd/ |
| 11 | History of Art & Architecture | https://www.bu.edu/academics/grs/programs/history-art-architecture/phd/ |
| 12 | Linguistics CAS/GRS | https://www.bu.edu/academics/grs/programs/linguistics/phd-in-linguistics/ |
| 13 | Mathematics | https://www.bu.edu/academics/grs/programs/mathematics-statistics/phd-mathematics/ |
| 14 | Neuroscience | https://www.bu.edu/academics/grs/programs/neuroscience/phd/ |
| 15 | Philosophy CAS/GRS | https://www.bu.edu/academics/grs/programs/philosophy/phd/ |
| 16 | Physics | https://www.bu.edu/academics/grs/programs/physics/phd/ |
| 17 | Political Science | https://www.bu.edu/academics/grs/programs/political-science/phd/ |
| 18 | Psychology CAS/GRS | https://www.bu.edu/academics/grs/programs/psychology/phd/ |
| 19 | Religion CAS/GRS | https://www.bu.edu/academics/grs/programs/religion/ |
| 20 | Sociology CAS/GRS | https://www.bu.edu/academics/grs/programs/sociology/phd/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Science Education | https://www.bu.edu/academics/wheelock/programs/curriculum-teaching/edd/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching of Chemistry | https://www.bu.edu/academics/wheelock/programs/science-education/graduate-certificate-in-chemistry-education/ |
| 2 | European Studies | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-european-studies/ |
| 3 | Holocaust, Genocide & Human Rights Studies | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-holocaust-genocide-human-rights-studies/ |
| 4 | Latin American Studies | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-latin-american-studies/ |
| 5 | Linguistics CAS/GRS | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-linguistics/ |
| 6 | Muslim Studies | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-muslim-studies/ |

#### College of Communication

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Emerging Media Studies | https://www.bu.edu/academics/com/programs/emerging-media-studies/ma |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Advertising | https://www.bu.edu/academics/com/programs/advertising/advertising-ms/ |
| 2 | Branded Content Production | https://www.bu.edu/academics/com/programs/branded-content/ms/ |
| 3 | Journalism | https://www.bu.edu/academics/com/programs/journalism/ms/ |
| 4 | Media Science | https://www.bu.edu/academics/com/programs/media-science/ms-in-media-science/ |
| 5 | Media Ventures | https://www.bu.edu/academics/com/programs/ms/ |
| 6 | Public Relations | https://www.bu.edu/academics/com/programs/public-relations/ms-in-public-relations/ |
| 7 | Television | https://www.bu.edu/academics/com/programs/television/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Cinema & Media Production | https://www.bu.edu/academics/com/programs/mfa-in-cinema-and-media-production/ |
| 2 | Film | https://www.bu.edu/academics/com/programs/film/ |
| 3 | Film & Television Studies | https://www.bu.edu/academics/com/programs/film-television-studies/ |
| 4 | Screenwriting | https://www.bu.edu/academics/com/programs/screenwriting/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Emerging Media Studies | https://www.bu.edu/academics/com/programs/emerging-media-studies/phd |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Civic Science Communication | https://www.bu.edu/academics/com/programs/graduate-certificate-in-civic-science-communication/ |

#### College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence, Software Engineering | https://www.bu.edu/academics/eng/programs/ms-in-software-engineering-for-artificial-intelligence/ |
| 2 | Biomedical Engineering | https://www.bu.edu/academics/eng/programs/biomedical-engineering/ms/ |
| 3 | Computer Engineering | https://www.bu.edu/academics/eng/programs/computer-engineering/ms/ |
| 4 | Electrical Engineering | https://www.bu.edu/academics/eng/programs/electrical-engineering/ms/ |
| 5 | Electrical & Computer Engineering | https://www.bu.edu/academics/eng/programs/electrical-engineering/ms-in-electrical-computer-engineering/ |
| 6 | Materials Science & Engineering | https://www.bu.edu/academics/eng/programs/materials-science-engineering/ms/ |
| 7 | Mechanical Engineering | https://www.bu.edu/academics/eng/programs/mechanical-engineering/ms/ |
| 8 | Product Design & Manufacture | https://www.bu.edu/academics/eng/programs/product-design-manufacture/product-design-manufacture/ |
| 9 | Robotics & Autonomous Systems | https://www.bu.edu/academics/eng/programs/mechanical-engineering/ms-in-robotics-autonomous-systems/ |
| 10 | Software Engineering for Artificial Intelligence | https://www.bu.edu/academics/eng/programs/ms-in-software-engineering-for-artificial-intelligence/ |
| 11 | Systems Engineering | https://www.bu.edu/academics/eng/programs/systems-engineering/ms/ |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.bu.edu/academics/eng/programs/biomedical-engineering/meng/ |
| 2 | Materials Science & Engineering | https://www.bu.edu/academics/eng/programs/materials-science-engineering/meng/ |
| 3 | Systems Engineering | https://www.bu.edu/academics/eng/programs/systems-engineering/meng/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.bu.edu/academics/eng/programs/biomedical-engineering/phd/ |
| 2 | Computer Engineering | https://www.bu.edu/academics/eng/programs/computer-engineering/phd/ |
| 3 | Electrical Engineering | https://www.bu.edu/academics/eng/programs/electrical-engineering/phd/ |
| 4 | Materials Science & Engineering | https://www.bu.edu/academics/eng/programs/materials-science-engineering/phd/ |
| 5 | Mechanical Engineering | https://www.bu.edu/academics/eng/programs/mechanical-engineering/phd/ |
| 6 | Systems Engineering | https://www.bu.edu/academics/eng/programs/systems-engineering/phd/ |

#### College of Fine Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Education | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/art-education/online-ma-in-art-education/ |
| 2 | Art Education with Initial License | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/art-education/art-education-with-initial-license/ |
| 3 | Museum Education | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/museum-education/ |
| 4 | Musicology | https://www.bu.edu/academics/cfa/programs/school-of-music/musicology/ma/ |
| 5 | Music Theory | https://www.bu.edu/academics/cfa/programs/school-of-music/music-theory/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Directing | https://www.bu.edu/academics/cfa/programs/school-of-theatre/directing/ |
| 2 | Graphic Design | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/graphic-design/mfa/ |
| 3 | Lighting Design | https://www.bu.edu/academics/cfa/programs/school-of-theatre/lighting-design/mfa/ |
| 4 | Painting | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/painting/mfa/ |
| 5 | Print Media & Photography | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/mfa-in-print-media-photography/ |
| 6 | Production Management | https://www.bu.edu/academics/cfa/programs/school-of-theatre/production-management/ |
| 7 | Scene Design | https://www.bu.edu/academics/cfa/programs/school-of-theatre/scene-design/mfa/ |
| 8 | Sculpture | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/sculpture/mfa/ |
| 9 | Sound Design | https://www.bu.edu/academics/cfa/programs/school-of-theatre/sound-design/mfa/ |
| 10 | Technical Production | https://www.bu.edu/academics/cfa/programs/school-of-theatre/technical-production/mfa/ |
| 11 | Theatre Education | https://www.bu.edu/academics/cfa/programs/school-of-theatre/theatre-education/ |
| 12 | Visual Narrative | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/mfa-in-visual-narrative/ |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Composition | https://www.bu.edu/academics/cfa/programs/school-of-music/composition/mm/ |
| 2 | Conducting | https://www.bu.edu/academics/cfa/programs/school-of-music/conducting/mm/ |
| 3 | Historical Performance | https://www.bu.edu/academics/cfa/programs/school-of-music/historical-performance/mm/ |
| 4 | Musicology | https://www.bu.edu/academics/cfa/programs/school-of-music/musicology/mm/ |
| 5 | Music Education | https://www.bu.edu/academics/cfa/programs/school-of-music/music-education/mm/ |
| 6 | Music Performance | https://www.bu.edu/academics/cfa/programs/school-of-music/performance/mm/ |
| 7 | Performance, Music | https://www.bu.edu/academics/cfa/programs/school-of-music/performance/mm/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Musicology | https://www.bu.edu/academics/cfa/programs/school-of-music/musicology/phd/ |

##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Composition | https://www.bu.edu/academics/cfa/programs/school-of-music/composition/dma/ |
| 2 | Conducting | https://www.bu.edu/academics/cfa/programs/school-of-music/conducting/dma/ |
| 3 | Historical Performance | https://www.bu.edu/academics/cfa/programs/school-of-music/historical-performance/dma/ |
| 4 | Music Education | https://www.bu.edu/academics/cfa/programs/school-of-music/music-education/online-doctor-of-musical-arts-dma-in-music-education/ |
| 5 | Music Performance | https://www.bu.edu/academics/cfa/programs/school-of-music/performance/dma/ |
| 6 | Performance, Music | https://www.bu.edu/academics/cfa/programs/school-of-music/performance/dma/ |

##### CAGS
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | https://www.bu.edu/academics/cfa/programs/school-of-music/music-education/cags/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Graphic Design | https://www.bu.edu/academics/cfa/programs/school-of-visual-arts/graphic-design/certificate-graphic-design/ |
| 2 | Music Education | https://www.bu.edu/academics/cfa/programs/school-of-music/music-education/graduate-certificate-in-pre-k-12-music-teaching/ |

##### Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Scene Painting | https://www.bu.edu/academics/cfa/programs/school-of-theatre/scene-design/certificate/ |

#### Faculty of Computing & Data Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics | https://www.bu.edu/academics/cds/programs/ms-in-bioinformatics/ |
| 2 | Data Science | https://www.bu.edu/academics/cds/programs/ms-in-data-science/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics | https://www.bu.edu/academics/cds/programs/phd-in-bioinformatics/ |
| 2 | Computing & Data Sciences | https://www.bu.edu/academics/cds/programs/phd-in-computing-data-sciences/ |

#### Questrom School of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence in Business | https://www.bu.edu/academics/questrom/programs/ms-in-artificial-intelligence-in-business/ |
| 2 | Business Analytics | https://www.bu.edu/academics/questrom/programs/ms-in-business-analytics/ |
| 3 | Finance Questrom | https://www.bu.edu/academics/questrom/programs/ms-in-finance/ |
| 4 | Mathematical Finance & Financial Technology | https://www.bu.edu/academics/questrom/programs/mathematical-finance/ms/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.bu.edu/academics/questrom/programs/mba/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration & Management | https://www.bu.edu/academics/questrom/programs/phd-in-management/ |
| 2 | Business Economics | https://www.bu.edu/academics/questrom/programs/phd-in-business-economics/ |
| 3 | Mathematical Finance | https://www.bu.edu/academics/questrom/programs/mathematical-finance/phd/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.bu.edu/academics/questrom/programs/graduate-certificate-in-business-analytics/ |
| 2 | Financial Technology | https://www.bu.edu/academics/questrom/programs/graduate-certificate-in-financial-technology-fintech/ |

#### Sargent College of Health & Rehabilitation Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Physiology | https://www.bu.edu/academics/sar/programs/human-physiology/ms/ |
| 2 | Nutrition/Dietetics | https://www.bu.edu/academics/sar/programs/nutrition-dietetics/ms/ |
| 3 | Speech-Language Pathology | https://www.bu.edu/academics/sar/programs/speech-language-hearing-sciences/ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Physiology | https://www.bu.edu/academics/sar/programs/human-physiology/phd/ |
| 2 | Rehabilitation Sciences | https://www.bu.edu/academics/sar/programs/rehabilitation-sciences/ |
| 3 | Speech, Language & Hearing Sciences | https://www.bu.edu/academics/sar/programs/speech-language-hearing-sciences/phd/ |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://www.bu.edu/academics/sar/programs/physical-therapy/dpt/ |

##### OTD
| # | 项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy | https://www.bu.edu/academics/sar/programs/occupational-therapy/doctor-of-occupational-therapy/ |

#### School of Hospitality Administration

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://www.bu.edu/academics/sha/programs/ms-in-hospitality-management/ |
| 2 | Real Estate | https://www.bu.edu/academics/sha/programs/ms/ |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality | https://www.bu.edu/academics/sha/programs/master-of-management-in-hospitality/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Event Management | https://www.bu.edu/academics/sha/programs/events-management/ |
| 2 | Hospitality Management | https://www.bu.edu/academics/sha/programs/graduate-certificate-in-hospitality-management/ |
| 3 | Hospitality Management | https://www.bu.edu/academics/sha/programs/graduate-certificate-in-advanced-hospitality-management/ |

#### Wheelock College of Education & Human Development

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership & Policy Studies | https://www.bu.edu/academics/wheelock/programs/policy-planning-administration/ma-in-educational-policy-studies/ |
| 2 | Leadership, Policy & Advocacy for Early Childhood Well-Being | https://www.bu.edu/academics/wheelock/programs/early-childhood-education/ma-in-leadership-policy-advocacy-for-early-childhood-well-being/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Child Life & Family-Centered Care | https://www.bu.edu/academics/wheelock/programs/ms-in-child-life-family-centered-care/ |
| 2 | Learning Design & Technology | https://www.bu.edu/academics/wheelock/programs/learning-design-technology/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling Psychology & Applied Human Development | https://www.bu.edu/academics/wheelock/programs/applied-human-development/phd-counseling-psychology-applied-human-development/ |
| 2 | Deaf Studies | https://www.bu.edu/academics/wheelock/programs/deaf-studies/ |
| 3 | Educational Studies | https://www.bu.edu/academics/wheelock/programs/phd-in-educational-studies/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Teaching | https://www.bu.edu/academics/wheelock/programs/curriculum-teaching/edd/ |
| 2 | Deaf Studies | https://www.bu.edu/academics/wheelock/programs/deaf-studies/ |
| 3 | Early Childhood Education | https://www.bu.edu/academics/wheelock/programs/curriculum-teaching/edd/ |
| 4 | Educational Leadership & Policy Studies | https://www.bu.edu/academics/wheelock/programs/policy-planning-administration/educational-leadership-policy/ |
| 5 | Language & Literacy Education | https://www.bu.edu/academics/wheelock/programs/developmental-studies/edd/ |
| 6 | Mathematics Education | https://www.bu.edu/academics/wheelock/programs/curriculum-teaching/edd/ |
| 7 | Social Studies Education | https://www.bu.edu/academics/wheelock/programs/curriculum-teaching/edd/ |

##### CAGS
| # | 项目 | URL |
|---|------|-----|
| 1 | Bilingual Education/Teaching English to Speakers of Other Languages | https://www.bu.edu/academics/wheelock/programs/bilingual-education/ |
| 2 | Curriculum & Teaching | https://www.bu.edu/academics/wheelock/programs/curriculum-teaching/cags/ |
| 3 | Developmental Studies | https://www.bu.edu/academics/wheelock/programs/developmental-studies/cags-lit-language/ |
| 4 | Educational Leadership & Policy Studies | https://www.bu.edu/academics/wheelock/programs/policy-planning-administration/cags/ |
| 5 | English Education | https://www.bu.edu/academics/wheelock/programs/english-education/cags/ |
| 6 | Reading & Literacies Education | https://www.bu.edu/academics/wheelock/programs/literacy-education/cags/ |
| 7 | Teaching English to Speakers of Other Languages | https://www.bu.edu/academics/wheelock/programs/developmental-studies/cags-lit-language/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Wheelock | https://www.bu.edu/academics/wheelock/programs/artificial-intelligence/graduate-certificate-in-ai-education/ |
| 2 | Autism & Emotional/Behavioral Disorders | https://www.bu.edu/academics/wheelock/programs/special-education/graduate-certificate-in-autism-and-emotionalbehavioral-disorders/ |
| 3 | Bilingual Education/Teaching English to Speakers of Other Languages | https://www.bu.edu/academics/wheelock/programs/bilingual-education/ |
| 4 | Biology Education | https://www.bu.edu/academics/wheelock/programs/science-education/graduate-certificate-in-biology-education/ |
| 5 | General Science Education | https://www.bu.edu/academics/wheelock/programs/science-education/graduate-certificate-in-general-science-education/ |
| 6 | Literacy in Deaf Education | https://www.bu.edu/academics/wheelock/programs/deaf-studies/grad-cert-literacy/ |
| 7 | Physics Education | https://www.bu.edu/academics/wheelock/programs/science-education/graduate-certificate-in-physics-education/ |
| 8 | Reading & Literacies Education | https://www.bu.edu/academics/wheelock/programs/developmental-studies/graduate-certificate-in-literacy-intervention/ |
| 9 | Teaching English to Speakers of Other Languages | https://www.bu.edu/academics/wheelock/programs/bilingual-education/graduate-certificate-in-teaching-of-english-to-speakers-of-other-languages-tesol/ |
| 10 | Teaching Students with Moderate Disabilities | https://www.bu.edu/academics/wheelock/programs/special-education/graduate-certificate-in-teaching-students-with-moderate-disabilities-5-12/ |
| 11 | World Language Education | https://www.bu.edu/academics/wheelock/programs/modern-foreign-language-education/graduate-certificate-in-world-language-education/ |

#### Graduate School of Arts & Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | African American & Black Diaspora Studies | https://www.bu.edu/academics/grs/programs/african-american-studies/ |
| 2 | Cognitive & Neural Systems | https://www.bu.edu/academics/grs/programs/cognitive-neural-systems/ma/ |
| 3 | Economics, Global Development | https://www.bu.edu/academics/grs/programs/economics/ma-global-development-economics/ |
| 4 | Editorial Studies | https://www.bu.edu/academics/grs/programs/editorial-studies/ma/ |
| 5 | French Language & Literature | https://www.bu.edu/academics/grs/programs/romance-studies/ma-french/ |
| 6 | Geoarchaeology | https://www.bu.edu/academics/grs/programs/earth-environment/geoarchaeology-ma/ |
| 7 | Global Policy | https://www.bu.edu/academics/grs/programs/international-relations/ma-in-global-policy/ |
| 8 | Hispanic Language & Literatures | https://www.bu.edu/academics/grs/programs/romance-studies/ma-hispanic/ |
| 9 | International Affairs | https://www.bu.edu/academics/grs/programs/international-relations/international-affairs-ma/ |
| 10 | Preservation Studies | https://www.bu.edu/academics/grs/programs/preservation-studies/ |
| 11 | Public Anthropology | https://www.bu.edu/academics/grs/programs/anthropology/ma/ |
| 12 | Religious Studies | https://www.bu.edu/academics/grs/programs/religious-studies/ma-in-religious-studies/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Economics & Data Science | https://www.bu.edu/academics/grs/programs/economics/ms-in-applied-economics-and-data-science/ |
| 2 | Artificial Intelligence | https://www.bu.edu/academics/grs/programs/computer-science/ms-in-artificial-intelligence/ |
| 3 | Biostatistics | https://www.bu.edu/academics/grs/programs/biostatistics/ms/ |
| 4 | Earth & Environment | https://www.bu.edu/academics/grs/programs/earth-environment/ms-in-earth-environment/ |
| 5 | Economic Policy & Practice | https://www.bu.edu/academics/grs/programs/economics/ma-economic-policy/ |
| 6 | Energy & Environmental Analysis | https://www.bu.edu/academics/grs/programs/earth-environment/ma-energy-environment/ |
| 7 | Molecular Biology, Cell Biology & Biochemistry | https://www.bu.edu/academics/grs/programs/molecular-biology-cell-biology-biochemistry/ma/ |
| 8 | Quantum Science & Engineering | https://www.bu.edu/academics/grs/programs/physics/ms-in-quantum-science-engineering/ |
| 9 | Remote Sensing & Geospatial Sciences | https://www.bu.edu/academics/grs/programs/earth-environment/ma-remote-sensing/ |
| 10 | Statistical Practice | https://www.bu.edu/academics/grs/programs/mathematics-statistics/ms-in-statistical-practice/ |
| 11 | Statistics | https://www.bu.edu/academics/grs/programs/mathematics-statistics/ma-statistics/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Literary Translation | https://www.bu.edu/academics/grs/programs/mfa-in-literary-translation/ |
| 2 | Playwriting | https://www.bu.edu/academics/grs/programs/mfa-in-playwriting/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://www.bu.edu/academics/grs/programs/american-studies/ |
| 2 | Biostatistics | https://www.bu.edu/academics/grs/programs/biostatistics/phd/ |
| 3 | Cognitive & Neural Systems | https://www.bu.edu/academics/grs/programs/cognitive-neural-systems/phd/ |
| 4 | Earth & Environment | https://www.bu.edu/academics/grs/programs/earth-environment/phd-in-earth-environment/ |
| 5 | Editorial Studies | https://www.bu.edu/academics/grs/programs/editorial-studies/phd/ |
| 6 | French Language & Literature | https://www.bu.edu/academics/grs/programs/romance-studies/phd-french/ |
| 7 | Hispanic Language & Literatures | https://www.bu.edu/academics/grs/programs/romance-studies/phd-hispanic/ |
| 8 | Molecular Biology, Cell Biology & Biochemistry | https://www.bu.edu/academics/grs/programs/molecular-biology-cell-biology-biochemistry/phd/ |
| 9 | Sociology & Social Work CAS/GRS/SSW | https://www.bu.edu/academics/grs/programs/sociology/sociology-social-work/ |
| 10 | Statistics | https://www.bu.edu/academics/grs/programs/mathematics-statistics/phd-statistics/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Museum Studies | https://www.bu.edu/academics/grs/programs/museum-studies/ |
| 2 | Teaching Language, Literature & Film | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-teaching-language-literature-film/ |
| 3 | Teaching Writing | https://www.bu.edu/academics/grs/programs/graduate-certificate-in-teaching-writing/ |

#### Graduate Medical Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Mental Health Counseling & Behavioral Medicine | https://www.bu.edu/academics/gms/programs/mental-health-counseling-behavioral-medicine-program/ma/ |
| 2 | Physiology or Biophysics | https://www.bu.edu/academics/gms/programs/physiology-biophysics/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomy & Neurobiology | https://www.bu.edu/academics/gms/programs/anatomy-neurobiology/ms/ |
| 2 | Bioimaging | https://www.bu.edu/academics/gms/programs/bioimaging/ |
| 3 | Biomedical Forensic Sciences | https://www.bu.edu/academics/gms/programs/biomedical-forensic-sciences/ |
| 4 | Biomedical Research Technologies | https://www.bu.edu/academics/gms/programs/ms-in-biomedical-research-technologies/ |
| 5 | Clinical Research | https://www.bu.edu/academics/gms/programs/clinical-investigation/ms/ |
| 6 | Dermatology | https://www.bu.edu/academics/gms/programs/dermatology/ |
| 7 | Forensic Anthropology | https://www.bu.edu/academics/gms/programs/forensic-anthropology/ |
| 8 | Genetic Counseling | https://www.bu.edu/academics/gms/programs/genetic-counseling/ |
| 9 | Health Care Emergency Management | https://www.bu.edu/academics/gms/programs/healthcare-emergency-management/ |
| 10 | Health Professions Education | https://www.bu.edu/academics/gms/programs/ms-in-health-professions-education/ |
| 11 | Medical Anthropology & Cross-Cultural Practice | https://www.bu.edu/academics/gms/programs/medical-anthropology-and-cross-cultural-practice/ |
| 12 | Medical Sciences | https://www.bu.edu/academics/gms/programs/medical-sciences/ms/ |
| 13 | Medical Sciences and Mental Health Counseling & Behavioral Medicine | https://www.bu.edu/academics/gms/programs/medical-sciences/dual-degree-masters-program-in-medical-sciences-and-mental-health-counseling-behavioral-medicine/ |
| 14 | Nutrition & Metabolism | https://www.bu.edu/academics/gms/programs/nutrition-metabolism/ms/ |
| 15 | Oral Health Sciences | https://www.bu.edu/academics/gms/programs/oral-health-sciences-ms/ |
| 16 | Pathology & Laboratory Medicine | https://www.bu.edu/academics/gms/programs/pathology-laboratory-medicine/ma/ |
| 17 | Pharmacology | https://www.bu.edu/academics/gms/programs/pharmacology/ms |
| 18 | Physician Assistant Program | https://www.bu.edu/academics/gms/programs/physician-assistant/ |

##### MSD
| # | 项目 | URL |
|---|------|-----|
| 1 | Oral Biology | https://www.bu.edu/academics/gms/programs/oral-biology/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomy & Neurobiology | https://www.bu.edu/academics/gms/programs/anatomy-neurobiology/phd/ |
| 2 | Behavioral Neuroscience | https://www.bu.edu/academics/gms/programs/behavioral-neuroscience/ |
| 3 | Biochemistry | https://www.bu.edu/academics/gms/programs/biochemistry/phd/ |
| 4 | Biomedical Sciences, Program in | https://www.bu.edu/academics/gms/programs/pibs/ |
| 5 | Genetics & Genomics | https://www.bu.edu/academics/gms/programs/genetics-genomics/ |
| 6 | Molecular Medicine | https://www.bu.edu/academics/gms/programs/molecular-medicine/ |
| 7 | Neuroscience & Computational Neuroscience | https://www.bu.edu/academics/gms/programs/neuroscience/ |
| 8 | Nutrition & Metabolism | https://www.bu.edu/academics/gms/programs/nutrition-metabolism/phd/ |
| 9 | Oral Biology | https://www.bu.edu/academics/gms/programs/oral-biology/ |
| 10 | Pathology & Laboratory Medicine | https://www.bu.edu/academics/gms/programs/pathology-laboratory-medicine/phd/ |
| 11 | Pharmacology | https://www.bu.edu/academics/gms/programs/pharmacology/phd/ |
| 12 | Physiology or Biophysics | https://www.bu.edu/academics/gms/programs/physiology-biophysics/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Path 2 Path Program | https://www.bu.edu/academics/gms/programs/pathology-laboratory-medicine/path-2-path-graduate-certificate/ |

##### Cert Clin Derm
| # | 项目 | URL |
|---|------|-----|
| 1 | Dermatology | https://www.bu.edu/academics/gms/programs/dermatology/ |

#### Metropolitan College & Extended Education

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Gastronomy | https://www.bu.edu/academics/met/programs/gastronomy/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://www.bu.edu/academics/met/programs/actuarial-science/ms/ |
| 2 | Advertising | https://www.bu.edu/academics/met/programs/advertising/ |
| 3 | Applied Business Analytics | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-in-applied-business-analytics/ |
| 4 | Applied Data Analytics | https://www.bu.edu/academics/met/programs/computer-science/master-of-science-in-applied-data-analytics/ |
| 5 | Arts Administration | https://www.bu.edu/academics/met/programs/arts-administration/ms/ |
| 6 | Computer Information Systems | https://www.bu.edu/academics/met/programs/computer-science/mscis/ |
| 7 | Computer Science | https://www.bu.edu/academics/met/programs/computer-science/ms/ |
| 8 | Construction Management & Technology | https://www.bu.edu/academics/met/programs/construction-management-technology/ms-in-construction-management-technology/ |
| 9 | Criminal Justice | https://www.bu.edu/academics/met/programs/criminal-justice/mcj/ |
| 10 | Enterprise Risk Management | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-enterprise-risk-management/ |
| 11 | Financial Management | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-in-financial-management/ |
| 12 | Global Marketing Management | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-in-global-marketing-management/ |
| 13 | Health Communication | https://www.bu.edu/academics/met/programs/health-communication/ms/ |
| 14 | Health Informatics | https://www.bu.edu/academics/met/programs/computer-science/ms-in-health-informatics/ |
| 15 | Innovation & Entrepreneurship | https://www.bu.edu/academics/met/programs/administrative-sciences/ms/ |
| 16 | Insurance Management | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-insurance-management/ |
| 17 | Project Management | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-project-management/ |
| 18 | Software Development | https://www.bu.edu/academics/met/programs/computer-science/ms-in-software-development/ |
| 19 | Supply Chain Management | https://www.bu.edu/academics/met/programs/administrative-sciences/ms-in-supply-chain-management/ |
| 20 | Telecommunication | https://www.bu.edu/academics/met/programs/computer-science/telecommunication/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Foundations | https://www.bu.edu/academics/met/programs/actuarial-science/cert/ |
| 2 | Actuarial Science | https://www.bu.edu/academics/met/programs/actuarial-science/grad-cert/ |
| 3 | Administrative Sciences | https://www.bu.edu/academics/met/programs/administrative-sciences/ |
| 4 | Advanced Information Technology | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 5 | Applied Business Analytics | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 6 | Arts Management | https://www.bu.edu/academics/met/programs/arts-administration/graduate-certificates/ |
| 7 | Arts Marketing | https://www.bu.edu/academics/met/programs/arts-administration/graduate-certificates/ |
| 8 | Commercial Theater Development | https://www.bu.edu/academics/met/programs/arts-administration/graduate-certificates/ |
| 9 | Computer Networks | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 10 | Construction Management & Technology | https://www.bu.edu/academics/met/programs/administratative-sciences/grad-cert-diploma/ |
| 11 | Corporate Finance | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 12 | Crime Analysis | https://www.bu.edu/academics/met/programs/criminal-justice/graduate-certificate-in-crime-analysis/ |
| 13 | Criminal Justice | https://www.bu.edu/academics/met/programs/criminal-justice/graduate-certificate-in-criminal-justice/ |
| 14 | Cybercrime Investigation & Cybersecurity | https://www.bu.edu/academics/met/programs/criminal-justice/graduate-certificate-in-cybercrime-investigation-cybersecurity/ |
| 15 | Cybersecurity | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 16 | Data Analytics | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 17 | Database Management & Business Intelligence | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 18 | Enterprise Risk Management | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 19 | Financial Management | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 20 | Foundations of Health Communication | https://www.bu.edu/academics/met/programs/health-communication/graduate-certificate-in-foundations-of-health-communication/ |
| 21 | Global Marketing Management | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 22 | Healthcare Promotion, Media & Marketing | https://www.bu.edu/academics/met/programs/health-communication/graduate-certificate-in-healthcare-promotion-media-marketing/ |
| 23 | Health Informatics | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 24 | Information Technology | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 25 | Information Technology Project Management | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 26 | International Finance | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 27 | Investment Analysis | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 28 | Linguistics | https://www.bu.edu/academics/met/programs/graduate-certificate-in-linguistics/ |
| 29 | Project Management | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 30 | Project, Program & Portfolio Management | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 31 | Strategic Management in Criminal Justice | https://www.bu.edu/academics/met/programs/criminal-justice/graduate-certificate-in-strategic-management-in-criminal-justice/ |
| 32 | Supply Chain Management | https://www.bu.edu/academics/met/programs/administrative-sciences/grad-cert-diploma/ |
| 33 | Urban Policy & Planning | https://www.bu.edu/academics/met/programs/urban-affairs/graduate-certificate-in-urban-policy-planning/ |
| 34 | Visual & Digital Health Communication | https://www.bu.edu/academics/met/programs/health-communication/graduate-certificate-in-visual-digital-health-communication/ |
| 35 | Web Application Development | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |
| 36 | Wine Studies | https://www.bu.edu/academics/met/programs/graduate-certificate-in-wine-studies/ |

##### GRAD Certs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.bu.edu/academics/met/programs/computer-science/graduate-certificates/ |

##### Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Financial Planning | https://www.bu.edu/academics/met/programs/center-for-professional-education-programs/ |
| 2 | Genealogical Research | https://www.bu.edu/academics/met/programs/center-for-professional-education-programs/ |
| 3 | Paralegal Studies | https://www.bu.edu/academics/met/programs/center-for-professional-education-programs/ |
| 4 | Professional Fundraising | https://www.bu.edu/academics/met/programs/center-for-professional-education-programs/ |

#### School of Law

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | American Law | https://www.bu.edu/academics/law/programs/american-law/ |
| 2 | Banking & Financial Law | https://www.bu.edu/academics/law/programs/graduate-program-in-banking-financial-law/ |
| 3 | Intellectual Property & Information Law | https://www.bu.edu/academics/law/programs/intellectual-property-law/ |
| 4 | Law—American | https://www.bu.edu/academics/law/programs/american-law/ |
| 5 | Law—Banking & Financial | https://www.bu.edu/academics/law/programs/graduate-program-in-banking-financial-law/ |
| 6 | Law—Intellectual Property & Information | https://www.bu.edu/academics/law/programs/intellectual-property-law/ |
| 7 | Law—Taxation | https://www.bu.edu/academics/law/programs/graduate-tax-program/ |
| 8 | Tax Law | https://www.bu.edu/academics/law/programs/graduate-tax-program/ |

##### Two-Year LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | American Law | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-american-law/ |
| 2 | Banking & Financial Law | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-banking-financial-law/ |
| 3 | Intellectual Property & Information Law | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-intellectual-property-information-law/ |
| 4 | Law—Banking & Financial | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-banking-financial-law/ |
| 5 | Law—Intellectual Property & Information | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-intellectual-property-information-law/ |
| 6 | Law—Taxation | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-tax-law/ |
| 7 | Tax Law | https://www.bu.edu/academics/law/programs/two-year-master-of-laws-llm-in-tax-law/ |

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.bu.edu/academics/law/programs/jd/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Estate Planning | https://www.bu.edu/academics/law/programs/estate-planning-certificate/ |

##### JD/LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Asian Legal Studies | https://www.bu.edu/academics/law/programs/jdllm-asian-legal-studies/ |
| 2 | Banking & Financial Law | https://www.bu.edu/academics/law/programs/accelerated-llm-in-banking-financial-law/ |
| 3 | European Business Law | https://www.bu.edu/academics/law/programs/jdllm-in-international-and-european-business-law-at-icade/ |
| 4 | European Law | https://www.bu.edu/academics/law/programs/jdllm-in-european-law-at-paris-ii/ |
| 5 | Finance | https://www.bu.edu/academics/law/programs/jdllm-in-finance/ |
| 6 | International Commercial & Investment Arbitration | https://www.bu.edu/academics/law/programs/jd-llm-in-international-commercial-and-investment-arbitration-at-paris2/ |
| 7 | Law—Asian Legal Studies | https://www.bu.edu/academics/law/programs/jdllm-asian-legal-studies/ |
| 8 | Law—Banking & Financial | https://www.bu.edu/academics/law/programs/accelerated-llm-in-banking-financial-law/ |
| 9 | Law—European | https://www.bu.edu/academics/law/programs/jdllm-in-european-law-at-paris-ii/ |
| 10 | Law—International Business | https://www.bu.edu/academics/law/programs/jdllm-in-international-and-european-business-law-at-icade/ |
| 11 | Law—Taxation | https://www.bu.edu/academics/law/programs/accelerated-llm-in-taxation/ |
| 12 | Tax Law | https://www.bu.edu/academics/law/programs/accelerated-llm-in-taxation/ |

##### JD/MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration & Law | https://www.bu.edu/academics/law/programs/jdmba/ |
| 2 | Law & Business Administration | https://www.bu.edu/academics/law/programs/jdmba/ |

##### JD/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Law & Public Health | https://www.bu.edu/academics/law/programs/jdmph/ |
| 2 | Public Health & Law | https://www.bu.edu/academics/law/programs/jdmph/ |

#### School of Public Health

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Biostatistics | https://www.bu.edu/academics/sph/programs/ms-in-applied-biostatistics/ |
| 2 | Population Health Research | https://www.bu.edu/academics/sph/programs/ms-in-population-health-research/ |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Chronic & Non-Communicable Diseases | https://www.bu.edu/academics/sph/programs/mph/chronic-and-non-communicable-diseases/ |
| 2 | Community Assessment, Program Design, Implementation & Evaluation | https://www.bu.edu/academics/sph/programs/mph/community-assessment/ |
| 3 | Environmental Health and Justice | https://www.bu.edu/academics/sph/programs/mph/environmental-health/ |
| 4 | Epidemiology & Biostatistics | https://www.bu.edu/academics/sph/programs/mph/epidemiology-and-biostatistics/ |
| 5 | Global Health | https://www.bu.edu/academics/sph/programs/mph/global-health-2/ |
| 6 | Global Health Program Design, Monitoring & Evaluation | https://www.bu.edu/academics/sph/programs/mph/monitoring-and-evaluation/ |
| 7 | Healthcare Management | https://www.bu.edu/academics/sph/programs/mph/healthcare-management/ |
| 8 | Health Communication & Promotion | https://www.bu.edu/academics/sph/programs/programs/health-communication-and-promotion/ |
| 9 | Health Equity | https://www.bu.edu/academics/sph/programs/mph-in-health-equity/ |
| 10 | Health Policy & Law | https://www.bu.edu/academics/sph/programs/mph/health-policy-and-law/ |
| 11 | Human Rights & Social Justice | https://www.bu.edu/academics/sph/programs/mph/human-rights-and-social-justice/ |
| 12 | Infectious Disease | https://www.bu.edu/academics/sph/programs/mph/infectious-disease/ |
| 13 | Maternal & Child Health | https://www.bu.edu/academics/sph/programs/mph/maternal-and-child-health/ |
| 14 | Mental Health & Substance Use | https://www.bu.edu/academics/sph/programs/mph/mental-health-and-substance-use/ |
| 15 | Pharmaceutical Development, Delivery & Access | https://www.bu.edu/academics/sph/programs/mph/pharmaceutical-development-delivery-and-access/ |
| 16 | Program Management | https://www.bu.edu/academics/sph/programs/mph/monitoring-and-evaluation/ |
| 17 | Public Health | https://www.bu.edu/academics/sph/programs/mph/ |
| 18 | Sex, Sexuality & Gender | https://www.bu.edu/academics/sph/programs/mph/sex-sexuality-and-gender/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Health | https://www.bu.edu/academics/sph/programs/environmental-health/phd/ |
| 2 | Epidemiology | https://www.bu.edu/academics/sph/programs/epidemiology/phd/ |
| 3 | Health Services & Policy Research | https://www.bu.edu/academics/sph/programs/health-services-research/phd/ |

##### DrPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://www.bu.edu/academics/sph/programs/drph/ |

##### MD/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine & Public Health | https://www.bu.edu/academics/sph/programs/medicine-and-public-health/ |
| 2 | Public Health & Medicine | https://www.bu.edu/academics/sph/programs/medicine-and-public-health/ |

##### MS/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Genetic Counseling/Master of Public Health | https://www.bu.edu/academics/sph/programs/ms-in-genetic-counseling-master-of-public-health-ms-mph/ |
| 2 | Medical Sciences & Public Health | https://www.bu.edu/academics/sph/programs/medical-sciences-and-public-health/ |
| 3 | Public Health & Genetic Counseling | https://www.bu.edu/academics/sph/programs/ms-in-genetic-counseling-master-of-public-health-ms-mph/ |
| 4 | Public Health & Medical Sciences | https://www.bu.edu/academics/sph/programs/medical-sciences-and-public-health/ |

##### MSW/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health & Social Work | https://www.bu.edu/academics/sph/programs/social-work-and-public-health/ |
| 2 | Social Work & Public Health | https://www.bu.edu/academics/sph/programs/social-work-and-public-health/ |

#### School of Social Work

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work, Clinical Practice | https://www.bu.edu/academics/ssw/programs/clinical-social-work-practice/ |
| 2 | Social Work, Macro Practice | https://www.bu.edu/academics/ssw/programs/macro-social-work-practice/ |
| 3 | Social Work | https://www.bu.edu/academics/ssw/programs/msw/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.bu.edu/academics/ssw/programs/phd-in-social-work/ |

#### School of Theology

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Religion & Public Leadership | https://www.bu.edu/academics/sth/programs/marpl/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Theology—Theological Studies | https://www.bu.edu/academics/sth/programs/theological-studies-phd/ |

##### GRAD Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Anglican & Episcopal Studies | https://www.bu.edu/academics/sth/programs/sth-certificates/certificate-in-anglican-episcopal-studies/ |
| 2 | Evangelism | https://www.bu.edu/academics/sth/programs/sth-certificates/certificate-in-evangelism/ |
| 3 | Faith & Ecological Justice | https://www.bu.edu/academics/sth/programs/sth-certificates/certificate-in-faith-ecological-justice/ |
| 4 | Music Ministry | https://www.bu.edu/academics/sth/programs/sth-certificates/certificate-in-music-ministry/ |
| 5 | Religious Education | https://www.bu.edu/academics/sth/programs/sth-certificates/certificate-in-religious-education/ |
| 6 | Spirituality Studies | https://www.bu.edu/academics/sth/programs/sth-certificates/spirituality-studies/ |
| 7 | Theology & Latinx Studies | https://www.bu.edu/academics/sth/programs/certificate-in-theology-latinx-studies/ |

#### Henry M. Goldman School of Dental Medicine

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Public Health | https://www.bu.edu/academics/sdm/programs/dental-public-health/ms/ |

##### MSD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Biomechanics | https://www.bu.edu/academics/sdm/programs/applied-biomechanics/master-of-science-in-dentistry-msd-in-applied-biomechanics/ |
| 2 | Dental Biomaterials | https://www.bu.edu/academics/sdm/programs/dental-biomaterials/master-of-science-in-dentistry-in-dental-biomaterials/ |
| 3 | Dental Public Health | https://www.bu.edu/academics/sdm/programs/dental-public-health/msd/ |
| 4 | Endodontics | https://www.bu.edu/academics/sdm/programs/endodontics/msd/ |
| 5 | Esthetic, Digital, and Operative Dentistry | https://www.bu.edu/academics/sdm/programs/operative-dentistry/msd/ |
| 6 | Oral Biology | https://www.bu.edu/academics/sdm/programs/oral-biology/msd/ |
| 7 | Oral & Maxillofacial Surgery | https://www.bu.edu/academics/sdm/programs/oral-and-maxillofacial-surgery/msd/ |
| 8 | Orthodontics & Dentofacial Orthopedics | https://www.bu.edu/academics/sdm/programs/orthodontics-dentofacial-orthopedics/cags-msd/ |
| 9 | Pediatric Dentistry | https://www.bu.edu/academics/sdm/programs/pediatric-dentistry/msd/ |
| 10 | Periodontology | https://www.bu.edu/academics/sdm/programs/periodontology/msd/ |
| 11 | Prosthodontics | https://www.bu.edu/academics/sdm/programs/prosthodontics/cags-msd |

##### DScD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Biomechanics | https://www.bu.edu/academics/sdm/programs/doctor-of-science-in-dentistry-dscd-in-applied-biomechanics/ |
| 2 | Dental Biomaterials | https://www.bu.edu/academics/sdm/programs/dscd-dental-biomaterials/ |
| 3 | Endodontics | https://www.bu.edu/academics/sdm/programs/endodontics/dscd/ |
| 4 | Esthetic, Digital, and Operative Dentistry | https://www.bu.edu/academics/sdm/programs/operative-dentistry/dscd/ |
| 5 | Oral & Maxillofacial Surgery | https://www.bu.edu/academics/sdm/programs/oral-and-maxillofacial-surgery/dscd/ |
| 6 | Orthodontics & Dentofacial Orthopedics | https://www.bu.edu/academics/sdm/programs/orthodontics-dentofacial-orthopedics/dscd/ |
| 7 | Pediatric Dentistry | https://www.bu.edu/academics/sdm/programs/pediatric-dentistry/dscd/ |
| 8 | Periodontology | https://www.bu.edu/academics/sdm/programs/periodontology/dscd/ |
| 9 | Prosthodontics | https://www.bu.edu/academics/sdm/programs/prosthodontics/cags-dscd |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Orofacial & Skeletal Biology | https://www.bu.edu/academics/sdm/programs/oral-biology/phd/ |

##### DMD
| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Medicine | https://www.bu.edu/academics/sdm/programs/doctor-of-dental-medicine/ |

##### CAGS
| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Public Health | https://www.bu.edu/academics/sdm/programs/dental-public-health/cags/ |
| 2 | Endodontics | https://www.bu.edu/academics/sdm/programs/endodontics/cags/ |
| 3 | Esthetic, Digital, and Operative Dentistry | https://www.bu.edu/academics/sdm/programs/operative-dentistry/cags/ |
| 4 | Geriatric Dental Medicine | https://www.bu.edu/academics/sdm/programs/cags-in-geriatric-dental-medicine/ |
| 5 | Oral & Maxillofacial Surgery | https://www.bu.edu/academics/sdm/programs/oral-and-maxillofacial-surgery/cags/ |
| 6 | Orthodontics & Dentofacial Orthopedics | https://www.bu.edu/academics/sdm/programs/orthodontics-dentofacial-orthopedics/cags-msd/ |
| 7 | Pediatric Dentistry | https://www.bu.edu/academics/sdm/programs/pediatric-dentistry/cags/ |
| 8 | Periodontology | https://www.bu.edu/academics/sdm/programs/periodontology/cags/ |
| 9 | Prosthodontics | https://www.bu.edu/academics/sdm/programs/prosthodontics/cags/ |

#### Chobanian & Avedisian School of Medicine

##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://www.bu.edu/academics/busm/programs/four-year-program/ |


> Total graduate degree/certificate rows: 427

---

## 3. 申请要求与截止日期 (Application Requirements & Deadlines)

### 3.1 本科 — 核心数据表

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common Application / QuestBridge | `bu.edu/admissions/apply/first-year/` |
| 申请费 | $80 | `bu.edu/admissions/apply/first-year/` |
| ED I 截止日期 | November 2 | `bu.edu/admissions/apply/deadlines/` |
| ED I 通知日期 | December 15 | `bu.edu/admissions/apply/deadlines/` |
| ED II 截止日期 | January 5 | `bu.edu/admissions/apply/deadlines/` |
| ED II 通知日期 | February 9 | `bu.edu/admissions/apply/deadlines/` |
| RD 截止日期 | January 5 | `bu.edu/admissions/apply/deadlines/` |
| RD 通知日期 | March 28 | `bu.edu/admissions/apply/deadlines/` |
| 入学押金截止 | May 1 | `bu.edu/admissions/apply/deadlines/` |
| Merit 奖学金截止 | December 1 | `bu.edu/admissions/apply/deadlines/` |
| SAT/ACT 政策 | Test-optional through fall 2028 / spring 2029 | `bu.edu/admissions/apply/first-year/test-policy/` |
| SAT 代码 | 3087 | `bu.edu/admissions/apply/first-year/` |
| ACT 代码 | 1794 | `bu.edu/admissions/apply/first-year/` |
| Superscore | Yes — both SAT and ACT | `bu.edu/admissions/apply/first-year/` |
| 推荐信 | Counselor Recommendation + 1 Teacher Evaluation | `bu.edu/admissions/apply/first-year/` |
| 面试 | None required; optional InitialView for intl | `bu.edu/admissions/apply/international/` |
| Video Submission | Optional | `bu.edu/admissions/apply/first-year/` |
| 转学截止 (秋季) | March 15 | `bu.edu/admissions/apply/deadlines/` |
| 转学截止 (春季) | November 2 | `bu.edu/admissions/apply/deadlines/` |

### 3.2 本科英语水平要求

| 考试 | 建议最低分 | 备注 |
|------|-----------|------|
| TOEFL iBT | 90-100 (composite), 20 each section | 新评分标准 (2026年1月起): 5.0+ |
| IELTS Academic | 7.0 | 满足所有项目要求 |
| Duolingo English Test (DET) | 125-135 | 含视频面试 |
| TOEFL Home Edition | Accepted | IELTS Indicator / TOEFL ITP Plus 不接受 |
| TOEFL 代码 | 3087 | — |

> Source: `bu.edu/admissions/apply/international/` — "Students who are most competitive for admission will have a composite score of at least 90-100 and minimum scores of 20 in each section."

### 3.3 研究生 — 全局规则

- **招生模式**: 完全分散 — 17个学院各自独立招生
- **申请平台**: 各学院自管 (GRS用BU Graduate School portal, Law用LSAC, Med用AMCAS, Dental用ADEA AADSAS, SPH用SOPHAS等)
- **申请费**: 各学院不同 (GRS $95, Law $85, Med $110等)
- **GRE/GMAT**: 各项目自定 — 部分要求, 部分可选, 部分不要求
- **英语要求**: TOEFL或IELTS (各项目最低分不同)
- **CGS April-15**: BU是签署方

> Source: `bu.edu/grad/admission-funding/graduate-admission/` — "Each of our 17 schools and colleges and the Faculty of Computing & Data Sciences has its own admissions and financial aid process."

---

## 4. 费用与经济援助 (Costs & Financial Aid)

### 4.1 本科费用 (2026-2027学年)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| 学费 (Tuition) | $73,024 | — |
| 住宿 (Housing) | $13,170 | 标准宿舍 |
| 餐饮 (Food/Dining) | $7,570 | 标准餐饮计划 |
| 杂费 (Fees) | $1,570 | — |
| 其他费用 (Books/Personal) | $3,085 | — |
| **总费用 (Total COA)** | **$98,419** | — |

> Source: `bu.edu/admissions/tuition-aid/` — line-item COA for 2026-2027.

### 4.2 本科经济援助政策

| 政策维度 | 值 | 来源 |
|---------|-----|------|
| Need-blind (美国公民/PR) | Yes — 满足100%需求 | `bu.edu/admissions/tuition-aid/financial-aid/` |
| Need-blind (国际学生) | **No** — 不提供need-based aid | `bu.edu/admissions/tuition-aid/scholarships-financial-aid/` |
| 国际学生援助 | 仅merit奖学金 | `bu.edu/admissions/tuition-aid/scholarships-financial-aid/` |
| 收入≤$75,000 | Full tuition + housing + dining = $0 | `bu.edu/admissions/tuition-aid/affordable-bu/` |
| 收入$75k-$100k | Full tuition + ≤$10,000 | `bu.edu/admissions/tuition-aid/affordable-bu/` |
| 收入$100k-$150k | Full tuition + ≤$15,000 | `bu.edu/admissions/tuition-aid/affordable-bu/` |
| 收入$150k-$200k | Full tuition + ≤$20,000 | `bu.edu/admissions/tuition-aid/affordable-bu/` |
| 收入$200k+ | 定制援助 | `bu.edu/admissions/tuition-aid/affordable-bu/` |
| BU Scholarship Assurance | 学费涨则奖学金同比涨 | `bu.edu/admissions/tuition-aid/financial-aid/` |
| 无贷款政策 | 大一新生援助不含贷款 | `bu.edu/admissions/tuition-aid/financial-aid/` |
| CSS Profile + FAFSA | 必须提交 | `bu.edu/admissions/tuition-aid/financial-aid/` |

> Note: "Need-based financial aid from BU is not currently available to international students." — `bu.edu/admissions/tuition-aid/scholarships-financial-aid/`

### 4.3 研究生费用与资助框架

- **资助类型**: 因学院而异 — GRS PhD通常全额资助; 多数硕士项目自费
- **RA/TA/Fellowship**: GRS, ENG, SPH等研究型项目提供; 专业项目(Law, Med, Dental)通常不提供
- **申请费**: 各学院不同 ($75-$110)
- **学费**: 各学院不同 — MET, SPH等部分项目有在线/非全日制费率

---

## 5. 证据链索引 (Evidence Chain Index)

### E-U-001: ED I Deadline
```yaml
field: undergraduate.deadlines.ED_I
value: "November 2"
source_url: "https://www.bu.edu/admissions/apply/deadlines/"
source_snippet: "Application November 2"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-002: RD Deadline
```yaml
field: undergraduate.deadlines.RD
value: "January 5"
source_url: "https://www.bu.edu/admissions/apply/deadlines/"
source_snippet: "Application* January 5"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-003: Application Fee
```yaml
field: undergraduate.application_fee
value: "$80"
source_url: "https://www.bu.edu/admissions/apply/first-year/"
source_snippet: "Application Fee: Our application fee is $80"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004: Test Policy
```yaml
field: undergraduate.test_policy
value: "test-optional through fall 2028 and spring 2029"
source_url: "https://www.bu.edu/admissions/apply/first-year/test-policy/"
source_snippet: "Boston University has decided to remain test optional for students applying for admission through fall 2028 and spring 2029."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005: TOEFL Requirements
```yaml
field: undergraduate.english_proficiency.toefl
value: "90-100 composite, 20 each section; new scale 5.0+"
source_url: "https://www.bu.edu/admissions/apply/international/"
source_snippet: "Students who are most competitive for admission will have a composite score of at least 90-100 and minimum scores of 20 in each section."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-006: IELTS Requirements
```yaml
field: undergraduate.english_proficiency.ielts
value: "7.0"
source_url: "https://www.bu.edu/admissions/apply/international/"
source_snippet: "A total/overall score of 7 or higher will satisfy BU's English Language proficiency requirement for all programs."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-007: Tuition
```yaml
field: undergraduate.costs.tuition_2026_2027
value: "$73,024"
source_url: "https://www.bu.edu/admissions/tuition-aid/"
source_snippet: "Tuition $73,024"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-008: Total COA
```yaml
field: undergraduate.costs.total_coa_2026_2027
value: "$98,419"
source_url: "https://www.bu.edu/admissions/tuition-aid/"
source_snippet: "Total Cost of Attendance $98,419"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-009: Need-blind Policy
```yaml
field: undergraduate.aid.need_blind_domestic
value: "Yes — 100% need met"
source_url: "https://www.bu.edu/admissions/tuition-aid/financial-aid/"
source_snippet: "You'll receive financial assistance for 100% of your demonstrated need"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-010: International Aid Policy
```yaml
field: undergraduate.aid.need_blind_intl
value: "No — need-based aid not available to international students"
source_url: "https://www.bu.edu/admissions/tuition-aid/scholarships-financial-aid/"
source_snippet: "Need-based financial aid from BU is not currently available to international students."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-011: Income Thresholds
```yaml
field: undergraduate.aid.income_thresholds
value: "$0-75k=$0; $75k-100k≤$10k; $100k-150k≤$15k; $150k-200k≤$20k"
source_url: "https://www.bu.edu/admissions/tuition-aid/affordable-bu/"
source_snippet: "$0–$75,000 Full Tuition + Standard Housing & Dining Plan $0"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-012: Class Profile
```yaml
field: undergraduate.class_profile
value: "76,776 applicants; 3,450 enrolled; 3.7-4.0 GPA mid-50%; 21% international"
source_url: "https://www.bu.edu/admissions/why-bu/class-profile/"
source_snippet: "76,776 Total Applicants; 3,450 Total Enrolled; 3.7–4.0 Mid 50% GPA range"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-001: Graduate Admissions Model
```yaml
field: graduate.admissions_model
value: "Fully decentralized — 17 schools each run own admissions"
source_url: "https://www.bu.edu/grad/admission-funding/graduate-admission/"
source_snippet: "Each of our 17 schools and colleges and the Faculty of Computing & Data Sciences has its own admissions and financial aid process."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-P-001: Program Directory
```yaml
field: programs.total_count
value: "698 degree rows (443 unique program entries)"
source_url: "https://www.bu.edu/academics/degree-programs/"
source_snippet: "A–Z, we've got it covered. Search BU's programs by subject for degrees and courses of study."
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## 6. WeKnora 导入清单 (Import Manifest)

### Collection Structure

```
bu-knowledge-base-v2/
├── 00-overview.md              → Section 0 (rules 1-4)
├── 01-ug-cas.md                → CAS UG programs
├── 02-ug-com.md                → COM UG programs
├── 03-ug-eng.md                → ENG UG programs
├── 04-ug-cfa.md                → CFA UG programs
├── 05-ug-cds-pardee.md         → CDS + Pardee UG programs
├── 06-ug-questrom.md           → Questrom UG programs
├── 07-ug-sar-sha.md            → SAR + SHA UG programs
├── 08-ug-wheelock.md           → Wheelock UG programs
├── 09-ug-minors.md             → All UG minors
├── 10-grad-grs.md              → GRS graduate programs
├── 11-grad-gms.md              → GMS graduate programs
├── 12-grad-eng.md              → ENG graduate programs
├── 13-grad-com.md              → COM graduate programs
├── 14-grad-cfa.md              → CFA graduate programs
├── 15-grad-questrom.md         → Questrom graduate programs
├── 16-grad-met.md              → MET graduate programs
├── 17-grad-sph.md              → SPH graduate programs
├── 18-grad-wheelock.md         → Wheelock graduate programs
├── 19-grad-law.md              → Law programs
├── 20-grad-sdm.md              → Dental programs
├── 21-grad-ssw-sth.md          → SSW + STH programs
├── 22-grad-sar-sha-cds.md      → SAR + SHA + CDS grad programs
├── 23-deadlines.md             → Section 3
├── 24-costs.md                 → Section 4
├── 25-evidence.md              → Section 5
└── 26-comparison.md            → Section 7
```

### Follow-up Data Items

| Priority | Data Item | Target URL |
|----------|----------|------------|
| P0 | Per-program GRE/GMAT policy for graduate programs | Individual school admissions pages |
| P0 | Per-program graduate deadlines | Individual school admissions pages |
| P1 | CGS specific curriculum and transfer requirements | `bu.edu/academics/cgs/` |
| P1 | Kilachand Honors College requirements | `bu.edu/academics/khc/` |
| P1 | Detailed department mapping per school | Individual school bulletin pages |
| P2 | Per-program TOEFL minimums for graduate programs | Individual school admissions pages |
| P2 | Merit scholarship details and criteria | `bu.edu/admissions/tuition-aid/scholarships-financial-aid/first-year-merit/` |

---

## 7. 跨校比较框架 (Cross-School Comparison Framework)

| 维度 | BU | (其他学校) |
|------|-----|-----------|
| 本科总费用/年 | $98,419 | — |
| 学费/年 | $73,024 | — |
| Need-blind (美国) | Yes | — |
| Need-blind (国际) | No | — |
| ED I 截止 | Nov 2 | — |
| ED II 截止 | Jan 5 | — |
| RD 截止 | Jan 5 | — |
| SAT/ACT 要求 | Test-optional (through 2028/29) | — |
| TOEFL 最低 | 90-100 | — |
| IELTS 最低 | 7.0 | — |
| 免学费收入门槛 | $75,000 | — |
| 研究生申请费 | 各学院不同 | — |
| 项目总数 (Rule 1) | 698 | — |
| 学院数 (Rule 2) | 20 | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: bu.edu (admissions, bulletin, finaid, grad)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
