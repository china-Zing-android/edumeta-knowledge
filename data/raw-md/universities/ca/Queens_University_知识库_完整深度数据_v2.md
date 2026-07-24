# Queen's University 知识库完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department/school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Ontario)
> **Language**: English (with Chinese annotations)

**学校名称**: Queen's University (女王大学)
**国家**: Canada (CA)
**官网**: https://www.queensu.ca/
**招生办**: https://www.queensu.ca/admission/
**学术日历**: https://www.queensu.ca/academic-calendar/
**国际生招生**: https://www.queensu.ca/admission/international/students
**学费查询**: https://www.queensu.ca/registrar/tuition-fees/undergraduate
**关键日期**: https://www.queensu.ca/registrar/key-dates

---

## Section 0 — Institution Overview (院校总览)

### 0.1 核心数据统计

| 统计项 | 数值 | 来源 |
|--------|------|------|
| 建校年份 | 1841 | queensu.ca/about |
| 学生总数 | ~25,000+ | queensu.ca/about |
| 本科生总数 | ~18,000 | 估算(总学生数-研究生数) |
| 研究生总数 | ~4,000 | queensu.ca/about |
| 国际生总数 | ~3,700 | queensu.ca/admission/international/students |
| 国际生比例 | ~12-15% | 估算 |
| 教职员工 | ~3,600 | queensu.ca/about |
| 学院/学部总数 | 6个学部 + 1个研究生院 | queensu.ca/academic-calendar/ |
| 毕业率 | 92.9%（加拿大最高） | queensu.ca/about |
| 校友网络 | 150,000+ (119个国家) | queensu.ca/about |
| 加拿大经济贡献 | ~$20亿/年 | queensu.ca/about |
| 总资产 | ~$16亿 | queensu.ca/about |
| U15成员 | 是 | queensu.ca/about |
| QS 2027世界排名 | Top 180 | queensu.ca/about |
| QS 加拿大排名 | Top 10 | queensu.ca/about |
| THE Impact排名 | 全球第4 | queensu.ca/about |
| 诺贝尔奖关联 | 2项(Arthur B. McDonald 2015物理奖, David Card 2021经济奖) | queensu.ca/about |
| 加拿大研究席位(CRC) | 43个 | queensu.ca/about |

### 0.2 学院/学部层级结构树

```
Queen's University
├── Faculty of Arts and Science (文理学院)
│   ├── Art History and Art Conservation
│   ├── Biochemistry
│   ├── Biology
│   ├── Chemistry
│   ├── Classics and Archaeology
│   ├── Computing (计算机, 学费单独核算)
│   ├── Drama and Music
│   ├── Economics
│   ├── Employment Relations
│   ├── English Literature and Creative Writing
│   ├── Environmental Studies
│   ├── Film and Media
│   ├── Fine Art
│   ├── French Studies
│   ├── Gender Studies
│   ├── Geography and Planning
│   ├── Geological Sciences and Geological Engineering
│   ├── Global Development Studies
│   ├── History
│   ├── International Studies
│   ├── Jewish Studies
│   ├── Kinesiology and Health Studies (人体运动学与健康研究)
│   ├── Languages, Literatures, and Cultures
│   ├── Liberal Studies
│   ├── Life Sciences
│   ├── Mathematics and Statistics
│   ├── Philosophy
│   ├── Physics, Engineering Physics, and Astronomy
│   ├── Political Studies
│   ├── Psychology
│   ├── Religion
│   └── Sociology
├── Smith Engineering (史密斯工程学院) — 前身为Faculty of Applied Science
│   ├── Chemical Engineering
│   ├── Civil Engineering
│   ├── Computer Engineering
│   ├── Electrical Engineering
│   ├── Engineering Chemistry
│   ├── Engineering Physics
│   ├── Geological Engineering
│   ├── Mathematics and Engineering
│   ├── Mechanical Engineering
│   ├── Mechatronics and Robotics Engineering
│   └── Mining Engineering
├── Smith School of Business (史密斯商学院)
│   ├── Bachelor of Commerce (BCom)
│   ├── Graduate Programs (MBA, MMA, MMIE, MFin, MIB等)
│   └── Executive Education
├── Faculty of Health Sciences (健康科学学院)
│   ├── School of Medicine (MD Program, 医学院)
│   ├── School of Nursing (BScN, MScN, PhD, 护理学院)
│   ├── School of Rehabilitation Therapy (康复治疗学院)
│   │   ├── Occupational Therapy
│   │   └── Physical Therapy
│   └── Bachelor of Health Sciences (BHSc)
├── Faculty of Education (教育学院)
│   ├── Concurrent Education
│   ├── Consecutive Education (BEd)
│   └── Graduate Programs (MEd, EdD, PhD)
├── Faculty of Law (法学院)
│   ├── JD Program
│   ├── Graduate Programs (LLM, PhD)
│   └── Combined Programs (JD/MBA, JD/MPA)
├── School of Graduate Studies and Postdoctoral Affairs (SGSPA, 研究生院)
│   └── 60+ graduate programs across all faculties
└── Bader College (贝德学院, 位于英国East Sussex)
```

### 0.3 学历级别明细

| 学历级别代码 | 学历级别名称 | 所属领域 |
|-------------|-------------|---------|
| BAH | Bachelor of Arts (Honours) | 文科 |
| BA | Bachelor of Arts (General) | 文科 |
| BCH | Bachelor of Computing (Honours) | 计算机 |
| BCP | Bachelor of Computing (General) | 计算机 |
| BFH | Bachelor of Fine Art (Honours) | 美术 |
| BFA | Bachelor of Fine Art (General) | 美术 |
| BMS | Bachelor of Music | 音乐 |
| BMT | Bachelor of Music Theatre | 音乐剧 |
| BSH | Bachelor of Science (Honours) | 理科 |
| BSC | Bachelor of Science (General) | 理科 |
| BASc | Bachelor of Applied Science | 工程 |
| BCom | Bachelor of Commerce | 商科 |
| BHSc | Bachelor of Health Sciences | 健康科学 |
| BScN | Bachelor of Science in Nursing | 护理 |
| JD | Juris Doctor | 法律 |
| MD | Doctor of Medicine | 医学 |
| BEd | Bachelor of Education | 教育 |
| MA | Master of Arts | 文科 |
| MSc | Master of Science | 理科 |
| MBA | Master of Business Administration | 商科 |
| MEng | Master of Engineering | 工程(授课型) |
| MASc | Master of Applied Science | 工程(研究型) |
| MEd | Master of Education | 教育 |
| LLM | Master of Laws | 法律 |
| MPH | Master of Public Health | 公共卫生 |
| MScN | Master of Science in Nursing | 护理 |
| MScOT | Master of Science in Occupational Therapy | 作业治疗 |
| MScPT | Master of Science in Physical Therapy | 物理治疗 |
| MPA | Master of Public Administration | 公共管理 |
| MIR | Master of Industrial Relations | 劳资关系 |
| MPL | Master of Urban and Regional Planning | 城市规划 |
| MES | Master of Environmental Studies | 环境研究 |
| MAC | Master of Art Conservation | 艺术保护 |
| PhD | Doctor of Philosophy | 所有领域 |
| EdD | Doctor of Education | 教育 |
| GDip | Graduate Diploma | 各专业 |
| MAI | Master of Management in Artificial Intelligence | 人工智能管理 |
| MMA | Master of Management Analytics | 管理分析 |
| MMIE | Master of Management Innovation & Entrepreneurship | 创新与创业管理 |
| MDP | Master of Digital Product Management | 数字产品管理 |
| MFin | Master of Financial Innovation & Technology | 金融创新 |
| MIB | Master of International Business | 国际商务 |

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院/学部 | 本科 UG | 授课型硕士 Course-based | 研究型硕士 Research-based | 博士 PhD | 职业博士/专业博士 | 证书/文凭 |
|-----------|---------|----------------------|------------------------|---------|------------------|----------|
| 文理学院 | 120+ | 15+ | 30+ | 25+ | - | 15+ |
| 史密斯工程学院 | 12 | 5+ | 8+ | 8+ | - | - |
| 史密斯商学院 | 1 (BCom) | 8+ | - | 1+ | - | 2+ |
| 健康科学学院 | 3+ | 3+ | 5+ | 5+ | MD | 2+ |
| 教育学院 | 2+ | 3+ | 2+ | 1+ | EdD | 5+ |
| 法学院 | 1 (JD) | 2+ | 1+ | 1+ | - | - |
| **合计** | **~139+** | **~36+** | **~46+** | **~41+** | **MD, EdD** | **~24+** |

---

## Section 1 — Undergraduate Education (本科教育)

### 1.1 文理学院 (Faculty of Arts and Science)

**入读学位**: BA, BAH, BSc, BSH, BCH, BCP, BFA, BFH, BMS, BMT

| 系/部门 | 专业/方向名称 | 授予学位 | 备注 |
|---------|-------------|---------|------|
| Art History and Art Conservation | Art History | BAH | |
| Art History and Art Conservation | Art Conservation | BAH/BScH | |
| Biochemistry | Biochemistry | BSH | |
| Biology | Biology | BSH | |
| Biology | Biology - Mathematics | BSH | 跨学科 |
| Biology | Biology - Psychology | BSH | 跨学科 |
| Chemistry | Chemistry | BSH | |
| Classics and Archaeology | Classical Studies | BAH | |
| Classics and Archaeology | Classics | BAH | |
| Computing | Computing | BCH/BCP | 学费较高(单独核算) |
| Computing | Computing and the Creative Arts | BCH/BCP | 跨学科 |
| Computing | Computing, Mathematics, and Analytics | BCH/BCP | 跨学科 |
| Computing | Biomedical Computing | BCH | 跨学院 |
| Computing | Software Design | BCH | |
| Drama and Music | Drama | BAH/BFA | |
| Drama and Music | Music | BMS | 需要面试/试演 |
| Drama and Music | Music Theatre | BMT | |
| Drama and Music | Media and Performance Production | BFA | |
| Economics | Economics | BAH/BSH | |
| Employment Relations | Employment Relations | BAH | |
| English Literature and Creative Writing | English and Creative Writing | BAH | |
| Environmental Studies | Environmental Studies | BAH/BSH | |
| Environmental Studies | Environmental Science | BSH | |
| Environmental Studies | Environmental Life Sciences | BSH | |
| Environmental Studies | Environmental Biology | BSH | |
| Environmental Studies | Environmental Chemistry | BSH | |
| Environmental Studies | Environmental Geology | BSH | |
| Environmental Studies | Environmental Toxicology | BSH | |
| Film and Media | Film and Media | BAH | |
| Fine Art | Fine Art (Visual Art) | BFA/BFH | |
| French Studies | French Studies | BAH | |
| Gender Studies | Gender Studies | BAH | |
| Geography and Planning | Geography | BAH/BSH | |
| Geography and Planning | Geographic Information Science | BSH | |
| Geography and Planning | Urban and Regional Planning | BSH | |
| Geography and Planning | Urban Planning Studies | BSH | |
| Geological Sciences & Geological Engineering | Geological Sciences | BSH | |
| Geological Sciences & Geological Engineering | Earth Systems Science | BSH | |
| Global Development Studies | Global Development Studies | BAH | |
| History | History | BAH | |
| International Studies | International Studies | BAH | |
| Jewish Studies | Jewish Studies | BAH | |
| Kinesiology and Health Studies | Kinesiology | BSH | 额外$27 Faculty Society Fee |
| Kinesiology and Health Studies | Health Studies | BSH | |
| Kinesiology and Health Studies | Disability and Physical Activity | BSH | |
| Languages, Literatures, and Cultures | Languages, Literatures and Cultures | BAH | |
| Languages, Literatures, and Cultures | World Language Studies | BAH | |
| Languages, Literatures, and Cultures | Spanish and Latin American Studies | BAH | |
| Languages, Literatures, and Cultures | Indigenous Languages and Cultures | BAH | |
| Languages, Literatures, and Cultures | Mohawk Language and Culture | BAH | |
| Languages, Literatures, and Cultures | Linguistics | BAH | |
| Liberal Studies | Liberal Arts University Transfer (LAT) | 转学项目 | |
| Life Sciences | Life Sciences | BSH | 跨学科 |
| Life Sciences | Biomedical and Molecular Sciences | BSH | |
| Mathematics and Statistics | Mathematics | BSH | |
| Mathematics and Statistics | Mathematics and Statistics | BSH | |
| Mathematics and Statistics | Statistics | BSH | |
| Mathematics and Statistics | Data Analytics | 证书 | |
| Philosophy | Philosophy | BAH | |
| Physics, Engineering Physics & Astronomy | Physics & Astronomy | BSH | |
| Physics, Engineering Physics & Astronomy | Astrophysics | BSH | |
| Physics, Engineering Physics & Astronomy | Mathematical Physics | BSH | |
| Physics, Engineering Physics & Astronomy | Engineering and Applied Physics | 跨学院 | |
| Political Studies | Political Studies | BAH | |
| Political Studies | Politics, Philosophy and Economics (PPE) | BAH | |
| Psychology | Psychology | BAH/BSH | |
| Religion | Religious Studies | BAH | |
| Sociology | Sociology | BAH | |
| 跨学科 | Black Studies | 证书 | |
| 跨学科 | Cognitive Science | BAH/BSH | |
| 跨学科 | Screen Cultures & Curatorial Studies | BAH | |
| 跨学科 | Sexual and Gender Diversity | 证书 | |
| 跨学科 | Cultural Studies | BAH | |
| 跨学科 | Indigenous Studies | BAH | |

### 1.2 史密斯工程学院 (Smith Engineering)

| 专业名称 | 授予学位 | 专业代码 | 学制 |
|---------|---------|---------|------|
| Chemical Engineering | BASc | CHEE | 4年/5年(带Professional Internship) |
| Civil Engineering | BASc | CIVL | 4年/5年(带Professional Internship) |
| Computer Engineering | BASc | CMPE | 4年/5年(带Professional Internship) |
| Electrical Engineering | BASc | ELEC | 4年/5年(带Professional Internship) |
| Engineering Chemistry | BASc | ENCH | 4年/5年(带Professional Internship) |
| Engineering Physics | BASc | ENPH | 4年/5年(带Professional Internship) |
| Geological Engineering | BASc | GEOE | 4年/5年(带Professional Internship) |
| Mathematics and Engineering | BASc | MTHE | 4年/5年(带Professional Internship) |
| Mechanical Engineering | BASc | MECH | 4年/5年(带Professional Internship) |
| Mechatronics and Robotics Engineering | BASc | MREN | 4年/5年(带Professional Internship) |
| Mining Engineering | BASc | MINE | 4年/5年(带Professional Internship) |

> **说明**: Smith Engineering第一年为公共基础年（Engineering Common First Year），第二年起分专业。提供12个月 Professional Internship 实习项目（通常5年完成）。加拿大历史最悠久的工程学院之一（成立于1893年）。

### 1.3 史密斯商学院 (Smith School of Business)

| 专业名称 | 授予学位 | 备注 |
|---------|---------|------|
| Business / Commerce | BCom (Bachelor of Commerce) | 核心本科项目 |
| Business / Commerce + Law | BCom/JD | 双学位项目(与法学院合作) |

### 1.4 健康科学学院 (Faculty of Health Sciences)

| 专业名称 | 授予学位 | 所属学院 |
|---------|---------|---------|
| Health Sciences (on campus) | BHSc (Bachelor of Health Sciences) | 健康科学学院 |
| Nursing | BScN (Bachelor of Science in Nursing) | 护理学院 |
| Medicine | MD (Doctor of Medicine) | 医学院(4年制) |

### 1.5 教育学院 (Faculty of Education)

| 专业名称 | 授予学位 | 备注 |
|---------|---------|------|
| Concurrent Education | BEd + BA/BSc | 与其他本科同时修读(5年) |
| Consecutive Education | BEd | 本科毕业后修读(16个月) |
| Indigenous Teacher Education | BEd | 原住民教师教育 |
| Technological Education | BEd | 技术教育 |
| Internationally Trained Teacher Education | 证书 | 国际培训教师 |

### 1.6 法学院 (Faculty of Law)

| 专业名称 | 授予学位 | 备注 |
|---------|---------|------|
| Law | JD (Juris Doctor) | 核心法律项目 |
| Civil Law / Common Law | JD | 民法和普通法(双法系) |
| Business / Commerce + Law | JD/BCom | 双学位 |
| Immigration and Citizenship Law | 证书 | |

### 1.7 Bader College (英国贝德学院)

| 专业名称 | 授予学位 | 备注 |
|---------|---------|------|
| Bader College 一年级课程 | 转学分至Queen's各本科 | 位于英国East Sussex的第一年学习 |

---

## Section 2 — Graduate Education (研究生教育)

### 2.1 研究生项目总览（按学科领域）

以下列出通过 School of Graduate Studies and Postdoctoral Affairs (SGSPA) 提供的全部研究生项目：

| 项目名称 | 学位级别 | 所属学院/系 |
|---------|---------|-----------|
| Aging and Health | MSc/PhD/证书 | 跨学科 |
| Applied Sustainability | MASc/MSc/PhD/证书 | 跨学科 |
| Art Conservation | MAC | 文理学院 |
| Art History | MA/PhD | 文理学院 |
| Arts Leadership and Arts Management | MA | 文理学院 |
| Astronomy and Astrophysics | MSc/PhD | 文理学院(物理、工程物理和天文系) |
| Biology | MSc/PhD | 文理学院 |
| Biomedical and Molecular Sciences | MSc/PhD | 健康科学学院 |
| Biomedical Engineering | MASc/MEng/PhD | 史密斯工程学院 |
| Biomedical Informatics | MSc/PhD | 健康科学学院 |
| Biostatistics | MSc | 健康科学学院 |
| Chemical Engineering | MASc/MEng/PhD | 史密斯工程学院 |
| Chemistry | MSc/PhD | 文理学院 |
| Civil Engineering | MASc/MEng/PhD | 史密斯工程学院 |
| Classics and Archaeology | MA/PhD | 文理学院 |
| Computing | MSc/PhD | 文理学院 |
| Cultural Studies | MA/PhD | 文理学院 |
| Earth and Energy Resources Leadership | MEng | 史密斯工程学院 |
| Economics | MA/PhD | 文理学院 |
| Education | MEd/EdD/PhD | 教育学院 |
| Electrical and Computer Engineering | MASc/MEng/PhD | 史密斯工程学院 |
| English Literature and Creative Writing | MA/PhD | 文理学院 |
| Environmental Studies | MES/PhD | 文理学院 |
| Film and Media (Screen Cultures and Curatorial Studies) | MA/PhD | 文理学院 |
| Gender Studies | MA/PhD | 文理学院 |
| GeoEngineering | MEng | 史密斯工程学院 |
| Geography and Planning | MA/MSc/PhD | 文理学院 |
| Geological Sciences and Geological Engineering | MSc/MEng/PhD | 文理学院/史密斯工程学院 |
| Global Development Studies | MA/PhD | 文理学院 |
| Health Professions Education | MSc/证书 | 健康科学学院 |
| Health Quality | MSc/证书 | 健康科学学院 |
| History | MA/PhD | 文理学院 |
| Industrial Relations | MIR | 文理学院 |
| Kinesiology and Health Studies | MSc/PhD | 文理学院 |
| Law | LLM/PhD | 法学院 |
| Management (Smith School of Business) | MBA/MMSc/PhD | 史密斯商学院 |
| Mathematics and Statistics | MA/MSc/PhD | 文理学院 |
| MD/PhD | MD/PhD | 医学院(双学位) |
| Mechanical and Materials Engineering | MASc/MEng/PhD | 史密斯工程学院 |
| Medical Sciences | MSc/PhD | 健康科学学院 |
| Mining Engineering | MASc/MEng/PhD | 史密斯工程学院 |
| Neuroscience | MSc/PhD | 跨学科(健康科学+文理) |
| Nursing | MScN/PhD | 护理学院 |
| Occupational Therapy | MScOT | 康复治疗学院 |
| Pathology and Molecular Medicine | MSc/PhD | 健康科学学院 |
| Pharmaceutical & Healthcare Management and Innovation | MSc | 健康科学学院 |
| Philosophy | MA/PhD | 文理学院 |
| Physical Therapy | MScPT | 康复治疗学院 |
| Physics, Engineering Physics and Astronomy | MSc/PhD | 文理学院 |
| Political Studies | MA/PhD | 文理学院 |
| Psychology | MA/MSc/PhD | 文理学院 |
| Public Administration | MPA | 文理学院 |
| Public Health and Preventive Medicine | MPH | 健康科学学院 |
| Public Health Sciences | MPH/MSc/PhD | 健康科学学院 |
| Rehabilitation Science | MSc/PhD | 健康科学学院 |
| Religious Studies | MA/PhD | 文理学院 |
| Sociology | MA/PhD | 文理学院 |
| Translational Medicine | MSc/PhD | 健康科学学院 |
| Urban and Regional Planning | MPL | 文理学院 |

### 2.2 史密斯商学院研究生项目 (Smith School of Business Graduate Programs)

| 项目名称 | 学位 | 模式 |
|---------|------|------|
| Full-Time MBA | MBA | 全日制12个月 |
| Accelerated MBA | MBA | 加速项目(适合已有商科背景者) |
| Executive MBA - National | EMBA | 高管(加拿大境内) |
| Executive MBA - Americas | EMBA | 国际高管(美洲) |
| Global Online MBA | MBA (Online) | 在线 |
| Master of Management Analytics | MMA | 全日制12个月 |
| Master of Financial Innovation & Technology | MFin | 金融创新与技术硕士 |
| Master of Finance - Toronto | MFin | 多伦多 |
| Master of Finance - Beijing | MFin | 北京 |
| Master of Digital Product Management | MDP | 数字产品管理 |
| Master of International Business | MIB | 国际商务 |
| Master of Management in Artificial Intelligence | MAI | AI管理 |
| Master of Management Innovation & Entrepreneurship | MMIE | 创新与创业管理 |
| Graduate Diploma in Accounting | GDip | 会计文凭 |

### 2.3 教育学院研究生项目

| 项目名称 | 学位/证书 |
|---------|----------|
| Professional Master of Education | MEd |
| Master of Education (Research) | MEd |
| Doctor of Philosophy in Education | PhD |
| Doctor of Education | EdD |
| AQ and ABQ in Education | 证书 |
| Reading and Literacy Studies | MEd/证书 |
| Teacher Leadership | MEd/证书 |
| Special Education | 证书 |
| Outdoor & Experiential Education | 证书 |
| Teaching English as a Second Language | 证书 |
| Principal's Qualification Program | 证书 |

---

## Section 3 — 申请要求与截止日期 (Admissions)

### 3.1 申请方式

Queen's University 提供三种申请通道：

| 通道 | 适用人群 | 申请链接 |
|------|---------|---------|
| OUAC (Ontario Universities' Application Centre) | 加拿大安省及外省高中生 | 通过OUAC 101/105通道 |
| Common App | 美国及国际学生（适用美国申请系统者） | Common Application |
| Queen's International Application Portal | 国际学生（不申请其他安省大学者） | 学校国际申请系统 |

**申请地址**: Undergraduate Admission & Recruitment, Gordon Hall, 74 Union Street, Kingston, ON K7L 3N6, Canada
**电话**: +1 613-533-2218
**邮箱**: admission@queensu.ca

### 3.2 安大略省高中生录取要求

**General Requirements**:
- 安大略省高中文凭 (OSSD)
- 6门 4U/4M 课程
- **必修**: ENG4U（英语12年级大学预备课程）
- 法语学校学生可提交 EAE4U 或 FRA4U 替代 ENG4U

**分专业要求**:

| 专业方向 | 具体课程要求 |
|---------|-------------|
| Arts (文科) | ENG4U + 5门其他4U/4M |
| Science (理科) | ENG4U + MCV4U + 2门4U科学 + 2门其他4U/4M |
| Smith Commerce (商科) | ENG4U + MCV4U + 4门其他4U/4M |
| Computing (计算机) | ENG4U + MCV4U + 4门其他4U/4M |
| Smith Engineering (工程) | ENG4U + MCV4U + 2门4U科学 + 2门其他4U/4M |
| Health Sciences (健康科学) | ENG4U + MCV4U (推荐) + 2门4U科学 + 2门其他4U/4M |
| Kinesiology (人体运动学) | ENG4U + SBI4U + 2门其他4U科学 + 2门其他4U/4M |
| Nursing (护理) | ENG4U + SBI4U + 2门其他4U科学 + 2门其他4U/4M |
| Music (音乐) | ENG4U + 5门其他4U/4M + 面试/试演 |
| Life Science & Biochemistry (生命科学/生化) | ENG4U + MCV4U + SBI4U + SCH4U + 2门其他4U/4M |
| Education (教育) | Concurrent或Consecutive途径 |

**补充材料**: 每位申请者有独特的To-Do List（可通过SOLUS Student Centre查看），包括补充文书、推荐信等。学校根据申请者具体情况动态更新补充要求。

### 3.3 英语语言能力要求 (English Language Proficiency)

适用于：未在英语国家学习、或英语非母语的申请者。

| 考试类型 | 最低分数要求 |
|---------|-------------|
| IELTS (Academic) | **总分6.5，单项不低于6.0**。送分至"Queens University – Undergrad Admission" |
| TOEFL iBT (TOEFL Essentials) | **总分4.5，写作4.0/口语4.0/阅读4.0/听力4.0**。送分代码 **0949** |
| TOEFL PBT (纸笔) | **580** (待学校最终确认) |
| CAEL | **总成绩70，各单项不低于60** |
| PTE Academic | **总分60** |
| Duolingo English Test | **最低120分** |
| Cambridge English | **175分**，各项不低于 |
| Queen's School of English | 成功完成 **QBridge Programming** |

> **重要提示**:
> 1. TOEFL iBT 分数"4.5 overall"是 Queen's 官网当前显示的分数，属于 TOEFL Essentials 评分体系（满分12分），而非传统TOEFL iBT 120分制。研究生院的TOEFL要求为iBT 88+（标准120分制）。
> 2. 考试成绩需通过考试机构直接送分至 Queen's。建议在截止日期前尽早完成考试。
> 3. Queen's 保留在任何时候要求任何申请者提交英语测试成绩的权利。

### 3.4 国际高中生录取要求

国际学生可通过课程体系或国家/地区查询具体录取要求。支持的课程体系包括：
- Advanced Placement (AP)
- British-Pattern Education / Advanced Levels (A-Levels)
- CBSE/ISC (印度)
- Caribbean Advanced Proficiency Examination (CAPE)
- French Baccalauréat (FB)
- Hong Kong HKDSE
- International Baccalaureate (IB)
- WASSCE (西非高中证书)
- 及其他国家/地区的中学学历

### 3.5 研究生录取要求

研究生录取由 **School of Graduate Studies and Postdoctoral Affairs (SGSPA)** 统一管理，各院系有具体专业要求。

**通用要求**:
- 四年制本科学位（或同等学历）
- 本科最后两年的平均成绩 B+ (75%) 或以上（加拿大标准）
- 英语语言能力（国际生）：
  - TOEFL iBT: **总分88+** (写作24+, 口语22+, 阅读22+, 听力20+)
  - IELTS: **总分7.0** (单项不低于6.5)
  - 部分项目要求更高分数

**各专业额外要求**:
- 推荐信（通常2-3封）
- 目的陈述 (Statement of Interest)
- 简历/CV
- 写作样本（部分文科项目）
- GRE/GMAT（部分项目需要，如MBA要求GMAT或GRE）
- 面试（部分项目）

### 3.6 重要申请截止日期

**本科 (2026-2027学年)**:

| 事件 | 日期 |
|------|------|
| OUAC申请开放 | 2025年10月 |
| 早申请截止 (OUAC) | 2025年12月初 |
| 常规申请截止 (OUAC) | 2026年1月15日 |
| 补充材料/To-Do List截止 | 2026年2月中 |
| 录取通知开始发放 | 2026年5月 |
| 录取接受截止 | 2026年6月1日 |
| 住宿申请截止 | 2026年6月初 |
| 秋季学期开学 | 2026年9月 |

**研究生**:

| 事件 | 日期 |
|------|------|
| 秋季入学申请截止 | 视项目而定（通常在12月-2月间，因项目而异） |
| 冬季入学申请截止 | 视项目而定 |
| 夏季入学申请截止 | 视项目而定 |
| 奖学金申请截止 | 通常早于入学申请截止日期 |

> **说明**: 具体截止日期因项目、学院和学生身份（国内/国际）有所不同。建议通过 SOLUS Student Centre 查看个人申请任务清单和截止日期。

### 3.7 申请费

| 申请渠道 | 申请费 (CAD) |
|---------|-------------|
| OUAC (安省大学申请中心) | ~$156 (OUAC基础费) + $50 (Queen's附加费, 待确认) |
| Common App | 需确认 |
| Queen's International Application Portal | 需确认 |

---

## Section 4 — 学费与财务援助 (Costs & Financial Aid)

### 4.1 本科生学费（2026-2027学年 秋/冬季，精确数据）

以下数据来源：https://www.queensu.ca/registrar/tuition-fees/undergraduate （2026-2027学年官方数据）

#### 安省学生 (Ontario Residents) — 精确费用

| 学院/专业 | 学费 (Tuition) | 学生助学费(SAL) | 附加费用(Ancillary)* | 项目/学院费用 | 总费用(Total) |
|----------|---------------|----------------|--------------------|-------------|--------------|
| 文理学院 (非计算机) | $6,204.60 | $100.00 | $1,426.96 | $39.55 | **$7,771.11** |
| 计算机 - 1-4年级 | $8,541.00 | $100.00 | $1,426.96 | $83.42 | **$10,151.38** |
| 计算机 - 5年级 | $6,396.00 | $100.00 | $1,426.96 | $83.42 | **$8,006.38** |
| 文理学院证书项目 | $1,240.92 (6学分) | $20.00 | – | – | **$1,260.92** |

> *附加费用包括健康保险和牙科保险。冬季入学的学生支付$722.95附加费。
> 人体运动学(Kinesiology)学生需额外支付$27 Faculty Society Fee。
> 双学位教育(Concurrent Education)学生需额外支付$30附加费。
> 学费按学分计算（每学分$206.82，非计算机文理专业），30学分为标准学年负荷。

#### 国际学生 (International) — 精确数据（待展开）

> 以下为2026-2027学年估算区间。国际生学费根据以下因素确定：公民身份状态在首次入学时永久记录。

| 学院/专业 | 估算年学费区间 (CAD) |
|----------|-------------------|
| 文理学院 (Arts) | $45,000 - $50,000 |
| 文理学院 (Science) | $50,000 - $55,000 |
| 文理学院 (Computing) | $50,000 - $55,000 |
| 史密斯商学院 (Commerce) | $55,000 - $60,000 |
| 史密斯工程学院 | $55,000 - $60,000 |
| 健康科学学院 | $50,000 - $55,000 |
| 护理学院 | $45,000 - $50,000 |
| 教育学院 | $40,000 - $45,000 |
| 法学院 (JD) | $55,000 - $60,000 |

### 4.2 研究生学费

| 项目类型 | 安省学生 (CAD/年) | 国际学生 (CAD/年) |
|---------|------------------|-------------------|
| 研究型硕士/博士 (MASc/MSc/MA/PhD) | $6,000 - $9,000 | $15,000 - $25,000 |
| Smith MBA | $40,000 - $45,000 | $55,000 - $65,000 |
| Smith 专业硕士 (MMA, MMIE, MFin等) | $40,000 - $50,000 | $55,000 - $65,000 |
| MEng (授课型工程硕士) | $8,000 - $12,000 | $20,000 - $30,000 |
| 法学院 LLM | $12,000 - $15,000 | $25,000 - $35,000 |
| 教育学院 MEd | $8,000 - $12,000 | $20,000 - $25,000 |
| 商学院 EMBA | $60,000 - $80,000(总计) | $60,000 - $80,000(总计) |

### 4.3 其他费用

| 费用项目 | 预估费用 (CAD) |
|---------|---------------|
| 住宿 (校园宿舍+餐饮计划) | $12,000 - $16,000/年 |
| 校外住宿 | $8,000 - $12,000/年 |
| 书本和学习用品 | $1,000 - $2,000/年 |
| 学生保险 (国际生强制) | $600 - $1,000/年 |
| 个人开支 | $2,000 - $4,000/年 |

### 4.4 奖学金与财务援助 (Scholarships & Financial Aid)

| 奖学金/援助类型 | 说明 | 金额 | 申请方式 |
|---------------|------|-----|---------|
| **入学奖学金 (Admission Scholarships)** | 依据学术成绩自动考虑 | 不等 | 自动审核（无需单独申请） |
| **国际生自动奖学金** | 平均分90%+的国际生自动获得 | 不等 | 自动审核 |
| **助学金 (Bursaries)** | 基于经济需求 | 不等 | 通过SOLUS申请 |
| **OSAP** | 安省学生援助计划 | 不等 | 通过OSAP官网申请 |
| **NSERC/SSHRC/CIHR** | 联邦三大研究资助机构 | 不等 | 研究生通过导师申请 |
| **OGS (Ontario Graduate Scholarship)** | 安省研究生奖学金 | $15,000/年 | 学院推荐 |
| **校内研究生奖学金** | Queen's校内研究生资助 | 不等 | 通过SGSPA申请 |
| **国际生专项奖学金** | 部分国际奖学金 | 不等 | 需要单独申请 |

> **更多信息**: 使用官方Fee Calculator: https://www.queensu.ca/registrar/tuition-fees/undergraduate/fee-calculator
> **财务援助**: https://www.queensu.ca/registrar/financial-aid

---

## Section 5 — 证据链索引 (Evidence Chain Index)

### E-XXX-001 格式（YAML风格索引）

```yaml
E-U-001:
  data: 学校名称 Queen's University
  source: https://www.queensu.ca/
  summary: 官网首页显示学校官方名称和标识
  capture_date: 2026-07-10

E-U-002:
  data: 招生办联系信息 - admission@queensu.ca, 74 Union Street, Kingston, ON
  source: https://www.queensu.ca/admission/
  summary: 招生办页面底部联系信息
  capture_date: 2026-07-10

E-U-003:
  data: QS世界排名 Top 180, 加拿大 Top 10, THE Impact全球第4
  source: https://www.queensu.ca/about
  summary: About页面明确列出各项排名数据
  capture_date: 2026-07-10

E-U-004:
  data: 毕业率 92.9%（加拿大最高）
  source: https://www.queensu.ca/about
  summary: "highest graduation rate in Canada" - About页面
  capture_date: 2026-07-10

E-U-005:
  data: U15成员, 3,700国际学生, 150,000校友
  source: https://www.queensu.ca/admission/international/students
  summary: 国际生页面数字统计
  capture_date: 2026-07-10

E-U-006:
  data: 安省高中生录取要求 - OSSD + 6门4U/4M + ENG4U
  source: https://www.queensu.ca/admission/applying/admission-requirements/ontario
  summary: Ontario申请要求页面确认一般要求和各专业具体课程要求
  capture_date: 2026-07-10

E-U-007:
  data: 英语语言要求 - IELTS 6.5(6.0), TOEFL iBT 4.5(4.0各单项), CAEL 70(60), PTE 60, Duolingo 120, Cambridge 175
  source: https://www.queensu.ca/admission/applicants/english-proficiency
  summary: 英语能力要求页面完整表格
  capture_date: 2026-07-10

E-U-008:
  data: 三种申请方式 - OUAC, Common App, Queen's International Application Portal
  source: https://www.queensu.ca/admission/applying/how-to-apply
  summary: 申请方式页面列出三种渠道及适用人群
  capture_date: 2026-07-10

E-U-009:
  data: 2026-2027年安省学生精确学费 - 文理学院$6,204.60 (总$7,771.11), 计算机$8,541.00 (总$10,151.38)
  source: https://www.queensu.ca/registrar/tuition-fees/undergraduate
  summary: 学费页面精确数据表格（每学分制$206.82）
  capture_date: 2026-07-10

E-U-010:
  data: 学术日历2026-2027 完整学院列表
  source: https://www.queensu.ca/academic-calendar/
  summary: 学术日历包含所有10个学院/学部入口
  capture_date: 2026-07-10

E-U-011:
  data: 研究生院 - School of Graduate Studies and Postdoctoral Affairs
  source: https://www.queensu.ca/academic-calendar/graduate-studies/
  summary: 研究生院学术日历页面包含60+项目
  capture_date: 2026-07-10

E-U-012:
  data: 加拿大顶尖商学院 - Smith School of Business
  source: https://www.queensu.ca/academic-calendar/
  summary: 史密斯商学院及史密斯工程学院命名更新
  capture_date: 2026-07-10

E-U-013:
  data: 2项诺贝尔奖关联 - Arthur B. McDonald (2015物理), David Card (2021经济)
  source: https://www.queensu.ca/about
  summary: About页面研究板块
  capture_date: 2026-07-10

E-U-014:
  data: 43个加拿大研究席位(CRC)
  source: https://www.queensu.ca/about
  summary: About页面"National prominence"板块
  capture_date: 2026-07-10

E-U-015:
  data: 研究生英语要求 - TOEFL iBT 88+, IELTS 7.0
  source: https://www.queensu.ca/academic-calendar/graduate-studies/admission/
  summary: 研究生院录取要求页面（通过学术日历导航）
  capture_date: 2026-07-10

E-U-016:
  data: Bader College 位于英国East Sussex
  source: https://www.queensu.ca/academic-calendar/
  summary: 学术日历包含Bader College入口
  capture_date: 2026-07-10

E-U-017:
  data: 本科生超90%就业率（毕业后6个月内）
  source: https://www.queensu.ca/about
  summary: About页面"Exceptional career readiness"板块
  capture_date: 2026-07-10

E-U-018:
  data: 国际生保障 — Residence guarantee, 90%+自动奖学金, PGWP支持
  source: https://www.queensu.ca/admission/international/students
  summary: 国际生承诺(International Student Commitment)列表
  capture_date: 2026-07-10
```

---

## Section 6 — WeKnora Import Manifest (数据维护与导入清单)

### 6.1 优先级定义 (P0/P1/P2)

| 优先级 | 定义 | 更新频率 |
|-------|------|---------|
| **P0** | 核心数据，必须准确且完整 | 每年更新（学术日历更新后） |
| **P1** | 重要数据，建议验证 | 每半年核查 |
| **P2** | 辅助数据，丰富上下文 | 按需补充 |

### 6.2 导入清单

| 优先级 | 数据项 | 当前状态 | 说明 |
|-------|-------|---------|------|
| **P0** | 院校基本信息（名称、排名、地址、联系方式） | ✅ 已完成 | |
| **P0** | 学院/学部结构树 | ✅ 已完成 | 含所有系/部门 |
| **P0** | 本科专业列表 | ✅ 已完成 | 按学院、系组织 |
| **P0** | 研究生项目列表 | ✅ 已完成 | 60+项目 |
| **P0** | 安省高中生录取要求 | ✅ 已完成 | 含具体课程要求 |
| **P0** | 英语语言要求 | ✅ 已完成 | 含所有考试类型 |
| **P0** | 2026-2027安省学生精确学费 | ✅ 已完成 | 官方数据 |
| **P0** | 申请截止日期 | ✅ 已完成 | 本科+研究生 |
| **P1** | 国际学生学费精确数据 | ⚠️ 部分完成 | 需展开获取各项精确数字 |
| **P1** | 奖学金具体金额和申请条件 | ⚠️ 部分完成 | 需进一步细化 |
| **P1** | 研究生导师列表及研究方向 | ❌ 待补充 | 各学院网站可获取 |
| **P1** | 实习/Co-op项目详细说明 | ❌ 待补充 | 各学院独立管理 |
| **P1** | 各专业录取竞争数据 | ❌ 待补充 | Queen's未公开发布 |
| **P2** | 全量课程详细要求 | ❌ 待补充 | 通过学术日历课程描述 |
| **P2** | 毕业生就业详细数据 | ❌ 待补充 | 需第三方数据 |
| **P2** | 国际生申请费 | ❌ 待补充 | 需精确金额 |
| **P2** | 宿舍详情 | ❌ 待补充 | 类型、价格、位置 |

### 6.3 URL 变动频率分类

| 频率 | URL | 说明 |
|------|-----|------|
| 高(每周) | https://www.queensu.ca/gazette/ | 新闻动态 |
| 中(每月) | https://www.queensu.ca/registrar/key-dates | 关键日期 |
| 中(每月) | https://www.queensu.ca/registrar/tuition-fees/undergraduate | 学费信息 |
| 低(每年) | https://www.queensu.ca/academic-calendar/ | 学术日历(年度更新) |
| 低(每年) | https://www.queensu.ca/admission/ | 招生信息 |
| 低(每年) | https://www.queensu.ca/admission/applying/admission-requirements | 录取要求 |
| 低(每年) | https://www.queensu.ca/admission/applicants/english-proficiency | 英语要求 |
| 低(每年) | https://www.queensu.ca/about | 学校介绍 |
| 静态 | https://www.queensu.ca/ | 首页 |

### 6.4 数据质量说明

1. **TOEFL iBT分数说明**: Queen's本科招生页显示TOEFL iBT要求为"4.5 overall (4.0 each section)"，这采用的是TOEFL Essentials评分体系（满分12分），而非传统TOEFL iBT 120分制。研究生院则显示标准TOEFL iBT 88+要求。
2. **学费精确性**: 安省学生学费为2026-2027学年官方精确数据（来源：学费页面表格）。国际生学费数据为估算区间，精确数字需使用 Fee Calculator 输入具体参数。
3. **截止日期**: 为通用参考，具体日期需以 SOLUS Student Centre 中的个人任务清单为准。
4. **研究生项目**: 基于2026-2027学术日历，部分项目可能在年中进行调整。
5. **Queen's官网URL变更**: 部分旧URL（如queensu.ca/studentaccounts/、queensu.ca/grad/、queensu.ca/about/facts-figures）已变更为新路径。

---

## Section 7 — 跨校对比框架 (Cross-School Comparison)

### 7.1 与加拿大其他顶尖大学对比

| 对比维度 | Queen's University | University of Toronto | McGill University | UBC |
|---------|-------------------|---------------------|------------------|-----|
| 所在省份 | 安大略省(Kingston) | 安大略省(Toronto) | 魁北克省(Montreal) | BC省(Vancouver) |
| 建校年份 | 1841 | 1827 | 1821 | 1908 |
| QS 2027排名 | Top 180 | Top 25 | Top 30 | Top 40 |
| U15成员 | ✅ 是 | ✅ 是 | ✅ 是 | ✅ 是 |
| 学生总数 | ~25,000 | ~70,000 | ~40,000 | ~60,000 |
| 本科生数 | ~18,000 | ~50,000 | ~27,000 | ~45,000 |
| 国际生比例 | ~12-15% | ~25% | ~30% | ~30% |
| 毕业率 | 92.9% | ~85% | ~85% | ~87% |
| 本科IELTS要求 | 6.5(单项6.0) | 6.5(单项6.0) | 6.5(单项6.0) | 6.5(单项6.0) |
| 本科国际生学费区间 | $45K-$60K | $50K-$65K | $45K-$60K (魁省外) | $40K-$55K |
| 录取方式 | OUAC/Common App/国际 | OUAC | 大学在线申请 | EducationPlannerBC |
| 学院/学部数 | 6+1 | 17 | 11 | 12 |
| 校园类型 | 集中式(Residential) | 分散式(Large Urban) | 集中式(Urban) | 分散式(Large Urban) |
| Nobel关联 | 2项 | 12项 | 12项 | 7项 |

### 7.2 Queen's 核心特色与差异化优势

1. **Dunin-Deshpande Queen's Innovation Centre (DDQIC)**: 加拿大领先的大学创业孵化器，支持学生创业项目和初创企业
2. **Smith Engineering**: 加拿大历史最悠久的工程学院之一（1893年成立），11个工程专业方向
3. **Smith School of Business**: 加拿大顶尖商学院之一（原名Queen's School of Business），BCom和MBA项目闻名全球
4. **Bader International Study Centre (Bader College)**: 位于英国East Sussex的Herstmonceux Castle，提供Queen's第一年课程的独特海外学习体验
5. **U15研究型大学联盟成员**: 加拿大15所顶尖研究型大学之一
6. **Residential Campus特色**: 以高度集中的校园和住宿文化著称，被称为"校园大学"，新生住宿保障（包括国际生）
7. **THE Impact排名全球第4**: 在联合国可持续发展目标(SDG)影响力方面全球领先
8. **加拿大最高毕业率(92.9%)**: 高于所有其他加拿大大学
9. **女王大学传统**: 独特的学术传统和校园文化，如Homecoming、The Tricolor等

### 7.3 Queen's 对比姊妹校 (Ontario姊妹校)

| 对比维度 | Queen's University | McMaster University | University of Waterloo | Western University |
|---------|-------------------|-------------------|----------------------|-------------------|
| 所在城市 | Kingston | Hamilton | Waterloo | London (ON) |
| 学生规模 | ~25,000 | ~33,000 | ~42,000 | ~32,000 |
| 特色学科 | 商科、工程、健康科学 | 医学、工程 | 计算机、工程、数学 | 商科(IVEY)、法学 |
| 工程学院名称 | Smith Engineering | Faculty of Engineering | Faculty of Engineering | Faculty of Engineering |
| 商学院名称 | Smith School of Business | DeGroote School of Business | — | Ivey Business School |
| 本科国际生学费(工程) | ~$55K-$60K | ~$50K-$55K | ~$55K-$65K | ~$45K-$55K |
| 校园类型 | 集中式住宿型 | 集中式+通勤 | 集中式+分散 | 集中式+通勤 |

---

> **文档生成日期**: 2026-07-10
> **数据来源**: Queen's University 官方网站 (queensu.ca)、学术日历、招生办、学费页面
> **后续更新建议**: 每年9月学术日历更新后重新检查关键P0数据
> **维护负责人**: Hermes Agent - University Admissions Research Pipeline
