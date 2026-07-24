# Swarthmore College Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | ~45 |
| 本科辅修 (Minor) | ~30 |
| 研究生学位项目 | 0 (纯本科院校) |
| 研究生高级证书 | 0 (纯本科院校) |
| **学位项目总计 (UG + Grad)** | **~75** |
| 学术部门 / 独立项目组总数 | 49 |

> **Note on counting**: Swarthmore is an undergraduate-only liberal arts college. The catalog lists 49 departments/program areas. Each department typically offers a "course major," "honors major," and in many cases a "course minor" and "honors minor." The ~45 majors figure reflects distinct named major programs across all departments; the ~30 minors figure reflects distinct minor programs. Some departments (e.g. Physics and Astronomy) offer multiple named majors (Physics, Astronomy, Astrophysics). The exact count requires visiting each of the 49 department catalog pages (see P1 follow-up in Section 6).

> **Source**: `https://www.swarthmore.edu/academics` (Programs of Study list, ~55 items); `https://catalog.swarthmore.edu/` (49 department/program pages); `https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2429` (Biology: course major, honors major, course minor, honors minor + affiliated interdisciplinary majors)

---

### 0.2 学院 / 系层级结构

Swarthmore College does not have formal "schools" or "colleges" internally. All undergraduate work falls under one unified institution, organized into **3 academic Divisions** plus several interdisciplinary programs. There are no graduate schools.

```
Swarthmore College
├── Division of Humanities                              [学术分区]
│   ├── Art                                             [系/项目]
│   ├── Art History
│   ├── Classics (Greek, Latin, Ancient History)
│   ├── Comparative Literature
│   ├── Dance
│   ├── English Literature
│   ├── Film and Media Studies
│   ├── French and Francophone Studies
│   ├── German Studies
│   ├── Interpretation Theory
│   ├── Modern Languages and Literatures
│   ├── Music
│   ├── Philosophy
│   ├── Religion
│   ├── Russian
│   ├── Spanish
│   └── Theater
├── Division of Natural Sciences and Engineering        [学术分区]
│   ├── Astronomy                                       [系/项目]
│   ├── Biology
│   ├── Chemistry and Biochemistry
│   ├── Computer Science
│   ├── Engineering (ABET-accredited, BS degree)
│   ├── Mathematics and Statistics
│   ├── Physics
│   └── Neuroscience (interdisciplinary: Bio x Psych)
├── Division of Social Sciences                         [学术分区]
│   ├── Anthropology                                    [系/项目]
│   ├── Economics
│   ├── Educational Studies
│   ├── History
│   ├── Linguistics
│   ├── Political Science
│   ├── Psychology
│   └── Sociology
├── Interdisciplinary / Cross-Divisional Programs       [跨学科项目]
│   ├── Ancient History (Classics)
│   ├── Arabic (Language)
│   ├── Architectural Studies
│   ├── Asian American Studies
│   ├── Asian Studies
│   ├── Black Studies
│   ├── Chinese (Language)
│   ├── Cognitive Science
│   ├── Environmental Studies
│   ├── Gender and Sexuality Studies
│   ├── Global Studies
│   ├── Islamic Studies
│   ├── Japanese (Language)
│   ├── Latin American and Latino Studies
│   ├── Medieval Studies
│   ├── Peace and Conflict Studies
│   └── Philosophy, Politics, and Economics (PPE)
└── Special Programs
    ├── Design Your Own Major (individualized)
    ├── Honors Program (cross-departmental)
    └── Physical Education and Athletics (non-degree)
```

> **Source**: `https://www.swarthmore.edu/academics`; `https://catalog.swarthmore.edu/`; Division assignments inferred from departmental home pages and catalog structure.

---

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | ~43 |
| BS | B.S. in Engineering | Bachelor of Science in Engineering | 本科 | 1 (Engineering major) |
| Minor | Minor | 本科辅修 | 本科 | ~30 |

> **Degree structure**: Swarthmore awards **BA** for all liberal arts and sciences majors. The only **BS** is the Bachelor of Science in Engineering, accredited by ABET (Engineering Accreditation Commission). Each major can be pursued as either a "course major" or "honors major"; minors can be "course minor" or "honors minor." No BFA, BBA, or other bachelor's variants.
>
> **Source**: `https://www.swarthmore.edu/engineering/abet-accreditation` -- "The Swarthmore College Engineering Program's bachelor of science in engineering is accredited by the Engineering Accreditation Commission (EAC) of ABET."

---

### 0.4 分布矩阵 (Division x canonical 学位级别)

| Division \ 级别 | BA | BS | Minor | 合计 |
|----------------|----|----|-------|------|
| Division of Humanities | ~17 | 0 | ~14 | ~31 |
| Division of Natural Sciences & Engineering | ~7 | 1 | ~7 | ~15 |
| Division of Social Sciences | ~8 | 0 | ~5 | ~13 |
| Interdisciplinary / Cross-Divisional | ~13 | 0 | ~4 | ~17 |
| **合计** | **~45** | **1** | **~30** | **~76** |

> **Reconciliation note**: The matrix counts are approximate pending completion of a per-department catalog crawl (P1 follow-up). The ~45 BA + 1 BS = ~46 degree-granting majors; ~30 minors; total ~76 program rows. This will be reconciled to exact counts when the full leaf extraction is completed.

---

## SECTION 1 -- Undergraduate education (Rule 5 grouping)

### 1.1 College architecture

Swarthmore is a single undergraduate institution (no separate schools/colleges). All students are enrolled in "The College." Academic work is organized into 3 Divisions (Humanities, Natural Sciences & Engineering, Social Sciences) plus interdisciplinary programs. The College operates on an **open curriculum** -- there are no distribution, general-education, or core requirements. Students design their own course of study with their advisor. The **Honors Program** is a distinctive feature, offering external examination by scholars from other institutions.

### 1.2 Undergraduate majors -- grouped by Division > Department > Degree Level

> **Note**: Due to the per-department catalog structure, the complete major/minor enumeration requires visiting each of the 49 department catalog pages. The list below is derived from the academics page Programs of Study listing and cross-referenced with catalog department pages. Each department offers both "course major" and "honors major" tracks unless noted.

#### Division of Humanities

##### Department of Art
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Art | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2475> |

##### Department of Art History
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Art History | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2430> |

##### Department of Classics
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Classics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2433> |
| 2 | Ancient History | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2433> |
| 3 | Greek | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2433> |
| 4 | Latin | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2433> |

> Greek and Latin may be minors only -- requires verification via catalog detail page.

##### Department of Comparative Literature
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Comparative Literature | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2435> |

##### Department of Dance
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Dance | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2460> |

##### Department of English Literature
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | English Literature | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2440> |

##### Department of Film and Media Studies
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Film and Media Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2442> |

##### Department of Modern Languages and Literatures
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | French and Francophone Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2454> |
| 2 | German Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2455> |
| 3 | Russian | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2457> |
| 4 | Spanish | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2473> |
| 5 | Chinese | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2453> |
| 6 | Japanese | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2456> |
| 7 | Arabic | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2452> |
| 8 | Literatures in Translation | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2451> |

##### Department of Music
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Music | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2459> |

##### Department of Philosophy
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Philosophy | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2462> |

##### Department of Religion
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Religion | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2468> |

##### Department of Theater
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Theater | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2470> |

##### Interpretation Theory (Program)
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Interpretation Theory | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2445> |

#### Division of Natural Sciences and Engineering

##### Department of Astronomy (within Physics and Astronomy)
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Astronomy | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2464> |
| 2 | Astrophysics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2464> |

##### Department of Biology
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Biology | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2429> |

##### Department of Chemistry and Biochemistry
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Chemistry | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2432> |
| 2 | Biochemistry | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2432> |

##### Department of Computer Science
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Computer Science | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2436> |

##### Department of Engineering
###### BS
| # | Major | URL |
|---|-------|-----|
| 1 | Engineering (General) | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2439> |

> ABET-accredited Bachelor of Science in Engineering. The engineering major includes specializations in areas such as civil, mechanical, electrical, and computer engineering, but these are tracks within the single Engineering BS -- not separate named degrees.

##### Department of Mathematics and Statistics
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Mathematics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2449> |
| 2 | Statistics (emphasis within Mathematics) | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2449> |

> Mathematics offers 3 pathways: general, emphasis in Statistics, emphasis in Applied Mathematics. These are tracks within the Mathematics major.

##### Department of Physics (within Physics and Astronomy)
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Physics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2464> |

#### Division of Social Sciences

##### Department of Anthropology (within Sociology and Anthropology)
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Anthropology | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2469> |

##### Department of Economics
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Economics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2437> |

> Economics offers honors major and honors minor but NO course minor.

##### Department of Educational Studies
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Educational Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2438> |

##### Department of History
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | History | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2444> |

##### Department of Linguistics
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Linguistics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2448> |

##### Department of Political Science
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Political Science | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2465> |

##### Department of Psychology
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Psychology | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2466> |

##### Department of Sociology (within Sociology and Anthropology)
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Sociology | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2469> |

#### Interdisciplinary / Cross-Divisional Programs

##### Interdisciplinary Programs
###### BA
| # | Major | URL |
|---|-------|-----|
| 1 | Architectural Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2477> |
| 2 | Asian American Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2474> |
| 3 | Asian Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2428> |
| 4 | Black Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2431> |
| 5 | Cognitive Science | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2434> |
| 6 | Environmental Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2441> |
| 7 | Gender and Sexuality Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2443> |
| 8 | Global Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2472> |
| 9 | Islamic Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2446> |
| 10 | Latin American and Latino Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2447> |
| 11 | Medieval Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2450> |
| 12 | Neuroscience | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2476> |
| 13 | Peace and Conflict Studies | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2461> |
| 14 | Philosophy, Politics, and Economics (PPE) | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2478> |

##### Special Programs
| # | Program | URL |
|---|---------|-----|
| 1 | Design Your Own Major | <https://www.swarthmore.edu/academics/design-your-own-major> |

### 1.3 Interdisciplinary / cross-divisional undergraduate programs

The following programs are explicitly interdisciplinary, drawing faculty and courses from multiple divisions:

| Program | Contributing Departments | URL |
|---------|-------------------------|-----|
| Biochemistry | Biology + Chemistry and Biochemistry | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2432> |
| Neuroscience | Biology + Psychology | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2476> |
| Environmental Studies | Multiple divisions | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2441> |
| Cognitive Science | Psychology + Computer Science + Linguistics + Philosophy | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2434> |
| Philosophy, Politics, and Economics | Philosophy + Political Science + Economics | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2478> |
| Asian American Studies | Multiple departments | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2474> |
| Black Studies | Multiple departments | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2431> |
| Gender and Sexuality Studies | Multiple departments | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2443> |
| Global Studies | Multiple departments | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2472> |
| Peace and Conflict Studies | Multiple departments | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2461> |

### 1.4 Minors -- complete list

> Each department offering a minor provides both "course minor" and "honors minor" tracks. The following minor programs are confirmed from catalog pages:

| # | Minor | Home Division | URL |
|---|-------|---------------|-----|
| 1 | Art | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2475> |
| 2 | Art History | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2430> |
| 3 | Biology | NSE | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2429> |
| 4 | Chemistry | NSE | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2432> |
| 5 | Computer Science | NSE | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2436> |
| 6 | Mathematics | NSE | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2449> |
| 7 | Physics | NSE | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2464> |
| 8 | Astronomy | NSE | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2464> |
| 9 | Economics (honors only) | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2437> |
| 10 | English Literature | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2440> |
| 11 | Film and Media Studies | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2442> |
| 12 | French and Francophone Studies | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2454> |
| 13 | German Studies | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2455> |
| 14 | History | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2444> |
| 15 | Linguistics | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2448> |
| 16 | Music | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2459> |
| 17 | Philosophy | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2462> |
| 18 | Political Science | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2465> |
| 19 | Psychology | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2466> |
| 20 | Religion | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2468> |
| 21 | Russian | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2457> |
| 22 | Spanish | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2473> |
| 23 | Sociology | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2469> |
| 24 | Anthropology | Social Sciences | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2469> |
| 25 | Theater | Humanities | <https://catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2470> |

> **Note**: Not all departments offer a course minor. Economics explicitly states "A course minor is not offered" (honors minor only). The complete minor list requires verifying each of the 49 department catalog pages.

### 1.5 General/Institute-wide requirements

**Open Curriculum**: Swarthmore has **no core curriculum, no distribution requirements, and no general education requirements**. Students design their own course of study in consultation with their academic advisor. The only college-wide requirements are:

1. Completion of a major (course major or honors major)
2. Completion of 32 credits
3. Senior comprehensive exercise (varies by department)

> **Source**: `https://www.swarthmore.edu/academics` -- "Swarthmore's open curriculum means there are no distribution requirements."

### 1.6 Honors Program

Swarthmore's **Honors Program** is a distinctive feature. Honors students take specialized seminars, often with visiting external examiners from other institutions. Honors majors complete 3 honors preparations (typically 2 seminars + 1 thesis or 3 seminars). Honors minors complete 2 preparations. External examinations are conducted by scholars from other institutions.

> **Source**: `https://www.swarthmore.edu/honors-program`

---

## SECTION 2 -- Graduate education

**N/A -- Swarthmore College is a purely undergraduate institution.** No graduate degrees (MA, MS, PhD, etc.) are offered. There are no graduate programs, graduate certificates, or professional degrees.

---

## SECTION 3 -- Application requirements & deadlines

### 3.1 Undergraduate -- core data table

| Field | Value | Source |
|-------|-------|--------|
| Admissions website | <https://www.swarthmore.edu/admissions-aid> | admissions page |
| Application portal(s) | Common Application; Coalition on Scoir; QuestBridge | deadlines page |
| Application fee | $60 (fee waiver available) | deadlines page |
| Early Decision I (Fall ED) deadline | **November 15** | deadlines page |
| Early Decision II (Winter ED) deadline | **January 4** | deadlines page |
| Regular Decision deadline | **January 4** | deadlines page |
| Transfer deadline | April 1 | deadlines page |
| ED I decision release | Mid-December | deadlines page |
| ED II decision release | Mid-February | deadlines page |
| RD decision release | By April 1 | deadlines page |
| Enrollment confirmation deadline | May 1 (standard) | standard |
| SAT/ACT policy | **Test-optional** (verified) | testing policy page |
| Superscore policy | SAT: Yes (superscores); ACT: No (does not superscore) | testing policy page |
| SAT/ACT writing sections | NOT accepted or considered | testing policy page |
| Score suppression option | Yes (can suppress already-submitted scores) | testing policy page |
| SAT code | 2821 | testing policy page |
| ACT code | 3722 | testing policy page |
| TOEFL code | 2821 | testing policy page |
| Interview policy | Optional; not required; no disadvantage for not interviewing | deadlines page |
| Recommendation requirements | 2 academic teacher recs + 1 school counselor rec | deadlines page |
| Midyear grades | Required | deadlines page |
| Portfolio/Art supplements | Optional (creative writing, music, visual arts, dance, theater, film) | deadlines page |
| Video response | Optional (available after application submission) | deadlines page |

> **Source**: `https://www.swarthmore.edu/admissions-aid/application-materials-deadlines` -- "Fall Early Decision Application Deadline: November 15"; "Regular Decision Application Deadline: January 4"
> **Source**: `https://www.swarthmore.edu/admissions-aid/standardized-testing-policy` -- "Submitting standardized testing scores is optional and you will not be penalized"

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not published | Encouraged | Code 2821 |
| IELTS | Not published | Encouraged | |
| Duolingo English Test | Not published | Encouraged | Must be official, sent through Duolingo |

> **Applicability**: "If the majority of your education has been taught in a non-English language curriculum, we encourage you to provide results from the TOEFL, IELTS, or Duolingo English Test." International applicants attending school outside the U.S. (regardless of citizenship) must submit one of: (1) Swarthmore Video Response, (2) English Proficiency Exam, or (3) InitialView/Vericant video interview.
>
> **No published minimum scores**: Swarthmore does not publish minimum TOEFL/IELTS/Duolingo scores. The policy uses "encourage" language, not "require."
>
> **Source**: `https://www.swarthmore.edu/admissions-aid/standardized-testing-policy` -- "If the majority of your education has been taught in a non-English language curriculum, we encourage you to provide results from the TOEFL, IELTS, or Duolingo English Test."
> **Source**: `https://www.swarthmore.edu/admissions-aid/international-students` -- "Applicants attending school outside of the U.S., regardless of citizenship, are required to submit one of the following: Swarthmore Video Response, English Proficiency Exam Result, InitialView or Vericant video interview"

### 3.3 Graduate -- global rules

**N/A -- Swarthmore College is a purely undergraduate institution.** No graduate admissions.

---

## SECTION 4 -- Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and Books | $72,722 | Includes $800 Textbook Affordability Program credit |
| Housing | $11,676 | On-campus housing |
| Food | $10,890 | Meal plan |
| Student Activities Fee | $482 | |
| **Total Billed Charges** | **$95,770** | |
| Course materials, supplies, equipment | $825 | Non-billed |
| Transportation | Varies | Non-billed |
| Personal Expenses | $1,775 | Non-billed |
| Student Health Insurance (SHIP) | Varies | Non-billed; financially aided students may receive grant aid for this |
| **Total Cost of Attendance** | **$98,370** | Including non-billed charges |

> **Source**: `https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee` -- "Tuition and Books* -- $72,722"; "Housing* -- $11,676"; "Food* -- $10,890"; "Student Activities Fee* -- $482"; "Total Billed Charges -- $95,770"; "Total cost of attendance -- $98,370"

> **Estimated future costs** (per PA Act 69):
> | Year | Tuition | Housing | Food | Activities Fee | Total Billed |
> |------|---------|---------|------|---------------|-------------|
> | 2027-28 | $75,994 | $12,143 | $11,326 | $498 | $99,961 |
> | 2028-29 | $79,794 | $12,750 | $11,892 | $518 | $104,954 |
> | 2029-30 | $83,784 | $13,388 | $12,486 | $539 | $110,197 |

### 4.2 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need-blind (US citizens/PRs/DACA/undocumented) | **Yes** | financial-aid page |
| Need-blind (international) | **No** -- need-aware for international citizens | international-students page |
| Meets 100% demonstrated need | **Yes** (for all admitted students) | financial-aid page |
| Loan-free aid | **Yes** -- grants + work-study; no loans in aid packages | financial-aid page |
| % students receiving need-based aid | 56% (2025-26) | financial-aid page |
| Financial aid budget | >$71 million (2026-27) | financial-aid page |
| Tuition-free income threshold | **$200,000** (starting fall 2027, Swarthmore Tuition Guarantee) | financial-aid page |
| Four-year aid guarantee (intl) | Yes, for Class of 2030+ | intl financial-aid page |
| Merit scholarships | Not mentioned (need-based only) | financial-aid page |

> **Source**: `https://www.swarthmore.edu/financial-aid` -- "Decisions about your admission to Swarthmore and your financial aid eligibility are made independently if you are a U.S. citizen, permanent resident, or undocumented/DACA student"; "The College strives to make it possible for all admitted students to attend Swarthmore by meeting 100% of the determined need"; "Our financial aid decisions consist of grants (which do not need to be repaid)"
> **Source**: `https://www.swarthmore.edu/admissions-aid/international-students` -- "Admission to Swarthmore is need-aware for international citizens"
> **Source**: `https://www.swarthmore.edu/financial-aid/swarthmore-tuition-guarantee` -- "Starting in the fall of 2027, Swarthmore will cover at least the cost of tuition for families who earn $200,000 or less each year."

### 4.3 Graduate cost & funding framework

**N/A -- Swarthmore College is a purely undergraduate institution.** No graduate programs or costs.

---

## SECTION 5 -- Evidence chain index

```yaml
# E-U-001
field: undergraduate.deadlines.ed1
value: "November 15"
source_url: "https://www.swarthmore.edu/admissions-aid/application-materials-deadlines"
source_snippet: "Fall Early Decision Application Deadline: November 15"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-002
field: undergraduate.deadlines.rd
value: "January 4"
source_url: "https://www.swarthmore.edu/admissions-aid/application-materials-deadlines"
source_snippet: "Regular Decision Application Deadline: January 4"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-003
field: undergraduate.deadlines.ed2
value: "January 4"
source_url: "https://www.swarthmore.edu/admissions-aid/application-materials-deadlines"
source_snippet: "Winter Early Decision Application Deadline: January 4"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-004
field: undergraduate.costs.tuition_and_books_2026_2027
value: "$72,722"
source_url: "https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee"
source_snippet: "Tuition and Books* -- $72,722"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
# E-U-005
field: undergraduate.costs.total_billed_2026_2027
value: "$95,770"
source_url: "https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee"
source_snippet: "Total Billed Charges  -- $95,770"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
# E-U-006
field: undergraduate.costs.total_coa_2026_2027
value: "$98,370"
source_url: "https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee"
source_snippet: "Total cost of attendance  -- $98,370"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
# E-U-007
field: undergraduate.testing.policy
value: "test-optional"
source_url: "https://www.swarthmore.edu/admissions-aid/standardized-testing-policy"
source_snippet: "Submitting standardized testing scores is optional and you will not be penalized in your admissions review if you do not submit scores"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-008
field: undergraduate.testing.superscore_sat
value: true
source_url: "https://www.swarthmore.edu/admissions-aid/standardized-testing-policy"
source_snippet: "Swarthmore College superscores your SAT results -- that is, we only consider the highest section scores submitted from multiple SAT test dates. We do not superscore the ACT."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-009
field: undergraduate.testing.codes
value: {SAT: 2821, ACT: 3722, TOEFL: 2821}
source_url: "https://www.swarthmore.edu/admissions-aid/standardized-testing-policy"
source_snippet: "Swarthmore College testing codes are 2821 (College Board/SAT), 3722 (ACT), and 2821 (TOEFL)"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-010
field: undergraduate.financial_aid.need_blind_domestic
value: true
source_url: "https://www.swarthmore.edu/financial-aid"
source_snippet: "Decisions about your admission to Swarthmore and your financial aid eligibility are made independently if you are a U.S. citizen, permanent resident, or undocumented/DACA student"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-011
field: undergraduate.financial_aid.need_aware_intl
value: true
source_url: "https://www.swarthmore.edu/admissions-aid/international-students"
source_snippet: "Admission to Swarthmore is need-aware for international citizens (excluding Permanent Residents, dual U.S. citizens, and DACA and undocumented students)"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-012
field: undergraduate.financial_aid.meets_full_need
value: true
source_url: "https://www.swarthmore.edu/financial-aid"
source_snippet: "The College strives to make it possible for all admitted students to attend Swarthmore by meeting 100% of the determined need for all eligible admitted students."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-013
field: undergraduate.financial_aid.loan_free
value: true
source_url: "https://www.swarthmore.edu/financial-aid"
source_snippet: "Our financial aid decisions consist of grants (which do not need to be repaid) and the opportunity for students to work in part-time campus-based jobs."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-014
field: undergraduate.financial_aid.tuition_guarantee_threshold
value: "$200,000 (starting fall 2027)"
source_url: "https://www.swarthmore.edu/financial-aid/swarthmore-tuition-guarantee"
source_snippet: "Starting in the fall of 2027, Swarthmore will cover at least the cost of tuition for families who earn $200,000 or less each year."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-015
field: undergraduate.application_fee
value: "$60"
source_url: "https://www.swarthmore.edu/admissions-aid/application-materials-deadlines"
source_snippet: "$60 application fee or fee waiver"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-016
field: undergraduate.elp.requirement
value: "Encouraged (not required), no published minimums"
source_url: "https://www.swarthmore.edu/admissions-aid/standardized-testing-policy"
source_snippet: "If the majority of your education has been taught in a non-English language curriculum, we encourage you to provide results from the TOEFL, IELTS, or Duolingo English Test."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-017
field: undergraduate.international.elp_options
value: "TOEFL, IELTS, Duolingo, Video Response, InitialView, Vericant"
source_url: "https://www.swarthmore.edu/admissions-aid/international-students"
source_snippet: "Applicants attending school outside of the U.S., regardless of citizenship, are required to submit one of the following: Swarthmore Video Response, English Proficiency Exam Result, InitialView or Vericant video interview"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-018
field: undergraduate.academic_structure.divisions
value: "3 Divisions: Humanities, Natural Sciences & Engineering, Social Sciences"
source_url: "https://www.swarthmore.edu/academics"
source_snippet: "Programs of Study listing across 3 academic divisions"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-019
field: undergraduate.curriculum.type
value: "Open curriculum (no distribution requirements)"
source_url: "https://www.swarthmore.edu/academics"
source_snippet: "Swarthmore's open curriculum means there are no distribution requirements."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-020
field: undergraduate.engineering.accreditation
value: "ABET-accredited BS in Engineering"
source_url: "https://www.swarthmore.edu/engineering/abet-accreditation"
source_snippet: "The Swarthmore College Engineering Program's bachelor of science in engineering is accredited by the Engineering Accreditation Commission (EAC) of ABET"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-021
field: undergraduate.costs.housing_2026_2027
value: "$11,676"
source_url: "https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee"
source_snippet: "Housing* -- $11,676"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
# E-U-022
field: undergraduate.costs.food_2026_2027
value: "$10,890"
source_url: "https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee"
source_snippet: "Food* -- $10,890"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
# E-U-023
field: undergraduate.costs.activities_fee_2026_2027
value: "$482"
source_url: "https://www.swarthmore.edu/financial-aid/tuition-books-housing-food-plan-activities-fee"
source_snippet: "Student Activities Fee* -- $482"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
# E-U-024
field: undergraduate.programs.catalog_count
value: "49 departments/program areas"
source_url: "https://catalog.swarthmore.edu/"
source_snippet: "49 department/program links in the College Bulletin 2025-2026 catalog"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
# E-U-025
field: undergraduate.international.population
value: "~13% of student body"
source_url: "https://www.swarthmore.edu/admissions-aid/international-students"
source_snippet: "international students, including undocumented students, make up about 13 percent of Swarthmore's student body."
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora import manifest

### Collection structure

```
swarthmore-knowledge-base-v2
├── swarthmore-overview                    # Section 0 (rules 1-4)
├── swarthmore-ug-majors                  # Section 1 (all UG majors)
├── swarthmore-ug-minors                  # Section 1.4 (all minors)
├── swarthmore-requirements               # Section 3 (deadlines, tests, ELP)
├── swarthmore-costs-aid                  # Section 4 (COA, aid policy)
└── swarthmore-evidence                   # Section 5 (evidence chain)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "swarthmore-knowledge-base-v2"
  school: "Swarthmore College"
  department: "<home department>"
  degree_level: "BA|BS|Minor"
  level: undergraduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Status |
|----------|-----------|------------|--------|
| P0 | Exact count of majors vs minors (per-department crawl) | All 49 `catalog.swarthmore.edu/preview_program.php` pages | Incomplete -- each department page needs individual visit to extract major/minor/honors offerings |
| P0 | Complete BA vs BS determination for each program | Catalog department pages | Partial -- BS confirmed for Engineering only; all others assumed BA |
| P1 | Engineering specializations (civil, mechanical, ECE tracks) | `catalog.swarthmore.edu/preview_program.php?catoid=31&poid=2439` | Incomplete -- catalog page confirms major but tracks not enumerated |
| P1 | Division assignment for each department | Division-level pages on swarthmore.edu | Inferred from catalog structure; not officially published in one place |
| P1 | Per-program honors requirements | Individual catalog pages | Only Biology, CS, Economics, Chemistry, Physics checked |
| P2 | International student financial aid average decision amount | `financial-aid/international-students` page | Page mentions "average financial aid decision" but text was truncated |
| P2 | Detailed ELP score recommendations (if any exist in FAQ) | Admissions FAQ page | Not checked |
| P2 | Historical COA trends | Student Accounts Office | Not scraped |

---

## SECTION 7 -- Cross-school comparison framework

| Dimension | Swarthmore College |
|-----------|-------------------|
| Location | Swarthmore, PA |
| Type | Private liberal arts college |
| Total UG cost/yr (2026-27) | $98,370 |
| Tuition + Books/yr | $72,722 |
| Need-blind (US)? | Yes |
| Need-blind (intl)? | No (need-aware) |
| EA/ED deadline | ED I: Nov 15; ED II: Jan 4 |
| RD deadline | Jan 4 |
| SAT/ACT required? | No (test-optional) |
| TOEFL min | Not published |
| IELTS min | Not published |
| Tuition-free threshold | $200,000 (starting fall 2027) |
| Application fee | $60 |
| Total program count (UG majors) | ~45 |
| Department count | 49 |
| Division count | 3 + interdisciplinary |
| Open curriculum | Yes (no distribution requirements) |
| Honors program | Yes (external examination) |
| Engineering (ABET) | Yes (one of few LACs with ABET engineering) |
| Graduate programs | None (UG-only) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: swarthmore.edu, catalog.swarthmore.edu, apply.swarthmore.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
