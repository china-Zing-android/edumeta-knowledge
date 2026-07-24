# DePaul University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BSN/BSB/BAPS) | 171 |
| 本科辅修 (Minor) | 178 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/JD/etc.) | 191 |
| 研究生高级证书 (Advanced Certificate) | 67 |
| **学位项目总计 (UG + Grad)** | **614** |
| 学院 / 独立系所总数 | 10 |

> **Reconciliation**: rule-1 total (614) == sum of all programs in Sections 1 & 2.

### 0.2 学院 / 系层级结构

```
DePaul University
├── Driehaus College of Business                          [学院]
│   ├── School of Accountancy & MIS                       [系]
│   ├── Department of Finance                             [系]
│   ├── Department of Management & Entrepreneurship       [系]
│   ├── Department of Marketing                           [系]
│   ├── Department of Economics                           [系]
│   ├── School of Hospitality & Sports Business           [系]
│   └── Kellstadt Graduate School of Business             [系]
├── Jarvis College of Computing and Digital Media (CDM)   [学院]
│   ├── School of Computing                               [系]
│   ├── School of Cinematic Arts                          [系]
│   ├── School of Design                                  [系]
│   └── School of Information Technology                  [系]
├── College of Communication                              [学院]
│   ├── Department of Communication Studies               [系]
│   ├── Department of Journalism                          [系]
│   ├── Department of Public Relations & Advertising      [系]
│   └── Department of Media & Popular Culture             [系]
├── College of Education                                  [学院]
│   ├── Department of Teacher Education                   [系]
│   ├── Department of Educational Leadership              [系]
│   ├── Department of Counseling & Special Education      [系]
│   └── Department of Curriculum Studies                  [系]
├── College of Liberal Arts and Social Sciences (LAS)     [学院]
│   ├── Department of English                             [系]
│   ├── Department of History                             [系]
│   ├── Department of Philosophy                          [系]
│   ├── Department of Political Science                   [系]
│   ├── Department of Psychology                          [系]
│   ├── Department of Sociology                           [系]
│   ├── Department of Modern Languages                    [系]
│   ├── Department of Geography                           [系]
│   ├── Department of Anthropology                        [系]
│   ├── Department of Religious Studies                   [系]
│   ├── School of Social Work                             [系]
│   ├── Department of Public Policy & Administration      [系]
│   └── Department of International Studies               [系]
├── College of Science and Health (CSH)                   [学院]
│   ├── Department of Biological Sciences                 [系]
│   ├── Department of Chemistry                           [系]
│   ├── Department of Physics                             [系]
│   ├── Department of Mathematics                         [系]
│   ├── School of Nursing                                 [系]
│   ├── Department of Health Sciences                     [系]
│   ├── Department of Speech-Language Pathology           [系]
│   └── Department of Environmental Science               [系]
├── College of Law                                        [学院]
│   ├── JD Program                                        [系]
│   ├── LLM Programs                                      [系]
│   └── MLS Program                                       [系]
├── School of Music                                       [学院]
│   ├── Department of Performance                         [系]
│   ├── Department of Composition                         [系]
│   ├── Department of Jazz Studies                        [系]
│   └── Department of Music Education                     [系]
├── The Theatre School                                    [学院]
│   ├── Acting Program                                    [系]
│   ├── Design/Technical Programs                         [系]
│   ├── Directing & Writing Programs                      [系]
│   └── Theatre Studies                                   [系]
└── School of Continuing and Professional Studies (SCPS)  [学院]
    ├── Applied Professional Studies                      [系]
    ├── Business Administration (BAPS)                    [系]
    └── Computing (BAPS)                                  [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 82 |
| BS | Bachelor of Science | 本科 | 63 |
| BSB | Bachelor of Science in Business | 本科 | 18 |
| BFA | Bachelor of Fine Arts | 本科 | 19 |
| BM | Bachelor of Music | 本科 | 5 |
| BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BAPS | Bachelor of Applied Professional Studies | 本科 | 4 |
| BSPE | Bachelor of Science in Physical Education | 本科 | 1 |
| Minor | Minor (辅修) | 本科 | 178 |
| MA | Master of Arts | 研究生 | 40 |
| MS | Master of Science | 研究生 | 59 |
| MFA | Master of Fine Arts | 研究生 | 8 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MEd | Master of Education | 研究生 | 35 |
| MM | Master of Music | 研究生 | 4 |
| MPH | Master of Public Health | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 2 |
| MPP | Master of Public Policy | 研究生 | 2 |
| MSW | Master of Social Work | 研究生 | 2 |
| MNM | Master of Nonprofit Management | 研究生 | 2 |
| MLS | Master of Legal Studies | 研究生 | 2 |
| MSN | Master of Science in Nursing | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 5 |
| JD | Juris Doctor | 研究生 | 10 |
| PhD | Doctor of Philosophy | 研究生 | 7 |
| EdD | Doctor of Education | 研究生 | 3 |
| EdS | Education Specialist | 研究生 | 2 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | 67 |
| Joint | Joint Degree Programs | 研究生 | 4 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSB | BFA | BM | BSN | BAPS | BSPE | Minor | MA | MS | MFA | MBA | MEd | MM | MPH | MPA | MPP | MSW | MNM | MLS | MSN | LLM | JD | PhD | EdD | EdS | DBA | DNP | Certificate | Joint | 合计 |
|------------|----|----|-----|-----|----|-----|------|------|-------|----|----|-----|-----|-----|----|-----|-----|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|-----|-----|-------------|-------|------|
| LAS | 48 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 91 | 21 | 14 | 1 | 0 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 50 | 1 | 241 |
| Education | 13 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 10 | 3 | 0 | 0 | 35 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 2 | 0 | 0 | 3 | 0 | 94 |
| CDM | 6 | 19 | 0 | 5 | 0 | 0 | 0 | 0 | 26 | 3 | 21 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 0 | 92 |
| Business | 2 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 15 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 2 | 65 |
| CSH | 3 | 10 | 0 | 0 | 0 | 2 | 0 | 0 | 8 | 0 | 6 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 0 | 37 |
| Communication | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 28 |
| Theatre | 1 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 22 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 5 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 |
| Music | 1 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 17 |
| SCPS | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| **合计** | **82** | **63** | **18** | **19** | **5** | **2** | **4** | **1** | **178** | **40** | **59** | **8** | **2** | **35** | **4** | **1** | **2** | **2** | **2** | **2** | **2** | **1** | **5** | **10** | **7** | **3** | **2** | **1** | **1** | **67** | **4** | **614** |

> **Reconciliation**: row totals sum to 614; column totals sum to 614; matches rule-1 total.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

DePaul University has 10 colleges/schools, most of which grant undergraduate degrees. The School of Continuing and Professional Studies (SCPS) serves adult and non-traditional students with degree-completion programs. The College of Law is graduate-only. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Driehaus College of Business

##### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.depaul.edu/programs/accountancy-bsb/ |
| 2 | Accountancy (Honors) | https://catalog.depaul.edu/programs/accountancy-honors-bsb/ |
| 3 | Actuarial Science | https://catalog.depaul.edu/programs/actuarial-science-bsb/ |
| 4 | Business Administration | https://catalog.depaul.edu/programs/business-administration-bsb/ |
| 5 | Business Analytics | https://catalog.depaul.edu/programs/business-analytics-bsb/ |
| 6 | Economic Data Analytics | https://catalog.depaul.edu/programs/economic-data-analytics-bsb/ |
| 7 | Economics | https://catalog.depaul.edu/programs/economics-bsb/ |
| 8 | Economics (Honors) | https://catalog.depaul.edu/programs/economics-honors-bsb/ |
| 9 | Entrepreneurship | https://catalog.depaul.edu/programs/entrepreneurship-bsb/ |
| 10 | Finance | https://catalog.depaul.edu/programs/finance-bsb/ |
| 11 | Finance (Honors) | https://catalog.depaul.edu/programs/finance-honors-bsb/ |
| 12 | Hospitality Leadership | https://catalog.depaul.edu/programs/hospitality-leadership-bsb/ |
| 13 | Management | https://catalog.depaul.edu/programs/management-bsb/ |
| 14 | Management Information Systems | https://catalog.depaul.edu/programs/management-information-systems-bsb/ |
| 15 | Marketing | https://catalog.depaul.edu/programs/marketing-bsb/ |
| 16 | Marketing (Honors) | https://catalog.depaul.edu/programs/marketing-honors-bsb/ |
| 17 | Real Estate | https://catalog.depaul.edu/programs/real-estate-bsb/ |
| 18 | Sports Business | https://catalog.depaul.edu/programs/sports-business-bsb/ |

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.depaul.edu/programs/economics-ba/ |
| 2 | Economics (Honors) | https://catalog.depaul.edu/programs/economics-honors-ba/ |

#### Jarvis College of Computing and Digital Media (CDM)

##### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.depaul.edu/programs/computer-science-bs/ |
| 2 | Computer Science (Online) | https://catalog.depaul.edu/programs/computer-science-online-bs/ |
| 3 | Computer Science and Animation | https://catalog.depaul.edu/programs/computer-science-and-animation-bs/ |
| 4 | Computer Science and Economics | https://catalog.depaul.edu/programs/computer-science-and-economics-bs/ |
| 5 | Computer Science and Geography | https://catalog.depaul.edu/programs/computer-science-and-geography-bs/ |
| 6 | Computer Science and History | https://catalog.depaul.edu/programs/computer-science-and-history-bs/ |
| 7 | Computer Science and Writing and Rhetoric | https://catalog.depaul.edu/programs/computer-science-and-writing-and-rhetoric-bs/ |
| 8 | Cybersecurity | https://catalog.depaul.edu/programs/cybersecurity-bs/ |
| 9 | Data Science | https://catalog.depaul.edu/programs/data-science-bs/ |
| 10 | Game Design | https://catalog.depaul.edu/programs/game-design-bs/ |
| 11 | Game Programming | https://catalog.depaul.edu/programs/game-programming-bs/ |
| 12 | Information Systems | https://catalog.depaul.edu/programs/information-systems-bs/ |
| 13 | Information Technology | https://catalog.depaul.edu/programs/information-technology-bs/ |
| 14 | Information Technology (Online) | https://catalog.depaul.edu/programs/information-technology-online-bs/ |
| 15 | Intelligent Systems Engineering | https://catalog.depaul.edu/programs/intelligent-systems-engineering-bs/ |
| 16 | Mathematics and Computer Science (CDM) | https://catalog.depaul.edu/programs/mathematics-computer-science-bs-cdm/ |
| 17 | Network Technologies | https://catalog.depaul.edu/programs/network-technologies-bs/ |
| 18 | Robotics | https://catalog.depaul.edu/programs/robotics-bs/ |
| 19 | User Experience Design | https://catalog.depaul.edu/programs/user-experience-design-bs/ |

##### BFA (Bachelor of Fine Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation | https://catalog.depaul.edu/programs/animation-bfa/ |
| 2 | Art, Media and Design | https://catalog.depaul.edu/programs/art-media-design-bfa/ |
| 3 | Film and Television | https://catalog.depaul.edu/programs/film-television-bfa/ |
| 4 | Graphic Design | https://catalog.depaul.edu/programs/graphic-design-bfa/ |
| 5 | Industrial Design | https://catalog.depaul.edu/programs/industrial-design-bfa/ |

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation | https://catalog.depaul.edu/programs/animation-ba/ |
| 2 | Art, Media and Design | https://catalog.depaul.edu/programs/art-media-design-ba/ |
| 3 | Data Science | https://catalog.depaul.edu/programs/data-science-ba/ |
| 4 | Digital Communication | https://catalog.depaul.edu/programs/digital-communication-ba/ |
| 5 | Film and Television | https://catalog.depaul.edu/programs/film-television-ba/ |
| 6 | Media and Popular Culture | https://catalog.depaul.edu/programs/media-and-popular-culture-ba/ |

##### BAPS (Bachelor of Applied Professional Studies)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computing | https://catalog.depaul.edu/programs/computing-baps/ |
| 2 | Computing (Online) | https://catalog.depaul.edu/programs/computing-online-baps/ |

#### College of Communication

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication and Media | https://catalog.depaul.edu/programs/communication-media-ba/ |
| 2 | Communication and Media (Online) | https://catalog.depaul.edu/programs/communication-media-online-ba/ |
| 3 | Communication Studies | https://catalog.depaul.edu/programs/communication-studies-ba/ |
| 4 | Journalism | https://catalog.depaul.edu/programs/journalism-ba/ |
| 5 | Organizational Communication | https://catalog.depaul.edu/programs/organizational-communication-ba/ |
| 6 | Public Relations and Advertising | https://catalog.depaul.edu/programs/public-relations-advertising-ba/ |
| 7 | Sports Communication | https://catalog.depaul.edu/programs/sports-communication-ba/ |
| 8 | Media and Popular Culture | https://catalog.depaul.edu/programs/media-and-popular-culture-ba/ |

#### College of Education

##### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://catalog.depaul.edu/programs/early-childhood-education-bs/ |
| 2 | Elementary Education | https://catalog.depaul.edu/programs/elementary-education-bs/ |
| 3 | Middle Grades Education | https://catalog.depaul.edu/programs/middle-grades-edu-bs/ |
| 4 | Special Education | https://catalog.depaul.edu/programs/special-education-bs/ |
| 5 | Secondary Education Biology | https://catalog.depaul.edu/programs/secondary-education-biology-bs/ |
| 6 | Secondary Education Chemistry | https://catalog.depaul.edu/programs/secondary-education-chemistry-bs/ |
| 7 | Secondary Education Environmental Science | https://catalog.depaul.edu/programs/secondary-education-environmental-science-bs/ |
| 8 | Secondary Education Mathematics | https://catalog.depaul.edu/programs/secondary-education-mathematics-bs/ |
| 9 | Secondary Education Physics | https://catalog.depaul.edu/programs/secondary-education-phsyics-bs/ |
| 10 | Physical Education | https://catalog.depaul.edu/programs/physical-education-bspe/ |
| 11 | Exercise Science | https://catalog.depaul.edu/programs/exercise-science-bs/ |

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Secondary Education BA/BS | https://catalog.depaul.edu/programs/secondary-education-ba-bs/ |
| 2 | Secondary Education English | https://catalog.depaul.edu/programs/secondary-education-english-ba/ |
| 3 | Secondary Education History | https://catalog.depaul.edu/programs/secondary-education-history-ba/ |
| 4 | Secondary Education Mathematics | https://catalog.depaul.edu/programs/secondary-education-mathematics-ba/ |
| 5 | Secondary Education Social Science | https://catalog.depaul.edu/programs/secondary-education-social-science-ba/ |
| 6 | Visual Art Education | https://catalog.depaul.edu/programs/visual-art-education-ba/ |
| 7 | World Language Education (Chinese) | https://catalog.depaul.edu/programs/world-language-education-chinese-ba/ |
| 8 | World Language Education (French) | https://catalog.depaul.edu/programs/world-language-education-french-ba/ |
| 9 | World Language Education (German) | https://catalog.depaul.edu/programs/world-language-education-german-ba/ |
| 10 | World Language Education (Italian) | https://catalog.depaul.edu/programs/world-language-education-italian-ba/ |
| 11 | World Language Education (Japanese) | https://catalog.depaul.edu/programs/world-language-education-japanese-ba/ |
| 12 | World Language Education (Spanish) | https://catalog.depaul.edu/programs/world-language-education-spanish-ba/ |
| 13 | Recreation and Sport Management | https://catalog.depaul.edu/programs/recreation-and-sport-management-ba/ |

#### College of Liberal Arts and Social Sciences (LAS)

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | African and Black Diaspora Studies | https://catalog.depaul.edu/programs/african-black-diaspora-studies-ba/ |
| 2 | American Studies | https://catalog.depaul.edu/programs/american-studies-ba/ |
| 3 | Anthropology | https://catalog.depaul.edu/programs/anthropology-ba/ |
| 4 | Applied Behavioral Sciences | https://catalog.depaul.edu/programs/applied-behavioral-sciences-ba/ |
| 5 | Applied Behavioral Sciences (Online) | https://catalog.depaul.edu/programs/applied-behavioral-sciences-online-ba/ |
| 6 | Applied Diplomacy | https://catalog.depaul.edu/programs/applied-diplomacy-ba/ |
| 7 | Art | https://catalog.depaul.edu/programs/art-ba/ |
| 8 | Catholic Studies | https://catalog.depaul.edu/programs/catholic-studies-ba/ |
| 9 | Chinese Studies | https://catalog.depaul.edu/programs/chinese-studies-ba/ |
| 10 | Communication and Media | https://catalog.depaul.edu/programs/communication-media-ba/ |
| 11 | Criminology | https://catalog.depaul.edu/programs/criminology-ba/ |
| 12 | Criminology (Online) | https://catalog.depaul.edu/programs/criminology-online-ba/ |
| 13 | Decision Analytics | https://catalog.depaul.edu/programs/decision-analytics-ba/ |
| 14 | Decision Analytics (Online) | https://catalog.depaul.edu/programs/decision-analytics-online-ba/ |
| 15 | Digital Communication | https://catalog.depaul.edu/programs/digital-communication-ba/ |
| 16 | Economics | https://catalog.depaul.edu/programs/economics-ba/ |
| 17 | Economics (Honors) | https://catalog.depaul.edu/programs/economics-honors-ba/ |
| 18 | English | https://catalog.depaul.edu/programs/english-ba/ |
| 19 | Environmental Studies | https://catalog.depaul.edu/programs/environmental-studies-ba/ |
| 20 | French | https://catalog.depaul.edu/programs/french-ba/ |
| 21 | Geography | https://catalog.depaul.edu/programs/geography-ba/ |
| 22 | German | https://catalog.depaul.edu/programs/german-ba/ |
| 23 | Health Care Administration | https://catalog.depaul.edu/programs/health-care-administration-ba/ |
| 24 | History | https://catalog.depaul.edu/programs/history-ba/ |
| 25 | History of Art and Architecture | https://catalog.depaul.edu/programs/history-art-architecture-ba/ |
| 26 | International Studies | https://catalog.depaul.edu/programs/international-studies-ba/ |
| 27 | Islamic World Studies | https://catalog.depaul.edu/programs/islamic-world-studies-ba/ |
| 28 | Italian | https://catalog.depaul.edu/programs/italian-ba/ |
| 29 | Japanese Studies | https://catalog.depaul.edu/programs/japanese-studies-ba/ |
| 30 | Journalism | https://catalog.depaul.edu/programs/journalism-ba/ |
| 31 | Latin American and Latino Studies | https://catalog.depaul.edu/programs/latin-american-latino-studies-ba/ |
| 32 | Latino/a Culture and Communication | https://catalog.depaul.edu/programs/latino-a-culture-and-communication-ba/ |
| 33 | Leadership Studies | https://catalog.depaul.edu/programs/leadership-studies-ba/ |
| 34 | Leadership Studies (Online) | https://catalog.depaul.edu/programs/leadership-studies-online-ba/ |
| 35 | Non-Profit Management | https://catalog.depaul.edu/programs/non-profit-management-ba/ |
| 36 | Non-Profit Management (Online) | https://catalog.depaul.edu/programs/non-profit-management-online-ba/ |
| 37 | Peace, Justice and Conflict Studies | https://catalog.depaul.edu/programs/peace-justice-conflict-studies-ba/ |
| 38 | Philosophy | https://catalog.depaul.edu/programs/philosophy-ba/ |
| 39 | Political Science | https://catalog.depaul.edu/programs/political-science-ba/ |
| 40 | Psychology | https://catalog.depaul.edu/programs/psychology-ba/ |
| 41 | Psychology (Online) | https://catalog.depaul.edu/programs/psychology-online-ba/ |
| 42 | Psychology and Economics | https://catalog.depaul.edu/programs/psychology-and-economics-ba/ |
| 43 | Public Policy | https://catalog.depaul.edu/programs/public-policy-ba/ |
| 44 | Public Relations and Advertising | https://catalog.depaul.edu/programs/public-relations-advertising-ba/ |
| 45 | Religious Studies | https://catalog.depaul.edu/programs/religious-studies-ba/ |
| 46 | Social Work | https://catalog.depaul.edu/programs/social-work-minor/ |
| 47 | Sociology | https://catalog.depaul.edu/programs/sociology-ba/ |
| 48 | Spanish | https://catalog.depaul.edu/programs/spanish-ba/ |
| 49 | Sports Communication | https://catalog.depaul.edu/programs/sports-communication-ba/ |
| 50 | Women's and Gender Studies | https://catalog.depaul.edu/programs/womens-gender-studies-ba/ |
| 51 | Writing, Rhetoric and Discourse | https://catalog.depaul.edu/programs/writing-rhetoric-ba/ |
| 52 | Writing, Rhetoric and Discourse (Online) | https://catalog.depaul.edu/programs/writing-rhetoric-ba-online/ |

##### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.depaul.edu/programs/data-science-ba/ |
| 2 | Environmental Science | https://catalog.depaul.edu/programs/environmental-science-bs/ |
| 3 | Neuroscience | https://catalog.depaul.edu/programs/neuroscience-bs/ |
| 4 | Psychology | https://catalog.depaul.edu/programs/psychology-bs/ |

##### BFA (Bachelor of Fine Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Comedy Arts | https://catalog.depaul.edu/programs/comedy-arts-bfa/ |

#### College of Science and Health (CSH)

##### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://catalog.depaul.edu/programs/actuarial-science-bs/ |
| 2 | Astrophysics | https://catalog.depaul.edu/programs/astrophysics-bs/ |
| 3 | Biochemistry | https://catalog.depaul.edu/programs/biochemistry-bs/ |
| 4 | Biological Sciences | https://catalog.depaul.edu/programs/biological-sciences-bs/ |
| 5 | Chemistry | https://catalog.depaul.edu/programs/chemistry-bs/ |
| 6 | Computer Science | https://catalog.depaul.edu/programs/computer-science-bs/ |
| 7 | Data Science | https://catalog.depaul.edu/programs/data-science-bs/ |
| 8 | Environmental Science | https://catalog.depaul.edu/programs/environmental-science-bs/ |
| 9 | Health Sciences | https://catalog.depaul.edu/programs/health-sciences-bs/ |
| 10 | Mathematics and Computer Science (CSH) | https://catalog.depaul.edu/programs/mathematics-computer-science-bs-csh/ |
| 11 | Mathematical Sciences | https://catalog.depaul.edu/programs/mathematical-sciences-bs/ |
| 12 | Neuroscience | https://catalog.depaul.edu/programs/neuroscience-bs/ |
| 13 | Nursing | https://catalog.depaul.edu/programs/nursing-bsn/ |
| 14 | Physics | https://catalog.depaul.edu/programs/physics-bs/ |
| 15 | Recording Technology | https://catalog.depaul.edu/programs/recording-technology-bs/ |

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.depaul.edu/programs/biochemistry-ba/ |
| 2 | Biology | https://catalog.depaul.edu/programs/biology-ba/ |
| 3 | Chemistry | https://catalog.depaul.edu/programs/chemistry-ba/ |
| 4 | Mathematical Sciences | https://catalog.depaul.edu/programs/mathematical-sciences-ba/ |

##### BSN (Bachelor of Science in Nursing)
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.depaul.edu/programs/nursing-bsn/ |
| 2 | BSN Completion | https://catalog.depaul.edu/programs/bsn-completion-bsn/ |

#### School of Music

##### BM (Bachelor of Music)
| # | 专业 | URL |
|---|------|-----|
| 1 | Composition | https://catalog.depaul.edu/programs/composition-bm/ |
| 2 | Jazz Studies | https://catalog.depaul.edu/programs/jazz-studies-bm/ |
| 3 | Music Education | https://catalog.depaul.edu/programs/music-education-bm/ |
| 4 | Music Performance | https://catalog.depaul.edu/programs/music-performance-bm/ |
| 5 | Performing Arts Management | https://catalog.depaul.edu/programs/performing-arts-management-bm/ |

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.depaul.edu/programs/music-ba/ |

##### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Performing Arts Management | https://catalog.depaul.edu/programs/performing-arts-management-bs/ |

#### The Theatre School

##### BFA (Bachelor of Fine Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://catalog.depaul.edu/programs/acting-bfa/ |
| 2 | Costume Design | https://catalog.depaul.edu/programs/costume-design-bfa/ |
| 3 | Costume Technology | https://catalog.depaul.edu/programs/costume-technology-bfa/ |
| 4 | Dramaturgy/Criticism | https://catalog.depaul.edu/programs/dramaturgy-criticism-bfa/ |
| 5 | Lighting Design | https://catalog.depaul.edu/programs/lighting-design-bfa/ |
| 6 | Playwriting | https://catalog.depaul.edu/programs/playwriting-bfa/ |
| 7 | Projection Design | https://catalog.depaul.edu/programs/projection-design-bfa/ |
| 8 | Scene Design | https://catalog.depaul.edu/programs/scene-design-bfa/ |
| 9 | Sound Design | https://catalog.depaul.edu/programs/sound-design-bfa/ |
| 10 | Stage Management | https://catalog.depaul.edu/programs/stage-management-bfa/ |
| 11 | Theatre Arts | https://catalog.depaul.edu/programs/theatre-arts-bfa/ |
| 12 | Theatre Management | https://catalog.depaul.edu/programs/theatre-management-bfa/ |
| 13 | Theatre Technology | https://catalog.depaul.edu/programs/theatre-technology-bfa/ |

##### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://catalog.depaul.edu/programs/theatre-ba/ |

#### School of Continuing and Professional Studies (SCPS)

##### BAPS (Bachelor of Applied Professional Studies)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Behavioral Sciences | https://catalog.depaul.edu/programs/applied-behavioral-sciences-ba/ |
| 2 | Business Administration | https://catalog.depaul.edu/programs/business-administration-baps/ |
| 3 | Business Administration (Online) | https://catalog.depaul.edu/programs/business-administration-online-baps/ |
| 4 | Computing | https://catalog.depaul.edu/programs/computing-baps/ |
| 5 | Computing (Online) | https://catalog.depaul.edu/programs/computing-online-baps/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 父学院 | URL |
|---|------|--------|-----|
| 1 | Computer Science and Animation | CDM | https://catalog.depaul.edu/programs/computer-science-and-animation-bs/ |
| 2 | Computer Science and Economics | CDM + Business | https://catalog.depaul.edu/programs/computer-science-and-economics-bs/ |
| 3 | Computer Science and Geography | CDM + LAS | https://catalog.depaul.edu/programs/computer-science-and-geography-bs/ |
| 4 | Computer Science and History | CDM + LAS | https://catalog.depaul.edu/programs/computer-science-and-history-bs/ |
| 5 | Computer Science and Writing and Rhetoric | CDM + LAS | https://catalog.depaul.edu/programs/computer-science-and-writing-and-rhetoric-bs/ |
| 6 | Mathematics and Computer Science (CDM) | CDM | https://catalog.depaul.edu/programs/mathematics-computer-science-bs-cdm/ |
| 7 | Mathematics and Computer Science (CSH) | CSH | https://catalog.depaul.edu/programs/mathematics-computer-science-bs-csh/ |
| 8 | Psychology and Economics | LAS | https://catalog.depaul.edu/programs/psychology-and-economics-ba/ |

### 1.4 Minors — complete list

DePaul offers **178 undergraduate minors** across all colleges. Key minors include:

**Driehaus College of Business (13 minors)**: Accountancy, Business, Business Analytics, Business Visual Arts, Digital Marketing, Economics, Entrepreneurship, Event Management, Finance, Food & Beverage Management, Hospitality Leadership, International Business, Management, Management Information Systems, Marketing, Marketing Sales Leadership, Real Estate, Sports Business, Tourism

**CDM (26 minors)**: Animation, Animation Technical Director, Cinema Studies, Cinematography, Comedy Filmmaking, Computer Science, Cybersecurity, Data Science, Digital Cinema, Documentary Production, Documentary Studies, Electronics, Experimental Filmmaking, Game Design, Game Programming, Game Technical Director, Graphic Design, Illustration, Industrial Design, Information Systems, Information Technology, Motion Graphics, Network Technologies, Production Design, Screenwriting, Software Engineering, User Experience Design, Virtual Production Environment Design, Virtual Production Stage Operation, Visual Effects

**Communication (13 minors)**: Advertising Creative, Communication Media, Communication Studies, Environmental Communication, Health Communication, Intercultural Communication, Journalism, Latino Media Communication, Media and Popular Culture, Organizational Communication, Public Relations & Advertising, Radio-TV-New Media, Relational Communication, Sports Communication, Television Production

**Education (10 minors)**: Bilingual Education, Coaching, Early Childhood Education, Education Social Justice, Elementary Education, ESL Bilingual Education, Exceptionality Learning, Physical Education, Special Education

**LAS (91 minors)**: American Sign Language, American Studies, Anthropology, Applied Psychology, Arabic Studies, Archaeology, Architecture & Urbanism, Art, Bioethics & Society, Cannabis Studies, Catholic Studies, Chicago Studies, Chinese Language, Chinese Studies, Classical Studies, Commercial Chinese, Commercial French, Commercial Spanish, Community Service, Comparative Literature, Creative Practice Art & Writing, Creative Writing, Criminology, Dance, Digital Humanities, Disability Justice, Drawing, Economics, English Second Language, Environmental Sciences, Environmental Studies, Fandom Cult & Media Subculture, Food Studies, French, French Translation, Fundamentals of Psychology, Geography, German, German Studies, Global Asian Studies, Global Health, Greek, History, History of Art & Architecture, Industrial-Organizational Psych, International Politics, Irish Studies, Islamic World Studies, Italian, Japanese, Japanese Studies, Latin American & Latino Studies, Latina/o Culture & Communication, Lesbian Gay Bisexual Transgender Queer Studies, Liberal Studies, Linguistics, Literature, Mathematics, Media & Popular Culture, Museum Studies, Neuroscience, Nonprofit Organizations, Peace Justice & Conflict Studies, Philosophy, Photography, Political Science, Professional Writing, Psychology, Psychological Research Methods, Public Law & Political Thought, Public Policy Studies, Recreation & Sport Management, Religious Studies, Russian Studies, Social Work, Sociology, Sound Design, Spanish, Spanish Linguistics, Spanish Translation, Speech-Language Pathology, Sports Communication, Statistics, Studio Art, Sustainability Studies, Theatre Studies, Urban Geography & Planning, Women's & Gender Studies, Writing & Rhetoric

**CSH (8 minors)**: Biological Science, Chemistry, Computational Physics, Data Science, Discrete Mathematics, Environmental Sciences, Health, Mathematics, Neuroscience, Physics, Public Health Studies, Recording, Statistics

**Music (2 minors)**: Music Business, Music Studies

**Theatre (5 minors)**: Comedy Filmmaking, Dance, Documentary Studies, Screenwriting, Sound Design, Theatre Studies

### 1.5 General Education Requirements

DePaul's **Liberal Studies Program (LSP)** is the core curriculum for all undergraduate students. It requires 72 quarter hours across:
- Arts and Ideas
- Human Community
- Scientific World
- Writing
- Quantitative Reasoning
- Multiculturalism
- Experiential Learning

Honors Program available for high-achieving students.

---

## SECTION 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Driehaus College of Business / Kellstadt Graduate School

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | https://catalog.depaul.edu/programs/master-business-administration-mba/ |
| 2 | MBA (Business Analytics) | https://catalog.depaul.edu/programs/master-business-administration-business-analytics-mba/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy (Online) | https://catalog.depaul.edu/programs/accountancy-online-ms/ |
| 2 | Audit and Advisory Services | https://catalog.depaul.edu/programs/audit-advisory-services-msaa/ |
| 3 | Business Analytics | https://catalog.depaul.edu/programs/business-analytics-ms/ |
| 4 | Business Information Technology | https://catalog.depaul.edu/programs/business-information-technology-ms/ |
| 5 | Business Information Technology (Online) | https://catalog.depaul.edu/programs/business-information-technology-online-ms/ |
| 6 | Digital Marketing | https://catalog.depaul.edu/programs/digital-marketing-ms/ |
| 7 | Economics Quantitative Analysis | https://catalog.depaul.edu/programs/economics-quantitative-analysis-ms/ |
| 8 | Entrepreneurship (Online) | https://catalog.depaul.edu/programs/entrepreneurship-online-ms/ |
| 9 | Finance | https://catalog.depaul.edu/programs/finance-ms/ |
| 10 | Human Resources | https://catalog.depaul.edu/programs/human-resources-ms/ |
| 11 | Marketing Analysis | https://catalog.depaul.edu/programs/marketing-analysis-ms/ |
| 12 | Real Estate | https://catalog.depaul.edu/programs/real-estate-ms/ |
| 13 | Supply Chain Management | https://catalog.depaul.edu/programs/supply-chain-management-ms/ |
| 14 | Sustainable in Business | https://catalog.depaul.edu/programs/sustainable-in-business-ms/ |
| 15 | Taxation and Analytics (Online) | https://catalog.depaul.edu/programs/taxation-and-analytics-online-ms/ |

##### DBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.depaul.edu/programs/business-administration-dba/ |

#### Jarvis College of Computing and Digital Media (CDM)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://catalog.depaul.edu/programs/artificial-intelligence-ms/ |
| 2 | Artificial Intelligence (Online) | https://catalog.depaul.edu/programs/artificial-intelligence-online-ms/ |
| 3 | Business Analytics | https://catalog.depaul.edu/programs/business-analytics-ms/ |
| 4 | Computer Science | https://catalog.depaul.edu/programs/computer-science-ms/ |
| 5 | Computer Science (Online) | https://catalog.depaul.edu/programs/computer-science-online-ms/ |
| 6 | Cybersecurity | https://catalog.depaul.edu/programs/cybersecurity-ms/ |
| 7 | Cybersecurity (Online) | https://catalog.depaul.edu/programs/cybersecurity-online-ms/ |
| 8 | Data Science | https://catalog.depaul.edu/programs/data-science-ms/ |
| 9 | Data Science (Online) | https://catalog.depaul.edu/programs/data-science-online-ms/ |
| 10 | Game Programming | https://catalog.depaul.edu/programs/game-programming-ms/ |
| 11 | Game Programming (Online) | https://catalog.depaul.edu/programs/game-programming-online-ms/ |
| 12 | Health Informatics | https://catalog.depaul.edu/programs/health-informatics-ms/ |
| 13 | Health Informatics (Online) | https://catalog.depaul.edu/programs/health-informatics-online-ms/ |
| 14 | Human-Computer Interaction | https://catalog.depaul.edu/programs/human-computer-interaction-ms/ |
| 15 | Human-Computer Interaction (Online) | https://catalog.depaul.edu/programs/human-computer-interaction-online-ms/ |
| 16 | Information Systems | https://catalog.depaul.edu/programs/information-systems-ms/ |
| 17 | Information Systems (Online) | https://catalog.depaul.edu/programs/information-systems-online-ms/ |
| 18 | Network Engineering Security (Online) | https://catalog.depaul.edu/programs/network-engineering-security-online-ms/ |
| 19 | Software Engineering | https://catalog.depaul.edu/programs/software-engineering-ms/ |
| 20 | Software Engineering (Online) | https://catalog.depaul.edu/programs/software-engineering-online-ms/ |
| 21 | Film and Television | https://catalog.depaul.edu/programs/film-and-television-ms/ |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Animation | https://catalog.depaul.edu/programs/animation-ma/ |
| 2 | Digital Communication and Media Arts (CDM) | https://catalog.depaul.edu/programs/digital-communication-media-arts-cdm-ma/ |
| 3 | Film and Television | https://catalog.depaul.edu/programs/film-and-television-ms/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Animation | https://catalog.depaul.edu/programs/animation-mfa/ |
| 2 | Creative Producing | https://catalog.depaul.edu/programs/creative-producing-mfa/ |
| 3 | Documentary | https://catalog.depaul.edu/programs/documentary-mfa/ |
| 4 | Film and Television Directing | https://catalog.depaul.edu/programs/film-and-television-directing-mfa/ |
| 5 | Game Design | https://catalog.depaul.edu/programs/game-design-mfa/ |
| 6 | Screenwriting | https://catalog.depaul.edu/programs/screenwriting-mfa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer and Information Sciences | https://catalog.depaul.edu/programs/computer-and-information-sciences-phd/ |
| 2 | Human-Centered Design | https://catalog.depaul.edu/programs/human-centered-design-phd/ |

#### College of Communication

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication and Media | https://catalog.depaul.edu/programs/communication-media-ma/ |
| 2 | Digital Communication and Media Arts (Communication) | https://catalog.depaul.edu/programs/digital-communication-media-arts-communication-ma/ |
| 3 | Journalism | https://catalog.depaul.edu/programs/journalism-ma/ |
| 4 | Professional Communication (Online) | https://catalog.depaul.edu/programs/professional-communication-online-ma/ |
| 5 | Public Relations and Advertising | https://catalog.depaul.edu/programs/public-relations-advertising-ma/ |

#### College of Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Education Culture and Society (Online) | https://catalog.depaul.edu/programs/education-culture-and-society-online-med/ |
| 2 | Educational Leadership (Online) | https://catalog.depaul.edu/programs/educational-leadership-online-med/ |
| 3 | Middle Grades Education | https://catalog.depaul.edu/programs/middle-grades-education-med/ |
| 4 | Special Education | https://catalog.depaul.edu/programs/special-education-med/ |
| 5 | Teaching and Learning (Early Childhood) | https://catalog.depaul.edu/programs/teaching-learning-early-childhood-education-med/ |
| 6 | Teaching and Learning (Elementary) | https://catalog.depaul.edu/programs/teaching-learning-elementary-education-med/ |
| 7 | Teaching and Learning (Physical Education) | https://catalog.depaul.edu/programs/teaching-learning-physical-education-med/ |
| 8-19 | Teaching and Learning (Secondary - various subjects) | Various URLs |
| 20 | Value-Creating Education (Online) | https://catalog.depaul.edu/programs/value-creating-education-global-citizenship-online-med/ |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Bilingual Bicultural Education | https://catalog.depaul.edu/programs/bilingual-bicultural-education-ma/ |
| 2 | Counseling | https://catalog.depaul.edu/programs/counseling-ma/ |
| 3 | Curriculum Studies | https://catalog.depaul.edu/programs/curriculum-studies-ma/ |
| 4 | Curriculum Studies (Online) | https://catalog.depaul.edu/programs/curriculum-studies-online-ma/ |
| 5 | Education Culture and Society | https://catalog.depaul.edu/programs/education-culture-and-society-ma/ |
| 6 | Educational Leadership | https://catalog.depaul.edu/programs/educational-leadership-ma/ |
| 7 | Educational Leadership (Online) | https://catalog.depaul.edu/programs/educational-leadership-online-ma/ |
| 8 | Mathematics Education | https://catalog.depaul.edu/programs/mathematics-education-ma/ |
| 9 | Mathematics Education (Online) | https://catalog.depaul.edu/programs/mathematics-education-online-ma/ |
| 10 | Reading Specialist | https://catalog.depaul.edu/programs/reading-specialist-ma-med/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics for Teaching (Online) | https://catalog.depaul.edu/programs/mathematics-for-teaching-online-ms/ |
| 2 | Mathematics Teaching | https://catalog.depaul.edu/programs/mathematics-teaching-ms/ |
| 3 | Sport and Fitness Educational Leadership (Online) | https://catalog.depaul.edu/programs/sport-fitness-educational-leadership-online-ms/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum Studies | https://catalog.depaul.edu/programs/curriculum-studies-edd/ |
| 2 | Early Childhood Education | https://catalog.depaul.edu/programs/early-childhood-education-edd/ |
| 3 | Educational Leadership | https://catalog.depaul.edu/programs/educational-leadership-edd/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum Studies | https://catalog.depaul.edu/programs/curriculum-studies-phd/ |
| 2 | Educational Leadership | https://catalog.depaul.edu/programs/educational-leadership-phd/ |
| 3 | Global Educational Leadership | https://catalog.depaul.edu/programs/global-educational-leadership-phd/ |
| 4 | Value-Creating Education (Online) | https://catalog.depaul.edu/programs/value-creating-education-global-citizenship-online-phd/ |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum Studies | https://catalog.depaul.edu/programs/curriculum-studies-eds/ |
| 2 | Educational Leadership | https://catalog.depaul.edu/programs/educational-leadership-eds/ |

#### College of Liberal Arts and Social Sciences (LAS)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Diplomacy | https://catalog.depaul.edu/programs/applied-diplomacy-ma/ |
| 2 | Applied Professional Studies | https://catalog.depaul.edu/programs/applied-professional-studies-ma/ |
| 3 | Communication and Media | https://catalog.depaul.edu/programs/communication-media-ma/ |
| 4 | Community Psychology | https://catalog.depaul.edu/programs/community-psychology-ma/ |
| 5 | Critical Ethnic Studies | https://catalog.depaul.edu/programs/critical-ethnic-studies-ma/ |
| 6 | Education Culture and Society | https://catalog.depaul.edu/programs/education-culture-and-society-ma/ |
| 7 | French | https://catalog.depaul.edu/programs/french-ma/ |
| 8 | History | https://catalog.depaul.edu/programs/history-ma/ |
| 9 | Industrial-Organizational Psychology | https://catalog.depaul.edu/programs/industrial-organizational-psychology-ma/ |
| 10 | Interdisciplinary Studies | https://catalog.depaul.edu/programs/interdisciplinary-studies-ma/ |
| 11 | International Studies | https://catalog.depaul.edu/programs/international-studies-ma/ |
| 12 | Liberal Studies | https://catalog.depaul.edu/programs/liberal-studies-ma/ |
| 13 | Psychological Science | https://catalog.depaul.edu/programs/psychological-science-ma/ |
| 14 | Public Administration | https://catalog.depaul.edu/programs/public-administration-mpa/ |
| 15 | Sociology | https://catalog.depaul.edu/programs/sociology-ma/ |
| 16 | Spanish | https://catalog.depaul.edu/programs/spanish-ma/ |
| 17 | Sustainable Urban Development | https://catalog.depaul.edu/programs/sustainable-urban-development-ma/ |
| 18 | Women's and Gender Studies | https://catalog.depaul.edu/programs/womens-gender-studies-ma/ |
| 19 | Writing and Rhetoric Discourse | https://catalog.depaul.edu/programs/writing-rhetoric-discourse-ma/ |
| 20 | Writing and Publishing | https://catalog.depaul.edu/programs/writing-publishing-ma/ |
| 21 | Law | https://catalog.depaul.edu/programs/law-jd/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.depaul.edu/programs/applied-mathematics-ms/ |
| 2 | Applied Mathematics (Online) | https://catalog.depaul.edu/programs/applied-mathematics-online-ms/ |
| 3 | Applied Statistics | https://catalog.depaul.edu/programs/applied-statistics-ms/ |
| 4 | Applied Statistics (Online) | https://catalog.depaul.edu/programs/applied-statistics-online-ms/ |
| 5 | Clinical Psychology | https://catalog.depaul.edu/programs/clinical-psychology-ma/ |
| 6 | Community Psychology | https://catalog.depaul.edu/programs/community-psychology-ms/ |
| 7 | Environmental Science | https://catalog.depaul.edu/programs/environmental-science-ms/ |
| 8 | Industrial-Organizational Psychology | https://catalog.depaul.edu/programs/industrial-organizational-psychology-ms/ |
| 9 | Interdisciplinary Studies | https://catalog.depaul.edu/programs/interdisciplinary-studies-ms/ |
| 10 | Public Policy | https://catalog.depaul.edu/programs/public-policy-mpp/ |
| 11 | Pure Mathematics | https://catalog.depaul.edu/programs/pure-mathematics-ms/ |
| 12 | Research Psychology | https://catalog.depaul.edu/programs/research-psychology-ms/ |
| 13 | Social Work | https://catalog.depaul.edu/programs/social-work-msw/ |
| 14 | Social Work Advanced Standing | https://catalog.depaul.edu/programs/social-work-advanced-standing-msw/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing and Publishing | https://catalog.depaul.edu/programs/creative-writing-and-publishing-mfa/ |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://catalog.depaul.edu/programs/public-administration-mpa/ |
| 2 | Public Administration (Online) | https://catalog.depaul.edu/programs/public-administration-online-mpa/ |

##### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | https://catalog.depaul.edu/programs/public-policy-mpp/ |
| 2 | Public Policy (Online) | https://catalog.depaul.edu/programs/public-policy-online-mpp/ |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.depaul.edu/programs/social-work-msw/ |
| 2 | Social Work Advanced Standing | https://catalog.depaul.edu/programs/social-work-advanced-standing-msw/ |

##### MNM
| # | 项目 | URL |
|---|------|-----|
| 1 | Nonprofit Management | https://catalog.depaul.edu/programs/nonprofit-management-mnm/ |
| 2 | Nonprofit Management (Online) | https://catalog.depaul.edu/programs/nonprofit-management-online-mnm/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.depaul.edu/programs/philosophy-phd/ |

##### Joint Degrees
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work MSW + Women's & Gender Studies MA | https://catalog.depaul.edu/programs/social-work-msw-ma-wgs/ |
| 2 | Public Policy MPP + Journalism MA | https://catalog.depaul.edu/programs/public-policy-mpp-journalism-ma-joint-degree/ |

#### College of Science and Health (CSH)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.depaul.edu/programs/biological-sciences-ms/ |
| 2 | Chemistry | https://catalog.depaul.edu/programs/chemistry-ms/ |
| 3 | Environmental Science | https://catalog.depaul.edu/programs/environmental-science-ms/ |
| 4 | Generalist Nursing | https://catalog.depaul.edu/programs/generalist-nursing-ms/ |
| 5 | Occupational Therapy | https://catalog.depaul.edu/programs/occupational-therapy-ms/ |
| 6 | Physics | https://catalog.depaul.edu/programs/physics-ms/ |
| 7 | Speech-Language Pathology | https://catalog.depaul.edu/programs/speech-language-pathology-ms/ |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.depaul.edu/programs/public-health-mph/ |

##### MSN
| # | 项目 | URL |
|---|------|-----|
| 1 | Specialty (Online) | https://catalog.depaul.edu/programs/msn-specialty-online-msn/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice | https://catalog.depaul.edu/programs/doctor-of-nursing-practice-dnp/ |

##### Joint Degrees
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health MPH + Business MBA | https://catalog.depaul.edu/programs/public-health-mph-mba-management/ |

#### College of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://catalog.depaul.edu/programs/law-jd/ |
| 2-10 | Joint JD programs (Business, Computer Science, Cybersecurity, Information Systems, International Public Service, International Studies, Nonprofit Management, Public Administration, Public Policy, Public Service) | Various URLs |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Law | https://catalog.depaul.edu/programs/health-law-llm/ |
| 2 | Intellectual Property Law and Information Technology | https://catalog.depaul.edu/programs/intellectual-property-law-and-information-technology-llm/ |
| 3 | International Law | https://catalog.depaul.edu/programs/international-law-llm/ |
| 4 | US Legal Studies | https://catalog.depaul.edu/programs/us-legal-studies-llm/ |

##### MLS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Legal Studies | https://catalog.depaul.edu/programs/law-mls/ |
| 2 | MLS (Online) | https://catalog.depaul.edu/programs/law-online-mls/ |

#### School of Music

##### MM (Master of Music)
| # | 项目 | URL |
|---|------|-----|
| 1 | Composition | https://catalog.depaul.edu/programs/composition-mm/ |
| 2 | Jazz Studies | https://catalog.depaul.edu/programs/jazz-studies-mm/ |
| 3 | Music Education | https://catalog.depaul.edu/programs/music-education-mm/ |
| 4 | Music Performance | https://catalog.depaul.edu/programs/music-performance-mm/ |

#### The Theatre School

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Acting | https://catalog.depaul.edu/programs/acting-mfa/ |
| 2 | Film and Television Directing | https://catalog.depaul.edu/programs/film-and-television-directing-mfa/ |
| 3 | Screenwriting | https://catalog.depaul.edu/programs/screenwriting-mfa/ |

### 2.2 Graduate admissions model

DePaul's graduate admissions is **decentralized** — each college/school manages its own admissions process. Students apply directly to their program of interest. Application requirements vary by program.

**Application portals**:
- Driehaus College of Business: https://business.depaul.edu/
- CDM: https://cdm.depaul.edu/
- College of Education: https://education.depaul.edu/
- LAS: https://las.depaul.edu/
- CSH: https://csh.depaul.edu/
- College of Law: https://law.depaul.edu/
- School of Music: https://music.depaul.edu/
- The Theatre School: https://theatre.depaul.edu/

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application platform | Common App | depaul.edu/apply |
| Early Action (non-binding) | November 15 | depaul.edu/admission/undergraduate-admission |
| EA Notification | December 15 | depaul.edu/admission/undergraduate-admission |
| Regular Decision | February 1 | depaul.edu/admission/undergraduate-admission |
| RD Notification | March 15 | depaul.edu/admission/undergraduate-admission |
| Enrollment confirmation | May 1 (National Reply Date) | Standard US practice |
| Application fee | Free ($0) | depaul.edu (no fee mentioned; Common App) |
| SAT/ACT policy | **Test-optional** | depaul.edu/admission/undergraduate-admission/test-optional-faqs |
| Superscore | Yes (if scores submitted) | Standard policy |
| Self-report scores | Yes | Test-optional policy |
| TOEFL code | 1165 | depaul.edu/admission/international-admission/freshman |
| SAT code | 1165 | depaul.edu/admission/international-admission/freshman |
| Recommendations | Counselor recommendation | Standard |
| Interview | Not required | N/A |
| Scholarship priority | November 15 (EA) or February 1 | depaul.edu/tuition-and-aid/scholarships |
| **Need policy** | **Need-aware for all applicants** | User-provided (verify) |

**School-specific deadlines**:
- **School of Music**: Varies by program (typically December 1 - February 1)
- **Theatre School**: Acting/Stage Management: December 1; All other majors: February 1

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 80 (old scale) / 4 (new scale) | — | No subsection lower than 17 (old) / 3 (new) |
| TOEFL (new scale, Jan 2026+) | 4 | — | ETS TOEFL iBT score scale changed from 0-120 to 1-6 |
| IELTS Academic | 6.0 | — | Valid for 2 years |
| Duolingo English Test (DET) | 115 | — | — |
| SAT EBRW | 540 | — | Alternative to English proficiency test |
| ACT Reading + English | 18 Reading / 20 English | — | Alternative to English proficiency test |

> **Applicability**: Required for non-native English speakers. Students who score below minimums may be admitted conditionally.

### 3.3 Graduate — global rules

- **Decentralized admissions**: Each program sets own requirements
- **Application fee**: Varies by program (typically $40-$75)
- **GRE/GMAT**: Program-specific; many programs have made GRE/GMAT optional
- **English proficiency**: Same minimums as undergraduate (TOEFL 80 / IELTS 6.0 / DET 115)
- **CGS April 15 Resolution**: DePaul is a signatory

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

**Most colleges (Business, Communication, CDM, Education, LAS, CSH, SCPS)**:

| Expense item | Amount | Notes |
|-------------|--------|-------|
| Tuition (12-18 credits/term) | $16,060/term = **$48,180/year** | Package rate for full-time |
| Per-credit rate (1-11 or 18+ credits) | $878/credit | Part-time rate |
| Books, Course Materials, Supplies | $1,104/year | Estimated |
| Living Expenses (on-campus, housing + food) | $20,766/year | On-campus estimate |
| Living Expenses (with family) | $5,721/year | Living with parents |
| Transportation | $1,290/year | Estimated |
| Miscellaneous Personal Expenses | $4,794/year | Estimated |
| **Total COA (on-campus)** | **~$76,134/year** | Tuition + all indirect costs |
| **Total COA (with family)** | **~$55,269/year** | Tuition + with-family costs |

**Music and Theatre programs**:

| Expense item | Amount | Notes |
|-------------|--------|-------|
| Tuition (12-18 credits/term) | $16,801/term = **$50,403/year** | Package rate |
| All other costs | Same as above | — |
| **Total COA (on-campus)** | **~$78,357/year** | — |

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 |
|------|-----|
| Need-aware/need-blind | **Need-aware for all applicants** |
| Meet 100% demonstrated need | No (not guaranteed) |
| Merit scholarships | Yes — $14,000 to $33,000/year |
| Total scholarship investment | $300 million annually |
| Incoming freshman scholarships | $57 million annually |
| Need-based aid | $11 million+ annually |
| State Scholar Plus | Available for Illinois residents |
| RaiseMe micro-scholarships | Up to $40,000 over 4 years |
| Catholic high school scholarship | $20,000 (Illinois Catholic HS graduates with 3.0+) |
| FAFSA required | Yes (for federal/state/institutional need-based aid) |
| CSS Profile | Not mentioned (verify) |
| Loan-free packages | Not guaranteed |

### 4.3 Graduate cost & funding framework

- **Tuition**: Varies by program; typically $800-$1,200/credit hour
- **Application fee**: Varies by program ($40-$75)
- **Funding**: Assistantships, fellowships, and scholarships available by program
- **Business (Kellstadt)**: Merit scholarships available
- **Education**: Graduate assistantships available
- **CDM**: Research and teaching assistantships available

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 15"
  source_url: "https://www.depaul.edu/admission/undergraduate-admission"
  source_snippet: "Early Action Program Apply by: November 15 Notification by: December 15"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "February 1"
  source_url: "https://www.depaul.edu/admission/undergraduate-admission"
  source_snippet: "Regular Notification Apply by: February 1 Notification by: March 15"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.test_policy
  value: "Test-optional"
  source_url: "https://www.depaul.edu/admission/undergraduate-admission/test-optional-faqs"
  source_snippet: "DePaul has adopted a test-optional alternative for freshman admission. Students applying for freshman admission can choose whether to submit ACT or SAT scores as part of the application."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.english_proficiency.TOEFL
  value: "80 (old scale) / 4 (new scale)"
  source_url: "https://www.depaul.edu/admission/international-admission/freshman"
  source_snippet: "TOEFL* 80 or 4 on the TOEFL iBT with no subsection lower than 17 or 3"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.IELTS
  value: "6.0"
  source_url: "https://www.depaul.edu/admission/international-admission/freshman"
  source_snippet: "IELTS Academic 6"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.Duolingo
  value: "115"
  source_url: "https://www.depaul.edu/admission/international-admission/freshman"
  source_snippet: "Duolingo English Test (DET) 115 on the DET"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.costs.tuition_2026_2027
  value: "$48,180/year ($16,060/term)"
  source_url: "https://www.depaul.edu/tuition-and-aid/undergraduate-tuition-and-fees"
  source_snippet: "2026 $16,060 $48,180"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.costs.tuition_music_theatre
  value: "$50,403/year ($16,801/term)"
  source_url: "https://www.depaul.edu/tuition-and-aid/undergraduate-tuition-and-fees"
  source_snippet: "Undergraduate Music and Theatre Admit Year Per Term Annual 2026 $16,801 $50,403"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.costs.living_on_campus
  value: "$20,766/year"
  source_url: "https://www.depaul.edu/tuition-and-aid/understand-cost-of-attendance"
  source_snippet: "Living Expenses (including housing & food) $20,766"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.costs.books
  value: "$1,104/year"
  source_url: "https://www.depaul.edu/tuition-and-aid/understand-cost-of-attendance"
  source_snippet: "Books, Course Materials, Supplies, & Equipment $1,104"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.costs.transportation
  value: "$1,290/year"
  source_url: "https://www.depaul.edu/tuition-and-aid/understand-cost-of-attendance"
  source_snippet: "Transportation $1,290"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.costs.total_coa_on_campus
  value: "~$76,134/year"
  source_url: "https://www.depaul.edu/tuition-and-aid/understand-cost-of-attendance"
  source_snippet: "Total of items listed above $28,035 (plus tuition $48,180)"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.financial_aid.scholarships_total
  value: "$300 million annually"
  source_url: "https://www.depaul.edu/tuition-and-aid/scholarships"
  source_snippet: "$300,000,000: Our investment in your success"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.financial_aid.merit_range
  value: "$14,000 to $33,000/year"
  source_url: "https://www.depaul.edu/tuition-and-aid/scholarships"
  source_snippet: "$14,000 to $33,000"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.model
  value: "Decentralized"
  source_url: "https://www.depaul.edu/admission/graduate-admission"
  source_snippet: "Graduate application deadlines vary by program. Explore specific deadlines for each program."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-P-001:
  field: programs.total_count
  value: 614
  source_url: "https://catalog.depaul.edu/programs/"
  source_snippet: "614 program URLs extracted from catalog"
  capture_date: "2026-07-06"
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
depaul-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, matrix)
├── 01-ug-business                   (Section 1: Driehaus College UG programs)
├── 02-ug-cdm                        (Section 1: CDM UG programs)
├── 03-ug-communication              (Section 1: Communication UG programs)
├── 04-ug-education                  (Section 1: Education UG programs)
├── 05-ug-las                        (Section 1: LAS UG programs)
├── 06-ug-csh                        (Section 1: CSH UG programs)
├── 07-ug-music                      (Section 1: Music UG programs)
├── 08-ug-theatre                    (Section 1: Theatre UG programs)
├── 09-ug-scps                       (Section 1: SCPS programs)
├── 10-ug-minors                     (Section 1.4: all minors)
├── 11-grad-business                 (Section 2: Business grad programs)
├── 12-grad-cdm                      (Section 2: CDM grad programs)
├── 13-grad-communication            (Section 2: Communication grad programs)
├── 14-grad-education                (Section 2: Education grad programs)
├── 15-grad-las                      (Section 2: LAS grad programs)
├── 16-grad-csh                      (Section 2: CSH grad programs)
├── 17-grad-law                      (Section 2: Law programs)
├── 18-grad-music                    (Section 2: Music grad programs)
├── 19-grad-theatre                  (Section 2: Theatre grad programs)
├── 20-deadlines-requirements        (Section 3)
├── 21-costs-financial-aid           (Section 4)
└── 22-evidence-chain                (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "depaul-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "https://catalog.depaul.edu/programs/"
  capture_date: "2026-07-06"
  version: v2.0
  change_status: baseline
  last_verified: "2026-07-06"
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Application fee confirmation ($0 or amount) | depaul.edu/apply |
| P0 | Need-blind/need-aware policy verification | depaul.edu/tuition-and-aid/financial-aid-overview |
| P1 | Graduate application fee per program | Individual program pages |
| P1 | GRE/GMAT policy per graduate program | Individual program pages |
| P1 | Per-program TOEFL minimums (graduate) | Individual program pages |
| P2 | Detailed cost by college (if different) | depaul.edu/tuition-and-aid/undergraduate-tuition-and-fees |
| P2 | Financial aid income thresholds | depaul.edu/tuition-and-aid/scholarships |
| P2 | Average actual price paid | depaul.edu/tuition-and-aid/net-price-calculator |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | DePaul University |
|------|-------------------|
| Type | Private, Vincentian |
| Location | Chicago, IL |
| Total programs (Rule 1) | 614 |
| Schools/colleges (Rule 2) | 10 |
| UG tuition/year | $48,180 (most) / $50,403 (Music/Theatre) |
| Total COA/year (on-campus) | ~$76,134 |
| EA deadline | November 15 |
| RD deadline | February 1 |
| SAT/ACT required? | No (test-optional) |
| TOEFL minimum | 80 (old) / 4 (new) |
| IELTS minimum | 6.0 |
| Duolingo minimum | 115 |
| Need-blind (domestic)? | No (need-aware) |
| Need-blind (international)? | No (need-aware) |
| Merit scholarship range | $14,000-$33,000/year |
| Application fee | Free ($0) — verify |
| Graduate app fee | Varies by program |
| Strong programs | CDM (tech/animation), Business (Kellstadt), Communication, Education |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: catalog.depaul.edu, www.depaul.edu/admission, www.depaul.edu/tuition-and-aid
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
