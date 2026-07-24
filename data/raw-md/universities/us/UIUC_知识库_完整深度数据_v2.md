# University of Illinois Urbana-Champaign (UIUC) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BLA/BLS/BSW) | 186 |
| 本科辅修 (Minor) | 121 |
| 研究生学位项目 (MA/MS/PhD/MFA/MBA/EdD/etc.) | 272 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 36 |
| 研究生辅修 (Graduate Minor) | 30 |
| 专业学位 (Professional: JD/MD/DVM/MD-PhD) | 4 |
| **学位项目总计** | **649** |
| 学院 / 独立系所总数 | 16 |

### 0.2 学院 / 系层级结构

```
University of Illinois Urbana-Champaign
├── College of Agricultural, Consumer & Environmental Sciences (ACES) [学院]
│   ├── Agricultural & Biological Engineering [系]
│   ├── Agricultural & Consumer Economics [系]
│   ├── Animal Sciences [系]
│   ├── Crop Sciences [系]
│   ├── Food Science & Human Nutrition [系]
│   ├── Human Development & Family Studies [系]
│   ├── Natural Resources & Environmental Sciences [系]
│   └── ... (19 UG majors, 19 minors, 23 grad degrees, 5 grad certs)
├── College of Applied Health Sciences (AHS) [学院]
│   ├── Community Health [系]
│   ├── Kinesiology [系]
│   ├── Recreation, Sport & Tourism [系]
│   ├── Speech & Hearing Science [系]
│   └── ... (6 UG majors, 6 minors, 13 grad degrees, 7 grad certs)
├── College of Education (EDUC) [学院]
│   ├── Curriculum & Instruction [系]
│   ├── Educational Psychology [系]
│   ├── Education Policy, Organization & Leadership [系]
│   └── ... (7 UG majors, 1 minor, 21 grad degrees, 6 grad certs)
├── College of Fine & Applied Arts (FAA) [学院]
│   ├── Architecture [系]
│   ├── Art & Design [系]
│   ├── Dance [系]
│   ├── Landscape Architecture [系]
│   ├── Music [系]
│   ├── Theatre [系]
│   └── ... (31 UG majors, 12 minors, 23 grad degrees, 2 grad certs)
├── Gies College of Business (BUS) [学院]
│   ├── Accountancy [系]
│   ├── Business Administration [系]
│   ├── Finance [系]
│   ├── Information Systems [系]
│   ├── Management [系]
│   ├── Marketing [系]
│   ├── Operations Management [系]
│   └── ... (10 UG majors, 4 minors, 10 grad degrees, 12 grad certs)
├── Grainger College of Engineering (ENGR) [学院]
│   ├── Aerospace Engineering [系]
│   ├── Bioengineering [系]
│   ├── Chemical & Biomolecular Engineering [系] ⚠ shared with LAS
│   ├── Civil & Environmental Engineering [系]
│   ├── Computer Science [系]
│   ├── Electrical & Computer Engineering [系]
│   ├── Industrial & Enterprise Systems Engineering [系]
│   ├── Materials Science & Engineering [系]
│   ├── Mechanical Science & Engineering [系]
│   ├── Nuclear, Plasma & Radiological Engineering [系]
│   ├── Physics [系] ⚠ shared with LAS
│   ├── Systems Engineering & Design [系]
│   └── ... (30 UG majors, 9 minors, 37 grad degrees, 1 grad cert)
├── School of Information Sciences (iSchool) [学院]
│   ├── Information Sciences [系]
│   ├── Information Systems [系]
│   └── ... (2 UG majors, 2 minors, 9 grad degrees)
├── College of Law (LAW) [学院]
│   ├── Law [系]
│   └── ... (1 professional JD, 3 grad degrees)
├── College of Liberal Arts & Sciences (LAS) [学院]
│   ├── Anthropology [系]
│   ├── Astronomy [系]
│   ├── Atmospheric Sciences [系]
│   ├── Chemistry [系]
│   ├── Classics [系]
│   ├── Communication [系]
│   ├── Computer Science [系] ⚠ shared with Engineering
│   ├── Economics [系]
│   ├── English [系]
│   ├── Geography [系]
│   ├── Geology [系]
│   ├── History [系]
│   ├── Linguistics [系]
│   ├── Mathematics [系]
│   ├── Molecular & Cellular Biology [系]
│   ├── Philosophy [系]
│   ├── Physics [系] ⚠ shared with Engineering
│   ├── Political Science [系]
│   ├── Psychology [系]
│   ├── Sociology [系]
│   ├── Statistics [系]
│   └── ... (70 UG majors, 57 minors, 104 grad degrees, 16 grad minors)
├── College of Media (MDIA) [学院]
│   ├── Advertising [系]
│   ├── Journalism [系]
│   ├── Media & Cinema Studies [系]
│   └── ... (6 UG majors, 6 minors, 4 grad degrees)
├── School of Social Work (SOCW) [学院]
│   ├── Social Work [系]
│   └── ... (1 UG major, 1 minor, 5 grad degrees)
├── College of Veterinary Medicine (VETMED) [学院]
│   ├── Veterinary Medicine [系]
│   └── ... (11 grad degrees, 1 professional DVM)
├── Carle Illinois College of Medicine (CIMED) [学院]
│   ├── Medicine [系]
│   └── ... (1 MD, 1 MD/PhD)
├── School of Labor & Employment Relations (LER) [学院]
│   ├── Labor & Employment Relations [系]
│   └── ... (4 grad degrees, 3 grad certs)
├── Graduate College [学院]
│   └── (administers graduate programs across all colleges)
└── Division of Exploratory Studies [学院]
    └── (undeclared students)
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 123 |
| BA | Bachelor of Arts | 本科 | 45 |
| BFA | Bachelor of Fine Arts | 本科 | 8 |
| BM | Bachelor of Music | 本科 | 6 |
| BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| BLS | Bachelor of Liberal Studies | 本科 | 1 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| MS | Master of Science | 研究生 | 89 |
| PhD | Doctor of Philosophy | 研究生 | 90 |
| MA | Master of Arts | 研究生 | 34 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| EdM | Master of Education | 研究生 | 8 |
| MBA | Master of Business Administration | 研究生 | 1 |
| EdD | Doctor of Education | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 2 |
| MSW | Master of Social Work | 研究生 | 2 |
| MAS | Master of Accounting Science | 研究生 | 1 |
| MSA | Master of Science in Accountancy | 研究生 | 1 |
| MCS | Master of Computer Science | 研究生 | 1 |
| MARCH | Master of Architecture | 研究生 | 1 |
| MUP | Master of Urban Planning | 研究生 | 1 |
| MLA | Master of Landscape Architecture | 研究生 | 1 |
| MHA | Master of Health Administration | 研究生 | 1 |
| MHRIR | Master of Human Resources & Industrial Relations | 研究生 | 2 |
| MMus | Master of Music | 研究生 | 1 |
| MVS | Master of Veterinary Science | 研究生 | 2 |
| PSM | Professional Science Master | 研究生 | 4 |
| LLM | Master of Laws | 研究生 | 1 |
| CAS | Certificate of Advanced Study | 研究生 | 5 |
| MDes | Master of Design | 研究生 | 1 |
| MATESL | Master of Arts in Teaching ESL | 研究生 | 1 |
| MAAE | Master of Arts in Art Education | 研究生 | 1 |
| MANSC | Master of Animal Sciences | 研究生 | 1 |
| MME | Master of Music Education | 研究生 | 1 |
| MSL | Master of Studies in Law | 研究生 | 1 |
| MSUD | Master of Sustainable Urban Design | 研究生 | 1 |
| JSD | Doctor of Juridical Science | 研究生 | 1 |
| AD | Advanced Diploma | 研究生 | 1 |
| AMusD | Doctor of Musical Arts | 研究生 | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| Joint | Joint Degree | 研究生 | 1 |
| JD | Juris Doctor | 专业 | 1 |
| MD | Doctor of Medicine | 专业 | 1 |
| DVM | Doctor of Veterinary Medicine | 专业 | 1 |

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院 \ 级别 | BS | BA | BFA | BM | BLA | BLS | BSW | MS | PhD | MA | MFA | EdM | MBA | EdD | MPH | MSW | MAS | MSA | MCS | MARCH | MUP | MLA | MHA | MHRIR | MMus | MVS | PSM | LLM | CAS | MDes | MATESL | MAAE | MANSC | MME | MSL | MSUD | JSD | AD | AMusD | AuD | Joint | JD | MD | DVM | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Agricultural, Consumer & Environmental Sciences | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 42 |
| College of Applied Health Sciences | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 4 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 19 |
| Gies College of Business | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 22 |
| Carle Illinois College of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| College of Education | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 4 | 3 | 0 | 7 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 28 |
| Grainger College of Engineering | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 64 |
| College of Fine & Applied Arts | 8 | 8 | 7 | 6 | 1 | 0 | 0 | 1 | 7 | 2 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 53 |
| School of Information Sciences | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| College of Liberal Arts & Sciences | 35 | 35 | 1 | 0 | 0 | 1 | 0 | 36 | 39 | 28 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 178 |
| College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 |
| School of Labor and Employment Relations | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| College of Media | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| School of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 6 |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 12 |
| **合计** | 123 | 45 | 8 | 6 | 1 | 1 | 1 | 89 | 90 | 34 | 4 | 8 | 1 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 4 | 1 | 5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 454 |

> Reconciliation: Rule-1 degree total (462) == matrix cell-sum (454) ⚠️ MISMATCH

---

## Section 1 — Undergraduate Education

### 1.1 College/school architecture

UIUC has 16 colleges/schools granting undergraduate degrees. The largest is the College of Liberal Arts & Sciences (LAS) with 70 UG majors, followed by Fine & Applied Arts (31) and Grainger Engineering (30). See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural, Consumer & Environmental Sciences

##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Agricultural & Biological Engineering Sciences | https://catalog.illinois.edu/undergraduate/eng_aces/agricultural-biological-engineering-bs-agricultural-engineering-agricultural-science-bsag/ |

| 2 | Agricultural & Consumer Economics | https://catalog.illinois.edu/undergraduate/aces/agricultural-consumer-economics-bs/ |

| 3 | Agricultural Leadership, Education, & Communications | https://catalog.illinois.edu/undergraduate/aces/agricultural-leadership-education-communications-bs/ |

| 4 | Agronomy | https://catalog.illinois.edu/undergraduate/aces/agronomy-bs/ |

| 5 | Animal Sciences | https://catalog.illinois.edu/undergraduate/aces/animal-sciences-bs/ |

| 6 | Computer Science + Animal Sciences | https://catalog.illinois.edu/undergraduate/eng_aces/computer-science-animal-sciences-bs/ |

| 7 | Computer Science + Animal Sciences | https://catalog.illinois.edu/undergraduate/eng_aces/computer-science-animal-sciences-bs-mansc/ |

| 8 | Computer Science + Crop Sciences | https://catalog.illinois.edu/undergraduate/eng_aces/computer-science-crop-sciences-bs/ |

| 9 | Computer Science + Crop Sciences | https://catalog.illinois.edu/undergraduate/eng_aces/computer-science-crop-sciences-bs-ms/ |

| 10 | Crop Sciences | https://catalog.illinois.edu/undergraduate/aces/crop-sciences-bs/ |

| 11 | Dietetics | https://catalog.illinois.edu/undergraduate/aces/dietetics-nutrition-bs/ |

| 12 | Engineering Technology & Management for Agricultural Systems | https://catalog.illinois.edu/undergraduate/aces/engineering-technology-management-agricultural-systems-bs/ |

| 13 | Food Science | https://catalog.illinois.edu/undergraduate/aces/food-science-bs/ |

| 14 | Hospitality Management | https://catalog.illinois.edu/undergraduate/aces/hospitality-management-bs/ |

| 15 | Human Development & Family Studies | https://catalog.illinois.edu/undergraduate/aces/human-development-family-studies-bs/ |

| 16 | Natural Resources & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/natural-resources-environmental-sciences-bs/ |

| 17 | Nutrition | https://catalog.illinois.edu/undergraduate/aces/nutrition-health-bs/ |

| 18 | Plant Biotechnology | https://catalog.illinois.edu/undergraduate/aces/plant-biotechnology-bs/ |

| 19 | Sustainability in Food & Environmental Systems | https://catalog.illinois.edu/undergraduate/aces/sustainability-food-environmental-systems-bs/ |



#### College of Applied Health Sciences

##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Community Health | https://catalog.illinois.edu/undergraduate/ahs/community-health-bs/ |

| 2 | Interdisciplinary Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/interdisciplinary-health-sciences-bs/ |

| 3 | Kinesiology | https://catalog.illinois.edu/undergraduate/ahs/kinesiology-bs/.BA/BS |

| 4 | Public Health | https://catalog.illinois.edu/undergraduate/ahs/public-health-bs/ |

| 5 | Recreation, Sport & Tourism | https://catalog.illinois.edu/undergraduate/ahs/recreation-sport-tourism-bs/ |

| 6 | Speech & Hearing Science | https://catalog.illinois.edu/undergraduate/ahs/speech-hearing-science-bs/ |



#### Gies College of Business

##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Accountancy | https://catalog.illinois.edu/undergraduate/bus/accountancy-bs/ |

| 2 | Accountancy + Data Science | https://catalog.illinois.edu/undergraduate/bus/accountancy-data-science-bs/ |

| 3 | Business + Data Science | https://catalog.illinois.edu/undergraduate/bus/business-data-science-bs/ |

| 4 | Finance | https://catalog.illinois.edu/undergraduate/bus/finance-bs/ |

| 5 | Finance + Data Science | https://catalog.illinois.edu/undergraduate/bus/finance-data-science-bs/ |

| 6 | Information Systems | https://catalog.illinois.edu/undergraduate/bus/information-systems-bs/ |

| 7 | Management | https://catalog.illinois.edu/undergraduate/bus/management-business-bs/ |

| 8 | Marketing | https://catalog.illinois.edu/undergraduate/bus/marketing-bs/ |

| 9 | Operations Management | https://catalog.illinois.edu/undergraduate/bus/operations-management-bs/ |

| 10 | Strategy, Innovation, and Entrepreneurship | https://catalog.illinois.edu/undergraduate/bus/strategy-innovation-entrepreneurship-bs/ |

| 11 | Supply Chain Management | https://catalog.illinois.edu/undergraduate/bus/supply-chain-bs/ |



#### College of Education

##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Computer Science + Education | https://catalog.illinois.edu/undergraduate/education/computer-science-education-bs/ |

| 2 | Early Childhood Education | https://catalog.illinois.edu/undergraduate/education/early-childhood-education-bs/ |

| 3 | Elementary Education | https://catalog.illinois.edu/undergraduate/education/elementary-education-bs/ |

| 4 | Learning & Education Studies | https://catalog.illinois.edu/undergraduate/education/learning-education-studies-bs/ |

| 5 | Middle Grades Education | https://catalog.illinois.edu/undergraduate/education/middle-grades-education-bs/ |

| 6 | Secondary Education | https://catalog.illinois.edu/undergraduate/education/secondary-education-bs/ |

| 7 | Special Education | https://catalog.illinois.edu/undergraduate/education/special-education-bs/ |



#### Grainger College of Engineering

##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Aerospace Engineering | https://catalog.illinois.edu/undergraduate/engineering/aerospace-engineering-bs/ |

| 2 | Aerospace Engineering | https://catalog.illinois.edu/undergraduate/engineering/aerospace-engineering-bs-ms/ |

| 3 | Agricultural & Biological Engineering | https://catalog.illinois.edu/undergraduate/eng_aces/agricultural-biological-engineering-bs/ |

| 4 | Bioengineering | https://catalog.illinois.edu/undergraduate/engineering/bioengineering-bs/ |

| 5 | Chemical Engineering | https://catalog.illinois.edu/undergraduate/las/chemical-engineering-bs/ |

| 6 | Civil Engineering | https://catalog.illinois.edu/undergraduate/engineering/civil-engineering-bs/ |

| 7 | Computer Engineering | https://catalog.illinois.edu/undergraduate/engineering/computer-engineering-bs/ |

| 8 | Computer Engineering | https://catalog.illinois.edu/undergraduate/engineering/computer-electrical-engineering-bs-meng/ |

| 9 | Computer Science | https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs/ |

| 10 | Computer Science | https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs-ms/ |

| 11 | Computer Science | https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs-mcs/ |

| 12 | Computer Science + Bioengineering | https://catalog.illinois.edu/undergraduate/engineering/computer-science-bioengineering-bs/ |

| 13 | Computer Science + Physics | https://catalog.illinois.edu/undergraduate/engineering/computer-science-physics-bs/ |

| 14 | Electrical Engineering | https://catalog.illinois.edu/undergraduate/engineering/electrical-engineering-bs/ |

| 15 | Electrical Engineering | https://catalog.illinois.edu/undergraduate/engineering/electrical-computer-engineering-bs-meng/ |

| 16 | Engineering Mechanics | https://catalog.illinois.edu/undergraduate/engineering/engineering-mechanics-bs/ |

| 17 | Engineering Physics | https://catalog.illinois.edu/undergraduate/engineering/engineering-physics-bs/ |

| 18 | Environmental Engineering | https://catalog.illinois.edu/undergraduate/engineering/environmental-engineering-bs/ |

| 19 | Industrial Engineering | https://catalog.illinois.edu/undergraduate/engineering/industrial-engineering-bs/ |

| 20 | Innovation, Leadership, & Engineering Entrepreneurship | https://catalog.illinois.edu/undergraduate/engineering/innovation-leadership-engineering-entrepreneurship-bs/ |

| 21 | Materials Science & Engineering | https://catalog.illinois.edu/undergraduate/engineering/materials-science-engineering-bs/ |

| 22 | Materials Science & Engineering | https://catalog.illinois.edu/undergraduate/engineering/materials-engineering-bs-ms/ |

| 23 | Materials Science & Engineering | https://catalog.illinois.edu/undergraduate/engineering/materials-engineering-bs-meng/ |

| 24 | Materials Science & Engineering + Data Science | https://catalog.illinois.edu/undergraduate/engineering/materials-science-engineering-data-science-bs/ |

| 25 | Mechanical Engineering | https://catalog.illinois.edu/undergraduate/engineering/mechanical-engineering-bs/ |

| 26 | Neural Engineering | https://catalog.illinois.edu/undergraduate/engineering/neural-engineering-bs/ |

| 27 | Nuclear, Plasma & Radiological Engineering | https://catalog.illinois.edu/undergraduate/engineering/nuclear-plasma-radiological-engineering-bs/ |

| 28 | Nuclear, Plasma, and Radiological Engineering + Data Science | https://catalog.illinois.edu/undergraduate/engineering/nuclear-plasma-radiological-engineering-data-science-bs/ |

| 29 | Physics | https://catalog.illinois.edu/undergraduate/engineering/physics-bs/ |

| 30 | Physics | https://catalog.illinois.edu/undergraduate/engineering/engineering-physics-bs-energy-systems-meng/ |

| 31 | Systems Engineering and Design | https://catalog.illinois.edu/undergraduate/engineering/systems-engineering-design-bs/ |



#### College of Fine & Applied Arts

##### BA

| # | 专业 | URL |
|---|------|-----|

| 1 | Dance | https://catalog.illinois.edu/undergraduate/faa/dance-ba/ |

| 2 | Dance | https://catalog.illinois.edu/undergraduate/ahs_faa/dance-ba-kinesiology-bs/ |

| 3 | Music | https://catalog.illinois.edu/undergraduate/faa/music-ba/ |

| 4 | Studio Art | https://catalog.illinois.edu/undergraduate/faa/studio-art-basa/ |

| 5 | Urban Planning | https://catalog.illinois.edu/undergraduate/faa/urban-studies-planning-ba/ |

| 6 | Urban Planning | https://catalog.illinois.edu/undergraduate/faa/urban-studies-planning-ba-mup/ |

| 7 | Urban Studies Planning | https://catalog.illinois.edu/undergraduate/faa/urban-studies-planning-ba/ |

| 8 | Urban Studies Planning | https://catalog.illinois.edu/undergraduate/faa/urban-studies-planning-ba-mup/ |



##### BFA

| # | 专业 | URL |
|---|------|-----|

| 1 | Art & Design | https://catalog.illinois.edu/undergraduate/faa/academic-units/school-art-design/foundation/ |

| 2 | Art Education | https://catalog.illinois.edu/undergraduate/faa/art-education-bfa/ |

| 3 | Dance | https://catalog.illinois.edu/undergraduate/faa/dance-bfa/ |

| 4 | Graphic Design | https://catalog.illinois.edu/undergraduate/faa/graphic-design-bfa/ |

| 5 | Industrial Design | https://catalog.illinois.edu/undergraduate/faa/industrial-design-bfa/ |

| 6 | Studio Art | https://catalog.illinois.edu/undergraduate/faa/studio-art-bfasa/ |

| 7 | Theatre | https://catalog.illinois.edu/undergraduate/faa/theatre-bfa/ |



##### BLA

| # | 专业 | URL |
|---|------|-----|

| 1 | Landscape Architecture | https://catalog.illinois.edu/undergraduate/faa/landscape-architecture-bla/ |



##### BM

| # | 专业 | URL |
|---|------|-----|

| 1 | Jazz Performance | https://catalog.illinois.edu/undergraduate/faa/jazz-performance-bmus/ |

| 2 | Lyric Theatre | https://catalog.illinois.edu/undergraduate/faa/lyric-theatre-bma/ |

| 3 | Music Composition | https://catalog.illinois.edu/undergraduate/faa/music-composition-bmus/ |

| 4 | Music Education | https://catalog.illinois.edu/undergraduate/faa/music-education-bme/ |

| 5 | Musicology | https://catalog.illinois.edu/undergraduate/faa/musicology-bmus/ |

| 6 | Open Studies | https://catalog.illinois.edu/undergraduate/faa/music-open-studies-bmus/ |



##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Architectural Studies | https://catalog.illinois.edu/undergraduate/faa/architectural-studies-bs/ |

| 2 | Computer Science + Music | https://catalog.illinois.edu/undergraduate/eng_faa/computer-science-music-bs/ |

| 3 | Landscape Architecture | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-bs-landscape-architecture-mla/ |

| 4 | Sustainable Design | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-bs/ |

| 5 | Sustainable Design | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-bs-art-design-responsible-innovation-mfa/ |

| 6 | Sustainable Design | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-urban-planning-bs-mup/ |

| 7 | Sustainable Design | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-bs-landscape-architecture-mla/ |

| 8 | Urban Planning | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-bs-art-design-responsible-innovation-mfa/ |



##### BS+MUP

| # | 专业 | URL |
|---|------|-----|

| 1 | Urban Planning | https://catalog.illinois.edu/undergraduate/faa/sustainable-design-urban-planning-bs-mup/ |



#### School of Information Sciences

##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Information Sciences | https://catalog.illinois.edu/undergraduate/ischool/information-sciences-bs/ |

| 2 | Information Sciences + Data Science | https://catalog.illinois.edu/undergraduate/ischool/information-sciences-data-science-bs/ |



#### College of Liberal Arts & Sciences

##### BA

| # | 专业 | URL |
|---|------|-----|

| 1 | African American Studies | https://catalog.illinois.edu/undergraduate/las/african-american-studies-balas/ |

| 2 | Anthropology | https://catalog.illinois.edu/undergraduate/las/anthropology-balas/ |

| 3 | Art History | https://catalog.illinois.edu/undergraduate/las/art-history-balas/ |

| 4 | Asian American Studies | https://catalog.illinois.edu/undergraduate/las/asian-american-studies-balas/ |

| 5 | Classics | https://catalog.illinois.edu/undergraduate/las/classics-balas/ |

| 6 | Communication | https://catalog.illinois.edu/undergraduate/las/communication-balas/ |

| 7 | Comparative Literature | https://catalog.illinois.edu/undergraduate/las/comparative-world-literature-balas/comparative-literature/ |

| 8 | Creative Writing | https://catalog.illinois.edu/undergraduate/las/creative-writing-balas/ |

| 9 | East Asian Languages & Cultures | https://catalog.illinois.edu/undergraduate/las/east-asian-languages-cultures-balas/ |

| 10 | Economics | https://catalog.illinois.edu/undergraduate/las/economics-balas/ |

| 11 | English | https://catalog.illinois.edu/undergraduate/las/english-balas/ |

| 12 | French | https://catalog.illinois.edu/undergraduate/las/french-balas/ |

| 13 | French Teaching | https://catalog.illinois.edu/undergraduate/las/teaching-french-ba/ |

| 14 | Gender & Women's Studies | https://catalog.illinois.edu/undergraduate/las/gender-womens-studies-balas/ |

| 15 | Geography & Geographic Information Science | https://catalog.illinois.edu/undergraduate/las/geography-geographic-information-science-balas/ |

| 16 | German Teaching | https://catalog.illinois.edu/undergraduate/las/teaching-german-ba/ |

| 17 | Germanic Studies | https://catalog.illinois.edu/undergraduate/las/germanic-studies-balas/ |

| 18 | Global Studies | https://catalog.illinois.edu/undergraduate/las/global-studies-balas/ |

| 19 | History | https://catalog.illinois.edu/undergraduate/las/history-balas/ |

| 20 | Individual Plans of Study | https://catalog.illinois.edu/undergraduate/las/individual-plans-study/ |

| 21 | Interdisciplinary Studies | https://catalog.illinois.edu/undergraduate/las/interdisciplinary-studies-balas/ |

| 22 | Italian | https://catalog.illinois.edu/undergraduate/las/italian-balas/ |

| 23 | Latin American Studies | https://catalog.illinois.edu/undergraduate/las/latin-american-studies-balas/ |

| 24 | Latina/Latino Studies | https://catalog.illinois.edu/undergraduate/las/latina-latino-studies-balas/ |

| 25 | Linguistics | https://catalog.illinois.edu/undergraduate/las/linguistics-balas/ |

| 26 | Linguistics and Teaching English as a Second Language, BALAS (TESL) | https://catalog.illinois.edu/undergraduate/las/linguistics-teaching-english-second-language-tesl-balas/ |

| 27 | Philosophy | https://catalog.illinois.edu/undergraduate/las/philosophy-balas/ |

| 28 | Political Science | https://catalog.illinois.edu/undergraduate/las/political-science-balas/ |

| 29 | Portuguese | https://catalog.illinois.edu/undergraduate/las/portuguese-balas/ |

| 30 | Religion | https://catalog.illinois.edu/undergraduate/las/religion-balas/ |

| 31 | Russian & East European Studies | https://catalog.illinois.edu/undergraduate/las/russian-east-european-eurasian-studies-balas/ |

| 32 | Slavic Studies | https://catalog.illinois.edu/undergraduate/las/slavic-studies-balas/ |

| 33 | Sociology | https://catalog.illinois.edu/undergraduate/las/sociology-balas/ |

| 34 | Spanish | https://catalog.illinois.edu/undergraduate/las/spanish-balas/ |

| 35 | Spanish Teaching | https://catalog.illinois.edu/undergraduate/las/teaching-spanish-ba/ |



##### BFA

| # | 专业 | URL |
|---|------|-----|

| 1 | Art History | https://catalog.illinois.edu/undergraduate/faa/art-art-history-bfa/ |



##### BLS

| # | 专业 | URL |
|---|------|-----|

| 1 | Liberal Studies | https://catalog.illinois.edu/undergraduate/las/liberal-studies-bls/ |



##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Actuarial Science | https://catalog.illinois.edu/undergraduate/las/actuarial-science-bslas/ |

| 2 | Astronomy | https://catalog.illinois.edu/undergraduate/las/astronomy-bslas/ |

| 3 | Astronomy + Data Science | https://catalog.illinois.edu/undergraduate/las/astronomy-data-science-bslas/ |

| 4 | Astrophysics | https://catalog.illinois.edu/undergraduate/las/astrophysics-bslas/ |

| 5 | Atmospheric Sciences | https://catalog.illinois.edu/undergraduate/las/atmospheric-sciences-bslas/ |

| 6 | Biochemistry | https://catalog.illinois.edu/undergraduate/las/biochemistry-bs/ |

| 7 | Biology | https://catalog.illinois.edu/undergraduate/las/integrative-biology-bslas/ |

| 8 | Biology | https://catalog.illinois.edu/undergraduate/las/molecular-cellular-biology-bslas/ |

| 9 | Chemical Engineering + Data Science | https://catalog.illinois.edu/undergraduate/las/chemical-engineering-data-science-bs/index.html |

| 10 | Chemistry | https://catalog.illinois.edu/undergraduate/las/chemistry-bslas/ |

| 11 | Chemistry | https://catalog.illinois.edu/undergraduate/las/chemistry-bs/ |

| 12 | Computer Science + Anthropology | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-anthropology-bslas/ |

| 13 | Computer Science + Astronomy | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-astronomy-bs/ |

| 14 | Computer Science + Chemistry | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-chemistry-bslas/ |

| 15 | Computer Science + Economics | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-economics-bslas/ |

| 16 | Computer Science + Geography & Geographic Information Science | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-geography-geographic-information-science-bslas/ |

| 17 | Computer Science + Linguistics | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-linguistics-bslas/ |

| 18 | Computer Science + Philosophy | https://catalog.illinois.edu/undergraduate/eng_las/computer-science-philosophy-bslas/ |

| 19 | Earth, Society, & Environmental Sustainability | https://catalog.illinois.edu/undergraduate/las/earth-society-environmental-sustainability-bslas/ |

| 20 | Econometrics & Quantitative Economics | https://catalog.illinois.edu/undergraduate/las/econometrics-quantitative-economics-bslas/ |

| 21 | Environmental Sustainability | https://catalog.illinois.edu/undergraduate/las/environmental-sustainability-bslas/ |

| 22 | Geography & Geographic Information Science | https://catalog.illinois.edu/undergraduate/las/geography-geographic-information-science-bslas/ |

| 23 | Geology | https://catalog.illinois.edu/undergraduate/las/geology-bslas/ |

| 24 | Geology | https://catalog.illinois.edu/undergraduate/las/geology-bs/ |

| 25 | Individual Plans of Study | https://catalog.illinois.edu/undergraduate/las/individual-plans-study/ |

| 26 | Integrative Biology | https://catalog.illinois.edu/undergraduate/las/integrative-biology-bslas/ |

| 27 | Integrative Biology Honors | https://catalog.illinois.edu/undergraduate/las/integrative-biology-bslas/honors/ |

| 28 | Mathematics | https://catalog.illinois.edu/undergraduate/las/mathematics-bslas/ |

| 29 | Mathematics & Computer Science | https://catalog.illinois.edu/undergraduate/eng_las/mathematics-computer-science-bslas/ |

| 30 | Molecular & Cellular Biology | https://catalog.illinois.edu/undergraduate/las/molecular-cellular-biology-bslas/ |

| 31 | Molecular and Cellular Biology + Data Science | https://catalog.illinois.edu/undergraduate/las/molecular-cellular-biology-data-science-bslas/ |

| 32 | Neuroscience | https://catalog.illinois.edu/undergraduate/las/neuroscience-bslas/ |

| 33 | Psychology | https://catalog.illinois.edu/undergraduate/las/psychology-bslas/ |

| 34 | Statistics | https://catalog.illinois.edu/undergraduate/las/statistics-bslas/ |

| 35 | Statistics & Computer Science | https://catalog.illinois.edu/undergraduate/eng_las/statistics-computer-science-bslas/ |



#### College of Media

##### BA

| # | 专业 | URL |
|---|------|-----|

| 1 | Media | https://catalog.illinois.edu/undergraduate/media/media-ba/ |

| 2 | Sports Media | https://catalog.illinois.edu/undergraduate/media/sports-media-ba/ |



##### BS

| # | 专业 | URL |
|---|------|-----|

| 1 | Advertising | https://catalog.illinois.edu/undergraduate/media/advertising-bs/ |

| 2 | Computer Science + Advertising | https://catalog.illinois.edu/undergraduate/eng_media/computer-science-advertising-bs/ |

| 3 | Journalism | https://catalog.illinois.edu/undergraduate/media/journalism-bs/ |

| 4 | Media & Cinema Studies | https://catalog.illinois.edu/undergraduate/media/media-cinema-studies-bs/ |



#### School of Social Work

##### BSW

| # | 专业 | URL |
|---|------|-----|

| 1 | Social Work | https://catalog.illinois.edu/undergraduate/socw/social-work-bsw/ |



### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|

| 1 | Art History | LAS, FAA | https://catalog.illinois.edu/undergraduate/las/art-history-balas/ |

| 2 | Art History | LAS, FAA | https://catalog.illinois.edu/undergraduate/faa/art-art-history-bfa/ |

| 3 | Chemical Engineering | ENGR, LAS | https://catalog.illinois.edu/undergraduate/las/chemical-engineering-bs/ |



### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|

| 1 | Adult Development | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/adult-development/ |

| 2 | Advertising | College of Media | https://catalog.illinois.edu/undergraduate/media/minors/advertising/ |

| 3 | African American Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/african-american-studies/ |

| 4 | African Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/african-studies/ |

| 5 | American Indian Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/american-indian-studies/ |

| 6 | Animal Sciences | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/animal-sciences/ |

| 7 | Anthropology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/anthropology/ |

| 8 | Arabic Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/arabic-studies/ |

| 9 | Architectural Studies | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/architectural-studies/ |

| 10 | Art & Design | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/art-design/ |

| 11 | Art Education | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/community-based-art-education/ |

| 12 | Art History | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/faa/minors/art-history/ |

| 13 | Asian American Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/asian-american-studies/ |

| 14 | Astronomy | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/astronomy/ |

| 15 | Atmospheric Sciences | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/atmospheric-sciences/ |

| 16 | Bioengineering | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/bioengineering/ |

| 17 | Biomolecular Engineering | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/biomolecular-engineering/ |

| 18 | Business | Gies College of Business | https://catalog.illinois.edu/undergraduate/bus/minors/business-non-business/ |

| 19 | Business Analytics | Gies College of Business | https://catalog.illinois.edu/undergraduate/bus/minors/business-analytics/ |

| 20 | Chemistry | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/chemistry/ |

| 21 | Child Health & Well-being | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/child-health-well-being/ |

| 22 | Cinema Studies | College of Media | https://catalog.illinois.edu/undergraduate/media/minors/cinema-studies-minor/ |

| 23 | Civic Leadership | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/political-civic-leadership/ |

| 24 | Classical Civilizations | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/classical-civilizations/ |

| 25 | Classical Languages | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/classical-languages/ |

| 26 | Communication | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/communication/ |

| 27 | Community Based Art Education | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/community-based-art-education/ |

| 28 | Computational Science & Engineering | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/computational-science-engineering/ |

| 29 | Computer Science | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/computer-science/ |

| 30 | Creative Writing | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/creative-writing/ |

| 31 | Criminology, Law, & Society | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/criminology-law-society/ |

| 32 | Critical Film Production | College of Media | https://catalog.illinois.edu/undergraduate/media/minors/critical-film-production/ |

| 33 | Crop & Soil Management | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/crop-soil-management/ |

| 34 | Dance | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/dance/ |

| 35 | Data Science | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/data-science/index.html |

| 36 | Disability Studies | College of Applied Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/minors/disability-studies/ |

| 37 | East Asian Languages & Cultures | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/east-asian-languages-culture/ |

| 38 | Ecology & Conservation Biology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/ecology-conservation-biology/ |

| 39 | Economics | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/economics/ |

| 40 | Electrical & Computer Engineering | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/electrical-computer-engineering/ |

| 41 | Engineering Technology & Management for Agricultural Systems | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/engineering-technology-management-agricultural-systems/ |

| 42 | English | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/english/ |

| 43 | English as a Second Language | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/english-second-language/ |

| 44 | English as a Second Language | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/teacher-education-minor-english-second-language/ |

| 45 | Entrepreneurship | Gies College of Business | https://catalog.illinois.edu/undergraduate/bus/minors/entrepreneurship/ |

| 46 | Environmental Economics & Law | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/environmental-economics-law/ |

| 47 | Food & Agribusiness Management | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/food-agribusiness-management/ |

| 48 | Food & Environmental Systems | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/food-environmental-systems/ |

| 49 | Food Science | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/food-science/ |

| 50 | French | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/french/ |

| 51 | Game Studies & Design | School of Information Sciences | https://catalog.illinois.edu/undergraduate/ischool/minors/game-studies-design/ |

| 52 | Gender & Women's Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/gender-womens-studies/ |

| 53 | Geography & Geographic Information Science | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/geography-geographic-information-science/ |

| 54 | Geology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/geology/ |

| 55 | German | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/german/ |

| 56 | German Business & Commercial Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/german-business-commercial-studies/ |

| 57 | Global Labor Studies | School of Labor and Employment Relations | https://catalog.illinois.edu/undergraduate/ler/minors/global-labor-studies/ |

| 58 | Global Markets & Society | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/global-markets-society/ |

| 59 | Global Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/global-studies/ |

| 60 | Health Administration | College of Applied Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/minors/health-administration/ |

| 61 | Health Technology | College of Applied Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/minors/interdisciplinary-health-technology/ |

| 62 | Hindi Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/hindi-studies/ |

| 63 | Hip Hop Culture and the Arts | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/hip-hop-culture-arts/ |

| 64 | History | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/history/ |

| 65 | Horticulture | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/horticulture/ |

| 66 | Industrial and Agricultural Safety & Health | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/industrial-agricultural-safety-health/ |

| 67 | Informatics | School of Information Sciences | https://catalog.illinois.edu/undergraduate/informatics-programs/minors/informatics/ |

| 68 | Integrative Biology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/integrative-biology/ |

| 69 | International Business | Gies College of Business | https://catalog.illinois.edu/undergraduate/bus/minors/international-business/ |

| 70 | International Development Economics | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/international-development-economics/ |

| 71 | International Minor in ACES | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/international-agricultural-consumer-environmental-sciences/ |

| 72 | International Minor in Engineering | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/international-engineering/ |

| 73 | Islamic World, Study of the | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/islamic-world/ |

| 74 | Italian | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/italian/ |

| 75 | Japanese Arts and Aesthetics | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/japanese-arts-aesthetics/ |

| 76 | Jewish Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/jewish-culture/ |

| 77 | Journalism | College of Media | https://catalog.illinois.edu/undergraduate/media/minors/journalism/ |

| 78 | LGBT/Queer Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/lgbt-queer-studies/ |

| 79 | Landscape Studies | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/landscape/ |

| 80 | Latin American Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/latin-american-studies/ |

| 81 | Latina/Latino Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/latina-latino-studies/ |

| 82 | Leadership Studies | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/leadership-studies/ |

| 83 | Linguistics | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/linguistics/ |

| 84 | Materials Science & Engineering | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/materials-science-engineering/ |

| 85 | Mathematics | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/mathematics/ |

| 86 | Media | College of Media | https://catalog.illinois.edu/undergraduate/media/minors/media/ |

| 87 | Military Leadership | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/military-leadership/ |

| 88 | Minoritarian Aesthetics | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/minoritarian-aesthetics/ |

| 89 | Molecular & Cellular Biology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/molecular-cellular-biology/ |

| 90 | Music | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/music/ |

| 91 | Musical Theatre | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/musical-theatre-performing-artists/ |

| 92 | Natural Resource Conservation | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/natural-resource-conservation/ |

| 93 | Nutrition | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/nutrition/ |

| 94 | Philosophy | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/philosophy/ |

| 95 | Physics | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/physics/ |

| 96 | Political Science | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/political-science/ |

| 97 | Portuguese | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/portuguese/ |

| 98 | Psychology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/psychology/ |

| 99 | Public Health | College of Applied Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/minors/public-health/ |

| 100 | Public Relations | College of Media | https://catalog.illinois.edu/undergraduate/media/minors/public-relations/ |

| 101 | Quantum Information Science | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/quantum-information-science/ |

| 102 | Recreation, Sport & Tourism | College of Applied Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/minors/recreation-sport-tourism/ |

| 103 | Religion | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/religion/ |

| 104 | Russian & East European Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/russian-east-european-eurasian-studies/ |

| 105 | Russian Language & Literature | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/russian-language-literature/ |

| 106 | Scandinavian Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/scandinavian-studies/ |

| 107 | Secondary School Teaching | College of Education | https://catalog.illinois.edu/undergraduate/education/minors/teacher-education-secondary-school/ |

| 108 | Semiconductor Engineering | Grainger College of Engineering | https://catalog.illinois.edu/undergraduate/engineering/minors/semiconductor-engineering/ |

| 109 | Slavic Language, Literature & Culture | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/slavic-literature-language-culture/ |

| 110 | Social Work | School of Social Work | https://catalog.illinois.edu/undergraduate/minors/socw/ |

| 111 | Sociology | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/sociology/ |

| 112 | South Asian Studies | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/south-asian-studies-interdisciplinary/ |

| 113 | Spanish | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/spanish/ |

| 114 | Spatial & Quantitative Methods in Natural Resources & Environmental Sciences | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/spatial-quantitative-methods-natural-resources-environmental-sciences/ |

| 115 | Speech & Hearing Science | College of Applied Health Sciences | https://catalog.illinois.edu/undergraduate/ahs/minors/speech-hearing-science/ |

| 116 | Statistics | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/statistics/ |

| 117 | Sub-Saharan African Languages | College of Liberal Arts & Sciences | https://catalog.illinois.edu/undergraduate/las/minors/sub-saharan-african-languages/ |

| 118 | Sustainability, Energy, and Environment | PROVOST | https://catalog.illinois.edu/undergraduate/provost/minors/sustainability-energy-environment/ |

| 119 | Technology & Management | Gies College of Business | https://catalog.illinois.edu/undergraduate/eng_bus/minors/technology-management/ |

| 120 | Theatre | College of Fine & Applied Arts | https://catalog.illinois.edu/undergraduate/faa/minors/theatre/ |

| 121 | Wildlife & Fisheries Conservation | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/undergraduate/aces/minors/wildlife-fisheries/ |



### 1.5 General/Institute-wide requirements

UIUC requires all undergraduate students to complete general education requirements through the campus General Education program: Composition (2 courses), Advanced Composition (1), Humanities & the Arts (6 hours), Natural Sciences & Technology (6 hours), Social & Behavioral Sciences (6 hours), Quantitative Reasoning (1 course), Cultural Studies (3 hours), Language other than English (completion of level 3 or equivalent).

> Source: catalog.illinois.edu/general-information/

---

## Section 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 学位级别

#### College of Agricultural, Consumer & Environmental Sciences

##### MAAE

| # | 项目 | URL |
|---|------|-----|

| 1 | Agricultural & Applied Economics | https://catalog.illinois.edu/graduate/aces/agricultural-applied-economics-maae/ |



##### MANSC

| # | 项目 | URL |
|---|------|-----|

| 1 | Animal Sciences | https://catalog.illinois.edu/graduate/aces/animal-sciences-mansc/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Agricultural & Applied Economics | https://catalog.illinois.edu/graduate/aces/agricultural-applied-economics-ms/ |

| 2 | Agricultural Leadership, Education, & Communications | https://catalog.illinois.edu/graduate/aces/agricultural-leadership-education-communications-ms/ |

| 3 | Animal Sciences | https://catalog.illinois.edu/graduate/aces/animal-sciences-ms/ |

| 4 | Child Health | https://catalog.illinois.edu/graduate/aces/child-health-ms/ |

| 5 | Crop Sciences | https://catalog.illinois.edu/graduate/aces/crop-sciences-ms/ |

| 6 | Engineering Technology & Management for Agricultural Systems | https://catalog.illinois.edu/graduate/aces/engineering-technology-management-agricultural-systems-ms/ |

| 7 | Food Science & Human Nutrition | https://catalog.illinois.edu/graduate/aces/food-science-human-nutrition-ms/ |

| 8 | Human Development & Family Studies | https://catalog.illinois.edu/graduate/aces/human-development-family-studies-ms/ |

| 9 | Natural Resources & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/natural-resources-environmental-sciences-ms/ |

| 10 | Nutritional Sciences | https://catalog.illinois.edu/graduate/aces/nutritional-science-ms/ |



##### PSM

| # | 项目 | URL |
|---|------|-----|

| 1 | Bioprocessing & Bioenergy | https://catalog.illinois.edu/graduate/aces/bioprocessing-bioenergy-ms-professional-science-masters/ |

| 2 | Engineering Technology & Management for Agricultural Systems | https://catalog.illinois.edu/graduate/aces/engineering-technology-management-agricultural-systems-ms-professional-science-masters/ |

| 3 | Food Science & Human Nutrition | https://catalog.illinois.edu/graduate/aces/food-science-human-nutrition-ms/professional-science-masters/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Agricultural & Applied Economics | https://catalog.illinois.edu/graduate/aces/agricultural-applied-economics-phd/ |

| 2 | Animal Sciences | https://catalog.illinois.edu/graduate/aces/animal-sciences-phd/ |

| 3 | Crop Sciences | https://catalog.illinois.edu/graduate/aces/crop-sciences-phd/ |

| 4 | Engineering Technology & Management for Agricultural Systems | https://catalog.illinois.edu/graduate/aces/engineering-technology-management-agricultural-systems/ |

| 5 | Food Science & Human Nutrition | https://catalog.illinois.edu/graduate/aces/food-science-human-nutrition-phd/ |

| 6 | Human Development & Family Studies | https://catalog.illinois.edu/graduate/aces/human-development-family-studies-phd/ |

| 7 | Natural Resources & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/natural-resources-environmental-sciences-phd/ |

| 8 | Nutritional Sciences | https://catalog.illinois.edu/graduate/aces/nutritional-science-phd/ |



#### College of Applied Health Sciences

##### AuD

| # | 项目 | URL |
|---|------|-----|

| 1 | Speech & Hearing Science | https://catalog.illinois.edu/graduate/ahs/audiology-aud/ |



##### MA

| # | 项目 | URL |
|---|------|-----|

| 1 | Speech & Hearing Science | https://catalog.illinois.edu/graduate/ahs/speech-hearing-science-ma/ |



##### MHA

| # | 项目 | URL |
|---|------|-----|

| 1 | Health Administration | https://catalog.illinois.edu/graduate/ahs/health-administration-mha/ |



##### MPH

| # | 项目 | URL |
|---|------|-----|

| 1 | Epidemiology | https://catalog.illinois.edu/graduate/ahs/epidemiology-mph/ |

| 2 | Public Health | https://catalog.illinois.edu/graduate/ahs/public-health-mph/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Community Health | https://catalog.illinois.edu/graduate/ahs/community-health-ms/ |

| 2 | Health Technology | https://catalog.illinois.edu/graduate/ahs/health-technology-ms/ |

| 3 | Kinesiology | https://catalog.illinois.edu/graduate/ahs/kinesiology-ms/ |

| 4 | Recreation, Sport & Tourism | https://catalog.illinois.edu/graduate/ahs/recreation-sport-tourism-ms/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Community Health | https://catalog.illinois.edu/graduate/ahs/community-health-phd/ |

| 2 | Kinesiology | https://catalog.illinois.edu/graduate/ahs/kinesiology-phd/ |

| 3 | Recreation, Sport & Tourism | https://catalog.illinois.edu/graduate/ahs/recreation-sport-tourism-phd/ |

| 4 | Speech & Hearing Science | https://catalog.illinois.edu/graduate/ahs/speech-hearing-science-phd/ |



#### Gies College of Business

##### MAS

| # | 项目 | URL |
|---|------|-----|

| 1 | Accountancy | https://catalog.illinois.edu/graduate/bus/accountancy-mas/ |



##### MBA

| # | 项目 | URL |
|---|------|-----|

| 1 | Business Administration | https://catalog.illinois.edu/graduate/bus/business-administration-online-mba/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Business Analytics | https://catalog.illinois.edu/graduate/bus/business-analytics-ms/ |

| 2 | Finance | https://catalog.illinois.edu/graduate/bus/finance-ms/ |

| 3 | Financial Engineering | https://catalog.illinois.edu/graduate/bus_engineering/financial-engineering-ms/ |

| 4 | Management | https://catalog.illinois.edu/graduate/bus/management-ms/ |

| 5 | Technology Management | https://catalog.illinois.edu/graduate/bus/technology-management-ms/ |



##### MSA

| # | 项目 | URL |
|---|------|-----|

| 1 | Accountancy | https://catalog.illinois.edu/graduate/bus/accountancy-ms/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Accountancy | https://catalog.illinois.edu/graduate/bus/accountancy-phd/ |

| 2 | Business Administration | https://catalog.illinois.edu/graduate/bus/business-administration-phd/ |

| 3 | Finance | https://catalog.illinois.edu/graduate/bus/finance-phd/ |



#### College of Education

##### CAS

| # | 项目 | URL |
|---|------|-----|

| 1 | Curriculum & Instruction | https://catalog.illinois.edu/graduate/education/curriculum-instruction-cas/ |

| 2 | Education Policy, Organization & Leadership | https://catalog.illinois.edu/graduate/education/education-policy-organization-leadership-cas/ |



##### EdD

| # | 项目 | URL |
|---|------|-----|

| 1 | Curriculum & Instruction | https://catalog.illinois.edu/graduate/education/curriculum-instruction-edd/ |

| 2 | Education Policy, Organization & Leadership | https://catalog.illinois.edu/graduate/education/education-policy-organization-leadership-edd/ |



##### EdM

| # | 项目 | URL |
|---|------|-----|

| 1 | Curriculum & Instruction | https://catalog.illinois.edu/graduate/education/curriculum-instruction-edm/ |

| 2 | Early Childhood Education | https://catalog.illinois.edu/graduate/education/early-childhood-education-edm/ |

| 3 | Education Policy, Organization & Leadership | https://catalog.illinois.edu/graduate/education/education-policy-organization-leadership-edm/ |

| 4 | Educational Psychology | https://catalog.illinois.edu/graduate/education/educational-psychology-edm/ |

| 5 | Elementary Education | https://catalog.illinois.edu/graduate/education/elementary-education-edm/ |

| 6 | Secondary Education | https://catalog.illinois.edu/graduate/education/secondary-education-edm/ |

| 7 | Special Education | https://catalog.illinois.edu/graduate/education/special-education-edm/ |



##### MA

| # | 项目 | URL |
|---|------|-----|

| 1 | Curriculum & Instruction | https://catalog.illinois.edu/graduate/education/curriculum-instruction-ma/ |

| 2 | Education Policy, Organization & Leadership | https://catalog.illinois.edu/graduate/education/education-policy-organization-leadership-ma/ |

| 3 | Educational Psychology | https://catalog.illinois.edu/graduate/education/educational-psychology-ma/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Curriculum & Instruction | https://catalog.illinois.edu/graduate/education/curriculum-instruction-ms/ |

| 2 | Educational Psychology | https://catalog.illinois.edu/graduate/education/educational-psychology-ms/ |

| 3 | Mental Health Counseling | https://catalog.illinois.edu/graduate/education/mental-health-counseling-ms/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Curriculum & Instruction | https://catalog.illinois.edu/graduate/education/curriculum-instruction-phd/ |

| 2 | Education Policy, Organization & Leadership | https://catalog.illinois.edu/graduate/education/education-policy-organization-leadership-phd/ |

| 3 | Educational Psychology | https://catalog.illinois.edu/graduate/education/educational-psychology-phd/ |

| 4 | Special Education | https://catalog.illinois.edu/graduate/education/special-education-phd/ |



#### Grainger College of Engineering

##### MCS

| # | 项目 | URL |
|---|------|-----|

| 1 | Computer Science | https://catalog.illinois.edu/graduate/engineering/computer-science-mcs/ |



##### MENG

| # | 项目 | URL |
|---|------|-----|

| 1 | Bioengineering | https://catalog.illinois.edu/graduate/engineering/bioengineering-meng/ |

| 2 | Chemical Engineering Leadership | https://catalog.illinois.edu/graduate/engineering/chemical-engineering-leadership-meng/ |

| 3 | Electrical & Computer Engineering | https://catalog.illinois.edu/graduate/engineering/electrical-computer-engineering-meng/ |

| 4 | Engineering | https://catalog.illinois.edu/graduate/engineering/engineering-meng/ |

| 5 | Materials Engineering | https://catalog.illinois.edu/graduate/engineering/materials-engineering-meng/ |

| 6 | Mechanical Engineering | https://catalog.illinois.edu/graduate/engineering/mechanical-engineering-meng/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Aerospace Engineering | https://catalog.illinois.edu/graduate/engineering/aerospace-engineering-ms/ |

| 2 | Agricultural & Biological Engineering | https://catalog.illinois.edu/graduate/engineering/agricultural-biological-engineering-ms/ |

| 3 | Bioengineering | https://catalog.illinois.edu/graduate/engineering/bioengineering-ms/ |

| 4 | Biomedical Image Computing | https://catalog.illinois.edu/graduate/engineering/biomedical-image-computing-ms/ |

| 5 | Chemical Engineering | https://catalog.illinois.edu/graduate/las/chemical-engineering-ms/ |

| 6 | Civil Engineering | https://catalog.illinois.edu/graduate/engineering/civil-engineering-ms/ |

| 7 | Computer Science | https://catalog.illinois.edu/graduate/engineering/computer-science-ms/ |

| 8 | Electrical & Computer Engineering | https://catalog.illinois.edu/graduate/engineering/electrical-computer-engineering-ms/ |

| 9 | Environmental Engineering in Civil Engineering | https://catalog.illinois.edu/graduate/engineering/environmental-engineering-civil-engineering-ms/ |

| 10 | Industrial Engineering | https://catalog.illinois.edu/graduate/engineering/industrial-engineering-ms/ |

| 11 | Materials Science & Engineering | https://catalog.illinois.edu/graduate/engineering/materials-science-engineering-ms/ |

| 12 | Mechanical Engineering | https://catalog.illinois.edu/graduate/engineering/mechanical-engineering-ms/ |

| 13 | Nuclear, Plasma & Radiological Engineering | https://catalog.illinois.edu/graduate/engineering/nuclear-plasma-radiological-engineering-ms/ |

| 14 | Physics | https://catalog.illinois.edu/graduate/engineering/physics-ms/ |

| 15 | Physics, Teaching of | https://catalog.illinois.edu/graduate/engineering/teaching-physics-ms/ |

| 16 | Systems & Entrepreneurial Engineering | https://catalog.illinois.edu/graduate/engineering/systems-entrepreneurial-engineering-ms/ |

| 17 | Theoretical & Applied Mechanics | https://catalog.illinois.edu/graduate/engineering/theoretical-applied-mechanics-ms/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Aerospace Engineering | https://catalog.illinois.edu/graduate/engineering/aerospace-engineering-phd/ |

| 2 | Agricultural & Biological Engineering | https://catalog.illinois.edu/graduate/engineering/agricultural-biological-engineering-phd/ |

| 3 | Bioengineering | https://catalog.illinois.edu/graduate/engineering/bioengineering-phd/ |

| 4 | Chemical Engineering | https://catalog.illinois.edu/graduate/las/chemical-engineering-phd/ |

| 5 | Civil Engineering | https://catalog.illinois.edu/graduate/engineering/civil-engineering-phd/ |

| 6 | Computer Science | https://catalog.illinois.edu/graduate/engineering/computer-science-phd/ |

| 7 | Electrical & Computer Engineering | https://catalog.illinois.edu/graduate/engineering/electrical-computer-engineering-phd/ |

| 8 | Environmental Engineering in Civil Engineering | https://catalog.illinois.edu/graduate/engineering/environmental-engineering-civil-engineering-phd/ |

| 9 | Industrial Engineering | https://catalog.illinois.edu/graduate/engineering/industrial-engineering-phd/ |

| 10 | Materials Science & Engineering | https://catalog.illinois.edu/graduate/engineering/materials-science-engineering-phd/ |

| 11 | Mechanical Engineering | https://catalog.illinois.edu/graduate/engineering/mechanical-engineering-phd/ |

| 12 | Nuclear, Plasma & Radiological Engineering | https://catalog.illinois.edu/graduate/engineering/nuclear-plasma-radiological-engineering-phd/ |

| 13 | Physics | https://catalog.illinois.edu/graduate/engineering/physics-phd/ |

| 14 | Systems & Entrepreneurial Engineering | https://catalog.illinois.edu/graduate/engineering/systems-entrepreneurial-engineering-phd/ |

| 15 | Theoretical & Applied Mechanics | https://catalog.illinois.edu/graduate/engineering/theoretical-applied-mechanics-phd/ |



#### College of Fine & Applied Arts

##### AD

| # | 项目 | URL |
|---|------|-----|

| 1 | Music | https://catalog.illinois.edu/graduate/faa/artist-diploma-music/ |



##### AMusD

| # | 项目 | URL |
|---|------|-----|

| 1 | Music | https://catalog.illinois.edu/graduate/faa/music-dma/ |



##### EdM

| # | 项目 | URL |
|---|------|-----|

| 1 | Art Education | https://catalog.illinois.edu/graduate/faa/art-education-edm/ |



##### MA

| # | 项目 | URL |
|---|------|-----|

| 1 | Art Education | https://catalog.illinois.edu/graduate/faa/art-education-ma/ |

| 2 | Theatre | https://catalog.illinois.edu/graduate/faa/theatre-ma/ |



##### MARCH

| # | 项目 | URL |
|---|------|-----|

| 1 | Architecture | https://catalog.illinois.edu/graduate/faa/architecture-march/ |



##### MDes

| # | 项目 | URL |
|---|------|-----|

| 1 | Industrial Design | https://catalog.illinois.edu/graduate/faa/industrial-design-mdes/ |



##### MFA

| # | 项目 | URL |
|---|------|-----|

| 1 | Art & Design | https://catalog.illinois.edu/graduate/faa/art-design-mfa/ |

| 2 | Dance | https://catalog.illinois.edu/graduate/faa/dance-mfa/ |

| 3 | Theatre | https://catalog.illinois.edu/graduate/faa/theatre-mfa/ |



##### MLA

| # | 项目 | URL |
|---|------|-----|

| 1 | Landscape Architecture | https://catalog.illinois.edu/graduate/faa/landscape-architecture-mla/ |



##### MME

| # | 项目 | URL |
|---|------|-----|

| 1 | Music Education | https://catalog.illinois.edu/graduate/faa/music-education-mme/ |



##### MMus

| # | 项目 | URL |
|---|------|-----|

| 1 | Music | https://catalog.illinois.edu/graduate/faa/music-mmus/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Architectural Studies | https://catalog.illinois.edu/graduate/faa/architectural-studies-ms/ |



##### MSUD

| # | 项目 | URL |
|---|------|-----|

| 1 | Sustainable Urban Design | https://catalog.illinois.edu/graduate/faa/sustainable-urban-design-msud/ |



##### MUP

| # | 项目 | URL |
|---|------|-----|

| 1 | Urban Planning | https://catalog.illinois.edu/graduate/faa/urban-planning-mup/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Architecture | https://catalog.illinois.edu/graduate/faa/architecture-phd/ |

| 2 | Art Education | https://catalog.illinois.edu/graduate/faa/art-education-phd/ |

| 3 | Landscape Architecture | https://catalog.illinois.edu/graduate/faa/landscape-architecture-phd/ |

| 4 | Music Education | https://catalog.illinois.edu/graduate/faa/music-education-phd/ |

| 5 | Musicology | https://catalog.illinois.edu/graduate/faa/musicology-phd/ |

| 6 | Regional Planning | https://catalog.illinois.edu/graduate/faa/regional-planning-phd/ |

| 7 | Theatre | https://catalog.illinois.edu/graduate/faa/theatre-phd/ |



#### School of Information Sciences

##### CAS

| # | 项目 | URL |
|---|------|-----|

| 1 | Information Sciences | https://catalog.illinois.edu/graduate/is/library-information-science-cas/ |

| 2 | Library & Information Science | https://catalog.illinois.edu/graduate/is/library-information-science-cas/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Bioinformatics | https://catalog.illinois.edu/graduate/provost/bioinformatics-ms/ |

| 2 | Game Development | https://catalog.illinois.edu/graduate/is/game-development-ms/ |

| 3 | Information Management | https://catalog.illinois.edu/graduate/is/information-management-ms/ |

| 4 | Information Sciences | https://catalog.illinois.edu/graduate/is/library-information-science-ms/ |

| 5 | Library & Information Science | https://catalog.illinois.edu/graduate/is/library-information-science-ms/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Informatics | https://catalog.illinois.edu/graduate/informatics-programs/informatics-phd/ |

| 2 | Information Sciences | https://catalog.illinois.edu/graduate/is/information-science-phd/ |



#### College of Liberal Arts & Sciences

##### MA

| # | 项目 | URL |
|---|------|-----|

| 1 | African Studies | https://catalog.illinois.edu/graduate/las/african-studies-ma/ |

| 2 | Anthropology | https://catalog.illinois.edu/graduate/las/anthropology-ma/ |

| 3 | Art History | https://catalog.illinois.edu/graduate/faa/art-history-ma/ |

| 4 | Classics | https://catalog.illinois.edu/graduate/las/classics-ma/ |

| 5 | Communication | https://catalog.illinois.edu/graduate/las/communication-ma/ |

| 6 | Comparative Literature | https://catalog.illinois.edu/graduate/las/comparative-literature-ma/ |

| 7 | East Asian Languages & Cultures | https://catalog.illinois.edu/graduate/las/east-asian-languages-cultures-ma/ |

| 8 | English | https://catalog.illinois.edu/graduate/las/english-ma/ |

| 9 | English as a Second Language | https://catalog.illinois.edu/graduate/las/teaching-english-second-language-ma/ |

| 10 | European Union Studies | https://catalog.illinois.edu/graduate/las/european-union-studies-ma/ |

| 11 | French | https://catalog.illinois.edu/graduate/las/french-ma/ |

| 12 | Geography | https://catalog.illinois.edu/graduate/las/geography-ma/ |

| 13 | German | https://catalog.illinois.edu/graduate/las/german-ma/ |

| 14 | History | https://catalog.illinois.edu/graduate/las/history-ma/ |

| 15 | Italian | https://catalog.illinois.edu/graduate/las/italian-ma/ |

| 16 | Latin American Studies | https://catalog.illinois.edu/graduate/las/latin-american-studies-ma/ |

| 17 | Latin, Teaching of | https://catalog.illinois.edu/graduate/las/teaching-latin-ma/ |

| 18 | Linguistics | https://catalog.illinois.edu/graduate/las/linguistics-ma/ |

| 19 | Philosophy | https://catalog.illinois.edu/graduate/las/philosophy-ma/ |

| 20 | Political Science | https://catalog.illinois.edu/graduate/las/political-science-ma/ |

| 21 | Portuguese | https://catalog.illinois.edu/graduate/las/portuguese-ma/ |

| 22 | Religion | https://catalog.illinois.edu/graduate/las/religion-ma/ |

| 23 | Russian, East European & Eurasian Studies | https://catalog.illinois.edu/graduate/las/russian-east-european-eurasian-studies-ma/ |

| 24 | Slavic Languages & Literatures | https://catalog.illinois.edu/graduate/las/slavic-languages-literatures-ma/ |

| 25 | Sociology | https://catalog.illinois.edu/graduate/las/sociology-ma/ |

| 26 | South Asian & Middle Eastern Studies | https://catalog.illinois.edu/graduate/las/south-asian-middle-eastern-studies-ma/ |

| 27 | Spanish | https://catalog.illinois.edu/graduate/las/spanish-ma/ |

| 28 | Translation & Interpreting | https://catalog.illinois.edu/graduate/las/translation-interpreting-ma/ |



##### MATESL

| # | 项目 | URL |
|---|------|-----|

| 1 | Linguistics | https://catalog.illinois.edu/graduate/las/teaching-english-second-language-ma/ |



##### MFA

| # | 项目 | URL |
|---|------|-----|

| 1 | Creative Writing | https://catalog.illinois.edu/graduate/las/creative-writing-mfa/ |



##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Actuarial Science | https://catalog.illinois.edu/graduate/las/actuarial-science-ms/ |

| 2 | Applied Mathematics | https://catalog.illinois.edu/graduate/las/applied-mathematics-ms/ |

| 3 | Astronomy | https://catalog.illinois.edu/graduate/las/astronomy-ms/ |

| 4 | Atmospheric Sciences | https://catalog.illinois.edu/graduate/las/atmospheric-sciences-ms/ |

| 5 | Biochemistry | https://catalog.illinois.edu/graduate/las/biochemistry-ms/ |

| 6 | Biological Sciences, Teaching of | https://catalog.illinois.edu/graduate/las/teaching-biological-science-ms/ |

| 7 | Biology | https://catalog.illinois.edu/graduate/las/biology-ms/ |

| 8 | Biophysics & Quantitative Biology | https://catalog.illinois.edu/graduate/las/biophysics-quantitative-biology-ms/ |

| 9 | Cell & Developmental Biology | https://catalog.illinois.edu/graduate/las/cell-developmental-biology-ms/ |

| 10 | Chemistry | https://catalog.illinois.edu/graduate/las/chemistry-ms/ |

| 11 | Chemistry Teaching | https://catalog.illinois.edu/graduate/las/teaching-chemistry-ms/ |

| 12 | CyberGIS and Geospatial Data Science, MS | https://catalog.illinois.edu/graduate/las/cyberGIS-geospatial-data-science-ms/ |

| 13 | Ecology & Conservation Biology | https://catalog.illinois.edu/graduate/las/ecology-evolution-conservation-biology-ms/ |

| 14 | Ecology, Evolution & Conservation Biology | https://catalog.illinois.edu/graduate/las/ecology-evolution-conservation-biology-ms/ |

| 15 | Economics | https://catalog.illinois.edu/graduate/las/economics-ms/ |

| 16 | Entomology | https://catalog.illinois.edu/graduate/las/entomology-ms/ |

| 17 | Environmental Geology | https://catalog.illinois.edu/graduate/las/environmental-geology-ms/ |

| 18 | Evolution, Ecology, and Behavior | https://catalog.illinois.edu/graduate/las/evolution-ecology-behavior-ms/ |

| 19 | Geography | https://catalog.illinois.edu/graduate/las/geography-ms/ |

| 20 | Geology | https://catalog.illinois.edu/graduate/las/geology-ms/ |

| 21 | Global Studies | https://catalog.illinois.edu/graduate/las/global-studies-ms/ |

| 22 | Health Communication | https://catalog.illinois.edu/graduate/las/health-communication-ms/ |

| 23 | Integrative Biology | https://catalog.illinois.edu/graduate/las/integrative-biology-ms/ |

| 24 | Mathematics | https://catalog.illinois.edu/graduate/las/mathematics-ms/ |

| 25 | Mathematics Teaching | https://catalog.illinois.edu/graduate/las/teaching-mathematics-ms/ |

| 26 | Microbiology | https://catalog.illinois.edu/graduate/las/microbiology-ms/ |

| 27 | Molecular & Cellular Biology | https://catalog.illinois.edu/graduate/las/molecular-cellular-biology-ms/ |

| 28 | Molecular & Integrative Physiology | https://catalog.illinois.edu/graduate/las/molecular-integrative-physiology-ms/ |

| 29 | Plant Biology | https://catalog.illinois.edu/graduate/las/plant-biology-ms/ |

| 30 | Policy Economics | https://catalog.illinois.edu/graduate/las/policy-economics-ms/ |

| 31 | Predictive Analytics and Risk Management | https://catalog.illinois.edu/graduate/las/predictive-analytics-risk-management-ms/ |

| 32 | Psychological Science | https://catalog.illinois.edu/graduate/las/psychological-science-ms/ |

| 33 | Psychology | https://catalog.illinois.edu/graduate/las/psychological-science-ms/ |

| 34 | Psychology | https://catalog.illinois.edu/graduate/las/psychology-ms/ |

| 35 | Statistics | https://catalog.illinois.edu/graduate/las/statistics-ms/ |

| 36 | Weather And Climate Risk & Analysis | https://catalog.illinois.edu/graduate/las/weather-climate-risk-analytics-ms/ |



##### PSM

| # | 项目 | URL |
|---|------|-----|

| 1 | Geography | https://catalog.illinois.edu/graduate/las/geography-ms/geographic-information-science-professional-science-masters/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Anthropology | https://catalog.illinois.edu/graduate/las/anthropology-phd/ |

| 2 | Art History | https://catalog.illinois.edu/graduate/faa/art-history-phd/ |

| 3 | Astronomy | https://catalog.illinois.edu/graduate/las/astronomy-phd/ |

| 4 | Atmospheric Sciences | https://catalog.illinois.edu/graduate/las/atmospheric-sciences-phd/ |

| 5 | Biochemistry | https://catalog.illinois.edu/graduate/las/biochemistry-phd/ |

| 6 | Biology | https://catalog.illinois.edu/graduate/las/biology-phd/ |

| 7 | Biophysics & Quantitative Biology | https://catalog.illinois.edu/graduate/las/biophysics-quantitative-biology-phd/ |

| 8 | Cell & Developmental Biology | https://catalog.illinois.edu/graduate/las/cell-developmental-biology-phd/ |

| 9 | Chemistry | https://catalog.illinois.edu/graduate/las/chemistry-phd/ |

| 10 | Classical Philology | https://catalog.illinois.edu/graduate/las/classical-philology-phd/ |

| 11 | Communication | https://catalog.illinois.edu/graduate/las/communication-phd/ |

| 12 | Comparative Literature | https://catalog.illinois.edu/graduate/las/comparative-literature-phd/ |

| 13 | East Asian Languages & Cultures | https://catalog.illinois.edu/graduate/las/east-asian-languages-cultures-phd/ |

| 14 | Ecology & Conservation Biology | https://catalog.illinois.edu/graduate/las/ecology-evolution-conservation-biology-ms/ |

| 15 | Ecology, Evolution & Conservation Biology | https://catalog.illinois.edu/graduate/las/ecology-evolution-conservation-biology-phd/ |

| 16 | Economics | https://catalog.illinois.edu/graduate/las/economics-phd/ |

| 17 | English | https://catalog.illinois.edu/graduate/las/english-phd/ |

| 18 | Entomology | https://catalog.illinois.edu/graduate/las/entomology-phd/ |

| 19 | Evolution, Ecology, and Behavior | https://catalog.illinois.edu/graduate/las/evolution-ecology-behavior-phd/ |

| 20 | French | https://catalog.illinois.edu/graduate/las/french-phd/ |

| 21 | Geography | https://catalog.illinois.edu/graduate/las/geography-phd/ |

| 22 | Geology | https://catalog.illinois.edu/graduate/las/geology-phd/ |

| 23 | German | https://catalog.illinois.edu/graduate/las/german-phd/ |

| 24 | History | https://catalog.illinois.edu/graduate/las/history-phd/ |

| 25 | Italian | https://catalog.illinois.edu/graduate/las/italian-phd/ |

| 26 | Linguistics | https://catalog.illinois.edu/graduate/las/linguistics-phd/ |

| 27 | Mathematics | https://catalog.illinois.edu/graduate/las/mathematics-phd/ |

| 28 | Microbiology | https://catalog.illinois.edu/graduate/las/microbiology-phd/ |

| 29 | Molecular & Integrative Physiology | https://catalog.illinois.edu/graduate/las/molecular-integrative-physiology-phd/ |

| 30 | Neuroscience | https://catalog.illinois.edu/graduate/las/neuroscience-phd/ |

| 31 | Philosophy | https://catalog.illinois.edu/graduate/las/philosophy-phd/ |

| 32 | Plant Biology | https://catalog.illinois.edu/graduate/las/plant-biology-phd/ |

| 33 | Political Science | https://catalog.illinois.edu/graduate/las/political-science-phd/ |

| 34 | Portuguese | https://catalog.illinois.edu/graduate/las/portuguese-phd/ |

| 35 | Psychology | https://catalog.illinois.edu/graduate/las/psychology-phd/ |

| 36 | Slavic Languages & Literatures | https://catalog.illinois.edu/graduate/las/slavic-languages-literatures-phd/ |

| 37 | Sociology | https://catalog.illinois.edu/graduate/las/sociology-phd/ |

| 38 | Spanish | https://catalog.illinois.edu/graduate/las/spanish-phd/ |

| 39 | Statistics | https://catalog.illinois.edu/graduate/las/statistics-phd/ |



#### College of Law

##### JSD

| # | 项目 | URL |
|---|------|-----|

| 1 | Law | https://catalog.illinois.edu/graduate/law/science-law-jsd/ |



##### LLM

| # | 项目 | URL |
|---|------|-----|

| 1 | Law | https://catalog.illinois.edu/graduate/law/master-laws-llm/ |



##### MSL

| # | 项目 | URL |
|---|------|-----|

| 1 | Law | https://catalog.illinois.edu/graduate/law/master-studies-msl/ |



#### School of Labor and Employment Relations

##### MHRIR

| # | 项目 | URL |
|---|------|-----|

| 1 | Human Resources & Industrial Relations | https://catalog.illinois.edu/graduate/ler/human-resources-industrial-relations-mhrir/ |

| 2 | Labor & Employment Relations | https://catalog.illinois.edu/graduate/ler/human-resources-industrial-relations-mhrir/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Human Resources & Industrial Relations | https://catalog.illinois.edu/graduate/ler/human-resources-industrial-relations-phd/ |

| 2 | Labor & Employment Relations | https://catalog.illinois.edu/graduate/ler/human-resources-industrial-relations-phd/ |



#### College of Media

##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Advertising | https://catalog.illinois.edu/graduate/media/advertising-ms/ |

| 2 | Journalism | https://catalog.illinois.edu/graduate/media/journalism-ms/ |

| 3 | Strategic Brand Communication | https://catalog.illinois.edu/graduate/media/strategic-brand-communication-ms/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Communications & Media | https://catalog.illinois.edu/graduate/media/communications-media-phd/ |



#### School of Social Work

##### CAS

| # | 项目 | URL |
|---|------|-----|

| 1 | Schools Specialization | https://catalog.illinois.edu/graduate/socw/schools-specialization-cas/ |



##### Joint

| # | 项目 | URL |
|---|------|-----|

| 1 | Social Work | https://catalog.illinois.edu/graduate/socw/joint-degree/social-work-msw-phd/ |



##### MSW

| # | 项目 | URL |
|---|------|-----|

| 1 | Leadership & Social Change | https://catalog.illinois.edu/graduate/socw/social-work-msw/leadership-social-change/ |

| 2 | Social Work | https://catalog.illinois.edu/graduate/socw/social-work-msw/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Social Work | https://catalog.illinois.edu/graduate/socw/social-work-phd/ |



#### College of Veterinary Medicine

##### MS

| # | 项目 | URL |
|---|------|-----|

| 1 | Comparative Biosciences | https://catalog.illinois.edu/graduate/veterinary/medical-science-comparative-biosciences-ms/ |

| 2 | Pathobiology | https://catalog.illinois.edu/graduate/veterinary/medical-science-pathobiology-ms/ |

| 3 | Veterinary Medical Science - Comparative Biosciences | https://catalog.illinois.edu/graduate/veterinary/medical-science-comparative-biosciences-ms/ |

| 4 | Veterinary Medical Science - Pathobiology | https://catalog.illinois.edu/graduate/veterinary/medical-science-pathobiology-ms/ |

| 5 | Veterinary Medical Sciences - Veterinary Clinical Medicine | https://catalog.illinois.edu/graduate/veterinary/clinical-medicine-ms/ |



##### MVS

| # | 项目 | URL |
|---|------|-----|

| 1 | Applied Veterinary Sciences | https://catalog.illinois.edu/graduate/veterinary/applied-veterinary-sciences-mvs |

| 2 | Livestock Systems Health | https://catalog.illinois.edu/graduate/veterinary/livestock-systems-health-mvs/ |



##### PhD

| # | 项目 | URL |
|---|------|-----|

| 1 | Comparative Biosciences | https://catalog.illinois.edu/graduate/veterinary/medical-science-comparative-biosciences-phd/ |

| 2 | Pathobiology | https://catalog.illinois.edu/graduate/veterinary/medical-science-pathobiology-phd/ |

| 3 | Veterinary Medical Science - Comparative Biosciences | https://catalog.illinois.edu/graduate/veterinary/medical-science-comparative-biosciences-phd/ |

| 4 | Veterinary Medical Science - Pathobiology | https://catalog.illinois.edu/graduate/veterinary/medical-science-pathobiology-phd/ |



### 2.1b Graduate Certificates

| # | Certificate | School | URL |
|---|-------------|--------|-----|

| 1 | Accountancy Data Analytics | Gies College of Business | https://catalog.illinois.edu/graduate/bus/accy/accounting-data-analytics-cert/ |

| 2 | Accounting Foundations | Gies College of Business | https://catalog.illinois.edu/graduate/bus/accy/accounting-foundations-cert/ |

| 3 | Advanced Design Thinking | College of Fine & Applied Arts | https://catalog.illinois.edu/graduate/faa/art-design/advanced-design-thinking-cert/ |

| 4 | Agribusiness and Sustainable Food Production Economics | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/ace/agribusiness-and-sustainable-food-production-economics-cert/ |

| 5 | Biostatistics in Public Health | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/biostatistics-in-public-health/ |

| 6 | CPA Pathways | Gies College of Business | https://catalog.illinois.edu/graduate/bus/accy/cpa-pathways-cert/ |

| 7 | Cancer Education Management in Underrepresented and Diverse Communities | College of Education | https://catalog.illinois.edu/graduate/education/epol/cancer-education-management-underrepresented-diverse-communities-cert/ |

| 8 | Compensation Best Practices | School of Labor and Employment Relations | https://catalog.illinois.edu/graduate/ler/compensation-best-practices-cert/ |

| 9 | Computing Fundamentals | Grainger College of Engineering | https://catalog.illinois.edu/graduate/engineering/computing-fundamentals-cert/ |

| 10 | Dairy Nutrition for Udder Success | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/animal-sciences/dairy-nutrition-for-udder-success-cert/ |

| 11 | Digital Marketing | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/digital-marketing-cert/ |

| 12 | Entrepreneurship & Strategic Innovation | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/entrepreneurship-strategic-innovation-cert/ |

| 13 | Epidemiology in Public Health | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/epidemiology-public-health-cert/ |

| 14 | Financial Management | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/financial-management-cert/ |

| 15 | Food Regulations, Nutrition Policy, and Personalized Nutrition | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/dns/food-regulations-nutrition-policy-personalized-nutrition-cert/ |

| 16 | Fundamentals of Human Resources | School of Labor and Employment Relations | https://catalog.illinois.edu/graduate/ler/fundamentals-human-resources-cert/ |

| 17 | Global Challenges in Business | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/global-challenges-business-cert/ |

| 18 | Health Finance | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/health-finance-cert/ |

| 19 | Health and Well-being for Designed Environments | College of Fine & Applied Arts | https://catalog.illinois.edu/graduate/faa/arch/health-well-being-designed-environments-cert/ |

| 20 | Healthcare Analytics | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/healthcare-analytics-cert/ |

| 21 | Healthcare Innovation, Design, and Entrepreneurship | Gies College of Business | https://catalog.illinois.edu/graduate/bus/mba/healthcare-innovation-design-entrepreneurship-cert/ |

| 22 | Healthcare Quality and Strategy | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/healthcare-quality-strategy-cert/ |

| 23 | Human Resources Data Analytics | School of Labor and Employment Relations | https://catalog.illinois.edu/graduate/ler/human-resources-data-analytics-cert/ |

| 24 | Inclusive by Design in Recreation, Sport, and Tourism | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/inclusive-design-recreation-sport-tourism-cert/ |

| 25 | Instructional System Design Management and Leadership | College of Education | https://catalog.illinois.edu/graduate/education/epol/instructional-system-design-management-leadership-cert/ |

| 26 | International Education Administration and Leadership | College of Education | https://catalog.illinois.edu/graduate/education/epol/international-education-administration-leadership-cert/ |

| 27 | Land, Agriculture and Alternative Investing | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/ace/land-agriculture-and-alternative-investing-cert/ |

| 28 | Learning Design & Leadership | College of Education | https://catalog.illinois.edu/graduate/education/epol/learning-design-leadership-cert/ |

| 29 | Managerial Economics & Business Analysis | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/managerial-economics-business-analysis-cert/ |

| 30 | Middle Grades Education | College of Education | https://catalog.illinois.edu/graduate/education/middle-grades-education-cert/ |

| 31 | Public Health | College of Applied Health Sciences | https://catalog.illinois.edu/graduate/ahs/public-health-cert/ |

| 32 | Strategic Leadership Management | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/strategic-leadership-management-cert/ |

| 33 | Sustainability Education and Climate Justice | College of Education | https://catalog.illinois.edu/graduate/education/epol/sustainability-education-climate-justice-cert/ |

| 34 | Taxation | Gies College of Business | https://catalog.illinois.edu/graduate/bus/accy/taxation-cert/ |

| 35 | Value Chain Management | Gies College of Business | https://catalog.illinois.edu/graduate/bus/badm/value-chain-management-cert/ |

| 36 | Wetland Science and Conservation | College of Agricultural, Consumer & Environmental Sciences | https://catalog.illinois.edu/graduate/aces/nres/wetland-science-conservation-cert/ |



### 2.2 Graduate admissions model

UIUC graduate admissions is **decentralized**. The Graduate College sets minimum requirements, but each program makes its own admission decisions. Key details:

- **Application portal**: grad.illinois.edu/admissions/apply-now
- **Application fee**: $70 (domestic), $90 (international)
- **GRE**: Per-program (some required, some optional, some not accepted)
- **English proficiency**: Required for all international applicants
- **Minimum GPA**: 3.0 on last 60 hours of undergraduate study (program may require higher)
- **CGS April-15 signatory**: Yes

> Source: grad.illinois.edu/admissions/graduate-admissions-minimum-requirements

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value |
|-----------|-------|

| Admissions site | admissions.illinois.edu |
| Application portal | myIllini (myillini.illinois.edu) |
| Application opens | September 1 |
| Early Action deadline | November 1 (items by November 7) |
| Regular Decision deadline | January 5 (items by January 11) |
| EA notification | January 30 |
| RD notification | March 6 |
| Honors & Scholarship notification | By April 1 |
| Accept deadline | May 1 |
| Application fee | $75 |
| Fee waivers | Available (counselor signature, recruitment events, UI employees) |
| SAT/ACT policy | Test-optional (if provided, used in review) |
| Superscore | Yes (best section scores across test dates) |
| SAT code | 1836 |
| ACT code | 1836 |
| TOEFL code | 1836 |
| Interview policy | Not offered |
| Recommendations | Not required |
| Portfolio | Required for some FAA programs |
| Transfer deadline | March 1 (priority) |

> Source: admissions.illinois.edu/Apply/Freshman/dates

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|

| TOEFL iBT | 5.0 total (post-Jan 21, 2026) / 100 (pre-Jan 2026) | Competitive | Subscores all 4.5+ (new) / 20+ (old) |

| IELTS Academic | 7.5 total | Competitive | Subscores all 6.5+ |

| Duolingo English Test | 130 overall | Competitive | Subscores 125+ (Comprehension, Conversation, Literacy, Production) |

| SAT EBRW | No minimum | Competitive | Reviewed individually |

| ACT English | No minimum | Competitive | Reviewed individually |


> Note: Required for students who have not completed years 10-12 in an approved English-speaking country. Test scores must be taken within 2 years prior to enrollment. TOEFL iBT Special Home Edition accepted for fall 2026. IELTS OneSkill Retake, IELTS General, and TOEFL MyBest are NOT accepted.

> Source: admissions.illinois.edu/policies#english-competence

### 3.3 Graduate — global rules

- **Admissions model**: Decentralized (each program decides)
- **Application portal**: grad.illinois.edu/admissions/apply-now
- **Application fee**: $70 domestic / $90 international
- **GRE/GMAT**: Per-program (some required, some optional)
- **English proficiency**: Required for all international applicants
- **Minimum GPA**: 3.0 on last 60 hours (program may require higher)
- **CGS April-15 signatory**: Yes
- **TOEFL code**: 1836

> Source: grad.illinois.edu/admissions/graduate-admissions-minimum-requirements

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

#### Illinois Resident (Base Rate)

| Expense item | Amount | Description |
|-------------|--------|-------------|

| Tuition | $13,252 | Annual tuition (base rate) |
| Fees | $5,278 | Campus fees |
| Food & Housing | $15,858 | Double room + meal plan |
| Books & Supplies | $1,200 | Estimated |
| Other Expenses | $2,500 | Personal, transportation |
| **Total** | **$38,088** | |

#### Non-Resident (Base Rate)

| Expense item | Amount | Description |
|-------------|--------|-------------|

| Tuition | $35,928 | Annual tuition (base rate) |
| Fees | $5,278 | Campus fees |
| Food & Housing | $15,858 | Double room + meal plan |
| Books & Supplies | $1,200 | Estimated |
| Other Expenses | $2,840 | Personal, transportation |
| **Total** | **$61,104** | |

#### International (Base Rate)

| Expense item | Amount | Description |
|-------------|--------|-------------|

| Tuition | $36,970 | Annual tuition (other international) |
| Fees | $5,278 | Campus fees |
| Food & Housing | $15,858 | Double room + meal plan |
| Books & Supplies | $1,200 | Estimated |
| Other Expenses | $2,840 | Personal, transportation |
| **Total** | **$62,146** | |


> Note: LAS International rate is $38,576 (higher than other international). Tuition varies by major (Engineering, Business, etc. have differential rates).

> Source: cost.illinois.edu, registrar.illinois.edu/ug-tuition-rates-2627/

### 4.2 Undergraduate financial-aid policy

| Policy | Details |
|--------|---------|

| Need-blind/need-aware | Need-aware for all applicants (domestic and international) |
| Meets full need | Yes (for admitted students who demonstrate need) |
| Illinois Commitment | Free tuition for IL residents with family income ≤ $75,000 (effective fall 2025) |
| Merit scholarships | Available (separate application not required) |
| FAFSA priority deadline | March 15 |
| Loan-free packages | Available for qualifying students |
| International aid | Limited (need-aware, not guaranteed) |

> Source: osfa.illinois.edu/illinois-commitment/, admissions.illinois.edu/Invest/financial-aid

### 4.3 Graduate cost & funding framework

- **Tuition**: Varies by program and residency. Base rate ~$13,252 (resident) / ~$35,928 (non-resident) per year; professional programs have separate rates.
- **Funding**: Most PhD programs offer full funding (tuition waiver + stipend via RA/TA). Master's funding varies by program.
- **Application fee**: $70 domestic / $90 international
- **Fee waivers**: Available for financial hardship

> Source: grad.illinois.edu/admissions/, osfa.illinois.edu/cost/graduate-professional-cost/

---

## Section 5 — Evidence Chain Index

```yaml
---

# E-U-001: EA deadline
field: undergraduate.deadlines.EA
value: November 1
source_url: https://www.admissions.illinois.edu/Apply/Freshman/dates
source_snippet: "Early Action Deadline: November 1"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-002: RD deadline
field: undergraduate.deadlines.RD
value: January 5
source_url: https://www.admissions.illinois.edu/Apply/Freshman/dates
source_snippet: "Regular Decision Deadline: January 5"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-003: Application fee
field: undergraduate.application_fee
value: 75
source_url: https://www.admissions.illinois.edu/policies
source_snippet: "Applicants for admission must submit a $75 application fee"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-004: SAT/ACT policy
field: undergraduate.test_policy.SAT_ACT
value: test-optional (if provided, used in review)
source_url: https://www.admissions.illinois.edu/Apply/Freshman/requirements
source_snippet: "We accept either the ACT or SAT, and we don't prefer one over the other"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-005: TOEFL minimum
field: undergraduate.english_proficiency.TOEFL
value: 5.0 total (post-Jan 2026) / 100 (pre-Jan 2026)
source_url: https://www.admissions.illinois.edu/policies
source_snippet: "Score a minimum of 5.0 total with subscores all 4.5+"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-006: IELTS minimum
field: undergraduate.english_proficiency.IELTS
value: 7.5 total with subscores all 6.5+
source_url: https://www.admissions.illinois.edu/policies
source_snippet: "Score a minimum of 7.5 total with subscores all 6.5+"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-007: Duolingo minimum
field: undergraduate.english_proficiency.Duolingo
value: 130 overall with subscores 125+
source_url: https://www.admissions.illinois.edu/policies
source_snippet: "Score a minimum of 130 overall with subscores 125+"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-U-008: Resident tuition
field: undergraduate.cost.tuition_resident
value: $13,252
source_url: https://registrar.illinois.edu/ug-tuition-rates-2627/
source_snippet: "Summer 2026 through Spring 2027 (guaranteed rate): $13,252.00"

capture_date: 2026-07-05
evidence_type: official_webpage_table


# E-U-009: Non-resident tuition
field: undergraduate.cost.tuition_nonresident
value: $35,928
source_url: https://registrar.illinois.edu/ug-tuition-rates-2627/
source_snippet: "Nonresident Rate $35,928.00"

capture_date: 2026-07-05
evidence_type: official_webpage_table


# E-U-010: International tuition
field: undergraduate.cost.tuition_international
value: $36,970 (other intl) / $38,576 (LAS intl)
source_url: https://registrar.illinois.edu/ug-tuition-rates-2627/
source_snippet: "Other International Rate $36,970.00 / LAS International Rate $38,576.00"

capture_date: 2026-07-05
evidence_type: official_webpage_table


# E-U-011: Illinois Commitment threshold
field: undergraduate.financial_aid.illinois_commitment_income_threshold
value: $75,000
source_url: https://osfa.illinois.edu/illinois-commitment/
source_snippet: "If you're an Illinois resident whose family makes $75,000 or less"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-G-001: Grad application fee
field: graduate.application_fee
value: $70 domestic / $90 international
source_url: https://grad.illinois.edu/admissions/application-instructions
source_snippet: "Application fee: $70 (domestic), $90 (international)"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-G-002: Grad minimum GPA
field: graduate.minimum_gpa
value: 3.0 on last 60 hours
source_url: https://grad.illinois.edu/admissions/graduate-admissions-minimum-requirements
source_snippet: "Applicants must have earned at least a bachelor's degree"

capture_date: 2026-07-05
evidence_type: official_webpage


# E-P-001: Program directory
field: programs.total_catalog_entries
value: 537 (from catalog degree-programs index)
source_url: https://catalog.illinois.edu/degree-programs/
source_snippet: "537 programs in the degree programs index"

capture_date: 2026-07-05
evidence_type: official_webpage_table
```

---

## Section 6 — WeKnora Import Manifest

### Collection structure

```
uiuc-knowledge-base-v2/
├── 00-overview.md          (Section 0: counts, hierarchy, inventory, matrix)
├── 01-ug-aces.md           (ACES undergraduate programs)
├── 02-ug-ahs.md            (AHS undergraduate programs)
├── 03-ug-bus.md            (Business undergraduate programs)
├── 04-ug-educ.md           (Education undergraduate programs)
├── 05-ug-engr.md           (Engineering undergraduate programs)
├── 06-ug-faa.md            (Fine & Applied Arts undergraduate programs)
├── 07-ug-is.md             (Information Sciences undergraduate programs)
├── 08-ug-las.md            (LAS undergraduate programs)
├── 09-ug-media.md          (Media undergraduate programs)
├── 10-ug-socw.md           (Social Work undergraduate programs)
├── 11-ug-minors.md         (All undergraduate minors)
├── 12-grad-aces.md         (ACES graduate programs)
├── 13-grad-engr.md         (Engineering graduate programs)
├── 14-grad-las.md          (LAS graduate programs)
├── 15-grad-bus.md          (Business graduate programs)
├── 16-grad-other.md        (Other graduate programs)
├── 17-grad-certs.md        (Graduate certificates)
├── 18-prof.md              (Professional degrees: JD/MD/DVM)
├── 19-deadlines.md         (Section 3: deadlines & requirements)
├── 20-costs.md             (Section 4: costs & financial aid)
├── 21-evidence.md          (Section 5: evidence chain)
└── 22-comparison.md        (Section 7: cross-school framework)
```

## Section 7 — Cross-school Comparison Framework

| Dimension | UIUC | (other schools) |
|-----------|------|------------------|

| Type | Public |
| Location | Champaign, IL |
| EA deadline | November 1 |
| RD deadline | January 5 |
| Application fee | $75 |
| SAT/ACT required? | Test-optional |
| TOEFL min | 5.0 (new) / 100 (old) |
| IELTS min | 7.5 |
| Duolingo min | 130 |
| Resident tuition/yr | $13,252 (base) |
| Non-resident tuition/yr | $35,928 (base) |
| International tuition/yr | $36,970 (base) |
| Need-blind (domestic)? | No (need-aware) |
| Need-blind (international)? | No (need-aware) |
| Free tuition threshold | $75,000 (IL residents) |
| Total program count (Rule 1) | 649 |
| School/college count (Rule 2) | 16 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.illinois.edu, grad.illinois.edu, catalog.illinois.edu, registrar.illinois.edu, osfa.illinois.edu, cost.illinois.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program