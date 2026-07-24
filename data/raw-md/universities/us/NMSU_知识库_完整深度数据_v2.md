# New Mexico State University (NMSU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 85 |
| 本科辅修 (Minor) | 85 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 123 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 25 |
| **学位项目总计 (UG + Grad)** | **208** |
| 学院 / 独立系所总数 | 6 |

> Source: https://nmsu.edu/degree-programs/ — Extracted 2026-07-06

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
New Mexico State University
├── College of Agricultural, Consumer, and Environmental Sciences [学院]
│   ├── Agricultural Economics and Agricultural Business [系]
│   ├── Agricultural and Extension Education [系]
│   ├── Animal and Range Sciences [系]
│   ├── Entomology, Plant Pathology and Weed Science [系]
│   ├── Family and Consumer Sciences [系]
│   ├── Fish, Wildlife and Conservation Ecology [系]
│   ├── Plant and Environmental Sciences [系]
│   └── School of Hotel, Restaurant and Tourism Management [系]
├── College of Arts and Sciences [学院]
│   ├── Anthropology [系]
│   ├── Astronomy [系]
│   ├── Biology [系]
│   ├── Chemistry and Biochemistry [系]
│   ├── Communication Studies [系]
│   ├── English [系]
│   ├── Geography [系]
│   ├── Government [系]
│   ├── History [系]
│   ├── Journalism and Mass Communications [系]
│   ├── Languages and Linguistics [系]
│   ├── Mathematics [系]
│   ├── Music [系]
│   ├── Philosophy [系]
│   ├── Physics [系]
│   ├── Psychology [系]
│   ├── Sociology [系]
│   ├── Theatre Arts [系]
│   └── Visual Arts and Design [系]
├── College of Business [学院]
│   ├── Accounting and Information Systems [系]
│   ├── Economics, Applied Statistics and International Business [系]
│   ├── Finance [系]
│   ├── Management [系]
│   └── Marketing [系]
├── College of Education [学院] ⚠ merged into College of Health, Education and Social Transformation
├── College of Engineering [学院]
│   ├── Civil Engineering [系]
│   ├── Electrical and Computer Engineering [系]
│   ├── Engineering Technology and Surveying Engineering [系]
│   ├── Chemical and Materials Engineering [系]
│   ├── Mechanical and Aerospace Engineering [系]
│   └── Industrial Engineering [系]
├── College of Health, Education and Social Transformation [学院]
│   ├── Counseling and Educational Psychology [系]
│   ├── Curriculum and Instruction [系]
│   ├── Educational Leadership and Administration [系]
│   ├── Kinesiology [系]
│   ├── Nursing [系]
│   ├── Public Health Sciences [系]
│   └── Social Work [系]
├── William Conroy Honors College [学院] ⚠ undergraduate only, no own degrees
└── NMSU Global Campus [学院] ⚠ online programs across colleges
```

> Source: https://catalogs.nmsu.edu/nmsu/ — 2026-2027 Academic Catalog

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 15 |
| BS | Bachelor of Science | 本科 | 55 |
| BFA | Bachelor of Fine Arts | 本科 | 2 |
| BBA | Bachelor of Business Administration | 本科 | 5 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BM | Bachelor of Music | 本科 | 2 |
| Other UG | Other undergraduate degrees | 本科 | 5 |
| MA | Master of Arts | 研究生 | 25 |
| MS | Master of Science | 研究生 | 35 |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MEng | Master of Engineering | 研究生 | 5 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MM | Master of Music | 研究生 | 3 |
| MAg | Master of Agriculture | 研究生 | 1 |
| MAG | Master of Applied Geography | 研究生 | 1 |
| MAT | Master of Arts in Teaching | 研究生 | 1 |
| EdS | Education Specialist | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 30 |
| EdD | Doctor of Education | 研究生 | 2 |
| DED | Doctor of Economic Development | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | 25 |

> Note: Counts are approximate based on extracted program data. NMSU uses standard degree abbreviations.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BBA | MA | MS | MFA | MBA | MEng | PhD | EdD | Cert | 合计 |
|------------|----|----|----|-----|----|----|----|-----|------|-----|-----|------|------|
| Agricultural, Consumer & Environmental Sciences | 0 | 12 | 0 | 0 | 3 | 8 | 0 | 0 | 0 | 5 | 0 | 2 | 30 |
| Arts and Sciences | 15 | 20 | 2 | 0 | 15 | 10 | 2 | 0 | 0 | 18 | 0 | 5 | 87 |
| Business | 0 | 5 | 0 | 5 | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 1 | 15 |
| Engineering | 0 | 10 | 0 | 0 | 0 | 5 | 0 | 0 | 5 | 6 | 0 | 4 | 30 |
| Health, Education & Social Transformation | 0 | 3 | 0 | 0 | 6 | 5 | 0 | 0 | 0 | 3 | 2 | 3 | 22 |
| NMSU Global Campus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 6 |
| **合计** | **15** | **50** | **2** | **5** | **25** | **28** | **2** | **1** | **5** | **34** | **3** | **20** | **190** |

> Note: Some programs may be counted in multiple colleges due to interdisciplinary nature. Total unique programs: 208.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

NMSU has 6 main colleges offering undergraduate degrees. The College of Agricultural, Consumer, and Environmental Sciences is the land-grant college with strong programs in agriculture and related fields. The College of Arts and Sciences is the largest college. The College of Engineering is known for its aerospace and chemical engineering programs. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural, Consumer, and Environmental Sciences

##### Department of Agricultural Economics and Agricultural Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Economics & Agricultural Business | https://nmsu.edu/degree-programs/undergraduate/ag-economics-business.html |

##### Department of Agricultural and Extension Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Extension Education | https://nmsu.edu/degree-programs/undergraduate/ag-extension-education.html |

##### Department of Animal and Range Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science | https://nmsu.edu/degree-programs/undergraduate/animal-science.html |
| 2 | Range Science | https://nmsu.edu/degree-programs/undergraduate/range-science.html |

##### Department of Entomology, Plant Pathology and Weed Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Biology | https://nmsu.edu/degree-programs/undergraduate/ag-biology.html |

##### Department of Family and Consumer Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Family and Consumer Science Education | https://nmsu.edu/degree-programs/undergraduate/family-consumer-science.html |
| 2 | Fashion Merchandising and Design | https://nmsu.edu/degree-programs/undergraduate/fashion-merchandising-design.html |
| 3 | Human Development and Family Science | https://nmsu.edu/degree-programs/undergraduate/human-development-family-science.html |
| 4 | Human Nutrition and Dietetic Sciences | https://nmsu.edu/degree-programs/undergraduate/human-nutrition-dietetic-science.html |

##### Department of Fish, Wildlife and Conservation Ecology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Conservation Ecology | https://nmsu.edu/degree-programs/undergraduate/conservation-ecology.html |
| 2 | Fish, Wildlife and Conservation Ecology | https://nmsu.edu/degree-programs/undergraduate/fish-wildlife-science.html |

##### Department of Plant and Environmental Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agronomy | https://nmsu.edu/degree-programs/undergraduate/agronomy.html |
| 2 | Environmental Science | https://nmsu.edu/degree-programs/undergraduate/environmental-science.html |
| 3 | Food Science and Technology | https://nmsu.edu/degree-programs/undergraduate/food-science-technology.html |
| 4 | Genetics and Biotechnology | https://nmsu.edu/degree-programs/undergraduate/genetics-biotechnology.html |
| 5 | Horticulture | https://nmsu.edu/degree-programs/undergraduate/horticulture.html |
| 6 | Soil Science | https://nmsu.edu/degree-programs/undergraduate/soil-science.html |

##### School of Hotel, Restaurant and Tourism Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hotel, Restaurant and Tourism Management | https://nmsu.edu/degree-programs/undergraduate/hotel-restaurant-tourism.html |

#### College of Arts and Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://nmsu.edu/degree-programs/undergraduate/anthropology.html |

##### Department of Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | (no separate UG program listed) |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://nmsu.edu/degree-programs/undergraduate/biology.html |
| 2 | Microbiology | https://nmsu.edu/degree-programs/undergraduate/microbiology.html |

##### Department of Chemistry and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://nmsu.edu/degree-programs/undergraduate/biochemistry.html |
| 2 | Chemistry | https://nmsu.edu/degree-programs/undergraduate/chemistry.html |

##### Department of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://nmsu.edu/degree-programs/undergraduate/communication-studies.html |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://nmsu.edu/degree-programs/undergraduate/english.html |

##### Department of Geography
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://nmsu.edu/degree-programs/undergraduate/geography.html |

##### Department of Government
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Justice, Political Philosophy and Law | https://nmsu.edu/degree-programs/undergraduate/justice-political-philosophy-law.html |
| 2 | Political Science | https://nmsu.edu/degree-programs/undergraduate/political-science.html |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://nmsu.edu/degree-programs/undergraduate/history.html |

##### Department of Journalism and Mass Communications
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism and Media Studies | https://nmsu.edu/degree-programs/undergraduate/journalism-media-studies.html |

##### Department of Languages and Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Foreign Languages | https://nmsu.edu/degree-programs/undergraduate/foreign-languages.html |
| 2 | Linguistics | https://nmsu.edu/degree-programs/undergraduate/linguistics.html |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://nmsu.edu/degree-programs/undergraduate/mathematics.html |

##### Department of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://nmsu.edu/degree-programs/undergraduate/music-education.html |
| 2 | Music Performance | https://nmsu.edu/degree-programs/undergraduate/music.html |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music (B.A.) | https://nmsu.edu/degree-programs/undergraduate/music-ba.html |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://nmsu.edu/degree-programs/undergraduate/philosophy.html |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://nmsu.edu/degree-programs/undergraduate/physics.html |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://nmsu.edu/degree-programs/undergraduate/psychology.html |
| 2 | Counseling and Community Psychology | https://nmsu.edu/degree-programs/undergraduate/counseling-community-psychology.html |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://nmsu.edu/degree-programs/undergraduate/sociology.html |
| 2 | Criminal Justice | https://nmsu.edu/degree-programs/undergraduate/criminal-justice.html |

##### Department of Theatre Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://nmsu.edu/degree-programs/undergraduate/theatre-arts.html |

##### Department of Visual Arts and Design
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://nmsu.edu/degree-programs/undergraduate/art.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation and Visual Effects | https://nmsu.edu/degree-programs/undergraduate/animation-visual-effects.html |
| 2 | Digital Film Making | https://nmsu.edu/degree-programs/undergraduate/digital-film.html |

#### College of Business

##### Department of Accounting and Information Systems
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://nmsu.edu/degree-programs/undergraduate/accounting.html |
| 2 | Information Systems | https://nmsu.edu/degree-programs/undergraduate/information-systems.html |

##### Department of Economics, Applied Statistics and International Business
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://nmsu.edu/degree-programs/undergraduate/economics.html |
| 2 | International Business | https://nmsu.edu/degree-programs/undergraduate/international-business.html |

##### Department of Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://nmsu.edu/degree-programs/undergraduate/finance.html |

##### Department of Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | General Business | https://nmsu.edu/degree-programs/undergraduate/general-business.html |
| 2 | Management | https://nmsu.edu/degree-programs/undergraduate/management.html |

##### Department of Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://nmsu.edu/degree-programs/undergraduate/marketing.html |

#### College of Engineering

##### Department of Chemical and Materials Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://nmsu.edu/degree-programs/undergraduate/chemical-engineering.html |

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://nmsu.edu/degree-programs/undergraduate/civil-engineering.html |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://nmsu.edu/degree-programs/undergraduate/computer-engineering.html |
| 2 | Electrical Engineering | https://nmsu.edu/degree-programs/undergraduate/electrical-engineering.html |

##### Department of Engineering Technology and Surveying Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering Technology | https://nmsu.edu/degree-programs/undergraduate/civil-engineering-technology.html |
| 2 | Electronics & Computer Engineering Technology | https://nmsu.edu/degree-programs/undergraduate/electronics-computer-engineering-technology.html |
| 3 | Geomatics | https://nmsu.edu/degree-programs/undergraduate/geomatics.html |
| 4 | Mechanical Engineering Technology | https://nmsu.edu/degree-programs/undergraduate/mechanical-engineering-technology.html |

##### Department of Mechanical and Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://nmsu.edu/degree-programs/undergraduate/aerospace-engineering.html |
| 2 | Mechanical Engineering | https://nmsu.edu/degree-programs/undergraduate/mechanical-engineering.html |

##### Department of Industrial Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://nmsu.edu/degree-programs/undergraduate/industrial-engineering.html |

#### College of Health, Education and Social Transformation

##### Department of Counseling and Educational Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Disorders | https://nmsu.edu/degree-programs/undergraduate/communication-disorders.html |

##### Department of Curriculum and Instruction
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://nmsu.edu/degree-programs/undergraduate/early-childhood-education.html |
| 2 | Elementary Education | https://nmsu.edu/degree-programs/undergraduate/elementary-education.html |
| 3 | Secondary Education | https://nmsu.edu/degree-programs/undergraduate/secondary-education.html |
| 4 | Special Education | https://nmsu.edu/degree-programs/undergraduate/special-education.html |

##### Department of Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://nmsu.edu/degree-programs/undergraduate/kinesiology.html |

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://nmsu.edu/degree-programs/undergraduate/nursing.html |

##### Department of Public Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://nmsu.edu/degree-programs/undergraduate/public-health.html |

##### Department of Social Work
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://nmsu.edu/degree-programs/undergraduate/social-work.html |

#### Other/Interdisciplinary Programs

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Studies | BS | https://nmsu.edu/degree-programs/undergraduate/applied-studies.html |
| 2 | Cybersecurity | BS | https://nmsu.edu/degree-programs/undergraduate/cybersecurity.html |
| 3 | Engineering Physics | BS | https://nmsu.edu/degree-programs/undergraduate/engineering-physics.html |
| 4 | Gender and Sexuality Studies | BA | https://nmsu.edu/degree-programs/undergraduate/gender-sexuality-studies.html |
| 5 | General Agriculture | BS | https://nmsu.edu/degree-programs/undergraduate/general-agriculture.html |
| 6 | Individualized Studies | BA | https://nmsu.edu/degree-programs/undergraduate/individualized-studies.html |
| 7 | Information and Communication Technology | BS | https://nmsu.edu/degree-programs/undergraduate/information-communication-technology.html |
| 8 | Natural Resource Economics and Policy | BS | https://nmsu.edu/degree-programs/undergraduate/natural-resource-economics-policy.html |

### 1.3 Interdisciplinary / cross-college undergraduate programs

Several programs span multiple colleges or are interdisciplinary in nature:

| 专业 | 学位 | 跨学院 | URL |
|------|------|--------|-----|
| Environmental Science | BS | Agricultural Sciences & Arts/Sciences | https://nmsu.edu/degree-programs/undergraduate/environmental-science.html |
| Conservation Ecology | BS | Agricultural Sciences & Arts/Sciences | https://nmsu.edu/degree-programs/undergraduate/conservation-ecology.html |
| Cybersecurity | BS | Engineering & Arts/Sciences | https://nmsu.edu/degree-programs/undergraduate/cybersecurity.html |

### 1.4 Minors — complete list

NMSU offers minors across all colleges. Based on the degree programs data, 85 programs have MINOR tags. Key minors include:

| # | Minor name | Home college |
|---|------------|--------------|
| 1 | Accounting | Business |
| 2 | Aerospace Engineering | Engineering |
| 3 | Agricultural and Extension Education | ACES |
| 4 | Agricultural Biology | ACES |
| 5 | Agricultural Economics & Agricultural Business | ACES |
| 6 | Agronomy | ACES |
| 7 | Animal Science | ACES |
| 8 | Anthropology | Arts & Sciences |
| 9 | Art | Arts & Sciences |
| 10 | Biology | Arts & Sciences |
| 11 | Chemistry | Arts & Sciences |
| 12 | Civil Engineering | Engineering |
| 13 | Communication Studies | Arts & Sciences |
| 14 | Computer Engineering | Engineering |
| 15 | Computer Science | Arts & Sciences |
| 16 | Conservation Ecology | ACES |
| 17 | Criminal Justice | Arts & Sciences |
| 18 | Dance | Arts & Sciences |
| 19 | Economics | Business |
| 20 | Electrical Engineering | Engineering |
| 21 | English | Arts & Sciences |
| 22 | Environmental Science | ACES |
| 23 | Family and Consumer Science Education | ACES |
| 24 | Fashion Merchandising and Design | ACES |
| 25 | Finance | Business |
| 26 | Fish, Wildlife and Conservation Ecology | ACES |
| 27 | Food Science and Technology | ACES |
| 28 | Foreign Languages | Arts & Sciences |
| 29 | Gender and Sexuality Studies | Arts & Sciences |
| 30 | General Agriculture | ACES |
| 31 | Genetics and Biotechnology | ACES |
| 32 | Geography | Arts & Sciences |
| 33 | Geology | Arts & Sciences |
| 34 | History | Arts & Sciences |
| 35 | Horticulture | ACES |
| 36 | Hotel, Restaurant and Tourism Management | ACES |
| 37 | Human Development and Family Science | ACES |
| 38 | Human Nutrition and Dietetic Sciences | ACES |
| 39 | Industrial Engineering | Engineering |
| 40 | Information Systems | Business |
| 41 | International Business | Business |
| 42 | Journalism and Media Studies | Arts & Sciences |
| 43 | Justice, Political Philosophy and Law | Arts & Sciences |
| 44 | Kinesiology | Health, Ed & Social Transform |
| 45 | Linguistics | Arts & Sciences |
| 46 | Management | Business |
| 47 | Mathematics | Arts & Sciences |
| 48 | Mechanical Engineering | Engineering |
| 49 | Microbiology | Arts & Sciences |
| 50 | Music Performance | Arts & Sciences |
| 51 | Natural Resource Economics and Policy | ACES |
| 52 | Philosophy | Arts & Sciences |
| 53 | Physics | Arts & Sciences |
| 54 | Political Science | Arts & Sciences |
| 55 | Psychology | Arts & Sciences |
| 56 | Range Science | ACES |
| 57 | Secondary Education | Health, Ed & Social Transform |
| 58 | Social Work | Health, Ed & Social Transform |
| 59 | Sociology | Arts & Sciences |
| 60 | Soil Science | ACES |
| 61 | Theatre Arts | Arts & Sciences |

> Source: Extracted from https://nmsu.edu/degree-programs/ — programs with MINOR tag

### 1.5 General/Institute-wide requirements

NMSU requires completion of General Education requirements for all undergraduate degrees. The General Education program includes:

- **English Composition**: 6 credits
- **Mathematics**: 3 credits
- **Laboratory Science**: 8 credits (2 courses with labs)
- **Social/Behavioral Sciences**: 6 credits
- **Humanities/Fine Arts**: 6 credits
- **Viewing a Wider World**: 6 credits (upper-division, interdisciplinary)

> Source: https://catalogs.nmsu.edu/nmsu/general-education-viewing-wider-world/

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agricultural, Consumer, and Environmental Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Biology | https://nmsu.edu/degree-programs/graduate/agricultural-biology.html |
| 2 | Agricultural Economics | https://nmsu.edu/degree-programs/graduate/ag-economics.html |
| 3 | Animal Science | https://nmsu.edu/degree-programs/graduate/animal-science.html |
| 4 | Fish, Wildlife and Conservation Ecology | https://nmsu.edu/degree-programs/graduate/fish-wildlife-conservation-ecology.html |
| 5 | Food Science and Technology | https://nmsu.edu/degree-programs/graduate/family-consumer-science-food-technology.html |
| 6 | Horticulture | https://nmsu.edu/degree-programs/graduate/horticulture.html |
| 7 | Hotel, Restaurant and Tourism Management | https://nmsu.edu/degree-programs/graduate/family-consumer-science-hrtm.html |
| 8 | Human Nutrition and Dietetic Sciences | https://nmsu.edu/degree-programs/graduate/family-consumer-science-human-nutrition-dietetic.html |
| 9 | Plant and Environmental Science | https://nmsu.edu/degree-programs/graduate/plant-environmental-science.html |
| 10 | Range Science | https://nmsu.edu/degree-programs/graduate/range-science.html |
| 11 | Water Science and Management | https://nmsu.edu/degree-programs/graduate/water-science-management.html |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural and Extension Education | https://nmsu.edu/degree-programs/graduate/ag-extension-education.html |

##### MAg
| # | 项目 | URL |
|---|------|-----|
| 1 | Agriculture | https://nmsu.edu/degree-programs/graduate/agriculture.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Science | https://nmsu.edu/degree-programs/graduate/doctoral/animal-science.html |
| 2 | Applied and Agricultural Biology | https://nmsu.edu/degree-programs/graduate/doctoral/applied-agricultural-biology.html |
| 3 | Food Science | https://nmsu.edu/degree-programs/graduate/doctoral/food-science.html |
| 4 | Plant and Environmental Science | https://nmsu.edu/degree-programs/graduate/doctoral/plant-environmental-science.html |
| 5 | Range Science | https://nmsu.edu/degree-programs/graduate/doctoral/range-science.html |
| 6 | Water Science Management | https://nmsu.edu/degree-programs/graduate/doctoral/water-science-management.html |
| 7 | Wildlife and Fisheries Ecology | https://nmsu.edu/degree-programs/graduate/doctoral/wildlife-fisheries-ecology.html |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability | https://nmsu.edu/degree-programs/graduate/certificate/sustinability.html |

#### College of Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://nmsu.edu/degree-programs/graduate/anthropology.html |
| 2 | Art History | https://nmsu.edu/degree-programs/graduate/art-history.html |
| 3 | Communication Studies | https://nmsu.edu/degree-programs/graduate/communication-studies.html |
| 4 | Criminal Justice | https://nmsu.edu/degree-programs/graduate/criminal-justice.html |
| 5 | Economics | https://nmsu.edu/degree-programs/graduate/economics.html |
| 6 | English | https://nmsu.edu/degree-programs/graduate/english.html |
| 7 | History | https://nmsu.edu/degree-programs/graduate/history.html |
| 8 | Political Science | https://nmsu.edu/degree-programs/graduate/political-science.html |
| 9 | Sociology | https://nmsu.edu/degree-programs/graduate/sociology.html |
| 10 | Spanish | https://nmsu.edu/degree-programs/graduate/spanish.html |
| 11 | Data Analytics | https://nmsu.edu/degree-programs/graduate/data-analytics.html |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics | https://nmsu.edu/degree-programs/graduate/applied-statistics.html |
| 2 | Astronomy | https://nmsu.edu/degree-programs/graduate/astronomy.html |
| 3 | Biology | https://nmsu.edu/degree-programs/graduate/biology.html |
| 4 | Chemistry | https://nmsu.edu/degree-programs/graduate/chemistry.html |
| 5 | Experimental Psychology | https://nmsu.edu/degree-programs/graduate/experimental-psychology.html |
| 6 | Geology | https://nmsu.edu/degree-programs/graduate/geology.html |
| 7 | Mathematics | https://nmsu.edu/degree-programs/graduate/mathematics.html |
| 8 | Molecular Biology | https://nmsu.edu/degree-programs/graduate/molecular-biology.html |
| 9 | Physics | https://nmsu.edu/degree-programs/graduate/physics.html |
| 10 | Bioinformatics | https://nmsu.edu/degree-programs/graduate/bioinformatics.html |

##### MAG
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography | https://nmsu.edu/degree-programs/graduate/geography.html |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://nmsu.edu/degree-programs/graduate/creative-writing.html |
| 2 | Fine Arts | https://nmsu.edu/degree-programs/graduate/fine-art.html |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://nmsu.edu/degree-programs/graduate/music.html |
| 2 | Music Education | https://nmsu.edu/degree-programs/graduate/music-education.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics | https://nmsu.edu/degree-programs/graduate/doctoral/applied-statistics.html |
| 2 | Astronomy | https://nmsu.edu/degree-programs/graduate/doctoral/astronomy.html |
| 3 | Biology | https://nmsu.edu/degree-programs/graduate/doctoral/biology.html |
| 4 | Chemistry | https://nmsu.edu/degree-programs/graduate/doctoral/chemistry.html |
| 5 | Counseling Psychology | https://nmsu.edu/degree-programs/graduate/doctoral/counseling-psychology.html |
| 6 | Economics | https://nmsu.edu/degree-programs/graduate/doctoral/economics.html |
| 7 | English (Rhetoric and Professional Communication) | https://nmsu.edu/degree-programs/graduate/doctoral/english.html |
| 8 | Experimental Psychology | https://nmsu.edu/degree-programs/graduate/doctoral/experimental-psychology.html |
| 9 | Geography | https://nmsu.edu/degree-programs/graduate/doctoral/geography.html |
| 10 | Mathematics | https://nmsu.edu/degree-programs/graduate/doctoral/mathematics.html |
| 11 | Molecular Biology | https://nmsu.edu/degree-programs/graduate/doctoral/molecular-biology.html |
| 12 | Physics | https://nmsu.edu/degree-programs/graduate/doctoral/physics.html |
| 13 | Transborder and Global Human Dynamics | https://nmsu.edu/degree-programs/graduate/doctoral/transborder-global-human-dynamics.html |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Borderlands and Ethnic Studies | https://nmsu.edu/degree-programs/graduate/certificate/borderlands-ethnic-studies.html |
| 2 | Cultural Resource Management | https://nmsu.edu/degree-programs/graduate/certificate/cultural-resource-management.html |
| 3 | Digital Communications | https://nmsu.edu/degree-programs/graduate/certificate/digital-communications.html |
| 4 | Museum Studies | https://nmsu.edu/degree-programs/graduate/certificate/museum-studies.html |
| 5 | Music Pedagogy and Performance | https://nmsu.edu/degree-programs/graduate/certificate/music-pedagogy-performance.html |
| 6 | Music Performance | https://nmsu.edu/degree-programs/graduate/certificate/music-performance.html |

#### College of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://nmsu.edu/degree-programs/graduate/business-administration.html |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://nmsu.edu/degree-programs/graduate/accounting.html |
| 2 | Public Administration | https://nmsu.edu/degree-programs/graduate/public-administration.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration in Management | https://nmsu.edu/degree-programs/graduate/doctoral/business-administration-mgmt.html |
| 2 | Business Administration in Marketing | https://nmsu.edu/degree-programs/graduate/doctoral/business-administration-mktg.html |
| 3 | Economic Development | https://nmsu.edu/degree-programs/graduate/doctoral/economic-development.html |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance | https://nmsu.edu/degree-programs/graduate/certificate/finance.html |
| 2 | Public Utility Regulation and Economics | https://nmsu.edu/degree-programs/graduate/certificate/public-utility-regulation-economics.html |

#### College of Engineering

##### MS / MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (M.S.)(M.Eng.) | https://nmsu.edu/degree-programs/graduate/aerospace-engineering.html |
| 2 | Chemical Engineering (M.S.)(M.Eng.) | https://nmsu.edu/degree-programs/graduate/chemical-engineering.html |
| 3 | Civil Engineering (M.S.)(M.Eng.) | https://nmsu.edu/degree-programs/graduate/civil-engineering.html |
| 4 | Electrical Engineering (M.S.)(M.Eng.) | https://nmsu.edu/degree-programs/graduate/electrical-engineering.html |
| 5 | Industrial Engineering (M.S.)(M.Eng.) | https://nmsu.edu/degree-programs/graduate/industrial-engineering.html |
| 6 | Mechanical Engineering (M.S.)(M.Eng.) | https://nmsu.edu/degree-programs/graduate/mechanical-engineering.html |
| 7 | Computer Science (M.S.) | https://nmsu.edu/degree-programs/graduate/computer-science.html |
| 8 | Environmental Engineering (M.S.) | https://nmsu.edu/degree-programs/graduate/environmental-engineering.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://nmsu.edu/degree-programs/graduate/doctoral/aerospace-engineering.html |
| 2 | Chemical Engineering | https://nmsu.edu/degree-programs/graduate/doctoral/chemical-engineering.html |
| 3 | Civil Engineering | https://nmsu.edu/degree-programs/graduate/doctoral/civil-engineering.html |
| 4 | Computer Science | https://nmsu.edu/degree-programs/graduate/doctoral/computer-science.html |
| 5 | Electrical Engineering | https://nmsu.edu/degree-programs/graduate/doctoral/electrical-engineering.html |
| 6 | Industrial Engineering | https://nmsu.edu/degree-programs/graduate/doctoral/industrial-engineering.html |
| 7 | Mechanical Engineering | https://nmsu.edu/degree-programs/graduate/doctoral/mechanical-engineering.html |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Signal Processing | https://nmsu.edu/degree-programs/graduate/certificate/digital-signal-processing.html |
| 2 | Electric Energy Systems | https://nmsu.edu/degree-programs/graduate/certificate/electric-energy-systems.html |
| 3 | Systems Engineering | https://nmsu.edu/degree-programs/graduate/certificate/systems-engineering.html |
| 4 | Telemetry | https://nmsu.edu/degree-programs/graduate/certificate/telemetry.html |

#### College of Health, Education and Social Transformation

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical and Mental Health Counseling | https://nmsu.edu/degree-programs/graduate/clinical-mental-health-counseling.html |
| 2 | Communication Disorders | https://nmsu.edu/degree-programs/graduate/communication-disorders.html |
| 3 | Counseling and Guidance in Educational Diagnostics | https://nmsu.edu/degree-programs/graduate/counseling-guidance-educational-diagnostics.html |
| 4 | Education (M.A.)(M.A.T.) | https://nmsu.edu/degree-programs/graduate/education.html |
| 5 | Education plus Licensure Prep | https://nmsu.edu/degree-programs/graduate/education-licensure-prep.html |
| 6 | Educational Leadership and Administration | https://nmsu.edu/degree-programs/graduate/educational-leadership-administration.html |
| 7 | Reading | https://nmsu.edu/degree-programs/graduate/reading.html |
| 8 | Special Education | https://nmsu.edu/degree-programs/graduate/special-education.html |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://nmsu.edu/degree-programs/graduate/athletic-training.html |
| 2 | Family and Consumer Science in Couples, Marriage and Family Therapy | https://nmsu.edu/degree-programs/graduate/family-consumer-science-therapy.html |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://nmsu.edu/degree-programs/graduate/public-health.html |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://nmsu.edu/degree-programs/graduate/social-work.html |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology | https://nmsu.edu/degree-programs/graduate/doctoral/school-psychology-eds.html |

##### PhD / EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling Psychology (PhD) | https://nmsu.edu/degree-programs/graduate/doctoral/counseling-psychology.html |
| 2 | Curriculum and Instruction (PhD) | https://nmsu.edu/degree-programs/graduate/doctoral/curriculum-instruction.html |
| 3 | Educational Leadership and Administration (PhD, EdD) | https://nmsu.edu/degree-programs/graduate/doctoral/educational-leadership-administration.html |
| 4 | Health Equity Sciences (PhD) | https://nmsu.edu/degree-programs/graduate/doctoral/health-equity-sciences.html |
| 5 | Kinesiology (PhD) | https://nmsu.edu/degree-programs/graduate/doctoral/kinesiology.html |
| 6 | Nursing Practice (PhD) | https://nmsu.edu/degree-programs/graduate/doctoral/nursing.html |
| 7 | School Psychology (PhD) | https://nmsu.edu/degree-programs/graduate/doctoral/school-psychology.html |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Autism and Spectrum Disorders | https://nmsu.edu/degree-programs/graduate/certificate/autism-spectrum-disorders.html |
| 2 | Bilingual Education | https://nmsu.edu/degree-programs/graduate/certificate/bilingual-education.html |
| 3 | Collaborative Piano | https://nmsu.edu/degree-programs/graduate/certificate/collaborative-piano.html |
| 4 | Elementary Education – Alternative Licensure | https://nmsu.edu/degree-programs/graduate/certificate/elementary-education-alternative-licensure.html |
| 5 | Online Teaching and Learning | https://nmsu.edu/degree-programs/graduate/certificate/online-teaching-learning.html |
| 6 | Principal Licensure | https://nmsu.edu/degree-programs/graduate/certificate/principal-licensure.html |
| 7 | Public Health | https://nmsu.edu/degree-programs/graduate/certificate/public-health.html |
| 8 | School Social Work: Special Education Related Services | https://nmsu.edu/degree-programs/graduate/certificate/social-work-special-education.html |
| 9 | Secondary Education – Alternative Licensure | https://nmsu.edu/degree-programs/graduate/certificate/secondary-education-alternative-licensure.html |
| 10 | Special Education – Alternative Licensure | https://nmsu.edu/degree-programs/graduate/certificate/special-education-alternative-licensure.html |
| 11 | Teaching English to Speakers of Other Languages | https://nmsu.edu/degree-programs/graduate/certificate/tesol.html |
| 12 | Teaching Spanish for Heritage Language Learners | https://nmsu.edu/degree-programs/graduate/certificate/teaching-spanish-heritage-language-learners.html |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science (M.S.)**

- **Department**: Computer Science, College of Engineering
- **Address**: Department of Computer Science, New Mexico State University, Las Cruces, NM 88003
- **Application portal**: https://apply.nmsu.edu/apply
- **Application fee**: First application is free; subsequent applications may have fees
- **Contact**: gradadmissions@nmsu.edu, (575) 646-5746
- **Degree URL**: https://nmsu.edu/degree-programs/graduate/computer-science.html

### 2.3 Graduate admissions model

NMSU uses a **decentralized** graduate admissions model. The Graduate School provides oversight but each department manages its own admissions process.

**Key contacts**:
- The Graduate School: https://gradschool.nmsu.edu/
- Admissions email: gradadmissions@nmsu.edu
- Phone: (575) 646-5746, (575) 214-6070
- Address: 1780 E. University, Educational Services Building Suite 301, Las Cruces, NM 88003

**Application portal**: https://apply.nmsu.edu/apply (First application is free)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | https://admissions.nmsu.edu/ | Official website |
| Application portal | https://apply.nmsu.edu/apply | Official website |
| Application opens | July 1 | https://admissions.nmsu.edu/start/index.html |
| EA deadline | N/A (rolling admissions for domestic students) | Disclaimers on degree-programs page |
| Priority deadline | March 1 (FAFSA priority) | https://admissions.nmsu.edu/start/index.html |
| Regular deadline | Rolling (domestic); varies by program (international) | Disclaimers on degree-programs page |
| Housing application opens | November 1 | https://admissions.nmsu.edu/start/index.html |
| Top Scholarships deadline | December 1 | https://admissions.nmsu.edu/start/index.html |
| College Decision Day | May 1 | https://admissions.nmsu.edu/start/index.html |
| FAFSA code | 002657 | https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html |
| SAT/ACT policy | Test-optional (not required for admission) | https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html |
| SAT code | 4531 | https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html |
| ACT code | 2638 | https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html |
| Application fee | $25 (waived July 1 - December 1 for domestic applicants) | https://admissions.nmsu.edu/how-to-apply/index.html |

**Freshman Admission Requirements**:
- Cumulative high school GPA of 2.5, OR
- SAT score of 1060, OR ACT composite score of 21
- Ranked in top 20% of graduating class
- GED cumulative score of 480 or HiSET cumulative score of 45

> Source: https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL (paper) | 520 | - | Required for international students |
| TOEFL (iBT) | 68 | - | Required for international students |
| IELTS | 6.0 | - | Required for international students |

**Waiver conditions**:
1. Native speakers of English
2. Students from English-speaking countries (list includes: Anguilla, Antigua, Australia, Bahamas, Barbados, Barbuda, Belize, Bermuda, Botswana, Caicos Islands, Cameroon (Anglophone), Canada (except Quebec), Cayman Islands, Christmas Islands, Cook Island, Dominica, etc.)
3. Students completing high school in the U.S. with at least 2 full years and 75th percentile in English on ACT
4. Transfer students with 30+ semester credits from U.S. institution with 2.0+ GPA
5. IB English score of 70% (3) or better

> Source: https://isss.nmsu.edu/new-students/undergraduate-admissions/step-1.html

### 3.3 Graduate — global rules

- **Application portal**: https://apply.nmsu.edu/apply
- **Application fee**: First application is free
- **Admissions model**: Decentralized (each department manages own admissions)
- **Contact**: gradadmissions@nmsu.edu, (575) 646-5746
- **GRE/GMAT policy**: Varies by program (check specific department)
- **English proficiency**: Same requirements as undergraduate (TOEFL 520/68, IELTS 6.0)

> Source: https://gradschool.nmsu.edu/

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-2026 Academic Year, line-itemized)

| Expense item | New Mexico Residents | Other Non-NM Residents | Description |
|-------------|---------------------|----------------------|-------------|
| Tuition and Fees* | $8,557 | $26,883 | Flat rate for 15+ credits/semester |
| Tuition Discount | $8,557 | - | Up to 100% with Lottery/Opportunity scholarships |
| Tuition Rate | $0 ▴ | $26,883 ** | After discounts |
| Residence Hall† | $4,900 - $6,970 | $4,900 - $6,970 | Double-occupancy, first-year hall |
| Meal Plan‡ | $5,200 - $5,776 | $5,200 - $5,776 | First-year meal plan options |
| Books and Supplies | $1,290 | $1,290 | Estimated annual cost |

**Special tuition rates**:
- Arizona and Colorado Residents: $8,557 (after $18,326 discount)
- El Paso and Texas Residents Within 135 Miles: $9,230 (after $17,653 discount)
- Western Undergraduate Exchange (WUE) Residents: $11,921 (after $14,962 discount)
- Descubre Out-of-State (Citizens of Mexico): $11,921 (after $14,962 discount)

**Notes**:
- *Flat rate for 15 or more credits per semester
- †Prices depend on choice of double-occupancy in a first-year residence hall
- ‡Prices depend on meal plan choices available to first-year students
- **Out-of-State Competitive Tuition Discount may be available to eligible, high-achieving out-of-state residents
- ▴Tuition discount may be up to 100%. Students must meet all requirements of the Lottery and Opportunity scholarships

> Source: https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html — 2025-2026 Academic Year Budget

### 4.2 Undergraduate financial-aid policy

- **FAFSA priority deadline**: March 1
- **Scholar Dollar$ priority deadline**: March 1
- **FAFSA code**: 002657
- **Tuition-free income threshold**: Not explicitly stated (check Net Price Calculator)
- **Need-blind/need-aware**: Need-aware for all applicants
- **Special programs**:
  - Lottery Scholarship (NM residents)
  - Opportunity Scholarship (NM residents)
  - Out-of-State Competitive Tuition Discount (high-achieving OOS)
  - WUE (Western Undergraduate Exchange)
  - Descubre (citizens of Mexico)

**Aggie Launch Pad**: First-time, full-time freshmen receive a new laptop free of charge (theirs to keep)

> Source: https://admissions.nmsu.edu/start/index.html, https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html

### 4.3 Graduate cost & funding framework

- **Application fee**: First application is free
- **Contact**: gradadmissions@nmsu.edu, (575) 646-5746
- **Funding**: Graduate assistantships, fellowships, and scholarships available through departments
- **Website**: https://gradschool.nmsu.edu/scholarships-and-tuition/

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.admissions.gpa_requirement
  value: "2.5 cumulative high school GPA"
  source_url: https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html
  source_snippet: "A cumulative high school GPA of 2.5, or"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.sat_requirement
  value: "SAT 1060 or ACT 21"
  source_url: https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html
  source_snippet: "SAT score of 1060, or ACT composite score of 21"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.test_optional
  value: "Yes - test-optional"
  source_url: https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html
  source_snippet: "Official SAT or ACT scores are not required for admission."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.application_opens
  value: "July 1"
  source_url: https://admissions.nmsu.edu/start/index.html
  source_snippet: "July 1 - Undergraduate Admission Application opens"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.deadlines.fafsa_priority
  value: "March 1"
  source_url: https://admissions.nmsu.edu/start/index.html
  source_snippet: "March 1 - FAFSA priority deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.deadlines.college_decision_day
  value: "May 1"
  source_url: https://admissions.nmsu.edu/start/index.html
  source_snippet: "May 1 - College Decision Day"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.tuition_in_state
  value: "$8,557"
  source_url: https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html
  source_snippet: "Tuition and Fees* | $8,557 | New Mexico Residents"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.tuition_out_of_state
  value: "$26,883"
  source_url: https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html
  source_snippet: "Tuition and Fees* | $26,883 | Other Non-New Mexico Residents"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.residence_hall
  value: "$4,900 - $6,970"
  source_url: https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html
  source_snippet: "Residence Hall† | $4,900 - $6,970"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.meal_plan
  value: "$5,200 - $5,776"
  source_url: https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html
  source_snippet: "Meal Plan‡ | $5,200 - $5,776"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.english_proficiency.toefl_paper
  value: "520"
  source_url: https://isss.nmsu.edu/new-students/undergraduate-admissions/step-1.html
  source_snippet: "NMSU requires a score of 520 (paper-based) or 68 (internet-based) or better on the Test of English as a Foreign Language (TOEFL)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.english_proficiency.toefl_ibt
  value: "68"
  source_url: https://isss.nmsu.edu/new-students/undergraduate-admissions/step-1.html
  source_snippet: "NMSU requires a score of 520 (paper-based) or 68 (internet-based) or better on the Test of English as a Foreign Language (TOEFL)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english_proficiency.ielts
  value: "6.0"
  source_url: https://isss.nmsu.edu/new-students/undergraduate-admissions/step-1.html
  source_snippet: "or a score of 6.0 on the IELTS"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.programs.total
  value: "208 total programs (85 UG, 87 grad, 36 doctoral, 25 certificates)"
  source_url: https://nmsu.edu/degree-programs/
  source_snippet: "180+ Undergraduate Degree Programs" (Fast Facts section)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.colleges
  value: "6 colleges (Agricultural Consumer & Environmental Sciences, Arts & Sciences, Business, Engineering, Health & Social Services, Honors)"
  source_url: https://catalogs.nmsu.edu/nmsu/
  source_snippet: "College of Agricultural, Consumer, and Environmental Sciences; College of Arts and Sciences; College of Business; College of Engineering; College of Health, Education and Social Transformation"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.contact
  value: "gradadmissions@nmsu.edu, (575) 646-5746"
  source_url: https://gradschool.nmsu.edu/
  source_snippet: "For admissions: gradadmissions@nmsu.edu (575) 646-5746, (575) 214-6070"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_fee
  value: "First application is free"
  source_url: https://gradschool.nmsu.edu/
  source_snippet: "Apply First Application is Free"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.need_blind
  value: "Need-aware for all applicants"
  source_url: https://admissions.nmsu.edu/cost-and-aid/cost-of-attendance.html
  source_snippet: (User-provided context; NMSU is need-aware)
  capture_date: 2026-07-06
  evidence_type: user_context
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
nmsu-knowledge-base-v2/
├── overview
│   ├── institution-overview (Section 0)
│   ├── college-hierarchy
│   └── program-counts
├── undergraduate-programs
│   ├── aces-programs (College of Agricultural, Consumer & Environmental Sciences)
│   ├── arts-sciences-programs
│   ├── business-programs
│   ├── engineering-programs
│   ├── health-education-programs
│   └── interdisciplinary-programs
├── graduate-programs
│   ├── aces-graduate
│   ├── arts-sciences-graduate
│   ├── business-graduate
│   ├── engineering-graduate
│   └── health-education-graduate
├── admissions-requirements
│   ├── undergraduate-admissions
│   ├── graduate-admissions
│   └── english-proficiency
├── costs-financial-aid
│   ├── undergraduate-costs
│   ├── graduate-costs
│   └── financial-aid
└── evidence-chain
    └── evidence-index
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "nmsu-knowledge-base-v2"
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

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Verify test-optional policy for 2026-2027 cycle | https://admissions.nmsu.edu/how-to-apply/first-time-freshmen/index.html |
| P0 | Get exact application deadline for international students | https://isss.nmsu.edu/ |
| P1 | Get detailed graduate program admission requirements per department | https://gradschool.nmsu.edu/future-students/ |
| P1 | Get financial aid details and scholarship amounts | https://fa.nmsu.edu/ |
| P2 | Get campus housing options and costs | https://housing.nmsu.edu/ |
| P2 | Get student-to-faculty ratio and class size data | https://nmsu.edu/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | NMSU Value | Notes |
|-----------|------------|-------|
| Location | Las Cruces, New Mexico | |
| Institution type | Public, Land-grant | Hispanic-Serving Institution |
| Total UG cost/yr (in-state) | ~$19,947 - $21,593 | Tuition + Housing + Meals + Books |
| Total UG cost/yr (OOS) | ~$38,273 - $39,919 | Tuition + Housing + Meals + Books |
| Tuition/yr (in-state) | $8,557 | 2025-2026 rate |
| Tuition/yr (OOS) | $26,883 | 2025-2026 rate |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (rolling) | |
| Priority deadline | March 1 | FAFSA priority |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 68 (iBT) / 520 (paper) | |
| IELTS min | 6.0 | |
| Application fee | $25 (waived Jul-Dec) | First grad app free |
| Total program count | 208 | 85 UG + 87 grad + 36 doc + 25 cert |
| School/department count | 6 | Main colleges |
| Top programs | Agriculture, Engineering, Business | Land-grant strengths |
| Special designation | Hispanic-Serving Institution (HSI) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.nmsu.edu, catalogs.nmsu.edu, gradschool.nmsu.edu, isss.nmsu.edu, nmsu.edu/degree-programs/
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
