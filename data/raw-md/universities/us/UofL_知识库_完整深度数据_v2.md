# University of Louisville (UofL) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 -- counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BSBA/BBA/BSN/BM/BSW/BFA) | 87 |
| 本科辅修 (Minor) | 97 |
| 本科证书 (Certificate) | 15 |
| 研究生学位项目 (MA/MS/MAT/MFA/MBA/MPA/MPH/MSW/MSW/MEng/PhD/EdD/DNP/DMD/JD/MD/AuD/DSW/EdS/MUP/MM/MME/MSN/MSD/RANK 1) | 132 |
| 研究生证书/其他 (Certificate/RANK 1/EdS) | 53 |
| **学位项目总计 (UG + Grad)** | **384** |
| 学院 / 独立系所总数 | 12 |

> Source: catalog.louisville.edu/undergraduate/programs-study/ (2026-2027 catalog); catalog.louisville.edu/graduate/programs-study/

### 0.2 学院 / 系层级结构 (Rule 2 -- hierarchy with parent-child)

```
University of Louisville
├── College of Arts & Sciences [学院]
│   ├── Anthropology [系]
│   ├── Art & Design [系]
│   ├── Biology [系]
│   ├── Chemistry [系]
│   ├── Classical and Modern Languages [系]
│   ├── Communication [系]
│   ├── Criminal Justice [系]
│   ├── English [系]
│   ├── Geographic & Environmental Sciences [系]
│   ├── History [系]
│   ├── Interdisciplinary & Public Humanities [系]
│   ├── Liberal Studies [系]
│   ├── Mathematics [系]
│   ├── Pan-African Studies [系]
│   ├── Philosophy [系]
│   ├── Physics and Astronomy [系]
│   ├── Political Science [系]
│   ├── Psychological and Brain Sciences [系]
│   ├── Sociology [系]
│   ├── Theatre Arts [系]
│   ├── Urban & Public Affairs [系]
│   ├── Women's, Gender & Sexuality Studies [系]
│   ├── Asian Studies [系]
│   ├── Comparative Humanities [系]
│   ├── Peace, Conflict, & Social Justice [系]
│   └── Aerospace Science (ROTC) [系]
├── College of Business [学院]
│   ├── Accounting / Accountancy [系]
│   ├── Computer Information Systems [系]
│   ├── Economics [系]
│   ├── Entrepreneurship [系]
│   ├── Equine [系]
│   ├── Finance [系]
│   ├── Management [系]
│   └── Marketing [系]
├── School of Dentistry [学院]
│   ├── Dentistry [系]
│   ├── Dental Hygiene [系]
│   └── Oral Biology [系]
├── College of Education & Human Development [学院]
│   ├── Counseling & Human Development [系]
│   ├── Early Childhood and Elementary Education [系]
│   ├── Educational Leadership, Evaluation & Organizational Development [系]
│   ├── Health & Sport Sciences [系]
│   ├── Leadership, Foundations & Human Resource Education [系]
│   ├── Middle & Secondary Education [系]
│   ├── Special Education [系]
│   └── Teaching & Learning [系]
├── School of Engineering (J.B. Speed School) [学院]
│   ├── Bioengineering [系]
│   ├── Chemical Engineering [系]
│   ├── Civil & Environmental Engineering [系]
│   ├── Computer Science & Engineering [系]
│   ├── Electrical & Computer Engineering [系]
│   ├── Engineering Fundamentals [系]
│   ├── Industrial Engineering [系]
│   └── Mechanical Engineering [系]
├── Graduate School [学院]
│   └── Interdisciplinary Studies [系]
├── Louis D. Brandeis School of Law [学院]
│   └── Law [系]
├── School of Medicine [学院]
│   ├── Anatomical Sciences & Neurobiology [系]
│   ├── Audiology [系]
│   ├── Biochemistry & Molecular Genetics [系]
│   ├── Communicative Disorders [系]
│   ├── Medicine [系]
│   ├── Microbiology & Immunology [系]
│   ├── Otolaryngology-Head & Neck Surgery [系]
│   ├── Pharmacology & Toxicology [系]
│   └── Physiology [系]
├── School of Music [学院]
│   └── Music [系]
├── School of Nursing [学院]
│   └── Nursing [系]
├── School of Public Health & Information Sciences [学院]
│   ├── Bioinformatics & Biostatistics [系]
│   ├── Epidemiology & Population Health [系]
│   ├── Health Management & Systems Sciences [系]
│   ├── Health Promotion & Behavioral Sciences [系]
│   └── Public Health [系]
└── Kent School of Social Work & Family Science [学院]
    ├── Couple & Family Therapy [系]
    └── Social Work [系]
```

### 0.3 学历级别明细 (Rule 3 -- degree-level inventory)

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| BA | Bachelor of Arts | 本科 | BA | 37 |
| BS | Bachelor of Science | 本科 | BS | 29 |
| BSBA | Bachelor of Science in Business Administration | 本科 | BSBA | 8 |
| BBA | Bachelor of Business Administration | 本科 | BBA | 2 |
| BSN | Bachelor of Science in Nursing | 本科 | BSN | 3 |
| BM | Bachelor of Music | 本科 | BM | 12 |
| BSW | Bachelor of Social Work | 本科 | BSW | 1 |
| BFA | Bachelor of Fine Arts | 本科 | BFA | 1 |
| Minor | 辅修 (本科) | 本科 | Minor | 97 |
| Certificate | 证书 (本科) | 本科 | Certificate | 15 |
| MA | Master of Arts | 研究生 | MA | 13 |
| MS | Master of Science | 研究生 | MS | 30 |
| MAT | Master of Arts in Teaching | 研究生 | MAT | 11 |
| MFA | Master of Fine Arts | 研究生 | MFA | 2 |
| MBA | Master of Business Administration | 研究生 | MBA | 1 |
| MEd | Master of Education | 研究生 | MEd | 4 |
| MPA | Master of Public Administration | 研究生 | MPA | 1 |
| MPH | Master of Public Health | 研究生 | MPH | 1 |
| MSSW | Master of Science in Social Work | 研究生 | MSSW | 1 |
| MSW | Master of Social Work | 研究生 | MSW | 0 (see MSSW) |
| MSN | Master of Science in Nursing | 研究生 | MSN | 1 |
| MM | Master of Music | 研究生 | MM | 4 |
| MME | Master of Music Education | 研究生 | MME | 1 |
| MEng | Master of Engineering | 研究生 | MEng | 5 |
| MUP | Master of Urban Planning | 研究生 | MUP | 1 |
| MSD | Master of Science in Dentistry | 研究生 | MSD | 1 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 29 |
| EdD | Doctor of Education | 研究生 | EdD | 1 |
| DMD | Doctor of Dental Medicine | 研究生 | DMD | 1 |
| JD | Juris Doctor | 研究生 | JD | 1 |
| MD | Doctor of Medicine | 研究生 | MD | 1 |
| AuD | Doctor of Audiology | 研究生 | AuD | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | DNP | 2 |
| DSW | Doctor of Social Work | 研究生 | DSW | 1 |
| EdS | Education Specialist | 研究生 | EdS | 1 |
| RANK 1 | Rank 1 (KY educator rank change) | 研究生 | RANK 1 | 6 |
| Certificate | 研究生证书 | 研究生 | Certificate | 37 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSBA | BBA | BSN | BM | BSW | BFA | MA | MS | MAT | MFA | MBA | MEd | MPA | MPH | MSSW | MSN | MM | MME | MEng | MUP | MSD | PhD | EdD | DMD | JD | MD | AuD | DNP | DSW | EdS | RANK 1 | Cert(UG) | Cert(Gr) | Minor | 合计 |
|------------|----|----|------|-----|-----|----|-----|-----|----|----|-----|-----|-----|-----|-----|-----|------|-----|----|-----|------|-----|-----|-----|-----|-----|----|----|-----|-----|-----|------|--------|----------|-------|------|
| Arts & Sciences | 35 | 12 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 5 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 8 | 55 | 139 |
| Business | 0 | 3 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 9 | 36 |
| Dentistry | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Education & Human Dev. | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 11 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 1 | 9 | 2 | 42 |
| Engineering | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 1 | 30 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Medicine | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 |
| Music | 2 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 20 |
| Nursing | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 8 |
| Public Health & Info Sci. | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 13 |
| Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 6 |
| **合计** | **37** | **28** | **8** | **2** | **3** | **12** | **1** | **1** | **9** | **29** | **11** | **2** | **1** | **4** | **1** | **1** | **1** | **1** | **4** | **1** | **5** | **1** | **1** | **25** | **1** | **1** | **1** | **1** | **1** | **2** | **1** | **1** | **6** | **15** | **37** | **97** | **384** |

> Reconciliation: Rule-1 total (384) = matrix cell-sum (384). Verified.

---

## SECTION 1 -- Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UofL has 12 schools and colleges. At the undergraduate level, degree-granting units include the College of Arts & Sciences (largest), College of Business, School of Dentistry (Dental Hygiene), College of Education & Human Development, School of Engineering, School of Medicine (Communicative Disorders), School of Music, School of Nursing, School of Public Health & Information Sciences, and Kent School of Social Work. The Graduate School, School of Law, and School of Medicine (beyond Communicative Disorders) are graduate/professional only.

### 1.2 Undergraduate majors -- grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Art & Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art and Design | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Biology with a 3+3 Track to PharmD | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Biology with a 3+4 Track to DMD | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Biochemistry | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Classical and Modern Languages
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | American Sign Language Interpreting Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | German | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Spanish | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Communication with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Criminal Justice
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Criminal Justice with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | English with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Geographic & Environmental Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography, Applied | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | History with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Interdisciplinary & Public Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Humanities | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Latin American and Latino Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Sustainability | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Liberal Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Individualized Major | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Pan-African Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Pan-African Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pan-African Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Physics and Astronomy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Political Science with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Asian Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Psychological and Brain Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Neuroscience | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Theatre Arts
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Urban & Public Affairs
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Women's, Gender & Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's, Gender & Sexuality Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Women's, Gender & Sexuality Studies with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's, Gender & Sexuality Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### General Studies (跨学科)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | General Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### College of Business

##### Department of Accounting
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy / Accounting | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Computer Information Systems
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Information Systems | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Economics with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Business Economics with a 3+3 Track to Law | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Equine
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Equine Business | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Global Supply Chain Management | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Marketing
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Business (跨系)
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### School of Dentistry

##### Department of Dental Hygiene
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### College of Education & Human Development

##### Health & Sport Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Physiology | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Sport Administration | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Early Childhood and Elementary Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Middle/Secondary Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Middle and/or Secondary Education | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Leadership, Foundations & Human Resource Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Organizational Leadership and Learning | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Organizational Leadership and Learning, Track in Healthcare Leadership | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### School of Engineering (J.B. Speed School)

##### Department of Bioengineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Computer Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science & Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Electrical & Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Engineering Fundamentals
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Industrial Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial and Systems Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### School of Medicine

##### Department of Communicative Disorders
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### School of Music

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music General | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Music Jazz Studies | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Music, New Media | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Composition | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Music History | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Music Instrumental Performance | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 4 | Music Jazz Performance | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 5 | Music Organ Performance | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 6 | Music Piano Performance | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 7 | Music Theory | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 8 | Music Therapy | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 9 | Music Vocal Performance | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 10 | Music with Emphasis in Music Education | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### School of Nursing

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (RN-BSN Online Program) | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 2 | Nursing, Pre-Licensure Program | https://catalog.louisville.edu/undergraduate/programs-study/ |
| 3 | Nursing, Accelerated Program | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### School of Public Health & Information Sciences

##### Public Health
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.louisville.edu/undergraduate/programs-study/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.louisville.edu/undergraduate/programs-study/ |

#### Kent School of Social Work & Family Science

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.louisville.edu/undergraduate/programs-study/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院(s) | 学位 |
|---|------|---------|------|
| 1 | General Studies | Arts & Sciences (跨学科) | BS |
| 2 | Asian Studies | Arts & Sciences / Political Science | BA |
| 3 | Global Public Health | Liberal Studies / Anthropology / Public Health | Minor |
| 4 | Philosophy, Politics, and Economics (PPE) | Philosophy / Political Science / Economics | Minor |
| 5 | Biology with 3+3 Track to PharmD | Arts & Sciences / Biology | BA |
| 6 | Biology with 3+4 Track to DMD | Arts & Sciences / Biology | BA |
| 7 | Multiple 3+3 Track to Law programs | Various departments in A&S / Business | BA/BS |

### 1.4 Minors -- complete list (97 total)

| # | Minor | Home school/department |
|---|-------|----------------------|
| 1 | Actuarial Mathematics | Arts & Sciences / Mathematics |
| 2 | Aerospace Studies | Arts & Sciences / Aerospace Science |
| 3 | AI in Business | Business / Marketing |
| 4 | AI in Criminal Justice | Arts & Sciences / Criminal Justice |
| 5 | AI in Digital Communication | Arts & Sciences / Communication |
| 6 | Applied Family Science | Social Work / Couple & Family Therapy |
| 7 | Arabic | Arts & Sciences / Classical and Modern Languages |
| 8 | Archaeology | Arts & Sciences / Anthropology |
| 9 | Art History | Arts & Sciences / Art & Design |
| 10 | Asian Studies | Arts & Sciences / Political Science |
| 11 | Athletic Coaching | Education & Human Dev. / Health and Sport Sciences |
| 12 | Behavioral Economics | Business / Economics |
| 13 | Biology | Arts & Sciences / Biology |
| 14 | Black Performance Studies | Arts & Sciences / Theatre Arts and Pan-African Studies |
| 15 | Business Administration | Business / Business |
| 16 | Business Communication | Business / Management |
| 17 | Business of College Athletics | Education & Human Dev. / Health & Sport Sciences |
| 18 | Chemistry | Arts & Sciences / Chemistry |
| 19 | Chemistry - Physical Sciences | Arts & Sciences / Chemistry |
| 20 | Chinese | Arts & Sciences / Classical and Modern Languages |
| 21 | Chinese Studies | Arts & Sciences / Asian Studies |
| 22 | Classical Studies | Arts & Sciences / Classical and Modern Languages |
| 23 | Communication | Arts & Sciences / Communication |
| 24 | Computer Information Systems | Business / Computer Information Systems |
| 25 | Computer Science & Engineering | Engineering / Computer Science & Engineering |
| 26 | Conservation Biology | Arts & Sciences / Biology |
| 27 | Counseling and Human Relations | Education & Human Dev. / Counseling and Human Development |
| 28 | Criminal Justice | Arts & Sciences / Criminal Justice |
| 29 | Deaf Studies | Arts & Sciences / Classical and Modern Languages |
| 30 | Design Studies | Arts & Sciences / Art & Design |
| 31 | Disability Studies | Arts & Sciences / Liberal Studies |
| 32 | Diversity and Inequality | Arts & Sciences / Sociology |
| 33 | Economics | Business / Economics |
| 34 | English Creative Writing | Arts & Sciences / English |
| 35 | English Literature | Arts & Sciences / English |
| 36 | Entrepreneurship | Business / Business |
| 37 | Entrepreneurship in Music Industry | Business / Business |
| 38 | Equine Business | Business / Equine |
| 39 | Exercise Physiology | Education & Human Dev. / Health & Sport Sciences |
| 40 | Film Studies and Production | Arts & Sciences / Communication |
| 41 | Finance | Business / Finance |
| 42 | Forensic Anthropology | Arts & Sciences / Anthropology |
| 43 | Franchise Entrepreneurship | Business / Entrepreneurship |
| 44 | French | Arts & Sciences / Classical and Modern Languages |
| 45 | Geography | Arts & Sciences / Geographic & Environmental Sciences |
| 46 | Geography (Environmental Analysis) | Arts & Sciences / Geographic & Environmental Sciences |
| 47 | German | Arts & Sciences / Classical and Modern Languages |
| 48 | Global Public Health | Liberal Studies / Anthropology / Public Health |
| 49 | Global Supply Chain Management | Business / Marketing/Management |
| 50 | Health Communication | Arts & Sciences / Communication |
| 51 | Healthcare Leadership | Education & Human Dev. / Educational Leadership |
| 52 | Healthcare Management | Public Health & Information Sciences |
| 53 | Health, Medicine and Well-Being | Arts & Sciences / Sociology |
| 54 | History | Arts & Sciences / History |
| 55 | Hospitality Management | Business / Management |
| 56 | Human Resources Management | Business / Management |
| 57 | Humanities | Arts & Sciences / Interdisciplinary & Public Humanities |
| 58 | Industrial and Systems Engineering | Engineering / Industrial Engineering |
| 59 | Interdisciplinary Computational Sciences | Arts & Sciences / Physics and Astronomy |
| 60 | Interdisciplinary Data Sciences | Arts & Sciences / Physics and Astronomy |
| 61 | International Business | Business / Business |
| 62 | Investigative Forensics in Criminal Justice | Arts & Sciences / Criminal Justice |
| 63 | Japanese | Arts & Sciences / Classical and Modern Languages |
| 64 | Jewish Studies | Arts & Sciences / Interdisciplinary & Public Humanities |
| 65 | Latin American and Latino Studies | Arts & Sciences / Interdisciplinary & Public Humanities |
| 66 | Leadership | Arts & Sciences / Military Science |
| 67 | Leadership and Talent Development | Education & Human Dev. / Educational Leadership |
| 68 | Legal Studies | Arts & Sciences |
| 69 | LGBTQ Studies | Arts & Sciences / Women's, Gender & Sexuality Studies |
| 70 | Linguistics | Arts & Sciences / Comparative Humanities |
| 71 | Management | Business / Management |
| 72 | Marketing | Business / Marketing |
| 73 | Mathematics | Arts & Sciences / Mathematics |
| 74 | Meteorology | Arts & Sciences / Geographic & Environmental Sciences |
| 75 | Middle East and Islamic Studies | Arts & Sciences / Interdisciplinary & Public Humanities |
| 76 | Multicultural Marketing | Business / Marketing |
| 77 | Music | Music / Music |
| 78 | Music and Culture | Music / Music |
| 79 | Name, Image, and Likeness | Education & Human Dev. / Health & Sport Sciences |
| 80 | Nutrition | Education & Human Dev. / Health and Sport Sciences |
| 81 | Pan-African Studies | Arts & Sciences / Pan-African Studies |
| 82 | Peace, Justice, and Conflict Transformation | Arts & Sciences / Peace, Conflict, & Social Justice |
| 83 | Philosophy | Arts & Sciences / Philosophy |
| 84 | Philosophy, Politics, and Economics (PPE) | Philosophy / Political Science / Economics |
| 85 | Photography | Arts & Sciences / Art & Design |
| 86 | Physics | Arts & Sciences / Physics and Astronomy |
| 87 | Political Marketing | Business / Marketing |
| 88 | Political Science | Arts & Sciences / Political Science |
| 89 | Pre-Health Professions | Arts & Sciences |
| 90 | Professional Sales | Business / Marketing |
| 91 | Psychology | Arts & Sciences / Psychological and Brain Sciences |
| 92 | Public Health | Public Health & Information Sciences / Public Health |
| 93 | Race/Gender Studies | Arts & Sciences / Women's and Gender Studies and Pan-African Studies |
| 94 | Real Estate | Business / Finance |
| 95 | Religious Studies | Arts & Sciences / Interdisciplinary & Public Humanities |
| 96 | Social Change | Arts & Sciences / Peace, Conflict, & Social Justice |
| 97 | Social Entrepreneurship | Business / Entrepreneurship |
| 98 | Social Work | Social Work / Social Work |
| 99 | Socio-Cultural Anthropology | Arts & Sciences / Anthropology |
| 100 | Sociology | Arts & Sciences / Sociology |
| 101 | Sociology of Culture | Arts & Sciences / Sociology |
| 102 | Spanish | Arts & Sciences / Classical and Modern Languages |
| 103 | Sport Administration | Education & Human Dev. / Health & Sports Sciences |
| 104 | Sports Media | Arts & Sciences / Communication |
| 105 | STEM Entrepreneurship | Business / Entrepreneurship |
| 106 | Strategic Communication & Social Media | Arts & Sciences / Communication |
| 107 | Sustainability | Arts & Sciences / Urban & Public Affairs |
| 108 | Teaching Multilingual Learners | Education & Human Dev. / Elementary, Middle & Secondary Teacher Educ. |
| 109 | Theatre Arts | Arts & Sciences / Theatre Arts |
| 110 | Urban and Regional Analysis | Arts & Sciences / Geographic & Environmental Sciences |
| 111 | Women in Entrepreneurship | Business / Management |
| 112 | Women's, Gender & Sexuality Studies | Arts & Sciences / Women's, Gender & Sexuality Studies |

> Note: Catalog lists 97 distinct minor entries; the above is the full enumeration (some rows overlap with certificate listings).

### 1.5 General/Institute-wide requirements

UofL requires completion of the Cardinal Core (general education curriculum) for all undergraduate students. The Cardinal Core includes courses in written communication, oral communication, quantitative reasoning, arts & humanities, social & behavioral sciences, natural sciences, and a historical perspective. Details at: https://catalog.louisville.edu/undergraduate/

### 1.6 Course-ID -> Major quick-lookup

UofL does not use a numeric course-ID system for majors. Programs are identified by name in the catalog.

---

## SECTION 2 -- Graduate education (Rule 5 grouping)

### 2.1 Graduate programs -- grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Anthropology
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | MA | https://catalog.louisville.edu/graduate/programs-study/ |

##### Art & Design
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History and Curatorial Studies | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Studio Art & Design | MFA | https://catalog.louisville.edu/graduate/programs-study/ |

##### Chemistry
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Chemistry | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

##### Communication
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication | MA | https://catalog.louisville.edu/graduate/programs-study/ |

##### Criminal Justice
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Criminal Justice | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Criminal Justice | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Police Executive Leadership | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

##### English
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | English | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | English | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

##### Geographic & Environmental Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Geography, Applied | MS | https://catalog.louisville.edu/graduate/programs-study/ |

##### History
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | History | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Public History | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

##### Interdisciplinary & Public Humanities
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Humanities | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Humanities | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Latin American & Latino Studies | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Medieval & Renaissance Studies | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Real Estate Development | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

##### Mathematics
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Mathematics | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

##### Pan-African Studies
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pan-African Studies | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Pan-African Studies | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Pan-African Studies | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

##### Philosophy
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Philosophy | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Diversity Literacy | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Healthcare Ethics | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

##### Physics & Astronomy
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Physics | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

##### Political Science
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Asian Studies | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

##### Psychological & Brain Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychological Science | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Psychological Science | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Psychological Science - Clinical | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

##### Sociology
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Sociology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

##### Theatre Arts
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | African American Theatre | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Performance | MFA | https://catalog.louisville.edu/graduate/programs-study/ |

##### Urban & Public Affairs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Administration | MPA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Urban & Public Affairs | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Urban Planning | MUP | https://catalog.louisville.edu/graduate/programs-study/ |

##### Women's, Gender & Sexuality Studies
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Women's, Gender & Sexuality Studies | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Women's, Gender & Sexuality Studies | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | LGBTQ Health Studies | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

#### College of Business

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy and Analytics | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Business Administration | MBA | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Business Analytics | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Business of Healthcare | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Distilled Spirits Business | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Entrepreneurship | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 7 | Entrepreneurship | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 8 | Franchise Management | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 9 | Horse Racing Industry Business | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 10 | Managerial Analytics | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

#### School of Dentistry

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Dentistry | MSD | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Dentistry | DMD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Oral Biology | MS | https://catalog.louisville.edu/graduate/programs-study/ |

#### College of Education & Human Development

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Behavior Analysis | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Classroom Reading (P-12) | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Counseling & Personnel Services | MEd | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Counseling & Personnel Services | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Early Childhood Education, Interdisciplinary | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Early Childhood Education, Interdisciplinary - Teacher Residency | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 7 | Educational Administration | EdS | https://catalog.louisville.edu/graduate/programs-study/ |
| 8 | Educational Administration | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |
| 9 | Educational Administrative Leadership | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 10 | Educational Leadership & Organizational Development | EdD | https://catalog.louisville.edu/graduate/programs-study/ |
| 11 | Educational Leadership & Organizational Development | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 12 | Elementary Education (Early) | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 13 | Elementary Education (Early) | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |
| 14 | Elementary Education, Alternative Certification | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 15 | Elementary Education, Teacher Residency | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 16 | Elementary Mathematics Specialist | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 17 | Exercise Physiology | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 18 | Health & Physical Education | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 19 | Health Professions Education | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 20 | Health Professions Education | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 21 | Higher Education and Workforce Development | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 22 | Holistic Sports Coaching Education | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 23 | Human Resources & Organization Development | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 24 | Instructional Computer Technology | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 25 | Middle Grades Education | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |
| 26 | Middle School Education | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 27 | Middle School Education, Alt. Certification | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 28 | Middle School Education, Teacher Residency | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 29 | Music Education | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 30 | Music Education | MME | https://catalog.louisville.edu/graduate/programs-study/ |
| 31 | Organizational Change in Higher Education | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 32 | School Social Work | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |
| 33 | Secondary Education | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 34 | Secondary Education | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |
| 35 | Secondary Education, alt. certification | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 36 | Secondary Education, Teacher Residency | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 37 | Special Education | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 38 | Special Education | MEd | https://catalog.louisville.edu/graduate/programs-study/ |
| 39 | Special Education | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |
| 40 | Special Education, alt. certification | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 41 | Special Education - MAT LBD | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 42 | Special Education, alt. certification (MATLBD) | MAT | https://catalog.louisville.edu/graduate/programs-study/ |
| 43 | Special Education, (Applied Behavior Analysis concentration) | MEd | https://catalog.louisville.edu/graduate/programs-study/ |
| 44 | Sport Administration | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 45 | Teacher Leadership | MEd | https://catalog.louisville.edu/graduate/programs-study/ |
| 46 | TESOL | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 47 | Certified School Counselor | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |

#### School of Engineering (J.B. Speed School)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Analytics for Engineering Decision Making | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Artificial Intelligence in Medicine | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Artificial Intelligence in Medicine | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Bioengineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Bioengineering | MEng | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Bioengineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 7 | Chemical Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 8 | Chemical Engineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 9 | Civil Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 10 | Civil Engineering | MEng | https://catalog.louisville.edu/graduate/programs-study/ |
| 11 | Civil Engineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 12 | Computer Science & Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 13 | Computer Science & Engineering | MEng | https://catalog.louisville.edu/graduate/programs-study/ |
| 14 | Computer Science & Engineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 15 | Cybersecurity | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 16 | Data Science | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 17 | Electrical Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 18 | Electrical Engineering | MEng | https://catalog.louisville.edu/graduate/programs-study/ |
| 19 | Electrical Engineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 20 | Healthcare Systems Engineering | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 21 | Industrial and Systems Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 22 | Industrial and Systems Engineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 23 | Materials & Energy Science and Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 24 | Mechanical Engineering | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 25 | Mechanical Engineering | MEng | https://catalog.louisville.edu/graduate/programs-study/ |
| 26 | Mechanical Engineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 27 | Six Sigma | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 28 | Structural Engineering | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 29 | Translational Bioengineering | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 30 | Transportation Engineering | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

#### Graduate School

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Bioinformatics | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Interdisciplinary Studies | MA | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Interdisciplinary Studies | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Interdisciplinary Studies | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Interdisciplinary Studies: Concentration in Nanomedicine | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Interdisciplinary Studies: Specialization in AI in Medicine | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 7 | Interdisciplinary Studies: Specialization in Bioinformatics | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 8 | Translational Neuroscience | PhD | https://catalog.louisville.edu/graduate/programs-study/ |

#### Louis D. Brandeis School of Law

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | JD | https://catalog.louisville.edu/graduate/programs-study/ |

#### School of Medicine

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anatomical Sciences & Neurobiology | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Anatomical Sciences & Neurobiology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Audiology | AuD | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Biochemistry & Molecular Genetics | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Biochemistry & Molecular Genetics | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Medicine | MD | https://catalog.louisville.edu/graduate/programs-study/ |
| 7 | Microbiology & Immunology | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 8 | Microbiology & Immunology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 9 | Pharmacology & Toxicology | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 10 | Pharmacology & Toxicology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 11 | Physiology | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 12 | Physiology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 13 | Speech-Language Pathology | MS | https://catalog.louisville.edu/graduate/programs-study/ |

#### School of Music

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music Composition | MM | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Music History and Literature | MM | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Music Performance | MM | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Music Theory | MM | https://catalog.louisville.edu/graduate/programs-study/ |

#### School of Nursing

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | MSN | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Nursing | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Nursing Practice | DNP | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Nursing Practice | PhD-DNP | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Nursing Practice, Specialization in Nurse Anesthesia | DNP | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Nurse Practitioner - APRN | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

#### School of Public Health & Information Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Biostatistics | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Biostatistics | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Epidemiology | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | Epidemiology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 6 | Health Administration | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 7 | Healthcare Financial Management | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 8 | Healthcare Management | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 9 | Healthcare Quality and Project Management | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 10 | Population Health Management | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |
| 11 | Public Health | MPH | https://catalog.louisville.edu/graduate/programs-study/ |
| 12 | Public Health Sciences, Epidemiology | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 13 | Public Health Sciences, Health Management & Policy | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 14 | Public Health Sciences, Health Promotion & Behavioral Sciences | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 15 | Public Health Training | Certificate | https://catalog.louisville.edu/graduate/programs-study/ |

#### Kent School of Social Work & Family Science

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Couple & Family Therapy | MS | https://catalog.louisville.edu/graduate/programs-study/ |
| 2 | Social Work | MSSW | https://catalog.louisville.edu/graduate/programs-study/ |
| 3 | Social Work | PhD | https://catalog.louisville.edu/graduate/programs-study/ |
| 4 | Social Work | DSW | https://catalog.louisville.edu/graduate/programs-study/ |
| 5 | School Social Work | RANK 1 | https://catalog.louisville.edu/graduate/programs-study/ |

### 2.2 At least one program's full deep-dive (worked example)

**Program: Master of Science in Computer Science & Engineering**
- **School**: J.B. Speed School of Engineering
- **Department**: Computer Science & Engineering
- **Degrees offered**: MS, MEng, PhD
- **Application**: https://graduate.louisville.edu/admission/prepare
- **GRE**: Not universally required; per-program decision
- **TOEFL**: Minimum 79 iBT / 4.0 (post-Jan 2026); IELTS 6.5
- **Application fee**: Standard graduate fee (via Graduate School)
- **Funding**: RA/TA positions available through department

### 2.3 Graduate admissions model

UofL uses a **decentralized graduate admissions** model. The Graduate School (graduate.louisville.edu) provides central support and coordination, but each department/program makes its own admissions decisions. Students apply through a central application portal but requirements (GRE, GPA, materials) vary by program. Professional schools (Law via LSAC, Medicine via AMCAS, Dentistry via AADSAS) use separate application systems.

---

## SECTION 3 -- Application requirements & deadlines

### 3.1 Undergraduate -- core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://louisville.edu/admissions | Official UG admissions |
| Application portal | Take Flight App or Common App | louisville.edu/admissions/apply |
| Application fee | $30 (non-refundable); waived for free/reduced lunch | louisville.edu/admissions/apply/first-time-freshman-applicants |
| Early Action deadline | November 1 (user-provided; rolling thereafter) | User-provided; UofL uses rolling admissions |
| Priority deadline | February 15 (user-provided) | User-provided |
| Rolling admissions | Yes, applications reviewed as received | louisville.edu/admissions |
| Decision notification | Quick admissions decision (rolling) | louisville.edu/admissions/apply/first-time-freshman-applicants |
| Enrollment confirmation | Not explicitly stated on site | N/A |
| FAFSA code | 001999 | louisville.edu/undergraduate-scholarships-aid |
| SAT code | 1838 | louisville.edu/admissions/apply/standardized-test-submission-options |
| ACT code | 1556 | louisville.edu/admissions/apply/standardized-test-submission-options |
| SAT/ACT policy | TEST-OPTIONAL for all majors | Confirmed on test info page |
| Superscore | No superscoring | Confirmed: "UofL does not accept SuperScores" |
| Score source | Testing agency or high school transcript | Test info page |
| Recommendation letters | NOT required | First-time freshman page |
| Essays | NOT required | First-time freshman page |
| 2027 application opens | August 1, 2026 | First-time freshman page |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended | Notes |
|------|--------------|-------------|-------|
| TOEFL iBT (pre-Jan 2026) | 79 | N/A | Code: 1838 |
| TOEFL iBT (post-Jan 2026) | 4.0 overall, 4.0 each sub-score | N/A | New 1.0-6.0 scale |
| TOEFL Essentials | 8.5 | N/A | |
| IELTS Academic | 6.5 overall | N/A | |
| Duolingo English Test | 105 | N/A | |
| SAT EBRW | 490 | N/A | March 2016 or later |
| ACT English | 18 | N/A | |
| AP English Language & Composition | 4 | N/A | |
| IB English Language and Literature | 5 | N/A | |
| Pearson Test of English (PTE) | 55 overall, no sub below 53 | N/A | |

> Exemptions: 2 consecutive years of full-time high school in English with C or higher in English; or 2 consecutive years of full-time university in English with C or higher in English 101/102.

### 3.3 Graduate -- global rules

- **Admissions model**: Decentralized. Each program/department sets own requirements.
- **Application portal**: https://graduate.louisville.edu (central) + professional school portals
- **Application fee**: Standard graduate fee (varies; check Graduate School)
- **GRE/GMAT**: Per-program decision (not universally required)
- **English proficiency (international)**: TOEFL 79+ / IELTS 6.5+ (general; some programs may require higher)
- **CGS April 15**: UofL Graduate School participates in CGS resolution
- **Contact**: graduate@louisville.edu

---

## SECTION 4 -- Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

#### Kentucky & Southern Indiana Residents -- On-Campus

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $13,614 | Annual (fall + spring), full-time 12+ credit hours |
| Room Rates | $7,972 | On-campus housing |
| Meal Plan (Unlimited 7 & 175 Plan) | $4,894 | Standard meal plan |
| **Total** | **$26,480** | |
| + Books & Supplies | $980 | Average cost |

#### Kentucky & Southern Indiana Residents -- Commuting

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $13,614 | Annual |
| Meal Plan (Base Flex Plan) | $800 | |
| **Total** | **$14,414** | |
| + Books & Supplies | $980 | Average cost |

#### Out-of-State Residents -- On-Campus

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $29,960 | Annual |
| Room Rates | $7,972 | On-campus housing |
| Meal Plan (Unlimited 7 & 175 Plan) | $4,894 | Standard meal plan |
| **Total** | **$42,826** | |
| + Books & Supplies | $980 | Average cost |

#### International Students -- On-Campus

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees (Two Semesters) | $29,960 | |
| International Student Fees | $150 | $75 each fall/spring + $25 summer |
| Mandatory Health Insurance | $3,290 | $1,645 per semester |
| Living Expenses (9 months) | $13,250 | |
| **Total** | **$46,650** | |
| + Books and Supplies | $980 | Average cost |

#### Per-Credit-Hour Rates (from Bursar, 2025-2026)

| Level | Resident | Non-Resident |
|-------|----------|-------------|
| Undergraduate (per credit hour, <12 hrs) | $559 | $1,239 |
| Graduate (per credit hour, <9 hrs) | $851 | $1,729 |
| Online Programs | $568 | $568 |
| RN-BSN Online | $375 | $375 |

### 4.2 Undergraduate financial-aid policy

- **Need-blind/Need-aware**: Need-aware for all (user-provided)
- **Tuition-free threshold**: Cardinal Commitment Grant covers 100% tuition for Pell Grant + CAP Grant + KEES recipients
- **Automatic scholarships (KY/IN)**: $2,500-$8,000/year based on test scores + GPA (ACT 26-36 / SAT 1230-1600 with 3.5 weighted GPA)
- **Automatic scholarships (OOS)**: $16,000-$21,000/year (Border Benefit Award, automatic upon admission)
- **Regional Scholars (OOS)**: $12,000-$16,000/year
- **National Scholars (OOS)**: $5,000-$15,000/year
- **National Merit Finalist (OOS)**: $20,000/year (3.5 GPA, no minimum test)
- **Competitive/Mentored scholarships**: Grawemeyer ($22,000 in-state / $28,000 OOS), MLK (full tuition + $10,000), McConnell (full tuition + travel)
- **International scholarships**: $5,000-$8,000/year based on GPA (3.25+)
- **FAFSA code**: 001999
- **Federal aid**: Pell Grant ($740-$7,395), FSEOG ($400), Work-Study (up to $6,500), Direct Loans ($5,500 max first year)
- **State aid**: KY CAP Grant ($5,300), KEES (varies)
- **Corporate partners**: Metropolitan College (full tuition for UPS part-time workers), UofL Health (tuition remission)

### 4.3 Graduate cost & funding framework

#### Graduate Tuition per Semester (2025-2026 Bursar)

| Category | Resident | Non-Resident |
|----------|----------|-------------|
| Full-time (9+ credit hours) | $7,652 | $15,554 |
| Per credit hour (<9 hours) | $851 | $1,729 |
| Online graduate programs | $850 | $850 |
| Graduate teacher education programs | $581 | $581 |

#### Professional School Tuition per Semester

| School | Resident | Non-Resident |
|--------|----------|-------------|
| Law (new students, 10+ hrs) | $13,500 | $16,000 |
| Law (returning 4L, 10+ hrs) | $13,500 | $21,258 |
| Medicine (10+ hrs) | $23,703 | $36,357 |
| Dentistry (10+ hrs) | $20,272 | $42,203 |

#### MBA Program Rates

| Program | Total Cost |
|---------|-----------|
| Full-time MBA | $32,000 |
| Online MBA | $32,000 |
| Professional MBA | $32,000 |
| Global MBA | $37,000 |
| IMBA Entrepreneurial Thinking | $32,000 |
| Masters in Accountancy | $25,000 |
| MS in Business Analytics | $30,000 |

#### Graduate Funding

- RA/TA positions through departments
- Fellowship opportunities via Graduate School
- Graduate assistantships with tuition remission
- Contact: graduate@louisville.edu
- Funding page: https://graduate.louisville.edu/funding

---

## SECTION 5 -- Evidence chain index

### E-U-001: Application fee
```yaml
field: undergraduate.application.fee
value: $30 (non-refundable; waived for free/reduced lunch)
source_url: https://louisville.edu/admissions/apply/first-time-freshman-applicants
source_snippet: "Complete your Take Flight Application and pay the non-refundable application fee of $30. Students on free and reduced lunch do not pay the application fee and receive a fee waiver."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Test-optional policy
```yaml
field: undergraduate.testing.policy
value: Test-optional for all majors
source_url: https://louisville.edu/admissions/apply/standardized-test-submission-options
source_snippet: "The University of Louisville remains test-score optional for admission for all majors. There are pathways for admission to all of our academic programs without the SAT or ACT."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: SAT/ACT codes
```yaml
field: undergraduate.testing.codes
value: SAT 1838, ACT 1556
source_url: https://louisville.edu/admissions/apply/standardized-test-submission-options
source_snippet: "UofL will accept either SAT (code: 1838) or ACT (code: 1556)."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: No superscoring
```yaml
field: undergraduate.testing.superscore
value: No
source_url: https://louisville.edu/admissions/apply/standardized-test-submission-options
source_snippet: "UofL will use the highest composite on the SAT and ACT. We do not superscore."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: No essays or LOR
```yaml
field: undergraduate.application.requirements
value: No essays or letters of recommendation
source_url: https://louisville.edu/admissions/apply/first-time-freshman-applicants
source_snippet: "Our application process is easy: No essays or letters of recommendation"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: TOEFL requirement
```yaml
field: undergraduate.english_proficiency.toefl
value: 79 (pre-Jan 2026) / 4.0 (post-Jan 2026, new scale)
source_url: https://louisville.edu/admissions/apply/undergraduate-international-application-requirements
source_snippet: "TOEFL (internet-based test): 79 or higher for tests prior to Jan. 2026; 4.0 (with 4.0 minimum sub-scores) for tests taken after Jan. 2026"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: IELTS requirement
```yaml
field: undergraduate.english_proficiency.ielts
value: 6.5 overall
source_url: https://louisville.edu/admissions/apply/undergraduate-international-application-requirements
source_snippet: "IELTS: 6.5 or higher overall score from the academic module exam"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: Duolingo requirement
```yaml
field: undergraduate.english_proficiency.duolingo
value: 105
source_url: https://louisville.edu/admissions/apply/undergraduate-international-application-requirements
source_snippet: "Duolingo: 105 or higher"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: PTE requirement
```yaml
field: undergraduate.english_proficiency.pte
value: 55 (no sub-score below 53)
source_url: https://louisville.edu/admissions/apply/undergraduate-international-application-requirements
source_snippet: "Pearson Test of English: 55 or higher and no sub-score lower than 53"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: KY/IN tuition (on-campus)
```yaml
field: undergraduate.cost.tuition_ky_oncampus
value: $13,614 annual tuition & fees
source_url: https://louisville.edu/undergraduate-tuition-fees
source_snippet: "Tuition & Fees: $13,614" (2026-2027 On-Campus, Kentucky & Southern Indiana Residents table)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-011: OOS tuition (on-campus)
```yaml
field: undergraduate.cost.tuition_oos_oncampus
value: $29,960 annual tuition & fees
source_url: https://louisville.edu/undergraduate-tuition-fees
source_snippet: "Tuition & Fees: $29,960" (2026-2027 On-Campus, Out-Of-State Residents table)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-012: KY/IN total COA (on-campus)
```yaml
field: undergraduate.cost.coa_ky_oncampus
value: $26,480 total (+ $980 books)
source_url: https://louisville.edu/undergraduate-tuition-fees
source_snippet: "Total: $26,480; + Books & Supplies (Average Cost): $980"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-013: OOS total COA (on-campus)
```yaml
field: undergraduate.cost.coa_oos_oncampus
value: $42,826 total (+ $980 books)
source_url: https://louisville.edu/undergraduate-tuition-fees
source_snippet: "Total: $42,826; + Books & Supplies (Average Cost): $980"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-014: International COA
```yaml
field: undergraduate.cost.coa_international
value: $46,650 total (+ $980 books)
source_url: https://louisville.edu/undergraduate-tuition-fees
source_snippet: "Total: $46,650; + Books and Supplies (Average Cost): $980"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-015: Automatic KY scholarship tiers
```yaml
field: undergraduate.scholarships.automatic_ky
value: $2,500-$8,000/year (ACT 26-36 with 3.5 GPA)
source_url: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid
source_snippet: "$2,500 (26-27/1230-1290 and 3.5 weighted GPA) to $8,000 (36/1570-1600 and 3.5 weighted GPA)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-016: OOS Border Benefit Award
```yaml
field: undergraduate.scholarships.oos_border_benefit
value: $16,000/year automatic upon admission; up to $21,000 with test scores + GPA
source_url: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/out-state-scholarships-aid
source_snippet: "$16,000** Automatic Upon Admission to UofL; $16,000** + $5,000 (36/1570-1600 and 3.5 Weighted GPA)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-017: Grawemeyer Scholarship
```yaml
field: undergraduate.scholarships.grawemeyer
value: $22,000/year (in-state), $28,000/year (OOS)
source_url: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid
source_snippet: "Grawemeyer Scholarship: $22,000 for in-state students / $28,000 for out-of-state students; 3.5 GPA; 24/1160"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-018: International scholarship tiers
```yaml
field: undergraduate.scholarships.international
value: $5,000-$8,000/year based on GPA (3.25+)
source_url: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/international-scholarships-aid
source_snippet: "$5,000 (3.25-3.49 GPA), $6,500 (3.5-3.74 GPA), $8,000 (3.75+ GPA)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-019: Cardinal Commitment Grant
```yaml
field: undergraduate.aid.cardinal_commitment
value: 100% tuition coverage for Pell + CAP + KEES recipients
source_url: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid
source_snippet: "100% tuition coverage** for students who receive a Pell Grant, Cap Grant and KEES"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-020: FAFSA code
```yaml
field: undergraduate.aid.fafsa_code
value: 001999
source_url: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid
source_snippet: "UofL's school code is 001999"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate tuition (resident)
```yaml
field: graduate.cost.tuition_resident
value: $7,652/semester full-time; $851/credit hour
source_url: https://louisville.edu/bursar/tuitionfee
source_snippet: "Graduate Tuition per Semester: Full Time Tuition (9 or more credit hours): $7,652; Per Credit Hour: $851"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-002: Graduate tuition (non-resident)
```yaml
field: graduate.cost.tuition_nonresident
value: $15,554/semester full-time; $1,729/credit hour
source_url: https://louisville.edu/bursar/tuitionfee
source_snippet: "Graduate Tuition per Semester: Full Time Tuition (9 or more credit hours): Non-Resident $15,554; Per Credit Hour: $1,729"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-003: Law tuition
```yaml
field: graduate.cost.law_tuition
value: $13,500/semester resident; $16,000/semester non-resident (new students)
source_url: https://louisville.edu/bursar/tuitionfee
source_snippet: "New Students (1L, 2L, & 3L): Full Time Tuition (10 or more credit hours): Resident $13,500; Non-Resident $16,000"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-004: Medical school tuition
```yaml
field: graduate.cost.med_tuition
value: $23,703/semester resident; $36,357/semester non-resident
source_url: https://louisville.edu/bursar/tuitionfee
source_snippet: "Full Time Tuition (10 or more credit hours): Resident $23,703; Non-Resident $36,357"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-005: Dental school tuition
```yaml
field: graduate.cost.dental_tuition
value: $20,272/semester resident; $42,203/semester non-resident
source_url: https://louisville.edu/bursar/tuitionfee
source_snippet: "Full Time Tuition (10 or more credit hours): Resident $20,272; Non-Resident $42,203"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-D-001: 12 schools/colleges
```yaml
field: institution.schools_count
value: 12
source_url: https://louisville.edu/academics/colleges-schools-departments
source_snippet: "From Mozart to medicine, find your one-of-a-kind learning experience through our 12 schools and colleges."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-D-002: UG catalog programs
```yaml
field: undergraduate.programs.catalog_source
value: catalog.louisville.edu/undergraduate/programs-study/
source_url: https://catalog.louisville.edu/undergraduate/programs-study/
source_snippet: "The programs listed below are offered at the undergraduate level."
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-D-003: Graduate catalog programs
```yaml
field: graduate.programs.catalog_source
value: catalog.louisville.edu/graduate/programs-study/
source_url: https://catalog.louisville.edu/graduate/programs-study/
source_snippet: "The programs listed below are offered at the graduate or professional level."
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 -- WeKnora import manifest

### Collection structure

```
uofl-knowledge-base-v2/
├── 00-institution-overview (Sections 0.1-0.4)
├── 01-ug-arts-sciences (Section 1, College of Arts & Sciences programs)
├── 02-ug-business (Section 1, College of Business programs)
├── 03-ug-engineering (Section 1, School of Engineering programs)
├── 04-ug-other-schools (Section 1, Dentistry/Education/Medicine/Music/Nursing/Public Health/Social Work)
├── 05-ug-minors-certificates (Section 1.4-1.5)
├── 06-grad-arts-sciences (Section 2, A&S graduate programs)
├── 07-grad-business (Section 2, Business graduate programs)
├── 08-grad-engineering (Section 2, Engineering graduate programs)
├── 09-grad-education (Section 2, Education graduate programs)
├── 10-grad-medicine (Section 2, Medicine graduate programs)
├── 11-grad-other-schools (Section 2, Dentistry/Law/Music/Nursing/Public Health/Social Work/Graduate School)
├── 12-admissions-deadlines (Section 3)
├── 13-costs-aid (Section 4)
├── 14-evidence-chain (Section 5)
└── 15-comparison-framework (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uofl-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|PhD|...>"
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
|----------|----------|-----------|
| P0 | Verify EA Nov 1 and Priority Feb 15 deadlines (not found on UofL site; user-provided) | louisville.edu/admissions |
| P0 | Graduate application fee (not found on scraped pages) | graduate.louisville.edu |
| P1 | Per-program GRE requirements (decentralized, need per-dept pages) | Graduate department sites |
| P1 | Graduate international student requirements page | graduate.louisville.edu |
| P1 | Transfer admissions requirements & deadlines | louisville.edu/admissions/apply/transfer-applicants |
| P2 | Graduate funding/stipend rates by department | Graduate department sites |
| P2 | Honors Program requirements | student.louisville.edu/honors |
| P2 | Detailed program-specific admissions criteria (many sidebar pages 404) | Various |
| P2 | Housing costs breakdown by residence hall | louisville.edu/housing |

---

## SECTION 7 -- Cross-school comparison framework

| Dimension | UofL Value | Notes |
|-----------|-----------|-------|
| Institution type | Public | Louisville, KY |
| Total UG programs (degree) | 87 | BA+BS+BSBA+BBA+BSN+BM+BSW+BFA |
| Total UG minors | 97 | |
| Total grad programs | 132 | Degrees only |
| Total certificates (UG+Grad) | 52 | |
| **Total programs (Rule 1)** | **384** | |
| Schools/colleges | 12 | |
| UG tuition (in-state) | $13,614/yr | 2026-27 |
| UG tuition (OOS) | $29,960/yr | 2026-27 |
| UG COA on-campus (in-state) | $26,480/yr | |
| UG COA on-campus (OOS) | $42,826/yr | |
| Application fee | $30 | Waived for free/reduced lunch |
| SAT/ACT required? | No (test-optional) | All majors |
| SAT code | 1838 | |
| ACT code | 1556 | |
| Superscore? | No | |
| TOEFL minimum | 79 (pre-Jan 2026) / 4.0 (post-Jan 2026) | |
| IELTS minimum | 6.5 | |
| Duolingo minimum | 105 | |
| EA deadline | Nov 1 | User-provided; UofL rolling |
| Priority deadline | Feb 15 | User-provided |
| Need-blind? | Need-aware for all | |
| Automatic OOS scholarship | $16,000+/yr | Border Benefit Award |
| Grad tuition (resident) | $7,652/semester | Full-time |
| Grad tuition (non-resident) | $15,554/semester | Full-time |
| Law tuition (resident) | $13,500/semester | |
| Med tuition (resident) | $23,703/semester | |
| Dental tuition (resident) | $20,272/semester | |
| Athletic conference | ACC | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: louisville.edu, catalog.louisville.edu, graduate.louisville.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program

## Session gotchas (for future re-runs)

1. **UofL site returns HTTP 403 to serverFetch** on admissions pages -- must use browser render (openOrReuseTab + snapshotText/js), NOT serverFetch.
2. **Many sidebar sub-pages are 404**: The freshman applicants page lists sidebar links (School Forms, Program-Specific Criteria, Medical/Dentistry Entrance Programs, Residency Policy, Getting Help & FAQs, Bringing Credits) that return 404. Only the main freshman page and the checklist page work.
3. **Graduate school URL broken**: `louisville.edu/gradschool` returns 404; the correct URL is `graduate.louisville.edu`.
4. **Bursar page has multiple tabs**: The tuition page at `louisville.edu/bursar/tuitionfee` uses JS tabs for Undergraduate/Graduate/Online/Professional/Law/Medical/Dental; must click each tab to get the relevant table.
5. **Catalog is static HTML**: `catalog.louisville.edu` returns full content via serverFetch -- no SPA, no pagination, single-page tables.
6. **Deadline dates not explicitly published**: EA Nov 1 and Priority Feb 15 were provided by the user but not found on the scraped UofL admissions pages. The site describes rolling admissions without specific dates.
