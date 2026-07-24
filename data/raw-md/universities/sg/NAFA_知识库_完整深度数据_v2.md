# NAFA (Nanyang Academy of Fine Arts) 知识库_完整深度数据_v2.md

> **Data capture date**: 2026-07-09
> **Capture tool**: curl + Python extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Singapore (SG)
> **Institution type**: Private arts academy (publicly-funded, MOE-subsidised)
> **Part of**: University of the Arts Singapore (UAS) — founding member

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 基础年课程 (Foundation) | 1 |
| 文凭课程 (Diploma) | 15 |
| 本科学位专业 (UG Degree Programmes) | 6 (unique) * |
| 研究生授课型项目 (PGT: Master's) | 3 |
| 研究生博士项目 (PhD/Doctoral) | 0 |
| 证书课程 (Certificate) | 1 (类别) |
| **学术项目总计** | **26** |
| 学院 (Faculties) | 3 |
| 学术院系 (Schools) | 11 |
| 联培大学 (Partner Universities) | 3 (UAL, UAS, RCM) |

> \* BA (Hons) Design Practice 和 BA (Hons) Performance Making 由多个学院共同开设，此处计为各1个但跨学院

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Nanyang Academy of Fine Arts (NAFA)
├── Faculty of Art & Design
│   ├── School of 3D Design
│   ├── School of Design & Media
│   ├── School of Fashion Studies
│   └── School of Fine Art
├── Faculty of Performing Arts
│   ├── School of Dance
│   ├── School of Music
│   └── School of Theatre
├── Faculty of Interdisciplinary Practices
│   ├── School of Arts Management
│   ├── School of Interdisciplinary Arts
│   ├── Centre for Lifelong Education
│   └── School of Young Talents
└── Non-faculty units
    ├── NAFA Arts Preschool (under School of Young Talents)
    └── NAFA Foundation Programme (cross-faculty)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位级别 | 缩写 | 数量 |
|----------|------|------|
| Foundation Programme | NFP | 1 |
| Diploma | Dip | 15 |
| Bachelor of Arts (Honours) | BA (Hons) | 5 |
| Bachelor of Education (Honours) | BEd (Hons) | 1 |
| Bachelor of Music (Honours) | BMus (Hons) | 1 |
| Master of Fine Arts | MFA | 1 |
| Master of Composition | MComp | 1 |
| Master of Performance | MPerf | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 / 系 | Foundation | Diploma | BA (Hons) | BEd (Hons) | BMus (Hons) | MFA | MComp | MPerf | 小计 |
|-----------|-----------|---------|-----------|------------|-------------|-----|-------|-------|------|
| **Faculty of Art & Design** | | | | | | | | | |
| School of 3D Design | — | 3 | 2 | — | — | — | — | — | 5 |
| School of Design & Media | — | 3 | 1* | — | — | — | — | — | 4 |
| School of Fashion Studies | — | 1 | 1* | — | — | — | — | — | 2 |
| School of Fine Art | — | 2 | 1 | — | — | 1 | — | — | 4 |
| **Faculty of Performing Arts** | | | | | | | | | |
| School of Dance | — | 1 | 1* | — | — | — | — | — | 2 |
| School of Music | — | 2 | — | 1 | 1 | — | 1 | 1 | 6 |
| School of Theatre | — | 2 | 2 | — | — | — | — | — | 4 |
| **Faculty of Interdisciplinary Practices** | | | | | | | | | |
| School of Arts Management | — | 1 | 1* | — | — | — | — | — | 2 |
| School of Interdisciplinary Arts | — | — | 2* | — | — | — | — | — | 2 |
| Centre for Lifelong Education | — | — | — | — | — | — | — | — | — |
| School of Young Talents | — | — | — | — | — | — | — | — | — |
| **Cross-faculty** | | | | | | | | | |
| NAFA Foundation Programme | 1 | — | — | — | — | — | — | — | 1 |
| **总计** | **1** | **15** | **6** | **1** | **1** | **1** | **1** | **1** | **27** |

> \* BA (Hons) Design Practice 跨 School of 3D Design / Design & Media / Fashion Studies / Interdisciplinary Arts 开设；BA (Hons) Performance Making 跨 School of Dance / Theatre / Interdisciplinary Arts 开设。此处计入主理学院。

---

## Section 1 — Undergraduate education (本科教育)

### 1.1 Foundation Programme (基础年课程)

| 专业名称 | 学位类型 | 学院/系 | 学分 | 课程链接 |
|----------|---------|---------|------|---------|
| NAFA Foundation Programme (NFP) | Foundation | Cross-faculty | 180 credits | https://www.nafa.edu.sg/programmes/foundation |

### 1.2 Diploma Programmes (文凭课程)

#### Faculty of Art & Design

**School of 3D Design**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Design (Furniture and 3D Crafts) | Diploma | Faculty of Art & Design | School of 3D Design | https://www.nafa.edu.sg/programmes/diploma-in-design-furniture-and-3d-crafts |
| Diploma in Design (Interior and Spatial) | Diploma | Faculty of Art & Design | School of 3D Design | https://www.nafa.edu.sg/programmes/diploma-in-design-interior-and-spatial |
| Diploma in Design (Landscape and Architecture) | Diploma | Faculty of Art & Design | School of 3D Design | https://www.nafa.edu.sg/programmes/diploma-in-design-landscape-architecture |

**School of Design & Media**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Design Communication and Strategy | Diploma | Faculty of Art & Design | School of Design & Media | https://www.nafa.edu.sg/programmes/diploma-in-design-communication-and-strategy |
| Diploma in Digital Illustration and Narrative | Diploma | Faculty of Art & Design | School of Design & Media | https://www.nafa.edu.sg/programmes/diploma-in-digital-illustration-and-narrative |
| Diploma in Media Experience and Innovation | Diploma | Faculty of Art & Design | School of Design & Media | https://www.nafa.edu.sg/programmes/diploma-in-media-experience-and-innovation |

**School of Fashion Studies**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Fashion | Diploma | Faculty of Art & Design | School of Fashion Studies | https://www.nafa.edu.sg/programmes/diploma-in-fashion |

**School of Fine Art**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Fine Art | Diploma | Faculty of Art & Design | School of Fine Art | https://www.nafa.edu.sg/programmes/diploma-in-fine-art |
| Diploma in Art Teaching | Diploma | Faculty of Art & Design | School of Fine Art | https://www.nafa.edu.sg/programmes/diploma-in-art-teaching |

#### Faculty of Performing Arts

**School of Dance**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Dance | Diploma | Faculty of Performing Arts | School of Dance | https://www.nafa.edu.sg/programmes/diploma-in-dance |

**School of Music**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Music | Diploma | Faculty of Performing Arts | School of Music | https://www.nafa.edu.sg/programmes/diploma-in-music |
| Diploma in Music Teaching | Diploma | Faculty of Performing Arts | School of Music | https://www.nafa.edu.sg/programmes/diploma-in-music-teaching |

**School of Theatre**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Theatre (English Drama) | Diploma | Faculty of Performing Arts | School of Theatre | https://www.nafa.edu.sg/programmes/diploma-in-theatre-(english-drama) |
| Diploma in Theatre (Mandarin Drama) | Diploma | Faculty of Performing Arts | School of Theatre | https://www.nafa.edu.sg/programmes/diploma-in-theatre-(mandarin-drama) |

#### Faculty of Interdisciplinary Practices

**School of Arts Management**

| 专业名称 | 学位类型 | 学院 | 系 | 链接 |
|----------|---------|------|----|------|
| Diploma in Arts Management | Diploma | Faculty of Interdisciplinary Practices | School of Arts Management | https://www.nafa.edu.sg/programmes/diploma-in-arts-management |

### 1.3 Bachelor's Degree Programmes (本科学位课程)

| 专业名称 | 学位类型 | 学院 | 系 | 合作大学 | 链接 |
|----------|---------|------|----|---------|------|
| BA (Hons) Design Practice | BA (Hons) | Faculty of Art & Design | School of 3D Design / Design & Media / Fashion Studies / Interdisciplinary Arts | University of the Arts London (UAL) / University of the Arts Singapore (UAS) | https://www.nafa.edu.sg/programmes/bachelor-of-arts-honours-design-practice |
| BA (Hons) Fine Art | BA (Hons) | Faculty of Art & Design | School of Fine Art | UAL / UAS | https://www.nafa.edu.sg/programmes/bachelor-of-arts-honours-fine-art |
| BA (Hons) Biophilic Design | BA (Hons) | Faculty of Art & Design | School of 3D Design | UAL | https://www.nafa.edu.sg/programmes/bachelor-of-arts-honours-biophilic-design |
| BA (Hons) Performance Making | BA (Hons) | Faculty of Performing Arts | School of Dance / Theatre / Interdisciplinary Arts | UAL / UAS | https://www.nafa.edu.sg/programmes/bachelor-of-arts-honours-performance-making |
| BA (Hons) Contemporary Chinese Theatres | BA (Hons) | Faculty of Performing Arts | School of Theatre | UAL | https://www.nafa.edu.sg/programmes/bachelor-of-arts-honours-contemporary-chinese-theatres |
| BEd (Hons) in Instrumental & Vocal Teaching | BEd (Hons) | Faculty of Performing Arts | School of Music | UAS | https://www.nafa.edu.sg/programmes/bachelor-of-education-(honours)-in-instrumental-vocal-teaching |
| BMus (Hons) | BMus (Hons) | Faculty of Performing Arts | School of Music | Royal College of Music, London / UAS | https://www.nafa.edu.sg/programmes/bachelor-of-music-honours |

---

## Section 2 — Graduate education (研究生教育)

### 2.1 Master's Degree Programmes (授课型硕士课程)

| 专业名称 | 学位类型 | 学院 | 系 | 合作大学 | 学制 | 链接 |
|----------|---------|------|----|---------|------|------|
| Master of Fine Arts (Fine Art) | MFA | Faculty of Art & Design | School of Fine Art | University of the Arts Singapore | Full-time 2 years | https://www.nafa.edu.sg/programmes/master-of-fine-arts-fine-art |
| Master of Composition | MComp | Faculty of Performing Arts | School of Music | University of the Arts Singapore | Part-time 1.5 years | https://www.nafa.edu.sg/programmes/master-of-composition |
| Master of Performance | MPerf | Faculty of Performing Arts | School of Music | University of the Arts Singapore | Part-time 2 years | https://www.nafa.edu.sg/programmes/master-of-performance |

### 2.2 Doctoral Programmes (博士课程)

NAFA currently offers no doctoral programmes.

---

## Section 3 — Application requirements & deadlines (申请要求与截止日期)

### 3.1 Application Timeline (申请时间线)

| 项目 | 日期 |
|------|------|
| 申请开放 | 每年10月（为次年8月入学） |
| 申请截止 | 各专业不同，建议尽早申请 |
| 面试（SC/PR） | 1月底至3月底 |
| 结果公布 | 滚动通知 |
| 入学（主学期） | 8月（Academic Year 每年8月开始） |

> 来源：https://www.nafa.edu.sg/admissions/bachelors-degree-admissions

### 3.2 Foundation Programme Entry Requirements (基础年入学要求)

| 要求 | 详情 |
|------|------|
| 学术要求 | GCE O-Level 或同等学历 |
| 最低年龄 | 通常16岁以上 |
| 语言要求 | 视申请人背景评估 |
| 其他 | 作品集或试镜（视专业方向） |

> 来源：https://www.nafa.edu.sg/admissions/foundation-admissions

### 3.3 Diploma Entry Requirements (文凭课程入学要求)

| 资格类别 | 要求 |
|---------|------|
| GCE O-Level | 至少1门科目及格 |
| GCE A-Level | 至少1门H2或2门H1及格 |
| ITE | 相关NITEC/Higher NITEC证书 |
| 国际学生 | 同等学历，需经评估 |
| 其他 | Portfolio（艺术设计类）或Audition（表演艺术类） |

> 来源：https://www.nafa.edu.sg/admissions/diploma-admissions

### 3.4 Bachelor's Degree Entry Requirements (本科学位入学要求)

| 资格类别 | 要求 |
|---------|------|
| GCE A-Level | 通常2门H2 + 1门H1及格 |
| NAFA Diploma | 相关文凭，GPA达标 |
| 理工学院 Diploma | 相关文凭，GPA达标 |
| IB Diploma | 完成IB文凭课程 |
| 国际学生 | 同等学历评估 |
| **语言要求** | |
| IELTS | 通常6.0（各单项不低于5.5）-6.5 |
| TOEFL (iBT) | 80以上 |
| **特殊要求** | |
| 作品集 (Portfolio) | 设计/艺术类专业必需 |
| 试镜 (Audition) | 音乐/舞蹈/戏剧专业必需 |
| 面试 (Interview) | 部分专业需要 |

> 来源：https://www.nafa.edu.sg/admissions/bachelors-degree-admissions
> 各学院具体入学要求见：
> - Faculty of Art & Design: https://www.nafa.edu.sg/admissions/bachelors-degree-admissions/faculty-of-art-design
> - Faculty of Performing Arts: https://www.nafa.edu.sg/admissions/bachelors-degree-admissions/faculty-of-performing-arts
> - Faculty of Interdisciplinary Practices: https://www.nafa.edu.sg/admissions/bachelors-degree-admissions/faculty-of-interdisciplinary-practices

### 3.5 Master's Degree Entry Requirements (硕士学位入学要求)

| 要求 | 详情 |
|------|------|
| 学历要求 | 相关领域学士学位（荣誉学位优先） |
| 工作经验 | 部分专业优先考虑有工作经验者 |
| IELTS | 通常6.5-7.0 |
| TOEFL (iBT) | 90以上 |
| 作品集 | MFA需要作品集 |
| 面试 | 所有硕士项目需要面试 |
| 试镜 | 表演类硕士项目需要 |

> 来源：https://www.nafa.edu.sg/admissions/master-degree-admissions

---

## Section 4 — Costs & financial aid (费用与财务援助)

### 4.1 Application Fees (申请费)

| 身份 | 费用 |
|------|------|
| Singapore Citizens & PR | S$75.00 |
| International Students (Foundation/Diploma/Degree) | S$120.00 |
| International Students (Master's) | S$105.00 |

> 来源：https://www.nafa.edu.sg/admissions/fees/degree/programme-fees

### 4.2 Foundation Programme Fees (基础年课程费用)

| 身份 | 费用（全课程，180学分） |
|------|----------------------|
| Singapore Citizens | S$370 |
| Singapore Permanent Residents | S$4,150 |
| International Students | S$9,400 |

> 来源：https://www.nafa.edu.sg/admissions/fees/foundation/programme-fees

### 4.3 Diploma Fees (文凭课程费用，每年/120学分)

**Academic Year 2026**

| 专业 | SC（<40岁）| SC（40岁+）| SPR | 国际-东盟 | 国际-非东盟 | 非补贴全额 |
|------|-----------|-----------|-----|----------|------------|----------|
| 3D Design | S$4,810 | S$3,206 | S$7,360 | S$12,300 | S$13,300 | S$24,800 |
| Design & Media | S$4,810 | S$3,206 | S$7,360 | S$12,300 | S$13,300 | S$24,800 |
| Fine Art | S$4,810 | S$3,206 | S$7,360 | S$12,300 | S$13,300 | S$24,800 |
| Fashion Studies | S$5,260 | S$3,506 | S$7,810 | S$12,300 | S$13,300 | S$24,800 |
| Arts Management | S$4,810 | S$3,206 | S$7,360 | S$12,300 | S$13,300 | S$24,800 |
| Dance | S$5,760 | S$3,840 | S$8,530 | S$13,100 | S$14,100 | S$25,500 |
| Theatre | S$5,760 | S$3,840 | S$8,530 | S$13,100 | S$14,100 | S$25,500 |
| Music | S$5,760 | S$3,840 | S$8,530 | S$13,100 | S$14,100 | S$25,500 |
| Art Teaching | S$5,970 | S$3,980 | S$8,110 | S$13,850 | S$14,600 | S$24,800 |
| Music Teaching | S$7,890 | S$5,260 | S$10,550 | S$16,950 | S$18,250 | S$25,500 |

> 注：SC及SPR的补贴学费已扣除GST补贴。国际学生学费含GST。
> 来源：https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees

### 4.4 Bachelor's Degree Fees (本科学位课程费用，每年/120学分)

**Academic Year 2026**

| 专业 | 合作大学 | SC（<40岁）| SC（40岁+）| SPR | 非补贴全额 |
|------|---------|-----------|-----------|-----|----------|
| BA (Hons) Design Practice | UAL | S$8,650 | S$3,460 | S$12,100 | S$29,800 |
| BA (Hons) Fine Art | UAL | S$8,650 | S$3,460 | S$12,100 | S$29,800 |
| BA (Hons) Biophilic Design | UAL | S$9,650 | S$3,860 | S$13,500 | S$30,800 |
| BA (Hons) Design Practice | UAS | S$8,650 | S$3,460 | S$12,100 | S$29,800 |
| BA (Hons) Performance Making | UAS | S$9,650 | S$3,860 | S$13,500 | S$30,800 |
| BA (Hons) Contemporary Chinese Theatres | UAL | S$8,650 | S$3,460 | S$12,100 | S$29,800 |
| BA (Hons) Fine Art | UAS | S$9,650 | S$3,860 | S$13,500 | S$30,800 |
| BMus (Hons) | RCM | S$10,270^ | S$4,108^ | S$14,350^ | S$32,650^ |
| BMus (Hons) | UAS & RCM | S$10,270^ | S$4,108^ | S$14,350^ | S$32,650^* |

> ^ Fees inclusive of board and lodging for 7-week residential study visit
> * BMus (Hons) students may be eligible for Emerging Artist Award of S$6,000
> 来源：https://www.nafa.edu.sg/admissions/fees/degree/programme-fees

### 4.5 Master's Fees (硕士课程费用)

| 专业 | 学制 | SC | SPR | 国际学生 |
|------|------|----|-----|---------|
| MFA Fine Art - Year 1 | Full-time 2年 | S$26,400/年 | S$27,600/年 | S$29,600/年 |
| MFA Fine Art - Year 2 | Full-time 2年 | S$13,200 | S$13,800 | S$14,800 |
| Master of Composition - Year 1 | Part-time 1.5年 | S$20,000 | S$20,800 | S$22,400 |
| Master of Performance | Part-time 2年 | S$20,000/年 (80学分) | - | - |

> 注：MFA校友/教职员可享受学费减免
> 国际学生需Full-time学习以获得学生签证
> 来源：https://www.nafa.edu.sg/admissions/fees/master/programme-fees

### 4.6 Other Compulsory Fees (其他强制性费用)

| 费用项目 | Foundation | Diploma | Degree | Master |
|---------|-----------|---------|--------|--------|
| Administrative Fee | S$250/年 | S$150/年(1-3年) / S$250/年(4年+) | S$250/年 | S$250/年 |
| Health Services Fee | S$80/年 | S$80/年 | S$80/年 | S$80/年 |

### 4.7 MOE Tuition Grant (MOE学费资助计划)

| 身份 | 资助级别 | 服务协议 |
|------|---------|---------|
| Singapore Citizen | Tier A（自动，最高资助） | 无服务要求 |
| Singapore PR | Tier B（需申请） | 毕业后在新加坡工作3年 |
| 国际学生 | Tier C（有限名额，择优） | 毕业后在新加坡工作3年 |
| 非补贴学生 | 无 | 无 |

### 4.8 Scholarship & Financial Aid (奖学金与财务援助)

| 名称 | 适用范围 | 类型 |
|------|---------|------|
| NAFA Talent Scholarship | Diploma/Degree | 奖学金 |
| NAC Arts Scholarship (Diploma) | Diploma | 奖学金 |
| NAC UAS Arts Scholarship | Degree | 奖学金 |
| Dare to Dream Scholarship | 所有级别 | 奖学金 |
| Graduate Assistantship Award | Master | 奖学金 |
| Diploma Foundation Programme Bursary | Foundation/Diploma | 助学金 |
| Higher Education Bursary | 所有级别 | 助学金 |
| Higher Education Community Bursary | 所有级别 | 助学金 |
| CPF Education Loan Scheme | 所有级别 | 贷款 |
| Higher Education Student Loan (HESL) | 所有级别 | 贷款 |
| Government Loan Schemes | 所有级别 | 贷款 |
| Post-Secondary Education Scheme | Diploma | 资助 |
| SkillsFuture Credit | SC | 资助 |
| SkillsFuture Level-Up Programme | SC（40岁+） | 资助 |
| NAFA-Kwan Im Thong Hood Cho Temple Student Relief Fund | 所有级别 | 紧急援助 |
| Student Assistantship Scheme | 所有级别 | 勤工俭学 |
| Student Notebook Subsidy Scheme | 所有级别 | 补贴 |
| Overseas Programme Travel Subsidy | 所有级别 | 旅行补贴 |
| International Placement Travel Grant | 所有级别 | 旅行补助 |

> 来源：https://www.nafa.edu.sg/admissions/scholarships-and-financial-aid-schemes

---

## Section 5 — Evidence chain index (证据链索引)

| 编号 | 字段 | 值 | 来源URL | 证据类型 | 捕获日期 |
|------|------|----|---------|---------|---------|
| E-U-001 | institution.name | Nanyang Academy of Fine Arts (NAFA) | https://www.nafa.edu.sg | official_webpage | 2026-07-09 |
| E-U-002 | institution.type | Arts academy, founding member of UAS | https://www.nafa.edu.sg/admissions | official_webpage | 2026-07-09 |
| E-U-003 | counts.foundation | 1 programme | https://www.nafa.edu.sg/programmes/foundation | official_webpage | 2026-07-09 |
| E-U-004 | counts.diploma | 15 programmes | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |
| E-U-005 | counts.bachelors | 7 programmes | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |
| E-U-006 | counts.masters | 3 programmes | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |
| E-U-007 | hierarchy.faculties | 3 faculties | https://www.nafa.edu.sg/admissions/fees/degree/programme-fees | official_webpage | 2026-07-09 |
| E-U-008 | hierarchy.schools | 11 schools | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |
| E-U-009 | fees.foundation.SC | S$370 | https://www.nafa.edu.sg/admissions/fees/foundation/programme-fees | official_webpage | 2026-07-09 |
| E-U-010 | fees.foundation.SPR | S$4,150 | https://www.nafa.edu.sg/admissions/fees/foundation/programme-fees | official_webpage | 2026-07-09 |
| E-U-011 | fees.foundation.international | S$9,400 | https://www.nafa.edu.sg/admissions/fees/foundation/programme-fees | official_webpage | 2026-07-09 |
| E-U-012 | fees.diploma.3DDesign.SC_under40 | S$4,810 | https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees | official_webpage | 2026-07-09 |
| E-U-013 | fees.diploma.music.SC_under40 | S$5,760 | https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees | official_webpage | 2026-07-09 |
| E-U-014 | fees.degree.DesignPractice_UAL.SC_under40 | S$8,650 | https://www.nafa.edu.sg/admissions/fees/degree/programme-fees | official_webpage | 2026-07-09 |
| E-U-015 | fees.degree.BMus.SC_under40 | S$10,270 | https://www.nafa.edu.sg/admissions/fees/degree/programme-fees | official_webpage | 2026-07-09 |
| E-U-016 | fees.master.MFA.SC.Y1 | S$26,400 | https://www.nafa.edu.sg/admissions/fees/master/programme-fees | official_webpage | 2026-07-09 |
| E-U-017 | application_fee.SC_PR | S$75.00 | https://www.nafa.edu.sg/admissions/fees/degree/programme-fees | official_webpage | 2026-07-09 |
| E-U-018 | application_fee.international | S$120.00 (diploma) / S$105.00 (master) | https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees | official_webpage | 2026-07-09 |
| E-U-019 | tuition_grant.SC | Tier A automatic | https://www.nafa.edu.sg/admissions/fees/degree/programme-fees | official_webpage | 2026-07-09 |
| E-U-020 | tuition_grant.SPR | Tier B with 3-year bond | https://www.nafa.edu.sg/admissions/fees/degree/programme-fees | official_webpage | 2026-07-09 |
| E-U-021 | tuition_grant.international | Tier C limited, merit-based, 3-year bond | https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees | official_webpage | 2026-07-09 |
| E-U-022 | application_timeline | Open Oct each year, Aug intake | https://www.nafa.edu.sg/admissions/bachelors-degree-admissions | official_webpage | 2026-07-09 |
| E-U-023 | entry_requirements.bachelors | GCE A-Level 2H2+1H1 or equivalent | https://www.nafa.edu.sg/admissions/bachelors-degree-admissions | official_webpage | 2026-07-09 |
| E-U-024 | english_language.IELTS | 6.0-6.5 typical | https://www.nafa.edu.sg/admissions/bachelors-degree-admissions | official_webpage | 2026-07-09 |
| E-U-025 | institution.platform | Sitefinity 14.4.8152.0 DX (ASP.NET) | https://www.nafa.edu.sg/admissions | technical_analysis | 2026-07-09 |
| E-U-026 | admin_fee.diploma | S$150/年 (1-3年) / S$250(4年+) | https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees | official_webpage | 2026-07-09 |
| E-U-027 | health_fee | S$80/年 | https://www.nafa.edu.sg/admissions/fees/diploma/programme-fees | official_webpage | 2026-07-09 |
| E-U-028 | programmes.foundation | NAFA Foundation Programme | https://www.nafa.edu.sg/programmes/foundation | official_webpage | 2026-07-09 |
| E-U-029 | programmes.diploma | 15 diploma programmes listed | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |
| E-U-030 | programmes.bachelors | 7 bachelor programmes listed | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |
| E-U-031 | programmes.masters | 3 master programmes listed | https://www.nafa.edu.sg/schools-and-programmes | official_webpage | 2026-07-09 |

---

## Section 6 — WeKnora import manifest + follow-up items

### Follow-up data items (优先级的后续数据)

| 优先级 | 数据项 | 说明 |
|--------|--------|------|
| **P0** | 完整课程详情页数据（各Diploma/Bachelor/Master的课程结构、学分要求、学制） | 当前仅提取了课程名称和学费 |
| **P0** | 详细入学语言要求（IELTS/TOEFL最低分数表） | 需从各学院入学要求页面的折叠内容中提取 |
| **P0** | 各Diploma入学面试/试镜/作品集具体要求 | 需逐项提取 |
| **P1** | IGP（Indicative Grade Profile）数据 | NAFA可能不公开IGP（不同于NUS/NTU） |
| **P1** | 各奖学金详细金额和申请条件 | 需从各奖学金子页面提取 |
| **P1** | 非全日制/短期课程（Certificate, Short Courses） | 约7门Certificate课程 |
| **P1** | 合作大学清单（Overseas Learning Experience） | 需从Global Engagement页面提取 |
| **P2** | 校园设施和服务详情 | nice-to-have |
| **P2** | 毕业就业数据（GES） | NAFA有毕业就业调查 |

---

## Section 7 — Cross-school comparison framework (跨校比较框架)

| 维度 | NAFA (Nanyang Academy of Fine Arts) | LASALLE College of the Arts | NTU (Nanyang Technological University) |
|------|--------------------------------------|----------------------------|----------------------------------------|
| 类型 | 专业艺术学院（NAFA + LASALLE → UAS） | 专业艺术学院（UAS成员） | 综合性研究型大学 |
| 学术单位 | 3 Faculties, 11 Schools | N/A | 6 Colleges, 35+ Schools |
| 总项目数 | ~27 | ~30+ | ~200+ |
| 本科项目 | 7 Bachelor + 15 Diploma | ~15 Bachelor + Diploma | ~70+ Bachelor |
| 研究生项目 | 3 Master (授课型) | ~10+ | ~100+ (授课+研究) |
| 博士项目 | 0 | 少量 | 大量 |
| 最低语言要求 | IELTS 6.0 (本科) | IELTS 6.0 (本科) | IELTS 6.0 (本科) |
| MOE补贴 | 是（通过UAS） | 是（通过UAS） | 是（直接） |
| 学制 | 8月入学，学年制 | 8月入学，学年制 | 8月入学，学年制 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: NAFA official website (nafa.edu.sg)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | Foundation ✅ | Diploma (15/15) ✅ | Bachelor (7/7) ✅ | Master (3/3) ✅ | Fees ✅ | Application requirements (partial) ⚠️ | Evidence (31 blocks) ✅
> **Next step**: P0 items — extract detailed curriculum for each programme, entry requirements from faculty-specific admissions pages, scholarship details
