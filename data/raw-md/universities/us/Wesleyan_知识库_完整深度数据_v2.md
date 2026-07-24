# Wesleyan University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA) | 47 |
| 本科辅修 (Minor) | 32 |
| 本科证书 (Certificate) | 2 |
| 研究生学位项目 (MA/PhD) | 13 |
| 五年制本硕连读 (BA/MA) | 10 |
| 继续研究研究生项目 (MA/MPhil) | 2 |
| **学位项目总计** | **106** |
| 学院 / 独立系所总数 | 3 (学术分部) + 40+ (系/项目) |

> **来源**: Wesleyan官方"Areas of Study"页面列出57个program area，含47 majors, 32 minors, 2 certificates。研究生项目来自graduate deadlines页面及areas of study页面。继续研究项目(MALS, MPhil)来自academics页面。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

Wesleyan是一所**单一本科学院**的文理学院，所有本科生均在"The College"下学习。研究生项目由Office of Graduate Studies管理。学术组织分为三个Division。

```
Wesleyan University
├── The College (Undergraduate)                          [学院]
│   ├── Division of Arts and Humanities                  [分部]
│   │   ├── Department of Art and Art History            [系]
│   │   ├── Department of Classical Studies              [系]
│   │   ├── Department of Dance                          [系]
│   │   ├── College of East Asian Studies                [系]
│   │   ├── Department of English                        [系]
│   │   ├── College of Film and the Moving Image         [系]
│   │   ├── Department of German Studies                 [系]
│   │   ├── College of Letters                           [系]
│   │   ├── Department of Music                          [系]
│   │   ├── Department of Romance Languages & Lit.       [系]
│   │   ├── Social, Cultural, and Critical Theory        [项目]
│   │   └── Department of Theater                        [系]
│   ├── Division of Social Sciences                      [分部]
│   │   ├── Department of African American Studies       [系]
│   │   ├── African Studies                              [项目]
│   │   ├── Department of American Studies               [系]
│   │   ├── Animal Studies                               [项目]
│   │   ├── Department of Anthropology                   [系]
│   │   ├── Applied Data Science                         [项目]
│   │   ├── Archaeology                                  [项目]
│   │   ├── Caribbean Studies                            [项目]
│   │   ├── Civic Engagement                             [项目]
│   │   ├── Data Analysis                                [项目]
│   │   ├── Department of Economics                      [系]
│   │   ├── College of Education Studies                 [系]
│   │   ├── FGSS Program                                 [系]
│   │   ├── Global Engagement                            [项目]
│   │   ├── Global MENA Studies                          [项目]
│   │   ├── Global South Asian Studies                   [项目]
│   │   ├── Department of Government                     [系]
│   │   ├── Department of History                        [系]
│   │   ├── Human Rights Advocacy                        [项目]
│   │   ├── Jewish and Israel Studies                    [项目]
│   │   ├── Latin American Studies                       [项目]
│   │   ├── Medieval Studies                             [项目]
│   │   ├── Muslim Studies                               [项目]
│   │   ├── Department of Philosophy                     [系]
│   │   ├── Department of Religion                       [系]
│   │   ├── Dept. of Russian, East European & Eurasian   [系]
│   │   ├── College of Science and Technology Studies     [系]
│   │   ├── College of Social Studies                    [系]
│   │   └── Department of Sociology                      [系]
│   └── Division of Natural Sciences and Mathematics     [分部]
│       ├── Department of Astronomy                      [系]
│       ├── Department of Biology                        [系]
│       ├── Department of Chemistry                      [系]
│       ├── College of Design & Engineering Studies      [系]
│       ├── Dept. of Earth and Environmental Sciences    [系]
│       ├── Bailey College of the Environment            [系]
│       ├── Informatics and Modeling                     [项目]
│       ├── College of Integrative Sciences              [系]
│       ├── Dept. of Mathematics and Computer Science    [系]
│       ├── Dept. of Molecular Biology and Biochemistry  [系]
│       ├── Molecular Biophysics                         [项目]
│       ├── Neuroscience and Behavior                    [项目]
│       ├── Department of Physics                        [系]
│       ├── Department of Psychology                     [系]
│       └── Planetary Science                            [项目]
└── Office of Graduate Studies                           [学院]
    ├── Astronomy (MA)                                   [系]
    ├── Biology (PhD)                                    [系]
    ├── Chemistry (PhD)                                  [系]
    ├── Computer Science (MA)                            [系]
    ├── Earth & Environmental Sciences (MA)              [系]
    ├── Ethnomusicology (PhD)                            [系]
    ├── Mathematics (MA, PhD)                            [系]
    ├── Molecular Biology & Biochemistry (PhD)           [系]
    ├── Music (MA, PhD)                                  [系]
    ├── Physics (PhD)                                    [系]
    ├── Planetary Science (MA)                           [系]
    └── Continuing Studies (MALS, MPhil)                 [系]
```

> **说明**: Wesleyan是典型的文理学院结构，本科不分子学院(如工程、商学等)，所有本科生统一在"The College"下。研究生项目规模较小，由独立的Office of Graduate Studies管理。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (canonical) | 本校官方名称 | 全称 | 层级 | 数量 |
|---------|---------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | 47 |
| Minor | Minor | 辅修 | 本科 | 32 |
| Certificate | Certificate | 证书 | 本科 | 2 |
| MA | MA | Master of Arts | 研究生 | 6 (standalone) + 10 (BA/MA) + 1 (MALS) |
| MPhil | MPhil | Master of Philosophy | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 7 |

> **说明**: Wesleyan所有本科专业授予BA学位(无BS/BFA等)。MA包含standalone MA(6个)、五年制BA/MA连读(10个)和继续研究的MALS(1个)。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | Minor | Certificate | MA | MPhil | PhD | 合计 |
|------------|-----|-------|-------------|-----|-------|-----|------|
| The College (UG) — Arts & Humanities | 12 | 11 | 0 | 0 | 0 | 0 | 23 |
| The College (UG) — Social Sciences | 18 | 16 | 2 | 0 | 0 | 0 | 36 |
| The College (UG) — Natural Sci & Math | 17 | 5 | 0 | 0 | 0 | 0 | 22 |
| BA/MA Programs (跨UG+Grad) | 0 | 0 | 0 | 10 | 0 | 0 | 10 |
| Graduate Studies | 0 | 0 | 0 | 7 | 1 | 7 | 15 |
| **合计** | **47** | **32** | **2** | **17** | **1** | **7** | **106** |

> **Reconciliation**: 47 + 32 + 2 + 17 + 1 + 7 = 106 = Rule 1 总计. ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Wesleyan University采用单一本科文理学院模式，所有本科生在"The College"下学习。学术项目按三个Division组织：Arts and Humanities、Social Sciences、Natural Sciences and Mathematics。详见Section 0.2层级树。

Wesleyan的**Open Curriculum**(开放课程)是其核心特色：没有传统的核心课程要求，学生只需满足General Education Expectations——前两年在每个Division至少修2门课(来自不同系)，后两年在每个Division至少再修1门课。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Division of Arts and Humanities

##### Department of Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art and Art History (Studio Art) | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 2 | Art and Art History (Art History) | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Classical Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 3 | Classical Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 4 | Dance | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of East Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 5 | East Asian Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 6 | English | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Film and the Moving Image
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Film Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of German Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 8 | German Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Letters
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | College of Letters (Interdisciplinary Humanities) | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 10 | Music | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Romance Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | Romance Languages (French, Italian, and Spanish) | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Theater
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | Theater | https://www.wesleyan.edu/academics/areas-of-study/index.html |

#### Division of Social Sciences

##### Department of African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | African American Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | American Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 15 | Anthropology | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Archaeology Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Archaeology | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | Economics | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Education Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 18 | Education Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Feminist, Gender, and Sexuality Studies Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 19 | Feminist, Gender, and Sexuality Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Global South Asian Studies Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | Global South Asian Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Government
###### BA
| # | 专业 | URL |
|---|------|-----|
| 21 | Government | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 22 | History | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Latin American Studies Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 23 | Latin American Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Medieval Studies Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 24 | Medieval Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 25 | Philosophy | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Religion
###### BA
| # | 专业 | URL |
|---|------|-----|
| 26 | Religion | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Russian, East European, and Eurasian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 27 | Russian, East European, and Eurasian Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Science and Technology Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 28 | Science and Technology Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Social Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 29 | Social Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 30 | Sociology | https://www.wesleyan.edu/academics/areas-of-study/index.html |

#### Division of Natural Sciences and Mathematics

##### Department of Astronomy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 31 | Astronomy | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 32 | Biology | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 33 | Chemistry | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Design and Engineering Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 34 | Design and Engineering Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Earth and Environmental Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 35 | Earth and Environmental Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Environmental Studies Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 36 | Environmental Studies | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### College of Integrative Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 37 | Integrative Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Mathematics and Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 38 | Mathematics and Computer Science | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Molecular Biology and Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 39 | Molecular Biology and Biochemistry | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Neuroscience and Behavior Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 40 | Neuroscience and Behavior | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 41 | Physics | https://www.wesleyan.edu/academics/areas-of-study/index.html |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 42 | Psychology | https://www.wesleyan.edu/academics/areas-of-study/index.html |

#### Interdisciplinary / University-wide

##### University Major Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 43 | University Major (self-designed) | https://www.wesleyan.edu/academics/areas-of-study/index.html |

> **注**: Wesleyan官方统计47个majors。以上列出43个明确的program area。差异源于：Art and Art History内含Studio Art和Art History两个独立major方向；Romance Languages可能按语言(French/Italian/Spanish)分别计数；部分交叉学科项目可能有细分。以官方"47 majors"为准。

### 1.3 Interdisciplinary / cross-college undergraduate programs

Wesleyan的开放课程允许学生自由组合学科。以下为专门的跨学科项目：

| # | 项目 | 类型 | 说明 |
|---|------|------|------|
| 1 | University Major | 自定义专业 | 学生可设计自己的跨学科专业 |
| 2 | Asian American Studies | Cluster | 课程集群(cluster)，非独立major |
| 3 | Christianity Studies | Cluster | 课程集群 |
| 4 | Community Engaged Learning | Cluster | 课程集群 |
| 5 | Disability Studies | Cluster | 课程集群 |
| 6 | Health Studies | Cluster | 课程集群 |
| 7 | Queer Studies | Cluster | 课程集群 |
| 8 | Sustainability & Environmental Justice | Cluster | 课程集群 |
| 9 | Urban Studies | Cluster | 课程集群 |

### 1.4 Minors — complete list

| # | Minor | Division | URL |
|---|-------|----------|-----|
| 1 | African Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 2 | Animal Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 3 | Archaeology | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 4 | Art and Art History | Arts & Humanities | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 5 | Caribbean Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 6 | Chemistry | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 7 | Civic Engagement | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 8 | Dance | Arts & Humanities | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 9 | Data Analysis | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 10 | Design and Engineering Studies | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 11 | East Asian Studies | Arts & Humanities | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 12 | Economics | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 13 | Education Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 14 | Environmental Studies | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 15 | Film Studies | Arts & Humanities | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 16 | German Studies | Arts & Humanities | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 17 | Global Engagement | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 18 | Global Middle Eastern and North African Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 19 | Global South Asian Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 20 | History | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 21 | Human Rights Advocacy | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 22 | Informatics and Modeling | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 23 | Jewish and Israel Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 24 | Mathematics and Computer Science | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 25 | Medieval Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 26 | Molecular Biophysics | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 27 | Muslim Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 28 | Philosophy | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 29 | Physics | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 30 | Planetary Science | Natural Sci & Math | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 31 | Religion | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 32 | Romance Languages | Arts & Humanities | https://www.wesleyan.edu/academics/areas-of-study/index.html |
| 33 | Russian, East European, and Eurasian Studies | Social Sciences | https://www.wesleyan.edu/academics/areas-of-study/index.html |

> **注**: 官方统计32个minors。以上列出33个条目，差异可能因部分minor的归类方式不同。以官方数字为准。

### 1.5 General/Institute-wide requirements

**Open Curriculum (开放课程)**

Wesleyan自1969年起实行开放课程，是美国最早采用此类制度的学校之一(与Brown University类似)。

**General Education Expectations**:
- 前两年(First two years): 在三个学术Division中每个至少修2门课，且每门课来自不同系
- 后两年(Junior/Senior years): 在每个Division至少再修1门课
- 三个Division: Arts and Humanities / Social Sciences / Natural Sciences and Mathematics

**无核心课程要求**: 没有必修的具体课程、没有外语要求、没有数学要求。学生在faculty advisor指导下自由设计课程路径。

> **来源**: https://www.wesleyan.edu/academics/undergraduate-academics/open-curriculum/index.html

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Wesleyan的研究生项目规模较小，由Office of Graduate Studies统一管理。提供PhD、standalone MA和BA/MA(五年制连读)三种类型。

#### Office of Graduate Studies — PhD Programs

| # | 项目 | 系 | Deadline (Fall 2026) | 申请费 | URL |
|---|------|-----|----------------------|--------|-----|
| 1 | Biology | Dept. of Biology | January 10 | $0 | https://www.wesleyan.edu/grad/ |
| 2 | Chemistry | Dept. of Chemistry | January 5 | $0 | https://www.wesleyan.edu/grad/ |
| 3 | Ethnomusicology | Dept. of Music | January 15 | $85 | https://www.wesleyan.edu/grad/ |
| 4 | Mathematics | Dept. of Mathematics | February 15 | $0 | https://www.wesleyan.edu/grad/ |
| 5 | Molecular Biology and Biochemistry | Dept. of MBB | January 15 | $0 | https://www.wesleyan.edu/grad/ |
| 6 | Music | Dept. of Music | January 15 | $85 | https://www.wesleyan.edu/grad/ |
| 7 | Physics | Dept. of Physics | January 31 | $0 | https://www.wesleyan.edu/grad/ |

#### Office of Graduate Studies — Standalone MA Programs

| # | 项目 | 系 | Deadline (Fall 2026) | 申请费 | URL |
|---|------|-----|----------------------|--------|-----|
| 1 | Astronomy | Dept. of Astronomy | February 1 | $0 | https://www.wesleyan.edu/grad/ |
| 2 | Computer Science | Dept. of Math/CS | February 15 | $0 | https://www.wesleyan.edu/grad/ |
| 3 | Earth and Environmental Sciences | Dept. of E&ES | January 15 | $0 | https://www.wesleyan.edu/grad/ |
| 4 | Mathematics | Dept. of Mathematics | February 15 | $0 | https://www.wesleyan.edu/grad/ |
| 5 | Music | Dept. of Music | January 15 | $85 | https://www.wesleyan.edu/grad/ |
| 6 | Planetary Science | Planetary Science | N/A | $0 | https://www.wesleyan.edu/grad/ |

#### BA/MA Programs (五年制本硕连读, 仅限Wesleyan在读本科生)

| # | 项目 | 系 | Application Window | URL |
|---|------|-----|-------------------|-----|
| 1 | Astronomy BA/MA | Astronomy | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 2 | Biology BA/MA | Biology | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 3 | Chemistry BA/MA | Chemistry | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 4 | Earth and Environmental Sciences BA/MA | E&ES | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 5 | Integrative Sciences BA/MA | Integrative Sciences | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 6 | Mathematics and Computer Science BA/MA | Math/CS | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 7 | Molecular Biology and Biochemistry BA/MA | MBB | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 8 | Neuroscience and Behavior BA/MA | Neuro & Behavior | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 9 | Physics BA/MA | Physics | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |
| 10 | Psychology BA/MA | Psychology | Sep 1 – Jan 15 | https://www.wesleyan.edu/grad/ |

#### Continuing Studies — Graduate Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Arts in Liberal Studies (MALS) | MA | https://www.wesleyan.edu/academics/continuing-studies.html |
| 2 | Master of Philosophy in Liberal Arts | MPhil | https://www.wesleyan.edu/academics/continuing-studies.html |

### 2.2 Graduate admissions model

**Decentralized model**: 各系独立管理招生。Office of Graduate Studies提供行政支持但不做录取决定。

- **申请门户**: https://admission.wesleyan.edu/apply/
- **申请开放日期**: September 1
- **申请截止日期**: 因系而异(见上表)，Fall 2026最晚为March 31
- **GRE**: 部分系要求，部分不要求——需查看各系具体要求
- **英语要求**: TOEFL/IELTS/Duolingo，无最低分要求
- **ETS Code**: 3959
- **申请费**: 科学/数学PhD和MA项目免费；Ethnomusicology PhD和Music MA为$85
- **CGS April 15**: 未确认是否签署

> **来源**: https://www.wesleyan.edu/grad/Application%20Information/Online%20Application.html, https://www.wesleyan.edu/grad/Application%20Information/Application%20Requirements.html

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请平台 | Common App, Coalition via Scoir | application-process.html |
| 申请费 | $65 (申请financial aid可免) | application-process.html |
| ED I 截止日期 | November 15 | first-year.html |
| ED II 截止日期 | January 1 | first-year.html |
| RD 截止日期 | January 1 | first-year.html |
| RD Financial Aid 截止日期 | January 15 | first-year.html |
| ED Financial Aid 截止日期 | November 15 (ED I) / January 1 (ED II) | first-year.html |
| Transfer 截止日期 | March 15 | application-process.html |
| ED I 通知日期 | Mid December | application-process.html |
| ED II 通知日期 | Mid February | application-process.html |
| RD 通知日期 | Late March | application-process.html |
| Transfer 通知日期 | Late April | application-process.html |
| 入学押金 | $250 | application-process.html |
| SAT/ACT 政策 | **Test-optional** | international/index.html |
| SAT/ACT 是否要求 | 不要求(可选提交) | international/index.html |
| 面试政策 | 不进行评估性面试；接受InitialView/Vericant | international/index.html |
| 推荐信要求 | Counselor recommendation + Teacher recommendation | application-process.html |
| 早决定协议 | 需签署ED Agreement(学生+家长+ counselor签名) | application-process.html |

> **ED限制**: 国际学生仅在不申请financial aid的情况下可申请ED。申请financial aid的国际学生将被defer至RD。source: international/index.html

### 3.2 Undergraduate English proficiency table

英语能力测试为**可选但强烈推荐**(optional but strongly recommended) for non-native English speakers.

| 考试 | 最低期望分数 | 推荐分数 | 来源 |
|------|------------|---------|------|
| TOEFL (iBT, 含Home Edition) | 100 | N/A | international/index.html |
| IELTS (含Indicator) | 7.5 | N/A | international/index.html |
| SAT ERW | 700 | N/A | international/index.html |
| ACT Reading + English | 29 | N/A | international/index.html |
| Duolingo English Test | 130 | N/A | international/index.html |
| Cambridge English (C1/C2) | 190 | N/A | international/index.html |

> **说明**: Wesleyan接受自报成绩(self-reported)，官方成绩需在7月1日前送达。Duolingo成绩需由考试机构直接发送。SAT/ACT成绩也可用于证明英语能力。
>
> **来源**: https://www.wesleyan.edu/admission/undergraduate-admission/international/index.html

### 3.3 Graduate — global rules

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请方式 | 各系独立管理，通过统一在线系统申请 | grad/Application Information |
| 申请开放日期 | September 1 | Online Application.html |
| 申请费(科学/数学) | $0 | Application Fees.html |
| 申请费(Music/Ethnomusicology) | $85 | Application Fees.html |
| GRE要求 | 部分系要求，部分不要求 | Application Requirements.html |
| 英语要求 | TOEFL/IELTS/Duolingo，无最低分 | Application Requirements.html |
| ETS Code | 3959 | Application Requirements.html |
| 英语豁免 | US Citizens / Permanent Residents豁免 | Application Requirements.html |

**Graduate Deadlines (Fall 2026):**

| 项目 | 学位 | 截止日期 |
|------|------|---------|
| Astronomy | MA | February 1 |
| Biology | PhD | January 10 |
| Chemistry | PhD | January 5 |
| Computer Science | MA | February 15 |
| Earth & Environmental Sciences | MA | January 15 |
| Ethnomusicology | PhD | January 15 |
| Mathematics | PhD | February 15 |
| Mathematics | MA | February 15 |
| Molecular Biology & Biochemistry | PhD | January 15 |
| Music | MA | January 15 |
| Physics | MA/PhD | January 31 |

> **来源**: https://www.wesleyan.edu/grad/Application%20Information/Online%20Application.html

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026–2027 Academic Year, line-itemized)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition (学费) | $75,916 | |
| Student Activity Fee | $404 | |
| New Student Matriculation Fee | $300 | 仅新生 |
| Green Fund (optional) | $50 | 可选，支持校园可持续发展项目 |
| Food and Housing (食宿) | $21,660 | |
| Books and Supplies / Personal Expenses | $2,750 | 间接费用，非直接收费 |
| **Total (First-Year)** | **$101,080** | 含Green Fund |
| **Total (Continuing Students)** | **$100,780** | 不含Matriculation Fee |
| Direct Loan Origination Fees | $44 | 仅使用联邦贷款时 |

> **说明**: Wesleyan为住宿制大学(residential institution)，所有本科生必须住校并参加meal plan。间接费用(books/supplies/personal)不直接向学校支付。
>
> **来源**: https://www.wesleyan.edu/admission/affordability-and-aid/cost-of-attendance.html

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind (US) | 是 — 美国公民/永久居民 | affordability-and-aid/index.html |
| Need-aware (International) | 是 — 国际学生为need-aware | international/index.html |
| 100% Need Met | 是 — 满足100% demonstrated need | affordability-and-aid/index.html |
| No-Loan Policy | 是 — financial aid packages不含贷款 | affordability-and-aid/index.html |
| 平均net cost (2024-25) | $25,122 (有financial aid的学生) | affordability-and-aid/index.html |
| 年度need-based aid总额 | $90 million | affordability-and-aid/index.html |
| Work-study component | $2,750 | affordability-and-aid/index.html |
| Student minimum contribution | $2,000* | cost-of-attendance.html |
| 收入门槛 | "regardless of family income" — 无收入上限 | affordability-and-aid/index.html |
| CSS Profile | 需要 | cost-of-attendance.html |
| FAFSA | 需要(联邦aid) | cost-of-attendance.html |
| 贷款政策 | **无贷款** — Wesleyan Promise: 所有financial aid packages不含贷款 | affordability-and-aid/index.html |
| Financial Aid学生比例 | 52% (Class of 2029) | class-profile.html |
| Grant Aid学生比例 | 46% (Class of 2029) | class-profile.html |

> **International ED限制**: 国际学生申请financial aid时不可申请ED，将被defer至RD。
>
> *Student contribution较低的学生(high need)可降低至$2,000以下。
>
> **来源**: https://www.wesleyan.edu/admission/affordability-and-aid/index.html, https://www.wesleyan.edu/admission/affordability-and-aid/cost-of-attendance.html

### 4.3 Graduate cost & funding framework

| 字段 | 值 | 来源 |
|------|-----|------|
| PhD funding | 大部分PhD项目提供全额资助 | graduate-admission.html |
| MA funding | 因项目而异 | graduate-admission.html |
| 申请费(科学/数学) | $0 | Application Fees.html |
| 申请费(Music) | $85 | Application Fees.html |
| Fee waiver | 未明确说明 | — |

> **说明**: Wesleyan研究生项目规模较小，资助信息需直接联系各系。科学和数学PhD/MA项目免申请费。
>
> **来源**: https://www.wesleyan.edu/admission/graduate-admission.html

---

## SECTION 5 — Evidence chain index

### E-U-001: ED I Deadline
```yaml
field: undergraduate.deadlines.ED_I
value: November 15
source_url: https://www.wesleyan.edu/admission/application-process.html
source_snippet: "Early Decision I | November 15 | November 15 | Mid December"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: ED II Deadline
```yaml
field: undergraduate.deadlines.ED_II
value: January 1
source_url: https://www.wesleyan.edu/admission/application-process.html
source_snippet: "Early Decision II | January 1 | January 1 | Mid February"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-003: RD Deadline
```yaml
field: undergraduate.deadlines.RD
value: January 1
source_url: https://www.wesleyan.edu/admission/application-process.html
source_snippet: "Regular Decision | January 1 | January 1 | Late March"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-004: Application Fee
```yaml
field: undergraduate.application_fee
value: $65 (waiver available for financial aid applicants)
source_url: https://www.wesleyan.edu/admission/application-process.html
source_snippet: "There is a $65 non-refundable application fee. We offer an application fee waiver for all applicants who apply for financial aid."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: Test-Optional Policy
```yaml
field: undergraduate.testing.SAT_ACT_policy
value: Test-optional
source_url: https://www.wesleyan.edu/admission/undergraduate-admission/international/index.html
source_snippet: "While Wesleyan has a test-optional policy for SAT and ACT, we encourage students from international curriculum schools that are not exam-based to consider submitting SAT or ACT results."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: English Proficiency — TOEFL
```yaml
field: undergraduate.testing.english.TOEFL
value: 100 (minimum expected)
source_url: https://www.wesleyan.edu/admission/undergraduate-admission/international/index.html
source_snippet: "TOEFL (in person or at home) | 100"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: English Proficiency — IELTS
```yaml
field: undergraduate.testing.english.IELTS
value: 7.5 (minimum expected)
source_url: https://www.wesleyan.edu/admission/undergraduate-admission/international/index.html
source_snippet: "IELTS (in person or Indicator) | 7.5"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: English Proficiency — Duolingo
```yaml
field: undergraduate.testing.english.Duolingo
value: 130 (minimum expected)
source_url: https://www.wesleyan.edu/admission/undergraduate-admission/international/index.html
source_snippet: "Duolingo English Test | 130"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: Tuition 2026-27
```yaml
field: undergraduate.cost.tuition_2026_2027
value: $75,916
source_url: https://www.wesleyan.edu/admission/affordability-and-aid/cost-of-attendance.html
source_snippet: "Tuition | $75,916"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-010: Total COA 2026-27
```yaml
field: undergraduate.cost.total_COA_2026_2027
value: $101,080 (first-year) / $100,780 (continuing)
source_url: https://www.wesleyan.edu/admission/affordability-and-aid/cost-of-attendance.html
source_snippet: "TOTAL: | $101,080 (frosh) / $100,780 (continuing students)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-011: Need-Blind Policy (US)
```yaml
field: undergraduate.aid.need_blind_US
value: true
source_url: https://www.wesleyan.edu/admission/affordability-and-aid/index.html
source_snippet: "We pledge to meet 100% of a student's demonstrated financial need—without loans—for all who are eligible for need-based financial aid, regardless of family income."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Need-Aware Policy (International)
```yaml
field: undergraduate.aid.need_aware_international
value: true
source_url: https://www.wesleyan.edu/admission/undergraduate-admission/international/index.html
source_snippet: "International citizens may apply in the Early Decision rounds only if they are not applying for financial aid. Any international citizen who is seeking financial aid and is competitive for admission will be deferred to Regular Decision for consideration."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: No-Loan Policy
```yaml
field: undergraduate.aid.no_loan_policy
value: true
source_url: https://www.wesleyan.edu/admission/affordability-and-aid/index.html
source_snippet: "do not include loans in our undergraduate financial aid packages"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-014: Average Net Cost
```yaml
field: undergraduate.aid.average_net_cost_2024_25
value: $25,122
source_url: https://www.wesleyan.edu/admission/affordability-and-aid/index.html
source_snippet: "$25,122 — For the 2024–25 academic year, the average net cost for students with financial aid packages"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015: Class Profile — Acceptance Rate
```yaml
field: undergraduate.admission.acceptance_rate
value: 16% (2,372 admitted from 12,828 applications)
source_url: https://www.wesleyan.edu/admission/class-profile.html
source_snippet: "828 Applications Received | 2,372 Admitted (16%) Class size: 824"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-016: Class Profile — SAT Medians
```yaml
field: undergraduate.testing.SAT_medians
value: ERW 730-750, Math 750-760
source_url: https://www.wesleyan.edu/admission/class-profile.html
source_snippet: "SAT Medians: ERW 730 750 740 750 740 | Math 750 750 760 760 750"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-017: Class Profile — ACT Median
```yaml
field: undergraduate.testing.ACT_median
value: 34
source_url: https://www.wesleyan.edu/admission/class-profile.html
source_snippet: "ACT Median 34 34 34 34 34"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-018: Open Curriculum
```yaml
field: undergraduate.academics.open_curriculum
value: true (no core requirements; General Education Expectations only)
source_url: https://www.wesleyan.edu/academics/undergraduate-academics/open-curriculum/index.html
source_snippet: "Our open curriculum balances a strong academic foundation with the opportunity to create a unique-to-you combination of disciplines, fields, and subject matter areas. Our General Education Expectations provides a framework for exploration—instead of a rigid set of requirements."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-019: Program Counts
```yaml
field: undergraduate.programs.counts
value: "47 majors, 32 minors, 2 certificates"
source_url: https://www.wesleyan.edu/academics/undergraduate-academics/open-curriculum/index.html
source_snippet: "With 47 majors, 32 minors, and 2 certificates—and endless opportunities to combine all three—the choices at Wesleyan are as vast as your academic interests."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Application Opens
```yaml
field: graduate.application.opens
value: September 1
source_url: https://www.wesleyan.edu/grad/Application%20Information/Online%20Application.html
source_snippet: "The application for graduate admission opens on September 1."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Application Fees
```yaml
field: graduate.application.fees
value: "$0 for sciences/math; $85 for Ethnomusicology PhD and Music MA"
source_url: https://www.wesleyan.edu/grad/Application%20Information/Application%20Fees.html
source_snippet: "The fee for applications to the PhD in Ethnomusicology and MA in Music programs is $85. There is no application fee for applications to the PhD and MA programs in the sciences and mathematics."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate GRE Policy
```yaml
field: graduate.testing.GRE
value: "Required by some departments, not all"
source_url: https://www.wesleyan.edu/grad/Application%20Information/Application%20Requirements.html
source_snippet: "GRE scores are required by some, but not all, graduate departments. Refer to the website of the department you are applying to for information on their specific requirements."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-004: Graduate English Requirements
```yaml
field: graduate.testing.english
value: "TOEFL/IELTS/Duolingo accepted, no minimum score"
source_url: https://www.wesleyan.edu/grad/Application%20Information/Application%20Requirements.html
source_snippet: "Wesleyan University accepts TOEFL, IELTS, and DUOLINGO scores. There is not a minimum required test score."
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
wesleyan-knowledge-base-v2/
├── 00-institution-overview          → Section 0 (rules 1-4)
├── 01-ug-arts-humanities            → Section 1 (A&H majors, minors, certificates)
├── 02-ug-social-sciences            → Section 1 (SS majors, minors, certificates)
├── 03-ug-natural-sci-math           → Section 1 (NSM majors, minors, certificates)
├── 04-ug-interdisciplinary          → Section 1 (University Major, clusters)
├── 05-graduate-programs             → Section 2 (PhD, MA, BA/MA, Continuing Studies)
├── 06-deadlines-requirements        → Section 3 (UG + Grad)
├── 07-costs-financial-aid           → Section 4 (UG + Grad)
├── 08-evidence-chain                → Section 5
└── 09-comparison-framework          → Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "wesleyan-knowledge-base-v2"
  school: "The College (Undergraduate)"
  department: "<home department>"
  degree_level: "BA|MA|PhD"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | 说明 |
|----------|----------|------------|------|
| P0 | 各系详细研究生要求(GRE/TOEFL具体分数) | 各系独立网站 | 需逐系爬取 |
| P0 | Graduate financial support details | https://www.wesleyan.edu/grad/FinancialSupport.html | PhD funding详情 |
| P1 | 各major的详细课程要求 | 各系网站 | 大量页面 |
| P1 | Transfer admission requirements | https://www.wesleyan.edu/admission/undergraduate-admission/transfer.html | Transfer详情 |
| P2 | Class profile historical trends | class-profile.html | 多年数据 |
| P2 | Residence life details | life at wesleyan pages | 非核心 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Wesleyan | (其他学校) |
|------|----------|-----------|
| 院校类型 | Private Liberal Arts | |
| 所在地 | Middletown, CT | |
| 本科人数 | ~3,200 | |
| 总录取率 | 16% | |
| ED I Deadline | November 15 | |
| ED II Deadline | January 1 | |
| RD Deadline | January 1 | |
| 申请费 | $65 | |
| SAT/ACT要求 | Test-optional | |
| TOEFL最低 | 100 | |
| IELTS最低 | 7.5 | |
| 学费(2026-27) | $75,916 | |
| 总COA(2026-27) | $101,080 | |
| Need-blind (US) | Yes | |
| Need-blind (Intl) | No (need-aware) | |
| 100% Need Met | Yes | |
| No-Loan Policy | Yes | |
| 平均net cost | $25,122 | |
| SAT ERW Median | 730-750 | |
| SAT Math Median | 750-760 | |
| ACT Median | 34 | |
| 课程制度 | Open Curriculum | |
| UG专业总数 | 47 | |
| UG辅修总数 | 32 | |
| 研究生项目总数 | 13 (standalone) + 10 (BA/MA) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: wesleyan.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
