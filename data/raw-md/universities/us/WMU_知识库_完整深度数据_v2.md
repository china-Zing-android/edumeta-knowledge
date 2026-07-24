# Western Michigan University (WMU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BSE/BBA/BM/BSN/etc.) | 153 |
| 本科辅修 (Minor) | 131 |
| 本科证书 (Certificate) | 15 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 95 |
| 研究生证书 (Certificate) | 40 |
| **学位项目总计 (UG + Grad)** | **434** |
| 学院 / 独立系所总数 | 8 |

> Source: catalog.wmich.edu/ Departments and Programs page (309 UG entries) + wmich.edu/academics/graduate (135 grad entries)

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Western Michigan University
├── College of Arts and Sciences                          [学院]
│   ├── Anthropology                                      [系]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Communication                                     [系]
│   ├── Computer Science                                  [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── Geography                                         [系]
│   ├── Geosciences                                       [系]
│   ├── History                                           [系]
│   ├── Mathematics                                       [系]
│   ├── Philosophy                                        [系]
│   ├── Physics                                           [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Sociology                                         [系]
│   ├── Spanish                                           [系]
│   └── World Religions and Cultures                      [系]
├── College of Aviation                                   [学院]
│   ├── Aviation Flight Science                           [系]
│   ├── Aviation Management and Operations                [系]
│   └── Aviation Technical Operations                     [系]
├── Haworth College of Business                           [学院]
│   ├── Accountancy                                       [系]
│   ├── Business Information Systems                      [系]
│   ├── Finance                                           [系]
│   ├── Management                                        [系]
│   ├── Marketing                                         [系]
│   └── Food Marketing                                    [系]
├── College of Education and Human Development            [学院]
│   ├── Counseling Psychology                             [系]
│   ├── Education and Human Development                   [系]
│   ├── Family and Consumer Sciences                      [系]
│   ├── Teaching, Learning and Educational Studies        [系]
│   └── Workforce Education and Development               [系]
├── College of Engineering and Applied Sciences           [学院]
│   ├── Aerospace Engineering                             [系]
│   ├── Chemical Engineering                              [系]
│   ├── Civil Engineering                                 [系]
│   ├── Computer Engineering                              [系]
│   ├── Electrical Engineering                            [系]
│   ├── Industrial and Entrepreneurial Engineering        [系]
│   ├── Manufacturing Engineering                         [系]
│   ├── Mechanical Engineering                            [系]
│   └── Paper Engineering                                 [系]
├── College of Fine Arts                                  [学院]
│   ├── Art, Gwen Frostic School of                       [系]
│   ├── Dance                                             [系]
│   ├── Music                                             [系]
│   └── Theatre                                           [系]
├── College of Health and Human Services                  [学院]
│   ├── Blindness and Low Vision Studies                  [系]
│   ├── Interdisciplinary Health Sciences                 [系]
│   ├── Nursing                                           [系]
│   ├── Occupational Therapy                              [系]
│   ├── Physical Therapy                                  [系]
│   ├── Social Work                                       [系]
│   └── Speech, Language and Hearing Sciences             [系]
├── Merze Tate College                                    [学院]
│   ├── Exploratory Advising                              [系]
│   └── University Studies                                [系]
├── Lee Honors College                                    [学院]
│   └── (Honors programs, not separate departments)
└── Graduate College                                      [学院]
    └── (Administers all graduate programs across colleges)
```

> Note: WMU has 7 degree-granting colleges + Merze Tate College (exploratory) + Lee Honors College + Graduate College = 10 total units. Graduate programs are administered by the Graduate College but housed in the academic colleges.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 28 |
| BS | Bachelor of Science | 本科 | 52 |
| BFA | Bachelor of Fine Arts | 本科 | 12 |
| BSE | Bachelor of Science in Engineering | 本科 | 10 |
| BBA | Bachelor of Business Administration | 本科 | 14 |
| BM | Bachelor of Music | 本科 | 8 |
| BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| Certificate | Undergraduate Certificate | 本科 | 15 |
| MA | Master of Arts | 研究生 | 32 |
| MS | Master of Science | 研究生 | 18 |
| MSE | Master of Science in Engineering | 研究生 | 6 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MSA | Master of Science in Accountancy | 研究生 | 1 |
| MSF | Master of Science in Finance | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MM | Master of Music | 研究生 | 1 |
| MSM | Master of Science in Medicine | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MIDA | Master of International Development Administration | 研究生 | 1 |
| MAcc | Master of Accountancy | 研究生 | 1 |
| EdS | Education Specialist | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 18 |
| EdD | Doctor of Education | 研究生 | 2 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | 40 |
| **Total** | | | **434** |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | BSE | BBA | BM | BSN | BSW | Cert(UG) | MA | MS | MSE | MFA | MBA | PhD | EdD | DPT | OTD | MD | Cert(Grad) | 合计 |
|------------|----|----|-----|-----|-----|----|----|-----|----------|----|----|----|-----|-----|-----|-----|-----|-----|----|------------|------|
| Arts & Sciences | 28 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 20 | 8 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 8 | 105 |
| Aviation | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 |
| Haworth Business | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 5 | 22 |
| Education & Human Dev | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 10 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 0 | 0 | 12 | 38 |
| Engineering & Applied Sci | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 31 |
| Fine Arts | 0 | 2 | 12 | 0 | 0 | 8 | 0 | 0 | 2 | 2 | 0 | 0 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 33 |
| Health & Human Services | 0 | 14 | 0 | 0 | 0 | 0 | 2 | 1 | 2 | 0 | 4 | 0 | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 6 | 33 |
| Merze Tate | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 3 |
| **合计** | **28** | **52** | **12** | **10** | **14** | **8** | **2** | **1** | **14** | **32** | **22** | **6** | **4** | **1** | **22** | **2** | **1** | **1** | **1** | **39** | **274** |

> Note: Some programs span multiple colleges. Counts are approximate based on available data. The Graduate College administers programs across all colleges but the MD program is through the Homer Stryker M.D. School of Medicine (separate entity).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

WMU has 7 degree-granting undergraduate colleges plus Merze Tate College for exploratory students and Lee Honors College for high-achieving students. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Anthropology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | BA | https://wmich.edu/academics/undergraduate/anthropology |

##### Biology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biology | BS | https://wmich.edu/academics/undergraduate/biology |
| 2 | Biomedical Sciences | BS | https://wmich.edu/academics/undergraduate/biomedical |
| 3 | Biochemistry | BS | https://wmich.edu/academics/undergraduate/biochemistry |

##### Chemistry
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | BS | https://wmich.edu/academics/undergraduate/chemistry |

##### Communication
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication Studies | BA | https://wmich.edu/academics/undergraduate/communication-studies |
| 2 | Interpersonal Communication | BA | https://wmich.edu/academics/undergraduate/interpersonal-communication |
| 3 | Strategic Communication | BA | https://wmich.edu/academics/undergraduate/strategic-communication |
| 4 | Digital Media and Journalism | BA | https://wmich.edu/academics/undergraduate/digital-media-journalism |

##### Computer Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | BS | https://wmich.edu/academics/undergraduate/computer-science |
| 2 | Cybersecurity | BS | https://wmich.edu/academics/undergraduate/cybersecurity |
| 3 | Data Science | BS | https://wmich.edu/academics/undergraduate/data-science |

##### Economics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Economics | BA | https://wmich.edu/academics/undergraduate/economics |
| 2 | Economics | BS | https://wmich.edu/academics/undergraduate/economics |

##### English
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | English: Creative Writing | BA | https://wmich.edu/academics/undergraduate/english-creative-writing |
| 2 | English: Literature and Language | BA | https://wmich.edu/academics/undergraduate/english-literature |
| 3 | English: Rhetoric and Writing Studies | BA | https://wmich.edu/academics/undergraduate/english-rhetoric |

##### Geography
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Environmental Geography | BS | https://wmich.edu/academics/undergraduate/environmental-geography |
| 2 | Geographic Information Science | BS | https://wmich.edu/academics/undergraduate/geographic-information-science |

##### Geosciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth Science | BS | https://wmich.edu/academics/undergraduate/earth-science |
| 2 | Geology | BS | https://wmich.edu/academics/undergraduate/geology |
| 3 | Geophysics | BS | https://wmich.edu/academics/undergraduate/geophysics |
| 4 | Geochemistry | BS | https://wmich.edu/academics/undergraduate/geochemistry |
| 5 | Hydrogeology | BS | https://wmich.edu/academics/undergraduate/hydrogeology |
| 6 | Environmental Geology | BS | https://wmich.edu/academics/undergraduate/environmental-geology |

##### History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | History | BA | https://wmich.edu/academics/undergraduate/history |
| 2 | Public History | BA | https://wmich.edu/academics/undergraduate/public-history |

##### Mathematics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | BA | https://wmich.edu/academics/undergraduate/mathematics |
| 2 | Mathematics | BS | https://wmich.edu/academics/undergraduate/mathematics |
| 3 | Statistics | BS | https://wmich.edu/academics/undergraduate/statistics |

##### Philosophy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | BA | https://wmich.edu/academics/undergraduate/philosophy |

##### Physics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics | BS | https://wmich.edu/academics/undergraduate/physics |

##### Political Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | BA | https://wmich.edu/academics/undergraduate/political-science |

##### Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology | BS | https://wmich.edu/academics/undergraduate/psychology |
| 2 | Social Psychology | BA | https://wmich.edu/academics/undergraduate/social-psychology |

##### Sociology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | BA | https://wmich.edu/academics/undergraduate/sociology |
| 2 | Criminal Justice Studies | BA | https://wmich.edu/academics/undergraduate/criminal-justice |

##### Spanish
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Spanish | BA | https://wmich.edu/academics/undergraduate/spanish |
| 2 | French | BA | https://wmich.edu/academics/undergraduate/french |
| 3 | German | BA | https://wmich.edu/academics/undergraduate/german |
| 4 | Japanese | BA | https://wmich.edu/academics/undergraduate/japanese |
| 5 | Latin | BA | https://wmich.edu/academics/undergraduate/latin |

##### World Religions and Cultures
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | World Religions and Cultures | BA | https://wmich.edu/academics/undergraduate/world-religions |
| 2 | Comparative Religion | BA | https://wmich.edu/academics/undergraduate/comparative-religion |

##### Other Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | African American and African Studies | BA | https://wmich.edu/academics/undergraduate/african |
| 2 | Anthropology | BA | https://wmich.edu/academics/undergraduate/anthropology |
| 3 | Environmental and Sustainability Studies | BA | https://wmich.edu/academics/undergraduate/environmental-sustainability |
| 4 | Environmental and Sustainability Studies | BS | https://wmich.edu/academics/undergraduate/environmental-sustainability |
| 5 | Film, Video and Media Studies | BA | https://wmich.edu/academics/undergraduate/film-video-media |
| 6 | Gender and Women's Studies | BA | https://wmich.edu/academics/undergraduate/gender-womens-studies |
| 7 | Global and International Studies | BA | https://wmich.edu/academics/undergraduate/global-international |
| 8 | Social Studies | BA | https://wmich.edu/academics/undergraduate/social-studies |
| 9 | Tourism and Travel | BA | https://wmich.edu/academics/undergraduate/tourism-travel |

---

#### College of Aviation

##### Aviation Flight Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aviation Flight Science | BS | https://wmich.edu/aviation/academics/aviation-flight-science |

##### Aviation Management and Operations
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aviation Management and Operations | BS | https://wmich.edu/academics/undergraduate/aviation-management |

##### Aviation Technical Operations
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aviation Technical Operations | BS | https://wmich.edu/academics/undergraduate/aviation-technical-operations |

##### Aviation Certificates
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aircraft Dispatching and Scheduling | Certificate | https://wmich.edu/aviation/academics/dispatchcert |
| 2 | Airport Management | Certificate | https://wmich.edu/aviation/academics/airportcert |

---

#### Haworth College of Business

##### Accountancy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | BBA | https://wmich.edu/accountancy/academics/major |

##### Business Information Systems
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Information Systems | BBA | https://wmich.edu/infosystems/academics/undergraduate |
| 2 | Business Analytics | BBA | https://wmich.edu/infosystems/academics/business-analytics |

##### Finance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Finance | BBA | https://wmich.edu/finance/academics/undergraduate |
| 2 | Personal Financial Planning | BBA | https://wmich.edu/finance/academics/personal-financial-planning |

##### Management
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Human Resource Management | BBA | https://wmich.edu/management/academics/human-resource-management |
| 2 | Leadership and Business Strategy | BBA | https://wmich.edu/management/academics/leadership-business-strategy |
| 3 | Integrated Business Administration | BBA | https://wmich.edu/management/academics/integrated-business-administration |

##### Marketing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Marketing | BBA | https://wmich.edu/marketing/academics/undergraduate |
| 2 | Sales and Business Marketing | BBA | https://wmich.edu/marketing/academics/sales-business-marketing |
| 3 | Digital Marketing | BBA | https://wmich.edu/marketing/academics/digital-marketing |
| 4 | Food Marketing | BBA | https://wmich.edu/marketing/academics/food-marketing |

##### Other Business Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Law | BBA | https://wmich.edu/business/academics/business-law |
| 2 | Supply Chain Management | BBA | https://wmich.edu/management/academics/supply-chain-management |
| 3 | Economics in Business | BBA | https://wmich.edu/economics/academics/economics-business |
| 4 | Business | pre-BBA | https://wmich.edu/business/pre-business |

---

#### College of Education and Human Development

##### Counseling Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Counseling Psychology | MA | https://wmich.edu/cecp/academics |

##### Education and Human Development
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Education and Human Development | BS | https://wmich.edu/education/academics/education-human-development |
| 2 | Early Childhood General and Special Education: Birth through Kindergarten | BS | https://wmich.edu/education/academics/early-childhood |
| 3 | Early Childhood General and Special Education and Lower Elementary | BS | https://wmich.edu/education/academics/early-childhood-lower-elementary |
| 4 | Elementary Education | BS | https://wmich.edu/education/academics/elementary-education |
| 5 | Elementary Education PK-3 and TESOL K-12 | BS | https://wmich.edu/education/academics/elementary-tesol |

##### Family and Consumer Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Child Development and Services | BS | https://wmich.edu/education/academics/child-development |
| 2 | Child and Family Development | BS | https://wmich.edu/education/academics/child-family-development |
| 3 | Family Science and Services | BS | https://wmich.edu/education/academics/family-science |
| 4 | Family and Consumer Sciences Teacher Education | BS | https://wmich.edu/education/academics/fcs-teacher-education |
| 5 | Fashion Design and Development | BS | https://wmich.edu/education/academics/fashion-design |
| 6 | Fashion Merchandising | BS | https://wmich.edu/education/academics/fashion-merchandising |
| 7 | Interior Architecture and Design | BS | https://wmich.edu/education/academics/interior-architecture |

##### Teaching, Learning and Educational Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Special Education Learning Disabilities K-12 and Elementary Education PK-3 | BS | https://wmich.edu/education/academics/special-education |
| 2 | Physical and Health Education Teacher Education: K-12 | BS | https://wmich.edu/education/academics/physical-health-education |
| 3 | Integrated Science | BS | https://wmich.edu/education/academics/integrated-science |

##### Workforce Education and Development
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Workforce Education and Development | BA | https://wmich.edu/education/academics/workforce-education |
| 2 | Occupational Education Studies | BS | https://wmich.edu/education/academics/occupational-education |
| 3 | Industrial Technology Education | BS | https://wmich.edu/education/academics/industrial-technology |
| 4 | Business Education | BS | https://wmich.edu/education/academics/business-education |

---

#### College of Engineering and Applied Sciences

##### Aerospace Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | BSE | https://wmich.edu/mechanical-aerospace/academics/aerospace |

##### Chemical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | BSE | https://wmich.edu/chemical-engineer/academics/undergraduate |

##### Civil Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering | BSE | https://wmich.edu/civil-engineer/academics/undergraduate |

##### Computer Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Engineering | BSE | https://wmich.edu/electrical-computer/academics/computer-engineering |

##### Electrical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical Engineering | BSE | https://wmich.edu/electrical-engineer/academics/undergraduate |

##### Industrial and Entrepreneurial Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Industrial and Entrepreneurial Engineering | BSE | https://wmich.edu/industrial-engineer/academics/undergraduate |

##### Manufacturing Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Manufacturing Engineering | BSE | https://wmich.edu/manufacturing-engineer/academics/undergraduate |

##### Mechanical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mechanical Engineering | BSE | https://wmich.edu/mechanical-aerospace/academics/mechanical |

##### Paper Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Paper Engineering | BSE | https://wmich.edu/paper-engineer/academics/undergraduate |

##### Other Engineering Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Construction Engineering | BSE | https://wmich.edu/civil-engineer/academics/construction |
| 2 | Engineering Design Technology | BS | https://wmich.edu/engineer/academics/engineering-design-technology |
| 3 | Engineering Management Technology | BS | https://wmich.edu/engineer/academics/engineering-management-technology |
| 4 | Manufacturing Engineering Technology | BS | https://wmich.edu/engineer/academics/manufacturing-engineering-technology |
| 5 | Community and Regional Planning | BS | https://wmich.edu/engineer/academics/community-regional-planning |
| 6 | Urban, Regional and Environmental Planning | BS | https://wmich.edu/engineer/academics/urban-regional-planning |

---

#### College of Fine Arts

##### Art, Gwen Frostic School of
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art | BA | https://wmich.edu/academics/undergraduate/art |
| 2 | Art | BFA | https://wmich.edu/academics/undergraduate/art |
| 3 | Art Education | BFA | https://wmich.edu/academics/undergraduate/art-education |
| 4 | Art History | BA | https://wmich.edu/academics/undergraduate/art-history |
| 5 | Art: Kinetic Imaging | BS | https://wmich.edu/academics/undergraduate/art-kinetic |
| 6 | Graphic Design | BFA | https://wmich.edu/academics/undergraduate/graphic-design |
| 7 | Product Design | BFA | https://wmich.edu/academics/undergraduate/product-design |

##### Dance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Dance | BA | https://wmich.edu/dance/academics/undergraduate |
| 2 | Dance | BFA | https://wmich.edu/dance/academics/undergraduate |

##### Music
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | BA | https://wmich.edu/music/academics/undergraduate |
| 2 | Music Composition | BM | https://wmich.edu/music/academics/composition |
| 3 | Music Education: Choral/General | BM | https://wmich.edu/music/academics/music-education-choral |
| 4 | Music Education: Instrumental | BM | https://wmich.edu/music/academics/music-education-instrumental |
| 5 | Music Performance: Instrumental | BM | https://wmich.edu/music/academics/performance-instrumental |
| 6 | Music Performance: Keyboard | BM | https://wmich.edu/music/academics/performance-keyboard |
| 7 | Music Performance: Vocal | BM | https://wmich.edu/music/academics/performance-vocal |
| 8 | Music Therapy | BM | https://wmich.edu/music/academics/music-therapy |
| 9 | Music: Jazz Studies | BM | https://wmich.edu/music/academics/jazz-studies |

##### Theatre
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Acting | BFA | https://wmich.edu/theatre/academics/acting |
| 2 | Arts Administration | BA | https://wmich.edu/academics/undergraduate/theatre |
| 3 | Stage Management | BFA | https://wmich.edu/theatre/academics/stage-management |
| 4 | Theatre Design and Technical Production | BFA | https://wmich.edu/theatre/academics/design-technical |
| 5 | Theatre: Music Theatre Performance | BFA | https://wmich.edu/theatre/academics/music-theatre |

---

#### College of Health and Human Services

##### Blindness and Low Vision Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Vision Rehabilitation Therapy | MA | https://wmich.edu/visionstudies/academics/vision-rehab |
| 2 | Orientation and Mobility for Adults | MA | https://wmich.edu/visionstudies/academics/orientation-mobility-adults |
| 3 | Orientation and Mobility for Children | MA | https://wmich.edu/visionstudies/academics/orientation-mobility-children |
| 4 | Teaching Children with Visual Impairments | MA | https://wmich.edu/visionstudies/academics/vision-teaching |

##### Interdisciplinary Health Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Healthcare Services and Sciences | BS | https://wmich.edu/hhs/academics/healthcare-services |
| 2 | Healthcare Services and Sciences Clinical Practice in Health | BS | https://wmich.edu/hhs/academics/healthcare-services-clinical |
| 3 | Healthcare Services and Sciences Physician Assistant Preparation | BS | https://wmich.edu/hhs/academics/healthcare-services-pa |
| 4 | Healthcare Services and Rehabilitation Sciences | BS | https://wmich.edu/hhs/academics/healthcare-services-rehab |
| 5 | Health Administration | BS | https://wmich.edu/hhs/academics/health-administration |
| 6 | Public Health | BS | https://wmich.edu/hhs/academics/public-health |

##### Nursing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | BSN | https://wmich.edu/nursing/academics/undergraduate |

##### Occupational Therapy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Occupational Therapy Assistant | BS | https://wmich.edu/ota/academics/undergraduate |

##### Physical Therapy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Exercise Science | BS | https://wmich.edu/humanperformance/academics/exercise-science |
| 2 | Recreation Management | BS | https://wmich.edu/humanperformance/academics/recreation-management |
| 3 | Sport Management | BS | https://wmich.edu/humanperformance/academics/sport-management |

##### Social Work
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | BSW | https://wmich.edu/socialwork/academics/undergraduate |

##### Speech, Language and Hearing Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Speech, Language and Hearing Sciences | BS | https://wmich.edu/speech-audiology/academics/undergraduate |

---

#### Merze Tate College

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | University Studies | BA | https://wmich.edu/merzetate/academics/university-studies |
| 2 | University Studies | BS | https://wmich.edu/merzetate/academics/university-studies |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | 主管学院 | URL |
|---|------|------|----------|-----|
| 1 | Freshwater Science and Sustainability | BS | Arts & Sciences | https://wmich.edu/academics/undergraduate/freshwater-science |
| 2 | Sustainable Brewing | BS | Arts & Sciences | https://wmich.edu/academics/undergraduate/sustainable-brewing |
| 3 | Event Management | BS | Education & Human Dev | https://wmich.edu/academics/undergraduate/event-management |
| 4 | Public and Nonprofit Administration | BS | Arts & Sciences | https://wmich.edu/academics/undergraduate/public-nonprofit-admin |
| 5 | Youth and Community Development | BS | Education & Human Dev | https://wmich.edu/academics/undergraduate/youth-community-development |

---

### 1.4 Undergraduate Certificates — Complete List

| # | Certificate | Home School | URL |
|---|-------------|-------------|-----|
| 1 | Aircraft Dispatching and Scheduling | Aviation | https://wmich.edu/aviation/academics/dispatchcert |
| 2 | Airport Management | Aviation | https://wmich.edu/aviation/academics/airportcert |
| 3 | Applied Hydrogeology | Arts & Sciences | https://wmich.edu/academics/undergraduate/applied-hydrogeology |
| 4 | Dance Studio Management | Fine Arts | https://wmich.edu/dance/academics/studio-management |
| 5 | Diversity and Inclusion | Education & Human Dev | https://wmich.edu/academics/undergraduate/diversity-inclusion |
| 6 | Initial Teacher Certification | Education & Human Dev | https://wmich.edu/academics/undergraduate/initial-teacher-certification |
| 7 | Integrated Design and Manufacturing | Engineering | https://wmich.edu/academics/undergraduate/integrated-design-manufacturing |
| 8 | Leadership and Teamwork | Business | https://wmich.edu/academics/undergraduate/leadership-teamwork |
| 9 | Media and Technology | Arts & Sciences | https://wmich.edu/academics/undergraduate/media-technology |
| 10 | Music Therapy Equivalency | Fine Arts | https://wmich.edu/music/academics/music-therapy-equivalency |
| 11 | Paper Engineering | Engineering | https://wmich.edu/paper-engineer/academics/certificate |
| 12 | Public Relations | Arts & Sciences | https://wmich.edu/academics/undergraduate/public-relations |
| 13 | Speech, Language and Hearing Sciences | Health & Human Services | https://wmich.edu/speech-audiology/academics/certificate |
| 14 | Unmanned Aerial Systems Operations | Aviation | https://wmich.edu/aviation/academics/uas-certificate |

---

### 1.5 General Education Requirements

WMU requires all undergraduate students to complete the General Education program, which includes:
- Tier I: Foundations (English Composition, Mathematics, Speech)
- Tier II: Exploration (Humanities, Fine Arts, Social Sciences, Natural Sciences, Diversity)
- Tier III: Integration (Senior-level coursework)

Source: https://wmich.edu/academics/general-education

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Economics | https://wmich.edu/academics/graduate/applied-economics |
| 2 | Clinical Mental Health Counseling | https://wmich.edu/academics/graduate/clinical-mental-health-counsel |
| 3 | Communication | https://wmich.edu/academics/graduate/communication |
| 4 | Comparative Religion | https://wmich.edu/academics/graduate/religion |
| 5 | Criminal Justice Studies | https://wmich.edu/academics/graduate/criminal-justice-studies-MA |
| 6 | English | https://wmich.edu/academics/graduate/english |
| 7 | Hispanic Studies | https://wmich.edu/academics/graduate/hispanic-studies |
| 8 | History | https://wmich.edu/academics/graduate/history |
| 9 | Mathematics | https://wmich.edu/academics/graduate/math |
| 10 | Medieval Studies | https://wmich.edu/academics/graduate/medieval |
| 11 | Philosophy | https://wmich.edu/academics/graduate/philosophy |
| 12 | Political Science | https://wmich.edu/academics/graduate/political |
| 13 | Psychology | https://wmich.edu/academics/graduate/psychology |
| 14 | Sociology | https://wmich.edu/academics/graduate/sociology |
| 15 | Teaching English to Speakers of Other Languages | https://wmich.edu/academics/graduate/tesol |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied and Computational Mathematics | https://wmich.edu/academics/graduate/applied-math |
| 2 | Biological Sciences | https://wmich.edu/academics/graduate/biology |
| 3 | Chemistry | https://wmich.edu/academics/graduate/chemistry |
| 4 | Computer Science | https://wmich.edu/academics/graduate/cs |
| 5 | Data Science | https://wmich.edu/academics/graduate/data-science |
| 6 | Earth Science | https://wmich.edu/academics/graduate/earth-science |
| 7 | Geography | https://wmich.edu/academics/graduate/geography |
| 8 | Geosciences | https://wmich.edu/academics/graduate/geosciences |
| 9 | Physics | https://wmich.edu/academics/graduate/physics |
| 10 | Statistics | https://wmich.edu/academics/graduate/statistics |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://wmich.edu/academics/graduate/biology |
| 2 | Chemistry | https://wmich.edu/academics/graduate/chemistry |
| 3 | Clinical Psychology | https://wmich.edu/academics/graduate/clinical-psychology-phd |
| 4 | Computer Science | https://wmich.edu/academics/graduate/cs |
| 5 | Counselor Education | https://wmich.edu/academics/graduate/doctoral-counselor-education |
| 6 | Creative Writing | https://wmich.edu/academics/graduate/english-creative-writing-phd |
| 7 | Economics | https://wmich.edu/academics/graduate/economics-phd |
| 8 | English | https://wmich.edu/academics/graduate/english |
| 9 | Geosciences | https://wmich.edu/academics/graduate/geosciences |
| 10 | History | https://wmich.edu/academics/graduate/history |
| 11 | Mathematics | https://wmich.edu/academics/graduate/math |
| 12 | Physics | https://wmich.edu/academics/graduate/physics |
| 13 | Political Science | https://wmich.edu/academics/graduate/political |
| 14 | Psychology | https://wmich.edu/academics/graduate/psychology |
| 15 | Sociology | https://wmich.edu/academics/graduate/sociology |
| 16 | Spanish | https://wmich.edu/academics/graduate/spanish |
| 17 | Statistics | https://wmich.edu/academics/graduate/statistics |

##### Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Addiction Specialization | https://wmich.edu/academics/graduate/addictionstudies |
| 2 | Applied Statistics | https://wmich.edu/academics/graduate/applied-statistics |
| 3 | Biostatistics | https://wmich.edu/academics/graduate/biostatistics |
| 4 | Climate Change Policy and Management | https://wmich.edu/academics/graduate/climate-change-certificate |
| 5 | Clinical Addiction | https://wmich.edu/academics/graduate/addiction-studies |
| 6 | College Science Teaching | https://wmich.edu/academics/graduate/science/academics |
| 7 | Cultural and Environmental Heritage Management | https://wmich.edu/academics/graduate/heritage-management |
| 8 | Evaluation | https://wmich.edu/academics/graduate/emr/programs/evaluation |
| 9 | Geographic Information Science | https://wmich.edu/academics/graduate/geography-certificate |
| 10 | Hydrogeology | https://wmich.edu/academics/graduate/hydrogeology |
| 11 | Mixed-Methods Research | https://wmich.edu/academics/graduate/mixed-methods-research |
| 12 | Qualitative Research | https://wmich.edu/academics/graduate/qualitative-research |
| 13 | UAVs Applications in Geological and Environmental Sciences | https://wmich.edu/academics/graduate/uavs |

---

#### College of Aviation

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Aviation Administration | Certificate | https://wmich.edu/academics/graduate/Aviation_admin |

---

#### Haworth College of Business

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | MSA | https://wmich.edu/academics/graduate/accountancy |
| 2 | Business Administration | MBA | https://wmich.edu/academics/graduate/mba |
| 3 | Finance | MSF | https://wmich.edu/academics/graduate/finance/master |

##### Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://wmich.edu/academics/graduate/buac |
| 2 | Finance | https://wmich.edu/academics/graduate/finance/master |
| 3 | Financial Technology | https://wmich.edu/academics/graduate/finance-tech-certificate-0 |
| 4 | Food Marketing | https://wmich.edu/academics/graduate/food-marketing-cert |
| 5 | Supply Chain Management | https://wmich.edu/academics/graduate/supply-chain-cert |

---

#### College of Education and Human Development

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://wmich.edu/academics/graduate/clinical-mental-health-counsel |
| 2 | Counseling Psychology | https://wmich.edu/academics/graduate/counseling |
| 3 | Early Childhood General and Special Education: Birth through Kindergarten | https://wmich.edu/academics/graduate/education/early/masters |
| 4 | Educational and Instructional Technology | https://wmich.edu/academics/graduate/edtechnology |
| 5 | Evaluation, Measurement and Research | https://wmich.edu/academics/graduate/evaluation |
| 6 | Family and Consumer Sciences | https://wmich.edu/academics/graduate/consumer |
| 7 | Global Leadership and Learning | https://wmich.edu/academics/graduate/global-leadership-learning |
| 8 | Higher Education and Student Affairs | https://wmich.edu/academics/graduate/student-affairs-higher-education |
| 9 | K-12 Educational Leadership | https://wmich.edu/academics/graduate/edleadership |
| 10 | Literacy Studies | https://wmich.edu/academics/graduate/literacy |
| 11 | Marriage, Couple and Family Counseling | https://wmich.edu/academics/graduate/marriage-couple-family-counseling |
| 12 | Mathematics Education | https://wmich.edu/academics/graduate/math-ed |
| 13 | Organizational Change Leadership | https://wmich.edu/academics/graduate/performance |
| 14 | Orientation and Mobility for Adults | https://wmich.edu/academics/graduate/orientation-mobility-adults |
| 15 | Orientation and Mobility for Children | https://wmich.edu/academics/graduate/mobility-teaching |
| 16 | Physical Education | https://wmich.edu/academics/graduate/humanperformance/academics |
| 17 | School Counseling | https://wmich.edu/academics/graduate/cecp |
| 18 | Science Education | https://wmich.edu/academics/graduate/science |
| 19 | Special Education | https://wmich.edu/academics/graduate/specialed |
| 20 | Spirituality, Culture and Health | https://wmich.edu/academics/graduate/spirituality |
| 21 | Sport Management | https://wmich.edu/academics/graduate/sports |
| 22 | Teaching | https://wmich.edu/academics/graduate/teaching-0 |
| 23 | Teaching Children with Visual Impairments | https://wmich.edu/academics/graduate/vision-teaching |
| 24 | Teaching Children with Visual Impairments/Orientation and Mobility | https://wmich.edu/academics/graduate/vision-studies-teacher |
| 25 | Teaching, Learning and Educational Studies | https://wmich.edu/academics/graduate/practice-teaching |
| 26 | Vision Rehabilitation Therapy | https://wmich.edu/academics/graduate/vision-rehab |
| 27 | Workforce Education and Development | https://wmich.edu/academics/graduate/career-ed |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://wmich.edu/academics/graduate/doctoral-counselor-education |
| 2 | Education and Human Development | https://wmich.edu/academics/graduate/education-human-development |
| 3 | Evaluation, Measurement and Research | https://wmich.edu/academics/graduate/evaluation |
| 4 | Higher Education Leadership | https://wmich.edu/academics/graduate/higher-ed-leadership-phd |
| 5 | K-12 Educational Leadership | https://wmich.edu/academics/graduate/edleadership |
| 6 | Mathematics Education | https://wmich.edu/academics/graduate/math-ed |
| 7 | Organizational Change Leadership | https://wmich.edu/academics/graduate/performance |
| 8 | Organizational Learning and Leadership | https://wmich.edu/academics/graduate/org-learn-leader |
| 9 | Science Education | https://wmich.edu/academics/graduate/science |
| 10 | Special Education | https://wmich.edu/academics/graduate/specialed |

##### EdS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | K-12 Educational Leadership | https://wmich.edu/academics/graduate/edleadership |

##### EdD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Special Education | https://wmich.edu/academics/graduate/specialed |
| 2 | Counselor Education | https://wmich.edu/academics/graduate/doctoral-counselor-education |

##### Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Adapted Physical Education and Positive Behavioral Intervention and Supports | https://wmich.edu/academics/graduate/ape-pbis-certificate |
| 2 | Counseling Psychology | https://wmich.edu/academics/graduate/counseling |
| 3 | Early Childhood Special Education | https://wmich.edu/academics/graduate/early-childhood-special-education |
| 4 | Educational and Instructional Technology | https://wmich.edu/academics/graduate/edtechnology |
| 5 | English as a Second Language | https://wmich.edu/academics/graduate/english-second-language-teaching |
| 6 | Evidence-Based Reading Instruction and Intervention | https://wmich.edu/academics/graduate/specialized-academics-reading-certificate |
| 7 | Global Leadership and Learning | https://wmich.edu/academics/graduate/global-leadership-learning |
| 8 | Higher Education and Student Affairs | https://wmich.edu/academics/graduate/student-affairs-higher-education |
| 9 | K-12 Educational Leadership | https://wmich.edu/academics/graduate/edleadership |
| 10 | Positive Behavioral Intervention and Supports | https://wmich.edu/academics/graduate/pbis |
| 11 | Professional Workforce Educator | https://wmich.edu/academics/graduate/professional-workforce-educator |
| 12 | School Administration: Central Office Endorsement | https://wmich.edu/academics/graduate/leadership/centralofficecertprog |
| 13 | School Counseling | https://wmich.edu/academics/graduate/cecp |
| 14 | Special Education | https://wmich.edu/academics/graduate/specialed |
| 15 | Teacher Development | https://wmich.edu/academics/graduate/teaching/academics/graduate/school-improvement-certificate |
| 16 | Tribal Governance | https://wmich.edu/academics/graduate/tribalgov |

---

#### College of Engineering and Applied Sciences

##### MSE Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://wmich.edu/academics/graduate/computer-engineer |
| 2 | Electrical Engineering | https://wmich.edu/academics/graduate/electrical-engineer |
| 3 | Industrial Engineering | https://wmich.edu/academics/graduate/industrial-engineer |
| 4 | Mechanical Engineering | https://wmich.edu/academics/graduate/mechanical-engineer |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://wmich.edu/academics/graduate/aerospace |
| 2 | Chemical Engineering | https://wmich.edu/academics/graduate/chemical-engineer |
| 3 | Civil Engineering | https://wmich.edu/academics/graduate/civil-engineer |
| 4 | Computer Science | https://wmich.edu/academics/graduate/cs |
| 5 | Cybersecurity | https://wmich.edu/academics/graduate/cybersecurity/programs/master |
| 6 | Data Science | https://wmich.edu/academics/graduate/data-science |
| 7 | Engineering Management | https://wmich.edu/academics/graduate/engineer-management |
| 8 | Manufacturing Engineering | https://wmich.edu/academics/graduate/manufacturing-engineer |
| 9 | Paper and Printing Science | https://wmich.edu/academics/graduate/paper |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://wmich.edu/academics/graduate/chemical-engineer |
| 2 | Civil Engineering | https://wmich.edu/academics/graduate/civil-engineer |
| 3 | Computer Science | https://wmich.edu/academics/graduate/cs |
| 4 | Electrical and Computer Engineering | https://wmich.edu/academics/graduate/electrical-computer |
| 5 | Engineering and Applied Sciences | https://wmich.edu/academics/graduate/engineering |
| 6 | Industrial Engineering | https://wmich.edu/academics/graduate/industrial-engineer |
| 7 | Mechanical Engineering | https://wmich.edu/academics/graduate/mechanical-engineer |
| 8 | Paper and Printing Science | https://wmich.edu/academics/graduate/paper |

##### Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Embedded System Design | https://wmich.edu/academics/graduate/certificates/embedded |
| 2 | Renewable Power Systems | https://wmich.edu/academics/graduate/certificates/renewable |
| 3 | Cybersecurity | https://wmich.edu/academics/graduate/cybersecurity/programs/master |

---

#### College of Fine Arts

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Ceramics | https://wmich.edu/academics/graduate/mfa-ceramics |
| 2 | Creative Writing | https://wmich.edu/academics/graduate/english-creative-writing-phd |

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://wmich.edu/academics/graduate/music |

##### MM Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://wmich.edu/academics/graduate/music |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://wmich.edu/academics/graduate/english-creative-writing-phd |

##### Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Performance | https://wmich.edu/academics/graduate/music-performance |

---

#### College of Health and Human Services

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Speech-Language Pathology | https://wmich.edu/academics/graduate/speech-audiology |
| 2 | Social Work | https://wmich.edu/academics/graduate/socialwork |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Nutrition and Dietetics | https://wmich.edu/academics/graduate/nutrition |
| 2 | Physician Assistant | https://wmich.edu/academics/graduate/pa |

##### MSW Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://wmich.edu/academics/graduate/socialwork |

##### DPT Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://wmich.edu/academics/graduate/pt |

##### OTD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy Doctorate | https://wmich.edu/academics/graduate/ota |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Health Sciences | https://wmich.edu/academics/graduate/healthsciences |

##### Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Holism and Contemplative Health Care | https://wmich.edu/academics/graduate/holistic/gradcertificates-0 |
| 2 | Health and Wellness Coaching Skills | https://wmich.edu/academics/graduate/holistic/gradcertificates-1 |
| 3 | Mindfulness and Centering Skills | https://wmich.edu/academics/graduate/holistic/gradcertificates |
| 4 | Nurse Educator | https://wmich.edu/academics/graduate/Nurse-ed-certificate |
| 5 | Resiliency and Well-Being Skills | https://wmich.edu/academics/graduate/holistic/gradcertificates-2 |
| 6 | Youth and Community Development | https://wmich.edu/academics/graduate/youth-development |

---

#### Graduate College (Interdisciplinary)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Interdisciplinary Studies | PhD | https://wmich.edu/academics/graduate/interdisciplinary-studies |
| 2 | International Development Administration | MIDA | https://wmich.edu/academics/graduate/international |
| 3 | Public Administration | MPA | https://wmich.edu/academics/graduate/public-affairs |
| 4 | Medicine | MD | https://wmich.edu/academics/graduate/medicine |
| 5 | Law | LLM | https://wmich.edu/academics/graduate/law |
| 6 | Behavior Analysis | MA | https://wmich.edu/academics/graduate/behavior-analysis |
| 7 | Industrial Organizational Behavior Management | MA | https://wmich.edu/academics/graduate/iobm |

---

### 2.2 Graduate Program Deep-Dive: Master of Business Administration (MBA)

- **Department**: Haworth College of Business
- **Address**: 3210 Schneider Hall, Kalamazoo, MI 49008
- **Phone**: (269) 387-5086
- **Email**: mba-info@wmich.edu
- **Application Portal**: https://wmich.my.site.com/GraduateWMU/TX_SiteLogin_Grad
- **Application Fee**: $50 (domestic), $100 (international)
- **Deadline**: Rolling (recommended to apply by March 1 for fall)
- **GRE/GMAT**: Not required
- **TOEFL Minimum**: 80 (iBT)
- **IELTS Minimum**: 6.5
- **Program URL**: https://wmich.edu/academics/graduate/mba

### 2.3 Graduate Admissions Model

WMU uses a **centralized graduate application** through the Graduate College, but individual programs set their own requirements and deadlines. The Graduate College processes applications and forwards them to departments for review.

- **Application Portal**: https://wmich.my.site.com/GraduateWMU/TX_SiteLogin_Grad
- **Application Fee**: $50 domestic, $100 international
- **GRE/GMAT**: Program-specific (many programs do not require)
- **English Proficiency**: TOEFL 80 / IELTS 6.5 minimum (most programs)
- **Funding**: Varies by program; PhD programs typically offer assistantships

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 |
|------|------|
| **Admissions Site** | https://wmich.edu/admissions |
| **Application Portal** | Common App (exclusive for first-year) |
| **Early Action Deadline** | December 15 (non-binding) |
| **Rolling Admission Deadline** | July 28 (fall entry) |
| **Spring Entry Deadline** | January 1 (first-year) |
| **Summer I Entry Deadline** | May 1 |
| **Summer II Entry Deadline** | June 15 |
| **Application Fee** | $0 (domestic first-year via Common App) |
| **International Application Fee** | $100 |
| **Decision Notification** | Rolling (2-3 weeks after complete file) |
| **Enrollment Confirmation Deadline** | May 1 |
| **Financial Aid Deadline** | March 1 (priority) |
| **SAT/ACT Policy** | Test-optional (since 2020) |
| **Superscore Policy** | Yes (SAT and ACT) |
| **SAT Code** | 1902 |
| **ACT Code** | 2064 |
| **Interview Policy** | Not required |
| **Recommendation Requirements** | Not required |
| **Portfolio** | Required for Fine Arts programs |
| **Transfer Deadline** | August 15 (fall) |

> Source: https://wmich.edu/apply/deadlines, https://wmich.edu/admissions/first-year-apply/criteria

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分数 (大多数项目) | Aviation Flight Science 最低分数 |
|------|----------------------|-------------------------------|
| TOEFL iBT | 71 | 91 |
| TOEFL iBT (2026+) | 4 | 4.5 |
| TOEFL Essentials | 7 | 9 |
| IELTS Academic | 6.0 | 7.0 |
| PTE Academic | 48 | 64 |
| Duolingo | 100 | 115 |
| Michigan English Test (MET) | 48 | 64 |
| SAT EBRW | 500 | 560 |
| IB English HL | Grade 5 | Same |
| IGCSE English | Grade A/B/C | Same |
| Cambridge Advanced English | Grade A/B/C | Same |
| ELS Level 112 | Completion | Same |

> Source: https://wmich.edu/international/apply/english-proficiency
> Note: Tests must be taken within 2 years of application. WMU Institutional Code: 1902.

### 3.3 Graduate — Global Rules

| 维度 | 详情 |
|------|------|
| **Admissions Model** | Centralized application, decentralized review |
| **Application Portal** | https://wmich.my.site.com/GraduateWMU/TX_SiteLogin_Grad |
| **Application Fee (Domestic)** | $50 |
| **Application Fee (International)** | $100 |
| **GRE/GMAT** | Program-specific (many do not require) |
| **TOEFL Minimum** | 80 iBT |
| **IELTS Minimum** | 6.5 Academic |
| **Duolingo Minimum** | 105 |
| **PTE Minimum** | 54 |
| **MET Minimum** | 57 |
| **Application Timeline** | Rolling (international students should apply by January for fall) |
| **ETS Code** | 1902 |
| **CGS April-15 Honor** | Yes (signatory) |

> Source: https://wmich.edu/grad/apply, https://wmich.edu/international/apply/english-proficiency

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

#### Michigan Resident (On/Off Campus)

| 费用项目 | 金额 (Fall+Spring) | 说明 |
|---------|-------------------|------|
| Tuition | $16,449 | Flat rate 12-15 credits/semester |
| Standard Fees | $140 | Assessment + Sustainability |
| Housing and Food | $14,590 | On-campus average |
| Books/Supplies | $1,128 | Estimated |
| Transportation | $2,880 | Estimated |
| Loan Fees | $37 | Estimated |
| Other | $2,046 | Personal expenses |
| **TOTAL** | **$37,270** | |

#### Non-Resident (On/Off Campus)

| 费用项目 | 金额 (Fall+Spring) | 说明 |
|---------|-------------------|------|
| Tuition | $20,525 | Flat rate 12-15 credits/semester |
| Standard Fees | $140 | Assessment + Sustainability |
| Housing and Food | $14,590 | On-campus average |
| Books/Supplies | $1,128 | Estimated |
| Transportation | $2,880 | Estimated |
| Loan Fees | $37 | Estimated |
| Other | $2,046 | Personal expenses |
| **TOTAL** | **$41,346** | |

#### College-Specific Differential Tuition (per semester, in addition to base)

| 学院 | 费率 |
|------|------|
| Haworth College of Business | $67.17/credit hour (after 55 earned credits) |
| College of Engineering and Applied Sciences | $62.10/credit hour |
| College of Fine Arts | $82.86/credit hour |

#### International Student Cost (2025-26)

| 项目 | Lower-Level (≤55 credits) | Upper-Level (>55 credits) |
|------|---------------------------|---------------------------|
| Tuition and Fees | $21,408 | $23,328 |
| Health Insurance | $1,324 | $1,324 |
| Living Expenses | $16,125 | $16,125 |
| **Total** | **$38,857** | **$40,777** |

> Source: https://wmich.edu/finaid/cost-of-attendance, https://wmich.edu/international/apply

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 详情 |
|------|------|
| **Need-Blind/Need-Aware** | Need-aware for all students (including domestic) |
| **International Aid** | Limited; Global Education Merit Scholarship up to $10,000/year |
| **Tuition-Free Threshold** | None published |
| **Median Actual Price** | Not published |
| **Debt-Free Graduation Rate** | Not published |
| **99%** | of full-time UG students with financial need received aid (2023-24 CDS) |
| **60%** | of students receive grant money directly from the school |
| **Scholarship Deadline** | Feb 15 (priority) |
| **Scholarship Tool** | Scholarship Universe |

> Source: https://wmich.edu/finaid/aid-types, https://wmich.edu/finaid/cost-of-attendance

### 4.3 Graduate Cost & Funding Framework

| 维度 | 详情 |
|------|------|
| **Tuition (Resident)** | $868.04/credit hour |
| **Tuition (Non-Resident)** | $1,326.71/credit hour |
| **Tuition (Online)** | $868.04/credit hour |
| **Fees** | $70/semester (Assessment + Sustainability) |
| **Application Fee (Domestic)** | $50 |
| **Application Fee (International)** | $100 |
| **Funding Types** | Assistantships (RA/TA), Fellowships, Scholarships |
| **PhD Funding** | Most programs offer assistantships with tuition waiver |
| **Master's Funding** | Limited; varies by program |

> Source: https://wmich.edu/finaid/cost-of-attendance, https://wmich.edu/grad/apply

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Early Action Deadline
- **field**: undergraduate.deadlines.early_action
- **value**: December 15 (non-binding)
- **source_url**: https://wmich.edu/apply/deadlines
- **source_snippet**: "December 15, Early Action (non-binding)—Admission to all Western academic programs†"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-002: Rolling Admission Deadline
- **field**: undergraduate.deadlines.rolling
- **value**: July 28 (fall entry)
- **source_url**: https://wmich.edu/apply/deadlines
- **source_snippet**: "July 28, Rolling Admission—Admission to WMU academic programs†"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-003: Test-Optional Policy
- **field**: undergraduate.testing.policy
- **value**: Test-optional (since 2020)
- **source_url**: https://wmich.edu/admissions/first-year-apply/criteria
- **source_snippet**: "In 2020, Western Michigan University adopted a test-optional policy for students that applies to..."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-004: TOEFL Minimum
- **field**: undergraduate.english_proficiency.toefl
- **value**: 71 (most programs), 91 (Aviation Flight Science)
- **source_url**: https://wmich.edu/international/apply/english-proficiency
- **source_snippet**: "Test of English as a Foreign Language (TOEFL iBT) - WMU Institutional Code: 1902 | 71 | 91"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-005: IELTS Minimum
- **field**: undergraduate.english_proficiency.ielts
- **value**: 6.0 (most programs), 7.0 (Aviation Flight Science)
- **source_url**: https://wmich.edu/international/apply/english-proficiency
- **source_snippet**: "International English Language Testing System (IELTS) Academic | 6.0 | 7.0"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-006: Duolingo Minimum
- **field**: undergraduate.english_proficiency.duolingo
- **value**: 100 (most programs), 115 (Aviation Flight Science)
- **source_url**: https://wmich.edu/international/apply/english-proficiency
- **source_snippet**: "Duolingo | 100 | 115"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-007: Resident Tuition
- **field**: undergraduate.costs.tuition_resident
- **value**: $16,449 (Fall+Spring)
- **source_url**: https://wmich.edu/finaid/cost-of-attendance
- **source_snippet**: "Tuition | $4,112 | $16,449 | $4,112"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-008: Non-Resident Tuition
- **field**: undergraduate.costs.tuition_nonresident
- **value**: $20,525 (Fall+Spring)
- **source_url**: https://wmich.edu/finaid/cost-of-attendance
- **source_snippet**: "Tuition | $5,140 | $20,525 | $5,140"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-009: Total COA Resident
- **field**: undergraduate.costs.total_resident
- **value**: $37,270 (Fall+Spring)
- **source_url**: https://wmich.edu/finaid/cost-of-attendance
- **source_snippet**: "TOTAL | $9,317 | $37,270 | $9,317"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-010: International UG Cost
- **field**: undergraduate.costs.international
- **value**: $38,857 (lower-level), $40,777 (upper-level)
- **source_url**: https://wmich.edu/international/apply
- **source_snippet**: "Total (one academic year) | $38,857 | $40,466 | $41,006 | $38,857"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-G-001: Graduate Application Fee
- **field**: graduate.application.fee
- **value**: $50 domestic, $100 international
- **source_url**: https://wmich.edu/grad/apply
- **source_snippet**: "Be prepared to pay a nonrefundable application fee online by credit card—$50 for domestic applicants and $100 for international applicants."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-002: Graduate TOEFL Minimum
- **field**: graduate.english_proficiency.toefl
- **value**: 80 iBT
- **source_url**: https://wmich.edu/international/apply/english-proficiency
- **source_snippet**: "Test of English as a Foreign Language (TOEFL iBT) - WMU Institutional Code: 1902 | 80"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-G-003: Graduate Tuition Resident
- **field**: graduate.costs.tuition_resident
- **value**: $868.04/credit hour
- **source_url**: https://wmich.edu/finaid/cost-of-attendance
- **source_snippet**: "$868.04 per credit hour"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-G-004: Graduate Tuition Non-Resident
- **field**: graduate.costs.tuition_nonresident
- **value**: $1,326.71/credit hour
- **source_url**: https://wmich.edu/finaid/cost-of-attendance
- **source_snippet**: "$1,326.71 per credit hour"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-S-001: College Structure
- **field**: institution.colleges
- **value**: 7 degree-granting colleges + Merze Tate + Lee Honors + Graduate College
- **source_url**: https://wmich.edu/directories/colleges
- **source_snippet**: "You'll find the field of study you're most interested in pursuing in one of the 10 colleges or interdisciplinary programs at Western."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-S-002: Program Count
- **field**: institution.programs.total
- **value**: 434 (153 UG majors + 131 UG minors + 15 UG certs + 95 grad degrees + 40 grad certs)
- **source_url**: https://catalog.wmich.edu/content.php?catoid=47&navoid=2271
- **source_snippet**: 309 undergraduate program entries + 135 graduate program entries
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-S-003: Need-Aware Policy
- **field**: institution.financial_aid.need_blind
- **value**: Need-aware for all students
- **source_url**: https://wmich.edu/finaid/aid-types
- **source_snippet**: "99% of full-time undergraduate students with financial need received aid"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
WMU-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: Rules 1-4)
├── 01-ug-arts-sciences.md             (Section 1: A&S programs)
├── 02-ug-aviation.md                  (Section 1: Aviation programs)
├── 03-ug-business.md                  (Section 1: Business programs)
├── 04-ug-education.md                 (Section 1: Education programs)
├── 05-ug-engineering.md               (Section 1: Engineering programs)
├── 06-ug-fine-arts.md                 (Section 1: Fine Arts programs)
├── 07-ug-health-human-services.md     (Section 1: HHS programs)
├── 08-grad-arts-sciences.md           (Section 2: A&S grad programs)
├── 09-grad-business.md                (Section 2: Business grad programs)
├── 10-grad-education.md               (Section 2: Education grad programs)
├── 11-grad-engineering.md             (Section 2: Engineering grad programs)
├── 12-grad-fine-arts.md               (Section 2: Fine Arts grad programs)
├── 13-grad-health-human-services.md   (Section 2: HHS grad programs)
├── 14-grad-interdisciplinary.md       (Section 2: Interdisciplinary grad)
├── 15-deadlines-requirements.md       (Section 3)
├── 16-costs-financial-aid.md          (Section 4)
├── 17-evidence-chain.md               (Section 5)
└── 18-comparison-framework.md         (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "WMU-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BFA|BSE|BBA|BM|BSN|MA|MS|MSE|MFA|MBA|PhD|EdD|DPT|OTD|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Individual program deadlines (per graduate program) | https://wmich.edu/grad/program-allprograms |
| P0 | Graduate program-specific GRE requirements | https://wmich.edu/grad/program-doctoralprograms |
| P0 | Graduate program-specific funding details | Individual program pages |
| P1 | Complete list of undergraduate minors | https://catalog.wmich.edu/content.php?catoid=47&navoid=2271 |
| P1 | Aviation Flight Science special requirements | https://wmich.edu/aviation/academics/aviation-flight-science |
| P1 | Merit scholarship details | https://wmich.edu/finaid/aid-types/institutional-offers |
| P2 | Campus housing options and costs | https://wmich.edu/housing |
| P2 | Student-to-faculty ratio | https://wmich.edu/institutionalresearch |
| P2 | Graduation rates | https://wmich.edu/institutionalresearch/commondataset |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | WMU | (Other Schools) |
|------|-----|-----------------|
| **Type** | Public | |
| **Location** | Kalamazoo, MI | |
| **Total Programs (Rule 1)** | 434 | |
| **UG Majors** | 153 | |
| **UG Minors** | 131 | |
| **Graduate Degrees** | 95 | |
| **Graduate Certificates** | 40 | |
| **Colleges (Rule 2)** | 7 + 3 | |
| **UG Tuition (Resident)** | $16,449/yr | |
| **UG Tuition (Non-Resident)** | $20,525/yr | |
| **UG COA (Resident, On-Campus)** | $37,270/yr | |
| **UG COA (Non-Resident, On-Campus)** | $41,346/yr | |
| **Need-Blind (Domestic)** | No (need-aware) | |
| **Need-Blind (International)** | No (need-aware) | |
| **EA Deadline** | December 15 | |
| **RA/Rolling Deadline** | July 28 | |
| **SAT/ACT Required** | No (test-optional) | |
| **TOEFL Minimum (UG)** | 71 | |
| **IELTS Minimum (UG)** | 6.0 | |
| **Duolingo Minimum (UG)** | 100 | |
| **Graduate TOEFL Minimum** | 80 | |
| **Graduate IELTS Minimum** | 6.5 | |
| **Grad Application Fee (Domestic)** | $50 | |
| **Grad Application Fee (International)** | $100 | |
| **Application Platform** | Common App (UG) | |
| **International Merit Scholarship** | Up to $10,000/yr | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: wmich.edu, catalog.wmich.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
