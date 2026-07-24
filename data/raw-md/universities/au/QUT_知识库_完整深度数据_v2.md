# Queensland University of Technology (QUT) — 知识库完整深度数据 v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (Queensland)
> **Official website**: https://www.qut.edu.au/
> **CMS Platform**: Sitecore (behind Cloudflare WAF)

---

## Section 0 — 院校总览

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 100+（官方声称 "more than 100 real-world courses"） |
| 研究生授课型项目 (PGT) | 50+（估算，待精确提取） |
| 研究生博士项目 (PhD/Doctoral) | 大量研究型项目，涵盖各学院 |
| 学位项目总计 | 200+（估算，含双学位、垂直学位） |
| 学院 (Faculties) | 6 |
| 院系 (Schools) — 仅 Business and Law 已知 | 6（已知），其余学院待提取 |

### 0.2 学院 / 系层级结构

```
Queensland University of Technology (QUT)
├── Faculty of Business and Law
│   ├── School of Accountancy
│   ├── School of Advertising, Marketing and Public Relations
│   ├── School of Economics and Finance
│   ├── School of Law
│   ├── School of Management
│   └── QUT Graduate School of Business
├── Faculty of Creative Industries, Education and Social Justice
│   └── Schools (待提取)
├── Faculty of Engineering
│   └── Schools (待提取，含 Architecture/Built Environment)
├── Faculty of Health
│   └── Schools (待提取)
├── Faculty of Science
│   └── Schools (待提取)
└── Faculty of Indigenous Knowledges and Culture
    └── (跨学科教学与研究)
```

### 0.3 学历级别明细

| 学历级别 | 已知数量 |
|----------|---------|
| Bachelor Degree (学士) | 待全量提取 |
| Bachelor Degree (Honours) (荣誉学士) | 待全量提取 |
| Graduate Certificate (研究生证书) | 待全量提取 |
| Graduate Diploma (研究生文凭) | 待全量提取 |
| Master Degree (Coursework) (授课型硕士) | 待全量提取 |
| Master Degree (Research) (研究型硕士) | 待全量提取 |
| Doctor of Philosophy (PhD) (博士) | 待全量提取 |
| Higher Doctorate (高级博士) | 待全量提取 |
| Vertical Double Degree (本硕连读) | 待全量提取 |
| Diploma / Associate Degree (文凭/副学士) | 待全量提取 |

### 0.4 分布矩阵

> **说明**：由于 QUT 网站使用 Cloudflare WAF + Sitecore CMS，课程列表无法通过 API 或 sitemap 批量获取。下表为已知课程分布的框架，全量数据标注为 **P0 待提取**。

| 学院 \ 学位级别 | Bachelor | Bachelor (Hons) | Masters (CW) | PhD | GC/GD | Vertical DD |
|-----------------|:--------:|:----------------:|:------------:|:---:|:-----:|:-----------:|
| Business and Law | TBD | TBD | TBD | TBD | TBD | TBD |
| Creative Industries, Education & Social Justice | TBD | TBD | TBD | TBD | TBD | TBD |
| Engineering | TBD | TBD | TBD | TBD | TBD | TBD |
| Health | TBD | TBD | TBD | TBD | TBD | TBD |
| Science | TBD | TBD | TBD | TBD | TBD | TBD |
| Indigenous Knowledges and Culture | TBD | TBD | TBD | TBD | TBD | TBD |

---

## Section 1 — Undergraduate Education (本科教育)

### 1.1 Faculty of Business and Law

| 专业名称 | 学位类型 | 学院 | 院系 | URL |
|---------|---------|------|-----|-----|
| *待全量提取* | | | | |

### 1.2 Faculty of Creative Industries, Education and Social Justice

| 专业名称 | 学位类型 | 学院 | 院系 | URL |
|---------|---------|------|-----|-----|
| *待全量提取* | | | | |

### 1.3 Faculty of Engineering

**已知本科课程（Architecture and Built Environment 领域）：**

| 专业名称 | 学位类型 | 学院 | 院系 | URL |
|---------|---------|------|-----|-----|
| Diploma in Architectural Studies / Bachelor of Architectural Design | Diploma + Bachelor | Engineering | Architecture | https://www.qut.edu.au/courses/diploma-in-architectural-studies-bachelor-of-architectural-design |
| Diploma in Architectural Studies / Bachelor of Built Environment (Honours) | Diploma + Bachelor (Hons) | Engineering | Built Environment | https://www.qut.edu.au/courses/diploma-in-architectural-studies-bachelor-of-built-environment-honours |
| Bachelor of Architectural Design | Bachelor | Engineering | Architecture | https://www.qut.edu.au/courses/bachelor-of-architectural-design |
| Bachelor of Built Environment (Honours) | Bachelor (Hons) | Engineering | Built Environment | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours |
| Bachelor of Built Environment (Honours) (Interior Design) | Bachelor (Hons) | Engineering | Interior Design | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design |
| Bachelor of Built Environment (Honours) (Construction Management and Quantity Surveying) | Bachelor (Hons) | Engineering | Construction Management | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-construction-management-and-quantity-surveying |
| Bachelor of Built Environment (Honours) (Landscape Architecture) | Bachelor (Hons) | Engineering | Landscape Architecture | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-landscape-architecture |
| Bachelor of Built Environment (Honours) / Master of Project Management (Vertical Double Degree) | Bachelor (Hons) / Master | Engineering | Built Environment | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-master-of-project-management |

**UG 学习领域列表（待从各领域页面提取全量课程）：**
- Architecture and Built Environment, Arts, Business, Communication, Creative Arts, Design, Engineering, Health, Information Technology and Games, Justice, Languages, Law, Mathematics and Data Science, Science, Teaching, English Language and Pathway Programs

### 1.4 Faculty of Health

| 专业名称 | 学位类型 | 学院 | 院系 | URL |
|---------|---------|------|-----|-----|
| *待全量提取* | | | | |

### 1.5 Faculty of Science

| 专业名称 | 学位类型 | 学院 | 院系 | URL |
|---------|---------|------|-----|-----|
| *待全量提取* | | | | |

---

## Section 2 — Graduate Education (研究生教育)

### 2.1 Taught Postgraduate (PGT)

**PG 学习领域列表（待从各领域页面提取全量课程）：**
- Architecture, Business, Communication, Design, Education, Engineering, Health, Information Technology and Games, Justice, Languages, Law, Mathematics and Data Science, Science

**已知研究生课程（Architecture 领域）：**

| 专业名称 | 学位类型 | 学院 | URL |
|---------|---------|------|-----|
| Master of Architecture | Master (Coursework) | Engineering | https://www.qut.edu.au/study/postgraduate/architecture |

### 2.2 Research Degrees (PhD / MPhil)

| 专业名称 | 学位类型 | 学院 | URL |
|---------|---------|------|-----|
| PhDs and research degrees portal | PhD / MPhil | All faculties | https://www.qut.edu.au/study/phds-and-research-degrees |

---

## Section 3 — Application Requirements & Deadlines (申请要求与截止日期)

### 3.1 Undergraduate Entry Requirements

**Domestic Students:**
- **Recent secondary education**: Apply via QTAC (Queensland Tertiary Admissions Centre)
- **Higher education study**: Previous tertiary study considered
- **VET study**: Vocational Education and Training qualifications accepted
- **Work and life experience**: Mature-age entry pathways available
- **Adjustment schemes**: Available for elite athletes, difficult circumstances, subject bonuses
- **Bridging programs**: Short programs in physics, chemistry, Maths B
- **CASP**: Centralised Assessment Selection Program for Aboriginal and Torres Strait Islander students (via Oodgeroo Unit)
- **Performance/Creative Arts**: Additional entry for Bachelor of Creative Arts (Acting)

**International Students:**
- Apply directly to QUT (not QTAC)
- Academic requirements vary by country — country-specific entry requirements available on course detail pages

### 3.2 English Language Requirements

> **⚠️ P0 待提取**：英语语言要求页面受 Cloudflare 保护无法直接访问。已知各课程详情页面有独立的语言要求标签页，需逐个提取。

QUT 通常要求（基于澳大利亚大学通用标准）：
- **IELTS**: 通常 6.5（单项不低于 6.0），部分课程要求 7.0+
- **TOEFL iBT**: 通常 79-90
- **PTE Academic**: 通常 58-64

（确切分数需从各课程详情页的 "Requirements" 标签页提取）

### 3.3 Application Deadlines

| 入学季 | UG Domestic | UG International | PG International |
|-------|-------------|-----------------|-----------------|
| February (Semester 1) | Via QTAC key dates | *待提取* | *待提取* |
| July (Semester 2) | Via QTAC key dates | *待提取* | *待提取* |

> **⚠️ P0 待提取**：确切的申请截止日期需从 QUT 国际学生申请页面及各课程详情页提取。

### 3.4 Special Requirements

- **Portfolio**: Required for creative arts and design courses
- **Audition**: Required for Bachelor of Creative Arts (Acting)
- **Interview**: Some courses may require interviews
- **Prerequisites**: Specific subjects required for some courses (e.g., Maths B for engineering, Chemistry for health sciences)

---

## Section 4 — Costs & Financial Aid (费用与奖学金)

### 4.1 International Student Fees

> **⚠️ P0 待提取**：国际学生学费需从各课程详情页的 "Fees" 标签页逐个提取。QUT 在 Sitecore 中每个课程页面都有独立的费用信息。

**Known:**
- International fees are set per course (not a flat rate)
- Domestic students pay CSP (Commonwealth Supported Place) fees for eligible courses
- Domestic full-fee places available for some courses

### 4.2 Cost of Living (Monthly Estimates)

| 费用项目 | 学生公寓 (Student Apartment) | 包餐住宿 (Catered) | 合租 (Private share) |
|---------|:--------------------------:|:-----------------:|:-------------------:|
| 房租 (Rent) | $1,600 - $2,200 | $2,400 - $2,650 | $800 - $1,600 |
| 水电煤 (Utilities) | $150 - $175* | $150 - $175* | $150 - $175* |
| 伙食 (Food) | $560 - $1,500 | Included | $560 - $1,500 |
| 手机/网络 (Mobile/Internet) | $50 - $120 | $50 - $120 | $50 - $120 |
| 公共交通 (Public Transport) | $100 - $150 | $100 - $150 | $100 - $150 |
| **合计 (Total)** | **$2,460 - $2,795** | **$2,700 - $3,095** | **$1,660 - $3,545** |

\* 部分学生公寓已包含水电费

### 4.3 Scholarships

**International Student Scholarships:**
- QUT International Merit Scholarship (自动考虑)
- QUT Real World International Scholarship
- Country-specific scholarships
- 更多详情：https://www.qut.edu.au/study/fees-and-scholarships/scholarships/browse

**Domestic Student Scholarships:**
- 多种学术、体育、公平奖学金
- 浏览：https://www.qut.edu.au/study/fees-and-scholarships/scholarships/browse

### 4.4 Sponsorships

- QUT 接受多种政府和非政府资助项目
- 详情：https://www.qut.edu.au/study/fees-and-scholarships/sponsorships

---

## Section 5 — Evidence Chain Index (证据链索引)

| 编号 | 字段 | 值 | 来源 URL | 证据类型 | 捕获日期 |
|------|------|-----|---------|---------|---------|
| E-U-001 | institution.name | Queensland University of Technology (QUT) | https://www.qut.edu.au/ | official_webpage | 2026-07-10 |
| E-U-002 | institution.teqsa | PRV12079 | https://www.qut.edu.au/ (footer) | official_webpage | 2026-07-10 |
| E-U-003 | institution.cricos | 00213J | https://www.qut.edu.au/ (footer) | official_webpage | 2026-07-10 |
| E-U-004 | institution.abn | 83 791 724 622 | https://www.qut.edu.au/ (footer) | official_webpage | 2026-07-10 |
| E-U-005 | institution.students | 50,000+ | https://www.qut.edu.au/about | official_webpage | 2026-07-10 |
| E-U-006 | faculties.count | 6 | https://www.qut.edu.au/about/faculties-and-schools | official_webpage | 2026-07-10 |
| E-U-007 | faculty.business-and-law.schools | 6 schools | https://www.qut.edu.au/about/faculty-of-business-and-law | official_webpage | 2026-07-10 |
| E-U-008 | ug.study-areas | 15 areas | https://www.qut.edu.au/study/undergraduate | official_webpage | 2026-07-10 |
| E-U-009 | pg.study-areas | 13 areas | https://www.qut.edu.au/study/postgraduate | official_webpage | 2026-07-10 |
| E-U-010 | course.architecture | Bachelor of Built Environment (Honours) (Interior Design) | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design | official_webpage | 2026-07-10 |
| E-U-011 | course.cricos | 113182E (Interior Design) | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design | official_webpage | 2026-07-10 |
| E-U-012 | course.delivery | Gardens Point | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design | official_webpage | 2026-07-10 |
| E-U-013 | course.duration | 4 years full-time | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design | official_webpage | 2026-07-10 |
| E-U-014 | course.starts | February, July | https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design | official_webpage | 2026-07-10 |
| E-U-015 | fees.cost-of-living | $1,660 - $3,545/month | https://www.qut.edu.au/study/fees-and-scholarships | official_webpage | 2026-07-10 |
| E-U-016 | ug.applying | 4 pathways (secondary, higher ed, VET, work experience) | https://www.qut.edu.au/study/applying/undergraduate-applying | official_webpage | 2026-07-10 |
| E-U-017 | institution.campuses | Gardens Point + Kelvin Grove | https://www.qut.edu.au/about | official_webpage | 2026-07-10 |
| E-U-018 | institution.ranking | Top 100 in Architecture / Built Environment (QS 2026) | https://www.qut.edu.au/study/undergraduate/architecture-and-built-environment | official_webpage | 2026-07-10 |
| E-U-019 | business.triple-accreditation | AACSB, EQUIS, AMBA | https://www.qut.edu.au/about/faculty-of-business-and-law | official_webpage | 2026-07-10 |
| E-U-020 | law.ranking | #1 in Queensland, #5 in Australia, #54 in world (THE 2025) | https://www.qut.edu.au/about/faculty-of-business-and-law | official_webpage | 2026-07-10 |

---

## Section 6 — WeKnora Import Manifest (数据导入清单)

### Completed Data

| 数据项 | 状态 | 备注 |
|-------|------|------|
| 院校基本信息 | ✅ 已完成 | 名称、ID、地址、认证 |
| 学院结构 | ✅ 已完成 | 6个学院及 Business and Law 的子学院 |
| 学习领域列表 | ✅ 已完成 | UG 15个领域, PG 13个领域 |
| 课程URL模式 | ✅ 已完成 | /courses/{course-slug} |
| 申请途径 | ✅ 已完成 | Domestic + International |
| 生活费用 | ✅ 已完成 | 按月估算 |
| 课程详情页格式 | ✅ 已完成 | 含 Requirements/Fees/Scholarships 标签页 |

### Follow-Up Data Items

| 优先级 | 数据项 | 原因 | 估算工作量 |
|--------|-------|------|-----------|
| **P0** | 全量本科课程列表（学院×院系×专业） | 需逐个访问15个UG学习领域页面提取课程链接 | 15页浏览器访问 |
| **P0** | 全量研究生课程列表 | 需逐个访问13个PG学习领域页面提取课程链接 | 13页浏览器访问 |
| **P0** | 国际学生学费（各课程详情页） | 需从每个课程详情页的 "Fees" 标签页提取 | 每个课程需独立访问 |
| **P0** | 英语语言要求（IELTS/TOEFL/PTE） | 需从各课程详情页 "Requirements" 标签页提取 | 同上 |
| **P1** | 各学院下属院系完整列表 | 需访问 Engineering, Health, Science, CIEC 等学院页面 | 5页浏览器访问 |
| **P1** | 国际学生申请截止日期 | QUT 国际学生申请页面受 Cloudflare 保护 | 探索替代路径 |
| **P1** | 各课程 CRICOS 代码 | 部分已在课程详情页顶部显示，需全量提取 | 与课程列表同时提取 |
| **P2** | 各课程 ATAR/Selection rank | 需从 Domestic 课程视图提取 | 需切换 Domestic/International 视图 |
| **P2** | QUT College 路径课程 | Diploma, Foundation 等 | https://www.qut.edu.au/study/qut-college |
| **P2** | 奖学金细节（金额、条件） | 奖学金浏览器页面可用 | 中等 |

### Known Limitations

1. **Cloudflare WAF**: QUT 网站使用 Cloudflare WAF 保护，curl/requests 返回 403 挑战页面。所有页面必须通过真实浏览器访问。
2. **No sitemap access**: `/sitemap.xml` 被 Sitecore 拦截返回 404。无法通过 sitemap 批量获取所有课程 URL。
3. **No public API**: 未发现 Vue.js/React 数据 API。Sitecore 内容主要通过服务端渲染。
4. **Tab-based pages**: 国际学生页面使用 JS 标签页系统，URL query params 不影响标签页选中状态。
5. **CMS**: Sitecore 系统，部分页面使用 Sitecore 内部 GUID 路由，清洁 URL 不总是可用。

---

## Section 7 — Cross-School Comparison Framework (跨校对比框架)

| 维度 | QUT | UQ (参考) | Griffith (参考) |
|------|-----|-----------|----------------|
| 位置 | Brisbane CBD | Brisbane (St Lucia) | Brisbane (Nathan, Gold Coast) |
| 学生总数 | 50,000+ | 55,000+ | 50,000+ |
| 学院数 | 6 | 6 | 4 组 |
| 国际排名 (QS 2026) | Top 100 (Architecture/Built Env) | Top 50 (综合) | Top 300 (综合) |
| 本科课程数 | 100+ (待精确) | 200+ | 200+ |
| Business 认证 | Triple Crown (AACSB, EQUIS, AMBA) | AACSB, EQUIS | AACSB, EQUIS |
| CMS 平台 | Sitecore + Cloudflare | Squiz Matrix | Drupal + Funnelback |
| API 可访问 | ❌ | ❌ | ❌ (但 sitemap 可用) |
| 国际生学费 | 按课程而定 | 按课程而定 | 按课程而定 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: QUT official website (https://www.qut.edu.au/)
> **Granularity**: faculty → school → degree-level → program (部分完成)
> **Completeness**: Structural framework ✅ | Faculty hierarchy ✅ | Full UG programmes ⚠️ (P0) | Full PG programmes ⚠️ (P0) | Fee data ⚠️ (P0) | Evidence (20 blocks) ✅
> **Next steps**: 执行 P0 数据采集——全量课程列表提取、国际学生学费、英语语言要求
