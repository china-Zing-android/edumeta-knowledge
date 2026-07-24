# University of Nebraska-Lincoln (UNL) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1-4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 132 |
| 本科辅修 (Minor) | 68 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 148 |
| 研究生高级证书 (Certificate / Diploma) | 43 |
| **学位项目总计 (UG + Grad)** | **343** |
| 学院 / 独立系所总数 | 9 (UG) + Graduate Studies |

> **Source**: catalog.unl.edu/undergraduate/majors/ (200 entries: 132 majors + 68 minors); graduate.unl.edu/academics/programs (191 entries: 148 degree programs + 43 certificates)

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Nebraska-Lincoln
├── College of Agricultural Sciences & Natural Resources (CASNR)  [学院]
│   ├── Agribusiness
│   ├── Agricultural Economics
│   ├── Agricultural Leadership, Education & Communication
│   ├── Agricultural Systems Technology
│   ├── Agronomy
│   ├── Animal Science
│   ├── Biochemistry (CASNR)
│   ├── Entomology
│   ├── Environmental & Sustainability Studies
│   ├── Fisheries & Wildlife
│   ├── Food Science & Technology
│   ├── Forensic Science
│   ├── Grassland Systems
│   ├── Horticulture
│   ├── Mechanized Systems Management
│   ├── Microbiology
│   ├── Natural Resources
│   ├── PGA Golf Management
│   ├── Plant Biology
│   ├── Plant & Landscape Systems
│   ├── Regional & Community Forestry
│   ├── Veterinary Science
│   └── Water Science
├── College of Architecture  [学院]
│   ├── Architectural Studies
│   ├── Interior Design
│   └── Landscape Architecture
├── College of Arts & Sciences  [学院]
│   ├── Actuarial Science (CAS)
│   ├── Anthropology
│   ├── Biochemistry (CAS)
│   ├── Biological Sciences
│   ├── Chemistry
│   ├── Classical Languages
│   ├── Classics & Religious Studies
│   ├── Communication Studies
│   ├── Computer Science
│   ├── Economics
│   ├── English
│   ├── Environmental Studies
│   ├── Ethnic Studies
│   ├── Film Studies
│   ├── French
│   ├── Geography
│   ├── Geology
│   ├── German
│   ├── Global Studies
│   ├── History
│   ├── Mathematics
│   ├── Music (CAS)
│   ├── Philosophy
│   ├── Physics
│   ├── Political Science
│   ├── Psychology
│   ├── Russian
│   ├── Sociology
│   ├── Spanish
│   ├── Statistics
│   ├── Theatre Arts
│   ├── Women's & Gender Studies
│   └── World Languages
├── College of Business  [学院]
│   ├── Accounting
│   ├── Actuarial Science (Business)
│   ├── Agribusiness (Business)
│   ├── Business Administration
│   ├── Business and Law
│   ├── Economics (Business)
│   ├── Finance
│   ├── International Business
│   ├── Management
│   ├── Marketing
│   ├── Supply Chain Management
│   └── Undecided Business
├── College of Education & Human Sciences  [学院]
│   ├── Child, Youth & Family Studies
│   ├── Communication Sciences & Disorders
│   ├── Early Childhood & Family Policy
│   ├── Education
│   ├── Educational Psychology
│   ├── Family & Consumer Sciences Education
│   ├── Hospitality, Restaurant & Tourism Management
│   ├── Human Development & Family Science
│   ├── Interior Design (CEHS)
│   ├── Nutrition & Health Sciences
│   ├── Special Education
│   ├── Textiles, Merchandising & Fashion Design
│   └── Tourism Management
├── College of Engineering  [学院]
│   ├── Agricultural Engineering
│   ├── Architectural Engineering (Omaha)
│   ├── Biological Systems Engineering
│   ├── Chemical & Biomolecular Engineering
│   ├── Civil Engineering
│   ├── Computer Engineering
│   ├── Construction Engineering
│   ├── Electrical Engineering
│   ├── Environmental Engineering
│   ├── Industrial & Management Systems Engineering
│   ├── Mechanical & Materials Engineering
│   ├── Software Engineering
│   └── Undecided Engineering
├── Hixson-Lied College of Fine & Performing Arts  [学院]
│   ├── Acting
│   ├── Art
│   ├── Art History & Criticism
│   ├── Dance
│   ├── Film & New Media
│   ├── Music (FPA)
│   ├── Theatre Arts (FPA)
│   └── Studio Art
├── College of Journalism & Mass Communications  [学院]
│   ├── Advertising & Public Relations
│   ├── Broadcasting
│   ├── Journalism
│   └── Sports Media & Communication
├── College of Public Affairs & Community Service  [学院]
│   ├── Criminology & Criminal Justice
│   ├── Gerontology
│   └── Public Administration
└── Graduate Studies (administers all graduate programs)  [学院]
    ├── Graduate programs across all colleges
    └── Professional programs (Law, Veterinary Medicine)
```

> **Note**: Some departments appear in multiple colleges (e.g., Actuarial Science in both Business and CAS; Biochemistry in both CAS and CASNR). These are separate degree programs with different requirements.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | ~45 |
| BS | BS | Bachelor of Science | 本科 | ~75 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | ~5 |
| BArch | BArch | Bachelor of Architecture | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 68 |
| MA | MA | Master of Arts | 研究生 | 22 |
| MS | MS | Master of Science | 研究生 | 52 |
| MFA | MFA | Master of Fine Arts | 研究生 | 2 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 4 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPAcc | MPAcc | Master of Professional Accountancy | 研究生 | 1 |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MAE | MAE | Master of Architectural Engineering | 研究生 | 1 |
| MAS | MAS | Master of Applied Science | 研究生 | 1 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 1 |
| MLS | MLS | Master of Legal Studies | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 0 |
| MCRP | MCRP | Master of Community & Regional Planning | 研究生 | 1 |
| MEGM | MEGM | Master of Engineering Management | 研究生 | 1 |
| AuD | AuD | Doctor of Audiology | 研究生 | 1 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 0 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| EdD | EdD | Doctor of Education | 研究生 | 2 |
| EdS | EdS | Education Specialist | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 42 |
| Certificate | GCER | Graduate Certificate | 研究生 | 43 |
| DualDegree | DUAL | Dual Degree (MS/PhD track) | 研究生 | 8 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

**Undergraduate Programs by College:**

| 学院 \ 级别 | BA | BS | BFA | BArch | Minor | 合计 |
|------------|----|----|-----|-------|-------|------|
| College of Agricultural Sciences & Natural Resources | 0 | 23 | 0 | 0 | 20 | 43 |
| College of Architecture | 0 | 2 | 0 | 1 | 1 | 4 |
| College of Arts & Sciences | 20 | 9 | 0 | 0 | 24 | 53 |
| College of Business | 0 | 12 | 0 | 0 | 6 | 18 |
| College of Education & Human Sciences | 0 | 30 | 0 | 0 | 6 | 36 |
| College of Engineering | 0 | 15 | 0 | 0 | 7 | 22 |
| Hixson-Lied College of Fine & Performing Arts | 3 | 3 | 5 | 0 | 1 | 12 |
| College of Journalism & Mass Communications | 0 | 4 | 0 | 0 | 0 | 4 |
| College of Public Affairs & Community Service | 0 | 1 | 0 | 0 | 2 | 3 |
| Other Academic Units | 0 | 0 | 0 | 0 | 3 | 3 |
| **合计** | **23** | **99** | **5** | **1** | **70** | **198** |

> **Note**: Counts are approximate based on catalog listings; some programs appear under multiple colleges (e.g., Actuarial Science in both Business and CAS). The 200 catalog entries include some pre-professional tracks and interdisciplinary programs not counted as standalone majors.

**Graduate Programs by Degree Level:**

| 学位级别 | 数量 |
|---------|------|
| MS | 52 |
| MA | 22 |
| PhD | 42 |
| Certificate | 43 |
| DualDegree (MS/PhD) | 8 |
| MBA | 1 |
| MFA | 2 |
| MEd | 4 |
| Other (MPA, MPAcc, MArch, MAE, MAS, MAT, MM, MLS, MCRP, MEGM, AuD, DMA, DVM, EdD, EdS) | 16 |
| **合计** | **191** |

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/College Architecture

UNL has 9 undergraduate-degree-granting colleges plus specialized academic units. Programs are organized by college in the catalog at catalog.unl.edu/undergraduate/. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Agricultural Sciences & Natural Resources (CASNR)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Agribusiness | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/agribusiness/ |
| 2 | Agricultural Economics | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/economics/ |
| 3 | Agricultural Leadership, Education and Communication | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/agricultural-leadership-education-communication/ |
| 4 | Agricultural Systems Technology | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/agricultural-systems-technology/ |
| 5 | Agronomy | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/agronomy/ |
| 6 | Animal Science | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/animal-science/ |
| 7 | Biochemistry (CASNR) | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/biochemistry/ |
| 8 | Entomology | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/entomology/ |
| 9 | Environmental & Sustainability Studies | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/environmental-sustainability-studies/ |
| 10 | Fisheries & Wildlife | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/fisheries-wildlife/ |
| 11 | Food Science & Technology | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/food-science-technology/ |
| 12 | Forensic Science | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/forensic-science/ |
| 13 | Grassland Systems | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/grassland-systems/ |
| 14 | Horticulture | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/horticulture/ |
| 15 | Mechanized Systems Management | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/mechanized-systems-management/ |
| 16 | Microbiology | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/microbiology/ |
| 17 | Natural Resources | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/natural-resources/ |
| 18 | PGA Golf Management | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/pga-golf-management/ |
| 19 | Plant Biology | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/plant-biology/ |
| 20 | Plant & Landscape Systems | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/plant-landscape-systems/ |
| 21 | Regional & Community Forestry | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/regional-community-forestry/ |
| 22 | Veterinary Science | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/veterinary-science/ |
| 23 | Water Science | BS | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/water-science/ |

#### College of Architecture

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architectural Studies | BS | https://catalog.unl.edu/undergraduate/architecture/architectural-studies/ |
| 2 | Interior Design | BS | https://catalog.unl.edu/undergraduate/architecture/interior-design/ |
| 3 | Landscape Architecture | BArch | https://catalog.unl.edu/undergraduate/architecture/landscape-architecture/ |

#### College of Arts & Sciences

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Actuarial Science (CAS) | BS | https://catalog.unl.edu/undergraduate/arts-sciences/actuarial-science/ |
| 2 | Anthropology | BA | https://catalog.unl.edu/undergraduate/arts-sciences/anthropology/ |
| 3 | Biochemistry (CAS) | BS | https://catalog.unl.edu/undergraduate/arts-sciences/biochemistry/ |
| 4 | Biological Sciences | BS | https://catalog.unl.edu/undergraduate/arts-sciences/biological-sciences/ |
| 5 | Chemistry | BS | https://catalog.unl.edu/undergraduate/arts-sciences/chemistry/ |
| 6 | Classical Languages | BA | https://catalog.unl.edu/undergraduate/arts-sciences/classical-languages/ |
| 7 | Classics & Religious Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/classics-religious-studies/ |
| 8 | Communication Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/communication-studies/ |
| 9 | Computer Science | BS | https://catalog.unl.edu/undergraduate/arts-sciences/computer-science/ |
| 10 | Economics | BA | https://catalog.unl.edu/undergraduate/arts-sciences/economics/ |
| 11 | English | BA | https://catalog.unl.edu/undergraduate/arts-sciences/english/ |
| 12 | Environmental Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/environmental-studies/ |
| 13 | Ethnic Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/ethnic-studies/ |
| 14 | Film Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/film-studies/ |
| 15 | French | BA | https://catalog.unl.edu/undergraduate/arts-sciences/french/ |
| 16 | Geography | BA | https://catalog.unl.edu/undergraduate/arts-sciences/geography/ |
| 17 | Geology | BS | https://catalog.unl.edu/undergraduate/arts-sciences/geology/ |
| 18 | German | BA | https://catalog.unl.edu/undergraduate/arts-sciences/german/ |
| 19 | Global Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/global-studies/ |
| 20 | History | BA | https://catalog.unl.edu/undergraduate/arts-sciences/history/ |
| 21 | Mathematics | BS | https://catalog.unl.edu/undergraduate/arts-sciences/mathematics/ |
| 22 | Philosophy | BA | https://catalog.unl.edu/undergraduate/arts-sciences/philosophy/ |
| 23 | Physics | BS | https://catalog.unl.edu/undergraduate/arts-sciences/physics/ |
| 24 | Political Science | BA | https://catalog.unl.edu/undergraduate/arts-sciences/political-science/ |
| 25 | Psychology | BA | https://catalog.unl.edu/undergraduate/arts-sciences/psychology/ |
| 26 | Russian | BA | https://catalog.unl.edu/undergraduate/arts-sciences/russian/ |
| 27 | Sociology | BA | https://catalog.unl.edu/undergraduate/arts-sciences/sociology/ |
| 28 | Spanish | BA | https://catalog.unl.edu/undergraduate/arts-sciences/spanish/ |
| 29 | Statistics | BS | https://catalog.unl.edu/undergraduate/arts-sciences/statistics/ |
| 30 | Theatre Arts | BA | https://catalog.unl.edu/undergraduate/arts-sciences/theatre-arts/ |
| 31 | Women's & Gender Studies | BA | https://catalog.unl.edu/undergraduate/arts-sciences/womens-gender-studies/ |

#### College of Business

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | BS | https://catalog.unl.edu/undergraduate/business/accounting/ |
| 2 | Actuarial Science (Business) | BS | https://catalog.unl.edu/undergraduate/business/actuarial-science/ |
| 3 | Agribusiness (Business) | BS | https://catalog.unl.edu/undergraduate/business/agribusiness/ |
| 4 | Business Administration | BS | https://catalog.unl.edu/undergraduate/business/business-administration/ |
| 5 | Business and Law | BS | https://catalog.unl.edu/undergraduate/business/business-and-law/ |
| 6 | Economics (Business) | BS | https://catalog.unl.edu/undergraduate/business/economics/ |
| 7 | Finance | BS | https://catalog.unl.edu/undergraduate/business/finance/ |
| 8 | International Business | BS | https://catalog.unl.edu/undergraduate/business/international-business/ |
| 9 | Management | BS | https://catalog.unl.edu/undergraduate/business/management/ |
| 10 | Marketing | BS | https://catalog.unl.edu/undergraduate/business/marketing/ |
| 11 | Supply Chain Management | BS | https://catalog.unl.edu/undergraduate/business/supply-chain-management/ |
| 12 | Undecided Business | BS | https://catalog.unl.edu/undergraduate/business/undecided/ |

#### College of Education & Human Sciences

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Child, Youth & Family Studies | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/child-youth-family-studies/ |
| 2 | Communication Sciences & Disorders | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/communication-sciences-disorders/ |
| 3 | Early Childhood Education | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/early-childhood-education/ |
| 4 | Elementary Education | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/elementary-education/ |
| 5 | Family & Consumer Sciences Education | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/family-consumer-sciences-education/ |
| 6 | Hospitality, Restaurant & Tourism Management | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/hospitality-restaurant-tourism-management/ |
| 7 | Human Development & Family Science | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/human-development-family-science/ |
| 8 | Interior Design (CEHS) | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/interior-design/ |
| 9 | Nutrition & Health Sciences | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/nutrition-health-sciences/ |
| 10 | Secondary Education | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/secondary-education/ |
| 11 | Special Education | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/special-education/ |
| 12 | Textiles, Merchandising & Fashion Design | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/textiles-merchandising-fashion-design/ |
| 13 | Tourism Management | BS | https://catalog.unl.edu/undergraduate/education-human-sciences/tourism-management/ |

#### College of Engineering

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Agricultural Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/agricultural/ |
| 2 | Architectural Engineering (Omaha) | BS | https://catalog.unl.edu/undergraduate/engineering/architectural/ |
| 3 | Biological Systems Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/biological-systems/ |
| 4 | Chemical & Biomolecular Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/chemical-biomolecular/ |
| 5 | Civil Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/civil/ |
| 6 | Computer Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/computer/ |
| 7 | Construction Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/construction/ |
| 8 | Electrical Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/electrical/ |
| 9 | Environmental Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/environmental/ |
| 10 | Industrial & Management Systems Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/industrial-management/ |
| 11 | Mechanical & Materials Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/mechanical-materials/ |
| 12 | Software Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/software/ |
| 13 | Undecided Engineering | BS | https://catalog.unl.edu/undergraduate/engineering/undecided/ |

#### Hixson-Lied College of Fine & Performing Arts

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Acting | BFA | https://catalog.unl.edu/undergraduate/fine-performing-arts/acting/ |
| 2 | Art | BA | https://catalog.unl.edu/undergraduate/fine-performing-arts/art/ |
| 3 | Art History and Criticism | BA | https://catalog.unl.edu/undergraduate/fine-performing-arts/art-history/ |
| 4 | Dance | BFA | https://catalog.unl.edu/undergraduate/fine-performing-arts/dance/ |
| 5 | Film & New Media | BA | https://catalog.unl.edu/undergraduate/fine-performing-arts/film-new-media/ |
| 6 | Music (FPA) | BM | https://catalog.unl.edu/undergraduate/fine-performing-arts/music/ |
| 7 | Theatre Arts (FPA) | BFA | https://catalog.unl.edu/undergraduate/fine-performing-arts/theatre-arts/ |
| 8 | Studio Art | BFA | https://catalog.unl.edu/undergraduate/fine-performing-arts/studio-art/ |

#### College of Journalism & Mass Communications

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advertising & Public Relations | BS | https://catalog.unl.edu/undergraduate/journalism-mass-communications/advertising-public-relations/ |
| 2 | Broadcasting | BS | https://catalog.unl.edu/undergraduate/journalism-mass-communications/broadcasting/ |
| 3 | Journalism | BS | https://catalog.unl.edu/undergraduate/journalism-mass-communications/journalism/ |
| 4 | Sports Media & Communication | BS | https://catalog.unl.edu/undergraduate/journalism-mass-communications/sports-media-communication/ |

#### College of Public Affairs & Community Service

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Criminology & Criminal Justice | BS | https://catalog.unl.edu/undergraduate/public-affairs-community-service/criminology-criminal-justice/ |
| 2 | Gerontology | BS | https://catalog.unl.edu/undergraduate/public-affairs-community-service/gerontology/ |
| 3 | Public Administration | BS | https://catalog.unl.edu/undergraduate/public-affairs-community-service/public-administration/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | 父级学院 |
|---|------|------|---------|
| 1 | Actuarial Science | BS | Business + CAS (separate programs) |
| 2 | Biochemistry | BS | CAS + CASNR (separate programs) |
| 3 | Agribusiness | BS | Business + CASNR (separate programs) |
| 4 | Environmental Studies | BA | CAS |
| 5 | Global Studies | BA | CAS |

### 1.4 Minors — Complete List

| # | Minor Name | Home College | URL |
|---|------------|-------------|-----|
| 1 | Aerospace Studies (Air Force ROTC) | Other Academic Units | https://catalog.unl.edu/undergraduate/academic-policies-other-units/aerospace-studies-air-force-rotc/ |
| 2 | African Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/african-studies-minor/ |
| 3 | African-American Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/african-american-studies-minor/ |
| 4 | Agricultural Climate Science | CASNR | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/applied-climate-science-minor/ |
| 5 | Arabic Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/arabic-studies-minor/ |
| 6 | Archaeology | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/archaeology-minor/ |
| 7 | Artificial Intelligence | Engineering | https://catalog.unl.edu/undergraduate/engineering/artificial-intelligence-minor/ |
| 8 | Asian Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/asian-studies-minor/ |
| 9 | Astronomy | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/astronomy-minor/ |
| 10 | Biochemistry (CAS) | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/biochemistry-minor/ |
| 11 | Biological Sciences | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/biological-sciences-minor/ |
| 12 | Business | Business | https://catalog.unl.edu/undergraduate/business/business-minor/ |
| 13 | Chemistry | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/chemistry-minor/ |
| 14 | Child, Youth & Family Studies | Education & Human Sciences | https://catalog.unl.edu/undergraduate/education-human-sciences/child-youth-family-studies-minor/ |
| 15 | Chinese | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/chinese-minor/ |
| 16 | Classics & Religious Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/classics-religious-studies-minor/ |
| 17 | Communication Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/communication-studies-minor/ |
| 18 | Computer Science | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/computer-science-minor/ |
| 19 | Computing | Engineering | https://catalog.unl.edu/undergraduate/engineering/computing-minor/ |
| 20 | Dance | Fine & Performing Arts | https://catalog.unl.edu/undergraduate/fine-performing-arts/dance-minor/ |
| 21 | Data Science | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/data-science-minor/ |
| 22 | Economics | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/economics-minor/ |
| 23 | English | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/english-minor/ |
| 24 | Environmental Engineering | Engineering | https://catalog.unl.edu/undergraduate/engineering/environmental-engineering-minor/ |
| 25 | Environmental Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/environmental-studies-minor/ |
| 26 | Ethnic Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/ethnic-studies-minor/ |
| 27 | Film Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/film-studies-minor/ |
| 28 | French | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/french-minor/ |
| 29 | Geography | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/geography-minor/ |
| 30 | Geology | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/geology-minor/ |
| 31 | German | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/german-minor/ |
| 32 | Global Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/global-studies-minor/ |
| 33 | History | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/history-minor/ |
| 34 | Horticulture | CASNR | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/horticulture-minor/ |
| 35 | Human Development & Family Science | Education & Human Sciences | https://catalog.unl.edu/undergraduate/education-human-sciences/human-development-family-science-minor/ |
| 36 | Japanese | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/japanese-minor/ |
| 37 | Jewish Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/jewish-studies-minor/ |
| 38 | Journalism & Mass Communications | Journalism | https://catalog.unl.edu/undergraduate/journalism-mass-communications/journalism-minor/ |
| 39 | Latin American Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/latin-american-studies-minor/ |
| 40 | Leadership & Communication | CASNR | https://catalog.unl.edu/undergraduate/agricultural-sciences-natural-resources/leadership-communication-minor/ |
| 41 | Mathematics | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/mathematics-minor/ |
| 42 | Military Science (Army ROTC) | Other Academic Units | https://catalog.unl.edu/undergraduate/academic-policies-other-units/military-science-army-rotc/ |
| 43 | Music | Fine & Performing Arts | https://catalog.unl.edu/undergraduate/fine-performing-arts/music-minor/ |
| 44 | Naval Science (Naval ROTC) | Other Academic Units | https://catalog.unl.edu/undergraduate/academic-policies-other-units/naval-science-naval-rotc/ |
| 45 | Nutrition & Health Sciences | Education & Human Sciences | https://catalog.unl.edu/undergraduate/education-human-sciences/nutrition-health-sciences-minor/ |
| 46 | Philosophy | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/philosophy-minor/ |
| 47 | Physics | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/physics-minor/ |
| 48 | Political Science | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/political-science-minor/ |
| 49 | Psychology | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/psychology-minor/ |
| 50 | Russian | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/russian-minor/ |
| 51 | Sociology | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/sociology-minor/ |
| 52 | Spanish | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/spanish-minor/ |
| 53 | Statistics | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/statistics-minor/ |
| 54 | Theatre Arts | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/theatre-arts-minor/ |
| 55 | Women's & Gender Studies | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/womens-gender-studies-minor/ |
| 56 | World Languages | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/world-languages-minor/ |
| 57 | Writing | Arts & Sciences | https://catalog.unl.edu/undergraduate/arts-sciences/writing-minor/ |

### 1.5 General/Institute-Wide Requirements

UNL uses the **Achievement-Centered Education (ACE)** general education program. All undergraduate students must complete 10 ACE requirements across 9 expected learning outcomes:
- ACE 1: Writing
- ACE 2: Communication
- ACE 3: Mathematical/Statistical/Computational Reasoning
- ACE 4: Scientific Inquiry
- ACE 5: Humanities
- ACE 6: Social Sciences
- ACE 7: Arts
- ACE 8: Ethics
- ACE 9: Global/Diversity/Integration (capstone)

> **Source**: catalog.unl.edu/undergraduate/academic-policies-other-units/general-education-requirements/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by Degree Level

UNL's Graduate Studies office (graduate.unl.edu) administers 191 graduate programs across all colleges. Programs are listed at graduate.unl.edu/academics/programs.

#### MS (Master of Science) — 52 programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://graduate.unl.edu/academics/programs/ACTS-MS/ |
| 2 | Agricultural & Biological Systems Engineering | https://graduate.unl.edu/academics/programs/ABSE-MS/ |
| 3 | Agricultural Economics | https://graduate.unl.edu/academics/programs/AECN-MS/ |
| 4 | Agricultural Systems Technology | https://graduate.unl.edu/academics/programs/AGST-MS/ |
| 5 | Agronomy | https://graduate.unl.edu/academics/programs/AGRO-MS/ |
| 6 | Animal Science | https://graduate.unl.edu/academics/programs/ASCI-MS/ |
| 7 | Architectural Engineering | https://graduate.unl.edu/academics/programs/AREN-MS/ |
| 8 | Artificial Intelligence | https://graduate.unl.edu/academics/programs/ARIN-MS-O/ |
| 9 | Athletic Training | https://graduate.unl.edu/academics/programs/ATHT-MS/ |
| 10 | Biochemistry | https://graduate.unl.edu/academics/programs/BIOC-MS/ |
| 11 | Biological Sciences | https://graduate.unl.edu/academics/programs/BIOS-MS/ |
| 12 | Business Analytics | https://graduate.unl.edu/academics/programs/BSAN-MS/ |
| 13 | Chemical Engineering | https://graduate.unl.edu/academics/programs/CHME-MS/ |
| 14 | Chemistry | https://graduate.unl.edu/academics/programs/CHEM-MS/ |
| 15 | Child, Youth and Family Studies | https://graduate.unl.edu/academics/programs/CYAF-MS/ |
| 16 | Civil Engineering | https://graduate.unl.edu/academics/programs/CIVE-MS/ |
| 17 | Communication Studies | https://graduate.unl.edu/academics/programs/COMM-MA/ |
| 18 | Computer Science | https://graduate.unl.edu/academics/programs/COMP-MS/ |
| 19 | Construction Engineering and Management | https://graduate.unl.edu/academics/programs/CEMT-MS/ |
| 20 | Earth and Atmospheric Sciences | https://graduate.unl.edu/academics/programs/GEOS-MS/ |
| 21 | Electrical Engineering | https://graduate.unl.edu/academics/programs/ELEC-MS/ |
| 22 | English | https://graduate.unl.edu/academics/programs/ENGL-MA/ |
| 23 | Entomology | https://graduate.unl.edu/academics/programs/ENTO-MS/ |
| 24 | Environmental Engineering | https://graduate.unl.edu/academics/programs/ENVE-MS/ |
| 25 | Finance | https://graduate.unl.edu/academics/programs/FINA-MS/ |
| 26 | Food Science and Technology | https://graduate.unl.edu/academics/programs/FDST-MS/ |
| 27 | Horticulture | https://graduate.unl.edu/academics/programs/HORT-MS/ |
| 28 | Leadership Education | https://graduate.unl.edu/academics/programs/LEED-MS/ |
| 29 | Mathematics | https://graduate.unl.edu/academics/programs/MATH-MS/ |
| 30 | Mechanical Engineering and Applied Mechanics | https://graduate.unl.edu/academics/programs/MEAM-MS/ |
| 31 | Natural Resource Sciences | https://graduate.unl.edu/academics/programs/NRSC-MS/ |
| 32 | Nutrition | https://graduate.unl.edu/academics/programs/NTRN-MS/ |
| 33 | Nutrition and Health Sciences | https://graduate.unl.edu/academics/programs/NUHS-MS/ |
| 34 | Physics and Astronomy | https://graduate.unl.edu/academics/programs/PHYA-MS/ |
| 35 | Plant Pathology | https://graduate.unl.edu/academics/programs/PLNT-MS/ |
| 36 | Political Science | https://graduate.unl.edu/academics/programs/POLS-MA/ |
| 37 | Psychology | https://graduate.unl.edu/academics/programs/PSYC-MA/ |
| 38 | Sociology | https://graduate.unl.edu/academics/programs/SOCI-MA/ |
| 39 | Speech-Language Pathology & Audiology | https://graduate.unl.edu/academics/programs/SLPA-MS/ |
| 40 | Statistics | https://graduate.unl.edu/academics/programs/STAT-MS/ |
| 41 | Supply Chain Management | https://graduate.unl.edu/academics/programs/SCMS-MS/ |
| 42 | Telecommunications Engineering | https://graduate.unl.edu/academics/programs/TELE-MS/ |
| 43 | Textiles, Merchandising and Fashion Design | https://graduate.unl.edu/academics/programs/TMFD-MS/ |
| 44-52 | Additional MS programs (see graduate.unl.edu for full list) | — |

#### MA (Master of Arts) — 22 programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://graduate.unl.edu/academics/programs/ANTH-MA/ |
| 2 | Art History | https://graduate.unl.edu/academics/programs/ARTH-MA/ |
| 3 | Business | https://graduate.unl.edu/academics/programs/BUSN-MA/ |
| 4 | Communication Studies | https://graduate.unl.edu/academics/programs/COMM-MA/ |
| 5 | Economics | https://graduate.unl.edu/academics/programs/ECON-MA/ |
| 6 | Educational Administration | https://graduate.unl.edu/academics/programs/EDAD-MA/ |
| 7 | Educational Psychology | https://graduate.unl.edu/academics/programs/EDPS-MA/ |
| 8 | English | https://graduate.unl.edu/academics/programs/ENGL-MA/ |
| 9 | Geography | https://graduate.unl.edu/academics/programs/GEOG-MA/ |
| 10 | History | https://graduate.unl.edu/academics/programs/HIST-MA/ |
| 11 | Journalism and Mass Communications | https://graduate.unl.edu/academics/programs/JAMC-MA/ |
| 12 | Modern Languages and Literatures | https://graduate.unl.edu/academics/programs/MODL-MA/ |
| 13 | Philosophy | https://graduate.unl.edu/academics/programs/PHIL-MA/ |
| 14 | Political Science | https://graduate.unl.edu/academics/programs/POLS-MA/ |
| 15 | Psychology | https://graduate.unl.edu/academics/programs/PSYC-MA/ |
| 16 | Sociology | https://graduate.unl.edu/academics/programs/SOCI-MA/ |
| 17 | Special Education | https://graduate.unl.edu/academics/programs/SPED-MA/ |
| 18 | Teaching, Learning and Teacher Education | https://graduate.unl.edu/academics/programs/TEAC-MA/ |
| 19 | Textiles, Merchandising and Fashion Design | https://graduate.unl.edu/academics/programs/TMFD-MA/ |
| 20-22 | Additional MA programs | — |

#### PhD (Doctor of Philosophy) — 42 programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Economics | https://graduate.unl.edu/academics/programs/AECN-PHD/ |
| 2 | Agronomy and Horticulture | https://graduate.unl.edu/academics/programs/AGRO-PHD/ |
| 3 | Animal Science | https://graduate.unl.edu/academics/programs/ASCI-PHD/ |
| 4 | Architectural Engineering | https://graduate.unl.edu/academics/programs/AREN-PHD/ |
| 5 | Biochemistry | https://graduate.unl.edu/academics/programs/BIOC-PHD/ |
| 6 | Biological Engineering | https://graduate.unl.edu/academics/programs/BENG-PHD/ |
| 7 | Biological Sciences | https://graduate.unl.edu/academics/programs/BIOS-PHD/ |
| 8 | Biomedical Engineering | https://graduate.unl.edu/academics/programs/BIOE-PHD/ |
| 9 | Business | https://graduate.unl.edu/academics/programs/BUSN-PHD/ |
| 10 | Chemical and Biomolecular Engineering | https://graduate.unl.edu/academics/programs/CHBE-PHD/ |
| 11 | Chemistry | https://graduate.unl.edu/academics/programs/CHEM-PHD/ |
| 12 | Civil Engineering | https://graduate.unl.edu/academics/programs/CIVE-PHD/ |
| 13 | Communication Studies | https://graduate.unl.edu/academics/programs/COMM-PHD/ |
| 14 | Complex Biosystems | https://graduate.unl.edu/academics/programs/CBIO-PHD/ |
| 15 | Computer Science | https://graduate.unl.edu/academics/programs/COMP-PHD/ |
| 16 | Earth and Atmospheric Sciences | https://graduate.unl.edu/academics/programs/GEOS-PHD/ |
| 17 | Economics | https://graduate.unl.edu/academics/programs/ECON-PHD/ |
| 18 | Educational Psychology | https://graduate.unl.edu/academics/programs/EDPS-PHD/ |
| 19 | Educational Studies | https://graduate.unl.edu/academics/programs/EDUS-PHD/ |
| 20 | Electrical Engineering | https://graduate.unl.edu/academics/programs/ELEC-PHD/ |
| 21 | Engineering | https://graduate.unl.edu/academics/programs/ENGR-PHD/ |
| 22 | English | https://graduate.unl.edu/academics/programs/ENGL-PHD/ |
| 23 | Entomology | https://graduate.unl.edu/academics/programs/ENTO-PHD/ |
| 24 | Food Science and Technology | https://graduate.unl.edu/academics/programs/FDST-PHD/ |
| 25 | Global Integrative Studies | https://graduate.unl.edu/academics/programs/GIST-PHD/ |
| 26 | History | https://graduate.unl.edu/academics/programs/HIST-PHD/ |
| 27 | Human Sciences | https://graduate.unl.edu/academics/programs/HUMS-PHD/ |
| 28 | Integrative Biomedical Sciences | https://graduate.unl.edu/academics/programs/IBMS-PHD/ |
| 29 | Mathematics | https://graduate.unl.edu/academics/programs/MATH-PHD/ |
| 30 | Mechanical Engineering and Applied Mechanics | https://graduate.unl.edu/academics/programs/MEAM-PHD/ |
| 31 | Modern Languages and Literatures | https://graduate.unl.edu/academics/programs/MODL-PHD/ |
| 32 | Music | https://graduate.unl.edu/academics/programs/MUSC-PHD/ |
| 33 | Natural Resource Sciences | https://graduate.unl.edu/academics/programs/NRSC-PHD/ |
| 34 | Nutrition | https://graduate.unl.edu/academics/programs/NTRN-PHD/ |
| 35 | Philosophy | https://graduate.unl.edu/academics/programs/PHIL-PHD/ |
| 36 | Physics and Astronomy | https://graduate.unl.edu/academics/programs/PHYA-PHD/ |
| 37 | Plant Pathology | https://graduate.unl.edu/academics/programs/PLNT-PHD/ |
| 38 | Political Science | https://graduate.unl.edu/academics/programs/POLS-PHD/ |
| 39 | Psychology | https://graduate.unl.edu/academics/programs/PSYC-PHD/ |
| 40 | Sociology | https://graduate.unl.edu/academics/programs/SOCI-PHD/ |
| 41 | Statistics | https://graduate.unl.edu/academics/programs/STAT-PHD/ |
| 42 | Veterinary Medicine | https://graduate.unl.edu/academics/programs/VMED-DVM/ |

#### Other Graduate Degrees

| 学位 | 项目 | URL |
|------|------|-----|
| MPAcc | Accountancy | https://graduate.unl.edu/academics/programs/ACCT-MPAC/ |
| MBA | Business | https://graduate.unl.edu/academics/programs/BUSN-MBA/ |
| MFA | Art | https://graduate.unl.edu/academics/programs/ART-MFA/ |
| MFA | Theatre Arts | https://graduate.unl.edu/academics/programs/THEA-MFA/ |
| MEd | Educational Administration | https://graduate.unl.edu/academics/programs/EDAD-MED/ |
| MEd | Special Education | https://graduate.unl.edu/academics/programs/SPED-MED/ |
| MEd | Teaching, Learning and Teacher Education | https://graduate.unl.edu/academics/programs/TEAC-MED/ |
| MPA | Public Administration | https://graduate.unl.edu/academics/programs/ACCT-MPAC/ |
| MArch | Architecture | https://graduate.unl.edu/academics/programs/ARCH-MARC/ |
| MAE | Architectural Engineering | https://graduate.unl.edu/academics/programs/AREN-MARE/ |
| MAS | Applied Science | https://graduate.unl.edu/academics/programs/APSC-MAS/ |
| MAT | Mathematics | https://graduate.unl.edu/academics/programs/MATH-MAT/ |
| MM | Music | https://graduate.unl.edu/academics/programs/MUSC-MM/ |
| MLS | Legal Studies | https://graduate.unl.edu/academics/programs/LGLS-MLS/ |
| MCRP | Community and Regional Planning | https://graduate.unl.edu/academics/programs/CRPL-MCRP/ |
| MEGM | Engineering Management | https://graduate.unl.edu/academics/programs/EMGT-MEGM/ |
| AuD | Audiology and Hearing Science | https://graduate.unl.edu/academics/programs/AUHS-AUD/ |
| DMA | Music | https://graduate.unl.edu/academics/programs/MUSC-DMA/ |
| DVM | Veterinary Medicine | https://graduate.unl.edu/academics/programs/VMED-DVM/ |
| EdD | Educational Administration | https://graduate.unl.edu/academics/programs/EDAD-EDD/ |
| EdD | Educational Studies | https://graduate.unl.edu/academics/programs/EDUS-EDD/ |
| EdS | Educational Psychology | https://graduate.unl.edu/academics/programs/EDPS-EDS/ |
| EdS | Teaching, Learning and Teacher Education | https://graduate.unl.edu/academics/programs/TEAC-EDS/ |

#### Graduate Certificates (43 programs)

| # | 项目 | URL |
|---|------|-----|
| 1 | Additive Manufacturing | https://graduate.unl.edu/academics/programs/ADMA-GCER/ |
| 2 | Advanced Horticulture | https://graduate.unl.edu/academics/programs/AHRT-GCER/ |
| 3 | Agronomy | https://graduate.unl.edu/academics/programs/AGRO-GCER/ |
| 4 | Bioanalytical Chemistry | https://graduate.unl.edu/academics/programs/BIOA-GCER/ |
| 5 | Business Analytics | https://graduate.unl.edu/academics/programs/BSAN-GCER/ |
| 6 | Chromatography and Analytical Separations | https://graduate.unl.edu/academics/programs/CHRM-GCER/ |
| 7 | Community College Leadership | https://graduate.unl.edu/academics/programs/CCLD-GCER/ |
| 8 | Computational Artificial Intelligence | https://graduate.unl.edu/academics/programs/COAI-GCER/ |
| 9 | Construction Engineering and Management | https://graduate.unl.edu/academics/programs/CEMT-GCER/ |
| 10 | Digital Humanities | https://graduate.unl.edu/academics/programs/DIGH-GCER/ |
| 11 | Early Childhood and Family Policy | https://graduate.unl.edu/academics/programs/ECFP-GCER/ |
| 12 | Early Childhood Special Education | https://graduate.unl.edu/academics/programs/ECSE-GCER/ |
| 13 | Early Literacy | https://graduate.unl.edu/academics/programs/ELIT-GCER/ |
| 14 | Educational Neuroscience | https://graduate.unl.edu/academics/programs/EDNR-GCER/ |
| 15 | Engineering Management | https://graduate.unl.edu/academics/programs/EMGT-GCER/ |
| 16 | Entomology | https://graduate.unl.edu/academics/programs/ENTO-GCER/ |
| 17 | Family Financial Planning | https://graduate.unl.edu/academics/programs/FFPL-GCER/ |
| 18 | Financial Analytics | https://graduate.unl.edu/academics/programs/FNAN-GCER/ |
| 19 | Financial Communications | https://graduate.unl.edu/academics/programs/FNCO-GCER/ |
| 20 | Financial Counseling | https://graduate.unl.edu/academics/programs/FHOC-GCER/ |
| 21 | Floriculture and Nursery Production Management | https://graduate.unl.edu/academics/programs/FNPM-GCER/ |
| 22 | Food Safety and Defense | https://graduate.unl.edu/academics/programs/FDSD-GCER/ |
| 23 | Forensic Anthropology | https://graduate.unl.edu/academics/programs/FORA-GCER/ |
| 24 | Geographic Information Science | https://graduate.unl.edu/academics/programs/GISC-GCER/ |
| 25 | Grassland Management | https://graduate.unl.edu/academics/programs/GRSM-GCER/ |
| 26 | Human Resources Management | https://graduate.unl.edu/academics/programs/HRES-GCER/ |
| 27 | Internet of Things | https://graduate.unl.edu/academics/programs/IOTS-GCER/ |
| 28 | K-3 Mathematics Specialist | https://graduate.unl.edu/academics/programs/K3MS-GCER/ |
| 29 | Marketing Analytics | https://graduate.unl.edu/academics/programs/MRKA-GCER/ |
| 30 | Mathematics Education | https://graduate.unl.edu/academics/programs/MAED-GCER/ |
| 31 | Medical/Family Therapy | https://graduate.unl.edu/academics/programs/MFTH-GCER/ |
| 32 | Mixed Methods Research | https://graduate.unl.edu/academics/programs/MMRS-GCER/ |
| 33 | Museum Studies | https://graduate.unl.edu/academics/programs/MUSS-GCER/ |
| 34 | Nutrition, Non-coding RNAs and Extracellular Vesicles | https://graduate.unl.edu/academics/programs/NNEV-GCER/ |
| 35 | Ornamentals, Landscape and Turf | https://graduate.unl.edu/academics/programs/ORLT-GCER/ |
| 36 | Personal Leadership | https://graduate.unl.edu/academics/programs/PRLE-GCER/ |
| 37 | Public Relations and Social Media | https://graduate.unl.edu/academics/programs/PRSM-GCER/ |
| 38 | Quilt Studies | https://graduate.unl.edu/academics/programs/QLTS-GCER/ |
| 39 | Response to Intervention: Reading | https://graduate.unl.edu/academics/programs/RINR-GCER/ |
| 40 | Rural Economic and Community Vitality | https://graduate.unl.edu/academics/programs/RECV-GCER/ |
| 41 | Sales Excellence | https://graduate.unl.edu/academics/programs/SALE-GCER/ |
| 42 | Sensory Disabilities | https://graduate.unl.edu/academics/programs/SDIS-GCER/ |
| 43 | Social Justice and Diversity Education | https://graduate.unl.edu/academics/programs/SJUS-GCER/ |
| 44 | Sports Promotion | https://graduate.unl.edu/academics/programs/SPPR-GCER/ |
| 45 | Strategic Innovation and Entrepreneurship | https://graduate.unl.edu/academics/programs/SIEN-GCER/ |
| 46 | Strategic Marketing | https://graduate.unl.edu/academics/programs/STMK-GCER/ |
| 47 | Supply Chain Analytics | https://graduate.unl.edu/academics/programs/SCAN-GCER/ |
| 48 | Supply Chain Management | https://graduate.unl.edu/academics/programs/SCMS-GCER/ |
| 49 | Teaching English to Speakers of Other Languages | https://graduate.unl.edu/academics/programs/TESO-GCER/ |
| 50 | Teaching of Writing | https://graduate.unl.edu/academics/programs/TWRT-GCER/ |
| 51 | Urban Design | https://graduate.unl.edu/academics/programs/URDS-GCER/ |
| 52 | World Language Teaching: German | https://graduate.unl.edu/academics/programs/WLTG-GCER/ |
| 53 | World Language Teaching: Spanish | https://graduate.unl.edu/academics/programs/WLTS-GCER/ |
| 54 | Youth Development | https://graduate.unl.edu/academics/programs/YTHD-GCER/ |

### 2.2 Graduate Admissions Model

**Centralized application, decentralized decisions.** Graduate Studies (graduate.unl.edu) provides a single application portal (go.unl.edu/gradapp), but each department/program sets its own deadlines, requirements, and admission decisions. Application fee: $50 (non-UNL applicants), $25 (currently enrolled UNL students). Fee waivers available for military, Pell Grant recipients, McNair Scholars, and Big Ten Academic Alliance FreeApp participants.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | Source |
|------|-----|--------|
| **Admissions Website** | https://admissions.unl.edu/ | admissions.unl.edu |
| **Application Portal** | Common App OR Nebraska's Application (wam.unl.edu/admission/start) | admissions.unl.edu/apply/ |
| **Application Fee** | $45 (domestic), $45 (international) | admissions.unl.edu/apply/admission-requirements/international/ |
| **Priority Deadline** | November 1 (for scholarship notification Feb 11) | admissions.unl.edu/apply/first-year-dates-deadlines/ |
| **Final Deadline** | May 1 (application + enrollment deposit due) | admissions.unl.edu/apply/first-year-dates-deadlines/ |
| **Spring Deadline** | December 1 | admissions.unl.edu/apply/ |
| **SAT/ACT Policy** | **Test-optional** — "You are not required to submit an ACT/SAT score to be considered for admission." | admissions.unl.edu/apply/admission-requirements/first-year/ |
| **SAT Code** | 6877 | admissions.unl.edu/apply/admission-requirements/international/ |
| **ACT Code** | 2482 | admissions.unl.edu/apply/admission-requirements/international/ |
| **Superscore** | Not specified | — |
| **Recommendation** | Not required | — |
| **Interview** | Not required | — |
| **Portfolio** | Required for Hixson-Lied College of Fine & Performing Arts (audition/portfolio) | admissions.unl.edu/apply/admission-requirements/first-year/ |

**Assured Admission Requirements (First-Year):**
- 3.0 cumulative high school GPA, OR
- ACT composite 20+, OR
- SAT 1040+ (Critical Reading + Math), OR
- Top 50% of graduating class

**Core Course Requirements (16 units):**
- English: 4 units
- Mathematics: 4 units (Algebra I, Algebra II, Geometry, + 1 advanced)
- Natural Sciences: 3 units (2 from bio/chem/physics/earth sci, 1 with lab)
- Social Sciences: 3 units
- World Language: 2 units (same language)

**College-Specific Additional Requirements:**
- **Architecture**: ACT 22+ or SAT 1110+; top 25% or GPA 3.2; Math 4 units including Pre-Calc/Trig
- **Engineering**: ACT 24+ or SAT 1180+; OR ACT Math 24+ or SAT Math 580+; OR GPA 3.5; Math 4 units including Pre-Calc/Trig; Sciences must include chemistry + physics
- **Business**: Transfer GPA 2.5+
- **Fine & Performing Arts**: Audition and/or portfolio required

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum (General Admission) | Minimum Subscore | College-Specific Minimums |
|------|---------------------------|------------------|--------------------------|
| **TOEFL iBT (new scale, after Jan 21, 2026)** | 4.0 | 4.0 | Architecture: 4.0; Engineering: 4.0; Journalism: 5.0 |
| **TOEFL iBT (old scale, before Jan 21, 2026)** | 79 | 18 | Architecture: 79; Education & Human Sciences: 79; Engineering: 80; Journalism: 100 |
| **TOEFL Paper-Based** | 550 | 55 | Architecture: 550; Engineering: 550; Journalism: 600 |
| **IELTS (Academic)** | 6.5 | 6.0 | Architecture: 6.5; Engineering: 6.5; Journalism: 7.0 |
| **Duolingo English Test** | 110 | 105 | Architecture: 110; Education & Human Sciences: 120; Engineering: 110; Journalism: 120 |
| **ACT English Subscore** | 20 | — | Architecture: 22; Education & Human Sciences: 22; Engineering: 22; Journalism: 24 |
| **SAT Digital Reading & Writing** | 520 | — | — |
| **Nebraska ELT** | 80 | 78 | Architecture: 80; Engineering: 80; Journalism: 85 |

**Exemptions**: Graduation from a US high school; completion of 30 transferable semester hours at a US college.

> **Source**: admissions.unl.edu/apply/admission-requirements/international/

### 3.3 Graduate — Global Rules

| 字段 | 值 | Source |
|------|-----|--------|
| **Application Portal** | go.unl.edu/gradapp | graduate.unl.edu/admissions/ |
| **Application Fee** | $50 (non-UNL); $25 (current UNL students) | graduate.unl.edu (Fee tab) |
| **Fee Waivers** | Military, Pell Grant, McNair Scholars, BTAA FreeApp | graduate.unl.edu (Fee tab) |
| **Deadlines** | Vary by department; rolling programs recommend Jan 7 (financial support), Mar 1 (fall), Sep 1 (spring), Feb 1 (summer) | graduate.unl.edu (Deadlines tab) |
| **GRE Policy** | Per-program (some require, some optional) | graduate.unl.edu/academics/programs/ |
| **TOEFL (old)** | 79 iBT minimum | graduate.unl.edu/english-proficiency/ |
| **TOEFL (new, after Jan 21, 2026)** | 4.0 minimum | graduate.unl.edu/english-proficiency/ |
| **IELTS** | 6.5 overall (Academic only) | graduate.unl.edu/english-proficiency/ |
| **Duolingo** | 120 (accepted through Dec 31, 2026) | graduate.unl.edu/english-proficiency/ |
| **ESL 887 Requirement** | TOEFL writing <25 or total <100; IELTS writing <7.0 or total <7.0 | graduate.unl.edu/english-proficiency/ |
| **Exemptions** | Bachelor's+ degree from English-medium institution | graduate.unl.edu/english-proficiency/ |
| **Institution Code** | 6877 (TOEFL) | graduate.unl.edu/english-proficiency/ |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (Current Academic Year, Line-Itemized)

**In-State (Nebraska Resident):**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $11,472 | 15 credit hours/semester x 2 semesters @ $303/credit hour |
| Housing & Food | $13,950 | Average on-campus housing + 21 meals/week |
| Books & Supplies | $1,128 | Estimated |
| Personal Expenses | $2,324 | Estimated |
| **Total Estimate** | **$28,874** | |

**Out-of-State (Nonresident):**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $31,542 | 15 credit hours/semester x 2 semesters @ $972/credit hour |
| Housing & Food | $13,950 | Average on-campus housing + 21 meals/week |
| Books & Supplies | $1,128 | Estimated |
| Personal Expenses | $2,324 | Estimated |
| **Total Estimate** | **$48,944** | |

**International:**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $31,942 | 15 credit hours/semester x 2 semesters |
| Housing & Food | $13,950 | Average on-campus housing + meals |
| Health Insurance | $3,976 | Required for international students |
| Books & Supplies | $1,128 | Estimated |
| Flights & Transportation | $1,094 | Estimated |
| Personal Expenses | $1,230 | Estimated |
| **Total Estimate** | **$53,320** | Amount required on bank statement for I-20 |

> **Note**: Colleges of Business, Architecture, and Engineering have differential tuition rates. Loan fees estimated at $64 apply to students receiving federal loans.
> **Source**: admissions.unl.edu/cost/

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | Source |
|------|-----|--------|
| **Need-Blind/Need-Aware** | Need-aware for all (domestic and international) | admissions.unl.edu/cost/ |
| **Tuition-Free Threshold** | Not published (no income-based free tuition program) | — |
| **Scholarships** | 97% of first-year students offered scholarship or grant | admissions.unl.edu/ |
| **Test-Preferred for Scholarships** | "You can maximize your consideration for departmental scholarships... by submitting an official ACT/SAT score" | admissions.unl.edu/cost/ |
| **Priority Scholarship Deadline** | November 1 (notification February 11) | admissions.unl.edu/apply/first-year-dates-deadlines/ |
| **FAFSA Priority** | February 1 for Nov 1 applicants; May 1 for others | admissions.unl.edu/apply/first-year-dates-deadlines/ |
| **Net Price Calculator** | Available at tcc.ruffalonl.com | admissions.unl.edu/cost/ |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | Source |
|------|-----|--------|
| **Application Fee** | $50 (non-UNL); $25 (current UNL) | graduate.unl.edu |
| **Funding Types** | RA/TA/fellowships available; varies by department | graduate.unl.edu/funding/ |
| **Financial Support Recommendation** | Apply by January 7 for fall financial support consideration | graduate.unl.edu (Deadlines tab) |

---

## SECTION 5 — Evidence Chain Index

```yaml
---
field: undergraduate.deadlines.priority
value: "November 1"
source_url: "https://admissions.unl.edu/apply/first-year-dates-deadlines/"
source_snippet: "Priority Deadline: Apply for admission by this date to be notified of scholarship awards on February 11."
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.deadlines.final
value: "May 1"
source_url: "https://admissions.unl.edu/apply/first-year-dates-deadlines/"
source_snippet: "Fall 2027 application for admission and enrollment deposit due."
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.test_policy
value: "Test-optional"
source_url: "https://admissions.unl.edu/apply/admission-requirements/first-year/"
source_snippet: "You are not required to submit an ACT/SAT score to be considered for admission."
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: undergraduate.cost.in_state_tuition
value: "$11,472"
source_url: "https://admissions.unl.edu/cost/"
source_snippet: "Tuition & Fees: $11,472"
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.cost.oos_tuition
value: "$31,542"
source_url: "https://admissions.unl.edu/cost/"
source_snippet: "Tuition & Fees: $31,542"
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.cost.international_total
value: "$53,320"
source_url: "https://admissions.unl.edu/cost/"
source_snippet: "Total Estimate: $53,320"
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.admission.gpa_requirement
value: "3.0 cumulative GPA (assured admission)"
source_url: "https://admissions.unl.edu/apply/admission-requirements/first-year/"
source_snippet: "Have a 3.0 cumulative high school grade point average."
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: undergraduate.english_proficiency.toefl
value: "79 iBT (old) / 4.0 (new after Jan 21, 2026)"
source_url: "https://admissions.unl.edu/apply/admission-requirements/international/"
source_snippet: "TOEFL Minimum Test Scores: Internet-Based (old): General Admission: 79; Internet-Based (new): General Admission: 4.0"
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.english_proficiency.ielts
value: "6.5 overall, 6.0 minimum subscore"
source_url: "https://admissions.unl.edu/apply/admission-requirements/international/"
source_snippet: "IELTS Minimum Test Scores: General Admission: 6.5, Minimum Subscore: 6.0"
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.english_proficiency.duolingo
value: "110, 105 minimum subscore"
source_url: "https://admissions.unl.edu/apply/admission-requirements/international/"
source_snippet: "Duolingo English Test Minimum Test Scores: General Admission: 110, Minimum Subscore: 105"
capture_date: 2026-07-07
evidence_type: official_webpage_table
---
field: undergraduate.application_fee
value: "$45"
source_url: "https://admissions.unl.edu/apply/admission-requirements/international/"
source_snippet: "The USD$45 application fee is payable online with a credit card."
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: graduate.application_fee
value: "$50 (non-UNL), $25 (current UNL)"
source_url: "https://cms.unl.edu/executive-vice-chancellor/graduate-studies/application-requirements-additional-details/"
source_snippet: "$50 – All applicants not currently enrolled at UNL; $25 – Currently enrolled UNL students"
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: graduate.english_proficiency.toefl
value: "79 iBT (old) / 4.0 (new after Jan 21, 2026)"
source_url: "https://cms.unl.edu/executive-vice-chancellor/graduate-studies/english-proficiency/"
source_snippet: "For tests taken prior to January 21, 2026, score of at least 79 (iBT). For tests taken after January 21, 2026, minimum score required: 4."
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: graduate.english_proficiency.ielts
value: "6.5 overall (Academic only)"
source_url: "https://cms.unl.edu/executive-vice-chancellor/graduate-studies/english-proficiency/"
source_snippet: "An overall band score of at least 6.5 on the academic test."
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: graduate.english_proficiency.duolingo
value: "120"
source_url: "https://cms.unl.edu/executive-vice-chancellor/graduate-studies/english-proficiency/"
source_snippet: "Graduate minimum score of 120."
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: programs.undergraduate.total
value: "132 majors + 68 minors = 200 catalog entries"
source_url: "https://catalog.unl.edu/undergraduate/majors/"
source_snippet: "Displaying: All Options" (200 program links extracted)
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: programs.graduate.total
value: "191 programs"
source_url: "https://graduate.unl.edu/academics/programs"
source_snippet: "191 program links extracted from graduate.unl.edu/academics/programs"
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: institution.type
value: "Public, Land-grant, Big Ten"
source_url: "https://www.unl.edu/"
source_snippet: "UNIVERSITY of NEBRASKA–LINCOLN" (Big Ten Conference membership)
capture_date: 2026-07-07
evidence_type: official_webpage
---
field: undergraduate.aid.scholarship_rate
value: "97% of first-year students offered scholarship or grant"
source_url: "https://admissions.unl.edu/"
source_snippet: "97% of first-year students are offered a scholarship or grant to attend Nebraska."
capture_date: 2026-07-07
evidence_type: official_webpage
---
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
unl-knowledge-base-v2/
├── 00-institution-overview          (Section 0: rules 1-4, counts, hierarchy, matrix)
├── 01-ug-college-casnr             (Section 1: CASNR majors)
├── 02-ug-college-architecture      (Section 1: Architecture majors)
├── 03-ug-college-arts-sciences     (Section 1: A&S majors)
├── 04-ug-college-business          (Section 1: Business majors)
├── 05-ug-college-education         (Section 1: CEHS majors)
├── 06-ug-college-engineering       (Section 1: Engineering majors)
├── 07-ug-college-fine-performing   (Section 1: FPA majors)
├── 08-ug-college-journalism        (Section 1: Journalism majors)
├── 09-ug-college-public-affairs    (Section 1: PACS majors)
├── 10-ug-minors                    (Section 1.4: all minors)
├── 11-grad-ms-programs             (Section 2: MS programs)
├── 12-grad-ma-programs             (Section 2: MA programs)
├── 13-grad-phd-programs            (Section 2: PhD programs)
├── 14-grad-other-degrees           (Section 2: MBA, MFA, EdD, etc.)
├── 15-grad-certificates            (Section 2: certificates)
├── 16-deadlines-requirements       (Section 3: UG + grad requirements)
├── 17-costs-financial-aid          (Section 4: costs + aid policy)
└── 18-evidence-chain               (Section 5: all evidence blocks)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "unl-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Verify exact UG degree types per program (BA vs BS vs BFA) from individual catalog pages | catalog.unl.edu/undergraduate/*/ |
| P0 | Get graduate tuition rates (not published on admissions site) | studentaccounts.unl.edu |
| P1 | Per-program GRE requirements for graduate programs | graduate.unl.edu/academics/programs/*/ |
| P1 | College-specific differential tuition rates | studentaccounts.unl.edu/tuition-and-fees/ |
| P2 | Detailed scholarship amounts and criteria | admissions.unl.edu/cost/scholarships/ |
| P2 | Honors Program admission details | admissions.unl.edu/information-for/high-achieving/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | UNL | (Other Schools) |
|------|-----|-----------------|
| Type | Public, Land-grant, Big Ten | |
| Location | Lincoln, NE | |
| UG Tuition (In-State) | $11,472/yr | |
| UG Tuition (OOS) | $31,542/yr | |
| UG Total COA (In-State) | $28,874/yr | |
| UG Total COA (OOS) | $48,944/yr | |
| Need-Blind? | Need-aware (all) | |
| EA Deadline | N/A (Priority: Nov 1) | |
| RD Deadline | May 1 | |
| SAT/ACT Required? | No (test-optional) | |
| TOEFL Min (UG) | 79 (old) / 4.0 (new) | |
| IELTS Min (UG) | 6.5 | |
| Duolingo Min (UG) | 110 | |
| Grad App Fee | $50 | |
| Total UG Majors | 132 | |
| Total UG Minors | 68 | |
| Total Grad Programs | 191 | |
| Total Program Count (Rule 1) | 343 | |
| School/College Count (Rule 2) | 9 (UG) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: admissions.unl.edu, graduate.unl.edu, catalog.unl.edu, cms.unl.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
