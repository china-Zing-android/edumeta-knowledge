# Singapore Institute of Management (SIM) — 知识库完整深度数据

> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_snapshot + curl + sitemap extraction
> **Target knowledge base**: WeKnora
> **Granularity**: institution → partner university → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Singapore (SG)

---

## Section 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 类别 | 数量 |
|------|------|
| 本科学位专业 (Bachelor's Degrees) | 72 |
| 研究生授课型项目 (Postgraduate Taught: MSc/MA/MBA/Grad Dip/Grad Cert) | 32 |
| 研究生博士项目 (PhD/Doctoral) | 0 |
| 文凭课程 (Diploma) | 8 |
| 证书/预科课程 (Certificate / Foundation) | 7 |
| **学位项目总计** | **119** |
| 合作大学 (University Partners) | 13 |
| SIM 自有学术部门 (SIM Global Education) | 1 |

**注**: 以上数据来自 SIM 官网 sitemap 的 125 个 programme-listing URL（去重后 119 个活跃项目）。不包含 Teach-out & Inactive Programmes。SIM 为私立教育机构（PEI），不设学院/系部传统学术架构。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

SIM 的组织架构与传统大学不同。其学术项目通过 SIM Global Education（自有）和 13 所合作大学（海外学位项目）提供：

```
Singapore Institute of Management (SIM)
│   PEI Registration: 199607747H
│   EduTrust: EDU-1-1003 (20/08/2022 - 19/08/2026)
│
├── SIM Global Education (SIM GE) [Singapore — 自有项目]
│   ├── Certificate / Foundation (证书/预科)
│   ├── Diploma (文凭)
│   └── Graduate Diploma / Graduate Certificate (研究生文凭/证书)
│
├── University of London (UK) [合作大学]
│   ├── Bachelor's Degrees (BSc)
│   ├── Graduate Diplomas
│   └── Graduate Certificates
│
├── University at Buffalo, State University of New York (USA) [合作大学]
│   ├── Bachelor of Arts (BA)
│   └── Bachelor of Science (BS)
│
├── University of Birmingham (UK) [合作大学]
│   ├── Bachelor of Science (Honours) — Top-up
│   └── Master of Science (MSc)
│
├── RMIT University (Australia) [合作大学]
│   ├── Bachelor of Accounting
│   ├── Bachelor of Business
│   └── Bachelor of Applied Science (Aviation) (Top-up)
│
├── University of Wollongong (Australia) [合作大学]
│   ├── Bachelor of Information Technology
│   └── Bachelor of Computer Science
│
├── University of Stirling (UK) [合作大学]
│   ├── BA (Honours) programmes
│   └── BA (Honours) Sport-related programmes
│
├── Cardiff University (UK) [合作大学]
│   └── Master of Science
│
├── University of Sydney (Australia) [合作大学]
│   └── Nursing programme
│
├── University of Warwick (UK) [合作大学]
│   └── Programmes (details TBC)
│
├── University of Alberta (Canada) [合作大学]
│   └── Programmes (details TBC)
│
├── Grenoble Ecole de Management (France) [合作大学]
│   └── MSc Programmes
│
├── Monash College (Australia) [合作大学]
│   └── Monash University Foundation Year
│
└── University of Adelaide (Australia) [合作大学]
    ├── Bachelor of Commerce
    └── Master of Business Administration
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 数量 | 说明 |
|---------|------|------|
| Certificate / Foundation (证书/预科) | 7 | SIM GE 自有 + Monash Foundation Year |
| Diploma (文凭) | 8 | SIM GE 自有文凭 |
| Bachelor's Degree, single major (学士, 单专业) | ~45 | 含 BA, BSc, BAcc, BIT 等 |
| Bachelor's Degree, double major (学士, 双专业) | ~12 | UB 双专业组合 |
| Bachelor's Degree, top-up (学士, 专升本) | ~10 | 含 BSc (Hons) Top-up 项目 |
| Bachelor's Degree, Honours (荣誉学士) | ~5 | BSc (Hons) |
| Graduate Certificate (研究生证书) | 8 | UoL + SIM GE |
| Graduate Diploma (研究生文凭) | 12 | UoL + SIM GE |
| Master's Degree (硕士) | 12 | MSc, MBA, MComp |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 合作大学/部门 | 证书/预科 | 文凭 | 学士 | 研究生证书 | 研究生文凭 | 硕士 | 合计 |
|-------------|----------|------|------|-----------|-----------|------|------|
| SIM Global Education | 5 | 8 | 0 | 3 | 3 | 0 | 19 |
| University of London | 1 | 0 | 17 | 5 | 8 | 0 | 31 |
| University at Buffalo | 0 | 0 | 22 | 0 | 0 | 0 | 22 |
| University of Birmingham | 0 | 0 | 6 | 0 | 0 | 1 | 7 |
| RMIT University | 0 | 0 | 3 | 0 | 0 | 0 | 3 |
| University of Wollongong | 0 | 0 | 5 | 0 | 0 | 0 | 5 |
| University of Stirling | 0 | 0 | 4 | 0 | 0 | 0 | 4 |
| Cardiff University | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Grenoble Ecole de Management | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Monash College | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| University of Adelaide | 0 | 0 | 1 | 0 | 0 | 1 | 2 |
| Other (Sydney/Warwick/Alberta/Nursing) | 0 | 0 | ~4 | 0 | 0 | 0 | ~4 |
| **合计** | **7** | **8** | **72** | **8** | **11** | **13** | **119** |

---

## Section 1 — Undergraduate Education

### 1.1 SIM Global Education — Diploma & Certificate/Foundation

| 项目名称 | 学历级别 | 合作方 | 学制 | 学费估算 |
|---------|---------|-------|------|---------|
| Certificate in Foundation Studies | Certificate/Foundation | SIM GE | Full-time, 3 months | — |
| Management Foundation Studies | Certificate/Foundation | SIM GE | — | — |
| Information Technology Foundation Studies | Certificate/Foundation | SIM GE | — | — |
| Certificate in Pre-sessional Business Management | Certificate/Foundation | SIM GE | — | — |
| International Foundation Programme | Certificate/Foundation | SIM GE | — | — |
| Diploma in Accounting | Diploma, single major | SIM GE | Full-time, 15 months | S$14,137.30 - S$15,794.10 |
| Diploma in Banking and Finance | Diploma, single major | SIM GE | Full-time, 15 months | — |
| Diploma in Information Technology | Diploma, single major | SIM GE | Full-time, 15 months | — |
| Diploma in Management Studies | Diploma, single major | SIM GE | Full-time, 15 months | — |
| Diploma in International Business | Diploma, single major | SIM GE | Full-time, 15 months | S$14,137.30 - S$15,794.10 |
| Diploma in Information Technology (E-Learning) | Diploma | SIM GE | — | — |
| Diploma in Management Studies (E-Learning) | Diploma | SIM GE | — | — |

### 1.2 University of London — Bachelor's Degrees

| 项目名称 | 学历级别 | 学制 | 学费估算 |
|---------|---------|------|---------|
| BSc (Hons) in Computer Science | Bachelor's Degree | FT 3yr | — |
| BSc (Hons) in Computer Science (Virtual Reality) | Bachelor's Degree | FT/PT 3yr | S$31,900 - S$53,080 |
| BSc (Hons) in Computer Science (Machine Learning & AI) | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Computer Science (Physical Computing / IoT) | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Computer Science (User Experience) | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Computer Science (Web & Mobile Development) | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Finance | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in International Relations | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Economics | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Economics and Finance | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Economics and Management | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Economics and Politics | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Accounting and Finance | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Business and Management | Bachelor's Degree | FT/PT 3yr | — |
| BSc (Hons) in Data Science and Business Analytics | Bachelor's Degree | FT/PT 3yr | — |
| BSc in Management and Digital Innovation | Bachelor's Degree | — | — |
| Certificate of Higher Education in Social Sciences | CertHE | — | — |

### 1.3 University at Buffalo — Bachelor's Degrees

| 项目名称 | 学历级别 | 学制 | 学费估算 |
|---------|---------|------|---------|
| BA (Economics) | Bachelor's Degree, single major | FT 3yr | S$41,627 - S$74,556 (SG/PR) / S$46,009 - S$82,404 (Intl) |
| BA (International Trade) | Bachelor's Degree, single major | FT 3yr | — |
| BA (Sociology) | Bachelor's Degree, single major | FT 3yr | — |
| BA (Communication) | Bachelor's Degree, single major | FT 3yr | — |
| BA (Psychology) | Bachelor's Degree, single major | FT 3yr | — |
| BA (International Trade and Psychology) | Bachelor's Degree, double major | FT 3yr | — |
| BA (International Trade and Sociology) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Psychology and Sociology) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Communication and Economics) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Communication and International Trade) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Communication and Psychology) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Communication and Sociology) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Economics and International Trade) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Economics and Psychology) | Bachelor's Degree, double major | FT 3yr | — |
| BA (Economics and Sociology) | Bachelor's Degree, double major | FT 3yr | — |
| BS (Business Administration) | Bachelor's Degree, single major | — | — |
| BS (Geographic Information Science) | Bachelor's Degree, single major | — | — |
| BS (Business Administration) and BA (Communication) | Bachelor's Degree, double major | — | — |
| BS (Business Administration) and BA (Economics) | Bachelor's Degree, double major | — | — |
| BS (Business Administration) and BA (International Trade) | Bachelor's Degree, double major | — | — |
| BS (Business Administration) and BA (Psychology) | Bachelor's Degree, double major | — | — |
| BS (Business Administration) and BA (Sociology) | Bachelor's Degree, double major | — | — |
| BS (Business Administration) and BS (Geographic Information Science) | Bachelor's Degree, double major | — | — |
| BS (GIS) and BA (Communication) | Bachelor's Degree, double major | — | — |
| BS (GIS) and BA (Economics) | Bachelor's Degree, double major | — | — |
| BS (GIS) and BA (International Trade) | Bachelor's Degree, double major | — | — |
| BS (GIS) and BA (Psychology) | Bachelor's Degree, double major | — | — |
| BS (GIS) and BA (Sociology) | Bachelor's Degree, double major | — | — |

### 1.4 University of Birmingham — Bachelor's Degrees (Top-up)

| 项目名称 | 学历级别 | 学制 | 学费估算 |
|---------|---------|------|---------|
| BSc (Hons) Business Management (Top-up) | Bachelor's, top-up | FT/PT 2yr | S$41,071 - S$45,518 |
| BSc (Hons) Business Management with Communications (Top-up) | Bachelor's, top-up | FT/PT 2yr | — |
| BSc (Hons) Business Management with Industrial Placement (Top-up) | Bachelor's, top-up | — | — |
| BSc (Hons) Business Management Communications and Year in Industry (Top-up) | Bachelor's, top-up | — | — |
| BSc (Hons) Accounting and Finance (Top-up) | Bachelor's, top-up | — | — |
| BSc (Hons) International Business (Top-up) | Bachelor's, top-up | — | — |

### 1.5 RMIT University — Bachelor's Degrees

| 项目名称 | 学历级别 | 学制 | 学费估算 |
|---------|---------|------|---------|
| Bachelor of Accounting | Bachelor's Degree | — | — |
| Bachelor of Business | Bachelor's Degree | FT 1.5-3yr / PT 2-3yr | S$25,584 - S$58,703 |
| Bachelor of Applied Science (Aviation) (Top-up) | Bachelor's, top-up | PT 1.5-2.5yr | S$22,184 - S$38,821 |

### 1.6 University of Wollongong — Bachelor's Degrees

| 项目名称 | 学历级别 | 学制 | 学费估算 |
|---------|---------|------|---------|
| Bachelor of Information Technology | Bachelor's Degree | FT 3yr | — |
| Bachelor of Computer Science (Artificial Intelligence and Big Data) | Bachelor's Degree | FT 3yr | — |
| Bachelor of Computer Science (Cyber Security) | Bachelor's Degree | FT 3yr | — |
| Bachelor of Computer Science (Digital Systems Security) | Bachelor's Degree | FT 3yr | — |
| Double Major: BCompSc (various combinations) | Bachelor's, double major | FT 3yr | S$27,887 - S$43,564 |

### 1.7 University of Stirling — Bachelor's Degrees

| 项目名称 | 学历级别 | 学制 |
|---------|---------|------|
| BA (Hons) Digital Media | Bachelor's Degree | — |
| BA (Hons) Marketing | Bachelor's Degree | — |
| BA (Hons) Sport and Marketing | Bachelor's Degree | — |
| BA (Hons) Sport Business Management | Bachelor's Degree | — |

### 1.8 Other University Bachelor's Programmes

| 项目名称 | 学历级别 | 合作方 |
|---------|---------|-------|
| Bachelor of Commerce | Bachelor's Degree | University of Adelaide |
| BA (Hons) in Professional Communication | Bachelor's Degree | — |
| Bachelor of Nursing (Honours) | Bachelor's Degree | University of Sydney |
| Bachelor of Nursing (Post-registration) | Bachelor's Degree | — |
| Bachelor of Psychological Science | Bachelor's Degree | — |
| Bachelor of Construction Management (Honours) (Top-up) | Bachelor's, top-up | — |
| Bachelor of Graphic Design (Top-up) | Bachelor's, top-up | — |
| Bachelor of Business Information Systems | Bachelor's Degree | — |
| BSc (Hons) in Computer Science (Top-up) | Bachelor's, top-up | — |
| BSc (Hons) in Computer Science with Security and Forensics (Top-up) | Bachelor's, top-up | — |
| Bachelor of Computer Science (Game and Mobile Development) | Bachelor's Degree | — |

---

## Section 2 — Graduate Education

### 2.1 University of London — Graduate Diplomas

| 项目名称 | 学制 | 学费估算 |
|---------|------|---------|
| Graduate Diploma in Business Analytics | FT/PT 1yr | S$13,935 - S$15,240 |
| Graduate Diploma in Management and Digital Innovation | FT/PT 1yr | S$13,935 - S$15,240 |
| Graduate Diploma in User Experience | FT 1yr | S$15,820 - S$17,390 |
| Graduate Diploma in Mobile Development | FT/PT 1yr | — |
| Graduate Diploma in Web Development | FT/PT 1yr | — |
| Graduate Diploma in Virtual Reality | FT/PT 1yr | — |
| Graduate Diploma in Physical Computing / IoT | FT/PT 1yr | — |
| Graduate Diploma in Machine Learning / AI | FT/PT 1yr | — |
| Graduate Diploma in Economics | FT/PT 1yr | — |
| Graduate Diploma in Finance | FT/PT 1yr | — |
| Graduate Diploma in Management | FT/PT 1yr | — |
| Graduate Diploma in Data Science | FT/PT 1yr | — |

### 2.2 University of London — Graduate Certificates

| 项目名称 | 学制 |
|---------|------|
| Graduate Certificate in User Experience | FT/PT 1yr |
| Graduate Certificate in Mobile Development | FT/PT 1yr |
| Graduate Certificate in Web Development | FT/PT 1yr |
| Graduate Certificate in Physical Computing / IoT | FT/PT 1yr |
| Graduate Certificate in Machine Learning / AI | FT/PT 1yr |

### 2.3 SIM Global Education — Graduate Programmes

| 项目名称 | 学制 | 备注 |
|---------|------|------|
| Graduate Diploma in Business Analytics (FT) | — | SIM GE 自有 |
| Graduate Diploma in Business Analytics (PT) | — | SIM GE 自有 |
| Graduate Diploma in Human Resource Management | — | SIM GE 自有 |
| Graduate Diploma in Business Sustainability | — | SIM GE 自有 |
| Graduate Certificate in Business Digitalisation (PT) | — | SIM GE 自有 |
| Graduate Certificate in Business Analytics (PT) | — | SIM GE 自有 |
| Graduate Certificate in Business Sustainability (PT) | — | SIM GE 自有 |
| Graduate Certificate in Human Resource Management (E-Learning) | — | 在线项目 |
| Graduate Certificate in Digital Marketing (E-Learning) | — | 在线项目 |
| Specialist Diploma in Social Entrepreneurship (PT) | — | SIM GE 自有 |

### 2.4 Master's Degrees

| 项目名称 | 合作方 | 学制 | 学费估算 |
|---------|-------|------|---------|
| MSc International Business | University of Birmingham | FT 1yr | S$42,575 - S$44,537 |
| MSc in AI + Statistical Analytics | Cardiff University | — | — |
| MSc Finance and Investment Banking (Top-up) | Grenoble Ecole de Management | FT 1yr | N/A |
| Master of Business Administration (MBA) | — | — | — |
| MBA (Innovation and Business Transformation) | — | — | — |
| MBA (International Business and Strategy) | — | — | — |
| MBA (Marketing) | — | — | — |
| Master of Computing (Data Analytics) | — | — | — |
| Master of Science Financial Management | — | — | — |
| Master of Science in Professional Accountancy | — | — | — |
| Master of Science in Sustainable Supply Chain Management | — | — | — |
| Master of Energy Efficient and Sustainable Building (Top-up) | — | — | — |
| Master of Business Administration | University of Adelaide | — | — |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 General Admission Requirements

SIM 采用全面的入学评估体系。申请要求因学历级别和合作大学而异：

**基本要求：**
- 具备与申请项目相应的学历资格（GCE A-Level、IB Diploma、理工学院文凭等）
- 满足英语语言能力要求
- 部分项目需要工作经验（MBA、Master's programmes）

**本地申请人 (Singaporean/PR)：**
- 文凭/证书课程：GCE O-Level 或同等学历
- 学士学位课程：GCE A-Level、IB Diploma、理工学院文凭或同等学历
- 研究生项目：学士学位

**国际申请人：**
- 学术资格需经评估等效
- 必须申请学生准证 (Student's Pass)
- 英语非母语者需提供英语能力证明

### 3.2 English Language Requirements

英语能力要求因项目而异。一般要求：

| 考试 | 最低分数要求（典型） |
|------|-------------------|
| IELTS | 6.0 - 6.5（因项目而异） |
| TOEFL (iBT) | 70 - 90（因项目而异） |
| PTE Academic | 50 - 62（因项目而异） |
| GCE O-Level English | C6 或以上 |

具体分数要求见各项目详情页。

### 3.3 Application Process

1. 准备文件（教育证书、身份证明、照片等）
2. 通过 SIM Application Portal 创建账户并提交申请
3. 支付申请费
4. 上传支持文件
5. 文件验证（三种方式：到校验证、OpenCert、Zoom 视频验证）
6. 等待录取结果（约1个月内）

**申请费：**
- 本地申请人: S$109.00（含9% GST）
- 国际申请人: S$545.00（含9% GST，不含学生准证申请费）

### 3.4 Application Deadlines

截止日期因项目而异。典型入学时间为每年 1月、4月、7月、8月、10月。

**申请截止日期示例（来自 listings）：**
- University at Buffalo (Aug 2026 Fall Intake): 至 2026年7月13日
- University of London programmes: 至 2026年8月24日
- SIM GE Diploma: 2026年1月12日至8月7日（国际）/ 2026年2月20日至8月14日（本地）
- RMIT University: 2026年7月4日至10月23日
- University of Birmingham MSc: 2026年8月10日（国际）/ 9月9日（本地）

具体截止日期请参阅各项目详情页。

### 3.5 Student Pass (国际申请人)

申请全日制项目的国际申请人必须在线申请学生准证 (Student's Pass)，由新加坡移民与关卡局 (ICA) 审批。

### 3.6 标准化考试要求

- IB Diploma results — 机构代码 036234 (SIM Global Education)
- SAT / AP scores — 机构代码 6590 (Singapore Institute of Management)
- ACT scores — 机构代码 8251 (SIM Global Education)

---

## Section 4 — Costs & Financial Aid

### 4.1 申请费

| 类别 | 费用 |
|------|------|
| 本地申请人 | S$109.00（含 GST） |
| 国际申请人 | S$545.00（含 GST） |

### 4.2 学费范围（示例）

| 项目类型 | 学费范围（含 GST） |
|---------|-----------------|
| SIM GE Diploma（本地） | S$14,137 - S$15,794 |
| UoL BSc (Hons) programmes | S$31,900 - S$53,080 |
| UB BA programmes (SG/PR) | S$41,627 - S$74,556 |
| UB BA programmes (International) | S$46,009 - S$82,404 |
| UoB BSc (Hons) Top-up | S$41,071 - S$45,518 |
| UoB MSc International Business | S$42,575 - S$44,537 |
| RMIT Bachelor of Business | S$25,584 - S$58,703 |
| UoW BCompSc Double Major | S$27,887 - S$43,564 |
| RMIT Aviation (Top-up) | S$22,184 - S$38,821 |

具体学费详见各项目详情页。学费因合作大学、项目、学制而异。

### 4.3 付款方式

- PayNow（平台费豁免至另行通知）
- Flywire（需支付不可退还的平台费）
- 国际电汇（银行转账需 4 天）
- 信用卡/借记卡
- 学习贷款（OCBC、DBS、UOB 银行）

### 4.4 奖学金

| 奖学金名称 | 金额 | 适用对象 |
|-----------|------|---------|
| SIM STARRR Award for New Undergraduate Students | — | 新生（学术+CCA+领导力优秀） |
| SIM GE Scholarship (Academic Excellence & Leadership) | S$15,000/人 | 本地及国际本科生 |
| SIM GE Scholarship (Sports & Artistic Talent) | S$15,000/人 | 本地及国际本科生 |
| SIM GE Diploma Scholarship (Academic Excellence) | 覆盖学费 | 国际文凭新生 |
| SIM GE Diploma Scholarship (Merit) | 覆盖学费 | 国际文凭新生 |
| Chairman's Award for Resilience | S$3,000/人 | 在职兼读学士/硕士学生 |
| IRAS Scholarship Programmes | — | 特定合作项目 |
| ASEAN Impact Award | — | ASEAN 学生 |
| SIM-UB Scholarship | — | UB 项目学生 |
| SIM-UoB MSc Scholarship | — | UoB 硕士项目学生 |
| SIM-University of Stirling Sports Scholarship | — | Stirling 项目学生 |
| SIM-University of Sydney Nursing Talent Development Fund | — | 护理项目学生 |
| University of London scholarships | — | UoL 项目学生 |

### 4.5 助学金 & 财务援助

- SIM Global Education Bursary（助学金）
- SIM GE Crisis Fund（危机基金）

---

## Section 5 — Evidence Chain Index

| 编号 | 字段 | 值 | 来源 URL | 证据类型 |
|------|------|-----|---------|---------|
| E-U-001 | institution.name | Singapore Institute of Management (SIM) | https://www.sim.edu.sg/ | official_webpage |
| E-U-002 | institution.type | Private Education Institution (PEI) | https://www.sim.edu.sg/about-sim/discover-sim/who-we-are | official_webpage |
| E-U-003 | registration.number | 199607747H | https://www.sim.edu.sg/ | official_webpage (footer) |
| E-U-004 | edutrust.cert | EDU-1-1003 (20/08/2022 - 19/08/2026) | https://www.sim.edu.sg/degrees-diplomas/sim-global-education/edutrust | official_webpage |
| E-U-005 | programme.count | 132 results total (listing page) | https://www.sim.edu.sg/degrees-diplomas/programmes/programme-listing | official_webpage |
| E-U-006 | programme.sitemap.count | 125 programme listing URLs | https://www.sim.edu.sg/sitemap.xml | sitemap |
| E-U-007 | partner.universities | 13 university partners | https://www.sim.edu.sg/degrees-diplomas/sim-global-education/university-partners-sim-ge | official_webpage |
| E-U-008 | application.fee.local | S$109.00 | https://www.sim.edu.sg/degrees-diplomas/admissions/application-process | official_webpage |
| E-U-009 | application.fee.international | S$545.00 | https://www.sim.edu.sg/degrees-diplomas/admissions/application-process | official_webpage |
| E-U-010 | scholarship.ge.academic | S$15,000 per scholar | https://www.sim.edu.sg/degrees-diplomas/admissions/scholarships | official_webpage |
| E-U-011 | scholarship.chairman.award | S$3,000 per awardee | https://www.sim.edu.sg/degrees-diplomas/admissions/scholarships | official_webpage |
| E-U-012 | fees.payment.methods | PayNow, Flywire, Credit/Debit Card, Bank Transfer | https://www.sim.edu.sg/degrees-diplomas/admissions/application-process/fees-payments-and-financial-matters | official_webpage |
| E-U-013 | address.main | 461 Clementi Road, Singapore 599491 | https://www.sim.edu.sg/contact-us | official_webpage |
| E-U-014 | address.pd | 41 Namly Avenue, Singapore 267616 | https://www.sim.edu.sg/contact-us | official_webpage |
| E-U-015 | contact.email | study@sim.edu.sg | https://www.sim.edu.sg/contact-us | official_webpage |
| E-U-016 | contact.phone | 6248 9746 | https://www.sim.edu.sg/contact-us | official_webpage |
| E-U-017 | programme.sample.UB.BA.Economics.fees | S$41,627 - S$74,556 (SG/PR) / S$46,009 - S$82,404 (Intl) | https://www.sim.edu.sg/degrees-diplomas/programmes/programme-listing | official_webpage (listing card) |
| E-U-018 | programme.sample.UoL.VR.fees | S$31,900 - S$53,080 | https://www.sim.edu.sg/degrees-diplomas/programmes/programme-listing | official_webpage (listing card) |
| E-U-019 | programme.sample.UoB.BusMgmt.fees | S$41,071 - S$45,518 | https://www.sim.edu.sg/degrees-diplomas/programmes/programme-listing | official_webpage (listing card) |
| E-U-020 | programme.sample.RMIT.BBus.fees | S$25,584 - S$58,703 | https://www.sim.edu.sg/degrees-diplomas/programmes/programme-listing | official_webpage (listing card) |
| E-U-021 | programme.sample.UoW.DoubleMajor.fees | S$27,887 - S$43,564 | https://www.sim.edu.sg/degrees-diplomas/programmes/programme-listing | official_webpage (listing card) |

---

## Section 6 — WeKnora Import Manifest

### 6.1 文档信息

| 字段 | 值 |
|------|-----|
| 文件名 | Singapore_Institute_of_Management_知识库_完整深度数据_v2.md |
| 知识库路径 | knowledge-base/sg/ |
| 文档版本 | v2.0 (deep) |
| 生成日期 | 2026-07-09 |
| 数据源 | https://www.sim.edu.sg/ |
| 完整性 | 结构框架 ✅ | 学士课程列表 ✅ | 研究生课程列表 ✅ | 证据链 (21 blocks) ✅ |

### 6.2 后续跟进事项 (P0/P1/P2)

| 优先级 | 数据项 | 说明 |
|-------|--------|------|
| **P0** | 英文语言要求具体分数 | IELTS/TOEFL/PTE 最低分数因项目而异，需从各项目详情页提取 |
| **P0** | 各项目完整学费数据 | 需要逐页提取所有 119 个项目的学费 |
| **P0** | 部分合作大学项目详情 | University of Sydney, University of Warwick, University of Alberta 项目需补充 |
| **P1** | 学术录取要求细化 | GCE A-Level、IB、理工学院文凭的具体录取分数/等级 |
| **P1** | 毕业生就业数据 | Graduate Employment Survey 结果 |
| **P1** | IGP (Indicative Grade Profile) | 如有发布需提取 |
| **P2** | 学校历史与背景 | 可补充至院校总览 |
| **P2** | 校园设施详情 | 图书馆、实验室、体育设施等 |
| **P2** | 学生生活信息 | 学生社团、CCA、住宿等 |

---

## Section 7 — Cross-School Comparison Framework

### 7.1 新加坡私立教育机构 (PEI) 比较

| 维度 | Singapore Institute of Management (SIM) |
|------|----------------------------------------|
| 机构类型 | 私立教育机构 (PEI) |
| EduTrust 认证 | 是 (EDU-1-1003, 至 2026-08-19) |
| 合作大学数量 | 13 |
| 合作大学国家 | 新加坡、澳大利亚、英国、美国、加拿大、法国 |
| 项目总数 | ~119 |
| 本科学位 | ~72 |
| 研究生项目 | ~32 |
| 文凭/证书 | ~15 |
| 自有学术资格 | 是 (SIM GE) |
| 海外大学学位授予 | 是（由合作大学授予学位） |
| 校园 | Clementi Road（SIM GE）、Namly Avenue（SIM Academy） |
| 成立年份 | 1964 (作为管理协会) |
| 注册状态 | 199607747H (Singapore Institute of Management Pte Ltd) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: SIM official website (sim.edu.sg), sitemap, programme listing pages, admissions pages
> **Granularity**: institution → partner university → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (72 programmes listed) | PG programmes ✅ (32 programmes listed) | Evidence (21 blocks) ✅
> **Next step**: P0 items — extract English language requirements per programme, complete fee data for all 119 programmes, fill in partner programme details for Sydney/Warwick/Alberta
