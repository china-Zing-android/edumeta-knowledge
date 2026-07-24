# University of Florida Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BAE/BSEd) | 158 |
| 本科辅修 (Minor) | 169 |
| 本科证书 (Certificate) | 82 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 179 |
| 研究生证书 (Graduate Certificate) | 200+ |
| **学位项目总计 (UG + Grad)** | **588+** |
| 学院 / 独立系所总数 | 16 |

### 0.2 学院 / 系层级结构

```
University of Florida
├── College of Agricultural and Life Sciences (CALS)          [学院]
│   ├── Agricultural Education and Communication              [系]
│   ├── Agronomy                                              [系]
│   ├── Animal Molecular and Cellular Biology                 [系]
│   ├── Animal Sciences                                       [系]
│   ├── Entomology and Nematology                             [系]
│   ├── Family, Youth, and Community Sciences                 [系]
│   ├── School of Forest, Fisheries, and Geomatics Sciences   [系]
│   ├── Food and Resource Economics                           [系]
│   ├── Food Science and Human Nutrition                      [系]
│   ├── Genetics and Genomics (CALS)                          [系]
│   ├── Horticultural Sciences                                [系]
│   ├── Microbiology and Cell Science                         [系]
│   ├── School of Natural Resources and Environment           [系]
│   ├── Plant Molecular and Cellular Biology (CALS)           [系]
│   ├── Plant Pathology                                       [系]
│   ├── Soil, Water, and Ecosystem Sciences                   [系]
│   └── Wildlife Ecology and Conservation                     [系]
├── College of the Arts                                       [学院]
│   ├── School of Art + Art History                           [系]
│   ├── Digital Worlds Institute                              [系]
│   ├── School of Music                                       [系]
│   └── School of Theatre + Dance                             [系]
├── Warrington College of Business                            [学院]
│   ├── School of Accounting                                  [系]
│   ├── Department of Finance, Insurance and Real Estate      [系]
│   ├── Department of Information Systems and Operations Mgmt [系]
│   ├── Department of Management                              [系]
│   └── Department of Marketing                               [系]
├── College of Dentistry                                      [学院]
│   └── Department of Dental Sciences                         [系]
├── College of Design, Construction and Planning (DCP)        [学院]
│   ├── School of Architecture                                [系]
│   ├── Department of Construction Management                 [系]
│   ├── Department of Interior Design                         [系]
│   ├── Department of Landscape Architecture                  [系]
│   └── Department of Urban and Regional Planning             [系]
├── College of Education                                      [学院]
│   ├── School of Human Development and Organizational Studies[系]
│   ├── School of Special Education, School Psychology and    [系]
│   │   Early Childhood Studies
│   └── School of Teaching and Learning                       [系]
├── Herbert Wertheim College of Engineering                   [学院]
│   ├── Department of Aerospace Engineering                   [系]
│   ├── J. Crayton Pruitt Family Dept of Biomedical Eng       [系]
│   ├── Department of Chemical Engineering                    [系]
│   ├── Department of Civil and Coastal Engineering           [系]
│   ├── Department of Computer and Information Science Eng    [系]
│   ├── Department of Electrical and Computer Engineering     [系]
│   ├── Department of Environmental Engineering Sciences      [系]
│   ├── Department of Industrial and Systems Engineering      [系]
│   ├── Department of Materials Science and Engineering       [系]
│   ├── Department of Mechanical and Aerospace Engineering    [系]
│   └── Department of Nuclear Engineering Sciences            [系]
├── College of Health and Human Performance (HHP)             [学院]
│   ├── Department of Applied Physiology and Kinesiology      [系]
│   ├── Department of Health Education and Behavior           [系]
│   ├── Department of Sport Management                        [系]
│   └── Department of Tourism, Hospitality and Event Mgmt     [系]
├── College of Journalism and Communications                  [学院]
│   ├── Department of Advertising                             [系]
│   ├── Department of Journalism                              [系]
│   └── Department of Public Relations                        [系]
├── Levin College of Law                                      [学院]
│   └── (Professional law programs - JD, LLM, SJD)           [系]
├── College of Liberal Arts and Sciences (CLAS)               [学院]
│   ├── Department of Astronomy                               [系]
│   ├── Department of Biology                                 [系]  ⚠ shared with CALS
│   ├── Department of Chemistry                               [系]
│   ├── Department of Computer and Information Science Eng    [系]  ⚠ shared with Engineering
│   ├── Department of Criminology                             [系]
│   ├── Department of English                                 [系]
│   ├── Department of Geography                               [系]
│   ├── Department of Geology                                 [系]
│   ├── Department of History                                 [系]
│   ├── Department of Mathematics                             [系]
│   ├── Department of Philosophy                              [系]
│   ├── Department of Physics                                 [系]
│   ├── Department of Political Science                       [系]
│   ├── Department of Psychology                              [系]
│   ├── Department of Religion                                [系]
│   ├── Department of Sociology                               [系]
│   ├── Department of Statistics                              [系]
│   ├── Department of Women's Studies                         [系]
│   ├── Department of Zoology                                 [系]
│   └── (20+ language/literature departments)                 [系]
├── College of Medicine                                       [学院]
│   ├── Department of Anatomy and Cell Biology                [系]
│   ├── Department of Biochemistry and Molecular Biology      [系]
│   ├── Department of Molecular Genetics and Microbiology     [系]
│   ├── Department of Neuroscience                            [系]
│   ├── Department of Pathology, Immunology and Lab Medicine  [系]
│   ├── Department of Pharmacology and Therapeutics           [系]
│   └── Department of Physiology                              [系]
├── College of Nursing                                        [学院]
│   └── Department of Nursing                                 [系]
├── College of Pharmacy                                       [学院]
│   ├── Department of Medicinal Chemistry                     [系]
│   ├── Department of Pharmaceutics                           [系]
│   ├── Department of Pharmacotherapy and Translational Res   [系]
│   └── Department of Pharmacodynamics                        [系]
├── College of Public Health and Health Professions (PHHP)    [学院]
│   ├── Department of Clinical and Health Psychology          [系]
│   ├── Department of Communication Sciences and Disorders    [系]
│   ├── Department of Environmental and Global Health         [系]
│   ├── Department of Health Services Research, Mgmt and Policy[系]
│   ├── Department of Occupational Therapy                   [系]
│   ├── Department of Physical Therapy                       [系]
│   └── Department of Rehabilitation Counseling              [系]
├── College of Veterinary Medicine                            [学院]
│   ├── Department of Large Animal Clinical Sciences          [系]
│   ├── Department of Small Animal Clinical Sciences          [系]
│   └── Department of Infectious Diseases and Immunology      [系]
└── Hamilton Center for Classical and Civic Education         [学院]
    └── (Classical liberal arts programs)                     [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~60 |
| BS | Bachelor of Science | 本科 | ~85 |
| BFA | Bachelor of Fine Arts | 本科 | 4 |
| BM | Bachelor of Music | 本科 | 1 |
| BAE | Bachelor of Arts in Education | 本科 | 3 |
| BSEd | Bachelor of Science in Education | 本科 | 2 |
| B.Des | Bachelor of Design | 本科 | 3 |
| Minor | 本科辅修 | 本科 | 169 |
| Certificate | 本科证书 | 本科 | 82 |
| M.A. | Master of Arts | 研究生 | Multiple |
| M.S. | Master of Science | 研究生 | Multiple |
| M.B.A. | Master of Business Administration | 研究生 | Multiple |
| M.Ed. | Master of Education | 研究生 | Multiple |
| M.E. | Master of Engineering | 研究生 | Multiple |
| M.F.A. | Master of Fine Arts | 研究生 | Multiple |
| M.P.H. | Master of Public Health | 研究生 | Multiple |
| M.Arch. | Master of Architecture | 研究生 | 1 |
| M.Acc. | Master of Accounting | 研究生 | 1 |
| M.M. | Master of Music | 研究生 | 1 |
| M.L.A. | Master of Landscape Architecture | 研究生 | 1 |
| M.U.R.P. | Master of Urban and Regional Planning | 研究生 | 1 |
| M.H.A. | Master of Health Administration | 研究生 | 1 |
| M.I.B. | Master of International Business | 研究生 | 1 |
| Ed.S. | Specialist in Education | 研究生 | Multiple |
| Ph.D. | Doctor of Philosophy | 研究生 | Multiple |
| Ed.D. | Doctor of Education | 研究生 | Multiple |
| Au.D. | Doctor of Audiology | 研究生 | 1 |
| D.M.A. | Doctor of Musical Arts | 研究生 | 1 |
| D.P.M. | Doctor of Plant Medicine | 研究生 | 1 |
| D.V.M. | Doctor of Veterinary Medicine | 研究生 | 1 |
| M.D. | Doctor of Medicine | 研究生 | 1 |
| J.D. | Juris Doctor | 研究生 | 1 |
| Graduate Certificate | 研究生证书 | 研究生 | 200+ |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BAE/BSEd | Minor | UG Cert | Grad Programs | Grad Cert | 合计 |
|------------|----|----|-----|----|---------|-------|---------|---------------|-----------|------|
| CLAS | 50 | 7 | 0 | 0 | 0 | 58 | 10 | 36 | 20+ | 131+ |
| CALS | 0 | 24 | 0 | 0 | 0 | 33 | 10 | 27 | 27 | 97+ |
| Engineering | 0 | 16 | 0 | 0 | 0 | 8 | 3 | 19 | 20+ | 66+ |
| Arts | 3 | 7 | 4 | 1 | 0 | 8 | 4 | 11 | 5 | 43 |
| Warrington | 0 | 9 | 0 | 0 | 0 | 3 | 2 | 17 | 2 | 33 |
| HHP | 0 | 7 | 0 | 0 | 0 | 4 | 2 | 5 | 6 | 24 |
| DCP | 0 | 5 | 0 | 0 | 0 | 3 | 1 | 12 | 8 | 29 |
| Education | 2 | 0 | 0 | 0 | 4 | 2 | 2 | 21 | 15+ | 46+ |
| Journalism | 0 | 8 | 0 | 0 | 0 | 3 | 2 | 1 | 8 | 22 |
| PHHP | 0 | 4 | 0 | 0 | 0 | 4 | 3 | 13 | 10+ | 34+ |
| Hamilton | 4 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 7 |
| Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 15+ | 20+ |
| Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 7 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 15+ | 21+ |
| Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| Online | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| **合计** | **59** | **91** | **4** | **1** | **4** | **126** | **37** | **177** | **143+** | **642+** |

---

## SECTION 1 -- Undergraduate education

### 1.1 College/school architecture

UF has 16 degree-granting colleges/schools. The undergraduate programs are distributed across 14 colleges (Law, Medicine, Dentistry, and Veterinary Medicine are graduate/professional only at the UG level). The College of Liberal Arts and Sciences (CLAS) is the largest undergraduate college with 57 majors. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors -- grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts and Sciences (CLAS)

##### Department of African American Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | African American Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/AFA_BA/ |

##### Department of Languages, Literatures, and Cultures
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | African Languages | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/FAF_BA/ |
| 2 | Arabic | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/FAR_BA/ |
| 3 | Chinese | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/CHI_BA/ |
| 4 | Dual Languages | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/DLG_BA/ |
| 5 | French and Francophone Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/FRE_BA/ |
| 6 | German | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/GER_BA/ |
| 7 | Hebrew | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/HBR_BA/ |
| 8 | Hispanic and Latin American Languages, Literatures and Linguistics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/SPN_BA/ |
| 9 | Italian | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/ITA_BA/ |
| 10 | Japanese | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/JPN_BA/ |
| 11 | Portuguese | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/POR_BS/ |
| 12 | Russian | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/RUS_BA/ |
| 13 | Spanish | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/SPN_BS/ |
| 14 | Spanish and Portuguese | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/SPP_BA/ |

##### Department of Anthropology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Anthropology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/APY_BA_BS/ |

##### Department of Astronomy
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Astronomy and Astrophysics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/ATY_BA/ |

##### Department of Biology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Biology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/BLY_BA/ |
| 2 | Biology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/BLY_BA_BS/ |

##### Department of Botany
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Botany | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/BOT_BS/ |

##### Department of Chemistry
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Biochemistry | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/CHY_BS/ |

##### Department of Classical Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Classical Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/CLC_BA/ |

##### Department of Computer and Information Science and Engineering
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Computer Science | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/CSC_BS/ |

##### Department of Criminology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Criminology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/CCJ_BA/ |

##### Department of Economics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Economics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/ECO_BA/ |

##### Department of English
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | English | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/EH_BA/ |

##### Department of Geography
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Geography | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/GEO_BA/ |
| 2 | Geography | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/GEO_BS/ |

##### Department of Geology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Geology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/GLY_BA/ |

##### Department of History
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | History | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/HIS_BA/ |

##### Department of Mathematics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Mathematics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/MAS_BA/ |

##### Department of Philosophy
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Philosophy | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/PHI_BA/ |

##### Department of Physics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Physics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/PHY_BA/ |

##### Department of Political Science
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Political Science | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/POL_BA/ |

##### Department of Psychology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Psychology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/PSY_BA/ |
| 2 | Psychology | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/PSY_BS/ |

##### Department of Religion
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Religion | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/REL_BA/ |

##### Department of Sociology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Sociology | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/SYO_BA/ |

##### Department of Statistics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Data Science | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/STA_BS/ |
| 2 | Statistics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/STA_BA/ |

##### Department of Women's Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Women's Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/WST_BA/ |

##### Department of Zoology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Zoology | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/ZOO_BS/ |

##### Other CLAS Programs
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Jewish Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/JST_BA/ |
| 2 | Linguistics | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/LIN_BA/ |
| 3 | International Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/INS_BA/ |
| 4 | Marine Sciences | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/MSC_BS/ |
| 5 | Meteorology | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/MET_BS/ |
| 6 | Microbiology and Cell Science | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/MCB_BS/ |
| 7 | Sustainability Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/SUS_BA/ |
| 8 | Interdisciplinary Studies | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/IDS_BA/ |
| 9 | Foreign Languages and Literatures | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/FOL_BA/ |

#### College of Agricultural and Life Sciences (CALS)

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Agricultural Education and Communication | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/AEC_BS/ |
| 2 | Agricultural Operations Management | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/AOM_BS/ |
| 3 | Animal Sciences | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/ANS_BS/ |
| 4 | Biology (CALS) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/BLY_BS/ |
| 5 | Botany (CALS) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/BOT_BS/ |
| 6 | Dietetics | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/DTS_BS/ |
| 7 | Entomology and Nematology | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/ENY_BS/ |
| 8 | Family, Youth and Community Sciences | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/FYC_BS/ |
| 9 | Food and Resource Economics | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/FRE_BS/ |
| 10 | Food Science | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/FOS_BS/ |
| 11 | Forest Resources and Conservation | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/FRC_BS/ |
| 12 | Geomatics | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/GEM_BS/ |
| 13 | Environmental Management in Agriculture and Natural Resources | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/EMA_BS/ |
| 14 | Marine Sciences (CALS) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/MSC_BS/ |
| 15 | Microbiology and Cell Science (CALS) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/MCB_BS/ |
| 16 | Natural Resource Conservation | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/NRC_BS/ |
| 17 | Nutritional Sciences | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/NUS_BS/ |
| 18 | Plant Science | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/PLS_BS/ |
| 19 | Soil, Water, and Ecosystem Sciences | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/SWS_BS/ |
| 20 | Wildlife Ecology and Conservation | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGAGL/WEC_BS/ |

#### Herbert Wertheim College of Engineering

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Aerospace Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/ARO_BSAE/ |
| 2 | Biological Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/BSE_BSBE/ |
| 3 | Biomedical Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/BME_BSBM/ |
| 4 | Chemical Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CHE_BSCH/ |
| 5 | Civil Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CEG_BSCE/ |
| 6 | Computer Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CPE_BSCS/ |
| 7 | Computer Science (Engineering) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CSC_BSCS/ |
| 8 | Digital Arts and Sciences (Engineering) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/DAR_BS/ |
| 9 | Electrical Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/ELE_BSEE/ |
| 10 | Environmental Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/ENV_BSEN/ |
| 11 | Industrial and Systems Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/ISE_BSIE/ |
| 12 | Industrialized Construction Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/ICE_BS/ |
| 13 | Materials Science and Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/MSE_BSMS/ |
| 14 | Mechanical Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/MAE_BSME/ |
| 15 | Nuclear Engineering | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/NUC_BSNE/ |
| 16 | Exploring Engineering Studies | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/EGN_BS/ |

#### College of the Arts

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Art | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/VAS_BA/ |
| 2 | Art | BFA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/ART_BFA/ |
| 3 | Art History | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/ARH_BAHA/ |
| 4 | Dance | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/DAN_BA/ |
| 5 | Dance | BFA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/DAN_BFA/ |
| 6 | Digital Arts and Sciences | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/DAR_BADA/ |
| 7 | Graphic Design | BFA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/GRA_BFA/ |
| 8 | Music Business and Entrepreneurship | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/MUS_BSME/ |
| 9 | Music Education | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/MUS_BSED/ |
| 10 | Music | BM | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/MUS_BMUS/ |
| 11 | Theatre | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/THE_BA/ |
| 12 | Theatre Performance | BFA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/TPR_BFA/ |
| 13 | Theatre Production | BFA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/TPR_BFA/ |
| 14 | Digital Arts and Sciences (UF Online) | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGART/DAR_BADA_UFO/ |

#### Warrington College of Business

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Accounting | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/ACT_BSAC/ |
| 2 | Business Administration (General Business) | BSBA | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/BSBA/ |
| 3 | Business Administration (General Studies) | BABA | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/BABA/ |
| 4 | Finance | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/FIN_BS/ |
| 5 | Information Systems | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/ISM_BS/ |
| 6 | Management | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/MAN_BS/ |
| 7 | Marketing | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/MKT_BS/ |
| 8 | Business Administration (UF Online) | BSBA | https://catalog.ufl.edu/UGRD/colleges-schools/UGACT/BSBA_UFO/ |

#### College of Journalism and Communications

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Advertising | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGJRC/ADV_BSAD/ |
| 2 | Advertising (Persuasive Messaging) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGJRC/ADV_BSAD02_UFO/ |
| 3 | Journalism | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGJRC/JOU_BS/ |
| 4 | Journalism (Sports and Media) | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGJRC/JOU_BS02/ |
| 5 | Media Production, Management, and Technology | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGJRC/RTV_BS/ |
| 6 | Public Relations | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGJRC/PUR_BS/ |

#### College of Design, Construction and Planning (DCP)

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Architecture | B.Des | https://catalog.ufl.edu/UGRD/colleges-schools/UGDCP/ARC_BDES/ |
| 2 | Interior Design | B.Des | https://catalog.ufl.edu/UGRD/colleges-schools/UGDCP/IND_BDES/ |
| 3 | Landscape Architecture | B.Des | https://catalog.ufl.edu/UGRD/colleges-schools/UGDCP/LAA_BDES/ |
| 4 | Sustainability and the Built Environment | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGDCP/SUS_BS/ |
| 5 | Urban Sciences and Planning | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGDCP/URP_BS/ |

#### College of Education

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Early Childhood Education (Age 3 - Grade 3) | BAE | https://catalog.ufl.edu/UGRD/colleges-schools/UGEDU/EYC_BAE/ |
| 2 | Education Sciences | BA | https://catalog.ufl.edu/UGRD/colleges-schools/UGEDU/EDS_BA/ |
| 3 | Elementary Education (Grades K-6) | BAE | https://catalog.ufl.edu/UGRD/colleges-schools/UGEDU/ELE_BAE/ |

#### College of Health and Human Performance (HHP)

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Applied Physiology and Kinesiology | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGHHU/APK_BSAP/ |
| 2 | Health Education and Behavior | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGHHU/HEB_BS/ |
| 3 | Sport Management | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGHHU/SPM_BS/ |
| 4 | Tourism, Hospitality and Event Management | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGHHU/THM_BS/ |

#### College of Public Health and Health Professions (PHHP)

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Communication Sciences and Disorders | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGPBH/CSD_BS/ |
| 2 | Health Science | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGPBH/HSC_BS/ |
| 3 | Public Health | BS | https://catalog.ufl.edu/UGRD/colleges-schools/UGPBH/PHC_BS/ |

#### College of Nursing

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing | BSN | https://catalog.ufl.edu/UGRD/colleges-schools/UGNUR/NUR_BSN/ |

#### Hamilton Center for Classical and Civic Education

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | American Government, History, Literature, and Law | BA | https://catalog.ufl.edu/UGRD/colleges-schools/hamilton/AGH_BA/ |
| 2 | Great Books and Ideas | BA | https://catalog.ufl.edu/UGRD/colleges-schools/hamilton/GBI_BA/ |
| 3 | Philosophy, Politics, Economics, and Law | BA | https://catalog.ufl.edu/UGRD/colleges-schools/hamilton/PPE_BA/ |
| 4 | War, Statecraft and Strategy | BA | https://catalog.ufl.edu/UGRD/colleges-schools/hamilton/WSS_BA/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Home College | Cross-listed With | URL |
|---|------|-------------|-------------------|-----|
| 1 | Computer Science | CLAS | Engineering | Both colleges offer BS |
| 2 | Biology | CLAS | CALS | Both colleges offer BA/BS |
| 3 | Botany | CLAS | CALS | Both colleges offer BS |
| 4 | Digital Arts and Sciences | Arts | Engineering | BA in Arts, BS in Engineering |
| 5 | Marine Sciences | CLAS | CALS | Both colleges offer BS |
| 6 | Microbiology and Cell Science | CLAS | CALS | Both colleges offer BS |

### 1.4 Minors -- complete list

UF offers 169 undergraduate minors across all colleges. Key minors include:

**CLAS (58 minors)**: Actuarial Science, African American Studies, African Studies, American Indian and Indigenous Studies, Arabic Language and Literature, Asian Studies, Astronomy, Botany, Chemistry, Classical Studies, Computer Science, Criminology, Dance, Economics, English, Film and Media Studies, French, Geography, Geology, German, Greek Studies, Hebrew, History, Italian, Japanese, Jewish Studies, Latin American Studies, Linguistics, Mathematics, Medieval and Early Modern Studies, Meteorology, Philosophy, Physics, Political Science, Portuguese, Psychology, Religion, Russian, Sociology, Spanish, Statistics, Sustainability Studies, Women's Studies, Zoology, and more.

**CALS (33 minors)**: Agricultural and Natural Resource Communication, Agricultural and Rural Entrepreneurship, Agricultural Curriculum and Development, Agribusiness Management, Animal Genetics, Animal Sciences, Aquaculture, Botany, Crop Management, Dairy Science, Entomology, Environmental Horticulture, Family and Community Sciences, Fermentation Sciences, Food and Resource Economics, Food Science, Forest Resources, Geomatics, Horticultural Science, International Development and Humanitarian Assistance, Microbiology, Natural Resource Conservation, Nutritional Sciences, Plant Pathology, Plant Science, Soil Science, Turfgrass Science, Wildlife Ecology and Conservation, and more.

**Engineering (8 minors)**: Aerospace Engineering, Biomedical Engineering, Civil Engineering, Computer Engineering, Electrical Engineering, Environmental Engineering, Materials Science and Engineering, Mechanical Engineering.

**Arts (8 minors)**: Art, Art History, Dance, Digital Arts and Sciences, Music, Music Business, Theatre, Theatre Production.

**Warrington (3 minors)**: Accounting, Actuarial Science, Business Administration.

**HHP (4 minors)**: Applied Physiology and Kinesiology, Health Education and Behavior, Sport Management, Tourism and Hospitality Management.

**Journalism (3 minors)**: Advertising, Communication Studies, Journalism.

**DCP (3 minors)**: Architecture, Construction Management, Sustainability and the Built Environment.

**PHHP (4 minors)**: Communication Sciences and Disorders, Disability Studies, Health Science, Public Health.

**Hamilton (3 minors)**: American History, Government, Literature, and Law; Classical Studies; Philosophy, Politics, Economics, and Law.

### 1.5 General/Institute-wide requirements

UF requires all undergraduate students to complete the **General Education** program, which includes courses in:
- Composition (6 credits)
- Humanities (6 credits)
- Social and Behavioral Sciences (6 credits)
- Biological Sciences (6 credits)
- Physical Sciences (6 credits)
- Mathematics (6 credits)
- International focus (3 credits)
- Diversity (3 credits)

Total: 36 credits of General Education coursework.

Source: https://catalog.ufl.edu/UGRD/academic-regulations/

---

## SECTION 2 -- Graduate education

### 2.1 Graduate programs -- grouped by 学院 > 系 > 学位级别

UF offers over 250 graduate degree programs across 16 colleges. The Graduate School coordinates admissions and academic standards.

#### College of Liberal Arts and Sciences (36 programs)

Programs include: African American Studies, Anthropology, Astronomy, Biochemistry and Molecular Biology, Botany, Chemistry, Classics, Computer and Information Sciences, Criminology, Economics, English, Entomology, Geography, Geology, History, Linguistics, Mathematics, Microbiology, Molecular Biology, Philosophy, Physics, Political Science, Psychology, Religion, Romance Languages, Sociology, Statistics, Zoology, and more.

Degrees offered: MA, MS, MFA, PhD

#### College of Agricultural and Life Sciences (27 programs)

Programs include: Agricultural and Biological Engineering, Agricultural Education and Communication, Agronomy, Animal Molecular and Cellular Biology, Animal Sciences, Entomology and Nematology, Family Youth and Community Sciences, Fisheries and Aquatic Sciences, Food and Resource Economics, Food Science, Food Science and Human Nutrition, Forest Resources and Conservation, Genetics and Genomics, Horticultural Sciences, Interdisciplinary Ecology, Microbiology and Cell Science, Nutritional Sciences, Plant Breeding, Plant Medicine, Plant Molecular and Cellular Biology, Plant Pathology, Soil Water and Ecosystem Sciences, Wildlife Ecology and Conservation, Youth Development and Family Sciences.

Degrees offered: MS, MFAS, MFRC, MPVM, PhD, DPM

#### Herbert Wertheim College of Engineering (19 programs)

Programs include: Aerospace Engineering, Agricultural and Biological Engineering, Biomedical Engineering, Chemical Engineering, Civil Engineering, Coastal and Oceanographic Engineering, Computer and Information Science and Engineering, Electrical and Computer Engineering, Engineering Education, Environmental Engineering Sciences, Industrial and Systems Engineering, Materials Science and Engineering, Mechanical Engineering, Nuclear Engineering, and more.

Degrees offered: ME, MS, MEng, PhD

#### College of Education (21 programs)

Programs include: Art Education, Computer Science Education, Counselor Education, Curriculum and Teaching, Early Childhood Education, Educational Leadership, Educational Psychology, Educational Technology, Elementary Education, English Education, Higher Education Administration, Mathematics Education, Music Education, Physical Education, Reading and Literacy Education, School Psychology, Science Education, Social Studies Education, Special Education, Student Personnel in Higher Education.

Degrees offered: MA, MAE, MAT, MEd, MMT, EdS, EdD, PhD

#### Warrington College of Business (17 programs)

Programs include: Accounting, Business Administration (MBA, MA, MS), Business Administration PhD (Accounting, Finance, Information Systems, Management, Marketing), Entrepreneurship, Finance, Information Systems and Operations Management, International Business, Management, Marketing, Real Estate.

Degrees offered: MAcc, MAB, MIB, MBA, MS, MSBA, MSE, MSISOM, PhD

#### College of Public Health and Health Professions (13 programs)

Programs include: Audiology, Biostatistics, Clinical and Health Psychology, Clinical Rehabilitation Counseling, Communication Sciences and Disorders, Environmental Health, Epidemiology, Health Services Research, Occupational Therapy, Physical Therapy, Public Health, Rehabilitation Science.

Degrees offered: AuD, DPT, MA, MPH, MS, MHS, PhD

#### College of Design, Construction and Planning (12 programs)

Programs include: Architecture, Construction Management, Design Construction and Planning PhD, Fire and Emergency Sciences, Historic Preservation, Interior Design, Landscape Architecture, Sustainable Development, Urban and Regional Planning.

Degrees offered: MArch, MCM, MDes, MHDP, MHP, MID, MLA, MS, MSDP, MURP, PhD

#### College of the Arts (11 programs)

Programs include: Art Education, Art History, Arts in Medicine, Dance, Design and Visual Communications, Digital Arts and Sciences, Music, Music Education, Theatre.

Degrees offered: MA, MFA, MM, PhD, DMA

#### College of Medicine (6 programs)

Programs include: Anatomy and Cell Education, Biomedical Informatics, Biomedical Neuroscience, Clinical and Translational Science, Medical Physiology, Pharmacology and Therapeutics.

Degrees offered: MS, PhD

#### College of Pharmacy (5 programs)

Programs include: Pharmaceutical Chemistry, Pharmaceutics, Pharmacodynamics, Pharmacotherapy and Translational Research, Pharmaceutical Outcomes and Policy.

Degrees offered: MS, MSP, PhD

#### College of Health and Human Performance (5 programs)

Programs include: Applied Physiology and Kinesiology, Health Education and Behavior, Sport Management, Tourism Hospitality and Event Management.

Degrees offered: MS, PhD

#### College of Veterinary Medicine (2 programs)

Programs include: Large Animal Clinical Sciences, Small Animal Clinical Sciences, Veterinary Medical Sciences.

Degrees offered: DVM, MPVM, MS, PhD

#### College of Dentistry (1 program)

Dental Sciences.

Degrees offered: MS, PhD

#### College of Nursing (1 program)

Nursing.

Degrees offered: DNP, PhD

#### College of Journalism and Communications (1 program)

Mass Communication.

Degrees offered: MAMC, PhD

### 2.2 At least one program's full deep-dive

**Computer and Information Science and Engineering (CISE)**

- Department: Department of Computer and Information Science and Engineering
- College: Herbert Wertheim College of Engineering
- Degrees offered: MS, PhD
- GRE: Required for most programs
- TOEFL minimum: 80 iBT (Graduate School minimum)
- Application portal: https://www.applyweb.com/uflgrad/index.ftl
- Application fee: $30 (domestic), $30 (international)
- Contact: cise.ufl.edu

### 2.3 Graduate admissions model

UF graduate admissions is **decentralized**. Each college/department sets its own requirements, deadlines, and review processes. All applicants apply through the centralized UF Graduate School application portal (CollegeNET), but the department makes the admission decision.

- Application portal: https://www.applyweb.com/uflgrad/index.ftl
- Graduate School: https://grad.ufl.edu/
- Each program has its own deadline (most fall deadlines are December-January)
- GRE/GMAT requirements vary by program
- English proficiency: TOEFL 80 iBT / IELTS 6.0 (minimum, programs may require higher)

---

## SECTION 3 -- Application requirements & deadlines

### 3.1 Undergraduate -- core data table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | Common App, Coalition App, or UF Direct | admissions.ufl.edu |
| Early Decision (ED) deadline | October 15 | admissions.ufl.edu/apply/freshman/deadlines |
| Early Action (EA) deadline | November 1 | admissions.ufl.edu/apply/freshman/deadlines |
| Regular Decision (RD) deadline | January 15 | admissions.ufl.edu/apply/freshman/deadlines |
| ED notification | December 11 | admissions.ufl.edu/apply/freshman/deadlines |
| EA notification | January 22 | admissions.ufl.edu/apply/freshman/deadlines |
| RD notification | March 19 | admissions.ufl.edu/apply/freshman/deadlines |
| Enrollment confirmation | May 1 | admissions.ufl.edu/apply/freshman/deadlines |
| Application fee | $30 | admissions.ufl.edu |
| SAT/ACT policy | **REQUIRED** (NOT test-optional) | admissions.ufl.edu/apply/freshman/requirements |
| CLT accepted | Yes (Classic Learning Test) | admissions.ufl.edu/apply/freshman/requirements |
| Superscoring | Yes (SAT and ACT) | admissions.ufl.edu/apply/freshman/requirements |
| SAT code | 5812 | admissions.ufl.edu |
| ACT code | 0758 | admissions.ufl.edu |
| Recommendation letters | Not required | admissions.ufl.edu |
| Interview | Not offered | admissions.ufl.edu |
| High school requirements | 16 academic units: 4 English, 4 Math, 3 Science, 3 Social Studies, 2 Foreign Language | admissions.ufl.edu/apply/freshman/requirements |
| GPA requirement | Minimum C average in academic core | admissions.ufl.edu/apply/freshman/requirements |

**Important verification**: UF is **NOT test-optional**. SAT, ACT, or Classic Learning Test (CLT) scores are REQUIRED for all freshman applicants. This is mandated by Florida Board of Governors Regulation 6.008.

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|--------------|-------------------|-------|
| TOEFL iBT | 80 | N/A | Required for all international applicants |
| TOEFL Paper | 550 | N/A | Accepted |
| IELTS Academic | 6.0 | N/A | Required for all international applicants |
| Duolingo English Test | Not specified | N/A | Check with admissions |
| PTE Academic | Not specified | N/A | Check with admissions |

- All international applicants must provide English proficiency test scores
- Exemptions: Students who completed 3+ years at a US-accredited high school
- TOEFL school code: 5812
- IELTS: Send to "The University of Florida, 201 Criser Hall, Gainesville, FL 32611"

Source: https://admissions.ufl.edu/apply/freshman/international

### 3.3 Graduate -- global rules

- **Decentralized admissions**: Each department sets its own requirements
- **Application portal**: CollegeNET (https://www.applyweb.com/uflgrad/index.ftl)
- **Application fee**: $30 (domestic and international)
- **GRE**: Required by most programs (some programs waive for applicants with prior graduate degrees)
- **GMAT**: Required for MBA applicants
- **English proficiency (Graduate School minimum)**: TOEFL iBT 80 / TOEFL Paper 550 / IELTS 6.0
- **Exemptions**: Applicants with a graduate degree from a US institution may be exempt from English proficiency requirements
- **Most PhD programs**: Fully funded with stipends
- **CGS April 15**: UF is a signatory

Source: https://gradcatalog.ufl.edu/graduate/admission/

---

## SECTION 4 -- Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense Item | In-State (On/Off Campus) | Out-of-State (On/Off Campus) | In-State (Living w/ Parents) |
|-------------|-------------------------|------------------------------|------------------------------|
| Tuition / Fees | $6,380 | $30,900 | $6,380 |
| Books, Course Materials, Supplies | $1,220 | $1,220 | $1,220 |
| Transportation | $1,700 | $1,700 | $1,700 |
| Living Expenses | $14,190 | $14,190 | $4,600 |
| Miscellaneous Personal Expenses | $2,224 | $2,224 | $2,224 |
| Federal Student Loan Fees | $56 | $56 | $56 |
| **Total Budget** | **$25,770** | **$50,290** | **$16,180** |

*Tuition/fee figures are projected estimates for 2026-27 for incoming freshmen (based on 30 credit hours total for fall and spring semesters).*

Source: https://www.sfa.ufl.edu/cost/

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all applicants** (domestic and international)
- **Merit scholarships available** through the Office of Admissions
- **Bright Futures Scholarship**: Florida state scholarship for qualifying FL high school graduates
- **Benacquisto Scholarship**: For National Merit/Finalists
- **Gator Nation Scholarship**: For out-of-state students
- **Florida Prepaid**: Accepted for tuition
- **Need-based aid**: FAFSA required for federal and state aid
- **CSS Profile**: Not required (UF uses FAFSA only)

Source: https://admissions.ufl.edu/cost-and-aid/scholarships

### 4.3 Graduate cost & funding framework

| Expense Item | In-State (On Campus) | In-State (Off Campus) | Out-of-State (Off Campus) |
|-------------|---------------------|----------------------|---------------------------|
| Tuition / Fees | $12,740 | $12,740 | $31,872 |
| Books, Course Materials | $1,235 | $1,235 | $1,235 |
| Transportation | $1,660 | $1,660 | $1,660 |
| Living Expenses | $13,395 | $17,755 | $17,755 |
| Miscellaneous Personal | $2,603 | $2,603 | $2,603 |
| Federal Student Loan Fees | $87 | $87 | $87 |
| **Total Budget** | **$31,720** | **$36,080** | **$55,212** |

*Graduate tuition/fee figures are projected estimates for 2025-26.*

**Funding framework**:
- Most PhD programs offer full funding (tuition waiver + stipend + health insurance)
- RA/TA positions available across departments
- Fellowships: University Fellowships, McKnight Fellowships, Grinter Fellowships
- Master's programs: Generally self-funded, some assistantships available
- Application fee: $30 (no fee waivers from Office of Admissions)

Source: https://www.sfa.ufl.edu/cost/graduate-costs/

---

## SECTION 5 -- Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.ED
  value: "October 15"
  source_url: "https://admissions.ufl.edu/apply/freshman/deadlines"
  source_snippet: "Application Deadline | Early Decision (Binding) | October 15"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: "https://admissions.ufl.edu/apply/freshman/deadlines"
  source_snippet: "Application Deadline | Early Action (Non-Binding) | November 1"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.RD
  value: "January 15"
  source_url: "https://admissions.ufl.edu/apply/freshman/deadlines"
  source_snippet: "Application Deadline | Regular Decision (Non-Binding) | January 15"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.test_policy
  value: "REQUIRED (SAT/ACT/CLT)"
  source_url: "https://admissions.ufl.edu/apply/freshman/requirements"
  source_snippet: "All applicants must submit test scores from the SAT, ACT and/or CLT."
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.cost.tuition_in_state
  value: "$6,380"
  source_url: "https://www.sfa.ufl.edu/cost/"
  source_snippet: "Tuition / Fees | In-state Undergrad On/Off Campus | $6,380"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.cost.tuition_out_of_state
  value: "$30,900"
  source_url: "https://www.sfa.ufl.edu/cost/"
  source_snippet: "Tuition / Fees | Out-of-state Undergrad On/Off Campus | $30,900"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_in_state
  value: "$25,770"
  source_url: "https://www.sfa.ufl.edu/cost/"
  source_snippet: "Total Budget | In-state Undergrad On/Off Campus | $25,770"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.total_out_of_state
  value: "$50,290"
  source_url: "https://www.sfa.ufl.edu/cost/"
  source_snippet: "Total Budget | Out-of-state Undergrad On/Off Campus | $50,290"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.english_proficiency.toefl
  value: "80 iBT / 550 Paper"
  source_url: "https://gradcatalog.ufl.edu/graduate/admission/"
  source_snippet: "TOEFL: 550 paper, or 80 Internet & Home Edition"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_proficiency.ielts
  value: "6.0"
  source_url: "https://gradcatalog.ufl.edu/graduate/admission/"
  source_snippet: "IELTS: 6"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-G-001:
  field: graduate.cost.tuition_in_state
  value: "$12,740"
  source_url: "https://www.sfa.ufl.edu/cost/graduate-costs/"
  source_snippet: "Tuition / Fees | In-state Graduate On Campus | $12,740"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.cost.tuition_out_of_state
  value: "$31,872"
  source_url: "https://www.sfa.ufl.edu/cost/graduate-costs/"
  source_snippet: "Tuition / Fees | Out-of-state Graduate Off Campus | $31,872"
  capture_date: "2026-07-05"
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.application_fee
  value: "$30"
  source_url: "https://admissions.ufl.edu/apply/graduate"
  source_snippet: "Complete the application... pay the non-refundable application fee"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-G-004:
  field: graduate.english_proficiency.toefl
  value: "80 iBT"
  source_url: "https://gradcatalog.ufl.edu/graduate/admission/"
  source_snippet: "TOEFL: 550 paper, or 80 Internet & Home Edition"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-G-005:
  field: graduate.english_proficiency.ielts
  value: "6.0"
  source_url: "https://gradcatalog.ufl.edu/graduate/admission/"
  source_snippet: "IELTS: 6"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-G-006:
  field: graduate.program_count
  value: "250+"
  source_url: "https://admissions.ufl.edu/apply/graduate"
  source_snippet: "more than 250 graduate majors"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-S-001:
  field: institution.need_blind
  value: false
  source_url: "https://admissions.ufl.edu"
  source_snippet: "Need-aware for all applicants"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-S-002:
  field: institution.type
  value: "Public"
  source_url: "https://www.ufl.edu"
  source_snippet: "University of Florida - Public Research University"
  capture_date: "2026-07-05"
  evidence_type: official_webpage

E-S-003:
  field: institution.location
  value: "Gainesville, FL"
  source_url: "https://www.ufl.edu"
  source_snippet: "Gainesville, FL 32611"
  capture_date: "2026-07-05"
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora import manifest

### Collection structure

```
uf-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-clas.md                       (CLAS majors + minors)
├── 02-ug-cals.md                       (CALS majors + minors)
├── 03-ug-engineering.md                (Engineering majors + minors)
├── 04-ug-arts.md                       (Arts majors + minors)
├── 05-ug-warrington.md                 (Business majors + minors)
├── 06-ug-journalism.md                 (Journalism majors + minors)
├── 07-ug-dcp.md                        (DCP majors + minors)
├── 08-ug-education.md                  (Education majors + minors)
├── 09-ug-hhp.md                        (HHP majors + minors)
├── 10-ug-phhp.md                       (PHHP majors + minors)
├── 11-ug-hamilton.md                   (Hamilton majors + minors)
├── 12-ug-nursing.md                    (Nursing major)
├── 13-ug-certificates.md               (All UG certificates)
├── 14-grad-clas.md                     (CLAS graduate programs)
├── 15-grad-cals.md                     (CALS graduate programs)
├── 16-grad-engineering.md              (Engineering graduate programs)
├── 17-grad-education.md                (Education graduate programs)
├── 18-grad-warrington.md               (Business graduate programs)
├── 19-grad-phhp.md                     (PHHP graduate programs)
├── 20-grad-dcp.md                      (DCP graduate programs)
├── 21-grad-arts.md                     (Arts graduate programs)
├── 22-grad-medicine.md                 (Medicine graduate programs)
├── 23-grad-pharmacy.md                 (Pharmacy graduate programs)
├── 24-grad-hhp.md                      (HHP graduate programs)
├── 25-grad-vetmed.md                   (Vet Med graduate programs)
├── 26-grad-other.md                    (Dentistry, Nursing, Journalism)
├── 27-deadlines-requirements.md        (Section 3)
├── 28-costs-financial-aid.md           (Section 4)
├── 29-evidence-chain.md                (Section 5)
└── 30-grad-certificates.md             (Graduate certificates)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uf-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BFA|BM|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "<URL>"
  capture_date: "2026-07-05"
  version: v2.0
  change_status: baseline
  last_verified: "2026-07-05"
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Department websites |
| P0 | Per-program application deadlines (grad) | Department websites |
| P0 | Complete list of graduate certificates (200+) | gradcatalog.ufl.edu/graduate/certificates/ |
| P1 | Per-program TOEFL/IELTS recommended scores | Department websites |
| P1 | Scholarship amounts and criteria | admissions.ufl.edu/cost-and-aid/scholarships |
| P1 | Financial aid policy details (need-aware specifics) | sfa.ufl.edu |
| P2 | Transfer admission requirements | admissions.ufl.edu/apply/transfer |
| P2 | Honors Program details | honors.ufl.edu |
| P2 | PaCE program details | admissions.ufl.edu/apply/freshman/pace |

---

## SECTION 7 -- Cross-school comparison framework

| Dimension | UF Value |
|-----------|----------|
| Institution type | Public |
| Location | Gainesville, FL |
| Total UG programs (Rule 1) | 409 (158 majors + 169 minors + 82 certificates) |
| Total grad programs (Rule 1) | 179 departments + 200+ certificates |
| School/college count (Rule 2) | 16 |
| EA deadline | November 1 |
| ED deadline | October 15 |
| RD deadline | January 15 |
| SAT/ACT required? | **YES** (required, not test-optional) |
| CLT accepted? | Yes |
| Superscoring? | Yes |
| Application fee (UG) | $30 |
| TOEFL minimum | 80 iBT |
| IELTS minimum | 6.0 |
| In-state tuition/yr | $6,380 |
| OOS tuition/yr | $30,900 |
| In-state total COA | $25,770 |
| OOS total COA | $50,290 |
| Need-blind? | No (need-aware for all) |
| Grad application fee | $30 |
| Grad TOEFL minimum | 80 iBT |
| Grad IELTS minimum | 6.0 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.ufl.edu, sfa.ufl.edu, catalog.ufl.edu, gradcatalog.ufl.edu, grad.ufl.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
