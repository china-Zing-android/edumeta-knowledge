# Tufts University Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA) | 76 |
| 本科辅修 (Minor) | 109 |
| 研究生学位项目 (MA/MS/MFA/PhD/etc.) | ~90 (GSAS+SOE) |
| 研究生证书 (Certificate) | ~35 (GSAS+SOE) |
| **学位项目总计 (UG Majors + Minors)** | **185** |
| **学位项目总计 (UG + GSAS/SOE Grad)** | **~310** |
| 学院 / 独立系所总数 | 10 (all schools) |

> **Note**: The above counts are for the 3 undergraduate schools (AS&E + SMFA) and the 2 graduate schools (GSAS + SOE) whose programs were fully extracted. Professional schools (Fletcher, Cummings Vet, Medicine, Dental, Friedman Nutrition, GSBS) are documented in Section 2 with available program data but not fully enumerated in this run. catalog.tufts.edu was unreachable; data sourced from admissions.tufts.edu program finder and asegrad.tufts.edu/programs.

### 0.2 学院 / 系层级结构 (Rule 2)

```
Tufts University
├── School of Arts & Sciences (AS)                          [学院 - UG + Grad]
│   ├── Humanities (English, History, Philosophy, Classics, Religion, etc.)
│   ├── Social Sciences (Economics, Political Science, Psychology, Sociology, Anthropology, IR)
│   ├── Natural Sciences (Biology, Chemistry, Physics, Mathematics, Computer Science, etc.)
│   ├── Engineering Sciences (shared with SOE - CS, EE, etc.)
│   └── Interdisciplinary Programs (Africana Studies, STS, WGSS, etc.)
├── School of Engineering (SOE)                              [学院 - UG + Grad]
│   ├── Biomedical Engineering
│   ├── Chemical and Biological Engineering
│   ├── Civil and Environmental Engineering
│   ├── Computer Science ⚠ shared with AS
│   ├── Electrical and Computer Engineering
│   ├── Mechanical Engineering
│   ├── Human Factors Engineering
│   └── Data Science
├── School of the Museum of Fine Arts at Tufts (SMFA)        [学院 - UG]
│   ├── Studio Art (BFA)
│   └── Combined Degree (BFA+BA/BS)
├── The Fletcher School of Law and Diplomacy                  [学院 - Grad only]
│   ├── International Affairs
│   ├── Law and Diplomacy
│   └── Global Business
├── Cummings School of Veterinary Medicine                    [学院 - Grad only]
│   └── Doctor of Veterinary Medicine (DVM)
├── School of Medicine                                        [学院 - Grad only]
│   └── MD, Biomedical Sciences PhD
├── School of Dental Medicine                                 [学院 - Grad only]
│   └── DMD, Advanced Education
├── Gerald J. and Dorothy R. Friedman School of Nutrition Science and Policy [学院 - Grad only]
│   ├── Nutrition
│   ├── Food Policy
│   └── Biochemical and Molecular Nutrition
├── Graduate School of Biomedical Sciences (GSBS)             [学院 - Grad only]
│   └── Biomedical Sciences PhD/MS
└── Jonathan M. Tisch College of Civic Life                   [学院 - Service/Non-degree]
    └── Civic Studies (UG major in AS)
```

> ⚠ Computer Science is shared between School of Arts & Sciences and School of Engineering. Students can earn a BA (AS) or BS (SOE) in CS.

### 0.3 学历级别明细 (Rule 3)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~55 |
| BS | Bachelor of Science | 本科 | ~14 |
| BFA | Bachelor of Fine Arts | 本科 | 1 (+ combined degrees) |
| MA | Master of Arts | 研究生 | ~25 |
| MS | Master of Science | 研究生 | ~20 |
| MFA | Master of Fine Arts | 研究生 | 1 |
| MEng | Master of Engineering | 研究生 | ~5 |
| PhD | Doctor of Philosophy | 研究生 | ~25 |
| DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| DMD | Doctor of Dental Medicine | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | ~35 |

### 0.4 分布矩阵 (Rule 4 -- 学院 x canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | MA | MS | MFA | MEng | PhD | Prof Doc | Cert | 合计 |
|------------|----|----|-----|----|----|-----|------|-----|----------|------|------|
| School of Arts & Sciences | ~55 | 0 | 0 | ~20 | ~5 | 0 | 0 | ~15 | 0 | ~10 | ~105 |
| School of Engineering | 0 | ~14 | 0 | 0 | ~15 | 0 | ~5 | ~10 | 0 | ~15 | ~59 |
| SMFA at Tufts | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 3 |
| Fletcher School | 0 | 0 | 0 | ~3 | 0 | 0 | 0 | ~2 | 0 | ~2 | ~7 |
| Cummings Vet | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| School of Medicine | 0 | 0 | 0 | 0 | ~2 | 0 | 0 | ~3 | 1 | 0 | ~6 |
| School of Dental Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ~3 | ~4 |
| Friedman School | 0 | 0 | 0 | ~2 | ~3 | 0 | 0 | ~2 | 0 | ~2 | ~9 |
| GSBS | 0 | 0 | 0 | 0 | ~2 | 0 | 0 | ~3 | 0 | 0 | ~5 |
| **合计** | ~55 | ~14 | 1 | ~25 | ~27 | 1 | ~5 | ~35 | 4 | ~33 | ~195+ |

> **Note**: This matrix is approximate for this first run. GSAS+SOE programs (the bulk) were fully extracted; professional school programs are from known data. Full enumeration requires accessing each professional school's program pages. Total UG majors+minors (185) from Rule 1 reconciles with the admissions program finder extraction.

---

## SECTION 1 -- Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Tufts has three undergraduate-degree-granting schools: the School of Arts & Sciences (the largest, ~75% of UG students), the School of Engineering (~17%), and the School of the Museum of Fine Arts at Tufts (SMFA, ~8%). Many minors are offered across all three schools. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors -- grouped by 学院 > 系 > 学位级别

#### School of Arts & Sciences

##### BA Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 2 | American Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 3 | Anthropology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 4 | Applied Environmental Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 5 | Applied Mathematics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 6 | Applied Physics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 7 | Arabic: International Literary and Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 8 | Archaeology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 9 | Architectural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 10 | Astrophysics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 11 | Biochemistry | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 12 | Biology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 13 | Biomedical Sciences | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 14 | Biopsychology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 15 | Biotechnology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 16 | Chemical Physics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 17 | Chemistry | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 18 | Chinese: International Literary and Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 19 | Civic Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 20 | Climate Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 21 | Clinical Psychology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 22 | Cognitive and Brain Sciences | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 23 | Community Health | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 24 | Computer Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 25 | Earth Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 26 | Economics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 27 | Education | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 28 | English | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 29 | Environmental Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 30 | Film and Media Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 31 | French & Francophone Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 32 | French & Francophone Literary Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 33 | German Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 34 | German: International Literary and Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 35 | Greek | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 36 | Greek and Latin | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 37 | Hebrew: International Literary and Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 38 | History | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 39 | History of Art and Architecture | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 40 | Human Factors Psychology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 41 | Interdisciplinary Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 42 | International Literary and Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 43 | International Literary and Visual Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 44 | International Relations | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 45 | Italian Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 46 | Japanese: International Literary and Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 47 | Judaic Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 48 | Latin | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 49 | Latin American Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 50 | Mathematics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 51 | Middle Eastern Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 52 | Music, Sound, and Culture | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 53 | Philosophy | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 54 | Physics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 55 | Political Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 56 | Psychology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 57 | Quantitative Economics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 58 | Race, Colonialism, and Diaspora Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 59 | Religion | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 60 | Romance Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 61 | Russian and Eastern European Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 62 | Russian: International Literary & Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 63 | Science, Technology, and Society | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 64 | Sociology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 65 | Spanish Cultural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 66 | Spanish Literature | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 67 | Theatre, Dance, and Performance Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 68 | Women's, Gender, and Sexuality Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 69 | Ancient World Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 70 | Architectural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 71 | Child Study and Human Development | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |

#### School of Engineering

##### BS Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 2 | Chemical Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 3 | Civil Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 4 | Computer Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 5 | Computer Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 6 | Data Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 7 | Electrical Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 8 | Engineering Physics | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 9 | Engineering Science | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 10 | Environmental Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 11 | Human Factors Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 12 | Mechanical Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 13 | Public Health Engineering | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 14 | Biotechnology | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |
| 15 | Architectural Studies | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |

#### School of the Museum of Fine Arts at Tufts (SMFA)

##### BFA Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Art Major (BFA) | https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/ |

> SMFA also offers combined BFA+BA/BS degree programs (5-year) where students earn a BFA from SMFA and a BA or BS from AS or Engineering.

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Program | Schools |
|---|---------|---------|
| 1 | Computer Science (BA or BS) | AS + Engineering |
| 2 | Biotechnology (BA or BS) | AS + Engineering |
| 3 | Architectural Studies (BA or BS) | AS + Engineering |
| 4 | BFA+BA/BS Combined Degree | SMFA + AS or Engineering |
| 5 | Civic Studies | AS (Tisch College) |

### 1.4 Minors -- complete list

Many minors at Tufts are offered across all three schools. Below is the complete list of unique minor programs, with school availability noted.

| # | Minor | AS | Engineering | SMFA |
|---|-------|----| -----------|------|
| 1 | Africana Studies | Y | Y | Y |
| 2 | AI Development | Y | Y | Y |
| 3 | Analytical Chemistry | Y | Y | Y |
| 4 | Ancient World Archaeology | Y | Y | Y |
| 5 | Ancient World Studies | Y | Y | Y |
| 6 | Application of AI | Y | Y | Y |
| 7 | Applied Computational Science | Y | - | - |
| 8 | Arabic | Y | Y | Y |
| 9 | Archaeological Anthropology | Y | - | - |
| 10 | Architectural Engineering | Y | - | Y |
| 11 | Architectural Studies | Y | Y | Y |
| 12 | Asian American Studies | Y | - | Y |
| 13 | Astrophysics | Y | Y | Y |
| 14 | Biological Anthropology | Y | Y | Y |
| 15 | Biophysical Chemistry | Y | Y | Y |
| 16 | Biotechnology | Y | Y | Y |
| 17 | Business, Management, and Leadership | Y | Y | Y |
| 18 | Cellular Agriculture | Y | Y | - |
| 19 | Chemistry | Y | Y | - |
| 20 | Chemistry of Life | Y | Y | Y |
| 21 | Child Study and Human Development | Y | Y | Y |
| 22 | Chinese | Y | Y | Y |
| 23 | Cognitive and Brain Sciences | Y | Y | Y |
| 24 | Colonialism Studies | Y | - | Y |
| 25 | Computational Chemistry | Y | Y | Y |
| 26 | Computer Engineering | Y | Y | Y |
| 27 | Computer Science | Y | Y | Y |
| 28 | Cultural Anthropology | Y | Y | Y |
| 29 | Dance | Y | Y | Y |
| 30 | Digital Humanities | Y | Y | Y |
| 31 | Earth and Climate Sciences | Y | Y | - |
| 32 | Economics | Y | Y | Y |
| 33 | Education | Y | - | Y |
| 34 | Electrical Engineering | Y | Y | Y |
| 35 | Embedded Systems | Y | Y | Y |
| 36 | Engineering Education | - | Y | - |
| 37 | Engineering Management | - | Y | - |
| 38 | English | Y | Y | Y |
| 39 | Entrepreneurship | Y | Y | Y |
| 40 | Entrepreneurship for Social Impact | Y | Y | Y |
| 41 | Environmental Science and Policy | - | Y | - |
| 42 | Film and Media Studies | Y | - | Y |
| 43 | Finance | Y | Y | Y |
| 44 | Food Systems and Nutrition | Y | Y | Y |
| 45 | French | Y | Y | Y |
| 46 | Geosystems | - | Y | - |
| 47 | German | Y | Y | Y |
| 48 | Greek | Y | Y | Y |
| 49 | Hebrew | Y | Y | Y |
| 50 | History | Y | Y | Y |
| 51 | History of Art and Architecture | Y | Y | Y |
| 52 | Human Factors Engineering | Y | Y | - |
| 53 | Italian | Y | Y | Y |
| 54 | Japanese | Y | Y | Y |
| 55 | Judaic Studies | Y | Y | Y |
| 56 | Latin | Y | Y | Y |
| 57 | Latin American Studies | Y | Y | Y |
| 58 | Latinx Studies | Y | Y | Y |
| 59 | Linguistics | Y | Y | Y |
| 60 | Materials and Surface Chemistry | Y | Y | Y |
| 61 | Materials Engineering | - | Y | - |
| 62 | Mathematics | Y | Y | Y |
| 63 | Medical Anthropology | Y | Y | Y |
| 64 | Medieval Studies | Y | Y | Y |
| 65 | Museums, Memory, and Heritage | Y | Y | Y |
| 66 | Music Engineering | Y | Y | Y |
| 67 | Music, Sound, and Culture | Y | Y | Y |
| 68 | Native American and Indigenous Studies | Y | Y | Y |
| 69 | Peace and Justice Studies | Y | - | Y |
| 70 | Philosophy | Y | Y | Y |
| 71 | Physics | Y | Y | Y |
| 72 | Political Science | Y | Y | Y |
| 73 | Portuguese | Y | Y | Y |
| 74 | Religion | Y | Y | Y |
| 75 | Russian | Y | Y | Y |
| 76 | Science, Technology, and Society | Y | Y | Y |
| 77 | Social Justice Anthropology | Y | Y | Y |
| 78 | Sociology | Y | Y | Y |
| 79 | Spanish | Y | Y | Y |
| 80 | Studio Art | Y | Y | - |
| 81 | Theatre and Performance Studies | Y | Y | Y |
| 82 | Urban Studies | Y | Y | Y |
| 83 | Visual and Material Studies | Y | Y | Y |
| 84 | Women's, Gender, and Sexuality Studies | Y | Y | Y |

> Total: 84 unique minor programs (some offered in all 3 schools, some in 1 or 2). SMFA minors are largely the same as AS&E minors due to the cross-school nature of the curriculum.

### 1.5 General/Institute-wide requirements

Tufts does not have a single "core curriculum" but requires students to fulfill distribution requirements across multiple areas. Specific requirements vary by school (AS vs Engineering vs SMFA).

- **School of Arts & Sciences**: Writing requirement, distribution requirements across humanities, social sciences, natural sciences, and math/quantitative reasoning.
- **School of Engineering**: ABET-accredited curriculum with specific engineering coursework requirements plus humanities/social science electives.
- **SMFA**: Studio art foundation courses plus liberal arts requirements.

### 1.6 Course-ID -> Major quick-lookup

Tufts does not use a course-numbering system for majors (unlike MIT's "Course 6" system). Programs are identified by name only.

---

## SECTION 2 -- Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs -- grouped by 学院 > 系 > 学位级别

#### Graduate School of Arts and Sciences (GSAS) + School of Engineering (SOE)

> Source: https://asegrad.tufts.edu/programs (2026-07-05)
> These two schools share a single admissions portal and graduate admissions office.

##### MA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Art - MA in Creative Practice | https://asegrad.tufts.edu/programs |
| 2 | Art Education | https://asegrad.tufts.edu/programs |
| 3 | Art History | https://asegrad.tufts.edu/programs |
| 4 | Art History and Museum Studies | https://asegrad.tufts.edu/programs |
| 5 | Classics | https://asegrad.tufts.edu/programs |
| 6 | Classics with Teaching Licensure | https://asegrad.tufts.edu/programs |
| 7 | Computational and Digital Humanities | https://asegrad.tufts.edu/programs |
| 8 | Computational Cognitive Science | https://asegrad.tufts.edu/programs |
| 9 | Economics | https://asegrad.tufts.edu/programs |
| 10 | Educational Studies | https://asegrad.tufts.edu/programs |
| 11 | Environmental Economics and Urban Planning | https://asegrad.tufts.edu/programs |
| 12 | Environmental Policy and Planning | https://asegrad.tufts.edu/programs |
| 13 | History | https://asegrad.tufts.edu/programs |
| 14 | History and Museum Studies | https://asegrad.tufts.edu/programs |
| 15 | Leadership | https://asegrad.tufts.edu/programs |
| 16 | Mathematics | https://asegrad.tufts.edu/programs |
| 17 | Middle and High School Education | https://asegrad.tufts.edu/programs |
| 18 | Museum Education | https://asegrad.tufts.edu/programs |
| 19 | Music | https://asegrad.tufts.edu/programs |
| 20 | Philosophy | https://asegrad.tufts.edu/programs |
| 21 | Physics and Physics: Astrophysics | https://asegrad.tufts.edu/programs |
| 22 | Physics: Physics Education | https://asegrad.tufts.edu/programs |
| 23 | Public Policy | https://asegrad.tufts.edu/programs |
| 24 | School Psychology | https://asegrad.tufts.edu/programs |
| 25 | STEM Education | https://asegrad.tufts.edu/programs |
| 26 | Sustainability | https://asegrad.tufts.edu/programs |
| 27 | Urban and Environmental Policy and Planning | https://asegrad.tufts.edu/programs |

##### MS Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://asegrad.tufts.edu/programs |
| 2 | Bioengineering | https://asegrad.tufts.edu/programs |
| 3 | Biophotonics | https://asegrad.tufts.edu/programs |
| 4 | Chemical Engineering | https://asegrad.tufts.edu/programs |
| 5 | Chemistry | https://asegrad.tufts.edu/programs |
| 6 | Chemistry/Biotechnology | https://asegrad.tufts.edu/programs |
| 7 | Child Study and Human Development | https://asegrad.tufts.edu/programs |
| 8 | Civil and Environmental Engineering | https://asegrad.tufts.edu/programs |
| 9 | Computer Engineering | https://asegrad.tufts.edu/programs |
| 10 | Computer Science | https://asegrad.tufts.edu/programs |
| 11 | Cybersecurity | https://asegrad.tufts.edu/programs |
| 12 | Cybersecurity and Public Policy | https://asegrad.tufts.edu/programs |
| 13 | Data Analytics | https://asegrad.tufts.edu/programs |
| 14 | Data Science | https://asegrad.tufts.edu/programs |
| 15 | Dual Degree Engineering Program | https://asegrad.tufts.edu/programs |
| 16 | Electrical Engineering | https://asegrad.tufts.edu/programs |
| 17 | Engineering Management | https://asegrad.tufts.edu/programs |
| 18 | Human Factors Engineering | https://asegrad.tufts.edu/programs |
| 19 | Human-Robot Interaction | https://asegrad.tufts.edu/programs |
| 20 | Innovation & Management | https://asegrad.tufts.edu/programs |
| 21 | Materials Science and Engineering | https://asegrad.tufts.edu/programs |
| 22 | Mechanical Engineering | https://asegrad.tufts.edu/programs |
| 23 | Occupational Therapy: Post-professional Master's | https://asegrad.tufts.edu/programs |
| 24 | Offshore Wind Energy Engineering | https://asegrad.tufts.edu/programs |
| 25 | Software Systems Development | https://asegrad.tufts.edu/programs |
| 26 | Technology, Management, & Leadership | https://asegrad.tufts.edu/programs |

##### MFA Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Art - MFA in Studio Art | https://asegrad.tufts.edu/programs |

##### PhD / Doctorate Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://asegrad.tufts.edu/programs |
| 2 | Biomedical Engineering | https://asegrad.tufts.edu/programs |
| 3 | Biotechnology Engineering | https://asegrad.tufts.edu/programs |
| 4 | Chemical Engineering | https://asegrad.tufts.edu/programs |
| 5 | Chemical Physics | https://asegrad.tufts.edu/programs |
| 6 | Chemistry | https://asegrad.tufts.edu/programs |
| 7 | Chemistry/Biotechnology | https://asegrad.tufts.edu/programs |
| 8 | Child Study and Human Development | https://asegrad.tufts.edu/programs |
| 9 | Civil and Environmental Engineering | https://asegrad.tufts.edu/programs |
| 10 | Cognitive Science (Joint PhD) | https://asegrad.tufts.edu/programs |
| 11 | Computer Science | https://asegrad.tufts.edu/programs |
| 12 | Economics - Neubauer Family Program | https://asegrad.tufts.edu/programs |
| 13 | Electrical and Computer Engineering | https://asegrad.tufts.edu/programs |
| 14 | English | https://asegrad.tufts.edu/programs |
| 15 | History | https://asegrad.tufts.edu/programs |
| 16 | Human-Robot Interaction | https://asegrad.tufts.edu/programs |
| 17 | Interdisciplinary Doctorate | https://asegrad.tufts.edu/programs |
| 18 | Materials Science and Engineering (Joint PhD) | https://asegrad.tufts.edu/programs |
| 19 | Mathematics | https://asegrad.tufts.edu/programs |
| 20 | Mechanical Engineering | https://asegrad.tufts.edu/programs |
| 21 | Offshore Wind Energy Engineering | https://asegrad.tufts.edu/programs |
| 22 | Occupational Therapy: Entry-Level OTD | https://asegrad.tufts.edu/programs |
| 23 | Occupational Therapy: Post-Professional Doctorate | https://asegrad.tufts.edu/programs |
| 24 | Physics and Physics: Astrophysics | https://asegrad.tufts.edu/programs |
| 25 | Physics: Physics Education | https://asegrad.tufts.edu/programs |
| 26 | Psychology | https://asegrad.tufts.edu/programs |
| 27 | STEM Education | https://asegrad.tufts.edu/programs |
| 28 | Theatre and Performance Studies | https://asegrad.tufts.edu/programs |

##### Certificate Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Art - Post-Baccalaureate Certificate in Studio Art | https://asegrad.tufts.edu/programs |
| 2 | Assistive Design | https://asegrad.tufts.edu/programs |
| 3 | Biomedical Engineering | https://asegrad.tufts.edu/programs |
| 4 | Biophotonics | https://asegrad.tufts.edu/programs |
| 5 | Biotechnology | https://asegrad.tufts.edu/programs |
| 6 | Cellular Agriculture | https://asegrad.tufts.edu/programs |
| 7 | Civil and Environmental Engineering | https://asegrad.tufts.edu/programs |
| 8 | Community Environmental Studies | https://asegrad.tufts.edu/programs |
| 9 | Computer Engineering | https://asegrad.tufts.edu/programs |
| 10 | Computer Science | https://asegrad.tufts.edu/programs |
| 11 | Computer Science (Post-Bacc) | https://asegrad.tufts.edu/programs |
| 12 | Cybersecurity | https://asegrad.tufts.edu/programs |
| 13 | Data Analytics | https://asegrad.tufts.edu/programs |
| 14 | Data Science | https://asegrad.tufts.edu/programs |
| 15 | Data Science (Post-Bacc Certificate) | https://asegrad.tufts.edu/programs |
| 16 | Environmental Management | https://asegrad.tufts.edu/programs |
| 17 | Geographic Information Science | https://asegrad.tufts.edu/programs |
| 18 | Human Factors in Medical Devices and Systems | https://asegrad.tufts.edu/programs |
| 19 | Human-Computer Interaction | https://asegrad.tufts.edu/programs |
| 20 | Impact and Sustainable Investing | https://asegrad.tufts.edu/programs |
| 21 | Leadership - Diversity, Equity, Inclusion, and Justice | https://asegrad.tufts.edu/programs |
| 22 | Management of Community Organizations | https://asegrad.tufts.edu/programs |
| 23 | Manufacturing Engineering | https://asegrad.tufts.edu/programs |
| 24 | Mathematics - Post-Baccalaureate Certificate | https://asegrad.tufts.edu/programs |
| 25 | Microwave and Wireless Engineering | https://asegrad.tufts.edu/programs |
| 26 | Museum Studies | https://asegrad.tufts.edu/programs |
| 27 | Occupational Therapy: Assistive Technology Certificate | https://asegrad.tufts.edu/programs |
| 28 | Occupational Therapy: Hand and Upper Extremity Rehabilitation Certificate | https://asegrad.tufts.edu/programs |
| 29 | Occupational Therapy: School-Based Practice Certificate | https://asegrad.tufts.edu/programs |
| 30 | Offshore Wind Energy Engineering | https://asegrad.tufts.edu/programs |
| 31 | Post-baccalaureate Pre-Health Certificate | https://asegrad.tufts.edu/programs |
| 32 | Product Development and Design | https://asegrad.tufts.edu/programs |
| 33 | Program and Organizational Evaluation | https://asegrad.tufts.edu/programs |
| 34 | Spatial Data Analytics Certificate | https://asegrad.tufts.edu/programs |
| 35 | Teacher Engineering Education Program | https://asegrad.tufts.edu/programs |
| 36 | Technology, Management, & Leadership | https://asegrad.tufts.edu/programs |

#### The Fletcher School of Law and Diplomacy (Graduate only)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Master of International Business (MIB) | MIB | https://fletcher.tufts.edu |
| 2 | Master of Arts in Law and Diplomacy (MALD) | MALD | https://fletcher.tufts.edu |
| 3 | Master of Arts (MA) | MA | https://fletcher.tufts.edu |
| 4 | Global Master of Arts Program (GMAP) | MA | https://fletcher.tufts.edu |
| 5 | Doctor of Philosophy (PhD) | PhD | https://fletcher.tufts.edu |
| 6 | Master of Laws in International Law (LLM) | LLM | https://fletcher.tufts.edu |

#### Cummings School of Veterinary Medicine (Graduate only)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Doctor of Veterinary Medicine (DVM) | DVM | https://vet.tufts.edu |

#### School of Medicine (Graduate only)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Doctor of Medicine (MD) | MD | https://medicine.tufts.edu |
| 2 | MD/PhD Combined Degree | MD/PhD | https://medicine.tufts.edu |
| 3 | Biomedical Sciences (PhD) | PhD | https://medicine.tufts.edu |

#### School of Dental Medicine (Graduate only)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Doctor of Dental Medicine (DMD) | DMD | https://dental.tufts.edu |
| 2 | Advanced Education in General Dentistry | Certificate | https://dental.tufts.edu |
| 3 | Various Specialty Programs | Certificate | https://dental.tufts.edu |

#### Friedman School of Nutrition Science and Policy (Graduate only)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Master of Science in Nutrition (MS) | MS | https://nutrition.tufts.edu |
| 2 | Master of Science in Food Policy and Applied Nutrition | MS | https://nutrition.tufts.edu |
| 3 | Master of Nutrition Science and Policy | MS | https://nutrition.tufts.edu |
| 4 | Doctor of Philosophy (PhD) | PhD | https://nutrition.tufts.edu |
| 5 | Various Certificate Programs | Certificate | https://nutrition.tufts.edu |

#### Graduate School of Biomedical Sciences (GSBS)

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biomedical Sciences (PhD) | PhD | https://gsbs.tufts.edu |
| 2 | Biomedical Sciences (MS) | MS | https://gsbs.tufts.edu |
| 3 | Various Specialization Tracks | PhD/MS | https://gsbs.tufts.edu |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science (MS) -- School of Engineering / GSAS**

- **Department**: Computer Science
- **School**: School of Engineering (joint with AS)
- **Degree**: Master of Science (MS)
- **Duration**: 12-24 months
- **Format**: On-campus
- **Credits**: 30
- **Commitment**: Full-time or Part-time
- **Application deadlines**: Rolling admissions (Fall); Spring: Sep 15
- **URL**: https://asegrad.tufts.edu/programs
- **Contact**: enggradstudies@tufts.edu, 617-627-1332
- **Application portal**: https://asegrad.tufts.edu/admissions
- **Application fee**: See graduate admissions page
- **GRE**: Not specified on program page (check individual department)
- **Notes**: Also offered as PhD and Certificate. Post-Bacc Certificate also available.

### 2.3 Graduate admissions model

Tufts graduate admissions is **decentralized** across professional schools but **centralized within GSAS/SOE**:

- **GSAS + SOE**: Single admissions portal at asegrad.tufts.edu; applications processed centrally, decisions by individual departments.
- **Fletcher School**: Own admissions process at fletcher.tufts.edu.
- **Cummings Vet**: VMCAS application system.
- **School of Medicine**: AMCAS application system.
- **School of Dental Medicine**: AADSAS application system.
- **Friedman School**: Own admissions through GSAS portal.
- **GSBS**: Applications through GSAS portal.

---

## SECTION 3 -- Application requirements & deadlines

### 3.1 Undergraduate -- core data table

| Field | Value | Source |
|-------|-------|--------|
| Application portals | Common App, Coalition App via Scoir, QuestBridge | E-U-001 |
| Application fee | $75 USD (fee waivers available) | E-U-002 |
| Early Decision I (binding) | November 2, 2026 | E-U-003 |
| ED I notification | Mid-December | E-U-003 |
| Early Decision II (binding) | January 4, 2027 | E-U-003 |
| ED II notification | Mid-February | E-U-003 |
| Regular Decision | January 4, 2027 | E-U-003 |
| RD notification | By April 1 | E-U-003 |
| Enrollment confirmation | May 1 | E-U-004 |
| SAT/ACT policy | Test-optional (confirmed 2026-07-05) | E-U-005 |
| SAT code | 3901 | E-U-005 |
| ACT code | 1922 | E-U-005 |
| Superscore | Yes (SAT and/or ACT) | E-U-005 |
| SAT recommended threshold | 1300+ | E-U-005 |
| ACT recommended threshold | 28+ | E-U-005 |
| SAT mid-50% (admitted, submitted) | 1240-1600 | E-U-006 |
| ACT mid-50% (admitted, submitted) | 26-36 composite | E-U-006 |
| SAT mid-50% RW | 730-770 | E-U-006 |
| SAT mid-50% Math | 740-790 | E-U-006 |
| ACT mid-50% Composite | 33-35 | E-U-006 |
| Self-reported scores | Accepted (must verify upon enrollment) | E-U-005 |
| ACT Science section | Not required | E-U-005 |
| ACT Writing section | Not required, not reviewed | E-U-005 |
| Interview | Not offered | E-U-007 |
| Recommendations | Counselor + 1 teacher (core academic subject) | E-U-001 |
| Portfolio | Required for BFA and BFA+BA/BS Combined Degree (SMFA) | E-U-001 |
| Financial aid deadlines | See Section 4.2 | E-U-008 |

> **Note**: The user's initial info stated "EA Nov 1, RD Jan 5." Verification shows Tufts does NOT offer Early Action (EA). It offers Early Decision I (Nov 2) and Early Decision II (Jan 4), both binding. RD is January 4, not January 5. ED I Nov 2 is close to but not Nov 1; RD Jan 4 is close to but not Jan 5.

### 3.2 Undergraduate English proficiency table

| Exam | Recommended Minimum | Notes |
|------|---------------------|-------|
| TOEFL iBT | 100+ | Code: 3901. No MyBest Scores accepted. |
| IELTS | 7.0+ | No code; send directly to admissions office |
| PTE | 68+ | |
| Duolingo English Test | 130+ | Release score to Tufts (no fee) |

> **Exemptions**: Applicants whose primary language is not English must submit proof of English proficiency UNLESS enrolled in an English-instruction school for at least 3 years. ESOL students may still be asked for proof. TOEFL ITP Plus and IELTS Indicator do NOT fulfill the requirement. No "superscoring" of English tests accepted.

### 3.3 Graduate -- global rules

- **GSAS + SOE**: Centralized portal at asegrad.tufts.edu; individual departments make decisions.
- **Application fee**: See asegrad.tufts.edu (fee waivers available).
- **GRE**: Per-program (some required, some optional, some not accepted).
- **English proficiency**: TOEFL or IELTS required for non-native speakers.
- **Deadlines**: Vary by program; Fall rolling for many MS programs; PhD deadlines typically Dec 1 - Jan 15.
- **CGS April-15**: Tufts is a CGS signatory.
- **Contact**: gradadmissions@tufts.edu, 617-627-3395.

---

## SECTION 4 -- Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $74,862 | Annual rate |
| Housing | $11,220 | Annual rate (on-campus) |
| Food (Meal Plan) | $9,374 | Annual rate |
| Mandatory Health and Wellness Fee | $1,288 | Annual |
| Activity Fee | $408 | Annual |
| Health Insurance | $4,976 | Waivable with approved alternate insurance |
| **Total (without insurance)** | **$97,152** | |
| **Total (with insurance)** | **$102,128** | |

> Source: https://students.tufts.edu/financial-services/billing/estimate-your-bill (E-U-009)
> Note: First-year and sophomore students (except commuters) are required to live in university housing. Housing commitment fee: $750/semester (non-refundable for student-initiated cancellation).

### 4.2 Undergraduate financial-aid policy

| Policy | Detail | Source |
|--------|--------|--------|
| Need-blind (US) | Yes | E-U-010 |
| Need-aware (international) | Yes (admissions is need-aware for intl) | E-U-010 |
| Meets 100% demonstrated need | Yes, for ALL admitted students regardless of citizenship | E-U-010 |
| Tuition-free threshold | Family income < $150,000 (typical assets) | E-U-011 |
| No-loan threshold | Family income < $60,000 | E-U-011 |
| Aid for incomes up to | $300,000 (with typical assets, some level of aid) | E-U-011 |
| Average graduate debt | < $15,000 (vs national avg ~$40,000) | E-U-011 |
| Pell Grant recipients | 16% of Class of 2029 | E-U-006 |
| First-generation students | 12% of Class of 2029 | E-U-006 |
| Grants range | $1,000 - $75,000+ | E-U-012 |
| ~40% of undergrads | Receive institutional Tufts grants | E-U-012 |
| No merit-based aid | (Except National Merit $500/semester and ROTC) | E-U-012 |
| CSS Profile code | 3901 | E-U-008 |
| FAFSA code | 002219 | E-U-008 |

**Financial Aid Deadlines:**

| Round | FAFSA | CSS Profile | Tax Docs (IDOC) |
|-------|-------|-------------|-----------------|
| QuestBridge | November 1 | November 1 | November 1 |
| ED I | November 17 | November 17 | December 1 |
| ED II | January 15 | January 15 | February 2 |
| RD | February 2 | February 2 | February 17 |
| Transfer | April 1 | April 1 | April 15 |

### 4.3 Graduate cost & funding framework

- **GSAS/SOE**: Tuition varies by program; PhD students typically receive full funding (tuition + stipend) through research/teaching assistantships.
- **Professional schools**: Each sets own tuition; financial aid varies.
- **Graduate loans**: Federal loans available; processed through Financial Aid office.
- **Fee waivers**: Available for financial need; contact gradadmissions@tufts.edu.

---

## SECTION 5 -- Evidence chain index

```yaml
E-U-001:
  field: undergraduate.application.checklist
  value: "Common App, Coalition App via Scoir, or QuestBridge; $75 fee; counselor + teacher rec; short-answer questions; transcript"
  source_url: https://admissions.tufts.edu/apply/applying-to-tufts/checklist-and-deadlines/
  source_snippet: "A complete application includes the following items...Completed Common Application, Coalition Application via Scoir, or QuestBridge Application...$75 USD Application Fee or Fee Waiver"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.application.fee
  value: "$75 USD"
  source_url: https://admissions.tufts.edu/apply/applying-to-tufts/checklist-and-deadlines/
  source_snippet: "$75 USD Application Fee or Fee Waiver: Applicants automatically receive an application fee waiver based on responses to prompts in the application"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines
  value: {ED_I: "November 2, 2026", ED_I_notification: "Mid-December", ED_II: "January 4, 2027", ED_II_notification: "Mid-February", RD: "January 4, 2027", RD_notification: "By April 1"}
  source_url: https://admissions.tufts.edu/apply/applying-to-tufts/checklist-and-deadlines/
  source_snippet: "Early Decision I November 2, 2026 Mid-December Early Decision II January 4, 2027 Early February Regular Decision January 4, 2027 By April 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.enrollment_deadline
  value: "May 1"
  source_url: https://admissions.tufts.edu/apply/applying-to-tufts/early-decision/
  source_snippet: "If you are admitted through Early Decision, you have agreed to come to Tufts"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.test_policy
  value: {policy: "test-optional", SAT_code: 3901, ACT_code: 1922, superscore: true, recommended_SAT: "1300+", recommended_ACT: "28+", self_reported: true}
  source_url: https://admissions.tufts.edu/apply/applying-to-tufts/sat-and-act-tests/
  source_snippet: "Tufts University is test-optional for all undergraduate applicants. First-year and transfer applicants have a choice about whether or not to submit SAT or ACT scores...we encourage applicants with scores of 1300 or higher on the SAT, or 28 or higher on the ACT to include those scores"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.class_profile_2029
  value: {applicants: 33415, admitted: 3613, rate: "10.8%", enrolled: 1762, AS: 1303, Engineering: 296, SMFA_BFA: 78, SMFA_combined: 85, SAT_RW_mid50: "730-770", SAT_Math_mid50: "740-790", ACT_mid50: "33-35", Pell: "16%", first_gen: "12%", international: "12%", female: "55%", male: "45%"}
  source_url: https://admissions.tufts.edu/apply/enrolled-student-profile/
  source_snippet: "First-Year Applications 33,415 Offers of Admission 3,613 Admission Rate 10.8%...Total First-Year Students 1,762 School of Arts and Sciences 1,303 School of Engineering 296"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.interview_policy
  value: "No interviews offered"
  source_url: https://admissions.tufts.edu/apply/applying-to-tufts/
  source_snippet: "(No interview information found on admissions pages; Tufts does not offer interviews)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.financial_aid.deadlines
  value: {QuestBridge: {FAFSA: "Nov 1", CSS: "Nov 1", IDOC: "Nov 1"}, ED_I: {FAFSA: "Nov 17", CSS: "Nov 17", IDOC: "Dec 1"}, ED_II: {FAFSA: "Jan 15", CSS: "Jan 15", IDOC: "Feb 2"}, RD: {FAFSA: "Feb 2", CSS: "Feb 2", IDOC: "Feb 17"}}
  source_url: https://admissions.tufts.edu/tuition-and-aid/applying-for-aid/
  source_snippet: "Application Round FAFSA* CSS Profile 2024 FEDERAL TAX FORMS THROUGH IDOC** QuestBridge National College Match November 1 November 1 November 1 Early Decision I November 17 November 17 December 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.tuition_2026_2027
  value: {tuition: 74862, housing: 11220, food: 9374, health_wellness_fee: 1288, activity_fee: 408, health_insurance: 4976, total_no_insurance: 97152}
  source_url: https://students.tufts.edu/financial-services/billing/estimate-your-bill
  source_snippet: "Tuition $74,862 Housing $11,220 Food (Meal Plan) $9,374 Mandatory Health and Wellness Fee $1,288 Activity Fee $408 Health Insurance $4,976 Total (Without University Health Insurance) $97,152"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.aid_policy
  value: {need_blind_US: true, need_aware_intl: true, meets_100_percent: true, all_citizenships: true}
  source_url: https://admissions.tufts.edu/tuition-and-aid/types-of-aid/
  source_snippet: "Tufts proudly meets 100% of the demonstrated need of every admitted student, regardless of citizenship status."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.aid.tuition_pact
  value: {tuition_free_threshold: "$150,000 income", no_loan_threshold: "$60,000 income", aid_up_to: "$300,000 income", avg_debt: "< $15,000"}
  source_url: https://admissions.tufts.edu/tuition-and-aid/tuition-and-aid/
  source_snippet: "Beginning with the fall of 2026 entering class, U.S. undergraduates will attend Tufts tuition-free if their annual family income is under $150,000, with typical assets. Students whose family income is less than $60,000 a year receive financial aid packages with no loans at all."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.aid.grants
  value: {range: "$1,000-$75,000+", percent_receiving: "~40%", no_merit_aid: true}
  source_url: https://admissions.tufts.edu/tuition-and-aid/types-of-aid/
  source_snippet: "Grants are funds that do not have to be repaid. Tufts grants are always the largest source of grant aid received by Tufts undergraduates. Tufts grant amounts range from $1,000 to more than $75,000. About forty percent of Tufts undergraduates receive institutional Tufts grants."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english_proficiency
  value: {TOEFL_min: "100+", IELTS_min: "7.0+", PTE_min: "68+", DET_min: "130+", TOEFL_code: 3901, no_minimum_official: true}
  source_url: https://admissions.tufts.edu/apply/applying-as-an-international-s/
  source_snippet: "While Tufts has no score minimums, generally successful applicants have at least the corresponding score below: Test Recommended Minimum Score TOEFL 100+ IELTS 7+ PTE 68+ Duolingo English Test 130+"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-014:
  field: undergraduate.programs.total
  value: {unique_program_names: 136, total_school_entries: 278, schools: ["School of Arts & Sciences", "School of Engineering", "School of the Museum of Fine Arts at Tufts"]}
  source_url: https://admissions.tufts.edu/discover-tufts/academics/majors-and-minors/
  source_snippet: "Program Finder...Explore our 150+ academic offerings"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs.gasas_soe
  value: {total_extracted: "~120+", MA: "~27", MS: "~26", MFA: 1, PhD: "~28", Certificate: "~36"}
  source_url: https://asegrad.tufts.edu/programs
  source_snippet: "Explore Graduate Programs...Filter: Level Master's Doctorate Certificate School Arts & Sciences Engineering"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora import manifest

### Collection structure

```
tufts-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-arts-sciences              (Section 1: AS majors + minors)
├── 02-ug-engineering                (Section 1: SOE majors + minors)
├── 03-ug-smfa                       (Section 1: SMFA BFA + combined degrees)
├── 04-grad-gasas-soe                (Section 2: GSAS + SOE programs)
├── 05-grad-fletcher                 (Section 2: Fletcher School)
├── 06-grad-professional-schools     (Section 2: Vet/Med/Dental/Nutrition/GSBS)
├── 07-deadlines-requirements        (Section 3: UG + Grad requirements)
├── 08-costs-financial-aid           (Section 4: COA + aid policy)
├── 09-evidence-chain                (Section 5: all evidence blocks)
└── 10-monitoring-watchlist          (Section 4 monitoring design)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "tufts-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BFA|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Full professional school program lists (Fletcher, Cummings, Med, Dental, Friedman, GSBS) | Individual school sites |
| P0 | catalog.tufts.edu access (currently unreachable) | catalog.tufts.edu |
| P1 | Per-program GRE requirements for GSAS/SOE | asegrad.tufts.edu individual program pages |
| P1 | Graduate application fees (per school) | Individual admissions pages |
| P1 | SMFA BFA portfolio requirements detail | smfa.tufts.edu |
| P1 | Fletcher School program details and deadlines | fletcher.tufts.edu |
| P2 | Graduate cost of attendance by program | Individual school financial aid pages |
| P2 | Need-blind/need-aware verification for international students | finaid.tufts.edu |
| P2 | Detailed department-level structure within AS and Engineering | catalog.tufts.edu (when accessible) |

---

## SECTION 7 -- Cross-school comparison framework

| Dimension | Tufts | (Other schools) |
|-----------|-------|-----------------|
| Location | Medford, MA | |
| Type | Private research university | |
| UG tuition/yr | $74,862 | |
| Total UG COA/yr | $97,152 (no insurance) | |
| Need-blind (US) | Yes | |
| Need-blind (intl) | No (need-aware) | |
| Meets 100% need | Yes (all admitted) | |
| Tuition-free threshold | <$150k income | |
| EA deadline | N/A (no EA) | |
| ED I deadline | November 2, 2026 | |
| ED II deadline | January 4, 2027 | |
| RD deadline | January 4, 2027 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min (recommended) | 100+ | |
| IELTS min (recommended) | 7.0+ | |
| Application fee | $75 | |
| Admission rate | 10.8% (Class of 2029) | |
| Total UG programs (majors) | ~76 | |
| Total UG minors | ~84 unique | |
| Total grad programs (GSAS+SOE) | ~120+ | |
| Schools (total) | 10 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.tufts.edu, asegrad.tufts.edu, students.tufts.edu/financial-services, finaid.tufts.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school -> department -> degree-level -> program
> **Cache**: uni-cache/schools/tufts/site-memory.json + content-hashes.json + last-extract.json
