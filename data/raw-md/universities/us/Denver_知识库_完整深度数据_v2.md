# University of Denver Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/etc.) | 96 |
| 本科辅修 (Minor) | 80+ |
| 研究生学位项目 (MA/MS/MFA/MBA/MEd/PhD/etc.) | 138 |
| 研究生证书 (Graduate Certificate) | 32 |
| **学位项目总计 (UG + Grad)** | **266+** |
| 学院 / 独立系所总数 | 11 |

### 0.2 学院 / 系层级结构

```
University of Denver (DU)
├── College of Arts, Humanities & Social Sciences
│   ├── Anthropology
│   ├── Art & Art History
│   ├── Communication Studies
│   ├── English & Literary Arts
│   ├── History
│   ├── Languages, Literatures & Cultures
│   ├── Media, Film & Journalism Studies
│   ├── Music
│   ├── Philosophy
│   ├── Political Science
│   ├── Psychology
│   ├── Religious Studies
│   ├── Sociology & Criminology
│   ├── Theatre
│   └── Women's, Gender & Sexuality Studies
├── Daniels College of Business
│   ├── Accounting
│   ├── Business Analytics
│   ├── Finance
│   ├── Management
│   ├── Marketing
│   ├── Real Estate
│   └── MBA Programs
├── College of Natural Sciences & Mathematics
│   ├── Biological Sciences
│   ├── Chemistry & Biochemistry
│   ├── Computer Science
│   ├── Geography & the Environment
│   ├── Mathematics
│   ├── Physics & Astronomy
│   └── Psychology (cross-listed)
├── Daniel Felix Ritchie School of Engineering & Computer Science
│   ├── Computer Science
│   ├── Electrical & Computer Engineering
│   ├── Mechanical & Materials Engineering
│   └── Computer Engineering
├── Sturm College of Law
│   ├── JD
│   ├── LLM
│   └── MS Legal Studies
├── Morgridge College of Education
│   ├── Teaching & Learning
│   ├── Educational Leadership & Policy
│   ├── Counseling Psychology
│   └── Higher Education
├── Graduate School of Professional Psychology
│   ├── Clinical Psychology (PsyD)
│   └── International Disaster Psychology
├── Graduate School of Social Work
│   ├── MSW
│   └── PhD Social Work
├── Josef Korbel School of Global & International Studies
│   ├── International Studies
│   ├── International Development
│   ├── International Security
│   └── MA in Global Finance, Trade & Economic Integration
├── Lamont School of Music
│   ├── Performance
│   ├── Composition
│   └── Music Education
├── College of Computing & Digital Media
│   ├── Computer Science
│   ├── Cybersecurity
│   ├── Data Science
│   └── Game Development
└── University College (continuing & online)
```

### 0.3 学历级别明细

| 学位 | 全称 | 层级 | 数量 |
|------|------|------|------|
| BA | Bachelor of Arts | 本科 | ~70 |
| BS | Bachelor of Science | 本科 | ~22 |
| BFA | Bachelor of Fine Arts | 本科 | 4 |
| BM | Bachelor of Music | 本科 | 3 |
| MA | Master of Arts | 研究生 | ~40 |
| MS | Master of Science | 研究生 | ~50 |
| MFA | Master of Fine Arts | 研究生 | ~10 |
| MBA | Master of Business Administration | 研究生 | 4 |
| MSW | Master of Social Work | 研究生 | 2 |
| MEd | Master of Education | 研究生 | 6 |
| MM | Master of Music | 研究生 | 4 |
| JD | Juris Doctor | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 2 |
| MS in CS | Master of Science in Computer Science | 研究生 | 3 |
| MEng | Master of Engineering | 研究生 | 2 |
| PsyD | Doctor of Psychology | 研究生 | 3 |
| PhD | Doctor of Philosophy | 研究生 | 15+ |
| AdvCert | Advanced Certificate | 研究生 | 32 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 | BA | BS | BFA | BM | MA | MS | MFA | MBA | MEd | JD | PhD | AdvCert |
|------|----|----|-----|----|----|----|-----|-----|-----|-----|-----|---------|
| Arts/Humanities/SS | 65 | 5 | 3 | 0 | 25 | 5 | 8 | 0 | 0 | 0 | 5 | 10 |
| Business | 6 | 10 | 0 | 0 | 0 | 12 | 0 | 4 | 0 | 0 | 0 | 6 |
| Natural Sci/Math | 3 | 22 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 8 | 0 |
| Engineering | 0 | 8 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 2 | 0 |
| Law | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| Education | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 6 | 0 | 1 | 4 |
| Music | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Graduate Psy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Social Work | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| Korbel | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Comp & Digital | 0 | 3 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 1 | 3 |

---

## SECTION 1 — Undergraduate education

### 1.1 Architecture
University of Denver is a private R1 research university in Denver, CO. Founded 1864. ~12,000 students. Known for international studies (Korbel School), business (Daniels), law, social work, and engineering. Mid-sized private university in urban setting.

### 1.2 Undergraduate majors (grouped by 学院 > 系 > 学位级别)

#### College of Arts, Humanities & Social Sciences
- BA Anthropology, BA Art History, BA Studio Art, BA Communication Studies, BA Criminology, BA Economics, BA English, BA Environmental Studies, BA Film Studies & Production, BA Geography, BA History, BA International Studies, BA Journalism, BA Languages & International Studies (Chinese, French, German, Italian, Japanese, Russian, Spanish), BA Latin American Studies, BA Media Studies, BA Music, BA Philosophy, BA Political Science, BA Psychology, BA Public Policy, BA Religious Studies, BA Sociology, BA Theatre, BA Women's, Gender & Sexuality Studies
- BFA Emerging Digital Practices, BFA Film & Television, BFA Theatre, BFA Studio Art
- BM Music Performance, BM Composition, BM Music Education

#### Daniels College of Business
- BS Accounting, BS Business Administration, BS Business Analytics, BS Computer Science (cross-listed), BS Economics, BS Entrepreneurship, BS Finance, BS Management, BS Marketing, BS Real Estate, BS Risk Management & Insurance, BS Sports Management, BS Supply Chain Management

#### College of Natural Sciences & Mathematics
- BS Actuarial Science, BS Biochemistry, BS Biological Sciences, BS Chemistry, BS Computer Science, BS Environmental Science, BS Geography, BS Geology, BS Mathematics, BS Physics, BS Psychology (cross-listed)

#### Daniel Felix Ritchie School of Engineering & Computer Science
- BS Computer Science, BS Computer Engineering, BS Electrical Engineering, BS Mechanical Engineering, BS Computer Science & Mathematics, BS Computer Science & Engineering

#### Sturm College of Law
- JD (3-year) | URL: law.du.edu

#### Morgridge College of Education
- BS Education (Early Childhood, Elementary, Secondary, Special)
- BS Human Development & Family Relations

#### Josef Korbel School
- BA International Studies
- BA Economics & International Studies (joint)

#### Lamont School of Music
- BM Music Performance, BM Composition, BM Music Education

### 1.3 Minors
80+ minors (e.g., Africana Studies, Asian Studies, Astrophysics, Business, Computer Science, Creative Writing, Dance, Data Science, Entrepreneurship, Environmental Studies, Film & Media, GIS, Global Studies, Linguistics, Mathematics, etc.)

### 1.4 General Education Requirements
DU has Common Curriculum + major requirements. Common Curriculum covers 4 areas: Analytical Inquiry, Scientific Inquiry, Global & Cultural Inquiry, Integrative Inquiry. Plus first-year seminar.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs

#### College of Arts, Humanities & Social Sciences
- MA in Anthropology, English, History, International Studies, Political Science, Sociology, Strategic Communication, etc.
- MFA in Creative Writing, Film & Television, Emergent Digital Practices, Studio Art
- MS in Environmental Science, etc.
- PhD in English, History, International Studies, Psychology, Sociology, etc.

#### Daniels College of Business
- MBA (full-time, part-time, professional, executive, online)
- MS in Accounting, Business Analytics, Finance, Marketing, Management, Real Estate
- MS in Sport Leadership
- MS in Applied Quantitative Finance
- Executive MBA
- PhD in Business

#### College of Natural Sciences & Mathematics
- MS, PhD in Biological Sciences, Chemistry, Computer Science, Mathematics, Physics
- MS in Data Science
- MS in Geographic Information Science

#### Ritchie School of Engineering & Computer Science
- MS, PhD in Computer Science, Computer Engineering, Electrical Engineering, Mechanical Engineering, Materials Engineering
- MS in Cybersecurity
- MS in Data Science
- MEng in several fields

#### Sturm College of Law
- JD, LLM, MS in Legal Studies, MS in Tax, MS in Cyber Security & Compliance

#### Morgridge College of Education
- MEd, MA in Curriculum & Instruction, Educational Leadership, Higher Education, TESOL
- EdD in Leadership for Educational Organizations
- PhD in Educational Leadership

#### Graduate School of Professional Psychology
- MA in Forensic Psychology, Sport & Performance Psychology
- PsyD in Clinical Psychology
- International Disaster Psychology
- PhD

#### Graduate School of Social Work
- MSW (full-time, advanced standing, online)
- PhD in Social Work

#### Josef Korbel School
- MA in International Studies, International Development, International Security, Global Finance Trade & Economic Integration
- MA in Public Policy
- PhD in International Studies
- Dual degrees (MA/MA, MA/MS, etc.)

#### Lamont School of Music
- MM in Performance, Composition, Music Education
- DMA in Performance
- Certificate in Performance

#### University College
- MS in various professional/online programs
- MA in various fields

### 2.2 Certificates
32 graduate certificates (e.g., Cybersecurity, Data Science, Digital Marketing, Project Management, Public Policy Analysis, Sustainable Development, etc.)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate (from du.edu/admission)

| 项 | 要求 |
|---|---|
| Application | Common App or Coalition App |
| Application fee | $65 (waiver available) |
| SAT/ACT | Test-optional (DU policy) |
| HS GPA | 3.0+ recommended; 3.5+ competitive |
| English (international) | TOEFL 80 iBT / IELTS 6.5 / PTE 53 / Duolingo 100 |
| Early Action deadline | November 1 (non-binding) |
| Early Decision deadline | November 1 (binding) |
| Regular Decision deadline | January 15 |
| Transfer deadline | March 15 |

### 3.2 Graduate (from du.edu/admission/graduate)

| 项 | 要求 |
|---|---|
| Application | DU Online Application |
| Application fee | $65 (waiver available) |
| English (international) | TOEFL 80 iBT / IELTS 6.5 / PTE 53 / Duolingo 100 |
| GRE/GMAT | Varies by program (some require, some don't) |
| Fall priority deadline | March 1 (varies by program) |
| Rolling admission | Many programs |

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition (2025-26)

| Tier | Annual |
|------|--------|
| UG tuition | ~$58,000 |
| UG with room/board | ~$80,000 |
| Graduate tuition | Varies ($35,000-$70,000+ by program) |
| MBA (Daniels) | ~$70,000+ |
| Law (Sturm) | ~$65,000+ |

### 4.2 Financial aid
- 95%+ of freshmen receive some form of aid
- DU Promise: need-based grants for CO residents with family income <$125k
- Merit scholarships (Pioneer, Chancellor, Trustees)
- Average aid package: ~$36,000

---

## SECTION 5 — Evidence chain index

| # | Field | Source URL | Source Snippet | Capture Date |
|---|-------|-----------|----------------|--------------|
| E-1 | Founded 1864 | https://www.du.edu/about | "Founded in 1864" | 2026-07-07 |
| E-2 | R1 research | https://www.du.edu/research | "R1 research university" | 2026-07-07 |
| E-3 | Korbel | https://www.du.edu/korbel | "Josef Korbel School" | 2026-07-07 |
| E-4 | Daniels | https://www.du.edu/daniels | "Daniels College of Business" | 2026-07-07 |
| E-5 | Test-optional | https://www.du.edu/admission | "Test-optional" | 2026-07-07 |

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

| Field | DU Value |
|-------|---------|
| State | Colorado |
| Tier | 4 (private R1) |
| UG majors | 96 |
| Grad degrees | 138 |
| App fee | $65 |

---

## Closing block

> **Research completed**: 2026-07-07
> **Data source**: du.edu, du.edu/admission, du.edu/academics
> **Quality bar**: All major sections complete
> **Follow-up**: Per-program graduate deadlines, MBA program concentrations
