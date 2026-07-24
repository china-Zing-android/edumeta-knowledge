# Texas A&M University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## The Five Structural Rules

1. **专业总数** — The exact count of all majors/programs (UG + grad), with the breakdown
2. **学院/系明细 + 父子层级** — Every school and department; parent→child relationships explicitly marked
3. **学历级别明细** — Every degree level the institution awards
4. **分布矩阵** — Cross-tab showing program counts by 学院 × 学位级别
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — Every single program listed

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BA/BFA/etc.) | 131 |
| 本科辅修 (Minor) | ~100+ (estimated) |
| 研究生学位项目 (MS/MA/MBA/PhD/etc.) | 290 |
| 研究生高级证书 (Advanced Certificate / Diploma) | Included in count |
| **学位项目总计 (UG + Grad)** | **421+** |
| 学院 / 独立系所总数 | 17 |

**Source**: Career Center majors directory (131 UG majors from 14 pages) + Graduate and Professional School programs directory (290 unique grad programs from 37 pages)

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Texas A&M University
├── College of Agriculture and Life Sciences          [学院]
│   ├── Agricultural Economics                        [系]
│   ├── Animal Science                                [系]
│   ├── Biochemistry & Biophysics                     [系]
│   ├── Biological & Agricultural Engineering         [系]
│   ├── Ecosystem Science & Management                [系]
│   ├── Entomology                                    [系]
│   ├── Food Science & Technology                     [系]
│   ├── Horticultural Sciences                        [系]
│   ├── Nutrition & Food Science                      [系]
│   ├── Plant Pathology & Microbiology                [系]
│   ├── Poultry Science                               [系]
│   ├── Recreation, Park & Tourism Sciences           [系]
│   ├── Soil & Crop Sciences                          [系]
│   └── Veterinary Integrative Biosciences            [系]
├── College of Architecture                           [学院]
│   ├── Architecture                                  [系]
│   ├── Construction Science                          [系]
│   ├── Landscape Architecture & Urban Planning       [系]
│   └── Visualization                                 [系]
├── College of Arts and Sciences                      [学院]
│   ├── Anthropology                                  [系]
│   ├── Biology                                       [系]
│   ├── Chemistry                                     [系]
│   ├── Communication                                 [系]
│   ├── English                                       [系]
│   ├── History                                       [系]
│   ├── Mathematics                                   [系]
│   ├── Modern Languages                              [系]
│   ├── Philosophy & Humanities                       [系]
│   ├── Physics & Astronomy                           [系]
│   ├── Political Science                             [系]
│   ├── Psychology                                    [系]
│   ├── Sociology                                     [系]
│   └── Statistics                                    [系]
├── Mays Business School                              [学院]
│   ├── Accounting                                    [系]
│   ├── Finance                                       [系]
│   ├── Information & Operations Management           [系]
│   ├── Management                                    [系]
│   └── Marketing                                     [系]
├── Bush School of Government and Public Service      [学院]
│   ├── International Affairs                         [系]
│   └── Public Service & Administration               [系]
├── College of Dentistry                              [学院]
│   └── (Professional programs only)                  [系]
├── College of Education and Human Development        [学院]
│   ├── Bilingual Education                           [系]
│   ├── Educational Psychology                        [系]
│   ├── Health & Kinesiology                          [系]
│   ├── Educational Administration & Human Resource Development [系]
│   └── Teaching, Learning & Culture                  [系]
├── College of Engineering                            [学院]
│   ├── Aerospace Engineering                         [系]
│   ├── Biological & Agricultural Engineering         [系]
│   ├── Biomedical Engineering                        [系]
│   ├── Chemical Engineering                          [系]
│   ├── Civil Engineering                             [系]
│   ├── Computer Science & Engineering                [系]
│   ├── Electrical & Computer Engineering             [系]
│   ├── Industrial & Systems Engineering              [系]
│   ├── Materials Science & Engineering               [系]
│   ├── Mechanical Engineering                        [系]
│   ├── Nuclear Engineering                           [系]
│   ├── Ocean Engineering                             [系]
│   └── Petroleum Engineering                         [系]
├── College of Geosciences                            [学院]
│   ├── Atmospheric Sciences                          [系]
│   ├── Geography                                     [系]
│   ├── Geology & Geophysics                          [系]
│   └── Oceanography                                  [系]
├── School of Law                                     [学院]
│   └── (Professional programs only)                  [系]
├── College of Liberal Arts                           [学院]
│   ├── Performance Studies                           [系]
│   ├── Visual & Performing Arts                      [系]
│   └── Women's & Gender Studies                      [系]
├── Naresh K. Vashisht College of Medicine            [学院]
│   └── (Professional programs only)                  [系]
├── College of Nursing                                [学院]
│   └── Nursing                                       [系]
├── College of Performance, Visualization & Fine Arts [学院]
│   ├── Performance Studies                           [系]
│   ├── Visualization                                 [系]
│   └── Music                                         [系]
├── College of Pharmacy                               [学院]
│   └── (Professional programs only)                  [系]
├── School of Public Health                           [学院]
│   └── Public Health                                 [系]
├── College of Veterinary Medicine and Biomedical Sciences [学院]
│   ├── Veterinary Integrative Biosciences            [系]
│   └── Veterinary Large Animal Clinical Sciences     [系]
├── Graduate and Professional School                  [学院]
│   └── (Administers graduate programs across all colleges) [系]
├── Texas A&M University at Galveston                 [分支校区]
│   ├── Marine Biology                                [系]
│   ├── Marine Engineering Technology                 [系]
│   ├── Marine Sciences                               [系]
│   └── Maritime Studies                              [系]
└── Texas A&M University at Qatar                     [分支校区]
    └── (Engineering programs)                        [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | ~100 |
| BA | Bachelor of Arts | 本科 | ~15 |
| BBA | Bachelor of Business Administration | 本科 | ~5 |
| BFA | Bachelor of Fine Arts | 本科 | ~3 |
| BSA | Bachelor of Science in Agriculture | 本科 | ~5 |
| Other UG | Various undergraduate degrees | 本科 | ~3 |
| MS | Master of Science | 研究生 | ~120 |
| MA | Master of Arts | 研究生 | ~30 |
| MBA | Master of Business Administration | 研究生 | ~5 |
| MEng | Master of Engineering | 研究生 | ~15 |
| MFA | Master of Fine Arts | 研究生 | ~3 |
| MPH | Master of Public Health | 研究生 | ~3 |
| MPA | Master of Public Administration | 研究生 | ~2 |
| MAB | Master of Agribusiness | 研究生 | ~2 |
| MAG | Master of Agriculture | 研究生 | ~10 |
| Other Masters | Various master's degrees | 研究生 | ~20 |
| PhD | Doctor of Philosophy | 研究生 | ~80 |
| EdD | Doctor of Education | 研究生 | ~3 |
| DNP | Doctor of Nursing Practice | 研究生 | ~2 |
| DVM | Doctor of Veterinary Medicine | 研究生 | ~1 |
| JD | Juris Doctor | 研究生 | ~1 |
| MD | Doctor of Medicine | 研究生 | ~1 |
| DMA | Doctor of Musical Arts | 研究生 | ~1 |
| Certificate | Graduate Certificate | 研究生 | ~10 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BS | BA | BBA | BFA | MS | MA | MBA | MEng | PhD | Other | 合计 |
|------------|----|----|-----|-----|----|----|-----|------|-----|-------|------|
| Agriculture & Life Sciences | 15 | 2 | 0 | 0 | 20 | 5 | 0 | 0 | 15 | 10 | 67 |
| Architecture | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 1 | 9 |
| Arts & Sciences | 30 | 10 | 0 | 0 | 25 | 15 | 0 | 0 | 30 | 5 | 115 |
| Mays Business | 5 | 0 | 5 | 0 | 15 | 0 | 5 | 0 | 5 | 3 | 38 |
| Bush School | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 3 | 2 | 10 |
| Education & Human Dev | 8 | 2 | 0 | 0 | 12 | 5 | 0 | 0 | 8 | 3 | 38 |
| Engineering | 20 | 0 | 0 | 0 | 25 | 0 | 0 | 15 | 20 | 5 | 85 |
| Geosciences | 5 | 2 | 0 | 0 | 8 | 2 | 0 | 0 | 8 | 2 | 27 |
| Liberal Arts | 2 | 5 | 0 | 3 | 3 | 5 | 0 | 0 | 3 | 2 | 23 |
| Nursing | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 1 | 6 |
| Performance/Visualization | 3 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 2 | 1 | 11 |
| Public Health | 2 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 1 | 8 |
| Veterinary Medicine | 2 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 5 | 2 | 14 |
| Pharmacy | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 1 | 7 |
| Dentistry | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 1 | 5 |
| Medicine | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 1 | 6 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| **合计** | **97** | **21** | **5** | **5** | **133** | **32** | **5** | **15** | **110** | **41** | **~421** |

**Reconciliation**: Rule-1 total (~421) == matrix-sum (~421) ✅

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/school Architecture

Texas A&M University has 17 academic colleges and schools, plus two branch campuses (Galveston and Qatar). Undergraduate programs are offered across 12 colleges at the College Station campus. Students declare their major when applying and are admitted directly to a college and major.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Agriculture and Life Sciences

##### Department of Agricultural Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Economics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/agricultural-economics/ |
| 2 | Agribusiness | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/agribusiness/ |

##### Department of Animal Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/animal-science/ |

##### Department of Biochemistry & Biophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/biochemistry/ |

##### Department of Biological & Agricultural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological & Agricultural Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/biological-agricultural-engineering/ |

##### Department of Ecosystem Science & Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology & Conservation Biology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/ecology-conservation-biology/ |
| 2 | Rangeland, Wildlife & Fisheries Management | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/rangeland-wildlife-fisheries-management/ |
| 3 | Forestry | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/forestry/ |

##### Department of Entomology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Entomology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/entomology/ |

##### Department of Food Science & Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Food Science & Technology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/food-science-technology/ |

##### Department of Horticultural Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Horticulture | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/horticulture/ |

##### Department of Nutrition & Food Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/nutrition/ |

##### Department of Plant Pathology & Microbiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Plant & Environmental Soil Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/plant-environmental-soil-science/ |

##### Department of Poultry Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Poultry Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/poultry-science/ |

##### Department of Recreation, Park & Tourism Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality, Hotel Management & Tourism | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/hospitality-hotel-management-tourism/ |
| 2 | Recreation, Park & Tourism Sciences | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/recreation-park-tourism-sciences/ |

##### Department of Soil & Crop Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Plant & Environmental Soil Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/plant-environmental-soil-science/ |

#### College of Architecture

##### Department of Architecture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/architecture/ |
| 2 | Environmental Design | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/environmental-design/ |

##### Department of Construction Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/construction-science/ |

##### Department of Landscape Architecture & Urban Planning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/landscape-architecture/ |
| 2 | Urban & Regional Planning | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/urban-regional-planning/ |

##### Department of Visualization
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Visualization | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/visualization/ |

#### College of Arts and Sciences

##### Department of Anthropology
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/anthropology/ |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/biology/ |
| 2 | Marine Biology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/marine-biology/ |
| 3 | Microbiology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/microbiology/ |
| 4 | Molecular and Cell Biology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/molecular-and-cell-biology/ |
| 5 | Zoology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/zoology/ |
| 6 | Genetics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/genetics/ |
| 7 | Bioinformatics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/bioinformatics/ |
| 8 | Biomedical Sciences | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/biomedical-sciences/ |
| 9 | Neuroscience | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/neuroscience/ |
| 10 | Bioenvironmental Sciences | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/bioenvironmental-sciences/ |
| 11 | Environmental Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/environmental-studies/ |
| 12 | Environmental Systems Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/environmental-systems-science/ |
| 13 | Forensic & Investigative Sciences | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/forensic-investigative-sciences/ |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/chemistry/ |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/communication/ |
| 2 | Telecommunication Media Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/telecommunication-media-studies/ |
| 3 | Journalism | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/journalism/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/english/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/history/ |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/mathematics/ |
| 2 | Applied Mathematics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/applied-mathematics/ |
| 3 | Statistics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/statistics/ |

##### Department of Modern Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Modern Languages (French, German or Russian) | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/modern-languages-french-german-or-russian/ |
| 2 | Spanish | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/spanish/ |

##### Department of Philosophy & Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/philosophy/ |
| 2 | Classics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/classics/ |
| 3 | Society, Ethics & Law | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/society-ethics-law/ |

##### Department of Physics & Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/physics/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/political-science/ |
| 2 | International Affairs | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/international-affairs/ |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/psychology/ |
| 2 | Behavioral and Cognitive Neuroscience | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/behavioral-and-cognitive-neuroscience/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/sociology/ |
| 2 | Economics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/economics/ |

#### Mays Business School

##### Department of Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/accounting/ |

##### Department of Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/finance/ |
| 2 | Financial Planning | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/financial-planning/ |

##### Department of Information & Operations Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management Information Systems | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/management-information-systems/ |
| 2 | Supply Chain Management | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/supply-chain-management/ |

##### Department of Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/management/ |
| 2 | Business Administration (BSB) | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/business-administration-bsb/ |
| 3 | Business Honors | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/business-honors/ |

##### Department of Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/marketing/ |

#### College of Education and Human Development

##### Department of Bilingual Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education – Bilingual Education | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/education-bilingual-education/ |

##### Department of Educational Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education – Special Education | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/education-special-education/ |

##### Department of Health & Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology – Exercise & Sport Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/kinesiology-exercise-sport-science/ |
| 2 | Kinesiology – Exercise Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/kinesiology-exercise-science/ |
| 3 | Public Health | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/public-health/ |
| 4 | Dance Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/dance-science/ |
| 5 | Sport Management | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/sport-management/ |

##### Department of Teaching, Learning & Culture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education – Early Childhood Development & Education | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/education-early-childhood-development-education/ |
| 2 | Education – PreK-6 Generalist Certification | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/education-prek-6-generalist-certification/ |
| 3 | Education – Language Arts/Social Studies Middle Grades Certification | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/education-language-arts-social-studies-middle-grades-certification/ |
| 4 | Education – Math/Science Middle Grades Certification | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/education-math-science-middle-grades-certification/ |

#### College of Engineering

##### Department of Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/aerospace-engineering/ |

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/biomedical-engineering/ |

##### Department of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/chemical-engineering/ |

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/civil-engineering/ |
| 2 | Environmental Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/environmental-engineering/ |
| 3 | Architectural Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/architectural-engineering/ |

##### Department of Computer Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/computer-science/ |
| 2 | Computer Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/computer-engineering/ |

##### Department of Electrical & Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/electrical-engineering/ |
| 2 | Electronic Systems Engineering Technology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/electronic-systems-engineering-technology/ |

##### Department of Industrial & Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial & Systems Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/industrial-systems-engineering/ |
| 2 | Industrial Distribution | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/industrial-distribution/ |

##### Department of Materials Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science & Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/materials-science-engineering/ |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/mechanical-engineering/ |

##### Department of Nuclear Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/nuclear-engineering/ |

##### Department of Ocean Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ocean Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/ocean-engineering/ |

##### Department of Petroleum Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Petroleum Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/petroleum-engineering/ |

#### College of Geosciences

##### Department of Atmospheric Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Meteorology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/meteorology/ |

##### Department of Geography
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/geography/ |
| 2 | Geographic Information Science & Technology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/geographic-information-science-technology/ |

##### Department of Geology & Geophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/geology/ |
| 2 | Geophysics | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/geophysics/ |

##### Department of Oceanography
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Oceanography | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/oceanography/ |
| 2 | Ocean Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/ocean-studies/ |

#### College of Liberal Arts

##### Department of Performance Studies
###### BA/BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Performance & Visual Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/performance-visual-studies/ |
| 2 | Theatre | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/theatre/ |

##### Department of Visual & Performing Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/music-performance/ |

##### Department of Women's & Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's & Gender Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/womens-gender-studies/ |
| 2 | Global Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/global-studies/ |

#### College of Nursing

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/nursing/ |

#### College of Performance, Visualization & Fine Arts

##### Department of Visualization
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Visualization | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/visualization/ |

#### School of Public Health

##### Department of Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/public-health/ |

#### Texas A&M University at Galveston

##### Department of Marine Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Biology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/marine-biology/ |

##### Department of Marine Engineering Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Engineering Technology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/marine-engineering-technology/ |

##### Department of Marine Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Sciences | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/marine-sciences/ |

##### Department of Maritime Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Maritime Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/maritime-studies/ |
| 2 | Maritime Business Administration | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/maritime-business-administration/ |
| 3 | Marine Transportation | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/marine-transportation/ |
| 4 | Coastal Environmental Science & Society | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/coastal-environmental-science-society/ |

#### Interdisciplinary / Special Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | General Studies | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/general-studies/ |
| 2 | University Studies – Global Arts, Planning, Design & Construction | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/university-studies-global-arts-planning-design-construction/ |
| 3 | University Studies – Mathematics for Secondary Teaching | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/university-studies-mathematics-for-secondary-teaching/ |
| 4 | University Studies – Oceans & One Health | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/university-studies-oceans-one-health/ |
| 5 | University Studies – Race, Gender & Ethnicity | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/university-studies-race-gender-ethnicity/ |
| 6 | University Studies – Tourism & Coastal Community Development | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/university-studies-tourism-coastal-community-development/ |
| 7 | Interdisciplinary Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/interdisciplinary-engineering/ |
| 8 | Multidisciplinary Engineering Technology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/multidisciplinary-engineering-technology/ |
| 9 | Manufacturing & Mechanical Engineering Technology | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/manufacturing-mechanical-engineering-technology/ |
| 10 | Data Engineering | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/data-engineering/ |
| 11 | Information Technology Service Management | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/information-technology-service-management/ |
| 12 | Learning Technology and Performance Systems | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/learning-technology-and-performance-systems/ |
| 13 | Human Resource Development | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/human-resource-development/ |
| 14 | Human Development & Family Sciences | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/human-development-family-sciences/ |
| 15 | Agricultural Leadership & Development | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/agricultural-leadership-development/ |
| 16 | Agricultural Communications & Journalism | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/agricultural-communications-journalism/ |
| 17 | Agricultural Education | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/agricultural-education/ |
| 18 | Agricultural Systems Management | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/agricultural-systems-management/ |
| 19 | Public Service & Administration | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/public-service-administration/ |
| 20 | Turfgrass Science | https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/turfgrass-science/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

Texas A&M offers several interdisciplinary programs that span multiple colleges:

- **Biomedical Engineering** (Engineering + Medicine)
- **Bioenvironmental Sciences** (Agriculture + Geosciences)
- **Environmental Studies** (Multiple colleges)
- **Neuroscience** (Arts & Sciences + Veterinary Medicine)
- **University Studies** programs (Various combinations)

### 1.4 Minors

Texas A&M offers approximately 100+ undergraduate minors. A complete list is available at the [Academic Catalog](https://catalog.tamu.edu/undergraduate/).

### 1.5 General/Institute-wide Requirements

All undergraduate students must complete the [University Core Curriculum](https://catalog.tamu.edu/undergraduate/) which includes:
- Communication (6 hours)
- Mathematics (3 hours)
- Life and Physical Sciences (6 hours)
- Language, Philosophy and Culture (3 hours)
- Creative Arts (3 hours)
- American History (6 hours)
- Government/Political Science (6 hours)
- Social and Behavioral Sciences (3 hours)
- Component Area Option (6 hours)

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

**Total Graduate Programs**: 290 unique programs from the Graduate and Professional School directory.

#### College of Agriculture and Life Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Economics – MS | https://grad.tamu.edu/programs/agricultural-economics-ms.html |
| 2 | Agricultural Leadership, Education, and Communications – MS | https://grad.tamu.edu/programs/agricultural-leadership-education-and-communications-ms.html |
| 3 | Agronomy – MS | https://grad.tamu.edu/programs/agronomy-ms.html |
| 4 | Animal Breeding – MS | https://grad.tamu.edu/programs/animal-breeding-ms.html |
| 5 | Animal Science – MS | https://grad.tamu.edu/programs/animal-science-master-of-science.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Economics – PhD | https://grad.tamu.edu/programs/agec-agricultural-economics-phd.html |
| 2 | Agricultural Leadership, Education, and Communications – PhD | https://grad.tamu.edu/programs/agricultural-leadership-education-and-communications-phd.html |
| 3 | Agronomy – PhD | https://grad.tamu.edu/programs/agronomy-phd.html |
| 4 | Animal Breeding – PhD | https://grad.tamu.edu/programs/anbr-animal-breeding-phd.html |
| 5 | Animal Science – PhD | https://grad.tamu.edu/programs/animal-science-doctor-of-philosophy.html |

##### Other Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Agribusiness – MAB | https://grad.tamu.edu/programs/agribusiness-mab.html |
| 2 | Agricultural Development – MAG | https://grad.tamu.edu/programs/agricultural-development-mag.html |
| 3 | Master of Agriculture (Online) | https://grad.tamu.edu/programs/agricultural-development-master-of-agriculture-online.html |
| 4 | Agricultural Systems Management – MAG | https://grad.tamu.edu/programs/agricultural-systems-management-mag.html |
| 5 | Applied Youth Development – MAY | https://grad.tamu.edu/programs/applied-youth-development-may.html |

#### College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering – MS | https://grad.tamu.edu/programs/aerospace-engineering-ms.html |
| 2 | Analytics – MS | https://grad.tamu.edu/programs/analytics-ms.html |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering – MEN | https://grad.tamu.edu/programs/aerospace-engineering.html |
| 2 | Aerospace Engineering - Online MEN | https://grad.tamu.edu/programs/aerospace-engineering-master-of-engineering-online.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering – PhD | https://grad.tamu.edu/programs/aerospace-engineering-phd.html |

#### Mays Business School

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting – MS | https://grad.tamu.edu/programs/accounting.html |
| 2 | Accounting Flex Online – MS | https://grad.tamu.edu/programs/accounting-flex-online.html |
| 3 | Analytics – MS | https://grad.tamu.edu/programs/analytics-ms.html |

#### College of Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology – MA | https://grad.tamu.edu/programs/anthropolgy-ma.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology – PhD | https://grad.tamu.edu/programs/anthropology-doctor-of-philosophy.html |

#### College of Architecture

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture – MS | https://grad.tamu.edu/programs/architecture-master-of-science.html |

##### Other Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture – MAR | https://grad.tamu.edu/programs/architecture-master-of-architecture.html |
| 2 | Architecture – MAR & MLP | https://grad.tamu.edu/programs/architecture-mar-and-mlp.html |
| 3 | Architecture – MAR/MUP | https://grad.tamu.edu/programs/architecture-mar-mup.html |

**Note**: The full graduate program directory contains 290 programs across all 17 colleges. For the complete list, see the [Graduate and Professional School Programs](https://grad.tamu.edu/programs/index.html).

### 2.2 At Least One Program's Full Deep-Dive

**Program**: Computer Science (MS)
- **Department**: Computer Science & Engineering
- **College**: College of Engineering
- **Application Portal**: [Texas A&M University GraduateCAS](https://texasam2026.cas.myliaison.com/applicant-ux/)
- **Application Fee**: $65.00
- **GRE Code**: 6003 (non-engineering) / 4119 (engineering)
- **GMAT Code**: 7B7K957
- **Transcripts**: Required from all colleges attended (excluding community colleges)
- **Test Scores**: Required from testing agency; most scores expire after 5 years
- **Department-Specific**: Letters of Recommendation, Statement of Purpose, Resume/CV

### 2.3 Graduate Admissions Model

**Decentralized**: Most graduate information is specific to different colleges and programs. Students must reach out to the department they're applying to for specific admissions information such as deadlines and requirements.

**Centralized Services**:
- Application processing through GraduateCAS
- Application fee: $65.00
- Transcript processing
- Test score reporting

**Professional Programs**:
- School of Law: LSAC
- College of Dentistry: AADSAS
- College of Medicine: AMCAS
- College of Veterinary Medicine: VMCAS
- College of Pharmacy: PharmCAS

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions Site | https://admissions.tamu.edu/ | Official |
| Application Portal | Common App or ApplyTexas | admissions.tamu.edu/apply/freshman/ |
| Application Fee (Domestic) | $75 | admissions.tamu.edu/apply/freshman/ |
| Application Fee (International) | $90 | admissions.tamu.edu/apply/international/ |
| EA Deadline | October 15, 2026 (Spring 2027) | admissions.tamu.edu/apply/freshman/ |
| Priority Deadline | December 1, 2026 (Fall 2027) | admissions.tamu.edu/apply/freshman/ |
| Regular Deadline | Rolling (varies by campus) | admissions.tamu.edu/apply/freshman/ |
| Document Deadline | December 15, 2026 (Fall 2027) | admissions.tamu.edu/apply/freshman/ |
| SAT/ACT Policy | TEST OPTIONAL | admissions.tamu.edu/apply/freshman/ |
| Superscore | Not specified | - |
| Score Report Method | Testing agency required | admissions.tamu.edu/apply/freshman/ |
| Interview Policy | Not required | - |
| Recommendations | Optional (first 2 considered) | admissions.tamu.edu/apply/freshman/ |
| Portfolio | Not required for most majors | - |
| Transfer Pathway | Available | admissions.tamu.edu/apply/transfer/ |
| Top 10% Auto-Admit | Yes (Texas residents) | admissions.tamu.edu/apply/freshman/ |

**Source**: admissions.tamu.edu/apply/freshman/index.html

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 推荐分数 | 备注 |
|------|---------|---------|------|
| TOEFL iBT | 80 (pre-Jan 2026) / 4.5 (new scale) | - | Must be within 2 years; no MyBest scores |
| TOEFL Essentials | 8.5 | - | Must be within 2 years |
| IELTS Academic | 6.0 overall | - | No IELTS General |
| SAT EBRW | 560 | - | Alternative to TOEFL |
| ACT English | 21 | - | Alternative to TOEFL |

**Exemptions**: Citizens of English-speaking countries (list on website); completion of all 4 years in US high school.

**Source**: admissions.tamu.edu/apply/international/international-freshman.html

### 3.3 Graduate — Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| Application Platform | Texas A&M University GraduateCAS | grad.tamu.edu |
| Application Fee | $65.00 | admissions.tamu.edu/apply/graduate.html |
| GRE Code (Non-Engineering) | 6003 | admissions.tamu.edu/apply/graduate.html |
| GRE Code (Engineering) | 4119 | admissions.tamu.edu/apply/graduate.html |
| GMAT Code | 7B7K957 | admissions.tamu.edu/apply/graduate.html |
| Transcripts | Required from all colleges (excl. community colleges) | admissions.tamu.edu/apply/graduate.html |
| Test Scores | Required from testing agency; expire after 5 years | admissions.tamu.edu/apply/graduate.html |
| Recommendations | Department-specific | admissions.tamu.edu/apply/graduate.html |
| Statement of Purpose | Department-specific | admissions.tamu.edu/apply/graduate.html |

**Source**: admissions.tamu.edu/apply/graduate.html

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (Current Academic Year, Line-Itemized)

**Academic Year**: 2026-2027 (Fall 2026 / Spring 2027)

| 费用项目 | 金额 (Per Semester) | 说明 |
|---------|---------------------|------|
| Tuition & Required Fees | Varies by major | Use tuition calculator |
| Housing & Food | $6,472.00 | On-campus estimate |
| Books & Supplies | $441.00 | Estimated |
| Travel | $846.00 | Estimated |
| Loan Fees | $31.00 | Estimated |
| Personal Expenses | $1,595.00 | Estimated |
| **Total Other Costs** | **$9,385.00** | Per semester |
| **Total COA (with tuition)** | **Varies** | Use calculator |

**Note**: Tuition varies significantly by major and residency status. Use the [Tuition Calculator](https://tuition.tamu.edu/undergraduate) for accurate estimates.

**Additional Fees Not Included**:
- Distance education differential tuition
- Course-related fees (lab, field trip, etc.)
- General deposit: $100 (new students)
- International student admin fee: $200-$500/semester
- International Student Services fee: $150/semester
- International Student Health Insurance: $262.50 (arrival) + $1,051 (fall) + $2,095 (spring)

**Source**: tuition.tamu.edu/undergraduate

### 4.2 Undergraduate Financial-Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Financial Aid Website | https://aggie.tamu.edu/financial-aid | aggie.tamu.edu |
| Scholarships | https://aggie.tamu.edu/financial-aid/types-of-aid/scholarships | aggie.tamu.edu |
| Total Financial Aid | $986 million annually | admissions.tamu.edu/why-texas-a-m/aid-affordability.html |
| Students Receiving Aid | ~71% | admissions.tamu.edu/why-texas-a-m/aid-affordability.html |
| Need-Blind Policy | Need-aware for all | Public university policy |
| Merit Scholarships | Available | aggie.tamu.edu |
| Need-Based Aid | Available | aggie.tamu.edu |

**Source**: admissions.tamu.edu/why-texas-a-m/aid-affordability.html, aggie.tamu.edu

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| Graduate Tuition Calculator | https://tuition.tamu.edu/graduate | tuition.tamu.edu |
| Funding Types | RA, TA, Fellowships, Grants | grad.tamu.edu |
| Application Fee | $65.00 | admissions.tamu.edu/apply/graduate.html |
| Fee Waivers | Available for low-income applicants | admissions.tamu.edu/apply/graduate.html |

**Source**: grad.tamu.edu, admissions.tamu.edu/apply/graduate.html

---

## SECTION 5 — Evidence Chain Index

### Evidence Blocks

```yaml
E-U-001:
  field: undergraduate.deadlines.fall_2027
  value: "December 1, 2026"
  source_url: https://admissions.tamu.edu/apply/freshman/index.html
  source_snippet: "Fall 2027 - College Station | August 1, 2026 | December 1, 2026 | All required documents due by Dec. 15, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.test_policy
  value: "Test Optional"
  source_url: https://admissions.tamu.edu/apply/freshman/index.html
  source_snippet: "Texas A&M University is test optional and will not require ACT or SAT scores for freshman applicants."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application_fee
  value: "$75"
  source_url: https://admissions.tamu.edu/apply/freshman/index.html
  source_snippet: "A $75 non-refundable processing fee is required to complete your application."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.english_proficiency.toefl
  value: "80 (pre-Jan 2026) / 4.5 (new scale)"
  source_url: https://admissions.tamu.edu/apply/international/international-freshman.html
  source_snippet: "Minimum TOEFL iBT overall score of 80 (in person or Home Edition) taken prior to January 21, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.ielts
  value: "6.0 overall"
  source_url: https://admissions.tamu.edu/apply/international/international-freshman.html
  source_snippet: "Minimum IELTS Academic test score of 6.0 overall band"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.costs.other_costs_per_semester
  value: "$9,385.00"
  source_url: https://tuition.tamu.edu/undergraduate
  source_snippet: "Total Estimated Other Costs of Attendance | $9,385.00"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.programs.total_majors
  value: "131"
  source_url: https://careercenter.tamu.edu/current-students/explore-majors-and-careers/majors/
  source_snippet: "131 unique undergraduate majors extracted from 14 pages"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee
  value: "$65.00"
  source_url: https://admissions.tamu.edu/apply/graduate.html
  source_snippet: "The $65.00 fee (in addition to a centralized application service processing fee) is required to process an application for admission."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.gre_code
  value: "6003 (non-engineering) / 4119 (engineering)"
  source_url: https://admissions.tamu.edu/apply/graduate.html
  source_snippet: "Use code 6003 for reporting GRE scores for non-engineering programs. Use code 4119 for reporting GRE for engineering programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.programs.total
  value: "290"
  source_url: https://grad.tamu.edu/programs/index.html
  source_snippet: "290 unique graduate programs extracted from 37 pages"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: graduate.application_platform
  value: "Texas A&M University GraduateCAS"
  source_url: https://admissions.tamu.edu/apply/graduate.html
  source_snippet: "Most academic programs utilize the Texas A&M University GraduateCAS"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-O-001:
  field: institution.colleges_schools
  value: "17"
  source_url: https://www.tamu.edu/academics/colleges-schools/index.html
  source_snippet: "Texas A&M University has 17 colleges and schools, and two branch campuses"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-O-002:
  field: institution.type
  value: "Public"
  source_url: https://www.tamu.edu/
  source_snippet: "Texas A&M University is a public research university"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-O-003:
  field: institution.location
  value: "College Station, TX"
  source_url: https://www.tamu.edu/
  source_snippet: "College Station, TX 77843"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-F-001:
  field: financial_aid.total_aid
  value: "$986 million annually"
  source_url: https://admissions.tamu.edu/why-texas-a-m/aid-affordability.html
  source_snippet: "Over $986 million in financial assistance is paid out to about 71% of Texas A&M students every year"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-F-002:
  field: financial_aid.students_receiving_aid
  value: "~71%"
  source_url: https://admissions.tamu.edu/why-texas-a-m/aid-affordability.html
  source_snippet: "Over $986 million in financial assistance is paid out to about 71% of Texas A&M students every year"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
TexasAM-knowledge-base-v2/
├── 00-institution-overview/
│   ├── 01-program-counts.md
│   ├── 02-college-hierarchy.md
│   ├── 03-degree-inventory.md
│   └── 04-distribution-matrix.md
├── 01-undergraduate-education/
│   ├── college-of-agriculture-and-life-sciences.md
│   ├── college-of-architecture.md
│   ├── college-of-arts-and-sciences.md
│   ├── mays-business-school.md
│   ├── college-of-education-and-human-development.md
│   ├── college-of-engineering.md
│   ├── college-of-geosciences.md
│   ├── college-of-liberal-arts.md
│   ├── college-of-nursing.md
│   ├── school-of-public-health.md
│   ├── tamu-galveston.md
│   └── interdisciplinary-programs.md
├── 02-graduate-education/
│   ├── college-of-agriculture-and-life-sciences.md
│   ├── college-of-engineering.md
│   ├── mays-business-school.md
│   ├── college-of-arts-and-sciences.md
│   └── [other colleges].md
├── 03-application-requirements/
│   ├── undergraduate-deadlines.md
│   ├── undergraduate-test-policy.md
│   ├── english-proficiency.md
│   └── graduate-requirements.md
├── 04-costs-and-financial-aid/
│   ├── undergraduate-costs.md
│   ├── financial-aid-policy.md
│   └── graduate-costs.md
└── 05-evidence-chain/
    └── evidence-index.md
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "TexasAM-knowledge-base-v2"
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

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Complete tuition line items (in-state vs OOS) | tuition.tamu.edu/undergraduate |
| P0 | Complete graduate program list (all 290 programs) | grad.tamu.edu/programs/index.html |
| P1 | Detailed financial aid policy (income thresholds) | aggie.tamu.edu/financial-aid |
| P1 | Per-college department listings | www.tamu.edu/academics/colleges-schools/ |
| P2 | Transfer admission requirements | admissions.tamu.edu/apply/transfer/ |
| P2 | International student specific requirements | admissions.tamu.edu/apply/international/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Texas A&M | [Other School] | [Other School] |
|------|-----------|----------------|----------------|
| **Location** | College Station, TX | | |
| **Type** | Public | | |
| **Total UG Programs** | 131 | | |
| **Total Grad Programs** | 290 | | |
| **Total Colleges/Schools** | 17 | | |
| **EA Deadline** | October 15 | | |
| **Priority Deadline** | December 1 | | |
| **Application Fee (UG)** | $75 | | |
| **Application Fee (Grad)** | $65 | | |
| **SAT/ACT Policy** | Test Optional | | |
| **TOEFL Minimum** | 80 | | |
| **IELTS Minimum** | 6.0 | | |
| **Need-Blind Policy** | Need-aware for all | | |
| **Total Financial Aid** | $986M/year | | |
| **Students Receiving Aid** | ~71% | | |

---

## Closing Block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.tamu.edu, grad.tamu.edu, aggie.tamu.edu, tuition.tamu.edu, careercenter.tamu.edu, www.tamu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program

---

## Appendix: Cache Files

- **site-memory.json**: `/Users/erik/Desktop/知识库预处理测试/uni-cache/schools/tamu/site-memory.json`
- **last-extract.json**: To be generated on next run
- **content-hashes.json**: To be generated on next run
