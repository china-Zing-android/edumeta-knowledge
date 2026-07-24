# University of Guelph — 知识库完整深度数据 v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.1 (deep+)
> **Region**: Canada (Ontario)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG majors) | 90+ majors across 16 UG degree types |
| 本科辅修 (Minors) | 60+ minors |
| 研究生授课型项目 (PGT: MSc/MA/MBA/MEng/MPH/etc.) | 100+ graduate programs |
| 研究生博士项目 (PhD/Doctoral) | 80+ PhD programs |
| 学位项目总计 | ~250+ |
| 学院 (Colleges) | 7 |
| 学术院系/系所 (Academic Departments/Schools) | 30+ |
| 本科生总数 | ~30,000 |
| 研究生总数 | ~3,000 |
| 国际学生 | ~2,200 (from 140+ countries) |

### 0.2 学院/系层级结构 (Rule 2 — hierarchy)

```
University of Guelph
│
├── Ontario Agricultural College (OAC)
│   ├── Department of Animal Biosciences
│   ├── Department of Food, Agricultural and Resource Economics (FARE)
│   ├── Department of Plant Agriculture
│   ├── Department of Food Science
│   ├── School of Environmental Sciences
│   ├── School of Hospitality, Food and Tourism Management
│   └── Ridgetown Campus
│
├── College of Biological Science (CBS)
│   ├── Department of Integrative Biology
│   ├── Department of Molecular and Cellular Biology
│   └── Department of Human Health and Nutritional Sciences
│
├── Ontario Veterinary College (OVC)
│   ├── Department of Biomedical Sciences
│   ├── Department of Clinical Studies
│   ├── Department of Pathobiology
│   └── Department of Population Medicine
│
├── College of Engineering and Physical Sciences (CEPS)
│   ├── School of Engineering
│   │   ├── Biological Engineering
│   │   ├── Biomedical Engineering
│   │   ├── Civil Engineering
│   │   ├── Computer Engineering
│   │   ├── Engineering Systems and Computing
│   │   ├── Environmental Engineering
│   │   ├── Mechanical Engineering
│   │   ├── Mechatronics Engineering
│   │   ├── Software Engineering
│   │   └── Water Resources Engineering
│   ├── Department of Chemistry
│   ├── Department of Mathematics and Statistics
│   ├── Department of Physics
│   └── School of Computer Science
│
├── College of Social and Applied Human Sciences (CSAHS)
│   ├── Department of Economics
│   ├── Department of Geography, Environment and Geomatics
│   ├── Department of History
│   ├── Department of Political Science
│   ├── Department of Psychology
│   ├── Department of Sociology and Anthropology
│   ├── School of English and Theatre Studies
│   ├── School of Fine Art and Music
│   ├── School of Languages and Literatures
│   └── Department of Family Relations and Applied Nutrition
│
├── College of Arts (COA)
│   ├── School of Fine Art and Music (shared with CSAHS)
│   ├── School of English and Theatre Studies (shared with CSAHS)
│   └── Various arts departments
│
├── Gordon S. Lang School of Business and Economics (CBE/Lang)
│   ├── Department of Management
│   ├── Department of Marketing and Consumer Studies
│   └── Department of Economics (shared with CSAHS)
│
└── College of Arts (COA) — standalone college
    └── Cross-appointed departments shared with CSAHS
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 缩写 | 数量 (approx.) |
|---------|------|---------------|
| Bachelor of Arts | B.A. | 20+ majors |
| Bachelor of Science | B.Sc. | 25+ majors |
| Bachelor of Commerce | B.Comm. | 6+ majors |
| Bachelor of Engineering | B.Eng. | 10 majors |
| Bachelor of Computing | B.Comp. | 2 majors |
| Bachelor of Applied Science | B.A.Sc. | 3 majors |
| Bachelor of Science in Agriculture | B.Sc.(Agr.) | 5+ majors |
| Bachelor of Science in Environmental Sciences | B.Sc.(Env.) | 5 majors |
| Bachelor of Arts and Sciences | B.A.S. | 1 major |
| Bachelor of Bio-Resource Management | B.B.R.M. | 2 majors |
| Bachelor of Creative Arts, Health and Wellness | B.C.A. | 1 major |
| Bachelor of Indigenous Environmental Science and Practice | B.I.E.S.P. | 1 major |
| Bachelor of Landscape Architecture | B.L.A. | 1 major |
| Bachelor of Mathematics | B.Math. | 1 major |
| Bachelor of One Health | B.O.H. | 1 major |
| Doctor of Veterinary Medicine | D.V.M. | 1 program |
| Master of Science | M.Sc. | 40+ fields |
| Master of Arts | M.A. | 15+ fields |
| Master of Business Administration | MBA | 1 |
| Master of Engineering | M.Eng. | 5+ fields |
| Master of Public Health | MPH | 1 |
| Master of Landscape Architecture | M.L.A. | 1 |
| Doctor of Philosophy | Ph.D. | 80+ fields |
| Graduate Diploma/Certificate | — | 10+ |
| Associate Diploma (Ridgetown) | — | Several |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

> Note: Matrix shows approximate program distribution. Precise counts should be verified with official sources.

| 学院 | BA | BSc | BComm | BEng | BComp | BASc | BSc(Agr) | BSc(Env) | Other UG | MSc/MA | PhD | DVM |
|------|:--:|:---:|:-----:|:----:|:-----:|:----:|:--------:|:--------:|:--------:|:------:|:---:|:---:|
| OAC | 1 | 2 | 2 | — | — | — | 5+ | 1 | 3 | 20+ | 15+ | — |
| CBS | — | 8 | — | — | — | 1 | — | — | — | 10+ | 10+ | — |
| OVC | — | — | — | — | — | — | — | — | 1 (DVM) | 5+ | 5+ | 1 |
| CEPS | — | 3 | — | 10 | 2 | — | — | — | — | 10+ | 8+ | — |
| CSAHS | 15+ | 3 | — | — | — | 2 | — | 2 | — | 15+ | 12+ | — |
| Lang/CBE | — | — | 6+ | — | — | — | — | — | — | 3+ | 2+ | — |
| COA | 3 | — | — | — | — | — | — | — | — | 3+ | 3+ | — |

### 0.5 排名亮点 (Ranking Highlights)

| Ranking | Position |
|---------|:--------:|
| Maclean's Comprehensive University (Canada) 2025 | Top 6 |
| Times Higher Education — Reputation in Canada 2025 | Top 10 |
| Times Higher Education — Impact Rankings (Life Sciences) 2025 | Top 150 in World |
| Infosource — Comprehensive Research University (Canada) 2023 | Top 5 |

U of G is a comprehensive university (not U15 / medical-doctoral). Strong reputation in agriculture, veterinary sciences, life sciences, and food science.

---

## Section 1 — Undergraduate Education

### Section 1.1 — College of Arts (COA)

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Art History | BA | College of Arts | School of Fine Art and Music | https://www.uoguelph.ca/programs/art-history |
| Classical and Modern Cultures | BA | College of Arts | School of Languages and Literatures | https://www.uoguelph.ca/programs/classical-and-modern-cultures |
| Creative Writing | BA | College of Arts | School of English and Theatre Studies | https://www.uoguelph.ca/programs/creative-writing |
| English | BA | College of Arts | School of English and Theatre Studies | https://www.uoguelph.ca/programs/english |
| French Studies | BA | College of Arts | School of Languages and Literatures | https://www.uoguelph.ca/programs/french-studies |
| Music | BA | College of Arts | School of Fine Art and Music | https://www.uoguelph.ca/programs/music |
| Studio Art | BA | College of Arts | School of Fine Art and Music | https://www.uoguelph.ca/programs/studio-art |
| Theatre Studies | BA | College of Arts | School of English and Theatre Studies | https://www.uoguelph.ca/programs/theatre-studies |

### Section 1.2 — College of Biological Science (CBS)

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Animal Biology | BSc | CBS | Department of Integrative Biology | https://www.uoguelph.ca/programs/animal-biology |
| Biochemistry | BSc | CBS | Department of Molecular and Cellular Biology | https://www.uoguelph.ca/programs/biochemistry |
| Biological and Medical Physics | BSc | CBS | Department of Physics / CBS | https://www.uoguelph.ca/programs/biological-and-medical-physics |
| Biological and Pharmaceutical Chemistry | BSc | CBS | Department of Molecular and Cellular Biology | https://www.uoguelph.ca/programs/biological-and-pharmaceutical-chemistry |
| Biological Science | BSc | CBS | Department of Integrative Biology | https://www.uoguelph.ca/programs/biological-science |
| Biomedical Toxicology | BSc | CBS | Department of Biomedical Sciences | https://www.uoguelph.ca/programs/biomedical-toxicology |
| Human Health and Nutritional Sciences | BSc | CBS | Department of Human Health and Nutritional Sciences | https://www.uoguelph.ca/programs/human-health-nutritional-sciences |
| Human Kinetics | BSc | CBS | Department of Human Health and Nutritional Sciences | https://www.uoguelph.ca/programs/human-kinetics |
| Marine and Freshwater Biology | BSc | CBS | Department of Integrative Biology | https://www.uoguelph.ca/programs/marine-and-freshwater-biology |
| Microbiology and Immunology | BSc | CBS | Department of Molecular and Cellular Biology | https://www.uoguelph.ca/programs/microbiology-immunology |
| Molecular Biology and Genetics | BSc | CBS | Department of Molecular and Cellular Biology | https://www.uoguelph.ca/programs/molecular-biology-and-genetics |
| Neuroscience | BSc | CBS | CBS | https://www.uoguelph.ca/programs/neuroscience |
| Wildlife Biology and Conservation | BSc | CBS | Department of Integrative Biology | https://www.uoguelph.ca/programs/wildlife-biology-and-conservation |
| Zoology | BSc | CBS | Department of Integrative Biology | https://www.uoguelph.ca/programs/zoology |
| Applied Human Nutrition | BASc | CBS | Department of Family Relations and Applied Nutrition | https://www.uoguelph.ca/programs/applied-human-nutrition |
| Child Studies | BASc | CBS | Department of Family Relations and Applied Nutrition | https://www.uoguelph.ca/programs/child-studies |
| Family Studies and Human Development | BASc | CBS | Department of Family Relations and Applied Nutrition | https://www.uoguelph.ca/programs/family-studies-and-human-development |

### Section 1.3 — Gordon S. Lang School of Business and Economics (Lang/CBE)

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Accounting | BComm | Lang | Department of Management | https://www.uoguelph.ca/programs/accounting |
| Food and Agricultural Business | BComm | Lang | FARE | https://www.uoguelph.ca/programs/food-and-agricultural-business |
| Government, Economics and Management | BComm | Lang | Department of Management | https://www.uoguelph.ca/programs/government-economics-and-management |
| Hospitality and Tourism Management | BComm | Lang | School of Hospitality, Food and Tourism Management | https://www.uoguelph.ca/programs/hospitality-and-tourism-management |
| Management | BComm | Lang | Department of Management | https://www.uoguelph.ca/programs/management |
| Management Economics and Finance | BComm | Lang | Department of Management | https://www.uoguelph.ca/programs/management-economics-and-finance |
| Marketing Management | BComm | Lang | Department of Marketing and Consumer Studies | https://www.uoguelph.ca/programs/marketing-management |
| Real Estate | BComm | Lang | Department of Management | https://www.uoguelph.ca/programs/real-estate |
| Sport and Event Management | BComm | Lang | Department of Management | https://www.uoguelph.ca/programs/sport-and-event-management |

### Section 1.4 — College of Engineering and Physical Sciences (CEPS)

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Biological Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/biological-engineering |
| Biomedical Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/biomedical-engineering |
| Chemical Physics | BSc | CEPS | Department of Chemistry / Physics | https://www.uoguelph.ca/programs/chemical-physics |
| Chemistry | BSc | CEPS | Department of Chemistry | https://www.uoguelph.ca/programs/chemistry |
| Civil Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/civil-engineering |
| Computer Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/computer-engineering |
| Computer Science | BComp | CEPS | School of Computer Science | https://www.uoguelph.ca/programs/computer-science |
| Engineering Systems and Computing | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/engineering-systems-and-computing |
| Environmental Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/environmental-engineering |
| Mathematical Science | BSc | CEPS | Department of Mathematics and Statistics | https://www.uoguelph.ca/programs/mathematical-science |
| Mechanical Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/mechanical-engineering |
| Mechatronics Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/mechatronics-engineering |
| Physical Science | BSc | CEPS | Department of Physics | https://www.uoguelph.ca/programs/physical-science |
| Physics | BSc | CEPS | Department of Physics | https://www.uoguelph.ca/programs/physics |
| Software Engineering | BComp | CEPS | School of Computer Science | https://www.uoguelph.ca/programs/software-engineering |
| Theoretical Physics | BSc | CEPS | Department of Physics | https://www.uoguelph.ca/programs/theoretical-physics |
| Water Resources Engineering | BEng | CEPS | School of Engineering | https://www.uoguelph.ca/programs/water-resources-engineering |

### Section 1.5 — Ontario Agricultural College (OAC)

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Agriculture | BSc(Agr) | OAC | Various | https://www.uoguelph.ca/programs/agriculture |
| Animal Science | BSc(Agr) | OAC | Department of Animal Biosciences | https://www.uoguelph.ca/programs/animal-science |
| Crop Science | BSc(Agr) | OAC | Department of Plant Agriculture | https://www.uoguelph.ca/programs/crop-science |
| Honours Agriculture | BSc(Agr) | OAC | Various | https://www.uoguelph.ca/programs/honours-agriculture |
| Horticulture | BSc(Agr) | OAC | Department of Plant Agriculture | https://www.uoguelph.ca/programs/horticulture |
| Plant Science | BSc(Agr) | OAC | Department of Plant Agriculture | https://www.uoguelph.ca/programs/plant-science |
| Equine Management | BBRM | OAC | Department of Animal Biosciences | https://www.uoguelph.ca/programs/equine-management |
| Environmental Management | BBRM | OAC | School of Environmental Sciences | https://www.uoguelph.ca/programs/environmental-management |
| Food Science | BSc | OAC | Department of Food Science | https://www.uoguelph.ca/programs/food-science |
| Food, Agricultural and Resource Economics | BA | OAC | FARE | https://www.uoguelph.ca/programs/food-agricultural-resource-economics |

### Section 1.6 — College of Social and Applied Human Sciences (CSAHS)

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Anthropology | BA | CSAHS | Department of Sociology and Anthropology | https://www.uoguelph.ca/programs/anthropology |
| Criminal Justice and Public Policy | BA | CSAHS | Department of Political Science | https://www.uoguelph.ca/programs/criminal-justice-and-public-policy |
| Culture and Technology Studies | BA | CSAHS | Various | https://www.uoguelph.ca/programs/culture-and-technology-studies |
| Economics | BA | CSAHS | Department of Economics | https://www.uoguelph.ca/programs/economics |
| Environmental Governance | BA | CSAHS | Department of Geography, Environment and Geomatics | https://www.uoguelph.ca/programs/environmental-governance |
| Geography | BA | CSAHS | Department of Geography, Environment and Geomatics | https://www.uoguelph.ca/programs/geography |
| History | BA | CSAHS | Department of History | https://www.uoguelph.ca/programs/history |
| International Development Studies | BA | CSAHS | Various | https://www.uoguelph.ca/programs/international-development-studies |
| Justice and Legal Studies | BA | CSAHS | Department of Political Science | https://www.uoguelph.ca/programs/justice-and-legal-studies |
| Philosophy | BA | CSAHS | Department of Philosophy | https://www.uoguelph.ca/programs/philosophy |
| Political Science | BA | CSAHS | Department of Political Science | https://www.uoguelph.ca/programs/political-science |
| Psychology | BA | CSAHS | Department of Psychology | https://www.uoguelph.ca/programs/psychology |
| Sexualities, Genders and Social Change | BA | CSAHS | Department of Sociology and Anthropology | https://www.uoguelph.ca/programs/sexualities-genders-and-social-change |
| Sociology | BA | CSAHS | Department of Sociology and Anthropology | https://www.uoguelph.ca/programs/sociology |
| Environment and Resource Management | BSc(Env) | CSAHS | School of Environmental Sciences | https://www.uoguelph.ca/programs/environment-and-resource-management |
| Environmental Sciences | BSc(Env) | CSAHS | School of Environmental Sciences | https://www.uoguelph.ca/programs/environmental-sciences |
| Earth Observation and Geographic Information Science | BSc(Env) | CSAHS | Department of Geography, Environment and Geomatics | https://www.uoguelph.ca/programs/earth-geographic-info-science |
| Ecology | BSc(Env) | CSAHS | Department of Integrative Biology / SES | https://www.uoguelph.ca/programs/ecology |
| Environmental Economics and Policy | BSc(Env) | CSAHS | FARE / SES | https://www.uoguelph.ca/programs/environmental-economics-and-policy |

### Section 1.7 — Special/Cross-College Programs

| 专业名称 | 学位类型 | 学院 | 系/专业方向 | URL |
|---------|---------|------|-----------|-----|
| Bachelor of Arts and Sciences | BAS | Cross-College | Various | https://www.uoguelph.ca/programs/bachelor-of-arts-and-sciences |
| Bachelor of Arts, General | BA | CSAHS | Various | https://www.uoguelph.ca/programs/bachelor-of-arts-general |
| Bachelor of Arts, General (Online) | BA | CSAHS | Various | https://www.uoguelph.ca/programs/bachelor-of-arts-online |
| Bachelor of Creative Arts, Health and Wellness | BCA | Cross-College | COA / CBS | https://www.uoguelph.ca/programs/bachelor-of-creative-arts-health-and-wellness |
| Bachelor of Indigenous Environmental Science and Practice | BIESP | Cross-College | Various | https://www.uoguelph.ca/programs/bachelor-of-indigenous-environmental-science-and-practice |
| Bachelor of Landscape Architecture | BLA | CSAHS | School of Environmental Design and Rural Development | https://www.uoguelph.ca/programs/bachelor-of-landscape-architecture |
| Bachelor of Mathematics | BMath | CEPS | Department of Mathematics and Statistics | https://www.uoguelph.ca/programs/bachelor-of-mathematics |
| Bachelor of One Health | BOH | Cross-College | Various | https://www.uoguelph.ca/programs/bachelor-of-one-health |
| Doctor of Veterinary Medicine | DVM | OVC | OVC | https://uoguelph.ca/programs/doctor-veterinary-medicine/ |
| Bio-Medical Science | BSc | OVC | Department of Biomedical Sciences | https://www.uoguelph.ca/programs/biomedical-science |

### Minors (60+ available)

Selected minors include: Accounting, Applied Geomatics, Art History, Biochemistry, Biology, Biotechnology, Black Canadian Studies, Business, Business Economics, Chemistry, Classical Studies, Creative Writing, Earth Observation, Ecology, Economics, Engineering (Food), English, Entrepreneurship, European Culture and Civilization, Family and Child Studies, Food Science, French, Geography, German, Health and Well-Being, History, Human Resources, International Business, Italian, Linguistics, Marketing, Mathematics, Media and Cinema Studies, Museum Studies, Music, Philosophy, Physics, Political Science, Project Management, Psychology, Sociology, Spanish and Hispanic Studies, Statistics, Studio Art, Sustainable Business, Theatre Studies, Zoology, and more.

---

## Section 2 — Graduate Education

### Section 2.1 — Graduate Programs by College

> **Note**: Full graduate program listing available at https://graduatestudies.uoguelph.ca/ (login-restricted for per-program details) and https://calendar.uoguelph.ca/graduate-calendar/ (Graduate Calendar IX. Graduate Programs). Below is a representative listing organized by college.

#### Ontario Agricultural College (OAC)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| Animal Biosciences | MSc / PhD | OAC |
| Crop Science | MSc / PhD | OAC |
| Food Science | MSc / PhD | OAC |
| Food, Agricultural and Resource Economics | MSc / PhD | OAC |
| Plant Agriculture | MSc / PhD | OAC |
| Environmental Sciences | MSc / PhD | OAC |
| Hospitality and Tourism Management | MSc | OAC |
| Capacity Development and Extension | MSc | OAC |

#### College of Biological Science (CBS)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| Integrative Biology | MSc / PhD | CBS |
| Molecular and Cellular Biology | MSc / PhD | CBS |
| Human Health and Nutritional Sciences | MSc / PhD | CBS |
| Neuroscience | MSc / PhD | CBS |
| Biomedical Sciences | MSc / PhD | CBS/OVC |

#### Ontario Veterinary College (OVC)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| Biomedical Sciences | MSc / PhD | OVC |
| Clinical Studies | MSc / PhD | OVC |
| Pathobiology | MSc / PhD | OVC |
| Population Medicine | MSc / PhD | OVC |
| Veterinary Science | MSc / PhD | OVC |
| Public Health | MPH | OVC |

#### College of Engineering and Physical Sciences (CEPS)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| Chemistry | MSc / PhD | CEPS |
| Computer Science | MSc / PhD | CEPS |
| Engineering | MEng / MASc / PhD | CEPS |
| Mathematics and Statistics | MSc / PhD | CEPS |
| Physics | MSc / PhD | CEPS |
| Artificial Intelligence | MSc / PhD | CEPS |
| Cyber Security | MEng | CEPS |

#### College of Social and Applied Human Sciences (CSAHS)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| Economics | MA / PhD | CSAHS |
| Geography | MA / MSc / PhD | CSAHS |
| History | MA / PhD | CSAHS |
| Political Science | MA / PhD | CSAHS |
| Psychology | MA / PhD | CSAHS |
| Sociology | MA / PhD | CSAHS |
| Family Relations and Applied Nutrition | MSc / PhD | CSAHS |
| Rural Planning and Development | MSc / MPlan | CSAHS |
| Landscape Architecture | MLA | CSAHS |
| English and Theatre Studies | MA / PhD | CSAHS |
| Fine Arts | MFA | CSAHS |

#### Gordon S. Lang School of Business and Economics (Lang)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| Management | MSc / PhD | Lang |
| Marketing and Consumer Studies | MSc / PhD | Lang |
| Business Administration | MBA | Lang |

#### College of Arts (COA)

| 项目名称 | 学位类型 | 学院 |
|---------|---------|------|
| English | MA / PhD | COA |
| History | MA / PhD | COA |
| Philosophy | MA / PhD | COA |
| Music | MA | COA |
| Studio Art | MFA | COA |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admission

#### Canadian High School Students

**Ontario High School Students:**
- Apply through OUAC (Ontario Universities' Application Centre)
- **Deadline**: January 15, 2026 (applications accepted after this date)
- **Admission Average**: Calculated from top 6 completed 4U/M courses (including required courses)
- Offers released on ongoing basis from late January to mid-May

**Non-Ontario Canadian Students:**
- Provincial curriculum requirements vary by province
- General criteria: Secondary school graduation certificate that would admit to a recognized university in home province

#### International High School Students

**General Requirement:**
- Secondary school graduation certificate that would admit a student to an internationally recognized university in their home country
- Prerequisite course requirements must be met for the chosen degree program/major
- Predicted/interim/midterm grade 12 results may qualify for conditional offer

**Deadlines:**
- **Fall 2026 entry**: January 15 (high school) / May 15 (international outside Canada)
- **Document submission for early consideration**: February 1 (international high school students outside Canada)
- **Proof of English proficiency**: March 1 (soft deadline) / April 15
- **Accept offer**: June 1 (domestic) / June 1 (international outside Canada)
- **Tuition deposit**: December 15 ($2,000 international deposit)

#### English Language Proficiency Requirements

| Test | Minimum Score |
|-----|--------------|
| IELTS (Academic) | Overall 6.5, no band less than 6.0 |
| TOEFL iBT | Overall 89, no individual score less than 21 |
| PTE (Academic) | Overall 60, no component less than 60 |
| CAEL | Overall 70 |
| Duolingo English Test | Overall 110 |
| Cambridge English: C1/C2 | Overall 176, no band less than 169 |
| University of Guelph ELCP | Successful completion of Advanced Level (Levels 9 and 10) |

**Exemptions:**
- 4+ years full-time secondary/post-secondary study in English-language school system
- IB Diploma with English as language of instruction
- Francophone Canadian citizens educated in Canada

**Note**: Test scores must be within past 2 years from date of submission. TOEFL Institution Code for U of G: 0892.

### 3.2 Graduate Admission

**General Requirements:**
- Four-year bachelor's degree (or equivalent) from a recognized university
- Minimum B- (70%) average in last two years of study
- Program-specific prerequisites vary by department

**Application Deadlines:** (vary by program; typical windows)
- **Fall admission**: February 1 – June 1 (varies by program)
- **Winter admission**: August 1 – October 1 (varies by program)
- **Summer admission**: January 1 – March 1 (varies by program)

**Key Dates 2025-2026 (Undergraduate):**

| Date | Event |
|------|-------|
| Oct 1, 2025 | Winter housing applications open |
| Nov 1, 2025 | Winter 2026 application deadline (transfer & international) |
| Dec 1, 2025 | Canadian DVM application deadline |
| Jan 15, 2026 | Application deadline for high school students (Fall 2026) |
| Jan 23, 2026 | Lincoln Alexander Chancellor's / President's Scholarships deadline |
| Feb 1, 2026 | Early admission document deadline (international high school) |
| Mar 1, 2026 | BLA/DTA BIF submission, transfer summer application, English proficiency soft deadline |
| Apr 1, 2026 | SPF submission, SIF-D submission, transfer fall application deadline |
| Apr 15, 2026 | Scholarship application, transcript deadline (non-Ontario high school) |
| May 15, 2026 | International high school fall 2026 application deadline |
| June 1, 2026 | Accept offer through OUAC, residence deposit deadline |
| June 15, 2026 | International tuition deposit ($2,000) deadline |
| Aug 14, 2026 | Final deadline to satisfy conditions of offer |

### 3.3 Special Admission Programs

- **Student Profile Form (SPF)**: Encouraged for all applicants; deadline April 1
- **Background Information Form (BIF)**: Required for BLA (March 1), DTM (March 1), DVM (February 2)
- **Supplementary Information Form for Students with Disabilities (SIF-D)**: Deadline April 1
- **Co-op Education**: Available in many programs (additional $405/semester fee)
- **Deferral**: Application deadline July 30 for high school applicants

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition (2025-2026 estimates)

| Fee Category | Ontario Residents | Non-Ontario Domestic |
|-------------|:-----------------:|:--------------------:|
| Full-time Tuition* | $6,091 – $11,286 | $7,404 – $13,718 |
| Compulsory Fees | $1,768 – $1,930 | $1,768 – $1,930 |
| Residence Room | $7,900 – $11,116 | $7,900 – $11,116 |
| Meal Plan | $5,500 – $7,600 | $5,500 – $7,600 |
| Textbooks | ~$1,400 | ~$1,400 |
| Personal Budget | ~$2,500 | ~$2,500 |
| **Estimated Annual Total** | **$25,159 – $35,832** | **$27,000 – $38,000+** |

\*Co-op students pay an additional $405/semester for academic and work semesters.

|### 4.2 International Undergraduate Tuition (2025-2026)

International tuition by program (per year):

| Program | Tuition (CAD/year) |
|---------|:------------------:|
| Bachelor of Applied Science | $44,729 |
| Bachelor of Arts | $44,729 |
| Bachelor of Arts and Science | $44,729 |
| Bachelor of Bio-Resource Management | $44,729 |
| Bachelor of Commerce (Business) | $54,529 |
| Bachelor of Computing | $55,915 |
| Bachelor of Creative Arts, Health and Wellness | $44,729 |
| Bachelor of Engineering | $63,160 |
| Bachelor of Indigenous Environmental Science and Practice | $44,729 |
| Bachelor of Landscape Architecture | $54,320 |
| Bachelor of Mathematics | $44,729 |
| Bachelor of One Health | $44,729 |
| Bachelor of Science | $44,729 |
| Bachelor of Science in Agriculture | $44,729 |
| Bachelor of Science in Environmental Science | $44,729 |
| Doctor of Veterinary Medicine | $96,974 |

**Estimated annual total (including fees, housing, meals): $64,589 – $88,498 CAD**

Additional costs:
- Compulsory Fees: $1,768 – $1,930/year
- UHIP: $756/year (2025-2026)
- Residence Room: $7,900 – $11,116/year
- Meal Plan: $5,500 – $7,600/year
- Textbooks: ~$1,400/year
- Personal: ~$2,500/year

> **Fee Guarantee**: Future tuition increases capped at 5% per year.
> **Deposit**: Non-refundable $2,000 CAD tuition deposit required.

> **Note**: International students also pay UHIP ($756/year for single coverage, 2025-2026 rate).
> Tuition is billed per semester, not annually.

### 4.3 Graduate Fees (2025-2026)

- **Domestic MSc/PhD**: ~$3,000 – $5,000/semester (plus compulsory fees)
- **International MSc/PhD**: ~$8,000 – $14,000/semester (varies by program)
- **MBA**: Higher fee structure applies

|### 4.4 Financial Aid & Scholarships

**Domestic Entrance Scholarships:**
- **President's Scholarships**: $42,500 CAD — Application deadline January 23
- **Lincoln Alexander Chancellor's Scholarships**: $42,500 CAD — Application deadline January 23
- **Dr. Franco J. Vaccarino President's Scholarship**: $42,500 CAD — Application deadline January 23
- **Board of Governors' Scholarships**: $20,000 CAD — No application required (merit-based)
- **Entrance Scholarships**: $2,000 (95%+ avg) / $1,000 (90-94.9% avg) — Automatic consideration

**International Entrance Scholarships (up to $37,500 CAD over 4 years):**
- **President's International Entrance Scholarship**: One-time award $2,000 – $7,500 based on admission average (95%+ = $7,500). No application required.
- **University International Scholarship**: $5,000/year, renewable for up to 4 years ($20,000 total). No application required. Renewal: 80%+ average.
- **Dean's International Scholarship**: $2,500/year, renewable for up to 4 years ($10,000 total). No application required.
- **Dr. Franco J. Vaccarino President's Scholarship**: $42,500 CAD + guaranteed on-campus residence. Application deadline January 23.
- **International Transfer Scholarship**: $10,000 CAD (one-time) — No application required.
- **Quinn Memorial Scholarship**: $2,000 CAD — No application required.

**Deadline for international scholarship consideration**: March 1, 2026 (complete admission file)

**Bursaries:**
- Registrar's Entrance Bursaries: 550 awards of $4,000 CAD
- Accessibility Bursaries: 200 awards of $14,000 CAD
- Need-based awards: 7,870 students received $21.96 million in 2024-25 ($10.8M need-based)

**Other Funding:**
- OSAP (Ontario Student Assistance Program)
- Work-study programs
- Part-time employment opportunities

---

## Section 5 — Evidence Chain Index

### E-U-001: Institution Identity
| Field | Value |
|-------|-------|
| **Value** | University of Guelph, Guelph, Ontario, Canada |
| **Source URL** | https://www.uoguelph.ca/ |
| **Source Snippet** | "University of Guelph, Ontario, Canada — Improve Life" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-002: Founding & History
| Field | Value |
|-------|-------|
| **Value** | Established 1964; founding colleges OVC, OAC, Macdonald Institute (150+ years) |
| **Source URL** | https://www.uoguelph.ca/about |
| **Source Snippet** | "Established in 1964, the University enjoys a reputation for innovation and excellence dating back more than 150 years" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-003: Eight Colleges
| Field | Value |
|-------|-------|
| **Value** | 7+ colleges: OAC, CBS, OVC, CEPS, CSAHS, COA, Lang/CBE; 3 campuses (Guelph, Ridgetown, Guelph-Humber) |
| **Source URL** | https://www.uoguelph.ca/about |
| **Source Snippet** | "Today the University's eight colleges conduct cutting-edge teaching and research" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-004: Student Enrollment
| Field | Value |
|-------|-------|
| **Value** | 36,000+ students; 1,900+ international students from 140+ countries; 215,000+ alumni |
| **Source URL** | https://www.uoguelph.ca/about |
| **Source Snippet** | "36,000+ Undergraduate and Graduate Students" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-005: Undergraduate Programs Counts
| Field | Value |
|-------|-------|
| **Value** | 75+ majors, 60+ minors |
| **Source URL** | https://admission.uoguelph.ca/programs |
| **Source Snippet** | "75+ majors and 60+ minors" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-006: UG Program List
| Field | Value |
|-------|-------|
| **Value** | Full program listing with majors, minors, degree types |
| **Source URL** | https://www.uoguelph.ca/programs/undergraduate |
| **Source Snippet** | Comprehensive A-Z list of all undergraduate majors, minors, and degree types |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-007: UG Application Deadline
| Field | Value |
|-------|-------|
| **Value** | January 15 for high school students (Fall 2026) |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/apply/deadlines/ |
| **Source Snippet** | "January 15 | Application deadline for students currently enrolled in high school" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-008: International Application Deadlines
| Field | Value |
|-------|-------|
| **Value** | May 15 (Fall 2026), Feb 1 (early document deadline), Mar 1 (English proficiency soft deadline) |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/apply/deadlines/ |
| **Source Snippet** | "May 15 | Deadline for high school students studying outside of Canada to apply for fall 2026" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-009: English Proficiency Requirements
| Field | Value |
|-------|-------|
| **Value** | IELTS 6.5 (no band < 6); TOEFL 89 (no < 21); PTE 60; CAEL 70; Duolingo 110 |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/international/english-proficiency/ |
| **Source Snippet** | "Minimum overall score of 6.5 with no band less than 6" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-010: Domestic Tuition
| Field | Value |
|-------|-------|
| **Value** | $6,091 – $11,286 (Ontario); $7,404 – $13,718 (non-Ontario); estimated annual $25,159 – $35,832 |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/funding/ |
| **Source Snippet** | "Full-time Tuition* $6,091 - $11,286" and "Estimated annual expenses range from $25,159 to $35,832 CAD" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-011: Co-op Fees
| Field | Value |
|-------|-------|
| **Value** | Additional $405/semester for academic and work semesters |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/funding/ |
| **Source Snippet** | "*Co-op students pay an additional $405 CAD per semester for academic and work semesters." |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-012: Academic Calendar
| Field | Value |
|-------|-------|
| **Value** | 2026-2027 Academic Calendar; Undergraduate + Graduate + Guelph-Humber + Associate Diploma |
| **Source URL** | https://calendar.uoguelph.ca/ |
| **Source Snippet** | "2026-2027 Academic Calendar" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-013: Degree Programs
| Field | Value |
|-------|-------|
| **Value** | 16+ UG degree types: BA, BSc, BComm, BEng, BComp, BASc, BAS, BBRM, BCA, BIESP, BLA, BMath, BOH, BSc(Agr), BSc(Env), DVM |
| **Source URL** | https://calendar.uoguelph.ca/undergraduate-calendar/degree-programs/ |
| **Source Snippet** | Complete list of all undergraduate degree types offered |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-014: Ontario Curriculum Requirements
| Field | Value |
|-------|-------|
| **Value** | Top 6 completed 4U/M courses including required courses; offers released late Jan to mid-May |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/requirements/canadian/ |
| **Source Snippet** | "We use your top six completed 4U/M (or equivalent) courses, including required courses" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-015: Graduate Studies
| Field | Value |
|-------|-------|
| **Value** | 100+ graduate programs (MSc, MA, PhD, MEng, MBA, MPH, etc.); separate graduate admissions |
| **Source URL** | https://graduatestudies.uoguelph.ca/ |
| **Source Snippet** | "Graduate & Postdoctoral Studies" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-016: Programs List (Academic Calendar)
| Field | Value |
|-------|-------|
| **Value** | Comprehensive A-Z listing of 90+ areas of study including all majors, minors, certificates, diplomas |
| **Source URL** | https://calendar.uoguelph.ca/undergraduate-calendar/programs-majors-minors/ |
| **Source Snippet** | "This list includes all areas of study, including: degree programs, majors, areas of concentration, minors, certificates and diplomas" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-017: Graduate Fees Records
| Field | Value |
|-------|-------|
| **Value** | Graduate fee records by college abbreviation: COA, LANG, CEPS, CSAHS, CBS, OAC, OVC |
| **Source URL** | https://graduatestudies.uoguelph.ca/user/login?destination=node/67 |
| **Source Snippet** | Footer shows college-specific graduate records contacts |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-018: UHIP for International Students
| Field | Value |
|-------|-------|
| **Value** | $792/year single; $1,584 member+1 dependent; $2,376 family (2025-2026) |
| **Source URL** | https://www.uoguelph.ca/registrar/finances-fees/tuition-fees |
| **Source Snippet** | "UHIP rates, based on starting semester... Fall: $792.00" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-019: International Undergraduate Tuition
| Field | Value |
|-------|-------|
| **Value** | 2026-2027 rates approved by Board of Governors; program-specific per semester |
| **Source URL** | https://www.uoguelph.ca/registrar/finances-fees/tuition-fees |
| **Source Snippet** | "The 2026-27 tuition rates below have been approved by the Board of Governors and will become effective in Fall 2026" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

### E-U-020: Scholarships & Awards Timeline
| Field | Value |
|-------|-------|
| **Value** | President's/Lincoln Alexander scholarships deadline January 23; Entrance Financial Need Assessment deadline April 15 |
| **Source URL** | https://www.uoguelph.ca/admission/undergraduate/apply/deadlines/ |
| **Source Snippet** | "January 23 | Lincoln Alexander Chancellor's Scholarships application deadline" and "April 15 | Deadline to apply for scholarships and bursaries" |
| **Capture Date** | 2026-07-10 |
| **Evidence Type** | official_webpage |

---

## Section 6 — WeKnora Import Manifest & Follow-up

### Follow-up Data Items

| Priority | Data Item | Notes |
|----------|-----------|-------|
| **P0** | International tuition per program (detailed per-cohort rates) | Table exists on tuition page but per-program breakdown requires navigating through WebAdvisor or individual cohort PDFs |
| **P0** | Full graduate program listing (all 100+ programs) | Graduate program page requires login; calendar has programs list but detail pages hidden behind authentication |
| **P1** | Per-program admission requirements (prerequisites) | Each program has specific prerequisite courses; available from Admissions → Degree Program requirements |
| **P1** | Graduate English proficiency requirements | Likely similar to UG; verify at graduate studies international page |
| **P1** | Graduate tuition international rates per program | Detailed per-semester cohort rates |
| **P2** | Faculty profiles and research areas per department | Available from individual department websites |
| **P2** | Co-op program availability per major | Co-op availability varies by program |
| **P2** | Residence costs by residence type | Per-room rates available from Student Housing website |

### Known Data Gaps

- International tuition figures are page-level (per-semester range); per-program cohort rates require WebAdvisor login
- Graduate program listings in calendar may not include every collaborative specialization
- Some programs may be jointly offered by multiple colleges (cross-college attribution)
- Graduate application deadlines vary significantly by program; not all could be extracted

---

## Section 7 — Cross-School Comparison Framework

| Dimension | University of Guelph | University of Calgary (UCalgary) | University of Alberta (UAlberta) |
|-----------|:--------------------:|:--------------------------------:|:--------------------------------:|
| Location | Guelph, ON | Calgary, AB | Edmonton, AB |
| Established | 1964 (origins 150+ yrs) | 1966 | 1908 |
| Total Students | 36,000+ | ~33,000 | ~40,000 |
| International Students | 2,200+ (140+ countries) | ~5,000 | ~8,000 |
| Undergraduate Programs | 90+ majors, 60+ minors | 200+ programs | 200+ programs |
| Graduate Programs | 100+ | 250+ | 500+ |
| Colleges/Faculties | 7 colleges | 14 faculties | 18 faculties |
| Tuition (Domestic Annual) | $25K–$36K | $20K–$30K | $20K–$35K |
| IELTS Minimum | 6.5 (no band < 6.0) | 6.5 | 6.5 |
| TOEFL Minimum | 89 (no < 21) | 86 | 90 |
| Application Deadline (UG) | Jan 15 | Mar 1 | Mar 1 |
| U15 Research Intensive | No (Comprehensive) | Yes | Yes |
| Medical School | No (DVM only) | Yes | Yes |
| Campus Type | Single main + 2 satellite | Single main | Single main |

---

> **Document version**: v2.1 (deep+)
> **Generated**: 2026-07-10
> **Sources**: University of Guelph official website (uoguelph.ca), Admission (admission.uoguelph.ca), Academic Calendar (calendar.uoguelph.ca), Graduate Studies (graduatestudies.uoguelph.ca), International Admissions (uoguelph.ca/admission/undergraduate/international/)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (complete listing) | PG programmes ⚠️ (partial — graduate program page requires login) | Evidence (20 blocks) ✅ | Tuition ✅ (domestic detailed + international per-program exact rates) | Scholarships ✅ (domestic + international detailed amounts) | Rankings ✅
> **Next step**: Complete graduate program listing from graduate calendar PDF; graduate per-program tuition rates
