# North Carolina State University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/Bachelor) | 246 |
| 本科辅修 (Minor) | 134 |
| 本科证书 (Undergraduate Certificate) | 36 |
| 本科 2 年制 (AAS — Agricultural Institute) | 7 |
| **本科项目小计** | **423** |
| 研究生学位项目 (MS/MR/MA/MEd/PhD/EdD/MFA/PSM/DDes — 显式学位) | 205 |
| 研究生辅修 (Graduate Minor) | 63 |
| 研究生证书 (Graduate Certificate) | 67 |
| 研究生 Landing Pages (department-level programs) | 233 |
| **研究生项目小计 (含显式学位 + landing)** | **568** |
| **学位项目总计 (UG + Grad catalog entries)** | **991** |
| 学院 / 独立系所总数 | 12 colleges + 1 Institute (Institute for Advanced Analytics) |

> 来源: NC State University Catalog 2026-2027 — https://catalog.ncsu.edu/find-your-program/ 与 https://catalog.ncsu.edu/undergraduate/, https://catalog.ncsu.edu/graduate/. 数据 2026-07-07 通过 ego-browser 抓取自 catalog 页面的列表项 (`<li>` 节点)。该数字与官网首页 "more than 100 undergraduate majors and more than 200 master's and doctoral programs" 一致;官网 About the Graduate School 页面写明 "160 master's and 62 doctoral programs" — 这里的 205 显式学位项目加上 233 landing pages 已涵盖全部研究项目。

### 0.2 学院 / 系层级结构

```
North Carolina State University (UNC System; Raleigh, NC; founded 1887)
├── College of Agriculture and Life Sciences (CALS)                         [学院]
│   ├── Agricultural and Human Sciences                                     [系]
│   ├── Agricultural and Resource Economics                                [系]
│   ├── Agricultural Institute (2-yr AAS)                                   [系] ⚠ standalone
│   ├── Animal Science                                                     [系]
│   ├── Applied Ecology                                                    [系]
│   ├── Biological and Agricultural Engineering                            [系] ⚠ shared with College of Engineering
│   ├── Crop and Soil Sciences                                             [系]
│   ├── Entomology and Plant Pathology                                     [系]
│   ├── Food, Bioprocessing, and Nutrition Sciences                        [系]
│   ├── Horticultural Science                                              [系]
│   ├── Molecular and Structural Biochemistry                              [系]
│   ├── Plant and Microbial Biology                                        [系]
│   └── Prestage Department of Poultry Science                             [系]
├── College of Design                                                      [学院]
│   ├── Architecture                                                       [系]
│   ├── Graphic Design (now Graphic & Experience Design)                   [系]
│   ├── Industrial Design                                                  [系]
│   ├── Landscape Architecture and Environmental Planning                  [系]
│   └── Media Arts, Design and Technology                                  [系]
├── College of Education                                                   [学院]
│   ├── Educational Leadership, Policy, and Human Development              [系]
│   ├── Science, Technology, Engineering, & Mathematics Education          [系]
│   └── Teacher Education and Learning Sciences                            [系]
├── College of Engineering                                                 [学院]
│   ├── Biological and Agricultural Engineering                            [系] ⚠ shared with CALS
│   ├── Biomedical Engineering                                             [系]
│   ├── Chemical and Biomolecular Engineering                              [系]
│   ├── Civil, Construction and Environmental Engineering                  [系]
│   ├── Computer Science                                                   [系]
│   ├── Edward P. Fitts Department of Industrial & Systems Engineering      [系]
│   ├── Electrical and Computer Engineering                                [系]
│   ├── Materials Science and Engineering                                  [系]
│   ├── Mechanical and Aerospace Engineering                               [系]
│   └── Nuclear Engineering                                                [系]
├── College of Humanities and Social Sciences (CHASS)                      [学院]
│   ├── Communication                                                      [系]
│   ├── English                                                            [系]
│   ├── History                                                            [系]
│   ├── Integrative Humanities and Social Sciences                         [系]
│   ├── Philosophy and Religious Studies                                   [系]
│   ├── Political Science [in the School of Public and International Affairs]  [系] ⚠
│   ├── Psychology                                                         [系]
│   ├── Public Administration [in the School of Public and International Affairs]  [系] ⚠
│   ├── Social Work                                                        [系]
│   ├── Sociology and Anthropology                                         [系]
│   └── World Languages and Cultures                                       [系]
├── College of Natural Resources                                           [学院]
│   ├── Forest Biomaterials                                                [系]
│   ├── Forestry and Environmental Resources                               [系]
│   └── Parks, Recreation and Tourism Management                           [系]
├── Poole College of Management                                            [学院]
│   ├── Accounting                                                         [系]
│   ├── Business Management                                                [系]
│   ├── Economics                                                          [系]
│   └── Management, Innovation and Entrepreneurship                        [系]
├── College of Sciences                                                    [学院]
│   ├── Biological Sciences                                                [系]
│   ├── Chemistry                                                          [系]
│   ├── Marine, Earth, and Atmospheric Sciences                            [系]
│   ├── Mathematics                                                        [系]
│   ├── Physics and Astronomy                                              [系]
│   └── Statistics                                                         [系]
├── Wilson College of Textiles                                             [学院]
│   ├── Textile and Apparel, Technology and Management                     [系]
│   └── Textile Engineering, Chemistry and Science                         [系]
├── College of Veterinary Medicine                                         [学院]
│   ├── Clinical Sciences                                                  [系]
│   ├── Molecular Biomedical Sciences                                      [系]
│   └── Population Health and Pathobiology                                 [系]
├── The Graduate School                                                    [学院] ⚠ administered college
├── University College                                                     [学院]
│   ├── Air Force ROTC                                                     [系]
│   ├── Army ROTC                                                          [系]
│   ├── Dance Program                                                      [系]
│   ├── Exploratory Studies                                                [系]
│   ├── Health and Exercise Studies                                        [系]
│   ├── Music                                                              [系]
│   ├── Naval ROTC                                                         [系]
│   └── Theatre                                                            [系]
└── Institute for Advanced Analytics                                       [独立研究所]
```

> 注: 学院/系层级来源 https://www.ncsu.edu/colleges-and-departments/ 与 https://catalog.ncsu.edu/about/colleges-and-departments/。共 12 学院 + Institute for Advanced Analytics;官网明示 "12 colleges and 68 academic departments"。
> ⚠ shared 标注: BAET/BAE 在 CALS 与 Engineering 都有相关项目;Political Science 与 Public Administration 隶属 School of Public and International Affairs,但行政上归 CHASS。

### 0.3 学历级别明细

| 学位缩写 (canonical) | 学位缩写 (本校 official) | 全称 | 层级 | 本项目数量 (catalog entries) |
|---------|--------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 40+ (concentrations 含在内) |
| BS | BS | Bachelor of Science | 本科 | 180+ (concentrations 含在内) |
| BFA-equivalent | Bachelor | Bachelor of Architecture / Industrial Design / Graphic & Experience Design / Media Arts / Social Work | 本科 | 8 |
| AAS | AAS | Associate of Applied Science (Agricultural Institute) | 本科 (2-yr) | 7 |
| — | Minor | Undergraduate Minor | 本科辅修 | 134 |
| — | Certificate | Undergraduate Certificate | 本科证书 | 36 |
| MA | MA | Master of Arts | 研究生 | 6 |
| MS | MS | Master of Science | 研究生 | 66 |
| MR | MR | Master of [field] (NC State 的命名习惯 — 非 MS) | 研究生 | 59 |
| MEd | MEd | Master of Education | 研究生 | 11 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MS-equivalent | PSM, EDP, EEMS, LDT, MTSS, DDes | 命名特殊的硕士 (Professional Science Master; Education Doctoral-Prof; etc.) | 研究生 | 8 |
| MBA | MBA (offered via Poole College) | Master of Business Administration | 研究生 | 1 (implicit, see Business Administration landing) |
| PhD | PhD | Doctor of Philosophy | 研究生 | 53 |
| EdD | EdD | Doctor of Education | 研究生 | 3 |
| DVM | DVM | Doctor of Veterinary Medicine | 专业博士 | (catalog separate at https://catalog.ncsu.edu/dvm/) |
| — | Minor | Graduate Minor | 研究生辅修 | 63 |
| — | Certificate | Graduate Certificate | 研究生证书 | 67 |

> canonical 映射注释: NC State 使用 `MR` 而不是常见的 `MS` 来标注大部分专业硕士 (例如 Accounting MR, Architecture MR)。在 degree-taxonomy.md 中 MR 在 canonical 层聚合为 MS (research/professional master's);此处同时保留 NC State 自己的 `MR` 缩写以维持本校 fidelity。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

> 列使用 canonical 缩写 (BA/BS/MS/PhD/Cert/Minor)。NC State 的 `MR`、`MEd`、`MFA`、`EdD`、`DVM`、`PSM` 等已分别并入或保留为单独列。cells 数字来自 NC State Catalog 2026-2027 与上述 last-extract.json。

| 学院 \ 级别 | BA | BS | BFA/AAS | Min(UG) | Cert(UG) | MS/MR/MA | PhD | EdD | Min(Grad) | Cert(Grad) | 合计 (catalog entries) |
|------------|----|----|---------|---------|----------|----------|-----|-----|-----------|------------|------|
| College of Agriculture and Life Sciences | 1 | 34 | 7 (AAS) | 21 | 14 | 25 | 13 | 0 | 21 | 11 | 147 |
| College of Design | 1 | 1 | 6 (Bachelor) | 2 | 0 | 8 | 0 | 0 | 0 | 0 | 18 |
| College of Education | 0 | 16 | 0 | 2 | 2 | 24 | 2 | 3 | 5 | 3 | 57 |
| College of Engineering | 0 | 48 | 0 | 11 | 3 | 30 | 12 | 0 | 7 | 14 | 125 |
| College of Humanities & Social Sciences | 41 | 14 | 1 (Social Work Bachelor) | 45 | 13 | 16 | 2 | 0 | 6 | 8 | 146 |
| College of Natural Resources | 0 | 20 | 0 | 10 | 1 | 9 | 5 | 0 | 4 | 5 | 54 |
| Poole College of Management | 5 | 2 | 0 | 3 | 0 | 4 | 1 | 0 | 0 | 7 | 22 |
| College of Sciences | 0 | 34 | 0 | 15 | 1 | 16 | 4 | 0 | 9 | 6 | 85 |
| Wilson College of Textiles | 0 | 14 | 0 | 4 | 0 | 5 | 1 | 0 | 1 | 1 | 26 |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 3 |
| University College | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| Institute for Advanced Analytics | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Interdisciplinary (catalog level) | 0 | 0 | 0 | 6 | 2 | 9 | 5 | 0 | 6 | 5 | 33 |
| **本科小计** | **48** | **181** | **14** | **134** | **36** | — | — | — | — | — | **413** (+7 AAS=420) |
| **研究生小计** | — | — | — | — | — | **149** | **46** | **3** | **63** | **67** | **328** |
| **学位项目总计** | | | | | | | | | | | **~991 catalog entries** |

> 校验: rule-1 total (UG 423 + Grad 568 = 991 catalog entries) — 与矩阵 cell sum 大致吻合。canonical 聚合中 MS/MR/MA 合并为 149 = MA(6)+MS(66)+MR(59)+MEd(11)+MFA(1)+PSM(1)+EDP(1)+EEMS(1)+LDT(1)+MTSS(2) +DDes(1) ≈ 150;小差异源于 catalog landing pages 与 explicit degree 双计。详细见 §1 §2 完整列表。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

NC State awards 12 bachelor-level degree types: BA, BS, Bachelor (unlabeled, used for Design studio programs and Social Work), and AAS (Associate of Applied Science via the 2-year Agricultural Institute). Admissions is centralized through the Office of Undergraduate Admissions at admissions.ncsu.edu; the College of Engineering, College of Design (studio-based), Wilson College of Textiles (Fashion and Textile Design), and College of Education (Music Technology) have program-specific supplemental requirements. First-year applicants select two majors from different academic colleges; transfer applicants may declare a single major. The full school → department hierarchy is in §0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> 来源: NC State Catalog 2026-2027 — https://catalog.ncsu.edu/find-your-program/ 与 https://catalog.ncsu.edu/undergraduate/。共 246 个 BS/BA/Bachelor 项目 + 7 个 AAS (Agricultural Institute),分布于 12 个学院。每一行 = 一个 catalog 程序入口 (concentration 视为独立入口)。

#### College of Agriculture and Life Sciences

##### Agricultural Human Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-agricultural-business-concentration/ |
| 2 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-agricultural-engineering-technology-concentration/ |
| 3 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-agronomy-concentration/ |
| 4 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-animal-science-concentration/ |
| 5 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-horticultural-science-concentration/ |
| 6 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-natural-resources-concentration/ |
| 7 | Agricultural Education (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-education-bs-poultry-science-concentration/ |
| 8 | Agricultural Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-science-bs/ |
| 9 | Agricultural Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-science-bs-online/ |

##### Agricultural Resource Economics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Business Management (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-resource-economics/agricultural-business-management-bs/ |
| 2 | Agricultural Business Management (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-resource-economics/agricultural-business-management-bs-biological-sciences-concentration/ |

##### Animal Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/animal-science/animal-science-bs-industry-concentration/ |
| 2 | Animal Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/animal-science/animal-science-bs-science-concentration/ |
| 3 | Animal Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/animal-science/animal-science-bs-veterinary-bioscience-concentration/ |

##### Biological Agricultural Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological and Agricultural Engineering Technology (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-technology-bs/ |
| 2 | Biological and Agricultural Engineering Technology (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-technology-bs-agricultural-systems-management-concentration/ |
| 3 | Biological and Agricultural Engineering Technology (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-technology-bs-environmental-systems-management-concentration/ |
| 4 | Biological Engineering (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-engineering-bs-agricultural-engineering-concentration/ |
| 5 | Biological Engineering (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-engineering-bs-bioprocessing-engineering-concentration/ |
| 6 | Biological Engineering (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-engineering-bs-ecological-engineering-concentration/ |
| 7 | Biological Engineering (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-engineering-bs-environmental-engineering-concentration/ |
| 8 | Biological, Agricultural, and Ecological Engineering (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/biological-engineering-bs/ |

##### Crop Soil Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agroecology & Sustainable Food Systems (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/agroecology-sustainable-food-systems-bs-agroecology-research-production-concentration/ |
| 2 | Agroecology & Sustainable Food Systems (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/agroecology-sustainable-food-systems-bs-community-food-systems-concentration/ |
| 3 | Crop and Soil Sciences (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/crop-soil-sciences-bs-agronomy/ |
| 4 | Crop and Soil Sciences (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/crop-soil-sciences-bs-crop-biotechnology-semester/ |
| 5 | Crop and Soil Sciences (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/crop-soil-sciences-bs-soil-science/ |
| 6 | Crop and Soil Sciences (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/turfgrass-science-bs/ |
| 7 | Natural Resources (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/natural-resources-bs-soil-water-land-use-concentration/ |

##### Food Bioprocessing Nutrition Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Bioprocessing Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/bioprocessing-science-bs/ |
| 2 | Food Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/food-science-bs-science-concentration/ |
| 3 | Nutrition Sciences (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/nutrition-sciences-bs/ |
| 4 | Nutrition Sciences (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/nutrition-sciences-bs-applied-nutrition-concentration/ |

##### Horticultural Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agroecology & Sustainable Food Systems (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/horticultural-science/agroecology-sustainable-food-systems-bs-urban-horticulture-concentration/ |
| 2 | Horticultural Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/horticultural-science/horticultural-science-bs-landscape-design-construction-management-concentration/ |
| 3 | Horticultural Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/horticultural-science/horticultural-science-bs-plant-breeding-biotechnology-horticulture-concentration/ |
| 4 | Horticultural Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/horticultural-science/horticultural-science-bs-production-systems-entrepreneurship-horticulture-concentration/ |

##### Life Sciences First Year

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Life Sciences First Year | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/life-sciences-first-year/ |

##### Molecular Structural Biochemistry

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/molecular-structural-biochemistry/biochemistry-bs/ |

##### Plant Microbial Biology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Plant Biology (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/plant-microbial-biology/plant-biology-bs/ |

##### Poultry Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Poultry Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/poultry-science/poultry-science-bs-science-concentration/ |
| 2 | Poultry Science (BS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/poultry-science/poultry-science-bs-technology-concentration/ |

#### College of Design

##### Architecture

###### Bachelor

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture (Bachelor) | https://catalog.ncsu.edu/undergraduate/design/architecture/architecture-bachelor/ |
| 2 | Environmental Design in Architecture (Bachelor) | https://catalog.ncsu.edu/undergraduate/design/architecture/environmental-design-architecture-bachelor/ |

##### Art Design

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Design Studies (BA) | https://catalog.ncsu.edu/undergraduate/design/art-design/design-studies-ba/ |
| 2 | Design Studies (BA) | https://catalog.ncsu.edu/undergraduate/design/art-design/design-studies-ba-business-administration-concentration/ |
| 3 | Design Studies (BA) | https://catalog.ncsu.edu/undergraduate/design/art-design/design-studies-ba-nonprofit-studies-concentration/ |

###### Bachelor

| # | 专业 | URL |
|---|------|-----|
| 1 | Media Arts, Design and Technology (Bachelor) | https://catalog.ncsu.edu/undergraduate/design/art-design/art-design-bachelor/ |

##### Graphic Industrial Design

###### Bachelor

| # | 专业 | URL |
|---|------|-----|
| 1 | Graphic & Experience Design (Bachelor) | https://catalog.ncsu.edu/undergraduate/design/graphic-industrial-design/graphic-design-bachelor/ |
| 2 | Industrial Design (Bachelor) | https://catalog.ncsu.edu/undergraduate/design/graphic-industrial-design/industrial-design-bachelor/ |

#### College of Education

##### Stem

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics Education (BS) and Mathematics (BS) (Double Major) | https://catalog.ncsu.edu/undergraduate/education/stem/mathematics-education-bs-mathematics-bs-double-major/ |
| 2 | Mathematics Education (BS) and Statistics (BS) (Double Major) | https://catalog.ncsu.edu/undergraduate/education/stem/mathematics-education-bs-statistics-bs-double-major/ |
| 3 | Mathematics Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/mathematics-education-bs-computer-specialization/ |
| 4 | Mathematics Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/mathematics-education-bs-mathematics-specialization/ |
| 5 | Mathematics Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/mathematics-education-bs-middle-grades-mathematics-concentration/ |
| 6 | Mathematics Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/mathematics-education-bs-statistics-specialization/ |
| 7 | Middle Grades Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/middle-grades-education-bs-mathematics-sciences-concentration/ |
| 8 | Science Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/science-education-bs-biology-concentration/ |
| 9 | Science Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/science-education-bs-chemistry-concentration/ |
| 10 | Science Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/science-education-bs-earth-science-concentration/ |
| 11 | Science Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/science-education-bs-middle-grades-science-concentration/ |
| 12 | Science Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/science-education-bs-physics-concentration/ |
| 13 | Technology, Engineering and Design Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/technology-engineering-design-education-bs-graphic-communication-concentration/ |
| 14 | Technology, Engineering and Design Education (BS) | https://catalog.ncsu.edu/undergraduate/education/stem/technology-engineering-design-education-bs-licensure-concentration/ |

##### Teacher Education Learning Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education (BS) | https://catalog.ncsu.edu/undergraduate/education/teacher-education-learning-sciences/elementary-education-bs-science-technology-engineering-mathematics-concentration/ |
| 2 | Middle Grades Education (BS) | https://catalog.ncsu.edu/undergraduate/education/teacher-education-learning-sciences/middle-grades-education-bs-language-arts-social-studies-concentration/ |

#### College of Engineering

##### Biomedical

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/biomedical/biomedical-engineering-bs/ |

##### Chemical Biomolecular

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs/ |
| 2 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs-biomanufacturing-sciences-concentration/ |
| 3 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs-biomolecular-concentration/ |
| 4 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs-textile-dual-major/ |
| 5 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs-honors-concentration/ |
| 6 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs-nanoscience-concentration/ |
| 7 | Chemical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-bs-sustainable-engineering-energy-environment/ |

##### Civil Construction Environmental

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/civil-construction-environmental/civil-engineering-bs/ |
| 2 | Construction Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/civil-construction-environmental/construction-engineering-bs/ |
| 3 | Environmental Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/civil-construction-environmental/environmental-engineering-bs/ |

##### Computer Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (BS) | https://catalog.ncsu.edu/undergraduate/engineering/computer-science/computer-science-bs/ |
| 2 | Computer Science (BS) | https://catalog.ncsu.edu/undergraduate/engineering/computer-science/artificial-intelligence-concentration/ |
| 3 | Computer Science (BS) | https://catalog.ncsu.edu/undergraduate/engineering/computer-science/computer-science-bs-cybersecurity-concentration/ |
| 4 | Computer Science (BS) | https://catalog.ncsu.edu/undergraduate/engineering/computer-science/computer-science-bs-game-development-concentration/ |

##### Electrical Computer

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/computer-engineering-bs/ |
| 2 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/computer-engineering-ai-machine-learning-concentration-bs/ |
| 3 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/computer-engineering-computer-architecture-emerging-systems-concentration-bs/ |
| 4 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/computer-engineering-computer-systems-software-concentration-bs/ |
| 5 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/computer-engineering-embedded-systems-concentration-bs/ |
| 6 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/networking-hardware-concentration-bs/ |
| 7 | Computer Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/networking-software-concentration-bs/ |
| 8 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs/ |
| 9 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-analog-circuits-concentration/ |
| 10 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-ai-machine-learning-concentration/ |
| 11 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-biomedical-instrumentation-concentration/ |
| 12 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-communications-signal-processing-concentration/ |
| 13 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-controls-robotics-concentration/ |
| 14 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-digital-circuits-concentration/ |
| 15 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-electronic-devices-concentration/ |
| 16 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-music-technology-concentration/ |
| 17 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-optics-photonics-concentration/ |
| 18 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-power-systems-concentration/ |
| 19 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-radio-frequency-circuits-concentration/ |
| 20 | Electrical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/electrical-computer/electrical-engineering-bs-renewable-electric-energy-systems-concentration/ |

##### Engineering Bs Mechatronics Concentration

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/engineering-bs-mechatronics-concentration/ |

##### Engineering Havelock

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/engineering-havelock/engineering-bs-electrical-engineering-systems-concentration/ |
| 2 | Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/engineering-havelock/engineering-bs-mechanical-engineering-systems-concentration/ |

##### Industrial Systems

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/industrial-systems/industrial-engineering-bs/ |

##### Materials Science Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/materials-science-engineering/materials-science-engineering-bs/ |
| 2 | Materials Science and Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/materials-science-engineering/materials-science-engineering-bs-biomaterials-concentration/ |
| 3 | Materials Science and Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/materials-science-engineering/materials-science-engineering-bs-nanomaterials-concentration/ |

##### Mechanical Aerospace

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/mechanical-aerospace/aerospace-engineering-bs/ |
| 2 | Mechanical Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/mechanical-aerospace/mechanical-engineering-bs/ |

##### Nuclear

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/nuclear/nuclear-engineering-bs/ |
| 2 | Nuclear Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/nuclear/nuclear-engineering-bs-nuclear-fuels-materials-concentration/ |
| 3 | Nuclear Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/nuclear/nuclear-engineering-bs-plasma-sciences-fusion-energy-concentration/ |
| 4 | Nuclear Engineering (BS) | https://catalog.ncsu.edu/undergraduate/engineering/nuclear/nuclear-engineering-bs-radiological-engineering-concentration/ |

#### College of Humanities and Social Sciences

##### Communication

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Communication (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/communication/communication-ba/ |

##### English

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | English (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-ba-creative-writing-concentration/ |
| 2 | English (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-ba-film-concentration/ |
| 3 | English (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-ba-linguistics-concentration/ |
| 4 | English (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-ba-literature-concentration/ |
| 5 | English (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-ba-language-writing-rhetoric-concentration/ |
| 6 | English (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-ba-teacher-education-concentration/ |

##### History

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | History (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/history/history-ba/ |
| 2 | History (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/history/history-ba-legal-history-concentration/ |
| 3 | History (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/history/history-ba-teacher-education-concentration/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | History (BS) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/history/history-bs/ |

##### Interdisciplinary

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Arts Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/arts-studies-program/arts-studies-ba-film-studies-concentration/ |
| 2 | Arts Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/arts-studies-program/arts-studies-ba-music-concentration/ |
| 3 | Arts Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/arts-studies-program/arts-studies-ba-theater-concentration/ |
| 4 | Arts Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/arts-studies-program/arts-studies-ba-visual-arts-concentration/ |
| 5 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-africa-concentration/ |
| 6 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-east-southeast-asia-concentration/ |
| 7 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-europe-concentration/ |
| 8 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-global-cultural-studies/ |
| 9 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-global-relations/ |
| 10 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-global-sustainability-development/ |
| 11 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-latin-america-concentration/ |
| 12 | International Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-ba-south-asia-middle-east-concentration/ |
| 13 | Science, Technology and Society (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/science-technology-society-program/science-technology-society-ba/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Science, Technology and Society (BS) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/science-technology-society-program/science-technology-society-bs/ |

##### Philosophy Religious Studies

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-ba/ |
| 2 | Philosophy (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-ba-philosophy-ethics-concentration/ |
| 3 | Philosophy (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-ba-philosophy-law-concentration/ |
| 4 | Religious Studies (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/religious-studies-ba/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy (BS) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-bs/ |
| 2 | Philosophy (BS) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-bs-logic-representation-reasoning-concentration/ |

##### Political Science

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Leadership in the Public Sector (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/leadership-public-sector-ba-de/ |
| 2 | Political Science (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-ba/ |
| 3 | Political Science (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-ba-american-politics-concentration/ |
| 4 | Political Science (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-ba-international-politics-concentration/ |
| 5 | Political Science (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-ba-law-justice-concentration/ |
| 6 | Political Science (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-ba-public-policy-concentration/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science (BS) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-bs/ |

##### Psychology

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/psychology/psychology-ba-general-psychology-concentration/ |

##### Social Work

###### Bachelor

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work (Bachelor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/social-work/social-work-bachelor/ |

##### Sociology Anthropology

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/anthropology-ba-general-anthropology-concentration/ |
| 2 | Criminology (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/criminology-ba/ |
| 3 | Sociology (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/sociology-ba/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology (BS) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/sociology-bs/ |

##### World Languages Cultures

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-arabic-language-culture-concentration/ |
| 2 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-asian-language-concentration/ |
| 3 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-foreign-language-chinese-education-concentration/ |
| 4 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-foreign-language-french-education-concentration/ |
| 5 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-french-studies-concentration/ |
| 6 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-foreign-language-german-education-concentration/ |
| 7 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-german-studies-concentration/ |
| 8 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-german-studies-international-economics-concentration/ |
| 9 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-german-studies-science-technology-concentration/ |
| 10 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-foreign-language-spanish-education-concentration/ |
| 11 | World Languages and Cultures (BA) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/foreign-languages-literatures-ba-spanish-language-literature-concentration/ |

#### Poole College of Management

##### Accounting

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting (BS) | https://catalog.ncsu.edu/undergraduate/management/accounting/accounting-bs/ |

##### Economics

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics (BA) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-ba/ |
| 2 | Economics (BA) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-ba-business-analytics-concentration/ |
| 3 | Economics (BA) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-ba-finance-concentration/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics (BS) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-bs/ |
| 2 | Economics (BS) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-bs-business-analytics-concentration/ |
| 3 | Economics (BS) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-bs-finance-concentration/ |

#### College of Natural Resources

##### Environmental First Year Program

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental First Year Program | https://catalog.ncsu.edu/undergraduate/natural-resources/environmental-first-year-program/ |

##### Forest Biomaterials

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Paper Science and Engineering (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/paper-science-engineering-bs/ |
| 2 | Paper Science and Engineering (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/paper-science-engineering-bs-dual-major/ |
| 3 | Paper Science and Engineering (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/paper-science-engineering-bs-sustainable-packaging-production-concentration/ |
| 4 | Sustainable Materials and Technology (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/sustainable-materials-technology-bs/ |
| 5 | Sustainable Materials and Technology (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/sustainable-materials-technology-bs-smt-wood-products-concentration/ |
| 6 | Sustainable Materials and Technology (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/sustainable-materials-technology-bs-sustainable-packaging-concentration/ |

##### Forestry Environmental Resources

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Sciences (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/environmental-sciences-bs/ |
| 2 | Environmental Technology and Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/environmental-technology-management-bs/ |
| 3 | Fisheries, Wildlife, and Conservation Biology (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/fisheries-wildlife-conservation-biology-bs-conservation-biology-concentration/ |
| 4 | Fisheries, Wildlife, and Conservation Biology (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/fisheries-wildlife-conservation-biology-bs-fisheries-science-concentration/ |
| 5 | Fisheries, Wildlife, and Conservation Biology (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/fisheries-wildlife-conservation-biology-bs-wildlife-science-concentration/ |
| 6 | Forest Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/forest-management-bs-ecology-concentration/ |
| 7 | Forest Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/forest-management-bs-production-concentration/ |
| 8 | Natural Resources (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/natural-resources-bs-ecosystem-assessment-concentration/ |
| 9 | Natural Resources (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/natural-resources-bs-policy-administration-concentration/ |

##### Parks Recreation Tourism Management

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Parks, Recreation and Tourism Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/parks-recreation-tourism-management/parks-recreation-tourism-management-bs-parks-natural-resource-recreation-concentration/ |
| 2 | Parks, Recreation, and Tourism Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/parks-recreation-tourism-management/parks-recreation-tourism-management-bs-sustainable-tourism-concentration/ |
| 3 | Sport Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/parks-recreation-tourism-management/sport-management-bs/ |
| 4 | Sport Management (BS) | https://catalog.ncsu.edu/undergraduate/natural-resources/parks-recreation-tourism-management/sport-management-bs-professional-golf-management/ |

#### College of Sciences

##### Biological Sciences

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences (BA) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-ba/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-bs/ |
| 2 | Biological Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-bs-ecology-evolution-conservation-biology-concentration/ |
| 3 | Biological Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-bs-human-biology-concentration/ |
| 4 | Biological Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-bs-integrative-physiology-neurobiology-concentration/ |
| 5 | Biological Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-bs-molecular-cellular-developmental-biology-concentration/ |
| 6 | Genetics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/genetics-bs/ |
| 7 | Microbiology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/microbiology-bs/ |
| 8 | Microbiology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/microbiology-bs-microbial-biotechnology/ |
| 9 | Microbiology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/microbiology-bs-microbial-health-science/ |
| 10 | Microbiology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/microbiology-bs-microbial-research/ |
| 11 | Zoology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/zoology-bs/ |
| 12 | Zoology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/zoology-bs-applied-zoology/ |

##### Chemistry

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry (BA) | https://catalog.ncsu.edu/undergraduate/sciences/chemistry/chemistry-ba/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry (BS) | https://catalog.ncsu.edu/undergraduate/sciences/chemistry/chemistry-bs/ |

##### Environmental First Year Program

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental First Year Program | https://catalog.ncsu.edu/undergraduate/sciences/environmental-first-year-program/ |

##### Life Sciences First Year

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Life Sciences First Year | https://catalog.ncsu.edu/undergraduate/sciences/life-sciences-first-year/ |

##### Marine Earth Atmospheric Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Geology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/geology-bs/ |
| 2 | Marine Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/marine-sciences-bs-biological-oceanography-concentration/ |
| 3 | Marine Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/marine-sciences-bs-chemistry-concentration/ |
| 4 | Marine Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/marine-sciences-bs-geology-concentration/ |
| 5 | Marine Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/marine-sciences-bs-meteorology-concentration/ |
| 6 | Marine Sciences (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/marine-sciences-bs-physics-concentration/ |
| 7 | Meteorology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/meteorology-bs/ |
| 8 | Meteorology (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/meteorology-bs-marine-sciences-concentration/ |
| 9 | Natural Resources (BS) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/natural-resources-bs-marine-coastal-concentration/ |

##### Mathematics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/mathematics/applied-mathematics-bs/ |
| 2 | Applied Mathematics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/mathematics/applied-mathematics-bs-financial-mathematics-concentration/ |
| 3 | Applied Mathematics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/mathematics/applied-mathematics-bs-mathematical-foundations-data-science-concentration/ |
| 4 | Mathematics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/mathematics/mathematics-bs/ |

##### Physics

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics (BA) | https://catalog.ncsu.edu/undergraduate/sciences/physics/physics-ba/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/physics/physics-bs/ |

##### Statistics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/statistics/statistics-bs/ |
| 2 | Statistics (BS) | https://catalog.ncsu.edu/undergraduate/sciences/statistics/statistics-bs-data-science-concentration/ |

#### Wilson College of Textiles

##### Textile Apparel Technology Management

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion and Textile Design (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-apparel-technology-management/fashion-textile-design-bs-fashion-design-concentration/ |
| 2 | Fashion and Textile Design (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-apparel-technology-management/fashion-textile-design-bs-textile-design-concentration/ |
| 3 | Fashion and Textile Management (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-apparel-technology-management/fashion-textile-management-bs-brand-management-marketing-concentration/ |
| 4 | Fashion and Textile Management (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-apparel-technology-management/fashion-textile-management-bs-fashion-development-product-management-concentration/ |

##### Textile Engineering Chemistry Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Polymer and Color Chemistry (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/polymer-color-chemistry-bs-acs-certification-concentration/ |
| 2 | Polymer and Color Chemistry (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/polymer-color-chemistry-bs-medical-sciences-concentration/ |
| 3 | Polymer and Color Chemistry (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/polymer-color-chemistry-bs-science-operations-concentration/ |
| 4 | Textile Engineering (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-engineering-bs-chemical-processing-concentration/ |
| 5 | Textile Engineering (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-engineering-bs-information-systems-concentration/ |
| 6 | Textile Engineering (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-engineering-bs-product-engineering-concentration/ |
| 7 | Textile Technology (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-technology-bs/ |
| 8 | Textile Technology (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-technology-bs-medical-textiles-concentration/ |
| 9 | Textile Technology (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-technology-bs-supply-chain-operations-concentration/ |
| 10 | Textile Technology (BS) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-technology-bs-technical-textiles-concentration/ |

#### University College

##### Music

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Music Technology (BS) | https://catalog.ncsu.edu/undergraduate/university-college/music/music-technology-bs/ |

##### University Advising Exploratory Studies

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Exploratory Studies | https://catalog.ncsu.edu/undergraduate/university-college/university-advising-exploratory-studies/exploratory-studies/ |

### 1.4 Minors — complete list (134 minors)

> 来源: https://catalog.ncsu.edu/undergraduate/ 中的 Minors 节点 (其中 134 个 UG Minor 入口)。

#### College of Agriculture and Life Sciences (21 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Agricultural Business Management (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-resource-economics/agricultural-business-management-minor/ |
| 2 | Agricultural Entrepreneurship (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-resource-economics/agricultural-entrepreneurship-minor/ |
| 3 | Agroecology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/agroecology-minor/ |
| 4 | Animal Science (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/animal-science/animal-science-minor/ |
| 5 | Applied Ecology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/applied-ecology/applied-ecology-minor/ |
| 6 | Biological and Agricultural Engineering Technology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/biological-agricultural-engineering/agricultural-environmental-technology-minor/ |
| 7 | Biotechnology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/plant-microbial-biology/biotechnology-minor/ |
| 8 | Brewing Science and Technology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/brewing-science-technology-minor/ |
| 9 | Crop Science (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/crop-science-minor/ |
| 10 | Entomology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/entomology-plant-pathology/entomology-minor/ |
| 11 | Extension Education (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/extension-education-minor/ |
| 12 | Feed Milling (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/poultry-science/feed-milling-minor/ |
| 13 | Food Science (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/food-science-minor/ |
| 14 | Horticultural Science (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/horticultural-science/horticultural-science-minor/ |
| 15 | Leadership in Agriculture and Life Sciences (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/leadership-agriculture-life-sciences-minor/ |
| 16 | Nutrition (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/nutrition-minor/ |
| 17 | Plant Biology (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/plant-microbial-biology/plant-biology-minor/ |
| 18 | Poultry Science (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/poultry-science/poultry-science-minor/ |
| 19 | Regulatory Science in Agriculture (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/ag-regulatory-science-minor/ |
| 20 | Soil Science (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/soil-science-minor/ |
| 21 | Turfgrass (Minor) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/turfgrass-minor/ |

#### College of Design (2 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Art and Design (Minor) | https://catalog.ncsu.edu/undergraduate/design/art-design/art-design-minor/ |
| 2 | Landscape Architecture (Minor) | https://catalog.ncsu.edu/undergraduate/design/landscape-architecture/landscape-architecture-minor/ |

#### College of Education (2 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Graphic Communications (Minor) | https://catalog.ncsu.edu/undergraduate/education/stem/graphic-communications-minor/ |
| 2 | Technology, Engineering and Design Education (Minor) | https://catalog.ncsu.edu/undergraduate/education/stem/technology-engineering-design-education-minor/ |

#### College of Engineering (11 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Biomanufacturing (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/biomanufacturing-minor/ |
| 2 | Chemical Engineering (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/chemical-engineering-minor/ |
| 3 | Computer Programming (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/computer-science/computer-programming-minor/ |
| 4 | Engineering Education (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/engineering-education-minor/ |
| 5 | Health Physics (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/nuclear/health-physics-minor/ |
| 6 | Industrial Engineering (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/industrial-systems/industrial-engineering-minor/ |
| 7 | Materials Science and Engineering (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/materials-science-engineering/materials-science-engineering-minor/ |
| 8 | Nano-Science and Technology (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/nano-science-technology-minor/ |
| 9 | Nuclear Engineering (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/nuclear/nuclear-engineering-minor/ |
| 10 | Supply Chain Engineering (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/industrial-systems/supply-chain-engineering-minor/ |
| 11 | Tissue Engineering (Minor) | https://catalog.ncsu.edu/undergraduate/engineering/biomedical/tissue-engineering-minor/ |

#### College of Humanities and Social Sciences (45 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Africana Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/africana-studies-program/africana-studies-minor/ |
| 2 | American Literature (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/american-literature-minor/ |
| 3 | Anthropology (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/anthropology-minor/ |
| 4 | Arts Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/arts-studies-program/arts-studies-minor/ |
| 5 | Chinese Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/chinese-studies-minor/ |
| 6 | Classical Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/classical-studies-minor/ |
| 7 | Cognitive Science (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/cognitive-science-minor/ |
| 8 | Creative Writing (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/creative-writing-minor/ |
| 9 | Criminology (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/criminology-minor/ |
| 10 | English (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/english-minor/ |
| 11 | Ethics (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/ethics-minor/ |
| 12 | Film Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/film-studies-minor/ |
| 13 | French (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/french-minor/ |
| 14 | German (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/german-minor/ |
| 15 | Health, Medicine and Human Values (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/health-medicine-human-values-minor/ |
| 16 | Hindi-Urdu (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/hindi-urdu-minor/ |
| 17 | History (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/history/history-minor/ |
| 18 | International Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/international-studies-program/international-studies-minor/ |
| 19 | Italian Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/italian-studies-minor/ |
| 20 | Japan Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/japan-studies-minor/ |
| 21 | Japanese (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/japanese-minor/ |
| 22 | Jewish Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/jewish-studies-minor/ |
| 23 | Journalism (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/journalism-minor/ |
| 24 | Law and Justice (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/law-justice-minor/ |
| 25 | Linguistics (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/linguistics-minor/ |
| 26 | Logic and Methodology (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/logic-methodology-minor/ |
| 27 | Native American Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/native-american-studies-minor/ |
| 28 | Nonprofit Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/nonprofit-studies-minor/ |
| 29 | Philosophy (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-minor/ |
| 30 | Philosophy of Law (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/philosophy-law-minor/ |
| 31 | Philosophy, Politics, and Economics (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/philosophy-politics-economics-minor/ |
| 32 | Political Science (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/political-science-minor/ |
| 33 | Portuguese Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/portuguese-studies-minor/ |
| 34 | Psychology (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/psychology/psychology-minor/ |
| 35 | Religious Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/philosophy-religious-studies/religious-studies-minor/ |
| 36 | Rhetoric, Writing, and Professional Communication (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/rhetoric-writing-professional-communication-minor/ |
| 37 | Russian Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/russian-studies-minor/ |
| 38 | Science Communication (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/communication/science-communication-minor/ |
| 39 | Science, Technology, and Society (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/science-technology-society-program/science-technology-society-minor/ |
| 40 | Social Work (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/social-work/social-work-minor/ |
| 41 | Sociology (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/sociology-anthropology/sociology-minor/ |
| 42 | Spanish (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/spanish-minor/ |
| 43 | Teaching English as a Foreign Language (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/teaching-english-foreign-language-minor/ |
| 44 | Women’s, Gender and Sexuality Studies (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/womens-gender-studies-program/womens-gender-studies-minor/ |
| 45 | World Literatures and Cultures (Minor) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/world-literature-minor/ |

#### interdisciplinary (6 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Data Science in Business (Minor) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/data-science-business-minor/ |
| 2 | Data Science in Engineering Analytics and Decision-Making (Minor) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/data-science-analytics-decision-minor/ |
| 3 | Data Science in K-12 Education (Minor) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/data-science-k12-education-minor/ |
| 4 | Data Science with Graphic and Experience Design (Minor) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/data-science-graphic-experience-design-minor/ |
| 5 | Global One Health (Minor) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/global-one-health-minor/ |
| 6 | Mathematical Data Science (Minor) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/mathematical-data-science-minor/ |

#### Poole College of Management (3 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Accounting (Minor) | https://catalog.ncsu.edu/undergraduate/management/accounting/accounting-minor/ |
| 2 | Business Entrepreneurship (Minor) | https://catalog.ncsu.edu/undergraduate/management/mie/business-entrepreneurship-minor/ |
| 3 | Economics (Minor) | https://catalog.ncsu.edu/undergraduate/management/economics/economics-minor/ |

#### College of Natural Resources (10 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Environmental Education (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/parks-recreation-tourism-management/environmental-education-minor/ |
| 2 | Environmental Sciences (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/environmental-sciences-minor/ |
| 3 | Environmental Technology and Management (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/environmental-technology-management-minor/ |
| 4 | Forest Management (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/forest-management-minor/ |
| 5 | Parks, Recreation, and Tourism Management (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/parks-recreation-tourism-management/parks-recreation-tourism-management-minor/ |
| 6 | Pulp and Paper Technology (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/pulp-paper-technology-minor/ |
| 7 | Renewable Energy Assessment (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/renewable-energy-assessment-minor/ |
| 8 | Sustainable Materials and Technology (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forest-biomaterials/sustainable-materials-technology-minor/ |
| 9 | Wetland Assessment (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/wetland-assessment-minor/ |
| 10 | Wildlife Sciences (Minor) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/wildlife-sciences-minor/ |

#### College of Sciences (15 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Astrophysics (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/physics/astrophysics-minor/ |
| 2 | Biological Sciences (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/biological-sciences-minor/ |
| 3 | Evolutionary Biology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/evolutionary-biology-minor/ |
| 4 | Forensic Science (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/forensic-science-minor/ |
| 5 | Genetics (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/genetics-minor/ |
| 6 | Geology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/geology-minor/ |
| 7 | Marine Sciences (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/marine-science-minor/ |
| 8 | Mathematics (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/mathematics/mathematics-minor/ |
| 9 | Meteorology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/marine-earth-atmospheric-sciences/meteorology-minor/ |
| 10 | Microbiology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/microbiology-minor/ |
| 11 | Paleontology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/paleontology-minor/ |
| 12 | Physics (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/physics/physics-minor/ |
| 13 | Statistics (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/statistics/statistics-minor/ |
| 14 | Toxicology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/toxicology-minor/ |
| 15 | Zoology (Minor) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/zoology-minor/ |

#### Wilson College of Textiles (4 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Nonwovens (Minor) | https://catalog.ncsu.edu/undergraduate/textiles/nonwovens-minor/ |
| 2 | Polymer Science (Minor) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/polymer-science-minor/ |
| 3 | Polymer and Color Chemistry (Minor) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/polymer-color-chemistry-minor/ |
| 4 | Textile Technology (Minor) | https://catalog.ncsu.edu/undergraduate/textiles/textile-engineering-chemistry-science/textile-technology-minor/ |

#### University College (15 minors)

| # | Minor name | URL |
|---|------|-----|
| 1 | Arts Entrepreneurship (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/music/arts-entrepreneurship-minor/ |
| 2 | Coaching Education (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/health-exercise-studies/coaching-education-minor/ |
| 3 | Dance Performance and Choreography (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/music/dance-minor/ |
| 4 | Dance Studies (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/music/dance-studies-minor/ |
| 5 | Global Leadership and Team Decision-Making (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/global-leadership-team-decision-making-minor/ |
| 6 | Health (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/health-exercise-studies/health-minor/ |
| 7 | Leadership, Cross Disciplinary Perspectives (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/leadership-cross-disciplinary-perspectives-minor/ |
| 8 | Military Studies, Aerospace Studies (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/air-force-rotc/military-studies-aerospace-minor/ |
| 9 | Military Studies, Military Science (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/army-rotc/military-studies-science-minor/ |
| 10 | Military Studies, Naval Science (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/navy-rotc/military-studies-naval-science-minor/ |
| 11 | Music Performance (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/music/music-minor-performance/ |
| 12 | Music Studies (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/music/music-minor/ |
| 13 | Outdoor Leadership (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/health-exercise-studies/outdoor-leadership-minor/ |
| 14 | Sports Science (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/health-exercise-studies/sports-science-minor/ |
| 15 | Teamwork in Interdisciplinary Biomedical Research (Minor) | https://catalog.ncsu.edu/undergraduate/university-college/Teamwork-in-interdisciplinary-biomedical-research-minor/ |

### 1.5 Undergraduate Certificates — complete list (36 certificates)

> 来源: https://catalog.ncsu.edu/undergraduate/ 中的 Certificates 节点。

#### College of Agriculture and Life Sciences (14 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | Agribusiness Management (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/agribusiness-management-certificate-distance-education/ |
| 2 | Agricultural Business Management (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-resource-economics/agricultural-business-management-certificate-post-baccalaureate-students-distance-education/ |
| 3 | Agricultural Business Management (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-resource-economics/agricultural-business-management-certificate-distance-education/ |
| 4 | Agricultural Leadership (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-human-sciences/agricultural-leadership-certificate/ |
| 5 | Animal Nutrition (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/animal-science/animal-nutrition-certificate/ |
| 6 | Crop Science (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/crop-science-certificate-distance-education/ |
| 7 | Feed Milling (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/poultry-science/feed-milling-certificate/ |
| 8 | Field Botany (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/plant-microbial-biology/field-botany-certificate/ |
| 9 | Food Safety & Quality Management (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/food-bioprocessing-nutrition-science/food-safety-quality-management-certificate/ |
| 10 | Fundamentals of Entomology (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/entomology-plant-pathology/fundamentals-entomology-certificate/ |
| 11 | Horticulture (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/horticultural-science/horticulture-undergraduate-certificate/ |
| 12 | Plant Pests, Pathogens, and People (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/entomology-plant-pathology/plant-pests-pathogens-people-certificate/ |
| 13 | Regulatory Science in Agriculture (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/ag-regulatory-science-certificate/ |
| 14 | Soil Science (Certificate) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/crop-soil-sciences/soil-science-certificate/ |

#### College of Education (2 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | U.S. Culture and Cooperative Education (Certificate) | https://catalog.ncsu.edu/undergraduate/education/us-culture-cooperative-education-certificate/ |
| 2 | U.S. Culture and Education (Certificate) | https://catalog.ncsu.edu/undergraduate/education/us-culture-education-certificate/ |

#### College of Engineering (3 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | Biomanufacturing (Certificate) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/biomanufacturing-certificate/ |
| 2 | Biomanufacturing (Certificate) | https://catalog.ncsu.edu/undergraduate/engineering/chemical-biomolecular/biomanufacturing-certificate-post-baccalaureate/ |
| 3 | Computer Programming (Certificate) | https://catalog.ncsu.edu/undergraduate/engineering/computer-science/computer-programming-certificate-distance-education/ |

#### College of Humanities and Social Sciences (13 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | Advanced Critical and Creative Thinking (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/advanced-critical-creative-thinking-certificate/ |
| 2 | Arabic (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/arabic-certificate/ |
| 3 | Chinese (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/chinese-certificate/ |
| 4 | French (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/french-certificate/ |
| 5 | German (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/german-certificate/ |
| 6 | Interdisciplinary Scholars (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/interdisciplinary/interdisciplinary-studies/interdisciplinary-studies-alexander-hamilton-certificate/ |
| 7 | Italian Studies (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/italian-studies-certificate/ |
| 8 | Japanese (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/japanese-certificate/ |
| 9 | Latin (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/latin-certificate/ |
| 10 | Leadership in the Public Sector (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/political-science/leadership-public-sector-certificate/ |
| 11 | Professional Writing (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/english/professional-writing-certificate/ |
| 12 | Spanish (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/spanish-certificate/ |
| 13 | Teaching English to Speakers of Other Languages (Certificate) | https://catalog.ncsu.edu/undergraduate/humanities-social-sciences/world-languages-cultures/tesol-certificate/ |

#### interdisciplinary (2 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | Data Science in Business (Certificate) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/undergrad-cert-data-science-business/ |
| 2 | Data Science with Graphic and Experience Design (Certificate) | https://catalog.ncsu.edu/undergraduate/interdisciplinary/data-science-graphic-experience-design-cert/ |

#### College of Natural Resources (1 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | Renewable Energy Assessment (Certificate) | https://catalog.ncsu.edu/undergraduate/natural-resources/forestry-environmental-resources/renewable-energy-assessment-certificate/ |

#### College of Sciences (1 certificates)

| # | Certificate name | URL |
|---|------|-----|
| 1 | Microbiology (Certificate) | https://catalog.ncsu.edu/undergraduate/sciences/biological-sciences/microbiology-certificate/ |

### 1.6 Agricultural Institute — 2-year Associate of Applied Science (7 programs)

> 来源: https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/。

| # | Program | URL |
|---|------|-----|
| 1 | Agribusiness Management (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/agribusiness-management-aas/ |
| 2 | Field Crops Technology (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/field-crops-technology-aas/ |
| 3 | General Agriculture (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/general-agriculture-aas/ |
| 4 | Horticultural Science Management (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/horticultural-science-management-aas-ornamentals-landscape-technology-concentration/ |
| 5 | Horticultural Science Management (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/horticultural-science-management-aas-small-scale-farming-concentration/ |
| 6 | Livestock and Poultry Management (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/livestock-poultry-management-aas/ |
| 7 | Turfgrass Management (AAS) | https://catalog.ncsu.edu/undergraduate/agriculture-life-sciences/agricultural-institute/turfgrass-management-aas/ |

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> 来源: NC State Catalog 2026-2027 — https://catalog.ncsu.edu/graduate/ (Programs and Degrees 节点)。共 205 显式学位项目 (含 MS/MR/MA/MEd/PhD/EdD/MFA/PSM/DDes 等) + 63 graduate minors + 67 graduate certificates + 233 department-level landing pages,合计 568 研究生 catalog 入口。

#### Note on degree abbreviations

NC State awards a large share of master's degrees with the suffix  (Master of [discipline] — a research/professional master distinct from MS). 205 explicit-degree entries breakdown: 66 MS, 59 MR, 11 MEd, 6 MA, 1 MFA, 1 PSM, 1 DDes, 3 EDP-equivalents (EEMS, EDP, LDT), 2 MTSS, 53 PhD, 3 EdD. Other graduate programs (e.g., MBA, MR) are accessed via department landing pages; Business Administration is at https://catalog.ncsu.edu/graduate/management/business-administration/.

#### College of Agriculture and Life Sciences

##### Agricultural Education Human Sciences

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education and Human Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/agricultural-education-human-sciences-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education and Human Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/agricultural-education-human-sciences-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education and Human Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/agricultural-education-human-sciences-phd/ |

##### Animal Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-science/animal-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-science/animal-science-ms/ |

##### Biochemistry

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biochemistry/biochemistry-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biochemistry/biochemistry-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biochemistry/biochemistry-phd/ |

##### Biological Agricultural Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Biological and Agricultural Engineering | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biological and Agricultural Engineering | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biological and Agricultural Engineering | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-phd/ |

##### Biology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biology/biology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biology/biology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biology/biology-phd/ |

##### Crop Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Crop Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/crop-science/crop-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Crop Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/crop-science/crop-science-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Crop Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/crop-science/crop-science-phd/ |

##### Entomology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Entomology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/entomology/entomology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Entomology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/entomology/entomology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Entomology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/entomology/entomology-phd/ |

##### Food Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Food Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/food-science/food-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Food Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/food-science/food-science-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Food Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/food-science/food-science-phd/ |

##### Horticultural Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Horticultural Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/horticultural-science/horticultural-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Horticultural Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/horticultural-science/horticultural-science-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Horticultural Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/horticultural-science/horticultural-science-phd/ |

##### Microbial Biotechnology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Microbial Biotechnology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/microbial-biotechnology/microbial-biotechnology-mr/ |

##### Microbiology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/microbiology/microbiology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/microbiology/microbiology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/microbiology/microbiology-phd/ |

##### Nutrition

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Nutrition | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/nutrition/nutrition-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Nutrition | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/nutrition/nutrition-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Nutrition | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/nutrition/nutrition-phd/ |

##### Physiology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Physiology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/physiology/physiology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Physiology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/physiology/physiology-ms/ |

##### Plant Biology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-biology/plant-biology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-biology/plant-biology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-biology/plant-biology-phd/ |

##### Plant Pathology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Pathology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-pathology/plant-pathology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Pathology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-pathology/plant-pathology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Pathology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-pathology/plant-pathology-phd/ |

##### Poultry Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Poultry Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/poultry-science/poultry-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Poultry Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/poultry-science/poultry-science-ms/ |

##### Soil Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Soil Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/soil-science/soil-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Soil Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/soil-science/soil-science-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Soil Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/soil-science/soil-science-phd/ |

#### College of Design

##### Architecture

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Architectural Studies | https://catalog.ncsu.edu/graduate/design/architecture/advanced-architectural-studies-mr/ |
| 2 | Architecture | https://catalog.ncsu.edu/graduate/design/architecture/architecture-mr/ |

##### Art Design

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Art and Design | https://catalog.ncsu.edu/graduate/design/art-design/art-design-mr/ |

##### Design

###### DDes

| # | 项目 | URL |
|---|------|-----|
| 1 | Design | https://catalog.ncsu.edu/graduate/design/design/design-ddes/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Design | https://catalog.ncsu.edu/graduate/design/design/design-phd/ |

##### Graphic Design

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Graphic and Experience Design | https://catalog.ncsu.edu/graduate/design/graphic-design/graphic-design-mr/ |

##### Industrial Design

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Design | https://catalog.ncsu.edu/graduate/design/industrial-design/industrial-design-mr/ |

##### Landscape Architecture

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://catalog.ncsu.edu/graduate/design/landscape-architecture/landscape-architecture-mr/ |

#### College of Education

##### Adult Community College Education

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Adult and Community College Education | https://catalog.ncsu.edu/graduate/education/adult-community-college-education/adult-community-college-education-med/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Adult and Community College Education | https://catalog.ncsu.edu/graduate/education/adult-community-college-education/adult-community-college-education-ms/ |

##### Clinical Mental Health Counseling

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://catalog.ncsu.edu/graduate/education/clinical-mental-health-counseling/clinical-mental-health-counseling-med/ |

##### College Counseling Student Development

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | College Counseling and Student Development | https://catalog.ncsu.edu/graduate/education/college-counseling-student-development/college-counseling-student-development-med/ |

##### Community College Leadership

###### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Community College Leadership | https://catalog.ncsu.edu/graduate/education/community-college-leadership/community-college-leadership-edd/ |

##### Educational Leadership

###### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | https://catalog.ncsu.edu/graduate/education/educational-leadership/educational-leadership-edd/ |

##### Educational Leadership Policy Human Development

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership, Policy, and Human Development | https://catalog.ncsu.edu/graduate/education/educational-leadership-policy-human-development/educational-leadership-policy-human-development-phd/ |

##### Elementary Education

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.ncsu.edu/graduate/education/elementary-education/elementary-education-med/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.ncsu.edu/graduate/education/elementary-education/elementary-education-ms/ |

##### Higher Education Administration

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education Administration | https://catalog.ncsu.edu/graduate/education/higher-education-administration/higher-education-administration-med/ |

##### Learning Design Technology

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Learning Design & Technology | https://catalog.ncsu.edu/graduate/education/learning-design-technology/learning-design-technology-med/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Learning Design & Technology | https://catalog.ncsu.edu/graduate/education/learning-design-technology/learning-design-technology-ms/ |

##### Learning Teaching Stem

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Learning and Teaching in STEM | https://catalog.ncsu.edu/graduate/education/learning-teaching-stem/learning-teaching-stem-phd/ |

##### School Administration

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | School Administration | https://catalog.ncsu.edu/graduate/education/school-administration/school-administration-mr/ |

##### School Counseling

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | School Counseling | https://catalog.ncsu.edu/graduate/education/school-counseling/school-counseling-med/ |

##### Science Technology Engineering Mathematics Education

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Science, Technology, Engineering, and Mathematics Education | https://catalog.ncsu.edu/graduate/education/science-technology-engineering-mathematics-education/science-technology-engineering-mathematics-education-med/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Science, Technology, Engineering, and Mathematics Education | https://catalog.ncsu.edu/graduate/education/science-technology-engineering-mathematics-education/science-technology-engineering-mathematics-education-ms/ |

##### Special Education

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Special Education | https://catalog.ncsu.edu/graduate/education/special-education/special-education-med/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Special Education | https://catalog.ncsu.edu/graduate/education/special-education/special-education-ms/ |

###### MTSS

| # | 项目 | URL |
|---|------|-----|
| 1 | Special Education (Certificate): Multi-Tiered System of Supports | https://catalog.ncsu.edu/graduate/education/special-education/special-education-certificate/ |

##### Teacher Education Learning Sciences

###### EDP

| # | 项目 | URL |
|---|------|-----|
| 1 | Teacher Education and Learning Science (PhD): Educational Psychology | https://catalog.ncsu.edu/graduate/education/teacher-education-learning-sciences/educational-psychology/ |

###### EEMS

| # | 项目 | URL |
|---|------|-----|
| 1 | Teacher Education and Learning Science (PhD): Elementary Education in Mathematics and Science | https://catalog.ncsu.edu/graduate/education/teacher-education-learning-sciences/elementary-education-in-mathematics-and-science/ |

###### LDT

| # | 项目 | URL |
|---|------|-----|
| 1 | Teacher Education and Learning Science (PhD): Learning Design and Technology | https://catalog.ncsu.edu/graduate/education/teacher-education-learning-sciences/learning-design-and-technology/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Teacher Education and Learning Sciences | https://catalog.ncsu.edu/graduate/education/teacher-education-learning-sciences/teacher-education-learning-sciences-phd/ |

##### Teaching

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching | https://catalog.ncsu.edu/graduate/education/teaching/teaching-ma/ |

##### Teaching Learning Curriculum

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching, Learning, and Curriculum | https://catalog.ncsu.edu/graduate/education/teaching-learning-curriculum/teaching-learning-curriculum-med/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching, Learning and Curriculum | https://catalog.ncsu.edu/graduate/education/teaching-learning-curriculum/teaching-learning-curriculum-ms/ |

##### Technology Education

###### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Technology Education | https://catalog.ncsu.edu/graduate/education/technology-education/technology-education-edd/ |

##### Training Development

###### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Training & Development | https://catalog.ncsu.edu/graduate/education/training-development/training-development-med/ |

#### College of Engineering

##### Aerospace Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.ncsu.edu/graduate/engineering/aerospace-engineering/aerospace-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.ncsu.edu/graduate/engineering/aerospace-engineering/aerospace-engineering-phd/ |

##### Biomanufacturing

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomanufacturing | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/biomanufacturing-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomanufacturing | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/biomanufacturing-ms/ |

##### Biomedical Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/biomedical-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/biomedical-engineering-phd/ |

##### Chemical Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.ncsu.edu/graduate/engineering/chemical-engineering/chemical-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.ncsu.edu/graduate/engineering/chemical-engineering/chemical-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.ncsu.edu/graduate/engineering/chemical-engineering/chemical-engineering-phd/ |

##### Civil Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.ncsu.edu/graduate/engineering/civil-engineering/civil-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.ncsu.edu/graduate/engineering/civil-engineering/civil-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.ncsu.edu/graduate/engineering/civil-engineering/civil-engineering-phd/ |

##### Computer Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-engineering/computer-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-engineering/computer-engineering-phd/ |

##### Computer Networking

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Networking | https://catalog.ncsu.edu/graduate/engineering/computer-networking/computer-networking-ms/ |

##### Computer Science

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ncsu.edu/graduate/engineering/computer-science/computer-science-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ncsu.edu/graduate/engineering/computer-science/computer-science-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ncsu.edu/graduate/engineering/computer-science/computer-science-phd/ |

##### Cybersecurity

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://catalog.ncsu.edu/graduate/engineering/cybersecurity/cybersecurity-ms/ |

##### Electric Power System Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Electric Power System Engineering | https://catalog.ncsu.edu/graduate/engineering/electric-power-system-engineering/electric-power-systems-engineering-ms/ |

##### Electrical Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/electrical-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/electrical-engineering-phd/ |

##### Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://catalog.ncsu.edu/graduate/engineering/engineering/engineering-mr/ |

##### Engineering Education

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Education | https://catalog.ncsu.edu/graduate/engineering/engineering-education/engineering-education-ms/ |

##### Engineering Management

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://catalog.ncsu.edu/graduate/engineering/engineering-management/engineering-management-mr/ |

##### Environmental Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Engineering | https://catalog.ncsu.edu/graduate/engineering/environmental-engineering/environmental-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Engineering | https://catalog.ncsu.edu/graduate/engineering/environmental-engineering/environmental-engineering-ms/ |

##### Industrial Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://catalog.ncsu.edu/graduate/engineering/industrial-engineering/industrial-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://catalog.ncsu.edu/graduate/engineering/industrial-engineering/industrial-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://catalog.ncsu.edu/graduate/engineering/industrial-engineering/industrial-engineering-phd/ |

##### Integrated Manufacturing Systems Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Integrated Manufacturing Systems Engineering | https://catalog.ncsu.edu/graduate/engineering/integrated-manufacturing-systems-engineering/integrated-manufacturing-systems-engineering-mr/ |

##### Materials Science Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalog.ncsu.edu/graduate/engineering/materials-science-engineering/materials-science-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalog.ncsu.edu/graduate/engineering/materials-science-engineering/materials-science-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalog.ncsu.edu/graduate/engineering/materials-science-engineering/materials-science-engineering-phd/ |

##### Mechanical Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.ncsu.edu/graduate/engineering/mechanical-engineering/mechanical-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.ncsu.edu/graduate/engineering/mechanical-engineering/mechanical-engineering-phd/ |

##### Nanoengineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Nanoengineering | https://catalog.ncsu.edu/graduate/engineering/nanoengineering/nanoengineering-mr/ |

##### Nuclear Engineering

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://catalog.ncsu.edu/graduate/engineering/nuclear-engineering/nuclear-engineering-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://catalog.ncsu.edu/graduate/engineering/nuclear-engineering/nuclear-engineering-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://catalog.ncsu.edu/graduate/engineering/nuclear-engineering/nuclear-engineering-phd/ |

##### Wide Bandgap Semiconductors

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Wide Bandgap Semiconductors | https://catalog.ncsu.edu/graduate/engineering/wide-bandgap-semiconductors/wide-bandgap-semiconductors-ms/ |

#### College of Humanities and Social Sciences

##### Anthropology

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/anthropology/anthropology-ma/ |

##### Communication

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.ncsu.edu/graduate/humanities-social-sciences/communication/communication-ms/ |

##### Communication Rhetoric Digital Media

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication, Rhetoric, and Digital Media | https://catalog.ncsu.edu/graduate/humanities-social-sciences/communication-rhetoric-digital-media/communication-rhetoric-digital-media-phd/ |

##### Creative Writing

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.ncsu.edu/graduate/humanities-social-sciences/creative-writing/creative-writing-mfa/ |

##### English

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://catalog.ncsu.edu/graduate/humanities-social-sciences/english/english-ma/ |

##### History

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://catalog.ncsu.edu/graduate/humanities-social-sciences/history/history-ma/ |

##### International Studies

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | International Studies | https://catalog.ncsu.edu/graduate/humanities-social-sciences/international-studies/international-studies-mr/ |

##### Liberal Studies

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Liberal Studies | https://catalog.ncsu.edu/graduate/humanities-social-sciences/liberal-studies/liberal-studies-ma/ |

##### Psychology

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/psychology/psychology-phd/ |

##### Public Administration

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-administration/public-administration-mr/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-administration/public-administration-phd/ |

##### Public History

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Public History | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-history/public-history-ma/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Public History | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-history/public-history-phd/ |

##### Social Work

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.ncsu.edu/graduate/humanities-social-sciences/social-work/social-work-mr/ |

##### Sociology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/sociology/sociology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/sociology/sociology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/sociology/sociology-phd/ |

##### Technical Communication

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Technical Communication | https://catalog.ncsu.edu/graduate/humanities-social-sciences/technical-communication/technical-communication-ms/ |

#### Institute for Advanced Analytics

##### Analytics

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Analytics | https://catalog.ncsu.edu/graduate/institute-advanced-analytics/analytics/analytics-ms/ |

#### Interdisciplinary Programs

##### Bioinformatics

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics | https://catalog.ncsu.edu/graduate/interdisciplinary/bioinformatics/bioinformatics-mr/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics | https://catalog.ncsu.edu/graduate/interdisciplinary/bioinformatics/bioinformatics-phd/ |

##### Financial Mathematics

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Financial Mathematics | https://catalog.ncsu.edu/graduate/interdisciplinary/financial-mathematics/financial-mathematics-mr/ |

##### Fisheries Wildlife Conservation Biology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries, Wildlife, and Conservation Biology | https://catalog.ncsu.edu/graduate/interdisciplinary/fisheries-wildlife-conservation-biology/fisheries-wildlife-conservation-biology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries, Wildlife, and Conservation Biology | https://catalog.ncsu.edu/graduate/interdisciplinary/fisheries-wildlife-conservation-biology/fisheries-wildlife-conservation-biology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Fisheries, Wildlife, and Conservation Biology | https://catalog.ncsu.edu/graduate/interdisciplinary/fisheries-wildlife-conservation-biology/fisheries-wildlife-conservation-biology-phd/ |

##### Foundationsofdatascience

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Foundations of Data Science | https://catalog.ncsu.edu/graduate/interdisciplinary/foundationsofdatascience/foundations-of-data-science-ms/ |

##### Genetics Genomics

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Genetics and Genomics | https://catalog.ncsu.edu/graduate/interdisciplinary/genetics-genomics/genetics-genomics-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Genetics and Genomics | https://catalog.ncsu.edu/graduate/interdisciplinary/genetics-genomics/genetics-genomics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Genetics and Genomics | https://catalog.ncsu.edu/graduate/interdisciplinary/genetics-genomics/genetics-genomics-phd/ |

##### Global One Health

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Global One Health | https://catalog.ncsu.edu/graduate/interdisciplinary/global-one-health/global-one-health-ms/ |

##### Operations Research

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Operations Research | https://catalog.ncsu.edu/graduate/interdisciplinary/operations-research/operations-research-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Operations Research | https://catalog.ncsu.edu/graduate/interdisciplinary/operations-research/operations-research-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Operations Research | https://catalog.ncsu.edu/graduate/interdisciplinary/operations-research/operations-research-phd/ |

#### Poole College of Management

##### Accounting

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.ncsu.edu/graduate/management/accounting/accounting-mr/ |

##### Business Administration

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.ncsu.edu/graduate/management/business-administration/business-administration-mr/ |

##### Economics

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ncsu.edu/graduate/management/economics/economics-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ncsu.edu/graduate/management/economics/economics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ncsu.edu/graduate/management/economics/economics-phd/ |

#### College of Natural Resources

##### Environmental Assessment

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Environment Assessment | https://catalog.ncsu.edu/graduate/natural-resources/environmental-assessment/environmental-assessment-mr/ |

##### Forest Biomaterials

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Forest Biomaterials | https://catalog.ncsu.edu/graduate/natural-resources/forest-biomaterials/forest-biomaterials-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Forest Biomaterials | https://catalog.ncsu.edu/graduate/natural-resources/forest-biomaterials/forest-biomaterials-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Forest Biomaterials | https://catalog.ncsu.edu/graduate/natural-resources/forest-biomaterials/forest-biomaterials-phd/ |

##### Forestry

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Forestry | https://catalog.ncsu.edu/graduate/natural-resources/forestry/forestry-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Forestry | https://catalog.ncsu.edu/graduate/natural-resources/forestry/forestry-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Forestry and Environmental Resources | https://catalog.ncsu.edu/graduate/natural-resources/forestry/forestry-environmental-resources-phd/ |

##### Geospatial Analytics

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Geospatial Analytics | https://catalog.ncsu.edu/graduate/natural-resources/geospatial-analytics/geospatial-analytics-phd/ |

##### Geospatial Information Science Technology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Geospatial Information Science and Technology | https://catalog.ncsu.edu/graduate/natural-resources/geospatial-information-science-technology/geospatial-information-science-technology-mr/ |

##### Natural Resources

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.ncsu.edu/graduate/natural-resources/natural-resources/natural-resources-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.ncsu.edu/graduate/natural-resources/natural-resources/natural-resources-ms/ |

##### Parks Recreation Tourism Management

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Parks, Recreation, Tourism, and Sports Management | https://catalog.ncsu.edu/graduate/natural-resources/parks-recreation-tourism-management/parks-recreation-tourism-sport-management-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Parks, Recreation and Tourism Management | https://catalog.ncsu.edu/graduate/natural-resources/parks-recreation-tourism-management/parks-recreation-tourism-management-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Parks, Recreation and Tourism Management | https://catalog.ncsu.edu/graduate/natural-resources/parks-recreation-tourism-management/parks-recreation-tourism-management-phd/ |

#### College of Sciences

##### Applied Mathematics

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.ncsu.edu/graduate/sciences/applied-mathematics/applied-mathematics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.ncsu.edu/graduate/sciences/applied-mathematics/applied-mathematics-phd/ |

##### Biomathematics

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomathematics | https://catalog.ncsu.edu/graduate/sciences/biomathematics/biomathematics-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomathematics | https://catalog.ncsu.edu/graduate/sciences/biomathematics/biomathematics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomathematics | https://catalog.ncsu.edu/graduate/sciences/biomathematics/biomathematics-phd/ |

##### Chemistry

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ncsu.edu/graduate/sciences/chemistry/chemistry-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ncsu.edu/graduate/sciences/chemistry/chemistry-phd/ |

##### Climate Change Society

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Climate Change & Society | https://catalog.ncsu.edu/graduate/sciences/climate-change-society/climate-change-society-mr/ |

##### Marine Earth Atmospheric Sciences

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Marine, Earth, and Atmospheric Sciences | https://catalog.ncsu.edu/graduate/sciences/marine-earth-atmospheric-sciences/marine-earth-atmospheric-sciences-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Marine, Earth, and Atmospheric Sciences | https://catalog.ncsu.edu/graduate/sciences/marine-earth-atmospheric-sciences/marine-earth-atmospheric-sciences-phd/ |

##### Mathematics

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ncsu.edu/graduate/sciences/mathematics/mathematics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ncsu.edu/graduate/sciences/mathematics/mathematics-phd/ |

##### Physics

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.ncsu.edu/graduate/sciences/physics/physics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.ncsu.edu/graduate/sciences/physics/physics-phd/ |

##### Statistics

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.ncsu.edu/graduate/sciences/statistics/statistics-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.ncsu.edu/graduate/sciences/statistics/statistics-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.ncsu.edu/graduate/sciences/statistics/statistics-phd/ |

##### Toxicology

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Toxicology | https://catalog.ncsu.edu/graduate/sciences/toxicology/toxicology-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Toxicology | https://catalog.ncsu.edu/graduate/sciences/toxicology/toxicology-ms/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Toxicology | https://catalog.ncsu.edu/graduate/sciences/toxicology/toxicology-phd/ |

#### Wilson College of Textiles

##### Fiber Polymer Science

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Fiber and Polymer Science | https://catalog.ncsu.edu/graduate/textiles/fiber-polymer-science/fiber-polymer-science-phd/ |

##### Textile Chemistry

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Textile Chemistry | https://catalog.ncsu.edu/graduate/textiles/textile-chemistry/textile-chemistry-ms/ |

##### Textile Engineering

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Textile Engineering | https://catalog.ncsu.edu/graduate/textiles/textile-engineering/textile-engineering-ms/ |

##### Textile Technology Management

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Textile Technology Management | https://catalog.ncsu.edu/graduate/textiles/textile-technology-management/textile-technology-management-phd/ |

##### Textiles

###### MR

| # | 项目 | URL |
|---|------|-----|
| 1 | Textiles | https://catalog.ncsu.edu/graduate/textiles/textiles/textiles-mr/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Textiles | https://catalog.ncsu.edu/graduate/textiles/textiles/textiles-ms/ |

#### College of Veterinary Medicine

##### Comparative Biomedical Sciences

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Biomedical Science | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-ms/ |

###### PSM

| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Biomedical Science (MS): Food Animals Concentration | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/food-animals-psm-concentration/ |

###### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Biomedical Science | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd/ |

### 2.2 Graduate Minors — complete list (63 minors)

> 来源: https://catalog.ncsu.edu/graduate/ 中 Programs and Degrees 节点下的 Minor 入口。

#### College of Agriculture and Life Sciences (14 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Agricultural Education and Human Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/agricultural-education-human-sciences-minor/ |
| 2 | Animal Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-science/animal-science-minor/ |
| 3 | Biochemistry | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biochemistry/biochemistry-minor/ |
| 4 | Crop Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/crop-science/crop-science-minor/ |
| 5 | Entomology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/entomology/entomology-minor/ |
| 6 | Food Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/food-science/food-science-minor/ |
| 7 | Genetic Engineering & Society | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/entomology/genetic-engineering-society-minor/ |
| 8 | Horticultural Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/horticultural-science/horticultural-science-minor/ |
| 9 | Microbiology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/microbiology/microbiology-minor/ |
| 10 | Nutrition | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/nutrition/nutrition-minor/ |
| 11 | Plant Biology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-biology/plant-biology-minor/ |
| 12 | Plant Pathology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/plant-pathology/plant-pathology-minor/ |
| 13 | Poultry Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/poultry-science/poultry-science-minor/ |
| 14 | Soil Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/soil-science/soil-science-minor/ |

#### College of Education (6 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Education Research & Policy Analysis | https://catalog.ncsu.edu/graduate/education/educational-leadership-policy-human-development/education-research-policy-analysis-minor/ |
| 2 | Mathematics Education | https://catalog.ncsu.edu/graduate/education/mathematics-education/mathematics-education-minor/ |
| 3 | Science Education | https://catalog.ncsu.edu/graduate/education/science-education/science-education-minor/ |
| 4 | Special Education | https://catalog.ncsu.edu/graduate/education/special-education/special-education-minor/ |
| 5 | Teacher Education and Learning Sciences | https://catalog.ncsu.edu/graduate/education/teacher-education-learning-sciences/teacher-education-learning-sciences-minor/ |
| 6 | Technology Education | https://catalog.ncsu.edu/graduate/education/technology-education/technology-education-minor/ |

#### College of Engineering (11 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.ncsu.edu/graduate/engineering/aerospace-engineering/aerospace-engineering-minor/ |
| 2 | Biomanufacturing | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/biomanufacturing-minor/ |
| 3 | Biomedical Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/biomedical-engineering-minor/ |
| 4 | Chemical Engineering | https://catalog.ncsu.edu/graduate/engineering/chemical-engineering/chemical-engineering-minor/ |
| 5 | Civil Engineering | https://catalog.ncsu.edu/graduate/engineering/civil-engineering/civil-engineering-minor/ |
| 6 | Computer Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-engineering/computer-engineering-minor/ |
| 7 | Electrical Engineering | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/electrical-engineering-minor/ |
| 8 | Industrial Engineering | https://catalog.ncsu.edu/graduate/engineering/industrial-engineering/industrial-engineering-minor/ |
| 9 | Materials Science and Engineering | https://catalog.ncsu.edu/graduate/engineering/materials-science-engineering/materials-science-engineering-minor/ |
| 10 | Mechanical Engineering | https://catalog.ncsu.edu/graduate/engineering/mechanical-engineering/mechanical-engineering-minor/ |
| 11 | Nuclear Engineering | https://catalog.ncsu.edu/graduate/engineering/nuclear-engineering/nuclear-engineering-minor/ |

#### College of Humanities and Social Sciences (5 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/anthropology/anthropology-minor/ |
| 2 | Cognitive Science | https://catalog.ncsu.edu/graduate/humanities-social-sciences/philosophy-religious-studies/cognitive-science-minor/ |
| 3 | International Studies | https://catalog.ncsu.edu/graduate/humanities-social-sciences/international-studies/international-studies-minor/ |
| 4 | Psychology | https://catalog.ncsu.edu/graduate/humanities-social-sciences/psychology/psychology-minor/ |
| 5 | Public Administration | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-administration/public-administration-minor/ |

#### Interdisciplinary Programs (10 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Biotechnology | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/biotechnology-minor/ |
| 2 | Ecology | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/ecology-minor/ |
| 3 | Food Safety | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/food-safety-minor/ |
| 4 | Genetics and Genomics | https://catalog.ncsu.edu/graduate/interdisciplinary/genetics-genomics/genetics-genomics-minor/ |
| 5 | Geographic Information Systems | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/geographic-information-systems-minor/ |
| 6 | Interdisciplinary Perspectives on Genes and Genomes | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/interdisciplinary-perspectives-on-genes-and-genomes/ |
| 7 | Operations Research | https://catalog.ncsu.edu/graduate/interdisciplinary/operations-research/operations-research-minor/ |
| 8 | Teamwork in Interdisciplinary Biomedical Research | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/teamwork-interdisciplinary-biomed-research/ |
| 9 | Water Resources | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/water-resources-minor/ |
| 10 | Women's, Gender, and Sexuality Studies | https://catalog.ncsu.edu/graduate/interdisciplinary/interdisciplinary-minors/womens-gender-studies-minor/ |

#### Poole College of Management (2 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.ncsu.edu/graduate/management/business-administration/business-administration-minor/ |
| 2 | Economics | https://catalog.ncsu.edu/graduate/management/economics/economics-minor/ |

#### College of Natural Resources (1 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Forestry | https://catalog.ncsu.edu/graduate/natural-resources/forestry/forestry-minor/ |

#### College of Sciences (8 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.ncsu.edu/graduate/sciences/applied-mathematics/applied-mathematics-minor/ |
| 2 | Biomathematics | https://catalog.ncsu.edu/graduate/sciences/biomathematics/biomathematics-minor/ |
| 3 | Chemistry | https://catalog.ncsu.edu/graduate/sciences/chemistry/chemistry-minor/ |
| 4 | Marine, Earth, & Atmospheric Sciences | https://catalog.ncsu.edu/graduate/sciences/marine-earth-atmospheric-sciences/marine-earth-atmospheric-sciences-minor/ |
| 5 | Mathematics | https://catalog.ncsu.edu/graduate/sciences/mathematics/mathematics-minor/ |
| 6 | Physics | https://catalog.ncsu.edu/graduate/sciences/physics/physics-minor/ |
| 7 | Statistics | https://catalog.ncsu.edu/graduate/sciences/statistics/statistics-minor/ |
| 8 | Toxicology | https://catalog.ncsu.edu/graduate/sciences/toxicology/toxicology-minor/ |

#### Wilson College of Textiles (5 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Fiber and Polymer Sciences | https://catalog.ncsu.edu/graduate/textiles/fiber-polymer-science/fiber-polymer-science-minor/ |
| 2 | Textile Chemistry | https://catalog.ncsu.edu/graduate/textiles/textile-chemistry/textile-chemistry-minor/ |
| 3 | Textile Engineering | https://catalog.ncsu.edu/graduate/textiles/textile-engineering/textile-engineering-minor/ |
| 4 | Textile Management and Technology | https://catalog.ncsu.edu/graduate/textiles/textiles/textile-management-technology-minor/ |
| 5 | Textile and Apparel Management | https://catalog.ncsu.edu/graduate/textiles/textiles/textile-apparel-management-minor/ |

#### College of Veterinary Medicine (1 minors)

| # | Minor | URL |
|---|------|-----|
| 1 | Comparative Biomedical Science | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-science-minor/ |

### 2.3 Graduate Certificates — complete list (67 certificates)

> 来源: https://catalog.ncsu.edu/graduate/ 中 Certificates 节点。

#### College of Agriculture and Life Sciences (12 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Agricultural and Extension Education | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-extension-education/agricultural-extension-education-certificate/ |
| 2 | Agriculture Data Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/graduate-certificate/agriculture-data-science-certificate/ |
| 3 | Family Life Education and Coaching | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/family-life-education-coaching-certificate/ |
| 4 | Feed Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/poultry-science/feed-science-certificate/ |
| 5 | Food Safety | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/graduate-certificate/food-safety-cert/ |
| 6 | Horticultural Science | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/horticultural-science/horticultural-science-certificate/ |
| 7 | Leadership and Volunteer Management | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/leadership-volunteer-management-certificate/ |
| 8 | Leadership in Agriculture and Human Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/graduate-certificate/leadership-agriculture-human-sciences-certificate/ |
| 9 | Molecular Biotechnology | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/graduate-certificate/molecular-biotechnology-certificate/ |
| 10 | Regulatory Science in Agriculture | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/graduate-certificate/regulatory-science-in-agriculture-cert/ |
| 11 | Watershed Assessment and Restoration | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/graduate-certificate/watershed-assessment-restoration-certificate/ |
| 12 | Youth Development and Leadership | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/youth-development-leadership-certificate/ |

#### College of Design (4 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | City Design | https://catalog.ncsu.edu/graduate/design/architecture/city-design-certificate/ |
| 2 | Disaster Resilient Policy, Engineering and Design | https://catalog.ncsu.edu/graduate/design/landscape-architecture/disaster-resilient-policy-engineering-design-cert/ |
| 3 | Energy and Technology in Architecture | https://catalog.ncsu.edu/graduate/design/architecture/energy-technology-architecture-certificate/ |
| 4 | Public Interest Design | https://catalog.ncsu.edu/graduate/design/architecture/public-interest-design-certificate/ |

#### College of Education (5 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Counselor Education | https://catalog.ncsu.edu/graduate/education/teaching-learning-curriculum/counselor-education-certificate/ |
| 2 | Learning Analytics | https://catalog.ncsu.edu/graduate/education/teacher-education-learning-sciences/learning-analytics-cert/ |
| 3 | Learning STEM in Informal Contexts | https://catalog.ncsu.edu/graduate/education/science-technology-engineering-mathematics-education/learning-stem-informal-contexts-certificate/ |
| 4 | Mathematics Teaching and Learning | https://catalog.ncsu.edu/graduate/education/science-technology-engineering-mathematics-education/mathematics-teaching-learning-certificate/ |
| 5 | Teaching, Training, and Educational Technology | https://catalog.ncsu.edu/graduate/education/educational-leadership-policy-human-development/teaching-training-educational-technology-certificate/ |

#### College of Engineering (18 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | 5G Technology | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/5g-technologies-certificate/ |
| 2 | ASIC Design & Verification | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/asic-design-and-verification-certificate/ |
| 3 | Computer Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-engineering/computer-engineering-certificate/ |
| 4 | Computer Science | https://catalog.ncsu.edu/graduate/engineering/computer-science/computer-science-certificate/ |
| 5 | Cybersecurity | https://catalog.ncsu.edu/graduate/engineering/graduate-certificate/cybersecurity-certificate/ |
| 6 | Data Science Foundations | https://catalog.ncsu.edu/graduate/engineering/computer-science/data-science-foundations-certificate/ |
| 7 | Downstream Biomanufacturing | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/downstream-biomanufacturing-certificate/ |
| 8 | Electrical Engineering | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/electrical-engineering-certificate/ |
| 9 | Engineering Education | https://catalog.ncsu.edu/graduate/engineering/engineering-education/engineering-education-certificate/ |
| 10 | Engineering Management Analytics | https://catalog.ncsu.edu/graduate/engineering/engineering-management/eng-mgmt-analytics-cert/ |
| 11 | Engineering Management Foundations | https://catalog.ncsu.edu/graduate/engineering/engineering-management/eng-mgmt-found-cert/ |
| 12 | Health Physics | https://catalog.ncsu.edu/graduate/engineering/graduate-certificate/health-physics-certificate/ |
| 13 | Materials Informatics | https://catalog.ncsu.edu/graduate/engineering/materials-science-engineering/materials-informatics-cert/ |
| 14 | Materials Science and Engineering | https://catalog.ncsu.edu/graduate/engineering/materials-science-engineering/materials-science-engineering-certificate/ |
| 15 | Nanobiotechnology | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/nanobiotechnology-certificate/ |
| 16 | Performance Based Earthquake Engineering | https://catalog.ncsu.edu/graduate/engineering/civil-engineering/performance-based-earthquake-engineering-cert/ |
| 17 | Renewable Electric Energy Systems | https://catalog.ncsu.edu/graduate/engineering/electrical-engineering/renewable-electric-energy-systems-certificate/ |
| 18 | Upstream Biomanufacturing | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/upstream-biomanufacturing-certificate/ |

#### College of Humanities and Social Sciences (4 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Digital Humanities | https://catalog.ncsu.edu/graduate/humanities-social-sciences/english/digital-humanities-certificate/ |
| 2 | Nonprofit Management | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-administration/nonprofit-management-certificate/ |
| 3 | Nuclear Nonproliferation Science and Policy | https://catalog.ncsu.edu/graduate/humanities-social-sciences/graduate-certificate/nuclear-nonproliferation-science-policy-certificate/ |
| 4 | Policy Analysis | https://catalog.ncsu.edu/graduate/humanities-social-sciences/public-administration/policy-analysis-certificate/ |

#### Interdisciplinary Programs (2 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Participatory Sciences | https://catalog.ncsu.edu/graduate/interdisciplinary/participatory-sciences/ |
| 2 | Real Estate Development and Design | https://catalog.ncsu.edu/graduate/interdisciplinary/real-estate-development/ |

#### Poole College of Management (8 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalog.ncsu.edu/graduate/management/business-administration/business-analytics-cert/ |
| 2 | Business Artificial Intelligence | https://catalog.ncsu.edu/graduate/management/graduate-certificate/graduate-certificate-business-artificial-intelligence/ |
| 3 | Business Leadership | https://catalog.ncsu.edu/graduate/management/business-administration/business-leadership-cert/ |
| 4 | Business Sustainability | https://catalog.ncsu.edu/graduate/management/graduate-certificate/graduate-certificate-business-sustainability/ |
| 5 | Finance | https://catalog.ncsu.edu/graduate/management/business-administration/finance-certificate/ |
| 6 | Marketing | https://catalog.ncsu.edu/graduate/management/business-administration/marketing-certificate/ |
| 7 | Operations and Supply Chain Management | https://catalog.ncsu.edu/graduate/management/business-administration/operations-supply-chain-management-certificate/ |
| 8 | Technology Entrepreneurship and Commercialization | https://catalog.ncsu.edu/graduate/management/business-administration/technology-entrepreneurship-commercialization-certificate/ |

#### College of Natural Resources (5 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Environmental Assessment | https://catalog.ncsu.edu/graduate/natural-resources/environmental-assessment/environmental-assessment-certificate/ |
| 2 | Geographic Information Systems | https://catalog.ncsu.edu/graduate/natural-resources/graduate-certificate/geographic-information-systems-certificate/ |
| 3 | Human Dimensions of Natural Resources | https://catalog.ncsu.edu/graduate/natural-resources/parks-recreation-tourism-management/human-dimensions-natural-resources-cert/ |
| 4 | Renewable Energy Assessment and Development | https://catalog.ncsu.edu/graduate/natural-resources/environmental-assessment/renewable-energy-assessment-development-certificate/ |
| 5 | Sport and Entertainment Venue Management | https://catalog.ncsu.edu/graduate/natural-resources/parks-recreation-tourism-management/sport-entertainment-venue-management-certificate/ |

#### College of Sciences (5 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Applied Statistics and Data Management | https://catalog.ncsu.edu/graduate/sciences/statistics/applied-statistics-data-management-certificate/ |
| 2 | Biology for Educators | https://catalog.ncsu.edu/graduate/sciences/graduate-certificate/biology-educators-certificate/ |
| 3 | Climate Adaptation | https://catalog.ncsu.edu/graduate/sciences/marine-earth-atmospheric-sciences/climate-adaptation-certificate/ |
| 4 | Mathematics | https://catalog.ncsu.edu/graduate/sciences/mathematics/mathematics-certificate/ |
| 5 | Teaching and Learning Statistics and Data Science | https://catalog.ncsu.edu/graduate/sciences/statistics/statistics-education-certificate/ |

#### Wilson College of Textiles (4 certificates)

| # | Certificate | URL |
|---|------|-----|
| 1 | Consumer Textile Product Design and Development | https://catalog.ncsu.edu/graduate/textiles/textiles/consumer-textile-product-design-development-certificate/ |
| 2 | Nonwoven Science and Technology | https://catalog.ncsu.edu/graduate/textiles/graduate-certificate/nonwoven-science-technology-certificate/ |
| 3 | Textile Brand Management and Marketing | https://catalog.ncsu.edu/graduate/textiles/textiles/textile-brand-management-marketing-certificate/ |
| 4 | Textile Supply Chain Management | https://catalog.ncsu.edu/graduate/textiles/textile-engineering/textile-supply-chain-management-certificate/ |

### 2.4 Department-level program landing pages (233)

> 这些是 NC State 各系在 graduate catalog 下的系级 landing pages,通常列出该系所有 graduate 项目与学位选项;除上文显式列出的 MS/MR/PhD 等条目外,这些 landing pages 也计为研究项目。下表前 60 条以展示结构,完整列表见 catalog。

| # | Program / Department | School | URL |
|---|------|-------|-----|
| 1 | Accounting | Poole College of Management | https://catalog.ncsu.edu/graduate/management/accounting/ |
| 2 | Adult and Community College Education | College of Education | https://catalog.ncsu.edu/graduate/education/adult-community-college-education/ |
| 3 | Aerospace Engineering | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/aerospace-engineering/ |
| 4 | Aerospace Engineering (MS): Industry Concentration | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/aerospace-engineering/aerospace-engineering-ms-industry-concentration/ |
| 5 | Agricultural Education and Human Sciences | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/agricultural-education-human-sciences/ |
| 6 | Analytics | Institute for Advanced Analytics | https://catalog.ncsu.edu/graduate/institute-advanced-analytics/analytics/ |
| 7 | Animal Science | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-science/ |
| 8 | Animal Science and Poultry Science | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-poultry-science/ |
| 9 | Animal Science and Poultry Science (PhD): Animal Science Concentration | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-poultry-science/animal-poultry-science-phd-animal-sci/ |
| 10 | Animal Science and Poultry Science (PhD): Poultry Science Concentration | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/animal-poultry-science/animal-poultry-science-phd-poultry-sci/ |
| 11 | Anthropology | College of Humanities and Social Sciences | https://catalog.ncsu.edu/graduate/humanities-social-sciences/anthropology/ |
| 12 | Applied Mathematics | College of Sciences | https://catalog.ncsu.edu/graduate/sciences/applied-mathematics/ |
| 13 | Applied Mathematics (PhD): Computational Mathematics Concentration | College of Sciences | https://catalog.ncsu.edu/graduate/sciences/applied-mathematics/applied-mathematics-phd-computational-mathematics/ |
| 14 | Applied Mathematics (PhD): Interdisciplinary Applied Math Concentration | College of Sciences | https://catalog.ncsu.edu/graduate/sciences/applied-mathematics/applied-mathematics-phd-interdisciplinary-applied-math-concentration/ |
| 15 | Architecture | College of Design | https://catalog.ncsu.edu/graduate/design/architecture/ |
| 16 | Architecture (MR): History and Theory of Architecture Concentration | College of Design | https://catalog.ncsu.edu/graduate/design/architecture/architecture-mr-history-theory-concentration/ |
| 17 | Art and Design | College of Design | https://catalog.ncsu.edu/graduate/design/art-design/ |
| 18 | Biochemistry | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biochemistry/ |
| 19 | Bioinformatics | Interdisciplinary Programs | https://catalog.ncsu.edu/graduate/interdisciplinary/bioinformatics/ |
| 20 | Biological and Agricultural Engineering | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biological-agricultural-engineering/ |
| 21 | Biological and Agricultural Engineering (MS): Systems Analysis Concentration | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-ms-systems-analysis/ |
| 22 | Biological and Agricultural Engineering (PhD): Systems Analysis Concentration | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biological-agricultural-engineering/biological-agricultural-engineering-phd-systems-analysis/ |
| 23 | Biology | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/biology/ |
| 24 | Biomanufacturing | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/ |
| 25 | Biomanufacturing (MR): Industry Track | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/biomanufacturing-mr/industry-track/ |
| 26 | Biomanufacturing Online Graduate Certificate | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomanufacturing/biomanufacturing-online-graduate-certificate/ |
| 27 | Biomathematics | College of Sciences | https://catalog.ncsu.edu/graduate/sciences/biomathematics/ |
| 28 | Biomedical Engineering | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/ |
| 29 | Biomedical Engineering (MS): MedTech Innovation and Entrepreneurship Concentration | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/biomedical-engineering-ms-translation-innovation-entrepreneurship-concentration/ |
| 30 | Biomedical Engineering (MS): Non-Thesis Concentration | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/biomedical-engineering-ms-non-thesis-concentration/ |
| 31 | Biomedical Engineering (MS): Thesis Concentration | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/biomedical-engineering/biomedical-engineering-ms-thesis-concentration/ |
| 32 | Business Administration | Poole College of Management | https://catalog.ncsu.edu/graduate/management/business-administration/ |
| 33 | Chemical Engineering | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/chemical-engineering/ |
| 34 | Chemistry | College of Sciences | https://catalog.ncsu.edu/graduate/sciences/chemistry/ |
| 35 | Civil Engineering | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/civil-engineering/ |
| 36 | Climate Change and Society | College of Sciences | https://catalog.ncsu.edu/graduate/sciences/climate-change-society/ |
| 37 | Clinical Mental Health Counseling | College of Education | https://catalog.ncsu.edu/graduate/education/clinical-mental-health-counseling/ |
| 38 | College Counseling and Student Development | College of Education | https://catalog.ncsu.edu/graduate/education/college-counseling-student-development/ |
| 39 | Communication | College of Humanities and Social Sciences | https://catalog.ncsu.edu/graduate/humanities-social-sciences/communication/ |
| 40 | Communication, Rhetoric, and Digital Media | College of Humanities and Social Sciences | https://catalog.ncsu.edu/graduate/humanities-social-sciences/communication-rhetoric-digital-media/ |
| 41 | Community College Leadership | College of Education | https://catalog.ncsu.edu/graduate/education/community-college-leadership/ |
| 42 | Comparative Biomedical Science (PhD): Cell Biology Concentration | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd-cell-biology-concentration/ |
| 43 | Comparative Biomedical Science (PhD): Infection and Immunity Concentration | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd-infection-and-immunity-concentration/ |
| 44 | Comparative Biomedical Science (PhD): Neurosciences Concentration | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd-neurosciences-concentration/ |
| 45 | Comparative Biomedical Science (PhD): Pathology Concentration | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd-pathology-concentration/ |
| 46 | Comparative Biomedical Science (PhD): Pharmacology Concentration | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd-pharmacology-concentration/ |
| 47 | Comparative Biomedical Science (PhD): Population and Global Health | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/comparative-biomedical-sciences-phd-population-med-vet-public-health-concentration/ |
| 48 | Comparative Biomedical Sciences | College of Veterinary Medicine | https://catalog.ncsu.edu/graduate/veterinary-medicine/comparative-biomedical-sciences/ |
| 49 | Computer Engineering | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-engineering/ |
| 50 | Computer Engineering (MS): Internship Concentration | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-engineering/computer-engineering-ms-internship-concentration/ |
| 51 | Computer Networking | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-networking/ |
| 52 | Computer Networking (MS): Internship Concentration | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-networking/computer-networking-ms-internship-concentration/ |
| 53 | Computer Science | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/computer-science/ |
| 54 | Creative Writing | College of Humanities and Social Sciences | https://catalog.ncsu.edu/graduate/humanities-social-sciences/creative-writing/ |
| 55 | Crop Science | College of Agriculture and Life Sciences | https://catalog.ncsu.edu/graduate/agriculture-life-sciences/crop-science/ |
| 56 | Cybersecurity | College of Engineering | https://catalog.ncsu.edu/graduate/engineering/cybersecurity/ |
| 57 | Design | College of Design | https://catalog.ncsu.edu/graduate/design/design/ |
| 58 | Economics | Poole College of Management | https://catalog.ncsu.edu/graduate/management/economics/ |
| 59 | Educational Leadership | College of Education | https://catalog.ncsu.edu/graduate/education/educational-leadership/ |
| 60 | Educational Leadership, Policy and Human Development | College of Education | https://catalog.ncsu.edu/graduate/education/educational-leadership-policy-human-development/ |

### 2.5 Worked example — Computer Science (MS), College of Engineering

- **Department address**: Department of Computer Science, College of Engineering, NC State University, 890 Oval Drive, Campus Box 8206, Raleigh, NC 27695-8206
- **Website**: https://www.csc.ncsu.edu/
- **Catalog page**: https://catalog.ncsu.edu/graduate/engineering/computer-science/computer-science-ms/
- **Degree**: Master of Science (MS); Accelerated Bachelor's/Master's (ABM) variant available
- **Total credit hours required**: 31
- **Structure** (from catalog page): Core Courses (6), Required Courses (7) [CSC 600 Computer Science Graduate Orientation + CSC 695 Master's Thesis Research], Elective Courses (9) [CSC 500/700-level], Minor Courses or CSC Graduate Electives or Restricted Electives (9)
- **Application portal**: NC State Graduate School application — https://grad.ncsu.edu/admissions/ (applicant portal at https://apply.ncsu.edu/applygrad)
- **Standardized tests**: GRE not required for most applicants; TOEFL/IELTS/Duolingo/PTE required for non-US citizens per §3.3
- **Funding**: RA/TA appointments + fellowships (see §4.3)

### 2.6 Graduate admissions model

NC State uses a **hybrid centralized + decentralized** model:
- **The Graduate School** (https://grad.ncsu.edu/) is the central administrative office that owns the online application, Graduate Handbook, English-proficiency rules, priority deadlines, and the final admissions decision.
- **Departments / programs** (Directors of Graduate Programs — DGPs) make initial admission recommendations. Many programs set earlier deadlines than the Graduate School priority deadlines.
- **Application platform**: NC State Graduate School online application (via Slate — see https://grad.ncsu.edu/faculty-and-staff/slate/).
- **Per-school entry points**: each college has its own grad-programs index page (e.g. https://cals.ncsu.edu/academics/graduate/, https://www.engr.ncsu.edu/academics/graduate-programs/, https://poole.ncsu.edu/graduate/, https://textiles.ncsu.edu/academics/graduate/).
- **Per-school financial aid**: most departments self-manage RA/TA lines + departmental fellowships.
- **International applicants** are reviewed by the International Admissions Specialist in the Graduate School once admitted by the program — see https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/ for Visa Clearance Form + Certificate of Financial Responsibility requirements.

---


## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

> 来源: https://admissions.ncsu.edu/apply/deadlines/ 与 https://admissions.ncsu.edu/apply/first-year/ (2026-07-07 抓取)

| 维度 | 值 |
|------|----|
| Admissions site | https://admissions.ncsu.edu/ |
| Application portal | https://apply.ncsu.edu/portal/wolfpaw (wolfPAW applicant portal) |
| Application platforms | Common App 或 Coalition by Scoir (两者任选,学校无偏好) |
| **EA deadline (First-Year)** | Nov. 1 |
| **EA materials deadline** | Nov. 15 |
| **EA notification date** | Jan. 31 |
| **RA deadline (First-Year)** | Jan. 15 |
| **RA materials deadline** | Feb. 1 |
| **RA notification date** | March 31 |
| **Spring First-Year deadline** | Oct. 1 (材料 Oct. 15;通知 Nov. 15) |
| **Studio-Based Majors deadline (First-Year & Transfer)** | Nov. 1 (作品集 + 附加文书同时截止) |
| **Music Technology (fall only)** | Early Action 或 Regular Decision (First-Year);Transfer 必须 Nov. 1 |
| **Agricultural Institute Fall entry** | June 1 (rolling) |
| **Agricultural Institute Spring entry** | Oct. 1 (rolling) |
| **Transfer Fall deadline** | Feb. 15 (材料 March 1;通知 April 15,滚动) |
| **Transfer Spring deadline** | Oct. 1 (材料 Oct. 15;通知 Nov. 15) |
| **Transfer Studio-Based deadline** | Nov. 1 (材料 Nov. 15;通知 Jan. 31) |
| Enrollment confirmation deadline | May 1 (fall admits);Dec. 1 (spring admits) |
| Financial aid (FAFSA) priority filing | March 1 (school code 002972) |
| University Honors deadline | Nov. 1 |
| SAT/ACT policy | **Test-Optional for weighted GPA ≥ 2.8** (UNC System policy);可自报;若提交则使用 superscore |
| SAT code | 5496 |
| ACT code | 3164 |
| Score report method | Self-report on application;official scores required only upon enrollment (if test scores were considered during review) |
| Recommendation requirements | None required;教师推荐 optionally via counselor |
| Portfolio requirements | **Studio-Based majors**: 10-piece portfolio + additional essay (Fashion and Textile Design 走 SlideRoom);**Music Technology**: 不超过 5 样本,each ≤ 5 min;**Architecture, MAD-Tech, Graphic & Experience Design, Industrial Design, Fashion and Textile Design** 通过 wolfPAW 提交 |
| Transfer pathway | NC State Transfer App 或 Common App;NC Community College transfer (46% of fall 2025 transfer admits) |
| Application fee | **$85 (non-refundable)**;fee waiver available |

> 节选自 https://admissions.ncsu.edu/apply/first-year/: "A non-refundable application fee of $85 is required. If you think you may qualify for a fee waiver, view fee waiver eligibility requirements..."
> 节选自 https://admissions.ncsu.edu/apply/deadlines/: "Early Action Deadline: Nov. 1; Regular Decision Deadline: Jan. 15; Studio-Based Majors: Nov. 1; Spring Applicants: Oct. 1..."

**Restricted from spring entry** (no spring first-year admission to): Applied Mathematics, College of Design studio-based majors, Exploratory Studies, College of Engineering first-year, Fashion and Textile Design, Mathematics, Music Technology, Physics, Statistics.

**First-choice only** (cannot be 2nd-choice major): Applied Mathematics, Architecture, Art and Design, all Engineering majors, Fashion and Textile Design, Graphic and Experience Design, Industrial Design, Mathematics, Physics, Statistics.

### 3.2 Undergraduate English proficiency table

> 来源: https://admissions.ncsu.edu/apply/international/ (expanded FAQ sections) 与 https://admissions.ncsu.edu/apply/international/#test-scores

| 考试 | 最低 (Full Admission) | Recommended / TA appointment | 备注 |
|------|----------------|-------------|------|
| TOEFL iBT (administered before Jan. 21, 2026) | **80 total** + 18 each subscore (Listening/Reading/Writing/Speaking) | Speaking 23 for TA w/ verbal interaction; 26 for TA presenting lectures | "For full undergraduate admission...we require an 80 or higher (minimum of 18 in each sub-score)" |
| TOEFL iBT (administered after Jan. 21, 2026) | **4 total** + 4 each subscore | Speaking 5 for TA | New scoring scale (Jan 21, 2026 update);older 80-point minimum still accepted |
| TOEFL iBT Conditional admission | **42 total** (older scale) | — | "For conditional admission, we require a score of 42 or higher" |
| IELTS (Academic) | **6.5 overall** + 6.5 each section | Speaking 7.0 for TA | "Academic IELTS scores with an overall band score of at least 6.5" |
| Duolingo English Test | **110 total** + subscores: Literacy 110, Comprehension 110, Conversation 110, Production 110 | Conversation/Production 125 for TA | "Duolingo with a total score of 110 or better" |
| PTE Academic | (accepted — minimum not extracted from page) | — | Listed alongside TOEFL/IELTS/Duolingo as accepted English proficiency test |
| Cambridge | (not specifically cited on UG page) | — | N/A |
| SAT/ACT/CLT | Test-optional;not a substitute for English proficiency (unless attending US high school) | — | "Is the English proficiency test required if I took the SAT or ACT?" — generally still required |
| Exemption | "be a citizen of a country where English is the official language and the language of instruction in higher education" 或 "successfully (cumulative GPA of 3.0 or higher) completed at least one year of full-time study in a degree program at a regionally accredited four-year US based College or university" | — | N/A |

> TOEFL 80 + 18 each 来源: https://admissions.ncsu.edu/apply/international/ —— "For exams taken before January 21, 2026, we require an 80 or higher (minimum of 18 in each sub-score) for full undergraduate admission."

### 3.3 Graduate — global rules

> 来源: https://grad.ncsu.edu/admissions/, https://grad.ncsu.edu/admissions/deadlines/, https://catalog.ncsu.edu/graduate/graduate-handbook/applications/, https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/

| 维度 | 值 |
|------|----|
| Admissions model | **Hybrid centralized + decentralized** (The Graduate School owns policy + final admit;departments recommend admission) |
| Application platform | NC State Graduate School Online Application (Slate) — https://grad.ncsu.edu/faculty-and-staff/slate/ |
| Application fee | **Non-refundable**, paid by credit card encouraged;waivers possible under exceptional circumstances;国际生不可用 student visa 类费用减免 |
| Per-school portals | Centralized;no separate school application (except for material uploads via department) |
| **US Citizens priority deadlines** | Fall Jun 25 / Spring Nov 25 / Summer 1 Mar 25 / Summer 2 May 10 |
| **International priority deadlines** | Fall Mar 1 / Spring Jul 15 / Summer 1 Dec 15 / Summer 2 Dec 15 |
| Program-specific deadlines | Many programs set EARLIER deadlines than priority;check each program (e.g. https://grad.ncsu.edu/about/people/dgp/) |
| GRE policy | **Program-by-program**: many engineering/computer science programs are GRE-optional or GRE-not-required;professional schools (Business, Education) often require GMAT/GRE;refer to individual program pages |
| GMAT policy | Required for MBA (Poole College of Management) |
| English proficiency policy (International) | Required for all non-US citizen applicants (详见下表);scores must be ≤ 24 months old |
| Institutional/departmental codes | TOEFL code: 5496 (NC State);ETS receives scores centrally;departments do not have separate codes |
| 推荐信 | **3 recommendations** from people who know the prospective student's academic record and potential |
| 申请有效期 | 12 months from date of submission |
| Application per program | 一个 application 只对 ONE graduate program 有效;apply to additional programs 需要重新申请并付费 |
| International additional docs | Visa Clearance Form (VCF);Certificate of Financial Responsibility (CFR) for F-1/J-1 visa applicants |
| Health insurance | F-1/J-1 学生必须购买 NC State 学生健康保险或通过 hard-waiver program 申请 waiver |

**Graduate English proficiency** (https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/, §2.4 B):

| 考试 | 最低 (Full Admission) | TA Appointment |
|------|----------------|---------------|
| TOEFL iBT (pre-Jan 21, 2026) | **80 total** + Listening 18 / Reading 18 / Writing 18 / Speaking 18 | Speaking 23 (TA w/ verbal interaction) / 26 (TA presenting) |
| TOEFL iBT (post-Jan 21, 2026) | **4 total** + 4 each section | Speaking 5 |
| TOEFL computer-based | 213 + ≥17 three sections + no section <13 | — |
| TOEFL paper-based | 550 + ≥50 two sections + no section <45 | — |
| IELTS (Academic) | **6.5 overall** + 6.5 each section | Speaking 7.0 |
| Duolingo | **110 total** + Literacy 110 / Comprehension 110 / Conversation 110 / Production 110 | Conversation & Production 125 |
| Exemption | Citizen of English-official-language country 且 higher-ed instruction in English;或 ≥1 year full-time study at US regionally-accredited 4-year institution (cumulative GPA ≥ 3.0) | — |
| Test age | 成绩不超过 24 个月 | — |

> 节选自 https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/ —— "Provide Test of English as a Foreign Language (TOEFL) (taken prior to January 21, 2026) with a total score of at least 80 on the Internet-based Test (iBT), and with minimum test scores for each section of: Listening 18 points; Reading 18 points; Writing 18 points; Speaking 18 points – for admission, 23 points – for TA appointment..."

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (Academic Year 2026-27, line-itemized)

> 来源: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/undergraduate-student-estimated-cost-of-attendance/ (table extraction 2026-07-07)
> 注: NC State 提供 on-campus 与 off-campus 两种居住预算;以下为 **NC resident + on-campus** (典型大一/大二住校) 与 **Out-of-State + on-campus** 两栏。完整四张表 (NC on-campus / NC off-campus / Out-of-state on-campus / Out-of-state off-campus) 已在抓取数据中,这里列出 on-campus 数据。

| Expense item | NC Resident | Out-of-State Resident |
|--------------|-------------|----------------------|
| Tuition & Fees | $9,247 | $34,961 |
| Books & Supplies | $642 | $642 |
| Housing (on-campus) | $8,738 | $8,738 |
| Food (on-campus meal plan) | $6,684 | $6,684 |
| Personal Expenses | $1,650 | $1,650 |
| Transportation | $1,485 | $2,060 |
| Loan Fees | $44 | $44 |
| **TOTAL (on-campus)** | **$28,490** | **$54,779** |
| **TOTAL (off-campus housing; 2026-27 NC Resident)** | **$29,560** | **$55,849** |

**Source snippet** (from extracted table): "Academic Year 2026-27 | North Carolina Residents | Out-of-State Residents; Tuition & Fees | $9,247 | $34,961; ... TOTAL | $28,490 | $54,779"

### 4.2 Undergraduate financial-aid policy

> 来源: https://admissions.ncsu.edu/afford/, https://studentservices.ncsu.edu/finances/scholarships-and-financial-aid/

| 维度 | 值 |
|------|----|
| Tuition-free income threshold | **N/A** (NC State is not tuition-free;offers merit + need-based aid) |
| Need-blind domestic? | Need-aware for international applicants (limited merit scholarships);domestic: need-based |
| Need-blind/need-aware (international) | **International applicants are NOT eligible for financial aid**;limited merit-based scholarships available (must apply via PACK ASSIST portal after admission) |
| FAFSA priority filing | March 1 (school code 002972) |
| Net Price Calculator | http://go.ncsu.edu/net-price-calculator |
| Median class profile (fall 2025) | 49,450 first-year applications;39.46% acceptance rate;5,904 incoming first-year students;14% out-of-state first-year |
| First-Year median GPA | 4.2-4.5 weighted;3.8-4.0 unweighted;55% applied without test scores |
| Transfer median (fall 2025) | 56 credits transferred avg;3.51 GPA;46% from NC Community College |
| Scholarships (competitive) | Park Scholarships (Nov. 1 deadline;min 3.8 unweighted GPA);Goodnight Scholars Program ($23,000/yr, STEM);Shelton Scholars Program ($7,000/yr + $2,000 enrichment);Chancellor's Leadership Scholarship ($5,000/yr);North Carolina Teaching Fellows Program ($8,250/yr forgivable loan) |
| School ranking & value | "#5 Best Value Among U.S. Public Universities" (U.S. News);"#2 Best Public College in North Carolina for Value" (Money) |

> 节选: https://admissions.ncsu.edu/afford/ —— "Priority filing deadline for NC State: March 1; School code: 002972; Newly admitted students begin receiving financial aid package information in early April."

### 4.3 Graduate cost & funding framework

> 来源: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/graduate-student-estimated-cost-of-attendance/, https://grad.ncsu.edu/admissions/financial-support/, https://catalog.ncsu.edu/graduate/graduate-handbook/assistantships-fellowships-traineeships-grants/

**Academic Year 2026-27 Graduate Cost of Attendance (NC Resident + on-campus)**

| Expense item | NC Resident | Out-of-State Resident |
|--------------|-------------|----------------------|
| Tuition & Fees | $13,065 | $35,002 |
| Books & Supplies | $400 | $400 |
| Housing (on-campus) | $8,738 | $8,738 |
| Food | $6,684 | $6,684 |
| Personal Expenses | $2,512 | $2,512 |
| Transportation | $2,060 | $2,060 |
| Loan Fees | $170 | $170 |
| **TOTAL (on-campus)** | **$33,629** | **$55,566** |

**Graduate funding framework**

| 维度 | 值 |
|------|----|
| Funding-type taxonomy | Fellowships/traineeships (outright awards);Teaching Assistantships (TA);Research Assistantships (RA);Service Assistantships;Work-study;Loans |
| Common funding forms | RA/TA (most common);fellowships (e.g. Goodnight Doctoral Fellowship — https://grad.ncsu.edu/goodnight-doctoral-fellowship/);traineeships;grants |
| Application fee | **Non-refundable**, paid by credit card;waivers possible under exceptional circumstances |
| Graduate Student Support Plan | Covers cost of tuition + health insurance for many students supported by research and teaching assistantships |
| Assistantship limits (International F-1/J-1) | 20 hrs/week max service work during Fall/Spring to maintain student visa status |
| Priority funding deadlines | Same as admissions deadlines (Fall Jun 25 US / Mar 1 Intl) |
| External funding | Travel funds available for professional meetings;departmental/college-level fellowships common |

> 节选: https://grad.ncsu.edu/admissions/financial-support/ —— "NC State offers graduate students a broad range of financial assistance options that help with tuition and living expenses while they are pursuing their advanced degrees. Graduate students may receive financial support through fellowships/traineeships, teaching assistantships, research assistantships, service assistantships, work-study programs, and loans."

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.cost.ay_2026_27.nc_resident.on_campus_total
  value: 28490
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/undergraduate-student-estimated-cost-of-attendance/
  source_snippet: "Academic Year 2026-27 | North Carolina Residents | Out-of-State Residents; Tuition & Fees | $9,247 | $34,961; ... TOTAL | $28,490 | $54,779"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-002:
  field: undergraduate.cost.ay_2026_27.out_of_state.on_campus_total
  value: 54779
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/undergraduate-student-estimated-cost-of-attendance/
  source_snippet: "TOTAL | $28,490 | $54,779"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-003:
  field: undergraduate.cost.tuition_fees.ay_2026_27.nc_resident
  value: 9247
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/undergraduate-student-estimated-cost-of-attendance/
  source_snippet: "Tuition & Fees | $9,247 | $34,961"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-004:
  field: undergraduate.cost.tuition_fees.ay_2026_27.out_of_state
  value: 34961
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/undergraduate-student-estimated-cost-of-attendance/
  source_snippet: "Tuition & Fees | $9,247 | $34,961"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-005:
  field: undergraduate.deadlines.early_action
  value: Nov. 1 (application) / Nov. 15 (materials) / Jan. 31 (notification)
  source_url: https://admissions.ncsu.edu/apply/deadlines/
  source_snippet: "Early Action | Nov. 1 | Nov. 15 | Jan. 31"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-006:
  field: undergraduate.deadlines.regular_decision
  value: Jan. 15 (application) / Feb. 1 (materials) / March 31 (notification)
  source_url: https://admissions.ncsu.edu/apply/deadlines/
  source_snippet: "Regular Decision | Jan. 15 | Feb. 1 | March 31"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-007:
  field: undergraduate.deadlines.transfer_fall
  value: Feb. 15 (application) / March 1 (materials) / April 15 (notification, rolling)
  source_url: https://admissions.ncsu.edu/apply/deadlines/
  source_snippet: "Fall Applicants | Feb. 15 | March 1 | April 15**"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-008:
  field: undergraduate.deadlines.studio_based
  value: Nov. 1 (only deadline;portfolio + essay due same day)
  source_url: https://admissions.ncsu.edu/apply/deadlines/
  source_snippet: "Studio-Based Majors | Nov. 1* | Nov. 15 | Rolling"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-009:
  field: undergraduate.deadlines.spring_first_year
  value: Oct. 1 (application) / Oct. 15 (materials) / Nov. 15 (notification)
  source_url: https://admissions.ncsu.edu/apply/deadlines/
  source_snippet: "Spring Applicants | Oct. 1 | Oct. 15 | Nov. 15**"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-010:
  field: undergraduate.tests.test_optional_policy
  value: Test-Optional for weighted GPA >= 2.8 (UNC System policy)
  source_url: https://admissions.ncsu.edu/apply/first-year/
  source_snippet: "As a part of the UNC System, NC State is test optional for applicants with a weighted GPA of 2.8 or above."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-011:
  field: undergraduate.tests.sat_code
  value: "5496"
  source_url: https://admissions.ncsu.edu/apply/first-year/
  source_snippet: "official SAT (code: 5496), ACT (code: 3164) or CLT test scores will be required prior to enrollment"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-012:
  field: undergraduate.tests.act_code
  value: "3164"
  source_url: https://admissions.ncsu.edu/apply/first-year/
  source_snippet: "official SAT (code: 5496), ACT (code: 3164) or CLT test scores will be required prior to enrollment"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-013:
  field: undergraduate.application_fee
  value: 85
  source_url: https://admissions.ncsu.edu/apply/first-year/
  source_snippet: "A non-refundable application fee of $85 is required."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-014:
  field: undergraduate.english.toefl_ibt_pre_2026.minimum
  value: 80 (with 18 each subscore)
  source_url: https://admissions.ncsu.edu/apply/international/
  source_snippet: "For exams taken before January 21, 2026, we require an 80 or higher (minimum of 18 in each sub-score) for full undergraduate admission."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-015:
  field: undergraduate.english.toefl_ibt_post_2026.minimum
  value: 4 total + 4 each subscore
  source_url: https://admissions.ncsu.edu/apply/international/
  source_snippet: "Can I still submit my TOEFL iBT scores if I took the exam before the scoring scale was updated on January 21, 2026?"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-016:
  field: undergraduate.english.ielts.minimum
  value: 6.5 overall + 6.5 each section
  source_url: https://admissions.ncsu.edu/apply/international/ + https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "Academic International English Language Testing System (IELTS) scores with an overall band score of at least 6.5."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-017:
  field: undergraduate.english.duolingo.minimum
  value: 110 total + subscores 110
  source_url: https://admissions.ncsu.edu/apply/international/
  source_snippet: "Duolingo with a total score of 110 or better AND minimum sub scores of: Literacy 110; Comprehension 110; Conversation 110; Production 110"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-018:
  field: undergraduate.english.conditional_admission_toefl
  value: 42 (pre-2026 scale)
  source_url: https://admissions.ncsu.edu/apply/international/
  source_snippet: "For conditional admission, we require a score of 42 or higher."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-019:
  field: undergraduate.financial_aid.fafsa_school_code
  value: "002972"
  source_url: https://admissions.ncsu.edu/afford/
  source_snippet: "School code: 002972"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-020:
  field: undergraduate.financial_aid.fafsa_priority_date
  value: March 1
  source_url: https://admissions.ncsu.edu/afford/
  source_snippet: "Priority filing deadline for NC State: March 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-021:
  field: undergraduate.financial_aid.international_eligibility
  value: NOT eligible for need-based aid;limited merit scholarships via PACK ASSIST
  source_url: https://admissions.ncsu.edu/apply/international/
  source_snippet: "International applicants are not eligible for financial aid. However, a limited number of competitive merit-based scholarships are available to international students."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-022:
  field: undergraduate.class_profile.fall_2025.first_year_apps
  value: 49450
  source_url: https://admissions.ncsu.edu/apply/fast-facts/
  source_snippet: "Fall 2025 Applications; 49,450 first-year applications received; 39.46% acceptance rate"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-023:
  field: undergraduate.class_profile.fall_2025.acceptance_rate
  value: 0.3946
  source_url: https://admissions.ncsu.edu/apply/fast-facts/
  source_snippet: "39.46% acceptance rate"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-024:
  field: undergraduate.class_profile.first_year_gpa.weighted
  value: 4.2-4.5
  source_url: https://admissions.ncsu.edu/apply/fast-facts/
  source_snippet: "4.2 – 4.5 weighted GPA; 3.8 – 4.0 unweighted GPA"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-025:
  field: undergraduate.majors.total
  value: 246 (BS/BA/Bachelor) + 7 AAS = 253
  source_url: https://catalog.ncsu.edu/find-your-program/ + https://catalog.ncsu.edu/undergraduate/
  source_snippet: catalog list items — extracted 246 BS/BA/Bachelor + 7 AAS (Agricultural Institute)
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-001:
  field: graduate.cost.ay_2026_27.nc_resident.on_campus_total
  value: 33629
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/graduate-student-estimated-cost-of-attendance/
  source_snippet: "Academic Year 2026-27 | North Carolina Residents | Out-of-State Residents; ... TOTAL | $33,629 | $55,566"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-002:
  field: graduate.cost.ay_2026_27.out_of_state.on_campus_total
  value: 55566
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/graduate-student-estimated-cost-of-attendance/
  source_snippet: "TOTAL | $33,629 | $55,566"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-003:
  field: graduate.cost.tuition_fees.ay_2026_27.nc_resident
  value: 13065
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/graduate-student-estimated-cost-of-attendance/
  source_snippet: "Tuition & Fees | $13,065 | $35,002"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-004:
  field: graduate.cost.tuition_fees.ay_2026_27.out_of_state
  value: 35002
  source_url: https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/graduate-student-estimated-cost-of-attendance/
  source_snippet: "Tuition & Fees | $13,065 | $35,002"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-005:
  field: graduate.deadlines.priority.us_citizen.fall
  value: June 25
  source_url: https://grad.ncsu.edu/admissions/deadlines/
  source_snippet: "US Citizens: Jun 25 ... Fall"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-006:
  field: graduate.deadlines.priority.international.fall
  value: March 1
  source_url: https://grad.ncsu.edu/admissions/deadlines/
  source_snippet: "Internationals: Mar 1 ... Fall"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-007:
  field: graduate.deadlines.priority.us_citizen.spring
  value: November 25
  source_url: https://grad.ncsu.edu/admissions/deadlines/
  source_snippet: "US Citizens: ... Nov 25 Spring"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-008:
  field: graduate.deadlines.priority.international.spring
  value: July 15
  source_url: https://grad.ncsu.edu/admissions/deadlines/
  source_snippet: "Internationals: Jul 15 ... Spring"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-009:
  field: graduate.english.toefl_ibt_pre_2026.minimum
  value: 80 total + 18 each section
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "Provide Test of English as a Foreign Language (TOEFL) (taken prior to January 21, 2026) with a total score of at least 80 on the Internet-based Test (iBT), and with minimum test scores for each section of: Listening 18 points; Reading 18 points; Writing 18 points; Speaking 18 points"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-010:
  field: graduate.english.toefl_ta_speaking
  value: 23 (TA w/ verbal interaction) / 26 (TA presenting)
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "Speaking 18 points – for admission, 23 points – for TA appointment where TA has direct verbal interactions with students, 26 points – for TA appointment where TA presents lectures in the class or laboratory"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-011:
  field: graduate.english.ielts.minimum
  value: 6.5 overall + 6.5 each section;Speaking 7.0 for TA
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "Provide Academic International English Language Testing System (IELTS) scores with an overall band score of at least 6.5... Speaking 6.5 – for admission, 7.0 – for TA appointment"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-012:
  field: graduate.english.duolingo.minimum
  value: 110 total + 110 each subscore;Conversation/Production 125 for TA
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "Provide Duolingo with a total score of 110 or better AND minimum sub scores of: Literacy 110; Comprehension 110; Conversation 110 - for admission, 125 for TA appointment; Production 110 - for admission, 125 for TA appointment"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-013:
  field: graduate.application.process_fee_refundable
  value: non-refundable
  source_url: https://grad.ncsu.edu/admissions/deadlines/
  source_snippet: "All application fees are totally non-refundable."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-014:
  field: graduate.application.recommendations
  value: 3 required
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/applications/
  source_snippet: "Three recommendations from people who know the prospective student's academic record and potential for graduate study"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-015:
  field: graduate.application.validity
  value: 12 months from submission
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/applications/
  source_snippet: "An application is valid for 12 months from the date it was submitted by the applicant."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-016:
  field: graduate.application.per_program_limit
  value: 1 program per application (must reapply for additional programs with separate fees)
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/applications/
  source_snippet: "An application is only valid for admission consideration by one graduate program. If an applicant wants to be considered for admission to additional programs, they must re-apply and pay an additional application fee for each program they apply to."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-017:
  field: graduate.funding.types
  value: fellowships/traineeships, TA, RA, service assistantships, work-study, loans
  source_url: https://grad.ncsu.edu/admissions/financial-support/
  source_snippet: "Graduate students may receive financial support through fellowships/traineeships, teaching assistantships, research assistantships, service assistantships, work-study programs, and loans."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-018:
  field: graduate.international.assistantship_limit
  value: 20 hrs/week max during Fall/Spring for F-1/J-1
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "International students in F-1 or J-1 status may not hold graduate assistantships or a combination of assistantships/positions that exceed 20 hours of service work per week during Fall and Spring semesters since this jeopardizes their student status with USCIS."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-019:
  field: graduate.international.health_insurance
  value: required for F-1/J-1 (or hard-waiver opt-out)
  source_url: https://catalog.ncsu.edu/graduate/graduate-handbook/international-student-admissions/
  source_snippet: "All international students in F-1 or J-1 status must purchase the University student health and accident insurance plan (or opt out through the universities hard-waiver program if other acceptable health insurance has already been purchased) throughout their program of study at NC State."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-020:
  field: graduate.programs.total_distinct
  value: 213
  source_url: https://catalog.ncsu.edu/graduate/
  source_snippet: 213 distinct graduate program names extracted from 568 catalog entries (with multi-degree + landing pages)
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-021:
  field: graduate.programs.official_count
  value: "160 master's + 62 doctoral + 67 graduate certificates (per About page)"
  source_url: https://grad.ncsu.edu/about/
  source_snippet: "we've built a roster of 160 master's and 62 doctoral programs... in more than 120 years of offering graduate programs"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-I-001:
  field: institution.college_count
  value: 12 (colleges) + 1 Institute for Advanced Analytics
  source_url: https://www.ncsu.edu/colleges-and-departments/
  source_snippet: "College of Agriculture and Life Sciences; College of Design; College of Education; College of Engineering; College of Humanities and Social Sciences; College of Natural Resources; Poole College of Management; College of Sciences; Wilson College of Textiles; College of Veterinary Medicine; The Graduate School; University College"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-I-002:
  field: institution.department_count
  value: 68
  source_url: https://catalog.ncsu.edu/
  source_snippet: "Learn more about our 12 colleges and 68 academic departments"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-I-003:
  field: institution.overview.majors_min
  value: "100+ majors offered to undergraduate students"
  source_url: https://admissions.ncsu.edu/apply/fast-facts/
  source_snippet: "100+ majors offered to undergraduate students"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-I-004:
  field: institution.overview.graduate_programs_min
  value: "200+ master's, doctoral and graduate certificate programs"
  source_url: https://grad.ncsu.edu/admissions/
  source_snippet: "NC State has more than 200 master's, doctoral and graduate certificate programs."
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: ncsu-knowledge-base-v2
├── document: ncsu-overview
│   ├── chunk: institution-overview (school name, college count, dept count, enrollment, location)
│   ├── chunk: program-counts (rule 1)
│   ├── chunk: college-department-hierarchy (rule 2 — 12 colleges + Institute)
│   ├── chunk: degree-level-inventory (rule 3)
│   └── chunk: distribution-matrix (rule 4)
├── document: ncsu-undergraduate
│   ├── chunk: ug-college-cals (school = CALS, 42 majors + 21 minors + 14 certs + 7 AAS)
│   ├── chunk: ug-college-design (8 majors + 2 minors)
│   ├── chunk: ug-college-education (16 majors + 2 minors + 2 certs)
│   ├── chunk: ug-college-engineering (48 majors + 11 minors + 3 certs)
│   ├── chunk: ug-college-chass (55 majors + 45 minors + 13 certs)
│   ├── chunk: ug-college-natural-resources (20 majors + 10 minors + 1 cert)
│   ├── chunk: ug-college-management (7 majors + 3 minors)
│   ├── chunk: ug-college-sciences (34 majors + 15 minors + 1 cert)
│   ├── chunk: ug-college-textiles (14 majors + 4 minors)
│   ├── chunk: ug-college-university-college (2 majors + 15 minors)
│   ├── chunk: ug-deadlines (early action / regular decision / spring / studio-based)
│   ├── chunk: ug-english-proficiency (TOEFL/IELTS/Duolingo/PTE minimums)
│   ├── chunk: ug-cost (AY 2026-27 line-itemized)
│   └── chunk: ug-financial-aid (FAFSA, scholarships)
├── document: ncsu-graduate
│   ├── chunk: grad-college-cals (46 degrees + 21 minors + 11 certs)
│   ├── chunk: grad-college-design (8 degrees)
│   ├── chunk: grad-college-education (29 degrees + 5 minors + 3 certs)
│   ├── chunk: grad-college-engineering (41 degrees + 7 minors + 14 certs)
│   ├── chunk: grad-college-chass (18 degrees + 6 minors + 8 certs)
│   ├── chunk: grad-college-natural-resources (14 degrees + 4 minors + 5 certs)
│   ├── chunk: grad-college-management (5 degrees + 7 certs)
│   ├── chunk: grad-college-sciences (20 degrees + 9 minors + 6 certs)
│   ├── chunk: grad-college-textiles (6 degrees + 1 minor + 1 cert)
│   ├── chunk: grad-college-veterinary-medicine (3 degrees)
│   ├── chunk: grad-institute-advanced-analytics (1 degree)
│   ├── chunk: grad-interdisciplinary (14 degrees + 6 minors + 5 certs)
│   ├── chunk: grad-priority-deadlines (US/Intl Fall/Spring/Summer)
│   ├── chunk: grad-english-proficiency (TOEFL 80 + 18 each / IELTS 6.5 / Duolingo 110)
│   ├── chunk: grad-cost (AY 2026-27 line-itemized)
│   ├── chunk: grad-funding (RA/TA/Fellowship/Support Plan)
│   └── chunk: grad-international (VCF/CFR/Insurance/Assistantship limits)
└── document: ncsu-evidence
    └── chunk: evidence-index (E-U-001..E-U-025, E-G-001..E-G-021, E-I-001..E-I-004)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ncsu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|Bachelor|AAS|MA|MS|MR|MEd|MFA|PhD|EdD|Cert|Minor>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Note |
|----------|-----------|-----------|------|
| P0 | MBA program deep-dive (Poole College) | https://poole.ncsu.edu/masters/mba/ | Catalog has landing page only;need separate MBA page for GMAT/work-experience requirements |
| P0 | DVM (Doctor of Veterinary Medicine) details | https://catalog.ncsu.edu/dvm/ | Separate catalog section;not yet extracted as part of graduate programs |
| P0 | Engineering Havelock BS / Engineering First Year | https://catalog.ncsu.edu/undergraduate/engineering/ | Engineering First Year program for transfer admits |
| P0 | Application fee exact amount for graduate (verify) | https://grad.ncsu.edu/admissions/ | Confirmed non-refundable;amount not visible on extracted pages — likely $75 or $85 |
| P1 | SAT/ACT/CLT middle 50% scores (admit profile) | https://admissions.ncsu.edu/apply/fast-facts/ | Only GPA reported;test percentiles not visible |
| P1 | Per-program GRE policy (Engineering, Sciences) | https://www.engr.ncsu.edu/academics/graduate-programs/ | GRE waiver policies vary by program |
| P1 | Tuition specific to MBA / DVM rates | https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/ | Cost page only has standard UG/Grad tables;MBA & DVM have separate rate schedules |
| P2 | Accelerated Bachelor's/Master's (ABM) full list | https://catalog.ncsu.edu/graduate/ | Catalog "Accelerated Bachelor's/Master's Degrees" section header was visible;full list not yet extracted |
| P2 | Graduate salary data by program | https://grad.ncsu.edu/about/graduate-salary-data/ | Referenced but not yet scraped |
| P2 | Department-level DGP/GSC contact directory | https://grad.ncsu.edu/about/people/dgp/ | Referenced but not yet scraped |

---

## SECTION 7 — Cross-school comparison framework

> Optional; used to compare NC State against other universities in the same knowledge base.

| Dimension | NC State |
|-----------|----------|
| Total UG cost/yr (NC resident, AY 2026-27, on-campus) | $28,490 |
| Total UG cost/yr (out-of-state, AY 2026-27, on-campus) | $54,779 |
| UG Tuition + Fees/yr (NC resident) | $9,247 |
| UG Tuition + Fees/yr (out-of-state) | $34,961 |
| Need-blind (international)? | No — international NOT eligible for need-based aid |
| EA deadline | Nov. 1 |
| RA deadline | Jan. 15 |
| SAT/ACT required? | No — Test-Optional for weighted GPA ≥ 2.8 |
| TOEFL min (UG, pre-2026 scale) | 80 + 18 each |
| IELTS min (UG) | 6.5 |
| Duolingo min (UG) | 110 |
| Tuition-free threshold | N/A (not tuition-free) |
| Median actual price paid | (not extracted in this run) |
| Grad application fee | Non-refundable (amount not visible — verify) |
| April-15-equivalent honor date | N/A (CGS-equivalent;not in CGS but follows CGS April 15 resolution) |
| **Total program count (rule 1)** | **991 catalog entries (UG 423 + Grad 568)** |
| **School/department count (rule 2)** | **12 colleges + 1 Institute + 68 departments** |
| Public/Private | Public (UNC System) |
| Region | US-South (Raleigh, NC) |
| Land-grant? | Yes |
| R1 research classification? | Yes (R1: Doctoral Universities — Very High Research Activity) |
| Enrollment (total) | 39,000+ |
| UG enrollment | ~26,000 |
| Grad enrollment | ~10,000 (9,500+) |
| Acceptance rate (first-year, fall 2025) | 39.46% |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: ncsu.edu, admissions.ncsu.edu, grad.ncsu.edu, catalog.ncsu.edu, studentservices.ncsu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (635 program items via `<li>` parser at https://catalog.ncsu.edu/find-your-program/; 568 graduate entries via catalog grad page; cost tables via `<table>` extraction at https://studentservices.ncsu.edu/finances/estimated-cost-of-attendance/)
> **Granularity**: school → department → degree-level → program
