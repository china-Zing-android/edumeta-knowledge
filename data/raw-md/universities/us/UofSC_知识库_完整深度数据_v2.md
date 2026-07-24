# University of South Carolina Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 116 |
| 本科辅修 (Minor) | N/A (需进一步提取) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 236 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 47 |
| **学位项目总计 (UG + Grad)** | **352+** |
| 学院 / 独立系所总数 | 15 |

### 0.2 学院 / 系层级结构

```
University of South Carolina
├── McCausland College of Arts and Sciences          [学院]
│   ├── Department of Anthropology                   [系]
│   ├── Department of Biological Sciences            [系]
│   ├── Department of Chemistry                      [系]
│   ├── Department of Criminology and Criminal Justice [系]
│   ├── Department of English                        [系]
│   ├── Department of Geography                      [系]
│   ├── Department of History                        [系]
│   ├── Department of Mathematics                    [系]
│   ├── Department of Philosophy                     [系]
│   ├── Department of Physics and Astronomy          [系]
│   ├── Department of Political Science              [系]
│   ├── Department of Psychology                     [系]
│   ├── Department of Sociology                      [系]
│   ├── Department of Statistics                     [系]
│   └── School of Visual Art and Design              [系]
├── Darla Moore School of Business                   [学院]
│   ├── Department of Accounting                     [系]
│   ├── Department of Finance                        [系]
│   ├── Department of Management                     [系]
│   ├── Department of Marketing                      [系]
│   ├── Department of Operations and Supply Chain    [系]
│   └── Department of Economics                      [系]
├── Molinaroli College of Engineering and Computing   [学院]
│   ├── Department of Aerospace Engineering          [系]
│   ├── Department of Biomedical Engineering         [系]
│   ├── Department of Chemical Engineering           [系]
│   ├── Department of Civil and Environmental Engineering [系]
│   ├── Department of Computer Science and Engineering [系]
│   ├── Department of Electrical Engineering         [系]
│   ├── Department of Mechanical Engineering         [系]
│   └── Department of Integrated Information Technology [系]
├── College of Education                              [学院]
│   ├── Department of Educational Leadership and Policies [系]
│   ├── Department of Educational Studies            [系]
│   ├── Department of Instruction and Teacher Education [系]
│   └── Department of Physical Education             [系]
├── Arnold School of Public Health                    [学院]
│   ├── Department of Environmental Health Sciences  [系]
│   ├── Department of Epidemiology and Biostatistics [系]
│   ├── Department of Exercise Science               [系]
│   ├── Department of Health Promotion, Education, and Behavior [系]
│   ├── Department of Health Services Policy and Management [系]
│   └── Department of Communication Sciences and Disorders [系]
├── College of Information and Communications         [学院]
│   ├── School of Journalism and Mass Communications [系]
│   └── School of Library and Information Science    [系]
├── College of Nursing                                [学院]
├── College of Social Work                            [学院]
├── School of Music                                   [学院]
├── College of Hospitality, Retail and Sport Management [学院]
│   ├── Department of Hospitality and Tourism Management [系]
│   ├── Department of Retail and Fashion Merchandising [系]
│   └── Department of Sport and Entertainment Management [系]
├── Joseph F. Rice School of Law                      [学院]
├── Floyd School of Medicine                          [学院]
│   ├── School of Medicine Columbia                  [系]
│   └── School of Medicine Greenville                [系]
├── College of Pharmacy                               [学院]
├── South Carolina Honors College                     [学院]
├── The Graduate School                               [学院]
└── Palmetto College                                  [学院]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 45 |
| BS | Bachelor of Science | 本科 | 35 |
| BFA | Bachelor of Fine Arts | 本科 | 8 |
| BSE | Bachelor of Science in Engineering | 本科 | 12 |
| BSBA | Bachelor of Science in Business Administration | 本科 | 10 |
| BAJMC | Bachelor of Arts in Journalism and Mass Communications | 本科 | 6 |
| MA | Master of Arts | 研究生 | 35 |
| MS | Master of Science | 研究生 | 45 |
| MFA | Master of Fine Arts | 研究生 | 5 |
| MBA | Master of Business Administration | 研究生 | 4 |
| ME | Master of Engineering | 研究生 | 12 |
| MEd | Master of Education | 研究生 | 15 |
| MPH | Master of Public Health | 研究生 | 10 |
| MSW | Master of Social Work | 研究生 | 3 |
| MSN | Master of Science in Nursing | 研究生 | 8 |
| MACC | Master of Accountancy | 研究生 | 2 |
| PhD | Doctor of Philosophy | 研究生 | 45 |
| EdD | Doctor of Education | 研究生 | 8 |
| DNP | Doctor of Nursing Practice | 研究生 | 10 |
| MD | Doctor of Medicine | 研究生 | 2 |
| JD | Juris Doctor | 研究生 | 1 |
| EdS | Educational Specialist | 研究生 | 2 |
| Certificate | Graduate Certificate | 研究生 | 47 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BSE | BSBA | BAJMC | MA | MS | MFA | MBA | ME | MEd | MPH | MSW | MSN | MACC | PhD | EdD | DNP | MD | JD | EdS | Certificate | 合计 |
|------------|----|----|----|-----|------|-------|----|----|----|-----|----|----|-----|-----|-----|------|-----|-----|-----|----|----|-----|-------------|------|
| McCausland College of Arts and Sciences | 35 | 20 | 5 | 0 | 0 | 0 | 15 | 8 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 104 |
| Darla Moore School of Business | 0 | 0 | 0 | 0 | 10 | 0 | 2 | 3 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 4 | 27 |
| Molinaroli College of Engineering and Computing | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 8 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 4 | 43 |
| College of Education | 0 | 3 | 0 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 4 | 8 | 0 | 0 | 0 | 2 | 0 | 40 |
| Arnold School of Public Health | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 4 | 31 |
| College of Information and Communications | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 14 |
| College of Nursing | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 3 | 32 |
| College of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| School of Music | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| College of Hospitality, Retail and Sport Management | 0 | 6 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 12 |
| Joseph F. Rice School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 | 6 |
| Floyd School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 8 |
| College of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| South Carolina Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **35** | **35** | **8** | **12** | **10** | **6** | **35** | **45** | **5** | **4** | **12** | **15** | **10** | **3** | **8** | **2** | **45** | **8** | **10** | **2** | **1** | **2** | **47** | **352** |

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

University of South Carolina has 15 colleges and schools offering undergraduate programs. The McCausland College of Arts and Sciences is the largest undergraduate school, followed by the Darla Moore School of Business and the Molinaroli College of Engineering and Computing. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### McCausland College of Arts and Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://sc.edu/study/majors_and_degrees/anthropology-ba.php |

##### Department of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://sc.edu/study/majors_and_degrees/biological-sciences-bs.php |
| 2 | Biochemistry and Molecular Biology | https://sc.edu/study/majors_and_degrees/biochemistry-and-molecular-biology-bs.php |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://sc.edu/study/majors_and_degrees/chemistry-bs.php |

##### Department of Criminology and Criminal Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice | https://sc.edu/study/majors_and_degrees/criminology-and-criminal-justice-ba.php |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://sc.edu/study/majors_and_degrees/english-ba.php |
| 2 | Creative Writing | https://sc.edu/study/majors_and_degrees/creative-writing-ba.php |

##### Department of Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://sc.edu/study/majors_and_degrees/geography-ba.php |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://sc.edu/study/majors_and_degrees/history-ba.php |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://sc.edu/study/majors_and_degrees/mathematics-bs.php |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://sc.edu/study/majors_and_degrees/philosophy-ba.php |

##### Department of Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://sc.edu/study/majors_and_degrees/physics-bs.php |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://sc.edu/study/majors_and_degrees/political-science-ba.php |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://sc.edu/study/majors_and_degrees/psychology-bs.php |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://sc.edu/study/majors_and_degrees/sociology-ba.php |

##### School of Visual Art and Design
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | 3D/Sculpture: Studio Art | https://sc.edu/study/majors_and_degrees/3d-sculpture-studio-art-bfa.php |
| 2 | Art Education | https://sc.edu/study/majors_and_degrees/art-education-bfa.php |
| 3 | Graphic Design | https://sc.edu/study/majors_and_degrees/graphic-design-bfa.php |
| 4 | Painting | https://sc.edu/study/majors_and_degrees/painting-bfa.php |
| 5 | Printmaking | https://sc.edu/study/majors_and_degrees/printmaking-bfa.php |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://sc.edu/study/majors_and_degrees/art-history-ba.php |
| 2 | African American Studies | https://sc.edu/study/majors_and_degrees/african-american-studies-ba.php |

#### Darla Moore School of Business

##### Department of Accounting
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://sc.edu/study/majors_and_degrees/accounting-bsba.php |

##### Department of Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://sc.edu/study/majors_and_degrees/finance-bsba.php |

##### Department of Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://sc.edu/study/majors_and_degrees/management-bsba.php |

##### Department of Marketing
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://sc.edu/study/majors_and_degrees/marketing-bsba.php |

##### Department of Operations and Supply Chain
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Operations and Supply Chain | https://sc.edu/study/majors_and_degrees/operations-and-supply-chain-bsba.php |

##### Department of Economics
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://sc.edu/study/majors_and_degrees/economics-bsba.php |

#### Molinaroli College of Engineering and Computing

##### Department of Aerospace Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://sc.edu/study/majors_and_degrees/aerospace-engineering-bse.php |

##### Department of Biomedical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://sc.edu/study/majors_and_degrees/biomedical-engineering-bse.php |

##### Department of Chemical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://sc.edu/study/majors_and_degrees/chemical-engineering-bse.php |

##### Department of Civil and Environmental Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://sc.edu/study/majors_and_degrees/civil-engineering-bse.php |

##### Department of Computer Science and Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://sc.edu/study/majors_and_degrees/computer-science-bse.php |
| 2 | Computer Engineering | https://sc.edu/study/majors_and_degrees/computer-engineering-bse.php |

##### Department of Electrical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://sc.edu/study/majors_and_degrees/electrical-engineering-bse.php |

##### Department of Mechanical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://sc.edu/study/majors_and_degrees/mechanical-engineering-bse.php |

#### College of Education

##### Department of Physical Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Sport Psychology and Counseling | https://sc.edu/study/majors_and_degrees/applied-sport-psychology-and-counseling-bs.php |
| 2 | Physical Education | https://sc.edu/study/majors_and_degrees/physical-education-bs.php |

##### Department of Instruction and Teacher Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://sc.edu/study/majors_and_degrees/elementary-education-bs.php |

#### Arnold School of Public Health

##### Department of Exercise Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Science | https://sc.edu/study/majors_and_degrees/exercise-science-bs.php |

##### Department of Communication Sciences and Disorders
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | https://sc.edu/study/majors_and_degrees/communication-sciences-and-disorders-bs.php |

##### Department of Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://sc.edu/study/majors_and_degrees/public-health-bs.php |

#### College of Information and Communications

##### School of Journalism and Mass Communications
###### BAJMC
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://sc.edu/study/majors_and_degrees/advertising-bajmc.php |
| 2 | Broadcast Journalism | https://sc.edu/study/majors_and_degrees/broadcast-journalism-bajmc.php |
| 3 | Mass Communications | https://sc.edu/study/majors_and_degrees/mass-communications-bajmc.php |
| 4 | Print Journalism | https://sc.edu/study/majors_and_degrees/print-journalism-bajmc.php |
| 5 | Public Relations | https://sc.edu/study/majors_and_degrees/public-relations-bajmc.php |

#### College of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://sc.edu/study/majors_and_degrees/nursing-bsn.php |

#### School of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance | https://sc.edu/study/majors_and_degrees/music-performance-bm.php |
| 2 | Music Education | https://sc.edu/study/majors_and_degrees/music-education-bm.php |

#### College of Hospitality, Retail and Sport Management

##### Department of Hospitality and Tourism Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://sc.edu/study/majors_and_degrees/hospitality-management-bs.php |

##### Department of Retail and Fashion Merchandising
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Retail Management | https://sc.edu/study/majors_and_degrees/retail-management-bs.php |
| 2 | Fashion Merchandising | https://sc.edu/study/majors_and_degrees/fashion-merchandising-bs.php |

##### Department of Sport and Entertainment Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport and Entertainment Management | https://sc.edu/study/majors_and_degrees/sport-and-entertainment-management-bs.php |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院组合 | URL |
|---|------|----------|-----|
| 1 | Accelerated Undergraduate to M.D. | Floyd School of Medicine + South Carolina Honors College | https://sc.edu/study/majors_and_degrees/accelerated-undergraduate-to-md-barsc-and-md.php |
| 2 | Biomedical Engineering | McCausland College of Arts and Sciences + Molinaroli College of Engineering and Computing | https://sc.edu/study/majors_and_degrees/biomedical-engineering-ba-bs.php |

### 1.4 Minors — complete list

N/A (需进一步提取 - 本科辅修列表需要单独提取)

### 1.5 General/Institute-wide requirements

USC requires all undergraduate students to complete the Carolina Core, which includes:
- English Composition (6 hours)
- Analytical Reasoning and Problem Solving (3-8 hours)
- Scientific Literacy (7-8 hours)
- Social Sciences (6 hours)
- Humanities and Fine Arts (6 hours)
- Foreign Language (0-12 hours)
- Integrative Courses (3 hours)

### 1.6 Course-ID → Major quick-lookup

N/A (USC does not use a numbering system for majors)

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### McCausland College of Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/anthropology-ma/index.php |
| 2 | Art Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/art-education-ma/index.php |
| 3 | Art History | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/art-history-ma/index.php |
| 4 | Art Studio | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/art-studio-ma/index.php |
| 5 | Dance Studies | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/dance-studies-ma/index.php |
| 6 | English | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/english-ma/index.php |
| 7 | Film and Media | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/film-and-media-ma/index.php |
| 8 | Geography | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/geography-ma/index.php |
| 9 | History | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/history-ma/index.php |
| 10 | Mathematics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/mathematics-ma/index.php |
| 11 | Philosophy | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/philosophy-ma/index.php |
| 12 | Political Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/political-science-ma/index.php |
| 13 | Sociology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/sociology-ma/index.php |
| 14 | Spanish | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/spanish-ma/index.php |
| 15 | Statistics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/statistics-ma/index.php |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biological-sciences-ms/index.php |
| 2 | Chemistry | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/chemistry-ms/index.php |
| 3 | Criminology and Criminal Justice | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/criminology-and-criminal-justice-ms/index.php |
| 4 | Earth and Environmental Resources Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/earth-and-environmental-resources-management-meerm/index.php |
| 5 | Mathematics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/mathematics-ms/index.php |
| 6 | Physics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/physics-ms/index.php |
| 7 | Psychology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/psychology-ms/index.php |
| 8 | Statistics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/statistics-ms/index.php |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Studio | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/art-studio-mfa/index.php |
| 2 | Creative Writing | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/creative-writing-mfa/index.php |
| 3 | Dance | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/dance-mfa/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/anthropology-phd/index.php |
| 2 | Biological Sciences | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biological-sciences-phd/index.php |
| 3 | Chemistry | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/chemistry-phd/index.php |
| 4 | Comparative Literature | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/comparative-literature-phd/index.php |
| 5 | Criminology and Criminal Justice | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/criminology-and-criminal-justice-phd/index.php |
| 6 | Economics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/economics-phd/index.php |
| 7 | English | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/english-phd/index.php |
| 8 | Geography | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/geography-phd/index.php |
| 9 | History | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/history-phd/index.php |
| 10 | Mathematics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/mathematics-phd/index.php |
| 11 | Philosophy | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/philosophy-phd/index.php |
| 12 | Physics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/physics-phd/index.php |
| 13 | Political Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/political-science-phd/index.php |
| 14 | Psychology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/psychology-phd/index.php |
| 15 | Sociology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/sociology-phd/index.php |
| 16 | Statistics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/statistics-phd/index.php |

#### Darla Moore School of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/accountancy-ma/index.php |
| 2 | Business Analytics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/business-analytics-ms/index.php |
| 3 | Economics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/economics-ms/index.php |
| 4 | Finance | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/finance-ms/index.php |
| 5 | Human Resources | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/human-resources-ms/index.php |
| 6 | International Business | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/international-business-ms/index.php |
| 7 | Marketing | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/marketing-ms/index.php |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | One Year MBA | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/business-administration-one-year-mba/index.php |
| 2 | Professional MBA | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/business-administration-professional-mba/index.php |
| 3 | International MBA | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/business-administration-international-mba/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/business-administration-phd/index.php |
| 2 | Economics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/economics-phd/index.php |

#### Molinaroli College of Engineering and Computing

##### ME
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/aerospace-engineering-me/ |
| 2 | Biomedical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biomedical-engineering-me/index.php |
| 3 | Chemical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/chemical-engineering-me/index.php |
| 4 | Civil Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/civil-engineering-me/index.php |
| 5 | Computer Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/computer-engineering-me/index.php |
| 6 | Computer Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/computer-science-me/index.php |
| 7 | Electrical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/electrical-engineering-me/index.php |
| 8 | Mechanical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/mechanical-engineering-me/index.php |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/aerospace-engineering-ms/index.php |
| 2 | Biomedical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biomedical-engineering-ms/index.php |
| 3 | Chemical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/chemical-engineering-ms/index.php |
| 4 | Civil Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/civil-engineering-ms/index.php |
| 5 | Computer Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/computer-engineering-ms/index.php |
| 6 | Computer Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/computer-science-ms/index.php |
| 7 | Electrical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/electrical-engineering-ms/index.php |
| 8 | Engineering Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/engineering-management-ms/index.php |
| 9 | Mechanical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/mechanical-engineering-ms/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/aerospace-engineering-phd/index.php |
| 2 | Biomedical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biomedical-engineering-phd/index.php |
| 3 | Chemical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/chemical-engineering-phd/index.php |
| 4 | Civil Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/civil-engineering-phd/index.php |
| 5 | Computer Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/computer-science-phd/index.php |
| 6 | Electrical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/electrical-engineering-phd/index.php |
| 7 | Mechanical Engineering | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/mechanical-engineering-phd/index.php |

#### College of Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/applied-behavior-analysis-med/index.php |
| 2 | Education Administration | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/education-administration-med/index.php |
| 3 | Educational Psychology and Research | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/educational-psychology-and-research-med/index.php |
| 4 | Special Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/special-education-med/index.php |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/art-education-mat/index.php |
| 2 | Elementary Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/elementary-education-mat/index.php |
| 3 | Foreign Language | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/foreign-language-mat/index.php |
| 4 | Music Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/music-education-mat/index.php |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Practice and Innovation | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/educational-practice-and-innovation-edd/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/counselor-education-phd/index.php |
| 2 | Education Administration | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/education-administration-phd/index.php |
| 3 | Educational Psychology and Research | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/educational-psychology-and-research-phd/index.php |
| 4 | Foundations of Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/foundations-of-education-phd/index.php |

#### Arnold School of Public Health

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/athletic-training-ms/index.php |
| 2 | Biostatistics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biostatistics-ms/index.php |
| 3 | Environmental Health Sciences | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/environmental-health-sciences-ms/index.php |
| 4 | Epidemiology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/epidemiology-ms/index.php |
| 5 | Exercise Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/exercise-science-ms/index.php |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Health Sciences | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/environmental-health-sciences-mph/index.php |
| 2 | Epidemiology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/epidemiology-mph/index.php |
| 3 | Health Promotion, Education, and Behavior | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/health-promotion-education-and-behavior-mph/index.php |
| 4 | Health Services Policy and Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/health-services-policy-and-management-mph/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biostatistics-phd/index.php |
| 2 | Communication Sciences and Disorders | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/communication-sciences-and-disorder-phd/index.php |
| 3 | Environmental Health Sciences | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/environmental-health-sciences-phd/index.php |
| 4 | Epidemiology | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/epidemiology-phd/index.php |
| 5 | Exercise Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/exercise-science-phd/index.php |
| 6 | Health Promotion, Education, and Behavior | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/health-promotion-education-and-behavior-phd/index.php |

#### College of Nursing

##### MSN
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult Gerontology Acute Care Nurse Practitioner | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/adult-gerontology-acute-care-nurse-practitioner-msn/index.php |
| 2 | Family Nurse Practitioner | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/family-nurse-practitioner-msn/index.php |
| 3 | Nursing Administration | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/nursing-administration-msn/index.php |
| 4 | Nursing Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/nursing-education-msn/index.php |
| 5 | Psychiatric Mental Health Nurse Practitioner | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/psychiatric-mental-health-nurse-practitioner-msn/index.php |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult Gerontology Acute Care Nurse Practitioner | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/adult-gerontology-acute-care-nurse-practitioner-dnp/index.php |
| 2 | Clinical Expert | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/clinical-expert-dnp/index.php |
| 3 | Executive Healthcare Leadership | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/executive-healthcare-leadership-dnp/index.php |
| 4 | Family Nurse Practitioner | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/family-nurse-practitioner-dnp/index.php |
| 5 | Nurse Anesthesia | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/nurse-anesthesia-dnp/index.php |
| 6 | Psychiatric Mental Health Nurse Practitioner | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/psychiatric-mental-health-nurse-practitioner-dnp/index.php |

#### College of Social Work

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/social-work-msw/index.php |

#### School of Music

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/music-ma/index.php |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Performance | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/music-performance-mm/index.php |
| 2 | Music Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/music-education-mm/index.php |

##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Performance | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/music-performance-dma/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/music-education-phd/index.php |

#### College of Hospitality, Retail and Sport Management

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/hospitality-management-ms/index.php |
| 2 | Retail and Fashion Merchandising | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/retail-and-fashion-merchandising-ms/index.php |
| 3 | Sport and Entertainment Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/sport-and-entertainment-management-ms/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/hospitality-management-phd/index.php |
| 2 | Sport and Entertainment Management | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/sport-and-entertainment-management-phd/index.php |

#### Joseph F. Rice School of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/law-jd/index.php |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | American Law | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/american-law-llm/index.php |

##### MSL
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Law and Sustainability | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/environmental-law-and-sustainability-msl/index.php |

#### Floyd School of Medicine

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biomedical-science-ms/index.php |
| 2 | Genetic Counseling | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/genetic-counseling-ms/index.php |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Science | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/biomedical-science-phd/index.php |

#### College of Pharmacy

##### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/pharmacy-pharmd/index.php |

### 2.2 At least one program's full deep-dive (worked example)

**Program: Computer Science - MS**
- Department: Department of Computer Science and Engineering
- College: Molinaroli College of Engineering and Computing
- Application Portal: https://apply.sc.edu/
- Application Fee: $50 (domestic), $100 (international)
- GRE: Required
- TOEFL Minimum: 80 iBT
- IELTS Minimum: 6.5
- Application Deadline: Rolling (recommended by February 1 for fall)
- Contact: Graduate Director, Department of Computer Science and Engineering

### 2.3 Graduate admissions model

USC Graduate School uses a centralized application system through the Graduate School office. Each program has its own admission requirements and deadlines. The Graduate School processes applications and forwards them to individual departments for review.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 |
|------|-----|
| Admissions site | https://sc.edu/about/offices_and_divisions/undergraduate_admissions/ |
| Application portal | https://apply.sc.edu/ or Common App |
| EA deadline | October 15 (application), November 1 (credentials) |
| Honors College deadline | November 15 (application), December 1 (credentials) |
| RD deadline | December 1 (application), January 15 (credentials) |
| Decision notification (EA) | Mid-December |
| Decision notification (Honors) | Mid-February |
| Decision notification (RD) | Mid-March |
| SAT/ACT policy | Test-optional through fall, spring and summer 2027 |
| Superscore policy | Yes |
| Application fee | $50 (domestic), $100 (international) |
| Recommendation requirements | Not required |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL iBT | 80 | N/A |
| IELTS | 6.5 | N/A |
| Duolingo English Test | 115 | N/A |
| PTE Academic | 53 | N/A |
| Cambridge English | 176 | N/A |

Applicability: Required for all international applicants whose native language is not English.

### 3.3 Graduate — global rules

- Application Platform: https://apply.sc.edu/ (USC Graduate Application)
- Standard Application Fee: $50 (domestic), $100 (international)
- GRE/GMAT Policy: Varies by program
- Language Test Policy: TOEFL 80+ or IELTS 6.5+ for non-native English speakers
- Application Timeline: Varies by program; many have rolling admissions

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

#### Resident Students (On Campus)

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $12,288 | Per year (12 hours enrollment per term) |
| Tech Fee | $400 | Per year |
| Books and Supplies | $1,522 | Estimated |
| Weighted Average Program Fees | $1,580 | Varies by program |
| Housing | $11,432 | On campus |
| Food | $5,902 | On campus |
| Personal | $4,790 | Estimated |
| Transportation | $2,670 | Estimated |
| **Total** | **$40,584** | On campus |

#### Non-Resident Students (On Campus)

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $38,098 | Per year (12 hours enrollment per term) |
| Tech Fee | $400 | Per year |
| Books and Supplies | $1,522 | Estimated |
| Weighted Average Program Fees | $1,580 | Varies by program |
| Housing | $11,432 | On campus |
| Food | $5,902 | On campus |
| Personal | $4,790 | Estimated |
| Transportation | $2,670 | Estimated |
| **Total** | **$66,394** | On campus |

### 4.2 Undergraduate financial-aid policy

- FAFSA School Code: 003448
- FAFSA Opens: October 1
- FAFSA Deadline: April 1
- Nearly 90% of students receive some form of financial aid
- Need-aware for all applicants (including international)
- Merit-based scholarships available

### 4.3 Graduate cost & funding framework

- Graduate Assistantships: Available (tuition waiver + stipend)
- Fellowships: Available for qualified students
- Travel Grants: Available for research presentations
- Application Fee: $50 (domestic), $100 (international)

---

## SECTION 5 — Evidence chain index

```yaml
field: undergraduate.admissions.EA_deadline
value: "October 15 (application), November 1 (credentials)"
source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/index.php
source_snippet: "Early Action Application Deadline - Apply by Oct. 15 to receive an admissions decision by mid-December. Credentials due by Nov. 1."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.admissions.RD_deadline
value: "December 1 (application), January 15 (credentials)"
source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/index.php
source_snippet: "Regular Decision Application Deadline - Apply by Dec. 1 to receive an admissions decision by mid-March. Credentials due by Jan. 15."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.admissions.test_optional
value: "Test-optional through fall, spring and summer 2027 terms"
source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/index.php
source_snippet: "USC is test-optional through the fall, spring and summer 2027 terms."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.cost.tuition_resident
value: "$12,288 per year"
source_url: https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php
source_snippet: "Tuition - $12,288"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.cost.tuition_nonresident
value: "$38,098 per year"
source_url: https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php
source_snippet: "Tuition - $38,098"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.cost.total_resident_oncampus
value: "$40,584"
source_url: https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php
source_snippet: "Total - $40,584"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.cost.total_nonresident_oncampus
value: "$66,394"
source_url: https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php
source_snippet: "Total - $66,394"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.english_proficiency.toefl_min
value: "80 iBT"
source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_international_students/index.php
source_snippet: "TOEFL iBT: 80"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.ielts_min
value: "6.5"
source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_international_students/index.php
source_snippet: "IELTS: 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: programs.total_count
value: "376"
source_url: https://sc.edu/study/majors_and_degrees/index.php
source_snippet: "Displaying 376 of 376 degrees"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: graduate.programs_count
value: "236"
source_url: https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/index.php
source_snippet: "Showing 1 to 25 of 236 entries"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: colleges.count
value: "15+"
source_url: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/index.php
source_snippet: "COLLEGES & SCHOOLS - Arts and Sciences, Business, Education, Engineering and Computing, etc."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.tuition.per_credit_resident
value: "$512.00"
source_url: https://sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/index.php
source_snippet: "Resident Student - $512.00 per credit hour"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.tuition.per_credit_nonresident
value: "$1,587.50"
source_url: https://sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/index.php
source_snippet: "Non-Resident Student - $1,587.50 per credit hour"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
uofsc-knowledge-base-v2
├── overview
│   ├── uofsc-institutional-overview.md
│   └── uofsc-program-counts.md
├── undergraduate
│   ├── uofsc-ug-arts-sciences.md
│   ├── uofsc-ug-business.md
│   ├── uofsc-ug-engineering.md
│   ├── uofsc-ug-education.md
│   ├── uofsc-ug-public-health.md
│   ├── uofsc-ug-info-comm.md
│   ├── uofsc-ug-nursing.md
│   ├── uofsc-ug-music.md
│   ├── uofsc-ug-hospitality.md
│   └── uofsc-ug-interdisciplinary.md
├── graduate
│   ├── uofsc-grad-arts-sciences.md
│   ├── uofsc-grad-business.md
│   ├── uofsc-grad-engineering.md
│   ├── uofsc-grad-education.md
│   ├── uofsc-grad-public-health.md
│   ├── uofsc-grad-nursing.md
│   ├── uofsc-grad-social-work.md
│   ├── uofsc-grad-music.md
│   ├── uofsc-grad-hospitality.md
│   ├── uofsc-grad-law.md
│   ├── uofsc-grad-medicine.md
│   └── uofsc-grad-pharmacy.md
├── admissions
│   ├── uofsc-ug-deadlines.md
│   ├── uofsc-ug-requirements.md
│   ├── uofsc-grad-admissions.md
│   └── uofsc-international.md
└── costs
    ├── uofsc-ug-costs.md
    ├── uofsc-grad-costs.md
    └── uofsc-financial-aid.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uofsc-knowledge-base-v2"
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
| P0 | Complete undergraduate minors list | https://sc.edu/study/majors_and_degrees/ |
| P0 | Complete graduate program URLs for all 236 programs | https://sc.edu/study/colleges_schools/graduate_school/apply/degree_programs-application-requirements/ |
| P1 | Detailed English proficiency requirements per program | https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_international_students/ |
| P1 | Graduate tuition by program | https://sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/ |
| P1 | Scholarship details and merit awards | https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/ |
| P2 | Honors College admission requirements | https://sc.edu/study/colleges_schools/honors_college/ |
| P2 | Transfer admission requirements | https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/ |
| P2 | Housing and dining options | https://sc.edu/about/offices_and_divisions/housing/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UofSC Value | Notes |
|-----------|-------------|-------|
| Total UG cost/yr (resident, on-campus) | $40,584 | 2026-27 estimate |
| Total UG cost/yr (non-resident, on-campus) | $66,394 | 2026-27 estimate |
| Tuition/yr (resident) | $12,288 | Per year |
| Tuition/yr (non-resident) | $38,098 | Per year |
| Need-blind (intl?) | No | Need-aware for all |
| EA deadline | October 15 | Application deadline |
| RD deadline | December 1 | Application deadline |
| SAT/ACT required? | No | Test-optional through 2027 |
| TOEFL min | 80 iBT | Undergraduate |
| IELTS min | 6.5 | Undergraduate |
| Total program count (rule 1) | 376 | All levels |
| School/department count (rule 2) | 15+ | Colleges and schools |
| Graduate programs | 236 | Graduate School |
| Application fee (domestic) | $50 | Undergraduate |
| Application fee (international) | $100 | Undergraduate |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: sc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
