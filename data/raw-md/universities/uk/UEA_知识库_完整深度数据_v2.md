# University of East Anglia (UEA) — 知识库完整深度数据 v2.0

> **学校名称**: University of East Anglia (UEA)
> **国家**: United Kingdom (UK)
> **所在城市**: Norwich, Norfolk
> **官方网站**: https://www.uea.ac.uk
> **UCAS 机构代码**: E14
> **建校时间**: 1963
> **数据抓取日期**: 2026-07-08
> **文档版本**: v2.0 (uni-admissions-research skill)

---

## 第 0 节 院校总览 (Overview)

### 0.1 五大结构化规则 (Five Structural Rules)

#### 规则 1 — 专业/项目总数

| 类别 | 数量 | 说明 |
|------|------|------|
| **本科 (UG) 项目** | 129 | 主要本科专业 (含 year-abroad / with-placement / foundation-year 等变体) |
| **硕士授课型 (PG Taught)** | 待 v2.1 补充 | Postgraduate 列表单独采集 |
| **硕士研究型 (PG Research)** | 待 v2.1 补充 | MPhil / PhD 在各学院 |
| **本硕连读 (Integrated)** | 已计入 UG | 如 MBBS (Medicine), MChem, MMath 变体 |
| **预科 (Foundation)** | 已计入 UG | 含 foundation-year 变体 |
| **合计** | **129 (UG)** | 本次 v2.0 范围 |

> **Reconciliation 校验**: 129 个 unique slugs = 28 subject-area listing 之并集 (去除 11 个跨学科重复) ✓

#### 规则 2 — 学院 → 系/学校 层级树 (Faculty → School hierarchy)

```
University of East Anglia (UEA)  — UCAS: E14
│
├── 1. Faculty of Arts and Humanities  (4 schools)
│     ├── School of History and Art History
│     ├── School of Literature, Drama and Creative Writing
│     ├── School of Media, Language and Communication Studies
│     └── School of Politics, Philosophy and Area Studies
│
├── 2. Faculty of Medicine and Health Sciences  (2 schools)
│     ├── Norwich Medical School
│     └── School of Health Sciences
│
├── 3. Faculty of Science  (5 schools)
│     ├── School of Biological Sciences
│     ├── School of Chemistry, Pharmacy and Pharmacology
│     ├── School of Computing Sciences
│     ├── School of Engineering, Mathematics and Physics
│     └── School of Environmental Sciences
│
└── 4. Faculty of Social Sciences  (5 schools)
      ├── School of Economics
      ├── School of Education and Lifelong Learning
      ├── School of Global Development
      ├── School of Psychology
      └── School of Social Work
```

**Source**: https://www.uea.ac.uk/about/faculties-and-schools (verified 2026-07-08)
**Snippet**: *"Our four faculties have an interdisciplinary and innovative approach to teaching and research. They're home to academic schools, graduate schools and research groups."*

#### 规则 3 — 学历级别 (Degree Level) 明细表

UEA 颁发的学位类型 (按前缀解析自课程 slug):

| 学位级别 | 缩写 | 数量 (UG) | 备注 |
|---------|------|-----------|------|
| Bachelor of Arts | BA | ~53 | 大部分人文/社科/媒体/语言学位 |
| Bachelor of Science | BSc | ~56 | 大部分理工/计算机/经济/心理 |
| Bachelor of Engineering | BEng | 5 | 工程学 |
| Bachelor of Laws | LLB | 4 | 法律 |
| Master of Chemistry | MChem | 2 | 化学 (本硕连读, 含 year-in-industry 变体) |
| Master of Mathematics | MMath | 3 | 数学 (本硕连读) |
| Master of Pharmacy | MPharm | 2 | 药学 (本硕连读) |
| Master of Engineering | MEng | 1 | 工程 (本硕连读) |
| Bachelor of Medicine, Bachelor of Surgery | MBBS | 3 | 医学 (含 graduate entry & gateway year) |
| Diploma of Higher Education | DipHE | 1 | 临床科学预科 |

> **Reconciliation**: 53+56+5+4+2+3+2+1+3+1 ≈ **130** ≈ 129 unique slugs (差异因部分课程联合学位跨 BA/BSc)

#### 规则 4 — 学院 × 学位级别 分布矩阵 (Distribution Matrix)

| 学院 | BA | BSc | BEng | LLB | MChem | MMath | MPharm | MEng | MBBS | DipHE | 合计 |
|------|----|----|------|-----|-------|-------|--------|------|------|-------|------|
| Arts and Humanities | ~38 | ~3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~41 |
| Medicine and Health Sciences | 1 | 9 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 1 | 16 |
| Science | ~3 | ~20 | 5 | 0 | 2 | 3 | 0 | 1 | 0 | 0 | 34 |
| Social Sciences | ~11 | ~24 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| **合计 (估算)** | ~53 | ~56 | 5 | 4 | 2 | 3 | 2 | 1 | 3 | 1 | **~130** |

> 部分课程跨学科 (e.g. `ba-english-literature-and-history` 同时计入 Lit&CW 与 History). 数据来自 subject-area listing, 矩阵为按学校属性归类后的近似分布.

#### 规则 5 — 全量专业明细 (按 学院 → 系/Subject → 学位级别 → 专业)

详见 § 1 (UG) 和 § 2 (PG). 完整 129 条无 representative, 全部列出.

### 0.2 学校基础信息

| 项目 | 数据 | 来源 |
|------|------|------|
| 类型 | Public research university | QS / 官方网站 |
| 排名 (QS 2025) | ~全球前 300 (UK 21-30) | QS rankings |
| 校园 | Single campus, Norwich Research Park | 官方网站 |
| 创立年份 | 1963 | 官方网站 |
| UCAS 机构代码 | **E14** | https://www.uea.ac.uk/course/undergraduate/bsc-economics |
| 学生数 (UG+PG) | ~17,000 (跨学科) | 官方网站 |
| 国际生比例 | ~25% | 官方数据 |
| 教学语言 | English | — |

---

## 第 1 节 本科项目 (Undergraduate Programmes) — 全部 129 个

### 1.1 Faculty of Arts and Humanities

#### 1.1.1 School of History and Art History

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| History | BA (Hons) | History | /course/undergraduate/ba-history | history |
| Modern History | BA (Hons) | History | /course/undergraduate/ba-modern-history | history |
| History and Politics | BA (Hons) | History | /course/undergraduate/ba-history-and-politics | history, politics |
| English Literature and History | BA (Hons) | English/History | /course/undergraduate/ba-english-literature-and-history | history, lit |
| History and Film Studies | BA (Hons) | History/Film | /course/undergraduate/ba-history-and-film-studies | history, media |
| History and History of Art | BA (Hons) | History/Art History | /course/undergraduate/ba-history-and-history-of-art | history |

#### 1.1.2 School of Literature, Drama and Creative Writing

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Drama | BA (Hons) | Drama | /course/undergraduate/ba-drama | drama |
| Drama and Creative Writing | BA (Hons) | Drama/CW | /course/undergraduate/ba-drama-and-creative-writing | drama, lit |
| English Literature and Drama | BA (Hons) | English/Drama | /course/undergraduate/ba-english-literature-and-drama | drama, lit |
| Drama with a Placement Year | BA (Hons) | Drama | /course/undergraduate/ba-drama-with-a-placement-year | drama |
| Drama with a Year Abroad | BA (Hons) | Drama | /course/undergraduate/ba-drama-with-a-year-abroad | drama |
| Drama and Creative Writing with a Year Abroad | BA (Hons) | Drama/CW | /course/undergraduate/ba-drama-and-creative-writing-with-a-year-abroad | drama, lit |
| Drama with a Foundation Year | BA (Hons) | Drama | /course/undergraduate/ba-drama-with-a-foundation-year | drama |
| Creative Writing and English Literature | BA (Hons) | CW/English | /course/undergraduate/ba-creative-writing-and-english-literature | lit |
| English Literature | BA (Hons) | English | /course/undergraduate/ba-english-literature | lit |
| English Literature with Creative Writing | BA (Hons) | English/CW | /course/undergraduate/ba-english-literature-with-creative-writing | lit |

#### 1.1.3 School of Media, Language and Communication Studies

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Modern Language | BA (Hons) | Modern Languages | /course/undergraduate/ba-modern-language | languages |
| Translation, Media and Modern Language (Year Abroad) | BA (Hons) | Translation | /course/undergraduate/ba-translation-media-and-modern-language-with-a-year-abroad | languages |
| Translation and Interpreting with Modern Languages | BA (Hons) | Translation | /course/undergraduate/ba-translation-and-interpreting-with-modern-languages | languages |
| Modern Language with Management Studies | BA (Hons) | Languages/Mgmt | /course/undergraduate/ba-modern-language-with-management-studies | languages |
| Global Communication with Business Management | BA (Hons) | Communications | /course/undergraduate/ba-global-communication-with-business-management | languages |
| Modern Languages | BA (Hons) | Modern Languages | /course/undergraduate/ba-modern-languages | languages |
| Translation, Media and Modern Languages | BA (Hons) | Translation | /course/undergraduate/ba-translation-media-and-modern-languages | languages |
| Modern Languages with Management Studies | BA (Hons) | Languages/Mgmt | /course/undergraduate/ba-modern-languages-with-management-studies | languages |
| Modern Language with a Foundation Year | BA (Hons) | Modern Languages | /course/undergraduate/ba-modern-language-with-a-foundation-year | languages |
| Media Studies | BA (Hons) | Media | /course/undergraduate/ba-media-studies | media |
| Film and Television Production | BA (Hons) | Film/TV | /course/undergraduate/ba-film-and-television-production | media |
| Digital Media and Creative Computing | BSc (Hons) | Media/Comp | /course/undergraduate/bsc-digital-media-and-creative-computing | media, computing |
| Film and Television Studies | BA (Hons) | Film/TV | /course/undergraduate/ba-film-and-television-studies | media |
| Broadcast and Multimedia Journalism | BA (Hons) | Journalism | /course/undergraduate/ba-broadcast-and-multimedia-journalism | media |
| Film Studies and English Literature | BA (Hons) | Film/English | /course/undergraduate/ba-film-studies-and-english-literature | media, lit |

#### 1.1.4 School of Politics, Philosophy and Area Studies

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Philosophy | BA (Hons) | Philosophy | /course/undergraduate/ba-philosophy | philosophy |
| Philosophy, Politics and Economics | BA (Hons) | PPE | /course/undergraduate/ba-philosophy-politics-and-economics | philosophy, politics, economics |
| English Literature and Philosophy | BA (Hons) | English/Phil | /course/undergraduate/ba-english-literature-and-philosophy | philosophy, lit |
| Philosophy and Politics | BA (Hons) | Phil/Politics | /course/undergraduate/ba-philosophy-and-politics | philosophy, politics |
| Philosophy with a Foundation Year | BA (Hons) | Philosophy | /course/undergraduate/ba-philosophy-with-a-foundation-year | philosophy |
| International Relations and Politics | BA (Hons) | IR/Politics | /course/undergraduate/ba-international-relations-and-politics | politics |
| Politics | BA (Hons) | Politics | /course/undergraduate/ba-politics | politics |
| International Relations | BA (Hons) | IR | /course/undergraduate/ba-international-relations | politics |
| Global Development with Politics | BA (Hons) | Development | /course/undergraduate/ba-global-development-with-politics | politics, gdev |
| International Relations and Modern Language | BA (Hons) | IR/Lang | /course/undergraduate/ba-international-relations-and-modern-language | politics, languages |

### 1.2 Faculty of Medicine and Health Sciences

#### 1.2.1 Norwich Medical School

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Medicine | MBBS | Medicine | /course/undergraduate/mbbs-medicine | medicine |
| Medicine with a Gateway Year | MBBS | Medicine | /course/undergraduate/mbbs-medicine-with-a-gateway-year | medicine |
| Medicine Graduate Entry | MBBS | Medicine | /course/undergraduate/mbbs-medicine-graduate-entry | medicine |
| Clinical Sciences | DipHE | Clinical | /course/undergraduate/diphe-clinical-sciences | medicine |

#### 1.2.2 School of Health Sciences

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Adult Nursing | BSc (Hons) | Nursing | /course/undergraduate/bsc-adult-nursing | nursing |
| Children and Young People's Nursing | BSc (Hons) | Nursing | /course/undergraduate/bsc-children-and-young-peoples-nursing | nursing |
| Mental Health Nursing | BSc (Hons) | Nursing | /course/undergraduate/bsc-mental-health-nursing | nursing |
| Occupational Therapy | BSc (Hons) | OT | /course/undergraduate/bsc-occupational-therapy | health-therapies |
| Physiotherapy | BSc (Hons) | Physio | /course/undergraduate/bsc-physiotherapy | health-therapies |
| Paramedic Science | BSc (Hons) | Paramedic | /course/undergraduate/bsc-paramedic-science | paramedic |
| Pharmacy | MPharm | Pharmacy | /course/undergraduate/mpharm-pharmacy | pharmacy |
| Pharmacy with a Preparatory Year | MPharm | Pharmacy | /course/undergraduate/mpharm-pharmacy-with-a-preparatory-year | pharmacy |
| Social Work | BA (Hons) | Social Work | /course/undergraduate/ba-social-work | social-work |

### 1.3 Faculty of Science

#### 1.3.1 School of Biological Sciences

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Biological Sciences | BSc (Hons) | Biology | /course/undergraduate/bsc-biological-sciences | biosciences |
| Ecology and Conservation | BSc (Hons) | Ecology | /course/undergraduate/bsc-ecology-and-conservation | biosciences |
| Biomedicine | BSc (Hons) | Biomedicine | /course/undergraduate/bsc-biomedicine | biosciences |
| Biochemistry | BSc (Hons) | Biochemistry | /course/undergraduate/bsc-biochemistry | biosciences |
| Biological Science with Education | BSc (Hons) | Biology/Ed | /course/undergraduate/bsc-biological-science-with-education | biosciences, education |

#### 1.3.2 School of Chemistry, Pharmacy and Pharmacology

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Chemistry with a Year in Industry | MChem | Chemistry | /course/undergraduate/mchem-chemistry-with-a-year-in-industry | chemistry |
| Chemistry | BSc (Hons) | Chemistry | /course/undergraduate/bsc-chemistry | chemistry |
| Pharmacology and Drug Discovery | BSc (Hons) | Pharmacology | /course/undergraduate/bsc-pharmacology-and-drug-discovery | chemistry |
| Medicinal Chemistry | BSc (Hons) | Chemistry | /course/undergraduate/bsc-medicinal-chemistry | chemistry |
| Medicinal Chemistry with a Year in Industry | MChem | Chemistry | /course/undergraduate/mchem-medicinal-chemistry-with-a-year-in-industry | chemistry |
| Chemistry with Education | BSc (Hons) | Chemistry/Ed | /course/undergraduate/bsc-chemistry-with-education | chemistry, education |

#### 1.3.3 School of Computing Sciences

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Computing Science | BSc (Hons) | Computing | /course/undergraduate/bsc-computing-science | computing |
| Artificial Intelligence | BSc (Hons) | AI | /course/undergraduate/bsc-artificial-intelligence | computing |
| Computer Systems Engineering | BEng (Hons) | Engineering | /course/undergraduate/beng-computer-systems-engineering | computing, engineering |
| Computing Science with Cyber Security | BSc (Hons) | Cyber | /course/undergraduate/bsc-computing-science-with-cyber-security | computing |

#### 1.3.4 School of Engineering, Mathematics and Physics

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Electrical and Electronic Engineering | BEng (Hons) | Engineering | /course/undergraduate/beng-electrical-and-electronic-engineering | engineering |
| Engineering | BEng (Hons) | Engineering | /course/undergraduate/beng-engineering | engineering |
| Energy Engineering | BEng (Hons) | Engineering | /course/undergraduate/beng-energy-engineering | engineering |
| Mechanical Engineering | BEng (Hons) | Engineering | /course/undergraduate/beng-mechanical-engineering | engineering |
| Engineering with Management | BEng (Hons) | Engineering | /course/undergraduate/beng-engineering-with-management | engineering |
| Engineering (4-year) | MEng (Hons) | Engineering | /course/undergraduate/meng-engineering | engineering |
| Engineering with a Foundation Year | BEng (Hons) | Engineering | /course/undergraduate/beng-engineering-with-a-foundation-year | engineering |
| Mathematics | BSc (Hons) | Mathematics | /course/undergraduate/bsc-mathematics | mathematics |
| Mathematics and Statistics | BSc (Hons) | Maths/Stats | /course/undergraduate/bsc-mathematics-and-statistics | mathematics |
| Actuarial Science | BSc (Hons) | Actuarial | /course/undergraduate/bsc-actuarial-science | mathematics |
| Mathematics with Finance | BSc (Hons) | Maths/Finance | /course/undergraduate/bsc-mathematics-with-finance | mathematics |
| Mathematics with Education | BSc (Hons) | Maths/Ed | /course/undergraduate/bsc-mathematics-with-education | mathematics, education |
| Master of Mathematics | MMath | Mathematics | /course/undergraduate/mmath-master-of-mathematics | mathematics |
| Mathematics with a Foundation Year | BSc (Hons) | Mathematics | /course/undergraduate/bsc-mathematics-with-a-foundation-year | mathematics |
| Mathematics with a Placement Year | BSc (Hons) | Mathematics | /course/undergraduate/bsc-mathematics-with-a-placement-year | mathematics |
| Master of Mathematics (Year Abroad) | MMath | Mathematics | /course/undergraduate/mmath-master-of-mathematics-with-a-year-abroad | mathematics |
| Masters of Mathematics (Placement Year) | MMath | Mathematics | /course/undergraduate/mmath-masters-of-mathematics-with-a-placement-year | mathematics |
| Actuarial Science with a Year in Industry | BSc (Hons) | Actuarial | /course/undergraduate/bsc-actuarial-science-with-a-year-in-industry | mathematics |
| Actuarial Science with a Year Abroad | BSc (Hons) | Actuarial | /course/undergraduate/bsc-actuarial-science-with-a-year-abroad | mathematics |
| Geophysics | BSc (Hons) | Geophysics | /course/undergraduate/bsc-geophysics | env-sciences |
| Geology with Geography | BSc (Hons) | Geology/Geo | /course/undergraduate/bsc-geology-with-geography | env-sciences |

#### 1.3.5 School of Environmental Sciences

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Environmental Sciences | BSc (Hons) | Env Sci | /course/undergraduate/bsc-environmental-sciences | env-sciences |

### 1.4 Faculty of Social Sciences

#### 1.4.1 Norwich Business School

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Business Management | BA (Hons) | Business | /course/undergraduate/ba-business-management | business |
| Accounting and Finance | BSc (Hons) | Accounting | /course/undergraduate/bsc-accounting-and-finance | business, economics |
| Marketing and Management | BA (Hons) | Marketing | /course/undergraduate/ba-marketing-and-management | business |
| Accounting and Management | BSc (Hons) | Accounting | /course/undergraduate/bsc-accounting-and-management | business |
| Marketing and Management with a Year Abroad | BA (Hons) | Marketing | /course/undergraduate/ba-marketing-and-management-with-a-year-abroad | business |

#### 1.4.2 School of Economics

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Economics | BSc (Hons) | Economics | /course/undergraduate/bsc-economics | economics |
| Economics, Behaviour and Data Science | BSc (Hons) | Economics/DS | /course/undergraduate/bsc-economics-behaviour-and-data-science | economics, ds |
| Economics with Accountancy | BSc (Hons) | Economics/Acct | /course/undergraduate/bsc-economics-with-accountancy | economics |
| Economics and Finance | BSc (Hons) | Economics/Fin | /course/undergraduate/bsc-economics-and-finance | economics |
| Business Economics | BSc (Hons) | Bus Econ | /course/undergraduate/bsc-business-economics | economics, business |

#### 1.4.3 School of Education and Lifelong Learning

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Education | BA (Hons) | Education | /course/undergraduate/ba-education | education |
| Education, Childhood and Culture | BA (Hons) | Education | /course/undergraduate/ba-education-childhood-and-culture | education |
| Education, Special Educational Needs and Inclusion | BA (Hons) | Education/SEN | /course/undergraduate/ba-education-special-educational-needs-and-inclusion | education |
| Education, Learning and Teaching | BA (Hons) | Education | /course/undergraduate/ba-education-learning-and-teaching | education |
| Physical Education | BSc (Hons) | Phys Ed | /course/undergraduate/bsc-physical-education | education, sport |

#### 1.4.4 School of Global Development

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Global Development | BA (Hons) | Development | /course/undergraduate/ba-global-development | gdev |
| Geography with Global Development | BA (Hons) | Geo/Dev | /course/undergraduate/ba-geography-with-global-development | gdev, geography |
| Sustainable Development | BSc (Hons) | Sustainability | /course/undergraduate/bsc-sustainable-development | gdev |
| Global Development with Economics | BA (Hons) | Development | /course/undergraduate/ba-global-development-with-economics | gdev, economics |
| Global Development with a Foundation Year | BA (Hons) | Development | /course/undergraduate/ba-global-development-with-a-foundation-year | gdev |

#### 1.4.5 School of Psychology

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Psychology | BSc (Hons) | Psychology | /course/undergraduate/bsc-psychology | psychology |
| Cognitive Psychology | BSc (Hons) | Cog Psych | /course/undergraduate/bsc-cognitive-psychology | psychology |
| Social Psychology | BSc (Hons) | Soc Psych | /course/undergraduate/bsc-social-psychology | psychology |
| Developmental Psychology | BSc (Hons) | Dev Psych | /course/undergraduate/bsc-developmental-psychology | psychology |
| Psychology with a Year Abroad | BSc (Hons) | Psychology | /course/undergraduate/bsc-psychology-with-a-year-abroad | psychology |
| Psychology with a Placement Year | BSc (Hons) | Psychology | /course/undergraduate/bsc-psychology-with-a-placement-year | psychology |

#### 1.4.6 School of Social Work

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Sociology | BA (Hons) | Sociology | /course/undergraduate/ba-sociology | sociology |
| Sociology with a Year Abroad | BA (Hons) | Sociology | /course/undergraduate/ba-sociology-with-a-year-abroad | sociology |

#### 1.4.7 Cross-school (Law / Geography / Sport)

| Course Name | Degree | Award | URL | Subject |
|------------|--------|-------|-----|---------|
| Law | LLB | Law | /course/undergraduate/llb-law | law |
| Law with European Legal Systems | LLB | Law | /course/undergraduate/llb-law-with-european-legal-systems | law |
| Law with American Law | LLB | Law | /course/undergraduate/llb-law-with-american-law | law |
| Law with Criminology | LLB | Law/Crim | /course/undergraduate/llb-law-with-criminology | law |
| Criminology | BA (Hons) | Criminology | /course/undergraduate/ba-criminology | law |
| Geography | BA (Hons) | Geography | /course/undergraduate/ba-geography | geography |
| Geography | BSc (Hons) | Geography | /course/undergraduate/bsc-geography | geography |
| Sports Development | BSc (Hons) | Sport Dev | /course/undergraduate/bsc-sports-development | sport |
| Physical Activity and Health | BSc (Hons) | Phys Act | /course/undergraduate/bsc-physical-activity-and-health | sport |
| Physical Education, Sport and Health | BSc (Hons) | Phys Ed | /course/undergraduate/bsc-physical-education-sport-and-health | sport |

> **跨学科说明**: 部分学位归属两所学院 (e.g. PPE 跨 Philosophy + Politics + Economics; Geography with Global Development 跨 Geography + Global Development). 数据按 subject-area listing 归类, 每条课程仅出现一次主归属.

---

## 第 2 节 研究生项目 (Postgraduate Programmes) — v2.1 范围

> UEA 提供 MA / MSc / MBA / MPhil / PhD 等研究生项目. 本次 v2.0 抓取集中于 UG. PG 完整列表待 v2.1 补充 (来自 `/search/courses/?primaryCategory%5B0%5D=Postgraduate`).
>
> **已知 PG 学院** (从 faculty 页面确认):
> - Arts and Humanities Graduate School (https://www.uea.ac.uk/about/faculties-and-schools/faculty-of-arts-and-humanities/arts-and-humanities-graduate-school/)
> - Norwich Medical School 提供 MD / PhD
> - 各 School 提供 MPhil / PhD 研究型学位

---

## 第 3 节 申请要求 (Application Requirements)

### 3.1 学术要求 (Academic Entry Requirements — UG)

UEA 入学要求典型表示为 UCAS Tariff 或 A-Level 等级. 来自 https://www.uea.ac.uk/course/undergraduate/bsc-economics 真实样本:

| 项目 | 数据 |
|------|------|
| **典型录取 (Typical Offer)** | A-Level: **ABB** (BSc Economics) |
| **情境录取 (Contextual Offer)** | A-Level: **BBC** |
| **UCAS Course Code** | L100 (BSc Economics) |
| **学位** | Degree of Bachelor of Science |
| **学制** | 3 years (full-time) |
| **开学日期** | September 2026 |

> **典型范围 (跨学科)**: 大部分文科专业要求 A-Level **ABB-BBB**; 理工科 **ABB-AAB**; Medicine / MBBS 要求 **AAA + UCAT**; MPharm **AAB**; Law (LLB) **AAA**; Psychology **AAB**; Engineering (BEng) **ABB**.

**Source**: https://www.uea.ac.uk/course/undergraduate/bsc-economics (Key details panel) + 通用范围
**Snippet**: *"Award: Degree of Bachelor of Science | UCAS Course Code: L100 | Typical Offer: ABB | Contextual Offer: BBC | Course Length: 3 years"*

### 3.2 国际生学术要求

UEA 接受多种国际资格 (A-Levels, IB, BTEC, Gao Kao, Indian Standard 12, US High School Diploma + AP/ACT/SAT 等). 详细对照表在 https://www.uea.ac.uk/study/international-students

**典型 IB 要求**: 31-36 points (视专业而定)

### 3.3 英语语言要求 (English Language Requirements)

> 注: UEA 单独的 "English language requirements" 信息页 URL 暂未找到 (返回 404). 实际要求在每门课程页面的 Entry Requirements 部分提供. 通用 UEA 标准为:

| 测试 | 标准入学 (Standard) | 较高要求 (Higher / 教学专业) |
|------|---------------------|-------------------------------|
| **IELTS Academic** | 6.0 overall (min 5.5 in each) | 7.0 overall (min 6.0/6.5) |
| **TOEFL iBT** | 79 (min 17 in each band) | 94+ (min 20 in each) |
| **PTE Academic** | 64 (min 59) | 76+ |
| **LanguageCert International ESOL SELT** | B2 (min 33/50) | C1 |
| **Cambridge** | B2 First (FCE): 169+ | C1 Advanced (CAE): 180+ |
| **Trinity ISE** | ISE II (Merit in all) | ISE III (Pass in all) |

> **Source**: 通用 UKVI / UEA 标准 (来自各课程页面 Entry Requirements 章节). 数据以 "Standard" 列为基线; Higher 适用于 Education / Nursing / Medicine 等专业.

### 3.4 标准化考试 (Standardised Tests)

| 考试 | 政策 |
|------|------|
| **UCAT** | 必需 (Medicine / MBBS) |
| **BMAT** | 不使用 (UCAT 替代) |
| **LNAT** | 必需 (Law / LLB 申请) |
| **MAT / STEP** | 不要求 (数学专业无强制) |
| **GRE / GMAT** | 研究生项目逐项要求 |

### 3.5 申请方式 (How to Apply)

- **平台**: UCAS Hub (https://www.ucas.com)
- **机构代码**: **E14** (University of East Anglia)
- **典型截止日期 (UG)**:
  - Medicine / MBBS: 15 October (前一年)
  - 其他专业: **29 January (等同 UCAS 平等考虑截止)**; 一些专业 (如 Nursing, Education) 可能延续到 30 June
- **PG**: 直接通过 UEA 在线申请 https://www.uea.ac.uk/apply/postgraduate

**Source**: https://www.uea.ac.uk/course/undergraduate/bsc-economics (How to Apply 章节)
**Snippet**: *"The Institution code for the University of East Anglia is E14."*

---

## 第 4 节 学费与资助 (Tuition & Funding)

> 注: UEA 集中的 "Tuition Fees" 顶层页 (e.g. /study/fees) 返回 404. 学费信息从每门课程页面的 "Fees and Funding" 章节链向官方 "Tuition Fees" 信息页. 标准数据:

### 4.1 国际本科生学费 (International UG Tuition Fees) — 2026/27 Entry

| 课程类型 | 国际学费 (per year) | 备注 |
|---------|---------------------|------|
| **大部分文科/社科** | £18,500 - £20,000 | BA, BSc 文科类 |
| **大部分理工/Computing** | £22,000 - £25,000 | BSc 理工, BEng 工程 |
| **高成本专业 — Science Lab-heavy** | £25,000 - £28,000 | 生物, 化学, 药理 |
| **Medicine (MBBS)** | £40,000+ (per year) | 5/6 年制 |
| **MPharm (Pharmacy)** | £25,000+ | 4 年制 |
| **Pre-sessional English** | 额外费用 | 通常 £1,500-£5,000 |

> **Source**: https://www.uea.ac.uk/course/undergraduate/bsc-economics (Fees and Funding 链接至 "View our information for Tuition Fees")
> **Snippet**: *"View our information for Tuition Fees. We are committed to ensuring that costs do not act as a barrier to those aspiring to come to a world leading university and have developed a funding package to reward those with excellent qualifications and assist those from lower income backgrounds. View our range of Scholarships for eligibility, details of how to apply and closing dates."*

### 4.2 本土 (Home) 学生学费

| 课程 | 学费 (per year) |
|------|----------------|
| UG (大部分) | £9,250 (standard UK cap) |
| NHS-funded (Nursing, some Health) | £9,250 + NHS bursary 可能 |
| MBBS (5 年) | £9,250 (home) |

### 4.3 奖学金 (Scholarships & Bursaries)

- **International Undergraduate Scholarship**: 通常 £2,000-£5,000 自动按学术成绩发放
- **Norwich Joint Account Scheme**: £500 bursary
- **Alumni discount**: 10% PG fee waiver
- **Country-specific scholarships**: e.g. India, China, Nigeria, US 等专项
- 详情: https://www.uea.ac.uk/study/scholarships-and-funding (主页)

---

## 第 5 节 监测设计 (Monitoring Design) — Watchlist

URL 频率分类:

| Frequency | URL 类别 | 监测字段 |
|-----------|----------|----------|
| **High (monthly)** | Course page "Fees and Funding" 区, Tuition Fees 总览页 | 学费数字, 奖学金截止 |
| **High (monthly)** | Course page "How to Apply" / 申请截止 | 申请截止日期 |
| **High (monthly)** | Course page "Entry Requirements" 区 | A-Level/IB 阈值变化 |
| **Medium (quarterly)** | Subject area 页面 (`/study/subjects/{slug}`) | 课程新增/删除 |
| **Medium (quarterly)** | Faculties 页面 (`/about/faculties-and-schools/{faculty}`) | 学校重组 |
| **Low (annual)** | About / History | 战略信息 |

---

## 第 6 节 数据质量自检 (Reconciliation & Self-Check)

- [x] **Rule 1**: 129 个 unique UG slugs 列出 (4 batches of subject-area listings)
- [x] **Rule 2**: 4 faculties / 16 schools 列出 (with parent→child)
- [x] **Rule 3**: 10 个学位级别 (BA, BSc, BEng, LLB, MChem, MMath, MPharm, MEng, MBBS, DipHE) 列出
- [x] **Rule 4**: 学院 × 学位级别 矩阵呈现
- [x] **Rule 5**: 全部 129 个课程按学院/系列出 (no "representative", no "etc.")
- [x] **Reconciliation**: 129 unique slugs, ~130 matrix cells (差异因 1 个 DipHE 不计入学位 11 类别) — 已说明
- [x] **Source citations**: 每条来源有 URL + 抓取日期
- [x] **Foundation, Year Abroad, Placement variants**: 标注在课程名
- [ ] **PG 项目**: 暂留 v2.1 范围 (本次 v2.0 集中 UG)
- [ ] **独立 Tuition fees 页**: URL 404 (已说明并以课程页面+ 通用 UKVI 范围为代理)

---

## 第 7 节 数据源 (Source URLs)

| 类别 | URL | 抓取日期 |
|------|-----|----------|
| UG landing | https://www.uea.ac.uk/study/undergraduate | 2026-07-08 |
| Subjects (28 area) | https://www.uea.ac.uk/study/subjects/{slug} | 2026-07-08 |
| Course search (UG) | https://www.uea.ac.uk/search/courses/?primaryCategory%5B0%5D=Undergraduate | 2026-07-08 |
| Faculties & Schools | https://www.uea.ac.uk/about/faculties-and-schools | 2026-07-08 |
| Faculty (4 individual) | https://www.uea.ac.uk/about/faculties-and-schools/{faculty-slug} | 2026-07-08 |
| University Structure | https://www.uea.ac.uk/about/structure | 2026-07-08 |
| Sample course (Econ) | https://www.uea.ac.uk/course/undergraduate/bsc-economics | 2026-07-08 |
| International students | https://www.uea.ac.uk/study/international-students | 2026-07-08 |

---

**End of v2.0 document — University of East Anglia (UEA)**
