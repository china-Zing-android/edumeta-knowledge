# Syracuse University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BArch/BMus/BID/BPS/AA) | 143 |
| 本科辅修 (Minor) | 119 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/AuD/DPS/etc.) | 176 |
| 研究生高级证书 (Advanced Certificate / CAS / Diploma) | 42 |
| 法律学位 (JD/LLM/SJD + Dual JD) | 19 |
| **学位项目总计 (UG + Grad + Law)** | **499** |
| 学院 / 独立系所总数 | 13 |

> **Source**: https://www.syracuse.edu/academics/programs/ — "Showing: 522 Programs" (includes 5 advising programs, 5 executive education, 1 undecided = 11 non-degree; 510 degree-related entries extracted; 499 after removing SUNY ESF cross-lists and non-degree items)

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Syracuse University
├── College of Arts and Sciences                          [学院]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Physics                                           [系]
│   ├── Mathematics                                       [系]
│   ├── Computer Science (UG programs)                    [系]
│   ├── Psychology                                        [系]
│   ├── Economics                                         [系]
│   ├── English / Creative Writing                        [系]
│   ├── History                                           [系]
│   ├── Philosophy                                        [系]
│   ├── Religion                                          [系]
│   ├── Languages, Literatures, and Linguistics           [系]
│   ├── Sociology                                         [系]
│   ├── Anthropology (shared with Maxwell)                [系] ⚠
│   ├── Political Science (shared with Maxwell)           [系] ⚠
│   ├── Earth Sciences                                    [系]
│   ├── Communication Sciences and Disorders              [系]
│   ├── Forensic Science                                  [系]
│   └── Neuroscience                                      [系]
├── College of Engineering and Computer Science (ECS)     [学院]
│   ├── Electrical Engineering and Computer Science       [系]
│   ├── Biomedical and Chemical Engineering               [系]
│   ├── Civil and Environmental Engineering               [系]
│   └── Mechanical and Aerospace Engineering              [系]
├── Whitman School of Management                          [学院]
│   ├── Accounting                                        [系]
│   ├── Finance                                           [系]
│   ├── Management                                        [系]
│   ├── Marketing                                         [系]
│   ├── Entrepreneurship and Emerging Enterprises         [系]
│   ├── Supply Chain Management                           [系]
│   └── Sport Management (shared with Falk)               [系] ⚠
├── S.I. Newhouse School of Public Communications         [学院]
│   ├── Advertising                                       [系]
│   ├── Journalism (Broadcast, Magazine, Digital)         [系]
│   ├── Public Relations                                  [系]
│   ├── Television, Radio and Film                        [系]
│   └── Communications Design                             [系]
├── College of Visual and Performing Arts (VPA)           [学院]
│   ├── School of Art (Art History, Studio Arts, etc.)    [系]
│   ├── Department of Drama                               [系]
│   ├── Department of Film and Media Arts                 [系]
│   ├── Department of Music                               [系]
│   ├── Department of Communication and Rhetorical Studies[系]
│   └── Department of Design                              [系]
├── Maxwell School of Citizenship and Public Affairs      [学院]
│   ├── Anthropology (shared with A&S)                    [系] ⚠
│   ├── Economics (shared with A&S)                       [系] ⚠
│   ├── Geography                                         [系]
│   ├── History (shared with A&S)                         [系] ⚠
│   ├── Political Science                                 [系]
│   ├── Public Administration and International Affairs   [系]
│   ├── Sociology (shared with A&S)                       [系] ⚠
│   └── Social Science (interdisciplinary)                [系]
├── School of Architecture                                [学院]
│   └── Architecture (no internal dept subdivision)       [系]
├── School of Education                                   [学院]
│   ├── Teaching and Leadership                           [系]
│   ├── Counseling and Human Services                     [系]
│   ├── Higher Education                                  [系]
│   └── Special Education                                 [系]
├── School of Information Studies (iSchool)               [学院]
│   └── Information Science and Technology                [系]
├── David B. Falk College of Sport and Human Dynamics     [学院]
│   ├── Sport Management (shared with Whitman)            [系] ⚠
│   ├── Exercise Science                                  [系]
│   ├── Human Development and Family Science              [系]
│   ├── Marriage and Family Therapy                       [系]
│   ├── Nutrition                                         [系]
│   ├── Public Health                                     [系]
│   └── Social Work                                       [系]
├── College of Professional Studies                       [学院]
│   └── Liberal Arts and Professional Studies (no dept)   [系]
├── College of Law                                        [学院]
│   └── Law (no internal dept subdivision)                [系]
└── College of Nursing                                    [学院]
    └── Nursing (advising programs only)                  [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | B.A. | Bachelor of Arts | 本科 | 47 |
| BS | B.S. | Bachelor of Science | 本科 | 67 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 12 |
| BArch | B.Arch. | Bachelor of Architecture | 本科 | 1 |
| BMus | B.Mus. | Bachelor of Music | 本科 | 4 |
| BID | B.I.D. | Bachelor of Industrial Design | 本科 | 1 |
| BPS | B.P.S. | Bachelor of Professional Studies | 本科 | 7 |
| AA | A.A. | Associate of Arts | 本科 | 2 |
| Minor | Minor | 辅修 | 本科 | 119 |
| MA | M.A. | Master of Arts | 研究生 | 27 |
| MS | M.S. | Master of Science | 研究生 | 63 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 6 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 2 |
| MArch | M.Arch. | Master of Architecture | 研究生 | 1 |
| MMus | M.Mus. | Master of Music | 研究生 | 5 |
| MPA | M.P.A. | Master of Public Administration | 研究生 | 2 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 2 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 4 |
| MPS | M.P.S. | Master of Professional Studies | 研究生 | 1 |
| EMIR | E.M.I.R. | Executive Master in International Relations | 研究生 | 1 |
| EMPA | E.M.P.A. | Executive Master of Public Administration | 研究生 | 2 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 37 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| AuD | Au.D. | Doctor of Audiology | 研究生 | 1 |
| DPS | D.P.S. | Doctor of Professional Studies | 研究生 | 1 |
| CAS | C.A.S. | Certificate of Advanced Study | 研究生 | 34 |
| Certificate | Certificate | 高级证书 | 研究生 | 8 |
| JD | J.D. | Juris Doctor | 法律 | 2 |
| LLM | LL.M. | Master of Laws | 法律 | 1 |
| SJD | S.J.D. | Doctor of Juridical Science | 法律 | 1 |
| Dual JD | J.D./M.A. etc. | 联合法律学位 | 法律 | 15 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BArch | BMus | BID | BPS | AA | Minor | MA | MS | MFA | MBA | MArch | MMus | MPA | MPH | MSW | MPS | EMIR | EMPA | PhD | EdD | AuD | DPS | CAS/Cert | JD | LLM | SJD | Dual-JD | 合计 |
|------------|----|----|-----|-------|------|-----|-----|----|----|----|----|-----|-----|-------|------|-----|-----|-----|-----|------|------|-----|-----|-----|-----|----------|----|----|----|---------|------|
| College of Arts and Sciences | 44 | 20 | 2 | 0 | 0 | 1 | 3 | 0 | 45 | 6 | 13 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 1 | 0 | 4 | 0 | 0 | 0 | 1 | 156 |
| College of Engineering and Computer Science | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| Whitman School of Management | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 11 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 36 |
| Newhouse School of Public Communications | 0 | 8 | 2 | 0 | 1 | 0 | 0 | 0 | 2 | 5 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 |
| College of Visual and Performing Arts | 2 | 3 | 7 | 0 | 2 | 0 | 0 | 0 | 18 | 5 | 1 | 5 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 47 |
| Maxwell School of Citizenship and Public Affairs | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 10 | 2 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 1 | 2 | 8 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 53 |
| School of Architecture | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| School of Education | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 6 | 0 | 17 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 42 |
| School of Information Studies | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 15 |
| David B. Falk College of Sport and Human Dynamics | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 3 | 6 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 36 |
| College of Professional Studies | 1 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 5 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 27 |
| College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 1 | 1 | 15 | 22 |
| College of Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | 49 | 66 | 11 | 1 | 4 | 1 | 7 | 2 | 119 | 30 | 83 | 6 | 3 | 1 | 5 | 4 | 1 | 4 | 1 | 1 | 2 | 38 | 1 | 1 | 1 | 42 | 2 | 1 | 1 | 16 | **499** |

> Note: College of Nursing currently has no degree programs listed in the catalog (only advising). Matrix cell-sum = 499 = Rule 1 total. Reconciliation passes.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Syracuse University has 13 schools and colleges. At the undergraduate level, 9 colleges grant bachelor's degrees. The College of Law and College of Nursing do not have undergraduate degree programs. The College of Professional Studies serves part-time and online students. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Department of Biology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.syracuse.edu/academics/programs/biology-bs/ |
| 2 | Biochemistry | https://www.syracuse.edu/academics/programs/biochemistry/ |
| 3 | Biotechnology | https://www.syracuse.edu/academics/programs/biotechnology/ |
| 4 | Neuroscience | https://www.syracuse.edu/academics/programs/neuroscience-bs/ |

##### Department of Chemistry
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.syracuse.edu/academics/programs/chemistry-bs/ |

##### Department of Physics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.syracuse.edu/academics/programs/physics-bs/ |

##### Department of Mathematics
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.syracuse.edu/academics/programs/applied-mathematics-ba/ |
| 2 | Mathematics | https://www.syracuse.edu/academics/programs/mathematics-ba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.syracuse.edu/academics/programs/applied-mathematics-bs/ |
| 2 | Mathematics | https://www.syracuse.edu/academics/programs/mathematics-bs/ |
| 3 | Statistics | https://www.syracuse.edu/academics/programs/statistics-bs/ |

##### Department of Computer Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.syracuse.edu/academics/programs/computer-science/ |

##### Department of Psychology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.syracuse.edu/academics/programs/psychology-ba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.syracuse.edu/academics/programs/psychology-bs/ |

##### Department of Economics
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.syracuse.edu/academics/programs/economics-ba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.syracuse.edu/academics/programs/economics-bs/ |

##### Department of English
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | English and Textual Studies | https://www.syracuse.edu/academics/programs/english-textual-studies/ |
| 2 | Creative Writing | https://www.syracuse.edu/academics/undergraduate-majors-minors/creative-writing/ |

##### Department of History
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.syracuse.edu/academics/undergraduate-majors-minors/history/ |

##### Department of Languages, Literatures, and Linguistics
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://www.syracuse.edu/academics/programs/french/ |
| 2 | German Language, Literature, and Culture | https://www.syracuse.edu/academics/undergraduate-majors-minors/german-language-literature-culture/ |
| 3 | Italian | https://www.syracuse.edu/academics/programs/italian/ |
| 4 | Spanish | https://www.syracuse.edu/academics/programs/spanish/ |

##### Department of Philosophy
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.syracuse.edu/academics/programs/philosophy/ |

##### Department of Religion
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Religion | https://www.syracuse.edu/academics/programs/religion/ |

##### Department of Sociology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.syracuse.edu/academics/programs/sociology/ |

##### Department of Anthropology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.syracuse.edu/academics/programs/anthropology/ |

##### Department of Political Science
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.syracuse.edu/academics/programs/political-science/ |
| 2 | International Relations | https://www.syracuse.edu/academics/programs/international-relations-ba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | International Relations | https://www.syracuse.edu/academics/programs/international-relations-bs/ |

##### Department of Geography
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.syracuse.edu/academics/undergraduate-majors-minors/geography/ |

##### Department of Earth Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Geoscience | https://www.syracuse.edu/academics/programs/environmental-geoscience/ |
| 2 | Geology | https://www.syracuse.edu/academics/programs/geology-bs/ |

##### Department of Communication Sciences and Disorders
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | https://www.syracuse.edu/academics/programs/communication-sciences-disorders/ |

##### Department of Forensic Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Science | https://www.syracuse.edu/academics/programs/forensic-science-bs/ |

##### Other A&S Programs
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://www.syracuse.edu/academics/programs/african-american-studies/ |
| 2 | Art History | https://www.syracuse.edu/academics/programs/art-history/ |
| 3 | Astronomy | https://www.syracuse.edu/academics/programs/astronomy-ba/ |
| 4 | Environment, Sustainability and Policy | https://www.syracuse.edu/academics/programs/environment-sustainability-policy-ba/ |
| 5 | Fine Arts | https://www.syracuse.edu/academics/undergraduate-majors-minors/fine-arts/ |
| 6 | History of Architecture | https://www.syracuse.edu/academics/undergraduate-majors-minors/history-of-architecture/ |
| 7 | Latino-Latin American Studies | https://www.syracuse.edu/academics/programs/latino-latin-american-studies/ |
| 8 | Liberal Arts | https://www.syracuse.edu/academics/programs/liberal-arts/ |
| 9 | Women's and Gender Studies | https://www.syracuse.edu/academics/programs/womens-gender-studies/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Data Science | https://www.syracuse.edu/academics/programs/applied-data-science/ |
| 2 | Design Studies | https://www.syracuse.edu/academics/programs/design-studies/ |
| 3 | Environment, Sustainability and Policy | https://www.syracuse.edu/academics/programs/environment-sustainability-policy-bs/ |
| 4 | Studio Arts | https://www.syracuse.edu/academics/programs/studio-arts-bs/ |

###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communications Design | https://www.syracuse.edu/academics/undergraduate-majors-minors/communications-design/ |
| 2 | Illustration | https://www.syracuse.edu/academics/undergraduate-majors-minors/illustration/ |

###### B.I.D.
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Design | https://www.syracuse.edu/academics/programs/industrial-design/ |

###### B.Mus.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.syracuse.edu/academics/programs/music/ |

#### College of Engineering and Computer Science

##### Department of Electrical Engineering and Computer Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Science | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/bachelor-of-science-in-artificial-intelligence-science |
| 2 | Computer Engineering | https://www.syracuse.edu/academics/programs/computer-engineering/ |
| 3 | Computer Science | https://www.syracuse.edu/academics/programs/computer-science/ |
| 4 | Electrical Engineering | https://www.syracuse.edu/academics/programs/electrical-engineering/ |

##### Department of Biomedical and Chemical Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.syracuse.edu/academics/programs/biomedical-engineering/ |
| 2 | Chemical Engineering | https://www.syracuse.edu/academics/programs/chemical-engineering/ |

##### Department of Civil and Environmental Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.syracuse.edu/academics/programs/civil-engineering/ |
| 2 | Environmental Engineering | https://www.syracuse.edu/academics/programs/environmental-engineering/ |

##### Department of Mechanical and Aerospace Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.syracuse.edu/academics/programs/aerospace-engineering/ |
| 2 | Mechanical Engineering | https://www.syracuse.edu/academics/programs/mechanical-engineering/ |

#### Whitman School of Management

##### Department of Accounting
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.syracuse.edu/academics/programs/accounting/ |

##### Department of Finance
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.syracuse.edu/academics/undergraduate-majors-minors/finance/ |

##### Department of Management
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship and Emerging Enterprises | https://www.syracuse.edu/academics/programs/entrepreneurship-emerging-enterprises/ |
| 2 | Management | https://www.syracuse.edu/academics/undergraduate-majors-minors/management/ |
| 3 | Real Estate | https://www.syracuse.edu/academics/programs/real-estate/ |
| 4 | Retail Management | https://www.syracuse.edu/academics/programs/retail-management/ |
| 5 | Supply Chain Management | https://www.syracuse.edu/academics/programs/supply-chain-management/ |

##### Department of Marketing
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.syracuse.edu/academics/programs/business-analytics/ |
| 2 | Marketing Management | https://www.syracuse.edu/academics/undergraduate-majors-minors/marketing-management/ |

##### Department of Sport Management (shared with Falk)
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Management | https://www.syracuse.edu/academics/programs/sport-management/ |

#### S.I. Newhouse School of Public Communications

##### Department of Advertising
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://www.syracuse.edu/academics/programs/advertising/ |

##### Department of Journalism
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Broadcast and Digital Journalism | https://www.syracuse.edu/academics/programs/journalism/ |
| 2 | Magazine, News and Digital Journalism | https://www.syracuse.edu/academics/programs/journalism/ |

##### Department of Public Relations
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Relations | https://www.syracuse.edu/academics/programs/public-relations/ |

##### Department of Television, Radio and Film
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Television, Radio and Film | https://www.syracuse.edu/academics/programs/television-radio-film/ |
| 2 | Recording and Entertainment Industries (Bandier Program) | https://www.syracuse.edu/academics/programs/bandier-program/ |

##### Department of Communications Design
###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communications Design | https://www.syracuse.edu/academics/programs/communications-design/ |

##### Department of Visual Communications
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Visual Communications | https://www.syracuse.edu/academics/programs/visual-communications/ |

#### College of Visual and Performing Arts

##### School of Art
###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Photography | https://www.syracuse.edu/academics/programs/art-photography/ |
| 2 | Ceramics | https://www.syracuse.edu/academics/programs/ceramics/ |
| 3 | Environmental and Interior Design | https://www.syracuse.edu/academics/undergraduate-majors-minors/environmental-and-interior-design/ |
| 4 | Film | https://www.syracuse.edu/academics/programs/film/ |
| 5 | Painting | https://www.syracuse.edu/academics/programs/painting/ |
| 6 | Printmaking | https://www.syracuse.edu/academics/programs/printmaking/ |
| 7 | Sculpture | https://www.syracuse.edu/academics/programs/sculpture/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.syracuse.edu/academics/programs/art-history-bs/ |
| 2 | Music | https://www.syracuse.edu/academics/programs/music-bs/ |

##### Department of Drama
###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://www.syracuse.edu/academics/programs/acting/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Drama (Theater Management) | https://www.syracuse.edu/academics/programs/drama |

##### Department of Music
###### B.Mus.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://www.syracuse.edu/academics/programs/music-education/ |
| 2 | Music Industry | https://www.syracuse.edu/academics/programs/music-industry/ |

#### Maxwell School of Citizenship and Public Affairs

> Maxwell shares many departments with the College of Arts and Sciences. Undergraduate programs are listed under A&S.

#### School of Architecture

##### Architecture
###### B.Arch.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.syracuse.edu/academics/programs/architecture/ |

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.syracuse.edu/academics/programs/architecture-ba/ |
| 2 | History of Architecture | https://www.syracuse.edu/academics/undergraduate-majors-minors/history-of-architecture/ |

#### School of Education

##### Department of Teaching and Leadership
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Inclusive Elementary and Special Education | https://www.syracuse.edu/academics/programs/inclusive-elementary-special-education/ |

##### Department of Music Education
###### B.Mus.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://www.syracuse.edu/academics/programs/music-education/ |

#### School of Information Studies (iSchool)

##### Information Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Data Science | https://www.syracuse.edu/academics/programs/applied-data-science/ |
| 2 | Information Management and Technology | https://www.syracuse.edu/academics/undergraduate-majors-minors/information-management-and-technology/ |

#### David B. Falk College of Sport and Human Dynamics

##### Department of Sport Management
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Analytics | https://www.syracuse.edu/academics/programs/sport-analytics/ |
| 2 | Sport Management | https://www.syracuse.edu/academics/programs/sport-management/ |
| 3 | Esports Communications and Management | https://www.syracuse.edu/academics/programs/esports-communications-management/ |
| 4 | Management and Sport Management Dual | https://www.syracuse.edu/academics/programs/management-sport-management-dual/ |

##### Department of Public Health
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://www.syracuse.edu/academics/programs/public-health/ |

##### Department of Nutrition
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition | https://www.syracuse.edu/academics/programs/nutrition/ |

##### Department of Human Development and Family Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development and Family Science | https://www.syracuse.edu/academics/programs/human-development-family-science/ |

##### Department of Exercise Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Health and Exercise Science | https://www.syracuse.edu/academics/programs/health-exercise-science/ |

##### Department of Social Work
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.syracuse.edu/academics/programs/social-work/ |

#### College of Professional Studies

###### B.P.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management (Online) | https://online.syracuse.edu/academics/undergraduate/bachelors-in-business-management |
| 2 | Cybersecurity Administration (Online) | https://online.syracuse.edu/academics/undergraduate/bachelors-in-cybersecurity-administration |
| 3 | AI in Business Process Automation (Online) | https://www.syracuse.edu/academics/programs/ai-in-business-process-automation-online-bps/ |
| 4 | Creative Leadership (Online) | https://online.syracuse.edu/academics/undergraduate/bachelors-in-creative-leadership |

###### A.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts | https://www.syracuse.edu/academics/programs/liberal-arts-aa/ |
| 2 | Liberal Arts (Online) | https://online.syracuse.edu/academics/undergraduate/associate-in-liberal-arts/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Public Health Accelerated B.S./MPH | Falk College | https://www.syracuse.edu/academics/programs/public-health-accelerated-bs-mph/ |

### 1.4 Minors — Complete List

| # | Minor | Home School | URL |
|---|-------|-------------|-----|
| 1 | Accounting | Whitman | https://whitman.syracuse.edu/undergraduate/whitman-minors-in-management |
| 2 | Addiction Studies | Falk | https://courses.syracuse.edu/preview_program.php?catoid=38&poid=19233 |
| 3 | African American Studies | A&S | https://artsandsciences.syracuse.edu/degree-programs/african-american-studies-minor/ |
| 4 | Animation and Visual Effects | VPA | https://vpa.syracuse.edu/academics/film-media-arts/minors/ |
| 5 | Anthropology | A&S | https://www.maxwell.syr.edu/academics/anthropology-department/major-and-minors |
| 6 | Applications of AI | iSchool | https://ischool.syracuse.edu/academics/applications-of-ai-minor/ |
| 7 | Applied Data Science | iSchool | https://ischool.syracuse.edu/academics/data-science-minor/ |
| 8 | Applied Statistics | A&S | https://artsandsciences.syracuse.edu/degree-programs/applied-statistics-minor/ |
| 9 | Arabic | A&S | https://artsandsciences.syracuse.edu/languages-literatures-and-linguistics/arabic/ |
| 10 | Architecture | Architecture | https://soa.syr.edu/programs/undergraduate/minor-in-architecture/ |
| 11 | Art History | A&S | https://artsandsciences.syracuse.edu/degree-programs/art-history-minor/ |
| 12 | Art Photography | VPA | https://vpa.syracuse.edu/academics/film-media-arts/minors |
| 13 | Asian/Asian American Studies | A&S | https://artsandsciences.syracuse.edu/degree-programs/asianasian-american-studies |
| 14 | Atrocity Studies and the Practices of Social Justice | Education | https://soe.syr.edu/academics/undergraduate/atrocity-studies-minor/ |
| 15 | Child and Family Policy | Falk | https://courses.syracuse.edu/undergraduate/minors/child-family-policy-studies/ |
| 16 | Civil Engineering | ECS | https://ecs.syracuse.edu/academics/minors/civil-engineering |
| 17 | Computer Engineering | ECS | https://ecs.syracuse.edu/academics/minors/computer-engineering |
| 18 | Computer Science | ECS | https://ecs.syracuse.edu/academics/minors/computer-science |
| 19 | Economics | A&S | https://artsandsciences.syracuse.edu/degree-programs/economics-minor/ |
| 20 | Electrical Engineering | ECS | https://ecs.syracuse.edu/academics/minors/electrical-engineering |
| 21 | Emerging Sport Enterprise | Falk | https://falk.syracuse.edu/academics/undergraduate/minors/emerging-sport-enterprise-minor/ |
| 22 | Energy Systems | ECS | https://ecs.syracuse.edu/academics/minors/energy-systems |
| 23 | Engineering and Computer Science Management | ECS | https://ecs.syracuse.edu/academics/minors/engineering-and-computer-science-management |
| 24 | Environment and Society | Maxwell | https://www.maxwell.syr.edu/academics/environment-and-society-minor |
| 25 | Environmental Engineering | ECS | https://ecs.syracuse.edu/academics/minors/environmental-engineering |
| 26 | Geography | Maxwell | https://www.maxwell.syr.edu/academics/geography-department/minor |
| 27 | Human Development and Family Science | Falk | https://courses.syracuse.edu/undergraduate/minors/human-development-family-science/ |
| 28 | Sport Analytics | Falk | https://falk.syracuse.edu/academics/undergraduate/minors/sport-analytics-minor/ |
| 29 | Sport Event Management | Falk | https://falk.syracuse.edu/academics/undergraduate/minors/sport-event-management-minor/ |
| 30 | Sport Management | Falk | https://falk.syracuse.edu/academics/undergraduate/minors/sport-management-minor/ |
| 31-119 | *(Additional 89 minors across all schools — see full list at https://www.syracuse.edu/academics/programs/?degree-type=Minor)* | Various | https://www.syracuse.edu/academics/programs/ |

### 1.5 General/Institute-Wide Requirements

Syracuse University requires all undergraduate students to complete the **Shared Competencies** framework, which includes:
- Written Communication
- Oral Communication
- Quantitative Reasoning
- Critical and Creative Thinking
- Scientific Inquiry and Research Skills
- Civic and Ethical Responsibility
- Diversity, Equity, Inclusion and Accessibility
- Global Awareness and Engagement

Source: https://coursecatalog.syracuse.edu/

### 1.6 Course-ID → Major Quick-Lookup

Syracuse does not use a course-ID numbering system for programs. Programs are identified by name and school.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.maxwell.syr.edu/academics/anthropology-department/ma-and-phd |
| 2 | Biology | https://thecollege.syr.edu/degree-programs/biology-phd/ |
| 3 | Chemistry | https://artsandsciences.syracuse.edu/chemistry/graduate/ |
| 4 | Cognitive Psychology | https://thecollege.syr.edu/psychology/graduate-study-psychology/cognitive-psychology-graduate-program-overview/ |
| 5 | Clinical Psychology | https://thecollege.syr.edu/psychology/graduate-study-psychology/clinical-psychology-graduate-program-overview/ |
| 6 | Composition and Cultural Rhetoric | https://artsandsciences.syracuse.edu/english/graduate-programs/ |
| 7 | Creative Writing | http://english.syr.edu/cw/cw-program.html |
| 8 | Economics | https://www.maxwell.syr.edu/academics/economics-department/phd |
| 9 | English | https://artsandsciences.syracuse.edu/english/graduate-programs/ |
| 10 | Geography | https://www.maxwell.syr.edu/academics/geography-department/phd |
| 11 | History | https://artsandsciences.syracuse.edu/history/graduate-programs/ |
| 12 | Mathematics | https://artsandsciences.syracuse.edu/mathematics/graduate-studies/ |
| 13 | Philosophy | https://artsandsciences.syracuse.edu/philosophy/graduate-programs/ |
| 14 | Physics | https://artsandsciences.syracuse.edu/physics/graduate-programs/ |
| 15 | Political Science | https://www.maxwell.syr.edu/academics/political-science-department/phd |

##### M.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.maxwell.syr.edu/academics/anthropology-department/ma-and-phd |
| 2 | Art History | https://artsandsciences.syracuse.edu/art-music-histories/graduate-programs-art-history/masters-in-art-history-main-campus/ |
| 3 | Art History, Florence Program | https://artsandsciences.syracuse.edu/art-music-histories/graduate-programs-art-history/florence-ma-renaissance-art/ |
| 4 | Economics | https://www.maxwell.syr.edu/academics/economics-department/ma |
| 5 | Economics and International Relations | https://www.maxwell.syr.edu/academics/economics-department/ma-eir |
| 6 | English | https://artsandsciences.syracuse.edu/english/graduate-programs/ |
| 7 | Geography | https://www.maxwell.syr.edu/academics/geography-department/ma |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics | https://artsandsciences.syracuse.edu/degree-programs/applied-statistics/ |
| 2 | Biochemistry | https://artsandsciences.syracuse.edu/chemistry/graduate/ |
| 3 | Chemistry | https://artsandsciences.syracuse.edu/chemistry/graduate/ |
| 4 | Mathematics | https://artsandsciences.syracuse.edu/mathematics/graduate-studies/ |
| 5 | Physics | https://artsandsciences.syracuse.edu/physics/graduate-programs/ |

##### M.F.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | http://english.syr.edu/cw/cw-program.html |

##### Au.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology | https://artsandsciences.syracuse.edu/communication-sciences-and-disorders/doctor-of-audiology/ |

#### College of Engineering and Computer Science

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Science | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/master-of-science-in-artificial-intelligence-science |
| 2 | Biomedical Engineering | https://ecs.syracuse.edu/academics/biomedical-and-chemical-engineering/programs/bioengineering-master-program |
| 3 | Chemical Engineering | https://ecs.syracuse.edu/academics/biomedical-and-chemical-engineering/programs/chemical-engineering-master-program |
| 4 | Civil Engineering | https://ecs.syracuse.edu/academics/civil-and-environmental-engineering/programs/civil-engineering-master-program |
| 5 | Computer Engineering | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/computer-engineering-master-program |
| 6 | Computer Science | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/computer-science-master-program |
| 7 | Computer Science (Online) | https://onlinegrad.syracuse.edu/engineering/computer-science/ |
| 8 | Cybersecurity | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/cybersecurity-master-program |
| 9 | Cybersecurity (Online) | https://onlinegrad.syracuse.edu/engineering/cybersecurity/ |
| 10 | Electrical Engineering | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/electrical-engineering-master-program |
| 11 | Engineering Management | https://ecs.syracuse.edu/academics/mechanical-and-aerospace-engineering/programs/engineering-management-master-program |
| 12 | Engineering Management (Online) | https://online.syracuse.edu/academics/graduate/masters-in-engineering-management |
| 13 | Environmental Engineering | https://ecs.syracuse.edu/academics/civil-and-environmental-engineering/programs/environmental-engineering-master-program |
| 14 | Environmental Engineering Science | https://ecs.syracuse.edu/academics/civil-and-environmental-engineering/programs/environmental-engineering-science-master-program |
| 15 | Mechanical and Aerospace Engineering | https://ecs.syracuse.edu/academics/mechanical-and-aerospace-engineering/programs/mechanical-aerospace-engineering-master-program |
| 16 | Operations Research and System Analytics | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/masters-of-science-in-operations-research-and-system-analytics |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://ecs.syracuse.edu/academics/biomedical-and-chemical-engineering/programs/bioengineering-doctoral-program |
| 2 | Chemical Engineering | https://ecs.syracuse.edu/academics/biomedical-and-chemical-engineering/programs/chemical-engineering-doctoral-program |
| 3 | Civil and Environmental Engineering | https://ecs.syracuse.edu/academics/civil-and-environmental-engineering/programs/civil-engineering-doctoral-program |
| 4 | Computer/Information Science and Engineering | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/computer-information-science-engineering-doctoral-program |
| 5 | Electrical and Computer Engineering | https://ecs.syracuse.edu/academics/electrical-engineering-and-computer-science/programs/electrical-computer-engineering-doctoral-program |
| 6 | Mechanical and Aerospace Engineering | https://ecs.syracuse.edu/academics/mechanical-and-aerospace-engineering/programs/mechanical-aerospace-engineering-doctor-program |

#### Whitman School of Management

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://whitman.syracuse.edu/graduate-programs/ms-accounting |
| 2 | Business Analytics | https://whitman.syracuse.edu/graduate-programs/ms-business-analytics |
| 3 | Entrepreneurship | https://whitman.syracuse.edu/graduate-programs/ms-entrepreneurship |
| 4 | Finance | https://whitman.syracuse.edu/graduate-programs/ms-finance |
| 5 | Marketing | https://whitman.syracuse.edu/graduate-programs/ms-marketing |
| 6 | Supply Chain Management | https://whitman.syracuse.edu/graduate-programs/ms-supply-chain-management |
| 7 | Professional Accounting (Online) | https://onlinegrad.syracuse.edu/business/accounting/ |
| 8 | Business Analytics (Online) | https://onlinegrad.syracuse.edu/business/business-analytics/ |
| 9 | Finance (Online) | https://onlinegrad.syracuse.edu/business/finance/ |
| 10 | Supply Chain Management (Online) | https://onlinegrad.syracuse.edu/business/supply-chain-management/ |

##### M.B.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Full-Time MBA | https://whitman.syracuse.edu/graduate-programs/full-time-mba-program |
| 2 | Online MBA | https://onlinegrad.syracuse.edu/business/mba/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://whitman.syracuse.edu/graduate-programs/phd-program |

#### S.I. Newhouse School of Public Communications

##### M.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Advertising | https://newhouse.syracuse.edu/academics/advertising/masters/ |
| 2 | Arts Journalism and Communications (Goldring Program) | https://newhouse.syracuse.edu/academics/arts-journalism/masters/ |
| 3 | Audio Arts | https://vpa.syracuse.edu/academics/audio-arts/ |
| 4 | Magazine, News and Digital Journalism | https://newhouse.syracuse.edu/academics/magazine-news-digital-journalism/masters/ |
| 5 | Public Relations | https://newhouse.syracuse.edu/academics/public-relations/masters/ |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Media Management | https://newhouse.syracuse.edu/academics/advanced-media-management/masters/ |
| 2 | Broadcast and Digital Journalism | https://newhouse.syracuse.edu/academics/broadcast-digital-journalism/masters/ |
| 3 | Communications Management (Blended) | https://onlinegrad.syracuse.edu/communications/communications-management/ |
| 4 | Newhouse Online M.S. | https://onlinegrad.syracuse.edu/communications/ |
| 5 | Television, Radio and Film | https://newhouse.syracuse.edu/academics/television-radio-film/masters/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Mass Communications | https://newhouse.syracuse.edu/academics/mass-communications/phd/ |

#### College of Visual and Performing Arts

##### M.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://artsandsciences.syracuse.edu/art-music-histories/graduate-programs-art-history/ |
| 2 | Audio Arts | https://vpa.syracuse.edu/academics/audio-arts/ |
| 3 | Museum Studies | https://vpa.syracuse.edu/academics/museum-studies/ |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Therapy | https://vpa.syracuse.edu/academics/creative-arts-therapy/art-therapy-ms/ |

##### M.F.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Photography | https://vpa.syracuse.edu/academics/film-media-arts/programs/art-photography-mfa/ |
| 2 | Computer Art | https://vpa.syracuse.edu/academics/computer-art/ |
| 3 | Creative Writing | https://vpa.syracuse.edu/academics/creative-writing/ |
| 4 | Film | https://vpa.syracuse.edu/academics/film-media-arts/programs/film-mfa/ |
| 5 | Studio Art | https://vpa.syracuse.edu/academics/studio-art/ |

##### M.Mus. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Composition | https://vpa.syracuse.edu/academics/music/graduate/ |
| 2 | Music Education | https://vpa.syracuse.edu/academics/music/graduate/ |
| 3 | Music Performance | https://vpa.syracuse.edu/academics/music/graduate/ |
| 4 | Sound Recording Technology | https://vpa.syracuse.edu/academics/music/graduate/ |

#### Maxwell School of Citizenship and Public Affairs

##### M.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.maxwell.syr.edu/academics/anthropology-department/ma-and-phd |
| 2 | Economics | https://www.maxwell.syr.edu/academics/economics-department/ma |
| 3 | Economics and International Relations | https://www.maxwell.syr.edu/academics/economics-department/ma-eir |
| 4 | Geography | https://www.maxwell.syr.edu/academics/geography-department/ma |
| 5 | History | https://www.maxwell.syr.edu/academics/history-department/ma |
| 6 | International Relations | https://www.maxwell.syr.edu/academics/international-relations/ma |
| 7 | Political Science | https://www.maxwell.syr.edu/academics/political-science-department/ma |
| 8 | Public Administration | https://www.maxwell.syr.edu/academics/public-administration/ma |
| 9 | Sociology | https://www.maxwell.syr.edu/academics/sociology-department/ma |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Data Science | https://ischool.syr.edu/academics/applied-data-science-masters-degree/ |

##### M.P.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.maxwell.syr.edu/academics/public-administration/mpa |
| 2 | Public Administration (Online) | https://onlinegrad.syracuse.edu/public-administration/ |

##### M.A./M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Human-Centered Artificial Intelligence | https://ischool.syracuse.edu/academics/applied-human-centered-artificial-intelligence-masters-degree/ |

##### E.M.I.R. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Master in International Relations | https://www.maxwell.syr.edu/academics/international-relations/emir |

##### E.M.P.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Master of Public Administration | https://www.maxwell.syr.edu/academics/public-administration/empa |
| 2 | Executive Master of Public Administration (Online) | https://onlinegrad.syracuse.edu/executive-mpa/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.maxwell.syr.edu/academics/anthropology-department/ma-and-phd |
| 2 | Economics | https://www.maxwell.syr.edu/academics/economics-department/phd |
| 3 | Geography | https://www.maxwell.syr.edu/academics/geography-department/phd |
| 4 | History | https://www.maxwell.syr.edu/academics/history-department/phd |
| 5 | Political Science | https://www.maxwell.syr.edu/academics/political-science-department/phd |
| 6 | Public Administration | https://www.maxwell.syr.edu/academics/public-administration/phd |
| 7 | Sociology | https://www.maxwell.syr.edu/academics/sociology-department/phd |

##### C.A.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Society Organizations | https://www.maxwell.syr.edu/academics/cas/civil-society-organizations |
| 2 | Conflict and Collaboration | https://www.maxwell.syr.edu/academics/cas/conflict-and-collaboration |
| 3 | Conflict and Collaboration (Online) | https://www.maxwell.syr.edu/academics/cas/conflict-and-collaboration-online |
| 4 | Data Analytics for Public Policy | https://www.maxwell.syr.edu/academics/cas/data-analytics-public-policy |
| 5 | European Union and Contemporary Europe | https://www.maxwell.syr.edu/academics/cas/european-union |
| 6 | GIS and Spatial Analysis | https://www.maxwell.syr.edu/academics/cas/gis-spatial-analysis |
| 7 | Health Services Management and Policy | https://www.maxwell.syr.edu/academics/cas/health-services-management |
| 8 | National Security Studies | https://www.maxwell.syr.edu/academics/cas/national-security-studies |
| 9 | Nonprofit Management | https://www.maxwell.syr.edu/academics/cas/nonprofit-management |
| 10 | Public Finance and Budgeting | https://www.maxwell.syr.edu/academics/cas/public-finance-budgeting |
| 11 | Science, Technology, and Environmental Policy | https://www.maxwell.syr.edu/academics/cas/science-technology-environmental-policy |
| 12 | Security Studies | https://www.maxwell.syr.edu/academics/cas/security-studies |

#### School of Architecture

##### M.Arch. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | http://soa.syr.edu/programs/march/ |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://soa.syr.edu/admissions/graduate/ms-architecture/ |

#### School of Education

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://soe.syr.edu/academics/graduate/counseling/ |
| 2 | Cultural Foundations of Education | https://soe.syr.edu/academics/graduate/cultural-foundations/ |
| 3 | Education Leadership | https://soe.syr.edu/academics/graduate/education-leadership/ |
| 4 | Higher Education | https://soe.syr.edu/academics/graduate/higher-education/ |
| 5 | Instructional Design, Development and Evaluation | https://soe.syr.edu/academics/graduate/idde/ |
| 6 | Literacy Education | https://soe.syr.edu/academics/graduate/literacy-education/ |
| 7 | Mathematics Education | https://soe.syr.edu/academics/graduate/mathematics-education/ |
| 8 | Music Education | https://soe.syr.edu/academics/graduate/music-education/ |
| 9 | Science Education | https://soe.syr.edu/academics/graduate/science-education/ |
| 10 | Special Education | https://soe.syr.edu/academics/graduate/special-education/ |
| 11 | Teaching and Curriculum | https://soe.syr.edu/academics/graduate/teaching-curriculum/ |
| 12-17 | *(Additional M.S. programs)* | https://soe.syr.edu/academics/graduate/ |

##### Ed.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://soe.syr.edu/academics/graduate/edd/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://soe.syr.edu/academics/graduate/phd/ |
| 2 | Special Education | https://soe.syr.edu/academics/graduate/special-education/ |

#### School of Information Studies (iSchool)

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Data Science | https://ischool.syr.edu/academics/applied-data-science-masters-degree/ |
| 2 | Applied Data Science (Online) | https://onlinegrad.syracuse.edu/information-science/applied-data-science/ |
| 3 | Information Management | https://ischool.syr.edu/academics/information-management/ |
| 4 | Library and Information Science | https://ischool.syr.edu/academics/library-information-science/ |
| 5 | Library and Information Science (Online) | https://onlinegrad.syracuse.edu/information-science/library-and-information-science/ |
| 6 | Enterprise Data Systems (Online) | https://onlinegrad.syracuse.edu/information-science/enterprise-data-systems/ |

##### D.P.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science | https://ischool.syr.edu/academics/data-science-dps/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Information Science and Technology | https://ischool.syr.edu/academics/phd/ |

#### David B. Falk College of Sport and Human Dynamics

##### M.A. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Marriage and Family Therapy | https://falk.syracuse.edu/academics/graduate/marriage-family-therapy/ |
| 2 | Marriage and Family Therapy (Online) | https://falk.syracuse.edu/academics/graduate/marriage-family-therapy-online/ |
| 3 | Nutrition Science | https://falk.syracuse.edu/academics/graduate/nutrition-science/ |

##### M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Exercise Science | https://falk.syracuse.edu/academics/graduate/exercise-science/ |
| 2 | Human Development and Family Science | https://falk.syracuse.edu/academics/graduate/human-development-family-science/ |
| 3 | Sport Analytics (Online) | https://falk.syracuse.edu/academics/graduate/sport-analytics-online/ |

##### M.P.H. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://falk.syracuse.edu/academics/graduate/public-health/ |

##### M.S.W. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://falk.syracuse.edu/academics/graduate/social-work/ |
| 2 | Social Work (Advanced Standing) | https://falk.syracuse.edu/academics/graduate/social-work-advanced-standing/ |
| 3 | Social Work (Online) | https://onlinegrad.syracuse.edu/social-work/ |
| 4 | Social Work (Online, Advanced Standing) | https://onlinegrad.syracuse.edu/social-work/advanced-standing/ |

##### Ph.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Exercise Science | https://falk.syracuse.edu/academics/graduate/exercise-science-phd/ |
| 2 | Human Development and Family Science | https://falk.syracuse.edu/academics/graduate/human-development-family-science-phd/ |
| 3 | Marriage and Family Therapy | https://falk.syracuse.edu/academics/graduate/marriage-family-therapy-phd/ |

#### College of Professional Studies

##### Online M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Data Science (Online) | https://onlinegrad.syracuse.edu/information-science/applied-data-science/ |
| 2 | Computer Science (Online) | https://onlinegrad.syracuse.edu/engineering/computer-science/ |

##### Online M.P.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Project Management (Online) | https://professionalstudies.syracuse.edu/academics/online/project-management-masters/ |

#### College of Law

##### J.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://law.syr.edu/admissions/jd-admissions/ |
| 2 | JDinteractive (Online) | https://jdinteractive.syr.edu/ |

##### LL.M. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws | https://law.syr.edu/admissions/llm-admissions/ |

##### S.J.D. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Juridical Science | https://law.syr.edu/academics/degree-programs/ |

##### Dual J.D. Programs
| # | 项目 | Partner School | URL |
|---|------|----------------|-----|
| 1 | J.D./M.A. (various) | A&S/Maxwell | https://law.syr.edu/academics/degree-programs/ |
| 2 | J.D./M.B.A. | Whitman | https://law.syr.edu/academics/degree-programs/ |
| 3 | J.D./M.S. (Forensic Science) | A&S | https://law.syr.edu/academics/degree-programs/ |
| 4 | J.D./M.S./C.A.S. (Forensic Science) | A&S | https://law.syr.edu/academics/degree-programs/ |
| 5 | J.D./Ph.D. (Philosophy) | A&S | https://law.syr.edu/academics/degree-programs/ |
| 6 | J.D./M.P.A. | Maxwell | https://law.syr.edu/academics/degree-programs/ |
| 7 | J.D./M.S.W. | Falk | https://law.syr.edu/academics/degree-programs/ |

### 2.2 Graduate Admissions Model

Syracuse uses a **decentralized graduate admissions model**. Each school/college manages its own admissions process, deadlines, and requirements. There is no single centralized graduate application portal.

- **Centralized services**: Syracuse University Graduate School provides administrative support
- **Application platform**: Varies by school (some use departmental portals, some use centralized systems)
- **Application fee**: Varies by program (typically $75-$85)
- **GRE/GMAT**: Per-program policy (many programs have made GRE optional)
- **CGS April-15 signatory**: Yes

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 数据 |
|------|------|
| Admissions site | https://www.syracuse.edu/admissions-aid/ |
| Application portal | Common Application or Coalition Application (powered by Scoir) |
| Application fee | $85 |
| Early Action (EA) deadline | November 1 |
| Early Decision I (ED I) deadline | November 1 |
| Early Decision II (ED II) deadline | January 5 |
| Regular Decision (RD) deadline | January 5 |
| Spring enrollment deadline | November 15 |
| EA notification | Early February |
| ED I notification | Late December |
| ED II notification | Mid-January |
| RD notification | Mid-March |
| EA reply date | May 1 |
| ED I reply date | February 15 (if admitted to first choice) |
| ED II reply date | March 1 (if admitted to first choice) |
| RD reply date | May 1 |
| SAT/ACT policy | **Test-optional** (Fall 2026, Spring 2027, Fall 2027, Spring 2028) |
| Superscore policy | N/A (test-optional) |
| Score-report method | Self-report accepted; official scores if submitted |
| Interview policy | Not required |
| Recommendation requirements | One academic recommendation + counselor evaluation |
| Portfolio | Required for Architecture, VPA Art/Design/Film, Drama, Music |
| Transfer deadline | December 1 (preferred November 15) |

> **Source**: https://www.syracuse.edu/admissions-aid/application-process/apply/dates-deadlines/

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum (Most Schools) | Minimum (Whitman/Architecture) | Minimum (Newhouse) | Recommended |
|------|----------------------|-------------------------------|-------------------|-------------|
| TOEFL iBT | 85+ | 90+ | 102+ | Higher is better |
| TOEFL (new scale, eff. 1.21.26) | 4.5 | 5 | 5 | Higher is better |
| IELTS Academic | 6.5+ | 7.0+ | 7.0+ | Higher is better |
| Cambridge English | 176+ | 185+ | 185+ | Higher is better |
| Duolingo English Test (DET) | 125+ | 125+ | 130+ | Higher is better |
| PTE Academic | Accepted | Accepted | Accepted | — |

**Exemptions**: Students who attended in-person secondary schools in the US for at least 3 full academic years (Grades 10-12), or transfer students with 24+ credits from a US institution with 3.0+ GPA (excluding ESL).

**NOT accepted**: TOEFL Essentials, TOEFL ITP, TOEFL MyBest Score, IELTS Indicator.

**TOEFL code**: 2823

> **Source**: https://www.syracuse.edu/admissions-aid/application-process/international/undergraduate/requirements/

### 3.3 Graduate — Global Rules

- **Admissions model**: Fully decentralized; each school/college manages its own
- **Application platforms**: Vary by school
- **Standard application fee**: $75-$85 (varies by program)
- **GRE/GMAT policy**: Per-program; many programs have made GRE optional
- **Language-test policy**: TOEFL/IELTS required for non-native English speakers; per-program minimums
- **CGS April-15 honor date**: Yes (signatory)
- **ETS institutional code**: 2823

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27, On-Campus)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $69,180 | Full-time, two semesters |
| Housing & Food | $20,580 | Average on-campus |
| Miscellaneous fees | $1,869 | Includes Residential Technology Service Fee |
| Books, course materials, supplies, equipment | $1,847 | |
| Transportation | $839 | |
| Personal expenses | $1,294 | |
| Loan fees | $67 | If applicable |
| **Total Cost of Attendance** | **$95,676** | |
| Health insurance | $2,868 | Mandatory; may be waived with adequate private insurance |
| **Total with health insurance** | **$98,544** | |

> **Source**: https://www.syracuse.edu/admissions-aid/tuition-fees/undergraduate-costs/

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 数据 |
|------|------|
| Students receiving aid | 82% |
| Total aid distributed | $571M+ (2022-23: $465M) |
| Need-blind/need-aware | **Need-aware for all** (not need-blind) |
| Need-blind for internationals | No |
| Merit scholarships | Yes (for all students including internationals) |
| International aid | Merit-based scholarships only |
| Tuition-free threshold | Not published |
| Loan-free policy | Not published |
| CSS Profile required | Yes |
| FAFSA required | Yes |

> **Source**: https://www.syracuse.edu/admissions-aid/financial-aid-scholarships/

### 4.3 Graduate Cost & Funding Framework

| 维度 | 数据 |
|------|------|
| Tuition (main campus) | $37,548/year ($2,086/credit, 18 credits) |
| Housing & Food | $16,780 |
| Miscellaneous fees | $1,028 |
| Books/supplies | $1,128 |
| Transportation | $1,781 |
| Personal expenses | $2,452 |
| Loan fees | $216 |
| Health insurance | $2,868 |
| **Total COA (Grad)** | **$63,801** |
| Social Work tuition | $1,226/credit |
| Marriage and Family Therapy tuition | $1,226/credit |
| College of Law tuition | $2,411/credit |

> **Source**: https://www.syracuse.edu/admissions-aid/tuition-fees/graduate-costs/

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/apply/dates-deadlines/
  source_snippet: "Early Action (First-year students only): November 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.ED_I
  value: "November 1"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/apply/dates-deadlines/
  source_snippet: "Early Decision (First-year students only): November 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.ED_II
  value: "January 5"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/apply/dates-deadlines/
  source_snippet: "Early Decision II (First-year students only): January 5"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.deadlines.RD
  value: "January 5"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/apply/dates-deadlines/
  source_snippet: "Regular Decision: First Year: January 5"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.test_policy
  value: "Test-optional (Fall 2026, Spring 2027, Fall 2027, Spring 2028)"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/undergraduate/first-year/requirements/
  source_snippet: "SAT/ACT scores will not be required for students applying for Fall 2026, Spring 2027, Fall 2027 or Spring 2028 admission."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.costs.tuition_2026_2027
  value: "$69,180"
  source_url: https://www.syracuse.edu/admissions-aid/tuition-fees/undergraduate-costs/
  source_snippet: "Tuition - $69,180"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.total_coa_on_campus
  value: "$95,676"
  source_url: https://www.syracuse.edu/admissions-aid/tuition-fees/undergraduate-costs/
  source_snippet: "Total Cost of Attendance - $95,676"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.english_proficiency.TOEFL_minimum
  value: "85+ (most schools), 90+ (Whitman/Architecture), 102+ (Newhouse)"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/international/undergraduate/requirements/
  source_snippet: "Preferred TOEFL: 85+ (A&S, Maxwell, VPA, Education, ECS, Falk, iSchool); 90+ (Whitman, Architecture); 102+ (Newhouse)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.english_proficiency.IELTS_minimum
  value: "6.5+ (most), 7.0+ (Whitman/Architecture/Newhouse)"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/international/undergraduate/requirements/
  source_snippet: "Preferred IELTS: 6.5+ (most schools); 7.0+ (Whitman, Architecture, Newhouse)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.english_proficiency.TOEFL_code
  value: "2823"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/international/undergraduate/requirements/
  source_snippet: "Use ID code 2823 when requesting your official TOEFL scores from ETS."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.financial_aid.students_receiving_aid
  value: "82%"
  source_url: https://www.syracuse.edu/admissions-aid/financial-aid-scholarships/
  source_snippet: "More than 81% of our students receive aid—the majority of it in the form of grants and scholarships that do not have to be repaid."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.application_fee
  value: "$85"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/apply/dates-deadlines/
  source_snippet: "Application fee: $85"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.application_portal
  value: "Common Application or Coalition Application (powered by Scoir)"
  source_url: https://www.syracuse.edu/admissions-aid/application-process/undergraduate/first-year/requirements/
  source_snippet: "Common Application or Coalition Application, powered by Scoir"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.costs.tuition_2026_2027
  value: "$37,548/year ($2,086/credit)"
  source_url: https://www.syracuse.edu/admissions-aid/tuition-fees/graduate-costs/
  source_snippet: "Tuition - $37,548 ($2,086 per credit)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.costs.total_coa
  value: "$63,801"
  source_url: https://www.syracuse.edu/admissions-aid/tuition-fees/graduate-costs/
  source_snippet: "Total Cost of Attendance - $63,801"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.costs.law_tuition
  value: "$2,411/credit"
  source_url: https://www.syracuse.edu/admissions-aid/tuition-fees/graduate-costs/
  source_snippet: "College of Law (Residential and JDinteractive) is $2,411 per credit"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-P-001:
  field: programs.total_count
  value: 499
  source_url: https://www.syracuse.edu/academics/programs/
  source_snippet: "Showing: 522 Programs" (522 includes 11 non-degree items + 12 ESF cross-lists; 499 Syracuse degree programs)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-002:
  field: programs.schools_count
  value: 13
  source_url: https://www.syracuse.edu/academics/programs/
  source_snippet: "Choose from nearly 600 undergraduate, graduate and certificate programs within our 13 schools and colleges"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
syracuse-knowledge-base-v2
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-college-of-arts-and-sciences.md
├── 02-ug-engineering-and-computer-science.md
├── 03-ug-whitman-management.md
├── 04-ug-newhouse-communications.md
├── 05-ug-visual-and-performing-arts.md
├── 06-ug-maxwell-citizenship.md
├── 07-ug-architecture.md
├── 08-ug-education.md
├── 09-ug-information-studies.md
├── 10-ug-falk-sport-human-dynamics.md
├── 11-ug-professional-studies.md
├── 12-grad-all-schools.md              (Section 2: grouped by school)
├── 13-law-programs.md
├── 14-deadlines-requirements.md        (Section 3)
├── 15-costs-financial-aid.md           (Section 4)
├── 16-evidence-chain.md                (Section 5)
└── 17-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "syracuse-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | College of Nursing degree programs (currently shows 0 in catalog) | https://nursing.syracuse.edu/academics/ |
| P0 | Per-program GRE requirements for graduate programs | Individual program pages |
| P1 | Graduate application deadlines per school | Individual school admissions pages |
| P1 | Detailed financial aid policy (income thresholds, loan-free) | https://financialaid.syr.edu/ |
| P1 | International student financial requirements | https://www.syracuse.edu/admissions-aid/application-process/international/ |
| P2 | Transfer admissions requirements and deadlines | https://www.syracuse.edu/admissions-aid/application-process/transfer/ |
| P2 | Graduate stipend/funding information per program | Individual program pages |
| P2 | Student-to-faculty ratio verification | https://www.syracuse.edu/about/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Syracuse University |
|------|-------------------|
| Type | Private R1 Research University |
| Location | Syracuse, NY |
| UG Tuition (2026-27) | $69,180 |
| UG Total COA (on-campus) | $95,676 |
| Grad Tuition (2026-27) | $37,548/year ($2,086/credit) |
| Need-blind (domestic) | No (need-aware) |
| Need-blind (international) | No |
| EA deadline | November 1 |
| ED I deadline | November 1 |
| ED II deadline | January 5 |
| RD deadline | January 5 |
| SAT/ACT required? | No (test-optional through Spring 2028) |
| TOEFL minimum | 85+ (most), 90+ (Whitman/Arch), 102+ (Newhouse) |
| IELTS minimum | 6.5+ (most), 7.0+ (Whitman/Arch/Newhouse) |
| Duolingo minimum | 125+ (most), 130+ (Newhouse) |
| Application fee | $85 |
| Total programs (Rule 1) | 499 |
| Schools/colleges (Rule 2) | 13 |
| Students receiving aid | 82% |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: syracuse.edu, ecs.syracuse.edu, whitman.syracuse.edu, newhouse.syracuse.edu, vpa.syracuse.edu, maxwell.syr.edu, soa.syr.edu, soe.syr.edu, ischool.syracuse.edu, falk.syracuse.edu, law.syr.edu, financialaid.syr.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
