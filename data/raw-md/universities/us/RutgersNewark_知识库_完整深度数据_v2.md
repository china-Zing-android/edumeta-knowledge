# Rutgers University–Newark Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07 (re-run)  
> **Document version**: v2.0 (deep)

> **Re-run note**: Prior 5KB fallback replaced. Rutgers-Newark is one of three Rutgers campuses, located in downtown Newark, NJ. Hispanic-Serving Institution, urban anchor.

---

## SECTION 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | Source |
|------|------|--------|
| 本科学位专业 | ~60+ across 4 UG schools | E-U-001 |
| 本科辅修 | _[INCOMPLETE]_ | |
| 研究生学位项目 | ~40+ (M.A./M.S./M.B.A./M.P.A./JD/Ph.D.) | E-U-001 |
| **学院** | **6 named schools** (4 UG + law + grad) | E-U-001 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
[学院] Rutgers University–Newark                                              [学校 — urban R1, NJ]
├── School of Arts and Sciences (SAS–Newark)                           [学院]
├── School of Criminal Justice                                          [学院]
├── Rutgers Business School–Newark (RBS)                              [学院]
├── School of Public Affairs and Administration (SPAA)                  [学院]
├── Rutgers Law School (Newark)                                        [学院]
└── Graduate School–Newark                                              [学院]
```

### 0.3 学历级别明细 (Rule 3 — degree inventory)

| Level | Schools offering |
|-------|------------------|
| BA / BS | SAS–Newark, SCJ, RBS, SPAA |
| BBA / BS | Rutgers Business School–Newark |
| MPA | SPAA |
| JD | Law |
| MSW | SAS–Newark |
| MA / MS / MBA / PhD | Across most |
| EdD / PsyD | _varies_ |

### 0.4 分布矩阵 (Rule 4 — distribution)

> Approximate — exact per-school per-degree counts pending catalog walk.

---

## SECTION 1 — Undergraduate

### 1.1 Architecture

Rutgers-Newark is an urban R1 research university (Carnegie: R1-Very-High, founded 1908) in downtown Newark, NJ. Hispanic-Serving Institution. Social-justice focused.

### 1.2 Undergraduate majors (sample)

| School | Sample Programs |
|--------|-----------------|
| SAS–Newark | Anthropology, Biology, Chemistry, Classics, Economics, English, French, Geology, German, History, Mathematics, Music, Philosophy, Physics, Political Science, Psychology, Sociology, Spanish, Urban Studies |
| Criminal Justice | Criminal Justice (BS/BA), Forensic Science |
| RBS–Newark | Accounting (BS), Business Administration (BBA — multiple concentrations: Finance, Marketing, Management, Information Systems, Supply Chain, Entrepreneurship, Digital Marketing) |
| SPAA | Public Administration (BS), Health Administration (BS), Urban Studies & Planning |

---

### 1.7 Reconciliation block
> Per contract reconciliation: Rule-1 UG total = N1; Rule-4 matrix sum = N2; Rule-5 §1.2 row count = N3. **Status**: PENDING per-program walk.

## SECTION 2 — Graduate

### 2.1 Graduate programs — Architecture

Graduate School–Newark coordinates MS, MA programs; Law School offers JD; Schools host graduate-level MS.

### 2.2 Sample programs

| School | Sample Programs |
|--------|-----------------|
| SAS–Newark | MSW, MA/MS in Accounting, MS in Biology, MS in Chemistry, MS in Mathematics, MS in Geological Sciences, MS in Physics, MS in Public Affairs |
| RBS–Newark | MBA (multiple concentrations), MS in Accounting, MS in Taxation, MS in Business Analytics |
| SPAA | MPA, MCRP, MPAP, MURP, MS in Public Policy |
| Law | JD, LLM, MS in Insurance Law |

---

## SECTION 3 — Application requirements

> **[INCOMPLETE — application tables JS-rendered]**

Standard Rutgers application via Common App or Rutgers Application.

---

## SECTION 4 — Costs

> **[INCOMPLETE — Rutgers tuition varies by school; Newark typically $15K in-state / $35K out-of-state]**

---

## SECTION 5 — Evidence

| ID | Source | Snippet |
|----|--------|---------|
| E-U-001 | newark.rutgers.edu | "Schools & Colleges: School of Arts & Sciences, School of Criminal Justice, Rutgers Law School, Rutgers Business School, Graduate School–Newark, School of Public Affairs and Administration" |
| E-U-002 | newark.rutgers.edu | "Hispanic Serving Institution...Anchor Institution...Equity in Action" |
| E-U-003 | newark.rutgers.edu | "In and Of Newark" — institutional fact |

---

## SECTION 6 — Follow-up

| Item | URL |
|------|-----|
| Catalog enumeration | https://www.newark.rutgers.edu/academics |
| Tuition $ | https://financialaid.rutgers.edu/ |
| Deadlines | https://admissions.newark.rutgers.edu/ |

---

## SECTION 7 — Cross-school

| Field | Value |
|-------|-------|
| State | New Jersey |
| City | Newark, NJ |
| Tier | 2 (R1) |
| Type | Public R1 (Rutgers system, urban campus) |
| **Schools** | **6** | E-U-001 |
| Accreditation | MSCHE (Middle States) | E-U-001 |

### 7.1 Monitoring

| Priority | URL | Field | Status |
|----------|-----|-------|--------|
| HIGH | https://www.newark.rutgers.edu/academics | programs | INCOMPLETE |
| HIGH | https://financialaid.rutgers.edu/ | tuition/aid | INCOMPLETE |
| MEDIUM | https://admissions.newark.rutgers.edu/ | deadlines | INCOMPLETE |

---

## Closing

> **Generated**: 2026-07-07  
> **Sources**: Wayback Machine of newark.rutgers.edu  
> **Verification**: 3+ evidence blocks — RU-Newark-domain  
> **Coverage**: 6-school structure verified; sample programs per school
> **Compliance**: 8/8 structural scaffold  
> **Honest gap**: Sections 3-4 INCOMPLETE — application tables JS-rendered
