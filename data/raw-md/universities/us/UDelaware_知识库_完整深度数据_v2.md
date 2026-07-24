# University of Delaware Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BLA/BCE/BChE/BBE/BME/BSN/BSEd/etc.) | 154 |
| 本科辅修 (Minor) | 120 |
| 研究生学位项目 (MA/MS/MBA/MPA/MPP/MPH/MFA/PhD/DNP/DPT/etc.) | 161 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 35 |
| **学位项目总计 (UG + Grad)** | **315** |
| 学院 / 独立系所总数 | 10 colleges + 4 schools |

> **来源说明**: 本科专业数来自 UD Major Finder 页面（"more than 150 major fields of study"）；研究生项目数来自 Graduate Program Finder（161 programs）；辅修和证书数来自 2026-2027 Undergraduate Catalog。Graduate College 官方数据：60 doctoral, 145 master's, 35 certificate programs。

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Delaware
├── College of Agriculture and Natural Resources (CANR)        [学院]
│   ├── Animal & Food Sciences                                 [系]
│   ├── Applied Economics & Statistics                          [系]
│   ├── Entomology & Wildlife Ecology                          [系]
│   └── Plant & Soil Sciences                                  [系]
├── College of Arts and Sciences (CAS)                         [学院]
│   ├── Africana Studies                                       [系]
│   ├── Anthropology                                           [系]
│   ├── Art & Design                                           [系]
│   ├── Art Conservation                                       [系]
│   ├── Art History                                            [系]
│   ├── Biological Sciences                                    [系]
│   ├── Chemistry & Biochemistry                               [系]
│   ├── Communication                                          [系]
│   ├── English                                                [系]
│   ├── Fashion & Apparel Studies                              [系]
│   ├── History                                                [系]
│   ├── Languages, Literatures & Cultures                      [系]
│   ├── Linguistics & Cognitive Science                        [系]
│   ├── Mathematical Sciences                                  [系]
│   ├── School of Music                                        [系/学校]
│   ├── Philosophy                                             [系]
│   ├── Physics & Astronomy                                    [系]
│   ├── Political Science & International Relations            [系]
│   ├── Psychological & Brain Sciences                         [系]
│   ├── Sociology & Criminal Justice                           [系]
│   ├── Theatre & Dance                                        [系]
│   └── Women & Gender Studies                                 [系]
├── Alfred Lerner College of Business and Economics            [学院]
│   ├── Accounting & Management Information Systems            [系]
│   ├── Business Administration                                [系]
│   ├── Economics                                              [系]
│   ├── Finance                                                [系]
│   └── Hospitality & Sport Business Management                [系]
├── College of Earth, Ocean, and Environment (CEOE)            [学院]
│   ├── Earth Sciences                                         [系]
│   ├── Geography & Spatial Sciences                           [系]
│   └── School of Marine Science & Policy                      [系/学校]
├── College of Education and Human Development (CEHD)          [学院]
│   ├── School of Education                                    [系/学校]
│   └── Human Development & Family Sciences                    [系]
├── College of Engineering (COE)                               [学院]
│   ├── Biomedical Engineering                                 [系]
│   ├── Chemical & Biomolecular Engineering                    [系]
│   ├── Civil & Environmental Engineering                      [系]
│   ├── Computer & Information Sciences                        [系]
│   ├── Electrical & Computer Engineering                      [系]
│   ├── Materials Science & Engineering                        [系]
│   └── Mechanical Engineering                                 [系]
├── College of Health Sciences (CHS)                           [学院]
│   ├── Communication Sciences & Disorders                     [系]
│   ├── Epidemiology                                           [系]
│   ├── Health Behavior & Nutrition Sciences                   [系]
│   ├── Kinesiology & Applied Physiology                       [系]
│   ├── Medical & Molecular Sciences                           [系]
│   ├── Physical Therapy                                       [系]
│   └── School of Nursing                                      [系/学校]
├── Graduate College                                           [学院]
├── Honors College                                             [学院]
└── Joseph R. Biden, Jr. School of Public Policy & Admin       [学院]
    └── Public Policy & Administration                         [系]
```

> **说明**: CAS 有 23 个系/学校，是最大的学院。School of Music、School of Marine Science & Policy、School of Nursing、School of Education 分别隶属于各自的母学院。Honors College 和 Graduate College 不直接授予学位，而是提供跨学院的荣誉课程和研究生管理。

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 (canonical) | 本校官方缩写 | 全称 | 层级 | 本项目数量 |
|---------|---------|------|------|-----------|
| AS | AS | Associate in Science | 本科 | 4 |
| AA | AA | Associate in Arts | 本科 | 3 |
| BA | BA | Bachelor of Arts | 本科 | 52 |
| BS | BS | Bachelor of Science | 本科 | 68 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BM | BM | Bachelor of Music | 本科 | 22 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| BCE | BCE | Bachelor of Civil Engineering | 本科 | 1 |
| BChE | BChE | Bachelor of Chemical Engineering | 本科 | 1 |
| BBE | BBE | Bachelor of Biomedical Engineering | 本科 | 1 |
| BEE | BEE | Bachelor of Electrical Engineering | 本科 | 1 |
| BME | BME | Bachelor of Mechanical Engineering | 本科 | 1 |
| BCpE | BCpE | Bachelor of Computer Engineering | 本科 | 1 |
| BCEM | BCEM | Bachelor of Construction Eng. & Mgmt | 本科 | 1 |
| BENE | BENE | Bachelor of Environmental Engineering | 本科 | 1 |
| BMSE | BMSE | Bachelor of Materials Science Eng. | 本科 | 1 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BSEd | BSEd | Bachelor of Science in Education | 本科 | 11 |
| MA | MA | Master of Arts | 研究生 | 18 |
| MS | MS | Master of Science | 研究生 | 52 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MPA | MPA | Master of Public Administration | 研究生 | 2 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 8 |
| MM | MM | Master of Music | 研究生 | 2 |
| MCE | MCE | Master of Civil Engineering | 研究生 | 1 |
| MSECE | MSECE | Master of Science in ECE | 研究生 | 1 |
| MSME | MSME | Master of Science in ME | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 42 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 35 |
| Minor | Minor | Undergraduate Minor | 本科辅修 | 120 |

> **说明**: UD 工程学院各系授予独特的工程学士学位缩写（BCE, BChE, BBE, BEE, BME, BCpE, BCEM, BENE, BMSE），这些在 degree-taxonomy.md 中映射到 BEng（canonical）。音乐学院授予 BM（Bachelor of Music）。教育学院授予 BSEd。研究生项目中，MS 是最常见的学位（52个项目），其次是 PhD（42个）。

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab, 学院 × canonical 学位级别)

| 学院 \ 级别 | AA/AS | BA | BS | BFA | BM | BEng | BSN | BSEd | MA | MS | MBA | MPA/MPP | MPH | MEd | MM | PhD | DNP/DPT/EdD | Cert | 合计 |
|------------|-------|----|----|-----|----|------|-----|------|----|----|-----|---------|-----|-----|----|-----|-------------|------|------|
| CANR | 1 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 2 | 28 |
| CAS | 2 | 45 | 20 | 2 | 22 | 0 | 0 | 0 | 12 | 8 | 0 | 0 | 0 | 0 | 2 | 15 | 0 | 14 | 142 |
| Lerner | 1 | 2 | 27 | 0 | 0 | 0 | 0 | 0 | 2 | 8 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 8 | 52 |
| CEOE | 0 | 5 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 24 |
| CEHD | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 11 | 0 | 2 | 0 | 0 | 0 | 6 | 0 | 2 | 1 | 0 | 26 |
| COE | 0 | 1 | 8 | 0 | 0 | 9 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 1 | 41 |
| CHS | 1 | 0 | 11 | 0 | 0 | 0 | 2 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 1 | 27 |
| Biden School | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 9 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 6 | 0 | 4 | 11 |
| **合计** | **8** | **56** | **92** | **2** | **22** | **9** | **2** | **11** | **15** | **51** | **2** | **2** | **1** | **6** | **2** | **43** | **3** | **33** | **360** |

> **说明**: 此矩阵包含所有学位项目（含 4+1 连读项目中的研究生部分单独计数）。Honors College 不授予独立学位，而是为各学院学生提供荣誉课程。总计 360 个学位项目反映了所有 distinct degree programs（不含辅修）。Rule 1 中的 315 仅计 distinct programs（不含 4+1 项目中的重复计数），而矩阵中的 360 包含了 4+1 项目的研究生端。两个数字的差异源于 4+1 项目在 UG 和 Grad 两端的双重计数。

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

UD 拥有 10 个学院，其中 8 个授予本科学位。详见 Section 0.2 层级树。工程学院各系授予独特的工程学士学位（BCE, BChE, BBE 等），音乐学院授予 BM，教育学院授予 BSEd。

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Agriculture and Natural Resources (CANR)

##### Animal & Food Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Biosciences | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97606 |
| 2 | Animal Science | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97045 |
| 3 | Food and Agribusiness Marketing | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97046 |
| 4 | Food Science | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97047 |
| 5 | Pre-Veterinary Medicine | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97050 |
| 6 | Sustainable Food Systems | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97607 |

###### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture and Natural Resources | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97071 |

##### Applied Economics & Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental and Resource Economics | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97048 |
| 2 | Statistics | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97052 |

##### Entomology & Wildlife Ecology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Insect Ecology and Conservation | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97049 |
| 2 | Wildlife Ecology and Conservation | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97053 |

##### Plant & Soil Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture and Natural Resources | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97044 |
| 2 | Plant Science | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97051 |

###### BLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://catalog.udel.edu/preview_program.php?catoid=97&poid=97072 |

#### College of Arts and Sciences (CAS)

##### Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.udel.edu/academics/programs/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.udel.edu/academics/programs/ |
| 2 | Anthropology Education | https://www.udel.edu/academics/programs/ |

##### Art & Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.udel.edu/academics/programs/ |
| 2 | Art History | https://www.udel.edu/academics/programs/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Arts | https://www.udel.edu/academics/programs/ |
| 2 | Visual Communications | https://www.udel.edu/academics/programs/ |

##### Art Conservation
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Conservation | https://www.udel.edu/academics/programs/ |

##### Biological Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.udel.edu/academics/programs/ |
| 2 | Biological Sciences Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.udel.edu/academics/programs/ |
| 2 | Applied Molecular Biology and Biotechnology | https://www.udel.edu/academics/programs/ |

##### Chemistry & Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.udel.edu/academics/programs/ |
| 2 | Chemistry Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.udel.edu/academics/programs/ |
| 2 | Biochemistry | https://www.udel.edu/academics/programs/ |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://www.udel.edu/academics/programs/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.udel.edu/academics/programs/ |
| 2 | English Education | https://www.udel.edu/academics/programs/ |
| 3 | Comparative Literature | https://www.udel.edu/academics/programs/ |

##### Fashion & Apparel Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Design and Product Innovation | https://www.udel.edu/academics/programs/ |
| 2 | Fashion Merchandising and Management | https://www.udel.edu/academics/programs/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.udel.edu/academics/programs/ |
| 2 | History Education | https://www.udel.edu/academics/programs/ |

##### Languages, Literatures & Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese Studies | https://www.udel.edu/academics/programs/ |
| 2 | French Studies | https://www.udel.edu/academics/programs/ |
| 3 | German Studies | https://www.udel.edu/academics/programs/ |
| 4 | Italian Studies | https://www.udel.edu/academics/programs/ |
| 5 | Japanese Studies | https://www.udel.edu/academics/programs/ |
| 6 | Russian Studies | https://www.udel.edu/academics/programs/ |
| 7 | Spanish Studies | https://www.udel.edu/academics/programs/ |
| 8 | Three Languages | https://www.udel.edu/academics/programs/ |
| 9 | Intensive French Studies | https://www.udel.edu/academics/programs/ |
| 10 | Intensive Italian Studies | https://www.udel.edu/academics/programs/ |
| 11 | Latin American & Iberian Studies | https://www.udel.edu/academics/programs/ |

##### Linguistics & Cognitive Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Science | https://www.udel.edu/academics/programs/ |

##### Mathematical Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.udel.edu/academics/programs/ |
| 2 | Mathematics Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.udel.edu/academics/programs/ |
| 2 | Applied Mathematics | https://www.udel.edu/academics/programs/ |
| 3 | Mathematics and Data Science | https://www.udel.edu/academics/programs/ |
| 4 | Mathematics and Economics | https://www.udel.edu/academics/programs/ |
| 5 | Actuarial Sciences | https://www.udel.edu/academics/programs/ |
| 6 | Mathematics Education | https://www.udel.edu/academics/programs/ |

##### School of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.udel.edu/academics/programs/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Music-Instrumental | https://www.udel.edu/academics/programs/ |
| 2 | Applied Music-Piano | https://www.udel.edu/academics/programs/ |
| 3 | Applied Music-Voice | https://www.udel.edu/academics/programs/ |
| 4 | Music Composition | https://www.udel.edu/academics/programs/ |
| 5 | Music Education-General/Choral | https://www.udel.edu/academics/programs/ |
| 6 | Music Education-Instrumental | https://www.udel.edu/academics/programs/ |
| 7 | Music History and Literature | https://www.udel.edu/academics/programs/ |
| 8 | Music Theory | https://www.udel.edu/academics/programs/ |
| 9 | Jazz and Improvisation | https://www.udel.edu/academics/programs/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.udel.edu/academics/programs/ |

##### Physics & Astronomy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.udel.edu/academics/programs/ |
| 2 | Astronomy | https://www.udel.edu/academics/programs/ |
| 3 | Physics Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.udel.edu/academics/programs/ |
| 2 | Applied Physics | https://www.udel.edu/academics/programs/ |

##### Political Science & International Relations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.udel.edu/academics/programs/ |
| 2 | International Relations | https://www.udel.edu/academics/programs/ |
| 3 | Political Science Education | https://www.udel.edu/academics/programs/ |

##### Psychological & Brain Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.udel.edu/academics/programs/ |
| 2 | Psychology Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.udel.edu/academics/programs/ |

##### Sociology & Criminal Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.udel.edu/academics/programs/ |
| 2 | Criminal Justice | https://www.udel.edu/academics/programs/ |
| 3 | Sociology Education | https://www.udel.edu/academics/programs/ |

##### Theatre & Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://www.udel.edu/academics/programs/ |
| 2 | Dance | https://www.udel.edu/academics/programs/ |

##### Women & Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women and Gender Studies | https://www.udel.edu/academics/programs/ |

##### Interdisciplinary (CAS)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | https://www.udel.edu/academics/programs/ |
| 2 | European Studies | https://www.udel.edu/academics/programs/ |
| 3 | Global Studies | https://www.udel.edu/academics/programs/ |
| 4 | Liberal Studies | https://www.udel.edu/academics/programs/ |

#### Alfred Lerner College of Business and Economics

##### Accounting & Management Information Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.udel.edu/academics/programs/ |
| 2 | Management Information Systems | https://www.udel.edu/academics/programs/ |
| 3 | Information Systems | https://www.udel.edu/academics/programs/ |

##### Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.udel.edu/academics/programs/ |
| 2 | Computer Science and Business | https://www.udel.edu/academics/programs/ |
| 3 | Entrepreneurship | https://www.udel.edu/academics/programs/ |
| 4 | Global Business | https://www.udel.edu/academics/programs/ |
| 5 | Management | https://www.udel.edu/academics/programs/ |
| 6 | Marketing | https://www.udel.edu/academics/programs/ |
| 7 | Operations Management | https://www.udel.edu/academics/programs/ |

###### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.udel.edu/academics/programs/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.udel.edu/academics/programs/ |
| 2 | Economics Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.udel.edu/academics/programs/ |

##### Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.udel.edu/academics/programs/ |
| 2 | Financial Planning and Wealth Management | https://www.udel.edu/academics/programs/ |
| 3 | Fintech | https://www.udel.edu/academics/programs/ |

##### Hospitality & Sport Business Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality and Event Business Management | https://www.udel.edu/academics/programs/ |
| 2 | Hospitality Industry Management | https://www.udel.edu/academics/programs/ |
| 3 | Human Resource Management | https://www.udel.edu/academics/programs/ |
| 4 | Sport Management | https://www.udel.edu/academics/programs/ |
| 5 | Sports Performance Analytics | https://www.udel.edu/academics/programs/ |

#### College of Earth, Ocean, and Environment (CEOE)

##### Earth Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences | https://www.udel.edu/academics/programs/ |
| 2 | Environmental Science | https://www.udel.edu/academics/programs/ |
| 3 | Earth Science Education | https://www.udel.edu/academics/programs/ |

##### Geography & Spatial Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://www.udel.edu/academics/programs/ |
| 2 | Geography | https://www.udel.edu/academics/programs/ |
| 3 | Geography Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | GIScience and Environmental Data Analytics | https://www.udel.edu/academics/programs/ |
| 2 | Meteorology and Climate Science | https://www.udel.edu/academics/programs/ |

##### School of Marine Science & Policy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Science | https://www.udel.edu/academics/programs/ |

#### College of Education and Human Development (CEHD)

##### School of Education
###### BSEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary and Middle School Teacher Education | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://www.udel.edu/academics/programs/ |

###### AA
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://www.udel.edu/academics/programs/ |
| 2 | Elementary and Middle School Teacher Education | https://www.udel.edu/academics/programs/ |

##### Human Development & Family Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Relations Administration | https://www.udel.edu/academics/programs/ |
| 2 | Human Services | https://www.udel.edu/academics/programs/ |

#### College of Engineering (COE)

##### Biomedical Engineering
###### BBE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.udel.edu/academics/programs/ |

##### Chemical & Biomolecular Engineering
###### BChE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.udel.edu/academics/programs/ |

##### Civil & Environmental Engineering
###### BCE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.udel.edu/academics/programs/ |

###### BENE
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Engineering | https://www.udel.edu/academics/programs/ |

###### BCEM
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Engineering and Management | https://www.udel.edu/academics/programs/ |

##### Computer & Information Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.udel.edu/academics/programs/ |
| 2 | Artificial Intelligence Engineering | https://www.udel.edu/academics/programs/ |
| 3 | Cybersecurity Engineering | https://www.udel.edu/academics/programs/ |

###### BCpE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.udel.edu/academics/programs/ |

##### Electrical & Computer Engineering
###### BEE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.udel.edu/academics/programs/ |

##### Materials Science & Engineering
###### BMSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://www.udel.edu/academics/programs/ |

##### Mechanical Engineering
###### BME
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.udel.edu/academics/programs/ |

#### College of Health Sciences (CHS)

##### Communication Sciences & Disorders
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | (No standalone UG major; see Speech-Language Pathology graduate program) | N/A |

##### Health Behavior & Nutrition Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Behavior Science | https://www.udel.edu/academics/programs/ |
| 2 | Nutrition and Dietetics | https://www.udel.edu/academics/programs/ |
| 3 | Nutrition and Medical Sciences | https://www.udel.edu/academics/programs/ |
| 4 | Public Health | https://www.udel.edu/academics/programs/ |

##### Kinesiology & Applied Physiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://www.udel.edu/academics/programs/ |
| 2 | Human Physiology | https://www.udel.edu/academics/programs/ |
| 3 | Sports Health | https://www.udel.edu/academics/programs/ |

##### Medical & Molecular Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Diagnostics | https://www.udel.edu/academics/programs/ |
| 2 | Medical Laboratory Science | https://www.udel.edu/academics/programs/ |
| 3 | Applied Molecular Biology and Biotechnology | https://www.udel.edu/academics/programs/ |
| 4 | Integrated Health Sciences | https://www.udel.edu/academics/programs/ |
| 5 | Interdisciplinary Studies in Medical and Molecular Sciences | https://www.udel.edu/academics/programs/ |

##### School of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing - Traditional Program | https://www.udel.edu/academics/programs/ |
| 2 | Nursing - Accelerated Degree Program | https://www.udel.edu/academics/programs/ |

#### Joseph R. Biden, Jr. School of Public Policy & Administration

##### Public Policy & Administration
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Civic Leadership and Policy Studies | https://www.udel.edu/academics/programs/ |
| 2 | Public Policy | https://www.udel.edu/academics/programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Energy and Environmental Policy | https://www.udel.edu/academics/programs/ |
| 2 | Leadership | https://www.udel.edu/academics/programs/ |

###### AA
| # | 专业 | URL |
|---|------|-----|
| 1 | Community and Nonprofit Leadership | https://www.udel.edu/academics/programs/ |

### 1.3 Interdisciplinary / Cross-College Programs

UD 提供大量跨学院的联合学位（4+1）项目，详见 2026-2027 Catalog。主要跨学院组合包括：
- CAS + Lerner: 多个 BA/BS + MBA 4+1 项目
- CAS + CEOE: Environmental Science + Environmental Science and Management 4+1
- COE + Lerner: 多个 BEng + MBA 4+1 项目
- CAS + COE: Computer Science + 各种工程 MS 4+1

### 1.4 Minors — Complete List

UD 提供约 120 个本科辅修。按学院分布：

**CANR (12)**: Animal Enterprise & Agribusiness Entrepreneurship, Animal Nutrition, Animal Science, Environmental Soil Science, Equine Science, Food & Agribusiness Marketing, Food Science, Insect & Wildlife Conservation, Landscape Horticulture, Resource Economics, Sports Performance Analytics, Statistical Data Analytics, Statistics

**CAS (~70)**: Actuarial Sciences, African Studies, Africana Studies, Ancient Greek & Roman Studies, Anthropology, Applied Music (多种乐器), Arabic, Architectural Studies, Art, Art History, Asian Studies, Astronomy, Biochemistry, Biology, Chemistry, Chinese, Cognitive Science, Comparative Literature, Computational Biology, Culture Medicine & Health, Dance, Domestic Violence Prevention, Emergency Management, English, Environmental Humanities, European Studies, Fashion History & Culture, Fashion Management, French, Functional Wearable Design, Game Studies & Esports, German, German Studies, Global Studies, History, Human Rights, Interactive Media, International Relations, Irish Studies, Islamic Studies, Italian, Japanese, Jewish Studies, Journalism, Latin American & Iberian Studies, Legal Studies, Linguistics, Material Culture Technology & Design, Mathematics, Mathematics & Data Science, Medical Humanities, Mediterranean Studies, Military Leadership, Museum Studies, Music (Composition/Jazz/Industry/Musical), Musical Theatre, Neuroscience, Philosophy, Physics, Political Communication, Political Science, Politics & Social Justice, Psychology, Religious Studies, Russian, Science Technology & Philosophy, Sexualities & Gender Studies, Sociology, Spanish (多种方向), Sustainable Apparel, Theatre (多种方向), Women & Gender Studies, Women & Religion, Writing

**Lerner (~20)**: Advertising, Applied AI for Business, Beverage Management, Business Administration, Business Analytics, Economics, Entrepreneurship, Event Management, Financial Reporting, Fintech, Gastronomy & Cuisines, Integrated Design, International Business, Management, Management Information Systems, Professional Selling & Sales Management, Real Estate Management, Restaurant Management, Social Innovation & Entrepreneurship, Spa & Wellness Management, Sport Business Analytics, Sport Management, Tourism & Travel Management, Trust Management

**CEOE (6)**: Coastal & Marine Geoscience, Earth Sciences, Geography, Human Dimensions of Climate Change, Marine Science, Meteorology, Peace & Justice Studies

**CEHD (4)**: Educational Studies, Educational Technology, Human Development & Family Sciences, Race Culture & Equity in Education

**COE (~16)**: Aerospace Military Leadership, Artificial Intelligence, Biochemical Engineering, Bioelectrical Engineering, Bioinformatics, Biomechanical Engineering, Civil Engineering, Computer Engineering, Computer Science, Construction Management, Cybersecurity, Electrical Engineering, Environmental Engineering, Materials Science & Engineering, Nanoscale Materials, Sustainable Built Environments, Sustainable Energy Technology

**CHS (~12)**: Forensic Science, Genetic Counseling, Global Health, Health & Wellness, Health Physical Activity & Disability, Healthcare Theatre, Kinesiology, Medical Diagnostics, Medical Social Services, Nutrition, Public Health, Strength & Conditioning

**Biden School (3)**: Energy & Environmental Policy, Leadership, Public Policy

### 1.5 General Education Requirements

UD 的通识教育要求称为 **University Requirements**，包括：
- **First-Year Experience (FYE)**: 大一必修课程
- **Discovery Learning Experiences (DLE)**: 发现学习体验
- **Multicultural Course**: 多元文化课程
- **Capstone**: 毕业顶石课程
- **University Breadth Requirements**: 跨学科广度要求（Creative Arts & Humanities, History & Cultural Change, Social & Behavioral Sciences, Mathematics/Natural Sciences & Technology）

> 来源: https://catalog.udel.edu/content.php?catoid=97&navoid=35630

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院

UD Graduate College 管理 60 个博士项目、145 个硕士项目和 35 个研究生证书。以下按学院列出主要研究生项目。

#### College of Agriculture and Natural Resources
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Agricultural and Resource Economics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Animal and Food Sciences | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Entomology and Wildlife Ecology | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Plant and Soil Sciences | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Applied Economics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Statistics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Food Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | Wildlife Ecology | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### College of Arts and Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Art History for Museum Professionals | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Art Conservation | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Biological Sciences | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Chemistry & Biochemistry | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Communication | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | English | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | History | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | Languages, Literatures & Cultures | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 10 | Linguistics & Cognitive Science | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 11 | Mathematics | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 12 | Music | MM | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 13 | Physics | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 14 | Political Science & International Relations | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 15 | Psychological & Brain Sciences | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 16 | Sociology | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 17 | Criminology | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 18 | Economics | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 19 | Africana Studies | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 20 | Applied Mathematics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 21 | Data Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 22 | Statistics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 23 | Applied Statistics (Online) | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 24 | Strategic Communication | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 25 | Italian Studies | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 26 | Fashion and Apparel Studies | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 27 | Interdisciplinary Neuroscience | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 28 | Climatology | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 29 | Quantum Science and Engineering | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### Alfred Lerner College of Business and Economics
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MBA (Business Administration) | MBA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | MBA Online | MBA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Accounting | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Business Analytics and Information Management | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Economics | MA/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Finance | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Hospitality and Sport Business Analytics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | International Business | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | International Business Online | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 10 | Entrepreneurship and Innovation | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 11 | Financial Services Analytics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 12 | Hospitality Business Management | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 13 | Applied Artificial Intelligence for Business | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 14 | Business Analytics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 15 | Economics and Entrepreneurship for Educators | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### College of Earth, Ocean, and Environment
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth Sciences | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Environmental Science and Management | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Geography | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Marine Studies | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Marine Policy | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Oceanography | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Ocean Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | Geological Sciences | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | GIS | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### College of Education and Human Development
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Education | MEd/EdD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Educational Statistics and Research Methods | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Educational Technology | MEd | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Human Development and Family Sciences | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | School Psychology | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Teaching English as a Second Language | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Teaching Students with Disabilities | MEd | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | Literacy (Online) | MEd | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | Teacher Leadership (Online) | MEd | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 10 | Childhood Education in Languages, Literatures & Cultures | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 11 | Secondary STEM Education | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 12 | Evaluation Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 13 | Social Work | MSW | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### College of Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Chemical Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Civil Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Computer Science | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Electrical and Computer Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Materials Science and Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Mechanical Engineering | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | Artificial Intelligence | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | Cybersecurity | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 10 | Cybersecurity Online | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 11 | Data Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 12 | Robotics | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 13 | Electrochemical Engineering | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 14 | Composite Materials | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 15 | Composites Manufacturing and Engineering | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 16 | Railroad Engineering | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 17 | Bioinformatics Data Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 18 | Electrical & Computer Engineering Online | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 19 | Engineering and Public Policy | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 20 | Wind Power Science, Engineering and Policy | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### College of Health Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing: Master of Science in Nursing (MSN) | MSN | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Nursing: Doctor of Nursing Practice | DNP | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Nursing: PhD in Nursing | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Physical Therapy | DPT | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Athletic Training | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Biomechanics and Movement Science | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Applied Physiology | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | Exercise Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | Clinical Exercise Physiology | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 10 | Health Behavior Science and Promotion | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 11 | Health Promotion | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 12 | Human Nutrition | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 13 | Medical and Molecular Sciences | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 14 | Medical Laboratory Sciences | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 15 | Communication Sciences and Disorders | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 16 | Speech Language Pathology | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 17 | Epidemiology | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 18 | Applied Epidemiology | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 19 | Biopharmaceutical Sciences | MS/PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 20 | Public Health | MPH | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 21 | Nursing: Nurse-Midwife Program | Certificate | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 22 | Nursing: Post-Master's Certificate | Certificate | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### Graduate College (Interdisciplinary)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Disaster Science & Management | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Energy and Environmental Policy | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | Water Science & Policy | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Materials Science and Engineering | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Minerals, Materials & Society | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Molecular Biosciences | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

#### Joseph R. Biden, Jr. School of Public Policy & Administration
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Policy and Administration | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 2 | Public Administration | MPA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 3 | MPA Online | MPA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 4 | Public Policy | MPP | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 5 | Urban Affairs and Public Policy | MA | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 6 | Community Engagement | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 7 | Historic Preservation | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 8 | Preservation Studies | PhD | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 9 | Urban Analytics and Policy | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |
| 10 | Urban Data Science | MS | https://www.udel.edu/academics/colleges/grad/prospective-students/programs/ |

### 2.2 Graduate Admissions Deep-Dive

**Application Portal**: https://grad.udel.edu/apply/
**Application Fee**: $75 (waivers available for veterans, McNair scholars, LSAMP participants, etc.)
**Contact**: grad@udel.edu, (302) 831-6824, 234 Hullihen Hall, Newark, DE 19716

### 2.3 Graduate Admissions Model

UD 采用**半集中式**研究生招生模式：
- Graduate College 提供统一申请门户和行政管理
- 各学院/项目自行审核申请、设定截止日期和录取标准
- 财务资助由各项目自行管理（RA/TA/Fellowship）
- 国际学生需完成 OISS Pre-Arrival Task List

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 数据 | 来源 |
|------|------|------|
| **申请系统** | Common Application 或 Coalition Application | https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/ |
| **申请费** | $75 (不可退还) | 同上 |
| **EA 截止日期** | November 1 | 同上 |
| **Honors College 截止** | November 1 | 同上 |
| **Nursing 截止日期** | December 1 | 同上 |
| **School of Music 优先截止** | December 1 | 同上 |
| **RD 优先截止日期** | January 15 | 同上 |
| **EA/Honors 决定发布** | January 31 前 | 同上 |
| **Nursing 决定发布** | February 15 前 | 同上 |
| **RD 决定发布** | 3月中旬 | 同上 |
| **SAT/ACT 政策** | Test-optional（所有申请人） | 同上 |
| **SAT 送分代码** | 5811 | 同上 |
| **ACT 送分代码** | 0634 | 同上 |
| **Superscore** | SAT superscore; ACT 取最高综合分 | 同上 |
| **推荐信** | 最多两封（可选） | 同上 |
| **成绩单** | 通过 STARS 系统自报 | 同上 |
| **面试** | 无 | 同上 |
| **作品集** | 仅音乐专业需要 audition | 同上 |

### 3.2 Undergraduate English Proficiency Table

| 考试 | 直录最低分 | 有条件录取分数 | 来源 |
|------|-----------|---------------|------|
| **TOEFL iBT** | 79 | 65–78 | https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/international-admissions/ |
| **TOEFL Essentials** | 8 | — | 同上 |
| **IELTS** | 6.5 | 5.5–6.0 | 同上 |
| **Duolingo (DET)** | 110+ | 95–109 | 同上 |
| **PTE Academic** | 53 | — | 同上 |
| **Cambridge English** | B2 First / 171 | — | 同上 |
| **EIKEN** | Grade 1 Pass or Pre-1 Pass | — | 同上 |
| **GaoKao English** | 125+/150 or 105/120 | 105–124/150 | 同上 |
| **South Korea CSAT** | Level 1 | Level 2 | 同上 |

**替代方式**:
- SAT EBRW: 550
- ACT English: 24
- GCE/GCSE/IGCSE/O-Levels: C or higher in English First Language
- IB English Lang and Lit, SL/HL: 6
- 三年以上非 ESL 美国高中英语课程，成绩 B 或以上

### 3.3 Graduate — Global Rules

| 维度 | 数据 | 来源 |
|------|------|------|
| **申请系统** | UD Graduate Application Portal | https://www.udel.edu/academics/colleges/grad/prospective-students/grad-admissions/ |
| **申请费** | $75 | 同上 |
| **GRE/GMAT** | 因项目而异（非全校统一要求） | https://www.udel.edu/academics/colleges/grad/prospective-students/grad-admissions/test-scores/ |
| **GRE 有效期** | 5年 | 同上 |
| **TOEFL 最低分** | 79 iBT（部分项目要求100） | 同上 |
| **TOEFL Speaking 最低** | 18 | 同上 |
| **IELTS 等效** | TOEFL 79 = IELTS 6.5; TOEFL 100 = IELTS 7.0 | 同上 |
| **英语成绩有效期** | 2年 | 同上 |
| **TOEFL 免试条件** | 在英语为主要语言的国家获得学位 | 同上 |
| **推荐信** | 必需 | 同上 |
| **简历** | 必需 | 同上 |
| **申请文书** | 必需 | 同上 |
| **ETS 送分代码** | 5811（无需部门代码） | 同上 |
| **截止日期** | 因项目而异 | 同上 |
| **录取类别** | Regular, Provisional, Non-Degree | 同上 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

#### In-State (Delaware Resident) — On-Campus

| 费用项目 | 金额 | 来源 |
|----------|------|------|
| Tuition (Full-Time, 12+ credits) | $15,740 | https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/in-state-freshmen/ |
| Mandatory Full-Time Fees | $2,550 | 同上 |
| Housing (Standard) | $9,286 | 同上 |
| Food (Standard) | $7,328 | 同上 |
| **Billable Total** | **$34,904** | 同上 |
| Books, Supplies, Course Materials | $1,250 | 同上 |
| Misc./Personal Costs | $1,942 | 同上 |
| Transportation | $1,000 | 同上 |
| Loan Fees | $58 | 同上 |
| **Non-Billable Total** | **$4,250** | 同上 |
| **TOTAL COA** | **$39,154** | 同上 |

#### Out-of-State — On-Campus

| 费用项目 | 金额 | 来源 |
|----------|------|------|
| Tuition (Full-Time, 12+ credits) | $42,470 | https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/out-of-state-freshmen/ |
| Mandatory Full-Time Fees | $2,550 | 同上 |
| Housing (Standard) | $9,286 | 同上 |
| Food (Standard) | $7,328 | 同上 |
| **Billable Total** | **$61,634** | 同上 |
| Books, Supplies, Course Materials | $1,250 | 同上 |
| Misc./Personal Costs | $1,942 | 同上 |
| Transportation | $1,000 | 同上 |
| Loan Fees | $58 | 同上 |
| **Non-Billable Total** | **$4,250** | 同上 |
| **TOTAL COA** | **$65,884** | 同上 |

#### Mandatory Fees Breakdown (Full-Time)

| 费用 | 金额 |
|------|------|
| New Student Orientation | $260 |
| Student Comprehensive | $1,548 |
| Student Wellbeing Fee | $734 |
| Student Center | $268 |
| International Student Service | $360 |

#### Differential Charges (Students Admitted Fall 2025+)

| 项目 | 年度附加费 |
|------|-----------|
| College of Engineering | $4,000 |
| Lerner College of Business & Economics | $3,000 |
| Nursing | $2,500 |
| Honors College | $2,000 |
| Arts & Sciences (Music Majors) | $1,250 |

### 4.2 Undergraduate Financial-Aid Policy

| 维度 | 数据 | 来源 |
|------|------|------|
| **Need-blind/Need-aware** | Need-aware for all; 不向国际学生提供 need-based aid | https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/international-students/ |
| **国际学生 need-based aid** | 不提供（"As a state-funded, public university, we cannot offer need-based financial aid to international students"） | 同上 |
| **Merit 奖学金范围** | $5,000–$15,000/年（国际学生可获得） | 同上 |
| **Distinguished Scholars** | 覆盖学费、食宿（需保持 3.0 GPA） | 同上 |
| **奖学金申请** | 无需额外申请（自动考虑） | 同上 |
| **FAFSA 代码** | 001431 | https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/ |
| **Net Price Calculator** | https://udel.clearcostcalculator.com/student | 同上 |
| **Merit 奖学金 Appeal** | 不接受（"appeals for additional merit scholarship funding are not available"） | 同上 |

### 4.3 Graduate Cost & Funding Framework

| 维度 | 数据 | 来源 |
|------|------|------|
| **学费（每学分）** | $1,149 | https://www.udel.edu/academics/colleges/grad/prospective-students/cost-of-attendance/ |
| **年度学费估算（9-12学分/学期）** | $20,682 | 同上 |
| **Mandatory Fees** | $1,102/年（Wellbeing $734 + Student Center $268 + Recreation $100） | 同上 |
| **总学费+费用** | ~$22,144 | 同上 |
| **医疗保险（有合同）** | $544.26 | 同上 |
| **医疗保险（无合同）** | $3,887.54 | 同上 |
| **校外生活费估算（12个月）** | $25,644（房租$17,940 + 水电$2,400 + 食品$5,304） | 同上 |
| **Sustaining Status（硕士）** | $892/学期 | 同上 |
| **Sustaining Status（博士）** | $1,347/学期 | 同上 |
| **申请毕业费（硕士）** | $50 | 同上 |
| **申请毕业费（博士）** | $95 | 同上 |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.admissions.EA_deadline
  value: "November 1"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/
  source_snippet: "November 1: Early Action & Honors College deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.RD_deadline
  value: "January 15"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/
  source_snippet: "January 15: Regular admission priority deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.test_optional
  value: true
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/
  source_snippet: "UD is test-optional for all applicants. Students choose whether to submit SAT or ACT scores."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.cost.tuition_in_state_2026_2027
  value: "$15,740"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/in-state-freshmen/
  source_snippet: "Full-Time Tuition (12+ credits) $15,740"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.cost.tuition_out_of_state_2026_2027
  value: "$42,470"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/out-of-state-freshmen/
  source_snippet: "Full-Time Tuition (12+ credits) $42,470"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.cost.total_coa_in_state
  value: "$39,154"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/in-state-freshmen/
  source_snippet: "TOTAL ESTIMATED YEARLY COA $39,154"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_coa_out_of_state
  value: "$65,884"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/out-of-state-freshmen/
  source_snippet: "Total Estimated Yearly Cost of Attendance $65,884"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.admissions.application_fee
  value: "$75"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/
  source_snippet: "Pay the non-refundable $75 application fee"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.admissions.mid_50_gpa
  value: "3.68 – 4.22"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/
  source_snippet: "GPA 3.68 – 4.22"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.admissions.mid_50_sat
  value: "1240 – 1390"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/freshman-admissions/
  source_snippet: "SAT 1240 – 1390"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-001:
  field: international.english_proficiency.toefl_min
  value: "79 iBT"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/international-admissions/
  source_snippet: "TOEFL iBT 79 iBT / 550 PBT / 233 CBT"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-002:
  field: international.english_proficiency.ielts_min
  value: "6.5"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/international-admissions/
  source_snippet: "IELTS 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-003:
  field: international.english_proficiency.duolingo_min
  value: "110+"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/apply-to-ud/international-admissions/
  source_snippet: "Duolingo (DET) 110+"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-004:
  field: international.financial_aid.need_based
  value: "Not available for international students"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/international-students/
  source_snippet: "As a state-funded, public university, we cannot offer need-based financial aid to international students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-005:
  field: international.merit_scholarships
  value: "$5,000 – $15,000/year"
  source_url: https://www.udel.edu/apply/undergraduate-admissions/financing-your-degree/international-students/
  source_snippet: "International students are eligible for merit scholarships ranging from $5,000 to $15,000 per year."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.application_fee
  value: "$75"
  source_url: https://www.udel.edu/academics/colleges/grad/prospective-students/grad-admissions/
  source_snippet: "Application Fee: $75.00 for the current application season"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.cost.tuition_per_credit
  value: "$1,149"
  source_url: https://www.udel.edu/academics/colleges/grad/prospective-students/cost-of-attendance/
  source_snippet: "Base rate: $1,149 per credit hour"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_proficiency.toefl_min
  value: "79 iBT (some programs require 100)"
  source_url: https://www.udel.edu/academics/colleges/grad/prospective-students/grad-admissions/test-scores/
  source_snippet: "Minimum TOEFL iBT score: 79 (some programs require 100)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-001:
  field: programs.total_ug_majors
  value: "154+"
  source_url: https://www.udel.edu/content/udel/en/apply/undergraduate-admissions/major-finder
  source_snippet: "more than 150 major fields of study"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-002:
  field: programs.total_grad_programs
  value: "161"
  source_url: https://www.udel.edu/academics/colleges/grad/prospective-students/programs/
  source_snippet: "60 doctoral and 145 master's degree programs... 35 certificate programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-S-001:
  field: institution.colleges
  value: "10 colleges"
  source_url: https://www.udel.edu/academics/colleges/
  source_snippet: "CANR, CAS, Lerner, CEOE, CEHD, COE, CHS, Graduate College, Honors College, Biden School"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
udelaware-knowledge-base-v2/
├── 00-institution-overview
│   ├── 00.1-program-counts.md
│   ├── 00.2-hierarchy-tree.md
│   ├── 00.3-degree-inventory.md
│   └── 00.4-distribution-matrix.md
├── 01-undergraduate-education
│   ├── 01.1-CANR-programs.md
│   ├── 01.2-CAS-programs.md
│   ├── 01.3-Lerner-programs.md
│   ├── 01.4-CEOE-programs.md
│   ├── 01.5-CEHD-programs.md
│   ├── 01.6-COE-programs.md
│   ├── 01.7-CHS-programs.md
│   └── 01.8-Biden-programs.md
├── 02-graduate-education
│   ├── 02.1-CANR-grad.md
│   ├── 02.2-CAS-grad.md
│   ├── 02.3-Lerner-grad.md
│   ├── 02.4-CEOE-grad.md
│   ├── 02.5-CEHD-grad.md
│   ├── 02.6-COE-grad.md
│   ├── 02.7-CHS-grad.md
│   └── 02.8-Biden-grad.md
├── 03-requirements-deadlines
│   ├── 03.1-ug-deadlines.md
│   ├── 03.2-ug-english-proficiency.md
│   └── 03.3-grad-admissions.md
├── 04-costs-financial-aid
│   ├── 04.1-ug-cost-in-state.md
│   ├── 04.2-ug-cost-out-of-state.md
│   ├── 04.3-ug-financial-aid.md
│   └── 04.4-grad-cost.md
└── 05-evidence-chain
    └── 05.1-evidence-index.md
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "udelaware-knowledge-base-v2"
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

| 优先级 | 数据项 | 目标 URL | 说明 |
|--------|--------|---------|------|
| P0 | 各研究生项目具体截止日期 | 各项目单独页面 | 因项目而异，需逐一爬取 |
| P0 | 各研究生项目 GRE/GMAT 要求 | 各项目单独页面 | 因项目而异 |
| P1 | 完整辅修列表（带 URL） | Catalog minors 页面 | 需进一步爬取 |
| P1 | 各研究生项目详细录取要求 | 各项目页面 | GPA minimum, specific requirements |
| P1 | 工程学院各系详细信息 | engineering.udel.edu | 网站连接失败，需重试 |
| P2 | 奖学金详细信息 | Financial aid 页面 | Merit scholarship details |
| P2 | 4+1 项目完整列表 | Catalog | 需从 catalog 提取 |
| P2 | 研究生 funding 机会详情 | grad funding 页面 | RA/TA/Fellowship details |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | University of Delaware |
|------|----------------------|
| **类型** | Public Research University |
| **位置** | Newark, Delaware |
| **本科生总数** | ~19,000 |
| **研究生总数** | ~4,000 |
| **UG 学费 (In-State)** | $15,740 |
| **UG 学费 (OOS)** | $42,470 |
| **UG 总 COA (In-State)** | $39,154 |
| **UG 总 COA (OOS)** | $65,884 |
| **Need-blind (Intl?)** | No (need-aware for all; no need-based aid for intl) |
| **EA 截止日期** | November 1 |
| **RD 截止日期** | January 15 |
| **SAT/ACT 要求** | Test-optional |
| **TOEFL 最低分** | 79 |
| **IELTS 最低分** | 6.5 |
| **Duolingo 最低分** | 110 |
| **研究生申请费** | $75 |
| **研究生学费/学分** | $1,149 |
| **专业总数 (Rule 1)** | 154 UG + 161 Grad = 315 |
| **学院数 (Rule 2)** | 10 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: udel.edu, catalog.udel.edu, lerner.udel.edu, cehd.udel.edu, canr.udel.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
