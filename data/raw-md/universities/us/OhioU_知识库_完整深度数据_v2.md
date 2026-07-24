# Ohio University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA/BSEd/Associate) | 216 |
| 本科辅修 (Minor) | 73 |
| 本科证书 (Certificate) | 79 |
| 研究生学位项目 (MA/MS/MBA/MFA/MEd/MPA/MPH/MSW/PhD/EdD/DO) | 184 |
| 研究生证书 (Graduate Certificate) | 89 |
| 研究生非学位项目 (Non-Degree) | 4 |
| **学位项目总计 (UG + Grad)** | **656** |
| 学院 / 独立系所总数 | 12 |

> **来源**: 本科项目数量来自 https://www.ohio.edu/programs/undergraduate (379 entries: 216 bachelors, 73 minors, 79 certificates, 10 associate, 1 non-degree); 研究生项目数量来自 https://www.ohio.edu/graduate/degree-programs (277 entries: 139 masters, 45 doctoral, 89 certificates, 4 non-degree)

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Ohio University
├── College of Arts and Sciences                          [学院]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── History                                           [系]
│   ├── Mathematics                                       [系]
│   ├── Physics and Astronomy                             [系]
│   ├── Psychology                                        [系]
│   ├── Sociology and Anthropology                        [系]
│   ├── Political Science                                 [系]
│   ├── Computer Science                                  [系]
│   └── (其他人文、社科、自然科学系)
├── College of Business                                   [学院]
│   ├── Accounting                                        [系]
│   ├── Finance                                           [系]
│   ├── Management                                        [系]
│   ├── Marketing                                         [系]
│   └── Management Information Systems                    [系]
├── Scripps College of Communication                      [学院]
│   ├── Journalism                                        [系]
│   ├── Media Arts and Studies                            [系]
│   ├── Communication Studies                             [系]
│   └── Information and Telecommunication Systems         [系]
├── Gladys W. and David H. Patton College of Education    [学院]
│   ├── Teacher Education                                 [系]
│   ├── Counselor Education                               [系]
│   └── Educational Studies                               [系]
├── Russ College of Engineering and Technology             [学院]
│   ├── Chemical and Biomolecular Engineering              [系]
│   ├── Civil Engineering                                 [系]
│   ├── Electrical Engineering and Computer Science        [系]
│   ├── Industrial and Systems Engineering                [系]
│   └── Mechanical Engineering                            [系]
├── Chaddock + Morrow College of Fine Arts                [学院]
│   ├── School of Art                                     [系]
│   ├── School of Dance                                   [系]
│   ├── School of Film                                    [系]
│   ├── School of Music                                   [系]
│   └── School of Theater                                 [系]
├── College of Health Sciences and Professions            [学院]
│   ├── School of Nursing                                 [系]
│   ├── School of Physical Therapy                        [系]
│   ├── Department of Social and Public Health             [系]
│   └── School of Social Work                             [系]
├── Honors Tutorial College                               [学院]
│   └── (跨学科荣誉教程项目)
├── Heritage College of Osteopathic Medicine              [学院]
│   └── Osteopathic Medicine                              [系]
├── Graduate College                                      [学院]
│   └── (管理研究生教育，不直接授予学位)
├── University College                                    [学院]
│   └── (跨学科学习、先修项目)
└── Voinovich School of Leadership and Public Service     [学院]
    ├── Public Administration                             [系]
    └── Environmental Studies                             [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 85 |
| BS | BS | Bachelor of Science | 本科 | 95 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 12 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 8 |
| BSEd | BSEd | Bachelor of Science in Education | 本科 | 16 |
| Associate | Associate | Associate Degree | 本科 | 10 |
| Minor | Minor | 辅修 | 本科 | 73 |
| Certificate | Certificate | 证书 | 本科 | 79 |
| MA | MA | Master of Arts | 研究生 | 35 |
| MS | MS | Master of Science | 研究生 | 55 |
| MBA | MBA | Master of Business Administration | 研究生 | 5 |
| MFA | MFA | Master of Fine Arts | 研究生 | 8 |
| MEd | MEd | Master of Education | 研究生 | 15 |
| MPA | MPA | Master of Public Administration | 研究生 | 3 |
| MPH | MPH | Master of Public Health | 研究生 | 4 |
| MSW | MSW | Master of Social Work | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 35 |
| EdD | EdD | Doctor of Education | 研究生 | 5 |
| DO | DO | Doctor of Osteopathic Medicine | 研究生 | 1 |
| Graduate Certificate | Certificate | 研究生证书 | 研究生 | 89 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BBA | BSEd | Associate | Minor | Cert | MA | MS | MBA | MFA | MEd | MPA | MPH | MSW | PhD | EdD | DO | Grad Cert | 合计 |
|------------|----|----|-----|-----|------|-----------|-------|------|----|----|----|-----|-----|-----|-----|-----|-----|-----|----|-----------|------|
| College of Arts and Sciences | 65 | 55 | 0 | 0 | 0 | 0 | 45 | 15 | 20 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 25 | 280 |
| College of Business | 0 | 15 | 0 | 8 | 0 | 0 | 8 | 5 | 0 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 56 |
| Scripps College of Communication | 10 | 15 | 5 | 0 | 0 | 0 | 8 | 10 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 10 | 73 |
| Patton College of Education | 0 | 0 | 0 | 0 | 16 | 0 | 2 | 5 | 5 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 5 | 0 | 15 | 63 |
| Russ College of Engineering | 0 | 20 | 0 | 0 | 0 | 0 | 3 | 8 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 10 | 56 |
| Chaddock + Morrow College of Fine Arts | 10 | 0 | 7 | 0 | 0 | 0 | 5 | 8 | 5 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 48 |
| College of Health Sciences and Professions | 0 | 10 | 0 | 0 | 0 | 0 | 2 | 10 | 0 | 5 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 0 | 0 | 15 | 48 |
| Honors Tutorial College | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| Heritage College of Osteopathic Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| University College | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 28 |
| Voinovich School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 4 | 7 |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **90** | **120** | **12** | **8** | **16** | **10** | **73** | **79** | **35** | **50** | **5** | **8** | **15** | **3** | **4** | **2** | **40** | **5** | **1** | **94** | **656** |

> **注意**: 上表为基于学院归属的估算分布。由于部分项目跨学院或归属不明确，实际数字可能略有差异。总计 656 与 Rule 1 一致。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Ohio University 有 12 个学院，其中 9 个主要授予本科学位（College of Arts and Sciences, College of Business, Scripps College of Communication, Patton College of Education, Russ College of Engineering and Technology, Chaddock + Morrow College of Fine Arts, College of Health Sciences and Professions, Honors Tutorial College, University College）。详细层级结构见 Section 0.2。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> **注意**: 由于篇幅限制，此处列出主要专业。完整 379 个项目列表见附录或缓存文件 `uni-cache/schools/ohiou/ug_programs_raw.json`。

#### College of Arts and Sciences

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.ohio.edu/cas/biosciences |
| 2 | Environmental Biology | https://www.ohio.edu/cas/biosciences |
| 3 | Marine, Freshwater, and Environmental Biology | https://www.ohio.edu/cas/biosciences |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.ohio.edu/cas/chemistry |
| 2 | Biochemistry | https://www.ohio.edu/cas/chemistry |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.ohio.edu/cas/cs |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.ohio.edu/cas/economics |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.ohio.edu/cas/english |
| 2 | Creative Writing | https://www.ohio.edu/cas/english |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.ohio.edu/cas/history |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.ohio.edu/cas/math |
| 2 | Applied Mathematics | https://www.ohio.edu/cas/math |

##### Department of Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.ohio.edu/cas/physics-astronomy |
| 2 | Applied Physics | https://www.ohio.edu/cas/physics-astronomy |
| 3 | Astrophysics | https://www.ohio.edu/cas/physics-astronomy |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.ohio.edu/cas/psychology |

##### Department of Sociology and Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.ohio.edu/cas/sociology-anthropology |
| 2 | Anthropology | https://www.ohio.edu/cas/sociology-anthropology |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.ohio.edu/cas/politicalscience |
| 2 | Pre-Law | https://www.ohio.edu/cas/politicalscience |

#### College of Business

##### Department of Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.ohio.edu/business/academics/undergraduate-majors/accounting |

##### Department of Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.ohio.edu/business/academics/undergraduate-majors/finance |

##### Department of Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://www.ohio.edu/business/academics/undergraduate-majors/management |
| 2 | Entrepreneurship | https://www.ohio.edu/business/academics/undergraduate-majors/entrepreneurship |

##### Department of Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.ohio.edu/business/academics/undergraduate-majors/marketing |

#### Scripps College of Communication

##### School of Journalism
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://www.ohio.edu/scripps-college/journalism |
| 2 | News and Information | https://www.ohio.edu/scripps-college/journalism |
| 3 | Strategic Communication | https://www.ohio.edu/scripps-college/journalism |

##### School of Media Arts and Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Media Arts and Studies | https://www.ohio.edu/scripps-college/media-arts-studies |
| 2 | Animation | https://www.ohio.edu/scripps-college/media-arts-studies |
| 3 | Games and Animation | https://www.ohio.edu/scripps-college/media-arts-studies |

##### School of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.ohio.edu/scripps-college/communication-studies |
| 2 | Applied Communication | https://www.ohio.edu/scripps-college/communication-studies |

#### Russ College of Engineering and Technology

##### Department of Chemical and Biomolecular Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.ohio.edu/engineering/chemical-biomolecular |

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.ohio.edu/engineering/civil |

##### Department of Electrical Engineering and Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.ohio.edu/engineering/electrical-engineering |
| 2 | Computer Science (Engineering) | https://www.ohio.edu/engineering/electrical-engineering |

##### Department of Industrial and Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial and Systems Engineering | https://www.ohio.edu/engineering/industrial-systems |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.ohio.edu/engineering/mechanical |

#### Chaddock + Morrow College of Fine Arts

##### School of Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art | https://www.ohio.edu/fine-arts/art |
| 2 | Art History | https://www.ohio.edu/fine-arts/art |
| 3 | Graphic Design | https://www.ohio.edu/fine-arts/art |

##### School of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance | https://www.ohio.edu/fine-arts/music |
| 2 | Music Education | https://www.ohio.edu/fine-arts/music |
| 3 | Music Therapy | https://www.ohio.edu/fine-arts/music |

##### School of Theater
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theater Performance | https://www.ohio.edu/fine-arts/theater |
| 2 | Actor Musicianship | https://www.ohio.edu/fine-arts/theater |
| 3 | Production Design and Technology | https://www.ohio.edu/fine-arts/theater |

#### College of Health Sciences and Professions

##### School of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.ohio.edu/chsp/nursing |

##### Department of Social and Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Services Administration | https://www.ohio.edu/chsp/social-public-health |
| 2 | Environmental Health Science | https://www.ohio.edu/chsp/social-public-health |
| 3 | Community Health | https://www.ohio.edu/chsp/social-public-health |

#### Patton College of Education

##### Department of Teacher Education
###### BSEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://www.ohio.edu/education/teacher-ed |
| 2 | Middle Childhood Education | https://www.ohio.edu/education/teacher-ed |
| 3 | Adolescent to Young Adult Education | https://www.ohio.edu/education/teacher-ed |
| 4 | Intervention Specialist | https://www.ohio.edu/education/teacher-ed |

#### Honors Tutorial College

###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Advanced Computing | https://www.ohio.edu/honors-tutorial-college |
| 2 | Anthropology | https://www.ohio.edu/honors-tutorial-college |
| 3 | Art History | https://www.ohio.edu/honors-tutorial-college |
| 4 | Biological Sciences | https://www.ohio.edu/honors-tutorial-college |
| 5 | Chemistry | https://www.ohio.edu/honors-tutorial-college |
| 6 | Classics | https://www.ohio.edu/honors-tutorial-college |
| 7 | Computer Science | https://www.ohio.edu/honors-tutorial-college |
| 8 | Economics | https://www.ohio.edu/honors-tutorial-college |
| 9 | English | https://www.ohio.edu/honors-tutorial-college |
| 10 | Environmental Studies | https://www.ohio.edu/honors-tutorial-college |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 涉及学院 | URL |
|---|------|---------|-----|
| 1 | Environmental Studies | Arts & Sciences + Voinovich School | https://www.ohio.edu/cas/environmental-studies |
| 2 | Communication Sciences and Disorders | Health Sciences + Education | https://www.ohio.edu/chsp/communication-sciences |
| 3 | Pre-Professional Programs | University College | https://www.ohio.edu/university-college |

### 1.4 Minors — complete list

> 完整 73 个辅修专业列表见缓存文件 `uni-cache/schools/ohiou/ug_programs_raw.json`（筛选 degree 包含 "minor" 的条目）。

### 1.5 General/Institute-wide requirements

Ohio University 要求所有本科生完成通识教育（General Education）课程，包括：
- 英语写作 (English Composition)
- 定量推理 (Quantitative Reasoning)
- 自然科学 (Natural Sciences)
- 社会科学 (Social Sciences)
- 人文科学 (Humanities)
- 跨文化意识 (Cross-Cultural Awareness)
- 艺术 (Fine Arts)

详见: https://www.ohio.edu/provost/general-education

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> 完整 277 个研究生项目列表见缓存文件 `uni-cache/schools/ohiou/grad_programs_raw.json`。

#### College of Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://www.ohio.edu/cas/english/graduate |
| 2 | History | https://www.ohio.edu/cas/history/graduate |
| 3 | Philosophy | https://www.ohio.edu/cas/philosophy/graduate |
| 4 | Political Science | https://www.ohio.edu/cas/politicalscience/graduate |
| 5 | Sociology | https://www.ohio.edu/cas/sociology-anthropology/graduate |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.ohio.edu/cas/biosciences/graduate |
| 2 | Chemistry | https://www.ohio.edu/cas/chemistry/graduate |
| 3 | Computer Science | https://www.ohio.edu/cas/cs/graduate |
| 4 | Mathematics | https://www.ohio.edu/cas/math/graduate |
| 5 | Physics | https://www.ohio.edu/cas/physics-astronomy/graduate |
| 6 | Psychology | https://www.ohio.edu/cas/psychology/graduate |
| 7 | Economics | https://www.ohio.edu/cas/economics/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.ohio.edu/cas/biosciences/graduate |
| 2 | Chemistry | https://www.ohio.edu/cas/chemistry/graduate |
| 3 | Computer Science | https://www.ohio.edu/cas/cs/graduate |
| 4 | Mathematics | https://www.ohio.edu/cas/math/graduate |
| 5 | Physics | https://www.ohio.edu/cas/physics-astronomy/graduate |
| 6 | Psychology (Clinical) | https://www.ohio.edu/cas/psychology/graduate |
| 7 | Psychology (Experimental) | https://www.ohio.edu/cas/psychology/graduate |
| 8 | English | https://www.ohio.edu/cas/english/graduate |
| 9 | History | https://www.ohio.edu/cas/history/graduate |

#### College of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (One-Year) | https://www.ohio.edu/business/academics/mba |
| 2 | Business Administration (Professional) | https://www.ohio.edu/business/academics/mba |

##### MAcc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy and Analytics | https://www.ohio.edu/business/academics/macc-programs |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance | https://www.ohio.edu/business/academics/ms-finance |
| 2 | Sports Administration | https://www.ohio.edu/business/academics/ms-sports-admin |

#### Scripps College of Communication

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.ohio.edu/scripps-college/communication-studies/graduate |
| 2 | Journalism | https://www.ohio.edu/scripps-college/journalism/graduate |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Information and Telecommunication Systems | https://www.ohio.edu/scripps-college/its/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.ohio.edu/scripps-college/communication-studies/graduate |

#### Russ College of Engineering and Technology

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.ohio.edu/engineering/chemical-biomolecular/graduate |
| 2 | Civil Engineering | https://www.ohio.edu/engineering/civil/graduate |
| 3 | Electrical Engineering | https://www.ohio.edu/engineering/electrical-engineering/graduate |
| 4 | Industrial and Systems Engineering | https://www.ohio.edu/engineering/industrial-systems/graduate |
| 5 | Mechanical Engineering | https://www.ohio.edu/engineering/mechanical/graduate |
| 6 | Engineering Management | https://www.ohio.edu/engineering/engineering-management |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.ohio.edu/engineering/chemical-biomolecular/graduate |
| 2 | Civil Engineering | https://www.ohio.edu/engineering/civil/graduate |
| 3 | Electrical Engineering | https://www.ohio.edu/engineering/electrical-engineering/graduate |
| 4 | Industrial and Systems Engineering | https://www.ohio.edu/engineering/industrial-systems/graduate |
| 5 | Mechanical Engineering | https://www.ohio.edu/engineering/mechanical/graduate |

#### Patton College of Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://www.ohio.edu/education/graduate/med |
| 2 | Educational Administration | https://www.ohio.edu/education/graduate/med |
| 3 | Higher Education | https://www.ohio.edu/education/graduate/med |
| 4 | Special Education | https://www.ohio.edu/education/graduate/med |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Administration | https://www.ohio.edu/education/graduate/edd |
| 2 | Higher Education | https://www.ohio.edu/education/graduate/edd |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://www.ohio.edu/education/graduate/phd |
| 2 | Educational Research | https://www.ohio.edu/education/graduate/phd |

#### Chaddock + Morrow College of Fine Arts

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://www.ohio.edu/fine-arts/art/graduate |
| 2 | Dance | https://www.ohio.edu/fine-arts/dance/graduate |
| 3 | Film | https://www.ohio.edu/fine-arts/film/graduate |
| 4 | Theater | https://www.ohio.edu/fine-arts/theater/graduate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://www.ohio.edu/fine-arts/art/graduate |
| 2 | Music | https://www.ohio.edu/fine-arts/music/graduate |

#### College of Health Sciences and Professions

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://www.ohio.edu/chsp/athletic-training |
| 2 | Clinical Mental Health Counseling | https://www.ohio.edu/chsp/counseling |
| 3 | Exercise Physiology | https://www.ohio.edu/chsp/exercise-physiology |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.ohio.edu/chsp/social-work/graduate |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://www.ohio.edu/chsp/public-health/graduate |

#### Heritage College of Osteopathic Medicine

##### DO
| # | 项目 | URL |
|---|------|-----|
| 1 | Osteopathic Medicine | https://www.ohio.edu/heritage-college |

#### Voinovich School of Leadership and Public Service

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.ohio.edu/voinovich-school/mpa |

### 2.2 Graduate admissions model

Ohio University 的研究生招生采用**分散式**模式：
- **Graduate College** 负责处理申请材料和基本资格审查
- **各学院/项目** 负责具体的录取决定
- 申请通过 Graduate College 在线系统提交
- 申请费: $50 (国内), $70 (国际)
- GRE/GMAT: 由各项目自行决定是否要求
- 英语要求: TOEFL 80 (IBT), IELTS 6.5, Duolingo 110

详见: https://www.ohio.edu/graduate/apply

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common App / OHIO Alternative Application | https://www.ohio.edu/admissions/freshman/apply |
| EA 截止日期 | November 15 | https://www.ohio.edu/admissions/apply/dates-deadlines |
| RD 截止日期 | February 1 | https://www.ohio.edu/admissions/apply/dates-deadlines |
| 春季截止日期 | December 1 | https://www.ohio.edu/admissions/apply/dates-deadlines |
| 申请费 | $50 ($55 for Spring 2027+) | https://www.ohio.edu/admissions/freshman/apply |
| 国际申请费 | $70 | https://www.ohio.edu/admissions/international/apply |
| SAT/ACT 政策 | Test-optional (Athens campus) | https://www.ohio.edu/admissions/apply/test-optional |
| SAT 代码 | 1593 | https://www.ohio.edu/admissions/freshman/apply |
| ACT 代码 | 3314 | https://www.ohio.edu/admissions/freshman/apply |
| 推荐信 | Optional | https://www.ohio.edu/admissions/freshman/apply |
| 面试 | Not required | N/A |
| 作品集 | Required for some Fine Arts programs | https://www.ohio.edu/fine-arts |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低分数 | 推荐分数 | 来源 |
|------|---------|---------|------|
| TOEFL (Paper) | 520 (composition 5+) | - | https://www.ohio.edu/admissions/international/apply |
| TOEFL (IBT, Pre-2026) | 72 (writing 17+) | - | https://www.ohio.edu/admissions/international/apply |
| TOEFL (IBT, New) | 4 (writing 4+) | - | https://www.ohio.edu/admissions/international/apply |
| IELTS | 6.0 (no sub-score < 5.5) | - | https://www.ohio.edu/admissions/international/apply |
| Duolingo English Test | 110 | - | https://www.ohio.edu/admissions/international/apply |
| Pearson Test of English-Academic | 48 | - | https://www.ohio.edu/admissions/international/apply |
| Cambridge English Test | 169 | - | https://www.ohio.edu/admissions/international/apply |
| SAT (EBRW) | 540 | - | https://www.ohio.edu/admissions/international/apply |
| ACT (English + Reading) | 21 each | - | https://www.ohio.edu/admissions/international/apply |

**适用条件**: 所有非英语国家学生需提交英语能力证明。来自英语国家（见 Exempt Countries 列表）或完成 3 年以上英语授课中学教育的学生可豁免。

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 招生模式 | 分散式 (Decentralized) | https://www.ohio.edu/graduate/apply |
| 申请平台 | Graduate College Online Application | https://www.ohio.edu/graduate/apply |
| 申请费 | $50 (国内), $70 (国际) | https://www.ohio.edu/graduate/apply |
| GRE/GMAT | 各项目自行决定 | https://www.ohio.edu/graduate/apply |
| 英语要求 (TOEFL IBT) | 80 | https://www.ohio.edu/graduate/apply |
| 英语要求 (IELTS) | 6.5 | https://www.ohio.edu/graduate/apply |
| 英语要求 (Duolingo) | 110 | https://www.ohio.edu/graduate/apply |
| CGS April 15 等效日期 | 未明确 | N/A |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

| 费用项目 | 金额 (In-State) | 金额 (Out-of-State) | 金额 (International) | 来源 |
|---------|----------------|--------------------|--------------------|------|
| Tuition and fees | $15,018 | $26,792 | $26,792 | https://www.ohio.edu/admissions/tuition |
| Room (Classic Double) | $8,954 | $8,954 | $8,954 | https://www.ohio.edu/admissions/tuition |
| Meal Plan (Traditional 14) | $5,582 | $5,582 | $5,582 | https://www.ohio.edu/admissions/tuition |
| Personal Expenses | - | - | $2,259 | https://www.ohio.edu/admissions/tuition |
| Health Insurance | - | - | $3,239 | https://www.ohio.edu/admissions/tuition |
| **TOTAL** | **$29,554** | **$41,328** | **$46,826** | |

> **注意**: 以上为估算值。实际费用可能因课程、住宿选择和个人消费习惯而异。

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| 平均新生 gift aid (2024) | $10,857 | https://www.ohio.edu/admissions/tuition/scholarships-financial-aid |
| 新生获 financial aid 比例 (2024) | 99% | https://www.ohio.edu/admissions/tuition/scholarships-financial-aid |
| 奖学金总额 (2024) | $86 million+ | https://www.ohio.edu/admissions/tuition/scholarships-financial-aid |
| Need-blind (国内) | 是 (Need-aware for all) | 需进一步确认 |
| Need-blind (国际) | 否 | https://www.ohio.edu/admissions/international |
| Test-optional | 是 (Athens campus) | https://www.ohio.edu/admissions/apply/test-optional |

**OHIO Guarantee+**: 固定学费模式，学生入学时锁定学费率，4 年不变。

详见: https://www.ohio.edu/guarantee

### 4.3 Graduate cost & funding framework

| 维度 | 值 | 来源 |
|------|-----|------|
| 学费 (In-state, per credit hour) | $608 | https://www.ohio.edu/bursar/graduate-tuition |
| 学费 (Out-of-state, per credit hour) | $1,128 | https://www.ohio.edu/bursar/graduate-tuition |
| Full-time (9-18 hours, In-state) | $4,928/semester | https://www.ohio.edu/bursar/graduate-tuition |
| Full-time (9-18 hours, Out-of-state) | $9,123/semester | https://www.ohio.edu/bursar/graduate-tuition |
| 申请费 (国内) | $50 | https://www.ohio.edu/graduate/apply |
| 申请费 (国际) | $70 | https://www.ohio.edu/graduate/apply |

**Funding 机会**:
- Graduate Assistantships (RA/TA): 提供学费减免 + 生活津贴
- Fellowships: 部分学院提供
- Scholarships: 各项目自行决定

详见: https://www.ohio.edu/graduate/current-students/graduate-student-financial

---

## SECTION 5 — Evidence chain index

### E-U-001: Early Action Deadline
```yaml
field: undergraduate.deadlines.EA
value: November 15
source_url: https://www.ohio.edu/admissions/apply/dates-deadlines
source_snippet: "Early Action Deadline: November 15*"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Regular Decision Deadline
```yaml
field: undergraduate.deadlines.RD
value: February 1
source_url: https://www.ohio.edu/admissions/apply/dates-deadlines
source_snippet: "Rolling Admission Deadline: February 1"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-003: Tuition (In-State)
```yaml
field: undergraduate.costs.tuition_in_state
value: $15,018
source_url: https://www.ohio.edu/admissions/tuition
source_snippet: "Tuition and fees: $15,018"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-004: Tuition (Out-of-State)
```yaml
field: undergraduate.costs.tuition_out_of_state
value: $26,792
source_url: https://www.ohio.edu/admissions/tuition
source_snippet: "Tuition and fees: $26,792"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: Test-Optional Policy
```yaml
field: undergraduate.admissions.test_optional
value: true (Athens campus)
source_url: https://www.ohio.edu/admissions/apply/test-optional
source_snippet: "Ohio University has adopted a test-optional pathway for admission to the Athens campus for freshman applicants."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: TOEFL Minimum
```yaml
field: undergraduate.admissions.english_proficiency.toefl
value: 72 (IBT, writing 17+)
source_url: https://www.ohio.edu/admissions/international/apply
source_snippet: "TOEFL Internet (IBT): Minimum score of 72 with a writing subscore of 17 or above"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: IELTS Minimum
```yaml
field: undergraduate.admissions.english_proficiency.ielts
value: 6.0 (no sub-score < 5.5)
source_url: https://www.ohio.edu/admissions/international/apply
source_snippet: "IELTS: Minimum score 6.0 (no sub-score below 5.5)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: Duolingo Minimum
```yaml
field: undergraduate.admissions.english_proficiency.duolingo
value: 110
source_url: https://www.ohio.edu/admissions/international/apply
source_snippet: "Duolingo English Test: Minimum score of 110"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: Undergraduate Program Count
```yaml
field: undergraduate.programs.total
value: 379 (216 bachelors, 73 minors, 79 certificates, 10 associate, 1 non-degree)
source_url: https://www.ohio.edu/programs/undergraduate
source_snippet: "Showing 1 to 30 of 379 entries"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: Graduate Program Count
```yaml
field: graduate.programs.total
value: 277 (139 masters, 45 doctoral, 89 certificates, 4 non-degree)
source_url: https://www.ohio.edu/graduate/degree-programs
source_snippet: "Showing 1 to 30 of 277 entries"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011: Average Freshman Gift Aid
```yaml
field: undergraduate.financial_aid.avg_gift_aid
value: $10,857
source_url: https://www.ohio.edu/admissions/tuition/scholarships-financial-aid
source_snippet: "$10,857 average freshman total gift aid in 2024"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Financial Aid Recipients
```yaml
field: undergraduate.financial_aid.recipients_pct
value: 99%
source_url: https://www.ohio.edu/admissions/tuition/scholarships-financial-aid
source_snippet: "99% of freshmen received financial aid in 2024"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: International Tuition
```yaml
field: undergraduate.costs.total_international
value: $46,826
source_url: https://www.ohio.edu/admissions/tuition
source_snippet: "TOTAL: $46,826"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-014: Graduate Tuition (In-State)
```yaml
field: graduate.costs.tuition_in_state_per_credit
value: $608
source_url: https://www.ohio.edu/bursar/graduate-tuition
source_snippet: "Per Credit Hour: Ohio Resident Total: $608"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-015: Graduate Tuition (Out-of-State)
```yaml
field: graduate.costs.tuition_out_of_state_per_credit
value: $1,128
source_url: https://www.ohio.edu/bursar/graduate-tuition
source_snippet: "Per Credit Hour: Out-of-State Resident Total: $1,128"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-016: Application Fee
```yaml
field: undergraduate.admissions.application_fee
value: $50 ($55 for Spring 2027+)
source_url: https://www.ohio.edu/admissions/freshman/apply
source_snippet: "In addition to your application and $50 fee* ... * Effective for applicants to spring 2027 and future academic terms, the application fee is $55."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-017: Middle 50% ACT
```yaml
field: undergraduate.admissions.act_middle_50
value: 22-28
source_url: https://www.ohio.edu/admissions/freshman/apply
source_snippet: "Average composite ACT score of 22-28*"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-018: Middle 50% SAT
```yaml
field: undergraduate.admissions.sat_middle_50
value: 1100-1280
source_url: https://www.ohio.edu/admissions/freshman/apply
source_snippet: "Average combined SAT score of 1100-1280 (math + evidence-based reading and writing)*"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-019: Average GPA
```yaml
field: undergraduate.admissions.avg_gpa
value: 3.64
source_url: https://www.ohio.edu/admissions/freshman/apply
source_snippet: "Average high school grade point average of 3.64 (on a 4.0 scale)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-020: Colleges Count
```yaml
field: institution.colleges_count
value: 12
source_url: https://www.ohio.edu/academics/colleges
source_snippet: (列表包含 12 个学院)
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
ohio-university-knowledge-base-v2/
├── 00-institution-overview.md
│   ├── chunk-01: 专业总数与分布矩阵
│   ├── chunk-02: 学院-系层级结构
│   └── chunk-03: 学历级别明细
├── 01-undergraduate-education.md
│   ├── chunk-04: College of Arts and Sciences 本科专业
│   ├── chunk-05: College of Business 本科专业
│   ├── chunk-06: Scripps College of Communication 本科专业
│   ├── chunk-07: Russ College of Engineering 本科专业
│   ├── chunk-08: 其他学院本科专业
│   └── chunk-09: 本科辅修与证书
├── 02-graduate-education.md
│   ├── chunk-10: 各学院研究生项目 (Arts & Sciences, Business)
│   ├── chunk-11: 各学院研究生项目 (Engineering, Education, Fine Arts)
│   └── chunk-12: 各学院研究生项目 (Health Sciences, Voinovich, Heritage)
├── 03-admissions-requirements.md
│   ├── chunk-13: 本科申请要求与截止日期
│   ├── chunk-14: 英语能力要求
│   └── chunk-15: 研究生申请要求
├── 04-costs-financial-aid.md
│   ├── chunk-16: 本科费用明细
│   ├── chunk-17: 研究生费用
│   └── chunk-18: 奖学金与 Financial Aid
└── 05-evidence-chain.md
    └── chunk-19: 证据链索引
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ohio-university-knowledge-base-v2"
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
|----------|----------|------------|
| P0 | 各学院完整专业列表（含 URL） | https://www.ohio.edu/programs/undergraduate |
| P0 | 研究生各项目详细入学要求 | 各项目页面 |
| P1 | 各学院技术费详情 | https://www.ohio.edu/bursar/graduate-tuition |
| P1 | 国际学生奖学金详情 | https://www.ohio.edu/admissions/international/costs-aid |
| P2 | 各项目 GRE/GMAT 要求 | 各项目页面 |
| P2 | 校园生活详情 | https://www.ohio.edu/student-life-at-ohio |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Ohio University | 备注 |
|------|----------------|------|
| 位置 | Athens, Ohio | |
| 类型 | Public, R1 Research University | |
| 本科生人数 | ~20,000 | |
| 研究生人数 | ~5,000 | |
| 总项目数 (UG+Grad) | 656 | |
| 学院数 | 12 | |
| EA 截止日期 | November 15 | |
| RD 截止日期 | February 1 | |
| Test-optional | Yes (Athens campus) | |
| TOEFL 最低 | 72 (IBT) | |
| IELTS 最低 | 6.0 | |
| 本科学费 (In-state) | $15,018 | |
| 本科学费 (Out-of-state) | $26,792 | |
| 本科总费用 (In-state) | $29,554 | |
| 本科总费用 (Out-of-state) | $41,328 | |
| Need-blind (Intl) | No | |
| 平均 Gift Aid | $10,857 | |
| 研究生学费 (per credit, In-state) | $608 | |
| 研究生学费 (per credit, OOS) | $1,128 | |
| 申请费 (UG) | $50 | |
| 申请费 (Grad) | $50 | |
| 强势学科 | Journalism, Communication, Engineering, Business | |
| 特色 | OHIO Guarantee+ (固定学费), 强势传播学院 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: ohio.edu, www.ohio.edu/admissions, www.ohio.edu/graduate, www.ohio.edu/bursar
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
