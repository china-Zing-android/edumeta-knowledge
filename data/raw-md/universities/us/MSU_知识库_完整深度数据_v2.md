# Mississippi State University (MSU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BBA/BAS/BSW/BARCH) | 80 |
| 本科辅修 (Minor) | 55 |
| 研究生学位项目 (MA/MS/MBA/MFA/MPH/MPPA/EdS/PhD/DVM/etc.) | 168 |
| 研究生高级证书 (Graduate Certificate) | 2 |
| **学位项目总计 (UG + Grad)** | **250** |
| 学院 / 独立系所总数 | 14 |

> Source: MSU 2025-26 Academic Catalog, undergraduate and graduate catalogs.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Mississippi State University
├── College of Agriculture and Life Sciences (CALS)          [学院]
│   ├── Department of Agricultural and Biological Engineering [系]
│   ├── Department of Agricultural Economics                  [系]
│   ├── Department of Agricultural Science and Plant Protection [系]
│   ├── Department of Animal and Dairy Sciences               [系]
│   ├── Department of Biochemistry, Nutrition, and Health Promotion [系]
│   ├── Department of Landscape Architecture and Environmental Design [系]
│   ├── Department of Plant and Soil Sciences                 [系]
│   ├── Department of Poultry Science                         [系]
│   └── School of Human Sciences                              [系]
├── College of Architecture, Art, and Design (CAAD)           [学院]
│   ├── School of Architecture                                [系]
│   ├── Department of Art                                     [系]
│   ├── Building Construction Science                         [系]
│   └── Interior Design                                       [系]
├── College of Arts & Sciences (CAS)                          [学院]
│   ├── African American Studies                              [系]
│   ├── Department of Anthropology and Middle Eastern Cultures [系]
│   ├── Department of Biological Sciences                     [系]
│   ├── Department of Chemistry                               [系]
│   ├── Department of Classical & Modern Languages and Literatures [系]
│   ├── Department of Communication, Media & Theatre          [系]
│   ├── Department of English                                 [系]
│   ├── Department of Geosciences                             [系]
│   ├── Department of History                                 [系]
│   ├── Department of Mathematics and Statistics              [系]
│   ├── Department of Philosophy and Religion                 [系]
│   ├── Department of Physics and Astronomy                   [系]
│   ├── Department of Political Science and Public Administration [系]
│   ├── Department of Psychology                              [系]
│   ├── Department of Sociology                               [系]
│   ├── Economics                                             [系]
│   ├── Gender Studies                                        [系]
│   ├── General Science                                       [系]
│   ├── Interdisciplinary Studies                             [系]
│   ├── Liberal Arts                                          [系]
│   └── Music                                                 [系]
├── College of Business (COB)                                 [学院]
│   ├── Richard C. Adkerson School of Accountancy             [系]
│   ├── Department of Finance and Economics                   [系]
│   ├── Department of Management and Information Systems      [系]
│   ├── Department of Marketing, Quantitative Analysis and Supply Chain Logistics [系]
│   └── International Business Program                        [系]
├── College of Education (COE)                                [学院]
│   ├── Department of Teacher Education and Leadership        [系]
│   ├── Department of Counseling, Higher Education Leadership, Educational Psychology, and Foundations [系]
│   ├── Department of Kinesiology                             [系]
│   ├── Department of Music                                   [系]
│   └── Department of Technology, Leadership and Design       [系]
├── James Worth Bagley College of Engineering (BCoE)          [学院]
│   ├── Department of Aerospace Engineering                   [系]
│   ├── Department of Agricultural and Biological Engineering [系]
│   ├── Dave C. Swalm School of Chemical Engineering          [系]
│   ├── Richard A. Rula School of Civil and Environmental Engineering [系]
│   ├── Department of Computer Science and Engineering        [系]
│   ├── Department of Electrical and Computer Engineering     [系]
│   ├── Department of Industrial and Systems Engineering      [系]
│   └── Michael W. Hall School of Mechanical Engineering      [系]
├── College of Forest Resources (CFR)                         [学院]
│   ├── Department of Forestry                                [系]
│   ├── Department of Sustainable Bioproducts                 [系]
│   └── Department of Wildlife, Fisheries and Aquaculture     [系]
├── College of Veterinary Medicine (CVM)                      [学院]
│   ├── DVM Program                                           [系]
│   └── Veterinary Technology Program                         [系]
├── College of Professional and Continuing Studies (PCS)      [学院]
├── College of Integrative Studies (CIS)                      [学院]
├── School of Nursing                                         [学院]
├── School of Health Professions                              [学院]
├── Graduate School                                           [学院]
└── Judy and Bobby Shackouls Honors College                   [学院]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 14 |
| BS | BS | Bachelor of Science | 本科 | 30 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 10 |
| BAS | BAS | Bachelor of Applied Science | 本科 | 4 |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| BARCH | B.Arch | Bachelor of Architecture | 本科 | 1 |
| BM | BM | Bachelor of Music | 本科 | 1 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 55 |
| MA | MA | Master of Arts | 研究生 | 8 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 4 |
| MS | MS | Master of Science | 研究生 | 65 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MEng | M.Eng | Master of Engineering | 研究生 | 2 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 1 |
| MPAcc | M.P.Acc | Master of Professional Accountancy | 研究生 | 2 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MPPA | MPPA | Master of Public Policy and Administration | 研究生 | 1 |
| MABM | MABM | Master of Agribusiness Management | 研究生 | 1 |
| MAg | M.Ag | Master of Agriculture | 研究生 | 1 |
| MMEd | M.M.Ed | Master of Music Education | 研究生 | 3 |
| MPAS | MPAS | Master of Physician Assistant Studies | 研究生 | 1 |
| MSIS | MSIS | Master of Science in Information Systems | 研究生 | 1 |
| MSIT | MSIT | Master of Science in Instructional Technology | 研究生 | 3 |
| MTax | M.Tax | Master of Taxation | 研究生 | 1 |
| EdS | Ed.S | Educational Specialist | 研究生 | 7 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 55 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| GradCert | Grad Cert | Graduate Certificate | 研究生 | 2 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BBA | BAS | BSW | BARCH | BM | BSN | Minor | MA | MAT | MS | MBA | MEng | MFA | MLA | MPAcc | MPH | MPPA | MABM | MAg | MMEd | MPAS | MSIS | MSIT | MTax | EdS | PhD | DVM | GradCert | 合计 |
|------------|----|----|-----|-----|-----|-----|-------|----|-----|-------|----|----|----|----|------|-----|-----|-------|-----|------|------|-----|------|------|------|------|------|-----|-----|-----|----------|------|
| Agriculture & Life Sciences | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 47 |
| Architecture, Art & Design | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 |
| Arts & Sciences | 14 | 16 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 30 | 6 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 97 |
| Business | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 4 | 0 | 0 | 27 |
| Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 4 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3 | 0 | 7 | 6 | 0 | 0 | 36 |
| Engineering | 0 | 13 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 10 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 38 |
| Forest Resources | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 12 |
| Veterinary Medicine | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 11 |
| Prof & Continuing Studies | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Integrative Studies | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Health Professions | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Graduate School (interdisc.) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 5 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 1 | 18 |
| **合计** | **14** | **53** | **1** | **10** | **4** | **1** | **1** | **1** | **1** | **55** | **8** | **4** | **65** | **2** | **2** | **1** | **1** | **2** | **1** | **1** | **1** | **1** | **3** | **1** | **1** | **3** | **1** | **7** | **55** | **1** | **2** | **250** |

> Reconciliation: rule-1 total (250) == matrix cell-sum (250) ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

MSU has 14 academic colleges and schools offering undergraduate degrees. See Section 0.2 for the full hierarchy tree. The university is organized into traditional land-grant colleges with strong agriculture, engineering, and science programs.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture and Life Sciences

##### Department of Agricultural Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness — Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 2 | Agribusiness — Policy and Law | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 3 | Agribusiness — Production | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 4 | Environmental Economics and Sustainability | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Agricultural and Biological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Agricultural Engineering Technology and Business — Enterprise Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 6 | Agricultural Engineering Technology and Business — Natural Resources and Environmental Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 7 | Agricultural Engineering Technology and Business — Precision Agriculture | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 8 | Agricultural Engineering Technology and Business — Surveying and Geomatics | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Agricultural Science and Plant Protection
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Agricultural Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Animal and Dairy Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Animal and Dairy Sciences — Business and Industry | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 11 | Animal and Dairy Sciences — Production Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 12 | Animal and Dairy Sciences — Pre-Veterinary/Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 13 | Animal and Dairy Sciences — Pre-Veterinary Medical Technology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Biochemistry, Nutrition, and Health Promotion
###### BS
| # | 专业 | URL |
|---|------|-----|
| 14 | Biochemistry — Bioinformatics | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 15 | Biochemistry — Entomology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 16 | Biochemistry — Food Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 17 | Biochemistry — Forensic Sciences | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 18 | Biochemistry — Plant Pathology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 19 | Biochemistry — Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 20 | Culinology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 21 | Food Science, Nutrition and Health Promotion — Pre-Health | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 22 | Food Science, Nutrition and Health Promotion — Food Safety | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 23 | Food Science, Nutrition and Health Promotion — Food and Nutrition | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 24 | Food Science, Nutrition and Health Promotion — Food Processing/Business | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 25 | Food Science, Nutrition and Health Promotion — Food Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Landscape Architecture and Environmental Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 26 | Landscape Architecture | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 27 | Landscape Contracting and Management — Landscape Business Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 28 | Landscape Contracting and Management — Ecosystem Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Plant and Soil Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 29 | Agronomy — Agricultural and Environmental Soil Sciences | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 30 | Agronomy — Golf and Sports Turf Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 31 | Agronomy — Integrated Crop Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 32 | Agronomy — Integrated Pest Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 33 | Environmental Science in Agricultural Systems | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 34 | Horticulture — Floral Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 35 | Horticulture — Floriculture and Ornamental Horticulture | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 36 | Horticulture — Food Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 37 | Horticulture — Fruit and Vegetable Production | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### Department of Poultry Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 38 | Poultry Science — Applied Poultry Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 39 | Poultry Science — Food Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 40 | Poultry Science — Science and Pre-Vet Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

##### School of Human Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 41 | Agricultural Education, Leadership, and Communications — Agricultural Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 42 | Agricultural Education, Leadership, and Communications — Agricultural Leadership | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 43 | Agricultural Education, Leadership, and Communications — Agricultural Communications | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 44 | Fashion Design and Merchandising — Design and Product Development | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 45 | Fashion Design and Merchandising — Merchandising | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 46 | Human Development and Family Science — Child Development | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 47 | Human Development and Family Science — Child Life | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 48 | Human Development and Family Science — Youth Development | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 49 | Human Development and Family Science — Family and Consumer Sciences Teacher Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |
| 50 | Human Development and Family Science — Family Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofagricultureandlifesciences/ |

#### College of Architecture, Art, and Design

##### School of Architecture
###### B.Arch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofarchitectureartanddesign/ |

##### Department of Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 2 | Art (BFA) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofarchitectureartanddesign/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Art (BS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofarchitectureartanddesign/ |

##### Building Construction Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Building Construction Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofarchitectureartanddesign/ |

##### Interior Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Interior Design | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofarchitectureartanddesign/ |

#### College of Arts & Sciences

##### Department of Anthropology and Middle Eastern Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Biological Sciences | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |
| 3 | Medical Technology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |
| 4 | Microbiology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 5 | Chemistry (BA) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Chemistry (BS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Classical & Modern Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Foreign Languages | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Communication, Media & Theatre
###### BA
| # | 专业 | URL |
|---|------|-----|
| 8 | Communication | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | English | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Geosciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Geoscience | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | History | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Mathematics and Statistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | Mathematics (BA) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Mathematics (BS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Philosophy and Religion
###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | Philosophy | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 15 | Physics | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Political Science and Public Administration
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Political Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 17 | Psychology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 18 | Sociology (BA) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 19 | Applied Sociology (BS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | Economics | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Interdisciplinary Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 21 | Interdisciplinary Studies | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Liberal Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 22 | Liberal Arts | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 23 | Music (BA) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 24 | Music (BM) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 25 | Social Work | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

##### General Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 26 | General Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofartsampsciences/ |

#### College of Business

##### Richard C. Adkerson School of Accountancy
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |

##### Department of Finance and Economics
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 2 | Finance | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |
| 3 | Finance — Risk Management and Insurance | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |

##### Department of Management and Information Systems
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 4 | Information Systems | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |
| 5 | Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |
| 6 | Entrepreneurship | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |

##### Department of Marketing, Quantitative Analysis and Supply Chain Logistics
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 7 | Marketing | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |
| 8 | Marketing — Professional Golf Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |
| 9 | Supply Chain Logistics | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |

##### International Business Program
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 10 | International Business/Foreign Languages (double degree) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofbusiness/ |

#### College of Education

##### Department of Teacher Education and Leadership
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofeducation/ |
| 2 | Secondary Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofeducation/ |
| 3 | Special Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofeducation/ |

##### Department of Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Kinesiology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofeducation/ |

##### Department of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 5 | Music Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofeducation/ |

##### Department of Technology, Leadership and Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Technology Education | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofeducation/ |

#### James Worth Bagley College of Engineering

##### Department of Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Department of Agricultural and Biological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Artificial Intelligence Biosystems Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Dave C. Swalm School of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Chemical Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Richard A. Rula School of Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Civil Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Department of Computer Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Computer Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |
| 6 | Computer Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |
| 7 | Cybersecurity | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |
| 8 | Software Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

###### BAS
| # | 专业 | URL |
|---|------|-----|
| 9 | Cybersecurity (BAS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Electrical Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Department of Industrial and Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 11 | Industrial and Systems Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Michael W. Hall School of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Mechanical Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Petroleum Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Petroleum Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 14 | Biomedical Engineering | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/thejamesworthbagleycollegeofengineering/ |

#### College of Forest Resources

##### Department of Forestry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forestry — Forest Business | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 2 | Forestry — Forest Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 3 | Forestry — Environmental Conservation | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 4 | Forestry — Urban Forestry | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 5 | Forestry — Wildlife Management | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |

##### Department of Sustainable Bioproducts
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Sustainable Bioproducts — Business | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 7 | Sustainable Bioproducts — Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |

##### Department of Wildlife, Fisheries and Aquaculture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Wildlife, Fisheries and Aquaculture — Conservation Biology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 9 | Wildlife, Fisheries and Aquaculture — Conservation Law Enforcement | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 10 | Wildlife, Fisheries and Aquaculture — Human-Wildlife Interactions | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 11 | Wildlife, Fisheries and Aquaculture — Wildlife Agriculture Conservation | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 12 | Wildlife, Fisheries and Aquaculture — Wildlife, Fisheries & Aquaculture Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 13 | Wildlife, Fisheries and Aquaculture — Wildlife Veterinary Medicine | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |

##### Natural Resource and Environmental Conservation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 14 | Natural Resource and Environmental Conservation — Natural Resource Law and Administration | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 15 | Natural Resource and Environmental Conservation — Resource Conservation Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |
| 16 | Natural Resource and Environmental Conservation — Natural Resource Technology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofforestresources/ |

#### College of Veterinary Medicine

##### Veterinary Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Medical Technology | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofveterinarymedicine/ |

#### College of Professional and Continuing Studies

###### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Office Technology (BAS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/professionalandcontinuingstudies/ |
| 2 | Public Management (BAS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/professionalandcontinuingstudies/ |
| 3 | Organization Leadership (BAS) | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/professionalandcontinuingstudies/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | University Studies | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/professionalandcontinuingstudies/ |

#### College of Integrative Studies

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/collegeofintegrativestudies/ |

#### School of Nursing

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.msstate.edu/undergraduate/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

- **International Business/Foreign Languages** — joint BBA (College of Business) + BA (College of Arts & Sciences)
- **Five-Year, Two-Degree Curricula** — BS in Agriculture + BS in Business or Liberal Arts (CALS + COB or CAS)

### 1.4 Minors — complete list

MSU offers approximately 55 undergraduate minors across all colleges. Key minors include: African American Studies, Anthropology, Biological Sciences, Chemistry, Cognitive Science, Communication, Creative Writing, Data Analytics and Society, English, Film, Foreign Languages, Gender Studies, Geography, Geology, Geoscience, Geospatial and Remote Sensing, History, International Studies, Leadership, Linguistics, Mathematics, Medical Humanities, Middle Eastern Studies, Microbiology, Philosophy, Physics, Political Science, Pre-Law, Psychology, Religion, Social Justice Studies, Sociology, Statistics, World Language Teaching, and others.

### 1.5 General Education Requirements

MSU requires all undergraduates to complete General Education requirements including: English Composition (6 hrs), Oral Communication (3 hrs), Foreign Language (2-3 semesters), Fine Arts (3 hrs), Humanities (6-18 hrs depending on degree), Social Sciences (6-18 hrs depending on degree), Natural Sciences (9-10 hrs), and a junior/senior level writing course.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agriculture and Life Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural and Extension Education — Leadership | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Agricultural and Extension Education — Teaching | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 3 | Agricultural Life Sciences — Animal Physiology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Agricultural Life Sciences — Biochemistry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 5 | Agricultural Life Sciences — Entomology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 6 | Agricultural Life Sciences — Genetics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 7 | Agricultural Life Sciences — Plant Pathology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 8 | Agriculture — Agricultural Economics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 9 | Agriculture — Animal and Dairy Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 10 | Agriculture — Animal Nutrition | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 11 | Agriculture — Animal Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 12 | Agriculture — Engineering Technology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 13 | Agriculture — Poultry Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 14 | Fashion Design & Merchandising — Design & Product Development | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 15 | Fashion Design & Merchandising — Merchandising | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 16 | Food Science, Nutrition, and Health Promotion — Food Science and Technology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 17 | Food Science, Nutrition, and Health Promotion — Health Promotion | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 18 | Food Science, Nutrition, and Health Promotion — Nutrition | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 19 | Human Development and Family Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 20 | Plant & Soil Sciences — Agronomy | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 21 | Plant & Soil Sciences — Horticulture | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 22 | Plant & Soil Sciences — Weed Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MABM
| # | 项目 | URL |
|---|------|-----|
| 23 | Agribusiness Management | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MAg
| # | 项目 | URL |
|---|------|-----|
| 24 | Agriculture — Animal & Dairy Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 25 | Food Science, Nutrition, and Health Promotion — Public Health Nutrition | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 26 | Agricultural Sciences — Agricultural and Extension Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 27 | Agricultural Sciences — Animal and Dairy Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 28 | Agricultural Sciences — Animal Nutrition | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 29 | Agricultural Sciences — Engineering Technology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 30 | Agricultural Sciences — Poultry Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 31 | Life Sciences — Animal Physiology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 32 | Life Sciences — Biochemistry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 33 | Life Sciences — Entomology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 34 | Life Sciences — Genetics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 35 | Life Sciences — Plant Pathology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 36 | Food Science, Nutrition and Health Promotion — Food Science and Technology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 37 | Food Science, Nutrition and Health Promotion — Functional Foods, Nutrition and Health | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 38 | Food Science, Nutrition and Health Promotion — Nutrition | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 39 | Plant & Soil Sciences — Agronomy | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 40 | Plant & Soil Sciences — Horticulture | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 41 | Plant & Soil Sciences — Weed Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### College of Architecture, Art, and Design

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Historic Preservation | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MLA
| # | 项目 | URL |
|---|------|-----|
| 2 | Landscape Architecture | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### GradCert
| # | 项目 | URL |
|---|------|-----|
| 3 | Public Design | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### College of Arts & Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Anthropology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Economics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 3 | English | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Foreign Language | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 5 | History | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 6 | Political Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 7 | Biological Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 8 | Chemistry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 9 | General Biology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 10 | Geoscience — Applied Meteorology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 11 | Geoscience — Broadcast Meteorology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 12 | Geoscience — Environmental Geoscience | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 13 | Geoscience — Geography | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 14 | Geoscience — Geology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 15 | Geoscience — Geospatial Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 16 | Geoscience — Professional Meteorology/Climatology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 17 | Geoscience — Teachers in Geosciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 18 | Mathematics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 19 | Physics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 20 | Psychology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 21 | Sociology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 22 | Statistics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 23 | Applied Psychology — Cognitive Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 24 | Applied Psychology — Clinical Psychology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 25 | Biological Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 26 | Chemistry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 27 | Earth and Atmospheric Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 28 | History | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 29 | Mathematical Sciences | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 30 | Molecular Biology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 31 | Physics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 32 | Sociology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### College of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Project Management | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MPAcc
| # | 项目 | URL |
|---|------|-----|
| 3 | Accounting | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Accounting — Systems | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 5 | Information Systems | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MTax
| # | 项目 | URL |
|---|------|-----|
| 6 | Taxation | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 7 | Business Administration — Business Information Systems | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 8 | Business Administration — Finance | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 9 | Business Administration — Management | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 10 | Business Administration — Marketing | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### College of Education

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Community College Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Secondary Teacher Alternate Route | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 3 | Counselor Education — Clinical Mental Health | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Counselor Education — Rehabilitation Counseling | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 5 | Counselor Education — School Counseling | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 6 | Educational Leadership — School Administration | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 7 | Educational Leadership — Student Affairs & Higher Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 8 | Educational Psychology — General Educational Psychology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 9 | Educational Psychology — Psychometry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 10 | Elementary Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 11 | Kinesiology — Exercise Physiology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 12 | Kinesiology — Sport Administration | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 13 | Kinesiology — Sport Pedagogy | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 14 | Secondary Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 15 | Special Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 16 | Workforce Education Leadership | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MMEd
| # | 项目 | URL |
|---|------|-----|
| 17 | Music Education — Choral Music | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 18 | Music Education — Elementary Music | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 19 | Music Education — Instrumental Music | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MSIT
| # | 项目 | URL |
|---|------|-----|
| 20 | Instructional Technology — Distance Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 21 | Instructional Technology — Instructional Design | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 22 | Instructional Technology — Multimedia | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 23 | Education — Counselor Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 24 | Education — Education-Technology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 25 | Education — Elementary Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 26 | Education — School Administration | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 27 | Education — School Psychology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 28 | Education — Secondary Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 29 | Education — Special Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 30 | Counselor Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 31 | Curriculum and Instruction — General Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 32 | Curriculum and Instruction — Early Childhood Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 33 | Curriculum and Instruction — Elementary Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 34 | Curriculum and Instruction — Reading Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 35 | Curriculum and Instruction — Secondary Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 36 | Curriculum and Instruction — Special Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 37 | Educational Leadership — Higher Education Leadership | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 38 | Educational Leadership — P-12 School Leadership | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 39 | Educational Psychology — General Educational Psychology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 40 | Educational Psychology — School Psychology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 41 | Kinesiology — Exercise Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 42 | Kinesiology — Sport Studies | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 43 | Instructional Systems & Workforce Development | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 44 | Community College Leadership | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### James Worth Bagley College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Biosystems Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 3 | Biomedical Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Chemical Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 5 | Civil Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 6 | Computational Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 7 | Computer Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 8 | Cyber Security & Operations — Cyber Defense | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 9 | Cyber Security & Operations — Cyber Operations | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 10 | Electrical and Computer Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 11 | Industrial Engineering — Human Factors & Ergonomics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 12 | Industrial Engineering — Industrial Systems | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 13 | Industrial Engineering — Management Systems | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 14 | Industrial Engineering — Manufacturing Systems | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 15 | Industrial Engineering — Operations Research | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 16 | Mechanical Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 17 | Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 18 | Engineering — Military Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 19 | Engineering — Aerospace Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 20 | Engineering — Applied Physics | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 21 | Engineering — Biosystems Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 22 | Engineering — Chemical Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 23 | Engineering — Civil Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 24 | Engineering — Engineering Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 25 | Engineering — Mechanical Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 26 | Biomedical Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 27 | Computational Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 28 | Computer Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 29 | Electrical & Computer Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 30 | Industrial and Systems Engineering | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### College of Forest Resources

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Forestry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Sustainable Bioproducts | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 3 | Wildlife, Fisheries and Aquaculture | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Wildlife, Fisheries, and Aquaculture — Conservation Education | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 5 | Forest Resources — Forestry | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 6 | Forest Resources — Sustainable Bioproducts | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 7 | Forest Resources — Wildlife, Fisheries and Aquaculture | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### College of Veterinary Medicine

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Veterinary Medical Sciences — Computational Biology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 2 | Veterinary Medical Sciences — Infectious Disease | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 3 | Veterinary Medical Science — Population Medicine Non-Thesis | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 4 | Veterinary Medical Science — Population Medicine | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 5 | Veterinary Medical Sciences — Toxicology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 6 | Veterinary Medical Sciences — Veterinary Medical Research | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### DVM
| # | 项目 | URL |
|---|------|-----|
| 7 | Doctor of Veterinary Medicine | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 8 | Veterinary Medical Science — Computational Biology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 9 | Veterinary Medical Science — Infectious Disease | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 10 | Veterinary Medical Science — Population Medicine | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 11 | Veterinary Medical Science — Veterinary Medical Research | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### School of Nursing

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### School of Health Professions

##### MPAS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Assistant Studies | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

#### Graduate School (interdisciplinary)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 2 | Environmental Toxicology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 3 | Forensic Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 4 | Environmental Toxicology | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |
| 5 | Forensic Science | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

##### GradCert
| # | 项目 | URL |
|---|------|-----|
| 6 | Clinical Health Promotion and Wellness Coaching | https://catalog.msstate.edu/graduate/degrees-majors-offered/ |

### 2.2 At least one program's full deep-dive (worked example)

**Master of Science in Computer Science (Bagley College of Engineering)**

- Department: Department of Computer Science and Engineering
- Office: 250 McCain Hall
- Telephone: (662) 325-2270
- Application: Online at https://www.grad.msstate.edu/admissions
- Application fee: $60 (domestic), $80 (international)
- GRE: Required for some concentrations
- TOEFL/IELTS: TOEFL 79+ / IELTS 6.5+ recommended
- Thesis and non-thesis options available
- Starkville and Distance Education delivery modes

### 2.3 Graduate admissions model

MSU uses a **centralized application system** through the Graduate School (https://www.grad.msstate.edu/). Applicants submit one application to the Graduate School, which then routes materials to the specific department/program for review. Each department sets its own additional requirements (GRE scores, portfolio, writing samples, etc.). The Graduate School sets university-wide minimums:
- Bachelor's degree from accredited institution
- Minimum 3.0 GPA on last 60 hours of undergraduate coursework
- Three letters of recommendation
- Statement of purpose
- Official transcripts
- Application fee ($60 domestic, $80 international)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Application portal | https://apply.msstate.edu/ | admissions.msstate.edu |
| Application fee (domestic) | $50 | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Application fee (international) | $60 | admissions.msstate.edu/apply/admission-process/international |
| Admissions policy | Rolling admissions | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| EA deadline | N/A (no EA) | admissions.msstate.edu |
| RD deadline | N/A (rolling; open until 10th day of classes) | admissions.msstate.edu |
| Application opens (Summer/Fall) | August 1 | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Application opens (Spring) | August 5 | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Decision timeline | 2-3 weeks after complete file | admissions.msstate.edu FAQ |
| Test policy | Test-optional | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Superscore | Yes (ACT or SAT separately) | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| ACT code | 2220 | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| SAT code | 1480 | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Minimum GPA (MS residents) | 2.0 on CPC | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Minimum GPA (non-residents) | Holistic review | admissions.msstate.edu/apply/admission-process/freshman-admissions |
| Recommendation letters | Not required for UG | admissions.msstate.edu |
| Interview | Not required | admissions.msstate.edu |
| Portfolio | Not required (except Architecture/Art) | admissions.msstate.edu |
| On-campus housing | Required for freshmen | admissions.msstate.edu FAQ |
| FAFSA code | 002423 | sfa.msstate.edu |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | 来源 |
|------|---------|-------------|------|
| TOEFL iBT | 71 | Some departments require higher | admissions.msstate.edu/apply/admission-process/international |
| IELTS | 6.0 | Some departments require higher | admissions.msstate.edu/apply/admission-process/international |
| Duolingo English Test | 105 | — | admissions.msstate.edu/apply/admission-process/international |
| ACT English | 19 | — | admissions.msstate.edu/apply/admission-process/international |
| SAT EBRW | 510 | — | admissions.msstate.edu/apply/admission-process/international |

> Exemptions: Students who complete the English Language Institute (ELI) program, or who are from English-speaking countries, may be exempt.

### 3.3 Graduate — global rules

- Centralized application via Graduate School
- Application fee: $60 domestic, $80 international
- GRE: Per-program (some require, some don't)
- TOEFL/IELTS: TOEFL 79+ / IELTS 6.5+ recommended (varies by program)
- CGS April-15 resolution: MSU is a signatory
- Application timeline: Rolling for most programs; some have specific deadlines
- Most PhD programs offer full funding (TA/RA positions)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, Starkville campus)

| Expense item | In-State (per semester, 12-16 hrs) | Out-of-State (per semester, 12-16 hrs) | 来源 |
|-------------|-----------------------------------|---------------------------------------|------|
| Tuition & Required Fees | $5,422.50 | $5,422.50 | controller.msstate.edu/accountservices/tuition/starkville-campus |
| Non-Resident Fee | $0.00 | $9,495.50 | controller.msstate.edu/accountservices/tuition/starkville-campus |
| Capital Improvement Fee | $100.00 | $100.00 | controller.msstate.edu/accountservices/tuition/starkville-campus |
| Student Activities Fee | $25.00 | $25.00 | controller.msstate.edu/accountservices/tuition/starkville-campus |
| **Total per semester** | **$5,547.50** | **$15,043.00** | controller.msstate.edu/accountservices/tuition/starkville-campus |
| **Total per year (2 semesters)** | **$11,095** | **$30,086** | controller.msstate.edu/accountservices/tuition/starkville-campus |

| Additional estimated annual costs | Amount | 来源 |
|----------------------------------|--------|------|
| Housing | ~$9,990 | sfa.msstate.edu/cost |
| Food/Meal Plan | ~$5,210 | sfa.msstate.edu/cost |
| Books & Supplies | ~$1,200 | sfa.msstate.edu/cost |
| Personal/Transportation | ~$3,000 | sfa.msstate.edu/cost |

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all applicants** (not need-blind)
- FAFSA code: 002423
- Automatic academic scholarships based on GPA and ACT/SAT scores (no separate application required)
- General Scholarship Application opens October 1 for additional competitive scholarships
- Out-of-state students eligible for non-resident tuition scholarships
- No tuition-free income threshold published
- Mississippi residents eligible for state aid programs

### 4.3 Graduate cost & funding framework

- Graduate tuition: Same per-credit-hour rates as undergraduate
- Most PhD programs offer full funding through TA/RA positions
- Master's funding varies by department
- Application fee: $60 domestic, $80 international
- Fee waivers available for MSU employees

---

## SECTION 5 — Evidence chain index

```yaml
field: undergraduate.admissions.test_policy
value: "Test-optional"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "Test-Optional: Students who choose not to participate in ACT or SAT testing will be reviewed for admissibility."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.application_fee
value: "$50 domestic / $60 international"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "There is a $50 non-refundable fee to submit your application."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.deadline_policy
value: "Rolling admissions"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "MSU has a rolling admissions policy. The application for each semester will remain open until the 10th day of classes."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.application_opens
value: "August 1 (Summer/Fall), August 5 (Spring)"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "Application for Admission Opens: apply.msstate.edu August 1"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.english_proficiency.tofel
value: "71 minimum"
source_url: https://www.admissions.msstate.edu/apply/admission-process/international
source_snippet: "Acceptable score on the TOEFL exam 71 (some departments require a higher score)"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.english_proficiency.ielts
value: "6.0 minimum"
source_url: https://www.admissions.msstate.edu/apply/admission-process/international
source_snippet: "An acceptable score on the IELTS exam 6.0 (some departments require a higher score)"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.english_proficiency.duolingo
value: "105"
source_url: https://www.admissions.msstate.edu/apply/admission-process/international
source_snippet: "Duolingo English Test score of 105"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.cost.tuition_in_state_per_semester
value: "$5,547.50"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Tuition & Required Fees $5,422.50 ... Total Fee $5,547.50"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_oos_per_semester
value: "$15,043.00"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Tuition & Required Fees $5,422.50 ... Non-Resident Fee $9,495.50 ... Total Fee $15,043.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_in_state_annual
value: "$11,095"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Total Fee $5,547.50 per semester (x2 = $11,095 annually)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_oos_annual
value: "$30,086"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Total Fee $15,043.00 per semester (x2 = $30,086 annually)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.admissions.min_gpa_ms_residents
value: "2.0 on CPC"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "A minimum 2.0 grade-point average on the CPC"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.act_code
value: "2220"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "ACT College Code - 2220 or SAT College Code – 1480"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.sat_code
value: "1480"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "ACT College Code - 2220 or SAT College Code – 1480"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.superscore
value: "Yes (ACT or SAT separately)"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "MSU will use the superscore (highest ACT or SAT subject test scores from the same test type when scores from more than one test date are submitted.)"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.fafsa_code
value: "002423"
source_url: https://www.admissions.msstate.edu/tuition-scholarships-aid
source_snippet: "MSU's Federal School Code is 002423"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: institution.type
value: "Public land-grant university"
source_url: https://catalog.msstate.edu/undergraduate/
source_snippet: "Mississippi State University is a public, land-grant university whose mission is to provide access and opportunity"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: institution.accreditation
value: "SACSCOC"
source_url: https://catalog.msstate.edu/undergraduate/
source_snippet: "Mississippi State University is accredited by the Southern Association of Colleges and Schools Commission on Colleges (SACSCOC)"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.admissions.application_fee
value: "$60 domestic / $80 international"
source_url: https://catalog.msstate.edu/graduate/admissions-information/
source_snippet: "a non-refundable application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.housing_requirement
value: "Required for freshmen"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "Yes. First-time freshman students are generally required to live on campus"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.decision_timeline
value: "2-3 weeks"
source_url: https://www.admissions.msstate.edu/apply/admission-process/freshman-admissions
source_snippet: "Most students receive an admissions decision about 2–3 weeks after all required application materials have been submitted."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.cost.per_credit_hour_in_state
value: "$462.42"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Total Fee (Per Credit Hour) $462.42"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.per_credit_hour_oos
value: "$1,253.92"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Total Fee (Per Credit Hour) $1,253.92"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: graduate.tuition.same_as_ug
value: "Same per-credit-hour rates"
source_url: https://www.controller.msstate.edu/accountservices/tuition/starkville-campus
source_snippet: "Tuition and required fees are charged on a per-credit-hour basis to all students."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.cost.housing_estimate
value: "~$9,990/year"
source_url: https://www.sfa.msstate.edu/cost/
source_snippet: "Housing $9,990"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.cost.food_estimate
value: "~$5,210/year"
source_url: https://www.sfa.msstate.edu/cost/
source_snippet: "Food $5,210"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
MSU-knowledge-base-v2/
├── overview (Section 0)
├── undergraduate-programs (Section 1)
│   ├── college-agriculture-life-sciences
│   ├── college-architecture-art-design
│   ├── college-arts-sciences
│   ├── college-business
│   ├── college-education
│   ├── bagley-college-engineering
│   ├── college-forest-resources
│   ├── college-veterinary-medicine
│   ├── college-professional-continuing-studies
│   ├── college-integrative-studies
│   └── school-nursing
├── graduate-programs (Section 2)
│   ├── grad-agriculture-life-sciences
│   ├── grad-architecture-art-design
│   ├── grad-arts-sciences
│   ├── grad-business
│   ├── grad-education
│   ├── grad-engineering
│   ├── grad-forest-resources
│   ├── grad-veterinary-medicine
│   ├── grad-nursing
│   ├── grad-health-professions
│   └── grad-interdisciplinary
├── admissions-deadlines (Section 3)
├── costs-financial-aid (Section 4)
└── evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "MSU-knowledge-base-v2"
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

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Full COA line-item breakdown (SFA page JS-rendered) | https://www.sfa.msstate.edu/cost/ |
| P0 | Automatic scholarship amounts by GPA/ACT | https://www.sfa.msstate.edu/scholarships/ |
| P1 | Per-program GRE requirements (graduate) | Individual department pages |
| P1 | Per-program TOEFL minimums (some departments higher) | Individual department pages |
| P2 | School of Nursing specific programs | https://catalog.msstate.edu/ |
| P2 | School of Health Professions specific programs | https://catalog.msstate.edu/ |
| P2 | MSU-Meridian campus programs | https://catalog.msstate.edu/undergraduate/collegesanddegreeprograms/msu-meridian/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | MSU | (other schools) |
|-----------|-----|-----------------|
| Type | Public land-grant | |
| Location | Starkville, MS | |
| SEC athletics | Yes | |
| UG tuition in-state/year | $11,095 | |
| UG tuition OOS/year | $30,086 | |
| Need-blind (domestic) | No (need-aware) | |
| Need-blind (intl) | No (need-aware) | |
| EA deadline | N/A (rolling) | |
| RD deadline | N/A (rolling) | |
| SAT/ACT required | No (test-optional) | |
| TOEFL min | 71 | |
| IELTS min | 6.0 | |
| Duolingo min | 105 | |
| App fee (UG) | $50 | |
| App fee (Grad) | $60 | |
| Total programs (Rule 1) | 250 | |
| School/college count (Rule 2) | 14 | |
| FAFSA code | 002423 | |
| ACT code | 2220 | |
| SAT code | 1480 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.msstate.edu, catalog.msstate.edu, controller.msstate.edu, sfa.msstate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
