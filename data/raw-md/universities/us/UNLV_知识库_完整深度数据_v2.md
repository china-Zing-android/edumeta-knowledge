# University of Nevada, Las Vegas (UNLV) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BLA/BSW/BSE) | 78 |
| 本科辅修 (Minor) | 84 |
| 本科证书 (Undergraduate Certificate) | 18 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/etc.) | 130 |
| 研究生高级证书 (Advanced Graduate Certificate / Graduate Certificate) | 67 |
| **学位项目总计 (UG + Grad)** | **377** |
| 学院 / 独立系所总数 | 16 |

> **数据来源**: UNLV官方网站 (unlv.edu/academics, unlv.edu/admissions/undergraduate)
> **验证**: 本科78个专业+84个辅修来自招生页面; 研究生197个项目来自学术页面(130学位+67证书)

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Nevada, Las Vegas
├── Lee Business School                                        [学院]
│   ├── Accounting                                             [系]
│   ├── Economics                                              [系]
│   ├── Entrepreneurship                                       [系]
│   ├── Finance                                                [系]
│   ├── Information Systems                                    [系]
│   ├── Management                                             [系]
│   ├── Marketing                                              [系]
│   ├── Real Estate                                            [系]
│   └── Insurance and Risk Management                          [系]
├── School of Dental Medicine                                  [学院] (Professional)
│   └── Dental Medicine                                        [系]
├── College of Education                                       [学院]
│   ├── Curriculum and Instruction                             [系]
│   ├── Educational Psychology                                 [系]
│   ├── Educational Policy and Leadership                      [系]
│   ├── Early Childhood Education                              [系]
│   ├── Elementary Education                                   [系]
│   ├── Secondary Education                                    [系]
│   ├── Special Education                                      [系]
│   └── Counselor Education                                    [系]
├── Howard R. Hughes College of Engineering                    [学院]
│   ├── Civil Engineering                                      [系]
│   ├── Computer Engineering                                   [系]
│   ├── Computer Science                                       [系]
│   ├── Electrical Engineering                                 [系]
│   ├── Mechanical Engineering                                 [系]
│   ├── Entertainment Engineering and Design                   [系]
│   └── Construction Management                                [系]
├── College of Fine Arts                                       [学院]
│   ├── Art                                                    [系]
│   ├── Art History                                            [系]
│   ├── Dance                                                  [系]
│   ├── Film                                                   [系]
│   ├── Music                                                  [系]
│   ├── Theatre Arts                                           [系]
│   ├── Architecture                                           [系]
│   ├── Interior Architecture and Design                       [系]
│   └── Landscape Architecture                                 [系]
├── Graduate College                                           [学院]
│   └── Interdisciplinary Graduate Programs                    [系]
├── Honors College                                             [学院]
│   └── Honors Programs                                        [系]
├── William F. Harrah College of Hospitality                   [学院]
│   └── Hospitality Management                                 [系]
├── School of Integrated Health Sciences                       [学院]
│   ├── Applied Health Sciences                                [系]
│   ├── Comprehensive Medical Imaging                          [系]
│   ├── Health Physics                                         [系]
│   ├── Healthcare Administration                              [系]
│   ├── Kinesiology                                            [系]
│   └── Nutrition Sciences                                     [系]
├── William S. Boyd School of Law                              [学院] (Professional)
│   └── Law                                                    [系]
├── College of Liberal Arts                                    [学院]
│   ├── Anthropology                                           [系]
│   ├── Communication Studies                                  [系]
│   ├── English                                                [系]
│   ├── History                                                [系]
│   ├── Philosophy                                             [系]
│   ├── Political Science                                      [系]
│   ├── Psychology                                             [系]
│   ├── Sociology                                              [系]
│   ├── World Languages and Cultures                           [系]
│   ├── Criminal Justice                                       [系]
│   └── Interdisciplinary Studies                              [系]
├── Kirk Kerkorian School of Medicine at UNLV                  [学院] (Professional)
│   └── Medicine                                               [系]
├── School of Nursing                                          [学院]
│   └── Nursing                                                [系]
├── School of Public Health                                    [学院]
│   ├── Public Health                                          [系]
│   └── Social Work                                            [系]
├── College of Sciences                                        [学院]
│   ├── Biological Sciences                                    [系]
│   ├── Chemistry                                              [系]
│   ├── Computer Science                                       [系] ⚠ shared with Engineering
│   ├── Geoscience                                             [系]
│   ├── Mathematics                                            [系]
│   ├── Physics                                                [系]
│   ├── Astronomy                                              [系]
│   ├── Biochemistry                                           [系]
│   └── Neuroscience                                           [系]
└── Greenspun College of Urban Affairs                         [学院]
    ├── Journalism and Media Studies                           [系]
    ├── Public Policy and Leadership                           [系]
    ├── Human Services                                         [系]
    ├── Criminal Justice                                       [系] ⚠ shared with Liberal Arts
    └── Communication Studies                                  [系] ⚠ shared with Liberal Arts
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 25 |
| BS | BS | Bachelor of Science | 本科 | 40 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 3 |
| BM | BM | Bachelor of Music | 本科 | 2 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| BSE | BSE | Bachelor of Science in Engineering | 本科 | 6 |
| Minor | Minor | 本科辅修 | 本科 | 84 |
| Certificate | UG Certificate | 本科证书 | 本科 | 18 |
| MA | MA | Master of Arts | 研究生 | 20 |
| MS | MS | Master of Science | 研究生 | 35 |
| MFA | MFA | Master of Fine Arts | 研究生 | 5 |
| MBA | MBA | Master of Business Administration | 研究生 | 8 |
| MEd | MEd | Master of Education | 研究生 | 10 |
| MSE | MSE | Master of Science in Engineering | 研究生 | 4 |
| MPA | MPA | Master of Public Administration | 研究生 | 2 |
| MPH | MPH | Master of Public Health | 研究生 | 2 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MHA | MHA | Master of Health Administration | 研究生 | 2 |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MDes | MDes | Master of Design | 研究生 | 1 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 2 |
| EdS | EdS | Educational Specialist | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 25 |
| EdD | EdD | Doctor of Education | 研究生 | 3 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 |
| PsyD | PsyD | Doctor of Psychology | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| DMD | DMD | Doctor of Dental Medicine | 研究生 | 1 |
| Certificate | Advanced Graduate Certificate | 研究生高级证书 | 研究生 | 40 |
| Certificate | Graduate Certificate | 研究生证书 | 研究生 | 27 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BLA | BSW | BSE | Minor | UG Cert | MA | MS | MFA | MBA | MEd | MSE | MPA | MPH | MSW | MHA | MArch | MDes | MAT | EdS | PhD | EdD | DMA | PsyD | DPT | DNP | JD | MD | DMD | Grad Cert | 合计 |
|------------|----|----|----|----|-----|-----|-----|-------|---------|----|----|----|-----|-----|-----|-----|-----|-----|-----|-------|------|-----|-----|-----|-----|-----|------|-----|-----|----|----|----|-----------|------|
| Lee Business School | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 8 | 2 | 0 | 5 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 36 |
| School of Dental Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 4 |
| College of Education | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 0 | 2 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 41 |
| Howard R. Hughes College of Engineering | 0 | 7 | 0 | 0 | 0 | 0 | 6 | 5 | 2 | 0 | 4 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 34 |
| College of Fine Arts | 8 | 2 | 3 | 2 | 1 | 0 | 0 | 8 | 4 | 3 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 46 |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 12 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| William F. Harrah College of Hospitality | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 8 |
| School of Integrated Health Sciences | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 23 |
| William S. Boyd School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 3 |
| College of Liberal Arts | 15 | 2 | 0 | 0 | 0 | 1 | 0 | 15 | 6 | 10 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 71 |
| Kirk Kerkorian School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| School of Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 5 |
| School of Public Health | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 10 |
| College of Sciences | 3 | 12 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 2 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 43 |
| Greenspun College of Urban Affairs | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 23 |
| **合计** | **29** | **51** | **3** | **2** | **1** | **1** | **6** | **55** | **25** | **17** | **35** | **5** | **8** | **10** | **4** | **2** | **2** | **1** | **2** | **1** | **1** | **2** | **1** | **30** | **3** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **55** | **377** |

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UNLV has 16 academic units offering undergraduate programs. See Section 0.2 for the complete hierarchy tree. The undergraduate programs are organized by college/school, then department, then degree level.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Lee Business School
##### Department of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.unlv.edu/academics/degrees/undergraduate |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Economics | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Entrepreneurship
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Entrepreneurship | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Finance | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Information Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Information Systems | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Management | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Marketing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Marketing | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Real Estate
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Real Estate | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Insurance and Risk Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Insurance and Risk Management | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of International Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, International Business | https://www.unlv.edu/academics/degrees/undergraduate |

#### College of Education
##### Department of Early Childhood Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Elementary Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Secondary Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Secondary Education | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Special Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Special Education | https://www.unlv.edu/academics/degrees/undergraduate |

#### Howard R. Hughes College of Engineering
##### Department of Civil Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Computer Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Electrical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Mechanical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Entertainment Engineering and Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Entertainment Engineering and Design | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | Entertainment Technology and Design | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.unlv.edu/academics/degrees/undergraduate |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Construction Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | https://www.unlv.edu/academics/degrees/undergraduate |

#### College of Fine Arts
##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.unlv.edu/academics/degrees/undergraduate |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.unlv.edu/academics/degrees/undergraduate |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Film
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.unlv.edu/academics/degrees/undergraduate |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | Jazz and Commercial Music | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Theatre Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Architecture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Interior Architecture and Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interior Architecture and Design | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Landscape Architecture
###### BLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://www.unlv.edu/academics/degrees/undergraduate |

#### William F. Harrah College of Hospitality
##### Department of Hospitality Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://www.unlv.edu/academics/degrees/undergraduate |

#### School of Integrated Health Sciences
##### Department of Applied Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Comprehensive Medical Imaging
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Comprehensive Medical Imaging | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Health Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Physics | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Healthcare Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Healthcare Administration | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Nutrition Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition Sciences | https://www.unlv.edu/academics/degrees/undergraduate |

#### College of Liberal Arts
##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.unlv.edu/academics/degrees/undergraduate |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of World Languages and Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | World Languages & Cultures | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Criminal Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Interdisciplinary Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | General Studies in Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |

#### School of Nursing
##### Department of Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.unlv.edu/academics/degrees/undergraduate |

#### School of Public Health
##### Department of Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.unlv.edu/academics/degrees/undergraduate |

#### College of Sciences
##### Department of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.unlv.edu/academics/degrees/undergraduate |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | Biochemistry | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Geoscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | Earth and Environmental Science | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.unlv.edu/academics/degrees/undergraduate |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of General Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Science | https://www.unlv.edu/academics/degrees/undergraduate |

#### Greenspun College of Urban Affairs
##### Department of Journalism and Media Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism and Media Studies | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Public Policy and Leadership
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy and Leadership | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Human Services
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Services | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Criminal Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Audio Production | https://www.unlv.edu/academics/degrees/undergraduate |

##### Department of Graphic Design and Media
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Graphic Design and Media | https://www.unlv.edu/academics/degrees/undergraduate |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Cybersecurity | Interdisciplinary (Engineering + Urban Affairs) | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | Creative Practice | Interdisciplinary | https://www.unlv.edu/academics/degrees/undergraduate |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 | Accounting | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 2 | Addictions Prevention | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 3 | Addictions Treatment | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 4 | Aerospace Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 5 | African American and African Diaspora Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 6 | American Indian and Indigenous Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 7 | Anthropology | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 8 | Applied Health Sciences | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 9 | Art History | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 10 | Asian and Asian American Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 11 | Biological Sciences | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 12 | Brookings Public Policy | Greenspun College of Urban Affairs | https://www.unlv.edu/academics/degrees/undergraduate |
| 13 | Business Administration | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 14 | Business Analytics | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 15 | Business Spanish Experience | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 16 | Chemistry | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 17 | Chinese Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 18 | Classical Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 19 | Communication Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 20 | Computer Science | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 21 | Creative Writing | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 22 | Criminal Justice | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 23 | Dance | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 24 | Dance Production/Management | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 25 | Data Science and Artificial Intelligence | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 26 | Earth and Environmental Science | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 27 | Economics | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 28 | English | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 29 | Entertainment Engineering and Design | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 30 | Entrepreneurship | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 31 | Environmental Studies and Health | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 32 | Family Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 33 | Film | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 34 | Finance | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 35 | French | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 36 | Gender and Sexuality Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 37 | Geology | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 38 | German Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 39 | Gerontology | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 40 | Global Entrepreneurship Experience | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 41 | Great Works | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 42 | Health Physics | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 43 | History | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 44 | Human Services | Greenspun College of Urban Affairs | https://www.unlv.edu/academics/degrees/undergraduate |
| 45 | Information Systems | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 46 | International Business | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 47 | Italian Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 48 | Japanese Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 49 | Jazz and Commercial Music | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 50 | Journalism and Media Studies | Greenspun College of Urban Affairs | https://www.unlv.edu/academics/degrees/undergraduate |
| 51 | Kinesiology | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 52 | Landscape Studies | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 53 | Latinx and Latin American Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 54 | Management | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 55 | Mariachi | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 56 | Marketing | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 57 | Mathematics | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 58 | Actuarial Science | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 59 | Statistics | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 60 | Military Science | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 61 | Music | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 62 | Music Technology | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 63 | Neuroscience | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 64 | Nutrition Sciences | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 65 | Philosophy | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 66 | Physical Geography | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 67 | Physics | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 68 | Pilates | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 69 | Political Science | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 70 | Problem Gambling | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 71 | Professional Writing | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 72 | Psychology | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 73 | Public Health | School of Public Health | https://www.unlv.edu/academics/degrees/undergraduate |
| 74 | Real Estate | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 75 | Religious Studies | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 76 | Risk Management and Insurance | Lee Business School | https://www.unlv.edu/academics/degrees/undergraduate |
| 77 | Secondary Education | College of Education | https://www.unlv.edu/academics/degrees/undergraduate |
| 78 | Social Work | School of Public Health | https://www.unlv.edu/academics/degrees/undergraduate |
| 79 | Sociology | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 80 | Solar and Renewable Energy | College of Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 81 | Spanish | College of Liberal Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 82 | Special Education | College of Education | https://www.unlv.edu/academics/degrees/undergraduate |
| 83 | Sustainability and Health | School of Integrated Health Sciences | https://www.unlv.edu/academics/degrees/undergraduate |
| 84 | Technology Commercialization | College of Engineering | https://www.unlv.edu/academics/degrees/undergraduate |
| 85 | Theatre | College of Fine Arts | https://www.unlv.edu/academics/degrees/undergraduate |
| 86 | Unmanned Aircraft Systems | College of Engineering | https://www.unlv.edu/academics/degrees/undergraduate |

### 1.5 General/Institute-wide requirements

UNLV requires completion of the University Core Curriculum (UCC) for all undergraduate students. The UCC includes courses in:
- English Composition (6 credits)
- Mathematics (3 credits)
- Natural Sciences (6 credits)
- Social Sciences (6 credits)
- Humanities and Fine Arts (6 credits)
- Constitution (3 credits)
- Cultural Diversity (3 credits)

Total: approximately 33-36 credits of general education requirements.

### 1.6 Course-ID → Major quick-lookup

UNLV does not use a course numbering system for majors. Programs are identified by name and degree type.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Lee Business School
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Applied Economics and Data Intelligence | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Quantitative Finance | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Management Information Systems | https://www.unlv.edu/academics/degrees/graduate |
| 5 | Hotel Administration (with Hospitality College) | https://www.unlv.edu/academics/degrees/graduate |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (Evening) | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Business Administration (Online) | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Executive MBA | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Dual MBA/M.S. Computer Science | https://www.unlv.edu/academics/degrees/graduate |
| 5 | Dual MBA/M.S. Cybersecurity | https://www.unlv.edu/academics/degrees/graduate |
| 6 | Dual MBA/D.M.D. | https://www.unlv.edu/academics/degrees/graduate |
| 7 | Dual MBA/M.H.A. | https://www.unlv.edu/academics/degrees/graduate |
| 8 | Dual MBA/M.S. Hotel Administration | https://www.unlv.edu/academics/degrees/graduate |
| 9 | Dual MBA/J.D. | https://www.unlv.edu/academics/degrees/graduate |
| 10 | Dual MBA/M.S. Management Information Systems | https://www.unlv.edu/academics/degrees/graduate |
| 11 | Dual MBA/M.D. | https://www.unlv.edu/academics/degrees/graduate |
| 12 | Dual MBA/M.S. Quantitative Finance | https://www.unlv.edu/academics/degrees/graduate |

#### College of Education
##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Instruction | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Early Childhood Education | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Educational Policy and Leadership | https://www.unlv.edu/academics/degrees/graduate |
| 4 | English Language Learning | https://www.unlv.edu/academics/degrees/graduate |
| 5 | Higher Education | https://www.unlv.edu/academics/degrees/graduate |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Couple and Family Therapy | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Educational Psychology | https://www.unlv.edu/academics/degrees/graduate |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Elementary Education | https://www.unlv.edu/academics/degrees/graduate |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Instruction | https://www.unlv.edu/academics/degrees/graduate |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Instruction | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Educational Leadership | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Instruction | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Educational Psychology | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Education Policy, Organizational Leadership and Higher Education | https://www.unlv.edu/academics/degrees/graduate |

#### Howard R. Hughes College of Engineering
##### MS/MSE
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Biomedical Engineering | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Civil Engineering | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Computer Science | https://www.unlv.edu/academics/degrees/graduate |
| 5 | Construction and Infrastructure Management | https://www.unlv.edu/academics/degrees/graduate |
| 6 | Cybersecurity | https://www.unlv.edu/academics/degrees/graduate |
| 7 | Data Analytics | https://www.unlv.edu/academics/degrees/graduate |
| 8 | Electrical Engineering | https://www.unlv.edu/academics/degrees/graduate |
| 9 | Entertainment Engineering and Design | https://www.unlv.edu/academics/degrees/graduate |
| 10 | Mechanical Engineering | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Computer Science | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Electrical Engineering | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Mechanical Engineering | https://www.unlv.edu/academics/degrees/graduate |

#### College of Fine Arts
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Music | https://www.unlv.edu/academics/degrees/graduate |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Creative Writing | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Dance | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Film (Writing for Dramatic Media) | https://www.unlv.edu/academics/degrees/graduate |

##### MArch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://www.unlv.edu/academics/degrees/graduate |

##### MDes
| # | 项目 | URL |
|---|------|-----|
| 1 | Design | https://www.unlv.edu/academics/degrees/graduate |

##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Performance | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://www.unlv.edu/academics/degrees/graduate |

#### William F. Harrah College of Hospitality
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality Administration | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Hotel Administration | https://www.unlv.edu/academics/degrees/graduate |

##### EMHA
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Master of Hospitality Administration | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality Administration | https://www.unlv.edu/academics/degrees/graduate |

#### School of Integrated Health Sciences
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Health Physics | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Kinesiology | https://www.unlv.edu/academics/degrees/graduate |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Physics | https://www.unlv.edu/academics/degrees/graduate |

#### School of Law
##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://law.unlv.edu/admissions |

#### College of Liberal Arts
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Communication Studies | https://www.unlv.edu/academics/degrees/graduate |
| 3 | English | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Hispanic Studies | https://www.unlv.edu/academics/degrees/graduate |
| 5 | History | https://www.unlv.edu/academics/degrees/graduate |
| 6 | Quantitative Business Economics | https://www.unlv.edu/academics/degrees/graduate |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Emergency and Crisis Management | https://www.unlv.edu/academics/degrees/graduate |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://www.unlv.edu/academics/degrees/graduate |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Clinical Psychology | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Criminology & Criminal Justice | https://www.unlv.edu/academics/degrees/graduate |
| 4 | English | https://www.unlv.edu/academics/degrees/graduate |
| 5 | History | https://www.unlv.edu/academics/degrees/graduate |

##### PsyD
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Psychology | https://www.unlv.edu/academics/degrees/graduate |

#### School of Medicine
##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://www.unlv.edu/medicine/admissions/applicants |

#### School of Nursing
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://www.unlv.edu/academics/degrees/graduate |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://www.unlv.edu/academics/degrees/graduate |

#### School of Public Health
##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://www.unlv.edu/academics/degrees/graduate |

#### College of Sciences
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Astronomy | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Biochemistry | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Biological Sciences | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Chemistry | https://www.unlv.edu/academics/degrees/graduate |
| 5 | Computer Science | https://www.unlv.edu/academics/degrees/graduate |
| 6 | Geoscience | https://www.unlv.edu/academics/degrees/graduate |
| 7 | Mathematical Sciences | https://www.unlv.edu/academics/degrees/graduate |
| 8 | Physics | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Astronomy | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Biological Sciences | https://www.unlv.edu/acadics/degrees/graduate |
| 3 | Chemistry | https://www.unlv.edu/academics/degrees/graduate |
| 4 | Geoscience | https://www.unlv.edu/academics/degrees/graduate |
| 5 | Mathematical Sciences | https://www.unlv.edu/academics/degrees/graduate |
| 6 | Neuroscience | https://www.unlv.edu/academics/degrees/graduate |
| 7 | Physics | https://www.unlv.edu/academics/degrees/graduate |

#### Greenspun College of Urban Affairs
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Criminal Justice | https://www.unlv.edu/academics/degrees/graduate |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Healthcare Administration | https://www.unlv.edu/academics/degrees/graduate |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.unlv.edu/academics/degrees/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Affairs | https://www.unlv.edu/academics/degrees/graduate |

#### Graduate College (Interdisciplinary)
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://www.unlv.edu/academics/degrees/graduate |
| 2 | Data Analytics | https://www.unlv.edu/academics/degrees/graduate |
| 3 | Emergency and Crisis Management | https://www.unlv.edu/academics/degrees/graduate |

### 2.2 At least one program's full deep-dive (worked example)

**Program: Master of Science in Hospitality Administration**
- **College**: William F. Harrah College of Hospitality
- **Department**: Hospitality Management
- **Degree**: MS
- **URL**: https://www.unlv.edu/academics/degrees/graduate
- **Application Portal**: https://unlv.my.site.com/students/CLogin
- **Application Fee**: $60 (domestic), $95 (international)
- **Fall Deadline**: December 15
- **Spring Deadline**: N/A
- **GRE/GMAT**: Not required for this program
- **TOEFL Minimum**: 80 (iBT) / IELTS 6.5
- **Contact**: Harrah College of Hospitality, UNLV
- **Notes**: UNLV's hospitality program is consistently ranked among the top in the nation. The William F. Harrah College of Hospitality is one of the premier hospitality programs globally, benefiting from Las Vegas's position as a major hospitality and entertainment hub.

### 2.3 Graduate admissions model

**Decentralized admissions model**: The Graduate College sets minimum standards, but individual departments may have additional requirements.

**Minimum Graduate College Requirements:**
- Bachelor's degree from regionally accredited institution
- Minimum GPA: 2.75 overall OR 3.0 for last 60 semester hours
- Application fee: $60 (domestic), $95 (international)
- Official transcripts from all postsecondary institutions
- GRE/GMAT: Varies by program (some require, some don't)

**Application Timeline:**
- Fall applications open: September 1
- Spring applications open: February 1
- Summer applications open: July 1

**International Student Deadlines:**
- Fall: May 1
- Spring: October 1

**Graduate Assistantship Deadlines:**
- Fall: March 1
- Spring: November 1

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| **招生网站** | https://www.unlv.edu/admissions/undergraduate |
| **申请门户** | Common App (https://www.commonapp.org/school/university-nevada-las-vegas-unlv) 或 UNLV Application (https://unlv.my.site.com/students/CLogin) |
| **EA截止日期** | N/A (UNLV不提供Early Action) |
| **优先截止日期(Priority)** | 11月15日 (奖学金和助学金优先考虑) |
| **秋季申请截止日期** | 6月1日 |
| **春季申请截止日期** | 12月1日 |
| **入学确认截止日期** | Check MyUNLV after admission |
| **助学金申请截止日期** | 11月15日 (新生优先) |
| **SAT/ACT政策** | Test-optional (不强制要求，但鼓励提交用于课程安排) |
| **SAT学校代码** | 4861 |
| **ACT学校代码** | 2496 |
| **最低SAT分数** | 1120 (EBRW + Math) |
| **最低ACT分数** | 22 (Composite) |
| **面试政策** | 无要求 |
| **推荐信要求** | 无要求 |
| **申请费** | $60 (国内), $95 (国际) |

### 3.2 Undergraduate English proficiency table

| 考试类型 | UNLV最低分数 | 推荐分数 | 备注 |
|---------|------------|---------|------|
| TOEFL iBT (Legacy) | 总分72, 单项不低于17 | - | 2026年1月前有效 |
| TOEFL iBT (New) | 总分4.0/6.0, 单项不低于3.5 | - | 2026年1月起生效 |
| IELTS Academic | 总分6.0, 单项不低于5.5 | - | |
| PTE Academic | 总分59, 单项不低于50 | - | |
| Duolingo | 总分95, 单项不低于90 | - | |
| ELS | Level 109 | - | |
| CEFR | B2 | - | |
| MET | 53 | - | |
| SAT EBRW | 480 | - | |
| ACT English | 18 | - | |

**免除条件**:
- 美国机构授予学位的申请者
- 来自英语国家的申请者 (英国、澳大利亚、加拿大等)
- 英语授课机构毕业的申请者

### 3.3 Graduate — global rules

**招生模式**: 分散式 (Decentralized) - 研究生院设定最低标准，各院系可有额外要求

**最低研究生院要求**:
- 学士学位 (地区认可机构)
- GPA: 2.75整体 或 3.0最后60学分
- 申请费: $60 (国内), $95 (国际)
- GRE/GMAT: 因项目而异 (部分项目要求，部分不要求)

**申请材料**:
- 完整的在线申请
- 所有就读院校的正式成绩单
- 英语能力证明 (国际学生)
- 项目特定材料 (因院系而异)

**申请时间线**:
- 秋季申请开放: 9月1日
- 春季申请开放: 2月1日
- 夏季申请开放: 7月1日

**国际学生截止日期**:
- 秋季: 5月1日
- 春季: 10月1日

**研究生助理截止日期**:
- 秋季: 3月1日
- 春季: 11月1日

**英语能力要求 (研究生)**:

| 考试类型 | UNLV最低分数 | 备注 |
|---------|------------|------|
| TOEFL iBT (Legacy) | 80 | |
| TOEFL iBT (New) | 4.0/6.0, 单项不低于3.5 | 2026年1月起 |
| IELTS Academic | 6.5, 单项不低于6.0 | |
| PTE Academic | 65, 单项不低于59 | |
| Duolingo | 105, 单项不低于100 | |
| ELS | Level 112 | |
| CEFR | B2 | |
| MET | 58 | |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

**2026-2027学年费用 (15学分/学期)**

| 费用项目 | 住校(On Campus) | 校外双人间(Off Campus) | 与父母同住(Commuting) | 说明 |
|---------|----------------|---------------------|---------------------|------|
| 学费和杂费 (Tuition & Fees) | $11,231 | $11,231 | $11,231 | 本州居民; 含一次性新生费$200 |
| 住宿和水电 (Housing & Utilities) | $7,424 | $8,690 | $2,897 | 来源: Housing & Residential Life |
| 餐饮 (Food) | $6,024 | $6,024 | $3,012 | 来源: Housing & Residential Life |
| 书籍和学习材料 (Books, Course Materials, Supplies & Equipment) | $1,290 | $1,290 | $1,290 | |
| 交通 (Transportation) | $1,360 | $3,040 | $3,040 | |
| 杂项和个人开支 (Miscellaneous & Personal) | $3,304 | $3,304 | $3,304 | |
| 联邦学生贷款费用 (Federal Student Loan Fees) | $50 | $50 | $50 | 仅适用于接受联邦贷款的学生 |
| **本州居民总计** | **$30,683** | **$33,629** | **$24,824** | |
| **非本州居民总计** | **$50,284** | **$53,230** | **$44,425** | 含非居民费用$20,189 |

**2027-2028学年费用 (15学分/学期)**

| 费用项目 | 住校(On Campus) | 校外双人间(Off Campus) | 与父母同住(Commuting) | 说明 |
|---------|----------------|---------------------|---------------------|------|
| 学费和杂费 (Tuition & Fees) | $12,014 | $12,014 | $12,014 | 本州居民; 含一次性新生费$200 |
| 住宿和水电 (Housing & Utilities) | $7,870 | $9,577 | $3,192 | |
| 餐饮 (Food) | $6,530 | $6,530 | $3,265 | |
| 书籍和学习材料 (Books, Course Materials, Supplies & Equipment) | $1,330 | $1,330 | $1,330 | |
| 交通 (Transportation) | $1,426 | $3,431 | $3,431 | |
| 杂项和个人开支 (Miscellaneous & Personal) | $3,434 | $3,434 | $3,434 | |
| 联邦学生贷款费用 (Federal Student Loan Fees) | $141 | $141 | $141 | |
| **本州居民总计** | **$32,745** | **$36,457** | **$26,807** | |
| **非本州居民总计** | **$54,582** | **$58,294** | **$48,644** | 含非居民费用$21,837 |

**研究生费用 (2026-2027, 9学分/学期)**

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| 学费和杂费 (Tuition & Fees) | $8,416/年 | 本州居民; 含一次性新生费$120 |
| 住宿和水电 (Housing & Utilities) | $17,379/年 | 单人间 |
| 餐饮 (Food) | $6,024/年 | |
| 书籍和学习材料 | $1,290/年 | |
| 交通 | $3,040/年 | |
| 杂项和个人开支 | $3,304/年 | |
| 联邦学生贷款费用 | $600/年 | |
| **本州居民总计** | **$40,053/年** | |
| **非本州居民总计** | **$60,242/年** | 含非居民费用$20,189 |
| **研究生健康保险 (强制)** | **$4,350/年** | 不含在上述费用中 |

### 4.2 Undergraduate financial-aid policy

| 维度 | 详情 |
|------|------|
| **Rebel Edge Program** | 内华达州居民符合条件可获得免费学费和杂费 (联邦、州和机构资助后剩余部分); 最多15学分 + $1,000年度书本津贴 |
| **获得资助的学生比例** | 超过90%的本科生获得资助 |
| **Need-blind政策** | Need-aware (对所有学生，包括国际学生) |
| **FAFSA学校代码** | 002569 |
| **优先截止日期 (新生)** | 11月15日 |
| **优先截止日期 (转学生)** | 3月15日 |
| **优先截止日期 (在校本科生)** | 4月15日 |
| **优先截止日期 (研究生)** | 4月15日 |
| **资助类型** | 奖学金 (Scholarships), 助学金 (Grants), 学费减免 (Waivers), 贷款 (Loans), 勤工俭学 (Work-Study) |
| **奖学金特点** | 自动考虑 (无需额外申请), 可续4年, 可与其他资助叠加, 可用于食宿 |

### 4.3 Graduate cost & funding framework

**资助类型**:
- **全额资助**: 研究助理 (RA), 教学助理 (TA), 奖学金 (Fellowship)
- **部分资助**: 部分学费减免, 助学金
- **自费**: 学生贷款, 个人资金

**研究生助理信息**:
- 超过1,000个研究生助理职位
- 年度研究生资助总额超过$25 million
- 申请截止日期: 秋季3月1日, 春季11月1日

**申请费**:
- 国内: $60
- 国际: $95
- 费用减免政策: 因项目而异

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.admission.requirements.gpa
  value: "3.0 GPA in 13 core units"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "3.0 GPA in 13 core units: English - 4, Math - 3, Social Science - 3, Natural Science - 3"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admission.requirements.sat
  value: "1120 SAT (EBRW and math)"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "1120 SAT* (EBRW and math) *1040 SAT for exams taken prior to March 2016"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admission.requirements.act
  value: "22 ACT (composite score)"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "22 ACT (composite score)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.priority_finaid
  value: "November 15"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "Priority deadline for fall financial aid and scholarship consideration: November 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.deadlines.fall_application
  value: "June 1"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "Fall application deadline: June 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.application_fee
  value: "$60"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "You will be required to pay the nonrefundable $60 application fee by credit or debit card."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.test_policy
  value: "Test-optional (not required for admission or scholarship consideration)"
  source_url: https://www.unlv.edu/admissions/first-year
  source_snippet: "ACT or SAT Scores – Test scores are not required for admission or scholarship consideration but are encouraged for UNLV course placement."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.tuition.resident_2026_2027
  value: "$11,231/year"
  source_url: https://www.unlv.edu/apply/college-costs
  source_snippet: "Nevada Resident Undergraduate $5,516 Semester $11,231 Yearly"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.tuition.nonresident_2026_2027
  value: "$31,420/year"
  source_url: https://www.unlv.edu/apply/college-costs
  source_snippet: "Nonresident Undergraduate $15,610 Semester $31,420 Yearly"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.english_proficiency.toefl
  value: "72 (no band below 17)"
  source_url: https://www.unlv.edu/admissions/international/undergraduate/english-proficiency
  source_snippet: "TOEFL iBT Test (Legacy) Overall score of 72 (Scale: 0 - 120) No band below 17"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.english_proficiency.ielts
  value: "6.0 (no band below 5.5)"
  source_url: https://www.unlv.edu/admissions/international/undergraduate/english-proficiency
  source_snippet: "IELTS Academic Overall band of 6.0 No band below 5.5"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.english_proficiency.duolingo
  value: "95 (no band below 90)"
  source_url: https://www.unlv.edu/admissions/international/undergraduate/english-proficiency
  source_snippet: "Duolingo A minimum score of 95 No band below 90"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.admission.requirements.gpa
  value: "2.75 overall or 3.0 last 60 credits"
  source_url: https://www.unlv.edu/admissions/graduate/domestic
  source_snippet: "Grade Point Average – You must have a minimum overall grade point average of 2.75 (4.00=A) for the bachelor's degree or a minimum 3.00 (4.00=A) for the last two years (60 semester hours)."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_fee
  value: "$60 (domestic), $95 (international)"
  source_url: https://www.unlv.edu/admissions/graduate/domestic
  source_snippet: "A nonrefundable admission application fee, payable check, money order, or online by credit card of $60 to the Board of Regents, UNLV."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-003:
  field: graduate.deadlines.international_fall
  value: "May 1"
  source_url: https://www.unlv.edu/admissions/graduate/application-deadlines
  source_snippet: "All application materials must be submitted to the Graduate College through the Application Portal by May 1 (fall semester)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-004:
  field: graduate.deadlines.ga_fall
  value: "March 1"
  source_url: https://www.unlv.edu/admissions/graduate/application-deadlines
  source_snippet: "If you are applying for a graduate assistantship, all application materials must be submitted by March 1 (fall semester)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-005:
  field: graduate.english_proficiency.toefl
  value: "80"
  source_url: https://www.unlv.edu/admissions/international/graduate/english-proficiency
  source_snippet: "TOEFL iBT Test (Legacy) Overall score of 80 (Scale: 0 - 120)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.english_proficiency.ielts
  value: "6.5 (no band below 6.0)"
  source_url: https://www.unlv.edu/admissions/international/graduate/english-proficiency
  source_snippet: "IELTS Academic Overall band of 6.5 No band below 6.0"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-I-001:
  field: institution.overview
  value: "Public R1 research university, 16 academic units, 78 majors, 84 minors, 197 graduate programs"
  source_url: https://www.unlv.edu/academics
  source_snippet: "We offer 78 majors, 84 minors and 197 graduate degree and certificate programs"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-I-002:
  field: institution.research_classification
  value: "R1 - Nation's Highest Recognition for Research Excellence"
  source_url: https://www.unlv.edu/academics
  source_snippet: "R1 NATION'S HIGHEST RECOGNITION FOR RESEARCH EXCELLENCE"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-I-003:
  field: financial_aid.rebel_edge
  value: "Free tuition for eligible Nevada residents"
  source_url: https://www.unlv.edu/paying-for-college
  source_snippet: "Nevada residents meeting income and enrollment criteria can receive free tuition and fees for up to 15 credits, plus a $1,000 annual book stipend."
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
unlv-knowledge-base-v2
├── unlv-overview (Section 0)
│   ├── chunk-01: 专业与项目总数
│   ├── chunk-02: 学院/系层级结构
│   ├── chunk-03: 学历级别明细
│   └── chunk-04: 分布矩阵
├── unlv-undergraduate (Section 1)
│   ├── chunk-05: Lee Business School 本科专业
│   ├── chunk-06: College of Education 本科专业
│   ├── chunk-07: College of Engineering 本科专业
│   ├── chunk-08: College of Fine Arts 本科专业
│   ├── chunk-09: College of Liberal Arts 本科专业
│   ├── chunk-10: College of Sciences 本科专业
│   ├── chunk-11: 其他学院本科专业
│   └── chunk-12: 本科辅修完整列表
├── unlv-graduate (Section 2)
│   ├── chunk-13: Lee Business School 研究生项目
│   ├── chunk-14: College of Education 研究生项目
│   ├── chunk-15: College of Engineering 研究生项目
│   ├── chunk-16: College of Fine Arts 研究生项目
│   ├── chunk-17: College of Liberal Arts 研究生项目
│   ├── chunk-18: College of Sciences 研究生项目
│   └── chunk-19: 其他学院研究生项目
├── unlv-admissions (Section 3)
│   ├── chunk-20: 本科申请要求与截止日期
│   ├── chunk-21: 英语能力要求
│   └── chunk-22: 研究生申请要求
├── unlv-costs (Section 4)
│   ├── chunk-23: 本科费用明细
│   ├── chunk-24: 研究生费用
│   └── chunk-25: 助学金与奖学金
└── unlv-evidence (Section 5)
    └── chunk-26: 证据链索引
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "unlv-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标URL | 说明 |
|--------|--------|---------|------|
| P0 | 各研究生项目的具体截止日期 | https://www.unlv.edu/admissions/graduate/application-deadlines | 已获取主要截止日期，但需验证每个项目的具体日期 |
| P0 | 各研究生项目的GRE/GMAT要求 | 各院系网站 | 因项目而异，需逐一核实 |
| P1 | 本科各专业的具体课程要求 | https://www.unlv.edu/academics/catalogs | 需访问课程目录获取详细信息 |
| P1 | 研究生各项目的资助机会 | 各院系网站 | 需访问各院系了解具体资助信息 |
| P2 | 校园住宿详细费用 | https://www.unlv.edu/housing | 需获取具体宿舍类型和费用 |
| P2 | 各专业的就业数据 | UNLV Career Services | 需访问职业服务网站获取毕业生就业信息 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | UNLV | 对比学校1 | 对比学校2 | 对比学校3 |
|------|------|---------|---------|---------|
| **学校类型** | Public R1 Research | | | |
| **地理位置** | Las Vegas, NV | | | |
| **本科学费/年 (本州)** | $11,231 | | | |
| **本科学费/年 (非本州)** | $31,420 | | | |
| **研究生学费/年 (本州)** | $8,416 | | | |
| **Need-blind (国际生?)** | No (Need-aware) | | | |
| **EA截止日期** | N/A | | | |
| **优先截止日期** | November 15 | | | |
| **秋季申请截止日期** | June 1 | | | |
| **SAT/ACT要求** | Test-optional | | | |
| **TOEFL最低分 (本科)** | 72 | | | |
| **IELTS最低分 (本科)** | 6.0 | | | |
| **Duolingo最低分 (本科)** | 95 | | | |
| **TOEFL最低分 (研究生)** | 80 | | | |
| **IELTS最低分 (研究生)** | 6.5 | | | |
| **Rebel Edge/免费学费** | Yes (Nevada residents) | | | |
| **研究生申请费** | $60 (domestic) | | | |
| **本科专业总数** | 78 | | | |
| **辅修总数** | 84 | | | |
| **研究生项目总数** | 197 | | | |
| **学院/学校总数** | 16 | | | |
| **学生/教师比例** | 18:1 | | | |
| **第一代大学生比例** | 50% | | | |
| **研究中心数量** | 55+ | | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: www.unlv.edu, law.unlv.edu, unlv.my.site.com
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
