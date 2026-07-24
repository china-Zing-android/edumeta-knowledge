# University of Minnesota, Twin Cities (UMN) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 162 |
| 本科辅修 (Minor) | 328 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 302 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 135 |
| **学位项目总计 (UG + Grad)** | **946** |
| 学院 / 独立系所总数 | 17 |

> Source: UMN Twin Cities Catalog (Coursedog API), captured 2026-07-06

### 0.2 学院 / 系层级结构 (Rule 2 -- Hierarchy)

UMN Twin Cities has **19 colleges and schools** (17 with programs in the catalog, plus the Graduate School which administers research programs and 2 additional professional schools).

```
University of Minnesota, Twin Cities
├── Carlson School of Management [学院]
│   ├── Accounting, Finance, Marketing, Management, etc.
│   └── Programs: 37
├── College of Biological Sciences [学院]
│   ├── Biology, Biochemistry, Genetics, Ecology, etc.
│   └── Programs: 13
├── College of Continuing and Professional Studies [学院]
│   ├── Applied Sciences, Health Sciences, IT, etc.
│   └── Programs: 28
├── College of Design [学院]
│   ├── Architecture, Apparel Design, Graphic Design, etc.
│   └── Programs: 22
├── College of Education and Human Development [学院]
│   ├── Education, Social Work, Family Science, etc.
│   └── Programs: 78
├── College of Food, Agricultural and Natural Resource Sciences (CFANS) [学院]
│   ├── Agricultural Sciences, Environmental Sciences, Food Science, etc.
│   └── Programs: 38
├── College of Liberal Arts (CLA) [学院]
│   ├── Humanities, Social Sciences, Arts, Languages, etc.
│   └── Programs: 150
├── College of Science and Engineering (CSE) [学院]
│   ├── Engineering, Computer Science, Mathematics, Physical Sciences, etc.
│   └── Programs: 71
├── School of Nursing [学院]
│   └── Programs: 17
├── College of Pharmacy [学院]
│   └── Programs: 14
├── School of Dentistry [学院]
│   └── Programs: 17
├── School of Public Health [学院]
│   └── Programs: 32
├── Medical School [学院]
│   └── Programs: 20
├── Law School [学院]
│   └── Programs: 6
├── College of Veterinary Medicine [学院]
│   └── Programs: 13
├── Humphrey School of Public Affairs [学院]
│   └── Programs: 14
└── Graduate School [学院]
    └── Programs: 18
```

> Note: The Graduate School administers research-based graduate programs across multiple departments. Professional programs (Medicine, Dentistry, Law, Veterinary Medicine, Pharmacy) have their own schools with separate admissions.

### 0.3 学历级别明细 (Rule 3 -- Degree Level Inventory)

| 学位缩写 | canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|

| BS | BS | Bachelor of Science | 本科 | 89 |
| BA | BA | Bachelor of Arts | 本科 | 66 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 5 |
| BAS | BAS | Bachelor of Applied Science | 本科 | 3 |
| BMus | BMus | Bachelor of Music | 本科 | 3 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| Minor | Minor | Minor (辅修) | 本科 | 328 |
| MS | MS | Master of Science | 研究生 | 106 |
| MA | MA | Master of Arts | 研究生 | 46 |
| MFA | MFA | Master of Fine Arts | 研究生 | 4 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MAcc | MAcc | Master of Accountancy | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 17 |
| MSW | MSW | Master of Social Work | 研究生 | 2 |
| MPH | MPH | Master of Public Health | 研究生 | 8 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 1 |
| MN | MN | Master of Nursing | 研究生 | 1 |
| MPS | MPS | Master of Professional Studies | 研究生 | 10 |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 1 |
| MUP | MUP | Master of Urban Planning | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 98 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 2 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 3 |
| DDS | DDS | Doctor of Dental Surgery | 研究生 | 1 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| AuD | AuD | Doctor of Audiology | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| Certificate | Certificate | 高级证书/文凭 | 研究生 | 135 |
| Residency | Residency | 住院医师培训 | 研究生 | 1 |

> **学位规范化**: UMN uses standard US degree abbreviations. Engineering degrees have unique UMN-specific abbreviations (B.A.E.M., B.Ch.E., B.C.E., etc.) which map to canonical BS. Carlson School uses B.S.B. (Bachelor of Science in Business) which maps to canonical BS.

### 0.4 分布矩阵 (Rule 4 -- Distribution Cross-Tab)


| 学院 \ 级别 | BA | BS | BFA | BAS | BMus | BLA | Minor | MS | MA | MFA | MBA | MEd | MSW | MPH | MPA | MPP | MArch | MM | MN | MPS | MLA | MUP | MAcc | PhD | DNP | DPT | EdD | JD | MD | LLM | DDS | DVM | AuD | OTD | PharmD | Certificate | Residency | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlson School of Management | 4 | 10 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 37 |
| College of Biological Sciences | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 |
| College of Continuing and Professional Studies | 2 | 4 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 28 |
| College of Design | 0 | 5 | 2 | 0 | 0 | 1 | 0 | 4 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 22 |
| College of Education and Human Development | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 2 | 7 | 0 | 0 | 16 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 33 | 0 | 78 |
| College of Food, Agricultural and Natural Resource Sciences | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 38 |
| College of Liberal Arts | 57 | 10 | 3 | 0 | 3 | 0 | 0 | 4 | 31 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 8 | 0 | 150 |
| College of Pharmacy | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 14 |
| College of Science and Engineering | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 71 |
| College of Veterinary Medicine | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 0 | 13 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 18 |
| Humphrey School of Public Affairs | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 14 |
| Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Medical School | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 20 |
| School of Dentistry | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 9 | 1 | 17 |
| School of Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 17 |
| School of Public Health | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 32 |
| **合计** | 66 | 89 | 5 | 3 | 3 | 1 | 328 | 106 | 46 | 4 | 2 | 17 | 2 | 8 | 1 | 1 | 1 | 1 | 1 | 10 | 1 | 1 | 1 | 98 | 1 | 1 | 1 | 2 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 135 | 1 | **946** |

> Reconciliation: Rule-1 total (946) == matrix cell-sum (588) == Rule-5 row-count. ❌ MISMATCH 

---

## SECTION 1 -- Undergraduate Education

### 1.1 College Architecture

UMN Twin Cities has **8 freshman-admitting colleges** and **5 upper-division (transfer-only) colleges** for undergraduate education. See Section 0.2 for the full hierarchy tree.

**Freshman-admitting colleges**: Carlson School of Management, College of Biological Sciences, College of Design, College of Education and Human Development, College of Food Agricultural and Natural Resource Sciences (CFANS), College of Liberal Arts (CLA), College of Science and Engineering (CSE), School of Nursing.

**Transfer-only colleges**: College of Continuing and Professional Studies, Medical Laboratory Sciences (College of Pharmacy), Dental Hygiene (School of Dentistry), Mortuary Science (Medical School), Public Health (School of Public Health).

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别


#### Carlson School of Management

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Business Analytics M.A.B.A. | <https://umtc.catalog.prod.coursedog.com/programs/243230X02> |
| 2 | Business Administration M.B.A. | <https://umtc.catalog.prod.coursedog.com/programs/015230602> |
| 3 | Doctor of Business Administration D.B.A. | <https://umtc.catalog.prod.coursedog.com/programs/236662302> |
| 4 | Management Science M.B.A. | <https://umtc.catalog.prod.coursedog.com/programs/246930602> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/000420502> |
| 2 | Entrepreneurial Management B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/210620502> |
| 3 | Finance & Risk Management Insurance B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/219720502> |
| 4 | Finance B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/102220502> |
| 5 | Human Resources and Industrial Relations B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/039720502> |
| 6 | International Business B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/102520502> |
| 7 | Management Information Systems B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/102420502> |
| 8 | Marketing B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/102620502> |
| 9 | Public & Nonprofit Management B.S.B | <https://umtc.catalog.prod.coursedog.com/programs/217520502> |
| 10 | Supply Chain & Operations Management B.S.B. | <https://umtc.catalog.prod.coursedog.com/programs/219620502> |

#### College of Biological Sciences

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry B.S. | <https://umtc.catalog.prod.coursedog.com/programs/012420110> |
| 2 | Biology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/013220110> |
| 3 | Cellular and Organismal Physiology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/238520110> |
| 4 | Ecology, Evolution, and Behavior B.S. | <https://umtc.catalog.prod.coursedog.com/programs/025120110> |
| 5 | Genetics, Cell Biology, and Development B.S. | <https://umtc.catalog.prod.coursedog.com/programs/034520110> |
| 6 | Microbiology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/056020110> |
| 7 | Neuroscience B.S. | <https://umtc.catalog.prod.coursedog.com/programs/059020110> |
| 8 | Plant and Microbial Biology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/069720110> |

#### College of Continuing and Professional Studies

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Inter-College Program B.A. | <https://umtc.catalog.prod.coursedog.com/programs/203720218> |
| 2 | Multidisciplinary Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/226320218> |

##### BAS

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management B.A.Sc. | <https://umtc.catalog.prod.coursedog.com/programs/100624618> |
| 2 | Healthcare Management B.A.Sc. | <https://umtc.catalog.prod.coursedog.com/programs/231724618> |
| 3 | Information Technology Infrastructure B.A.Sc. | <https://umtc.catalog.prod.coursedog.com/programs/206724618> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences M.B.S. | <https://umtc.catalog.prod.coursedog.com/programs/011837918> |
| 2 | Health and Wellbeing Sciences B.S. | <https://umtc.catalog.prod.coursedog.com/programs/241320118> |
| 3 | Inter-College Program B.S. | <https://umtc.catalog.prod.coursedog.com/programs/203720118> |
| 4 | Multidisciplinary Studies B.S. | <https://umtc.catalog.prod.coursedog.com/programs/226320118> |

#### College of Design

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture B.D.A. | <https://umtc.catalog.prod.coursedog.com/programs/214623122> |
| 2 | Graphic Design B.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/036520922> |

##### BLA

| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Landscape Architecture | <https://umtc.catalog.prod.coursedog.com/programs/046822022> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Apparel Design B.S. | <https://umtc.catalog.prod.coursedog.com/programs/014320122> |
| 2 | Architecture B.S. | <https://umtc.catalog.prod.coursedog.com/programs/008820122> |
| 3 | Interior Design B.S. | <https://umtc.catalog.prod.coursedog.com/programs/044220122> |
| 4 | Product Design B.S. | <https://umtc.catalog.prod.coursedog.com/programs/224020122> |
| 5 | Retail and Consumer Studies B.S. | <https://umtc.catalog.prod.coursedog.com/programs/093120122> |

#### College of Education and Human Development

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Marketing Education B.S. | <https://umtc.catalog.prod.coursedog.com/programs/207520106> |
| 2 | Early Childhood B.S. | <https://umtc.catalog.prod.coursedog.com/programs/201820106> |
| 3 | Elementary Education: Foundations B.S. | <https://umtc.catalog.prod.coursedog.com/programs/035320106> |
| 4 | Family Social Science B.S. | <https://umtc.catalog.prod.coursedog.com/programs/029620106> |
| 5 | Human Resource Development B.S. | <https://umtc.catalog.prod.coursedog.com/programs/040220106> |
| 6 | Integrated Degree Program B.S. | <https://umtc.catalog.prod.coursedog.com/programs/228520106> |
| 7 | Kinesiology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/046520106> |
| 8 | Physical Activity and Health Promotion B.S. | <https://umtc.catalog.prod.coursedog.com/programs/246220106> |
| 9 | Special Education B.S. | <https://umtc.catalog.prod.coursedog.com/programs/087920106> |
| 10 | Sport Management B.S. | <https://umtc.catalog.prod.coursedog.com/programs/104520106> |
| 11 | Youth Studies B.S. | <https://umtc.catalog.prod.coursedog.com/programs/505520106> |

#### College of Food, Agricultural and Natural Resource Sciences

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Communication and Marketing B.S. | <https://umtc.catalog.prod.coursedog.com/programs/001920130> |
| 2 | Agricultural Education B.S. | <https://umtc.catalog.prod.coursedog.com/programs/002020130> |
| 3 | Agricultural and Food Business Management B.S. | <https://umtc.catalog.prod.coursedog.com/programs/009420130> |
| 4 | Animal Science B.S. | <https://umtc.catalog.prod.coursedog.com/programs/210420130> |
| 5 | Applied Economics B.S. | <https://umtc.catalog.prod.coursedog.com/programs/008320130> |
| 6 | Environmental Sciences, Policy and Management B.S. | <https://umtc.catalog.prod.coursedog.com/programs/216020130> |
| 7 | Fisheries, Wildlife, and Conservation Biology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/030020130> |
| 8 | Food Science B.S. | <https://umtc.catalog.prod.coursedog.com/programs/030820130> |
| 9 | Forest and Natural Resource Management B.S. | <https://umtc.catalog.prod.coursedog.com/programs/032420130> |
| 10 | Nutrition B.S. | <https://umtc.catalog.prod.coursedog.com/programs/059820130> |
| 11 | Plant Science B.S. | <https://umtc.catalog.prod.coursedog.com/programs/228820130> |
| 12 | Sustainable Agriculture and Food Systems B.S. | <https://umtc.catalog.prod.coursedog.com/programs/228920130> |
| 13 | Sustainable Systems Management B.S. | <https://umtc.catalog.prod.coursedog.com/programs/100820130> |

#### College of Liberal Arts

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | African American and African Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/000920217> |
| 2 | American Indian Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/005420217> |
| 3 | American Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/005620217> |
| 4 | Anthropology B.A. | <https://umtc.catalog.prod.coursedog.com/programs/008020217> |
| 5 | Art B.A. | <https://umtc.catalog.prod.coursedog.com/programs/009620217> |
| 6 | Art History B.A. | <https://umtc.catalog.prod.coursedog.com/programs/010420217> |
| 7 | Asian and Middle Eastern Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/202620217> |
| 8 | Astrophysics B.A. | <https://umtc.catalog.prod.coursedog.com/programs/011220217> |
| 9 | Bachelor of Individualized Studies B.I.S. | <https://umtc.catalog.prod.coursedog.com/programs/012326017> |
| 10 | Biology, Society, and Environment B.A. | <https://umtc.catalog.prod.coursedog.com/programs/205820217> |
| 11 | Chemistry B.A. | <https://umtc.catalog.prod.coursedog.com/programs/016820217> |
| 12 | Chicano-Latino Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/017020217> |
| 13 | Classical and Near Eastern Religions and Cultures B.A. | <https://umtc.catalog.prod.coursedog.com/programs/230720217> |
| 14 | Communication Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/088420217> |
| 15 | Computer Science B.A. | <https://umtc.catalog.prod.coursedog.com/programs/019620217> |
| 16 | Cultural Studies and Comparative Literature B.A. | <https://umtc.catalog.prod.coursedog.com/programs/023020217> |
| 17 | Dakota Language B.A. | <https://umtc.catalog.prod.coursedog.com/programs/250220217> |
| 18 | Dance B.A. | <https://umtc.catalog.prod.coursedog.com/programs/022320217> |
| 19 | Developmental Psychology B.A. | <https://umtc.catalog.prod.coursedog.com/programs/017220217> |
| 20 | Earth Sciences B.A. | <https://umtc.catalog.prod.coursedog.com/programs/035620217> |
| 21 | Economics - Quantitative B.A. | <https://umtc.catalog.prod.coursedog.com/programs/024520217> |
| 22 | Economics B.A. | <https://umtc.catalog.prod.coursedog.com/programs/024820217> |
| 23 | English B.A. | <https://umtc.catalog.prod.coursedog.com/programs/027620217> |
| 24 | Environmental Geosciences BA | <https://umtc.catalog.prod.coursedog.com/programs/026520217> |
| 25 | French Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/033620217> |
| 26 | French and Italian Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/033520217> |
| 27 | Gender, Women and Sexuality Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/097020217> |
| 28 | Geography B.A. | <https://umtc.catalog.prod.coursedog.com/programs/034820217> |
| 29 | German, Scandinavian, Dutch B.A. | <https://umtc.catalog.prod.coursedog.com/programs/228220217> |
| 30 | Global Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/136820217> |
| 31 | History B.A. | <https://umtc.catalog.prod.coursedog.com/programs/038020217> |
| 32 | Human Physiology B.A. | <https://umtc.catalog.prod.coursedog.com/programs/068820217> |
| 33 | Individually Designed Interdepartmental B.A. | <https://umtc.catalog.prod.coursedog.com/programs/045920217> |
| 34 | Italian Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/045220217> |
| 35 | Jewish Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/045820217> |
| 36 | Journalism B.A. | <https://umtc.catalog.prod.coursedog.com/programs/046020217> |
| 37 | Linguistics B.A. | <https://umtc.catalog.prod.coursedog.com/programs/050420217> |
| 38 | Mathematics B.A. | <https://umtc.catalog.prod.coursedog.com/programs/052020217> |
| 39 | Media and Information B.A. | <https://umtc.catalog.prod.coursedog.com/programs/051620217> |
| 40 | Music B.A. | <https://umtc.catalog.prod.coursedog.com/programs/058020217> |
| 41 | Ojibwe Language B.A. | <https://umtc.catalog.prod.coursedog.com/programs/220620217> |
| 42 | Philosophy B.A. | <https://umtc.catalog.prod.coursedog.com/programs/065220217> |
| 43 | Physics B.A. | <https://umtc.catalog.prod.coursedog.com/programs/067620217> |
| 44 | Political Science B.A. | <https://umtc.catalog.prod.coursedog.com/programs/071220217> |
| 45 | Psychology B.A. | <https://umtc.catalog.prod.coursedog.com/programs/081220217> |
| 46 | Religious Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/083420217> |
| 47 | Russian B.A. | <https://umtc.catalog.prod.coursedog.com/programs/084020217> |
| 48 | Sociology B.A. | <https://umtc.catalog.prod.coursedog.com/programs/086820217> |
| 49 | Sociology of Law, Criminology, and Justice B.A. | <https://umtc.catalog.prod.coursedog.com/programs/086720217> |
| 50 | Spanish Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/087620217> |
| 51 | Spanish and Portuguese Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/087720217> |
| 52 | Speech-Language-Hearing Sciences B.A. | <https://umtc.catalog.prod.coursedog.com/programs/088620217> |
| 53 | Statistical Practice B.A. | <https://umtc.catalog.prod.coursedog.com/programs/234320217> |
| 54 | Strategic Communication: Advertising and Public Relations B.A. | <https://umtc.catalog.prod.coursedog.com/programs/212520217> |
| 55 | Studies in Cinema and Media Culture B.A. | <https://umtc.catalog.prod.coursedog.com/programs/202720217> |
| 56 | Theatre Arts B.A. | <https://umtc.catalog.prod.coursedog.com/programs/092020217> |
| 57 | Urban Studies B.A. | <https://umtc.catalog.prod.coursedog.com/programs/093020217> |

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Acting B.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/205220917> |
| 2 | Art B.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/009620917> |
| 3 | Dance B.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/022320917> |

##### BMus

| # | 专业 | URL |
|---|------|-----|
| 1 | Music B. Mus. | <https://umtc.catalog.prod.coursedog.com/programs/058024717> |
| 2 | Music Education B. Mus | <https://umtc.catalog.prod.coursedog.com/programs/058424717> |
| 3 | Music Therapy B. Mus. | <https://umtc.catalog.prod.coursedog.com/programs/058624717> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/008020117> |
| 2 | Developmental Psychology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/017220117> |
| 3 | Economics B.S. | <https://umtc.catalog.prod.coursedog.com/programs/024820117> |
| 4 | Geography B.S. | <https://umtc.catalog.prod.coursedog.com/programs/034820117> |
| 5 | Psychology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/081220117> |
| 6 | Sociology B.S. | <https://umtc.catalog.prod.coursedog.com/programs/086820117> |
| 7 | Sociology of Law, Criminology, and Justice B.S. | <https://umtc.catalog.prod.coursedog.com/programs/086720117> |
| 8 | Statistical Science B.S. | <https://umtc.catalog.prod.coursedog.com/programs/234420117> |
| 9 | Technical Writing and Communication B.S. | <https://umtc.catalog.prod.coursedog.com/programs/091320117> |
| 10 | Urban Studies B.S. | <https://umtc.catalog.prod.coursedog.com/programs/093020117> |

#### College of Pharmacy

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Laboratory Sciences B.S. | <https://umtc.catalog.prod.coursedog.com/programs/230820115> |

#### College of Science and Engineering

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering and Mechanics B.A.E.M. | <https://umtc.catalog.prod.coursedog.com/programs/000821107> |
| 2 | Astrophysics B.S.Astrop. | <https://umtc.catalog.prod.coursedog.com/programs/011624207> |
| 3 | Biomedical Engineering B.Bm.E. | <https://umtc.catalog.prod.coursedog.com/programs/013428907> |
| 4 | Bioproducts and Biosystems Engineering B.B.B.E. | <https://umtc.catalog.prod.coursedog.com/programs/216629107> |
| 5 | Chemical Engineering B.Ch.E. | <https://umtc.catalog.prod.coursedog.com/programs/016021407> |
| 6 | Chemistry B.S.Chem. | <https://umtc.catalog.prod.coursedog.com/programs/016827007> |
| 7 | Civil Engineering B.C.E. | <https://umtc.catalog.prod.coursedog.com/programs/018021607> |
| 8 | Computer Engineering B.Comp.E. | <https://umtc.catalog.prod.coursedog.com/programs/018326107> |
| 9 | Computer Science B.S. Comp.Sc. | <https://umtc.catalog.prod.coursedog.com/programs/019627107> |
| 10 | Data Science B S D S | <https://umtc.catalog.prod.coursedog.com/programs/231329907> |
| 11 | Earth Sciences B.S. Earth Sciences | <https://umtc.catalog.prod.coursedog.com/programs/224429307> |
| 12 | Electrical Engineering B.E.E. | <https://umtc.catalog.prod.coursedog.com/programs/026421707> |
| 13 | Environmental Engineering B.Env.E | <https://umtc.catalog.prod.coursedog.com/programs/101929707> |
| 14 | Environmental Geosciences B S E G | <https://umtc.catalog.prod.coursedog.com/programs/02652A107> |
| 15 | Geoengineering B.GeoE. | <https://umtc.catalog.prod.coursedog.com/programs/035221807> |
| 16 | Industrial and Systems Engineering B.I.Sy.E. | <https://umtc.catalog.prod.coursedog.com/programs/214929607> |
| 17 | Materials Science and Engineering B.Mat.S.E. | <https://umtc.catalog.prod.coursedog.com/programs/052125507> |
| 18 | Mathematics B.S.Math. | <https://umtc.catalog.prod.coursedog.com/programs/052027207> |
| 19 | Mechanical Engineering B.M.E. | <https://umtc.catalog.prod.coursedog.com/programs/052822207> |
| 20 | Physics B.S. Phys. | <https://umtc.catalog.prod.coursedog.com/programs/067627307> |

#### College of Veterinary Medicine

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Medicine B S V S | <https://umtc.catalog.prod.coursedog.com/programs/094425003> |

#### Medical School

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Mortuary Science B.S. | <https://umtc.catalog.prod.coursedog.com/programs/057220111> |

#### School of Dentistry

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene B.S.D.H. | <https://umtc.catalog.prod.coursedog.com/programs/021624904> |

#### School of Nursing

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing B.S.N. | <https://umtc.catalog.prod.coursedog.com/programs/059620714> |

#### School of Public Health

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health B.A. | <https://umtc.catalog.prod.coursedog.com/programs/082020220> |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

> Note: UMN's interdisciplinary programs are typically housed within a single college but may involve coursework from multiple colleges. The University Honors Program is open to students across all colleges.

### 1.4 Minors -- Complete List


| # | Minor Name | Home College | URL |
|---|-----------|--------------|-----|
| 1 | Accounting Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0004MIN02> |
| 2 | Addictions Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2423MING18> |
| 3 | Advanced English Language Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/ro3hi9SiQNzbxfntDquM> |
| 4 | Aerospace Engineering and Mechanics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2148MING07> |
| 5 | African American and African Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0009MIN17> |
| 6 | Agricultural & Food Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2492MIN30> |
| 7 | Agricultural and Environmental Science Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2491MIN30> |
| 8 | Agricultural and Food Business Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0094MIN30> |
| 9 | Agronomy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0040MIN30> |
| 10 | American Indian Public Health and Wellness Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2404MING20> |
| 11 | American Indian Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0054MIN17> |
| 12 | American Indian and Indigenous Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2390MING17> |
| 13 | American Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0056MING17> |
| 14 | American Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0056MIN17> |
| 15 | Animal Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2104MIN30> |
| 16 | Animal Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0069MING30> |
| 17 | Anthropology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0080MIN17> |
| 18 | Anthropology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0080MING17> |
| 19 | Applied Economics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0083MIN30> |
| 20 | Applied Economics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0083MING30> |
| 21 | Applied Plant Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1150MING30> |
| 22 | Applied Psychology in Educational and Community Settings Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2189MIN06> |
| 23 | Applied/Computational Math | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0082MING08> |
| 24 | Architecture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0088MIN22> |
| 25 | Art History Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0104MING17> |
| 26 | Art History Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0104MIN17> |
| 27 | Art Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0096MIN17> |
| 28 | Art Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0096MING17> |
| 29 | Arts and Cultural Leadership Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/qImaDFPx6XXMEWtJBYTb> |
| 30 | Asian American Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2083MIN17> |
| 31 | Asian and Middle Eastern Cultures and Media Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2475MING17> |
| 32 | Asian and Middle Eastern Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2026MIN17> |
| 33 | Astrophysics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0116MING07> |
| 34 | Astrophysics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0112MIN17> |
| 35 | Austrian and Central European Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2116MIN17> |
| 36 | Behavioral Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2337MIN10> |
| 37 | Biblical Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0122MIN17> |
| 38 | Biochemistry Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0124MIN10> |
| 39 | Biochemistry, Molecular Biology and Biophysics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0135MING08> |
| 40 | Bioethics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0127MING08> |
| 41 | Bioinformatics and Computational Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2193MING07> |
| 42 | Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0132MIN10> |
| 43 | Biomedical Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0134MING07> |
| 44 | Bioproducts Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2010MIN30> |
| 45 | Bioproducts and Biosystems Science, Engineering and Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2194MING30> |
| 46 | Biostatistics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0138MING20> |
| 47 | Biotechnology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2516MIN10> |
| 48 | Business Administration Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0152MING02> |
| 49 | Business Analytics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2361MIN02> |
| 50 | Business Law Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2352MIN02> |
| 51 | Business Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2381MING02> |
| 52 | Business of Healthcare Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2437MIN02> |
| 53 | Cell Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2451MIN10> |
| 54 | Cellular and Molecular Neuroscience Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2403MIN10> |
| 55 | Chemical Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0160MING07> |
| 56 | Chemical Physics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0164MING07> |
| 57 | Chemistry Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0168MING07> |
| 58 | Chemistry Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0168MIN17> |
| 59 | Chicano-Latino Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0170MIN17> |
| 60 | Civil Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0180MING07> |
| 61 | Classical and Near Eastern Religions and Cultures Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0186MIN17> |
| 62 | Classical and Near Eastern Religions and Cultures Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1184MING17> |
| 63 | Climate Change and Health Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2477MING20> |
| 64 | Climate Justice Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/vqj0xTdnxqej2GdBBivt> |
| 65 | Climatology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2004MIN30> |
| 66 | Clinical Physiology and Movement Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2238MING06> |
| 67 | Cognitive Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0247MING17> |
| 68 | Communication Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0884MIN17> |
| 69 | Communication Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2074MING17> |
| 70 | Comparative Literature Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0192MING17> |
| 71 | Comparative Studies in Discourse and Society Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0231MING17> |
| 72 | Comparative U.S. Race and Ethnicity Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2171MIN17> |
| 73 | Computational Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2402MIN10> |
| 74 | Computer Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0196MING07> |
| 75 | Computer Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0196MIN17> |
| 76 | Conservation Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2351MING30> |
| 77 | Construction Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1006MIN18> |
| 78 | Corporate Environmental Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2141MIN30> |
| 79 | Creative Writing Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1203MIN17> |
| 80 | Cultural Studies and Comparative Literature Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0230MIN17> |
| 81 | Cyber Security Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2347MING07> |
| 82 | Dance Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0223MIN17> |
| 83 | Data Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2313MING07> |
| 84 | Data Science in Astrophysics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2434MING07> |
| 85 | Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1227MING22> |
| 86 | Development Practice Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2209MING16> |
| 87 | Developmental Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0172MIN17> |
| 88 | Developmental Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2420MING06> |
| 89 | Developmental Studies and Social Change Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0253MING17> |
| 90 | Digital Media Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2348MIN17> |
| 91 | Dutch Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0235MIN17> |
| 92 | Early Modern Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2210MING17> |
| 93 | Earth Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2244MING07> |
| 94 | Earth Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0356MIN17> |
| 95 | Ecological Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2199MIN07> |
| 96 | Ecological Restoration in Landscape Architecture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2333MING22> |
| 97 | Ecology, Evolution and Behavior Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1244MING10> |
| 98 | Econometrics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2456MIN17> |
| 99 | Economics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0248MING17> |
| 100 | Economics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0248MIN17> |
| 101 | Education, Curriculum, and Instruction Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2073MING06> |
| 102 | Educational Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0260MING06> |
| 103 | Educational Psychology Research Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2466MIN06> |
| 104 | Electrical Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0264MING07> |
| 105 | English Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0276MING17> |
| 106 | English Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0276MIN17> |
| 107 | Ensemble Music Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2511MIN17> |
| 108 | Entomology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0284MING30> |
| 109 | Entrepreneurial Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2106MIN02> |
| 110 | Entrepreneurship Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2521MIN02> |
| 111 | Environmental Geosciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0265MIN17> |
| 112 | Environmental Health Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0288MING20> |
| 113 | Environmental Sciences, Policy and Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2160MIN30> |
| 114 | Epidemiology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0292MING20> |
| 115 | Esports Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/NlkgEVhzSaHJgEK59fn6> |
| 116 | Family Financial Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2368MIN06> |
| 117 | Family Social Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0296MIN06> |
| 118 | Family Social Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0296MING06> |
| 119 | Family Therapy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2367MIN06> |
| 120 | Family Violence Prevention Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2039MIN06> |
| 121 | Family and Community Engagement Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2369MIN06> |
| 122 | Fashion Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2261MIN22> |
| 123 | Feminist and Critical Sexuality Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2242MING17> |
| 124 | Finance Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1022MIN02> |
| 125 | Financial Mathematics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2165MING07> |
| 126 | Finnish Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0299MIN17> |
| 127 | Fisheries, Wildlife, and Conservation Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0300MIN30> |
| 128 | Food Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0308MIN30> |
| 129 | Food Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0308MING30> |
| 130 | Food Systems Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0984MIN30> |
| 131 | Forest Ecosystem Management and Conservation Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0324MIN30> |
| 132 | French Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0336MING17> |
| 133 | French Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0336MIN17> |
| 134 | Gay, Lesbian, Bisexual, Transgender Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2127MIN17> |
| 135 | Gender, Intersectionality, and Public Policy Graduate Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/bz1kBhwMglD5LgtB4cFJ> |
| 136 | Gender, Women and Sexuality Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0970MIN17> |
| 137 | Genetics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0344MIN10> |
| 138 | Geoengineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0352MING07> |
| 139 | Geographic Information Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0349MIN17> |
| 140 | Geographic Information Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0349MING17> |
| 141 | Geography Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0348MING17> |
| 142 | Geography Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0348MIN17> |
| 143 | German Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0364MIN17> |
| 144 | Germanic Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1363MING17> |
| 145 | Gerontology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0369MING20> |
| 146 | Global Public Health Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2388MING20> |
| 147 | Global Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1368MIN17> |
| 148 | Graphic Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/j0VtqN2UhZ9kDp45G6Fq> |
| 149 | Greek Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0370MIN17> |
| 150 | Health Equity Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2354MING20> |
| 151 | Health Informatics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0383MING08> |
| 152 | Health Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2345MIN17> |
| 153 | Health Services Research, Policy, and Administration Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0405MING20> |
| 154 | Health and Genomics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2481MIN10> |
| 155 | Healthcare Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2317MIN18> |
| 156 | Hebrew Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0372MIN17> |
| 157 | Heritage Studies and Public History Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2362MING22> |
| 158 | Hispanic and Lusophone Literatures, Cultures, and Linguistics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2169MING17> |
| 159 | History Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0380MING17> |
| 160 | History Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0380MIN17> |
| 161 | History of Science, Technology, and Medicine Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2159MING08> |
| 162 | History of Science, Technology, and Medicine Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2159MIN17> |
| 163 | Horticulture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0400MIN30> |
| 164 | Human Factors and Ergonomics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1419MING22> |
| 165 | Human Resources and Industrial Relations Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0397MIN02> |
| 166 | Human Rights Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2078MING17> |
| 167 | Industrial and Systems Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2149MING07> |
| 168 | Infant and Early Childhood Mental Health Graduate Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2170MING06> |
| 169 | Information Technology Infrastructure Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2067MIN18> |
| 170 | Information Technology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1034MIN07> |
| 171 | Insect Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0284MIN30> |
| 172 | Integrative Biology and Physiology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2214MING11> |
| 173 | Integrative Leadership Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2277MING06> |
| 174 | Integrative Neuroscience Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0590MIN10> |
| 175 | Integrative Therapies & Healing Practices Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2243MING14> |
| 176 | Interdisciplinary Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1227MIN22> |
| 177 | Interior Environments Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2311MIN22> |
| 178 | Internal | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0445MING08> |
| 179 | International Agriculture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0447MIN30> |
| 180 | International Business Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1025MIN02> |
| 181 | International Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1007MING06> |
| 182 | Interpersonal Relationships Research Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0449MING06> |
| 183 | Islamic Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2421MIN17> |
| 184 | Italian Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2186MING17> |
| 185 | Italian Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0452MIN17> |
| 186 | Jewish Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0458MIN17> |
| 187 | Joint Military Science Leadership Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0537MIN18> |
| 188 | Kinesiology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0465MING06> |
| 189 | Land and Atmospheric Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2213MING30> |
| 190 | Landscape Architecture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0468MING22> |
| 191 | Landscape Design and Planning Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0286MIN22> |
| 192 | Latin Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0480MIN17> |
| 193 | Law Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0484MING09> |
| 194 | Leadership Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2003MIN35> |
| 195 | Learning Technologies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2395MIN06> |
| 196 | Lighting Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2412MING22> |
| 197 | Lighting Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2412MIN22> |
| 198 | Linguistics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0504MING17> |
| 199 | Linguistics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0504MIN17> |
| 200 | Literacy and Rhetorical Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2044MING17> |
| 201 | Long Term Care Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2458MIN18> |
| 202 | Management Information Systems Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1024MIN02> |
| 203 | Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0511MIN02> |
| 204 | Management of Technology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0555MIN07> |
| 205 | Management of Technology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0555MING07> |
| 206 | Managing People in Organizations Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2507MIN02> |
| 207 | Marine Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2299MIN10> |
| 208 | Marketing Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1026MIN02> |
| 209 | Mass Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0516MING17> |
| 210 | Materials Science and Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0521MING07> |
| 211 | Mathematics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0520MIN17> |
| 212 | Mathematics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0520MING07> |
| 213 | Mechanical Engineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0528MING07> |
| 214 | Media and Information Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0516MIN17> |
| 215 | Medical Laboratory Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/pszf5e9hgHE6Myz2ZmXY> |
| 216 | Medical Spanish Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/QsvOMnj7uXit0PipkjjL> |
| 217 | Medieval Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0550MING17> |
| 218 | Medieval Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0550MIN17> |
| 219 | Microbiology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0560MIN10> |
| 220 | Microbiology, Immunology, and Cancer Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1566MING11> |
| 221 | Molecular Pharmacology and Therapeutics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2480MING11> |
| 222 | Molecular, Cellular, Developmental Biology and Genetics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0571MING08> |
| 223 | Moving Image Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2241MING17> |
| 224 | Moving Image, Media and Sound Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/lRnoYeKijha3voP0JMXJ> |
| 225 | Museum & Curatorial Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2459MIN17> |
| 226 | Museum Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0577MING22> |
| 227 | Music Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0580MING17> |
| 228 | Music Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0580MIN17> |
| 229 | Native American Environmental Knowledge Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2252MIN30> |
| 230 | Natural Resources Science and Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2072MING30> |
| 231 | Neuroengineering Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2271MING07> |
| 232 | Neuroscience Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0590MING11> |
| 233 | Norwegian Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0589MIN17> |
| 234 | Nutrition Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0598MING30> |
| 235 | Nutrition Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0598MIN30> |
| 236 | Oral Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0614MING04> |
| 237 | Parent and Family Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/MDSiJNQpXEsX4bxfWpKQ> |
| 238 | Park and Protected Area Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0756MIN30> |
| 239 | Pharmaceutical Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/hBUj79LwuFvS5bZ7Nuy3> |
| 240 | Pharmaceutics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0636MING15> |
| 241 | Pharmacology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0644MIN10> |
| 242 | Pharmacotherapy and Health Systems Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/p29OTlHdLmDo6eSJldjN> |
| 243 | Philosophy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0652MING17> |
| 244 | Philosophy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0652MIN17> |
| 245 | Physical Activity and Health Promotion Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2375MIN06> |
| 246 | Physics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0676MING07> |
| 247 | Physics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0676MIN17> |
| 248 | Plant Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0697MIN10> |
| 249 | Plant Pathology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0693MING30> |
| 250 | Plant and Microbial Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0697MING10> |
| 251 | Political Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0711MING17> |
| 252 | Political Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0712MIN17> |
| 253 | Population Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2132MING17> |
| 254 | Population Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2132MIN17> |
| 255 | Portuguese Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0716MIN17> |
| 256 | Prevention Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2203MING06> |
| 257 | Product Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2240MING22> |
| 258 | Product Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2240MIN22> |
| 259 | Program Evaluation Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2029MING06> |
| 260 | Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0812MING17> |
| 261 | Psychology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0812MIN17> |
| 262 | Public Health Data Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/uqg0mdIIZh775sWFAXVc> |
| 263 | Public Health Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0820MIN17> |
| 264 | Public Health Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0820MING20> |
| 265 | Public Interest Design Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2374MIN22> |
| 266 | Public Policy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1778MING16> |
| 267 | Quaternary Paleoecology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0809MING07> |
| 268 | Race, Indigeneity, Disability, Gender, and Sexuality Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2409MING17> |
| 269 | Racial Justice in Urban Schooling Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2373MIN06> |
| 270 | Real Estate Development and Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/Y4cYVnMXkQfk7uXCTliX> |
| 271 | Religious Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0834MING17> |
| 272 | Religious Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0834MIN17> |
| 273 | Retail and Consumer Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0931MIN22> |
| 274 | Rhetoric, Scientific and Technical Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0831MING17> |
| 275 | Risk Management and Insurance Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1027MIN02> |
| 276 | Robotics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2429MING07> |
| 277 | Russian Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0840MIN17> |
| 278 | Science Communication & Outreach Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/us2Ge7uFSYTmwI2EecNW> |
| 279 | Science, Technology, and Environmental Policy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1867MING16> |
| 280 | Scientific and Technical Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0897MING17> |
| 281 | Security Technologies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2201MING07> |
| 282 | Sexual Health Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2376MING20> |
| 283 | Social Justice Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2143MIN06> |
| 284 | Social Science Genetics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/LcUpbCx5AvUAM0DDRkhB> |
| 285 | Social and Administrative Pharmacy Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0855MING15> |
| 286 | Sociocultural Studies in Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0887MING06> |
| 287 | Sociology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0868MING17> |
| 288 | Sociology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0868MIN17> |
| 289 | Sociology of Law, Criminology, and Justice Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0867MIN17> |
| 290 | Soil Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0874MIN30> |
| 291 | Spanish Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0876MIN17> |
| 292 | Special Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0879MIN06> |
| 293 | Special Education Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2493MING06> |
| 294 | Speech-Language-Hearing Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0886MIN17> |
| 295 | Speech-Language-Hearing Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2136MING17> |
| 296 | Sport Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1045MIN06> |
| 297 | Sport Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2040MING06> |
| 298 | Sports Coaching Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0187MIN06> |
| 299 | Sports Media and Promotion Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/h3MiV2t0W1Q9P014Q0YO> |
| 300 | Statistics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0900MING17> |
| 301 | Statistics Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0900MIN17> |
| 302 | Stem Cell Biology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2200MING11> |
| 303 | Strategic Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2425MIN02> |
| 304 | Studies in Africa and African Diaspora Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0893MING17> |
| 305 | Studies in Cinema and Media Culture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2027MIN17> |
| 306 | Studies of Science and Technology Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0907MING17> |
| 307 | Supply Chain & Operations Management Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2196MIN02> |
| 308 | Sustainability Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2163MIN30> |
| 309 | Sustainable Agriculture Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0983MIN30> |
| 310 | Sustainable Agriculture Systems Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0983MING30> |
| 311 | Swedish Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0903MIN17> |
| 312 | Teaching English as a Second Language Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2105MIN06> |
| 313 | Technical Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1B1zyNEtH8FAa04lVn13> |
| 314 | Technical Writing and Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0913MIN17> |
| 315 | Theatre Arts Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0920MIN17> |
| 316 | Theatre Arts Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0920MING17> |
| 317 | Translational Sensory Sciences Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2398MING17> |
| 318 | University Honors Program | N/A | <https://umtc.catalog.prod.coursedog.com/programs/LipYiE9A7BEBsvpy9DgX> |
| 319 | Urban Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0930MIN17> |
| 320 | Urban and Community Forestry Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0942MIN30> |
| 321 | Urban and Regional Planning Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/1925MING16> |
| 322 | User Experience (UX) Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2455MIN22> |
| 323 | Water Resources Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/0979MING08> |
| 324 | Water Science Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2012MIN30> |
| 325 | Wildlife Care and Handling Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2357MIN30> |
| 326 | World Music Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/2433MIN17> |
| 327 | Writing, Rhetoric, and Technical Communication Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/dkh21WRsTi7DhR6Sj7UJ> |
| 328 | Youth Studies Minor | N/A | <https://umtc.catalog.prod.coursedog.com/programs/5055MIN06> |


### 1.5 General Education Requirements

UMN Twin Cities requires all undergraduate students to complete the **Liberal Education Requirements** (LEP), which span multiple knowledge areas including:
- Written and Oral Communication
- Mathematical Thinking
- Biological Sciences, Physical Sciences, and Technology
- Historical Perspectives, Social Sciences, and Human Diversity
- Literature, Fine Arts, and Philosophy
- Global Perspectives and Ethical/Civic Responsibility

> Source: UMN Twin Cities Catalog

### 1.6 Total Undergraduate Program Count

| Category | Count |
|----------|-------|
| Degree Majors | 162 |
| Minors | 328 |
| **Total UG Programs** | **490** |

---

## SECTION 2 -- Graduate Education

### 2.1 Graduate Programs -- Grouped by 学院 > 系 > 学位级别


#### Carlson School of Management

##### MAcc

| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy M.Acc | <https://umtc.catalog.prod.coursedog.com/programs/215639702> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/230031502> |
| 2 | Business Research M.S. | <https://umtc.catalog.prod.coursedog.com/programs/232431502> |
| 3 | Business Taxation M.B.T. | <https://umtc.catalog.prod.coursedog.com/programs/015836402> |
| 4 | Finance M.S. | <https://umtc.catalog.prod.coursedog.com/programs/102231502> |
| 5 | Human Resources and Industrial Relations M.H.R.I.R. | <https://umtc.catalog.prod.coursedog.com/programs/039730W02> |
| 6 | Marketing M.MKTG | <https://umtc.catalog.prod.coursedog.com/programs/102630Y02> |
| 7 | Supply Chain Management M.S. | <https://umtc.catalog.prod.coursedog.com/programs/204731502> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/015260202> |

#### College of Biological Sciences

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology, Evolution and Behavior M.S. | <https://umtc.catalog.prod.coursedog.com/programs/124431510> |
| 2 | Microbial Engineering M.S. | <https://umtc.catalog.prod.coursedog.com/programs/056731510> |
| 3 | Plant and Microbial Biology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/069731510> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology, Evolution and Behavior Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/124460210> |
| 2 | Plant and Microbial Biology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/069760210> |

#### College of Continuing and Professional Studies

##### MPS

| # | 项目 | URL |
|---|------|-----|
| 1 | Addictions Counseling M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/234930I18> |
| 2 | Applied Sciences Leadership M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/243930I18> |
| 3 | Arts and Cultural Leadership M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/224530I18> |
| 4 | Civic Engagement M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/240030I18> |
| 5 | Horticulture M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/225130I18> |
| 6 | Integrated Behavioral Health M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/227030I18> |
| 7 | Sexual Health M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/237630I18> |

#### College of Design

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Design M.A. | <https://umtc.catalog.prod.coursedog.com/programs/122730422> |
| 2 | Heritage Studies and Public History M.H.S.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/236230S22> |

##### MArch

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture M.Arch. | <https://umtc.catalog.prod.coursedog.com/programs/008830322> |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Design M.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/122730822> |

##### MLA

| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture M.L.A. | <https://umtc.catalog.prod.coursedog.com/programs/046836722> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture M.S. | <https://umtc.catalog.prod.coursedog.com/programs/008831522> |
| 2 | Design M.S. | <https://umtc.catalog.prod.coursedog.com/programs/122731522> |
| 3 | Human Factors and Ergonomics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/141931522> |
| 4 | Landscape Architecture M.S. | <https://umtc.catalog.prod.coursedog.com/programs/046831522> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Design Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/122760222> |
| 2 | Human Factors and Ergonomics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/141960222> |

#### College of Education and Human Development

##### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Organizational Leadership, Policy, and Development Ed.D. | <https://umtc.catalog.prod.coursedog.com/programs/229860106> |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Child and Adolescent Development M.A. | <https://umtc.catalog.prod.coursedog.com/programs/236030406> |
| 2 | Developmental Psychology MA | <https://umtc.catalog.prod.coursedog.com/programs/242030406> |
| 3 | Education, Curriculum, and Instruction M.A. | <https://umtc.catalog.prod.coursedog.com/programs/207330406> |
| 4 | Educational Psychology M.A. | <https://umtc.catalog.prod.coursedog.com/programs/026030406> |
| 5 | Family Social Science M.A. | <https://umtc.catalog.prod.coursedog.com/programs/029630406> |
| 6 | Organizational Leadership, Policy, and Development M.A. | <https://umtc.catalog.prod.coursedog.com/programs/229830406> |
| 7 | Sport Management M. A. | <https://umtc.catalog.prod.coursedog.com/programs/204030406> |

##### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Adult Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/000335006> |
| 2 | Curriculum and Instruction M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/024135006> |
| 3 | Early Care and Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/250935006> |
| 4 | Early Childhood Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/023835006> |
| 5 | Family Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/033735006> |
| 6 | Human Resource Development M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/040235006> |
| 7 | Leadership in Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/092435006> |
| 8 | Literacy Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/212935006> |
| 9 | Physical Activity and Health M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/237035006> |
| 10 | Special Education Initial License M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/234135006> |
| 11 | Special Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/087935006> |
| 12 | Sport Management M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/204035006> |
| 13 | Sport and Exercise Science M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/233435006> |
| 14 | Teaching M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/099235006> |
| 15 | Work and Human Resource Education M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/095935006> |
| 16 | Youth Development Leadership M.Ed. | <https://umtc.catalog.prod.coursedog.com/programs/095435006> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Kinesiology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/046531506> |
| 2 | Master of Learning and Talent Development | <https://umtc.catalog.prod.coursedog.com/programs/250830Z06> |

##### MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work M.S.W. | <https://umtc.catalog.prod.coursedog.com/programs/086431406> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Developmental Psychology PhD | <https://umtc.catalog.prod.coursedog.com/programs/242060206> |
| 2 | Education, Curriculum, and Instruction Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/207360206> |
| 3 | Educational Psychology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/026060206> |
| 4 | Family Social Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/029660206> |
| 5 | Kinesiology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/046560206> |
| 6 | Organizational Leadership, Policy, and Development Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/229860206> |
| 7 | Social Work Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/086460206> |

#### College of Food, Agricultural and Natural Resource Sciences

##### MPS

| # | 项目 | URL |
|---|------|-----|
| 1 | Dietetics M.P.S. | <https://umtc.catalog.prod.coursedog.com/programs/022830I30> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education & Communication MS | <https://umtc.catalog.prod.coursedog.com/programs/252031530> |
| 2 | Agricultural Education M.S. | <https://umtc.catalog.prod.coursedog.com/programs/002031530> |
| 3 | Animal Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/006931530> |
| 4 | Applied Economics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/008331530> |
| 5 | Applied Plant Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/115031530> |
| 6 | Bioproducts and Biosystems Science, Engineering and Management M.S. | <https://umtc.catalog.prod.coursedog.com/programs/219431530> |
| 7 | Conservation Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/235131530> |
| 8 | Entomology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/028431530> |
| 9 | Food Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/030831530> |
| 10 | Land and Atmospheric Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/221331530> |
| 11 | Natural Resources Science and Management M.S. | <https://umtc.catalog.prod.coursedog.com/programs/207231530> |
| 12 | Nutrition M.S. | <https://umtc.catalog.prod.coursedog.com/programs/059831530> |
| 13 | Plant Pathology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/069331530> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Sciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/006960230> |
| 2 | Applied Economics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/008360230> |
| 3 | Applied Plant Sciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/115060230> |
| 4 | Bioproducts and Biosystems Science, Engineering and Management Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/219460230> |
| 5 | Conservation Sciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/235160230> |
| 6 | Entomology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/028460230> |
| 7 | Food Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/030860230> |
| 8 | Land and Atmospheric Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/221360230> |
| 9 | Natural Resources Science and Management Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/207260230> |
| 10 | Nutrition Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/059860230> |
| 11 | Plant Pathology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/069360230> |

#### College of Liberal Arts

##### AuD

| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology Au.D. | <https://umtc.catalog.prod.coursedog.com/programs/211762017> |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies M.A. | <https://umtc.catalog.prod.coursedog.com/programs/005630417> |
| 2 | Anthropology M.A. | <https://umtc.catalog.prod.coursedog.com/programs/008030417> |
| 3 | Art History M.A. | <https://umtc.catalog.prod.coursedog.com/programs/010430417> |
| 4 | Asian and Middle Eastern Cultures and Media MA | <https://umtc.catalog.prod.coursedog.com/programs/247530417> |
| 5 | Asian and Middle Eastern Studies MA | <https://umtc.catalog.prod.coursedog.com/programs/247830417> |
| 6 | Classical and Near Eastern Religions and Cultures M.A. | <https://umtc.catalog.prod.coursedog.com/programs/251930417> |
| 7 | Classical and Near Eastern Studies M.A. | <https://umtc.catalog.prod.coursedog.com/programs/118430417> |
| 8 | Communication Studies M.A. | <https://umtc.catalog.prod.coursedog.com/programs/207430417> |
| 9 | Comparative Literature M.A. | <https://umtc.catalog.prod.coursedog.com/programs/019230417> |
| 10 | Comparative Studies in Discourse and Society M.A. | <https://umtc.catalog.prod.coursedog.com/programs/023130417> |
| 11 | Economics M.A. | <https://umtc.catalog.prod.coursedog.com/programs/024830417> |
| 12 | English M.A. | <https://umtc.catalog.prod.coursedog.com/programs/027630417> |
| 13 | Feminist Studies M.A. | <https://umtc.catalog.prod.coursedog.com/programs/032930417> |
| 14 | French M.A. | <https://umtc.catalog.prod.coursedog.com/programs/033630417> |
| 15 | Geography M.A. | <https://umtc.catalog.prod.coursedog.com/programs/034830417> |
| 16 | Germanic Studies M.A. | <https://umtc.catalog.prod.coursedog.com/programs/136330417> |
| 17 | Health Communication M.A. | <https://umtc.catalog.prod.coursedog.com/programs/231930417> |
| 18 | Hispanic and Lusophone Literatures, Cultures, and Linguistics M.A. | <https://umtc.catalog.prod.coursedog.com/programs/216930417> |
| 19 | History M.A. | <https://umtc.catalog.prod.coursedog.com/programs/038030417> |
| 20 | Linguistics M.A. | <https://umtc.catalog.prod.coursedog.com/programs/050430417> |
| 21 | Mass Communication M.A. | <https://umtc.catalog.prod.coursedog.com/programs/051630417> |
| 22 | Music D.M.A. | <https://umtc.catalog.prod.coursedog.com/programs/058061717> |
| 23 | Music M.A. | <https://umtc.catalog.prod.coursedog.com/programs/058030417> |
| 24 | Philosophy M.A. | <https://umtc.catalog.prod.coursedog.com/programs/065230417> |
| 25 | Political Science M.A. | <https://umtc.catalog.prod.coursedog.com/programs/071230417> |
| 26 | Psychology M.A. | <https://umtc.catalog.prod.coursedog.com/programs/081230417> |
| 27 | Rhetoric, Scientific and Technical Communication M.A. | <https://umtc.catalog.prod.coursedog.com/programs/083130417> |
| 28 | Sociology M.A. | <https://umtc.catalog.prod.coursedog.com/programs/086830417> |
| 29 | Speech-Language-Hearing Science M.A. | <https://umtc.catalog.prod.coursedog.com/programs/213630417> |
| 30 | Strategic Communication M.A. | <https://umtc.catalog.prod.coursedog.com/programs/212530417> |
| 31 | Theatre Arts M.A. | <https://umtc.catalog.prod.coursedog.com/programs/092030417> |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Art M.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/009630817> |
| 2 | Creative Writing M.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/120330817> |
| 3 | Theatre Arts M.F.A. | <https://umtc.catalog.prod.coursedog.com/programs/092030817> |

##### MM

| # | 项目 | URL |
|---|------|-----|
| 1 | Music M.M. | <https://umtc.catalog.prod.coursedog.com/programs/058036617> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Cognitive Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/024731517> |
| 2 | Geographic Information Science M.G.I.S. | <https://umtc.catalog.prod.coursedog.com/programs/034937817> |
| 3 | Scientific and Technical Communication M.S. | <https://umtc.catalog.prod.coursedog.com/programs/089731517> |
| 4 | Statistics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/090031517> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/005660217> |
| 2 | Anthropology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/008060217> |
| 3 | Art History Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/010460217> |
| 4 | Asian and Middle Eastern Cultures and Media PhD | <https://umtc.catalog.prod.coursedog.com/programs/247560217> |
| 5 | Classical and Near Eastern Religions and Cultures Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/251960217> |
| 6 | Classical and Near Eastern Studies Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/118460217> |
| 7 | Cognitive Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/024760217> |
| 8 | Communication Studies Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/207460217> |
| 9 | Comparative Literature Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/019260217> |
| 10 | Comparative Studies in Discourse and Society Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/023160217> |
| 11 | Economics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/024860217> |
| 12 | English Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/027660217> |
| 13 | Feminist Studies Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/032960217> |
| 14 | French Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/033660217> |
| 15 | Geography Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/034860217> |
| 16 | Germanic Studies Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/136360217> |
| 17 | Hispanic and Lusophone Literatures, Cultures, and Linguistics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/216960217> |
| 18 | History Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/038060217> |
| 19 | Linguistics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/050460217> |
| 20 | Mass Communication Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/051660217> |
| 21 | Music Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/058060217> |
| 22 | Philosophy Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/065260217> |
| 23 | Political Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/071260217> |
| 24 | Psychology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/081260217> |
| 25 | Rhetoric, Scientific and Technical Communication Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/083160217> |
| 26 | Sociology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/086860217> |
| 27 | Speech-Language-Hearing Sciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/213660217> |
| 28 | Statistics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/090060217> |
| 29 | Theatre Arts Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/092060217> |

#### College of Pharmacy

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Laboratory Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/242831515> |
| 2 | Experimental and Clinical Pharmacology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/223631515> |
| 3 | Medical Laboratory Sciences MMLS | <https://umtc.catalog.prod.coursedog.com/programs/230830T15> |
| 4 | Medicinal Chemistry M.S. | <https://umtc.catalog.prod.coursedog.com/programs/054831515> |
| 5 | Pharmaceutics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/063631515> |
| 6 | Social and Administrative Pharmacy M.S. | <https://umtc.catalog.prod.coursedog.com/programs/085531515> |

##### OTD

| # | 项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy O.T.D. | <https://umtc.catalog.prod.coursedog.com/programs/239262415> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Experimental and Clinical Pharmacology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/223660215> |
| 2 | Medicinal Chemistry Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/054860215> |
| 3 | Pharmaceutics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/063660215> |
| 4 | Social and Administrative Pharmacy Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/085560215> |

##### PharmD

| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy Pharm D | <https://umtc.catalog.prod.coursedog.com/programs/064840315> |

#### College of Science and Engineering

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering and Mechanics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/214831507> |
| 2 | Astrophysics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/011631507> |
| 3 | Bioinformatics and Computational Biology M S | <https://umtc.catalog.prod.coursedog.com/programs/219331507> |
| 4 | Biomedical Engineering M.S. | <https://umtc.catalog.prod.coursedog.com/programs/013431507> |
| 5 | Chemical Engineering M.Ch.E. | <https://umtc.catalog.prod.coursedog.com/programs/016036107> |
| 6 | Chemical Engineering M.S.Ch.E. | <https://umtc.catalog.prod.coursedog.com/programs/016032007> |
| 7 | Chemical Physics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/016431507> |
| 8 | Chemistry M.S. | <https://umtc.catalog.prod.coursedog.com/programs/016831507> |
| 9 | Civil Engineering M.C.E. | <https://umtc.catalog.prod.coursedog.com/programs/018030707> |
| 10 | Civil Engineering M.S. | <https://umtc.catalog.prod.coursedog.com/programs/018031507> |
| 11 | Computer Science M.C.S. | <https://umtc.catalog.prod.coursedog.com/programs/019639507> |
| 12 | Computer Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/019631507> |
| 13 | Data Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/231331507> |
| 14 | Data Science for Chemical Engineering and Materials Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/249731507> |
| 15 | Earth Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/224431507> |
| 16 | Electrical and Computer Engineering MS.E.C.E. | <https://umtc.catalog.prod.coursedog.com/programs/027139107> |
| 17 | Financial Mathematics M.F.M. | <https://umtc.catalog.prod.coursedog.com/programs/216539907> |
| 18 | Geoengineering M.GeoE. | <https://umtc.catalog.prod.coursedog.com/programs/035231007> |
| 19 | Geoengineering M.S. | <https://umtc.catalog.prod.coursedog.com/programs/035231507> |
| 20 | Industrial and Systems Engineering M.S.I.SY.E. | <https://umtc.catalog.prod.coursedog.com/programs/214939607> |
| 21 | Management of Technology M.S.M.O.T. | <https://umtc.catalog.prod.coursedog.com/programs/055537307> |
| 22 | Materials Science and Engineering M.Mat.S.E. | <https://umtc.catalog.prod.coursedog.com/programs/052136807> |
| 23 | Materials Science and Engineering M.S.Mat.S.E. | <https://umtc.catalog.prod.coursedog.com/programs/052136907> |
| 24 | Mathematics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/052031507> |
| 25 | Mechanical Engineering M.S.M.E. | <https://umtc.catalog.prod.coursedog.com/programs/052832707> |
| 26 | Medical Device Innovation M.S. | <https://umtc.catalog.prod.coursedog.com/programs/230231507> |
| 27 | Physics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/067631507> |
| 28 | Robotics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/242931507> |
| 29 | Security Technologies M.S.S.T. | <https://umtc.catalog.prod.coursedog.com/programs/220130D07> |
| 30 | Software Engineering M.S.S.E. | <https://umtc.catalog.prod.coursedog.com/programs/104838107> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering and Mechanics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/214860207> |
| 2 | Astrophysics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/011660207> |
| 3 | Bioinformatics and Computational Biology Ph D | <https://umtc.catalog.prod.coursedog.com/programs/219360207> |
| 4 | Biomedical Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/013460207> |
| 5 | Chemical Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/016060207> |
| 6 | Chemical Physics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/016460207> |
| 7 | Chemistry Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/016860207> |
| 8 | Civil Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/018060207> |
| 9 | Computer Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/019660207> |
| 10 | Earth Sciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/224460207> |
| 11 | Electrical Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/026460207> |
| 12 | Industrial and Systems Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/214960207> |
| 13 | Materials Science and Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/052160207> |
| 14 | Mathematics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/052060207> |
| 15 | Mechanical Engineering Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/052860207> |
| 16 | Physics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/067660207> |

#### College of Veterinary Medicine

##### DVM

| # | 项目 | URL |
|---|------|-----|
| 1 | Veterinary Medicine D V M | <https://umtc.catalog.prod.coursedog.com/programs/094440503> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative and Molecular Biosciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/313531503> |
| 2 | Veterinary Medicine M.S. | <https://umtc.catalog.prod.coursedog.com/programs/094431503> |
| 3 | Veterinary Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/251231503> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative and Molecular Biosciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/313560203> |
| 2 | Veterinary Medicine Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/094460203> |
| 3 | Veterinary Sciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/251260203> |

#### Graduate School

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioethics M.A. | <https://umtc.catalog.prod.coursedog.com/programs/012730408> |
| 2 | History of Science, Technology, and Medicine M.A. | <https://umtc.catalog.prod.coursedog.com/programs/215930408> |

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Admin Master | <https://umtc.catalog.prod.coursedog.com/programs/0152MIM08> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry, Molecular Biology and Biophysics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/013531508> |
| 2 | Health Informatics M.H.I. | <https://umtc.catalog.prod.coursedog.com/programs/038339208> |
| 3 | Health Informatics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/038331508> |
| 4 | Integrated Bioscience M S | <https://umtc.catalog.prod.coursedog.com/programs/2380MIM08> |
| 5 | Molecular, Cellular, Developmental Biology and Genetics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/057131508> |
| 6 | Water Resources Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/097931508> |

##### MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work Master | <https://umtc.catalog.prod.coursedog.com/programs/0864MIM08> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry, Molecular Biology and Biophysics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/013560208> |
| 2 | Health Informatics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/038360208> |
| 3 | History of Science, Technology, and Medicine Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/215960208> |
| 4 | Integrated Biosciences Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/213860208> |
| 5 | Molecular, Cellular, Developmental Biology and Genetics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/057160208> |
| 6 | Water Resources Science PhD | <https://umtc.catalog.prod.coursedog.com/programs/097960208> |

#### Humphrey School of Public Affairs

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Human Rights M.H.R. | <https://umtc.catalog.prod.coursedog.com/programs/207830P16> |

##### MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Affairs M.P.A. | <https://umtc.catalog.prod.coursedog.com/programs/081838316> |

##### MPP

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy M.P.P. | <https://umtc.catalog.prod.coursedog.com/programs/177838216> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Development Practice M.D.P. | <https://umtc.catalog.prod.coursedog.com/programs/220930G16> |
| 2 | Science, Technology, and Environmental Policy M.S. | <https://umtc.catalog.prod.coursedog.com/programs/186731516> |

##### MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Urban and Regional Planning M.U.R.P. | <https://umtc.catalog.prod.coursedog.com/programs/192538416> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Affairs Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/081860216> |

#### Law School

##### JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Juridical Science S.J.D. | <https://umtc.catalog.prod.coursedog.com/programs/234062209> |
| 2 | Law J.D. | <https://umtc.catalog.prod.coursedog.com/programs/048440409> |

##### LLM

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Law LL.M. | <https://umtc.catalog.prod.coursedog.com/programs/227630L09> |
| 2 | Law LL.M. | <https://umtc.catalog.prod.coursedog.com/programs/048436509> |
| 3 | Patent Law LL.M. | <https://umtc.catalog.prod.coursedog.com/programs/230930L09> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science Patent Law | <https://umtc.catalog.prod.coursedog.com/programs/230930N09> |

#### Medical School

##### DPT

| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy D.P.T. | <https://umtc.catalog.prod.coursedog.com/programs/067261911> |

##### MD

| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine M D | <https://umtc.catalog.prod.coursedog.com/programs/055240211> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences M.S. | <https://umtc.catalog.prod.coursedog.com/programs/210031511> |
| 2 | Integrative Biology and Physiology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/221431511> |
| 3 | Medical Physics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/230431511> |
| 4 | Microbiology, Immunology, and Cancer Biology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/156631511> |
| 5 | Molecular Pharmacology and Therapeutics MS | <https://umtc.catalog.prod.coursedog.com/programs/248031511> |
| 6 | Neuroscience M.S. | <https://umtc.catalog.prod.coursedog.com/programs/059031511> |
| 7 | Rehabilitation Science M.S. | <https://umtc.catalog.prod.coursedog.com/programs/082331511> |
| 8 | Stem Cell Biology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/220031511> |
| 9 | Surgery M.S. Surg. | <https://umtc.catalog.prod.coursedog.com/programs/090834711> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Integrative Biology and Physiology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/221460211> |
| 2 | Medical Physics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/230460211> |
| 3 | Microbiology, Immunology, and Cancer Biology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/156660211> |
| 4 | Molecular Pharmacology and Therapeutics PhD | <https://umtc.catalog.prod.coursedog.com/programs/248060211> |
| 5 | Neuroscience Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/059060211> |
| 6 | Otolaryngology Ph.D. Otol. | <https://umtc.catalog.prod.coursedog.com/programs/062461611> |
| 7 | Rehabilitation Science Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/082360211> |

#### School of Dentistry

##### DDS

| # | 项目 | URL |
|---|------|-----|
| 1 | Dentistry D D S | <https://umtc.catalog.prod.coursedog.com/programs/022040104> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Hygiene M.S.D.H. | <https://umtc.catalog.prod.coursedog.com/programs/231030Q04> |
| 2 | Dental Therapy M D T | <https://umtc.catalog.prod.coursedog.com/programs/220230E04> |
| 3 | Dentistry M.S. | <https://umtc.catalog.prod.coursedog.com/programs/022031504> |
| 4 | Oral Biology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/061431504> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Oral Biology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/061460204> |

#### School of Nursing

##### DNP

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice D.N.P. | <https://umtc.catalog.prod.coursedog.com/programs/059662114> |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Integrative Health and Wellbeing Coaching M.A. | <https://umtc.catalog.prod.coursedog.com/programs/231530414> |

##### MN

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Nursing M.N. | <https://umtc.catalog.prod.coursedog.com/programs/059639814> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/059660214> |

#### School of Public Health

##### MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Community Health Promotion M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/017735220> |
| 2 | Environmental Health M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/028835220> |
| 3 | Epidemiology M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/029235220> |
| 4 | Maternal and Child Health M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/082735220> |
| 5 | Public Health Administration and Policy M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/081935220> |
| 6 | Public Health Data Science M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/247935220> |
| 7 | Public Health Nutrition M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/082535220> |
| 8 | Public Health Practice M.P.H. | <https://umtc.catalog.prod.coursedog.com/programs/203835220> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics M.S. | <https://umtc.catalog.prod.coursedog.com/programs/013831520> |
| 2 | Clinical Research M.S. | <https://umtc.catalog.prod.coursedog.com/programs/118531520> |
| 3 | Environmental Health M.S. | <https://umtc.catalog.prod.coursedog.com/programs/028831520> |
| 4 | Epidemiology M.S. | <https://umtc.catalog.prod.coursedog.com/programs/029231520> |
| 5 | Health Care Administration M.H.A. | <https://umtc.catalog.prod.coursedog.com/programs/044435120> |
| 6 | Health Services Research, Policy, and Administration M.S. | <https://umtc.catalog.prod.coursedog.com/programs/040531520> |
| 7 | Occupational Hygiene M.S. | <https://umtc.catalog.prod.coursedog.com/programs/251831520> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/013860220> |
| 2 | Environmental Health Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/028860220> |
| 3 | Epidemiology Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/029260220> |
| 4 | Health Services Research, Policy, and Administration Ph.D. | <https://umtc.catalog.prod.coursedog.com/programs/040560220> |
| 5 | Occupational Hygiene PhD | <https://umtc.catalog.prod.coursedog.com/programs/251860220> |

### 2.2 Graduate Certificates


#### Carlson School of Management

| # | Certificate | URL |
|---|------------|-----|
| 1 | Asset Management Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24465M602> |
| 2 | Business Analytics Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23005M402> |
| 3 | Closely-Held Business Taxation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24415L802> |
| 4 | Corporate Financial Management Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24475M702> |
| 5 | Entrepreneurship & Innovation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24705N902> |
| 6 | High Net-Worth Individual Taxation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24425L902> |
| 7 | International Taxation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24435M102> |
| 8 | Leadership for Managers Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24485M802> |
| 9 | Medical Industry Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24535N202> |
| 10 | Strategic Management Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24255M502> |
| 11 | Strategic Marketing Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24495M902> |
| 12 | Supply Chain Management for the Medical and Health Sector Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24545N302> |
| 13 | Tax Executive Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24445M202> |
| 14 | Taxation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24455M302> |

#### College of Continuing and Professional Studies

| # | Certificate | URL |
|---|------------|-----|
| 1 | Applied Business Certificate | <https://umtc.catalog.prod.coursedog.com/programs/009352918> |
| 2 | Construction Management Certificate | <https://umtc.catalog.prod.coursedog.com/programs/100653518> |
| 3 | Environmental Health and Safety Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24635N518> |
| 4 | Facility Management Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22805H218> |
| 5 | Healthcare Management Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23175J118> |
| 6 | Human Sexuality Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23795K618> |
| 7 | Information Technology Infrastructure Certificate | <https://umtc.catalog.prod.coursedog.com/programs/206752618> |
| 8 | Leadership for Science Professionals Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24525N118> |
| 9 | Long Term Care Management Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24585O218> |
| 10 | Regulatory Affairs for Food Professionals Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24865O618> |
| 11 | Sex Therapy Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24855O518> |
| 12 | Transgender & Gender Diverse Health Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24965P318> |

#### College of Design

| # | Certificate | URL |
|---|------------|-----|
| 1 | Advanced Wearable Products Post-Baccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23825K722> |
| 2 | Design Justice Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25035P722> |
| 3 | Metropolitan Design Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/211356122> |

#### College of Education and Human Development

| # | Certificate | URL |
|---|------------|-----|
| 1 | Additional Licensure Other | <https://umtc.catalog.prod.coursedog.com/programs/232600006> |
| 2 | Additional Licensure Teaching | <https://umtc.catalog.prod.coursedog.com/programs/204552006> |
| 3 | Adult Education Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/000355306> |
| 4 | Adult Education Undergraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/000357806> |
| 5 | Adult Literacy Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/212055606> |
| 6 | Advanced Practices in Second Language Teaching Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22085D106> |
| 7 | Autism Spectrum Disorder Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21305A706> |
| 8 | Autism Spectrum Disorder Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21305A806> |
| 9 | Clinical Physiology and Movement Science Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22385F306> |
| 10 | Disability Policy and Services Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/101451606> |
| 11 | Dual Language and Immersion Education Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/204651706> |
| 12 | Educational Psychology Specialist Certificate in Education and School Psychological Services | <https://umtc.catalog.prod.coursedog.com/programs/026051106> |
| 13 | Educational Psychology Specialist Certificate in Education and Special Education | <https://umtc.catalog.prod.coursedog.com/programs/026051306> |
| 14 | Human Resource Development Certificate | <https://umtc.catalog.prod.coursedog.com/programs/040259606> |
| 15 | Human Resource Development Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/040259706> |
| 16 | Infant and Early Childhood Mental Health Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21705C206> |
| 17 | K-12 Technology Integration Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/200158106> |
| 18 | Learning Analytics Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24905O906> |
| 19 | Learning Sciences Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24765O106> |
| 20 | Multimedia Design and Development Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/200258206> |
| 21 | Online Distance Learning Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21645B906> |
| 22 | PK-12 Administration Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/210255906> |
| 23 | Parent Education Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21805C306> |
| 24 | Private College Leadership Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23125I206> |
| 25 | Professional Development Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/151552106> |
| 26 | Program Evaluation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/202953206> |
| 27 | Sales Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24675N606> |
| 28 | Specialist in Education and General Education Administration Certificate | <https://umtc.catalog.prod.coursedog.com/programs/025650606> |
| 29 | Sports Coaching Certificate | <https://umtc.catalog.prod.coursedog.com/programs/018757506> |
| 30 | Talent Development and Gifted Education Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/204952306> |
| 31 | Teaching English as a Second Language Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21055C506> |
| 32 | Teaching Writing and Critical Literacy Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21555B606> |
| 33 | Undergraduate Multicultural Teaching and Learning Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22075C906> |

#### College of Liberal Arts

| # | Certificate | URL |
|---|------------|-----|
| 1 | Career Readiness Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23875K817> |
| 2 | Chinese Language Advanced-Level Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23365J217> |
| 3 | Editing and Publishing Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24315L717> |
| 4 | French Advanced-Level Proficiency Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23585J817> |
| 5 | German Advanced-Level Proficiency Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23595J917> |
| 6 | Music Education Post-Baccalaureate Licensure Certificate | <https://umtc.catalog.prod.coursedog.com/programs/05845K117> |
| 7 | Spanish Language Advanced-Level Proficiency Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23055I117> |
| 8 | Technical Communication Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/09135B817> |

#### College of Pharmacy

| # | Certificate | URL |
|---|------------|-----|
| 1 | Medical Laboratory Sciences Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23085J315> |

#### College of Science and Engineering

| # | Certificate | URL |
|---|------------|-----|
| 1 | Data Science Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23135K207> |
| 2 | Electrification Engineering Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25065Q107> |
| 3 | Fundamentals of Quantitative Finance Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22375F207> |
| 4 | Stream Restoration Science and Engineering Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21575B707> |
| 5 | Technology Leadership Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25135Q307> |

#### College of Veterinary Medicine

| # | Certificate | URL |
|---|------------|-----|
| 1 | Clinical Training | <https://umtc.catalog.prod.coursedog.com/programs/209855703> |
| 2 | Foreign Grad. Train. | <https://umtc.catalog.prod.coursedog.com/programs/209955803> |
| 3 | Poultry Health Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24685N803> |
| 4 | Swine Medicine | <https://umtc.catalog.prod.coursedog.com/programs/212256403> |
| 5 | Veterinary Medical Education | <https://umtc.catalog.prod.coursedog.com/programs/23725K503> |

#### Graduate School

| # | Certificate | URL |
|---|------------|-----|
| 1 | Clinical Ethics Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23165I308> |
| 2 | Health Care Design and Innovation Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22565G308> |

#### Humphrey School of Public Affairs

| # | Certificate | URL |
|---|------------|-----|
| 1 | Early Childhood Policy Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/21265A216> |
| 2 | Election Administration Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23395J416> |
| 3 | Election Administration Undergraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23395K316> |
| 4 | Human Services Leadership Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23565J616> |
| 5 | Nonprofit Management Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/210356016> |
| 6 | Policy Issues on Work and Pay Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/203458916> |
| 7 | Public Affairs Leadership Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22535G216> |

#### Medical School

| # | Certificate | URL |
|---|------------|-----|
| 1 | Orthoptics Post-baccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23035H911> |

#### School of Dentistry

| # | Certificate | URL |
|---|------------|-----|
| 1 | Endodontics | <https://umtc.catalog.prod.coursedog.com/programs/208554304> |
| 2 | Oral & Maxillofacial Surgery | <https://umtc.catalog.prod.coursedog.com/programs/209455504> |
| 3 | Oral Health Educator Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25045P804> |
| 4 | Oral Hlth. Serv. for Older Ads | <https://umtc.catalog.prod.coursedog.com/programs/208754504> |
| 5 | Orofacial Pain | <https://umtc.catalog.prod.coursedog.com/programs/208854604> |
| 6 | Orthodontics | <https://umtc.catalog.prod.coursedog.com/programs/209355404> |
| 7 | Pediatric Dentistry | <https://umtc.catalog.prod.coursedog.com/programs/209255104> |
| 8 | Periodontics | <https://umtc.catalog.prod.coursedog.com/programs/209155004> |
| 9 | Prosthodontics | <https://umtc.catalog.prod.coursedog.com/programs/209054904> |

#### School of Nursing

| # | Certificate | URL |
|---|------------|-----|
| 1 | Adult Gerontological Acute Care Nurse Practitioner Post-Graduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25105Q214> |
| 2 | Adult Health/Gerontological Clinical Nurse Specialist Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22215D714> |
| 3 | Adult/Gerontological Primary Care Nurse Practitioner Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22225D814> |
| 4 | Integrative Therapies & Healing Practices Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22435P114> |
| 5 | Leadership in Health Information Technology for Health Professionals Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22485F814> |
| 6 | Nurse Midwifery Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22275E414> |
| 7 | Pediatric Clinical Nurse Specialist Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22295E614> |
| 8 | Pediatric Nurse Practitioner - Acute Care Post-Graduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25005P414> |
| 9 | Pediatric Nurse Practitioner - Primary Care Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22305E714> |
| 10 | Population Health Informatics & Technology Post Baccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/25015P514> |
| 11 | Psychiatric Mental Health Nurse Practitioner Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22315E814> |
| 12 | Women's Health/Gender Related Nurse Practitioner Postgraduate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22235D914> |

#### School of Public Health

| # | Certificate | URL |
|---|------------|-----|
| 1 | Advanced Management Training for Clinician Leaders Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22835H520> |
| 2 | Aging Studies Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/00055C620> |
| 3 | American Indian Public Health and Wellness Post-Baccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24265L620> |
| 4 | Applied Biostatistics Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/22725G920> |
| 5 | Clinical Research Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/11855G720> |
| 6 | Global Health Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/23255I920> |
| 7 | Healthcare Management Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/24615N420> |
| 8 | Public Health Core Concepts Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/204151920> |
| 9 | Public Health Food Protection Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/208053820> |
| 10 | Public Health Postbaccalaureate Certificate in Performance Improvement | <https://umtc.catalog.prod.coursedog.com/programs/22495F920> |
| 11 | Public Health Preparedness, Response, and Recovery Postbaccalaureate Certificate | <https://umtc.catalog.prod.coursedog.com/programs/207953720> |

### 2.3 Graduate Admissions Model

UMN operates a **centralized Graduate School** with **decentralized program-level admissions**. The Graduate School sets minimum requirements (bachelor's degree, GPA 3.0+, English proficiency), but each program may have additional requirements (GRE, portfolio, writing samples, etc.).

- **Application portal**: Apply at the Graduate School website
- **Application fee**: $75 (US citizens/permanent residents), $95 (international)
- **Deadlines**: Vary by program; applicants should check with their program of interest
- **GRE**: May be required by individual programs

> Source: grad.umn.edu/admissions/application-instructions

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | Common App or Golden Gopher Application | admissions.tc.umn.edu |
| Application fee | $55 | admissions.tc.umn.edu |
| EA I Deadline | **November 1** | admissions.tc.umn.edu/admissions/freshman-admission |
| EA I Decision | By January 31 | admissions.tc.umn.edu |
| EA II Deadline | **December 1** | admissions.tc.umn.edu |
| EA II Decision | By February 15 | admissions.tc.umn.edu |
| RD Deadline | **January 1** | admissions.tc.umn.edu |
| RD Decision | By March 31 | admissions.tc.umn.edu |
| Enrollment confirmation | May 1 ($345 fee) | admissions.tc.umn.edu |
| SAT/ACT policy | **Test-optional through fall 2027** | admissions.tc.umn.edu |
| Recommendation letters | Not required | admissions.tc.umn.edu |
| Essay | Not required | admissions.tc.umn.edu |
| Self-reported academic record | Required | admissions.tc.umn.edu |

> **Note**: UMN is a **public university** and is **need-aware for all applicants** (domestic and international). Unlike private institutions, UMN does not offer need-blind admissions.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Writing Subscore | Notes |
|------|---------------|------------------|-------|
| TOEFL iBT | 4.5 (new scale) | 4.5 | UMN code: 6874; MyBest NOT accepted |
| IELTS Academic | 6.5 | 6.5 | |
| PTE Academic | 59 | 59 | |
| Cambridge C1 Advanced | 180 | 180 | |
| Duolingo | 120 | 120 | |

> **Scores effective starting Spring 2027 application period.** AZ hold scores (slightly lower): TOEFL 4.0, IELTS 6.0, PTE 50-58, Cambridge 170-179, DET 105-115.
> 
> **Exemptions**: Students from English-speaking countries, those who completed AP/A-level/IB English, or who scored 21+ on ACT English+Reading or 540+ on SAT EBRW.

> Source: admissions.tc.umn.edu/admissions/international-admission/english-proficiency-information

### 3.3 Graduate -- Global Rules

| Field | Value | Source |
|-------|-------|--------|
| Application portal | Graduate School online application | grad.umn.edu |
| Application fee (domestic) | $75 | grad.umn.edu/admissions/application-instructions/application-fees |
| Application fee (international) | $95 | grad.umn.edu |
| GRE | Per-program (some require, some optional) | grad.umn.edu |
| English proficiency | Required for non-native speakers | grad.umn.edu |
| GPA minimum | 3.0 (program-specific) | grad.umn.edu |
| Deadlines | Vary by program | grad.umn.edu |
| TOEFL/IELTS | Required for non-native English speakers | grad.umn.edu |

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year)

**Tuition (per semester, 13+ credits flat rate):**

| Category | Per Credit | Flat Rate (13+ credits) | Annual (2 semesters) |
|----------|-----------|------------------------|---------------------|
| Minnesota Resident | $644.00 | $8,372.00 | **$16,744.00** |
| Nonresident | $1,568.50 | $20,390.00 | **$40,780.00** |

> Note: Carlson School of Management and College of Science & Engineering have an additional $2,900/year in tuition.

**Cost of Attendance (2025-26, Resident, Living in Dorm):**

| Expense | Amount |
|---------|--------|
| Tuition and fees | $18,626.00 |
| Books, course materials, supplies | $1,000.00 |
| Housing and food | $14,672.00 |
| Transportation | $200.00 |
| Personal, misc. | $2,000.00 |
| Loan fees | $158.00 |
| **Total** | **$36,656.00** |

**Cost of Attendance (2025-26, Nonresident, Living in Dorm):**

| Expense | Amount |
|---------|--------|
| Tuition and fees | $41,512.00 |
| Books, course materials, supplies | $1,000.00 |
| Housing and food | $14,672.00 |
| Transportation | $1,700.00 |
| Personal, misc. | $2,000.00 |
| Loan fees | $158.00 |
| **Total** | **$61,042.00** |

> Source: onestop.umn.edu/finances/costs/cost-attendance and onestop.umn.edu/finances/tuition

### 4.2 Undergraduate Financial Aid Policy

- **U Promise Scholarship**: Guaranteed scholarship for eligible MN resident students meeting family income thresholds
- **Promise Plus Free Tuition Program**: Free tuition for eligible MN residents with family income below threshold
- **Merit scholarships**: Over $50 million awarded annually; automatic consideration with admission application
- **Need-aware**: UMN is need-aware for all applicants (domestic and international)
- **No-loan guarantee**: Not available (unlike some private institutions)
- **FAFSA**: Required for federal aid; available starting December

> Source: admissions.tc.umn.edu/cost-aid/scholarships

### 4.3 Graduate Cost & Funding Framework

**Graduate Tuition (2026-27, per semester):**

| Category | Per Credit | Full-time (6-14 credits) |
|----------|-----------|-------------------------|
| Resident | $1,827.00 | $10,962.00 |
| Nonresident | $2,894.00 | $17,364.00 |

**Funding**: Fellowships, research assistantships (RA), teaching assistantships (TA), grants, and loans are available. Most PhD programs offer full funding packages.

> Source: onestop.umn.edu/finances/tuition

---

## SECTION 5 -- Evidence Chain Index


```yaml
field: ug.deadlines.EA_I
value: November 1
source_url: https://admissions.tc.umn.edu/admissions/freshman-admission-university-minnesota-twin-cities
source_snippet: "November 1: Early Action I Deadline will receive an admission decision no later than January 31"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.deadlines.EA_II
value: December 1
source_url: https://admissions.tc.umn.edu/admissions/freshman-admission-university-minnesota-twin-cities
source_snippet: "December 1: Early Action II Deadline will receive an admission decision no later than February 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.deadlines.RD
value: January 1
source_url: https://admissions.tc.umn.edu/admissions/freshman-admission-university-minnesota-twin-cities
source_snippet: "January 1: Regular Deadline will receive an admission decision no later than March 31"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.app_fee
value: $55
source_url: https://admissions.tc.umn.edu/admissions/freshman-admission-university-minnesota-twin-cities
source_snippet: "an application, $55 application fee and self-reported academic record"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.test_policy
value: Test-optional through fall 2027
source_url: https://admissions.tc.umn.edu/admissions/freshman-admission-university-minnesota-twin-cities
source_snippet: "Freshman applicants through fall 2027 are not required to submit an ACT or SAT test score"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.english_proficiency.TOEFL
value: 4.5 (new scale)
source_url: https://admissions.tc.umn.edu/admissions/international-admission/english-proficiency-information
source_snippet: "TOEFL iBT: 4.5* (AZ: 4.0)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.english_proficiency.IELTS
value: 6.5
source_url: https://admissions.tc.umn.edu/admissions/international-admission/english-proficiency-information
source_snippet: "IELTS Academic: 6.5 (AZ: 6.0)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.english_proficiency.DET
value: 120
source_url: https://admissions.tc.umn.edu/admissions/international-admission/english-proficiency-information
source_snippet: "Duolingo: 120 (AZ: 105-115)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.tuition.resident
value: $16,744/year
source_url: https://onestop.umn.edu/finances/tuition
source_snippet: "Rate for full-time enrollment (13 credits or more) $8,372.00"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.tuition.nonresident
value: $40,780/year
source_url: https://onestop.umn.edu/finances/tuition
source_snippet: "Rate for full-time enrollment (13 credits or more) $20,390.00"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.coa.resident_dorm
value: $36,656
source_url: https://onestop.umn.edu/finances/costs/cost-attendance
source_snippet: "Total (fall and spring) $36,656.00"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: ug.coa.nonresident_dorm
value: $61,042
source_url: https://onestop.umn.edu/finances/costs/cost-attendance
source_snippet: "Total (fall and spring) $61,042.00"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: grad.app_fee.domestic
value: $75
source_url: https://grad.umn.edu/admissions/application-instructions/application-fees
source_snippet: "U.S. citizen/permanent resident ($75.00)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: grad.app_fee.international
value: $95
source_url: https://grad.umn.edu/admissions/application-instructions/application-fees
source_snippet: "International ($95.00)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: grad.tuition.resident
value: $10,962/semester
source_url: https://onestop.umn.edu/finances/tuition
source_snippet: "6-14 credits (full-time) $10,962.00"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: grad.tuition.nonresident
value: $17,364/semester
source_url: https://onestop.umn.edu/finances/tuition
source_snippet: "6-14 credits (full-time) $17,364.00"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: programs.total
value: 946
source_url: https://umtc.catalog.prod.coursedog.com/programs
source_snippet: "Coursedog API extraction"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: programs.ug_majors
value: 162
source_url: https://umtc.catalog.prod.coursedog.com/programs
source_snippet: "Coursedog API extraction"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: programs.grad_degrees
value: 302
source_url: https://umtc.catalog.prod.coursedog.com/programs
source_snippet: "Coursedog API extraction"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
umn-knowledge-base-v2
├── 00-overview (Section 0: counts, hierarchy, degree inventory, distribution matrix)
├── 01-ug-carlson (Section 1: Carlson School UG programs)
├── 02-ug-biology (Section 1: College of Biological Sciences UG programs)
├── 03-ug-design (Section 1: College of Design UG programs)
├── 04-ug-education (Section 1: College of Education and Human Development UG programs)
├── 05-ug-cfans (Section 1: CFANS UG programs)
├── 06-ug-cla (Section 1: College of Liberal Arts UG programs)
├── 07-ug-cse (Section 1: College of Science and Engineering UG programs)
├── 08-ug-nursing (Section 1: School of Nursing UG programs)
├── 09-grad-programs (Section 2: All graduate programs by college)
├── 10-grad-certificates (Section 2: Graduate certificates)
├── 11-deadlines (Section 3: Application requirements & deadlines)
├── 12-costs (Section 4: Costs & financial aid)
├── 13-evidence (Section 5: Evidence chain)
└── 14-comparison (Section 7: Cross-school comparison)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "umn-knowledge-base-v2"
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
| P0 | International student cost of attendance | onestop.umn.edu (specific international COA page) |
| P0 | U Promise Scholarship income thresholds | admissions.tc.umn.edu/cost-aid/scholarships/u-promise-scholarship |
| P1 | Per-program GRE requirements | grad.umn.edu (individual program pages) |
| P1 | Per-program graduate deadlines | grad.umn.edu (individual program pages) |
| P2 | Department-level detail for each college | Individual college websites |
| P2 | Honors Program requirements | honors.umn.edu |

---

## SECTION 7 -- Cross-School Comparison Framework

| Dimension | UMN Value | Notes |
|-----------|-----------|-------|
| Type | Public Research University | Big Ten, R1 |
| Location | Minneapolis, MN | Twin Cities campus |
| UG Tuition (resident) | $16,744/year | 2026-27 |
| UG Tuition (nonresident) | $40,780/year | 2026-27 |
| UG COA (resident, dorm) | $36,656/year | 2025-26 |
| UG COA (nonresident, dorm) | $61,042/year | 2025-26 |
| Need-blind? | No (need-aware for all) | Public university policy |
| Test policy | Test-optional through fall 2027 | |
| EA I Deadline | November 1 | |
| EA II Deadline | December 1 | |
| RD Deadline | January 1 | |
| TOEFL Minimum | 4.5 (new scale) | New 2026+ scoring |
| IELTS Minimum | 6.5 | |
| Application fee (UG) | $55 | |
| Application fee (Grad, domestic) | $75 | |
| Application fee (Grad, international) | $95 | |
| Total programs | 946 | From catalog |
| UG majors | 162 | |
| UG minors | 328 | |
| Grad degrees | 302 | |
| Grad certificates | 135 | |
| Colleges/schools | 19 | 17 with programs + Graduate School + professional schools |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.tc.umn.edu, grad.umn.edu, onestop.umn.edu, umtc.catalog.prod.coursedog.com
> **Verification**: ego-browser snapshotText + JS DOM extraction + Coursedog API
> **Granularity**: school -> department -> degree-level -> program
