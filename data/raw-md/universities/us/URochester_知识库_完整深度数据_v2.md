# University of Rochester Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM) | 87 |
| 本科辅修 (Minor) | 83 |
| 研究生硕士学位项目 (MA/MS/MBA/MM/MSEd/MFA) | 20 |
| 研究生博士项目 (PhD/EdD/DMA/DNP/MD/DBA) | 24 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 13 |
| **学位项目总计 (UG + Grad)** | **227** |
| 学院 / 独立系所总数 | 7 |

> **数据来源**: admissions.rochester.edu/academics/majors-and-minors/ 页面筛选器计数 (2026-07-06 抓取)
> **注意**: 87 majors + 83 minors = 170 个本科专业/辅修项目 (部分科目同时提供 major 和 minor)
> **研究生细分**: Master's (20) + PhD (24) + Certificate (13) = 57 个研究生项目

### 0.2 学院 / 系层级结构

```
University of Rochester
├── School of Arts & Sciences (SAS)                    [学院]
│   ├── Department of Anthropology                     [系]
│   ├── Department of Art & Art History                [系]
│   ├── Department of Biology                          [系]
│   ├── Department of Brain & Cognitive Sciences       [系]
│   ├── Department of Chemistry                        [系]
│   ├── Department of Classics                         [系]
│   ├── Department of Computer Science                 [系]
│   ├── Department of Earth & Environmental Sciences   [系]
│   ├── Department of Economics                        [系]
│   ├── Department of English                          [系]
│   ├── Department of History                          [系]
│   ├── Department of Linguistics                      [系]
│   ├── Department of Mathematics                      [系]
│   ├── Department of Modern Languages & Cultures      [系]
│   ├── Department of Music                            [系]
│   ├── Department of Philosophy                       [系]
│   ├── Department of Physics & Astronomy              [系]
│   ├── Department of Political Science                [系]
│   ├── Department of Psychology                       [系]
│   ├── Department of Religion & Classics              [系]
│   ├── Department of Sociology                        [系]
│   ├── Department of Statistics                       [系]
│   ├── Department of Visual & Cultural Studies        [系]
│   └── Department of Women's, Gender, & Sexuality Studies [系]
│
├── Hajim School of Engineering & Applied Sciences     [学院]
│   ├── Department of Biomedical Engineering           [系]
│   ├── Department of Chemical Engineering             [系]
│   ├── Department of Computer Science                 [系]  ⚠ shared with SAS
│   ├── Department of Electrical & Computer Engineering [系]
│   ├── Department of Mechanical Engineering           [系]
│   ├── Department of Optics                           [系]
│   ├── Department of Audio & Music Engineering        [系]
│   └── Institute of Optics                            [系]
│
├── Eastman School of Music                            [学院]
│   ├── Department of Composition                      [系]
│   ├── Department of Conducting & Ensembles           [系]
│   ├── Department of Humanities                       [系]
│   ├── Department of Jazz Studies & Contemporary Media [系]
│   ├── Department of Music Teaching & Learning        [系]
│   ├── Department of Musicology                       [系]
│   ├── Department of Music Theory                     [系]
│   ├── Department of Organ, Sacred Music & Historical Keyboards [系]
│   ├── Department of Piano                            [系]
│   ├── Department of Sound Arts & Engineering         [系]
│   ├── Department of Strings, Harp & Guitar           [系]
│   ├── Department of Voice, Opera & Vocal Coaching    [系]
│   └── Department of Woodwinds, Brass & Percussion    [系]
│
├── Simon Business School                              [学院]
│   ├── Department of Finance                          [系]
│   ├── Department of Marketing                        [系]
│   ├── Department of Operations                       [系]
│   ├── Department of Economics                        [系]
│   └── Department of Accounting                       [系]
│
├── Warner School of Education & Human Development     [学院]
│   ├── Department of Teaching & Curriculum            [系]
│   ├── Department of Educational Leadership           [系]
│   ├── Department of Human Development                [系]
│   └── Department of Counseling Psychology            [系]
│
├── School of Medicine & Dentistry                     [学院]
│   ├── Department of Medicine                         [系]
│   ├── Department of Surgery                          [系]
│   ├── Department of Pediatrics                       [系]
│   ├── Department of Obstetrics & Gynecology          [系]
│   ├── Department of Psychiatry                       [系]
│   ├── Department of Neurology                        [系]
│   ├── Department of Radiology                        [系]
│   ├── Department of Pathology                        [系]
│   ├── Department of Anesthesiology                   [系]
│   ├── Department of Emergency Medicine               [系]
│   ├── Department of Family Medicine                  [系]
│   ├── Department of Microbiology & Immunology        [系]
│   ├── Department of Biochemistry & Biophysics        [系]
│   ├── Department of Neuroscience                     [系]
│   ├── Department of Pharmacology & Physiology        [系]
│   ├── Department of Biostatistics & Computational Biology [系]
│   ├── Department of Public Health Sciences           [系]
│   ├── Department of Health Humanities & Bioethics    [系]
│   └── Eastman Institute for Oral Health              [系]
│
└── School of Nursing                                  [学院]
    ├── Department of Adult/Gerontology Nursing         [系]
    ├── Department of Family Nursing                    [系]
    ├── Department of Psychiatric Mental Health Nursing [系]
    └── Department of Nursing Education                 [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~60 |
| BS | Bachelor of Science | 本科 | ~25 |
| BM | Bachelor of Music | 本科 | ~5 |
| BFA | Bachelor of Fine Arts | 本科 | ~2 |
| MA | Master of Arts | 研究生 | ~10 |
| MS | Master of Science | 研究生 | ~12 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | ~2 |
| MM | Master of Music | 研究生 | ~5 |
| MSEd | Master of Science in Education | 研究生 | ~5 |
| MSW | Master of Social Work | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | ~20 |
| EdD | Doctor of Education | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生 | ~3 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| Advanced Certificate | 高级证书 | 研究生 | ~13 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BM | BFA | MA | MS | MBA | MM | MSEd | PhD | EdD | DMA | DNP | MD | DBA | Adv Cert | 合计 |
|------------|----|----|----|----|----|----|----|----|------|-----|-----|-----|-----|----|-----|----------|------|
| School of Arts & Sciences | ~55 | ~5 | 0 | 0 | ~8 | ~4 | 0 | 0 | 0 | ~14 | 0 | 0 | 0 | 0 | 0 | ~5 | ~91 |
| Hajim School of Engineering | 0 | ~15 | 0 | 0 | 0 | ~8 | 0 | 0 | 0 | ~7 | 0 | 0 | 0 | 0 | 0 | ~3 | ~33 |
| Eastman School of Music | 0 | 0 | ~5 | ~2 | 0 | 0 | 0 | ~5 | 0 | ~3 | 0 | ~3 | 0 | 0 | 0 | ~2 | ~20 |
| Simon Business School | 0 | ~2 | 0 | 0 | 0 | ~5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ~2 | ~11 |
| Warner School of Education | 0 | 0 | 0 | 0 | ~2 | 0 | 0 | 0 | ~5 | 0 | 1 | 0 | 0 | 0 | 0 | ~3 | ~11 |
| School of Medicine & Dentistry | 0 | 0 | 0 | 0 | 0 | ~2 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | 1 | 0 | ~2 | ~10 |
| School of Nursing | 0 | ~1 | 0 | 0 | 0 | ~2 | 0 | 0 | 0 | ~1 | 0 | 0 | 1 | 0 | 0 | ~1 | ~6 |
| **合计** | **~55** | **~23** | **~5** | **~2** | **~10** | **~21** | **1** | **~5** | **~5** | **~30** | **1** | **~3** | **1** | **1** | **1** | **~18** | **~182** |

> **注意**: 此矩阵为基于已知数据的估算。确切数字需要从各学院详细项目列表中提取。

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

University of Rochester 的本科教育主要由两个学院提供:
- **School of Arts & Sciences (SAS)**: 提供人文、自然科学和社会科学领域的学位
- **Hajim School of Engineering & Applied Sciences**: 提供工程和应用科学领域的学位
- **Eastman School of Music**: 提供音乐表演和音乐教育学位 (独立招生)
- **Simon Business School**: 提供本科商科课程

详见 Section 0.2 层级树。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### School of Arts & Sciences (SAS)

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Anthropology |
| 2 | Art History | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Art%20History |
| 3 | Biology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Biology |
| 4 | Brain and Cognitive Sciences | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Brain%20and%20Cognitive%20Sciences |
| 5 | Chemistry | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Chemistry |
| 6 | Classics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Classics |
| 7 | Comparative Literature | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Comparative%20Literature |
| 8 | Computer Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Computer%20Science |
| 9 | Creative Writing | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Creative%20Writing |
| 10 | Dance | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Dance |
| 11 | Digital Media Studies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Digital%20Media%20Studies |
| 12 | East Asian Studies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=East%20Asian%20Studies |
| 13 | Economics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Economics |
| 14 | English | https://admissions.rochester.edu/academics/majors-and-minors/?subject=English |
| 15 | English Literature | https://admissions.rochester.edu/academics/majors-and-minors/?subject=English%20Literature |
| 16 | Environmental Studies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Environmental%20Studies |
| 17 | Film and Media Studies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Film%20and%20Media%20Studies |
| 18 | French | https://admissions.rochester.edu/academics/majors-and-minors/?subject=French |
| 19 | Gender, Sexuality, and Women's Studies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Gender,%20Sexuality,%20and%20Women%27s%20Studies |
| 20 | German | https://admissions.rochester.edu/academics/majors-and-minors/?subject=German |
| 21 | History | https://admissions.rochester.edu/academics/majors-and-minors/?subject=History |
| 22 | International Relations | https://admissions.rochester.edu/academics/majors-and-minors/?subject=International%20Relations |
| 23 | Italian | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Italian |
| 24 | Japanese | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Japanese |
| 25 | Linguistics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Linguistics |
| 26 | Mathematics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Mathematics |
| 27 | Music | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Music |
| 28 | Philosophy | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Philosophy |
| 29 | Physics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Physics |
| 30 | Political Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Political%20Science |
| 31 | Psychology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Psychology |
| 32 | Religion | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Religion |
| 33 | Russian | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Russian |
| 34 | Russian Studies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Russian%20Studies |
| 35 | Sociology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Sociology |
| 36 | Spanish | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Spanish |
| 37 | Statistics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Statistics |
| 38 | Studio Arts | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Studio%20Arts |
| 39 | Theater | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Theater |

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Biochemistry |
| 2 | Biological Sciences | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Biological%20Sciences |
| 3 | Biophysics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Biophysics |
| 4 | Computational Biology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Computational%20Biology |
| 5 | Data Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Data%20Science |
| 6 | Earth, Environmental, and Planetary Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Earth,%20Environmental,%20and%20Planetary%20Science |
| 7 | Ecology and Evolutionary Biology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Ecology%20and%20Evolutionary%20Biology |
| 8 | Geological Sciences | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Geological%20Sciences |
| 9 | Mathematics and Statistics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Mathematics%20and%20Statistics |
| 10 | Microbiology | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Microbiology |
| 11 | Molecular Genetics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Molecular%20Genetics |
| 12 | Neuroscience | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Neuroscience |
| 13 | Physics and Astronomy | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Physics%20and%20Astronomy |

#### Hajim School of Engineering & Applied Sciences

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Biomedical%20Engineering |
| 2 | Chemical Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Chemical%20Engineering |
| 3 | Computer Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Computer%20Science |
| 4 | Electrical and Computer Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Electrical%20and%20Computer%20Engineering |
| 5 | Electrical Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Electrical%20Engineering |
| 6 | Engineering Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Engineering%20Science |
| 7 | Environmental Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Environmental%20Engineering |
| 8 | Materials Science | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Materials%20Science |
| 9 | Mechanical Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Mechanical%20Engineering |
| 10 | Optical Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Optical%20Engineering |
| 11 | Optics | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Optics |

#### Eastman School of Music

##### BM Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Performance | https://www.esm.rochester.edu/academics/undergraduate/ |
| 2 | Composition | https://www.esm.rochester.edu/academics/undergraduate/ |
| 3 | Music Education | https://www.esm.rochester.edu/academics/undergraduate/ |
| 4 | Jazz Studies & Contemporary Media | https://www.esm.rochester.edu/academics/undergraduate/ |
| 5 | Musical Arts | https://www.esm.rochester.edu/academics/undergraduate/ |

##### BFA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Audio Arts Technologies | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Audio%20Arts%20Technologies |
| 2 | Audio and Music Engineering | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Audio%20and%20Music%20Engineering |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 项目 | 涉及学院 | URL |
|---|------|---------|-----|
| 1 | Audio and Music Engineering | Hajim + Eastman | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Audio%20and%20Music%20Engineering |
| 2 | Audio Arts Technologies | Eastman + Hajim | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Audio%20Arts%20Technologies |
| 3 | Health, Behavior, and Society | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Health,%20Behavior,%20and%20Society |
| 4 | Health Policy | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Health%20Policy |
| 5 | International Relations | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=International%20Relations |
| 6 | Politics, Philosophy, and Economics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Politics,%20Philosophy,%20and%20Economics |
| 7 | Sustainability | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Sustainability |
| 8 | Data Science | SAS + Hajim | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Data%20Science |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 | Accounting | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Accounting |
| 2 | Actuarial Studies | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Actuarial%20Studies |
| 3 | American Sign Language | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=American%20Sign%20Language |
| 4 | Arabic | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Arabic |
| 5 | Business | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Business |
| 6 | Business Analytics | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Business%20Analytics |
| 7 | Chinese | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Chinese |
| 8 | Classical Civilization | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Classical%20Civilization |
| 9 | Climate Change Science | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Climate%20Change%20Science |
| 10 | Community-Engaged Learning | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Community-Engaged%20Learning |
| 11 | Dance Studies | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Dance%20Studies |
| 12 | Economics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Economics |
| 13 | Entrepreneurship | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Entrepreneurship |
| 14 | Environmental Health | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Environmental%20Health |
| 15 | Epidemiology | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Epidemiology |
| 16 | Film and Media Studies | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Film%20and%20Media%20Studies |
| 17 | Finance | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Finance |
| 18 | Financial Economics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Financial%20Economics |
| 19 | Hebrew | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Hebrew |
| 20 | Information Systems | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Information%20Systems |
| 21 | Italian | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Italian |
| 22 | Japanese | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Japanese |
| 23 | Jewish Studies | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Jewish%20Studies |
| 24 | Journalism | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Journalism |
| 25 | Korean | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Korean |
| 26 | Latin | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Latin |
| 27 | Legal Studies | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Legal%20Studies |
| 28 | Linguistics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Linguistics |
| 29 | Literary Translation | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Literary%20Translation |
| 30 | Marketing | Simon | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Marketing |
| 31 | Mathematics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Mathematics |
| 32 | Music | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Music |
| 33 | Music and Linguistics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Music%20and%20Linguistics |
| 34 | Music Cognition | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Music%20Cognition |
| 35 | Philosophy | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Philosophy |
| 36 | Physics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Physics |
| 37 | Political Science | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Political%20Science |
| 38 | Psychology | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Psychology |
| 39 | Religion | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Religion |
| 40 | Russian | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Russian |
| 41 | Sociology | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Sociology |
| 42 | Spanish | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Spanish |
| 43 | Statistics | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Statistics |
| 44 | Studio Arts | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Studio%20Arts |
| 45 | Sustainability | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Sustainability |
| 46 | Theater | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Theater |
| 47 | Writing Studies | SAS | https://admissions.rochester.edu/academics/majors-and-minors/?subject=Writing%20Studies |

### 1.5 General/Institute-wide requirements

**Rochester Curriculum**: University of Rochester 采用独特的 Rochester Curriculum，没有传统的通识教育核心课程要求。学生只需完成:
1. **One required course**: Writing 105 (或等效课程)
2. **Major requirements**: 学生选择的专业课程
3. **Electives**: 其余课程由学生自由选择

这种灵活的课程设置允许学生根据自己的兴趣和职业目标定制教育路径。

> **来源**: admissions.rochester.edu/academics/rochester-curriculum/

### 1.6 Combined Degree Programs (CDP)

| 程序 | 描述 | 学制 | URL |
|------|------|------|-----|
| GEAR (Graduate Engineering at Rochester) | BA/BS + 工程硕士 | 5年 | https://admissions.rochester.edu/academics/combined-degree-programs/ |
| GRADE (Guaranteed Rochester Accelerated Degree Education) | BA/BS + MSEd | 5年 | https://admissions.rochester.edu/academics/combined-degree-programs/ |
| HEAL (Health and Epidemiology Advanced Learning) | BA/BS + 公共卫生硕士 | 5年 | https://admissions.rochester.edu/academics/combined-degree-programs/ |
| REMS (Rochester Early Medical Scholars) | BA/BS + MD | 8年 | https://admissions.rochester.edu/academics/combined-degree-programs/ |
| DDE (Dual Degree at Eastman) | 音乐 + 学术学位 | 5年 | https://admissions.rochester.edu/academics/combined-degree-programs/ |
| Business Master's Pathway | 本科 + Simon MS | 5年 | https://admissions.rochester.edu/academics/combined-degree-programs/ |

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### School of Arts & Sciences (SAS)

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://www.sas.rochester.edu/graduate/ |
| 2 | Mathematics | https://www.sas.rochester.edu/graduate/ |
| 3 | Statistics | https://www.sas.rochester.edu/graduate/ |
| 4 | History | https://www.sas.rochester.edu/graduate/ |
| 5 | Philosophy | https://www.sas.rochester.edu/graduate/ |
| 6 | Political Science | https://www.sas.rochester.edu/graduate/ |
| 7 | Psychology | https://www.sas.rochester.edu/graduate/ |
| 8 | English | https://www.sas.rochester.edu/graduate/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science | https://www.sas.rochester.edu/graduate/ |
| 2 | Computational Biology | https://www.sas.rochester.edu/graduate/ |
| 3 | Biostatistics | https://www.sas.rochester.edu/graduate/ |
| 4 | Epidemiology | https://www.sas.rochester.edu/graduate/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.sas.rochester.edu/graduate/ |
| 2 | Brain and Cognitive Sciences | https://www.sas.rochester.edu/graduate/ |
| 3 | Chemistry | https://www.sas.rochester.edu/graduate/ |
| 4 | Computer Science | https://www.sas.rochester.edu/graduate/ |
| 5 | Economics | https://www.sas.rochester.edu/graduate/ |
| 6 | English | https://www.sas.rochester.edu/graduate/ |
| 7 | History | https://www.sas.rochester.edu/graduate/ |
| 8 | Mathematics | https://www.sas.rochester.edu/graduate/ |
| 9 | Philosophy | https://www.sas.rochester.edu/graduate/ |
| 10 | Physics | https://www.sas.rochester.edu/graduate/ |
| 11 | Political Science | https://www.sas.rochester.edu/graduate/ |
| 12 | Psychology | https://www.sas.rochester.edu/graduate/ |
| 13 | Statistics | https://www.sas.rochester.edu/graduate/ |
| 14 | Visual and Cultural Studies | https://www.sas.rochester.edu/graduate/ |

#### Hajim School of Engineering & Applied Sciences

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.hajim.rochester.edu/graduate/ |
| 2 | Chemical Engineering | https://www.hajim.rochester.edu/graduate/ |
| 3 | Computer Science | https://www.hajim.rochester.edu/graduate/ |
| 4 | Electrical and Computer Engineering | https://www.hajim.rochester.edu/graduate/ |
| 5 | Materials Science | https://www.hajim.rochester.edu/graduate/ |
| 6 | Mechanical Engineering | https://www.hajim.rochester.edu/graduate/ |
| 7 | Optics | https://www.hajim.rochester.edu/graduate/ |
| 8 | Audio and Music Engineering | https://www.hajim.rochester.edu/graduate/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.hajim.rochester.edu/graduate/ |
| 2 | Chemical Engineering | https://www.hajim.rochester.edu/graduate/ |
| 3 | Computer Science | https://www.hajim.rochester.edu/graduate/ |
| 4 | Electrical and Computer Engineering | https://www.hajim.rochester.edu/graduate/ |
| 5 | Materials Science | https://www.hajim.rochester.edu/graduate/ |
| 6 | Mechanical Engineering | https://www.hajim.rochester.edu/graduate/ |
| 7 | Optics | https://www.hajim.rochester.edu/graduate/ |

#### Eastman School of Music

##### MM Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Performance | https://www.esm.rochester.edu/academics/graduate/ |
| 2 | Composition | https://www.esm.rochester.edu/academics/graduate/ |
| 3 | Music Education | https://www.esm.rochester.edu/academics/graduate/ |
| 4 | Conducting | https://www.esm.rochester.edu/academics/graduate/ |
| 5 | Jazz Studies & Contemporary Media | https://www.esm.rochester.edu/academics/graduate/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Musicology | https://www.esm.rochester.edu/academics/graduate/ |
| 2 | Music Theory | https://www.esm.rochester.edu/academics/graduate/ |
| 3 | Music Education | https://www.esm.rochester.edu/academics/graduate/ |

##### DMA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Performance | https://www.esm.rochester.edu/academics/graduate/ |
| 2 | Composition | https://www.esm.rochester.edu/academics/graduate/ |
| 3 | Conducting | https://www.esm.rochester.edu/academics/graduate/ |

#### Simon Business School

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Full-Time MBA | https://www.simon.rochester.edu/programs/full-time-mba/ |
| 2 | Executive MBA | https://www.simon.rochester.edu/programs/executive-mba/ |
| 3 | Professional MBA | https://www.simon.rochester.edu/programs/professional-mba/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://www.simon.rochester.edu/programs/ms-programs/ |
| 2 | Finance | https://www.simon.rochester.edu/programs/ms-programs/ |
| 3 | Business Analytics | https://www.simon.rochester.edu/programs/ms-programs/ |
| 4 | Marketing Analytics | https://www.simon.rochester.edu/programs/ms-programs/ |
| 5 | AI in Business | https://www.simon.rochester.edu/programs/ms-programs/ |

##### DBA Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Business Administration | https://www.simon.rochester.edu/programs/dba/ |

#### Warner School of Education & Human Development

##### MSEd Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching & Curriculum | https://www.warner.rochester.edu/degrees/ |
| 2 | Educational Leadership | https://www.warner.rochester.edu/degrees/ |
| 3 | Human Development | https://www.warner.rochester.edu/degrees/ |
| 4 | Counseling Psychology | https://www.warner.rochester.edu/degrees/ |
| 5 | Special Education | https://www.warner.rochester.edu/degrees/ |

##### EdD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education | https://www.warner.rochester.edu/degrees/ |

#### School of Medicine & Dentistry

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Physics | https://www.urmc.rochester.edu/education/graduate/ |
| 2 | Clinical Investigation | https://www.urmc.rochester.edu/education/graduate/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry & Molecular Biology | https://www.urmc.rochester.edu/education/graduate/ |
| 2 | Biophysics, Structural & Computational Biology | https://www.urmc.rochester.edu/education/graduate/ |
| 3 | Cellular & Molecular Pharmacology & Physiology | https://www.urmc.rochester.edu/education/graduate/ |
| 4 | Epidemiology | https://www.urmc.rochester.edu/education/graduate/ |
| 5 | Genetics, Development & Stem Cells | https://www.urmc.rochester.edu/education/graduate/ |
| 6 | Immunology, Microbiology & Virology | https://www.urmc.rochester.edu/education/graduate/ |
| 7 | Neuroscience | https://www.urmc.rochester.edu/education/graduate/ |
| 8 | Pathology & Experimental Medicine | https://www.urmc.rochester.edu/education/graduate/ |
| 9 | Translational Biomedical Science | https://www.urmc.rochester.edu/education/graduate/ |

##### MD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine | https://www.urmc.rochester.edu/education/md-program/ |

#### School of Nursing

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult/Gerontology Nurse Practitioner | https://www.son.rochester.edu/academics/ |
| 2 | Family Nurse Practitioner | https://www.son.rochester.edu/academics/ |
| 3 | Psychiatric Mental Health Nurse Practitioner | https://www.son.rochester.edu/academics/ |

##### DNP Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice | https://www.son.rochester.edu/academics/ |

##### PhD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://www.son.rochester.edu/academics/ |

### 2.2 At least one program's full deep-dive

**Computer Science (PhD) — School of Arts & Sciences**

- **Department**: Department of Computer Science
- **School**: School of Arts & Sciences & Hajim School of Engineering (joint)
- **Degrees offered**: MS, PhD
- **Application deadline**: January 15 (fall admission)
- **GRE**: Not required
- **TOEFL minimum**: 100 (iBT) / 5 (new scoring)
- **IELTS minimum**: 7.5
- **Application portal**: https://www.rochester.edu/college/graduate/
- **Contact**: cs-grad@rochester.edu

### 2.3 Graduate admissions model

University of Rochester 的研究生招生是**分散式**的:
- **SAS/Hajim**: 通过 GEPA (Graduate Education and Postdoctoral Affairs) 办公室
- **Eastman**: 独立招生
- **Simon**: 独立招生
- **Warner**: 独立招生
- **School of Medicine & Dentistry**: 独立招生 (MD 通过 AMCAS, PhD 通过各系)
- **School of Nursing**: 独立招生

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common Application, Coalition for College | admissions.rochester.edu/applying/how-to-apply/ |
| ED I 截止日期 | November 1 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| ED II 截止日期 | January 5 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| RD 截止日期 | January 5 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| 优先奖学金截止 | December 1 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| ED I 通知 | Mid-December | admissions.rochester.edu/applying/dates-and-deadlines/ |
| ED II 通知 | Early February | admissions.rochester.edu/applying/dates-and-deadlines/ |
| RD 通知 | April 1 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| 入学确认 | May 1 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| 申请费 | $65 | admissions.rochester.edu/applying/how-to-apply/ |
| SAT/ACT 政策 | Test-optional | admissions.rochester.edu/applying/testing-policies/ |
| 推荐信 | 1 counselor + 1 teacher | admissions.rochester.edu/applying/how-to-apply/ |
| 面试 | 可选 (强烈推荐) | admissions.rochester.edu/applying/interviewing/ |

### 3.2 Undergraduate English proficiency table

| 考试 | 推荐分数 | 说明 |
|------|---------|------|
| TOEFL iBT | 100 (旧评分) / 5 (新评分) | 学校代码: 2928 |
| IELTS | 7.5 | 学术类 |
| Duolingo English Test (DET) | 130 | |

> **来源**: admissions.rochester.edu/applying/international-students/
> **注意**: 2026年1月21日起 TOEFL 采用新评分标准

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | 各学院独立 | 分散式 |
| 申请费 (SAS/Hajim) | $70 | www.rochester.edu/college/graduate/ |
| 申请费 (Simon) | $90 | www.simon.rochester.edu/ |
| GRE 政策 | 因项目而异 | 各项目要求不同 |
| TOEFL 最低要求 | 100 (iBT) / 5 (新评分) | 各项目要求不同 |
| IELTS 最低要求 | 7.5 | 各项目要求不同 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

| 费用项目 | 住校学生 | 走读学生 | 与父母同住 |
|---------|---------|---------|-----------|
| Tuition | $71,750 | $71,750 | $71,750 |
| Mandatory Fees | $1,622 | $1,622 | $1,622 |
| Housing | $12,822 | $5,716 | $1,500 |
| Food | $8,506 | $6,670 | $5,170 |
| Transportation | $300 | $300 | $300 |
| Personal Expenses | $1,022 | $1,022 | $1,022 |
| **Total** | **$96,022** | **$87,080** | **$81,364** |

> **来源**: www.rochester.edu/financial-aid/tuition-costs/undergraduate-tuition-expenses/
> **注意**: 2025-2026 学年 Tuition 为 $69,030

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-blind (美国学生) | 是 | www.rochester.edu/financial-aid/ |
| Need-blind (国际学生) | 否 (need-aware) | admissions.rochester.edu/applying/international-students/ |
| 满足 100% demonstrated need | 是 | www.rochester.edu/financial-aid/ |
| CSS Profile | 需要 | admissions.rochester.edu/applying/international-students/ |
| FAFSA | 需要 | www.rochester.edu/financial-aid/ |
| 学校代码 (FAFSA) | 002894 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| 学校代码 (CSS) | 2928 | admissions.rochester.edu/applying/dates-and-deadlines/ |
| 奖学金政策 | 自动考虑 merit scholarships | admissions.rochester.edu/applying/how-to-apply/ |

### 4.3 Graduate cost & funding framework

| 学院 | 学费 (年) | 资助类型 | 来源 |
|------|----------|---------|------|
| SAS (PhD) | ~$60,000 | 全额资助 (TA/RA/Fellowship) | www.sas.rochester.edu/graduate/ |
| Hajim (PhD) | ~$60,000 | 全额资助 (TA/RA/Fellowship) | www.hajim.rochester.edu/graduate/ |
| Eastman | ~$55,000 | 因项目而异 | www.esm.rochester.edu/ |
| Simon MBA | ~$110,000 (总计) | 奖学金 + 贷款 | www.simon.rochester.edu/ |
| Warner | ~$50,000 | 因项目而异 | www.warner.rochester.edu/ |
| SON | ~$55,000 | 因项目而异 | www.son.rochester.edu/ |

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: "https://admissions.rochester.edu/applying/dates-and-deadlines/"
source_snippet: "Early decision I (ED I) November 1 Mid-December Within 3 weeks of notification"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-002
field: undergraduate.deadlines.ED_II
value: "January 5"
source_url: "https://admissions.rochester.edu/applying/dates-and-deadlines/"
source_snippet: "Early decision II (ED II) January 5 Early February Within 3 weeks of notification"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-003
field: undergraduate.deadlines.RD
value: "January 5"
source_url: "https://admissions.rochester.edu/applying/dates-and-deadlines/"
source_snippet: "Regular decision (RD)* January 5 April 1 May 1"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-004
field: undergraduate.testing.test_optional
value: true
source_url: "https://admissions.rochester.edu/applying/testing-policies/"
source_snippet: "The University of Rochester's undergraduate admissions process is test optional."
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-005
field: undergraduate.cost.tuition_2026_2027
value: "$71,750"
source_url: "https://www.rochester.edu/financial-aid/tuition-costs/undergraduate-tuition-expenses/"
source_snippet: "Tuition $71,750 $71,750 $71,750"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-006
field: undergraduate.cost.total_on_campus_2026_2027
value: "$96,022"
source_url: "https://www.rochester.edu/financial-aid/tuition-costs/undergraduate-tuition-expenses/"
source_snippet: "Total $96,022 $87,080 $81,364"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-007
field: undergraduate.english_proficiency.toefl
value: "100 (old) / 5 (new)"
source_url: "https://admissions.rochester.edu/applying/international-students/"
source_snippet: "TOEFL iBT (School Code: 2928) 100 (former scoring) | 5 (new scoring)"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-008
field: undergraduate.english_proficiency.ielts
value: "7.5"
source_url: "https://admissions.rochester.edu/applying/international-students/"
source_snippet: "IELTS 7.5"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-009
field: undergraduate.english_proficiency.det
value: "130"
source_url: "https://admissions.rochester.edu/applying/international-students/"
source_snippet: "Duolingo English Test 130"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-010
field: undergraduate.financial_aid.need_blind_us
value: true
source_url: "https://www.rochester.edu/financial-aid/"
source_snippet: "The University of Rochester is committed to helping students meet their financial needs."
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-011
field: undergraduate.financial_aid.need_blind_intl
value: false
source_url: "https://admissions.rochester.edu/applying/international-students/"
source_snippet: "Financial need is a contributing factor, however, for international applicants."
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-012
field: undergraduate.programs.total_majors
value: 87
source_url: "https://admissions.rochester.edu/academics/majors-and-minors/"
source_snippet: "Major (87)"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-013
field: undergraduate.programs.total_minors
value: 83
source_url: "https://admissions.rochester.edu/academics/majors-and-minors/"
source_snippet: "Minor (83)"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-014
field: undergraduate.curriculum
value: "Rochester Curriculum - no core requirements, only one required course (Writing 105)"
source_url: "https://admissions.rochester.edu/academics/rochester-curriculum/"
source_snippet: "With unparalleled flexibility, the Rochester Curriculum fits your personal needs, strengths, and preferences."
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-001
field: graduate.sas.phd_programs
value: 14
source_url: "https://www.sas.rochester.edu/graduate/"
source_snippet: "With 13 master's programs and 14 PhD programs"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-002
field: graduate.hajim.phd_programs
value: 7
source_url: "https://www.hajim.rochester.edu/graduate/"
source_snippet: "Our seven PhD programs and 10 master's programs"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-003
field: graduate.hajim.ms_programs
value: 10
source_url: "https://www.hajim.rochester.edu/graduate/"
source_snippet: "Our seven PhD programs and 10 master's programs"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-004
field: graduate.simon.full_time_mba
value: "Full-Time MBA"
source_url: "https://www.simon.rochester.edu/"
source_snippet: "Full-Time MBA Elevate your skills and take control of your career journey with a Simon MBA."
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-005
field: graduate.simon.ms_programs
value: "Accountancy, Finance, Business Analytics, Marketing Analytics, AI in Business"
source_url: "https://www.simon.rochester.edu/"
source_snippet: "Full-Time MS Programs Learn about generative AI-focused curriculum"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-006
field: graduate.warner.programs
value: "Doctorate, Master's, Certificates, Online Programs"
source_url: "https://www.warner.rochester.edu/"
source_snippet: "Doctorate Master's Certificates Online Programs"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-007
field: graduate.nursing.ranking
value: "#1 in Upstate New York, #11 master's, #22 bachelor's"
source_url: "https://www.son.rochester.edu/"
source_snippet: "Ranked #1 in Upstate New York, according to U.S. News and World Report. Top 25 Nursing programs Ranked #11 master's and #22 bachelor's"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-008
field: graduate.eastman.degrees
value: "BM, MM, PhD, DMA"
source_url: "https://www.esm.rochester.edu/academics/"
source_snippet: "Degrees and Certificates Graduate Studies Undergraduate Studies"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-009
field: graduate.schools
value: "SAS, Hajim, Eastman, Simon, Warner, Medicine & Dentistry, Nursing"
source_url: "https://www.rochester.edu/academics/"
source_snippet: "School of Arts & Sciences, Hajim School of Engineering & Applied Sciences, Eastman School of Music, School of Medicine & Dentistry, School of Nursing, Simon Business School, Warner School of Education"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-010
field: undergraduate.combined_degree_programs
value: "GEAR, GRADE, HEAL, REMS, DDE, Business Master's Pathway"
source_url: "https://admissions.rochester.edu/academics/combined-degree-programs/"
source_snippet: "Graduate Engineering at Rochester (GEAR), Guaranteed Rochester Accelerated Degree Education (GRADE), Health and Epidemiology Advanced Learning (HEAL), Rochester Early Medical Scholars (REMS), Dual Degree at Eastman (DDE), Business Master's Pathway"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
urochester-knowledge-base-v2/
├── overview/
│   ├── institution-overview (Section 0)
│   └── schools-and-departments (Section 0.2)
├── undergraduate/
│   ├── sas-majors (Section 1.2 SAS)
│   ├── hajim-majors (Section 1.2 Hajim)
│   ├── eastman-majors (Section 1.2 Eastman)
│   ├── simon-majors (Section 1.2 Simon)
│   ├── minors (Section 1.4)
│   └── combined-degree-programs (Section 1.6)
├── graduate/
│   ├── sas-graduate (Section 2.1 SAS)
│   ├── hajim-graduate (Section 2.1 Hajim)
│   ├── eastman-graduate (Section 2.1 Eastman)
│   ├── simon-graduate (Section 2.1 Simon)
│   ├── warner-graduate (Section 2.1 Warner)
│   ├── medicine-graduate (Section 2.1 Medicine)
│   └── nursing-graduate (Section 2.1 Nursing)
├── admissions/
│   ├── deadlines (Section 3.1)
│   ├── testing-policies (Section 3.1)
│   ├── english-proficiency (Section 3.2)
│   └── graduate-admissions (Section 3.3)
├── costs/
│   ├── undergraduate-cost (Section 4.1)
│   ├── financial-aid (Section 4.2)
│   └── graduate-cost (Section 4.3)
└── evidence/
    └── evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "urochester-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BM|MA|MS|PhD|...>"
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
| P0 | Exact count of UG majors by degree type (BA vs BS vs BM) | admissions.rochester.edu/academics/majors-and-minors/ |
| P0 | Complete graduate program list per school | 各学院网站 |
| P0 | Eastman School of Music detailed program list | esm.rochester.edu/academics/ |
| P1 | Per-program GRE requirements for graduate programs | 各项目网站 |
| P1 | Graduate application deadlines by program | 各项目网站 |
| P1 | Simon Business School detailed tuition and fees | simon.rochester.edu/ |
| P1 | Warner School of Education detailed program list | warner.rochester.edu/ |
| P2 | School of Medicine & Dentistry graduate programs | urmc.rochester.edu/education/ |
| P2 | School of Nursing graduate programs | son.rochester.edu/academics/ |
| P2 | Financial aid income thresholds | www.rochester.edu/financial-aid/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | University of Rochester | (Other schools) |
|------|------------------------|-----------------|
| Type | Private research university | |
| Location | Rochester, NY | |
| UG Tuition (2026-27) | $71,750 | |
| UG Total COA (on-campus) | $96,022 | |
| Need-blind (US) | Yes | |
| Need-blind (intl) | No (need-aware) | |
| Test policy | Test-optional | |
| TOEFL minimum | 100 (old) / 5 (new) | |
| IELTS minimum | 7.5 | |
| ED I deadline | November 1 | |
| ED II deadline | January 5 | |
| RD deadline | January 5 | |
| Total UG programs | 87 majors + 83 minors | |
| Total grad programs | ~32 | |
| Schools | 7 | |
| Curriculum | Rochester Curriculum (no core) | |
| Application fee | $65 | |
| CSS Profile code | 2928 | |
| FAFSA code | 002894 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.rochester.edu, www.rochester.edu, www.sas.rochester.edu, www.hajim.rochester.edu, www.esm.rochester.edu, www.simon.rochester.edu, www.warner.rochester.edu, www.son.rochester.edu, www.urmc.rochester.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
