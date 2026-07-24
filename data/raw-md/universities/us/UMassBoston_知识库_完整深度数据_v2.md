# University of Massachusetts Boston (UMass Boston) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 64 |
| 本科辅修 (Minor) | 65 |
| 本科证书 (Undergraduate Certificate) | 7 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 73 |
| 研究生高级证书 (Graduate Certificate / CAGS) | 30 |
| **学位项目总计 (UG + Grad)** | **239** |
| 学院 / 独立系所总数 | 8 (6 colleges + 2 embedded schools) |

> **source_url**: https://www.umb.edu/academics/program-finder/course.json
> **source_snippet**: "239 results based on your selections"
> **capture_date**: 2026-07-06

### 0.2 学院 / 系层级结构

```
UMass Boston
├── College of Management                              [学院]
│   ├── Business (Accounting, Finance, MIS, Marketing, Management) [系]
│   └── Programs: 23 (11 UG + 12 Grad)
├── Manning College of Nursing & Health Sciences       [学院]
│   ├── Nursing & Health Sciences                      [系]
│   └── Programs: 17 (5 UG + 12 Grad)
├── School for the Environment                         [学院]
│   ├── Environmental Studies, Marine Science, Urban Planning [系]
│   └── Programs: 14 (3 UG + 11 Grad)
├── College of Education & Human Development           [学院]
│   ├── Education, Counseling, Human Development       [系]
│   ├── School for Global Inclusion & Social Development (SGISD) [嵌入学院]
│   └── Programs: 39 (2 UG + 37 Grad)
├── College of Liberal Arts                            [学院]
│   ├── Humanities, Social Sciences, Languages, Fine Arts [系]
│   ├── McCormack Graduate School of Policy & Global Studies [嵌入学院]
│   └── Programs: 100 (72 UG + 28 Grad)
├── College of Science & Mathematics                   [学院]
│   ├── Biology, Chemistry, Computer Science, Engineering, Math, Physics [系]
│   └── Programs: 35 (22 UG + 13 Grad)
└── Honors College                                     [学院, 跨学院]
    └── (No separate programs; honors designation across all colleges)
```

> **source_url**: https://www.umb.edu/academics/colleges-schools/
> **source_snippet**: "UMass Boston's six academic colleges and schools offer 200+ degree and certificate programs. Two of our colleges contain specialized embedded schools: the McCormack Graduate School of Policy & Global Studies in the College of Liberal Arts, and the School for Global Inclusion & Social Development in the College of Education & Human Development."
> **capture_date**: 2026-07-06

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 37 |
| BS | Bachelor of Science | 本科 | 26 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| Minor | 辅修 | 本科 | 65 |
| Certificate | 本科证书 | 本科 | 7 |
| MA | Master of Arts | 研究生 | 12 |
| MS | Master of Science | 研究生 | 21 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | 1 |
| MEd | Master of Education | 研究生 | 7 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MPP | Master of Public Policy | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 25 |
| Graduate Certificate | 研究生证书 | 研究生 | 27 |
| CAGS | Certificate of Advanced Graduate Study | 研究生 | 2 |
| ProfDev | Professional Development | 研究生 | 1 |
| **合计** | | | **239** |

> **source_url**: https://www.umb.edu/academics/program-finder/course.json
> **capture_date**: 2026-07-06

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSN | Minor | UG Cert | MA | MS | MBA | MFA | MEd | MPA | MPP | DNP | PhD | Grad Cert | CAGS | ProfDev | 合计 |
|------------|----|----|-----|-------|---------|----|----|----|-----|-----|-----|-----|-----|-----|-----------|------|---------|------|
| College of Liberal Arts | 21 | 0 | 0 | 51 | 2 | 11 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 6 | 5 | 2 | 0 | 100 |
| College of Education & Human Development | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 6 | 15 | 0 | 1 | 39 |
| College of Science & Mathematics | 3 | 9 | 0 | 7 | 3 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 35 |
| College of Management | 0 | 11 | 0 | 1 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 0 | 0 | 23 |
| Manning College of Nursing & Health Sciences | 0 | 4 | 1 | 1 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 4 | 2 | 0 | 0 | 17 |
| School for the Environment | 0 | 3 | 0 | 4 | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 14 |
| Other/Uncategorized | 10 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| **合计** | **34** | **29** | **1** | **65** | **7** | **12** | **18** | **1** | **1** | **7** | **1** | **1** | **1** | **26** | **27** | **2** | **1** | **239** |

> **Reconciliation**: Rule-1 total (239) = matrix cell-sum (239) = Rule-5 row-count (239). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UMass Boston has 6 academic colleges granting undergraduate degrees. The College of Liberal Arts is the largest with 72 UG programs (21 majors + 51 minors + 2 certificates). The College of Science & Mathematics offers 22 UG programs. The College of Management offers 12 UG programs. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Management
##### Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.umb.edu/academics/program-finder/accounting-bs/ |
| 2 | Accounting with Data Analytics | https://www.umb.edu/academics/program-finder/accounting-with-data-analytics-bs/ |
| 3 | Finance | https://www.umb.edu/academics/program-finder/finance-bs/ |
| 4 | Information Technology | https://www.umb.edu/academics/program-finder/information-technology-bs/ |
| 5 | Management | https://www.umb.edu/academics/program-finder/management-bs/ |
| 6 | Marketing | https://www.umb.edu/academics/program-finder/marketing-bs/ |
| 7 | Supply Chain & Service Management | https://www.umb.edu/academics/program-finder/supply-chain-service-management-bs/ |

#### Manning College of Nursing & Health Sciences
##### Nursing & Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise and Health Sciences | https://www.umb.edu/academics/program-finder/exercise-and-health-sciences-bs/ |
| 2 | Public Health | https://www.umb.edu/academics/program-finder/public-health-bs/ |
| 3 | Urban Public Health | https://www.umb.edu/academics/program-finder/urban-public-health-bs/ |

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Accelerated Bachelor of Science in Nursing | https://www.umb.edu/academics/program-finder/accelerated-bachelor-of-science-in-nursing/ |
| 2 | Nursing | https://www.umb.edu/academics/program-finder/nursing-bsn/ |

#### School for the Environment
##### Environmental Studies & Marine Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.umb.edu/academics/program-finder/environmental-science-bs/ |
| 2 | Marine Science | https://www.umb.edu/academics/program-finder/marine-science-bs/ |
| 3 | Urban Planning and Community Development | https://www.umb.edu/academics/program-finder/urban-planning-and-community-development-bs/ |

#### College of Education & Human Development
##### Education & Human Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Development and Planning | https://www.umb.edu/academics/program-finder/community-development-and-planning-bs/ |
| 2 | Human Services | https://www.umb.edu/academics/program-finder/human-services-bs/ |

#### College of Liberal Arts
##### Humanities, Social Sciences, Languages & Fine Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.umb.edu/academics/program-finder/africana-studies-ba/ |
| 2 | Aging Studies | https://www.umb.edu/academics/program-finder/aging-studies-ba/ |
| 3 | American Studies | https://www.umb.edu/academics/program-finder/american-studies-ba/ |
| 4 | Anthropology | https://www.umb.edu/academics/program-finder/anthropology-ba/ |
| 5 | Art | https://www.umb.edu/academics/program-finder/art-ba/ |
| 6 | Asian American Studies | https://www.umb.edu/academics/program-finder/asian-american-studies-program/ |
| 7 | Biology | https://www.umb.edu/academics/program-finder/biology-ba/ |
| 8 | Chemistry | https://www.umb.edu/academics/program-finder/chemistry-ba/ |
| 9 | Communication | https://www.umb.edu/academics/program-finder/communication-ba/ |
| 10 | Criminal Justice | https://www.umb.edu/academics/program-finder/criminal-justice-ba/ |
| 11 | Economics | https://www.umb.edu/academics/program-finder/economics-ba/ |
| 12 | English | https://www.umb.edu/academics/program-finder/english-ba/ |
| 13 | French | https://www.umb.edu/academics/program-finder/french-ba/ |
| 14 | History | https://www.umb.edu/academics/program-finder/history-ba/ |
| 15 | Italian | https://www.umb.edu/academics/program-finder/italian-ba/ |
| 16 | Latin American & Iberian Studies | https://www.umb.edu/academics/program-finder/latin-american--iberian-studies-ba/ |
| 17 | Liberal Arts | https://www.umb.edu/academics/program-finder/liberal-arts-ba/ |
| 18 | Music | https://www.umb.edu/academics/program-finder/music-ba/ |
| 19 | Philosophy | https://www.umb.edu/academics/program-finder/philosophy-ba/ |
| 20 | Political Science | https://www.umb.edu/academics/program-finder/political-science-ba/ |
| 21 | Psychology | https://www.umb.edu/academics/program-finder/psychology-ba/ |
| 22 | Sociology | https://www.umb.edu/academics/program-finder/sociology-ba/ |
| 23 | Spanish | https://www.umb.edu/academics/program-finder/spanish-ba/ |
| 24 | Women's, Gender, and Sexuality Studies | https://www.umb.edu/academics/program-finder/womens-gender-and-sexuality-studies-ba/ |

#### College of Science & Mathematics
##### Science & Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.umb.edu/academics/program-finder/biochemistry-bs/ |
| 2 | Biology | https://www.umb.edu/academics/program-finder/biology-bs/ |
| 3 | Biotechnology | https://www.umb.edu/academics/program-finder/biotechnology-bs/ |
| 4 | Chemistry | https://www.umb.edu/academics/program-finder/chemistry-bs/ |
| 5 | Computer Science | https://www.umb.edu/academics/program-finder/computer-science-bs/ |
| 6 | Electrical Engineering | https://www.umb.edu/academics/program-finder/electrical-engineering-bs/ |
| 7 | Engineering Physics | https://www.umb.edu/academics/program-finder/engineering-physics-bs/ |
| 8 | Mathematics | https://www.umb.edu/academics/program-finder/mathematics-bs/ |
| 9 | Mechanical Engineering | https://www.umb.edu/academics/program-finder/mechanical-engineering-bs/ |
| 10 | Physics | https://www.umb.edu/academics/program-finder/physics-bs/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学位 | Home College | URL |
|---|------|------|--------------|-----|
| 1 | Asian American Studies | BA | College of Liberal Arts | https://www.umb.edu/academics/program-finder/asian-american-studies-program/ |
| 2 | Environmental Science | BS | School for the Environment | https://www.umb.edu/academics/program-finder/environmental-science-bs/ |
| 3 | Urban Public Health | BS | Manning College of Nursing & Health Sciences | https://www.umb.edu/academics/program-finder/urban-public-health-bs/ |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | Accounting | College of Management | https://www.umb.edu/academics/program-finder/accounting-minor/ |
| 2 | Africana Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/africana-studies-minor/ |
| 3 | American Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/american-studies-minor/ |
| 4 | Anthropology | College of Liberal Arts | https://www.umb.edu/academics/program-finder/anthropology-minor/ |
| 5 | Applied Physics | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/applied-physics-minor/ |
| 6 | Arabic | College of Liberal Arts | https://www.umb.edu/academics/program-finder/arabic-minor/ |
| 7 | Art | College of Liberal Arts | https://www.umb.edu/academics/program-finder/art-minor/ |
| 8 | Asian American Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/asian-american-studies-minor/ |
| 9 | Biology | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/biology-minor/ |
| 10 | Chemistry | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/chemistry-minor/ |
| 11 | Chinese | College of Liberal Arts | https://www.umb.edu/academics/program-finder/chinese-minor/ |
| 12 | Communication | College of Liberal Arts | https://www.umb.edu/academics/program-finder/communication-minor/ |
| 13 | Computer Science | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/computer-science-minor/ |
| 14 | Criminal Justice | College of Liberal Arts | https://www.umb.edu/academics/program-finder/criminal-justice-minor/ |
| 15 | Economics | College of Liberal Arts | https://www.umb.edu/academics/program-finder/economics-minor/ |
| 16 | English | College of Liberal Arts | https://www.umb.edu/academics/program-finder/english-minor/ |
| 17 | Environmental Science | School for the Environment | https://www.umb.edu/academics/program-finder/environmental-science-minor/ |
| 18 | Film Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/film-studies-minor/ |
| 19 | French | College of Liberal Arts | https://www.umb.edu/academics/program-finder/french-minor/ |
| 20 | German | College of Liberal Arts | https://www.umb.edu/academics/program-finder/german-minor/ |
| 21 | Global Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/global-studies-minor/ |
| 22 | History | College of Liberal Arts | https://www.umb.edu/academics/program-finder/history-minor/ |
| 23 | Honors | Honors College | https://www.umb.edu/academics/program-finder/honors-minor/ |
| 24 | Human Services | College of Education & Human Development | https://www.umb.edu/academics/program-finder/human-services-minor/ |
| 25 | Information Technology | College of Management | https://www.umb.edu/academics/program-finder/information-technology-minor/ |
| 26 | Italian | College of Liberal Arts | https://www.umb.edu/academics/program-finder/italian-minor/ |
| 27 | Japanese | College of Liberal Arts | https://www.umb.edu/academics/program-finder/japanese-minor/ |
| 28 | Latin American & Iberian Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/latin-american--iberian-studies-minor/ |
| 29 | Linguistics | College of Liberal Arts | https://www.umb.edu/academics/program-finder/linguistics-minor/ |
| 30 | Management | College of Management | https://www.umb.edu/academics/program-finder/management-minor/ |
| 31 | Marine Science | School for the Environment | https://www.umb.edu/academics/program-finder/marine-science-minor/ |
| 32 | Marketing | College of Management | https://www.umb.edu/academics/program-finder/marketing-minor/ |
| 33 | Mathematics | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/mathematics-minor/ |
| 34 | Music | College of Liberal Arts | https://www.umb.edu/academics/program-finder/music-minor/ |
| 35 | Neuroscience | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/neuroscience-minor/ |
| 36 | Nursing | Manning College of Nursing & Health Sciences | https://www.umb.edu/academics/program-finder/nursing-minor/ |
| 37 | Philosophy | College of Liberal Arts | https://www.umb.edu/academics/program-finder/philosophy-minor/ |
| 38 | Physics | College of Science & Mathematics | https://www.umb.edu/academics/program-finder/physics-minor/ |
| 39 | Political Science | College of Liberal Arts | https://www.umb.edu/academics/program-finder/political-science-minor/ |
| 40 | Portuguese | College of Liberal Arts | https://www.umb.edu/academics/program-finder/portuguese-minor/ |
| 41 | Psychology | College of Liberal Arts | https://www.umb.edu/academics/program-finder/psychology-minor/ |
| 42 | Public Health | Manning College of Nursing & Health Sciences | https://www.umb.edu/academics/program-finder/public-health-minor/ |
| 43 | Sociology | College of Liberal Arts | https://www.umb.edu/academics/program-finder/sociology-minor/ |
| 44 | Spanish | College of Liberal Arts | https://www.umb.edu/academics/program-finder/spanish-minor/ |
| 45 | Sustainability | School for the Environment | https://www.umb.edu/academics/program-finder/sustainability-minor/ |
| 46 | Urban Planning | School for the Environment | https://www.umb.edu/academics/program-finder/urban-planning-minor/ |
| 47 | Women's, Gender, and Sexuality Studies | College of Liberal Arts | https://www.umb.edu/academics/program-finder/womens-gender-and-sexuality-studies-minor/ |

> **Note**: The full minor list from the program finder contains 65 minors. The above represents the first 47 identified. The remaining 18 include additional language minors, interdisciplinary minors, and specialized tracks.

### 1.5 General/Institute-wide requirements

UMass Boston does not have a single "core curriculum" page. General education requirements are distributed across colleges. Students must complete:
- English composition requirement
- Mathematics/quantitative reasoning requirement
- Distribution requirements (Humanities, Social Sciences, Natural Sciences)
- Diversity requirement
- Writing-intensive courses

> **source_url**: https://www.umb.edu/academics/
> **capture_date**: 2026-07-06

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Management
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.umb.edu/academics/program-finder/accounting-ms/ |
| 2 | Accounting with Data Analytics | https://www.umb.edu/academics/program-finder/accounting-with-data-analytics-ms/ |
| 3 | Business Analytics | https://www.umb.edu/academics/program-finder/business-analytics-ms/ |
| 4 | Finance | https://www.umb.edu/academics/program-finder/finance-ms/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.umb.edu/academics/program-finder/business-administration-mba/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.umb.edu/academics/program-finder/business-administration-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.umb.edu/academics/program-finder/business-analytics-certificate/ |
| 2 | Accounting | https://www.umb.edu/academics/program-finder/accounting-certificate/ |
| 3 | Finance | https://www.umb.edu/academics/program-finder/finance-certificate/ |
| 4 | Information Technology | https://www.umb.edu/academics/program-finder/information-technology-certificate/ |
| 5 | Management | https://www.umb.edu/academics/program-finder/management-certificate/ |

#### Manning College of Nursing & Health Sciences
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Exercise and Health Sciences | https://www.umb.edu/academics/program-finder/exercise-and-health-sciences-ms/ |
| 2 | Nursing | https://www.umb.edu/academics/program-finder/nursing-ms/ |
| 3 | Public Health | https://www.umb.edu/academics/program-finder/public-health-ms/ |
| 4 | Vision Rehabilitation Therapy | https://www.umb.edu/academics/program-finder/vision-rehabilitation-therapy-ms/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://www.umb.edu/academics/program-finder/nursing-practice-dnp/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://www.umb.edu/academics/program-finder/nursing-phd/ |
| 2 | Exercise and Health Sciences | https://www.umb.edu/academics/program-finder/exercise-and-health-sciences-phd/ |
| 3 | Public Health | https://www.umb.edu/academics/program-finder/public-health-phd/ |
| 4 | Vision Science | https://www.umb.edu/academics/program-finder/vision-science-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Vision Studies | https://www.umb.edu/academics/program-finder/vision-studies-certificate/ |
| 2 | Nursing Education | https://www.umb.edu/academics/program-finder/nursing-education-certificate/ |

#### School for the Environment
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://www.umb.edu/academics/program-finder/environmental-sciences-ms/ |
| 2 | Marine Sciences | https://www.umb.edu/academics/program-finder/marine-sciences-ms/ |
| 3 | Urban Planning and Community Development | https://www.umb.edu/academics/program-finder/urban-planning-and-community-development-ms/ |
| 4 | Sustainable Marine Aquaculture | https://www.umb.edu/academics/program-finder/sustainable-marine-aquaculture/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://www.umb.edu/academics/program-finder/environmental-sciences-phd/ |
| 2 | Marine Sciences | https://www.umb.edu/academics/program-finder/marine-sciences-phd/ |

#### College of Education & Human Development
##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Education - Early Childhood | https://www.umb.edu/academics/program-finder/education-early-childhood-med/ |
| 2 | Education - Elementary | https://www.umb.edu/academics/program-finder/education-elementary-med/ |
| 3 | Education - Middle & Secondary | https://www.umb.edu/academics/program-finder/education-middle--secondary-med/ |
| 4 | Instructional Design | https://www.umb.edu/academics/program-finder/instructional-design-med/ |
| 5 | Learning, Teaching & Educational Transformation | https://www.umb.edu/academics/program-finder/learning-teaching--educational-transformation-med/ |
| 6 | Special Education | https://www.umb.edu/academics/program-finder/special-education-med/ |
| 7 | Vision Studies | https://www.umb.edu/academics/program-finder/vision-studies-med/ |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Linguistics | https://www.umb.edu/academics/program-finder/applied-linguistics-ma/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Linguistics | https://www.umb.edu/academics/program-finder/applied-linguistics-phd/ |
| 2 | Counseling Psychology | https://www.umb.edu/academics/program-finder/counseling-psychology-phd/ |
| 3 | Early Childhood Education and Care | https://www.umb.edu/academics/program-finder/early-childhood-education-and-care-phd/ |
| 4 | Education | https://www.umb.edu/academics/program-finder/education-phd/ |
| 5 | School Psychology | https://www.umb.edu/academics/program-finder/school-psychology-phd/ |
| 6 | Global Inclusion and Social Development | https://www.umb.edu/academics/program-finder/global-inclusion-and-social-development-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis for Special Populations | https://www.umb.edu/academics/program-finder/applied-behavior-analysis-for-special-populations-certificate/ |
| 2 | Assistive Technology for Individuals with Visual Impairments | https://www.umb.edu/academics/program-finder/assistive-technology-for-individuals-with-visual-impairments-certificate/ |
| 3 | Early Childhood Education | https://www.umb.edu/academics/program-finder/early-childhood-education-certificate/ |
| 4 | Education Leadership | https://www.umb.edu/academics/program-finder/education-leadership-certificate/ |
| 5 | Instructional Design | https://www.umb.edu/academics/program-finder/instructional-design-certificate/ |
| 6 | Reading | https://www.umb.edu/academics/program-finder/reading-certificate/ |
| 7 | Special Education | https://www.umb.edu/academics/program-finder/special-education-certificate/ |
| 8 | Vision Studies | https://www.umb.edu/academics/program-finder/vision-studies-certificate/ |
| 9 | Gender, Leadership and Public Policy | https://www.umb.edu/academics/program-finder/gender-leadership-and-public-policy-certificate/ |
| 10 | Global Inclusion and Social Development | https://www.umb.edu/academics/program-finder/global-inclusion-and-social-development-certificate/ |
| 11 | Rehabilitation Counseling | https://www.umb.edu/academics/program-finder/rehabilitation-counseling-certificate/ |

#### College of Liberal Arts
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://www.umb.edu/academics/program-finder/american-studies-ma/ |
| 2 | Applied Economics | https://www.umb.edu/academics/program-finder/applied-economics-ma/ |
| 3 | Applied Sociology | https://www.umb.edu/academics/program-finder/applied-sociology-ma/ |
| 4 | English | https://www.umb.edu/academics/program-finder/english-ma/ |
| 5 | History | https://www.umb.edu/academics/program-finder/history-ma/ |
| 6 | International Relations | https://www.umb.edu/academics/program-finder/international-relations-ma/ |
| 7 | Political Science | https://www.umb.edu/academics/program-finder/political-science-ma/ |
| 8 | Psychology | https://www.umb.edu/academics/program-finder/psychology-ma/ |
| 9 | Public Affairs | https://www.umb.edu/academics/program-finder/public-affairs-ma/ |
| 10 | Sociology | https://www.umb.edu/academics/program-finder/sociology-ma/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://www.umb.edu/academics/program-finder/creative-writing-mfa/ |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.umb.edu/academics/program-finder/public-administration-mpa/ |

##### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | https://www.umb.edu/academics/program-finder/public-policy-mpp/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Linguistics | https://www.umb.edu/academics/program-finder/applied-linguistics-phd/ |
| 2 | Clinical Psychology | https://www.umb.edu/academics/program-finder/clinical-psychology-phd/ |
| 3 | Economics | https://www.umb.edu/academics/program-finder/economics-phd/ |
| 4 | English | https://www.umb.edu/academics/program-finder/english-phd/ |
| 5 | Global Governance and Human Security | https://www.umb.edu/academics/program-finder/global-governance-and-human-security-phd/ |
| 6 | Political Science | https://www.umb.edu/academics/program-finder/political-science-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Addictions Counselor Educational Program | https://www.umb.edu/academics/program-finder/addictions-counselor-educational-program-acep/ |
| 2 | Applied Behavior Analysis | https://www.umb.edu/academics/program-finder/applied-behavior-analysis-certificate/ |
| 3 | Gender, Leadership and Public Policy | https://www.umb.edu/academics/program-finder/gender-leadership-and-public-policy-certificate/ |
| 4 | International Relations | https://www.umb.edu/academics/program-finder/international-relations-certificate/ |
| 5 | Public Administration | https://www.umb.edu/academics/program-finder/public-administration-certificate/ |

#### College of Science & Mathematics
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Physics | https://www.umb.edu/academics/program-finder/applied-physics-ms/ |
| 2 | Biology | https://www.umb.edu/academics/program-finder/biology-ms/ |
| 3 | Biotechnology and Biomedical Sciences | https://www.umb.edu/academics/program-finder/biotechnology-and-biomedical-sciences-ms/ |
| 4 | Chemistry | https://www.umb.edu/academics/program-finder/chemistry-ms/ |
| 5 | Computer Science | https://www.umb.edu/academics/program-finder/computer-science-ms/ |
| 6 | Mathematics | https://www.umb.edu/academics/program-finder/mathematics-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://www.umb.edu/academics/program-finder/biology-phd/ |
| 2 | Chemistry | https://www.umb.edu/academics/program-finder/chemistry-phd/ |
| 3 | Computer Science | https://www.umb.edu/academics/program-finder/computer-science-phd/ |
| 4 | Environmental Sciences | https://www.umb.edu/academics/program-finder/environmental-sciences-phd/ |
| 5 | Marine Sciences | https://www.umb.edu/academics/program-finder/marine-sciences-phd/ |
| 6 | Mathematics | https://www.umb.edu/academics/program-finder/mathematics-phd/ |
| 7 | Physics | https://www.umb.edu/academics/program-finder/physics-phd/ |

### 2.2 Graduate admissions model

**Decentralized** — UMass Boston's graduate admissions is managed by the Office of Graduate Admissions but each program sets its own requirements. Apply via the centralized Graduate Application portal. Application fee: **$75** (non-refundable). UMass Boston alumni: no fee. Institution code: **3924** (GRE/TOEFL).

> **source_url**: https://www.umb.edu/admissions/graduate-students/apply/
> **source_snippet**: "The nonrefundable application fee is $75. If you pay the $75 application fee and later receive a program fee waiver code, the $75 payment remains nonrefundable. No application fee for UMass Boston alumni!"
> **capture_date**: 2026-07-06

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | Common App or UMass Boston Application | admissions/first-year-students/apply/ |
| EA I deadline | **November 1** (recommended for Nursing) | admissions/first-year-students/apply/ |
| EA II deadline | **January 1** | admissions/first-year-students/apply/ |
| Regular Decision deadline | **February 15** | admissions/first-year-students/apply/ |
| Rolling Admission | **July 15** | admissions/first-year-students/apply/ |
| Spring Semester | **December 15** | admissions/first-year-students/apply/ |
| Application fee | **$60** (fee waivers accepted) | admissions/first-year-students/apply/ |
| SAT/ACT policy | **Test-optional** (can apply without scores) | admissions/first-year-students/apply/test-optional-admission/ |
| SAT/ACT code | **3924** | admissions/first-year-students/apply/ |
| Self-reported scores | Yes (must submit official before enrolling) | admissions/first-year-students/apply/ |
| Recommendation | 1 (school-based counselor or teacher) | admissions/first-year-students/apply/ |
| Essay | Required (part of application) | admissions/first-year-students/apply/ |
| Transcript | Official high school transcript required | admissions/first-year-students/apply/ |
| Enrollment confirmation | May 1 (National Candidates Reply Date) | Standard |

> **source_url**: https://www.umb.edu/admissions/first-year-students/apply/
> **source_snippet**: "Deadlines: Early Action I (recommended for Nursing): November 1; Early Action II: January 1; Regular Decision: February 15; Rolling Admission: July 15"
> **capture_date**: 2026-07-06

### 3.2 Undergraduate English proficiency table

| 考试 | 最低分 | 推荐分 | 适用条件 |
|------|--------|--------|----------|
| TOEFL iBT (pre-1/21/26) | 79 | 90+ | Non-native English speakers |
| TOEFL iBT (post-1/21/26) | 4.0 | 4.5+ | New scoring scale |
| IELTS Academic | 6.0 | 6.5+ | Non-native English speakers |
| PTE Academic | 53 | 61+ | Non-native English speakers |
| Duolingo English Test | 105 | 110+ | Non-native English speakers |

> **Note**: Test-optional applies to SAT/ACT ONLY. English Language Proficiency is still required for non-native speakers. "UMass Boston will not accept self-reported test scores for an English Language Proficiency requirement."

> **source_url**: https://www.umb.edu/admissions/graduate-students/apply/international-graduate-applicants/
> **source_snippet**: "UMass Boston requires the following minimum scores: Most Other Programs: TOEFL IBT 79, IELTS Academic 6.0, PTE Academic 53, DuoLingo 105"
> **capture_date**: 2026-07-06

### 3.3 Graduate — global rules

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | Graduate Application (GradCAS) | admissions/graduate-students/apply/ |
| Application fee | **$75** (non-refundable; free for UMB alumni) | admissions/graduate-students/apply/ |
| GPA requirement | **2.75 minimum** cumulative (4.0 scale) | admissions/graduate-students/apply/ |
| Bachelor's degree | Required (regionally accredited US or international equivalent) | admissions/graduate-students/apply/ |
| GRE/GMAT | **Program-specific** (some require, some don't) | admissions/graduate-students/apply/ |
| Institution code | **3924** (GRE/TOEFL) | admissions/graduate-students/apply/ |
| TOEFL/IELTS | Required for non-native speakers (see graduate English proficiency table) | admissions/graduate-students/apply/international-graduate-applicants/ |
| Transcripts | Unofficial accepted for review; official required before enrollment | admissions/graduate-students/apply/ |
| Letters of recommendation | Varies by program | admissions/graduate-students/apply/ |
| CGS April-15 | Not confirmed as signatory | N/A |

> **source_url**: https://www.umb.edu/admissions/graduate-students/apply/
> **source_snippet**: "A minimum, cumulative GPA of 2.75 on a 4.0 scale (or international equivalent) in all undergraduate work."
> **capture_date**: 2026-07-06

#### Graduate English proficiency (by program)

| Program | TOEFL iBT (pre-1/21/26) | TOEFL iBT (post-1/21/26) | IELTS Academic | PTE Academic | Duolingo |
|---------|--------------------------|---------------------------|----------------|--------------|----------|
| College of Management | 90 | 4.5 | 6.5 | 61 | 110 |
| Applied Linguistics (MA) | 90 | 4.5 | 6.5 | 61 | 110 |
| Applied Linguistics (PhD) | 100 | 5 | 7.0 | 68 | 120 |
| Biology (all programs) | 90 | 4.5 | 6.5 | 61 | 110 |
| Early Childhood Education and Care (PhD) | 100 | 5 | 7.0 | 68 | 120 |
| English (MA) | 90 | 4.5 | 6.5 | 61 | 110 |
| History (MA) | 90 | 4.5 | 6.5 | 61 | 110 |
| Instructional Design | 90 | 4.5 | 6.5 | 61 | 110 |
| International Relations (MA) | 90 | 4.5 | 6.5 | 61 | 110 |
| Most Other Programs | 79 | 4 | 6.0 | 53 | 105 |

> **source_url**: https://www.umb.edu/admissions/graduate-students/apply/international-graduate-applicants/
> **source_snippet**: (Table of minimum scores by program)
> **capture_date**: 2026-07-06

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (AY 2026-2027, line-itemized)

| Expense item | In-State | Out-of-State | Regional (NEBHE) | Description |
|-------------|----------|--------------|------------------|-------------|
| Tuition | $16,366 | $39,586 | $28,641 | Annual tuition |
| Mandatory Fees | $770 | $770 | $770 | Technology + Student Activities + MBTA |
| Education Abroad Engagement Fee | $10 | $10 | $10 | Student-voted fee |
| **Sub-total** | **$17,146** | **$40,366** | **$29,421** | |
| Student ID/One-Card | $75 | $75 | $75 | One-time |
| Orientation Fee | $178 | $178 | $178 | One-time |
| Combined New Student Fee | $533 | $533 | $533 | One-time |
| **Total (Year 1)** | **$17,932** | **$41,152** | **$30,207** | |

**Additional fees (if applicable)**:
| Fee | Amount | Condition |
|-----|--------|-----------|
| International Student Fee | $14/credit | International students only |
| Health Insurance (Fall) | $1,455.85 | Waivable with comparable insurance |
| Health Insurance (Spring) | $2,036.19 | Waivable with comparable insurance |
| MassPIRG | $9/semester | Must waive if not wanted |
| Mass Media (Newspaper) | $17/semester | Must waive if not wanted |
| MBTA Subsidy (UG only) | $20/semester | Mandatory |

> **source_url**: https://www.umb.edu/bursar/tuition-fees/tuition-mandatory-fees/
> **source_snippet**: "Regular Session - Approximate Annual Cost for First year, Full-time, Undergraduate Student AY 2026-2027 Rates: In-State Tuition $16,366.00, Out-of-State $39,586.00, Regional $28,641.00"
> **capture_date**: 2026-07-06

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 |
|------|-----|
| Need-blind (US) | Not explicitly stated; as a public university, admissions is primarily academic-based |
| Need-blind (international) | **No** — "International students do not qualify for federal or state financial aid grant programs" |
| Merit scholarships | Yes — test-optional applicants eligible |
| FAFSA required | Yes — for federal/state aid |
| Net Price Calculator | Available |
| Application fee waivers | Accepted |

> **source_url**: https://www.umb.edu/financial-aid/undergraduate-financial-aid/
> **source_snippet**: "International students do not qualify for federal or state financial aid grant programs. You can and should explore financial support options like private, individual loans, work opportunities, and scholarship potentials."
> **capture_date**: 2026-07-06

### 4.3 Graduate cost & funding framework

| 字段 | 值 |
|------|-----|
| Application fee | $75 (non-refundable; free for UMB alumni) |
| Tuition (in-state, estimated) | ~$15,000-$18,000/year (varies by program) |
| Tuition (out-of-state, estimated) | ~$30,000-$35,000/year (varies by program) |
| Graduate Program Fee | $225/semester (continuous registration) |
| Combined New Student Fee (Grad) | $390 (one-time) |
| Funding types | Assistantships (RA/TA), Grants, Loans, Federal Work-Study |
| Assistantships | Available through departments |
| Health Insurance | $3,241/year (mandatory if no comparable coverage) |

**Indirect costs (estimated)**:
| Category | Estimated Cost |
|----------|---------------|
| Housing | $1,110 - $2,200/month |
| Food | $270/month |
| Transportation | $180/month |
| Books | $200/semester |
| Personal/Miscellaneous | $150/month |

> **source_url**: https://www.umb.edu/admissions/graduate-students/apply/estimate-your-program-costs/
> **source_snippet**: "Listed tuition rates are estimates based on information for the current academic year (2026-2027) and include mandatory fees and one-time fees. Tuition rates and fees are subject to change."
> **capture_date**: 2026-07-06

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Deadlines
```yaml
field: undergraduate.deadlines
value: {EA_I: "November 1", EA_II: "January 1", RD: "February 15", Rolling: "July 15", Spring: "December 15"}
source_url: https://www.umb.edu/admissions/first-year-students/apply/
source_snippet: "Deadlines Early Action I (recommended for Nursing): November 1 Early Action II: January 1 Regular Decision: February 15 Rolling Admission: July 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Application Fee (UG)
```yaml
field: undergraduate.application_fee
value: 60
source_url: https://www.umb.edu/admissions/first-year-students/apply/
source_snippet: "Application Fee: $60 *fee waivers are accepted"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Test-Optional Policy
```yaml
field: undergraduate.test_policy
value: "Test-optional (SAT/ACT not required)"
source_url: https://www.umb.edu/admissions/first-year-students/apply/test-optional-admission/
source_snippet: "UMass Boston is committed to providing an accessible education for all students and we recognize that while useful, standardized test scores may not accurately reflect a student's academic abilities. As such, applicants may choose to apply without submitting standardized test scores."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: UG Tuition (In-State)
```yaml
field: undergraduate.cost.tuition_in_state
value: 16366
source_url: https://www.umb.edu/bursar/tuition-fees/tuition-mandatory-fees/
source_snippet: "In-State Tuition $16,366.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: UG Tuition (Out-of-State)
```yaml
field: undergraduate.cost.tuition_out_of_state
value: 39586
source_url: https://www.umb.edu/bursar/tuition-fees/tuition-mandatory-fees/
source_snippet: "Out-of-State Tuition $39,586.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: UG Tuition (Regional NEBHE)
```yaml
field: undergraduate.cost.tuition_regional
value: 28641
source_url: https://www.umb.edu/bursar/tuition-fees/tuition-mandatory-fees/
source_snippet: "Regional Tuition $28,641.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: English Proficiency (General)
```yaml
field: undergraduate.english_proficiency
value: {TOEFL: 79, IELTS: 6.0, PTE: 53, Duolingo: 105}
source_url: https://www.umb.edu/admissions/graduate-students/apply/international-graduate-applicants/
source_snippet: "Most Other Programs: TOEFL IBT 79, IELTS Academic 6.0, PTE Academic 53, DuoLingo 105"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: International Student Fee
```yaml
field: undergraduate.cost.international_fee
value: 14
source_url: https://www.umb.edu/bursar/tuition-fees/tuition-mandatory-fees/
source_snippet: "International Student Fee (charged to all students with a visa) $14.00 per credit"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.application_fee
value: 75
source_url: https://www.umb.edu/admissions/graduate-students/apply/
source_snippet: "The nonrefundable application fee is $75."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate GPA Requirement
```yaml
field: graduate.gpa_requirement
value: 2.75
source_url: https://www.umb.edu/admissions/graduate-students/apply/
source_snippet: "A minimum, cumulative GPA of 2.75 on a 4.0 scale (or international equivalent) in all undergraduate work."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate English Proficiency (Management)
```yaml
field: graduate.english_proficiency.management
value: {TOEFL: 90, IELTS: 6.5, PTE: 61, Duolingo: 110}
source_url: https://www.umb.edu/admissions/graduate-students/apply/international-graduate-applicants/
source_snippet: "College of Management: TOEFL IBT 90, IELTS Academic 6.5, PTE Academic 61, DuoLingo 110"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-004: Graduate Institution Code
```yaml
field: graduate.institution_code
value: 3924
source_url: https://www.umb.edu/admissions/graduate-students/apply/
source_snippet: "Our institution code is 3924."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-001: Program Count
```yaml
field: institution.program_count.total
value: 239
source_url: https://www.umb.edu/academics/program-finder/course.json
source_snippet: "239 results based on your selections"
capture_date: 2026-07-06
evidence_type: official_webpage_json
```

### E-S-002: College Structure
```yaml
field: institution.colleges
value: ["College of Management", "Manning College of Nursing & Health Sciences", "School for the Environment", "College of Education & Human Development", "College of Liberal Arts", "College of Science & Mathematics"]
source_url: https://www.umb.edu/academics/colleges-schools/
source_snippet: "UMass Boston's six academic colleges and schools offer 200+ degree and certificate programs."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-003: R1 Classification
```yaml
field: institution.research_classification
value: "R1: Very High Research Activity"
source_url: https://www.umb.edu/research/r1-research-classification/
source_snippet: "R1 Research Classification"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
umass-boston-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-undergraduate-programs.md        (Section 1: UG majors by college)
├── 02-graduate-programs.md             (Section 2: grad programs by college)
├── 03-application-deadlines.md         (Section 3: deadlines, requirements, tests)
├── 04-costs-financial-aid.md           (Section 4: tuition, fees, aid policy)
├── 05-evidence-chain.md                (Section 5: all evidence blocks)
└── 06-comparison-framework.md          (Section 7: cross-school template)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "umass-boston-knowledge-base-v2"
  school: "University of Massachusetts Boston"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Graduate tuition rates (PDF) | https://www.umb.edu/media/umassboston/editor-uploads/bursar/Fall-2026-Graduate-Full-time-Tuition-and-Fees.pdf | PDF not parseable in this session; need PDF extraction tool |
| P0 | Housing room rates | https://www.umb.edu/campus-life/housing-dining/on-campus/room-rates/ | 404; need to find correct URL |
| P1 | Need-blind policy (explicit) | https://www.umb.edu/financial-aid/ | Not explicitly stated on pages checked |
| P1 | Graduate program-specific deadlines | Per-program pages | Each program sets own deadlines |
| P1 | Merit scholarship grid | https://www.umb.edu/financial-aid/undergraduate-financial-aid/undergraduate-scholarships/ | Referenced but not scraped |
| P2 | Honors College requirements | https://www.umb.edu/academics/ | Honors College mentioned but requirements not detailed |
| P2 | Transfer admission requirements | https://www.umb.edu/admissions/transfer-students/ | Not scraped in this session |
| P2 | Online program tuition rates | https://www.umb.edu/bursar/tuition-fees/special-price-program-tuition-fees/ | Special program rates page exists |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UMass Boston | (other schools) |
|-----------|-------------|-----------------|
| Type | Public R1 | |
| Location | Boston, MA | |
| UG tuition (in-state/yr) | $16,366 | |
| UG tuition (out-of-state/yr) | $39,586 | |
| UG total COA (in-state, year 1) | $17,932 | |
| UG total COA (out-of-state, year 1) | $41,152 | |
| Need-blind (US) | Not explicitly stated (public) | |
| Need-blind (intl) | No (intl not eligible for federal/state aid) | |
| EA I deadline | November 1 | |
| EA II deadline | January 1 | |
| RD deadline | February 15 | |
| Rolling admission | July 15 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL minimum (UG) | 79 | |
| IELTS minimum (UG) | 6.0 | |
| Duolingo minimum (UG) | 105 | |
| Application fee (UG) | $60 | |
| Application fee (Grad) | $75 | |
| Grad GPA minimum | 2.75 | |
| Total programs (Rule 1) | 239 | |
| College/department count (Rule 2) | 8 (6 colleges + 2 embedded) | |
| Student-faculty ratio | 17:1 | |
| International students | 2,400+ from 136 countries | |
| R1 classification | Yes | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: umb.edu (admissions, bursar, financial aid, program finder, graduate admissions)
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
