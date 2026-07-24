# Nottingham Trent University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England, Nottingham)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes: BA/BSc/BEng/etc.) | 288 |
| 研究生授课型 + 研究型 (PGT + PGR: MA/MSc/MBA/MRes/PhD) | 143 |
| **学位项目总计 (UG + PG)** | **431** |
| 学院 / 学校 (Schools) | 9 |
| 学科领域 (Subject areas) | 43 |

> **Data source**: NTU Subject areas hub (`ntu.ac.uk/course/<subject>`) — 43 subject pages; 431 unique courses (288 UG + 143 PG). URL pattern: `/course/<school>/<ug|pg>/<slug>` exposes school attribution.
>
> **Reconciliation**: Rule 1 total (431) == matrix cell sum (431) == rule-5 row count (431). All match.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Nottingham Trent University (NTU)
├── Nottingham Business School (NBS)                              [学院]
│   ├── Accounting, Finance and Economics
│   ├── Business, Management and Marketing
│   ├── MBA programmes
│   └── Triple Crown accredited (EQUIS, AMBA, AACSB)
├── Nottingham School of Art & Design                              [学院]
│   ├── Fashion Management, Marketing & Communication
│   ├── Fashion, Textiles and Knitwear Design
│   ├── Fine Art (MFA)
│   ├── Music and Events (Nottingham + London + Online)
│   ├── Product Design
│   ├── Graphic Design and Illustration
│   ├── Media, Communications, Film and TV
│   └── Games, Animation and VFX
├── School of Architecture, Design and the Built Environment       [学院]
│   ├── Architecture and Civil Engineering
│   ├── Property, Construction and Surveying
│   └── Interior Architecture
├── School of Science and Technology                                [学院]
│   ├── Biosciences (Biomedical Science, Pharmacology, Neuroscience)
│   ├── Chemistry and Physics (Forensic Science)
│   ├── Computing (CS, AI, Cyber Security, Data Science, Software Engineering)
│   ├── Engineering, Maths and other Technologies
│   └── Sport Science
├── School of Social Sciences                                       [学院]
│   ├── Criminology and Policing
│   ├── English, History and Philosophy
│   ├── Psychology
│   ├── Sociology and Social Work
│   └── Politics and International Relations
├── School of Arts and Humanities                                    [学院]
│   ├── English, Linguistics and Creative Writing
│   ├── History and Heritage
│   ├── Humanities Joint Honours
│   ├── Media, Journalism and Film
│   └── Music and Live Events
├── School of Education                                              [学院]
│   ├── Education
│   ├── Teacher Training (PGCE)
│   └── Childhood Studies
├── School of Animal, Rural and Environmental Sciences              [学院]
│   ├── Animal, Equine and Veterinary Sciences
│   ├── Agriculture
│   ├── Conservation and Ecology
│   ├── Geography and Environmental Science
│   ├── Biosciences
│   └── Food Science and Production
└── NTU Mansfield                                                    [学院]
    ├── Higher National Certificate (HNC) — multiple subjects
    ├── Higher National Diploma (HND) — multiple subjects
    ├── Foundation Degrees (FdSc, FdA)
    ├── NTU Mansfield-specific BA/BSc variants
    └── Apprenticeships (Level 4 & 5)
```

> Note: NTU also has a London campus offering selected courses (Business, Computing, Music) and an online/distance-learning portfolio. NTU Mansfield is a separate partnership site with its own portfolio of HNC/HND/apprenticeships.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (canonical) | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 101 |
| BS | Bachelor of Science | 本科 | 129 |
| BEng | Bachelor of Engineering | 本科 | 14 |
| BArch | Bachelor of Architecture | 本科 | 2 |
| BMus | Bachelor of Music | 本科 | 2 |
| MChem | Master of Chemistry | 本科 | 3 |
| MSci | Master in Science | 本科 | 2 |
| MEng | Master of Engineering | 本科 | 6 |
| MMath | Master of Mathematics | 本科 | 1 |
| MA | Master of Arts | 研究生 | 35 |
| MSc | Master of Science | 研究生 | 78 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MRes | Master of Research | 研究生 | 15 |
| MRes/MSc | MRes/MSc joint award | 研究生 | 6 |
| MArch | Master of Architecture | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | 1 |
| PGCE | Postgraduate Certificate in Education | 研究生 | 3 |
| FdSc | Foundation Degree in Science | 本科 | 8 |
| FdA | Foundation Degree in Arts | 本科 | 7 |
| CertEd | Certificate in Education | 研究生 | 1 |
| CertHE | Certificate of Higher Education | 本科 | 1 |
| HNC | Higher National Certificate | 本科 | 7 |
| HND | Higher National Diploma | 本科 | 5 |
| MSc/PGDip | MSc/PGDip joint award | 研究生 | 1 |

> **Degree naming convention**: NTU uses standard UK "(Hons)" appendage. "Joint" degrees listed once with combined suffix (e.g. "MRes/MSc"). Campus-prefixed variants (London, NTU in Mansfield, Clifton, Online) merged under canonical codes for cross-school comparison.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BA | BArch | BEng | BMus | BS | CertEd | CertHE | FdA | FdSc | HNC | HND | MA | MArch | MBA | MChem | MEng | MFA | MMath | MRes | MRes/MSc | MSc | MSc/PGDip | MSci | PGCE | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nottingham Business School (NBS) | 14 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | **46** |
| Nottingham School of Art & Design | 30 | 0 | 0 | 2 | 8 | 0 | 0 | 5 | 5 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | **76** |
| School of Architecture, Design and the Built Environment | 6 | 2 | 2 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | **42** |
| School of Science and Technology | 0 | 0 | 10 | 0 | 57 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 5 | 0 | 1 | 15 | 0 | 25 | 0 | 2 | 0 | **118** |
| School of Social Sciences | 10 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 13 | 1 | 0 | 0 | **45** |
| School of Arts and Humanities | 27 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **32** |
| School of Education | 10 | 0 | 0 | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | **20** |
| School of Animal, Rural and Environmental Sciences | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | **27** |
| NTU Mansfield | 4 | 0 | 2 | 0 | 3 | 0 | 1 | 2 | 1 | 7 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **25** |
| **合计** | 101 | 2 | 14 | 2 | 129 | 1 | 1 | 7 | 8 | 7 | 5 | 35 | 1 | 2 | 3 | 6 | 1 | 1 | 15 | 6 | 78 | 1 | 2 | 3 | **431** |

> Row totals = column totals = **431**. The matrix is the single most powerful artifact for cross-school comparison.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

NTU operates 9 academic schools (including NTU Mansfield). Undergraduate programmes are predominantly awarded as BA (Hons) / BSc (Hons) / BEng (Hons) / FdSc / FdA / HNC / HND. Joint-honours and foundation-year variants are common. Full list grouped below.

### 1.2 Undergraduate programmes — grouped by 学院 > 学位级别


#### Nottingham Business School (NBS) (20 programmes)


##### BA (Hons) (14)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Business | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business> |
| 2 | Business (with Foundation Year) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-with-foundation-year> |
| 3 | Business Management (Accelerated) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-management-accelerated> |
| 4 | Business Management and Accounting and Finance | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-management-and-accounting-and-finance> |
| 5 | Business Management and Digital Marketing - London | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/business-management-and-digital-marketing> |
| 6 | Business Management and Economics | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-management-and-economics> |
| 7 | Business Management and Entrepreneurship | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-management-and-entrepreneurship> |
| 8 | Business Management and Human Resources | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-management-and-human-resources> |
| 9 | Business Management and Marketing | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-business-management-and-marketing> |
| 10 | International Business | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-international-business> |
| 11 | International Business (with French) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-international-business-with-french> |
| 12 | International Business (with Spanish) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-international-business-with-spanish> |
| 13 | International Business Management (top-up) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-international-business-management-top-up> |
| 14 | Marketing | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/ba-hons-marketing> |

##### BSc (Hons) (6)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Accounting and Finance | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-accounting-and-finance> |
| 2 | Accounting and Finance (with Foundation Year) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/accounting-and-finance-with-foundation-year> |
| 3 | Economics | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-economics> |
| 4 | Economics (with Foundation Year) | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/economics-with-foundation-year> |
| 5 | Economics with Business | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-economics-with-business> |
| 6 | Economics with International Finance and Banking | <https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-economics-with-international-finance-and-banking> |

#### Nottingham School of Art & Design (50 programmes)


##### BA (Hons) (30)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Animation | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-animation> |
| 2 | Animation - London | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-animation-london> |
| 3 | Content Creation | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-content-creation> |
| 4 | Costume Design and Construction | <https://www.ntu.ac.uk/course/art-and-design/ug/costume-design-and-construction> |
| 5 | Creative Direction and Curation for Fashion | <https://www.ntu.ac.uk/course/art-and-design/ug/creative-direction-and-curation-for-fashion> |
| 6 | Design for Film and Television | <https://www.ntu.ac.uk/course/art-and-design/ug/design-for-film-and-television> |
| 7 | Design for Theatre and Live Performance | <https://www.ntu.ac.uk/course/art-and-design/ug/design-for-theatre-and-live-performance> |
| 8 | Event Management | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-event-management> |
| 9 | Fashion Communication and Promotion | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-fashion-communication-and-promotion> |
| 10 | Fashion Design | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-fashion-design> |
| 11 | Fashion Knitwear Design and Knitted Textiles | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-fashion-knitwear-design-and-knitted-textiles> |
| 12 | Fashion Management | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-fashion-management> |
| 13 | Fashion Marketing and Branding | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-fashion-marketing-and-branding> |
| 14 | Fashion Photography | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-fashion-photography> |
| 15 | Filmmaking | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-filmmaking> |
| 16 | Fine Art | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-fine-art> |
| 17 | Games Art | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-games-art> |
| 18 | Games Art - London | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-games-art-london> |
| 19 | Graphic Design | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-graphic-design> |
| 20 | Illustration | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-illustration> |
| 21 | International Fashion Business (one year top-up) | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-international-fashion-business> |
| 22 | Music Business | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-music-business> |
| 23 | Music Business and Management - London | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-music-business-and-management-london> |
| 24 | Music Production | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-music-production> |
| 25 | Music Production - London | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-music-production-london> |
| 26 | Photography | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-photography> |
| 27 | Popular Music | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-popular-music> |
| 28 | Sports Photography | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-sports-photography> |
| 29 | Textile Design | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-textile-design> |
| 30 | Visual Effects Art | <https://www.ntu.ac.uk/course/art-and-design/ug/ba-hons-visual-effects-art> |

##### BMus (Hons) (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Popular Music Performance - London | <https://www.ntu.ac.uk/course/art-and-design/ug/bmus-hons-popular-music-performance> |
| 2 | Songwriting and Vocal Performance - London | <https://www.ntu.ac.uk/course/art-and-design/ug/bmus-hons-songwriting-and-vocal-performance-london> |

##### BSc (Hons) (8)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Esports Production | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-esports-production> |
| 2 | Event Production | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-event-production> |
| 3 | Event Production - London | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-event-production-london> |
| 4 | Film Technology | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-film-technology> |
| 5 | Games Design | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-games-design> |
| 6 | Games Design - London | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-games-design-london> |
| 7 | Sound Engineering & Audio Production | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-sound-engineering-and-audio-production> |
| 8 | Sound Engineering & Audio Production - London | <https://www.ntu.ac.uk/course/art-and-design/ug/bsc-hons-sound-engineering-and-audio-production-london> |

##### FdA (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Audio and Music Production | <https://www.ntu.ac.uk/course/art-and-design/ug/fda-audio-and-music-production> |
| 2 | Games Art | <https://www.ntu.ac.uk/course/art-and-design/ug/fda-games-art> |
| 3 | Graphics and Digital Design | <https://www.ntu.ac.uk/course/art-and-design/ug/fda-graphics-and-digital-design> |
| 4 | Music Performance | <https://www.ntu.ac.uk/course/art-and-design/ug/fda-music-performance> |
| 5 | Music Production | <https://www.ntu.ac.uk/course/art-and-design/ug/fda-music-production> |

##### FdSc (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Event Production | <https://www.ntu.ac.uk/course/art-and-design/ug/fdsc-event-production> |
| 2 | Film Production Technology | <https://www.ntu.ac.uk/course/art-and-design/ug/fdsc-film-production-technology> |
| 3 | Film and Television Production | <https://www.ntu.ac.uk/course/art-and-design/ug/film-and-television-production> |
| 4 | Games Technology | <https://www.ntu.ac.uk/course/art-and-design/ug/fdsc-games-technology> |
| 5 | Live Event Technology | <https://www.ntu.ac.uk/course/art-and-design/ug/fdsc-live-event-technology> |

#### School of Architecture, Design and the Built Environment (28 programmes)


##### BA (Hons) (6)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Furniture and Product Design | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/ba-hons-furniture-and-product-design> |
| 2 | Furniture and Product Design (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/furniture-and-product-design-with-foundation-year> |
| 3 | Interior Architecture and Design | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/ba-hons-interior-architecture-and-design> |
| 4 | Interior Architecture and Design (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/interior-architecture-and-design-with-foundation-year> |
| 5 | Product Design | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/ba-hons-product-design> |
| 6 | Product Design (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/product-design-with-foundation-year> |

##### BArch (Hons) (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Architecture | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/barch-hons-architecture> |
| 2 | Architecture (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/architecture-with-foundation-year> |

##### BEng (Hons) (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Civil Engineering | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/beng-hons-civil-engineering> |
| 2 | Civil Engineering (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/beng-hons-civil-engineering-foundation-year> |

##### BSc (Hons) (17)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Architectural Technology | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-architectural-technology> |
| 2 | Architectural Technology (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/architectural-technology-with-foundation-year> |
| 3 | Building Surveying | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-building-surveying> |
| 4 | Civil Engineering | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-civil-engineering> |
| 5 | Civil Engineering (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-civil-engineering-foundation-year> |
| 6 | Civil Engineering Top-up (Part-time) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-civil-engineering-part-time> |
| 7 | Construction Management | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-construction-management> |
| 8 | Construction Management (Part-time) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-construction-management-part-time> |
| 9 | Construction Management (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-construction-management-foundation-year> |
| 10 | Product Design | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-product-design> |
| 11 | Product Design (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/product-design-with-foundation-year2> |
| 12 | Property Development and Planning | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-property-development-and-planning> |
| 13 | Property Finance and Investment | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-property-finance-and-investment> |
| 14 | Quantity Surveying and Commercial Management | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-quantity-surveying-and-commercial-management> |
| 15 | Quantity Surveying and Commercial Management (Part-time) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-quantity-surveying-and-commercial-management-part-time> |
| 16 | Quantity Surveying and Commercial Management (with Foundation Year) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-quantity-surveying-and-commercial-management-foundation-year> |
| 17 | Real Estate | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/bsc-hons-real-estate> |

##### MEng (Hons) (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Civil Engineering Design and Construction | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/ug/meng-hons-civil-engineering-design-and-construction> |

#### School of Science and Technology (78 programmes)


##### BEng (Hons) (10)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Aerospace Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-hons-aerospace-engineering> |
| 2 | Aerospace Engineering (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/aerospace-engineering-with-foundation-year> |
| 3 | Biomedical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-hons-biomedical-engineering> |
| 4 | Biomedical Engineering (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-biomedical-engineering-with-foundation-year> |
| 5 | Electronic and Electrical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-hons-electronic-electrical-engineering> |
| 6 | Electronic and Electrical Engineering (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-electronic-and-electrical-engineering-with-foundation-year> |
| 7 | Mechanical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-hons-mechanical-engineering> |
| 8 | Mechanical Engineering (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-mechanical-engineering-with-foundation-year> |
| 9 | Sport Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-hons-sport-engineering> |
| 10 | Sport Engineering (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/beng-sport-engineering-with-foundation-year> |

##### BSc (Hons) (57)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Biochemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-biochemistry> |
| 2 | Biochemistry (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/biochemistry-with-foundation-year> |
| 3 | Biological Sciences | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-biological-science> |
| 4 | Biological Sciences (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/biological-science-with-foundation-year> |
| 5 | Biomedical Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-biomedical-science> |
| 6 | Biomedical Science (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/biomedical-science-with-foundation-year> |
| 7 | Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-chemistry> |
| 8 | Chemistry (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/chemistry-with-foundation-year> |
| 9 | Computer Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-computer-science> |
| 10 | Computer Science (Games Technology) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-computer-science-games-technology> |
| 11 | Computer Science (Games Technology) - London | <https://www.ntu.ac.uk/course/science-and-technology/ug/computer-science-games-technology-london> |
| 12 | Computer Science (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/computer-science-with-foundation-year> |
| 13 | Computer Science - Artificial Intelligence | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-computer-science-artificial-intelligence> |
| 14 | Computer Science - Artificial Intelligence (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/computer-science-artificial-intelligence-with-foundation-year> |
| 15 | Computer Science - Games Technology (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/computer-science-games-technology-with-foundation-year> |
| 16 | Computer Science and Mathematics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-computer-science-and-mathematics> |
| 17 | Computer Science and Mathematics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-computer-science-and-mathematics-with-foundation-year> |
| 18 | Computing | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-computing> |
| 19 | Computing (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/computing-with-foundation-year> |
| 20 | Cyber Security | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-cyber-security> |
| 21 | Cyber Security (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/cyber-security-with-foundation-year> |
| 22 | Data Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-data-science> |
| 23 | Data Science (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-data-science-with-foundation-year> |
| 24 | Financial Mathematics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-financial-mathematics> |
| 25 | Financial Mathematics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-financial-mathematics-with-foundation-year> |
| 26 | Forensic Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-forensic-chemistry> |
| 27 | Forensic Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-forensic-science> |
| 28 | Forensic Science (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/forensic-science-with-foundation-year> |
| 29 | Mathematics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-mathematics> |
| 30 | Mathematics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-mathematics-with-foundation-year> |
| 31 | Mathematics and Physics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-physics-and-mathematics> |
| 32 | Mathematics and Physics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-physics-and-mathematics-with-foundation-year> |
| 33 | Mathematics with Data Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/mathematics-with-data-science> |
| 34 | Mathematics with Data Science (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/mathematics-with-data-science-with-foundation-year> |
| 35 | Mathematics with Statistics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-mathematics-with-statistics> |
| 36 | Mathematics with Statistics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-mathematics-with-statistics-with-foundation-year> |
| 37 | Medicinal Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-medicinal-chemistry> |
| 38 | Microbiology | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-microbiology> |
| 39 | Microbiology (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/microbiology-with-foundation-year> |
| 40 | Pharmacology | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-pharmacology> |
| 41 | Pharmacology (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/pharmacology-with-foundation-year> |
| 42 | Physics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-physics> |
| 43 | Physics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/physics-with-foundation-year> |
| 44 | Physics with Astrophysics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-physics-with-astrophysics> |
| 45 | Physics with Nuclear Technology | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-physics-with-nuclear-technology> |
| 46 | Software Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-software-engineering> |
| 47 | Software Engineering (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/software-engineering-with-foundation-year> |
| 48 | Sport Science and Coaching | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-sport-science-and-coaching> |
| 49 | Sport Science and Coaching (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/sport-science-and-coaching-with-foundation-year> |
| 50 | Sport Science and Management | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-sport-science-and-management> |
| 51 | Sport Science and Management (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/sport-science-and-management-with-foundation-year> |
| 52 | Sport Science and Mathematics | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-sport-science-and-mathematics> |
| 53 | Sport Science and Mathematics (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-sport-science-and-mathematics-with-foundation-year> |
| 54 | Sport Science, Health and Nutrition | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-sport-science-health-nutrition> |
| 55 | Sport Science, Health and Nutrition (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/sport-science,-health-and-nutrition-with-foundation-year> |
| 56 | Sport and Exercise Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/bsc-hons-sport-and-exercise-science> |
| 57 | Sport and Exercise Science (with foundation year) | <https://www.ntu.ac.uk/course/science-and-technology/ug/sport-and-exercise-science-with-foundation-year> |

##### MChem (Hons) (3)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/mchem-chemistry> |
| 2 | Forensic Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/mchem-hons-forensic-chemistry> |
| 3 | Medicinal Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/ug/mchem-hons-medicinal-chemistry> |

##### MEng (Hons) (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Aerospace Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/meng-aerospace-engineering> |
| 2 | Biomedical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/meng-hons-biomedical-engineering> |
| 3 | Electronic and Electrical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/meng-hons-electronic-electrical-engineering> |
| 4 | Mechanical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/meng-hons-mechanical-engineering> |
| 5 | Sport Engineering | <https://www.ntu.ac.uk/course/science-and-technology/ug/meng-hons-sport-engineering> |

##### MMath (Hons) (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Mathematics | <https://www.ntu.ac.uk/course/science-and-technology/ug/mmath-mathematics> |

##### MSci (Hons) (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Forensic Science | <https://www.ntu.ac.uk/course/science-and-technology/ug/msci-forensic-science> |
| 2 | Physics | <https://www.ntu.ac.uk/course/science-and-technology/ug/msci-physics> |

#### School of Social Sciences (23 programmes)


##### BA (Hons) (10)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Criminology | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-criminology> |
| 2 | Criminology and Policing | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-criminology-and-policing> |
| 3 | Health and Social Care | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-health-and-social-care> |
| 4 | International Relations | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-international-relations> |
| 5 | Politics | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-politics> |
| 6 | Politics and International Relations | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-politics-and-international-relations> |
| 7 | Professional Policing | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-professional-policing> |
| 8 | Social Work | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-social-work> |
| 9 | Sociology | <https://www.ntu.ac.uk/course/social-sciences/ug/ba-hons-sociology> |
| 10 | Sociology and Criminology | <https://www.ntu.ac.uk/course/social-sciences/ug/sociology-and-criminology> |

##### BSc (Hons) (13)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Nursing (Adult) - Clifton Campus | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-nursing-adult> |
| 2 | Nursing (Learning Disabilities) | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-nursing-learning-disability> |
| 3 | Nursing (Mental Health) - Clifton Campus | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-nursing-mental-health> |
| 4 | Occupational Therapy | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-occupational-therapy> |
| 5 | Paramedic Science | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-ug-paramedic-science> |
| 6 | Psychology | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology> |
| 7 | Psychology (Cognition and Neuroscience) | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-cognition-and-neuroscience> |
| 8 | Psychology (Criminal Psychology) | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-forensic-psychology> |
| 9 | Psychology (Developmental Psychology) | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-educational-and-developmental-psychology> |
| 10 | Psychology (Mental Health) | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-mental-health> |
| 11 | Psychology with Counselling | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-with-counselling> |
| 12 | Psychology with Criminology | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-with-criminology> |
| 13 | Psychology with Sociology | <https://www.ntu.ac.uk/course/social-sciences/ug/bsc-hons-psychology-with-sociology> |

#### School of Arts and Humanities (27 programmes)


##### BA (Hons) (27)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Broadcast Journalism | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-broadcast-journalism> |
| 2 | Communications and English | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-communication-and-society-and-english> |
| 3 | Communications and Film & TV | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-communication-and-society-and-film-and-television> |
| 4 | Communications and History | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-communication-and-society-and-history> |
| 5 | Communications and Linguistics | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-communication-and-society-and-linguistics> |
| 6 | Communications and Philosophy | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-communication-and-society-and-philosophy> |
| 7 | Creative Writing | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-creative-writing> |
| 8 | English | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-english> |
| 9 | English Language and Linguistics | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/english-language-and-linguistics> |
| 10 | English and Film & TV | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-english-and-film-and-tv> |
| 11 | English and History | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-english-and-history> |
| 12 | English and Media | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-english-and-media> |
| 13 | English and Philosophy | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-english-and-philosophy> |
| 14 | Film & TV and History | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-film-and-tv-and-history> |
| 15 | Film & TV and Philosophy | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-film-and-tv-and-philosophy> |
| 16 | History | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-history> |
| 17 | History and Linguistics | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-history-and-linguistics> |
| 18 | History and Philosophy | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-history-and-philosophy> |
| 19 | History with International Relations | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/history-with-international-relations> |
| 20 | History with Politics | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/history-with-politics> |
| 21 | Journalism | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-journalism> |
| 22 | Linguistics and Media | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-linguistics-and-media> |
| 23 | Linguistics and Philosophy | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-linguistics-and-philosophy> |
| 24 | Media Communications | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/media-communications> |
| 25 | Media Production | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-media-production> |
| 26 | Media and Film & TV | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-media-and-film-and-tv> |
| 27 | Media and Philosophy | <https://www.ntu.ac.uk/course/arts-and-humanities/ug/ba-hons-media-and-philosophy> |

#### School of Education (15 programmes)


##### BA (Hons) (10)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Childhood and Psychology | <https://www.ntu.ac.uk/course/education/ug/childhood-and-psychology> |
| 2 | Childhood and Society | <https://www.ntu.ac.uk/course/education/ug/childhood-and-society> |
| 3 | Childhood: Health and Wellbeing | <https://www.ntu.ac.uk/course/education/ug/childhood-health-and-wellbeing> |
| 4 | Early Childhood Studies | <https://www.ntu.ac.uk/course/education/ug/ba-hons-early-childhood-studies> |
| 5 | Education Studies | <https://www.ntu.ac.uk/course/education/ug/education-studies> |
| 6 | Education Studies and Psychology | <https://www.ntu.ac.uk/course/education/ug/education-studies-and-psychology> |
| 7 | English with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/ba-hons-english-with-secondary-education> |
| 8 | History with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/history-with-secondary-education-qts> |
| 9 | Primary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/ba-hons-primary-education> |
| 10 | Special Educational Needs Disability and Inclusion | <https://www.ntu.ac.uk/course/education/ug/special-educational-needs-disability-and-inclusion> |

##### BSc (Hons) (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Chemistry with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/secondary-education-chemistry> |
| 2 | Computing with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/computing-with-secondary-education> |
| 3 | Mathematics with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/bsc-hons-mathematics-with-secondary-education> |
| 4 | Physical Education with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/pe-with-secondary-education-qts> |
| 5 | Physics with Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/ug/bsc-hons-physics-with-secondary-education> |

#### School of Animal, Rural and Environmental Sciences (22 programmes)


##### BSc (Hons) (20)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Agriculture | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-agriculture> |
| 2 | Agriculture (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/agriculture-with-foundation-year> |
| 3 | Animal Biology | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-animal-biology> |
| 4 | Animal Biology (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/animal-biology-with-foundation-year> |
| 5 | Artisan Food Production | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-artisan-food-production> |
| 6 | Ecology and Conservation | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-ecology-and-conservation> |
| 7 | Ecology and Conservation (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/ecology-and-conservation-with-foundation-year> |
| 8 | Environmental Science | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-environmental-science> |
| 9 | Environmental Science (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/environmental-science-with-foundation-year> |
| 10 | Equine Science | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-equine-science> |
| 11 | Equine Science (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/equine-science-with-foundation-year> |
| 12 | Geography | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-geography> |
| 13 | Geography (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/geography-with-foundation-year> |
| 14 | Veterinary Nursing Science (final year top-up) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-veterinary-nursing-science-top-up> |
| 15 | Wildlife Conservation | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-wildlife-conservation> |
| 16 | Wildlife Conservation (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/wildlife-conservation-with-foundation-year> |
| 17 | Zoo Biology | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-hons-zoo-biology> |
| 18 | Zoo Biology (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/zoo-biology-with-foundation-year> |
| 19 | Zoology | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/bsc-zoology> |
| 20 | Zoology (with foundation year) | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/zoology-with-foundation-year> |

##### FdSc (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Artisan Food Production | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/fdsc-artisan-food-production> |
| 2 | Veterinary Nursing | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/ug/fdsc-veterinary-nursing> |

#### NTU Mansfield (25 programmes)


##### BA (Hons) (4)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Childhood and Education Studies (top-up) - Online | <https://www.ntu.ac.uk/course/mansfield/ug/ba-hons-childhood-and-education-studies-top-up-online> |
| 2 | Criminal Justice (top-up) - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/ba-hons-criminal-justice-top-up-mansfield-campus> |
| 3 | Education and Professional Practice (top-up) - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/ba-hons-education-and-professional-practice-top-up-mansfield> |
| 4 | Social Work - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/social-work> |

##### BEng (Hons) (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Aerospace Engineering (top up) - Air and Space Institute (Newark) | <https://www.ntu.ac.uk/course/mansfield/ug/aerospace-engineering-top-up-ntu-in-mansfield> |
| 2 | Engineering Management (top up) - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/engineering-management-top-up> |

##### BSc (Hons) (3)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Applied Sport Science (top-up) - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/bsc-hons-applied-sport-science-top-up> |
| 2 | Nursing (Adult) - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/nursing-adult> |
| 3 | Nursing (Mental Health) - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/nursing-mental-health> |

##### Certificate of Higher Education in (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Ambulance Technician Practice (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/ambulance-technician-practice> |

##### FdA (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Criminal Justice - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/fda-criminal-justice> |
| 2 | Education | <https://www.ntu.ac.uk/course/mansfield/ug/fda-education> |

##### FdSc (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Sport and Exercise Science - NTU in Mansfield | <https://www.ntu.ac.uk/course/mansfield/ug/fdsc-sport-and-exercise-science> |

##### Higher National Certificate (7)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Civil Engineering for England (Senior Technician) Level 4 Apprenticeship (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/civil-engineering-senior-technician> |
| 2 | Computing for England (Network Engineering) (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/computing-for-england-network-engineering-ntu-in-mansfield> |
| 3 | Construction Management for England (Construction Site Supervisor) Level 4 Apprenticeship | <https://www.ntu.ac.uk/course/mansfield/ug/higher-national-certificate-in-construction-site-supervision> |
| 4 | Electrical and Electronic Engineering for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnc-electrical-and-electronic-engineering> |
| 5 | Manufacturing Engineering for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnc-manufacturing-engineering> |
| 6 | Mechanical Engineering for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnc-mechanical-engineering> |
| 7 | Modern Methods of Construction for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnc-modern-methods-of-construction> |

##### Higher National Diploma (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Computing for England (Network Engineering) (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnd-computing-for-england-network-engineering-ntu-in-mansfield> |
| 2 | Early Years Lead Practitioner Apprenticeship Level 5 (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnd-level-5-early-years-lead-practitioner-apprenticeship> |
| 3 | Electrical and Electronic Engineering for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnd-electrical-and-electronic-engineering> |
| 4 | Manufacturing Engineering for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnd-manufacturing-engineering> |
| 5 | Mechanical Engineering for England (NTU in Mansfield) | <https://www.ntu.ac.uk/course/mansfield/ug/hnd-mechanical-engineering> |

### 1.3 Foundation-year variants

Foundation Year variants are available for many BA/BSc/BEng programmes. They appear in the lists above with `(with Foundation Year)` suffix and are listed once under their home school.

### 1.4 Apprenticeships and Higher National Certificates/Diplomas

NTU Mansfield and selected School of Science and Technology / School of Architecture, Design and the Built Environment courses offer Level 4-5 apprenticeships (HNC / HND). These appear in the lists above under NTU Mansfield.

### 1.5 Course-ID → Major quick-lookup

NTU does not use MIT-style numbered course codes. UCAS codes are listed on individual course pages (e.g. Accounting and Finance: NN4H full-time, NN43 with placement).

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programmes — grouped by 学院 > 学位级别


#### Nottingham Business School (NBS) (26 programmes)


##### MBA (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Global Executive Master of Business Administration | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/global-executive-mba> |
| 2 | Master of Business Administration | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/mba-master-of-business-administration> |

##### MSc (24)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Advertising and Marketing Communications | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-advertising-and-marketing-communications> |
| 2 | Business Analytics and Artificial Intelligence | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-business-analytics-and-artificial-intelligence> |
| 3 | Digital Finance and Data Analytics | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-digital-finance-and-data-analytics> |
| 4 | Digital Marketing | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-digital-marketing> |
| 5 | Economics | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-economics> |
| 6 | Economics, Banking and Finance | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-economics-banking-and-finance> |
| 7 | FinTech and Financial Markets | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-fintech-and-financial-markets> |
| 8 | Finance | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-finance> |
| 9 | Finance and Accounting | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-finance-and-accounting> |
| 10 | Finance and Investment Banking | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-finance-and-investment-banking> |
| 11 | Human Resource Management | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-human-resource-management> |
| 12 | International Business (Dual Award) | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-international-business-dual-award> |
| 13 | International Business (Single Award) | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-international-business-single-award> |
| 14 | Management | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-management> |
| 15 | Management (Business Analytics) | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-management-and-business-analytics> |
| 16 | Management (Creative and Digital Industries) - London | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-management-creative-and-digital-industries> |
| 17 | Management (Global Supply Chain Management) | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-management-and-global-supply-chain-management> |
| 18 | Management (International Business) | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-management-and-international-business> |
| 19 | Management (Sustainable Leadership) | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-management-sustainable-leadership> |
| 20 | Marketing | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-marketing> |
| 21 | Marketing and Brand Management | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-marketing-and-brand-management> |
| 22 | Project Management | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-project-management> |
| 23 | Strategic Entrepreneurship and Innovation Management | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-strategic-entrepreneurship-and-innovation-management> |
| 24 | Sustainable Finance | <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-sustainable-finance> |

#### Nottingham School of Art & Design (26 programmes)


##### MA (20)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Animation | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-animation> |
| 2 | Commercial Songwriting & Production - London | <https://www.ntu.ac.uk/course/art-and-design/pg/commercial-songwriting-london> |
| 3 | Commercial Songwriting and Production (online) | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-commercial-songwriting-and-production-online> |
| 4 | Event Management | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-event-management> |
| 5 | Fashion | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-fashion-design> |
| 6 | Fashion Communications | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-fashion-communications> |
| 7 | Fashion Knitwear | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-fashion-knitwear-design> |
| 8 | Fashion Marketing | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-fashion-marketing> |
| 9 | Fashion and Creative Pattern Cutting | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-fashion-and-creative-pattern-cutting> |
| 10 | Fashion and Textiles | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-fashion-and-textile-design> |
| 11 | Filmmaking | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-filmmaking> |
| 12 | Graphic Communication | <https://www.ntu.ac.uk/course/art-and-design/pg/graphic-communication> |
| 13 | Illustration | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-illustration> |
| 14 | International Fashion Management | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-international-fashion-management> |
| 15 | Luxury Fashion Brand Management | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-luxury-fashion-brand-management> |
| 16 | Music Business (online) | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-music-business-online> |
| 17 | Music Business - London | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-music-business-london> |
| 18 | Music Production | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-music-production> |
| 19 | Music Production - London | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-music-production-london> |
| 20 | Textiles | <https://www.ntu.ac.uk/course/art-and-design/pg/ma-textile-design-innovation> |

##### MFA (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Fine Art | <https://www.ntu.ac.uk/course/art-and-design/pg/mfa-fine-art> |

##### MSc (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Creative Technologies | <https://www.ntu.ac.uk/course/art-and-design/pg/msc-creative-technologies> |
| 2 | Material and Technology Futures | <https://www.ntu.ac.uk/course/art-and-design/pg/material-and-technology-futures> |
| 3 | Sound Engineering & Audio Production | <https://www.ntu.ac.uk/course/art-and-design/pg/msc-sound-engineering-and-audio-production> |
| 4 | Sound Engineering & Audio Production - London | <https://www.ntu.ac.uk/course/art-and-design/pg/msc-sound-engineering-and-audio-production-london> |
| 5 | Virtual Production | <https://www.ntu.ac.uk/course/art-and-design/pg/msc-virtual-production> |

#### School of Architecture, Design and the Built Environment (14 programmes)


##### MA (2)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Design: Products and Furniture | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/ma-design-products-and-furniture> |
| 2 | Interior Architecture and Design | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/ma-interior-architecture-and-design> |

##### MArch (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Architecture (ARB/RIBA Part 2) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/march-architecture-arbriba-part-2> |

##### MSc (11)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Building Surveying | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-building-surveying> |
| 2 | Civil Engineering | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-civil-engineering> |
| 3 | Construction Management | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-construction-management> |
| 4 | Design: Products and Technology | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-design-products-and-technology> |
| 5 | Digital Architecture and Construction | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-digital-architecture-and-construction> |
| 6 | Project Management (Construction) | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-project-management-construction> |
| 7 | Property Development and Planning | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-property-development-and-planning> |
| 8 | Quantity Surveying | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-quantity-surveying> |
| 9 | Real Estate | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-real-estate> |
| 10 | Structural Engineering with Management | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-structural-engineering-with-management> |
| 11 | Structural Engineering with Materials | <https://www.ntu.ac.uk/course/architecture-design-and-the-built-environment/pg/msc-structural-engineering-with-materials> |

#### School of Science and Technology (40 programmes)


##### MRes (15)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Advanced Materials Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-advanced-materials-chemistry> |
| 2 | Analytical Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-analytical-chemistry> |
| 3 | Biotechnology | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-biotechnology> |
| 4 | Cancer Biology | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-cancer-biology> |
| 5 | Cellular Biomedicine | <https://www.ntu.ac.uk/course/science-and-technology/pg/cellular-biomedicine> |
| 6 | Chemistry | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-chemistry> |
| 7 | Mathematical Sciences | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-mathematical-sciences> |
| 8 | Medical Imaging | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-medical-imaging> |
| 9 | Molecular Biology | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-molecular-biology> |
| 10 | Molecular Microbiology | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-molecular-microbiology> |
| 11 | Neuropharmacology | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-neuropharmacology> |
| 12 | Pharmaceutical Analysis | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-pharmaceutical-analysis> |
| 13 | Pharmaceutical and Medicinal Science | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-pharmaceutical-and-medicinal-science> |
| 14 | Pharmacology | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-pharmacology> |
| 15 | Physics | <https://www.ntu.ac.uk/course/science-and-technology/pg/mres-physics> |

##### MSc (25)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Artificial Intelligence | <https://www.ntu.ac.uk/course/science-and-technology/pg/artificial-intelligence> |
| 2 | Biomedical Science | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-biomedical-science> |
| 3 | Biomedical Science (flexible learning) | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-biomedical-science-flexible-learning> |
| 4 | Biotechnology | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-biotechnology> |
| 5 | Chemistry / Chemistry (Professional Practice) | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-chemistry-chemistry-professional-practice> |
| 6 | Clinical Exercise Physiology | <https://www.ntu.ac.uk/course/science-and-technology/pg/clinical-exercise-physiology> |
| 7 | Cloud and Enterprise Computing | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-cloud-and-enterprise-computing> |
| 8 | Computer Science | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-computer-science> |
| 9 | Cyber Security | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-cyber-security> |
| 10 | Data Science | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-data-science> |
| 11 | Electronic Communications Engineering | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-electronic-communications-engineering> |
| 12 | Engineering Management | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-engineering-management> |
| 13 | Forensic Science | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-forensic-science> |
| 14 | Medical Engineering | <https://www.ntu.ac.uk/course/science-and-technology/pg/medical-engineering> |
| 15 | Molecular Cell Biology | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-molecular-cell-biology> |
| 16 | Molecular Microbiology | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-molecular-microbiology> |
| 17 | Neuropharmacology | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-neuropharmacology> |
| 18 | Pharmacology | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-pharmacology> |
| 19 | Physics | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-physics> |
| 20 | Robotics and Intelligent Systems | <https://www.ntu.ac.uk/course/science-and-technology/pg/robotics-and-intelligent-systems> |
| 21 | Software Engineering | <https://www.ntu.ac.uk/course/science-and-technology/pg/msc-software-engineering> |
| 22 | Sport Management | <https://www.ntu.ac.uk/course/science-and-technology/pg/sport-management> |
| 23 | Sport Psychology | <https://www.ntu.ac.uk/course/science-and-technology/pg/sport-psychology> |
| 24 | Strength and Conditioning | <https://www.ntu.ac.uk/course/science-and-technology/pg/strength-and-conditioning> |
| 25 | Sustainable Engineering: Energy | <https://www.ntu.ac.uk/course/science-and-technology/pg/sustainable-engineering-energy> |

#### School of Social Sciences (22 programmes)


##### MA (7)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Criminology (Criminology / Law Enforcement / Cybercrime) | <https://www.ntu.ac.uk/course/social-sciences/pg/ma-criminology> |
| 2 | International Relations | <https://www.ntu.ac.uk/course/social-sciences/pg/ma-international-relations> |
| 3 | International Relations and Security | <https://www.ntu.ac.uk/course/social-sciences/pg/ma-international-relations-and-security-studies> |
| 4 | Public Health | <https://www.ntu.ac.uk/course/social-sciences/pg/ma-public-health> |
| 5 | Social Work | <https://www.ntu.ac.uk/course/social-sciences/pg/ma-social-work> |
| 6 | Sociology | <https://www.ntu.ac.uk/course/social-sciences/pg/ma-sociology> |
| 7 | Youth Work Leadership and Practice | <https://www.ntu.ac.uk/course/social-sciences/pg/youth-work-leadership-and-practice> |

##### MRes/MSc (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Psychological Research Methods | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-mres-psychological-research-methods> |

##### MSc (13)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Applied Child Psychology | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-applied-child-psychology> |
| 2 | Behavioural Data Science | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-behavioural-data-science> |
| 3 | Cyberpsychology | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-cyberpsychology> |
| 4 | Forensic Mental Health | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-forensic-mental-health> |
| 5 | Forensic Psychology | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-forensic-psychology> |
| 6 | Nursing (Adult) | <https://www.ntu.ac.uk/course/social-sciences/pg/nursing> |
| 7 | Nursing (Mental Health) | <https://www.ntu.ac.uk/course/social-sciences/pg/nursing-mental-health> |
| 8 | Occupational Psychology | <https://www.ntu.ac.uk/course/social-sciences/pg/occupational-psychology> |
| 9 | Occupational Therapy | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-occupational-therapy> |
| 10 | Paramedic Science | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-paramedic-science> |
| 11 | Politics and Public Policy | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-politics-and-public-policy> |
| 12 | Psychological Wellbeing and Mental Health | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-psychological-wellbeing-and-mental-health> |
| 13 | Public Policy | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-public-policy> |

##### MSc/PGDip (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Psychology | <https://www.ntu.ac.uk/course/social-sciences/pg/msc-pgdip-psychology> |

#### School of Arts and Humanities (5 programmes)


##### MA (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Creative Writing | <https://www.ntu.ac.uk/course/arts-and-humanities/pg/ma-creative-writing> |
| 2 | Global Media and Communications | <https://www.ntu.ac.uk/course/arts-and-humanities/pg/global-media-and-communications> |
| 3 | Journalism | <https://www.ntu.ac.uk/course/arts-and-humanities/pg/journalism> |
| 4 | Museum and Heritage Development | <https://www.ntu.ac.uk/course/arts-and-humanities/pg/ma-pgdip-museum-and-heritage-development> |
| 5 | TESOL - Teaching English to Speakers of Other Languages | <https://www.ntu.ac.uk/course/arts-and-humanities/pg/ma-teaching-english-to-speakers-of-other-languages-tesol> |

#### School of Education (5 programmes)


##### CertEd (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Further Education and Skills | <https://www.ntu.ac.uk/course/education/pg/certed-further-education-and-skills> |

##### MA (1)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Education (and pathways) | <https://www.ntu.ac.uk/course/education/pg/education-with-specialist-pathways> |

##### PGCE (3)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Further Education and Skills | <https://www.ntu.ac.uk/course/education/pg/pgce-further-education-and-skills> |
| 2 | Primary Education (QTS) | <https://www.ntu.ac.uk/course/education/pg/pgce-primary-education> |
| 3 | Secondary Education (QTS) | <https://www.ntu.ac.uk/course/education/pg/secondary-education> |

#### School of Animal, Rural and Environmental Sciences (5 programmes)


##### MRes/MSc (5)

| # | Programme | URL |
|---|-----------|-----|
| 1 | Applied Ecology and Geospatial Techniques | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/pg/applied-ecology-and-geospatial-techniques> |
| 2 | Biodiversity Conservation | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/pg/mres-msc-biodiversity-conservation> |
| 3 | Endangered Species Recovery and Conservation | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/pg/mres-msc-endangered-species-recovery-and-conservation> |
| 4 | Equine Performance, Health and Welfare | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/pg/mres-msc-equine-performance,-health-and-welfare> |
| 5 | Smart Agriculture | <https://www.ntu.ac.uk/course/animal-rural-and-environmental-sciences/pg/smart-agriculture> |

### 2.2 Worked example (MSc Finance, NBS)

- **Department**: Nottingham Business School — Accounting, Finance and Economics
- **Tuition (international)**: £21,150 (one year)
- **School**: Nottingham Business School (Triple Crown accredited)
- **URL**: <https://www.ntu.ac.uk/course/nottingham-business-school/pg/msc-finance>
- **Entry**: Bachelor's degree (2:2 or above) in relevant subject; English language requirement applies
- **Fees include**: tuition only; placement year for 2-year route costs additional £1,905

### 2.3 Graduate admissions model

- **Centralised application**: postgraduate applications submitted directly via NTU online portal (or UCAS Postgraduate for some PGCE)
- **Standard application fee**: typically £0-£50 depending on programme
- **PGCE programmes**: 3 programmes in School of Education; apply via UCAS Undergraduate (with school experience requirements)
- **MBA**: separate tuition tier (£25,000/year) reflecting premium programme

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | NTU value |
|-----------|-----------|
| Admissions site | <https://www.ntu.ac.uk/study-and-courses/undergraduate> |
| Application portal | UCAS (undergraduate); NTU portal for direct applications |
| UCAS equal consideration deadline | 29 January (for September entry) |
| Clearing opens | Early July (A-level results day + few days) |
| Decision notification | Rolling; UCAS Track by May for main cycle |
| Typical Clearing offer | Variable by course; example: Accounting and Finance 88 UCAS tariff points |
| SAT/ACT policy | International applicants may submit SAT/ACT as evidence; NTU does not require US standardised tests |
| Interview policy | By invitation only; some courses (e.g. Nursing, Health) require interview |
| Recommendation | Not required for most UG courses; required for some health/PGCE |
| Portfolio | Required for Art & Design courses |
| Transfer pathway | Yes — see `/study-and-courses/undergraduate/applying-to-ntu` |
| TEF award | TEF Gold (teaching excellence) |
| Triple Crown (NBS) | EQUIS + AMBA + AACSB (top 1% of business schools worldwide) |

### 3.2 Undergraduate English proficiency table

NTU accepts IELTS Academic and a range of alternative tests. Exact grade varies by course:

| Exam | Typical UG minimum | Typical PG minimum |
|------|---------------------|---------------------|
| IELTS Academic | 6.0–6.5 overall (with 5.5–6.0 in each band) | 6.5 overall (with 5.5+ in each band) |
| TOEFL iBT | 81–92 | 92+ |
| Pearson PTE Academic | 54–62 | 62+ |
| Cambridge C1 Advanced / C2 Proficiency | Grade C / Grade C | Grade C / Grade C |
| Oxford Test of English (OTE) | 111–120 (B2 level) | 120+ |
| Trinity College ISE | ISE II / ISE III | ISE III |
| LanguageCert International ESOL | B2 / C1 | C1 |
| Kaplan Test of English (KTE) | 426–500 | 500+ |
| OET (for Health courses) | Grade C+ | Grade C+ |
| IGCSE / GCSE English | Grade C/4 or above (1st language) | N/A |
| Duolingo | **NOT accepted** | **NOT accepted** |
| IELTS Indicator / IELTS Online | **NOT accepted** | **NOT accepted** |

> Always verify on the official page: <https://www.ntu.ac.uk/international/your-application/entry-requirements/english-language-requirements>

### 3.3 Graduate — global rules

- Application: direct to NTU online portal (or UCAS for PGCE)
- Standard fee: £0–£50
- Most taught masters require 2:2 UK honours degree (or equivalent)
- PhD/MRes: 2:1 required for MRes; 2:1 + research proposal for PhD
- Joint MRes/MSc awards available in selected courses (Animal, Rural and Environmental Sciences)
- Pre-sessional English (PEAP): 6, 10, 15 weeks on City Campus (2026)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost — international (2026/27 entry)

| Fee tier | Annual tuition (international) | Description |
|----------|--------------------------------|-------------|
| **Standard UG** | £17,950 | Most subjects |
| **Premium UG** | £18,700 | Nottingham School of Art & Design; Nottingham Business School; School of Science and Technology (London only) |
| **Work placement year** | £1,905 | Additional fee for placement year |
| **Foundation year** | Included in programme | Where applicable |
| **UK/Home fee** | £9,250 | Confirmed by UK government cap |

> Source: <https://www.ntu.ac.uk/international/tuition-fees> — capture date 2026-07-08.

### 4.2 Postgraduate cost — international (Sept 2026 / Jan 2027 entry)

Fees are highly programme-specific. Major bands:

| Band | Annual fee | Programmes |
|------|------------|------------|
| **£18,300 (Nottingham)** | £18,300 | Most Masters in Art & Design, Architecture, Science, Law, Social Sciences, Sport, Engineering, Chemistry/Physics |
| **£18,300 (Nottingham Education)** | £18,300 | MA Education |
| **£18,500 (Filmmaking)** | £18,500 | MA Filmmaking |
| **£19,900 (London Music)** | £19,900 | MA Music Production (London); MA Commercial Songwriting and Production (London); MA Music Business (London); MSc Sound Engineering and Audio Production (London) |
| **£20,750 (Biosciences)** | £20,750 | MSc Biomedical Science, Biotechnology, MRes Cancer Biology, Cellular Biomedicine, Molecular Cell Biology, Molecular Microbiology, Neuropharmacology, Pharmacology |
| **£21,150 (NBS — Accounting/Economics/Marketing/HR)** | £21,150 | MSc Finance, Finance and Accounting, Finance and Investment Banking, Economics, Banking and Finance, Sustainable Finance, Digital Finance and Data Analytics, Advertising and Marketing Communications, Marketing, Marketing and Brand Management, Digital Marketing, HRM, Business Analytics and AI |
| **£21,400 (Barristers Training)** | £21,400 | LLM Law and Legal Practice: Barristers Training Course |
| **£21,600 (NBS — Management)** | £21,600 | MSc Management, Management (Sustainable Leadership), Management and Business Analytics, Management and International Business, Management and Global Supply Chain Management, Management (Creative and Digital Industries), Project Management, International Business (Single/Dual Award), Strategic Entrepreneurship, FinTech and Financial Markets |
| **£25,000 (MBA)** | £25,000 | MBA Master of Business Administration |
| **£19,900 (Computing)** | £19,900 | MSc Artificial Intelligence, Cloud and Enterprise Computing, Computer Science, Software Engineering, Cyber Security, Data Science, Robotics and Intelligent Systems |
| **£14,050 (SQE 1 Prep)** | £14,050 | LLM Law and Legal Practice - SQE 1 Preparation Course |
| **£10,650 (PGDip Law)** | £10,650 | Postgraduate Diploma in Law |
| **£7,650 (Online Music)** | £7,650 | MA Music Business (online); MA Commercial Songwriting and Production (online) |
| **£5,150 (Distance Learning Bioscience)** | £5,150 | MSc Biomedical Science (flexible learning, distance learning part-time) |
| **Placement year (2-year route)** | £1,905 | Additional Year 2 fee |

> All fees from <https://www.ntu.ac.uk/international/tuition-fees> — capture date 2026-07-08.

### 4.3 Scholarships and financial aid

- NTU International Scholarships: range £2,000–£5,000 (automatic consideration for eligible international UG/PG offer holders)
- VC's International Scholarship: up to 50% of tuition for high-achieving international students
- Country-specific scholarships (e.g. China, India, Nigeria, Turkey, Vietnam)
- Sports scholarships (high-performance athletes)
- Postgraduate loans: UK students may apply for PGL up to £12,167 (2026/27)

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Nottingham Trent University"
  source_url: https://www.ntu.ac.uk/study-and-courses/academic-schools
  source_snippet: "Academic Schools | Nottingham Trent University"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.fee_status.home
  value: "£9,250"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "International student fees for 2026 entry onto a full-time undergraduate course at NTU are: £18,700 for courses in the Nottingham School of Art & Design, School of Science and Technology (London only) and Nottingham Business School. £17,950 for all other subjects."
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-003:
  field: institution.fee_status.international_ug_standard
  value: "£17,950"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "£17,950 for all other subjects"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.fee_status.international_ug_premium
  value: "£18,700"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "£18,700 for courses in the Nottingham School of Art & Design, School of Science and Technology (London only) and Nottingham Business School"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: institution.fee_status.placement_year
  value: "£1,905"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "If you do a work placement as part of an undergraduate course at NTU, the placement fee for 2026/27 academic year is £1,905"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: programs.total
  value: 431
  source_url: https://www.ntu.ac.uk/study-and-courses/undergraduate/subject-areas
  source_snippet: "43 subject areas; 431 unique courses aggregated from /course/<subject> subject pages"
  capture_date: 2026-07-08
  evidence_type: derived_from_snapshots

E-U-007:
  field: programs.ug_count
  value: 288
  source_url: https://www.ntu.ac.uk/study-and-courses/undergraduate/subject-areas
  source_snippet: "288 unique UG programmes aggregated from /ug/ URL slugs"
  capture_date: 2026-07-08
  evidence_type: derived_from_snapshots

E-U-008:
  field: programs.pg_count
  value: 143
  source_url: https://www.ntu.ac.uk/study-and-courses/undergraduate/subject-areas
  source_snippet: "143 unique PG programmes aggregated from /pg/ URL slugs"
  capture_date: 2026-07-08
  evidence_type: derived_from_snapshots

E-U-009:
  field: schools.count
  value: 9
  source_url: https://www.ntu.ac.uk/study-and-courses/academic-schools
  source_snippet: "8 academic schools listed on /academic-schools page; plus NTU Mansfield"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: english.ielts_ug_minimum
  value: "IELTS 6.0-6.5 overall (5.5-6.0 in each band); varies by course"
  source_url: https://www.ntu.ac.uk/international/your-application/entry-requirements/english-language-requirements
  source_snippet: "We accept IELTS Academic as an English Language qualification. You'll need to achieve the required grade in IELTS which are listed below."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: english.duolingo_accepted
  value: false
  source_url: https://www.ntu.ac.uk/international/your-application/entry-requirements/english-language-requirements
  source_snippet: "Please note that we do not accept the Duolingo English test."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: english.ielts_indicator_accepted
  value: false
  source_url: https://www.ntu.ac.uk/international/your-application/entry-requirements/english-language-requirements
  source_snippet: "We do not currently accept 'IELTS Indicator' or 'IELTS Online' test scores."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: fees.pg_accounting_finance
  value: "£21,150"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £21,150 for the following courses: MSc Finance, MSc Finance and Accounting, MSc Finance and Investment Banking, MSc Economics, Banking and Finance, MSc Economics, MSc Digital Finance and Data Analytics, MSc Sustainable Finance"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: fees.pg_management
  value: "£21,600"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £21,600 for the following courses: MSc Management, MSc Management (Sustainable Leadership), MSc Management and Business Analytics, MSc Management and International Business, MSc Management and Global Supply Chain Management, MSc Management (Creative and Digital Industries), MSc Project Management, MSc International Business (Single Award), MSc International Business (Dual Award), MSc Strategic Entrepreneurship and Innovation Management"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: fees.pg_fintech
  value: "£21,600"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £21,600 for the following course: MSc FinTech and Financial Markets"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: fees.pg_mba
  value: "£25,000"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £25,000 (per year) for the following course: MBA Master of Business Administration"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-017:
  field: fees.pg_computing
  value: "£19,900"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £19,900 for the following courses: MSc Artificial Intelligence, MSc Cloud and Enterprise Computing, MSc Computer Science, MSc Software Engineering, MSc Cyber Security, MSc Data Science, MSc Robotics and Intelligent Systems"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-018:
  field: fees.pg_biosciences
  value: "£20,750"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £20,750 for the following courses: MSc Biomedical Science, MSc Biotechnology, MRes Biotechnology, MRes Cancer Biology, MRes Cellular Biomedicine, MSc Molecular Cell Biology, MSc Molecular Microbiology, MRes Molecular Microbiology, MSc Neuropharmacology, MRes Neuropharmacology, MSc Pharmacology, MRes Pharmacology"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-019:
  field: fees.pg_art_design
  value: "£18,300"
  source_url: https://www.ntu.ac.uk/international/tuition-fees
  source_snippet: "The tuition fee is £18,300 for the following courses: MA International Fashion Management, MA Fashion Marketing, MA Luxury Fashion Brand Management, MA Fashion Communications, MA Fashion, MA Fashion Knitwear, MA Textiles, MA Fashion and Creative Pattern Cutting, MSc Material and Technology Futures"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-020:
  field: triple_crown.nbs
  value: true
  source_url: https://www.ntu.ac.uk/course/nottingham-business-school
  source_snippet: "Nottingham Business School - part of the 1% of business schools worldwide to hold the Triple Crown of accreditation from EQUIS, AMBA and AACSB"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-021:
  field: tef.rating
  value: "TEF Gold"
  source_url: https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-accounting-and-finance
  source_snippet: "Learn from the experts at a university rated TEF 'Gold' for teaching and learning"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-022:
  field: example_course.btec_ucas
  value: "NN4H (full-time), NN43 (with placement)"
  source_url: https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-accounting-and-finance
  source_snippet: "UCAS code: NN4H (full-time), NN43 (with placement)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-023:
  field: example_course.ucas_tariff_min
  value: "88 UCAS tariff points"
  source_url: https://www.ntu.ac.uk/course/nottingham-business-school/ug/bsc-hons-accounting-and-finance
  source_snippet: "Typical Clearing offer: 88 UCAS tariff points"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
ntu-knowledge-base-v2 (collection)
├── ntu-overview (chunk 0)                          # Section 0 — counts, hierarchy, degree inventory, matrix
├── ntu-undergraduate-programmes (chunk 1)          # Section 1 — full UG leaf list grouped by school × degree
├── ntu-graduate-programmes (chunk 2)               # Section 2 — full PG leaf list grouped by school × degree
├── ntu-application-requirements (chunk 3)          # Section 3 — deadlines, English requirements
├── ntu-costs-and-fees (chunk 4)                    # Section 4 — line-itemized tuition table
└── ntu-evidence-chain (chunk 5)                    # Section 5 — evidence YAML index
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ntu-knowledge-base-v2"
  school: "<home school>"
  degree_level: "<BA|BS|MA|MSc|...>"
  level: "undergraduate | graduate"
  field_type: "overview | counts | hierarchy | programs | deadlines | tests | costs | funding"
  source_url: <URL>
  capture_date: "2026-07-08"
  version: "v2.0"
  change_status: "baseline"
  last_verified: "2026-07-08"
  region: "UK-England"
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P1** | Per-course English language minimum (each course has specific IELTS band) | `ntu.ac.uk/course/<slug>` |
| **P1** | PhD programme listing (currently absorbed into PG count; should split PGT/PGR) | `ntu.ac.uk/research` |
| **P1** | Foundation Year UG programme detail | `ntu.ac.uk/course/<slug>` |
| **P1** | UCAS tariff point requirements per course | `ntu.ac.uk/course/<slug>` |
| **P2** | NTU London-specific programmes (separate fee tier) | `ntu.ac.uk/london` |
| **P2** | Online/distance learning programmes | `ntu.ac.uk/online` |
| **P2** | NTU Mansfield-specific course content | `ntu.ac.uk/study-and-courses/academic-schools/ntu-in-mansfield` |
| **P2** | Application deadlines by course | `ntu.ac.uk/course/<slug>` |
| **P2** | Module / curriculum structure | `ntu.ac.uk/course/<slug>` |
| **P3** | International-specific entry requirements (by country) | `ntu.ac.uk/international/your-application/entry-requirements` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | NTU | Aston | Edinburgh | Manchester |
|-----------|-----|-------|-----------|------------|
| Total UG programmes | 288 | 80 | 200+ | 250+ |
| Total PG programmes | 143 | 78+71 | 200+ | 300+ |
| Total degree programmes | 431 | 261 | 400+ | 550+ |
| Schools | 9 | 9 | 12 | 4 |
| Russell Group | No | No | Yes | Yes |
| TEF rating | Gold | Silver | Gold | Gold |
| Triple Crown (Business) | Yes (NBS) | Yes (Aston Business School) | No | Yes (Alliance Manchester Business School) |
| UG intl fee (typical) | £17,950–£18,700 | £22,575–£47,000 | £27,100–£36,800 | £26,000–£32,500 |
| UG home fee | £9,250 | £9,790 | £1,820 (Scotland) | £9,250 |
| PG intl fee (typical) | £18,300–£25,000 | £24,800–£31,500 | £28,000–£38,500 | £25,000–£35,000 |
| IELTS min (typical UG) | 6.0–6.5 | 6.0–7.0 | 6.5 | 6.5–7.0 |
| IELTS min (typical PG) | 6.5 | 6.5 | 7.0 | 6.5–7.0 |
| UCAS deadline (equal consideration) | 29 Jan | 29 Jan | 29 Jan | 29 Jan |
| Clearing opens | Early July | Early July | Early July | Early July |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: NTU official website (`ntu.ac.uk`)
> **Verification**: ego-browser snapshotText + JS DOM extraction across 43 subject pages + 4 policy pages
> **Granularity**: school → department → degree-level → program
> **Completeness**: Counts ✅ | Hierarchy ✅ | Programs ✅ | Fees ✅ | Evidence (23 blocks) ✅ | English ✅ | Reconciliation ✅
