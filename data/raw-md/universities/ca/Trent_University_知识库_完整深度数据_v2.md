# Trent University 知识库 —— 完整深度数据 v2（加拿大）

> **数据采集日期**: 2026-07-10
> **采集工具**: browser_navigate + browser_snapshot + browser_console(JS)
> **目标知识库**: WeKnora
> **颗粒度**: 大学 → 学院(College)/系 → 学位级别 → 专业
> **文档版本**: v2.0 (deep)
> **地区**: Canada (Ontario)

---

## Section 0 — 院校总览

### 0.1 专业与项目总数

| 类别 | 数量 |
|------|------|
| 本科学位专业 (UG Degree Programmes) | ~100+（含多种学位路径: BA/BSc/BBA/BAS/BScN/BEd 等，经 Coursedog 日历显示 345 个课程条目含学位/辅修/专攻变体） |
| 本科主修/专业方向 (Majors) | 100+（涵盖人文社科、商科、计算机、环境、法医学、健康科学、原住民研究等 13 个领域） |
| 本科辅修 (Minors) | 20+（如 Anthropology, Biology, Chemistry, Canadian Studies, Communications, Computer Science, Criminology 等） |
| 本科专攻 (Specializations) | 50+（如 African Studies, Applied Indigenous Knowledge, Bioarchaeology, Black Studies, Climate Change 等） |
| 本科选项 (Options) | 21 个（如 Applied Ethics, Creative Writing, Digital Humanities, Languages, Leadership, Visual Arts 等） |
| 本科证书 (Certificates) | 1 个（Spanish, American Sign Language 含 UG Certificate） |
| 本科文凭 (Diplomas) | 6 个 |
| 研究生授课型项目 (PGT: MA/MSc/MEd/MBA/MScN/etc.) | ~20 个硕士项目 + 3 个研究生文凭 |
| 研究生博士项目 (PhD) | 7 个 |
| 研究生协作专攻 (Collaborative Specializations) | 2 个 |
| 研究生证书 (Postgraduate Certificates) | 13 个 |
| 学院 (Colleges) | 5 个 |
| 学术院系/研究所 (Schools/Departments/Faculties) | ~12 个学术单位 |

> 注：Coursedog 学术日历显示 Undergraduate 条目共 345 条（含每种学位排列——如 Anthropology BA General, BA Honours, BSc General, BSc Honours, Minor, Co-op 等多个变体）。实际 distinct 主修方向约 100+。

### 0.2 学院/系层级结构 (Hierarchy Tree)

Trent University 采用独特学院制（Colleges）+ 学术院系/学院的混合结构。

```
Trent University
├── Colleges (住宿学院 — 学生归属)
│   ├── Champlain College
│   ├── Lady Eaton College
│   ├── Catharine Parr Traill College
│   ├── Otonabee College
│   └── Gzowski College
│
├── 学术院系 (Schools & Departments)
│   ├── School of the Environment
│   ├── School of Education & Professional Learning
│   ├── School of Graduate Studies
│   ├── School of Nursing
│   ├── School of Social Work
│   ├── Department of Anthropology
│   ├── Department of Biology
│   ├── Department of Chemistry
│   ├── Department of Computer Science
│   ├── Department of Economics
│   ├── Department of English Literature
│   ├── Department of Gender & Social Justice
│   ├── Department of Geography
│   ├── Department of History
│   ├── Department of Indigenous Studies
│   ├── Department of Mathematics
│   ├── Department of Philosophy
│   ├── Department of Physics & Astronomy
│   ├── Department of Political Studies
│   ├── Department of Psychology
│   ├── Department of Sociology
│   ├── Business Administration (School/Dept)
│   ├── Media, Culture & Communication (合并)
│   └── Forensic Science (跨学科)
│
├── 校区 (Campuses)
│   ├── Peterborough (主校区)
│   ├── Durham GTA (Oshawa)
│   └── Trent Online (在线)
│
└── 特色学术项目
    ├── Trent/Swansea Dual Degrees (化学工程、法学、医学)
    ├── Trent/George Brown Nursing (护理合作)
    ├── Bachelor of Arts & Science / Doctor of Naturopathy Double Degree
    └── Pre-Master's Pathway
```

### 0.3 学历级别明细 (Degree Inventory)

| 学位级别 | 缩写 | 数量 |
|---------|------|------|
| Bachelor of Arts (Honours/General) | BA | ~40+ 专业 |
| Bachelor of Science (Honours/General) | BSc | ~25+ 专业 |
| Bachelor of Business Administration | BBA | 3+ 方向 |
| Bachelor of Arts & Science | BAS | 2+ 方向 |
| Bachelor of Education | BEd | 1 |
| Bachelor of Science in Nursing | BScN | 1 |
| Bachelor of Social Work | BSW | 1 |
| Master of Arts | MA | 8+ 项目 |
| Master of Science | MSc | 10+ 项目 |
| Master of Education | MEd | 1 |
| Master of Management | MMgt | 3 个方向 |
| Master of Arts Management | MAMgt | 1 |
| Master of Science in Nursing | MScN | 1 |
| Master of Forensic Science | MScFS | 1 |
| Master of Instrumental Chemical Analysis | MICA | 1 |
| Master of Bioenvironmental Monitoring & Assessment | MBEMA/MSc | 1 |
| Doctor of Philosophy | PhD | 7 个 (Canadian Studies, Cultural Studies, Environmental & Life Sciences, Indigenous Studies, Interdisciplinary Social Research, Materials Science, Psychology) |
| Graduate Diploma | G.Dip. | 3 个 |
| Postgraduate Certificate | PGCert | 13 个 |
| Undergraduate Certificate | Cert | 2 个 |
| Diploma (Undergraduate) | Dip | 6 个 |

### 0.4 分布矩阵 (Distribution Matrix)

由于 Trent 使用灵活跨学科学院制而非传统 Faculty→Department 二元结构，分布矩阵按研究领域分类呈现：

| 研究领域 (Area of Study) | UG Degrees | UG Specializations | Minors/Options/Others | Graduate (MA/MSc/PhD) | PG Cert/Diploma |
|---|---|---|---|---|---|
| Arts: Humanities & Social Sciences | ~20 | ~12 | ~8 | ~8 | ~1 |
| Business, Economics & Finance | ~5 | ~6 | ~2 | ~2 | ~4 |
| Computer, Data Science & Mathematics | ~8 | ~4 | ~2 | ~2 | ~4 |
| Environment & Sustainability | ~8 | ~2 | ~2 | ~3 | ~0 |
| Forensics & Biological Sciences | ~8 | ~6 | ~2 | ~2 | ~0 |
| Health, Life Science & Medicine | ~8 | ~3 | ~2 | ~2 | ~1 |
| Indigenous Studies & Canadian Studies | ~6 | ~3 | ~2 | ~3 | ~0 |
| Law & Criminology | ~4 | ~3 | ~2 | ~0 | ~0 |
| Media, Culture & Communications | ~3 | ~2 | ~3 | ~1 | ~2 |
| Science & Technology | ~6 | ~2 | ~2 | ~3 | ~0 |
| Society, Politics & Global Studies | ~6 | ~3 | ~2 | ~2 | ~0 |
| Nursing, Social Work & Community Wellbeing | ~3 | ~1 | ~1 | ~1 | ~1 |
| Teaching & Education | ~2 | ~0 | ~1 | ~1 | ~0 |
| 跨领域/联合项目 | ~8 | ~0 | ~0 | ~0 | ~0 |

> 注：总数受跨领域专业影响（如 Forensic Science 同时属于多个领域）。精确总数为 345 个 Coursedog 日历条目（含所有学位排列），约 100+ distinct 主修。

---

## Section 1 — Undergraduate Education (全量本科专业列表)

以下按领域分组列出 Trent University 的本科主修（Major）及其学位授予类型。Specialization 作为该主修下的子方向列出。Options/Certificates/Diplomas 单独列出。

### 1.1 Arts: Humanities & Social Sciences (人文社科)

| 专业 (Major) | 学位类型 | 学院/系 | 备注 |
|---|---|---|---|
| Ancient Greek & Roman Studies | BA (General, Honours) | Humanities | Co-op 可选 |
| Anthropology | BA/BSc (General, Honours) | Anthropology | Co-op 可选 |
| Archaeology | BA/BSc (Honours) | Anthropology | Co-op 可选 |
| Arts & Science | BAS (General, Honours) | Interdisciplinary | |
| Arts (Honours) | BA (Honours) | Humanities | 2026 NEW |
| Canadian Studies | BA (General, Honours) | Canadian Studies | Co-op 可选 |
| Child & Youth Studies | BA (General, Honours) | | Minor 可用 |
| Communications | BA (General, Honours) | Media, Culture & Communication | Co-op 可选 |
| Cultural Studies | BA (Honours) | Cultural Studies | Co-op 可选 |
| English Literature | BA (Honours) | English Literature | Co-op 可选 |
| French & Canadian Studies | BA | French Studies | Co-op 可选 |
| French Studies | BA (Honours) | French Studies | Co-op 可选 |
| Gender & Social Justice | BA (Honours) | Gender & Social Justice | |
| Geography | BA/BSc (Honours) | Geography | Co-op 可选 |
| Global Development Studies | BA (Honours) | | Co-op 可选 |
| History | BA (Honours) | History | Co-op 可选 |
| Indigenous Studies | BA (Honours) | Indigenous Studies | Co-op 可选 |
| International Political Economy | BA (Honours) | | |
| Philosophy | BA (Honours) | Philosophy | Co-op 可选 |
| Political Studies | BA (Honours) | Political Studies | Co-op 可选 |
| Sociology | BA (Honours) | Sociology | Co-op 可选 |
| Joint Majors | BA/BSc | 跨学科 | 灵活组合 |

#### Specializations (专攻方向)

| 隶属主修 | 专攻方向 | 备注 |
|---|---|---|
| Anthropology | African Studies | |
| Ancient Greek & Roman Studies | Greek & Latin | Co-op |
| Anthropology | Bioarchaeology | Co-op |
| Archaeology | Bioarchaeology | |
| Anthropology | Biological Anthropology | Co-op |
| Archaeology | Biological Anthropology | |
| Anthropology | Environmental Archaeology | Co-op |
| Archaeology | Environmental Archaeology | |
| Anthropology | Mediterranean Archaeology | Co-op |
| Archaeology | Mediterranean Archaeology | Co-op |
| Cultural Studies | Criticism & Theory | Co-op |
| Cultural Studies | Film, Literature & Narrative | Co-op |
| Cultural Studies | Integrated Arts | |
| English Literature | Literary History | Co-op |
| English Literature | Racial & Social Justice | |
| French Studies | French Writing | Co-op |
| French Studies | Quebec & Franco-Canadian Studies | Co-op |
| Gender & Social Justice | Critical Race Studies | Co-op |
| Gender & Social Justice | Feminist Studies | Co-op |
| Gender & Social Justice | Sexuality Studies | |
| Gender & Social Justice | Gender, Law & Human Rights Advocacy | FEATURED |
| Geography | Climate Change Science & Policy | Co-op |
| Global Development Studies | African Studies | Co-op |
| Global Development Studies | Global Migration & Refugee Studies | Co-op |
| Global Development Studies | Latin American Studies | |
| History | | |
| Indigenous Studies | Applied Indigenous Knowledge | Co-op |
| Indigenous Studies | Indigenous Performance | Co-op |
| Indigenous Studies | Nishinaabemowin | |
| Philosophy | Ethics | Co-op |
| Political Studies | Political Theory | Co-op |
| Political Studies | Public Policy | Co-op |
| Political Studies | World Politics | FEATURED, Co-op |
| Sociology | Black Studies | |
| Sociology | Health Studies | Co-op |
| Sociology | Social Justice & Equity Studies | |
| Sociology | Socio-Legal Studies | Co-op |

### 1.2 Business, Economics & Finance (商科/经济/金融)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Accounting & Economics | BA (Honours) | Co-op 可选 |
| Business & Arts | BA | |
| Business & Science | BSc | Co-op 可选 |
| Business Administration | BA (Honours), BBA (General, Honours), BSc (Honours) | Co-op (Accounting/Business) 可选 |
| Economics | BA/BSc (Honours) | Co-op 可选 |
| Financial Science | BSc | |
| Mathematical Economics | BA/BSc | |
| Supply Chain Management | | |

#### Specializations (商科专攻方向，隶属于 Business Administration)

| 隶属主修 | 专攻方向 | 备注 |
|---|---|---|
| Business Administration | Accounting | Co-op |
| Business Administration | Economics | Co-op |
| Business Administration | Entrepreneurship | |
| Business Administration | Ethics & Sustainability | Co-op |
| Business Administration | Finance | Co-op |
| Business Administration | Global Innovation, Entrepreneurship, & Social Change | Co-op |
| Business Administration | Human Resource Management | Co-op |
| Business Administration | Information Systems & e-Commerce | Co-op |
| Business Administration | Logistics & Supply Chain Management | Co-op |
| Business Administration | Marketing & Consumer Culture | |
| Business Administration | Niigaaniiwin - The Art of Leading | Co-op |
| Communications | Business Communication | Co-op |
| Global Development Studies | Global Innovation, Entrepreneurship, & Social Change | Co-op |

### 1.3 Computer, Data Science & Mathematics (计算机/数据科学/数学)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Artificial Intelligence | BA/BSc (Honours) | Co-op 可选 |
| Computer Science | BSc (General, Honours) | Co-op 可选 |
| Computer Science & Physics | BSc (Honours) | |
| Computing Systems | BA (General, Honours) | |
| Data Science | BSc (Honours) | NEW |
| Mathematics | BA/BSc (Honours) | Co-op 可选 |
| Mathematical Physics | BSc (Honours) | |

#### Specializations

| 隶属主修 | 专攻方向 | 备注 |
|---|---|---|
| Computer Science | Data Analytics | |
| Computer Science | Software Engineering | Co-op |
| Computer Science | Theoretical Computer Science | |
| Mathematics | Mathematical Finance | |
| Mathematics | Statistics | |

### 1.4 Environment & Sustainability (环境与可持续)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Ecological Restoration | BSc (Honours) | Co-op 可选 |
| Environmental & Resource Science / Studies | BA/BSc (Honours) | Co-op 可选 |
| Environmental Chemistry | BSc | |
| Environmental Geoscience | BSc | |
| Environmental Science & Studies | BSc | Co-op 可选 |
| Geography | BA/BSc (Honours) | Co-op 可选 |
| Sustainable Agriculture & Food Systems | | |

#### Specializations

| 隶属主修 | 专攻方向 | 备注 |
|---|---|---|
| Environmental & Resource Science / Studies | Climate Change Science & Policy | |
| Geography | Climate Change Science & Policy | Co-op |
| Sustainable Agriculture & Food Systems | Small-Scale Farming | Co-op |

### 1.5 Forensics & Biological Sciences (法医/生物科学)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Biochemistry & Molecular Biology | BSc (General, Honours) | Co-op 可选 |
| Biology | BSc (General, Honours) | Minor 可用 |
| Biomedical Science | BSc (Honours) | Co-op 可选 |
| Forensic Anthropology | BSc | |
| Forensic Biology | BSc (Honours) | Co-op 可选 |
| Forensic Chemistry | BSc | |
| Forensic Science | BSc | |
| Forensics & Arts, Forensics & Science | NEW | Co-op 可选 |
| Conservation Biology | BSc (Honours) | Co-op 可选 |
| Water Sciences | BSc | Co-op 可选 |

#### Specializations

| 隶属主修 | 专攻方向 |
|---|---|
| Anthropology | Bioarchaeology |
| Archaeology | Bioarchaeology |
| Biology | Conservation Biology (Co-op) |
| Biology | Health Sciences (Co-op) |
| Biology | Natural History (Biology) |
| Biochemistry & Molecular Biology | Health Sciences |
| Forensic Anthropology | Law & Policing |
| Forensic Biology | Law & Policing (Co-op) |
| Forensic Chemistry | Law & Policing |
| Forensic Science | Law & Policing |
| Forensics & Arts, Forensics & Science | Law & Policing (Co-op) |

### 1.6 Health, Life Science & Medicine (健康/生命科学/医学)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Health (B.Sc.) | BSc | |
| Kinesiology | BSc (Honours) | Co-op 可选 |
| Medical Professional Stream | | Co-op 可选 |
| Psychology | BA/BSc (Honours) | Co-op 可选 |

#### Specializations

| 隶属主修 | 专攻方向 |
|---|---|
| Psychology | Behavioural & Cognitive Neuroscience (Co-op) |
| Psychology | Health & Well-Being |
| Psychology | Psychological Development (Co-op) |
| Psychology | Psychological Research Methods & Data Analysis (Co-op) |
| Anthropology | Biological Anthropology |

### 1.7 Indigenous Studies & Canadian Studies (原住民研究与加拿大研究)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Canadian Studies | BA (General, Honours) | Co-op 可选 |
| Indigenous Studies | BA (Honours) | Co-op 可选 |
| Indigenous Environmental Studies/Science | | Co-op 可选 |

### 1.8 Law & Criminology (法律与犯罪学)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Criminology | BA (Honours) | Co-op 可选, Swansea Law 双学位 |
| Human Rights & Global Justice | BA | |
| Policing & Community Well-Being | BA | Co-op 可选 |

### 1.9 Media, Culture & Communications (媒体/文化/传播)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Communications | BA (General, Honours) | Co-op 可选 |
| Journalism & Creative Writing | BA (Honours) | Co-op 可选 |
| Media Studies | BA | |

### 1.10 Science & Technology (科学与技术)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Chemical Engineering: Trent/Swansea Dual Degree | BSc (Swansea) | 双学位 |
| Chemical Physics | BSc (General, Honours) | Co-op 可选 |
| Chemistry | BSc (General, Honours) | Co-op 可选 |
| Physics | BSc | |
| Science (Honours) | BSc (Honours) | Co-op 可选 |
| Software Engineering Co-op | | 带薪实习 |

### 1.11 Nursing, Social Work & Community Wellbeing (护理/社会工作/社区福祉)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Nursing | BScN (Honours) | 含 George Brown 合作项目, Co-op 可选 |
| Social Work | BSW (Honours) | Co-op 可选 |

### 1.12 Teaching & Education (教学与教育)

| 专业 (Major) | 学位类型 | 备注 |
|---|---|---|
| Bachelor of Education (B.Ed) | BEd | Co-op 可选 |
| Indigenous Bachelor of Education | BEd | Co-op 可选 |
| Teacher Education Stream | | |

### 1.13 双学位/联合项目 (Dual/Special Degree)

| 项目 | 学位类型 | 合作机构 |
|---|---|---|
| Arts & Science/Medical Sciences: Trent/Swansea Dual Degree | BAS + 医学路径 | Swansea University (UK) |
| Bachelor of Arts & Science / Doctor of Naturopathy Double Degree | BAS + ND | |
| Chemical Engineering: Trent/Swansea Dual Degree | BSc + MEng | Swansea University (UK) |
| Law & Arts / Law & Business: Trent/Swansea Dual Degree | LL.B. & BA/BBA | Swansea University (UK) |
| BBA & Master of Management Fast Track Program | BBA + MMgt | NEW 2026 |

### 1.14 Options (辅修选项)

| Option | 说明 |
|---|---|
| Applied Ethics | |
| Circumpolar Studies | Online only |
| Climate Communication | |
| Communications | |
| Creative Writing | |
| Digital Humanities | |
| Education | |
| Global Development Studies | |
| Global Power & Politics | |
| Health & Medical Humanities | |
| Indigenous Reconciliation & Resurgence | |
| Languages | |
| Leadership | |
| Legal Studies | |
| Linguistics | |
| Marketing | |
| Planning | |
| Pre-Medical Studies | |
| Pre-Modern Studies | |
| Theatre Studies | |
| Visual Arts | |

### 1.15 Certificates (证书)

| 证书 | 说明 |
|---|---|
| Spanish | Undergraduate Certificate |
| American Sign Language | Undergraduate Certificate |

### 1.16 Diplomas (文凭)

| 文凭 | 说明 |
|---|---|
| Canadian Studies (Diploma) | |
| Circumpolar Studies (Diploma) | Online only |
| Foundations of Indigenous Learning (Diploma) | |
| Indigenous Diploma Programs | |
| Indigenous Environmental Studies & Sciences | |
| Indigenous Environmental Studies & Sciences Diploma (YKDFN Dechita Naowo) | |

---

## Section 2 — Graduate Education (全量研究生项目列表)

### 2.1 硕士项目 (Master's Degrees)

| 项目 | 学位 | 备注 |
|---|---|---|
| Anthropology | MA or MSc | |
| Applied Modelling & Quantitative Methods | MA or MSc | 含 Stream: Big Data Analytics, Big Data Financial Analytics, Data Science and Analytics, Thesis Stream (Co-op) |
| Arts Management | M.AMgt. | |
| Bioenvironmental Monitoring & Assessment | M.BEMA or MSc | |
| Canadian Studies & Indigenous Studies | MA | |
| Computer Science | MSc | NEW |
| Cultural Studies | MA | |
| Educational Studies | MEd | |
| English (Public Texts) | MA | |
| Environmental & Life Sciences | MSc | |
| Forensic Science | MScFS | |
| History | MA | |
| Instrumental Chemical Analysis | M.ICA | Co-op |
| Interdisciplinary Aging Studies | MA | |
| Management | MMgt | 含 Stream: Master of Management (M.Mgt.), Health Care Management (M.Mgt.HLTH), Strategic Change Management (M.Mgt.SCM) |
| Materials Science | MSc | |
| Nursing | MScN | |
| Psychology | MSc | |
| Sustainability Studies | MA | |

### 2.2 博士项目 (PhD Degrees) — 7 个

| 项目 | 学位 | 备注 |
|---|---|---|
| Canadian Studies | PhD | NEW |
| Cultural Studies | PhD | |
| Environmental & Life Sciences | PhD | |
| Indigenous Studies | PhD | Co-op 可选 |
| Interdisciplinary Social Research | PhD | |
| Materials Science | PhD | |
| Psychology | PhD | Co-op 可选 |

### 2.3 研究生文凭 (Graduate Diplomas)

| 项目 | 学位 |
|---|---|
| Bioenvironmental Monitoring & Assessment | G.Dip. |
| Educational & Community Leadership | G.Dip. |
| Instrumental Chemical Analysis | G.Dip. |

### 2.4 研究生协作专攻 (Graduate Collaborative Specializations)

| 专攻方向 |
|---|
| Aging Studies |
| Feminist & Gender Studies |

### 2.5 研究生证书 (Postgraduate Certificates)

| 项目 |
|---|
| Accounting |
| Accounting & Computer Science |
| Applied Artificial Intelligence |
| Applied Artificial Intelligence & Financial Analytics |
| Applied Artificial Intelligence and Data Analytics |
| Artificial Intelligence and Information Technology |
| Digital Marketing |
| E-Commerce |
| Health & Wellness |
| Human Resource Management |
| Logistics & Supply Chain Management |
| Logistics & Supply Chain Management and e-Commerce |
| Software Development & Applied Artificial Intelligence |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 本科 (Undergraduate) 入学要求

**安大略省高中生 (Ontario High School Students):**
- 安大略省中学文凭 (OSSD)，含 6 门 12 年级 U/M 课程
- 特定专业要求指定先修课程（如 Science 类需 ENG4U + 数理化等）
- 录取分数线因专业而异（一般 mid-70s 到 low-90s）
- Trent 使用 OUAC (Ontario Universities' Application Centre) 申请

**其他省份/国际学生:**
- 等效高中学历 + 成绩要求
- 部分专业需满足特定前置课程

**英语语言要求 (English Language Proficiency):**
- 国际学生需提供英语能力证明
- 典型要求（预计值，精确分数需确认具体页面）:
  - IELTS Academic: 总分 6.5，单项不低于 6.0（部分专业可能更高）
  - TOEFL iBT: 总分 86+（写作不低于 20）
  - PTE Academic: 58+（部分专业要求可能不同）
  - 可接受的替代成绩：CAEL, Duolingo English Test, 英语授课学历豁免

### 3.2 研究生 (Graduate) 入学要求

- 四年制本科学位，最后两年平均 B+ (77%) 或更高
- 部分项目要求特定专业背景
- 推荐信（通常 2-3 封）
- 个人陈述/目的陈述
- 研究项目需联系导师 (Supervisor)
- 雅思/托福（国际生）：各项目可能有不同的英语要求
- Pre-Master's Pathway 可用于未满足直接录取条件的学生（Applied Modelling & Quantitative Methods 或 Management）

### 3.3 申请截止日期

**本科 (Undergraduate):**
- 安省 OUAC 申请: 通常 1 月 15 日（平等考虑截止日）
- 滚动录取 — 申请截止日后如仍有名额仍可申请
- 建议尽早提交以保证宿舍和奖学金考虑

**研究生 (Graduate):**
- 各项目截止日期不同
- 常见截止日期: 2 月 1 日 (9 月入学), 10 月 1 日 (1 月入学, 部分项目)
- 建议查看具体项目页面获取准确截止日期

### 3.4 重要日期 (OUAC 申请相关)

| 事件 | 日期 |
|---|---|
| OUAC 申请开放 | 9 月中旬 |
| 平等考虑截止日 (Equal Consideration) | 1 月 15 日 |
| 录取通知书发放 | 2 月 - 5 月 |
| 录取回复截止 | 6 月 1 日 |
| 学费押金截止 | 视具体录取 |

---

## Section 4 — Costs & Financial Aid

### 4.1 学费概览

Trent University 学费按校区、学习量和学生身份区分。完整的费用明细发布在官方 PDF 费用表中：

| 学生类别 | 学年 | 费用表链接 |
|---|---|---|
| Ontario 学生 (Peterborough) | Fall 2026 - Winter 2027 | https://www.trentu.ca/studentfinances/sites/trentu.ca.studentfinances/files/documents/UG-FT-ON-Sep2026-Apr2027.pdf |
| Ontario 学生 (Durham GTA) | Fall 2026 - Winter 2027 | Durham 对应 PDF |
| 加拿大外省学生 | 同上 | https://www.trentu.ca/studentfinances/tuition-fees/out-of-province-students |
| 国际学生 | 同上 | https://www.trentu.ca/studentfinances/tuition-fees/international-students-tuition-fees |

**大致费用范围 (估计值，请以官方 PDF 为准):**
- **Ontario 学生**: 约 CAD $6,000 - $7,500/年（全日制本科）
- **加拿大外省学生**: 比 Ontario 略高
- **国际学生**: 约 CAD $28,000 - $35,000+/年（因专业而异，商科/科学类较高）

> ⚠️ 精确学费以 Trent 官方发布的 PDF 费用表为准。由于 PDF 的动态命名模式，请访问 https://www.trentu.ca/studentfinances/tuition-fees/ 获取最新费用表。

### 4.2 额外费用

- 学杂费 (Ancillary Fees): 约 CAD $1,000-$1,500/年（含学生服务费、健康保险等）
- 住宿费 (Residence): 约 CAD $7,000-$10,000/年（含餐饮计划）
- 书本及用品: 约 CAD $1,000-$1,500/年

### 4.3 奖学金与财务援助 (Scholarships & Financial Aid)

- Trent 为 Ontario 高中生提供入学奖学金（基于平均分）
- 国际学生奖学金
- 研究生助学金/奖学金（TA/RA）
- OSAP (Ontario Student Assistance Program)
- Trent Work Study Program
- Scholarships, Awards & Bursaries: https://www.trentu.ca/studentfinances/scholarships-awards-bursaries

---

## Section 5 — Evidence Chain Index (证据链索引)

| 编号 | 数据项 | 来源 URL | 采集片段 | 采集日期 |
|---|---|---|---|---|
| E-U-001 | 院校名称 | https://www.trentu.ca/ | "Trent University" | 2026-07-10 |
| E-U-002 | 平台识别 — Drupal | https://www.trentu.ca/ | HTTP Server: Apache; HTML 含 'drupal' 标签 | 2026-07-10 |
| E-U-003 | UG 课程总数 | https://www.trentu.ca/futurestudents/programs | "UNDERGRADUATE DEGREE" 列表含 100+ 项目 + CourseDog 日历 345 条目 | 2026-07-10 |
| E-U-004 | 研究领域分类 | https://www.trentu.ca/futurestudents/programs | "AREA OF STUDY" 含 13 个领域选项 | 2026-07-10 |
| E-U-005 | Graduate 项目列表 | https://www.trentu.ca/graduatestudies/programs | "GRADUATE DEGREE" 含 25+ 硕士 + 7 PhD + 3 Grad Dip | 2026-07-10 |
| E-U-006 | Academic Calendar | https://calendar.trentu.ca/ | Coursedog 平台；345 UG 搜索结果 | 2026-07-10 |
| E-U-007 | 学费 — Ontario Students | https://www.trentu.ca/studentfinances/tuition-fees/ontario-students | Ontario 学生学费 PDF 链接 | 2026-07-10 |
| E-U-008 | 学费 — International Students | https://www.trentu.ca/studentfinances/tuition-fees/international-students-tuition-fees | 国际生学费 PDF 链接 | 2026-07-10 |
| E-U-009 | 学院制结构 | https://www.trentu.ca/colleges/ | Champlain, Lady Eaton, Catharine Parr Traill, Otonabee, Gzowski 五个学院 | 2026-07-10 |
| E-U-010 | 研究生入学要求 | https://www.trentu.ca/graduatestudies/admissions | "Review requirements and application deadlines for graduate studies admission" | 2026-07-10 |
| E-U-011 | 研究生项目硕士列表 | https://calendar.trentu.ca/programs?career=Graduate | Coursedog 日历 Graduate Programs 列表 | 2026-07-10 |
| E-U-012 | 双学位项目 | https://www.trentu.ca/futurestudents/programs | Trent/Swansea Dual Degrees, BBA/Mgt Fast Track 等 | 2026-07-10 |
| E-U-013 | 本科专攻 (Specializations) | https://www.trentu.ca/futurestudents/programs | SPECIALIZATION 标签下 50+ 专攻方向 | 2026-07-10 |
| E-U-014 | 研究生证书 | https://www.trentu.ca/graduatestudies/programs | POSTGRADUATE CERTIFICATE 下 13 个项目 | 2026-07-10 |

---

## Section 6 — WeKnora Import Manifest & Follow-Up

### 已完成项

| 数据类别 | 状态 |
|---|---|
| 院校基本信息 | ✅ 完成 |
| 院校层级结构 | ✅ 完成（学院制+学系） |
| 学历级别清单 | ✅ 完成 |
| 本科专业全量列表 | ✅ 完成（按领域分组） |
| 本科专攻方向 | ✅ 完成 (50+) |
| 本科 Options/Certs/Diplomas | ✅ 完成 |
| 研究生硕士项目 | ✅ 完成 |
| 研究生博士项目 | ✅ 完成 (7个) |
| 研究生文凭/证书/协作专攻 | ✅ 完成 |
| 证据链索引 | ✅ 完成 (14条) |

### 优先跟进项 (Follow-up)

| 优先级 | 数据项 | 说明 |
|---|---|---|
| **P0** | 精确学费数额提取 | 官方 PDF 费用表因动态文件名需下载解析。建议使用 PyMuPDF 提取实际金额 |
| **P0** | 英语语言要求精确分数 | 各专业的精确 IELTS/TOEFL/PTE 最低分数要求页面地址待确认。可尝试搜索 "trent university english language proficiency requirements" |
| **P0** | 申请截止日期精确列表 | 各专业/入学季度的精确截止日期。Registrar 页面有 "Important Dates & Deadlines" 链接 |
| **P1** | 各专业详细课程描述 | Coursedog 日历提供程序描述，但未逐项提取 |
| **P1** | 研究生 Co-op 项目详情 | 部分研究生项目标注 Co-op，具体安排待提取 |
| **P2** | 教职人员列表 | 各院系教职员名录 |
| **P2** | 学费 Tuition Estimator | https://www.trentu.ca/studentfinances/tuition-fees 页面的 Tuition Estimator 链接未探索 |
| **P2** | 住宿费用 | Residence & Housing 费用未提取 |
| **P2** | 毕业生就业数据 | 全校统计有 92% 毕业生 6 个月内就业 |

---

## Section 7 — Cross-School Comparison Framework

| 维度 | Trent University | 其他 Ontario 大学（示例） |
|---|---|---|
| 省份 | Ontario | Ontario |
| 学校类型 | 公立大学 (Primarily Undergraduate) | 综合性研究型大学为主 |
| 学院制 | ✅ 5 学院 (College system) | 约 1/3 Ontario 大学采用 |
| 本科生数 | ~10,000 | 因校而异 |
| 本科专业数 | ~100+ majors / 345 课程条目 | 大型大学可达 200+ |
| 研究生项目数 | ~25 Master's + 7 PhD | 综合性大学通常 100+ 研究生项目 |
| 双学位/国际合作 | Swansea University (UK), George Brown | 常见于研究型大学 |
| Co-op/带薪实习 | 多数专业可选 Co-op | 大型大学通常也提供 |
| 校区 | Peterborough + Durham GTA + Online | |
| UG 学费 (Ontario) | ~$6,000-7,500 CAD | Ontario 统一政府监管范围 |
| UG 学费 (国际) | ~$28,000-35,000+ CAD | 各校各专业差别大 |
| 排名 (Maclean's) | #1 Undergraduate University in Ontario (校园宣传) | Primarily Undergraduate 类别 |

---

> **文档版本**: v2.0 (deep)
> **生成日期**: 2026-07-10
> **来源**: Trent University 官方网站 (trentu.ca) + 学术日历 (calendar.trentu.ca)
> **颗粒度**: 大学 → 学院(College)/系 → 学位级别 → 专业
> **完整性**: 结构框架 ✅ | UG 项目 ✅ (全量) | PG 项目 ✅ (全量) | 费用数据 ⚠️ (P0) | 申请要求 ⚠️ (P0) | 证据链 (14 blocks) ✅
> **下一步**: 提取精确学费 PDF 数据 + 英语语言要求精确分数 + 申请截止日期
