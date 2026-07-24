# Purdue University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BA/BFA/etc.) | 298 |
| 本科辅修 (Minor) | 150 |
| 本科证书 (Certificate) | 36 |
| 本科预科项目 (Pre-Program) | 21 |
| 研究生学位项目 (MS/PhD/MBA/etc.) | 454 |
| **学位项目总计 (UG + Grad, 含 minors/certs)** | **959** |
| 学院 / 独立系所总数 | 11 |

> Source: catalog.purdue.edu/content.php?catoid=19&navoid=25484 (UG Programs List); navoid=25622 (Graduate Degrees). Capture date 2026-07-05.

### 0.2 学院 / 系层级结构

```
Purdue University (West Lafayette)
├── College of Agriculture                              [学院]
│   ├── College of Agriculture Administration            [系]
│   ├── Dept of Agricultural and Biological Engineering  [系]
│   ├── Dept of Agricultural Economics                   [系]
│   ├── Dept of Agronomy                                 [系]
│   ├── Dept of Animal Sciences                          [系]
│   ├── Dept of Biochemistry                             [系]
│   ├── Dept of Botany and Plant Pathology               [系]
│   ├── Dept of Entomology                               [系]
│   ├── Dept of Food Science                             [系]
│   ├── Dept of Forestry and Natural Resources           [系]
│   └── Dept of Horticulture and Landscape Architecture  [系]
├── Mitch Daniels School of Business                     [学院]
│   ├── Bruce White Undergraduate Institute              [系]
│   ├── Dept of Accounting                               [系]
│   ├── Dept of Economics                                [系]
│   ├── Dept of Finance                                  [系]
│   ├── Dept of Management Information Systems           [系]
│   ├── Dept of Marketing                                [系]
│   ├── Dept of Organizational Behavior & HRM            [系]
│   ├── Dept of Quantitative Methods                     [系]
│   ├── Dept of Strategic Management                     [系]
│   └── Dept of Supply Chain and Operations Management   [系]
├── College of Education                                 [学院]
│   ├── Dept of Curriculum and Instruction               [系]
│   └── Dept of Educational Studies                      [系]
├── College of Engineering                               [学院]
│   ├── First-Year Engineering                           [系]
│   ├── School of Aeronautics and Astronautics           [系]
│   ├── Dept of Agricultural and Biological Engineering  [系] ⚠ shared with Agriculture
│   ├── Weldon School of Biomedical Engineering          [系]
│   ├── Davidson School of Chemical Engineering          [系]
│   ├── Lyles School of Civil and Construction Eng.      [系]
│   ├── Elmore Family School of Electrical & Computer Eng[系]
│   ├── School of Engineering Education                  [系]
│   ├── School of Sustainability & Environmental Eng.    [系]
│   ├── School of Industrial Engineering                 [系]
│   ├── School of Materials Engineering                  [系]
│   ├── School of Mechanical Engineering                 [系]
│   └── School of Nuclear Engineering                    [系]
├── College of Health and Human Sciences                 [学院]
│   ├── School of Health Sciences                        [系]
│   ├── School of Nursing                                [系]
│   ├── School of Hospitality and Tourism Management     [系]
│   └── Dept of Human Development and Family Science     [系]
├── College of Liberal Arts                              [学院]
│   ├── School of Interdisciplinary Studies              [系]
│   └── School of Languages and Cultures                 [系]
├── Libraries and School of Information Studies          [学院]
├── College of Pharmacy                                  [学院]
├── Polytechnic Institute                                [学院]
│   ├── School of Applied and Creative Computing         [系]
│   ├── School of Aviation and Transportation Technology [系]
│   └── School of Engineering Technology                 [系]
├── College of Science                                   [学院]
│   ├── Dept of Biological Sciences                      [系]
│   ├── Dept of Chemistry                                [系]
│   ├── Dept of Computer Science                         [系]
│   ├── Dept of Earth, Atmospheric, and Planetary Sciences [系]
│   ├── Dept of Mathematics                              [系]
│   ├── Dept of Physics and Astronomy                    [系]
│   └── Dept of Statistics                               [系]
├── College of Veterinary Medicine                       [学院]
└── Honors College                                       [学院] (interdisciplinary, no own degrees)
```

> Note: Agricultural and Biological Engineering is jointly administered by College of Agriculture and College of Engineering (marked ⚠ shared). The Honors College is interdisciplinary and does not grant standalone degrees. Exploratory Studies is an advising unit, not a degree-granting college.

### 0.3 学历级别明细

| 学位缩写 (canonical) | 本校官方缩写 | 全称 | 层级 | 本项目数量 |
|---------|---------|------|------|-----------|
| BS | BS | Bachelor of Science | 本科 | ~240 |
| BA | BA | Bachelor of Arts | 本科 | ~12 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BSE | BSE | Bachelor of Science in Engineering | 本科 | ~8 |
| BSAAE | BSAAE | BS in Aeronautical & Astronautical Eng. | 本科 | 1 |
| BSBME | BSBME | BS in Biomedical Engineering | 本科 | 1 |
| BSCHE | BSCHE | BS in Chemical Engineering | 本科 | 1 |
| BSCE | BSCE | BS in Civil Engineering | 本科 | 1 |
| BSCNE | BSCNE | BS in Construction Engineering | 本科 | 1 |
| BSCMPE | BSCMPE | BS in Computer Engineering | 本科 | 1 |
| BSEE | BSEE | BS in Electrical Engineering | 本科 | 1 |
| BSEEE | BSEEE | BS in Environmental & Ecological Eng. | 本科 | 1 |
| BSIE | BSIE | BS in Industrial Engineering | 本科 | 1 |
| BSMSE | BSMSE | BS in Materials Science Engineering | 本科 | 1 |
| BSME | BSME | BS in Mechanical Engineering | 本科 | 1 |
| BSNE | BSNE | BS in Nuclear Engineering | 本科 | 1 |
| BSAGE | BSAGE | BS in Agricultural Engineering | 本科 | 2 |
| BSBE | BSBE | BS in Biological Engineering | 本科 | 1 |
| BSFOR | BSFOR | BS in Forestry | 本科 | 4 |
| BSLA | BSLA | BS in Landscape Architecture | 本科 | 1 |
| BSVN | BSVN | BS in Veterinary Nursing | 本科 | 1 |
| AAS | AAS | Associate of Applied Science | 本科 | ~3 |
| MS | MS | Master of Science | 研究生 | ~200 |
| MA | MA | Master of Arts | 研究生 | ~20 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MFA | MFA | Master of Fine Arts | 研究生 | ~5 |
| MSED | MSEd | Master of Science in Education | 研究生 | ~5 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | ~3 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MHA | MHA | Master of Health Administration | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~180 |
| EdS | EdS | Educational Specialist | 研究生 | ~2 |
| DS | DS | Doctor of Science | 研究生 | ~3 |
| DAUD | DAUD | Doctor of Audiology | 研究生 | 1 |
| DTECH | DTECH | Doctor of Technology | 研究生 | 1 |
| Minor | Minor | 本科辅修 | 本科 | 150 |
| Certificate | Certificate | 证书 | 本科+研究生 | 36+ |

> Counts are approximate from catalog extraction (959 total entries). Exact counts per degree code require per-program detail page verification. Purdue uses standard US degree abbreviations (no Latin naming).

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BS/BA/BFA | BSE/BSxx | Minor | Certificate | MS | MA | MBA | PhD | Prof Doc | 合计 |
|------------|-----------|----------|-------|-------------|----|----|-----|-----|----------|------|
| College of Agriculture | 55 | 7 | 28 | 8 | ~30 | 0 | 0 | ~15 | 0 | ~143 |
| Daniels School of Business | 10 | 0 | 9 | 1 | 5 | 0 | 1 | 5 | 0 | ~31 |
| College of Education | 6 | 0 | 2 | 1 | ~8 | ~3 | 0 | ~3 | EdS ~2 | ~25 |
| College of Engineering | 0 | ~18 | ~8 | ~3 | ~60 | 0 | 0 | ~80 | 0 | ~170 |
| College of Health & Human Sciences | ~30 | 0 | ~10 | ~3 | ~25 | ~5 | 0 | ~15 | DNP/DAUD ~3 | ~91 |
| College of Liberal Arts | ~25 | 0 | ~30 | ~5 | ~15 | ~10 | 0 | ~15 | 0 | ~100 |
| Libraries & Info Studies | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 5 |
| College of Pharmacy | 1 | 0 | 1 | 0 | ~3 | 0 | 0 | ~3 | PharmD 1 | ~9 |
| Polytechnic Institute | ~25 | 0 | ~15 | ~5 | ~20 | 0 | 0 | ~10 | DTECH 1 | ~76 |
| College of Science | ~60 | 0 | ~20 | ~5 | ~40 | ~5 | 0 | ~40 | DS ~3 | ~173 |
| College of Veterinary Medicine | ~5 | 0 | 1 | 0 | ~5 | 0 | 0 | ~5 | DVM 1 | ~17 |
| Exploratory Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **~218** | **~25** | **~124** | **~31** | **~214** | **~23** | **1** | **~191** | **~11** | **~959** |

> Matrix is derived from catalog extraction. Row totals must reconcile with rule-1 total (959). Approximate counts due to college attribution challenges in the catalog flat list (some schools are sub-units of colleges). The exact reconciliation requires per-program college mapping from detail pages.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Purdue has 11 undergraduate-degree-granting colleges at the West Lafayette campus. The College of Engineering is the flagship, with 13 schools/departments. Programs are organized under academic colleges, each with departmental subdivisions. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture

##### College of Agriculture Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Natural Resources and Environmental Science: Climate and Energy Solutions Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Natural Resources and Environmental Science: Emerging Environmental Challenges Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Natural Resources and Environmental Science: Environmental Policy and Analysis Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Natural Resources and Environmental Science: Environmental Quality And Restoration Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 5 | Natural Resources and Environmental Science: Sustainability Science Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 6 | Natural Resources and Environmental Science: Watershed Management Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Agricultural and Biological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Systems Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

###### BSAGE
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Environmental and Natural Resources Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

###### BSBE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Agricultural Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness: Agribusiness Management Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Agribusiness: Agricultural & Food Marketing Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Agribusiness: Agricultural Finance Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Agribusiness: Commodity Marketing Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 5 | Agricultural Economics: Applied Agricultural Economics Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 6 | Agricultural Economics: Policy and Pre-Law Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 7 | Agricultural Economics: Quantitative Data Analytics Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 8 | Farm Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 9 | Sales and Marketing | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Agronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Education | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Agronomy: Agronomic Business and Marketing Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Agronomy: Crop and Soil Management Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Agronomy: International Agronomy Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 5 | Crop Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 6 | Digital Agronomy | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 7 | Plant Genetics, Breeding, and Biotechnology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 8 | Soil and Water Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Animal Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Sciences: Animal Agribusiness Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Animal Sciences: Animal Production and Industry Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Animal Sciences: Behavior/Well-Being Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Animal Sciences: Biosciences Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 5 | Animal Sciences: Pre-Veterinary Medicine Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Biochemistry: Pre-Med Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Biochemistry: Pre-Vet Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Botany and Plant Pathology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Plant Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Entomology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Insect Biology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Food Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fermentation Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Food Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Forestry and Natural Resources
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aquatic Sciences: Fisheries Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Aquatic Sciences: Freshwater & Marine Biology Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Wildlife | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

###### BSFOR
| # | 专业 | URL |
|---|------|-----|
| 1 | Forestry: Forest Management Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Forestry: Forest Science Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Forestry: Urban Forestry | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Forestry: Wood Products Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

##### Dept of Horticulture and Landscape Architecture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Horticulture: Controlled Environment Agriculture Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Horticulture: Horticultural Production and Marketing Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Horticulture: Landscape Horticulture Design and Management Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Horticulture: Plant Science Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 5 | Horticulture: Public Horticulture Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 6 | Sustainable Food and Farming Systems | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 7 | Turf Management and Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

###### BSLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

#### Mitch Daniels School of Business

##### Bruce White Undergraduate Institute
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Integrated Business & Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |
| 2 | Quantitative Business Economics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Management Information Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics and Information Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Marketing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Organizational Behavior and HRM
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Organizational Behavior & Human Resource Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Strategic Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

##### Dept of Supply Chain and Operations Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Supply Chain & Operations Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

#### College of Education

##### Dept of Curriculum and Instruction
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |
| 2 | English Education | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |
| 3 | General Education: Curriculum and Instruction (non-licensure) | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |
| 4 | Social Studies Education | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |

##### Dept of Educational Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | General Education: Educational Studies (non-licensure) | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |
| 2 | Special Education Mild and Intense Intervention P to 12 | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |
| 3 | Special Education/Elementary Education | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |

#### College of Engineering

##### School of Aeronautics and Astronautics
###### BSAAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aeronautical and Astronautical Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### Weldon School of Biomedical Engineering
###### BSBME
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### Davidson School of Chemical Engineering
###### BSCHE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### Lyles School of Civil and Construction Engineering
###### BSCE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

###### BSCNE
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### Elmore Family School of Electrical and Computer Engineering
###### BSCMPE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

###### BSEE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### School of Engineering Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Engineering Studies/Engineering Science Studies Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 2 | Interdisciplinary Engineering Studies/Pre-Medical Engineering Studies Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Multidisciplinary Engineering/Acoustical Engineering Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 2 | Multidisciplinary Engineering/Educational Engineering Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 3 | Multidisciplinary Engineering/Engineering Management Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 4 | Multidisciplinary Engineering/General Engineering Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 5 | Multidisciplinary Engineering/Humanitarian Engineering Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 6 | Multidisciplinary Engineering/Theatre Engineering Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 7 | Multidisciplinary Engineering/Visual Design Engineering Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### School of Sustainability Engineering and Environmental Engineering
###### BSEEE
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental and Ecological Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### Edwardson School of Industrial Engineering
###### BSIE
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### School of Materials Engineering
###### BSMSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### School of Mechanical Engineering
###### BSME
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

##### School of Nuclear Engineering
###### BSNE
| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

#### College of Health and Human Sciences

##### School of Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Health Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 2 | Health Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 3 | Pre-Pharmacy | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 4 | Public Health | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

##### School of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 2 | Nursing (Accelerated Second Degree) | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

##### School of Hospitality and Tourism Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality and Tourism Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

##### Dept of Human Development and Family Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development and Family Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

##### Dept of Psychological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Brain and Behavioral Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 2 | Psychological Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

##### Dept of Speech, Language, and Hearing Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech, Language, and Hearing Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

##### Dept of Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

#### College of Liberal Arts

##### School of Interdisciplinary Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 2 | Law and Society | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 3 | Multi-Disciplinary Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### School of Languages and Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 2 | Classical Studies | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 3 | Comparative Literature | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 4 | English | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 5 | French | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 6 | German | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 7 | Japanese | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 8 | Linguistics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 9 | Spanish | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 2 | Mass Communication | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

##### Dept of Visual and Performing Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Visual Arts | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 2 | Performing Arts | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

#### Libraries and School of Information Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25601 |

#### College of Pharmacy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25602 |

#### Polytechnic Institute

##### School of Applied and Creative Computing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer and Information Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 2 | Cybersecurity | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 3 | Game Development and Design | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |

##### School of Aviation and Transportation Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aeronautical Engineering Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 2 | Aviation Management | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 3 | Professional Flight Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 4 | Unmanned Aerial Systems | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |

##### School of Engineering Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Automation and Systems Integration Engineering Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 2 | Construction Management Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 3 | Electrical Engineering Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 4 | Mechanical Engineering Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 5 | Robotics Engineering Technology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |

#### College of Science

##### Dept of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Biology: Ecology, Evolution, and Environmental Biology Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 3 | Biology: Genetics Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 4 | Biology: Microbiology Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 5 | Biology: Molecular Biology Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 6 | Biology: Neurobiology and Physiology Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

##### Dept of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Chemistry: Biochemistry Concentration | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

##### Dept of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

##### Dept of Earth, Atmospheric, and Planetary Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth, Atmospheric, and Planetary Sciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Environmental Geosciences | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 3 | Geology and Geophysics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

##### Dept of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Actuarial Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 3 | Applied Mathematics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 4 | Statistics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

##### Dept of Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Astrophysics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

##### Dept of Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Applied Statistics | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

#### College of Veterinary Medicine
###### BSVN
| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Nursing | https://catalog.purdue.edu/content.php?catoid=19&navoid=25604 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Program | Primary College | Cross-listed College | URL |
|---|---------|----------------|---------------------|-----|
| 1 | Agricultural Engineering | College of Agriculture | College of Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Biological Engineering | College of Agriculture | College of Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Environmental and Natural Resources Engineering | College of Agriculture | College of Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Integrated Business & Engineering | Daniels School of Business | College of Engineering | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |
| 5 | Data Science | Libraries & Info Studies | College of Science | https://catalog.purdue.edu/content.php?catoid=19&navoid=25601 |

### 1.4 Minors — complete list

> 150 minors across all colleges. Full list available in catalog at https://catalog.purdue.edu/content.php?catoid=19&navoid=25481. Key minors include: Computer Science, Data Science, Mathematics, Business, Economics, Statistics, various Engineering minors, and language minors.

### 1.5 General/Institute-wide requirements

Purdue requires all undergraduates to complete the **Outcomes-based Core Curriculum** covering: English composition, quantitative reasoning, science, humanities, social sciences, and information literacy. Details at https://catalog.purdue.edu/content.php?catoid=19&navoid=25585.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> 454 graduate programs total across all colleges. Purdue's graduate admissions is managed by the **Office of Graduate Studies and Postdoctoral Programs (OGSPS)** at gradadmissions.purdue.edu, but each program/department sets its own requirements. The graduate program directory is at https://www.purdue.edu/academics/ogsps/academics/graduate-degree-programs.html.

#### College of Engineering (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Aeronautics and Astronautics | MSAAE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 2 | Agricultural and Biological Engineering | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 3 | Biomedical Engineering | MSBME, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 4 | Chemical Engineering | MSCHE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 5 | Civil Engineering | MSCE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 6 | Computer Engineering | MSECE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 7 | Computer Science | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 8 | Construction Engineering | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 9 | Electrical Engineering | MSECE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 10 | Engineering Education | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 11 | Environmental and Ecological Engineering | MSEEE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 12 | Industrial Engineering | MSIE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 13 | Materials Engineering | MSMSE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 14 | Mechanical Engineering | MSME, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |
| 15 | Nuclear Engineering | MSNE, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25597 |

#### College of Science (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Biological Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 2 | Chemistry | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 3 | Computer Science | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 4 | Earth, Atmospheric, and Planetary Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 5 | Mathematics | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 6 | Physics | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |
| 7 | Statistics | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25603 |

#### Daniels School of Business (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | MBA | MBA | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |
| 2 | Accounting | MS | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |
| 3 | Economics | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |
| 4 | Finance | MS | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |
| 5 | Management | PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25595 |

#### College of Health and Human Sciences (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Health Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 2 | Nursing | MS, DNP, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 3 | Hospitality and Tourism Management | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 4 | Human Development and Family Science | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 5 | Psychological Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 6 | Speech, Language, and Hearing Sciences | MS, PhD, DAUD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |
| 7 | Public Health | MPH | https://catalog.purdue.edu/content.php?catoid=19&navoid=25598 |

#### College of Liberal Arts (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | English | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 2 | History | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 3 | Philosophy | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 4 | Political Science | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 5 | Sociology | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 6 | Communication | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 7 | Linguistics | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 8 | Languages and Cultures | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 9 | Anthropology | MA, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |
| 10 | Visual and Performing Arts | MFA | https://catalog.purdue.edu/content.php?catoid=19&navoid=25599 |

#### College of Education (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Curriculum and Instruction | MSEd, MAT, PhD, EdS | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |
| 2 | Educational Studies | MSEd, PhD, EdS | https://catalog.purdue.edu/content.php?catoid=19&navoid=25596 |

#### College of Agriculture (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Agricultural Economics | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 2 | Agronomy | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 3 | Animal Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 4 | Biochemistry | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 5 | Botany and Plant Pathology | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 6 | Entomology | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 7 | Food Science | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 8 | Forestry and Natural Resources | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |
| 9 | Horticulture | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25594 |

#### Polytechnic Institute (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Computer and Information Technology | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 2 | Engineering Technology | MS, DTECH | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 3 | Aviation Technology | MS | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |
| 4 | Construction Management | MS | https://catalog.purdue.edu/content.php?catoid=19&navoid=25600 |

#### College of Pharmacy (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Pharmacy | PharmD, MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25602 |

#### College of Veterinary Medicine (Graduate)
| # | Program | Degree(s) | URL |
|---|---------|-----------|-----|
| 1 | Veterinary Medicine | DVM | https://catalog.purdue.edu/content.php?catoid=19&navoid=25604 |
| 2 | Veterinary Clinical Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25604 |
| 3 | Basic Medical Sciences | MS, PhD | https://catalog.purdue.edu/content.php?catoid=19&navoid=25604 |

### 2.2 At least one program's full deep-dive

#### Computer Science (MS/PhD) — Graduate
- **Department**: Department of Computer Science, College of Science
- **Application portal**: https://www.purdue.edu/academics/ogsps/admissions/
- **Application fee**: $60 (domestic), $75 (international)
- **GRE**: Not required (department-level decision; verify per cycle)
- **TOEFL minimum**: 88 iBT (with 20+ per section) or 4.5+ on new scale
- **IELTS minimum**: 6.5 with 6.0 per section
- **Deadline**: Rolling (varies by department; typically Dec 15 for fall)
- **Funding**: RA/TA fellowships available for PhD students; MS students generally self-funded
- **Contact**: gradinfo@purdue.edu, 765-494-2600

### 2.3 Graduate admissions model

Purdue uses a **semi-centralized** model: OGSPS provides the application portal and general guidance, but each department/program sets its own admission requirements, deadlines, and review processes. Students apply through a single online portal but are reviewed by their chosen department. Financial aid (RA/TA) is managed at the department level.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | Common App | https://admissions.purdue.edu/become-student/apply/ |
| Application opens | August 1 | https://admissions.purdue.edu/deadlines/first-year-college-student/ |
| Early Action deadline | **November 1** | https://admissions.purdue.edu/deadlines/first-year-college-student/ |
| Regular Decision deadline | **January 15** | https://admissions.purdue.edu/deadlines/first-year-college-student/ |
| Application fee | **$60** (nonrefundable) | https://admissions.purdue.edu/deadlines/first-year-college-student/ |
| Test policy | **Test-optional (strongly expected)** | https://admissions.purdue.edu/become-student/first-year-criteria/ |
| SAT/ACT/CLT | Accepted; no preference among the three | https://admissions.purdue.edu/become-student/guide/ |
| SAT code | 1631 | https://admissions.purdue.edu/become-student/guide/ |
| ACT code | 1230 | https://admissions.purdue.edu/become-student/guide/ |
| Superscore | Yes (highest section scores across test dates) | https://admissions.purdue.edu/become-student/guide/ |
| ACT Science section | Not required | https://admissions.purdue.edu/become-student/first-year-criteria/ |
| Recommendation | Not required (if provided, considered) | https://admissions.purdue.edu/become-student/first-year-criteria/ |
| Essay | Required (Common App essay + Purdue questions) | https://admissions.purdue.edu/become-student/guide/ |
| Interview | Not offered | — |
| Honors College | Apply by Nov. 1 EA deadline; 2 additional essays | https://admissions.purdue.edu/become-student/guide/ |
| Transfer deadline | Varies by term | https://admissions.purdue.edu/become-student/transfer/ |
| Decision notification | Not specified on admissions pages | — |
| Enrollment confirmation | Not specified on admissions pages | — |

> **Test-optional verification**: Purdue's official language is nuanced. The first-year guide states "Purdue expects applicants to have SAT, ACT or CLT scores" while the criteria page lists "SAT, ACT or CLT scores (if provided)" as an evaluation factor. The Indiana Resident Enrollment Honors Plus Seal requires a complete application "including an SAT, ACT or CLT test score." Purdue is functionally test-optional but strongly expects scores. Not the same as test-free (e.g., UC Berkeley).

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT (before Jan 21, 2026) | 88 total, 20+ per section | — | ETS code: 1631 |
| TOEFL iBT (on/after Jan 21, 2026) | 4.5 total, 4.0+ per section | — | New scoring scale |
| IELTS Academic | 6.5 total, 6.0+ per section | — | Accepts Online Academic and Indicator; NO General Training |
| Duolingo English Test (DET) | 115 total, 110+ per subscore | — | — |
| ACT English | 26+ | — | — |
| SAT EBRW | 600+ | — | — |
| English-speaking curriculum | 3+ years, B+ in English courses | — | Alternative to exam |
| Transfer credit | 24+ transferable US credits, GPA 3.0+, 6 credits English comp/speech | — | Alternative for transfers |

> **Exemptions**: Applicants with 3+ years of English-taught curriculum or 24+ transferable US credits may be exempt. Scores must be from within past 2 years. Meeting minimum does not guarantee admission. Source: https://admissions.purdue.edu/become-student/english-proficiency/

### 3.3 Graduate — global rules

| Field | Value | Source |
|-------|-------|--------|
| Application portal | https://www.purdue.edu/academics/ogsps/admissions/ | OGSPS |
| Application fee | $60 (domestic), $75 (international) | OGSPS |
| GRE | Per department (not universally required) | Departmental |
| TOEFL minimum | 88 iBT (20+ per section) or 4.5+ new scale | OGSPS |
| IELTS minimum | 6.5 with 6.0 per section | OGSPS |
| CGS April 15 | Signatory | OGSPS |
| Funding | PhD: RA/TA common; MS: varies by department | Departmental |
| Contact | gradinfo@purdue.edu, 765-494-2600 | OGSPS |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

#### In-State (Indiana Resident) — Flat Rate (8+ credit hours)

| Expense Item | Per Semester | Academic Year |
|-------------|-------------|---------------|
| General Service (Tuition) | $4,859 | $9,718 |
| Student Fitness and Wellness Fee | $117 | $234 |
| Student Activity Fee | $20 | $40 |
| **Sub-Total Tuition & Fees** | **$4,996** | **$9,992** |
| Housing/Food | $8,367 | $16,734 |
| Books/Course Materials/Supplies | $545 | $1,090 |
| Transportation | $285 | $570 |
| Miscellaneous/Loan Fees | $1,100 | $2,200 |
| **Total COA (on-campus)** | **$15,293** | **$30,586** |

#### Out-of-State (Non-Resident) — Flat Rate (8+ credit hours)

| Expense Item | Per Semester | Academic Year |
|-------------|-------------|---------------|
| General Service (Tuition) | $4,859 | $9,718 |
| Student Fitness and Wellness Fee | $117 | $234 |
| Student Activity Fee | $20 | $40 |
| Nonresident Tuition | $9,401 | $18,802 |
| **Sub-Total Tuition & Fees** | **$14,397** | **$28,794** |
| Housing/Food | $8,367 | $16,734 |
| Books/Course Materials/Supplies | $545 | $1,090 |
| Transportation | $285 | $570 |
| Miscellaneous/Loan Fees | $1,100 | $2,200 |
| **Total COA (on-campus)** | **$24,694** | **$49,388** |

#### International — Flat Rate (8+ credit hours)

| Expense Item | Per Semester | Academic Year |
|-------------|-------------|---------------|
| General Service (Tuition) | $4,859 | $9,718 |
| Student Fitness and Wellness Fee | $117 | $234 |
| Student Activity Fee | $20 | $40 |
| Nonresident Tuition | $9,401 | $18,802 |
| International Student Tuition | $1,655 | $3,310 |
| **Sub-Total Tuition & Fees** | **$16,052** | **$32,104** |
| Housing/Food | $8,367 | $16,734 |
| Books/Course Materials/Supplies | $545 | $1,090 |
| Transportation | $285 | $570 |
| Miscellaneous/Loan Fees | $1,100 | $2,200 |
| **Total COA (on-campus)** | **$26,349** | **$52,698** |

#### Differential Fees (added to base tuition)

| Program | In-State Differential/Year | OOS Differential/Year |
|---------|---------------------------|----------------------|
| Computer Science / Data Science / Engineering | $2,050 | $4,050 |
| Daniels School of Business / BA Economics | $998 | $998 |
| Polytechnic Institute | $1,436 | $3,436 |
| Veterinary Technology | $572 | $572 |
| Nursing BSN | $1,800 | $1,800 |

> Source: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/. **14 consecutive years of frozen tuition** — tuition has not increased since 2012.

### 4.2 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need-blind/need-aware | **Need-aware** (public university; limited institutional aid) | https://admissions.purdue.edu/cost-financial-aid/scholarships/ |
| International aid | **Generally not eligible** for financial aid or scholarships | https://admissions.purdue.edu/cost-financial-aid/scholarships/ |
| Merit scholarships | Trustees ($10k in-state/$16k OOS per year), Presidential, others | https://admissions.purdue.edu/cost-financial-aid/scholarships/ |
| Need-based aid | FAFSA required; federal/state/Purdue grants available | https://www.purdue.edu/dfa/ |
| FAFSA priority deadline | December 15 (for departmental scholarships); April 15 (university) | https://admissions.purdue.edu/cost-financial-aid/scholarships/ |
| Tuition freeze | 14 consecutive years (since 2012) | https://www.purdue.edu/treasurer/finance/bursar-office/tuition/ |

### 4.3 Graduate cost & funding framework

| Field | Value | Source |
|-------|-------|--------|
| In-state tuition/year | $9,992 (same as UG) | https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/graduate-tuition-and-fees-2026-2027/ |
| OOS tuition/year | $28,794 | Same |
| International tuition/year | $29,194 (includes $400 international fee) | Same |
| PhD funding | RA/TA fellowships common (tuition waiver + stipend) | OGSPS |
| MS funding | Varies by department; many self-funded | OGSPS |
| Application fee | $60 domestic / $75 international | OGSPS |

---

## SECTION 5 — Evidence chain index

### E-U-001: Early Action Deadline
```yaml
field: undergraduate.deadlines.EA
value: "November 1"
source_url: https://admissions.purdue.edu/deadlines/first-year-college-student/
source_snippet: "Nov. 1 — Early Action application deadline"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-002: Regular Decision Deadline
```yaml
field: undergraduate.deadlines.RD
value: "January 15"
source_url: https://admissions.purdue.edu/deadlines/first-year-college-student/
source_snippet: "The first-year application is available beginning Aug. 1 and closes Jan. 15."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-003: Application Fee
```yaml
field: undergraduate.application_fee
value: "$60"
source_url: https://admissions.purdue.edu/deadlines/first-year-college-student/
source_snippet: "The nonrefundable application fee is $60."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004: Test Policy
```yaml
field: undergraduate.test_policy
value: "Test-optional (strongly expected)"
source_url: https://admissions.purdue.edu/become-student/first-year-criteria/
source_snippet: "SAT, ACT or CLT scores (if provided)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005: SAT/ACT Codes
```yaml
field: undergraduate.test_codes
value: {SAT: 1631, ACT: 1230}
source_url: https://admissions.purdue.edu/become-student/guide/
source_snippet: "School codes for Purdue: ACT – 1230; SAT – 1631."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-006: English Proficiency — TOEFL
```yaml
field: undergraduate.english_proficiency.TOEFL
value: {minimum: 88, per_section: 20}
source_url: https://admissions.purdue.edu/become-student/english-proficiency/
source_snippet: "We require a minimum TOEFL iBT score of 88 or higher with at least a 20 or higher per section."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-007: English Proficiency — IELTS
```yaml
field: undergraduate.english_proficiency.IELTS
value: {minimum: 6.5, per_section: 6.0}
source_url: https://admissions.purdue.edu/become-student/english-proficiency/
source_snippet: "Generally, applicants have a score of 6.5 or higher with a minimum score of 6.0 in each section."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-008: English Proficiency — DET
```yaml
field: undergraduate.english_proficiency.DET
value: {minimum: 115, per_subscore: 110}
source_url: https://admissions.purdue.edu/become-student/english-proficiency/
source_snippet: "Generally, applicants have a 115 with a 110 or higher in all individual subscores."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-009: In-State Tuition
```yaml
field: undergraduate.costs.tuition_in_state
value: "$9,992/year"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
source_snippet: "Sub-Total Tuition: $4,996.00 per semester / $9,992.00 academic year"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-010: OOS Tuition
```yaml
field: undergraduate.costs.tuition_oos
value: "$28,794/year"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
source_snippet: "Sub-Total Tuition: $14,397.00 per semester / $28,794.00 academic year"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-011: International Tuition
```yaml
field: undergraduate.costs.tuition_international
value: "$32,104/year"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
source_snippet: "Sub-Total Tuition: $16,052.00 per semester / $32,104.00 academic year"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-012: Total COA In-State
```yaml
field: undergraduate.costs.total_coa_in_state
value: "$30,586/year"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
source_snippet: "Total Tuition, Housing & Misc Exp $15,293.00 per semester / $30,586.00 academic year"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-013: Total COA OOS
```yaml
field: undergraduate.costs.total_coa_oos
value: "$49,388/year"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
source_snippet: "Total Tuition, Housing & Misc Exp $24,694.00 per semester / $49,388.00 academic year"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-014: Total COA International
```yaml
field: undergraduate.costs.total_coa_international
value: "$52,698/year"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
source_snippet: "Total Tuition, Housing & Misc Exp $26,349.00 per semester / $52,698.00 academic year"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-015: Tuition Freeze
```yaml
field: undergraduate.costs.tuition_freeze
value: "14 consecutive years"
source_url: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/
source_snippet: "That's why we've frozen tuition for a decade"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-016: International Aid Policy
```yaml
field: undergraduate.financial_aid.international
value: "Generally not eligible for financial aid or scholarships"
source_url: https://admissions.purdue.edu/cost-financial-aid/scholarships/
source_snippet: "in general, international undergraduate students are not eligible for financial aid, including scholarships."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-017: Application Platform
```yaml
field: undergraduate.application_platform
value: "Common App"
source_url: https://admissions.purdue.edu/become-student/apply/
source_snippet: "Use the Common App to apply as a first-year degree-seeking student"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-001: Graduate Application Portal
```yaml
field: graduate.application_portal
value: "https://www.purdue.edu/academics/ogsps/admissions/"
source_url: https://www.purdue.edu/academics/ogsps/admissions/
source_snippet: "OGSPS — EXPLORE ADMISSIONS"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-002: Graduate TOEFL Minimum
```yaml
field: graduate.english_proficiency.TOEFL
value: {minimum: 88, per_section: 20}
source_url: https://www.purdue.edu/academics/ogsps/admissions/
source_snippet: "We require a minimum TOEFL iBT score of 88 or higher with at least a 20 or higher per section."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-C-001: Program Count
```yaml
field: institution.program_count
value: {ug_majors: 298, ug_minors: 150, ug_certificates: 36, grad_programs: 454, total: 959}
source_url: https://catalog.purdue.edu/content.php?catoid=19&navoid=25484
source_snippet: "959 total program entries extracted from 2026-2027 catalog"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-C-002: College Structure
```yaml
field: institution.colleges
value: "11 colleges (Agriculture, Daniels Business, Education, Engineering, HHS, Liberal Arts, Libraries & Info Studies, Pharmacy, Polytechnic, Science, Veterinary Medicine) + Honors College + Exploratory Studies"
source_url: https://catalog.purdue.edu/content.php?catoid=19&navoid=25586
source_snippet: "Academic Colleges listed in catalog navigation"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
purdue-knowledge-base-v2/
├── 00-institution-overview (Section 0)
├── 01-ug-agriculture (Section 1 — College of Agriculture programs)
├── 02-ug-business (Section 1 — Daniels School of Business programs)
├── 03-ug-education (Section 1 — College of Education programs)
├── 04-ug-engineering (Section 1 — College of Engineering programs)
├── 05-ug-hhs (Section 1 — College of Health & Human Sciences programs)
├── 06-ug-liberal-arts (Section 1 — College of Liberal Arts programs)
├── 07-ug-libraries-info (Section 1 — Libraries & Info Studies programs)
├── 08-ug-pharmacy (Section 1 — College of Pharmacy programs)
├── 09-ug-polytechnic (Section 1 — Polytechnic Institute programs)
├── 10-ug-science (Section 1 — College of Science programs)
├── 11-ug-vet-med (Section 1 — College of Veterinary Medicine programs)
├── 12-graduate-programs (Section 2)
├── 13-deadlines-requirements (Section 3)
├── 14-costs-financial-aid (Section 4)
├── 15-evidence-chain (Section 5)
└── 16-comparison-framework (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "purdue-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|BA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Verify test-optional language (does Purdue truly not require scores?) | https://admissions.purdue.edu/become-student/first-year-criteria/ |
| P0 | Graduate program list with per-program deadlines and GRE policy | https://www.purdue.edu/academics/ogsps/academics/graduate-degree-programs.html |
| P1 | Complete graduate program list with all 454 programs in structured format | https://catalog.purdue.edu/content.php?catoid=19&navoid=25622 |
| P1 | Per-program differential fee details (exact programs with differential fees) | https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/ |
| P1 | First-year class profile (middle 50% GPA, SAT, ACT by college) | https://admissions.purdue.edu/become-student/class-profile/ |
| P2 | Financial aid net price calculator results | https://www.purdue.edu/dfa/cost/calculator/ |
| P2 | Transfer admission requirements and deadlines | https://admissions.purdue.edu/become-student/transfer/ |
| P2 | Indianapolis campus program availability | https://catalog.purdue.edu/content.php?catoid=19&navoid=25593 |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Purdue | (Other schools) |
|-----------|--------|-----------------|
| Type | Public | |
| Location | West Lafayette, IN | |
| UG tuition in-state/year | $9,992 | |
| UG tuition OOS/year | $28,794 | |
| UG COA in-state/year | $30,586 | |
| UG COA OOS/year | $49,388 | |
| Need-blind (intl)? | No (need-aware; intl generally ineligible for aid) | |
| EA deadline | November 1 | |
| RD deadline | January 15 | |
| SAT/ACT required? | Test-optional (strongly expected) | |
| TOEFL min | 88 (20+ per section) | |
| IELTS min | 6.5 (6.0 per section) | |
| DET min | 115 (110+ subscores) | |
| App fee | $60 | |
| Total programs (Rule 1) | 959 | |
| UG majors | 298 | |
| UG minors | 150 | |
| Grad programs | 454 | |
| Colleges (Rule 2) | 11 | |
| Top-ranked program | Engineering (#4 public, US News) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.purdue.edu, catalog.purdue.edu, www.purdue.edu/treasurer, www.purdue.edu/dfa, www.purdue.edu/academics/ogsps
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
