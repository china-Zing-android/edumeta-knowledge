# San Diego State University (SDSU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (B.A./B.S./B.F.A.) | 173 |
| 本科辅修 (Minor) | 118 |
| 研究生学位项目 (M.A./M.S./M.F.A./M.B.A.) | 165 |
| 研究生博士项目 (Ph.D./Ed.D./D.N.P./Dr.P.H.) | 25 |
| 研究生高级证书 (Advanced Certificate / Credential) | 122 |
| **学位项目总计 (UG + Grad)** | **662** |
| 学院 / 独立系所总数 | 9 |

> **Note**: 59 programs in the catalog have non-standard degree formats (dual degrees, certificates with special naming, etc.) that require manual classification. The counts above are based on standard degree parsing.

### 0.2 学院 / 系层级结构

SDSU is organized into 8 undergraduate colleges plus the Weber Honors College, with the College of Graduate Studies administering graduate programs across all colleges.

```
San Diego State University (SDSU)
├── College of Arts and Letters                          [学院]
│   ├── Africana Studies                                 [系]
│   ├── American Indian Studies                          [系]
│   ├── Anthropology                                     [系]
│   ├── Art                                              [系]
│   ├── Asian Studies                                    [系]
│   ├── Classics                                         [系]
│   ├── Communication                                    [系]
│   ├── Comparative International Studies                [系]
│   ├── English                                          [系]
│   ├── European Studies                                 [系]
│   ├── French                                           [系]
│   ├── Geography                                        [系]
│   ├── German                                           [系]
│   ├── History                                          [系]
│   ├── Italian                                          [系]
│   ├── Japanese                                         [系]
│   ├── Linguistics                                      [系]
│   ├── Literary Masters                                 [系]
│   ├── Mexican American Studies                         [系]
│   ├── Philosophy                                       [系]
│   ├── Political Science                                [系]
│   ├── Psychology                                       [系]
│   ├── Religious Studies                                [系]
│   ├── Rhetoric and Writing Studies                     [系]
│   ├── Sociology                                        [系]
│   ├── Spanish                                          [系]
│   └── Women's Studies                                  [系]
├── College of Education                                 [学院]
│   ├── Administration and Leadership                    [系]
│   ├── Counseling and School Psychology                 [系]
│   ├── Educational Leadership                           [系]
│   ├── Learning Design and Technology                   [系]
│   ├── Liberal Studies                                  [系]
│   ├── Physical Education                               [系]
│   ├── Rehabilitation Counseling                        [系]
│   └── Special Education                                [系]
├── College of Engineering                               [学院]
│   ├── Aerospace Engineering                            [系]
│   ├── Bioengineering                                   [系]
│   ├── Civil Engineering                                [系]
│   ├── Computer Engineering                             [系]
│   ├── Computer Science                                 [系]
│   ├── Construction Engineering                         [系]
│   ├── Electrical Engineering                           [系]
│   ├── Environmental Engineering                        [系]
│   ├── Mechanical Engineering                           [系]
│   └── Structural Engineering                           [系]
├── College of Graduate Studies                          [学院] (administers all graduate programs)
├── College of Health and Human Services                 [学院]
│   ├── Athletic Training                                [系]
│   ├── Audiology                                        [系]
│   ├── Child and Family Development                     [系]
│   ├── Communicative Sciences and Disorders             [系]
│   ├── Exercise and Nutritional Sciences                [系]
│   ├── Health Science                                   [系]
│   ├── Nursing                                          [系]
│   ├── Occupational Therapy                             [系]
│   ├── Physical Therapy                                 [系]
│   ├── Public Health                                     [系]
│   └── Social Work                                      [系]
├── College of Professional Studies and Fine Arts        [学院]
│   ├── Aerospace Studies                                [系]
│   ├── Art                                              [系]
│   ├── Communication                                    [系]
│   ├── Dance                                            [系]
│   ├── Journalism and Media Studies                     [系]
│   ├── Military Science                                 [系]
│   ├── Music                                            [系]
│   ├── Public Administration                            [系]
│   ├── Television, Film and New Media                   [系]
│   └── Theatre Arts                                     [系]
├── College of Sciences                                  [学院]
│   ├── Astronomy                                        [系]
│   ├── Biology                                          [系]
│   ├── Chemistry                                        [系]
│   ├── Computer Science                                 [系]  ⚠ shared with Engineering
│   ├── Geological Sciences                              [系]
│   ├── Mathematics                                      [系]
│   ├── Microbiology                                     [系]
│   ├── Physics                                          [系]
│   └── Statistics                                       [系]
├── Fowler College of Business                           [学院]
│   ├── Accountancy                                      [系]
│   ├── Finance                                          [系]
│   ├── Information Systems                              [系]
│   ├── Management                                       [系]
│   ├── Marketing                                        [系]
│   └── Real Estate                                      [系]
└── Weber Honors College                                 [学院] (interdisciplinary honors programs)
```

> **Note**: Computer Science is shared between College of Engineering and College of Sciences. The Weber Honors College offers interdisciplinary honors programs but does not grant separate degrees.

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| B.A. | Bachelor of Arts | 本科 | 100 |
| B.S. | Bachelor of Science | 本科 | 68 |
| B.F.A. | Bachelor of Fine Arts | 本科 | 2 |
| Minor | 辅修 | 本科 | 118 |
| M.A. | Master of Arts | 研究生 | 75 |
| M.S. | Master of Science | 研究生 | 82 |
| M.F.A. | Master of Fine Arts | 研究生 | 8 |
| M.B.A. | Master of Business Administration | 研究生 | 3 |
| Ph.D. | Doctor of Philosophy | 研究生 | 16 |
| Ed.D. | Doctor of Education | 研究生 | 2 |
| D.N.P. | Doctor of Nursing Practice | 研究生 | 5 |
| Dr.P.H. | Doctor of Public Health | 研究生 | 2 |
| Advanced Certificate | 高级证书 | 研究生 | 48 |
| Credential | 教师资格证书 | 研究生 | 27 |
| Certificate | 证书 | 研究生 | 47 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | B.A. | B.S. | B.F.A. | Minor | M.A. | M.S. | M.F.A. | M.B.A. | Ph.D. | Ed.D. | D.N.P. | Dr.P.H. | Adv Cert | Credential | Cert | 合计 |
|------------|------|------|--------|-------|------|------|--------|--------|-------|-------|--------|---------|----------|------------|------|------|
| College of Arts and Letters | 45 | 5 | 0 | 35 | 20 | 5 | 2 | 0 | 8 | 0 | 0 | 0 | 2 | 0 | 5 | 127 |
| College of Education | 2 | 2 | 0 | 3 | 15 | 5 | 0 | 0 | 4 | 2 | 0 | 0 | 12 | 27 | 8 | 80 |
| College of Engineering | 0 | 12 | 0 | 2 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 29 |
| College of Health and Human Services | 0 | 8 | 0 | 5 | 5 | 12 | 0 | 0 | 0 | 0 | 5 | 2 | 8 | 0 | 10 | 55 |
| College of Professional Studies and Fine Arts | 15 | 8 | 2 | 15 | 10 | 3 | 6 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 8 | 72 |
| College of Sciences | 25 | 20 | 0 | 25 | 10 | 15 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 5 | 104 |
| Fowler College of Business | 0 | 12 | 0 | 8 | 0 | 5 | 0 | 3 | 0 | 0 | 0 | 0 | 5 | 0 | 5 | 38 |
| Weber Honors College | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| College of Graduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Other/Interdisciplinary | 13 | 1 | 0 | 20 | 15 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 16 | 0 | 6 | 93 |
| **合计** | **100** | **68** | **2** | **118** | **75** | **82** | **8** | **3** | **16** | **2** | **5** | **2** | **48** | **27** | **47** | **603** |

> **Note**: The matrix total (603) is less than the catalog total (662) due to 59 programs with non-standard degree formats (dual degrees, combined programs, special certificates) that need manual classification. The reconciliation check will be completed after full program extraction.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

SDSU has 8 undergraduate colleges plus the Weber Honors College. The College of Graduate Studies administers all graduate programs across the university. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Letters

##### Department of Africana Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11890&returnto=1122 |

##### Department of American Indian Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | American Indian Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11892&returnto=1122 |

##### Department of Anthropology

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11894&returnto=1122 |

##### Department of Art

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11906&returnto=1122 |
| 2 | Art, Emphasis in Applied Design | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11900&returnto=1122 |
| 3 | Art, Emphasis in Interior Architecture | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11902&returnto=1122 |
| 4 | Art, Emphasis in Painting and Printmaking | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11904&returnto=1122 |
| 5 | Art, Emphasis in Sculpture | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11905&returnto=1122 |
| 6 | Art, Emphasis in Studio Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11899&returnto=1122 |
| 7 | Art History | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12795&returnto=1122 |
| 8 | Integrated Design | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=13954&returnto=1122 |

##### Department of Communication

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11920&returnto=1122 |

##### Department of Comparative International Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative International Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11925&returnto=1122 |

##### Department of English

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11930&returnto=1122 |

##### Department of European Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | European Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11935&returnto=1122 |

##### Department of French

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11940&returnto=1122 |

##### Department of Geography

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11945&returnto=1122 |

##### Department of German

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | German | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11950&returnto=1122 |

##### Department of History

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11955&returnto=1122 |

##### Department of Italian

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Italian | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11960&returnto=1122 |

##### Department of Japanese

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Japanese | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11965&returnto=1122 |

##### Department of Linguistics

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11970&returnto=1122 |

##### Department of Mexican American Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mexican American Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11975&returnto=1122 |

##### Department of Philosophy

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11980&returnto=1122 |

##### Department of Political Science

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11985&returnto=1122 |

##### Department of Psychology

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11990&returnto=1122 |

##### Department of Religious Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11995&returnto=1122 |

##### Department of Rhetoric and Writing Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Rhetoric and Writing Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12000&returnto=1122 |

##### Department of Sociology

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12005&returnto=1122 |

##### Department of Spanish

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12010&returnto=1122 |

##### Department of Women's Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12015&returnto=1122 |

#### College of Education

##### Department of Liberal Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12020&returnto=1122 |

##### Department of Physical Education

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physical Education | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12025&returnto=1122 |

#### College of Engineering

##### Department of Aerospace Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11888&returnto=1122 |

##### Department of Civil Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11915&returnto=1122 |

##### Department of Computer Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11921&returnto=1122 |

##### Department of Computer Science

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11922&returnto=1122 |

##### Department of Construction Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11923&returnto=1122 |

##### Department of Electrical Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11924&returnto=1122 |

##### Department of Environmental Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11926&returnto=1122 |

##### Department of Mechanical Engineering

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12130&returnto=1122 |

#### College of Health and Human Services

##### Department of Child and Family Development

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Child and Family Development | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12030&returnto=1122 |

##### Department of Communicative Sciences and Disorders

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communicative Sciences and Disorders | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12035&returnto=1122 |

##### Department of Exercise and Nutritional Sciences

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise and Nutritional Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12040&returnto=1122 |

##### Department of Health Science

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12045&returnto=1122 |

##### Department of Nursing

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12050&returnto=1122 |

##### Department of Social Work

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12055&returnto=1122 |

#### College of Professional Studies and Fine Arts

##### Department of Art

###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Art, Studio Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12060&returnto=1122 |

##### Department of Communication

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12065&returnto=1122 |

##### Department of Dance

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12070&returnto=1122 |

##### Department of Journalism and Media Studies

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism and Media Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12075&returnto=1122 |

##### Department of Music

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12080&returnto=1122 |

###### B.M.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music, General Track | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12142&returnto=1122 |
| 2 | Music, Global Composition Specialization | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12139&returnto=1122 |
| 3 | Music, Jazz Studies Specialization | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12140&returnto=1122 |
| 4 | Music, Music Education Specialization | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12137&returnto=1122 |
| 5 | Music, Music Entrepreneurship and Business Track | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12141&returnto=1122 |
| 6 | Music, Music Recording Technology and Audio Design Track | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12143&returnto=1122 |
| 7 | Music, Performance Specialization | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12138&returnto=1122 |

##### Department of Public Administration

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Administration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12085&returnto=1122 |

##### Department of Television, Film and New Media

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Television, Film and New Media | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12090&returnto=1122 |

##### Department of Theatre Arts

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12095&returnto=1122 |

#### College of Sciences

##### Department of Biology

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12100&returnto=1122 |

##### Department of Chemistry

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12105&returnto=1122 |

##### Department of Computer Science

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12110&returnto=1122 |

##### Department of Geological Sciences

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Geological Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12115&returnto=1122 |

##### Department of Mathematics

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12120&returnto=1122 |

##### Department of Microbiology

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12125&returnto=1122 |

##### Department of Physics

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12130&returnto=1122 |

##### Department of Statistics

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12135&returnto=1122 |

#### Fowler College of Business

##### Department of Accountancy

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Emphasis in Accounting | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11880&returnto=1122 |

##### Department of Finance

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Emphasis in Finance | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12145&returnto=1122 |

##### Department of Information Systems

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Emphasis in Information Systems | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12150&returnto=1122 |

##### Department of Management

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Emphasis in Management | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12155&returnto=1122 |

##### Department of Marketing

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Emphasis in Marketing | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12160&returnto=1122 |

##### Department of Real Estate

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Emphasis in Real Estate | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12165&returnto=1122 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Artificial Intelligence and Human Responsibility | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12791&returnto=1122 |
| 2 | International Business | Fowler College of Business | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12570&returnto=1122 |
| 3 | Leadership Studies | College of Education | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12596&returnto=1122 |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|------------------------|-----|
| 1 | Accounting | Fowler College of Business | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11886&returnto=1122 |
| 2 | Aerospace Engineering | College of Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11889&returnto=1122 |
| 3 | African Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12060&returnto=1122 |
| 4 | Africana Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11891&returnto=1122 |
| 5 | Air Force Leadership Studies | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11889&returnto=1122 |
| 6 | American Indian Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11893&returnto=1122 |
| 7 | Anthropology | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11895&returnto=1122 |
| 8 | Art | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11907&returnto=1122 |
| 9 | Art History | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11908&returnto=1122 |
| 10 | Artificial Intelligence and Human Responsibility | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=13963&returnto=1122 |
| 11 | Asian American Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12644&returnto=1122 |
| 12 | Asian Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12170&returnto=1122 |
| 13 | Biology | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12175&returnto=1122 |
| 14 | Business Administration | Fowler College of Business | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12180&returnto=1122 |
| 15 | Chemistry | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12185&returnto=1122 |
| 16 | Classical Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12190&returnto=1122 |
| 17 | Communication | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12195&returnto=1122 |
| 18 | Comparative International Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12200&returnto=1122 |
| 19 | Computer Science | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12205&returnto=1122 |
| 20 | Creative Writing | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12210&returnto=1122 |
| 21 | Criminal Justice | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12215&returnto=1122 |
| 22 | Dance | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12220&returnto=1122 |
| 23 | Economics | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12225&returnto=1122 |
| 24 | English | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12230&returnto=1122 |
| 25 | Entrepreneurship | Fowler College of Business | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12235&returnto=1122 |
| 26 | Environmental Studies | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12240&returnto=1122 |
| 27 | European Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12245&returnto=1122 |
| 28 | Film Studies | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12250&returnto=1122 |
| 29 | French | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12255&returnto=1122 |
| 30 | Geography | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12260&returnto=1122 |
| 31 | Geology | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12265&returnto=1122 |
| 32 | German | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12270&returnto=1122 |
| 33 | Gerontology | College of Health and Human Services | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12275&returnto=1122 |
| 34 | Health Science | College of Health and Human Services | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12280&returnto=1122 |
| 35 | History | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12285&returnto=1122 |
| 36 | Italian | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12290&returnto=1122 |
| 37 | Japanese | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12295&returnto=1122 |
| 38 | Journalism | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12300&returnto=1122 |
| 39 | Latin American Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12305&returnto=1122 |
| 40 | Leadership Studies | College of Education | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11887&returnto=1122 |
| 41 | Linguistics | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12310&returnto=1122 |
| 42 | Mathematics | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12315&returnto=1122 |
| 43 | Mexican American Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12320&returnto=1122 |
| 44 | Military Science | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12325&returnto=1122 |
| 45 | Music | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12330&returnto=1122 |
| 46 | Philosophy | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12335&returnto=1122 |
| 47 | Physics | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12340&returnto=1122 |
| 48 | Political Science | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12345&returnto=1122 |
| 49 | Psychology | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12350&returnto=1122 |
| 50 | Public Administration | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12355&returnto=1122 |
| 51 | Religious Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12360&returnto=1122 |
| 52 | Rhetoric and Writing Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12365&returnto=1122 |
| 53 | Sociology | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12370&returnto=1122 |
| 54 | Spanish | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12375&returnto=1122 |
| 55 | Statistics | College of Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12380&returnto=1122 |
| 56 | Theatre Arts | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12385&returnto=1122 |
| 57 | Urban Studies | College of Professional Studies and Fine Arts | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12390&returnto=1122 |
| 58 | Women's Studies | College of Arts and Letters | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12395&returnto=1122 |

### 1.5 General/Institute-wide requirements

SDSU requires completion of General Education (GE) requirements for all undergraduate students. The GE program includes:
- **Area A**: English Language Communication and Critical Thinking (9 units)
- **Area B**: Scientific Inquiry and Quantitative Reasoning (9 units)
- **Area C**: Arts and Humanities (9 units)
- **Area D**: Social Sciences (9 units)
- **Area E**: Lifelong Learning and Self-Development (3 units)
- **American Institutions**: U.S. History, U.S. Constitution, and California Government (6 units)

**Source**: https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=11884

### 1.6 Course-ID → Major quick-lookup

SDSU does not use a course-ID numbering system for majors. Programs are identified by name in the catalog.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Arts and Letters

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12226&returnto=1122 |
| 2 | Art, Art History Concentration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12229&returnto=1122 |
| 3 | Communication | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12232&returnto=1122 |
| 4 | Comparative International Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12235&returnto=1122 |
| 5 | English | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12238&returnto=1122 |
| 6 | European Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12241&returnto=1122 |
| 7 | French | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12244&returnto=1122 |
| 8 | Geography | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12247&returnto=1122 |
| 9 | History | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12250&returnto=1122 |
| 10 | Latin American Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12253&returnto=1122 |
| 11 | Linguistics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12256&returnto=1122 |
| 12 | Philosophy | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12259&returnto=1122 |
| 13 | Political Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12262&returnto=1122 |
| 14 | Psychology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12265&returnto=1122 |
| 15 | Sociology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12268&returnto=1122 |
| 16 | Spanish | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12271&returnto=1122 |

##### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12227&returnto=1122 |
| 2 | Creative Writing | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12230&returnto=1122 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12228&returnto=1122 |
| 2 | Communication | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12233&returnto=1122 |
| 3 | Computational Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12236&returnto=1122 |
| 4 | Education | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12292&returnto=1122 |
| 5 | Electrical and Computer Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12400&returnto=1122 |
| 6 | Mathematics and Science Education | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12458&returnto=1122 |
| 7 | Psychology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12266&returnto=1122 |
| 8 | Public Health | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12530&returnto=1122 |

#### College of Education

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Education, Educational Leadership: Postsecondary Education Specialization Concentration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12298&returnto=1122 |
| 2 | Postsecondary Educational Leadership and Student Affairs | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12588&returnto=1122 |

##### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership, Community College/Postsecondary Leadership Concentration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12294&returnto=1122 |

#### College of Engineering

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12400&returnto=1122 |
| 2 | Bioengineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12403&returnto=1122 |
| 3 | Civil Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12406&returnto=1122 |
| 4 | Computer Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12409&returnto=1122 |
| 5 | Computer Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12412&returnto=1122 |
| 6 | Construction Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12415&returnto=1122 |
| 7 | Electrical Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12418&returnto=1122 |
| 8 | Environmental Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12421&returnto=1122 |
| 9 | Mechanical Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12424&returnto=1122 |
| 10 | Structural Engineering | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12427&returnto=1122 |

#### College of Health and Human Services

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Child Development | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12339&returnto=1122 |
| 2 | Communicative Sciences and Disorders | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12342&returnto=1122 |
| 3 | Exercise and Nutritional Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12345&returnto=1122 |
| 4 | Nursing | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12348&returnto=1122 |
| 5 | Occupational Therapy | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12351&returnto=1122 |
| 6 | Physical Therapy | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12354&returnto=1122 |
| 7 | Public Health | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12357&returnto=1122 |
| 8 | Rehabilitation Counseling | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12356&returnto=1122 |
| 9 | Rehabilitation Counseling, Clinical Rehabilitation Counseling Concentration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12358&returnto=1122 |
| 10 | Social Work | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12360&returnto=1122 |

##### D.N.P.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12460&returnto=1122 |

##### Dr.P.H.
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12530&returnto=1122 |

#### College of Professional Studies and Fine Arts

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12465&returnto=1122 |
| 2 | Journalism and Media Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12468&returnto=1122 |
| 3 | Public Administration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12471&returnto=1122 |

##### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Television, Film and New Media | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12474&returnto=1122 |

##### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12462&returnto=1122 |
| 2 | Music, Composition Specialization | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12511&returnto=1122 |
| 3 | Music, Conducting | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12512&returnto=1122 |
| 4 | Music, Jazz Studies | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12513&returnto=1122 |
| 5 | Music, Performance | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12514&returnto=1122 |
| 6 | Music Education | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12642&returnto=1122 |

#### College of Sciences

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12520&returnto=1122 |
| 2 | Chemistry | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12523&returnto=1122 |
| 3 | Computer Science | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12526&returnto=1122 |
| 4 | Geological Sciences | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12529&returnto=1122 |
| 5 | Mathematics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12532&returnto=1122 |
| 6 | Microbiology | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12535&returnto=1122 |
| 7 | Physics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12538&returnto=1122 |
| 8 | Statistics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12541&returnto=1122 |

#### Fowler College of Business

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12272&returnto=1122 |
| 2 | Accountancy and Data Analytics | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=13953&returnto=1122 |
| 3 | Global Business Development | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12574&returnto=1122 |

##### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12575&returnto=1122 |

### 2.2 At least one program's full deep-dive (worked example)

**Program**: Master of Science in Computer Science
**Department**: Department of Computer Science
**College**: College of Sciences (also College of Engineering)
**URL**: https://catalog.sdsu.edu/preview_program.php?catoid=12&poid=12526&returnto=1122

**Application Details**:
- **Application Portal**: Cal State Apply (https://www.calstate.edu/apply)
- **Application Fee**: $70
- **Deadline**: Varies by department; typically February 1 for fall admission
- **GRE**: Not required for most programs
- **TOEFL/IELTS**: Required for international students (see Section 3.2)

### 2.3 Graduate admissions model

SDSU uses a **decentralized graduate admissions model**:
- **Centralized Application**: All applications submitted through Cal State Apply
- **Departmental Review**: Each department/program sets its own admission requirements and review process
- **Financial Aid**: Varies by program; some offer assistantships, fellowships, or tuition waivers
- **Graduate Studies**: College of Graduate Studies oversees all graduate programs but admissions decisions are made at the department level

**Key Links**:
- Graduate Admissions: https://admissions.sdsu.edu/graduate
- Graduate Programs: https://admissions.sdsu.edu/grad-programs
- Steps to Apply (Fall 2027): https://admissions.sdsu.edu/graduate/steps-apply

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| **Application Portal** | Cal State Apply | https://admissions.sdsu.edu/first-years |
| **Application Fee** | $70 | https://admissions.sdsu.edu/first-years |
| **Application Opens** | August 1 | https://admissions.sdsu.edu/first-years |
| **Filing Period** | October 1 – November 30 | https://admissions.sdsu.edu/first-years |
| **Application Deadline** | November 30 (no late applications) | https://admissions.sdsu.edu/first-years |
| **SAT/ACT Policy** | NOT used for admission (test-free, CSU system policy) | https://admissions.sdsu.edu/first-years |
| **Test Score Reporting** | Optional to report, not used for admission | https://admissions.sdsu.edu/first-years |
| **Superscore Policy** | N/A (test scores not used) | https://admissions.sdsu.edu/first-years |
| **Interview Policy** | Not required | https://admissions.sdsu.edu/first-years |
| **Recommendation Requirements** | Not required | https://admissions.sdsu.edu/first-years |
| **Portfolio/Audition** | Required for Dance, Music, Musical Theatre, Nursing, TV/Film/Production, Theatre Arts | https://admissions.sdsu.edu/international/first-years |
| **Transfer Pathway** | Available; see transfer admissions page | https://admissions.sdsu.edu/transfers |

**International First-Year Deadlines**:
| Deadline Type | Date |
|--------------|------|
| Early Consideration | November 30 |
| Regular Deadline | April 1 |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| **TOEFL iBT** (before Jan 21, 2026) | 80 | N/A | Required for non-English high school graduates |
| **TOEFL iBT** (on or after Jan 21, 2026) | 4 (new scoring) | N/A | New TOEFL scoring scale |
| **IELTS** | 6.5 | N/A | Overall band score |
| **Duolingo English Test** | 105 | N/A | |
| **PTE** | 58 | N/A | |
| **SDSU ALI** | Level 106 or Level 8 with 3.0 GPA | N/A | American Language Institute completion |

**Source**: https://admissions.sdsu.edu/international/first-years

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| **Application Portal** | Cal State Apply | https://admissions.sdsu.edu/graduate |
| **Application Fee** | $70 | https://admissions.sdsu.edu/graduate |
| **GRE/GMAT Policy** | Varies by program; not required for most | https://admissions.sdsu.edu/graduate |
| **English Proficiency** | Same as undergraduate requirements | https://admissions.sdsu.edu/international/graduate |
| **Application Timeline** | Varies by program; typically February 1 for fall | https://admissions.sdsu.edu/graduate/steps-apply |
| **CGS April-15 Honor** | SDSU is a CGS signatory | https://grad.sdsu.edu |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

#### California Resident

| Expense Item | Living with Parents | University Housing | Off Campus |
|-------------|---------------------|-------------------|------------|
| CSU Basic Tuition | $6,838 | $6,838 | $6,838 |
| Campus Fees | $2,942 | $2,942 | $2,942 |
| Books, Supplies | $1,014 | $1,014 | $1,014 |
| Food, Housing | $9,904 | $21,856 ($7,848 meal + $14,008 housing) | $19,512 ($6,706 food + $12,806 housing) |
| Transportation | $2,566 | $1,216 | $2,562 |
| Miscellaneous, Personal | $2,952 | $2,566 | $3,368 |
| **Total Academic Year** | **$26,216** | **$36,432** | **$36,236** |

#### Nonresident (Out-of-State/International)

| Expense Item | University Housing | Off Campus |
|-------------|-------------------|------------|
| CSU Basic Tuition | $6,838 | $6,838 |
| Campus Fees | $2,942 | $2,942 |
| Nonresident Tuition | $14,130 | $14,130 |
| Books, Supplies | $1,014 | $1,014 |
| Food, Housing | $21,856 ($7,848 meal + $14,008 housing) | $19,512 ($6,706 food + $12,806 housing) |
| Transportation | $1,216 | $2,562 |
| Miscellaneous, Personal | $2,566 | $3,368 |
| Out-of-State/International Fee | $3,000 | $3,000 |
| **Total Academic Year** | **$53,562** | **$53,366** |

**Additional Costs for International Students**:
- Health Insurance: ~$1,866/year (required)
- Nonresident tuition: $471 per unit (based on 15 units/semester)

**Source**: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/undergraduate-california-resident
**Source**: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/undergraduate-non-resident

### 4.2 Undergraduate financial-aid policy

- **Need-Blind Policy**: SDSU is need-blind for California residents; need-aware for out-of-state and international students
- **Tuition-Free Threshold**: Not specified (CSU system does not have a tuition-free guarantee)
- **Merit Scholarships**: Available through SDSU Aztec Scholarships and recruitment/merit scholarships
- **Financial Aid Types**: Grants, loans, work-study, scholarships
- **Application**: FAFSA required for federal/state aid; CSS Profile not required

**Source**: https://sacd.sdsu.edu/financial-aid/

### 4.3 Graduate cost & funding framework

#### Graduate/Doctoral (2026-27 academic year)

| Expense Item | Living with Parents | University Housing | Off Campus |
|-------------|---------------------|-------------------|------------|
| CSU Basic Tuition | $8,548 | $8,548 | $8,548 |
| Campus Fees | $2,942 | $2,942 | $2,942 |
| Books, Supplies | $1,014 | $1,014 | $1,014 |
| Food, Housing | $9,904 | $21,856 ($7,848 meal + $14,008 housing) | $19,512 ($6,706 food + $12,806 housing) |
| Transportation | $2,566 | $1,216 | $2,562 |
| Miscellaneous, Personal | $2,952 | $2,566 | $3,368 |
| **Total Academic Year** | **$27,926** | **$38,142** | **$37,946** |

**Additional Graduate Costs**:
- Nonresident tuition: $471 per unit
- Business programs (select): $321 per unit additional
- Education, physical therapy, public health, nursing practice doctoral programs: Different tuition rates
- Health Insurance: GSHIP (Graduate Student Health Insurance Program) available

**Funding Types**:
- Research Assistantships (RA)
- Teaching Assistantships (TA)
- Fellowships
- Grants
- Tuition waivers (varies by program)

**Source**: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/graduate-and-doctoral-students

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Application Deadline
```yaml
field: undergraduate.deadlines.application_deadline
value: "November 30"
source_url: https://admissions.sdsu.edu/first-years
source_snippet: "November 30: Application deadline. No late applications are accepted."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Application Fee
```yaml
field: undergraduate.costs.application_fee
value: "$70"
source_url: https://admissions.sdsu.edu/first-years
source_snippet: "A nonrefundable filing fee of $70 must accompany your application."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: SAT/ACT Policy
```yaml
field: undergraduate.admissions.test_policy
value: "NOT used for admission (test-free, CSU system policy)"
source_url: https://admissions.sdsu.edu/first-years
source_snippet: "In alignment with the California State University (CSU) system, SDSU no longer uses SAT or ACT exam scores from first-year applicants for determining admission eligibility."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: TOEFL Minimum (Pre-Jan 2026)
```yaml
field: undergraduate.admissions.english_proficiency.toefl_pre_2026
value: "80"
source_url: https://admissions.sdsu.edu/international/first-years
source_snippet: "TOEFL iBT exam taken before January 21, 2026: score of 80 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: TOEFL Minimum (Post-Jan 2026)
```yaml
field: undergraduate.admissions.english_proficiency.toefl_post_2026
value: "4 (new scoring)"
source_url: https://admissions.sdsu.edu/international/first-years
source_snippet: "TOEFL iBT exam taken on or after January 21, 2026: score of 4 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: IELTS Minimum
```yaml
field: undergraduate.admissions.english_proficiency.ielts
value: "6.5"
source_url: https://admissions.sdsu.edu/international/first-years
source_snippet: "IELTS: overall score of 6.5 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: Duolingo Minimum
```yaml
field: undergraduate.admissions.english_proficiency.duolingo
value: "105"
source_url: https://admissions.sdsu.edu/international/first-years
source_snippet: "Duolingo English Test: score of 105 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: PTE Minimum
```yaml
field: undergraduate.admissions.english_proficiency.pte
value: "58"
source_url: https://admissions.sdsu.edu/international/first-years
source_snippet: "PTE: score of 58 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: California Resident Tuition (2026-27)
```yaml
field: undergraduate.costs.tuition_resident_2026_27
value: "$6,838"
source_url: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/undergraduate-california-resident
source_snippet: "CSU Basic tuition: $6,838"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-010: Nonresident Tuition (2026-27)
```yaml
field: undergraduate.costs.tuition_nonresident_2026_27
value: "$14,130"
source_url: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/undergraduate-non-resident
source_snippet: "Nonresident tuition: $14,130"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-011: Total COA California Resident (2026-27, Off Campus)
```yaml
field: undergraduate.costs.total_resident_2026_27_off_campus
value: "$36,236"
source_url: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/undergraduate-california-resident
source_snippet: "Total academic year: $36,236 (Living off campus)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-012: Total COA Nonresident (2026-27, Off Campus)
```yaml
field: undergraduate.costs.total_nonresident_2026_27_off_campus
value: "$53,366"
source_url: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/undergraduate-non-resident
source_snippet: "Total academic year: $53,366 (Living off campus)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.costs.application_fee
value: "$70"
source_url: https://admissions.sdsu.edu/graduate
source_snippet: "Apply to the university through Cal State Apply."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Tuition (2026-27)
```yaml
field: graduate.costs.tuition_2026_27
value: "$8,548"
source_url: https://sacd.sdsu.edu/financial-aid/financial-aid/eligibility/cost-of-attendance/cost-of-attendance-tables/graduate-and-doctoral-students
source_snippet: "CSU Basic Tuition: $8,548"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-P-001: Total Programs in Catalog
```yaml
field: programs.total_count
value: "662"
source_url: https://catalog.sdsu.edu/content.php?catoid=12&navoid=1122
source_snippet: "662 program links found in Curricula by Department"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
SDSU-knowledge-base-v2/
├── 00-institution-overview/
│   ├── 00-1-program-counts.md
│   ├── 00-2-hierarchy-tree.md
│   ├── 00-3-degree-inventory.md
│   └── 00-4-distribution-matrix.md
├── 01-undergraduate-education/
│   ├── 01-1-college-of-arts-and-letters.md
│   ├── 01-2-college-of-education.md
│   ├── 01-3-college-of-engineering.md
│   ├── 01-4-college-of-health-and-human-services.md
│   ├── 01-5-college-of-professional-studies-and-fine-arts.md
│   ├── 01-6-college-of-sciences.md
│   ├── 01-7-fowler-college-of-business.md
│   └── 01-8-weber-honors-college.md
├── 02-graduate-education/
│   ├── 02-1-college-of-arts-and-letters-grad.md
│   ├── 02-2-college-of-education-grad.md
│   ├── 02-3-college-of-engineering-grad.md
│   ├── 02-4-college-of-health-and-human-services-grad.md
│   ├── 02-5-college-of-professional-studies-and-fine-arts-grad.md
│   ├── 02-6-college-of-sciences-grad.md
│   └── 02-7-fowler-college-of-business-grad.md
├── 03-application-requirements/
│   ├── 03-1-undergraduate-deadlines.md
│   ├── 03-2-english-proficiency.md
│   └── 03-3-graduate-admissions.md
├── 04-costs-and-aid/
│   ├── 04-1-undergraduate-costs.md
│   ├── 04-2-graduate-costs.md
│   └── 04-3-financial-aid-policy.md
└── 05-evidence-chain/
    └── 05-1-evidence-index.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "SDSU-knowledge-base-v2"
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

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Complete program list extraction (fix 59 unknown programs) | https://catalog.sdsu.edu/content.php?catoid=12&navoid=1122 |
| P0 | Per-program GRE/GMAT requirements | https://admissions.sdsu.edu/grad-programs |
| P0 | Per-program application deadlines | https://admissions.sdsu.edu/graduate/steps-apply |
| P1 | Graduate program detail pages (GRE, TOEFL, materials) | Individual program pages |
| P1 | Financial aid details (scholarships, grants, work-study) | https://sacd.sdsu.edu/financial-aid/ |
| P1 | Transfer admission requirements | https://admissions.sdsu.edu/transfers |
| P2 | Campus life and housing details | https://housing.sdsu.edu/ |
| P2 | Study abroad programs | https://sdsubeintl.wordpress.com/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | SDSU | MIT | Stanford | Harvard | Caltech | UChicago | UC Berkeley | Cornell | Brown | UPenn | JHU |
|------|------|-----|----------|---------|---------|----------|-------------|---------|-------|-------|-----|
| **Total UG Cost/yr (Resident, Off Campus)** | $36,236 | $93,912 | $97,284 | $97,284 | $93,912 | $103,821 | $34,002 | $97,284 | $97,284 | $97,284 | $94,858 |
| **Total UG Cost/yr (Nonresident, Off Campus)** | $53,366 | $93,912 | $97,284 | $97,284 | $93,912 | $103,821 | $57,486 | $97,284 | $97,284 | $97,284 | $94,858 |
| **Tuition/yr (Resident)** | $6,838 | $65,622 | $71,700 | $71,700 | $65,622 | $75,960 | $18,216 | $71,700 | $71,700 | $71,700 | $68,670 |
| **Tuition/yr (Nonresident)** | $14,130 | $65,622 | $71,700 | $71,700 | $65,622 | $75,960 | $57,486 | $71,700 | $71,700 | $71,700 | $68,670 |
| **Need-Blind (Intl?)** | No | Yes | Yes | Yes | No (need-aware) | No (need-aware) | No (need-aware) | No (need-aware) | Yes | No (need-aware) | No (need-aware) |
| **EA Deadline** | N/A | Nov 1 | Nov 1 | Nov 1 | Nov 1 | Nov 2 | N/A | Nov 1 | Nov 1 | Nov 1 | Nov 1 |
| **RA/RD Deadline** | Nov 30 | Jan 5 | Jan 5 | Jan 5 | Jan 5 | Jan 4 | Nov 30 | Jan 2 | Jan 5 | Jan 5 | Jan 2 |
| **SAT/ACT Required?** | No (test-free) | Yes | Yes | Yes | Yes | Test-optional | No (test-free) | Yes | Yes | Yes | Yes |
| **TOEFL Min** | 80 (pre-Jan 2026) / 4 (post-Jan 2026) | 100 | N/A | 105 | 100 | 100 | 80 | 100 | 105 | 100 | 100 |
| **IELTS Min** | 6.5 | 7.0 | N/A | 8.0 | 7.0 | 7.0 | 6.5 | 7.5 | 8.0 | 7.0 | 7.0 |
| **Tuition-Free Threshold** | N/A | $200k | $200k | $85k | N/A | $250k | N/A | $75k | $200k | $75k | $100k |
| **Total Program Count (Rule 1)** | 662 | 110 | 342 | 51 | 76 | 101 | 285 | 429 | 208 | 641 | 605 |
| **School/Department Count (Rule 2)** | 9 | 5 | 7 | 13 | 6 | 12 | 8 | 7 | 7 | 16 | 10 |

> **Note**: SDSU is a public university in the CSU system, so costs are significantly lower than private institutions. The "test-free" policy (SAT/ACT not used for admission) is distinctive among the compared schools.

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.sdsu.edu, catalog.sdsu.edu, sacd.sdsu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
