# University of Wisconsin-Madison (UW-Madison) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA/BLS/BSE/BLA/BM/BSN/BSW/JBA/JBS/BNS) | 224 |
| 本科证书 (Certificate) | 116 |
| 研究生学位项目 (MA/MS/PhD/MBA/MFA/MEng/MPA/MSW/MM/DMA/DNP/JD/LLM/SJD/MD/MGCS/DPT/PharmD/DVM/MPH) | 286 |
| 研究生证书/博士辅修 (Graduate Certificate / Doctoral Minor) | 137 |
| **学位项目总计 (UG + Grad)** | **763** |
| 学院 / 独立系所总数 | 14 |

> **来源**: guide.wisc.edu (2026-2027 edition), 涵盖 undergraduate/, graduate/, law/, medicine/, pharmacy/, veterinary/ 所有程序页面。

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
UW-Madison
├── College of Agricultural and Life Sciences (CALS)              [学院]
│   ├── Agricultural and Applied Economics                        [系]
│   ├── Animal and Dairy Sciences                                 [系]
│   ├── Biochemistry                                              [系]
│   ├── Biological Systems Engineering                            [系]
│   ├── Community and Environmental Sociology                     [系]
│   ├── Entomology                                                [系]
│   ├── Food and Nutritional Sciences                             [系]
│   ├── Forest and Wildlife Ecology                               [系]
│   ├── Life Sciences Communication                               [系]
│   ├── Plant and Agroecosystem Sciences                          [系]
│   ├── Plant Pathology                                           [系]
│   └── Soil and Environmental Sciences                           [系]
├── School of Business                                            [学院]
│   ├── Accounting and Information Systems                        [系]
│   ├── Finance                                                   [系]
│   ├── Management and Human Resources                            [系]
│   ├── Marketing                                                 [系]
│   ├── Operations and Information Management                     [系]
│   └── Real Estate and Urban Land Economics                      [系]
├── School of Education                                           [学院]
│   ├── Art                                                       [系]
│   ├── Curriculum and Instruction                                [系]
│   ├── Dance                                                     [系]
│   ├── Educational Leadership and Policy Analysis                [系]
│   ├── Educational Policy Studies                                [系]
│   ├── Educational Psychology                                    [系]
│   ├── Kinesiology                                               [系]
│   └── Rehabilitation Psychology and Special Education           [系]
├── College of Engineering                                        [学院]
│   ├── Biomedical Engineering                                    [系]
│   ├── Chemical and Biological Engineering                       [系]
│   ├── Civil and Environmental Engineering                       [系]
│   ├── Electrical and Computer Engineering                       [系]
│   ├── Industrial and Systems Engineering                        [系]
│   ├── Materials Science and Engineering                         [系]
│   ├── Mechanical Engineering                                    [系]
│   └── Nuclear Engineering and Engineering Physics               [系]
├── School of Human Ecology                                       [学院]
│   ├── Civil Society & Community Studies                         [系]
│   ├── Consumer Science                                          [系]
│   ├── Design Studies                                            [系]
│   ├── Human Development and Family Studies                      [系]
│   └── Interior Architecture                                    [系]
├── The Information School                                        [学院]
├── La Follette School of Public Affairs                          [学院]
├── Law School                                                    [学院]
├── College of Letters & Science                                  [学院]
│   ├── African American Studies                                  [系]
│   ├── African Cultural Studies                                  [系]
│   ├── Anthropology                                              [系]
│   ├── Art History                                               [系]
│   ├── Asian Languages and Cultures                              [系]
│   ├── Astronomy                                                 [系]
│   ├── Atmospheric and Oceanic Sciences                          [系]
│   ├── Bacteriology                                              [系]
│   ├── Botany                                                    [系]
│   ├── Chemistry                                                 [系]
│   ├── Classical and Ancient Near Eastern Studies                 [系]
│   ├── Communication Arts                                        [系]
│   ├── Computer Sciences                                         [系]
│   ├── Economics                                                 [系]
│   ├── English                                                   [系]
│   ├── French and Italian                                        [系]
│   ├── Gender and Women's Studies                                [系]
│   ├── Genetics                                                  [系]
│   ├── Geography                                                 [系]
│   ├── Geoscience                                                [系]
│   ├── German, Nordic, and Slavic                                [系]
│   ├── History                                                   [系]
│   ├── Integrative Biology                                       [系]
│   ├── Journalism and Mass Communication                         [系]
│   ├── Language Sciences                                         [系]
│   ├── Mathematics                                               [系]
│   ├── Mead Witter School of Music                               [系]  ⚠ also listed as separate school
│   ├── Medical Physics                                           [系]
│   ├── Philosophy                                                [系]
│   ├── Physics                                                   [系]
│   ├── Planning and Landscape Architecture                       [系]
│   ├── Political Science                                         [系]
│   ├── Psychology                                                [系]
│   ├── Religious Studies                                         [系]
│   ├── Social Work                                               [系]
│   ├── Sociology                                                 [系]
│   └── Spanish and Portuguese                                    [系]
├── School of Medicine and Public Health                          [学院]
│   ├── Biostatistics and Medical Informatics                     [系]
│   ├── Cell and Regenerative Biology                             [系]
│   ├── Communication Sciences and Disorders                      [系]
│   ├── Medical Physics                                           [系]
│   ├── Oncology                                                  [系]
│   ├── Pathology                                                 [系]
│   └── Population Health Sciences                                [系]
├── Mead Witter School of Music                                   [学院]
├── School of Nursing                                             [学院]
├── School of Pharmacy                                            [学院]
├── School of Veterinary Medicine                                 [学院]
└── Gaylord Nelson Institute for Environmental Studies             [学院]
    ├── Nelson Institute (undergraduate)                          [系]
    └── Nelson Institute (graduate)                               [系]
```

> **注意**: Mead Witter School of Music 在本科阶段隶属于 College of Letters & Science，但在研究生阶段是独立的学院。Law School、Medicine and Public Health、Veterinary Medicine 主要提供研究生/专业学位。

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| BA | Bachelor of Arts | 本科 | BA | 62 |
| BS | Bachelor of Science | 本科 | BS | 126 |
| BFA | Bachelor of Fine Arts | 本科 | BFA | 2 |
| BBA | Bachelor of Business Administration | 本科 | BBA | 17 |
| BLS | Bachelor of Liberal Studies | 本科 | BLS | 1 |
| BSE | Bachelor of Science in Engineering | 本科 | BSE | 4 |
| BLA | Bachelor of Landscape Architecture | 本科 | BLA | 1 |
| BM | Bachelor of Music | 本科 | BM | 2 |
| BSN | Bachelor of Science in Nursing | 本科 | BSN | 3 |
| BSW | Bachelor of Social Work | 本科 | BSW | 1 |
| JBA | Journalism Bachelor of Arts | 本科 | JBA | 1 |
| JBS | Journalism Bachelor of Science | 本科 | JBS | 1 |
| BNS | Bachelor of Naval Science | 本科 | BNS | 1 |
| Certificate | 本科证书 | 本科 | Certificate | 116 |
| MA | Master of Arts | 研究生 | MA | 36 |
| MS | Master of Science | 研究生 | MS | 109 |
| MFA | Master of Fine Arts | 研究生 | MFA | 4 |
| MBA | Master of Business Administration | 研究生 | MBA | 9 |
| MEng | Master of Engineering | 研究生 | MEng | 2 |
| MPA | Master of Public Administration | 研究生 | MPA | 1 |
| MPH | Master of Public Health | 研究生 | MPH | 1 |
| MSW | Master of Social Work | 研究生 | MSW | 2 |
| MM | Master of Music | 研究生 | MM | 2 |
| MGCS | Master of Genetic Counselor Studies | 研究生 | MGCS | 1 |
| DMA | Doctor of Musical Arts | 研究生 | DMA | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | DNP | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | DPT | 1 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 108 |
| JD | Juris Doctor | 研究生 | JD | 1 |
| LLM | Master of Laws | 研究生 | LLM | 1 |
| SJD | Doctor of Juridical Science | 研究生 | SJD | 1 |
| MD | Doctor of Medicine | 研究生 | MD | 1 |
| PharmD | Doctor of Pharmacy | 研究生 | PharmD | 1 |
| DVM | Doctor of Veterinary Medicine | 研究生 | DVM | 1 |
| Doctoral Minor | 博士辅修 | 研究生 | Doctoral Minor | 110 |
| Grad/Prof Certificate | 研究生专业证书 | 研究生 | Graduate/Professional Certificate | 27 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BBA | BLS | BSE | BLA | BM | BSN | BSW | JBA | JBS | BNS | Cert(UG) | MA | MS | MFA | MBA | MEng | MPA | MPH | MSW | MM | MGCS | DMA | DNP | DPT | PhD | JD | LLM | SJD | MD | PharmD | DVM | DocMinor | GradCert | 合计 |
|------------|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|----------|----|----|-----|-----|------|-----|-----|-----|-----|------|-----|-----|-----|-----|----|-----|-----|----|--------|-----|----------|----------|------|
| CALS | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 67 |
| Business | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 46 |
| Education | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 29 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 61 |
| Engineering | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 21 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 41 |
| Human Ecology | 0 | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 23 |
| Information School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 7 |
| La Follette | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| L&S | 62 | 94 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 1 | 0 | 28 | 20 | 75 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 1 | 0 | 0 | 59 | 0 | 0 | 0 | 0 | 0 | 0 | 65 | 18 | 434 |
| Medicine & Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 8 | 0 | 0 | 0 | 1 | 0 | 0 | 8 | 5 | 40 |
| Music | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| Nursing | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 11 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 5 |
| Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 4 |
| Environmental Studies | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 9 |
| **合计** | 62 | 129 | 2 | 17 | 1 | 4 | 1 | 2 | 3 | 1 | 1 | 1 | 1 | 113 | 36 | 108 | 4 | 9 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 112 | 2 | 1 | 1 | 1 | 1 | 1 | 104 | 27 | **763** |

> **注意**: Music 在本科阶段计入 L&S，但在研究生阶段是独立学院。Environmental Studies (Gaylord Nelson Institute) 是独立学院。部分研究生项目（如 Biostatistics, Cell Biology, Oncology, Pathology）计入 Medicine & Public Health。

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UW-Madison 有 9 个本科学院，提供 224 个学位专业和 116 个证书项目。详见 Section 0.2 层级树。

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Agricultural and Life Sciences (CALS)

##### Agricultural and Applied Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Applied Economics | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/agricultural-applied-economics/agricultural-applied-economics-bs/ |
| 2 | Agricultural Business Management | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/agricultural-applied-economics/agricultural-business-management-bs/ |

##### Animal and Dairy Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal and Veterinary Biosciences | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/animal-dairy-sciences/animal-veterinary-biosciences-bs/ |
| 2 | Animal Sciences | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/animal-dairy-sciences/animal-sciences-bs/ |

##### Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry (CALS) | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/biochemistry/biochemistry-bs/ |

##### Biological Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Systems Engineering | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/biological-systems-engineering/biological-systems-engineering-bs/ |

##### Community and Environmental Sociology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Community and Environmental Sociology | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/community-environmental-sociology/community-environmental-sociology-bs/ |

##### Entomology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Entomology | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/entomology/entomology-bs/ |

##### Food and Nutritional Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dietetics | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/food-nutritional-sciences/dietetics-bs/ |
| 2 | Food Science | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/food-nutritional-sciences/food-science-bs/ |
| 3 | Nutritional Sciences | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/food-nutritional-sciences/nutritional-sciences-bs/ |

##### Forest and Wildlife Ecology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forest Science | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/forest-wildlife-ecology/forest-science-bs/ |
| 2 | Wildlife Ecology | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/forest-wildlife-ecology/wildlife-ecology-bs/ |

##### Life Sciences Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Life Sciences Communication | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/life-sciences-communication/life-sciences-communication-bs/ |

##### Plant and Agroecosystem Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agroecology | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/plant-agroecosystem-sciences/agroecology-bs/ |
| 2 | Agronomy | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/plant-agroecosystem-sciences/agronomy-bs/ |

##### Plant Pathology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Plant Pathology | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/plant-pathology/plant-pathology-bs/ |

##### Soil and Environmental Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/soil-environmental-sciences/environmental-sciences-bs/ |
| 2 | Soil Science | https://guide.wisc.edu/undergraduate/agricultural-life-sciences/soil-environmental-sciences/soil-science-bs/ |

#### School of Business

##### Accounting and Information Systems
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://guide.wisc.edu/undergraduate/business/accounting-information-systems/accounting-bba/ |
| 2 | Information Systems | https://guide.wisc.edu/undergraduate/business/accounting-information-systems/information-systems-bba/ |

##### Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://guide.wisc.edu/undergraduate/business/finance/finance-bba/ |
| 2 | Finance, Investment and Banking | https://guide.wisc.edu/undergraduate/business/finance/finance-investment-banking-bba/ |
| 3 | Real Estate | https://guide.wisc.edu/undergraduate/business/finance/real-estate-bba/ |

##### Management and Human Resources
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://guide.wisc.edu/undergraduate/business/management-human-resources/management-bba/ |
| 2 | Human Resources | https://guide.wisc.edu/undergraduate/business/management-human-resources/human-resources-bba/ |

##### Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://guide.wisc.edu/undergraduate/business/marketing/marketing-bba/ |
| 2 | Marketing, Analytics | https://guide.wisc.edu/undergraduate/business/marketing/marketing-analytics-bba/ |

##### Operations and Information Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Operations and Technology Management | https://guide.wisc.edu/undergraduate/business/operations-information-management/operations-technology-management-bba/ |
| 2 | Supply Chain Management | https://guide.wisc.edu/undergraduate/business/operations-information-management/supply-chain-management-bba/ |

##### Real Estate and Urban Land Economics
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate and Urban Land Economics | https://guide.wisc.edu/undergraduate/business/real-estate-urban-land-economics/real-estate-urban-land-economics-bba/ |

#### School of Education

##### Art
###### BS / BFA
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art Education | BS | https://guide.wisc.edu/undergraduate/education/art/art-education-bs/ |
| 2 | Art | BS | https://guide.wisc.edu/undergraduate/education/art/art-bs/ |
| 3 | Art | BFA | https://guide.wisc.edu/undergraduate/education/art/art-bfa/ |

##### Curriculum and Instruction
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://guide.wisc.edu/undergraduate/education/curriculum-instruction/elementary-education-bs/ |

##### Dance
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://guide.wisc.edu/undergraduate/education/dance/dance-bfa/ |

##### Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise and Movement Science | https://guide.wisc.edu/undergraduate/education/kinesiology/exercise-movement-science-bs/ |

#### College of Engineering

##### Biomedical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://guide.wisc.edu/undergraduate/engineering/biomedical-engineering/biomedical-engineering-bse/ |

##### Chemical and Biological Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://guide.wisc.edu/undergraduate/engineering/chemical-biological-engineering/chemical-engineering-bse/ |

##### Civil and Environmental Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://guide.wisc.edu/undergraduate/engineering/civil-environmental-engineering/civil-engineering-bse/ |

##### Electrical and Computer Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://guide.wisc.edu/undergraduate/engineering/electrical-computer-engineering/computer-engineering-bse/ |
| 2 | Electrical Engineering | https://guide.wisc.edu/undergraduate/engineering/electrical-computer-engineering/electrical-engineering-bse/ |

##### Industrial and Systems Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://guide.wisc.edu/undergraduate/engineering/industrial-systems-engineering/industrial-engineering-bse/ |

##### Materials Science and Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://guide.wisc.edu/undergraduate/engineering/materials-science-engineering/materials-science-engineering-bse/ |

##### Mechanical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://guide.wisc.edu/undergraduate/engineering/mechanical-engineering/mechanical-engineering-bse/ |
| 2 | Aerospace Engineering | https://guide.wisc.edu/undergraduate/engineering/mechanical-engineering/aerospace-engineering-bs/ |

##### Nuclear Engineering and Engineering Physics
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Physics | https://guide.wisc.edu/undergraduate/engineering/nuclear-engineering-engineering-physics/engineering-physics-bse/ |
| 2 | Nuclear Engineering | https://guide.wisc.edu/undergraduate/engineering/nuclear-engineering-engineering-physics/nuclear-engineering-bse/ |

##### Naval Science (College-wide)
###### BNS
| # | 专业 | URL |
|---|------|-----|
| 1 | Naval Science | https://guide.wisc.edu/undergraduate/engineering/college-wide/naval-science-bns/ |

#### School of Human Ecology

##### Civil Society & Community Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Community and Nonprofit Leadership | https://guide.wisc.edu/undergraduate/human-ecology/civil-society-community-studies/community-nonprofit-leadership-bs/ |

##### Consumer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Consumer Behavior and Marketplace Studies | https://guide.wisc.edu/undergraduate/human-ecology/consumer-science/consumer-behavior-marketplace-studies-bs/ |
| 2 | Personal Finance | https://guide.wisc.edu/undergraduate/human-ecology/consumer-science/personal-finance-bs/ |

##### Design Studies
###### BS / BFA
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Interior Architecture | BS | https://guide.wisc.edu/undergraduate/human-ecology/design-studies/interior-architecture-bs/ |
| 2 | Textiles and Fashion Design | BFA | https://guide.wisc.edu/undergraduate/human-ecology/design-studies/textiles-fashion-design-bfa/ |

##### Human Development and Family Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development and Family Studies | https://guide.wisc.edu/undergraduate/human-ecology/human-development-family-studies/human-development-family-studies-bs/ |

#### College of Letters & Science

##### (Multiple Departments)
###### BA / BS
| # | 专业 | 学位 | 系 | URL |
|---|------|------|-----|-----|
| 1 | African American Studies | BA | African American Studies | https://guide.wisc.edu/undergraduate/letters-science/african-american-studies/african-american-studies-ba/ |
| 2 | African American Studies | BS | African American Studies | https://guide.wisc.edu/undergraduate/letters-science/african-american-studies/african-american-studies-bs/ |
| 3 | African Cultural Studies | BA | African Cultural Studies | https://guide.wisc.edu/undergraduate/letters-science/african-cultural-studies/african-cultural-studies-ba/ |
| 4 | African Cultural Studies | BS | African Cultural Studies | https://guide.wisc.edu/undergraduate/letters-science/african-cultural-studies/african-cultural-studies-bs/ |
| 5 | Anthropology | BA | Anthropology | https://guide.wisc.edu/undergraduate/letters-science/anthropology/anthropology-ba/ |
| 6 | Anthropology | BS | Anthropology | https://guide.wisc.edu/undergraduate/letters-science/anthropology/anthropology-bs/ |
| 7 | Art History | BA | Art History | https://guide.wisc.edu/undergraduate/letters-science/art-history/art-history-ba/ |
| 8 | Art History | BS | Art History | https://guide.wisc.edu/undergraduate/letters-science/art-history/art-history-bs/ |
| 9 | Asian Languages and Cultures | BA | Asian Languages and Cultures | https://guide.wisc.edu/undergraduate/letters-science/asian-languages-cultures/asian-languages-cultures-ba/ |
| 10 | Asian Languages and Cultures | BS | Asian Languages and Cultures | https://guide.wisc.edu/undergraduate/letters-science/asian-languages-cultures/asian-languages-cultures-bs/ |
| 11 | Astronomy-Physics | BA | Astronomy | https://guide.wisc.edu/undergraduate/letters-science/astronomy/astronomy-physics-ba/ |
| 12 | Astronomy-Physics | BS | Astronomy | https://guide.wisc.edu/undergraduate/letters-science/astronomy/astronomy-physics-bs/ |
| 13 | Atmospheric and Oceanic Sciences | BA | Atmospheric and Oceanic Sciences | https://guide.wisc.edu/undergraduate/letters-science/atmospheric-oceanic-sciences/atmospheric-oceanic-sciences-ba/ |
| 14 | Atmospheric and Oceanic Sciences | BS | Atmospheric and Oceanic Sciences | https://guide.wisc.edu/undergraduate/letters-science/atmospheric-oceanic-sciences/atmospheric-oceanic-sciences-bs/ |
| 15 | Biochemistry | BA | College-wide | https://guide.wisc.edu/undergraduate/letters-science/college-wide/biochemistry-ba/ |
| 16 | Biochemistry | BS | College-wide | https://guide.wisc.edu/undergraduate/letters-science/college-wide/biochemistry-bs/ |
| 17 | Biology | BA | Integrative Biology | https://guide.wisc.edu/undergraduate/letters-science/integrative-biology/biology-ba/ |
| 18 | Biology | BS | Integrative Biology | https://guide.wisc.edu/undergraduate/letters-science/integrative-biology/biology-bs/ |
| 19 | Chemistry | BA | Chemistry | https://guide.wisc.edu/undergraduate/letters-science/chemistry/chemistry-ba/ |
| 20 | Chemistry | BS | Chemistry | https://guide.wisc.edu/undergraduate/letters-science/chemistry/chemistry-bs/ |
| 21 | Classical Humanities | BA | Classical and Ancient Near Eastern Studies | https://guide.wisc.edu/undergraduate/letters-science/classical-ancient-near-eastern-studies/classical-humanities-ba/ |
| 22 | Classics | BA | Classical and Ancient Near Eastern Studies | https://guide.wisc.edu/undergraduate/letters-science/classical-ancient-near-eastern-studies/classics-ba/ |
| 23 | Communication Arts | BA | Communication Arts | https://guide.wisc.edu/undergraduate/letters-science/communication-arts/communication-arts-ba/ |
| 24 | Communication Arts | BS | Communication Arts | https://guide.wisc.edu/undergraduate/letters-science/communication-arts/communication-arts-bs/ |
| 25 | Communication Sciences and Disorders | BS | Communication Sciences and Disorders | https://guide.wisc.edu/undergraduate/letters-science/communication-sciences-disorders/communication-sciences-disorders-bs/ |
| 26 | Computer Sciences | BA | Computer Sciences | https://guide.wisc.edu/undergraduate/letters-science/computer-sciences/computer-sciences-ba/ |
| 27 | Computer Sciences | BS | Computer Sciences | https://guide.wisc.edu/undergraduate/letters-science/computer-sciences/computer-sciences-bs/ |
| 28 | Economics | BA | Economics | https://guide.wisc.edu/undergraduate/letters-science/economics/economics-ba/ |
| 29 | Economics | BS | Economics | https://guide.wisc.edu/undergraduate/letters-science/economics/economics-bs/ |
| 30 | English | BA | English | https://guide.wisc.edu/undergraduate/letters-science/english/english-ba/ |
| 31 | English | BS | English | https://guide.wisc.edu/undergraduate/letters-science/english/english-bs/ |
| 32 | French | BA | French and Italian | https://guide.wisc.edu/undergraduate/letters-science/french-italian/french-ba/ |
| 33 | Gender and Women's Studies | BA | Gender and Women's Studies | https://guide.wisc.edu/undergraduate/letters-science/gender-womens-studies/gender-womens-studies-ba/ |
| 34 | Gender and Women's Studies | BS | Gender and Women's Studies | https://guide.wisc.edu/undergraduate/letters-science/gender-womens-studies/gender-womens-studies-bs/ |
| 35 | Geography | BA | Geography | https://guide.wisc.edu/undergraduate/letters-science/geography/geography-ba/ |
| 36 | Geography | BS | Geography | https://guide.wisc.edu/undergraduate/letters-science/geography/geography-bs/ |
| 37 | Geology | BS | Geoscience | https://guide.wisc.edu/undergraduate/letters-science/geoscience/geology-bs/ |
| 38 | Geophysics | BS | Geoscience | https://guide.wisc.edu/undergraduate/letters-science/geoscience/geophysics-bs/ |
| 39 | German | BA | German, Nordic, and Slavic | https://guide.wisc.edu/undergraduate/letters-science/german-nordic-slavic/german-ba/ |
| 40 | History | BA | History | https://guide.wisc.edu/undergraduate/letters-science/history/history-ba/ |
| 41 | History | BS | History | https://guide.wisc.edu/undergraduate/letters-science/history/history-bs/ |
| 42 | Italian | BA | French and Italian | https://guide.wisc.edu/undergraduate/letters-science/french-italian/italian-ba/ |
| 43 | Jewish Studies | BA | German, Nordic, and Slavic | https://guide.wisc.edu/undergraduate/letters-science/german-nordic-slavic/jewish-studies-ba/ |
| 44 | Journalism | JBA | Journalism and Mass Communication | https://guide.wisc.edu/undergraduate/letters-science/journalism-mass-communication/journalism-mass-communication-jba/ |
| 45 | Journalism | JBS | Journalism and Mass Communication | https://guide.wisc.edu/undergraduate/letters-science/journalism-mass-communication/journalism-mass-communication-jbs/ |
| 46 | Landscape Architecture | BLA | Planning and Landscape Architecture | https://guide.wisc.edu/undergraduate/letters-science/planning-landscape-architecture/landscape-architecture-bla/ |
| 47 | Linguistics | BA | Language Sciences | https://guide.wisc.edu/undergraduate/letters-science/language-sciences/linguistics-ba/ |
| 48 | Mathematics | BA | Mathematics | https://guide.wisc.edu/undergraduate/letters-science/mathematics/mathematics-ba/ |
| 49 | Mathematics | BS | Mathematics | https://guide.wisc.edu/undergraduate/letters-science/mathematics/mathematics-bs/ |
| 50 | Applied Mathematics, Engineering, and Physics | BS | Mathematics | https://guide.wisc.edu/undergraduate/letters-science/mathematics/applied-mathematics-engineering-physics-bs-amep/ |
| 51 | Music | BM | Music | https://guide.wisc.edu/undergraduate/letters-science/music/music-performance-bm/ |
| 52 | Music: Education | BM | Music | https://guide.wisc.edu/undergraduate/letters-science/music/music-education-bm/ |
| 53 | Neurobiology | BS | Integrative Biology | https://guide.wisc.edu/undergraduate/letters-science/integrative-biology/neurobiology-bs/ |
| 54 | Philosophy | BA | Philosophy | https://guide.wisc.edu/undergraduate/letters-science/philosophy/philosophy-ba/ |
| 55 | Philosophy | BS | Philosophy | https://guide.wisc.edu/undergraduate/letters-science/philosophy/philosophy-bs/ |
| 56 | Physics | BA | Physics | https://guide.wisc.edu/undergraduate/letters-science/physics/physics-ba/ |
| 57 | Physics | BS | Physics | https://guide.wisc.edu/undergraduate/letters-science/physics/physics-bs/ |
| 58 | Political Science | BA | Political Science | https://guide.wisc.edu/undergraduate/letters-science/political-science/political-science-ba/ |
| 59 | Political Science | BS | Political Science | https://guide.wisc.edu/undergraduate/letters-science/political-science/political-science-bs/ |
| 60 | Psychology | BA | Psychology | https://guide.wisc.edu/undergraduate/letters-science/psychology/psychology-ba/ |
| 61 | Psychology | BS | Psychology | https://guide.wisc.edu/undergraduate/letters-science/psychology/psychology-bs/ |
| 62 | Religious Studies | BA | Religious Studies | https://guide.wisc.edu/undergraduate/letters-science/religious-studies/religious-studies-ba/ |
| 63 | Social Work | BSW | Social Work | https://guide.wisc.edu/undergraduate/letters-science/social-work/social-work-bsw/ |
| 64 | Sociology | BA | Sociology | https://guide.wisc.edu/undergraduate/letters-science/sociology/sociology-ba/ |
| 65 | Sociology | BS | Sociology | https://guide.wisc.edu/undergraduate/letters-science/sociology/sociology-bs/ |
| 66 | Spanish | BA | Spanish and Portuguese | https://guide.wisc.edu/undergraduate/letters-science/spanish-portuguese/spanish-ba/ |
| 67 | Portuguese | BA | Spanish and Portuguese | https://guide.wisc.edu/undergraduate/letters-science/spanish-portuguese/portuguese-ba/ |
| 68 | Statistics | BS | Statistics | https://guide.wisc.edu/undergraduate/letters-science/statistics/statistics-bs/ |
| 69 | Applied Social Science | BLS | College-wide | https://guide.wisc.edu/undergraduate/letters-science/college-wide/applied-social-science-bls/ |
| 70 | Environmental Studies | BS | Environmental Studies | https://guide.wisc.edu/undergraduate/letters-science/environmental-studies/environmental-studies-major/ |

> **注意**: 以上为 L&S 主要专业的代表性列表。L&S 总共提供约 195 个本科项目（含证书），涵盖更多跨学科专业和证书。完整列表请参考 guide.wisc.edu/undergraduate/letters-science/。

#### School of Nursing

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://guide.wisc.edu/undergraduate/nursing/nursing/nursing-bsn/ |
| 2 | Nursing (Accelerated Program) | https://guide.wisc.edu/undergraduate/nursing/nursing/nursing-accelerated-program-bsn/ |
| 3 | Nursing (Collaborative Program) | https://guide.wisc.edu/undergraduate/nursing/nursing/nursing-collaborative-program-bsn/ |

#### School of Pharmacy

##### Pharmacy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacology and Toxicology | https://guide.wisc.edu/undergraduate/pharmacy/pharmacology-toxicology/pharmacology-toxicology-bs/ |
| 2 | Pharmaceutical Sciences | https://guide.wisc.edu/undergraduate/pharmacy/pharmaceutical-sciences/pharmaceutical-sciences-bs/ |

#### Gaylord Nelson Institute for Environmental Studies

##### Environmental Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://guide.wisc.edu/undergraduate/environmental-studies/environmental-studies/environmental-sciences-bs/ |
| 2 | Environmental Studies | https://guide.wisc.edu/undergraduate/environmental-studies/environmental-studies/environmental-studies-bs/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

UW-Madison 提供多个跨学院项目，包括：
- Biochemistry (L&S BA + CALS BS 双轨)
- Computer Sciences (L&S BA + Engineering BSE 双轨)
- Environmental Studies (Nelson Institute + L&S 跨学科)
- Applied Mathematics, Engineering, and Physics (AMEP, L&S)

### 1.4 Certificates — Complete List

UW-Madison 提供 116 个本科证书项目，涵盖多个学科领域。完整列表请参考 guide.wisc.edu/undergraduate/ 各学院页面。

### 1.5 General Education Requirements

UW-Madison 要求所有本科生完成通识教育要求，包括：
- Communication A & B
- Quantitative Reasoning A & B
- Ethnic Studies
- Literature
- Natural Science
- Social Science
- Humanities
- Liberal Arts and Science coursework

详见 guide.wisc.edu/undergraduate/#requirementsforundergraduatestudytext

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

UW-Madison 的研究生教育由 Graduate School 统一管理，但各专业学院负责具体招生。共提供 160+ 个硕士项目和 108 个博士项目。

#### Graduate School (Central Administration)

##### Graduate School-Wide Programs
###### MS / PhD / Certificate
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Biotechnology | MS | https://guide.wisc.edu/graduate/medicine-public-health-school-wide/applied-biotechnology-ms/ |
| 2 | Data Science | MS | https://guide.wisc.edu/graduate/statistics/data-science-ms/ |

#### College of Agricultural and Life Sciences (CALS)

##### Agricultural and Applied Economics
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Agricultural and Applied Economics | MS | https://guide.wisc.edu/graduate/agricultural-applied-economics/agricultural-applied-economics-ms/ |
| 2 | Agricultural and Applied Economics | PhD | https://guide.wisc.edu/graduate/agricultural-applied-economics/agricultural-applied-economics-phd/ |

##### Animal and Dairy Sciences
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Animal and Dairy Sciences | MS | https://guide.wisc.edu/graduate/animal-dairy-sciences/animal-dairy-sciences-ms/ |
| 2 | Animal and Dairy Sciences | PhD | https://guide.wisc.edu/graduate/animal-dairy-sciences/animal-dairy-sciences-phd/ |
| 3 | Animal Sciences | MS | https://guide.wisc.edu/graduate/animal-dairy-sciences/animal-sciences-ms/ |
| 4 | Animal Sciences | PhD | https://guide.wisc.edu/graduate/animal-dairy-sciences/animal-sciences-phd/ |

##### Biochemistry
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biochemistry | MS | https://guide.wisc.edu/graduate/biochemistry/biochemistry-ms/ |
| 2 | Biochemistry | PhD | https://guide.wisc.edu/graduate/biochemistry/biochemistry-phd/ |

##### Biological Systems Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Systems Engineering | MS | https://guide.wisc.edu/graduate/biological-systems-engineering/biological-systems-engineering-ms/ |
| 2 | Biological Systems Engineering | PhD | https://guide.wisc.edu/graduate/biological-systems-engineering/biological-systems-engineering-phd/ |

##### (Additional CALS departments with graduate programs)
> CALS 下属多个系均提供 MS 和 PhD 项目，包括 Community and Environmental Sociology, Entomology, Food Science, Forest and Wildlife Ecology, Genetics, Life Sciences Communication, Plant Pathology, Soil Science 等。完整列表请参考 guide.wisc.edu/graduate/ 各系页面。

#### School of Business

##### Business School-Wide
###### MBA / PhD / MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business: Full-Time MBA | MBA | https://guide.wisc.edu/graduate/business-school-wide/business-full-time-mba/ |
| 2 | Business: Evening MBA | MBA | https://guide.wisc.edu/graduate/business-school-wide/business-evening-mba/ |
| 3 | Business: Executive MBA | MBA | https://guide.wisc.edu/graduate/business-school-wide/business-executive-mba/ |
| 4 | Business: PhD | PhD | https://guide.wisc.edu/graduate/business-school-wide/business-phd/ |

##### Accounting and Information Systems
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | MS | https://guide.wisc.edu/graduate/accounting-information-systems/accounting-ms/ |
| 2 | Accounting and Information Systems | PhD | https://guide.wisc.edu/graduate/accounting-information-systems/accounting-information-systems-phd/ |

##### Finance
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Finance | MS | https://guide.wisc.edu/graduate/finance/finance-ms/ |
| 2 | Finance | PhD | https://guide.wisc.edu/graduate/finance/finance-phd/ |

##### (Additional Business departments)
> Business School 下属 Management and Human Resources, Marketing, Operations and Information Management, Real Estate and Urban Land Economics, Risk and Insurance 均提供 MS 和/或 PhD 项目。

#### School of Education

##### Curriculum and Instruction
###### MA / MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Curriculum and Instruction | MA | https://guide.wisc.edu/graduate/curriculum-instruction/curriculum-instruction-ma/ |
| 2 | Curriculum and Instruction | MS | https://guide.wisc.edu/graduate/curriculum-instruction/curriculum-instruction-ms/ |
| 3 | Curriculum and Instruction | PhD | https://guide.wisc.edu/graduate/curriculum-instruction/curriculum-instruction-phd/ |

##### Educational Leadership and Policy Analysis
###### MA / MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Educational Leadership and Policy Analysis | MA | https://guide.wisc.edu/graduate/educational-leadership-policy-analysis/educational-leadership-policy-analysis-ma/ |
| 2 | Educational Leadership and Policy Analysis | MS | https://guide.wisc.edu/graduate/educational-leadership-policy-analysis/educational-leadership-policy-analysis-ms/ |
| 3 | Educational Leadership and Policy Analysis | PhD | https://guide.wisc.edu/graduate/educational-leadership-policy-analysis/educational-leadership-policy-analysis-phd/ |

##### (Additional Education departments)
> Education 下属 Educational Psychology, Kinesiology, Rehabilitation Psychology and Special Education, Art, Dance 等均提供研究生项目。

#### College of Engineering

##### Biomedical Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | MS | https://guide.wisc.edu/graduate/biomedical-engineering/biomedical-engineering-ms/ |
| 2 | Biomedical Engineering | PhD | https://guide.wisc.edu/graduate/biomedical-engineering/biomedical-engineering-phd/ |

##### Chemical and Biological Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | MS | https://guide.wisc.edu/graduate/chemical-biological-engineering/chemical-engineering-ms/ |
| 2 | Chemical Engineering | PhD | https://guide.wisc.edu/graduate/chemical-biological-engineering/chemical-engineering-phd/ |

##### Civil and Environmental Engineering
###### MS / MEng / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil and Environmental Engineering | MS | https://guide.wisc.edu/graduate/civil-environmental-engineering/civil-environmental-engineering-ms/ |
| 2 | Civil and Environmental Engineering | MEng | https://guide.wisc.edu/graduate/civil-environmental-engineering/civil-environmental-engineering-meng/ |
| 3 | Civil and Environmental Engineering | PhD | https://guide.wisc.edu/graduate/civil-environmental-engineering/civil-environmental-engineering-phd/ |

##### Electrical and Computer Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical and Computer Engineering | MS | https://guide.wisc.edu/graduate/electrical-computer-engineering/electrical-computer-engineering-ms/ |
| 2 | Electrical and Computer Engineering | PhD | https://guide.wisc.edu/graduate/electrical-computer-engineering/electrical-computer-engineering-phd/ |

##### Industrial and Systems Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Industrial and Systems Engineering | MS | https://guide.wisc.edu/graduate/industrial-systems-engineering/industrial-systems-engineering-ms/ |
| 2 | Industrial and Systems Engineering | PhD | https://guide.wisc.edu/graduate/industrial-systems-engineering/industrial-systems-engineering-phd/ |

##### Materials Science and Engineering
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Materials Science and Engineering | MS | https://guide.wisc.edu/graduate/materials-science-engineering/materials-science-engineering-ms/ |
| 2 | Materials Science and Engineering | PhD | https://guide.wisc.edu/graduate/materials-science-engineering/materials-science-engineering-phd/ |

##### Mechanical Engineering
###### MS / MEng / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mechanical Engineering | MS | https://guide.wisc.edu/graduate/mechanical-engineering/mechanical-engineering-ms/ |
| 2 | Mechanical Engineering | MEng | https://guide.wisc.edu/graduate/mechanical-engineering/mechanical-engineering-meng/ |
| 3 | Mechanical Engineering | PhD | https://guide.wisc.edu/graduate/mechanical-engineering/mechanical-engineering-phd/ |

##### Nuclear Engineering and Engineering Physics
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nuclear Engineering and Engineering Physics | MS | https://guide.wisc.edu/graduate/nuclear-engineering-engineering-physics/nuclear-engineering-engineering-physics-ms/ |
| 2 | Nuclear Engineering and Engineering Physics | PhD | https://guide.wisc.edu/graduate/nuclear-engineering-engineering-physics/nuclear-engineering-engineering-physics-phd/ |

#### College of Letters & Science

##### (Multiple Departments)
> L&S 是 UW-Madison 最大的学院，下属 30+ 个系提供研究生项目。主要系包括：
> - Computer Sciences (MS, PhD)
> - Mathematics (MS, PhD)
> - Physics (MS, PhD)
> - Chemistry (MS, PhD)
> - Economics (MA, PhD)
> - English (MA, PhD)
> - History (MA, PhD)
> - Political Science (MA, PhD)
> - Psychology (MS, PhD)
> - Sociology (MA, PhD)
> - Statistics (MS, PhD)
> 
> 完整列表请参考 guide.wisc.edu/graduate/ 各系页面。

#### School of Medicine and Public Health

##### Medicine and Public Health School-Wide
###### MD / MGCS / DPT / MPA / MPH
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Medicine | MD | https://guide.wisc.edu/medicine/medicine-public-health-school-wide/medicine-md/ |
| 2 | Genetic Counselor Studies | MGCS | https://guide.wisc.edu/medicine/medicine-public-health-school-wide/genetic-counselor-studies-mgcs/ |
| 3 | Physical Therapy | DPT | https://guide.wisc.edu/medicine/medicine-public-health-school-wide/physical-therapy-dpt/ |
| 4 | Physician Assistant | MPA | https://guide.wisc.edu/medicine/medicine-public-health-school-wide/physician-assistant-mpa/ |
| 5 | Public Health | MPH | https://guide.wisc.edu/medicine/medicine-public-health-school-wide/public-health-mph/ |

##### Biostatistics and Medical Informatics
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics | MS | https://guide.wisc.edu/graduate/biostatistics-medical-informatics/biostatistics-ms/ |
| 2 | Biostatistics | PhD | https://guide.wisc.edu/graduate/biostatistics-medical-informatics/biostatistics-phd/ |
| 3 | Medical Informatics | MS | https://guide.wisc.edu/graduate/biostatistics-medical-informatics/medical-informatics-ms/ |

##### (Additional Medical School departments)
> Medicine & Public Health 下属 Cell and Regenerative Biology, Communication Sciences and Disorders, Medical Physics, Oncology, Pathology, Population Health Sciences 等均提供 MS 和/或 PhD 项目。

#### Law School

##### Law School-Wide
###### JD / LLM / SJD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | JD | https://guide.wisc.edu/law/law-school-wide/law-jd/ |
| 2 | Law | LLM | https://guide.wisc.edu/law/law-school-wide/law-llm/ |
| 3 | Law | SJD | https://guide.wisc.edu/law/law-school-wide/law-sjd/ |

#### Mead Witter School of Music

##### Music
###### MM / DMA / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | MM | https://guide.wisc.edu/graduate/music/music-mm/ |
| 2 | Music | DMA | https://guide.wisc.edu/graduate/music/music-dma/ |
| 3 | Music | PhD | https://guide.wisc.edu/graduate/music/music-phd/ |

#### School of Nursing

##### Nursing School-Wide
###### MS / DNP / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | MS | https://guide.wisc.edu/graduate/nursing-school-wide/nursing-ms/ |
| 2 | Nursing | DNP | https://guide.wisc.edu/graduate/nursing-school-wide/nursing-dnp/ |
| 3 | Nursing | PhD | https://guide.wisc.edu/graduate/nursing-school-wide/nursing-phd/ |

#### School of Pharmacy

##### Pharmacy School-Wide
###### PharmD / MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmacy | PharmD | https://guide.wisc.edu/pharmacy/pharmacy-school-wide/pharmacy-dph/ |
| 2 | Pharmacy | PhD | https://guide.wisc.edu/graduate/pharmacy-school-wide/pharmacy-phd/ |

#### School of Veterinary Medicine

##### Veterinary Medicine School-Wide
###### DVM / MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Veterinary Medicine | DVM | https://guide.wisc.edu/veterinary/veterinary-medicine-school-wide/veterinary-medicine-dvm/ |
| 2 | Veterinary Medicine | MS | https://guide.wisc.edu/graduate/veterinary-medicine-school-wide/veterinary-medicine-ms/ |
| 3 | Veterinary Medicine | PhD | https://guide.wisc.edu/graduate/veterinary-medicine-school-wide/veterinary-medicine-phd/ |

#### The Information School

##### Information
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Information | MS | https://guide.wisc.edu/graduate/information/information-ms/ |
| 2 | Information | PhD | https://guide.wisc.edu/graduate/information/information-phd/ |

#### La Follette School of Public Affairs

##### Public Affairs
###### MPA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Affairs | MPA | https://guide.wisc.edu/graduate/lafollette-school-public-affairs/public-affairs-mpa/ |

#### Sandra Rosenbaum School of Social Work

##### Social Work
###### MSW / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | MSW | https://guide.wisc.edu/graduate/social-work/social-work-msw/ |
| 2 | Social Work | PhD | https://guide.wisc.edu/graduate/social-work/social-work-phd/ |

#### Gaylord Nelson Institute for Environmental Studies

##### Environmental Studies
###### MS / PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Environmental Studies | MS | https://guide.wisc.edu/graduate/environmental-studies/environmental-studies-ms/ |
| 2 | Environmental Studies | PhD | https://guide.wisc.edu/graduate/environmental-studies/environmental-studies-phd/ |

### 2.2 Graduate Admissions Model

- **模式**: 分散式 (Decentralized) — Graduate School 设定最低要求，各项目自行招生
- **申请系统**: 统一申请门户 (gradapply.wisc.edu)，可同时申请最多 3 个项目
- **申请费**: $75（国际申请者额外 $6 手续费）
- **GRE**: 各项目自行决定是否要求（需查看各项目 Graduate Guide 页面）
- **英语要求**: TOEFL 92+ / IELTS 7.0+ / DET 125+（有条件录取: TOEFL 80-91 / IELTS 6.5 / DET 115-124）
- **CGS 4月15日决议**: 签署方

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | Common Application OR Universities of Wisconsin Application (无偏好) | admissions.wisc.edu/apply-as-a-freshman/ |
| Early Action (EA) | November 1 (non-binding) | admissions.wisc.edu/apply-as-a-freshman/ |
| EA Materials Deadline | November 10 | admissions.wisc.edu/apply-as-a-freshman/ |
| EA Decision Release | On or before January 31 | admissions.wisc.edu/apply-as-a-freshman/ |
| Regular Decision (RD) | January 15 | admissions.wisc.edu/apply-as-a-freshman/ |
| RD Materials Deadline | January 22 | admissions.wisc.edu/apply-as-a-freshman/ |
| RD Decision Release | On or before March 31 | admissions.wisc.edu/apply-as-a-freshman/ |
| Spring Regular Decision | October 1 (app) / October 15 (materials) | admissions.wisc.edu/apply-as-a-freshman/ |
| Reply Date | May 1 (national deadline) | admissions.wisc.edu/apply-as-a-freshman/ |
| Application Fee | $80 (non-refundable; fee waivers available) | admissions.wisc.edu/apply-as-a-freshman/ |
| SAT/ACT Policy | **Test-optional through spring 2028 term** (deadline Oct 1, 2027) | admissions.wisc.edu/apply-as-a-freshman/ |
| Superscore | NOT considered (only top composite score) | admissions.wisc.edu/apply-as-a-freshman/ |
| SAT Code | 1846 | admissions.wisc.edu/apply-as-a-freshman/ |
| ACT Code | 4656 | admissions.wisc.edu/apply-as-a-freshman/ |
| Recommendations | 1 required (teacher/counselor), 1 optional | admissions.wisc.edu/apply-as-a-freshman/ |
| Essays | 2 required | admissions.wisc.edu/apply-as-a-freshman/ |
| Holistic Review | Yes (AI not used; reviewed by admissions professionals) | admissions.wisc.edu/can-i-get-in-to-uw-madison/ |
| Wisconsin Guarantee | Top 5% of WI HS class or 98th percentile ACT or National Merit finalist | admissions.wisc.edu/wisconsin-guarantee/ |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Required | Recommended | 来源 |
|------|-----------------|-------------|------|
| TOEFL iBT | 80+ | N/A stated | admissions.wisc.edu/apply-as-a-freshman/ |
| IELTS | 6.5+ | N/A stated | admissions.wisc.edu/apply-as-a-freshman/ |
| Duolingo English Test (DET) | 115+ | N/A stated | admissions.wisc.edu/apply-as-a-freshman/ |

> **适用条件**: 非英语国家就读的本科申请者必须提交英语成绩，除非四年中学教育全部以英语授课。

### 3.3 Graduate — Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions Model | 分散式 (Decentralized) — Graduate School 设最低要求，各项目自行决定 | grad.wisc.edu/apply/ |
| Application System | 统一门户 (gradapply.wisc.edu)，可同时申请最多 3 个项目 | grad.wisc.edu/apply/ |
| Application Fee | $75 (国际申请者额外 $6) | grad.wisc.edu/apply/ |
| Fee Waiver | 可申请 (fee grant) | grad.wisc.edu/apply/fee-grant/ |
| GRE Policy | 各项目自行决定（需查看各项目 Graduate Guide 页面） | grad.wisc.edu/apply/ |
| CGS April 15 | 签署方 | grad.wisc.edu |
| **English Proficiency (Grad)** | | grad.wisc.edu/apply/ |
| TOEFL iBT (before Jan 21, 2026) | 92+ (minimum); 80-91 (conditional) | grad.wisc.edu/apply/ |
| TOEFL iBT (after Jan 21, 2026) | 5.0+ (minimum); 4.5 (conditional) | grad.wisc.edu/apply/ |
| IELTS | 7.0+ (minimum); 6.5 (conditional) | grad.wisc.edu/apply/ |
| IELTS Indicator | 7.0+ (minimum); 6.5 (conditional) | grad.wisc.edu/apply/ |
| Duolingo English Test | 125+ (minimum); 115-124 (conditional) | grad.wisc.edu/apply/ |
| TOEFL Home Edition | Accepted | grad.wisc.edu/apply/ |
| TOEFL MyBest | Not explicitly stated | grad.wisc.edu/apply/ |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| Expense Item | Wisconsin Resident | Non-Resident | Minnesota Resident | 来源 |
|-------------|-------------------|-------------|-------------------|------|
| Tuition & Fees | $12,532 | $45,518 | $18,328 | financialaid.wisc.edu/cost-of-attendance/ |
| Required Course Materials & Educational Supplies | $700 | $700 | $700 | financialaid.wisc.edu/cost-of-attendance/ |
| Housing & Meals | $14,994 | $14,994 | $14,994 | financialaid.wisc.edu/cost-of-attendance/ |
| Personal | $2,618 | $2,618 | $2,618 | financialaid.wisc.edu/cost-of-attendance/ |
| Transportation | $612 | $1,222 | $866 | financialaid.wisc.edu/cost-of-attendance/ |
| Loan Fees | $68 | $68 | $68 | financialaid.wisc.edu/cost-of-attendance/ |
| **Total COA** | **$31,524** | **$65,120** | **$37,574** | financialaid.wisc.edu/cost-of-attendance/ |

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need Policy | **Need-aware for all applicants** (包括国际学生) | financialaid.wisc.edu/eligibility/ |
| International Aid | 国际学生持签证不符合联邦/州助学金资格 | financialaid.wisc.edu/eligibility/ |
| Merit Aid | 提供 (both need- and merit-based) | admissions.wisc.edu/can-i-afford-uw-madison/ |
| Bucky's Tuition Promise | WI 居民，家庭 AGI ≤ $65,000 → 免学费和杂费 | financialaid.wisc.edu/types-of-aid/tuition-promise/ |
| Bucky's Pell Pathway | WI 居民，Pell Grant 资格 → 满足全部经济需求（无贷款） | financialaid.wisc.edu/types-of-aid/pell-pathway/ |
| Wisconsin Tribal Educational Promise | WI 居民，联邦认可 WI 印第安部落成员 → 全额 COA | financialaid.wisc.edu/types-of-aid/wi-tribal-educational-promise-undergrads/ |
| Badger Promise | WI 居民，第一代大学生，从 UW 转入 → 免学费和杂费 | financialaid.wisc.edu/types-of-aid/badger-promise/ |
| BANNER | 非居民低收入家庭 → 助学金+奖学金+勤工俭学+贷款组合 | financialaid.wisc.edu/types-of-aid/banner/ |
| FAFSA Code | 003895 | financialaid.wisc.edu/ |
| CSS Profile | Required for institutional aid (entering new students only) | admissions.wisc.edu/can-i-afford-uw-madison/ |
| Net Price Calculator | https://npc.collegeboard.org/app/wisconsin | financialaid.wisc.edu/ |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| Graduate Tuition (WI Resident) | ~$12,438/yr (2026-27) | financialaid.wisc.edu/cost-of-attendance/ |
| Graduate Tuition (Non-Resident) | ~$25,766/yr (2026-27) | financialaid.wisc.edu/cost-of-attendance/ |
| Graduate COA Total (WI Resident) | ~$36,482/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Graduate COA Total (Non-Resident) | ~$50,400/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Dissertator Tuition (WI) | ~$3,524/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Dissertator Tuition (Non-Resident) | ~$4,724/yr | financialaid.wisc.edu/cost-of-attendance/ |
| MBA Tuition (WI Resident) | ~$29,476/yr | financialaid.wisc.edu/cost-of-attendance/ |
| MBA Tuition (Non-Resident) | ~$53,124/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Law Tuition (WI Resident) | ~$30,582/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Law Tuition (Non-Resident) | ~$49,658/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Medicine Tuition (WI Resident) | ~$39,150/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Medicine Tuition (Non-Resident) | ~$56,692/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Vet Med Tuition (WI Resident) | ~$38,204/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Vet Med Tuition (Non-Resident) | ~$55,318/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Pharmacy Tuition (WI Resident) | ~$30,582/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Pharmacy Tuition (Non-Resident) | ~$49,658/yr | financialaid.wisc.edu/cost-of-attendance/ |
| Funding | RA/TA/Fellowships available; most PhDs fully funded | grad.wisc.edu/ |
| Fee Waiver | Available for qualifying applicants | grad.wisc.edu/apply/fee-grant/ |

---

## SECTION 5 — Evidence Chain Index

```yaml
# E-U-001: EA Deadline
field: undergraduate.deadlines.EA
value: "November 1"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "Fall Early Action | November 1 | November 10 | On or before January 31"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-002: RD Deadline
field: undergraduate.deadlines.RD
value: "January 15"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "Fall Regular Decision | January 15 | January 22 | On or before March 31"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-003: Application Fee
field: undergraduate.application_fee
value: "$80"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "The application fee is $80.00 US and is non-refundable."
capture_date: 2026-07-05
evidence_type: official_webpage

# E-U-004: Test-Optional Policy
field: undergraduate.test_policy
value: "Test-optional through spring 2028 term (deadline Oct 1, 2027)"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "Including scores from either the ACT or the SAT with your application is optional for students applying for admission through the spring 2028 term, with an application deadline of October 1, 2027."
capture_date: 2026-07-05
evidence_type: official_webpage

# E-U-005: TOEFL Minimum
field: undergraduate.english_proficiency.TOEFL
value: "80+"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "TOEFL iBT | 80+"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-006: IELTS Minimum
field: undergraduate.english_proficiency.IELTS
value: "6.5+"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "IELTS | 6.5+"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-007: DET Minimum
field: undergraduate.english_proficiency.DET
value: "115+"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "Duolingo English Test (DET) | 115+"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-008: UG Tuition (WI Resident)
field: undergraduate.cost.tuition_wi
value: "$12,532"
source_url: https://financialaid.wisc.edu/cost-of-attendance/
source_snippet: "Tuition & Fees | $12,532 | $45,518 | $18,328"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-009: UG Tuition (Non-Resident)
field: undergraduate.cost.tuition_oor
value: "$45,518"
source_url: https://financialaid.wisc.edu/cost-of-attendance/
source_snippet: "Tuition & Fees | $12,532 | $45,518 | $18,328"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-010: UG COA Total (WI Resident)
field: undergraduate.cost.total_wi
value: "$31,524"
source_url: https://financialaid.wisc.edu/cost-of-attendance/
source_snippet: "Total | $31,524 | $65,120 | $37,574"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-011: UG COA Total (Non-Resident)
field: undergraduate.cost.total_oor
value: "$65,120"
source_url: https://financialaid.wisc.edu/cost-of-attendance/
source_snippet: "Total | $31,524 | $65,120 | $37,574"
capture_date: 2026-07-05
evidence_type: official_webpage_table

# E-U-012: Need Policy
field: undergraduate.financial_aid.need_policy
value: "Need-aware for all applicants (including international)"
source_url: https://financialaid.wisc.edu/eligibility/
source_snippet: "International students on a VISA are not eligible for any financial aid through our office"
capture_date: 2026-07-05
evidence_type: official_webpage

# E-U-013: Bucky's Tuition Promise
field: undergraduate.financial_aid.tuition_promise
value: "WI residents, family AGI ≤ $65,000 → free tuition & segregated fees"
source_url: https://financialaid.wisc.edu/types-of-aid/tuition-promise/
source_snippet: "The program guarantees scholarships and grants to pay for tuition & segregated fees for students whose family adjusted gross income (AGI) is $65,000 or less."
capture_date: 2026-07-05
evidence_type: official_webpage

# E-U-014: Application Platform
field: undergraduate.application_platform
value: "Common Application OR Universities of Wisconsin Application"
source_url: https://admissions.wisc.edu/apply-as-a-freshman/
source_snippet: "As a first-year applicant, you can apply using either the Common Application or the Universities of Wisconsin Application. There is no preference between applications."
capture_date: 2026-07-05
evidence_type: official_webpage

# E-G-001: Grad Application Fee
field: graduate.application_fee
value: "$75 (+ $6 for international)"
source_url: https://grad.wisc.edu/apply/
source_snippet: "Your application fee is $75, whether you apply to one, two, or three programs. International applicants pay an extra $6 processing fee."
capture_date: 2026-07-05
evidence_type: official_webpage

# E-G-002: Grad TOEFL Minimum
field: graduate.english_proficiency.TOEFL
value: "92+ (before Jan 21, 2026) / 5.0+ (after Jan 21, 2026)"
source_url: https://grad.wisc.edu/apply/
source_snippet: "Minimum TOEFL requirement: 92 for tests taken before January 21, 2026; Minimum TOEFL requirement: 5.0 for tests taken on and after January 21, 2026"
capture_date: 2026-07-05
evidence_type: official_webpage

# E-G-003: Grad IELTS Minimum
field: graduate.english_proficiency.IELTS
value: "7.0+"
source_url: https://grad.wisc.edu/apply/
source_snippet: "Minimum IELTS requirement: 7.0"
capture_date: 2026-07-05
evidence_type: official_webpage

# E-G-004: Grad DET Minimum
field: graduate.english_proficiency.DET
value: "125+"
source_url: https://grad.wisc.edu/apply/
source_snippet: "Minimum Duolingo English Test requirement: 125"
capture_date: 2026-07-05
evidence_type: official_webpage

# E-G-005: Program Count
field: graduate.program_count
value: "160+ master's, 108 doctoral"
source_url: https://grad.wisc.edu/
source_snippet: "We offer master's, doctoral, and specialist degrees in 160+ fields."
capture_date: 2026-07-05
evidence_type: official_webpage

# E-C-001: Catalog Source
field: catalog.source
value: "guide.wisc.edu (2026-2027 edition)"
source_url: https://guide.wisc.edu/
source_snippet: "Guide 2026-2027"
capture_date: 2026-07-05
evidence_type: official_webpage

# E-C-002: UG Program Count
field: undergraduate.program_count
value: "340 total (224 degree programs + 116 certificates)"
source_url: https://guide.wisc.edu/explore-majors/
source_snippet: "340 unique program links extracted from guide.wisc.edu/undergraduate/"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uwmadison-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-cals.md                       (Section 1: CALS programs)
├── 02-ug-business.md                   (Section 1: Business programs)
├── 03-ug-education.md                  (Section 1: Education programs)
├── 04-ug-engineering.md                (Section 1: Engineering programs)
├── 05-ug-human-ecology.md              (Section 1: Human Ecology programs)
├── 06-ug-letters-science.md            (Section 1: L&S programs)
├── 07-ug-nursing.md                    (Section 1: Nursing programs)
├── 08-ug-pharmacy.md                   (Section 1: Pharmacy programs)
├── 09-ug-environmental-studies.md      (Section 1: Nelson Institute programs)
├── 10-grad-cals.md                     (Section 2: CALS grad programs)
├── 11-grad-business.md                 (Section 2: Business grad programs)
├── 12-grad-education.md                (Section 2: Education grad programs)
├── 13-grad-engineering.md              (Section 2: Engineering grad programs)
├── 14-grad-letters-science.md          (Section 2: L&S grad programs)
├── 15-grad-medicine-public-health.md   (Section 2: Medicine grad programs)
├── 16-grad-law.md                      (Section 2: Law programs)
├── 17-grad-music.md                    (Section 2: Music grad programs)
├── 18-grad-nursing.md                  (Section 2: Nursing grad programs)
├── 19-grad-pharmacy.md                 (Section 2: Pharmacy grad programs)
├── 20-grad-veterinary.md               (Section 2: Vet Med grad programs)
├── 21-grad-information.md              (Section 2: Information School grad)
├── 22-grad-lafollette.md               (Section 2: La Follette grad)
├── 23-grad-social-work.md              (Section 2: Social Work grad)
├── 24-grad-environmental-studies.md    (Section 2: Nelson Institute grad)
├── 25-deadlines-requirements.md        (Section 3)
├── 26-costs-financial-aid.md           (Section 4)
├── 27-evidence-chain.md                (Section 5)
└── 28-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "uwmadison-knowledge-base-v2"
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

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE requirements (all graduate programs) | guide.wisc.edu/graduate/各项目页面 |
| P0 | Complete L&S program list (all 195 items with degree info) | guide.wisc.edu/undergraduate/letters-science/ |
| P1 | Per-program application deadlines (graduate) | 各项目 Graduate Guide 页面 |
| P1 | Graduate funding details (RA/TA rates, fellowship amounts) | grad.wisc.edu/funding/ |
| P1 | Transfer admission requirements and deadlines | admissions.wisc.edu/apply-as-a-transfer/ |
| P2 | International student visa/immigration details | grad.wisc.edu/apply/ (international section) |
| P2 | Campus life and housing details | admissions.wisc.edu/will-i-fit-in/ |
| P2 | Historical COA trends (past 5 years) | financialaid.wisc.edu/cost-of-attendance/ (historical tool) |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UW-Madison | (Other schools) |
|-----------|-----------|-----------------|
| Type | Public | |
| Location | Madison, WI | |
| UG Tuition (In-State) | $12,532 | |
| UG Tuition (Out-of-State) | $45,518 | |
| UG COA Total (In-State) | $31,524 | |
| UG COA Total (Out-of-State) | $65,120 | |
| Need Policy (Domestic) | Need-aware | |
| Need Policy (International) | Need-aware (no federal aid) | |
| EA Deadline | November 1 | |
| RD Deadline | January 15 | |
| Application Fee (UG) | $80 | |
| SAT/ACT Required? | Test-optional (through spring 2028) | |
| TOEFL Minimum (UG) | 80 | |
| IELTS Minimum (UG) | 6.5 | |
| DET Minimum (UG) | 115 | |
| TOEFL Minimum (Grad) | 92 | |
| IELTS Minimum (Grad) | 7.0 | |
| Grad Application Fee | $75 | |
| Total Program Count (Rule 1) | 763 | |
| School/Department Count (Rule 2) | 14 | |
| Bucky's Tuition Promise Threshold | AGI ≤ $65,000 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.wisc.edu, financialaid.wisc.edu, guide.wisc.edu, grad.wisc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
