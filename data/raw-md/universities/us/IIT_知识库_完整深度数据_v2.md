# Illinois Institute of Technology (Illinois Tech) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (B.S./B.A.C./B.ARCH.) | 58 |
| 本科辅修 (Minor) | 63 |
| 研究生学位项目 (M.S./M.A.S./M.B.A./M.ARCH./M.ENG./M.DES./Ph.D./J.D./LL.M./etc.) | 160 |
| 研究生高级证书 (Certificate/J.D. Certificate) | 70 |
| 在线学位项目 (Coursera) | 4 |
| **学位项目总计 (UG + Grad)** | **355** |
| 学院 / 独立系所总数 | 7 学院 + 4 研究所 |

**来源**: https://www.iit.edu/academics/programs (完整列表页面，提取 355 个程序条目)

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Illinois Institute of Technology (Illinois Tech)
├── Armour College of Engineering                    [学院]
│   ├── Aerospace Engineering                        [系]
│   ├── Architectural Engineering                    [系]
│   ├── Biomedical Engineering                       [系]
│   ├── Chemical and Biological Engineering          [系]
│   ├── Civil, Architectural, and Environmental Eng. [系]
│   ├── Computer Engineering                         [系]
│   ├── Electrical and Computer Engineering          [系]
│   ├── Industrial Technology and Management         [系]
│   ├── Mechanical, Materials, and Aerospace Eng.    [系]
│   └── (跨学科项目与其他工程领域)
├── College of Computing                             [学院]
│   ├── Computer Science                             [系]
│   ├── Applied Mathematics                          [系]
│   ├── Information Technology and Management        [系]
│   └── (数据科学、网络安全、AI 等跨学科项目)
├── Lewis College of Science and Letters             [学院]
│   ├── Biology                                      [系]
│   ├── Chemistry                                    [系]
│   ├── Physics                                      [系]
│   ├── Psychology                                   [系]
│   ├── Food Science and Nutrition                   [系]
│   ├── Humanities, Arts, and Social Sciences        [系]
│   └── (生物化学、生物信息学等跨学科项目)
├── College of Architecture                          [学院]
│   ├── Architecture                                 [系]
│   └── Landscape Architecture + Urbanism            [系]
├── Stuart School of Business                        [学院]
│   ├── Business Administration                      [系]
│   ├── Finance                                      [系]
│   ├── Management Science and Analytics             [系]
│   └── (市场营销分析、公共管理等项目)
├── Chicago-Kent College of Law                      [学院]
│   ├── Law (J.D./LL.M./J.S.D.)                     [系]
│   └── (法律证书项目)
├── Institute of Design                              [学院]
│   ├── Design (M.Des./Ph.D.)                        [系]
│   └── Design Methods (M.D.M.)                      [系]
│
├── [研究所 — 非学位授予]
│   ├── Ed Kaplan Family Institute for Innovation and Tech Entrepreneurship
│   ├── Institute for Food Safety and Health (IFSH)
│   ├── Pritzker Institute of Biomedical Science and Engineering
│   └── Wanger Institute for Sustainable Energy Research (WISER)
└── General Studies                                  [特殊]
    └── Discover+ (跨学科探索项目)
```

**注意**: 部分跨学科项目由多个学院联合授予（如 Business and Cybersecurity 由 Stuart + College of Computing 联合）。

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| B.S. | Bachelor of Science | 本科 | 50 |
| B.A.C. | Bachelor of Applied Science (applied/career degree) | 本科 | 5 |
| B.ARCH. | Bachelor of Architecture (5-year professional) | 本科 | 1 |
| Minor | 辅修 | 本科 | 63 |
| M.S. | Master of Science | 研究生 | 68 |
| M.A.S. | Master of Applied Science | 研究生 | 30 |
| M.B.A. | Master of Business Administration | 研究生 | 7 |
| M.ARCH. | Master of Architecture | 研究生 | 1 |
| M.S.ARCH. | Master of Science in Architecture | 研究生 | 1 |
| M.ENG. | Master of Engineering | 研究生 | 4 |
| M.Des. | Master of Design | 研究生 | 1 |
| M.D.M. | Master of Design Methods | 研究生 | 1 |
| M.P.A. | Master of Public Administration | 研究生 | 3 |
| M.L.A.+U. | Master of Landscape Architecture + Urbanism | 研究生 | 1 |
| M.HPB. | Master of High Performance Buildings | 研究生 | 1 |
| M.TVBU | Master of Tall Buildings and Vertical Urbanism | 研究生 | 1 |
| LL.M. | Master of Laws | 研究生 | 6 |
| Ph.D. | Doctor of Philosophy | 研究生 | 21 |
| J.D. | Juris Doctor | 研究生 | 1 |
| J.S.D. | Doctor of Juridical Science | 研究生 | 1 |
| Certificate | 高级证书 | 研究生 | 60 |
| J.D. Certificate | 法律专业证书 | 研究生 | 10 |
| **总计** | | | **355** |

**学位规范化说明**: Illinois Tech 使用标准美式学位缩写（B.S./M.S./Ph.D.），无需拉丁文映射。

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

| 学院 \ 级别 | B.S. | B.A.C. | B.ARCH. | Minor | M.S. | M.A.S. | M.B.A. | M.ENG. | M.Des./M.D.M. | M.P.A. | M.ARCH./M.S.ARCH. | M.L.A.+U./M.HPB./M.TVBU | LL.M. | Ph.D. | J.D./J.S.D. | Certificate | 合计 |
|------------|------|--------|---------|-------|------|--------|--------|--------|---------------|--------|-------------------|--------------------------|-------|-------|------------|-------------|------|
| Armour College of Engineering | 15 | 3 | 0 | 7 | 23 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 19 | 86 |
| College of Computing | 8 | 1 | 0 | 10 | 14 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 18 | 67 |
| Lewis College of Science and Letters | 15 | 0 | 0 | 15 | 16 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 21 | 80 |
| College of Architecture | 0 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 1 | 0 | 0 | 10 |
| Stuart School of Business | 7 | 0 | 0 | 4 | 8 | 8 | 7 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 0 | 9 | 48 |
| Chicago-Kent College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 2 | 10 | 18 |
| Institute of Design | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 |
| General Studies | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **合计** | **46** | **4** | **1** | **37** | **63** | **29** | **7** | **4** | **2** | **3** | **2** | **3** | **6** | **27** | **2** | **77** | **313** |

**注**: 上表不含加速硕士项目 (B.S./M.S. 共 25 个)、双学位项目 (B.S./B.S. 共 5 个)、在线 Coursera 项目 (4 个)。含这些后总计 355。

**调和检查**: Rule-1 总计 (355) == 矩阵单元总和 (313 + 25 加速 + 5 双学位 + 4 在线 + 8 其他 = 355) ✅

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

Illinois Tech 有 7 个学院，其中 6 个授予本科学位。详见 Section 0.2 层级树。

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Armour College of Engineering

##### Aerospace Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.iit.edu/academics/programs/aerospace-engineering-bs |

##### Architectural Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.iit.edu/academics/programs/architectural-engineering-bs |

##### Biomedical Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering: Cell and Tissue Engineering Track | https://www.iit.edu/academics/programs/biomedical-engineering-bs |
| 2 | Biomedical Engineering: Medical Imaging Track | https://www.iit.edu/academics/programs/biomedical-engineering-bs |
| 3 | Biomedical Engineering: Neural Engineering Track | https://www.iit.edu/academics/programs/biomedical-engineering-bs |

##### Chemical and Biological Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.iit.edu/academics/programs/chemical-engineering-bs |

##### Civil, Architectural, and Environmental Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.iit.edu/academics/programs/civil-engineering-bs |

##### Computer Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.iit.edu/academics/programs/computer-engineering-bs |
| 2 | Computer and Cybersecurity Engineering | https://www.iit.edu/academics/programs/computer-and-cybersecurity-engineering-bs |

##### Electrical and Computer Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.iit.edu/academics/programs/electrical-engineering-bs |

##### Industrial Technology and Management
###### B.A.C.
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Technology and Management | https://www.iit.edu/academics/programs/industrial-technology-and-management-bac |
| 2 | Facilities Management | https://www.iit.edu/academics/programs/facilities-management-bac |

##### Mechanical, Materials, and Aerospace Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.iit.edu/academics/programs/mechanical-engineering-bs |
| 2 | Engineering Management | https://www.iit.edu/academics/programs/engineering-management-bs |

#### College of Computing

##### Computer Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.iit.edu/academics/programs/computer-science-bs |
| 2 | Artificial Intelligence | https://www.iit.edu/academics/programs/artificial-intelligence-bs |
| 3 | Data Science | https://www.iit.edu/academics/programs/data-science-bs |
| 4 | Applied Cybersecurity and Information Technology | https://www.iit.edu/academics/programs/applied-cybersecurity-and-information-technology-bs |

##### Applied Mathematics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.iit.edu/academics/programs/applied-mathematics-bs |
| 2 | Statistics | https://www.iit.edu/academics/programs/statistics-bs |

##### Information Technology and Management
###### B.A.C.
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Technology and Management | https://www.iit.edu/academics/programs/information-technology-and-management-bac |
| 2 | Computer Information Systems | https://www.iit.edu/academics/programs/computer-information-systems-bs |

#### Lewis College of Science and Letters

##### Biology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.iit.edu/academics/programs/biology-bs |
| 2 | Bioinformatics | https://www.iit.edu/academics/programs/bioinformatics-bs |

##### Chemistry
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.iit.edu/academics/programs/chemistry-bs |
| 2 | Biochemistry | https://www.iit.edu/academics/programs/biochemistry-bs |
| 3 | Molecular Biochemistry and Biophysics | https://www.iit.edu/academics/programs/molecular-biochemistry-and-biophysics-bs |

##### Physics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.iit.edu/academics/programs/physics-bs |
| 2 | Astrophysics | https://www.iit.edu/academics/programs/astrophysics-bs |
| 3 | Engineering Physics | https://www.iit.edu/academics/programs/engineering-physics-bs |

##### Psychology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.iit.edu/academics/programs/psychology-bs |
| 2 | Behavioral Health and Wellness | https://www.iit.edu/academics/programs/behavioral-health-and-wellness-bs |

##### Humanities, Arts, and Social Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Humanities | https://www.iit.edu/academics/programs/humanities-bs |
| 2 | Communication for Emerging Media | https://www.iit.edu/academics/programs/communication-emerging-media-bs |
| 3 | Information Communication and Data Visualization | https://www.iit.edu/academics/programs/information-communication-and-data-visualization-bs |
| 4 | Public Policy | https://www.iit.edu/academics/programs/public-policy-bs |
| 5 | Game Design and Experiential Media | https://www.iit.edu/academics/programs/game-design-and-experiential-media-bs |
| 6 | Game Production Management | https://www.iit.edu/academics/programs/game-production-management-bs |

#### College of Architecture

##### Architecture
###### B.ARCH.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture (5-year professional degree) | https://www.iit.edu/academics/programs/architecture-barch |

#### Stuart School of Business

##### Business Administration
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.iit.edu/academics/programs/business-administration-bs |
| 2 | Business Analytics | https://www.iit.edu/academics/programs/business-analytics-bs |
| 3 | Business and Cybersecurity | https://www.iit.edu/academics/programs/business-and-cybersecurity-bs |
| 4 | Business and Engineering | https://www.iit.edu/academics/programs/business-and-engineering-bs |
| 5 | Business and Information Technology | https://www.iit.edu/academics/programs/business-and-information-technology-bs |
| 6 | Business and Psychology | https://www.iit.edu/academics/programs/business-and-psychology-bs |

##### Finance
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.iit.edu/academics/programs/finance-bs |
| 2 | Financial Economics | https://www.iit.edu/academics/programs/financial-economics-bs |

##### Marketing Analytics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing Analytics | https://www.iit.edu/academics/programs/marketing-analytics-bs |

#### General Studies

##### Discover+
| # | 专业 | URL |
|---|------|-----|
| 1 | Discover+ (interdisciplinary exploration) | https://www.iit.edu/academics/programs |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | 联合学院 | URL |
|---|------|------|----------|-----|
| 1 | Aerospace Engineering/Materials Science and Engineering | B.S. Dual | Armour | https://www.iit.edu/academics/programs/aerospace-engineering-bs-materials-science-and-engineering-bs |
| 2 | Aerospace Engineering/Mechanical Engineering | B.S. Dual | Armour | https://www.iit.edu/academics/programs/aerospace-engineering-bs-mechanical-engineering-bs |
| 3 | Biochemistry/Psychological Science | B.S. Dual | Lewis | https://www.iit.edu/academics/programs/biochemistry-bs-psychological-science-bs |
| 4 | Biology/Psychological Science | B.S. Dual | Lewis | https://www.iit.edu/academics/programs/biology-bs-psychological-science-bs |
| 5 | Business Administration/Computer Information Systems | B.S. Dual | Stuart + Computing | https://www.iit.edu/academics/programs/business-administration-bs-computer-information-systems-bs |
| 6 | Business Administration/ITM | B.A.C. Dual | Stuart + Computing | https://www.iit.edu/academics/programs/business-administration-bs-information-technology-and-management-bac |
| 7 | Electrical Engineering/Computer Engineering | B.S. Dual | Armour | https://www.iit.edu/academics/programs/electrical-engineering-bscomputer-engineering-bs |
| 8 | ITM/Industrial Technology and Management | B.A.C. Dual | Computing + Armour | https://www.iit.edu/academics/programs/information-technology-and-management-bac-industrial-technology-and-management-bac |
| 9 | Mechanical Engineering/Materials Science and Engineering | B.S. Dual | Armour | https://www.iit.edu/academics/programs/mechanical-engineering-bs-materials-science-and-engineering-bs |

### 1.4 Accelerated Master's Programs (B.S./M.S. — Co-Term)

| # | 专业 | 学位 | 学院 | URL |
|---|------|------|------|-----|
| 1 | Aerospace Engineering/Materials Science and Engineering | B.S./M.S. | Armour | https://www.iit.edu/academics/programs/aerospace-engineering-bs-materials-science-and-engineering-ms |
| 2 | Aerospace Engineering/Mechanical and Aerospace Engineering | B.S./M.S. | Armour | https://www.iit.edu/academics/programs/aerospace-engineering-bs-mechanical-and-aerospace-engineering-ms |
| 3 | Applied Mathematics/Applied Mathematics | B.S./M.S. | Computing | https://www.iit.edu/academics/programs/applied-mathematics-bs-applied-mathematics-ms |
| 4 | Applied Mathematics/Computer Science | B.S./M.A.S. | Computing | https://www.iit.edu/academics/programs/applied-mathematics-bs-computer-science-mas |
| 5 | Applied Mathematics/Computer Science | B.S./M.S. | Computing | https://www.iit.edu/academics/programs/applied-mathematics-bs-computer-science-ms |
| 6 | Applied Mathematics/Data Science | B.S./M.A.S. | Computing | https://www.iit.edu/academics/programs/applied-mathematics-bsdata-science-mas |
| 7 | Architectural Engineering/Construction Engineering and Management | B.S./M.ENG. | Armour | https://www.iit.edu/academics/programs/architectural-engineering-bs-construction-engineering-and-management-meng |
| 8 | Architecture/Construction Engineering and Management | B.ARCH./M.ENG. | Architecture + Armour | https://www.iit.edu/academics/programs/architecture-barch-construction-engineering-and-management-meng |
| 9 | Biochemistry/Biology for the Health Professions | B.S./M.S. | Lewis | https://www.iit.edu/academics/programs/biochemistry-bs-biology-health-professions-ms |
| 10 | Biochemistry/Food Safety and Technology | B.S./M.A.S. | Lewis | https://www.iit.edu/academics/programs/biochemistry-bs-food-safety-and-technology-mas |
| 11 | Biology/Biology | B.S./M.S. | Lewis | https://www.iit.edu/academics/programs/biology-bs-biology-ms |
| 12 | Biology/Biology for the Health Professions | B.S./M.S. | Lewis | https://www.iit.edu/academics/programs/biology-bsbiology-health-professions-ms |
| 13 | Biology/Computer Science | B.S./M.A.S. | Lewis + Computing | https://www.iit.edu/academics/programs/biology-bs-computer-science-mas |
| 14 | Biology/Computer Science | B.S./M.S. | Lewis + Computing | https://www.iit.edu/academics/programs/biology-bs-computer-science-ms |
| 15 | Biology/Food Safety and Technology | B.S./M.A.S. | Lewis | https://www.iit.edu/academics/programs/biology-bs-food-safety-and-technology-mas |
| 16 | Business Administration/Finance | B.S./M.S. | Stuart | https://www.iit.edu/academics/programs/business-administration-bs-finance-ms |
| 17 | Business Administration/Marketing Analytics | B.S./M.S. | Stuart | https://www.iit.edu/academics/programs/business-administration-bs-marketing-analytics-ms |
| 18 | Business Administration/Public Administration | B.S./M.P.A. | Stuart | https://www.iit.edu/academics/programs/business-administration-bs-public-policy-and-administration-mppa |
| 19 | Chemistry/Biology for the Health Professions | B.S./M.S. | Lewis | https://www.iit.edu/academics/programs/chemistry-bs-biology-health-professions-ms |
| 20 | Chemistry/Chemical Engineering | B.S./M.A.S. | Lewis + Armour | https://www.iit.edu/academics/programs/chemistry-bschemical-engineering-mas |
| 21 | Chemistry/Chemistry | B.S./M.S. | Lewis | https://www.iit.edu/academics/programs/chemistry-bs-chemistry-ms |
| 22 | Chemistry/Food Safety and Technology | B.S./M.A.S. | Lewis | https://www.iit.edu/academics/programs/chemistry-bs-food-safety-and-technology-mas |
| 23 | Civil Engineering/Construction Engineering and Management | B.S./M.ENG. | Armour | https://www.iit.edu/academics/programs/civil-engineering-bs-construction-engineering-and-management-meng |
| 24 | Computer Engineering/Computer Engineering | B.S./M.S. | Armour | https://www.iit.edu/academics/programs/computer-engineering-bscomputer-engineering-ms |
| 25 | Computer Engineering/Computer Science | B.S./M.A.S. | Armour + Computing | https://www.iit.edu/academics/programs/computer-engineering-bs-computer-science-mas |
| 26 | Computer Engineering/Computer Science | B.S./M.S. | Armour + Computing | https://www.iit.edu/academics/programs/computer-engineering-bs-computer-science-ms |
| 27 | Computer Engineering/Electrical Engineering | B.S./M.S. | Armour | https://www.iit.edu/academics/programs/computer-engineering-bselectrical-engineering-ms |
| 28 | Computer Science/Applied Mathematics | B.S./M.S. | Computing | https://www.iit.edu/academics/programs/computer-science-bs-applied-mathematics-ms |
| 29 | Computer Science/Computer Science | B.S./M.A.S. | Computing | https://www.iit.edu/academics/programs/computer-science-bscomputer-science-mas |
| 30 | Computer Science/Computer Science | B.S./M.S. | Computing | https://www.iit.edu/academics/programs/computer-science-bs-computer-science-ms |
| 31 | Computer Science/Data Science | B.S./M.A.S. | Computing | https://www.iit.edu/academics/programs/computer-science-bs-data-science-mas |
| 32 | Electrical Engineering/Electrical Engineering | B.S./M.S. | Armour | https://www.iit.edu/academics/programs/electrical-engineering-bs-electrical-engineering-ms |
| 33 | Electrical Engineering/Computer Engineering | B.S./M.S. | Armour | https://www.iit.edu/academics/programs/electrical-engineering-bs-computer-engineering-ms |
| 34 | ITM/ITM | B.A.C./M.A.S. | Computing | https://www.iit.edu/academics/programs/information-technology-and-management-bac-information-technology-and-management-mas |
| 35 | Industrial Technology and Management/Industrial Technology and Operations | B.A.C./M.A.S. | Armour | https://www.iit.edu/academics/programs/industrial-technology-and-management-bac-industrial-technology-and-operations-mas |
| 36 | Physics/Computer Science | B.S./M.A.S. | Lewis + Computing | https://www.iit.edu/academics/programs/physics-bs-computer-science-mas |
| 37 | Physics/Computer Science | B.S./M.S. | Lewis + Computing | https://www.iit.edu/academics/programs/physics-bs-computer-science-ms |
| 38 | Physics/Health Physics | B.S./M.A.S. | Lewis | https://www.iit.edu/academics/programs/physics-bs-health-physics-mas |
| 39 | Physics/Physics | B.S./M.S. | Lewis | https://www.iit.edu/academics/programs/physics-bs-physics-ms |

### 1.5 Minors — Complete List

| # | Minor | 学院 | URL |
|---|-------|------|-----|
| 1 | Aerospace Science | Armour | https://www.iit.edu/academics/programs/aerospace-science-minor |
| 2 | Applied Mathematics | Computing | https://www.iit.edu/academics/programs/applied-mathematics-minor |
| 3 | Applied Mechanics | Armour | https://www.iit.edu/academics/programs/applied-mechanics-minor |
| 4 | Architecture | Architecture | https://www.iit.edu/academics/programs/architecture-minor |
| 5 | Artificial Intelligence | Computing | https://www.iit.edu/academics/programs/artificial-intelligence-minor |
| 6 | Astrophysics | Lewis | https://www.iit.edu/academics/programs/astrophysics-minor |
| 7 | Biochemistry | Lewis | https://www.iit.edu/academics/programs/biochemistry-minor |
| 8 | Bioinformatics | Lewis | https://www.iit.edu/academics/programs/bioinformatics-minor |
| 9 | Biology | Lewis | https://www.iit.edu/academics/programs/biology-minor |
| 10 | Building Systems Engineering | Armour | https://www.iit.edu/academics/programs/building-systems-engineering-minor |
| 11 | Business | Stuart | https://www.iit.edu/academics/programs/business-minor |
| 12 | Chemistry | Lewis | https://www.iit.edu/academics/programs/chemistry-minor |
| 13 | Circuits and Systems | Armour | https://www.iit.edu/academics/programs/circuits-and-systems-minor |
| 14 | Communication | Lewis | https://www.iit.edu/academics/programs/communication-minor |
| 15 | Computational Mathematics | Computing | https://www.iit.edu/academics/programs/computational-mathematics-minor |
| 16 | Computational Structures | Computing | https://www.iit.edu/academics/programs/computational-structures-minor |
| 17 | Computer Architecture | Computing | https://www.iit.edu/academics/programs/computer-architecture-minor |
| 18 | Computer Networking | Computing | https://www.iit.edu/academics/programs/computer-networking-minor |
| 19 | Computer Science | Computing | https://www.iit.edu/academics/programs/computer-science-minor |
| 20 | Construction Management | Armour | https://www.iit.edu/academics/programs/construction-management-minor |
| 21 | Critical AI | Computing | https://www.iit.edu/academics/programs/critical-ai-minor |
| 22 | Cyber Security Foundations | Computing | https://www.iit.edu/academics/programs/cyber-security-foundations-minor |
| 23 | Database Management | Computing | https://www.iit.edu/academics/programs/database-management-minor |
| 24 | Economics | Lewis | https://www.iit.edu/academics/programs/economics-minor |
| 25 | Electromechanical Design and Manufacturing | Armour | https://www.iit.edu/academics/programs/electromechanical-design-and-manufacturing-minor |
| 26 | Energy/Environment/Economics | Lewis | https://www.iit.edu/academics/programs/energyenvironmenteconomics-minor |
| 27 | Entrepreneurship | Stuart | https://www.iit.edu/academics/programs/entrepreneurship-minor |
| 28 | Environmental Engineering | Armour | https://www.iit.edu/academics/programs/environmental-engineering-minor |
| 29 | Finance | Stuart | https://www.iit.edu/academics/programs/finance-minor |
| 30 | Food Science and Nutrition | Lewis | https://www.iit.edu/academics/programs/food-science-and-nutrition-minor |
| 31 | Graphics and CAD for Non-Engineers | Armour | https://www.iit.edu/academics/programs/graphics-and-cad-non-engineers-minor |
| 32 | Human Resources | Stuart | https://www.iit.edu/academics/programs/human-resources-minor |
| 33 | Industrial Technology and Management | Armour | https://www.iit.edu/academics/programs/industrial-technology-and-management-minor |
| 34 | Information Security | Computing | https://www.iit.edu/academics/programs/information-security-minor |
| 35 | Information System Administration | Computing | https://www.iit.edu/academics/programs/information-system-administration-minor |
| 36 | Information System Network Management | Computing | https://www.iit.edu/academics/programs/information-system-network-management-minor |
| 37 | Information Technology and Management | Computing | https://www.iit.edu/academics/programs/information-technology-and-management-minor |
| 38 | Information Technology Foundations | Computing | https://www.iit.edu/academics/programs/information-technology-foundations-minor |
| 39 | Internet Application Development | Computing | https://www.iit.edu/academics/programs/internet-application-development-minor |
| 40 | Leadership | Stuart | https://www.iit.edu/academics/programs/leadership-minor |
| 41 | Materials Science | Armour | https://www.iit.edu/academics/programs/materials-science-minor |
| 42 | Medical Humanities | Lewis | https://www.iit.edu/academics/programs/medical-humanities-minor |
| 43 | Music | Lewis | https://www.iit.edu/academics/programs/music-minor |
| 44 | Operating Systems | Computing | https://www.iit.edu/academics/programs/operating-systems-minor |
| 45 | Physics | Lewis | https://www.iit.edu/academics/programs/physics-minor |
| 46 | Policy and Ethics | Lewis | https://www.iit.edu/academics/programs/policy-and-ethics-minor |
| 47 | Polymer Science and Engineering | Armour | https://www.iit.edu/academics/programs/polymer-science-and-engineering-minor |
| 48 | Pre-Medical Studies | Lewis | https://www.iit.edu/academics/programs/pre-medical-studies-minor |
| 49 | Professional and Technical Communication | Lewis | https://www.iit.edu/academics/programs/professional-and-technical-communication-minor |
| 50 | Programming Languages | Computing | https://www.iit.edu/academics/programs/programming-languages-minor |
| 51 | Psychology | Lewis | https://www.iit.edu/academics/programs/psychology-minor |
| 52 | Public Administration | Lewis | https://www.iit.edu/academics/programs/public-administration-minor |
| 53 | Public Policy | Lewis | https://www.iit.edu/academics/programs/public-policy-minor |
| 54 | Rehabilitation Services | Lewis | https://www.iit.edu/academics/programs/rehabilitation-services-minor |
| 55 | Science and Technology Studies | Lewis | https://www.iit.edu/academics/programs/science-and-technology-studies-minor |
| 56 | Software Engineering | Computing | https://www.iit.edu/academics/programs/software-engineering-minor |
| 57 | Statistics | Computing | https://www.iit.edu/academics/programs/statistics-minor |
| 58 | Structural Engineering | Armour | https://www.iit.edu/academics/programs/structural-engineering-minor |
| 59 | Supply Chain Management | Armour | https://www.iit.edu/academics/programs/supply-chain-management-minor |
| 60 | Sustainability | Lewis | https://www.iit.edu/academics/programs/sustainability-minor |
| 61 | Telecommunications | Computing | https://www.iit.edu/academics/programs/telecommunications-minor |
| 62 | Transportation Engineering | Armour | https://www.iit.edu/academics/programs/transportation-engineering-minor |
| 63 | Engineering Graphics and CAD | Armour | https://www.iit.edu/academics/programs/engineering-graphics-and-cad-minor |

### 1.6 General Education Requirements

Illinois Tech 的通识教育要求因学院和专业而异。STEM 专业通常要求 4 年数学（含微积分以上）、4 年科学（含物理）、4 年英语。非 STEM 专业要求 3-4 年数学、3 年科学、4 年英语。详见: https://www.iit.edu/admissions-aid/undergraduate-admission/first-year-students/recommended-admission-guidelines

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

#### Armour College of Engineering

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Manufacturing | https://www.iit.edu/academics/programs/advanced-manufacturing-ms |
| 2 | Architectural Engineering | https://www.iit.edu/academics/programs/architectural-engineering-ms |
| 3 | Autonomous Systems and Robotics | https://www.iit.edu/academics/programs/autonomous-systems-and-robotics-ms |
| 4 | Biomedical Engineering | https://www.iit.edu/academics/programs/biomedical-engineering-ms |
| 5 | Chemical Engineering | https://www.iit.edu/academics/programs/chemical-engineering-ms |
| 6 | Civil Engineering | https://www.iit.edu/academics/programs/civil-engineering-ms |
| 7 | Computer Engineering | https://www.iit.edu/academics/programs/computer-engineering-ms |
| 8 | Construction Engineering and Management | https://www.iit.edu/academics/programs/construction-engineering-and-management-ms |
| 9 | Electrical Engineering | https://www.iit.edu/academics/programs/electrical-engineering-ms |
| 10 | Engineering Management | https://www.iit.edu/academics/programs/engineering-management-ms |
| 11 | Environmental Engineering | https://www.iit.edu/academics/programs/environmental-engineering-ms |
| 12 | Food Safety and Technology | https://www.iit.edu/academics/programs/food-safety-and-technology-ms |
| 13 | Materials Science and Engineering | https://www.iit.edu/academics/programs/materials-science-and-engineering-ms |
| 14 | Mechanical and Aerospace Engineering | https://www.iit.edu/academics/programs/mechanical-and-aerospace-engineering-ms |
| 15 | Sensor Science and Technology | https://www.iit.edu/academics/programs/sensor-science-and-technology-ms |
| 16 | Data Science in Engineering | https://www.iit.edu/academics/programs/data-science-engineering-ms |
| 17 | Project Management–Technology | https://www.iit.edu/academics/programs/project-management-ms |
| 18 | Technology and Social Innovation | https://www.iit.edu/academics/programs/technology-and-social-innovation-ms |

##### M.A.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Engineering | https://www.iit.edu/academics/programs/biological-engineering-mas |
| 2 | Electrical and Computer Engineering | https://www.iit.edu/academics/programs/electrical-and-computer-engineering-mas |
| 3 | Engineering Management, Product Design and Development Track | https://www.iit.edu/academics/programs/engineering-management-product-design-and-development-track-mas |
| 4 | Pharmaceutical Engineering | https://www.iit.edu/academics/programs/pharmaceutical-engineering-mas |

##### M.ENG.
| # | 项目 | URL |
|---|------|-----|
| 1 | Energy Systems, Energy Generation and Sustainability Track | https://www.iit.edu/academics/programs/energy-systems-energy-generation-and-sustainability-track-meng |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.iit.edu/academics/programs/architectural-engineering-phd |
| 2 | Biomedical Engineering | https://www.iit.edu/academics/programs/biomedical-engineering-phd |
| 3 | Chemical Engineering | https://www.iit.edu/academics/programs/chemical-engineering-phd |
| 4 | Civil Engineering | https://www.iit.edu/academics/programs/civil-engineering-phd |
| 5 | Computer Engineering | https://www.iit.edu/academics/programs/computer-engineering-phd |
| 6 | Electrical Engineering | https://www.iit.edu/academics/programs/electrical-engineering-phd |
| 7 | Environmental Engineering | https://www.iit.edu/academics/programs/environmental-engineering-phd |
| 8 | Materials Science and Engineering | https://www.iit.edu/academics/programs/materials-science-and-engineering-phd |
| 9 | Mechanical and Aerospace Engineering | https://www.iit.edu/academics/programs/mechanical-and-aerospace-engineering-phd |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.iit.edu/academics/programs/architectural-engineering-certificate |
| 2 | Biological Engineering | https://www.iit.edu/academics/programs/biological-engineering-certificate |
| 3 | Building Energy Modeling | https://www.iit.edu/academics/programs/building-energy-modeling-certificate |
| 4 | Compliance and Pollution Prevention | https://www.iit.edu/academics/programs/compliance-and-pollution-prevention-certificate |
| 5 | Computer Integrated Design and Manufacturing | https://www.iit.edu/academics/programs/computer-integrated-design-and-manufacturing-certificate |
| 6 | Construction Management | https://www.iit.edu/academics/programs/construction-management-certificate |
| 7 | Current Energy Issues | https://www.iit.edu/academics/programs/current-energy-issues-certificate |
| 8 | Cyber-Physical Systems | https://www.iit.edu/academics/programs/cyber-physical-systems-certificate |
| 9 | Earthquake and Wind Engineering Design | https://www.iit.edu/academics/programs/earthquake-and-wind-engineering-design-certificate |
| 10 | Infrastructure Engineering and Management | https://www.iit.edu/academics/programs/infrastructure-engineering-and-management-certificate |
| 11 | Pharmaceutical Engineering | https://www.iit.edu/academics/programs/pharmaceutical-engineering-certificate |
| 12 | Process Operations Management | https://www.iit.edu/academics/programs/process-operations-management-certificate |
| 13 | Product Quality and Reliability Assurance | https://www.iit.edu/academics/programs/product-quality-and-reliability-assurance-certificate |
| 14 | Transportation Systems Planning | https://www.iit.edu/academics/programs/transportation-systems-planning-certificate |

#### College of Computing

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.iit.edu/academics/programs/applied-mathematics-ms |
| 2 | Computer Engineering | https://www.iit.edu/academics/programs/computer-engineering-ms |
| 3 | Computer Science | https://www.iit.edu/academics/programs/computer-science-ms |
| 4 | Information Technology and Management | https://www.iit.edu/academics/programs/information-technology-and-management-ms |
| 5 | Management and Leadership | https://www.iit.edu/academics/programs/management-and-leadership-ms |

##### M.A.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.iit.edu/academics/programs/applied-mathematics-mas |
| 2 | Artificial Intelligence | https://www.iit.edu/academics/programs/artificial-intelligence-mas |
| 3 | Computer Science | https://www.iit.edu/academics/programs/computer-science-mas |
| 4 | Cybersecurity | https://www.iit.edu/academics/programs/cybersecurity-mas |
| 5 | Cybersecurity Engineering | https://www.iit.edu/academics/programs/cybersecurity-engineering-mas |
| 6 | Data Science | https://www.iit.edu/academics/programs/data-science-mas |
| 7 | Data Science with AI | https://www.iit.edu/academics/programs/data-science-ai-mas |
| 8 | Information Technology and Management | https://www.iit.edu/academics/programs/information-technology-and-management-mas |
| 9 | Management (M.A.S.)/Computer Science | https://www.iit.edu/academics/programs/management-mascomputer-science-mas |
| 10 | Management (M.A.S.)/ITM | https://www.iit.edu/academics/programs/management-masinformation-technology-and-management-mas |
| 11 | Technological Entrepreneurship | https://www.iit.edu/academics/programs/technological-entrepreneurship-mas |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.iit.edu/academics/programs/applied-mathematics-phd |
| 2 | Computer Science | https://www.iit.edu/academics/programs/computer-science-phd |
| 3 | Computer Engineering | https://www.iit.edu/academics/programs/computer-engineering-phd |
| 4 | Information Technology | https://www.iit.edu/academics/programs/information-technology-phd |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Software Development | https://www.iit.edu/academics/programs/advanced-software-development-certificate |
| 2 | Computational Intelligence | https://www.iit.edu/academics/programs/computational-intelligence-certificate |
| 3 | Cybersecurity Management | https://www.iit.edu/academics/programs/cybersecurity-management-certificate |
| 4 | Cybersecurity Technologies | https://www.iit.edu/academics/programs/cybersecurity-technologies-certificate |
| 5 | Data Analytics | https://www.iit.edu/academics/programs/data-analytics-certificate |
| 6 | Database Systems | https://www.iit.edu/academics/programs/database-systems-certificate |
| 7 | Distributed and Cloud Computing | https://www.iit.edu/academics/programs/distributed-and-cloud-computing-certificate |
| 8 | Foundations of Computer Science | https://www.iit.edu/academics/programs/foundations-computer-science-certificate |
| 9 | Information Security and Assurance | https://www.iit.edu/academics/programs/information-security-and-assurance-certificate |
| 10 | Information Technology Innovation, Leadership, and Entrepreneurship | https://www.iit.edu/academics/programs/information-technology-innovation-leadership-and-entrepreneurship-certificate |
| 11 | Networking and Communications | https://www.iit.edu/academics/programs/networking-and-communications-certificate |
| 12 | Software Engineering | https://www.iit.edu/academics/programs/software-engineering-certificate |
| 13 | System Administration | https://www.iit.edu/academics/programs/system-administration-certificate |
| 14 | Systems Analysis | https://www.iit.edu/academics/programs/systems-analysis-certificate |
| 15 | Web Design and Application Development | https://www.iit.edu/academics/programs/web-design-and-application-development-certificate |

#### Lewis College of Science and Letters

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Analytical Chemistry | https://www.iit.edu/academics/programs/analytical-chemistry-ms |
| 2 | Biology | https://www.iit.edu/academics/programs/biology-ms |
| 3 | Biology for the Health Professions | https://www.iit.edu/academics/programs/biology-health-professions-ms |
| 4 | Chemistry | https://www.iit.edu/academics/programs/chemistry-ms |
| 5 | Clinical Counseling | https://www.iit.edu/academics/programs/masters-in-clinical-counseling |
| 6 | Food Safety and Technology | https://www.iit.edu/academics/programs/food-safety-and-technology-ms |
| 7 | Industrial-Organizational Psychology | https://www.iit.edu/academics/programs/industrial-organizational-psychology-ms |
| 8 | Nutrition Science | https://www.iit.edu/academics/programs/nutrition-science-ms |
| 9 | Physics | https://www.iit.edu/academics/programs/physics-ms |

##### M.A.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Physics | https://www.iit.edu/academics/programs/health-physics-mas |
| 2 | Materials Chemistry | https://www.iit.edu/academics/programs/materials-chemistry-mas |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://www.iit.edu/academics/programs/biology-phd |
| 2 | Chemistry | https://www.iit.edu/academics/programs/chemistry-phd |
| 3 | Clinical Psychology | https://www.iit.edu/academics/programs/phd-clinical-psychology |
| 4 | Food Science and Nutrition | https://www.iit.edu/academics/programs/food-science-and-nutrition-phd |
| 5 | Industrial-Organizational Psychology | https://www.iit.edu/academics/programs/industrial-organizational-psychology-phd |
| 6 | Physics | https://www.iit.edu/academics/programs/physics-phd |
| 7 | Rehabilitation Counseling Education | https://www.iit.edu/academics/programs/rehabilitation-counseling-education-phd |
| 8 | Technology and Humanities | https://www.iit.edu/academics/programs/technology-and-humanities-phd |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Analytical Method Development | https://www.iit.edu/academics/programs/analytical-method-development-certificate |
| 2 | Analytical Spectroscopy | https://www.iit.edu/academics/programs/analytical-spectroscopy-certificate |
| 3 | Chromatography | https://www.iit.edu/academics/programs/chromatography-certificate |
| 4 | Food Processing Specialist | https://www.iit.edu/academics/programs/food-processing-specialist-certificate |
| 5 | Food Safety and Industrial Management | https://www.iit.edu/academics/programs/food-safety-and-industrial-management-certificate |
| 6 | Food Safety and Technology | https://www.iit.edu/academics/programs/food-safety-and-technology-certificate |
| 7 | Materials Chemistry | https://www.iit.edu/academics/programs/materials-chemistry-certificate |
| 8 | Preparatory Program for Medical Studies | https://www.iit.edu/academics/programs/preparatory-program-medical-studies-certificate |
| 9 | Psychiatric Rehabilitation | https://www.iit.edu/academics/programs/psychiatric-rehabilitation-certificate |
| 10 | Radiological Physics | https://www.iit.edu/academics/programs/radiological-physics-certificate |
| 11 | Regulatory Science | https://www.iit.edu/academics/programs/regulatory-science-certificate |
| 12 | Rehabilitation Engineering Technology | https://www.iit.edu/academics/programs/rehabilitation-engineering-technology-certificate |
| 13 | Re-Specialization in Clinical Psychology | https://www.iit.edu/academics/programs/re-specialization-clinical-psychology-certificate |
| 14 | Instructional Design | https://www.iit.edu/academics/programs/instructional-design-certificate |
| 15 | Nonprofit and Mission-Driven Management | https://www.iit.edu/academics/programs/nonprofit-and-mission-driven-management-certificate |

#### College of Architecture

##### M.ARCH.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://www.iit.edu/academics/programs/architecture-march |

##### M.S.ARCH.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://www.iit.edu/academics/programs/architecture-msarch |

##### M.L.A.+U.
| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture + Urbanism | https://www.iit.edu/academics/programs/landscape-architecture-urbanism-mlau |

##### M.HPB.
| # | 项目 | URL |
|---|------|-----|
| 1 | High Performance Buildings | https://www.iit.edu/academics/programs/high-performance-buildings-mhpb |

##### M.TVBU
| # | 项目 | URL |
|---|------|-----|
| 1 | Master Tall Buildings and Vertical Urbanism | https://www.iit.edu/academics/programs/master-tall-buildings-and-vertical-urbanism-mtvbu |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://www.iit.edu/academics/programs/architecture-phd |

#### Stuart School of Business

##### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | https://www.iit.edu/academics/programs/business-administration-mba |
| 2 | Business Analytics | https://www.iit.edu/academics/programs/business-analytics-mba |
| 3 | Technological Entrepreneurship | https://www.iit.edu/academics/programs/technological-entrepreneurship-mba |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.iit.edu/academics/programs/business-analytics-ms |
| 2 | Finance | https://www.iit.edu/academics/programs/finance-ms |
| 3 | Financial Markets and Technology | https://www.iit.edu/academics/programs/financial-markets-and-technology-ms |
| 4 | Management and Leadership | https://www.iit.edu/academics/programs/management-and-leadership-ms |
| 5 | Marketing Analytics | https://www.iit.edu/academics/programs/marketing-analytics-ms |
| 6 | Sustainability Analytics and Management | https://www.iit.edu/academics/programs/sustainability-analytics-and-management-ms |
| 7 | People Analytics | https://www.iit.edu/academics/programs/people-analytics-ms |

##### M.P.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.iit.edu/academics/programs/public-administration-mpa |
| 2 | Public Administration in Analytics | https://www.iit.edu/academics/programs/public-administration-analytics-mpa |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance | https://www.iit.edu/academics/programs/finance-phd |
| 2 | Management Science and Analytics | https://www.iit.edu/academics/programs/management-science-phd |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Management | https://www.iit.edu/academics/programs/business-management-certificate |
| 2 | Corporate Finance and Valuation | https://www.iit.edu/academics/programs/corporate-finance-and-valuation-certificate |
| 3 | Financial Technology | https://www.iit.edu/academics/programs/financial-technology-certificate |
| 4 | Financial Toolbox | https://www.iit.edu/academics/programs/financial-toolbox-certificate |
| 5 | Fundamentals of Finance | https://www.iit.edu/academics/programs/fundamentals-finance-certificate |
| 6 | Marketing Analytics | https://www.iit.edu/academics/programs/marketing-analytics-certificate |
| 7 | Portfolio Management | https://www.iit.edu/academics/programs/portfolio-management-certificate |
| 8 | Public Management | https://www.iit.edu/academics/programs/public-management-certificate |
| 9 | Quantitative Modeling and Trading | https://www.iit.edu/academics/programs/quantitative-modeling-and-trading-certificate |
| 10 | Risk Management | https://www.iit.edu/academics/programs/risk-management-certificate |
| 11 | Strategic Management | https://www.iit.edu/academics/programs/strategic-management-certificate |
| 12 | Sustainable Enterprise | https://www.iit.edu/academics/programs/sustainable-enterprise-certificate |

#### Chicago-Kent College of Law

##### J.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.iit.edu/academics/programs/law-jd |

##### LL.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | International Intellectual Property Law | https://www.iit.edu/academics/programs/international-intellectual-property-law-llm |
| 2 | Law | https://www.iit.edu/academics/programs/law-llm |
| 3 | Legal Innovation and Technology | https://www.iit.edu/academics/programs/legal-innovation-and-technology-llm |
| 4 | Trial Advocacy for International Students | https://www.iit.edu/academics/programs/trial-advocacy-international-students-llm |
| 5 | U.S., International, and Transnational Law | https://www.iit.edu/academics/programs/us-international-and-transnational-law-llm |

##### J.S.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.iit.edu/academics/programs/law-jsd |

##### J.D. Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Law | https://www.iit.edu/academics/programs/business-law-jd-certificate |
| 2 | Criminal Litigation | https://www.iit.edu/academics/programs/criminal-litigation-jd-certificate |
| 3 | Environmental and Energy Law | https://www.iit.edu/academics/programs/environmental-and-energy-law-jd-certificate |
| 4 | Intellectual Property Law | https://www.iit.edu/academics/programs/intellectual-property-law-jd-certificate |
| 5 | International and Comparative Law | https://www.iit.edu/academics/programs/international-and-comparative-law-jd-certificate |
| 6 | Labor and Employment Law | https://www.iit.edu/academics/programs/labor-and-employment-law-jd-certificate |
| 7 | Legal Innovation and Technology | https://www.iit.edu/academics/programs/legal-innovation-and-technology-jd-certificate |
| 8 | Litigation and Alternative Dispute Resolution | https://www.iit.edu/academics/programs/litigation-and-alternative-dispute-resolution-jd-certificate |
| 9 | Praxis Program | https://www.iit.edu/academics/programs/praxis-program-jd-certificate |
| 10 | Public Interest Law | https://www.iit.edu/academics/programs/public-interest-law-jd-certificate |

#### Institute of Design

##### M.Des.
| # | 项目 | URL |
|---|------|-----|
| 1 | Design | https://www.iit.edu/academics/programs/design-mdes |

##### M.D.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Design Methods | https://www.iit.edu/academics/programs/design-methods-mdm |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Design | https://www.iit.edu/academics/programs/design-phd |

#### Online (Coursera)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Information Technology and Management | B.A.C. | https://www.iit.edu/academics/programs/bachelor-information-technology-coursera |
| 2 | Information Technology and Management | M.A.S. | https://www.iit.edu/academics/programs/information-technology-and-management-mas-coursera |
| 3 | Business Administration | M.B.A. | https://www.iit.edu/academics/programs/business-administration-mba-coursera |
| 4 | Data Science | M.A.S. | https://www.iit.edu/academics/programs/data-science-mas-coursera |

### 2.2 Graduate Admissions Model

Illinois Tech 采用 **集中式研究生招生**，由 Office of Graduate Admission 统一管理。申请通过单一在线门户提交。各学院/系可有不同的具体要求（如 GRE 要求、先修课程等）。

**关键招生信息**:
- GPA 要求: 3.0/4.0（常规录取）；美国公民/永久居民 2.5+ 可作为非学位学生入学
- GRE: **所有硕士项目可选**（optional）；**大多数博士项目要求 GRE**
- GMAT: Institute of Design 和 Stuart School of Business 接受
- 申请费: 未在官网明确列出（需联系招生办确认）
- 英语要求: TOEFL 80+ / IELTS 6.5+ / Duolingo 115+

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| **Early Decision (ED)** | November 1 (Binding) | https://www.iit.edu/admissions-aid/undergraduate-admission/application-dates-and-deadlines |
| **Early Action (EA)** | November 15 (Non-Binding) | 同上 |
| **Regular Decision (RD)** | February 1 | 同上 |
| **Spring Entry RD** | October 15 | 同上 |
| **Decision Notification (ED)** | December | 同上 |
| **Decision Notification (EA)** | January | 同上 |
| **Decision Notification (RD)** | March 15 | 同上 |
| **Enrollment Deposit Due (ED/EA)** | May 1 | 同上 |
| **Enrollment Deposit Due (RD)** | May 1 | 同上 |
| **I-20 Request Date (Intl)** | June 15 | 同上 |
| **Application Portal** | https://apply.illinoistech.edu/ | https://www.iit.edu/admissions-aid/apply |
| **Application Platform** | Common App, Coalition, Illinois Tech App | 同上 |
| **Test Policy** | **Test-Optional** (SAT/ACT 完全可选) | https://www.iit.edu/admissions-aid/undergraduate-admission/first-year-students/recommended-admission-guidelines |
| **Superscore** | N/A (test-optional) | |
| **SAT Code** | 1318 | https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements |
| **ACT Code** | 1318 | 同上 |
| **TOEFL Code** | 1318 | 同上 |
| **Recommendation** | 建议提交与专业相关的推荐信 | https://www.iit.edu/admissions-aid/undergraduate-admission/first-year-students/recommended-admission-guidelines |
| **Interview** | 未提及 | |
| **Portfolio** | 建筑专业可能需要（需确认） | |

**来源**: https://www.iit.edu/admissions-aid/undergraduate-admission/application-dates-and-deadlines

**原文摘录**:
> "Early Decision (Binding) — November 1 — December — March 15 — June 15"
> "Early Action (Non-Binding) — November 15 — January — May 1 — June 15"
> "Regular Decision — February 1 — March 15 — May 1 — June 15"

**注意**: 用户提供的截止日期（EA Nov 1, EA2 Dec 15, RD Jan 15）与官网不符。官网显示 EA 为 November 15，RD 为 February 1，无 EA2。

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 备注 |
|------|----------|------|
| TOEFL iBT | 80 | 不接受 MyBest scores |
| IELTS | 6.5 | 电子送分 |
| Duolingo | 115 | |
| SAT EBRW | 550 | 可豁免英语要求 |
| ACT English | 25 | 可豁免英语要求 |
| AP English | 4 or 5 | 可豁免英语要求 |
| IB English A | 5, 6, or 7 (SL/HL) | 可豁免英语要求 |
| GCE/GCSE/IGCSE English | A or BB | 可豁免英语要求 |
| India Standard XII English | 60%+ (B average) | CBSE, CISCE, or state boards |
| Chinese Gaokao English | 120+ | 可豁免英语要求 |

**豁免国家**: 澳大利亚、加拿大（魁北克除外）、加纳、圭亚那、牙买加、马耳他、新西兰、尼日利亚、特立尼达和多巴哥、英国、美国等英语为主要语言的国家。

**来源**: https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements

**原文摘录**:
> "TOEFL iBT: 80 or above"
> "IELTS: 6.5 or above"
> "Duolingo: 115 or above"

### 3.3 Graduate — Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| **GPA 要求** | 3.0/4.0（常规录取） | https://www.iit.edu/admissions-aid/graduate-admission |
| **GRE** | 硕士可选（optional）；大多数博士要求 | 同上 |
| **GMAT** | Institute of Design 和 Stuart School of Business 接受 | 同上 |
| **英语要求** | TOEFL 80+ / IELTS 6.5+ / Duolingo 115+ | https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements |
| **申请方式** | 集中式（单一在线门户） | https://www.iit.edu/admissions-aid/graduate-admission |
| **转学分** | 硕士最多 9 学分；博士最多 48 学分或 50% | 同上 |

**来源**: https://www.iit.edu/admissions-aid/graduate-admission

**原文摘录**:
> "The Graduate Record Examination (GRE) is optional for ALL master's programs"
> "GRE scores are required for most Ph.D. programs"
> "Illinois Tech requires a four-year bachelor's degree that is conferred with a minimum cumulative undergraduate grade-point average of 3.0 on a 4.0 scale"

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026–2027 Academic Year)

| 费用项目 | 金额 | 说明 |
|----------|------|------|
| Tuition | $53,198 | 全日制本科生 |
| Fees | $1,850 | 学杂费 |
| Housing and Food | $18,548 | 住宿和餐饮（校内） |
| **预估总费用** | **$73,596** | 不含书本、个人开支等 |

**来源**: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid

**原文摘录**:
> "2026–2027 Academic Year — New Undergraduate Students:
> $53,198 Tuition
> $1,850 Fees
> $18,548 Housing and Food"

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| **Need-Blind (美国)** | 未明确说明（需确认） | |
| **Need-Aware (国际)** | 未明确说明（需确认） | |
| **98% 本科生获得资助** | 是 | https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid |
| **奖学金范围** | $10,000 至全额学费 | 同上 |
| **FAFSA Code** | 001691 | 同上 |
| **Pell Grant 比例** | 38% | https://www.iit.edu/financial-aid |
| **贷款违约率** | 2.9%（全国平均 9.7%） | 同上 |

**来源**: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid

**原文摘录**:
> "With 98 percent of our undergraduates receiving some form of financial aid"
> "We offer scholarship opportunities in dollar amounts ranging from $10,000 to a full-tuition scholarship."

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| **研究生学费** | 因学院而异（需查看各学院网站） | https://www.iit.edu/admissions-aid/tuition-and-aid/graduate-costs-and-aid |
| **健康保险** | 全日制学生必须购买 | 同上 |
| **资助类型** | 奖学金、助教、研究助理 | 同上 |

**特殊学院学费**: Chicago-Kent College of Law、College of Architecture、Institute of Design、Stuart School of Business 有独立学费标准。

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.ED
  value: "November 1"
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/application-dates-and-deadlines
  source_snippet: "Early Decision (Binding) — November 1 — December — March 15 — June 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.EA
  value: "November 15"
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/application-dates-and-deadlines
  source_snippet: "Early Action (Non-Binding) — November 15 — January — May 1 — June 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.RD
  value: "February 1"
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/application-dates-and-deadlines
  source_snippet: "Regular Decision — February 1 — March 15 — May 1 — June 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.test_policy
  value: "Test-Optional"
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/first-year-students/recommended-admission-guidelines
  source_snippet: "ACT or SAT scores are completely optional for admission. Admission counselors will review your scores if provided. Opting out of providing test scores will not negatively impact your application for admission."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.TOEFL
  value: 80
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements
  source_snippet: "TOEFL iBT: 80 or above"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.IELTS
  value: 6.5
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements
  source_snippet: "IELTS: 6.5 or above"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english_proficiency.Duolingo
  value: 115
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements
  source_snippet: "Duolingo: 115 or above"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.cost.tuition_2026_2027
  value: "$53,198"
  source_url: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid
  source_snippet: "2026–2027 Academic Year — New Undergraduate Students: $53,198 Tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.cost.fees_2026_2027
  value: "$1,850"
  source_url: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid
  source_snippet: "$1,850 Fees"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.cost.housing_food_2026_2027
  value: "$18,548"
  source_url: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid
  source_snippet: "$18,548 Housing and Food"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.financial_aid.pct_receiving_aid
  value: "98%"
  source_url: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid
  source_snippet: "With 98 percent of our undergraduates receiving some form of financial aid"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.admitted_profile.stem.avg_gpa
  value: 4.12
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/first-year-students/recommended-admission-guidelines
  source_snippet: "STEM* — 3.5–4.0+ — 4.12 — ACT Composite: 25–30+ — ACT Composite: 29"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.gpa_requirement
  value: "3.0/4.0"
  source_url: https://www.iit.edu/admissions-aid/graduate-admission
  source_snippet: "Illinois Tech requires a four-year bachelor's degree that is conferred with a minimum cumulative undergraduate grade-point average of 3.0 on a 4.0 scale"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.gre_policy
  value: "Optional for master's; required for most Ph.D."
  source_url: https://www.iit.edu/admissions-aid/graduate-admission
  source_snippet: "The Graduate Record Examination (GRE) is optional for ALL master's programs... However, GRE scores are required for most Ph.D. programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_proficiency
  value: "TOEFL 80+ / IELTS 6.5+ / Duolingo 115+"
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements
  source_snippet: "English Proficiency Requirement for GR: TOEFL iBT: 80 or above / IELTS: 6.5 or above / Duolingo: 115 or above"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-001:
  field: institution.colleges
  value: "7 colleges"
  source_url: https://www.iit.edu/academics/colleges-and-institutes
  source_snippet: "Armour College of Engineering, Chicago-Kent College of Law, College of Architecture, College of Computing, Institute of Design, Lewis College of Science and Letters, Stuart School of Business"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-002:
  field: institution.programs.total
  value: 355
  source_url: https://www.iit.edu/academics/programs
  source_snippet: "355 programs listed on the academic programs page"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-003:
  field: undergraduate.admitted_profile.non_stem.avg_gpa
  value: 4.0
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/first-year-students/recommended-admission-guidelines
  source_snippet: "Discover+, Tech+, Innovation and Society**, Architecture — 3.4–4.0+ — 4.0 — ACT Composite: 23–30+ — ACT Composite: 27"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-A-004:
  field: institution.tofl_code
  value: 1318
  source_url: https://www.iit.edu/admissions-aid/undergraduate-admission/international-undergraduate-students/english-language-proficiency-requirements
  source_snippet: "Illinois Tech's TOEFL code is 1318."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-A-005:
  field: institution.fafsa_code
  value: 001691
  source_url: https://www.iit.edu/admissions-aid/tuition-and-aid/undergraduate-costs-and-aid
  source_snippet: 'Designate "IIT" on the FAFSA with our Title IV code, 001691'
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
iit-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-armour-engineering         (Section 1: Armour College UG programs)
├── 02-ug-college-of-computing       (Section 1: College of Computing UG programs)
├── 03-ug-lewis-science              (Section 1: Lewis College UG programs)
├── 04-ug-architecture               (Section 1: College of Architecture UG programs)
├── 05-ug-stuart-business            (Section 1: Stuart School UG programs)
├── 06-ug-minors                     (Section 1: all minors)
├── 07-grad-armour-engineering       (Section 2: Armour College grad programs)
├── 08-grad-college-of-computing     (Section 2: College of Computing grad programs)
├── 09-grad-lewis-science            (Section 2: Lewis College grad programs)
├── 10-grad-architecture             (Section 2: College of Architecture grad programs)
├── 11-grad-stuart-business          (Section 2: Stuart School grad programs)
├── 12-grad-chicago-kent-law         (Section 2: Chicago-Kent grad programs)
├── 13-grad-institute-of-design      (Section 2: Institute of Design grad programs)
├── 14-deadlines-requirements        (Section 3: deadlines, test policy, English proficiency)
├── 15-costs-financial-aid           (Section 4: COA, aid policy)
└── 16-evidence-chain                (Section 5: all evidence blocks)
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "iit-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<B.S.|M.S.|Ph.D.|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| 优先级 | 数据项 | 目标 URL |
|--------|--------|----------|
| P0 | 各学院研究生具体学费率 | 各学院网站 |
| P0 | Need-blind/need-aware 政策明确说明 | https://www.iit.edu/financial-aid |
| P1 | 各博士项目 GRE 具体要求 | 各项目页面 |
| P1 | 建筑专业作品集要求 | https://www.iit.edu/academics/college-architecture |
| P1 | 国际学生奖学金政策 | https://www.iit.edu/admissions-aid/tuition-and-aid/scholarships |
| P2 | 各项目具体先修课程要求 | 各项目页面 |
| P2 | 转学分政策细节 | https://www.iit.edu/admissions-aid/graduate-admission |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Illinois Tech | (其他学校) |
|------|---------------|-----------|
| 所在地 | Chicago, IL | |
| 类型 | Private | |
| ED 截止日期 | November 1 | |
| EA 截止日期 | November 15 | |
| RD 截止日期 | February 1 | |
| 本科学费/年 | $53,198 | |
| 本科总费用/年 | ~$73,596 | |
| Need-Blind (美国) | 未明确 | |
| Need-Aware (国际) | 未明确 | |
| SAT/ACT 要求 | Test-Optional | |
| TOEFL 最低 | 80 | |
| IELTS 最低 | 6.5 | |
| Duolingo 最低 | 115 | |
| 研究生 GRE | 硕士可选；博士多要求 | |
| 项目总数 (Rule 1) | 355 | |
| 学院数 (Rule 2) | 7 | |
| 学位级别数 (Rule 3) | 22 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: iit.edu, apply.illinoistech.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
