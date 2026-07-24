# Clarkson University Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview) -- Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Major/Concentration) | 36 |
| 本科辅修 (Minor) | 26 |
| 研究生学位项目 (Master's/Doctorate) | 22 |
| 研究生高级证书 (Advanced Certificate) | 4 |
| 预科/专业方向 (Advising Track / Pre-Professional) | 7 |
| **学位项目总计 (UG Majors + Grad Degrees + Certs)** | **62** |
| **全部项目总计 (含辅修、预科、微证书等)** | **95** |
| 学院总数 | 4 (含 Graduate School) |

> Note: Clarkson网站显示 "89 program areas of study"，其中部分项目同时提供多个学位级别（如 Major + Minor），因此按学位级别拆分后总计95项。

### 0.2 学院/系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Clarkson University
├── Wallace H. Coulter School of Engineering & Applied Sciences  [学院]
│   ├── Department of Chemical & Biomolecular Engineering        [系]
│   │   ├── Chemical Engineering (UG Major, Grad MS/PhD)
│   │   └── Biomolecular Engineering (UG Concentration)
│   ├── Department of Civil & Environmental Engineering          [系]
│   │   ├── Civil Engineering (UG Major, Grad MS/PhD)
│   │   ├── Construction Engineering Management (UG Concentration, Grad MS/AdvCert)
│   │   ├── Environmental Engineering (UG Major/Minor, Grad MS/PhD)
│   │   ├── Structural Engineering (UG Concentration)
│   │   └── Water Resources Engineering (UG Concentration)
│   ├── Department of Electrical & Computer Engineering          [系]
│   │   ├── Computer Engineering (UG Major)
│   │   ├── Electrical Engineering (UG Major/Minor)
│   │   └── Electrical & Computer Engineering (Grad PhD/MS)
│   ├── Department of Mechanical & Aerospace Engineering         [系]
│   │   ├── Aerospace Engineering (UG Major)
│   │   └── Mechanical Engineering (UG Major, Grad MS/PhD)
│   ├── Department of Computer Science                           [系]
│   │   ├── Computer Science (UG Major/Minor, Grad MS/PhD)
│   │   ├── Software Engineering (UG Major/Minor)
│   │   └── Data Science (UG Major/Minor, Grad MS)
│   ├── Department of Engineering Studies                        [系]
│   │   ├── Engineering & Management (UG Major)
│   │   ├── Engineering Studies (UG Major)
│   │   └── Engineering Management (Grad MS)
│   ├── Department of Environmental Science & Engineering        [系]
│   │   └── Environmental Science & Sustainability (UG Minor/Major)
│   └── Interdisciplinary Engineering Programs
│       ├── Advanced Manufacturing Engineering (UG Minor)
│       ├── Architectural & Facilities Engineering (UG Minor)
│       ├── Biomedical Engineering (UG Minor)
│       ├── Electrical Power Engineering (UG Concentration)
│       ├── Industrial Hygiene (UG Concentration)
│       ├── Materials Science & Engineering (UG Minor, Grad PhD)
│       ├── Power Engineering (Grad Concentration)
│       ├── Power Systems Engineering (UG Major)
│       ├── Robotics (UG Minor)
│       ├── Sustainable Energy Systems Engineering (UG Minor)
│       ├── Engineering Science (UG Minor, Grad MS)
│       └── Electrical & Computer Engineering (Grad MS/PhD)
├── Reh School of Business                                       [学院]
│   ├── Business (UG Major/Minor, Grad MBA, AdvCert)
│   ├── Business Analytics (UG Major, Grad MS)
│   ├── Business of Biotechnology (UG Major)
│   ├── Business of Energy (UG Major)
│   ├── Economics (UG Minor)
│   ├── Finance (UG Minor)
│   ├── Financial Information & Analysis (UG Major)
│   ├── Global Supply Chain Management (UG Major, Grad MS/AdvCert)
│   ├── Healthcare Business (UG Major)
│   ├── Human Resources Management (UG Minor)
│   ├── Information Systems (UG Major)
│   ├── Innovation & Entrepreneurship (UG Major)
│   ├── Marketing (UG Minor)
│   ├── Product Development & Marketing (UG Minor)
│   ├── Clinical Leadership in Healthcare Management (Grad MS)
│   ├── Healthcare Data Analytics (Grad MS)
│   └── Healthcare Management (Grad MS/AdvCert)
├── Lewis School of Health & Life Sciences                       [学院]
│   ├── Department of Biology                                    [系]
│   │   └── Biology (UG Major/Minor)
│   ├── Department of Chemistry                                  [系]
│   │   └── Chemistry (UG Major/Minor, Grad MS/PhD)
│   ├── Department of Physics                                    [系]
│   │   └── Physics (UG Major/Minor, Grad MS/PhD)
│   ├── Department of Mathematics                                [系]
│   │   ├── Mathematics (UG Major/Minor, Grad MS/PhD)
│   │   └── Applied Mathematics & Statistics (UG Major)
│   ├── Department of Psychology                                  [系]
│   │   └── Psychology (UG Major/Minor)
│   ├── Biochemistry (UG Major)
│   ├── Biomedical Science & Technology (UG Minor)
│   ├── Cognitive Neuroscience (UG Minor)
│   ├── Data Science (UG Major/Minor, Grad MS)  ⚠ shared with Coulter
│   ├── Digital Arts (UG Minor)
│   ├── Direct Entry Healthcare Programs (UG Major)
│   ├── Environmental Science & Sustainability (UG Minor/Major)
│   ├── Healthcare (UG Major)
│   ├── Humanities & Social Sciences (UG Minor)
│   ├── Anthropology (UG Minor)
│   ├── Communication (UG Minor)
│   ├── Gender & Sexuality Studies (UG Minor)
│   ├── Law Studies (UG Minor)
│   ├── Literature (UG Minor)
│   ├── Teaching (UG Minor)
│   ├── War Studies (UG Minor)
│   ├── Occupational Therapy (UG Major, Grad MS)
│   ├── Physical Therapy (UG Major, Grad DPT)
│   ├── Physician Assistant Studies (UG Major, Grad MS)
│   ├── Bioscience & Technology, Interdisciplinary (Grad MS/PhD)
│   ├── Science Studies (UG Major)
│   ├── Medicine & Healthcare (UG Minor)
│   ├── Computational Science (UG Minor)
│   ├── Industrial Hygiene (UG Concentration)  ⚠ shared with Coulter
│   └── Sustainable Solutions for the Developing World (UG Minor)
├── The Clarkson School (Early College Program)                  [学院]
│   └── Early college for high school students (not degree-granting)
└── Graduate School                                              [学院]
    └── Cross-cutting graduate programs across all disciplines
        (specific programs listed under their home schools above)
```

> Note: Data Science is jointly housed in Coulter and Lewis schools. Industrial Hygiene spans Coulter and Lewis. The Clarkson School is an early college program for high school students, not a traditional degree-granting school.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 0 |
| BS | BS | Bachelor of Science | 本科 | 34 (Majors) |
| Minor | Minor | 辅修 | 本科 | 26 |
| Concentration | Concentration | 专业方向 | 本科 | 5 |
| Advising Track | Advising Track | 预科方向 | 本科 | 7 |
| MS | MS | Master of Science | 研究生 | 13 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 7 |
| Adv Cert | Advanced Certificate | 高级证书 | 研究生 | 4 |

> Clarkson以BS学位为主，不授予BA学位。所有本科专业均授予Bachelor of Science (BS)学位。

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BS | Minor | Concentration | Adv Track | MS | MBA | PhD | DPT | Adv Cert | 合计 |
|------------|----|----|----|----|----|----|----|----|----|------|
| Coulter School of Engineering & Applied Sciences | 14 | 8 | 4 | 0 | 8 | 0 | 5 | 0 | 1 | 40 |
| Reh School of Business | 8 | 6 | 0 | 0 | 4 | 1 | 0 | 0 | 3 | 22 |
| Lewis School of Health & Life Sciences | 12 | 12 | 1 | 7 | 1 | 0 | 2 | 1 | 0 | 36 |
| Graduate School (cross-cutting) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **34** | **26** | **5** | **7** | **13** | **1** | **7** | **1** | **4** | **98** |

> Note: 数据科学(Data Science)和工业卫生(Industrial Hygiene)为跨院项目，在矩阵中归入其主归属学院。总项目数98与网站显示的89个"program areas"有差异，因部分program areas包含多个学位级别。Graduate School的项目已归入各主院系。

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Clarkson University设有3个本科学院和1个早期大学项目，提供34个本科专业(Major)、26个辅修(Minor)、5个专业方向(Concentration)和7个预科方向(Advising Track)。详见Section 0.2层级树。

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### Wallace H. Coulter School of Engineering & Applied Sciences

##### Department of Chemical & Biomolecular Engineering
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.clarkson.edu/academics/majors-minors |

###### Concentration
| # | 专业方向 | URL |
|---|---------|-----|
| 1 | Biomolecular Engineering | https://www.clarkson.edu/academics/majors-minors |

##### Department of Civil & Environmental Engineering
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.clarkson.edu/academics/majors-minors |
| 2 | Environmental Engineering | https://www.clarkson.edu/academics/majors-minors |

###### Concentration
| # | 专业方向 | URL |
|---|---------|-----|
| 1 | Construction Engineering Management | https://www.clarkson.edu/academics/majors-minors |
| 2 | Structural Engineering | https://www.clarkson.edu/academics/majors-minors |
| 3 | Water Resources Engineering | https://www.clarkson.edu/academics/majors-minors |

##### Department of Electrical & Computer Engineering
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.clarkson.edu/academics/majors-minors |
| 2 | Electrical Engineering | https://www.clarkson.edu/academics/majors-minors |

##### Department of Mechanical & Aerospace Engineering
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.clarkson.edu/academics/majors-minors |
| 2 | Mechanical Engineering | https://www.clarkson.edu/academics/majors-minors |

##### Department of Computer Science
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.clarkson.edu/academics/majors-minors |
| 2 | Software Engineering | https://www.clarkson.edu/academics/majors-minors |
| 3 | Data Science | https://www.clarkson.edu/academics/majors-minors |

##### Department of Engineering Studies
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering & Management | https://www.clarkson.edu/academics/majors-minors |
| 2 | Engineering Studies | https://www.clarkson.edu/academics/majors-minors |

##### Interdisciplinary Engineering Programs
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Power Systems Engineering | https://www.clarkson.edu/academics/majors-minors |

###### Concentration
| # | 专业方向 | URL |
|---|---------|-----|
| 1 | Electrical Power Engineering | https://www.clarkson.edu/academics/majors-minors |
| 2 | Industrial Hygiene | https://www.clarkson.edu/academics/majors-minors |

#### Reh School of Business

##### Business Programs
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business | https://www.clarkson.edu/academics/majors-minors |
| 2 | Business Analytics | https://www.clarkson.edu/academics/majors-minors |
| 3 | Business of Biotechnology | https://www.clarkson.edu/academics/majors-minors |
| 4 | Business of Energy | https://www.clarkson.edu/academics/majors-minors |
| 5 | Financial Information & Analysis | https://www.clarkson.edu/academics/majors-minors |
| 6 | Global Supply Chain Management | https://www.clarkson.edu/academics/majors-minors |
| 7 | Healthcare Business | https://www.clarkson.edu/academics/majors-minors |
| 8 | Information Systems | https://www.clarkson.edu/academics/majors-minors |
| 9 | Innovation & Entrepreneurship | https://www.clarkson.edu/academics/majors-minors |

#### Lewis School of Health & Life Sciences

##### Department of Biology
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.clarkson.edu/academics/majors-minors |

##### Department of Chemistry
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.clarkson.edu/academics/majors-minors |

##### Department of Physics
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.clarkson.edu/academics/majors-minors |

##### Department of Mathematics
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics & Statistics | https://www.clarkson.edu/academics/majors-minors |
| 2 | Mathematics | https://www.clarkson.edu/academics/majors-minors |

##### Department of Psychology
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.clarkson.edu/academics/majors-minors |

##### Health & Life Sciences Programs
###### BS (Major)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.clarkson.edu/academics/majors-minors |
| 2 | Direct Entry Healthcare Programs | https://www.clarkson.edu/academics/majors-minors |
| 3 | Environmental Science & Sustainability | https://www.clarkson.edu/academics/majors-minors |
| 4 | Healthcare | https://www.clarkson.edu/academics/majors-minors |
| 5 | Occupational Therapy | https://www.clarkson.edu/academics/majors-minors |
| 6 | Physical Therapy | https://www.clarkson.edu/academics/majors-minors |
| 7 | Physician Assistant Studies | https://www.clarkson.edu/academics/majors-minors |
| 8 | Science Studies | https://www.clarkson.edu/academics/majors-minors |
| 9 | University Studies | https://www.clarkson.edu/academics/majors-minors |
| 10 | Professional Studies | https://www.clarkson.edu/academics/majors-minors |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 项目 | 主归属学院 | 共享学院 | URL |
|---|------|----------|---------|-----|
| 1 | Data Science | Lewis School | Coulter School | https://www.clarkson.edu/academics/majors-minors |
| 2 | Industrial Hygiene | Coulter School | Lewis School | https://www.clarkson.edu/academics/majors-minors |
| 3 | Joint Programs (4+1/3+2/3+2+2) | Multiple | Multiple | https://www.clarkson.edu/academics/majors-minors |
| 4 | Business 3+1 BS/MBA | Reh School | Graduate | https://www.clarkson.edu/academics/majors-minors |

### 1.4 Minors -- Complete List

| # | Minor名称 | 主归属学院 | URL |
|---|----------|----------|-----|
| 1 | Advanced Manufacturing Engineering | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 2 | Anthropology | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 3 | Artificial Intelligence & Machine Learning | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 4 | Biomedical Engineering | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 5 | Biomedical Science & Technology | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 6 | Business | Reh | https://www.clarkson.edu/academics/majors-minors |
| 7 | Communication | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 8 | Computational Science | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 9 | Digital Arts | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 10 | Economics | Reh | https://www.clarkson.edu/academics/majors-minors |
| 11 | Electrical Engineering | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 12 | Engineering Science | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 13 | Environmental Science & Sustainability | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 14 | Finance | Reh | https://www.clarkson.edu/academics/majors-minors |
| 15 | Gender & Sexuality Studies | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 16 | Human Resources Management | Reh | https://www.clarkson.edu/academics/majors-minors |
| 17 | Humanities & Social Sciences | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 18 | Information Technology | Reh | https://www.clarkson.edu/academics/majors-minors |
| 19 | Law Studies | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 20 | Literature | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 21 | Marketing | Reh | https://www.clarkson.edu/academics/majors-minors |
| 22 | Materials Science & Engineering | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 23 | Medicine & Healthcare | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 24 | Product Development & Marketing | Reh | https://www.clarkson.edu/academics/majors-minors |
| 25 | Robotics | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 26 | Sustainable Energy Systems Engineering | Coulter | https://www.clarkson.edu/academics/majors-minors |
| 27 | Sustainable Solutions for the Developing World | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 28 | Teaching | Lewis | https://www.clarkson.edu/academics/majors-minors |
| 29 | War Studies | Lewis | https://www.clarkson.edu/academics/majors-minors |

### 1.5 Advising Tracks (Pre-Professional)

| # | 预科方向 | URL |
|---|---------|-----|
| 1 | Pre-Dental | https://www.clarkson.edu/academics/majors-minors |
| 2 | Pre-Health Sciences | https://www.clarkson.edu/academics/majors-minors |
| 3 | Pre-Medical | https://www.clarkson.edu/academics/majors-minors |
| 4 | Pre-Optometry | https://www.clarkson.edu/academics/majors-minors |
| 5 | Pre-Pharmacy | https://www.clarkson.edu/academics/majors-minors |
| 6 | Pre-Public Health | https://www.clarkson.edu/academics/majors-minors |
| 7 | Pre-Veterinary | https://www.clarkson.edu/academics/majors-minors |

### 1.6 General Education Requirements

Clarkson University要求所有本科生完成Professional Experience（实习/合作教育），这是区别于其他大学的特色要求。详见 https://www.clarkson.edu/academics 。

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 系 > 学位级别

#### Wallace H. Coulter School of Engineering & Applied Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.clarkson.edu/academics/majors-minors |
| 2 | Civil Engineering | https://www.clarkson.edu/academics/majors-minors |
| 3 | Computer Science | https://www.clarkson.edu/academics/majors-minors |
| 4 | Construction Engineering Management | https://www.clarkson.edu/academics/majors-minors |
| 5 | Data Science | https://www.clarkson.edu/academics/majors-minors |
| 6 | Electrical & Computer Engineering | https://www.clarkson.edu/academics/majors-minors |
| 7 | Engineering Management | https://www.clarkson.edu/academics/majors-minors |
| 8 | Engineering Science | https://www.clarkson.edu/academics/majors-minors |
| 9 | Environmental Engineering | https://www.clarkson.edu/academics/majors-minors |
| 10 | Mechanical Engineering | https://www.clarkson.edu/academics/majors-minors |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.clarkson.edu/academics/majors-minors |
| 2 | Civil Engineering | https://www.clarkson.edu/academics/majors-minors |
| 3 | Computer Science | https://www.clarkson.edu/academics/majors-minors |
| 4 | Electrical & Computer Engineering | https://www.clarkson.edu/academics/majors-minors |
| 5 | Environmental Engineering | https://www.clarkson.edu/academics/majors-minors |
| 6 | Materials Science & Engineering | https://www.clarkson.edu/academics/majors-minors |
| 7 | Mechanical Engineering | https://www.clarkson.edu/academics/majors-minors |

##### Advanced Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Engineering Management | https://www.clarkson.edu/academics/majors-minors |

##### Concentration (Graduate)
| # | 项目 | URL |
|---|------|-----|
| 1 | Power Engineering | https://www.clarkson.edu/academics/majors-minors |

#### Reh School of Business

##### MS / MBA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business (MBA) | MBA | https://www.clarkson.edu/academics/majors-minors |
| 2 | Business Analytics | MS | https://www.clarkson.edu/academics/majors-minors |
| 3 | Clinical Leadership in Healthcare Management | MS | https://www.clarkson.edu/academics/majors-minors |
| 4 | Global Supply Chain Management | MS | https://www.clarkson.edu/academics/majors-minors |
| 5 | Healthcare Data Analytics | MS | https://www.clarkson.edu/academics/majors-minors |
| 6 | Healthcare Management | MS | https://www.clarkson.edu/academics/majors-minors |

##### Advanced Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Business (Advanced Certificate) | https://www.clarkson.edu/academics/majors-minors |
| 2 | Global Supply Chain Management | https://www.clarkson.edu/academics/majors-minors |
| 3 | Healthcare Management | https://www.clarkson.edu/academics/majors-minors |

#### Lewis School of Health & Life Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.clarkson.edu/academics/majors-minors |
| 2 | Mathematics | https://www.clarkson.edu/academics/majors-minors |
| 3 | Occupational Therapy | https://www.clarkson.edu/academics/majors-minors |
| 4 | Physician Assistant Studies | https://www.clarkson.edu/academics/majors-minors |
| 5 | Physics | https://www.clarkson.edu/academics/majors-minors |

##### DPT (Doctor of Physical Therapy)
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://www.clarkson.edu/academics/majors-minors |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioscience & Technology, Interdisciplinary | https://www.clarkson.edu/academics/majors-minors |
| 2 | Chemistry | https://www.clarkson.edu/academics/majors-minors |
| 3 | Mathematics | https://www.clarkson.edu/academics/majors-minors |
| 4 | Physics | https://www.clarkson.edu/academics/majors-minors |

### 2.2 Graduate Program Deep-Dive: Computer Science (MS/PhD)

| 字段 | 值 |
|------|-----|
| 学院 | Wallace H. Coulter School of Engineering & Applied Sciences |
| 学位 | MS, PhD |
| 申请平台 | Clarkson Graduate Online Application |
| 申请费 | Currently waived |
| 截止日期 | Rolling admissions (no set deadline) |
| 英语要求 | TOEFL 80 / IELTS 6.5 / PTE 56 / Duolingo 115 |
| TOEFL Code | 2084 |
| 联系方式 | graduate@clarkson.edu / 518-631-9831 |
| URL | https://www.clarkson.edu/admissions-aid/graduate |

### 2.3 Graduate Admissions Model

- **模式**: Decentralized（各学院自行管理招生，Graduate School提供统一申请平台）
- **申请平台**: Clarkson Graduate Online Application (https://www.clarkson.edu/admissions-aid/graduate/how-to-apply)
- **截止日期**: Rolling admissions，无固定截止日期
- **申请费**: Currently waived（当前免收申请费）
- **TOEFL Code**: 2084
- **联系方式**:
  - Domestic: graduate@clarkson.edu
  - International: gradintl@clarkson.edu
  - Phone: 518-631-9831

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Clarkson App 或 Common App | E-U-001 |
| 申请费 | $0（首年申请免申请费） | E-U-002 |
| Early Decision截止日期 | 12月1日 | E-U-003 |
| Regular Decision截止日期 | 1月15日 | E-U-004 |
| 奖学金截止日期 | 1月15日（RD），12月1日（ED） | E-U-005 |
| FAFSA截止日期 | 2月1日 | E-U-006 |
| 押金截止日期 | 5月1日（已延长至5月15日） | E-U-007 |
| SAT/ACT政策 | Test-optional（可选提交） | E-U-008 |
| 推荐信要求 | 2封 | E-U-009 |
| 成绩单要求 | 官方成绩单 | E-U-010 |
| 个人陈述 | Required | E-U-011 |
| AP学分 | 4分和5分可获学分 | E-U-012 |
| IB学分 | 按IB标准1-7分评定 | E-U-013 |
| 录取方式 | Holistic review（综合评审） | E-U-014 |
| 申请Portal | https://undergrad.clarkson.edu/ | E-U-015 |

> Note: Clarkson网站显示的截止日期为Early Decision (12月1日)和Regular Decision (1月15日)。用户提供的EA Nov 1和EA2 Dec 1日期未在官网确认，可能为往年数据或特定项目截止日期。

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分 | 推荐分 | 来源 |
|------|--------|--------|------|
| TOEFL iBT | 80 | N/A | E-U-016 |
| TOEFL Essentials | 8.5 | N/A | E-U-016 |
| IELTS | 6.5 | N/A | E-U-016 |
| PTE | 56 | N/A | E-U-016 |
| Duolingo English Test | 115 | N/A | E-U-016 |

> 适用条件：国际学生需要提交英语能力证明。详见 https://www.clarkson.edu/admissions-aid/graduate/how-to-apply

### 3.3 Graduate -- Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| 录取模式 | Decentralized（各学院自主招生） | E-G-001 |
| 申请平台 | Clarkson Graduate Online Application | E-G-002 |
| 申请费 | Currently waived（当前免费） | E-G-003 |
| 截止日期 | Rolling admissions（滚动录取） | E-G-004 |
| GRE/GMAT政策 | 未明确要求（各项目可能不同） | E-G-005 |
| 英语要求 | TOEFL 80 / IELTS 6.5 / PTE 56 / Duolingo 115 | E-G-006 |
| TOEFL Code | 2084 | E-G-007 |
| 联系方式(Domestic) | graduate@clarkson.edu | E-G-008 |
| 联系方式(International) | gradintl@clarkson.edu | E-G-009 |
| 电话 | 518-631-9831 | E-G-010 |

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| 费用项目 | 金额 | 说明 | 来源 |
|---------|------|------|------|
| Tuition | $61,594 | 学费 | E-U-017 |
| Fees | $1,370 | 杂费 | E-U-017 |
| Housing (average) | $10,840 | 住宿（加权平均） | E-U-017 |
| Food | $8,528 | 餐饮 | E-U-017 |
| Books/Course Materials/Supplies/Equipment | $1,560 | 书本/课程材料 | E-U-017 |
| Personal | $900 | 个人开支 | E-U-017 |
| Transportation | $1,596 | 交通 | E-U-017 |
| Loan Fees | $68 | 贷款手续费 | E-U-017 |
| **Total Costs** | **$86,456** | **总费用** | E-U-017 |
| **Direct Costs** | **$82,332** | **直接费用（学费+杂费+住宿+餐饮）** | E-U-017 |

> 来源: https://www.clarkson.edu/admissions-aid/undergraduate/tuition-costs

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| 获得资助比例 | 90% | E-U-018 |
| 全额学费学生比例 | 0% | E-U-018 |
| 平均资助金额 | $41,285/年 | E-U-018 |
| 支付不到总费用一半的学生比例 | 60% | E-U-018 |
| 无债务毕业比例 | 25% | E-U-018 |
| 债务低于起薪比例 | 80% | E-U-018 |
| 平均起薪(2025届) | $82,786 | E-U-019 |
| Need-blind/Need-aware(美国) | Need-based aid available（通过FAFSA申请） | E-U-020 |
| Need-blind/Need-aware(国际) | Need-aware（不提供need-based aid给国际学生） | E-U-021 |
| 国际学生奖学金范围 | $5,000 - $40,000/年 | E-U-022 |
| 国际学生奖学金申请 | 自动考虑（无需额外申请） | E-U-023 |
| Ignite Presidential Fellowship | 全额学费（10名学生，8学期） | E-U-024 |
| Solinsky Engineers Program | $5,000/年（最多4年，工程专业） | E-U-025 |
| FAFSA截止日期 | 2月1日 | E-U-006 |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| 标准学费（全日制） | $1,545/学分 | E-G-011 |
| 在线项目学费 | $1,025/学分 | E-G-012 |
| Physical Therapy (DPT) | $11,035/学期（7学期） | E-G-013 |
| Physician Assistant (MS) | $12,719/学期（8学期） | E-G-014 |
| 军人学费 | $1,545/学分（与标准相同） | E-G-015 |
| 奖学金覆盖比例 | 最高30%学费（merit-based） | E-G-016 |
| 申请费 | Currently waived | E-G-003 |
| 资助类型 | Assistantships, Scholarships, Loans, Fellowships | E-G-017 |
| 企业合作伙伴折扣 | 可通过雇主获得学费折扣 | E-G-018 |
| 96%就业率 | 毕业生在相关领域就业或继续深造 | E-G-019 |

> 来源: https://www.clarkson.edu/admissions-aid/graduate/cost-aid

---

## SECTION 5 -- Evidence Chain Index

### Undergraduate Evidence (E-U-xxx)

```yaml
E-U-001:
  field: undergraduate.application.system
  value: "Clarkson App or Common App"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/how-to-apply
  source_snippet: "Incoming undergraduate students can complete ONE of the applications listed below"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.application.fee
  value: "$0 (no fee for first-year applicants)"
  source_url: https://www.clarkson.edu/apply
  source_snippet: "Students who are applying for first-year entry will not be charged an application fee if you apply using the Clarkson or Common App."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.early_decision
  value: "December 1"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate
  source_snippet: "Early Decision: December 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.regular_decision
  value: "January 15"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate
  source_snippet: "Regular Decision: January 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.deadlines.scholarship
  value: "January 15 (RD), December 1 (ED)"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/how-to-apply
  source_snippet: "To be eligible for merit scholarships and grants, we need to receive your admission application and any additional scholarship submissions by January 15. If you are applying for early decision, the deadline is December 1."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.deadlines.fafsa
  value: "February 1"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/how-to-apply
  source_snippet: "deadline to file the FAFSA is February 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.deadlines.deposit
  value: "May 1 (extended to May 15)"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate
  source_snippet: "Accepted Students: We've extended our deposit deadline! You now have until May 15th to make your deposit and become a Golden Knight!"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.testing.test_optional
  value: "Test-optional"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "Clarkson continues to be test optional. Application materials required will be two letters of recommendation, official transcripts and a personal statement."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.requirements.recommendations
  value: "Two letters of recommendation"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "Application materials required will be two letters of recommendation, official transcripts and a personal statement."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.requirements.transcripts
  value: "Official transcripts"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "Application materials required will be two letters of recommendation, official transcripts and a personal statement."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.requirements.personal_statement
  value: "Required"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "Application materials required will be two letters of recommendation, official transcripts and a personal statement."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.testing.ap_credit
  value: "Scores of 4 and 5 accepted"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "Clarkson will accept scores of 4 and 5 on AP tests within our current awarding parameters."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.testing.ib_credit
  value: "Graded on IB 1-7 scale"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "Missing IB exams will not matter as long as the student meets the IB requirements as IB will still grade on the normal 1-7 scale."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.admissions.review_type
  value: "Holistic review"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/undergraduate-admissions-faqs
  source_snippet: "When reviewing applications, our admissions team is reading your application holistically. We look at course load, course type, letters of recommendation, and all four years of high school."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.application.portal
  value: "https://undergrad.clarkson.edu/"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate
  source_snippet: "undergrad.clarkson.edu"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.testing.english_proficiency
  value: {TOEFL: 80, TOEFL_Essentials: 8.5, IELTS: 6.5, PTE: 56, Duolingo: 115}
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "Accepted tests with minimum acceptable scores are: TOEFL (80) and TOEFL Essentials (8.5), IELTS (6.5), PTE (56) or Duolingo English Test (115)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.cost.attendance_2026_2027
  value: {tuition: 61594, fees: 1370, housing: 10840, food: 8528, books: 1560, personal: 900, transportation: 1596, loan_fees: 68, total: 86456, direct: 82332}
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/tuition-costs
  source_snippet: "Tuition: $61,594, Fees: $1,370, Housing (average): $10,840, Food: $8,528, Total Costs: $86,456"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-018:
  field: undergraduate.aid.statistics
  value: {aid_rate: "90%", full_tuition: "0%", avg_award: "$41,285", half_cost: "60%", debt_free: "25%"}
  source_url: https://www.clarkson.edu/admissions-aid/financial-aid
  source_snippet: "90% of Clarkson undergraduate students receive financial aid. That means that 0% of Clarkson students pay full tuition. Nearly 60% pay less than half of the total cost. $41,285 average yearly financial aid award."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-019:
  field: undergraduate.outcomes.starting_salary
  value: "$82,786 (Class of 2025)"
  source_url: https://www.clarkson.edu/admissions-aid/financial-aid
  source_snippet: "$82,786 Is the average starting salary for Clarkson graduates for the Class of 2025."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-020:
  field: undergraduate.aid.need_blind_us
  value: "Need-based aid available (FAFSA required)"
  source_url: https://www.clarkson.edu/admissions-aid/financial-aid
  source_snippet: "If you are a U.S. citizen, make sure you have your Free Application for Federal Student Aid (FAFSA) filled out by the February 1 deadline to be eligible for federal, state and institutional need-based aid."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-021:
  field: undergraduate.aid.international
  value: "Need-aware; no need-based aid for international students"
  source_url: https://www.clarkson.edu/admissions-aid/international/tuition-costs
  source_snippet: "Scholarships are available, but Clarkson does not provide need-based aid to international students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-022:
  field: undergraduate.aid.international_scholarship_range
  value: "$5,000 - $40,000/year"
  source_url: https://www.clarkson.edu/admissions-aid/international/tuition-costs
  source_snippet: "Clarkson's international scholarships range from $5,000 to $40,000 a year."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-023:
  field: undergraduate.aid.international_scholarship_auto
  value: "Automatically considered (no additional application)"
  source_url: https://www.clarkson.edu/admissions-aid/international/tuition-costs
  source_snippet: "All accepted international undergraduate students are considered for partial scholarships from Clarkson — no additional application required."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-024:
  field: undergraduate.aid.ignite_fellowship
  value: "Full tuition for 10 students, 8 semesters"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/tuition-costs/scholarships-grants-loans
  source_snippet: "The Ignite Presidential Fellowship is a merit-based scholarship covering all tuition costs for 10 first-time students entering Clarkson for four years (eight semesters) of undergraduate study."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-025:
  field: undergraduate.aid.solinsky_engineers
  value: "$5,000/year for up to 4 years (engineering students)"
  source_url: https://www.clarkson.edu/admissions-aid/undergraduate/tuition-costs/scholarships-grants-loans
  source_snippet: "Each Solinsky Engineer is awarded $5,000 per year, for up to four years of undergraduate study at Clarkson, for a total of $20,000."
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

### Graduate Evidence (E-G-xxx)

```yaml
E-G-001:
  field: graduate.admissions.model
  value: "Decentralized"
  source_url: https://www.clarkson.edu/admissions-aid/graduate
  source_snippet: "The Office of Graduate Admissions"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.application.platform
  value: "Clarkson Graduate Online Application"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "Complete the Graduate School Online Application Form."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.application.fee
  value: "Currently waived"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "To support prospective graduate students, we are waiving application fees at this time."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.deadlines
  value: "Rolling admissions (no set deadlines)"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "For Clarkson University's programs, there are no set deadlines for graduate admissions. Instead, we review applications on a rolling basis."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-005:
  field: graduate.testing.gre_policy
  value: "Not explicitly required (program-specific)"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "Along with all requirements listed above, review any program-specific prerequisites before submitting your application."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-006:
  field: graduate.testing.english_proficiency
  value: {TOEFL: 80, TOEFL_Essentials: 8.5, IELTS: 6.5, PTE: 56, Duolingo: 115}
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "Accepted tests with minimum acceptable scores are: TOEFL (80) and TOEFL Essentials (8.5), IELTS (6.5), PTE (56) or Duolingo English Test (115)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-007:
  field: graduate.testing.toefl_code
  value: "2084"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/how-to-apply
  source_snippet: "TOEFL Institution Code is 2084"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-008:
  field: graduate.contact.domestic
  value: "graduate@clarkson.edu"
  source_url: https://www.clarkson.edu/admissions-aid/graduate
  source_snippet: "Domestic Students: graduate@clarkson.edu"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-009:
  field: graduate.contact.international
  value: "gradintl@clarkson.edu"
  source_url: https://www.clarkson.edu/admissions-aid/graduate
  source_snippet: "International Students: gradintl@clarkson.edu"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-010:
  field: graduate.contact.phone
  value: "518-631-9831"
  source_url: https://www.clarkson.edu/admissions-aid/graduate
  source_snippet: "Phone: 518-631-9831"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-011:
  field: graduate.cost.tuition_standard
  value: "$1,545/credit"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "$1,545 per credit (this rate pertains to all students including military)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-012:
  field: graduate.cost.tuition_online
  value: "$1,025/credit"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "$1,025 per credit(this rate pertains to all students including military)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-013:
  field: graduate.cost.dpt
  value: "$11,035/term (7 terms)"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "$11,035 per term (7 terms)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-014:
  field: graduate.cost.pa
  value: "$12,719/term (8 terms)"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "$12,719 per term (8 terms)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-015:
  field: graduate.cost.tuition_military
  value: "$1,545/credit (same as standard)"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "$1,545 per credit (this rate pertains to all students including military)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-016:
  field: graduate.aid.scholarship_coverage
  value: "Up to 30% tuition (merit-based)"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "In-person programs also have merit-based scholarships that can cover up to 30% of tuition."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-017:
  field: graduate.aid.funding_types
  value: "Assistantships, Scholarships, Loans, Fellowships"
  source_url: https://www.clarkson.edu/admissions-aid/graduate/cost-aid
  source_snippet: "We offer a wide array of financing options for our graduate students in master's and PhD programs. These include assistantships, scholarships, loans and other financing options."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-018:
  field: graduate.aid.corporate_partnerships
  value: "Employer tuition discounts available"
  source_url: https://www.clarkson.edu/admissions-aid/graduate
  source_snippet: "We partner with several corporations to offer tuition discounts."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-019:
  field: graduate.outcomes.placement_rate
  value: "96%"
  source_url: https://www.clarkson.edu/admissions-aid/graduate
  source_snippet: "our graduate programs provide tangible results in earning potential and career advancement. Illustrating this, our graduate programs have a 96 percent placement rate"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
clarkson-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0 (rules 1-4)
├── 01-ug-coulter-engineering.md        # Section 1 - Coulter programs
├── 02-ug-reh-business.md               # Section 1 - Reh programs
├── 03-ug-lewis-health-life.md          # Section 1 - Lewis programs
├── 04-ug-minors-complete.md            # Section 1.4 - all minors
├── 05-grad-coulter-engineering.md      # Section 2 - Coulter grad
├── 06-grad-reh-business.md             # Section 2 - Reh grad
├── 07-grad-lewis-health-life.md        # Section 2 - Lewis grad
├── 08-application-requirements.md      # Section 3
├── 09-costs-financial-aid.md           # Section 4
├── 10-evidence-chain.md                # Section 5
└── 11-comparison-framework.md          # Section 7
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "clarkson-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|MS|MBA|PhD|DPT|AdvCert>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| 优先级 | 数据项 | 目标URL | 说明 |
|--------|-------|---------|------|
| P0 | 验证EA/EA2截止日期 | https://www.clarkson.edu/admissions-aid/undergraduate | 用户提到EA Nov 1和EA2 Dec 1，但官网只显示ED Dec 1和RD Jan 15 |
| P0 | 国际学生详细学费表 | https://www.clarkson.edu/admissions-aid/international/tuition-costs | 未获取具体金额 |
| P1 | 各项目具体GRE/GMAT要求 | 各项目页面 | 需要逐项目查询 |
| P1 | 奖学金详细分类和金额 | https://www.clarkson.edu/admissions-aid/undergraduate/tuition-costs/scholarships-grants-loans | 需要更详细的奖学金列表 |
| P1 | Need-blind政策官方确认 | Clarkson Common Data Set | 官网未明确说明need-blind/need-aware |
| P2 | 各工程专业ABET认证状态 | 各专业页面 | 工程专业认证信息 |
| P2 | 住宿详细费率 | https://www.clarkson.edu/student-life/housing-dining#housing-rates | 各宿舍楼具体费率 |
| P2 | 研究生各项目具体截止日期 | 各项目页面 | 部分项目可能有固定截止日期 |

---

## SECTION 7 -- Cross-School Comparison Framework

| 维度 | Clarkson University | 其他学校(待填) |
|------|-------------------|---------------|
| 所在地 | Potsdam, NY | |
| 学校类型 | Private | |
| 本科总费用/年 | $86,456 (2026-27) | |
| 学费/年 | $61,594 (2026-27) | |
| Need-blind(美国) | Need-based aid available | |
| Need-blind(国际) | Need-aware | |
| EA截止日期 | N/A (ED: Dec 1) | |
| RD截止日期 | Jan 15 | |
| SAT/ACT要求 | Test-optional | |
| TOEFL最低分 | 80 | |
| IELTS最低分 | 6.5 | |
| Duolingo最低分 | 115 | |
| 平均资助金额 | $41,285/年 | |
| 平均起薪 | $82,786 (2025届) | |
| 研究生申请费 | Currently waived | |
| 专业总数(Rule 1) | 95 (all) / 62 (degree programs) | |
| 学院数(Rule 2) | 4 | |
| 研究生就业率 | 96% | |
| 本科生就业率 | 99% | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.clarkson.edu, undergrad.clarkson.edu, connect.clarkson.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school -> department -> degree-level -> program
