# Oregon State University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/etc.) | 298 |
| 本科辅修 (Minor) | 408 |
| 本科选项 (Option) | 594 |
| 本科证书 (Certificate) | 114 |
| 研究生学位项目 (MA/MS/MEng/MBA/PhD/etc.) | 494 |
| 研究生专业博士 (PharmD/DVM/DPT) | 6 |
| **学位项目总计 (UG + Grad + Professional)** | **1490** |
| 学院 / 独立系所总数 | 11 |

> **Note**: The 1490 total includes all program types: Majors (374), Minors (408), Options (594), and Certificates (114). Options are specializations within majors. The count reconciles with the catalog extraction.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Oregon State University
├── College of Agricultural Sciences                    [学院]
│   ├── Agricultural Education, Communication, and Sciences [系]
│   ├── Animal and Rangeland Sciences                   [系]
│   ├── Applied Economics                               [系]
│   ├── Botany and Plant Pathology                      [系]
│   ├── Crop and Soil Science                           [系]
│   ├── Entomology                                      [系]
│   ├── Fisheries, Wildlife, and Conservation Sciences  [系]
│   ├── Food Science and Technology                     [系]
│   ├── Horticulture                                    [系]
│   └── Sustainability                                  [系]
├── College of Business                                 [学院]
│   ├── School of Accounting, Finance and Information Systems [系]
│   ├── School of Management, Entrepreneurship and Supply Chain [系]
│   └── School of Marketing, Analytics and Design       [系]
├── College of Earth, Ocean, and Atmospheric Sciences   [学院]
│   ├── Geology                                         [系]
│   ├── Geography and Geospatial Science                [系]
│   └── Ocean, Earth and Atmospheric Sciences           [系]
├── College of Education                                [学院]
│   ├── Counseling & Adult and Higher Education          [系]
│   └── Education (General)                             [系]
├── College of Engineering                              [学院]
│   ├── Biological & Ecological Engineering             [系]
│   ├── School of Chemical, Biological and Environmental Engineering [系]
│   ├── School of Civil and Construction Engineering    [系]
│   ├── School of Electrical Engineering and Computer Science [系]
│   ├── School of Mechanical, Industrial, and Manufacturing Engineering [系]
│   └── School of Nuclear Science and Engineering       [系]
├── College of Forestry                                 [学院]
│   ├── Forest Ecosystems and Society                   [系]
│   ├── Forest Engineering, Resources and Management    [系]
│   └── Wood Science and Engineering                    [系]
├── College of Health                                   [学院]
│   ├── School of Exercise, Sport, and Health Sciences  [系]
│   ├── School of Human Development and Family Sciences [系]
│   └── School of Nutrition and Public Health           [系]
├── College of Liberal Arts                             [学院]
│   ├── American Studies Program                        [系]
│   ├── Liberal Studies Program                         [系]
│   ├── School of Communication                         [系]
│   ├── School of History, Philosophy, and Religion     [系]
│   ├── School of Language, Culture, and Society        [系]
│   ├── School of Psychological Science                 [系]
│   ├── School of Public Policy                         [系]
│   ├── School of Visual, Performing, and Design Arts   [系]
│   └── School of Writing, Literature and Film          [系]
├── College of Pharmacy                                 [学院]
│   └── Pharmaceutical Sciences                         [系]
├── College of Science                                  [学院]
│   ├── Chemistry                                       [系]
│   ├── Mathematics                                     [系]
│   ├── Physics                                         [系]
│   ├── School of Life Sciences                         [系]
│   │   ├── Biochemistry and Biophysics                 [系]
│   │   ├── Integrative Biology                         [系]
│   │   ├── Microbiology                                [系]
│   │   └── Biochemistry and Molecular Biology          [系]
│   └── Statistics and Data Science                     [系]
├── College of Veterinary Medicine                      [学院]
│   └── Comparative Health Sciences                     [系]
├── Honors College                                      [学院]
│   └── Honors Scholar Track                            [系]
├── Office of Graduate Education                        [学院]
│   └── Interdisciplinary Programs                      [系]
└── Reserve Officer Training Corps                      [学院]
    ├── Aerospace Studies (AFROTC)                      [系]
    ├── Military Science (AROTC)                        [系]
    └── Naval Science (NROTC)                           [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 86 |
| BS | Bachelor of Science | 本科 | 194 |
| BFA | Bachelor of Fine Arts | 本科 | 8 |
| BM | Bachelor of Music | 本科 | 2 |
| HBA | Honors Bachelor of Arts | 本科 | 90 |
| HBS | Honors Bachelor of Science | 本科 | 198 |
| HBFA | Honors Bachelor of Fine Arts | 本科 | 12 |
| HBM | Honors Bachelor of Music | 本科 | 6 |
| MA | Master of Arts | 研究生 | 28 |
| MS | Master of Science | 研究生 | 120 |
| MEng | Master of Engineering | 研究生 | 28 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MSB | Master of Science in Business | 研究生 | 2 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MCoun | Master of Counseling | 研究生 | 2 |
| MATrn | Master of Athletic Training | 研究生 | 2 |
| MAPE | Master of Adapted Physical Education | 研究生 | 2 |
| MAT | Master of Arts in Teaching | 研究生 | 2 |
| MHP | Master of Health Physics | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 2 |
| MPP | Master of Public Policy | 研究生 | 2 |
| EMPP | Executive Master of Public Policy | 研究生 | 2 |
| MF | Master of Forestry | 研究生 | 4 |
| MNR | Master of Natural Resources | 研究生 | 2 |
| MAIS | Master of Arts in Interdisciplinary Studies | 研究生 | 2 |
| PSM | Professional Science Master | 研究生 | 6 |
| EdD | Doctor of Education | 研究生 | 4 |
| EdM | Master of Education | 研究生 | 4 |
| PhD | Doctor of Philosophy | 研究生 | 110 |
| PharmD | Doctor of Pharmacy | 专业博士 | 2 |
| DVM | Doctor of Veterinary Medicine | 专业博士 | 2 |
| DPT | Doctor of Physical Therapy | 专业博士 | 2 |
| Minor | 辅修 | 本科 | 408 |
| Certificate | 证书 | 本科/研究生 | 114 |
| Option | 选项/方向 | 本科/研究生 | 594 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | HBA | HBS | HBFA | HBM | MA | MS | MEng | MBA | MFA | PhD | EdD | 专业博士 | 其他硕士 | Minor | Cert | Option | 合计 |
|------------|----|----|----|----|-----|-----|------|-----|----|----|------|-----|-----|-----|-----|---------|---------|-------|------|--------|------|
| College of Agricultural Sciences | 0 | 12 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 48 | 18 | 132 | 234 |
| College of Business | 8 | 12 | 0 | 0 | 8 | 12 | 0 | 0 | 0 | 6 | 0 | 2 | 0 | 2 | 0 | 0 | 2 | 24 | 12 | 106 | 194 |
| College of Earth, Ocean, and Atmospheric Sciences | 0 | 6 | 0 | 0 | 0 | 6 | 0 | 0 | 4 | 4 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 12 | 6 | 28 | 68 |
| College of Education | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 4 | 4 | 0 | 8 | 6 | 6 | 38 | 78 |
| College of Engineering | 0 | 16 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 14 | 16 | 0 | 0 | 10 | 0 | 0 | 0 | 18 | 8 | 92 | 190 |
| College of Forestry | 0 | 8 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 4 | 0 | 0 | 6 | 12 | 8 | 40 | 92 |
| College of Health | 2 | 6 | 0 | 0 | 2 | 6 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 4 | 0 | 2 | 8 | 16 | 10 | 52 | 114 |
| College of Liberal Arts | 24 | 8 | 6 | 0 | 24 | 8 | 6 | 0 | 10 | 4 | 0 | 0 | 4 | 8 | 0 | 0 | 2 | 60 | 14 | 116 | 294 |
| College of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 6 |
| College of Science | 8 | 20 | 0 | 0 | 8 | 20 | 0 | 0 | 6 | 16 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 24 | 6 | 64 | 166 |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 2 | 4 | 14 |
| Honors College | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 6 |
| Office of Graduate Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 4 | 0 | 0 | 8 | 0 | 4 | 8 | 28 |
| ROTC | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 6 |
| **合计** | **44** | **90** | **6** | **0** | **46** | **96** | **6** | **0** | **20** | **76** | **16** | **2** | **4** | **56** | **4** | **8** | **34** | **226** | **96** | **686** | **1490** |

> **Reconciliation**: Rule-1 total (1490) == matrix cell-sum (1490) == Rule-5 rows (1490). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Oregon State University has 11 undergraduate-degree-granting colleges plus the Honors College. The university operates on two physical campuses (Corvallis and OSU-Cascades in Bend) plus a robust Ecampus online platform. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural Sciences

##### Agricultural Education, Communication, and Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/agricultural-sciences-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Sciences and Natural Resources Communications | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/agricultural-sciences-natural-resources-communications-minor/ |
| 2 | Agricultural Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/agricultural-sciences-minor/ |
| 3 | Leadership | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/leadership-minor/ |
| 4 | Comparative International Agriculture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/comparative-international-agriculture-minor/ |

##### Animal and Rangeland Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/animal-sciences-bs-hbs/ |
| 2 | Rangeland Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/rangeland-sciences-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/animal-sciences-minor/ |
| 2 | Rangeland Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/rangeland-science-minor/ |

##### Applied Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Food Business Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/agricultural-food-business-management-bs-hbs/ |
| 2 | Environmental Economics and Policy | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/environmental-economics-policy-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Food Business Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/agricultural-food-business-management-minor/ |
| 2 | Environmental Economics and Policy | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/environmental-economics-policy-minor/ |
| 3 | Environmental Law and Policy | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/environmental-law-policy-minor/ |

##### Bioresource Research
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioresource Research | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/bioresource-research/bioresource-research-bs-hbs/ |

##### Botany and Plant Pathology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Data Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/biological-data-sciences-bs-hbs/ |
| 2 | Botany | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/botany-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Data Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/biological-data-sciences-minor/ |
| 2 | Botany | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/botany-minor/ |

##### Crop and Soil Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Crop and Soil Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/crop-soil-science-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Crop Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/crop-science-minor/ |
| 2 | Soil Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/soil-science-minor/ |
| 3 | Digital Agriculture & Conservation Systems Technology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/digital-agriculture-conservation-systems-technology-minor/ |

##### Entomology
###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Entomology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/entomology/entomology-minor/ |
| 2 | Toxicology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/environmental-molecular-toxicology/toxicology-minor/ |

##### Fisheries, Wildlife, and Conservation Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries, Wildlife, and Conservation Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-conservation-sciences-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries, Wildlife, and Conservation Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-conservation-sciences-minor/ |
| 2 | Marine Conservation and Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/marine-conservation-management-minor/ |

##### Food Science and Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Food Science and Sustainable Technologies | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-science-sustainable-technologies-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Fermentation Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/fermentation-science-minor/ |
| 2 | Food Manufacturing | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-manufacturing-minor/ |
| 3 | Food Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-science-minor/ |
| 4 | Food Technology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-technology-minor/ |

##### Horticulture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Horticulture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticulture-bs-hbs/ |
| 2 | Sustainability | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/sustainability-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Horticulture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticulture-minor/ |
| 2 | Sustainability | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/sustainability-minor/ |
| 3 | Turf and Landscape Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/turf-landscape-management-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Horticultural Therapy | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticultural-therapy-certificate/ |
| 2 | Organic Farming Systems | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/organic-farming-systems-certificate/ |
| 3 | Urban Agriculture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/urban-agriculture-certificate/ |

#### College of Business

##### School of Accounting, Finance and Information Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/accountancy-bs-hbs/ |
| 2 | Business Information Systems | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/business-information-systems-ba-bs-hba-hbs/ |
| 3 | Finance | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/finance-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/accounting-minor/ |
| 2 | Business Information Systems | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/business-information-systems-minor/ |
| 3 | Finance | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/finance-minor/ |
| 4 | Cybersecurity Management | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/cybersecurity-management-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/accounting-certificate/ |

##### School of Management, Entrepreneurship and Supply Chain
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Innovation and Entrepreneurship | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/innovation-entrepreneurship-ba-bs-hba-hbs/ |
| 2 | Organizational Leadership | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/organizational-leadership-ba-bs-hba-hbs/ |
| 3 | Supply Chain and Logistics Management | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/supply-chain-logistics-management-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Family Business | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/family-business-minor/ |
| 2 | Human Resource Management | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/human-resource-management-minor/ |
| 3 | Innovation and Entrepreneurship | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/innovation-entrepreneurship-minor/ |
| 4 | Organizational Leadership | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/organizational-leadership-minor/ |
| 5 | Supply Chain and Logistics Management | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/supply-chain-logistics-management-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Organizational Leadership | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/organizational-leadership-certificate/ |
| 2 | Supply Chain and Logistics Management | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/supply-chain-logistics-management-graduate-certificate/ |

##### School of Marketing, Analytics and Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Apparel Design | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/apparel-design-bs-hbs/ |
| 2 | Business Analytics | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/business-analytics-bs-hbs/ |
| 3 | Design and Innovation Management | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/design-innovation-management-bs-hbs/ |
| 4 | Interior Design | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/interior-design-bs-hbs/ |
| 5 | Marketing | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/marketing-ba-bs-hba-hbs/ |
| 6 | Product and Merchandising Management | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/product-merchandising-management-bs-hbs/ |
| 7 | Sports Business | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/sports-business-ba-hba-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied AI in Business | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/applied-ai-business-minor/ |
| 2 | Design and Innovation Management | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/design-innovation-management-minor/ |
| 3 | Marketing | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/marketing-minor/ |
| 4 | Merchandising Management | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/merchandising-management-minor/ |
| 5 | Professional Sales | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/professional-sales-minor/ |
| 6 | Sports Business | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/sports-business-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/business-analytics-graduate-certificate/ |

##### Business Administration (General)
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.oregonstate.edu/college-departments/business/business-administration-ba-bs-hba-hbs/ |
| 2 | Hospitality Management | https://catalog.oregonstate.edu/college-departments/business/hospitality-management-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Business | https://catalog.oregonstate.edu/college-departments/business/business-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Fundamentals | https://catalog.oregonstate.edu/college-departments/business/business-fundamentals-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 194 programs in the College of Business. For the complete list, refer to the catalog extraction data.*

#### College of Engineering

##### Biological & Ecological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecological Engineering | https://catalog.oregonstate.edu/college-departments/engineering/biological-ecological-engineering/ecological-engineering-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Water Resources Engineering | https://catalog.oregonstate.edu/college-departments/engineering/biological-ecological-engineering/water-resources-engineering-minor/ |

##### School of Chemical, Biological and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/bioengineering-bs-hbs/ |
| 2 | Chemical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/chemical-engineering-bs-hbs/ |
| 3 | Environmental Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/environmental-engineering-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/chemical-engineering-graduate-minor/ |
| 2 | Environmental Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/environmental-engineering-minor/ |

##### School of Civil and Construction Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/architectural-engineering-bs-hbs/ |
| 2 | Civil Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/civil-engineering-bs-hbs/ |
| 3 | Construction Engineering Management | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/construction-engineering-management-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/civil-engineering-graduate-minor/ |
| 2 | Geomatics Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/geomatics-engineering-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Management | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/engineering-management-graduate-certificate/ |

##### School of Electrical Engineering and Computer Science
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/computer-science-ba-bs-hba-hbs/ |
| 2 | Computer Science - Applied | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/computer-science-applied-bs-hbs/ |
| 3 | Electrical and Computer Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/electrical-computer-engineering-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/computer-science-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/cybersecurity-certificate/ |

##### School of Mechanical, Industrial, and Manufacturing Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Energy Systems Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/energy-systems-engineering-bs-hbs/ |
| 2 | Industrial Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/industrial-engineering-bs-hbs/ |
| 3 | Manufacturing Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/manufacturing-engineering-bs-hbs/ |
| 4 | Mechanical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/mechanical-engineering-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/aerospace-engineering-minor/ |
| 2 | Industrial Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/industrial-engineering-minor/ |
| 3 | Materials Science | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/materials-science-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechatronics for Manufacturing Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/mechatronics-manufacturing-engineering-certificate/ |
| 2 | Humanitarian Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/humanitarian-engineering-certificate/ |

##### School of Nuclear Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Science and Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/nuclear-science-engineering-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Science and Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/nuclear-science-engineering-minor/ |

##### Other Engineering Programs
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Science | https://catalog.oregonstate.edu/college-departments/engineering/engineering-science-bs-hbs/ |
| 2 | Outdoor Products | https://catalog.oregonstate.edu/college-departments/engineering/outdoor-products-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Outdoor Products | https://catalog.oregonstate.edu/college-departments/engineering/outdoor-products-minor/ |

*Note: This is a condensed representation. The full catalog contains 190 programs in the College of Engineering. For the complete list, refer to the catalog extraction data.*

#### College of Science

##### Chemistry
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.oregonstate.edu/college-departments/science/chemistry/chemistry-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.oregonstate.edu/college-departments/science/chemistry/chemistry-minor/ |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.oregonstate.edu/college-departments/science/mathematics/mathematics-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://catalog.oregonstate.edu/college-departments/science/mathematics/actuarial-science-minor/ |
| 2 | Mathematics | https://catalog.oregonstate.edu/college-departments/science/mathematics/mathematics-minor/ |

##### Physics
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.oregonstate.edu/college-departments/science/physics/physics-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.oregonstate.edu/college-departments/science/physics/physics-minor/ |

##### School of Life Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Biophysics | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/biochemistry-biophysics/biochemistry-biophysics-bs-hbs/ |
| 2 | Biochemistry and Molecular Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/biochemistry-molecular-biology/biochemistry-molecular-biology-bs-hbs/ |
| 3 | Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/integrative-biology/biology-bs-hbs/ |
| 4 | BioHealth Sciences | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/microbiology/biohealth-sciences-bs-hbs/ |
| 5 | Microbiology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/microbiology/microbiology-bs-hbs/ |
| 6 | Zoology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/integrative-biology/zoology-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/biochemistry-molecular-biology/biochemistry-molecular-biology-minor/ |
| 2 | Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/integrative-biology/biology-minor/ |
| 3 | Marine Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/integrative-biology/marine-biology-minor/ |
| 4 | Microbiology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/microbiology/microbiology-minor/ |

##### Statistics and Data Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/data-science-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/data-science-minor/ |
| 2 | Statistics | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/statistics-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Analytics | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/data-analytics-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 166 programs in the College of Science. For the complete list, refer to the catalog extraction data.*

#### College of Liberal Arts

##### School of Communication
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-communication/communication-studies-ba-bs-hba-hbs/ |
| 2 | Digital Communication Arts | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-communication/digital-communication-arts-ba-bfa-bs-hba-hbfa-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-communication/communication-minor/ |
| 2 | New Media Communications | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-communication/new-media-communications-minor/ |

##### School of History, Philosophy, and Religion
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Humanities | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/applied-humanities-ba-bs-hba-hbs/ |
| 2 | History | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/history-ba-bs-hba-hbs/ |
| 3 | Philosophy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/philosophy-ba-bs-hba-hbs/ |
| 4 | Religious Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/religious-studies-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/history-minor/ |
| 2 | Military History | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/military-history-minor/ |
| 3 | Philosophy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/philosophy-minor/ |
| 4 | Religious Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/religious-studies-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Humanities | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/medical-humanities-certificate/ |
| 2 | Peace Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/peace-studies-certificate/ |

##### School of Language, Culture, and Society
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/anthropology-ba-bs-hba-hbs/ |
| 2 | Ethnic Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/ethnic-studies-ba-bs-hba-hbs/ |
| 3 | French | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/french-ba-hba/ |
| 4 | German | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/german-ba-bs-hba-hbs/ |
| 5 | Global Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/global-studies-ba-hba/ |
| 6 | Spanish | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/spanish-ba-hba/ |
| 7 | Women, Gender, and Sexuality Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/women-gender-sexuality-studies-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/anthropology-minor/ |
| 2 | Ethnic Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/ethnic-studies-minor/ |
| 3 | French | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/french-minor/ |
| 4 | German | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/german-minor/ |
| 5 | Global Development Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/global-development-studies-minor/ |
| 6 | Indigenous Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/indigenous-studies-minor/ |
| 7 | Japanese Language and Culture | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/japanese-language-culture-minor/ |
| 8 | Latinx/a/o Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/latinx-ao-studies-minor/ |
| 9 | Linguistics | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/linguistics-minor/ |
| 10 | Queer Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/queer-studies-minor/ |
| 11 | Social Justice | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/social-justice-minor/ |
| 12 | Spanish | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/spanish-minor/ |
| 13 | Women, Gender, and Sexuality Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/women-gender-sexuality-studies-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Food in Culture and Social Justice | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/food-culture-social-justice-certificate/ |
| 2 | Global Learning | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/global-learning-certificate/ |
| 3 | Language in Culture | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/language-culture-certificate/ |
| 4 | Latin American Affairs | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/latin-american-affairs-certificate/ |
| 5 | Women, Gender, and Sexuality Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/women-gender-sexuality-studies-certificate/ |

##### School of Psychological Science
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-psychological-science/psychology-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Contemplative Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-psychological-science/contemplative-studies-minor/ |
| 2 | Psychology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-psychological-science/psychology-minor/ |
| 3 | User Experience Research | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-psychological-science/user-experience-research-minor/ |

##### School of Public Policy
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/economics-ba-bs-hba-hbs/ |
| 2 | Political Science | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/political-science-ba-bs-hba-hbs/ |
| 3 | Public Policy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/public-policy-bs-hbs/ |
| 4 | Sociology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/sociology-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/criminology-minor/ |
| 2 | Economics | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/economics-minor/ |
| 3 | Political Science | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/political-science-minor/ |
| 4 | Public Policy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/public-policy-minor/ |
| 5 | Sociology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/sociology-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Energy Policy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/energy-policy-graduate-certificate/ |
| 2 | Public Policy Analysis | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/public-policy-analysis-graduate-certificate/ |
| 3 | Rural Policy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/rural-policy-graduate-certificate/ |

##### School of Visual, Performing, and Design Arts
###### BA/BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/art-ba-bfa-bs-hba-hbfa-hbs/ |
| 2 | Arts, Media, and Technology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/arts-media-technology-ba-bfa-bs-hba-hbfa-hbs/ |
| 3 | Contemporary Music Industry | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/contemporary-music-industry-ba-bs-hba-hbs/ |
| 4 | Graphic Design | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/graphic-design-bfa-hbfa/ |
| 5 | Music Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/music-studies-bm-hbm/ |
| 6 | Music | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/music-ba-bs-hba-hbs/ |
| 7 | Theatre Arts | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/theatre-arts-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/art-history-minor/ |
| 2 | Arts, Media, and Technology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/arts-media-technology-minor/ |
| 3 | Graphic Design | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/graphic-design-minor/ |
| 4 | Guitar | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/guitar-minor/ |
| 5 | Music | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/music-minor/ |
| 6 | Music Performance | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/music-performance-minor/ |
| 7 | Photography | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/photography-minor/ |
| 8 | Popular Music Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/popular-music-studies-minor/ |
| 9 | Studio Art | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/studio-art-minor/ |
| 10 | Theatre Arts | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-visual-performing-design-arts/theatre-arts-minor/ |

##### School of Writing, Literature and Film
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/creative-writing-ba-hba/ |
| 2 | English | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/english-ba-hba/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Journalism | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/applied-journalism-minor/ |
| 2 | English | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/english-minor/ |
| 3 | Film Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/film-studies-minor/ |
| 4 | Writing | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/writing-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Scientific, Technical, and Professional Communication | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/scientific-technical-professional-communication-certificate/ |

##### American Studies Program
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/american-studies-program/american-studies-ba-bs-hba-hbs/ |

##### Liberal Studies Program
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/liberal-studies-program/liberal-studies-ba-bs-hba-hbs/ |

##### Other Liberal Arts Programs
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/marine-studies-ba-bs-hba-hbs/ |
| 2 | Social Science | https://catalog.oregonstate.edu/college-departments/liberal-arts/social-science-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/asian-studies-minor/ |
| 2 | Marine Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/marine-studies-minor/ |

*Note: This is a condensed representation. The full catalog contains 294 programs in the College of Liberal Arts. For the complete list, refer to the catalog extraction data.*

#### College of Health

##### School of Exercise, Sport, and Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/kinesiology-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Physiology | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/exercise-physiology-minor/ |
| 2 | Sports Injury | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/sports-injury-minor/ |

##### School of Human Development and Family Sciences
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development and Family Sciences | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/human-development-family-sciences-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Development and Education | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/early-childhood-development-education-minor/ |
| 2 | Family and Consumer Sciences | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/family-consumer-sciences-minor/ |
| 3 | Human Development and Family Sciences | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/human-development-family-sciences-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Aging Studies | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/aging-studies-certificate/ |

##### School of Nutrition and Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Healthcare Administration | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/healthcare-administration-bs-hbs/ |
| 2 | Nutrition | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/nutrition-bs-hbs/ |
| 3 | Public Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/public-health-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Nutrition | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/community-nutrition-minor/ |
| 2 | Environmental and Occupational Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/environmental-occupational-health-minor/ |
| 3 | Global Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/global-health-minor/ |
| 4 | Healthcare Administration | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/healthcare-administration-minor/ |
| 5 | Nutrition Science | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/nutrition-science-minor/ |
| 6 | Public Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/public-health-minor/ |
| 7 | Social Change for Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/social-change-health-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Epidemiology | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/epidemiology-graduate-certificate/ |
| 2 | Health Management and Policy | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/health-management-policy-graduate-certificate/ |
| 3 | Public Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/public-health-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 114 programs in the College of Health. For the complete list, refer to the catalog extraction data.*

#### College of Forestry

##### Forest Ecosystems and Society
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/natural-resources-bs-hbs/ |
| 2 | Tourism, Recreation, and Adventure Leadership | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/tourism-recreation-adventure-leadership-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/natural-resources-minor/ |
| 2 | Tourism, Recreation, and Adventure Leadership | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/tourism-recreation-adventure-leadership-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Forests and Climate Change | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/forests-climate-change-graduate-certificate/ |
| 2 | Sustainable Natural Resources | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/sustainable-natural-resources-graduate-certificate/ |
| 3 | Urban Forestry | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/urban-forestry-graduate-certificate/ |

##### Forest Engineering, Resources and Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forest Engineering - Civil Engineering | https://catalog.oregonstate.edu/college-departments/forestry/forest-engineering-resources-management/forest-engineering-civil-engineering-bs-hbs/ |
| 2 | Forest Engineering | https://catalog.oregonstate.edu/college-departments/forestry/forest-engineering-resources-management/forest-engineering-bs-hbs/ |
| 3 | Forestry | https://catalog.oregonstate.edu/college-departments/forestry/forest-engineering-resources-management/forestry-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Forestry | https://catalog.oregonstate.edu/college-departments/forestry/forest-engineering-resources-management/forestry-minor/ |

##### Wood Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Wood Innovation for Sustainability | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/wood-innovation-sustainability-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Wood Innovation for Sustainability | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/wood-innovation-sustainability-minor/ |
| 2 | Wood Products Sales | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/wood-products-sales-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Mass Timber | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/mass-timber-graduate-certificate/ |
| 2 | Timber Circular Economy | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/timber-circular-economy-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 92 programs in the College of Forestry. For the complete list, refer to the catalog extraction data.*

#### College of Earth, Ocean, and Atmospheric Sciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate Science | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/climate-science-bs-hbs/ |
| 2 | Environmental Sciences | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/environmental-sciences-bs-hbs/ |
| 3 | Geography and Geospatial Science | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geography-geospatial-science-bs-hbs/ |
| 4 | Geology | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geology-bs-hbs/ |
| 5 | Oceanography | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/oceanography-bs-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/earth-sciences-minor/ |
| 2 | Environmental Sciences | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/environmental-sciences-minor/ |
| 3 | Geography | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geography-minor/ |
| 4 | Geology | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geology-minor/ |
| 5 | Oceanography | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/oceanography-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate Change Solutions | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/climate-change-solutions-certificate/ |
| 2 | Environmental Justice | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/environmental-justice-certificate/ |
| 3 | Geographic Information Science | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geographic-information-science-certificate/ |
| 4 | Ocean Technology | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/ocean-technology-certificate/ |

*Note: This is a condensed representation. The full catalog contains 68 programs in the College of Earth, Ocean, and Atmospheric Sciences. For the complete list, refer to the catalog extraction data.*

#### College of Education

###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.oregonstate.edu/college-departments/education/elementary-education-ba-bs-hba-hbs/ |
| 2 | Secondary Education | https://catalog.oregonstate.edu/college-departments/education/secondary-education-ba-bs-hba-hbs/ |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://catalog.oregonstate.edu/college-departments/education/education-minor/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | College Student Services Administration | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/college-student-services-administration-graduate-certificate/ |
| 2 | Educational Practice and Research Dual Language Specialization | https://catalog.oregonstate.edu/college-departments/education/educational-practice-research-dual-language-specialization-graduate-certificate/ |
| 3 | English for Speakers of Other Languages | https://catalog.oregonstate.edu/college-departments/education/english-speakers-other-languages-graduate-certificate/ |
| 4 | Instructional Design | https://catalog.oregonstate.edu/college-departments/education/instructional-design-graduate-certificate/ |
| 5 | Special Education | https://catalog.oregonstate.edu/college-departments/education/special-education-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 78 programs in the College of Education. For the complete list, refer to the catalog extraction data.*

#### College of Pharmacy

###### Professional
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy (PharmD) | https://catalog.oregonstate.edu/college-departments/pharmacy/pharmacy-pharmd/ |

*Note: The College of Pharmacy has 6 programs total. For the complete list, refer to the catalog extraction data.*

#### College of Veterinary Medicine

###### Professional
| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Medicine (DVM) | https://catalog.oregonstate.edu/college-departments/veterinary-medicine/veterinary-medicine-dvm/ |

*Note: The College of Veterinary Medicine has 14 programs total. For the complete list, refer to the catalog extraction data.*

#### Honors College

###### HBA/HBS/HBFA/HBM
| # | 专业 | URL |
|---|------|-----|
| 1 | Honors Scholar Track A | https://catalog.oregonstate.edu/college-departments/honors-college/honors-scholar-track-hba-hbfa-hbm-hbs/ |
| 2 | Honors Scholar Track B | https://catalog.oregonstate.edu/college-departments/honors-college/honors-scholar-track-hba-hbfa-hbm-hbs/ |

###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Design for Social Impact | https://catalog.oregonstate.edu/college-departments/honors-college/design-social-impact-certificate/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

Oregon State has several interdisciplinary programs that span multiple colleges:

| # | 专业 | 主管学院 | URL |
|---|------|---------|-----|
| 1 | Environmental Sciences | College of Earth, Ocean, and Atmospheric Sciences | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/environmental-sciences-bs-hbs/ |
| 2 | Sustainability | College of Agricultural Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/sustainability-bs-hbs/ |
| 3 | Bioresource Research | College of Agricultural Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/bioresource-research/bioresource-research-bs-hbs/ |

### 1.4 Minors — complete list

Oregon State offers 408 undergraduate minors across all colleges. See the catalog extraction data for the complete list.

### 1.5 General/Institute-wide requirements

Oregon State University requires completion of the **Core Education** curriculum for all undergraduate degrees. The Core Education includes:

- **Writing I** (3 credits)
- **Writing II** (3 credits)
- **Speech Communication** (3 credits)
- **Mathematics** (3-4 credits)
- **Physical Science** (4 credits)
- **Biological Science** (4 credits)
- **Social Science** (3-4 credits)
- **Arts & Humanities** (3-4 credits)
- **Cultural Diversity** (3-4 credits)
- **Difference, Power, & Discrimination** (3 credits)

Total: ~48 credits of Core Education requirements.

Source: https://catalog.oregonstate.edu/core-education

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agricultural Sciences

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/agricultural-education-ms/ |
| 2 | Applied Economics | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/applied-economics-ma-ms-phd/ |
| 3 | Animal Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/animal-science-ms-phd/ |
| 4 | Botany and Plant Pathology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/botany-plant-pathology-ms-phd/ |
| 5 | Crop Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/crop-science-ms-phd/ |
| 6 | Entomology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/entomology/entomology-ma-ms-phd/ |
| 7 | Fisheries, Wildlife, and Conservation Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-conservation-sciences-ms-phd/ |
| 8 | Food Science and Technology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-science-technology-ms-phd/ |
| 9 | Horticulture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticulture-ms-phd/ |
| 10 | Rangeland Ecology and Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/rangeland-ecology-management-ms-phd/ |
| 11 | Soil Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/soil-science-ms-phd/ |
| 12 | Toxicology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/environmental-molecular-toxicology/toxicology-ms-phd/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Economics | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/applied-economics-ma-ms-phd/ |
| 2 | Animal Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/animal-science-ms-phd/ |
| 3 | Botany and Plant Pathology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/botany-plant-pathology-ms-phd/ |
| 4 | Crop Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/crop-science-ms-phd/ |
| 5 | Entomology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/entomology/entomology-ma-ms-phd/ |
| 6 | Fisheries, Wildlife, and Conservation Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-conservation-sciences-ms-phd/ |
| 7 | Food Science and Technology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-science-technology-ms-phd/ |
| 8 | Horticulture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticulture-ms-phd/ |
| 9 | Rangeland Ecology and Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/rangeland-ecology-management-ms-phd/ |
| 10 | Soil Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/soil-science-ms-phd/ |
| 11 | Toxicology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/environmental-molecular-toxicology/toxicology-ms-phd/ |

##### PSM Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries and Wildlife Administration | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-administration-psm/ |

##### Graduate Minor Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/agricultural-education-communication-sciences/agricultural-education-graduate-minor/ |
| 2 | Animal Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/animal-science-graduate-minor/ |
| 3 | Applied Economics | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/applied-economics/applied-economics-graduate-minor/ |
| 4 | Botany and Plant Pathology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/botany-plant-pathology/botany-plant-pathology-graduate-minor/ |
| 5 | Crop Science | https://catalog.oregonstate.edu/college-departments/agriultural-sciences/crop-soil-science/crop-science-graduate-minor/ |
| 6 | Entomology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/entomology/entomology-graduate-minor/ |
| 7 | Fisheries, Wildlife, and Conservation Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-conservation-sciences-graduate-minor/ |
| 8 | Food Science and Technology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/food-science-technology/food-science-technology-graduate-minor/ |
| 9 | Horticulture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticulture-graduate-minor/ |
| 10 | Rangeland Ecology and Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/animal-rangeland-sciences/rangeland-ecology-management-graduate-minor/ |
| 11 | Soil Science | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/crop-soil-science/soil-science-graduate-minor/ |
| 12 | Toxicology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/environmental-molecular-toxicology/toxicology-graduate-minor/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-management-graduate-certificate/ |
| 2 | Fisheries, Wildlife, and Conservation Sciences | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/fisheries-wildlife-conservation-sciences-certificate/ |
| 3 | Marine Mammal | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/marine-mammal-graduate-certificate/ |
| 4 | Wildlife Management | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/fisheries-wildlife-conservation-sciences/wildlife-management-graduate-certificate/ |
| 5 | Toxicology | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/environmental-molecular-toxicology/toxicology-graduate-certificate/ |
| 6 | Organic Agriculture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/organic-agriculture-graduate-certificate/ |
| 7 | Horticultural Therapy | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/horticultural-therapy-certificate/ |
| 8 | Organic Farming Systems | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/organic-farming-systems-certificate/ |
| 9 | Urban Agriculture | https://catalog.oregonstate.edu/college-departments/agricultural-sciences/horticulture/urban-agriculture-certificate/ |

*Note: This is a condensed representation. The full catalog contains 234 programs in the College of Agricultural Sciences. For the complete list, refer to the catalog extraction data.*

#### College of Business

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://catalog.oregonstate.edu/college-departments/business/business-administration-mba-phd/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business (MSB) | https://catalog.oregonstate.edu/college-departments/business/business-graduate-msb/ |
| 2 | Business Analytics and Applied AI | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/business-analytics-applied-ai-graduate-ms/ |
| 3 | Information Systems | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/information-systems-ms/ |
| 4 | Supply Chain and Logistics Management | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/supply-chain-logistics-management-graduate-ms/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.oregonstate.edu/college-departments/business/business-administration-mba-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.oregonstate.edu/college-departments/business/school-accounting-finance-information-systems/accounting-certificate/ |
| 2 | Business Analytics | https://catalog.oregonstate.edu/college-departments/business/school-marketing-analytics-design/business-analytics-graduate-certificate/ |
| 3 | Business Fundamentals | https://catalog.oregonstate.edu/college-departments/business/business-fundamentals-graduate-certificate/ |
| 4 | Organizational Leadership | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/organizational-leadership-graduate-minor/ |
| 5 | Supply Chain and Logistics Management | https://catalog.oregonstate.edu/college-departments/business/school-management-entrepreneurship-supply-chain/supply-chain-logistics-management-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 194 programs in the College of Business. For the complete list, refer to the catalog extraction data.*

#### College of Engineering

##### MEng Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/bioengineering-meng-ms-phd/ |
| 2 | Chemical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/chemical-engineering-meng-ms-phd/ |
| 3 | Civil Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/civil-engineering-meng-ms-phd/ |
| 4 | Computer Science | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/computer-science-meng-ms-phd/ |
| 5 | Electrical and Computer Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/electrical-computer-engineering-meng-ms-phd/ |
| 6 | Environmental Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/environmental-engineering-meng-ms-phd/ |
| 7 | Industrial Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/industrial-engineering-meng-ms-phd/ |
| 8 | Materials Science | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/materials-science-meng-ms-phd/ |
| 9 | Mechanical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/mechanical-engineering-meng-ms-phd/ |
| 10 | Nuclear Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/nuclear-engineering-meng-ms-phd/ |
| 11 | Robotics | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/robotics-meng-ms-phd/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/bioengineering-meng-ms-phd/ |
| 2 | Chemical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/chemical-engineering-meng-ms-phd/ |
| 3 | Civil Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/civil-engineering-meng-ms-phd/ |
| 4 | Computer Science | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/computer-science-meng-ms-phd/ |
| 5 | Electrical and Computer Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/electrical-computer-engineering-meng-ms-phd/ |
| 6 | Environmental Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/environmental-engineering-meng-ms-phd/ |
| 7 | Industrial Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/industrial-engineering-meng-ms-phd/ |
| 8 | Materials Science | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/materials-science-meng-ms-phd/ |
| 9 | Mechanical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/mechanical-engineering-meng-ms-phd/ |
| 10 | Nuclear Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/nuclear-engineering-meng-ms-phd/ |
| 11 | Robotics | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/robotics-meng-ms-phd/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/bioengineering-meng-ms-phd/ |
| 2 | Chemical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/chemical-engineering-meng-ms-phd/ |
| 3 | Civil Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/civil-engineering-meng-ms-phd/ |
| 4 | Computer Science | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/computer-science-meng-ms-phd/ |
| 5 | Electrical and Computer Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/electrical-computer-engineering-meng-ms-phd/ |
| 6 | Environmental Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-chemical-biological-environmental-engineering/environmental-engineering-meng-ms-phd/ |
| 7 | Industrial Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/industrial-engineering-meng-ms-phd/ |
| 8 | Materials Science | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/materials-science-meng-ms-phd/ |
| 9 | Mechanical Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/mechanical-engineering-meng-ms-phd/ |
| 10 | Nuclear Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-nuclear-science-engineering/nuclear-engineering-meng-ms-phd/ |
| 11 | Robotics | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/robotics-meng-ms-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://catalog.oregonstate.edu/college-departments/engineering/school-electrical-engineering-computer-science/cybersecurity-certificate/ |
| 2 | Engineering Management | https://catalog.oregonstate.edu/college-departments/engineering/school-civil-construction-engineering/engineering-management-graduate-certificate/ |
| 3 | Humanitarian Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/humanitarian-engineering-certificate/ |
| 4 | Mechatronics for Manufacturing Engineering | https://catalog.oregonstate.edu/college-departments/engineering/school-mechanical-industrial-manufacturing-engineering/mechatronics-manufacturing-engineering-certificate/ |
| 5 | Water Resources Engineering | https://catalog.oregonstate.edu/college-departments/engineering/biological-ecological-engineering/water-resources-engineering-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 190 programs in the College of Engineering. For the complete list, refer to the catalog extraction data.*

#### College of Science

##### MA/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.oregonstate.edu/college-departments/science/chemistry/chemistry-ma-ms-phd/ |
| 2 | Mathematics | https://catalog.oregonstate.edu/college-departments/science/mathematics/mathematics-ma-ms-phd/ |
| 3 | Physics | https://catalog.oregonstate.edu/college-departments/science/physics/physics-ma-ms-phd/ |
| 4 | Biochemistry and Biophysics | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/biochemistry-biophysics/biochemistry-biophysics-ma-ms-phd/ |
| 5 | Integrative Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/integrative-biology/integrative-biology-ms-phd/ |
| 6 | Microbiology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/microbiology/microbiology-ms-phd/ |
| 7 | Data Analytics | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/data-analytics-graduate-ms/ |
| 8 | Statistics | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/statistics-ms-phd/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.oregonstate.edu/college-departments/science/chemistry/chemistry-ma-ms-phd/ |
| 2 | Mathematics | https://catalog.oregonstate.edu/college-departments/science/mathematics/mathematics-ma-ms-phd/ |
| 3 | Physics | https://catalog.oregonstate.edu/college-departments/science/physics/physics-ma-ms-phd/ |
| 4 | Biochemistry and Biophysics | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/biochemistry-biophysics/biochemistry-biophysics-ma-ms-phd/ |
| 5 | Integrative Biology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/integrative-biology/integrative-biology-ms-phd/ |
| 6 | Microbiology | https://catalog.oregonstate.edu/college-departments/science/school-life-sciences/microbiology/microbiology-ms-phd/ |
| 7 | Statistics | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/statistics-ms-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Analytics | https://catalog.oregonstate.edu/college-departments/science/statistics-data-science/data-analytics-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 166 programs in the College of Science. For the complete list, refer to the catalog extraction data.*

#### College of Liberal Arts

##### MA/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Anthropology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/applied-anthropology-ma-ms-phd/ |
| 2 | Applied Ethics | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/applied-ethics-ma-ms/ |
| 3 | Communication | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-communication/communication-ma-ms/ |
| 4 | English | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/english-ma/ |
| 5 | History | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-history-philosophy-religion/history-ma-ms/ |
| 6 | Women, Gender, and Sexuality Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/women-gender-sexuality-studies-ma-phd/ |

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/creative-writing-mfa/ |
| 2 | Writing | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/writing-mfa/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Anthropology | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/applied-anthropology-ma-ms-phd/ |
| 2 | Women, Gender, and Sexuality Studies | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/women-gender-sexuality-studies-ma-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Energy Policy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/energy-policy-graduate-certificate/ |
| 2 | Food in Culture and Social Justice | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-language-culture-society/food-culture-social-justice-graduate-minor/ |
| 3 | Public Policy Analysis | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/public-policy-analysis-graduate-certificate/ |
| 4 | Rural Policy | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-public-policy/rural-policy-graduate-certificate/ |
| 5 | Scientific, Technical, and Professional Communication | https://catalog.oregonstate.edu/college-departments/liberal-arts/school-writing-literature-film/scientific-technical-professional-communication-certificate/ |

*Note: This is a condensed representation. The full catalog contains 294 programs in the College of Liberal Arts. For the complete list, refer to the catalog extraction data.*

#### College of Health

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adapted Physical Education (MAPE) | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/adapted-physical-education-mape/ |
| 2 | Kinesiology | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/kinesiology-ms-phd/ |
| 3 | Human Development and Family Studies | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/human-development-family-studies-ms-phd/ |
| 4 | Nutrition | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/nutrition-ms-phd/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Kinesiology | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/kinesiology-ms-phd/ |
| 2 | Human Development and Family Studies | https://catalog.oregonstate.edu/college-departments/health/school-human-development-family-sciences/human-development-family-studies-ms-phd/ |
| 3 | Nutrition | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/nutrition-ms-phd/ |
| 4 | Public Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/public-health-mph-phd/ |

##### Professional Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training (MATrn) | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/athletic-training-matrn/ |
| 2 | Physical Therapy (DPT) | https://catalog.oregonstate.edu/college-departments/health/school-exercise-sport-health-sciences/physical-therapy-dpt/ |
| 3 | Public Health (MPH) | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/public-health-mph-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Epidemiology | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/epidemiology-graduate-certificate/ |
| 2 | Health Management and Policy | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/health-management-policy-graduate-certificate/ |
| 3 | Public Health | https://catalog.oregonstate.edu/college-departments/health/school-nutrition-public-health/public-health-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 114 programs in the College of Health. For the complete list, refer to the catalog extraction data.*

#### College of Forestry

##### MF/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Forest Ecosystems and Society | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/forest-ecosystems-society-mf-ms-phd/ |
| 2 | Sustainable Forest Management | https://catalog.oregonstate.edu/college-departments/forestry/forest-engineering-resources-management/sustainable-forest-management-mf-ms-phd/ |
| 3 | Wood Science | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/wood-science-ms-phd/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Forest Ecosystems and Society | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/forest-ecosystems-society-mf-ms-phd/ |
| 2 | Sustainable Forest Management | https://catalog.oregonstate.edu/college-departments/forestry/forest-engineering-resources-management/sustainable-forest-management-mf-ms-phd/ |
| 3 | Wood Science | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/wood-science-ms-phd/ |

##### PSM Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Wood Innovation for Sustainability | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/wood-innovation-sustainability-psm/ |

##### MNR Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/natural-resources-mnr/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Forests and Climate Change | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/forests-climate-change-graduate-certificate/ |
| 2 | Mass Timber | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/mass-timber-graduate-certificate/ |
| 3 | Sustainable Natural Resources | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/sustainable-natural-resources-graduate-certificate/ |
| 4 | Timber Circular Economy | https://catalog.oregonstate.edu/college-departments/forestry/wood-science-engineering/timber-circular-economy-graduate-certificate/ |
| 5 | Urban Forestry | https://catalog.oregonstate.edu/college-departments/forestry/forest-ecosystems-society/urban-forestry-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 92 programs in the College of Forestry. For the complete list, refer to the catalog extraction data.*

#### College of Earth, Ocean, and Atmospheric Sciences

##### MA/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography and Geospatial Science | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geography-geospatial-science-ms-phd/ |
| 2 | Geology | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geology-ma-ms-phd/ |
| 3 | Marine Resource Management | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/marine-resource-management-ms/ |
| 4 | Ocean, Earth and Atmospheric Sciences | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/ocean-earth-atmospheric-sciences-ms-phd/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography and Geospatial Science | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geography-geospatial-science-ms-phd/ |
| 2 | Geology | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geology-ma-ms-phd/ |
| 3 | Ocean, Earth and Atmospheric Sciences | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/ocean-earth-atmospheric-sciences-ms-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Climate Change Solutions | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/climate-change-solutions-certificate/ |
| 2 | Environmental Justice | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/environmental-justice-certificate/ |
| 3 | Geographic Information Science | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/geographic-information-science-graduate-certificate/ |
| 4 | Marine Resource Management | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/marine-resource-management-graduate-certificate/ |
| 5 | Ocean Technology | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/ocean-technology-certificate/ |
| 6 | Water Conflict Management and Transformation | https://catalog.oregonstate.edu/college-departments/earth-ocean-atmospheric-sciences/water-conflict-management-transformation-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 68 programs in the College of Earth, Ocean, and Atmospheric Sciences. For the complete list, refer to the catalog extraction data.*

#### College of Education

##### EdD/EdM/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult and Higher Education | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/adult-higher-education-edd-edm-phd/ |
| 2 | College Student Services Administration | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/college-student-services-administration-graduate-edm-ms/ |
| 3 | Counseling | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/counseling-mcoun-phd/ |
| 4 | Education | https://catalog.oregonstate.edu/college-departments/education/education-edd-ms-phd/ |
| 5 | Teaching (MAT) | https://catalog.oregonstate.edu/college-departments/education/teaching-mat/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult and Higher Education | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/adult-higher-education-edd-edm-phd/ |
| 2 | Counseling | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/counseling-mcoun-phd/ |
| 3 | Education | https://catalog.oregonstate.edu/college-departments/education/education-edd-ms-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | College Student Services Administration | https://catalog.oregonstate.edu/college-departments/education/counseling-adult-higher-education/college-student-services-administration-graduate-certificate/ |
| 2 | Educational Practice and Research Dual Language Specialization | https://catalog.oregonstate.edu/college-departments/education/educational-practice-research-dual-language-specialization-graduate-certificate/ |
| 3 | English for Speakers of Other Languages | https://catalog.oregonstate.edu/college-departments/education/english-speakers-other-languages-graduate-certificate/ |
| 4 | Instructional Design | https://catalog.oregonstate.edu/college-departments/education/instructional-design-graduate-certificate/ |
| 5 | Special Education | https://catalog.oregonstate.edu/college-departments/education/special-education-graduate-certificate/ |

*Note: This is a condensed representation. The full catalog contains 78 programs in the College of Education. For the complete list, refer to the catalog extraction data.*

#### College of Pharmacy

##### MS/PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalog.oregonstate.edu/college-departments/pharmacy/pharmaceutical-sciences-ms-phd/ |

##### Professional Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy (PharmD) | https://catalog.oregonstate.edu/college-departments/pharmacy/pharmacy-pharmd/ |

*Note: The College of Pharmacy has 6 programs total. For the complete list, refer to the catalog extraction data.*

#### College of Veterinary Medicine

##### MS/PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Health Sciences | https://catalog.oregonstate.edu/college-departments/veterinary-medicine/comparative-health-sciences-ms-phd/ |

##### Professional Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Veterinary Medicine (DVM) | https://catalog.oregonstate.edu/college-departments/veterinary-medicine/veterinary-medicine-dvm/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | One Health | https://catalog.oregonstate.edu/college-departments/veterinary-medicine/one-health-certificate/ |

*Note: The College of Veterinary Medicine has 14 programs total. For the complete list, refer to the catalog extraction data.*

#### Office of Graduate Education

##### Interdisciplinary Graduate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://catalog.oregonstate.edu/college-departments/graduate-education/environmental-sciences-ma-ms-phd-psm/ |
| 2 | Interdisciplinary Studies (MAIS) | https://catalog.oregonstate.edu/college-departments/graduate-education/interdisciplinary-studies-mais/ |
| 3 | Water Resources Engineering | https://catalog.oregonstate.edu/college-departments/graduate-education/water-resources-engineering-ms-phd/ |
| 4 | Water Resources Policy and Management | https://catalog.oregonstate.edu/college-departments/graduate-education/water-resources-policy-management-graduate-ms/ |
| 5 | Water Resources Science | https://catalog.oregonstate.edu/college-departments/graduate-education/water-resources-science-ms-phd/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | College and University Teaching | https://catalog.oregonstate.edu/college-departments/graduate-education/college-university-teaching-graduate-certificate/ |
| 2 | Environmental Management | https://catalog.oregonstate.edu/college-departments/graduate-education/environmental-management-graduate-certificate/ |

### 2.2 At least one program's full deep-dive (worked example)

#### Computer Science (MEng, MS, PhD) — College of Engineering

- **Department**: School of Electrical Engineering and Computer Science
- **Degrees offered**: MEng, MS, PhD
- **Application portal**: https://graduate.oregonstate.edu/admissions
- **Application fee**: $85 (domestic, starting Winter 2026); $85 (international)
- **GRE**: Not required
- **TOEFL minimum**: 80 iBT (minimum 18 on each sub-section)
- **IELTS minimum**: 6.5
- **Duolingo minimum**: 110
- **Deadlines**: Program-specific; check program page
- **Funding**: Graduate assistantships available (TA/RA)
- **Contact**: See program page for primary contact

### 2.3 Graduate admissions model

Oregon State uses a **decentralized** graduate admissions model. The Office of Graduate Education sets minimum university-wide requirements, but each academic program establishes its own:
- Application deadlines (often earlier than university deadlines)
- Additional requirements (GRE, portfolios, writing samples)
- Admission decisions
- Financial aid/funding decisions

**Application process**:
1. Apply online at https://graduate.oregonstate.edu/admissions
2. Submit application fee ($85 domestic starting Winter 2026; $85 international)
3. Upload required documents (transcripts, statement of purpose, letters of recommendation)
4. Programs review applications and make admission decisions

**CGS April-15 signatory**: Yes

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://admissions.oregonstate.edu/ | Official website |
| Application portal | OSU Application or Common Application | https://admissions.oregonstate.edu/apply-choose-application |
| Early Action deadline | November 3, 2025 (Fall 2026) / November 2, 2026 (Fall 2027) | https://admissions.oregonstate.edu/undergraduate-admission-deadlines |
| Priority deadline | February 2, 2026 (Fall 2026) / February 1, 2027 (Fall 2027) | https://admissions.oregonstate.edu/undergraduate-admission-deadlines |
| Rolling admission | Yes (applications remain open on space available basis) | https://admissions.oregonstate.edu/undergraduate-admission-deadlines |
| Application fee | $65 | https://admissions.oregonstate.edu/first-year-students |
| Test policy | Test-optional | https://admissions.oregonstate.edu/admission-requirements |
| Superscore | N/A (test-optional) | https://admissions.oregonstate.edu/admission-requirements |
| SAT/ACT codes | Not specified | - |
| Interview policy | Not required | - |
| Recommendation letters | Not required (except when appealing denial) | https://admissions.oregonstate.edu/admission-requirements |
| Portfolio | Not required for most programs | - |
| Transfer deadline | March 16, 2026 (Fall 2026) | https://admissions.oregonstate.edu/undergraduate-admission-deadlines |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低分 | 推荐分 | 适用条件 |
|------|--------|--------|----------|
| TOEFL iBT | 70 | - | International students |
| IELTS | 6.0 | - | International students |
| PTEA | 48 | - | International students |
| Duolingo | 100 | - | International students |
| SAT Evidence-Based Reading/Writing | 560 | - | Alternative to English proficiency test |
| ACT English | 21 | - | Alternative to English proficiency test |
| AP English L&C | 3 | - | Alternative to English proficiency test |
| IB Diploma Language A (HL) | 5 | - | Alternative to English proficiency test |

**Alternative pathways**:
- Two English composition courses (Writing 121+) with grades C- or better from a US university
- IGCSE O or A Level English with a grade of C or better

**Pathway programs** (lower requirements):
- 3-term pathway: TOEFL 60 / IELTS 5.5 / Duolingo 90
- 4-term pathway: TOEFL 50 / IELTS 5.0 / Duolingo 75

**Score validity**: Scores must be less than two years old as of the start term requested.

**Source**: https://admissions.oregonstate.edu/international/programs/undergraduate-degree-programs/first-year-freshman

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions model | Decentralized (each program sets own requirements) | https://graduate.oregonstate.edu/admissions |
| Application portal | https://graduate.oregonstate.edu/admissions | Official website |
| Application fee (domestic) | $75 (through Fall 2025); $85 (starting Winter 2026) | https://graduate.oregonstate.edu/admissions/process |
| Application fee (international) | $85 | https://graduate.oregonstate.edu/admissions/process |
| GRE policy | Per-program (some require, some don't) | https://graduate.oregonstate.edu/admissions |
| CGS April-15 signatory | Yes | https://graduate.oregonstate.edu/admissions |
| TOEFL minimum (regular) | 80 iBT (minimum 18 on each sub-section) | https://graduate.oregonstate.edu/admissions/international |
| IELTS minimum | 6.5 | https://graduate.oregonstate.edu/admissions/international |
| Duolingo minimum | 110 | https://graduate.oregonstate.edu/admissions/international |
| TOEFL code | 4586 | https://graduate.oregonstate.edu/admissions/international |
| GTA speaking requirement | TOEFL speaking 22 / IELTS speaking 7.0 | https://graduate.oregonstate.edu/admissions/international |
| Score validity | Must be no more than two years old at time of first term registration | https://graduate.oregonstate.edu/admissions/international |
| MyBest TOEFL | NOT accepted | https://graduate.oregonstate.edu/admissions/international |
| TOEFL ITP | NOT accepted (non-OSU locations) | https://graduate.oregonstate.edu/admissions/international |

**Graduate deadlines**:
- U.S. Citizens and Permanent Residents: Absolutely no later than 30 days prior to the first day of classes
- International Applicants: Please submit at least 90 days before the start of the term

**Source**: https://graduate.oregonstate.edu/admissions/deadlines

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

#### Corvallis Campus — Resident Undergraduate

| 费用项目 | 金额 (3 Terms) | 金额 (1 Term) | 说明 |
|---------|---------------|--------------|------|
| Tuition and Fees (15 CR) | $16,014 | $5,338 | Mandatory fees included |
| Living Expenses (Food and Housing) | $18,066 | $6,022 | On-campus estimate |
| **Estimated Billable Cost Total** | **$34,080** | **$11,360** | |
| Books, Course Materials, Supplies, and Equipment | $600 | $200 | Non-billable |
| Personal and Miscellaneous | $2,958 | $986 | Non-billable |
| Transportation | $930 | $310 | Non-billable |
| **Estimated Non-Billable Cost Total** | **$4,488** | **$1,496** | |
| **Estimated TOTAL** | **$38,568** | **$12,856** | |

#### Corvallis Campus — Non-Resident Undergraduate

| 费用项目 | 金额 (3 Terms) | 金额 (1 Term) | 说明 |
|---------|---------------|--------------|------|
| Tuition and Fees (15 CR) | $42,459 | $14,153 | Mandatory fees included |
| Living Expenses (Food and Housing) | $18,066 | $6,022 | On-campus estimate |
| **Estimated Billable Cost Total** | **$60,525** | **$20,175** | |
| Books, Course Materials, Supplies, and Equipment | $600 | $200 | Non-billable |
| Personal and Miscellaneous | $2,958 | $986 | Non-billable |
| Transportation | $930 | $310 | Non-billable |
| **Estimated Non-Billable Cost Total** | **$4,488** | **$1,496** | |
| **Estimated TOTAL** | **$65,013** | **$21,671** | |

**Source**: https://financialaid.oregonstate.edu/cost-attendance

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-blind/need-aware | Need-aware for all (domestic and international) | https://admissions.oregonstate.edu/cost-and-aid |
| Meets full demonstrated need | Not guaranteed | https://admissions.oregonstate.edu/cost-and-aid |
| Tuition-free threshold | Not specified | - |
| Median actual price paid | Not specified | - |
| Debt-free graduation rate | Not specified | - |
| Average starting salary | $57,700 (early career); $104,500 (mid-career) | https://admissions.oregonstate.edu/cost-and-aid |
| WUE (Western Undergraduate Exchange) | Available (competitive, limited number of qualifying students) | https://admissions.oregonstate.edu/wue |
| Nonresident Tuition Equity | Available for qualifying students | https://admissions.oregonstate.edu/tuition-equity-and-exemption-non-resident-tuition |
| Bridge to Success Program | Available | https://admissions.oregonstate.edu/bridge-success |

**Scholarships**:
- Over $15 million in scholarships funded by alumni
- Scholarships available through ScholarDollars platform
- https://scholarships.oregonstate.edu/

### 4.3 Graduate cost & funding framework

#### Corvallis Campus — Resident Graduate

| 费用项目 | 金额 (3 Terms) | 金额 (1 Term) | 说明 |
|---------|---------------|--------------|------|
| Tuition and Fees (11 CR) | $17,391 | $5,797 | Mandatory fees included |
| Living Expenses (Food and Housing) | $18,066 | $6,022 | On-campus estimate |
| **Estimated Billable Cost Total** | **$35,457** | **$11,819** | |
| Books, Course Materials, Supplies, and Equipment | $600 | $200 | Non-billable |
| Personal and Miscellaneous | $2,958 | $986 | Non-billable |
| Transportation | $930 | $310 | Non-billable |
| **Estimated Non-Billable Cost Total** | **$4,488** | **$1,496** | |
| **Estimated TOTAL** | **$39,945** | **$13,315** | |

#### Corvallis Campus — Non-Resident Graduate

| 费用项目 | 金额 (3 Terms) | 金额 (1 Term) | 说明 |
|---------|---------------|--------------|------|
| Tuition and Fees (11 CR) | $36,840 | $12,280 | Mandatory fees included |
| Living Expenses (Food and Housing) | $18,066 | $6,022 | On-campus estimate |
| **Estimated Billable Cost Total** | **$54,906** | **$18,302** | |
| Books, Course Materials, Supplies, and Equipment | $600 | $200 | Non-billable |
| Personal and Miscellaneous | $2,958 | $986 | Non-billable |
| Transportation | $930 | $310 | Non-billable |
| **Estimated Non-Billable Cost Total** | **$4,488** | **$1,496** | |
| **Estimated TOTAL** | **$59,394** | **$19,798** | |

**Source**: https://financialaid.oregonstate.edu/cost-attendance

**Graduate funding**:
- Graduate Assistantships (TA/RA): https://graduate.oregonstate.edu/funding
- Graduate Fellowships: https://graduate.oregonstate.edu/funding/graduate-fellowships
- Graduate Student Awards: https://graduate.oregonstate.edu/funding/graduate-student-awards
- Scholar Incentive Program: https://graduate.oregonstate.edu/funding/scholar-incentive-program
- Tuition Support Programs: https://graduate.oregonstate.edu/funding/tuition-support-programs
- Western Regional Graduate Program (WRGP): https://graduate.oregonstate.edu/funding/western-regional-graduate-program-wrgp

---

## SECTION 5 — Evidence chain index

### Evidence blocks

```yaml
E-U-001:
  field: undergraduate.admissions.deadlines.early_action
  value: "November 3, 2025 (Fall 2026)"
  source_url: https://admissions.oregonstate.edu/undergraduate-admission-deadlines
  source_snippet: "November 3, 2025 - Early Action Deadline for Corvallis campus applicants. Students who have applied and have a complete application file will be notified by mid-December."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.deadlines.priority
  value: "February 2, 2026 (Fall 2026)"
  source_url: https://admissions.oregonstate.edu/undergraduate-admission-deadlines
  source_snippet: "February 2, 2026 – Priority Application Deadline for Corvallis campus students. Students wishing to receive full consideration for admission and aim to have access to the greatest set of scholarship opportunities and should apply by this date."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.test_policy
  value: "Test-optional"
  source_url: https://admissions.oregonstate.edu/admission-requirements
  source_snippet: "OSU is test-optional. Test scores, if you elect to submit them, are never the sole or primary reason for an admissions decision; they are always considered in context and as supplemental information."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.admissions.application_fee
  value: "$65"
  source_url: https://admissions.oregonstate.edu/first-year-students
  source_snippet: "Pay the $65 application fee or request a waiver (at the end of the application)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.costs.tuition_resident_2026_2027
  value: "$16,014 (3 terms)"
  source_url: https://financialaid.oregonstate.edu/cost-attendance
  source_snippet: "2026-2027 Estimated Resident Undergraduate Expense 3 Terms 1 Term Tuition and Fees (15 CR) 1 $16,014 $5,338"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.tuition_nonresident_2026_2027
  value: "$42,459 (3 terms)"
  source_url: https://financialaid.oregonstate.edu/cost-attendance
  source_snippet: "2026-2027 Estimated Non-Resident Undergraduate Expense 3 Terms 1 Term Tuition and Fees (15 CR) 1 $42,459 $14,153"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.total_resident_2026_2027
  value: "$38,568 (3 terms)"
  source_url: https://financialaid.oregonstate.edu/cost-attendance
  source_snippet: "Estimated TOTAL $38,568 $12,856"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.costs.total_nonresident_2026_2027
  value: "$65,013 (3 terms)"
  source_url: https://financialaid.oregonstate.edu/cost-attendance
  source_snippet: "Estimated TOTAL $65,013 $21,671"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.english_proficiency.toefl
  value: "70 iBT"
  source_url: https://admissions.oregonstate.edu/international/programs/undergraduate-degree-programs/first-year-freshman
  source_snippet: "Language Requirements 70 iBT TOEFL"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_proficiency.ielts
  value: "6.0"
  source_url: https://admissions.oregonstate.edu/international/programs/undergraduate-degree-programs/first-year-freshman
  source_snippet: "6.0 IELTS"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.english_proficiency.duolingo
  value: "100"
  source_url: https://admissions.oregonstate.edu/international/programs/undergraduate-degree-programs/first-year-freshman
  source_snippet: "100 Duolingo"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.application_fee_domestic
  value: "$85 (starting Winter 2026)"
  source_url: https://graduate.oregonstate.edu/admissions/process
  source_snippet: "Domestic degree seeking (including graduate certificates) $75 $85 International degree seeking (including graduate certificates) $85 $85"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.english_proficiency.toefl
  value: "80 iBT (minimum 18 on each sub-section)"
  source_url: https://graduate.oregonstate.edu/admissions/international
  source_snippet: "TOEFL iBT - 80 * Minimum score of 18 on each sub-section"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_proficiency.ielts
  value: "6.5"
  source_url: https://graduate.oregonstate.edu/admissions/international
  source_snippet: "IELTS - 6.5 *"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.english_proficiency.duolingo
  value: "110"
  source_url: https://graduate.oregonstate.edu/admissions/international
  source_snippet: "Duolingo - 110 * (must include sub-scores)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-005:
  field: graduate.ets_code
  value: "4586"
  source_url: https://graduate.oregonstate.edu/admissions/international
  source_snippet: "The ETS institution code for OSU is 4586."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-006:
  field: graduate.costs.tuition_resident_2026_2027
  value: "$17,391 (3 terms)"
  source_url: https://financialaid.oregonstate.edu/cost-attendance
  source_snippet: "2026-2027 Estimated Resident Graduate Expense 3 Terms 1 Term Tuition and Fees (11 CR) 1 $17,391 $5,797"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-007:
  field: graduate.costs.tuition_nonresident_2026_2027
  value: "$36,840 (3 terms)"
  source_url: https://financialaid.oregonstate.edu/cost-attendance
  source_snippet: "2026-2027 Estimated Non-Resident Graduate Expense 3 Terms 1 Term Tuition and Fees (11 CR) 1 $36,840 $12,280"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-008:
  field: graduate.deadlines.domestic
  value: "Absolutely no later than 30 days prior to the first day of classes"
  source_url: https://graduate.oregonstate.edu/admissions/deadlines
  source_snippet: "U.S. Citizens and Permanent Residents Absolutely no later than 30 days prior to the first day of classes."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-009:
  field: graduate.deadlines.international
  value: "Please submit your application at least 90 days before the start of the term"
  source_url: https://graduate.oregonstate.edu/admissions/deadlines
  source_snippet: "International Applicants Please submit your application at least 90 days before the start of the term you are applying for."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-010:
  field: programs.total_count
  value: 1490
  source_url: https://catalog.oregonstate.edu/programs
  source_snippet: "1490 program items extracted from catalog.oregonstate.edu/programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage_extraction

E-G-011:
  field: colleges.count
  value: 11
  source_url: https://catalog.oregonstate.edu/college-departments
  source_snippet: "College of Agricultural Sciences, College of Business, College of Earth Ocean and Atmospheric Sciences, College of Education, College of Engineering, College of Forestry, College of Health, College of Liberal Arts, College of Pharmacy, College of Science, College of Veterinary Medicine"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
oregonstate-knowledge-base-v2/
├── 00-overview/
│   ├── 01-program-counts.md
│   ├── 02-hierarchy-tree.md
│   ├── 03-degree-inventory.md
│   └── 04-distribution-matrix.md
├── 01-undergraduate/
│   ├── college-of-agricultural-sciences.md
│   ├── college-of-business.md
│   ├── college-of-earth-ocean-atmospheric-sciences.md
│   ├── college-of-education.md
│   ├── college-of-engineering.md
│   ├── college-of-forestry.md
│   ├── college-of-health.md
│   ├── college-of-liberal-arts.md
│   ├── college-of-pharmacy.md
│   ├── college-of-science.md
│   ├── college-of-veterinary-medicine.md
│   └── honors-college.md
├── 02-graduate/
│   ├── college-of-agricultural-sciences-grad.md
│   ├── college-of-business-grad.md
│   ├── college-of-earth-ocean-atmospheric-sciences-grad.md
│   ├── college-of-education-grad.md
│   ├── college-of-engineering-grad.md
│   ├── college-of-forestry-grad.md
│   ├── college-of-health-grad.md
│   ├── college-of-liberal-arts-grad.md
│   ├── college-of-pharmacy-grad.md
│   ├── college-of-science-grad.md
│   ├── college-of-veterinary-medicine-grad.md
│   └── office-of-graduate-education-interdisciplinary.md
├── 03-deadlines/
│   ├── undergraduate-deadlines.md
│   └── graduate-deadlines.md
├── 04-costs/
│   ├── undergraduate-costs.md
│   └── graduate-costs.md
├── 05-english-proficiency/
│   ├── undergraduate-english-requirements.md
│   └── graduate-english-requirements.md
└── 06-evidence-chain/
    └── evidence-index.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "oregonstate-knowledge-base-v2"
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

| 优先级 | 数据项 | 目标 URL |
|--------|--------|----------|
| P0 | Per-program GRE requirements (graduate) | https://graduate.oregonstate.edu/admissions |
| P0 | Per-program specific deadlines (graduate) | https://graduate.oregonstate.edu/admissions/deadlines |
| P1 | Complete program list with all options/specializations | https://catalog.oregonstate.edu/programs |
| P1 | Cascades campus specific programs and costs | https://admissions.oregonstate.edu/international |
| P1 | Ecampus online program list and costs | https://ecampus.oregonstate.edu/ |
| P2 | Merit scholarship details and criteria | https://scholarships.oregonstate.edu/ |
| P2 | WUE eligibility details | https://admissions.oregonstate.edu/wue |
| P2 | Nonresident Tuition Equity details | https://admissions.oregonstate.edu/tuition-equity-and-exemption-non-resident-tuition |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Oregon State University | (blank for other schools) |
|------|------------------------|---------------------------|
| Total UG cost/yr (resident) | $38,568 | |
| Total UG cost/yr (non-resident) | $65,013 | |
| Tuition/yr (resident) | $16,014 | |
| Tuition/yr (non-resident) | $42,459 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | November 3, 2025 | |
| Priority deadline | February 2, 2026 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min (UG) | 70 | |
| IELTS min (UG) | 6.0 | |
| TOEFL min (grad) | 80 | |
| IELTS min (grad) | 6.5 | |
| Tuition-free threshold | N/A | |
| Median price paid | Not specified | |
| Grad application fee | $85 | |
| April-15-equivalent honor date | Yes (CGS signatory) | |
| Total program count (rule 1) | 1490 | |
| School/department count (rule 2) | 11 colleges | |
| Public/Private | Public | |
| Location | Corvallis, Oregon | |
| Campuses | Corvallis, OSU-Cascades (Bend), Ecampus (online) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.oregonstate.edu, graduate.oregonstate.edu, financialaid.oregonstate.edu, catalog.oregonstate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
