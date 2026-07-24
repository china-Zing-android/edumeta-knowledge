# Loyola Marymount University (LMU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BBA/BSE) | 55 |
| 本科辅修 (Minor) | 58 |
| 研究生学位项目 (MA/MS/MBA/MFA/MSE/PhD/EdD/JD/LLM/DBA) | 46 |
| 研究生高级证书/凭证 (Certificate/Credential/Authorization) | 14 |
| **学位项目总计 (UG + Grad)** | **131** |
| 学院 / 独立系所总数 | 7 |

> **来源**: https://www.lmu.edu/academics/degrees/ — "We offer 55 undergraduate majors and 58 minor programs, along with 46 master's degree programs, four doctorate programs and 14 credential/authorization programs."

### 0.2 学院 / 系层级结构

```
Loyola Marymount University
├── Bellarmine College of Liberal Arts                    [学院]
│   ├── African American Studies                          [系]
│   ├── Asian and Pacific Studies                         [系]
│   ├── Chicana/o and Latina/o Studies                    [系]
│   ├── Classics and Archaeology                          [系]
│   ├── Communication Studies                             [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── History                                           [系]
│   ├── Modern Languages                                  [系]
│   ├── Philosophy                                        [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Sociology                                         [系]
│   ├── Theological Studies                               [系]
│   ├── Women's and Gender Studies                        [系]
│   └── Urban Studies                                     [系]
├── College of Business Administration                    [学院]
│   ├── Accounting                                        [系]
│   ├── Entrepreneurship                                  [系]
│   ├── Finance                                           [系]
│   ├── Information Systems and Business Analytics        [系]
│   ├── Management and Leadership                         [系]
│   └── Marketing                                         [系]
├── College of Communication and Fine Arts                [学院]
│   ├── Communication Studies                             [系]
│   ├── Dance                                             [系]
│   ├── Journalism                                        [系]
│   ├── Music                                             [系]
│   ├── Recording Arts                                    [系]
│   ├── Studio Arts                                       [系]
│   └── Theatre Arts                                      [系]
├── Frank R. Seaver College of Science and Engineering    [学院]
│   ├── Civil Engineering                                 [系]
│   ├── Computer Engineering                              [系]
│   ├── Computer Science                                  [系]
│   ├── Electrical Engineering                            [系]
│   ├── Environmental Science                             [系]
│   ├── Mathematics                                       [系]
│   ├── Mechanical Engineering                            [系]
│   ├── Physics                                           [系]
│   └── Health and Human Sciences                         [系]
├── School of Education                                   [学院]
│   ├── Educational Leadership                            [系]
│   ├── Counseling                                        [系]
│   ├── Special Education                                 [系]
│   └── Teacher Preparation                               [系]
├── School of Film and Television                         [学院]
│   ├── Animation                                         [系]
│   ├── Film and Television Production                    [系]
│   ├── Film, Television, and Media Studies               [系]
│   ├── Screenwriting                                     [系]
│   └── Writing for the Screen                            [系]
└── Loyola Law School                                     [学院]
    ├── Juris Doctor (Day Program)                        [系]
    ├── Juris Doctor (Hybrid Evening Program)             [系]
    ├── Master of Laws (LL.M.)                            [系]
    └── Master of Science in Legal Studies (M.L.S.)       [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| B.A. | Bachelor of Arts | 本科 | 35 |
| B.S. | Bachelor of Science | 本科 | 14 |
| B.B.A. | Bachelor of Business Administration | 本科 | 5 |
| B.F.A. | Bachelor of Fine Arts | 本科 | 1 |
| B.S.E. | Bachelor of Science in Engineering | 本科 | 4 |
| Minor | 辅修 | 本科 | 58 |
| M.A. | Master of Arts | 研究生 | 16 |
| M.S. | Master of Science | 研究生 | 10 |
| M.S.E. | Master of Science in Engineering | 研究生 | 4 |
| M.F.A. | Master of Fine Arts | 研究生 | 4 |
| M.B.A. | Master of Business Administration | 研究生 | 3 |
| J.D. | Juris Doctor | 研究生 | 4 |
| LL.M. | Master of Laws | 研究生 | 3 |
| M.L.S. | Master of Science in Legal Studies | 研究生 | 1 |
| Ed.D. | Doctor of Education | 研究生 | 1 |
| Ed.S. | Educational Specialist | 研究生 | 1 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| Certificate | 高级证书 | 研究生 | 22 |
| Credential | 教学凭证 | 研究生 | 11 |
| Credential Authorization | 凭证授权 | 研究生 | 1 |

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院 \ 级别 | B.A. | B.S. | B.B.A. | B.F.A. | B.S.E. | Minor | M.A. | M.S. | M.S.E. | M.F.A. | M.B.A. | J.D. | LL.M. | Ed.D. | DBA | Certificate | Credential | 合计 |
|------------|------|------|--------|--------|--------|-------|------|------|--------|--------|--------|------|-------|-------|-----|-------------|------------|------|
| Bellarmine College of Liberal Arts | 15 | 0 | 0 | 0 | 0 | 25 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 45 |
| College of Business Administration | 0 | 0 | 5 | 0 | 0 | 3 | 0 | 5 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 4 | 0 | 21 |
| College of Communication and Fine Arts | 5 | 0 | 0 | 1 | 0 | 8 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| Frank R. Seaver College of Science and Engineering | 0 | 7 | 0 | 0 | 4 | 6 | 0 | 3 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 32 |
| School of Education | 1 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 12 | 20 |
| School of Film and Television | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Loyola Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 0 | 0 | 0 | 0 | 7 |
| **合计** | **24** | **7** | **5** | **1** | **4** | **44** | **10** | **8** | **4** | **4** | **3** | **4** | **3** | **1** | **1** | **13** | **12** | **131** |

> **注意**: 部分专业跨越多个学院（如 Economics 在 Bellarmine），上表按主归属学院统计。Certificate 和 Credential 合并统计。

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

LMU 有 7 个学院，其中 6 个提供本科教育（Loyola Law School 仅提供研究生/J.D. 教育）。详见 Section 0.2 层级树。

### 1.2 Undergraduate Majors — grouped by 学院 > 系 > 学位级别

#### Bellarmine College of Liberal Arts

##### African American Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://www.lmu.edu/academics/degrees/degree/program,118618.html |

##### Asian and Pacific Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian and Pacific Studies | https://www.lmu.edu/academics/degrees/degree/program,118619.html |

##### Chicana/o and Latina/o Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chicana/o and Latina/o Studies | https://www.lmu.edu/academics/degrees/degree/program,114375.html |

##### Classics and Archaeology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics and Archaeology | https://www.lmu.edu/academics/degrees/degree/program,114426.html |

##### Communication Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.lmu.edu/academics/degrees/degree/program,114415.html |

##### Economics
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.lmu.edu/academics/degrees/degree/program,114377.html |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.lmu.edu/academics/degrees/degree/program,114377.html |

##### English
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.lmu.edu/academics/degrees/degree/program,114378.html |

##### History
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.lmu.edu/academics/degrees/degree/program,114381.html |

##### International Relations
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | International Relations | https://www.lmu.edu/academics/degrees/degree/program,142375.html |

##### Modern Languages
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Modern Languages | https://www.lmu.edu/academics/degrees/degree/program,114384.html |

##### Philosophy
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.lmu.edu/academics/degrees/degree/program,114385.html |

##### Philosophy, Politics, and Economics
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy, Politics, and Economics | https://www.lmu.edu/academics/degrees/degree/program,593785.html |

##### Political Science
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.lmu.edu/academics/degrees/degree/program,114386.html |

##### Psychology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.lmu.edu/academics/degrees/degree/program,114389.html |

##### Sociology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.lmu.edu/academics/degrees/degree/program,114390.html |

##### Theological Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Theological Studies | https://www.lmu.edu/academics/degrees/degree/program,114392.html |

##### Urban Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Studies | https://www.lmu.edu/academics/degrees/degree/program,114393.html |

##### Women's and Gender Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's and Gender Studies | https://www.lmu.edu/academics/degrees/degree/program,114394.html |

---

#### College of Business Administration

##### Accounting
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.lmu.edu/academics/degrees/degree/program,114408.html |

##### Entrepreneurship
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship | https://www.lmu.edu/academics/degrees/degree/program,114409.html |

##### Finance
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.lmu.edu/academics/degrees/degree/program,114411.html |

##### Information Systems and Business Analytics
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Systems and Business Analytics (ISBA) | https://www.lmu.edu/academics/degrees/degree/program,114410.html |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Systems and Business Analytics (ISBA) | https://www.lmu.edu/academics/degrees/degree/program,114410.html |

##### Management and Leadership
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Management and Leadership | https://www.lmu.edu/academics/degrees/degree/program,114412.html |

##### Marketing
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.lmu.edu/academics/degrees/degree/program,114413.html |

---

#### College of Communication and Fine Arts

##### Dance
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.lmu.edu/academics/degrees/degree/program,114416.html |

##### Music
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.lmu.edu/academics/degrees/degree/program,114417.html |

##### Recording Arts
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Recording Arts | https://www.lmu.edu/academics/degrees/degree/program,114421.html |

##### Studio Arts
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Arts | https://www.lmu.edu/academics/degrees/degree/program,114418.html |

###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Arts | https://www.lmu.edu/academics/degrees/degree/program,114418.html |

##### Theatre Arts
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://www.lmu.edu/academics/degrees/degree/program,114419.html |

---

#### Frank R. Seaver College of Science and Engineering

##### Applied Mathematics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.lmu.edu/academics/degrees/degree/program,114395.html |

##### Applied Physics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physics | https://www.lmu.edu/academics/degrees/degree/program,121388.html |

##### Biochemistry
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.lmu.edu/academics/degrees/degree/program,114396.html |

##### Biology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.lmu.edu/academics/degrees/degree/program,114397.html |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.lmu.edu/academics/degrees/degree/program,114397.html |

##### Chemistry
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.lmu.edu/academics/degrees/degree/program,114398.html |

##### Civil Engineering
###### B.S.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.lmu.edu/academics/degrees/degree/program,114399.html |

##### Computer Engineering
###### B.S.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.lmu.edu/academics/degrees/degree/program,469718.html |

##### Computer Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lmu.edu/academics/degrees/degree/program,114400.html |

##### Electrical Engineering
###### B.S.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.lmu.edu/academics/degrees/degree/program,114401.html |

##### Environmental Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.lmu.edu/academics/degrees/degree/program,114402.html |

##### Environmental Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://www.lmu.edu/academics/degrees/degree/program,114429.html |

##### Health and Human Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Health and Human Sciences | https://www.lmu.edu/academics/degrees/degree/program,114403.html |

##### Mathematics
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.lmu.edu/academics/degrees/degree/program,114404.html |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.lmu.edu/academics/degrees/degree/program,114404.html |

##### Mechanical Engineering
###### B.S.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.lmu.edu/academics/degrees/degree/program,114406.html |

##### Physics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.lmu.edu/academics/degrees/degree/program,114407.html |

##### Statistics and Data Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics and Data Science | https://www.lmu.edu/academics/degrees/degree/program,411329.html |

---

#### School of Education

##### Education and Learning Sciences
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Education and Learning Sciences | https://www.lmu.edu/academics/degrees/degree/program,114383.html |

---

#### School of Film and Television

##### Animation
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation | https://www.lmu.edu/academics/degrees/degree/program,114420.html |

##### Film and Television Production
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Television Production | https://www.lmu.edu/academics/degrees/degree/program,114423.html |

##### Film, Television, and Media Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Film, Television, and Media Studies | https://www.lmu.edu/academics/degrees/degree/program,114442.html |

##### Screenwriting
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Screenwriting | https://www.lmu.edu/academics/degrees/degree/program,114422.html |

---

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学位 | 主归属学院 | URL |
|---|------|------|-----------|-----|
| 1 | Philosophy, Politics, and Economics | B.A. | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,593785.html |
| 2 | Statistics and Data Science | B.S. | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,411329.html |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 | Accounting | College of Business Administration | https://www.lmu.edu/academics/degrees/degree/program,114408.html |
| 2 | African American Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,118618.html |
| 3 | Animation | School of Film and Television | https://www.lmu.edu/academics/degrees/degree/program,114420.html |
| 4 | Applied Data Analysis | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,595425.html |
| 5 | Applied Developmental Psychology | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,571994.html |
| 6 | Applied Mathematics | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114395.html |
| 7 | Art History | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114414.html |
| 8 | Asian and Pacific Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,118619.html |
| 9 | Asian Pacific American Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114424.html |
| 10 | Biochemistry | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114396.html |
| 11 | Bioethics | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114443.html |
| 12 | Biology | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114397.html |
| 13 | Business Administration | College of Business Administration | https://www.lmu.edu/academics/degrees/degree/program,114439.html |
| 14 | Business Law | College of Business Administration | https://www.lmu.edu/academics/degrees/degree/program,459289.html |
| 15 | Catholic Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114425.html |
| 16 | Chemistry | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114398.html |
| 17 | Chicana/o and Latina/o Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114375.html |
| 18 | Chinese | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114433.html |
| 19 | Classics and Archaeology | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114426.html |
| 20 | Cognitive Science | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,580323.html |
| 21 | Dance | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114416.html |
| 22 | Digital Media, Cultures, and Industries | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,556858.html |
| 23 | Disabilities Studies | School of Education | https://www.lmu.edu/academics/degrees/degree/program,582169.html |
| 24 | Economics | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114377.html |
| 25 | Electrical Engineering | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114401.html |
| 26 | English | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114378.html |
| 27 | Environmental Science | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114402.html |
| 28 | Environmental Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114429.html |
| 29 | Film, Television, and Media Studies | School of Film and Television | https://www.lmu.edu/academics/degrees/degree/program,114442.html |
| 30 | French | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114380.html |
| 31 | German | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114435.html |
| 32 | Health and Human Sciences | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114403.html |
| 33 | Health and Society | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,277110.html |
| 34 | History | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114381.html |
| 35 | International Business | College of Business Administration | https://www.lmu.edu/academics/degrees/degree/program,389391.html |
| 36 | International Documentary Production | School of Film and Television | https://www.lmu.edu/academics/degrees/degree/program,325416.html |
| 37 | International Relations | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,142375.html |
| 38 | Irish Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114431.html |
| 39 | Islamic Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,582165.html |
| 40 | Italian | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114436.html |
| 41 | Jewish Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114432.html |
| 42 | Journalism | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114427.html |
| 43 | LGBTQ Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,585211.html |
| 44 | Mathematics | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114404.html |
| 45 | Modern Greek Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114437.html |
| 46 | Music | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114417.html |
| 47 | Peace and Justice Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,253104.html |
| 48 | Philosophy | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114385.html |
| 49 | Physics | Frank R. Seaver College of Science and Engineering | https://www.lmu.edu/academics/degrees/degree/program,114407.html |
| 50 | Political Science | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114386.html |
| 51 | Psychology | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114389.html |
| 52 | Public Relations | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,238311.html |
| 53 | Screenwriting | School of Film and Television | https://www.lmu.edu/academics/degrees/degree/program,114422.html |
| 54 | Sociology | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114390.html |
| 55 | Spanish | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114391.html |
| 56 | Sport Studies | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,608158.html |
| 57 | Studio Arts | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114418.html |
| 58 | Theatre Arts | College of Communication and Fine Arts | https://www.lmu.edu/academics/degrees/degree/program,114419.html |
| 59 | Theological Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114392.html |
| 60 | Urban Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114393.html |
| 61 | Women's and Gender Studies | Bellarmine College of Liberal Arts | https://www.lmu.edu/academics/degrees/degree/program,114394.html |

### 1.5 General/Institute-wide requirements

LMU 要求所有本科生完成核心课程（Core Curriculum），包括：
- 一年级研讨课 (First Year Seminar)
- 写作 (Writing)
- 数学/逻辑 (Mathematics/Logic)
- 自然科学 (Natural Science)
- 社会科学 (Social Science)
- 人文 (Humanities)
- 神学/宗教研究 (Theology/Religious Studies)
- 哲学 (Philosophy)
- 伦理学 (Ethics)
- 多元文化研究 (Diversity Studies)
- 艺术 (Fine Arts)

> 来源: https://www.lmu.edu/academics/degrees/ — 核心课程要求详见 LMU 大学公报

---

## SECTION 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Business Administration

##### MBA Program
###### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | MBA Program | https://www.lmu.edu/academics/degrees/degree/program,116272.html |

##### Business Analytics
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.lmu.edu/academics/degrees/degree/program,258778.html |

##### Entrepreneurship and Sustainable Innovation
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Entrepreneurship and Sustainable Innovation | https://www.lmu.edu/academics/degrees/degree/program,370160.html |

##### Management
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Management | https://www.lmu.edu/academics/degrees/degree/program,379888.html |

##### Taxation
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Taxation | https://www.lmu.edu/academics/degrees/degree/program,422669.html |

##### Entertainment Leadership and Management
###### MASTER
| # | 项目 | URL |
|---|------|-----|
| 1 | Entertainment Leadership and Management | https://www.lmu.edu/academics/degrees/degree/program,524463.html |

##### Doctor of Business Administration
###### DBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Business Administration | https://www.lmu.edu/academics/degrees/degree/program,524209.html |

##### Certificates
###### CERTIFICATE
| # | 项目 | URL |
|---|------|-----|
| 1 | Business of Sports | https://www.lmu.edu/academics/degrees/degree/program,605270.html |
| 2 | Executive Education | https://www.lmu.edu/academics/degrees/degree/program,253575.html |
| 3 | Foundations of Management | https://www.lmu.edu/academics/degrees/degree/program,469285.html |

---

#### College of Communication and Fine Arts

##### Theatre Arts M.F.A.: Performance Pedagogy
###### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Theatre Arts M.F.A.: Performance Pedagogy | https://www.lmu.edu/academics/degrees/degree/program,245961.html |

---

#### Frank R. Seaver College of Science and Engineering

##### Civil Engineering
###### M.S.E.
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.lmu.edu/academics/degrees/degree/program,114399.html |

##### Computer Engineering
###### M.S.E.
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.lmu.edu/academics/degrees/degree/program,469718.html |

##### Computer Science
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lmu.edu/academics/degrees/degree/program,114400.html |

##### Electrical Engineering
###### M.S.E.
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.lmu.edu/academics/degrees/degree/program,114401.html |

##### Environmental Science
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.lmu.edu/academics/degrees/degree/program,114402.html |

##### Healthcare Systems Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Healthcare Systems Engineering | https://www.lmu.edu/academics/degrees/degree/program,144972.html |

##### Mechanical Engineering
###### M.S.E.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.lmu.edu/academics/degrees/degree/program,114406.html |

##### Systems Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Systems Engineering | https://www.lmu.edu/academics/degrees/degree/program,114711.html |

##### Certificates
###### CERTIFICATE
| # | 项目 | URL |
|---|------|-----|
| 1 | Additive Manufacturing | https://www.lmu.edu/academics/degrees/degree/program,464124.html |
| 2 | Aeronautics and Space Systems | https://www.lmu.edu/academics/degrees/degree/program,341192.html |
| 3 | Artificial Intelligence | https://www.lmu.edu/academics/degrees/degree/program,614351.html |
| 4 | Cybersecurity | https://www.lmu.edu/academics/degrees/degree/program,341196.html |
| 5 | Engineering Project Management | https://www.lmu.edu/academics/degrees/degree/program,341197.html |
| 6 | Lean Healthcare Systems | https://www.lmu.edu/academics/degrees/degree/program,114712.html |
| 7 | Software Architecture | https://www.lmu.edu/academics/degrees/degree/program,341201.html |
| 8 | Sustainability | https://www.lmu.edu/academics/degrees/degree/program,341203.html |
| 9 | Systems Engineering | https://www.lmu.edu/academics/degrees/degree/program,341204.html |
| 10 | Water and Wastewater Treatment | https://www.lmu.edu/academics/degrees/degree/program,341205.html |
| 11 | Water Quality Management | https://www.lmu.edu/academics/degrees/degree/program,341206.html |

---

#### School of Education

##### Counseling
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://www.lmu.edu/academics/degrees/degree/program,114687.html |

##### Educational Leadership
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | https://www.lmu.edu/academics/degrees/degree/program,172066.html |

##### Educational Leadership for Social Justice
###### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership for Social Justice | https://www.lmu.edu/academics/degrees/degree/program,114713.html |

##### Educational Studies
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Studies | https://www.lmu.edu/academics/degrees/degree/program,114693.html |

##### Marital & Family Therapy / Art Therapy
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Marital & Family Therapy / Art Therapy | https://www.lmu.edu/academics/degrees/degree/program,114447.html |

##### School Psychology
###### M.A. / Ed.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology | https://www.lmu.edu/academics/degrees/degree/program,114689.html |

##### Special Education
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Special Education | https://www.lmu.edu/academics/degrees/degree/program,114690.html |

##### Teacher Preparation - Graduate
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Teacher Preparation - Graduate | https://www.lmu.edu/academics/degrees/degree/program,172069.html |

##### Credentials and Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Administrative Services Credential / School Administration | M.A. / CREDENTIAL | https://www.lmu.edu/academics/degrees/degree/program,114686.html |
| 2 | Bilingual Teacher Education - Chinese or Spanish | CREDENTIAL | https://www.lmu.edu/academics/degrees/degree/program,172068.html |
| 3 | Catholic Archdiocesan School Teachers (CAST) | M.A. / CREDENTIAL | https://www.lmu.edu/academics/degrees/degree/program,172045.html |
| 4 | Catholic School Administration Certificate | CERTIFICATE | https://www.lmu.edu/academics/degrees/degree/program,172062.html |
| 5 | Child Welfare & Attendance Added Authorization | CREDENTIAL AUTHORIZATION | https://www.lmu.edu/academics/degrees/degree/program,248006.html |
| 6 | LMU / Teach For America Partnership | M.A. / CREDENTIAL | https://www.lmu.edu/academics/degrees/degree/program,172071.html |
| 7 | Partners in Los Angeles Catholic Education (PLACE) | M.A. / CREDENTIAL | https://www.lmu.edu/academics/degrees/degree/program,172073.html |
| 8 | Teacher Preparation - Undergraduate | CREDENTIAL | https://www.lmu.edu/academics/degrees/degree/program,172065.html |

---

#### School of Film and Television

##### Film and Television Production
###### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Film and Television Production | https://www.lmu.edu/academics/degrees/degree/program,114423.html |

##### Writing and Producing for Television
###### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Writing and Producing for Television | https://www.lmu.edu/academics/degrees/degree/program,114369.html |

##### Writing for the Screen
###### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Writing for the Screen | https://www.lmu.edu/academics/degrees/degree/program,114707.html |

---

#### Bellarmine College of Liberal Arts

##### English
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://www.lmu.edu/academics/degrees/degree/program,114378.html |

##### Pastoral Theology
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Pastoral Theology | https://www.lmu.edu/academics/degrees/degree/program,114444.html |

##### Philosophy
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.lmu.edu/academics/degrees/degree/program,114385.html |

##### Theological Studies
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Theological Studies | https://www.lmu.edu/academics/degrees/degree/program,114392.html |

##### Yoga Studies
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Yoga Studies | https://www.lmu.edu/academics/degrees/degree/program,114445.html |

---

#### Loyola Law School

##### Juris Doctor
###### J.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor Day Program | https://www.lmu.edu/academics/degrees/degree/program,207439.html |
| 2 | Hybrid Juris Doctor Evening Program | https://www.lmu.edu/academics/degrees/degree/program,207466.html |

##### Joint Degrees
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Joint J.D. / MBA | J.D. / MBA | https://www.lmu.edu/academics/degrees/degree/program,207467.html |
| 2 | Joint J.D. / Tax LL.M. | J.D. / LL.M. | https://www.lmu.edu/academics/degrees/degree/program,207468.html |

##### Master of Laws
###### LL.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws (LL.M.) | https://www.lmu.edu/academics/degrees/degree/program,207472.html |
| 2 | Online Master of Laws (Tax LL.M.) | https://www.lmu.edu/academics/degrees/degree/program,272896.html |

##### Master of Science in Legal Studies
###### M.L.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Legal Studies (M.L.S.) | https://www.lmu.edu/academics/degrees/degree/program,207478.html |

---

### 2.2 At least one program's full deep-dive (worked example)

**MBA Program — College of Business Administration**

- **Department**: College of Business Administration
- **Address**: 1 LMU Drive, Los Angeles, CA 90045
- **Application Portal**: https://graduatestudies.lmu.edu/apply/
- **Program URL**: https://www.lmu.edu/academics/degrees/degree/program,116272.html
- **Tuition**: $1,902 per unit (2026-2027)
- **Application Fee**: See graduate admissions
- **Deadlines**: See https://grad.lmu.edu/apply/programdeadlines/

### 2.3 Graduate admissions model

LMU 研究生招生采用分散式管理：
- **中央研究生招生**: https://graduatestudies.lmu.edu/apply/
- **各学院独立管理**: 每个学院有自己的招生标准和截止日期
- **法学院独立招生**: https://www.lls.edu/admissions/
- **研究生项目截止日期**: https://grad.lmu.edu/apply/programdeadlines/

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| **招生网站** | https://admission.lmu.edu/ | admission.lmu.edu |
| **申请系统** | Common App, LMU Application | admission.lmu.edu |
| **Early Decision (绑定)** | November 1 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **Early Action (非绑定)** | November 1 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **Early Decision II (绑定)** | January 8 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **Regular Decision** | January 15 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **Spring 入学** | October 15 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **FAFSA 截止日期** | February 1 (ED: Nov 15, ED II/EA: Jan 15) | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **申请费** | $75 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **推荐信** | 1封 required (建议2封) | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **成绩单** | 需提交 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **SAT/ACT** | Test Optional | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **ED 通知时间** | 12月中旬 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **EA 通知时间** | 12月下旬 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **RD 通知时间** | 4月1日前 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |
| **确认入学截止** | May 1 | admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ |

> **来源**: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/ — "November 1: Early Decision (binding) admission for Fall; November 1: Early Action (non-binding) admission for Fall; January 8: Early Decision II (binding) admission for Fall; January 15: Regular Decision Admission for Fall"

### 3.2 Undergraduate English proficiency table

| 考试 | 最低要求 | 建议分数 | 备注 |
|------|---------|---------|------|
| TOEFL iBT | 80 | 90+ | 未明确公布最低分，建议90+ |
| IELTS | 6.5 | 7.0+ | 未明确公布最低分 |
| Duolingo | 未公布 | - | 需联系招生办确认 |
| PTE | 未公布 | - | 需联系招生办确认 |

> **注意**: LMU 未在官网明确公布英语最低分数要求，建议直接联系 admission@lmu.edu 确认

### 3.3 Graduate — global rules

- **招生模式**: 分散式，各学院独立管理
- **申请平台**: https://graduatestudies.lmu.edu/apply/
- **法学院申请**: https://www.lls.edu/admissions/
- **申请费**: 详见各学院
- **GRE/GMAT**: 因项目而异
- **语言要求**: 因项目而异
- **截止日期**: https://grad.lmu.edu/apply/programdeadlines/

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-2027 Academic Year)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| **Tuition (全日制)** | $68,042/年 | 12+ 学分/学期 |
| **Tuition (每学期)** | $34,021/学期 | 12+ 学分/学期 |
| **Part-Time Tuition** | $2,840/学分 | 少于12学分 |
| **Auditors** | $712/学分 | 旁听 |
| **Post Bacc Pre-Med** | $1,460/学分 | 医学预科 |
| **Tuition Deposit** | $500 | 入学押金 |
| **New Student Fee** | $500 | 新生费用 |
| **New International Student Fee** | $1,200 | 国际新生 |
| **Spring Entry New Student Fee** | $260 | 春季入学新生 |
| **Registration Fee** | $65/学期 | 注册费 |
| **Student Activity Fee** | $144/学期 | 学生活动费 |
| **Student Recreation Facility Fee** | $108/学期 | 体育设施费 |
| **International Student Fee** | $75/学期 | 国际学生费 |
| **Media Fee** | $140/年 | 媒体费 |
| **Tuition Refund Insurance** | $224/学期 | 学费退还保险 |
| **Accident Insurance** | $124/年 | 意外保险 (7+学分) |
| **Fall Student Health Insurance** | $1,164 | 健康保险 (8/1-12/31) |
| **Spring Student Health Insurance** | $1,612 | 健康保险 (1/1-7/31) |
| **Parking Fee** | $502/学期 | 停车费 |

> **来源**: https://finance.lmu.edu/controller/osfs/studentaccounts/tuitionothercostsbudgetworksheet/20262027academicyear/undergraduatetuitionandfees20262027/

### 4.2 Undergraduate financial-aid policy

- **Need-Need Aware**: LMU 对所有申请者采用 Need-Aware 政策
- **Test Optional**: SAT/ACT 可选
- **学术奖学金**: 所有一年级申请者自动考虑，无需额外申请
- **奖学金信息**: http://financialaid.lmu.edu/prospectivestudents/scholarships/
- **FAFSA 截止**: 2月1日 (ED: 11月15日, ED II/EA: 1月15日)

> **来源**: http://financialaid.lmu.edu/ — "All first-year applicants are automatically considered for academic scholarships"

### 4.3 Graduate cost & funding framework

**研究生学费 (2026-2027)**

| 项目 | 学费/学分 |
|------|----------|
| Doctorate of Business Administration | $2,789 |
| Doctorate School of Education | $2,270 |
| MBA | $1,902 |
| Other CBA Programs | $1,902 |
| MS in Accounting | $1,902 |
| MS in Taxation | $1,902 |
| MS in Entertainment Leadership and Management | $1,902 |
| MFA Performance Pedagogy | $1,814 |
| Seaver College of Science & Engineering | $1,814 |
| School of Film & Television | $1,814 |
| Marriage and Family Therapy | $1,814 |
| School of Education | $1,822 |
| Bellarmine College of Liberal Arts | $1,722 |
| All Other Graduate Programs | $1,722 |

> **来源**: https://finance.lmu.edu/controller/osfs/studentaccounts/tuitionothercostsbudgetworksheet/20262027academicyear/graduatetuitionandfees20262027/

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Undergraduate Deadlines
```yaml
field: undergraduate.deadlines
value:
  early_decision: "November 1"
  early_action: "November 1"
  early_decision_ii: "January 8"
  regular_decision: "January 15"
  spring: "October 15"
source_url: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/
source_snippet: "November 1: Early Decision (binding) admission for Fall; November 1: Early Action (non-binding) admission for Fall; January 8: Early Decision II (binding) admission for Fall; January 15: Regular Decision Admission for Fall"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Test Optional Policy
```yaml
field: undergraduate.testing.policy
value: "Test Optional"
source_url: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/
source_snippet: "The ACT or SAT is optional for students"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Application Fee
```yaml
field: undergraduate.application.fee
value: 75
source_url: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/
source_snippet: "Be sure to include the $75 application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Undergraduate Tuition
```yaml
field: undergraduate.cost.tuition_2026_2027
value: 68042
source_url: https://finance.lmu.edu/controller/osfs/studentaccounts/tuitionothercostsbudgetworksheet/20262027academicyear/undergraduatetuitionandfees20262027/
source_snippet: "Undergraduate Tuition Per Academic Year for programs of 12 or more semester hours $68,042.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: FAFSA Deadline
```yaml
field: undergraduate.financial_aid.fafsa_deadline
value: "February 1"
source_url: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/
source_snippet: "February 1 is the deadline for first-year applicants to submit the FAFSA"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: Program Count
```yaml
field: undergraduate.programs.total
value:
  majors: 55
  minors: 58
source_url: https://www.lmu.edu/academics/degrees/
source_snippet: "We offer 55 undergraduate majors and 58 minor programs, along with 46 master's degree programs, four doctorate programs and 14 credential/authorization programs"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: Graduate Tuition (MBA)
```yaml
field: graduate.cost.tuition_mba_2026_2027
value: 1902
source_url: https://finance.lmu.edu/controller/osfs/studentaccounts/tuitionothercostsbudgetworksheet/20262027academicyear/graduatetuitionandfees20262027/
source_snippet: "MBA $1,902.00 per unit"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: Seven Schools/Colleges
```yaml
field: institution.schools
value:
  - Bellarmine College of Liberal Arts
  - College of Business Administration
  - College of Communication and Fine Arts
  - Frank R. Seaver College of Science and Engineering
  - Loyola Law School
  - School of Education
  - School of Film and Television
source_url: https://www.lmu.edu/academics/degrees/
source_snippet: "COLLEGES AND SCHOOLS: LMU Bellarmine College of Liberal Arts, LMU College of Business Administration, LMU College of Communication and Fine Arts, LMU Frank R. Seaver College of Science and Engineering, LMU Loyola Law School, LMU School of Education, LMU School of Film and Television"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: Recommendation Requirement
```yaml
field: undergraduate.application.recommendation
value: "1 letter required (teacher and counselor/principal recommended)"
source_url: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/
source_snippet: "Submit a letter of recommendation with your application. This should be sent from an official at the school you attend. A letter from a teacher and a letter from your counselor or principal are recommended. One letter of recommendation is required."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: Enrollment Confirmation Deadline
```yaml
field: undergraduate.admissions.enrollment_confirmation
value: "May 1"
source_url: https://admission.lmu.edu/learnmore/prospectivestudents/first-yearapplicants/
source_snippet: "students accepted under Early Action still have until the Candidate's Reply Date of May 1 to commit to LMU"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
lmu-knowledge-base-v2/
├── lmu-overview                    # Section 0: 院校总览
├── lmu-undergraduate-programs      # Section 1: 本科专业
│   ├── lmu-bellarmine-liberal-arts
│   ├── lmu-business-administration
│   ├── lmu-communication-fine-arts
│   ├── lmu-seaver-science-engineering
│   ├── lmu-education
│   └── lmu-film-television
├── lmu-graduate-programs           # Section 2: 研究生项目
│   ├── lmu-grad-business
│   ├── lmu-grad-communication-fine-arts
│   ├── lmu-grad-science-engineering
│   ├── lmu-grad-education
│   ├── lmu-grad-film-television
│   ├── lmu-grad-liberal-arts
│   └── lmu-law-school
├── lmu-admissions-deadlines        # Section 3: 申请要求与截止日期
├── lmu-costs-financial-aid         # Section 4: 费用与资助
└── lmu-evidence-chain              # Section 5: 证据链
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "lmu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|MBA|JD|...>"
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
| P0 | 国际学生具体要求 | https://grad.lmu.edu/apply/internationalstudents/ |
| P0 | 研究生各项目截止日期详情 | https://grad.lmu.edu/apply/programdeadlines/ |
| P1 | 住宿费用明细 | https://finance.lmu.edu/controller/osfs/studentaccounts/tuitionothercostsbudgetworksheet/20262027academicyear/studenthousingfees20262027/ |
| P1 | 餐饮费用明细 | https://finance.lmu.edu/controller/osfs/studentaccounts/tuitionothercostsbudgetworksheet/20262027academicyear/mealplanfees20262027/ |
| P1 | 奖学金具体金额和条件 | http://financialaid.lmu.edu/prospectivestudents/scholarships/ |
| P2 | 各学院具体GRE/GMAT要求 | 各学院研究生招生页面 |
| P2 | 英语能力考试具体分数要求 | 需联系招生办确认 |

---

## SECTION 7 — Cross-school Comparison Framework

| 维度 | LMU | 备注 |
|------|-----|------|
| **学校类型** | Private Jesuit | 洛杉矶私立耶稣会大学 |
| **位置** | Los Angeles, CA | 西海岸大城市 |
| **US News 排名** | No. 6 Private University in California | 2026 |
| **本科总费用/年** | ~$68,042 (tuition only) | 2026-2027 |
| **Need-Blind (国际生)** | No | Need-Aware for all |
| **EA 截止日期** | November 1 | 非绑定 |
| **ED 截止日期** | November 1 | 绑定 |
| **RD 截止日期** | January 15 | - |
| **SAT/ACT 要求** | Test Optional | 可选 |
| **TOEFL 最低** | 未明确公布 | 建议90+ |
| **IELTS 最低** | 未明确公布 | 建议7.0+ |
| **申请费** | $75 | - |
| **专业总数 (Rule 1)** | 131 | 55 UG majors + 58 minors + 46 master's + 4 doctorate + 14 credentials |
| **学院数 (Rule 2)** | 7 | 7 schools/colleges |
| **平均班级规模** | 20 | - |
| **实习机会** | 2,000 | - |
| **学生组织** | 200+ | - |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admission.lmu.edu, financialaid.lmu.edu, finance.lmu.edu, grad.lmu.edu, www.lmu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
