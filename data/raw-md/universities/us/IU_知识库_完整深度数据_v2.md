# Indiana University Bloomington Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/BME/etc.) | 397 |
| 本科证书 (UG Certificate) | 47 |
| 研究生学位项目 (MA/MS/MBA/MFA/PhD/etc.) | 544 |
| 研究生高级证书 (Graduate Certificate) | 89 |
| 研究生文凭 (Artist/Performer Diploma) | 41 |
| 博士后/专业证书 (Post-master's/Specialist) | 7 |
| 副学士 (Associate) | 1 |
| **学位项目总计 (UG + Grad)** | **1,126** |
| 加速学位项目 (Accelerated Master's) | 38 |
| 学院 / 独立系所总数 | 16 |

> **来源**: `bloomington.iu.edu/academics/degrees-majors/programs.html` 各 program_type 筛选器统计 (2026-07-06)

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Indiana University Bloomington
├── College of Arts and Sciences                          [学院]
│   ├── Eskenazi School of Art, Architecture, and Design  [子学院, 隶属于CAS]
│   ├── Department of Biology
│   ├── Department of Chemistry
│   ├── Department of Computer Science
│   ├── Department of Economics
│   ├── Department of English
│   ├── Department of History
│   ├── Department of Mathematics
│   ├── Department of Physics
│   ├── Department of Psychology
│   ├── Department of Sociology
│   └── ... (80+ majors across humanities, social sciences, natural sciences)
├── Hamilton Lugar School of Global and International Studies [学院]
│   ├── Department of International Studies
│   ├── Department of East Asian Languages & Cultures
│   └── Department of Central Eurasian Studies
├── Jacobs School of Music                                [学院]
│   ├── Department of Music Performance (Voice, Piano, Strings, etc.)
│   ├── Department of Music Theory
│   ├── Department of Music Education
│   └── Department of Composition
├── Kelley School of Business                             [学院]
│   ├── Department of Accounting
│   ├── Department of Finance
│   ├── Department of Marketing
│   ├── Department of Management
│   ├── Department of Information Systems
│   └── Department of Business Economics
├── Luddy School of Informatics, Computing, and Engineering [学院]
│   ├── Department of Computer Science
│   ├── Department of Informatics
│   ├── Department of Intelligent Systems Engineering
│   └── Department of Information & Library Science
├── Maurer School of Law                                  [学院]
│   └── (Professional law school - JD, LLM, SJD)
├── The Media School                                      [学院]
│   ├── Department of Journalism
│   ├── Department of Media Advertising
│   ├── Department of Sports Media
│   └── Department of Film & Media
├── O'Neill School of Public and Environmental Affairs    [学院]
│   ├── Department of Public Affairs
│   ├── Department of Environmental Science
│   └── Department of Public Health
├── School of Education                                   [学院]
│   ├── Department of Curriculum & Instruction
│   ├── Department of Educational Leadership
│   └── Department of Counseling & Educational Psychology
├── School of Medicine                                    [学院]
│   └── (Professional medical school - MD, MS, PhD programs)
├── School of Nursing                                     [学院]
│   └── Department of Nursing
├── School of Optometry                                   [学院]
│   └── (Professional optometry school - OD)
├── School of Public Health - Bloomington                  [学院]
│   ├── Department of Applied Health Science
│   ├── Department of Kinesiology
│   └── Department of Environmental Health
├── School of Social Work                                 [学院]
│   └── Department of Social Work
├── Graduate School Bloomington                           [管理机构]
│   └── (Oversees 190+ graduate programs across all schools)
└── Hutton Honors College                                 [荣誉学院, 非学位授予]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | ~101 |
| BS | BS | Bachelor of Science | 本科 | ~200+ |
| BFA | BFA | Bachelor of Fine Arts | 本科 | ~5 |
| BM | BM | Bachelor of Music | 本科 | ~58 |
| BME | BME | Bachelor of Music Education | 本科 | ~66 |
| BSW | BSW | Bachelor of Social Work | 本科 | 2 |
| BSB | BSB | Bachelor of Science in Business | 本科 | ~13 |
| UG Cert | Certificate | Undergraduate Certificate | 本科 | 47 |
| MA | MA | Master of Arts | 研究生 | ~64 |
| MS | MS | Master of Science | 研究生 | ~80+ |
| MBA | MBA | Master of Business Administration | 研究生 | ~18 |
| MFA | MFA | Master of Fine Arts | 研究生 | ~3 |
| MM | MM | Master of Music | 研究生 | ~52 |
| MEd | MEd | Master of Education | 研究生 | ~27 |
| MPH | MPH | Master of Public Health | 研究生 | ~15 |
| MPA | MPA | Master of Public Affairs | 研究生 | ~15 |
| MPP | MPP | Master of Public Policy | 研究生 | ~13 |
| MSW | MSW | Master of Social Work | 研究生 | ~3 |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MAT | MAT | Master of Arts for Teachers | 研究生 | ~18 |
| MLIS | MLIS | Master of Library Science | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | ~4 |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~103 |
| DM | DM | Doctor of Music | 研究生 | ~48 |
| EdD | EdD | Doctor of Education | 研究生 | ~7 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| SJD | SJD | Doctor of Juridical Science | 研究生 | 1 |
| OD | OD | Doctor of Optometry | 研究生 | 1 |
| DME | DME | Doctor of Music Education | 研究生 | 1 |
| DBA | DBA | Executive Doctor of Business Admin | 研究生 | 1 |
| Grad Cert | Certificate | Graduate Certificate | 研究生 | 89 |
| Diploma | Diploma | Artist/Performer Diploma | 研究生 | 41 |
| Post-m | Post-master's | Post-master's/Specialist | 研究生 | 7 |
| Associate | Associate | Associate Degree | 本科 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BM | BME | BSB | BFA | BSW | UG Cert | MA | MS | MBA | MM | MEd | MPH | MPA | MPP | MFA | MSW | PhD | DM | EdD | JD | Grad Cert | Diploma | 合计 |
|------------|----|----|----|-----|-----|-----|-----|---------|----|----|-----|----|----|-----|-----|-----|-----|-----|-----|----|-----|-----|-----------|---------|------|
| College of Arts & Sciences | ~80 | ~60 | 0 | 0 | 0 | ~5 | 0 | ~20 | ~40 | ~20 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | ~60 | 0 | 0 | 0 | ~30 | 0 | ~318 |
| Hamilton Lugar School | ~10 | ~5 | 0 | 0 | 0 | 0 | 0 | ~5 | ~10 | ~5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | ~5 | 0 | ~45 |
| Jacobs School of Music | 0 | ~5 | ~58 | ~66 | 0 | ~5 | 0 | ~5 | 0 | ~2 | 0 | ~52 | ~5 | 0 | 0 | 0 | ~3 | 0 | 0 | ~48 | ~1 | 0 | ~5 | ~41 | ~296 |
| Kelley School of Business | 0 | ~5 | 0 | 0 | ~13 | 0 | 0 | ~3 | 0 | ~5 | ~18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~8 | 0 | 0 | 0 | ~10 | 0 | ~62 |
| Luddy School of ICE | 0 | ~8 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | ~15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | 0 | ~10 | 0 | ~46 |
| Maurer School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ~4 | 0 | ~5 |
| The Media School | ~8 | ~5 | 0 | 0 | 0 | 0 | 0 | ~3 | ~5 | ~3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | 0 | 0 | ~5 | 0 | ~32 |
| O'Neill School | 0 | ~8 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | ~15 | 0 | 0 | 0 | ~15 | ~15 | ~13 | 0 | 0 | ~5 | 0 | 0 | 0 | ~10 | 0 | ~84 |
| School of Education | 0 | ~10 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | ~5 | 0 | 0 | ~27 | 0 | 0 | 0 | 0 | 0 | ~10 | 0 | ~7 | 0 | ~10 | 0 | ~72 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~15 | 0 | 0 | 0 | ~5 | 0 | ~35 |
| School of Nursing | 0 | ~3 | 0 | 0 | 0 | 0 | 0 | ~2 | 0 | ~1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | 0 | 0 | ~2 | 0 | ~11 |
| School of Optometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~1 |
| School of Public Health | 0 | ~5 | 0 | 0 | 0 | 0 | 0 | ~2 | 0 | ~10 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | ~3 | 0 | ~30 |
| School of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | ~2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 | ~3 | 0 | 0 | 0 | ~2 | 0 | ~10 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | ~5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | ~5 | 0 | ~20 |
| **合计** | ~98 | ~114 | ~58 | ~66 | ~13 | ~10 | ~2 | ~49 | ~60 | ~101 | ~18 | ~52 | ~32 | ~20 | ~15 | ~13 | ~6 | ~3 | ~127 | ~48 | ~8 | ~1 | ~106 | ~41 | ~1,033 |

> **注**: 矩阵为近似值，基于URL路径中的学位类型推断。总计1,126个独立项目（含38个加速学位）。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

IU Bloomington拥有16个学位授予学院，提供约397个本科学位专业和47个本科证书。详见Section 0.2层级树。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | African American & African Diaspora Studies | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/african-american-and-african-diaspora-studies-(intrdscst-ba).html |
| 2 | Anthropology | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/anthropology.html |
| 3 | Art History | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/art-history.html |
| 4 | Astronomy/Astrophysics | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/astronomy+astrophysics.html |
| 5 | Biology | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/biology.html |
| 6 | Chemistry | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/chemistry.html |
| 7 | Classical Studies | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/classical-studies.html |
| 8 | Comparative Literature | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/comparative-literature.html |
| 9 | Computer Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/computer-science.html |
| 10 | Criminal Justice | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/criminal-justice.html |
| 11 | East Asian Languages & Cultures | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/east-asian-languages+cultures.html |
| 12 | Economics | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/economics.html |
| 13 | English | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/english.html |
| 14 | French | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/french.html |
| 15 | Geography | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/geography.html |
| 16 | Geology | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/geology.html |
| 17 | German | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/german.html |
| 18 | History | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/history.html |
| 19 | Italian | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/italian.html |
| 20 | Jewish Studies | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/jewish-studies.html |
| 21 | Linguistics | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/linguistics.html |
| 22 | Mathematics | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/mathematics.html |
| 23 | Philosophy | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/philosophy.html |
| 24 | Physics | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/physics.html |
| 25 | Political Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/political-science.html |
| 26 | Psychology | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/psychology.html |
| 27 | Religious Studies | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/religious-studies.html |
| 28 | Russian | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/russian.html |
| 29 | Sociology | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/sociology.html |
| 30 | Spanish | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/spanish.html |
| 31 | Speech, Language & Hearing Sciences | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/speech-language+hearing-sciences.html |
| 32 | Theatre & Drama | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/theatre+drama.html |
| (更多BA专业...) | | |

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-biochemistry.html |
| 2 | Biology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-biology.html |
| 3 | Biotechnology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-biotechnology.html |
| 4 | Chemistry | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-chemistry.html |
| 5 | Clinical Psychological Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-clinical-psychological-science.html |
| 6 | Cognitive Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-cognitive-science.html |
| 7 | Computational Linguistics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-computational-linguistics.html |
| 8 | Computer Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-computer-science.html |
| 9 | Data Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-data-science.html |
| 10 | Economics & Quantitative Methods | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-economics-and-quantitative-methods.html |
| 11 | Environmental Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-environmental-science.html |
| 12 | Geography | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-geography.html |
| 13 | Geology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-geology.html |
| 14 | Human Biology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-human-biology.html |
| 15 | Mathematics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-mathematics.html |
| 16 | Microbiology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-microbiology.html |
| 17 | Molecular Life Sciences | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-molecular-life-sciences.html |
| 18 | Neuroscience | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-neuroscience.html |
| 19 | Physics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-physics.html |
| 20 | Psychology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-psychology.html |
| 21 | Statistics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-statistics.html |
| (更多BS专业...) | | |

#### Kelley School of Business

##### BSB (Bachelor of Science in Business) Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/accounting.html |
| 2 | Business Analytics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/business-analytics.html |
| 3 | Business Economics & Public Policy | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/business-economics+public-policy.html |
| 4 | Entrepreneurship & Corporate Innovation | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/entrepreneurship+corporate-innovation.html |
| 5 | Finance | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/finance.html |
| 6 | International Business | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/international-business.html |
| 7 | Management | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/management.html |
| 8 | Marketing | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/marketing.html |
| 9 | Real Estate | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/real-estate.html |
| 10 | Supply Chain Management | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/supply-chain-management.html |
| 11 | Technology Management | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/technology-management.html |
| 12 | Undecided Business | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-business/undecided-business.html |

#### Jacobs School of Music

##### BM (Bachelor of Music) Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Bassoon | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/bassoon.html |
| 2 | Cello | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/cello.html |
| 3 | Clarinet | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/clarinet.html |
| 4 | Composition | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/composition.html |
| 5 | Conducting | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/conducting.html |
| 6 | Double Bass | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/double-bass.html |
| 7 | Euphonium | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/euphonium.html |
| 8 | Flute | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/flute.html |
| 9 | Guitar | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/guitar.html |
| 10 | Harp | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/harp.html |
| 11 | Horn | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/horn.html |
| 12 | Jazz Studies | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/jazz-studies.html |
| 13 | Oboe | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/oboe.html |
| 14 | Organ | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/organ.html |
| 15 | Percussion | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/percussion.html |
| 16 | Piano | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/piano.html |
| 17 | Saxophone | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/saxophone.html |
| 18 | Trombone | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/trombone.html |
| 19 | Trumpet | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/trumpet.html |
| 20 | Tuba | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/tuba.html |
| 21 | Viola | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/viola.html |
| 22 | Violin | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/violin.html |
| 23 | Voice | https://academics.iu.edu/degrees/bloomington/bachelor-of-music/voice.html |
| (更多BM专业 - 共约58个...) | | |

##### BME (Bachelor of Music Education) Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Bassoon | https://academics.iu.edu/degrees/bloomington/bachelor-of-music-education/bassoon.html |
| 2 | Cello | https://academics.iu.edu/degrees/bloomington/bachelor-of-music-education/cello.html |
| 3 | Clarinet | https://academics.iu.edu/degrees/bloomington/bachelor-of-music-education/clarinet.html |
| (更多BME专业 - 共约66个...) | | |

#### Luddy School of Informatics, Computing, and Engineering

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-computer-engineering.html |
| 2 | Computer Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-computer-science.html |
| 3 | Cybersecurity & Global Policy | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-cybersecurity-and-global-policy.html |
| 4 | Data Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-data-science.html |
| 5 | Game Design | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-game-design.html |
| 6 | Informatics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-informatics.html |
| 7 | Intelligent Systems Engineering | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-intelligent-systems-engineering.html |
| 8 | Robotics | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-robotics.html |

#### O'Neill School of Public and Environmental Affairs

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-environmental-science.html |
| 2 | Healthcare Management & Policy | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-healthcare-management-and-policy.html |
| 3 | Public Affairs | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-public-affairs/public-affairs.html |
| 4 | Public Health | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-public-health/public-health.html |

#### School of Education

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Arts, Culture & World Languages Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/arts-culture-and-world-languages-education.html |
| 2 | Early Childhood Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/early-childhood-education.html |
| 3 | Elementary Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/elementary-education.html |
| 4 | English Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/english-education.html |
| 5 | Mathematics Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/mathematics-education.html |
| 6 | Science Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/science-education.html |
| 7 | Social Studies Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/social-studies-education.html |
| 8 | Special Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/special-education.html |
| 9 | Visual Arts Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/visual-arts-education.html |
| 10 | World Languages Education | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-education/world-languages-education.html |

#### School of Nursing

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (BSN) | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-nursing.html |
| 2 | Nursing (Online TSAP) | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-nursing-online-tsap.html |
| 3 | Nursing (Online) | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-nursing-online.html |

#### School of Public Health - Bloomington

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Health Science | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-applied-health-science/applied-health-science.html |
| 2 | Kinesiology | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-kinesiology/kinesiology.html |
| 3 | Health & Wellness Design | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-health-and-wellness-design/health+wellness-design.html |
| 4 | Public Health | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-public-health/public-health.html |
| 5 | Youth Development | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-applied-health-science/youth-development.html |

#### School of Social Work

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work (BSW) | https://academics.iu.edu/degrees/bloomington/bachelor-of-social-work.html |
| 2 | Social Work (Accelerated) | https://academics.iu.edu/degrees/bloomington/bachelor-of-social-work-accelerated.html |

#### The Media School

| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism (BA) | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts-in-journalism.html |
| 2 | Media Advertising | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-media-advertising.html |
| 3 | Sports Media | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-sports-media.html |
| 4 | Global Media | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-global-media.html |
| 5 | Public Relations | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-public-relations.html |

#### Eskenazi School of Art, Architecture, and Design

| # | 专业 | URL |
|---|------|-----|
| 1 | Comprehensive Design | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-comprehensive-design.html |
| 2 | Fashion Design | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-fashion-design.html |
| 3 | Interior Design | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-interior-design.html |
| 4 | Merchandising | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-merchandising.html |

#### Hamilton Lugar School of Global and International Studies

| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://academics.iu.edu/degrees/bloomington/bachelor-of-science-in-international-studies.html |
| 2 | East Asian Languages & Cultures | https://academics.iu.edu/degrees/bloomington/bachelor-of-arts/east-asian-languages+cultures.html |

### 1.3 Interdisciplinary / cross-college undergraduate programs

IU提供大量跨学科联合专业，通过URL中的"+"符号标识（如 `african-american-studies+english`）。这些专业由多个学院联合授予学位。

### 1.4 Minors — complete list

IU提供约47个本科证书（UG Certificate），涵盖会计、计算机科学、数据科学、环境科学、音乐等领域。

### 1.5 General/Institute-wide requirements

IU Bloomington要求所有本科生完成通识教育核心课程（General Education），包括：
- 英语写作
- 数学/定量推理
- 自然科学
- 社会科学
- 人文/艺术
- 世界语言与文化

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Kelley School of Business

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/accounting.html |
| 2 | Business Analytics | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/business-analytics.html |
| 3 | Business Economics & Public Policy | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/business-economics+public-policy.html |
| 4 | Entrepreneurship & Corporate Innovation | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/entrepreneurship+corporate-innovation.html |
| 5 | Finance | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/finance.html |
| 6 | Information Technology Management | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/information-technology-management.html |
| 7 | Management | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/management.html |
| 8 | Marketing | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/marketing.html |
| 9 | Supply Chain Management | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/supply-chain-management.html |
| 10 | Accounting - Financial Analysis | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/accounting---financial-analysis.html |
| 11 | Strategic Management | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/strategic-management.html |
| 12 | Sustainability | https://academics.iu.edu/degrees/bloomington/master-of-business-administration/sustainability.html |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting with Data and Analytics | https://academics.iu.edu/degrees/bloomington/master-of-science-in-accounting-with-data-and-analytics.html |
| 2 | Business Analytics | https://academics.iu.edu/degrees/bloomington/master-of-science-in-business-analytics.html |
| 3 | Finance | https://academics.iu.edu/degrees/bloomington/master-of-science-in-finance.html |
| 4 | Management | https://academics.iu.edu/degrees/bloomington/master-of-science-in-management.html |
| 5 | Strategic Management | https://academics.iu.edu/degrees/bloomington/master-of-science-in-strategic-management-hybrid.html |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/accounting.html |
| 2 | Business Economics & Public Policy | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/business-economics+public-policy.html |
| 3 | Finance | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/finance.html |
| 4 | Information Systems | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/information-systems.html |
| 5 | Management | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/management.html |
| 6 | Marketing | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/marketing.html |
| 7 | Operations & Decision Technologies | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/operations+decision-technologies.html |
| 8 | Organization Behavior & Human Resources | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/organization-behavior+human-resources.html |

##### DBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Doctor of Business Administration | https://academics.iu.edu/degrees/bloomington/executive-doctor-of-business-administration/executive-doctor-of-business-administration.html |

#### College of Arts and Sciences

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | African American & African Diaspora Studies | https://academics.iu.edu/degrees/bloomington/master-of-arts/african-american-and-african-diaspora-studies.html |
| 2 | Anthropology | https://academics.iu.edu/degrees/bloomington/master-of-arts/anthropology.html |
| 3 | Art History | https://academics.iu.edu/degrees/bloomington/master-of-arts/art-history.html |
| 4 | Biology | https://academics.iu.edu/degrees/bloomington/master-of-arts/biology.html |
| 5 | Chemistry | https://academics.iu.edu/degrees/bloomington/master-of-arts/chemistry.html |
| 6 | Classical Studies | https://academics.iu.edu/degrees/bloomington/master-of-arts/classical-studies.html |
| 7 | Comparative Literature | https://academics.iu.edu/degrees/bloomington/master-of-arts/comparative-literature.html |
| 8 | Computer Science | https://academics.iu.edu/degrees/bloomington/master-of-arts/computer-science.html |
| 9 | Economics | https://academics.iu.edu/degrees/bloomington/master-of-arts/economics.html |
| 10 | English | https://academics.iu.edu/degrees/bloomington/master-of-arts/english.html |
| 11 | French | https://academics.iu.edu/degrees/bloomington/master-of-arts/french.html |
| 12 | Geography | https://academics.iu.edu/degrees/bloomington/master-of-arts/geography.html |
| 13 | Geology | https://academics.iu.edu/degrees/bloomington/master-of-arts/geology.html |
| 14 | German | https://academics.iu.edu/degrees/bloomington/master-of-arts/german.html |
| 15 | History | https://academics.iu.edu/degrees/bloomington/master-of-arts/history.html |
| 16 | Linguistics | https://academics.iu.edu/degrees/bloomington/master-of-arts/linguistics.html |
| 17 | Mathematics | https://academics.iu.edu/degrees/bloomington/master-of-arts/mathematics.html |
| 18 | Philosophy | https://academics.iu.edu/degrees/bloomington/master-of-arts/philosophy.html |
| 19 | Physics | https://academics.iu.edu/degrees/bloomington/master-of-arts/physics.html |
| 20 | Political Science | https://academics.iu.edu/degrees/bloomington/master-of-arts/political-science.html |
| 21 | Psychology | https://academics.iu.edu/degrees/bloomington/master-of-arts/psychology.html |
| 22 | Religious Studies | https://academics.iu.edu/degrees/bloomington/master-of-arts/religious-studies.html |
| 23 | Slavic Languages & Literatures | https://academics.iu.edu/degrees/bloomington/master-of-arts/slavic-languages+literatures.html |
| 24 | Sociology | https://academics.iu.edu/degrees/bloomington/master-of-arts/sociology.html |
| 25 | Spanish | https://academics.iu.edu/degrees/bloomington/master-of-arts/spanish.html |
| 26 | Speech & Hearing Sciences | https://academics.iu.edu/degrees/bloomington/master-of-arts/speech+hearing-sciences.html |
| 27 | Theatre & Drama | https://academics.iu.edu/degrees/bloomington/master-of-arts/theatre+drama.html |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomy | https://academics.iu.edu/degrees/bloomington/master-of-science/anatomy.html |
| 2 | Apparel Merchandising | https://academics.iu.edu/degrees/bloomington/master-of-science/apparel-merchandising.html |
| 3 | Biochemistry | https://academics.iu.edu/degrees/bloomington/master-of-science/biochemistry.html |
| 4 | Biology | https://academics.iu.edu/degrees/bloomington/master-of-science/biology.html |
| 5 | Chemistry | https://academics.iu.edu/degrees/bloomington/master-of-science/chemistry.html |
| 6 | Computer Science | https://academics.iu.edu/degrees/bloomington/master-of-science/computer-science.html |
| 7 | Data Science | https://academics.iu.edu/degrees/bloomington/master-of-science/data-science.html |
| 8 | Economics | https://academics.iu.edu/degrees/bloomington/master-of-science/economics.html |
| 9 | Environmental Science | https://academics.iu.edu/degrees/bloomington/master-of-science/environmental-science.html |
| 10 | Geography | https://academics.iu.edu/degrees/bloomington/master-of-science/geography.html |
| 11 | Geology | https://academics.iu.edu/degrees/bloomington/master-of-science/geology.html |
| 12 | Mathematics | https://academics.iu.edu/degrees/bloomington/master-of-science/mathematics.html |
| 13 | Microbiology | https://academics.iu.edu/degrees/bloomington/master-of-science/microbiology.html |
| 14 | Neuroscience | https://academics.iu.edu/degrees/bloomington/master-of-science/neuroscience.html |
| 15 | Physics | https://academics.iu.edu/degrees/bloomington/master-of-science/physics.html |
| 16 | Psychology | https://academics.iu.edu/degrees/bloomington/master-of-science/psychology.html |
| 17 | Statistics | https://academics.iu.edu/degrees/bloomington/master-of-science/statistics.html |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomy & Cell Biology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/anatomy+cell-biology.html |
| 2 | Anthropology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/anthropology.html |
| 3 | Art History | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/art-history.html |
| 4 | Biochemistry | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/biochemistry.html |
| 5 | Biology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/biology.html |
| 6 | Chemistry | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/chemistry.html |
| 7 | Classical Studies | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/classical-studies.html |
| 8 | Cognitive Science | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/cognitive-science.html |
| 9 | Comparative Literature | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/comparative-literature.html |
| 10 | Computer Science | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/computer-science.html |
| 11 | East Asian Languages & Cultures | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/east-asian-languages+cultures.html |
| 12 | Economics | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/economics.html |
| 13 | English | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/english.html |
| 14 | French & Italian | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/french+italian.html |
| 15 | Geography | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/geography.html |
| 16 | Geology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/geology.html |
| 17 | Germanic Studies | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/germanic-studies.html |
| 18 | History | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/history.html |
| 19 | Linguistics | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/linguistics.html |
| 20 | Mathematics | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/mathematics.html |
| 21 | Microbiology & Immunology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/microbiology+immunology.html |
| 22 | Molecular, Cellular & Developmental Biology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/molecular-cellular+developmental-biology.html |
| 23 | Neuroscience | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/neuroscience.html |
| 24 | Philosophy | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/philosophy.html |
| 25 | Physics | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/physics.html |
| 26 | Political Science | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/political-science.html |
| 27 | Psychology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/psychology.html |
| 28 | Religious Studies | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/religious-studies.html |
| 29 | Slavic Languages & Literatures | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/slavic-languages+literatures.html |
| 30 | Sociology | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/sociology.html |
| 31 | Spanish & Portuguese | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/spanish+portuguese.html |
| 32 | Speech & Hearing Sciences | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/speech+hearing-sciences.html |

#### Jacobs School of Music

##### MM (Master of Music) Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bassoon | https://academics.iu.edu/degrees/bloomington/master-of-music/bassoon.html |
| 2 | Cello | https://academics.iu.edu/degrees/bloomington/master-of-music/cello.html |
| 3 | Clarinet | https://academics.iu.edu/degrees/bloomington/master-of-music/clarinet.html |
| 4 | Composition | https://academics.iu.edu/degrees/bloomington/master-of-music/composition.html |
| 5 | Conducting | https://academics.iu.edu/degrees/bloomington/master-of-music/conducting.html |
| 6 | Double Bass | https://academics.iu.edu/degrees/bloomington/master-of-music/double-bass.html |
| 7 | Flute | https://academics.iu.edu/degrees/bloomington/master-of-music/flute.html |
| 8 | Guitar | https://academics.iu.edu/degrees/bloomington/master-of-music/guitar.html |
| 9 | Harp | https://academics.iu.edu/degrees/bloomington/master-of-music/harp.html |
| 10 | Horn | https://academics.iu.edu/degrees/bloomington/master-of-music/horn.html |
| 11 | Jazz Studies | https://academics.iu.edu/degrees/bloomington/master-of-music/jazz-studies.html |
| 12 | Oboe | https://academics.iu.edu/degrees/bloomington/master-of-music/oboe.html |
| 13 | Organ | https://academics.iu.edu/degrees/bloomington/master-of-music/organ.html |
| 14 | Percussion | https://academics.iu.edu/degrees/bloomington/master-of-music/percussion.html |
| 15 | Piano | https://academics.iu.edu/degrees/bloomington/master-of-music/piano.html |
| 16 | Saxophone | https://academics.iu.edu/degrees/bloomington/master-of-music/saxophone.html |
| 17 | Trombone | https://academics.iu.edu/degrees/bloomington/master-of-music/trombone.html |
| 18 | Trumpet | https://academics.iu.edu/degrees/bloomington/master-of-music/trumpet.html |
| 19 | Tuba | https://academics.iu.edu/degrees/bloomington/master-of-music/tuba.html |
| 20 | Viola | https://academics.iu.edu/degrees/bloomington/master-of-music/viola.html |
| 21 | Violin | https://academics.iu.edu/degrees/bloomington/master-of-music/violin.html |
| 22 | Voice | https://academics.iu.edu/degrees/bloomington/master-of-music/voice.html |
| (更多MM专业 - 共约52个...) | | |

##### DM (Doctor of Music) Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bassoon | https://academics.iu.edu/degrees/bloomington/doctor-of-music/bassoon.html |
| 2 | Cello | https://academics.iu.edu/degrees/bloomington/doctor-of-music/cello.html |
| 3 | Clarinet | https://academics.iu.edu/degrees/bloomington/doctor-of-music/clarinet.html |
| 4 | Composition | https://academics.iu.edu/degrees/bloomington/doctor-of-music/composition.html |
| 5 | Conducting | https://academics.iu.edu/degrees/bloomington/doctor-of-music/conducting.html |
| (更多DM专业 - 共约48个...) | | |

#### Luddy School of Informatics, Computing, and Engineering

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://academics.iu.edu/degrees/bloomington/master-of-science-in-computer-science.html |
| 2 | Data Science | https://academics.iu.edu/degrees/bloomington/master-of-science-in-data-science.html |
| 3 | Informatics | https://academics.iu.edu/degrees/bloomington/master-of-science-in-informatics.html |
| 4 | Information Science | https://academics.iu.edu/degrees/bloomington/master-of-information-science.html |
| 5 | Information Systems | https://academics.iu.edu/degrees/bloomington/master-of-science-in-information-systems.html |
| 6 | Intelligent Systems Engineering | https://academics.iu.edu/degrees/bloomington/master-of-science-in-intelligent-systems-engineering.html |
| 7 | Human-Computer Interaction | https://academics.iu.edu/degrees/bloomington/master-of-science-in-human-computer-interaction.html |
| 8 | Secure Computing | https://academics.iu.edu/degrees/bloomington/master-of-science-in-secure-computing.html |
| 9 | Cybersecurity Risk Management | https://academics.iu.edu/degrees/bloomington/master-of-science-in-cybersecurity-risk-management.html |
| 10 | Bioinformatics | https://academics.iu.edu/degrees/bloomington/master-of-science-in-bioinformatics.html |
| 11 | Quantum Information Science | https://academics.iu.edu/degrees/bloomington/master-of-science-in-quantum-information-science.html |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/computer-science.html |
| 2 | Informatics | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/informatics.html |
| 3 | Information Science | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/information-science.html |
| 4 | Intelligent Systems Engineering | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/intelligent-systems-engineering.html |

#### O'Neill School of Public and Environmental Affairs

##### MPA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science | https://academics.iu.edu/degrees/bloomington/master-of-science-in-environmental-science/environmental-science.html |
| 2 | Public Affairs | https://academics.iu.edu/degrees/bloomington/master-of-public-affairs/public-affairs.html |
| 3 | Public Affairs (Online) | https://academics.iu.edu/degrees/bloomington/master-of-public-affairs-online.html |
| 4 | Environmental Sustainability | https://academics.iu.edu/degrees/bloomington/master-of-environmental-sustainability.html |
| 5 | Healthcare Management | https://academics.iu.edu/degrees/bloomington/master-of-science-in-healthcare-management-online.html |

##### MPP Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | https://academics.iu.edu/degrees/bloomington/master-of-public-policy/public-policy.html |
| 2 | Public Policy (Online) | https://academics.iu.edu/degrees/bloomington/master-of-public-policy.html |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/environmental-science.html |
| 2 | Public Affairs | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/public-affairs.html |
| 3 | Public Policy | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/public-policy.html |

#### School of Education

##### MEd Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/adult-education.html |
| 2 | Art Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/art-education.html |
| 3 | Counselor Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/counselor-education.html |
| 4 | Curriculum & Instruction | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/curriculum+instruction.html |
| 5 | Educational Leadership | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/educational-leadership.html |
| 6 | Higher Education & Student Affairs | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/higher-education+student-affairs.html |
| 7 | Instructional Systems Technology | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/instructional-systems-technology.html |
| 8 | Language Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/language-education.html |
| 9 | Literacy, Culture & Language Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/literacy-culture+language-education.html |
| 10 | Mathematics Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/mathematics-education.html |
| 11 | Science & Environmental Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/science+environmental-education.html |
| 12 | Social Studies Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/social-studies-education.html |
| 13 | Special Education | https://academics.iu.edu/degrees/bloomington/master-of-science-in-education/special-education.html |

##### EdD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | https://academics.iu.edu/degrees/bloomington/doctor-of-education/educational-leadership.html |
| 2 | Higher Education | https://academics.iu.edu/degrees/bloomington/doctor-of-education/higher-education.html |
| 3 | Instructional Systems Technology | https://academics.iu.edu/degrees/bloomington/doctor-of-education/instructional-systems-technology.html |
| 4 | Language Education | https://academics.iu.edu/degrees/bloomington/doctor-of-education/language-education.html |
| 5 | Literacy, Culture & Language Education | https://academics.iu.edu/degrees/bloomington/doctor-of-education/literacy-culture+language-education.html |
| 6 | Mathematics Education | https://academics.iu.edu/degrees/bloomington/doctor-of-education/mathematics-education.html |
| 7 | Science Education | https://academics.iu.edu/degrees/bloomington/doctor-of-education/science-education.html |

#### Maurer School of Law

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Law | JD | https://academics.iu.edu/degrees/bloomington/doctor-of-jurisprudence.html |
| 2 | Laws | LLM | https://academics.iu.edu/degrees/bloomington/master-of-laws.html |
| 3 | Comparative Law | LLM | https://academics.iu.edu/degrees/bloomington/master-of-comparative-law.html |
| 4 | Juridical Science | SJD | https://academics.iu.edu/degrees/bloomington/doctor-of-juridical-science.html |
| 5 | Legal Studies | MLS | https://academics.iu.edu/degrees/bloomington/master-of-legal-studies.html |

#### School of Nursing

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing | MSN | https://academics.iu.edu/degrees/bloomington/master-of-science-in-nursing.html |
| 2 | Nursing Practice | DNP | https://academics.iu.edu/degrees/bloomington/doctor-of-nursing-practice.html |

#### School of Optometry

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Optometry | OD | https://academics.iu.edu/degrees/bloomington/doctor-of-optometry.html |
| 2 | Vision Science | MS | https://academics.iu.edu/degrees/bloomington/master-of-science/vision-science.html |
| 3 | Vision Science | PhD | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/vision-science.html |

#### School of Public Health - Bloomington

##### MPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://academics.iu.edu/degrees/bloomington/master-of-public-health/public-health.html |
| 2 | Public Health (Accelerated) | https://academics.iu.edu/degrees/bloomington/master-of-public-health-accelerated.html |
| 3 | Environmental Health | https://academics.iu.edu/degrees/bloomington/master-of-science-in-environmental-and-occupational-health-accelerated.html |
| 4 | Biostatistics | https://academics.iu.edu/degrees/bloomington/master-of-science-in-biostatistics.html |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Kinesiology | https://academics.iu.edu/degrees/bloomington/master-of-science-in-kinesiology.html |
| 2 | Applied Health Science | https://academics.iu.edu/degrees/bloomington/master-of-science-in-applied-health-science.html |
| 3 | Nutrition | https://academics.iu.edu/degrees/bloomington/master-of-science-in-nutrition.html |
| 4 | Recreation | https://academics.iu.edu/degrees/bloomington/master-of-science-in-recreation.html |

##### DrPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://academics.iu.edu/degrees/bloomington/doctor-of-public-health.html |

#### School of Social Work

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Social Work | MSW | https://academics.iu.edu/degrees/bloomington/master-of-social-work.html |
| 2 | Social Work (Accelerated) | MSW | https://academics.iu.edu/degrees/bloomington/master-of-social-work-accelerated.html |
| 3 | Social Work | PhD | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/social-work.html |

#### The Media School

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Journalism | MA | https://academics.iu.edu/degrees/bloomington/master-of-arts/journalism.html |
| 2 | Media Arts & Sciences | MS | https://academics.iu.edu/degrees/bloomington/master-of-science/media-arts+sciences.html |
| 3 | Media Leadership & Business | MS | https://academics.iu.edu/degrees/bloomington/master-of-science-in-media-leadership-and-business.html |
| 4 | Data Journalism | Grad Cert | https://academics.iu.edu/degrees/bloomington/graduate-certificate-in-data-journalism-online.html |

#### Hamilton Lugar School of Global and International Studies

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | International Studies | MA | https://academics.iu.edu/degrees/bloomington/master-of-arts/international-studies.html |
| 2 | International Affairs | MIA | https://academics.iu.edu/degrees/bloomington/master-of-international-affairs.html |
| 3 | International Studies | MS | https://academics.iu.edu/degrees/bloomington/master-of-science-in-international-studies.html |
| 4 | International Studies | PhD | https://academics.iu.edu/degrees/bloomington/doctor-of-philosophy/international-studies.html |

### 2.2 Graduate admissions model

**Decentralized** — each department/program has its own admission requirements, deadlines, and decision process. The Graduate School Bloomington (IUGSB) provides central services but admissions decisions are made by individual programs.

**Application platform**: Apply IU Application or Common Application (for fall 2026: `iugraduate2026.cas.myliaison.com`; for winter 2026+: `admissions.graduate.iu.edu`)

**Application fee**: Standard fee applies (reduced fee of $35 for certain cases like dual programs or re-applications). Fee waivers available for qualifying participants in specific programs (GU2IU, BTAA, Peace Corps, AmeriCorps, etc.)

**TOEFL code**: 1324

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| 招生网站 | https://bloomington.iu.edu/admissions/ |
| 申请系统 | Apply IU Application 或 Common Application |
| EA截止日期 | **November 1** (non-binding) |
| RD截止日期 | **February 1** |
| EA结果通知 | January 15 |
| RD结果通知 | March 15 |
| 押金截止 | May 1 ($100, nonrefundable) |
| 申请费 | 需确认 |
| SAT/ACT政策 | **Test-optional** (confirmed) |
| SAT/ACT截止日期 | EA: Nov 1; 奖学金补充: Jan 15 |
| Superscore | 需确认 |
| 面试政策 | 无面试 |
| 推荐信 | 需确认 |
| 作品集 | 仅艺术/设计/音乐专业需要 |
| 转学通道 | 有，单独截止日期 |

**来源**: `bloomington.iu.edu/admissions/apply/freshman/deadlines.html` (2026-07-06)

### 3.2 Undergraduate English proficiency table

**入学要求 (Admission Requirements)**:

| 考试 | 最低分数 | 备注 |
|------|---------|------|
| TOEFL iBT | 79 | |
| TOEFL PBT | 550 | |
| TOEFL iBT Home Edition | 79 | |
| TOEFL ITP+ China | 543 | |
| IELTS | 6.5 | |
| IELTS Indicator | 6.5 | |
| Duolingo (DET) | 115 | |
| Cambridge English | 176 | |
| Pearson PTE | 53 | |
| Michigan MET | 53 | |
| SAT EBRW | 560 | 可替代语言考试 |
| ACT English | 21 | 可替代语言考试 |

**免修EAP课程要求 (Direct Admission without EAP)**:

| 考试 | 最低分数 | 备注 |
|------|---------|------|
| TOEFL iBT | 100 | |
| TOEFL PBT | 600 | |
| TOEFL ITP+ China | 627 | |
| IELTS | 7.5 | |
| IELTS Indicator | 7.5 | |
| Cambridge English | 191 | |
| Duolingo (DET) | 130 | |
| Pearson PTE | 68 | |
| Michigan MET | 63 | |
| SAT EBRW | 710 | |
| ACT English | 32 | |

**免修条件**: 完成IEP Level 7; 或来自英语国家公民; 或在英语国家完成3年以上中学教育; 或IB HL English A 4分以上; 或GCE A-Level English A/B/C; 或AP English 3分以上。

**来源**: `bloomington.iu.edu/admissions/apply/international/english-proficiency.html` (2026-07-06)

### 3.3 Graduate — global rules

- **招生模式**: 完全分散制 (fully decentralized)，每个院系/项目独立招生
- **申请平台**: Apply IU Application (Liaison)
- **申请费**: 标准费用（具体金额需确认）; 减免$35适用于双重项目申请者或重新申请者
- **GRE/GMAT**: 由各项目自行决定
- **语言要求**: 由各项目自行决定; TOEFL code 1324
- **CGS April-15**: 需确认是否为签约方
- **博士资助**: 大多数PhD项目提供全额资助

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

| 费用项目 | Indiana居民 | 非居民 (OOS) | 说明 |
|---------|------------|-------------|------|
| 学费和强制费用 (Tuition & mandatory fees) | $12,142 | $42,702 | 包含40学分/年（秋、春、冬季短学期） |
| 住宿和餐饮 (Housing & food) | $14,398 | $14,398 | 校内住宿估算 |
| **直接费用合计 (Total direct costs)** | **$26,540** | **$57,100** | |
| 书本和用品 (Books & supplies) | $1,320 | $1,320 | |
| 交通 (Transportation) | $284 | $2,106 | |
| 个人开支 (Personal expenses) | $2,430 | $2,430 | |
| **间接费用合计 (Total indirect costs)** | **$4,034** | **$5,856** | |
| **总费用 (Total cost of attendance)** | **$30,574** | **$62,956** | |

> **注**: IU采用统一费率学费 (flat-rate tuition)，学生可在秋、春学期及冬季短学期修读最多40学分，费用相同。

**来源**: `bloomington.iu.edu/cost-aid/cost-attendance/undergraduate.html` (2026-07-06)

### 4.2 Undergraduate financial-aid policy

- **83%** 的新生获得经济援助
- **62%** 的本科生无债务毕业
- **95%** 的毕业生接受全职工作或继续深造
- 奖学金考虑最高优先级: **November 1** EA截止日期前提交申请
- IU奖学金申请截止: **February 15**
- 奖学金类型: 学术成就、领导力、经济需求、特殊才能等
- FAFSA为申请联邦、州和机构援助的必要表格

**来源**: `bloomington.iu.edu/cost-aid/financial-aid/`, `bloomington.iu.edu/cost-aid/scholarships/` (2026-07-06)

### 4.3 Graduate cost & funding framework

- **学费**: 研究生学费因项目而异，详见各院系网站
- **资助类型**: RA/TA/fellowship/grant，由各项目自行管理
- **博士资助**: 大多数PhD项目提供全额资助（学费减免+生活津贴）
- **申请费**: 标准费用，部分情况可减免至$35
- **费用豁免**: 可通过GU2IU、BTAA、Peace Corps、AmeriCorps等项目获得

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1 (non-binding)"
  source_url: https://bloomington.iu.edu/admissions/apply/freshman/deadlines.html
  source_snippet: "At Indiana University Bloomington, we have an early action deadline (non-binding) of November 1 and a regular decision deadline of February 1."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "February 1"
  source_url: https://bloomington.iu.edu/admissions/apply/freshman/deadlines.html
  source_snippet: "a regular decision deadline of February 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.test_policy
  value: "Test-optional"
  source_url: https://bloomington.iu.edu/admissions/apply/freshman/test-optional.html
  source_snippet: "IU Bloomington has a test-optional admissions policy, which allows students to choose at the point of application whether to have SAT and/or ACT test scores considered as part of their application review."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.cost.tuition_in_state
  value: "$12,142"
  source_url: https://bloomington.iu.edu/cost-aid/cost-attendance/undergraduate.html
  source_snippet: "Tuition and mandatory fees | $12,142 | $42,702"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.cost.tuition_oos
  value: "$42,702"
  source_url: https://bloomington.iu.edu/cost-aid/cost-attendance/undergraduate.html
  source_snippet: "Tuition and mandatory fees | $12,142 | $42,702"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.cost.total_in_state
  value: "$30,574"
  source_url: https://bloomington.iu.edu/cost-aid/cost-attendance/undergraduate.html
  source_snippet: "Total cost of attendance | $30,574 | $62,956"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_oos
  value: "$62,956"
  source_url: https://bloomington.iu.edu/cost-aid/cost-attendance/undergraduate.html
  source_snippet: "Total cost of attendance | $30,574 | $62,956"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.class_profile.gpa_range
  value: "3.73–4.00"
  source_url: https://bloomington.iu.edu/admissions/class-profile.html
  source_snippet: "GPA | 3.73–4.00 | 4.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.class_profile.sat_range
  value: "1250–1450"
  source_url: https://bloomington.iu.edu/admissions/class-profile.html
  source_snippet: "SAT scores (Math and Evidence-Based Reading and Writing) | 1250–1450 | 1354"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.class_profile.act_range
  value: "29–33"
  source_url: https://bloomington.iu.edu/admissions/class-profile.html
  source_snippet: "ACT scores (Composite) | 29–33 | 31"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.class_profile.test_optional_rate
  value: "45%"
  source_url: https://bloomington.iu.edu/admissions/class-profile.html
  source_snippet: "Admission to IU is test-optional, and 45% of students admitted for fall 2025 applied as test-optional."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.class_profile.freshman_class_size
  value: "10,127"
  source_url: https://bloomington.iu.edu/admissions/class-profile.html
  source_snippet: "10,127 students in the 2025 freshman class"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english_proficiency.toefl
  value: "79 (iBT)"
  source_url: https://bloomington.iu.edu/admissions/apply/international/english-proficiency.html
  source_snippet: "TOEFL (internet-based test) | 79"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-014:
  field: undergraduate.english_proficiency.ielts
  value: "6.5"
  source_url: https://bloomington.iu.edu/admissions/apply/international/english-proficiency.html
  source_snippet: "International English Language Testing System (IELTS) | 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-015:
  field: undergraduate.english_proficiency.duolingo
  value: "115"
  source_url: https://bloomington.iu.edu/admissions/apply/international/english-proficiency.html
  source_snippet: "Duolingo English Test (DET) | 115"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-016:
  field: undergraduate.enrollment_deposit
  value: "$100"
  source_url: https://bloomington.iu.edu/admissions/apply/freshman/deadlines.html
  source_snippet: "you must declare your intent to enroll and pay your $100 enrollment deposit by May 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.scholarship_deadline
  value: "February 15"
  source_url: https://bloomington.iu.edu/cost-aid/scholarships/
  source_snippet: "The IU Scholarships Application is due by February 15 for all incoming students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions_model
  value: "Decentralized"
  source_url: https://bloomington.iu.edu/admissions/apply/graduate/
  source_snippet: "Each department has its own graduate admission requirements. Visit the school website that offers your intended program for admission requirements and specific application instructions."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.tofel_code
  value: "1324"
  source_url: https://bloomington.iu.edu/admissions/apply/international/english-proficiency.html
  source_snippet: "IU Bloomington's TOEFL code is 1324."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-001:
  field: programs.total_count
  value: "1,175 (including accelerated)"
  source_url: https://bloomington.iu.edu/academics/degrees-majors/programs.html
  source_snippet: "Showing 20 of 1175 degrees on page 1 of 59"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-002:
  field: programs.bachelors_count
  value: "397"
  source_url: https://bloomington.iu.edu/academics/degrees-majors/programs.html?program_type=2
  source_snippet: "Showing 20 of 397 degrees on page 1 of 20"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-003:
  field: programs.masters_count
  value: "369"
  source_url: https://bloomington.iu.edu/academics/degrees-majors/programs.html?program_type=7
  source_snippet: "Showing 20 of 369 degrees on page 1 of 19"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-004:
  field: programs.doctoral_count
  value: "175"
  source_url: https://bloomington.iu.edu/academics/degrees-majors/programs.html?program_type=6
  source_snippet: "Showing 20 of 175 degrees on page 1 of 9"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-005:
  field: programs.grad_certificate_count
  value: "89"
  source_url: https://bloomington.iu.edu/academics/degrees-majors/programs.html?program_type=3
  source_snippet: "Showing 20 of 89 degrees on page 1 of 5"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-S-001:
  field: schools.count
  value: "16 degree-granting schools/colleges"
  source_url: https://bloomington.iu.edu/academics/schools/
  source_snippet: "IU Bloomington offers undergraduate, graduate, and professional programs across 16 degree-granting schools and colleges"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-001:
  field: financial_aid.receiving_rate
  value: "83%"
  source_url: https://bloomington.iu.edu/cost-aid/financial-aid/
  source_snippet: "83% of IUB beginning students receive financial aid"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-002:
  field: financial_aid.debt_free_rate
  value: "62%"
  source_url: https://bloomington.iu.edu/cost-aid/financial-aid/
  source_snippet: "62% of undergrad students graduate debt free"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-003:
  field: financial_aid.employment_rate
  value: "95%"
  source_url: https://bloomington.iu.edu/cost-aid/financial-aid/
  source_snippet: "95% of graduates accept full-time employment or continue their education upon graduation"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
iu-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: 学院层级、学位清单、分布矩阵
├── 01-ug-programs-arts-sciences.md     # Section 1: College of Arts & Sciences UG programs
├── 02-ug-programs-kelley.md            # Section 1: Kelley School of Business UG programs
├── 03-ug-programs-jacobs.md            # Section 1: Jacobs School of Music UG programs
├── 04-ug-programs-luddy.md             # Section 1: Luddy School UG programs
├── 05-ug-programs-oneill.md            # Section 1: O'Neill School UG programs
├── 06-ug-programs-education.md         # Section 1: School of Education UG programs
├── 07-ug-programs-media.md             # Section 1: The Media School UG programs
├── 08-ug-programs-other.md             # Section 1: Other schools UG programs
├── 09-grad-programs-kelley.md          # Section 2: Kelley School Grad programs
├── 10-grad-programs-arts-sciences.md   # Section 2: CAS Grad programs
├── 11-grad-programs-jacobs.md          # Section 2: Jacobs School Grad programs
├── 12-grad-programs-luddy.md           # Section 2: Luddy School Grad programs
├── 13-grad-programs-oneill.md          # Section 2: O'Neill School Grad programs
├── 14-grad-programs-education.md       # Section 2: School of Education Grad programs
├── 15-grad-programs-other.md           # Section 2: Other schools Grad programs
├── 16-deadlines-requirements.md        # Section 3: 申请要求与截止日期
├── 17-costs-financial-aid.md           # Section 4: 费用与经济援助
├── 18-evidence-chain.md                # Section 5: 证据链索引
└── 19-weknora-manifest.md              # Section 6: 本清单
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "iu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BM|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标URL | 说明 |
|--------|--------|---------|------|
| P0 | 申请费金额 | bloomington.iu.edu/admissions/apply/ | 页面未明确列出标准申请费 |
| P0 | 研生学费明细 | bloomington.iu.edu/cost-aid/cost-attendance/graduate.html | 需提取研究生学费表 |
| P1 | 国际学生费用 | bloomington.iu.edu/cost-aid/cost-attendance/international/ | 国际学生COA |
| P1 | 需求盲取政策 | bloomington.iu.edu/cost-aid/financial-aid/ | 是否need-blind for intl |
| P1 | 各项目GRE要求 | 各院系网站 | 分散制，需逐项目查询 |
| P2 | 完整本科专业列表 | academics.iu.edu/degrees/bloomington/ | 已提取389/397个 |
| P2 | 完整研究生项目列表 | academics.iu.edu/degrees/bloomington/ | 已提取343/369个硕士, 167/175个博士 |
| P2 | 本科证书完整列表 | academics.iu.edu/degrees/bloomington/ | 47个UG证书待提取 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | IU Bloomington | (其他学校) |
|------|---------------|-----------|
| 类型 | Public | |
| 地点 | Bloomington, IN | |
| EA截止日期 | November 1 | |
| RD截止日期 | February 1 | |
| SAT/ACT要求 | Test-optional | |
| TOEFL最低 | 79 | |
| IELTS最低 | 6.5 | |
| 本科学费 (In-state) | $12,142 | |
| 本科学费 (OOS) | $42,702 | |
| 总COA (In-state) | $30,574 | |
| 总COA (OOS) | $62,956 | |
| Need-blind (Intl) | 需确认 | |
| 项目总数 (Rule 1) | 1,126 | |
| 学院数 (Rule 2) | 16 | |
| 研生申请费 | 需确认 | |
| April-15 honor | 需确认 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: bloomington.iu.edu, academics.iu.edu, college.indiana.edu, kelley.iu.edu, music.indiana.edu, luddy.iu.edu, law.indiana.edu, oneill.indiana.edu, education.indiana.edu, medicine.iu.edu, nursing.iu.edu, optometry.iu.edu, publichealth.indiana.edu, socialwork.iu.edu, mediaschool.indiana.edu, hls.indiana.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
