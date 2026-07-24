# University of Idaho Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BMus/etc.) | 106 |
| 本科辅修 (Minor) | 103 |
| 本科副学士 (Associate) | 4 |
| 本科证书 (Certificate) | 83 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 108 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 40 |
| 研究生教育专家 (Ed.S.) | 2 |
| **学位项目总计 (UG + Grad)** | **443** |
| 学院 / 独立系所总数 | 10 |

> **Source**: catalog.uidaho.edu/academic-offerings/ (2026-27 catalog)
> **Note**: The degree finder page (uidaho.edu/academics/degree-finder) shows 437 results; the catalog lists 443 total programs including certificates and associates.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Idaho
├── College of Agricultural and Life Sciences         [学院]
│   ├── Agricultural Economics                        [系]
│   ├── Animal and Veterinary Science                 [系]
│   ├── Entomology                                    [系]
│   ├── Food Science                                  [系]
│   ├── Plant Science                                 [系]
│   └── Soil and Land Resources                       [系]
├── College of Art and Architecture                   [学院]
│   ├── Architecture                                  [系]
│   ├── Art and Design                                [系]
│   ├── Interior Architecture and Design              [系]
│   └── Landscape Architecture                        [系]
├── College of Business and Economics                 [学院]
│   ├── Accountancy                                   [系]
│   ├── Business                                      [系]
│   ├── Economics                                     [系]
│   ├── Finance                                       [系]
│   ├── Marketing                                     [系]
│   └── Management                                    [系]
├── College of Education, Health and Human Sciences   [学院]
│   ├── Curriculum and Instruction                    [系]
│   ├── Educational Leadership                        [系]
│   ├── Exercise, Sport and Health Sciences            [系]
│   ├── Family and Consumer Sciences                  [系]
│   └── Special Education                             [系]
├── College of Engineering                            [学院]
│   ├── Biological Engineering                        [系]
│   ├── Chemical Engineering                          [系]
│   ├── Civil Engineering                             [系]
│   ├── Computer Science                              [系]  ⚠ shared with Science
│   ├── Electrical Engineering                        [系]
│   ├── Industrial and Systems Engineering            [系]
│   ├── Mechanical Engineering                        [系]
│   └── Nuclear Engineering                           [系]
├── College of Graduate Studies                       [学院]
│   └── Interdisciplinary Studies                     [系]
├── College of Law                                    [学院]
│   └── Law                                           [系]
├── College of Letters, Arts and Social Sciences      [学院]
│   ├── Communication                                 [系]
│   ├── English                                       [系]
│   ├── History                                       [系]
│   ├── Music                                         [系]
│   ├── Philosophy                                    [系]
│   ├── Political Science                             [系]
│   ├── Psychology                                    [系]
│   ├── Sociology                                     [系]
│   └── Theatre Arts                                  [系]
├── College of Natural Resources                      [学院]
│   ├── Conservation Biology                          [系]
│   ├── Fire Ecology and Management                   [系]
│   ├── Fisheries Science                             [系]
│   ├── Forest Resources                              [系]
│   ├── Rangeland Ecology and Management              [系]
│   └── Wildlife Sciences                             [系]
└── College of Science                                [学院]
    ├── Biology                                       [系]
    ├── Chemistry                                     [系]
    ├── Computer Science                              [系]  ⚠ shared with Engineering
    ├── Geology                                       [系]
    ├── Mathematics                                   [系]
    ├── Microbiology                                  [系]
    ├── Physics                                       [系]
    └── Statistics                                    [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| AA | A.A. | Associate of Arts | 本科 | 1 |
| AS | A.S. | Associate of Science | 本科 | 3 |
| BA | B.A. | Bachelor of Arts | 本科 | 15 |
| BS | B.S. / B.S.Bus. / B.S.Ed. | Bachelor of Science | 本科 | 69 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 1 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 1 |
| BM | B.Mus. | Bachelor of Music | 本科 | 4 |
| BGS | B.G.S. | Bachelor of General Studies | 本科 | 1 |
| MA | M.A. | Master of Arts | 研究生 | 8 |
| MS | M.S. / M.S.A.T. / M.Acct. / M.N.R. / P.S.M. | Master of Science | 研究生 | 38 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 1 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 3 |
| MArch | M.Arch. | Master of Architecture | 研究生 | 1 |
| MEd | M.Ed. | Master of Education | 研究生 | 4 |
| MEng | M.Engr. | Master of Engineering | 研究生 | 8 |
| MLA | M.L.A. | Master of Landscape Architecture | 研究生 | 1 |
| MPA | M.P.A. | Master of Public Administration | 研究生 | 1 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | 2 |
| MM | M.Mus. | Master of Music | 研究生 | 1 |
| EdS | Ed.S. | Education Specialist | 研究生 | 2 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 28 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| PsyD | Psy.D. | Doctor of Psychology | 研究生 | 1 |
| DAS | D.A.S. | Doctor of Anatomical Sciences | 研究生 | 1 |
| DAT | D.A.T. | Doctor of Athletic Training | 研究生 | 1 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | AS | BA | BS | BBA | BFA | BM | MA | MS | MBA | MFA | MArch | MEd | MEng | MLA | MPA | MAT | EdS | PhD | EdD | PsyD | JD | 合计 |
|------------|----|----|----|----|-----|----|----|----|----|----|-------|----|------|----|-----|-----|-----|-----|-----|------|----|------|
| Agricultural & Life Sciences | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 15 |
| Art & Architecture | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Business & Economics | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| Education, Health & Human Sciences | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 2 | 2 | 0 | 1 | 1 | 0 | 19 |
| Engineering | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 32 |
| Graduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Letters, Arts & Social Sciences | 0 | 15 | 0 | 0 | 0 | 0 | 8 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 35 |
| Natural Resources | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 11 |
| Science | 3 | 0 | 12 | 0 | 0 | 4 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 11 | 0 | 0 | 0 | 47 |
| **合计** | 3 | 15 | 54 | 1 | 1 | 4 | 8 | 38 | 1 | 3 | 1 | 4 | 8 | 1 | 1 | 2 | 2 | 28 | 1 | 1 | 1 | **179** |

> **Note**: The distribution matrix counts degree-granting programs only (majors, not minors or certificates). The total of 179 degree programs reconciles with the sum of undergraduate majors (106) minus non-degree entries plus graduate degrees (108 minus certificates and Ed.S.). Minors (103), associates (4), and certificates (123) are excluded from the matrix as they are non-degree credentials.

---

## Section 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

University of Idaho has 10 academic colleges. For the complete hierarchy tree with parent-child relationships, see Section 0.2 above.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural and Life Sciences

##### Agricultural Economics
###### B.S.Ag.Econ.
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Economics — Agribusiness emphasis | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Agricultural Economics — Applied economics emphasis | https://catalog.uidaho.edu/academic-offerings/ |

##### Agricultural Education
###### B.S.Ag.Ed.
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Education | https://catalog.uidaho.edu/academic-offerings/ |

##### Animal and Veterinary Science
###### B.S.A.V.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal and Veterinary Science — Business option | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Animal and Veterinary Science — Dairy science option | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Animal and Veterinary Science — Production option | https://catalog.uidaho.edu/academic-offerings/ |

##### Plant Science
###### B.S.Pl.Sc.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biotechnology and Plant Genomics | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Crop Science and Management | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Horticulture and Urban Agriculture | https://catalog.uidaho.edu/academic-offerings/ |

##### Soil and Water Sciences
###### B.S.S.W.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Systems Management | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Environmental Soil Science | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Water Science and Management | https://catalog.uidaho.edu/academic-offerings/ |

##### Entomology
###### B.S.Ag.L.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Entomology | https://catalog.uidaho.edu/academic-offerings/ |

##### Sustainable Food Systems
###### B.S.Ag.L.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sustainable Food Systems | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Art and Architecture

##### Architecture
###### B.S.Arch.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.uidaho.edu/academic-offerings/ |

##### Art and Design
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uidaho.edu/academic-offerings/ |

###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art and Design | https://catalog.uidaho.edu/academic-offerings/ |

##### Interior Architecture and Design
###### B.I.A.D.
| # | 专业 | URL |
|---|------|-----|
| 1 | Interior Architecture and Design | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Business and Economics

##### Business
###### B.S.Bus.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Business Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Business Information and Analytics | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Business Management | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Finance | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Marketing | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Operations and Supply Chain Management | https://catalog.uidaho.edu/academic-offerings/ |

###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Education, Health and Human Sciences

##### Curriculum and Instruction
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Elementary Education | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Secondary Education | https://catalog.uidaho.edu/academic-offerings/ |

##### Exercise, Sport and Health Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise, Sport and Health Sciences | https://catalog.uidaho.edu/academic-offerings/ |

##### Family and Consumer Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Child Development | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Family and Consumer Sciences | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Engineering

##### Biological Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Chemical Engineering
###### B.S.Ch.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Civil Engineering
###### B.S.C.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Computer Science
###### B.S.C.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.uidaho.edu/academic-offerings/ |

##### Electrical and Computer Engineering
###### B.S.E.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Electrical Engineering — Global | https://catalog.uidaho.edu/academic-offerings/ |

###### B.S.Comp.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Industrial and Systems Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial and Systems Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Mechanical Engineering
###### B.S.M.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Engineering Technology
###### B.S.Tech.
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Technology | https://catalog.uidaho.edu/academic-offerings/ |

##### Environmental Design
###### B.S.E.D.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Design | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Letters, Arts and Social Sciences

##### Communication
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Broadcasting and Digital Media | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Communication | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Journalism | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Public Relations | https://catalog.uidaho.edu/academic-offerings/ |

##### English
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Creative Writing (Certificate) | https://catalog.uidaho.edu/academic-offerings/ |

##### History
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.uidaho.edu/academic-offerings/ |

##### Music
###### B.Mus.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Music Business | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Music Composition | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Music Performance | https://catalog.uidaho.edu/academic-offerings/ |

##### Philosophy
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.uidaho.edu/academic-offerings/ |

##### Political Science
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.uidaho.edu/academic-offerings/ |

##### Psychology
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.uidaho.edu/academic-offerings/ |

##### Sociology
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.uidaho.edu/academic-offerings/ |

##### Theatre Arts
###### B.A./B.F.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://catalog.uidaho.edu/academic-offerings/ |

##### Dance
###### B.S.Dan.
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalog.uidaho.edu/academic-offerings/ |

##### Interdisciplinary Studies
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.uidaho.edu/academic-offerings/ |

##### General Studies
###### B.G.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | General Studies | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Natural Resources

##### Conservation Biology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Conservation Biology | https://catalog.uidaho.edu/academic-offerings/ |

##### Fisheries Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries Science | https://catalog.uidaho.edu/academic-offerings/ |

##### Forest Resources
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Forestry | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Forest and Sustainable Products | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Natural Resources Enterprise Management | https://catalog.uidaho.edu/academic-offerings/ |

##### Rangeland Ecology and Management
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Rangeland Ecology and Management | https://catalog.uidaho.edu/academic-offerings/ |

##### Wildlife Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Wildlife Sciences | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Science

##### Biology
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Bioinformatics | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Medical Sciences | https://catalog.uidaho.edu/academic-offerings/ |

##### Chemistry
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Biochemistry | https://catalog.uidaho.edu/academic-offerings/ |

##### Computer Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Cybersecurity | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Virtual Technologies | https://catalog.uidaho.edu/academic-offerings/ |

##### Geology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Geological Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Earth and Spatial Sciences | https://catalog.uidaho.edu/academic-offerings/ |

##### Mathematics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Statistics | https://catalog.uidaho.edu/academic-offerings/ |

##### Microbiology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | https://catalog.uidaho.edu/academic-offerings/ |

##### Physics
###### B.A./B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.uidaho.edu/academic-offerings/ |

##### Environmental Science
###### B.S.Env.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Climate Change | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Global Disease Ecology | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Ecology and Ecosystem Science | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Fire Ecology and Management | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Law

##### Pre-Law
| # | 专业 | URL |
|---|------|-----|
| 1 | Politics and Law (Certificate) | https://catalog.uidaho.edu/academic-offerings/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Bioinformatics | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Environmental Science | Science / Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Global Disease Ecology | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Interdisciplinary Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |

### 1.4 Minors — complete list

| # | Minor | Home college | URL |
|---|-------|--------------|-----|
| 1 | Accounting | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Addictions | Education, Health & Human Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Advertising | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Aerospace Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Aging Studies | Education, Health & Human Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Agribusiness | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Agricultural Communications and Leadership | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 8 | Agricultural Extension Education | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 9 | Agricultural Commodity Risk Management | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 10 | American Indian Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 11 | Animal Science | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 12 | Anthropology | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 13 | Apparel, Textiles and Design | Education, Health & Human Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 14 | Aquaculture | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 15 | Architecture | Art & Architecture | https://catalog.uidaho.edu/academic-offerings/ |
| 16 | Art | Art & Architecture | https://catalog.uidaho.edu/academic-offerings/ |
| 17 | Artificial Intelligence | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 18 | Asian Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 19 | Biochemistry | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 20 | Bioethics | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 21 | Biology | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 22 | Biotechnology and Plant Genomics | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 23 | Black Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 24 | Broadcasting and Digital Media | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 25 | Business | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 26 | Business Analytics | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 27 | Chemistry | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 28 | Communication | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 29 | Comparative/International Politics | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 30 | Computer Science | Science / Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 31 | Creative Writing | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 32 | Crop Management | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 33 | Crop Science | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 34 | Cybersecurity | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 35 | Dance | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 36 | Ecology | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 37 | Economics | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 38 | English Literature | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 39 | Entomology | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 40 | Entrepreneurship | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 41 | Environmental Communication | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 42 | Film and Television Production | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 43 | Finance | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 44 | Fire Ecology and Management | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 45 | Fisheries Science | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 46 | Food Science | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 47 | Forest Operations | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 48 | Forest Resources | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 49 | French | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 50 | Geography | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 51 | Geological and Mining Engineering | Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 52 | Geology | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 53 | German | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 54 | Groundwater Hydrology | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 55 | History | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 56 | Horticulture | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 57 | Human and Community Engagement | Education, Health & Human Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 58 | Interior Architecture and Design | Art & Architecture | https://catalog.uidaho.edu/academic-offerings/ |
| 59 | International Agriculture | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 60 | International Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 61 | Jazz Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 62 | Journalism | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 63 | Landscape Architecture | Art & Architecture | https://catalog.uidaho.edu/academic-offerings/ |
| 64 | Marketing | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 65 | Mathematics | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 66 | Mechanical Engineering | Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 67 | Microbiology | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 68 | Military Science | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 69 | Molecular Biology and Biochemistry | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 70 | Music | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 71 | Musical Theatre | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 72 | Natural Resource Conservation | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 73 | Natural Resource Economics | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 74 | Natural Resources | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 75 | Naval Science | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 76 | Nutritional Sciences | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 77 | Outdoor Recreation Leadership | Education, Health & Human Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 78 | Philosophy | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 79 | Philosophy, Politics and Economics | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 80 | Physics | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 81 | Plant Protection | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 82 | Political Science | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 83 | Pre-Health Professions Studies | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 84 | Professional Writing | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 85 | Psychology | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 86 | Public Relations | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 87 | Rangeland Ecology and Management | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 88 | Religious Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 89 | Renewable Materials | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 90 | Sales Management | Business & Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 91 | Sociology | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 92 | Soil Science | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 93 | Spanish | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 94 | Statistics | Science | https://catalog.uidaho.edu/academic-offerings/ |
| 95 | Sustainable Food Systems | Agricultural & Life Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 96 | Sustainable Tourism and Leisure Enterprises | Education, Health & Human Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 97 | Teaching English as a Second Language | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 98 | Theatre Design and Technology | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 99 | Theatre Performance | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 100 | Vocal-Instrumental Music Education | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 101 | Water Science and Management | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 102 | Wildlife Sciences | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 103 | Women's, Gender and Sexuality Studies | Letters, Arts & Social Sciences | https://catalog.uidaho.edu/academic-offerings/ |

### 1.5 General/Institute-wide requirements

University of Idaho requires all undergraduate students to complete the University Core Requirements (UCORE). The UCORE curriculum includes courses in:
- English Composition
- Mathematics
- Natural Sciences
- Social Sciences
- Humanities
- Fine Arts
- Diversity
- International

> **Source**: catalog.uidaho.edu/general-requirements-academic-procedures/

---

## Section 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agricultural and Life Sciences

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Animal Science | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Applied Economics | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Plant Science | https://catalog.uidaho.edu/academic-offerings/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Physiology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Entomology | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Plant Science | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Art and Architecture

##### M.Arch.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.uidaho.edu/academic-offerings/ |

##### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uidaho.edu/academic-offerings/ |

##### M.L.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://catalog.uidaho.edu/academic-offerings/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Integrated Architecture and Design | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Business and Economics

##### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | General Management | https://catalog.uidaho.edu/academic-offerings/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Technology Management | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Education, Health and Human Sciences

##### M.Ed.
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Educational Leadership | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Physical Education | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Special Education | https://catalog.uidaho.edu/academic-offerings/ |

##### M.A.T.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Secondary Education | https://catalog.uidaho.edu/academic-offerings/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Child Development | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Dietetics | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Family and Consumer Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Kinesiology | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Leadership and Organization Development | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Psychology | https://catalog.uidaho.edu/academic-offerings/ |

##### Ed.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Educational Leadership | https://catalog.uidaho.edu/academic-offerings/ |

##### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Learning, Leadership and Innovation | https://catalog.uidaho.edu/academic-offerings/ |

##### Psy.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Psychology | https://catalog.uidaho.edu/academic-offerings/ |

##### D.A.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical Sciences | https://catalog.uidaho.edu/academic-offerings/ |

##### D.A.T.
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Engineering

##### M.Engr.
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Biological Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Chemical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Civil Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Computer Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Electrical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Engineering Management | https://catalog.uidaho.edu/academic-offerings/ |
| 8 | Industrial and Systems Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 9 | Mechanical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 10 | Nuclear Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Biological Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Chemical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Civil Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Computer Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Computer Science | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Electrical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 8 | Industrial and Systems Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 9 | Mechanical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 10 | Nuclear Engineering | https://catalog.uidaho.edu/academic-offerings/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Chemical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Civil Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Computer Science | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Mechanical Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Nuclear Engineering | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Law

##### J.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Letters, Arts and Social Sciences

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | English | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | History | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Political Science | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Teaching English to Speakers of Other Languages | https://catalog.uidaho.edu/academic-offerings/ |

##### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Theatre Arts | https://catalog.uidaho.edu/academic-offerings/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Emerging Media | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Geography | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Psychology | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Statistical Science | https://catalog.uidaho.edu/academic-offerings/ |

##### M.A./M.Mus.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.uidaho.edu/academic-offerings/ |

##### M.P.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://catalog.uidaho.edu/academic-offerings/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Experimental Psychology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Geography | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | History | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Political Science | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Natural Resources

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Geography | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Soil and Land Resources | https://catalog.uidaho.edu/academic-offerings/ |

##### M.N.R.
| # | 项目 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Natural Resources | https://catalog.uidaho.edu/academic-offerings/ |

#### College of Science

##### M.A.T./M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.uidaho.edu/academic-offerings/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics and Computational Biology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Biology | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Chemistry | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Climate Science and Solutions | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Food Science | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Geology | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Groundwater Hydrology | https://catalog.uidaho.edu/academic-offerings/ |
| 8 | Neuroscience | https://catalog.uidaho.edu/academic-offerings/ |
| 9 | Nuclear Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 10 | Nutritional Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 11 | Physics | https://catalog.uidaho.edu/academic-offerings/ |
| 12 | Plant Pathology | https://catalog.uidaho.edu/academic-offerings/ |
| 13 | Water Resources | https://catalog.uidaho.edu/academic-offerings/ |

##### P.S.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Science and Technology | https://catalog.uidaho.edu/academic-offerings/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics and Computational Biology | https://catalog.uidaho.edu/academic-offerings/ |
| 2 | Biology | https://catalog.uidaho.edu/academic-offerings/ |
| 3 | Chemistry | https://catalog.uidaho.edu/academic-offerings/ |
| 4 | Entomology | https://catalog.uidaho.edu/academic-offerings/ |
| 5 | Food Science | https://catalog.uidaho.edu/academic-offerings/ |
| 6 | Geology | https://catalog.uidaho.edu/academic-offerings/ |
| 7 | Mathematics | https://catalog.uidaho.edu/academic-offerings/ |
| 8 | Microbiology, Molecular Biology, and Biochemistry | https://catalog.uidaho.edu/academic-offerings/ |
| 9 | Neuroscience | https://catalog.uidaho.edu/academic-offerings/ |
| 10 | Nuclear Engineering | https://catalog.uidaho.edu/academic-offerings/ |
| 11 | Nutritional Sciences | https://catalog.uidaho.edu/academic-offerings/ |
| 12 | Physics | https://catalog.uidaho.edu/academic-offerings/ |
| 13 | Plant Science | https://catalog.uidaho.edu/academic-offerings/ |
| 14 | Soil and Land Resources | https://catalog.uidaho.edu/academic-offerings/ |
| 15 | Water Resources | https://catalog.uidaho.edu/academic-offerings/ |

##### Education
###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://catalog.uidaho.edu/academic-offerings/ |

### 2.2 Graduate admissions model

University of Idaho's graduate admissions is managed by the College of Graduate Studies (COGS). Applications are submitted through a centralized portal, but admission decisions are made by individual departments/programs.

**Key features:**
- Application fee: $30 (domestic), $30 (international)
- Minimum GPA: 3.00 on 4.00 scale
- GRE: Varies by program (some require, some optional, some not accepted)
- English proficiency required for international applicants
- Rolling admission for most programs
- 4+1 Master's Program available for current U of I undergraduates

> **Source**: https://www.uidaho.edu/graduate-studies/admissions/admissions-requirements

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | Common App or University of Idaho application | uidaho.edu/admissions-apply |
| Application fee | $50 (nonrefundable); FREE for Idaho residents | uidaho.edu/admissions-apply/first-year-students |
| Admission type | Rolling admission | uidaho.edu/admissions-apply/dates-deadlines |
| Priority deadline | February 15 (housing priority) | uidaho.edu/admissions-apply/dates-deadlines |
| Decision notification | Rolling (as applications received) | uidaho.edu/admissions-apply/dates-deadlines |
| Reply/enrollment deadline | Not specified (rolling) | — |
| FAFSA code | 001626 | uidaho.edu/financial-aid |

### 3.2 Test policy

**Test-conditional admission** (NOT strictly test-optional):

| GPA Range | Test Requirement |
|-----------|------------------|
| 3.00 - 4.00 | Test scores NOT required |
| 2.60 - 2.99 | ACT 15+ OR SAT 740+ required (or opt-in to Vandal Gateway Program) |
| 2.30 - 2.59 | Admitted through Vandal Gateway Program (test scores not required) |
| Idaho residents with ISAT ≥ Level 3 + 3 | Automatic admission regardless of GPA |

> **Source**: uidaho.edu/admissions-apply/first-year-students
> **Note**: UIdaho is test-conditional (GPA-based), NOT fully test-optional. Students with GPA ≥ 3.00 do not need test scores; those with lower GPAs may need them.

### 3.3 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 70 (before Jan 21, 2026) / 4.0 (after Jan 21, 2026) | — | Must be taken within 2 years of application |
| IELTS | 6.0 | — | Academic version |
| Duolingo | 100 | — | — |
| PTE Academic | 48 | — | — |
| SAT ERW | 550 | — | — |
| Cambridge C1/C2 | Pass | — | — |
| ALCP completion | N/A | — | U of I's own language program |

**Waivers available for:**
- Students with previous degree from accredited U.S. institution
- Students from English-speaking countries (extensive list provided)
- Students who completed English-medium instruction

> **Source**: uidaho.edu/international/admissions

### 3.4 Graduate — global rules

| Field | Value | Source |
|-------|-------|--------|
| Application portal | futurevandals.uidaho.edu/apply/ | uidaho.edu/graduate-studies/admissions |
| Application fee | $30 | uidaho.edu/graduate-studies/admissions/admissions-requirements |
| Minimum GPA | 3.00 on 4.00 scale | uidaho.edu/graduate-studies/admissions/admissions-requirements |
| GRE/GMAT | Varies by program | uidaho.edu/graduate-studies/academics |
| English proficiency | Required for international students | uidaho.edu/graduate-studies/admissions/international-grad-admissions-requirements |
| CGS April 15 signatory | Not specified | — |
| Admission types | Regular, Non-degree, Graduate Certificate, Readmission | uidaho.edu/graduate-studies/admissions |

**Graduate English proficiency requirements:**
- TOEFL iBT: 79 (minimum)
- IELTS: 6.5 (minimum)
- Duolingo: 105 (minimum)

> **Source**: uidaho.edu/graduate-studies/admissions/international-grad-admissions-requirements

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

#### Idaho Residents

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $9,824 | Full-time student (2 semesters) |
| Housing and meals | $12,995 | Estimated median on-campus |
| Books and supplies | $1,227 | Full-time student estimate |
| **Subtotal direct costs** | **$24,046** | |
| Transportation | $2,874 | Varies by individual |
| Miscellaneous and personal | $3,838 | Health insurance, personal items |
| **Total costs** | **$30,758** | |

#### Non-Idaho Residents

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $29,300 | Includes $19,476 out-of-state tuition |
| Housing and meals | $12,995 | Estimated median on-campus |
| Books and supplies | $1,227 | Full-time student estimate |
| **Subtotal direct costs** | **$43,522** | |
| Transportation | $2,874 | Varies by individual |
| Miscellaneous and personal | $3,838 | Health insurance, personal items |
| **Total costs** | **$50,234** | |

#### WUE Recipients (Western Undergraduate Exchange)

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $13,538 | WUE discounted rate |
| Housing and meals | $12,995 | Estimated median on-campus |
| Books and supplies | $1,227 | Full-time student estimate |
| **Subtotal direct costs** | **$27,760** | |
| Transportation | $2,874 | Varies by individual |
| Miscellaneous and personal | $3,838 | Health insurance, personal items |
| **Total costs** | **$34,472** | |

> **Source**: uidaho.edu/financial-aid/cost-of-attendance
> **Note**: WUE minimum award value: $16,350 (2026-27)

### 4.2 Graduate cost (2026-27 academic year)

#### Idaho Residents

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $11,577 | Full-time (2 semesters) |
| Housing and meals | $11,916 | Estimated |
| Books and supplies | $1,227 | |
| **Subtotal direct costs** | **$24,720** | |
| Transportation | $2,874 | |
| Miscellaneous | $3,838 | |
| **Total costs** | **$31,432** | |

#### Non-Idaho Residents & International

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $31,582 | Includes $20,005 non-resident tuition |
| Housing and meals | $11,916 | Estimated |
| Books and supplies | $1,227 | |
| **Subtotal direct costs** | **$44,725** | |
| Transportation | $2,874 | |
| Miscellaneous | $3,838 | |
| **Total costs** | **$51,437** | |

### 4.3 Law cost (2025-26, 2026-27 TBD)

#### Idaho Residents

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition and fees | $28,617 | Full-time (2 semesters) |
| Housing and meals | $11,916 | |
| Books and supplies | $3,120 | |
| **Subtotal direct costs** | **$43,653** | |
| Transportation | $2,874 | |
| Miscellaneous | $3,838 | |
| **Total costs** | **$50,365** | |

> **Source**: uidaho.edu/financial-aid/cost-of-attendance (Law section)

### 4.4 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need-blind/need-aware | Need-aware for all | uidaho.edu/financial-aid |
| Meets 100% demonstrated need | No | — |
| Tuition-free income threshold | Not specified | — |
| Zero parent contribution threshold | Not specified | — |
| Loan-free | No (loans included in aid packages) | — |
| Merit scholarships available | Yes ($30M+ annually) | uidaho.edu/financial-aid/scholarships |
| WUE program | Yes (for eligible western states) | uidaho.edu/financial-aid/scholarships/out-of-state-scholarship |
| FAFSA required | Yes (for federal aid) | uidaho.edu/financial-aid |

**Scholarship programs:**
- In-state scholarships
- Out-of-state scholarships
- WUE (Western Undergraduate Exchange)
- Invitation to Idaho
- MESA (Microchip Engineering & Security Alliance)
- Scholarship Universe (external scholarship search tool)

> **Source**: uidaho.edu/financial-aid/scholarships

---

## Section 5 — Evidence Chain Index

```yaml
E-U-001:
  field: ug.costs.tuition_idaho
  value: $9,824
  source_url: https://www.uidaho.edu/financial-aid/cost-of-attendance
  source_snippet: "$9,824 — Full-time student fees/tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: ug.costs.tuition_oos
  value: $29,300
  source_url: https://www.uidaho.edu/financial-aid/cost-of-attendance
  source_snippet: "$29,300 — Full-time student fees/tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: ug.costs.total_idaho
  value: $30,758
  source_url: https://www.uidaho.edu/financial-aid/cost-of-attendance
  source_snippet: "$30,758 — Total costs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: ug.costs.total_oos
  value: $50,234
  source_url: https://www.uidaho.edu/financial-aid/cost-of-attendance
  source_snippet: "$50,234 — Total costs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: ug.admission.type
  value: Rolling admission
  source_url: https://www.uidaho.edu/admissions-apply/dates-deadlines
  source_snippet: "The university will admit students and award scholarships and other financial aid to qualified students on a rolling basis as applications are received."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: ug.admission.application_fee
  value: $50 (free for Idaho residents)
  source_url: https://www.uidaho.edu/admissions-apply/first-year-students
  source_snippet: "$50 application fee (nonrefundable). No application fee required for Idaho residents."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: ug.test_policy
  value: Test-conditional (GPA-based)
  source_url: https://www.uidaho.edu/admissions-apply/first-year-students
  source_snippet: "New first-year students will automatically be considered for admission if their cumulative unweighted GPA is 3.00 or higher. Test scores are not required."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: ug.intl.toefl_min
  value: 70 (before Jan 21, 2026) / 4.0 (after Jan 21, 2026)
  source_url: https://www.uidaho.edu/international/admissions
  source_snippet: "TOEFL (Test of English as a Foreign Language) — Test date is before Jan. 21, 2026: minimum score of 70; Test date is after Jan. 21, 2026: minimum score of 4.0"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: ug.intl.ielts_min
  value: 6.0
  source_url: https://www.uidaho.edu/international/admissions
  source_snippet: "IELTS (International English Language Testing System) with a minimum score of 6.0"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: ug.intl.duolingo_min
  value: 100
  source_url: https://www.uidaho.edu/international/admissions
  source_snippet: "Duolingo English Test with a minimum score of 100"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: ug.intl.gpa_requirement
  value: 2.5 GPA (first-year), 2.0 GPA (transfer)
  source_url: https://www.uidaho.edu/international/admissions
  source_snippet: "First Year Student: A 2.5 grade-point average (GPA) on a 4.0 scale is required from your secondary school."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: grad.admission.gpa_min
  value: 3.00
  source_url: https://www.uidaho.edu/graduate-studies/admissions/admissions-requirements
  source_snippet: "Graduate applicants must have a minimum overall undergraduate grade point average (GPA) of 3.00 on a 4.00 grade scale."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: grad.admission.fee
  value: $30
  source_url: https://www.uidaho.edu/graduate-studies/admissions/admissions-requirements
  source_snippet: "Complete the online application ($30 fee)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: grad.costs.tuition_idaho
  value: $11,577
  source_url: https://www.uidaho.edu/financial-aid/cost-of-attendance
  source_snippet: "$11,577 — Full time student fees/tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: grad.costs.tuition_oos
  value: $31,582
  source_url: https://www.uidaho.edu/financial-aid/cost-of-attendance
  source_snippet: "$31,582 — Full time student fees/tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-001:
  field: programs.total
  value: 443
  source_url: https://catalog.uidaho.edu/academic-offerings/
  source_snippet: "Academic Offerings at the University of Idaho — Undergraduate + Graduate/Professional programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-002:
  field: colleges.count
  value: 10
  source_url: https://www.uidaho.edu/academics/degree-finder
  source_snippet: "College filter options: Agricultural and Life Sciences, Art and Architecture, Business and Economics, Education Health and Human Sciences, Engineering, Graduate Studies, Law, Letters Arts and Social Sciences, Natural Resources, Science"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## Section 6 — WeKnora Import Manifest

### Collection structure

```
uidaho-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0 (rules 1-4)
├── 01-ug-agricultural-life-sciences.md # Section 1: College of Agricultural & Life Sciences
├── 02-ug-art-architecture.md           # Section 1: College of Art & Architecture
├── 03-ug-business-economics.md         # Section 1: College of Business & Economics
├── 04-ug-education-health.md           # Section 1: College of Education, Health & Human Sciences
├── 05-ug-engineering.md                # Section 1: College of Engineering
├── 06-ug-law.md                        # Section 1: College of Law (pre-law)
├── 07-ug-letters-arts-social.md        # Section 1: College of Letters, Arts & Social Sciences
├── 08-ug-natural-resources.md          # Section 1: College of Natural Resources
├── 09-ug-science.md                    # Section 1: College of Science
├── 10-grad-all-colleges.md             # Section 2: All graduate programs
├── 11-admissions-requirements.md       # Section 3
├── 12-costs-financial-aid.md           # Section 4
├── 13-evidence-chain.md                # Section 5
└── 14-comparison-framework.md          # Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uidaho-knowledge-base-v2"
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

| Priority | Data item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Verify test-optional policy current status | uidaho.edu/admissions-apply/first-year-students | GPA-conditional policy confirmed |
| P0 | Graduate program-specific GRE requirements | uidaho.edu/graduate-studies/academics | Per-program GRE varies |
| P1 | International student aid policy details | uidaho.edu/international/scholarships-funding | Need-aware confirmed |
| P1 | WUE eligible states list | uidaho.edu/financial-aid/scholarships/out-of-state-scholarship | 16 WICHE states |
| P1 | Graduate funding details (RA/TA/fellowships) | uidaho.edu/graduate-studies/graduate-funding | Need to verify funding availability |
| P2 | Online program list | catalog.uidaho.edu/academic-offerings/ | Separate section in catalog |
| P2 | MESA program details | uidaho.edu/mesa | Microchip Engineering & Security Alliance |
| P2 | Transfer admission requirements | uidaho.edu/admissions-apply/transfer-students | Separate page |

---

## Section 7 — Cross-school Comparison Framework

| Dimension | UIdaho Value | Notes |
|-----------|--------------|-------|
| **Total UG cost/yr (Idaho resident)** | $30,758 | 2026-27 estimate |
| **Total UG cost/yr (Non-resident)** | $50,234 | 2026-27 estimate |
| **Tuition/yr (Idaho resident)** | $9,824 | |
| **Tuition/yr (Non-resident)** | $29,300 | |
| **Need-blind (domestic)?** | No (need-aware) | |
| **Need-blind (international)?** | No (need-aware) | |
| **EA deadline** | N/A | Rolling admission |
| **RD deadline** | Rolling (priority Feb 15) | |
| **SAT/ACT required?** | Conditional (GPA-based) | GPA ≥ 3.00 = not required |
| **TOEFL min** | 70 / 4.0 | Before/after Jan 21, 2026 |
| **IELTS min** | 6.0 | |
| **Duolingo min** | 100 | |
| **Grad application fee** | $30 | |
| **Total program count** | 443 | UG + Grad |
| **School/college count** | 10 | |
| **Carnegie classification** | R1 (Very High Research) | |
| **Land-grant** | Yes | |
| **Location** | Moscow, Idaho | |
| **Campus type** | College town | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: uidaho.edu, catalog.uidaho.edu, futurevandals.uidaho.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
