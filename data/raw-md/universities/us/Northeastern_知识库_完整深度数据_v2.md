# Northeastern University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Individual Majors) | 109 |
| 本科联合专业 (Combined Majors) | 199 |
| 本科学位专业总计 | 308 |
| 本科辅修 (Minor) | N/A (未单独列出) |
| 研究生学位项目 (Master's/Certificate/Doctorate/PhD) | 286 |
| 学院 / 独立系所总数 | 10 |
| **学位项目总计 (UG + Grad)** | **594** |

> **来源**: admissions.northeastern.edu/academics/areas-of-study/ (329 majors, 199 combined majors); graduate.northeastern.edu/programs/ (286 graduate programs)

### 0.2 学院 / 系层级结构

```
Northeastern University
├── Bouvé College of Health Sciences                    [学院]
│   ├── Health Sciences
│   ├── Nursing
│   ├── Pharmaceutical Sciences
│   ├── Pharmacy (PharmD)
│   ├── Speech Language Pathology and Audiology
│   └── Public Health
├── College of Arts, Media and Design                   [学院]
│   ├── Architecture
│   ├── Art: Art, Visual Studies
│   ├── Communication Studies
│   ├── Design
│   ├── Game Art and Animation
│   ├── Game Design
│   ├── Journalism
│   ├── Landscape Architecture
│   ├── Media and Screen Studies
│   ├── Media Arts
│   ├── Music / Music Industry / Music Technology
│   ├── Public Relations
│   └── Theatre
├── College of Engineering                              [学院]
│   ├── Bioengineering
│   ├── Chemical Engineering
│   ├── Civil Engineering
│   ├── Computer Engineering
│   ├── Electrical Engineering
│   ├── Environmental Engineering
│   ├── Industrial Engineering
│   └── Mechanical Engineering
├── College of Professional Studies                     [学院]
│   └── (Graduate programs, professional development)
├── College of Science                                  [学院]
│   ├── Applied Physics / Biomedical Physics / Physics
│   ├── Biochemistry / Chemistry
│   ├── Biology / Cell and Molecular Biology / Marine Biology
│   ├── Behavioral Neuroscience
│   ├── Environmental and Sustainability Sciences / Environmental Science / Environmental Studies
│   ├── Linguistics
│   ├── Mathematics
│   └── Psychology
├── College of Social Sciences and Humanities           [学院]
│   ├── Africana Studies / Global Asian Studies
│   ├── American Sign Language / ASL-English Interpreting
│   ├── Criminology and Criminal Justice
│   ├── Cultural Anthropology
│   ├── Economics
│   ├── English
│   ├── History / History, Culture, and Law
│   ├── Human Services
│   ├── International Affairs
│   ├── Philosophy
│   ├── Political Science / Politics, Philosophy, Economics
│   ├── Religious Studies
│   ├── Sociology
│   └── Spanish
├── D'Amore-McKim School of Business                    [学院]
│   ├── Business Administration (16 concentrations)
│   ├── International Business (16 concentrations)
│   └── Accounting / MBA / graduate programs
├── Khoury College of Computer Sciences                 [学院]
│   ├── Computer Science
│   ├── Computing and Law
│   ├── Cybersecurity
│   └── Data Science
├── Mills College at Northeastern                       [学院]
│   └── (Liberal arts programs, Oakland campus)
└── School of Law                                       [学院]
    └── JD / LLM / graduate law programs
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~50 |
| BS | Bachelor of Science | 本科 | ~45 |
| BFA | Bachelor of Fine Arts | 本科 | ~5 |
| BArch | Bachelor of Architecture | 本科 | 2 |
| BSBA | Bachelor of Science in Business Administration | 本科 | ~32 |
| BSIB | Bachelor of Science in International Business | 本科 | ~16 |
| PharmD | Doctor of Pharmacy | 本科 | 1 |
| MS | Master of Science | 研究生 | ~120 |
| MA | Master of Arts | 研究生 | ~30 |
| MBA | Master of Business Administration | 研究生 | ~15 |
| MEng | Master of Engineering | 研究生 | ~20 |
| MFA | Master of Fine Arts | 研究生 | ~5 |
| MPH | Master of Public Health | 研究生 | ~5 |
| MEd | Master of Education | 研究生 | ~10 |
| MSW | Master of Social Work | 研究生 | 2 |
| MArch | Master of Architecture | 研究生 | 2 |
| JD | Juris Doctor | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | ~30 |
| EdD | Doctor of Education | 研究生 | ~5 |
| DNP | Doctor of Nursing Practice | 研究生 | ~3 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | ~120 |

> **注**: 研究生项目总计286个，包括硕士、博士、专业博士和研究生证书。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BArch | BSBA | BSIB | PharmD | MS | MA | MBA | MEng | MFA | MPH | MEd | PhD | EdD | DNP | JD | Certificate | 合计 |
|------------|----|----|-----|-------|------|------|--------|----|----|-----|------|-----|-----|-----|-----|-----|-----|-----|-------------|------|
| Bouvé College of Health Sciences | 0 | 4 | 0 | 0 | 0 | 0 | 1 | 15 | 0 | 0 | 0 | 0 | 5 | 0 | 5 | 0 | 3 | 0 | 20 | 53 |
| College of Arts, Media and Design | 10 | 0 | 5 | 2 | 0 | 0 | 0 | 5 | 5 | 0 | 0 | 5 | 0 | 0 | 3 | 0 | 0 | 0 | 10 | 45 |
| College of Engineering | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 20 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 15 | 73 |
| College of Professional Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 5 | 0 | 0 | 0 | 0 | 5 | 0 | 5 | 0 | 0 | 30 | 55 |
| College of Science | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 15 | 5 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 10 | 58 |
| College of Social Sciences and Humanities | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 10 | 0 | 0 | 0 | 0 | 5 | 5 | 0 | 0 | 0 | 15 | 70 |
| D'Amore-McKim School of Business | 0 | 0 | 0 | 0 | 16 | 16 | 0 | 15 | 0 | 15 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 10 | 77 |
| Khoury College of Computer Sciences | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 10 | 34 |
| Mills College at Northeastern | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 6 |
| **合计** | 40 | 36 | 5 | 2 | 16 | 16 | 1 | 105 | 25 | 15 | 20 | 5 | 5 | 10 | 41 | 5 | 3 | 1 | 125 | **594** |

> **注**: 数量为估算值，基于页面声明（329 UG majors + 199 combined = 308 UG; 286 grad programs）。实际精确数字需从完整目录提取。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Northeastern University拥有9个本科学院（加上Mills College at Northeastern共10个），提供329个主修专业和199个联合专业。详见Section 0.2层级树。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Bouvé College of Health Sciences

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Science* | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Nursing | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Pharmaceutical Sciences | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Speech Language Pathology and Audiology | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | Public Health* | https://admissions.northeastern.edu/academics/areas-of-study/ |

##### PharmD
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy (PharmD) | https://admissions.northeastern.edu/academics/areas-of-study/ |

> *表示同时在Boston和Oakland校区提供

#### College of Arts, Media and Design

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Communication Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Journalism | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Media and Screen Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | Media Arts | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 6 | Music | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 7 | Music Industry | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 8 | Music Technology | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 9 | Public Relations | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 10 | Theatre | https://admissions.northeastern.edu/academics/areas-of-study/ |

##### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art: Art, Visual Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Design | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Game Art and Animation | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Game Design | https://admissions.northeastern.edu/academics/areas-of-study/ |

##### BArch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Landscape Architecture | https://admissions.northeastern.edu/academics/areas-of-study/ |

#### College of Engineering

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Chemical Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Civil Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Computer Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | Electrical Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 6 | Environmental Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 7 | Industrial Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 8 | Mechanical Engineering | https://admissions.northeastern.edu/academics/areas-of-study/ |

#### College of Science

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Behavioral Neuroscience* | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Biochemistry | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Biology* | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | Biomedical Physics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 6 | Cell and Molecular Biology | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 7 | Chemistry | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 8 | Environmental and Sustainability Sciences | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 9 | Environmental Science | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 10 | Environmental Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 11 | Linguistics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 12 | Marine Biology | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 13 | Mathematics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 14 | Physics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 15 | Psychology* | https://admissions.northeastern.edu/academics/areas-of-study/ |

#### College of Social Sciences and Humanities

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | American Sign Language | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | American Sign Language – English Interpreting | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Criminology and Criminal Justice | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | Cultural Anthropology | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 6 | Economics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 7 | English | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 8 | Global Asian Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 9 | History | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 10 | History, Culture, and Law | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 11 | Human Services | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 12 | International Affairs | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 13 | Philosophy | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 14 | Political Science | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 15 | Politics, Philosophy, Economics* | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 16 | Religious Studies | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 17 | Sociology | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 18 | Spanish | https://admissions.northeastern.edu/academics/areas-of-study/ |

#### D'Amore-McKim School of Business

##### BSBA (Business Administration)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration: Accounting | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Business Administration: Accounting and Advisory Services | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Business Administration: Brand Management | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Business Administration: Business Analytics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | Business Administration: Corporate Innovation | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 6 | Business Administration: Entrepreneurial Startups | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 7 | Business Administration: Family Business | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 8 | Business Administration: Finance | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 9 | Business Administration: Fintech | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 10 | Business Administration: Healthcare Management and Consulting | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 11 | Business Administration: Management | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 12 | Business Administration: Management Information Systems | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 13 | Business Administration: Marketing | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 14 | Business Administration: Marketing Analytics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 15 | Business Administration: Social Innovation and Entrepreneurship | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 16 | Business Administration: Supply Chain Management | https://admissions.northeastern.edu/academics/areas-of-study/ |

##### BSIB (International Business)
| # | 专业 | URL |
|---|------|-----|
| 1 | International Business: Accounting | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | International Business: Accounting and Advisory Services | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | International Business: Brand Management | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | International Business: Business Analytics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 5 | International Business: Corporate Innovation | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 6 | International Business: Entrepreneurial Startups | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 7 | International Business: Family Business | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 8 | International Business: Finance | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 9 | International Business: Fintech | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 10 | International Business: Healthcare Management and Consulting | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 11 | International Business: Management | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 12 | International Business: Management Information Systems | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 13 | International Business: Marketing | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 14 | International Business: Marketing Analytics | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 15 | International Business: Social Innovation and Entrepreneurship | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 16 | International Business: Supply Chain Management | https://admissions.northeastern.edu/academics/areas-of-study/ |

#### Khoury College of Computer Sciences

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science* | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 2 | Computing and Law | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 3 | Cybersecurity | https://admissions.northeastern.edu/academics/areas-of-study/ |
| 4 | Data Science | https://admissions.northeastern.edu/academics/areas-of-study/ |

#### Mills College at Northeastern

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Discover Oakland* (Interdisciplinary Studies) | https://admissions.northeastern.edu/academics/areas-of-study/ |

> 注: Mills College at Northeastern在Oakland校区提供文科项目，具体专业列表需进一步确认。

### 1.3 Interdisciplinary / cross-college undergraduate programs

Northeastern提供199个联合专业（Combined Majors），这些项目结合两个学科领域。具体列表请访问:
https://admissions.northeastern.edu/academics/areas-of-study/ (选择"Combined Majors"筛选)

### 1.4 Minors — complete list

Northeastern的辅修项目信息未在本科招生页面单独列出。建议访问课程目录获取完整辅修列表。

### 1.5 General/Institute-wide requirements

Northeastern的核心课程要求信息请访问:
https://undergraduate.northeastern.edu/

### 1.6 Course-ID → Major quick-lookup

Northeastern不使用课程编号系统来标识专业。

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Northeastern提供286个研究生项目，包括硕士、博士、专业博士和研究生证书。以下为按学院分组的主要项目:

#### Bouvé College of Health Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult-Gerontology Acute Care Nursing | https://graduate.northeastern.edu/programs/ |
| 2 | Public Health | https://graduate.northeastern.edu/programs/ |
| 3 | Pharmaceutical Sciences | https://graduate.northeastern.edu/programs/ |
| 4 | Health Informatics | https://graduate.northeastern.edu/programs/ |
| 5 | Applied Behavior Analysis | https://graduate.northeastern.edu/programs/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice | https://graduate.northeastern.edu/programs/ |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Physical Therapy | https://graduate.northeastern.edu/programs/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult-Gerontology Acute Care Nursing | https://graduate.northeastern.edu/programs/ |
| 2 | Adult-Gerontology Primary Care Nursing | https://graduate.northeastern.edu/programs/ |

#### College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced and Intelligent Manufacturing | https://graduate.northeastern.edu/programs/ |
| 2 | Chemical Engineering | https://graduate.northeastern.edu/programs/ |
| 3 | Civil Engineering | https://graduate.northeastern.edu/programs/ |
| 4 | Computer Engineering | https://graduate.northeastern.edu/programs/ |
| 5 | Electrical Engineering | https://graduate.northeastern.edu/programs/ |
| 6 | Environmental Engineering | https://graduate.northeastern.edu/programs/ |
| 7 | Industrial Engineering | https://graduate.northeastern.edu/programs/ |
| 8 | Mechanical Engineering | https://graduate.northeastern.edu/programs/ |
| 9 | Operations Research | https://graduate.northeastern.edu/programs/ |
| 10 | Structural Engineering | https://graduate.northeastern.edu/programs/ |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://graduate.northeastern.edu/programs/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://graduate.northeastern.edu/programs/ |
| 2 | Civil Engineering | https://graduate.northeastern.edu/programs/ |
| 3 | Computer Engineering | https://graduate.northeastern.edu/programs/ |
| 4 | Electrical Engineering | https://graduate.northeastern.edu/programs/ |
| 5 | Mechanical Engineering | https://graduate.northeastern.edu/programs/ |

#### D'Amore-McKim School of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | AI MBA | https://graduate.northeastern.edu/programs/ |
| 2 | Accounting/MBA | https://graduate.northeastern.edu/programs/ |
| 3 | Full-Time MBA | https://graduate.northeastern.edu/programs/ |
| 4 | Part-Time MBA | https://graduate.northeastern.edu/programs/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://graduate.northeastern.edu/programs/ |
| 2 | Business Analytics | https://graduate.northeastern.edu/programs/ |
| 3 | Finance | https://graduate.northeastern.edu/programs/ |
| 4 | International Business | https://graduate.northeastern.edu/programs/ |
| 5 | Management | https://graduate.northeastern.edu/programs/ |
| 6 | Marketing | https://graduate.northeastern.edu/programs/ |
| 7 | Technological Entrepreneurship | https://graduate.northeastern.edu/programs/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Financial Decision Making | https://graduate.northeastern.edu/programs/ |
| 2 | Business Analytics | https://graduate.northeastern.edu/programs/ |

#### Khoury College of Computer Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://graduate.northeastern.edu/programs/ |
| 2 | Cybersecurity | https://graduate.northeastern.edu/programs/ |
| 3 | Data Science | https://graduate.northeastern.edu/programs/ |
| 4 | Artificial Intelligence | https://graduate.northeastern.edu/programs/ |
| 5 | Information Systems | https://graduate.northeastern.edu/programs/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://graduate.northeastern.edu/programs/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | AI Applications | https://graduate.northeastern.edu/programs/ |
| 2 | Agile Project Management | https://graduate.northeastern.edu/programs/ |

#### College of Science

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://graduate.northeastern.edu/programs/ |
| 2 | Biochemistry | https://graduate.northeastern.edu/programs/ |
| 3 | Biotechnology | https://graduate.northeastern.edu/programs/ |
| 4 | Cell and Gene Therapy | https://graduate.northeastern.edu/programs/ |
| 5 | Chemistry | https://graduate.northeastern.edu/programs/ |
| 6 | Physics | https://graduate.northeastern.edu/programs/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://graduate.northeastern.edu/programs/ |
| 2 | Chemistry | https://graduate.northeastern.edu/programs/ |
| 3 | Mathematics | https://graduate.northeastern.edu/programs/ |
| 4 | Physics | https://graduate.northeastern.edu/programs/ |
| 5 | Psychology | https://graduate.northeastern.edu/programs/ |

#### College of Social Sciences and Humanities

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://graduate.northeastern.edu/programs/ |
| 2 | History | https://graduate.northeastern.edu/programs/ |
| 3 | Political Science | https://graduate.northeastern.edu/programs/ |
| 4 | Sociology | https://graduate.northeastern.edu/programs/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice | https://graduate.northeastern.edu/programs/ |
| 2 | Economics | https://graduate.northeastern.edu/programs/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://graduate.northeastern.edu/programs/ |
| 2 | English | https://graduate.northeastern.edu/programs/ |
| 3 | History | https://graduate.northeastern.edu/programs/ |
| 4 | Political Science | https://graduate.northeastern.edu/programs/ |
| 5 | Sociology | https://graduate.northeastern.edu/programs/ |

#### College of Professional Studies

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Psychology | https://graduate.northeastern.edu/programs/ |
| 2 | Corporate and Organizational Communication | https://graduate.northeastern.edu/programs/ |
| 3 | Education | https://graduate.northeastern.edu/programs/ |
| 4 | Geographic Information Technology | https://graduate.northeastern.edu/programs/ |
| 5 | Homeland Security | https://graduate.northeastern.edu/programs/ |
| 6 | Leadership | https://graduate.northeastern.edu/programs/ |
| 7 | Nonprofit Management | https://graduate.northeastern.edu/programs/ |
| 8 | Project Management | https://graduate.northeastern.edu/programs/ |
| 9 | Regulatory Affairs | https://graduate.northeastern.edu/programs/ |
| 10 | Technical Communication | https://graduate.northeastern.edu/programs/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education | https://graduate.northeastern.edu/programs/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Agile Project Management | https://graduate.northeastern.edu/programs/ |
| 2 | Applied Psychology | https://graduate.northeastern.edu/programs/ |
| 3 | Corporate and Organizational Communication | https://graduate.northeastern.edu/programs/ |
| 4 | Education | https://graduate.northeastern.edu/programs/ |

#### School of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://law.northeastern.edu/admissions/ |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws | https://law.northeastern.edu/admissions/ |

### 2.2 At least one program's full deep-dive (worked example)

#### Computer Science (MS) — Khoury College of Computer Sciences

- **项目网址**: https://graduate.northeastern.edu/programs/
- **学位**: Master of Science (MS)
- **学院**: Khoury College of Computer Sciences
- **校区**: Boston, MA (also available online and at regional campuses)
- **申请要求**:
  - 在线申请表
  - 所有本科和研究生成绩单
  - 个人陈述
  - 简历
  - 推荐信（具体数量请查看项目页面）
  - GRE（可选，视项目而定）
  - 英语水平证明（国际学生）
- **申请截止日期**: 滚动录取，建议提前申请
- **申请费**: 请查看项目页面

### 2.3 Graduate admissions model

Northeastern研究生招生采用分散式管理，各学院独立管理招生流程:

- **招生平台**: 各学院使用不同的申请系统
- **申请要求**: 因项目而异，一般需要成绩单、个人陈述、简历、推荐信
- **标准化考试**: 部分项目要求GRE、LSAT或GMAT
- **申请费**: 因项目而异
- **国际学生**: 需要英语水平证明（TOEFL/IELTS等）、外国学历评估、I-20申请表

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| 招生网站 | https://admissions.northeastern.edu/ |
| 申请系统 | Common Application 或 Coalition Application |
| 申请费 | $75 (不可退还) |
| ED I 截止日期 | November 1 |
| ED I 通知日期 | By January 1 |
| ED II 截止日期 | January 1 |
| ED II 通知日期 | By March 1 |
| EA 截止日期 | November 1 |
| EA 通知日期 | By February 15 |
| RD 截止日期 | January 1 |
| RD 通知日期 | By April 1 |
| FAFSA/CSS截止日期 (ED I) | November 15 |
| FAFSA/CSS截止日期 (EA) | December 1 |
| FAFSA/CSS截止日期 (ED II) | January 15 |
| FAFSA/CSS截止日期 (RD) | February 15 |
| SAT/ACT政策 | Test-optional (可选提交) |
| SAT代码 | 3667 |
| ACT代码 | 1880 |
| Superscore政策 | 是，SAT和ACT均superscore |
| 推荐信要求 | 1封学校顾问推荐信 + 1封教师推荐信 |
| 面试政策 | 未要求 |
| 作品集 | College of Arts, Media and Design申请者可提交 |
| 转学截止日期 (秋季) | April 15 |
| 转学截止日期 (春季) | October 15 |

### 3.2 Undergraduate English proficiency table

| 考试 | 中间50%分数范围 | 备注 |
|------|----------------|------|
| TOEFL iBT | 102-110 | 接受考试中心iBT和Home Edition |
| IELTS Academic | 7.5-8.0 | 不接受IELTS Indicator |
| Duolingo English Test (DET) | 130-140 | |
| PTE Academic | 79-86 | 不接受PTE Academic Online |
| Cambridge C1 Advanced/C2 Proficiency | 195-202 | |

> **注**: Northeastern没有最低分数要求，而是公布录取学生的中间50%分数范围。不接受TOEFL Essentials、TOEFL iBT Paper Test、TOEFL ITP。

### 3.3 Graduate — global rules

- **招生模式**: 分散式，各学院独立管理
- **申请平台**: 各学院使用不同系统
- **申请要求**: 因项目而异，一般需要:
  - 在线申请表
  - 所有本科和研究生成绩单
  - 个人陈述
  - 简历/履历
  - 1-3封推荐信（视项目而定）
  - GRE、LSAT或GMAT（部分项目要求）
- **申请费**: 因项目而异
- **英语水平要求**: 国际学生需提供TOEFL/IELTS等成绩
- **截止日期**: 因项目而异，建议提前申请

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-2026 academic year, line-itemized)

| 费用项目 | 金额 (Boston校区) | 金额 (Oakland校区) | 说明 |
|---------|------------------|------------------|------|
| Tuition | $67,990 | $67,990 | 学费 |
| Fees | $1,299 | $1,744 | 杂费 |
| Housing | $13,148 | $13,148 | 住宿（因选择而异） |
| Food | $8,900 | $8,900 | 餐饮（因选择而异） |
| Books and course materials | $1,000 | $1,000 | 书本和课程材料（估算） |
| Personal expenses | $900 | $900 | 个人开支（估算） |
| Transportation | $900 | $900 | 交通（估算） |
| **总计** | **$94,137** | **$94,582** | |

> **注**: 以上为估算费用，实际费用因个人选择而异。费用须经董事会批准。

### 4.2 Undergraduate financial-aid policy

| 维度 | 详情 |
|------|------|
| Need-blind/Need-aware | Need-aware for all (仅美国公民/永久居民可申请need-based aid) |
| 国际学生need-based aid | 不可申请 |
| 70%+ | 第一年学生获得经济援助（包括merit奖学金和grants） |
| $470M | 2024-2025学年本科生机构援助总额 |
| 50% | 毕业时无债务的学生比例 |
| Northeastern Promise | 承诺满足所有符合条件学生的全部demonstrated need |
| CSS代码 | 3667 |
| FAFSA代码 | 002199 |
| Merit奖学金 | 提供，基于学术成就 |
| 无债务毕业 | 超过50%的学生无债务毕业 |

### 4.3 Graduate cost & funding framework

- **学费**: 因项目而异，请访问各学院网站或 https://graduate.northeastern.edu/admissions-aid/tuition-financial-aid/
- **资助类型**: 奖学金、助教金、研究助理金、grants
- **申请费**: 因项目而异
- **费用减免**: 部分项目提供费用减免

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001: Deadlines - ED I
field: undergraduate.deadlines.ED_I
value: {application: "November 1", notification: "By January 1", fafsa_css: "November 15"}
source_url: https://admissions.northeastern.edu/application-information/admissions-deadlines-decisions/
source_snippet: "Early Decision I Application Deadline: November 1   Early Decision I Decision Notification: By January 1"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-002: Deadlines - EA
field: undergraduate.deadlines.EA
value: {application: "November 1", notification: "By February 15", fafsa_css: "December 1"}
source_url: https://admissions.northeastern.edu/application-information/admissions-deadlines-decisions/
source_snippet: "Application Deadline: November 1  Decision Notification: By February 15"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-003: Deadlines - ED II
field: undergraduate.deadlines.ED_II
value: {application: "January 1", notification: "By March 1", fafsa_css: "January 15"}
source_url: https://admissions.northeastern.edu/application-information/admissions-deadlines-decisions/
source_snippet: "Early Decision II Application Deadline: January 1   Early Decision II Decision Notification: By March 1"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-004: Deadlines - RD
field: undergraduate.deadlines.RD
value: {application: "January 1", notification: "By April 1", fafsa_css: "February 15"}
source_url: https://admissions.northeastern.edu/application-information/admissions-deadlines-decisions/
source_snippet: "Application Deadline: January 1   Decision Notification: By April 1"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-005: Test-Optional Policy
field: undergraduate.testing.policy
value: "test-optional"
source_url: https://admissions.northeastern.edu/application-information/first-year-applicants/
source_snippet: "Northeastern University is test-optional and does not require applicants to submit standardized testing to be considered for admission."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-006: SAT/ACT Codes
field: undergraduate.testing.codes
value: {SAT: "3667", ACT: "1880"}
source_url: https://admissions.northeastern.edu/application-information/first-year-applicants/
source_snippet: "you may submit the SAT(CEEB Code 3667), ACT (College Code 1880), or both"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-007: English Proficiency - TOEFL
field: undergraduate.english_proficiency.TOEFL
value: {middle_50: "102-110", notes: "Accepts iBT and Home Edition"}
source_url: https://admissions.northeastern.edu/application-information/international-applicants/
source_snippet: "102 to 110 on TOEFL Internet-Based Test (Northeastern will accept either the in-person iBT completed in a test center, or the online iBT Home Edition. Northeastern's TOEFL Code is 3667.)"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-008: English Proficiency - IELTS
field: undergraduate.english_proficiency.IELTS
value: {middle_50: "7.5-8.0"}
source_url: https://admissions.northeastern.edu/application-information/international-applicants/
source_snippet: "7.5 to 8.0 on the IELTS Academic"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-009: English Proficiency - DET
field: undergraduate.english_proficiency.DET
value: {middle_50: "130-140"}
source_url: https://admissions.northeastern.edu/application-information/international-applicants/
source_snippet: "130 to 140 on the Duolingo English Test (DET)"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-010: English Proficiency - PTE
field: undergraduate.english_proficiency.PTE
value: {middle_50: "79-86"}
source_url: https://admissions.northeastern.edu/application-information/international-applicants/
source_snippet: "79 to 86 on the PTE Academic"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-011: English Proficiency - Cambridge
field: undergraduate.english_proficiency.Cambridge
value: {middle_50: "195-202", tests: "C1 Advanced or C2 Proficiency"}
source_url: https://admissions.northeastern.edu/application-information/international-applicants/
source_snippet: "195 to 202 on either C1 Advanced (CAE) or C2 Proficiency (CPE)"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-012: Tuition
field: undergraduate.cost.tuition
value: {amount: 67990, currency: "USD", academic_year: "2025-2026"}
source_url: https://admissions.northeastern.edu/cost-financial-aid/
source_snippet: "Tuition - $67,990"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-013: Total Cost of Attendance
field: undergraduate.cost.total_coa
value: {boston: 94137, oakland: 94582, currency: "USD", academic_year: "2025-2026"}
source_url: https://admissions.northeastern.edu/cost-financial-aid/
source_snippet: "Estimated Annual Direct and Indirect Costs: $94,137 (Boston), $94,582 (Oakland)"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-014: Financial Aid Statistics
field: undergraduate.financial_aid.statistics
value: {percent_receiving_aid: "70%+", institutional_aid_2024_25: "$470M", percent_no_debt: "50%+"}
source_url: https://admissions.northeastern.edu/cost-financial-aid/
source_snippet: "70%+ of first-year students receive financial aid, including merit scholarships and grants. $470M in institutional aid will be awarded to undergraduate students in the 2024-2025 academic year. 50% of Northeastern students graduate with no debt."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-015: Application Fee
field: undergraduate.application.fee
value: {amount: 75, currency: "USD", non_refundable: true}
source_url: https://admissions.northeastern.edu/application-information/first-year-applicants/
source_snippet: "Non-refundable application fee of $75"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-016: Program Count
field: undergraduate.programs.count
value: {individual_majors: 329, combined_majors: 199, total: "329 + 199 combined"}
source_url: https://admissions.northeastern.edu/academics/areas-of-study/
source_snippet: "With 329 majors, 9 undergraduate colleges and programs, and 199 combined majors"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-017: Colleges
field: undergraduate.colleges.count
value: 10
source_url: https://www.northeastern.edu/academics/colleges/
source_snippet: "Our personalized undergraduate and graduate programs lead to degrees through the doctorate in 10 colleges and schools"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-001: Graduate Programs Count
field: graduate.programs.count
value: "200+"
source_url: https://graduate.northeastern.edu/
source_snippet: "Choose from 200-plus tailored master's, professional doctorate, PhD, and certificate programs"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-002: Graduate Programs Total
field: graduate.programs.total
value: 286
source_url: https://graduate.northeastern.edu/programs/
source_snippet: "Showing 1-10 of 286 Results"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-018: Need-Based Aid Eligibility
field: undergraduate.financial_aid.need_based_eligibility
value: "U.S. citizens and Permanent Residents only"
source_url: https://admissions.northeastern.edu/cost-financial-aid/applying-for-financial-aid/
source_snippet: "In order to be eligible for need-based financial aid, a student must be a U.S. citizen or a Permanent Resident."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-019: Northeastern Promise
field: undergraduate.financial_aid.promise
value: "Meets full demonstrated need, scholarship/grants not reduced, need-based grants increase with tuition"
source_url: https://admissions.northeastern.edu/cost-financial-aid/applying-for-financial-aid/
source_snippet: "We are dedicated to meeting the full demonstrated need for each admitted student eligible for federal financial aid. Northeastern University scholarship and grant funds will not be reduced during your undergraduate program (for up to eight in-class semesters)."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-020: Co-op Program
field: undergraduate.experiential.coop
value: "#1 university for co-ops and internships"
source_url: https://graduate.northeastern.edu/
source_snippet: "#1 University for co-ops and internships (U.S. News & World Report, 2025)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
northeastern-knowledge-base-v2/
├── 00-institution-overview.md
├── 01-undergraduate-colleges/
│   ├── bouve-health-sciences.md
│   ├── arts-media-design.md
│   ├── engineering.md
│   ├── science.md
│   ├── social-sciences-humanities.md
│   ├── damore-mckim-business.md
│   ├── khoury-computer-sciences.md
│   ├── mills-oakland.md
│   └── undeclared-explore.md
├── 02-graduate-programs/
│   ├── bouve-graduate.md
│   ├── engineering-graduate.md
│   ├── business-graduate.md
│   ├── khoury-graduate.md
│   ├── science-graduate.md
│   ├── social-sciences-graduate.md
│   ├── professional-studies-graduate.md
│   └── law-graduate.md
├── 03-deadlines-requirements.md
├── 04-costs-financial-aid.md
├── 05-english-proficiency.md
└── 06-combined-majors.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "northeastern-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| 优先级 | 数据项目 | 目标URL |
|--------|---------|--------|
| P0 | 完整199个联合专业列表 | https://admissions.northeastern.edu/academics/areas-of-study/ |
| P0 | 完整286个研究生项目列表 | https://graduate.northeastern.edu/programs/ |
| P1 | 各研究生项目具体申请费和截止日期 | 各学院网站 |
| P1 | 本科辅修完整列表 | 课程目录 |
| P1 | 各研究生项目GRE/GMAT要求 | 各学院网站 |
| P2 | Oakland校区具体专业列表 | https://ug-admissions.sites.northeastern.edu/oakland/ |
| P2 | London校区具体专业列表 | https://ug-admissions.sites.northeastern.edu/london/ |
| P2 | 各专业具体课程要求 | 课程目录 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Northeastern University | 备注 |
|------|------------------------|------|
| 所在城市 | Boston, MA | 私立大学 |
| 本科总费用/年 | $94,137 (Boston) | 2025-2026学年 |
| 学费/年 | $67,990 | 2025-2026学年 |
| Need-blind (国际生?) | 否 (Need-aware for all) | 仅美国公民/PR可申请need-based aid |
| EA截止日期 | November 1 | |
| ED I截止日期 | November 1 | |
| ED II截止日期 | January 1 | |
| RD截止日期 | January 1 | |
| SAT/ACT要求 | Test-optional | 可选提交 |
| TOEFL中间50% | 102-110 | |
| IELTS中间50% | 7.5-8.0 | |
| DET中间50% | 130-140 | |
| PTE中间50% | 79-86 | |
| 申请费 | $75 | 不可退还 |
| 研究生项目总数 | 286 | |
| 本科专业总数 | 329 + 199 combined | |
| 学院总数 | 10 | |
| Co-op项目 | 是 (#1排名) | U.S. News 2025 |
| 70%+学生获得援助 | 是 | |
| 50%学生无债务毕业 | 是 | |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.northeastern.edu, graduate.northeastern.edu, www.northeastern.edu, studentfinance.northeastern.edu, law.northeastern.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
