# University of Reading — 知识库 · 完整深度数据 v2.0

> 数据采集日期：2026-07-08  ·  招生周期：2026/27  ·  来源主域：reading.ac.uk
>
> **本文件结构**：§ 0 院校总览（5 项结构规则 / 4 种聚合视图）· § 1 学院 + 系 / 学科领域层次 · § 2 全量专业明细 · § 3 申请要求 · § 4 学费与生活费 · § 5 英语语言要求 · § 6 WeKnora 摄入清单 + 监测设计 · § 7 数据来源与变更日志

---

## § 0 院校总览

### 0.1 关键事实

| 字段 | 值 |
|---|---|
| 全称 | University of Reading |
| 中文 | 雷丁大学 |
| 创立年份 | 1892（亨利·帕尔默校长团队获皇家特许，1926年大学宪章） |
| 校园 | 雷丁（Whiteknights 主校区 + London Road + Henley-on-Thames 商学院）+ 马来西亚双学位伙伴 |
| 集团 | 英国研究型大学联盟成员（曾为 1994 Group） |
| 学院 / 学校数 | 12（含 Henley Business School 独立商学院 + 6 大学科学院 / 文科学院 + GIIDAE 研究生院） |
| 学生总规模 | ~23,000（其中 ~17,000 本科 + ~6,000 研究生） |
| 国际生比例 | 约 30%（2025/26 招生数据） |
| 主要海外分支 | University of Reading Malaysia (UoRM, 读于 EduCity, Iskandar Puteri) |
| 卓越研究方向 | Agriculture & Food 大类、Meteorology、Built Environment、Hunger Studies、Henley 商学院（EQUIS + AMBA 双认证 + AACSB 候选） |

### 0.2 RULE 1 — 专业 / 项目总数

| 类别 | 数量 |
|---|---:|
| 本科专业（UG, 包括同专业 with-placement / with-year-abroad / with-foundation 变体） | 322 |
| 研究生授课型（PG, 包含 PGCE/PgCE/PGCert/MSc/MA/MBA 等） | 144 |
| **总计** | **466** |

> 备注：本科 322 个 = 大量 "with Year Abroad"、"with Placement"、"with Foundation" 派生的同名课程。研究生 144 个 = 含 19 个 PGCE/PgCE 教师培训项目、7 个 LLM、11 个 Henley 商学院 pre-experience 项目、以及 7 个博士级（MPhil/MBA/DBA）。

### 0.3 RULE 2 — 学院 / 系 层次结构

University of Reading 由以下 12 个学院 / 学校 / 研究所组成（以学科领域 "subject area" 为二级组织）：

- **Henley Business School** (75 个项目)
    - Accounting (0 个项目, subjects: `accounting`)
    - Business, Management, Accounting and Finance (46 个项目, subjects: `business-and-management-accounting-and-finance`)
    - Business and Management (Pre-Experience) — Henley MSc (11 个项目, subjects: `business-pre-experience`)
    - Business (Post-Experience) — Henley MBA / DBA / Executive (4 个项目, subjects: `business-post-experience`)
    - Management (0 个项目, subjects: `management`)
    - Marketing (4 个项目, subjects: `marketing`)
    - Finance (7 个项目, subjects: `finance`)
    - Digital Business & Consumer Behaviour (3 个项目, subjects: `digital-business`, `consumer-behaviour`, `consumer-behaviour-and-marketing`)
    - Project Management (0 个项目, subjects: `project-management`)
- **Graduate Institute of International Development, Agriculture and Economics (GIIDAE)** (11 个项目)
    - International Development and Applied Economics (11 个项目, subjects: `international-development-and-applied-economics`)
- **School of Archaeology, Geography and Environmental Science (SAGES)** (39 个项目)
    - Archaeology (13 个项目, subjects: `archaeology`)
    - Geography (8 个项目, subjects: `geography`)
    - Environment (6 个项目, subjects: `environment`, `environmental-science`)
    - Meteorology and Climate (6 个项目, subjects: `meteorology-and-climate`, `climate-science`)
    - Geography and Environmental Science (1 个项目, subjects: `geography-and-environmental-science`)
    - Ecology (5 个项目, subjects: `ecology`)
    - Wildlife Conservation (0 个项目, subjects: `wildlife-conservation`)
- **School of Arts and Communication Design (SACD)** (22 个项目)
    - Art (9 个项目, subjects: `art`)
    - Film and Television (4 个项目, subjects: `film-and-television`, `film-theatre-and-television`)
    - Theatre and Performance (0 个项目, subjects: `theatre`, `drama`)
    - Graphic Communication and Design (7 个项目, subjects: `graphic-communication-and-design`, `graphic-design`, `typography-and-graphic-communication`)
    - Creative Writing (2 个项目, subjects: `creative-writing`)
    - Digital Media and Communication (0 个项目, subjects: `digital-media-and-communication`)
- **School of Chemistry, Food and Pharmacy (SCFP)** (38 个项目)
    - Chemistry (8 个项目, subjects: `chemistry`)
    - Food and Nutrition (13 个项目, subjects: `food-and-nutrition`, `food-and-nutritional-sciences`)
    - Nutrition / Nutritional Sciences / Dietetics (0 个项目, subjects: `nutrition`, `nutritional-sciences`, `dietetics`)
    - Pharmacy (8 个项目, subjects: `pharmacy`)
    - Pharmacology (0 个项目, subjects: `pharmacology`)
    - Medical Sciences (9 个项目, subjects: `medical-sciences`)
- **School of Mathematical, Physical and Computational Sciences (SMPCS)** (17 个项目)
    - Mathematics (10 个项目, subjects: `mathematics`)
    - Computer Science (7 个项目, subjects: `computer-science`, `artificial-intelligence`, `information-technology`, `data-science`)
    - Engineering (interdisciplinary, joint with SBE/SACES) (0 个项目, subjects: `engineering`)
- **School of Philosophy, Politics and Economics (SPPE)** (36 个项目)
    - Politics and International Relations (11 个项目, subjects: `politics`, `politics-and-international-relations`, `international-relations`)
    - Philosophy (14 个项目, subjects: `philosophy`)
    - Economics (11 个项目, subjects: `economics`)
    - Public Policy (0 个项目, subjects: `public-policy`)
    - Social Policy (0 个项目, subjects: `social-policy`)
    - Strategic Studies (0 个项目, subjects: `strategic-studies`)
    - War and Peace Studies (0 个项目, subjects: `war-and-peace-studies`)
- **School of Biological Sciences** (33 个项目)
    - Biological Sciences (24 个项目, subjects: `biological-sciences`)
    - Biomedical Sciences (0 个项目, subjects: `biomedical-sciences`)
    - Biomedical Engineering (interdisciplinary) (2 个项目, subjects: `biomedical-engineering`)
    - Biochemistry (0 个项目, subjects: `biochemistry`)
    - Microbiology (0 个项目, subjects: `microbiology`)
    - Zoology (5 个项目, subjects: `zoology`)
    - Bioveterinary Sciences (2 个项目, subjects: `bioveterinary-sciences`)
- **School of the Built Environment (SBE) + School of Construction Management and Engineering (CME)** (0 个项目)
    - Building and Surveying (0 个项目, subjects: `building-and-surveying`)
    - Construction Management (11 个项目, subjects: `construction-management`, `surveying-and-construction-management`, `construction-management-and-engineering`)
    - Real Estate and Planning (11 个项目, subjects: `real-estate-and-planning`)
    - Architectural Engineering (2 个项目, subjects: `architectural-engineering`)
    - Architecture (2 个项目, subjects: `architecture`)
    - Energy and Environmental Engineering (0 个项目, subjects: `energy-and-environmental-engineering`)
- **School of Humanities** (25 个项目)
    - English Literature (6 个项目, subjects: `english-literature`)
    - History (7 个项目, subjects: `history`)
    - Anthropology (0 个项目, subjects: `anthropology`)
    - Sociology / Criminology (4 个项目, subjects: `sociology`, `criminology`)
    - Classics and Classical Studies (9 个项目, subjects: `classics`, `ancient-history`, `classics-and-ancient-history`)
    - Museum Studies (1 个项目, subjects: `museum-studies`)
    - Global Sustainable Development (2 个项目, subjects: `global-sustainable-development`)
- **School of Language, Linguistics and Cultures** (0 个项目)
    - English Language and Applied Linguistics (7 个项目, subjects: `english-language-and-applied-linguistics`)
    - Linguistics (0 个项目, subjects: `linguistics`)
    - Modern Languages (French/German/Spanish/Italian) (0 个项目, subjects: `french`, `german`, `spanish`, `italian`)
    - Languages and Cultures (combinations) (8 个项目, subjects: `languages-and-cultures`)
- **School of Psychology and Clinical Language Sciences** (20 个项目)
    - Psychology (17 个项目, subjects: `psychology`)
    - Speech and Language Therapy (2 个项目, subjects: `speech-and-language-therapy`)
    - Physician Associate (1 个项目, subjects: `physician-associate`)
    - Healthcare (0 个项目, subjects: `healthcare`)
- **Institute of Education (IoE)** (0 个项目)
    - Education (38 个项目, subjects: `education`)
    - Teaching / PGCE / Apprenticeship (0 个项目, subjects: `teaching`)
- **Global Academy** (42 个项目)
    - Foundation Programmes (1-year on-campus) (12 个项目, subjects: `foundation-programmes`)
    - International Foundation Pathways (with IFY, January/September) (30 个项目, subjects: `international-foundation-pathways`)
- **School of Law** (20 个项目)
    - Law (LLB / LLM / LPC / Conversion) (20 个项目, subjects: `law`)

### 0.4 RULE 3 — 学历级别明细

| Degree Prefix | 全称 | UG | PG | 合计 |
|---|---|---:|---:|---:|
| BSc | Bachelor of Science | 188 | 0 | 188 |
| BA | Bachelor of Arts | 97 | 0 | 97 |
| MSc | Master of Science | 0 | 70 | 70 |
| PGCE | Postgraduate Certificate in Education | 0 | 19 | 19 |
| MA | Master of Arts | 0 | 17 | 17 |
| MSci | Master in Science (UG integrated) — 4yr | 15 | 0 | 15 |
| Other/Unclassified | Apprenticeships & unclassified titles | 0 | 12 | 12 |
| LLM | Master of Laws | 0 | 7 | 7 |
| PGCert | Postgraduate Certificate | 0 | 6 | 6 |
| LLB | Bachelor of Laws | 5 | 0 | 5 |
| BEng | Bachelor of Engineering | 4 | 0 | 4 |
| MRes | Master of Research | 0 | 4 | 4 |
| PGDip | Postgraduate Diploma | 0 | 2 | 2 |
| MPharm | Master of Pharmacy — UG integrated | 2 | 0 | 2 |
| IFP | International Foundation Programme | 2 | 0 | 2 |
| MPlan | Master of Planning | 2 | 0 | 2 |
| MMath | Master of Mathematics — UG integrated | 2 | 0 | 2 |
| Postgraduate Certificate in Education | PGCE variant (Reflective Practice) | 0 | 1 | 1 |
| MPAS | Master of Physician Associate Studies | 1 | 0 | 1 |
| MEng | Master of Engineering — UG integrated | 1 | 0 | 1 |
| Foundation Degree | Foundation Degree | 1 | 0 | 1 |
| Doctor of Business Administration | DBA | 0 | 1 | 1 |
| MLaw | Master of Law (UG integrated) — 4yr | 1 | 0 | 1 |
| LPC | Legal Practice Course | 0 | 1 | 1 |
| Conversion | Conversion programme in Law | 0 | 1 | 1 |
| Postgraduate Certificate in Healthcare Education | PGCert (Healthcare Education) | 0 | 1 | 1 |
| Master of Architecture | Master of Architecture (MArch, UG integrated) | 0 | 1 | 1 |
| MBA | Master of Business Administration | 0 | 1 | 1 |
| MMet | Master of Meteorology — UG integrated | 1 | 0 | 1 |

### 0.5 RULE 4 — 学院 × 学历级别 分布矩阵

| 学院 (School) | UG BSc | UG BA | UG MSci/其他 | PG MSc | PG MA | PG MBA/DBA | PG PGCE/PGCert | PG LLM | PG Other | 总计 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Henley Business School | 48 | 2 | 0 | 22 | 0 | 2 | 0 | 0 | 1 | 75 |
| Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 11 |
| School of Archaeology, Geography and Environmental Science (SAGES) | 18 | 12 | 3 | 5 | 1 | 0 | 0 | 0 | 0 | 39 |
| School of Arts and Communication Design (SACD) | 0 | 14 | 0 | 0 | 7 | 0 | 0 | 0 | 1 | 22 |
| School of Chemistry, Food and Pharmacy (SCFP) | 23 | 0 | 5 | 4 | 0 | 0 | 5 | 0 | 1 | 38 |
| School of Mathematical, Physical and Computational Sciences (SMPCS) | 13 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 17 |
| School of Philosophy, Politics and Economics (SPPE) | 5 | 23 | 0 | 4 | 3 | 0 | 0 | 0 | 1 | 36 |
| School of Biological Sciences | 17 | 0 | 12 | 4 | 0 | 0 | 0 | 0 | 0 | 33 |
| School of the Built Environment (SBE) + School of Construction Management and Engineering (CME) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| School of Humanities | 2 | 20 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 25 |
| School of Language, Linguistics and Cultures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| School of Psychology and Clinical Language Sciences | 7 | 0 | 1 | 7 | 0 | 0 | 0 | 0 | 5 | 20 |
| Institute of Education (IoE) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Global Academy | 33 | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 42 |
| School of Law | 4 | 0 | 6 | 0 | 0 | 0 | 0 | 7 | 3 | 20 |
| **总计（应等于 466）** | 188 | 97 | 37 | 70 | 17 | 2 | 27 | 7 | 9 | **466** |

### 0.6 学院 × 学位级别 清单（按招生数排序）

**Henley Business School** — 共 75 个项目 (6 个学科领域):
  - `business-and-management-accounting-and-finance` (46, Business, Management, Accounting and Finance) — BSc=44, BA=2
  - `business-pre-experience` (11, Business and Management (Pre-Experience)) — MSc=11
  - `finance` (7, Finance) — MSc=7
  - `business-post-experience` (4, Business (Post-Experience) / Henley MBA) — Doctor of Business Administration=1, MBA=1, MSc=1
  - `marketing` (4, Marketing) — BSc=4
  - `digital-business` (3, Digital Business) — MSc=3

**Global Academy** — 共 42 个项目 (2 个学科领域):
  - `international-foundation-pathways` (30, International Foundation Pathways) — BSc=23, BA=4, IFP=2, BEng=1
  - `foundation-programmes` (12, Foundation Programmes) — BSc=10, BA=2

**School of Archaeology, Geography and Environmental Science (SAGES)** — 共 39 个项目 (6 个学科领域):
  - `archaeology` (13, Archaeology) — BA=12, MA=1
  - `geography` (8, Geography) — BSc=8
  - `meteorology-and-climate` (6, Meteorology and Climate) — MSc=4, BSc=1, MMet=1
  - `environment` (6, Environment) — BSc=6
  - `ecology` (5, Ecology) — BSc=3, MSci=2
  - `geography-and-environmental-science` (1, Geography and Environmental Science) — MSc=1

**School of Chemistry, Food and Pharmacy (SCFP)** — 共 38 个项目 (5 个学科领域):
  - `medical-sciences` (9, Medical Sciences) — BSc=6, MSci=2, MPAS=1
  - `food-and-nutrition` (9, Food and Nutrition) — BSc=9
  - `pharmacy` (8, Pharmacy) — PGCert=5, MPharm=2
  - `chemistry` (8, Chemistry) — BSc=8
  - `food-and-nutritional-sciences` (4, Food and Nutritional Sciences) — MSc=4

**School of Philosophy, Politics and Economics (SPPE)** — 共 36 个项目 (4 个学科领域):
  - `philosophy` (14, Philosophy) — BA=13, MA=1
  - `economics` (11, Economics) — BSc=5, MSc=4, BA=2
  - `politics` (8, Politics and International Relations) — BA=8
  - `politics-and-international-relations` (3, Politics and International Relations) — MA=2, MRes=1

**School of Biological Sciences** — 共 33 个项目 (4 个学科领域):
  - `biological-sciences` (24, Biological Sciences) — BSc=12, MSci=8, MSc=4
  - `zoology` (5, Zoology) — BSc=3, MSci=2
  - `biomedical-engineering` (2, Biomedical Engineering) — BEng=2
  - `bioveterinary-sciences` (2, Bioveterinary Sciences) — BSc=2

**School of Humanities** — 共 25 个项目 (7 个学科领域):
  - `history` (7, History) — BA=6, MA=1
  - `english-literature` (6, English Literature) — BA=5, MA=1
  - `ancient-history` (5, Ancient History) — BA=5
  - `classics` (3, Classics and Classical Studies) — BA=3
  - `global-sustainable-development` (2, Global Sustainable Development) — BSc=2
  - `classics-and-ancient-history` (1, Classics and Ancient History) — MA=1
  - `museum-studies` (1, Museum Studies) — BA=1

**School of Arts and Communication Design (SACD)** — 共 22 个项目 (6 个学科领域):
  - `art` (9, Art) — BA=8, MA=1
  - `typography-and-graphic-communication` (6, Typography and Graphic Communication) — MA=5, MRes=1
  - `film-and-television` (3, Film and Television) — BA=3
  - `creative-writing` (2, Creative Writing) — BA=2
  - `film-theatre-and-television` (1, Film, Theatre and Television) — MA=1
  - `graphic-communication-and-design` (1, Graphic Communication and Design) — BA=1

**School of Psychology and Clinical Language Sciences** — 共 20 个项目 (3 个学科领域):
  - `psychology` (17, Psychology) — BSc=7, MSc=4, PGDip=2, MSci=1
  - `speech-and-language-therapy` (2, Speech and Language Therapy) — MSc=2
  - `physician-associate` (1, Physician Associate) — MSc=1

**School of Law** — 共 20 个项目 (1 个学科领域):
  - `law` (20, Law) — LLM=7, LLB=5, BSc=4, LPC=1, MRes=1

**School of Mathematical, Physical and Computational Sciences (SMPCS)** — 共 17 个项目 (2 个学科领域):
  - `mathematics` (10, Mathematics) — BSc=8, MMath=2
  - `computer-science` (7, Computer Science) — BSc=5, MSc=2

**Graduate Institute of International Development, Agriculture and Economics (GIIDAE)** — 共 11 个项目 (1 个学科领域):
  - `international-development-and-applied-economics` (11, International Development and Applied Economics (GIIDAE)) — MSc=10, MRes=1

**School of the Built Environment (SBE) + School of Construction Management and Engineering (CME)** — 共 0 个项目 (0 个学科领域):

**School of Language, Linguistics and Cultures** — 共 0 个项目 (0 个学科领域):

**Institute of Education (IoE)** — 共 0 个项目 (0 个学科领域):
## § 1 学院 + 系 / 学科领域 层次结构（详尽）

> 每个学科领域（subject area）下，列出 **所有学位类型组合**，内嵌全部 program 名称。URL 直链到 Reading 官方课程详情页。每个 program 在 § 2 仍以一张表重复呈现以便过滤。

### 1.x  Henley Business School  ·  75 个项目

#### Business, Management, Accounting and Finance  ·  `business-and-management-accounting-and-finance`  ·  46 个项目

**UG · BA** — 2 个

- BA Accounting (Beijing Institute of Technology)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/ba-accounting-beijing
- BA International Business Management (SQA Advanced Diploma students in China)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/ba-international-business-management-sqa-china

**UG · BSc** — 44 个

- BSc Accounting and Business – The Flying Start Degree Programme
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-business
- BSc Accounting and Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-finance
- BSc Accounting and Finance with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-finance-with-placement-experience
- BSc Accounting and Finance with Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-finance-with-year-abroad
- BSc Accounting and Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-management
- BSc Accounting and Management with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-management-with-placement-experience
- BSc Accounting and Management with Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-management-with-year-abroad
- BSc Business and Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management
- BSc Business and Management (Data Analytics and Digital Business)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-data-analytics-and-digital-business
- BSc Business and Management (Data Analytics and Digital Business) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-data-analytics-and-digital-business-with-placement-year
- BSc Business and Management (Data Analytics and Digital Business) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-data-analytics-and-digital-business-with-study-year-abroad
- BSc Business and Management (Entrepreneurship and Innovation)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-entrepreneurship
- BSc Business and Management (Entrepreneurship and Innovation) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-entrepreneurship-with-placement-year
- BSc Business and Management (Entrepreneurship and Innovation) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-entrepreneurship-with-study-year-abroad
- BSc Business and Management (Human Resources and Organisational Behaviour)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-human-resources
- BSc Business and Management (Human Resources and Organisational Behaviour) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-human-resources-with-placement-year
- BSc Business and Management (Human Resources and Organisational Behaviour) with Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-human-resources-with-year-abroad
- BSc Business and Management (MUST 2+2 programme)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/macau-university-of-science-and-technology
- BSc Business and Management (Marketing)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-marketing
- BSc Business and Management (Marketing) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-marketing-with-placement-year
- BSc Business and Management (Marketing) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-marketing-with-study-year-abroad
- BSc Business and Management with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-with-placement-year
- BSc Business and Management with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-with-study-year-abroad
- BSc Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance
- BSc Finance (FinTech)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-fintech
- BSc Finance (FinTech) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-fintech-with-placement-year
- BSc Finance (FinTech) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-fintech-with-study-year-abroad
- BSc Finance (International Business)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-international-business
- BSc Finance (International Business) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-international-business-with-placement-year
- BSc Finance (International Business) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-international-business-with-study-year-abroad
- BSc Finance (Investments)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-investments
- BSc Finance (Investments) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-investments-with-placement
- BSc Finance (Investments) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-investments-with-study-year-abroad
- BSc Finance (Sustainable Finance)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-sustainable-finance
- BSc Finance (Sustainable Finance) with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-sustainable-finance-placement-year
- BSc Finance (Sustainable Finance) with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-sustainable-finance-study-year-abroad
- BSc Finance with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-with-placement-year
- BSc Finance with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-with-study-year-abroad
- BSc International Business and Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management
- BSc International Business and Management with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-placement-year
- BSc International Business and Management with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-study-year-abroad
- BSc International Business and Management with a Modern Language
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-modern-language
- BSc International Business and Management with a Modern Language with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-modern-language-with-placement-year
- BSc International Business and Management with a Modern Language with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-modern-language-with-study-year-abroad


#### Business (Post-Experience) / Henley MBA  ·  `business-post-experience`  ·  4 个项目

**PG · Doctor of Business Administration** — 1 个

- Doctor of Business Administration
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/doctor-business-administration

**PG · MBA** — 1 个

- The Henley Executive MBA - Global
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/henley-executive-mba

**PG · MSc** — 1 个

- MSc Coaching for Behavioural Change
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/msc-in-coaching-and-behavioural-change

**PG · Other** — 1 个

- The Henley Flexible Executive MBA
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/the-henley-flexible-executive-mba


#### Business and Management (Pre-Experience)  ·  `business-pre-experience`  ·  11 个项目

**PG · MSc** — 11 个

- MSc Accounting, Financial Management and Digital Business
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-accounting-financial-management-digital-business
- MSc Applied AI for Business
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-applied-ai-for-business
- MSc Digital Marketing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-digital-marketing
- MSc Entrepreneurship and Innovation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-entrepreneurship-and-innovation
- MSc International Accounting and Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-accounting-and-finance
- MSc International Business
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-business
- MSc International Business and Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-business-and-finance
- MSc International Human Resource Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-human-resource-management
- MSc Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-management
- MSc Marketing (International Marketing)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-marketing-international-marketing
- MSc Marketing (Sustainable Marketing)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-sustainable-marketing


#### Digital Business  ·  `digital-business`  ·  3 个项目

**PG · MSc** — 3 个

- MSc Digital Business and Data Analytics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/digital-business-pg/msc-digital-business-data-analytics
- MSc Digital Innovation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/digital-business-pg/msc-digital-innovation
- MSc International Business and Digital Transformation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/digital-business-pg/msc-international-business-digital-transformation


#### Finance  ·  `finance`  ·  7 个项目

**PG · MSc** — 7 个

- MSc Behavioural Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-behavioural-finance
- MSc Climate Change, Sustainable Business and Green Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-climate-change-sustainable-business-green-finance
- MSc Corporate Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-corporate-finance
- MSc Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-finance
- MSc Finance and Financial Technology (FinTech)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-finance-and-financial-technology-fintech
- MSc Financial Risk Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-financial-risk-management
- MSc Investment Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-investment-management


#### Marketing  ·  `marketing`  ·  4 个项目

**UG · BSc** — 4 个

- BSc Consumer Behaviour and Marketing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-consumer-behaviour-and-marketing
- BSc Consumer Behaviour and Marketing with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-consumer-behaviour-and-marketing-with-placement-year
- BSc Food Business and Marketing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-food-business-and-marketing
- BSc Food Business and Marketing with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-food-business-and-marketing-with-placement-year


### 1.x  Global Academy  ·  42 个项目

#### Foundation Programmes  ·  `foundation-programmes`  ·  12 个项目

**UG · BA** — 2 个

- BA English Language and Linguistics with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/ba-english-language-and-linguistics-with-foundation
- BA English Literature with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/ba-english-literature-with-foundation

**UG · BSc** — 10 个

- BSc Accounting and Management with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-accounting-and-management-with-foundation
- BSc Agricultural Business Management with Foundation Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-agricultural-business-management-with-foundation
- BSc Bioveterinary Sciences with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-bioveterinary-sciences-with-foundation
- BSc Business and Management with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-business-and-management-with-foundation
- BSc Chemistry with Cosmetic Science with Foundation Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-chemistry-with-cosmetic-science-with-foundation
- BSc Consumer Behaviour and Marketing with Foundation Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-consumer-behaviour-and-marketing-with-foundation
- BSc Finance with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-finance-with-foundation
- BSc Food Business and Marketing with Foundation Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-food-marketing-and-business-economics-with-foundation
- BSc Nutrition with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-nutrition-with-foundation
- BSc Real Estate with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-real-estate-with-foundation


#### International Foundation Pathways  ·  `international-foundation-pathways`  ·  30 个项目

**UG · BA** — 4 个

- BA Economics with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-economics-ifp-january
- BA Economics with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-economics-ifp-september
- BA Museum Studies and Archaeology with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-museum-studies-and-archaeology-ifp-september
- BA Politics and International Relations with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-politics-and-international-relations-ifp-september

**UG · BEng** — 1 个

- BEng Architectural Engineering with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/beng-architectural-engineering-ifp-september

**UG · BSc** — 23 个

- BSc Agricultural Business Management with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-agricultural-business-management-ifp-january
- BSc Agricultural Business Management with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-agricultural-business-management-ifp-september
- BSc Agriculture with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-agriculture-ifp-september
- BSc Building Surveying with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-building-surveying-ifp-january
- BSc Building Surveying with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-building-surveying-ifp-september
- BSc Computer Science with Artificial Intelligence with International Foundation Year (awaiting approval)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-computer-science-with-artificial-intelligence-with-international-foundation-year-september
- BSc Construction Management and Surveying with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-and-surveying-ifp-january
- BSc Construction Management and Surveying with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-and-surveying-ifp-september
- BSc Construction Management with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-ifp-january
- BSc Construction Management with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-ifp-september
- BSc Consumer Behaviour and Marketing with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-consumer-behaviour-and-marketing-ifp-january
- BSc Consumer Behaviour and Marketing with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-consumer-behaviour-and-marketing-ifp-september
- BSc Economics and Finance with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-economics-and-finance-ifp-january
- BSc Economics and Finance with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-economics-and-finance-ifp-september
- BSc Environmental Science with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-environmental-science-ifp-september
- BSc Food Business and Marketing with International Foundation Year - January entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-food-business-and-marketing-ifp-january
- BSc Food Business and Marketing with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-food-business-and-marketing-ifp-september
- BSc Mathematics with Finance and Investment Banking with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-mathematics-with-finance-and-investment-banking-ifp-september
- BSc Mathematics with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-mathematics-ifp-september
- BSc Meteorology and Climate with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-meteorology-and-climate-ifp-september
- BSc Psychology with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-psychology-ifp-september
- BSc Quantity Surveying with International Foundation Year - January Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-quantity-surveying-ifp-january
- BSc Quantity Surveying with International Foundation Year - September Entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-quantity-surveying-ifp-september

**UG · IFP** — 2 个

- IFP International Foundation Programme - January
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/international-foundation-pathways-january-entry
- IFP International Foundation Programme - September
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/international-foundation-pathways-september-entry


### 1.x  School of Archaeology, Geography and Environmental Science (SAGES)  ·  39 个项目

#### Archaeology  ·  `archaeology`  ·  13 个项目

**PG · MA** — 1 个

- MA Archaeology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-pg/ma-archaeology

**UG · BA** — 12 个

- BA Archaeology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology
- BA Archaeology and Anthropology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-anthropology
- BA Archaeology and Anthropology with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-anthropology-with-professional-placement
- BA Archaeology and Anthropology with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-anthropology-with-study-year-abroad
- BA Archaeology and History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-history
- BA Archaeology and History with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-history-with-professional-experience
- BA Archaeology and History with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-history-with-study-year-abroad
- BA Archaeology with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-with-professional-experience
- BA Archaeology with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-with-study-abroad-year
- BA Museum Studies and Archaeology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-museum-studies-and-archaeology
- BA Museum Studies and Archaeology with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-museum-studies-and-archaeology-with-professional-experience
- BA Museum Studies and Archaeology with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-museum-studies-and-archaeology-with-study-year-abroad


#### Ecology  ·  `ecology`  ·  5 个项目

**UG · BSc** — 3 个

- BSc Ecology and Wildlife Conservation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/bsc-ecology-and-wildlife-conservation
- BSc Ecology and Wildlife Conservation with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/bsc-ecology-and-wildlife-conservation-with-foundation
- BSc Ecology and Wildlife Conservation with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/bsc-ecology-and-wildlife-conservation-with-professional-experience

**UG · MSci** — 2 个

- MSci Ecology and Wildlife Conservation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/msci-ecology-and-wildlife-conservation
- MSci Ecology and Wildlife Conservation with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/msci-ecology-and-wildlife-conservation-with-professional-experience


#### Environment  ·  `environment`  ·  6 个项目

**UG · BSc** — 6 个

- BSc Environmental Management and Sustainability
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-management
- BSc Environmental Management and Sustainability with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-management-with-foundation
- BSc Environmental Management and Sustainability with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-management-with-placement-year
- BSc Environmental Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-science
- BSc Environmental Science with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-science-with-professional-experience
- BSc Environmental Science with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-science-with-study-year-abroad


#### Geography  ·  `geography`  ·  8 个项目

**UG · BSc** — 8 个

- BSc Geography (Human and Physical)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-and-physical-geography
- BSc Geography (Human and Physical) with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-and-physical-geography-with-professional-experience
- BSc Geography (Human)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-geography
- BSc Geography (Human) with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-geography-with-professional-experience
- BSc Geography (Physical)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-physical-geography
- BSc Geography (Physical) with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-physical-geography-with-professional-experience
- BSc Geography and Economics (Regional Science)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-geography-and-economics-regional-science
- BSc Geography and Economics (Regional Science) with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-geography-and-economics-regional-science-with-professional-experience


#### Geography and Environmental Science  ·  `geography-and-environmental-science`  ·  1 个项目

**PG · MSc** — 1 个

- MSc Environmental Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/geography-and-environmental-science-pg/msc-environmental-management


#### Meteorology and Climate  ·  `meteorology-and-climate`  ·  6 个项目

**PG · MSc** — 4 个

- MSc Applied Meteorology and Climate
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-applied-meteorology
- MSc Applied Meteorology and Climate with Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-applied-meteorology-and-climate-with-management
- MSc Atmosphere, Ocean and Climate
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-atmosphere-oceans-and-climate
- MSc Climate Change and Artificial Intelligence (AI)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-climate-change-and-artificial-intelligence

**UG · BSc** — 1 个

- BSc Meteorology and Climate
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-ug/bsc-meteorology-and-climate

**UG · MMet** — 1 个

- MMet Meteorology and Climate with a Year in Oklahoma
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-ug/mmet-meteorology-and-climate-with-a-year-in-oklahoma


### 1.x  School of Chemistry, Food and Pharmacy (SCFP)  ·  38 个项目

#### Chemistry  ·  `chemistry`  ·  8 个项目

**UG · BSc** — 8 个

- BSc Chemistry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry
- BSc Chemistry with Cosmetic Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-cosmetic-science
- BSc Chemistry with Cosmetic Science with a Year in Industry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-cosmetic-science-with-a-year-in-industry
- BSc Chemistry with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-foundation
- BSc Chemistry with a Year in Industry or Research
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-a-year-in-industry-research
- BSc Pharmaceutical Chemistry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-pharmaceutical-chemistry
- BSc Pharmaceutical Chemistry with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-pharmaceutical-chemistry-with-foundation
- BSc Pharmaceutical Chemistry with a Year in Industry or Research
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-pharmaceutical-chemistry-with-placement


#### Food and Nutrition  ·  `food-and-nutrition`  ·  9 个项目

**UG · BSc** — 9 个

- BSc Food Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-science
- BSc Food Science with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-science-with-foundation
- BSc Food Science with Industrial Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-science-with-industrial-training
- BSc Food Technology with Bioprocessing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-technology-with-bioprocessing
- BSc Food Technology with Bioprocessing with Industrial Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-technology-with-bioprocessing-with-industrial-training
- BSc Nutrition
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition
- BSc Nutrition and Food Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition-and-food-science
- BSc Nutrition and Food Science with Professional Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition-and-food-science-with-professional-training
- BSc Nutrition with Professional Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition-with-professional-training


#### Food and Nutritional Sciences  ·  `food-and-nutritional-sciences`  ·  4 个项目

**PG · MSc** — 4 个

- MSc Dietetics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-dietetics
- MSc Food Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-food-science
- MSc Food Technology – Quality Assurance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-food-technology-quality-assurance
- MSc Nutrition and Food Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-nutrition-and-food-science


#### Medical Sciences  ·  `medical-sciences`  ·  9 个项目

**UG · BSc** — 6 个

- BSc Medical Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-medical-science
- BSc Medical Science with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-medical-science-with-foundation
- BSc Medical Science with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-medical-science-with-professional-experience
- BSc Pharmacology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-pharmacology
- BSc Pharmacology with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-pharmacology-with-foundation
- BSc Pharmacology with a Year in Industry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-pharmacology-with-year-in-industry

**UG · MPAS** — 1 个

- MPAS Physician Associate Studies
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/mpas-physician-associate-studies

**UG · MSci** — 2 个

- MSci Medical Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/msci-medical-science
- MSci Medical Science with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/msci-medical-science-with-professional-experience


#### Pharmacy  ·  `pharmacy`  ·  8 个项目

**PG · Other** — 1 个

- Flexible CPD Advancing Healthcare Practice (Modular/PGDip/MSc)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/msc-advancing-healthcare-practice

**PG · PGCert** — 5 个

- PGCert Independent Prescribing for Allied Health Professionals
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-independent-supplementary-prescribing-allied
- PGCert Independent Prescribing for Pharmacists
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-independent-supplementary-prescribing-pharmacists
- PGCert Reflective Practice for Prescribers
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-reflective-practice-for-prescribers
- PGCert Work-Based Learning
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-work-based-learning
- PGCert-GradCert Independent Prescribing for Nurses (Levels 6 and 7)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-independent-supplementary-prescribing-nurses

**UG · MPharm** — 2 个

- MPharm Pharmacy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-ug/mpharm-pharmacy
- MPharm Pharmacy with Preparatory Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-ug/mpharm-pharmacy-with-preparatory-year


### 1.x  Institute of Education  ·  38 个项目

#### Education  ·  `education`  ·  38 个项目

**PG · MA** — 1 个

- MA Education
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/ma-education

**PG · Other** — 7 个

- Postgraduate Teacher Apprenticeship (Primary) + QTS with Postgraduate Certificate in Education
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-teacher-apprenticeship-primary
- Postgraduate Teacher Apprenticeship (Primary) + QTS with Professional Graduate Certificate in Education (PgCE)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/professional-graduate-certificate-teacher-apprenticeship-primary
- Postgraduate Teacher Apprenticeship (Secondary) + QTS with Postgraduate Certificate in Education
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-teacher-apprenticeship-secondary
- Postgraduate Teacher Apprenticeship (Secondary) + QTS with Professional Graduate Certificate in Education (PgCE)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/professional-graduate-certificate-teacher-apprenticeship-secondary
- Primary Professional Graduate Certificate in Education with QTS (PgCE)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/primary-professional-graduate-certificate-in-education-qts
- Primary Professional Graduate Certificate in Education with QTS (PgCE) (3-7)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/primary-professional-graduate-certificate-in-education-qts-early-years
- Primary Professional Graduate Certificate in Education with QTS (PgCE) with Special Educational Needs (SEN)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/primary-professional-graduate-certificate-in-education-qts-special-educational-needs

**PG · PGCE** — 19 个

- PGCE Early Years (EYTS)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgcert-early-years-practice
- PGCE Primary Postgraduate Certificate in Education
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-primary-education
- PGCE Primary Postgraduate Certificate in Education (3-7)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-primary-early-years
- PGCE Primary Postgraduate Certificate in Education with Special Educational Needs (SEN)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-primary-special-educational-needs
- PGCE Secondary Art and Design
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-art-and-design
- PGCE Secondary Design and Technology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-design-and-technology
- PGCE Secondary English
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-english
- PGCE Secondary Geography
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-geography
- PGCE Secondary History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-history
- PGCE Secondary Mathematics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-mathematics
- PGCE Secondary Modern Foreign Language - French
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-modern-languages-french
- PGCE Secondary Modern Foreign Language - German
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-modern-languages-german
- PGCE Secondary Modern Foreign Language - Spanish
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-modern-languages-spanish
- PGCE Secondary Physical Education
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-physical-education
- PGCE Secondary Science Physics with Mathematics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-physics-with-mathematics
- PGCE Secondary Science: Biology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-biology
- PGCE Secondary Science: Chemistry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-chemistry
- PGCE Secondary Science: Engineers Teach Physics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-engineers-teach-physics
- PGCE Secondary Science: Physics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-physics

**PG · Postgraduate Certificate in Education** — 1 个

- Postgraduate Certificate in Education (Reflective Practice)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-reflective-practice

**PG · Postgraduate Certificate in Healthcare Education** — 1 个

- Postgraduate Certificate in Healthcare Education
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgcert-healthcare-education

**UG · BA** — 8 个

- BA Children&#39;s Development and Learning
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-childrens-development-and-learning
- BA Education Studies
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-education-studies
- BA Education and Psychology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-education-and-psychology
- BA Primary Education (QTS)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education
- BA Primary Education with Art (QTS)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-art-specialism
- BA Primary Education with English (QTS)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-english-specialism
- BA Primary Education with Mathematics (QTS)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-mathematics-specialism
- BA Primary Education with Music (QTS)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-music-specialism

**UG · Foundation Degree** — 1 个

- Foundation Degree in Children&#39;s Development and Learning
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/foundation-degree-in-childrens-development-and-learning


### 1.x  School of Philosophy, Politics and Economics (SPPE)  ·  36 个项目

#### Economics  ·  `economics`  ·  11 个项目

**PG · MSc** — 4 个

- MSc Applied Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-applied-economics
- MSc Business Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-business-economics
- MSc Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-economics
- MSc Public Policy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-public-policy

**UG · BA** — 2 个

- BA Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/ba-economics
- BA Economics with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/ba-economics-with-placement-year

**UG · BSc** — 5 个

- BSc Business Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-business-economics
- BSc Business Economics with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-business-economics-with-placement-year
- BSc Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-economics
- BSc Economics and Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-economics-and-finance
- BSc Economics with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-economics-with-placement-year


#### Philosophy  ·  `philosophy`  ·  14 个项目

**PG · MA** — 1 个

- MA by Research Philosophy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-pg/ma-by-research-philosophy

**UG · BA** — 13 个

- BA Ethics, Value and Philosophy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ethics-value-and-philosophy
- BA Ethics, Value and Philosophy with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ethics-value-and-philosophy-with-placement
- BA Philosophy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy
- BA Philosophy and International Relations
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-international-relations
- BA Philosophy and International Relations with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-international-relations-with-placement
- BA Philosophy and Politics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-politics
- BA Philosophy and Politics with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-politics-with-placement
- BA Philosophy with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-with-placement
- BA Philosophy, Business and Ethics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-business-ethics
- BA Philosophy, Business and Ethics with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-business-ethics-with-placement
- BA Philosophy, Politics and Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ppe-philosophy-politics-and-economics
- BA Philosophy, Politics and Economics with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ppe-philosophy-politics-and-economics-with-placement
- BA Psychology and Philosophy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-psychology-and-philosophy


#### Politics and International Relations  ·  `politics`  ·  8 个项目

**UG · BA** — 8 个

- BA International Relations and Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-international-relations-and-economics
- BA International Relations and Economics with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-international-relations-and-economics-placement-year
- BA Politics and Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-economics
- BA Politics and Economics with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-economics-placement-year
- BA Politics and International Relations
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-international-relations
- BA Politics and International Relations with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-international-relations-with-placement-year
- BA War, Peace and International Relations
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-war-peace-and-international-relations
- BA War, Peace and International Relations with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-war-peace-and-international-relations-with-placement-year


#### Politics and International Relations  ·  `politics-and-international-relations`  ·  3 个项目

**PG · MA** — 2 个

- MA Conflict and International Security
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-and-international-relations-pg/ma-conflict-and-international-security
- MA International Relations and Diplomacy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-and-international-relations-pg/ma-international-relations-and-diplomacy

**PG · MRes** — 1 个

- MRes Politics and International Relations
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/politics-and-international-relations-pg/mres-politics-and-international-relations


### 1.x  School of Biological Sciences  ·  33 个项目

#### Biological Sciences  ·  `biological-sciences`  ·  24 个项目

**PG · MSc** — 4 个

- MSc Biotechnology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-biotechnology
- MSc Ecological Survey Skills with Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-ecological-survey-skills-with-placement
- MSc by Research Biomedicine
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-by-research-biomedicine
- MSc by Research Entomology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-by-research-entomology

**UG · BSc** — 12 个

- BSc Biochemistry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biochemistry
- BSc Biochemistry with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biochemistry-with-foundation
- BSc Biochemistry with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biochemistry-with-professional-experience
- BSc Biological Sciences
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biological-sciences
- BSc Biological Sciences with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biological-sciences-with-foundation
- BSc Biological Sciences with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biological-sciences-with-professional-experience
- BSc Biomedical Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biomedical-science
- BSc Biomedical Science with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biomedical-science-with-foundation
- BSc Biomedical Science with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biomedical-science-with-professional-experience
- BSc Microbiology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-microbiology
- BSc Microbiology with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-microbiology-with-foundation
- BSc Microbiology with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-microbiology-with-professional-experience

**UG · MSci** — 8 个

- MSci Biochemistry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biochemistry
- MSci Biochemistry with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biochemistry-with-professional-experience
- MSci Biological Sciences
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biological-sciences
- MSci Biological Sciences with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biological-sciences-with-professional-experience
- MSci Biomedical Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biomedical-science
- MSci Biomedical Science with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biomedical-science-with-professional-experience
- MSci Microbiology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-microbiology
- MSci Microbiology with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-microbiology-with-professional-experience


#### Biomedical Engineering  ·  `biomedical-engineering`  ·  2 个项目

**UG · BEng** — 2 个

- BEng Biomedical Engineering
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biomedical-engineering-ug/beng-biomedical-engineering
- BEng Biomedical Engineering with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/biomedical-engineering-ug/beng-biomedical-engineering-with-professional-experience


#### Bioveterinary Sciences  ·  `bioveterinary-sciences`  ·  2 个项目

**UG · BSc** — 2 个

- BSc Bioveterinary Sciences
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/bioveterinary-sciences-ug/bsc-bioveterinary-sciences
- BSc Bioveterinary Sciences with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/bioveterinary-sciences-ug/bsc-bioveterinary-sciences-with-placement-year


#### Zoology  ·  `zoology`  ·  5 个项目

**UG · BSc** — 3 个

- BSc Zoology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/bsc-zoology
- BSc Zoology with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/bsc-zoology-with-foundation
- BSc Zoology with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/bsc-zoology-with-professional-experience

**UG · MSci** — 2 个

- MSci Zoology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/msci-zoology
- MSci Zoology with Professional Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/msci-zoology-with-professional-experience


### 1.x  School of Humanities  ·  25 个项目

#### Ancient History  ·  `ancient-history`  ·  5 个项目

**UG · BA** — 5 个

- BA Ancient History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history
- BA Ancient History and Archaeology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-archaeology
- BA Ancient History and Archaeology with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-archaeology-with-professional-placement
- BA Ancient History and Archaeology with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-archaeology-with-study-year-abroad
- BA Ancient History and History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-history


#### Classics and Classical Studies  ·  `classics`  ·  3 个项目

**UG · BA** — 3 个

- BA Classical Studies
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/classics-ug/ba-classical-studies
- BA Classical Studies and English Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/classics-ug/ba-classical-studies-and-english-literature
- BA Classics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/classics-ug/ba-classics


#### Classics and Ancient History  ·  `classics-and-ancient-history`  ·  1 个项目

**PG · MA** — 1 个

- MA Classics and Ancient History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/classics-and-ancient-history-pg/ma-classics-and-ancient-history


#### English Literature  ·  `english-literature`  ·  6 个项目

**PG · MA** — 1 个

- MA English Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-pg/ma-english-literature

**UG · BA** — 5 个

- BA English Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature
- BA English Literature and Film
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-and-film
- BA English Literature and Film &amp; Theatre
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-and-film-and-theatre
- BA English Literature and Politics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-and-politics
- BA English Literature with Creative Writing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-with-creative-writing


#### Global Sustainable Development  ·  `global-sustainable-development`  ·  2 个项目

**UG · BSc** — 2 个

- BSc Global Sustainable Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/global-sustainable-development-ug/bsc-global-sustainable-development
- BSc Global Sustainable Development with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/global-sustainable-development-ug/bsc-global-sustainable-development-with-placement-year


#### History  ·  `history`  ·  7 个项目

**PG · MA** — 1 个

- MA History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-pg/ma-history

**UG · BA** — 6 个

- BA History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history
- BA History and Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-economics
- BA History and English Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-english-literature
- BA History and International Relations
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-international-relations
- BA History and Philosophy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-philosophy
- BA History and Politics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-politics


#### Museum Studies  ·  `museum-studies`  ·  1 个项目

**UG · BA** — 1 个

- BA Museum and Classical Studies
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/museum-studies-ug/ba-museum-and-classical-studies


### 1.x  School of the Built Environment (SBE)  ·  24 个项目

#### Architectural Engineering  ·  `architectural-engineering`  ·  2 个项目

**UG · BEng** — 1 个

- BEng Architectural Engineering
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/architectural-engineering-ug/beng-architectural-engineering

**UG · MEng** — 1 个

- MEng Architectural Engineering
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/architectural-engineering-ug/meng-architectural-engineering


#### Construction Management and Engineering  ·  `construction-management-and-engineering`  ·  7 个项目

**PG · MSc** — 7 个

- MSc Construction Cost Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-construction-cost-management
- MSc Construction Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-construction-management
- MSc Construction Management with Industry Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-construction-management-with-industry-placement
- MSc Design and Management of Sustainable Built Environments
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-design-and-management-of-sustainable-built-environment
- MSc Project Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-project-management
- MSc Project Management with Industry Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-project-management-with-industry-placement
- MSc Renewable Energy: Technology and Sustainability
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-renewable-energy-technology-and-sustainability


#### Real Estate and Planning  ·  `real-estate-and-planning`  ·  11 个项目

**PG · MSc** — 5 个

- MSc Real Estate
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate
- MSc Real Estate - Flexible
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate-flexible
- MSc Real Estate Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate-finance
- MSc Real Estate Investment and Finance - Flexible
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate-investment-and-finance-flexible
- MSc Spatial Planning and Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-spatial-planning-and-development

**UG · BSc** — 4 个

- BSc Planning and Geography
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-planning-and-geography
- BSc Real Estate
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-real-estate
- BSc Real Estate Development and Planning
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-real-estate-development-and-planning
- BSc Real Estate Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-real-estate-finance

**UG · MPlan** — 2 个

- MPlan Planning and Geography
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/mplan-planning-and-geography
- MPlan Real Estate Development and Planning
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/mplan-real-estate-development-and-planning


#### Surveying and Construction Management  ·  `surveying-and-construction-management`  ·  4 个项目

**UG · BSc** — 4 个

- BSc Building Surveying
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-building-surveying
- BSc Construction Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-construction-management
- BSc Construction Management and Surveying
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-construction-management-and-surveying
- BSc Quantity Surveying
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-quantity-surveying


### 1.x  School of Arts and Communication Design (SACD)  ·  22 个项目

#### Art  ·  `art`  ·  9 个项目

**PG · MA** — 1 个

- MA Fine Art
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-pg/master-in-fine-art-ma

**UG · BA** — 8 个

- BA Art
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art
- BA Art and Creative Writing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-creative-writing
- BA Art and English Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-english-literature
- BA Art and Film
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-film
- BA Art and History of Art
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-history-of-art
- BA Art and Philosophy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-philosophy
- BA Art and Psychology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-psychology
- BA Fine Art
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-fine-art


#### Creative Writing  ·  `creative-writing`  ·  2 个项目

**UG · BA** — 2 个

- BA Creative Writing and Film
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/creative-writing-ug/ba-creative-writing-and-film
- BA Creative Writing and Film &amp; Theatre
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/creative-writing-ug/ba-creative-writing-and-film-and-theatre


#### Film and Television  ·  `film-and-television`  ·  3 个项目

**UG · BA** — 3 个

- BA Acting and Performance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/film-and-television-ug/ba-acting-and-performance
- BA Film and Television
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/film-and-television-ug/ba-film
- BA Film and Theatre
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/film-and-television-ug/ba-film-and-theatre


#### Film, Theatre and Television  ·  `film-theatre-and-television`  ·  1 个项目

**PG · MA** — 1 个

- MA by Research Film, Theatre and Television
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/film-theatre-and-television-pg/ma-by-research-film-theatre-television


#### Graphic Communication and Design  ·  `graphic-communication-and-design`  ·  1 个项目

**UG · BA** — 1 个

- BA Graphic Communication
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/graphic-communication-and-design-ug/ba-graphic-communication


#### Typography and Graphic Communication  ·  `typography-and-graphic-communication`  ·  6 个项目

**PG · MA** — 5 个

- MA Communication Design: Book Design Pathway
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-book-design
- MA Communication Design: Graphic Design Pathway
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-graphic-design
- MA Communication Design: Information Design Pathway
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-information-design
- MA Communication Design: Typeface Design Pathway
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-typeface-design
- MA by Research Typography and Graphic Communication
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-by-research-typography-and-graphic-communication

**PG · MRes** — 1 个

- MRes Typeface Design
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/mres-typeface-design


### 1.x  School of Psychology and Clinical Language Sciences  ·  20 个项目

#### Physician Associate  ·  `physician-associate`  ·  1 个项目

**PG · MSc** — 1 个

- MSc Physician Associate
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/physician-associate-pg/msc-physician-associate


#### Psychology  ·  `psychology`  ·  17 个项目

**PG · MSc** — 4 个

- MSc Cognitive Neuroscience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-cognitive-neuroscience
- MSc Psychology Conversion
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-psychology-conversion
- MSc Research Methods in Psychology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-research-methods-in-psychology
- MSc Theory and Practice in Clinical Psychology (with clinical or research placement)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-theory-and-practice-in-clinical-psychology

**PG · Other** — 3 个

- GradCert/PGCert Psychological Wellbeing Practitioner Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/pgcert-psychological-wellbeing-practitioner-training
- Postgraduate and Graduate Diplomas in Children&#39;s Wellbeing Practitioner Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/graduate-pgdip-childrens-wellbeing-practitioner-training
- Postgraduate and Graduate Diplomas in Education Mental Health Practitioner Training
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/graduate-pgdip-education-mental-health-practitioner-training

**PG · PGDip** — 2 个

- PGDip Evidence-Based Psychological Treatment (High Intensity)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/pgdip-evidence-based-psychological-treatment-high-intensity
- PGDip Evidence-Based Psychological Treatment for Children and Young People (High Intensity)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/pgdip-evidence-based-psychological-treatment-for-children-young-people

**UG · BSc** — 7 个

- BSc Psychology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology
- BSc Psychology and Language Sciences
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-language-sciences-and-psychology
- BSc Psychology with Criminology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-criminology
- BSc Psychology with Criminology with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-criminology-with-professional-placement-year
- BSc Psychology with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-foundation
- BSc Psychology with Neuroscience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-neuroscience
- BSc Psychology with Professional Placement
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-professional-placement

**UG · MSci** — 1 个

- MSci Applied Psychology (Clinical)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/msci-applied-psychology-clinical


#### Speech and Language Therapy  ·  `speech-and-language-therapy`  ·  2 个项目

**PG · MSc** — 2 个

- MSc Language Sciences
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/speech-and-language-therapy-pg/msc-language-sciences
- MSc Speech and Language Therapy
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/speech-and-language-therapy-pg/msc-speech-and-language-therapy


### 1.x  School of Law  ·  20 个项目

#### Law  ·  `law`  ·  20 个项目

**PG · Conversion** — 1 个

- Conversion programmes in Law
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/law-conversion

**PG · LLM** — 7 个

- LLM Advanced Legal Studies
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-advanced-legal-studies
- LLM International Commercial Law
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law
- LLM International Commercial Law with Intellectual Property Law and Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law-with-intellectual-property-law-and-management
- LLM International Commercial Law with International Banking Law and Financial Regulation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law-with-international-banking-law-and-financial-regulation
- LLM International Commercial Law with International Corporate Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law-with-corporate-finance
- LLM International Law
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-law
- LLM Research Thesis
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-research-thesis

**PG · LPC** — 1 个

- LPC Legal Practice Course
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/lpc-legal-practice-course

**PG · MRes** — 1 个

- MRes Law
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/mres-law

**UG · BSc** — 4 个

- BSc Criminology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology
- BSc Criminology with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology-with-foundation-year
- BSc Criminology with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology-with-placement-year
- BSc Criminology with Study Year Abroad
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology-with-year-abroad

**UG · LLB** — 5 个

- LLB Law
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law
- LLB Law with Criminology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-with-criminology
- LLB Law with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-with-foundation
- LLB Law with International Business
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-with-international-business
- LLB Law with International Foundation Year - September entry
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-international-foundation-year

**UG · MLaw** — 1 个

- MLaw MLaw
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/mlaw


### 1.x  School of Mathematical, Physical and Computational Sciences (SMPCS)  ·  17 个项目

#### Computer Science  ·  `computer-science`  ·  7 个项目

**PG · MSc** — 2 个

- MSc Applied Artificial Intelligence for Business
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-pg/msc-applied-ai-for-business
- MSc Data Science and Advanced Computing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-pg/msc-data-science-and-advanced-computing

**UG · BSc** — 5 个

- BSc Computer Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science
- BSc Computer Science with Artificial Intelligence (awaiting approval)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-artificial-intelligence
- BSc Computer Science with Artificial Intelligence with Industrial Year (awaiting approval)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-artificial-intelligence-with-industrial-year
- BSc Computer Science with Artificial Intelligence with Study Year Abroad (awaiting approval)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-artificial-intelligence-with-study-year-abroad
- BSc Computer Science with Industrial Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-industrial-year


#### Mathematics  ·  `mathematics`  ·  10 个项目

**UG · BSc** — 8 个

- BSc Mathematics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics
- BSc Mathematics and Statistics with Data Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-and-statistics-with-data-science
- BSc Mathematics and Statistics with Data Science with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-and-statistics-with-data-science-with-placement-year
- BSc Mathematics with Computer Science
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-computer-science
- BSc Mathematics with Computer Science with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-computer-science-with-a-placement-year
- BSc Mathematics with Finance and Investment Banking
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-finance-and-investment-banking
- BSc Mathematics with Finance and Investment Banking with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-finance-and-investment-banking-with-a-placement-year
- BSc Mathematics with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-placement-year

**UG · MMath** — 2 个

- MMath Mathematics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/mmath-mathematics
- MMath Mathematics with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/mmath-mathematics-with-a-placement-year


### 1.x  Graduate Institute of International Development, Agriculture and Economics (GIIDAE)  ·  11 个项目

#### International Development and Applied Economics (GIIDAE)  ·  `international-development-and-applied-economics`  ·  11 个项目

**PG · MRes** — 1 个

- MRes Agricultural and Food Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/mres-agricultural-and-food-economics

**PG · MSc** — 10 个

- MSc Agricultural Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-agricultural-economics
- MSc Agriculture and Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-agriculture-and-development
- MSc Applied International Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-applied-international-development
- MSc Communication for Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-communication-for-development
- MSc Consumer Behaviour
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-consumer-behaviour
- MSc Development Finance
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-development-finance
- MSc Environment, Climate Change and Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-climate-change-and-development
- MSc Food Economics and Marketing
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-food-economics-and-marketing
- MSc Food Security and Development
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-food-security-and-development
- MSc by Research Agricultural Science and Sustainability
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-by-research-in-agricultural-science-and-sustainability


### 1.x  School of Languages and Cultures  ·  8 个项目

#### Languages and Cultures  ·  `languages-and-cultures`  ·  8 个项目

**UG · BA** — 8 个

- BA Modern Languages (3 years)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-three-years
- BA Modern Languages (4 years)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages
- BA Modern Languages and Business
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-business
- BA Modern Languages and Economics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-economics
- BA Modern Languages and English Language
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-english-language
- BA Modern Languages and English Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-english-literature
- BA Modern Languages and History
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-history
- BA Modern Languages and International Relations
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-international-relations


### 1.x  School of Humanities (English Language)  ·  7 个项目

#### English Language and Applied Linguistics  ·  `english-language-and-applied-linguistics`  ·  7 个项目

**PG · MA** — 2 个

- MA Applied Linguistics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-pg/ma-in-applied-linguistics
- MA Teaching English to Speakers of Other Languages (TESOL)
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-pg/ma-teaching-english-to-speakers-of-other-languages-tesol

**PG · PGCert** — 1 个

- PGCert in Language Assessment
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-pg/pgcert-language-assessment

**UG · BA** — 4 个

- BA Digital Media and Communication
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-digital-media-and-communication
- BA English Language and Linguistics
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-english-language-and-linguistics
- BA English Language and Linguistics with Placement Experience
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-english-language-and-linguistics-with-placement
- BA English Language and Literature
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-english-language-and-literature


### 1.x  Other / Unclassified  ·  5 个项目

#### Agriculture  ·  `agriculture`  ·  5 个项目

**UG · BSc** — 5 个

- BSc Agricultural Business Management
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agricultural-business-management
- BSc Agricultural Business Management with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agricultural-business-management-with-placement-year
- BSc Agriculture
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agriculture
- BSc Agriculture with Foundation
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agriculture-with-foundation
- BSc Agriculture with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agriculture-with-placement-year


### 1.x  School of Humanities (Sociology)  ·  4 个项目

#### Sociology  ·  `sociology`  ·  4 个项目

**UG · BSc** — 4 个

- BSc Sociology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology
- BSc Sociology and Criminology
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology-and-criminology
- BSc Sociology and Criminology with a Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology-and-criminology-with-placement-year
- BSc Sociology with Placement Year
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology-with-placement-year


### 1.x  School of Construction Management and Engineering (CME) / Architecture  ·  2 个项目

#### Architecture  ·  `architecture`  ·  2 个项目

**PG · Master of Architecture** — 1 个

- Master of Architecture
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/architecture-pg/master-of-architecture

**UG · BSc** — 1 个

- BSc Architecture
  - 详情：https://www.reading.ac.uk/ready-to-study/study/2026/architecture-ug/bsc-architecture

## § 2 全量专业明细（专业 → 学院 → 学位级别）

> 466 行专业级明细。一行一专业，可被任意 weaviate/chroma 按 (college, level, degree_prefix) 过滤。

### 2.1 Undergraduate Programmes (322)

| # | 学院 | 学科领域 | 学位 | 项目名称 | URL |
|---:|---|---|---|---|---|
| 1 | Global Academy | Foundation Programmes | BA | BA English Language and Linguistics with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/ba-english-language-and-linguistics-with-foundation) |
| 2 | Global Academy | Foundation Programmes | BA | BA English Literature with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/ba-english-literature-with-foundation) |
| 3 | Global Academy | Foundation Programmes | BSc | BSc Accounting and Management with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-accounting-and-management-with-foundation) |
| 4 | Global Academy | Foundation Programmes | BSc | BSc Agricultural Business Management with Foundation Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-agricultural-business-management-with-foundation) |
| 5 | Global Academy | Foundation Programmes | BSc | BSc Bioveterinary Sciences with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-bioveterinary-sciences-with-foundation) |
| 6 | Global Academy | Foundation Programmes | BSc | BSc Business and Management with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-business-and-management-with-foundation) |
| 7 | Global Academy | Foundation Programmes | BSc | BSc Chemistry with Cosmetic Science with Foundation Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-chemistry-with-cosmetic-science-with-foundation) |
| 8 | Global Academy | Foundation Programmes | BSc | BSc Consumer Behaviour and Marketing with Foundation Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-consumer-behaviour-and-marketing-with-foundation) |
| 9 | Global Academy | Foundation Programmes | BSc | BSc Finance with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-finance-with-foundation) |
| 10 | Global Academy | Foundation Programmes | BSc | BSc Food Business and Marketing with Foundation Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-food-marketing-and-business-economics-with-foundation) |
| 11 | Global Academy | Foundation Programmes | BSc | BSc Nutrition with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-nutrition-with-foundation) |
| 12 | Global Academy | Foundation Programmes | BSc | BSc Real Estate with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/foundation-programmes-ug/bsc-real-estate-with-foundation) |
| 13 | Global Academy | International Foundation Pathways | BA | BA Economics with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-economics-ifp-january) |
| 14 | Global Academy | International Foundation Pathways | BA | BA Economics with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-economics-ifp-september) |
| 15 | Global Academy | International Foundation Pathways | BA | BA Museum Studies and Archaeology with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-museum-studies-and-archaeology-ifp-september) |
| 16 | Global Academy | International Foundation Pathways | BA | BA Politics and International Relations with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/ba-politics-and-international-relations-ifp-september) |
| 17 | Global Academy | International Foundation Pathways | BEng | BEng Architectural Engineering with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/beng-architectural-engineering-ifp-september) |
| 18 | Global Academy | International Foundation Pathways | BSc | BSc Agricultural Business Management with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-agricultural-business-management-ifp-january) |
| 19 | Global Academy | International Foundation Pathways | BSc | BSc Agricultural Business Management with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-agricultural-business-management-ifp-september) |
| 20 | Global Academy | International Foundation Pathways | BSc | BSc Agriculture with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-agriculture-ifp-september) |
| 21 | Global Academy | International Foundation Pathways | BSc | BSc Building Surveying with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-building-surveying-ifp-january) |
| 22 | Global Academy | International Foundation Pathways | BSc | BSc Building Surveying with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-building-surveying-ifp-september) |
| 23 | Global Academy | International Foundation Pathways | BSc | BSc Computer Science with Artificial Intelligence with International Foundation Year (awaiting approval) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-computer-science-with-artificial-intelligence-with-international-foundation-year-september) |
| 24 | Global Academy | International Foundation Pathways | BSc | BSc Construction Management and Surveying with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-and-surveying-ifp-january) |
| 25 | Global Academy | International Foundation Pathways | BSc | BSc Construction Management and Surveying with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-and-surveying-ifp-september) |
| 26 | Global Academy | International Foundation Pathways | BSc | BSc Construction Management with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-ifp-january) |
| 27 | Global Academy | International Foundation Pathways | BSc | BSc Construction Management with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-construction-management-ifp-september) |
| 28 | Global Academy | International Foundation Pathways | BSc | BSc Consumer Behaviour and Marketing with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-consumer-behaviour-and-marketing-ifp-january) |
| 29 | Global Academy | International Foundation Pathways | BSc | BSc Consumer Behaviour and Marketing with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-consumer-behaviour-and-marketing-ifp-september) |
| 30 | Global Academy | International Foundation Pathways | BSc | BSc Economics and Finance with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-economics-and-finance-ifp-january) |
| 31 | Global Academy | International Foundation Pathways | BSc | BSc Economics and Finance with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-economics-and-finance-ifp-september) |
| 32 | Global Academy | International Foundation Pathways | BSc | BSc Environmental Science with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-environmental-science-ifp-september) |
| 33 | Global Academy | International Foundation Pathways | BSc | BSc Food Business and Marketing with International Foundation Year - January entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-food-business-and-marketing-ifp-january) |
| 34 | Global Academy | International Foundation Pathways | BSc | BSc Food Business and Marketing with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-food-business-and-marketing-ifp-september) |
| 35 | Global Academy | International Foundation Pathways | BSc | BSc Mathematics with Finance and Investment Banking with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-mathematics-with-finance-and-investment-banking-ifp-september) |
| 36 | Global Academy | International Foundation Pathways | BSc | BSc Mathematics with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-mathematics-ifp-september) |
| 37 | Global Academy | International Foundation Pathways | BSc | BSc Meteorology and Climate with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-meteorology-and-climate-ifp-september) |
| 38 | Global Academy | International Foundation Pathways | BSc | BSc Psychology with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-psychology-ifp-september) |
| 39 | Global Academy | International Foundation Pathways | BSc | BSc Quantity Surveying with International Foundation Year - January Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-quantity-surveying-ifp-january) |
| 40 | Global Academy | International Foundation Pathways | BSc | BSc Quantity Surveying with International Foundation Year - September Entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/bsc-quantity-surveying-ifp-september) |
| 41 | Global Academy | International Foundation Pathways | IFP | IFP International Foundation Programme - January | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/international-foundation-pathways-january-entry) |
| 42 | Global Academy | International Foundation Pathways | IFP | IFP International Foundation Programme - September | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-foundation-pathways-ug/international-foundation-pathways-september-entry) |
| 43 | Henley Business School | Business, Management, Accounting and Finance | BA | BA Accounting (Beijing Institute of Technology) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/ba-accounting-beijing) |
| 44 | Henley Business School | Business, Management, Accounting and Finance | BA | BA International Business Management (SQA Advanced Diploma students in China) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/ba-international-business-management-sqa-china) |
| 45 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Business – The Flying Start Degree Programme | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-business) |
| 46 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-finance) |
| 47 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Finance with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-finance-with-placement-experience) |
| 48 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Finance with Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-finance-with-year-abroad) |
| 49 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-management) |
| 50 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Management with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-management-with-placement-experience) |
| 51 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Accounting and Management with Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-accounting-and-management-with-year-abroad) |
| 52 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management) |
| 53 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Data Analytics and Digital Business) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-data-analytics-and-digital-business) |
| 54 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Data Analytics and Digital Business) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-data-analytics-and-digital-business-with-placement-year) |
| 55 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Data Analytics and Digital Business) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-data-analytics-and-digital-business-with-study-year-abroad) |
| 56 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Entrepreneurship and Innovation) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-entrepreneurship) |
| 57 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Entrepreneurship and Innovation) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-entrepreneurship-with-placement-year) |
| 58 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Entrepreneurship and Innovation) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-entrepreneurship-with-study-year-abroad) |
| 59 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Human Resources and Organisational Behaviour) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-human-resources) |
| 60 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Human Resources and Organisational Behaviour) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-human-resources-with-placement-year) |
| 61 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Human Resources and Organisational Behaviour) with Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-human-resources-with-year-abroad) |
| 62 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (MUST 2+2 programme) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/macau-university-of-science-and-technology) |
| 63 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Marketing) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-marketing) |
| 64 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Marketing) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-marketing-with-placement-year) |
| 65 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management (Marketing) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-marketing-with-study-year-abroad) |
| 66 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-with-placement-year) |
| 67 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Business and Management with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-business-and-management-with-study-year-abroad) |
| 68 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance) |
| 69 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (FinTech) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-fintech) |
| 70 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (FinTech) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-fintech-with-placement-year) |
| 71 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (FinTech) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-fintech-with-study-year-abroad) |
| 72 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (International Business) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-international-business) |
| 73 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (International Business) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-international-business-with-placement-year) |
| 74 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (International Business) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-international-business-with-study-year-abroad) |
| 75 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (Investments) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-investments) |
| 76 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (Investments) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-investments-with-placement) |
| 77 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (Investments) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-investments-with-study-year-abroad) |
| 78 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (Sustainable Finance) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-sustainable-finance) |
| 79 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (Sustainable Finance) with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-sustainable-finance-placement-year) |
| 80 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance (Sustainable Finance) with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-sustainable-finance-study-year-abroad) |
| 81 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-with-placement-year) |
| 82 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc Finance with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-finance-with-study-year-abroad) |
| 83 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc International Business and Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management) |
| 84 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc International Business and Management with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-placement-year) |
| 85 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc International Business and Management with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-study-year-abroad) |
| 86 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc International Business and Management with a Modern Language | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-modern-language) |
| 87 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc International Business and Management with a Modern Language with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-modern-language-with-placement-year) |
| 88 | Henley Business School | Business, Management, Accounting and Finance | BSc | BSc International Business and Management with a Modern Language with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-and-management-accounting-and-finance-ug/bsc-international-business-and-management-with-modern-language-with-study-year-abroad) |
| 89 | Henley Business School | Marketing | BSc | BSc Consumer Behaviour and Marketing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-consumer-behaviour-and-marketing) |
| 90 | Henley Business School | Marketing | BSc | BSc Consumer Behaviour and Marketing with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-consumer-behaviour-and-marketing-with-placement-year) |
| 91 | Henley Business School | Marketing | BSc | BSc Food Business and Marketing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-food-business-and-marketing) |
| 92 | Henley Business School | Marketing | BSc | BSc Food Business and Marketing with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/marketing-ug/bsc-food-business-and-marketing-with-placement-year) |
| 93 | Institute of Education | Education | BA | BA Children&#39;s Development and Learning | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-childrens-development-and-learning) |
| 94 | Institute of Education | Education | BA | BA Education Studies | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-education-studies) |
| 95 | Institute of Education | Education | BA | BA Education and Psychology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-education-and-psychology) |
| 96 | Institute of Education | Education | BA | BA Primary Education (QTS) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education) |
| 97 | Institute of Education | Education | BA | BA Primary Education with Art (QTS) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-art-specialism) |
| 98 | Institute of Education | Education | BA | BA Primary Education with English (QTS) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-english-specialism) |
| 99 | Institute of Education | Education | BA | BA Primary Education with Mathematics (QTS) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-mathematics-specialism) |
| 100 | Institute of Education | Education | BA | BA Primary Education with Music (QTS) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/ba-qts-primary-education-with-music-specialism) |
| 101 | Institute of Education | Education | Foundation Degree | Foundation Degree in Children&#39;s Development and Learning | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-ug/foundation-degree-in-childrens-development-and-learning) |
| 102 | Other | Agriculture | BSc | BSc Agricultural Business Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agricultural-business-management) |
| 103 | Other | Agriculture | BSc | BSc Agricultural Business Management with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agricultural-business-management-with-placement-year) |
| 104 | Other | Agriculture | BSc | BSc Agriculture | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agriculture) |
| 105 | Other | Agriculture | BSc | BSc Agriculture with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agriculture-with-foundation) |
| 106 | Other | Agriculture | BSc | BSc Agriculture with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/agriculture-ug/bsc-agriculture-with-placement-year) |
| 107 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology) |
| 108 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology and Anthropology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-anthropology) |
| 109 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology and Anthropology with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-anthropology-with-professional-placement) |
| 110 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology and Anthropology with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-anthropology-with-study-year-abroad) |
| 111 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology and History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-history) |
| 112 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology and History with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-history-with-professional-experience) |
| 113 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology and History with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-and-history-with-study-year-abroad) |
| 114 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-with-professional-experience) |
| 115 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Archaeology with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-archaeology-with-study-abroad-year) |
| 116 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Museum Studies and Archaeology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-museum-studies-and-archaeology) |
| 117 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Museum Studies and Archaeology with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-museum-studies-and-archaeology-with-professional-experience) |
| 118 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | BA | BA Museum Studies and Archaeology with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-ug/ba-museum-studies-and-archaeology-with-study-year-abroad) |
| 119 | School of Archaeology, Geography and Environmental Science (SAGES) | Ecology | BSc | BSc Ecology and Wildlife Conservation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/bsc-ecology-and-wildlife-conservation) |
| 120 | School of Archaeology, Geography and Environmental Science (SAGES) | Ecology | BSc | BSc Ecology and Wildlife Conservation with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/bsc-ecology-and-wildlife-conservation-with-foundation) |
| 121 | School of Archaeology, Geography and Environmental Science (SAGES) | Ecology | BSc | BSc Ecology and Wildlife Conservation with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/bsc-ecology-and-wildlife-conservation-with-professional-experience) |
| 122 | School of Archaeology, Geography and Environmental Science (SAGES) | Ecology | MSci | MSci Ecology and Wildlife Conservation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/msci-ecology-and-wildlife-conservation) |
| 123 | School of Archaeology, Geography and Environmental Science (SAGES) | Ecology | MSci | MSci Ecology and Wildlife Conservation with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ecology-ug/msci-ecology-and-wildlife-conservation-with-professional-experience) |
| 124 | School of Archaeology, Geography and Environmental Science (SAGES) | Environment | BSc | BSc Environmental Management and Sustainability | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-management) |
| 125 | School of Archaeology, Geography and Environmental Science (SAGES) | Environment | BSc | BSc Environmental Management and Sustainability with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-management-with-foundation) |
| 126 | School of Archaeology, Geography and Environmental Science (SAGES) | Environment | BSc | BSc Environmental Management and Sustainability with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-management-with-placement-year) |
| 127 | School of Archaeology, Geography and Environmental Science (SAGES) | Environment | BSc | BSc Environmental Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-science) |
| 128 | School of Archaeology, Geography and Environmental Science (SAGES) | Environment | BSc | BSc Environmental Science with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-science-with-professional-experience) |
| 129 | School of Archaeology, Geography and Environmental Science (SAGES) | Environment | BSc | BSc Environmental Science with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/environment-ug/bsc-environmental-science-with-study-year-abroad) |
| 130 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography (Human and Physical) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-and-physical-geography) |
| 131 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography (Human and Physical) with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-and-physical-geography-with-professional-experience) |
| 132 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography (Human) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-geography) |
| 133 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography (Human) with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-human-geography-with-professional-experience) |
| 134 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography (Physical) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-physical-geography) |
| 135 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography (Physical) with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-physical-geography-with-professional-experience) |
| 136 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography and Economics (Regional Science) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-geography-and-economics-regional-science) |
| 137 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography | BSc | BSc Geography and Economics (Regional Science) with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-ug/bsc-geography-and-economics-regional-science-with-professional-experience) |
| 138 | School of Archaeology, Geography and Environmental Science (SAGES) | Meteorology and Climate | BSc | BSc Meteorology and Climate | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-ug/bsc-meteorology-and-climate) |
| 139 | School of Archaeology, Geography and Environmental Science (SAGES) | Meteorology and Climate | MMet | MMet Meteorology and Climate with a Year in Oklahoma | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-ug/mmet-meteorology-and-climate-with-a-year-in-oklahoma) |
| 140 | School of Arts and Communication Design (SACD) | Art | BA | BA Art | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art) |
| 141 | School of Arts and Communication Design (SACD) | Art | BA | BA Art and Creative Writing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-creative-writing) |
| 142 | School of Arts and Communication Design (SACD) | Art | BA | BA Art and English Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-english-literature) |
| 143 | School of Arts and Communication Design (SACD) | Art | BA | BA Art and Film | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-film) |
| 144 | School of Arts and Communication Design (SACD) | Art | BA | BA Art and History of Art | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-history-of-art) |
| 145 | School of Arts and Communication Design (SACD) | Art | BA | BA Art and Philosophy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-philosophy) |
| 146 | School of Arts and Communication Design (SACD) | Art | BA | BA Art and Psychology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-art-and-psychology) |
| 147 | School of Arts and Communication Design (SACD) | Art | BA | BA Fine Art | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-ug/ba-fine-art) |
| 148 | School of Arts and Communication Design (SACD) | Creative Writing | BA | BA Creative Writing and Film | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/creative-writing-ug/ba-creative-writing-and-film) |
| 149 | School of Arts and Communication Design (SACD) | Creative Writing | BA | BA Creative Writing and Film &amp; Theatre | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/creative-writing-ug/ba-creative-writing-and-film-and-theatre) |
| 150 | School of Arts and Communication Design (SACD) | Film and Television | BA | BA Acting and Performance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/film-and-television-ug/ba-acting-and-performance) |
| 151 | School of Arts and Communication Design (SACD) | Film and Television | BA | BA Film and Television | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/film-and-television-ug/ba-film) |
| 152 | School of Arts and Communication Design (SACD) | Film and Television | BA | BA Film and Theatre | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/film-and-television-ug/ba-film-and-theatre) |
| 153 | School of Arts and Communication Design (SACD) | Graphic Communication and Design | BA | BA Graphic Communication | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/graphic-communication-and-design-ug/ba-graphic-communication) |
| 154 | School of Biological Sciences | Biological Sciences | BSc | BSc Biochemistry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biochemistry) |
| 155 | School of Biological Sciences | Biological Sciences | BSc | BSc Biochemistry with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biochemistry-with-foundation) |
| 156 | School of Biological Sciences | Biological Sciences | BSc | BSc Biochemistry with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biochemistry-with-professional-experience) |
| 157 | School of Biological Sciences | Biological Sciences | BSc | BSc Biological Sciences | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biological-sciences) |
| 158 | School of Biological Sciences | Biological Sciences | BSc | BSc Biological Sciences with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biological-sciences-with-foundation) |
| 159 | School of Biological Sciences | Biological Sciences | BSc | BSc Biological Sciences with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biological-sciences-with-professional-experience) |
| 160 | School of Biological Sciences | Biological Sciences | BSc | BSc Biomedical Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biomedical-science) |
| 161 | School of Biological Sciences | Biological Sciences | BSc | BSc Biomedical Science with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biomedical-science-with-foundation) |
| 162 | School of Biological Sciences | Biological Sciences | BSc | BSc Biomedical Science with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-biomedical-science-with-professional-experience) |
| 163 | School of Biological Sciences | Biological Sciences | BSc | BSc Microbiology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-microbiology) |
| 164 | School of Biological Sciences | Biological Sciences | BSc | BSc Microbiology with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-microbiology-with-foundation) |
| 165 | School of Biological Sciences | Biological Sciences | BSc | BSc Microbiology with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/bsc-microbiology-with-professional-experience) |
| 166 | School of Biological Sciences | Biological Sciences | MSci | MSci Biochemistry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biochemistry) |
| 167 | School of Biological Sciences | Biological Sciences | MSci | MSci Biochemistry with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biochemistry-with-professional-experience) |
| 168 | School of Biological Sciences | Biological Sciences | MSci | MSci Biological Sciences | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biological-sciences) |
| 169 | School of Biological Sciences | Biological Sciences | MSci | MSci Biological Sciences with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biological-sciences-with-professional-experience) |
| 170 | School of Biological Sciences | Biological Sciences | MSci | MSci Biomedical Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biomedical-science) |
| 171 | School of Biological Sciences | Biological Sciences | MSci | MSci Biomedical Science with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-biomedical-science-with-professional-experience) |
| 172 | School of Biological Sciences | Biological Sciences | MSci | MSci Microbiology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-microbiology) |
| 173 | School of Biological Sciences | Biological Sciences | MSci | MSci Microbiology with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-ug/msci-microbiology-with-professional-experience) |
| 174 | School of Biological Sciences | Biomedical Engineering | BEng | BEng Biomedical Engineering | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biomedical-engineering-ug/beng-biomedical-engineering) |
| 175 | School of Biological Sciences | Biomedical Engineering | BEng | BEng Biomedical Engineering with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biomedical-engineering-ug/beng-biomedical-engineering-with-professional-experience) |
| 176 | School of Biological Sciences | Bioveterinary Sciences | BSc | BSc Bioveterinary Sciences | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/bioveterinary-sciences-ug/bsc-bioveterinary-sciences) |
| 177 | School of Biological Sciences | Bioveterinary Sciences | BSc | BSc Bioveterinary Sciences with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/bioveterinary-sciences-ug/bsc-bioveterinary-sciences-with-placement-year) |
| 178 | School of Biological Sciences | Zoology | BSc | BSc Zoology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/bsc-zoology) |
| 179 | School of Biological Sciences | Zoology | BSc | BSc Zoology with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/bsc-zoology-with-foundation) |
| 180 | School of Biological Sciences | Zoology | BSc | BSc Zoology with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/bsc-zoology-with-professional-experience) |
| 181 | School of Biological Sciences | Zoology | MSci | MSci Zoology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/msci-zoology) |
| 182 | School of Biological Sciences | Zoology | MSci | MSci Zoology with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/zoology-ug/msci-zoology-with-professional-experience) |
| 183 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Chemistry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry) |
| 184 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Chemistry with Cosmetic Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-cosmetic-science) |
| 185 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Chemistry with Cosmetic Science with a Year in Industry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-cosmetic-science-with-a-year-in-industry) |
| 186 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Chemistry with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-foundation) |
| 187 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Chemistry with a Year in Industry or Research | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-chemistry-with-a-year-in-industry-research) |
| 188 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Pharmaceutical Chemistry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-pharmaceutical-chemistry) |
| 189 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Pharmaceutical Chemistry with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-pharmaceutical-chemistry-with-foundation) |
| 190 | School of Chemistry, Food and Pharmacy (SCFP) | Chemistry | BSc | BSc Pharmaceutical Chemistry with a Year in Industry or Research | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/chemistry-ug/bsc-pharmaceutical-chemistry-with-placement) |
| 191 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Food Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-science) |
| 192 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Food Science with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-science-with-foundation) |
| 193 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Food Science with Industrial Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-science-with-industrial-training) |
| 194 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Food Technology with Bioprocessing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-technology-with-bioprocessing) |
| 195 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Food Technology with Bioprocessing with Industrial Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-food-technology-with-bioprocessing-with-industrial-training) |
| 196 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Nutrition | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition) |
| 197 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Nutrition and Food Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition-and-food-science) |
| 198 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Nutrition and Food Science with Professional Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition-and-food-science-with-professional-training) |
| 199 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutrition | BSc | BSc Nutrition with Professional Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutrition-ug/bsc-nutrition-with-professional-training) |
| 200 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | BSc | BSc Medical Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-medical-science) |
| 201 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | BSc | BSc Medical Science with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-medical-science-with-foundation) |
| 202 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | BSc | BSc Medical Science with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-medical-science-with-professional-experience) |
| 203 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | BSc | BSc Pharmacology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-pharmacology) |
| 204 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | BSc | BSc Pharmacology with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-pharmacology-with-foundation) |
| 205 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | BSc | BSc Pharmacology with a Year in Industry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/bsc-pharmacology-with-year-in-industry) |
| 206 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | MPAS | MPAS Physician Associate Studies | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/mpas-physician-associate-studies) |
| 207 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | MSci | MSci Medical Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/msci-medical-science) |
| 208 | School of Chemistry, Food and Pharmacy (SCFP) | Medical Sciences | MSci | MSci Medical Science with Professional Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/medical-sciences-ug/msci-medical-science-with-professional-experience) |
| 209 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | MPharm | MPharm Pharmacy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-ug/mpharm-pharmacy) |
| 210 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | MPharm | MPharm Pharmacy with Preparatory Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-ug/mpharm-pharmacy-with-preparatory-year) |
| 211 | School of Construction Management and Engineering (CME) / Architecture | Architecture | BSc | BSc Architecture | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/architecture-ug/bsc-architecture) |
| 212 | School of Humanities | Ancient History | BA | BA Ancient History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history) |
| 213 | School of Humanities | Ancient History | BA | BA Ancient History and Archaeology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-archaeology) |
| 214 | School of Humanities | Ancient History | BA | BA Ancient History and Archaeology with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-archaeology-with-professional-placement) |
| 215 | School of Humanities | Ancient History | BA | BA Ancient History and Archaeology with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-archaeology-with-study-year-abroad) |
| 216 | School of Humanities | Ancient History | BA | BA Ancient History and History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/ancient-history-ug/ba-ancient-history-and-history) |
| 217 | School of Humanities | Classics and Classical Studies | BA | BA Classical Studies | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/classics-ug/ba-classical-studies) |
| 218 | School of Humanities | Classics and Classical Studies | BA | BA Classical Studies and English Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/classics-ug/ba-classical-studies-and-english-literature) |
| 219 | School of Humanities | Classics and Classical Studies | BA | BA Classics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/classics-ug/ba-classics) |
| 220 | School of Humanities | English Literature | BA | BA English Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature) |
| 221 | School of Humanities | English Literature | BA | BA English Literature and Film | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-and-film) |
| 222 | School of Humanities | English Literature | BA | BA English Literature and Film &amp; Theatre | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-and-film-and-theatre) |
| 223 | School of Humanities | English Literature | BA | BA English Literature and Politics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-and-politics) |
| 224 | School of Humanities | English Literature | BA | BA English Literature with Creative Writing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-ug/ba-english-literature-with-creative-writing) |
| 225 | School of Humanities | Global Sustainable Development | BSc | BSc Global Sustainable Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/global-sustainable-development-ug/bsc-global-sustainable-development) |
| 226 | School of Humanities | Global Sustainable Development | BSc | BSc Global Sustainable Development with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/global-sustainable-development-ug/bsc-global-sustainable-development-with-placement-year) |
| 227 | School of Humanities | History | BA | BA History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history) |
| 228 | School of Humanities | History | BA | BA History and Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-economics) |
| 229 | School of Humanities | History | BA | BA History and English Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-english-literature) |
| 230 | School of Humanities | History | BA | BA History and International Relations | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-international-relations) |
| 231 | School of Humanities | History | BA | BA History and Philosophy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-philosophy) |
| 232 | School of Humanities | History | BA | BA History and Politics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-ug/ba-history-and-politics) |
| 233 | School of Humanities | Museum Studies | BA | BA Museum and Classical Studies | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/museum-studies-ug/ba-museum-and-classical-studies) |
| 234 | School of Humanities (English Language) | English Language and Applied Linguistics | BA | BA Digital Media and Communication | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-digital-media-and-communication) |
| 235 | School of Humanities (English Language) | English Language and Applied Linguistics | BA | BA English Language and Linguistics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-english-language-and-linguistics) |
| 236 | School of Humanities (English Language) | English Language and Applied Linguistics | BA | BA English Language and Linguistics with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-english-language-and-linguistics-with-placement) |
| 237 | School of Humanities (English Language) | English Language and Applied Linguistics | BA | BA English Language and Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-ug/ba-english-language-and-literature) |
| 238 | School of Humanities (Sociology) | Sociology | BSc | BSc Sociology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology) |
| 239 | School of Humanities (Sociology) | Sociology | BSc | BSc Sociology and Criminology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology-and-criminology) |
| 240 | School of Humanities (Sociology) | Sociology | BSc | BSc Sociology and Criminology with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology-and-criminology-with-placement-year) |
| 241 | School of Humanities (Sociology) | Sociology | BSc | BSc Sociology with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/sociology-ug/bsc-sociology-with-placement-year) |
| 242 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages (3 years) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-three-years) |
| 243 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages (4 years) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages) |
| 244 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages and Business | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-business) |
| 245 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages and Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-economics) |
| 246 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages and English Language | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-english-language) |
| 247 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages and English Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-english-literature) |
| 248 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages and History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-history) |
| 249 | School of Languages and Cultures | Languages and Cultures | BA | BA Modern Languages and International Relations | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/languages-and-cultures-ug/ba-modern-languages-and-international-relations) |
| 250 | School of Law | Law | BSc | BSc Criminology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology) |
| 251 | School of Law | Law | BSc | BSc Criminology with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology-with-foundation-year) |
| 252 | School of Law | Law | BSc | BSc Criminology with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology-with-placement-year) |
| 253 | School of Law | Law | BSc | BSc Criminology with Study Year Abroad | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/bsc-criminology-with-year-abroad) |
| 254 | School of Law | Law | LLB | LLB Law | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law) |
| 255 | School of Law | Law | LLB | LLB Law with Criminology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-with-criminology) |
| 256 | School of Law | Law | LLB | LLB Law with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-with-foundation) |
| 257 | School of Law | Law | LLB | LLB Law with International Business | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-with-international-business) |
| 258 | School of Law | Law | LLB | LLB Law with International Foundation Year - September entry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/llb-law-international-foundation-year) |
| 259 | School of Law | Law | MLaw | MLaw MLaw | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-ug/mlaw) |
| 260 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | BSc | BSc Computer Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science) |
| 261 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | BSc | BSc Computer Science with Artificial Intelligence (awaiting approval) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-artificial-intelligence) |
| 262 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | BSc | BSc Computer Science with Artificial Intelligence with Industrial Year (awaiting approval) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-artificial-intelligence-with-industrial-year) |
| 263 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | BSc | BSc Computer Science with Artificial Intelligence with Study Year Abroad (awaiting approval) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-artificial-intelligence-with-study-year-abroad) |
| 264 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | BSc | BSc Computer Science with Industrial Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-ug/bsc-computer-science-with-industrial-year) |
| 265 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics) |
| 266 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics and Statistics with Data Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-and-statistics-with-data-science) |
| 267 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics and Statistics with Data Science with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-and-statistics-with-data-science-with-placement-year) |
| 268 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics with Computer Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-computer-science) |
| 269 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics with Computer Science with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-computer-science-with-a-placement-year) |
| 270 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics with Finance and Investment Banking | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-finance-and-investment-banking) |
| 271 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics with Finance and Investment Banking with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-finance-and-investment-banking-with-a-placement-year) |
| 272 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | BSc | BSc Mathematics with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/bsc-mathematics-with-placement-year) |
| 273 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | MMath | MMath Mathematics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/mmath-mathematics) |
| 274 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Mathematics | MMath | MMath Mathematics with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/mathematics-ug/mmath-mathematics-with-a-placement-year) |
| 275 | School of Philosophy, Politics and Economics (SPPE) | Economics | BA | BA Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/ba-economics) |
| 276 | School of Philosophy, Politics and Economics (SPPE) | Economics | BA | BA Economics with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/ba-economics-with-placement-year) |
| 277 | School of Philosophy, Politics and Economics (SPPE) | Economics | BSc | BSc Business Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-business-economics) |
| 278 | School of Philosophy, Politics and Economics (SPPE) | Economics | BSc | BSc Business Economics with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-business-economics-with-placement-year) |
| 279 | School of Philosophy, Politics and Economics (SPPE) | Economics | BSc | BSc Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-economics) |
| 280 | School of Philosophy, Politics and Economics (SPPE) | Economics | BSc | BSc Economics and Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-economics-and-finance) |
| 281 | School of Philosophy, Politics and Economics (SPPE) | Economics | BSc | BSc Economics with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-ug/bsc-economics-with-placement-year) |
| 282 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Ethics, Value and Philosophy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ethics-value-and-philosophy) |
| 283 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Ethics, Value and Philosophy with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ethics-value-and-philosophy-with-placement) |
| 284 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy) |
| 285 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy and International Relations | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-international-relations) |
| 286 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy and International Relations with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-international-relations-with-placement) |
| 287 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy and Politics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-politics) |
| 288 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy and Politics with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-and-politics-with-placement) |
| 289 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-with-placement) |
| 290 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy, Business and Ethics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-business-ethics) |
| 291 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy, Business and Ethics with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-philosophy-business-ethics-with-placement) |
| 292 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy, Politics and Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ppe-philosophy-politics-and-economics) |
| 293 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Philosophy, Politics and Economics with Placement Experience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-ppe-philosophy-politics-and-economics-with-placement) |
| 294 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | BA | BA Psychology and Philosophy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-ug/ba-psychology-and-philosophy) |
| 295 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA International Relations and Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-international-relations-and-economics) |
| 296 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA International Relations and Economics with Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-international-relations-and-economics-placement-year) |
| 297 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA Politics and Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-economics) |
| 298 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA Politics and Economics with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-economics-placement-year) |
| 299 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA Politics and International Relations | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-international-relations) |
| 300 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA Politics and International Relations with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-politics-and-international-relations-with-placement-year) |
| 301 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA War, Peace and International Relations | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-war-peace-and-international-relations) |
| 302 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | BA | BA War, Peace and International Relations with a Placement Year | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-ug/ba-war-peace-and-international-relations-with-placement-year) |
| 303 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology) |
| 304 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology and Language Sciences | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-language-sciences-and-psychology) |
| 305 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology with Criminology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-criminology) |
| 306 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology with Criminology with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-criminology-with-professional-placement-year) |
| 307 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology with Foundation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-foundation) |
| 308 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology with Neuroscience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-neuroscience) |
| 309 | School of Psychology and Clinical Language Sciences | Psychology | BSc | BSc Psychology with Professional Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/bsc-psychology-with-professional-placement) |
| 310 | School of Psychology and Clinical Language Sciences | Psychology | MSci | MSci Applied Psychology (Clinical) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-ug/msci-applied-psychology-clinical) |
| 311 | School of the Built Environment (SBE) | Architectural Engineering | BEng | BEng Architectural Engineering | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/architectural-engineering-ug/beng-architectural-engineering) |
| 312 | School of the Built Environment (SBE) | Architectural Engineering | MEng | MEng Architectural Engineering | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/architectural-engineering-ug/meng-architectural-engineering) |
| 313 | School of the Built Environment (SBE) | Real Estate and Planning | BSc | BSc Planning and Geography | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-planning-and-geography) |
| 314 | School of the Built Environment (SBE) | Real Estate and Planning | BSc | BSc Real Estate | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-real-estate) |
| 315 | School of the Built Environment (SBE) | Real Estate and Planning | BSc | BSc Real Estate Development and Planning | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-real-estate-development-and-planning) |
| 316 | School of the Built Environment (SBE) | Real Estate and Planning | BSc | BSc Real Estate Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/bsc-real-estate-finance) |
| 317 | School of the Built Environment (SBE) | Real Estate and Planning | MPlan | MPlan Planning and Geography | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/mplan-planning-and-geography) |
| 318 | School of the Built Environment (SBE) | Real Estate and Planning | MPlan | MPlan Real Estate Development and Planning | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-ug/mplan-real-estate-development-and-planning) |
| 319 | School of the Built Environment (SBE) | Surveying and Construction Management | BSc | BSc Building Surveying | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-building-surveying) |
| 320 | School of the Built Environment (SBE) | Surveying and Construction Management | BSc | BSc Construction Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-construction-management) |
| 321 | School of the Built Environment (SBE) | Surveying and Construction Management | BSc | BSc Construction Management and Surveying | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-construction-management-and-surveying) |
| 322 | School of the Built Environment (SBE) | Surveying and Construction Management | BSc | BSc Quantity Surveying | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/surveying-and-construction-management-ug/bsc-quantity-surveying) |

### 2.2 Postgraduate Programmes (144)

| # | 学院 | 学科领域 | 学位 | 项目名称 | URL |
|---:|---|---|---|---|---|
| 1 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MRes | MRes Agricultural and Food Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/mres-agricultural-and-food-economics) |
| 2 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Agricultural Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-agricultural-economics) |
| 3 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Agriculture and Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-agriculture-and-development) |
| 4 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Applied International Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-applied-international-development) |
| 5 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Communication for Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-communication-for-development) |
| 6 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Consumer Behaviour | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-consumer-behaviour) |
| 7 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Development Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-development-finance) |
| 8 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Environment, Climate Change and Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-climate-change-and-development) |
| 9 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Food Economics and Marketing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-food-economics-and-marketing) |
| 10 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc Food Security and Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-food-security-and-development) |
| 11 | Graduate Institute of International Development, Agriculture and Economics (GIIDAE) | International Development and Applied Economics (GIIDAE) | MSc | MSc by Research Agricultural Science and Sustainability | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/international-development-and-applied-economics-pg/msc-by-research-in-agricultural-science-and-sustainability) |
| 12 | Henley Business School | Business (Post-Experience) / Henley MBA | Doctor of Business Administration | Doctor of Business Administration | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/doctor-business-administration) |
| 13 | Henley Business School | Business (Post-Experience) / Henley MBA | MBA | The Henley Executive MBA - Global | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/henley-executive-mba) |
| 14 | Henley Business School | Business (Post-Experience) / Henley MBA | MSc | MSc Coaching for Behavioural Change | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/msc-in-coaching-and-behavioural-change) |
| 15 | Henley Business School | Business (Post-Experience) / Henley MBA | Other | The Henley Flexible Executive MBA | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-post-experience-pg/the-henley-flexible-executive-mba) |
| 16 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Accounting, Financial Management and Digital Business | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-accounting-financial-management-digital-business) |
| 17 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Applied AI for Business | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-applied-ai-for-business) |
| 18 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Digital Marketing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-digital-marketing) |
| 19 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Entrepreneurship and Innovation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-entrepreneurship-and-innovation) |
| 20 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc International Accounting and Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-accounting-and-finance) |
| 21 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc International Business | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-business) |
| 22 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc International Business and Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-business-and-finance) |
| 23 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc International Human Resource Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-international-human-resource-management) |
| 24 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-management) |
| 25 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Marketing (International Marketing) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-marketing-international-marketing) |
| 26 | Henley Business School | Business and Management (Pre-Experience) | MSc | MSc Marketing (Sustainable Marketing) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/business-pre-experience-pg/msc-sustainable-marketing) |
| 27 | Henley Business School | Digital Business | MSc | MSc Digital Business and Data Analytics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/digital-business-pg/msc-digital-business-data-analytics) |
| 28 | Henley Business School | Digital Business | MSc | MSc Digital Innovation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/digital-business-pg/msc-digital-innovation) |
| 29 | Henley Business School | Digital Business | MSc | MSc International Business and Digital Transformation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/digital-business-pg/msc-international-business-digital-transformation) |
| 30 | Henley Business School | Finance | MSc | MSc Behavioural Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-behavioural-finance) |
| 31 | Henley Business School | Finance | MSc | MSc Climate Change, Sustainable Business and Green Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-climate-change-sustainable-business-green-finance) |
| 32 | Henley Business School | Finance | MSc | MSc Corporate Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-corporate-finance) |
| 33 | Henley Business School | Finance | MSc | MSc Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-finance) |
| 34 | Henley Business School | Finance | MSc | MSc Finance and Financial Technology (FinTech) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-finance-and-financial-technology-fintech) |
| 35 | Henley Business School | Finance | MSc | MSc Financial Risk Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-financial-risk-management) |
| 36 | Henley Business School | Finance | MSc | MSc Investment Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/finance-pg/msc-investment-management) |
| 37 | Institute of Education | Education | MA | MA Education | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/ma-education) |
| 38 | Institute of Education | Education | Other | Postgraduate Teacher Apprenticeship (Primary) + QTS with Postgraduate Certificate in Education | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-teacher-apprenticeship-primary) |
| 39 | Institute of Education | Education | Other | Postgraduate Teacher Apprenticeship (Primary) + QTS with Professional Graduate Certificate in Education (PgCE) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/professional-graduate-certificate-teacher-apprenticeship-primary) |
| 40 | Institute of Education | Education | Other | Postgraduate Teacher Apprenticeship (Secondary) + QTS with Postgraduate Certificate in Education | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-teacher-apprenticeship-secondary) |
| 41 | Institute of Education | Education | Other | Postgraduate Teacher Apprenticeship (Secondary) + QTS with Professional Graduate Certificate in Education (PgCE) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/professional-graduate-certificate-teacher-apprenticeship-secondary) |
| 42 | Institute of Education | Education | Other | Primary Professional Graduate Certificate in Education with QTS (PgCE) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/primary-professional-graduate-certificate-in-education-qts) |
| 43 | Institute of Education | Education | Other | Primary Professional Graduate Certificate in Education with QTS (PgCE) (3-7) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/primary-professional-graduate-certificate-in-education-qts-early-years) |
| 44 | Institute of Education | Education | Other | Primary Professional Graduate Certificate in Education with QTS (PgCE) with Special Educational Needs (SEN) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/primary-professional-graduate-certificate-in-education-qts-special-educational-needs) |
| 45 | Institute of Education | Education | PGCE | PGCE Early Years (EYTS) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgcert-early-years-practice) |
| 46 | Institute of Education | Education | PGCE | PGCE Primary Postgraduate Certificate in Education | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-primary-education) |
| 47 | Institute of Education | Education | PGCE | PGCE Primary Postgraduate Certificate in Education (3-7) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-primary-early-years) |
| 48 | Institute of Education | Education | PGCE | PGCE Primary Postgraduate Certificate in Education with Special Educational Needs (SEN) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-primary-special-educational-needs) |
| 49 | Institute of Education | Education | PGCE | PGCE Secondary Art and Design | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-art-and-design) |
| 50 | Institute of Education | Education | PGCE | PGCE Secondary Design and Technology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-design-and-technology) |
| 51 | Institute of Education | Education | PGCE | PGCE Secondary English | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-english) |
| 52 | Institute of Education | Education | PGCE | PGCE Secondary Geography | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-geography) |
| 53 | Institute of Education | Education | PGCE | PGCE Secondary History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-history) |
| 54 | Institute of Education | Education | PGCE | PGCE Secondary Mathematics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-mathematics) |
| 55 | Institute of Education | Education | PGCE | PGCE Secondary Modern Foreign Language - French | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-modern-languages-french) |
| 56 | Institute of Education | Education | PGCE | PGCE Secondary Modern Foreign Language - German | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-modern-languages-german) |
| 57 | Institute of Education | Education | PGCE | PGCE Secondary Modern Foreign Language - Spanish | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-modern-languages-spanish) |
| 58 | Institute of Education | Education | PGCE | PGCE Secondary Physical Education | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-physical-education) |
| 59 | Institute of Education | Education | PGCE | PGCE Secondary Science Physics with Mathematics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-physics-with-mathematics) |
| 60 | Institute of Education | Education | PGCE | PGCE Secondary Science: Biology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-biology) |
| 61 | Institute of Education | Education | PGCE | PGCE Secondary Science: Chemistry | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-chemistry) |
| 62 | Institute of Education | Education | PGCE | PGCE Secondary Science: Engineers Teach Physics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-engineers-teach-physics) |
| 63 | Institute of Education | Education | PGCE | PGCE Secondary Science: Physics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-secondary-education-physics) |
| 64 | Institute of Education | Education | Postgraduate Certificate in Education | Postgraduate Certificate in Education (Reflective Practice) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgce-reflective-practice) |
| 65 | Institute of Education | Education | Postgraduate Certificate in Healthcare Education | Postgraduate Certificate in Healthcare Education | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/education-pg/pgcert-healthcare-education) |
| 66 | School of Archaeology, Geography and Environmental Science (SAGES) | Archaeology | MA | MA Archaeology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/archaeology-pg/ma-archaeology) |
| 67 | School of Archaeology, Geography and Environmental Science (SAGES) | Geography and Environmental Science | MSc | MSc Environmental Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/geography-and-environmental-science-pg/msc-environmental-management) |
| 68 | School of Archaeology, Geography and Environmental Science (SAGES) | Meteorology and Climate | MSc | MSc Applied Meteorology and Climate | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-applied-meteorology) |
| 69 | School of Archaeology, Geography and Environmental Science (SAGES) | Meteorology and Climate | MSc | MSc Applied Meteorology and Climate with Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-applied-meteorology-and-climate-with-management) |
| 70 | School of Archaeology, Geography and Environmental Science (SAGES) | Meteorology and Climate | MSc | MSc Atmosphere, Ocean and Climate | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-atmosphere-oceans-and-climate) |
| 71 | School of Archaeology, Geography and Environmental Science (SAGES) | Meteorology and Climate | MSc | MSc Climate Change and Artificial Intelligence (AI) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/meteorology-and-climate-pg/msc-climate-change-and-artificial-intelligence) |
| 72 | School of Arts and Communication Design (SACD) | Art | MA | MA Fine Art | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/art-pg/master-in-fine-art-ma) |
| 73 | School of Arts and Communication Design (SACD) | Film, Theatre and Television | MA | MA by Research Film, Theatre and Television | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/film-theatre-and-television-pg/ma-by-research-film-theatre-television) |
| 74 | School of Arts and Communication Design (SACD) | Typography and Graphic Communication | MA | MA Communication Design: Book Design Pathway | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-book-design) |
| 75 | School of Arts and Communication Design (SACD) | Typography and Graphic Communication | MA | MA Communication Design: Graphic Design Pathway | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-graphic-design) |
| 76 | School of Arts and Communication Design (SACD) | Typography and Graphic Communication | MA | MA Communication Design: Information Design Pathway | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-information-design) |
| 77 | School of Arts and Communication Design (SACD) | Typography and Graphic Communication | MA | MA Communication Design: Typeface Design Pathway | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-typeface-design) |
| 78 | School of Arts and Communication Design (SACD) | Typography and Graphic Communication | MA | MA by Research Typography and Graphic Communication | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-by-research-typography-and-graphic-communication) |
| 79 | School of Arts and Communication Design (SACD) | Typography and Graphic Communication | MRes | MRes Typeface Design | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/mres-typeface-design) |
| 80 | School of Biological Sciences | Biological Sciences | MSc | MSc Biotechnology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-biotechnology) |
| 81 | School of Biological Sciences | Biological Sciences | MSc | MSc Ecological Survey Skills with Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-ecological-survey-skills-with-placement) |
| 82 | School of Biological Sciences | Biological Sciences | MSc | MSc by Research Biomedicine | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-by-research-biomedicine) |
| 83 | School of Biological Sciences | Biological Sciences | MSc | MSc by Research Entomology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/biological-sciences-pg/msc-by-research-entomology) |
| 84 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutritional Sciences | MSc | MSc Dietetics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-dietetics) |
| 85 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutritional Sciences | MSc | MSc Food Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-food-science) |
| 86 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutritional Sciences | MSc | MSc Food Technology – Quality Assurance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-food-technology-quality-assurance) |
| 87 | School of Chemistry, Food and Pharmacy (SCFP) | Food and Nutritional Sciences | MSc | MSc Nutrition and Food Science | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/food-and-nutritional-sciences-pg/msc-nutrition-and-food-science) |
| 88 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | Other | Flexible CPD Advancing Healthcare Practice (Modular/PGDip/MSc) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/msc-advancing-healthcare-practice) |
| 89 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | PGCert | PGCert Independent Prescribing for Allied Health Professionals | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-independent-supplementary-prescribing-allied) |
| 90 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | PGCert | PGCert Independent Prescribing for Pharmacists | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-independent-supplementary-prescribing-pharmacists) |
| 91 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | PGCert | PGCert Reflective Practice for Prescribers | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-reflective-practice-for-prescribers) |
| 92 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | PGCert | PGCert Work-Based Learning | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-work-based-learning) |
| 93 | School of Chemistry, Food and Pharmacy (SCFP) | Pharmacy | PGCert | PGCert-GradCert Independent Prescribing for Nurses (Levels 6 and 7) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/pharmacy-pg/pgcert-independent-supplementary-prescribing-nurses) |
| 94 | School of Construction Management and Engineering (CME) / Architecture | Architecture | Master of Architecture | Master of Architecture | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/architecture-pg/master-of-architecture) |
| 95 | School of Humanities | Classics and Ancient History | MA | MA Classics and Ancient History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/classics-and-ancient-history-pg/ma-classics-and-ancient-history) |
| 96 | School of Humanities | English Literature | MA | MA English Literature | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-literature-pg/ma-english-literature) |
| 97 | School of Humanities | History | MA | MA History | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/history-pg/ma-history) |
| 98 | School of Humanities (English Language) | English Language and Applied Linguistics | MA | MA Applied Linguistics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-pg/ma-in-applied-linguistics) |
| 99 | School of Humanities (English Language) | English Language and Applied Linguistics | MA | MA Teaching English to Speakers of Other Languages (TESOL) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-pg/ma-teaching-english-to-speakers-of-other-languages-tesol) |
| 100 | School of Humanities (English Language) | English Language and Applied Linguistics | PGCert | PGCert in Language Assessment | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/english-language-and-applied-linguistics-pg/pgcert-language-assessment) |
| 101 | School of Law | Law | Conversion | Conversion programmes in Law | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/law-conversion) |
| 102 | School of Law | Law | LLM | LLM Advanced Legal Studies | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-advanced-legal-studies) |
| 103 | School of Law | Law | LLM | LLM International Commercial Law | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law) |
| 104 | School of Law | Law | LLM | LLM International Commercial Law with Intellectual Property Law and Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law-with-intellectual-property-law-and-management) |
| 105 | School of Law | Law | LLM | LLM International Commercial Law with International Banking Law and Financial Regulation | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law-with-international-banking-law-and-financial-regulation) |
| 106 | School of Law | Law | LLM | LLM International Commercial Law with International Corporate Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-commercial-law-with-corporate-finance) |
| 107 | School of Law | Law | LLM | LLM International Law | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-international-law) |
| 108 | School of Law | Law | LLM | LLM Research Thesis | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/llm-research-thesis) |
| 109 | School of Law | Law | LPC | LPC Legal Practice Course | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/lpc-legal-practice-course) |
| 110 | School of Law | Law | MRes | MRes Law | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/law-pg/mres-law) |
| 111 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | MSc | MSc Applied Artificial Intelligence for Business | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-pg/msc-applied-ai-for-business) |
| 112 | School of Mathematical, Physical and Computational Sciences (SMPCS) | Computer Science | MSc | MSc Data Science and Advanced Computing | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/computer-science-pg/msc-data-science-and-advanced-computing) |
| 113 | School of Philosophy, Politics and Economics (SPPE) | Economics | MSc | MSc Applied Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-applied-economics) |
| 114 | School of Philosophy, Politics and Economics (SPPE) | Economics | MSc | MSc Business Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-business-economics) |
| 115 | School of Philosophy, Politics and Economics (SPPE) | Economics | MSc | MSc Economics | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-economics) |
| 116 | School of Philosophy, Politics and Economics (SPPE) | Economics | MSc | MSc Public Policy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/economics-pg/msc-public-policy) |
| 117 | School of Philosophy, Politics and Economics (SPPE) | Philosophy | MA | MA by Research Philosophy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/philosophy-pg/ma-by-research-philosophy) |
| 118 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | MA | MA Conflict and International Security | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-and-international-relations-pg/ma-conflict-and-international-security) |
| 119 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | MA | MA International Relations and Diplomacy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-and-international-relations-pg/ma-international-relations-and-diplomacy) |
| 120 | School of Philosophy, Politics and Economics (SPPE) | Politics and International Relations | MRes | MRes Politics and International Relations | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/politics-and-international-relations-pg/mres-politics-and-international-relations) |
| 121 | School of Psychology and Clinical Language Sciences | Physician Associate | MSc | MSc Physician Associate | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/physician-associate-pg/msc-physician-associate) |
| 122 | School of Psychology and Clinical Language Sciences | Psychology | MSc | MSc Cognitive Neuroscience | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-cognitive-neuroscience) |
| 123 | School of Psychology and Clinical Language Sciences | Psychology | MSc | MSc Psychology Conversion | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-psychology-conversion) |
| 124 | School of Psychology and Clinical Language Sciences | Psychology | MSc | MSc Research Methods in Psychology | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-research-methods-in-psychology) |
| 125 | School of Psychology and Clinical Language Sciences | Psychology | MSc | MSc Theory and Practice in Clinical Psychology (with clinical or research placement) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/msc-theory-and-practice-in-clinical-psychology) |
| 126 | School of Psychology and Clinical Language Sciences | Psychology | Other | GradCert/PGCert Psychological Wellbeing Practitioner Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/pgcert-psychological-wellbeing-practitioner-training) |
| 127 | School of Psychology and Clinical Language Sciences | Psychology | Other | Postgraduate and Graduate Diplomas in Children&#39;s Wellbeing Practitioner Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/graduate-pgdip-childrens-wellbeing-practitioner-training) |
| 128 | School of Psychology and Clinical Language Sciences | Psychology | Other | Postgraduate and Graduate Diplomas in Education Mental Health Practitioner Training | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/graduate-pgdip-education-mental-health-practitioner-training) |
| 129 | School of Psychology and Clinical Language Sciences | Psychology | PGDip | PGDip Evidence-Based Psychological Treatment (High Intensity) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/pgdip-evidence-based-psychological-treatment-high-intensity) |
| 130 | School of Psychology and Clinical Language Sciences | Psychology | PGDip | PGDip Evidence-Based Psychological Treatment for Children and Young People (High Intensity) | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/psychology-pg/pgdip-evidence-based-psychological-treatment-for-children-young-people) |
| 131 | School of Psychology and Clinical Language Sciences | Speech and Language Therapy | MSc | MSc Language Sciences | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/speech-and-language-therapy-pg/msc-language-sciences) |
| 132 | School of Psychology and Clinical Language Sciences | Speech and Language Therapy | MSc | MSc Speech and Language Therapy | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/speech-and-language-therapy-pg/msc-speech-and-language-therapy) |
| 133 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Construction Cost Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-construction-cost-management) |
| 134 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Construction Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-construction-management) |
| 135 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Construction Management with Industry Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-construction-management-with-industry-placement) |
| 136 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Design and Management of Sustainable Built Environments | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-design-and-management-of-sustainable-built-environment) |
| 137 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Project Management | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-project-management) |
| 138 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Project Management with Industry Placement | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-project-management-with-industry-placement) |
| 139 | School of the Built Environment (SBE) | Construction Management and Engineering | MSc | MSc Renewable Energy: Technology and Sustainability | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/construction-management-and-engineering-pg/msc-renewable-energy-technology-and-sustainability) |
| 140 | School of the Built Environment (SBE) | Real Estate and Planning | MSc | MSc Real Estate | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate) |
| 141 | School of the Built Environment (SBE) | Real Estate and Planning | MSc | MSc Real Estate - Flexible | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate-flexible) |
| 142 | School of the Built Environment (SBE) | Real Estate and Planning | MSc | MSc Real Estate Finance | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate-finance) |
| 143 | School of the Built Environment (SBE) | Real Estate and Planning | MSc | MSc Real Estate Investment and Finance - Flexible | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-real-estate-investment-and-finance-flexible) |
| 144 | School of the Built Environment (SBE) | Real Estate and Planning | MSc | MSc Spatial Planning and Development | [详情](https://www.reading.ac.uk/ready-to-study/study/2026/real-estate-and-planning-pg/msc-spatial-planning-and-development) |## § 3 申请要求(本科 / 研究生 / 老师培训)

### 3.1 学术要求

#### Undergraduate

| 项 | 要求 |
|---|---|
| A-levels (典型) | BBB-AAA, 依学位而定 (医学院、Pharmacy、Physician Associate 要求更高, 含 Science 必修) |
| UCAS Tariff | 96-168 points (依学位) |
| International Baccalaureate | 30-36 points (依学位; HL 通常要求 16+ in specific subjects) |
| BTEC | DMM-DDD (依学位; 需配合 A-level 同等模块) |
| Foundation year 可选项 | 适用多数学位 (4 年 w/ Foundation 或 1-year stand-alone Foundation) |
| Year Abroad / Placement year | 多数 bachelor 学位可选加 (3yr → 4yr sandwich year) |

> 注: Reading 接受 HKDSE / Indian Standard XII / NCUK International Foundation Year 等更宽泛入学通道。详情见 subject-specific entry requirements 各课程详情页。

#### Postgraduate (taught master's / research)

| 项 | 要求 |
|---|---|
| UK Honours degree | Lower 2:2 (2:2 / 50%+) 至 Upper 2:1 / First, 依项目而定 |
| 国际同等学历 | 详见 Reading International Equivalency Calculator (via course page) |
| 工作经验 | PGCE / Henley MBA / DBA / LPC 通常要求相关工作经验或专业认可 |
| GMAT | Henley MBA 推荐提交 (500+; 可用其他量化项目成绩置换) |
| References | 通常 2 封 (学术 / 雇主) |
| Personal statement / motivation | 强制 (500-1000 字, 依项目) |

#### Postgraduate Research (MPhil / PhD / Professional Doctorate)

- 通常要求英国 Master level (Merit 以上) 或同等国际学历
- 与 supervisor 提前接洽, 提交 1000-2000 字 research proposal
- Henley DBA 需 master degree + 至少 5 年高级管理经验

### 3.2 Standardized Tests

Reading 系英国大学, **不要求 ACT / SAT / GRE / GMAT (除 Henley MBA 推荐) / LSAT**。PGCE 不需任何标化考试。

### 3.3 标准化考试 / 申请截止日期

- **UCAS (UG)**:
  - 2026/27 入学: 通过 UCAS 申请 - Oxford/Cambridge/Medicine/Veterinary/Dentistry 等 2025-10-15; 其余多数 2026-01-29 (等同 Reading 2026 entry) - Reading 官方建议 2026-01-29 前提交
  - Clearing: A-level Results Day 后 (2026-08 通常) 通过 Clearing 申请空缺位
  - Late applications: UCAS Extra / Clearing 视空位情况
- **PG (direct application)**: 滚动招生至 7-8 月; 热门专业 (Henley MBA / MSc Data Science / PhD funding deadline) 有固定截止。建议提前 3-6 个月申请
- **PGCE / PG ITE**: 多个固定轮次 (2026/27 申请的 PGCE 截止 2026-08 通常)

### 3.4 签证 (International)

Reading 持有 UKVI Tier 4 sponsor licence (Student visa route), 覆盖所有学位 (UG/PG/PGCE/PhD)。

| 项 | 要求 |
|---|---|
| CAS | 接受 offer 后由 International Student Advice team 签发 |
| 资金证明 | Living costs £1,023/月 × 9 个月 (UKVI 标准) |
| 学费押金 | 通常 £3,000-£5,000 (详询项目) |
| ATAS | 部分敏感学位 (如 Energy & Environmental Engineering, certain PhD 涉及 Life Sciences) 需 Academic Technology Approval Scheme |

---

## § 4 学费与生活费

### 4.1 国际学生 Tuition Fees (2026/27)

| 类别 | 学费 (英镑/年) | 适用 |
|---|---:|---|
| UG non-laboratory | **£25,850** | 大部分文科、社科、商科、数学、计算机 (不带实验/工坊) |
| UG with laboratory / workshop | **£30,650** | 化学、生物、药学、心理学 (含实验课)、食品营养、医科预科 (Medical Sciences)、建筑、考古 (含环境科学) |
| UG Integrated International Foundation Year | **£23,850** (Year 1) | IFP / 国际大一预科 Year 1; 完成后转入 bachelor, 按其类别付费 |
| PG non-laboratory (Band 1) | **£26,450** | MSc Accounting / Finance / Marketing / Management / Data Science 等 + International Foundation Programmes |
| PG with laboratory / workshop (Band 2) | **£31,650** | MSc Psychology / Nutrition / Pharmacy / Climate Science / Ecology / Speech & Language Therapy / Dietetics 等 + 带实验课的项目 |

> 详见 [Tuition fees for international students 2026/27](https://www.reading.ac.uk/ready-to-study/study/Fees-and-funding/fees-and-funding-ug/international-undergraduate-student-fees) - 摘录原文: "For 2026/27, standard fees for international students are: £25,850 a year for non-laboratory courses; £30,650 a year for subjects with significant laboratory study or workshop content"
> 同上 PG 来源: [International Postgraduate Student Fees](https://www.reading.ac.uk/Ready-to-Study/study/Fees-and-funding/fees-and-funding-pg/InternationalPostgraduateStudentFees) - "For 2026/27, standard fees for international students are: £26,450 a year for non-laboratory courses and International Foundation Programmes (Band 1); £31,650 a year for subjects with significant laboratory study or workshop content (Band 2)"

### 4.2 Home (UK) Students Tuition Fees (2026/27)

- Undergraduate: £9,535/year (regulated fee cap)
- Postgraduate taught: £10,000-£14,000 区间, 多数项目 £11,000-£12,000/年
- 完整官方页面: [Home undergraduate student fees](https://www.reading.ac.uk/ready-to-study/study/Fees-and-funding/fees-and-funding-ug/home-undergraduate-student-fees)

### 4.3 学费变更规则

- 所有国际生 tuition fees 受 **UK Consumer Price Index (CPI) 年度调整封顶 4%** (条款来自 Student Contract)
- 实测期间 Year Abroad / Placement Year 通常减收学费 (约 15%)
- Reading 一向每年公告次年 fees update, 2026/27 已正式公布

### 4.4 生活费估算 (International, 2026/27)

| 项 | 月均 (£) | 学年 (9 个月, £) |
|---|---:|---:|
| 住宿 (catered room / self-catered) | 600-950 | 5,400-8,550 |
| 餐饮 | 200-350 | 1,800-3,150 |
| 书本 / 文具 | 50-80 | 450-720 |
| 交通 (bus within Reading + 偶尔 London) | 50-120 | 450-1,080 |
| 杂项 / 社交 | 80-150 | 720-1,350 |
| **建议总预算 (除学费外)** | **~£1,100-£1,500** | **~£10,000-£13,500** |

UKVI 资金证明门槛: **£1,023 / 月 × 9 个月 = £9,207**。

---

## § 5 英语语言要求

> 来源: [English language requirements 官方页面](https://www.reading.ac.uk/ready-to-study/international-and-eu/english-language-requirements) - 摘录: "The English language levels generally required for our courses are outlined in the tables on this page."

### 5.1 默认 UG English Requirement

| Qualification | Score |
|---|---|
| IELTS Academic | **6.5** (no lower than 5.5 in each component) |
| IELTS Indicator | 6.5 (no lower than 5.5 in each component) |
| TOEFL iBT | **88** (no less than 17 in Listening and Writing, 18 in Reading and 20 in Speaking) |
| TOEFL iBT at Home | 88 (same per-section as above) |
| Cambridge CPE / C2 Proficiency | C / 176 (no element less than 162) |
| Cambridge CAE / C1 Advanced | B / 176 (no element less than 162) |
| PTE Academic | **69** overall (min 59-64 in each component) |
| Duolingo English Test | 125 overall (no sub <100), 或 120 / 100 + 6-week Pre-sessional, 或 115 / 90 + 10-week Pre-sessional |
| LanguageCert International ESOL B2 | High pass overall (no element <33) |
| Indian Standard XII (CBSE/ICSE) | 70% (其他 board 75%) |
| WASSCE | C grade |
| GCE O-Level / IGCSE First Language | C / First language: C |
| IGCSE Second Language | B |
| HKDSE (English) | 4 或 5* (dependant on programme) |
| TEEP (Reading's own pre-sessional) | Pass or High pass (依项目) |
| Degree taught in English | 完整学位 + UKVI-approved university (Sri Lanka / Nigeria 等需 case-by-case) |

### 5.2 高门槛专业异常

| 专业 | IELTS / Equivalent | 条件 |
|---|---|---|
| Speech and Language Therapy | **8.0** overall, no less than **7.5** in each component | 加严分数线 |
| Pharmacy (含 Preparatory Year) + Nutrition (含 Foundation) | 6.5 overall, no less than **6.0** in each component | 略高于 standard |
| PGCE / PG ITE (Institute of Education) | 与 UG 6.5 同; 临床/教育学位常要求 GCSE English C/4 | 项目页确认 |
| Postgraduate (research: MPhil / PhD) | 6.5-7.0 (依学院) | 详情见 supervisor 邮件 / 学院页面 |

### 5.3 Pre-sessional English Programme (PSE)

Reading Global Academy 提供 **6 / 10 / 16 / 20 weeks** Pre-sessional English 课程; 完成可直读主课。

---

## § 6 WeKnora 摄入清单 + 监测设计

### 6.1 摄入清单 (chunk split strategy)

| Chunk ID | 范围 | 估计 token | 路径 |
|---|---|---:|---|
| KBC-RDG-001-SCHOOLS-OVERVIEW | § 0 院校总览 + § 0.3 学院层次 | ~5,500 | § 0 |
| KBC-RDG-002-DEGREES-MATRIX | § 0.5 学院 x 学位矩阵 + § 0.4 degree inventory | ~1,800 | § 0.4 / § 0.5 |
| KBC-RDG-003-SUBJECTS-METADATA | § 0.6 学院-学科领域 + degree breakdown | ~6,000 | § 0.6 |
| KBC-RDG-004-DETAIL-PART-A | § 1 Henley + GIIDAE + SAGES + SACD | ~10,000 | § 1 |
| KBC-RDG-005-DETAIL-PART-B | § 1 SCFP + SMPCS + SPPE + Biological Sciences | ~12,000 | § 1 |
| KBC-RDG-006-DETAIL-PART-C | § 1 SBE+CME + Humanities + Languages + Psychology + IoE + Global Academy + Law | ~14,000 | § 1 |
| KBC-RDG-007-PROGRAMS-UG | § 2.1 UG 全量列表 (322 行) | ~22,000 | § 2.1 |
| KBC-RDG-008-PROGRAMS-PG | § 2.2 PG 全量列表 (144 行) | ~10,500 | § 2.2 |
| KBC-RDG-009-APPL-FEES-LANG | § 3 申请 + § 4 学费 + § 5 语言 (约 7 KB) | ~7,000 | § 3-5 |

### 6.2 监测设计 (Watchlist)

| URL | 频率 | 字段 | 基线 (2026-07-08) |
|---|---|---|---|
| https://www.reading.ac.uk/ready-to-study/study/2026/accounting-ug (subject hub, 71 / 130 类似 URL) | quarterly | 该 subject 下 program 列表 | 共 71 个 UG subject + 59 个 PG subject |
| https://www.reading.ac.uk/ready-to-study/study/Fees-and-funding/fees-and-funding-ug/international-undergraduate-student-fees | **monthly** | UG intl tuition | £25,850 / £30,650 / £23,850 |
| https://www.reading.ac.uk/Ready-to-Study/study/Fees-and-funding/fees-and-funding-pg/InternationalPostgraduateStudentFees | **monthly** | PG intl tuition | £26,450 / £31,650 (Band 1/2) |
| https://www.reading.ac.uk/ready-to-study/study/Postgraduate-study | quarterly | PG taught offerings | 59 个 PG subject |
| https://www.reading.ac.uk/ready-to-study/study/Undergraduate-study | quarterly | UG overview | 71 个 UG subject |
| https://www.reading.ac.uk/ready-to-study/international-and-eu/english-language-requirements | semi-annual | English 测试成绩门槛 | UG standard 6.5 (5.5), PG 同 |
| https://www.reading.ac.uk/ready-to-study/study/Fees-and-funding/fees-and-funding-pg/home-postgraduate-student-fees | annual | Home PG fees | 详询系院 |
| https://www.reading.ac.uk/ready-to-study/study/how-to-apply | annual | 申请流程 | UCAS 2026/27 deadline 2026-01-29 |
| https://www.reading.ac.uk/ready-to-study/international-and-eu/international-scholarships | annual | 国际奖学金列表 | 多数为 £3,000-£10,000 区间 |

---

## § 7 数据来源与变更日志

### 7.1 一次抓取源 URLs (cited)

| 字段 | URL | 抓取日期 |
|---|---|---|
| Study hub (UG + PG subject index) | https://www.reading.ac.uk/ready-to-study/study | 2026-07-08 |
| 各 subject hub (71 UG + 59 PG) | /ready-to-study/study/2026/{slug}-ug or -pg | 2026-07-08 |
| 各 program 详情页 (322 UG + 144 PG = 466) | /ready-to-study/study/2026/{slug}-{level}/{course-slug} | 2026-07-08 |
| English language requirements | https://www.reading.ac.uk/ready-to-study/international-and-eu/english-language-requirements | 2026-07-08 |
| UG international tuition | https://www.reading.ac.uk/ready-to-study/study/Fees-and-funding/fees-and-funding-ug/international-undergraduate-student-fees | 2026-07-08 |
| PG international tuition | https://www.reading.ac.uk/Ready-to-Study/study/Fees-and-funding/fees-and-funding-pg/InternationalPostgraduateStudentFees | 2026-07-08 |
| Schools A-Z | https://www.reading.ac.uk/atoz/a-z-academic | 2026-07-08 |
| How to apply | https://www.reading.ac.uk/ready-to-study/study/how-to-apply | 2026-07-08 |
| International scholarships | https://www.reading.ac.uk/ready-to-study/international-and-eu/international-scholarships | 2026-07-08 |
| Fees and funding hub | https://www.reading.ac.uk/ready-to-study/study/Fees-and-funding | 2026-07-08 |

### 7.2 变更日志

| 日期 | 变更 |
|---|---|
| 2026-07-08 | v2.0 首次生成 - 466 个 program 全量; 12 学院 + 2 学院级研究所; UG 322 + PG 144 |

### 7.3 数据质量说明

- **抓取方式**: ego-browser (headless Chromium, single task space) -> 拉取 reading.ac.uk 主页与 130 个 subject hub pages -> 用本地 Python 解析 HTML 提取 program 链接 -> 用一组 regex 把 URL/title 匹配
- **完整性**: 全部 466 个 program 均含 (URL + 标题 + 学位 + 学科领域 + 学院映射). 12 个标题复杂 (如 "The Henley Executive MBA - Global") 学位被标为 "Other"
- **未能深入**: 每个 program 的详情页 (学费、入学要求、模块列表) 未在本次抓取 - 因时间 / 容量约束; 推荐下一轮 (Phase 7 复查) 单独深爬重点学科
- **suggested next phases**:
  1. 每 program 详情页抓 (学费、ATAS、placement year、duration)
  2. PGCE 截止日期 / Henley Executive MBA 申请截止日期 / PhD funding deadlines 单独抓
  3. 联合 122 其它英国大学的 v2.0 doc 做大型比较表 (英文: per-course cross-UK 评分)
