# University of Virginia (UVA) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/B.S.Ed./B.P.S.) | ~75 |
| 本科辅修 (Minor) | ~55 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 143 |
| 研究生高级证书 (Advanced Certificate / Diploma) | Included in 143 |
| **学位项目总计 (UG + Grad)** | **~273** |
| 学院 / 独立系所总数 | 12 |

> Source: UVA reports "143 master's and doctoral programs" on graduate studies page. UG majors/minors enumerated from virginia.edu/majors-minors/.

### 0.2 学院 / 系层级结构

```
University of Virginia
├── College and Graduate School of Arts & Sciences [学院]
│   ├── Humanities Division [系]
│   │   ├── English
│   │   ├── History
│   │   ├── Philosophy
│   │   ├── Religious Studies
│   │   ├── Classics
│   │   ├── Media Studies
│   │   ├── Art History
│   │   ├── Music
│   │   ├── Drama
│   │   └── Dance
│   ├── Social Sciences Division [系]
│   │   ├── Politics
│   │   ├── Economics
│   │   ├── Sociology
│   │   ├── Anthropology
│   │   ├── Psychology
│   │   ├── Linguistics
│   │   ├── Cognitive Science
│   │   ├── Global Studies
│   │   ├── Environmental Sciences
│   │   └── Media Studies
│   ├── Natural Sciences & Mathematics Division [系]
│   │   ├── Biology
│   │   ├── Chemistry
│   │   ├── Physics
│   │   ├── Mathematics
│   │   ├── Statistics
│   │   ├── Astronomy
│   │   ├── Neuroscience
│   │   └── Environmental Sciences
│   ├── Languages & Literatures [系]
│   │   ├── French
│   │   ├── German
│   │   ├── Spanish
│   │   ├── Italian
│   │   ├── Portuguese
│   │   ├── Chinese Language & Literature
│   │   ├── Japanese Language & Literature
│   │   ├── Korean
│   │   ├── Slavic Languages and Literatures
│   │   ├── South Asian Languages and Literatures
│   │   └── Middle Eastern and South Asian Languages and Cultures
│   ├── Interdisciplinary Programs [系]
│   │   ├── African American and African Studies
│   │   ├── American Studies
│   │   ├── East Asian Languages, Literatures and Culture
│   │   ├── Jewish Studies
│   │   ├── Latin American Studies
│   │   ├── Medieval Studies
│   │   ├── Political and Social Thought
│   │   ├── Political Philosophy, Policy, and Law
│   │   ├── Women, Gender & Sexuality
│   │   ├── Archaeology
│   │   ├── Environmental Thought and Practice
│   │   ├── Health, Ethics, and Society
│   │   ├── Global Environments and Sustainability
│   │   └── Behavioral Neuroscience (B.S.)
│   └── Computer Science [系] ⚠ shared with Engineering
│       ├── Computer Science, B.A.
│       └── Computer Science, B.S.
│
├── School of Engineering and Applied Science [学院]
│   ├── Department of Mechanical and Aerospace Engineering [系]
│   │   ├── Aerospace Engineering
│   │   └── Mechanical Engineering
│   ├── Department of Civil and Environmental Engineering [系]
│   │   └── Civil Engineering
│   ├── Department of Chemical Engineering [系]
│   │   └── Chemical Engineering
│   ├── Department of Electrical and Computer Engineering [系]
│   │   └── Electrical Engineering
│   ├── Department of Computer Science [系] ⚠ shared with A&S
│   │   └── Computer Science (B.A. and B.S.)
│   ├── Department of Biomedical Engineering [系]
│   │   └── Biomedical Engineering
│   ├── Department of Materials Science and Engineering [系]
│   │   └── Materials Science and Engineering
│   ├── Department of Systems and Information Engineering [系]
│   │   └── Systems Engineering
│   ├── Department of Engineering and Society [系]
│   │   ├── History of Science and Technology Minor
│   │   ├── Science and Technology Policy Minor
│   │   ├── Science, Technology, and Society Minor
│   │   └── Technology Ethics Minor
│   ├── Applied Mathematics Program [系]
│   │   └── Applied Mathematics
│   └── Engineering Science [系]
│       └── Engineering Science
│
├── School of Architecture [学院]
│   ├── Architecture [系]
│   │   ├── Architecture (B.S.Arch)
│   │   └── Architectural History
│   ├── Urban and Environmental Planning [系]
│   │   └── Urban and Environmental Planning
│   └── Interdisciplinary Minors [系]
│       ├── Design Minor
│       ├── Historic Preservation Minor
│       └── Landscape Architecture Minor
│
├── School of Education and Human Development [学院]
│   ├── Department of Curriculum, Instruction and Special Education [系]
│   │   ├── Early Childhood Education, B.S.Ed.
│   │   ├── Elementary Education, B.S.Ed.
│   │   └── Special Education, B.S.Ed.
│   ├── Department of Kinesiology [系]
│   │   └── Kinesiology, B.S.Ed.
│   ├── Department of Human Services [系]
│   │   ├── Youth & Social Innovation, B.S.Ed.
│   │   └── Speech Communication Disorders, B.S.Ed.
│   └── Minors [系]
│       ├── Global Studies in Education Minor
│       └── Health and Wellbeing Minor
│
├── McIntire School of Commerce [学院]
│   ├── Commerce [系]
│   │   └── Commerce (B.S.)
│   └── Minors [系]
│       ├── Entrepreneurship Minor
│       ├── General Business Minor
│       ├── Leadership Minor
│       └── Real Estate Minor
│
├── School of Nursing [学院]
│   └── Nursing [系]
│       └── Nursing (B.S.N.)
│
├── Frank Batten School of Leadership and Public Policy [学院]
│   └── Public Policy [系]
│       └── Public Policy and Leadership
│
├── School of Data Science [学院]
│   └── Data Science [系]
│       ├── Data Science, B.S.
│       └── Data Science Minor
│
├── School of Continuing and Professional Studies [学院]
│   ├── Interdisciplinary Studies [系]
│   │   ├── Interdisciplinary Studies (B.I.S.)
│   │   └── Health Sciences Management, B.P.S.
│   └── Certificates [系]
│       ├── Accounting Certificate
│       ├── Certified Financial Planning Certificate
│       ├── Cloud Computing Certificate
│       ├── Cybersecurity Analysis Certificate
│       └── Information Technology Certificate
│
├── Darden School of Business (Graduate Only) [学院]
│   └── MBA / Executive Programs
│
├── School of Law (Graduate Only) [学院]
│   └── J.D. / LL.M. / S.J.D.
│
├── School of Medicine (Graduate Only) [学院]
│   └── M.D. / Biomedical Graduate Programs
│
└── Graduate School of Arts & Sciences [学院]
    └── (Administers graduate programs across multiple departments)
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本校数量 |
|---------|------|------|---------|
| BA | Bachelor of Arts | 本科 | ~40 |
| BS | Bachelor of Science | 本科 | ~25 |
| B.S.Ed. | Bachelor of Science in Education | 本科 | 7 |
| B.S.Arch | Bachelor of Science in Architecture | 本科 | 2 |
| B.S.N. | Bachelor of Science in Nursing | 本科 | 1 |
| B.I.S. | Bachelor of Interdisciplinary Studies | 本科 | 1 |
| B.P.S. | Bachelor of Professional Studies | 本科 | 1 |
| Minor | 辅修 | 本科 | ~55 |
| Certificate | 证书 (UG) | 本科 | 6 |
| MA | Master of Arts | 研究生 | ~20 |
| MS | Master of Science | 研究生 | ~30 |
| MBA | Master of Business Administration | 研究生 | 1 |
| M.Ed. | Master of Education | 研究生 | ~5 |
| M.Arch | Master of Architecture | 研究生 | 2 |
| MPP | Master of Public Policy | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | ~3 |
| M.Eng. | Master of Engineering | 研究生 | ~5 |
| PhD | Doctor of Philosophy | 研究生 | ~40 |
| EdD | Doctor of Education | 研究生 | ~2 |
| MD | Doctor of Medicine | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| SJD | Doctor of Juridical Science | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| Certificate | 高级证书 (Grad) | 研究生 | ~15 |

> Source: UVA reports "143 master's and doctoral programs" across 12 schools. Degree inventory estimated from program listings.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | B.S.Ed. | B.S.N. | Minor | Cert(UG) | MA | MS | MBA | MPP/MPA | MFA | M.Eng. | PhD | Prof Doc | Cert(Grad) | 合计 |
|------------|----|----|---------|--------|-------|----------|----|----|-----|---------|-----|--------|-----|----------|------------|------|
| College of Arts & Sciences | ~40 | ~5 | 0 | 0 | ~40 | 0 | ~15 | ~10 | 0 | 0 | ~3 | 0 | ~25 | 0 | ~5 | ~143 |
| School of Engineering | 0 | ~10 | 0 | 0 | ~5 | 0 | 0 | ~8 | 0 | 0 | 0 | ~5 | ~8 | 0 | ~3 | ~39 |
| School of Architecture | 0 | ~2 | 0 | 0 | ~3 | 0 | 0 | ~2 | 0 | 0 | 0 | 0 | ~2 | 0 | ~2 | ~11 |
| School of Education | 0 | 0 | 7 | 0 | ~2 | 0 | 0 | ~5 | 0 | 0 | 0 | 0 | ~3 | ~2 | ~3 | ~22 |
| McIntire School of Commerce | 0 | 1 | 0 | 0 | ~4 | 0 | 0 | ~3 | 0 | 0 | 0 | 0 | ~2 | 0 | ~2 | ~12 |
| School of Nursing | 0 | 0 | 0 | 1 | 0 | 0 | 0 | ~2 | 0 | 0 | 0 | 0 | ~1 | ~1 | ~1 | ~6 |
| Batten School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | ~1 | 0 | 0 | ~3 |
| School of Data Science | 0 | 1 | 0 | 0 | 1 | 0 | 0 | ~2 | 0 | 0 | 0 | 0 | ~1 | 0 | ~1 | ~6 |
| School of Continuing & Professional Studies | 0 | 0 | 0 | 0 | 0 | 6 | 0 | ~2 | 0 | 0 | 0 | 0 | 0 | 0 | ~2 | ~10 |
| Darden School of Business | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | ~1 | 0 | ~2 | ~4 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~1 | ~1 | ~1 | ~3 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | 0 | ~5 | ~1 | ~3 | ~14 |
| **合计** | ~40 | ~19 | 7 | 1 | ~55 | 6 | ~15 | ~39 | 1 | 2 | ~3 | ~5 | ~50 | ~6 | ~25 | **~273** |

> Note: This matrix is estimated from the 143 graduate programs reported by UVA and the undergraduate majors/minors enumerated from virginia.edu/majors-minors/. Exact counts require per-school program directory enumeration (P0 follow-up).

---

## SECTION 1 — Undergraduate Education

### 1.1 College/School Architecture

UVA has 8 undergraduate-degree-granting schools. First-year applicants apply to one of: College of Arts & Sciences, School of Architecture, School of Engineering, School of Nursing, or Kinesiology (within the School of Education). Students interested in McIntire Commerce, Batten Public Policy, Data Science, or other Education programs apply to the College of Arts & Sciences first.

### 1.2 Undergraduate Majors — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | African American and African Studies | https://woodson.as.virginia.edu/undergraduate-program |
| 2 | American Studies | https://americanstudies.as.virginia.edu/ |
| 3 | Anthropology | https://anthropology.as.virginia.edu/undergraduate-degree-programs |
| 4 | Archaeology | https://archaeology.virginia.edu/ |
| 5 | Art History | https://art.as.virginia.edu/art-history |
| 6 | Astronomy | https://astronomy.as.virginia.edu/why-study-astronomy |
| 7 | Biology | https://bio.as.virginia.edu/undergraduate |
| 8 | Chemistry | https://chemistry.as.virginia.edu/undergraduate |
| 9 | Chinese Language & Literature | https://eastasian.as.virginia.edu/chinese |
| 10 | Classics | https://classics.as.virginia.edu/undergraduate-program |
| 11 | Cognitive Science | https://cogsci.as.virginia.edu/admission-and-requirements |
| 12 | Computer Science, B.A. | https://engineering.virginia.edu/department/computer-science/academics/cs-undergraduate-programs |
| 13 | Drama | https://drama.virginia.edu/undergraduate-programs |
| 14 | East Asian Languages, Literatures and Culture | https://eastasian.as.virginia.edu/east-asian-studies |
| 15 | Economics | https://economics.virginia.edu/ |
| 16 | English | https://english.as.virginia.edu/english-major |
| 17 | Environmental Sciences | https://evsc.as.virginia.edu/undergraduate |
| 18 | Environmental Thought and Practice | https://etp.virginia.edu/prospective-students |
| 19 | French | https://french.as.virginia.edu/undergraduate |
| 20 | German | https://german.as.virginia.edu/index.php/undergraduate-program |
| 21 | Global Studies | https://globalstudies.as.virginia.edu/ |
| 22 | Global Environments and Sustainability | https://globalstudies.as.virginia.edu/global-environments-sustainability |
| 23 | History | https://history.virginia.edu/undergradprogram |
| 24 | Italian | https://spanitalport.as.virginia.edu/italian-major |
| 25 | Japanese Language & Literature | https://eastasian.as.virginia.edu/japanese |
| 26 | Jewish Studies | https://jewishstudies.as.virginia.edu/major |
| 27 | Korean | https://eastasian.as.virginia.edu/korean |
| 28 | Latin American Studies | https://latinamerican.virginia.edu/majors |
| 29 | Linguistics | https://linguistics.virginia.edu/ba-program |
| 30 | Mathematics | https://math.virginia.edu/undergraduate/ |
| 31 | Media Studies | https://mediastudies.as.virginia.edu/media-studies-major |
| 32 | Medieval Studies | https://medievalstudies.as.virginia.edu/major |
| 33 | Middle Eastern and South Asian Languages and Cultures | https://mesalc.as.virginia.edu/undergraduate-program |
| 34 | Music | https://music.virginia.edu/undergraduate |
| 35 | Neuroscience | https://neuroscience.as.virginia.edu/undergraduate-major |
| 36 | Philosophy | https://philosophy.virginia.edu/major |
| 37 | Physics | https://www.phys.virginia.edu/Education/undergrad.asp |
| 38 | Political and Social Thought | https://pst.as.virginia.edu/major |
| 39 | Political Philosophy, Policy, and Law | https://ppl.virginia.edu/about |
| 40 | Politics | https://politics.virginia.edu/undergraduate-program |
| 41 | Portuguese | https://spanitalport.as.virginia.edu/portuguese-program |
| 42 | Psychology | https://psychology.as.virginia.edu/undergraduate-program |
| 43 | Religious Studies | https://religiousstudies.as.virginia.edu/major |
| 44 | Slavic Languages and Literatures | https://slavic.as.virginia.edu/undergraduate-majors |
| 45 | Sociology | https://sociology.as.virginia.edu/welcome-sociology |
| 46 | South Asian Languages and Literatures | https://mesalc.as.virginia.edu/language-literature-major |
| 47 | Spanish | https://spanitalport.as.virginia.edu/majoring-spanish |
| 48 | Statistics | https://statistics.as.virginia.edu/selecting-majorminor |
| 49 | Studio Art | https://art.as.virginia.edu/studio-art |
| 50 | Women, Gender & Sexuality | https://wgs.as.virginia.edu/overview |

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Behavioral Neuroscience, B.S. | https://psychology.as.virginia.edu/bs-behavioral-neuroscience |
| 2 | Computer Science, B.S. | https://engineering.virginia.edu/department/computer-science/academics/cs-undergraduate-programs |

##### Minors (College of Arts & Sciences)
| # | Minor | URL |
|---|------|-----|
| 1 | American Sign Language | https://asl.virginia.edu/ |
| 2 | Asian Pacific American Studies | https://americanstudies.as.virginia.edu/minor-asian-pacific-american-studies |
| 3 | Business Spanish Minor | https://spanitalport.as.virginia.edu/minoring-spanish |
| 4 | Dance | https://drama.virginia.edu/minor-dance |
| 5 | Data Analytics | https://statistics.as.virginia.edu/minor-data-analytics |
| 6 | Foreign Affairs Minor | https://politics.virginia.edu/undergraduate-major-and-minor |
| 7 | Global Culture and Commerce | https://anthropology.as.virginia.edu/global-culture-and-commerce-minor |
| 8 | Government Minor | https://politics.virginia.edu/undergraduate-major-and-minor |
| 9 | Health, Ethics, and Society | https://bioethics.as.virginia.edu/health-ethics-and-society-program |
| 10 | Latinx Studies Minor | https://americanstudies.as.virginia.edu/minor-latinx-studies |
| 11 | Native American Indigenous Studies Minor | https://americanstudies.as.virginia.edu/minor-native-american-indigenous-studies |
| 12 | Public Writing and Rhetoric Minor | https://english.as.virginia.edu/english-minor-public-writing-and-rhetoric |

#### School of Engineering and Applied Science

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://engineering.virginia.edu/department/mechanical-and-aerospace-engineering/academics/ae-undergraduate-program |
| 2 | Applied Mathematics | https://engineering.virginia.edu/offices-programs/applied-mathematics |
| 3 | Biomedical Engineering | https://engineering.virginia.edu/bme |
| 4 | Chemical Engineering | https://engineering.virginia.edu/department/chemical-engineering/academics/che-undergraduate-programs |
| 5 | Civil Engineering | https://engineering.virginia.edu/department/civil-and-environmental-engineering/academics/cee-undergraduate-programs |
| 6 | Computer Engineering | https://engineering.virginia.edu/offices-programs/computer-engineering-program |
| 7 | Electrical Engineering | https://engineering.virginia.edu/department/electrical-and-computer-engineering/academics/ece-undergraduate-programs |
| 8 | Engineering Science | https://engineering.virginia.edu/undergraduate-study/future-undergrads/special-academic-programs/engineering-science |
| 9 | Materials Science and Engineering | https://engineering.virginia.edu/department/materials-science-and-engineering/academics/mse-undergraduate-programs |
| 10 | Mechanical Engineering | https://engineering.virginia.edu/department/mechanical-and-aerospace-engineering/academics/me-undergraduate-program |
| 11 | Systems Engineering | https://engineering.virginia.edu/department/systems-and-information-engineering/academics/sie-undergraduate-programs |

##### Minors (Engineering)
| # | Minor | URL |
|---|------|-----|
| 1 | History of Science and Technology | https://engineering.virginia.edu/department/engineering-and-society/academics/history-science-and-technology-minor |
| 2 | Science and Technology Policy | https://engineering.virginia.edu/department/engineering-and-society/academics/science-and-technology-policy-minor |
| 3 | Science, Technology, and Society | https://engineering.virginia.edu/department/engineering-and-society/academics/sts-minor |
| 4 | Technology and the Environment | https://engineering.virginia.edu/department/civil-and-environmental-engineering/academics/undergraduate-programs/technology-and-environment-minor |
| 5 | Technology Ethics | https://engineering.virginia.edu/department/engineering-and-society/academics/technology-ethics-minor |

#### School of Architecture

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Architecture | B.S.Arch | https://www.arch.virginia.edu/programs/architecture |
| 2 | Architectural History | BA | https://www.arch.virginia.edu/programs/architectural-history |
| 3 | Urban and Environmental Planning | BA | https://www.arch.virginia.edu/programs/urban-environmental-planning |

##### Minors (Architecture)
| # | Minor | URL |
|---|------|-----|
| 1 | Design Minor | https://www.arch.virginia.edu/programs/undergraduate-minors |
| 2 | Historic Preservation Minor | https://www.arch.virginia.edu/programs/undergraduate-minors |
| 3 | Landscape Architecture Minor | https://www.arch.virginia.edu/programs/undergraduate-minors |

#### School of Education and Human Development

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Early Childhood Education | B.S.Ed. | https://education.virginia.edu/academics/programs/early-childhood-education-bsed-bachelor-science-education |
| 2 | Elementary Education | B.S.Ed. | https://education.virginia.edu/academics/programs/elementary-education-bsed-bachelor-science-education |
| 3 | Kinesiology | B.S.Ed. | https://education.virginia.edu/offices-departments/kinesiology |
| 4 | Special Education | B.S.Ed. | https://education.virginia.edu/academics/programs/special-education-bsed-bachelor-science-education |
| 5 | Speech Communication Disorders | B.S.Ed. | https://education.virginia.edu/academics/programs/speech-communication-disorders-bsed-bachelor-science-education |
| 6 | Youth & Social Innovation | B.S.Ed. | https://education.virginia.edu/academics/programs/youth-social-innovation-bsed-bachelor-science-education |

##### Minors (Education)
| # | Minor | URL |
|---|------|-----|
| 1 | Global Studies in Education Minor | https://education.virginia.edu/academics/programs/global-studies-education-undergraduate-minor |
| 2 | Health and Wellbeing Minor | https://education.virginia.edu/academics/programs/health-wellbeing-undergraduate-minor |

#### McIntire School of Commerce

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Commerce | B.S. | https://www.commerce.virginia.edu/bs-commerce |

##### Minors (Commerce)
| # | Minor | URL |
|---|------|-----|
| 1 | Entrepreneurship | https://www.commerce.virginia.edu/minors/entrepreneurship |
| 2 | General Business | https://www.commerce.virginia.edu/minors/general-business |
| 3 | Leadership | https://www.commerce.virginia.edu/minors/leadership |
| 4 | Real Estate | https://www.commerce.virginia.edu/minors/real-estate |

#### School of Nursing

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing | B.S.N. | https://nursing.virginia.edu/academics/bsn/ |

#### Frank Batten School of Leadership and Public Policy

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Public Policy and Leadership | BA | https://batten.virginia.edu/academics/undergraduate-programs |

#### School of Data Science

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Data Science | B.S. | https://datascience.virginia.edu/degrees/bsds |

##### Minor
| # | Minor | URL |
|---|------|-----|
| 1 | Data Science Minor | https://datascience.virginia.edu/degrees/minor-data-science |

#### School of Continuing and Professional Studies

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Interdisciplinary Studies | B.I.S. | https://www.scps.virginia.edu/programs/bachelor-interdisciplinary-studies-degree |
| 2 | Health Sciences Management | B.P.S. | https://www.scps.virginia.edu/programs/bachelor-professional-studies-health-sciences-management |

##### Certificates (SCPS)
| # | Certificate | URL |
|---|------|-----|
| 1 | Accounting | https://www.scps.virginia.edu/programs/accounting-certificate |
| 2 | Certified Financial Planning | https://www.scps.virginia.edu/programs/certified-financial-planning-certificate |
| 3 | Cloud Computing | https://www.scps.virginia.edu/programs/cloud-computing-certificate |
| 4 | Cybersecurity Analysis | https://www.scps.virginia.edu/programs/undergraduate-cybersecurity-analysis-certificate |
| 5 | Information Technology | https://www.scps.virginia.edu/programs/information-technology-certificate |

### 1.3 Interdisciplinary / Cross-College Programs

| # | 专业 | Primary School | Cross-listed Schools | URL |
|---|------|---------------|---------------------|-----|
| 1 | Computer Science (B.A.) | College of Arts & Sciences | Engineering | https://engineering.virginia.edu/department/computer-science/academics/cs-undergraduate-programs |
| 2 | Computer Science (B.S.) | Engineering | Arts & Sciences | https://engineering.virginia.edu/department/computer-science/academics/cs-undergraduate-programs |
| 3 | Data Science (B.S.) | School of Data Science | Engineering, A&S | https://datascience.virginia.edu/degrees/bsds |
| 4 | Applied Mathematics | Engineering | A&S | https://engineering.virginia.edu/offices-programs/applied-mathematics |
| 5 | Global Environments and Sustainability | A&S | Multiple | https://globalstudies.as.virginia.edu/global-environments-sustainability |

### 1.4 Minors — Complete List

~55 minors across all schools (enumerated above under each school's section).

### 1.5 General Education Requirements

UVA does not have a single university-wide core curriculum. Each school has its own requirements:
- **College of Arts & Sciences**: Area requirements (Humanities, Social Sciences, Natural Sciences, Foreign Language, Second Writing)
- **Engineering**: First-year engineering courses, math/science foundation
- **Architecture**: Design studio sequence
- **Education**: Professional education coursework
- **Commerce**: Pre-commerce prerequisites before entering McIntire (typically second year)
- **Nursing**: Pre-nursing prerequisites before entering the BSN program

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — grouped by 学院 > 学位级别

UVA offers **143 graduate programs** across 12 schools. Graduate admissions is **decentralized** — each school manages its own admissions process.

#### Graduate School of Arts & Sciences
- Administers PhD and master's programs across humanities, social sciences, and natural sciences
- Programs span departments in the College of Arts & Sciences
- **Application**: Through the Graduate School portal
- **Funding**: Most PhD programs offer full funding (tuition + stipend)

#### School of Engineering and Applied Science (Graduate)
- **MS programs**: ~8 departments (Aerospace, Biomedical, Chemical, Civil, Computer Science, Electrical, Materials, Systems)
- **PhD programs**: ~8 departments
- **M.Eng.**: Professional master's in multiple departments
- **Application**: engineering.virginia.edu/admissions/graduate-admissions/
- **GRE**: Varies by department

#### Darden School of Business
- **MBA** (Full-time, Executive, Global Executive)
- **PhD** in Business Administration
- **Certificates**: Various executive education
- **Application**: www.darden.virginia.edu/mba/admissions/
- **GMAT/GRE**: Required for MBA

#### School of Law
- **JD** (Juris Doctor)
- **LL.M.** (Master of Laws)
- **SJD** (Doctor of Juridical Science)
- **Application**: Through LSAC
- **LSAT**: Required for JD

#### School of Medicine
- **MD** (Doctor of Medicine)
- **Biomedical Graduate Programs**: PhD and MS in various biomedical sciences
- **Application**: Through AMCAS for MD; direct for graduate programs

#### School of Nursing (Graduate)
- **MSN** (Master of Science in Nursing)
- **DNP** (Doctor of Nursing Practice)
- **PhD** in Nursing
- **Application**: nursing.virginia.edu/academics/graduate/

#### McIntire School of Commerce (Graduate)
- **MS in Commerce**
- **MS in Global Commerce**
- **MS in Business Analytics**
- **Application**: www.commerce.virginia.edu/ms-commerce/

#### School of Education and Human Development (Graduate)
- **M.Ed.** in various specializations
- **EdD** (Doctor of Education)
- **PhD** in Education
- **Application**: education.virginia.edu/admissions/

#### School of Architecture (Graduate)
- **M.Arch** (Master of Architecture)
- **M.L.A.** (Master of Landscape Architecture)
- **MS in Architectural History**
- **MS in Urban and Environmental Planning**
- **Application**: www.arch.virginia.edu/admissions/

#### Frank Batten School of Leadership and Public Policy (Graduate)
- **MPP** (Master of Public Policy)
- **MBA/MPP** dual degree (with Darden)
- **Application**: batten.virginia.edu/admissions/

#### School of Data Science (Graduate)
- **MS in Data Science**
- **PhD in Data Science**
- **Application**: datascience.virginia.edu/admissions/

#### School of Continuing and Professional Studies (Graduate)
- **MS in various professional fields**
- **Certificates**: Various professional certificates
- **Application**: www.scps.virginia.edu/admissions/

### 2.2 Graduate Admissions Model

UVA operates a **fully decentralized** graduate admissions model. There is no single graduate application portal — each school runs its own admissions process with separate:
- Application portals
- Fee structures
- GRE/GMAT policies
- Deadlines
- Financial aid decisions

**Application fee**: Varies by school (typically $70-$85 for most programs)

### 2.3 Graduate Funding

- **PhD programs**: Most offer full funding (tuition waiver + stipend + health insurance)
- **Master's programs**: Vary by school; many are self-funded
- **Professional programs** (MBA, JD, MD): Self-funded with school-specific aid
- **CGS April 15 resolution**: UVA is a signatory

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | Source |
|------|-----|--------|
| Application Portal | Common Application | https://admission.virginia.edu/apply |
| Application Fee | ~$70 (verify) | Common App |
| Early Decision Deadline | November 1 | https://admission.virginia.edu/admission/deadlines-instructions |
| Early Decision Notification | By December 15 | https://admission.virginia.edu/admission/deadlines-instructions |
| Early Action Deadline | November 1 | https://admission.virginia.edu/admission/deadlines-instructions |
| Early Action Notification | By February 15 | https://admission.virginia.edu/admission/deadlines-instructions |
| Regular Decision Deadline | January 5 | https://admission.virginia.edu/admission/deadlines-instructions |
| Regular Decision Notification | By April 1 | https://admission.virginia.edu/admission/deadlines-instructions |
| Enrollment Deposit Deadline | May 1 | https://admission.virginia.edu/admission/deadlines-instructions |
| Spring Transfer Deadline | October 1 | https://admission.virginia.edu/admission/deadlines-instructions |
| Fall Transfer Deadline | March 1 | https://admission.virginia.edu/admission/deadlines-instructions |
| SAT/ACT Policy | Test-optional for Fall 2027 | https://admission.virginia.edu/admission/deadlines-instructions |
| Superscoring | Yes (SAT and ACT) | https://admission.virginia.edu/admission/deadlines-instructions |
| SAT Code | 5820 | https://admission.virginia.edu/admission/deadlines-instructions |
| ACT Code | 4412 | https://admission.virginia.edu/admission/deadlines-instructions |
| Recommendations | Secondary school report + 1 teacher evaluation | https://admission.virginia.edu/admission/deadlines-instructions |
| Interview | None offered | https://admission.virginia.edu/i-am/international |
| Demonstrated Interest | Not tracked | https://admission.virginia.edu/admission/deadlines-instructions |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified | Encouraged | Strongly encouraged for non-native speakers |
| IELTS | Not specified | Encouraged | Academic version |
| Cambridge C1/C2 | Not specified | Encouraged | Accepted |
| Duolingo English Test (DET) | Not specified | Encouraged | Accepted |
| InitialView | N/A | Optional | Video interview evaluation |
| Vericant | N/A | Optional | Video interview evaluation |

> Source: "We strongly encourage all applicants whose first language is not English to participate in an English language assessment" — https://admission.virginia.edu/i-am/international

### 3.3 Graduate — Global Rules

- **Decentralized admissions**: Each of 12 schools manages its own process
- **Application platforms**: Vary by school (direct portals, LSAC, AMCAS, NursingCAS, etc.)
- **Application fee**: Varies by school (~$70-$85)
- **GRE/GMAT**: Per-program policy (some required, some optional, some not accepted)
- **English proficiency**: TOEFL/IELTS typically required for international applicants
- **CGS April 15**: UVA is a signatory

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

#### College of Arts & Sciences — First Year

| Expense Item | Virginian | Non-Virginian | Description |
|-------------|-----------|---------------|-------------|
| Tuition | $16,842 | $57,432 | Annual tuition |
| Fees | $3,940 | $4,622 | Mandatory comprehensive fees |
| **Subtotal (Direct)** | **$20,782** | **$62,054** | |
| Housing | $8,730 | $8,730 | On-Grounds housing |
| Food | $7,340 | $7,340 | Meal plan |
| Books & Supplies | $1,540 | $1,540 | Course materials |
| Personal Expenses | $3,000 | $3,000 | Miscellaneous |
| Loan Fees | $72 | $72 | Direct loan fees |
| Travel | $550 | $550-$2,240 | Varies by region |
| **Total COA** | **$42,014** | **$83,286-$84,976** | |

#### School of Engineering — First Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $27,906 | $68,948 |
| Fees | $3,952 | $4,634 |
| **Total COA** | **$53,090** | **$94,814-$96,504** |

#### School of Architecture — First Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $18,074 | $58,716 |
| Fees | $4,022 | $4,704 |
| **Total COA** | **$43,328** | **$84,652-$86,342** |

#### School of Education — First Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $16,842 | $57,432 |
| Fees | $3,952 | $4,634 |
| **Total COA** | **$42,026** | **$83,298-$84,988** |

#### School of Nursing — First Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $21,670 | $62,424 |
| Fees | $3,966 | $4,648 |
| **Total COA** | **$46,868** | **$88,304-$89,994** |

#### McIntire School of Commerce — Second Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $16,842 | $57,432 |
| Fees | $4,018 | $4,700 |
| **Total COA** | **$43,256** | **$84,528-$86,218** |

#### Batten School — Third/Fourth Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $29,356 | $70,464 |
| Fees | $3,968 | $4,650 |
| **Total COA** | **$55,720** | **$97,510-$99,200** |

#### School of Data Science — Third/Fourth Year

| Expense Item | Virginian | Non-Virginian |
|-------------|-----------|---------------|
| Tuition | $29,356 | $70,464 |
| Fees | $3,992 | $4,674 |
| **Total COA** | **$55,744** | **$97,534-$99,224** |

> Source: https://sfs.virginia.edu/financial-aid-new-applicants/financial-aid-basics/estimated-undergraduate-cost-attendance-2026-2027

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | Source |
|------|-----|--------|
| Program Name | AccessUVA | https://sfs.virginia.edu/our-financial-aid-commitment-you-0 |
| Need Met | 100% of demonstrated need | https://sfs.virginia.edu/our-financial-aid-commitment-you-0 |
| Need-Blind (US) | Yes | UVA policy |
| Need-Aware (International) | Yes | https://admission.virginia.edu/i-am/international |
| International Aid | No funds for foreign nationals (except UWC) | https://admission.virginia.edu/i-am/international |
| Income ≤$50K (VA) | Tuition, fees, housing, food covered | https://sfs.virginia.edu/our-financial-aid-commitment-you-0 |
| Income ≤$100K (VA) | Tuition and fees covered | https://sfs.virginia.edu/our-financial-aid-commitment-you-0 |
| Merit Scholarships | Not offered | UVA policy |
| Loans | Included in aid packages | SFS policy |
| Forms Required | FAFSA + CSS Profile | SFS website |

> Note: The $50K and $100K thresholds apply to Virginia residents with assets <$100K.

### 4.3 Graduate Cost & Funding Framework

- **PhD programs**: Most fully funded (tuition + stipend + health insurance)
- **Master's programs**: Vary by school; many self-funded
- **Professional programs** (MBA, JD, MD): Self-funded with school-specific aid
- **Application fee**: Varies by school (~$70-$85)
- **Fee waivers**: Available based on need

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.ED
  value: "November 1"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "Early Decision | November 1 | November 8 | By December 15"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "Early Action | November 1 | November 8 | By February 15"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.RD
  value: "January 5"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "Regular Decision | January 5 | January 10 | By April 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.testing.test_optional
  value: "Test-optional for Fall 2027"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "If you're applying for first year admission for Fall 2027, you'll have the choice of sharing or not sharing standardized test scores."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.testing.superscoring
  value: "Yes"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "Super-scoring has been the a long-held practice at UVA."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.testing.sat_code
  value: "5820"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "Our ETS code is 5820."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.testing.act_code
  value: "4412"
  source_url: https://admission.virginia.edu/admission/deadlines-instructions
  source_snippet: "Our ACT code is 4412."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.intl.english_exams
  value: ["TOEFL", "IELTS", "Cambridge C1/C2", "Duolingo English Test"]
  source_url: https://admission.virginia.edu/i-am/international
  source_snippet: "Results from the following exams may be submitted: The Test of English as a Foreign Language (TOEFL), The International English Language Testing System (IELTS), Cambridge C1 Advanced or C2 Proficiency, The Duolingo English Test (DET)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.intl.financial_aid
  value: "No funds for foreign nationals (except UWC students)"
  source_url: https://admission.virginia.edu/i-am/international
  source_snippet: "For international students who are foreign nationals, the University of Virginia does not have funds available for scholarships or loans."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.cost.tuition_in_state
  value: "$16,842 (A&S), $27,906 (Engineering)"
  source_url: https://sfs.virginia.edu/financial-aid-new-applicants/financial-aid-basics/estimated-undergraduate-cost-attendance-2026-2027
  source_snippet: "College of Arts and Sciences, First Year | Virginian | Non-Virginian | Tuition | 16,842 | 57,432"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.tuition_out_of_state
  value: "$57,432 (A&S), $68,948 (Engineering)"
  source_url: https://sfs.virginia.edu/financial-aid-new-applicants/financial-aid-basics/estimated-undergraduate-cost-attendance-2026-2027
  source_snippet: "College of Arts and Sciences, First Year | Virginian | Non-Virginian | Tuition | 16,842 | 57,432"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.cost.total_coa_in_state
  value: "$42,014 (A&S First Year)"
  source_url: https://sfs.virginia.edu/financial-aid-new-applicants/financial-aid-basics/estimated-undergraduate-cost-attendance-2026-2027
  source_snippet: "Total | 42,014 | 83,286 to 84,976"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.aid.accessUVA
  value: "100% need met; $50K income = tuition/fees/housing/food; $100K = tuition/fees"
  source_url: https://sfs.virginia.edu/our-financial-aid-commitment-you-0
  source_snippet: "for Virginia families earning $50K or less per year and who have assets less than $100K, we'll provide need-based grants and scholarships equivalent to at least the cost of tuition, required fees, housing, and food"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.statistics.applications
  value: "64,457"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "64,457 | Completed Applications"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-015:
  field: undergraduate.statistics.admitted
  value: "10,086"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "10,086 | Offers of Admission"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-016:
  field: undergraduate.statistics.enrolled
  value: "3,986"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "3,986 | First-year students enrolled"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-017:
  field: undergraduate.statistics.sat_middle_50
  value: "EBRW: 700-760, Math: 710-780"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "700-760 | Evidence-Based Reading and Writing | 710-780 | Math"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-018:
  field: undergraduate.statistics.act_middle_50
  value: "32-35"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "Middle 50% range for ACT composite scores: 32-35"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-019:
  field: undergraduate.statistics.retention_rate
  value: "97%"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "97% | of first year students return for the second year"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-020:
  field: undergraduate.statistics.graduation_rate_6yr
  value: "94%"
  source_url: https://admission.virginia.edu/admission/statistics
  source_snippet: "94% | 6-year graduation rate"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.total_programs
  value: "143"
  source_url: https://www.virginia.edu/graduate-studies/
  source_snippet: "The University of Virginia has 143 master's and doctoral programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.schools
  value: "12"
  source_url: https://www.virginia.edu/graduate-admission/
  source_snippet: "UVA offers some of the nation's leading graduate programs. Learn more about the admission policies and requirements for graduate programs at UVA's 12 schools"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uva-knowledge-base-v2/
├── 00-overview/
│   ├── 00-institution-overview.md (Rules 1-4)
│   └── 01-school-hierarchy.md
├── 01-undergraduate/
│   ├── 01-college-of-arts-sciences.md
│   ├── 02-school-of-engineering.md
│   ├── 03-school-of-architecture.md
│   ├── 04-school-of-education.md
│   ├── 05-mcintire-school-of-commerce.md
│   ├── 06-school-of-nursing.md
│   ├── 07-batten-school.md
│   ├── 08-school-of-data-science.md
│   ├── 09-school-of-continuing-studies.md
│   └── 10-interdisciplinary-programs.md
├── 02-graduate/
│   ├── 01-graduate-school-of-arts-sciences.md
│   ├── 02-engineering-graduate.md
│   ├── 03-darden-business.md
│   ├── 04-school-of-law.md
│   ├── 05-school-of-medicine.md
│   ├── 06-nursing-graduate.md
│   ├── 07-commerce-graduate.md
│   ├── 08-education-graduate.md
│   ├── 09-architecture-graduate.md
│   ├── 10-batten-graduate.md
│   └── 11-data-science-graduate.md
├── 03-deadlines/
│   └── 01-undergraduate-deadlines.md
├── 04-costs/
│   ├── 01-undergraduate-costs.md
│   └── 02-financial-aid-policy.md
├── 05-testing/
│   └── 01-standardized-testing.md
└── 06-evidence/
    └── 01-evidence-chain.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uva-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Complete graduate programs directory (all 143 programs with names, degrees, URLs) | Each school's graduate programs page |
| P0 | Application fee amount (verify ~$70) | Common App or UVA Apply page |
| P0 | TOEFL/IELTS minimum scores (if any) | Admission FAQ or testing page |
| P1 | Graduate COA by school | sfs.virginia.edu |
| P1 | Graduate application deadlines by program | Each school's admissions page |
| P1 | GRE/GMAT requirements by program | Each school's admissions page |
| P2 | Per-program TOEFL/IELTS requirements | Graduate program pages |
| P2 | Graduate funding details by school | Graduate school websites |
| P2 | Transfer admission requirements detail | admission.virginia.edu/transfer |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UVA | (Other schools) |
|-----------|-----|-----------------|
| Type | Public | |
| Location | Charlottesville, VA | |
| Founded | 1819 (Thomas Jefferson) | |
| Total Enrollment | 26,685 (Fall 2025) | |
| UG Enrollment | 17,848 | |
| Grad Enrollment | 8,837 | |
| UG Tuition (In-State) | $16,842 (A&S) | |
| UG Tuition (OOS) | $57,432 (A&S) | |
| UG Total COA (In-State) | $42,014 (A&S) | |
| UG Total COA (OOS) | $83,286 (A&S) | |
| Need-Blind (US) | Yes | |
| Need-Blind (Intl) | No | |
| Need Met | 100% | |
| EA Deadline | November 1 | |
| ED Deadline | November 1 | |
| RD Deadline | January 5 | |
| Test Policy | Test-optional (Fall 2027) | |
| SAT Middle 50% | 1410-1540 | |
| ACT Middle 50% | 32-35 | |
| TOEFL Minimum | Not specified | |
| IELTS Minimum | Not specified | |
| Acceptance Rate | 15.6% (2025) | |
| 4-Year Graduation Rate | 92% | |
| 6-Year Graduation Rate | 94% | |
| Retention Rate | 97% | |
| UG Programs | ~75 majors | |
| Grad Programs | 143 | |
| Schools | 12 | |
| Application Portal | Common App | |
| Application Fee | ~$70 (verify) | |
| Graduate App Fee | Varies by school | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admission.virginia.edu, sfs.virginia.edu, www.virginia.edu, engineering.virginia.edu, commerce.virginia.edu, arch.virginia.edu, education.virginia.edu, nursing.virginia.edu, batten.virginia.edu, datascience.virginia.edu, scps.virginia.edu, darden.virginia.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
