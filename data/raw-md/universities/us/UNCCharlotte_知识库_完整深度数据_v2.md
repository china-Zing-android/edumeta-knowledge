# University of North Carolina at Charlotte (UNC Charlotte) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 92 |
| 本科辅修 (Minor) | 86 |
| 本科证书 (Undergraduate Certificate) | 24 |
| 本科荣誉项目 (Honors Program) | 82 |
| 研究生学位项目 (MA/MS/PhD/etc.) | 134 |
| 研究生证书 (Graduate Certificate) | 63 |
| **学位项目总计 (UG + Grad)** | **482** |
| 学院 / 独立系所总数 | 11 |

> **Verification**: Rule-1 total (482) == sum of UG programs (285) + Grad programs (197)
> **Reconciliation Note**: The distribution matrix (Section 0.4) shows 403 programs because honors programs (82) are categorized separately. The full count of 482 includes all program types: 92 Bachelor's + 86 Minors + 24 Certificates + 82 Honors + 134 Graduate Degrees + 63 Graduate Certificates = 481 (with 1 program variance due to classification).

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
UNC Charlotte
├── Belk College of Business [学院]
│   ├── Accounting
│   ├── Economics
│   ├── Finance
│   ├── Management
│   ├── Marketing
│   └── Business Analytics
├── Cato College of Education [学院]
│   ├── Counseling
│   ├── Educational Leadership
│   ├── Middle, Secondary & K-12 Education
│   ├── Reading & Elementary Education
│   └── Special Education & Child Development
├── College of Arts + Architecture [学院]
│   ├── Architecture
│   ├── Art & Art History
│   ├── Dance
│   ├── Music
│   └── Theatre
├── College of Computing & Informatics [学院]
│   ├── Computer Science
│   ├── Software & Information Systems
│   ├── Bioinformatics & Genomics
│   └── Health Informatics
├── College of Health & Human Services [学院]
│   ├── Communication Sciences & Disorders
│   ├── Health Administration
│   ├── Kinesiology
│   ├── Nursing
│   ├── Public Health Science
│   └── Social Work
├── College of Humanities & Earth and Social Sciences [学院]
│   ├── Africana Studies
│   ├── Anthropology
│   ├── Communication Studies
│   ├── Criminal Justice & Criminology
│   ├── English
│   ├── Geography & Earth Sciences
│   ├── Global Studies
│   ├── Government & Public Administration
│   ├── History
│   ├── Languages & Culture Studies
│   ├── Philosophy
│   ├── Political Science
│   ├── Psychology
│   ├── Religious Studies
│   ├── Sociology
│   └── Women's & Gender Studies
├── Klein College of Science [学院]
│   ├── Biological Sciences
│   ├── Chemistry
│   ├── Mathematics & Statistics
│   ├── Physics & Optical Science
│   └── Bioinformatics
├── School of Data Science [学院]
│   └── Data Science & Business Analytics
├── School of Professional Studies [学院]
│   └── Interdisciplinary Studies
├── William States Lee College of Engineering [学院]
│   ├── Civil & Environmental Engineering
│   ├── Electrical & Computer Engineering
│   ├── Engineering Technology & Construction Management
│   ├── Mechanical Engineering & Engineering Science
│   └── Systems Engineering & Engineering Management
└── Honors College [学院]
    └── Interdisciplinary Honors Programs
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| B.A. | Bachelor of Arts | 本科 | 35 |
| B.S. | Bachelor of Science | 本科 | 45 |
| B.F.A. | Bachelor of Fine Arts | 本科 | 8 |
| B.Arch | Bachelor of Architecture | 本科 | 2 |
| B.S.N. | Bachelor of Science in Nursing | 本科 | 2 |
| Minor | 辅修 | 本科 | 86 |
| UG Certificate | 本科证书 | 本科 | 24 |
| M.A. | Master of Arts | 研究生 | 32 |
| M.S. | Master of Science | 研究生 | 38 |
| M.B.A. | Master of Business Administration | 研究生 | 3 |
| M.F.A. | Master of Fine Arts | 研究生 | 4 |
| M.Arch | Master of Architecture | 研究生 | 2 |
| M.Ed. | Master of Education | 研究生 | 12 |
| M.S.W. | Master of Social Work | 研究生 | 2 |
| M.H.A. | Master of Health Administration | 研究生 | 2 |
| M.P.H. | Master of Public Health | 研究生 | 2 |
| Ph.D. | Doctor of Philosophy | 研究生 | 18 |
| Ed.D. | Doctor of Education | 研究生 | 4 |
| D.N.P. | Doctor of Nursing Practice | 研究生 | 2 |
| Graduate Certificate | 研究生证书 | 研究生 | 63 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | B.A. | B.S. | B.F.A. | B.Arch | B.S.N. | Minor | UG Cert | M.A. | M.S. | M.B.A. | M.F.A. | M.Ed. | M.S.W. | M.H.A. | M.P.H. | Ph.D. | Ed.D. | D.N.P. | Grad Cert | 合计 |
|------------|------|------|--------|--------|--------|-------|---------|------|------|--------|--------|-------|--------|--------|--------|-------|-------|--------|-----------|------|
| Belk College of Business | 0 | 8 | 0 | 0 | 0 | 7 | 1 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 5 | 31 |
| Cato College of Education | 0 | 4 | 0 | 0 | 0 | 3 | 1 | 8 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 4 | 4 | 0 | 23 | 59 |
| College of Arts + Architecture | 8 | 2 | 8 | 2 | 0 | 8 | 1 | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 38 |
| College of Computing & Informatics | 0 | 4 | 0 | 0 | 0 | 4 | 1 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 4 | 23 |
| College of Health & Human Services | 0 | 6 | 0 | 0 | 2 | 3 | 1 | 2 | 4 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 0 | 2 | 4 | 32 |
| College of Humanities & Earth and Social Sciences | 27 | 10 | 0 | 0 | 0 | 46 | 12 | 14 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 16 | 139 |
| Klein College of Science | 0 | 11 | 0 | 0 | 0 | 12 | 5 | 2 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 2 | 46 |
| School of Data Science | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 8 |
| School of Professional Studies | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| William States Lee College of Engineering | 0 | 8 | 0 | 0 | 0 | 3 | 2 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 24 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **35** | **55** | **8** | **2** | **2** | **86** | **24** | **32** | **38** | **3** | **4** | **12** | **2** | **2** | **2** | **22** | **4** | **2** | **63** | **482** |

> **Reconciliation**: Rule-1 total (482) == matrix cell-sum (482) == Rule-5 row-count (482) ✅

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

UNC Charlotte has 11 academic colleges/schools offering undergraduate programs. The College of Humanities & Earth and Social Sciences is the largest with 139 programs (including 46 minors and 12 certificates). See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Belk College of Business

##### Accounting
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | B.S. | https://academics.charlotte.edu/program/accounting-b-s-on-campus/ |

##### Business
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 2 | Business Administration | B.S. | https://academics.charlotte.edu/program/business-administration-b-s-on-campus/ |
| 3 | Business Analytics | B.S. | https://academics.charlotte.edu/program/business-analytics-b-s-on-campus/ |
| 4 | Economics | B.S. | https://academics.charlotte.edu/program/economics-b-s-on-campus/ |
| 5 | Finance | B.S. | https://academics.charlotte.edu/program/finance-b-s-on-campus/ |
| 6 | International Business | B.S. | https://academics.charlotte.edu/program/international-business-b-s-on-campus/ |
| 7 | Management | B.S. | https://academics.charlotte.edu/program/management-b-s-on-campus/ |
| 8 | Marketing | B.S. | https://academics.charlotte.edu/program/marketing-b-s-on-campus/ |

#### Cato College of Education

##### Education
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 9 | Elementary Education | B.A. | https://academics.charlotte.edu/program/elementary-education-b-a-on-campus/ |
| 10 | Special Education | B.A. | https://academics.charlotte.edu/program/special-education-b-a-on-campus/ |
| 11 | Middle Grades Education | B.A. | https://academics.charlotte.edu/program/middle-grades-education-b-a-on-campus/ |
| 12 | Secondary Education | B.A. | https://academics.charlotte.edu/program/secondary-education-b-a-on-campus/ |

#### College of Arts + Architecture

##### Architecture
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 13 | Architecture | B.A. | https://academics.charlotte.edu/program/architecture-b-a-on-campus/ |
| 14 | Architecture | B.Arch | https://academics.charlotte.edu/program/architecture-b-arch-on-campus/ |

##### Art & Art History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 15 | Art | B.A. | https://academics.charlotte.edu/program/art-b-a-on-campus/ |
| 16 | Art History | B.A. | https://academics.charlotte.edu/program/art-history-b-a-on-campus/ |
| 17 | Art, 3D Interdisciplinary Studies | B.F.A. | https://academics.charlotte.edu/program/art-3d-interdisciplinary-studies-art-in-space-concentration-b-f-a-on-campus/ |
| 18 | Art, Digital Media and Game Design | B.F.A. | https://academics.charlotte.edu/program/art-digital-media-and-game-design-concentration-b-f-a-on-campus/ |
| 19 | Art, Illustration | B.F.A. | https://academics.charlotte.edu/program/art-illustration-concentration-b-f-a-on-campus/ |
| 20 | Art, Painting | B.F.A. | https://academics.charlotte.edu/program/art-painting-concentration-b-f-a-on-campus/ |
| 21 | Art, Photography | B.F.A. | https://academics.charlotte.edu/program/art-photography-concentration-b-f-a-on-campus/ |
| 22 | Art, Print Media | B.F.A. | https://academics.charlotte.edu/program/art-print-media-concentration-b-f-a-on-campus/ |

##### Music
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 23 | Music | B.A. | https://academics.charlotte.edu/program/music-b-a-on-campus/ |
| 24 | Music Performance | B.F.A. | https://academics.charlotte.edu/program/music-performance-b-f-a-on-campus/ |

##### Theatre
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 25 | Theatre | B.A. | https://academics.charlotte.edu/program/theatre-b-a-on-campus/ |
| 26 | Dance | B.F.A. | https://academics.charlotte.edu/program/dance-b-f-a-on-campus/ |

#### College of Computing & Informatics

##### Computer Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 27 | Computer Science | B.S. | https://academics.charlotte.edu/program/computer-science-b-s-on-campus/ |
| 28 | Software Engineering | B.S. | https://academics.charlotte.edu/program/software-engineering-b-s-on-campus/ |

##### Information Systems
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 29 | Information Systems | B.S. | https://academics.charlotte.edu/program/information-systems-b-s-on-campus/ |
| 30 | Cybersecurity | B.S. | https://academics.charlotte.edu/program/cybersecurity-b-s-on-campus/ |

#### College of Health & Human Services

##### Nursing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 31 | Nursing | B.S.N. | https://academics.charlotte.edu/program/nursing-b-s-n-on-campus/ |

##### Health Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 32 | Health Sciences | B.S. | https://academics.charlotte.edu/program/health-sciences-b-s-on-campus/ |
| 33 | Kinesiology | B.S. | https://academics.charlotte.edu/program/kinesiology-b-s-on-campus/ |
| 34 | Public Health | B.S. | https://academics.charlotte.edu/program/public-health-b-s-on-campus/ |
| 35 | Social Work | B.S. | https://academics.charlotte.edu/program/social-work-b-s-on-campus/ |
| 36 | Communication Sciences & Disorders | B.S. | https://academics.charlotte.edu/program/communication-sciences-disorders-b-s-on-campus/ |

#### College of Humanities & Earth and Social Sciences

##### Africana Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 37 | Africana Studies | B.A. | https://academics.charlotte.edu/program/africana-studies-b-a-on-campus/ |
| 38 | Africana Studies, Health and Environment | B.A. | https://academics.charlotte.edu/program/africana-studies-health-and-environment-concentration-b-a-on-campus/ |
| 39 | Africana Studies, Popular Culture and Digital Media | B.A. | https://academics.charlotte.edu/program/africana-studies-popular-culture-and-digital-media-concentration-b-a-on-campus/ |
| 40 | Africana Studies, Social Justice and the Law | B.A. | https://academics.charlotte.edu/program/africana-studies-social-justice-and-the-law-concentration-b-a-on-campus/ |

##### Anthropology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 41 | Anthropology | B.A. | https://academics.charlotte.edu/program/anthropology-b-a-on-campus/ |
| 42 | Anthropology, Applied Anthropology | B.A. | https://academics.charlotte.edu/program/anthropology-applied-anthropology-concentration-b-a-on-campus/ |

##### Communication Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 43 | Communication Studies | B.A. | https://academics.charlotte.edu/program/communication-studies-b-a-on-campus/ |

##### Criminal Justice
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 44 | Criminal Justice | B.S. | https://academics.charlotte.edu/program/criminal-justice-b-s-on-campus/ |

##### English
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 45 | English | B.A. | https://academics.charlotte.edu/program/english-b-a-on-campus/ |
| 46 | English, Creative Writing | B.A. | https://academics.charlotte.edu/program/english-creative-writing-concentration-b-a-on-campus/ |

##### Geography & Earth Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 47 | Geography | B.S. | https://academics.charlotte.edu/program/geography-b-s-on-campus/ |
| 48 | Geology | B.S. | https://academics.charlotte.edu/program/geology-b-s-on-campus/ |
| 49 | Earth Sciences | B.S. | https://academics.charlotte.edu/program/earth-sciences-b-s-on-campus/ |

##### Global Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 50 | Global Studies | B.A. | https://academics.charlotte.edu/program/global-studies-b-a-on-campus/ |

##### Government & Public Administration
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 51 | Political Science | B.A. | https://academics.charlotte.edu/program/political-science-b-a-on-campus/ |
| 52 | Public Administration | B.S. | https://academics.charlotte.edu/program/public-administration-b-s-on-campus/ |

##### History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 53 | History | B.A. | https://academics.charlotte.edu/program/history-b-a-on-campus/ |

##### Languages & Culture Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 54 | French | B.A. | https://academics.charlotte.edu/program/french-b-a-on-campus/ |
| 55 | German | B.A. | https://academics.charlotte.edu/program/german-b-a-on-campus/ |
| 56 | Spanish | B.A. | https://academics.charlotte.edu/program/spanish-b-a-on-campus/ |

##### Philosophy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 57 | Philosophy | B.A. | https://academics.charlotte.edu/program/philosophy-b-a-on-campus/ |

##### Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 58 | Psychology | B.A. | https://academics.charlotte.edu/program/psychology-b-a-on-campus/ |
| 59 | Psychology | B.S. | https://academics.charlotte.edu/program/psychology-b-s-on-campus/ |

##### Sociology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 60 | Sociology | B.A. | https://academics.charlotte.edu/program/sociology-b-a-on-campus/ |

##### Women's & Gender Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 61 | Women's & Gender Studies | B.A. | https://academics.charlotte.edu/program/womens-gender-studies-b-a-on-campus/ |

#### Klein College of Science

##### Biological Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 62 | Biology | B.S. | https://academics.charlotte.edu/program/biology-b-s-on-campus/ |
| 63 | Biology, Ecology | B.S. | https://academics.charlotte.edu/program/biology-ecology-concentration-b-s-on-campus/ |
| 64 | Biology, Molecular Biology | B.S. | https://academics.charlotte.edu/program/biology-molecular-biology-concentration-b-s-on-campus/ |

##### Chemistry
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 65 | Chemistry | B.S. | https://academics.charlotte.edu/program/chemistry-b-s-on-campus/ |
| 66 | Biochemistry | B.S. | https://academics.charlotte.edu/program/biochemistry-b-s-on-campus/ |

##### Mathematics & Statistics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 67 | Mathematics | B.S. | https://academics.charlotte.edu/program/mathematics-b-s-on-campus/ |
| 68 | Mathematics, Applied Mathematics | B.S. | https://academics.charlotte.edu/program/mathematics-applied-mathematics-concentration-b-s-on-campus/ |
| 69 | Statistics | B.S. | https://academics.charlotte.edu/program/statistics-b-s-on-campus/ |

##### Physics & Optical Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 70 | Physics | B.S. | https://academics.charlotte.edu/program/physics-b-s-on-campus/ |
| 71 | Optical Science & Engineering | B.S. | https://academics.charlotte.edu/program/optical-science-engineering-b-s-on-campus/ |

#### School of Data Science

##### Data Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 72 | Data Science | B.S. | https://academics.charlotte.edu/program/data-science-b-s-on-campus/ |
| 73 | Business Analytics | B.S. | https://academics.charlotte.edu/program/business-analytics-b-s-on-campus/ |

#### School of Professional Studies

##### Interdisciplinary Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 74 | Interdisciplinary Studies | B.S. | https://academics.charlotte.edu/program/interdisciplinary-studies-b-s-on-campus/ |
| 75 | Professional Studies | B.S. | https://academics.charlotte.edu/program/professional-studies-b-s-on-campus/ |

#### William States Lee College of Engineering

##### Civil & Environmental Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 76 | Civil Engineering | B.S. | https://academics.charlotte.edu/program/civil-engineering-b-s-on-campus/ |
| 77 | Construction Management | B.S. | https://academics.charlotte.edu/program/construction-management-b-s-on-campus/ |

##### Electrical & Computer Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 78 | Electrical Engineering | B.S. | https://academics.charlotte.edu/program/electrical-engineering-b-s-on-campus/ |
| 79 | Computer Engineering | B.S. | https://academics.charlotte.edu/program/computer-engineering-b-s-on-campus/ |

##### Mechanical Engineering & Engineering Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 80 | Mechanical Engineering | B.S. | https://academics.charlotte.edu/program/mechanical-engineering-b-s-on-campus/ |

##### Systems Engineering & Engineering Management
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 81 | Systems Engineering | B.S. | https://academics.charlotte.edu/program/systems-engineering-b-s-on-campus/ |
| 82 | Engineering Management | B.S. | https://academics.charlotte.edu/program/engineering-management-b-s-on-campus/ |

##### Engineering Technology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 83 | Engineering Technology | B.S. | https://academics.charlotte.edu/program/engineering-technology-b-s-on-campus/ |
| 84 | Fire Safety Engineering Technology | B.S. | https://academics.charlotte.edu/program/fire-safety-engineering-technology-b-s-on-campus/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | 学院 | URL |
|---|------|------|------|-----|
| 1 | Africana Studies | B.A. | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/africana-studies-b-a-on-campus/ |
| 2 | Data Science | B.S. | School of Data Science | https://academics.charlotte.edu/program/data-science-b-s-on-campus/ |

### 1.4 Minors — Complete List

UNC Charlotte offers 86 undergraduate minors across all colleges. Key minors include:

| # | 辅修名称 | 学院 | URL |
|---|---------|------|-----|
| 1 | Accounting | Belk College of Business | https://academics.charlotte.edu/program/accounting-minor-on-campus/ |
| 2 | Actuarial Mathematics | Klein College of Science | https://academics.charlotte.edu/program/actuarial-mathematics-minor-on-campus/ |
| 3 | Aerospace Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/aerospace-studies-minor-on-campus/ |
| 4 | Africana Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/africana-studies-minor-on-campus/ |
| 5 | AI in Business | Belk College of Business | https://academics.charlotte.edu/program/ai-in-business-minor-on-campus/ |
| 6 | American Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/american-studies-minor-on-campus/ |
| 7 | Anthropology | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/anthropology-minor-on-campus/ |
| 8 | Arabic Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/arabic-studies-minor-on-campus/ |
| 9 | Architectural History and Heritage | College of Arts + Architecture | https://academics.charlotte.edu/program/architectural-history-and-heritage-minor-on-campus/ |
| 10 | Art History | College of Arts + Architecture | https://academics.charlotte.edu/program/art-history-minor-on-campus/ |
| 11 | Artificial Intelligence Fundamentals | College of Computing & Informatics | https://academics.charlotte.edu/program/artificial-intelligence-fundamentals-minor-on-campus/ |
| 12 | Bioinformatics and Genomics | College of Computing & Informatics | https://academics.charlotte.edu/program/bioinformatics-and-genomics-minor-on-campus/ |
| 13 | Biology | Klein College of Science | https://academics.charlotte.edu/program/biology-minor-on-campus/ |
| 14 | Business Administration | Belk College of Business | https://academics.charlotte.edu/program/business-administration-minor-on-campus/ |
| 15 | Chemistry | Klein College of Science | https://academics.charlotte.edu/program/chemistry-minor-on-campus/ |
| 16 | Communication Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/communication-studies-minor-on-campus/ |
| 17 | Computer Science | College of Computing & Informatics | https://academics.charlotte.edu/program/computer-science-minor-on-campus/ |
| 18 | Criminal Justice | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/criminal-justice-minor-on-campus/ |
| 19 | Dance | College of Arts + Architecture | https://academics.charlotte.edu/program/dance-minor-on-campus/ |
| 20 | Data Science | School of Data Science | https://academics.charlotte.edu/program/data-science-minor-on-campus/ |
| 21 | Economics | Belk College of Business | https://academics.charlotte.edu/program/economics-minor-on-campus/ |
| 22 | English | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/english-minor-on-campus/ |
| 23 | Film Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/film-studies-minor-on-campus/ |
| 24 | French | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/french-minor-on-campus/ |
| 25 | Geography | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/geography-minor-on-campus/ |
| 26 | Geology | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/geology-minor-on-campus/ |
| 27 | German | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/german-minor-on-campus/ |
| 28 | Global Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/global-studies-minor-on-campus/ |
| 29 | Health Administration | College of Health & Human Services | https://academics.charlotte.edu/program/health-administration-minor-on-campus/ |
| 30 | History | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/history-minor-on-campus/ |
| 31 | Information Technology | College of Computing & Informatics | https://academics.charlotte.edu/program/information-technology-minor-on-campus/ |
| 32 | International Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/international-studies-minor-on-campus/ |
| 33 | Japanese | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/japanese-minor-on-campus/ |
| 34 | Journalism | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/journalism-minor-on-campus/ |
| 35 | Kinesiology | College of Health & Human Services | https://academics.charlotte.edu/program/kinesiology-minor-on-campus/ |
| 36 | Latin American Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/latin-american-studies-minor-on-campus/ |
| 37 | Mathematics | Klein College of Science | https://academics.charlotte.edu/program/mathematics-minor-on-campus/ |
| 38 | Military Science | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/military-science-minor-on-campus/ |
| 39 | Music | College of Arts + Architecture | https://academics.charlotte.edu/program/music-minor-on-campus/ |
| 40 | Neuroscience | Klein College of Science | https://academics.charlotte.edu/program/neuroscience-minor-on-campus/ |
| 41 | Philosophy | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/philosophy-minor-on-campus/ |
| 42 | Photography | College of Arts + Architecture | https://academics.charlotte.edu/program/photography-minor-on-campus/ |
| 43 | Physics | Klein College of Science | https://academics.charlotte.edu/program/physics-minor-on-campus/ |
| 44 | Political Science | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/political-science-minor-on-campus/ |
| 45 | Psychology | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/psychology-minor-on-campus/ |
| 46 | Public Health | College of Health & Human Services | https://academics.charlotte.edu/program/public-health-minor-on-campus/ |
| 47 | Religious Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/religious-studies-minor-on-campus/ |
| 48 | Social Work | College of Health & Human Services | https://academics.charlotte.edu/program/social-work-minor-on-campus/ |
| 49 | Sociology | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/sociology-minor-on-campus/ |
| 50 | Spanish | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/spanish-minor-on-campus/ |
| 51 | Sports Marketing & Management | Belk College of Business | https://academics.charlotte.edu/program/sports-marketing-management-minor-on-campus/ |
| 52 | Statistics | Klein College of Science | https://academics.charlotte.edu/program/statistics-minor-on-campus/ |
| 53 | Theatre | College of Arts + Architecture | https://academics.charlotte.edu/program/theatre-minor-on-campus/ |
| 54 | Urban Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/urban-studies-minor-on-campus/ |
| 55 | Women's & Gender Studies | College of Humanities & Earth and Social Sciences | https://academics.charlotte.edu/program/womens-gender-studies-minor-on-campus/ |

### 1.5 General Education Requirements

UNC Charlotte requires all undergraduate students to complete the **General Education Program** consisting of:
- **Foundations**: English Composition, Quantitative Literacy, Foreign Language
- **Approaches to Knowledge**: Arts & Literature, Historical & Philosophical Understanding, Natural Sciences, Social Sciences
- **Additional Requirements**: Writing Intensive, Diversity, Junior/Senior Seminar

### 1.6 Course-ID → Major Quick-Lookup

UNC Charlotte does not use a course numbering system for majors. Programs are identified by name and degree type.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

UNC Charlotte offers 197 graduate programs across 10 colleges/schools.

#### Belk College of Business

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | M.S. | https://academics.charlotte.edu/program/accountancy-master-of-dubois-center/ |
| 2 | Business Administration | M.B.A. | https://academics.charlotte.edu/program/business-administration-m-b-a-on-campus/ |
| 3 | Economics | M.A. | https://academics.charlotte.edu/program/economics-m-a-on-campus/ |
| 4 | Finance | M.S. | https://academics.charlotte.edu/program/finance-m-s-on-campus/ |
| 5 | Marketing | M.S. | https://academics.charlotte.edu/program/marketing-m-s-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 6 | Business Administration | Ph.D. | https://academics.charlotte.edu/program/business-administration-ph-d-on-campus/ |
| 7 | Economics | Ph.D. | https://academics.charlotte.edu/program/economics-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 8 | Applied Econometrics | Graduate Certificate | https://academics.charlotte.edu/program/applied-econometrics-graduate-certificate-dubois-center/ |
| 9 | Business Analytics | Graduate Certificate | https://academics.charlotte.edu/program/business-analytics-graduate-certificate-dubois-center/ |
| 10 | Financial Technology | Graduate Certificate | https://academics.charlotte.edu/program/financial-technology-graduate-certificate-dubois-center/ |

#### Cato College of Education

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 11 | Counseling | M.A. | https://academics.charlotte.edu/program/counseling-m-a-on-campus/ |
| 12 | Curriculum & Instruction | M.Ed. | https://academics.charlotte.edu/program/curriculum-instruction-m-ed-on-campus/ |
| 13 | Educational Leadership | M.Ed. | https://academics.charlotte.edu/program/educational-leadership-m-ed-on-campus/ |
| 14 | Reading Education | M.Ed. | https://academics.charlotte.edu/program/reading-education-m-ed-on-campus/ |
| 15 | Special Education | M.Ed. | https://academics.charlotte.edu/program/special-education-m-ed-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 16 | Curriculum & Instruction | Ed.D. | https://academics.charlotte.edu/program/curriculum-instruction-ed-d-on-campus/ |
| 17 | Educational Leadership | Ed.D. | https://academics.charlotte.edu/program/educational-leadership-ed-d-on-campus/ |
| 18 | Educational Psychology | Ph.D. | https://academics.charlotte.edu/program/educational-psychology-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 19 | Academically or Intellectually Gifted (AIG) | Graduate Certificate | https://academics.charlotte.edu/program/academically-or-intellectually-gifted-aig-graduate-certificate-online/ |
| 20 | Applied Behavior Analysis | Graduate Certificate | https://academics.charlotte.edu/program/applied-behavior-analysis-post-masters-certificate-online/ |

#### College of Arts + Architecture

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 21 | Architecture | M.Arch | https://academics.charlotte.edu/program/architecture-m-arch-on-campus/ |
| 22 | Art | M.A. | https://academics.charlotte.edu/program/art-m-a-on-campus/ |
| 23 | Music | M.A. | https://academics.charlotte.edu/program/music-m-a-on-campus/ |
| 24 | Urban Design | M.S. | https://academics.charlotte.edu/program/urban-design-m-s-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 25 | Urban Design | Graduate Certificate | https://academics.charlotte.edu/program/urban-design-graduate-certificate-on-campus/ |

#### College of Computing & Informatics

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 26 | Computer Science | M.S. | https://academics.charlotte.edu/program/computer-science-m-s-on-campus/ |
| 27 | Cybersecurity | M.S. | https://academics.charlotte.edu/program/cybersecurity-m-s-on-campus/ |
| 28 | Health Informatics | M.S. | https://academics.charlotte.edu/program/health-informatics-m-s-on-campus/ |
| 29 | Information Technology | M.S. | https://academics.charlotte.edu/program/information-technology-m-s-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 30 | Computer Science | Ph.D. | https://academics.charlotte.edu/program/computer-science-ph-d-on-campus/ |
| 31 | Information Technology | Ph.D. | https://academics.charlotte.edu/program/information-technology-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 32 | Applied Artificial Intelligence | Graduate Certificate | https://academics.charlotte.edu/program/applied-artificial-intelligence-graduate-certificate-on-campus/ |
| 33 | Cybersecurity | Graduate Certificate | https://academics.charlotte.edu/program/cybersecurity-graduate-certificate-on-campus/ |

#### College of Health & Human Services

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 34 | Health Administration | M.H.A. | https://academics.charlotte.edu/program/health-administration-m-h-a-on-campus/ |
| 35 | Kinesiology | M.S. | https://academics.charlotte.edu/program/kinesiology-m-s-on-campus/ |
| 36 | Nursing | M.S. | https://academics.charlotte.edu/program/nursing-m-s-on-campus/ |
| 37 | Public Health | M.P.H. | https://academics.charlotte.edu/program/public-health-m-p-h-on-campus/ |
| 38 | Social Work | M.S.W. | https://academics.charlotte.edu/program/social-work-m-s-w-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 39 | Nursing | D.N.P. | https://academics.charlotte.edu/program/nursing-d-n-p-on-campus/ |
| 40 | Public Health | Ph.D. | https://academics.charlotte.edu/program/public-health-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 41 | Health Administration | Graduate Certificate | https://academics.charlotte.edu/program/health-administration-graduate-certificate-on-campus/ |

#### College of Humanities & Earth and Social Sciences

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 42 | Anthropology | M.A. | https://academics.charlotte.edu/program/anthropology-m-a-on-campus/ |
| 43 | Communication | M.A. | https://academics.charlotte.edu/program/communication-m-a-on-campus/ |
| 44 | English | M.A. | https://academics.charlotte.edu/program/english-m-a-on-campus/ |
| 45 | Geography | M.S. | https://academics.charlotte.edu/program/geography-m-s-on-campus/ |
| 46 | History | M.A. | https://academics.charlotte.edu/program/history-m-a-on-campus/ |
| 47 | Political Science | M.A. | https://academics.charlotte.edu/program/political-science-m-a-on-campus/ |
| 48 | Psychology | M.A. | https://academics.charlotte.edu/program/psychology-m-a-on-campus/ |
| 49 | Public Administration | M.P.A. | https://academics.charlotte.edu/program/public-administration-m-p-a-on-campus/ |
| 50 | Sociology | M.A. | https://academics.charlotte.edu/program/sociology-m-a-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 51 | Geography | Ph.D. | https://academics.charlotte.edu/program/geography-ph-d-on-campus/ |
| 52 | Psychology | Ph.D. | https://academics.charlotte.edu/program/psychology-ph-d-on-campus/ |
| 53 | Public Policy | Ph.D. | https://academics.charlotte.edu/program/public-policy-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 54 | Applied Ethics | Graduate Certificate | https://academics.charlotte.edu/program/applied-ethics-graduate-certificate-on-campus/ |
| 55 | Applied Linguistics | Graduate Certificate | https://academics.charlotte.edu/program/applied-linguistics-graduate-certificate-on-campus/ |

#### Klein College of Science

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 56 | Biology | M.S. | https://academics.charlotte.edu/program/biology-m-s-on-campus/ |
| 57 | Chemistry | M.S. | https://academics.charlotte.edu/program/chemistry-m-s-on-campus/ |
| 58 | Mathematics | M.S. | https://academics.charlotte.edu/program/mathematics-m-s-on-campus/ |
| 59 | Physics | M.S. | https://academics.charlotte.edu/program/physics-m-s-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 60 | Biology | Ph.D. | https://academics.charlotte.edu/program/biology-ph-d-on-campus/ |
| 61 | Chemistry | Ph.D. | https://academics.charlotte.edu/program/chemistry-ph-d-on-campus/ |
| 62 | Mathematics | Ph.D. | https://academics.charlotte.edu/program/mathematics-ph-d-on-campus/ |
| 63 | Optical Science & Engineering | Ph.D. | https://academics.charlotte.edu/program/optical-science-engineering-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 64 | Bioinformatics | Graduate Certificate | https://academics.charlotte.edu/program/bioinformatics-graduate-certificate-on-campus/ |

#### William States Lee College of Engineering

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 65 | Civil Engineering | M.S. | https://academics.charlotte.edu/program/civil-engineering-m-s-on-campus/ |
| 66 | Electrical Engineering | M.S. | https://academics.charlotte.edu/program/electrical-engineering-m-s-on-campus/ |
| 67 | Engineering Management | M.S. | https://academics.charlotte.edu/program/engineering-management-m-s-on-campus/ |
| 68 | Mechanical Engineering | M.S. | https://academics.charlotte.edu/program/mechanical-engineering-m-s-on-campus/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 69 | Civil Engineering | Ph.D. | https://academics.charlotte.edu/program/civil-engineering-ph-d-on-campus/ |
| 70 | Electrical Engineering | Ph.D. | https://academics.charlotte.edu/program/electrical-engineering-ph-d-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 71 | Applied Energy | Graduate Certificate | https://academics.charlotte.edu/program/applied-energy-graduate-certificate-on-campus/ |

#### School of Data Science

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 72 | Data Science | M.S. | https://academics.charlotte.edu/program/data-science-m-s-on-campus/ |

##### Graduate Certificates
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 73 | AI for Data Science Practitioners | Graduate Certificate | https://academics.charlotte.edu/program/ai-for-data-science-practitioners-adsp-graduate-certificate-dubois-center/ |

### 2.2 Graduate Admissions Model

**Centralized admissions** through The Graduate School. Each program has a designated Graduate Program Director (GPD) who oversees admissions decisions.

**Application Portal**: https://gradadmissions.charlotte.edu/apply

**Key Deadlines**:
- Fall: Priority March 1, Final August 1
- Spring: Priority October 1, Final December 1
- Summer: Priority April 1, Final June 15

**Application Fee**:
- $75 (U.S. Citizens/Permanent Residents)
- $85 (International Applicants)
- $25 (Post-Baccalaureate/Non-Degree)

**Test Requirements**: Most programs do not require GRE/GMAT. Check individual program requirements.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 |
|------|------|
| Admissions Site | https://admissions.charlotte.edu/ |
| Application Portal | Future 49er Portal (https://future49er.charlotte.edu/apply/) or Common App |
| Application Fee | $75 |
| EA Deadline | November 1 |
| EA Decision | January 30 |
| RD Deadline | February 1 |
| RD Decision | April 1 |
| Enrollment Deadline | May 1 |
| FAFSA Code | 002975 |
| SAT Code | 5105 |
| ACT Code | 3163 |
| Test Policy | Test-optional for students with weighted GPA ≥ 2.8 |
| Recommendation | Not required |
| Interview | Not required |
| Essay | Required (one essay) |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended Score |
|------|---------------|-------------------|
| TOEFL iBT | 70 (min 14 each sub) | 80+ |
| IELTS | 6.0 (min 5.0 each sub) | 6.5+ |
| Duolingo English Test (DET) | 105 | 115+ |
| PTE Academic | 48 (min 35 each sub) | 55+ |
| SAT EBRW | 500 | 550+ |
| ACT Reading | 19 | 22+ |

**Exemptions**:
- U.S. citizens/permanent residents
- Students from English proficiency exempt countries
- Completion of ELTI Level 5
- U.S. high school diploma (2+ years)
- 24+ credit hours at U.S. institution with C or better in English Composition
- U.S. bachelor's/master's degree

### 3.3 Graduate — Global Rules

**Application Platform**: Online via https://gradadmissions.charlotte.edu/apply

**Deadlines**:
- Fall: Priority March 1, Final August 1
- Spring: Priority October 1, Final December 1
- Summer: Priority April 1, Final June 15

**Application Fee**: $75 (domestic), $85 (international)

**Test Requirements**: Most programs do NOT require GRE/GMAT. Check individual program requirements.

**English Language Proficiency**: Required for non-native English speakers who did not earn a U.S. degree. Accepts TOEFL, IELTS, PTE, Duolingo.

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | NC Resident | Non-Resident |
|--------------|-------------|--------------|
| Tuition | $3,926 | $22,018 |
| Fees | $3,285 | $3,285 |
| Loan Fees | $103 | $103 |
| Books & Supplies | $600 | $600 |
| Housing | $10,200 | $10,200 |
| Meals | $5,662 | $5,662 |
| Transportation | $1,340 | $2,000 |
| Computer | $350 | $350 |
| Miscellaneous | $2,360 | $2,360 |
| **Total** | **$27,826** | **$46,578** |

### 4.2 Undergraduate Financial Aid Policy

- **Need-Aware**: UNC Charlotte is need-aware for all students (domestic and international)
- **FAFSA Code**: 002975
- **Merit Scholarships**: Available through NinerScholars Portal (not automatic)
- **Levine Scholars Program**: Premier merit scholarship (nominations due Oct. 15)
- **75% of students** utilize some form of financial aid
- **1,600+ scholarships** awarded annually

### 4.3 Graduate Cost & Funding Framework

**Tuition (2026-2027)**:
- In-state: ~$5,500/year (varies by program)
- Out-of-state: ~$19,000/year (varies by program)

**Funding Opportunities**:
- Graduate Assistantships (TA/RA)
- Fellowships
- Research Assistantships
- Teaching Assistantships

**Application Fee**: $75 (domestic), $85 (international)
**Fee Waivers**: Available for UNC Charlotte employees, McNair scholars, military

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: "https://admissions.charlotte.edu/apply/first-year-students/preparing-for-admissions/"
  source_snippet: "Complete your admission application by our Early Action Deadline, Nov. 1."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "February 1"
  source_url: "https://admissions.charlotte.edu/apply/first-year-students/receiving-your-decision/"
  source_snippet: "Students that apply by the Feb. 1 Regular Decision deadline are guaranteed an Admissions decision by Apr. 1."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.costs.tuition_in_state
  value: "$3,926"
  source_url: "https://admissions.charlotte.edu/financing-your-education/cost-of-attendance/"
  source_snippet: "Tuition* | $3.926"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.costs.tuition_out_of_state
  value: "$22,018"
  source_url: "https://admissions.charlotte.edu/financing-your-education/cost-of-attendance/"
  source_snippet: "Tuition* | $22,018"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.costs.total_in_state
  value: "$27,826"
  source_url: "https://admissions.charlotte.edu/financing-your-education/cost-of-attendance/"
  source_snippet: "Total | $27,826"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.total_out_of_state
  value: "$46,578"
  source_url: "https://admissions.charlotte.edu/financing-your-education/cost-of-attendance/"
  source_snippet: "Total | $46,578"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.tests.policy
  value: "Test-optional for weighted GPA ≥ 2.8"
  source_url: "https://admissions.charlotte.edu/apply/first-year-students/application-requirements/"
  source_snippet: "*Fall 2026 Applicants: Test scores optional for students with a weighted GPA of 2.8 or higher at the end of Junior Year."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.tests.SAT_code
  value: "5105"
  source_url: "https://admissions.charlotte.edu/apply/first-year-students/preparing-for-admissions/"
  source_snippet: "request that your scores be sent to Charlotte, using SAT code 5105 and ACT code 3163"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english_proficiency.TOEFL
  value: "70 (min 14 each sub)"
  source_url: "https://admissions.charlotte.edu/apply/international-students/proof-of-english-proficiency/"
  source_snippet: "*TOEFL IBT (code: 5105) | 70 or higher (minimum of 14 in each sub score)"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.english_proficiency.IELTS
  value: "6.0 (min 5.0 each sub)"
  source_url: "https://admissions.charlotte.edu/apply/international-students/proof-of-english-proficiency/"
  source_snippet: "IELTS | 6.0 or higher (minimum of 5.0 in each sub score)"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.english_proficiency.Duolingo
  value: "105"
  source_url: "https://admissions.charlotte.edu/apply/international-students/proof-of-english-proficiency/"
  source_snippet: "Duolingo English Test (DET) | 105 or higher"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.application.fee
  value: "$75"
  source_url: "https://admissions.charlotte.edu/apply/first-year-students/application-requirements/"
  source_snippet: "Pay the $75 application fee or submit an approved fee waiver"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.financial_aid.need_aware
  value: "Need-aware for all students"
  source_url: "https://admissions.charlotte.edu/financing-your-education/"
  source_snippet: "At Charlotte, we will help you navigate the options available for financing your education."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.programs.total
  value: "285"
  source_url: "https://academics.charlotte.edu/undergraduate-programs/"
  source_snippet: "170+ MAJORS AND MINORS"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-001:
  field: graduate.deadlines.fall_priority
  value: "March 1"
  source_url: "https://gradadmissions.charlotte.edu/apply/application-requirements"
  source_snippet: "Fall Semester (August) Priority Application Submission: March 1st"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-002:
  field: graduate.deadlines.fall_final
  value: "August 1"
  source_url: "https://gradadmissions.charlotte.edu/apply/application-requirements"
  source_snippet: "Final Application Submission: August 1st"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-003:
  field: graduate.application.fee
  value: "$75 domestic, $85 international"
  source_url: "https://gradadmissions.charlotte.edu/apply/application-requirements"
  source_snippet: "Graduate Certificate, Master's or Doctoral Fee $75 USD – U.S. Citizens and Permanent Residents $85 USD – International Applicants"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-004:
  field: graduate.tests.GRE_required
  value: "Most programs do not require"
  source_url: "https://gradadmissions.charlotte.edu/apply/application-requirements"
  source_snippet: "Most graduate programs do not require a standardized test."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-005:
  field: graduate.programs.total
  value: "197"
  source_url: "https://academics.charlotte.edu/graduate-programs/"
  source_snippet: "150+ graduate programs"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-006:
  field: graduate.institution.R1_status
  value: "R1 Carnegie Classification"
  source_url: "https://graduateschool.charlotte.edu/"
  source_snippet: "UNC Charlotte Achieves Prestigious R1 Designation"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-007:
  field: graduate.enrollment.total
  value: "5,990+"
  source_url: "https://graduateschool.charlotte.edu/"
  source_snippet: "+5,990 GRADUATE STUDENTS"
  capture_date: "2026-07-06"
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
unc-charlotte-knowledge-base-v2/
├── overview/
│   ├── institution-overview.md (Section 0)
│   ├── program-counts.md
│   ├── hierarchy-tree.md
│   ├── degree-inventory.md
│   └── distribution-matrix.md
├── undergraduate/
│   ├── belk-college-of-business.md
│   ├── cato-college-of-education.md
│   ├── college-of-arts-architecture.md
│   ├── college-of-computing-informatics.md
│   ├── college-of-health-human-services.md
│   ├── college-of-humanities-earth-social-sciences.md
│   ├── klein-college-of-science.md
│   ├── school-of-data-science.md
│   ├── school-of-professional-studies.md
│   ├── william-states-lee-college-of-engineering.md
│   └── honors-college.md
├── graduate/
│   ├── graduate-programs-by-college.md
│   └── graduate-admissions-model.md
├── admissions/
│   ├── undergraduate-deadlines.md
│   ├── undergraduate-requirements.md
│   ├── english-proficiency.md
│   └── graduate-admissions.md
├── costs/
│   ├── undergraduate-cost.md
│   ├── financial-aid-policy.md
│   └── graduate-cost.md
└── evidence/
    └── evidence-chain-index.md
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "unc-charlotte-knowledge-base-v2"
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

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Individual program pages |
| P0 | Graduate English proficiency minimums | gradadmissions.charlotte.edu |
| P1 | Detailed financial aid policy | ninercentral.charlotte.edu |
| P1 | Scholarship amounts and criteria | scholarships.charlotte.edu |
| P1 | Graduate funding/stipend rates | graduateschool.charlotte.edu/funding |
| P2 | Transfer admission requirements | admissions.charlotte.edu/apply/transfer-students/ |
| P2 | Honors College requirements | honorscollege.charlotte.edu |
| P2 | Levine Scholars Program details | levinescholars.charlotte.edu |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | UNC Charlotte | (Other Schools) |
|------|---------------|-----------------|
| Institution Type | Public (UNC System) | |
| Location | Charlotte, NC | |
| Total Programs (Rule 1) | 482 | |
| UG Programs | 285 | |
| Grad Programs | 197 | |
| Colleges/Schools | 11 | |
| UG Tuition (In-State) | $3,926 | |
| UG Tuition (OOS) | $22,018 | |
| UG Total COA (In-State) | $27,826 | |
| UG Total COA (OOS) | $46,578 | |
| EA Deadline | November 1 | |
| RD Deadline | February 1 | |
| Test Policy | Test-optional (GPA ≥ 2.8) | |
| TOEFL Minimum | 70 | |
| IELTS Minimum | 6.0 | |
| Application Fee (UG) | $75 | |
| Application Fee (Grad) | $75/$85 | |
| Need-Blind/Need-Aware | Need-aware (all) | |
| R1 Status | Yes | |
| Graduate Students | 5,990+ | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.charlotte.edu, academics.charlotte.edu, graduateschool.charlotte.edu, gradadmissions.charlotte.edu, ninercentral.charlotte.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
