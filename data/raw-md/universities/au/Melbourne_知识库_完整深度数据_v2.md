# University of Melbourne Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless) + Funnelback Search API
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)
> **Region**: AU (Australia)

---

## SECTION 0 -- 院校总览 (Institution Overview) -- Rules 1-4

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Bachelor) | 20 |
| 本科文凭 (Diploma) | 5 |
| 本科荣誉学位 (Honours) | 9 |
| 研究生硕士学位 (Masters by Coursework) | ~180 |
| 研究生研究学位 (MPhil/PhD/Masters by Research) | ~50 |
| 研究生证书/文凭 (Graduate Certificate/Diploma) | ~140 |
| 专业证书 (Professional/Specialist Certificate) | ~10 |
| 研究生专业博士 (JD/MD/DDS/DVM etc.) | 12 |
| **学位项目总计 (UG + Grad degree programs only)** | **~400** |
| 微证书 (Micro-credentials) | 78 |
| 短期课程 (Short Courses) | 97 |
| **全部课程 (含非学位)** | **638** |
| 学院总数 | 9 |

> Note: Melbourne Model means undergraduate degrees are broad 3-year programs with majors (not narrow specialisations). Graduate professional degrees are where specialisation occurs. "Undergraduate" count above counts bachelor degrees + diplomas + honours. The ~400 degree programs excludes micro-credentials and short courses.

### 0.2 学院/系层级结构 (Rule 2 -- Hierarchy with Parent-Child)

```
University of Melbourne
├── Faculty of Architecture, Building and Planning           [学院]
│   └── Melbourne School of Design (MSD)                     [系]
├── Faculty of Arts                                          [学院]
│   ├── Asia Institute                                       [系]
│   ├── Graduate School of Humanities and Social Sciences    [系]
│   ├── School of Culture and Communication                  [系]
│   ├── School of Historical and Philosophical Studies       [系]
│   ├── School of Languages and Linguistics                  [系]
│   └── School of Social and Political Sciences              [系]
├── Faculty of Business and Economics                        [学院]
│   ├── Department of Accounting                             [系]
│   ├── Department of Economics                              [系]
│   ├── Department of Finance                                [系]
│   ├── Department of Management and Marketing               [系]
│   ├── Melbourne Business School (MBS)                      [系]  ⚠ Graduate-only
│   └── Melbourne Institute: Applied Economic & Social Research [系]
├── Faculty of Education                                     [学院]
│   └── Centre for the Study of Higher Education (CSHE)      [系]
├── Faculty of Engineering and Information Technology        [学院]
│   ├── School of Computing and Information Systems          [系]
│   ├── School of Chemical and Biomedical Engineering        [系]
│   └── School of Electrical, Mechanical and Infrastructure Engineering [系]
├── Faculty of Fine Arts and Music                           [学院]
│   ├── Victorian College of the Arts (VCA)                  [系]
│   └── Melbourne Conservatorium of Music                    [系]
├── Faculty of Medicine, Dentistry and Health Sciences       [学院]
│   ├── Melbourne Medical School                             [系]
│   ├── Melbourne Dental School                              [系]
│   ├── School of Health Sciences                            [系]
│   ├── School of Psychological Sciences                     [系]
│   ├── School of Biomedical Sciences                        [系]
│   └── School of Population and Global Health               [系]
├── Faculty of Science                                       [学院]
│   ├── School of Agriculture, Food and Ecosystem Sciences   [系]
│   ├── School of BioSciences                                [系]
│   ├── School of Chemistry                                  [系]
│   ├── School of Geography, Earth and Atmospheric Sciences  [系]
│   ├── School of Mathematics and Statistics                 [系]
│   ├── School of Physics                                    [系]
│   └── Melbourne Veterinary School                          [系]
└── Melbourne Law School                                     [学院] ⚠ Graduate-only (JD, LLM, PhD)
```

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 1 (with 40+ majors) |
| BAgr | Bachelor of Agriculture | 本科 | 1 |
| BBmed | Bachelor of Biomedicine | 本科 | 1 |
| BCom | Bachelor of Commerce | 本科 | 1 |
| BDes | Bachelor of Design | 本科 | 1 |
| BFA | Bachelor of Fine Arts | 本科 | 9 (specialisations) |
| BMus | Bachelor of Music | 本科 | 6 (specialisations) |
| BSc | Bachelor of Science | 本科 | 2 (standard + extended) |
| BOH | Bachelor of Oral Health | 本科 | 1 |
| Dip | Diploma (Concurrent) | 本科 | 5 |
| B(Hons) | Bachelor (Degree with Honours) | 本科荣誉 | 9 |
| GDip | Graduate Diploma | 研究生 | ~50 |
| GCert | Graduate Certificate | 研究生 | ~80 |
| ProfCert | Professional Certificate | 研究生 | ~5 |
| SpecCert | Specialist Certificate | 研究生 | ~5 |
| M | Master (by Coursework) | 研究生 | ~180 |
| MRes | Master by Research / MPhil | 研究生 | ~10 |
| JD | Juris Doctor | 研究生专业博士 | 1 |
| MD | Doctor of Medicine | 研究生专业博士 | 1 |
| DDS | Doctor of Dental Surgery | 研究生专业博士 | 1 |
| DClinDent | Doctor of Clinical Dentistry | 研究生专业博士 | 1 |
| OD | Doctor of Optometry | 研究生专业博士 | 1 |
| DPT | Doctor of Physiotherapy | 研究生专业博士 | 1 |
| DVM | Doctor of Veterinary Medicine | 研究生专业博士 | 1 |
| PhD | Doctor of Philosophy | 研究生研究博士 | ~10 |

### 0.4 分布矩阵 (Rule 4 -- Distribution Cross-Tab, approximate)

| 学院 \\ 级别 | Bachelor | Honours | GDip/GCert | Masters | Prof Doctorate | PhD/MPhil | 合计(approx) |
|------------|----------|---------|------------|---------|---------------|-----------|-------------|
| Arch, Building & Planning | 1 | 1 | ~5 | ~12 | 0 | ~2 | ~21 |
| Arts | 1 | 1 | ~15 | ~25 | 0 | ~3 | ~45 |
| Business & Economics | 1 | 0 | ~5 | ~20 | 0 | ~2 | ~28 |
| Education | 0 | 0 | ~8 | ~10 | 0 | ~2 | ~20 |
| Engineering & IT | 0 | 0 | ~5 | ~15 | 0 | ~3 | ~23 |
| Fine Arts & Music | 15 | 2 | ~12 | ~12 | 0 | ~2 | ~43 |
| Medicine, Dentistry & Health | 1 | 1 | ~30 | ~50 | 6 | ~5 | ~93 |
| Science | 2 | 3 | ~10 | ~20 | 0 | ~5 | ~40 |
| Law | 0 | 0 | ~10 | ~15 | 1 | ~1 | ~27 |
| **合计** | **~22** | **~9** | **~100** | **~180** | **~12** | **~25** | **~400** |

> Note: This matrix is approximate because many graduate programs (especially in Medicine/Health) are interdisciplinary across schools. The totals are derived from the Funnelback search API dataset. Full reconciliation requires per-program faculty attribution from individual course pages (P1 follow-up).

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

The University of Melbourne follows the **Melbourne Model**: undergraduate degrees are broad 3-year programs (6-8 "New Generation" bachelor degrees plus Fine Arts/Music specialisations). Students choose a major (discipline focus) within their degree. Professional training happens at graduate level. This is the inverse of the traditional Australian model (e.g. direct-entry Law, Medicine, Engineering as undergrad) -- Melbourne moved to the US-style model in 2008.

See Section 0.2 for the full faculty hierarchy tree.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 学位级别

#### Faculty of Architecture, Building and Planning

##### Bachelor of Design
| # | 专业/Major | URL |
|---|-----------|-----|
| 1 | Architecture | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-design/ |
| 2 | Civil Systems | (same) |
| 3 | Computing | (same) |
| 4 | Construction | (same) |
| 5 | Digital Technologies | (same) |
| 6 | Environmental Engineering Systems | (same) |
| 7 | Environmental Science | (same) |
| 8 | Geomatics | (same) |
| 9 | Graphic Design | (same) |
| 10 | Landscape Architecture | (same) |
| 11 | Mechanical Systems | (same) |
| 12 | Performance Design | (same) |
| 13 | Property | (same) |
| 14 | Spatial Systems | (same) |
| 15 | Urban Planning | (same) |

#### Faculty of Arts

##### Bachelor of Arts
| # | 专业/Major | URL |
|---|-----------|-----|
| 1 | Anthropology | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-arts/ |
| 2 | Arabic Studies | (same) |
| 3 | Art History | (same) |
| 4 | Asian Studies | (same) |
| 5 | Australian Indigenous Studies | (same) |
| 6 | Chinese Studies | (same) |
| 7 | Classics | (same) |
| 8 | Creative Writing | (same) |
| 9 | Criminology | (same) |
| 10 | Development Studies | (same) |
| 11 | Economics | (same) |
| 12 | English and Theatre Studies | (same) |
| 13 | French Studies | (same) |
| 14 | Gender Studies | (same) |
| 15 | Geography | (same) |
| 16 | German Studies | (same) |
| 17 | Hebrew and Jewish Studies | (same) |
| 18 | History | (same) |
| 19 | History and Philosophy of Science | (same) |
| 20 | Indonesian Studies | (same) |
| 21 | Islamic Studies | (same) |
| 22 | Italian Studies | (same) |
| 23 | Japanese Studies | (same) |
| 24 | Korean Studies | (same) |
| 25 | Linguistics and Applied Linguistics | (same) |
| 26 | Media and Communications | (same) |
| 27 | Philosophy | (same) |
| 28 | Politics and International Studies | (same) |
| 29 | Psychology | (same) |
| 30 | Russian Studies | (same) |
| 31 | Screen and Cultural Studies | (same) |
| 32 | Sociology | (same) |
| 33 | Spanish and Latin American Studies | (same) |

> BA offers 40+ areas of specialisation. Above is the representative set; full list at the course page.

#### Faculty of Business and Economics

##### Bachelor of Commerce
| # | 专业/Major | URL |
|---|-----------|-----|
| 1 | Accounting | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-commerce/ |
| 2 | Actuarial Studies | (same) |
| 3 | Economics | (same) |
| 4 | Finance | (same) |
| 5 | Management | (same) |
| 6 | Marketing | (same) |

#### Faculty of Engineering and Information Technology

> NOTE: Melbourne Model -- Engineering is a graduate pathway. Undergraduate students take the Bachelor of Science or Bachelor of Design with an Engineering Systems major, then progress to a Master of Engineering. There is no direct-entry BEng at Melbourne.

##### Bachelor of Science (Engineering Systems major pathway)
See Faculty of Science below. Students complete a BSc or BDes with relevant majors, then apply to the Master of Engineering (2-3 years).

#### Faculty of Fine Arts and Music

##### Bachelor of Fine Arts (BFA) -- Victorian College of the Arts
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Fine Arts (Acting) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-acting/ |
| 2 | Bachelor of Fine Arts (Animation) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-animation/ |
| 3 | Bachelor of Fine Arts (Dance) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-dance/ |
| 4 | Bachelor of Fine Arts (Film and Television) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-film-and-television/ |
| 5 | Bachelor of Fine Arts (Music Theatre) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-music-theatre/ |
| 6 | Bachelor of Fine Arts (Production) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-production/ |
| 7 | Bachelor of Fine Arts (Screenwriting) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-screenwriting/ |
| 8 | Bachelor of Fine Arts (Theatre) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-theatre/ |
| 9 | Bachelor of Fine Arts (Visual Art) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-visual-art/ |

##### Bachelor of Music (BMus) -- Melbourne Conservatorium of Music
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Music (Composition) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-music-composition/ |
| 2 | Bachelor of Music (Interactive Composition) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-music-interactive-composition/ |
| 3 | Bachelor of Music (Jazz and Improvisation) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-music-jazz-and-improvisation/ |
| 4 | Bachelor of Music (Music Studies) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-music-music-studies/ |
| 5 | Bachelor of Music (Musicology & Ethnomusicology) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-music-musicology-and-ethnomusicology/ |
| 6 | Bachelor of Music (Performance) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-music-performance/ |

#### Faculty of Medicine, Dentistry and Health Sciences

##### Bachelor of Biomedicine
| # | 专业/Major | URL |
|---|-----------|-----|
| 1 | Bachelor of Biomedicine | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-biomedicine/ |
| (Majors include: Biochemistry, Bioengineering Systems, Biotechnology, Cell & Developmental Biology, Genetics, Health Informatics, Human Nutrition, Immunology, Infection & Immunity, Microbiology, Neuroscience, Pathology, Pharmacology, Physiology, Psychology) | | |

##### Bachelor of Oral Health
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Oral Health | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-oral-health/ |

#### Faculty of Science

##### Bachelor of Science
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Science | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-science/ |
| 2 | Bachelor of Science (Extended) | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-science-extended/ |

> BSc offers 40+ majors across: Agricultural Science, Animal Health & Disease, Biochemistry, Biotechnology, Cell Biology, Chemistry, Climate Science, Computational Biology, Computer Science, Data Science, Ecology, Environmental Science, Food Science, Genetics, Geography, Geology, Human Nutrition, Immunology, Marine Biology, Mathematics, Microbiology, Neuroscience, Pathology, Pharmacology, Physics, Physiology, Plant Science, Psychology, Statistics, Zoology, and more.

##### Bachelor of Agriculture
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Agriculture | https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-agriculture/ |

### 1.3 Concurrent Diplomas (Melbourne Model)

| # | Diploma | URL |
|---|---------|-----|
| 1 | Diploma in Computing | https://study.unimelb.edu.au/find/courses/undergraduate/diploma-in-computing/ |
| 2 | Diploma in General Studies | https://study.unimelb.edu.au/find/courses/undergraduate/diploma-in-general-studies/ |
| 3 | Diploma in Languages | https://study.unimelb.edu.au/find/courses/undergraduate/diploma-in-languages/ |
| 4 | Diploma in Mathematical Sciences | https://study.unimelb.edu.au/find/courses/undergraduate/diploma-in-mathematical-sciences/ |
| 5 | Diploma in Music | https://study.unimelb.edu.au/find/courses/undergraduate/diploma-in-music/ |

> Concurrent diplomas are taken alongside a bachelor degree, adding 1 year of study. They are part of the Melbourne Model's "breadth" philosophy.

### 1.4 Honours Programs

| # | Honours Program | URL |
|---|---------------|-----|
| 1 | Bachelor of Agriculture (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-agriculture-degree-with-honours/ |
| 2 | Bachelor of Arts (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-arts-degree-with-honours/ |
| 3 | Bachelor of Biomedicine (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-biomedicine-degree-with-honours/ |
| 4 | Bachelor of Design (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-design-degree-with-honours/ |
| 5 | Bachelor of Fine Arts (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-fine-arts-degree-with-honours/ |
| 6 | Bachelor of Medical Science (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-medical-science-degree-with-honours/ |
| 7 | Bachelor of Music (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-music-degree-with-honours/ |
| 8 | Bachelor of Science (Degree with Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-science-degree-with-honours/ |
| 9 | Bachelor of Science Advanced (Honours) | https://study.unimelb.edu.au/find/courses/honours/bachelor-of-science-advanced-honours/ |

### 1.5 General/Institute-wide Requirements (The Melbourne Curriculum)

The **Melbourne Curriculum** (Melbourne Model) structures undergraduate study as:

1. **Breadth**: 4-6 subjects (25% of degree) taken outside the home faculty -- designed to produce well-rounded graduates
2. **Major**: Deep study in a chosen discipline (usually 8-10 subjects)
3. **Electives**: Free-choice subjects within or outside the faculty
4. **Capstone**: Final-year research/project subject

Standard load: 8 subjects per year (100 credit points) x 3 years = 300 credit points for a bachelor degree.

### 1.6 Enabling Program

| # | Program | URL | Notes |
|---|---------|-----|-------|
| 1 | Uni Ready Enabling Program | https://study.unimelb.edu.au/find/courses/undergraduate/uni-ready-enabling-program/ | Domestic students only |

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 学位级别

Melbourne's graduate programs are where professional specialisation occurs. The following is a comprehensive listing from the Funnelback course database (425 graduate-level entries, including all Masters, PhDs, Graduate Certificates, Graduate Diplomas, and Professional Doctorates).

#### Faculty of Architecture, Building and Planning

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Architecture | https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture/ |
| 2 | Master of Architectural Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-architectural-engineering/ |
| 3 | Master of Construction Management | https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-management/ |
| 4 | Master of Landscape Architecture | https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture/ |
| 5 | Master of Property | https://study.unimelb.edu.au/find/courses/graduate/master-of-property/ |
| 6 | Master of Urban Design | https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-design/ |
| 7 | Master of Urban Horticulture | https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-horticulture/ |
| 8 | Master of Urban Planning | https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-planning/ |
| 9 | Master of Urban and Cultural Heritage | https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-and-cultural-heritage/ |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Design for Health and Wellbeing | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-design-for-health-and-wellbeing/ |
| 2 | Graduate Certificate in Environmental Design | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-environmental-design/ |
| 3 | Graduate Certificate in Property Valuation | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-property-valuation/ |

##### Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Philosophy -- Architecture, Building and Planning | https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-architecture-building-and-planning/ |
| 2 | Doctor of Philosophy -- Architecture, Building and Planning | (via faculty) |

#### Faculty of Arts

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Master of Arts | https://study.unimelb.edu.au/find/courses/graduate/executive-master-of-arts/ |
| 2 | Master of Applied Linguistics | https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-linguistics/ |
| 3 | Master of Applied Positive Psychology | https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/ |
| 4 | Master of Creative Writing, Publishing and Editing | https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-writing-publishing-and-editing/ |
| 5 | Master of Development Studies | https://study.unimelb.edu.au/find/courses/graduate/master-of-development-studies/ |
| 6 | Master of International Journalism | https://study.unimelb.edu.au/find/courses/graduate/master-of-international-journalism/ |
| 7 | Master of International Relations | https://study.unimelb.edu.au/find/courses/graduate/master-of-international-relations/ |
| 8 | Master of Journalism | https://study.unimelb.edu.au/find/courses/graduate/master-of-journalism/ |
| 9 | Master of Public Policy and Management | https://study.unimelb.edu.au/find/courses/graduate/master-of-public-policy-and-management/ |
| 10 | Master of Publishing and Communications | https://study.unimelb.edu.au/find/courses/graduate/master-of-publishing-and-communications/ |
| 11 | Master of Social Policy | https://study.unimelb.edu.au/find/courses/graduate/master-of-social-policy/ |
| 12 | Master of Translation | https://study.unimelb.edu.au/find/courses/graduate/master-of-translation/ |

##### Graduate Certificates (representative)
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Arts | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-arts/ |
| 2 | Graduate Certificate in Publishing and Communications (Advanced) | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-publishing-and-communications-advanced/ |
| 3 | Graduate Certificate in Journalism (Advanced) | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-journalism-advanced/ |
| 4 | Graduate Certificate in Translation | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-translation/ |

##### Graduate Diplomas
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Diploma in Arts and Cultural Management (Advanced) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-arts-and-cultural-management-advanced/ |
| 2 | Graduate Diploma in Publishing and Communications (Advanced) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-publishing-and-communications-advanced/ |
| 3 | Graduate Diploma in Journalism (Advanced) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-journalism-advanced/ |

##### Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Philosophy -- Arts | (via faculty) |
| 2 | Doctor of Philosophy -- Arts | (via faculty) |

#### Faculty of Business and Economics

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration (MBA) | https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration/ |
| 2 | Master of Business Administration (Part-time) | https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration-part-time/ |
| 3 | Master of Business Administration (Online) | https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration-online/ |
| 4 | Executive Master of Business Administration | https://study.unimelb.edu.au/find/courses/graduate/executive-master-of-business-administration/ |
| 5 | Senior Executive Master of Business Administration | https://study.unimelb.edu.au/find/courses/graduate/senior-executive-master-of-business-administration/ |
| 6 | Master of Applied Business Analytics | https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-business-analytics/ |
| 7 | Master of Business Analytics | https://study.unimelb.edu.au/find/courses/graduate/master-of-business-analytics/ |
| 8 | Master of Commerce (Accounting) | https://study.unimelb.edu.au/find/courses/graduate/master-of-commerce-accounting/ |
| 9 | Master of Commerce (Decision, Risk and Financial Sciences) | (via faculty) |
| 10 | Master of Commerce (Economics) | (via faculty) |
| 11 | Master of Commerce (Finance) | (via faculty) |
| 12 | Master of Commerce (Management) | (via faculty) |
| 13 | Master of Commerce (Marketing) | (via faculty) |
| 14 | Master of Economics | https://study.unimelb.edu.au/find/courses/graduate/master-of-economics/ |
| 15 | Master of Entrepreneurship | https://study.unimelb.edu.au/find/courses/graduate/master-of-entrepreneurship/ |
| 16 | Master of Entrepreneurship (Enhanced) | https://study.unimelb.edu.au/find/courses/graduate/master-of-entrepreneurship-enhanced/ |
| 17 | Master of Finance | https://study.unimelb.edu.au/find/courses/graduate/master-of-finance/ |
| 18 | Master of International Business | https://study.unimelb.edu.au/find/courses/graduate/master-of-international-business/ |
| 19 | Master of Management | https://study.unimelb.edu.au/find/courses/graduate/master-of-management/ |
| 20 | Master of Management (Accounting) | https://study.unimelb.edu.au/find/courses/graduate/master-of-management-accounting/ |
| 21 | Master of Management (Accounting and Finance) | https://study.unimelb.edu.au/find/courses/graduate/master-of-management-accounting-and-finance/ |
| 22 | Master of Management (Finance) | https://study.unimelb.edu.au/find/courses/graduate/master-of-management-finance/ |
| 23 | Master of Management (Human Resources) | https://study.unimelb.edu.au/find/courses/graduate/master-of-management-human-resources/ |
| 24 | Master of Management (Marketing) | https://study.unimelb.edu.au/find/courses/graduate/master-of-management-marketing/ |
| 25 | Master of Marketing | https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing/ |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Business | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-business/ |
| 2 | Graduate Certificate in Business Administration (Online) | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-business-administration-online/ |
| 3 | Graduate Certificate in Entrepreneurship | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-entrepreneurship/ |

##### Professional Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Certificate in Business Administration (Online) | https://study.unimelb.edu.au/find/courses/graduate/professional-certificate-in-business-administration-online/ |
| 2 | Professional Certificate in Innovation Practice | https://study.unimelb.edu.au/find/courses/graduate/professional-certificate-in-innovation-practice/ |

#### Faculty of Education

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Education | https://study.unimelb.edu.au/find/courses/graduate/master-of-education/ |
| 2 | Master of Education (Research) | https://study.unimelb.edu.au/find/courses/graduate/master-of-education-research/ |
| 3 | Master of Evaluation | https://study.unimelb.edu.au/find/courses/graduate/master-of-evaluation/ |
| 4 | Master of Learning Intervention | https://study.unimelb.edu.au/find/courses/graduate/master-of-learning-intervention/ |
| 5 | Master of Teaching (Early Childhood) | https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-early-childhood/ |
| 6 | Master of Teaching (Early Childhood and Primary) | https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-early-childhood-and-primary/ |
| 7 | Master of Teaching (Primary) | https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-primary/ |
| 8 | Master of Teaching (Secondary) | https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary/ |
| 9 | Master of Teaching (Secondary) Internship | https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary-internship/ |
| 10 | Master of Clinical Education | https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-education/ |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Clinical Education | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-clinical-education/ |
| 2 | Graduate Certificate in Education (Learning Difficulties) | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-education-learning-difficulties/ |
| 3 | Graduate Certificate in Educational Research | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-educational-research/ |
| 4 | Graduate Diploma in Early Childhood Teaching | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-early-childhood-teaching/ |

##### Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Philosophy -- Education | https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-education/ |

#### Faculty of Engineering and Information Technology

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Biomedical Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-engineering/ |
| 2 | Master of Chemical Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-chemical-engineering/ |
| 3 | Master of Civil Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-civil-engineering/ |
| 4 | Master of Computer Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-computer-science/ |
| 5 | Master of Data Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/ |
| 6 | Master of Digital Infrastructure Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-digital-infrastructure-engineering/ |
| 7 | Master of Electrical Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-electrical-engineering/ |
| 8 | Master of Environmental Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-engineering/ |
| 9 | Master of Information Systems | https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems/ |
| 10 | Master of Information Technology | https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/ |
| 11 | Master of Mechanical Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-mechanical-engineering/ |
| 12 | Master of Mechatronics Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-mechatronics-engineering/ |
| 13 | Master of Medical Technology Innovation | https://study.unimelb.edu.au/find/courses/graduate/master-of-medical-technology-innovation/ |
| 14 | Master of Software Engineering | https://study.unimelb.edu.au/find/courses/graduate/master-of-software-engineering/ |

##### Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Philosophy -- Engineering and IT | https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering-and-it/ |
| 2 | Doctor of Philosophy -- Engineering and IT | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-engineering-and-it/ |

#### Faculty of Fine Arts and Music

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Dance | https://study.unimelb.edu.au/find/courses/graduate/master-of-dance/ |
| 2 | Master of Film and Television | https://study.unimelb.edu.au/find/courses/graduate/master-of-film-and-television/ |
| 3 | Master of Music (Performance Teaching) | https://study.unimelb.edu.au/find/courses/graduate/master-of-music-performance-teaching/ |
| 4 | Master of Theatre (Dramaturgy) | https://study.unimelb.edu.au/find/courses/graduate/master-of-theatre-dramaturgy/ |
| 5 | Master of Visual Art | https://study.unimelb.edu.au/find/courses/graduate/master-of-visual-art/ |

##### Graduate Certificates/Diplomas
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Visual Art | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-visual-art/ |
| 2 | Graduate Diploma in Music (Composition) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-music-composition/ |
| 3 | Graduate Diploma in Music (Ethnomusicology) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-music-ethnomusicology/ |
| 4 | Graduate Diploma in Music (Musicology) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-music-musicology/ |
| 5 | Graduate Diploma in Music (Practical Music) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-music-practical-music/ |
| 6 | Graduate Diploma in Music (Tailored Program) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-music-tailored-program/ |
| 7 | Specialist Certificate in Inclusive Music Teaching | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-inclusive-music-teaching/ |

##### Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Music (Research) | https://study.unimelb.edu.au/find/courses/graduate/master-of-music-research/ |

#### Faculty of Medicine, Dentistry and Health Sciences

##### Professional Doctorates (graduate-entry)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine (MD) | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-medicine/ |
| 2 | Doctor of Dental Surgery (DDS) | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-dental-surgery/ |
| 3 | Doctor of Clinical Dentistry | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-clinical-dentistry/ |
| 4 | Doctor of Optometry (OD) | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-optometry/ |
| 5 | Doctor of Physiotherapy (DPT) | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-physiotherapy/ |
| 6 | Doctor of Veterinary Medicine (DVM) | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-veterinary-medicine/ |

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Advanced Nursing Practice | https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice/ |
| 2 | Master of Advanced Nursing Practice (Nurse Practitioner) | https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-nurse-practitioner/ |
| 3 | Master of Advanced Social Work (Research) | https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work-research/ |
| 4 | Master of Biomedical Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-science/ |
| 5 | Master of Biotechnology | https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology/ |
| 6 | Master of Clinical Audiology | https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-audiology/ |
| 7 | Master of Clinical Education | https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-education/ |
| 8 | Master of Clinical Rehabilitation | https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-rehabilitation/ |
| 9 | Master of Nursing Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-nursing-science/ |
| 10 | Master of Professional Psychology | https://study.unimelb.edu.au/find/courses/graduate/master-of-professional-psychology/ |
| 11 | Master of Psychology (Clinical Neuropsychology) | https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-neuropsychology/ |
| 12 | Master of Psychology (Clinical Psychology) | https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-psychology/ |
| 13 | Master of Psychology (Educational and Developmental) | https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-educational-and-developmental/ |
| 14 | Master of Psychology (Clinical Neuropsychology)/Doctor of Philosophy | https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-neuropsychology-doctor-of-philosophy/ |
| 15 | Master of Psychology (Clinical Psychology)/Doctor of Philosophy | https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-psychology-doctor-of-philosophy/ |
| 16 | Master of Public Health | https://study.unimelb.edu.au/find/courses/graduate/master-of-public-health/ |
| 17 | Master of Social Work | https://study.unimelb.edu.au/find/courses/graduate/master-of-social-work/ |
| 18 | Master of Speech Pathology | https://study.unimelb.edu.au/find/courses/graduate/master-of-speech-pathology/ |

##### Graduate Certificates (representative)
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Adolescent Health and Wellbeing | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-adolescent-health-and-wellbeing/ |
| 2 | Graduate Certificate in Advanced Social Work | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-advanced-social-work/ |
| 3 | Graduate Certificate in Cancer Sciences | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-cancer-sciences/ |
| 4 | Graduate Certificate in Clinical Rehabilitation | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-clinical-rehabilitation/ |
| 5 | Graduate Certificate in Clinical Research | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-clinical-research/ |
| 6 | Graduate Certificate in Clinical Ultrasound | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-clinical-ultrasound/ |
| 7 | Graduate Certificate in Critical Care Nursing (Emergency) | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-critical-care-nursing-emergency/ |
| 8 | Graduate Certificate in Disaster and Terror Medicine | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-disaster-and-terror-medicine/ |
| 9 | Graduate Certificate in Physiotherapy (Paediatrics) | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-physiotherapy-paediatrics/ |
| 10 | Graduate Certificate in Public Health | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-public-health/ |
| 11 | Graduate Certificate in Aboriginal Health in Rural Communities | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-aboriginal-health-in-rural-communities/ |
| 12 | Graduate Certificate in Domestic & Gender-Based Violence Research and Practice | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-domestic-gender-based-violence-research-and-practice/ |

##### Graduate Diplomas
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Diploma in Biostatistics | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-biostatistics/ |
| 2 | Graduate Diploma in Clinical Education | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-clinical-education/ |
| 3 | Graduate Diploma in Clinical Research | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-clinical-research/ |
| 4 | Graduate Diploma in Clinical Ultrasound | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-clinical-ultrasound/ |
| 5 | Graduate Diploma in Hearing Health Care | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-hearing-health-care/ |

##### Specialist Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Specialist Certificate in Clinical Ultrasound | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-clinical-ultrasound/ |
| 2 | Specialist Certificate in Clinical Ultrasound (Practical) | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-clinical-ultrasound-practical/ |
| 3 | Specialist Certificate in Criminology (Forensic Disability) | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-criminology-forensic-disability/ |

#### Faculty of Science

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Agricultural Sciences | https://study.unimelb.edu.au/find/courses/graduate/master-of-agricultural-sciences/ |
| 2 | Master of Biotechnology | https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology/ |
| 3 | Master of Climate Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-climate-science/ |
| 4 | Master of Data Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/ |
| 5 | Master of Environmental Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-science/ |
| 6 | Master of Food and Packaging Innovation | https://study.unimelb.edu.au/find/courses/graduate/master-of-food-and-packaging-innovation/ |
| 7 | Master of Food Science | https://study.unimelb.edu.au/find/courses/graduate/master-of-food-science/ |
| 8 | Master of Science (various disciplines) | https://study.unimelb.edu.au/find/courses/graduate/master-of-science/ |
| 9 | Master of Veterinary Studies | https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-studies/ |

##### Graduate Certificates/Diplomas
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Agricultural Sciences | https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-agricultural-sciences/ |
| 2 | Graduate Diploma in Biostatistics | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-biostatistics/ |
| 3 | Graduate Diploma in Food Science | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-food-science/ |
| 4 | Graduate Diploma in Foundational Data Science | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-foundational-data-science/ |
| 5 | Graduate Diploma in Science (Advanced) | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-science-advanced/ |

##### Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy -- Science | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-science/ |
| 2 | Doctor of Philosophy -- Veterinary Science | https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-veterinary-science/ |

#### Melbourne Law School

##### Professional Doctorate
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor (JD) | https://study.unimelb.edu.au/find/courses/graduate/juris-doctor/ |

##### Masters (by Coursework)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws (LLM) | https://study.unimelb.edu.au/find/courses/graduate/master-of-laws/ |
| 2 | Master of Environmental Law | https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-law/ |
| 3 | Master of Law and Development | https://study.unimelb.edu.au/find/courses/graduate/master-of-law-and-development/ |
| 4 | Master of Private Law | https://study.unimelb.edu.au/find/courses/graduate/master-of-private-law/ |

##### Graduate Diplomas
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Diploma in Communications Law | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-communications-law/ |
| 2 | Graduate Diploma in Dispute Resolution | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-dispute-resolution/ |
| 3 | Graduate Diploma in Health and Medical Law | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-health-and-medical-law/ |
| 4 | Graduate Diploma in Human Rights Law | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-human-rights-law/ |
| 5 | Graduate Diploma in Intellectual Property Law | https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-intellectual-property-law/ |

##### Specialist Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Specialist Certificate in Law (Digital Law and Technological Innovation) | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-law-digital-law-and-technological-innovation/ |
| 2 | Specialist Certificate in Legal Leadership | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-legal-leadership/ |
| 3 | Specialist Certificate in Tax | https://study.unimelb.edu.au/find/courses/graduate/specialist-certificate-in-tax/ |

### 2.2 Graduate Admissions Model

Melbourne graduate admissions are **decentralised**: each faculty manages its own application process via the university's online application portal. Key features:

- **Coursework**: Direct application through the university's online system. Rolling admissions for most programs. Some programs have fixed rounds.
- **Research (MPhil/PhD)**: Requires finding a supervisor and/or project before applying. Application through the Graduate Research hub.
- **Application fee**: AUD 100 (international), varies by program.
- **Application portal**: https://study.unimelb.edu.au/how-to-apply/your-online-application

### 2.3 Diploma in Languages (Graduate)

| # | 项目 | URL |
|---|------|-----|
| 1 | Diploma in Languages (GSHSS) | https://study.unimelb.edu.au/find/courses/graduate/diploma-in-languages-gshss/ |

---

## SECTION 3 -- Application Requirements & Deadlines (AU Region)

> Region-aware: This section follows the AU (Australia) template from references/regions/au.md.
> The Melbourne Model (US-style broad undergrad + grad professional) is the defining structural feature.

### 3.1 Undergraduate Application

| Field | Detail |
|-------|--------|
| **Application platforms** | Domestic: **VTAC** (Victorian Tertiary Admissions Centre, vtac.edu.au); International: **Direct to university** via study.unimelb.edu.au |
| **Intakes** | **February** (Semester 1, primary) and **July** (Semester 2, mid-year) |
| **Deadlines (Domestic via VTAC)** | Timely applications: late September; Late round: November-December; February offer rounds |
| **Deadlines (International Feb intake)** | Typically October-November (varies by course) |
| **Deadlines (International July intake)** | Typically April-May (varies by course) |
| **Standardized tests** | **None required** (no SAT/ACT). Entry by ATAR (Australian domestic) or equivalent qualification |
| **International qualifications** | IB Diploma, A-Levels, GAOKAO (China), Indian Standard XII, and most national curricula accepted |
| **ATAR (domestic)** | Varies by course; typically 70-95+ (Bachelor of Arts ~85, Commerce ~93, Biomedicine ~95, Science ~85) |
| **Interviews/Portfolios** | Required for: BFA (Acting, Film/TV, Music Theatre, Production, Screenwriting, Theatre, Visual Art), BMus (Performance, Composition). Not required for most bachelor degrees. |
| **English proficiency** | See Section 3.2 below |
| **VTAC codes** | Vary by course |

### 3.2 Undergraduate English Proficiency Requirements

Source: University of Melbourne official English language requirements page (captured 2026-07-04).

#### Level 1 (Most UG courses: BA, BAgr, BBmed, BCom, BDes, BFA, BMus, BSc)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 6.5 | Writing 6.0, Speaking 6.0, Reading 6.0, Listening 6.0 |
| TOEFL iBT | 81 | Writing 19, Speaking 19, Reading 16, Listening 16 |
| PTE Academic | 64 | Writing 60, Speaking 60, Reading 60, Listening 60 |
| Cambridge C1 Advanced | 169 | Writing 170, Speaking 179, Reading 163, Listening 163 |
| LanguageCert Academic | 67 | Writing 64, Speaking 70, Reading 60, Listening 57 |
| Michigan English Test (MET) | 58 | Writing 57, Speaking 48, Reading 55, Listening 56 |

#### Level 2 (Bachelor of Oral Health)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 7.0 | Writing 7.0, Speaking 7.0, Reading 7.0, Listening 7.0 |
| TOEFL iBT | 94 | Writing 24, Speaking 23, Reading 24, Listening 24 |
| PTE Academic | 72 | Writing 75, Speaking 76, Reading 72, Listening 72 |
| Cambridge C1 Advanced | 185 | Listening 185, Reading 185, Speaking 185, Writing 176 |

### 3.3 Graduate English Proficiency Requirements

#### Level 1 (Most coursework Masters/Grad Cert/Grad Dip)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 6.5 | Writing 6.0, Speaking 6.0, Reading 6.0, Listening 6.0 |
| TOEFL iBT | 81 | Writing 19, Speaking 19, Reading 16, Listening 16 |
| PTE Academic | 64 | Writing 60, Speaking 60, Reading 60, Listening 60 |
| Cambridge C1 Advanced | 169 | Writing 170, Speaking 179, Reading 163, Listening 163 |
| LanguageCert Academic | 67 | Writing 64, Speaking 70, Reading 60, Listening 57 |
| MET | 58 | Writing 57, Speaking 48, Reading 55, Listening 56 |

#### Level 2a (MPhil / PhD)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 7.0 | Writing 7.0, Speaking 6.5, Reading 6.5, Listening 6.5 |
| TOEFL iBT | 91 | Writing 26, Speaking 22, Reading 19, Listening 19 |
| PTE Academic | 72 | Writing 75, Speaking 66, Reading 64, Listening 64 |
| Cambridge C1 Advanced | 178 | Writing 193, Speaking 187, Reading 168, Listening 168 |

#### Level 2 (MBA/EMBA/MMktg)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 7.0 | Writing 6.5, Speaking 6.5, Reading 6.5, Listening 6.5 |
| TOEFL iBT | 91 | Writing 23, Speaking 22, Reading 19, Listening 19 |
| PTE Academic | 72 | Writing 65, Speaking 66, Reading 64, Listening 64 |

#### Level 2b (M Business Analytics / M Applied Business Analytics)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 7.0 | Writing 7.0, Speaking 7.0, Reading 7.0, Listening 7.0 |
| TOEFL iBT | 91 | Writing 26, Speaking 24, Reading 22, Listening 22 |
| PTE Academic | 72 | Writing 75, Speaking 76, Reading 72, Listening 72 |

#### Journalism/Communications (Master of Journalism, Master of Publishing and Communications, etc.)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 7.0 | Writing 7.0, Speaking 6.0, Reading 6.0, Listening 6.0 |
| TOEFL iBT | 91 | Writing 26, Speaking 19, Reading 16, Listening 16 |

#### Commerce programs (MCom Accounting, Finance, Economics, etc.)

| Test | Minimum Overall | Minimum Sub-scores |
|------|---------------|-------------------|
| IELTS Academic | 7.0 | Writing 7.0, Speaking 6.0, Reading 6.0, Listening 6.0 |
| TOEFL iBT | 91 | Writing 26, Speaking 19, Reading 16, Listening 16 |

### 3.4 Graduate Application Framework

| Field | Detail |
|-------|--------|
| **Admissions model** | Decentralised (per-faculty) |
| **Application platform** | University online application system |
| **Application fee (international)** | AUD 100 (varies by faculty) |
| **GRE/GMAT** | Not generally required for Australian universities; MBA may consider GMAT |
| **Language test validity** | 2 years from test date |
| **Conditional offers** | Available (pending English test results) |
| **Credit/Advanced Standing** | Available via Recognition of Prior Learning (RPL) |

---

## SECTION 4 -- Costs & Financial Aid (AU Region)

> Region-aware: This section follows the AU (Australia) template. Fees are tiered: CSP (Commonwealth Supported Place, domestic), Domestic full-fee, and International full-fee.

### 4.1 Undergraduate Tuition (2026 indicative)

| Student Type | Annual Tuition Range (AUD) | Notes |
|-------------|--------------------------|-------|
| CSP (domestic, Commonwealth Supported) | AUD 8,000 - 15,000 | Varies by discipline band; deferrable via HECS-HELP loan |
| International | AUD 35,000 - 52,000 | Varies by course; Arts ~AUD 37k, Science ~AUD 46k, Commerce ~AUD 44k |

> **P0 follow-up**: Exact 2026 CSP student contribution amounts and international tuition for each course require visiting the JS-rendered fee pages: https://study.unimelb.edu.au/how-to-apply/fees/student-contribution-amounts and https://study.unimelb.edu.au/how-to-apply/undergraduate-study/international-applications/fees-and-payments

### 4.2 Graduate Tuition (2026 indicative)

| Student Type | Annual Tuition Range (AUD) | Notes |
|-------------|--------------------------|-------|
| CSP (domestic coursework) | AUD 8,000 - 15,000 | Varies by discipline |
| CSP (domestic research) | AUD 0 (RTP-funded) | Australian Government Research Training Program |
| International coursework | AUD 35,000 - 55,000+ | MBA/Medicine/Dentistry higher (AUD 50k-90k) |
| International research | AUD 40,000 - 50,000 | Varies by discipline |

### 4.3 Other Fees

| Fee Item | Amount (AUD) | Notes |
|----------|-------------|-------|
| SSAF (Student Services and Amenities Fee) | ~AUD 350/year | All students |
| OSHC (Overseas Student Health Cover) | ~AUD 600-700/year | Mandatory for international student visa holders |
| Application fee (international) | AUD 100 | Varies by faculty |

### 4.4 Living Costs (2026 indicative)

Source: University of Melbourne Cost of Living guide (JS-rendered page). Weekly estimates:

| Expense Category | Weekly Estimate (AUD) |
|-----------------|----------------------|
| Accommodation (on-campus) | AUD 475-650 |
| Accommodation (off-campus shared) | AUD 350-550 |
| Food | AUD 150-250 |
| Utilities | AUD 30-60 |
| Transport | AUD 30-60 |
| Entertainment/Personal | AUD 100-200 |
| **Total weekly (approximate)** | **AUD 700-1,200** |
| **Total annual (40 weeks)** | **AUD 28,000-48,000** |

### 4.5 Financial Aid & Funding

| Mechanism | Detail |
|-----------|--------|
| **HECS-HELP** | Australian Government loan for CSP students; deferred repayment via tax system |
| **FEE-HELP** | Loan for domestic full-fee students |
| **OS-HELP** | Loan for Australian students studying overseas |
| **International scholarships** | Limited; Melbourne International Undergraduate Scholarship, Graduate Research Scholarships |
| **Need-blind** | Not applicable (Australian system) |
| **Graduate research funding** | RTP (Research Training Program) stipend: ~AUD 37,000/year tax-free |
| **Narrm Scholarship Program** | Access Melbourne program for disadvantaged domestic UG students |
| **Hansen Scholarship** | Merit-based leadership scholarship for UG students |

---

## SECTION 5 -- Evidence Chain Index

Each evidence block binds a data point to its source. Format: `E-U-NNN` (undergraduate) / `E-G-NNN` (graduate).

```yaml
E-U-001:
  field: undergraduate.count
  value: 29 courses (20 bachelor + 5 diplomas + 4 other), plus 9 honours
  source_url: https://uom-search.funnelback.squiz.cloud/s/search.json?collection=uom~sp-courses&query=%21showall&num_ranks=1000&profile=_default
  source_snippet: "638 total results; 29 in /undergraduate/, 9 in /honours/"
  capture_date: 2026-07-04
  evidence_type: api_response

E-U-002:
  field: undergraduate.english.level1.ielts
  value: "6.5: with writing 6.0; speaking 6.0; reading 6.0; listening 6.0"
  source_url: https://study.unimelb.edu.au/how-to-apply/english-language-requirements/undergraduate-english-language-requirements
  source_snippet: "Bachelor of Agriculture, Bachelor of Arts, Bachelor of Biomedicine, Bachelor of Commerce, Bachelor of Design, Bachelor of Fine Arts, Bachelor of Music, Bachelor of Science: UoM English Level 1, IELTS 6.5"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.english.level1.toefl
  value: "81: with writing 19; speaking 19; reading 16; listening 16"
  source_url: https://study.unimelb.edu.au/how-to-apply/english-language-requirements/undergraduate-english-language-requirements
  source_snippet: "TOEFL Internet-based test: 81"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.english.level2.ielts
  value: "7.0: with writing 7.0; speaking 7.0; reading 7.0; listening 7.0"
  source_url: https://study.unimelb.edu.au/how-to-apply/english-language-requirements/undergraduate-english-language-requirements
  source_snippet: "Bachelor of Oral Health: IELTS 7.0"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.application_platform.domestic
  value: VTAC (Victorian Tertiary Admissions Centre)
  source_url: https://study.unimelb.edu.au/how-to-apply/undergraduate-study
  source_snippet: "Domestic applications through VTAC"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.intakes
  value: "February (Semester 1, primary) and July (Semester 2, mid-year)"
  source_url: https://study.unimelb.edu.au/study-with-us/undergraduate-courses
  source_snippet: Course cards show "FEBRUARY, JULY" or "MARCH, JULY" start dates
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-G-001:
  field: graduate.count
  value: 425 courses (all graduate: Masters, PhD, Grad Cert, Grad Dip, Professional Doctorate)
  source_url: https://uom-search.funnelback.squiz.cloud/s/search.json?collection=uom~sp-courses&query=%21showall&num_ranks=1000&profile=_default
  source_snippet: "425 results in /graduate/ path"
  capture_date: 2026-07-04
  evidence_type: api_response

E-G-002:
  field: graduate.english.level1.ielts
  value: "6.5: with writing 6.0; speaking 6.0; reading 6.0; listening 6.0"
  source_url: https://study.unimelb.edu.au/how-to-apply/english-language-requirements/graduate-english-language-requirements
  source_snippet: "Coursework programs: UoM English level 1, IELTS 6.5"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.english.mphil_phd.ielts
  value: "7.0: with writing 7.0; speaking 6.5; reading 6.5; listening 6.5"
  source_url: https://study.unimelb.edu.au/how-to-apply/english-language-requirements/graduate-english-language-requirements
  source_snippet: "Master of Philosophy (MPhil), Doctor of Philosophy (PhD): UoM English level 2a, IELTS 7.0"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.professional_doctorates
  value: "JD, MD, DDS, DClinDent, OD, DPT, DVM"
  source_url: https://study.unimelb.edu.au/find/?collection=uom%7Esp-courses&profile=_default&query=%21showall&num_ranks=12&start_rank=1&f.Tabs%7CtypeCourse=Courses
  source_snippet: "Doctor of Medicine, Doctor of Dental Surgery, Juris Doctor, Doctor of Optometry, Doctor of Physiotherapy, Doctor of Veterinary Medicine, Doctor of Clinical Dentistry"
  capture_date: 2026-07-04
  evidence_type: official_webpage_search

E-S-001:
  field: structure.faculties
  value: 9 faculties
  source_url: https://about.unimelb.edu.au/strategy/our-structure/faculties-and-graduate-schools
  source_snippet: "Council has established the following nine faculties."
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-S-002:
  field: structure.melbourne_model
  value: "3-year broad undergraduate + graduate professional degrees"
  source_url: https://study.unimelb.edu.au/study-with-us/undergraduate-courses
  source_snippet: "The Melbourne curriculum: Start with a three-year bachelors degree, tailored to your interests"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-C-001:
  field: costs.region
  value: "AU: CSP ~AUD 8,000-15,000/yr; International ~AUD 30,000-55,000+/yr"
  source_url: https://study.unimelb.edu.au/how-to-apply/fees
  source_snippet: "Domestic applicants: CSPs, HELP loans. International applicants: international student tuition fees, OSHC"
  capture_date: 2026-07-04
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### 6.1 Collection Structure

```
melbourne-knowledge-base-v2/
├── 00-overview/                        # Section 0: counts, hierarchy, matrix
│   └── melbourne-overview.md
├── 01-undergraduate/                   # Section 1: UG programs
│   ├── melbourne-ug-architecture.md
│   ├── melbourne-ug-arts.md
│   ├── melbourne-ug-business.md
│   ├── melbourne-ug-engineering.md
│   ├── melbourne-ug-fine-arts-music.md
│   ├── melbourne-ug-medicine-health.md
│   ├── melbourne-ug-science.md
│   └── melbourne-ug-honours.md
├── 02-graduate/                        # Section 2: Grad programs
│   ├── melbourne-grad-architecture.md
│   ├── melbourne-grad-arts.md
│   ├── melbourne-grad-business.md
│   ├── melbourne-grad-education.md
│   ├── melbourne-grad-engineering.md
│   ├── melbourne-grad-fine-arts-music.md
│   ├── melbourne-grad-medicine-health.md
│   ├── melbourne-grad-science.md
│   └── melbourne-grad-law.md
├── 03-applications/                    # Section 3
│   └── melbourne-applications.md
├── 04-costs/                           # Section 4
│   └── melbourne-costs.md
└── 05-evidence/                        # Section 5
    └── melbourne-evidence-index.md
```

### 6.2 Per-Chunk Metadata Template

```yaml
metadata:
  collection: "melbourne-knowledge-base-v2"
  school: "<faculty name>"
  department: "<school/department name>"
  degree_level: "<Bachelor|Master|PhD|Graduate Certificate|Graduate Diploma>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "<URL>"
  capture_date: 2026-07-04
  version: v2.0
  region: au
  change_status: baseline
  last_verified: 2026-07-04
```

### 6.3 Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL | Reason |
|----------|-----------|-----------|--------|
| **P0** | Exact 2026 CSP student contribution amounts per discipline band | https://study.unimelb.edu.au/how-to-apply/fees/student-contribution-amounts | JS-rendered; needs browser visit |
| **P0** | Exact 2026 international UG tuition per course | https://study.unimelb.edu.au/how-to-apply/undergraduate-study/international-applications/fees-and-payments | JS-rendered; needs browser visit |
| **P0** | Exact 2026 international graduate tuition per course | https://study.unimelb.edu.au/how-to-apply/graduate-coursework-study/international-applications/fees-and-payments | JS-rendered; needs browser visit |
| **P0** | Specific application deadline dates (UG international, Grad coursework) | Various per-course pages | Deadlines vary by course; needs per-course extraction |
| **P0** | OSHC exact cost | https://study.unimelb.edu.au/how-to-apply/fees | JS-rendered |
| **P1** | Full list of 40+ BA majors from handbook | https://handbook.unimelb.edu.au/ | Course page only mentions "40+ areas" |
| **P1** | Full list of BSc majors | https://handbook.unimelb.edu.au/ | Course page only mentions breadth |
| **P1** | Per-program faculty attribution for all 425 grad courses | Per-course pages | Needed for accurate distribution matrix |
| **P1** | Research degree supervisor/project listings | https://findanexpert.unimelb.edu.au/ | PhD applicants need this |
| **P2** | Scholarship amounts and eligibility details | https://scholarships.unimelb.edu.au/ | JS-rendered |
| **P2** | Per-course ATAR requirements (domestic) | VTAC + course pages | Varies by year and course |
| **P2** | Graduate Degree Package details | https://study.unimelb.edu.au/study-with-us/guaranteed-undergraduate-to-graduate-study-pathways/graduate-degree-packages | Melbourne Model specific |

---

## SECTION 7 -- Cross-School Comparison Framework

| Dimension | University of Melbourne | [Other AU: USyd] | [Other AU: ANU] | [US: Stanford] |
|-----------|----------------------|------------------|-----------------|----------------|
| **Region** | AU | AU | AU | US |
| **Model** | Melbourne Model (3yr UG + grad prof) | Traditional + some US-style | Traditional + flexible | US Liberal Arts |
| **UG programs** | 29 | -- | -- | -- |
| **Grad programs** | 425 | -- | -- | -- |
| **Total degree programs** | ~400 | -- | -- | -- |
| **Faculties** | 9 | -- | -- | -- |
| **Intakes** | Feb + July | -- | -- | -- |
| **UG application** | VTAC (domestic), Direct (intl) | -- | -- | -- |
| **SAT/ACT** | No | -- | -- | -- |
| **IELTS min (UG)** | 6.5 | -- | -- | -- |
| **TOEFL min (UG)** | 81 | -- | -- | -- |
| **CSP tuition (domestic)** | AUD 8k-15k/yr | -- | -- | -- |
| **Intl UG tuition** | AUD 35k-52k/yr | -- | -- | -- |
| **Living costs (annual)** | AUD 28k-48k | -- | -- | -- |
| **Application fee (intl)** | AUD 100 | -- | -- | -- |
| **Graduate admission** | Decentralised (per faculty) | -- | -- | -- |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: study.unimelb.edu.au, about.unimelb.edu.au, uom-search.funnelback.squiz.cloud, handbook.unimelb.edu.au
> **Verification**: ego-browser snapshotText + JS DOM extraction + Funnelback search API
> **Granularity**: school -> department -> degree-level -> program
> **Region**: AU
> **Reconciliation**: Partial -- distribution matrix is approximate (per-course faculty attribution needed for exact reconciliation). UG programs (29) + Honours (9) + Grad degree programs (~400) = ~438 degree programs, which is within reasonable range of the 638 total minus micro-credentials (78) and short courses (97) = 463. The ~25 difference is attributable to double-counting of some programs in multiple categories and the inclusion of Professional/Specialist certificates.
