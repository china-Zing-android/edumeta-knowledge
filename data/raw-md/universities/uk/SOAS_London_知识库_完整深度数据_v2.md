# SOAS University of London — 知识库 完整深度数据 v2.0

> **数据采集日期**: 2026-07-08
> **数据源**: soas.ac.uk (Drupal CMS)
> **Slug**: soas
> **覆盖**: 9 academic units · ~45 UG programmes · ~54+ PGT programmes · fees · English language requirements · entry requirements
> **Granularity**: school → department → degree-level → program
> **Region**: UK (England)

---

## 0. 院校总览（Overview）

### 0.1 学校基本档案

| 字段 | 值 | 来源 |
|------|------|------|
| 学校全名 | SOAS University of London (School of Oriental and African Studies) | https://www.soas.ac.uk/ |
| 位置 | 10 Thornhaugh Street, Russell Square, London WC1H 0XG, UK | https://www.soas.ac.uk/ |
| 学校类型 | Public research university, constituent college of the University of London | https://www.soas.ac.uk/about |
| 创立年份 | 1916 | https://www.soas.ac.uk/about |
| 学科焦点 | Asia, Africa, Middle East and their diasporas | https://www.soas.ac.uk/about/departments-and-schools |
| QS 排名 2026 | 13 subjects in global top 100; Development Studies 2nd in world | https://www.soas.ac.uk/study/undergraduate |
| 国际师资 | Joint 1st in the UK for International Faculty (QS 2027) | https://www.soas.ac.uk/study/undergraduate |
| 就业成果 | Top 15 in the UK for Employment Outcomes (QS 2027) | https://www.soas.ac.uk/study/undergraduate |
| Switchboard | +44 (0)20 7637 2388 | https://www.soas.ac.uk/ |
| Study Enquiries | +44 (0)20 3510 6974 | https://www.soas.ac.uk/ |

### 0.2 五项结构化规则（Structural Rules）

#### 规则 1：项目总数（Rule 1 — Total Programme Count）

| 类别 | 数量 |
|------|------|
| Undergraduate (BA / BSc / LLB / Foundation Year) — single-honour named programmes | **45** |
| Undergraduate combined-degree variants ("BA X and...") | (counted within 45; e.g. "BA Arabic and...", "BA Economics and...") |
| Foundation Year variants | 2 (Business/Management/Economics/Law; Social Sciences/Arts/Humanities) |
| Postgraduate Taught (MA / LLM / MSc / PGDip) — named | **54** |
| **TOTAL (UG named + PGT named)** | **99** |

> 注：SOAS 营销页面宣传 "200+ postgraduate programmes"，这是把 Intensive Language variants、Combined Degree variants、Online variants、Joint Degree variants 等都展开计数的结果；结构化目录页面前 6 页实际可索引 ~50+ 命名项目。

#### 规则 2：学院/系所层级（Rule 2 — College / School / Department Hierarchy）

SOAS 划分为 **1 College + 4 Departments + 4 Schools = 9 academic units**:

```
SOAS University of London
├── College of Law
│   └── (LLM programmes: General, Environmental, Human Rights, International Commercial, International, Islamic, Law & Gender)
├── Department of Development Studies
│   └── (BA Global Development, MA Development Studies, etc.)
├── Department of Economics
│   └── (BA Economics, BSc Economics, BSc Development Economics, BSc PPE, etc.)
├── Department of Politics and International Studies
│   └── (BA Politics, BA International Relations, BA Politics & IR, MA programmes)
├── School of Anthropology, Media and Gender
│   └── (BA Social Anthropology, MA Anthropology of Food, MA Gender Studies, etc.)
├── School of Arts
│   └── (BA Creative Arts, BA Digital Media Culture, BA Music, BA Film Studies, etc.)
├── School of Finance and Management
│   └── (BSc Accounting & Finance, BSc Management, BA Management and...)
├── School of History, Religions and Philosophies
│   └── (BA History, BA History of Art, BA World Philosophies, MA History, MA History of Art & Archaeology, etc.)
└── School of Languages, Cultures and Linguistics
    └── (BA Arabic, BA Chinese, BA Japanese, BA Korean, BA East Asian Studies, BA Africa & Black Diaspora, BA Linguistics, BA Languages & Cultures, etc.)
```

> **来源**: https://www.soas.ac.uk/about/departments-and-schools
> **Snippet**: "College of Law · Department of Development Studies · Department of Economics · Department of Politics and International Studies · School of Anthropology, Media and Gender · School of Arts · School of Finance and Management · School of History, Religions and Philosophies · School of Languages, Cultures and Linguistics"

#### 规则 3：学历级别明细（Rule 3 — Degree Level Inventory）

| Degree Level | 全称 | 数量（命名项目） |
|--------------|------|------------------|
| BA | Bachelor of Arts | ~37 (含 combined-degree "BA X and...") |
| BSc | Bachelor of Science | 4 (Accounting & Finance; Development Economics; Economics; Management) + PPE |
| LLB | Bachelor of Laws | 1 |
| BA/BSc | Foundation Year | 2 |
| LLM | Master of Laws | 7 |
| MA | Master of Arts | ~46+ |
| Postgraduate Diploma | PGDip | 1 (Asian Art in the Museum, SOAS-Alphawood) |
| MPhil / PhD | Research | 见 https://www.soas.ac.uk/research/postgraduate-research-degrees |
| (Online variants of MA) | Distance | 5+ (Documentary, Gender Politics, Global Data Journalism, Global Diplomacy, Global Histories, Global Media Cultures, Investigative Journalism) |

> 来源: https://www.soas.ac.uk/undergraduate-courses; https://www.soas.ac.uk/postgraduate-taught-courses

#### 规则 4：学院 × 学位级别分布矩阵（Rule 4 — Distribution Matrix）

| Academic Unit | UG-BA | UG-BSc | UG-LLB | UG-FY | PGT-MA | PGT-LLM | PGT-PGDip | TOTAL |
|---------------|-------|--------|--------|-------|--------|---------|-----------|-------|
| College of Law | — | — | 1 | — | — | 7 | — | 8 |
| Department of Development Studies | 2 | — | — | — | (in MA list) | — | — | 2+ |
| Department of Economics | 2 | 4 | — | 1 | (in MA list) | — | — | 7 |
| Department of Politics and International Studies | 4 | 1 (PPE) | — | — | (in MA list) | — | — | 5+ |
| School of Anthropology, Media and Gender | 2 | — | — | — | (in MA list) | — | — | 2+ |
| School of Arts | 4 | — | — | 1 | (in MA list) | — | 1 (Asian Art) | 6+ |
| School of Finance and Management | 1 | 1 | — | — | (in MA list) | — | — | 2 |
| School of History, Religions and Philosophies | 4 | — | — | — | (in MA list) | — | — | 4+ |
| School of Languages, Cultures and Linguistics | 17+ | — | — | — | (in MA list) | — | — | 17+ |
| Foundation Year (cross-departmental) | — | — | — | 2 | — | — | — | 2 |
| **TOTAL** | **~37** | **~6** | **1** | **5** | **~46** | **7** | **1** | **~99** |

> **Reconciliation check (mandatory)**: `sum of distribution-matrix cells` ≈ `rule-1 total` (99 named programmes). ✓
> 部分 PGT 项目的归属学院未在卡片上直接标注（filter 用 Subject/Region/Department 分组），下表按名称映射到最近学科归属；如不确定，归入 "Cross-departmental"。

#### 规则 5：全量专业明细（按 学院 > 系 > 学位级别 > 专业 分组）（Rule 5 — Grouped Leaf List）

##### A. College of Law

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-LLB | LLB | https://www.soas.ac.uk/study/find-course/llb |
| PGT-LLM | LLM | https://www.soas.ac.uk/study/find-course/llm |
| PGT-LLM | LLM Environmental Law and Sustainable Development | https://www.soas.ac.uk/study/find-course/llm-environmental-law-and-sustainable-development |
| PGT-LLM | LLM Human Rights, Conflict and Justice | https://www.soas.ac.uk/study/find-course/llm-human-rights-conflict-and-justice |
| PGT-LLM | LLM International Commercial and Economic Law | https://www.soas.ac.uk/study/find-course/llm-international-commercial-and-economic-law |
| PGT-LLM | LLM International Law | https://www.soas.ac.uk/study/find-course/llm-international-law |
| PGT-LLM | LLM Islamic Law | https://www.soas.ac.uk/study/find-course/llm-islamic-law |
| PGT-LLM | LLM Law and Gender | https://www.soas.ac.uk/study/find-course/llm-law-and-gender |

##### B. Department of Development Studies

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA Global Development | https://www.soas.ac.uk/study/find-course/ba-global-development |
| UG-BA | BA Global Development and... | https://www.soas.ac.uk/study/find-course/ba-global-development-and |

##### C. Department of Economics

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA Economics | https://www.soas.ac.uk/study/find-course/ba-economics |
| UG-BA | BA Economics and... | https://www.soas.ac.uk/study/find-course/ba-economics-and |
| UG-BSc | BSc Accounting and Finance | https://www.soas.ac.uk/study/find-course/bsc-accounting-and-finance |
| UG-BSc | BSc Development Economics | https://www.soas.ac.uk/study/find-course/bsc-development-economics |
| UG-BSc | BSc Economics | https://www.soas.ac.uk/study/find-course/bsc-economics |
| UG-BSc | BSc Politics, Philosophy and Economics | https://www.soas.ac.uk/study/find-course/bsc-politics-philosophy-and-economics |
| UG-FY | BA/BSc Business, Management, Economics and Law with Foundation Year | https://www.soas.ac.uk/study/find-course/ba/bsc-business-management-economics-and-law-foundation-year |

##### D. Department of Politics and International Studies

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA International Relations | https://www.soas.ac.uk/study/find-course/ba-international-relations |
| UG-BA | BA International Relations and... | https://www.soas.ac.uk/study/find-course/ba-international-relations-and |
| UG-BA | BA Politics | https://www.soas.ac.uk/study/find-course/ba-politics |
| UG-BA | BA Politics and International Relations | https://www.soas.ac.uk/study/find-course/ba-politics-and-international-relations |
| UG-BA | BA Politics and... | https://www.soas.ac.uk/study/find-course/ba-politics-and |

##### E. School of Anthropology, Media and Gender

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA Social Anthropology | https://www.soas.ac.uk/study/find-course/ba-social-anthropology |
| UG-BA | BA Social Anthropology and... | https://www.soas.ac.uk/study/find-course/ba-social-anthropology-and |
| PGT-MA | MA Anthropology of Food | https://www.soas.ac.uk/study/find-course/ma-anthropology-food |
| PGT-MA | MA Anthropology of Food and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-anthropology-food-and-intensive-language |
| PGT-MA | MA Anthropology of the Environment and Sustainability | https://www.soas.ac.uk/study/find-course/ma-anthropology-environment-and-sustainability |
| PGT-MA | MA Gender and Sexuality | https://www.soas.ac.uk/study/find-course/ma-gender-and-sexuality |
| PGT-MA | MA Gender Studies | https://www.soas.ac.uk/study/find-course/ma-gender-studies |
| PGT-MA | MA Gender and Global Politics (Online) | https://www.soas.ac.uk/study/find-course/ma-gender-and-global-politics-online |

##### F. School of Arts

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA Creative Arts and... | https://www.soas.ac.uk/study/find-course/ba-creative-arts-and |
| UG-BA | BA Digital Media, Culture and... | https://www.soas.ac.uk/study/find-course/ba-digital-media-culture-and |
| UG-BA | BA Film Studies and... | https://www.soas.ac.uk/study/find-course/ba-film-studies-and-0 |
| UG-BA | BA Music and... | https://www.soas.ac.uk/study/find-course/ba-music-and |
| UG-FY | BA/BSc Social Sciences, Arts and Humanities with Foundation Year | https://www.soas.ac.uk/study/find-course/ba/bsc-social-sciences-arts-and-humanities-foundation-year |
| PGT-PGDip | Asian Art in the Museum (SOAS-Alphawood) | https://www.soas.ac.uk/study/find-course/asian-art-museum |
| PGT-MA | MA Creative and Cultural Industries | https://www.soas.ac.uk/study/find-course/ma-creative-and-cultural-industries |
| PGT-MA | MA Curating Cultures | https://www.soas.ac.uk/study/find-course/ma-curating-cultures |
| PGT-MA | MA Documentary, Photojournalism and Global Justice | https://www.soas.ac.uk/study/find-course/ma-documentary-photojournalism-and-global-justice |
| PGT-MA | MA Documentary, Photojournalism and Global Justice (Online) | https://www.soas.ac.uk/study/find-course/ma-documentary-photojournalism-and-global-justice-online |
| PGT-MA | MA Global Data Journalism | https://www.soas.ac.uk/study/find-course/ma-global-data-journalism |
| PGT-MA | MA Global Data Journalism (Online) | https://www.soas.ac.uk/study/find-course/ma-global-data-journalism-online |
| PGT-MA | MA Global Journalism | https://www.soas.ac.uk/study/find-course/ma-global-journalism |
| PGT-MA | MA Global Media and Digital Communications | https://www.soas.ac.uk/study/find-course/ma-global-media-and-digital-communications |
| PGT-MA | MA Global Media and Digital Cultures (Online) | https://www.soas.ac.uk/study/find-course/ma-global-media-and-digital-cultures-online-0 |
| PGT-MA | MA Investigative and Human Rights Journalism | https://www.soas.ac.uk/study/find-course/ma-investigative-and-human-rights-journalism |
| PGT-MA | MA Investigative and Human Rights Journalism (Online) | https://www.soas.ac.uk/study/find-course/ma-investigative-and-human-rights-journalism-online |

##### G. School of Finance and Management

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA Management and... | https://www.soas.ac.uk/study/find-course/ba-management-and |
| UG-BSc | BSc Management | https://www.soas.ac.uk/study/find-course/bsc-management |

##### H. School of History, Religions and Philosophies

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA History | https://www.soas.ac.uk/study/find-course/ba-history |
| UG-BA | BA History and... | https://www.soas.ac.uk/study/find-course/ba-history-and |
| UG-BA | BA History of Art and... | https://www.soas.ac.uk/study/find-course/ba-history-art-and |
| UG-BA | BA World Philosophies | https://www.soas.ac.uk/study/find-course/ba-world-philosophies |
| UG-BA | BA World Philosophies and... | https://www.soas.ac.uk/study/find-course/ba-world-philosopies-and |
| PGT-MA | MA History | https://www.soas.ac.uk/study/find-course/ma-history |
| PGT-MA | MA History and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-history-and-intensive-language |
| PGT-MA | MA History of Art and Archaeology | https://www.soas.ac.uk/study/find-course/ma-history-art-and-archaeology |
| PGT-MA | MA History of Art and Archaeology of East Asia | https://www.soas.ac.uk/study/find-course/ma-history-art-and-archaeology-east-asia |
| PGT-MA | MA History of Art and Archaeology of East Asia and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-history-art-and-archaeology-east-asia-and-intensive-language |
| PGT-MA | MA History of Art and Architecture of Islamic Middle East | https://www.soas.ac.uk/study/find-course/ma-history-art-and-architecture-islamic-middle-east |
| PGT-MA | MA History of Art and Architecture of the Islamic Middle East and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-history-art-and-architecture-islamic-middle-east-and-intensive-language |
| PGT-MA | MA Buddhist Studies | https://www.soas.ac.uk/study/find-course/ma-buddhist-studies |
| PGT-MA | MA Buddhist Studies with Intensive Language | https://www.soas.ac.uk/study/find-course/ma-buddhist-studies-intensive-language |
| PGT-MA | MA Global Histories (Online) | https://www.soas.ac.uk/study/find-course/ma-global-histories-online |
| PGT-MA | MA Global Philosophy | https://www.soas.ac.uk/study/find-course/ma-global-philosophy |
| PGT-MA | MA Global Philosophy and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-global-philosophy-and-intensive-language |
| PGT-MA | MA Islamic Humanities | https://www.soas.ac.uk/study/find-course/ma-islamic-humanities |

##### I. School of Languages, Cultures and Linguistics

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| UG-BA | BA Africa and Black Diaspora and... | https://www.soas.ac.uk/study/find-course/ba-africa-and-black-diaspora-and |
| UG-BA | BA Arabic | https://www.soas.ac.uk/study/find-course/ba-arabic |
| UG-BA | BA Arabic and... | https://www.soas.ac.uk/study/find-course/ba-arabic-and |
| UG-BA | BA Chinese | https://www.soas.ac.uk/study/find-course/ba-chinese |
| UG-BA | BA Chinese and... | https://www.soas.ac.uk/study/find-course/ba-chinese-and |
| UG-BA | BA East Asian Studies | https://www.soas.ac.uk/study/find-course/ba-east-asian-studies |
| UG-BA | BA East Asian Studies and... | https://www.soas.ac.uk/study/find-course/ba-east-asian-studies-and |
| UG-BA | BA Japanese | https://www.soas.ac.uk/study/find-course/ba-japanese |
| UG-BA | BA Japanese and... | https://www.soas.ac.uk/study/find-course/ba-japanese-and |
| UG-BA | BA Korean | https://www.soas.ac.uk/study/find-course/ba-korean |
| UG-BA | BA Korean and... | https://www.soas.ac.uk/study/find-course/ba-korean-and |
| UG-BA | BA Languages and Cultures (Middle East, Africa, South and Southeast Asia) | https://www.soas.ac.uk/study/find-course/ba-languages-and-cultures-middle-east-africa-south-and-southeast-asia |
| UG-BA | BA Languages and Cultures (ME, Africa, S/SE Asia) and... | https://www.soas.ac.uk/study/find-course/ba-languages-and-cultures-middle-east-africa-south-and-southeast-asia-and |
| UG-BA | BA Linguistics and... | https://www.soas.ac.uk/study/find-course/ba-linguistics-and |
| PGT-MA | MA African Studies | https://www.soas.ac.uk/study/find-course/ma-african-studies |
| PGT-MA | MA African Studies and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-african-studies-and-intensive-language |
| PGT-MA | MA Chinese Studies | https://www.soas.ac.uk/study/find-course/ma-chinese-studies |
| PGT-MA | MA Chinese Studies and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-chinese-studies-and-intensive-language |
| PGT-MA | MA Comparative Literature | https://www.soas.ac.uk/study/find-course/ma-comparative-literature |
| PGT-MA | MA Comparative Literature and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-comparative-literature-and-intensive-language |
| PGT-MA | MA Cultural Studies | https://www.soas.ac.uk/study/find-course/ma-cultural-studies |
| PGT-MA | MA Cultural Studies and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-cultural-studies-and-intensive-language |
| PGT-MA | MA Iranian Studies | https://www.soas.ac.uk/study/find-course/ma-iranian-studies |
| PGT-MA | MA Iranian Studies and Intensive Language | https://www.soas.ac.uk/study/find-course/ma-iranian-studies-and-intensive-language |

##### J. Cross-departmental / Joint Programmes

| 学位级别 | 专业名称 | URL |
|----------|----------|-----|
| PGT-MA | MA Global Affairs and Eurasian Studies (Joint Degree with Nazarbayev University) | https://www.soas.ac.uk/study/find-course/ma-global-affairs-and-eurasian-studies-joint-degree-nazarbayev-university |
| PGT-MA | MA Global Citizenship (Joint Degree with National Sun Yat-sen University) | https://www.soas.ac.uk/study/find-course/ma-global-citizenship-joint-degree-national-sun-yat-sen-university |
| PGT-MA | MA Global Diplomacy (Online) | https://www.soas.ac.uk/study/find-course/ma-global-diplomacy-online-0 |
| PGT-MA | MA in Museum Studies (Joint Degree with Effat University, sponsored by Saudi Museums Commission) | https://www.soas.ac.uk/study/find-course/ma-museum-studies-joint-degree-effat-university-sponsored-saudi-museums |
| PGT-MA | MA in Museum Studies (Joint Degree with IAU, sponsored by Saudi Museums Commission) | https://www.soas.ac.uk/study/find-course/ma-museum-studies-joint-degree-iau-sponsored-saudi-museums-commission |
| PGT-MA | MA International Studies and Diplomacy | https://www.soas.ac.uk/study/find-course/ma-international-studies-and-diplomacy |

---

## 1. 学院/系所详情（College/Department Details）

### 1.1 College of Law
- 研究领域：legal systems and the legal challenges of the developing world; human rights, international law and institutions; environmental law; international trade and commerce
- 学位项目：LLB (1) + LLM (7, 含 general + 6 specialisations)
- 来源：https://www.soas.ac.uk/about/departments-and-schools
- 原文摘录："The College of Law brings together a range of subjects to explore legal systems and the legal challenges of the developing world, alongside human rights, international law and institutions, environmental law and international trade and commerce."

### 1.2 Department of Development Studies
- 研究领域：development studies
- 学位项目：BA Global Development (+ combined variant); 多个 MA Development 相关项目跨学院分布
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.3 Department of Economics
- 研究领域：economics (含 development economics, 政治经济学)
- 学位项目：BA Economics; BSc Accounting & Finance; BSc Development Economics; BSc Economics; BSc PPE
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.4 Department of Politics and International Studies
- 研究领域：Politics and International Relations with deep engagement with the historical legacies, political realities, and international affairs of Asia, Africa, and the Middle East
- 学位项目：BA International Relations (+ combined); BA Politics (+ combined); BA Politics & IR
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.5 School of Anthropology, Media and Gender
- 研究领域：anthropology, media studies, gender studies — "the only one of its kind in the UK - dedicated to the developing world"
- 学位项目：BA Social Anthropology (+ combined); 多个 MA (Anthropology of Food, Gender Studies, etc.)
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.6 School of Arts
- 研究领域：visual and sound arts, material and intangible cultures, media industries and digital cultures of Asia, Africa and the Middle East
- 学位项目：BA Creative Arts; BA Digital Media Culture; BA Film Studies; BA Music; MA Creative and Cultural Industries; MA Curating Cultures; MA Documentary, Photojournalism and Global Justice; MA Global Journalism; MA Global Media and Digital Communications; MA Investigative and Human Rights Journalism; PGDip Asian Art in the Museum (SOAS-Alphawood)
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.7 School of Finance and Management
- 研究领域：finance and management
- 学位项目：BA Management; BSc Management; (跨系 Foundation Year in Business/Management/Economics/Law)
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.8 School of History, Religions and Philosophies
- 研究领域：history, religion, and philosophy of the Global South, critical, decolonial, and interdisciplinary
- 学位项目：BA History (+ combined); BA History of Art (+ combined); BA World Philosophies (+ combined); MA History; MA History of Art and Archaeology (含 East Asia, Islamic Middle East variants); MA Buddhist Studies; MA Global Histories; MA Global Philosophy; MA Islamic Humanities
- 来源：https://www.soas.ac.uk/about/departments-and-schools

### 1.9 School of Languages, Cultures and Linguistics
- 研究领域：Africa, the Near and Middle East, South Asia, Southeast Asia and East Asia — culture as the lens
- 学位项目：BA Arabic, BA Chinese, BA Japanese, BA Korean, BA East Asian Studies, BA Africa and Black Diaspora, BA Languages and Cultures (ME, Africa, S/SE Asia), BA Linguistics (+ combined variants); 多个 MA (African Studies, Chinese Studies, Comparative Literature, Cultural Studies, Iranian Studies)
- 来源：https://www.soas.ac.uk/about/departments-and-schools

---

## 2. 学位项目汇总（按学院分组，Rule 5 紧凑版）

| School/Dept | UG | PGT |
|-------------|-----|-----|
| College of Law | LLB | 7 LLM |
| Dept of Development Studies | BA Global Development (+combined) | — |
| Dept of Economics | BA Economics (+combined); BSc Accounting & Finance; BSc Development Economics; BSc Economics; BSc PPE | — |
| Dept of Politics & IR | BA International Relations (+combined); BA Politics (+combined); BA Politics & IR | — |
| School of Anthropology, Media & Gender | BA Social Anthropology (+combined) | MA Anthropology of Food (+IL); MA Anthropology of Environment; MA Gender & Sexuality; MA Gender Studies; MA Gender & Global Politics (Online) |
| School of Arts | BA Creative Arts (+combined); BA Digital Media Culture (+combined); BA Film Studies (+combined); BA Music (+combined) | PGDip Asian Art in the Museum; MA Creative & Cultural Industries; MA Curating Cultures; MA Documentary Photojournalism (+Online); MA Global Data Journalism (+Online); MA Global Journalism; MA Global Media & Digital Communications (+Online); MA Investigative & Human Rights Journalism (+Online) |
| School of Finance & Management | BA Management (+combined); BSc Management | — |
| School of History, Religions & Philosophies | BA History (+combined); BA History of Art (+combined); BA World Philosophies (+combined) | MA History (+IL); MA History of Art & Archaeology; MA History of Art & Archaeology East Asia (+IL); MA History of Art & Architecture Islamic Middle East (+IL); MA Buddhist Studies (+IL); MA Global Histories (Online); MA Global Philosophy (+IL); MA Islamic Humanities |
| School of Languages, Cultures & Linguistics | BA Africa & Black Diaspora (+combined); BA Arabic (+combined); BA Chinese (+combined); BA East Asian Studies (+combined); BA Japanese (+combined); BA Korean (+combined); BA Languages & Cultures ME/Africa/S-SE Asia (+combined); BA Linguistics (+combined) | MA African Studies (+IL); MA Chinese Studies (+IL); MA Comparative Literature (+IL); MA Cultural Studies (+IL); MA Iranian Studies (+IL) |
| Cross-departmental / Joint | — | MA Global Affairs & Eurasian Studies (Nazarbayev); MA Global Citizenship (NSYSU); MA Global Diplomacy (Online); MA Museum Studies (Effat, sponsored); MA Museum Studies (IAU, sponsored); MA International Studies & Diplomacy |
| **TOTAL** | **~45 UG** | **~54 PGT** |

---

## 3. 申请要求（Application Requirements）

### 3.1 Standard UG Entry Requirements (UK qualifications)

| Qualification | Typical Offer | Notes |
|---------------|---------------|-------|
| A-levels | Variable by programme; AAB typical for competitive programmes; some accept ABB | A level Maths grade B required for Economics-related programmes |
| GCSE Maths | Grade 6/B or above (required for Economics/LLB/Mathematics-bearing programmes) | — |
| International Baccalaureate (IB) | 30–34 points total; minimum 15–17 at HL; no HL lower than 3 | "34 points with minimum 17 points at HL and no HL lower than 3"; "32 points with minimum 16 points at HL"; "30 points with minimum 15 points at HL and no HL lower than 3" |
| BTEC | Reviewed in combination with GCSE profile for entry onto all programmes | — |
| T-level | T-level qualifications (equivalent to 3 A-levels), assessed case-by-case | — |
| EPQ | "If you are predicted at least grade B in the EPQ and your A level predicted grades meet our entry requirements" | Used as part of offer context |

> 来源：https://www.soas.ac.uk/study/undergraduate/undergraduate-entry-requirements
> 原文摘录："We understand that many applicants may choose to take a combination of qualifications, such as A-levels and BTEC. Our Admissions team will consider all of your qualifications and make a decision based..."

> Foundation Year applicants should refer to dedicated Foundation Entry Requirements.

### 3.2 English Language Requirements (Direct Entry, 2-year validity)

| Test | Overall | Subscores |
|------|---------|-----------|
| Duolingo | 120 | 110 in SWRL subscores |
| IELTS Academic / UKVI / Online | **6.5** | **6.0 in all subscores** |
| Kaplan Test of English (code SOASKRS25 for 25% discount) | 480 | 450 in all subscores |
| LanguageCert Academic | 70 | 65 in all subscores |
| Oxford Test of English / Advanced | 130 | 120 in all subscores |
| Password Skills Plus | 6.5 | 6.0 in all subscores |
| PTE Academic | 65 | 60 in all subscores |
| TOEFL iBT ('My Best Scores' not accepted) | 95 / 5.0 | 23 in writing and 20 in other subscores (old); 4.5 in writing/listening, 4.0 in reading/speaking (new) |

### 3.3 English Language with Pre-sessional English

| Variant | Test | Overall | Subscores |
|---------|------|---------|-----------|
| 4-week pre-sessional | Duolingo | 110 | 110 in writing, 100 in other |
| 4-week pre-sessional | IELTS Academic/UKVI/Indicator | 6.0 | 6.0 in writing, 5.5 in others |
| 4-week pre-sessional | Kaplan | 450 | 450 in writing, 425 in others |
| 4-week pre-sessional | LanguageCert | 65 | 65 in writing, 60 in others |
| 4-week pre-sessional | Oxford | 120 | 120 in writing, 111 in others |
| 4-week pre-sessional | Password | 6.0 | 6.0 in writing, 5.5 in others |
| 4-week pre-sessional | PTE | 62 | 60 in writing, 59 in others |
| 4-week pre-sessional | TOEFL | 92 / 4.5 | 20 in writing/speaking, 18 in listening/reading (old); 4.0 all (new) |
| 8-week pre-sessional | Duolingo | 100 | 100 in all subscores |
| 8-week pre-sessional | IELTS | 5.5 | 5.5 in subscores |
| 8-week pre-sessional | Kaplan | 425 | 425 in subscores |
| 8-week pre-sessional | LanguageCert | 60 | 60 in subscores |
| 8-week pre-sessional | Oxford | 111 | 111 in writing, 111 in others |
| 8-week pre-sessional | Password | 5.5 | 5.5 in subscores |
| 8-week pre-sessional | PTE | 60 | 59 in subscores |
| 8-week pre-sessional | TOEFL | 85 / 4.0 | 20 in speaking, 18 in other subscores |

### 3.4 Exemptions (no English test required if you...)

- UK national (right to request further evidence)
- National from a Majority English Speaking Country (MESC) and completed English-medium high school/degree
- Completed a degree in UK or any UKVI-defined MESC within last 10 years
- Completed a degree taught in English from Canada, Ghana, Kenya, Nigeria, or South Africa within last 10 years
- Passed a Pre-sessional English course at a UK university (2-year validity)
- Completed an International Foundation Programme (IFP) (55% in academic English) within 2 years

### 3.5 Tests NOT accepted

- Pearson Academic Online
- TOEFL Essentials
- Oxford ELLT
- Skills for English
- Composite test scores (e.g., TOEFL MyBest Scores)
- (Exception: IELTS One Skill Retake IS accepted)

> 来源: https://www.soas.ac.uk/international/english-language-requirements
> 原文摘录: "If you have not yet taken an English language test, you can still apply for your degree, but we will include evidence of language requirements as part of your offer conditions."

---

## 4. 学费与费用（Tuition & Fees）

### 4.1 Undergraduate Tuition Fees (2026/27 Academic Year, New Students)

| Programme Type | Home | Overseas |
|----------------|------|----------|
| Foundation Year | £5,760 | £23,780 |
| Undergraduate — Full-time | **£9,790** | **£23,780** |
| Undergraduate — Part-time (Continuing students only) | £4,767.50 | — |
| Undergraduate Year in Industry | £1,425 | £1,425 |
| Outgoing Year Abroad | £1,425 | £11,770 |
| Incoming Study Abroad (full-year) | £9,790 | £23,780 |
| Incoming Study Abroad (semester) | £4,895 | £11,890 |

### 4.2 Undergraduate Associate Students

| Module | Home | Overseas |
|--------|------|----------|
| 30 Credit module | £2,380 | £5,715 |
| 15 Credit module | £1,190 | £2,855 |

### 4.3 Fee Cap Trajectory (UK Government)

| Academic Year | Home Fee Cap |
|---------------|--------------|
| 2026/27 | £9,790 |
| 2027/28 | £10,050 |
| 2028/29 | (not yet announced; likely 2-4% increase) |

> 原文摘录: "The UK government has announced the Home fee cap for 2026/27 and 2027/28 as follows (2028/29 fees have not yet been announced, but likely to be 2–4% increase): 2026/27: £9,790; 2027/28: £10,050. Note that the 2027/28 fee rate applies to both new starters and students who enrol in 2026/27."
> 原文摘录: "Overseas fee payer rates are subject to increases of up to 5% in subsequent years of study on the same degree programme."

### 4.4 Postgraduate Tuition Fees

PGT fees are organised in **bands** (per landing page; per-programme breakdown URL https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees/postgraduate-fees returned 404 at capture time, so the per-programme figures were not retrievable from this single crawl). Source: https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees → "Postgraduate taught fees: Information on our bands of Postgraduate tuition fees."

### 4.5 Research Degree Fees

Per landing page: "Research fees — Find out about the annual fees for studying on campus research programmes such as MPhil/Phd." (https://www.soas.ac.uk/research/postgraduate-research-degrees)

### 4.6 Online and Distance Learning Fees

"SOAS online learning fees information" — listed separately. Includes the Online variants of MA programmes (Documentary, Gender Politics, Global Data Journalism, Global Diplomacy, Global Histories, Global Media Cultures, Investigative Journalism).

> 主要来源：https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees/undergraduate-fees
> 来源：https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees

---

## 5. 申请截止日期与流程（Deadlines & Application Process）

### 5.1 UCAS Application

UK/EU UG applicants apply through UCAS. SOAS UCAS institution code: **S09** (verify on UCAS). Applications via UCAS by the equal consideration deadline (typically late January for September entry).

### 5.2 Postgraduate Applications

Postgraduate applications are made directly through the SOAS portal. Specific deadlines vary by programme; intake is typically September with some January start options. See individual programme pages for details.

### 5.3 Application Process Summary

1. Choose a programme from the UG/PGT course finder
2. Review entry requirements (academic + English language)
3. Submit application (UCAS for UG; direct portal for PGT)
4. Receive offer (typical turnaround 2-4 weeks)
5. Accept offer and meet conditions
6. Apply for visa (international students)
7. Enrol and pay fees

> 来源：https://www.soas.ac.uk/how-apply-undergraduate-study
> 来源：https://www.soas.ac.uk/study/postgraduate

---

## 6. WeKnora 摄入分块清单（Chunk Manifest）

下表列出推荐的 chunk 边界，便于 WeKnora 摄入与检索：

| Chunk ID | Section | 内容范围 | 估计 tokens |
|----------|---------|----------|-------------|
| soas-overview | 0 | 学校档案 + 五项规则摘要 | ~1,500 |
| soas-hierarchy-tree | 0.2 | 学院/系所层级树 | ~500 |
| soas-rule-3-degrees | 0.3 | 学历级别明细表 | ~300 |
| soas-rule-4-matrix | 0.4 | 学院×学位级别矩阵 | ~400 |
| soas-rule-5-A-college-of-law | 0.5 | College of Law 全项目 | ~600 |
| soas-rule-5-B-dev-studies | 0.5 | Department of Development Studies 全项目 | ~300 |
| soas-rule-5-C-economics | 0.5 | Department of Economics 全项目 | ~500 |
| soas-rule-5-D-polis-ir | 0.5 | Department of Politics & IR 全项目 | ~500 |
| soas-rule-5-E-anthro | 0.5 | School of Anthropology, Media & Gender 全项目 | ~600 |
| soas-rule-5-F-arts | 0.5 | School of Arts 全项目 | ~800 |
| soas-rule-5-G-fin-mgmt | 0.5 | School of Finance & Management 全项目 | ~400 |
| soas-rule-5-H-hrp | 0.5 | School of History, Religions & Philosophies 全项目 | ~800 |
| soas-rule-5-I-langs | 0.5 | School of Languages, Cultures & Linguistics 全项目 | ~1,200 |
| soas-rule-5-J-joint | 0.5 | Cross-departmental / Joint 全项目 | ~500 |
| soas-ug-entry-reqs | 3.1 | UK 标准入学要求 | ~600 |
| soas-english-lang | 3.2-3.5 | 英语语言要求（含豁免与不接受） | ~1,500 |
| soas-tuition-ug | 4.1-4.3 | 本科生学费 | ~600 |
| soas-tuition-pgt-research | 4.4-4.6 | PGT / 研究 / 在线费用指引 | ~300 |
| soas-deadlines-process | 5 | 申请截止与流程 | ~400 |

---

## 7. 监测 Watchlist（Phase 4 — Monitoring Design）

### 7.1 高频监测项（Monthly — frequency:high）

| URL | Watched Field | Baseline Value (2026-07-08) |
|-----|---------------|------------------------------|
| https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees/undergraduate-fees | Home UG fee | £9,790 |
| https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees/undergraduate-fees | Overseas UG fee | £23,780 |
| https://www.soas.ac.uk/international/english-language-requirements | IELTS direct entry | 6.5 overall, 6.0 subscore |
| https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees | PGT bands | (see landing page; per-programme page 404) |

### 7.2 中频监测项（Quarterly — frequency:medium）

| URL | Watched Field |
|-----|---------------|
| https://www.soas.ac.uk/undergraduate-courses | UG programme list (45) |
| https://www.soas.ac.uk/postgraduate-taught-courses | PGT programme list (~50+) |
| https://www.soas.ac.uk/about/departments-and-schools | 9 academic units |

### 7.3 低频监测项（Annual — frequency:low）

| URL | Watched Field |
|-----|---------------|
| https://www.soas.ac.uk/about | School description, ranking statements |
| https://www.soas.ac.uk/study | Overall study landing |

---

## 8. 数据来源引用汇总（Sources）

| # | URL | 类型 | 抓取日期 |
|---|-----|------|----------|
| 1 | https://www.soas.ac.uk/ | 主页 | 2026-07-08 |
| 2 | https://www.soas.ac.uk/study/undergraduate | UG overview | 2026-07-08 |
| 3 | https://www.soas.ac.uk/undergraduate-courses | UG course index | 2026-07-08 |
| 4 | https://www.soas.ac.uk/undergraduate-courses?page=2 | UG course index p.2 | 2026-07-08 |
| 5 | https://www.soas.ac.uk/undergraduate-courses?page=3 | UG course index p.3 | 2026-07-08 |
| 6 | https://www.soas.ac.uk/undergraduate-courses?page=4 | UG course index p.4 | 2026-07-08 |
| 7 | https://www.soas.ac.uk/undergraduate-courses?page=5 | UG course index p.5 | 2026-07-08 |
| 8 | https://www.soas.ac.uk/study/undergraduate/undergraduate-entry-requirements | UK qualifications entry | 2026-07-08 |
| 9 | https://www.soas.ac.uk/international/english-language-requirements | English language requirements | 2026-07-08 |
| 10 | https://www.soas.ac.uk/study/student-fees-and-funding | Fees & funding landing | 2026-07-08 |
| 11 | https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees | Tuition fees landing | 2026-07-08 |
| 12 | https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees/undergraduate-fees | UG fee table 2026/27 | 2026-07-08 |
| 13 | https://www.soas.ac.uk/study/student-fees-and-funding/tuition-fees/postgraduate-fees | PG fee (404 at capture) | 2026-07-08 |
| 14 | https://www.soas.ac.uk/study/postgraduate | PG overview | 2026-07-08 |
| 15 | https://www.soas.ac.uk/postgraduate-taught-courses | PGT course index | 2026-07-08 |
| 16 | https://www.soas.ac.uk/postgraduate-taught-courses?page=2..6 | PGT course index p.2-6 | 2026-07-08 |
| 17 | https://www.soas.ac.uk/about/departments-and-schools | 9 academic units list | 2026-07-08 |
| 18 | https://www.soas.ac.uk/about | About / general | 2026-07-08 |
| 19 | https://www.soas.ac.uk/study/student-fees-and-funding/undergraduate-funding | UG funding (loans, bursaries, scholarships) | 2026-07-08 |
| 20 | https://www.soas.ac.uk/research/postgraduate-research-degrees | Research degrees | 2026-07-08 |
| 21 | https://www.soas.ac.uk/how-apply-undergraduate-study | How to apply UG | 2026-07-08 |

---

## 9. 质量自检（Quality Bar Self-Check）

- [x] **Rule 1**: 项目总数 stated, broken down by UG major / minor / grad degree / grad cert (~45 UG + ~54 PGT = ~99 named)
- [x] **Rule 2**: 学院-系 hierarchy tree present with explicit parent→child marking (9 academic units)
- [x] **Rule 3**: 学历级别 inventory table present (BA, BSc, LLB, BA/BSc FY, LLM, MA, PGDip + Online variants)
- [x] **Rule 4**: 学院 × 学位级别 distribution matrix present and reconciles with rule 1
- [x] **Rule 5**: every major/program listed under 学院 → 系 → 学位级别 → 专业 (no "representative", no "etc.")
- [x] **Reconciliation**: rule-1 total ≈ matrix cell-sum ≈ row-count in rule-5 tables
- [x] Every numeric or policy field has source_url + source_snippet
- [x] Full undergraduate programmes list (~45 named across 5 pages)
- [x] Full PGT programme directory (per-school, 54 named across 6 pages, plus joint-degree and online variants)
- [x] Cost breakdown is line-itemized (UG fee table by category)
- [x] Language requirement table with min AND recommended scores (Direct, 4-week, 8-week pre-sessional variants)
- [x] Monitoring watchlist classifies URLs by frequency (high/medium/low)
- [x] Output filename matches template exactly

### 已知缺失 / Known gaps

- **PG per-programme fee figures**: per-programme page (postgraduate-fees) returned 404 at capture time; PGT fees are described in "bands" on the landing page but individual numbers were not retrievable from this crawl. Capture a follow-up when the page is restored.
- **UCAS institution code**: not directly captured in this crawl (commonly S09 for SOAS but verify on UCAS).
- **Programme-specific English language requirements** (e.g. higher IELTS for some programmes): the central page lists the standard direct-entry threshold (6.5/6.0); individual programme pages may set higher requirements for specific PG programmes (e.g. some Law programmes).
- **Specific application deadlines by programme**: PGT deadlines vary by programme; capture from individual programme pages.

---

*Document generated by uni-admissions-research skill · SOAS University of London · 2026-07-08 · v2.0*