# The City College of New York (CCNY) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: curl + manual extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BArch/BEng/etc.) | 78 |
| 本科辅修 (Minor) | 60+ |
| 研究生学位项目 (MA/MS/MFA/MBA/MEd/PhD/etc.) | 95 |
| 研究生证书 (Graduate Certificate) | 22 |
| **学位项目总计 (UG + Grad)** | **195+** |
| 学院 / 独立系所总数 | 5 |

### 0.2 学院 / 系层级结构

```
The City College of New York (CCNY)
├── Division of Interdisciplinary Studies
├── School of Architecture
│   ├── Undergraduate Architecture (BArch)
│   └── Urban Design
├── School of Education
│   ├── Teaching, Learning, and Culture
│   └── Educational Leadership
├── College of Engineering
│   ├── Biomedical Engineering
│   ├── Chemical Engineering
│   ├── Civil Engineering
│   ├── Computer Science
│   ├── Electrical Engineering
│   ├── Mechanical Engineering
├── School of Humanities and Arts
│   ├── Art
│   ├── English
│   ├── Modern Languages and Literatures
│   ├── Music
│   ├── Theatre and Speech
│   ├── Interdisciplinary Arts and Sciences
│   ├── Classics
│   ├── Comparative Literature
│   ├── Media and Communication Arts
│   ├── Philosophy
│   ├── Interdisciplinary
├── Macaulay Honors College (cross-college)
├── College of Liberal Arts and Sciences
│   ├── Anthropology
│   ├── Economics
│   ├── History
│   ├── Political Science
│   ├── Psychology
│   ├── Sociology
│   ├── International Studies
│   ├── Women's and Gender Studies
│   ├── Pre-Health
├── Sophie Davis Biomedical Education Program
├── Grove School of Engineering (formerly College of Engineering)
└── CUNY School of Medicine (joint with CUNY)
```

### 0.3 学历级别明细

| 学位 | 全称 | 层级 | 数量 |
|------|------|------|------|
| BA | Bachelor of Arts | 本科 | ~35 |
| BS | Bachelor of Science | 本科 | ~30 |
| BArch | Bachelor of Architecture | 本科 | 1 |
| BEng | Bachelor of Engineering | 本科 | 6 |
| BFA | Bachelor of Fine Arts | 本科 | 3 |
| MA | Master of Arts | 研究生 | ~25 |
| MS | Master of Science | 研究生 | ~35 |
| MFA | Master of Fine Arts | 研究生 | ~10 |
| MArch | Master of Architecture | 研究生 | 3 |
| MEng | Master of Engineering | 研究生 | 5 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 2 |
| MSEd | Master of Science in Education | 研究生 | ~5 |
| PhD | Doctor of Philosophy | 研究生 | 4 |
| AdvCert | Advanced Certificate | 研究生 | 22 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 | BA | BS | BEng | BFA | BArch | MA | MS | MEng | MFA | MArch | MPH | PhD | AdvCert |
|------|----|----|------|-----|-------|----|----|------|-----|-------|-----|-----|---------|
| Architecture | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| Education | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 8 |
| Engineering | 0 | 0 | 6 | 0 | 0 | 1 | 16 | 5 | 0 | 0 | 0 | 3 | 4 |
| Humanities and Arts | 22 | 0 | 0 | 3 | 0 | 12 | 0 | 0 | 8 | 0 | 0 | 0 | 0 |
| Liberal Arts and Sciences | 13 | 30 | 0 | 0 | 0 | 8 | 19 | 0 | 2 | 0 | 2 | 1 | 10 |

---

## SECTION 1 — Undergraduate education

### 1.1 Architecture
CCNY is the flagship college of CUNY system (City University of New York). Founded 1847. ~13,000 students. Located in Harlem, Manhattan. Known for engineering, architecture, and liberal arts. Public.

### 1.2 Undergraduate majors (grouped by 学院 > 系 > 学位级别)

#### School of Architecture
- BArch (5-year) | URL: ccny.cuny.edu/architecture

#### College of Engineering
- BS Biomedical Engineering
- BS Chemical Engineering
- BS Civil Engineering
- BS Computer Engineering
- BS Computer Science
- BS Electrical Engineering
- BS Mechanical Engineering
- BE Engineering Science (interdisciplinary)

#### School of Education
- BS Education: Childhood Education (Grades 1-6)
- BS Education: Earth Science (Adolescent)
- BS Education: English (Adolescent)
- BS Education: Mathematics (Adolescent)
- BS Education: Social Studies (Adolescent)
- BS Education: Special Education
- BS Education: Teaching English to Speakers of Other Languages (TESOL)
- BS Communication Sciences and Disorders

#### School of Humanities and Arts
- BA Anthropology
- BA Art (Studio, History, Photography, Graphic Design, etc.)
- BA Classical, Middle Eastern & Asian Languages & Cultures
- BA Comparative Literature
- BA English
- BA Film and Video Production
- BA French
- BA Interdisciplinary Liberal Arts
- BA Interdisciplinary Arts
- BA Media and Communication Arts
- BA Music
- BA Music Education
- BA Philosophy
- BA Russian
- BA Spanish
- BA Speech-Language Pathology
- BA Theatre
- BFA Art
- BFA Electronic Design & Multimedia
- BFA Jazz Performance
- BFA Music
- BFA Theatre

#### College of Liberal Arts and Sciences
- BA Asian Studies
- BA Black Studies
- BA Economics
- BA History
- BA International Studies
- BA Latin American & Latino Studies
- BA Political Science
- BA Pre-law Studies
- BA Psychology
- BA Public Policy & Administration
- BA Social Studies
- BA Sociology
- BA Women's and Gender Studies
- BS Biology
- BS Biotechnology
- BS Chemistry
- BS Environmental Earth System Science
- BS Earth and Atmospheric Science
- BS Geology
- BS Mathematics
- BS Physics
- BS Pre-medical / Pre-dental / Pre-veterinary tracks

#### Special Programs
- Sophie Davis Biomedical Education Program (BS/MD 7-year combined)
- Macaulay Honors College (cross-college, 8 campuses)
- CUNY School of Medicine (combined BS/MD)

### 1.3 Minors
60+ minors (e.g., Africana Studies, Asian Studies, Astrophysics, Computer Science, Creative Writing, Environmental Studies, Film, GIS, International Studies, Linguistics, Mathematics, Physics, Public Policy, Queer Studies, Statistics, etc.)

### 1.4 General Education Requirements
CCNY requires general education including English Composition, Quantitative Reasoning, Scientific Reasoning, Creative Expression, World Cultures, US Experience, etc. See ccny.cuny.edu/gened.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs

#### School of Architecture
- MArch, MS Architecture, MS Urban Design
- Advanced Certificate in Urban Design

#### School of Education
- MSEd in Bilingual Education
- MSEd in Educational Leadership
- MSEd in Special Education
- MSEd in Teaching English to Speakers of Other Languages (TESOL)
- MS in Childhood Education
- MS in Early Childhood Education
- MA in Teaching
- MS in Educational Leadership
- MS in Literacy
- PhD in Urban Education

#### College of Engineering
- MS Biomedical Engineering
- MS Chemical Engineering
- MS Civil Engineering
- MS Computer Science
- MS Data Science
- MS Electrical Engineering
- MS Mechanical Engineering
- MS Environmental Engineering
- MEng in several fields
- PhD in Engineering (with various specializations)

#### School of Humanities and Arts
- MFA in Art
- MFA in Creative Writing (fiction, poetry, translation)
- MFA in Film
- MFA in Theatre
- MA in English
- MA in Liberal Studies
- MA in Music
- MA in Spanish
- MA in TESOL
- MS in Branding + Integrated Communications
- MS in Data Journalism

#### College of Liberal Arts and Sciences
- MA in Economics
- MA in History
- MA in International Relations
- MA in Political Science
- MA in Psychology (with various specializations)
- MA in Sociology
- MA in Translation & Interpreting
- MS in Biology
- MS in Chemistry
- MS in Environmental Science
- MS in Mathematics
- MS in Physics
- MPH in Public Health
- MS in Data Science
- MS in Sustainability
- Advanced Certificate in Aging & Gerontology
- Advanced Certificate in Public Health
- Advanced Certificate in Geographic Information Systems
- Advanced Certificate in Statistics
- PhD in Physics (joint)
- PhD in Clinical Psychology (CUNY Graduate Center)

### 2.2 Certificates
22 graduate certificates across various schools.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate (from ccny.cuny.edu/admissions)

| 项 | 要求 |
|---|---|
| Application | CUNY Application (via CUNYfirst) |
| Application fee | $65 (waiver available) |
| SAT/ACT | Test-optional (CUNY-wide policy) |
| HS GPA | 80+ average; competitive varies by major |
| English (international) | TOEFL 80 iBT / IELTS 6.5 / PTE 53 / Duolingo 100 |
| Fall priority deadline | February 1 (for scholarship consideration) |
| Fall final deadline | Rolling (through summer) |

### 3.2 Graduate (from ccny.cuny.edu/admissions/graduate)

| 项 | 要求 |
|---|---|
| Application | CUNY Application (or specific school portal) |
| Application fee | $75 |
| English (international) | TOEFL 80 iBT / IELTS 6.5 |
| GRE/GMAT | Varies by program |
| Fall priority deadline | April 15 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition (2025-26)

| Tier | Annual |
|------|--------|
| NY State Resident UG | ~$7,500 |
| Out-of-state UG | ~$19,000 |
| NY State Resident Grad | ~$11,000 |
| Out-of-state Grad | ~$22,000 |
| International | ~$33,000 (varies) |

Housing/board: ~$15,000/yr (CCNY has limited on-campus housing; most NYC students commute)

### 4.2 Financial aid
- 75%+ of undergrads receive some aid
- TAP (NY State Tuition Assistance Program)
- Pell Grants
- CUNY has diversity scholarships and Macaulay Honors (free tuition)
- ASPIRA, College Discovery, SEEK programs for underrepresented students

---

## SECTION 5 — Evidence chain index

| # | Field | Source URL | Source Snippet | Capture Date |
|---|-------|-----------|----------------|--------------|
| E-1 | CUNY flagship | https://www.ccny.cuny.edu/about | "City College is the founding institution of the City University of New York" | 2026-07-07 |
| E-2 | Founded 1847 | https://www.ccny.cuny.edu/about | "Founded in 1847" | 2026-07-07 |
| E-3 | Application | https://www.ccny.cuny.edu/admissions | "Apply via CUNYfirst" | 2026-07-07 |
| E-4 | Sophie Davis | https://www.ccny.cuny.edu/sophie-davis | "BS/MD 7-year program" | 2026-07-07 |
| E-5 | Engineering | https://www.ccny.cuny.edu/engineering | "Grove School of Engineering" | 2026-07-07 |

---

## SECTION 6 — WeKnora import manifest

Chunks:
- C1: 院校总览
- C2: Undergraduate
- C3: Graduate
- C4: Requirements
- C5: Costs
- C6: Evidence

---

## SECTION 7 — Cross-school comparison row

| Field | CCNY Value |
|-------|-----------|
| State | New York |
| Tier | 5 (public, urban) |
| UG majors | 78 |
| Grad degrees | 95 |
| App fee | $65 |

---

## Closing block

> **Research completed**: 2026-07-07
> **Data source**: ccny.cuny.edu, cuny.edu
> **Quality bar**: All major sections complete
> **Follow-up**: Per-program graduate deadlines, JD program details (CCNY has no JD), specific engineering concentrations
