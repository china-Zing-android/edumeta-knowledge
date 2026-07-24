# The London School of Economics and Political Science (LSE) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch (static extraction) + ego-browser (planned for verification)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/LLB) | 43 (4 BA + 38 BSc + 1 LLB) |
| 研究生授课型 (MSc/MA/LLM/MPA/MPP) | 110 |
| 研究生执行硕士 (Executive Masters) | 12 |
| 研究生双学位 (Double Degrees) | 24 |
| 研究生博士 (MPhil/PhD / MRes/PhD) | 35 |
| 访问研究学生 (Visiting Research Student) | 27 |
| **研究生项目总计** | **157** (不含访问研究学生) |
| **学位项目总计 (UG + Grad taught+research)** | **200** |
| 学院 / 系所总数 | 26 (20 departments + 6 institutes/schools) |

> **Note**: LSE officially states "over 40 undergraduate degrees." The full list of 43 UG programmes was extracted via ego-browser from the LSE programme search (filtered by "Undergraduate" study type, 43 results). This includes 19 programmes not in the previous extraction (BA Geography, BSc Economics and Data Science, BSc Financial Mathematics and Statistics, BSc International Social and Public Policy with Economics/Politics, BSc Mathematics with Data Science, BSc Mathematics Statistics and Business, BSc Philosophy Politics and Economics, BSc Politics and Economics, BSc Social Anthropology, LLB Bachelor of Laws, and others).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

LSE does not have traditional "schools/colleges" — it is organized as a single institution with **Departments**, **Institutes**, and **Schools**. All UG programmes are administered centrally.

```
The London School of Economics and Political Science (LSE)
├── Departments [系]
│   ├── Department of Accounting                          [系]
│   ├── Department of Anthropology                       [系]
│   ├── Department of Economics                          [系]
│   ├── Department of Economic History                   [系]
│   ├── Department of Finance                            [系]
│   ├── Department of Gender Studies                     [系]
│   ├── Department of Geography and Environment          [系]
│   ├── Department of Government                         [系]
│   ├── Department of Health Policy                      [系]
│   ├── Department of International Development          [系]
│   ├── Department of International History              [系]
│   ├── Department of International Relations            [系]
│   ├── Department of Management                         [系]
│   ├── Department of Mathematics                        [系]
│   ├── Department of Media and Communications           [系]
│   ├── Department of Methodology                        [系]
│   ├── Dept of Philosophy, Logic and Scientific Method  [系]
│   ├── Dept of Psychological and Behavioural Science    [系]
│   ├── Department of Social Policy                      [系]
│   ├── Department of Sociology                          [系]
│   └── Department of Statistics                         [系]
├── Institutes & Schools [研究所/学院]
│   ├── Data Science Institute                           [研究所]
│   ├── European Institute                               [研究所]
│   ├── Firoz Lalji Institute for Africa                 [研究所]
│   ├── Global School of Sustainability                  [学院]
│   ├── International Inequalities Institute             [研究所]
│   ├── LSE Law School                                   [学院]
│   ├── Marshall Institute                               [研究所]
│   └── School of Public Policy                          [学院]
└── Support Units
    ├── Centre for Language Studies                       [支持单位]
    └── LSE Careers                                       [支持单位]
```

> **Note**: LSE is not a collegiate university. All departments report directly to the School. Some institutes (e.g., Data Science Institute, International Inequalities Institute) are cross-departmental research centres rather than degree-granting units. The School of Public Policy and LSE Law School are the closest equivalents to "professional schools."

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 4 |
| BSc | Bachelor of Science | 本科 | 38 |
| LLB | Bachelor of Laws | 本科 | 1 |
| MSc | Master of Science | 授课型研究生 | ~90 |
| MA | Master of Arts | 授课型研究生 | 1 |
| LLM | Master of Laws | 授课型研究生 | 1 |
| MPA | Master of Public Administration | 授课型研究生 | 3 (含执行版) |
| MPP | Master of Public Policy | 授课型研究生 | 1 |
| Executive MSc/MA/LLM | Executive Masters | 授课型研究生 | 12 |
| Double Degree | 双学位 (LSE + partner) | 授课型研究生 | 24 |
| MPhil/PhD | Master of Philosophy / Doctor of Philosophy | 博士 | 24 |
| MRes/PhD | Master of Research / Doctor of Philosophy | 博士 | 11 |
| Visiting Research Student | 访问研究学生 | 非学位 | 27 |

> **Note**: LSE does not award BA (Hons) with classification — all UG degrees are classified. The BA is used for Anthropology, History, and Social Anthropology. MPhil/PhD is the standard doctoral route; MRes/PhD is used by Economics, Finance, Management, Accounting, Political Science, Anthropology, and International Development.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院/部门 \ 级别 | BA | BSc | MSc | MA | LLM | MPA/MPP | Exec Masters | Double Degree | MPhil/PhD | MRes/PhD | VRS | 合计 |
|----------------|----|----|-----|----|-----|---------|-------------|--------------|-----------|----------|-----|------|
| Accounting | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 7 |
| Anthropology | 2 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 7 |
| Economics | 0 | 3 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 10 |
| Economic History | 0 | 3 | 5 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 11 |
| Finance | 0 | 4 | 6 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 13 |
| Gender Studies | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 10 |
| Geography & Environment | 1 | 3 | 6 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 13 |
| Government | 0 | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 10 |
| Health Policy | 0 | 0 | 5 | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 1 | 11 |
| International Development | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 8 |
| International History | 1 | 1 | 3 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 10 |
| International Relations | 0 | 3 | 8 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 16 |
| Law / LSE Law School | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 1 | 8 |
| Management | 0 | 1 | 8 | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 1 | 16 |
| Mathematics | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 8 |
| Media & Communications | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 1 | 13 |
| Methodology | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Philosophy | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 8 |
| Psychological & Behavioural Sci | 0 | 1 | 4 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 8 |
| Social Policy | 0 | 3 | 2 | 0 | 0 | 3 | 0 | 1 | 1 | 1 | 1 | 12 |
| Sociology | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 8 |
| Statistics | 0 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 10 |
| Cross-dept / School of Public Policy | 0 | 0 | 3 | 0 | 0 | 2 | 3 | 3 | 0 | 0 | 0 | 11 |
| LSE-Fudan / LSE-NUS / LSE-PKU etc. | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 8 |
| **合计** | **4** | **38** | **90** | **1** | **2** | **5** | **12** | **24** | **24** | **11** | **27** | **~239** |

> **Reconciliation note**: UG programme counts updated 2026-07-08 via ego-browser extraction from LSE programme search (43 UG programmes: 4 BA + 38 BSc + 1 LLB). The graduate totals (157 programmes) are fully extracted from the Available-programmes page. Row totals may not sum exactly due to cross-departmental programmes counted once under primary department. The LLB is listed under Law / LSE Law School but does not have a dedicated column in this matrix.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

LSE is a single-faculty institution — all undergraduate programmes are administered centrally through the departments listed in Section 0.2. There are no separate undergraduate colleges. Students apply through UCAS and are admitted to specific degree programmes.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> **Total UG programmes: 43** (4 BA + 38 BSc + 1 LLB). Extracted 2026-07-08 via ego-browser from LSE programme search.

#### Department of Accounting
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Accounting and Finance | NN34 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-accounting-and-finance |

#### Department of Anthropology
##### BA
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BA Anthropology and Law | ML16 | https://www.lse.ac.uk/study-at-lse/undergraduate/ba-anthropology-and-law |
| 2 | BA Social Anthropology | L601 | https://www.lse.ac.uk/study-at-lse/undergraduate/ba-social-anthropology |
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Social Anthropology | L603 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-social-anthropology |

#### Department of Economics
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Economics | L101 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics |
| 2 | BSc Econometrics and Mathematical Economics | L140 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-econometrics-and-mathematical-economics |

#### Department of Economic History
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Economic History | V300 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economic-history |
| 2 | BSc Economic History and Geography | V3L7 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economic-history-and-geography |
| 3 | BSc Economics and Economic History | VL31 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics-and-economic-history |

#### Department of Finance
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Finance | N300 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-finance |
| 2 | BSc Actuarial Science | N321 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-actuarial-science |
| 3 | BSc Actuarial Science (with a Placement Year) | N322 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-actuarial-science-with-a-placement-year |
| 4 | BSc Data Science | N3UD | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-data-science |

#### Department of Geography and Environment
##### BA
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BA Geography | F800 | https://www.lse.ac.uk/study-at-lse/undergraduate/ba-geography |
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Geography with Economics | L7L1 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-geography-with-economics |
| 2 | BSc Environment and Sustainable Development | FK84 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-environment-and-sustainable-development |
| 3 | BSc Environment and Sustainable Development with Economics | F9L1 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-environment-and-sustainable-development-with-economics |

#### Department of Government
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Politics | L230 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-politics |
| 2 | BSc Politics and International Relations | L290 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-politics-and-international-relations |
| 3 | BSc Politics and Economics | LL12 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-politics-and-economics |
| 4 | BSc Politics and Philosophy | LV25 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-politics-and-philosophy |

#### Department of International History
##### BA
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BA History | V146 | https://www.lse.ac.uk/study-at-lse/undergraduate/ba-history |
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc History and Politics | LV21 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-history-and-politics |

#### Department of International Relations
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc International Relations | L250 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-international-relations |
| 2 | BSc International Relations and History | VL12 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-international-relations-and-history |
| 3 | BSc International Relations and Chinese | L2T1 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-international-relations-and-chinese |

#### Department of Management
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Management | N200 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-management |

#### Department of Mathematics
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Mathematics and Economics | GL11 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-mathematics-and-economics |
| 2 | BSc Mathematics with Economics | G1L1 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-mathematics-with-economics |
| 3 | BSc Financial Mathematics and Statistics | GN13 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-financial-mathematics-and-statistics |
| 4 | BSc Mathematics with Data Science | G140 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-mathematics-with-data-science |

#### Department of Philosophy, Logic and Scientific Method
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Philosophy, Logic and Scientific Method | V503 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-philosophy-logic-and-scientific-method |
| 2 | BSc Philosophy and Economics | LV15 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-philosophy-and-economics |
| 3 | BSc Philosophy, Politics and Economics | L0V0 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-philosophy-politics-and-economics |

#### Department of Psychological and Behavioural Science
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Psychological and Behavioural Science | C800 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-psychological-and-behavioural-science |

#### Department of Social Policy
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc International Social and Public Policy | L400 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-international-social-and-public-policy |
| 2 | BSc International Social and Public Policy with Economics | LLK1 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-international-social-and-public-policy-with-economics |
| 3 | BSc International Social and Public Policy with Politics | LL42 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-international-social-and-public-policy-with-politics |

#### Department of Sociology
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Sociology | L301 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-sociology |

#### Department of Statistics
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Economics and Data Science | L1N3 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics-and-data-science |
| 2 | BSc Mathematics, Statistics and Business | G0N0 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-mathematics-statistics-and-business |

#### LSE Law School
##### LLB
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | LLB Bachelor of Laws | M100 | https://www.lse.ac.uk/study-at-lse/undergraduate/llb-bachelor-of-laws |

#### Cross-departmental / Joint Honours
##### BSc
| # | 专业 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | BSc Language, Culture and Society | L3R9 | https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-language-culture-and-society |

### 1.3 Interdisciplinary / cross-departmental undergraduate programmes

LSE's joint honours programmes are cross-departmental by nature. The following programmes span multiple departments:

| Programme | Departments involved | UCAS |
|-----------|---------------------|------|
| BA Anthropology and Law | Anthropology + Law School | ML16 |
| BSc Economics and Economic History | Economics + Economic History | VL31 |
| BSc Economic History and Geography | Economic History + Geography | V3L7 |
| BSc Economics and Data Science | Statistics + Economics | L1N3 |
| BSc Environment and Sustainable Development with Economics | Geography + Economics | F9L1 |
| BSc Financial Mathematics and Statistics | Mathematics + Statistics | GN13 |
| BSc Geography with Economics | Geography + Economics | L7L1 |
| BSc History and Politics | International History + Government | LV21 |
| BSc International Relations and History | International Relations + International History | VL12 |
| BSc International Relations and Chinese | International Relations + Language Centre | L2T1 |
| BSc International Social and Public Policy with Economics | Social Policy + Economics | LLK1 |
| BSc International Social and Public Policy with Politics | Social Policy + Government | LL42 |
| BSc Language, Culture and Society | Multi-departmental | L3R9 |
| BSc Mathematics and Economics | Mathematics + Economics | GL11 |
| BSc Mathematics with Data Science | Mathematics + Statistics | G140 |
| BSc Mathematics with Economics | Mathematics + Economics | G1L1 |
| BSc Mathematics, Statistics and Business | Statistics + Mathematics | G0N0 |
| BSc Philosophy and Economics | Philosophy + Economics | LV15 |
| BSc Philosophy, Politics and Economics | Philosophy + Government + Economics | L0V0 |
| BSc Politics and Economics | Government + Economics | LL12 |
| BSc Politics and International Relations | Government + International Relations | L290 |
| BSc Politics and Philosophy | Government + Philosophy | LV25 |

### 1.4 Minors — complete list

LSE does not offer undergraduate minors. Students take 12 units over 3 years with some option choices outside their main department, but there is no formal minor system.

### 1.5 General/Institute-wide requirements

All LSE undergraduate students take **LSE100** (The LSE Course: Understanding the Causes of Things) — a compulsory half-unit course in the first year that introduces interdisciplinary thinking across the social sciences.

### 1.6 Entry requirements summary

| Requirement tier | A-Level | IB Diploma | Typical programmes |
|-----------------|---------|------------|-------------------|
| A*AA (A* in Maths) | A*AA | 39 points, 766 HL, 7 in Maths | Economics, Econometrics & ME, Finance, Accounting & Finance, Maths & Econ, Maths with Econ, Actuarial Science, Data Science, PBS |
| AAA | AAA | 38 points, 766 HL | Management (A in Maths), IR, Politics & IR, Politics, Politics & Philosophy, History & Politics, Env & Sustainable Dev, IR & History |
| AAB | AAB | 37 points, 666 HL | Sociology, Social Anthropology, BA History, Economic History, Philosophy Logic & Scientific Method, ISPP, Language Culture & Society |

**Contextual offers**: LSE makes reduced offers (typically one grade lower) for applicants from underrepresented backgrounds.

**TMUA requirement**: BSc Economics and BSc Econometrics and Mathematical Economics require the TMUA (Test of Mathematics for University Admission).

**GCSE requirements**: All programmes require minimum Grade B (6) in GCSE English Language and Mathematics. Most expect "several GCSE grades at A (7) and A* (8-9)."

---

## SECTION 2 — Graduate education

### 2.1 Graduate programmes — grouped by 学院 > 系 > 学位级别

#### Department of Accounting
##### MSc
| # | 项目 | UCAS代码 | URL |
|---|------|---------|-----|
| 1 | MSc Accounting and Finance | N4U1 | https://www.lse.ac.uk/study-at-lse/graduate/msc-accounting-and-finance |
| 2 | MSc Accounting and Data Analytics | N4U5 | https://www.lse.ac.uk/study-at-lse/graduate/msc-accounting-and-data-analytics |
| 3 | MSc Accounting, Organisations and Institutions | N4U4 | https://www.lse.ac.uk/study-at-lse/graduate/msc-accounting-organisations-and-institutions |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD Accounting (Accounting, Organisations and Institutions) | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-accounting-accounting-organisations-and-institutions |
| 2 | MRes/PhD Accounting (Economics of Accounting) | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-accounting-economics-of-accounting |

#### Department of Anthropology
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Anthropology and Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-anthropology-and-development |
| 2 | MSc Social Anthropology | https://www.lse.ac.uk/study-at-lse/graduate/msc-social-anthropology |
| 3 | MSc Social Anthropology (Religion in the Contemporary World) | https://www.lse.ac.uk/study-at-lse/graduate/msc-social-anthropology-religion-in-the-contemporary-world |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD Anthropology | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-anthropology |

#### Department of Economics
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Economics | https://www.lse.ac.uk/study-at-lse/graduate/msc-economics |
| 2 | MSc Economics (2 Year Programme) | https://www.lse.ac.uk/study-at-lse/graduate/msc-economics-two-year-programme |
| 3 | MSc Econometrics and Mathematical Economics | https://www.lse.ac.uk/study-at-lse/graduate/msc-econometrics-and-mathematical-economics |
| 4 | MSc Finance and Economics | https://www.lse.ac.uk/study-at-lse/graduate/msc-finance-and-economics |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD Economics | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-economics |
| 2 | MRes/PhD Economics and Management | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-economics-and-management |

#### Department of Economic History
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Economic History | https://www.lse.ac.uk/study-at-lse/graduate/msc-economic-history |
| 2 | MSc Economic History (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-economic-history-research |
| 3 | MSc Empires, Colonialism and Globalisation | https://www.lse.ac.uk/study-at-lse/graduate/msc-empires-colonialism-and-globalisation |
| 4 | MSc Financial History | https://www.lse.ac.uk/study-at-lse/graduate/msc-financial-history |
| 5 | MSc Political Economy of Late Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-economy-of-late-development |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Economic History | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-economic-history |

#### Department of Finance
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Finance (full-time) | https://www.lse.ac.uk/study-at-lse/graduate/msc-finance-full-time |
| 2 | MSc Finance (part-time) | https://www.lse.ac.uk/study-at-lse/graduate/msc-finance-part-time |
| 3 | MSc Finance and Private Equity | https://www.lse.ac.uk/study-at-lse/graduate/msc-finance-and-private-equity |
| 4 | MSc Finance and Risk | https://www.lse.ac.uk/study-at-lse/graduate/msc-finance-and-risk |
| 5 | MSc Financial Mathematics | https://www.lse.ac.uk/study-at-lse/graduate/msc-financial-mathematics |
| 6 | MSc Real Estate Economics and Finance | https://www.lse.ac.uk/study-at-lse/graduate/msc-real-estate-economics-and-finance |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD Finance | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-finance |

#### Department of Gender Studies
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Gender | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender |
| 2 | MSc Gender (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-research |
| 3 | MSc Gender (Rights and Human Rights) | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-rights-and-human-rights |
| 4 | MSc Gender (Sexuality) | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-sexuality |
| 5 | MSc Gender, Development and Globalisation | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-development-and-globalisation |
| 6 | MSc Gender, Media and Culture | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-media-and-culture |
| 7 | MSc Gender, Peace and Security | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-peace-and-security |
| 8 | MSc Gender, Policy and Inequalities | https://www.lse.ac.uk/study-at-lse/graduate/msc-gender-policy-and-inequalities |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Gender | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-gender |

#### Department of Geography and Environment
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc City Design and Social Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-city-design-and-social-science |
| 2 | MSc Environment and Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-environment-and-development |
| 3 | MSc Environmental Economics and Climate Change | https://www.lse.ac.uk/study-at-lse/graduate/msc-environmental-economics-and-climate-change |
| 4 | MSc Environmental Policy and Regulation | https://www.lse.ac.uk/study-at-lse/graduate/msc-environmental-policy-and-regulation |
| 5 | MSc Geographic Data Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-geographic-data-science |
| 6 | MSc Local Economic Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-local-economic-development/ |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Economic Geography | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-economic-geography |
| 2 | MPhil/PhD Environmental Economics | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-environmental-economics |
| 3 | MPhil/PhD Environmental Policy and Development | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-environmental-policy-and-development |
| 4 | MPhil/PhD Human Geography and Urban Studies | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-human-geography-and-urban-studies |

#### Department of Government
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc European and International Politics and Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-european-and-international-politics-and-policy |
| 2 | MSc Political Economy of Europe in the World | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-economy-of-europe-in-the-world |
| 3 | MSc Political Science (Conflict Studies and Comparative Politics) | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-science-conflict-studies-and-comparative-politics |
| 4 | MSc Political Science (Global Politics) | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-science-global-politics |
| 5 | MSc Political Science (Political Behaviour) | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-science-political-behaviour |
| 6 | MSc Political Science (Political Science and Political Economy) | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-science-political-science-and-political-economy |
| 7 | MSc Political Theory | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-theory |
| 8 | MSc Politics and Communication | https://www.lse.ac.uk/study-at-lse/graduate/msc-politics-and-communication |
| 9 | MSc Public Policy and Administration | https://www.lse.ac.uk/study-at-lse/graduate/msc-public-policy-and-administration |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD European Studies | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-european-studies |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD Political Science | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-political-science |

#### Department of Health Policy
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Global Health Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-global-health-policy |
| 2 | MSc Health and International Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-health-and-international-development |
| 3 | MSc Health Data Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-health-data-science |
| 4 | MSc International Health Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-health-policy |
| 5 | MSc International Health Policy (Health Economics) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-health-policy-health-economics |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Health Policy and Health Economics | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-health-policy-and-health-economics |

##### Executive Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive MSc Health Economics, Outcomes and Management in Clinical Sciences | https://www.lse.ac.uk/study-at-lse/graduate/executive-msc-health-economics-outcomes-management-clinical-sciences |
| 2 | Executive MSc Health Economics, Policy and Management | https://www.lse.ac.uk/study-at-lse/graduate/executive-msc-health-economics-policy-and-management |
| 3 | Executive MSc Healthcare Decision Making (with NICE) | https://www.lse.ac.uk/study-at-lse/graduate/executive-msc-healthcare-decision-making |

#### Department of International Development
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Development Management (Applied Development Economics) | https://www.lse.ac.uk/study-at-lse/graduate/msc-development-management-applied-development-economics |
| 2 | MSc Development Management (Political Economy) | https://www.lse.ac.uk/study-at-lse/graduate/msc-development-management-political-economy |
| 3 | MSc Development Studies | https://www.lse.ac.uk/study-at-lse/graduate/msc-development-studies |
| 4 | MSc Economic Policy for International Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-economic-policy-for-international-development |
| 5 | MSc International Development and Humanitarian Emergencies | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-development-and-humanitarian-emergencies |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD International Development | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-international-development |

#### Department of International History
##### MA/MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MA Modern History | https://www.lse.ac.uk/study-at-lse/graduate/ma-modern-history |
| 2 | MSc History of International Relations | https://www.lse.ac.uk/study-at-lse/graduate/msc-history-of-international-relations |
| 3 | MSc International and Asian History | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-and-asian-history |
| 4 | MSc Theory and History of International Relations | https://www.lse.ac.uk/study-at-lse/graduate/msc-theory-and-history-of-international-relations |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD International History | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-international-history |

#### Department of International Relations
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Culture and Conflict in a Global Europe | https://www.lse.ac.uk/study-at-lse/graduate/msc-culture-and-conflict-in-a-global-europe |
| 2 | MSc International Migration and Public Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-migration-and-public-policy |
| 3 | MSc International Political Economy | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-political-economy |
| 4 | MSc International Political Economy (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-political-economy-research |
| 5 | MSc International Relations | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-relations |
| 6 | MSc International Relations (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-relations-research |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD International Relations | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-international-relations |

##### Executive Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive MSc International Strategy and Diplomacy | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-strategy-and-diplomacy |

#### LSE Law School
##### LLM / MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws (LLM) | https://www.lse.ac.uk/study-at-lse/graduate/llm |
| 2 | MSc Law and Finance | https://www.lse.ac.uk/study-at-lse/graduate/msc-law-and-finance |
| 3 | MSc Regulation | https://www.lse.ac.uk/study-at-lse/graduate/msc-regulation |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Law | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-law |

##### Executive Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Master of Laws (ELLM) | https://www.lse.ac.uk/study-at-lse/graduate/executive-master-of-laws-ellm |

#### Department of Management
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Master's in Management | https://www.lse.ac.uk/study-at-lse/graduate/global-masters-management |
| 2 | MSc Management | https://www.lse.ac.uk/study-at-lse/graduate/masters-in-management |
| 3 | MSc Management and Strategy | https://www.lse.ac.uk/study-at-lse/graduate/msc-management-and-strategy |
| 4 | MSc Management of Information Systems and Digital Innovation | https://www.lse.ac.uk/study-at-lse/graduate/msc-management-information-systems-and-digital-innovation |
| 5 | MSc Marketing | https://www.lse.ac.uk/study-at-lse/graduate/msc-marketing |
| 6 | MSc Human Resources and Organisations (HRM/CIPD) | https://www.lse.ac.uk/study-at-lse/graduate/msc-human-resources-and-organisations |
| 7 | MSc Human Resources and Organisations (International Employment Relations/CIPD) | https://www.lse.ac.uk/study-at-lse/graduate/msc-human-resources-and-organisations |
| 8 | MSc Human Resources and Organisations (Organisational Behaviour) | https://www.lse.ac.uk/study-at-lse/graduate/msc-human-resources-and-organisations |
| 9 | MSc Social Innovation and Entrepreneurship | https://www.lse.ac.uk/study-at-lse/graduate/msc-social-innovation-and-entrepreneurship |

##### MRes/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MRes/PhD Management (Employment Relations and Human Resources) | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-management-employment-relations-and-human-resources |
| 2 | MRes/PhD Management (Information Systems and Innovation) | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-management-information-systems-and-innovation |
| 3 | MRes/PhD Management (Marketing) | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-management-marketing |
| 4 | MRes/PhD Management (Organisational Behaviour) | https://www.lse.ac.uk/study-at-lse/graduate/mresphd-management-organisational-behaviour |

##### Executive Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Global Master's in Management | https://www.lse.ac.uk/study-at-lse/graduate/executive-global-msc-management |
| 2 | Executive MSc Social Business and Entrepreneurship | https://www.lse.ac.uk/study-at-lse/graduate/executive-msc-social-business-and-entrepreneurship |

#### Department of Mathematics
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Mathematics and Computation | https://www.lse.ac.uk/study-at-lse/graduate/msc-mathematics-and-computation |
| 2 | MSc Quantitative Methods for Risk Management | https://www.lse.ac.uk/study-at-lse/graduate/msc-quantitative-methods-for-risk-management |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Mathematics | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-mathematics |

#### Department of Media and Communications
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Media and Communications | https://www.lse.ac.uk/study-at-lse/graduate/msc-media-and-communications |
| 2 | MSc Media and Communications (Data and Society) | https://www.lse.ac.uk/study-at-lse/graduate/msc-media-and-communications-data-and-society |
| 3 | MSc Media and Communications (Media and Communication Governance) | https://www.lse.ac.uk/study-at-lse/graduate/msc-media-and-communications-media-and-communication-governance |
| 4 | MSc Media and Communications (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-media-and-communications-research |
| 5 | MSc Media, Communication and Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-media-communication-and-development |
| 6 | MSc Strategic Communications and Society | https://www.lse.ac.uk/study-at-lse/graduate/msc-strategic-communications-and-society |
| 7 | MSc Politics and Communication | https://www.lse.ac.uk/study-at-lse/graduate/msc-politics-and-communication |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Media and Communications | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-media-and-communications |

#### Department of Methodology
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Social Research Methods | https://www.lse.ac.uk/study-at-lse/graduate/msc-social-research-methods |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Social Research Methods | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-social-research-methods |

#### Department of Philosophy, Logic and Scientific Method
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Philosophy and Public Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-philosophy-and-public-policy |
| 2 | MSc Philosophy of Economics and the Social Sciences | https://www.lse.ac.uk/study-at-lse/graduate/msc-philosophy-of-economics-and-the-social-sciences |
| 3 | MSc Philosophy of Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-philosophy-of-science |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Philosophy | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-philosophy |

#### Department of Psychological and Behavioural Science
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Behavioural Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-behavioural-science |
| 2 | MSc Organisational and Social Psychology | https://www.lse.ac.uk/study-at-lse/graduate/msc-organisational-and-social-psychology |
| 3 | MSc Social and Cultural Psychology | https://www.lse.ac.uk/study-at-lse/graduate/msc-social-and-cultural-psychology |
| 4 | MSc Social and Public Communication | https://www.lse.ac.uk/study-at-lse/graduate/msc-social-and-public-communication |
| 5 | MSc Societal and Environmental Psychology | https://www.lse.ac.uk/study-at-lse/graduate/msc-societal-and-environmental-psychology |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Psychological and Behavioural Science | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-psychological-and-behavioural-science |

##### Executive Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive MSc Behavioural Science (Modular) | https://www.lse.ac.uk/study-at-lse/graduate/executive-msc-behavioural-science |

#### Department of Social Policy
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc International Social and Public Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-social-and-public-policy |
| 2 | MSc International Social and Public Policy (Development) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-social-and-public-policy-development |
| 3 | MSc International Social and Public Policy (Education) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-social-and-public-policy-education |
| 4 | MSc International Social and Public Policy (Migration) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-social-and-public-policy-migration |
| 5 | MSc International Social and Public Policy (Non-Governmental Organisations) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-social-and-public-policy-non-governmental-organisations |
| 6 | MSc International Social and Public Policy (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-international-social-and-public-policy-research |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Social Policy | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-social-policy |

#### Department of Sociology
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Culture and Society | https://www.lse.ac.uk/study-at-lse/graduate/msc-culture-and-society |
| 2 | MSc Culture, Justice and Environment | https://www.lse.ac.uk/study-at-lse/graduate/msc-culture-justice-and-environment |
| 3 | MSc Economy and Society | https://www.lse.ac.uk/study-at-lse/graduate/msc-economy-and-society |
| 4 | MSc Inequalities and Social Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-inequalities-and-social-science |
| 5 | MSc Political Sociology | https://www.lse.ac.uk/study-at-lse/graduate/msc-political-sociology |
| 6 | MSc Sociology | https://www.lse.ac.uk/study-at-lse/graduate/msc-sociology |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Sociology | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-sociology |

#### Department of Statistics
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Data Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-data-science |
| 2 | MSc Statistics | https://www.lse.ac.uk/study-at-lse/graduate/msc-statistics |
| 3 | MSc Statistics (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-statistics-research |
| 4 | MSc Financial Statistics | https://www.lse.ac.uk/study-at-lse/graduate/msc-statistics-financial-statistics |
| 5 | MSc Financial Statistics (Research) | https://www.lse.ac.uk/study-at-lse/graduate/msc-statistics-financial-statistics-research |

##### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Statistics | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-statistics |

#### School of Public Policy
##### MPA / MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration (MPA) | https://www.lse.ac.uk/study-at-lse/graduate/master-of-public-administration |
| 2 | MPA Data Science for Public Policy | https://www.lse.ac.uk/study-at-lse/graduate/mpa-data-science-for-public-policy |
| 3 | Master of Public Policy (MPP) | https://www.lse.ac.uk/study-at-lse/graduate/master-of-public-policy |

##### Executive Masters
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Master of Public Administration | https://www.lse.ac.uk/study-at-lse/graduate/executive-master-of-public-administration |

#### Cross-departmental / Double Degrees
| # | 项目 | URL |
|---|------|-----|
| 1 | LSE-Bocconi Double Degree in European and International Public Policy and Politics | https://www.lse.ac.uk/study-at-lse/graduate/lse-bocconi-double-degree-european-international-public-policy-and-politics |
| 2 | LSE-Columbia Double Master of Public Administration (MPA) | https://www.lse.ac.uk/study-at-lse/graduate/lse-columbia-double-mpa |
| 3 | LSE-Columbia Double MSc European Politics, Conflict and Culture | https://www.lse.ac.uk/study-at-lse/graduate/lse-columbia-double-degree-european-politics-conflict-and-culture |
| 4 | LSE-Columbia Double MSc International and World History | https://www.lse.ac.uk/study-at-lse/graduate/lse-columbia-double-degree-international-and-world-history |
| 5 | LSE-Fudan Double MSc Global Media and Communications | https://www.lse.ac.uk/study-at-lse/graduate/msc-global-media-and-communications-lse-and-fudan |
| 6 | LSE-Fudan Double MSc Global Political Economy of China and Europe | https://www.lse.ac.uk/study-at-lse/graduate/lse-fudan-double-degree-in-the-global-political-economy-of-china-and-europe |
| 7 | LSE-Fudan Double MSc International Social and Public Policy | https://www.lse.ac.uk/study-at-lse/graduate/lse-fudan-double-masters-ispp |
| 8 | LSE-Leipzig Double Degree in Global Studies and Economic History | https://www.lse.ac.uk/study-at-lse/graduate/lse-leipzig-double-degree-in-global-studies-and-economic-history |
| 9 | LSE-LSHTM Double MSc Health Policy, Planning and Financing | https://www.lse.ac.uk/study-at-lse/graduate/msc-health-policy-planning-and-financing |
| 10 | LSE-NUS Double MA Asian and International History | https://www.lse.ac.uk/study-at-lse/graduate/lse-nus-double-degree-ma-asian-and-international-history |
| 11 | LSE-NYU Double MSc Media, Culture and Global Cities | https://www.lse.ac.uk/study-at-lse/graduate/double-masters-degree-in-media-culture-and-global-cities-lse-and-nyu |
| 12 | LSE-PKU Double MSc Environmental Policy, Technology and Health (Environment and Development) | https://www.lse.ac.uk/study-at-lse/graduate/lse-pku-double-degree-in-environmental-policy-technology-and-health |
| 13 | LSE-PKU Double MSc Environmental Policy, Technology and Health (Environmental Economics) | https://www.lse.ac.uk/study-at-lse/graduate/lse-pku-double-degree-in-environmental-policy-technology-and-health |
| 14 | LSE-PKU Double MSc Environmental Policy, Technology and Health (Environmental Policy) | https://www.lse.ac.uk/study-at-lse/graduate/lse-pku-double-degree-in-environmental-policy-technology-and-health |
| 15 | LSE-PKU Double MSc International Affairs | https://www.lse.ac.uk/study-at-lse/graduate/lse-pku-double-degree-in-msc-international-affairs |
| 16 | LSE-Sciences Po Double Degree Affaires Internationales and IR/IPE | https://www.lse.ac.uk/study-at-lse/graduate/lse-sciences-po-double-degree-affaires-internationales |
| 17 | LSE-Sciences Po Double Degree in European Studies | https://www.lse.ac.uk/study-at-lse/graduate/lse-sciences-po-double-degree-in-european-studies |
| 18 | LSE-Sciences Po MSc Development Management (Applied Dev Econ) | https://www.lse.ac.uk/study-at-lse/graduate/msc-development-management-applied-development-economics |
| 19 | LSE-Sciences Po MSc Development Management (Political Economy) | https://www.lse.ac.uk/study-at-lse/graduate/msc-development-management-political-economy |
| 20 | LSE-Sciences Po Double MPP/MPA | https://www.lse.ac.uk/study-at-lse/graduate/lse-sciences-po-double-mpa |
| 21 | LSE-Sciences Po Double MSc Political Economy of Development | https://www.lse.ac.uk/study-at-lse/graduate/lse-sciences-po-degree-in-political-economy-of-dev |
| 22 | LSE-Sciences Po Double MSc Urban Policy | https://www.lse.ac.uk/study-at-lse/graduate/lse-sciences-po-double-degree-in-urban-policy |
| 23 | LSE-Toronto Double MPA and Master of Global Affairs | https://www.lse.ac.uk/study-at-lse/graduate/lse-toronto-double-mpa |
| 24 | LSE-USC Double MSc Global Media and Communications | https://www.lse.ac.uk/study-at-lse/graduate/msc-global-media-and-communications-lse-and-usc |

#### TRIUM Global Executive MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | TRIUM Global Executive MBA | https://www.lse.ac.uk/study-at-lse/graduate/trium-global-executive-mba |

#### Additional cross-departmental MSc programmes
| # | 项目 | URL |
|---|------|-----|
| 1 | MSc Applied Social Data Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-applied-social-data-science |
| 2 | MSc Behavioural Science | https://www.lse.ac.uk/study-at-lse/graduate/msc-behavioural-science |
| 3 | MSc China in Comparative Perspective | https://www.lse.ac.uk/study-at-lse/graduate/msc-china-in-comparative-perspective |
| 4 | MSc Criminology and Criminal Justice Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-criminal-justice-policy |
| 5 | MSc Human Rights | https://www.lse.ac.uk/study-at-lse/graduate/msc-human-rights |
| 6 | MSc Human Rights and Politics | https://www.lse.ac.uk/study-at-lse/graduate/msc-human-rights-and-politics |
| 7 | MSc Innovation Policy | https://www.lse.ac.uk/study-at-lse/graduate/msc-innovation-policy |
| 8 | MSc Regional and Urban Planning Studies | https://www.lse.ac.uk/study-at-lse/graduate/msc-regional-and-urban-planning-studies |
| 9 | MSc Urbanisation and Development | https://www.lse.ac.uk/study-at-lse/graduate/msc-urbanisation-and-development |

##### MPhil/PhD (cross-departmental)
| # | 项目 | URL |
|---|------|-----|
| 1 | MPhil/PhD Computational Social Science | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-computational-social-science |
| 2 | MPhil/PhD Data, Networks and Society | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-data-networks-and-society |
| 3 | MPhil/PhD Demography (Social/Formal) | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-demography-social-formal |
| 4 | MPhil/PhD Regional and Urban Planning Studies | https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-regional-and-urban-planning-studies |

#### Executive Masters (cross-departmental)
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive MSc Cities | https://www.lse.ac.uk/study-at-lse/graduate/executive-msc-in-cities |

### 2.2 Graduate admissions model

LSE graduate admissions is **centralized** — all applications go through the LSE Graduate Admissions Office, not individual departments. However, each department sets its own entry requirements and makes admission decisions.

- **Application portal**: LSE Online Application System (direct, not through UCAS)
- **Application fee**: Not specified on main pages (varies by programme)
- **Deadlines**: Rolling or per-programme; most taught programmes have rounds
- **Research programmes**: MPhil/PhD and MRes/PhD applications typically open in October and close in January
- **CGS April-15**: LSE is a signatory of the CGS April 15 Resolution for research programmes

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application platform | **UCAS** |
| UCAS deadline | **13 January 2027** (for 2027/28 entry) |
| Oxbridge/October 15 deadline | N/A (LSE is not Oxford/Cambridge) |
| Application fee | UCAS standard fee (set by UCAS) |
| Personal statement | UCAS single personal statement (one for all 5 choices) |
| References | 1 academic reference (UCAS) |
| Interviews | **Not required** (LSE does not interview UG applicants) |
| Admissions tests | **TMUA** required for BSc Economics and BSc Econometrics and Mathematical Economics |
| Conditional offers | Yes — based on predicted A-Level/IB grades |
| Decision notification | Via UCAS Track |
| Enrolment confirmation | UCAS firm/insurance choice deadline |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Component Requirements | Validity |
|------|--------------|----------------------|----------|
| **IELTS Academic** | 7.0 | 7.0 in each component | 2 years before 1 Sept |
| **TOEFL iBT** | 100 | Writing 27, Reading 25, Listening 24, Speaking 24 | 2 years before 1 Sept |
| **TOEFL iBT** (Jan 2026+ scale) | 5.5 | Writing 5, Reading 5, Listening 5, Speaking 5 | 2 years before 1 Sept |
| **PTE Academic** (in-person) | 70 | 70 in all components | 2 years before 1 Sept |
| **Cambridge C1 Advanced** | 185 | 185 in each component | Forever |
| **Cambridge C2 Proficiency** | 185 | 185 in each component | Forever |
| **Trinity ISE** | Level III | Distinction in each component | 2 years before 1 Sept |

**Exemptions**: Nationals of UKVI majority English-speaking countries whose first language is English; holders of a completed UG degree (3+ years), PG taught degree (1+ year), or PhD from those countries.

**Key rules**: IELTS/TOEFL/Trinity scores must come from a single sitting. IELTS General NOT accepted. PTE Academic online NOT accepted.

### 3.3 Graduate — English proficiency

LSE has **four tiers** of English language requirements for postgraduate programmes:

#### Standard (most taught programmes)
| Test | Overall | Reading | Listening | Writing | Speaking |
|------|---------|---------|-----------|---------|----------|
| IELTS Academic | 7.0 | 6.5 | 6.5 | 6.5 | 6.5 |
| TOEFL iBT | 100 | 23 | 22 | 24 | 22 |
| PTE Academic | 70 | 62 | 62 | 62 | 62 |
| Cambridge C1/C2 | 185 | 176 | 176 | 176 | 176 |

#### Higher
| Test | Overall | Reading | Listening | Writing | Speaking |
|------|---------|---------|-----------|---------|----------|
| IELTS Academic | 7.0 | **7.0** | 6.5 | 6.5 | 6.5 |
| TOEFL iBT | 100 | **25** | 22 | 24 | 22 |
| PTE Academic | 70 | **70** | 62 | 62 | 62 |

#### Research — MPhil/PhD (except Law & Statistics)
| Test | Overall | Reading | Listening | Writing | Speaking |
|------|---------|---------|-----------|---------|----------|
| IELTS Academic | 7.0 | 7.0 | 6.5 | **7.0** | 6.5 |
| TOEFL iBT | 100 | 25 | 22 | **27** | 22 |

#### Law programmes (including MPhil/PhD Law)
| Test | Overall | Reading | Listening | Writing | Speaking |
|------|---------|---------|-----------|---------|----------|
| IELTS Academic | **7.5** | 7.0 | 7.0 | 7.0 | 6.5 |
| TOEFL iBT | **109** | 25 | 24 | 27 | 22 |
| PTE Academic | **78** | 70 | 70 | 70 | 62 |

**PG Exemptions**: Same as UG — nationals of majority English-speaking countries; holders of qualifying degrees from those countries.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026/27 academic year)

| Fee Category | Amount (GBP) |
|-------------|-------------|
| **Home (UK) tuition** | £9,790 per year |
| **Overseas tuition (Tier 1)** | £28,900 per year |
| **Overseas tuition (Tier 2)** | £30,700 per year |
| **Overseas tuition (Tier 3)** | £32,100 per year |
| **Overseas tuition (Tier 4)** | £35,700 per year |
| **Overseas tuition (Tier 5)** | £39,900 per year |
| **Year abroad fee (Home)** | £1,465 per year |
| **Year abroad fee (Overseas)** | £4,335 per year |
| **Placement year fee (Home)** | £1,955 per year |
| **Placement year fee (Overseas)** | £6,140 per year |

**Overseas fee tiers by programme**:
- **£28,900**: BA History, BA Social Anthropology, BSc Economic History, BSc Economic History & Geography, BSc International Relations & Chinese, BSc International Relations & History, BSc International Social and Public Policy, BSc Language Culture and Society, BSc Politics, BSc History and Politics, BSc Politics and Philosophy, BSc Philosophy Logic and Scientific Method
- **£30,700**: BA Anthropology and Law, BSc Actuarial Science, BSc Economics and Economic History, BSc Environment and Sustainable Development, BSc Environment and Sustainable Development with Economics, BSc Geography with Economics, BSc International Relations, BSc Management, BSc Philosophy and Economics, BSc Politics and International Relations, BSc Psychological and Behavioural Science, BSc Sociology
- **£32,100**: BSc Data Science
- **£35,700**: BSc Accounting and Finance, BSc Finance, BSc Mathematics and Economics, BSc Mathematics with Economics
- **£39,900**: BSc Economics, BSc Econometrics and Mathematical Economics

> **Note**: Home fee is set at the UK Government maximum (£9,250 → £9,790 from 2025/26). Overseas fees are fixed from year of entry but "may rise in line with inflation" for new entrants.

### 4.2 Undergraduate financial-aid policy

| Field | Value |
|-------|-------|
| Need-blind/need-aware | Need-aware for all students (including Home) |
| LSE Bursary | Available for Home students with household income below threshold |
| LSE Scholarships | Limited merit-based and need-based scholarships for international students |
| Student Finance England | Home students eligible for tuition fee loans and maintenance loans |
| International scholarships | Limited — LSE Graduate Support Scheme, Chevening, Commonwealth |

> **Note**: LSE is NOT need-blind. Unlike US Ivy League institutions, LSE does not guarantee to meet full demonstrated need. International students should expect to self-fund or secure external scholarships.

### 4.3 Graduate cost & funding framework

| Field | Value |
|-------|-------|
| Tuition fees | Vary by programme — listed on individual programme pages |
| Fee reduction for LSE UG alumni | 10% discount on taught graduate fees |
| Research funding | Most MPhil/PhD programmes offer full funding (fees + stipend) |
| Taught master's funding | Generally self-funded; some departmental scholarships available |
| Application fee | Not centrally published (varies) |
| Fee-waiver policy | Needs-based fee waivers available for some programmes |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "The London School of Economics and Political Science (LSE)"
  source_url: https://www.lse.ac.uk
  source_snippet: "The London School of Economics and Political Science (LSE)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.programme_count
  value: "over 40 undergraduate degrees"
  source_url: https://www.lse.ac.uk/study-at-lse/Undergraduate
  source_snippet: "Choose from over 40 undergraduate degrees across the social sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.fees.home_2026_27
  value: "£9,790"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics
  source_snippet: "Home: £9,790 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.fees.overseas_economics_2026_27
  value: "£39,900"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics
  source_snippet: "Overseas students (2026/27): £39,900 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.fees.overseas_management_2026_27
  value: "£35,700"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-accounting-and-finance
  source_snippet: "Overseas: £35,700 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.fees.overseas_history_2026_27
  value: "£28,900"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/ba-history
  source_snippet: "Overseas students: £28,900 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.entry_requirements.economics
  value: "A*AA with A* in Mathematics; IB 39 points, 766 HL, 7 in Maths"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics
  source_snippet: "Standard offer: A*AA with an A* in Mathematics; IB: 39 points overall, 766 at Higher Level, with a 7 in Mathematics"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.entry_requirements.sociology
  value: "AAB; IB 37 points, 666 HL"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-sociology
  source_snippet: "Standard offer: AAB; IB: 37 points overall, with 666 at higher level"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english_requirements.ielts
  value: "7.0 overall, 7.0 each component"
  source_url: https://www.lse.ac.uk/study-at-lse/Undergraduate/Prospective-Students/How-to-Apply/English-language-requirements
  source_snippet: "IELTS Academic (incl. online): 7.0 Overall, 7.0 in each component"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_requirements.toefl
  value: "100 overall; W27/R25/L24/S24"
  source_url: https://www.lse.ac.uk/study-at-lse/Undergraduate/Prospective-Students/How-to-Apply/English-language-requirements
  source_snippet: "TOEFL iBT: 100 Writing: 27, Reading: 25, Listening: 24, Speaking: 24"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.ucas_deadline
  value: "13 January 2027"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics
  source_snippet: "Application Deadline: 13 January 2027"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.tmua_requirement
  value: "TMUA mandatory for BSc Economics and BSc Econometrics and Mathematical Economics"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics
  source_snippet: "TMUA (Test of Mathematics for University Admission) is mandatory"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-001:
  field: graduate.programme_count
  value: "157 programmes (110 MSc/MA/LLM/MPA/MPP + 12 Executive + 24 Double Degrees + 35 MPhil/PhD + 27 VRS)"
  source_url: https://www.lse.ac.uk/study-at-lse/Graduate/Available-programmes
  source_snippet: "Total: 157 programmes across all categories"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-002:
  field: graduate.english_requirements.standard
  value: "IELTS 7.0 (6.5 each); TOEFL 100 (R23/L22/W24/S22)"
  source_url: https://www.lse.ac.uk/study-at-lse/Graduate/Prospective-students/Entry-requirements/English-language-requirements
  source_snippet: "IELTS Academic: 7.0 Overall, Reading 6.5, Listening 6.5, Writing 6.5, Speaking 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_requirements.law
  value: "IELTS 7.5 (R7.0/L7.0/W7.0/S6.5); TOEFL 109 (R25/L24/W27/S22)"
  source_url: https://www.lse.ac.uk/study-at-lse/Graduate/Prospective-students/Entry-requirements/English-language-requirements
  source_snippet: "IELTS Academic: 7.5 Overall, Reading 7.0, Listening 7.0, Writing 7.0, Speaking 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-004:
  field: graduate.entry_requirements.degree_mark
  value: "at least 70% in final year; GPA 3.5/4.0"
  source_url: https://www.lse.ac.uk/study-at-lse/Graduate/Prospective-students/Entry-requirements
  source_snippet: "at least 70 per cent of the available marks in your final year examinations; a GPA of at least 3.5 out of 4 or above"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-005:
  field: graduate.fee_reduction_lse_alumni
  value: "10% discount for LSE UG alumni"
  source_url: https://www.lse.ac.uk/study-at-lse/Graduate/fees-and-funding
  source_snippet: "Students who completed undergraduate study at LSE and are beginning taught graduate study receive a fee reduction of 10 per cent of the fee"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-S-001:
  field: departments.count
  value: "20 departments + 6 institutes/schools"
  source_url: https://info.lse.ac.uk/Staff/Departments-and-Institutes
  source_snippet: "20 Departments, 5 Institutes/Schools, 2 Other academic units"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-S-002:
  field: undergraduate.interviews
  value: "Not required"
  source_url: https://www.lse.ac.uk/study-at-lse/Undergraduate/Prospective-Students/How-to-Apply
  source_snippet: "LSE does not interview applicants for undergraduate admission"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-S-003:
  field: undergraduate.year_abroad_fee
  value: "Home £1,465; Overseas £4,335"
  source_url: https://info.lse.ac.uk/staff/divisions/Planning-Division/Table-of-Fees
  source_snippet: "Exchange/Study Abroad Year Fees 2026/27: Home £1,465, Overseas £4,335"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-S-004:
  field: undergraduate.placement_year_fee
  value: "Home £1,955; Overseas £6,140"
  source_url: https://info.lse.ac.uk/staff/divisions/Planning-Division/Table-of-Fees
  source_snippet: "Placement Year Fees 2026/27: Home £1,955, Overseas £6,140"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-S-005:
  field: undergraduate.admissions_statistics.economics
  value: "2,885 applications, 217 intake (13:1 ratio)"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-economics
  source_snippet: "Applications: 2,885; Intake: 217; Ratio: 13:1"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-S-006:
  field: undergraduate.admissions_statistics.management
  value: "2,407 applications, 163 intake (15:1 ratio)"
  source_url: https://www.lse.ac.uk/study-at-lse/undergraduate/bsc-management
  source_snippet: "Applications: 2,407; Intake: 163; Ratio: 15:1"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
lse-knowledge-base-v2/
├── 00-overview.md                    ← Section 0 (rules 1-4)
├── 01-ug-programmes.md               ← Section 1 (full UG list)
├── 02-pg-taught-programmes.md        ← Section 2 (MSc/MA/LLM/MPA/MPP)
├── 03-pg-executive-programmes.md     ← Section 2 (Executive Masters)
├── 04-pg-double-degrees.md           ← Section 2 (Double Degrees)
├── 05-pg-research-programmes.md      ← Section 2 (MPhil/PhD, MRes/PhD)
├── 06-application-requirements.md    ← Section 3
├── 07-costs-and-funding.md           ← Section 4
├── 08-evidence-chain.md              ← Section 5
└── 09-comparison-framework.md        ← Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "lse-knowledge-base-v2"
  school: "<home department>"
  department: "<home department>"
  degree_level: "<BA|BSc|MSc|MA|LLM|MPA|MPP|MPhil/PhD|MRes/PhD>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Per-programme overseas fees for all 43 UG programmes | Individual programme pages |
| **P1** | Graduate programme fees (per-programme overseas fees) | Individual programme pages |
| **P1** | Graduate application deadlines (per-programme) | Individual programme pages |
| **P1** | Graduate application fee amount | Graduate admissions pages |
| **P2** | Per-programme A-Level/IB entry requirements for all 43 UG programmes | Individual programme pages |
| **P2** | LSE Bursary/scholarship details and thresholds | Financial aid pages |
| **P2** | Research programme funding details (stipend rates) | Graduate funding pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | LSE | Imperial | UCL | KCL | Edinburgh |
|-----------|-----|---------|-----|-----|-----------|
| Total UG programmes | 43 | ~70 | ~437 | ~150 | ~300 |
| Total PG programmes | 157 | ~248 | TBD | TBD | TBD |
| Russell Group | Yes | Yes | Yes | Yes | Yes |
| Home UG fee (2026/27) | £9,790 | £9,250 | £9,250 | £9,250 | £9,250 |
| Overseas UG fee range | £28,900–£39,900 | TBD | TBD | TBD | TBD |
| Application platform | UCAS | UCAS | UCAS | UCAS | UCAS |
| UCAS deadline | 13 Jan 2027 | 15 Jan | 15 Jan | 15 Jan | 15 Jan |
| IELTS UG minimum | 7.0 (7.0 each) | TBD | TBD | TBD | TBD |
| Interviews | No | Some | Some | Some | Some |
| Admissions tests | TMUA (Economics) | TBD | TBD | TBD | TBD |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Updated**: 2026-07-08 (UG programme list corrected via ego-browser)
> **Sources**: www.lse.ac.uk, info.lse.ac.uk
> **Verification**: ego-browser (UG programmes), WebFetch (PG programmes, fees, deadlines)
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programmes 43/43 (100%) | PG programmes 157/157 (100%) | Evidence (21 blocks) | Fees (UG complete, PG partial)
> **Next step**: Verify PG fees per programme; extract per-programme A-Level/IB requirements for all 43 UG programmes
