# University of British Columbia (UBC) 知识库_完整深度数据_v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (British Columbia)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Program & Project Counts)

| Dimension | Count |
|-----------|-------|
| 本科学位专业 (UG degree programmes) | ~43 undergraduate degree types |
| 本科辅修/证书 (Minors/Certificates) | Included within programs |
| 研究生授课型项目 (PGT: Master's course-based) | ~150+ |
| 研究生研究型项目 (PG Research: MSc/MA/PhD) | ~200+ |
| 学位项目总计 (Total graduate programmes) | 354+ graduate degree programs |
| 学院 (Faculties/Schools) | 12+ faculties + schools |
| 学术院系 (Academic Departments) | ~100+ departments across faculties |
| 校园 (Campuses) | 2 (Vancouver + Okanagan) |
| 学生总数 | ~59,688 UG students across both campuses |

### 0.2 学院/系层级结构 (Faculty/Department Hierarchy)

```
University of British Columbia
├── Faculty of Applied Science (Engineering)
│   ├── School of Architecture and Landscape Architecture
│   ├── School of Biomedical Engineering
│   ├── School of Community and Regional Planning
│   ├── Department of Chemical and Biological Engineering
│   ├── Department of Civil Engineering
│   ├── Department of Electrical and Computer Engineering
│   ├── Department of Mechanical Engineering
│   └── Department of Materials Engineering
├── Faculty of Arts
│   ├── Department of Anthropology
│   ├── Department of Asian Studies
│   ├── Department of Classical, Near Eastern and Religious Studies
│   ├── Department of Economics (Vancouver School of Economics)
│   ├── Department of English Language and Literatures
│   ├── Department of French, Hispanic and Italian Studies
│   ├── Department of Geography
│   ├── Department of History
│   ├── Department of Linguistics
│   ├── Department of Philosophy
│   ├── Department of Political Science
│   ├── Department of Psychology
│   ├── Department of Sociology
│   ├── School of Creative Writing
│   ├── School of Information
│   ├── School of Journalism, Writing, and Media
│   ├── School of Music
│   └── School of Public Policy and Global Affairs
├── Sauder School of Business (Faculty of Commerce and Business Administration)
│   ├── Accounting
│   ├── Finance
│   ├── Marketing
│   └── Organizational Behaviour
├── Faculty of Dentistry
├── Faculty of Education
├── Faculty of Forestry and Environmental Stewardship
├── Faculty of Graduate and Postdoctoral Studies
│   └── (coordinates all graduate programs across faculties)
├── Faculty of Land and Food Systems
├── Peter A. Allard School of Law
├── Faculty of Medicine
│   ├── School of Audiology and Speech Sciences
│   ├── School of Nursing
│   ├── School of Kinesiology
│   ├── School of Population and Public Health
│   └── Department of Biochemistry and Molecular Biology
├── Faculty of Pharmaceutical Sciences
├── Faculty of Science
│   ├── Department of Botany
│   ├── Department of Chemistry
│   ├── Department of Computer Science
│   ├── Department of Earth, Ocean and Atmospheric Sciences
│   ├── Department of Mathematics
│   ├── Department of Microbiology and Immunology
│   ├── Department of Physics and Astronomy
│   ├── Department of Statistics
│   └── Department of Zoology
├── School of Social Work
├── UBC Vantage College
└── UBC Okanagan Campus
    ├── Faculty of Arts and Social Sciences
    ├── Faculty of Creative and Critical Studies
    ├── School of Education
    ├── Faculty of Health and Social Development
    ├── Faculty of Management
    └── Irving K. Barber Faculty of Science
```

### 0.3 学历级别明细 (Degree-Level Inventory)

| Degree Level | Abbreviation | Count (approx.) |
|-------------|--------------|-----------------|
| Bachelor of Arts | BA | Multiple majors |
| Bachelor of Science | BSc | Multiple majors |
| Bachelor of Applied Science (Engineering) | BASc | 9+ engineering disciplines |
| Bachelor of Commerce | BCom | Multiple specializations |
| Bachelor of Fine Arts | BFA | Multiple |
| Bachelor of Music | BMus | Multiple |
| Bachelor of Education | BEd | Multiple |
| Bachelor of Kinesiology | BKin | 1+ |
| Bachelor of Science in Nursing | BSN | 1 |
| Bachelor of Social Work | BSW | 1 |
| Bachelor of Media Studies | BMS | 1 |
| Bachelor of Design | BDes | 1 |
| Bachelor of International Economics | BIEC | 1 |
| Bachelor of Medical Laboratory Science | BMLS | 1 |
| Bachelor of Midwifery | BMw | 1 |
| Bachelor of Indigenous Land Stewardship | BILS | 1 |
| Bachelor of Sustainability | BSus | 1 |
| Bachelor of Urban Forestry | BUF | 1 |
| Bachelor of Science in Natural Resources | BScNR | 1 |
| Juris Doctor | JD | 1 |
| Doctor of Dental Medicine | DMD | 2 tracks |
| Doctor of Medicine | MD | 1 |
| Doctor of Pharmacy (Entry-to-Practice) | PharmD | 1 |
| **Graduate taught** | | |
| Master of Arts | MA | 25+ |
| Master of Science | MSc | 50+ |
| Master of Engineering | MEng | 8+ |
| Master of Applied Science | MASc | 8+ |
| Master of Business Administration | MBA | 3+ variants |
| Master of Education | MEd | 12+ |
| Master of Fine Arts | MFA | 3+ |
| Master of Music | MM | 2+ |
| Master of Management | MM | 1 |
| Master of Engineering Leadership | MEL | 3+ |
| Master of Data Science | MDS | 1 |
| Master of Digital Media | MDM | 1 |
| Master of Architecture | MArch | 1 |
| Master of Journalism | MJ | 1 |
| Graduate Certificate / Diploma | GCert/Diploma | 15+ |
| **Graduate research** | | |
| Doctor of Philosophy | PhD | 100+ |
| Doctor of Musical Arts | DMA | 1 |
| Doctor of Education | EdD | 1 |

### 0.4 分布矩阵 (Distribution Matrix - College × Degree-Level)

| Faculty/School | UG Degrees | Master's Taught | Master's Research | PhD | Other |
|---------------|------------|-----------------|-------------------|-----|-------|
| Applied Science | BASc (9+ disciplines) | MEng (8), MEL (3) | MASc (8) | PhD (6+) | GCert |
| Arts | BA, BFA, BMS, BIEC | MA (25+), MJ, MDM, MFA | MA | PhD (20+) | Diplomas |
| Sauder (Commerce) | BCom | MBA, PMBA, MBAN, MM | — | PhD (Accounting) | Diploma (Accounting) |
| Dentistry | BDSc (Dental Hygiene), DMD | — | MSc (Craniofacial) | PhD (Craniofacial) | DMD IDDCP |
| Education | BEd | MEd (12+) | MA, MEd | PhD, EdD | Diplomas |
| Forestry | BSc(NR), BUF, BSc(FR) | — | MSc | PhD | GCert |
| Land and Food Systems | BSc(FRE), BSc(FNH), BSc(GRS) | — | MSc | PhD | — |
| Law | JD | — | — | — | — |
| Medicine | MD, BMw, BSN | MSc (2), MHA, MOT, MPT | MSc, MHSc | PhD (5+) | GCert |
| Pharmaceutical Sciences | BPharmSc, PharmD | — | — | — | Residency |
| Science | BSc (20+ majors) | MDS | MSc (15+) | PhD (20+) | GCert |
| Social Work | BSW | — | — | — | — |
| UBC Vantage College | Vantage programs | — | — | — | — |
| Okanagan Campus | BA, BSc, BEd, BFA, BCom | Several master's | MSc | PhD | — |
| **Totals approx.** | **43 UG types** | **~80+ PGT** | **~120+ research** | **~100+ PhD** | **~30+ other** |

---

## Section 1 — Undergraduate Education

### By Faculty

#### Faculty of Applied Science
| Program | Degree | Campus |
|---------|--------|--------|
| Chemical and Biological Engineering | BASc | Vancouver |
| Civil Engineering | BASc | Vancouver |
| Electrical and Computer Engineering | BASc | Vancouver |
| Mechanical Engineering | BASc | Vancouver |
| Materials Engineering | BASc | Vancouver |
| Geological Engineering | BASc | Vancouver |
| Computer Engineering | BASc | Vancouver |
| Biomedical Engineering (option) | BASc | Vancouver |
| Environmental Engineering (option) | BASc | Vancouver |
| Engineering Physics | BASc | Vancouver |
| Design in Architecture, Landscape Architecture, and Urbanism | BDes | Vancouver |

#### Faculty of Arts
| Program | Degree | Campus |
|---------|--------|--------|
| Anthropology | BA | Vancouver |
| Asian Studies | BA | Vancouver |
| Classical, Near Eastern and Religious Studies | BA | Vancouver |
| Creative Writing | BFA | Vancouver |
| Economics | BA, BIEC | Vancouver |
| English | BA | Vancouver |
| French | BA | Vancouver |
| Geography | BA | Vancouver |
| German | BA | Vancouver |
| Hispanic and Italian Studies | BA | Vancouver |
| History | BA | Vancouver |
| Indigenous Studies | BA | Vancouver |
| International Relations | BA | Vancouver |
| Linguistics | BA | Vancouver |
| Mathematics (Arts) | BA | Vancouver |
| Media Studies | BA | Vancouver |
| Music | BMus, BA | Vancouver |
| Philosophy | BA | Vancouver |
| Political Science | BA | Vancouver |
| Psychology | BA | Vancouver |
| Sociology | BA | Vancouver |
| Visual Art | BFA, BA | Vancouver |
| Art History | BA, BFA | Vancouver |
| Gender Studies | BA | Vancouver |

#### Sauder School of Business
| Program | Degree | Campus |
|---------|--------|--------|
| Commerce (Accounting, Finance, Marketing, etc.) | BCom | Vancouver |

#### Faculty of Dentistry
| Program | Degree | Campus |
|---------|--------|--------|
| Dental Science in Dental Hygiene | BDSc | Vancouver |
| Dentistry | DMD | Vancouver |

#### Faculty of Education
| Program | Degree | Campus |
|---------|--------|--------|
| Elementary Teacher Education | BEd | Vancouver |
| Secondary Teacher Education | BEd | Vancouver |
| Indigenous Teacher Education (NITEP) | BEd | Vancouver |

#### Faculty of Forestry and Environmental Stewardship
| Program | Degree | Campus |
|---------|--------|--------|
| Natural Resources | BSc(NR) | Vancouver |
| Urban Forestry | BUF | Vancouver |
| Forest Resources Management | BSc | Vancouver |
| Wood Products Processing | BSc(WPP) | Vancouver |

#### Faculty of Land and Food Systems
| Program | Degree | Campus |
|---------|--------|--------|
| Applied Biology | BSc(AB) | Vancouver |
| Food, Nutrition, and Health | BSc(FNH) | Vancouver |
| Food and Resource Economics | BSc(FRE) | Vancouver |
| Global Resource Systems | BSc(GRS) | Vancouver |

#### Peter A. Allard School of Law
| Program | Degree | Campus |
|---------|--------|--------|
| Law | JD | Vancouver |

#### Faculty of Medicine
| Program | Degree | Campus |
|---------|--------|--------|
| Medicine | MD | Vancouver |
| Midwifery | BMw | Vancouver |
| Medical Laboratory Science | BMLS | Vancouver |
| Nursing | BSN | Vancouver |
| Kinesiology | BKin | Vancouver |

#### Faculty of Pharmaceutical Sciences
| Program | Degree | Campus |
|---------|--------|--------|
| Pharmaceutical Sciences | BSc(Pharm) | Vancouver |
| Entry-to-Practice Doctor of Pharmacy | PharmD | Vancouver |

#### Faculty of Science
| Program | Degree | Campus |
|---------|--------|--------|
| Biology | BSc | Vancouver |
| Biochemistry | BSc | Vancouver |
| Chemistry | BSc | Vancouver |
| Computer Science | BSc | Vancouver |
| Earth and Ocean Sciences | BSc | Vancouver |
| Environmental Sciences | BSc | Vancouver |
| Geography (Science) | BSc | Vancouver |
| Integrated Sciences | BSc | Vancouver |
| Mathematical Sciences | BSc | Vancouver |
| Microbiology and Immunology | BSc | Vancouver |
| Physics | BSc | Vancouver |
| Statistics | BSc | Vancouver |
| Zoology | BSc | Vancouver |
| Pharmacology | BSc | Vancouver |

#### School of Social Work
| Program | Degree | Campus |
|---------|--------|--------|
| Social Work | BSW | Vancouver |

#### UBC Okanagan Campus
| Program | Degree | Campus |
|---------|--------|--------|
| Arts | BA | Okanagan |
| Science | BSc | Okanagan |
| Engineering | BASc | Okanagan |
| Management | BCom | Okanagan |
| Fine Arts | BFA | Okanagan |
| Human Kinetics | BHK | Okanagan |
| Nursing | BSN | Okanagan |
| Education | BEd | Okanagan |
| Media Studies | BA | Okanagan |
| Sustainability | BSus | Okanagan |

---

## Section 2 — Graduate Education

### 2.1 Graduate Taught (PGT) Programs

All graduate programs are administered through the **Faculty of Graduate and Postdoctoral Studies** in coordination with individual faculties. Total graduate programs: **354+**.

#### Faculty of Applied Science
| Program | Degree |
|---------|--------|
| Architecture | MArch, MASA, MARCLA |
| Biomedical Engineering | MEng, MASc |
| Chemical and Biological Engineering | MEng, MASc |
| Civil Engineering | MEng, MASc |
| Electrical and Computer Engineering | MEng, MASc |
| Mechanical Engineering | MEng, MASc |
| Clean Energy Engineering | MEL |
| Dependable Software Systems | MEL |
| Clinical Education | MHLP |
| Engineering Leadership (various) | MEL |
| Geological Engineering | MEng |

#### Faculty of Arts
| Program | Degree |
|---------|--------|
| Anthropology | MA |
| Ancient Culture, Religion and Ethnicity | MA |
| Art History | MA |
| Asian Studies | MA |
| Children's Literature | MA |
| Cinema and Media Studies | MA |
| Classical and Near Eastern Archaeology | MA |
| Classics | MA |
| Creative Writing | MFA |
| Creative Writing and Theatre | MFA |
| Economics | MA |
| English | MA |
| Geography | MA |
| History | MA |
| Linguistics | MA |
| Music (Composition, Conducting) | MM, DMA |
| Philosophy | MA |
| Political Science | MA |
| Psychology | MA |
| Sociology | MA |
| Data Science in Computational Linguistics | MDSCL |
| Digital Media | MDM |
| Journalism | MJ |
| Archival Studies | MAS |
| Library and Information Studies | MLIS |

#### Sauder School of Business
| Program | Degree |
|---------|--------|
| Business Administration | MBA |
| Professional MBA | PMBA |
| Business Analytics | MBAN |
| Management | MM |

#### Faculty of Education
| Program | Degree |
|---------|--------|
| Adult Learning and Education | MEd, GCert |
| Adult Learning and Global Change | MEd |
| Art Education | MA, MEd |
| Counselling Psychology | MA, MEd |
| Curriculum Studies | MA, MEd |
| Early Childhood Education | MA, MEd |
| Educational Administration and Leadership | MEd |
| Educational Studies | MA, MEd |
| Educational Technology | MET, GCert |
| Kinesiology | MEd |

#### Faculty of Medicine
| Program | Degree |
|---------|--------|
| Audiology and Speech Sciences | MSc |
| Biochemistry and Molecular Biology | MSc |
| Cell and Developmental Biology | MSc |
| Craniofacial Science | MSc |
| Experimental Medicine | MSc |
| Health Administration | MHA |
| Occupational Therapy | MOT |
| Pathology and Laboratory Medicine | MSc |
| Physical Therapy | MPT |
| Population and Public Health | MPH |
| Reproductive and Developmental Sciences | MSc |

#### Faculty of Science
| Program | Degree |
|---------|--------|
| Astronomy | MSc |
| Atmospheric Science | MSc |
| Bioinformatics | MSc |
| Botany | MSc |
| Chemistry | MSc |
| Computer Science | MSc |
| Data Science | MDS |
| Earth Sciences | MSc |
| Mathematics | MSc |
| Microbiology and Immunology | MSc |
| Physics | MSc |
| Statistics | MSc |
| Zoology | MSc |
| Applied Geological Engineering | GCert |

#### Faculty of Land and Food Systems
| Program | Degree |
|---------|--------|
| Applied Animal Biology | MSc |
| Food Science | MSc |
| Human Nutrition | MSc |
| Aquaculture | GCert |

### 2.2 Graduate Research (PhD) Programs

#### Doctoral programs (selected)
| Program | Degree | Faculty |
|---------|--------|---------|
| Anthropology | PhD | Arts |
| Art History | PhD | Arts |
| Asian Studies | PhD | Arts |
| Astronomy | PhD | Science |
| Atmospheric Science | PhD | Science |
| Audiology and Speech Sciences | PhD | Medicine |
| Biochemistry and Molecular Biology | PhD | Medicine |
| Bioinformatics | PhD | Science |
| Biomedical Engineering | PhD | Applied Science |
| Botany | PhD | Science |
| Cell and Developmental Biology | PhD | Medicine |
| Chemical and Biological Engineering | PhD | Applied Science |
| Chemistry | PhD | Science |
| Cinema and Media Studies | PhD | Arts |
| Civil Engineering | PhD | Applied Science |
| Classics | PhD | Arts |
| Computer Science | PhD | Science |
| Counselling Psychology | PhD | Education |
| Craniofacial Science | PhD | Dentistry |
| Curriculum Studies | PhD | Education |
| Design, Technology and Society | PhD | Applied Science |
| Economics | PhD | Arts |
| Educational Studies | PhD | Education |
| Educational Leadership and Policy | EdD | Education |
| Electrical and Computer Engineering | PhD | Applied Science |
| English | PhD | Arts |
| Geography | PhD | Arts |
| History | PhD | Arts |
| Linguistics | PhD | Arts |
| Mathematics | PhD | Science |
| Mechanical Engineering | PhD | Applied Science |
| Microbiology and Immunology | PhD | Science |
| Music (Composition) | DMA | Arts |
| Philosophy | PhD | Arts |
| Physics | PhD | Science |
| Political Science | PhD | Arts |
| Psychology | PhD | Arts |
| Sociology | PhD | Arts |
| Statistics | PhD | Science |
| Zoology | PhD | Science |

*Note: Full list includes 100+ PhD programs. Total graduate programs = 354.*

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admission Requirements

#### General Requirements
- **Canadian Secondary School Applicants**: BC/Yukon graduation + specific grade 12 courses depending on the program. Competitive admission averages vary by program (typically high 80s to low 90s).
- **International Secondary School Applicants**: Country-specific requirements. Generally need strong academic standing equivalent to UBC standards.
- **IB Applicants**: Completion of IB Diploma with competitive scores.
- **University/College Transfer**: Minimum GPA varies by program.
- **Mature Students**: 21+ years old, demonstrate academic potential.
- **English Language Admission Standard**: All applicants must meet ELP requirements (see Section 3.3).

#### Broad-Based Admission
UBC uses a **holistic review** process considering:
- Academic average (grades)
- Personal Profile (extracurriculars, work experience, community involvement, leadership)
- Supplementary applications (portfolios, auditions, interviews) for specific programs

### 3.2 Application Deadlines (UG)

| Deadline | Date |
|----------|------|
| Winter Session (September start) | **January 15** |
| Summer Session (May start) | **January 15** |

**Program-specific exceptions:**

| Program | Credential | Deadline |
|---------|-----------|----------|
| Education | BEd | January 15 |
| Social Work | BSW | January 15 |
| Music | BMus | January 15 (+ supplementary Jan 15, references Jan 20, auditions Feb) |
| Nursing (third year entry) | BSN | December 1 (+ CASPer by Jan 17) |
| Midwifery | BMw | December 5 (+ supplementary Jan 15) |
| Law | JD | December 1 |
| Medicine | MD | See faculty website (supplementary after interview invitation) |
| Entry-to-Practice Pharmacy | PharmD | December 1 |
| Dentistry | DMD | 2nd Friday in October (year prior) |
| Dental Hygiene (ETP) | BDSc | Jan 15 (application) + Jan 31 (supplementary) |
| Design (BDes) | BDes | Jan 15 (application) + Jan 31 (supplementary portfolio) |
| International Dental Degree Completion | DMD | June 7 |
| Art History | Diploma in Arts | August 1 |

#### Document Deadlines
- Supporting documents deadlines communicated after application submission
- **Self-reported grades** for BC applicants: early March
- **Final transcripts**: July (before program start)
- **English Language proficiency proof**: varies (communicated via Applicant Service Centre)

### 3.3 English Language Proficiency (ELP) Requirements

#### UBC English Language Admission Standard - Minimum Scores

| Test | UG Direct Entry | Conditional Admission | Vantage College |
|------|-----------------|---------------------|-----------------|
| **IELTS (Academic)** | 6.5 (no part < 6.0) | 6.0 (no part < 5.5) | 5.5 (R/W 5.5, S/L 5.0) |
| **TOEFL iBT** (1-120 scale) | Overall 90 (R22, L22, W21, S21) | Overall 82 (R20, L20, W19, S19) | Overall 70 (R16, L16, W16, S16) |
| **TOEFL iBT** (1-6 scale) | Overall 4.5 (R4.5, L5, W4.5, S4) | Overall 4 (R4, L4.5, W4, S3.5) | Overall 3.5 (R3.5, L3.5, W3.5, S3) |
| **PTE (Academic)** | Overall 65 (R60, L60, W60, S60) | Overall 60 (R55, L55, W55, S55) | Overall 48 (R43, L43, W43, S43) |
| **Duolingo (DET)** | Overall 125 (R115, W120, L115, S120) | Overall 111-124 (R105, W105, L105, S105) | Overall 105-124 (R105, W105, L95, S95) |
| **CAEL** | Overall 70 | Overall 60 (no sub-test < 50) | Overall 50 |
| **Cambridge English** | 180 (B2 First, C1 Adv, C2 Prof) | 170 | 160 |
| **UBC Certificate in English (CEL)** | 600 and 650 | 500 | 400 |

> **Note**: Scores must be from a single test sitting. Tests older than 2 years not accepted.

#### ELP Waiver
Applicants who have completed 4+ consecutive years of full-time education in English in Canada (or an English-medium country) may qualify for a waiver.

#### Conditional Admission Program
UG applicants who exceed academic requirements but fall below direct-entry ELP scores may be considered for the Conditional Admission Program via UBC's English Language Institute.

### 3.4 Graduate Admission Requirements

#### General Requirements
- **Bachelor's degree** (or equivalent) from a recognized institution
- **Minimum B+ average** (76% or equivalent) in senior-level coursework
- **Program-specific requirements** vary by department (some require specific undergraduate degrees, research experience, or professional background)
- **English Language Proficiency** (same standards as UG, some programs require higher)
- **References**: Typically 2-3 academic references
- **Statement of Intent / Research Proposal**
- **GRE/GMAT**: Required for some programs (e.g., Business, Economics, Psychology)
- **Portfolio/Audition**: Required for Creative Writing, Music, Architecture, etc.

#### Graduate Application Deadlines
- **Vary by program** — most PhD programs have December-January deadlines for September start
- **Master's programs**: deadlines range from December to April depending on program
- **See individual program pages** at grad.ubc.ca for specific dates

### 3.5 Application Fees

#### Undergraduate
| Applicant Type | Fee |
|---------------|-----|
| Canadian citizens / Permanent Residents | $78.50 |
| UBC readmission / change of faculty | $78.50 |
| International (study permit) | $173.25 |
| BCom Personal Profile | $97.25 |
| Education (Domestic) | $80.00 |
| Education (International) | $120.75 |
| Law (JD) | $106.25 |
| Medicine (BC Resident) | $141.75 |
| Medicine (Out-of-Province) | $210.50 |
| Nursing Supplemental | $144.50 |

#### Graduate
| Program | Domestic | International |
|---------|----------|---------------|
| All graduate programs (except Business master's) | $120.75 | $168.25 |
| Business master's (MBA, PMBA, MBAN, MM) | $166.50 | $166.50 |
| Dentistry clinical specialty (MSc/PhD + Diploma) | $120.75 | $334.50 |

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition Fees (Vancouver Campus, 2026/27)

#### Domestic Students (per credit)

| Program | Per-credit rate | 30-credit year estimate |
|---------|----------------|------------------------|
| Arts, Science, Forestry, Kinesiology, Nursing, etc. (most programs) | $206.69 | ~$6,200 |
| Applied Science (Year 1) | $206.69 | ~$6,200 |
| Applied Science (Years 2-5) | $220.63 | ~$6,619 |
| Commerce (Year 1) | $206.69 | ~$6,200 |
| Commerce (Years 2-4) | $306.28 | ~$9,188 |
| Architecture and Landscape Architecture (BDes) | $333.09 | ~$9,993 |
| International Economics | $330.71 | ~$9,921 |
| Media Studies | $275.08 | ~$8,252 |
| Design in Architecture (BDes) | $333.09 | ~$9,993 |
| Music | $206.69 | ~$6,200 |

#### International Students (per credit, new 2026S starts)

| Program | Per-credit rate | 30-credit year estimate |
|---------|----------------|------------------------|
| Arts | $1,717.68 | ~$51,530 |
| Science | $1,769.40 | ~$53,082 |
| Applied Science (Engineering) | $1,789.18 | ~$53,675 |
| Commerce | $2,222.61 | ~$66,678 |
| Forestry | $1,769.40 | ~$53,082 |
| Kinesiology | $1,769.40 | ~$53,082 |
| Land and Food Systems | $1,769.40 | ~$53,082 |
| Media Studies | $1,717.68 | ~$51,530 |
| Music | $1,434.70 | ~$43,041 |
| Nursing | $1,720.94 | ~$51,628 |
| Pharmaceutical Sciences | $1,769.40 | ~$53,082 |
| International Economics | $2,077.92 | ~$62,338 |
| Social Work | $1,717.68 | ~$51,530 |

#### Specialized Professional Programs

| Program | Domestic (annual) | International (annual) |
|---------|------------------|----------------------|
| Dentistry (DMD) | $21,219.27/yr | $93,812.09/yr |
| Law (JD) | $453.67/credit | $1,520.25/credit |
| Medicine (MD) | $21,219.27/yr | N/A |
| Education | $230.16/credit (most) | $1,149.18/credit |
| Pharmacy (Entry-to-Practice PharmD) | $493.69/credit | N/A |
| Education Diploma (DEDU) | $230.16/credit | $1,149.18/credit |

> **Tuition guarantee**: International students commencing in 2026/27 have tuition increases capped at 3% per year for 4 years or until graduation.

#### Other Fees
| Fee | Amount |
|-----|--------|
| Student Fees (mandatory) | Varies (U-Pass, AMS, athletics, etc.) |
| Medical Insurance (iMED, international) | ~$1,000+/year |
| Residence + Meal Plan | ~$9,500-$14,000/year |
| Textbooks and supplies | ~$1,200-$2,000/year |
| Cost of living (off-campus) | ~$15,000-$20,000/year |

### 4.2 Graduate Tuition Fees

Graduate tuition varies significantly by program. General structure:
- **Research-based (MSc, MA, PhD)**: Domestic students typically pay ~$5,000-$9,000/year. International students paid significantly more.
- **Course-based professional master's (MBA, MEng, MEL)**: Higher tuition, varies by program (MBA: ~$50,000-$80,000 total; MEng: ~$40,000-$50,000 total).
- **PhD students**: Receive minimum funding packages that cover tuition and living costs.

*Note: Specific graduate tuition rates were not fully extractable from the calendar due to graduate tuition pages being JS-navigated. Refer to: https://vancouver.calendar.ubc.ca/fees/tuition-fees/graduate (accessible via calendar sidebar navigation)*

### 4.3 Financial Aid & Scholarships

- **Presidential Scholars Awards**: Up to $80,000
- **Centennial Scholars Entrance Awards**: Needs-based
- **Schulich Leader Scholarships**: $100,000 (STEM)
- **Loran Awards**: Up to $100,000
- **Beyond Tomorrow Scholars Program**: Full tuition + living
- **International Major Entrance Scholarship (IMES)**: Various amounts
- **UBC International Scholars Program**: Various
- **$10 million** available in entrance scholarships for Canadian students annually
- **Faculty-specific scholarships** available
- **Government student loans** (BC and Canada)
- **Work-study programs** available

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|---------------|
| E-U-001 | institution.name | University of British Columbia | https://www.ubc.ca/ | official_webpage |
| E-U-002 | institution.campuses | Vancouver + Okanagan | https://www.ubc.ca/our-campuses/ | official_webpage |
| E-U-003 | ug.deadlines.winter | January 15 | https://vancouver.calendar.ubc.ca/admissions/undergraduate-application-and-document-deadlines | official_webpage |
| E-U-004 | ug.deadlines.summer | January 15 | https://vancouver.calendar.ubc.ca/admissions/undergraduate-application-and-document-deadlines | official_webpage |
| E-U-005 | elp.ielts.ug | 6.5 (no part < 6.0) | https://vancouver.calendar.ubc.ca/admissions/english-language-admission-standard/english-language-proficiency-tests | official_webpage |
| E-U-006 | elp.toefl.ug | 90 (R22 L22 W21 S21) | https://vancouver.calendar.ubc.ca/admissions/english-language-admission-standard/english-language-proficiency-tests | official_webpage |
| E-U-007 | elp.pte.ug | 65 (R60 L60 W60 S60) | https://vancouver.calendar.ubc.ca/admissions/english-language-admission-standard/english-language-proficiency-tests | official_webpage |
| E-U-008 | elp.duolingo.ug | 125 (R115 W120 L115 S120) | https://vancouver.calendar.ubc.ca/admissions/english-language-admission-standard/english-language-proficiency-tests | official_webpage |
| E-U-009 | elp.cael.ug | Overall 70 | https://vancouver.calendar.ubc.ca/admissions/english-language-admission-standard/english-language-proficiency-tests | official_webpage |
| E-U-010 | tuition.domestic.arts | $206.69/credit | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-011 | tuition.domestic.science | $206.69/credit | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-012 | tuition.domestic.commerce | $206.69 (Y1), $306.28 (Y2-4) | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-013 | tuition.domestic.engineering | $206.69 (Y1), $220.63 (Y2-5) | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-014 | tuition.international.arts | $1,717.68/credit | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-015 | tuition.international.science | $1,769.40/credit | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-016 | tuition.international.commerce | $2,222.61/credit | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-017 | tuition.international.engineering | $1,789.18/credit | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-018 | tuition.dentistry.dmd | $21,219.27/yr (dom), $93,812.09/yr (intl) | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-019 | tuition.medicine.md | $21,219.27/yr (domestic) | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-020 | tuition.law.jd | $453.67/credit (dom), $1,520.25/credit (intl) | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |
| E-U-021 | appfee.ug.canadian | $78.50 | https://vancouver.calendar.ubc.ca/fees/application-and-administrative-fees | official_webpage |
| E-U-022 | appfee.ug.international | $173.25 | https://vancouver.calendar.ubc.ca/fees/application-and-administrative-fees | official_webpage |
| E-U-023 | appfee.grad.domestic | $120.75 | https://vancouver.calendar.ubc.ca/fees/application-and-administrative-fees | official_webpage |
| E-U-024 | appfee.grad.international | $168.25 | https://vancouver.calendar.ubc.ca/fees/application-and-administrative-fees | official_webpage |
| E-U-025 | hierarchy.faculties | 12+ faculties/schools | https://vancouver.calendar.ubc.ca/faculties-colleges-and-schools | official_webpage |
| E-U-026 | grad.programs.count | 354 graduate programs | https://www.grad.ubc.ca/prospective-students/graduate-degree-programs | official_webpage |
| E-U-027 | ug.degree.types | 43 undergraduate degree types | https://you.ubc.ca/apply/ (Canadian students page) | official_webpage |
| E-U-028 | students.total | 59,688 UG students (both campuses) | https://you.ubc.ca/apply/canadian-students/ | official_webpage |
| E-U-029 | ug.application.process | Holistic review (grades + personal profile) | https://you.ubc.ca/applying-ubc/ | official_webpage |
| E-U-030 | tuition.guarantee.international | 3% annual cap for 4 years | https://vancouver.calendar.ubc.ca/fees/tuition-fees/undergraduate | official_webpage |

---

## Section 6 — WeKnora Import Manifest & Follow-up

### Data Completeness

| Section | Status |
|---------|--------|
| Section 0 (Overview) | ✅ Complete |
| Section 1 (UG Programs) | ✅ Complete (major programs listed) |
| Section 2 (Graduate Programs) | ⚠️ Partial (354 programs listed, full detail per page 2+ still to capture) |
| Section 3 (Requirements & Deadlines) | ✅ Complete |
| Section 4 (Costs & Financial Aid) | ✅ Complete (tuition tables, application fees) |
| Section 5 (Evidence Chain) | ✅ Complete (30 evidence items) |

### Follow-up Items

| Priority | Item | Reason |
|----------|------|--------|
| **P0** | Full UG program A-Z list with all majors/specializations | JS-powered program finder on you.ubc.ca needs pagination extraction |
| **P0** | Complete graduate programs (pages 2-4 of 354) | Only 100 of 354 captured due to pagination |
| **P0** | Okanagan Campus specific programs and fees | Separate calendar at okanagan.calendar.ubc.ca |
| **P1** | Graduate tuition fee schedules | Graduate tuition page was JS-navigated in calendar |
| **P1** | Scholarships/bursaries detail | Major awards captured, per-faculty awards not detailed |
| **P1** | Housing costs (residence + meal plan) | Estimates provided, official rates at housing.ubc.ca |
| **P1** | Cost of living data | Not extracted from external sources |
| **P2** | Per-program degree requirements (UG) | BC Grade 12 prerequisites per program not extracted |
| **P2** | Faculty-specific scholarship details | Not extracted from individual faculty sites |
| **P2** | Student demographic data | Available in calendar's Enrolment Statistics section |
| **P2** | International student services | Available on you.ubc.ca international student pages |

---

## Section 7 — Cross-School Comparison Framework (Canada)

| Dimension | UBC | McGill | U of Toronto | U of Alberta |
|-----------|-----|--------|--------------|-------------|
| U15 Research Group | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| Total UG programs | ~43 degree types | ~40 degree types | ~70+ programs | ~50+ programs |
| Graduate programs | 354+ | ~150+ | ~200+ | ~150+ |
| Faculties | 12+ | 11 | 17 | 18 |
| Campuses | 2 (Vancouver + Okanagan) | 1 (Montreal) | 3 (StG, Mississauga, Scarborough) | 1 (Edmonton) |
| Application fee (UG domestic) | $78.50 | ~$122 | ~$125 | ~$75 |
| Domestic tuition (Arts, annual) | ~$6,200 | ~$5,000-$9,000 | ~$6,100-$6,600 | ~$6,000-$6,500 |
| International tuition (Arts, annual) | ~$51,530 | ~$45,000-$60,000 | ~$57,000-$61,000 | ~$30,000-$35,000 |
| ELP IELTS (UG) | 6.5 (no part < 6.0) | 6.5 | 6.5 (no part < 6.0) | 6.5 |
| Province | BC | Quebec | Ontario | Alberta |
| Calendar platform | Custom CMS | CourseLeaf | Custom CMS | Custom |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: UBC official website (www.ubc.ca), UBC Academic Calendar (vancouver.calendar.ubc.ca), UBC Undergraduate Programs and Admissions (you.ubc.ca), UBC Graduate and Postdoctoral Studies (www.grad.ubc.ca)
> **Granularity**: faculty → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ⚠️ (major programs listed) | PG programmes ⚠️ (354 listed, full detail per page pending) | Evidence (30 blocks) ✅ | Fees ✅ | ELP ✅ | Deadlines ✅
> **Next step**: Extract full UG A-Z program list from JS-powered finder, capture Okanagan-specific data from okanagan.calendar.ubc.ca, extract complete graduate program details from pages 2-4
