# Auburn University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BA/BFA/BArch/etc.) | 175 |
| 本科辅修 (Minor) | ~104 |
| 研究生学位项目 (MS/MA/MAcc/PhD/DVM/etc.) | ~120 |
| 研究生证书 (Graduate Certificate) | ~44 |
| **学位项目总计 (UG + Grad)** | **~339+** |
| 学院 / 独立系所总数 | 13 (含 University College + Graduate School) |

> 注：UG major 数来自 bulletin.auburn.edu/undergraduate/majors/ 目录（含学位后缀的条目）；minor 数来自 bulletin.auburn.edu/undergraduate/minors/ 页面链接计数；grad 数来自 bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/ 目录（过滤导航链接后）。

### 0.2 学院 / 系层级结构

```
Auburn University
├── College of Agriculture                                  [学院]
│   ├── Agricultural Economics and Rural Sociology           [系]
│   ├── Animal Sciences                                      [系]
│   ├── Biosystems Engineering (shared w/ Engineering)        [系]  ⚠
│   ├── Crop, Soil and Environmental Sciences                [系]
│   ├── Entomology and Plant Pathology                       [系]
│   ├── Fisheries, Aquaculture and Aquatic Sciences           [系]
│   ├── Horticulture                                         [系]
│   ├── Poultry Science                                      [系]
│   └── General Agriculture                                  [系]
├── College of Architecture, Design and Construction         [学院]
│   ├── Architecture                                         [系]
│   ├── Building Science                                     [系]
│   └── Industrial and Graphic Design                        [系]
├── Raymond J. Harbert College of Business                   [学院]
│   ├── School of Accountancy                                [系]
│   ├── Department of Business Analytics and Information Systems [系]
│   ├── Department of Finance                                [系]
│   ├── Department of Management                             [系]
│   ├── Department of Marketing                              [系]
│   └── School of Supply Chain Management                    [系]
├── College of Education                                     [学院]
│   ├── Curriculum and Teaching                              [系]
│   ├── Kinesiology                                          [系]
│   └── Special Education, Rehabilitation and Counseling     [系]
├── Samuel Ginn College of Engineering                       [学院]
│   ├── Department of Aerospace Engineering                  [系]
│   ├── Department of Biosystems Engineering (shared w/ Ag)  [系]  ⚠
│   ├── Department of Chemical Engineering                   [系]
│   ├── Department of Civil Engineering                      [系]
│   ├── Department of Computer Science and Software Engineering [系]
│   ├── Department of Electrical and Computer Engineering    [系]
│   ├── Department of Industrial and Systems Engineering     [系]
│   └── Department of Mechanical Engineering                 [系]
├── College of Forestry, Wildlife and Environment            [学院]
│   ├── Forestry                                             [系]
│   ├── Wildlife Sciences                                    [系]
│   └── Geospatial / Environmental Conservation              [系]
├── College of Human Sciences                                [学院]
│   ├── Consumer and Design Sciences                         [系]
│   ├── Human Development and Family Studies                 [系]
│   ├── School of Hospitality Management                     [系]
│   └── Nutritional Sciences                                 [系]
├── College of Liberal Arts                                  [学院]
│   ├── Department of Aviation                               [系]
│   ├── Department of Communication and Journalism           [系]
│   ├── Department of Communication Disorders                [系]
│   ├── Department of Economics                              [系]
│   ├── Department of English                                [系]
│   ├── Department of Foreign Languages and Literatures      [系]
│   ├── Department of History                                [系]
│   ├── Department of Philosophy                             [系]
│   ├── Department of Political Science                      [系]
│   ├── Department of Psychology                             [系]
│   ├── School of Fine Arts (Art)                            [系]
│   ├── Department of Sociology, Anthropology and Social Work [系]
│   ├── Music                                                [系]
│   └── Theatre                                              [系]
├── College of Nursing                                       [学院]
│   └── Nursing                                              [系]
├── James I. Harrison College of Pharmacy                    [学院]
│   └── Drug and Biopharmaceutical Sciences                  [系]
├── College of Sciences and Mathematics                      [学院]
│   ├── Biological Sciences                                  [系]
│   ├── Chemistry and Biochemistry                           [系]
│   ├── Geology and Geography                                [系]
│   ├── Mathematics and Statistics                           [系]
│   ├── Physics                                              [系]
│   └── Pre-Health Professional Curricula                    [系]
├── College of Veterinary Medicine                           [学院]
│   └── Veterinary Medicine / Public and One Health          [系]
├── School of Nursing                                        [学院] (under College of Nursing)
├── University College                                       [学院]
│   └── Interdisciplinary University Studies                 [系]
└── Graduate School                                          [学院] (administers all grad programs)
```

> ⚠ Biosystems Engineering is jointly housed in College of Agriculture AND Samuel Ginn College of Engineering; listed under both in the catalog.

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | 32 |
| BS | BS | Bachelor of Science | 本科 | 104 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 6 |
| BArch | BArch | Bachelor of Architecture | 本科 | 2 |
| BSBA | BSBA | Bachelor of Science in Business Administration | 本科 | 10 |
| BAE | BAE | Bachelor of Aerospace Engineering | 本科 | 1 |
| BBSE | BBSE | Bachelor of Biosystems Engineering | 本科 | 3 |
| BCHE | BCHE | Bachelor of Chemical Engineering | 本科 | 1 |
| BCE | BCE | Bachelor of Civil Engineering | 本科 | 1 |
| BCPE | BCPE | Bachelor of Computer Engineering | 本科 | 1 |
| BCS | BCS | Bachelor of Computer Science | 本科 | 1 |
| BEE | BEE | Bachelor of Electrical Engineering | 本科 | 1 |
| BISE | BISE | Bachelor of Industrial and Systems Engineering | 本科 | 1 |
| BMTLE | BMTLE | Bachelor of Materials Engineering | 本科 | 1 |
| BME | BME | Bachelor of Mechanical Engineering | 本科 | 1 |
| BSWE | BSWE | Bachelor of Software Engineering | 本科 | 1 |
| BIND | BIND | Bachelor of Industrial Design | 本科 | 1 |
| BIARCH | BIARCH | Bachelor of Interior Architecture | 本科 | 2 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| BMED | BMED | Bachelor of Music Education | 本科 | 1 |
| BMU | BMU | Bachelor of Music | 本科 | 5 |
| MA | MA | Master of Arts | 研究生 | ~15 |
| MS | MS | Master of Science | 研究生 | ~45 |
| MFA | MFA | Master of Fine Arts | 研究生 | ~2 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | ~20 |
| MAcc | MAcc | Master of Accountancy | 研究生 | 1 |
| MAg | MAg | Master of Agriculture | 研究生 | ~3 |
| MBC | MBC | Master of Building Construction | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MArch | MArch | Master of Architecture | 研究生 | ~1 |
| EdS | EdS | Education Specialist | 研究生 | ~12 |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~35 |
| EdD | EdD | Doctor of Education | 研究生 | ~2 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| AuD | AuD | Doctor of Audiology | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| GCert | Graduate Certificate | Graduate Certificate | 研究生证书 | ~44 |

> Auburn 使用大量工程领域专属学士学位缩写（BAE/BBSE/BCHE/BCE/BCPE/BCS/BEE/BISE/BMTLE/BME/BSWE），canonical 层面均映射到 BS。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BArch | BSBA | BEng* | BMU | BMED | Minor | MA | MS | MBA | MEd | MFA | MAcc | MAg | MBC | MSW | EdS | PhD | EdD | DVM | AuD | DPT | GCert | 合计 |
|------------|----|----|-----|-------|------|-------|-----|------|-------|----|----|-----|-----|-----|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-------|------|
| College of Agriculture | 0 | 18 | 0 | 0 | 0 | 1 | 0 | 0 | ~11 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | ~40 |
| Architecture, Design & Construction | 0 | 3 | 1 | 2 | 0 | 0 | 0 | 0 | ~3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | ~15 |
| Harbert College of Business | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | ~5 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | ~22 |
| College of Education | 0 | 19 | 0 | 0 | 0 | 0 | 0 | 1 | ~4 | 0 | 6 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 10 | 3 | 2 | 0 | 0 | 0 | 6 | ~66 |
| Samuel Ginn College of Engineering | 0 | 2 | 0 | 0 | 0 | 10 | 0 | 0 | ~5 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 8 | ~39 |
| Forestry, Wildlife & Environment | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | ~4 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | ~20 |
| College of Human Sciences | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | ~21 |
| College of Liberal Arts | 26 | 6 | 5 | 0 | 0 | 0 | 5 | 0 | ~20 | 8 | 4 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 5 | 0 | 0 | 0 | 0 | 5 | ~87 |
| College of Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 |
| Harrison College of Pharmacy | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~2 |
| Sciences and Mathematics | 4 | 41 | 0 | 0 | 0 | 0 | 0 | 0 | ~15 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 5 | ~83 |
| Veterinary Medicine | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 | ~8 |
| University College | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~1 |
| **合计** | **30** | **117** | **6** | **2** | **10** | **11** | **5** | **1** | **~104** | **8** | **~41** | **1** | **14** | **2** | **1** | **3** | **1** | **1** | **10** | **~32** | **2** | **1** | **1** | **1** | **~44** | **~339+** |

> *BEng* 列合并了 Auburn 所有工程领域专属学士学位（BAE/BBSE/BCHE/BCE/BCPE/BCS/BEE/BISE/BMTLE/BME/BSWE），canonical 映射到 BS/工程学士。
> 矩阵中带 ~ 的数字为估算值（minor/grad 部分因目录解析限制未能逐条精确归因到系）。

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Auburn University 有 12 个本科学院 + 1 个 University College。详见 Section 0.2 层级树。

### 1.2 Undergraduate Majors — 按 学院 > 系 > 学位级别 分组

#### College of Agriculture

##### Agricultural Economics and Rural Sociology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Business & Economics | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/agriculturaleconomicsandruralsociology/agriculturalbusinessandeconomics_major/ |

##### General Agriculture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Communications | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/generalagriculture/agcommunications_major/ |

##### Horticulture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Science | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/horticulturehort/agriculturalscience_major/ |
| 2 | Horticulture — Fruit and Vegetable Production Track | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/horticulturehort/fruitandvegetableproductionemphasis_major/ |
| 3 | Horticulture — Landscape Horticulture Track | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/horticulturehort/horticulture_landscapehorticultureemphasis_major/ |
| 4 | Horticulture — Nursery and Greenhouse Science Track | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/horticulturehort/horticulture_nurseryandgreenhouseemphasis_major/ |
| 5 | Horticulture — Pre-Landscape Architecture Track | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/horticulturehort/prelandscape_architecture_major/ |

##### Animal Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Sciences — Animal Industries Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/animalsciencesansc/animalsciences_productionoption_major/ |
| 2 | Animal Sciences — Pre-Veterinary & Animal Biosciences Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/animalsciencesansc/animalsciences_pre-vetrinarymedicine_professionaloption_major/ |

##### Entomology and Plant Pathology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Biotechnology | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/entomologyandplantpathology/appliedbiotechnology_major/ |

##### Biosystems Engineering (shared with Engineering)
###### BS / BBSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological and Agricultural Technology Management (BS) | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/biosystemsengineeringbsen/BioTech_major/ |
| 2 | Biosystems Engineering (BBSE) | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofbiosystemsengineering/biosystemsengineering_major/ |
| 3 | Biosystems Engineering — Bioprocess Engineering Option (BBSE) | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofbiosystemsengineering/biosystemsengineeringbioprocessengr_obtion/ |
| 4 | Biosystems Engineering — Ecological Engineering Option (BBSE) | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofbiosystemsengineering/ecologicalengineeringoption_major/ |
| 5 | Biosystems Engineering — Forest Engineering Option (BBSE) | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofbiosystemsengineering/forestengineering_major/ |

##### Crop, Soil and Environmental Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Crop and Soil Sciences | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/agronomyandsoilsagrn/agronomysoils_science_major |
| 2 | Crop and Soil Sciences — Turfgrass Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/agronomyandsoilsagrn/agronomysoils_turfgrass_major |
| 3 | Environmental Science | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/agronomyandsoilsagrn/environmentalscience_major/ |

##### Fisheries, Aquaculture and Aquatic Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries, Aquaculture, and Aquatic Sciences — Fisheries and Aquaculture Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/fisheriesandalliedaquaculturesfish/fisheriesandaquaculture_major/ |
| 2 | Fisheries, Aquaculture, and Aquatic Sciences — Marine Resources Management Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/fisheriesandalliedaquaculturesfish/marineresources_major/ |
| 3 | Fisheries, Aquaculture, and Aquatic Sciences — Pre-Professional Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/fisheriesandalliedaquaculturesfish/fisheries_preprofessional_major/ |

##### Poultry Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Poultry Science — Production Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/poultrysciencepoul/poultryscience_poultryproductionoption_major/ |
| 2 | Poultry Science — Pre-Veterinary Medicine Option | https://bulletin.auburn.edu/undergraduate/collegeofagriculture/poultrysciencepoul/poultryscience_pre-veterinarymedicineoption_major/ |

---

#### College of Architecture, Design and Construction

##### Architecture
###### BArch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture (Foundation Unit) | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/architecture_foundation-unit_major/ |
| 2 | Architecture (Summer Design) | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/architecture_summer-design_major/ |

###### BIARCH
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture/Interior Architecture (Foundation Unit) | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/architectureinterior-foundationunit_major/ |
| 2 | Architecture/Interior Architecture (Summer Design) | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/architectureinterior-summerdesign_major/ |

###### BLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/Landscape_major/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Design | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/environmentaldesign_major/ |
| 2 | Environmental Design — Pre-Landscape Architecture | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/architecture/environmentaldesign-prelandscapearchitecturetrack_major/ |

##### Building Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Building Science | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/buildingscience/buildingscience_major/ |

##### Industrial and Graphic Design
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Graphic Design | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/industrialandgraphicdesign/graphicdesign_major/ |

###### BIND
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Design | https://bulletin.auburn.edu/undergraduate/collegeofarchitecturedesignandconstruction/industrialandgraphicdesign/industrialdesign_major |

---

#### Raymond J. Harbert College of Business

##### School of Accountancy
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy — On-Campus Option for First Degree Candidates | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/schoolofaccountancyacct/accountancy_major/ |
| 2 | Accountancy — Online Option for Second Degree Candidates | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/schoolofaccountancyacct/accountancyonline_major |

##### Department of Business Analytics and Information Systems
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/department-of-business-analytics-and-information-systems/businessanalytics_major/ |
| 2 | Information Systems Management | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/department-of-business-analytics-and-information-systems/informationsystemsmanagement_major/ |

##### Department of Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/departmentoffinancefinc/finance_major/ |

##### Department of Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration — On-Campus Option | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/departmentofmanagementmngt/businessadministration_major/ |
| 2 | Business Administration — Online Degree Completer Program | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/departmentofmanagementmngt/businessadministrationonline_major/index.html |
| 3 | Management | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/departmentofmanagementmngt/management_major/ |

##### Department of Marketing
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/departmentofmarketingmktg/marketing_major/ |

##### School of Supply Chain Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Supply Chain Management | https://bulletin.auburn.edu/undergraduate/collegeofbusiness/schoolofsupplychainmgntscmn/scmn_major |

---

#### College of Education

##### Curriculum and Teaching
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agriscience Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/agriscienceeducation_major/ |
| 2 | Business and Marketing Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/businessandmarketing_major/ |
| 3 | Chemistry Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/chemistryeducation_major/ |
| 4 | Early Childhood Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/earlychildhoodeducation_major/ |
| 5 | Elementary Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/elementaryeducation_major/ |
| 6 | English Language Arts Education/English | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/englishlanguageartseducation_major/ |
| 7 | French Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/foreignlanguageeducation-french_major/ |
| 8 | General Science Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/generalscienceeducation-geologyearthsystem |
| 9 | General Social Science Education/History | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/generalsocialscienceeducation-history/ |
| 10 | German Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/foreignlanguageeducation-german_major/ |
| 11 | Mathematics Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/mathematicseducation_major/ |
| 12 | Physics Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/physicseducation_major/ |
| 13 | Science Teaching (double major) | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/scienceteachingdouble_major/ |
| 14 | Spanish Education | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/foreignlanguageeducation-spanish_major/ |

###### BMED
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education: Instrumental and Vocal | https://bulletin.auburn.edu/undergraduate/collegeofeducation/curriculumandteaching/musiceducation-instrumentalandvocal_major/ |

##### Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise, Performance, & Health Optimization | https://bulletin.auburn.edu/undergraduate/collegeofeducation/kinesiology/exerciseperformance_and_healthoptimization_major/index.html |
| 2 | Exercise Science | https://bulletin.auburn.edu/undergraduate/collegeofeducation/kinesiology/exercisescience_major/ |

##### Special Education, Rehabilitation and Counseling
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Collaborative Teacher Special Education: K–12 | https://bulletin.auburn.edu/undergraduate/collegeofeducation/specialeducationrehabilitationandcounseling/collaborativeteachereducation_major/ |
| 2 | Early Childhood/Elementary Special Education: P–6 | https://bulletin.auburn.edu/undergraduate/collegeofeducation/specialeducationrehabilitationandcounseling/earlychildhoodspecialeducation_major/ |
| 3 | Rehabilitation and Disability Studies | https://bulletin.auburn.edu/undergraduate/collegeofeducation/specialeducationrehabilitationandcounseling/rehabilitationanddisabilitystudies_major/ |

---

#### Samuel Ginn College of Engineering

##### Department of Aerospace Engineering
###### BAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofaerospaceengineering/aerospaceengineering_major/ |

##### Department of Chemical Engineering
###### BCHE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofchemicalengineering/chemicalengineering_major/ |

##### Department of Civil Engineering
###### BCE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofcivilengineering/civilengineering_major/ |

##### Department of Electrical and Computer Engineering
###### BCPE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofelectricalandcomputerengineering/computerengineering_major/ |

###### BEE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofelectricalandcomputerengineering/electricalengineering_major/ |

##### Department of Computer Science and Software Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofcomputerscienceandsoftwareengineering/computerscience_major/ |

###### BCS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science — Online Degree Completer Program | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofcomputerscienceandsoftwareengineering/bachelorofcomputerscience_major/ |

###### BSWE
| # | 专业 | URL |
|---|------|-----|
| 1 | Software Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofcomputerscienceandsoftwareengineering/softwareengineering_major/ |

##### Department of Industrial and Systems Engineering
###### BISE
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial and Systems Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofindustrialandsystemsengineering/industrialandsystemsengineering_major/ |

##### Department of Mechanical Engineering
###### BMTLE
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofmechanicalengineering/materialsengineering_major/ |

###### BME
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofmechanicalengineering/mechanicalengineering_major/ |

---

#### College of Forestry, Wildlife and Environment

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Conservation and Management | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/environmentalconservationandmanagement_major/index.html |
| 2 | Forestry | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/preforestry_major/forestry |
| 3 | Geospatial Information Science | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/preforestry_major/geospatialandenvironmentalinformatics/ |
| 4 | Parks and Recreation Management | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/parksandrecreationmanagement_major |
| 5 | Sustainable Packaging | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/forestryandwildlifescience/sustainablebiomaterialsandpackaging_major/ |
| 6 | Wildlife Ecology and Management | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/forestryandwildlifescience/wildlifeecologyandmanagement_major/ |
| 7 | Wildlife Enterprise Management | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/forestryandwildlifescience/wildlifeEnterprisemanagement_major/ |
| 8 | Wildlife Sciences — Pre-Veterinary Medicine | https://bulletin.auburn.edu/undergraduate/schoolofforestryandwildlifesciences/forestryandwildlifescience/wildlifescience-prevetconcentration_major/ |

---

#### College of Human Sciences

##### Consumer and Design Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Apparel Merchandising, Design and Production Management — Apparel Merchandising Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofconsumeranddesignsciences/apparelmerchandisingoption_major/ |
| 2 | Apparel Merchandising, Design and Production Management — Apparel Design and Production Management Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofconsumeranddesignsciences/productdesignandproductionmanagementoption_major/ |
| 3 | Interior Design | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofconsumeranddesignsciences/interiordesign_major/ |
| 4 | Philanthropy and Non-Profit Studies | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofconsumeranddesignsciences/philanthropy_major/ |

##### Human Development and Family Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Studies in Human Sciences | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofhumandevelopmentandfamilystudies/globalstudies_major/ |
| 2 | Human Development and Family Science | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofhumandevelopmentandfamilystudies/humandevelopmentandfamilystudies_major/ |
| 3 | Human Development and Family Science — Child Life Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofhumandevelopmentandfamilystudies/humandevelopmentandfamilyscienceoptioninchildlife/index.html |
| 4 | Human Development and Family Science — Early Child Development | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofhumandevelopmentandfamilystudies/humandevelopmentandfamilyscienceoptioninearlychilddevelopment/index.html |

##### School of Hospitality Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management — Culinary Science Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/schoolofhospitalitymanagement/hospitalitymanagement_culinaryscienceoption_major/index.html |
| 2 | Hospitality Management — Event Management Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/schoolofhospitalitymanagement/hospitalitymanagement_eventmanagementoption_major/index.html |
| 3 | Hospitality Management — Hotel and Restaurant Management Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/schoolofhospitalitymanagement/hospitalitymanagement_hotelandrestaurantmanagementoption_major/index.html |

##### Nutritional Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition — Nutrition/Dietetics Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofnutritionalsciences/nutritiondieteticsoption_major/index.html |
| 2 | Nutrition — Nutrition Science Option (pre-professional) | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofnutritionalsciences/nutritionscienceoption_major/index.html |
| 3 | Nutrition — Nutrition Wellness Option | https://bulletin.auburn.edu/undergraduate/collegeofhumansciences/departmentofnutritionalsciences/wellnessoption_major/index.html |

---

#### College of Liberal Arts

##### Department of Aviation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aviation Management | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofaviation/aviationmanagment_option/ |
| 2 | Professional Flight | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofaviation/professionalflight/ |

##### Department of Communication and Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationjournalismcmjn/communication_major/ |
| 2 | Film and Media Studies | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationjournalismcmjn/radiotelevisionandfilm_major/ |
| 3 | Film and Media Studies — Film Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationjournalismcmjn/mediastudiesviualmedia_major/ |
| 4 | Journalism | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationjournalismcmjn/journalism_major/ |
| 5 | Journalism — Sports Production Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationjournalismcmjn/journalismsportsprod_major/ |
| 6 | Public Relations | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationjournalismcmjn/publicrelations_major/ |

##### Department of Communication Disorders
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech, Language, and Hearing Sciences | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofcommunicationdisorderscmds/SLHS_major/ |

##### Department of Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics — Primary Track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofeconomicsecon/economics-primarytrack_major/ |
| 2 | Economics — Quantitative Track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofeconomicsecon/economics-quantitativetrack_major/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English — Creative Writing Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofenglishengl/english-creativewriting_major/ |
| 2 | English — Literature Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofenglishengl/english-literature_major/ |
| 3 | English — Professional and Public Writing Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofenglishengl/english-professionalwritingandliteracystudies_major/ |

##### Department of Foreign Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/french_major/ |
| 2 | French — International Trade Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/french-internationaltrade_major/ |
| 3 | German | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/german_major/ |
| 4 | German — International Trade Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/german-internationaltrade_major/ |
| 5 | International Studies | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/internationalstudies_major/index.html |
| 6 | Spanish | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/spanish_major/ |
| 7 | Spanish — International Trade Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofforeignlanguagesandliteraturesflng/spanish-internationaltrade_major/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofhistory/history_major/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofphilosophyphil/philosophy_major/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Services Administration | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofpoliticalsciencepoli/healthservicesadministration_major/ |
| 2 | Law and Justice | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofpoliticalsciencepoli/lawandjustice_major/ |
| 3 | Political Science | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofpoliticalsciencepoli/politicalscience_major/ |
| 4 | Public Administration | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofpoliticalsciencepoli/publicadministration_major/ |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofpsychologypsyc/psychology_major/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofpsychologypsyc/neuroscience/index.html |

##### School of Fine Arts (Art)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/schooloffinearts/art_major/ |
| 2 | Art History Option | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/schooloffinearts/arthistory_major/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Studio/Fine Arts | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/schooloffinearts/studio-finearts_major/ |

##### Department of Sociology, Anthropology and Social Work
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofsociologyanthropologyandsocialworksocy/anthropology_major/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofsociologyanthropologyandsocialworksocy/socialwork_major/ |
| 2 | Sociology | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/departmentofsociologyanthropologyandsocialworksocy/sociology_major/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/music/music_major/ |

###### BMU
| # | 专业 | URL |
|---|------|-----|
| 1 | Music: Commercial Music track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/music/musicperformance-commercial_major/index.html |
| 2 | Music: Composition (Technology) track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/music/musicperformance-composition_major/ |
| 3 | Music: Instrumental track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/music/musicperformance-instrumental_major/ |
| 4 | Music: Piano track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/music/musicperformance-piano_major/ |
| 5 | Music: Voice track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/music/musicperformance-voice_major/ |

##### Theatre
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/theatre/theatre_major |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre/Fine Arts — Design/Technology Track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/theatre/theatre-designtechnology_major |
| 2 | Theatre/Fine Arts — Management Track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/theatre/theatre-management_major |
| 3 | Theatre/Fine Arts — Music Theatre Track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/theatre/theatre-musictheatre_major |
| 4 | Theatre/Fine Arts — Performance Track | https://bulletin.auburn.edu/undergraduate/collegeofliberalarts/theatre/theatre-performance_major |

---

#### College of Nursing

##### Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing — Traditional | https://bulletin.auburn.edu/undergraduate/schoolofnursing/nursingtraditional_major/ |
| 2 | RN — BSN | https://bulletin.auburn.edu/undergraduate/schoolofnursing/nursingRNtoBSN_major/ |

---

#### James I. Harrison College of Pharmacy

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Drug and Biopharmaceutical Sciences | https://bulletin.auburn.edu/undergraduate/jamesharrisonschoolofpharmacy/drugandbiopharmaceuticalsciences_major/index.html |

---

#### College of Sciences and Mathematics

##### Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/mathematicsandstatistics/appliedmathematics_major/ |
| 2 | Applied Mathematics — Actuarial Science Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/mathematicsandstatistics/actuarialscience_major/ |
| 3 | Applied Mathematics — Applied Discrete Mathematics Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/mathematicsandstatistics/applieddiscretemathematics_major/ |
| 4 | Mathematics | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/mathematicsandstatistics/mathematics_major |

##### Chemistry and Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry (BA) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/bacurriculuminchemistry_major/ |
| 2 | Chemistry (BA) — Forensics Track | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/bacurriculuminchemistryforensics_major/ |
| 3 | Pre-Medicine, Pre-Dental, Pre-Optometry (BA Chemistry) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/bacurriculuminchemistry_major_pre-meddenopt/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry (BS) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/bscurriculuminchemistry_major/ |
| 2 | Biochemistry Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/biochemistry_major |
| 3 | Laboratory Science | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/laboratorytechnology_major/ |
| 4 | Laboratory Science - Histotechnology Track | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/laboratoryhistotechnology_major/ |
| 5 | Laboratory Science — Pre-Medicine | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/laboratorytechnology_premed_major/ |
| 6 | Laboratory Science — Pre-Physician Assistant | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/laboratorytechnology_prepa_major/ |
| 7 | Medical Laboratory Science | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/chemistryandbiochemistry/medicaltechnology_major |

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Genetics | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/genetics_major/ |
| 2 | Marine Biology | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/marinebiology_major |
| 3 | Microbial, Cellular and Molecular Biology — Microbiology Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/microbialcellularmolecularbiology-microbiology_major |
| 4 | Microbial, Cellular and Molecular Biology — Cell & Molecular Biology Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/microbialcellularmolecularbiology-cellmolecularbiology_major |
| 5 | Organismal Biology — Conservation & Biodiversity Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/orgbio-conversationbiodiversity_major/ |
| 6 | Organismal Biology — Ecology, Evolution & Behavior Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/orgbio-ecoevolutionbehavior_major/ |
| 7 | Organismal Biology — Integrative Biology Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/orgbiointegrativebio_major/ |

##### Geology and Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography and Environmental Studies | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/geologyandgeography/geography_major |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/geologyandgeography/geology_major |
| 2 | Geology — Earth System Science Option | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/geologyandgeography/geologyearthscienceoption_major/ |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/physics/physics_major/ |

##### Pre-Health Professional Curricula
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-Pharmacy | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/biomedicalsciences_major_pre-phar/ |
| 2 | Pre-Medicine, Pre-Dental, Pre-Optometry (Biomedical Sciences) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/biomedicalsciences_major_pre-med/ |
| 3 | Pre-Anesthesiologist Assistant | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/biomedicalsciences_major_anesth/ |
| 4 | Health Sciences, Pre-Physical Therapy, Pre-Physician Assistant | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/biomedicalsciences_major_InterHealth/ |
| 5 | Pre-Medicine, Pre-Dental, Pre-Optometry (Genetics) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/genetics_major_pre-med/index.html |
| 6 | Pre-Veterinary Medicine (Genetics) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/genetics_major_pre-vet/ |
| 7 | Pre-Medical, Pre-Dental, Pre-Optometry (Microbiology) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/microbialcellularmolecularbiology-microbiology_major_pre-med/ |
| 8 | Pre-Physical Therapy, Pre-Physician Assistant (Microbiology) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/microbialcellularmolecularbiology-microbiology_major_pre-pphsppat/ |
| 9 | Pre-Veterinary Medicine (Microbiology) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/microbiology_preveterinarymedicine_major/ |
| 10 | Pre-Medicine, Pre-Dental, Pre-Optometry (Organismal Bio) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/ibio_major_premed/ |
| 11 | Pre-Physical Therapy, Pre-Physician Assistant (Organismal Bio) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/biologicalsciences/ibio_major_prepphsppat/ |
| 12 | Pre-Veterinary Medicine (Organismal Bio) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/prehealthprofessionalcurricula/orgbio_preveterinarymedicine_major/ |
| 13 | Pre-Medicine, Pre-Dental, Pre-Optometry (Physics) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/physics/physics_major_pre-med/ |
| 14 | Pre-Physical Therapy, Pre-Physician Assistant (Physics) | https://bulletin.auburn.edu/undergraduate/collegeofsciencesandmathematics/physics/physics_major_pre-pphsppat/ |

---

#### College of Veterinary Medicine

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public and One Health | https://bulletin.auburn.edu/undergraduate/collegeofveterinarymedicine/public_and_one_health_major/index.html |

---

#### University College

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary University Studies | https://bulletin.auburn.edu/undergraduate/universitycollege/idsc_major/ |

---

### 1.3 Interdisciplinary / cross-college undergraduate programs

Biosystems Engineering 是 College of Agriculture 和 Samuel Ginn College of Engineering 共同管理的跨学院项目。

### 1.4 Minors — complete list

Auburn 提供约 104 个本科辅修（Minor），完整列表见 https://bulletin.auburn.edu/undergraduate/minors/。

### 1.5 Core Curriculum

Auburn 大学要求所有本科生完成核心课程（Core Curriculum）。详见 https://bulletin.auburn.edu/undergraduate/academicpolicies/corecurriculum/。

---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — 按 学院 > 学位级别 分组

Auburn Graduate School 提供 200+ 研究生学位项目选项。以下为 bulletin.auburn.edu 目录中列出的项目。因研究生项目组织通常不按"系"细分，此处按学院 → 学位级别分组。

#### College of Agriculture

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Agricultural Economics | MS, MAg, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/agriculturaleconomicsandruralsociologymsmag_major/ |
| 2 | Animal Sciences | MS, MAg, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/animalsciencesmsmagphd_major/ |
| 3 | Agriscience Education | MS, MEd, EdS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/curriculumandteachingmedmsedsphd_major/agriscience/ |
| 4 | Rural Sociology | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/ruralsociologyms_major |
| 5 | Rural Studies | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/ruralstudies_gcrt/ |
| 6 | Plant Pathology | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/plantpathologymajor/ |
| 7 | Entomology | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/entomologymajor/ |
| 8 | Fisheries | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/fisheriesmajor/ |
| 9 | Horticulture | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/horticulturemajor/ |
| 10 | Poultry Science | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/poultrysciencemajor/ |
| 11 | Crop and Soil Sciences | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/cropandsoilsciencesmajor/ |

#### College of Architecture, Design and Construction

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture — Public Interest Design Option | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/masterarchitectureinterestdesign_major/ |
| 2 | Building Construction | GCert, MBC, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/buildingsciencembc_major/ |

#### Harbert College of Business

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | GCert, MAcc | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/accountancymac_major/ |
| 2 | Business | MBA, MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/businessadministrationmbamsphd_major/ |
| 3 | Business Analytics and AI | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/bual_gcrt/ |
| 4 | Business Analytics and Information Systems | GCert, MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/informationsystems/ |
| 5 | Supply Chain Management | GCert, MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/supplychain/index.html |

#### College of Education

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Administration of Elementary and Secondary Education | MEd, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/administrationofelementaryandsecondaryeducation/ |
| 2 | Administration of Higher Education | MEd, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/administrationofhighereducation/ |
| 3 | Administration of Supervision and Curriculum | MEd, PhD, EdS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/administrationofsupervisionandcurriculum/ |
| 4 | Adult Education | MS, MEd, PhD, EdS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/adulteducation/ |
| 5 | Adult Education and English Language Teaching | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/adulteducationandenglishlang_certificate/ |
| 6 | Business and Marketing Education | MS, MEd, EdS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/curriculumandteachingmedmsedsphd_major/businessandmarketingeducation/ |
| 7 | Career and Technical Education | PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/curriculumandteachingmedmsedsphd_major/careerandtechnicaleducation/ |
| 8 | Special Education, Rehabilitation, and Counseling | GCert, MA, MEd, MS, EdS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/specialeducationrehabilitationandcounseling_major/ |
| 9 | Science Education: General Science | MS, MEd, PhD, EdS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/curriculumandteachingmedmsedsphd_major/scienceeducation/ |
| 10 | Social Science Education: General Social Science | MEd, EdS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/curriculumandteachingmedmsedsphd_major/socialscienceeducation/ |
| 11 | Teaching English as a Second Language (TESL)/TEFL | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/curriculumandteachingmedmsedsphd_major/teachingenglishsecondandforeignlanguage/ |
| 12 | Teaching English for Specific Purposes | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/TeachingEnglishforSpecificPurposes_ms/ |
| 13 | Technology Educator | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/technologyeducator_certificate/ |
| 14 | Transition Specialist | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/specialeducationrehabilitationandcounseling_major/transitionspecialist_cert/ |
| 15 | Workforce Education, Training, and Development | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/educationalfoundationsleadershipandtechnologymedmsedsphd_major/workforceeducationtraininganddevelopment_certificate/index.html |
| 16 | Rehabilitation and Disability Studies | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/rehabilitationmajor/ |

#### Samuel Ginn College of Engineering

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/aerospaceengineeringmaemsphd/ |
| 2 | Artificial Intelligence Engineering | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/aiengineering_ms/index.html |
| 3 | Artificial Intelligence Engineering | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/aiengineering_gcrt/index.html |
| 4 | Automotive Manufacturing Systems | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/industrialandsystemsengineeringmisemisembamsphd_major/automotivemfgsystems_certificate |
| 5 | Biosystems Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/biosystemsengineeringmsphd_major/ |
| 6 | Chemical Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/chemicalengineeringmchemsphd_major/ |
| 7 | Civil Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/civilengr_major/ |
| 8 | Computer Science and Software Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/computersciencesoftwareengineeringmajor/ |
| 9 | Data Science and Engineering | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/datascience_ms/ |
| 10 | Electrical Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/electricalengineeringmaemsphd/ |
| 11 | Industrial and Systems Engineering | MS, MBA, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/industrialandsystemsengineeringmisemisembamsphd_major/ |
| 12 | Materials Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/materialsengineeringmsphd_major/ |
| 13 | Mechanical Engineering | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/mechanicalengineeringmaemsphd/ |
| 14 | Space Systems | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/spacesystems_gcrt/index.html |
| 15 | Structural Analysis in Structural Engineering | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/structuralanalysis_gcrt/ |
| 16 | Structural Design in Structural Engineering | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/structuraldesign_gcrt/ |
| 17 | Tribology (Mechanical Engineering) | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/tribologygraduatecertificate/ |
| 18 | Water Resources Engineering | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/waterresources_gcrt/ |
| 19 | Water Environmental Modeling | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/waterenvironment_gcrt/ |
| 20 | Wireless Engineering | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/wirelessengineering_gcrt |

#### College of Forestry, Wildlife and Environment

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Forestry | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/forestrymajor/ |
| 2 | Wildlife Sciences | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/wildlifesciencesmsphd_major/ |
| 3 | Natural Resources | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/naturalresourcesmajor/ |

#### College of Human Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Human Development and Family Studies | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/humandevelopmentandfamilystudiesmsphd_major/ |
| 2 | Nutrition | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/nutritionmajor/ |
| 3 | Hospitality Management | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/hospitalitymanagementmajor/ |

#### College of Liberal Arts

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication and Journalism | MA, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/communicationandjournalismmajor/ |
| 2 | Communication Disorders | MCD, MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/communicationdisordersmcdms_major/ |
| 3 | Economics | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/economicsmajor/ |
| 4 | English | MA, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/englishmajor/ |
| 5 | History | MA, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/historymajor/ |
| 6 | Foreign Languages and Literatures | MA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/foreignlanguagesmajor/ |
| 7 | Philosophy | MA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/philosophymajor/ |
| 8 | Political Science | MA, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/politicalsciencemajor/ |
| 9 | Psychology | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/psychologymajor/ |
| 10 | Public Administration | MPA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/publicadministrationmajor/ |
| 11 | Sociology | MS, MA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/sociologymsma_major/ |
| 12 | Social Work | MSW | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/socialworkma_major/ |
| 13 | Spanish | MA, MHS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/spanish_major/ |
| 14 | Speech, Language, and Hearing Sciences | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/communicationdisordersmcdms_major/ |
| 15 | Music | MM, DMA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/musicmajor/ |
| 16 | Art | MFA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/artmajor/ |
| 17 | Theatre | MFA | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/theatremajor/ |

#### College of Nursing

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | MSN, DNP | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/nursingmajor/ |

#### Harrison College of Pharmacy

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmaceutical Sciences | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/pharmaceuticalsciencesmajor/ |

#### College of Sciences and Mathematics

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Sciences | GCert, MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/biologicalsciencesmsphd_major/ |
| 2 | Biomedical Sciences | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/biomedicalsciencesmsphd_major/ |
| 3 | Chemistry | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/chemistryandbiochemistrymsphd_major/ |
| 4 | Geology | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/geologymajor/ |
| 5 | Mathematics | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/mathematicsmsphd_major/ |
| 6 | Physics | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/physicsmsphd_major/ |
| 7 | Statistics | MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/statisticsmsmps_major/ |
| 8 | Statistics and Data Science | PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/statisticsdatasci_major/ |

#### College of Veterinary Medicine

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Veterinary Medicine | DVM | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/veterinaryclinicalsciences_major/ |
| 2 | Veterinary Biomedical Sciences | MS, PhD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/veterinarybiomedicalsciencesmajor/ |
| 3 | Veterinary Social Work | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/vetsowo_gcrt/ |

#### Other Interdisciplinary / University-wide

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Bioproducts and Bioprocessing | GCert | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/biop_gcrt/ |
| 2 | Brewing Science and Operations | GCert, MS | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/brewingscienceoperations_ms_gcrt/ |
| 3 | Audiology | AuD | https://bulletin.auburn.edu/thegraduateschool/graduatedegreesoffered/audiologyprogramaud_major/ |

> 注：以上为 bulletin 目录中可确认的主要项目。Auburn 宣称有 200+ 研究生项目选项（含方向/浓度），此处列出的为目录中有独立 URL 的条目。

### 2.2 Graduate admissions model

Auburn 的研究生招生由 Graduate School 统一管理，但各项目自行设置要求。申请通过 Auburn Graduate School 在线系统提交。GRE/考试要求因项目而异——"Test scores are optional for many programs, so visit the program's website for details, dates and deadlines."（来源：graduate.auburn.edu）

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | source_url |
|------|-----|------------|
| Application portal | AU App 或 Common App | https://auburn.edu/admissions/apply/index.php |
| Application fee (domestic) | $50 (non-refundable) | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Application fee (international) | $60 (non-refundable) | https://auburn.edu/admissions/prospective-students/international/index.php |
| EA Round 1 材料截止 | September 15 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| EA Round 2 材料截止 | October 15 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| EA Round 3 材料截止 | November 15 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| EA Round 4 (Final EA) 材料截止 | December 1, 2026 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Regular Decision 材料截止 | February 1, 2027 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Financial Aid Priority Deadline | February 16, 2027 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Enrollment Deposit Deadline | May 1, 2027 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| ACT/SAT Score Received Deadline (scholarship) | January 12, 2027 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Test policy | Test-preferred; 3.6+ GPA 可 test-optional | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Superscoring | SAT 和 ACT 均接受 superscore | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| ACT code | 0011 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| SAT code | 1005 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Recommendation letters | Optional (Academic Letters of Support) | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Personal statement | Optional | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Acceptance rate | 50% | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Freshman Profile ACT (Resident, middle 50%) | 24-31 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Freshman Profile ACT (Non-Resident, middle 50%) | 28-32 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Freshman Profile SAT (Resident, middle 50%) | 1210-1380 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Freshman Profile SAT (Non-Resident, middle 50%) | 1270-1380 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |
| Freshman Profile GPA (middle 50%) | 3.87-4.31 | https://auburn.edu/admissions/prospective-students/freshmen/index.php |

### 3.2 Undergraduate English Proficiency table (International)

| 考试 | 最低要求 | source_url |
|------|----------|------------|
| TOEFL iBT | 79 | https://auburn.edu/admissions/prospective-students/international/index.php |
| TOEFL CBT | 213 | https://auburn.edu/admissions/prospective-students/international/index.php |
| TOEFL PBT | 550 | https://auburn.edu/admissions/prospective-students/international/index.php |
| PTE | 53 | https://auburn.edu/admissions/prospective-students/international/index.php |
| IELTS | 6.5 | https://auburn.edu/admissions/prospective-students/international/index.php |

> 豁免条件：在美国高中毕业、或在美国认证机构完成 English 1100 和 1120（English Composition I/II）并获得 C 或更好成绩。

### 3.3 Graduate — global rules

- **招生模式**：集中管理 + 各项目自行审核。通过 Graduate School 在线系统统一申请。
- **考试要求**：因项目而异。"Test scores are optional for many programs"（来源：graduate.auburn.edu）
- **申请费**：见各项目页面。
- **CGS April 15 签署**：是（Auburn Graduate School 签署 CGS April 15 Resolution）。

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

#### Alabama Resident

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition / Fees | $13,572 | Direct cost |
| Living Expenses (Housing/Food) — On-Campus | $18,424 | Direct cost (if on-campus) |
| Living Expenses (Housing/Food) — Off-Campus | $16,124 | Estimated |
| Living Expenses (Housing/Food) — With Parent | $8,852 | Estimated |
| Books & Supplies | $1,200 | Estimated |
| Personal | $3,088 | Estimated |
| Transportation | $3,232 | Estimated |
| **Total On-Campus** | **$39,516** | |
| **Total Off-Campus** | **$37,216** | |
| **Total With Parent** | **$29,944** | |

#### Non-Resident (包括国际学生)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition / Fees | $37,596 | Direct cost |
| Living Expenses (Housing/Food) — On-Campus | $18,424 | Direct cost (if on-campus) |
| Living Expenses (Housing/Food) — Off-Campus | $16,124 | Estimated |
| Books, Course Materials, Supplies, and Equipment | $1,200 | Estimated |
| Personal | $3,088 | Estimated |
| Transportation | $3,232 | Estimated |
| **Total On-Campus** | **$63,540** | |
| **Total Off-Campus** | **$61,240** | |

> 注：Business, Engineering, Nursing, Interior Design, Hospitality Management, Architecture/Design/Construction 专业有额外 program fees，见 https://auburn.edu/administration/finaid/cost/estimates/index.php

> source_url: https://auburn.edu/administration/finaid/cost/index.php
> source_snippet: "2026-2027 Estimated Cost of Attendance ... Alabama Resident ... Tuition / Fees1 $13,572 ... Non-Resident ... Tuition / Fees1 $37,596"

### 4.2 Undergraduate Financial Aid Policy

- Auburn 是公立大学，need-aware for all applicants（包括州内和州外/国际）
- 提供 Grants, Scholarships, Federal Work-Study, Loans
- FAFSA 是唯一必需的经济援助表格
- 奖学金从 11 月到次年 5 月初发放给第一年学生
- 需要经济援助的国际学生需提交 Financial Affidavit 和 Supporting Bank Letter

> source_url: https://auburn.edu/administration/finaid/index.php

### 4.3 Graduate Cost & Funding Framework

- 研究生学费信息见 https://auburn.edu/academic/international/isss/cost.php
- Graduate Assistantships & Fellowships 可用（来源：bulletin.auburn.edu）
- 申请费因项目而异

---

## SECTION 5 — Evidence Chain Index

### E-U-001 — Freshmen EA Deadlines
```yaml
field: undergraduate.deadlines.ea_rounds
value: {round1: "Sep 15", round2: "Oct 15", round3: "Nov 15", round4_final: "Dec 1, 2026"}
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Decision Rounds ... Round 1 September 15 Mid-October ... Round 2 October 15 Mid-November ... Round 3 November 15 Mid-December ... Early Action Round 4 December 1, 2026 Early-February"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002 — Regular Decision Deadline
```yaml
field: undergraduate.deadlines.rd
value: "February 1, 2027"
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Regular Decision February 1, 2027 Early March"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003 — Application Fee (Domestic)
```yaml
field: undergraduate.application_fee_domestic
value: 50
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Paid the $50 non-refundable application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004 — Application Fee (International)
```yaml
field: undergraduate.application_fee_international
value: 60
source_url: https://auburn.edu/admissions/prospective-students/international/index.php
source_snippet: "Pay the $60 non-refundable application fee (USD)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005 — Test Policy
```yaml
field: undergraduate.test_policy
value: "Test-preferred; applicants with 3.6+ GPA may apply test-optional"
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Auburn University is a test-preferred institution; your scores on standardized tests (such as the SAT or ACT) and your overall GPA are important. Applicants with at least a 3.6 GPA who cannot secure a test will be considered for admission under our test-optional pathway."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006 — Freshman Profile (Resident)
```yaml
field: undergraduate.freshman_profile_resident
value: {ACT: "24-31", SAT: "1210-1380", GPA: "3.87-4.31"}
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Resident ACT 24-31 SAT 1210-1380 GPA 3.87-4.31"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007 — Freshman Profile (Non-Resident)
```yaml
field: undergraduate.freshman_profile_nonresident
value: {ACT: "28-32", SAT: "1270-1380", GPA: "3.87-4.31"}
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Non-Resident ACT 28-32 SAT 1270-1380 GPA 3.87-4.31"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008 — Acceptance Rate
```yaml
field: undergraduate.acceptance_rate
value: "50%"
source_url: https://auburn.edu/admissions/prospective-students/freshmen/index.php
source_snippet: "Overall Acceptance Rate: 50%"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009 — English Proficiency (TOEFL)
```yaml
field: undergraduate.english_proficiency.toefl_ibt
value: 79
source_url: https://auburn.edu/admissions/prospective-students/international/index.php
source_snippet: "TOEFL iBT score of 79 (Internet-Based Test)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010 — English Proficiency (IELTS)
```yaml
field: undergraduate.english_proficiency.ielts
value: 6.5
source_url: https://auburn.edu/admissions/prospective-students/international/index.php
source_snippet: "IELTS band score of 6.5 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011 — English Proficiency (PTE)
```yaml
field: undergraduate.english_proficiency.pte
value: 53
source_url: https://auburn.edu/admissions/prospective-students/international/index.php
source_snippet: "PTE score of 53"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012 — COA Alabama Resident (On-Campus)
```yaml
field: undergraduate.cost.coa_al_resident_oncampus
value: {tuition_fees: 13572, housing_food: 18424, books: 1200, personal: 3088, transportation: 2332, total: 39516}
source_url: https://auburn.edu/administration/finaid/cost/index.php
source_snippet: "Alabama Resident ... Tuition / Fees1 $13,572 ... Total Estimated Cost2 $39,516"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-013 — COA Non-Resident (On-Campus)
```yaml
field: undergraduate.cost.coa_nonresident_oncampus
value: {tuition_fees: 37596, housing_food: 18424, books: 1200, personal: 3088, transportation: 2332, total: 63540}
source_url: https://auburn.edu/administration/finaid/cost/index.php
source_snippet: "Non-Resident ... Tuition / Fees1 $37,596 ... Total Estimated Cost2 $63,540"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-014 — UG Majors Count
```yaml
field: undergraduate.programs.majors_count
value: 175
source_url: https://bulletin.auburn.edu/undergraduate/majors/
source_snippet: "195 catalog entries with degree suffixes (175 unique degree programs after deduplication)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015 — Colleges Count
```yaml
field: institution.colleges_count
value: 13
source_url: https://auburn.edu/about/colleges-departments.php
source_snippet: "College of Agriculture, College of Architecture Design and Construction, Raymond J. Harbert College of Business, College of Education, Samuel Ginn College of Engineering, College of Forestry Wildlife and Environment, College of Human Sciences, College of Liberal Arts, College of Nursing, Harrison College of Pharmacy, College of Sciences and Mathematics, College of Veterinary Medicine, University College"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001 — Graduate Programs Count
```yaml
field: graduate.programs.total
value: "200+"
source_url: https://graduate.auburn.edu/
source_snippet: "Choose from over 200 degree programs at the master's, education specialist, or doctoral level and a variety of graduate minors and graduate certificate programs"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002 — Graduate Test Policy
```yaml
field: graduate.test_policy
value: "Test scores are optional for many programs"
source_url: https://graduate.auburn.edu/
source_snippet: "Test scores are optional for many programs, so visit the program's website for details, dates and deadlines."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-001 — Institution Type
```yaml
field: institution.type
value: "Public, Land-grant, SEC"
source_url: https://auburn.edu/about/
source_snippet: "Auburn University" (public land-grant institution, SEC athletics)
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
auburn-knowledge-base-v2/
├── overview (Section 0)
├── undergraduate-programs (Section 1 — by college)
│   ├── college-of-agriculture
│   ├── college-of-architecture-design-construction
│   ├── harbert-college-of-business
│   ├── college-of-education
│   ├── samuel-ginn-college-of-engineering
│   ├── college-of-forestry-wildlife-environment
│   ├── college-of-human-sciences
│   ├── college-of-liberal-arts
│   ├── college-of-nursing
│   ├── harrison-college-of-pharmacy
│   ├── college-of-sciences-mathematics
│   ├── college-of-veterinary-medicine
│   └── university-college
├── graduate-programs (Section 2 — by college)
├── admissions-requirements (Section 3)
├── costs-financial-aid (Section 4)
└── evidence-index (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "auburn-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|BA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL | 说明 |
|--------|--------|----------|------|
| P0 | 各研究生项目具体 deadline/GRE 要求 | 各项目页面 | Graduate admissions 完全分散 |
| P0 | 各专业 additional program fees 金额 | https://auburn.edu/administration/finaid/cost/estimates/index.php | Business/Engineering/Nursing/Architecture 等有额外费用 |
| P1 | Graduate tuition 均价 | https://www.auburn.edu/academic/international/isss/cost.php | 国际学生费用页面 |
| P1 | 研究生申请费 | 各项目页面 | 因项目而异 |
| P1 | UG minors 完整列表（逐条提取） | https://bulletin.auburn.edu/undergraduate/minors/ | 当前仅统计数量 |
| P2 | Need-blind/need-aware 具体政策 | Financial Aid 页面 | 需确认对国际学生的具体政策 |
| P2 | Scholarships 详情和金额 | https://auburn.edu/administration/finaid/scholarship/ | 奖学金具体条件 |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Auburn University | (其他学校) |
|------|------------------|-----------|
| 公/私立 | Public (Land-grant) | |
| 所在地 | Auburn, AL | |
| UG Tuition (In-State) | $13,572 | |
| UG Tuition (OOS) | $37,596 | |
| UG Total COA (In-State, On-Campus) | $39,516 | |
| UG Total COA (OOS, On-Campus) | $63,540 | |
| Need-Blind (Domestic) | Need-aware for all | |
| Need-Blind (International) | Need-aware | |
| EA Deadline | Dec 1 (final EA) | |
| RD Deadline | Feb 1 | |
| Test Policy | Test-preferred (3.6+ GPA = test-optional) | |
| TOEFL Min | 79 | |
| IELTS Min | 6.5 | |
| Acceptance Rate | 50% | |
| Total UG Programs | ~175 | |
| Total Grad Programs | 200+ | |
| School/College Count | 13 | |
| Application Portal | AU App / Common App | |
| Application Fee (UG Domestic) | $50 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: bulletin.auburn.edu, auburn.edu/admissions, auburn.edu/administration/finaid, graduate.auburn.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
