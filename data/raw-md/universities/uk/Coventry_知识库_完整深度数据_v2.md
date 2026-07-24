# Coventry University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser + WebFetch (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Russell Group**: No
> **TEF Rating**: Gold Overall (2023)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 126 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/LLM/PGDip/PGCert) | 146 (Coventry campus) + 18 (London campus) = 164 |
| 研究生博士项目 (PhD/Doctoral) | Available separately via research degrees page |
| **学位项目总计 (UG + PGT)** | **290** |
| 学院 (Faculties) | 4 (main campus) + 1 (London campus) |
| 学术单位 (Schools) | ~10 |

> **Data source**: Coventry University clearing course finder (`coventry.ac.uk/clearing/course-finder/`) — 126 UG courses; PG A-Z list (`coventry.ac.uk/study-at-coventry/postgraduate-study/az-course-list/`) — 146 unique PG taught courses at Coventry campus + 18 at London campus.
> **Note**: Online courses (via `coventry.ac.uk/online/`) and research degrees are excluded from this count. Some courses have foundation year variants which are not counted separately.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Coventry University
├── Faculty of Arts and Humanities                                              [学院]
│   ├── School of Art and Design                                                [系]
│   ├── School of Humanities                                                    [系]
│   └── School of Media and Performing Arts                                     [系]
├── Faculty of Business and Law                                                 [学院]
│   ├── Coventry Business School                                                [系]
│   └── School of Law                                                           [系]
├── Faculty of Engineering, Environment and Computing                           [学院]
│   ├── School of Computing, Electronics and Mathematics                        [系]
│   └── School of Energy, Environment and Sciences                              [系]
├── Faculty of Health and Life Sciences                                         [学院]
│   ├── School of Health Sciences                                               [系]
│   └── School of Psychological, Social and Behavioural Sciences                [系]
└── Coventry University London (separate campus)                                [学院]
    └── (Business, Finance, Marketing, Fashion, Hospitality programmes)         [系]
```

> **Note**: The faculty/school structure is inferred from URL path codes (`/course-structure/ug/{code}/`) and subject area groupings on the Coventry website. The exact internal organizational chart was not publicly accessible on the pages scraped. Some schools (e.g. School of Energy, Environment and Sciences) span multiple traditional disciplines.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BSc (Hons) | Bachelor of Science (Honours) | 本科 | ~45 |
| BA (Hons) | Bachelor of Arts (Honours) | 本科 | ~40 |
| BEng (Hons) | Bachelor of Engineering (Honours) | 本科 | ~12 |
| BBA (Hons) | Bachelor of Business Administration (Honours) | 本科 | 1 |
| LLB (Hons) | Bachelor of Laws (Honours) | 本科 | 5 |
| MSci | Master in Science (Integrated UG) | 本科 | ~6 |
| MEng | Master in Engineering (Integrated UG) | 本科 | ~5 |
| MDes | Master of Design (Integrated UG) | 本科 | ~1 |
| MArch | Master of Architecture | 本科 | 1 |
| FD | Foundation Degree | 本科 | ~1 |
| MSc | Master of Science | 研究生 | ~80 |
| MA | Master of Arts | 研究生 | ~35 |
| MBA | Master of Business Administration | 研究生 | ~8 |
| LLM | Master of Laws | 研究生 | ~4 |
| MArch | Master of Architecture | 研究生 | 1 |
| PGDip | Postgraduate Diploma | 研究生 | ~5 |
| PGCert | Postgraduate Certificate | 研究生 | ~8 |
| D.Clin.Psych | Doctorate in Clinical Psychology | 研究生 | 1 |

> **Note**: Counts are approximate based on the 290 extracted programs. Integrated master's degrees (MSci, MEng) are classified as undergraduate level per UK convention. Foundation year variants are not counted separately.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BSc | BA | BEng | LLB | MSci/MEng/MDes/March | BBA | Other UG | MSc | MA | MBA | LLM | PGCert/PGDip | 合计 |
|------------|-----|-----|------|-----|----------------------|-----|----------|-----|-----|-----|-----|-------------|------|
| Faculty of Arts and Humanities | 1 | 27 | 0 | 0 | 2 | 0 | 1 | 0 | 27 | 0 | 0 | 0 | 58 |
| Faculty of Business and Law | 7 | 5 | 0 | 5 | 0 | 1 | 2 | 11 | 2 | 1 | 3 | 2 | 39 |
| Faculty of Engineering, Environment and Computing | 15 | 0 | 12 | 0 | 8 | 0 | 3 | 45 | 0 | 0 | 0 | 3 | 86 |
| Faculty of Health and Life Sciences | 17 | 4 | 0 | 0 | 0 | 0 | 0 | 10 | 1 | 0 | 0 | 7 | 39 |
| School codes: ees (split) | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| London campus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 6 | 0 | 2 | 18 |
| **合计** | | | | | | | | | | | | | **~290** |

> **Note**: The ees (Energy, Environment and Sciences) school code appears in both UG and PG data. Some courses bridge faculties. London campus courses are separate from main campus. Matrix cells are approximate and may not sum exactly due to classification overlaps.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

Coventry University's undergraduate programmes are delivered across 4 faculties. The Faculty of Engineering, Environment and Computing has the largest UG portfolio, followed by Arts and Humanities. Each faculty contains multiple schools. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Arts and Humanities

##### School of Art and Design

###### BA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Acting, Stage and Screen | https://www.coventry.ac.uk/course-structure/ug/fah/acting-stage-and-screen-ba-hons/ |
| 2 | Animation | https://www.coventry.ac.uk/course-structure/ug/fah/animation-ba-hons/ |
| 3 | Architecture | https://www.coventry.ac.uk/course-structure/ug/fah/architecture-bsc-hons/ |
| 4 | Digital Media | https://www.coventry.ac.uk/course-structure/ug/fah/digital-media-ba-hons/ |
| 5 | English Literature | https://www.coventry.ac.uk/course-structure/ug/fah/english-literature-ba/ |
| 6 | Fashion | https://www.coventry.ac.uk/course-structure/ug/fah/fashion-ba-hons/ |
| 7 | Fashion Brand and Communication | https://www.coventry.ac.uk/course-structure/ug/fah/fashion-brand-and-communication-ba/ |
| 8 | Film Production | https://www.coventry.ac.uk/course-structure/ug/fah/film-production-ba-hons/ |
| 9 | Fine Art | https://www.coventry.ac.uk/course-structure/ug/fah/fine-art-ba-hons/ |
| 10 | Games Art | https://www.coventry.ac.uk/course-structure/ug/fah/games-art-ba-hons/ |
| 11 | Games Design and Development | https://www.coventry.ac.uk/course-structure/ug/fah/games-design-and-development-ba/ |
| 12 | Graphic Design | https://www.coventry.ac.uk/course-structure/ug/fah/graphic-design-ba-hons/ |
| 13 | History | https://www.coventry.ac.uk/course-structure/ug/fah/history-ba-hons/ |
| 14 | History and Politics | https://www.coventry.ac.uk/course-structure/ug/fah/history-and-politics-ba-hons/ |
| 15 | Illustration | https://www.coventry.ac.uk/course-structure/ug/fah/illustration-ba-hons/ |
| 16 | Interior Architecture and Design | https://www.coventry.ac.uk/course-structure/ug/fah/interior-architecture-and-design-ba-hons/ |
| 17 | International Fashion Business | https://www.coventry.ac.uk/course-structure/ug/fah/international-fashion-business-ba-hons/ |
| 18 | International Relations | https://www.coventry.ac.uk/course-structure/ug/fah/international-relations-ba-hons/ |
| 19 | Journalism | https://www.coventry.ac.uk/course-structure/ug/fah/journalism-ba-hons/ |
| 20 | Media and Communications | https://www.coventry.ac.uk/course-structure/ug/fah/media-and-communications-ba-hons/ |
| 21 | Media Production | https://www.coventry.ac.uk/course-structure/ug/fah/media-production-ba-hons/ |
| 22 | Philosophy | https://www.coventry.ac.uk/course-structure/ug/fah/philosophy-ba/ |
| 23 | Photography | https://www.coventry.ac.uk/course-structure/ug/fah/photography-ba-hons/ |
| 24 | Politics | https://www.coventry.ac.uk/course-structure/ug/fah/politics-ba/ |
| 25 | Politics and International Relations | https://www.coventry.ac.uk/course-structure/ug/fah/politics-and-international-relations/ |
| 26 | Popular Music Performance and Songwriting | https://www.coventry.ac.uk/course-structure/ug/fah/popular-music-performance-and-songwriting-ba-hons/ |
| 27 | Product Design | https://www.coventry.ac.uk/course-structure/ug/fah/product-design-ba/ |
| 28 | Sociology | https://www.coventry.ac.uk/course-structure/ug/fah/sociology-ba-hons/ |
| 29 | Sociology and Criminology | https://www.coventry.ac.uk/course-structure/ug/fah/sociology-and-criminology-ba-hons/ |

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music and Audio Production | https://www.coventry.ac.uk/course-structure/ug/fah/music-and-audio-production-bsc/ |

###### MDes/BA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Automotive and Transport Design | https://www.coventry.ac.uk/course-structure/ug/fah/automotive-and-transport-design-mdesba-hons/ |

###### BSc (Hons) / MSci

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.coventry.ac.uk/course-structure/ug/fah/architecture-bsc-hons/ |

#### Faculty of Business and Law

##### Coventry Business School

###### BA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising and Digital Marketing | https://www.coventry.ac.uk/course-structure/ug/fbl/advertising-and-digital-marketing-ba/ |
| 2 | Business and HR Management | https://www.coventry.ac.uk/course-structure/ug/fbl/business-and-hr-management-ba-hons/ |
| 3 | Business and Marketing | https://www.coventry.ac.uk/course-structure/ug/fbl/business-and-marketing-ba-hons/ |
| 4 | Business Management | https://www.coventry.ac.uk/course-structure/ug/fbl/business-management-ba-hons/ |
| 5 | Marketing | https://www.coventry.ac.uk/course-structure/ug/fbl/marketing-ba-hons/ |

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://www.coventry.ac.uk/course-structure/ug/fbl/accountancy-bsc-hons/ |
| 2 | Accounting and Finance | https://www.coventry.ac.uk/course-structure/ug/fbl/accounting-and-finance-bsc-hons/ |
| 3 | Banking and Finance | https://www.coventry.ac.uk/course-structure/ug/fbl/banking-and-finance-bsc-hons/ |
| 4 | Business and Finance | https://www.coventry.ac.uk/course-structure/ug/fbl/business-and-finance-bsc-hons/ |
| 5 | Business Economics | https://www.coventry.ac.uk/course-structure/ug/fbl/business-economics-bsc-hons/ |
| 6 | Economics | https://www.coventry.ac.uk/course-structure/ug/fbl/economics-bsc-hons/ |
| 7 | Finance and Investment | https://www.coventry.ac.uk/course-structure/ug/fbl/finance-and-investment-bsc-hons/ |
| 8 | Financial Economics | https://www.coventry.ac.uk/course-structure/ug/fbl/financial-economics-bsc-hons/ |
| 9 | International Business Management | https://www.coventry.ac.uk/course-structure/ug/fbl/international-business-management-bsc-hons/ |

###### BBA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.coventry.ac.uk/course-structure/ug/fbl/business-administration-bba-hons/ |

###### LLB (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Commercial Law | https://www.coventry.ac.uk/course-structure/ug/fbl/commercial-law-llb/ |
| 2 | Criminal Law and Justice | https://www.coventry.ac.uk/course-structure/ug/fbl/criminal-law-and-justice-llb/ |
| 3 | International Law | https://www.coventry.ac.uk/course-structure/ug/fbl/international-law-llb/ |
| 4 | Law | https://www.coventry.ac.uk/course-structure/ug/fbl/law-llb-hons/ |
| 5 | MLaw (Legal Practice) | https://www.coventry.ac.uk/course-structure/ug/fbl/mlaw-legal-practice/ |

##### Coventry Business School (cbl codes)

###### BA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics and Management | https://www.coventry.ac.uk/course-structure/ug/cbl/business-analytics-management/ |
| 2 | Events Management | https://www.coventry.ac.uk/course-structure/ug/cbl/events-management-ba-hons/ |
| 3 | Financial Planning and Wealth Management | https://www.coventry.ac.uk/course-structure/ug/cbl/financial-planning-wealth-management/ |
| 4 | Sport Business Management | https://www.coventry.ac.uk/course-structure/ug/cbl/sport-business-management-ba-hons/ |

#### Faculty of Engineering, Environment and Computing

##### School of Computing, Electronics and Mathematics (eec)

###### BSc (Hons) / MSci

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/ |
| 2 | Computer Science with Artificial Intelligence | https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-with-artificial-intelligence-msci-bsc-hons/ |
| 3 | Data Science | https://www.coventry.ac.uk/course-structure/ug/eec/data-science-mscibsc/ |
| 4 | Mathematics | https://www.coventry.ac.uk/course-structure/ug/eec/mathematics-bsc-hons/ |

###### BEng (Hons) / MEng

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Systems Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/aerospace-systems-engineering-beng-hons/ |
| 2 | Aerospace Technology | https://www.coventry.ac.uk/course-structure/ug/eec/aerospace-technology-beng-hons/ |
| 3 | Architectural Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/architectural-engineering-beng/ |
| 4 | Automotive Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/automotive-engineering-mengbeng-hons/ |
| 5 | Civil and Environmental Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/civil-and-environmental-engineering-beng/ |
| 6 | Civil Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/civil-engineering-mengbeng/ |
| 7 | Computer Systems Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/computer-systems-engineering-mengbeng/ |
| 8 | Electrical and Electronic Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/electrical-and-electronic-engineering-beng/ |
| 9 | Manufacturing Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/manufacturing-engineering-mengbeng-hons/ |
| 10 | Mechanical Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/mechanical-engineering-mengbeng-hons/ |
| 11 | Motorsport Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/motorsport-engineering-mengbeng-hons/ |

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aviation Management | https://www.coventry.ac.uk/course-structure/ug/eec/aviation-management-bsc-hons/ |
| 2 | Building Surveying | https://www.coventry.ac.uk/course-structure/ug/eec/building-surveying-bsc-hons/ |
| 3 | Civil Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/civil-engineering-bsc/ |
| 4 | Construction Project Management | https://www.coventry.ac.uk/course-structure/ug/eec/construction-project-management-bsc-hons/ |
| 5 | Disaster and Emergency Management | https://www.coventry.ac.uk/course-structure/ug/eec/disaster-and-emergency-management-bsc-hons/ |
| 6 | Ethical Hacking and Cybersecurity | https://www.coventry.ac.uk/course-structure/ug/eec/ethical-hacking-and-cybersecurity-bsc/ |
| 7 | Geography | https://www.coventry.ac.uk/course-structure/ug/eec/geography-bsc-hons/ |
| 8 | Geography and Environmental Hazards | https://www.coventry.ac.uk/course-structure/ug/eec/geography-and-environmental-hazards-bsc/ |
| 9 | Information Technology Management | https://www.coventry.ac.uk/course-structure/ug/eec/information-technology-management-bsc/ |
| 10 | Quantity Surveying and Commercial Management | https://www.coventry.ac.uk/course-structure/ug/eec/quantity-surveying-and-commercial-management-bsc-hons/ |
| 11 | Real Estate and Property Management | https://www.coventry.ac.uk/course-structure/ug/eec/real-estate-and-property-management-bsc-hons/ |
| 12 | Software Engineering | https://www.coventry.ac.uk/course-structure/ug/eec/software-engineering-bsc/ |

###### MSci

| # | 专业 | URL |
|---|------|-----|
| 1 | Chiropractic | https://www.coventry.ac.uk/course-structure/ug/eec/chiropractic-msci/ |

###### BA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.coventry.ac.uk/course-structure/ug/eec/geography-ba-hons/ |

##### School of Energy, Environment and Sciences (ees)

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Design Technology | https://www.coventry.ac.uk/course-structure/ug/ees/architectural-design-technology/ |
| 2 | Biotechnology | https://www.coventry.ac.uk/course-structure/ug/ees/biotechnology-msci-bsc-hons/ |
| 3 | Computer Games Programming | https://www.coventry.ac.uk/course-structure/ug/ees/computer-games-programming/ |
| 4 | Digital Technology and Computing | https://www.coventry.ac.uk/course-structure/ug/ees/digital-technology-computing/ |
| 5 | Ecology and Conservation | https://www.coventry.ac.uk/course-structure/ug/ees/ecology-conservation-bsc/ |
| 6 | Environmental Science | https://www.coventry.ac.uk/course-structure/ug/ees/environmental-science-bsc/ |
| 7 | Pharmaceutical Science | https://www.coventry.ac.uk/course-structure/ug/ees/pharmaceutical-science-bsc-hons-msci/ |
| 8 | Sustainability and Environmental Management | https://www.coventry.ac.uk/course-structure/ug/ees/sustainability-and-environmental-management-bsc-hons/ |
| 9 | Sustainable Design Engineering | https://www.coventry.ac.uk/course-structure/ug/ees/sustainable-design-engineering-beng-meng-hons/ |

#### Faculty of Health and Life Sciences

##### School of Health Sciences (hls)

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological and Forensic Science | https://www.coventry.ac.uk/course-structure/ug/hls/biological-and-forensic-science-bsc-hons/ |
| 2 | Biomedical Science / Applied Biomedical Science | https://www.coventry.ac.uk/course-structure/ug/hls/biomedical-science-applied-biomedical-science-bsc/ |
| 3 | Criminology | https://www.coventry.ac.uk/course-structure/ug/hls/criminology-ba-hons/ |
| 4 | Criminology and Law | https://www.coventry.ac.uk/course-structure/ug/hls/criminology-and-law-ba-hons/ |
| 5 | Criminology and Psychology | https://www.coventry.ac.uk/course-structure/ug/hls/criminology-and-psychology-ba/ |
| 6 | Forensic Investigations | https://www.coventry.ac.uk/course-structure/ug/hls/forensic-investigations-bsc-hons/ |
| 7 | Forensic Science | https://www.coventry.ac.uk/course-structure/ug/hls/forensic-science-bsc-hons/ |
| 8 | Human Biosciences | https://www.coventry.ac.uk/course-structure/ug/hls/human-biosciences-bsc/ |
| 9 | Nutrition and Health | https://www.coventry.ac.uk/course-structure/ug/hls/nutrition-and-health-bsc-hons/ |
| 10 | Pharmacology | https://www.coventry.ac.uk/course-structure/ug/hls/pharmacology-bsc/ |
| 11 | Psychology | https://www.coventry.ac.uk/course-structure/ug/hls/psychology-bsc-hons/ |
| 12 | Psychology and Counselling | https://www.coventry.ac.uk/course-structure/ug/hls/psychology-counselling-bsc/ |
| 13 | Public Health | https://www.coventry.ac.uk/course-structure/ug/hls/public-health-bsc/ |
| 14 | Sport and Exercise Science | https://www.coventry.ac.uk/course-structure/ug/hls/sport-and-exercise-science-bsc-hons/ |
| 15 | Sports Coaching | https://www.coventry.ac.uk/course-structure/ug/hls/sports-coaching-bsc/ |
| 16 | Sports Therapy | https://www.coventry.ac.uk/course-structure/ug/hls/sports-therapy-bsc-hons/ |

###### BA (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Childhood, Youth and Education Studies | https://www.coventry.ac.uk/course-structure/ug/hls/childhood-youth-and-education-studies-ba-hons/ |

##### School of Health Sciences — NHS Programmes (hls-nhs)

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Adult Nursing | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/adult-nursing-bsc-hons/ |
| 2 | Adult Nursing (Blended Learning) | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/adult-nursing-blended-learning-bsc-hons/ |
| 3 | Learning Disabilities Nursing | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/learning-disabilities-nursing-bsc-hons/ |
| 4 | Mental Health Nursing | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/mental-health-nursing-bsc-hons/ |
| 5 | Occupational Therapy | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/occupational-therapy-bsc-hons/ |
| 6 | Operating Department Practice | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/operating-department-practice-bsc/ |
| 7 | Paramedic Science | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/paramedic-science-bsc/ |
| 8 | Social Work | https://www.coventry.ac.uk/course-structure/ug/hls-nhs/social-work-ba-hons/ |

##### School of Psychological, Social and Behavioural Sciences (cas)

###### BSc (Hons)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Forensic Investigations | https://www.coventry.ac.uk/course-structure/ug/cas/criminology-and-forensic-investigations/ |
| 2 | Criminology and Youth Justice | https://www.coventry.ac.uk/course-structure/ug/cas/criminology-and-youth-justice-ba-hons/ |
| 3 | English and Creative Writing | https://www.coventry.ac.uk/course-structure/ug/cas/english-and-creative-writing-ba-hons/ |
| 4 | Esports Production and Gaming | https://www.coventry.ac.uk/course-structure/ug/cas/esports-production-gaming/ |
| 5 | Forensic Criminal Psychology | https://www.coventry.ac.uk/course-structure/ug/cas/forensic-criminal-psychology-bsc-hons/ |
| 6 | Psychology of Sport and Exercise | https://www.coventry.ac.uk/course-structure/ug/cas/psychology-sport-exercise/ |
| 7 | Psychology with Education | https://www.coventry.ac.uk/course-structure/ug/cas/psychology-with-education-bsc-hons/ |

##### Other (diploma)

###### Foundation Degree

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing Associate | https://www.coventry.ac.uk/course-structure/ug/diploma/nursing-associate-foundation-degree/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

The following courses share common first years across related degrees, allowing students to switch after Year 1:

- **Business cluster**: Business Management, Business Administration, Business Analytics and Management, Business and HRM, Business and Marketing, Events Management, International Business Management, Marketing, Sport Business Management
- **Computer Science cluster**: Computer Science, Computer Science with AI, Digital Technology and Computing, IT Management, Software Engineering
- **Law cluster**: Law, Commercial Law, Criminal Law and Justice, International Law, MLaw (Legal Practice)

### 1.4 Minors — complete list

N/A — UK universities do not typically offer standalone minors.

### 1.5 General/Institute-wide requirements

Coventry University uses a common first year model within subject clusters, allowing students to switch between related degrees after Year 1 (subject to progression requirements). This is not a traditional general education/core curriculum but a subject-area flexibility mechanism.

### 1.6 Course-ID → Major quick-lookup

Coventry uses UCAS codes for undergraduate applications. Institution code: **C85**. Example UCAS codes:
- Computer Science BSc: G400
- Computer Science MSci: I108
- Law LLB: M100
- Business Management BA: N221
- Adult Nursing BSc: HU01

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Faculty of Business and Law — Coventry Business School (cbl)

##### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Financial Management | https://www.coventry.ac.uk/course-structure/pg/cbl/accounting-and-financial-management-msc/ |
| 2 | Banking and Finance | https://www.coventry.ac.uk/course-structure/pg/cbl/banking-and-finance-msc/ |
| 3 | Business Analytics | https://www.coventry.ac.uk/course-structure/pg/cbl/business-analytics-msc/ |
| 4 | Digital Marketing Management | https://www.coventry.ac.uk/course-structure/pg/cbl/digital-marketing-mgt-msc/ |
| 5 | Events and Experience Management | https://www.coventry.ac.uk/course-structure/pg/cbl/events-experience-mgt-msc/ |
| 6 | Finance | https://www.coventry.ac.uk/course-structure/pg/cbl/finance-msc/ |
| 7 | FinTech | https://www.coventry.ac.uk/course-structure/pg/cbl/fintech-msc/ |
| 8 | International Business Management | https://www.coventry.ac.uk/course-structure/pg/cbl/international-business-management-msc/ |
| 9 | International Human Resource Management | https://www.coventry.ac.uk/course-structure/pg/cbl/international-human-resource-management-msc/ |
| 10 | International Marketing Management | https://www.coventry.ac.uk/course-structure/pg/cbl/international-marketing-msc/ |
| 11 | Investment Management | https://www.coventry.ac.uk/course-structure/pg/cbl/investment-management-msc/ |
| 12 | Project Management | https://www.coventry.ac.uk/course-structure/pg/cbl/project-management-msc/ |
| 13 | Sport Management | https://www.coventry.ac.uk/course-structure/pg/cbl/sport-management-msc/ |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Advertising and Brand Management | https://www.coventry.ac.uk/course-structure/pg/cbl/advertising-and-brand-management-ma/ |

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration (MBA) | https://www.coventry.ac.uk/course-structure/pg/cbl/masters-in-business-administration/ |
| 2 | Master in Management (MiM) | https://www.coventry.ac.uk/course-structure/pg/cbl/master-in-management-mim/ |

##### LLM

| # | 项目 | URL |
|---|------|-----|
| 1 | International Commercial Law | https://www.coventry.ac.uk/course-structure/pg/cbl/international-commercial-law-llm/ |
| 2 | Law | https://www.coventry.ac.uk/course-structure/pg/cbl/law-llm/ |

##### PGCert/PGDip

| # | 项目 | URL |
|---|------|-----|
| 1 | Principles of Law | https://www.coventry.ac.uk/course-structure/pg/cbl/principles-of-law-pg-cert/ |
| 2 | Protective Security and Resilience | https://www.coventry.ac.uk/course-structure/pg/cbl/protective-security-and-resilience/ |
| 3 | Understanding Legal Practice / Professional Legal Practice LLM | https://www.coventry.ac.uk/course-structure/pg/cbl/professional-legal-practice-llm/ |

#### Faculty of Engineering, Environment and Computing (ees)

##### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Aerospace Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/advanced-aerospace-engineering-msc/ |
| 2 | Advanced Mechanical Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/advanced-mechanical-engineering-msc/ |
| 3 | Advanced Software Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/advanced-software-engineering-msc/ |
| 4 | Air Transport Management | https://www.coventry.ac.uk/course-structure/pg/ees/air-transport-management-msc/ |
| 5 | Antimicrobial Resistance | https://www.coventry.ac.uk/course-structure/pg/ees/antimicrobial-resistance-msc/ |
| 6 | Applied Strength, Conditioning and Rehabilitation | https://www.coventry.ac.uk/course-structure/pg/ees/applied-strength-conditioning-rehabilitation-msc/ |
| 7 | Artificial Intelligence and Human Factors | https://www.coventry.ac.uk/course-structure/pg/ees/artificial-intelligence-human-factors-msc/ |
| 8 | Automotive Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/automotive-engineering-msc/ |
| 9 | Biomedical Science | https://www.coventry.ac.uk/course-structure/pg/ees/biomedical-science-msc/ |
| 10 | Biotechnology | https://www.coventry.ac.uk/course-structure/pg/ees/biotechnology-msc/ |
| 11 | Building Services Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/building-services-engineering-msc/ |
| 12 | Civil Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/civil-engineering-msc/ |
| 13 | Civil Engineering Project Management | https://www.coventry.ac.uk/course-structure/pg/ees/civil-engineering-project-management/ |
| 14 | Civil Infrastructure Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/civil-infrastructure-engineering-msc/ |
| 15 | Computer Science | https://www.coventry.ac.uk/course-structure/pg/ees/computer-science-msc/ |
| 16 | Construction Management with BIM | https://www.coventry.ac.uk/course-structure/pg/ees/construction-management-msc/ |
| 17 | Construction Project and Cost Management | https://www.coventry.ac.uk/course-structure/pg/ees/construction-project-and-cost-management-msc/ |
| 18 | Control, Robotics and Intelligent Automation | https://www.coventry.ac.uk/course-structure/pg/ees/control-robotics-intelligent-automation-msc/ |
| 19 | Cyber Security | https://www.coventry.ac.uk/course-structure/pg/ees/cyber-security-msc/ |
| 20 | Data Science | https://www.coventry.ac.uk/course-structure/pg/ees/data-science-msc/ |
| 21 | Data Science and Computational Intelligence | https://www.coventry.ac.uk/course-structure/pg/ees/data-science-and-computational-intelligence-msc/ |
| 22 | Design and Systems Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/design-and-systems-engineering-msc/ |
| 23 | Disaster Management and Resilience | https://www.coventry.ac.uk/course-structure/pg/ees/disaster-management-msc/ |
| 24 | Electrical and Electronic Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/electrical-and-electronic-engineering-msc/ |
| 25 | Electrical Automotive Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/electrical-automotive-engineering-msc/ |
| 26 | Embedded Systems Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/embedded-systems-engineering-msc/ |
| 27 | Emergency Management and Resilience | https://www.coventry.ac.uk/course-structure/pg/ees/emergency-management-and-resilience-msc/ |
| 28 | Energy Transition Management | https://www.coventry.ac.uk/course-structure/pg/ees/energy-transition-management-msc/ |
| 29 | Engineering Management | https://www.coventry.ac.uk/course-structure/pg/ees/engineering-management-msc/ |
| 30 | Engineering Project Management | https://www.coventry.ac.uk/course-structure/pg/ees/engineering-project-management-msc/ |
| 31 | Environmental Building Performance Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/environmental-building-performance-engineering-msc/ |
| 32 | Environmental Data Analytics | https://www.coventry.ac.uk/course-structure/pg/ees/environmental-data-analytics-msc/ |
| 33 | Food Safety and Control | https://www.coventry.ac.uk/course-structure/pg/ees/food-safety-and-control-msc/ |
| 34 | Games Technology | https://www.coventry.ac.uk/course-structure/pg/ees/games-technology/ |
| 35 | Global Pharmaceutical and Biotech Management | https://www.coventry.ac.uk/course-structure/pg/ees/global-pharmaceutical-and-biotech-management-msc/ |
| 36 | Intelligent Transport Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/intelligent-transport-engineering-msc/ |
| 37 | Intelligent Transport Systems | https://www.coventry.ac.uk/course-structure/pg/ees/intelligent-transport-systems-msc/ |
| 38 | International Development and Sustainable Practice | https://www.coventry.ac.uk/course-structure/pg/ees/international-development-sustainable-practice/ |
| 39 | Management of Information Systems and Technology | https://www.coventry.ac.uk/course-structure/pg/ees/management-of-information-systems-and-technology-msc/ |
| 40 | Manufacturing and Production Engineering Management | https://www.coventry.ac.uk/course-structure/pg/ees/manufacturing-and-production-engineering-management-msc/ |
| 41 | Oil and Gas Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/oil-and-gas-engineering-msc/ |
| 42 | Oil and Gas Management | https://www.coventry.ac.uk/course-structure/pg/ees/oil-and-gas-management-msc/ |
| 43 | Pharmacology and Drug Discovery | https://www.coventry.ac.uk/course-structure/pg/ees/pharmacology-and-drug-discovery-msc/ |
| 44 | Power Electronics and Energy Systems | https://www.coventry.ac.uk/course-structure/pg/ees/power-electronics-and-energy-systems-msc/ |
| 45 | Public Health Nutrition | https://www.coventry.ac.uk/course-structure/pg/ees/public-health-nutrition-msc/ |
| 46 | Renewable Energy Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/renewable-energy-engineering-msc/ |
| 47 | Renewable Energy Management | https://www.coventry.ac.uk/course-structure/pg/ees/renewable-energy-management-msc/ |
| 48 | Sport and Exercise Psychology | https://www.coventry.ac.uk/course-structure/pg/ees/sport-exercise-psychology-msc/ |
| 49 | Structural Engineering | https://www.coventry.ac.uk/course-structure/pg/ees/structural-engineering-msc/ |
| 50 | Supply Chain Management and Logistics | https://www.coventry.ac.uk/course-structure/pg/ees/supply-chain-management-and-logistics-msc/ |
| 51 | Sustainability and Environmental Management | https://www.coventry.ac.uk/course-structure/pg/ees/environmental-management-msc/ |
| 52 | Sustainable Transport Systems | https://www.coventry.ac.uk/course-structure/pg/ees/sustainable-transport-systems-msc/ |

##### PGCert

| # | 项目 | URL |
|---|------|-----|
| 1 | Crowded Places and Public Safety Management | https://www.coventry.ac.uk/course-structure/pg/ees/crowded-places-and-public-safety-management/ |
| 2 | Emergency and Incident Management | https://www.coventry.ac.uk/course-structure/pg/ees/emergency-and-incident-management-pg-cert/ |
| 3 | Emergency Preparedness and Management | https://www.coventry.ac.uk/course-structure/pg/ees/emergency-preparedness-and-management-pg-cert/ |

#### Faculty of Arts and Humanities (cas)

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Innovation Leadership | https://www.coventry.ac.uk/course-structure/pg/cas/applied-innovation-leadership-ma/ |
| 2 | Automotive and Transport Design | https://www.coventry.ac.uk/course-structure/pg/cas/automotive-design-ma/ |
| 3 | Automotive Journalism | https://www.coventry.ac.uk/course-structure/pg/cas/automotive-journalism-ma/ |
| 4 | Communication, Culture and Media | https://www.coventry.ac.uk/course-structure/pg/cas/communication-culture-and-media-ma/ |
| 5 | Creative Writing | https://www.coventry.ac.uk/course-structure/pg/cas/creative-writing-ma/ |
| 6 | Criminology and Criminal Justice | https://www.coventry.ac.uk/course-structure/pg/cas/criminology-and-criminal-justice-ma/ |
| 7 | Curation | https://www.coventry.ac.uk/course-structure/pg/cas/curation-ma/ |
| 8 | Design Management | https://www.coventry.ac.uk/course-structure/pg/cas/design-management-ma/ |
| 9 | Diplomacy and Conflict Resolution | https://www.coventry.ac.uk/course-structure/pg/cas/diplomacy-conflict-resolution-ma/ |
| 10 | English Literature | https://www.coventry.ac.uk/course-structure/pg/cas/english-literature-ma/ |
| 11 | Film and Media Production | https://www.coventry.ac.uk/course-structure/pg/cas/film-media-production-ma/ |
| 12 | Fine Art: Digital | https://www.coventry.ac.uk/course-structure/pg/cas/fine-art-digital-ma/ |
| 13 | Games Studio Development | https://www.coventry.ac.uk/course-structure/pg/cas/games-studio-development-ma/ |
| 14 | Global Journalism and Public Relations | https://www.coventry.ac.uk/course-structure/pg/cas/global-journalism-ma/ |
| 15 | Graphic Design | https://www.coventry.ac.uk/course-structure/pg/cas/graphic-design-ma/ |
| 16 | History | https://www.coventry.ac.uk/course-structure/pg/cas/history-ma/ |
| 17 | Illustration and Animation | https://www.coventry.ac.uk/course-structure/pg/cas/illustration-and-animation-ma/ |
| 18 | Interior Design | https://www.coventry.ac.uk/course-structure/pg/cas/interior-design-ma/ |
| 19 | International Relations | https://www.coventry.ac.uk/course-structure/pg/cas/international-relations-ma/ |
| 20 | Music and Sound Production | https://www.coventry.ac.uk/course-structure/pg/cas/music-production-ma/ |
| 21 | Photography | https://www.coventry.ac.uk/course-structure/pg/cas/photography-ma/ |
| 22 | Popular Music Practice | https://www.coventry.ac.uk/course-structure/pg/cas/popular-music-practice-ma/ |
| 23 | Product Design Innovation | https://www.coventry.ac.uk/course-structure/pg/cas/product-design-innovation-ma/ |
| 24 | Sociology and Social Research | https://www.coventry.ac.uk/course-structure/pg/cas/sociology-social-research-ma/ |
| 25 | Sports Journalism | https://www.coventry.ac.uk/course-structure/pg/cas/sports-journalism-ma/ |
| 26 | Terrorism, International Crime and Global Security | https://www.coventry.ac.uk/course-structure/pg/cas/terrorism-international-crime-and-global-security-ma/ |
| 27 | Virtual and Augmented Reality | https://www.coventry.ac.uk/course-structure/pg/cas/immersive-and-virtual-media-ma/ |

##### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Psychology | https://www.coventry.ac.uk/course-structure/pg/cas/applied-psychology/ |
| 2 | Business and Organisational Psychology | https://www.coventry.ac.uk/course-structure/pg/cas/business-and-organisational-psychology-msc/ |
| 3 | Forensic Psychology | https://www.coventry.ac.uk/course-structure/pg/cas/forensic-psychology-msc/ |
| 4 | Forensic Psychology and Mental Health | https://www.coventry.ac.uk/course-structure/pg/cas/forensic-psychology-and-mental-health-msc/ |
| 5 | Psychology | https://www.coventry.ac.uk/course-structure/pg/cas/psychology-msc/ |

##### MArch

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://www.coventry.ac.uk/course-structure/pg/cas/architecture-march/ |

##### D.Clin.Psych

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctorate in Clinical Psychology | https://www.coventry.ac.uk/course-structure/pg/cas/clinical-psychology-dcli/ |

#### Faculty of Health and Life Sciences — School of Health Sciences (shc)

##### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Adult Nursing (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/adult-nursing-pre-registration-msc/ |
| 2 | Advanced Clinical Practice | https://www.coventry.ac.uk/course-structure/pg/shc/advanced-clinical-practice-msc/ |
| 3 | Children and Young People's Nursing (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/children-and-young-peoples-nursing-pre-registration-msc/ |
| 4 | Dietetics and Leadership (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/dietetics-and-leadership-msc/ |
| 5 | Global Healthcare Management | https://www.coventry.ac.uk/course-structure/pg/shc/global-health-care-management-msc/ |
| 6 | Global Public Health | https://www.coventry.ac.uk/course-structure/pg/shc/global-public-health-msc/ |
| 7 | Learning Disabilities Nursing (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/learning-disabilities-nursing-msc-pre-registration/ |
| 8 | Mental Health Nursing (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/mental-health-nursing-msc-pre-registration/ |
| 9 | Nursing | https://www.coventry.ac.uk/course-structure/pg/shc/nursing-msc/ |
| 10 | Occupational Therapy (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/occupational-therapy-msc/ |
| 11 | Physiotherapy | https://www.coventry.ac.uk/course-structure/pg/shc/physiotherapy-msc/ |
| 12 | Physiotherapy and Leadership (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/physiotherapy-and-leadership-msc/ |
| 13 | Podiatry and Leadership (pre-registration) | https://www.coventry.ac.uk/course-structure/pg/shc/podiatry-and-leadership-msc/ |

##### MA/PGDip

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.coventry.ac.uk/course-structure/pg/shc/social-work-ma/ |

##### PGCert

| # | 项目 | URL |
|---|------|-----|
| 1 | Cognitive Behavioural Therapy | https://www.coventry.ac.uk/course-structure/pg/shc/cognitive-behavioural-therapy-pgdipmsc/ |
| 2 | Critical Care Nursing | https://www.coventry.ac.uk/course-structure/pg/shc/critical-care-nursing-pg-cert/ |
| 3 | Low Intensity Psychological Interventions | https://www.coventry.ac.uk/course-structure/pg/shc/low-intensity-psychological-intervention/ |
| 4 | Practice Education | https://www.coventry.ac.uk/course-structure/pg/shc/practice-education-pgc/ |

#### Coventry University London (London campus)

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Finance | https://www.coventry.ac.uk/london/course-structure/pg/finance-mba/ |
| 2 | Global Business | https://www.coventry.ac.uk/london/course-structure/pg/global-business-mba/ |
| 3 | Global Healthcare Management and Leadership | https://www.coventry.ac.uk/london/course-structure/pg/global-healthcare-management-and-leadership-mba/ |
| 4 | International Fashion Management | https://www.coventry.ac.uk/london/course-structure/pg/international-fashion-management-mba/ |
| 5 | International Human Resource Management | https://www.coventry.ac.uk/london/course-structure/pg/international-human-resource-management-mba/ |
| 6 | International Marketing | https://www.coventry.ac.uk/london/course-structure/pg/international-marketing-mba/ |
| 7 | Leadership in the Digital Age | https://www.coventry.ac.uk/london/course-structure/pg/leadership-digital-mba/ |

##### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Marketing | https://www.coventry.ac.uk/london/course-structure/pg/digital-marketing-msc/ |
| 2 | Economics and Banking | https://www.coventry.ac.uk/london/course-structure/pg/economics-banking-msc/ |
| 3 | Financial Technology | https://www.coventry.ac.uk/london/course-structure/pg/financial-technology-fintech-msc/ |
| 4 | Global Finance | https://www.coventry.ac.uk/london/course-structure/pg/global-finance-msc/ |
| 5 | Innovation Management and Entrepreneurship | https://www.coventry.ac.uk/london/course-structure/pg/innovation-management-entrepreneurship-msc/ |
| 6 | International Fashion Marketing | https://www.coventry.ac.uk/london/course-structure/pg/international-fashion-marketing-msc/ |
| 7 | International Hospitality and Tourism Management | https://www.coventry.ac.uk/london/course-structure/pg/international-hospitality-and-tourism-management-msc/ |
| 8 | International Project Management | https://www.coventry.ac.uk/london/course-structure/pg/international-project-management-msc/ |
| 9 | Investment, Risk and Trading | https://www.coventry.ac.uk/london/course-structure/pg/investment-risk-trading-msc/ |
| 10 | Management | https://www.coventry.ac.uk/london/course-structure/pg/management-msc/ |
| 11 | Professional Accounting | https://www.coventry.ac.uk/london/course-structure/pg/professional-accounting-msc/ |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science MSc** — Faculty of Engineering, Environment and Computing

| Field | Value |
|-------|-------|
| Course code | EEST029 |
| Location | Coventry University (Coventry) |
| Duration | 1 year full-time; up to 2 years with professional placement |
| Credits | 180 total |
| Start date | July 2026 |
| UK fee | £11,200/year |
| International fee | £18,600/year |
| Placement fee | £1,500/year (UK) / £1,800/year (international) |
| Entry requirement (UK) | Honours degree 2:2 or above in a computational discipline |
| Entry requirement (Intl) | Same + IELTS 6.5 overall (min 5.5 per component) |
| Application | Direct to university (international); online portal (UK) |
| Accreditation | CMI Level 7 Certificate (via Advanced Software Development module) |
| Source URL | https://www.coventry.ac.uk/course-structure/pg/ees/computer-science-msc/ |

### 2.3 Graduate admissions model

Coventry uses a **decentralized** model for postgraduate admissions:
- **UK students**: Apply via the Coventry University online applicant portal
- **International students**: Apply directly to the university (some courses via UCAS)
- **Application fee**: Not explicitly stated on course pages (appears to be free for most courses)
- **Contact**: +44 (0)24 7765 6565 | ukadmissions@coventry.ac.uk (UK) / ioadmissions@coventry.ac.uk (international)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | UCAS | coventry.ac.uk/study-at-coventry/apply-now/ |
| Institution code | C85 | Course pages |
| UCAS deadline (equal consideration) | January (standard) | coventry.ac.uk/international-students-hub/entry-requirements/ |
| Oxford/Cambridge deadline | N/A (not Oxbridge) | — |
| Admissions tests | None specified (course-specific portfolios for design courses) | Course pages |
| Personal statement | UCAS single statement | UCAS standard |
| References | 1 academic reference (UCAS) | UCAS standard |
| Interviews | Some courses (e.g. Nursing, Social Work) | Course pages |
| Conditional offers | Yes — offers conditional on A-Level/IB final grades | Course pages |
| Clearing | Available for 2026 entry | coventry.ac.uk/clearing/ |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum (UG) | Minimum (PG) | Notes |
|------|-------------|-------------|-------|
| IELTS Academic | 6.0 overall (min 5.5 per component) | 6.5 overall (min 5.5 per component) | Standard requirement; some courses may be higher |
| TOEFL iBT | 79 (min 18 per component) | 88 (min 19 per component) | New scoring scale: 4.0 overall (UG) / 4.5 overall (PG) |
| Other accepted | PTE, Cambridge, Duolingo (varies) | PTE, Cambridge (varies) | "Other English qualifications are considered" |
| Pre-sessional English | Available | Available | For students who don't meet requirements |
| Exemptions | Some EU countries with sufficient English grades in national qualifications | Same | Austria, Belgium, Croatia, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Latvia, Luxembourg, Netherlands, Norway |

### 3.3 Graduate — global rules

- **Application platform**: Direct to university (no UCAS for PG)
- **Standard entry requirement**: Honours degree 2:2 or above (or international equivalent)
- **Country-specific requirements**: Detailed per-country requirements available at `coventry.ac.uk/international-students-hub/entry-requirements/`
- **English language**: IELTS 6.5 overall (min 5.5 per component) for most courses
- **GRE/GMAT**: Not required for most courses (MBA may have work experience requirements)
- **Application timeline**: Rolling admissions with multiple start dates (September, November, January, March, May, July)
- **Application fee**: Not explicitly stated (appears to be free)
- **Alumni discount**: 25% discount on PG tuition for Coventry University graduates (from September 2025)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

| Expense item | UK/Home fee | International fee | Notes |
|-------------|-------------|-------------------|-------|
| Tuition (standard courses) | £9,790/year | £17,600/year | Business, Law, Arts, Humanities |
| Tuition (lab/clinical courses) | £9,790/year | £20,800/year | Engineering, Computing, Sciences |
| EU (with bursary) | £9,790/year | — | EU Support Bursary available |
| EU (without bursary) | — | £17,600–£20,800/year | Depends on course |
| Placement year fee | £1,575/year | £1,900/year | Academic year 2028/29 |
| Additional costs | £400+ per trip | £400+ per trip | Optional overseas field trips |
| Living costs | Not specified | Not specified | "Top 10 Student City in England for Affordability" (QS 2026) |

> **Source**: Course pages (e.g. Computer Science BSc, Law LLB, Business Management BA). Fees may increase annually — up to 5% above inflation for international students.
> **Note**: NHS-funded courses (Nursing, Midwifery, AHPs) may have different fee structures. Students on NHS courses can apply for a minimum government training payment of £5,000/year.

### 4.2 Undergraduate financial-aid policy

- **Student Finance England**: Available for UK/home students (loans for tuition and maintenance)
- **EU Support Bursary**: Available for eligible EU students (reduces fees to home rate)
- **Scholarships**: Available for international students (competitive, subject to availability)
- **Payment plans**: Available for self-funded international students
- **Need-blind**: Not applicable (UK fee-status system, not need-based admissions)
- **Tuition-free threshold**: N/A (UK system)

### 4.3 Graduate cost & funding framework

| Fee type | UK/Home | International | Source |
|----------|---------|---------------|--------|
| PGT tuition (standard) | £9,350–£11,200/year | £18,600/year | Course pages |
| MBA tuition | Varies | Varies | Course pages |
| London campus tuition | Varies | Varies | London course pages |
| Professional placement fee | £1,500/year | £1,800/year | Computer Science MSc page |
| Application fee | Not stated (appears free) | Not stated | — |

**Funding types**:
- Self-funded (most common for international students)
- Scholarships (competitive, university-specific)
- Chevening/Commonwealth scholarships (for eligible countries)
- Alumni discount: 25% for Coventry graduates on PG programmes

---

## SECTION 5 — Evidence chain index

```yaml
---
field: undergraduate.total_programs
value: 126
source_url: https://www.coventry.ac.uk/clearing/course-finder/
source_snippet: "126 undergraduate courses available for September 2026"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: postgraduate.total_programs
value: 146 (Coventry campus) + 18 (London campus) = 164
source_url: https://www.coventry.ac.uk/study-at-coventry/postgraduate-study/az-course-list/
source_snippet: "260 total listings (including year variants); 146 unique courses at Coventry campus"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: ug.tuition.home
value: £9,790/year
source_url: https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/
source_snippet: "UK, Ireland, Channel Islands, Isle of Man: £9,790"
capture_date: 2026-07-08
evidence_type: official_webpage_table
---
field: ug.tuition.international.standard
value: £17,600/year
source_url: https://www.coventry.ac.uk/course-structure/ug/fbl/law-llb-hons/
source_snippet: "International: £17,600"
capture_date: 2026-07-08
evidence_type: official_webpage_table
---
field: ug.tuition.international.lab
value: £20,800/year
source_url: https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/
source_snippet: "International: £20,800"
capture_date: 2026-07-08
evidence_type: official_webpage_table
---
field: pgt.tuition.home
value: £9,350–£11,200/year
source_url: https://www.coventry.ac.uk/course-structure/pg/ees/computer-science-msc/
source_snippet: "UK/Ireland/Channel Islands/Isle of Man: £11,200/year"
capture_date: 2026-07-08
evidence_type: official_webpage_table
---
field: pgt.tuition.international
value: £18,600/year
source_url: https://www.coventry.ac.uk/course-structure/pg/ees/computer-science-msc/
source_snippet: "International: £18,600/year"
capture_date: 2026-07-08
evidence_type: official_webpage_table
---
field: english_language.ug.ielts
value: 6.0 overall (min 5.5 per component)
source_url: https://www.coventry.ac.uk/international-students-hub/entry-requirements/
source_snippet: "Undergraduate: IELTS 6.0 overall with minimum 5.5 in each component"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: english_language.pg.ielts
value: 6.5 overall (min 5.5 per component)
source_url: https://www.coventry.ac.uk/international-students-hub/entry-requirements/
source_snippet: "Postgraduate: IELTS 6.5 overall with minimum 5.5 in each component"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: english_language.ug.toefl
value: 79 (min 18 per component)
source_url: https://www.coventry.ac.uk/international-students-hub/entry-requirements/
source_snippet: "TOEFL iBT score of 79 (minimum component score 18)"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: english_language.pg.toefl
value: 88 (min 19 per component)
source_url: https://www.coventry.ac.uk/international-students-hub/entry-requirements/
source_snippet: "TOEFL iBT score of 88 (minimum component score 19)"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: application.ucas_code
value: C85
source_url: https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/
source_snippet: "Institution Code: C85"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: application.placement_fee
value: £1,575 (UK) / £1,900 (international)
source_url: https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/
source_snippet: "Placement year fee: £1,575 (UK fee-payers) or £1,900 (international fee-payers)"
capture_date: 2026-07-08
evidence_type: official_webpage_table
---
field: alumni_discount
value: 25% discount on PG tuition
source_url: https://www.coventry.ac.uk/international-students-hub/fees-and-funding/
source_snippet: "All Coventry University graduates can receive a 25% discount from September 2025 from the tuition fees payable for their postgraduate programme."
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: china.ug_requirement
value: 3 years high school with 80%+, or first year university with 70%+, or 3-year college diploma with 70%+
source_url: https://www.coventry.ac.uk/international-students-hub/entry-requirements/
source_snippet: "China — UG: 3 years high school with 80%+, or first year university with 70%+, or 3-year college diploma with 70%+"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: india.ug_requirement
value: Standard XII with 60%+ (60% in English from certain boards)
source_url: https://www.coventry.ac.uk/international-students-hub/entry-requirements/
source_snippet: "India UG (Business): Standard XII with 60%+"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: tef_rating
value: Gold Overall (2023)
source_url: https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/
source_snippet: "TEF Gold overall (Teaching Excellence Framework 2023)"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: qs_stars
value: 5 QS Stars for Teaching and Facilities
source_url: https://www.coventry.ac.uk/course-structure/ug/eec/computer-science-mscibsc-hons/
source_snippet: "5 QS Stars for Teaching and Facilities"
capture_date: 2026-07-08
evidence_type: official_webpage
---
field: nhs_training_payment
value: Minimum £5,000/year
source_url: https://www.coventry.ac.uk/course-structure/ug/hls-nhs/adult-nursing-bsc-hons/
source_snippet: "All eligible learners can apply for a minimum government payment of £5,000 per year"
capture_date: 2026-07-08
evidence_type: official_webpage
---
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
coventry-knowledge-base-v2/
├── overview/                          → Section 0 (counts, hierarchy, degrees, matrix)
├── undergraduate/
│   ├── faculty-arts-humanities/       → Section 1.2 (Faculty of Arts and Humanities courses)
│   ├── faculty-business-law/          → Section 1.2 (Faculty of Business and Law courses)
│   ├── faculty-engineering-computing/ → Section 1.2 (Faculty of Engineering, Environment and Computing courses)
│   ├── faculty-health-life-sciences/  → Section 1.2 (Faculty of Health and Life Sciences courses)
│   └── requirements/                  → Section 3.1 (UG entry requirements, deadlines)
├── postgraduate/
│   ├── faculty-business-law/          → Section 2.1 (CBL courses)
│   ├── faculty-engineering-computing/ → Section 2.1 (EES courses)
│   ├── faculty-arts-humanities/       → Section 2.1 (CAS courses)
│   ├── faculty-health-life-sciences/  → Section 2.1 (SHC courses)
│   ├── london-campus/                 → Section 2.1 (London courses)
│   └── requirements/                  → Section 3.3 (PG entry requirements)
├── costs/                             → Section 4 (fees, funding)
└── evidence/                          → Section 5 (evidence chain)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "coventry-knowledge-base-v2"
  school: "<home faculty>"
  department: "<home school, if applicable>"
  degree_level: "<BSc|BA|BEng|LLB|MSc|MA|MBA|LLM|PGCert|PGDip>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Full faculty/school organizational chart | coventry.ac.uk/the-university/governance/academic-structure/ (returned 400 error) |
| P0 | Research degree programmes (PhD/MPhil) | coventry.ac.uk/research/research-opportunities/research-students/research-degrees/ |
| P0 | Online course catalogue | coventry.ac.uk/online/search/ |
| P1 | Per-course international fees (lab vs non-lab distinction) | Individual course pages |
| P1 | Country-specific entry requirements (remaining countries P-Z) | coventry.ac.uk/international-students-hub/entry-requirements/ |
| P1 | Scholarships details and application process | coventry.ac.uk/international-students-hub/fees-and-funding/ |
| P2 | Accommodation costs | coventry.ac.uk/international-students-hub/accommodation/ |
| P2 | Student satisfaction data (NSS results per course) | Course pages |
| P2 | Graduate employment statistics | Course pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Coventry University | (blank for other schools) |
|-----------|--------------------|--------------------------|
| Total UG programs | 126 | |
| Total PGT programs | 164 | |
| Total faculties (main campus) | 4 | |
| UG tuition (Home) | £9,790/year | |
| UG tuition (International, standard) | £17,600/year | |
| UG tuition (International, lab) | £20,800/year | |
| PGT tuition (Home) | £9,350–£11,200/year | |
| PGT tuition (International) | £18,600/year | |
| IELTS UG minimum | 6.0 (5.5 per component) | |
| IELTS PG minimum | 6.5 (5.5 per component) | |
| TOEFL UG minimum | 79 (18 per component) | |
| TOEFL PG minimum | 88 (19 per component) | |
| UCAS code | C85 | |
| TEF rating | Gold Overall (2023) | |
| QS Stars | 5 (Teaching and Facilities) | |
| Clearing available | Yes (2026) | |
| Russell Group | No | |
| Placement year available | Yes (£1,575–£1,900) | |
| Alumni discount (PG) | 25% | |
| Multiple start dates | Yes (Sep, Nov, Jan, Mar, May, Jul) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: coventry.ac.uk
> **Verification**: ego-browser snapshotText + JS DOM extraction + WebFetch
> **Granularity**: faculty → school → degree-level → program
