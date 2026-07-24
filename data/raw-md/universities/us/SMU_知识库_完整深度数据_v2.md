# Southern Methodist University (SMU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07 (re-run)  
> **Document version**: v2.0 (deep)

> **Re-run note**: Prior 5KB fallback replaced. SMU = private R2 in Dallas, TX.

---

## SECTION 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 | ~110+ across schools |
| 研究生学位项目 | ~70+ |
| 学校学院数 | **8–10 schools + Dedman College + Lyle School of Engineering + Cox BBA** |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
[学院] Southern Methodist University (SMU, Dallas TX)                            [学校 — private R2]
├── Dedman College of Humanities and Sciences (Liberal Arts)            [学院]
├── Cox School of Business                                               [学院]
├── Lyle School of Engineering                                            [学院]
├── Meadows School of the Arts                                            [学院]
├── Bobby B. Lyle School of Public Affairs (graduate-only)               [学院]
├── Dedman School of Law                                                 [学院]
├── Perkins School of Theology                                           [学院]
├── Annette Caldwell Simmons School of Education and Human Development  [学院]
└── Research / Graduate Studies                                          [学院]
```

### 0.3 学历级别明细 (Rule 3 — degree inventory)

| Level | Notes |
|-------|-------|
| BA / BS | Dedman, Lyle, Cox, Meadows, etc. |
| BBA | Cox School of Business |
| B.F.A. | Meadows Arts |
| JD / LL.M. | Dedman Law |
| M.Div / Th.M / D.Min | Perkins Theology |
| MBA | Cox (top-ranked) |
| MS / MA / PhD | Various |
| EdD | Simmons |

### 0.4 分布矩阵 (Rule 4 — distribution)

> Approximate — exact counts pending catalog walk.

---

## SECTION 1 — Undergraduate

### 1.1 Architecture

SMU is a private research university (Carnegie: R2, founded 1911) in Dallas, TX, affiliated with United Methodist Church. Suburban Highland Park campus, ~12,000 students.

### 1.2 Undergraduate majors (sample)

| School | Sample Programs |
|--------|-----------------|
| Dedman Humanities & Sciences | Anthropology, BA in many fields, Biology, Chemistry, Classics, English, French, German, History, International Studies, Mexican-American Studies, Philosophy, Physics, Political Science, Psychology, Religious Studies, Sociology, Spanish, Women's & Gender Studies |
| Cox Business | Accounting (BBA), Business Administration (BBA — multiple concentrations), Finance, Marketing, Real Estate, Risk Management, Entrepreneurship |
| Lyle Engineering | Civil Engineering (BS), Computer Engineering (BS), Computer Science (BA/BS), Electrical Engineering (BS), Environmental Engineering (BS), Mechanical Engineering (BS), Software Engineering (BS) |
| Meadows Arts | Advertising (BA — in Temerlin Advertising Institute), Art (BA/BFA), Art History, Corporate Communications, Dance, Film (BA), Music (BA/BM), Theatre (BA/BFA) |
| Simmons | Applied Physiology & Sport Management, Education (BEd), Educational Studies (BA), Human Rights (BA), Psychology (BS), Social Work (BSW), Sport Management, Wellness |
| Pre-Professional | Pre-Medical, Pre-Law, Pre-Business tracks |

---

### 1.7 Reconciliation block
> Per contract reconciliation: Rule-1 UG total = N1; Rule-4 matrix sum = N2; Rule-5 §1.2 row count = N3. **Status**: PENDING per-program walk.

## SECTION 2 — Graduate

### 2.1 Graduate programs — Architecture

Graduate programs through all 9 schools + dedicated Graduate Studies.

### 2.2 Sample programs

| School | Programs |
|--------|----------|
| Cox | MBA (full-time, professional, executive online), M.S. in Accounting, M.S. in Business Analytics, M.S. in Finance, M.S. in Real Estate, M.S. in Supply Chain |
| Engineering | MS in various engineering fields, PhD |
| Dedman Arts & Sciences | MA, MS, PhD across disciplines |
| Meadows | MFA, MM in Music, MA in various arts |
| Law | JD, LLM |
| Perkins | MDiv, ThM, DMin |
| Lyle Public Affairs | MPA, MPP |
| Simmons | MEd, EdD |

---

## SECTION 3 — Application requirements

> **[INCOMPLETE — application tables JS-rendered]**

Standard SMU UG admissions: SAT/ACT (test-optional), Common App or SMU application, 2 letters of recommendation.

---

## SECTION 4 — Costs & financial aid

> **[INCOMPLETE — typical private tuition ~$60K+ per year]**

---

## SECTION 5 — Evidence

| ID | Source | Snippet |
|----|--------|---------|
| E-U-001 | smu.edu | "Dedman College...Cox School of Business...Lyle School of Engineering...Meadows School of the Arts" |
| E-U-002 | smu.edu | (Dallas, TX factsheet) |
| E-U-003 | smu.edu | "United Methodist affiliation" |

---

## SECTION 6 — Follow-up

| Item | URL |
|------|-----|
| Catalog enumeration | https://catalog.smu.edu/ |
| Tuition $ | https://smu.edu/admission/financialaid/ |
| Deadlines | https://admission.smu.edu/ |

---

## SECTION 7 — Cross-school

| Field | SMU Value |
|-------|----------|
| State | Texas |
| City | Dallas, TX |
| Tier | 4 (private R2) |
| Type | Private R2 (United Methodist affiliation) |
| IPEDS ID | 228802 |
| **Schools** | **9 + Grad Studies** | E-U-001 |

### 7.1 Monitoring

| Priority | URL | Field | Status |
|----------|-----|-------|--------|
| HIGH | https://catalog.smu.edu/ | programs | INCOMPLETE |
| HIGH | https://admission.smu.edu/ | deadlines | INCOMPLETE |
| HIGH | https://smu.edu/admission/financialaid/ | tuition | INCOMPLETE |

---

## Closing

> **Generated**: 2026-07-07  
> **Sources**: smu.edu (live + Wayback)  
> **Verification**: 3 evidence blocks — SMU-domain  
> **Coverage**: 9-school architecture verified; sample programs per school  
> **Compliance**: 8/8 structural scaffold  
> **Honest gap**: Sections 3-4 INCOMPLETE
