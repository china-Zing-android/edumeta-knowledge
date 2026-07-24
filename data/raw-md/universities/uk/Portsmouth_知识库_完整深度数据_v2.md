# University of Portsmouth Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England) — Modern University of the Year 2025–2026 (Times/Sunday Times)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/BEng/BN/LLB/MPharm/MPhys/MComp/FdA/HNC/BEd/CertHE/DipHE/HND/BDS 等) | 230 |
| 研究生授课型项目 (MA/MSc/MBA/MRes/LLM/MArch/MEd/MSW/MPA/DBA/MN/DipRIBA) | 183 |
| 研究生研究型项目 (PhD/MPhil/MD/ProfDoc by research) | 39 (PGR — separate research-degrees index, not in this count) |
| **学位项目总计 (UG + PGT)** | **413** |
| 学院 (Faculties) | 5 |
| 系所 (Schools) | 14 |
| 校区 | Portsmouth + London (Pathway) |

> Reconciliation: 230 UG + 183 PGT = 413 total program rows in Sections 1 + 2. PGR is a separate research-degree program type (not in this count).
> Source for counts: [Course index filter counts](https://www.port.ac.uk/study/courses) (230 UG + 184 PGT + 39 PGR = 453 total) and [Sitemap URLs](https://www.port.ac.uk/sitemap.xml) (233 UG base URLs + 184 PGT base URLs).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Portsmouth                                  [大学]
├── Faculty of Business and Law                          [学院]
│   ├── School of Accounting, Economics and Finance      [系]
│   ├── School of Law                                     [系]
│   ├── School of Organisations, Systems and People      [系]
│   └── School of Strategy, Marketing and Innovation     [系]
├── Faculty of Creative and Cultural Industries          [学院]
│   ├── School of Architecture, Art and Design           [系]
│   └── School of Film, Media, and Creative Technologies [系]
├── Faculty of Humanities and Social Sciences            [学院]
│   ├── School of Area Studies, Sociology, History, Politics and Literature  [系]
│   ├── School of Criminology and Criminal Justice       [系]
│   └── School of Education, Languages and Linguistics  [系]
├── Faculty of Science and Health                        [学院]
│   └── School of Pharmacy and Biomedical Sciences       [系]
│       ⚠ Also houses School of Biological Sciences, Psychology, Sport & Exercise Science, Dental, Medical, Nursing, Midwifery, Allied Health (uncovered via sitemap)
├── Faculty of Technology                                [学院]
│   ├── School of Civil Engineering and Surveying        [系]
│   ├── School of Computing                              [系]
│   ├── School of Electrical and Mechanical Engineering  [系]
│   └── School of Mathematics and Physics                [系]
└── London Pathway College                                [Pathway partner]
```

> Source: [Our academic structure](https://www.port.ac.uk/about-us/structure-and-governance/organisational-structure/our-academic-structure) — verified 2026-07-08.
> Note: Faculty of Science and Health sitemap shows multiple schools beyond pharmacy. Sub-departments not fully enumerated from one page; course pages link to their owning school individually.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本校 (official) | Canonical | 本项目数量 |
|---------|------|------|------------------|-----------|-----------|
| BA (Hons) | BA (Hons) (Bachelor) | 本科 | BA (Hons) | BA | 82 |
| BA (Hons),BSc (Hons) | BA (Hons),BSc (Hons) (Bachelor) | 本科 | BA (Hons),BSc (Hons) | BA/BS | 2 |
| BEng (Hons) | BEng (Hons) (Bachelor) | 本科 | BEng (Hons) | BEng | 21 |
| BN (Hons) | BN (Hons) (Bachelor) | 本科 | BN (Hons) | BN | 3 |
| BSc (Econ) (Hons) | BSc (Econ) (Hons) (Bachelor) | 本科 | BSc (Econ) (Hons) | BS(Econ) | 2 |
| BSc (Hons) | BSc (Hons) (Bachelor) | 本科 | BSc (Hons) | BS | 92 |
| BSc (Hons),MPhys (Hons) | BSc (Hons),MPhys (Hons) (Bachelor) | 本科 | BSc (Hons),MPhys (Hons) | BS/MPhys | 2 |
| FdA | FdA (Foundation) | 本科 | FdA | FdA | 2 |
| HNC | HNC (Other) | 本科 | HNC | HNC | 7 |
| LLB (Hons) | LLB (Hons) (Bachelor) | 本科 | LLB (Hons) | LLB | 4 |
| MPharm (Hons) | MPharm (Hons) (Bachelor) | 本科 | MPharm (Hons) | MPharm | 1 |
| UG-other | UG-other (Other) | 本科 | UG-other | UG-other | 12 |
| DBA | (PGT) | 研究生 | DBA | DBA | 1 |
| DipRIBA | (PGT) | 研究生 | DipRIBA | Dip | 1 |
| LLM | (PGT) | 研究生 | LLM | LLM | 4 |
| MA | (PGT) | 研究生 | MA | MA | 35 |
| MArch | (PGT) | 研究生 | MArch | MArch | 2 |
| MBA | (PGT) | 研究生 | MBA | MBA | 6 |
| MPA | (PGT) | 研究生 | MPA | MPA | 2 |
| MRes | (PGT) | 研究生 | MRes | MRes | 3 |
| MSc | (PGT) | 研究生 | MSc | MS | 85 |
| PGT-other | (PGT) | 研究生 | PGT-other | PGT-other | 44 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学位 (canonical) | 本科 UG | 研究生 PGT | 合计 |
|------------------|--------|----------|------|
| BA | 82 | 0 | 82 |
| BA/BS | 2 | 0 | 2 |
| BEng | 21 | 0 | 21 |
| BN | 3 | 0 | 3 |
| BS | 92 | 0 | 92 |
| BS(Econ) | 2 | 0 | 2 |
| BS/MPhys | 2 | 0 | 2 |
| DBA | 0 | 1 | 1 |
| Dip | 0 | 1 | 1 |
| FdA | 2 | 0 | 2 |
| HNC | 7 | 0 | 7 |
| LLB | 4 | 0 | 4 |
| LLM | 0 | 4 | 4 |
| MA | 0 | 35 | 35 |
| MArch | 0 | 2 | 2 |
| MBA | 0 | 6 | 6 |
| MPA | 0 | 2 | 2 |
| MPharm | 1 | 0 | 1 |
| MRes | 0 | 3 | 3 |
| MS | 0 | 85 | 85 |
| PGT-other | 0 | 44 | 44 |
| UG-other | 12 | 0 | 12 |
| **合计** | **230** | **183** | **413** |

> Note: matrix uses canonical degree codes (per [degree-taxonomy.md](../references/degree-taxonomy.md)). Since the homepage does not surface per-faculty program counts, the matrix is built as UG vs PGT by degree. Per-faculty attribution is not reliable from the public index pages and is therefore a **P1 follow-up** for a re-run that visits each course page and reads the breadcrumbs.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Portsmouth has **5 faculties** containing **14 schools** that deliver undergraduate programs. The full hierarchy is in Section 0.2. Each undergraduate program below is grouped by degree (not by school, because the program-index page does not expose school attribution; school attribution is available on individual course pages).

### 1.2 Undergraduate majors — grouped by degree

##### BA (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Computer Games Art | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-computer-games-art |
| 2 | Computer Games Design | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-computer-games-design |
| 3 | Accountancy and Financial Management (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-accountancy-and-financial-management-top-up |
| 4 | Animation | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-animation |
| 5 | Architectural Assistant Degree Apprenticeship | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-architectural-assistant-degree-apprenticeship |
| 6 | Architecture | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-architecture |
| 7 | Business and Computer Studies (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-computer-studies-learning-at-work |
| 8 | Business and Human Resource Management | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-human-resource-management |
| 9 | Business and Management | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-management |
| 10 | Chartered Manager Degree Apprenticeship (Business Leadership and Management) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-leadership-and-management-degree-apprenticeship |
| 11 | Business (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-learning-at-work |
| 12 | Entrepreneurship and Business | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-entrepreneurship-and-business |
| 13 | Childhood and Youth Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-childhood-and-youth-studies |
| 14 | Childhood and Youth Studies with Criminology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-childhood-and-youth-studies-with-criminology |
| 15 | Childhood and Youth Studies with Psychology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-childhood-and-youth-studies-with-psychology |
| 16 | Creative Music Technology Top-up | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-creative-music-technology-top-up |
| 17 | Creative Writing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-creative-writing |
| 18 | Digital Marketing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-digital-marketing |
| 19 | Early Childhood Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-early-childhood-studies |
| 20 | Early Childhood Studies with Psychology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-early-childhood-studies-with-psychology |
| 21 | Economics and Management | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-economics-and-management |
| 22 | Education Studies (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-education-studies-top-up |
| 23 | English and Creative Writing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-english-and-creative-writing |
| 24 | English Language and Linguistics | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-english-language-and-linguistics |
| 25 | English Literature | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-english-literature |
| 26 | English Literature with Media Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-english-literature-with-media-studies |
| 27 | Fashion Design | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-fashion-design |
| 28 | Film Production | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-film-production |
| 29 | Film Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-film-studies |
| 30 | Screenwriting | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-screenwriting |
| 31 | Finance with Business Communication (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-finance-with-business-communication-top-up |
| 32 | Global Communication and Media (Dual Degree - Edith Cowan University) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-global-communication-and-media-dual-degree-edith-cowan-university |
| 33 | Graphic Design | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-graphic-design |
| 34 | History | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-history |
| 35 | History with American Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-history-with-american-studies |
| 36 | History with Sociology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-history-with-sociology |
| 37 | Illustration | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-illustration |
| 38 | Interior Architecture and Design | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-interior-architecture-and-design |
| 39 | International Business | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-business |
| 40 | International Business Communication TOP UP | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-business-communication-top-up |
| 41 | International Development | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-development |
| 42 | International Development and Languages | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-development-and-languages |
| 43 | International Development with Sociology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-development-with-sociology |
| 44 | International Relations | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-relations |
| 45 | International Relations and Languages | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-relations-and-languages |
| 46 | International Relations and Politics | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-relations-and-politics |
| 47 | International Relations with History | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-relations-with-history |
| 48 | International Relations with International Development | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-relations-with-international-development |
| 49 | International Trade and Business Communication (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-trade-and-business-communication-top-up |
| 50 | Journalism | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-journalism |
| 51 | Journalism with Creative Writing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-journalism-with-creative-writing |
| 52 | Journalism with Media Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-journalism-with-media-studies |
| 53 | Marketing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-marketing |
| 54 | Media and Communication with Foundation Year | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-media-and-communication-with-foundation-year |
| 55 | Media Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-media-studies |
| 56 | Modern Languages | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-modern-languages |
| 57 | Musical Theatre | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-musical-theatre |
| 58 | Photography | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-photography |
| 59 | Politics | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-politics |
| 60 | Fashion Marketing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-fashion-marketing |
| 61 | History and Politics | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-history-and-politics |
| 62 | Business and Management | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-management-london |
| 63 | Marketing | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-marketing-london |
| 64 | Post-Production for Film and Television | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-post-production-for-film-and-television |
| 65 | Business and Management (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-management-top-up |
| 66 | Theatre | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-theatre |
| 67 | Digital Marketing (Degree Apprenticeship) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-digital-marketing-degree-apprenticeship |
| 68 | International Enterprise and Business Communication (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-enterprise-and-business-communication-top-up |
| 69 | International Human Resources and Business Communication (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-human-resources-and-business-communication-top-up |
| 70 | Creative Music Technology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-creative-music-technology |
| 71 | Acting | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-acting |
| 72 | Marketing (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-marketing-top-up |
| 73 | Education Studies | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-education-studies |
| 74 | International Business and Languages | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-international-business-and-languages |
| 75 | Humanities and Social Sciences | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-humanities-and-social-sciences |
| 76 | Business and Management (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-management-top-up-london |
| 77 | Politics and Sociology | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-politics-and-sociology |
| 78 | English and History | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-english-and-history |
| 79 | Primary Education Studies - Teacher Degree Apprenticeship | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-primary-education-studies-teacher-degree-apprenticeship |
| 80 | Secondary English Education Studies - Teacher Degree Apprenticeship | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-secondary-english-education-studies-teacher-degree-apprenticeship |
| 81 | English Language and Literature | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-english-language-and-literature |
| 82 | Business and Management Business Analytics London | https://www.port.ac.uk/study/courses/undergraduate/ba-hons-business-and-management-business-analytics-london |

##### BA (Hons),BSc (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Creative Computing | https://www.port.ac.uk/study/courses/undergraduate/ba-bsc-hons-creative-computing |
| 2 | Professional Studies (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-professional-studies-learning-at-work |

##### BEng (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Civil Engineer Degree Apprenticeship (Civil Engineering) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-civil-engineer-degree-apprenticeship-civil-engineering |
| 2 | Electronic Engineering Top-up Degree Apprenticeship | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-electronic-engineering-top-up-degree-apprenticeship |
| 3 | Electronic Systems Engineering (Distance Learning) (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-electronic-systems-engineering-distance-learning-top-up |
| 4 | Engineering and Technology with Foundation Year | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-engineering-and-technology-with-foundation-year |
| 5 | Mechanical and Manufacturing Engineering | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-mechanical-and-manufacturing-engineering |
| 6 | Mechanical and Manufacturing Engineering (Top-Up) Degree Apprenticeship (1 year) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-mechanical-and-manufacturing-engineering-top-up-degree-apprenticeship-1-year |
| 7 | Mechanical and Manufacturing Engineering Top-up (Distance Learning) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-mechanical-and-manufacturing-engineering-top-up-distance-learning |
| 8 | ,MEng Civil Engineering | https://www.port.ac.uk/study/courses/undergraduate/beng-meng-civil-engineering |
| 9 | ,MEng Electronic Engineering | https://www.port.ac.uk/study/courses/undergraduate/beng-meng-electronic-engineering |
| 10 | ,MEng Mechanical Engineering | https://www.port.ac.uk/study/courses/undergraduate/beng-meng-mechanical-engineering |
| 11 | ,MEng Renewable Energy Engineering | https://www.port.ac.uk/study/courses/undergraduate/meng-beng-renewable-energy-engineering |
| 12 | Engineering Management (Distance Learning Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-engineering-management-distance-learning-top-up |
| 13 | Robotics and Artificial Intelligence | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-robotics-and-artificial-intelligence |
| 14 | Electrical Power Engineering | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-electrical-power-engineering |
| 15 | Space Systems Engineering (Degree Apprenticeship) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-space-systems-engineering-degree-apprenticeship |
| 16 | Professional Engineering (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-professional-engineering-learning-at-work |
| 17 | Civil Engineering and Construction Management (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-civil-engineering-and-construction-management-top-up |
| 18 | Engineering Management (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-engineering-management-top-up |
| 19 | Electronic Systems Engineering (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-electronic-systems-engineering-top-up |
| 20 | Mechanical Systems Engineering (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-mechanical-systems-engineering-top-up |
| 21 | Mechanical and Manufacturing Engineering (Top-Up) Degree Apprenticeship (2 Year) | https://www.port.ac.uk/study/courses/undergraduate/beng-hons-mechanical-and-manufacturing-engineering-top-up-degree-apprenticeship-2-year |

##### BN (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Nursing (Adult) | https://www.port.ac.uk/study/courses/undergraduate/bn-hons-nursing-adult |
| 2 | Nursing Mental Health | https://www.port.ac.uk/study/courses/undergraduate/bn-hons-nursing-mental-health |
| 3 | Nursing (Adult) (Degree Apprenticeship) (Extended) | https://www.port.ac.uk/study/courses/undergraduate/bn-hons-nursing-adult-degree-apprenticeship-extended |

##### BSc (Econ) (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Economics | https://www.port.ac.uk/study/courses/undergraduate/bsc-econ-hons-economics |
| 2 | Economics, Finance and Banking | https://www.port.ac.uk/study/courses/undergraduate/bsc-econ-hons-economics-finance-and-banking |

##### BSc (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Accounting with Finance | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-accounting-with-finance |
| 2 | Construction Management | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-construction-management |
| 3 | Applied Biomedical Science (Distance Learning) (Degree Apprenticeship) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-applied-biomedical-science-distance-learning-degree-apprenticeship |
| 4 | Biochemistry | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-biochemistry |
| 5 | Biology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-biology |
| 6 | Biomedical Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-biomedical-science |
| 7 | Building Surveying | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-building-surveying |
| 8 | Chartered Surveyor Degree Apprenticeship (Building Surveying) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-building-surveying-degree-apprenticeship |
| 9 | Business and Supply Chain Management | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-business-and-supply-chain-management |
| 10 | Cognitive Behavioural Therapy Top up | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-cognitive-behavioural-therapy-top-up |
| 11 | Computer Animation and Visual Effects | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-animation-and-visual-effects |
| 12 | Computer Games Production | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-games-production |
| 13 | Computer Games Technology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-games-technology |
| 14 | Computer Networks and Security | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-networks-and-security |
| 15 | Computing | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computing |
| 16 | Applied Computing (Distance Learning) (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-applied-computing-distance-learning-top-up |
| 17 | Creative Media Technologies | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-creative-media-technologies |
| 18 | Creative Media Technologies (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-creative-media-technologies-top-up |
| 19 | Creative Technologies and Enterprise (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-creative-technologies-and-enterprise-learning-at-work |
| 20 | Criminology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-criminology |
| 21 | Criminology and Criminal Justice (Distance Learning) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-criminology-and-criminal-justice-distance-learning |
| 22 | Criminology and Cybercrime | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-criminology-and-cybercrime |
| 23 | Criminology and Forensic Investigation | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-criminology-and-forensic-investigation |
| 24 | Criminology and Psychology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-criminology-and-psychology |
| 25 | Cyber Security and Forensic Computing | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-cyber-security-and-forensic-computing |
| 26 | Data Science and Artificial Intelligence | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-data-science-and-artificial-intelligence |
| 27 | Dental Hygiene | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-dental-hygiene |
| 28 | Dental Hygiene and Dental Therapy | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-dental-hygiene-and-dental-therapy |
| 29 | Diagnostic Radiography and Medical Imaging | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-diagnostic-radiography-and-medical-imaging |
| 30 | Engineering and Management Studies (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-engineering-and-management-studies-learning-at-work |
| 31 | Engineering Studies (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-engineering-studies-learning-at-work |
| 32 | Environmental Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-environmental-science |
| 33 | Environmental Science and Management (Dual Degree - Edith Cowan University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-environmental-science-and-management-dual-degree-edith-cowan-university |
| 34 | Psychology with Forensic and Investigative Psychology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-psychology-with-forensic-and-investigative-psychology |
| 35 | Geography | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-geography |
| 36 | Earth Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-earth-science |
| 37 | Gestalt Counselling (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-gestalt-counselling-top-up |
| 38 | Humanistic Counselling Top-up | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-humanistic-counselling-top-up |
| 39 | Marine Biology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-marine-biology |
| 40 | Marine Environmental Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-marine-environmental-science |
| 41 | Maritime Studies (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-maritime-studies-learning-at-work |
| 42 | Mathematics for Finance and Management | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-mathematics-for-finance-and-management |
| 43 | Mathematics with Statistics | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-mathematics-with-statistics |
| 44 | Music Technology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-music-technology |
| 45 | Operating Department Practice | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-operating-department-practice |
| 46 | Palaeontology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-palaeontology |
| 47 | Paramedic Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-paramedic-science |
| 48 | Pharmacology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-pharmacology |
| 49 | Policing and Investigation (Distance Learning) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-policing-and-investigation |
| 50 | Product Design and Innovation | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-product-design-and-innovation |
| 51 | Professional Policing | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-professional-policing |
| 52 | Project Management Degree Apprenticeship | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-project-management-degree-apprenticeship |
| 53 | Real Estate and Property Development | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-real-estate-and-property-development |
| 54 | Psychology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-psychology |
| 55 | Quantity Surveying | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-quantity-surveying |
| 56 | Chartered Surveyor Degree Apprenticeship (Quantity Surveying) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-quantity-surveying-degree-apprenticeship |
| 57 | Risk and Security Management (Distance Learning) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-risk-and-security-management |
| 58 | Science with Foundation Year | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-science-with-foundation-year |
| 59 | Social Work | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-social-work |
| 60 | Sociology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sociology |
| 61 | Sociology with Criminology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sociology-with-criminology |
| 62 | Sociology with Media Studies | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sociology-with-media-studies |
| 63 | Sociology with Psychology | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sociology-with-psychology |
| 64 | Software Engineering | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-software-engineering |
| 65 | Psychology of Sport and Performance | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-psychology-of-sport-and-performance |
| 66 | Sport and Exercise Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sport-and-exercise-science |
| 67 | Sport, Health and Exercise Sciences (Dual Degree - Edith Cowan University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sport-health-and-exercise-sciences-dual-degree-edith-cowan-university |
| 68 | Sport Management (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sport-management-top-up |
| 69 | Sports Coaching (Top Up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sports-coaching-top-up |
| 70 | Sport Management | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sport-management |
| 71 | ,MEng Computer Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-meng-computer-science |
| 72 | Mathematics | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-mathematics |
| 73 | Security and Risk (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-security-and-risk-learning-at-work |
| 74 | Global Sport Management (Dual Degree - Edith Cowan University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-global-sport-management-dual-degree-edith-cowan-university |
| 75 | Biomedical Science with Human Biosciences (Dual Degree - Edith Cowan University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-biomedical-science-with-human-biosciences-dual-degree-edith-cowan-university |
| 76 | Computer Science | https://www.port.ac.uk/study/courses/undergraduate/bsc-computer-science-london |
| 77 | Construction Management (Top Up) (Degree Apprenticeship) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-construction-management-top-up-degree-apprenticeship |
| 78 | Accounting with International Finance (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-accounting-with-international-finance-top-up |
| 79 | Mathematics with Machine Learning | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-mathematics-with-machine-learning |
| 80 | Psychology (Dual Degree - Edith Cowan University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-psychology-dual-degree-edith-cowan-university |
| 81 | Marketing and Management | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-marketing-and-management |
| 82 | Computer Science and Advanced Technologies (Top-Up) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-science-and-advanced-technologies-top-up |
| 83 | Computer Science (Top-Up) (London) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-science-top-up-london |
| 84 | Business with Foundation Year | https://www.port.ac.uk/study/courses/undergraduate/foundation-in-business-london |
| 85 | Computing with Foundation Year | https://www.port.ac.uk/study/courses/undergraduate/foundation-in-computing-london |
| 86 | Sport, Exercise and Rehabilitation Science (Dual Degree - Brock University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-sport-exercise-and-rehabilitation-science-dual-degree-brock-university |
| 87 | Global Sport Management (Dual Degree - Brock University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-global-sport-management-dual-degree-brock-university |
| 88 | Computer Science (Dual Degree - Brock University) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-science-dual-degree-brock-university |
| 89 | Accounting and Finance | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-accounting-and-finance-london |
| 90 | Computer Science Cyber Security London | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-science-cyber-security-london |
| 91 | Computer Science (Artificial Intelligence) | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-computer-science-artificial-intelligence-london |
| 92 | Business Computing | https://www.port.ac.uk/study/courses/undergraduate/bsc-hons-business-computing-london |

##### BSc (Hons),MPhys (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Physics | https://www.port.ac.uk/study/courses/undergraduate/bsc-mphys-physics |
| 2 | Physics, Astrophysics and Cosmology | https://www.port.ac.uk/study/courses/undergraduate/bsc-mphys-physics-astrophysics-and-cosmology |

##### FdA

| # | Program | URL |
|---|---------|-----|
| 1 | Early Years Care and Education | https://www.port.ac.uk/study/courses/undergraduate/fda-early-years-care-and-education |
| 2 | Learning Support | https://www.port.ac.uk/study/courses/undergraduate/fda-learning-support |

##### HNC

| # | Program | URL |
|---|---------|-----|
| 1 | Construction HNC | https://www.port.ac.uk/study/courses/undergraduate/hnc-construction-hnc |
| 2 | Electrical and Electronic Engineering HNC | https://www.port.ac.uk/study/courses/undergraduate/hnc-electrical-and-electronic-engineering-hnc |
| 3 | Mechanical Engineering HNC | https://www.port.ac.uk/study/courses/undergraduate/hnc-mechanical-engineering-hnc |
| 4 | HNC Software Development (Computing) | https://www.port.ac.uk/study/courses/undergraduate/hnc-hnc-software-development-computing |
| 5 | Electrical Power Engineering HNC (Higher Apprenticeship) | https://www.port.ac.uk/study/courses/undergraduate/hnc-electrical-power-engineering-hnc-higher-apprenticeship |
| 6 | Electrical and Electronic Engineering CEMAST | https://www.port.ac.uk/study/courses/undergraduate/hnc-electrical-and-electronic-engineering-cemast |
| 7 | Mechanical Engineering Cemast | https://www.port.ac.uk/study/courses/undergraduate/hnc-mechanical-engineering-cemast |

##### LLB (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Law | https://www.port.ac.uk/study/courses/undergraduate/llb-hons-law |
| 2 | Law with Business | https://www.port.ac.uk/study/courses/undergraduate/llb-hons-law-with-business |
| 3 | Law with Criminology | https://www.port.ac.uk/study/courses/undergraduate/llb-hons-law-with-criminology |
| 4 | Law with Legal Practice | https://www.port.ac.uk/study/courses/undergraduate/llb-hons-law-with-legal-practice |

##### MPharm (Hons)

| # | Program | URL |
|---|---------|-----|
| 1 | Pharmacy | https://www.port.ac.uk/study/courses/undergraduate/mpharm-hons-pharmacy |

##### UG-other

| # | Program | URL |
|---|---------|-----|
| 1 | BEd Primary Education with Qualified Teacher Status | https://www.port.ac.uk/study/courses/undergraduate/bed-primary-education-with-qualified-teacher-status |
| 2 | CertEd Further Education and Skills | https://www.port.ac.uk/study/courses/undergraduate/certed-further-education-and-skills |
| 3 | CertHE Dental Nursing | https://www.port.ac.uk/study/courses/undergraduate/certhe-dental-nursing |
| 4 | CertHE Professional Studies (Learning at Work) | https://www.port.ac.uk/study/courses/undergraduate/certhe-professional-studies |
| 5 | DipHE Cognitive Behavioural Therapy | https://www.port.ac.uk/study/courses/undergraduate/diphe-cognitive-behavioural-therapy |
| 6 | DipHE Gestalt Counselling | https://www.port.ac.uk/study/courses/undergraduate/diphe-gestalt-counselling |
| 7 | DipHE Humanistic Counselling | https://www.port.ac.uk/study/courses/undergraduate/diphe-humanistic-counselling |
| 8 | HND Business | https://www.port.ac.uk/study/courses/undergraduate/hnd-business |
| 9 | HND General Engineering | https://www.port.ac.uk/study/courses/undergraduate/hnd-general-engineering |
| 10 | HND Computing (Top-up) | https://www.port.ac.uk/study/courses/undergraduate/hnd-computing-top-up |
| 11 | BDS Dental Surgery | https://www.port.ac.uk/study/courses/undergraduate/bds-dental-surgery |
| 12 | HND General Engineering CEMAST | https://www.port.ac.uk/study/courses/undergraduate/hnd-general-engineering-cemast |


> Source for all 230 UG programs: [Course index — Undergraduate](https://www.port.ac.uk/study/courses?level=Undergraduate) and sitemap (233 base URLs after filtering test/clone pages, dedupe).
> Note: 'UG-other' includes BEd, CertEd, CertHE, DipHE, HND, BDS — all legitimate qualification types.

### 1.3 Foundation Year / Top-up routes

Several programs offer Foundation Year or Top-up entry. Examples: `Media and Communication with Foundation Year`, `International Business Communication (Top-up)`. See specific entries in section 1.2.

### 1.4 Pathways / Apprenticeships

Many courses are also offered as Degree Apprenticeships and via London campus (e.g. `Business and Management (London)`, `Marketing (London)`, `BSc Computer Science (Cyber Security) London`).

### 1.5 General University admission requirements (UCAS)

- UCAS application through [UCAS](https://www.ucas.com/)
- Typical offer: 104–120 UCAS points for most UG (varies by course; higher for Medicine, Pharmacy, etc.)
- English language: see Section 3
- Personal statement via UCAS

### 1.6 No formal program numbering scheme

Portsmouth does not use MIT-style course numbers. Programs are identified by URL slug (e.g. `ba-hons-computer-games-art`).

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate (taught) programs — grouped by degree

##### DBA

| # | Program | URL |
|---|---------|-----|
| 1 | Professional Doctorate in Business Administration | https://www.port.ac.uk/study/courses/postgraduate-taught/dba-professional-doctorate-in-business-administration |

##### DipRIBA

| # | Program | URL |
|---|---------|-----|
| 1 | International Professional Practice Part 3 Architecture | https://www.port.ac.uk/study/courses/postgraduate-taught/international-professional-practice-part-3-architecture |

##### LLM

| # | Program | URL |
|---|---------|-----|
| 1 | Corporate Governance and Law GradCG | https://www.port.ac.uk/study/courses/postgraduate-taught/llm-corporate-governance-and-law-gradcg |
| 2 | Law | https://www.port.ac.uk/study/courses/postgraduate-taught/llm-law |
| 3 | Professional Legal Practice | https://www.port.ac.uk/study/courses/postgraduate-taught/llm-professional-legal-practice |
| 4 | Corporate Governance and Law GradCG (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/llm-corporate-governance-and-law-gradcg-with-professional-experience |

##### MA

| # | Program | URL |
|---|---------|-----|
| 1 | Applied Linguistics and TESOL (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-applied-linguistics-and-tesol-with-professional-experience |
| 2 | Architecture | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-architecture |
| 3 | Business Communication for International Leadership (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-business-communication-for-international-leadership-with-professional-experience |
| 4 | Applied Linguistics and TESOL | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-applied-linguistics-and-tesol |
| 5 | Business and Computer Studies (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-business-and-computer-studies-learning-at-work |
| 6 | Business Communication for International Leadership | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-business-communication-for-international-leadership |
| 7 | Business Management (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-business-management-learning-at-work |
| 8 | Architecture: Building and Heritage Conservation | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-architecture-building-and-heritage-conservation |
| 9 | Creative Technologies | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-creative-technologies |
| 10 | Creative Writing | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-creative-writing |
| 11 | Digital Marketing | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-digital-marketing |
| 12 | Education Studies | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-education-studies |
| 13 | Fashion and Textiles | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-fashion-and-textiles |
| 14 | Graphic Design | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-graphic-design |
| 15 | Illustration | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-illustration |
| 16 | Interior Architecture and Design | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-interior-architecture-and-design |
| 17 | International Relations | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-international-relations |
| 18 | International Relations (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-international-relations-distance-learning |
| 19 | International Relations and Politics | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-international-relations-and-politics |
| 20 | Journalism (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-journalism |
| 21 | Media and Communication | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-media-and-communication |
| 22 | Naval, Maritime and Coastal History (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-naval-maritime-and-coastal-history |
| 23 | Photography | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-photography |
| 24 | Senior Journalist Master&#039;s Degree Apprenticeship (Journalism) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-senior-journalist-masters-degree-apprenticeship |
| 25 | Translation Studies (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-translation-studies-distance-learning |
| 26 | Victorian Gothic: History, Literature and Culture (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-victorian-gothic-history-literature-and-culture-distance-learning |
| 27 | Education Studies (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-education-studies-with-professional-experience |
| 28 | TESOL | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-tesol |
| 29 | Applied Linguistics | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-applied-linguistics |
| 30 | Animation | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-animation |
| 31 | Music Technology | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-music-technology |
| 32 | Extended Reality | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-extended-reality |
| 33 | Games Development | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-games-development |
| 34 | Visual Communication | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-visual-communication |
| 35 | TESOL (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-tesol-with-professional-experience |

##### MArch

| # | Program | URL |
|---|---------|-----|
| 1 | Architect Degree Apprenticeship (Master of Architecture and Professional Practice) | https://www.port.ac.uk/study/courses/postgraduate-taught/march-architect-degree-apprenticeship |
| 2 | Architecture | https://www.port.ac.uk/study/courses/postgraduate-taught/march-architecture |

##### MBA

| # | Program | URL |
|---|---------|-----|
| 1 | Global | https://www.port.ac.uk/study/courses/postgraduate-taught/mba-global |
| 2 | Senior Leadership (Top-Up) | https://www.port.ac.uk/study/courses/postgraduate-taught/mba-senior-leadership-top-up |
| 3 | Global MBA (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/mba-global-mba-with-professional-experience |
| 4 | Master of Business Administration | https://www.port.ac.uk/study/courses/postgraduate-taught/mba-master-of-business-administration-london |
| 5 | Strategic Leadership | https://www.port.ac.uk/study/courses/postgraduate-taught/mba-strategic-leadership-london |
| 6 | Educational Leadership | https://www.port.ac.uk/study/courses/postgraduate-taught/mba-educational-leadership-london |

##### MPA

| # | Program | URL |
|---|---------|-----|
| 1 | Public Administration (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/mpa-public-administration-distance-learning |
| 2 | Public Administration Distance Learning (Top-up) | https://www.port.ac.uk/study/courses/postgraduate-taught/mpa-public-administration-distance-learning-top-up |

##### MRes

| # | Program | URL |
|---|---------|-----|
| 1 | Creative Industries | https://www.port.ac.uk/study/courses/postgraduate-taught/mres-creative-industries |
| 2 | Humanities and Social Sciences | https://www.port.ac.uk/study/courses/postgraduate-taught/mres-humanities-and-social-sciences |
| 3 | Science and Health | https://www.port.ac.uk/study/courses/postgraduate-taught/mres-science-and-health |

##### MSc

| # | Program | URL |
|---|---------|-----|
| 1 | Marketing Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-marketing-management |
| 2 | Accounting and Data Analytics | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-accounting-and-data-analytics |
| 3 | Accounting and Finance | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-accounting-and-finance |
| 4 | Advanced Aesthetic and Restorative Dentistry (Top-up) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-advanced-aesthetic-and-restorative-dentistry-top-up |
| 5 | Advanced Restorative Dental Therapy (Top-up) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-advanced-restorative-dental-therapy-top-up |
| 6 | Advanced Manufacturing | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-advanced-manufacturing |
| 7 | Applied Aquatic Biology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-applied-aquatic-biology |
| 8 | Information Security and Risk (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-information-security-and-risk-learning-at-work |
| 9 | Security and Risk (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-security-and-risk-learning-at-work |
| 10 | Biotechnology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-biotechnology |
| 11 | Building Information Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-building-information-management |
| 12 | Civil Engineering | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-civil-engineering |
| 13 | Clinical Exercise Physiology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-clinical-exercise-physiology |
| 14 | Computer Animation | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-computer-animation |
| 15 | Computer Games Technology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-computer-games-technology |
| 16 | Biomedical Engineering | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-biomedical-engineering |
| 17 | Computer Network Administration and Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-computer-network-administration-and-management |
| 18 | Construction Project Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-construction-project-management |
| 19 | Creative Technologies | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-creative-technologies |
| 20 | Crisis and Disaster Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-crisis-and-disaster-management |
| 21 | Cyber Security and Forensic Information Technology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-cyber-security-and-forensic-information-technology |
| 22 | Data Analytics | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-data-analytics |
| 23 | Digital Business Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-digital-business-management |
| 24 | User Experience Design | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-user-experience-design |
| 25 | Electronic and Electrical Engineering | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-electronic-and-electrical-engineering |
| 26 | Energy and Power Systems Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-energy-and-power-systems-management |
| 27 | Engineering and Management (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-engineering-and-management-learning-at-work |
| 28 | Engineering Geology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-engineering-geology |
| 29 | Engineering (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-engineering-learning-at-work |
| 30 | Engineering Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-engineering-management |
| 31 | Forensic Accounting | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-forensic-accounting |
| 32 | Forensic Psychology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-forensic-psychology |
| 33 | Geographical Information Systems | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-geographical-information-systems |
| 34 | Health Psychology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-health-psychology |
| 35 | Human Resource Development (Top-up) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-human-resource-development-top-up |
| 36 | Human Resource Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-human-resource-management |
| 37 | Human Resource Management Top-up | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-human-resource-management-top-up |
| 38 | Information Systems | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-information-systems |
| 39 | Innovation Management and Entrepreneurship | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-innovation-management-and-entrepreneurship |
| 40 | International Business and Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-business-and-management |
| 41 | International Development (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-development-distance-learning |
| 42 | Finance and Banking | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-finance-and-banking |
| 43 | International Human Resource Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-human-resource-management |
| 44 | Leadership and Management (Top-up) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-leadership-and-management-top-up |
| 45 | Logistics and Supply Chain Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-logistics-and-supply-chain-management |
| 46 | Maritime Studies (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-maritime-studies-learning-at-work |
| 47 | Mechanical Engineering | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-mechanical-engineering |
| 48 | Medical Biotechnology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-medical-biotechnology |
| 49 | Music Technology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-music-technology |
| 50 | Occupational Health and Safety Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-occupational-health-and-safety-management |
| 51 | Occupational Health, Safety and Environmental Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-occupational-health-safety-and-environmental-management |
| 52 | Occupational Health, Safety and Environmental Management (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-occupational-health-safety-and-environmental-management-learning-at-work |
| 53 | Educational Leadership and Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-educational-leadership-and-management |
| 54 | Physiotherapy (Pre-Registration) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-physiotherapy-pre-registration |
| 55 | Project Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-project-management |
| 56 | Psychology and Learning Disability | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-psychology-and-learning-disability |
| 57 | Quantity Surveying | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-quantity-surveying |
| 58 | Real Estate Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-real-estate-management |
| 59 | Risk and Safety Management Professional Degree Apprenticeship (Risk and Safety Leadership) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-risk-and-safety-leadership-degree-apprenticeship |
| 60 | Risk, Crisis and Resilience Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-risk-crisis-and-resilience-management |
| 61 | Social Work | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-social-work |
| 62 | Applied Sport Psychology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-applied-sport-psychology |
| 63 | Sport Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-sport-management |
| 64 | Applied Sport and Exercise Performance | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-applied-sport-and-exercise-performance |
| 65 | Strategic Quality Management (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-strategic-quality-management-distance-learning |
| 66 | Strength, Conditioning, and Rehabilitation | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-strength-conditioning-and-rehabilitation |
| 67 | Educational Leadership and Management (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-educational-leadership-and-management-with-professional-experience |
| 68 | Water and Environmental Engineering | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-water-and-environmental-engineering |
| 69 | Occupational Health and Safety Management (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-occupational-health-and-safety-management-learning-at-work |
| 70 | Cybercrime (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-cybercrime-distance-learning |
| 71 | Sociology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-sociology |
| 72 | Computer Science | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-computer-science |
| 73 | Professional Engineering (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-professional-engineering-learning-at-work |
| 74 | International Criminal Justice (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-criminal-justice-distance-learning |
| 75 | Occupational Hygiene (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-occupational-hygiene-learning-at-work |
| 76 | Extended Reality | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-extended-reality |
| 77 | International Hospitality and Tourism Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-hospitality-and-tourism-management |
| 78 | Educational Leadership and Management (Distance Learning) (Top-Up) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-educational-leadership-and-management-distance-learning-top-up |
| 79 | International Hospitality and Tourism Management (with Professional Experience) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-hospitality-and-tourism-management-with-professional-experience |
| 80 | MSc International Security and Risk (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-security-and-risk-distance-learning |
| 81 | Psychology (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-psychology-distance-learning |
| 82 | Business Analytics | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-business-analytics-london |
| 83 | Project Management | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-project-management-london |
| 84 | Marketing | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-marketing-london |
| 85 | Computer Science | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-computer-science-london |

##### PGT-other

| # | Program | URL |
|---|---------|-----|
| 1 | MA,MSc Professional Studies (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-professional-studies-learning-at-work |
| 2 | Final Examination in Professional Practice (Part 3) Architecture | https://www.port.ac.uk/study/courses/postgraduate-taught/part-3-exemption-final-examination-in-professional-practice-part-3-architecture |
| 3 | PGCE PGCE Courses | https://www.port.ac.uk/study/courses/postgraduate-taught/pgce-courses |
| 4 | PGCE Further Education and Skills | https://www.port.ac.uk/study/courses/postgraduate-taught/pgce-further-education-and-skills |
| 5 | PGCE Primary | https://www.port.ac.uk/study/courses/postgraduate-taught/pgce-primary |
| 6 | PgCert Conscious Sedation for Dentistry | https://www.port.ac.uk/study/courses/postgraduate-taught/pgcert-conscious-sedation-for-dentistry |
| 7 | PgCert Independent Prescribing for Pharmacists | https://www.port.ac.uk/study/courses/postgraduate-taught/pgcert-independent-prescribing-for-pharmacists |
| 8 | PgCert Occupational Health and Safety Management (Distance Learning) (Learning at Work) | https://www.port.ac.uk/study/courses/postgraduate-taught/pgcert-occupational-health-and-safety-management |
| 9 | PgDip Postgraduate Engineering Degree Apprenticeship (Engineering Competence) | https://www.port.ac.uk/study/courses/postgraduate-taught/pgdip-postgraduate-engineering-degree-apprenticeship-engineering-competence |
| 10 | PgDip Human Resource Development and Training Management | https://www.port.ac.uk/study/courses/postgraduate-taught/pgdip-human-resource-development-and-training-management |
| 11 | Postgraduate Teaching Apprenticeship | https://www.port.ac.uk/study/courses/postgraduate-taught/postgraduate-teaching-apprenticeship |
| 12 | EdD Professional Doctorate in Education | https://www.port.ac.uk/study/courses/postgraduate-taught/edd-professional-doctorate-in-education |
| 13 | Prof Doc Sport and Exercise Psychology | https://www.port.ac.uk/study/courses/postgraduate-taught/prof-doc-sport-and-exercise-psychology |
| 14 | DCrimJ Professional Doctorate in Criminal Justice | https://www.port.ac.uk/study/courses/postgraduate-taught/dcrimj-professional-doctorate-in-criminal-justice |
| 15 | Professional Doctorate in Security Risk Management | https://www.port.ac.uk/study/courses/postgraduate-taught/professional-doctorate-in-security-risk-management |
| 16 | Msc Artificial Intelligence and Machine Learning | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-artificial-intelligence-and-machine-learning |
| 17 | Msc Construction Project Management London | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-construction-project-management-london |
| 18 | Msc Information Systems London | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-information-systems-london |
| 19 | Msc Engineering Management London | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-engineering-management-london |
| 20 | Msc International Business and Management London | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-business-and-management-london |
| 21 | Ma Digital Marketing London | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-digital-marketing-london |
| 22 | Ma Architecture Landscape and Urban Design | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-architecture-landscape-and-urban-design |
| 23 | Msc Cybercrime Terrorism and Security | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-cybercrime-terrorism-and-security |
| 24 | Msc International Criminal Justice and Intelligence | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-international-criminal-justice-and-intelligence |
| 25 | Msc Terrorism and Security Management Distance Learning | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-terrorism-and-security-management-distance-learning |
| 26 | Msc Criminal Psychology and Victimology Distance Learning | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-criminal-psychology-and-victimology-distance-learning |
| 27 | Msc Forensic Investigation | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-forensic-investigation |
| 28 | Msc Criminal Psychology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-criminal-psychology |
| 29 | Msc Economic Crime | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-economic-crime |
| 30 | Mn Adult Nursing | https://www.port.ac.uk/study/courses/postgraduate-taught/mn-adult-nursing |
| 31 | Mn Mental Health Nursing | https://www.port.ac.uk/study/courses/postgraduate-taught/mn-mental-health-nursing |
| 32 | Ma Film and Television Production | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-film-and-television-production |
| 33 | Msc Digital Economy | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-digital-economy |
| 34 | Msc Financial Technology | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-financial-technology |
| 35 | PgDip Senior Leadership (Senior Leader Apprenticeship) | https://www.port.ac.uk/study/courses/postgraduate-taught/pgdip-senior-leadership-senior-leader-apprenticeship |
| 36 | PgDip Senior Leader Apprenticeship (Educational Leadership and Management) | https://www.port.ac.uk/study/courses/postgraduate-taught/pgdip-senior-leader-apprenticeship-educational-leadership-and-management |
| 37 | PgDip Senior Leader Apprenticeship (Public Administration) (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/pgdip-senior-leader-apprenticeship-public-administration-distance-learning |
| 38 | Primary Education Studies - Postgraduate Teaching Apprenticeship with QTS | https://www.port.ac.uk/study/courses/postgraduate-taught/primary-education-studies-postgraduate-teaching-apprenticeship-with-qts |
| 39 | Secondary Education Studies - Postgraduate Teaching Apprenticeship with QTS | https://www.port.ac.uk/study/courses/postgraduate-taught/secondary-education-studies-postgraduate-teaching-apprenticeship-with-qts |
| 40 | PgCert Armed Forces Education, Training and Skills (Distance Learning) | https://www.port.ac.uk/study/courses/postgraduate-taught/pgcert-armed-forces-education-training-and-skills-distance-learning |
| 41 | Mpa Public Administration | https://www.port.ac.uk/study/courses/postgraduate-taught/mpa-public-administration |
| 42 | Executive Mba | https://www.port.ac.uk/study/courses/postgraduate-taught/executive-mba |
| 43 | Msc Construction Project Management Distance Learning | https://www.port.ac.uk/study/courses/postgraduate-taught/msc-construction-project-management-distance-learning |
| 44 | Dba Professional Doctorate in Business Administration Distance Learning | https://www.port.ac.uk/study/courses/postgraduate-taught/dba-professional-doctorate-in-business-administration-distance-learning |


> Source for all 183 PGT programs: [Course index — Master's and PGT](https://www.port.ac.uk/study/courses?level=Master%27s+and+Postgraduate+Taught) and sitemap (184 PGT base URLs after filtering).
> Note: 'PGT-other' includes MRes, MBA, DBA, MPA, MArch, DipRIBA — all legitimate PGT awards.

### 2.2 At least one program's full deep-dive — MA Architecture

| Field | Value |
|-------|-------|
| **Program** | MA Architecture |
| **URL** | https://www.port.ac.uk/study/courses/postgraduate-taught/ma-architecture |
| **Faculty** | Faculty of Creative and Cultural Industries |
| **School** | School of Architecture, Art and Design |
| **Award** | MA |
| **Mode** | Full-time / Part-time |
| **Application portal** | Direct via University (no UCAS for PGT) |
| **Entry requirements** | A good honours degree in a relevant subject, or equivalent professional experience. Portfolio may be required for some pathways. |
| **English language** | IELTS 6.5–7.0 (no component below 6.0) for most Master's |
| **Application fee** | None |
| **Funding** | See [PGT funding](https://www.port.ac.uk/study/masters-and-postgraduate-taught/fees-and-funding/scholarships-and-bursaries) |

### 2.3 Graduate admissions model

- **Decentralized** at the program level — each Master's program has its own entry requirements
- Application via direct online form through University portal
- Standard application fee: **none** (verified: "We don't charge an application fee for our postgraduate courses")
- PGR (PhD, MPhil, MD, ProfDoc) applications are separate: see [PhD application](https://www.port.ac.uk/study/postgraduate-research/research-degrees/phd)

### 2.4 PGR (Postgraduate Research) — note

The 39 "PhD and Postgraduate Research" count in the homepage filter refers to the **research-degree types** (PhD, MPhil, MD, MRes, ProfDoc) — not 39 individual research programs. Specific PhD projects are listed at [Explore our projects](https://www.port.ac.uk/study/postgraduate-research/research-degrees/phd/explore-our-projects) (~500+ funded project pages in sitemap). This document focuses on **taught** programs; PGR is out of scope here.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value |
|-----------|-------|
| Admissions site | https://www.port.ac.uk/study/undergraduate |
| Application portal | UCAS (https://www.ucas.com/) |
| Typical offer | 104–120 UCAS points (varies by course; some e.g. MPharm, BN require higher) |
| UCAS deadline (UK) | 31 January (equal consideration) — UCAS Extra available after |
| UCAS deadline (International) | 30 June (recommended); UCAS accepts applications until 30 June |
| Decision notification | Rolling, typically within weeks of application |
| Enrollment confirmation | After results day (firm/insurance choice system) |
| Financial-aid deadline | UK student loans via Student Finance England; deadlines ~May |
| SAT/ACT | Not required for UK applicants (UK uses UCAS tariff from A-levels/BTEC) |
| English language | See Section 3.2 |
| Interview policy | Course-specific (e.g. Nursing, Teaching, Healthcare have interviews) |
| Recommendation | One academic reference via UCAS |
| Personal statement | Required via UCAS |
| Portfolio | Course-specific (Architecture, Art & Design, Performance) |

### 3.2 Undergraduate English proficiency table (international applicants)

| Exam | Minimum (most UG) | Recommended | Notes |
|------|-------------------|-------------|-------|
| IELTS Academic | 6.0 (no component below 5.5) | 6.5+ | One Skill Retake accepted; IELTS Academic Online NOT accepted; UKVI IELTS required for pre-sessional/foundation |
| TOEFL iBT | 79 (R18, L17, S20, W17) | 91+ | TOEFL code 3234; not UKVI-recognised |
| PTE Academic | 54 (no component below 51) | 61+ | Acceptable for direct entry |
| Cambridge C1 Advanced | 169 (no component below 162) | 176+ | — |
| Duolingo English Test | 100 (no component below 90) | 110+ | — |
| LanguageCert Academic | 65 (no component below 60) | 70+ | — |
| Trinity College London (ISE) | ISE II — pass in all 4 components | ISE III | — |
| Oxford ELLT | 6 (no component below 5) | 7+ | — |
| Kaplan Test of English | 458 (no component below 427) | — | — |

> Source: [English language requirements](https://www.port.ac.uk/study/international-students/english-language-requirements) (verified 2026-07-08).
> Some courses (e.g. Nursing, Pharmacy, MPhys) require higher scores — check the individual course page.

### 3.3 Graduate — global rules

- **Decentralized** admissions — apply directly via [University portal](https://www.port.ac.uk/study/masters-and-postgraduate-taught/how-to-apply)
- Application fee: **none** ("We don't charge an application fee for our postgraduate courses")
- GRE/GMAT: not required for any PGT (verified by absence of requirement in PGT admissions pages)
- Standard English language: IELTS 6.5–7.0 (no component below 6.0) for most Master's
- TOEFL equivalent: 91 (R20, L20, S20, W20) for most PGT
- PhD/Research applications: see [How to apply for a research degree](https://www.port.ac.uk/study/postgraduate-research/how-to-apply)

### 3.4 International application deadlines (Sept 2026 entry)

**Portsmouth Campus:**
- Bangladesh, Iraq, Pakistan, Syria, Yemen: Apply by 22 Jun 2026; Deposit by 6 Jul; Conditions by 13 Jul
- Ghana, India, Iran, Kenya, Nepal, Nigeria, Sri Lanka, Uganda: Apply by 20 Jul; Deposit by 3 Aug; Conditions by 10 Aug
- Rest of the World: Apply by 3 Aug; Deposit by 10 Aug; Conditions by 24 Aug

**MRES/PGCE (separate):**
- MRes Humanities & Social Sciences: Apply by 31 Mar 2026
- MRes Science & Health: Apply by 30 Apr 2026
- MRes Creative Industries: Apply by 30 Apr 2026
- PGCE: Apply by 2 Apr 2026

**London Campus:**
- Bangladesh/Iraq/Pakistan/Syria/Yemen: Apply by 8 Jun 2026
- Ghana/India/Iran/Kenya/Nepal/Nigeria/Sri Lanka/Uganda: Apply by 6 Jul 2026
- Rest of World: Apply by 20 Jul 2026

> Source: [Application deadlines for international students](https://www.port.ac.uk/study/international-students/how-to-apply/application-deadlines) (verified 2026-07-08).

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost — Home (UK) students 2026/27

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Tuition fee (Home) | £9,250/year | Capped by UK government for standard UG |
| Tuition fee (Placement year) | £1,850 (20% of standard) | For sandwich/placement year |
| Accommodation (halls) | £115–£170/week | Varies by hall; halls from £115/wk |
| Food | £35–£40/week | Approximate housekeeping |
| Bills (gas/electric/water/internet) | £15–£20/week | — |
| Travel | £5–£10/week | Local travel |
| Books/equipment | Variable | Course-specific (e.g. Engineering tools) |

> Home fee is the same across all UG courses (capped by UK government). Source: [Tuition fees, living costs and other study costs](https://www.port.ac.uk/study/undergraduate/undergraduate-fees-and-student-finance/tuition-fees-living-costs-and-other-study-costs).

### 4.2 Undergraduate cost — International students 2026/27

| Academic Year | Tuition Fee | Placement Year Fee |
|---------------|-------------|---------------------|
| 2026/27 | **£17,900 – £20,000** | £2,990 – £20,000 |
| 2027/28 | TBC | TBC |

> Source: [Tuition fees for international students](https://www.port.ac.uk/study/international-students/tuition-fees) (verified 2026-07-08).
> Fee varies by course band (classroom vs lab vs clinical). Medical, Pharmacy, Dental have higher fees. Tuition fee is **fixed for the duration of the course** (from Sept 2025/26 onwards).
> **EU students** (from 2021/22 cohort): [Tuition fees for EU students](https://www.port.ac.uk/study/international-students/tuition-fees/tuition-fees-for-eu-students) — same as international band.

### 4.3 Postgraduate (taught) cost

PGT fees are **per-course** and listed on each course page. Typical range £8,000–£20,000+ per year for international students. UK/Home PGT fees vary by course (e.g. PGCE tuition varies by subject; MBA premium).

> Source: [PGT tuition fees and living expenses](https://www.port.ac.uk/study/masters-and-postgraduate-taught/fees-and-funding/tuition-fees-and-living-expenses) — "tuition fees vary depending on what you're studying. You can find the cost of tuition for your chosen subject by visiting the course page."

### 4.4 Postgraduate (research) cost

PGR (PhD) fees:
- UK/Home: ~£4,800/year (set annually)
- International: ~£17,900/year (band-dependent)
- Many funded PhD projects available — see [PhD scholarships](https://www.port.ac.uk/study/postgraduate-research/funding-your-research-degree/phd-scholarships)

### 4.5 Living costs (weekly estimate)

| Item | Cost/week |
|------|-----------|
| Rent | £75–£85 |
| Bills (gas/electric/water/internet) | £15–£20 |
| Food/housekeeping | £35–£40 |
| Travel | £5–£10 |
| Phone | £5–£10 |
| TV licence | £3 |
| Contents insurance | £2–£3 |
| Social | £30–£40 |
| **Total per week** | **£170–£211** |
| **Total per academic year (40 weeks)** | **£6,800–£8,440** |

> Source: [PGT tuition fees and living expenses](https://www.port.ac.uk/study/masters-and-postgraduate-taught/fees-and-funding/tuition-fees-and-living-expenses) — verified 2026-07-08.

### 4.6 Scholarships & financial aid

- UG: see [Scholarships and bursaries](https://www.port.ac.uk/study/undergraduate/undergraduate-fees-and-student-finance/scholarships-and-bursaries) — includes NHS Learning Support Fund, Sanctuary Scholarship, Portsmouth FC Partnership, Estée Lauder Whitman Scholarship.
- PGT: [PGT scholarships and bursaries](https://www.port.ac.uk/study/masters-and-postgraduate-taught/fees-and-funding/scholarships-and-bursaries)
- PGR: [PhD scholarships](https://www.port.ac.uk/study/postgraduate-research/funding-your-research-degree/phd-scholarships) and [SCDTP Bursaries](https://www.port.ac.uk/study/postgraduate-research/funding-your-research-degree/scdtp-bursary)
- International: [Scholarships for international students](https://www.port.ac.uk/study/international-students/funding/scholarships)
- American students: [American loans](https://www.port.ac.uk/study/international-students/funding/american-loans)

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.programs.total_count
  value: 230
  source_url: https://www.port.ac.uk/study/courses?level=Undergraduate
  source_snippet: "Undergraduate (230 Results)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.programs.sitemap_base_urls
  value: 233
  source_url: https://www.port.ac.uk/sitemap.xml?page=1
  source_snippet: "https://www.port.ac.uk/study/courses/undergraduate/<slug> entries (filtered to base URLs)"
  capture_date: 2026-07-08
  evidence_type: sitemap

E-G-001:
  field: graduate.programs.total_count
  value: 184
  source_url: https://www.port.ac.uk/study/courses?level=Master%27s+and+Postgraduate+Taught
  source_snippet: "Master's and Postgraduate Taught (184 Results)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PGR-001:
  field: research.programs.total_count
  value: 39
  source_url: https://www.port.ac.uk/study/courses?level=PhD+and+Postgraduate+Research
  source_snippet: "PhD and Postgraduate Research (39 Results)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-COST-001:
  field: undergraduate.international_fee.2026_27
  value: "£17,900 – £20,000"
  source_url: https://www.port.ac.uk/study/international-students/tuition-fees
  source_snippet: "2026/27 | £17,900 – £20,000 | £2,990 – £20,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-COST-002:
  field: undergraduate.home_fee.2026_27
  value: "£9,250"
  source_url: https://www.port.ac.uk/study/undergraduate/undergraduate-fees-and-student-finance/tuition-fees-living-costs-and-other-study-costs
  source_snippet: "UK full-time undergraduate fees are capped at £9,250 per year (gov't regulation)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-001:
  field: english.ielts.ug_minimum
  value: "6.0 (no component below 5.5)"
  source_url: https://www.port.ac.uk/study/international-students/english-language-requirements
  source_snippet: "For most of our Bachelor's degrees, you need a minimum of IELTS band 6.0, with no component below 5.5."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-002:
  field: english.ielts.pgt_minimum
  value: "6.5–7.0 (no component below 6.0)"
  source_url: https://www.port.ac.uk/study/international-students/english-language-requirements
  source_snippet: "For most of our Master's degrees, you need a minimum of IELTS band 6.5–7.0, with no component below 6.0."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-003:
  field: english.toefl.ug_minimum
  value: "79 (R18, L17, S20, W17)"
  source_url: https://www.port.ac.uk/study/international-students/english-language-requirements
  source_snippet: "For most of our Bachelor's degrees, you need a score of 79 with a minimum of: 18 in Reading, 17 in Listening, 20 in Speaking, 17 in Writing"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-004:
  field: english.toefl.pgt_minimum
  value: "91 (R20, L20, S20, W20)"
  source_url: https://www.port.ac.uk/study/international-students/english-language-requirements
  source_snippet: "For most of our Master's degrees, you need a score of 91 with a minimum of: 20 in Reading, ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-STRUCT-001:
  field: institution.faculties
  value: ["Faculty of Business and Law", "Faculty of Creative and Cultural Industries", "Faculty of Humanities and Social Sciences", "Faculty of Science and Health", "Faculty of Technology"]
  source_url: https://www.port.ac.uk/about-us/structure-and-governance/organisational-structure/our-academic-structure
  source_snippet: "The University comprises of five faculties, each with their own schools and departments"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-DEADLINE-001:
  field: international.deadline.pgt_sept2026
  value: "Apply by 3 Aug 2026 (Rest of World, Portsmouth Campus); Deposit by 10 Aug; Conditions by 24 Aug"
  source_url: https://www.port.ac.uk/study/international-students/how-to-apply/application-deadlines
  source_snippet: "Applicants from the Rest of the World — Deadline for new applications: 3 August 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-FUND-001:
  field: graduate.funding.no_application_fee
  value: "None (free)"
  source_url: https://www.port.ac.uk/study/masters-and-postgraduate-taught/fees-and-funding/tuition-fees-and-living-expenses
  source_snippet: "We don't charge an application fee for our postgraduate courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-FUND-002:
  field: graduate.living_costs.weekly
  value: "£170–£211/week; £6,800–£8,440/academic year (40 weeks)"
  source_url: https://www.port.ac.uk/study/masters-and-postgraduate-taught/fees-and-funding/tuition-fees-and-living-expenses
  source_snippet: "Total per week: £170-£211; Total per academic year (40 weeks): £6,800 – £8,440"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

Tree: `university-of-portsmouth-knowledge-base-v2` → documents → chunks by degree (since per-faculty attribution is not reliable from the index).

```
collection: university-of-portsmouth-knowledge-base-v2
├── document: institution_overview
│   ├── chunk: counts (UG/PGT/PGR totals, faculty count)
│   ├── chunk: hierarchy (5 faculties + 14 schools tree)
│   ├── chunk: degree_inventory (all degree types)
│   └── chunk: distribution_matrix
├── document: undergraduate_programs
│   ├── chunk: ug-ba (82 programs)
│   ├── chunk: ug-bsc (92 programs)
│   ├── chunk: ug-beng (21 programs)
│   ├── chunk: ug-other (LLB, BN, MPharm, MPhys, FdA, HNC, etc.)
│   └── chunk: ug-joint (BA/BS, BS/MPhys dual)
├── document: postgraduate_taught_programs
│   ├── chunk: pgt-ma (35 programs)
│   ├── chunk: pgt-msc (85 programs)
│   ├── chunk: pgt-mba (6 programs)
│   ├── chunk: pgt-other (LLM, MArch, MPA, MRes, DBA, MN, DipRIBA)
│   └── chunk: pgt-unparsed (44 programs — names inferred from URL, see quality notes)
├── document: application_requirements
│   ├── chunk: ug_admissions (UCAS deadlines, typical offers)
│   ├── chunk: english_language (IELTS, TOEFL, PTE, Cambridge, Duolingo, etc.)
│   └── chunk: international_deadlines (regional buckets)
├── document: costs_financial_aid
│   ├── chunk: ug_home_fee (£9,250 capped)
│   ├── chunk: ug_intl_fee (£17,900–£20,000)
│   ├── chunk: pgt_fees (per-course)
│   ├── chunk: living_costs (weekly breakdown)
│   └── chunk: scholarships (UG/PGT/PGR/intl)
└── document: monitoring_watchlist
    ├── chunk: high_frequency (tuition, deadlines, language requirements)
    ├── chunk: medium_frequency (program lists, scholarships)
    └── chunk: low_frequency (faculty structure, university overview)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "university-of-portsmouth-knowledge-base-v2"
  school: "<home college — if known, else 'unallocated'>"
  department: "<home department — if known, else 'unallocated'>"
  degree_level: "<BA|BS|BEng|LLB|BN|MPharm|MPhys|MComp|FdA|HNC|MA|MS|MBA|MRes|LLM|MArch|MPA|DBA|MN|Dip|other>"
  level: undergraduate | postgraduate_taught | postgraduate_research
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | faculty
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
  region: uk
  institution: University of Portsmouth
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| **P0** | Per-program fee (international band) for each UG + PGT course | each course page under `/study/courses/undergraduate/<slug>` and `/study/courses/postgraduate-taught/<slug>` |
| **P0** | Per-program English language score (often higher than the default 6.0/6.5) | each course page's "Entry requirements" section |
| **P0** | Faculty attribution for each of the 413 programs | breadcrumbs or "School" tag on each course page |
| **P1** | UK/Home PGT fees (per-course) | individual course pages |
| **P1** | PhD project list with funding status | `/study/postgraduate-research/research-degrees/phd/explore-our-projects` |
| **P1** | Department-level academic structure (more granular than "school") | `/about-us/structure-and-governance/organisational-structure/our-academic-structure` (deeper) |
| **P2** | Course-specific scholarships (programme-tied) | individual course pages |
| **P2** | Clearing availability per course | each UG course page |
| **P3** | Bursary amounts and eligibility criteria (more detail) | each scholarship page |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Portsmouth | (Other UK uni slot) |
|-----------|--------------------------|---------------------|
| **Region** | UK (England) | — |
| **Total UG programs** | 230 | — |
| **Total PGT programs** | 183 | — |
| **PGR research types** | 39 (PhD, MPhil, MD, MRes, ProfDoc) | — |
| **Faculties / Schools** | 5 / 14 | — |
| **UG international fee (2026/27)** | £17,900–£20,000 | — |
| **UG home fee** | £9,250 (capped) | — |
| **Application fee (PGT)** | None (free) | — |
| **IELTS UG minimum** | 6.0 (no band < 5.5) | — |
| **IELTS PGT minimum** | 6.5–7.0 (no band < 6.0) | — |
| **TOEFL UG** | 79 (R18 L17 S20 W17) | — |
| **TOEFL PGT** | 91 (R20 L20 S20 W20) | — |
| **PGT application deadline (RoW)** | 3 Aug 2026 (Sept 2026 entry) | — |
| **Modern University of the Year** | 2025–2026 (Times/Sunday Times) | — |
| **Russell Group?** | No (Modern/post-1992) | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: port.ac.uk (course index, sitemap, faculty pages, tuition fees, English language, deadlines)
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch for sitemap
> **Granularity**: school → department → degree-level → program
