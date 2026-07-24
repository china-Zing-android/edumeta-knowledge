# University of Prince Edward Island 知识库 — 完整深度数据 v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Prince Edward Island)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~70+ 个专业/方向（含 majors, minors, specializations, honours） |
| 研究生授课型项目 (PGT: MA/MSc/MBA/MEd/MN/MGA) | ~12 个硕士项目 |
| 研究生博士项目 (PhD/Doctoral) | 6 个博士项目 |
| 证书项目 (Certificate) | ~8 个证书项目 |
| 学院 (Faculties) | 8 大学院 + 研究生院 |
| 学术院系 (Academic Departments) | 生物学、化学、计算机科学、数学、物理、心理学、经济学、英语、历史、哲学、政治学、社会学/人类学、现代语言等 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Prince Edward Island (UPEI)
├── Faculty of Arts
│   ├── Acadian Studies (BA)
│   ├── Anthropology (BA)
│   ├── Applied Arts in Journalism (BA)
│   ├── Applied Communication, Leadership, and Culture (BA)
│   ├── Asian Studies (BA)
│   ├── Bachelor of Applied Arts in Journalism (BA)
│   ├── Bachelor of Integrated Studies (BIS)
│   ├── Bachelor of Music (BMus)
│   ├── Bachelor of Music Education (BMusEd)
│   ├── Canadian Studies (BA)
│   ├── Catholic Studies (BA)
│   ├── Christian Studies (BA)
│   ├── Classics (BA)
│   ├── Diversity and Social Justice Studies (BA)
│   ├── Economics (BA)
│   ├── English (BA)
│   ├── Fine Arts (BA)
│   ├── French (BA)
│   ├── History (BA)
│   ├── Indigenous Studies (BA major/minor)
│   ├── International Studies (BA)
│   ├── Island Studies (BA)
│   ├── Journalism (BA)
│   ├── Korean Studies (BA)
│   ├── Medieval and Renaissance Studies (BA)
│   ├── Modern Languages (BA)
│   ├── Music (BA, BMus)
│   ├── Philosophy (BA)
│   ├── Political Science (BA)
│   ├── Psychology (BA)  — shared with Science
│   ├── Religious Studies (BA)
│   ├── Social Studies of Science (BA)
│   ├── Sociology (BA)
│   ├── Sociology/Anthropology (BA)
│   ├── Spanish (BA)
│   ├── Theatre Studies (BA)
│   ├── University Writing (BA)
│   └── Doctor of Psychology (PsyD) — Graduate
├── Faculty of Business
│   ├── Accelerated Bachelor of Business Administration (BBA)
│   ├── Bachelor of Business Administration (BBA)
│   ├── Bachelor of Business in Tourism and Hospitality (BBTH)
│   ├── Bachelor of Business Studies (BBS)
│   ├── Accounting (Certificate)
│   ├── Business (Certificate)
│   ├── Public Administration (Certificate)
│   ├── Executive Master of Business Administration (EMBA) — Graduate
│   ├── Master of Business Administration (MBA) — Graduate
│   └── Master of Business Administration in Global Leadership (MBA GL) — Graduate
├── Faculty of Education
│   ├── Bachelor of Education (BEd)
│   ├── Bachelor of Education - Français Langue Seconde (BEd)
│   ├── Adult Education (Certificate)
│   ├── Certificate in Adult Education (CAE)
│   ├── Certificate in Educational Leadership (Nunavut)
│   ├── Master of Education in Leadership in Learning (MEd) — Graduate
│   └── Doctor of Philosophy in Educational Studies (PhD) — Graduate
├── Faculty of Science
│   ├── Actuarial Science (BSc)
│   ├── Analytics (BSc)
│   ├── Applied Climate Change and Adaptation (BSc)
│   ├── Bachelor of Applied Health Science in Paramedicine (BSc)
│   ├── Bachelor of Applied Science in Radiography (BSc)
│   ├── Bachelor of Environmental Studies (BES)
│   ├── Bachelor of Science in Biotechnology (BSc)
│   ├── Bachelor of Wildlife Conservation (BSc)
│   ├── Biology (BSc)
│   ├── Biotechnology (BSc)
│   ├── Chemistry (BSc)
│   ├── Computer Science (BSc)
│   ├── Environmental Studies (BSc)
│   ├── Financial Mathematics (BSc)
│   ├── Foods and Nutrition (BSc)
│   ├── Kinesiology (BSc)
│   ├── Mathematics (BSc)
│   ├── Medical and Biological Physics (BSc)
│   ├── Physics (BSc)
│   ├── Pre-veterinary Medicine Stream (BSc)
│   ├── Psychology (BSc) — shared with Arts
│   ├── Radiography (BSc)
│   ├── Statistics (BSc)
│   ├── Wildlife Conservation (BSc)
│   ├── Dietetic Internship (Foods and Nutrition) (Certificate)
│   ├── Master of Applied Health Services Research (MSc) — Graduate
│   ├── Master of Science - Environmental Sciences (MSc) — Graduate
│   ├── Master of Science - Human Biology (MSc) — Graduate
│   ├── Master of Science - Molecular and Macromolecular Sciences (MSc) — Graduate
│   ├── Master of Science, Mathematical and Computational Sciences (MSc) — Graduate
│   ├── PhD in Environmental Sciences (PhD) — Graduate
│   ├── PhD in Molecular and Macromolecular Sciences (PhD) — Graduate
│   └── Environmental Sciences (PhD) — Graduate
├── Faculty of Nursing
│   ├── Accelerated Bachelor of Science in Nursing (BScN)
│   ├── Bachelor of Science in Nursing (BScN)
│   ├── Master of Nursing (MN) — Graduate
├── Faculty of Sustainable Design Engineering
│   ├── Bachelor of Science in Sustainable Design Engineering (BSc)
│   ├── Engineering (BSc)
│   ├── Master of Science, Sustainable Design Engineering (MSc) — Graduate
│   └── Doctor of Philosophy in Sustainable Design Engineering (PhD) — Graduate
├── Faculty of Veterinary Medicine (Atlantic Veterinary College)
│   ├── Doctor of Veterinary Medicine (DVM)
│   ├── Master of Science in Veterinary Medicine (MSc) — Graduate
│   ├── Master of Veterinary Science (MVSc) — Graduate
│   └── Doctor of Philosophy in Veterinary Medicine (PhD) — Graduate
├── Faculty of Indigenous Knowledge, Education, Research, and Applied Studies
│   ├── Indigenous Studies (major) — shared with Arts
│   └── Indigenous Studies (minor)
├── Graduate Studies (跨学院)
│   ├── Master in Global Affairs (MGA)
│   ├── Master of Cleantech Leadership and Transformation
│   ├── Master of Arts in Island Studies (MAIS)
│   ├── Global Affairs (Master in)
│   └── various PhD programs listed under respective faculties
└── Pre-professional Programs
    ├── Pre-veterinary Medicine Stream
    └── Pre-medicine / Health Professions preparation
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 缩写 | 数量 |
|---------|------|------|
| Bachelor of Arts | BA | 30+ 专业领域 |
| Bachelor of Science | BSc | 20+ 专业领域 |
| Bachelor of Business Administration | BBA | 3 (含加速) |
| Bachelor of Business in Tourism and Hospitality | BBTH | 1 |
| Bachelor of Business Studies | BBS | 1 |
| Bachelor of Education | BEd | 2 |
| Bachelor of Music | BMus | 1 |
| Bachelor of Music Education | BMusEd | 1 |
| Bachelor of Science in Nursing | BScN | 2 (含加速) |
| Bachelor of Applied Arts in Journalism | BA (Applied) | 1 |
| Bachelor of Applied Health Science in Paramedicine | BSc | 1 |
| Bachelor of Applied Science in Radiography | BSc | 1 |
| Bachelor of Environmental Studies | BES | 1 |
| Bachelor of Science in Biotechnology | BSc | 1 |
| Bachelor of Science in Sustainable Design Engineering | BSc | 1 |
| Bachelor of Wildlife Conservation | BSc | 1 |
| Bachelor of Integrated Studies | BIS | 1 |
| Doctor of Veterinary Medicine | DVM | 1 |
| Doctor of Psychology | PsyD | 1 (graduate) |
| Master of Arts | MA | 1 (Island Studies) |
| Master of Science | MSc | 6+ 方向 |
| Master of Business Administration | MBA | 3 (含EMBA, Global Leadership) |
| Master of Education | MEd | 1 |
| Master of Nursing | MN | 1 |
| Master in Global Affairs | MGA | 1 |
| Master of Veterinary Science | MVSc | 1 |
| Master of Cleantech Leadership and Transformation | MCLT | 1 |
| Doctor of Philosophy | PhD | 6 (教育、工程、环境、分子大分子、兽医医学) |
| Certificate | Cert | ~8 (会计、成人教育、商业、公共管理、饮食实习) |

### 0.4 本科 / 研究生分布矩阵 (Rule 4 — distribution matrix)

| 学院 | 本科项目 | 硕士项目 | 博士项目 | 证书项目 |
|------|---------|---------|---------|---------|
| Arts | ~25 | 2 (MAIS, PsyD) | 0 | 0 |
| Business | 4 | 3 (MBA/EMBA/GL) | 0 | 3 |
| Education | 2 | 1 (MEd) | 1 (PhD) | 3 |
| Science | ~18 | 6 (MSc) | 3 (PhD) | 1 |
| Nursing | 2 | 1 (MN) | 0 | 0 |
| Sustainable Design Engineering | 2 | 1 (MSc) | 1 (PhD) | 0 |
| Veterinary Medicine | 1 (DVM) | 3 (MSc/MVSc) | 1 (PhD) | 0 |
| Indigenous Knowledge | 1 (shared) | 0 | 0 | 0 |
| Graduate Studies (跨学院) | 0 | 2 (MGA, MCLT) | 0 | 0 |

---

## Section 1 — 本科招生 (Undergraduate Admissions)

### 1.1 一般入学要求 (General Admission Requirements)

**加拿大高中生：**
- 完成12年基础教育，获得高中文凭
- 满足所申请专业的特定课程前置要求
- 参考 UPEI Academic Calendar 获取完整录取标准

**加拿大高中成绩等效对照表：** 详见 [Canadian High School Equivalency Chart](https://www.upei.ca/admission-requirements/undergraduate-admissions)

**不同省份要求：**
- PEI 高中：English 621 课程需达到70%可作为英语能力证明
- 其他加拿大省份：equivalent Grade 12 academic English course

**录取类型：**
- 正常录取 (Regular Admission)
- 重新录取 (Re-admission)
- 转学 (Transfer Agreements)
- CEGEP (魁北克)
- 国际文凭 (International Baccalaureate)
- 先修课程 (Advanced Placement)
- Gateway Program
- Concurrent Enrolment (PEI 12年级双学分)

### 1.2 国际学生入学要求 (International Admission Requirements)

**基本要求：**
- 完成12年初等和中等教育，获得高中文凭
- 或 Senior Secondary Certificate / Higher Secondary School Certificate
- 或其他同等学历证明
- 满足最低入学资格不保证录取（竞争性录取）

**按国家具体要求：** 涵盖100+个国家/地区（详见 [Country-specific Requirements](https://www.upei.ca/admission-requirements/country-specific-requirements)）

**主要国家要求示例：**

| 国家/地区 | 最低要求 |
|----------|---------|
| 中国 (China) | 11-12年级5门学术科目均分70-80%，或会考平均B |
| 印度 (India) | Standard XII 5门学术科目最低70%（CBSE/CISCE） |
| 美国 (USA) | 官方高中文凭/成绩单，最低GPA 2.8/4.0，4门大学预备课程 |
| 英国 (UK) | GCSE 5门O-Level课程C以上 + 2门A-Level C以上 |
| 香港 (HK) | HKDSE 至少5门学术科目（含英语、数学/科学，视专业） |
| 台湾 (Taiwan) | 高中毕业证+会考，必修科目平均B |
| 韩国 (South Korea) | 高中毕业证，至少70%/B以上 |
| 日本 (Japan) | 高中毕业证，最低3/5（通常要求更高） |
| 巴基斯坦 (Pakistan) | Intermediate/Higher Secondary Certificate, 65-70%以上 |
| 孟加拉国 (Bangladesh) | HSC/SSC，至少Second Division |
| 伊朗 (Iran) | Diplom-Metevaseth 14-15/20 |
| 尼日利亚 (Nigeria) | WAEC SSCE (需在线验证)，最低3分 |
| 加纳 (Ghana) | WAEC SSSCE，最低3分 |
| 肯尼亚 (Kenya) | KCSE 最低C+ |
| 巴西 (Brazil) | Certificado de Conclusão do 2 Grau/Ensino Médio |

### 1.3 英语语言能力要求 (English Language Proficiency Requirements)

**Undergraduate Programs — 标准要求：**

| 考试类型 | Arts, Science, Business, Engineering | Nursing, Radiography, DVM, Education |
|---------|--------------------------------------|--------------------------------------|
| IELTS (Academic) | Overall 6.5, no band below 6.0 | Overall 7.0 (writing & speaking 7.0, reading & listening 6.5) |
| TOEFL iBT | 80+ (写作最低21) | 100+ |
| TOEFL PBT | 550 (TWE 5.5) | 600 (TWE 6) |
| CAEL | 60 | 70 |
| PTE Academic | 58 | 66 |
| Cambridge (B2/C1/C2) | Overall 176 (writing 176, others ≥169) | Overall 185 (writing & speaking 185, others 176) |
| Duolingo | Overall 120 (Literacy 115, Comprehension 115, Conversation 115, Production 115) | 同左 |
| Oxford ELLT | Overall 7 (no component below 6) | Overall 7 (writing & speaking 8, reading & listening 7) |
| GTEC CBT | 1176–1250 | 1250+ |
| English 621 (PEI高中课程) | 70% | N/A |
| CanTEST | **UPEI不接受** Holland College的CanTEST成绩 | — |

**豁免条件：**
- 在加拿大或其他英语为主要语言的国家完成3年全日制英语学习
- 在加拿大以非英语语言接受教育但能证明双语能力者也可接受

**有条件录取 (Conditional Admission)：**
- 成绩低于最低标准者可能有条件录取（Nursing, Radiography, Education, DVM除外）
- 条件清除方式：重新考试 或 参加 UPEI English Academic Preparation (EAP) 课程 + 部分学分课程

### 1.4 申请流程 (Application Process)

**申请步骤：**
1. 创建 UPEI 账户 或 登录已有账户
2. 完成在线申请表
3. 缴纳申请费并提交申请
4. 提交成绩单和支持文件
5. 查看申请状态

**申请费：**
- 加拿大国内申请人：$75 CAD
- 国际申请人：$100 CAD
- 兽医医学项目：$75 CAD

**成绩单提交方式：**
- MyCreds/MesCertif/My eQuals/Digitary CORE 电子共享
- 邮件：registrar@upei.ca（需学校直接发送）
- 邮寄：UPEI Registrar's Office, 550 University Avenue, Charlottetown, PE, C1A 4P3
- 传真：902-566-0795

**处理时间：** 5-10个工作日

**联系方式：**
- 申请咨询：apply@upei.ca
- 电话：1-800-606-8734
- 国际学生咨询：inte@upei.ca

---

## Section 2 — 研究生招生 (Graduate Admissions)

### 2.1 硕士项目列表 (Graduate Taught/Research Programs)

| 项目名称 | 学院 | 类型 |
|---------|------|------|
| Master of Arts in Island Studies (MAIS) | Arts | Thesis/Course |
| Master in Global Affairs (MGA) | Graduate Studies | Course |
| Master of Business Administration (MBA) | Business | Course |
| Executive MBA (EMBA) | Business | Course |
| MBA in Global Leadership | Business | Course |
| Master of Education in Leadership in Learning (MEd) | Education | Course |
| Master of Nursing (MN) | Nursing | Course |
| Master of Applied Health Services Research | Science | Thesis |
| MSc - Environmental Sciences | Science | Thesis |
| MSc - Human Biology | Science | Thesis |
| MSc - Molecular and Macromolecular Sciences | Science | Thesis |
| MSc, Mathematical and Computational Sciences | Science | Thesis |
| MSc, Sustainable Design Engineering | Engineering | Thesis |
| MSc in Veterinary Medicine | Veterinary Medicine | Thesis |
| Master of Veterinary Science (MVSc) | Veterinary Medicine | Course/Thesis |
| Master of Cleantech Leadership and Transformation | Graduate Studies | Course |
| Doctor of Psychology (PsyD) | Arts | Professional |

### 2.2 博士项目列表 (PhD Programs)

| 项目名称 | 学院 |
|---------|------|
| Doctor of Philosophy in Educational Studies | Education |
| Doctor of Philosophy in Sustainable Design Engineering | Engineering |
| Doctor of Philosophy in Veterinary Medicine | Veterinary Medicine |
| PhD in Environmental Sciences | Science |
| PhD in Molecular and Macromolecular Sciences | Science |

---

## Section 3 — 学费与费用 (Tuition and Fees)

### 3.1 学费概览 (2026–2027 Academic Year)

> UPEI 使用交互式学费选择器 (Tuition and Fees Selector)，以下数据通过官方页面采集。

**申请费 (Application Fees):**
- 加拿大国内申请人：$75 CAD
- 国际申请人：$100 CAD
- DVM 项目：$75 CAD

**英语学术准备课程 (EAP):**
- 全日制国内 EAP：$9,491 CAD
- 全日制国际 EAP：$19,881 CAD
- 非全日制国内 EAP：$813/门课
- 非全日制国际 EAP：$1,785/门课

**其他学术费用:**
- 旁听课 (3学时)：$517 CAD
- 课程型 PLAR：$407 CAD
- 项目型 PLAR：$814 CAD
- 学生成功项目：$658 CAD

**服务费:**
- 挑战考试 (Challenge Exam)：$406 CAD
- 特殊学分评估：$406 CAD
- 逾期缴费（秋冬学期）：$60/$30 CAD
- 逾期缴费（夏季学期）：$25 CAD
- NSF 退票管理费：$20 CAD
- 全日制恢复学籍：$50 CAD
- 非全日制恢复学籍：$25 CAD

### 3.2 缴费截止日期 (Payment Deadlines)

| 学期 | 截止日期 |
|------|---------|
| Fall Term 2026 | 2026年9月22日星期二下午4:00 |
| Winter Term 2027 | 2027年1月26日星期二下午4:00 |
| Summer Term | 参照 myUPEI 各课程具体日期 |

**注意事项：**
- 未按时缴费可能被取消课程注册
- 可申请 "Permission to Pay Later" 表格
- 逾期缴费将产生滞纳金

### 3.3 奖学金与助学金 (Scholarships and Awards)

- UPEI 每年发放超过 $1,450万 加元的奖学金和助学金
- **保证入学奖学金 (Guaranteed Entrance Scholarships)**：根据入学成绩自动评估
- **学术卓越奖 (Academic Excellence Awards)**
- **George Coles Bursary**：PEI 居民本科首学位，最高 $3,500/年
- **Island Advantage Bursary**：基于经济需求的 PEI 学生补助
- **Marion L. Reid Grant**：PEI 居民医疗保健项目学生，最高 $12,800
- **国际入学奖 (International Entrance Award)**
- **国际学生紧急助学金 (Emergency International Student Bursary)**
- 申请截止日期：第一学期奖 cycle — 10月1日；第二学期 — 2月1日

---

## Section 4 — 重要日期与截止日期 (Important Dates & Deadlines)

### 4.1 学年安排

| 学期 | 大致时间 |
|------|---------|
| Fall Term | 9月 – 12月 |
| Winter Term | 1月 – 4月 |
| Summer Term | 5月 – 8月 |

### 4.2 申请截止日期

**国际学生本科申请：**
- 非竞争性项目的国际申请人截止日期每年确定，联系 inte@upei.ca 获取信息
- 由于签证申请时间、住宿和项目容量的考虑

**奖学金申请：**
- 第一学期奖 cycle：10月1日
- 第二学期奖 cycle：2月1日
- 保证入学奖学金：自动评估

---

## Section 5 — 学校特色与关键指标 (Key Metrics & Highlights)

### 5.1 关键数据

| 指标 | 数据 |
|------|------|
| 全日制学生与教师比 | 18:1 |
| 国际学生代表国家数 | 90+ 国家 |
| 年度奖学金和助学金总额 | $1,450万+ CAD |
| 合作交换项目 | 60+ 项目覆盖27个国家 |
| 校区 | 3个（Charlottetown主校区, Cairo, St. Peter's） |

### 5.2 学校特色

- **小班教学**：个性化学习体验，师生比18:1
- **Atlantic Veterinary College (AVC)**：加拿大五大兽医学院之一
- **可持续设计工程学院**：加拿大领先的工程设计教育
- **位置**：位于加拿大爱德华王子岛省夏洛特敦市
- **校园**：主校区位于 550 University Ave, Charlottetown, PE C1A 4P3

### 5.3 学院列表 (Faculties)

1. Faculty of Arts (文学院)
2. Faculty of Business (商学院)
3. Faculty of Education (教育学院)
4. Faculty of Science (理学院)
5. Faculty of Nursing (护理学院)
6. Faculty of Sustainable Design Engineering (可持续设计工程学院)
7. Faculty of Veterinary Medicine / Atlantic Veterinary College (兽医学院)
8. Faculty of Indigenous Knowledge, Education, Research, and Applied Studies (原住民知识学院)
9. Graduate Studies (研究生院)

---

## Section 6 — 全部项目完整列表 (Full Program Leaf List)

### 本科项目 (Undergraduate Programs)

| 项目名称 | 所属学院 | 学历 |
|---------|---------|------|
| Acadian Studies | Arts | BA |
| Accelerated Bachelor of Business Administration | Business | BBA |
| Accelerated Bachelor of Science in Nursing | Nursing | BScN |
| Actuarial Science | Science | BSc |
| Analytics | Science | BSc |
| Anthropology | Arts | BA |
| Applied Arts in Journalism | Arts | BA |
| Applied Climate Change and Adaptation | Science | BSc |
| Applied Communication, Leadership, and Culture | Arts | BA |
| Asian Studies | Arts | BA |
| Bachelor of Applied Arts in Journalism | Arts | BA |
| Bachelor of Applied Health Science in Paramedicine | Science | BSc |
| Bachelor of Applied Science in Radiography | Science | BSc |
| Bachelor of Business Administration | Business | BBA |
| Bachelor of Business in Tourism and Hospitality | Business | BBTH |
| Bachelor of Business Studies | Business | BBS |
| Bachelor of Education | Education | BEd |
| Bachelor of Education - Français Langue Seconde | Education | BEd |
| Bachelor of Environmental Studies | Science | BES |
| Bachelor of Integrated Studies | Arts | BIS |
| Bachelor of Music | Arts | BMus |
| Bachelor of Music Education | Arts | BMusEd |
| Bachelor of Science in Biotechnology | Science | BSc |
| Bachelor of Science in Nursing | Nursing | BScN |
| Bachelor of Science in Sustainable Design Engineering | Engineering | BSc |
| Bachelor of Wildlife Conservation | Science | BSc |
| Biology | Science | BSc |
| Biotechnology | Science | BSc |
| Canadian Studies | Arts | BA |
| Catholic Studies | Arts | BA |
| Chemistry | Science | BSc |
| Christian Studies | Arts | BA |
| Classics | Arts | BA |
| Computer Science | Science | BSc |
| Diversity and Social Justice Studies | Arts | BA |
| Doctor of Veterinary Medicine (DVM) | Veterinary Medicine | DVM |
| Economics | Arts | BA |
| Engineering | Engineering | BSc |
| English | Arts | BA |
| Environmental Studies | Science | BES |
| Financial Mathematics | Science | BSc |
| Fine Arts | Arts | BA |
| Foods and Nutrition | Science | BSc |
| French | Arts | BA |
| History | Arts | BA |
| Indigenous Studies (major) | Indigenous/Arts | BA |
| Indigenous Studies (minor) | Indigenous | Minor |
| Integrated Studies | Arts | BIS |
| International Studies | Arts | BA |
| Island Studies | Arts | BA |
| Kinesiology | Science | BSc |
| Korean Studies | Arts | BA |
| Mathematics | Science | BSc |
| Medical and Biological Physics | Science | BSc |
| Medieval and Renaissance Studies | Arts | BA |
| Modern Languages | Arts | BA |
| Music (BA) | Arts | BA |
| Nursing | Nursing | BScN |
| Paramedicine | Science | BSc |
| Philosophy | Arts | BA |
| Physics | Science | BSc |
| Political Science | Arts | BA |
| Pre-veterinary Medicine Stream | Science | BSc |
| Psychology | Arts/Science | BA/BSc |
| Radiography | Science | BSc |
| Religious Studies | Arts | BA |
| Social Studies of Science | Arts | BA |
| Sociology | Arts | BA |
| Sociology/Anthropology | Arts | BA |
| Spanish | Arts | BA |
| Statistics | Science | BSc |
| Sustainable Design Engineering | Engineering | BSc |
| Theatre Studies | Arts | BA |
| University Writing | Arts | BA |
| Wildlife Conservation | Science | BSc |

### 证书项目 (Certificate Programs)

| 项目名称 | 所属学院 |
|---------|---------|
| Accounting (Certificate) | Business |
| Adult Education (Certificate) | Education |
| Business (Certificate) | Business |
| Certificate in Accounting | Business |
| Certificate in Adult Education (CAE) | Education |
| Certificate in Business | Business |
| Certificate in Educational Leadership (Nunavut) | Education |
| Dietetic Internship (Foods and Nutrition) | Science |
| Public Administration (Certificate) | Business |

### 研究生项目 (Graduate Programs)

| 项目名称 | 所属学院 | 类型 |
|---------|---------|------|
| Master in Global Affairs | Graduate Studies | Master |
| Master of Applied Health Services Research | Science | MSc |
| Master of Arts in Island Studies | Arts | MA |
| Master of Business Administration | Business | MBA |
| Master of Business Administration in Global Leadership | Business | MBA |
| Master of Cleantech Leadership and Transformation | Graduate Studies | Master |
| Master of Education in Leadership in Learning | Education | MEd |
| Master of Nursing | Nursing | MN |
| MSc - Environmental Sciences | Science | MSc |
| MSc - Human Biology | Science | MSc |
| MSc - Molecular and Macromolecular Sciences | Science | MSc |
| MSc in Veterinary Medicine | Veterinary Medicine | MSc |
| MSc, Mathematical and Computational Sciences | Science | MSc |
| MSc, Sustainable Design Engineering | Engineering | MSc |
| Master of Veterinary Science | Veterinary Medicine | MVSc |
| Executive Master of Business Administration | Business | EMBA |
| Doctor of Psychology (PsyD) | Arts | PsyD |
| PhD in Educational Studies | Education | PhD |
| PhD in Environmental Sciences | Science | PhD |
| PhD in Molecular and Macromolecular Sciences | Science | PhD |
| PhD in Sustainable Design Engineering | Engineering | PhD |
| PhD in Veterinary Medicine | Veterinary Medicine | PhD |

---

## Section 7 — 关键信息源与证据链 (Evidence Chain & Source Mapping)

| 数据类别 | 来源URL | 采集方法 |
|---------|--------|---------|
| 首页/院校总览 | https://www.upei.ca/ | browser_navigate |
| 全部项目列表 | https://www.upei.ca/programs | browser_navigate + browser_console (JS提取) |
| 申请流程 | https://www.upei.ca/apply | browser_navigate + browser_snapshot |
| 本科招生要求 | https://www.upei.ca/admission-requirements/undergraduate-admissions | browser_navigate + browser_snapshot |
| 英语语言要求 | https://www.upei.ca/admission-requirements/english-language-proficiency-requirements/undergraduate-programs | browser_navigate + browser_snapshot |
| 各国入学要求 | https://www.upei.ca/admission-requirements/country-specific-requirements | browser_navigate + browser_console (text提取) |
| 国际学生信息 | https://www.upei.ca/international-students | browser_navigate + browser_snapshot |
| 国际学生申请前须知 | https://www.upei.ca/international-students/before-you-apply | browser_navigate + browser_snapshot |
| 学费与费用 | https://www.upei.ca/fees | browser_navigate + browser_snapshot |
| 其他费用 | https://www.upei.ca/fees/other-fees | browser_navigate + browser_snapshot |
| 缴费截止日期 | https://www.upei.ca/fees/deadlines | browser_navigate + browser_snapshot |
| 财务援助 | https://www.upei.ca/fees/financial-aid | browser_navigate + browser_snapshot |
| 奖学金与奖项 | https://www.upei.ca/scholarships-and-awards | browser_navigate + browser_snapshot |
| 项目详情示例(生物) | https://www.upei.ca/programs/biology | browser_navigate + browser_snapshot |

---

## Section 8 — 数据监控与更新建议 (Monitoring & Update Design)

| 数据点 | 建议更新频率 | 监控方式 |
|--------|------------|---------|
| 项目列表 | 每学期 | 检查 https://www.upei.ca/programs 是否有新增/关闭项目 |
| 学费 | 每年7月 | 检查 https://www.upei.ca/fees (新学年费率通常在5-7月发布) |
| 录取要求 | 每年9月 | 检查 admission-requirements 子页面更新 |
| 英语语言要求 | 每年 | 检查 undergraduate-programs 页面更新 |
| 申请截止日期 | 每年8月 | 检查 Apply 页面和 deadlines 页面 |
| 奖学金信息 | 每年 | 检查 https://www.upei.ca/scholarships-and-awards |
| 各国入学要求 | 每年 | 检查 country-specific-requirements 页面更新 |

---

*End of Document — University of Prince Edward Island 完整深度数据 v2*
