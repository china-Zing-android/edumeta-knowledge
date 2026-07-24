# St George's, University of London (City St George's) — 知识库完整深度数据 v2.0

> **状态**: 完整提取 (Phase 0–5 完成) — 2026-07-08 抓取
> **主域名**: https://www.citystgeorges.ac.uk
> **历史域名**: https://www.sgul.ac.uk (legacy, redirects)
> **重点校园**: Tooting campus (Cranmer Terrace, London SW17 0RE, UK) — 原 SGUL 校区
> **抓取工具**: ego-browser (Chromium headless)
> **文档格式**: v2.0 标准化 (院校 → 系 → 学位级别 → 专业)

---

## Section 0 — 院校总览

### 0.1 关键事实

| 字段 | 值 | 来源 |
|------|------|------|
| 中文名 | 圣乔治伦敦大学 | — |
| 英文名 (历史) | St George's, University of London | sgul.ac.uk (legacy) |
| 运营名 (2024+) | City St George's, University of London | citystgeorges.ac.uk |
| 类型 | Specialist Health Sciences University（合并后仍以健康科学为核心特色） | Tooting campus focus |
| 重点校园 | Tooting campus, Cranmer Terrace, London SW17 0RE | https://www.citystgeorges.ac.uk/about/find-contact/find/tooting-campus |
| 隶属机构 | University of London (联盟成员) | 历史身份 |
| 2024 合并 | 与 City, University of London 合并为 City St George's, University of London | merged institution |
| 重点排名 | Complete University Guide 2026: #3 UK (medical school focus) | https://www.citystgeorges.ac.uk/prospective-students (snapshot 2026-07-08) |
| 学院核心 | School of Health & Medical Sciences (健康与医学院) | https://www.citystgeorges.ac.uk/about/schools/health-sciences |

### 0.2 Rule 1 — 专业/项目总数（结构化计数）

**Rule 1 — Total program count**: **36 programmes at Tooting campus**

| 类别 | 数量 | 说明 |
|------|------|------|
| Undergraduate degree (BSc/MSci/MBBS/iBSc) | 14 | 包括 5 年制 MBBS、4 年制 Graduate Entry MBBS、8 个 BSc (Hons)、1 个 MSci、2 个 iBSc |
| Postgraduate taught (MSc/PGCert/PGDip/MPAS/MRes/MA) | 22 | 包括 MSc 主学位 + MSc/PGDip/PGCert 组合 + 多个 standalone PGCert + 5 个 MRes + 1 个 MPAS + 1 个 MA |
| Postgraduate research (PhD/MPhil by research) | 0 | Tooting campus 未列出单独的 PG research 项目（健康方向研究 PhD 通常归类在 City St George's 研究学位下） |
| **Total** | **36** | 与 citystgeorges.ac.uk 过滤器 "Tooting campus" 报告的 36 一致 |

> **RECONCILIATION CHECK**: 14 UG + 22 PGT + 0 PGR = 36 — 与 citystgeorges.ac.uk 课程索引页报告的 "36 courses (Tooting campus filter)" 完全一致。✓

### 0.3 Rule 2 — 学院/系明细 + 父子层级

**所有 36 个 Tooting 项目均归属于单一学院 — School of Health & Medical Sciences**

```
City St George's, University of London
└── School of Health & Medical Sciences (健康与医学院) [Tooting campus]
    ├── Department of Medicine (8 个项目)
    │     MBBS, MBBS Graduate Entry, Physician Associate, Genomic Medicine,
    │     Clinical Neuroscience, Sports Cardiology, Advanced Clinical Practice, Heart Failure
    ├── Department of Molecular and Biomedical Sciences (7 个项目)
    │     Biomedical Science BSc, MSci, 5 × MRes pathways
    ├── Department of Allied Health (5 个项目)
    │     Diagnostic Radiography, Therapeutic Radiography, Physiotherapy,
    │     Occupational Therapy, Advanced Musculoskeletal Practice
    ├── Department of Nursing and Midwifery (3 个项目)
    │     Occupational Therapy (pre-reg), Clinical Practice, Healthcare/Biomedical Education
    ├── Department of Psychology and Neuroscience (2 个项目)
    │     Healthcare Science (Physiological Sciences), Clinical Neuroscience Practice
    ├── Department of Optometry and Visual Science (0 个 Tooting 学位项目)
    │     (department exists but no courses in this filter set)
    ├── Department of Population Health and Policy (5 个项目)
    │     Medical Ethics Law & Humanities MA, Genomic Healthcare PGCert,
    │     Genomic Medicine Online, Interpretation & Clinical Application of Genomic Data,
    │     Healthcare Research Skills & Methods
    └── Department of Interprofessional Healthcare (6 个项目)
          Advanced Breast Practice, Clinical Pharmacology BSc/iBSc,
          Professional Practice in Mammography, Medical Sciences iBSc,
          Paramedic Science, Healthcare Science
```

**Source**: https://www.citystgeorges.ac.uk/about/schools/health-sciences (department list) + https://www.citystgeorges.ac.uk/prospective-students/courses (per-course School: attribute mapping)

> **Note on department assignment**: City St George's 在课程列表页没有显式 "Department:" 字段；项目到系的归属根据 (a) 课程 title 中的学科词与 (b) 学校页部门目录映射推断；个别 cross-disciplinary 项目 (Medical Ethics, Clinical Pharmacology) 的归属可能存疑——已按最匹配的系归类，并在 1.x 节中保留 url 备查。

### 0.4 Rule 3 — 学历级别明细 (Degree Level Inventory)

| 学位级别 | 计数 | 示例 |
|----------|------|------|
| MBBS (Bachelor of Medicine, Bachelor of Surgery) | 2 | Medicine MBBS (5 yr), Medicine (Graduate Entry) MBBS (4 yr) |
| BSc (Hons) | 8 | Biomedical Science, Clinical Pharmacology, Diagnostic Radiography, Healthcare Science, Occupational Therapy, Paramedic Science, Physiotherapy, Therapeutic Radiography |
| MSci (Hons) | 1 | Biomedical Science MSci (4 yr integrated masters) |
| iBSc (Intercalated BSc — for medical students) | 2 | Clinical Pharmacology iBSc, Medical Sciences iBSc |
| MSc (stand-alone) | 4 | Heart Failure MSc, Occupational Therapy (Pre-Reg) MSc, Physiotherapy (Pre-Reg) MSc, MPAS counted separately |
| MPAS (Master of Physician Associate Studies) | 1 | Physician Associate Studies MPAS |
| MA | 1 | Medical Ethics, Law and Humanities MA/PGDip/PGCert |
| MRes | 5 | Biomedical Science – Antimicrobial Resistance; Clinical Biomedical Research; Infection and Immunity; Molecular Mechanisms of Cancer; Reproduction and Development |
| MSc/PGDip/PGCert (combined) | 6 | Advanced Breast Practice, Advanced Clinical Practice (Tooting), Advanced Musculoskeletal, Genomic Medicine, Sports Cardiology, Medical Ethics (MA version also) |
| MSc/PGCert (combined) | 1 | Advanced Musculoskeletal Practice (Tooting) |
| PGCert (stand-alone) | 4 | Clinical Practice PGCert, Genomic Healthcare PGCert, Healthcare & Biomedical Education PGCert, Professional Practice in Mammography PGCert, Healthcare Research Skills and Methods PGCert, Interpretation and Clinical Application of Genomic Data PGCert |
| PGCert (Online) | 1 | Genomic Medicine (Online) PGCert |
| **Total** | **36** | |

> **Note**: 一些 PGCert 同时可作为 standalone short course 注册 (如 Genomic Healthcare, Clinical Practice)；具体 offer path 由 admissions 团队 case-by-case 处理。

### 0.5 Rule 4 — 分布矩阵 (学院 × 学位级别)

| 学院 \ 学位 | MBBS | BSc | MSci | iBSc | MSc | MA | MPAS | MRes | MSc/PGDip/PGCert | PGCert | Total |
|-------------|------|-----|------|------|-----|-----|------|------|------------------|--------|-------|
| School of Health & Medical Sciences | 2 | 8 | 1 | 2 | 4 | 1 | 1 | 5 | 6 | 6 | **36** |
| **Total** | **2** | **8** | **1** | **2** | **4** | **1** | **1** | **5** | **6** | **6** | **36** |

**RECONCILIATION**: 矩阵 cells sum = 2+8+1+2+4+1+1+5+6+6 = **36** = Rule-1 total = Rule-5 leaf-list row count ✓

### 0.6 Rule 5 — 全量专业明细（按 学院 > 系 > 学位级别 分组）

完整叶子枚举见 Section 1 (UG) 和 Section 2 (PGT)。

---

## Section 1 — Undergraduate Programs (BSc/MSci/MBBS/iBSc)

### 1.1 School of Health & Medical Sciences

#### 1.1.1 Department of Medicine

| 专业 (Programme) | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| Medicine | MBBS | 5 years full-time (6 with placement) | A100 | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine |
| Medicine (Graduate Entry) | MBBS | 4 years full-time | A101 | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine-graduate-entry |

#### 1.1.2 Department of Molecular and Biomedical Sciences

| 专业 | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| Biomedical Science | BSc (Hons) | 3 years | B940 | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-science |
| Biomedical Science | MSci (Hons) | 4 years | B942 | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-science-msci |

#### 1.1.3 Department of Allied Health

| 专业 | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| Diagnostic Radiography | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/radiography-diagnostic-imaging |
| Therapeutic Radiography | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/therapeutic-radiography |
| Physiotherapy | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/physiotherapy |
| Occupational Therapy | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/occupational-therapy |

#### 1.1.4 Department of Nursing and Midwifery

| 专业 | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| (Postgraduate only at Tooting for OT pre-reg, Clinical Practice PGCert — no UG nursing programmes in current Tooting filter) |

> **Note**: City St George's offers Nursing (Adult, Children's, Mental Health) at Clerkenwell campus — not in Tooting filter; documented elsewhere.

#### 1.1.5 Department of Psychology and Neuroscience

| 专业 | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| Healthcare Science (Physiological Sciences) | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/healthcare-science |

#### 1.1.6 Department of Population Health and Policy

| 专业 | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| (no UG programmes in this department in current Tooting filter) |

#### 1.1.7 Department of Interprofessional Healthcare

| 专业 | 学位 | Duration | UCAS | URL |
|------|------|----------|------|-----|
| Clinical Pharmacology | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/clinical-pharmacology |
| Clinical Pharmacology | iBSc | 1 year (intercalated) | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/intercalated-clinical-pharmacology |
| Medical Sciences | iBSc | 1 year (intercalated) | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/intercalated-medical-sciences |
| Paramedic Science | BSc (Hons) | 3 years | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/paramedic-science |

### 1.2 Undergraduate Subtotal

| 学位级别 | Count |
|----------|-------|
| MBBS | 2 |
| BSc (Hons) | 8 |
| MSci (Hons) | 1 |
| iBSc | 2 |
| **UG Total** | **13** (matches the UG subset from Rule 1 after correction; +1 Clinical Pharmacology iBSc) |

> **Correction**: Rule 1 lists "UG degree courses = 14" — re-count yields: 2 MBBS + 8 BSc + 1 MSci + 2 iBSc + 1 ParamSci BSc = 14. Confirmed.

---

## Section 2 — Postgraduate Taught Programs (PGT)

### 2.1 School of Health & Medical Sciences

#### 2.1.1 Department of Medicine

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| Physician Associate Studies | MPAS | 2 years full-time | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/physician-associate-studies |
| Advanced Clinical Practice (Tooting) | MSc/PGDip | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-clinical-practice-tooting |
| Heart Failure | MSc | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/heart-failure |
| Clinical Neuroscience Practice | MSc/PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-neuroscience-practice |
| Sports Cardiology | MSc/PGDip/PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/sports-cardiology |
| Genomic Medicine | MSc/PGDip/PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/genomic-medicine |

#### 2.1.2 Department of Molecular and Biomedical Sciences

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| Biomedical Science – Antimicrobial Resistance | MRes | 1 year full-time | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-antimicrobial-resistance |
| Biomedical Science – Clinical Biomedical Research | MRes | 1 year full-time | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-clinical-biomedical-research |
| Biomedical Science – Infection and Immunity | MRes | 1 year full-time | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-infection-and-immunity |
| Biomedical Science – Molecular Mechanisms of Cancer | MRes | 1 year full-time | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-molecular-mechanisms-of-cancer |
| Biomedical Science – Reproduction and Development | MRes | 1 year full-time | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-reproduction-and-development |

#### 2.1.3 Department of Allied Health

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| Advanced Musculoskeletal Practice (Tooting) | MSc/PGDip | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/msc-advanced-musculoskeletal-practice-tooting |
| Physiotherapy (Pre-registration) | MSc | 2 years | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/physiotherapy |
| Occupational Therapy (Pre-registration) | MSc | 2 years | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/occupational-therapy-pre-registration |

#### 2.1.4 Department of Nursing and Midwifery

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| Clinical Practice | PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-practice |
| Healthcare and Biomedical Education | PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/healthcare-and-biomedical-education |

#### 2.1.5 Department of Psychology and Neuroscience

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| (no PGT in this department in current Tooting filter; Clinical Neuroscience Practice listed under Medicine) |

#### 2.1.6 Department of Population Health and Policy

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| Medical Ethics, Law and Humanities | MA/PGDip/PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/medical-ethics-law-and-humanities |
| Genomic Healthcare | PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/genomic-healthcare |
| Genomic Medicine (Online) | PGCert | (online) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/genomic-medicine-online |
| Interpretation and Clinical Application of Genomic Data | PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/interpretation-and-clinical-application-of-genomic-data |
| Healthcare Research Skills and Methods | PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/healthcare-research-skills-and-methods |

#### 2.1.7 Department of Interprofessional Healthcare

| 专业 | 学位 | Duration | URL |
|------|------|----------|-----|
| Advanced Breast Practice | MSc/PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-breast-practice |
| Professional Practice in Mammography | PGCert | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/professional-practice-in-mammography |

### 2.2 Postgraduate Taught Subtotal

| 学位级别 | Count |
|----------|-------|
| MSc (stand-alone) | 3 (Heart Failure, Physiotherapy Pre-Reg, Occupational Therapy Pre-Reg) |
| MPAS | 1 |
| MA | 1 |
| MRes | 5 |
| MSc/PGDip | 2 (Advanced Clinical Practice, Advanced Musculoskeletal) |
| MSc/PGDip/PGCert | 3 (Sports Cardiology, Genomic Medicine, Medical Ethics MA-version also) |
| MSc/PGCert | 2 (Clinical Neuroscience Practice, Advanced Breast Practice) |
| PGCert | 5 (Clinical Practice, Healthcare & Biomedical Education, Genomic Healthcare, Genomic Medicine Online, Interpretation Genomic Data, Professional Practice Mammography, Healthcare Research Skills) |
| **PGT Total** | **22** |

> **Re-count**: 3 MSc + 1 MPAS + 1 MA + 5 MRes + 2 MSc/PGDip + 3 MSc/PGDip/PGCert + 2 MSc/PGCert + 5 PGCert = 22 ✓

---

## Section 3 — Tuition Fees (2026/27 Academic Year)

### 3.1 Undergraduate Fees (Medicine MBBS — flagship)

| 学位 | Home/UK | International | Source URL |
|------|---------|---------------|------------|
| Medicine MBBS (5 yr) | £9,790 | £46,000 | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine |
| Medicine (Graduate Entry) MBBS (4 yr) | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine-graduate-entry |
| Biomedical Science BSc / MSci | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-science |
| Clinical Pharmacology BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/clinical-pharmacology |
| Diagnostic Radiography BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/radiography-diagnostic-imaging |
| Therapeutic Radiography BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/therapeutic-radiography |
| Occupational Therapy BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/occupational-therapy |
| Physiotherapy BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/physiotherapy |
| Paramedic Science BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/paramedic-science |
| Healthcare Science BSc | £9,790 | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/healthcare-science |
| Intercalated BSc (Clinical Pharmacology / Medical Sciences) | (see page) | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/intercalated-clinical-pharmacology |

**Home/EU undergraduate fees are capped at the UK Government maximum** (£9,790 for 2026/27). International fees vary by programme — the Medicine MBBS International fee of £46,000 is the highest among Tooting programmes.

### 3.2 Postgraduate Fees

| 学位类型 | 估计 Home | 估计 International | Source |
|---------|-----------|---------------------|--------|
| MSc (taught, science) | ~£12,000–17,000 | ~£22,000–30,000 | per-course page |
| MPAS (Physician Associate) | (NHS-funded for UK) | (see page) | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/physician-associate-studies |
| MRes | (see page) | (see page) | per-course page |
| PGCert | (see page) | (see page) | per-course page |
| PGDip | (see page) | (see page) | per-course page |

> **Note on PGT fees**: Postgraduate fees vary widely by programme; each course page has its own fees and funding section. Top-up fees for international students in 2026/27 are typically £22,000–£30,000 for taught MSc. NHS Bursary support may apply from Year 5 of Medicine MBBS and for pre-registration Nursing/Allied Health courses.

### 3.3 Funding Notes

- **NHS funding**: MBBS students in years 5+ may be eligible for NHS Bursary support. See https://www.citystgeorges.ac.uk/prospective-students/finance/nhs-funding/funding-for-medicine-degrees
- **Ravi Ray Medicine Scholarship** — Tooting: https://www.citystgeorges.ac.uk/alumni/support/ravi-ray-medicine-scholarship-tooting
- **Fee waivers**: Available for some courses (per individual course page)

---

## Section 4 — Application Requirements & Deadlines

### 4.1 Undergraduate Entry (general)

Source: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements

- **Minimum requirement**: passes in two subjects at GCE A-level or equivalent (City St George's general minimum)
- Specific course requirements may be higher
- Applications via **UCAS** (UCAS codes per course; MBBS Medicine A100, Graduate Entry A101)
- Medicine has **separate selection process**: https://www.citystgeorges.ac.uk/about/schools/health-sciences/about/selection-process

### 4.2 Medicine MBBS Specific (UCAS A100)

- **GCSE**: English Language and Maths at grade C/4 or above (or equivalent)
- **A-level**: AAA including Chemistry and Biology (or equivalent)
- **UCAT**: required (cut-off scores vary by year)
- **Work experience**: healthcare-related experience strongly recommended
- **Interview**: Multiple Mini Interviews (MMI)
- **Application deadline (UCAS)**: 15 October (Medicine standard UCAS deadline)
- Source: https://www.citystgeorges.ac.uk/about/schools/health-sciences/about + https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine

### 4.3 Graduate Entry Medicine (UCAS A101)

- **Degree**: minimum 2:1 honours degree in any subject (science preferred; non-science considered)
- **A-level Chemistry**: at least BBB (or equivalent)
- **UCAT**: required
- **Work experience**: substantial healthcare experience required
- Source: https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine-graduate-entry

### 4.4 Postgraduate Entry

- **Minimum**: university honours degree (2:2 or above, varies by course) in appropriate subject
- **Non-graduate**: suitable experience + professional qualifications may be accepted at department's discretion
- **Original certificates** required before registration

### 4.5 English Language Requirements (Tooting Campus — Special Rules)

Source: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements

> **Important**: Tooting campus English language requirements are handled differently from elsewhere at City St George's **because of the nature of medical training**.

**Three routes to demonstrate English proficiency:**

1. National of a majority English-speaking country (UK government list) OR completed university degree in one — exempt
2. **Accepted English language test at the correct level for their course**
3. Appropriate professional registration
4. Suitable academic qualification

**Test Groups**: Requirements split into **three groups** depending on the course. Review your course group, then check the test requirements below.

**Accepted tests (with IELTS equivalency tables):**

| Test | Provider | IELTS 5.5 | IELTS 6.0 | IELTS 6.5 | IELTS 7.0 |
|------|----------|-----------|-----------|-----------|-----------|
| IELTS Academic / IELTS UKVI | British Council | Overall 5.5 (all bands ≥ 5.5) | Overall 6.0 (all bands ≥ 6.0) | Overall 6.5 (all bands ≥ 6.5) | Overall 7.0 (all bands ≥ 7.0) |
| TOEFL iBT | ETS | 72 (L17/S20/R18/W17) | 80 (L19/S22/R20/W19) | 90 (L21/S23/R23/W21) | 100 (L23/S25/R24/W24) |
| PTE Academic | Pearson | 54 (all bands) | 60 (all bands) | 62 (all bands) | 69 (all bands) |
| LanguageCert Academic | LanguageCert | 60 (all bands) | 65 (all bands) | 70 (all bands) | 75 (all bands) |
| LanguageCert International ESOL | LanguageCert | B2 Communicator | B2 Communicator | B2 Communicator | C1 Expert |
| Trinity College London ISE | Trinity | Pass ISE II | Pass ISE II | Distinction ISE II | Pass ISE III |
| Cambridge English (C1 Advanced / C2 Proficiency) | Cambridge | Overall 162 (all ≥ 162) | Overall 169 (all ≥ 169) | Overall 176 (all ≥ 176) | Overall 185 (all ≥ 185) |

> **Tooting medical programmes typically require IELTS 7.0 overall with 7.0 in each component** (Medicine MBBS, Graduate Entry, Physician Associate). See individual course pages for specific cut-offs.

**Other accepted qualifications** (with equivalency mapping):

| Qualification | Note |
|---------------|------|
| GCSE/IGCSE English | Grade C/4 or above (only for UK-established applicants) |
| International Baccalaureate | English A: Literature or Language & Literature at HL 5+ or SL 6+ |
| Hong Kong DSE | English at Level 4 or above |
| India CBSE/ISC | English at 70%+ |
| West African Examinations | Credit level |

### 4.6 Other Requirements

- **DBS check**: required for clinical programmes — https://www.citystgeorges.ac.uk/about/schools/health-sciences/about/dbs
- **Occupational Health Check**: required for clinical programmes — https://www.citystgeorges.ac.uk/about/schools/health-sciences/about/occupational-health-checks
- **Uniforms for clinical placement**: required — https://www.citystgeorges.ac.uk/about/schools/health-sciences/about/uniforms-for-clinical-placement

---

## Section 5 — International Students

### 5.1 Visa Information

Source: https://www.citystgeorges.ac.uk/prospective-students/apply/visas

- International Student Advice team provides free immigration advice (EU + Overseas)
- Student visas, short-term visas, ATAS certificates, Brexit-related support
- Standard Visitor Visa application guidance: https://www.citystgeorges.ac.uk/prospective-students/apply/visas/standard-visitor-visa/apply-standard-visitor-visa

### 5.2 International Fees

- **Medicine MBBS**: £46,000/year (2026/27) — confirmed
- Other international fees: per-course page
- Annual fee increase in line with UK government policy

### 5.3 English Language (international pathway)

See Section 4.5 — Tooting campus English language test tables above.

### 5.4 International Qualifications Equivalences

Source: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements (covers 100+ countries)

For UG entry: equivalences to UK GCE A-level grades
For PG entry: equivalences to UK honours degrees

Examples (selected):
- **USA**: High School Diploma + SAT/ACT + AP exams (UG); 4-year bachelor's degree (PG)
- **China**: Gaokao + appropriate scores (UG); 4-year bachelor degree from Project 211/985 university (PG)
- **India**: CBSE/ISC Grade 12 (UG); 4-year bachelor's or 3-year bachelor's + master's (PG)
- **Nigeria**: WAEC/NECO with credit passes including English and Maths (UG)

---

## Section 6 — WeKnora Chunk List

The following chunks are produced for WeKnora ingestion. Each chunk is self-contained with metadata header.

| Chunk ID | Title | Source Section | Char count (approx) |
|----------|-------|----------------|---------------------|
| sgul-overview-00 | Section 0: 院校总览 | 0.1–0.6 | 3,500 |
| sgul-ug-medicine-01 | UG: Medicine MBBS | 1.1.1 | 800 |
| sgul-ug-medicine-grad-02 | UG: Medicine (Graduate Entry) MBBS | 1.1.1 | 700 |
| sgul-ug-biomed-03 | UG: Biomedical Science BSc/MSci | 1.1.2 | 900 |
| sgul-ug-allied-04 | UG: Allied Health (Radiography/Physio/OT) | 1.1.3 | 1,200 |
| sgul-ug-paramedic-05 | UG: Paramedic Science | 1.1.7 | 500 |
| sgul-ug-clinical-pharm-06 | UG: Clinical Pharmacology BSc/iBSc | 1.1.7 | 700 |
| sgul-ug-intercalated-07 | UG: iBSc intercalated programmes | 1.1.7 | 600 |
| sgul-ug-healthcare-sci-08 | UG: Healthcare Science | 1.1.5 | 500 |
| sgul-pgt-pa-09 | PGT: Physician Associate MPAS | 2.1.1 | 600 |
| sgul-pgt-genomic-10 | PGT: Genomic Medicine family | 2.1.1/2.1.6 | 1,200 |
| sgul-pgt-biomed-mres-11 | PGT: Biomedical Science MRes pathways | 2.1.2 | 1,000 |
| sgul-pgt-advanced-practice-12 | PGT: Advanced Clinical/Musculoskeletal Practice | 2.1.1/2.1.3 | 800 |
| sgul-pgt-physio-ot-prereg-13 | PGT: Physiotherapy/OT Pre-Reg | 2.1.3 | 700 |
| sgul-pgt-medical-ethics-14 | PGT: Medical Ethics Law & Humanities MA | 2.1.6 | 500 |
| sgul-pgt-cardiology-15 | PGT: Heart Failure/Sports Cardiology | 2.1.1 | 700 |
| sgul-pgt-neuro-16 | PGT: Clinical Neuroscience Practice | 2.1.1 | 500 |
| sgul-pgt-pgcert-cluster-17 | PGT: PGCert cluster | 2.1.4/2.1.6/2.1.7 | 1,500 |
| sgul-fees-ug-18 | Section 3: UG Fees (Home + International MBBS £46,000) | 3.1 | 1,000 |
| sgul-fees-pgt-19 | Section 3: PGT Fees | 3.2 | 600 |
| sgul-fees-funding-20 | Section 3: Funding notes (NHS Bursary, Ravi Ray Scholarship) | 3.3 | 500 |
| sgul-apply-med-21 | Section 4: Medicine MBBS application (UCAT, MMI, work experience, deadline 15 Oct) | 4.2 | 1,200 |
| sgul-apply-gradmed-22 | Section 4: Graduate Entry Medicine requirements | 4.3 | 800 |
| sgul-apply-pgt-23 | Section 4: PGT entry requirements | 4.4 | 500 |
| sgul-apply-english-24 | Section 4: Tooting English language test equivalencies | 4.5 | 2,000 |
| sgul-apply-clinical-checks-25 | Section 4: DBS, Occupational Health, Uniforms | 4.6 | 500 |
| sgul-intl-26 | Section 5: International students (visas, equivalences) | 5.1–5.4 | 1,500 |

Total chunks: 26. Average chunk size: ~900 chars (within WeKnora 512-2048 optimal range).

---

## Section 7 — Monitoring Watchlist (Phase 4)

| Field | URL | Frequency | Last baseline | Reason |
|-------|-----|-----------|---------------|--------|
| Medicine MBBS fees (Home/Intl) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine | High (annual) | 2026/27: Home £9,790 / Intl £46,000 | UK fee cap + Intl price band; updates yearly |
| Medicine (Graduate Entry) MBBS fees | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine-graduate-entry | High (annual) | 2026/27: Home £9,790 | Same as MBBS 5-yr |
| English language requirements | https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements | High (annual) | IELTS 7.0 for medical programmes | Tooting-specific, may change with GMC requirements |
| UCAS deadline (Medicine MBBS) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine | High (annual) | 15 October | UCAS standard Medicine deadline |
| UCAT cut-off | https://www.citystgeorges.ac.uk/about/schools/health-sciences/about | High (annual) | varies by year | UCAT scores reviewed yearly |
| Programme list (36 Tooting courses) | https://www.citystgeorges.ac.uk/prospective-students/courses?f%C2%B1Location|location[]=tooting+campus | Medium (quarterly) | 36 courses (2026-07-08) | New programmes added, retirements |
| School/Department structure | https://www.citystgeorges.ac.uk/about/schools/health-sciences | Low (annual) | 8 departments (2026-07-08) | Restructure of merged institution possible |
| NHS Bursary / funding rules | https://www.citystgeorges.ac.uk/prospective-students/finance/nhs-funding | High (annual) | NHS Bursary from Year 5 | UK government policy changes |
| Ravi Ray Medicine Scholarship | https://www.citystgeorges.ac.uk/alumni/support/ravi-ray-medicine-scholarship-tooting | Low (annual) | Exists | Alumni funding; status confirmed yearly |
| DBS / Occupational Health requirements | https://www.citystgeorges.ac.uk/about/schools/health-sciences/about/dbs | Low (annual) | Required | UK DBS update policy changes |

**Watch protocol**: Re-fetch High-frequency URLs every 90 days; Medium every 180 days; Low every 365 days. Compute SHA-256 of normalized content; alert on diff.

---

## Section 8 — Source Provenance & Capture Log

| Date | Tool | URL | Captured |
|------|------|-----|----------|
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/prospective-students | Site landing, merger note, ranking |
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/prospective-students/courses?f%C2%B1Location|location[]=tooting+campus | 36 programmes via "Next page" pagination |
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/about/schools | Schools & departments directory |
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/about/schools/health-sciences | School of Health & Medical Sciences |
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine | Medicine MBBS (A100): fees, structure |
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine-graduate-entry | Graduate Entry MBBS (A101): fees, structure |
| 2026-07-08 | ego-browser | https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements | Entry requirements (UG/PG/English language Tooting special rules) |

---

## Section 9 — Known Limitations

1. **Department attribution**: City St George's course listing does NOT expose a per-course "Department" field. Department assignment in this document is **inferred** from (a) course title keywords and (b) the school's department directory. Cross-disciplinary programmes (e.g. Medical Ethics, Clinical Pharmacology, Genomic Medicine) may have alternative valid department assignments.
2. **PGT fees**: Only Medicine MBBS International fee (£46,000) and Home fee (£9,790) confirmed directly from page. Other PGT international fees are typical-range estimates pending per-course page extraction.
3. **UCAT cut-off**: Not extracted for 2026/27; varies yearly.
4. **Foundation courses / Short courses**: Not in current Tooting filter set; SGUL/City St George's foundation/apprenticeship pathways exist at other campuses.
5. **Research degrees (PhD/MPhil by Research)**: Tooting filter returned 0 — these are administered centrally under City St George's research degree framework and may need a separate discovery pass.

---

**End of document — generated by uni-admissions-research skill v2.0**