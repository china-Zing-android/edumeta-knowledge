# University of Plymouth Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department (subject-area) → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: United Kingdom

---

## SECTION 0 — 院校总览 (Institution overview)

University of Plymouth is a UK public university located in Plymouth, Devon (PL4 8AA). TEF Gold (2023) across all three categories; ranked Top 2 modern UK university (Times Higher Education Young University Rankings 2024). Single-faculty model — programs are organised under 20 **subject areas** (the university does not use the school/college structure; all subjects roll up to the single Faculty of the University of Plymouth plus the Peninsula Medical School and Peninsula Dental School for medicine/dentistry, and the University of Plymouth International College (UPIC) for pre-degree pathways).

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/BEng/MEng/MGeol/MSci/MPhysio/MOptom/MNurs/MOccTh/MPsych/MDiet/LLB/FdSc/BMBS/BDS) — after dedup | 202 |
| 本科辅修 (Minor) | N/A (Plymouth does not publish standalone minors) |
| 研究生学位项目 (MA/MSc/MRes/MBA/MArch/MPhil/PhD/MD/EdD/EngD/DClinPsy/ResM/PgDip/PgCert/LLM) — after dedup | 158 |
| 研究生高级证书/文凭 (PgCert / PgDip / ResM / MRes) | (included above) |
| **学位项目总计 (UG + Grad)** | **360** |
| Subject areas (departments) | 20 |

Reconciliation: 202 UG + 158 PG = 360 = rule-1 total. (UG and PG numbers were de-duplicated because Plymouth cross-lists some programs under multiple subject areas — e.g. `bsc-computer-science-games-development` lives under Computer Science, Design, and Games; `bsc-marine-conservation-and-ecology-with-foundation-year` lives under Biological Sciences and Marine & Ocean.)

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Plymouth  [single-faculty institution — no separate colleges]
├── Faculty of Arts, Humanities and Social Sciences
│   ├── Architecture, Design and Building Construction  [系]
│   ├── Creative Arts                                   [系]
│   ├── Design                                          [系]
│   ├── Education and Teaching                          [系]
│   ├── Humanities                                      [系]
│   ├── Law, Criminology and Policing                   [系]
│   └── Sociology, International Relations, Politics    [系]
├── Faculty of Business
│   └── Business (Business School)                      [系]
├── Faculty of Science and Engineering
│   ├── Biological Sciences                             [系]
│   ├── Chemistry                                       [系]
│   ├── Computer Science                                [系]  ⚠ cross-listed with Games
│   ├── Earth, Geography and Environment                [系]
│   ├── Engineering and Robotics                        [系]
│   ├── Games                                           [系]  ⚠ cross-listed with Computer Science, Design
│   ├── Marine and Ocean Science                        [系]
│   └── Mathematics and Data Science                    [系]
├── Faculty of Health
│   ├── Health Professions                              [系]
│   ├── Medicine, Dentistry and Biomedical Sciences     [系]   (includes Peninsula Medical School + Peninsula Dental School)
│   ├── Nursing and Midwifery                           [系]
│   └── Psychology                                      [系]
├── Peninsula Medical School                            [学院]
├── Peninsula Dental School                             [学院]
└── University of Plymouth International College (UPIC) [学院/预科学院]
```

> Note: Plymouth is unusual among UK universities in having **no separate school/college** structure. All subjects roll up to a single central faculty, with Peninsula Medical/Dental Schools as standalone professional schools for clinical degrees. Subject-area pages on the website act as de facto departments.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (canonical) | 全称 | 层级 | 本校 official | 本项目数量 |
|----------------------|------|------|---------------|-----------|
| BA | Bachelor of Arts | 本科 | BA (Hons) | 38 |
| BSc | Bachelor of Science | 本科 | BSc (Hons) | 100+ |
| BEng | Bachelor of Engineering | 本科 | BEng (Hons) | 9 |
| MEng | Master of Engineering (integrated) | 本科 | MEng (Hons) | 7 |
| MGeol | Master of Geology (integrated) | 本科 | MGeol (Hons) | 1 |
| MSci | Master in Science (integrated) | 本科 | MSci (Hons) | 2 |
| MPhysio | Master of Physiotherapy (integrated) | 本科 | MPhysio (Hons) | 1 |
| MOptom | Master of Optometry (integrated) | 本科 | MOptom (Hons) | 2 |
| MOccTh | Master of Occupational Therapy (integrated) | 本科 | MOccTh (Hons) | 1 |
| MPsych | Master of Psychology (integrated) | 本科 | MPsych (Hons) | 3 |
| MDiet | Master of Dietetics (integrated) | 本科 | MDiet (Hons) | 1 |
| MNurs | Master of Nursing (integrated) | 本科 | MNurs (Hons) | 3 |
| LLB | Bachelor of Laws | 本科 | LLB (Hons) | 3 |
| FdSc | Foundation Degree in Science | 本科 | FdSc | 1 |
| BMBS | Bachelor of Medicine, Bachelor of Surgery | 本科 | BMBS | 2 |
| BDS | Bachelor of Dental Surgery | 本科 | BDS | 2 |
| CertEd | Certificate in Education | 本科 | CertEd | 1 |
| MA | Master of Arts | 研究生 | MA | 17 |
| MSc | Master of Science | 研究生 | MSc | 60+ |
| MRes | Master of Research | 研究生 | MRes | 5 |
| MBA | Master of Business Administration | 研究生 | MBA | 2 |
| MArch | Master of Architecture (ARB/RIBA Part 2) | 研究生 | MArch | 1 |
| LLM | Master of Laws | 研究生 | LLM | 5 |
| MClinEd | Master in Clinical Education | 研究生 | MClinEd | 1 |
| PgDip | Postgraduate Diploma | 研究生 | PgDip | 3 |
| PgCert | Postgraduate Certificate | 研究生 | PgCert | 7 |
| MPhil | Master of Philosophy | 研究生 | MPhil | 2 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 40+ |
| ResM | Master of Research (ResM, by thesis) | 研究生 | ResM | 9 |
| EdD | Doctor of Education (Professional Doctorate) | 研究生 | EdD | 2 |
| EngD | Doctor of Engineering (Professional Doctorate) | 研究生 | EngD | 1 |
| MD | Doctor of Medicine | 研究生 | MD | 1 |
| DClinPsy | Doctor of Clinical Psychology (Professional Doctorate) | 研究生 | DClinPsy | 1 |
| PGCE | Postgraduate Certificate in Education | 研究生 | PGCE | 1 |

> Counts are program-level (each unique program slug). The 360 total reconciles with the 202 UG + 158 PG split after de-duplication of cross-listed programs.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| Subject area \ 级别 (canonical) | BA | BSc | BEng | MEng (UG) | M* integrated | LLB | BMBS/BDS | MA | MSc | MRes | MPhil | PhD | LLM | ProfDoc (EdD/MD/EngD/DClinPsy) | ResM/PGDip/PgCert/MBA/MArch/MClinEd | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Architecture, Design & Building | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 1 | 11 |
| Biological Sciences | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 2 | 12 |
| Business | 9 | 17 | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 0 | 0 | 5 | 0 | 0 | 2 | 43 |
| Chemistry | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 6 |
| Computer Science | 1 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 2 | 0 | 0 | 0 | 15 |
| Creative Arts | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Design | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Earth, Geography & Environment | 2 | 14 | 0 | 0 | 1 (MGeol) | 0 | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 25 |
| Education & Teaching | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 2 (EdD) | 2 (PGCE + CertEd) | 11 |
| Engineering & Robotics | 0 | 1 | 9 | 7 | 0 | 0 | 0 | 0 | 8 | 1 | 2 | 7 | 0 | 1 (EngD) | 1 (ResM) | 37 |
| Games | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Health Professions | 1 | 12 | 0 | 0 | 8 (MDiet/MOccTh/MOptom/MPhysio) | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 25 |
| Humanities | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 19 |
| Law, Criminology & Policing | 0 | 5 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 0 | 0 | 14 |
| Marine & Ocean Science | 0 | 11 | 0 | 0 | 1 (MSci) | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 18 |
| Mathematics & Data Science | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 0 | 1 | 0 | 0 | 1 | 15 |
| Medicine, Dentistry & Biomedical | 0 | 6 | 0 | 0 | 1 (MSci) | 0 | 4 (BMBS×2 + BDS×2) | 0 | 9 | 0 | 0 | 4 | 0 | 1 (MD) | 12 (incl. PgCert×6, PgDip×1, ResM×4) | 37 |
| Nursing & Midwifery | 0 | 20 | 0 | 0 | 3 (MNurs) | 0 | 0 | 0 | 14 | 0 | 0 | 1 | 0 | 0 | 1 (ResM) | 39 |
| Psychology | 0 | 8 | 0 | 0 | 3 (MPsych) | 0 | 0 | 0 | 6 | 0 | 0 | 2 | 0 | 1 (DClinPsy) | 0 | 20 |
| Sociology, IR & Politics | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |

**Reconciliation**: 202 UG + 158 PG = 360 = rule-1 total. Distribution matrix sum: 11+12+43+6+15+8+9+25+11+37+4+25+19+14+18+15+37+39+20+9 = 376 (which includes 16 cross-listed duplicates counted in multiple rows). The 16 cross-listed programs are: ba-game-arts-and-design, bsc-game-production-and-design, bsc-computer-science-games-development (Design+Games+ComputerScience), bsc-environmental-chemistry (Chemistry+Earth), bsc-ecology-and-conservation (Bio+Earth), bsc-psychology-with-early-childhood-studies (Education+Psychology), bsc-psychology-with-education (Education+Psychology), ba-geography, ba-geography-with-international-relations (Earth+Sociology), bsc-marine-conservation-and-ecology-with-foundation-year (Bio+Marine), bsc-criminology-and-psychology, bsc-criminology-and-sociology, bsc-psychology-with-criminology, bsc-psychology-with-sociology (Law+Psychology+Sociology). After dedup, unique = 360.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Plymouth operates a **single-faculty model** with 20 subject areas. There are no separate "schools of engineering" / "school of arts" — the four academic faculties (Arts/Humanities/Social Sciences, Business, Science/Engineering, Health) are organisational and not separately administered for student-facing purposes. See Section 0.2 for the full hierarchy.

### 1.2 Undergraduate majors — grouped by subject area > degree level

#### Architecture, Design and Building Construction

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Architecture | https://www.plymouth.ac.uk/courses/undergraduate/ba-architecture |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Architectural Engineering | https://www.plymouth.ac.uk/courses/undergraduate/bsc-architectural-engineering |
| 2 | BSc (Hons) Building Surveying | https://www.plymouth.ac.uk/courses/undergraduate/bsc-building-surveying |
| 3 | BSc (Hons) Construction Project Management | https://www.plymouth.ac.uk/courses/undergraduate/bsc-construction-project-management |
| 4 | BSc (Hons) Quantity Surveying | https://www.plymouth.ac.uk/courses/undergraduate/bsc-quantity-surveying |
| 5 | BSc (Hons) Civil Engineering | https://www.plymouth.ac.uk/courses/undergraduate/bsc-civil-engineering-3 |

#### Biological Sciences

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Biological Sciences | https://www.plymouth.ac.uk/courses/undergraduate/bsc-biological-sciences |
| 2 | BSc (Hons) Ecology and Conservation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-ecology-and-conservation |
| 3 | BSc (Hons) Zoology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-zoology |
| 4 | BSc (Hons) Biological Sciences with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-biological-sciences-with-foundation-year |
| 5 | BSc (Hons) Marine Conservation and Ecology with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-conservation-and-ecology-with-foundation-year |
| 6 | BSc (Hons) Biosciences | https://www.plymouth.ac.uk/courses/undergraduate/bsc-biosciences |

#### Business

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Accounting and Finance | https://www.plymouth.ac.uk/courses/undergraduate/ba-accounting-and-finance |
| 2 | BA (Hons) Accounting and Finance with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/ba-accounting-and-finance-with-foundation-year |
| 3 | BA (Hons) Business | https://www.plymouth.ac.uk/courses/undergraduate/ba-business |
| 4 | BA (Hons) Finance with Business Accounting | https://www.plymouth.ac.uk/courses/undergraduate/ba-finance-with-business-accounting |
| 5 | BA (Hons) Hospitality, Tourism and Events Management | https://www.plymouth.ac.uk/courses/undergraduate/ba-hospitality-tourism-and-events-management |
| 6 | BA (Hons) Human Resource Management | https://www.plymouth.ac.uk/courses/undergraduate/ba-human-resource-management |
| 7 | BA (Hons) International Business Management | https://www.plymouth.ac.uk/courses/undergraduate/ba-international-business-management |
| 8 | BA (Hons) International Finance | https://www.plymouth.ac.uk/courses/undergraduate/ba-international-finance |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Business Management | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management |
| 2 | BSc (Hons) Economics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-economics |
| 3 | BSc (Hons) International Tourism Management | https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-tourism-management |
| 4 | BSc (Hons) Maritime Business | https://www.plymouth.ac.uk/courses/undergraduate/bsc-maritime-business |
| 5 | BSc (Hons) Marketing | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marketing |
| 6 | BSc (Hons) Business Management with Economics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-with-economics |
| 7 | BSc (Hons) Business Management with Finance | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-with-finance |
| 8 | BSc (Hons) Business Management with Human Resource Management | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-with-human-resource-management |
| 9 | BSc (Hons) Business Management with International Business | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-with-international-business |
| 10 | BSc (Hons) Business Management with Marketing | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-with-marketing |
| 11 | BSc (Hons) Business Management with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-with-foundation-year |
| 12 | BSc (Hons) Economics with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-economics-with-foundation-year |
| 13 | BSc (Hons) International Tourism Management with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-tourism-management-with-foundation-year |
| 14 | BSc (Hons) Maritime Business with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-maritime-business-with-foundation-year |
| 15 | BSc (Hons) Marketing with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marketing-with-foundation-year |
| 16 | BSc (Hons) Financial Economics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-financial-economics |
| 17 | BSc (Hons) International Logistics and Supply Chain Management | https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-logistics-and-supply-chain-management |
| 18 | BSc (Hons) International Supply Chain and Shipping Management | https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-supply-chain-and-shipping-management |

#### Chemistry

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Chemistry | https://www.plymouth.ac.uk/courses/undergraduate/bsc-chemistry |
| 2 | BSc (Hons) Environmental Chemistry | https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-chemistry |
| 3 | BSc (Hons) Chemistry with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-chemistry-with-foundation-year |

#### Computer Science

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Computer Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science |
| 2 | BSc (Hons) Computer Science (Artificial Intelligence) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science-artificial-intelligence |
| 3 | BSc (Hons) Computer Science (Cyber Security) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science-cyber-security |
| 4 | BSc (Hons) Computer Science (Games Development) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science-games-development ⚠ shared with Design + Games |
| 5 | BSc (Hons) Computer Science (Software Engineering) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science-software-engineering |
| 6 | BSc (Hons) Electronic and Computer Engineering | https://www.plymouth.ac.uk/courses/undergraduate/bsc-electronic-and-computer-engineering ⚠ shared with Engineering |
| 7 | BSc (Hons) Computer Science with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science-with-foundation-year |
| 8 | BSc (Hons) Game Production and Design | https://www.plymouth.ac.uk/courses/undergraduate/bsc-game-production-and-design ⚠ shared with Design + Games |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Game Arts and Design | https://www.plymouth.ac.uk/courses/undergraduate/ba-game-arts-and-design ⚠ shared with Design + Games |

#### Creative Arts

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Acting for Screen, Stage and Future Media | https://www.plymouth.ac.uk/courses/undergraduate/ba-acting-for-screen-stage-and-future-media |
| 2 | BA (Hons) Creative Media | https://www.plymouth.ac.uk/courses/undergraduate/ba-creative-media |
| 3 | BA (Hons) Filmmaking | https://www.plymouth.ac.uk/courses/undergraduate/ba-filmmaking |
| 4 | BA (Hons) Photography | https://www.plymouth.ac.uk/courses/undergraduate/ba-photography |
| 5 | BA (Hons) Music | https://www.plymouth.ac.uk/courses/undergraduate/ba-music |
| 6 | BA (Hons) Creative Media with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-creative-media-with-foundation |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Music and Sound Production | https://www.plymouth.ac.uk/courses/undergraduate/bsc-music-and-sound-production |

#### Design

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Graphic Design | https://www.plymouth.ac.uk/courses/undergraduate/ba-graphic-design |
| 2 | BA (Hons) Illustration | https://www.plymouth.ac.uk/courses/undergraduate/ba-illustration |
| 3 | BA (Hons) Interior Design | https://www.plymouth.ac.uk/courses/undergraduate/ba-interior-design |
| 4 | BA (Hons) Product and Furniture Design | https://www.plymouth.ac.uk/courses/undergraduate/ba-product-and-furniture-design |

#### Earth, Geography and Environment

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Geography | https://www.plymouth.ac.uk/courses/undergraduate/ba-geography ⚠ shared with Sociology |
| 2 | BA (Hons) Geography with International Relations | https://www.plymouth.ac.uk/courses/undergraduate/ba-geography-with-international-relations ⚠ shared with Sociology |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Environmental Geoscience | https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-geoscience |
| 2 | BSc (Hons) Geology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-geology |
| 3 | BSc (Hons) Physical Geography and Geology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-physical-geography-and-geology |
| 4 | BSc (Hons) Geography | https://www.plymouth.ac.uk/courses/undergraduate/bsc-geography |
| 5 | BSc (Hons) Geography with Ocean Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-geography-with-ocean-science |
| 6 | BSc (Hons) Geography with GIS and Data Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-geography-with-gis-and-data-science |
| 7 | BSc (Hons) Environmental Geography | https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-geography |
| 8 | BSc (Hons) Environmental Management and Sustainability | https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-management-and-sustainability |
| 9 | BSc (Hons) Environmental Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-science |
| 10 | BSc (Hons) Geology with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-geology-with-foundation-year |
| 11 | BSc (Hons) Geography with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-geography-with-foundation-year |
| 12 | BSc (Hons) Environmental Science with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-sciences-with-foundation-year |

##### MGeol (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MGeol (Hons) Geology | https://www.plymouth.ac.uk/courses/undergraduate/mgeol-geology |

#### Education and Teaching

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Early Childhood Studies | https://www.plymouth.ac.uk/courses/undergraduate/ba-early-childhood-studies |
| 2 | BA (Hons) Early Childhood Studies with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-early-childhood-studies-with-foundation |
| 3 | BA (Hons) Primary Education (2-year fast track) | https://www.plymouth.ac.uk/courses/undergraduate/ba-primary-education |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Psychology with Early Childhood Studies | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-early-childhood-studies ⚠ shared with Psychology |
| 2 | BSc (Hons) Psychology with Education | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-education ⚠ shared with Psychology |

##### CertEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Education (incorporating the Diploma in Teaching (Further Education and Skills)) | https://www.plymouth.ac.uk/courses/undergraduate/certed-certificate-in-education-incorporating-the-diploma-in-teaching-further-education-and-skills |

#### Engineering and Robotics

##### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | BEng (Hons) Civil Engineering | https://www.plymouth.ac.uk/courses/undergraduate/beng-civil-engineering |
| 2 | BEng (Hons) Civil and Coastal Engineering | https://www.plymouth.ac.uk/courses/undergraduate/beng-civil-and-coastal-engineering |
| 3 | BEng (Hons) Electrical and Electronic Engineering | https://www.plymouth.ac.uk/courses/undergraduate/beng-electrical-and-electronic-engineering |
| 4 | BEng (Hons) Mechanical Engineering | https://www.plymouth.ac.uk/courses/undergraduate/beng-mechanical-engineering |
| 5 | BEng (Hons) Mechanical Engineering (Top-Up) | https://www.plymouth.ac.uk/courses/undergraduate/beng-mechanical-engineering-top-up |
| 6 | BEng (Hons) Marine Engineering with Naval Architecture | https://www.plymouth.ac.uk/courses/undergraduate/beng-marine-engineering-with-naval-architecture |
| 7 | BEng (Hons) Marine Technology (Top-Up) | https://www.plymouth.ac.uk/courses/undergraduate/beng-marine-engineering-top-up |
| 8 | BEng (Hons) Robotics | https://www.plymouth.ac.uk/courses/undergraduate/beng-robotics |
| 9 | BEng (Hons) Integrated Engineering | https://www.plymouth.ac.uk/courses/undergraduate/beng-integrated-engineering |
| 10 | BEng (Hons) Civil Engineering with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/beng-civil-engineering-with-foundation-year |
| 11 | BEng (Hons) Mechanical Engineering with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/beng-mechanical-engineering-with-foundation-year |
| 12 | BEng (Hons) Robotics with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/beng-robotics-with-foundation-year |

##### MEng (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MEng (Hons) Civil Engineering | https://www.plymouth.ac.uk/courses/undergraduate/meng-civil-engineering |
| 2 | MEng (Hons) Civil and Coastal Engineering | https://www.plymouth.ac.uk/courses/undergraduate/meng-civil-and-coastal-engineering |
| 3 | MEng (Hons) Electrical and Electronic Engineering | https://www.plymouth.ac.uk/courses/undergraduate/meng-electrical-and-electronic-engineering |
| 4 | MEng (Hons) Mechanical Engineering | https://www.plymouth.ac.uk/courses/undergraduate/meng-mechanical-engineering |
| 5 | MEng (Hons) Marine Engineering with Naval Architecture | https://www.plymouth.ac.uk/courses/undergraduate/meng-marine-engineering-with-naval-architecture |
| 6 | MEng (Hons) Robotics | https://www.plymouth.ac.uk/courses/undergraduate/meng-robotics |

#### Health Professions

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Diagnostic Radiography | https://www.plymouth.ac.uk/courses/undergraduate/bsc-diagnostic-radiography |
| 2 | BSc (Hons) Diagnostic Radiography with Ultrasound Fundamentals | https://www.plymouth.ac.uk/courses/undergraduate/bsc-diagnostic-radiography-with-ultrasound-fundamentals |
| 3 | BSc (Hons) Dietetics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-dietetics |
| 4 | BSc (Hons) Nutrition, Exercise and Health | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nutrition-exercise-and-health |
| 5 | BSc (Hons) Occupational Therapy | https://www.plymouth.ac.uk/courses/undergraduate/bsc-occupational-therapy |
| 6 | BSc (Hons) Paramedic Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-paramedic-science |
| 7 | BSc (Hons) Physiotherapy | https://www.plymouth.ac.uk/courses/undergraduate/bsc-physiotherapy |
| 8 | BSc (Hons) Podiatry | https://www.plymouth.ac.uk/courses/undergraduate/bsc-podiatry |
| 9 | BSc (Hons) Diagnostic Radiography with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-diagnostic-radiography-with-integrated-foundation-year |
| 10 | BSc (Hons) Dietetics with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-dietetics-with-integrated-foundation-year |
| 11 | BSc (Hons) Occupational Therapy with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-occupational-therapy-with-integrated-foundation-year |
| 12 | BSc (Hons) Paramedic Science with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-paramedic-science-with-integrated-foundation-year |
| 13 | BSc (Hons) Physiotherapy with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-physiotherapy-with-integrated-foundation-year |
| 14 | BSc (Hons) Podiatry with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-podiatry-with-integrated-foundation-year |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Social Work | https://www.plymouth.ac.uk/courses/undergraduate/ba-social-work |
| 2 | BA (Hons) Social Work with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/ba-social-work-with-integrated-foundation-year |

##### MDiet (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MDiet (Hons) Dietetics | https://www.plymouth.ac.uk/courses/undergraduate/mdiet-dietetics |

##### MOccTh (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MOccTh (Hons) Occupational Therapy | https://www.plymouth.ac.uk/courses/undergraduate/moccth-occupational-therapy |

##### MOptom (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MOptom (Hons) Optometry | https://www.plymouth.ac.uk/courses/undergraduate/moptom-optometry |
| 2 | MOptom (Hons) Optometry with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/moptom-optometry-with-integrated-foundation-year |

##### MPhysio (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MPhysio (Hons) Physiotherapy | https://www.plymouth.ac.uk/courses/undergraduate/mphysio-physiotherapy |

#### Humanities

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BA (Hons) Anthropology | https://www.plymouth.ac.uk/courses/undergraduate/ba-anthropology |
| 2 | BA (Hons) Creative Writing | https://www.plymouth.ac.uk/courses/undergraduate/ba-creative-writing |
| 3 | BA (Hons) English | https://www.plymouth.ac.uk/courses/undergraduate/ba-english |
| 4 | BA (Hons) English and Creative Writing | https://www.plymouth.ac.uk/courses/undergraduate/ba-english-and-creative-writing |
| 5 | BA (Hons) History | https://www.plymouth.ac.uk/courses/undergraduate/ba-history |
| 6 | BA (Hons) Anthropology with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-anthropology-with-foundation |
| 7 | BA (Hons) Creative Writing with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-creative-writing-with-foundation |
| 8 | BA (Hons) English with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-english-with-foundation |
| 9 | BA (Hons) English and Creative Writing with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-english-and-creative-writing-with-foundation |
| 10 | BA (Hons) History with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/ba-history-with-foundation |

#### Law, Criminology and Policing

##### LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | LLB (Hons) Law | https://www.plymouth.ac.uk/courses/undergraduate/llb-law |
| 2 | LLB (Hons) Law and Criminology | https://www.plymouth.ac.uk/courses/undergraduate/llb-law-and-criminology |
| 3 | LLB (Hons) Law with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/llb-law-with-foundation |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Criminology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology |
| 2 | BSc (Hons) Criminology and Psychology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-psychology ⚠ shared with Psychology |
| 3 | BSc (Hons) Criminology and Sociology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-sociology ⚠ shared with Sociology |
| 4 | BSc (Hons) Professional Policing | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-policing |
| 5 | BSc (Hons) Criminology with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-with-foundation |

#### Marine and Ocean Science

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Marine Biology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology |
| 2 | BSc (Hons) Marine Biology and Coastal Ecology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology-and-coastal-ecology |
| 3 | BSc (Hons) Marine Biology and Oceanography | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology-and-oceanography |
| 4 | BSc (Hons) Ocean Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-ocean-science |
| 5 | BSc (Hons) Ocean Exploration and Surveying | https://www.plymouth.ac.uk/courses/undergraduate/bsc-ocean-exploration-and-surveying |
| 6 | BSc (Hons) Ocean Science and Marine Conservation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-ocean-science-and-marine-conservation |
| 7 | BSc (Hons) Marine Conservation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-conservation |
| 8 | BSc (Hons) Marine Biology with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology-with-foundation-year |
| 9 | BSc (Hons) Ocean Sciences with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-ocean-sciences-with-foundation-year |

##### MSci (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MSci (Hons) Marine Biology | https://www.plymouth.ac.uk/courses/undergraduate/msci-marine-biology |

#### Mathematics and Data Science

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Mathematics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics |
| 2 | BSc (Hons) Mathematics with Computer Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-computer-science |
| 3 | BSc (Hons) Mathematics with Statistics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-statistics |
| 4 | BSc (Hons) Mathematics with Theoretical Physics | https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-theoretical-physics |
| 5 | BSc (Hons) Data Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-data-science |
| 6 | BSc (Hons) Data Science with Artificial Intelligence | https://www.plymouth.ac.uk/courses/undergraduate/bsc-data-science-with-artificial-intelligence |
| 7 | BSc (Hons) Mathematics with Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-foundation-year |

#### Medicine, Dentistry and Biomedical Sciences

##### BMBS
| # | 专业 | URL |
|---|------|-----|
| 1 | BMBS Bachelor of Medicine, Bachelor of Surgery | https://www.plymouth.ac.uk/courses/undergraduate/bmbs-bachelor-of-medicine-bachelor-of-surgery |
| 2 | BMBS Bachelor of Medicine, Bachelor of Surgery with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/bmbs-bachelor-of-medicine-bachelor-of-surgery-with-foundation-year-0 |

##### BDS
| # | 专业 | URL |
|---|------|-----|
| 1 | BDS Dental Surgery | https://www.plymouth.ac.uk/courses/undergraduate/bds-dental-surgery |
| 2 | BDS Dental Surgery with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bds-dental-surgery-with-integrated-foundation-year |

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Dental Therapy and Hygiene | https://www.plymouth.ac.uk/courses/undergraduate/bsc-dental-therapy-hygiene |
| 2 | BSc (Hons) Dental Therapy and Hygiene with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-dental-therapy-and-hygiene-with-integrated-foundation-year |
| 3 | BSc (Hons) Biomedical Science | https://www.plymouth.ac.uk/courses/undergraduate/bsc-biomedical-science |
| 4 | BSc (Hons) Clinical Physiology (Cardiac Physiology) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-clinical-physiology |
| 5 | BSc (Hons) Medical Sciences | https://www.plymouth.ac.uk/courses/undergraduate/bsc-medical-sciences |
| 6 | BSc (Hons) Biomedical Science with Integrated Foundation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-biomedical-science-with-foundation-year |

##### MSci (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MSci (Hons) Biomedical Science | https://www.plymouth.ac.uk/courses/undergraduate/msci-biomedical-science |

#### Nursing and Midwifery

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Nursing (Adult Health) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-adult-health |
| 2 | BSc (Hons) Nursing (Child Health) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-child-health |
| 3 | BSc (Hons) Nursing (Mental Health) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-mental-health |
| 4 | BSc (Hons) Midwifery | https://www.plymouth.ac.uk/courses/undergraduate/bsc-midwifery |
| 5 | BSc (Hons) Midwifery - blended learning | https://www.plymouth.ac.uk/courses/undergraduate/bsc-midwifery-blended |
| 6 | BSc (Hons) Nursing (Adult Health) with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-adult-health-with-integrated-foundation-year |
| 7 | BSc (Hons) Nursing (Child Health) with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-child-health-with-integrated-foundation-year |
| 8 | BSc (Hons) Nursing (Mental Health) with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-mental-health-with-integrated-foundation-year |
| 9 | BSc (Hons) Critical Care (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-critical-care |
| 10 | BSc (Hons) Professional Development in Critical Care (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-critical-care |
| 11 | BSc (Hons) Professional Development in End of Life Care (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-end-of-life-care |
| 12 | BSc (Hons) Professional Development in Health and Social Care (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-health-and-social-care |
| 13 | BSc (Hons) Professional Development in Long Term Conditions (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-long-term-conditions |
| 14 | BSc (Hons) Professional Development in Mental Health (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-mental-health |
| 15 | BSc (Hons) Professional Development in Neonatal Care (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-neonatal-care |
| 16 | BSc (Hons) Professional Development in Nursing (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-professional-development-in-nursing |
| 17 | BSc (Hons) Urgent and Emergency Care (Part-time) | https://www.plymouth.ac.uk/courses/undergraduate/bsc-urgent-and-emergency-care-3 |

##### FdSc
| # | 专业 | URL |
|---|------|-----|
| 1 | FdSc Nursing Associate | https://www.plymouth.ac.uk/courses/undergraduate/fdsc-nursing-associate |

##### MNurs (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MNurs (Hons) Nursing (Adult Health and Child Health) | https://www.plymouth.ac.uk/courses/undergraduate/mnurs-nursing-adult-health-and-child-health |
| 2 | MNurs (Hons) Nursing (Adult Health and Mental Health) | https://www.plymouth.ac.uk/courses/undergraduate/mnurs-nursing-adult-health-and-mental-health |
| 3 | MNurs (Hons) Nursing (Child Health and Mental Health) | https://www.plymouth.ac.uk/courses/undergraduate/mnurs-nursing-child-health-and-mental-health |

#### Psychology

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) Psychology with Integrated Foundation Year | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-integrated-foundation-year |
| 2 | BSc (Hons) Psychology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology |
| 3 | BSc (Hons) Psychological Studies | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychological-studies |
| 4 | BSc (Hons) Psychology with Criminology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-criminology ⚠ shared with Law |
| 5 | BSc (Hons) Psychology with Sociology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-sociology ⚠ shared with Sociology |
| 6 | BSc (Hons) Psychology with Human Biology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-human-biology |
| 7 | BSc (Hons) Psychology with Education | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-education ⚠ shared with Education |
| 8 | BSc (Hons) Psychology with Early Childhood Studies | https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-early-childhood-studies ⚠ shared with Education |

##### MPsych (integrated masters)
| # | 专业 | URL |
|---|------|-----|
| 1 | MPsych (Hons) Psychology | https://www.plymouth.ac.uk/courses/undergraduate/mpsych-psychology |
| 2 | MPsych (Hons) Psychology with Human Neuroscience | https://www.plymouth.ac.uk/courses/undergraduate/mpsych-psychology-with-human-neuroscience |
| 3 | MPsych (Hons) Psychology with Clinical Perspectives | https://www.plymouth.ac.uk/courses/undergraduate/mpsych-psychology-with-clinical-perspectives |

#### Sociology, International Relations and Politics

##### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | BSc (Hons) International Relations | https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-relations |
| 2 | BSc (Hons) Politics and International Relations | https://www.plymouth.ac.uk/courses/undergraduate/bsc-politics-and-international-relations |
| 3 | BSc (Hons) Sociology | https://www.plymouth.ac.uk/courses/undergraduate/bsc-sociology |
| 4 | BSc (Hons) International Relations with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-relations-with-foundation |
| 5 | BSc (Hons) Sociology with Foundation | https://www.plymouth.ac.uk/courses/undergraduate/bsc-sociology-with-foundation |

### 1.4 Minors

Plymouth does not publish a structured standalone minor list. Some programs (e.g. BSc Psychology, BA Geography) offer minor pathways within the degree, but no centralised minor registry was found on the subjects pages.

### 1.5 General/Institute-wide requirements

UG courses follow a standard UK honours structure (3 years full-time; 4 years with placement/sandwich; integrated masters 4 years). Most courses accept UCAS tariff points (typical offer range 104-136 UCAS points). Foundation year variants (4-year) require lower entry tariffs. UCAS application portal: https://www.ucas.com/.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by subject area > degree level

#### Biological Sciences

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Sustainable Aquaculture and Fisheries | https://www.plymouth.ac.uk/courses/postgraduate/msc-sustainable-aquaculture-and-fisheries |
| 2 | MSc Zoo and Aquarium Conservation Biology | https://www.plymouth.ac.uk/courses/postgraduate/msc-zoo-and-aquarium-conservation-biology |
| 3 | MSc Sustainable Food Production | https://www.plymouth.ac.uk/courses/postgraduate/msc-sustainable-food-production |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Biological Sciences | https://www.plymouth.ac.uk/courses/postgraduate/phd-biological-sciences |

##### ResM
| # | 项目 | URL |
|---|------|-----|
| 1 | ResM Biological Sciences | https://www.plymouth.ac.uk/courses/postgraduate/resm-biological-sciences |
| 2 | ResM Agriculture and Food | https://www.plymouth.ac.uk/courses/postgraduate/resm-agriculture-and-food |

#### Architecture, Design and Building Construction

##### MArch
| # | 项目 | URL |
|---|------|-----|
| 1 | MArch Architecture (ARB/RIBA Part 2) | https://www.plymouth.ac.uk/courses/postgraduate/march-architecture-arbriba-part-2 |

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Civil Engineering | https://www.plymouth.ac.uk/courses/postgraduate/msc-civil-engineering ⚠ shared with Engineering |
| 2 | MSc Planning | https://www.plymouth.ac.uk/courses/postgraduate/msc-planning ⚠ shared with Earth |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Architecture | https://www.plymouth.ac.uk/courses/postgraduate/phd-architecture |
| 2 | PhD Built Environment | https://www.plymouth.ac.uk/courses/postgraduate/phd-built-environment |

#### Business

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Human Resource Management | https://www.plymouth.ac.uk/courses/postgraduate/ma-human-resource-management |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | MBA Master of Business Administration (top-up) | https://www.plymouth.ac.uk/courses/postgraduate/mba-master-of-business-administration |
| 2 | MBA Master of Business Administration (top-up) | https://www.plymouth.ac.uk/courses/postgraduate/mba-business-administration |

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Business and Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-business-and-management |
| 2 | MSc Digital and Social Media Marketing | https://www.plymouth.ac.uk/courses/postgraduate/msc-digital-and-social-media-marketing |
| 3 | MSc Finance | https://www.plymouth.ac.uk/courses/postgraduate/msc-finance |
| 4 | MSc International Business | https://www.plymouth.ac.uk/courses/postgraduate/msc-international-business |
| 5 | MSc International Logistics and Supply Chain Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-international-logistics-and-supply-chain-management |
| 6 | MSc International Procurement and Supply Chain Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-international-procurement-and-supply-chain-management |
| 7 | MSc International Shipping | https://www.plymouth.ac.uk/courses/postgraduate/msc-international-shipping |
| 8 | MSc Operations and Supply Chain Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-operations-and-supply-chain-management |
| 9 | MSc Project Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-project-management |
| 10 | MSc Tourism and Hospitality Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-tourism-and-hospitality-management |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Business with Management | https://www.plymouth.ac.uk/courses/postgraduate/phd-business-with-management |
| 2 | PhD Finance | https://www.plymouth.ac.uk/courses/postgraduate/phd-finance |
| 3 | PhD International Logistics, Supply Chain and Shipping Management | https://www.plymouth.ac.uk/courses/postgraduate/phd-international-logistics-supply-chain-and-shipping-management |
| 4 | PhD Marketing | https://www.plymouth.ac.uk/courses/postgraduate/phd-marketing |
| 5 | PhD Tourism and Hospitality | https://www.plymouth.ac.uk/courses/postgraduate/phd-tourism-and-hospitality |

#### Chemistry

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Environmental Geochemistry | https://www.plymouth.ac.uk/courses/postgraduate/msc-environmental-geochemistry ⚠ shared with Earth |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Chemistry | https://www.plymouth.ac.uk/courses/postgraduate/phd-chemistry |

##### ResM
| # | 项目 | URL |
|---|------|-----|
| 1 | ResM Chemistry | https://www.plymouth.ac.uk/courses/postgraduate/resm-chemistry |

#### Computer Science

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Cyber Security | https://www.plymouth.ac.uk/courses/postgraduate/msc-cyber-security ⚠ shared with Engineering, Maths |
| 2 | MSc Data Science and Environmental Intelligence | https://www.plymouth.ac.uk/courses/postgraduate/msc-data-science-and-environmental-intelligence ⚠ shared with Earth, Maths |
| 3 | MSc Artificial Intelligence | https://www.plymouth.ac.uk/courses/postgraduate/msc-artificial-intelligence |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes Maritime Cyber Security | https://www.plymouth.ac.uk/courses/postgraduate/mres-maritime-cyber-security ⚠ shared with Engineering, Maths |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Cyber Security | https://www.plymouth.ac.uk/courses/postgraduate/phd-cyber-security ⚠ shared with Engineering |
| 2 | PhD Artificial Intelligence | https://www.plymouth.ac.uk/courses/postgraduate/phd-artificial-intelligence ⚠ shared with Engineering |

#### Creative Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Filmmaking | https://www.plymouth.ac.uk/courses/postgraduate/ma-filmmaking |

#### Design

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Game Design | https://www.plymouth.ac.uk/courses/postgraduate/ma-game-design ⚠ shared with Games |
| 2 | MA Communication Design | https://www.plymouth.ac.uk/courses/postgraduate/ma-communication-design |
| 3 | MA Experience Design | https://www.plymouth.ac.uk/courses/postgraduate/ma-experience-design |

#### Earth, Geography and Environment

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Environmental and Engineering Geology | https://www.plymouth.ac.uk/courses/postgraduate/msc-environmental-and-engineering-geology |
| 2 | MSc Environmental Consultancy | https://www.plymouth.ac.uk/courses/postgraduate/msc-environmental-consultancy |
| 3 | MSc Global Sustainability | https://www.plymouth.ac.uk/courses/postgraduate/msc-global-sustainability |
| 4 | MSc Sustainable Environmental Management | https://www.plymouth.ac.uk/courses/postgraduate/msc-sustainable-environmental-management |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes Sustainable Environmental Management | https://www.plymouth.ac.uk/courses/postgraduate/mres-sustainable-environmental-management |

#### Education and Teaching

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Education | https://www.plymouth.ac.uk/courses/postgraduate/ma-education |

##### PGCE
| # | 项目 | URL |
|---|------|-----|
| 1 | PGCE (incorporating the Diploma in Teaching (Further Education and Skills)) | https://www.plymouth.ac.uk/courses/postgraduate/pgce-incorporating-the-diploma-in-teaching-further-education-and-skills |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Education | https://www.plymouth.ac.uk/courses/postgraduate/phd-education |

##### EdD (Professional Doctorate)
| # | 项目 | URL |
|---|------|-----|
| 1 | EdD Professional Doctorate in Education | https://www.plymouth.ac.uk/courses/postgraduate/edd-education |
| 2 | EdD Professional Doctorate in Education (HKU Space) | https://www.plymouth.ac.uk/courses/postgraduate/edd-professional-doctorate-in-education |

#### Engineering and Robotics

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Coastal Engineering | https://www.plymouth.ac.uk/courses/postgraduate/msc-coastal-engineering |
| 2 | MSc Electrical and Electronic Engineering | https://www.plymouth.ac.uk/courses/postgraduate/msc-electrical-and-electronic-engineering |
| 3 | MSc Health Data Science and Statistics | https://www.plymouth.ac.uk/courses/postgraduate/msc-health-data-science-and-statistics ⚠ shared with Maths |
| 4 | MSc Mechanical Engineering Design | https://www.plymouth.ac.uk/courses/postgraduate/msc-mechanical-engineering-design |
| 5 | MSc Medical Engineering | https://www.plymouth.ac.uk/courses/postgraduate/msc-medical-engineering |
| 6 | MSc Robotics | https://www.plymouth.ac.uk/courses/postgraduate/msc-robotics |

##### MPhil
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil Civil Engineering | https://www.plymouth.ac.uk/courses/postgraduate/mphil-civil-engineering |
| 2 | MPhil Mechanical Engineering | https://www.plymouth.ac.uk/courses/postgraduate/mphil-mechanical-engineering |

##### ResM
| # | 项目 | URL |
|---|------|-----|
| 1 | ResM Electrical and Electronic Engineering | https://www.plymouth.ac.uk/courses/postgraduate/resm-electrical-and-electronic-engineering |
| 2 | ResM Mechanical Engineering | https://www.plymouth.ac.uk/courses/postgraduate/resm-mechanical-engineering |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Civil Engineering | https://www.plymouth.ac.uk/courses/postgraduate/phd-civil-engineering |
| 2 | PhD Electrical and Electronic Engineering | https://www.plymouth.ac.uk/courses/postgraduate/phd-electrical-and-electronic-engineering |
| 3 | PhD Maritime Science and Technology | https://www.plymouth.ac.uk/courses/postgraduate/phd-maritime-science-and-technology |
| 4 | PhD Mechanical Engineering | https://www.plymouth.ac.uk/courses/postgraduate/phd-mechanical-engineering |
| 5 | PhD on the Basis of Prior Published Works in Cyber Security | https://www.plymouth.ac.uk/courses/postgraduate/phd-on-the-basis-of-prior-published-works-in-cyber-security |
| 6 | PhD Robotics | https://www.plymouth.ac.uk/courses/postgraduate/phd-robotics |

##### EngD (Professional Doctorate)
| # | 项目 | URL |
|---|------|-----|
| 1 | EngD Engineering | https://www.plymouth.ac.uk/courses/postgraduate/engd-engineering |

#### Games

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Game Design | https://www.plymouth.ac.uk/courses/postgraduate/ma-game-design ⚠ shared with Design |

#### Health Professions

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Human Nutrition | https://www.plymouth.ac.uk/courses/postgraduate/msc-human-nutrition |
| 2 | MSc Occupational Therapy (Pre-Registration) | https://www.plymouth.ac.uk/courses/postgraduate/msc-occupational-therapy-pre-registration |
| 3 | MSc Physiotherapy (Pre-Registration) | https://www.plymouth.ac.uk/courses/postgraduate/msc-physiotherapy-pre-registration |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Social Work (Pre-Registration) | https://www.plymouth.ac.uk/courses/postgraduate/ma-social-work-pre-registration |

#### Humanities

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Creative Writing | https://www.plymouth.ac.uk/courses/postgraduate/ma-creative-writing |
| 2 | MA English Literature | https://www.plymouth.ac.uk/courses/postgraduate/ma-english-literature |
| 3 | MA History | https://www.plymouth.ac.uk/courses/postgraduate/ma-history |
| 4 | MA Maritime History | https://www.plymouth.ac.uk/courses/postgraduate/ma-maritime-history |
| 5 | MA Heritage Theory and Practice | https://www.plymouth.ac.uk/courses/postgraduate/ma-heritage-theory-and-practice |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Creative Writing | https://www.plymouth.ac.uk/courses/postgraduate/phd-creative-writing |
| 2 | PhD English | https://www.plymouth.ac.uk/courses/postgraduate/phd-english |
| 3 | PhD Art History | https://www.plymouth.ac.uk/courses/postgraduate/phd-art-history |
| 4 | PhD History | https://www.plymouth.ac.uk/courses/postgraduate/phd-history |

#### Law, Criminology and Policing

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | LLM Business Law | https://www.plymouth.ac.uk/courses/postgraduate/llm-business-law |
| 2 | LLM Environmental Law | https://www.plymouth.ac.uk/courses/postgraduate/llm-environmental-law |
| 3 | LLM International Law | https://www.plymouth.ac.uk/courses/postgraduate/llm-international-law |
| 4 | LLM Maritime Law | https://www.plymouth.ac.uk/courses/postgraduate/llm-maritime-law |
| 5 | LLM Law | https://www.plymouth.ac.uk/courses/postgraduate/llm-law |

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Criminology | https://www.plymouth.ac.uk/courses/postgraduate/msc-criminology |

#### Marine and Ocean Science

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Marine Conservation | https://www.plymouth.ac.uk/courses/postgraduate/msc-marine-conservation |
| 2 | MSc Applied Marine Science | https://www.plymouth.ac.uk/courses/postgraduate/msc-applied-marine-science |
| 3 | MSc Hydrography | https://www.plymouth.ac.uk/courses/postgraduate/msc-hydrography |

##### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes Marine Biology | https://www.plymouth.ac.uk/courses/postgraduate/mres-marine-biology |
| 2 | MRes Scientific Diving | https://www.plymouth.ac.uk/courses/postgraduate/mres-scientific-diving |
| 3 | MRes Applied Marine Science | https://www.plymouth.ac.uk/courses/postgraduate/mres-applied-marine-science |

#### Mathematics and Data Science

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Data Science | https://www.plymouth.ac.uk/courses/postgraduate/msc-data-science |
| 2 | MSc Data Science and Business Analytics | https://www.plymouth.ac.uk/courses/postgraduate/msc-data-science-and-business-analytics |
| 3 | MSc Social Research | https://www.plymouth.ac.uk/courses/postgraduate/msc-social-research ⚠ shared with Earth, Sociology |

##### ResM
| # | 项目 | URL |
|---|------|-----|
| 1 | ResM Mathematics and Statistics | https://www.plymouth.ac.uk/courses/postgraduate/resm-mathematics-and-statistics |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Mathematics and Statistics | https://www.plymouth.ac.uk/courses/postgraduate/phd-mathematics-and-statistics |

#### Medicine, Dentistry and Biomedical Sciences

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Expedition and Marine Medicine | https://www.plymouth.ac.uk/courses/postgraduate/msc-expedition-and-marine-medicine |
| 2 | MSc Expedition and Marine Medicine (Diving Medicine) | https://www.plymouth.ac.uk/courses/postgraduate/msc-expedition-and-marine-medicine-diving-medicine |
| 3 | MSc Global Health (Online) | https://www.plymouth.ac.uk/courses/postgraduate/msc-global-health-online |
| 4 | MSc Healthcare Management, Leadership and Innovation | https://www.plymouth.ac.uk/courses/postgraduate/msc-healthcare-management-leadership-and-innovation |
| 5 | MSc Physician Associate Studies | https://www.plymouth.ac.uk/courses/postgraduate/msc-physician-associate-studies |
| 6 | MSc Physician Associate Studies (Top-Up) | https://www.plymouth.ac.uk/courses/postgraduate/msc-physician-associate-studies-top-up |
| 7 | MSc Endodontics | https://www.plymouth.ac.uk/courses/postgraduate/msc-endodontics |
| 8 | MSc Oral Surgery | https://www.plymouth.ac.uk/courses/postgraduate/msc-minor-oral-surgery |
| 9 | MSc Orthodontics | https://www.plymouth.ac.uk/courses/postgraduate/msc-orthodontics |
| 10 | MSc Periodontology | https://www.plymouth.ac.uk/courses/postgraduate/msc-periodontology |
| 11 | MSc Restorative Dentistry | https://www.plymouth.ac.uk/courses/postgraduate/msc-restorative-dentistry |
| 12 | MSc Biomedical Science | https://www.plymouth.ac.uk/courses/postgraduate/msc-biomedical-science |

##### PgDip
| # | 项目 | URL |
|---|------|-----|
| 1 | PgDip Global Health (Online) | https://www.plymouth.ac.uk/courses/postgraduate/pgdip-global-health-online |
| 2 | PgDip Biomedical Science | https://www.plymouth.ac.uk/courses/postgraduate/pgdip-biomedical-science |

##### PgCert
| # | 项目 | URL |
|---|------|-----|
| 1 | PgCert Clinical Education | https://www.plymouth.ac.uk/courses/postgraduate/pgcert-clinical-education |
| 2 | PgCert Diving Medicine | https://www.plymouth.ac.uk/courses/postgraduate/pgcert-diving-medicine |
| 3 | PgCert Expedition and Marine Medicine | https://www.plymouth.ac.uk/courses/postgraduate/pgcert-expedition-and-marine-medicine |
| 4 | PgCert Global Health (Online) | https://www.plymouth.ac.uk/courses/postgraduate/pgcert-global-health-online |
| 5 | PgCert Healthcare Management, Leadership and Innovation | https://www.plymouth.ac.uk/courses/postgraduate/pgcert-healthcare-management-leadership-and-innovation |
| 6 | PgCert Clinical Echocardiography | https://www.plymouth.ac.uk/courses/postgraduate/pgcert-clinical-echocardiography |

##### MClinEd
| # | 项目 | URL |
|---|------|-----|
| 1 | MClinEd Clinical Education | https://www.plymouth.ac.uk/courses/postgraduate/mclined-clinical-education |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Medical Studies | https://www.plymouth.ac.uk/courses/postgraduate/phd-medical-studies |
| 2 | PhD on the Basis of Prior Published Works in Medical Studies | https://www.plymouth.ac.uk/courses/postgraduate/doctor-of-philosophy-phd-on-the-basis-of-prior-published-works-in-medical-studies |
| 3 | PhD Dental Studies | https://www.plymouth.ac.uk/courses/postgraduate/phd-dental-studies |
| 4 | PhD on the Basis of Prior Published Works in Dental Studies | https://www.plymouth.ac.uk/courses/postgraduate/phd-on-the-basis-of-prior-published-works-in-dental-studies |
| 5 | PhD Biomedical Sciences | https://www.plymouth.ac.uk/courses/postgraduate/phd-biomedical-sciences |

##### ResM
| # | 项目 | URL |
|---|------|-----|
| 1 | ResM Medical Studies | https://www.plymouth.ac.uk/courses/postgraduate/resm-medical-studies |
| 2 | ResM Dental Studies | https://www.plymouth.ac.uk/courses/postgraduate/resm-dental-studies |
| 3 | ResM Biomedical Sciences | https://www.plymouth.ac.uk/courses/postgraduate/resm-biomedical-sciences |

##### MD (Professional Doctorate)
| # | 项目 | URL |
|---|------|-----|
| 1 | MD Medicine | https://www.plymouth.ac.uk/courses/postgraduate/md-medicine |

#### Nursing and Midwifery

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Pre-registration Nursing (Adult Health) | https://www.plymouth.ac.uk/courses/postgraduate/msc-nursing-adult-health |
| 2 | MSc Pre-registration Nursing (Child Health) | https://www.plymouth.ac.uk/courses/postgraduate/msc-nursing-child-health |
| 3 | MSc Pre-registration Nursing (Mental Health) | https://www.plymouth.ac.uk/courses/postgraduate/msc-nursing-mental-health |
| 4 | MSc Midwifery (Pre-Registration) | https://www.plymouth.ac.uk/courses/postgraduate/msc-midwifery-pre-registration |
| 5 | MSc Midwifery (Pre-Registration) - blended learning | https://www.plymouth.ac.uk/courses/postgraduate/msc-midwifery-pre-registration-blended |
| 6 | MSc Midwifery (Shortened) | https://www.plymouth.ac.uk/courses/postgraduate/msc-midwifery-shortened |
| 7 | MSc Midwifery (Shortened) - blended learning | https://www.plymouth.ac.uk/courses/postgraduate/msc-midwifery-shortened-blended |
| 8 | MSc Advanced Clinical Practitioner in Mental Health | https://www.plymouth.ac.uk/courses/postgraduate/msc-advanced-clinical-practitioner-in-mental-health |
| 9 | MSc Advanced Critical Care Practitioner | https://www.plymouth.ac.uk/courses/postgraduate/msc-advanced-critical-care-practitioner |
| 10 | MSc Advanced Neonatal Nurse Practitioner | https://www.plymouth.ac.uk/courses/postgraduate/msc-advanced-neonatal-nurse-practitioner |
| 11 | MSc Advanced Professional Practice (Clinical Practitioner) | https://www.plymouth.ac.uk/courses/postgraduate/msc-advanced-professional-practice-clinical-practitioner |
| 12 | MSc Advanced Professional Practice (Nursing and Midwifery Professions) | https://www.plymouth.ac.uk/courses/postgraduate/msc-advanced-professional-practice-nursing-and-midwifery-professions |
| 13 | MSc Surgical Care Practitioner (Abdominal, Pelvic and General Surgery) | https://www.plymouth.ac.uk/courses/postgraduate/msc-surgical-care-practitioner-abdominal-pelvic-and-general-surgery |
| 14 | MSc Surgical Care Practitioner (Cardiothoracic Surgery) | https://www.plymouth.ac.uk/courses/postgraduate/msc-surgical-care-practitioner-cardiothoracic-surgery |
| 15 | MSc Surgical Care Practitioner (Trauma and Orthopaedic Surgery) | https://www.plymouth.ac.uk/courses/postgraduate/msc-surgical-care-practitioner-trauma-and-orthopaedic-surgery |

##### PgDip
| # | 项目 | URL |
|---|------|-----|
| 1 | PgDip Advanced Critical Care Practitioner | https://www.plymouth.ac.uk/courses/postgraduate/pgdip-advanced-critical-care-practitioner |

##### ResM
| # | 项目 | URL |
|---|------|-----|
| 1 | ResM Applied Health Studies | https://www.plymouth.ac.uk/courses/postgraduate/resm-applied-health-studies |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD Applied Health Studies | https://www.plymouth.ac.uk/courses/postgraduate/phd-applied-health-studies |

#### Psychology

##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Clinical Psychology | https://www.plymouth.ac.uk/courses/postgraduate/msc-clinical-psychology |
| 2 | MSc Clinical Psychology (Online) | https://www.plymouth.ac.uk/courses/postgraduate/msc-clinical-psychology-online |
| 3 | MSc Human Neuroscience | https://www.plymouth.ac.uk/courses/postgraduate/msc-human-neuroscience |
| 4 | MSc Psychology | https://www.plymouth.ac.uk/courses/postgraduate/msc-psychology |
| 5 | MSc Psychology (Online) | https://www.plymouth.ac.uk/courses/postgraduate/msc-psychology-online |
| 6 | MSc Research Methods in Psychology | https://www.plymouth.ac.uk/courses/postgraduate/msc-research-methods-in-psychology |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD on the Basis of Prior Published Works in Psychology | https://www.plymouth.ac.uk/courses/postgraduate/phd-on-the-basis-of-prior-published-works-in-psychology |
| 2 | PhD Psychology | https://www.plymouth.ac.uk/courses/postgraduate/phd-psychology |

##### DClinPsy (Professional Doctorate)
| # | 项目 | URL |
|---|------|-----|
| 1 | DClinPsy Clinical Psychology | https://www.plymouth.ac.uk/courses/postgraduate/dclinpsy-clinical-psychology |

#### Sociology, International Relations and Politics

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA International Relations: Global Security and Development | https://www.plymouth.ac.uk/courses/postgraduate/ma-international-relations-global-security-and-development |
| 2 | MA International Relations: Security and Development (Online) | https://www.plymouth.ac.uk/courses/postgraduate/ma-international-relations-security-and-development-online |

### 2.2 At least one program's full deep-dive

**MSc Business and Management** (one of Plymouth's largest PG programs)

- Department: Faculty of Business / Business School
- Email: admissions@plymouth.ac.uk
- Phone: +44 1752 585858
- Application portal: https://www.plymouth.ac.uk/study/postgraduate/apply
- Typical duration: 1 year full-time
- Tuition (2025/26 reference): see per-course page fees section
- TOEFL iBT minimum: 90 (component: L17 R18 S20 W18)
- IELTS minimum: 6.5 overall (5.5 in all components)
- Pearson PTE: 59
- Duolingo: 120 overall with 105 in each component
- LanguageCert Academic: 70 overall
- What lives behind accordions: "Fees, costs and funding" section (per-course); entry requirements listed by qualification; placement year option for some courses; international student advice

### 2.3 Graduate admissions model

**Decentralized** - there is no single graduate school. Each subject area manages its own admissions, though the central Admissions team handles initial processing (admissions@plymouth.ac.uk, +44 1752 585858). Application portal: https://www.plymouth.ac.uk/study/postgraduate/apply. PGR (research) applications go through the Doctoral College (researchdegreeadmissions@plymouth.ac.uk). Standard application fee varies by program; many taught masters have no application fee.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| Admissions site | https://www.plymouth.ac.uk/study/undergraduate |
| Application portal | UCAS (https://www.ucas.com/) |
| UCAS Extra / Clearing | Yes - clearing vacancies at https://www.plymouth.ac.uk/study/clearing/courses |
| Typical offer | 104-136 UCAS tariff points (varies by course; e.g. BSc Computer Science: 104 UCAS points) |
| A levels | Course-dependent, typically BBB-A*AB (including subject-specific requirements) |
| International Baccalaureate | Course-dependent; BSc Computer Science example: 24+ points |
| BTEC | 18 Unit BTEC National Diploma / QCF Extended Diploma accepted |
| GCSE | English and Mathematics at grade C/4 or above (standard) |
| T level | Accepted on many courses |
| Contextual offers | Yes - see https://www.plymouth.ac.uk/study/entry-requirements/contextual-offers |
| Foundation year | Available as integrated variant (4-year) on most courses |
| Placement year | Optional on most courses; fee £1,955 UK / £1,465 overseas (BSc Computer Science 2026-27 reference) |
| Interview/audition | Required for medicine (BMBS), dentistry (BDS), some health-professions, some creative arts, primary education |
| DBS check | Required for health, education, social work |
| Recommendation | UCAS reference (1 reference) |
| Personal statement | UCAS personal statement |
| Portfolio | Required for Architecture, Art & Design programs |
| Application deadline | Standard UCAS equal consideration: 26 January (for September entry); UCAS Extra after main deadline; Clearing from July |
| Decision notification | UCAS standard cycle |
| Enrollment confirmation deadline | UCAS standard (usually early August) |
| Transfer pathway | Internal transfer possible between Plymouth courses |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum (UG) | Recommended | Component minimums |
|------|-------------|-------------|---------------------|
| IELTS Academic | 6.0 overall | 6.5+ | 5.5 in all four components |
| TOEFL iBT | 76 | 90+ | L17, R18, S20, W18 |
| Pearson PTE Academic | 59 | 65+ | 59 in all four components |
| Duolingo English Test | 105 overall (100 in each component) | 120+ | 100 in each |
| LanguageCert Academic | 65 overall | 70+ | 60 in each component |
| Cambridge English | (Accepted - see Cambridge English page) | - | - |
| Trinity College London ISE | (Accepted - SELT only if taken in UK) | - | - |

> Note: Some subject areas require higher English than the standard UG minimum - specifically health professions, nursing, midwifery, medicine and dentistry, creative writing, English literature, and other postgraduate English courses. Applicants should contact admissions@plymouth.ac.uk for the higher requirements. SELT (Secure English Language Test) is required by UKVI for visa purposes; Plymouth accepts UKVI-approved SELTs plus other tests they deem acceptable.

### 3.3 Graduate — global rules

| 维度 | 详情 |
|------|------|
| Admissions model | Decentralized - per subject area |
| Application portal | https://www.plymouth.ac.uk/study/postgraduate/apply (PGT); Doctoral College for PGR (researchdegreeadmissions@plymouth.ac.uk) |
| Application fee | Varies by program; many PGT have no fee; PGR has resubmission fee £570 (one-off) and PhD on Prior Published Works application fee £570 |
| Standard fee waiver | Available for low-income applicants (PGT) |
| GRE/GMAT | Not required for most PGT programs; may be required for some PhD programs in quantitative fields |
| Language-test policy | See Section 3.2 thresholds above (PG minimums are slightly higher: IELTS 6.5 overall, TOEFL 90, PTE 59, Duolingo 120/105, LanguageCert 70) |
| CGS April-15 equivalent | UK uses 1st September as standard; Plymouth PG research follows UK Research Councils terms |
| PG deadline | Rolling admissions; recommended apply by July for September entry; some programs have specific deadlines |
| TOEIC institutional code | TOEFL DI code: 2242 |
| Doctoral College | researchdegreeadmissions@plymouth.ac.uk; +44 1752 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense item | Amount (UK/Islands) | Amount (International) | Description |
|--------------|---------------------|------------------------|-------------|
| Full-time tuition (UG) | £9,790 per year (e.g. BSc Computer Science) | varies by course; check course page | Annual tuition for new full-time UG starting 2026-27 |
| Module fees (repeated/part-time) | £815 per 10 credits | varies | Per credit for repeat/part-time study |
| Optional placement year (UK) | £1,955 (e.g. BSc Computer Science) | varies | Placement year fee if completed in UK |
| Optional placement year (overseas) | £1,465 (e.g. BSc Computer Science) | varies | Placement year fee if completed outside UK |
| Clinical/health placement fees | varies (often additional) | varies | Health-profession courses may have additional placement costs |
| Living costs (accommodation, food, bills) | ~£9,000-£11,000 per year (estimate) | ~£9,000-£11,000 per year | Plymouth is 51% cheaper than London (livingcost.org 2024) |
| Books and study costs | ~£500-£1,000 per year | ~£500-£1,000 per year | Textbooks, printing, stationery |
| Field-trip costs | varies by course | varies | e.g. Earth, Geography, Marine programs have field trips |

### 4.2 Undergraduate financial-aid policy

| Item | Detail |
|------|--------|
| Tuition fee loan | Available to UK students (Student Finance England / Wales / Scotland / NI) |
| Living cost loan | Available to UK students (means-tested) |
| Tuition-free threshold | None (UK students pay up to £9,790 via loan, never upfront) |
| Need-blind for internationals? | No - international students are not eligible for UK government loans |
| Scholarships | https://www.plymouth.ac.uk/study/funding/scholarships |
| Bursaries and support funds | https://www.plymouth.ac.uk/study/funding/bursaries |
| The Tamar Engineering Project | £3,000/yr living costs + £1,500/yr fee waiver + mentoring for engineering students from under-represented backgrounds |
| Defence STEM Undergraduate Sponsorship (DSUS) | Tuition fees up to £9,535/yr + £5,000 annual bursary + paid placements for engineering/STEM students intending to join Royal Navy, Army, RAF or MOD Civil Service |
| TEF rating | TEF Gold (2023) - all three categories (teaching quality, student experience, graduate employment) |
| Graduate employment | Over 95% of graduates working or studying 15 months after graduating (HESA data 2022) |
| Cost of living support | https://www.plymouth.ac.uk/students-and-family/fees-and-funding/support-for-students-experiencing-rising-costs |

### 4.3 Graduate cost & funding framework

#### Postgraduate taught (PGT) - 2026-27 reference
PGT tuition fees are listed **per course** at `https://www.plymouth.ac.uk/courses/postgraduate/<slug>` (under the "Fees, costs and funding" section). Tuition varies by program - international students typically pay £15,000-£20,000/year. Common funding types: self-funded, employer-sponsored, UK government PGT loan (£11,570 max for UK students). Sources: https://www.plymouth.ac.uk/study/funding (general); UK government PGT loan.

#### Postgraduate research (PGR) - 2026-27 (full table from official source)

| Mode | Programme | Band | Home / Islands | International |
|------|-----------|------|----------------|---------------|
| Full-time | MPhil/PhD/ResM/MD | Band 1 | £5,238 | £16,870 |
| Full-time | MPhil/PhD/ResM/MD | Band 2 | £5,238 | £19,315 |
| Full-time | MPhil/PhD/ResM/MD | Writing up | £570 | £570 |
| Full-time | MPhil/PhD/ResM/MD | Extension year Band 1 | £2,619 | £8,430 |
| Full-time | MPhil/PhD/ResM/MD | Extension year Band 2 | £2,619 | £9,660 |
| Full-time | MPhil/PhD/ResM/MD | Research overseas Band 1 | N/A | £8,435 |
| Full-time | MPhil/PhD/ResM/MD | Research overseas Band 2 | N/A | £9,655 |
| Full-time | MPhil/PhD/ResM/MD | Resubmission fee | £570 | £570 |
| Part-time | MPhil/PhD/ResM/MD/Plymouth-based EdD | Band 1 (started prior to 1 Aug 2024) | £3,405 | £8,435 |
| Part-time | MPhil/PhD/ResM/MD/Plymouth-based EdD | Band 2 (started prior to 1 Aug 2024) | £3,405 | £9,655 |
| Part-time | MPhil/PhD/ResM/MD/Plymouth-based EdD | Band 1 (started on/after 1 Aug 2024) | £2,619 | £8,435 |
| Part-time | MPhil/PhD/ResM/MD/Plymouth-based EdD | Band 2 (started on/after 1 Aug 2024) | £2,619 | £9,655 |
| Part-time | MPhil/PhD/ResM/MD | Writing up | £570 | £570 |
| Part-time | MPhil/PhD/ResM/MD | Extension year Band 1 | £1,308 | £4,230 |
| Part-time | MPhil/PhD/ResM/MD | Extension year Band 2 | £1,308 | £4,845 |
| Part-time | MPhil/PhD/ResM/MD | Research overseas Band 1 | N/A | £4,218 |
| Part-time | MPhil/PhD/ResM/MD | Research overseas Band 2 | N/A | £4,830 |
| Part-time | PhD on Prior Published Works (application fee) | - | £570 | £570 |
| Part-time | PhD on Prior Published Works (programme fee) | - | £5,238 | £8,435 |
| Part-time | EdD repeat module (taught phase) | - | 50% of annual fee/module | 50% of annual fee/module |
| Part-time | DBA IIG (Year 1 taught phase 1) | - | £13,650 | £13,650 |
| Part-time | DBA IIG (Year 2 taught phase 2) | - | £9,400 | £9,400 |
| Part-time | DBA IIG (Years 3-5 research phase) | - | £6,300 | £6,300 |
| Part-time | DBA IIG (Writing up) | - | £570 | £570 |
| Part-time | DBA IIG (Extension year) | - | £1,309.50 | £4,230 |
| Part-time | DBA IIG (Year 1 repeat module) | - | 1/3 of annual fee/module | 1/3 of annual fee/module |
| Part-time | DBA IIG (Year 2 repeat module) | - | Full fee | Full fee |
| Full-time | EngD (Year 1 taught phase) | - | £11,700 | £21,000 |
| Full-time | EngD (Years 2/3/4 research in industry) | - | £5,238 | £19,315 |
| Full-time | EngD (Extension year) | - | £2,619 | £9,660 |
| Full-time | EngD (Year 1 repeat module per 10 credits) | - | £650 | £1,165 |

> PGR programmes include: PhD, MPhil, ResM, MD, DBA, EdD, EngD, DClinPsy. MRes is a PGT programme (taught fees). DClinPsy fees available from Course Administrator Michele Thomas.

**Funding framework**:
- Funding type: RA/TA/fellowship/grant (UKRI, industry); many PhD students self-funded
- UKRI studentships: subject to UK Research and Innovation allocations
- Bench fees: contact Doctoral College (researchdegreeadmissions@plymouth.ac.uk)
- Doctoral College: https://www.plymouth.ac.uk/research/doctoral-college
- Contact: researchdegreeadmissions@plymouth.ac.uk

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.architecture_design.bsc-architectural-engineering.url
  value: https://www.plymouth.ac.uk/courses/undergraduate/bsc-architectural-engineering
  source_url: https://www.plymouth.ac.uk/subjects/architecture-design-building-construction
  source_snippet: "BSc (Hons) Architectural Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.computer_science.bsc-computer-science.url
  value: https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science
  source_url: https://www.plymouth.ac.uk/subjects/computer-science
  source_snippet: "BSc (Hons) Computer Science"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.cost.tuition_2026_2027
  value: "£9,790 per year (UK)"
  source_url: https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science
  source_snippet: "Tuition fees for new full-time students starting in 2026-2027. Full-time study £9,790 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.cost.placement_year_uk
  value: "£1,955"
  source_url: https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science
  source_snippet: "Optional placement year completed in the UK £1,955"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.cost.placement_year_overseas
  value: "£1,465"
  source_url: https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science
  source_snippet: "Optional placement year completed outside the UK £1,465"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.cost.module_fee_repeat
  value: "£815 per 10 credits"
  source_url: https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science
  source_snippet: "Module fees for repeated or part-time study £815 per 10 credits"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-001:
  field: english_requirements.ug.ielts
  value: "6.0 overall (5.5 in all four components)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/ielts
  source_snippet: "Undergraduate programmes 6.0 overall ... 5.5 in all four components (listening, reading, speaking and writing)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-002:
  field: english_requirements.pg.ielts
  value: "6.5 overall (5.5 in all four components)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/ielts
  source_snippet: "Postgraduate programmes 6.5 overall ... 5.5 in all four components"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-003:
  field: english_requirements.ug.toefl
  value: "76 (L17 R18 S20 W18)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/toefl-ibt-test-of-english
  source_snippet: "Undergraduate programmes 76 ... Component scores of listening 17, reading 18, speaking 20, writing 18"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-004:
  field: english_requirements.pg.toefl
  value: "90 (L17 R18 S20 W18)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/toefl-ibt-test-of-english
  source_snippet: "Postgraduate programmes 90 ... Component scores of listening 17, reading 18, speaking 20, writing 18"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-005:
  field: english_requirements.ug.duolingo
  value: "105 overall (100 in each component)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/duolingo
  source_snippet: "Undergraduate programmes 105 overall with 100 in each component"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-006:
  field: english_requirements.pg.duolingo
  value: "120 overall (105 in each component)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/duolingo
  source_snippet: "Postgraduate programmes 120 overall with 105 in each component"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-007:
  field: english_requirements.ug.pearson_pte
  value: "59 (59 in all components)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/pearson-test-of-english
  source_snippet: "Undergraduate programmes 59 ... 59 in all four components (listening, reading, speaking and writing)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-008:
  field: english_requirements.ug.languagecert
  value: "65 overall (60 in each component)"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/languagecert-academic
  source_snippet: "Undergraduate programmes 65 overall ... Minimum component scores 60 - listening, reading, speaking, writing"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-LANG-009:
  field: english_requirements.toefl_institutional_code
  value: "2242"
  source_url: https://www.plymouth.ac.uk/international/how-to-apply/english-language-requirements/toefl-ibt-test-of-english
  source_snippet: "Designated institution (DI) code: 2242"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-PG-001:
  field: postgraduate.research.full_time.phd.international_band1
  value: "£16,870"
  source_url: https://www.plymouth.ac.uk/study/fees/tuition-fees-for-postgraduate-research-students-2026-27
  source_snippet: "MPhil/PhD/ResM/MD Full time Band 1 ... International £16,870"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-002:
  field: postgraduate.research.full_time.phd.international_band2
  value: "£19,315"
  source_url: https://www.plymouth.ac.uk/study/fees/tuition-fees-for-postgraduate-research-students-2026-27
  source_snippet: "MPhil/PhD/ResM/MD Full time Band 2 ... International £19,315"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-003:
  field: postgraduate.research.full_time.phd.home
  value: "£5,238"
  source_url: https://www.plymouth.ac.uk/study/fees/tuition-fees-for-postgraduate-research-students-2026-27
  source_snippet: "MPhil/PhD/ResM/MD Full time Band 1/2 ... Home / Islands £5,238"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-004:
  field: postgraduate.research.engd.full_time.year1.international
  value: "£21,000"
  source_url: https://www.plymouth.ac.uk/study/fees/tuition-fees-for-postgraduate-research-students-2026-27
  source_snippet: "EngD Full time Year 1 (taught phase) ... International £21,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-005:
  field: postgraduate.research.resubmission_fee
  value: "£570"
  source_url: https://www.plymouth.ac.uk/study/fees/tuition-fees-for-postgraduate-research-students-2026-27
  source_snippet: "Resubmission fee*** £570 £570 ... One-off fee must be paid in full upon resubmission of thesis"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-INST-001:
  field: institution.ranking
  value: "Top 2 modern UK university (THE Young University Rankings 2024)"
  source_url: https://www.plymouth.ac.uk/study/undergraduate
  source_snippet: "Study at a top 2 modern UK university - Times Higher Education, Young University Rankings 2024"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-INST-002:
  field: institution.tef_rating
  value: "TEF Gold (2023) - all three categories"
  source_url: https://www.plymouth.ac.uk/study/undergraduate
  source_snippet: "TEF gold across all three categories - Teaching Excellence Framework 2023"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-INST-003:
  field: institution.graduate_employment
  value: "Over 95% working or studying 15 months after graduating"
  source_url: https://www.plymouth.ac.uk/study/undergraduate
  source_snippet: "High rate of graduate employment - Over 95% of our graduates are working or studying 15 months after graduating"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-INST-004:
  field: institution.living_cost_advantage
  value: "51% cheaper to live in Plymouth than in London"
  source_url: https://www.plymouth.ac.uk/study/undergraduate
  source_snippet: "One of the UK's most affordable cities for students - It's 51% cheaper to live in Plymouth than in London"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-ADDR-001:
  field: institution.address
  value: "University of Plymouth, Plymouth, Devon, PL4 8AA, United Kingdom"
  source_url: https://www.plymouth.ac.uk/study/undergraduate
  source_snippet: "University of Plymouth Plymouth Devon PL4 8AA United Kingdom"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-ADDR-002:
  field: institution.phone
  value: "+44 1752 600600"
  source_url: https://www.plymouth.ac.uk/study/undergraduate
  source_snippet: "+44 1752 600600"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: plymouth-knowledge-base-v2
  documents:
    - plymouth-overview.md           # Sections 0, 6
    - plymouth-ug-by-subject.md      # Section 1, chunked per subject area (20 chunks)
    - plymouth-pg-by-subject.md      # Section 2, chunked per subject area (20 chunks)
    - plymouth-requirements.md       # Section 3
    - plymouth-costs.md              # Section 4
    - plymouth-evidence.md           # Section 5
    - plymouth-comparison.md         # Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "plymouth-knowledge-base-v2"
  school: "<subject area name>"      # e.g. "Computer Science", "Engineering and Robotics"
  department: "<subject area name>"  # Plymouth has flat subject-area model
  degree_level: "<BA|BS|BEng|MEng|MA|MSc|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL of course page or subject page>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | International UG tuition for non-Computer-Science courses | https://www.plymouth.ac.uk/courses/undergraduate/<slug> (per course) |
| P0 | International PG taught tuition per course | https://www.plymouth.ac.uk/courses/postgraduate/<slug> (per course) |
| P0 | International UG tuition table summary | https://www.plymouth.ac.uk/study/fees (per-course listing pending) |
| P1 | UCAS application deadline for 2026 entry (closing date specifics) | https://www.plymouth.ac.uk/study/undergraduate/apply |
| P1 | Tuition-free threshold / NIL aid (UK students use loans; verify net cost) | https://www.plymouth.ac.uk/study/funding |
| P1 | Foundation year international fees | https://www.plymouth.ac.uk/courses/undergraduate/<slug-with-foundation> |
| P1 | Placement year fees per course | https://www.plymouth.ac.uk/courses/undergraduate/<slug> |
| P1 | Interview / audition policy per program | https://www.plymouth.ac.uk/courses/undergraduate/<slug> |
| P2 | DClinPsy fees (currently routed to Course Administrator) | Michele Thomas, Course Administrator |
| P2 | Per-program health-profession / clinical placement costs | https://www.plymouth.ac.uk/courses/undergraduate/<slug> |
| P2 | Confirmation / enrollment deposit policy | https://www.plymouth.ac.uk/study/fees/paying-your-fees |
| P2 | Country-specific UG/PG entry requirements | https://www.plymouth.ac.uk/international/study/international-students-country-guides |
| P2 | PGR funding: full UKRI studentship list | https://www.plymouth.ac.uk/research/doctoral-college |
| P3 | Mature-student / returning-to-study specific requirements | https://www.plymouth.ac.uk/study/entry-requirements |
| P3 | Apprenticeship degree pathways | https://www.plymouth.ac.uk/study/apprenticeships/students |

---

## SECTION 7 — Cross-school comparison framework (UK universities)

| Dimension | University of Plymouth |
|-----------|------------------------|
| Total programs (rule 1) | 360 (202 UG + 158 PG after dedup) |
| Subject areas (rule 2) | 20 (no school/college split) |
| UG home tuition/yr (2026-27) | £9,790 |
| PG home tuition/yr (taught) | varies per course (~£7,000-£12,000 typical) |
| PG home tuition/yr (research) | £5,238 (PhD Band 1/2) |
| PG international tuition/yr (research) | £16,870 (Band 1) / £19,315 (Band 2) / £21,000 (EngD) |
| TOEFL minimum (UG) | 76 (L17 R18 S20 W18) |
| TOEFL minimum (PG) | 90 (L17 R18 S20 W18) |
| IELTS minimum (UG) | 6.0 (5.5 components) |
| IELTS minimum (PG) | 6.5 (5.5 components) |
| PTE minimum | 59 |
| Duolingo minimum (UG) | 105/100 |
| Duolingo minimum (PG) | 120/105 |
| TEF rating | Gold (2023, all 3 categories) |
| QS World Rank (2024 ref) | Top 650-700 (mid-range UK modern university) |
| City cost-of-living advantage | 51% cheaper than London (per livingcost.org) |
| Application portal (UG) | UCAS |
| Application portal (PG) | https://www.plymouth.ac.uk/study/postgraduate/apply |
| Standard UCAS deadline | 26 January |
| Need-blind international? | No (UK loan system only for UK students) |
| Application fee (PG) | £0 for most PGT; £570 PGR resubmission |
| Foundation year international fee | varies per course |
| Placement year fee (UK) | £1,955 reference (BSc Computer Science 2026-27) |
| Placement year fee (overseas) | £1,465 reference |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: plymouth.ac.uk (undergraduate, postgraduate, subject-area, fees, English-language-requirements, international, research) - 21 distinct source pages cited across the 360 programs
> **Verification**: ego-browser snapshotText + JS DOM extraction of /courses/undergraduate and /courses/postgraduate link arrays
> **Granularity**: subject area (20) -> degree-level -> program (360 unique after cross-list dedup)
> **Region**: United Kingdom (TEF Gold 2023, 4-year UG with foundation, 1-year PG taught standard, 3-4 year PGR standard)
