# University of South Australia 知识库完整深度数据

> **Data capture date**: 2026-07-11
> **Capture tool**: browser_navigate + curl + Python (AEM text extraction) + sitemap.xml
> **Target knowledge base**: WeKnora
> **Granularity**: college → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (South Australia)

---

## ⚠️ 重要说明 — 院校合并

> **University of South Australia (UniSA)** 已于 **2026年** 与 **University of Adelaide** 合并，成立新的 **Adelaide University**（阿德莱德大学）。
>
> 原 UniSA 官网 (`www.unisa.edu.au`) 大部分页面已重定向或下线（返回 404）。所有招生数据已整合至新机构 Adelaide University。
>
> 本知识库基于 Adelaide University 官方数据整理，传统 UniSA 历史数据已在下文中标注。
>
> 新机构官网: https://adelaide.edu.au/
> QS 2027 排名: **#79** (Adelaide University, Go8成员)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科专业 (Bachelor) | 315 |
| 硕士专业 (Master) | 112 |
| 博士专业 (Doctor) | 4 |
| 研究生证书/文凭 (Graduate Certificate/Diploma) | 96 |
| 国际项目 (International) | 7 |
| 其他（预科/桥梁/职业证书等） | 41 |
| **学位项目总计** | **~575** |
| 学院 (Colleges) | 6 |
| 研究领域 (Study Areas) | 22 |

> 来源: Adelaide University sitemap.xml (2026年7月)

### 0.2 学院/系层级结构 (Rule 2 — hierarchy)

```
Adelaide University (formerly UniSA + University of Adelaide)
├── College of Business and Law
│   ├── Accounting, Commerce & Economics
│   ├── Business, Marketing & Management
│   ├── Law and Justice
│   └── Property, Construction & Real Estate
│
├── College of Creative Arts, Design and Humanities
│   ├── Arts, Humanities & Social Sciences
│   ├── Creative Media & Communication
│   ├── Music
│   └── Architecture & Design
│
├── College of Education, Behavioural and Social Sciences
│   ├── Teaching & Education
│   ├── Psychology & Social Work
│   └── Tourism, Sport & Events
│
├── College of Engineering and Information Technology
│   ├── Engineering
│   ├── Computer Science & Information Technology
│   ├── Aviation
│   └── Mathematics & Data Science
│
├── College of Health
│   ├── Allied Health
│   ├── Health & Biomedical Sciences
│   ├── Medicine, Dentistry & Oral Health
│   ├── Nursing & Midwifery
│   └── Nutrition & Food Science
│
└── College of Science
    ├── Agriculture, Animal & Veterinary Science
    ├── Science, Environment & Sustainability
    └── Other science disciplines
```

### 0.3 院校身份信息

| 项目 | 信息 |
|------|------|
| 全称 | University of South Australia (UniSA) / Adelaide University (merged) |
| 成立年份 | 1991 (UniSA) / 2026 (Adelaide University merged entity) |
| 类型 | 公立研究型大学 |
| 位置 | Adelaide, South Australia, Australia |
| 校区 | Adelaide City, Magill, Mawson Lakes, Mount Gambier, Whyalla |
| 原CRICOS | 00121B (UniSA, 已合并) |
| 新CRICOS | 04249J (Adelaide University) |
| TEQSA | PRV14404 (Adelaide University) |
| ABN | 41 202 953 738 |
| 校长/VC | Professor Nicola Phillips |
| 联盟成员 | Group of Eight (Go8), 原ATN成员 |
| 联系方式 | +61-8-7420-5115 |
| 地址 | Level 4, 108 North Terrace, Adelaide SA 5000 |

---

## Section 1 — 学术项目总览 (Academic Programs)

### 1.1 所有本科专业 (All Bachelor Programs) [315个]

**商科与法律:**
- Bachelor of Business
- Bachelor of Business (Human Resource Management)
- Bachelor of Business (Innovation, Entrepreneurship and Strategy)
- Bachelor of Business (International Business)
- Bachelor of Business (Marketing)
- Bachelor of Business (Marketing and Design)
- Bachelor of Business (Project Management)
- Bachelor of Business (Real Estate)
- Bachelor of Business (Sport Management)
- Bachelor of Business (Tourism, Events and Hospitality Management)
- Bachelor of Commerce (Accounting)
- Bachelor of Commerce (Banking and Finance)
- Bachelor of Laws
- Bachelor of Laws (Honours)
- Bachelor of Property

**计算机与IT:**
- Bachelor of Computer Science
- Bachelor of Computer Science (Artificial Intelligence and Machine Learning)
- Bachelor of Computer Science (Human-Centred Computing)
- Bachelor of Computer Science (Programming Languages)
- Bachelor of Information Technology
- Bachelor of Information Technology (Games Development)
- Bachelor of Information Technology (Networking and Cyber Security)
- Bachelor of Information Technology (Software Development)
- Bachelor of Software Engineering (Honours)

**工程:**
- Bachelor of Engineering (Civil) (Honours)
- Bachelor of Engineering (Electrical) (Honours)
- Bachelor of Engineering (Mechanical) (Honours)
- Bachelor of Engineering (Chemical) (Honours)
- Bachelor of Engineering (Mining) (Honours)
- Bachelor of Engineering (Petroleum) (Honours)

**艺术与人文:**
- Bachelor of Arts
- Bachelor of Arts (Aboriginal Studies)
- Bachelor of Arts (Creative Writing)
- Bachelor of Arts (Cultural Studies)
- Bachelor of Arts (English Literature)
- Bachelor of Arts (Environmental Management)
- Bachelor of Arts (History)
- Bachelor of Arts (International Development)
- Bachelor of Arts (Linguistics and Applied Linguistics)
- Bachelor of Arts (Politics)
- Bachelor of Arts (International Security)
- Bachelor of International Relations
- Bachelor of Media and Communication
- Bachelor of Media and Communication (Digital and Social Media Storytelling)
- Bachelor of Media and Communication (Games Design and Production)
- Bachelor of Media and Communication (Media Cultures)
- Bachelor of Media and Communication (Screen Production)
- Bachelor of Media and Communication (Screen Studies)
- Bachelor of Media and Communication (Strategic Communication)

**教育与社会科学:**
- Bachelor of Teaching (Early Childhood Education)
- Bachelor of Teaching (Primary) (Honours)
- Bachelor of Teaching (Secondary) (Honours)
- Bachelor of Psychology
- Bachelor of Social Work
- Bachelor of Social Work (Honours)
- Bachelor of Social Science (Ageing and Disability)
- Bachelor of Social Science (Human Services)

**健康与护理:**
- Bachelor of Nursing
- Bachelor of Midwifery
- Bachelor of Biomedical and Health Sciences
- Bachelor of Biomedical and Health Sciences (Biochemistry)
- Bachelor of Biomedical and Health Sciences (Public Health)
- Bachelor of Health Sciences

**科学与环境:**
- Bachelor of Science
- Bachelor of Science (Animal Behaviour)
- Bachelor of Science (Animal Science)
- Bachelor of Science (Biochemistry)
- Bachelor of Science (Biotechnology)
- Bachelor of Science (Chemistry)
- Bachelor of Science (Analytical Chemistry)
- Bachelor of Science (Pure and Applied Chemistry)
- Bachelor of Science (Medicinal and Biological Chemistry)
- Bachelor of Science (Nuclear Chemistry)
- Bachelor of Science (Ecology)
- Bachelor of Science (Environmental Science)
- Bachelor of Science (Environmental and Geospatial Science)
- Bachelor of Science (Evolutionary Biology)
- Bachelor of Science (Evolutionary Biology and Palaeontology)
- Bachelor of Science (Food Science and Technology)
- Bachelor of Science (Genetics)
- Bachelor of Science (Geology)
- Bachelor of Science (Geology and Earth Resources)
- Bachelor of Science (Marine and Wildlife Conservation)
- Bachelor of Science (Microbiology and Immunology)
- Bachelor of Science (Plant Biology)
- Bachelor of Science (Space Science and Astrophysics)
- Bachelor of Science (Veterinary Bioscience)

**建筑与设计:**
- Bachelor of Architectural Design
- Bachelor of Aviation Management

### 1.2 所有硕士专业 (All Master Programs) [112个]

**商科:**
- Master of Business Administration (MBA)
- Master of Business Administration (Finance)
- Master of Business Administration (Marketing)
- Master of Business Administration (Sustainable Futures)
- International Master of Business Administration
- International Master of Business Administration (Business Analytics)
- International Master of Business Administration (Finance)
- International Master of Business Administration (Human Resource Management)
- International Master of Business Administration (Marketing)
- International Master of Business Administration (Project Management)
- International Master of Business Administration (Procurement and Supply Chain Management)
- Global Executive Master of Business Administration (Defence and Space)
- Master of Accounting and Finance
- Master of Finance
- Master of Professional Accounting
- Master of Business Analytics
- Master of Economics and Resource Policy
- Master of Economics and Resource Policy (Economic Analysis)
- Master of Economics and Resource Policy (Global Food and Agribusiness)
- Master of Economics and Resource Policy (International Trade)
- Master of Economics and Resource Policy (Public Economics and Policy)
- Master of Project Management
- Master of Construction Management
- Master of Data Science

**工程:**
- Master of Professional Engineering (Chemical)
- Master of Professional Engineering (Civil)
- Master of Professional Engineering (Electrical)
- Master of Professional Engineering (Energy Resources)
- Master of Professional Engineering (Environmental and Water Resources Management)
- Master of Professional Engineering (Mechanical)
- Master of Professional Engineering (Mechatronic)
- Master of Professional Engineering (Mining)
- Master of Professional Engineering (Structural)
- Master of Professional Engineering (Telecommunications)
- Master of Engineering (Biopharmaceutical)
- Master of Engineering (Engineering Management)
- Master of Engineering (Maritime)
- Master of Engineering (Materials)

**计算机:**
- Master of Information Technology (Applied Artificial Intelligence)
- Master of Information Technology (Computing and Innovation)
- Master of Information Technology (Cyber Security)
- Master of Information Technology (Enterprise Management)

**教育:**
- Master of Education
- Master of Teaching (Early Childhood Education)
- Master of Teaching (Primary)
- Master of Teaching (Secondary)

**健康:**
- Master of Social Work
- Master of Science (Biotechnology)
- Master of Science (Environment and Conservation)
- Master of Science (Global Food and Nutrition Science)
- Master of Science (Medical Radiation Physics)
- Master of Science (Sustainable Georesources)

**其他:**
- Master of Architecture
- Master of Nursing
- Master of Midwifery

### 1.3 博士与研究项目 (Doctoral Programs) [4个]

- Doctor of Medicine (MD)
- Doctor of Philosophy (PhD) — various disciplines
- Professional Doctorates (various)

### 1.4 研究生证书/文凭 (Graduate Certificate/Diploma) [96个]

包括以下领域的研究生证书:
- Professional Certificate in Pain Sciences
- Professional Certificate in Arbitration
- Professional Certificate in Advisory Services
- Professional Certificate in Understanding Childhood Trauma
- Professional Certificate in Clinical Dermoscopy
- Professional Certificate in Pragmatic Adaptive Educational Leadership
- Professional Certificate in Pragmatic Adaptive Educational Design
- Professional Certificate in Conservative Management of Pelvic Organ Prolapse
- Professional Certificate in Construction Contract Management
- Professional Certificate in Clinical Education
- Professional Certificate in Sonographic Principles and Theory
- Professional Certificate in Defence Contracting Law

以及其他研究生证书和文凭项目。

### 1.5 预科与桥梁项目 (Foundation and Pathway Programs)

- Foundation Studies
- Diploma in Building Studies
- Diploma in Mathematical Studies
- Diploma in Legal Studies
- Centre for Aboriginal Studies in Music (CASM) Foundation Year
- Aboriginal and Torres Strait Islander Pathway
- University Senior College

---

## Section 2 — 学费与费用 (Tuition and Fees)

### 2.1 国内学生 (Domestic Students) — CSP Band

**重要说明**: 澳大利亚高校学费不在中央页面，仅在具体课程页面中显示。以下为2026年澳大利亚政府CSP（Commonwealth Supported Place）标准学费档位：

| Band | 学科领域 | 预计年学费（AUD） |
|------|---------|------------------|
| Band 1 | Education, Nursing, English, Maths, Agriculture, Languages | ~$4,738 |
| Band 2 | Allied Health, IT, Engineering, Science, Built Environment | ~$9,537 |
| Band 3 | Medicine, Dentistry, Veterinary Science | ~$13,558 |
| Band 4 | Law, Accounting, Commerce, Communications, Society & Culture | ~$17,399 |

> 注: UniSA 原学费页面已下线，以上为澳洲政府标准CSP费率。
> 非学费相关费用页面: https://adelaide.edu.au/study/how-to-apply/entry-requirements/non-tuition-fees/

### 2.2 国际学生 (International Students)

国际学生学费按专业/每门课程单独定价。Adelaide University 的 AEM 网站使用 JavaScript 动态渲染，无法通过 curl 提取具体金额。

> 建议通过各专业详情页面查看: https://adelaide.edu.au/study/degrees/{program-name}/

---

## Section 3 — 英语语言要求 (English Language Requirements)

### 3.1 标准要求

| 测试类型 | 标准课程要求 | 语言密集型课程要求 | 护理/助产要求 |
|---------|------------|------------------|--------------|
| IELTS (Academic) | 总分 6.5 (每项≥6.0) | 总分 7.0 (每项≥6.5) | 总分 7.0 |
| TOEFL iBT | 对应IELTS 6.5等值 | 对应IELTS 7.0等值 | 总分 94 |
| PTE Academic | 对应IELTS 6.5等值 | 对应IELTS 7.0等值 | 总分 72 |
| Cambridge C1 Advanced | 接受 | 接受 | — |
| Cambridge C2 Proficiency | 接受 | 接受 | — |
| OET | 健康项目适用 | — | 适用 |

### 3.2 接受的其他英语证明方式

- Australian Year 12 英语科目合格
- International Baccalaureate Diploma (英语授课科目)
- 在英语国家完成本科及以上学历
- 英语语言中心 (ELC) 的 ELICOS 打包课程

### 3.3 英语豁免国家

来自以下国家的公民或在该国完成本科以上学历可豁免:
Australia, Canada (魁北克除外), New Zealand, Republic of Ireland, South Africa, United Kingdom, United States of America

### 3.4 有效期

英语测试成绩有效期为 **2年**（自测试日期起算）。

---

## Section 4 — 申请信息 (Application Information)

### 4.1 国际学生申请流程

| 步骤 | 说明 |
|------|------|
| 1. 选择课程 | 浏览 https://adelaide.edu.au/study/degrees/ |
| 2. 检查入学要求 | 学术成绩 + 英语语言要求 |
| 3. 准备材料 | 成绩单、英语测试成绩、护照等 |
| 4. 在线申请 | https://adelaide.edu.au/study/international-students/how-to-apply/apply-now/ |
| 5. 接受录取 | https://adelaide.edu.au/study/international-students/how-to-apply/accepting-your-offer/ |
| 6. 申请签证 | 使用CRICOS注册确认 |

### 4.2 入学途径 (Entry Pathways)

- Foundation Studies (预科)
- Diploma programs (文凭课程)
- University Senior College
- Credit transfer (学分转换)
- Future in Focus program
- Activate program

### 4.3 入学要求

**本科 (Undergraduate)**:
- 国内学生: ATAR (澳大利亚高等教育入学排名)
- 国际学生: 相当于澳大利亚 Year 12 的学历资格

**硕士 (Postgraduate)**:
- 认可的本科学位
- 部分专业需要相关工作经验和特定前置课程

---

## Section 5 — 奖学金 (Scholarships)

### 5.1 国际学生奖学金 (11项)

| 奖学金名称 | 金额/优惠 | 说明 |
|-----------|----------|------|
| Adelaide Academic Excellence Scholarship (50%) | 学费减免50% | 高成就国际学生 |
| Adelaide Emerging Leaders Award (25%) | 学费减免25% | 新兴领袖 |
| Adelaide Merit Scholarship (15%) | 学费减免15% | 优秀成绩 |
| Adelaide Global Alumni Scholarship (10%) | 学费减免10% | 校友 |
| Adelaide Partner Award (10%) | 学费减免10% | 合作院校 |
| Ashok Khurana Scholarship for Outstanding Indian Students | 待定 | 印度学生 |
| Adelaide Launch Your Future ASEAN Scholarship | 待定 | 东盟学生 |
| BUPA Adelaide University International Student Grant | 健康保险补助 | — |
| Adelaide Sarawak Alumni Scholarship | 待定 | 砂拉越校友 |
| Adelaide Academic Excellence Scholarship (50%) (S2) | 学费减免50% | — |
| Maurice de Rohan International Scholarship | 待定 | — |

### 5.2 国内学生主要奖学金

- Adelaide University Vice-Chancellor's Scholarship (校长奖学金)
- Adelaide University Future Leaders Scholarship (未来领袖奖学金)
- Adelaide University Aspire Scholarship
- Adelaide University Access Scholarship
- Adelaide University Research Scholarship (AURS)
- Research Training Program (RTP) Scholarship
- Commonwealth Scholarships
- Adelaide University Sports Scholarship
- Adelaide University Alumni Scholarship

> 完整奖学金列表: https://adelaide.edu.au/study/scholarships/

---

## Section 6 — 排名与声誉 (Rankings and Reputation)

### 6.1 Adelaide University (合并后)

| 排名类型 | 排名 | 年份 |
|---------|------|------|
| QS World University Rankings | **#79** | 2027 |
| Group of Eight (Go8) | 成员 | — |

### 6.2 University of South Australia (历史排名)

| 排名类型 | 排名 | 年份 |
|---------|------|------|
| QS World University Rankings | ~327 | 2025 |
| THE World University Rankings | 301-350 | 2025 |

---

## Section 7 — 关键日期 (Key Dates) — 待补充

> Adelaide University 的学制日历页面为 JS 动态渲染，具体日期无法通过 curl 提取。
> 建议访问: https://adelaide.edu.au/study/ 查看最新教学日历和申请截止日期。

### 澳大利亚通用学期模式

| 学期 | 典型时间 | 说明 |
|------|---------|------|
| Trimester 1 (T1) | 2月 – 5月 | 主要入学季 |
| Trimester 2 (T2) | 6月 – 8月 | 第二大入学季 |
| Trimester 3 (T3) | 9月 – 12月 | 国际学生常见第二入学季 |

---

## Section 8 — 校园与设施 (Campuses and Facilities)

原 UniSA 校区已全部整合至 Adelaide University:

| 校区 | 位置 | 特色 |
|------|------|------|
| Adelaide City Campus | Adelaide CBD | 主校区，商学院和法学院 |
| Magill Campus | Magill (东郊) | 教育、人文、社会科学 |
| Mawson Lakes Campus | Mawson Lakes | 工程、IT、科学 |
| Mount Gambier Campus | Mount Gambier (南澳) | 区域校区 |
| Whyalla Campus | Whyalla (南澳) | 区域校区，健康护理 |

---

## Section 9 — 数据质量说明

| 维度 | 说明 |
|------|------|
| 数据来源 | Adelaide University sitemap.xml + 网页提取 |
| 数据完整性 | ⚠️ 部分缺失 — UniSA 原官网已下线 |
| 缺失数据 | 专业学费详情、ATAR分数线、申请截止日期、课程描述 |
| 技术原因 | Adelaide University 使用 Adobe Experience Manager (AEM)，大部分内容通过 JavaScript 客户端渲染 |
| 建议 | 如需精确的每专业学费和截止日期，请人工访问 https://adelaide.edu.au/study/degrees/{program-name}/ |

---

## Section 10 — 附录: 完整学位项目列表

> 完整的 575 个学位项目 slug 列表已保存至 uni-cache 目录。

**Adelaide University 全部 22 个研究领域 (Study Areas):**

1. Accounting, Commerce & Economics
2. Agriculture, Animal & Veterinary Science
3. Allied Health
4. Architecture & Design
5. Arts, Humanities & Social Sciences
6. Aviation
7. Business, Marketing & Management
8. Computer Science & Information Technology
9. Creative Media & Communication
10. Engineering
11. Health & Biomedical Sciences
12. Law and Justice
13. Mathematics & Data Science
14. Medicine, Dentistry & Oral Health
15. Music
16. Nursing & Midwifery
17. Nutrition & Food Science
18. Property, Construction & Real Estate
19. Psychology & Social Work
20. Science, Environment & Sustainability
21. Teaching & Education
22. Tourism, Sport & Events

---

*Document generated by Hermes Agent — University Research Pipeline*
*Data extracted: 2026-07-11*
*Note: University of South Australia has been merged into Adelaide University as of 2026. This document reflects the current merged entity structure.*
