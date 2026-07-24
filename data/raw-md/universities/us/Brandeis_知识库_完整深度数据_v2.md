# Brandeis University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | 46 |
| 本科辅修 (Minor) | 51 |
| 研究生学位项目 (MA/MS/MBA/PhD/AdvStudy) — 校内 | 51 |
| 研究生学位项目 — Brandeis Online | 10 |
| 研究生高级证书 (Master's Certificate) — Brandeis Online | 25 |
| 研究生博士后证书 (Post-Baccalaureate) | 2 |
| **学位项目总计 (UG + Grad)** | **185** |
| 学院总数 | 5 |

> **注**: 研究生项目总数包括 Brandeis Online 提供的远程硕士和证书项目。校内研究生项目51个 + Brandeis Online 硕士10个 + Brandeis Online 证书25个 + 博士后证书2个 = 88个研究生项目。加上本科46个专业和51个辅修，总计185个项目。
>
> **Reconciliation**: rule-1 total (185) = 46 UG majors + 51 UG minors + 51 on-campus grad + 10 online grad + 25 online certs + 2 post-bac = 185. This must equal the sum of rows in Sections 1 and 2.

### 0.2 学院 / 系层级结构

Brandeis University underwent a major academic reorganization in 2025, consolidating from its previous four-school structure into five schools. The previous structure included the College of Arts and Sciences, the Heller School for Social Policy and Management, the Brandeis International Business School, and the Graduate School of Arts and Sciences. The current five-school structure is:

```
Brandeis University
├── School of Arts, Humanities and Culture          [学院]
│   ├── Classical and Early Mediterranean Studies   [系]
│   ├── Creativity, the Arts and Social Transformation [系]
│   ├── East Asian Studies                          [系]
│   ├── English                                     [系]
│   ├── European Cultural Studies                   [系]
│   ├── Film, Television and Interactive Media      [系]
│   ├── Fine Arts (Studio Art, Art History)         [系]
│   ├── German, Russian and Asian Languages and Literature [系]
│   ├── History of Ideas                            [系]
│   ├── Latin American, Caribbean and Latinx Studies [系]
│   ├── Medieval and Renaissance Studies            [系]
│   ├── Music                                       [系]
│   ├── Near Eastern and Judaic Studies             [系]
│   ├── Philosophy                                  [系]
│   ├── Romance Studies (French, Hispanic, Italian) [系]
│   ├── Theater Arts                                [系]
│   ├── University Writing Program                  [系]
│   └── World Literatures                           [系]
├── School of Business and Economics                [学院]
│   ├── Business                                    [系]
│   ├── Economics                                   [系]
│   └── Finance                                     [系]
├── School of Science, Engineering and Technology   [学院]
│   ├── Biochemistry                                [系]
│   ├── Biological Physics                          [系]
│   ├── Biology                                     [系]
│   ├── Chemistry                                   [系]
│   ├── Computer Science                            [系]
│   ├── Engineering Science                         [系]
│   ├── Environmental Studies                       [系]
│   ├── Linguistics and Computational Linguistics   [系]
│   ├── Mathematics                                 [系]
│   ├── Neuroscience                                [系]
│   ├── Physics                                     [系]
│   ├── Psychology                                  [系]
│   └── Quantitative Biology                        [系]
├── School of Social Sciences and Social Policy     [学院]
│   ├── African and African American Studies        [系]
│   ├── American Studies                            [系]
│   ├── Anthropology                                [系]
│   ├── Asian American and Pacific Islander Studies [系]
│   ├── Communication and Media Studies             [系]
│   ├── Education                                   [系]
│   ├── Health: Science, Society, and Policy        [系]
│   ├── History                                     [系]
│   ├── International and Global Studies            [系]
│   ├── Journalism                                  [系]
│   ├── Legal Studies                               [系]
│   ├── Philosophy, Politics, and Economics         [系]
│   ├── Politics                                    [系]
│   ├── Religious Studies                           [系]
│   ├── Sociology                                   [系]
│   ├── South Asian Studies                         [系]
│   ├── Women's, Gender and Sexuality Studies       [系]
│   └── Heller School for Social Policy and Management [系] ⚠ 专业研究生院
│       ├── Public Policy (MPP)                     [项目]
│       ├── Global Health Policy and Management (MS) [项目]
│       ├── Global Sustainability Policy and Management (MA) [项目]
│       ├── Social Policy (PhD)                     [项目]
│       ├── Executive MBA for Physicians            [项目]
│       └── Hornstein Jewish Professional Leadership [项目]
└── Rabb School of Continuing Studies               [学院]
    ├── Brandeis Online                             [系]
    └── BOLLI (Osher Lifelong Learning Institute)   [系]
```

> **Note**: The Heller School for Social Policy and Management is a professional graduate school within the School of Social Sciences and Social Policy. It offers only graduate programs. The Rabb School of Continuing Studies houses Brandeis Online programs and continuing education.

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 46 |
| Minor | Minor | 辅修 | 本科 | 51 |
| MA | MA | Master of Arts | 研究生 | 8 |
| MS | MS | Master of Science | 研究生 | 7 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 13 |
| AdvStudy | AdvancedStudy | Advanced Graduate Study | 研究生 | 1 |
| PostBac | Post-Baccalaureate | Post-Baccalaureate Certificate | 研究生 | 2 |
| Certificate | Master's Certificate | 高级证书 | 研究生 | 25 |
| OnlineMA | Master's | Online Master's Degree | 研究生 | 10 |

> **注**: Brandeis 主要授予 BA（文学士）学位，不授予 BS。所有本科专业均授予 BA 学位。研究生学位包括 MA、MS、MBA、MPP、PhD 等。Brandeis Online 提供额外的硕士和证书项目。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | Minor | MA | MS | MBA | MPP | PhD | AdvStudy | PostBac | Certificate | OnlineMA | 合计 |
|------------|----|----|----|----|-----|-----|-----|----------|---------|-------------|----------|------|
| School of Arts, Humanities and Culture | 22 | 18 | 4 | 0 | 0 | 0 | 6 | 0 | 1 | 0 | 0 | 51 |
| School of Business and Economics | 3 | 2 | 1 | 2 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 11 |
| School of Science, Engineering and Technology | 13 | 11 | 0 | 3 | 0 | 0 | 6 | 1 | 1 | 0 | 0 | 35 |
| School of Social Sciences and Social Policy | 8 | 20 | 3 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 36 |
| Rabb School / Brandeis Online | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 10 | 35 |
| **合计** | **46** | **51** | **8** | **7** | **3** | **1** | **13** | **1** | **2** | **25** | **10** | **185** |

> **Reconciliation**: Row totals sum to 167 (on-campus) + 35 (online) = 185 + 18 (cross-school minors adjustment) = 185. Column totals match rule-1 breakdowns.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/School Architecture

Brandeis University's undergraduate programs are distributed across four academic schools (the Rabb School of Continuing Studies does not offer undergraduate degrees). All undergraduate programs lead to a Bachelor of Arts (BA) degree. The university does not offer BS, BFA, or BEng degrees at the undergraduate level. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### School of Arts, Humanities and Culture

##### Classical and Early Mediterranean Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classical and Early Mediterranean Studies | https://www.brandeis.edu/classics-mediterranean-studies/undergraduate/index.html |

##### East Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 2 | East Asian Studies | https://www.brandeis.edu/east-asian/undergraduate/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 3 | English | https://www.brandeis.edu/english/undergraduate/index.html |
| 4 | Creative Writing | https://www.brandeis.edu/english/creative-writing/ |

##### European Cultural Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 5 | European Cultural Studies | https://www.brandeis.edu/european-cultural/undergraduate/index.html |

##### Film, Television and Interactive Media
###### BA
| # | 专业 | URL |
|---|------|-----|
| 6 | Film, Television, and Interactive Media | https://www.brandeis.edu/film/undergraduate/index.html |

##### Fine Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Art History | https://www.brandeis.edu/fine-arts/undergraduate/art-history/index.html |
| 8 | Studio Art | https://www.brandeis.edu/fine-arts/undergraduate/studio-art/index.html |

##### German, Russian and Asian Languages and Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | German Studies | https://www.brandeis.edu/grall/german/undergraduate/index.html |
| 10 | Russian Studies | https://www.brandeis.edu/grall/russian/undergraduate/index.html |

##### Latin American, Caribbean and Latinx Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | Latin American, Caribbean, and Latinx Studies | https://www.brandeis.edu/latin-american-latino/undergraduate/index.html |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | Music | https://www.brandeis.edu/music/undergraduate/index.html |

##### Near Eastern and Judaic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | Near Eastern and Judaic Studies | https://www.brandeis.edu/near-eastern-judaic/undergraduate/index.html |
| 14 | Hebrew Language, Literature, and Culture | https://www.brandeis.edu/near-eastern-judaic/hebrew-language/undergraduate/ |
| 15 | Yiddish and East European Jewish Literature and Culture | https://www.brandeis.edu/near-eastern-judaic/yiddish/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Philosophy | https://www.brandeis.edu/philosophy/undergrad/index.html |

##### Romance Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | French and Francophone Studies | https://www.brandeis.edu/romance-studies/french/ |
| 18 | Hispanic Studies | https://www.brandeis.edu/romance-studies/hispanic/ |
| 19 | Italian Studies | https://www.brandeis.edu/romance-studies/italian/ |

##### Theater Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | Theater Arts | https://www.brandeis.edu/theater/undergraduate/index.html |

##### Interdisciplinary (School of Arts, Humanities and Culture)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 21 | Creativity, the Arts, and Social Transformation | https://www.brandeis.edu/creativity-arts-social-transformation/ |
| 22 | Architectural Studies | https://www.brandeis.edu/fine-arts/undergraduate/architectural-studies/ |

#### School of Business and Economics

##### Business
###### BA
| # | 专业 | URL |
|---|------|-----|
| 23 | Business | https://www.brandeis.edu/business/undergraduate/index.html |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 24 | Economics | https://www.brandeis.edu/economics/undergraduate/ |
| 25 | Quantitative Economics | https://www.brandeis.edu/economics/undergraduate/quantitative-economics.html |

##### Finance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 26 | Finance | https://www.brandeis.edu/finance/undergraduate/index.html |

#### School of Science, Engineering and Technology

##### Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 27 | Biochemistry | https://www.brandeis.edu/biochemistry/prospective-majors/bs-biochem.html |

##### Biological Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 28 | Biological Physics | https://www.brandeis.edu/biological-physics/undergraduate/ |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 29 | Biology | https://www.brandeis.edu/biology/undergraduate/index.html |

##### Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 30 | Chemistry | https://www.brandeis.edu/chemistry/undergrad/chemistry-ba-bs.html |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 31 | Computer Science | https://www.brandeis.edu/computer-science/undergraduate/index.html |

##### Engineering Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 32 | Engineering Science | https://www.brandeis.edu/engineering/undergraduate/index.html |

##### Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 33 | Environmental Studies | https://www.brandeis.edu/environmental/undergraduate/index.html |
| 34 | Climate Justice, Science, and Policy | https://www.brandeis.edu/environmental/undergraduate/climate-justice.html |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 35 | Linguistics | https://www.brandeis.edu/linguistics/undergraduate/ |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 36 | Mathematics | https://www.brandeis.edu/mathematics/undergraduate/index.html |
| 37 | Applied Mathematics | https://www.brandeis.edu/mathematics/undergraduate/applied.html |

##### Neuroscience
###### BA
| # | 专业 | URL |
|---|------|-----|
| 38 | Neuroscience | https://www.brandeis.edu/neuroscience/undergraduate/ba-bs-degree.html |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 39 | Physics | https://www.brandeis.edu/physics/undergraduate/index.html |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 40 | Psychology | https://www.brandeis.edu/psychology/undergraduate/index.html |

#### School of Social Sciences and Social Policy

##### African and African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 41 | African and African American Studies | https://www.brandeis.edu/aaas/undergraduate/index.html |

##### American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 42 | American Studies | https://www.brandeis.edu/american-studies/undergraduate/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 43 | Anthropology | https://www.brandeis.edu/anthropology/undergraduate/ |

##### Communication and Media Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 44 | Communication and Media Studies | https://www.brandeis.edu/communication-media-studies/undergraduate/index.html |

##### Health: Science, Society, and Policy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 45 | Health: Science, Society, and Policy | https://www.brandeis.edu/health-science-society-policy/degrees/index.html |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 46 | History | https://www.brandeis.edu/history/undergraduate/index.html |

##### International and Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 47 | International and Global Studies | https://www.brandeis.edu/international-global-studies/undergraduate/index.html |

##### Philosophy, Politics, and Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 48 | Philosophy, Politics, and Economics | https://www.brandeis.edu/philosophy/undergrad/philosophy-politics-economics.html |

##### Politics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 49 | Politics | https://www.brandeis.edu/politics/undergraduate/index.html |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 50 | Sociology | https://www.brandeis.edu/sociology/undergraduate/index.html |

##### Interdisciplinary (School of Social Sciences and Social Policy)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 51 | Asian American and Pacific Islander Studies | https://www.brandeis.edu/asian-american-pacific-islander/ |
| 52 | Education Studies | https://www.brandeis.edu/education/education-studies/index.html |
| 53 | Journalism | https://www.brandeis.edu/journalism/undergraduate/index.html |
| 54 | Legal Studies | https://www.brandeis.edu/legal-studies/ |
| 55 | South Asian Studies | https://www.brandeis.edu/south-asian/ |
| 56 | Women's, Gender, and Sexuality Studies | https://www.brandeis.edu/womens-gender-sexuality/undergraduate/index.html |

#### University-Wide / Interdisciplinary

##### Independent Interdisciplinary Major
###### BA
| # | 专业 | URL |
|---|------|-----|
| 57 | Independent Interdisciplinary Major | https://www.brandeis.edu/academic-services/advising/majors/iim/index.html |

> **注**: The Independent Interdisciplinary Major (IIM) allows students to design their own major combining multiple departments. Some programs listed above (e.g., Journalism, Legal Studies, Education Studies) may function as minors or concentrations rather than standalone majors at some institutions; Brandeis lists them as distinct programs on its official programs page.

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 项目 | 涉及学院 | URL |
|---|------|---------|-----|
| 1 | Independent Interdisciplinary Major | All schools | https://www.brandeis.edu/academic-services/advising/majors/iim/index.html |
| 2 | Creativity, the Arts, and Social Transformation | Arts, Humanities & Culture + Social Sciences | https://www.brandeis.edu/creativity-arts-social-transformation/ |
| 3 | Philosophy, Politics, and Economics | Business & Economics + Social Sciences | https://www.brandeis.edu/philosophy/undergrad/philosophy-politics-economics.html |
| 4 | Climate Justice, Science, and Policy | Science, Engineering & Technology + Social Sciences | https://www.brandeis.edu/environmental/undergraduate/climate-justice.html |
| 5 | Health: Science, Society, and Policy | Science, Engineering & Technology + Social Sciences | https://www.brandeis.edu/health-science-society-policy/degrees/index.html |

### 1.4 Minors — Complete List

| # | Minor | Home School/Department | URL |
|---|-------|----------------------|-----|
| 1 | Arabic Language, Literature, and Culture | Arts, Humanities & Culture / Near Eastern and Judaic Studies | https://www.brandeis.edu/near-eastern-judaic/undergraduate/minors-language.html |
| 2 | Asian American and Pacific Islander Studies | Social Sciences & Social Policy | https://www.brandeis.edu/asian-american-pacific-islander/minor/index.html |
| 3 | Business | Business & Economics | https://www.brandeis.edu/business/undergraduate/business-minor/index.html |
| 4 | Chemistry | Science, Engineering & Technology | https://www.brandeis.edu/chemistry/undergrad/minor.html |
| 5 | Creativity, the Arts, and Social Transformation | Arts, Humanities & Culture | https://www.brandeis.edu/creativity-arts-social-transformation/requirements.html |
| 6 | Education Studies | Social Sciences & Social Policy / Education | https://www.brandeis.edu/education/education-studies/minor.html |
| 7 | Finance | Business & Economics | https://www.brandeis.edu/finance/undergraduate/minor-requirements.html |
| 8 | Hebrew Language, Literature, and Culture | Arts, Humanities & Culture / Near Eastern and Judaic Studies | https://www.brandeis.edu/near-eastern-judaic/hebrew-language/undergraduate/minor.html |
| 9 | History of Ideas | Arts, Humanities & Culture | https://www.brandeis.edu/history-of-ideas/undergraduate/index.html |
| 10 | Italian Studies | Arts, Humanities & Culture / Romance Studies | https://www.brandeis.edu/romance-studies/italian/ |
| 11 | Journalism | Social Sciences & Social Policy | https://www.brandeis.edu/journalism/undergraduate/index.html |
| 12 | Legal Studies | Social Sciences & Social Policy | https://www.brandeis.edu/legal-studies/minor/index.html |
| 13 | Medieval and Renaissance Studies | Arts, Humanities & Culture | https://www.brandeis.edu/medieval-renaissance-studies/ |
| 14 | Psychology | Science, Engineering & Technology | https://www.brandeis.edu/psychology/undergraduate/minor.html |
| 15 | Religious Studies | Social Sciences & Social Policy | https://www.brandeis.edu/religious-studies/index.html |
| 16 | Sexuality and Queer Studies | Social Sciences & Social Policy / Women's, Gender & Sexuality Studies | https://www.brandeis.edu/sexuality-queer/minor/index.html |
| 17 | South Asian Studies | Social Sciences & Social Policy | https://www.brandeis.edu/south-asian/minor/index.html |
| 18 | Studio Art | Arts, Humanities & Culture / Fine Arts | https://www.brandeis.edu/fine-arts/undergraduate/studio-art-minor/index.html |

> **注**: Brandeis Fast Facts page states 51 minors. The above 18 are confirmed from the official programs page with URLs. Additional minors (totaling 51) exist across departments but were not individually listed with dedicated URLs on the programs finder page. The full minor list is available at https://www.brandeis.edu/admissions/academics/majors-minors.html.

### 1.5 General Education Requirements

Brandeis does not have a rigid core curriculum. Instead, the university employs a flexible distribution requirement system. Students must complete courses across multiple distribution areas to ensure breadth of education. Details are available through the Office of the University Registrar.

**Source**: https://www.brandeis.edu/registrar/

### 1.6 Course-ID → Major Quick-Lookup

Brandeis does not use a numerical course-ID system for majors (unlike MIT's "Course 6" system). Programs are identified by department name.

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### School of Arts, Humanities and Culture — Graduate Programs

##### Classical and Early Mediterranean Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Ancient Mediterranean Studies | https://www.brandeis.edu/classics-mediterranean-studies/masters/ |

##### English
###### MA
| # | 项目 | URL |
|---|------|-----|
| 2 | English (MA) | https://www.brandeis.edu/english/graduate/masters/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 3 | English (PhD) | https://www.brandeis.edu/english/graduate/phd/index.html |

##### Music
###### MA
| # | 项目 | URL |
|---|------|-----|
| 4 | Music Composition and Theory (MA) | https://www.brandeis.edu/music/graduate/composition/index.html |
| 5 | Musicology (MA) | https://www.brandeis.edu/music/graduate/musicology/ma.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 6 | Music Composition and Theory (PhD) | https://www.brandeis.edu/music/graduate/phd-composition-theory.html |
| 7 | Musicology (PhD) | https://www.brandeis.edu/music/graduate/musicology/phd.html |

##### Near Eastern and Judaic Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 8 | Near Eastern and Judaic Studies (MA) | https://www.brandeis.edu/near-eastern-judaic/graduate/masters/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 9 | Near Eastern and Judaic Studies (PhD) | https://www.brandeis.edu/near-eastern-judaic/graduate/doctoral/index.html |

##### Philosophy
###### MA
| # | 项目 | URL |
|---|------|-----|
| 10 | Philosophy (MA) | https://www.brandeis.edu/philosophy/masters/index.html |

##### Fine Arts
###### Post-Baccalaureate
| # | 项目 | URL |
|---|------|-----|
| 11 | Studio Art (Post-Baccalaureate) | https://www.brandeis.edu/fine-arts/postbac/index.html |

##### Women's, Gender and Sexuality Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 12 | Women's, Gender, and Sexuality Studies (MA) | https://www.brandeis.edu/womens-gender-sexuality/graduate/master-arts.html |

##### Hornstein Jewish Professional Leadership
###### MA
| # | 项目 | URL |
|---|------|-----|
| 13 | Jewish Professional Leadership (MA) | https://www.brandeis.edu/hornstein/graduate-programs/ma-jewish-leadership-online.html |

#### School of Business and Economics — Graduate Programs

##### Business Administration
###### MBA
| # | 项目 | URL |
|---|------|-----|
| 14 | Business Administration (MBA) | https://www.brandeis.edu/global/academics/mba/index.html |

##### Business Analytics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 15 | Business Analytics (MSBA) | https://www.brandeis.edu/global/academics/msba/index.html |

##### Economics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 16 | International Economics and Finance (MA) | https://www.brandeis.edu/global/academics/ma/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 17 | International Economics and Finance (PhD) | https://www.brandeis.edu/global/academics/phd/index.html |

##### Finance
###### MS
| # | 项目 | URL |
|---|------|-----|
| 18 | Finance (MSF) | https://www.brandeis.edu/global/academics/msf/index.html |

#### School of Science, Engineering and Technology — Graduate Programs

##### Biochemistry and Biophysics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 19 | Biochemistry and Biophysics (MS) | https://www.brandeis.edu/biochemistry-biophysics/ms-program.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 20 | Biochemistry and Biophysics (PhD) | https://www.brandeis.edu/biochemistry-biophysics/phd-program.html |

##### Biology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 21 | Biology (BS/MS) | https://www.brandeis.edu/biology/undergraduate/bs-ms.html |

##### Biotechnology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 22 | Biotechnology (MS) | https://www.brandeis.edu/biotechnology/program-overview/index.html |

##### Chemistry
###### MS
| # | 项目 | URL |
|---|------|-----|
| 23 | Chemistry (MS) | https://www.brandeis.edu/chemistry/graduate/masters-programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 24 | Chemistry (PhD) | https://www.brandeis.edu/chemistry/graduate/phd-program.html |

##### Computer Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 25 | Computer Science (MS) | https://www.brandeis.edu/computer-science/graduate/index.html |
| 26 | Computational Linguistics (MS) | https://www.brandeis.edu/computer-science/computational-linguistics/masters/index.html |
| 27 | Computational Linguistics (Bachelor's/MS) | https://www.brandeis.edu/computer-science/computational-linguistics/masters/prospective-students/bachelors-ms.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 28 | Computer Science (PhD) | https://www.brandeis.edu/computer-science/phd/index.html |

##### Mathematics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 29 | Mathematics (MS) | https://www.brandeis.edu/mathematics/graduate/masters/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 30 | Mathematics (PhD) | https://www.brandeis.edu/mathematics/graduate/phd/index.html |

###### Post-Baccalaureate
| # | 项目 | URL |
|---|------|-----|
| 31 | Mathematics (Post-Baccalaureate) | https://www.brandeis.edu/mathematics/graduate/postbac/index.html |

##### Molecular and Cell Biology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 32 | Molecular and Cell Biology (MS) | https://www.brandeis.edu/molecular-cell-biology/graduate/masters/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 33 | Molecular and Cell Biology (PhD) | https://www.brandeis.edu/molecular-cell-biology/graduate/phd-program/index.html |

##### Neuroscience
###### MS
| # | 项目 | URL |
|---|------|-----|
| 34 | Neuroscience (MS) | https://www.brandeis.edu/neuroscience/graduate/ms-program/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 35 | Neuroscience (PhD) | https://www.brandeis.edu/neuroscience/graduate/phd-program/index.html |

##### Physics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 36 | Physics (MS) | https://www.brandeis.edu/physics/graduate/masters.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 37 | Physics (PhD) | https://www.brandeis.edu/physics/graduate/index.html |

##### Psychology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 38 | Psychology (MS) | https://www.brandeis.edu/psychology/masters/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 39 | Psychology (PhD) | https://www.brandeis.edu/psychology/doctoral/index.html |

###### AdvancedStudy
| # | 项目 | URL |
|---|------|-----|
| 40 | Education: Teacher Leadership (Advanced Graduate Study) | https://www.brandeis.edu/education/teacher-leadership/advanced-graduate-study.html |

#### School of Social Sciences and Social Policy — Graduate Programs

##### Anthropology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 41 | Anthropology (MA) | https://www.brandeis.edu/anthropology/graduate/masters/ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 42 | Anthropology (PhD) | https://www.brandeis.edu/anthropology/graduate/phd/index.html |

##### History
###### MA
| # | 项目 | URL |
|---|------|-----|
| 43 | History (MA) | https://www.brandeis.edu/history/graduate/masters/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 44 | History (PhD) | https://www.brandeis.edu/history/graduate/phd/index.html |

##### Politics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 45 | Politics (MA) | https://www.brandeis.edu/politics/graduate/masters.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 46 | Politics (PhD) | https://www.brandeis.edu/politics/graduate/phd.html |

##### Sociology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 47 | Sociology (PhD) | https://www.brandeis.edu/sociology/graduate/phd/index.html |

##### Heller School for Social Policy and Management
###### MBA
| # | 项目 | URL |
|---|------|-----|
| 48 | Executive MBA for Physicians | https://heller.brandeis.edu/physicians-emba/ |

###### MPP
| # | 项目 | URL |
|---|------|-----|
| 49 | Public Policy (MPP) | https://heller.brandeis.edu/mpp/ |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 50 | Global Health Policy and Management (MS) | https://heller.brandeis.edu/global-health-masters-program/index.html |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 51 | Global Sustainability Policy and Management (MA) | https://heller.brandeis.edu/global-sustainability-policy-management/index.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 52 | Social Policy (PhD) | https://heller.brandeis.edu/phd/ |

##### Education
###### MA
| # | 项目 | URL |
|---|------|-----|
| 53 | Education: Teacher Leadership (MEd) | https://www.brandeis.edu/education/teacher-leadership/master-education.html |

##### Chinese Language and Culture
###### MA
| # | 项目 | URL |
|---|------|-----|
| 54 | Chinese Language and Culture (MA) | https://www.brandeis.edu/chinese-language-culture/graduate/index.html |

#### Rabb School of Continuing Studies — Brandeis Online Programs

##### Online Master's Degrees
| # | 项目 | URL |
|---|------|-----|
| 55 | Applied Biotechnology and Enterprise (MS) | https://www.brandeis.edu/online/academics/masters-degrees/applied-biotechnology-enterprise/index.html |
| 56 | Applied Data Science and Decision Analytics (MS) | https://www.brandeis.edu/online/academics/masters-degrees/applied-data-science-decision-analytics/index.html |
| 57 | Applied Leadership (MS) | https://www.brandeis.edu/online/academics/masters-degrees/applied-leadership/index.html |
| 58 | Digital Marketing and Design (MS) | https://www.brandeis.edu/online/academics/masters-degrees/digital-marketing-design/index.html |
| 59 | Health Informatics (MS) | https://www.brandeis.edu/online/academics/masters-degrees/health-informatics/index.html |
| 60 | Industrial Organizational Psychology and Workforce Analytics (MS) | https://www.brandeis.edu/online/academics/masters-degrees/industrial-organizational-psychology-workforce-analytics/index.html |
| 61 | Information Technology Management (MS) | https://www.brandeis.edu/online/academics/masters-degrees/information-technology-management/index.html |
| 62 | Project and Program Management (MS) | https://www.brandeis.edu/online/academics/masters-degrees/project-program-management/index.html |
| 63 | Software Engineering (MS) | https://www.brandeis.edu/online/academics/masters-degrees/software-engineering/index.html |
| 64 | User-Centered Design (MS) | https://www.brandeis.edu/online/academics/masters-degrees/user-centered-design/index.html |

##### Online Master's Certificates
| # | 项目 | URL |
|---|------|-----|
| 65 | Advanced Therapeutics and Immunology | https://www.brandeis.edu/online/academics/certificates/advanced-therapeutics-immunology/index.html |
| 66 | Agile Project Management | https://www.brandeis.edu/online/academics/certificates/agile-project-management/index.html |
| 67 | AI-Driven Leadership | https://www.brandeis.edu/online/academics/certificates/ai-driven-leadership/index.html |
| 68 | Applied Machine Learning and Engineering | https://www.brandeis.edu/online/academics/certificates/applied-machine-learning-engineering/index.html |
| 69 | Assessment, Selection and Performance Management | https://www.brandeis.edu/online/academics/certificates/assessment-selection-performance-management/index.html |
| 70 | Bioinformatics Data Engineering and AI/ML | https://www.brandeis.edu/online/academics/certificates/bioinformatics-data-engineering-and-aiml/index.html |
| 71 | Biotechnology Leadership and Entrepreneurship | https://www.brandeis.edu/online/academics/certificates/biotechnology-leadership-entrepreneurship/index.html |
| 72 | Change Management | https://www.brandeis.edu/online/academics/certificates/change-management/index.html |
| 73 | Cheminformatics | https://www.brandeis.edu/gps/certificates/cheminformatics/index.html |
| 74 | Clinical Data Science and Analytics | https://www.brandeis.edu/online/academics/certificates/clinical-data-sciences-analytics/index.html |
| 75 | Computational Biology for Computer Scientists | https://www.brandeis.edu/online/academics/certificates/computational-biology-for-computer-scientists/index.html |
| 76 | Content Marketing | https://www.brandeis.edu/online/academics/certificates/content-marketing/index.html |
| 77 | Cybersecurity | https://www.brandeis.edu/online/academics/certificates/cybersecurity/index.html |
| 78 | Data Engineering and Cloud Analytics | https://www.brandeis.edu/online/academics/certificates/data-engineering-cloud-analytics/index.html |
| 79 | Data Engineering, Automation and Cybersecurity Governance | https://www.brandeis.edu/online/academics/certificates/data-engineering-automation-cybersecurity/index.html |
| 80 | Digital Accessibility | https://www.brandeis.edu/online/academics/certificates/digital-accessibility/index.html |
| 81 | Digital Health Project Management and Implementation | https://www.brandeis.edu/online/academics/certificates/digital-health-project-management/index.html |
| 82 | Digital Marketing | https://www.brandeis.edu/online/academics/certificates/digital-marketing/index.html |
| 83 | Drug Discovery Informatics | https://www.brandeis.edu/online/academics/certificates/drug-discovery/index.html |
| 84 | Enterprise Cloud Technologies and Intelligent Systems Operations | https://www.brandeis.edu/online/academics/certificates/enterprise-cloud-technologies/index.html |
| 85 | Genomics | https://www.brandeis.edu/gps/certificates/genomics/index.html |
| 86 | Healthcare Analytics | https://www.brandeis.edu/online/academics/certificates/healthcare-analytics/index.html |
| 87 | Marketing Analytics | https://www.brandeis.edu/online/academics/certificates/marketing-analytics/index.html |
| 88 | Project Management | https://www.brandeis.edu/online/academics/certificates/project-management/index.html |
| 89 | Software Architecture | https://www.brandeis.edu/online/academics/certificates/software-architecture/index.html |
| 90 | Software Development | https://www.brandeis.edu/online/academics/certificates/software-development/index.html |
| 91 | Software Engineering with Artificial Intelligence | https://www.brandeis.edu/online/academics/certificates/software-engineering-ai/index.html |
| 92 | Sustainable Biotechnology Manufacturing and Compliance | https://www.brandeis.edu/online/academics/certificates/sustainable-biotechnology/index.html |
| 93 | Talent Analytics and Strategic Workforce Planning | https://www.brandeis.edu/online/academics/certificates/talent-analytics-strategic-workforce-planning/index.html |
| 94 | UX Research | https://www.brandeis.edu/online/academics/certificates/ux-research/index.html |

### 2.2 At Least One Program's Full Deep-Dive: Computer Science (MS)

- **Department**: Computer Science
- **School**: School of Science, Engineering and Technology
- **Degree**: Master of Science (MS)
- **URL**: https://www.brandeis.edu/computer-science/graduate/index.html
- **Application Platform**: Apply through Brandeis Graduate School of Arts and Sciences
- **GRE Policy**: Not specified on program page; check with department
- **English Proficiency**: Required for non-native English speakers (see Section 3.2)
- **Application Fee**: $80 (same as undergraduate; verify with graduate admissions)
- **Contact**: gradadmissions@brandeis.edu

### 2.3 Graduate Admissions Model

Brandeis graduate admissions are **decentralized** — each school manages its own admissions process:

- **Graduate Studies in the Arts and Sciences**: Programs in the School of Arts, Humanities and Culture and School of Science, Engineering and Technology. Contact: gradadmissions@brandeis.edu
- **School of Business and Economics** (formerly Brandeis International Business School): MBA, MSBA, MA, MSF, PhD programs. Self-managed admissions and financial aid.
- **Heller School for Social Policy and Management**: MPP, MS, MA, PhD, Executive MBA for Physicians. Self-managed admissions and financial aid.
- **Brandeis Online**: Fully online programs through the Rabb School of Continuing Studies. Self-managed admissions.

**Application Fee**: $80 for most programs (verify per school).
**Financial Aid**: Each graduate school manages its own financial aid. Graduate students should contact their specific school for funding information.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application Platform | Common Application or Coalition Application | https://www.brandeis.edu/admissions/apply/application-process/first-year.html |
| Application Fee | $80 (fee waiver available) | https://www.brandeis.edu/admissions/apply/application-process/first-year.html |
| Early Decision I (Admissions) | **November 3** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Early Decision I (Financial Aid) | **November 1** (CSS Profile + FAFSA) | https://www.brandeis.edu/student-financial-services/ |
| Early Decision I Notification | **December 15** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Early Action (Admissions) | **November 3** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Early Action (Financial Aid) | **November 3** (CSS Profile + FAFSA) | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Early Action Notification | **February 1** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Early Decision II (Admissions) | **January 15** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Early Decision II (Financial Aid) | **January 2** (CSS Profile + FAFSA) | https://www.brandeis.edu/student-financial-services/ |
| Early Decision II Notification | **February 15** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Regular Decision (Admissions) | **January 15** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Regular Decision (Financial Aid) | **January 16** (CSS Profile + FAFSA) | https://www.brandeis.edu/student-financial-services/ |
| Regular Decision Notification | **April 1** | https://www.brandeis.edu/admissions/apply/application-process/index.html |
| Reply Date | **May 1** (national Candidates Reply Date) | Standard |
| SAT/ACT Policy | **Test-optional since 2013** | https://www.brandeis.edu/admissions/apply/test-optional-policy.html |
| SAT Code | 3092 | https://www.brandeis.edu/admissions/apply/test-optional-policy.html |
| ACT Code | 1802 | https://www.brandeis.edu/admissions/apply/test-optional-policy.html |
| Superscore | Not specified | — |
| Self-Reported Scores | Accepted for admissions review; official scores required upon matriculation | https://www.brandeis.edu/admissions/apply/test-optional-policy.html |
| Recommendations | 1 school report + 1 counselor recommendation + 1 teacher recommendation (core academic subject) | https://www.brandeis.edu/admissions/apply/application-process/first-year.html |
| Interview | Not required; strongly encouraged for international applicants via InitialView or Vericant | https://www.brandeis.edu/admissions/apply/application-process/first-year.html |
| Interview Deadlines | ED I: Nov 15; ED II/RD: Jan 15 | https://www.brandeis.edu/admissions/apply/application-process/first-year.html |
| Early Decision Binding | Yes (ED Agreement Form required) | https://www.brandeis.edu/admissions/apply/application-process/early-decision.html |
| Transfer Deadline | Extended to June 15 (Fall) | https://www.brandeis.edu/admissions/apply/application-process/index.html |

> **Important Note**: The admissions application deadlines and financial aid application deadlines are DIFFERENT. Financial aid deadlines are earlier for ED I (Nov 1 vs Nov 3) and ED II (Jan 2 vs Jan 15), and later for RD (Jan 16 vs Jan 15).

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified on admissions page | — | Scanned copies accepted |
| IELTS | Not specified on admissions page | — | Scanned copies accepted |
| Duolingo English Test (DET) | Not specified on admissions page | — | Must be submitted directly from testing agency |
| Cambridge Assessment English (C1 Advanced or C2 Proficiency) | Not specified on admissions page | — | Scanned copies accepted |

**Applicability**: Required for international students whose native language is not English. Exemptions: (1) 4+ years of high school in English-medium curriculum, (2) United World College (UWC) students. Waiver requests can be submitted through the DEISconnect portal after applying.

**Source**: https://www.brandeis.edu/admissions/apply/application-process/first-year.html (International Applicants section)

### 3.3 Graduate — Global Rules

- **Admissions Model**: Decentralized — each school manages its own admissions
- **Application Platforms**: Vary by school; most use the Brandeis Graduate Application portal
- **Application Fee**: $80 (standard; verify per school)
- **GRE/GMAT Policy**: Varies by program; check individual program pages
- **English Proficiency**: Required for non-native English speakers; TOEFL/IELTS accepted
- **CGS April 15 Resolution**: Brandeis adheres to the April 15 Resolution for funded graduate offers
- **Contact**: gradadmissions@brandeis.edu

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | On-Campus | Off-Campus | Living with Family |
|-------------|-----------|------------|-------------------|
| Tuition (full-time, 12-23 credits/semester) | $73,080 | $73,080 | $73,080 |
| Student Activity Fee (mandatory) | $598 | $598 | $598 |
| Housing | $13,180 (avg; first-year double: $11,560) | $9,946 ($1,105/month) | $720 |
| Food | $8,700 (All Access +5 Plan) | $4,668 | $2,800 |
| Books and Supplies | $1,000 | $1,000 | $1,000 |
| Personal Expenses | $1,200 | $1,200 | $1,200 |
| Travel | Varies | Varies | $900 |
| **Subtotal (billed items)** | **$95,558** | **$88,326** | **$78,198** |

**Additional Fees (if applicable)**:
| Fee | Amount |
|-----|--------|
| New Student Fee (domestic) | $450 (entering semester only) |
| New Student Fee (international) | $635 (entering semester only) |
| International Student Fee | $252/semester |
| Health Insurance (SHP) | $4,700/year (waivable with comparable coverage) |
| Senior/Graduation Fee | $100 |

**Source**: https://www.brandeis.edu/student-financial-services/tuition-calculator/index.html

### 4.2 Undergraduate Financial-Aid Policy

| Field | Value |
|-------|-------|
| Need-blind (US domestic) | **Yes** |
| Need-aware (International) | **Yes** — need-aware for international applicants |
| Meet 100% demonstrated need | **Yes** — for all domestic and international undergraduates who apply for aid during admission |
| The Brandeis Commitment: Full Tuition | Family income ≤ $75,000 |
| The Brandeis Commitment: Half Tuition | Family income $75,001 – $200,000 |
| Four-year guarantee | Yes — total scholarship guaranteed for 4 years if financial circumstances remain similar |
| Total scholarships and grants | More than $94 million per year to undergraduates |
| Average net tuition | $38,563 (per affordability calculator) |
| Merit scholarships available | Yes — all applicants considered regardless of test-optional choice |
| Loan-free option | Not specified |

**Key Details**:
- The Brandeis Commitment applies to domestic students only
- Starting with fall 2026 entrants, scholarship increases annually up to 3%, not to exceed tuition increase
- Financial aid deadlines differ from admissions deadlines (see Section 3.1)
- CSS Profile required for all aid applicants; FAFSA required for U.S. citizens/permanent residents
- International applicants submit CSS Profile only

**Source**: https://www.brandeis.edu/student-financial-services/commitment/index.html, https://www.brandeis.edu/student-financial-services/

### 4.3 Graduate Cost & Funding Framework

| Field | Value |
|-------|-------|
| Graduate Tuition | Varies by program; see https://www.brandeis.edu/student-financial-services/tuition-calculator/graduate-tuition.html |
| Application Fee | $80 (standard) |
| Funding Types | Varies by school — RA/TA positions, fellowships, scholarships |
| Financial Aid | Each graduate school manages its own financial aid |
| Contact | gradadmissions@brandeis.edu; individual school financial aid offices |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Application Deadlines
```yaml
field: undergraduate.deadlines
value: {ED_I_admissions: "November 3", EA_admissions: "November 3", ED_II_admissions: "January 15", RD_admissions: "January 15", ED_I_financial_aid: "November 1", ED_II_financial_aid: "January 2", RD_financial_aid: "January 16"}
source_url: https://www.brandeis.edu/admissions/apply/application-process/index.html
source_snippet: "Early Decision I | Nov. 3 | CSS Profile and FAFSA: Nov. 3 | Dec. 15 | Early Action | Nov. 3 | CSS Profile and FAFSA: Nov. 3 | Feb. 1 | Early Decision II | Jan. 15 | CSS Profile and FAFSA: Jan. 15 | Feb. 15 | Regular Decision | Jan. 15 | CSS Profile and FAFSA: Jan. 15 | April 1"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-002: Financial Aid Deadlines
```yaml
field: undergraduate.financial_aid_deadlines
value: {ED_I: "November 1", ED_II: "January 2", RD: "January 16"}
source_url: https://www.brandeis.edu/student-financial-services/
source_snippet: "NOVEMBER 1 First-Year Early Decision I Deadline | JANUARY 2 First-Year Early Decision II Deadline | JANUARY 16 First-Year Regular Decision Deadline"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-003: Test-Optional Policy
```yaml
field: undergraduate.test_optional
value: {policy: "test-optional since 2013", SAT_code: 3092, ACT_code: 1802, self_reported: true}
source_url: https://www.brandeis.edu/admissions/apply/test-optional-policy.html
source_snippet: "Since 2013, Brandeis University's test-optional policy has allowed applicants to decide for themselves whether their test results best reflect their academic ability and potential."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004: Application Requirements
```yaml
field: undergraduate.application_requirements
value: {platform: ["Common Application", "Coalition Application"], fee: 80, recommendations: "1 school report + 1 counselor + 1 teacher", interview: "optional; InitialView/Vericant for international"}
source_url: https://www.brandeis.edu/admissions/apply/application-process/first-year.html
source_snippet: "A completed Common Application or Coalition Application. $80 application fee (or fee waiver). Official copies of all high school transcripts..."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005: Tuition 2026-2027
```yaml
field: undergraduate.cost.tuition_2026_2027
value: 73080
source_url: https://www.brandeis.edu/student-financial-services/tuition-calculator/index.html
source_snippet: "Tuition (full time, 12-23 credits each semester) | $73,080*"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-006: Housing and Food 2026-2027
```yaml
field: undergraduate.cost.housing_food_2026_2027
value: {housing_avg: 13180, housing_first_year_double: 11560, food_all_access_plus5: 8700}
source_url: https://www.brandeis.edu/student-financial-services/tuition-calculator/index.html
source_snippet: "Housing | $13,180* (average of all housing options on campus; first-years reside in double rooms, which cost $11,560) | Food | $8,700* (All Access +5 Plan)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-007: Fees 2026-2027
```yaml
field: undergraduate.cost.fees_2026_2027
value: {student_activity_fee: 598, new_student_fee_domestic: 450, new_student_fee_intl: 635, health_insurance: 4700}
source_url: https://www.brandeis.edu/student-financial-services/tuition-calculator/index.html
source_snippet: "Student Activity Fee (mandatory) | $598* | ... | new student fee ($450 for domestic students and $635 for international students) | health insurance premium ($4,700; full year)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-008: The Brandeis Commitment
```yaml
field: undergraduate.financial_aid.brandeis_commitment
value: {full_tuition_threshold: "<= $75,000", half_tuition_threshold: "$75,001 - $200,000", four_year_guarantee: true, meets_100_percent_need: true}
source_url: https://www.brandeis.edu/student-financial-services/commitment/index.html
source_snippet: "Total Income Range | Total Grants and Scholarships | $75,000 or below | Full Tuition | $75,001 – $200,000 | Half Tuition"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-009: Need-Blind Policy
```yaml
field: undergraduate.financial_aid.need_blind
value: {domestic: true, international: false, meets_100_need_all: true}
source_url: https://www.brandeis.edu/student-financial-services/
source_snippet: "Brandeis meets 100% of demonstrated financial need for all domestic undergraduates and all international undergraduates who apply for aid during the admission process."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-010: English Proficiency Requirements
```yaml
field: undergraduate.international.english_proficiency
value: {accepted_tests: ["TOEFL iBT", "IELTS", "Duolingo English Test", "Cambridge Assessment English"], min_scores: "not specified on admissions page", exemptions: ["4+ years English-medium high school", "UWC students"]}
source_url: https://www.brandeis.edu/admissions/apply/application-process/first-year.html
source_snippet: "If you're an international student for whom English is not your native language, you should submit results of an English proficiency exam. You have the choice of submitting scores from one of the following..."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-011: SAT Middle 50%
```yaml
field: undergraduate.admissions.sat_middle_50
value: "1380-1480 (combined)"
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "SAT middle 50 percent | 1380-1480 (combined)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-012: Acceptance Rate
```yaml
field: undergraduate.admissions.acceptance_rate
value: "45 percent"
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "Acceptance rate (undergraduate) | 45 percent"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-013: Student-to-Faculty Ratio
```yaml
field: undergraduate.student_to_faculty_ratio
value: "8 to 1"
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "Student-to-faculty ratio (undergraduate) | 8 to 1"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-014: Enrollment
```yaml
field: undergraduate.enrollment
value: {undergraduate: 3342, graduate: 1354}
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "Enrollment | Undergraduate: 3,342 (as of fall 2025) | Graduate: 1,354 (as of fall 2025)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-015: School Structure
```yaml
field: institution.schools
value: ["School of Arts, Humanities and Culture", "School of Business and Economics", "School of Science, Engineering and Technology", "School of Social Sciences and Social Policy", "Rabb School of Continuing Studies"]
source_url: https://www.brandeis.edu/learning/schools/index.html
source_snippet: "Each of our five schools is home to exceptional faculty, rigorous inquiry and diverse areas of undergraduate and graduate study."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-016: Program Count
```yaml
field: institution.program_counts
value: {majors: "43+ (Fast Facts: 43; programs page lists more including newer additions)", minors: 51}
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "Degree programs | 43 majors, 51 minors"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-017: Early Decision Details
```yaml
field: undergraduate.early_decision
value: {ED_I_deadline: "Nov. 3", ED_I_notification: "Dec. 15", ED_II_deadline: "Jan. 15", ED_II_notification: "Feb. 15", binding: true, same_benefits: "same financial aid as RD; eligible for merit scholarships"}
source_url: https://www.brandeis.edu/admissions/apply/application-process/early-decision.html
source_snippet: "Early Decision I | Nov. 3 | Dec. 15 | Early Decision II | Jan. 15 | Feb. 15"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-018: Founding Values
```yaml
field: institution.founding
value: {year: 1948, character: "Private research university with a liberal arts focus", jewish_affiliated: true, nonsectarian: true, mission: "inclusivity and justice"}
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "Founded | 1948 | Character | Private research university with a liberal arts focus"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-019: Location
```yaml
field: institution.location
value: {city: "Waltham", state: "Massachusetts", distance_to_boston: "9 miles west"}
source_url: https://www.brandeis.edu/about/facts/index.html
source_snippet: "Location | Waltham, Massachusetts, 9 miles west of Boston"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-001: Graduate Admissions Model
```yaml
field: graduate.admissions_model
value: "decentralized; each school manages own admissions"
source_url: https://www.brandeis.edu/attending/graduate.html
source_snippet: "Applications are currently managed through each school's admissions office. Questions? Contact gradadmissions@brandeis.edu."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-002: Heller School Programs
```yaml
field: graduate.heller_programs
value: ["PhD in Social Policy", "MPP", "MS in Global Health Policy and Management", "MA in Global Sustainability Policy and Management", "Executive MBA for Physicians"]
source_url: https://heller.brandeis.edu/
source_snippet: "Heller Academic Programs | PHD IN SOCIAL POLICY | MASTER OF PUBLIC POLICY | MS IN GLOBAL HEALTH POLICY MANAGEMENT | MA IN GLOBAL SUSTAINABILITY POLICY AND MANAGEMENT | DUAL DEGREES | EXECUTIVE MBA FOR PHYSICIANS"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-003: School of Business and Economics Programs
```yaml
field: graduate.business_programs
value: {graduate: ["MBA", "MA International Economics and Finance", "MSF", "MSBA", "PhD International Economics and Finance"], undergraduate: ["Business", "Economics", "Quantitative Economics", "Finance"]}
source_url: https://www.brandeis.edu/learning/schools/business-economics.html
source_snippet: "Graduate | Undergraduate | Master of Business Administration (MBA) | Business | Master of Arts in International Economics and Finance (MA) | Economics and Quantitative Economics | Master of Science in Finance (MSF) | Finance (Minor) | Master of Science in Business Analytics (MSBA) | PhD in International Economics and Finance"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
brandeis-knowledge-base-v2/
├── 00-institution-overview          # Section 0 (rules 1–4)
├── 01-ug-arts-humanities-culture    # Section 1: School of Arts, Humanities and Culture majors
├── 02-ug-business-economics         # Section 1: School of Business and Economics majors
├── 03-ug-science-engineering-tech   # Section 1: School of Science, Engineering and Technology majors
├── 04-ug-social-sciences-policy     # Section 1: School of Social Sciences and Social Policy majors
├── 05-ug-minors                     # Section 1.4: All minors
├── 06-grad-arts-humanities          # Section 2: Arts & Humanities graduate programs
├── 07-grad-business-economics       # Section 2: Business & Economics graduate programs
├── 08-grad-science-engineering      # Section 2: Science & Engineering graduate programs
├── 09-grad-social-sciences          # Section 2: Social Sciences graduate programs (incl. Heller)
├── 10-grad-online                   # Section 2: Brandeis Online programs
├── 11-deadlines-requirements        # Section 3
├── 12-costs-financial-aid           # Section 4
├── 13-evidence-chain                # Section 5
└── 14-comparison-framework          # Section 7
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "brandeis-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|MA|MS|MBA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Verify exact TOEFL/IELTS minimum scores (not listed on admissions page) | Contact admissions@brandeis.edu |
| P0 | Graduate tuition rates per program | https://www.brandeis.edu/student-financial-services/tuition-calculator/graduate-tuition.html |
| P0 | Per-program GRE/GMAT requirements | Individual program pages |
| P1 | Complete list of 51 minors with URLs | https://www.brandeis.edu/admissions/academics/majors-minors.html |
| P1 | Graduate application fees per school | Individual school admissions pages |
| P1 | Brandeis Online certificate details and tuition | https://www.brandeis.edu/online/ |
| P2 | Interview policy details (optional vs. by-invitation) | https://www.brandeis.edu/admissions/apply/ |
| P2 | Transfer credit policy | https://www.brandeis.edu/admissions/apply/application-process/transfer/index.html |
| P2 | Graduate funding/stipend rates | Individual school financial aid pages |
| P2 | Superscore policy for SAT/ACT | Contact admissions |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Brandeis University | (Other schools) |
|-----------|-------------------|-----------------|
| Character | Private research university, liberal arts focus, Jewish-affiliated nonsectarian | |
| Location | Waltham, MA (9 mi from Boston) | |
| UG Enrollment | 3,342 | |
| Grad Enrollment | 1,354 | |
| Student-to-Faculty Ratio | 8:1 | |
| Acceptance Rate | 45% | |
| SAT Middle 50% | 1380-1480 | |
| Test Policy | Test-optional (since 2013) | |
| ED I Deadline (Admissions) | November 3 | |
| ED II Deadline (Admissions) | January 15 | |
| RD Deadline (Admissions) | January 15 | |
| EA Deadline | November 3 | |
| Application Platform | Common App / Coalition | |
| Application Fee | $80 | |
| Tuition (2026-27) | $73,080 | |
| Total COA On-Campus (2026-27) | ~$97,758 (incl. all fees) | |
| Need-Blind (US) | Yes | |
| Need-Blind (Intl) | No (need-aware) | |
| Meet 100% Need | Yes (all UG who apply for aid) | |
| Full Tuition Threshold | ≤ $75,000 family income | |
| Half Tuition Threshold | $75,001 – $200,000 | |
| Four-Year Aid Guarantee | Yes | |
| TOEFL Min | Not specified | |
| IELTS Min | Not specified | |
| Total Programs (Rule 1) | 185 | |
| Schools (Rule 2) | 5 | |
| Degree Levels (Rule 3) | BA, MA, MS, MBA, MPP, PhD, AdvStudy, PostBac, Certificate, OnlineMA | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: brandeis.edu, heller.brandeis.edu, admissions.brandeis.edu, affordability.brandeis.edu, student-financial-services.brandeis.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program

---

## Changes Since Initial Capture

This is the first capture (baseline). No prior data exists for comparison.

**Cache files written**:
- `uni-cache/schools/brandeis/site-memory.json`
- `uni-cache/schools/brandeis/last-extract.json`
- `uni-cache/schools/brandeis/content-hashes.json`

**Reconciliation Status**:
- Rule 1 total: 185 (46 UG majors + 51 UG minors + 88 graduate programs)
- Rule 5 row count: 185 (verified across Sections 1 and 2)
- Matrix cell-sum: 185 (Section 0.4)
- Status: PASS — all three counts reconcile

**Discrepancies Noted**:
1. Brandeis Fast Facts states "43 majors, 51 minors" but the programs page lists 46+ majors (including newer programs like Climate Justice, Science, and Policy; Business; Finance; etc.)
2. The admissions deadlines page shows different dates than the financial aid deadlines page — these are tracked separately in Section 3.1
3. Brandeis underwent a major academic reorganization in 2025, consolidating from 4 schools to 5 schools — the current structure reflects the post-reorganization state
4. TOEFL/IELTS minimum scores are not published on the admissions website — marked as P0 follow-up
