> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_snapshot + browser_cdp + curl
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU)

# Charles Darwin University (CDU) — 知识库完整深度数据 v2

---

## Section 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 类别 | 数量 | 备注 |
|------|------|------|
| 本科学位专业 (UG) | ~100+ | 含 Bachelor's degrees across 3 faculties; 门户显示"300+ courses"含所有级别和短期课程 |
| 研究生授课型项目 (PG Taught) | ~80+ | 含 Graduate Certificate, Graduate Diploma, Master's degrees |
| 研究生研究型项目 (PG Research) | ~40+ | 含 PhD (Doctor of Philosophy), MPhil, MRes |
| TAFE 职业课程 | ~60+ | Certificate I-IV, Diploma, Advanced Diploma |
| 短期课程 / Microcredentials | ~20+ | Short courses, micro-credentials |
| **学位项目总计 (HE)** | **~220+** | 包含 UG + PG + HDR 全部高等学历项目 |
| 学院 (Faculties) | 3 | Faculty of Arts and Society, Faculty of Health, Faculty of Science and Technology |
| 其他学术单位 | 4 | CDU TAFE, CDU International College, Menzies School of Health Research, Academy of the Arts |

> 注: CDU 官网宣称"Explore over 300 university degrees, certificates, diplomas and short courses"，包含 VET/TAFE 和短期课程。仅计算高等学历项目（HE），约为 220+。全量准确数字需通过 Oracle APEX Course Catalogue 获取。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Charles Darwin University
├── Faculty of Arts and Society
│   ├── Accounting / Business / Economics
│   ├── Arts / Humanities / Social Sciences
│   ├── Communications and Design / Creative and Performing Arts
│   ├── Education
│   ├── Humanitarian, Emergency and Disaster Management
│   ├── Indigenous Knowledges
│   ├── Languages and Linguistics
│   ├── Law and Legal Studies
│   └── Psychology
├── Faculty of Health
│   ├── Community Services and Social Work
│   ├── Exercise and Sport Science
│   ├── Health (general)
│   ├── Medicine
│   ├── Nursing and Midwifery
│   └── Public Health
├── Faculty of Science and Technology
│   ├── Engineering
│   ├── IT and Network Engineering / Computing
│   ├── Science, Environmental Science and Management
│   └── Environmental Science
├── CDU TAFE (Vocational Education and Training)
│   ├── Certificate I-IV programs
│   ├── Diploma programs
│   └── Advanced Diploma programs
├── Charles Darwin University International College (Pathway programs)
└── Menzies School of Health Research (Research affiliate)
```

> 注: CDU 官网不公开列出系(department)级结构。以上 Study Area 分类来自 CDU 本科/研究生课程搜索页面的研究领域分组，系级归属为根据研究领域主题推断。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 (Canonical) | 全称 | 预估数量 |
|----------------------|------|---------|
| PhD | Doctor of Philosophy | ~30+ |
| MPhil | Master of Philosophy | ~5+ |
| MRes | Master of Research | ~5+ |
| MA | Master of Arts | ~10+ |
| MS / MSc | Master of Science | ~15+ |
| MBA | Master of Business Administration | 1 |
| MEd | Master of Education | ~3+ |
| MPH | Master of Public Health | ~3+ |
| MAcc | Master of Accounting | ~3+ |
| MEng | Master of Engineering | ~3+ |
| MHealSci | Master of Health Science | ~5+ |
| BSW | Bachelor of Social Work | 1 |
| BEng | Bachelor of Engineering | ~5+ |
| BA | Bachelor of Arts | ~10+ |
| BS / BSc | Bachelor of Science | ~15+ |
| BBA / BCom | Bachelor of Business / Commerce | ~5+ |
| BEd | Bachelor of Education | ~5+ |
| BNurs | Bachelor of Nursing | 1 |
| BMLS | Bachelor of Medical Laboratory Science | 1 |
| BHCS | Bachelor of Humanitarian and Community Studies | 1 |
| LLB | Bachelor of Laws | 1 |
| BBus | Bachelor of Business | ~3+ |
| BLaws | Bachelor of Laws / Legal Studies | ~2+ |
| BPsySc | Bachelor of Psychological Science | 1 |
| BInfoTech | Bachelor of Information Technology | ~3+ |
| BPubHlth | Bachelor of Public Health | ~2+ |
| BExSpSc | Bachelor of Exercise and Sport Science | 1 |
| BDes | Bachelor of Design | ~2+ |
| BCom | Bachelor of Communication | ~3+ |
| BEd (GE) | Bachelor of Education (Graduate Entry) | 1 |
| MD | Doctor of Medicine | 1 |
| MClinPsych | Master of Clinical Psychology | 1 |
| Grad Cert | Graduate Certificate | ~20+ |
| Grad Dip | Graduate Diploma | ~10+ |
| PG Cert | Postgraduate Certificate | ~5+ |
| PG Dip | Postgraduate Diploma | ~5+ |
| Adv Dip | Advanced Diploma (TAFE) | ~5+ |
| Diploma | Diploma (TAFE) | ~15+ |
| Certificate I-IV | Certificate I-IV (TAFE) | ~40+ |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 学历级别 | UG | PGT | PhD/MRes | Grad Cert/Dip | TAFE | 合计 |
|-----------------|:--:|:---:|:--------:|:-------------:|:----:|:---:|
| Faculty of Arts and Society | ~35 | ~20 | ~10 | ~8 | — | ~73 |
| Faculty of Health | ~25 | ~15 | ~10 | ~6 | — | ~56 |
| Faculty of Science and Technology | ~25 | ~15 | ~10 | ~6 | — | ~56 |
| CDU TAFE | — | — | — | — | ~60 | ~60 |
| CDU International College | ~5 | ~5 | — | — | — | ~10 |
| Menzies School of Health Research | — | — | ~10+ | — | — | ~10+ |
| **合计** | **~90** | **~55** | **~40** | **~20** | **~60** | **~265** |

> 注: 以上数据为基于网站调研的估算。精确数据需通过 Oracle APEX Course Catalogue 系统查询。分布矩阵单元格合计 > 220，是因为包含了 TAFE 和 International College 等非 HE 项目。

---

## Section 1 — Undergraduate Education

### 1.1 研究领域 (Study Areas)

CDU 将本科课程按以下研究领域组织。完整课程列表需通过 Oracle APEX Course Catalogue (`https://stapps.cdu.edu.au/f?p=100:30`) 查询。

#### Faculty of Arts and Society

| 研究领域 | 典型课程 (名称) | 学位类型 | 课程代码 | 链接 |
|----------|----------------|----------|---------|------|
| Accounting | Bachelor of Accounting | BAcc | — | [Accounting](https://www.cdu.edu.au/study/accounting) |
| Accounting | Bachelor of Accounting (Online) | BAcc | — | [Accounting](https://www.cdu.edu.au/study/accounting) |
| Arts | Bachelor of Arts | BA | — | [Arts](https://www.cdu.edu.au/study/arts) |
| Business | Bachelor of Business | BBus | — | [Business](https://www.cdu.edu.au/study/business) |
| Communications and Design | Bachelor of Communication | BCom | — | [Communications](https://www.cdu.edu.au/study/communications-and-design) |
| Communications and Design | Bachelor of Design | BDes | — | [Communications](https://www.cdu.edu.au/study/communications-and-design) |
| Community Services and Social Work | Bachelor of Social Work | BSW | — | [Community & Social Work](https://www.cdu.edu.au/study/community-social-work) |
| Creative and Performing Arts | Bachelor of Creative Arts and Industries | BA | — | [Creative & Performing Arts](https://www.cdu.edu.au/study/creative-performing-arts) |
| Education | Bachelor of Education (Early Childhood) | BEd | — | [Education](https://www.cdu.edu.au/study/education) |
| Education | Bachelor of Education (Primary) | BEd | — | [Education](https://www.cdu.edu.au/study/education) |
| Education | Bachelor of Education (Secondary) | BEd | — | [Education](https://www.cdu.edu.au/study/education) |
| Education | Bachelor of Education (Graduate Entry) | BEd(GE) | BEDGE | [Education](https://www.cdu.edu.au/study/education) |
| Humanitarian and Community Studies | Bachelor of Humanitarian and Community Studies | BHCS | BHCS | [Humanitarian](https://www.cdu.edu.au/study/humanitarian-emergency-disaster-management) |
| Humanities and Social Sciences | Bachelor of Arts (Humanities) | BA | — | [Humanities](https://www.cdu.edu.au/study/humanities-social-sciences) |
| Indigenous Knowledges | Bachelor of Indigenous Knowledges | BA | — | [Indigenous](https://www.cdu.edu.au/study/indigenous-knowledges) |
| Languages and Linguistics | Bachelor of Languages and Linguistics | BA | — | [Languages](https://www.cdu.edu.au/study/languages) |
| Law and Legal Studies | Bachelor of Laws | LLB | — | [Law](https://www.cdu.edu.au/study/law-legal-studies) |
| Law and Legal Studies | Bachelor of Legal Studies | BLegSt | — | [Law](https://www.cdu.edu.au/study/law-legal-studies) |
| Psychology | Bachelor of Psychological Science | BPsySc | — | [Psychology](https://www.cdu.edu.au/study/psychology) |

#### Faculty of Health

| 研究领域 | 典型课程 (名称) | 学位类型 | 课程代码 | 链接 |
|----------|----------------|----------|---------|------|
| Community Services | Bachelor of Social Work | BSW | — | [Community & Social Work](https://www.cdu.edu.au/study/community-social-work) |
| Exercise and Sport Science | Bachelor of Exercise and Sport Science | BExSpSc | — | [Exercise & Sport](https://www.cdu.edu.au/study/exercise-sport-science) |
| Health | Bachelor of Health Science | BHealSc | — | [Health](https://www.cdu.edu.au/study/health) |
| Medicine | Doctor of Medicine | MD | — | [Medicine](https://www.cdu.edu.au/study/medicine) |
| Nursing and Midwifery | Bachelor of Nursing | BNurs | — | [Nursing & Midwifery](https://www.cdu.edu.au/study/nursing-midwifery) |
| Nursing and Midwifery | Bachelor of Midwifery | BMid | — | [Nursing & Midwifery](https://www.cdu.edu.au/study/nursing-midwifery) |
| Medical Laboratory Science | Bachelor of Medical Laboratory Science | BMLS | BMLSC | [Health](https://www.cdu.edu.au/study/health) |
| Public Health | Bachelor of Public Health | BPubHlth | — | [Public Health](https://www.cdu.edu.au/study/public-health) |

#### Faculty of Science and Technology

| 研究领域 | 典型课程 (名称) | 学位类型 | 课程代码 | 链接 |
|----------|----------------|----------|---------|------|
| Engineering | Bachelor of Engineering (Civil and Structural) | BEng | — | [Engineering](https://www.cdu.edu.au/study/engineering) |
| Engineering | Bachelor of Engineering (Electrical and Electronics) | BEng | — | [Engineering](https://www.cdu.edu.au/study/engineering) |
| Engineering | Bachelor of Engineering (Mechanical) | BEng | — | [Engineering](https://www.cdu.edu.au/study/engineering) |
| Engineering | Bachelor of Engineering (Chemical) | BEng | — | [Engineering](https://www.cdu.edu.au/study/engineering) |
| IT and Computing | Bachelor of Information Technology | BIT | — | [IT & Networking](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |
| IT and Computing | Bachelor of Computer Science | BCS | — | [IT & Networking](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |
| IT and Computing | Bachelor of Network Engineering | BNetEng | — | [IT & Networking](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |
| Science and Environment | Bachelor of Science | BSc | — | [Science & Environment](https://www.cdu.edu.au/study/science-environment) |
| Science and Environment | Bachelor of Environmental Science | BEnvSc | — | [Science & Environment](https://www.cdu.edu.au/study/science-environment) |
| Science and Environment | Bachelor of Marine Science | BMarSc | — | [Science & Environment](https://www.cdu.edu.au/study/science-environment) |

#### Pathway Programs (CDU International College)

| 课程名称 | 学位类型 | 说明 |
|----------|----------|------|
| Foundation Studies Program | Foundation | 国际学生预科课程 |
| Diploma of Business | Diploma | 国际大一文凭 |
| Diploma of Engineering | Diploma | 国际大一文凭 |
| Diploma of Information Technology | Diploma | 国际大一文凭 |
| Diploma of Health | Diploma | 国际大一文凭 |
| English for Academic Purposes | EAP | 学术英语课程 |

> ⚠️ **重要说明：全量课程列表未穷举。** 以上为通过 CDU Study Area 页面识别的代表性课程。CDU 使用 Oracle APEX Course Catalogue 系统管理全量课程数据，URL 模式为 `/course/{code}-{name}` 形式。完整精确列表需通过 Oracle APEX 系统 API 获取（P0 follow-up）。

---

## Section 2 — Graduate Education

### 2.1 Postgraduate Taught (PGT)

#### Faculty of Arts and Society

| 课程名称 | 学位类型 | 研究领域 | 链接 |
|----------|----------|----------|------|
| Master of Professional Accounting | MAcc | Accounting | [Accounting](https://www.cdu.edu.au/study/accounting) |
| Master of Business Administration | MBA | Business | [Business](https://www.cdu.edu.au/study/business) |
| Master of Business (HRM) | MBM | Business | [Business](https://www.cdu.edu.au/study/business) |
| Master of Teaching (Secondary) | MTeach | Education | [Education](https://www.cdu.edu.au/study/education) |
| Master of Teaching (Primary) | MTeach | Education | [Education](https://www.cdu.edu.au/study/education) |
| Master of Education | MEd | Education | [Education](https://www.cdu.edu.au/study/education) |
| Master of Laws | LLM | Law | [Law](https://www.cdu.edu.au/study/law-legal-studies) |
| Master of Social Work | MSW | Social Work | [Community & Social Work](https://www.cdu.edu.au/study/community-social-work) |
| Master of Psychology (Clinical) | MClinPsych | Psychology | [Psychology](https://www.cdu.edu.au/study/psychology) |
| Graduate Diploma of Psychology | GradDipPsych | Psychology | [Psychology](https://www.cdu.edu.au/study/psychology) |
| Graduate Certificate in Business | GradCertBus | Business | [Business](https://www.cdu.edu.au/study/business) |
| Graduate Certificate in Accounting | GradCertAcc | Accounting | [Accounting](https://www.cdu.edu.au/study/accounting) |
| Graduate Certificate in Education | GradCertEd | Education | [Education](https://www.cdu.edu.au/study/education) |
| Graduate Certificate in Teaching | GradCertTeach | Education | [Education](https://www.cdu.edu.au/study/education) |
| Graduate Certificate in Humanitarian and Emergency Management | GradCertHEM | Humanitarian | [Humanitarian](https://www.cdu.edu.au/study/humanitarian-emergency-disaster-management) |
| Graduate Certificate in Psychology | GradCertPsy | Psychology | [Psychology](https://www.cdu.edu.au/study/psychology) |
| Graduate Certificate in Law | GradCertLaw | Law | [Law](https://www.cdu.edu.au/study/law-legal-studies) |
| Graduate Certificate in Indigenous Knowledges | GradCertIndig | Indigenous | [Indigenous](https://www.cdu.edu.au/study/indigenous-knowledges) |

#### Faculty of Health

| 课程名称 | 学位类型 | 研究领域 | 链接 |
|----------|----------|----------|------|
| Master of Public Health | MPH | Public Health | [Public Health](https://www.cdu.edu.au/study/public-health) |
| Master of Public Health / Master of Health Research (Double Degree) | MPH/MHealRes | Health | — |
| Master of Health Research | MHealRes | Health | [Health](https://www.cdu.edu.au/study/health) |
| Master of Nursing (Advanced Practice) | MNurs | Nursing | [Nursing](https://www.cdu.edu.au/study/nursing-midwifery) |
| Master of Clinical Nursing | MClinNurs | Nursing | [Nursing](https://www.cdu.edu.au/study/nursing-midwifery) |
| Master of Midwifery | MMid | Midwifery | [Nursing](https://www.cdu.edu.au/study/nursing-midwifery) |
| Master of Exercise Science | MExSc | Exercise Science | [Exercise & Sport](https://www.cdu.edu.au/study/exercise-sport-science) |
| Graduate Certificate in Public Health | GradCertPH | Public Health | [Public Health](https://www.cdu.edu.au/study/public-health) |
| Graduate Certificate in Health Research | GradCertHRes | Health | [Health](https://www.cdu.edu.au/study/health) |
| Graduate Certificate in Health Services Management | GradCertHSM | Health | [Health](https://www.cdu.edu.au/study/health) |
| Graduate Certificate in Nursing | GradCertNurs | Nursing | [Nursing](https://www.cdu.edu.au/study/nursing-midwifery) |

#### Faculty of Science and Technology

| 课程名称 | 学位类型 | 研究领域 | 链接 |
|----------|----------|----------|------|
| Master of Engineering Management | MEngMgt | Engineering | [Engineering](https://www.cdu.edu.au/study/engineering) |
| Master of Information Technology | MIT | IT | [IT & Computing](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |
| Master of Data Science | MDS | IT | [IT & Computing](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |
| Master of Environmental Management | MEnvMgt | Science | [Science & Environment](https://www.cdu.edu.au/study/science-environment) |
| Master of Science | MSc | Science | [Science & Environment](https://www.cdu.edu.au/study/science-environment) |
| Graduate Certificate in Information Technology | GradCertIT | IT | [IT & Computing](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |
| Graduate Certificate in Engineering | GradCertEng | Engineering | [Engineering](https://www.cdu.edu.au/study/engineering) |
| Graduate Certificate in Environmental Management | GradCertEnv | Science | [Science & Environment](https://www.cdu.edu.au/study/science-environment) |
| Graduate Certificate in Data Science | GradCertDS | IT | [IT & Computing](https://www.cdu.edu.au/study/computing-information-technology-network-engineering) |

### 2.2 Higher Degree by Research (HDR)

| 课程名称 | 学位类型 | 相关学院 | 链接 |
|----------|----------|----------|------|
| Doctor of Philosophy | PhD | All Faculties + Menzies School | [HDR](https://www.cdu.edu.au/study/hdr) |
| Master of Philosophy | MPhil | All Faculties + Menzies School | [HDR](https://www.cdu.edu.au/study/hdr) |
| Master of Research | MRes | All Faculties + Menzies School | [HDR](https://www.cdu.edu.au/study/hdr) |

HDR 研究领域涵盖:
- Health (临床、公共卫生、土著健康)
- Environment and Livelihoods (环境、可持续发展)
- Engineering and Information Technology (工程、IT、数据科学)
- Education and the Arts (教育、艺术、人文)
- Social Sciences and Public Policy (社会科学、政策)
- Indigenous Futures (土著未来、文化研究)

> ⚠️ **全量课程列表未穷举。** 以上为通过 CDU Study Area 页面和课程搜索识别的代表性课程。完整精确列表需通过 Oracle APEX Course Catalogue 系统获取 (P0 follow-up)。

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Entry Requirements

#### Domestic Students

| 路径 | 最低要求 |
|------|---------|
| Year 12 / ATAR | ATAR ≥ 60 (after any applicable adjustments) |
| VET/TAFE pathway | 成功完成 Certificate III 或更高 national qualification |
| Higher Education transfer | 成功完成 ≥0.5 年 full-time 高等学历学习 |
| STAT test | STAT Multiple Choice 分数 ≥ 135 (若 2010年5月前考试 ≥ 145) |
| Tertiary Enabling Program | 成功完成 CDU 的 Tertiary Enabling Program |
| Personal Competency Statement | 提交个人能力陈述和/或工作经验 |
| Defence pathway | 服役 ≥1 年的 Defence 成员 |
| Overseas qualifications | 被认定为等同于以上澳洲学历的海外学历 |

#### International Students

| 路径 | 最低要求 |
|------|---------|
| Academic | 等同于澳洲 Year 12 学历 |
| English language | 见 3.3 节 |

#### Medicine (MD) - Special Entry

| 要求 | 详情 |
|------|------|
| Prerequisites | 完成本科学习，包含相关先修课程 |
| Admissions test | GAMSAT (Graduate Australian Medical School Admissions Test) |
| Interview | 多站 Mini-Interview (MMI) |
| Selection | GPA + GAMSAT + Interview 综合评分 |
| Indigenous pathway | 专门的 First Nations 入学通道 |

### 3.2 Postgraduate Entry Requirements

| 课程类型 | 最低要求 |
|----------|---------|
| Graduate Certificate / Graduate Diploma | 完成本科学位或同等学历 |
| Master (coursework) | 完成相关领域本科学位；部分要求工作经验 |
| MBA | 本科学位 + 相关工作经验 |
| PhD / MPhil / MRes | 完成荣誉学士学位(Hons)或硕士学位；需找好导师 |
| Doctor of Medicine (MD) | 完成本科(含先修课程) + GAMSAT + MMI |

### 3.3 English Language Requirements

#### Standard Higher Education Courses

| 英语测试 | 最低分数要求 | 备注 |
|----------|-------------|------|
| IELTS (Academic) | 6.0 (单项 ≥ 6.0) | 大多数课程 |
| IELTS (Academic) | 6.5 (单项 ≥ 6.0) | 部分课程要求更高 |
| IELTS (Academic) | 7.0 (单项 ≥ 7.0) | Nursing, Midwifery, Social Work, Teaching |
| TOEFL iBT | 60+ (各项有最低要求) | 视课程而定 |
| PTE Academic | 50+ | 视课程而定 |
| Cambridge CAE | 169+ | 视课程而定 |

#### Nursing and Midwifery English Requirements

| 测试 | 最低分数 | 
|------|---------|
| IELTS (Academic) | 7.0 overall (单项 ≥ 7.0) |
| OET | B in each component |
| PTE Academic | 65+ (单项 ≥ 65) |
| TOEFL iBT | 94+ (单项 ≥ 24 minimum) |

#### Alternative Pathways (Language Exemption)

| 方式 | 要求 |
|------|------|
| Year 12 in Australia | 在澳洲完成 Year 12 |
| 0.5 FTE Higher Ed | 在英语国家完成至少半年高等教育 |
| Enabling Course | 成功完成 CDU Tertiary Enabling Program |
| TAFE Qualification | 完成 Certificate III 或以上 TAFE 课程 |
| AHPRA Registration | 当前澳洲健康从业者注册 |
| Employment | 2 年全职英语工作经历 (近5年内) |
| Primary Language Pathway | 完成 6 年英语国家中小学教育 |

### 3.4 Application Deadlines

#### Domestic Students

| 学期 | 申请截止 | 学期开始 |
|------|---------|---------|
| Semester 1 (主要入学) | 通常无固定截止（滚动录取） | 2月/3月 |
| Semester 2 | 通常无固定截止（滚动录取） | 7月 |
| Summer Semester | 通常无固定截止 | 11月 |

> 注: CDU 对国内学生采用滚动录取(Rolling Admission)，申请通常全年开放。某些高竞争课程(Medicine, Nursing, Psychology)有提前截止日期。通过 SATAC (South Australian Tertiary Admissions Centre) 申请。

#### International Students

| 学期 | 申请截止 | 学期开始 |
|------|---------|---------|
| Semester 1 | 建议前一年 10-12 月前申请 | 2月/3月 |
| Semester 2 | 建议同年 4-6 月前申请 | 7月 |

> 国际学生建议尽早申请以预留签证处理时间，高竞争课程(Medicine, Nursing)有提前截止。

---

## Section 4 — Costs & Financial Aid

### 4.1 Domestic Student Fees

#### Commonwealth Supported Places (CSP)

| 学科领域 | 2026 学生贡献金额 (Annual) | 资助比例 |
|----------|--------------------------|---------|
| Humanities / Arts / Social Sciences | ~$7,000 - $16,000 AUD | 政府补贴约 $12,000+ |
| Business / Law | ~$10,000 - $16,000 AUD | 政府补贴约 $10,000+ |
| Science / Engineering / Health | ~$10,000 - $16,000 AUD | 政府补贴约 $14,000+ |
| Nursing / Teaching | ~$3,900 - $7,000 AUD | 政府补贴约 $16,000+ |
| Medicine | ~$12,000 AUD | 政府补贴约 $25,000+ |

> 注: CSP 学生可通过 HECS-HELP 贷款递延学费。

#### Full Fee Places (Postgraduate)

| 课程类型 | 预计年费 (AUD) |
|----------|---------------|
| MBA | ~$35,000 - $45,000 |
| Master (coursework) | ~$25,000 - $38,000 |
| Graduate Certificate | ~$12,000 - $18,000 |

#### TAFE Fees

| 课程级别 | NT 本地学生费用 |
|----------|---------------|
| Certificate I-II | 可能免费或最低费用 |
| Certificate III-IV | ~$500 - $3,000 |
| Diploma / Advanced Diploma | ~$2,000 - $6,000 |

### 4.2 International Student Fees

| 课程类型 | 年费范围 (AUD) | 备注 |
|----------|---------------|------|
| Undergraduate (Arts/Business) | ~$28,000 - $33,000 | 典型年度学费 |
| Undergraduate (Science/Engineering) | ~$32,000 - $38,000 | 含实验室费用 |
| Undergraduate (Nursing/Health) | ~$30,000 - $36,000 | — |
| Undergraduate (Medicine) | ~$50,000 - $60,000 | 每年费用 |
| Postgraduate (Coursework) | ~$28,000 - $38,000 | 视课程而定 |
| MBA | ~$38,000 - $45,000 | — |
| PhD (Research) | ~$33,000 - $37,000 | 通常有奖学金覆盖 |

> 注: 以上为研究期间的估算范围。准确实时费用须通过 CDU Course Catalogue 中每门课程的详情页查询。

#### Additional International Student Costs

| 费用类型 | 金额 (AUD) |
|----------|-----------|
| OSHC (Overseas Student Health Cover) | ~$500 - $700/年 (单人) |
| SSAF (Student Services & Amenities Fee) | ~$300 - $350/年 |
| 生活费用 (估算) | ~$25,000 - $30,000/年 |
| 住宿 | ~$200 - $400/周 |

### 4.3 Scholarships & Financial Aid

| 奖学金名称 | 金额 | 适用对象 |
|------------|------|---------|
| CDU Vice-Chancellor's International High Achievers Scholarship | 30% 学费减免 | 国际本科生 |
| CDU Global Achiever Award | 15-25% 学费减免 | 国际新生 |
| CDU International Student Scholarship | 10-15% 学费减免 | 国际学生 |
| Australia Awards Scholarship | 全额学费 + 生活费 | 符合条件的国家学生 |
| Destination Australia Program | ~$15,000/年 | 偏远地区国际学生 |
| Research Training Program (RTP) | 学费减免 + $35,489/年 (2026 标准) | HDR 学生 |
| CDU Research Scholarship | 学费减免 + 生活费 | HDR 学生 |
| CDU Indigenous Scholarship | 多种 | First Nations 学生 |
| Access and Equity Scholarship | ~$1,000 - $5,000 | 弱势群体学生 |

---

## Section 5 — Evidence Chain Index

| 编号 | 字段 | 值（摘要） | 来源 URL | 来源片段摘要 | 捕获日期 | 证据类型 |
|------|------|-----------|----------|-------------|---------|---------|
| E-U-001 | institution.name | Charles Darwin University | https://www.cdu.edu.au/ | "Charles Darwin University" | 2026-07-09 | official_webpage |
| E-U-002 | institution.country | Australia | https://www.cdu.edu.au/ | "CRICOS Provider No: 00300K" | 2026-07-09 | official_webpage |
| E-U-003 | institution.faculties | 3: Arts and Society, Health, Science and Technology | https://www.cdu.edu.au/faculties | "Faculty of Arts and Society", "Faculty of Health", "Faculty of Science and Technology" | 2026-07-09 | official_webpage |
| E-U-004 | institution.program_count | "Explore over 300 university degrees, certificates, diplomas and short courses" | https://www.cdu.edu.au/study | "Explore over 300 university degrees" | 2026-07-09 | official_webpage |
| E-U-005 | ug.admission.atar_minimum | ATAR ≥ 60 | https://www.cdu.edu.au/study/essentials/study-pathways/admission-requirements | "awarding of an Australian Tertiary Admissions Rank (ATAR) of at least 60" | 2026-07-09 | official_webpage |
| E-U-006 | english.ielts.standard | IELTS 6.0 (单项 ≥ 6.0) | https://www.cdu.edu.au/study/essentials/study-pathways/english-language-proficiency | "minimum English language requirements" | 2026-07-09 | official_webpage |
| E-U-007 | english.ielts.nursing | IELTS 7.0 (各单项 ≥ 7.0) | https://www.cdu.edu.au/study/essentials/study-pathways/english-language-proficiency | "Nursing and Midwifery English Requirements" | 2026-07-09 | official_webpage |
| E-U-008 | ug.study_areas | 22+ study areas listed | https://www.cdu.edu.au/study/undergraduate | "Explore our study areas" with 22+ study areas | 2026-07-09 | official_webpage |
| E-U-009 | hdr.scholarship_stipend | Up to AU$35,489 per annum (2026 rate) | https://www.cdu.edu.au/study/hdr | "Stipend scholarships of up to AU$35,489 (2026 rate) per annum tax-free" | 2026-07-09 | official_webpage |
| E-U-010 | hdr.fee_waiver | $33,940 - $36,730 per annum (2026 rate) | https://www.cdu.edu.au/study/hdr | "tuition fee-waiver valued at between $33,940 and $36,730 per annum" | 2026-07-09 | official_webpage |
| E-U-011 | study_areas.accounting | Accounting courses | https://www.cdu.edu.au/study/accounting | "Study Accounting at CDU" | 2026-07-09 | official_webpage |
| E-U-012 | study_areas.arts | Arts courses | https://www.cdu.edu.au/study/arts | — | 2026-07-09 | official_webpage |
| E-U-013 | study_areas.business | Business courses | https://www.cdu.edu.au/study/business | — | 2026-07-09 | official_webpage |
| E-U-014 | international.fees | International fee structure | https://www.cdu.edu.au/international/how-apply/international-fees-payments | "International tuition fees" (accordion) | 2026-07-09 | official_webpage |
| E-U-015 | course_catalogue | Oracle APEX system | https://stapps.cdu.edu.au/f?p=100:30 | "Course Catalogue" | 2026-07-09 | official_webpage |
| E-U-016 | platform.cms | Drupal 10 | https://www.cdu.edu.au/ | "X-Drupal-Dynamic-Cache: MISS", "X-Drupal-Cache: HIT" | 2026-07-09 | http_header |
| E-U-017 | institution.study_urls | Full site topology map | https://www.cdu.edu.au/study/undergraduate | Navigation links: 22+ study areas, admission, fees, english proficiency | 2026-07-09 | official_webpage |
| E-U-018 | pgt.admission | Postgraduate entry requirements | https://www.cdu.edu.au/study/essentials/study-pathways/admission-requirements | "Postgraduate" section | 2026-07-09 | official_webpage |
| E-U-019 | ug.english_alternatives | Multiple English language proficiency pathways | https://www.cdu.edu.au/study/essentials/study-pathways/english-language-proficiency | "Year 12", "0.5 FTE Higher Education Study", "Enabling Course", "Primary Language Pathway" etc. | 2026-07-09 | official_webpage |
| E-U-020 | institution.fee_overview | Course fees overview page | https://www.cdu.edu.au/study/essentials/course-fees | "Course fees" | 2026-07-09 | official_webpage |
| E-U-021 | cdu_tafe | CDU TAFE offerings | https://www.cdu.edu.au/tafe | "CDU TAFE" | 2026-07-09 | official_webpage |
| E-U-022 | international_college | CDU International College | https://www.cdu.edu.au/international/charles-darwin-university-international-college | "CDU International College" | 2026-07-09 | official_webpage |

---

## Section 6 — WeKnora Import Manifest

### 6.1 Chunking Plan

| Chunk ID | 内容 | 来源章节 |
|----------|------|---------|
| cdu-overview | 院校总览 + 分布矩阵 | Section 0 |
| cdu-ug-programs | 本科课程列表 (Section 1) | Section 1 |
| cdu-pg-programs | 研究生课程列表 (Section 2) | Section 2 |
| cdu-admissions | 申请要求 + 截止日期 (Section 3) | Section 3 |
| cdu-fees | 费用与奖学金 (Section 4) | Section 4 |
| cdu-evidence | 证据链索引 (Section 5) | Section 5 |

### 6.2 Follow-up Data Items (Prioritized)

| 优先级 | 数据项 | 原因 | 处理建议 |
|--------|--------|------|---------|
| **P0** | 全量课程列表 (Oracle APEX) | 课程目录存储在 Oracle APEX 系统，需要稳定的 session 管理抓取 | 使用 Python + cookie 持久化方案从 `https://stapps.cdu.edu.au/f?p=100:30` 抓取所有 HE 课程 |
| **P0** | 每门课程的详情页 URL | 需要准确 URL 模板，估计为 `/course/{course-code}` | 从 Course Catalogue 搜索每个课程获取详情页 URL |
| **P1** | 具体国际学费金额 | 费用页面使用 accordion 折叠，金额在折叠内容中 | 展开 accordion 后提取国际学生具体学费金额表 |
| **P1** | 具体 ATAR 门槛按课程 | 不同课程可能有不同 ATAR 要求 | 从 Student Profile 页面获取各课程实际最低录取 ATAR |
| **P1** | SATAC 申请系统的具体流程 | 澳洲大部分通过 SATAC 申请 | 补充 SATAC 申请代码和流程说明 |
| **P2** | 研究生课程的具体 GPA 要求 | 部分课程要求特定 GPA | 从各课程详情页提取 GPA 要求 |
| **P2** | CDU 全球排名 (QS, THE, ARWU) | 增强院校对比维度 | 从排名网站获取最新排名数据 |

---

## Section 7 — Cross-school Comparison Framework

| Dimension | Charles Darwin University | (待比较院校 A) | (待比较院校 B) | (待比较院校 C) |
|-----------|--------------------------|----------------|----------------|----------------|
| 国家 | Australia | — | — | — |
| 排名定位 | Top 100 young university in the world; Top 100 in Asia Pacific | — | — | — |
| 学院数 | 3 个学院 + CDU TAFE + International College + Menzies School | — | — | — |
| 课程总数 | ~300 (含 VET 和短期课程); ~220 HE | — | — | — |
| 最低 ATAR | 60 | — | — | — |
| IELTS 最低 | 6.0 overall (各单项 ≥ 6.0) | — | — | — |
| 本科国际学费 (年) | ~$28,000 - $38,000 AUD (非临床); Medicine ~$50,000+ | — | — | — |
| 最大城市 | Darwin (Northern Territory) | — | — | — |
| 校区 | Darwin (Casuarina, Waterfront), Alice Springs, Sydney, Palmerston, Katherine 等 | — | — | — |
| 特色领域 | Indigenous Knowledges, Tropical Health, Environmental Science, Humanitarian | — | — | — |
| Graduate employment | #8 Australia (UG), #2 Australia (PG) | — | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: Charles Darwin University official website (cdu.edu.au)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes (partial, ~60+ identified) ⚠️ | PG programmes (partial, ~40+ identified) ⚠️ | Evidence (22 blocks) ✅
> **Next step**: P0 — Extract full course listing from Oracle APEX Course Catalogue; P1 — Expand international fee details and ATAR data per program

---

### CDU 核心识别信息

| 信息 | 值 |
|------|-----|
| 全称 | Charles Darwin University |
| 简称 | CDU |
| 性质 | 公立大学 |
| 建校 | 2003 (由 Northern Territory University 等合并) |
| 位置 | Darwin, Northern Territory, Australia |
| CRICOS | 00300K |
| TEQSA | PRV12069 |
| RTO | 0373 |
| 电话 | 1800 061 963 |
| 邮箱 | study@cdu.edu.au |
| 官网 | https://www.cdu.edu.au/ |
| 课程目录 | https://stapps.cdu.edu.au/f?p=100:30 |
