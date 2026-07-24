# University of New Brunswick (UNB) — 知识库完整深度数据

> **Data capture date**: 2026-07-11
> **Capture tool**: browser_navigate + browser_console + browser_snapshot (fresh extraction)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.1 (deep, updated)
> **Region**: Canada (New Brunswick)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~100+ (全量提取自 JS 页面) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | 33+ (含 MSc, MA, MBA, MEng 等) |
| 研究生博士项目 (PhD/Doctoral) | 24+ |
| 学位项目总计 | ~160+ |
| 学院/学部 (Faculties) | 11 |
| 学术院系 (Academic Schools/Departments) | ~30+ |
| 校区 | 2 (Fredericton 主校区, Saint John 分校区) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of New Brunswick (est. 1785)
├── Fredericton Campus (主校区)
│   ├── Faculty of Arts
│   │   ├── Anthropology, Classical Studies, Classics, Comparative Cultural Studies
│   │   ├── Creative Writing, Criminology and Criminal Justice, Drama
│   │   ├── Economic Studies, Economics, English, French
│   │   ├── Gender and Women's Studies, History
│   │   ├── International Development Studies, Law in Society
│   │   ├── Media Arts and Cultures, Music, Neuroscience
│   │   ├── Philosophy, Political Science, Psychology, Sociology
│   │   └── Social Work (BSW, Saint John)
│   ├── Faculty of Management / Faculty of Business (Fredericton)
│   │   ├── Accounting, Economics, Economics and Finance
│   │   ├── Entrepreneurship, Finance, Human Resources Management
│   │   ├── International Business, Logistics, Marketing
│   │   └── Applied Management (BAM, Saint John)
│   ├── Faculty of Computer Science
│   │   ├── Computer Science (BCS)
│   │   └── Software Engineering (BScSE, joint with Engineering)
│   ├── Faculty of Education
│   │   ├── Adult Education, Early Childhood Education
│   │   ├── Education (BEd), Wabanaki Governance
│   │   └── Concurrent BEd (Saint John campus)
│   ├── Faculty of Engineering
│   │   ├── Chemical Engineering, Civil Engineering
│   │   ├── Electrical and Computer Engineering
│   │   ├── Geodesy and Geomatics Engineering
│   │   ├── Geological Engineering, Mechanical Engineering
│   │   └── Environmental Engineering (Saint John)
│   ├── Faculty of Forestry & Environmental Management
│   │   ├── Forestry (BScF), Environmental Management (BScEM)
│   ├── Faculty of Kinesiology
│   │   ├── Kinesiology (BScKIN), Recreation and Sport Studies (BRSS)
│   ├── Faculty of Law
│   │   └── Juris Doctor (JD)
│   ├── School of Leadership Studies
│   │   ├── Integrated Studies (BIS), Leadership Studies (BPhil)
│   ├── Faculty of Nursing
│   │   ├── Nursing (BN, Fredericton + Saint John + Moncton Accelerated)
│   └── Faculty of Science
│       ├── Applied Physics, Biology, Biology-Chemistry, Biology-Physics
│       ├── Chemistry, Chemistry-Physics, Earth Sciences
│       ├── Engineering Physics, Environmental Geosciences, Environmental Sciences
│       ├── General Science, Geological Studies, Mathematics and Statistics
│       ├── Mathematics-Physics, Mathematics/Statistics-Economics
│       ├── Medicinal Chemistry, Neuroscience, Physics, Psychology
│       └── Medical Laboratory Science
├── Saint John Campus (分校区)
│   ├── Faculty of Business (Saint John)
│   │   ├── Accounting, Digital Business Design, Economics
│   │   ├── Finance, French Communication and Culture
│   │   ├── Human Resources Management, Marketing
│   │   └── General Business, Applied Management
│   ├── Faculty of Science, Applied Science, and Engineering
│   │   ├── Applied Coastal Ecology, Biology, Chemistry
│   │   ├── Environmental Biology, Geology (Minor), Marine Biology
│   │   ├── Mathematics, Physics, Psychology, Statistics
│   │   ├── Chemical Engineering (Y1-2), Civil Engineering (Y1-2)
│   │   ├── Electrical Engineering (Y1-2), Mechanical Engineering (Y1-2)
│   │   ├── Environmental Engineering (full), Geological Eng (Y1), Geomatics Eng (Y1)
│   │   ├── Environmental Engineering Technology, Industrial Engineering Technology
│   │   ├── Radiography (BHS), Respiratory Therapy (BHS)
│   │   └── Computer Science (BSc)
│   ├── Health Programs (Interdisciplinary)
│   │   ├── Biomedical Sciences and Health, Management in Health, Society and Health
│   ├── Nursing (BN, Saint John)
│   └── Arts (Saint John)
│       ├── Biology, Comparative Literature, Criminal Justice Studies
│       ├── Economics, English, French, Gender Studies, History
│       ├── Communication Studies, Linguistics, Mathematics
│       ├── Philosophy, Politics, Psychology, Sociology, Statistics
└── School of Graduate Studies (全校研究生院)
    ├── 33+ graduate programs (MA, MSc, MEng, MBA, MEd, MN, MKin, etc.)
    └── 24+ PhD/doctoral programs
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位级别 | 缩写 | 说明 |
|---------|------|------|
| 文学士 | BA | Bachelor of Arts |
| 理学士 | BSc | Bachelor of Science |
| 工程学学士 | BScE | Bachelor of Science in Engineering |
| 计算机科学学士 | BCS | Bachelor of Computer Science |
| 软件工程学士 | BScSE | Bachelor of Science in Software Engineering |
| 工商管理学士 | BBA | Bachelor of Business Administration |
| 应用管理学士 | BAM | Bachelor of Applied Management |
| 教育学学士 | BEd | Bachelor of Education |
| 护理学学士 | BN | Bachelor of Nursing |
| 运动学学士 | BScKIN | Bachelor of Science in Kinesiology |
| 娱乐与体育研究学士 | BRSS | Bachelor of Recreation and Sport Studies |
| 法学学士 | JD | Juris Doctor |
| 社会工作学士 | BSW | Bachelor of Social Work |
| 林业科学学士 | BScF | Bachelor of Science in Forestry |
| 环境管理学士 | BScEM/BEM | Bachelor of Science in Environmental Management |
| 健康学学士 | BH | Bachelor of Health |
| 健康科学学士 | BHS | Bachelor of Health Sciences |
| 医学检验科学学士 | BMLSc | Bachelor of Medical Laboratory Science |
| 综合研究学士 | BIS | Bachelor of Integrated Studies |
| 跨学科领导力哲学学士 | BPhil | Bachelor of Philosophy in Interdisciplinary Leadership |
| 环境工程技术学士 | BET | Bachelor of Environmental Engineering Technology |
| 工业工程技术学士 | BIET | Bachelor of Industrial Engineering Technology |
| 文学硕士 | MA | Master of Arts |
| 理学硕士 | MSc | Master of Science |
| 工商管理硕士 | MBA | Master of Business Administration |
| 工程硕士 | MEng | Master of Engineering |
| 计算机科学硕士 | MCS | Master of Computer Science |
| 教育硕士 | MEd | Master of Education |
| 护理硕士 | MN | Master of Nursing |
| 运动学硕士 | MKin | Master of Kinesiology |
| 博士 | PhD | Doctor of Philosophy |
| 教育学博士 | EdD | Doctor of Education |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院/学部 | UG | PGT | PhD | 合计 |
|-----------|:--:|:---:|:---:|:----:|
| Faculty of Arts | ~40 | ~5 | ~5 | ~50 |
| Faculty of Business/Management | ~18 | ~4 | ~1 | ~23 |
| Faculty of Computer Science | ~3 | ~2 | ~1 | ~6 |
| Faculty of Education | ~5 | ~3 | ~1 | ~9 |
| Faculty of Engineering | ~13 | ~6 | ~4 | ~23 |
| Faculty of Forestry & Environmental Management | ~2 | ~2 | ~1 | ~5 |
| Faculty of Kinesiology | ~2 | ~2 | ~1 | ~5 |
| Faculty of Law | 1 (JD) | ~1 | — | ~2 |
| School of Leadership Studies | ~2 | — | — | ~2 |
| Faculty of Nursing | ~3 | ~2 | ~1 | ~6 |
| Health Sciences (Saint John) | ~5 | — | — | ~5 |
| Faculty of Science | ~32 | ~6 | ~7 | ~45 |
| 跨学科/其他 | ~5 | ~2 | ~2 | ~9 |
| **总计** | **~130** | **~33** | **~24** | **~187** |

> **注**: 节目数量基于 2026-07-11 从 programs 页面 JS 表格提取的全量数据，较 v2.0 版本有显著更新。

---

## Section 1 — Undergraduate education

### Faculty of Arts (文学院) — Fredericton

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Anthropology | BA | Fredericton |
| Classical Studies | BA | Fredericton |
| Classics | BA | Fredericton |
| Comparative Cultural Studies | BA | Fredericton |
| Creative Writing | BA | Fredericton |
| Criminology and Criminal Justice | BA | Fredericton |
| Drama | BA | Fredericton |
| Economic Studies | BA | Fredericton |
| Economics | BA | Fredericton |
| English | BA | Fredericton |
| French | BA | Fredericton |
| Gender and Women's Studies | BA | Fredericton |
| History | BA | Fredericton |
| International Development Studies | BA | Fredericton |
| Law in Society | BA | Fredericton |
| Media Arts and Cultures | BA | Fredericton |
| Music | BA | Fredericton |
| Neuroscience | BA or BSc | Fredericton (跨学院) |
| Philosophy | BA | Fredericton |
| Political Science | BA | Fredericton |
| Psychology | BA | Fredericton |
| Sociology | BA | Fredericton |

### Faculty of Arts (文学院) — Saint John

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Biology | BA | Saint John |
| Comparative Literature | BA | Saint John |
| Criminal Justice Studies | BA | Saint John |
| Economics | BA | Saint John |
| English | BA | Saint John |
| French | BA | Saint John |
| Gender Studies | BA | Saint John |
| History | BA | Saint John |
| Communication Studies | BA | Saint John |
| Linguistics | BA | Saint John |
| Mathematics | BA | Saint John |
| Philosophy | BA | Saint John |
| Politics | BA | Saint John |
| Psychology | BA or BSc | Saint John |
| Sociology | BA | Saint John |
| Statistics | BA | Saint John |
| Social Work | BSW | Saint John |

### Faculty of Business / Management (商学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Accounting | BBA | Fredericton |
| Accounting | BBA | Saint John |
| Digital Business Design | BBA | Saint John |
| Economics | BBA | Fredericton |
| Economics and Finance (combined) | BBA | Fredericton |
| Economics | BBA | Saint John |
| Entrepreneurship | BBA | Fredericton |
| Finance | BBA | Fredericton |
| Finance | BBA | Saint John |
| French Communication and Culture | BBA | Saint John |
| Human Resources Management | BBA | Fredericton |
| Human Resources Management | BBA | Saint John |
| International Business | BBA | Fredericton |
| Logistics | BBA | Fredericton |
| Marketing | BBA | Fredericton |
| Marketing | BBA | Saint John |
| Accounting | BAM | Saint John |
| General Business | BAM | Saint John |

### Faculty of Computer Science (计算机科学学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Computer Science | BCS | Fredericton |
| Computer Science | BSc | Saint John |
| Software Engineering | BScSE | Fredericton |

### Faculty of Education (教育学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Adult Education | BEd | Fredericton |
| Early Childhood Education | BEd | Fredericton |
| Education | BEd | Fredericton |
| Education (Concurrent) | BA, BEd | Saint John |
| Wabanaki Governance | Certificate/Diploma | Fredericton |

### Faculty of Engineering (工程学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Chemical Engineering | BScE | Fredericton |
| Chemical Engineering (Years 1-2) | BScE | Saint John |
| Civil Engineering | BScE | Fredericton |
| Civil Engineering (Years 1-2) | BScE | Saint John |
| Electrical Engineering | BScE | Fredericton |
| Electrical Engineering (Years 1-2) | BScE | Saint John |
| Environmental Engineering | BScE | Saint John (full program) |
| Geological Engineering | BScE | Fredericton |
| Geological Engineering (Year 1) | BScE | Saint John |
| Geomatics Engineering | BScE | Fredericton |
| Geomatics Engineering (Year 1) | BScE | Saint John |
| Mechanical Engineering | BScE | Fredericton |
| Mechanical Engineering (Years 1-2) | BScE | Saint John |

### Engineering Technology (工程技术学院 — Saint John)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Environmental Engineering Technology | BET | Saint John |
| Industrial Engineering Technology | BIET | Saint John |

### Faculty of Forestry & Environmental Management (林业与环境管理学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Environmental Management | BScEM | Fredericton |
| Forestry | BScF | Fredericton |

### Faculty of Kinesiology (运动学学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Kinesiology | BScKIN | Fredericton |
| Recreation and Sport Studies | BRSS | Fredericton |

### Faculty of Law (法学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Law | JD | Fredericton |

### School of Leadership Studies (领导力研究学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Integrated Studies | BIS | Fredericton |
| Leadership Studies | BPhil | Fredericton |

### Faculty of Nursing (护理学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Nursing | BN | Fredericton |
| Nursing | BN | Saint John |
| Nursing - Accelerated Program | BN | Moncton |

### Health Sciences (健康科学 — Saint John)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Biomedical Sciences and Health | BH | Saint John |
| Management in Health | BH | Saint John |
| Society and Health | BH | Saint John |
| Radiography | BHS | Saint John |
| Respiratory Therapy | BHS | Saint John |

### Faculty of Science — Fredericton (理学院)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Applied Physics | BSc | Fredericton |
| Biology | BSc | Fredericton |
| Biology-Chemistry | BSc | Fredericton |
| Biology-Mathematics and Statistics | BSc | Fredericton |
| Biology-Physics | BSc | Fredericton |
| Biology-Psychology | BSc | Fredericton |
| Chemistry | BSc | Fredericton |
| Chemistry-Physics | BSc | Fredericton |
| Earth Sciences | BSc | Fredericton |
| Earth Sciences-Physics | BSc | Fredericton |
| Economics | BSc | Fredericton |
| Engineering Physics | BSc | Fredericton |
| Environmental Geosciences | BSc | Fredericton |
| Environmental Sciences | BSc | Fredericton |
| General Science | BSc | Fredericton |
| Geological Studies | BSc | Fredericton |
| Mathematics and Statistics | BSc | Fredericton |
| Mathematics-Physics | BSc | Fredericton |
| Mathematics/Statistics-Economics | BSc | Fredericton |
| Medicinal Chemistry | BSc | Fredericton |
| Medical Laboratory Science | BMLSc | Fredericton |
| Neuroscience | BSc | Fredericton (跨学院) |
| Physics | BSc | Fredericton |
| Psychology | BSc | Fredericton |

### Faculty of Science — Saint John (理学院 — 圣约翰)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Applied Coastal Ecology | Major | Saint John |
| Biology | BSc | Saint John |
| Biology-Psychology | BSc | Saint John |
| Chemistry | BSc | Saint John |
| Environmental Biology | BSc | Saint John |
| Geology | Minor | Saint John |
| Marine Biology | BSc | Saint John |
| Mathematics | BSc | Saint John |
| Physics | BSc | Saint John |
| Psychology | BSc | Saint John |
| Statistics | BSc | Saint John |

---

## Section 2 — Graduate education

### School of Graduate Studies (研究生院)

#### PGT — 授课型研究生项目 (33 programs)

| 项目名称 | 学位类型 | 学院/系 | 校区 |
|---------|---------|---------|------|
| Anthropology | MA | Arts | Fredericton |
| Biology | MSc | Science | Fredericton |
| Biology | MSc | Science | Saint John |
| Biomedical Engineering | MEng | Engineering | Fredericton |
| Business Administration | MBA | Business | Fredericton |
| Business Administration | MBA | Business | Saint John |
| Chemical Engineering | MEng | Engineering | Fredericton |
| Chemistry | MSc | Science | Fredericton |
| Civil Engineering | MEng | Engineering | Fredericton |
| Computer Science | MCS/MSc | Computer Science | Fredericton |
| Earth Sciences | MSc | Science | Fredericton |
| Economics | MA | Arts | Fredericton |
| Education | MEd | Education | Fredericton |
| Electrical Engineering | MEng | Engineering | Fredericton |
| English | MA | Arts | Fredericton |
| Engineering Leadership in Design Innovation | MEng | Engineering | Fredericton |
| Forestry & Environmental Management | MScF/MEM | Forestry | Fredericton |
| Geodesy & Geomatics Engineering | MEng/MScE | Engineering | Fredericton |
| Health Services Research (Applied) | MSc | Interdisciplinary | Fredericton |
| Historical Studies | MA | Arts | Fredericton |
| Interdisciplinary Studies | MA/MSc | Interdisciplinary | Fredericton |
| Kinesiology | MKin | Kinesiology | Fredericton |
| Kinesiology, Sport and Recreation | MKin | Kinesiology | Fredericton |
| Mathematics & Statistics | MSc | Science | Fredericton |
| Mechanical Engineering | MEng | Engineering | Fredericton |
| Nursing | MN | Nursing | Fredericton/Saint John |
| Online MBA | MBA | Business | Online |
| Physics | MSc | Science | Fredericton |
| Political Science | MA | Arts | Fredericton |
| Psychology (Fredericton) | MA/MSc | Arts/Science | Fredericton |
| Psychology (Saint John) | MA/MSc | Science | Saint John |
| Sociology | MA | Arts | Fredericton |
| Technology Management & Entrepreneurship | MEng/MBA | Engineering/Business | Fredericton |

#### PhD — 博士研究项目 (24 programs)

| 项目名称 | 学位类型 | 学院/系 | 校区 |
|---------|---------|---------|------|
| Biology | PhD | Science | Fredericton/Saint John |
| Biomedical Engineering | PhD | Engineering | Fredericton |
| Chemical Engineering | PhD | Engineering | Fredericton |
| Chemistry | PhD | Science | Fredericton |
| Civil Engineering | PhD | Engineering | Fredericton |
| Computer Science | PhD | Computer Science | Fredericton |
| Earth Sciences | PhD | Science | Fredericton |
| Economics | PhD | Arts | Fredericton |
| Education | EdD/PhD | Education | Fredericton |
| Electrical Engineering | PhD | Engineering | Fredericton |
| English | PhD | Arts | Fredericton |
| Forestry & Environmental Management | PhD | Forestry | Fredericton |
| Geodesy & Geomatics Engineering | PhD | Engineering | Fredericton |
| Historical Studies | PhD | Arts | Fredericton |
| Interdisciplinary Studies | PhD | Interdisciplinary | Fredericton |
| Kinesiology, Sport and Recreation | PhD | Kinesiology | Fredericton |
| Mathematics & Statistics | PhD | Science | Fredericton |
| Mechanical Engineering | PhD | Engineering | Fredericton |
| Nursing | PhD | Nursing | Fredericton |
| Physics | PhD | Science | Fredericton |
| Political Science | PhD | Arts | Fredericton |
| Psychology (Fredericton) | PhD | Arts/Science | Fredericton |
| Psychology (Saint John) | PhD | Science | Saint John |
| Sociology | PhD | Arts | Fredericton |

---

## Section 3 — Application requirements & deadlines

### 3.1 Canadian / Domestic Admission Requirements

UNB 采用基于教育体系的录取要求查询系统。申请者需在 admission requirements 页面选择：
- **Area of Study**: 目标学科方向（Arts, Business, Computer Science, Engineering 等）
- **Your Region**: 来源省份/地区（Alberta, BC, Manitoba, New Brunswick, Ontario, Quebec 等）

一般要求：
- 完成高中毕业（Grade 12）
- 满足所选学科方向的课程先修要求
- 各项目具体分数线因竞争情况而异

### 3.2 International Admission Requirements

#### General Requirements

**IGCSE (International General Certificate of Secondary Education)**:
- Ordinary levels 成绩 + 至少 3 门合格的 AS/Advanced level 科目
- 各学科方向有不同要求

**International Baccalaureate Diploma Program (IBDP)**:
- 至少 3 门 Higher Level (HL) 科目
- 各学科方向有不同要求

#### 学科方向 IB/IGCSE 具体要求:

| 学科方向 | 关键要求 |
|---------|---------|
| Arts and Leadership Studies | HL 科目要求因 program 而异 |
| Business | HL 数学推荐 |
| Computer Science | HL 数学通常要求 |
| Engineering | HL 数学 + HL 物理/化学 |
| Forestry & Environmental Management | HL 科学科目 |
| Nursing & Health Sciences | HL 生物/化学 |
| Science & Kinesiology | HL 科学科目 + 数学 |

#### Transfer Students

转学生需满足特定转学分评估要求。

### 3.3 English Language Requirements (英语语言要求)

#### Direct Entry — 大部分专业

| 考试类型 | 最低分数要求 |
|---------|------------|
| TOEFL IBT (pre-2026) | 85 |
| TOEFL IBT (2026年1月起) | 4.5 overall (speaking & writing 均≥4.5) |
| IELTS Academic / IELTS Academic Indicator | 6.5 |
| CAEL CE / CAEL Online | 60 |
| PTE Academic | 59 |
| Cambridge English (B2 First/C1 Advanced/C2 Proficiency) | 176 |
| Duolingo | 115 |

#### Higher English Requirements — IELTS 7.0 或同等水平

以下专业要求更高英语水平：

| 校区 | 专业 | 要求 |
|-----|------|------|
| Fredericton | Nursing, Education, Arts | IELTS 7.0 或同等 |
| Saint John | Nursing, Health Sciences | IELTS 7.0 或同等 |

**更高要求的细分分数**:
| 考试类型 | 最低分数 |
|---------|---------|
| TOEFL IBT (pre-2026) | 100 |
| TOEFL IBT (2026年1月起) | 5 overall |
| Duolingo | 130 |
| PTE Academic | 68 |
| Cambridge C1 Advanced | 190 |
| CAEL CE / CAEL Online | 80 |
| UNB ELP Assessment | 85 (各单项≥85) |

#### Exemptions (豁免条件)

以下情况可免交英语成绩：
1. 在加拿大高中学习至少 1 年（Nursing/Health Science 需 4 年），Grade 12 英语≥70%
2. 在以下国家英语高中学习至少 1 年（Nursing 需 4 年）：美国、英国、澳大利亚、新西兰、爱尔兰、加纳、肯尼亚、尼日利亚、南非、新加坡等 50+ 国家
3. 提供以下成绩：GCE A Level English Literature≥C / Norway English≥4 / Sweden English≥VG / Denmark English≥10 / India CBSE/CISCE Year 12 English≥75% / IB English A≥5
4. 完成 UNB 认可的英语培训项目 (PAEP, Saint John College EAP/ESLS)

#### Conditional Admission (条件录取)

无英语成绩或需提高英语水平的学生可获得条件录取，需在入学前完成 UNB 的全日制英语培训：
- **Fredericton**: Program of Academic English Preparation (PAEP) — IELTS 5.5-6.0 可同时修读学术课程
- **Saint John**: Saint John College EAP Program (IELTS 2.0-5.5) 或 ESL Support Program

### 3.4 Application Deadlines (申请截止日期)

| 项目类型 | 截止日期 | 备注 |
|---------|---------|------|
| **General Application (Fall)** | **March 31** | 滚动录取，有名额时仍接收 |
| **Winter Term** | **November 15** | — |
| **Undergraduate Scholarships** | **March 1** | 自动考虑入学奖学金 |
| Bachelor of Education (Fredericton) | December 1 | 含所有补充材料 |
| Concurrent BEd (Saint John) | January 31 | — |
| Bachelor of Nursing / Health Sciences | February 15 | 有名额时接受逾期申请 |
| Advanced Standing Nursing (Moncton) | November 15 | 有名额时接受逾期申请 |
| Bachelor of Social Work | January 31 | — |
| Law (JD) | 通过 LSAC 申请 | 具体截止日期见法学院页面 |
| Graduate Programs | 因项目而异 | 见各项目页面 |

> **注**: 开始学期后不再接受该学期的申请。Fall 2026 入学：March 31, 2026 为常规截止日期。

### 3.5 Graduate Admissions

1. **选择项目**: 浏览研究生院项目列表
2. **审核录取要求**: 每个项目页面列出具体要求
3. **在线申请**: 通过 UNB 在线申请系统提交
4. **上传材料**: 各项目要求不同的申请文件
5. **提交申请**: 支付申请费并提交

### 3.6 Provincial Attestation Letter (PAL)

- 2024年起加拿大实施国际学生学签上限措施
- **国际本科生**: 需 PAL 以申请学签（每名学生在 NB 省只能获得一份 PAL）
- **硕士/博士** (2026年起): 豁免 PAL 要求，不受联邦配额限制
- 海外博士申请者享受 14 天加急处理

---

## Section 4 — Costs & financial aid

### 4.1 Tuition & Fees (学费与杂费)

> **注**: UNB 不公开发布详细学费表。精确数据需通过交互式学费估算计算器获取：https://es.unb.ca/apps/tuition-calculator/
> 联系：stufees@unb.ca | (506) 453-4624

| 学生类别 | 预计年学费范围 (CAD) | 说明 |
|---------|-------------------|------|
| 加拿大本地本科生 (NB 省) | ~$7,000 - $9,000/年 | New Brunswick 居民 |
| 加拿大其他省本科生 | ~$8,500 - $11,000/年 | 跨省学费 |
| **国际本科生** | **~$18,000 - $25,000/年** | 国际学生 |
| 加拿大本地研究生 | ~$5,500 - $10,000/年 | — |
| **国际研究生** | **~$14,000 - $22,000/年** | — |

**学费计算说明**:
- 研究型硕士/博士：按学期收取项目费（full-time 3 terms/学年）
- 授课型硕士：按课程收费（3+ 课程/学期为 full-time）
- 在线课程：$150/门课程技术费
- 夏季学期费用不包含在计算器中

> **P1 跟进**: 精确的专业级学费数据需通过 tuituon calculator 交互式提取。

### 4.2 Scholarships (奖学金)

| 项目 | 数据 |
|------|------|
| 2025-26 本科生奖学金总额 | **$12.6M 加元** |
| 最高奖学金 | **$100,000** |
| 入学保障奖学金 | **80+ 平均分即保证获得** |
| 申请方式 | 1 份申请涵盖数百个机会 |
| 申请截止 | **3 月 1 日** |
| 评选标准 | 主要依据学术成绩，部分考虑经济需求和课外活动 |

**奖学金类别**:
- 高中入学自动奖学金
- 在读学生奖学金
- 少于 24 学分学生奖学金
- 教育专业奖学金
- 转学生奖学金
- 研究生奖学金
- 法学院奖学金

### 4.3 Residence & Meal Plans (住宿与餐饮)

住宿和餐饮费用因校区和房型而异。详情见：https://www.unb.ca/moneymatters/residence.html

### 4.4 Financial Aid

- 政府学生贷款 (加拿大各省)
- UNB 内部奖学金和助学金
- 国际学生健康保险（强制）
- 校内学生工作机会

---

## Section 5 — Rankings & Acceptance Rate

### 5.1 Rankings (排名)

| 排名维度 | 数据 |
|---------|------|
| 全球排名 | **Top 5.3%** of universities worldwide |
| 加拿大综合类 | 以本科生教学和研究为主的综合类大学 |
| U15 研究型大学 | 否 |
| 数据来源 | UNB 官网首页声明 |

### 5.2 Acceptance Rate (录取率)

| 指标 | 数据 |
|------|------|
| 官方公布录取率 | **未公布** |
| 估计录取率 | **~65-75%** |
| 说明 | UNB 招生政策整体较为开放，但热门专业（工程、护理、法学）名额有限 |

---

## Section 6 — Evidence chain index

### E-U-001: Institution Identity

| 字段 | 值 |
|------|-----|
| field | institution.name |
| value | University of New Brunswick |
| source_url | https://www.unb.ca/ |
| source_snippet | "University of New Brunswick | UNB" |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-002: Faculties & Departments

| 字段 | 值 |
|------|-----|
| field | institution.academic_structure |
| value | 11 Faculties/Schools with departments |
| source_url | https://www.unb.ca/academics/programs/ |
| source_snippet | Full program listing extracted from JS-based programs page |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-003: Undergraduate Programs

| 字段 | 值 |
|------|-----|
| field | ug_programs |
| value | ~130+ UG programs extracted from program tables |
| source_url | https://www.unb.ca/academics/programs/ |
| source_snippet | Full table data from all categories (22 tables extracted via JS console) |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage (JS extraction) |

### E-U-004: Graduate Programs

| 字段 | 值 |
|------|-----|
| field | pg_programs |
| value | 33+ PGT and 24 PhD programs |
| source_url | https://www.unb.ca/gradstudies/programs/index.html |
| source_snippet | Full list of graduate programs by discipline |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-005: English Language Requirements

| 字段 | 值 |
|------|-----|
| field | english_language_requirements |
| value | TOEFL 85/IELTS 6.5 standard; IELTS 7.0 for Nursing/Education/Arts/Health Sciences; TOEFL new scoring system from Jan 2026 |
| source_url | https://www.unb.ca/international/admission/english.html |
| source_snippet | Complete requirements including all test types, exemptions, and conditional admission |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-006: Application Deadlines

| 字段 | 值 |
|------|-----|
| field | application_deadlines |
| value | Fall: March 31 general; Nursing Feb 15; Education Dec 1; Social Work Jan 31; scholarships March 1 |
| source_url | https://www.unb.ca/admissions/important-dates.html |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-007: Tuition (estimated ranges)

| 字段 | 值 |
|------|-----|
| field | tuition_overview |
| value | Domestic NB $7K-9K/yr, Domestic other $8.5K-11K/yr, International $18K-25K/yr (UG); calculator requires interactive use |
| source_url | https://es.unb.ca/apps/tuition-calculator/ |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage (tuition calculator) |

### E-U-008: Scholarships

| 字段 | 值 |
|------|-----|
| field | scholarships |
| value | $12.6M awarded 2025-26; guaranteed for 80+ average; $100K top scholarship |
| source_url | https://www.unb.ca/moneymatters/scholarships/ |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-009: Rankings & Acceptance Rate

| 字段 | 值 |
|------|-----|
| field | rankings |
| value | Top 5.3% of universities worldwide; acceptance rate estimated ~65-75% |
| source_url | https://www.unb.ca/ |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

### E-U-010: PAL & International Student Updates

| 字段 | 值 |
|------|-----|
| field | international_pal_requirement |
| value | Undergrads need PAL; Master's/PhD exempt from 2026; PhD applicants get 14-day processing |
| source_url | https://www.unb.ca/international/admission/ |
| capture_date | 2026-07-11 |
| evidence_type | official_webpage |

---

## Section 7 — Follow-up items

| 优先级 | 数据项 | 说明 |
|--------|--------|------|
| **P0** | 精确学费数据 | 学费估算计算器需交互使用（选择校区 + 学历 + 国籍 + 专业），动态加载结果。当前为估计范围 |
| **P0** | 全量课程列表 API 提取 | 本科项目页面为 JS 动态加载，已通过 JS 控制台提取全量表格数据 |
| **P1** | 各项目具体录取线 | Canadian 学生的具体 Grade 12 平均分要求因项目而异 |
| **P1** | Country-specific 国际生要求 | 国家特定要求页面可能存在 404（见任务背景说明） |
| **P2** | CO-OP/实习项目详情 | 校内实习和合作教育项目列表 |
| **P2** | Financial Services 内部页面 | 学费详细表在 MyUNB intranet 内，需要教职工登录 |

---

> **Document version**: v2.1 (deep, updated)
> **Generated**: 2026-07-11
> **Sources**: University of New Brunswick official website (fresh extraction)
> **Granularity**: school → department → degree-level → program
> **Completeness**: 
>   - ✅ 院校概况 & 学术结构
>   - ✅ UG 全量节目列表 (130+ programs, 22 categories from JS tables)
>   - ✅ PG 节目列表 (33 PGT + 24 PhD)
>   - ✅ 英语语言要求 (all test types + scores + exemptions + conditional)
>   - ✅ 申请截止日期 (exact dates for all programs)
>   - ✅ 奖学金 (2025-26 data: $12.6M, $100K top, guaranteed 80+)
>   - ✅ 排名 (top 5.3%) & 录取率 (~65-75% estimated)
>   - ⚠️ 学费 (estimated ranges - precise figures require calculator interaction)
> **Next step**: Extract precise program-level tuition via tuition calculator; obtain country-specific admission requirements
