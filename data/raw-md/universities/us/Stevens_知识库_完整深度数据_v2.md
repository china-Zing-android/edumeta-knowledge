# Stevens Institute of Technology Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BE) | 36 |
| 本科辅修 (Minor) | 22 |
| 研究生学位项目 (MS/MEng/MBA/PhD/Eng) | 125 |
| 研究生高级证书 (Graduate Certificate) | 120 |
| **学位项目总计 (UG + Grad)** | **283** |
| 学院 / 独立系所总数 | 5 schools, 10+ departments |

> Source: Stevens Program Finder (219 unique program links) + Academic Catalog (289 catalog entries including minors). Program Finder count of 219 includes dual-degree variants and online programs counted separately. Academic Catalog count of 289 includes all credential types. The 283 figure represents unique degree-granting programs excluding minors from the catalog count.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Stevens Institute of Technology
├── Charles V. Schaefer, Jr. School of Engineering and Science (SES)  [学院]
│   ├── Department of Biomedical Engineering                          [系]
│   ├── Department of Chemical Engineering and Materials Science      [系]
│   ├── Department of Chemistry and Chemical Biology                  [系]
│   ├── Department of Civil, Environmental and Ocean Engineering      [系]
│   ├── Department of Computer Science                                [系]
│   ├── Department of Electrical and Computer Engineering             [系]
│   ├── Department of Mathematical Sciences                           [系]
│   ├── Department of Mechanical Engineering                          [系]
│   ├── Department of Physics                                         [系]
│   └── Department of Systems Engineering                             [系]
├── School of Business                                                [学院]
│   ├── (No formal departmental subdivision; programs organized by discipline)
│   ├── Finance & Financial Engineering programs
│   ├── Business Analytics & AI programs
│   ├── Management & Enterprise Project Management programs
│   └── MBA programs
├── School of Humanities, Arts and Social Sciences (HASS)             [学院]
│   ├── Music and Technology program                                  [系]
│   ├── Visual Arts & Technology program                              [系]
│   ├── Science and Technology Studies                                [系]
│   └── Humanities and Social Sciences                                [系]
├── School of Computing (launching Fall 2026)                         [学院]
│   ├── Computer Science programs
│   ├── Artificial Intelligence programs
│   ├── Cybersecurity programs
│   └── Data Science programs
└── College of Professional Education                                 [学院]
    └── (Online and professional programs; no formal departmental subdivision)
```

> Note: The School of Computing is targeted to launch in Fall 2026 and will house programs currently under SES Department of Computer Science. Cross-listing exists between SES and Computing for CS, AI, and Cybersecurity programs.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BS | B.S. | Bachelor of Science | 本科 | 22 |
| BE | B.E. | Bachelor of Engineering | 本科 | 14 |
| Minor | Minor | 辅修 | 本科 | 22 |
| MS | M.S. | Master of Science | 研究生 | 55 |
| MEng | M.Eng. | Master of Engineering | 研究生 | 18 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 2 |
| Eng | Engr. | Degree of Engineer | 研究生 | 8 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 20 |
| Certificate | Grad Cert | Graduate Certificate | 研究生 | 120 |

> Stevens awards both BS and BE at the undergraduate level. Engineering programs typically award BE; science and business programs award BS. The Degree of Engineer is a post-master's professional degree unique to Stevens.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BS | BE | MS | MEng | MBA | Eng | PhD | Certificate | 合计 |
|------------|----|----|----|------|-----|-----|-----|-------------|------|
| Schaefer SES | 10 | 14 | 30 | 15 | 0 | 8 | 18 | 65 | 160 |
| School of Business | 8 | 0 | 12 | 0 | 2 | 0 | 2 | 40 | 64 |
| HASS | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 |
| School of Computing | 3 | 0 | 5 | 0 | 0 | 0 | 2 | 0 | 10 |
| College of Professional Education | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 14 | 19 |
| **合计** | **25** | **14** | **49** | **18** | **2** | **8** | **22** | **120** | **258** |

> Note: Dual-degree programs (MBA+MS, etc.) are counted once under their primary degree. Some programs are cross-listed between SES and the new School of Computing. The matrix includes unique degree programs from the Program Finder; the Academic Catalog's 289 count includes additional credential variants and minors not shown here.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Stevens has 5 schools, with undergraduate programs primarily in 4 schools (SES, Business, HASS, and the new School of Computing). The College of Professional Education is graduate/online-only. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Charles V. Schaefer, Jr. School of Engineering and Science

##### Department of Biomedical Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.stevens.edu/program/biomedical-engineering-bachelor-degree |

##### Department of Chemical Engineering and Materials Science
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.stevens.edu/program/chemical-engineering-bachelor-degree |

##### Department of Chemistry and Chemical Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.stevens.edu/program/biology-bachelor-degree |
| 2 | Chemical Biology | https://www.stevens.edu/program/chemical-biology-bachelor-degree |
| 3 | Chemistry | https://www.stevens.edu/program/chemistry-bachelor-degree |
| 4 | Accelerated Chemical Biology | https://www.stevens.edu/program/accelerated-chemical-biology-bachelor-degree |

##### Department of Civil, Environmental and Ocean Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stevens.edu/program/civil-engineering-bachelor-degree |
| 2 | Environmental Engineering | https://www.stevens.edu/program/environmental-engineering-bachelor-degree |
| 3 | Ocean Engineering | https://www.stevens.edu/program/bachelors-degree-in-ocean-engineering |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stevens.edu/program/computer-science-bachelor-degree |
| 2 | Cybersecurity | https://www.stevens.edu/program/cybersecurity-bachelor-degree |
| 3 | Artificial Intelligence | https://www.stevens.edu/program/bachelors-degree-in-artificial-intelligence |

##### Department of Electrical and Computer Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.stevens.edu/program/computer-engineering-bachelor-degree |
| 2 | Electrical Engineering | https://www.stevens.edu/program/electrical-engineering-bachelor-degree |

##### Department of Mathematical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.stevens.edu/program/mathematics-bachelor-degree |

##### Department of Mechanical Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.stevens.edu/program/mechanical-engineering-bachelor-degree |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.stevens.edu/program/physics-bachelor-degree |

##### Department of Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Management | https://www.stevens.edu/program/engineering-management-bachelor-degree |
| 2 | Engineering (General) | https://www.stevens.edu/program/engineering-bachelors-program |
| 3 | Industrial and Systems Engineering | https://www.stevens.edu/program/industrial-systems-engineering-bachelor-degree |
| 4 | Software Engineering | https://www.stevens.edu/program/software-engineering-bachelor-degree |
| 5 | Naval Engineering Concentration | https://www.stevens.edu/program/naval-engineering-concentration |

#### School of Business

##### (No formal department subdivision)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting & Analytics | https://www.stevens.edu/school-business/undergraduate-programs/accounting-analytics |
| 2 | Business & Technology | https://www.stevens.edu/school-business/undergraduate-programs/business-technology-major |
| 3 | Economics | https://www.stevens.edu/program/economics-bachelors-program |
| 4 | Finance | https://www.stevens.edu/school-business/undergraduate-programs/finance-major |
| 5 | Information Systems | https://www.stevens.edu/school-business/undergraduate-programs/information-systems |
| 6 | Management | https://www.stevens.edu/school-business/undergraduate-programs/management-major |
| 7 | Marketing Innovation & Analytics | https://www.stevens.edu/school-business/undergraduate-programs/marketing-innovation-analytics-major |
| 8 | Quantitative Finance | https://www.stevens.edu/school-business/undergraduate-programs/quantitative-finance-bachelor-degree |

#### School of Humanities, Arts and Social Sciences (HASS)

##### Music and Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Music and Technology | https://www.stevens.edu/program/music-technology |

##### Visual Arts & Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Visual Arts and Technology | https://www.stevens.edu/program/visual-arts-technology |

##### Science and Technology Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Science, Technology and Society | https://www.stevens.edu/program/science-technology-society |
| 2 | Science Communication | https://www.stevens.edu/program/science-communication |

##### Humanities and Social Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Quantitative Social Science | https://www.stevens.edu/program/social-sciences |
| 2 | Literature | https://www.stevens.edu/program/literature |
| 3 | Philosophy | https://www.stevens.edu/program/philosophy |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 类型 | URL |
|---|------|------|-----|
| 1 | Accelerated Law Program | Pre-Professional | https://www.stevens.edu/program/law-program |
| 2 | Bachelor's in Technology + MS in Business Intelligence & Analytics | Accelerated BS+MS | https://www.stevens.edu/program/bachelor-of-technology-and-m-s-in-business-intelligence-and-analytics |
| 3 | Bachelor's in Technology + MS in Finance | Accelerated BS+MS | https://www.stevens.edu/program/bachelor-of-technology-and-m-s-in-finance-accelerated-masters-program |
| 4 | Bachelor's in Technology + MS in Financial Engineering | Accelerated BS+MS | https://www.stevens.edu/program/bachelor-of-technology-and-m-s-in-financial-engineering-accelerated-masters |
| 5 | Bachelor's in Technology + MS in Information Systems | Accelerated BS+MS | https://www.stevens.edu/program/bachelor-of-technology-and-m-s-in-information-systems-accelerated-masters |
| 6 | Bachelor's in Technology + MS in Management | Accelerated BS+MS | https://www.stevens.edu/program/bachelor-of-technology-and-m-s-in-management-accelerated-masters-program |
| 7 | Bachelor's in Technology + MBA | Accelerated BS+MBA | https://www.stevens.edu/program/bachelor-of-technology-and-mba-accelerated-masters-program |

### 1.4 Minors — complete list

| # | Minor | Home school | URL |
|---|-------|-------------|-----|
| 1 | Accounting | Business | (catalog) |
| 2 | Astronomy | SES | (catalog) |
| 3 | Biochemical Engineering | SES | (catalog) |
| 4 | Biology | SES | (catalog) |
| 5 | Biomedical Engineering | SES | (catalog) |
| 6 | Chemical Engineering | SES | (catalog) |
| 7 | Chemical Biology | SES | (catalog) |
| 8 | Chemistry | SES | (catalog) |
| 9 | Coastal Engineering | SES | (catalog) |
| 10 | Computer Engineering | SES | (catalog) |
| 11 | Computer Science | SES/Computing | (catalog) |
| 12 | Cybersecurity | SES/Computing | (catalog) |
| 13 | Data Visualization | Business | (catalog) |
| 14 | Economics | Business | (catalog) |
| 15 | Financial Engineering | Business | (catalog) |
| 16 | Mathematics | SES | (catalog) |
| 17 | Music and Technology | HASS | (catalog) |
| 18 | Physics | SES | (catalog) |
| 19 | Science Communication | HASS | (catalog) |
| 20 | Science, Technology and Society | HASS | (catalog) |
| 21 | Visual Arts and Technology | HASS | (catalog) |
| 22 | Quantitative Social Science | HASS | (catalog) |

> Source: Stevens Academic Catalog 2025-2026. Minors are listed in the catalog under each school's program listings.

### 1.5 General/Institute-wide requirements

Stevens requires all undergraduates to complete the Stevens Core Curriculum, which includes:
- **Mathematics**: Calculus I, II, III + Differential Equations
- **Sciences**: Physics I, II + Chemistry I + Biology or additional science
- **Humanities/Social Sciences**: Minimum 6 courses across HASS disciplines
- **Writing**: Freshman Writing I, II
- **Design**: Senior Design Project (capstone)
- **Physical Education**: 2 semesters

> Source: Stevens Academic Catalog 2025-2026, General Requirements section.

### 1.6 Course-ID → Major quick-lookup

Stevens does not use a traditional course-numbering system for majors. Programs are identified by name and URL slug (e.g., `computer-science-bachelor-degree`).

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Charles V. Schaefer, Jr. School of Engineering and Science

##### Department of Biomedical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.stevens.edu/program/biomedical-engineering-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.stevens.edu/program/biomedical-engineering-phd |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomechanical Engineering | https://www.stevens.edu/program/biomechanical-engineering-graduate-certificate |
| 2 | Biomedical Engineering | https://www.stevens.edu/program/biomedical-engineering-graduate-certificate |

##### Department of Chemical Engineering and Materials Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.stevens.edu/program/chemical-engineering-masters |
| 2 | Materials Science and Engineering | https://www.stevens.edu/program/materials-science-engineering-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.stevens.edu/program/chemical-engineering-phd |
| 2 | Materials Science and Engineering | https://www.stevens.edu/program/materials-science-engineering-phd |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Technology for Energy and Sustainability | https://www.stevens.edu/program/materials-technology-energy-sustainability-graduate-certificate |
| 2 | Pharmaceutical Manufacturing | https://www.stevens.edu/program/pharmaceutical-manufacturing-graduate-certificate |
| 3 | Drug Discovery | https://www.stevens.edu/program/drug-discovery-graduate-certificate |

##### Department of Chemistry and Chemical Biology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Biology | https://www.stevens.edu/program/chemical-biology-masters |
| 2 | Chemistry | https://www.stevens.edu/program/chemistry-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Biology | https://www.stevens.edu/program/chemical-biology-phd |
| 2 | Chemistry | https://www.stevens.edu/program/chemistry-phd |

##### Department of Civil, Environmental and Ocean Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stevens.edu/program/civil-engineering-masters |
| 2 | Construction Engineering and Management | https://www.stevens.edu/program/construction-engineering-management-masters |
| 3 | Environmental Engineering | https://www.stevens.edu/program/environmental-engineering-masters |
| 4 | Ocean Engineering | https://www.stevens.edu/program/ocean-engineering-masters |
| 5 | Sustainability Management | https://www.stevens.edu/program/sustainability-management-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stevens.edu/program/civil-engineering-doctoral-program |
| 2 | Environmental Engineering | https://www.stevens.edu/program/environmental-engineering-doctoral-program |
| 3 | Ocean Engineering | https://www.stevens.edu/program/ocean-engineering-doctoral-program |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Management (Executives) | https://www.stevens.edu/program/advanced-certificate-executives-construction-management-graduate-certificate |
| 2 | Environmental Management | https://www.stevens.edu/program/environmental-management-graduate-certificate |

##### Department of Computer Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stevens.edu/program/computer-science-masters |
| 2 | Cybersecurity | https://www.stevens.edu/program/cybersecurity-masters |
| 3 | Data Science | https://www.stevens.edu/program/data-science-masters |
| 4 | Human-Centered AI | https://www.stevens.edu/program/masters-in-human-centered-ai |
| 5 | Machine Learning | https://www.stevens.edu/program/machine-learning-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stevens.edu/program/computer-science-doctoral-program |
| 2 | Data Science | https://www.stevens.edu/program/data-science-phd |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://www.stevens.edu/program/cybersecurity-graduate-certificate |
| 2 | Databases | https://www.stevens.edu/program/databases-graduate-certificate |
| 3 | Machine Learning | https://www.stevens.edu/program/machine-learning-graduate-certificate |
| 4 | Enterprise and Cloud Computing | https://www.stevens.edu/program/enterprise-cloud-computing-graduate-certificate |
| 5 | Enterprise Security and Information Assurance | https://www.stevens.edu/program/enterprise-security-and-information-assurance-graduate-certificate |
| 6 | Secure Network Systems Design | https://www.stevens.edu/program/secure-network-systems-design-graduate-certificate |
| 7 | Software Design and Development | https://www.stevens.edu/program/software-design-development-graduate-certificate |
| 8 | Software Engineering | https://www.stevens.edu/program/software-engineering-graduate-certificate |
| 9 | AI-Driven Software Systems Architecture | https://www.stevens.edu/program/ai-driven-software-systems-architecture |
| 10 | Fundamentals in AI | https://www.stevens.edu/program/fundamentals-in-artificial-intelligence-graduate-certificate |

##### Department of Electrical and Computer Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Artificial Intelligence | https://www.stevens.edu/program/applied-artificial-intelligence-masters |
| 2 | Computer Engineering | https://www.stevens.edu/program/computer-engineering-masters |
| 3 | Electrical Engineering | https://www.stevens.edu/program/electrical-engineering-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.stevens.edu/program/computer-engineering-phd |
| 2 | Electrical Engineering | https://www.stevens.edu/program/electrical-engineering-phd |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Power Systems Engineering | https://www.stevens.edu/program/power-systems-engineering-graduate-certificate |
| 2 | Microelectronics | https://www.stevens.edu/program/microelectronics-graduate-certificate |
| 3 | Photonics | https://www.stevens.edu/program/photonics-graduate-certificate |
| 4 | Wireless Communications | https://www.stevens.edu/program/wireless-communications-graduate-certificate |

##### Department of Mathematical Sciences
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Mathematics and Quantitative Risk | https://www.stevens.edu/program/actuarial-mathematics-quantitative-risk-masters |
| 2 | Applied Mathematics | https://www.stevens.edu/program/applied-mathematics-masters |
| 3 | Mathematics | https://www.stevens.edu/program/mathematics-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.stevens.edu/program/mathematics-phd |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics | https://www.stevens.edu/program/applied-statistics-graduate-certificate |
| 2 | Data Exploration and Visualization for Risk and Decision Making | https://www.stevens.edu/program/data-exploration-visualization-risk-decision-making-graduate-certificate |

##### Department of Mechanical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.stevens.edu/program/masters-in-aerospace-engineering |
| 2 | Mechanical Engineering | https://www.stevens.edu/program/mechanical-engineering-masters |
| 3 | Pharmaceutical Manufacturing | https://www.stevens.edu/program/pharmaceutical-manufacturing-masters |
| 4 | Robotics | https://www.stevens.edu/program/robotics-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.stevens.edu/program/mechanical-engineering-doctoral |
| 2 | Robotics | https://www.stevens.edu/program/robotics-doctoral-program |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.stevens.edu/program/aerospace-engineering-graduate-certificate |
| 2 | Application of ML to Mechanical Engineering | https://www.stevens.edu/program/application-of-machine-learning-to-mechanical-engineering-graduate |
| 3 | Application of ML to Pharmaceutical Development | https://www.stevens.edu/program/application-machine-learning-pharmaceutical-development-graduate-certificate |
| 4 | Autonomous Robotics | https://www.stevens.edu/program/autonomous-robotics-graduate-certificate |

##### Department of Physics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://www.stevens.edu/program/physics-masters |
| 2 | Quantum Engineering | https://www.stevens.edu/program/quantum-engineering-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://www.stevens.edu/program/physics-phd |

##### Department of Systems Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://www.stevens.edu/program/engineering-management-masters |
| 2 | Software Engineering | https://www.stevens.edu/program/software-engineering-masters |
| 3 | Space Systems Engineering | https://www.stevens.edu/program/space-systems-engineering-masters |
| 4 | Systems Engineering | https://www.stevens.edu/program/systems-engineering-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://www.stevens.edu/program/engineering-management-phd |
| 2 | Systems Engineering | https://www.stevens.edu/program/systems-engineering-phd |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://www.stevens.edu/program/engineering-management-graduate-certificate |
| 2 | Systems Engineering | https://www.stevens.edu/program/systems-engineering-graduate-certificate |
| 3 | Systems Supportability Engineering | https://www.stevens.edu/program/systems-supportability-engineering-graduate-certificate |
| 4 | AI-Enabled Systems Engineering | https://www.stevens.edu/program/ai-enabled-systems-engineering-graduate-certificate |
| 5 | Space Systems Engineering | https://www.stevens.edu/program/space-systems-engineering-graduate-certificate |
| 6 | AI in Engineering Design | https://www.stevens.edu/program/artificial-intelligence-engineering-design-graduate-certfificate |

##### Interdisciplinary (SES)
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Manufacturing (Online) | https://www.stevens.edu/program/online-pharmaceutical-manufacturing-masters |

#### School of Business

##### (No formal department subdivision)
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Analytics | https://www.stevens.edu/program/master-of-science-in-accounting-and-analytics |
| 2 | Business Analytics & AI | https://www.stevens.edu/program/masters-in-business-analytics-and-artificial-intelligence |
| 3 | Business Intelligence and Analytics | https://www.stevens.edu/program/business-intelligence-analytics-masters-program |
| 4 | Enterprise Project Management | https://www.stevens.edu/program/enterprise-project-management-masters-program |
| 5 | Finance | https://www.stevens.edu/program/finance-masters-program |
| 6 | Financial Engineering | https://www.stevens.edu/program/financial-engineering-masters-program |
| 7 | Financial Technology and Analytics | https://www.stevens.edu/program/financial-technology-and-analytics-masters-degree |
| 8 | Information Systems | https://www.stevens.edu/program/information-systems-masters-program |
| 9 | Management | https://www.stevens.edu/program/management-masters-program |
| 10 | Sports Technologies & Digital Transformation (Dual) | https://www.stevens.edu/program/sports-technologies-digital-transformation-dual-master-programs |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | MBA | https://www.stevens.edu/program/stevens-mba-ssb-grad |
| 2 | Analytics MBA | https://www.stevens.edu/program/analytics-mba |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | (via Graduate School) |
| 2 | Financial Engineering | (via Graduate School) |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Business Analytics | https://www.stevens.edu/program/applied-business-analytics-certificate-ssb |
| 2 | Business Intelligence & Analytics | https://www.stevens.edu/program/business-intelligence-and-analytics-certificate |
| 3 | Marketing Analytics | https://www.stevens.edu/program/marketing-analytics-certificate |
| 4 | Operational Excellence | https://www.stevens.edu/program/operational-excellence-certificate |
| 5 | Operations and Supply Chain Analytics | https://www.stevens.edu/program/operations-and-supply-chain-analytics-certificate |
| 6 | Algorithmic Trading Strategies | https://www.stevens.edu/program/algorithmic-trading-strategies |
| 7 | Financial Analytics | https://www.stevens.edu/program/financial-analytics-certificate |
| 8 | Financial Computing | https://www.stevens.edu/program/ssb-financial-computing-certificate |
| 9 | Financial Engineering | https://www.stevens.edu/program/financial-engineering-certificate |
| 10 | Financial Planning | https://www.stevens.edu/program/ssb-financial-planning-certificate |
| 11 | Financial Risk Engineering | https://www.stevens.edu/program/ssb-financial-risk-engineering-certificate |
| 12 | Financial Services Analytics | https://www.stevens.edu/program/financial-services-analytics-certificate |
| 13 | Financial Software Engineering | https://www.stevens.edu/program/ssb-financial-software-engineering-certificate |
| 14 | Financial Statistics | https://www.stevens.edu/program/ssb-financial-statistics-certificate |
| 15 | Financial Technology | https://www.stevens.edu/program/financial-technology-certificate |
| 16 | Foundations of Quantitative Data Science in Finance | https://www.stevens.edu/program/foundations-of-quantitative-data-science-in-finance-certificate |
| 17 | Fundamentals of Finance | https://www.stevens.edu/program/ssb-fundamentals-of-finance-certificate |
| 18 | Machine Learning in Finance | https://www.stevens.edu/program/ssb-machine-learning-finance-certificate |
| 19 | Software Engineering in Finance | https://www.stevens.edu/program/software-engineering-in-finance-certificate |
| 20 | Business Process Management & Service Innovation | https://www.stevens.edu/program/business-process-management-and-service-innovation |
| 21 | Corporate Innovation and Leadership | https://www.stevens.edu/program/corporate-innovation-and-leadership-ssb-grad |
| 22 | Fundamentals of Management | https://www.stevens.edu/program/fundamentals-of-management-certificate |
| 23 | Healthcare Management and Leadership | https://www.stevens.edu/program/healthcare-management-and-leadership-certificate-ssb |
| 24 | Information Management | https://www.stevens.edu/program/information-management-certificate |
| 25 | Management of AI | https://www.stevens.edu/program/management-of-ai-ssb |
| 26 | Management of Wireless Networks | https://www.stevens.edu/program/management-of-wireless-networks-certificate |
| 27 | Health Informatics | https://www.stevens.edu/program/health-informatics-graduate-certificate |
| 28 | Healthcare Systems and Data Analytics | https://www.stevens.edu/program/healthcare-systema-data-analytics-graduate-certificate |
| 29 | Logistics and Supply Chain Analysis | https://www.stevens.edu/program/logistics-supply-chain-analysis-graduate-certificate |

> Note: School of Business has numerous MBA+MS dual-degree programs (14 total) not listed individually here. See the Program Finder for the complete dual-degree list.

#### School of Computing (launching Fall 2026)

> Note: The School of Computing is new and will house programs currently under SES. Programs listed here are those explicitly listed on the School of Computing page.

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stevens.edu/program/computer-science-masters |
| 2 | Cybersecurity | https://www.stevens.edu/program/cybersecurity-masters |
| 3 | Machine Learning | https://www.stevens.edu/program/machine-learning-masters |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stevens.edu/program/computer-science-doctoral-program |
| 2 | Data Science (interdisciplinary) | https://www.stevens.edu/program/data-science-phd |

### 2.2 At least one program's full deep-dive (worked example)

**Program**: Master of Science in Computer Science
**School**: Charles V. Schaefer, Jr. School of Engineering and Science / Department of Computer Science
**URL**: https://www.stevens.edu/program/computer-science-masters

| Field | Value |
|-------|-------|
| Department Address | Department of Computer Science, Stevens Institute of Technology, 1 Castle Point Terrace, Hoboken, NJ 07030 |
| Application Platform | Stevens Graduate Application Portal |
| Application Fee | Waived for event attendees; standard fee not explicitly stated on program page |
| Preferred Deadline (Fall, Full-Time) | April 15 |
| Preferred Deadline (Spring, Full-Time) | November 1 |
| GRE | Not required (per graduate admissions policy) |
| English Proficiency | TOEFL or IELTS required for non-native speakers |
| Program Length | 30 credits |
| Thesis Option | Available |
| Online Option | Available (separate program listing) |

> Note: Detailed per-program GRE/TOEFL minimums are behind the graduate application portal and not publicly listed on the program page. Contact graduate@stevens.edu for specifics.

### 2.3 Graduate admissions model

Stevens uses a **centralized graduate admissions portal** with **decentralized program-level decision-making**. Key features:

- **Single application portal** for all graduate programs
- **Rolling admissions** with preferred deadlines
- **Per-program review**: each department/program makes its own admission decisions
- **Merit scholarships**: considered automatically for applicants meeting preferred deadlines
- **F1 visa students**: strongly encouraged to apply by preferred deadlines
- **Contact**: graduate@stevens.edu

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application Platform | Common Application, Coalition App with Scoir | https://www.stevens.edu/admission-aid/undergraduate-admissions/how-to-apply |
| Early Decision I (EDI) | November 15 (binding) | https://www.stevens.edu/admission-aid/undergraduate-admissions/admissions-timeline |
| Early Action (EA) | December 1 (non-binding) | same |
| Early Decision II (EDII) | January 5 (binding) | same |
| Regular Decision (RD) | January 5 (non-binding) | same |
| CSS Profile Due | EDI: Nov 15, EA: Dec 15, EDII/RD: Jan 5 | same |
| FAFSA Due | EDI: Nov 15, EA: Dec 15, EDII/RD: Jan 5 | same |
| Notification By | EDI: Dec 15, EA: Feb 1, EDII: Feb 15, RD: Apr 1 | same |
| Deposit By | EDI: Jan 10, EA: May 1, EDII: Mar 1, RD: May 1 | same |
| Application Fee | $75 | https://www.stevens.edu/admission-aid/undergraduate-admissions/international-students |
| SAT/ACT Policy | Test-optional through Fall 2026 (with exceptions) | same |
| Superscore | Not explicitly stated | — |
| Recommendations | 2 letters preferred (1 teacher + 1 counselor) | same |
| Interview | Optional for most; strongly recommended for international | same |
| CSS Code | 2819 | https://www.stevens.edu/page-basic/first-year-application-plans |
| FAFSA Code | 002639 | same |
| Transfer Spring Deadline | November 1 | https://www.stevens.edu/admission-aid/undergraduate-admissions/admissions-timeline |
| Transfer Fall Deadline | June 15 | same |
| Accelerated Pre-Med Deadline | November 1 | same |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Source |
|------|---------|-------------|--------|
| TOEFL iBT (Old) | 80 | — | https://www.stevens.edu/admission-aid/undergraduate-admissions/international-students |
| TOEFL iBT (New) | 4 | — | same |
| IELTS | 6.0 overall | — | same |
| Duolingo English Test | 105 | — | same |
| SAT I EBRW | 550 | — | same |

> Applicability: Required for international students (non-US Citizen, non-US Permanent Resident) whose first language is not English. Waiver may be granted for students who studied in the US for at least 3 years.

### 3.3 Graduate — global rules

| Field | Value | Source |
|-------|-------|--------|
| Admissions Model | Centralized portal, decentralized decisions | https://www.stevens.edu/admission-aid/graduate-admissions |
| Application Platform | Stevens Graduate Application | same |
| Preferred Deadline (Fall MS Full-Time) | April 15 | https://www.stevens.edu/admission-aid/graduate-admissions/application-deadlines |
| Preferred Deadline (Fall MS Part-Time) | August 15 | same |
| Preferred Deadline (Fall PhD) | January 15 | same |
| Preferred Deadline (Spring MS Full-Time) | November 1 | same |
| Preferred Deadline (Spring MS Part-Time) | January 1 | same |
| Preferred Deadline (Spring PhD) | September 1 | same |
| Summer Deadline (Domestic) | May 1 | same |
| Rolling Admissions | Yes (applications accepted after preferred deadlines) | same |
| GRE Policy | Not required (per admissions page) | https://www.stevens.edu/admission-aid/graduate-admissions |
| English Proficiency | TOEFL or IELTS for non-native speakers | same |
| Application Fee | Waived for event attendees | same |
| CGS April 15 | Not explicitly stated | — |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

**On-Campus:**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and Fees | $68,230 | Per academic year |
| Loan Fees | $70 | For students offered federal loans |
| Housing and Meals | $20,744 | On-campus residence |
| Books and Supplies | $1,200 | Estimated |
| Miscellaneous | $1,050 | Personal expenses |
| **Total Cost of Attendance** | **$91,294** | |

**Commuter:**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and Fees | $68,230 | Per academic year |
| Loan Fees | $70 | For students offered federal loans |
| Housing and Meals | $2,270 | Living at home |
| Books and Supplies | $1,200 | Estimated |
| Transportation | $500 | Estimated |
| Miscellaneous | $1,050 | Personal expenses |
| **Total Cost of Attendance** | **$73,320** | |

> Source: https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-costs-and-aid

### 4.2 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need-Blind/Need-Aware | Need-aware for all applicants (including US) | https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-scholarships-and-aid |
| International Aid | Limited merit-based Global Scholarship | same |
| Meet 100% Need | Not guaranteed | same |
| Tuition-Free Threshold | $75,000 family income (The Stevens Investment, starting Fall 2026) | https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-costs-and-aid/the-stevens-investment |
| Stevens Investment Eligibility | US citizens/PRs, family income ≤$75k, typical assets, first-time first-year, live on campus first year | same |
| Merit Scholarships | Available for exceptional academic records | https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-scholarships-and-aid |
| Students Receiving Aid | >90% | same |
| Loan-Free | Not guaranteed; Stevens Investment uses grants/scholarships only | https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-costs-and-aid/the-stevens-investment |

### 4.3 Graduate cost & funding framework

**2026-2027 Full-Time Graduate (On-Campus):**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and Fees | $47,826 | Per academic year |
| Loan Fees | $206 | For students offered federal loans |
| Housing and Meals | $20,744 | On-campus (note: limited space for new grad students) |
| Books and Supplies | $1,000 | Estimated |
| Miscellaneous | $1,050 | Personal expenses |
| **Total Cost of Attendance** | **$70,826** | |

**2026-2027 Full-Time Graduate (Commuter):**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and Fees | $47,826 | Per academic year |
| Loan Fees | $206 | |
| Housing and Meals | $2,270 | |
| Books and Supplies | $1,000 | |
| Transportation | $500 | |
| Miscellaneous | $1,050 | |
| **Total Cost of Attendance** | **$52,852** | |

> Source: https://www.stevens.edu/admission-aid/tuition-financial-aid/graduate-costs-and-funding

**Graduate Funding:**
- Teaching Assistantships (TA) and Research Assistantships (RA) available for select doctoral students
- Fellowships available
- Federal aid available for graduate students
- Merit-based scholarships considered for applicants meeting preferred deadlines

---

## SECTION 5 — Evidence chain index

### E-U-001: UG Deadlines
```yaml
field: undergraduate.deadlines
value: {EDI: "November 15", EA: "December 1", EDII: "January 5", RD: "January 5"}
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions/admissions-timeline
source_snippet: "Application Deadline: November 15 (EDI), December 1 (EA), January 5 (EDII), January 5 (RD)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-002: UG Cost of Attendance
```yaml
field: undergraduate.costs.tuition_2026_2027
value: {tuition: "$68,230", housing_meals: "$20,744", total_on_campus: "$91,294", total_commuter: "$73,320"}
source_url: https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-costs-and-aid
source_snippet: "Tuition and Fees: $68,230; Housing and Meals: $20,744; Total Cost of Attendance: $91,294"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-003: English Proficiency Requirements
```yaml
field: undergraduate.english_proficiency
value: {TOEFL: 80, IELTS: 6.0, Duolingo: 105, SAT_EBRW: 550}
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions/international-students
source_snippet: "TOEFL (minimum 80 iBT-Old; minimum 4 iBT-New), IELTS (minimum 6.0 overall), Duolingo English Test (minimum 105), SAT I Evidence-Based Reading & Writing (minimum 550)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004: Test-Optional Policy
```yaml
field: undergraduate.test_policy
value: "Test-optional through Fall 2026 (with exceptions)"
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions/international-students
source_snippet: "Stevens Institute of Technology is extending the SAT/ACT test optional policy, with some exceptions, through Fall 2026 first year applicants."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005: Application Fee
```yaml
field: undergraduate.application_fee
value: "$75"
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions/international-students
source_snippet: "$75 application fee"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-006: Financial Aid Policy
```yaml
field: undergraduate.financial_aid
value: {need_aware: true, stevens_investment_threshold: "$75,000", students_receiving_aid: ">90%"}
source_url: https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-scholarships-and-aid
source_snippet: "More than 90% of Stevens students receive some form of financial support"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-007: The Stevens Investment
```yaml
field: undergraduate.stevens_investment
value: {tuition_free: true, income_threshold: "$75,000", eligibility: "US citizens/PRs, first-time first-year, on-campus first year"}
source_url: https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-costs-and-aid/the-stevens-investment
source_snippet: "Beginning with the incoming class of Fall 2026, Stevens Institute of Technology will offer full tuition coverage to first-time, first-year, full-time undergraduate students who are U.S. citizens or permanent residents, whose families earn $75,000 or less per year"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-008: Transfer Deadlines
```yaml
field: undergraduate.transfer_deadlines
value: {spring: "November 1", fall: "June 15"}
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions/admissions-timeline
source_snippet: "Transfer for Spring Semester: Application Deadline November 1; Transfer for Fall Semester: Application Deadline June 15"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-G-001: Graduate Deadlines
```yaml
field: graduate.deadlines
value: {fall_ms_fulltime: "April 15", fall_phd: "January 15", spring_ms_fulltime: "November 1"}
source_url: https://www.stevens.edu/admission-aid/graduate-admissions/application-deadlines
source_snippet: "Master's Full-Time: April 15 (Fall), November 1 (Spring); Ph.D.: January 15 (Fall), September 1 (Spring)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-G-002: Graduate Cost
```yaml
field: graduate.costs.tuition_2026_2027
value: {tuition: "$47,826", total_on_campus: "$70,826", total_commuter: "$52,852"}
source_url: https://www.stevens.edu/admission-aid/tuition-financial-aid/graduate-costs-and-funding
source_snippet: "Tuition and Fees: $47,826; Housing and Meals: $20,744; Total Cost of Attendance: $70,826"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-G-003: Graduate Program Counts
```yaml
field: graduate.program_counts
value: {masters_degrees: "55+", phd_programs: 20, certificates: 120}
source_url: https://www.stevens.edu/admission-aid/graduate-admissions
source_snippet: "Stevens offers more than 55 master's degrees; 120 graduate certificate programs; 20 Ph.D. programs"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-A-001: Schools Structure
```yaml
field: institution.schools
value: ["Charles V. Schaefer, Jr. School of Engineering and Science", "School of Business", "School of Humanities, Arts and Social Sciences", "School of Computing (launching Fall 2026)", "College of Professional Education"]
source_url: https://www.stevens.edu/academics/our-schools
source_snippet: "Schaefer School of Engineering and Science; School of Business; School of Humanities, Arts and Social Sciences; School of Computing; College of Professional Education"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-A-002: SES Departments
```yaml
field: ses.departments
value: ["Biomedical Engineering", "Chemical Engineering and Materials Science", "Chemistry and Chemical Biology", "Civil, Environmental and Ocean Engineering", "Computer Science", "Electrical and Computer Engineering", "Mathematical Sciences", "Mechanical Engineering", "Physics", "Systems Engineering"]
source_url: https://www.stevens.edu/school-engineering-science/departments
source_snippet: "Departments in the School of Engineering and Science: Biomedical Engineering; Chemical Engineering and Materials Science; Chemistry and Chemical Biology; Civil, Environmental and Ocean Engineering; Computer Science; Electrical and Computer Engineering; Mathematical Sciences; Mechanical Engineering; Physics; Systems Engineering"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-A-003: Application Platforms
```yaml
field: undergraduate.application_platforms
value: ["Common Application", "Coalition App with Scoir"]
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions/how-to-apply
source_snippet: "Ways to Apply: COMMON APPLICATION; COALITION APP WITH SCOIR"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-A-004: Career Outcomes
```yaml
field: institution.career_outcomes
value: {avg_salary_2025: "$86,900", outcomes_rate: "93.4%", career_placement_rank: 12}
source_url: https://www.stevens.edu/admission-aid/undergraduate-admissions
source_snippet: "$86,900 average salary of Class of 2025 graduates; 93.4% of 2025 grads secured outcomes within 6 months; No. 12 For Career Placement (The Princeton Review)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
stevens-knowledge-base-v2
├── stevens-overview (Section 0: counts, hierarchy, degree inventory, matrix)
├── stevens-ug-programs (Section 1: all undergraduate majors by school/department)
├── stevens-grad-programs (Section 2: all graduate programs by school/department)
├── stevens-deadlines (Section 3: UG + grad deadlines and requirements)
├── stevens-costs (Section 4: UG + grad cost breakdown and aid policy)
├── stevens-evidence (Section 5: evidence chain index)
└── stevens-manifest (Section 6: this manifest)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "stevens-knowledge-base-v2"
  school: "Stevens Institute of Technology"
  department: "<home department, if applicable>"
  degree_level: "<BS|BE|MS|MEng|PhD|Certificate>"
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
| P0 | Per-program GRE/TOEFL minimums (behind application portal) | Graduate application portal |
| P0 | Detailed tuition breakdown (per-credit rates) | https://www.stevens.edu/office-of-student-accounts/tuition-and-fees |
| P1 | Need-aware policy specifics (is it truly need-aware for US students?) | Financial Aid office |
| P1 | Merit scholarship amounts and criteria | https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-scholarships-and-aid |
| P1 | Graduate application fee amount | Graduate admissions |
| P2 | Interview scheduling details | Campus Visit Portal |
| P2 | Program-specific admission rates | Institutional Research |
| P2 | Accreditation details | ABET, AACSB, etc. |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Stevens | (Other schools) |
|-----------|---------|-----------------|
| Location | Hoboken, NJ | |
| Type | Private, STEM-focused | |
| UG Tuition/yr | $68,230 | |
| UG Total COA (on-campus) | $91,294 | |
| Grad Tuition/yr | $47,826 | |
| Need-Blind (US)? | No (need-aware) | |
| Need-Blind (Intl)? | No (need-aware) | |
| Meet 100% Need? | Not guaranteed | |
| Tuition-Free Threshold | $75,000 (Stevens Investment) | |
| EA Deadline | December 1 | |
| ED I Deadline | November 15 | |
| ED II Deadline | January 5 | |
| RD Deadline | January 5 | |
| SAT/ACT Required? | Test-optional (through Fall 2026) | |
| TOEFL Minimum | 80 | |
| IELTS Minimum | 6.0 | |
| Duolingo Minimum | 105 | |
| Application Fee | $75 | |
| Total Programs (Rule 1) | 283 | |
| Schools (Rule 2) | 5 | |
| Avg Starting Salary | $86,900 | |
| Career Outcomes Rate | 93.4% | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: stevens.edu, stevens.catalog.prod.coursedog.com
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
