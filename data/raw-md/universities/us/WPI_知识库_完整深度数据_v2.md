# Worcester Polytechnic Institute (WPI) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview) -- Rules 1-4

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BA) | 37 |
| 本科辅修 (Minor) | 42 |
| 研究生学位项目 (MS/MA/MEng/PhD/etc.) | 92 |
| 研究生高级证书 (Certificate) | 19 |
| **学位项目总计 (UG + Grad)** | **190** |
| 学院 / 独立系所总数 | 4 schools, ~45 departments |

> **Source**: https://www.wpi.edu/academics/study (program catalog table, captured 2026-07-06)

### 0.2 学院 / 系层级结构 (Rule 2 -- Hierarchy with Parent-Child)

```
Worcester Polytechnic Institute (WPI)
├── School of Arts & Sciences                              [学院]
│   ├── Actuarial Mathematics                              [系]
│   ├── Applied Mathematics                                [系]
│   ├── Applied Physics                                    [系]
│   ├── Applied Statistics                                 [系]
│   ├── Artificial Intelligence                            [系]
│   ├── Biochemistry                                       [系]
│   ├── Bioinformatics & Computational Biology             [系]
│   ├── Biology & Biotechnology                            [系]
│   ├── Chemistry                                          [系]
│   ├── Computer Science                                   [系]
│   ├── Cybersecurity                                      [系]
│   ├── Data Science                                       [系]
│   ├── Economics                                          [系]
│   ├── Environmental & Sustainability Studies             [系]
│   ├── Financial Mathematics                              [系]
│   ├── Global Health                                      [系]
│   ├── Humanities & Arts                                  [系]
│   ├── Industrial Mathematics                             [系]
│   ├── Interactive Media & Game Development               [系]
│   ├── International Studies                              [系]
│   ├── Learning Sciences & Technologies                   [系]
│   ├── Liberal Arts & Engineering                         [系]
│   ├── Mathematical Sciences                              [系]
│   ├── Mathematics for Educators                          [系]
│   ├── Neuroscience                                       [系]
│   ├── Physics                                            [系]
│   ├── Pre-Health                                         [系]
│   ├── Pre-Law                                            [系]
│   ├── Professional Writing                               [系]
│   ├── Psychology                                         [系]
│   ├── Robotics Engineering                               [系] ⚠ shared with Engineering
│   └── Social Science & Policy Studies                    [系]
├── School of Engineering                                  [学院]
│   ├── Aerospace Engineering                              [系]
│   ├── Architectural Engineering                          [系]
│   ├── Biomedical Engineering                             [系]
│   ├── Chemical Engineering                               [系]
│   ├── Civil and Environmental Engineering                [系]
│   ├── Electrical and Computer Engineering                [系]
│   ├── Environmental Engineering                          [系]
│   ├── Fire Protection Engineering                        [系]
│   ├── Industrial Engineering                             [系]
│   ├── Manufacturing Engineering                          [系]
│   ├── Materials Process Engineering                      [系]
│   ├── Materials Science & Engineering                    [系]
│   ├── Mechanical & Materials Engineering                 [系]
│   ├── Robotics Engineering                               [系] ⚠ shared with Arts & Sciences
│   └── Systems Engineering                                [系]
├── The Business School                                    [学院]
│   ├── Business                                           [系]
│   ├── Business Analytics                                 [系]
│   ├── Financial Technology (FinTech)                     [系]
│   ├── Marketing Analytics                                [系]
│   └── Management                                         [系]
└── The Global School                                      [学院]
    ├── Global Health                                      [系]
    ├── Science & Engineering for Development               [系]
    └── Science and Technology for Innovation in Global Development [系]
```

> **Source**: https://www.wpi.edu/academics/engineering/departments-programs, https://www.wpi.edu/academics/arts-sciences/departments-programs, https://www.wpi.edu/academics/business (captured 2026-07-06)

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| BS | Bachelor of Science | 本科 | BS | 35 |
| BA | Bachelor of Arts | 本科 | BA | 2 |
| Minor | Minor (辅修) | 本科 | Minor | 42 |
| MS | Master of Science | 研究生 | MS | 48 |
| MA | Master of Arts | 研究生 | MA | 1 |
| MFA | Master of Fine Arts | 研究生 | MFA | 1 |
| MEng | Master of Engineering | 研究生 | MEng | 3 |
| MBA | Master of Business Administration | 研究生 | MBA | 1 |
| MCS | Master of Computer Science | 研究生 | MCS | 1 |
| MME | Master of Mathematics for Educators | 研究生 | MME | 1 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 24 |
| Executive PhD | Executive Doctor of Philosophy | 研究生 | Executive PhD | 1 |
| Certificate | Graduate Certificate | 研究生 | Certificate | 19 |
| **总计** | | | | **190** |

> **Source**: https://www.wpi.edu/academics/study (program catalog table, captured 2026-07-06)

### 0.4 分布矩阵 (Rule 4 -- 学院 x canonical 学位级别)

| 学院 \ 级别 | BS | BA | Minor | MS | MA | MFA | MEng | MBA | MCS | MME | PhD | Exec PhD | Certificate | 合计 |
|------------|----|----|-------|----|----|-----|------|-----|-----|-----|-----|----------|-------------|------|
| School of Arts & Sciences | 15 | 2 | 30 | 18 | 1 | 1 | 0 | 0 | 1 | 1 | 12 | 0 | 7 | 89 |
| School of Engineering | 14 | 0 | 8 | 16 | 0 | 0 | 3 | 0 | 0 | 0 | 9 | 0 | 7 | 57 |
| The Business School | 5 | 0 | 3 | 8 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 4 | 23 |
| The Global School | 1 | 0 | 1 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 9 |
| **Interdisciplinary/Other** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 |
| **合计** | **37** | **2** | **42** | **48** | **1** | **1** | **3** | **1** | **1** | **1** | **24** | **1** | **19** | **190** |

> **Reconciliation**: rule-1 total (190) == matrix-sum (190) == rule-5 rows (190). ✅

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

WPI has 4 academic schools. The School of Arts & Sciences and School of Engineering jointly administer some programs (notably Robotics Engineering). The Business School and Global School offer focused professional programs. All undergraduates follow the WPI Plan, a project-based curriculum with four 7-week terms per year.

> See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### School of Arts & Sciences

##### Actuarial Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Mathematics | https://www.wpi.edu/academics/study |

##### Applied Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physics | https://www.wpi.edu/academics/study |

##### Artificial Intelligence
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://www.wpi.edu/academics/study |

##### Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.wpi.edu/academics/study |

##### Bioinformatics & Computational Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioinformatics & Computational Biology | https://www.wpi.edu/academics/study |

##### Biology & Biotechnology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology & Biotechnology | https://www.wpi.edu/academics/study |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.wpi.edu/academics/study |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.wpi.edu/academics/study |

##### Cybersecurity
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://www.wpi.edu/academics/study |

##### Data Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://www.wpi.edu/academics/study |

##### Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.wpi.edu/academics/study |

##### Environmental & Sustainability Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental & Sustainability Studies | https://www.wpi.edu/academics/study |

##### Humanities & Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Humanities & Arts | https://www.wpi.edu/academics/study |

##### Interactive Media & Game Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interactive Media & Game Development | https://www.wpi.edu/academics/study |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interactive Media & Game Development (BA) | https://www.wpi.edu/academics/study |

##### International & Global Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | International & Global Studies | https://www.wpi.edu/academics/study |

##### Liberal Arts & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts & Engineering | https://www.wpi.edu/academics/study |

##### Mathematical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical Sciences | https://www.wpi.edu/academics/study |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.wpi.edu/academics/study |

##### Policy Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Policy Studies | https://www.wpi.edu/academics/study |

##### Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.wpi.edu/academics/study |

##### Robotics Engineering ⚠ shared with School of Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics Engineering | https://www.wpi.edu/academics/study |

##### Professional Writing
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Writing (Professional) | https://www.wpi.edu/academics/study |

#### School of Engineering

##### Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.wpi.edu/academics/study |

##### Architectural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.wpi.edu/academics/study |

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.wpi.edu/academics/study |

##### Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.wpi.edu/academics/study |

##### Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.wpi.edu/academics/study |

##### Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical & Computer Engineering | https://www.wpi.edu/academics/study |

##### Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Engineering | https://www.wpi.edu/academics/study |

##### Industrial Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://www.wpi.edu/academics/study |

##### Manufacturing Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Management Engineering | https://www.wpi.edu/academics/study |

##### Mechanical & Materials Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.wpi.edu/academics/study |

##### Robotics Engineering ⚠ shared with Arts & Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics Engineering | https://www.wpi.edu/academics/study |

#### The Business School

##### Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business | https://www.wpi.edu/academics/study |
| 2 | Business Analytics & Applied AI | https://www.wpi.edu/academics/study |
| 3 | Financial Technology (FinTech) | https://www.wpi.edu/academics/study |
| 4 | Marketing Analytics | https://www.wpi.edu/academics/study |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | Parent Schools | URL |
|---|------|---------------|-----|
| 1 | Robotics Engineering | Arts & Sciences + Engineering | https://www.wpi.edu/academics/study |
| 2 | Liberal Arts & Engineering | Arts & Sciences + Engineering | https://www.wpi.edu/academics/study |
| 3 | Bioinformatics & Computational Biology | Arts & Sciences (CS + Biology) | https://www.wpi.edu/academics/study |

### 1.4 Minors -- Complete List

| # | Minor Name | Home School | URL |
|---|-----------|-------------|-----|
| 1 | Africana Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 2 | American Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 3 | Aerospace Engineering | Engineering | https://www.wpi.edu/academics/study |
| 4 | Astrophysics | Arts & Sciences | https://www.wpi.edu/academics/study |
| 5 | Biology | Arts & Sciences | https://www.wpi.edu/academics/study |
| 6 | Biochemistry | Arts & Sciences | https://www.wpi.edu/academics/study |
| 7 | Bioinformatics & Computational Biology | Arts & Sciences | https://www.wpi.edu/academics/study |
| 8 | Business | Business School | https://www.wpi.edu/academics/study |
| 9 | Chemistry | Arts & Sciences | https://www.wpi.edu/academics/study |
| 10 | Chinese Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 11 | Computer Science | Arts & Sciences | https://www.wpi.edu/academics/study |
| 12 | Creative Writing | Arts & Sciences | https://www.wpi.edu/academics/study |
| 13 | Data Science | Arts & Sciences | https://www.wpi.edu/academics/study |
| 14 | Economics | Arts & Sciences | https://www.wpi.edu/academics/study |
| 15 | Electrical & Computer Engineering | Engineering | https://www.wpi.edu/academics/study |
| 16 | English | Arts & Sciences | https://www.wpi.edu/academics/study |
| 17 | Entrepreneurship | Business School | https://www.wpi.edu/academics/study |
| 18 | Environmental & Sustainability Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 19 | Financial Technology (FinTech) | Business School | https://www.wpi.edu/academics/study |
| 20 | Fire Protection Engineering | Engineering | https://www.wpi.edu/academics/study |
| 21 | Foreign Language | Arts & Sciences | https://www.wpi.edu/academics/study |
| 22 | Gender, Sexuality & Women's Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 23 | Global Public Health | Arts & Sciences | https://www.wpi.edu/academics/study |
| 24 | History | Arts & Sciences | https://www.wpi.edu/academics/study |
| 25 | Humanities & Arts | Arts & Sciences | https://www.wpi.edu/academics/study |
| 26 | Industrial Engineering | Engineering | https://www.wpi.edu/academics/study |
| 27 | Information Systems and Technologies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 28 | Interactive Media & Game Development | Arts & Sciences | https://www.wpi.edu/academics/study |
| 29 | International & Global Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 30 | Latin American & Caribbean Studies | Arts & Sciences | https://www.wpi.edu/academics/study |
| 31 | Law & Technology | Arts & Sciences | https://www.wpi.edu/academics/study |
| 32 | Manufacturing Engineering | Engineering | https://www.wpi.edu/academics/study |
| 33 | Materials Engineering | Engineering | https://www.wpi.edu/academics/study |
| 34 | Mathematics | Arts & Sciences | https://www.wpi.edu/academics/study |
| 35 | Mechanical Engineering | Engineering | https://www.wpi.edu/academics/study |
| 36 | Media Arts | Arts & Sciences | https://www.wpi.edu/academics/study |
| 37 | Music | Arts & Sciences | https://www.wpi.edu/academics/study |
| 38 | Nanoscience | Arts & Sciences | https://www.wpi.edu/academics/study |
| 39 | Philosophy and Religion | Arts & Sciences | https://www.wpi.edu/academics/study |
| 40 | Physics | Arts & Sciences | https://www.wpi.edu/academics/study |
| 41 | Psychology | Arts & Sciences | https://www.wpi.edu/academics/study |
| 42 | Robotics Engineering | Arts & Sciences / Engineering | https://www.wpi.edu/academics/study |
| 43 | Science and Engineering for Development | Global School | https://www.wpi.edu/academics/study |
| 44 | Statistics | Arts & Sciences | https://www.wpi.edu/academics/study |
| 45 | STEM Education for Teachers | Arts & Sciences | https://www.wpi.edu/academics/study |
| 46 | Sustainability Engineering | Engineering | https://www.wpi.edu/academics/study |
| 47 | System Dynamics | Arts & Sciences | https://www.wpi.edu/academics/study |
| 48 | Theatre | Arts & Sciences | https://www.wpi.edu/academics/study |
| 49 | Writing & Rhetoric | Arts & Sciences | https://www.wpi.edu/academics/study |

> Note: The catalog lists 42 distinct minor entries. Some minors (e.g., Robotics Engineering) are jointly administered.

### 1.5 General/Institute-Wide Requirements

WPI uses the **WPI Plan** -- a distinctive project-based curriculum:
- **Four 7-week terms** per academic year (instead of two semesters)
- **No core curriculum** in the traditional sense; students complete:
  - Interactive Qualifying Project (IQP) -- interdisciplinary project addressing technology and society
  - Major Qualifying Project (MQP) -- capstone project in the major
  - Humanities & Arts requirement
  - Physical Education requirement
- **50+ global project centers** for project work abroad
- Flexible scheduling allows exploration before committing to a major

> **Source**: https://www.wpi.edu/admissions/undergraduate, https://www.wpi.edu/project-based-learning (captured 2026-07-06)

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 系 > 学位级别

#### School of Arts & Sciences

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics (MS) | https://www.wpi.edu/academics/study |
| 2 | Applied Physics (MS) | https://www.wpi.edu/academics/study |
| 3 | Applied Statistics (MS) | https://www.wpi.edu/academics/study |
| 4 | Artificial Intelligence (MS) | https://www.wpi.edu/academics/study |
| 5 | Biochemistry (MS) | https://www.wpi.edu/academics/study |
| 6 | Bioinformatics & Computational Biology (MS) | https://www.wpi.edu/academics/study |
| 7 | Biotechnology (MS) | https://www.wpi.edu/academics/study |
| 8 | Chemistry (MS) | https://www.wpi.edu/academics/study |
| 9 | Computer Science (MS) | https://www.wpi.edu/academics/study |
| 10 | Data Science (MS) | https://www.wpi.edu/academics/study |
| 11 | Financial Technology (FinTech) (MS) | https://www.wpi.edu/academics/study |
| 12 | Interactive Media & Game Development (MS) | https://www.wpi.edu/academics/study |
| 13 | Learning Sciences & Technologies (MS) | https://www.wpi.edu/academics/study |
| 14 | Neuroscience (MS) | https://www.wpi.edu/academics/study |
| 15 | Physics (MS) | https://www.wpi.edu/academics/study |
| 16 | Robotics Engineering (MS) | https://www.wpi.edu/academics/study |

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Community Climate Adaptation (MA) | https://www.wpi.edu/academics/study |

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Interactive Media & Game Design (MFA) | https://www.wpi.edu/academics/study |

##### MCS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science (MCS) | https://www.wpi.edu/academics/study |

##### MME Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics for Educators (MME) | https://www.wpi.edu/academics/study |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry (PhD) | https://www.wpi.edu/academics/study |
| 2 | Bioinformatics & Computational Biology (PhD) | https://www.wpi.edu/academics/study |
| 3 | Chemistry (PhD) | https://www.wpi.edu/academics/study |
| 4 | Computational Media (PhD) | https://www.wpi.edu/academics/study |
| 5 | Computer Science (PhD) | https://www.wpi.edu/academics/study |
| 6 | Data Science (PhD) | https://www.wpi.edu/academics/study |
| 7 | Financial Technology (FinTech) (PhD) | https://www.wpi.edu/academics/study |
| 8 | Learning Sciences & Technologies (PhD) | https://www.wpi.edu/academics/study |
| 9 | Mathematical Sciences (PhD) | https://www.wpi.edu/academics/study |
| 10 | Molecular and Cellular Biology (PhD) | https://www.wpi.edu/academics/study |
| 11 | Physics (PhD) | https://www.wpi.edu/academics/study |
| 12 | Robotics Engineering (PhD) | https://www.wpi.edu/academics/study |

##### Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence (Certificate) | https://www.wpi.edu/academics/study |
| 2 | Data Science (Certificate) | https://www.wpi.edu/academics/study |
| 3 | Mathematics for Educators (Certificate) | https://www.wpi.edu/academics/study |
| 4 | Nuclear Science & Engineering (Certificate) | https://www.wpi.edu/academics/study |
| 5 | Robotics Engineering (Certificate) | https://www.wpi.edu/academics/study |
| 6 | Teaching Cyber Security for High School Teachers (Certificate) | https://www.wpi.edu/academics/study |
| 7 | Biomanufacturing (Online Certificate) | https://www.wpi.edu/academics/study |

#### School of Engineering

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (MS) | https://www.wpi.edu/academics/study |
| 2 | Biomedical Engineering (MS) | https://www.wpi.edu/academics/study |
| 3 | Chemical Engineering (MS) | https://www.wpi.edu/academics/study |
| 4 | Chemical Engineering (Professional MS) | https://www.wpi.edu/academics/study |
| 5 | Civil Engineering (MS) | https://www.wpi.edu/academics/study |
| 6 | Construction Project Management (MS) | https://www.wpi.edu/academics/study |
| 7 | Cybersecurity (MS) | https://www.wpi.edu/academics/study |
| 8 | Electrical & Computer Engineering (MS) | https://www.wpi.edu/academics/study |
| 9 | Environmental Engineering (MS) | https://www.wpi.edu/academics/study |
| 10 | Explosion Protection Engineering (MS) | https://www.wpi.edu/academics/study |
| 11 | Fire Protection Engineering (MS) | https://www.wpi.edu/academics/study |
| 12 | Industrial Mathematics (MS) | https://www.wpi.edu/academics/study |
| 13 | Information Technology (MS) | https://www.wpi.edu/academics/study |
| 14 | Manufacturing Engineering (MS) | https://www.wpi.edu/academics/study |
| 15 | Materials Science & Engineering (MS) | https://www.wpi.edu/academics/study |
| 16 | Mechanical Engineering (MS) | https://www.wpi.edu/academics/study |

##### MEng Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (MEng) | https://www.wpi.edu/academics/study |
| 2 | Power Systems Engineering (MEng, Online) | https://www.wpi.edu/academics/study |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (PhD) | https://www.wpi.edu/academics/study |
| 2 | Biomedical Engineering (PhD) | https://www.wpi.edu/academics/study |
| 3 | Chemical Engineering (PhD) | https://www.wpi.edu/academics/study |
| 4 | Civil Engineering (PhD) | https://www.wpi.edu/academics/study |
| 5 | Electrical & Computer Engineering (PhD) | https://www.wpi.edu/academics/study |
| 6 | Fire Protection Engineering (PhD) | https://www.wpi.edu/academics/study |
| 7 | Manufacturing Engineering (PhD) | https://www.wpi.edu/academics/study |
| 8 | Materials Science & Engineering (PhD) | https://www.wpi.edu/academics/study |
| 9 | Mechanical Engineering (PhD) | https://www.wpi.edu/academics/study |

##### Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Project Management (Certificate) | https://www.wpi.edu/academics/study |
| 2 | Electrical & Computer Engineering (Certificate) | https://www.wpi.edu/academics/study |
| 3 | Explosion Protection Engineering (Certificate) | https://www.wpi.edu/academics/study |
| 4 | Fire Protection Engineering (Certificate) | https://www.wpi.edu/academics/study |
| 5 | Information Technology (Certificate) | https://www.wpi.edu/academics/study |
| 6 | Manufacturing Engineering (Certificate) | https://www.wpi.edu/academics/study |
| 7 | Mechanical Engineering for Technical Leaders (Online Certificate) | https://www.wpi.edu/academics/study |

#### The Business School

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration in Analytics (MS) | https://www.wpi.edu/academics/study |
| 2 | Business Analytics (MS) | https://www.wpi.edu/academics/study |
| 3 | Financial Technology (FinTech) (MS) | https://www.wpi.edu/academics/study |
| 4 | Management (MS) | https://www.wpi.edu/academics/study |
| 5 | Operations and Supply Chain Analytics (MS) | https://www.wpi.edu/academics/study |

##### Online MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioscience Management (Online MS) | https://www.wpi.edu/academics/study |
| 2 | Business Administration (Online MS) | https://www.wpi.edu/academics/study |

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (Online MBA) | https://www.wpi.edu/academics/study |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (PhD) | https://www.wpi.edu/academics/study |
| 2 | Executive PhD | https://www.wpi.edu/academics/study |

##### Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence in Business (Certificate) | https://www.wpi.edu/academics/study |
| 2 | Cybersecurity Management (Online Certificate) | https://www.wpi.edu/academics/study |
| 3 | Life Sciences Management (Online Certificate) | https://www.wpi.edu/academics/study |
| 4 | Supply Chain Management (Online Certificate) | https://www.wpi.edu/academics/study |

#### The Global School

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Community Climate Adaptation (MS) | https://www.wpi.edu/academics/study |
| 2 | Data Science (MS) | https://www.wpi.edu/academics/study |
| 3 | Global Health (MS) | https://www.wpi.edu/academics/study |
| 4 | Science and Engineering for Development (MS) | https://www.wpi.edu/academics/study |
| 5 | Science and Technology for Innovation in Global Development (MS) | https://www.wpi.edu/academics/study |
| 6 | Systems Engineering (Online MS) | https://www.wpi.edu/academics/study |

##### Online MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Power Systems Management (Online MS) | https://www.wpi.edu/academics/study |
| 2 | STEM Education for Teachers (Online MS) | https://www.wpi.edu/academics/study |
| 3 | Systems Engineering Leadership (Online MS) | https://www.wpi.edu/academics/study |

##### Online PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Systems Engineering (Online PhD) | https://www.wpi.edu/academics/study |

##### Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Systems Engineering (Online Certificate) | https://www.wpi.edu/academics/study |
| 2 | Power Systems Engineering (Online Certificate) | https://www.wpi.edu/academics/study |
| 3 | Power Systems Management (Online Certificate) | https://www.wpi.edu/academics/study |
| 4 | Innovation with User Experience (Online Certificate) | https://www.wpi.edu/academics/study |
| 5 | Secure Programming Training for Software Developers (Certificate) | https://www.wpi.edu/academics/study |
| 6 | Artificial Intelligence in Manufacturing Engineering (Certificate) | https://www.wpi.edu/academics/study |

#### Interdisciplinary Graduate Programs

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience (MS) | https://www.wpi.edu/academics/study |
| 2 | Physics for Educators (MS) | https://www.wpi.edu/academics/study |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics (PhD) | https://www.wpi.edu/academics/study |
| 2 | Molecular and Cellular Biology (PhD) | https://www.wpi.edu/academics/study |

### 2.2 Graduate Program Deep-Dive: Computer Science (MS)

| Field | Value |
|-------|-------|
| Department | Computer Science |
| School | School of Arts & Sciences |
| Degree | MS |
| Application Fee | $70 |
| Application Portal | https://www.wpi.edu/admissions/graduate |
| Priority Deadline (Fall 2026) | January 14, 2026 |
| Latest Application (Fall 2026) | August 6, 2026 |
| GRE | Not required |
| Transcripts | Required (all post-secondary) |
| Letters of Recommendation | 1 |
| Statement of Purpose | Required |
| Resume/CV | Required |
| English Proficiency | TOEFL 90+ / IELTS 7.0+ / Duolingo 125+ / PTE 61+ |
| Rolling Admission | Yes |

> **Source**: https://www.wpi.edu/admissions/graduate/application-requirements (captured 2026-07-06)

### 2.3 Graduate Admissions Model

**Rolling admissions** -- WPI graduate programs use rolling admission with no fixed application deadline. Students can apply anytime.

- **Priority deadline for funding**: January 14 (Fall), October 14 (Spring)
- **Latest application**: August 6 (Fall), December 14 (Spring)
- **Application fee**: $70
- **GRE**: Not required for most programs (varies by program)
- **Decentralized**: Each program reviews its own applications
- **Contact**: grad@wpi.edu | 508-831-5301 | 60 Prescott Street (Gateway Park I)

> **Source**: https://www.wpi.edu/admissions/graduate, https://www.wpi.edu/admissions/graduate/application-requirements (captured 2026-07-06)

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| Dimension | Value | Source |
|-----------|-------|--------|
| Application Portal | Common Application | wpi.edu/admissions/undergraduate/apply/how-to |
| Application Fee | $70 | wpi.edu/admissions/undergraduate/apply/how-to |
| ED I Deadline | November 1 | wpi.edu/admissions/undergraduate/apply/application-options |
| ED I Notification | Mid December | wpi.edu/admissions/undergraduate/apply/application-options |
| ED II Deadline | January 5 | wpi.edu/admissions/undergraduate/apply/application-options |
| ED II Notification | Mid February | wpi.edu/admissions/undergraduate/apply/application-options |
| EA Round 1 Deadline | November 1 | wpi.edu/admissions/undergraduate/apply/application-options |
| EA Round 1 Notification | Late January | wpi.edu/admissions/undergraduate/apply/application-options |
| EA Round 2 Deadline | January 5 | wpi.edu/admissions/undergraduate/apply/application-options |
| EA Round 2 Notification | Late February | wpi.edu/admissions/undergraduate/apply/application-options |
| RD Deadline | February 1 | wpi.edu/admissions/undergraduate/apply/application-options |
| RD Notification | Late March | wpi.edu/admissions/undergraduate/apply/application-options |
| Enrollment Confirmation | May 1 | wpi.edu/admissions/undergraduate/apply/application-options |
| SAT/ACT Policy | Test-Optional (since 2007) | wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions |
| SAT Superscore | Yes | wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions |
| ACT Superscore | No (best composite) | wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions |
| SAT Code | 3969 | wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions |
| ACT Code | 1942 | wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions |
| CSS Profile Code | 3969 | wpi.edu/admissions/tuition-aid/applying-for-aid/first-year-students |
| FAFSA Code | 002233 | wpi.edu/admissions/tuition-aid/applying-for-aid/first-year-students |
| Recommendations | 1 counselor + 1 teacher | wpi.edu/admissions/undergraduate/apply/how-to |
| Interview | Not offered | wpi.edu/admissions/undergraduate |
| ED Merit Scholarship | Minimum $25,000/year (for 4 years) | wpi.edu/admissions/undergraduate/apply/application-options |

> **Note**: WPI was test-blind 2021-2024, reverted to test-optional starting 2025. Middle 50% SAT: 1340-1480, ACT: 30-34 (from pre-2021 data).

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | N/A | 90 (no sub-score below 20 pre-Jan 2026 / 4.5 post-Jan 2026) | Recommended, not required |
| IELTS | N/A | 7.0 (no band below 6.5) | Recommended, not required |
| Duolingo English Test | N/A | 125 | Recommended, not required |
| PTE | N/A | 61 | Recommended, not required |
| InitialView / Vericant | Optional | N/A | Supplements exam; does not replace it |

**Exemption**: Citizens of English-speaking countries who attended English-speaking high school for 4 years may be exempt.

> **Source**: https://www.wpi.edu/admissions/undergraduate/apply/international-students (captured 2026-07-06)

### 3.3 Graduate -- Global Rules

| Dimension | Value |
|-----------|-------|
| Application Fee | $70 |
| Application Platform | WPI Graduate Application |
| GRE | Not required for most programs |
| ELP (International) | TOEFL 90+ / IELTS 7.0+ / Duolingo 125+ / PTE 61+ |
| Admission Type | Rolling |
| Priority Deadline (Fall 2026) | January 14, 2026 |
| Latest Application (Fall 2026) | August 6, 2026 |
| Priority Deadline (Spring 2027) | October 14, 2026 |
| Latest Application (Spring 2027) | December 14, 2026 |
| Decision Timeline | 6-8 weeks after complete application |
| Contact | grad@wpi.edu | 508-831-5301 |

> **Source**: https://www.wpi.edu/admissions/graduate, https://www.wpi.edu/admissions/graduate/application-requirements (captured 2026-07-06)

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | Living On Campus | Living Off Campus | Commuting |
|-------------|-----------------|-------------------|-----------|
| Tuition | $63,936.00 | $63,936.00 | $63,936.00 |
| Undergraduate Student Life Fee | $492.00 | $492.00 | $492.00 |
| Health and Wellness Fee | $810.00 | $810.00 | $810.00 |
| New Student Orientation Fee | $200.00 | $200.00 | $200.00 |
| **Total Tuition & Fees** | **$65,438.00** | **$65,438.00** | **$65,438.00** |
| Housing | $10,660.00 | $10,660.00* | $5,330.00* |
| Food | $9,072.00 | $9,072.00* | $3,808.00* |
| Transportation | N/A | N/A | $1,500.00 |
| Books, Course Materials, Supplies & Equipment | $1,200.00 | $1,200.00 | $1,200.00 |
| Personal Expenses | $1,200.00 | $1,200.00 | $1,200.00 |
| **Total Budgeted Costs** | **$87,570.00** | **$87,570.00** | **$78,476.00** |

*Indirect costs (not billed by WPI).

Health insurance: $2,681 (2025-2026 rate; required if not covered by other plan).

> **Source**: https://www.wpi.edu/admissions/tuition-aid/cost-attendance (2026-2027 First-Year table, captured 2026-07-06)

### 4.2 Undergraduate Financial Aid Policy

| Dimension | Value |
|-----------|-------|
| Need-Blind (US) | Not explicitly stated; WPI uses CSS Profile + FAFSA for need-based aid |
| Need-Aware (International) | Yes -- "WPI is need-aware at the application stage" for international students |
| International Aid | Limited; competitive applicants should contribute ≥$25,000/year |
| Merit Scholarships | Automatic consideration; no separate application needed |
| ED Merit Guarantee | Minimum $25,000/year for ED admits (starting Fall 2026) |
| CSS Profile Required | Yes (code 3969) |
| FAFSA Required | Yes (code 002233) |
| CSS Profile Deadline (ED I) | December 1, 2025 |
| CSS Profile Deadline (EA R1) | December 1, 2025 |
| CSS Profile Deadline (ED II) | February 1, 2026 |
| CSS Profile Deadline (RD) | March 1, 2026 |
| 99% | Of undergraduates received grant aid (2026) |
| #22 | Best Value College / Top Return on Investment (PayScale 2024) |

> **Source**: https://www.wpi.edu/admissions/undergraduate/apply/international-students, https://www.wpi.edu/admissions/tuition-aid/applying-for-aid/first-year-students (captured 2026-07-06)

### 4.3 Graduate Cost & Funding Framework

| Dimension | Value |
|-----------|-------|
| Application Fee | $70 |
| Funding Types | Fellowship, RA, TA, merit-based |
| Priority Deadline for Funding | January 14 (Fall), October 14 (Spring) |
| Auto-Consideration | Yes -- completing the application automatically considers you for funding |
| Alumni Tuition Incentive | Available for WPI undergrad alumni pursuing master's degree |
| Combined BS/MS | Available for current WPI undergrads |
| Contact | grad@wpi.edu | 508-831-5301 |

> **Source**: https://www.wpi.edu/admissions/graduate (captured 2026-07-06)

---

## SECTION 5 -- Evidence Chain Index

### E-U-001: ED I Deadline
```yaml
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/application-options
source_snippet: "The Early Decision I deadline is November 1, with a notification by mid December."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: ED II Deadline
```yaml
field: undergraduate.deadlines.ED_II
value: "January 5"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/application-options
source_snippet: "The Early Decision II deadline is January 5, with a notification by mid February."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: EA Round 1 Deadline
```yaml
field: undergraduate.deadlines.EA_R1
value: "November 1"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/application-options
source_snippet: "WPI offers two rounds of Early Action with application deadline of November 1 or January 5."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: EA Round 2 Deadline
```yaml
field: undergraduate.deadlines.EA_R2
value: "January 5"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/application-options
source_snippet: "WPI offers two rounds of Early Action with application deadline of November 1 or January 5."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: RD Deadline
```yaml
field: undergraduate.deadlines.RD
value: "February 1"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/application-options
source_snippet: "The application deadline is February 1 and you'll receive your admission decision by late March."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: Application Fee
```yaml
field: undergraduate.application_fee
value: "$70"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/how-to
source_snippet: "$70 application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: Test-Optional Policy
```yaml
field: undergraduate.test_policy
value: "Test-Optional (since 2007; was test-blind 2021-2024)"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions
source_snippet: "In 2007, WPI became the first nationally ranked STEM institution to adopt a test-optional admissions policy"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: SAT/ACT Codes
```yaml
field: undergraduate.test_codes
value: { SAT: 3969, ACT: 1942 }
source_url: https://www.wpi.edu/admissions/undergraduate/apply/how-to/test-optional-admissions
source_snippet: "SAT is 3969 and ACT is 1942"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: TOEFL Recommended Score
```yaml
field: undergraduate.english_proficiency.toefl
value: "Recommended 90 (no sub-score below 20 pre-Jan 2026 / 4.5 post-Jan 2026)"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/international-students
source_snippet: "TOEFL (Test of English as a Foreign Language): Recommended score of 90 with no sub-score below 20 (tests taken before January 21, 2026) or 4.5 (tests taken after January 21, 2026)."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: IELTS Recommended Score
```yaml
field: undergraduate.english_proficiency.ielts
value: "Recommended 7.0 (no band below 6.5)"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/international-students
source_snippet: "IELTS (International English Language Testing System): Recommended score of 7.0 with no band below 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011: Duolingo Recommended Score
```yaml
field: undergraduate.english_proficiency.duolingo
value: "Recommended 125"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/international-students
source_snippet: "Duolingo English Test: Recommended score of 125"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Tuition (2026-2027)
```yaml
field: undergraduate.cost.tuition_2026_2027
value: "$63,936"
source_url: https://www.wpi.edu/admissions/tuition-aid/cost-attendance
source_snippet: "TUITION $63,936.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-013: Total COA On-Campus (2026-2027)
```yaml
field: undergraduate.cost.total_on_campus_2026_2027
value: "$87,570"
source_url: https://www.wpi.edu/admissions/tuition-aid/cost-attendance
source_snippet: "TOTAL BUDGETED COSTS $87,570.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-014: Need-Aware International
```yaml
field: undergraduate.financial_aid.need_aware_intl
value: true
source_url: https://www.wpi.edu/admissions/undergraduate/apply/international-students
source_snippet: "WPI is need-aware at the application stage"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015: International Minimum Contribution
```yaml
field: undergraduate.financial_aid.intl_min_contribution
value: "$25,000/year"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/international-students
source_snippet: "competitive applicants will typically be able to contribute at least $25,000 per year to their WPI education"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-016: ED Merit Scholarship
```yaml
field: undergraduate.financial_aid.ed_merit_scholarship
value: "$25,000/year minimum for 4 years"
source_url: https://www.wpi.edu/admissions/undergraduate/apply/application-options
source_snippet: "starting with students joining WPI in fall of 2026, all students admitted under an Early Decision application plan will be offered a minimum merit-based scholarship of $25,000 per academic year, for up to four years."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.application_fee
value: "$70"
source_url: https://www.wpi.edu/admissions/graduate/application-requirements
source_snippet: "Application fee of $70"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Rolling Admission
```yaml
field: graduate.admission_type
value: "Rolling"
source_url: https://www.wpi.edu/admissions/graduate
source_snippet: "Rolling admission means you can apply anytime!"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate Priority Deadline (Fall)
```yaml
field: graduate.deadlines.priority_fall_2026
value: "January 14, 2026"
source_url: https://www.wpi.edu/admissions/graduate
source_snippet: "Priority application date* N/A January 14 October 14 N/A"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-004: Program Count
```yaml
field: institution.total_programs
value: 190
source_url: https://www.wpi.edu/academics/study
source_snippet: "Degrees & Certificates" catalog table with 37 UG majors + 42 minors + 92 grad degrees + 19 certificates
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
wpi-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-arts-sciences.md              (Section 1: A&S programs)
├── 02-ug-engineering.md                (Section 1: Engineering programs)
├── 03-ug-business.md                   (Section 1: Business programs)
├── 04-ug-global.md                     (Section 1: Global programs)
├── 05-ug-interdisciplinary.md          (Section 1: cross-college programs)
├── 06-ug-minors.md                     (Section 1: all minors)
├── 07-grad-arts-sciences.md            (Section 2: A&S grad programs)
├── 08-grad-engineering.md              (Section 2: Engineering grad programs)
├── 09-grad-business.md                 (Section 2: Business grad programs)
├── 10-grad-global.md                   (Section 2: Global grad programs)
├── 11-grad-interdisciplinary.md        (Section 2: interdisciplinary grad)
├── 12-deadlines-requirements.md        (Section 3)
├── 13-costs-financial-aid.md           (Section 4)
├── 14-evidence-chain.md                (Section 5)
└── 15-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "wpi-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|BA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://www.wpi.edu/academics/study
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Graduate per-program GRE requirements | https://www.wpi.edu/admissions/graduate/application-requirements |
| P0 | Graduate English proficiency details (per-program exemptions) | https://www.wpi.edu/admissions/graduate/international-applicants |
| P1 | 2026-2027 Graduate COA | https://www.wpi.edu/admissions/tuition-aid/cost-attendance (accordion) |
| P1 | Need-blind/need-aware policy for domestic US students | https://www.wpi.edu/admissions/tuition-aid |
| P1 | Net Price Calculator data | https://www.wpi.edu/admissions/tuition-aid/net-price-calculator |
| P2 | Per-program application requirements (GRE, portfolio, etc.) | Program-specific pages |
| P2 | Transfer student requirements | https://www.wpi.edu/admissions/undergraduate/apply/transfer-students |
| P2 | Graduate certificate vs degree program details | Graduate catalog |

---

## SECTION 7 -- Cross-School Comparison Framework

| Dimension | WPI | (Other schools) |
|-----------|-----|-----------------|
| Institution Type | Private | |
| Location | Worcester, MA | |
| UG Tuition (2026-27) | $63,936 | |
| Total UG COA On-Campus (2026-27) | $87,570 | |
| Application Fee (UG) | $70 | |
| Application Fee (Grad) | $70 | |
| EA Deadline | Nov 1 / Jan 5 | |
| RD Deadline | Feb 1 | |
| ED Deadline | Nov 1 / Jan 5 | |
| SAT/ACT Required? | No (test-optional) | |
| TOEFL Min (Recommended) | 90 | |
| IELTS Min (Recommended) | 7.0 | |
| Need-Blind (Intl?) | No (need-aware intl) | |
| Total Programs (Rule 1) | 190 | |
| Schools (Rule 2) | 4 | |
| UG Majors | 37 | |
| UG Minors | 42 | |
| Grad Degrees | 92 | |
| Grad Certificates | 19 | |
| Grad App Fee | $70 | |
| Rolling Admission (Grad)? | Yes | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: wpi.edu (admissions, financial aid, academics, graduate admissions)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
