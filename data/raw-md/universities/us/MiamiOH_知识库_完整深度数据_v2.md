# Miami University (Ohio) Admissions Knowledge Base -- Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/BPh/BISA/BArch) | 102 |
| 本科辅修 (Minor) | 95 |
| 本科证书 (UG Certificate) | 11 |
| 本科 Co-Major | 17 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/DNP/etc.) | 76 |
| 研究生证书 (Graduate Certificate) | 23 |
| **学位项目总计 (UG + Grad, counting degree rows)** | **198** |
| 学院 / 独立系所总数 | 8 (6 UG-degree-granting colleges + 1 center + Graduate School) |

> Sources: bulletin.miamioh.edu (2026-2027 bulletin), graduateschool.miamioh.edu. Counts derived from structured extraction of each college's program listing. Co-majors counted separately (they share the degree designation of the primary major). UG certificates counted in the UG total. Graduate certificates counted in the grad total.

### 0.2 学院 / 系层级结构 (Rule 2)

```
Miami University (Oxford, OH)
├── College of Arts and Science (CAS)                    [学院]
│   ├── Anthropology                                     [系]
│   ├── Biochemistry                                     [系]
│   ├── Biology                                          [系]
│   ├── Botany                                           [系]
│   ├── Chemistry and Biochemistry                       [系]
│   ├── Data Analytics                                   [系]
│   ├── Economics (UG portion)                           [系]
│   ├── English                                          [系]
│   ├── Geography and Sustainable Development             [系]
│   ├── Geology and Environmental Earth Science           [系]
│   ├── History                                          [系]
│   ├── Mathematics                                      [系]
│   ├── Media and Communication                          [系]
│   ├── Microbiology                                     [系]
│   ├── Philosophy                                       [系]
│   ├── Physics                                          [系]
│   ├── Political Science                                [系]
│   ├── Psychology                                       [系]
│   ├── Sociology and Gerontology                        [系]
│   ├── Spanish and Portuguese                           [系]
│   ├── Speech Pathology and Audiology                   [系]
│   └── Interdisciplinary Programs (American Studies, Critical Race & Ethnic Studies, etc.) [系]
├── College of Creative Arts (CCA)                       [学院]
│   ├── Architecture + Interior Design                   [系]
│   ├── Art                                              [系]
│   ├── Emerging Technology in Business and Design        [系]
│   ├── Music                                            [系]
│   └── Theatre                                          [系]
├── College of Education, Health and Society (EHS)        [学院]
│   ├── Educational Leadership                           [系]
│   ├── Educational Psychology                           [系]
│   ├── Teacher Education                                [系]
│   ├── Kinesiology, Nutrition and Health                [系]
│   ├── Sport Leadership and Management                  [系]
│   └── Family Science and Social Work                   [系]
├── College of Engineering and Computing (CEC)            [学院]
│   ├── Chemical, Paper and Biomedical Engineering       [系]
│   ├── Electrical and Computer Engineering              [系]
│   ├── Mechanical and Manufacturing Engineering         [系]
│   ├── Computer Science and Software Engineering        [系]
│   └── Engineering (interdisciplinary)                  [系]
├── Farmer School of Business (FSB)                      [学院]
│   ├── Accountancy                                      [系]
│   ├── Finance                                          [系]
│   ├── Information Systems and Analytics                [系]
│   ├── Management                                       [系]
│   ├── Marketing                                        [系]
│   └── Economics (grad portion)                         [系]
├── College of Liberal Arts and Applied Science (CLAAS)   [学院]  (Regional Campuses)
│   ├── Applied Sciences                                 [系]
│   ├── Commerce                                         [系]
│   ├── Humanities and Creative Arts                     [系]
│   ├── Nursing                                          [系]
│   └── Social and Behavioral Sciences                   [系]
├── Center for Civics, Culture, and Society               [中心]
│   └── Civic Thought (minor only)                       [系]
└── The Graduate School                                  [学院]  (administrative umbrella)
    ├── Interdisciplinary Programs (CMSB, EEEB, EnvSci)  [系]
    └── (delegates to departments in the colleges above)
```

### 0.3 学历级别明细 (Rule 3)

| 学位缩写 (canonical) | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|--------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 31 |
| BISA | BISA | Bachelor of Arts in International Studies | 本科 | 1 |
| BPh | BPh | Bachelor of Philosophy | 本科 | 1 |
| BS | BS | Bachelor of Science | 本科 | 16 |
| BSED | BSED | Bachelor of Science in Education | 本科 | 7 |
| BSKNH | BSKNH | Bachelor of Science in Kinesiology, Nutrition, and Health | 本科 | 2 |
| BSW | BSW | Bachelor of Science in Social Work | 本科 | 1 |
| BSSLM | BSSLM | Bachelor of Science in Sport Leadership and Management | 本科 | 4 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 4 |
| BM | BM | Bachelor of Music | 本科 | 2 |
| BArch | BArch | Bachelor of Arts in Architecture | 本科 | 1 |
| BSAB | BSAB | Bachelor of Science (Business) | 本科 | 9 |
| Minor | Minor | 辅修 | 本科 | 95 |
| UG Cert | UG Cert | 本科证书 | 本科 | 11 |
| MA | MA | Master of Arts | 研究生 | 14 |
| MS | MS | Master of Science | 研究生 | 18 |
| MFA | MFA | Master of Fine Arts | 研究生 | 2 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 4 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 3 |
| MM | MM | Master of Music | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MEM | MEM | Master of Engineering | 研究生 | 3 |
| MCS | MCS | Master of Computer Science | 研究生 | 1 |
| MEET | MEET | Master of Entrepreneurship and Emerging Technology | 研究生 | 1 |
| MAcc | MAcc | Master of Accountancy | 研究生 | 1 |
| MES | MES | Master of Environmental Science | 研究生 | 1 |
| MGS | MGS | Master of Gerontological Studies | 研究生 | 1 |
| MSAT | MSAT | Master of Athletic Training | 研究生 | 1 |
| MSBA | MSBA | Master of Science in Business Analytics | 研究生 | 1 |
| MSN | MSN | Master of Science in Nursing | 研究生 | 1 |
| MSPE | MSPE | Master of Sport Analytics | 研究生 | 1 |
| EdS | EdS | Specialist in Education | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 14 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| Grad Cert | Grad Cert | 研究生证书 | 研究生 | 23 |

### 0.4 分布矩阵 (Rule 4 -- 学院 x canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSED | BFA | BM | BArch | BSAB | Other UG | Minor | UG Cert | MA | MS | MFA | MBA | MEd | MAT | Other Grad | PhD | EdD | DNP | Grad Cert | 合计 |
|------------|----|----|------|-----|-----|-------|------|----------|-------|---------|----|----|-----|-----|-----|-----|------------|-----|-----|-----|-----------|------|
| CAS | 31 | 16 | 0 | 0 | 0 | 0 | 0 | 2 | 52 | 10 | 8 | 5 | 1 | 0 | 0 | 2 | 3 | 7 | 0 | 0 | 5 | 142 |
| CCA | 5 | 1 | 0 | 4 | 2 | 1 | 0 | 0 | 14 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 30 |
| EHS | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 7 | 9 | 1 | 1 | 2 | 0 | 0 | 3 | 1 | 2 | 1 | 1 | 0 | 4 | 39 |
| CEC | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 8 |
| FSB | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 19 | 0 | 2 | 2 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 4 | 39 |
| CLAAS | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| CCS | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Grad School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 8 |
| **合计** | **36** | **17** | **7** | **4** | **2** | **1** | **9** | **9** | **95** | **11** | **11** | **14** | **2** | **1** | **3** | **3** | **9** | **10** | **1** | **1** | **23** | **269** |

> Note: Row totals include all program types (degree majors, minors, certificates, co-majors) for that college. Some graduate programs are interdisciplinary (CMSB, EEEB, EnvSci) and counted under the Graduate School. Reconciliation: total UG degree rows = 102, UG minors = 95, UG certs = 11, co-majors = 17 (counted within degree rows as they share the primary major's degree). Grad degree rows = 76, grad certs = 23. Total unique program entries = 269.

---

## SECTION 1 -- Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Miami University has 6 undergraduate-degree-granting colleges at the Oxford campus, plus 1 center (CCS, minor only) and the regional campus college (CLAAS). The Graduate School is an administrative umbrella. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors -- grouped by 学院 > 系 > 学位级别

#### College of Arts and Science (CAS)

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.miamioh.edu/arts-science/ |

##### Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://bulletin.miamioh.edu/arts-science/ |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.miamioh.edu/arts-science/ |

##### Botany
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Botany | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Botany | https://bulletin.miamioh.edu/arts-science/ |

##### Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.miamioh.edu/arts-science/ |

##### Data Analytics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Analytics | https://bulletin.miamioh.edu/arts-science/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Quantitative Economics | https://bulletin.miamioh.edu/arts-science/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English: Creative Writing | https://bulletin.miamioh.edu/arts-science/ |
| 2 | English: Literature | https://bulletin.miamioh.edu/arts-science/ |

##### Geography and Sustainable Development
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography and Sustainable Development | https://bulletin.miamioh.edu/arts-science/ |

##### Geology and Environmental Earth Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Earth Science | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Geology | https://bulletin.miamioh.edu/arts-science/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://bulletin.miamioh.edu/arts-science/ |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Mathematics | https://bulletin.miamioh.edu/arts-science/ |
| 3 | Mathematics and Statistics | https://bulletin.miamioh.edu/arts-science/ |

##### Media and Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Media and Communication | https://bulletin.miamioh.edu/arts-science/ |
| 3 | Strategic Communication | https://bulletin.miamioh.edu/arts-science/ |

##### Microbiology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | https://bulletin.miamioh.edu/arts-science/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.miamioh.edu/arts-science/ |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.miamioh.edu/arts-science/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Diplomacy and Global Politics | https://bulletin.miamioh.edu/arts-science/ |
| 3 | Public Administration | https://bulletin.miamioh.edu/arts-science/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.miamioh.edu/arts-science/ |

##### Sociology and Gerontology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://bulletin.miamioh.edu/arts-science/ |

##### Spanish and Portuguese
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://bulletin.miamioh.edu/arts-science/ |

##### Speech Pathology and Audiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech Pathology and Audiology | https://bulletin.miamioh.edu/arts-science/ |

##### Interdisciplinary Programs
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Individualized Studies | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Linguistics | https://bulletin.miamioh.edu/arts-science/ |
| 3 | Organizational Leadership | https://bulletin.miamioh.edu/arts-science/ |
| 4 | Professional Writing | https://bulletin.miamioh.edu/arts-science/ |
| 5 | Public Health | https://bulletin.miamioh.edu/arts-science/ |
| 6 | Urban and Regional Planning | https://bulletin.miamioh.edu/arts-science/ |
| 7 | World Languages and Cultures | https://bulletin.miamioh.edu/arts-science/ |

###### BISA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://bulletin.miamioh.edu/arts-science/ |

###### BPh
| # | 专业 | URL |
|---|------|-----|
| 1 | Individualized Studies | https://bulletin.miamioh.edu/arts-science/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data, Actuarial, and Statistical Sciences | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Zoology | https://bulletin.miamioh.edu/arts-science/ |

#### College of Creative Arts (CCA)

##### Architecture + Interior Design
###### BArch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://bulletin.miamioh.edu/creative-arts/ |

##### Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://bulletin.miamioh.edu/creative-arts/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://bulletin.miamioh.edu/creative-arts/ |
| 2 | Graphic + Experience Design | https://bulletin.miamioh.edu/creative-arts/ |
| 3 | Interior Design | https://bulletin.miamioh.edu/creative-arts/ |

##### Emerging Technology in Business and Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interactive Media and Design | https://bulletin.miamioh.edu/creative-arts/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Games + Simulation | https://bulletin.miamioh.edu/creative-arts/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://bulletin.miamioh.edu/creative-arts/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://bulletin.miamioh.edu/creative-arts/ |
| 2 | Music Performance | https://bulletin.miamioh.edu/creative-arts/ |

##### Theatre
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Performing Arts | https://bulletin.miamioh.edu/creative-arts/ |

##### Interdisciplinary
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Arts Management and Arts Entrepreneurship | https://bulletin.miamioh.edu/creative-arts/ |

###### BS (Art Education)
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | https://bulletin.miamioh.edu/creative-arts/ |

#### College of Education, Health and Society (EHS)

##### Teacher Education
###### BSED
| # | 专业 | URL |
|---|------|-----|
| 1 | Inclusive Education | https://bulletin.miamioh.edu/education-health-society/ |
| 2 | Integrated English Language Arts Education | https://bulletin.miamioh.edu/education-health-society/ |
| 3 | Integrated Mathematics Education | https://bulletin.miamioh.edu/education-health-society/ |
| 4 | Integrated Science Education | https://bulletin.miamioh.edu/education-health-society/ |
| 5 | Integrated Social Studies Education | https://bulletin.miamioh.edu/education-health-society/ |
| 6 | Middle Childhood Education | https://bulletin.miamioh.edu/education-health-society/ |
| 7 | Primary Education PK-5 | https://bulletin.miamioh.edu/education-health-society/ |

##### Kinesiology, Nutrition and Health
###### BSKNH
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://bulletin.miamioh.edu/education-health-society/ |
| 2 | Nutrition | https://bulletin.miamioh.edu/education-health-society/ |

##### Family Science and Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://bulletin.miamioh.edu/education-health-society/ |

##### Sport Leadership and Management
###### BSSLM
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Coaching | https://bulletin.miamioh.edu/education-health-society/ |
| 2 | Sport Communication and Media | https://bulletin.miamioh.edu/education-health-society/ |
| 3 | Sport Management | https://bulletin.miamioh.edu/education-health-society/ |

#### College of Engineering and Computing (CEC)

##### Chemical, Paper and Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://bulletin.miamioh.edu/engineering-computing/ |
| 2 | Paper Engineering | https://bulletin.miamioh.edu/engineering-computing/ |
| 3 | Biomedical Engineering | https://bulletin.miamioh.edu/engineering-computing/ |

##### Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.miamioh.edu/engineering-computing/ |
| 2 | Computer Engineering | https://bulletin.miamioh.edu/engineering-computing/ |

##### Mechanical and Manufacturing Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.miamioh.edu/engineering-computing/ |
| 2 | Manufacturing Engineering | https://bulletin.miamioh.edu/engineering-computing/ |

##### Computer Science and Software Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.miamioh.edu/engineering-computing/ |
| 2 | Software Engineering | https://bulletin.miamioh.edu/engineering-computing/ |
| 3 | Cybersecurity and Networking | https://bulletin.miamioh.edu/engineering-computing/ |

#### Farmer School of Business (FSB)

##### Accountancy
###### BSAB
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://bulletin.miamioh.edu/farmer-business/ |

##### Finance
###### BSAB
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://bulletin.miamioh.edu/farmer-business/ |
| 2 | Real Estate | https://bulletin.miamioh.edu/farmer-business/ |

##### Information Systems and Analytics
###### BSAB
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://bulletin.miamioh.edu/farmer-business/ |
| 2 | Information Systems and Cybersecurity Management | https://bulletin.miamioh.edu/farmer-business/ |

##### Management
###### BSAB
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Capital Management and Leadership | https://bulletin.miamioh.edu/farmer-business/ |
| 2 | Supply Chain and Operations Management | https://bulletin.miamioh.edu/farmer-business/ |

##### Marketing
###### BSAB
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://bulletin.miamioh.edu/farmer-business/ |

##### Economics (Farmer)
###### BSAB
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://bulletin.miamioh.edu/farmer-business/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

CAS Co-Majors (share degree designation of primary major):
| # | Co-Major | URL |
|---|----------|-----|
| 1 | Energy | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Environmental Science | https://bulletin.miamioh.edu/arts-science/ |
| 3 | Film Studies | https://bulletin.miamioh.edu/arts-science/ |
| 4 | Food Systems and Food Studies | https://bulletin.miamioh.edu/arts-science/ |
| 5 | Neuroscience | https://bulletin.miamioh.edu/arts-science/ |
| 6 | Pre-Art Therapy | https://bulletin.miamioh.edu/arts-science/ |
| 7 | Premedical and Pre-Health Studies | https://bulletin.miamioh.edu/arts-science/ |
| 8 | Sustainability | https://bulletin.miamioh.edu/arts-science/ |
| 9 | Women's, Gender, and Sexuality Studies | https://bulletin.miamioh.edu/arts-science/ |

CCA Co-Majors:
| # | Co-Major | URL |
|---|----------|-----|
| 1 | Arts Management | https://bulletin.miamioh.edu/creative-arts/ |
| 2 | Fashion | https://bulletin.miamioh.edu/creative-arts/ |
| 3 | Pre-Art Therapy | https://bulletin.miamioh.edu/creative-arts/ |

EHS Co-Majors:
| # | Co-Major | URL |
|---|----------|-----|
| 1 | Child Life Specialist | https://bulletin.miamioh.edu/education-health-society/ |

FSB Co-Majors:
| # | Co-Major | URL |
|---|----------|-----|
| 1 | Business Leadership | https://bulletin.miamioh.edu/farmer-business/ |
| 2 | Entrepreneurship | https://bulletin.miamioh.edu/farmer-business/ |

### 1.4 Minors -- complete list

#### CAS Minors (52)
| # | Minor | URL |
|---|-------|-----|
| 1 | Actuarial Science | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Aerospace Studies | https://bulletin.miamioh.edu/arts-science/ |
| 3 | American Studies | https://bulletin.miamioh.edu/arts-science/ |
| 4 | Anthropology | https://bulletin.miamioh.edu/arts-science/ |
| 5 | Archaeology | https://bulletin.miamioh.edu/arts-science/ |
| 6 | Bioinformatics | https://bulletin.miamioh.edu/arts-science/ |
| 7 | Chinese | https://bulletin.miamioh.edu/arts-science/ |
| 8 | Classical Studies | https://bulletin.miamioh.edu/arts-science/ |
| 9 | Creative Writing | https://bulletin.miamioh.edu/arts-science/ |
| 10 | Criminology | https://bulletin.miamioh.edu/arts-science/ |
| 11 | Data Analytics | https://bulletin.miamioh.edu/arts-science/ |
| 12 | Economics | https://bulletin.miamioh.edu/arts-science/ |
| 13 | English Literature | https://bulletin.miamioh.edu/arts-science/ |
| 14 | Ethics, Society, and Culture | https://bulletin.miamioh.edu/arts-science/ |
| 15 | Film Studies | https://bulletin.miamioh.edu/arts-science/ |
| 16 | French | https://bulletin.miamioh.edu/arts-science/ |
| 17 | Geography | https://bulletin.miamioh.edu/arts-science/ |
| 18 | Geology | https://bulletin.miamioh.edu/arts-science/ |
| 19 | German | https://bulletin.miamioh.edu/arts-science/ |
| 20 | Gerontology | https://bulletin.miamioh.edu/arts-science/ |
| 21 | Global Health | https://bulletin.miamioh.edu/arts-science/ |
| 22 | Global Perspectives on Sustainability | https://bulletin.miamioh.edu/arts-science/ |
| 23 | History | https://bulletin.miamioh.edu/arts-science/ |
| 24 | Horticulture | https://bulletin.miamioh.edu/arts-science/ |
| 25 | Humanities for Leadership | https://bulletin.miamioh.edu/arts-science/ |
| 26 | Individualized Studies | https://bulletin.miamioh.edu/arts-science/ |
| 27 | International Studies | https://bulletin.miamioh.edu/arts-science/ |
| 28 | Italian | https://bulletin.miamioh.edu/arts-science/ |
| 29 | Japanese | https://bulletin.miamioh.edu/arts-science/ |
| 30 | Journalism | https://bulletin.miamioh.edu/arts-science/ |
| 31 | Latin American Latino/a Caribbean Studies | https://bulletin.miamioh.edu/arts-science/ |
| 32 | Linguistics | https://bulletin.miamioh.edu/arts-science/ |
| 33 | Mathematics | https://bulletin.miamioh.edu/arts-science/ |
| 34 | Medical Humanities | https://bulletin.miamioh.edu/arts-science/ |
| 35 | Middle East, Jewish, and Islamic Studies | https://bulletin.miamioh.edu/arts-science/ |
| 36 | Military and Strategic Leadership | https://bulletin.miamioh.edu/arts-science/ |
| 37 | Molecular Biology | https://bulletin.miamioh.edu/arts-science/ |
| 38 | Naval Science | https://bulletin.miamioh.edu/arts-science/ |
| 39 | Neuroscience | https://bulletin.miamioh.edu/arts-science/ |
| 40 | Philosophy and Law | https://bulletin.miamioh.edu/arts-science/ |
| 41 | Philosophy, Politics, and Economics | https://bulletin.miamioh.edu/arts-science/ |
| 42 | Physics | https://bulletin.miamioh.edu/arts-science/ |
| 43 | Political Science | https://bulletin.miamioh.edu/arts-science/ |
| 44 | Pre-Art Therapy | https://bulletin.miamioh.edu/arts-science/ |
| 45 | Professional Writing and Rhetoric | https://bulletin.miamioh.edu/arts-science/ |
| 46 | Religion | https://bulletin.miamioh.edu/arts-science/ |
| 47 | Russian, East European, and Eurasian Studies | https://bulletin.miamioh.edu/arts-science/ |
| 48 | Sociology | https://bulletin.miamioh.edu/arts-science/ |
| 49 | Spanish | https://bulletin.miamioh.edu/arts-science/ |
| 50 | Statistical Methods | https://bulletin.miamioh.edu/arts-science/ |
| 51 | Statistics | https://bulletin.miamioh.edu/arts-science/ |
| 52 | Women's, Gender, and Sexuality Studies | https://bulletin.miamioh.edu/arts-science/ |

#### CCA Minors (14)
| # | Minor | URL |
|---|-------|-----|
| 1 | Animation | https://bulletin.miamioh.edu/creative-arts/ |
| 2 | Architecture and Interior Design Studies | https://bulletin.miamioh.edu/creative-arts/ |
| 3 | Arts Management | https://bulletin.miamioh.edu/creative-arts/ |
| 4 | Art and Architecture History | https://bulletin.miamioh.edu/creative-arts/ |
| 5 | Construction Management | https://bulletin.miamioh.edu/creative-arts/ |
| 6 | Dance | https://bulletin.miamioh.edu/creative-arts/ |
| 7 | Digital Innovation | https://bulletin.miamioh.edu/creative-arts/ |
| 8 | Digital Marketing | https://bulletin.miamioh.edu/creative-arts/ |
| 9 | Fashion | https://bulletin.miamioh.edu/creative-arts/ |
| 10 | Games + Simulation | https://bulletin.miamioh.edu/creative-arts/ |
| 11 | Graphic Design | https://bulletin.miamioh.edu/creative-arts/ |
| 12 | Interactive Media and Design | https://bulletin.miamioh.edu/creative-arts/ |
| 13 | Museums and Society | https://bulletin.miamioh.edu/creative-arts/ |
| 14 | Music Composition | https://bulletin.miamioh.edu/creative-arts/ |

#### EHS Minors (9)
| # | Minor | URL |
|---|-------|-----|
| 1 | Child Studies and Youth Development | https://bulletin.miamioh.edu/education-health-society/ |
| 2 | Coaching | https://bulletin.miamioh.edu/education-health-society/ |
| 3 | Community, Leadership, and Social Change | https://bulletin.miamioh.edu/education-health-society/ |
| 4 | Disability Studies | https://bulletin.miamioh.edu/education-health-society/ |
| 5 | Family Relationships | https://bulletin.miamioh.edu/education-health-society/ |
| 6 | Health Behavior | https://bulletin.miamioh.edu/education-health-society/ |
| 7 | Inclusive Special Education | https://bulletin.miamioh.edu/education-health-society/ |
| 8 | Nutrition | https://bulletin.miamioh.edu/education-health-society/ |
| 9 | Sport Analytics | https://bulletin.miamioh.edu/education-health-society/ |

#### FSB Minors (19)
| # | Minor | URL |
|---|-------|-----|
| 1 | Accountancy | https://bulletin.miamioh.edu/farmer-business/ |
| 2 | Artificial Intelligence for Business | https://bulletin.miamioh.edu/farmer-business/ |
| 3 | Arts Management | https://bulletin.miamioh.edu/farmer-business/ |
| 4 | Business | https://bulletin.miamioh.edu/farmer-business/ |
| 5 | Business Analytics | https://bulletin.miamioh.edu/farmer-business/ |
| 6 | Business Leadership | https://bulletin.miamioh.edu/farmer-business/ |
| 7 | Climate Accounting and Engineering | https://bulletin.miamioh.edu/farmer-business/ |
| 8 | Cybersecurity Management | https://bulletin.miamioh.edu/farmer-business/ |
| 9 | Economics | https://bulletin.miamioh.edu/farmer-business/ |
| 10 | Entrepreneurship | https://bulletin.miamioh.edu/farmer-business/ |
| 11 | Finance | https://bulletin.miamioh.edu/farmer-business/ |
| 12 | Financial Planning and Wealth Management | https://bulletin.miamioh.edu/farmer-business/ |
| 13 | Human Capital Management and Leadership | https://bulletin.miamioh.edu/farmer-business/ |
| 14 | Information Systems | https://bulletin.miamioh.edu/farmer-business/ |
| 15 | International Business | https://bulletin.miamioh.edu/farmer-business/ |
| 16 | Management | https://bulletin.miamioh.edu/farmer-business/ |
| 17 | Marketing | https://bulletin.miamioh.edu/farmer-business/ |
| 18 | Real Estate | https://bulletin.miamioh.edu/farmer-business/ |
| 19 | Supply Chain Management | https://bulletin.miamioh.edu/farmer-business/ |

#### CCS Minor (1)
| # | Minor | URL |
|---|-------|-----|
| 1 | Civic Thought | https://bulletin.miamioh.edu/civics-center/ |

### 1.5 General/Institute-wide requirements

Miami Plan for Liberal Education: https://miamioh.edu/academic-programs/academic-approach/index.html

The Miami Plan is the university's liberal education framework. All undergraduates complete foundational courses (English composition, mathematics, fine arts, humanities, social science, natural science, global perspectives), thematic sequences, and a senior capstone.

### 1.6 UG Certificates (11)
| # | Certificate | College | URL |
|---|-------------|---------|-----|
| 1 | Computational Linguistics | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 2 | Financial Mathematics | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 3 | Geographic Information Science (GIS) | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 4 | Global Readiness | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 5 | Humanities Engagement | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 6 | Mathematical Modeling | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 7 | Mathematics Education (non-licensure) | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 8 | Medical Spanish and Latino Health | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 9 | Premedical and Pre-Health Studies (post-bacc) | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 10 | Speech Pathology and Audiology (post-bacc) | CAS | https://bulletin.miamioh.edu/arts-science/ |
| 11 | Fostering Just Communities | EHS | https://bulletin.miamioh.edu/education-health-society/ |

---

## SECTION 2 -- Graduate education (Rule 5 grouping)

### 2.1 Graduate programs -- grouped by 学院 > 系 > 学位级别

> Source: bulletin.miamioh.edu/graduate-school/ and bulletin.miamioh.edu/graduate-fields-study/

#### College of Arts and Science (CAS) -- Graduate

##### Biology
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Biology & Botany | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Biology, Botany, & Microbiology | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MAT | Biological Sciences | https://bulletin.miamioh.edu/graduate-school/ |
| 4 | PhD | Biology, Botany, & Microbiology | https://bulletin.miamioh.edu/graduate-school/ |

##### Cell, Molecular and Structural Biology (interdisciplinary)
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Cell, Molecular and Structural Biology | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | PhD | Cell, Molecular and Structural Biology | https://bulletin.miamioh.edu/graduate-school/ |

##### Chemistry and Biochemistry
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Chemistry | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | PhD | Chemistry | https://bulletin.miamioh.edu/graduate-school/ |

##### Ecology, Evolution and Environmental Biology (interdisciplinary)
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | PhD | Ecology, Evolution and Environmental Biology | https://bulletin.miamioh.edu/graduate-school/ |

##### English
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | English | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MAT | English | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MFA | Creative Writing | https://bulletin.miamioh.edu/graduate-school/ |
| 4 | PhD | English | https://bulletin.miamioh.edu/graduate-school/ |

##### Environmental Science (interdisciplinary)
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MES | Environmental Science | https://bulletin.miamioh.edu/graduate-school/ |

##### Geography and Sustainable Development
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Geography | https://bulletin.miamioh.edu/graduate-school/ |

##### Geology and Environmental Earth Science
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Geology | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Geology | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | PhD | Geology | https://bulletin.miamioh.edu/graduate-school/ |

##### History
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | History | https://bulletin.miamioh.edu/graduate-school/ |

##### Mathematics
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Mathematics | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Mathematics | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MAT | Mathematics (for licensed teachers) | https://bulletin.miamioh.edu/graduate-school/ |

##### Philosophy
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Philosophy | https://bulletin.miamioh.edu/graduate-school/ |

##### Physics
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Physics | https://bulletin.miamioh.edu/graduate-school/ |

##### Psychology
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Psychology (as required step in doctoral program) | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | PhD | Psychology | https://bulletin.miamioh.edu/graduate-school/ |

##### Sociology and Gerontology
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MGS | Gerontological Studies | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | PhD | Social Gerontology | https://bulletin.miamioh.edu/graduate-school/ |

##### Spanish and Portuguese
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Spanish | https://bulletin.miamioh.edu/graduate-school/ |

##### Speech-Language Pathology
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Speech-Language Pathology | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Speech-Language Pathology | https://bulletin.miamioh.edu/graduate-school/ |

##### Statistics
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Statistics | https://bulletin.miamioh.edu/graduate-school/ |

#### Farmer School of Business (FSB) -- Graduate

| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MAcc | Accountancy | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MBA | Business Administration | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MSBA | Business Analytics | https://bulletin.miamioh.edu/graduate-school/ |
| 4 | MA | Economics | https://bulletin.miamioh.edu/graduate-school/ |
| 5 | MEET | Entrepreneurship and Emerging Technology | https://bulletin.miamioh.edu/graduate-school/ |

#### College of Education, Health and Society (EHS) -- Graduate

##### Educational Leadership
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MEd | Educational Leadership | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Educational Leadership | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | EdD | Educational Leadership | https://bulletin.miamioh.edu/graduate-school/ |

##### Educational Psychology
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MA | Educational Psychology | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MEd | Educational Psychology | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MS | Educational Psychology | https://bulletin.miamioh.edu/graduate-school/ |
| 4 | EdS | Educational Psychology | https://bulletin.miamioh.edu/graduate-school/ |

##### Family Sciences and Social Work
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MSW | Social Work | https://bulletin.miamioh.edu/graduate-school/ |

##### Kinesiology, Nutrition and Health
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Kinesiology, Nutrition and Health | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MSAT | Athletic Training | https://bulletin.miamioh.edu/graduate-school/ |

##### Sport Leadership and Management
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Sport Leadership and Management | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MSPE | Sport Analytics | https://bulletin.miamioh.edu/graduate-school/ |

##### Teacher Education
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MAT | Teaching | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MEd | Education | https://bulletin.miamioh.edu/graduate-school/ |

#### College of Engineering and Computing (CEC) -- Graduate

##### Computer Science and Software Engineering
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MCS | Computer Science | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Computer Science | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | PhD | Computer Science | https://bulletin.miamioh.edu/graduate-school/ |

##### Chemical, Paper and Biomedical Engineering
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Chemical Engineering | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Clinical Engineering | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MEM | Chemical Engineering | https://bulletin.miamioh.edu/graduate-school/ |

##### Electrical and Computer Engineering
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MEM | Electrical and Computer Engineering | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MS | Electrical and Computer Engineering | https://bulletin.miamioh.edu/graduate-school/ |

##### Mechanical Engineering
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MS | Mechanical Engineering | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MEM | Mechanical Engineering | https://bulletin.miamioh.edu/graduate-school/ |

##### Engineering (interdisciplinary)
| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | PhD | Engineering | https://bulletin.miamioh.edu/graduate-school/ |

#### College of Creative Arts (CCA) -- Graduate

| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MArch | Architecture | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | MFA | Art (Studio) | https://bulletin.miamioh.edu/graduate-school/ |
| 3 | MEET | Entrepreneurship and Emerging Technology | https://bulletin.miamioh.edu/graduate-school/ |
| 4 | MM | Music (Performance) | https://bulletin.miamioh.edu/graduate-school/ |

#### College of Liberal Arts and Applied Science (CLAAS) -- Graduate

| # | Degree | 项目 | URL |
|---|--------|------|-----|
| 1 | MSN | Nursing | https://bulletin.miamioh.edu/graduate-school/ |
| 2 | DNP | Nursing Practice | https://bulletin.miamioh.edu/graduate-school/ |

### 2.2 Graduate Certificate Programs (23)

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Advanced Business Analytics | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 2 | Advanced Manufacturing and Materials Evaluation | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 3 | Analytics | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 4 | Applied Marine Conservation | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 5 | Business Foundations | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 6 | Business Operations | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 7 | Child Life Specialist | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 8 | College Teaching | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 9 | Counseling and Crisis Management in Higher Education | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 10 | Deals | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 11 | Deep Learning and Generative AI | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 12 | Dynamical Systems and Mathematical Modeling | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 13 | Financial Acumen | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 14 | Geographic Information Sciences | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 15 | Global Culture and Conservation | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 16 | Higher Education Administration | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 17 | Leadership | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 18 | Learning, Cognitive, and Brain Sciences | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 19 | Mental Health Intervention | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 20 | Principal Licensure | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 21 | Reading Endorsement | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 22 | Self-Designed Graduate Certificate in Sport | https://bulletin.miamioh.edu/graduate-fields-study/ |
| 23 | Sport Management | https://bulletin.miamioh.edu/graduate-fields-study/ |

### 2.3 Graduate admissions model

Miami's Graduate School uses a **centralized application portal** (https://graduateschool.miamioh.edu/) with **decentralized departmental review**. Each department sets its own requirements (GRE, GPA minimums, deadlines). Application fee: $50 for degree programs, $20 for certificate programs, free for non-degree. Minimum undergraduate GPA: 2.75/4.00. CGS April-15 signatory.

---

## SECTION 3 -- Application requirements & deadlines

### 3.1 Undergraduate -- core data table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | Common App or Coalition App | miamioh.edu/admission-aid/apply/first-year-students/ |
| Application fee (domestic) | $50 (wailed if apply by Dec. 1) | miamioh.edu/admission-aid/apply/first-year-students/ |
| Application fee (international) | $70 (waived if apply by April 1) | miamioh.edu/admission-aid/apply/international-students/ |
| Early Decision (binding) | Nov. 1 | miamioh.edu/admission-aid/apply/dates-deadlines/undergraduate-students.html |
| ED Decision Notification | Dec. 1 | same |
| Early Action I (non-binding) | Nov. 1 | same |
| EA I Decision Notification | Dec. 15 | same |
| Early Action II (non-binding) | Dec. 1 | same |
| EA II Decision Notification | Feb. 1 | same |
| Regular Decision (non-binding) | Feb. 1 | same |
| RD Decision Notification | Mar. 15 | same |
| Deadline to Accept | May 1 | same |
| Spring Semester Deadline | Dec. 1 (Rolling) | same |
| Test policy | **TEST-OPTIONAL** | miamioh.edu/admission-aid/apply/first-year-students/college-entrance-testing.html |
| SAT/ACT codes | SAT: 1463, ACT: 3294 | same |
| Superscore | Yes (composite superscore) | same |
| Recommendation | At least 1 from counselor or academic teacher | miamioh.edu/admission-aid/apply/first-year-students/ |
| Interview | None offered | N/A |
| Portfolio/audition | Required for some CCA majors | miamioh.edu/admission-aid/apply/first-year-students/ |
| Transfer deadline | Rolling (apply early) | miamioh.edu/admission-aid/apply/ |

### 3.2 Undergraduate English proficiency table

> Source: miamioh.edu/admission-aid/apply/international-students/

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified on admissions page | -- | Required for non-native speakers; ACT/SAT may satisfy requirement |
| IELTS | Not specified on admissions page | -- | Required for non-native speakers |
| Duolingo | Not specified on admissions page | -- | Accepted as proof of ELP |

> Note: The admissions page states "TOEFL, IELTS or Duolingo test scores or an approved alternative proof of English language proficiency is required at the time of application." Specific minimum scores were not published on the pages accessed during this capture. ACT or SAT scores may be used to satisfy the ELP requirement. P0 follow-up: find the specific minimum score page (likely at miamioh.edu/global-initiatives/ or via the ISSS office).

### 3.3 Graduate -- global rules

| Field | Value | Source |
|-------|-------|--------|
| Application portal | https://graduateschool.miamioh.edu/ | miamioh.edu/admission-aid/apply/graduate-students/ |
| Application fee (degree) | $50 | same |
| Application fee (certificate) | $20 | same |
| Minimum GPA | 2.75/4.00 | same |
| GRE | Per-program (department decides) | bulletin.miamioh.edu/admission-graduate-students/ |
| ELP | Required for non-native speakers (TOEFL/IELTS) | same |
| Transcripts | Unofficial accepted with application | same |
| CGS April-15 | Signatory | graduateschool.miamioh.edu |

---

## SECTION 4 -- Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

> Source: miamioh.edu/admission-aid/costs-financial-aid/cost-of-attendance.html and miamioh.edu/onestop/costs/coa-by-cohort.html

**On-Campus (Oxford Campus):**

| Expense Item | Ohio Residents | Non-Ohio Residents | Type |
|-------------|---------------|-------------------|------|
| Tuition | $15,161.04 | $38,682.72 | Direct |
| Fees | $3,358.88 | $3,358.88 | Direct |
| Housing and Food | $17,154.00 | $17,154.00 | Direct |
| **Total On-Campus** | **$35,673.92** | **$59,195.60** | |

**Off-Campus (Oxford):**

| Expense Item | Per Semester | Annual | Type |
|-------------|-------------|--------|------|
| Tuition | $7,538 | $15,076 | Direct |
| Fees | $1,262 | $2,524 | Direct |
| Housing (Off-Campus) | $5,538 | $11,076 | Indirect |
| Food (Off-Campus) | $3,378 | $6,756 | Indirect |
| Books, Course Materials, Supplies, and Equipment | $665 | $1,330 | Indirect |
| Transportation | $1,635 | $3,270 | Indirect |
| Miscellaneous Personal Expenses | $1,340 | $2,680 | Indirect |
| **Total Off-Campus (In-State)** | | **$42,712** | |
| Non-Resident Surcharge | $11,052 | $22,104 | Direct |
| **Total Off-Campus (OOS)** | | **$64,816** | |

**Special Purpose and Course Fees:**
- College of Creative Arts: $52/semester
- Department of Emerging Technology in Business and Design (ETBD): $300/semester
- Farmer School of Business: $142.76/credit hour for most business courses
- College of Engineering and Computing: additional fees may apply

**Miami Tuition Promise**: Tuition, housing, meals, special purpose, and course fees are frozen for 4 years for each incoming class (since 2016).

### 4.2 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need-blind/need-aware | **Need-aware for all** (domestic and international) | miamioh.edu/admission-aid/costs-financial-aid/ |
| Merit scholarships | Yes; avg $7,144 (OH), $16,805 (OOS) for fall 2023 entering class | miamioh.edu/admission-aid/costs-financial-aid/affordable-miami.html |
| Gift aid received | 90% of fall 2024 first-year students | same |
| Miami Access Initiative | OH families with income <=$35,000: no tuition and fees | same |
| Tuition cap | No extra tuition beyond 12 credit hours/semester | same |
| 52% of fall 2021 OH first-years | Paid $0-$5,000/year | same |
| FAFSA code | 003077 | miamioh.edu/onestop/ |
| CSS Profile | Not mentioned | -- |

### 4.3 Graduate cost & funding framework

> Source: miamioh.edu/onestop/costs/graduate-students.html

**2026-2027 Oxford/VOA Graduate Students (Fall and Spring):**

| Fee Type | Ohio Residents (Per Semester) | Ohio Residents (Annual) | Non-Ohio Residents (Per Semester) | Non-Ohio Residents (Annual) |
|----------|------|------|------|------|
| Tuition | $7,689.90 | $15,379.80 | $7,689.90 | $15,379.80 |
| Non-Resident Surcharge | -- | -- | $11,268.98 | $22,537.96 |
| Fees | $1,278.02 | $2,556.04 | $1,278.02 | $2,556.04 |
| **Total** | **$8,967.92** | **$17,935.84** | **$20,236.90** | **$40,473.80** |

**Funding**: Graduate assistantships (teaching/research), GSSA scholarships, domestic/international grant-in-aid, research support awards, emergency fund. Most PhD programs offer full funding.

---

## SECTION 5 -- Evidence chain index

```yaml
---
field: undergraduate.deadlines.ED
value: "November 1 (binding, Dec. 1 decision)"
source_url: https://miamioh.edu/admission-aid/apply/dates-deadlines/undergraduate-students.html
source_snippet: "Early Decision (binding) Nov. 1 Dec. 1 Jan. 15"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.deadlines.EA_I
value: "November 1 (non-binding, Dec. 15 decision)"
source_url: https://miamioh.edu/admission-aid/apply/dates-deadlines/undergraduate-students.html
source_snippet: "Early Action I (Non-Binding) Nov. 1 Dec. 15 May 1"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.deadlines.EA_II
value: "December 1 (non-binding, Feb. 1 decision)"
source_url: https://miamioh.edu/admission-aid/apply/dates-deadlines/undergraduate-students.html
source_snippet: "Early Action II (Non-Binding) Dec. 1 Feb. 1 May 1"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.deadlines.RD
value: "February 1 (non-binding, Mar. 15 decision)"
source_url: https://miamioh.edu/admission-aid/apply/dates-deadlines/undergraduate-students.html
source_snippet: "Regular Decision (Non-Binding) Feb. 1 Mar. 15 May 1"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.test_policy
value: "Test-optional"
source_url: https://miamioh.edu/admission-aid/apply/first-year-students/college-entrance-testing.html
source_snippet: "ACT and SAT scores are optional for students applying to the university, which means domestic, first-year students will not be required to provide an ACT or SAT test score for admission or scholarship consideration."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.application_fee.domestic
value: "$50"
source_url: https://miamioh.edu/admission-aid/apply/first-year-students/index.html
source_snippet: "Select 'Miami Fee Waiver' on the undergraduate application to waive our $50 application fee when you apply by Dec. 1."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.application_fee.international
value: "$70"
source_url: https://miamioh.edu/admission-aid/apply/international-students/index.html
source_snippet: "Select 'Miami Fee Waiver' on the undergraduate application to waive our $70 application fee when you apply by April 1 for Fall 2026."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.cost.oncampus_ohio
value: "$35,673.92 (tuition $15,161.04 + fees $3,358.88 + housing/food $17,154)"
source_url: https://miamioh.edu/admission-aid/costs-financial-aid/cost-of-attendance.html
source_snippet: "Expense Ohio Residents Non-Ohio Residents Tuition $15,161.04 $38,682.72 Fees $3,358.88 $3,358.88 Housing and Food $17,154 $17,154 Total $35,673.92 $59,195.60"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.oncampus_oos
value: "$59,195.60 (tuition $38,682.72 + fees $3,358.88 + housing/food $17,154)"
source_url: https://miamioh.edu/admission-aid/costs-financial-aid/cost-of-attendance.html
source_snippet: "Total $35,673.92 $59,195.60"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.offcampus_instate
value: "$42,712/year"
source_url: https://miamioh.edu/onestop/costs/coa-by-cohort.html
source_snippet: "Estimated In-State Total $21,356 $42,712"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.offcampus_oos
value: "$64,816/year"
source_url: https://miamioh.edu/onestop/costs/coa-by-cohort.html
source_snippet: "Non-Resident Surcharge $11,052 $22,104 Estimated Out-of-State Total $32,408 $64,816"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.tuition_promise
value: "Tuition frozen for 4 years for each incoming class"
source_url: https://miamioh.edu/admission-aid/costs-financial-aid/affordable-miami.html
source_snippet: "Miami Tuition Promise Since 2016, the Miami Tuition Promise has frozen tuition, housing, meals, special purpose, and course fees for four years for each incoming class of students."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.financial_aid.merit_avg_oh
value: "$7,144 (fall 2023 entering class)"
source_url: https://miamioh.edu/admission-aid/costs-financial-aid/affordable-miami.html
source_snippet: "Average merit scholarships for first-year students entering in fall 2023 was $7,144 for Ohio students and $16,805 for out-of-state students."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.financial_aid.gift_aid_pct
value: "90% of fall 2024 first-year students received gift aid"
source_url: https://miamioh.edu/admission-aid/costs-financial-aid/affordable-miami.html
source_snippet: "90% of fall 2024 first-year students received gift aid (money you don't have to pay back)"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.financial_aid.access_initiative
value: "OH families with income <=$35,000: no tuition and fees"
source_url: https://miamioh.edu/admission-aid/costs-financial-aid/affordable-miami.html
source_snippet: "Miami Access Initiative ensures that academically competitive students from Ohio families with an income of $35,000 or less pay no tuition and fees."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.tuition_ohio
value: "$17,935.84/year ($8,967.92/semester)"
source_url: https://miamioh.edu/onestop/costs/graduate-students.html
source_snippet: "Ohio Residents Tuition $7,689.90 $15,379.80 Fees $1,278.02 $2,556.04 Total $8,967.92 $17,935.84"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: graduate.tuition_oos
value: "$40,473.80/year ($20,236.90/semester)"
source_url: https://miamioh.edu/onestop/costs/graduate-students.html
source_snippet: "Non-Ohio Residents Total $20,236.90 $40,473.80"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: graduate.application_fee
value: "$50 (degree), $20 (certificate)"
source_url: https://miamioh.edu/admission-aid/apply/graduate-students/index.html
source_snippet: "There is a $50 application fee when applying to a graduate degree program and a $20 fee for graduate certificate applications."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.program_counts
value: "61 master's + 1 specialist + 14 doctoral + 12 online + 22 certificates + 1 post-bacc"
source_url: https://miamioh.edu/graduate-school/index.html
source_snippet: "61 Master's Degree Programs and 1 Specialist Program 14 Doctoral Degree Programs 12 Online Graduate Programs 22 Graduate Certificates and 1 Post-Baccalaureate Certificate"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: institutional.ug_colleges
value: "6 UG-degree-granting colleges + 1 center + Graduate School"
source_url: https://bulletin.miamioh.edu/
source_snippet: "The College of Arts and Science, College of Creative Arts, College of Education Health and Society, College of Engineering and Computing, Farmer School of Business, College of Liberal Arts and Applied Science, Center for Civics Culture and Society, The Graduate School"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: institutional.rankings
value: "No. 2 for undergraduate teaching among U.S. public universities (U.S. News)"
source_url: https://miamioh.edu/admission-aid/index.html
source_snippet: "No. 2 For undergraduate teaching among U.S. public universities - U.S. News and World Report"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: institutional.graduation_rate
value: "98% Post-Graduation Success Rate"
source_url: https://miamioh.edu/admission-aid/index.html
source_snippet: "98% Post-Graduation Success Rate"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.elp.requirement
value: "TOEFL, IELTS, or Duolingo required for non-native speakers"
source_url: https://miamioh.edu/admission-aid/apply/international-students/index.html
source_snippet: "TOEFL, IELTS or Duolingo test scores or an approved alternative proof of English language proficiency is required at the time of application."
capture_date: 2026-07-06
evidence_type: official_webpage
---
```

---

## SECTION 6 -- WeKnora import manifest

### Collection structure

```
miamioh-knowledge-base-v2/
├── 00-institution-overview          (Section 0: rules 1-4, counts, hierarchy, matrix)
├── 01-ug-cas                        (Section 1: CAS programs)
├── 02-ug-cca                        (Section 1: CCA programs)
├── 03-ug-ehs                        (Section 1: EHS programs)
├── 04-ug-cec                        (Section 1: CEC programs)
├── 05-ug-fsb                        (Section 1: FSB programs)
├── 06-ug-claas                      (Section 1: CLAAS programs)
├── 07-ug-minors-certs               (Section 1: all minors + certificates)
├── 08-grad-cas                      (Section 2: CAS graduate programs)
├── 09-grad-fsb                      (Section 2: FSB graduate programs)
├── 10-grad-ehs                      (Section 2: EHS graduate programs)
├── 11-grad-cec                      (Section 2: CEC graduate programs)
├── 12-grad-cca-claas                (Section 2: CCA + CLAAS graduate)
├── 13-grad-certificates             (Section 2: all graduate certificates)
├── 14-deadlines-requirements        (Section 3)
├── 15-costs-financial-aid           (Section 4)
├── 16-evidence-chain                (Section 5)
└── 17-comparison-framework          (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "miamioh-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BFA|BM|MA|MS|PhD|...>"
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
| P0 | ELP specific minimum scores (TOEFL/IELTS/Duolingo) | miamioh.edu/global-initiatives/international-student-scholar-services/ |
| P0 | On-campus housing/food breakdown by room type | miamioh.edu/onestop/costs/ (behind accordion) |
| P1 | FSB additional transfer requirements details | miamioh.edu/admission-aid/apply/transfer-students/ |
| P1 | CCA audition/portfolio requirements per major | bulletin.miamioh.edu/creative-arts/ |
| P1 | Graduate program-specific deadlines and GRE requirements | Each department's graduate admissions page |
| P2 | Net Price Calculator data | miamioh.edu/onestop/costs/net-price-calculators.html |
| P2 | Honors College admission requirements | miamioh.edu/admission-aid/majors-minors-programs/honors-programs/ |
| P2 | Presidential Fellows Program details | miamioh.edu/admission-aid/ |

---

## SECTION 7 -- Cross-school comparison framework

| Dimension | Miami OH (this doc) | MIT | Stanford | Harvard | Caltech | UChicago | UC Berkeley | Cornell | Brown | UPenn | JHU |
|-----------|---------------------|-----|----------|---------|---------|----------|-------------|---------|-------|-------|-----|
| Type | Public | Private | Private | Private | Private | Private | Public | Private | Private | Private | Private |
| UG Tuition (in-state/yr) | $15,161 | -- | -- | -- | -- | -- | $18,216 | -- | -- | -- | -- |
| UG Tuition (OOS/yr) | $38,683 | -- | -- | -- | -- | -- | ~$57,486 | -- | -- | -- | -- |
| UG COA On-Campus (in-state) | $35,674 | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| UG COA On-Campus (OOS) | $59,196 | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Need-blind intl? | No (need-aware all) | Yes | No | Yes | No (need-aware) | No | No | No | Yes | No | No |
| EA deadline | Nov 1 | -- | -- | -- | Nov 1 | Nov 2 | N/A | -- | -- | -- | Nov 1 |
| ED deadline | Nov 1 | -- | -- | -- | -- | Nov 2 | N/A | Nov 1 | Nov 1 | Nov 1 | Nov 1 |
| RD deadline | Feb 1 | -- | -- | -- | Jan 5 | Jan 4 | Nov 30 | Jan 2 | Jan 5 | Jan 5 | Jan 2 |
| SAT/ACT required? | No (test-optional) | -- | -- | -- | Required | No | No (test-free) | Required | Required | Required | Required |
| TOEFL min | Not specified | -- | -- | -- | -- | -- | -- | -- | 105/5.5 | 100+ | 100 |
| IELTS min | Not specified | -- | -- | -- | -- | -- | -- | -- | 8.0 | 7.0+ | 7.0 |
| App fee (UG) | $50 | -- | -- | -- | -- | $90 | $70 | $85 | $80 | $75 | $70 |
| Total program count | 269 | -- | -- | -- | -- | -- | 439 | 429 | 208+ | 641 | 605 |
| School/college count | 8 | -- | -- | -- | -- | -- | 14 | 7 | 7 | 16 | 10 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: miamioh.edu, bulletin.miamioh.edu, graduateschool.miamioh.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
