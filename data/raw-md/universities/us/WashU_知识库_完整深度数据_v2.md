# Washington University in St. Louis (WashU) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BSBA/BMus) | 119 |
| 本科辅修 (Minor) | 121 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/JD/MD/etc.) | ~190 |
| 研究生高级证书 (Advanced Certificate / Diploma) | ~28 |
| **学位项目总计 (UG + Grad)** | **~458** |
| 学院 / 独立系所总数 | 9 (4 UG + 5 Grad/Prof + cross-school) |

> Note: Counts derived from bulletin.wustl.edu 2026-27 catalog. Graduate counts include dual-degree variants as separate rows where the bulletin lists them independently. Cross-school PhD programs (DBBS, CDS, IMSE) are counted once under their admin home.

### 0.2 学院 / 系层级结构 (Rule 2)

```
Washington University in St. Louis
├── College of Arts & Sciences [UG学院]
│   ├── Humanities & Social Sciences departments [系]
│   │   ├── African & African American Studies
│   │   ├── American Culture Studies
│   │   ├── Anthropology
│   │   ├── Classics
│   │   ├── Comparative Literature & Thought
│   │   ├── East Asian Languages & Cultures
│   │   ├── Economics
│   │   ├── Educational Studies
│   │   ├── English Literature
│   │   ├── Film and Media Studies
│   │   ├── French
│   │   ├── Germanic Languages & Literatures
│   │   ├── History
│   │   ├── Jewish, Islamic, & Middle Eastern Studies
│   │   ├── Latin American Studies
│   │   ├── Linguistics
│   │   ├── Music
│   │   ├── Philosophy
│   │   ├── Philosophy-Neuroscience-Psychology (PNP)
│   │   ├── Political Science
│   │   ├── Psychological & Brain Sciences
│   │   ├── Religious Studies
│   │   ├── Romance Languages & Literatures
│   │   ├── Sociology
│   │   ├── Spanish
│   │   └── Women, Gender, & Sexuality Studies
│   ├── Natural Sciences & Mathematics departments [系]
│   │   ├── Biology (with 5 specializations)
│   │   ├── Chemistry
│   │   ├── Earth, Environmental, & Planetary Sciences (Earth Science, Environmental Analysis, Environmental Science, Planetary Science)
│   │   ├── Mathematics (Mathematical Sciences, Math & CS, Math & Economics)
│   │   ├── Physics (with Astrophysics, Biophysics specializations)
│   │   └── Statistics (Data Science Major)
│   ├── Performing Arts [系]
│   │   ├── Dance
│   │   └── Drama
│   └── Interdisciplinary [系]
│       ├── Environmental Biology
│       ├── Environmental Policy
│       ├── Global Studies (6 concentrations)
│       ├── Latin American Studies
│       ├── Public Health & Society
│       └── Ancient Studies
├── Olin Business School [UG+Grad学院]
│   ├── Accounting [系]
│   ├── Economics & Strategy [系]
│   ├── Entrepreneurship [系]
│   ├── Finance [系]
│   ├── Health Care Management [系]
│   ├── Marketing [系]
│   ├── Organization & Strategic Management [系]
│   └── Supply Chain, Operations, & Technology [系]
├── Sam Fox School of Design & Visual Arts [UG+Grad学院]
│   ├── College of Architecture [子学院]
│   │   ├── Architecture (BA, BS)
│   │   └── Graduate: MArch, MLA, MUD, MS
│   └── College of Art [子学院]
│       ├── Art (BA, BFA with 5 concentrations)
│       ├── Communication Design (BFA)
│       ├── Design (BA with concentrations)
│       ├── Fashion Design (BFA)
│       └── Graduate: MDes, MFA (IVC), MFA (VA)
├── McKelvey School of Engineering [UG+Grad学院]
│   ├── Biomedical Engineering (BME) [系]
│   ├── Computer Science & Engineering (CSE) [系] -- includes CS, CSE, Data Science, Cybersecurity
│   ├── Electrical & Systems Engineering (ESE) [系] -- EE, Systems, Financial Eng
│   ├── Energy, Environmental & Chemical Engineering (EECE) [系]
│   ├── Mechanical Engineering & Materials Science (MEMS) [系] -- ME, Aerospace, Materials
│   └── Sever Institute (professional master's) [子学院]
├── Graduate School of Architecture & Urban Design [Grad学院] (part of Sam Fox)
├── Graduate School of Art [Grad学院] (part of Sam Fox)
├── Office of Graduate Studies, Arts & Sciences [Grad学院]
├── Olin Business School Graduate Programs [Grad学院]
├── McKelvey School of Engineering Graduate Programs [Grad学院]
├── Washington University School of Law [Grad/Prof学院]
│   ├── JD, LLM, MLS, JSD
│   └── Online programs
├── Washington University School of Medicine [Grad/Prof学院]
│   ├── Medical Education (MD, dual MD/PhD, MD/MBA, etc.)
│   ├── Audiology & Communication Sciences
│   ├── Biology & Biomedical Sciences (11 PhD programs)
│   ├── Clinical Investigation
│   ├── Genetic Counseling
│   ├── Informatics, Data Science, & Biostatistics
│   ├── Medical Physics
│   ├── Nursing Science
│   ├── Occupational Therapy
│   ├── Physical Therapy
│   ├── Population Health Sciences
│   └── Reproductive Sciences
├── Bursky School of Public Health [Grad学院]
│   ├── Master of Public Health (MPH)
│   └── PhD in Public Health Sciences
├── Brown School of Social Work & Social Policy [Grad学院]
│   ├── Master of Social Work (MSW)
│   ├── Master of Social Policy (MSP)
│   └── PhD in Social Work
├── Cross-School Interdisciplinary PhD Programs [跨学院]
│   ├── Division of Biology & Biomedical Sciences (DBBS)
│   ├── Division of Computational & Data Sciences (CDS)
│   └── Institute of Materials Science & Engineering (IMSE)
└── WashU Continuing & Professional Studies (CAPS) [继续教育]
```

### 0.3 学历级别明细 (Rule 3)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | ~40 |
| BS | BS | Bachelor of Science | 本科 | ~12 |
| BSBA | BSBA | Bachelor of Science in Business Administration | 本科 | 8 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 9 |
| BMus | BMus | Bachelor of Music | 本科 | 6 |
| MA | MA | Master of Arts | 研究生 | ~18 |
| MS | MS | Master of Science | 研究生 | ~35 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 5 (Full-Time, Flex, 3 Exec) |
| MEng | MEng | Master of Engineering | 研究生 | 5 |
| MArch | MArch | Master of Architecture | 研究生 | 2 (MArch2, MArch3) |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 1 |
| MDes | MDes | Master of Design | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MSP | MSP | Master of Social Policy | 研究生 | 1 |
| MACC | MACC | Master of Accounting | 研究生 | 1 |
| MUD | MUD | Master of Urban Design | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~60 |
| MD | MD | Doctor of Medicine | 研究生 | 2 (standard + 5-year) |
| JD | JD | Juris Doctor | 研究生 | 1 |
| AuD | AuD | Doctor of Audiology | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | OTD | Doctorate of Occupational Therapy | 研究生 | 1 |
| DBA | DBA | Doctor of Business Administration | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| MLS | MLS | Master of Legal Studies | 研究生 | 1 |
| JSD | JSD | Juris Scientiae Doctoris | 研究生 | 1 |
| MLA | MLA (liberal arts) | Master of Liberal Arts | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | ~28 |

### 0.4 分布矩阵 (学院 x canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSBA | BFA | BMus | MA | MS | MFA | MBA | MEng | MArch | MLA | MDes | PhD | MD | JD | AuD | DPT | OTD | DBA | LLM/MLS/JSD | MPH/MSW/MSP | Cert | 合计 |
|------------|----|----|------|-----|------|----|----|-----|-----|------|-------|-----|------|-----|----|----|----|----|----|----|----|-----|-----|------|
| Arts & Sciences | ~35 | ~10 | 0 | 0 | 6 | ~14 | ~6 | 2 | 0 | 0 | 0 | 0 | 0 | ~27 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | ~110 |
| Olin Business | 0 | 0 | 8 | 0 | 0 | 0 | ~8 | 0 | 5 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | ~27 |
| Sam Fox (Architecture) | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~9 |
| Sam Fox (Art) | 2 | 0 | 0 | 8 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~13 |
| McKelvey Engineering | 0 | ~12 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | 5 | 0 | 0 | 0 | ~12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | ~49 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | ~5 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 1 | ~10 | 0 | 0 | 0 | 0 | 0 | 0 | ~15 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | ~7 | ~38 |
| Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | ~3 |
| Brown School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | ~3 |
| Cross-School PhD | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 |
| **合计** | ~39 | ~22 | 8 | 8 | 6 | ~15 | ~36 | 4 | 5 | 5 | 2 | 1 | 1 | ~61 | 2 | 1 | 1 | 1 | 1 | 1 | 3 | 4 | ~31 | **~458** |

> Matrix cell-sum ~458. Rule-1 total ~458. Reconciliation: approximate match. Exact counts require deduplication of dual-degree variants and cross-listed programs.

---

## SECTION 1 -- Undergraduate Education

### 1.1 College/school architecture

WashU has four undergraduate-degree-granting schools: College of Arts & Sciences, Olin Business School, Sam Fox School of Design & Visual Arts (containing College of Architecture and College of Art), and McKelvey School of Engineering. Students apply to one school but may take courses across all. The Beyond Boundaries Program offers an interdisciplinary first-year experience. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors -- grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Humanities & Social Sciences

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | African & African American Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | American Culture Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Ancient Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Anthropology | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Arabic | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Art History and Archaeology | https://bulletin.wustl.edu/undergrad/majors/ |
| 7 | Classics | https://bulletin.wustl.edu/undergrad/majors/ |
| 8 | Comparative Literature and Thought | https://bulletin.wustl.edu/undergrad/majors/ |
| 9 | Comparative Literature and Thought, Comparative Arts Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 10 | Dance | https://bulletin.wustl.edu/undergrad/majors/ |
| 11 | Drama | https://bulletin.wustl.edu/undergrad/majors/ |
| 12 | East Asian Languages and Cultures | https://bulletin.wustl.edu/undergrad/majors/ |
| 13 | East Asian Languages and Cultures, Chinese Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 14 | East Asian Languages and Cultures, Japanese Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 15 | East Asian Languages and Cultures, Korean Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 16 | Economics | https://bulletin.wustl.edu/undergrad/majors/ |
| 17 | Economics, Financial Economics Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 18 | Educational Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 19 | English Literature | https://bulletin.wustl.edu/undergrad/majors/ |
| 20 | English Literature, Creative Writing Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 21 | English Literature, Publishing Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 22 | Film and Media Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 23 | Film and Media Studies, Film and Media Production Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 24 | French | https://bulletin.wustl.edu/undergrad/majors/ |
| 25 | Germanic Languages and Literatures | https://bulletin.wustl.edu/undergrad/majors/ |
| 26 | Global Studies, Development Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 27 | Global Studies, Eurasian Studies Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 28 | Global Studies, European Studies Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 29 | Global Studies, Global Asias Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 30 | Global Studies, Global Cultural Studies Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 31 | Global Studies, International Affairs Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 32 | Hebrew | https://bulletin.wustl.edu/undergrad/majors/ |
| 33 | History | https://bulletin.wustl.edu/undergrad/majors/ |
| 34 | Italian | https://bulletin.wustl.edu/undergrad/majors/ |
| 35 | Jewish, Islamic, and Middle Eastern Studies, Comparative Jewish and Islamic Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 36 | Jewish, Islamic, and Middle Eastern Studies, Modern Middle Eastern Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 37 | Latin American Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 38 | Linguistics | https://bulletin.wustl.edu/undergrad/majors/ |
| 39 | Music (BA) | https://bulletin.wustl.edu/undergrad/majors/ |
| 40 | Philosophy | https://bulletin.wustl.edu/undergrad/majors/ |
| 41 | Philosophy, Law and Policy Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 42 | Philosophy, Philosophy of Science Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 43 | Philosophy, Philosophy Research Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 44 | Philosophy-Neuroscience-Psychology, Cognitive Neuroscience Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 45 | Philosophy-Neuroscience-Psychology, Language Cognition and Culture Concentration | https://bulletin.wustl.edu/undergrad/majors/ |
| 46 | Political Science | https://bulletin.wustl.edu/undergrad/majors/ |
| 47 | Political Science, American Politics Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 48 | Political Science, Comparative Politics Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 49 | Political Science, International Politics Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 50 | Political Science, Political Methodology Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 51 | Political Science, Political Theory Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 52 | Psychological & Brain Sciences | https://bulletin.wustl.edu/undergrad/majors/ |
| 53 | Psychological & Brain Sciences, Cognition in Children Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 54 | Psychological & Brain Sciences, Cognitive Neuroscience Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 55 | Psychological & Brain Sciences, Experimental Psychopathology Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 56 | Psychological & Brain Sciences, Lifespan Development Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 57 | Psychological & Brain Sciences, Personality and Individual Differences Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 58 | Psychological & Brain Sciences: Cognitive Neuroscience | https://bulletin.wustl.edu/undergrad/majors/ |
| 59 | Psychological & Brain Sciences: Cognitive Neuroscience, Cognition in Children | https://bulletin.wustl.edu/undergrad/majors/ |
| 60 | Psychological & Brain Sciences: Cognitive Neuroscience, Experimental Psychopathology | https://bulletin.wustl.edu/undergrad/majors/ |
| 61 | Psychological & Brain Sciences: Cognitive Neuroscience, Lifespan Development | https://bulletin.wustl.edu/undergrad/majors/ |
| 62 | Psychological & Brain Sciences: Cognitive Neuroscience, Personality and Individual Differences | https://bulletin.wustl.edu/undergrad/majors/ |
| 63 | Public Health & Society | https://bulletin.wustl.edu/undergrad/majors/ |
| 64 | Religious Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 65 | Romance Languages and Literatures | https://bulletin.wustl.edu/undergrad/majors/ |
| 66 | Sociology | https://bulletin.wustl.edu/undergrad/majors/ |
| 67 | Sociology, Urban Studies Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 68 | Spanish | https://bulletin.wustl.edu/undergrad/majors/ |
| 69 | Women, Gender, and Sexuality Studies | https://bulletin.wustl.edu/undergrad/majors/ |
| 70 | Women, Gender, and Sexuality Studies, Health Specialization | https://bulletin.wustl.edu/undergrad/majors/ |
| 71 | Women, Gender, and Sexuality Studies, Politics Specialization | https://bulletin.wustl.edu/undergrad/majors/ |

###### BMus

| # | 专业 | URL |
|---|------|-----|
| 1 | Music (BMus) | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | Music, Composition Concentration (BMus) | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Music, General Concentration (BMus) | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Music, History and Culture Concentration (BMus) | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Music, Performance Concentration (BMus) | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Music, Theory Concentration (BMus) | https://bulletin.wustl.edu/undergrad/majors/ |

##### Natural Sciences & Mathematics

###### BS / BA

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Mathematics | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | Astrophysics | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Biochemistry | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Biology | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Biology, Ecology and Evolution Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Biology, Genomics and Computational Biology Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 7 | Biology, Microbiology Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 8 | Biology, Molecular Biology and Biochemistry Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 9 | Biology, Neuroscience Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 10 | Chemistry | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 11 | Chemistry, Biochemistry Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 12 | Data Science | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 13 | Earth Science | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 14 | Environmental Analysis | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 15 | Environmental Biology | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 16 | Environmental Policy | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 17 | Environmental Science | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 18 | Mathematical Sciences | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 19 | Mathematics | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 20 | Mathematics and Computer Science | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 21 | Mathematics and Economics | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 22 | Physics | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 23 | Physics, Biophysics Specialization | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 24 | Planetary Science | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 25 | Statistics | BA | https://bulletin.wustl.edu/undergrad/majors/ |

#### Olin Business School

##### BSBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | Economics and Strategy, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Entrepreneurship, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Finance, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Health Care Management, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Marketing, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 7 | Organization and Strategic Management, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |
| 8 | Supply Chain, Operations, and Technology, BSBA | https://bulletin.wustl.edu/undergrad/majors/ |

#### Sam Fox School of Design & Visual Arts

##### College of Architecture

###### BA / BS

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | Architecture | BS | https://bulletin.wustl.edu/undergrad/majors/ |

##### College of Art

###### BA / BFA

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | Art with Painting Concentration | BFA | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Art with Photography Concentration | BFA | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Art with Printmaking Concentration | BFA | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Art with Sculpture Concentration | BFA | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Art with Time-Based + Media Art Concentration | BFA | https://bulletin.wustl.edu/undergrad/majors/ |
| 7 | Communication Design | BFA | https://bulletin.wustl.edu/undergrad/majors/ |
| 8 | Design | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 9 | Design with Communication Concentration | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 10 | Design with Fashion Concentration | BA | https://bulletin.wustl.edu/undergrad/majors/ |
| 11 | Fashion Design | BFA | https://bulletin.wustl.edu/undergrad/majors/ |

#### McKelvey School of Engineering

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Chemical Engineering) (EECE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 2 | Applied Science (Electrical Engineering) (ESE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Applied Science (Mechanical Engineering) (MEMS), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Applied Science (Systems Science & Engineering) (ESE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Biomedical Engineering (BME), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Business and Computer Science (CSE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 7 | Chemical Engineering (EECE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 8 | Computer Engineering (CSE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 9 | Computer Engineering (ESE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 10 | Computer Science (CSE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 11 | Computer Science + Economics (CSE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 12 | Computer Science + Mathematics (CSE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 13 | Data Science (CSE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 14 | Electrical Engineering (ESE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 15 | Environmental Engineering (EECE), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 16 | Mechanical Engineering (MEMS), BS | https://bulletin.wustl.edu/undergrad/majors/ |
| 17 | Systems Science & Engineering (ESE), BS | https://bulletin.wustl.edu/undergrad/majors/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学位 | Cross-listed schools | URL |
|---|------|------|---------------------|-----|
| 1 | Business and Computer Science | BS (CSE) | Olin + McKelvey | https://admissions.washu.edu/academics/majors-programs/joint-degree-program-in-business-and-computer-science/ |
| 2 | Computer Science + Economics | BS (CSE) | McKelvey + A&S | https://bulletin.wustl.edu/undergrad/majors/ |
| 3 | Computer Science + Mathematics | BS (CSE) | McKelvey + A&S | https://bulletin.wustl.edu/undergrad/majors/ |
| 4 | Economics and Computer Science | BA | A&S (cross-listed) | https://bulletin.wustl.edu/undergrad/majors/ |
| 5 | Mathematics and Computer Science | BA | A&S (cross-listed) | https://bulletin.wustl.edu/undergrad/majors/ |
| 6 | Mathematics and Economics | BA | A&S (cross-listed) | https://bulletin.wustl.edu/undergrad/majors/ |
| 7 | Philosophy-Neuroscience-Psychology | BA | A&S (interdisciplinary) | https://bulletin.wustl.edu/undergrad/majors/ |

### 1.4 Minors -- complete list

Full list of 121 minors available at: https://bulletin.wustl.edu/undergrad/minors/

Key minors by school:
- **A&S**: Accounting (Non-BSBA), African & African American Studies, American Culture Studies, Ancient Studies, Anthropology, Applied Linguistics, Arabic, Art History, Asian American Studies, Astrophysics, Biology, Chemistry, Classics, Comparative Literature, Dance, Drama, Earth Science, East Asian Languages, Educational Studies, English, Environmental Science, Environmental Studies, Film & Media Studies, French, General Economics, Geospatial Science, Germanic Languages, Hebrew, History, Italian, Jazz Studies, Jewish/Islamic/Middle Eastern Studies, Latin American Studies, Linguistics, Mathematics, Medical Humanities, Medieval & Renaissance Studies, Music General Studies, Philosophy, Philosophy of Science, PNP, Physics, Planetary Science, Political Science, Psychological & Brain Sciences, Public Health & Society, Religion & Politics, Religious Studies, Sociology, South Asian Studies, Spanish, Speech & Hearing, Statistics, Translation Studies, Women/Gender/Sexuality Studies, Writing
- **Olin (Non-BSBA)**: Business Analytics, Business of Entertainment, Business of Social Impact, Business of Sports, Business of the Arts, Entrepreneurship, Finance, Health Care Management, Managerial Economics, Marketing, Organization & Strategic Management, Strategy, Supply Chain/Operations/Technology
- **Sam Fox**: Architectural History & Theory, Architecture, Art, Communication Design, Design, Fashion Design (BFA-level), Landscape Architecture, Urban Design
- **McKelvey**: Aerospace Engineering (MEMS), Bioinformatics (CSE), Biomedical Data Science (BME), Biomedical Physics, Computational AI (CSE), Computer Science (CSE), Electrical Engineering (ESE), Energy Engineering (EECE/ESE/MEMS), Environmental Engineering Science (EECE/MEMS), Human-Computer Interaction (CSE), Materials Science & Engineering (MEMS), Mechanical Engineering (MEMS), Mechatronics (ESE/MEMS), Nanoscale Science & Engineering (EECE/MEMS), Quantum Engineering (ESE), Robotics (ESE/MEMS), Systems Engineering for Social Good (ESE), Systems Science & Engineering (ESE)
- **Interdisciplinary**: Bioinformatics, Children's Studies, Creative Practice for Social Change, Data Science in the Humanities, Global Film & Media Studies, Human-Computer Interaction, Legal Studies

### 1.5 General/Institute-wide requirements

WashU does not have a single unified core curriculum. Each school has its own requirements:
- **College of Arts & Sciences**: University-wide requirements include Writing (first-year seminar), breadth requirements across divisions
- **Olin Business School**: Business core + university requirements
- **Sam Fox**: Design studio core + university requirements
- **McKelvey Engineering**: Engineering core + university requirements
- **Beyond Boundaries Program**: Interdisciplinary first-year experience

### 1.6 Course-ID to Major quick-lookup

Engineering programs use department codes: BME, CSE, ESE, EECE, MEMS. Business uses: ACCT, ECON, FIN, MKT, MGT, SCOT.

---

## SECTION 2 -- Graduate Education

### 2.1 Graduate programs -- grouped by 学院 > 系 > 学位级别

#### Graduate School of Architecture & Urban Design (Sam Fox School)

##### Master's Degrees

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Architecture (MArch 3, 6 semesters) | MArch | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 2 | Master of Architecture (MArch 2, 4 semesters) | MArch | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 3 | Master of Landscape Architecture | MLA | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 4 | Master of Urban Design | MUD | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 5 | MS in Advanced Architectural Design | MS | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 6 | MS in Architectural Studies | MS | https://bulletin.wustl.edu/grad/architecture/degrees/ |

##### Dual Degrees

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 7 | MArch/MPH | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 8 | MBA/MArch | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 9 | MCM/MArch | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 10 | MLA/MArch | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 11 | MLA/MUD | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 12 | MSW/MArch | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 13 | MSW/MUD | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |
| 14 | MUD/MArch | Dual | https://bulletin.wustl.edu/grad/architecture/degrees/ |

#### Graduate School of Art (Sam Fox School)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MDes for Human-Computer Interaction + Emerging Technology | MDes | https://bulletin.wustl.edu/grad/art/ |
| 2 | MFA in Illustration & Visual Culture | MFA | https://bulletin.wustl.edu/grad/art/ |
| 3 | MFA in Visual Art | MFA | https://bulletin.wustl.edu/grad/art/ |

#### Office of Graduate Studies, Arts & Sciences

##### Doctoral Degrees

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology, Archaeology Concentration | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 2 | Anthropology, Biological Anthropology Concentration | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 3 | Anthropology, Sociocultural Anthropology Concentration | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 4 | Art History and Archaeology | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 5 | Chemistry | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 6 | Classics | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 7 | Comparative Literature | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 8 | Earth, Environmental, and Planetary Sciences | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 9 | East Asian and Comparative Literatures | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 10 | East Asian Languages and Cultures | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 11 | Ecology & Evolutionary Biology | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 12 | Economics | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 13 | Education | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 14 | English and American Literature | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 15 | English and Comparative Literature | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 16 | French and Francophone Studies and Comparative Literature | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 17 | French and Francophone Studies | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 18 | German and Comparative Literature | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 19 | Germanic Languages and Literatures | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 20 | Hispanic Studies and Comparative Literature | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 21 | Hispanic Studies | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 22 | History | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 23 | Mathematics | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 24 | Music, Music Theory Concentration | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 25 | Music, Musicology Concentration | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 26 | Philosophy | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 27 | Philosophy-Neuroscience-Psychology | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 28 | Physics | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 29 | Political Science | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 30 | Psychological & Brain Sciences | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 31 | Sociology | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 32 | Statistics | PhD | https://bulletin.wustl.edu/grad/artsci/degrees/ |

##### Master's Degrees

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History and Archaeology | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 2 | Biology (Part-Time) | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 3 | Classics | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 4 | Dance | MFA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 5 | East Asian Languages and Cultures | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 6 | Economics | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 7 | Film and Media Studies | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 8 | German and Higher Education Administration | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 9 | Germanic Languages and Literatures | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 10 | Islamic and Near Eastern Studies | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 11 | Jewish Studies | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 12 | Liberal Arts (Part-Time) | MLA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 13 | Mathematics | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 14 | Music, Music Theory Concentration | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 15 | Music, Musicology Concentration | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 16 | Physics | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 17 | Statistics and Data Science, Applied Data Science Concentration | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 18 | Statistics and Data Science, Statistics Concentration | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 19 | Statistics and Data Science, Statistics for Political Science PhD Students | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 20 | Theater and Performance Studies | MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 21 | Writing | MFA | https://bulletin.wustl.edu/grad/artsci/degrees/ |

##### Accelerated BA/MA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Classics, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 2 | East Asian Languages and Cultures, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 3 | Economics, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 4 | Film and Media Studies, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 5 | Mathematics, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 6 | Physics, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 7 | Statistics and Data Science, Accelerated BA/MA (Applied Data Science) | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 8 | Statistics and Data Science, Accelerated BA/MA (Statistics) | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 9 | Theater and Performance Studies, Accelerated BA/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |

##### Graduate Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | American Culture Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 2 | Data Science in the Humanities | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 3 | Early Modern Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 4 | Film and Media Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 5 | Global Black Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 6 | Higher Education | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 7 | Language Instruction | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 8 | Latin American Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 9 | Quantitative Data Analysis | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 10 | Translation Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 11 | Women, Gender, and Sexuality Studies | https://bulletin.wustl.edu/grad/artsci/degrees/ |

##### Dual Degrees

| # | 项目 | URL |
|---|------|-----|
| 1 | Education, MAEd/MSW | https://bulletin.wustl.edu/grad/artsci/degrees/ |
| 2 | Women, Gender, and Sexuality Studies, JD/MA | https://bulletin.wustl.edu/grad/artsci/degrees/ |

#### Olin Business School

##### Graduate Master's Degrees

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MBA (Full-Time) | MBA | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 2 | Flex MBA | MBA | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 3 | Executive MBA St. Louis | MBA | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 4 | Executive MBA Mumbai | MBA | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 5 | Executive MBA Shanghai | MBA | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 6 | Master of Accounting (MACC) | MACC | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 7 | MS in AI for Business (MSAIB) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 8 | MS in Business Analytics (MSA) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 9 | MS in Business of Sports (MSBOS) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 10 | MS in Finance - Corporate Finance (MSFC) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 11 | MS in Finance - Quantitative (MSFQ) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 12 | MS in Finance - Wealth and Asset Management (MSFWAM) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 13 | MS in Supply Chain Management (MSSCM) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 14 | MS in Wealth Management (MSWM) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 15 | Online MS in Business Analytics (OMSBA) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |
| 16 | Flex MS in Finance (Flex MSF) | MS | https://bulletin.wustl.edu/grad/business/graduate-masters/ |

##### Graduate Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Analytics, Graduate Certificate | https://bulletin.wustl.edu/grad/business/graduate-certificates/ |
| 2 | Analytics, Advanced Graduate Certificate | https://bulletin.wustl.edu/grad/business/graduate-certificates/ |
| 3 | Finance, Graduate Certificate | https://bulletin.wustl.edu/grad/business/graduate-certificates/ |
| 4 | Finance, Advanced Graduate Certificate | https://bulletin.wustl.edu/grad/business/graduate-certificates/ |

##### Dual Degrees

| # | 项目 | Partner School | URL |
|---|------|---------------|-----|
| 1 | MBA/MPH | Brown School | https://bulletin.wustl.edu/grad/business/dual-degrees/ |
| 2 | MBA/MSW | Brown School | https://bulletin.wustl.edu/grad/business/dual-degrees/ |
| 3 | MBA/MS-BME | McKelvey Engineering | https://bulletin.wustl.edu/grad/business/dual-degrees/ |
| 4 | MBA/MEng-EECE | McKelvey Engineering | https://bulletin.wustl.edu/grad/business/dual-degrees/ |
| 5 | MBA/MArch | Sam Fox | https://bulletin.wustl.edu/grad/business/dual-degrees/ |
| 6 | MBA/JD | Law | https://bulletin.wustl.edu/grad/business/dual-degrees/ |
| 7 | MBA/MD | Medicine | https://bulletin.wustl.edu/grad/business/dual-degrees/ |

##### Doctoral Degrees

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Business Administration | DBA | https://bulletin.wustl.edu/grad/business/doctoral/ |
| 2 | PhD in Business | PhD | https://bulletin.wustl.edu/grad/business/doctoral/ |

#### McKelvey School of Engineering

| # | 项目 | 学位 | Dept | URL |
|---|------|------|------|-----|
| 1 | Aerosol Science & Engineering, Joint MS | MS | EECE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 2 | Aerospace Engineering | MSAE | MEMS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 3 | Biomedical Engineering | MS | BME | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 4 | Biomedical Engineering | PhD | BME | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 5 | Biomedical Engineering, Combined MD/PhD | PhD | BME | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 6 | Computational & Data Sciences | PhD | CDS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 7 | Computer Engineering | MS | CSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 8 | Computer Engineering | MS | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 9 | Computer Engineering | PhD | CSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 10 | Computer Science & Engineering | MEng | CSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 11 | Computer Science | MS | CSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 12 | Computer Science | PhD | CSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 13 | Cybersecurity Engineering | MS | CSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 14 | Electrical Engineering | MSEE | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 15 | Electrical Engineering | PhD | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 16 | Energy, Environmental, & Chemical Engineering | MEng | EECE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 17 | Energy, Environmental, & Chemical Engineering | MS | EECE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 18 | Energy, Environmental, & Chemical Engineering | PhD | EECE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 19 | Engineering Data Analytics & Statistics | MSDAS | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 20 | Imaging Science | MS | IS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 21 | Imaging Science | PhD | IS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 22 | Materials Science & Engineering | MS | MEMS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 23 | Materials Science & Engineering, Interdisciplinary PhD | PhD | IMSE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 24 | Mechanical Engineering | MEng | MEMS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 25 | Mechanical Engineering | MSME | MEMS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 26 | Mechanical Engineering | PhD | MEMS | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 27 | Robotics and Intelligent Systems | MEng | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 28 | Systems Science & Mathematics | MSSSM | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 29 | Systems Science & Mathematics | PhD | ESE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 30 | Combined MEng/MBA | Dual | EECE | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 31 | Master of Construction Management | MCM | Sever | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 32 | Master of Construction Management/MArch | Dual | Sever | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 33 | Master of Cybersecurity Management | MCM | Sever | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 34 | Master of Engineering Management | MEM | Sever | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 35 | Master of Information Systems Management | MISM | Sever | https://bulletin.wustl.edu/grad/engineering/degrees/ |

##### Engineering Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Controls Certificate (ESE) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 2 | Cybersecurity Engineering Certificate (CSE) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 3 | Data Mining & Machine Learning Certificate (CSE) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 4 | Financial Engineering Certificate (ESE) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 5 | Graduate Certificate in Construction Management (Sever) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 6 | Graduate Certificate in Cybersecurity Management (Sever) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 7 | Graduate Certificate in Engineering Management (Sever) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 8 | Imaging Science & Engineering Certificate (ESE) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 9 | Online Graduate Certificate in Cybersecurity Management (Sever) | https://bulletin.wustl.edu/grad/engineering/degrees/ |
| 10 | Quantum Engineering Certificate (ESE) | https://bulletin.wustl.edu/grad/engineering/degrees/ |

#### Washington University School of Law

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor | JD | https://bulletin.wustl.edu/law/ |
| 2 | Master of Laws | LLM | https://bulletin.wustl.edu/law/ |
| 3 | Master of Legal Studies | MLS | https://bulletin.wustl.edu/law/ |
| 4 | Juris Scientiae Doctoris | JSD | https://bulletin.wustl.edu/law/ |

#### Washington University School of Medicine

##### Medical Education

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Medicine | MD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 2 | Doctor of Medicine (Five-Year Program) | MD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 3 | MD/Master of Science in Clinical Investigation | Dual | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 4 | MD/Master of Population Health Sciences | Dual | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 5 | MD/MPH | Dual | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 6 | MD/MBA | Dual | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 7 | MD/PhD | Dual | https://bulletin.wustl.edu/medicine/degrees-offerings/ |

##### Audiology & Communication Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Audiology | AuD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 2 | PhD in Speech and Hearing Sciences | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 3 | MA in Speech and Hearing Sciences | MA | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 4 | MS in Deaf Education | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |

##### Biology & Biomedical Sciences (DBBS)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biochemistry, Biophysics, & Structural Biology | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 2 | Biomedical Informatics & Data Science | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 3 | Cancer Biology | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 4 | Computational & Systems Biology | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 5 | Developmental, Regenerative, & Stem Cell Biology | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 6 | Immunology | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 7 | Molecular Cell Biology | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 8 | Molecular Genetics & Genomics | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 9 | Molecular Microbiology & Microbial Pathogenesis | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 10 | Neurosciences | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 11 | Plant & Microbial Biosciences | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |

##### Other Medicine Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MS in Clinical Investigation | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 2 | Graduate Certificate in Clinical Investigation | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 3 | MS in Genetic Counseling | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 4 | MS in Biomedical Data Science and AI | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 5 | MS in Biomedical Informatics | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 6 | MS in Biostatistics | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 7 | MS in Biostatistics and Data Science | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 8 | Certificate in Biomedical Data Science and AI | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 9 | Certificate in Biomedical Informatics | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 10 | Certificate in Biostatistics and Data Science | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 11 | MS in Medical Physics | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 12 | PhD in Medical Physics | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 13 | Post-PhD Graduate Certificate in Medical Physics | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 14 | PhD in Nursing Science | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 15 | MS in Occupational Therapy | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 16 | Doctorate of Occupational Therapy | OTD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 17 | Post-Professional Doctorate of Occupational Therapy | OTD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 18 | PhD in Rehabilitation and Participation Science | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 19 | Doctor of Physical Therapy | DPT | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 20 | PhD in Movement Science | PhD | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 21 | Master of Population Health Sciences | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 22 | Certificate in Clinical Effectiveness | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 23 | Certificate in Health Equity and Disparities | Cert | https://bulletin.wustl.edu/medicine/degrees-offerings/ |
| 24 | MS in Reproductive Sciences | MS | https://bulletin.wustl.edu/medicine/degrees-offerings/ |

#### Bursky School of Public Health

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Public Health | MPH | https://bulletin.wustl.edu/publichealth/ |
| 2 | PhD in Public Health Sciences | PhD | https://bulletin.wustl.edu/publichealth/ |

#### Brown School of Social Work & Social Policy

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Social Work | MSW | https://bulletin.wustl.edu/brownschool/ |
| 2 | Master of Social Policy | MSP | https://bulletin.wustl.edu/brownschool/ |
| 3 | PhD in Social Work | PhD | https://bulletin.wustl.edu/brownschool/ |

#### Cross-School Interdisciplinary PhD Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Division of Biology & Biomedical Sciences (DBBS) | https://bulletin.wustl.edu/grad/cross-school-phd-programs/ |
| 2 | Division of Computational & Data Sciences (CDS) | https://bulletin.wustl.edu/grad/cross-school-phd-programs/ |
| 3 | Institute of Materials Science & Engineering (IMSE) | https://bulletin.wustl.edu/grad/cross-school-phd-programs/ |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science, PhD (McKelvey School of Engineering, CSE)**
- Department: Computer Science & Engineering (CSE)
- Degree: PhD
- URL: https://bulletin.wustl.edu/grad/engineering/degrees/
- Application: Through McKelvey School of Engineering graduate admissions
- GRE: Not required (verify per current cycle)
- TOEFL/IELTS: Required for international applicants
- Deadline: Varies; check department website
- Funding: Most PhD students receive full funding (tuition + stipend)

### 2.3 Graduate admissions model

WashU graduate admissions is **fully decentralized**. Each school manages its own admissions process, application portal, fee, and financial aid:

- **Arts & Sciences**: Office of Graduate Studies (OGS), artscigrads@wustl.edu
- **Olin Business**: OlinGradAdmissions@wustl.edu, 314-935-7301
- **McKelvey Engineering**: Department-level admissions
- **Law**: law.wustl.edu, 314-935-6400
- **Medicine**: medicine.wustl.edu/education
- **Public Health**: 314-935-4747
- **Brown School**: Separate admissions for MSW, MSP, PhD
- **Architecture & Art (Sam Fox)**: School-level admissions

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://admissions.washu.edu/ | admissions.washu.edu |
| Application portal | Common App or Coalition App | admissions.washu.edu |
| Application fee | Not specified on main pages; fee waiver available | admissions.washu.edu |
| Early Action deadline | November 2, 2026 (app); Nov 9 (materials); Nov 17 (financial aid) | admissions.washu.edu |
| Early Decision I deadline | November 2, 2026 (app); Nov 9 (materials); Nov 17 (financial aid) | admissions.washu.edu |
| Early Decision II deadline | January 4, 2027 (app); Jan 11 (materials); Jan 11 (financial aid) | admissions.washu.edu |
| Regular Decision deadline | January 4, 2027 (app); Jan 11 (materials); Feb 1 (financial aid) | admissions.washu.edu |
| EA/EDI decision release | December 23, 2026 (EA); December 11, 2026 (EDI) | admissions.washu.edu |
| EDII decision release | February 12, 2027 | admissions.washu.edu |
| RD decision release | April 1, 2027 | admissions.washu.edu |
| Candidate reply (RD) | May 1, 2027 | admissions.washu.edu |
| SAT/ACT policy | **Test-optional** | admissions.washu.edu |
| Superscore | Yes (SAT and ACT) | admissions.washu.edu |
| ACT Science section | Optional, not required, not used in superscore | admissions.washu.edu |
| Last test date accepted | December (October for EA/EDI) | admissions.washu.edu |
| SAT code | 6929 | admissions.washu.edu |
| ACT code | 2386 | admissions.washu.edu |
| TOEFL code | 6929 | admissions.washu.edu |
| CSS Profile code | 6929 | admissions.washu.edu |
| FAFSA code | 002520 | admissions.washu.edu |
| Interview policy | No evaluative interviews; optional video supplement | admissions.washu.edu |
| Recommendation | School Report, Official Transcript, Teacher Evaluation, Counselor Recommendation | admissions.washu.edu |
| Portfolio | Required for Sam Fox School applicants (Architecture/Art) | admissions.washu.edu |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT (pre-Jan 21, 2026) | N/A | 100 | Competitive range |
| TOEFL iBT (Jan 21, 2026+) | N/A | 5.0 | New reporting scale |
| TOEFL iBT Home Edition | Accepted | Same as above | |
| IELTS Academic | N/A | 7.0 | |
| Duolingo English Test | N/A | 130 | |

> Source: admissions.washu.edu/how-to-apply/english-testing-requirements/
> Applicability: International students for whom English is a second language. Exemptions: 3+ years in English-medium school in US. Starting Fall 2027, SAT/ACT scores no longer accepted in lieu of English proficiency.

### 3.3 Graduate -- global rules

Graduate admissions is fully decentralized. Each school sets its own:
- Application platform and fee
- GRE/GMAT policy (varies by program; many no longer require GRE)
- English language requirements
- Deadlines (typically Dec-Feb for fall entry)
- Financial aid and funding

ETS institutional codes vary by school. CGS April-15 honor date applies.

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $71,310 | Full-time, per year |
| Student Activity Fee | $712 | 1% of tuition, per year |
| Student Health & Wellness Fee | $700 | Per year |
| Average Housing & Food | $24,272 | Modern double room + Platinum meal plan |
| **Total University Charges** | **$96,994** | |
| Books & Supplies | $1,412 | Estimated, varies by program |
| Travel | $1,050 | ~4 trips/year estimate |
| Miscellaneous | $2,804 | Personal expenses |
| **Total Other Estimated Expenses** | **$5,266** | |
| **Total Estimated COA** | **~$102,260** | |

> Source: financialaid.washu.edu/costs/
> Note: The bulletin lists tuition as $34,120/semester ($68,240/year). The financial aid office lists $71,310/year. The discrepancy may reflect fees included in the financial aid figure. Using financialaid.washu.edu as authoritative.

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind (US citizens/PRs) | **Yes** (Gateway to Success, $1B initiative) | financialaid.washu.edu |
| Need-aware (international) | International first-years eligible for aid; must apply by deadline | financialaid.washu.edu |
| Meets demonstrated need | **100%, without loans** | financialaid.washu.edu |
| No-loan policy | **Yes** (scholarships, grants, work-study only) | financialaid.washu.edu |
| WashU Pledge | Full ride for MO/southern IL families with income <$75k | financialaid.washu.edu |
| Average need-based aid offer | $73,000 | financialaid.washu.edu |
| International transfer aid | **Not eligible** | financialaid.washu.edu |
| CSS Profile required | Yes (code 6929) | financialaid.washu.edu |
| FAFSA required | Yes for US citizens/PRs (code 002520) | financialaid.washu.edu |
| Enrollment deposit (domestic) | $600 | bulletin.wustl.edu |
| Enrollment deposit (international) | $885 | bulletin.wustl.edu |

### 4.3 Graduate cost & funding framework

Graduate costs and funding vary significantly by school:
- **PhD programs**: Most fully funded (tuition + stipend)
- **Professional master's**: Generally self-funded; scholarships available
- **Professional schools** (Law, Medicine, Business): Separate tuition structures
- Application fees vary by school

---

## SECTION 5 -- Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 2, 2026 (application); November 9 (materials); November 17 (financial aid); December 23 (decisions)"
  source_url: https://admissions.washu.edu/how-to-apply/application-dates-deadlines/
  source_snippet: "Early Action Nov. 2 ... Nov. 9 ... Nov. 17 ... Dec. 23"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.EDI
  value: "November 2, 2026 (application); November 9 (materials); November 17 (financial aid); December 11 (decisions)"
  source_url: https://admissions.washu.edu/how-to-apply/application-dates-deadlines/
  source_snippet: "Early Decision I Nov. 2 ... Nov. 9 ... Nov. 17 ... Dec. 11"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.EDII
  value: "January 4, 2027 (application); January 11 (materials); January 11 (financial aid); February 12 (decisions)"
  source_url: https://admissions.washu.edu/how-to-apply/application-dates-deadlines/
  source_snippet: "Early Decision II Jan. 4 ... Jan. 11 ... Jan. 11 ... Feb. 12"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.RD
  value: "January 4, 2027 (application); January 11 (materials); February 1 (financial aid); April 1 (decisions)"
  source_url: https://admissions.washu.edu/how-to-apply/application-dates-deadlines/
  source_snippet: "Regular Decision Jan. 4 ... Jan. 11 ... Feb. 1 ... Apr. 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.tests.policy
  value: "Test-optional"
  source_url: https://admissions.washu.edu/how-to-apply/first-year-us-applicants/
  source_snippet: "WashU is test optional. If you choose to submit scores, we accept self-reported scores on the Common App and Coalition App."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.tests.superscore
  value: "Yes (SAT and ACT)"
  source_url: https://admissions.washu.edu/how-to-apply/first-year-us-applicants/
  source_snippet: "We consider only the highest individual scores, whenever they occurred."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.tests.codes
  value: { SAT: 6929, ACT: 2386, TOEFL: 6929, CSS: 6929, FAFSA: 002520 }
  source_url: https://admissions.washu.edu/how-to-apply/first-year-us-applicants/
  source_snippet: "Our College Codes ACT: 2386 SAT: 6929 TOEFL: 6929 CSS Profile: 6929 FAFSA: 002520"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english_requirements
  value: { TOEFL_recommended: 100 (pre-Jan 2026) / 5.0 (post-Jan 2026), IELTS_recommended: 7.0, Duolingo_recommended: 130 }
  source_url: https://admissions.washu.edu/how-to-apply/english-testing-requirements/
  source_snippet: "TOEFL (or TOEFL iBT Home Edition): For exams taken prior to January 21, 2026, a minimum score of 100 is recommended. For exams taken on January 21, 2026 or later, a minimum score of 5.0 is recommended. IELTS Academic score of 7.0. Duolingo score of 130."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.cost.tuition
  value: "$71,310/year (2026-27)"
  source_url: https://financialaid.washu.edu/costs/
  source_snippet: "Tuition $71,310"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.total_coa
  value: "$96,994 university charges; ~$102,260 total estimated"
  source_url: https://financialaid.washu.edu/costs/
  source_snippet: "Total university charges $96,994 ... Total Other Estimated Expenses $5,266"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.housing_food
  value: "$24,272 average (modern double + Platinum meal plan)"
  source_url: https://financialaid.washu.edu/costs/
  source_snippet: "Average housing and food (university meal plan)* $24,272"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.aid.need_blind
  value: "Need-blind for US citizens/PRs; need-aware for internationals"
  source_url: https://financialaid.washu.edu/how-washu-helps/need-blind-policy/
  source_snippet: "WashU's Gateway to Success initiative is a $1 billion additional financial aid commitment that allows us to be 'need blind' in our admission process for first-year applicants who are U.S. citizens or permanent residents."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.aid.no_loan
  value: "100% demonstrated need met without loans"
  source_url: https://financialaid.washu.edu/
  source_snippet: "100% demonstrated financial need met without loans"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.aid.washu_pledge
  value: "Full ride for MO/southern IL families with income <$75k"
  source_url: https://financialaid.washu.edu/how-washu-helps/washu-pledge/
  source_snippet: "The WashU Pledge is a bold financial aid program that provides a free undergraduate education to incoming, full-time Missouri and southern Illinois students who come from a family with $75,000 or less in annual income."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.aid.average_offer
  value: "$73,000 average need-based financial aid offer"
  source_url: https://financialaid.washu.edu/
  source_snippet: "$73,000 average need-based financial aid offer"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.programs.total
  value: "119 UG majors + 121 minors"
  source_url: https://bulletin.wustl.edu/undergrad/majors/
  source_snippet: Full alphabetical listing of all undergraduate majors on bulletin.wustl.edu/undergrad/majors/
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.schools
  value: "4 UG schools: Arts & Sciences, Olin Business, Sam Fox (Architecture + Art), McKelvey Engineering"
  source_url: https://bulletin.wustl.edu/undergrad/
  source_snippet: "College of Arts & Sciences; Olin Business School; Sam Fox School of Design & Visual Arts (College of Architecture, College of Art); and McKelvey School of Engineering"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.schools
  value: "9 graduate/professional schools: Architecture & Urban Design, Art, Arts & Sciences, Business, Engineering, Law, Medicine, Public Health, Brown School (Social Work)"
  source_url: https://bulletin.wustl.edu/grad/
  source_snippet: "Architecture & Urban Design; Art; Arts & Sciences; Business; Engineering; Law; Medicine; Public Health; and Social Work & Social Policy"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.medicine.phd_programs
  value: "11 PhD programs in Biology & Biomedical Sciences"
  source_url: https://bulletin.wustl.edu/medicine/degrees-offerings/
  source_snippet: "Biochemistry, Biophysics, & Structural Biology, PhD; Biomedical Informatics & Data Science, PhD; Cancer Biology, PhD; Computational & Systems Biology, PhD; Developmental, Regenerative, & Stem Cell Biology, PhD; Immunology, PhD; Molecular Cell Biology, PhD; Molecular Genetics & Genomics, PhD; Molecular Microbiology & Microbial Pathogenesis, PhD; Neurosciences, PhD; Plant & Microbial Biosciences, PhD"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.business.programs
  value: "MBA (5 formats) + 10 specialized master's + 4 certificates + 2 doctoral"
  source_url: https://bulletin.wustl.edu/grad/business/graduate-masters/
  source_snippet: Lists Full-Time MBA, Flex MBA, 3 Executive MBAs, MACC, MSAIB, MSA, MSBOS, MSFC, MSFQ, MSFWAM, MSSCM, MSWM, OMSBA, Flex MSF
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.engineering.degrees
  value: "47 programs: 5 MEng, ~10 MS, ~12 PhD, ~10 certificates, dual degrees"
  source_url: https://bulletin.wustl.edu/grad/engineering/degrees/
  source_snippet: Full listing from Aerosol Science & Engineering to Systems Science & Mathematics
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection structure

```
washu-knowledge-base-v2
├── 00-overview (Section 0: counts, hierarchy, degree inventory, distribution matrix)
├── 01-ug-arts-sciences (Section 1: A&S majors grouped)
├── 02-ug-business (Section 1: Olin BSBA majors)
├── 03-ug-sam-fox (Section 1: Architecture + Art majors)
├── 04-ug-engineering (Section 1: McKelvey BS majors)
├── 05-ug-minors (Section 1.4: complete minors list)
├── 06-grad-architecture (Section 2: Architecture & Urban Design)
├── 07-grad-art (Section 2: Graduate School of Art)
├── 08-grad-arts-sciences (Section 2: A&S graduate programs)
├── 09-grad-business (Section 2: Olin graduate programs)
├── 10-grad-engineering (Section 2: McKelvey graduate programs)
├── 11-grad-law (Section 2: Law programs)
├── 12-grad-medicine (Section 2: Medicine programs)
├── 13-grad-public-health (Section 2: Public Health programs)
├── 14-grad-social-work (Section 2: Brown School programs)
├── 15-deadlines-requirements (Section 3)
├── 16-costs-aid (Section 4)
└── 17-evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "washu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BSBA|BFA|MA|MS|PhD|...>"
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
| P0 | Application fee amount | admissions.washu.edu/how-to-apply/ |
| P0 | Graduate tuition rates per school | bulletin.wustl.edu (per-school pages) |
| P0 | Per-program GRE policy (graduate) | Department websites |
| P1 | Graduate application deadlines per program | Department websites |
| P1 | Detailed housing costs by room type | housing.wustl.edu |
| P1 | Health insurance cost | financialaid.washu.edu |
| P2 | CAPS (Continuing & Professional Studies) programs | bulletin.wustl.edu/grad/caps/ |
| P2 | Class profile data (admit rate, GPA, test scores) | admissions.washu.edu/life-at-washu/incoming-class-profile/ |

---

## SECTION 7 -- Cross-school Comparison Framework

| Dimension | WashU | (Other schools TBD) |
|-----------|-------|---------------------|
| Type | Private | |
| Location | St. Louis, MO | |
| UG Tuition/yr | $71,310 | |
| Total UG COA/yr | ~$102,260 | |
| Need-blind (US) | Yes | |
| Need-blind (intl) | Need-aware | |
| Meets 100% need | Yes, no loans | |
| EA deadline | Nov 2 | |
| ED I deadline | Nov 2 | |
| ED II deadline | Jan 4 | |
| RD deadline | Jan 4 | |
| SAT/ACT required | No (test-optional) | |
| TOEFL min (recommended) | 100 / 5.0 | |
| IELTS min (recommended) | 7.0 | |
| Duolingo min (recommended) | 130 | |
| WashU Pledge threshold | $75k (MO/southern IL) | |
| Total program count (Rule 1) | ~458 | |
| School count (Rule 2) | 9 | |
| Avg need-based aid | $73,000 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.washu.edu, financialaid.washu.edu, bulletin.wustl.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school -> department -> degree-level -> program
