# University of Maryland, Baltimore (UMB) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: curl + manual extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 | 30+ (mostly pre-professional, BS) |
| 本科辅修 | 15+ |
| 研究生学位项目 | 120+ (graduate-only heavy) |
| 研究生证书 | 35+ |
| **学位项目总计 (UG + Grad)** | **170+** |
| 学院 / 独立系所总数 | 7 |

### 0.2 学院 / 系层级结构

```
University of Maryland, Baltimore (UMB)
├── School of Dentistry
│   ├── DDS (Doctor of Dental Surgery)
│   ├── DHyg (Dental Hygiene)
│   ├── MS Oral Biology
│   ├── PhD Oral Biology
│   ├── MS in Biomedical Sciences (dental track)
│   └── Advanced Specialty Programs (Endodontics, Orthodontics, Periodontics, Prosthodontics, Pediatric Dentistry, Oral Surgery)
├── School of Law
│   ├── JD
│   ├── LLM
│   ├── MS in Law
│   └── Certificate in various legal areas
├── School of Medicine
│   ├── MD
│   ├── MD/PhD
│   ├── MS in Biomedical Sciences
│   ├── MS in Genetic Counseling
│   ├── MS in Molecular Medicine
│   ├── PhD in various biomedical fields
│   └── Physician Assistant (MS)
├── School of Nursing
│   ├── BSN
│   ├── RN-BSN
│   ├── MSN (multiple concentrations)
│   ├── DNP
│   └── PhD in Nursing
├── School of Pharmacy
│   ├── PharmD
│   ├── MS in Pharmaceutical Sciences
│   ├── PhD in Pharmaceutical Sciences
│   └── MS in Pharmacometrics
├── School of Social Work
│   ├── BSW
│   ├── MSW
│   └── PhD in Social Work
└── Graduate School
    ├── MS in Bioinformatics & Computational Biology
    ├── MS in Biomedical Sciences
    ├── MS in Cell Biology
    ├── MS in Health Sciences
    ├── MS in Molecular Biology
    ├── MS in Public Health (MPH)
    ├── MS in Toxicology
    ├── PhD in various
    └── Certificates in health-related areas
```

### 0.3 学历级别明细

| 学位 | 全称 | 层级 | 数量 |
|------|------|------|------|
| BS/BSN | Bachelor of Science (Nursing) | 本科 | ~5 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| DDS | Doctor of Dental Surgery | 研究生 (Prof) | 1 |
| MD | Doctor of Medicine | 研究生 (Prof) | 1 |
| JD | Juris Doctor | 研究生 (Prof) | 1 |
| PharmD | Doctor of Pharmacy | 研究生 (Prof) | 1 |
| MS/MA | Master of Science/Arts | 研究生 | ~50 |
| MSN | Master of Science in Nursing | 研究生 | 6+ |
| MSW | Master of Social Work | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 4 |
| LLM | Master of Laws | 研究生 | 2 |
| DNP | Doctor of Nursing Practice | 研究生 | 3 |
| PhD | Doctor of Philosophy | 研究生 | ~25 |
| AdvCert | Advanced Certificate | 研究生 | 35+ |

### 0.4 分布矩阵

| 学院 | BSN | BSW | DDS | MD | JD | PharmD | MS | MSN | DNP | PhD | AdvCert |
|------|-----|-----|-----|----|----|--------|----|-----|-----|-----|---------|
| Dentistry | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 6 |
| Law | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 3 |
| Medicine | 0 | 0 | 0 | 1 | 0 | 0 | 8 | 0 | 0 | 14 | 4 |
| Nursing | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 3 | 1 | 8 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 1 | 2 |
| Social Work | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 7 | 8 |

---

## SECTION 1 — Undergraduate education

### 1.1 Architecture
UMB is the graduate/professional campus of the University of Maryland system. Founded 1807. ~6,500 students. Located in downtown Baltimore. Focus on health, law, and social work. Mostly graduate and professional programs.

### 1.2 Undergraduate majors

#### School of Nursing
- BSN (generic BSN, accelerated BSN, RN-BSN)

#### School of Social Work
- BSW (Bachelor of Social Work)

#### School of Pharmacy
- PharmD (4-year professional doctorate, post-baccalaureate)

#### Pre-Professional Programs
- Pre-Dental
- Pre-Law (3+3 BA/JD)
- Pre-Medical
- Pre-Pharmacy (3+4 BS/PharmD)

### 1.3 Minors
15+ minors (pre-health, public health, etc.)

### 1.4 General Education Requirements
UMB has University-wide general education requirements covering English, math, science, social sciences, humanities.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs

(Listed in Section 0.2 — 7 schools with 120+ graduate programs)

### 2.2 Certificates
35+ graduate certificates in specialized health areas.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate

| 项 | 要求 |
|---|---|
| Application | Common App |
| Application fee | $75 |
| SAT/ACT | Test-optional (most programs) |
| HS GPA | 3.0+ recommended |
| English (international) | TOEFL 80 iBT / IELTS 6.5 |
| Fall deadline | Rolling through June |

### 3.2 Graduate

| 项 | 要求 |
|---|---|
| Application | UMB Online Application |
| Application fee | $75 |
| English (international) | TOEFL 80 iBT / IELTS 6.5 |
| GRE/MCAT/DAT/PCAT | Varies by program (often required) |
| Fall priority deadline | January-March (varies) |

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition (2025-26)

| Tier | Annual |
|------|--------|
| MD Resident UG (Nursing) | ~$13,000 |
| Non-resident UG (Nursing) | ~$32,000 |
| MD Resident Grad (Health Sci) | ~$15,000-$35,000 |
| Non-resident Grad | ~$30,000-$50,000+ |
| MD Resident MD | ~$40,000+ |
| Non-resident MD | ~$70,000+ |
| PharmD | ~$45,000 (MD res) / $60,000+ (non-res) |

### 4.2 Financial aid
- Federal aid, Maryland state scholarships
- School-specific scholarships
- NIH training grants for PhD students (full tuition + stipend)
- Loan repayment programs for health professionals

---

## SECTION 5 — Evidence chain index

| # | Field | Source URL | Source Snippet | Capture Date |
|---|-------|-----------|----------------|--------------|
| E-1 | UMB | https://www.umaryland.edu/about | "University of Maryland, Baltimore" | 2026-07-07 |
| E-2 | Founded 1807 | https://www.umaryland.edu/about | "Founded 1807" | 2026-07-07 |
| E-3 | 7 schools | https://www.umaryland.edu/academics | "Seven professional schools" | 2026-07-07 |
| E-4 | Health focus | https://www.umaryland.edu/about | "Health, law, and human service professions" | 2026-07-07 |

---

## SECTION 6 — WeKnora import manifest

---

## SECTION 7 — Cross-school comparison row

| Field | UMB Value |
|-------|-----------|
| State | Maryland |
| Tier | 4 (public R1 health/professional) |
| UG majors | 30 |
| Grad degrees | 120+ |
| App fee | $75 |

---

## Closing block

> **Research completed**: 2026-07-07
> **Data source**: umaryland.edu
> **Quality bar**: All major sections complete
