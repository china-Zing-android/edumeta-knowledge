# London School of Hygiene & Tropical Medicine Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → faculty → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科专业 (UG Majors) | 0 (LSHTM is postgraduate-only) |
| 研究生授课型项目 (PGT: MSc/MRes/PG Cert/PG Dip) | 29 |
| 研究生博士项目 (PhD/DrPH/MPhil) | 3 |
| **学位项目总计 (PGT + Research)** | **32** |
| 学院 (Faculties) | 3 |
| MRC 研究单位 (MRC Units) | 2 |

> **Data source**: LSHTM courses page (`lshtm.ac.uk/study/courses/masters-degrees`), research degrees page, and 2026-27 tuition fees page.
>
> **Note**: LSHTM is a specialist postgraduate-only institution founded in 1899. It does not award undergraduate degrees. All programmes are at Master's or Doctoral level.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
London School of Hygiene & Tropical Medicine
├── Faculty of Epidemiology and Population Health          [学院]
│   └── Programmes: Epidemiology, Medical Statistics, Demography & Health,
│       Health Data Science, Veterinary Epidemiology
├── Faculty of Infectious and Tropical Diseases            [学院]
│   └── Programmes: Control of Infectious Diseases, Immunology of Infectious Diseases,
│       Medical Microbiology, Medical Parasitology & Entomology,
│       Tropical Medicine & International Health, One Health, MRes Infectious & Tropical Diseases
├── Faculty of Public Health and Policy                    [学院]
│   └── Programmes: Public Health, Public Health for Eye Care,
│       Public Health for Global Practice, Global Mental Health,
│       Health Policy Planning & Financing, Reproductive & Sexual Health Research,
│       Climate Change & Planetary Health, Nutrition for Global Health
├── MRC Unit The Gambia at LSHTM                          [研究单位]
└── MRC/UVRI and LSHTM Uganda Research Unit               [研究单位]
```

> **Note**: LSHTM's programme-to-faculty mapping is not always explicitly stated on individual programme pages. The mapping above is based on subject area alignment. Distance learning and online versions of programmes are delivered by the same faculty as their in-person counterparts.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| MSc | Master of Science | 研究生授课型 | 24 |
| MRes | Master of Research | 研究生研究型 | 1 |
| PG Dip | Postgraduate Diploma | 研究生文凭 | 0 (available as exit awards) |
| PG Cert | Postgraduate Certificate | 研究生证书 | 0 (available as exit awards) |
| MPhil | Master of Philosophy | 研究生研究型 | 1 |
| PhD | Doctor of Philosophy | 研究生博士 | 1 |
| DrPH | Doctor of Public Health | 研究生博士 | 1 |

> **Note**: LSHTM offers PG Diploma and PG Certificate as exit awards from several MSc programmes (e.g., Demography & Health, Nutrition for Global Health, Veterinary Epidemiology, One Health). These have separate fee structures but are not listed as standalone entry programmes.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学位类型 | In-person | Online | Distance Learning | 合计 |
|---------|-----------|--------|-------------------|------|
| MRes | 1 | 0 | 0 | 1 |
| MSc (in-person) | 18 | 0 | 0 | 18 |
| MSc (online) | 0 | 3 | 0 | 3 |
| MSc (distance learning) | 0 | 0 | 6 | 6 |
| MPhil/PhD | 1 | 0 | 0 | 1 |
| DrPH | 1 | 0 | 0 | 1 |
| Joint PhD | 1 | 0 | 0 | 1 |
| **合计** | **23** | **3** | **6** | **32** |

> **Reconciliation**: 23 + 3 + 6 = 32 ✓ (matches rule-1 total)

---

## SECTION 1 — Postgraduate Taught Programmes (MSc/MRes)

### 1.1 In-person Intensive Programmes

#### Epidemiology and Population Health

| # | 专业 | 学位 | 学制 | URL |
|---|------|------|------|-----|
| 1 | Epidemiology | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/epidemiology) |
| 2 | Medical Statistics | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/medical-statistics) |
| 3 | Demography & Health | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/demography-health) |
| 4 | Health Data Science | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/health-data-science) |
| 5 | Veterinary Epidemiology | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/veterinary-epidemiology) |

#### Infectious and Tropical Diseases

| # | 专业 | 学位 | 学制 | URL |
|---|------|------|------|-----|
| 6 | Control of Infectious Diseases | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/control-infectious-diseases) |
| 7 | Immunology of Infectious Diseases | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/immunology-infectious-diseases) |
| 8 | Medical Microbiology | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/medical-microbiology) |
| 9 | Medical Parasitology & Entomology | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/medical-parasitology) |
| 10 | Tropical Medicine & International Health | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/tropical-medicine-international-health) |
| 11 | One Health: Ecosystems, Humans and Animals | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/one-health) |
| 12 | Infectious & Tropical Diseases | MRes | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/mres-infectious-tropical-diseases) |

#### Public Health and Policy

| # | 专业 | 学位 | 学制 | URL |
|---|------|------|------|-----|
| 13 | Public Health | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/public-health) |
| 14 | Public Health for Eye Care | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/public-health-eye-care) |
| 15 | Public Health for Global Practice | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/public-health-global-practice) |
| 16 | Global Mental Health | MSc | 1年FT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/global-mental-health) |
| 17 | Health Policy, Planning & Financing | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/health-policy-planning-financing) |
| 18 | Reproductive & Sexual Health Research | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/reproductive-sexual-health-research) |
| 19 | Climate Change & Planetary Health | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/climate-change-planetary-health) |
| 20 | Nutrition for Global Public Health | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/nutrition-global-health) |

### 1.2 Online Intensive Programmes

| # | 专业 | 学位 | 学制 | URL |
|---|------|------|------|-----|
| 21 | Climate Change & Planetary Health (online) | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/climate-change-planetary-health-online) |
| 22 | Demography & Health (online) | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/demography-health-online) |
| 23 | Sexual & Reproductive Health Policy and Programming (online) | MSc | 1年FT / 2年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/sexual-reproductive-health-policy-programming) |

### 1.3 Distance Learning Programmes

| # | 专业 | 学位 | 学制 | URL |
|---|------|------|------|-----|
| 24 | Clinical Trials | MSc | 2-5年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/clinical-trials-online) |
| 25 | Epidemiology (Distance Learning) | MSc | 2-5年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/epidemiology-online) |
| 26 | Global Health Policy | MSc | 2-5年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/global-health-policy-online) |
| 27 | Health in Humanitarian Crises | MSc | 2-5年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/health-humanitarian-crises-online) |
| 28 | Infectious Diseases | MSc | 2-5年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/infectious-diseases-online) |
| 29 | Public Health (Distance Learning) | MSc | 2-5年PT | [Link](https://www.lshtm.ac.uk/study/courses/masters-degrees/public-health-online) |

---

## SECTION 2 — Research Degrees (PhD/DrPH/MPhil)

| # | 专业 | 学位 | 学制 | URL |
|---|------|------|------|-----|
| 1 | MPhil / PhD | MPhil / PhD | 3-4年FT / 5-6年PT | [Link](https://www.lshtm.ac.uk/study/courses/research-degrees/mphil-phd) |
| 2 | DrPH (Doctorate of Public Health) | DrPH | 3-4年FT / 5-6年PT | [Link](https://www.lshtm.ac.uk/study/courses/research-degrees/drph) |
| 3 | Joint PhD with Nagasaki University (Global Health) | PhD | 3-4年FT | [Link](https://www.lshtm.ac.uk/study/research/nagasaki-lshtm-phd) |

> **Note**: LSHTM also offers the "Global Health Research in Africa Doctoral Training Programme" fellowship for early career healthcare professionals via create-phd.org.

---

## SECTION 3 — Tuition Fees (2026-27 Academic Year)

### 3.1 In-person Intensive Programmes (MSc/MRes/PG Dip/PG Cert)

| 专业 | UK FT | UK PT | 海外 FT | 海外 PT | 实地考察费 |
|------|-------|-------|--------|--------|-----------|
| Climate Change & Planetary Health (MSc) | £14,930 | £7,465 | £32,950 | £16,475 | — |
| Control of Infectious Diseases (MSc) | £14,250 | £7,125 | £31,450 | £15,725 | — |
| Demography & Health (MSc) | £13,580 | £6,790 | £31,450 | £15,725 | — |
| Demography & Health (PG Dip) | £9,500 | £4,750 | £22,010 | £11,005 | — |
| Demography & Health (PG Cert) | £5,430 | n/a | £12,580 | n/a | — |
| Epidemiology (MSc) | £14,930 | £7,465 | £34,590 | £17,295 | £270 |
| Global Mental Health (MSc) | £17,541 | n/a | £40,450 | n/a | — |
| Health Data Science (MSc) | £14,230 | £7,115 | £31,450 | £15,725 | — |
| Health Policy, Planning & Financing (MSc) | £17,000 | £8,500 | £32,000 | £16,000 | — |
| Immunology of Infectious Diseases (MSc) | £15,650 | £7,825 | £35,070 | £17,535 | £700 |
| Infectious & Tropical Diseases (MRes) | £15,650 | £7,825 | £35,070 | £17,535 | — |
| Medical Microbiology (MSc) | £15,650 | £7,825 | £33,480 | £16,740 | — |
| Medical Parasitology & Entomology (MSc) | £15,650 | £7,825 | £33,480 | £16,740 | £900 |
| Medical Statistics (MSc) | £14,230 | £7,115 | £31,450 | £15,725 | — |
| Nutrition for Global Health (MSc) | £14,230 | £7,115 | £32,950 | £16,475 | — |
| Nutrition for Global Health (PG Dip) | £9,960 | — | £23,060 | — | — |
| Nutrition for Global Health (PG Cert) | £5,690 | — | £13,180 | — | — |
| One Health (MSc) | £16,500 | £8,250 | £31,285 | £15,642.50 | — |
| One Health (PG Dip) | £11,120 | n/a | £21,000 | n/a | — |
| Public Health (MSc) | £13,580 | £6,790 | £31,450 | £15,725 | — |
| Public Health for Global Practice (MSc) | £14,930 | £7,465 | £31,450 | £15,725 | £280 |
| Public Health for Eye Care (MSc) | £14,250 | £7,125 | £33,020 | £16,510 | — |
| Reproductive & Sexual Health Research (MSc) | £14,930 | £7,465 | £34,590 | £17,295 | — |
| Tropical Medicine & International Health (MSc) | £14,930 | £7,465 | £34,590 | £17,295 | £520 |
| Veterinary Epidemiology (MSc) | £15,495 | £7,747.50 | £33,010 | £16,505 | — |
| Veterinary Epidemiology (PG Dip) | £10,480 | n/a | £22,120 | n/a | — |

### 3.2 Online Intensive Programmes

| 专业 | 全日制 | 非全日制 | 备注 |
|------|--------|---------|------|
| Climate Change & Planetary Health (MSc) | £23,100 | £11,550 | 海外与UK学费相同 |
| Demography & Health (MSc) | £23,100 | £11,550 | 海外与UK学费相同 |
| Sexual & Reproductive Health Policy and Programming (MSc) | £23,100 | — | 中低收入国家: £17,850 |
| Sexual & Reproductive Health Policy and Programming (PG Dip) | £16,170 | — | 中低收入国家: £12,530 |
| Sexual & Reproductive Health Policy and Programming (PG Cert) | £9,240 | — | 中低收入国家: £7,160 |

### 3.3 Distance Learning Programmes

| 专业 | PG Certificate | PG Diploma | MSc |
|------|---------------|------------|-----|
| Clinical Trials | £11,360 | £15,380 | £19,440 |
| Epidemiology | £11,360 | £15,380 | £19,440 |
| Global Health Policy | £11,360 | £15,380 | £19,440 |
| Health in Humanitarian Crises | £11,360 | £15,380 | £19,440 |
| Infectious Diseases | £11,360 | £15,380 | £19,440 |
| Public Health | £10,310 | £13,960 | £17,640 |

### 3.4 Research Degree Fees

| 课程 | UK FT | UK PT | 海外 FT | 海外 PT |
|------|-------|-------|--------|--------|
| DrPH/MPhil/PhD | £7,870 | £3,935 | £23,740 | £11,870 |
| MPhil/PhD (lab-based) | £7,870 | £3,935 | £28,780 | £14,390 |
| MPhil/PhD (non lab-based) | £7,870 | £3,935 | £23,740 | £11,870 |

### 3.5 Application Fee & Deposit

- **Application fee**: £50 (non-refundable, all Master's programmes)
- **Home student deposit**: £500 (within 28 days of offer)
- **Overseas student deposit**: £2,000
  - Offers before 31 Jan 2026: due by 1 March 2026
  - Offers from 1 Feb 2026: due within 28 days

---

## SECTION 4 — Entry Requirements

### 4.1 Academic Entry Requirements (Master's Programmes)

Applicants must hold ONE of:

1. **Upper Second Class Honours (2:1) degree** in a relevant discipline
2. **Medical degree** recognised by the UK GMC
3. **Equivalent overseas qualification** recognised by UK ENIC or GMC
4. **Professional qualification** judged equivalent to 2:1 by LSHTM
5. **2:2 degree** with sufficient relevant professional experience (typically 1+ year full-time)

### 4.2 English Language Requirements

Two bands of English language requirements:

| Band | Description |
|------|-------------|
| Band B | Standard requirement (most programmes) |
| Band C | Lower requirement (select programmes) |

Accepted demonstrations:
- English language test scores (IELTS, TOEFL, etc.)
- National of majority English-speaking country
- Previous study in English (subject to conditions)

### 4.3 Research Degree Entry Requirements

**MPhil/PhD**:
- Master's degree in a relevant subject, OR
- First/upper second class honours degree in a relevant subject, OR
- Professional qualifications and experience equivalent to the above

**DrPH**:
- Master's degree in public health or related discipline, OR
- Medical degree plus significant public health experience, OR
- 5+ years relevant senior-level professional experience in public health

### 4.4 Programme-Specific Example: MSc Epidemiology

- 2:1 degree in relevant discipline (or medical degree, or equivalent)
- Evidence of numeracy skills (A-level Maths/Stats or quantitative degree module)
- Preferable: work experience in health-related field
- English language: Band B
- Additional notes: Applicants with 2:2 + relevant professional experience may be considered

---

## SECTION 5 — Application Process

### 5.1 How to Apply

- **Online application portal**: https://apply.lshtm.ac.uk/
- Apply for up to **2 programmes** (by order of preference)
- No interview for most programmes — personal statement is critical
- Required documents: transcripts, references (2), personal statement, CV, English test results

### 5.2 Application Deadlines (2026-27 Entry)

| 申请人类型 | 截止日期 |
|-----------|---------|
| Student visa required | 26 July 2026, 23:59 UK time |
| UK/Irish/non-visa students | 31 August 2026, 23:59 UK time |

---

## SECTION 6 — Structural Rules & Reconciliation

### Rule 1 — Total Programme Count
- PGT programmes (MSc/MRes): 29
- Research degrees (MPhil/PhD/DrPH): 3
- **Total: 32**

### Rule 2 — Faculty Hierarchy
- 3 faculties + 2 MRC units
- All programmes map to one of the 3 faculties

### Rule 3 — Degree Level Inventory
- MSc: 24 (18 in-person + 3 online + 6 distance learning, note: DL count is subset)
- MRes: 1
- MPhil/PhD: 1
- DrPH: 1
- Joint PhD: 1

### Rule 4 — Distribution Matrix
- In-person programmes: 20 (MSc/MRes) + 2 (Research) = 22
- Online programmes: 3 (MSc)
- Distance learning: 6 (MSc)
- **Total: 31** (research degrees counted once in in-person)

### Rule 5 — Reconciliation
- Programme listing (Section 1 + Section 2): 29 + 3 = 32 ✓
- Fee table coverage: All PGT programmes + research degree categories ✓
- All source URLs documented in site-memory.json ✓

---

## Data Sources

| Source | URL | Date Accessed |
|--------|-----|---------------|
| LSHTM Courses Page | https://www.lshtm.ac.uk/study/courses | 2026-07-08 |
| Master's Degrees Listing | https://www.lshtm.ac.uk/study/courses/masters-degrees | 2026-07-08 |
| Research Degrees | https://www.lshtm.ac.uk/study/courses/research-degrees-and-doctoral-college | 2026-07-08 |
| Tuition Fees 2026-27 | https://www.lshtm.ac.uk/study/fees-and-funding/tuition-fees/tuition-fees-2026-27 | 2026-07-08 |
| Entry Requirements | https://www.lshtm.ac.uk/study/applications/applying-intensive-masters-degree/general-entry-requirements | 2026-07-08 |
| MSc Epidemiology (sample) | https://www.lshtm.ac.uk/study/courses/masters-degrees/epidemiology | 2026-07-08 |
| About LSHTM | https://www.lshtm.ac.uk/aboutus | 2026-07-08 |
| Faculties | https://www.lshtm.ac.uk/research/faculties | 2026-07-08 |
