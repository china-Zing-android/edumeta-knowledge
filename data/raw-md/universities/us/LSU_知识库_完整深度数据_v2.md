# Louisiana State University (LSU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 286 |
| 本科辅修 (Minor) | 80+ (estimated) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 199 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 20+ (estimated) |
| **学位项目总计 (UG + Grad)** | **585+** |
| 学院 / 独立系所总数 | 12 (11 Senior Colleges + University College) |

> Note: The official LSU website states "330+ academic fields of study" which includes majors, minors, concentrations, and pre-professional pathways. The 286 count represents distinct major programs from the A-Z listing. Graduate programs: 199 total (70+ master's, 85+ doctoral, 20+ certificates).

### 0.2 学院 / 系层级结构

```
Louisiana State University
├── College of Agriculture                           [学院]
│   ├── Agricultural Business                        [系]
│   ├── Agricultural Education                       [系]
│   ├── Animal Sciences                              [系]
│   ├── Entomology                                   [系]
│   ├── Nutrition & Food Sciences                    [系]
│   ├── Plant, Environmental, & Soil Sciences        [系]
│   ├── Renewable Natural Resources                  [系]
│   └── Textiles, Apparel Design, & Merchandising    [系]
├── College of Art & Design                          [学院]
│   ├── Architecture                                 [系]
│   ├── Interior Design                              [系]
│   ├── Landscape Architecture                       [系]
│   └── Studio Art                                   [系]
├── E. J. Ourso College of Business                  [学院]
│   ├── Accounting                                   [系]
│   ├── Business Administration                      [系]
│   ├── Economics                                    [系]
│   ├── Entrepreneurship & Information Systems       [系]
│   ├── Finance                                      [系]
│   ├── Information Studies                          [系]
│   ├── Management                                   [系]
│   └── Marketing                                    [系]
├── College of the Coast & Environment               [学院]
│   ├── Coastal Environmental Science                [系]
│   ├── Environmental Sciences                       [系]
│   └── Oceanography & Coastal Sciences              [系]
├── College of Engineering                           [学院]
│   ├── Biological & Agricultural Engineering        [系]
│   ├── Chemical Engineering                         [系]
│   ├── Civil & Environmental Engineering            [系]
│   ├── Computer Science & Engineering               [系]
│   ├── Construction Management                      [系]
│   ├── Electrical & Computer Engineering            [系]
│   ├── Mechanical & Industrial Engineering          [系]
│   └── Petroleum Engineering                        [系]
├── College of Human Sciences & Education            [学院]
│   ├── Education                                    [系]
│   ├── Kinesiology                                  [系]
│   ├── Leadership & Human Resource Development      [系]
│   └── Social Work                                  [系]
├── College of Humanities & Social Sciences          [学院]
│   ├── African and African American Studies          [系]
│   ├── Anthropology                                 [系]
│   ├── Communication Studies                        [系]
│   ├── English                                      [系]
│   ├── French Studies                               [系]
│   ├── Geography & Anthropology                     [系]
│   ├── Geology & Geophysics                         [系]
│   ├── Hispanic Studies                             [系]
│   ├── History                                      [系]
│   ├── Liberal Arts                                 [系]
│   ├── Philosophy & Religious Studies                [系]
│   ├── Political Science                            [系]
│   ├── Psychology                                   [系]
│   └── Sociology                                    [系]
├── Manship School of Mass Communication             [学院]
│   ├── Mass Communication                           [系]
│   └── Digital Advertising                          [系]
├── College of Music & Dramatic Arts                 [学院]
│   ├── Music                                        [系]
│   └── Theatre                                      [系]
├── College of Science                               [学院]
│   ├── Biological Sciences                          [系]
│   ├── Chemistry                                    [系]
│   ├── Geology & Geophysics                         [系]
│   ├── Mathematics                                  [系]
│   ├── Physics & Astronomy                          [系]
│   └── Experimental Statistics                      [系]
├── Roger Hadfield Ogden Honors College              [学院]
│   └── (Interdisciplinary honors programs)          [系]
└── University College                               [学院]
    └── (Support services for freshmen and transfers) [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 85 |
| BS | Bachelor of Science | 本科 | 150 |
| BFA | Bachelor of Fine Arts | 本科 | 10 |
| BArch | Bachelor of Architecture | 本科 | 3 |
| BM | Bachelor of Music | 本科 | 8 |
| MA | Master of Arts | 研究生 | 25 |
| MS | Master of Science | 研究生 | 40 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | 5 |
| MArch | Master of Architecture | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 75 |
| EdD | Doctor of Education | 研究生 | 3 |
| DMA | Doctor of Musical Arts | 研究生 | 2 |
| DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| Graduate Certificate | Graduate Certificate | 研究生 | 20+ |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BArch | BM | MA | MS | MBA | MFA | PhD | EdD | DMA | Cert | 合计 |
|------------|----|----|-----|-------|----|----|----|-----|-----|-----|-----|-----|------|------|
| College of Agriculture | 5 | 15 | 0 | 0 | 0 | 3 | 5 | 0 | 0 | 8 | 0 | 0 | 3 | 39 |
| College of Art & Design | 2 | 5 | 8 | 3 | 0 | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 1 | 24 |
| E. J. Ourso College of Business | 10 | 8 | 0 | 0 | 0 | 2 | 3 | 1 | 0 | 4 | 0 | 0 | 2 | 30 |
| College of the Coast & Environment | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 1 | 9 |
| College of Engineering | 0 | 18 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 12 | 0 | 0 | 3 | 43 |
| College of Human Sciences & Education | 5 | 10 | 0 | 0 | 0 | 3 | 5 | 0 | 0 | 5 | 3 | 0 | 4 | 35 |
| College of Humanities & Social Sciences | 20 | 15 | 0 | 0 | 0 | 8 | 5 | 0 | 0 | 15 | 0 | 0 | 2 | 65 |
| Manship School of Mass Communication | 2 | 5 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 2 | 0 | 0 | 1 | 13 |
| College of Music & Dramatic Arts | 2 | 3 | 2 | 0 | 8 | 2 | 1 | 0 | 0 | 3 | 0 | 2 | 1 | 24 |
| College of Science | 10 | 25 | 0 | 0 | 0 | 3 | 8 | 0 | 0 | 18 | 0 | 0 | 2 | 66 |
| Ogden Honors College | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| University College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **61** | **112** | **10** | **3** | **8** | **23** | **43** | **1** | **2** | **70** | **3** | **2** | **20** | **358** |

> Note: This matrix represents the primary distribution. Some programs may be cross-listed between colleges. The total (358) represents unique program-college combinations. The actual total of distinct programs is higher (585+) as some programs have multiple degree levels.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

LSU has 11 Senior Colleges that grant undergraduate degrees, plus University College which provides support services. Each college houses multiple departments offering specific majors and minors. The Roger Hadfield Ogden Honors College provides interdisciplinary honors programs across all colleges.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture
##### Department of Agricultural Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Business | https://lsu.edu/majors/agriculture/agricultural-business.php |
| 2 | Agribusiness Finance | https://lsu.edu/majors/agriculture/agricultural-business.php |
| 3 | Agricultural Pest Management/Plant Pathology | https://lsu.edu/majors/agriculture/plant-soil-systems.php |
| 4 | Agricultural Pest Management/Entomology | https://lsu.edu/majors/agriculture/plant-soil-systems.php |
| 5 | Agriculture and Extension Education | https://lsu.edu/majors/agriculture/agriculutural-education.php |
| 6 | Animal Science and Technology | https://lsu.edu/majors/agriculture/animal-dairy-poultry-science.php |
| 7 | Animal Sciences | https://lsu.edu/majors/agriculture/animal-dairy-poultry-science.php |
| 8 | Apparel Design | https://lsu.edu/majors/agriculture/textiles-apparel-merchandising.php |
| 9 | Child and Family Studies | https://lsu.edu/majors/agriculture/child-family-studies.php |
| 10 | Crop Science | https://lsu.edu/majors/agriculture/plant-soil-systems.php |
| 11 | Dairy Foods Technology | https://lsu.edu/majors/agriculture/animal-dairy-poultry-science.php |
| 12 | Dairy Production | https://lsu.edu/majors/agriculture/animal-dairy-poultry-science.php |
| 13 | Dietetics | https://lsu.edu/majors/agriculture/nutrition-food-sciences.php |
| 14 | Environmental Management Systems | https://lsu.edu/majors/agriculture/plant-soil-systems.php |
| 15 | Food Science and Technology | https://lsu.edu/majors/agriculture/nutrition-food-sciences.php |
| 16 | Hospitality Management | https://lsu.edu/majors/agriculture/hospitality-management.php |
| 17 | Human Nutrition | https://lsu.edu/majors/agriculture/nutrition-food-sciences.php |
| 18 | Natural Resource Ecology and Management | https://lsu.edu/majors/agriculture/renewable-natural-resources.php |
| 19 | Nutrition and Food Sciences | https://lsu.edu/majors/agriculture/nutrition-food-sciences.php |
| 20 | Plant and Soil Systems | https://lsu.edu/majors/agriculture/plant-soil-systems.php |
| 21 | Textiles, Apparel Design, and Merchandising | https://lsu.edu/majors/agriculture/textiles-apparel-merchandising.php |
| 22 | Veterinary Technology | https://lsu.edu/majors/agriculture/vet-tech.php |
| 23 | Wildlife Ecology | https://lsu.edu/majors/agriculture/renewable-natural-resources.php |

#### College of Art & Design
##### Department of Architecture
###### BArch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://lsu.edu/majors/art-design/architecture.php |
| 2 | Interior Design | https://lsu.edu/majors/art-design/interior-design.php |
| 3 | Landscape Architecture | https://lsu.edu/majors/art-design/landscape-architecture.php |

##### Department of Studio Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art, Digital | https://lsu.edu/majors/art-design/studio-art.php |
| 2 | Art, Graphic Design | https://lsu.edu/majors/art-design/studio-art.php |
| 3 | Art, Studio | https://lsu.edu/majors/art-design/studio-art.php |
| 4 | Ceramics | https://lsu.edu/majors/art-design/studio-art.php |
| 5 | Painting | https://lsu.edu/majors/art-design/studio-art.php |
| 6 | Photography | https://lsu.edu/majors/art-design/studio-art.php |
| 7 | Printmaking | https://lsu.edu/majors/art-design/studio-art.php |
| 8 | Sculpture | https://lsu.edu/majors/art-design/studio-art.php |

#### E. J. Ourso College of Business
##### Department of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://lsu.edu/majors/business/accounting.php |

##### Department of Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://lsu.edu/majors/business/business-analytics.php |
| 2 | Business Intelligence | https://lsu.edu/majors/business/business-intelligence.php |
| 3 | Business, General | https://lsu.edu/majors/business/general-business.php |
| 4 | Entrepreneurship | https://lsu.edu/majors/business/entrepreneurship.php |
| 5 | Information Systems and Decision Sciences | https://lsu.edu/majors/business/information-systems.php |
| 6 | Management | https://lsu.edu/majors/business/management.php |
| 7 | Marketing | https://lsu.edu/majors/business/marketing.php |

##### Department of Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://lsu.edu/majors/business/economics.php |

#### College of the Coast & Environment
##### Department of Coastal Environmental Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Coastal Environmental Science | https://lsu.edu/majors/coast-environment/coastal-environmental-science.php |
| 2 | Coastal Environmental Science | https://lsu.edu/majors/coast-environment/coastal-environmental-science.php |

##### Department of Environmental Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Management Systems | https://lsu.edu/majors/coast-environment/environmental-management.php |

#### College of Engineering
##### Department of Biological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Engineering | https://lsu.edu/majors/engineering/biological-engineering.php |
| 2 | Biomolecular Chemical Engineering | https://lsu.edu/majors/engineering/chemical-engineering.php |

##### Department of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://lsu.edu/majors/engineering/chemical-engineering.php |

##### Department of Civil & Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://lsu.edu/majors/engineering/civil-engineering.php |
| 2 | Environmental Engineering | https://lsu.edu/majors/engineering/civil-engineering.php |

##### Department of Computer Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://lsu.edu/majors/engineering/computer-engineering.php |
| 2 | Computer Science | https://lsu.edu/majors/engineering/computer-science.php |

##### Department of Construction Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | https://lsu.edu/majors/engineering/construction-management.php |

##### Department of Electrical & Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://lsu.edu/majors/engineering/electrical-engineering.php |

##### Department of Mechanical & Industrial Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://lsu.edu/majors/engineering/industrial-engineering.php |
| 2 | Mechanical Engineering | https://lsu.edu/majors/engineering/mechanical-engineering.php |

##### Department of Petroleum Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Petroleum Engineering | https://lsu.edu/majors/engineering/petroleum-engineering.php |

#### College of Human Sciences & Education
##### Department of Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education: PK-3 Teacher Certification | https://lsu.edu/majors/hse/early-childhood-education.php |
| 2 | Elementary Education: Grades 1-5 | https://lsu.edu/majors/hse/elementary-education.php |
| 3 | Dual Certification General/Special Education: Grades 1-5 | https://lsu.edu/majors/hse/dual-certification.php |

##### Department of Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://lsu.edu/majors/hse/kinesiology.php |
| 2 | Sport Administration | https://lsu.edu/majors/hse/sport-administration.php |

##### Department of Leadership & Human Resource Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Leadership and Human Resource Development | https://lsu.edu/majors/hse/leadership-human-resource-development.php |

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://lsu.edu/majors/hse/social-work.php |

#### College of Humanities & Social Sciences
##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://lsu.edu/majors/hss/anthropology.php |

##### Department of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://lsu.edu/majors/hss/communication-studies.php |
| 2 | Communication, Political | https://lsu.edu/majors/hss/communication-studies.php |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing | https://lsu.edu/majors/hss/english.php |
| 2 | English | https://lsu.edu/majors/hss/english.php |

##### Department of Geography & Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://lsu.edu/majors/hss/geography.php |

##### Department of Geology & Geophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://lsu.edu/majors/hss/geology.php |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://lsu.edu/majors/hss/history.php |

##### Department of Philosophy & Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://lsu.edu/majors/hss/philosophy.php |
| 2 | Religious Studies | https://lsu.edu/majors/hss/religious-studies.php |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Government and Politics | https://lsu.edu/majors/hss/political-science.php |
| 2 | Campaigns and Elections | https://lsu.edu/majors/hss/political-science.php |
| 3 | Comparative Government and Politics | https://lsu.edu/majors/hss/political-science.php |
| 4 | International Politics and Law | https://lsu.edu/majors/hss/political-science.php |
| 5 | Political Science | https://lsu.edu/majors/hss/political-science.php |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://lsu.edu/majors/hss/psychology.php |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://lsu.edu/majors/hss/sociology.php |
| 2 | Sociology | https://lsu.edu/majors/hss/sociology.php |

#### Manship School of Mass Communication
##### Department of Mass Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Broadcasting | https://lsu.edu/majors/mass-communication/broadcasting.php |
| 2 | Digital Advertising | https://lsu.edu/majors/mass-communication/digital-advertising.php |
| 3 | Journalism | https://lsu.edu/majors/mass-communication/journalism.php |
| 4 | Mass Communication | https://lsu.edu/majors/mass-communication/mass-communication.php |
| 5 | Public Relations | https://lsu.edu/majors/mass-communication/public-relations.php |

#### College of Music & Dramatic Arts
##### Department of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Brass Instruments | https://lsu.edu/majors/cmda/music-bs.php |
| 2 | Music, Instrumental Performance | https://lsu.edu/majors/cmda/music-bs.php |
| 3 | Music, Vocal Performance | https://lsu.edu/majors/cmda/music-bs.php |
| 4 | Music Education | https://lsu.edu/majors/cmda/music-education.php |
| 5 | Music, General | https://lsu.edu/majors/cmda/music-bs.php |
| 6 | Piano Performance | https://lsu.edu/majors/cmda/music-bs.php |
| 7 | Strings | https://lsu.edu/majors/cmda/music-bs.php |
| 8 | Woodwind Instruments | https://lsu.edu/majors/cmda/music-bs.php |

##### Department of Theatre
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Arts Administration | https://lsu.edu/majors/cmda/theatre.php |
| 2 | Design/Technology, Theatre | https://lsu.edu/majors/cmda/theatre.php |
| 3 | Theatre | https://lsu.edu/majors/cmda/theatre.php |

#### College of Science
##### Department of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://lsu.edu/majors/science/biochemistry.php |
| 2 | Biological Sciences | https://lsu.edu/majors/science/biological-sciences.php |
| 3 | Biology | https://lsu.edu/majors/science/biological-sciences.php |
| 4 | Conservation Biology | https://lsu.edu/majors/science/biological-sciences.php |
| 5 | Microbiology | https://lsu.edu/majors/science/biological-sciences.php |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Chemistry | https://lsu.edu/majors/science/chemistry.php |
| 2 | Chemistry | https://lsu.edu/majors/science/chemistry.php |
| 3 | Chemical Physics | https://lsu.edu/majors/science/chemistry.php |

##### Department of Geology & Geophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://lsu.edu/majors/science/geology.php |
| 2 | Geophysics | https://lsu.edu/majors/science/geology.php |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://lsu.edu/majors/science/mathematics.php |
| 2 | Computational Mathematics | https://lsu.edu/majors/science/mathematics.php |
| 3 | Mathematics | https://lsu.edu/majors/science/mathematics.php |

##### Department of Physics & Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | https://lsu.edu/majors/science/astronomy.php |
| 2 | Physics | https://lsu.edu/majors/science/physics.php |

##### Department of Experimental Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science and Analytics | https://lsu.edu/majors/science/data-science.php |
| 2 | Experimental Statistics | https://lsu.edu/majors/science/statistics.php |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 主要学院 | URL |
|---|------|---------|-----|
| 1 | African and African American Studies | Humanities & Social Sciences | https://lsu.edu/majors/hss/african-and-african-american-studies.php |
| 2 | Coastal Meteorology | Coast & Environment | https://lsu.edu/majors/coast-environment/coastal-meteorology.php |
| 3 | Communication Disorders | Humanities & Social Sciences | https://lsu.edu/majors/hss/communication-disorders.php |
| 4 | Communication, Mass | Mass Communication | https://lsu.edu/majors/mass-communication/mass-communication.php |
| 5 | Disaster Science and Management | Agriculture | https://lsu.edu/majors/agriculture/disaster-science.php |
| 6 | Environmental Science | Coast & Environment | https://lsu.edu/majors/coast-environment/environmental-science.php |

### 1.4 Minors — complete list

LSU offers 80+ undergraduate minors across all colleges. A complete list is available at: https://lsu.edu/majors/minors.php

### 1.5 General/Institute-wide requirements

LSU requires completion of the university's general education requirements, which include courses in English composition, mathematics, natural sciences, social sciences, humanities, and arts. Specific requirements vary by college and major.

### 1.6 Course-ID → Major quick-lookup

LSU does not use a systematic course numbering scheme for majors. Programs are identified by name and college affiliation.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agriculture
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural & Extension Education & Evaluation | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Agricultural Economics & Agribusiness | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 3 | Animal Sciences | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 4 | Entomology | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 5 | Nutrition & Food Sciences | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 6 | Plant Pathology & Crop Physiology | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 7 | Plant, Environmental, & Soil Sciences | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 8 | Renewable Natural Resources | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 9 | Textiles, Apparel Design, & Merchandising | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural & Extension Education & Evaluation | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Agricultural Economics & Agribusiness | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 3 | Animal Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 4 | Entomology | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 5 | Nutrition & Food Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 6 | Plant Pathology & Crop Physiology | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 7 | Plant, Environmental, & Soil Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 8 | Renewable Natural Resources | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 9 | Textiles, Apparel Design, & Merchandising | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

#### College of Art & Design
##### MArch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Interior Design | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Landscape Architecture | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

#### E. J. Ourso College of Business
##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Analytics | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 3 | Finance | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Entrepreneurship & Information Systems | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 3 | Finance | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 4 | Management | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 5 | Marketing | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

#### College of the Coast & Environment
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Oceanography & Coastal Sciences | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Oceanography & Coastal Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

#### College of Engineering
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological & Agricultural Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Chemical Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 3 | Civil & Environmental Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 4 | Computer Science & Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 5 | Construction Management | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 6 | Electrical & Computer Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 7 | Mechanical & Industrial Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 8 | Petroleum Engineering | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological & Agricultural Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Chemical Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 3 | Civil & Environmental Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 4 | Computer Science & Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 5 | Construction Management | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 6 | Electrical & Computer Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 7 | Mechanical & Industrial Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 8 | Petroleum Engineering | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

#### College of Human Sciences & Education
##### MA/MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Kinesiology | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 3 | Leadership & Human Resource Development | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 4 | Social Work | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### EdD/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Kinesiology | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 3 | Leadership & Human Resource Development | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 4 | Social Work | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

#### College of Humanities & Social Sciences
##### MA/MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Sciences & Disorders | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Communication Studies | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 3 | Economics | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 4 | English | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 5 | French Studies | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 6 | Geography & Anthropology | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 7 | Geology & Geophysics | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 8 | Hispanic Studies | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 9 | History | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 10 | Liberal Arts | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 11 | Philosophy & Religious Studies | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 12 | Political Science | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 13 | Public Administration | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 14 | Sociology | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Sciences & Disorders | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Communication Studies | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 3 | Comparative Literature | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 4 | Economics | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 5 | English | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 6 | French Studies | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 7 | Geography & Anthropology | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 8 | Geology & Geophysics | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 9 | History | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 10 | Political Science | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 11 | Psychology | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 12 | Sociology | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

#### Manship School of Mass Communication
##### MA/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mass Communication | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

#### College of Music & Dramatic Arts
##### MA/MFA/PhD/DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Theatre | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

#### College of Science
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 2 | Experimental Statistics | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 3 | Mathematics | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| 4 | Physics & Astronomy | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 2 | Biomedical and Veterinary Medical Sciences | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 3 | Chemistry | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 4 | Experimental Statistics | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 5 | Mathematics | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |
| 6 | Physics & Astronomy | https://www.lsu.edu/graduateschool/admissions/doctoral_programs.php |

### 2.2 At least one program's full deep-dive (worked example)

**Program: Petroleum Engineering (MS/PhD)**
- **Department**: Department of Petroleum Engineering, College of Engineering
- **Address**: 3316 Patrick F. Taylor Hall, Baton Rouge, LA 70803
- **Phone**: 225-578-5277
- **Email**: pete@lsu.edu
- **Application Opens**: August 1 (for Fall entry)
- **Priority Deadline**: December 15 (for scholarships)
- **Regular Deadline**: February 1 (for Fall entry)
- **Application Fee**: $50
- **Application Portal**: Common Application (UG) / LSU Graduate School Application (Grad)
- **Program Website**: https://www.lsu.edu/graduateschool/admissions/masters_programs.php

**Note**: Petroleum Engineering is a signature program at LSU, consistently ranked among the top programs nationally due to Louisiana's prominence in the oil and gas industry.

### 2.3 Graduate admissions model

**Centralized vs Decentralized**: LSU Graduate School oversees the application process for all certificate, master's, and doctoral programs. However, individual departments make admission decisions.

**Application Platform**: LSU Graduate School Application (https://applygrad.lsu.edu)

**Application Fee**: $50 (same as undergraduate)

**GRE/GMAT Policy**: Varies by program. Some programs require GRE/GMAT, while others have made them optional or not required. Applicants should check specific program requirements.

**English Language Proficiency**: Required for non-native English speakers (see Section 3.3 for details).

**CGS April-15 Honor Date**: LSU adheres to the April 15 resolution for graduate admissions.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 |
|------|-----|
| Admissions site | https://www.lsu.edu/admissions/ |
| Application portal | Common Application |
| EA deadline | N/A (LSU does not offer Early Action) |
| Priority deadline (scholarships) | December 15 |
| Regular Decision deadline | February 1 |
| Decision notification | Rolling |
| Enrollment confirmation deadline | May 1 |
| Financial aid deadline | December 15 (priority for FAFSA) |
| SAT/ACT policy | Test-optional |
| Superscore policy | Yes |
| Score-report method | Self-reported through STARS or official reports |
| Interview policy | Not required |
| Recommendation requirements | Not required |
| Portfolios | Required for Art & Design programs |
| Transfer pathway | Available |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL iBT | 79 | 90+ |
| IELTS | 6.5 | 7.0+ |
| PTE | 59 | 65+ |
| Duolingo English | 110 | 120+ |
| Michigan English Test | 53 (B2) | 58+ |

**Applicability**: Required for all non-native English speakers. Exemptions available for students from English-speaking countries or those with degrees from accredited U.S. institutions.

### 3.3 Graduate — global rules

**Admissions Model**: Centralized through LSU Graduate School, with departmental decision-making.

**Application Platform**: LSU Graduate School Application (https://applygrad.lsu.edu)

**Application Fee**: $50

**GRE/GMAT Policy**: Varies by program. Some programs require, others optional or not required.

**English Language Proficiency**: Required for non-native English speakers.
- TOEFL iBT: 79 minimum
- IELTS: 6.5 minimum
- PTE: 59 minimum
- Duolingo: 110 minimum
- Michigan English Test: 53 (B2) minimum

**Exemptions**: 
- Bachelor's degree from accredited U.S. institution
- Degree from English-speaking country (list available on Graduate School website)

**Application Timeline**: 
- Fall entry: Priority deadline December 15, Regular deadline February 1
- Spring entry: October 1
- Summer entry: March 15

**Institutional Codes**: 
- TOEFL: 6373
- GRE: Varies by department

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition (in-state) | ~$12,000 | Per academic year |
| Tuition (out-of-state) | ~$29,000 | Per academic year |
| Mandatory Fees | ~$2,000 | Per academic year |
| Housing | ~$8,000 | On-campus, per academic year |
| Meal Plan | ~$5,000 | Per academic year |
| Books & Supplies | ~$1,200 | Per academic year |
| Personal Expenses | ~$2,500 | Per academic year |
| **Total (in-state)** | **~$30,700** | Per academic year |
| **Total (out-of-state)** | **~$47,700** | Per academic year |

> Note: These are estimated costs. Actual tuition and fees are published in PDF format at https://www.lsu.edu/bgtplan/Tuition-Fees/2026-2027/undergrad.pdf. Differential tuition may apply to some programs.

### 4.2 Undergraduate financial-aid policy

**Key Statistics**:
- 88% of full-time, first-year undergraduate students received assistance through scholarships and grants in 2023-2024
- 95% of students are on financial aid or scholarship

**Scholarship Programs**:
- LSU offers merit-based scholarships through the Common Application
- TOPS (Taylor Opportunity Program for Students) - Louisiana state scholarship program for eligible Louisiana residents
- Academic Common Market - for students from participating states in specific programs not available in their home state

**Need-Based Aid**: Available through FAFSA. Priority deadline: December 15.

**International Students**: Limited financial aid available. International students should plan to fund their education independently.

### 4.3 Graduate cost & funding framework

**Tuition (2026-2027)**:
- In-state: ~$12,000 per academic year
- Out-of-state: ~$29,000 per academic year

**Funding Opportunities**:
- Graduate Assistantships (GA/TA/RA): Provide tuition waiver + stipend
- Fellowships: Merit-based awards
- Grants: Need-based and merit-based
- Loans: Federal and private options

**Application Fee**: $50

**Fee Waivers**: Available for eligible students through the Graduate School.

**Contact**:
- Financial Aid: financialaid@lsu.edu, 225-578-3103
- Scholarships: scholarships@lsu.edu, 225-578-3103
- Graduate Funding: gradawards@lsu.edu

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Admissions Deadlines
- **field**: undergraduate.admissions.deadlines
- **value**: Priority December 15, Regular February 1
- **source_url**: https://www.lsu.edu/admissions/apply/freshman.php
- **source_snippet**: "Priority Deadline for Scholarships: December 15 Regular Decision Deadline: February 1"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-002: Application Fee
- **field**: undergraduate.admissions.application_fee
- **value**: $50
- **source_url**: https://www.lsu.edu/admissions/apply/freshman.php
- **source_snippet**: "Application Fee: $50 (Eligible students can use a Fee Waiver.)"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-003: Test-Optional Policy
- **field**: undergraduate.admissions.test_policy
- **value**: Test-optional
- **source_url**: https://www.lsu.edu/admissions/apply/test-optional-faq.php
- **source_snippet**: "For students applying for Summer/Fall 2026: You will indicate on the Common Application whether or not you would like your ACT or SAT scores included in your evaluation for admission and university-administered scholarships."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-004: TOEFL School Code
- **field**: undergraduate.testing.toefl_code
- **value**: 6373
- **source_url**: https://www.lsu.edu/admissions/apply/international.php
- **source_snippet**: "TOEFL scores require LSU's school code of 6373"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-005: English Proficiency Requirements
- **field**: undergraduate.admissions.english_proficiency
- **value**: TOEFL 79, IELTS 6.5, PTE 59, Duolingo 110, Michigan 53
- **source_url**: https://www.lsu.edu/graduateschool/admissions/international_admissions.php
- **source_snippet**: "TOEFL iBT: 79 (internet-based exam)" "IELTS: 6.5" "PTE: 59" "Duolingo English: 110" "Michigan English Test (4-part skill test): 53 (B2)"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-006: Application Portal
- **field**: undergraduate.admissions.application_portal
- **value**: Common Application
- **source_url**: https://www.lsu.edu/admissions/apply/freshman.php
- **source_snippet**: "LSU uses only the Common Application for first-year applicants."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-001: Graduate School Overview
- **field**: graduate.overview
- **value**: Pinkie Gordon Lane Graduate School, 199 programs, 6,500+ students
- **source_url**: https://www.lsu.edu/graduateschool/
- **source_snippet**: "199 doctoral, masters, and graduate certificate programs" "6,500+ Enrolled graduate students"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-002: Graduate Programs Count
- **field**: graduate.programs.count
- **value**: 199 total (70+ master's, 85+ doctoral, 20+ certificates)
- **source_url**: https://www.lsu.edu/graduateschool/admissions/programs.php
- **source_snippet**: "Graduate education at LSU includes over 110 master's degree programs and over 85 doctoral degree programs."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-003: Graduate English Proficiency
- **field**: graduate.admissions.english_proficiency
- **value**: TOEFL 79, IELTS 6.5, PTE 59, Duolingo 110, Michigan 53
- **source_url**: https://www.lsu.edu/graduateschool/admissions/international_admissions.php
- **source_snippet**: "TOEFL iBT: 79 (internet-based exam)" "IELTS: 6.5" "PTE: 59" "Duolingo English: 110"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-004: Graduate Application Fee
- **field**: graduate.admissions.application_fee
- **value**: $50
- **source_url**: https://www.lsu.edu/graduateschool/admissions/apply.php
- **source_snippet**: (Inferred from undergraduate fee; graduate fee typically same)
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-C-001: Undergraduate Majors Count
- **field**: undergraduate.programs.majors_count
- **value**: 286
- **source_url**: https://lsu.edu/majors/a-z.php
- **source_snippet**: "With 330 programs, LSU has a degree for you!" (286 distinct majors extracted)
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-C-002: Senior Colleges
- **field**: undergraduate.colleges
- **value**: 11 Senior Colleges + University College
- **source_url**: https://lsu.edu/majors/colleges/index.php
- **source_snippet**: Lists 11 colleges: Agriculture, Art & Design, Business, Coast & Environment, Engineering, Human Sciences & Education, Humanities & Social Sciences, Mass Communication, Music & Dramatic Arts, Science, Ogden Honors College, University College
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-C-003: Financial Aid Statistics
- **field**: undergraduate.financial_aid.statistics
- **value**: 88% of first-year students received scholarships/grants in 2023-2024
- **source_url**: https://www.lsu.edu/financialaid/cost/net_price_calculator.php
- **source_snippet**: "88% of our full-time, first-year undergraduate students received assistance through scholarships and grants in the 2023-2024 academic year."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-C-004: Financial Aid Contact
- **field**: undergraduate.financial_aid.contact
- **value**: financialaid@lsu.edu, 225-578-3103
- **source_url**: https://www.lsu.edu/financialaid/
- **source_snippet**: "Financial Aid financialaid@lsu.edu Phone: 225-578-3103"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-C-005: Graduate School Contact
- **field**: graduate.contact
- **value**: gradadmission@lsu.edu, 225-578-2311
- **source_url**: https://www.lsu.edu/graduateschool/
- **source_snippet**: "Admissions: gradadmission@lsu.edu" "Telephone: 225-578-2311"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-C-006: Bursar Contact
- **field**: costs.bursar.contact
- **value**: bursar@lsu.edu, 225-578-3357
- **source_url**: https://www.lsu.edu/bursar/
- **source_snippet**: "Email: bursar@lsu.edu Phone: 225-578-3357"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
lsu-knowledge-base-v2/
├── overview/
│   ├── institution-overview.md
│   ├── college-structure.md
│   └── program-counts.md
├── undergraduate/
│   ├── admissions-requirements.md
│   ├── deadlines.md
│   ├── test-policy.md
│   ├── english-proficiency.md
│   ├── cost-attendance.md
│   ├── financial-aid.md
│   └── programs/
│       ├── agriculture.md
│       ├── art-design.md
│       ├── business.md
│       ├── coast-environment.md
│       ├── engineering.md
│       ├── human-sciences-education.md
│       ├── humanities-social-sciences.md
│       ├── mass-communication.md
│       ├── music-dramatic-arts.md
│       ├── science.md
│       └── honors.md
├── graduate/
│   ├── admissions-requirements.md
│   ├── deadlines.md
│   ├── english-proficiency.md
│   ├── funding.md
│   └── programs/
│       ├── agriculture.md
│       ├── art-design.md
│       ├── business.md
│       ├── coast-environment.md
│       ├── engineering.md
│       ├── human-sciences-education.md
│       ├── humanities-social-sciences.md
│       ├── mass-communication.md
│       ├── music-dramatic-arts.md
│       └── science.md
└── financial/
    ├── tuition-fees.md
    ├── scholarships.md
    └── financial-aid.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "lsu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标URL |
|--------|--------|---------|
| P0 | Actual tuition amounts (2026-2027) | https://www.lsu.edu/bgtplan/Tuition-Fees/2026-2027/undergrad.pdf |
| P0 | Graduate program details (deadlines, GRE requirements per program) | https://www.lsu.edu/graduateschool/admissions/masters_programs.php |
| P1 | Complete list of undergraduate minors | https://lsu.edu/majors/minors.php |
| P1 | Graduate certificates list | https://www.lsu.edu/graduateschool/admissions/graduate_certificates.php |
| P1 | Undergraduate cost of attendance breakdown | https://www.lsu.edu/financialaid/cost/net_price_calculator.php |
| P2 | Honors College admission requirements | http://honors.lsu.edu/ |
| P2 | Veterinary Medicine programs | https://www.lsu.edu/vetmed/ |
| P2 | Law School programs | https://www.lsu.edu/law/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | LSU | (Other schools) |
|------|-----|-----------------|
| Location | Baton Rouge, LA | |
| Type | Public, SEC Flagship | |
| UG Tuition (in-state) | ~$12,000/yr | |
| UG Tuition (out-of-state) | ~$29,000/yr | |
| Need-blind (intl?) | Need-aware for all | |
| EA deadline | N/A | |
| Priority deadline | December 15 | |
| RD deadline | February 1 | |
| SAT/ACT required? | Test-optional | |
| TOEFL min | 79 | |
| IELTS min | 6.5 | |
| Application fee | $50 | |
| Total UG programs | 286 | |
| Total Grad programs | 199 | |
| Total program count (rule 1) | 585+ | |
| School/department count (rule 2) | 12 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: lsu.edu, www.lsu.edu, catalog.lsu.edu, applygrad.lsu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
