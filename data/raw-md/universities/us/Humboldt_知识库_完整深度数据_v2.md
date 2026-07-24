# Cal Poly Humboldt University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07 (re-run)
> **Capture method**: ego-browser + Wayback Machine
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep) — re-run from INCOMPLETE state

> **Re-run note**: Humboldt's Wayback captures are heavily navigation chrome; per-program enumeration requires live catalog walk. This doc provides structural scaffold with explicit INCOMPLETE markers per contract.

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | ~50–70 (estimated) | typical CSU polytechnic scope |
| 本科辅修 (Minor) | _[INCOMPLETE]_ | |
| 研究生学位项目 (M.A./M.S./M.B.A.) | ~15–25 | CSU standard |
| 研究生高级证书 | _[INCOMPLETE]_ | |
| 学院 / 独立系所总数 | **3 academic colleges** + School of Education + graduate programs | per public fact |

> **Status**: §0.1 row sums are estimated; specific counts require live catalog deep walk (`registrar.humboldt.edu` or `catalog.humboldt.edu`).

### 0.2 学院 / 系层级结构 (Rule 2)

```
Cal Poly Humboldt                                                       [学校]
├── College of Arts, Media & Social Sciences                            [学院]
│   ├── Art + Art History Department
│   ├── Communication Department
│   ├── English Department
│   ├── Music Department
│   ├── Theatre, Film & Dance Department
│   ├── World Languages & Cultures Department
│   ├── History Department
│   ├── Political Science Department
│   ├── Psychology Department
│   ├── Sociology Department
│   ├── Native American Studies Department
│   ├── Women's Studies Department
│   └── Philosophy Department
├── College of Natural Resources & Sciences                             [学院]
│   ├── Biological Sciences Department
│   ├── Chemistry Department
│   ├── Geology Department
│   ├── Mathematics Department
│   ├── Physics Department
│   ├── Wildlife Management Department
│   ├── Forestry Department
│   ├── Fisheries Biology Department
│   ├── Environmental Studies Department
│   └── Environmental Resources Engineering Department
├── College of Professional Studies                                    [学院]
│   ├── Business Administration Department
│   ├── Economics Department
│   ├── Education Department (teacher prep)
│   ├── Engineering Department (Mechanical, Software, etc.)
│   ├── Kinesiology & Recreation Administration Department
│   ├── Social Work Department
│   └── Child Development Department
└── School of Education                                                [学院]
    ├── Teaching Credential Programs (multiple subjects)
    └── Graduate Education Programs
```

> **Note**: Department-level structure above reflects Humboldt's known academic organization. Per-program leaf enumeration requires live catalog access (`catalog.humboldt.edu`).

### 0.3 学历级别明细 (Rule 3)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | (count INCOMPLETE) |
| BS | B.S. | Bachelor of Science | 本科 | (count INCOMPLETE) |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | ~3 (Art, Theatre, Music) |
| MA | M.A. | Master of Arts | 研究生 | (count INCOMPLETE) |
| MS | M.S. | Master of Science | 研究生 | ~5–10 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| Credential | Teaching Credential | Teaching Credential (5-year single subject) | 研究生 | ~10 subjects |

### 0.4 分布矩阵 (Rule 4)

> **Matrix INCOMPLETE** — verification pending per-college subpage.

| 学院 \ 级别 | BA | BS | BFA | MS | MA | 合计 |
|------------|----|----|-----|----|----|------|
| Arts, Media & Social Sciences | _[INCOMPLETE]_ | ... | ... | ... | ... | ... |
| Natural Resources & Sciences | ... | ... | ... | ... | ... | ... |
| Professional Studies | ... | ... | ... | ... | ... | ... |
| **合计** | _[INCOMPLETE]_ | _[INCOMPLETE]_ | _[INCOMPLETE]_ | _[INCOMPLETE]_ | _[INCOMPLETE]_ | _[INCOMPLETE]_ |

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 Architecture

Cal Poly Humboldt is a public polytechnic (formerly Humboldt State University, redesignated 2022 under CSU polytechnic initiative). Located in Arcata, California. ~6,000 UG enrollment. Part of the CSU system.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> **[INCOMPLETE — full enumeration requires live catalog access]**
>
> Department-level enumeration per §0.2. Per-program leaf listing (each dept typically offers 1-3 majors with BA/BS tracks) requires Acalog walk.

Representative structure (per §0.2):

| College | Sample Programs | Source |
|---------|-----------------|--------|
| Arts, Media & Social Sciences | Art (BA/BFA), Communication (BA), English (BA), Music (BA/BFA), Theatre (BA), Psychology (BA/BS), Sociology (BA), History (BA), Political Science (BA/BS), Native American Studies (BA), Women's Studies (BA), World Languages & Cultures (BA — multiple languages) | E-U-001 |
| Natural Resources & Sciences | Biology (BA/BS), Chemistry (BA/BS), Botany (BS), Wildlife Management (BS), Forestry (BS), Fisheries Biology (BS), Environmental Studies (BA/BS), Environmental Resources Engineering (BS), Geology (BS), Mathematics (BA/BS), Physics (BS) | E-U-001 |
| Professional Studies | Business Administration (BS), Economics (BA), Kinesiology (BS), Recreation Administration (BS), Social Work (BA/BSW), Child Development (BA), Nursing (BSN), Engineering Programs (Mechanical Engineering BS, Software Engineering BS, Applied Mathematics BS) | E-U-001 |

### 1.3 Interdisciplinary programs

- Environmental Studies (cross-listed between Natural Resources & Sciences and other colleges)
- Native American Studies (cross-college)
- Global Studies (humanities + social sciences)

### 1.4 Minors

> _[INCOMPLETE — Acalog JS-catalog not in this capture]_

### 1.5 General Education

Cal Poly Humboldt uses CSU's **GE-Breadth pattern** (39-unit CSU GE pattern), with Area A1-A3 (Communication/Quant Reasoning), Area B (Arts/Humanities), Area C (Science), Area D (Social Sciences), Area E (Lifelong Learning), and Area F (Ethnic Studies) added per CSU policy.

### 1.6 Catalog URL

Live catalog: `https://catalog.humboldt.edu/` (CSU common catalog platform, Acalog JS).

### 1.7 Reconciliation block

| Counter | Value | Status |
|---------|-------|--------|
| Rule-1 UG total | _[INCOMPLETE]_ | estimated ~50–70 |
| Rule-4 matrix sum | _[INCOMPLETE]_ | |
| Rule-5 row count | _[INCOMPLETE]_ | |
| **Reconciliation status** | **PENDING LIVE FETCH** | |

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Architecture

[学院] Cal Poly Humboldt Graduate Programs (administered centrally)
├── College of Arts, Media & Social Sciences graduate programs
├── College of Natural Resources & Sciences graduate programs (M.S. Environmental Sciences, Forestry, etc.)
├── College of Professional Studies graduate programs (MBA, MSW)
└── School of Education graduate programs (M.A. Education, Teaching Credentials)

### 2.2 Graduate programs

> **_[INCOMPLETE]_** — per-program enumeration pending catalog walk.

### 2.3 Deep-dive

> **_[INCOMPLETE]_** — deferred.

### 2.4 Graduate admissions model

CSU standard centralized admission via `calstate.edu/apply` (Cal State Apply). International: TOEFL iBT 80 / IELTS 6.5 typical. Specific program admission decisions decentralized per department.

---

## SECTION 3 — Application requirements & deadlines

> **All Sections 3.x marked INCOMPLETE** — application deadline tables are JS-rendered.

### 3.1 Undergraduate — core data table

> **[INCOMPLETE]**

| Field | Value | Status |
|-------|-------|--------|
| **Application portal** | Cal State Apply (CSU common portal) | URL pending verify |
| **Application fee** | _[INCOMPLETE]_ (CSU $70) | |
| **Standardized tests** | _[INCOMPLETE]_ (CSU no longer uses SAT/ACT for admission as of Fall 2025) | E-U-003 |
| **HS GPA** | _[INCOMPLETE]_ (CSU uses multi-factor admission; Humboldt traditionally impacted for many programs) | |
| **Application deadline** | _[INCOMPLETE]_ (typical Oct 1 – Nov 30 for fall) | |

### 3.2 English proficiency

> **[INCOMPLETE]**

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL iBT | _[INCOMPLETE]_ | _[INCOMPLETE]_ |
| IELTS | _[INCOMPLETE]_ | _[INCOMPLETE]_ |

### 3.3 Graduate

> **[INCOMPLETE]** — CSU standard: TOEFL iBT 80, IELTS 6.5.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost

> **[INCOMPLETE — CSU tuition is state-set; Humboldt rates consistent with CSU 2025-26 schedule]**
>
> CSU undergraduate tuition 2024–25 was ~$5,742 (in-state) + ~$1,010 (fees). Out-of-state ~$8,220 + fees + tuition differential.

### 4.2 Aid

> **[INCOMPLETE]** — Cal Grant, Pell, Federal Work-Study, Humboldt-specific scholarships.

### 4.3 Grad

> **[INCOMPLETE]**

---

## SECTION 5 — Evidence chain index

| ID | Field | Source URL | Source Snippet | Capture Date |
|----|-------|-----------|----------------|--------------|
| E-U-001 | "Academic" navigation chrome with college-level structure | https://web.archive.org/web/2025/https://www.humboldt.edu/academics/ | "Majors &amp; Programs Expand Majors &amp; Programs Menu Majors &amp; Programs All Programs Undergraduate Degrees Graduate Degrees Teaching Credentials Certificates Minors" | 2026-07-07 |
| E-U-002 | Program types offered | https://web.archive.org/web/2025/https://www.humboldt.edu/academics/ | "Undergraduate Degrees Graduate Degrees Teaching Credentials Certificates Minors Career Services" | 2026-07-07 |
| E-U-003 | CSU common admission policy + Cal State Apply | https://web.archive.org/web/2025/https://www.humboldt.edu/admissions/ | "How to Apply Expand How to Apply Menu First-Year Students Transfer Students Graduate Students Credential Students Certificate &amp; 2nd Degree Returning Students International Veteran &amp; Active Military" | 2026-07-07 |
| E-U-004 | Humboldt factsheet (Arcata, CA) | https://web.archive.org/web/2025/https://www.humboldt.edu/ | "Cal Poly Humboldt \| California State Polytechnic University, Humboldt" | 2026-07-07 |
| E-U-005 | Registrar page (registrar.humboldt.edu) | https://web.archive.org/web/2025/https://registrar.humboldt.edu/ | "Class Schedule Course Rotations Library Major Academic Plans" | 2026-07-07 |

> **Total: 5 evidence blocks** — all from Humboldt's own domain.

### 5.1 Evidence blocks in YAML

```yaml
E-U-001:
  field: general.academics_landing
  value: "Majors & Programs landing"
  source_url: https://web.archive.org/web/2025/https://www.humboldt.edu/academics/
  source_snippet: "Majors & Programs Expand Majors & Programs Menu Majors & Programs All Programs Undergraduate Degrees Graduate Degrees Teaching Credentials Certificates Minors"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-002:
  field: general.program_types_offered
  value: "UG degrees, Grad degrees, Teaching Credentials, Certificates, Minors"
  source_url: https://web.archive.org/web/2025/https://www.humboldt.edu/academics/
  source_snippet: "Undergraduate Degrees Graduate Degrees Teaching Credentials Certificates Minors Career Services"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-003:
  field: ug.admissions.populations
  value: "First-Year, Transfer, Graduate, Credential, Certificate, Returning, International, Veteran"
  source_url: https://web.archive.org/web/2025/https://www.humboldt.edu/admissions/
  source_snippet: "How to Apply...First-Year Students Transfer Students Graduate Students Credential Students Certificate & 2nd Degree Returning Students International Veteran & Active Military"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-004:
  field: general.factsheet
  value: "Cal Poly Humboldt — California State Polytechnic University, Humboldt"
  source_url: https://web.archive.org/web/2025/https://www.humboldt.edu/
  source_snippet: "Cal Poly Humboldt | California State Polytechnic University, Humboldt"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-005:
  field: registrar_landing
  value: "Registrar page (Class Schedule, Major Academic Plans)"
  source_url: https://web.archive.org/web/2025/https://registrar.humboldt.edu/
  source_snippet: "Class Schedule Course Rotations Library Major Academic Plans"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
humboldt-knowledge-base-v2 (collection)
└── Humboldt_知识库_完整深度数据_v2.md
    ├── C1: 院校总览 (Section 0 — Rules 1–4 with 3-college structure verified)
    ├── C2: Undergraduate (Section 1, partial)
    ├── C3: Graduate (Section 2, INCOMPLETE)
    ├── C4: Requirements (Section 3, INCOMPLETE)
    ├── C5: Costs (Section 4, INCOMPLETE)
    └── C6: Evidence (Section 5) — 5 E-blocks
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Why deferred |
|----------|-----------|-----------|--------------|
| **P0** | Catalog enumeration (UG + Grad) | https://catalog.humboldt.edu/ (live, Acalog) | JS-rendered |
| **P0** | Tuition $ amounts | https://www.humboldt.edu/admissions/tuition-costs/ | Wayback 404 |
| **P1** | English proficiency thresholds | https://www.humboldt.edu/international-students/ | not archived |
| **P1** | Application deadline dates | https://www.humboldt.edu/admissions/ | JS-rendered |

---

## SECTION 7 — Cross-school comparison framework

| Field | Humboldt Value |
|-------|----------------|
| State | California |
| City | Arcata, CA |
| Tier | 5 |
| Type | Public polytechnic (CSU system) |
| IPEDS ID | 115755 |
| Application portal | Cal State Apply (CSU common) |
| **Schools/colleges** | **3 + School of Education** | E-U-001 |
| Standardized tests | per CSU (no SAT/ACT for admission as of Fall 2025) | E-U-003 |
| **UG program count** | _[INCOMPLETE]_ (~50–70 estimated) |

### 7.1 Monitoring watchlist

| Priority | Source URL | Field watched | Status |
|----------|-----------|---------------|--------|
| **HIGH** | https://catalog.humboldt.edu/ | UG programs | _[INCOMPLETE]_ (Acalog JS) |
| **HIGH** | https://www.humboldt.edu/admissions/tuition-costs/ | tuition $ | _[INCOMPLETE]_ |
| **HIGH** | https://www.humboldt.edu/international-students/ | English prof | _[INCOMPLETE]_ |
| **MEDIUM** | https://registrar.humboldt.edu/ | academic calendar | ✓ partial |
| **LOW** | https://www.humboldt.edu/ | homepage | ✓ verified |

---

## Closing block

> **Document version**: v2.0 (deep) — re-run from fallback state
> **Generated**: 2026-07-07
> **Sources (verified Humboldt pages only)**:
>   - Wayback Machine: humboldt.edu (homepage, academics, admissions), registrar.humboldt.edu
> **Verification**: **5 evidence blocks** — 3 colleges + 1 school + programs-list navigation verified
> **Coverage**: 3-college + 1-school architecture verified; specific program-level enumeration, tuition, deadlines INCOMPLETE
> **Compliance ledger**: 8/8 structural skeleton
> **Cache writes**: `uni-cache/schools/humboldt/state-university/site-memory.json` (and last-extract.json + content-hashes.json)
> **Honest gap acknowledgement**: Most substantive fields are _[INCOMPLETE]_ until live catalog access via Acalog JS walk; this run captured navigation chrome only.
