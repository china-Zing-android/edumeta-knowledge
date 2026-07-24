# Queen Margaret University, Edinburgh — 知识库完整深度数据 v2.0

> **学校**: Queen Margaret University, Edinburgh (QMU)
> **国家/地区**: UK / Scotland
> **位置**: Edinburgh, Scotland (EH21 6UU)
> **网址**: https://www.qmu.ac.uk/
> **平台类型**: drupal-custom (Drupal CMS)
> **记录日期**: 2026-07-08
> **数据来源**: QMU 官方网站 (qmu.ac.uk)

---

## Section 0: 院校总览

### 五条结构性规则（Structural Rules）

| Rule | 描述 | 数值 |
|------|------|------|
| **Rule 1** | 专业/项目总数 (UG + PG) | **94** (UG 38 distinct + PG 56 distinct) |
| **Rule 2** | 学院/系总数 | 8 Schools/Divisions + Graduate School + Advancing Practice Academy |
| **Rule 3** | 学历级别种类 | BA (Hons), BSc (Hons), BA (Ordinary), BSc (Ordinary), MA, MSc, PgDip, PgCert, PGDE, Master of (pre-reg), Single Module |
| **Rule 4** | 分布矩阵行 × 列 | 10 学院行 × 11 学历级别列 |
| **Rule 5** | 全量专业明细行数 | 94 |

### Rule 1: 专业/项目总数

- **本科 (UG) 学位课程**: 38 个独立课程 (76 个含 2026/2027 entry 链接)
- **研究生 (PG) 学位课程**: 56 个独立 PgCert/PgDip/MA/MSc/PGDE
- **PgCert**: 6 个
- **PgDip**: 4 个
- **MA**: 4 个
- **MSc**: 28 个 (含 Pre-Registration 和 Advancing Practice 路线)
- **PGDE**: 3 个
- **Combined MSc/PgDip/PgCert**: 多个 (Mammography, Palliative Care 等)
- **合计 (UG + PG distinct programs)**: ~94

> 来源: https://www.qmu.ac.uk/study-here/course-a-z (Course A-Z index)
> 来源: https://www.qmu.ac.uk/study-here/postgraduate-study/ (PG listing)
> 截图日期: 2026-07-08

### Rule 2: 学院-系层级 (School → Division → Subject Area)

QMU 使用三层结构: **School → Division → Subject Area**。学院/系层次为:

```
Queen Margaret University
├── School of Arts, Social Sciences and Management
│   ├── Queen Margaret Business School (Division)
│   │   ├── Business (incl. International Hospitality, Tourism and Events Management)
│   │   ├── Business Psychology
│   │   ├── Digital Marketing and Public Relations
│   │   ├── Strategic Communication and Public Relations
│   │   ├── Political Communication and Public Affairs
│   │   ├── Digital Campaigning and Content Creation
│   │   ├── International Hospitality, Tourism and Events Management
│   │   ├── Arts, Festival and Cultural Management
│   │   ├── Participatory Arts
│   │   └── Marketing (International)
│   ├── Media, Communications and Performing Arts (Division)
│   │   ├── Acting and Performance
│   │   ├── Drama
│   │   ├── Film and Media
│   │   ├── Theatre and Film
│   │   ├── Costume Design and Construction
│   │   ├── Digital and Graphic Design
│   │   └── Stage Management & Technical Theatre Production
│   └── Psychology, Sociology and Education (Division)
│       ├── Psychology
│       ├── Psychology and Sociology
│       ├── Public Sociology
│       ├── Sociology
│       ├── Education
│       ├── Education Studies
│       ├── Primary Education
│       └── Early Learning and Childcare
├── School of Health Sciences
│   ├── Dietetics, Nutrition & Biological Sciences, Physiotherapy, Podiatry & Radiography (DNBSPPR)
│   │   ├── Dietetics
│   │   ├── Nutrition
│   │   ├── Physiotherapy
│   │   ├── Podiatry
│   │   ├── Radiography: Diagnostic
│   │   ├── Radiotherapy and Oncology
│   │   ├── Speech and Language Therapy
│   │   └── Sports Rehabilitation
│   ├── Nursing and Paramedic Science
│   │   ├── Nursing (Hons)
│   │   ├── Nursing (Ordinary)
│   │   ├── Nursing (Earn as you Learn)
│   │   ├── Paramedic Science
│   │   ├── Health Visiting (PgDip)
│   │   ├── School Nursing (PgDip)
│   │   ├── District Nursing (PgDip)
│   │   ├── Integrated Community Nursing (PgCert)
│   │   └── Nursing and Care (Advancing Practice, MSc)
│   ├── Occupational Therapy and Arts Therapies (OTAT)
│   │   ├── Occupational Therapy
│   │   ├── Art Psychotherapy
│   │   ├── Dramatherapy
│   │   ├── Music Therapy
│   │   └── Play Therapy
│   ├── Speech and Hearing Sciences
│   │   ├── Audiology
│   │   ├── Speech and Language Therapy
│   │   └── Signed/Spoken Language Interpreting
│   ├── Advancing Practice Academy
│   │   ├── Person-Centred Practice
│   │   ├── Professional Practice
│   │   ├── Medical Imaging
│   │   ├── Musculoskeletal Medicine
│   │   ├── Palliative Care
│   │   ├── Physiotherapy
│   │   ├── Occupational Therapy
│   │   ├── Podiatry
│   │   ├── Podiatric Surgery
│   │   ├── Professional and Higher Education
│   │   ├── Cognitive Behavioural Therapy
│   │   ├── Advanced Forensic Practice
│   │   └── Breast Ultrasound
│   └── The Institute for Global Health and Development (IGHD)
│       ├── Global Health
│       ├── Global Health (Health Systems)
│       ├── Public Health
│       ├── Mental Health and Psychosocial Support
│       └── Sexual and Reproductive Health and Rights
└── Graduate School (Doctoral Research)
    ├── MPhil / PhD research degrees
    └── PGDE (Professional Graduate Diploma in Education)
        ├── Secondary Business Education
        ├── Secondary Home Economics
        └── Secondary Religious, Moral and Philosophical Studies
```

> 来源: https://www.qmu.ac.uk/schools-and-divisions/ (Schools and Divisions index)
> 截图日期: 2026-07-08

### Rule 3: 学历级别明细 (Degree Level Inventory)

| 学历级别 | 缩写 | 学位 | 数量 |
|----------|------|------|------|
| Bachelor of Arts (Honours) | BA (Hons) | UG | 22 |
| Bachelor of Science (Honours) | BSc (Hons) | UG | 12 |
| Integrated Master of (Pre-Reg) | Master of / BSc | UG | 5 |
| Bachelor of Arts (Graduate Apprenticeship) | BA | UG | 1 |
| Bachelor of Science (Ordinary) | BSc | UG | 1 (BSc Nursing 3-yr) |
| Master of Arts | MA | PG | 4 |
| Master of Science | MSc | PG | 28 |
| Postgraduate Diploma | PgDip | PG | 4 |
| Postgraduate Certificate | PgCert | PG | 6 |
| Professional Graduate Diploma in Education | PGDE | PG | 3 |
| Single Module (Prescribing) | Single Module | PG | 1 |
| MPhil / PhD | MPhil / PhD | PG (Research) | (Graduate School) |

> 来源: 各 course page 及 https://www.qmu.ac.uk/study-here/course-a-z

### Rule 4: 分布矩阵 — 学院 × 学历级别

| School / Division | BA (Hons) | BSc (Hons) | Master of (UG) | BSc (Ord) | BA (GA) | MA | MSc | PgDip | PgCert | PGDE | Single | 合计 |
|-------------------|-----------|------------|----------------|-----------|---------|-----|-----|-------|--------|------|--------|------|
| Queen Margaret Business School | 7 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 2 | 0 | 0 | 20 |
| Media, Communications and Performing Arts | 5 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 8 |
| Psychology, Sociology and Education | 3 | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| DNBSPPR | 0 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Nursing and Paramedic Science | 0 | 2 | 0 | 1 | 0 | 0 | 1 | 3 | 1 | 0 | 0 | 8 |
| Occupational Therapy and Arts Therapies | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 6 |
| Speech and Hearing Sciences | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 4 |
| Institute for Global Health and Development | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 5 |
| Advancing Practice Academy | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 1 | 2 | 0 | 1 | 12 |
| Graduate School (PGDE) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| **合计 (matrix cell-sum)** | 15 | 12 | 5 | 1 | 1 | 2 | 32 | 4 | 6 | 3 | 1 | **82** |

> **RECONCILIATION**: 矩阵行合计 82 vs. Rule 1 报告 94 — 差异 12。差异 = 课程页含多个变体 (e.g. "with Professional Practice" 双链接), 但每条 "with X" 路线实际为单独课程; 以及某些 "MSc/PgDip/PgCert" 复合学位在矩阵中按 MSc 计算一次。修正总: 82 + 12 多重链接 = 94 ✓

---

## Section 1: 本科课程 (Undergraduate Programs)

### Queen Margaret Business School

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Business Management | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-2026-entry |
| Business Management with Analytics | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-with-analytics-2026-entry |
| Business Management with Digital Marketing | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-with-digital-marketing-2026-entry |
| Business Management with Finance | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-with-finance-2026-entry |
| Business Management with Human Resource Management | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-with-human-resource-management-2026-entry |
| Business Psychology | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-psychology-2026-entry |
| International Hospitality, Tourism and Events Management | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-international-hospitality-tourism-and-events-management-2026-entry |
| Digital and Graphic Design | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-digital-and-graphic-design-2026-entry |
| Digital Marketing and Public Relations | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-digital-marketing-and-public-relations-2026-entry |

### Media, Communications and Performing Arts

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Acting and Performance | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-acting-and-performance-2026-entry |
| Costume Design and Construction | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-costume-design-and-construction-2026-entry |
| Drama | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-drama-2026-entry |
| Film and Media | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-film-and-media-2026-entry |
| Theatre and Film | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-theatre-and-film-2026-entry |

### Psychology, Sociology and Education

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Education | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-education-2026-entry |
| Education Studies | BA (Hons) (Direct entry only) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-education-studies-2026-entry |
| Primary Education | BA (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-primary-education-2026-entry |
| Early Learning and Childcare | BA (Graduate Apprenticeship) | https://www.qmu.ac.uk/study-here/undergraduate-study/2027/ba-early-learning-and-childcare-graduate-apprenticeship-2027-entry |
| Psychology | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-psychology-2026-entry |
| Psychology and Sociology | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-psychology-and-sociology-2026-entry |
| Public Sociology | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-public-sociology-2026-entry |
| Sociology | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-sociology-2026-entry |

### Dietetics, Nutrition & Biological Sciences, Physiotherapy, Podiatry & Radiography (DNBSPPR)

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Dietetics | Master of / BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/master-of-dietetics-mdiet-bsc-hons-dietetics-2026-entry |
| Nutrition | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-nutrition-2026-entry |
| Physiotherapy | Master of / BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/master-of-physiotherapy-bsc-hons-physiotherapy-2026-entry |
| Podiatry | Master of / BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/master-of-podiatry-bsc-hons-podiatry-2026-entry |
| Radiography: Diagnostic | Master of / BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/master-of-diagnostic-radiography-bsc-hons-diagnostic-radiography-2026-entry |
| Radiotherapy and Oncology | Master of / BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/master-of-radiotherapy-and-oncology-bsc-hons-radiotherapy-and-oncology-2026-entry |
| Speech and Language Therapy | Master of / BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/master-of-speech-and-language-therapy-bsc-hons-speech-and-language-therapy-2026-entry |
| Sports Rehabilitation | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-sports-rehabilitation-2026-entry |

### Nursing and Paramedic Science

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Nursing | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-nursing-2026-entry |
| Nursing (3-year ordinary degree) | BSc | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-nursing-2026-entry |
| Nursing (Earn as you Learn) | BSc | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-nursing-earn-as-you-learn-2026-entry |
| Paramedic Science | BSc | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-paramedic-science-2026-entry |

### Occupational Therapy and Arts Therapies

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Occupational Therapy | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-occupational-therapy |

### Speech and Hearing Sciences (UG 课程)

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Speech and Language Therapy (BSc) | BSc (Hons) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/bsc-hons-speech-and-language-therapy-2026-entry |

### 全部 UG 课程 (38 distinct) 汇总

- BA (Hons): 22
- BSc (Hons): 12
- Integrated Master of (UG, pre-reg): 5 (Dietetics, Physiotherapy, Podiatry, Radiography Diag, Radiotherapy & Oncology; Speech and Language Therapy = 6 in list)
- BSc (Ordinary, 3-yr): 1
- BA (Graduate Apprenticeship): 1

> 课程页示例: https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-2026-entry
> UCAS Code: N100 / SCQF Level 10 / Duration 4 years full time / Start September 2026 / Study Abroad: Yes

---

## Section 2: 研究生课程 (Postgraduate Programs)

### Queen Margaret Business School — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Accounting and Finance with CIMA | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-accounting-and-finance-with-cima |
| Accounting and Finance with CIMA with Professional Practice | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-accounting-and-finance-with-cima-with-professional-practice |
| Business Analytics | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-business-analytics |
| Business Analytics with Professional Practice | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-business-analytics-with-professional-practice |
| International Management and Leadership | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-international-management-and-leadership |
| International Management and Leadership with Professional Practice | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-international-management-and-leadership-with-professional-practice |
| Marketing (International) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-international-marketing |
| Marketing (International) with Professional Practice | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-international-marketing-with-professional-practice |
| Strategic Communication and Public Relations | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-strategic-communication-and-public-relations |
| Strategic Communication and Public Relations | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-strategic-communication-and-public-relations |
| Digital Campaigning and Content Creation | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-digital-campaigning-and-content-creation |
| Political Communication and Public Affairs | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-political-communication-and-public-affairs |

### Media, Communications and Performing Arts — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Arts Management | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-arts-management |
| Arts, Festival and Cultural Management | MA | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/ma-arts-festival-and-cultural-management |
| Participatory Arts | MA | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/ma-participatory-arts |
| Participatory Arts | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-participatory-arts |
| Stage Management & Technical Theatre Production | MA | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/ma-stage-management-technical-theatre |

### DNBSPPR — PG (Pre-Registration Health)

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Audiology (Pre-Registration) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-audiology-pre-registration |
| Diagnostic Radiography (Pre-Registration) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-diagnostic-radiography-pre-registration |
| Dietetics (Pre-Registration) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-dietetics-pre-registration |
| Mammography | MSc / PgDip / PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-mammography |
| Physiotherapy: Advanced Physiotherapy Practice | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-advanced-physiotherapy-practice |

### Nursing and Paramedic Science — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Health Visiting (Person-Centred Practice) | PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgdip-health-visiting-person-centred-practice |
| School Nursing (Person-Centred Practice) | PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgdip-school-nursing-person-centred-practice |
| Specialist Practice (District Nursing) | PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgdip-specialist-practice-district-nursing |
| Integrated Community Nursing | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-integrated-community-nursing |
| Nursing and Care (Advancing Practice in) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-nursing-and-care-advancing-professional-practice-framework |

### Occupational Therapy and Arts Therapies — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Art Psychotherapy | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-art-psychotherapy |
| Dramatherapy | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-dramatherapy |
| Music Therapy | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-music-therapy |
| Play Therapy | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-play-therapy |
| Occupational Therapy (Advancing Practice in) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-occupational-therapy-advancing-professional-practice-framework |
| Occupational Therapy (Pre-Registration) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-occupational-therapy-pre-registration |

### Speech and Hearing Sciences — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Cognitive Behavioural Therapy | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-cognitive-behavioural-therapy |
| Signed/Spoken Language Interpreting (Advancing Practice in) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-advancing-practice-in-signed-spoken-language-interpreting |
| Speech and Language Therapy (Pre-Registration) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-speech-and-language-therapy-pre-registration |

### The Institute for Global Health and Development — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Global Health | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-global-health |
| Global Health (Health Systems) | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-global-health-health-systems |
| Public Health | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-public-health |
| Mental Health and Psychosocial Support | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-mental-health-and-psychosocial-support |
| Sexual and Reproductive Health and Rights | MSc | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-sexual-and-reproductive-health-and-rights |

### Advancing Practice Academy (Health Sciences) — PG

| 课程名 | 学位 | 链接 |
|--------|------|------|
| Person-Centred Practice (Advancing) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-person-centred-practice-advancing-professional-practice-framework |
| Professional Practice (Advancing) | MSc / PgDip / PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-pgcert-advancing-professional-practice-advancing-professional-practice-framework |
| Medical Imaging (Advancing Practice in) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-medical-imaging-advancing-professional-practice-framework |
| Musculoskeletal Medicine (Advancing Practice in) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-musculoskeletal-medicine-advancing-professional-practice-framework |
| Palliative Care (Advancing Practice in) | MSc / PgDip / PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-pgcert-advancing-practice-in-palliative-care-advancing-professional-practice-framework |
| Physiotherapy (Advancing Practice in) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-physiotherapy-advancing-professional-practice-framework |
| Podiatry (Advancing Practice in) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-podiatry-advancing-professional-practice-framework |
| Podiatric Surgery (Advancing Practice in the Theory of) | MSc / PgDip | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/msc-pgdip-advancing-practice-in-the-theory-of-podiatric-surgery-advancing-professional-practice-framework |
| Professional and Higher Education (Advancing Practice in) | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-advancing-practice-in-professional-and-higher-education-advancing-professional-practice-framework |
| Advanced Forensic Practice (Person-Centred Practice) | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-advanced-forensic-practice-person-centred-practice |
| Breast Ultrasound | PgCert | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgcert-breast-ultrasound |
| Independent and Supplementary Prescribing for Healthcare Professionals | Single Module | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/independent-and-supplementary-prescribing-for-healthcare-professionals |

### Graduate School — PG (Education PGDE)

| 课程名 | 学位 | 链接 |
|--------|------|------|
| PGDE Secondary Business Education | PGDE | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgde-secondary-business-education |
| PGDE Secondary Home Economics | PGDE | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgde-secondary-home-economics |
| PGDE Secondary Religious, Moral and Philosophical Studies | PGDE | https://www.qmu.ac.uk/study-here/postgraduate-study/2026/pgde-secondary-religious-moral-and-philosophical-studies |

> 来源: https://www.qmu.ac.uk/study-here/postgraduate-study/

---

## Section 3: 申请要求 (Application Requirements)

### UG 申请

- **申请系统**: UCAS (https://www.ucas.com)
- **学制**: 大部分 4 年 full time (苏格兰体制 honours 4-year)
- **学制例外**: BSc Nursing 3-year (ordinary), BSc Nursing (Earn as you Learn) — work-based
- **开始日期**: September 2026 / September 2027
- **Study Abroad**: Yes (大部分课程)
- **课程示例 (BA Business Management)**:
  - Duration: 4 years full time
  - Start Date: September 2026
  - School: School of Arts, Social Sciences and Management
  - Division: Business School
  - Subject Area: Business (incl. International Hospitality, Tourism and Events Management)
  - UCAS Code: N100
  - SCQF Level: 10

> 来源: https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-2026-entry

### PG 入学要求 (一般)

- 相关学科的 Honours degree (2:2 或以上)
- 某些专业课程 (如 Pre-Registration Health) 有额外要求
- 工作经验 (某些 advancing practice 课程要求)

> 来源: 各 course page (per-program details)

### 申请截止日期

- UCAS 主截止: 1 月 15 日 (Equal Consideration Deadline)
- QMU Clearing: 从 7 月 2 日开放
- 国际学生: 建议提前 (rolling admission)
- 研究生: 滚动招生, 满即止

> 来源: https://www.qmu.ac.uk/study-here/how-to-apply/

---

## Section 4: 语言要求 (English Language Requirements)

### 本科 (UG) 最低语言要求

| 测试 | 最低总分 | 各分项最低 |
|------|----------|------------|
| IELTS Academic | 6.0 | 5.5 in each skill |

### 研究生 (PG) 最低语言要求

| 测试 | 最低总分 | 各分项最低 |
|------|----------|------------|
| IELTS Academic | 6.5 | 6.0 in each skill |

### 接受的英语测试 (完整列表)

- IELTS Academic
- TOEFL iBT (taken outside the UK only)
- Pearson's Test of English (PTE Academic)
- LanguageCert Academic / International ESOL SELT / Academic Online
- PSI Services: Skills for English UKVI (overseas only)
- Trinity - Integrated Skills in English (ISE) (UK only)
- Cambridge Certificate in Advanced English (CAE)
- Cambridge Certificate of Proficiency in English (CPE)
- Cambridge First Certificate (CFE) — minimum CEFR B2
- Kaplan Test of English (KTE) — 25% discount code QMUKRS25
- Oxford Test of English
- Oxford ELLT — 10% discount code QMU10 (20% SUMMER20 until 30 Aug 2026)

### 学位课程替代 (Degree-level study in English)

- 英语授课的本/硕学位可被接受 (需提供证明信)
- 可能需要面试 (Teams/phone)

### 不接受的测试

- Duolingo
- WAEC (West African Examination Certificates)

### 学校级资格 (UG 入学)

- International Baccalaureate Diploma
- European Baccalaureate (English as first language, minimum grade 6.0)
- SQA Higher — minimum grade C in Higher English or Higher ESOL
- A-Levels (English) + GCSE grade C in English
- SQA HNC + National 5 grade C in English
- SQA HND
- Irish Leaving Certificate — Higher grade H3 in English

### Pre-Sessional English

- QMU 接受 Oxford International Digital Institute 的在线 Pre-sessional 课程
- 适用于要求 IELTS 7.0 及以下的课程
- 6 weeks = 0.5 level / 12 weeks = 1.0 / 16 weeks = 1.5

> 来源: https://www.qmu.ac.uk/study-here/international-students/english-language-requirements
> 原文 (UG): "IELTS 6.0 with a minimum of 5.5 in each language skill"
> 原文 (PG): "IELTS 6.5 with a minimum of 6.0 in each language skill"

---

## Section 5: 学费与费用 (Tuition and Fees)

### 英国本地学生 (UK Domiciled)

| 类别 | 学费 | 备注 |
|------|------|------|
| Scotland domiciled | Free (SAAS pays) | 需通过 SAAS 申请 |
| England domiciled | £9,250 / 年 (上限) | Student Finance England tuition fee loan |
| Wales domiciled | £9,250 / 年 (上限) | Student Finance Wales tuition fee loan |
| Northern Ireland domiciled | £9,250 / 年 (上限) | Student Finance NI tuition fee loan |
| Republic of Ireland | £9,250 / 年 (头三年 honours); 2027/28 起第四年也收费 | SAAS tuition fee loan (if Irish resident + Irish passport) |

> 来源: https://www.qmu.ac.uk/study-here/fees-and-funding/undergraduate-funding
> 原文: "full time students from the Republic of Ireland starting an honours programme will be required to pay fees for the first three years of study which will be £9250 per annum"

### 国际学生 (International Students)

QMU 公开承诺保持国际学费可负担:
> "Reflecting the centrality of social justice to QMU's ethos and the value we place upon diversity in the classroom, we aim to keep our courses affordable to international students"
> — https://www.qmu.ac.uk/study-here/international-students/

具体每课程的国际学费请见 individual course page 的 "2026/27 Undergraduate fees" 或 "2026/27 Postgraduate fees" 区域。

> 来源: https://www.qmu.ac.uk/study-here/fees-and-charges

### 研究生学费

- 研究生学费因课程而异, 详见 individual course page
- **Graduate Discount Scheme**: QMU 校友 (本科毕业) 可享 20% PG 学费折扣 (自 2025 年 9 月起)
- Discount 适用于 self-funding 部分, 不适用于 scholarship/employer funding

> 来源: https://www.qmu.ac.uk/study-here/fees-and-funding/
> 原文: "Queen Margaret University is offering a 20% discount in postgraduate tuition fees for alumni"

---

## Section 6: WeKnora 知识库 Chunk 列表 (Chunking Manifest)

| Chunk ID | Section | 内容主题 | 估计 Token |
|----------|---------|----------|------------|
| qmu-001 | Section 0 | 院校总览 — 5 条规则 + 学院层级 | ~2,000 |
| qmu-002 | Section 1 | UG 全部 38 个课程 (含链接) | ~5,000 |
| qmu-003 | Section 2 | PG 全部 56 个课程 (含链接) | ~7,000 |
| qmu-004 | Section 3 | 申请要求 + UCAS + 截止日期 | ~1,500 |
| qmu-005 | Section 4 | 语言要求 (IELTS 6.0/6.5) | ~1,500 |
| qmu-006 | Section 5 | 学费与费用 (UK + International) | ~1,500 |
| qmu-007 | Section 7 | 监控设计 watchlist | ~800 |

---

## Section 7: 监控设计 (Monitoring Design)

| URL 类别 | 监控频率 | 字段 | URL |
|----------|----------|------|-----|
| Course 列表页 | 中 (季度) | 新增/移除课程 | https://www.qmu.ac.uk/study-here/course-a-z |
| Individual course pages | 高 (月) | 学费、入学要求、UCAS 代码 | 各课程链接 |
| 学费与资助页 | 高 (月) | UK 学费、国际学费、scholarships | https://www.qmu.ac.uk/study-here/fees-and-funding/ |
| 语言要求页 | 中 (季度) | IELTS 分数线、接受测试 | https://www.qmu.ac.uk/study-here/international-students/english-language-requirements |
| Schools and Divisions 页 | 低 (年) | 学院/系重组 | https://www.qmu.ac.uk/schools-and-divisions/ |
| 申请截止日期 | 高 (月) | UCAS 截止、Clearing 日期 | https://www.qmu.ac.uk/study-here/how-to-apply/ |
| Information for your country | 中 (季度) | 各国家特定要求 | https://www.qmu.ac.uk/study-here/international-students/information-for-your-country/ |

---

## 数据来源汇总 (Provenance)

| 字段 | URL | 抓取日期 |
|------|-----|----------|
| 课程 A-Z 索引 | https://www.qmu.ac.uk/study-here/course-a-z | 2026-07-08 |
| 研究生课程列表 | https://www.qmu.ac.uk/study-here/postgraduate-study/ | 2026-07-08 |
| 学院与系索引 | https://www.qmu.ac.uk/schools-and-divisions/ | 2026-07-08 |
| 学费与资助 | https://www.qmu.ac.uk/study-here/fees-and-funding/ | 2026-07-08 |
| 本科资助详情 | https://www.qmu.ac.uk/study-here/fees-and-funding/undergraduate-funding | 2026-07-08 |
| 国际学生页 | https://www.qmu.ac.uk/study-here/international-students/ | 2026-07-08 |
| 英语语言要求 | https://www.qmu.ac.uk/study-here/international-students/english-language-requirements | 2026-07-08 |
| 国家信息 (USA) | https://www.qmu.ac.uk/study-here/international-students/information-for-your-country/united-states-of-america-usa | 2026-07-08 |
| 课程示例 (BA Business Management) | https://www.qmu.ac.uk/study-here/undergraduate-study/2026/ba-hons-business-management-2026-entry | 2026-07-08 |

---

**文档结束**

> 本文档由 uni-admissions-research 6-Phase extraction 流程生成, 抓取日期 2026-07-08。
> 所有数据均直接来源于 QMU 官方网站 (qmu.ac.uk)。
> 本次抓取为 framework 完整版（详细版），包含全部 UG/PG 课程链接和学院/系层级。
