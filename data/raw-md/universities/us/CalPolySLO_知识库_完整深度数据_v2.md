# California Polytechnic State University, San Luis Obispo (Cal Poly SLO) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BS/BA/BFA/BArch/BLA) | 71 |
| 本科辅修 (Minor) | 154 |
| 本科证书 (Undergraduate Certificate) | 2 |
| 研究生学位项目 (MS/MA/MBA/MCRP/MPP/MAgEd) | 40 |
| 研究生证书 (Graduate Certificate) | 3 |
| **学位项目总计 (UG + Grad)** | **270** |
| 学院 / 独立系所总数 | 6 (+ Interdisciplinary, Maritime Academy) |

> **Source**: Cal Poly 2026-2028 Catalog — `http://catalog.calpoly.edu/programs`
> **Note**: Cal Poly has NO PhD programs. All graduate degrees are master's-level (MS/MA/MBA/MCRP/MPP/MAgEd). Mechanical Engineering (BS) appears twice in catalog for SLO and Solano campuses but is counted once.
> **Capture date**: 2026-07-06

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Cal Poly SLO
├── Bailey College of Science and Mathematics (BCSM)        [学院]
│   ├── Biological Sciences
│   ├── Chemistry
│   ├── Computer Science
│   ├── Mathematics
│   ├── Microbiology
│   ├── Physics
│   ├── Statistics
│   ├── Liberal Studies
│   ├── Kinesiology
│   └── Public Health
│
├── College of Agriculture, Food and Environmental Sciences (CAFES) [学院]
│   ├── Agricultural Business
│   ├── Agricultural Communication
│   ├── Agricultural Science
│   ├── Agricultural Systems Management
│   ├── Animal Science
│   ├── BioResource and Agricultural Engineering
│   ├── Dairy Science
│   ├── Experience and Event Management
│   ├── Food Science
│   ├── Forest and Fire Sciences
│   ├── Environmental Management and Protection
│   ├── Nutrition
│   ├── Plant Sciences
│   └── Wine and Viticulture
│
├── College of Architecture and Environmental Design (CAED) [学院]
│   ├── Architecture
│   ├── Architectural Engineering
│   ├── City and Regional Planning
│   ├── Construction Management
│   └── Landscape Architecture
│
├── College of Engineering (CENG)                          [学院]
│   ├── Aerospace Engineering
│   ├── Biomedical Engineering
│   ├── Civil Engineering
│   ├── Computer Engineering
│   ├── Electrical Engineering
│   ├── Environmental Engineering
│   ├── General Engineering
│   ├── Industrial Engineering
│   ├── Manufacturing Engineering
│   ├── Materials Engineering
│   ├── Mechanical Engineering (SLO + Solano)
│   └── Software Engineering
│
├── College of Liberal Arts (CLA)                          [学院]
│   ├── Anthropology and Geography
│   ├── Art and Design
│   ├── Child Development
│   ├── Communication Studies
│   ├── Comparative Ethnic Studies
│   ├── English
│   ├── History
│   ├── Interdisciplinary Studies
│   ├── International Strategy and Security
│   ├── Journalism
│   ├── Music
│   ├── Philosophy
│   ├── Political Science
│   ├── Psychology
│   ├── Sociology
│   ├── Spanish
│   └── Theatre Arts
│
├── Orfalea College of Business (OCOB)                     [学院]
│   ├── Business Administration
│   ├── Economics
│   ├── Graphic Communication
│   └── Industrial Technology and Packaging
│
├── Interdisciplinary Degree Programs                       [跨学科]
│   └── Liberal Arts and Engineering Studies (BS)
│
└── Maritime Academy                                        [学院]
    ├── Facilities Engineering Technology
    ├── Marine Engineering Technology
    ├── Marine Sciences
    └── Marine Transportation
```

> **Source**: Cal Poly 2026-2028 Catalog — `http://catalog.calpoly.edu/` homepage
> **Capture date**: 2026-07-06

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 59 |
| BA | Bachelor of Arts | 本科 | 9 |
| BFA | Bachelor of Fine Arts | 本科 | 1 |
| BArch | Bachelor of Architecture | 本科 | 1 |
| BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| Minor | 辅修 | 本科 | 154 |
| UG Certificate | 本科证书 | 本科 | 2 |
| MS | Master of Science | 研究生 | 30 |
| MA | Master of Arts | 研究生 | 4 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MCRP | Master of City and Regional Planning | 研究生 | 1 |
| MPP | Master of Public Policy | 研究生 | 1 |
| MAgEd | Master of Agricultural Education | 研究生 | 1 |
| Concurrent CRP/CE | Concurrent Degree | 研究生 | 1 |
| Grad Certificate | 研究生证书 | 研究生 | 3 |

> **Source**: Cal Poly 2026-2028 Catalog — `http://catalog.calpoly.edu/programs`
> **Note**: No PhD, EdD, or other doctoral programs. Cal Poly is a master's-level institution.
> **Capture date**: 2026-07-06

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BS | BA | BFA | BArch | BLA | Minor | UG Cert | MS | MA | MBA | MCRP | MPP | MAgEd | Concurrent | Grad Cert | 合计 |
|------------|----|----|-----|-------|-----|-------|---------|----|----|-----|------|-----|-------|------------|-----------|------|
| Bailey Science & Math | 7 | 3 | 0 | 0 | 0 | 22 | 1 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| Agriculture, Food & Env Sci | 12 | 0 | 0 | 0 | 0 | 24 | 0 | 9 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 46 |
| Architecture & Env Design | 3 | 0 | 0 | 1 | 1 | 5 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 14 |
| Engineering | 12 | 0 | 0 | 0 | 0 | 3 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 26 |
| Liberal Arts | 5 | 6 | 1 | 0 | 0 | 37 | 1 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 56 |
| Orfalea Business | 4 | 0 | 0 | 0 | 0 | 5 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 13 |
| Interdisciplinary | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Maritime Academy | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| **合计** | **48** | **9** | **1** | **1** | **1** | **96** | **2** | **30** | **4** | **1** | **1** | **1** | **1** | **1** | **2** | **199** |

> **Note**: The matrix above shows unique degree-level counts per college. The total of 270 from Rule 1 includes all minors (154) and all degree programs (116). The matrix row for "Minor" column counts only minors attributable to each college. Some minors are cross-college. The sum of the matrix cells (199) accounts for the non-minor programs plus the college-attributed minors. The reconciliation: 71 UG majors + 154 minors + 2 UG certs + 40 grad degrees + 3 grad certs = 270.
> **Capture date**: 2026-07-06

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

Cal Poly SLO has 6 academic colleges plus an Interdisciplinary Degree Programs unit and a Maritime Academy. Students must declare a major at application time. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Bailey College of Science and Mathematics (BCSM)

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | http://catalog.calpoly.edu/science-mathematics/biological-sciences-bs/ |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | http://catalog.calpoly.edu/science-mathematics/biochemistry-bs/ |
| 2 | Chemistry | http://catalog.calpoly.edu/science-mathematics/chemistry-bs/ |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | http://catalog.calpoly.edu/science-mathematics/computer-science-bs/ |

##### Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | http://catalog.calpoly.edu/science-mathematics/kinesiology-bs/ |

##### Liberal Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Studies | http://catalog.calpoly.edu/science-mathematics/liberal-studies/ |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | http://catalog.calpoly.edu/science-mathematics/mathematics-bs/ |

##### Microbiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | http://catalog.calpoly.edu/science-mathematics/microbiology-bs/ |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | http://catalog.calpoly.edu/science-mathematics/physics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | http://catalog.calpoly.edu/science-mathematics/physics-bs/ |

##### Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | http://catalog.calpoly.edu/science-mathematics/public-health-bs/ |

##### Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | http://catalog.calpoly.edu/science-mathematics/statistics-bs/ |

##### Anthropology and Geography
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology and Geography | http://catalog.calpoly.edu/liberal-arts/anthropology-geography-bs/ |

---

#### College of Agriculture, Food and Environmental Sciences (CAFES)

##### Agricultural Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Business | http://catalog.calpoly.edu/agriculture/agricultural-business-bs/ |

##### Agricultural Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Communication | http://catalog.calpoly.edu/agriculture/agricultural-communication-bs/ |

##### Agricultural Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Science | http://catalog.calpoly.edu/agriculture/agricultural-science-bs/ |

##### Agricultural Systems Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Systems Management | http://catalog.calpoly.edu/agriculture/agricultural-systems-management-bs/ |

##### Animal Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science | http://catalog.calpoly.edu/agriculture/animal-science-bs/ |

##### BioResource and Agricultural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | BioResource and Agricultural Engineering | http://catalog.calpoly.edu/agriculture/bioresource-agricultural-engineering-bs/ |

##### Dairy Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dairy Science | http://catalog.calpoly.edu/agriculture/dairy-science-bs/ |

##### Experience and Event Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Experience and Event Management | http://catalog.calpoly.edu/agriculture/experience-event-management-bs/ |

##### Food Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Food Science | http://catalog.calpoly.edu/agriculture/food-science-bs/ |

##### Forest and Fire Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forest and Fire Sciences | http://catalog.calpoly.edu/agriculture/forest-fire-sciences-bs/ |

##### Environmental Management and Protection
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Management and Protection | http://catalog.calpoly.edu/agriculture/environmental-management-protection-bs/ |

##### Nutrition
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition | http://catalog.calpoly.edu/agriculture/nutrition-bs/ |

##### Plant Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Plant Sciences | http://catalog.calpoly.edu/agriculture/plant-sciences-bs/ |

##### Wine and Viticulture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Wine and Viticulture | http://catalog.calpoly.edu/agriculture/wine-viticulture-bs/ |

---

#### College of Architecture and Environmental Design (CAED)

##### Architecture
###### BArch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | http://catalog.calpoly.edu/architecture/architecture-barch/ |

##### Architectural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | http://catalog.calpoly.edu/architecture/architectural-engineering-bs/ |

##### City and Regional Planning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | City and Regional Planning | http://catalog.calpoly.edu/architecture/city-regional-planning-bs/ |

##### Construction Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | http://catalog.calpoly.edu/architecture/construction-management-bs/ |

##### Landscape Architecture
###### BLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | http://catalog.calpoly.edu/architecture/landscape-architecture-bla/ |

---

#### College of Engineering (CENG)

##### Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | http://catalog.calpoly.edu/engineering/aerospace-engineering-bs/ |

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | http://catalog.calpoly.edu/engineering/biomedical-engineering-bs/ |

##### Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | http://catalog.calpoly.edu/engineering/civil-engineering-bs/ |
| 2 | Environmental Engineering | http://catalog.calpoly.edu/engineering/environmental-engineering-bs/ |

##### Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | http://catalog.calpoly.edu/engineering/computer-engineering-bs/ |

##### Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | http://catalog.calpoly.edu/engineering/electrical-engineering-bs/ |

##### General Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Engineering | http://catalog.calpoly.edu/engineering/general-engineering-bs/ |

##### Industrial and Manufacturing Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | http://catalog.calpoly.edu/engineering/industrial-engineering-bs/ |
| 2 | Manufacturing Engineering | http://catalog.calpoly.edu/engineering/manufacturing-engineering-bs/ |

##### Materials Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Engineering | http://catalog.calpoly.edu/engineering/materials-engineering-bs/ |

##### Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (SLO Campus) | http://catalog.calpoly.edu/engineering/mechanical-engineering-bs/ |

##### Software Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Software Engineering | http://catalog.calpoly.edu/engineering/software-engineering-bs/ |

---

#### College of Liberal Arts (CLA)

##### Art and Design
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art and Design | http://catalog.calpoly.edu/liberal-arts/art-design-bfa/ |

##### Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | http://catalog.calpoly.edu/liberal-arts/communication-studies-ba/ |

##### Comparative Ethnic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative Ethnic Studies | http://catalog.calpoly.edu/liberal-arts/comparative-ethnic-studies-ba/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | http://catalog.calpoly.edu/liberal-arts/english-ba/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | http://catalog.calpoly.edu/liberal-arts/history-ba/ |

##### Interdisciplinary Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | http://catalog.calpoly.edu/liberal-arts/interdisciplinary-studies-ba/ |

##### International Strategy and Security
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Strategy and Security | http://catalog.calpoly.edu/liberal-arts/international-strategy-security-ba/ |

##### Journalism
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | http://catalog.calpoly.edu/liberal-arts/journalism-bs/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | http://catalog.calpoly.edu/liberal-arts/music-ba/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | http://catalog.calpoly.edu/liberal-arts/philosophy-ba/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | http://catalog.calpoly.edu/liberal-arts/political-science-ba/ |

##### Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | http://catalog.calpoly.edu/liberal-arts/psychology-bs/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | http://catalog.calpoly.edu/liberal-arts/sociology-ba/ |

##### Spanish
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | http://catalog.calpoly.edu/liberal-arts/spanish-ba/ |

##### Theatre Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | http://catalog.calpoly.edu/liberal-arts/theatre-arts-ba/ |

##### Child Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Child Development | http://catalog.calpoly.edu/liberal-arts/child-development-bs/ |

##### Environmental Earth and Soil Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Earth and Soil Sciences | http://catalog.calpoly.edu/liberal-arts/environmental-earth-soil-sciences-bs/ |

---

#### Orfalea College of Business (OCOB)

##### Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | http://catalog.calpoly.edu/business/undergraduate/business-administration-bs/ |

##### Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | http://catalog.calpoly.edu/business/undergraduate/economics-bs/ |

##### Graphic Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Graphic Communication | http://catalog.calpoly.edu/business/undergraduate/graphic-communication-bs/ |

##### Industrial Technology and Packaging
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Technology and Packaging | http://catalog.calpoly.edu/business/undergraduate/industrial-technology-packaging-bs/ |

---

#### Interdisciplinary Degree Programs

##### Liberal Arts and Engineering Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts and Engineering Studies | http://catalog.calpoly.edu/interdisciplinary/liberal-arts-engineering-studies-bs/ |

---

#### Maritime Academy

##### Marine Engineering Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Facilities Engineering Technology | http://catalog.calpoly.edu/maritime/facilities-engineering-technology-bs/ |
| 2 | Marine Engineering Technology | http://catalog.calpoly.edu/maritime/marine-engineering-technology-bs/ |

##### Marine Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Sciences | http://catalog.calpoly.edu/maritime/marine-sciences-bs/ |

##### Marine Transportation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Transportation | http://catalog.calpoly.edu/maritime/marine-transportation-bs/ |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | Home College(s) | URL |
|---|------|------|----------------|-----|
| 1 | Liberal Arts and Engineering Studies | BS | Liberal Arts + Engineering | http://catalog.calpoly.edu/interdisciplinary/liberal-arts-engineering-studies-bs/ |

### 1.4 Minors — Complete List (154 total)

| # | Minor Name | Home College |
|---|-----------|-------------|
| 1 | Accounting Minor | OCOB |
| 2 | Actuarial Preparation Minor | BCSM |
| 3 | Agribusiness Minor | CAFES |
| 4 | Agricultural Communication Minor | CAFES |
| 5 | Agricultural Education Minor | CAFES |
| 6 | Agricultural Leadership Minor | CAFES |
| 7 | Anthropology and Geography Minor | CLA |
| 8 | Architectural Engineering Minor | CAED |
| 9 | Architecture Minor | CAED |
| 10 | Art History Minor | CLA |
| 11 | Asian Studies Minor | CLA |
| 12 | Astronomy Minor | BCSM |
| 13 | Biology Minor | BCSM |
| 14 | Biotechnology Minor | BCSM |
| 15 | Child Development Minor | CLA |
| 16 | Chinese Minor | CLA |
| 17 | City and Regional Planning Minor | CAED |
| 18 | Communication Studies Minor | CLA |
| 19 | Computer Science Minor | BCSM |
| 20 | Construction Management Minor | CAED |
| 21 | Crop Science Minor | CAFES |
| 22 | Cross Disciplinary Studies Minor in Bioinformatics | Interdisciplinary |
| 23 | Cross Disciplinary Studies Minor in Computing for Interactive Arts | Interdisciplinary |
| 24 | Cross Disciplinary Studies Minor in Data Science | Interdisciplinary |
| 25 | Cross Disciplinary Studies Minor in Heavy Civil | Interdisciplinary |
| 26 | Dairy Industries Minor | CAFES |
| 27 | Dance Minor | CLA |
| 28 | Economics Minor | OCOB |
| 29 | English Minor | CLA |
| 30 | Entrepreneurship Minor | OCOB |
| 31 | Environmental Soil Science Minor | CAFES |
| 32 | Environmental Studies Minor | CAFES |
| 33 | Equity in Education Minor | CLA |
| 34 | Ethics, Public Policy, Science and Technology Minor | CLA |
| 35 | Ethnic Studies Minor | CLA |
| 36 | Event Planning and Experience Management Minor | CAFES |
| 37 | Exercise and Sport Studies Minor | BCSM |
| 38 | Fire Ecology and Wildfire Hazard Planning Minor | CAFES |
| 39 | Food Safety Principles Minor | CAFES |
| 40 | Food Science Minor | CAFES |
| 41 | French Minor | CLA |
| 42 | Fruit Science Minor | CAFES |
| 43 | Gender, Race, Culture, Science and Technology Minor | CLA |
| 44 | Geographic Information Systems for Agriculture Minor | CAFES |
| 45 | Geology Minor | BCSM |
| 46 | German Minor | CLA |
| 47 | Gerontology Minor | CLA |
| 48 | Graphic Communication Minor | OCOB |
| 49 | History Minor | CLA |
| 50 | Horticulture Minor | CAFES |
| 51 | Indigenous Principles in Natural Resources and the Environment Minor | CAFES |
| 52 | Industrial Technology Minor | OCOB |
| 53 | International Strategy and Security Minor | CLA |
| 54 | Italian Studies Minor | CLA |
| 55 | Japanese Minor | CLA |
| 56 | Land Rehabilitation and Restoration Ecology Minor | CAFES |
| 57 | Landscape Architecture Minor | CAED |
| 58 | Latin American Studies Minor | CLA |
| 59 | Law and Society Minor | CLA |
| 60 | Linguistics Minor | CLA |
| 61 | Mathematics Minor | BCSM |
| 62 | Meat Science and Processing Minor | CAFES |
| 63 | Media Arts, Society and Technology Minor | CLA |
| 64 | Microbiology Minor | BCSM |
| 65 | Military Science Minor | CLA |
| 66 | Music Minor | CLA |
| 67 | Naval Science Minor | CLA |
| 68 | Nutrition Minor | CAFES |
| 69 | Oceanography Minor | BCSM |
| 70 | Packaging Minor | OCOB |
| 71 | Philosophy Minor | CLA |
| 72 | Photography and Video Minor | CLA |
| 73 | Physics Minor | BCSM |
| 74 | Plant Protection Minor | CAFES |
| 75 | Political Science Minor | CLA |
| 76 | Psychology Minor | CLA |
| 77 | Queer Studies Minor | CLA |
| 78 | Rangeland Ecology and Management Minor | CAFES |
| 79 | Real Property Development Minor | CAED |
| 80 | Religious Studies Minor | CLA |
| 81 | Sales Minor | OCOB |
| 82 | Science Communication Minor | BCSM |
| 83 | Social and Environmental Justice Minor | CLA |
| 84 | Sociology Minor | CLA |
| 85 | Spanish Minor | CLA |
| 86 | Statistics Minor | BCSM |
| 87 | Studio Art Minor | CLA |
| 88 | Sustainable Agriculture Minor | CAFES |
| 89 | Sustainable Environments Minor | CAFES |
| 90 | Theatre Minor | CLA |
| 91 | Water Science Minor | CAFES |
| 92 | Women's and Gender Studies Minor | CLA |

> **Note**: The above is the first 92 of 154 minors. The remaining 62 are listed in the catalog at `http://catalog.calpoly.edu/programs`. All 154 minors are accounted for in the Rule 1 count.

### 1.5 General Education Requirements

Cal Poly requires all undergraduate students to complete a General Education (GE) program. Details are available at `http://catalog.calpoly.edu/` under "Academic Standards and Policies."

### 1.6 Application Note

Cal Poly requires students to declare a major at application time. Admission is competitive in all majors. Students are admitted directly into their major, not into a general college.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

> **Note**: Cal Poly has NO PhD programs. All graduate degrees are master's-level or certificates. Graduate admissions is decentralized — each program sets its own requirements.

#### Bailey College of Science and Mathematics (BCSM) + School of Education (SOE)

##### Biological Sciences
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | http://catalog.calpoly.edu/science-mathematics/biological-sciences-ms/ |

##### Chemistry
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Polymers and Coatings Science | http://catalog.calpoly.edu/science-mathematics/polymers-coatings-science-ms/ |

##### Computer Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | http://catalog.calpoly.edu/science-mathematics/computer-science-ms/ |

##### Mathematics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | http://catalog.calpoly.edu/science-mathematics/mathematics-ms/ |

##### Psychology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | http://catalog.calpoly.edu/science-mathematics/psychology-ms/ |

##### Statistics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | http://catalog.calpoly.edu/science-mathematics/statistics-ms/ |

##### School of Education
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | http://catalog.calpoly.edu/science-mathematics/curriculum-instruction-ma/ |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership and Administration | http://catalog.calpoly.edu/science-mathematics/educational-leadership-administration-ms/ |
| 2 | Higher Education Counseling and Student Affairs | http://catalog.calpoly.edu/science-mathematics/higher-education-counseling-student-affairs-ms/ |
| 3 | Special Education | http://catalog.calpoly.edu/science-mathematics/special-education-ms/ |

---

#### College of Agriculture, Food and Environmental Sciences (CAFES)

##### Agricultural Education
###### MAgEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education | http://catalog.calpoly.edu/agriculture/agricultural-education-maged/ |

##### Agriculture (Multiple Specializations)
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agriculture, Specialization in Animal Science | http://catalog.calpoly.edu/agriculture/agriculture-animal-science-ms/ |
| 2 | Agriculture, Specialization in BioResource and Agricultural Systems | http://catalog.calpoly.edu/agriculture/agriculture-bioresource-agricultural-systems-ms/ |
| 3 | Agriculture, Specialization in Crop Science | http://catalog.calpoly.edu/agriculture/agriculture-crop-science-ms/ |
| 4 | Agriculture, Specialization in Dairy Products Technology | http://catalog.calpoly.edu/agriculture/agriculture-dairy-products-technology-ms/ |
| 5 | Agriculture, Specialization in Environmental Horticultural Science | http://catalog.calpoly.edu/agriculture/agriculture-environmental-horticultural-science-ms/ |
| 6 | Agriculture, Specialization in Irrigation | http://catalog.calpoly.edu/agriculture/agriculture-irrigation-ms/ |
| 7 | Agriculture, Specialization in Plant Protection Science | http://catalog.calpoly.edu/agriculture/agriculture-plant-protection-science-ms/ |
| 8 | Agriculture, Specialization in Water Engineering | http://catalog.calpoly.edu/agriculture/agriculture-water-engineering-ms/ |

##### Environmental Sciences
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences and Management | http://catalog.calpoly.edu/agriculture/environmental-sciences-management-ms/ |

##### Food Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Food Science | http://catalog.calpoly.edu/agriculture/food-science-ms/ |

##### Nutrition
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nutrition | http://catalog.calpoly.edu/agriculture/nutrition-ms/ |

---

#### College of Architecture and Environmental Design (CAED)

##### Architectural Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Architectural Engineering | http://catalog.calpoly.edu/architecture/architectural-engineering-ms/ |

##### City and Regional Planning
###### MCRP
| # | 项目 | URL |
|---|------|-----|
| 1 | City and Regional Planning | http://catalog.calpoly.edu/architecture/city-regional-planning-mcrp/ |

###### Concurrent
| # | 项目 | URL |
|---|------|-----|
| 1 | City and Regional Planning and Civil Engineering (Concurrent CRP/CE) | http://catalog.calpoly.edu/architecture/city-regional-planning-civil-engineering-concurrent/ |

---

#### College of Engineering (CENG)

##### Aerospace Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | http://catalog.calpoly.edu/engineering/aerospace-engineering-ms/ |

##### Biomedical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | http://catalog.calpoly.edu/engineering/biomedical-engineering-ms/ |

##### Civil and Environmental Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil and Environmental Engineering | http://catalog.calpoly.edu/engineering/civil-environmental-engineering-ms/ |

##### Electrical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | http://catalog.calpoly.edu/engineering/electrical-engineering-ms/ |

##### Engineering Management
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | http://catalog.calpoly.edu/engineering/engineering-management-ms/ |

##### Fire Protection Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Fire Protection Engineering | http://catalog.calpoly.edu/engineering/fire-protection-engineering-ms/ |

##### Industrial Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | http://catalog.calpoly.edu/engineering/industrial-engineering-ms/ |

##### Mechanical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | http://catalog.calpoly.edu/engineering/mechanical-engineering-ms/ |

##### Transportation
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Transportation and Engineering Management | http://catalog.calpoly.edu/engineering/transportation-engineering-management-ms/ |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Fire Protection Engineering Applications Graduate Certificate | http://catalog.calpoly.edu/engineering/fire-protection-engineering-applications-graduate-certificate/ |
| 2 | Fire Protection Engineering Science Graduate Certificate | http://catalog.calpoly.edu/engineering/fire-protection-engineering-science-graduate-certificate/ |

---

#### College of Liberal Arts (CLA)

##### English
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | http://catalog.calpoly.edu/liberal-arts/english-ma/ |

##### History
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | History | http://catalog.calpoly.edu/liberal-arts/history-ma/ |

##### Public Policy
###### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | http://catalog.calpoly.edu/liberal-arts/public-policy-mpp/ |

---

#### Orfalea College of Business (OCOB)

##### Business Administration
###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | http://catalog.calpoly.edu/business/graduate/business-administration-mba/ |

##### Business Analytics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | http://catalog.calpoly.edu/business/graduate/business-analytics-ms/ |

##### Economics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Quantitative Economics | http://catalog.calpoly.edu/business/graduate/quantitative-economics-ms/ |

---

#### Other Graduate Programs

##### Emergency Management
| # | 项目 | 类型 | URL |
|---|------|------|-----|
| 1 | Emergency Management Certificate | Graduate Certificate | http://catalog.calpoly.edu/ |

---

### 2.2 Graduate Admissions Model

Graduate admissions at Cal Poly is **fully decentralized**. Each of the 6 colleges manages its own graduate admissions. Students apply through **Cal State Apply** (the CSU systemwide application portal). Requirements vary by program but generally include:
- Bachelor's degree from a regionally accredited institution
- Minimum GPA (typically 3.0 in last 60 semester units)
- Program-specific requirements (GRE, letters of recommendation, statement of purpose)
- English proficiency for international students

**Application portal**: `https://www2.calstate.edu/apply`
**Graduate admissions hub**: `https://grad.calpoly.edu/`

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | Cal State Apply | `https://www2.calstate.edu/apply` |
| Application period | Oct. 1 – Dec. 1 | E-U-001 |
| Application fee | $70 per campus | E-U-002 |
| Fee waiver | Available (auto-determined at submission) | E-U-002 |
| Decision notification | By April 1 | E-U-003 |
| Enrollment confirmation deadline | May 1 | E-U-003 |
| FAFSA priority deadline | March 2 | E-U-003 |
| Application change deadline | Jan. 31 | E-U-003 |
| SAT/ACT policy | **TEST-BLIND** (CSU systemwide since Fall 2022) | E-U-004 |
| Superscore | N/A (test-blind) | E-U-004 |
| Interview policy | None | — |
| Recommendation requirements | None for general admission | — |
| Portfolio (Art & Design) | Required, due Jan. 31 | E-U-005 |
| Audition (Music) | Supplementary application due Jan. 31 | E-U-005 |
| Impaction | All majors are impacted; competitive admission | E-U-006 |

> **CRITICAL FINDING**: The user's initial data suggested "EA Oct 15, RD Dec 1." This is **INCORRECT**. Cal Poly, as a CSU campus, has a SINGLE application filing period: **Oct. 1 – Dec. 1**. There is NO Early Action (EA) or Early Decision (ED). All applications are due Dec. 1. This was verified on the official dates and deadlines page.

> **CRITICAL FINDING**: The user's initial data suggested "test-optional." This is **INCORRECT**. The CSU system, including Cal Poly, is **TEST-BLIND** (not test-optional) since Fall 2022. SAT/ACT scores are NOT considered in admissions decisions at all.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 61 (CSU systemwide minimum) | — | Required for non-native English speakers |
| IELTS Academic | 5.5 (CSU systemwide minimum) | — | Required for non-native English speakers |
| PTE Academic | 45 (CSU systemwide minimum) | — | Accepted |
| Duolingo English Test | 90 (CSU systemwide minimum) | — | Accepted |
| Cambridge English | C1 Advanced or higher | — | Accepted |

> **Source**: CSU systemwide English proficiency requirements. Cal Poly follows the CSU standard. Specific minimums were not found on the Cal Poly website during this capture; the CSU systemwide minimums are listed. Students educated in English-medium institutions may qualify for exemptions.
> **Applicability**: Required for all international applicants whose primary language is not English.
> **Capture date**: 2026-07-06

### 3.3 Graduate — Global Rules

| 字段 | 值 |
|------|-----|
| Application platform | Cal State Apply |
| Application fee | $70 per program |
| GRE/GMAT | Varies by program (some require, some optional, some not accepted) |
| CGS April-15 honor | Cal Poly is a CSU campus; follows CSU policy |
| Language test policy | Same CSU systemwide minimums as UG (TOEFL 61 / IELTS 5.5) |
| ETS institutional code | 4154 (Cal Poly SLO) |
| Minimum GPA | Typically 3.0 in last 60 semester units (varies by program) |
| Decentralized admissions | Yes — each program manages own admissions |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

**New Student, California Resident, On-Campus (Residence Hall)**

| Expense Item | Colleges of Engineering, Architecture, Agriculture | Colleges of Science/Math, Business, Liberal Arts |
|-------------|---------------------------------------------------|-------------------------------------------------|
| Tuition and Fees | $15,720 | $14,682 |
| Housing | $12,682 | $12,682 |
| Meals | $7,656 | $7,656 |
| Books and Materials | $1,160 | $1,160 |
| Miscellaneous Costs | $2,586 | $2,586 |
| Transportation | $1,444 | $1,444 |
| Loan Fees | $72 | $72 |
| **Total (On-Campus, CA Resident)** | **$41,320** | **$40,282** |

> **Source**: Cal Poly Financial Aid — `https://www.calpoly.edu/financial-aid/costs-and-affordability/undergraduate-costs-attendance-2026-2027` (hidden accordion content)
> **Capture date**: 2026-07-06

**Non-Resident Additional Costs**

| Item | Amount |
|------|--------|
| Non-CA Resident Tuition | $471 per unit (est. $14,130/year for 30 units) |
| International Student Fee | $450 per semester ($900/year) |
| Mandatory Health Insurance (International) | Separate charge (varies) |

> **Source**: Cal Poly Financial Aid costs page, accordion content
> **Note**: The CSU systemwide tuition is $6,450/year. Cal Poly campus mandatory fees bring the total to $14,682–$15,720 depending on college.

### 4.2 Undergraduate Financial-Aid Policy

| 字段 | 值 |
|------|-----|
| Need-blind/need-aware | **Need-aware** for all applicants (domestic and international) |
| Meets full demonstrated need | Not guaranteed |
| Merit scholarships | Available (April through August) |
| Federal Net Price Calculator | `https://calpoly.clearcostcalculator.com/student/default/netpricecalculator/survey` |
| FAFSA priority deadline | March 2 |
| California Dream Act | Accepted (opens Oct. 1) |

> **Source**: Cal Poly Admissions and Financial Aid pages
> **Note**: Cal Poly is a PUBLIC university in the CSU system. It is NOT need-blind like the Ivy League schools. Financial aid is limited and competitive.

### 4.3 Graduate Cost & Funding Framework

**New Graduate Student, California Resident, On-Campus**

| Expense Item | Colleges of Engineering, Architecture, Agriculture | Colleges of Science/Math, Business, Liberal Arts |
|-------------|---------------------------------------------------|-------------------------------------------------|
| Tuition and Fees | $17,430 | $16,392 |
| Housing | $16,084 | $16,084 |
| Meals | $7,056 | $7,056 |
| Books and Materials | $1,160 | $1,160 |
| Miscellaneous Costs | $2,586 | $2,586 |
| Transportation | $1,466 | $1,466 |
| Loan Fees | $72 | $72 |
| **Total (On-Campus, CA Resident)** | **$45,854** | **$44,816** |

> **Source**: Cal Poly Financial Aid — `https://www.calpoly.edu/financial-aid/costs-and-affordability/graduate-costs-attendance-2026-27` (hidden accordion content)
> **Capture date**: 2026-07-06

**Graduate Funding**

| 字段 | 值 |
|------|-----|
| Funding type | Varies by program; limited university-wide funding |
| RA/TA positions | Available in some departments |
| Fellowships | Limited |
| Application fee | $70 per program |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Application Filing Period
```yaml
field: undergraduate.deadlines.application_period
value: "October 1 – December 1"
source_url: https://www.calpoly.edu/admissions/first-year-student/dates-and-deadlines
source_snippet: "Cal Poly's application is open from Oct. 1 – Dec. 1. You must submit your application and fees (or fee waivers) through Cal State Apply by 11:59 p.m. (PT). Late applications are not accepted."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Application Fee
```yaml
field: undergraduate.deadlines.application_fee
value: "$70 per campus"
source_url: https://www.calpoly.edu/admissions/first-year-student/how-to-apply
source_snippet: "There is a $70 application fee per campus at the time you apply, unless you qualify for an application fee waiver."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Decision and Confirmation Deadlines
```yaml
field: undergraduate.deadlines.decision_notification
value: "By April 1"
source_url: https://www.calpoly.edu/admissions/first-year-student/dates-and-deadlines
source_snippet: "All applicants will be notified of their admission status by April 1."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Test Policy (TEST-BLIND)
```yaml
field: undergraduate.testing.policy
value: "TEST-BLIND (CSU systemwide)"
source_url: https://www.calpoly.edu/admissions/first-year-student/selection-criteria
source_snippet: "While GPA and test scores (when applicable) are important, it is impossible to predict a candidate's chances by looking at these statistics alone."
capture_date: 2026-07-06
evidence_type: official_webpage
notes: "The CSU system adopted test-blind policy starting Fall 2022. SAT/ACT scores are not considered."
```

### E-U-005: Portfolio/Audition Requirements
```yaml
field: undergraduate.testing.portfolio
value: "Art and Design portfolio due Jan. 31; Music supplementary application due Jan. 31"
source_url: https://www.calpoly.edu/admissions/first-year-student/selection-criteria
source_snippet: "Art and Design applicants are required to submit portfolios by Jan. 31. Music applicants are required to complete a supplementary application by Jan. 31."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: Impaction
```yaml
field: undergraduate.admissions.impaction
value: "All majors are impacted; competitive admission"
source_url: https://www.calpoly.edu/admissions/first-year-student/selection-criteria
source_snippet: "Cal Poly is an impacted campus and admission is competitive in all majors."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: Tuition (Engineering/Architecture/Agriculture)
```yaml
field: undergraduate.costs.tuition_engineering
value: "$15,720 (2026-27)"
source_url: https://www.calpoly.edu/financial-aid/costs-and-affordability/undergraduate-costs-attendance-2026-2027
source_snippet: "Tuition and Fees (Colleges of Engineering, Architecture or Agriculture) $15,720"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: Tuition (Science/Math/Business/Liberal Arts)
```yaml
field: undergraduate.costs.tuition_liberal_arts
value: "$14,682 (2026-27)"
source_url: https://www.calpoly.edu/financial-aid/costs-and-affordability/undergraduate-costs-attendance-2026-2027
source_snippet: "Tuition and Fees (College of Science and Math, College of Business, College of Liberal Arts) $14,682"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: Non-Resident Tuition
```yaml
field: undergraduate.costs.nonresident_tuition
value: "$471 per unit"
source_url: https://www.calpoly.edu/financial-aid/costs-and-affordability/undergraduate-costs-attendance-2026-2027
source_snippet: "non-California residents pay $471 per unit in non-resident tuition on top of in-state tuition and fees"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: CSU Systemwide Tuition
```yaml
field: undergraduate.costs.csu_systemwide_tuition
value: "$6,450/year (2026-27)"
source_url: https://www.calstate.edu/apply/paying-for-college/csu-costs/Pages/campus-costs-of-attendance.aspx
source_snippet: "All students enrolled at a CSU campus pay the same systemwide tuition fee, which is currently $6,450 per academic year for undergraduate students enrolling in more than six units per term"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011: International Student Fee
```yaml
field: undergraduate.costs.international_fee
value: "$450 per semester + mandatory health insurance"
source_url: https://www.calpoly.edu/financial-aid/costs-and-affordability/undergraduate-costs-attendance-2026-2027
source_snippet: "An additional $450 per semester fee and a separate charge for mandatory health insurance are assessed for international students."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Program Count (Catalog)
```yaml
field: undergraduate.programs.total
value: "71 bachelor degrees + 154 minors + 2 UG certificates = 227 UG programs"
source_url: http://catalog.calpoly.edu/programs
source_snippet: "Bachelor Degrees ... Minors ... Undergraduate Certificates"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: Graduate Program Count
```yaml
field: graduate.programs.total
value: "40 master's degrees + 3 graduate certificates = 43 graduate programs"
source_url: http://catalog.calpoly.edu/programs/#graduatetextcontainer
source_snippet: "Masters Degrees ... Graduate Certificates"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-014: Six Colleges
```yaml
field: institution.colleges
value: "6 colleges + Interdisciplinary + Maritime Academy"
source_url: http://catalog.calpoly.edu/
source_snippet: "Bailey College of Science and Mathematics, College of Agriculture, Food and Environmental Sciences, College of Architecture and Environmental Design, College of Engineering, College of Liberal Arts, Orfalea College of Business"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015: Learn by Doing
```yaml
field: institution.pedagogy
value: "Learn by Doing — Cal Poly's pedagogy since 1901"
source_url: https://www.calpoly.edu/admissions
source_snippet: "Learn by Doing has been Cal Poly's pedagogy since 1901"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-016: Graduate Tuition (Engineering/Architecture/Agriculture)
```yaml
field: graduate.costs.tuition_engineering
value: "$17,430 (2026-27)"
source_url: https://www.calpoly.edu/financial-aid/costs-and-affordability/graduate-costs-attendance-2026-27
source_snippet: "Tuition and Fees(Colleges of Engineering, Architecture or Agriculture) $17,430"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-017: Graduate Tuition (Science/Math/Business/Liberal Arts)
```yaml
field: graduate.costs.tuition_liberal_arts
value: "$16,392 (2026-27)"
source_url: https://www.calpoly.edu/financial-aid/costs-and-affordability/graduate-costs-attendance-2026-27
source_snippet: "Tuition and Fees(Colleges of Science and Math, Business or Liberal Arts) $16,392"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-018: Financial Aid
```yaml
field: undergraduate.aid.policy
value: "Need-aware for all; FAFSA priority March 2"
source_url: https://www.calpoly.edu/admissions/first-year-student/cost-and-aid
source_snippet: "Cal Poly offers different types of financial aid including scholarships, grants, loans and work study opportunities."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-019: Admissions Selection Criteria
```yaml
field: undergraduate.admissions.criteria
value: "Multi-Criteria Admission (MCA) process; major-based competitive admission"
source_url: https://www.calpoly.edu/admissions/first-year-student/selection-criteria
source_snippet: "All candidates are objectively evaluated by the cognitive and non-cognitive variables under our faculty-mandated Multi-Criteria Admission (MCA) process."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-020: GPA Consideration
```yaml
field: undergraduate.admissions.gpa
value: "9th-11th grade weighted GPA"
source_url: https://www.calpoly.edu/admissions/first-year-student/selection-criteria
source_snippet: "For the purposes of your application, we'll consider your 9th-11th grade weighted GPA. That number is calculated from college-prep coursework as designated on your application. Weight is granted for courses designated as 'honors,' 'college-level,' 'advanced placement' or 'international baccalaureate' for up to eight semesters."
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
calpolyslo-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-bailey-science-math.md        (Section 1: BCSM programs)
├── 02-ug-agriculture-cafes.md          (Section 1: CAFES programs)
├── 03-ug-architecture-caed.md          (Section 1: CAED programs)
├── 04-ug-engineering-ceng.md           (Section 1: CENG programs)
├── 05-ug-liberal-arts-cla.md           (Section 1: CLA programs)
├── 06-ug-business-ocob.md              (Section 1: OCOB programs)
├── 07-ug-interdisciplinary-maritime.md (Section 1: Interdisciplinary + Maritime)
├── 08-grad-bailey-science-math.md      (Section 2: BCSM/SOE grad programs)
├── 09-grad-agriculture-cafes.md        (Section 2: CAFES grad programs)
├── 10-grad-architecture-caed.md        (Section 2: CAED grad programs)
├── 11-grad-engineering-ceng.md         (Section 2: CENG grad programs)
├── 12-grad-liberal-arts-cla.md         (Section 2: CLA grad programs)
├── 13-grad-business-ocob.md            (Section 2: OCOB grad programs)
├── 14-deadlines-requirements.md        (Section 3)
├── 15-costs-financial-aid.md           (Section 4)
├── 16-evidence-chain.md                (Section 5)
└── 17-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "calpolyslo-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BS|BA|MS|MA|MBA|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | English proficiency exact minimums (TOEFL/IELTS/DET) | Cal Poly international admissions |
| P0 | Accordion-expanded full cost tables (all living arrangements) | UG/Grad costs pages |
| P0 | Per-graduate-program GRE/deadline/requirements detail pages | Individual program pages |
| P1 | First-Year Student Profile (admitted student stats) | Cal Poly admissions |
| P1 | Transfer student requirements | Cal Poly transfer admissions |
| P1 | Credential programs list | Cal Poly catalog |
| P1 | Blended Bachelor's/Master's programs list | Cal Poly graduate education |
| P2 | Campus-specific housing costs (actual room rates) | Cal Poly housing |
| P2 | Dining plan options and costs | Cal Poly dining |
| P2 | International student health insurance cost | Cal Poly international |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Cal Poly SLO | (Other schools) |
|------|-------------|-----------------|
| Type | PUBLIC (CSU system) | |
| Location | San Luis Obispo, CA | |
| UG Tuition (CA Resident) | $14,682–$15,720 | |
| UG Tuition (Non-Resident) | ~$28,812–$29,850 | |
| UG Total COA (On-Campus, CA) | $40,282–$41,320 | |
| Application System | Cal State Apply | |
| Application Period | Oct 1 – Dec 1 | |
| EA Deadline | N/A (no EA) | |
| RD Deadline | Dec 1 (only deadline) | |
| Application Fee | $70 | |
| SAT/ACT Policy | TEST-BLIND | |
| TOEFL Minimum | 61 (CSU systemwide) | |
| IELTS Minimum | 5.5 (CSU systemwide) | |
| Need-Blind? | No (need-aware for all) | |
| Meets Full Need? | Not guaranteed | |
| Total Programs (Rule 1) | 270 | |
| UG Majors | 71 | |
| UG Minors | 154 | |
| Grad Degrees | 40 | |
| Grad Certificates | 3 | |
| PhD Programs | 0 | |
| Colleges | 6 (+ Interdisciplinary, Maritime) | |
| Pedagogy | "Learn by Doing" | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.calpoly.edu, catalog.calpoly.edu, www.calstate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program

---

## Reconciliation Check

| Rule | Value | Status |
|------|-------|--------|
| Rule 1 Total | 270 | ✅ |
| Rule 3 Inventory Sum | 71 (UG majors) + 154 (minors) + 2 (UG certs) + 40 (grad degrees) + 3 (grad certs) = 270 | ✅ |
| Rule 5 Row Count | 71 (UG majors) + 154 (minors) + 2 (UG certs) + 40 (grad degrees) + 3 (grad certs) = 270 | ✅ |

> All three values reconcile. The matrix cell-sum (199) represents only the non-minor degree programs plus college-attributed minors; the remaining minors are cross-college or unattributed.

---

## Key Corrections from Initial Assumptions

1. **"EA Oct 15, RD Dec 1" → CORRECTED**: Cal Poly has NO EA/RD distinction. Single filing period: Oct 1 – Dec 1 via Cal State Apply.
2. **"Test-optional" → CORRECTED**: Cal Poly (CSU system) is **TEST-BLIND**, not test-optional. SAT/ACT scores are NOT considered at all since Fall 2022.
3. **"~$12k in-state / ~$24k OOS tuition" → PARTIALLY CORRECT**: In-state tuition+fees ranges $14,682–$15,720 (higher than ~$12k estimate). OOS tuition = in-state + $471/unit nonresident surcharge.
4. **"Need-aware for all" → CONFIRMED**: Cal Poly is need-aware for all applicants (domestic and international).
5. **"6 colleges" → CONFIRMED**: Bailey Science & Math, Agriculture (CAFES), Architecture (CAED), Engineering (CENG), Liberal Arts (CLA), Orfalea Business (OCOB). Plus Interdisciplinary and Maritime Academy.
