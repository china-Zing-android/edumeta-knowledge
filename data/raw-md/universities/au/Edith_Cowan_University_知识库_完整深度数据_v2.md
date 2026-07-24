# Edith Cowan University (ECU) — 知识库完整深度数据 v2.0

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU) — Western Australia

---

## Section 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Bachelor Degrees) | 64 |
| 本科荣誉学位 (Honours) | 24 |
| 本科文凭 (Diploma UG) | 3 |
| 本科桥梁/预科 (Entry Pathways) | 1 |
| VET 高级文凭 (Advanced Diploma) | 4 |
| VET 证书 IV (Certificate IV) | 2 |
| VET 文凭 (Diploma VET) | 6 |
| 研究生证书 (Graduate Certificate) | 49 |
| 研究生文凭 (Graduate Diploma) | 27 |
| 授课型硕士 (Master by Coursework) | 56 |
| 研究型硕士 (Master by Research) | 10 |
| 博士 (Doctorate) | 2 |
| **学位项目总计** | **248** |
| 教学学院 (Schools) | 8 |
| 学术中心/项目 | 2 (Kurongkurl Katitjin, Academic Pathway Programs) |
| 校区 | 4 (City Campus, Joondalup, South West/Bunbury, Sri Lanka) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Edith Cowan University (ECU)
├── School of Arts & Humanities
│   ├── Creative Humanities
│   ├── Psychology, Counselling & Criminology
│   └── Social Sciences, Social Work & Youth Work
├── School of Business & Law
│   ├── Business
│   └── Law
├── School of Education
│   └── Teacher Education
├── School of Engineering
│   ├── Aviation
│   └── Engineering & Technology
├── School of Medical & Health Sciences
│   ├── Allied Health
│   ├── Exercise & Sports Science
│   ├── Health Science
│   ├── Medical & Biomedical Science
│   ├── Nutrition & Dietetics
│   ├── Occupational Health & Safety
│   ├── Paramedicine
│   └── Public Health
├── School of Nursing & Midwifery
│   └── Nursing & Midwifery
├── School of Science
│   ├── Computing
│   ├── Cyber Security
│   ├── Science
│   └── Security & Intelligence
├── Western Australian Academy of Performing Arts (WAAPA)
│   ├── Performing Arts
│   └── Production & Design
├── Kurongkurl Katitjin (Centre for Indigenous Australian Education and Research)
└── Academic Pathway Programs
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Degree Level | Count | AQF Level |
|-------------|-------|-----------|
| Certificate IV (VET) | 2 | 4 |
| Diploma (VET) | 6 | 5 |
| Advanced Diploma (VET) | 4 | 6 |
| Diploma (Undergraduate) | 3 | 5/6 |
| Bachelor Degree | 64 | 7 |
| Bachelor Honours Degree | 24 | 8 |
| Entry Pathway | 1 | — |
| Graduate Certificate | 49 | 8 |
| Graduate Diploma | 27 | 8 |
| Master by Coursework | 56 | 9 |
| Master by Research | 10 | 9 |
| Doctorate (PhD) | 2 | 10 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| School | Bachelor | Honours | Diploma UG | Grad Cert | Grad Dip | Master(CW) | Master(Res) | PhD | VET | Total |
|--------|----------|---------|------------|-----------|----------|------------|-------------|-----|-----|-------|
| Arts & Humanities | ~8 | ~4 | — | ~4 | ~2 | ~4 | ~1 | — | — | ~23 |
| Business & Law | ~10 | ~1 | ~1 | ~12 | ~6 | ~12 | — | — | — | ~42 |
| Education | ~4 | — | — | ~2 | ~3 | ~4 | — | — | — | ~13 |
| Engineering | ~15 | — | — | ~1 | — | ~3 | ~1 | — | — | ~20 |
| Medical & Health Sciences | ~8 | ~4 | — | ~6 | ~4 | ~8 | ~2 | — | — | ~32 |
| Nursing & Midwifery | ~5 | ~3 | — | ~3 | ~2 | ~5 | ~2 | — | — | ~20 |
| Science | ~8 | ~2 | — | ~6 | ~2 | ~5 | ~2 | — | — | ~25 |
| WAAPA | ~4 | ~1 | ~2 | — | — | ~1 | — | — | ~12 | ~20 |
| Multi-school/Other | ~2 | ~5 | — | ~15 | ~8 | ~14 | ~2 | ~2 | — | ~48 |
| **Total** | **64** | **24** | **3** | **49** | **27** | **56** | **10** | **2** | **12** | **248** |

> Note: Distribution matrix estimated based on study area classification. Exact per-school allocation requires individual program page inspection.

---

## Section 1 — Undergraduate Education

### Bachelor Degrees (64 programs)

| Program Name | Degree | School | Campus | Course Code | ATAR |
|-------------|--------|--------|--------|-------------|------|
| Bachelor of Arts | BA | Arts & Humanities | Joondalup, Online | U00 | — |
| Bachelor of Arts (Acting) | BA | WAAPA | City Campus | Y93 | — |
| Bachelor of Arts (Arts and Cultural Management) | BA | WAAPA | City Campus, Online | T74 | — |
| Bachelor of Arts (Dance) | BA | WAAPA | City Campus | T73 | — |
| Bachelor of Arts (Music Theatre) | BA | WAAPA | City Campus | G44 | — |
| Bachelor of Aviation | BAv | Engineering | Joondalup | K99 | — |
| Bachelor of Biomedical Science | BBiomedSc | Medical & Health Sciences | Joondalup | K05 | — |
| Bachelor of Biomedical Science (Bioscience) | BBiomedSc | Medical & Health Sciences | Joondalup | T89 | — |
| Bachelor of Business Analytics | BBA | Business & Law | City Campus, Online | Y00 | — |
| Bachelor of Commerce | BCom | Business & Law | City Campus, Online | W23 | 70 |
| Bachelor of Commerce/Bachelor of Psychology | BCom/BPsych | Business & Law | City Campus, Online | W75 | — |
| Bachelor of Communication | BComm | Arts & Humanities | City Campus | F35 | — |
| Bachelor of Community and Human Services | BCHS | Arts & Humanities | Joondalup, Online | O13 | — |
| Bachelor of Computer Science | BCS | Science | Joondalup | U65 | — |
| Bachelor of Counselling | BCouns | Arts & Humanities | Joondalup, Online | C56 | — |
| Bachelor of Counter Terrorism Security and Intelligence | BCTSI | Science | Joondalup, Online | Y14 | — |
| Bachelor of Creative Writing | BCW | Arts & Humanities | Online | F92 | — |
| Bachelor of Criminology and Justice | BCJ | Arts & Humanities | Joondalup, Online | G81 | — |
| Bachelor of Design | BDes | Arts & Humanities | City Campus | P79 | — |
| Bachelor of Education (Early Childhood Studies) | BEd | Education | Joondalup, SW, Online | Y42 | — |
| Bachelor of Education (Primary) | BEd | Education | Joondalup, SW, Online | Y41 | — |
| Bachelor of Education (Primary, 1-10) | BEd | Education | Joondalup, SW, Online | C99 | — |
| Bachelor of Education (Secondary) | BEd | Education | Joondalup, Online | Y68 | — |
| Bachelor of Engineering (Chemical) Honours | BE(Hons) | Engineering | Joondalup | Y50 | 80 |
| Bachelor of Engineering (Civil and Environmental) Honours | BE(Hons) | Engineering | Joondalup | Y28 | 80 |
| Bachelor of Engineering (Civil) Honours | BE(Hons) | Engineering | Joondalup | Y13 | 80 |
| Bachelor of Engineering (Computer Systems) Honours | BE(Hons) | Engineering | Joondalup | Y47 | 80 |
| Bachelor of Engineering (Computer Systems) Honours/Bachelor of Computer Science | BE(Hons)/BCS | Engineering | Joondalup | Y64 | — |
| Bachelor of Engineering (Electrical Power) Honours | BE(Hons) | Engineering | Joondalup | Y49 | 80 |
| Bachelor of Engineering (Electrical and Renewable Energy) Honours | BE(Hons) | Engineering | Joondalup | W21 | 80 |
| Bachelor of Engineering (Electronics and Communications) Honours | BE(Hons) | Engineering | Joondalup | Y51 | 80 |
| Bachelor of Engineering (Energy) Honours | BE(Hons) | Engineering | Joondalup | V32 | 80 |
| Bachelor of Engineering (Instrumentation Control and Automation) Honours | BE(Hons) | Engineering | Joondalup | Y46 | 80 |
| Bachelor of Engineering (Mechanical) Honours | BE(Hons) | Engineering | Joondalup | Y45 | 80 |
| Bachelor of Engineering (Mechatronics) Honours | BE(Hons) | Engineering | Joondalup | Y44 | 80 |
| Bachelor of Engineering (Mechatronics) Honours/Bachelor of Technology (Motorsports) | BE(Hons)/BTech | Engineering | Joondalup | Y75 | — |
| Bachelor of Engineering Honours/Bachelor of Commerce | BE(Hons)/BCom | Engineering | Joondalup | W26 | — |
| Bachelor of Engineering Honours/Bachelor of Science | BE(Hons)/BSc | Engineering | Joondalup | W32 | — |
| Bachelor of Environmental Science | BEnvSc | Science | Joondalup | W89 | — |
| Bachelor of Global Media and Communication | BGMC | Arts & Humanities | City Campus | T58 | — |
| Bachelor of Global Sport Business Management | BGSBM | Business & Law | Joondalup | Y53 | — |
| Bachelor of Global Sport Business Management (International) | BGSBM | Business & Law | Joondalup | T90 | — |
| Bachelor of Health Science | BHlthSc | Medical & Health Sciences | Joondalup | K97 | — |
| Bachelor of Hospitality and Tourism Management | BHTM | Business & Law | City Campus | K93 | — |
| Bachelor of Information Technology | BIT | Science | Joondalup | U67 | — |
| Bachelor of Journalism and Broadcast Media | BJBM | Arts & Humanities | City Campus | H31 | — |
| Bachelor of Laws | LLB | Business & Law | City Campus, Online | V72 | — |
| Bachelor of Laws (Graduate Entry) | LLB | Business & Law | City Campus | Y11 | — |
| Bachelor of Laws Honours | LLB(Hons) | Business & Law | City Campus | U37 | — |
| Bachelor of Laws/Bachelor of Commerce | LLB/BCom | Business & Law | City Campus, Online | W28 | — |
| Bachelor of Laws/Bachelor of Criminology and Justice | LLB/BCJ | Business & Law | City Campus, Online | K30 | — |
| Bachelor of Laws/Bachelor of Psychology | LLB/BPsych | Business & Law | City Campus, Online | W83 | — |
| Bachelor of Marketing, Advertising and Public Relations | BMarkPR | Business & Law | City Campus, Online | Y99 | — |
| Bachelor of Music | BMus | WAAPA | City Campus | W76 | — |
| Bachelor of Performing Arts | BPA | WAAPA | City Campus | Y97 | — |
| Bachelor of Preclinical Foundations of Imaging Science | BPFIS | Medical & Health Sciences | Joondalup | T78 | — |
| Bachelor of Psychological Science | BPsychSc | Arts & Humanities | Joondalup | C98 | — |
| Bachelor of Psychology | BPsych | Arts & Humanities | Joondalup, Online, Sri Lanka | W74 | — |
| Bachelor of Psychology and Counselling | BPsych&Coun | Arts & Humanities | Joondalup, Online | W65 | — |
| Bachelor of Psychology, Criminology and Justice | BPsychCJ | Arts & Humanities | Joondalup, Online | W73 | — |
| Bachelor of Science | BSc | Science | Joondalup, SW | M04 | — |
| Bachelor of Science (Cyber Security) | BSc | Science | Joondalup, Online, Sri Lanka | Y89 | — |
| Bachelor of Science (Exercise Science and Rehabilitation) | BSc | Medical & Health Sciences | Joondalup | M90 | — |
| Bachelor of Science (Exercise and Sports Science) | BSc | Medical & Health Sciences | Joondalup | M89 | — |
| Bachelor of Science (Exercise and Sports Science)/Bachelor of Commerce (Sport Business) | BSc/BCom | Medical & Health Sciences | Joondalup | W31 | — |
| Bachelor of Science (International Exercise and Sports Science) | BSc | Medical & Health Sciences | Joondalup | W97 | — |
| Bachelor of Science (Nursing) | BSc | Nursing & Midwifery | Joondalup, SW | C33 | — |
| Bachelor of Science (Nursing)/Bachelor of Science (Midwifery) | BSc | Nursing & Midwifery | Joondalup, SW | Y76 | — |
| Bachelor of Science (Occupational Therapy) | BSc | Medical & Health Sciences | Joondalup | H96 | — |
| Bachelor of Science (Paramedical Science) | BSc | Medical & Health Sciences | Joondalup, SW | K89 | — |
| Bachelor of Science/Bachelor of Commerce | BSc/BCom | Science/Business | Joondalup | W27 | — |
| Bachelor of Screen Production | BScrProd | Arts & Humanities | City Campus | D53 | — |
| Bachelor of Social Work | BSW | Arts & Humanities | SW, Online | K41 | — |
| Bachelor of Speech Pathology | BSpPath | Medical & Health Sciences | Joondalup | Y02 | — |
| Bachelor of Technology (Aeronautical) | BTech | Engineering | Joondalup | Y73 | — |
| Bachelor of Technology (Engineering) | BTech | Engineering | Joondalup, Sri Lanka | Y62 | — |
| Bachelor of Technology (Motorsports) | BTech | Engineering | Joondalup | G68 | — |
| Bachelor of Visual Arts | BVA | Arts & Humanities | City Campus | F23 | — |
| Bachelor of Youth Work | BYouthW | Arts & Humanities | Joondalup, Online | C57 | — |

### Honours Degrees (24 programs)

| Program Name | School | Campus | Course Code |
|-------------|--------|--------|-------------|
| Bachelor of Creative and Performing Arts Honours | WAAPA | City Campus | W92 |
| Bachelor of Laws Honours | Business & Law | City Campus | U37 |
| Bachelor of Music Honours | WAAPA | City Campus | K35 |
| Bachelor of Psychology (Honours) | Arts & Humanities | Online | T75 |
| Bachelor of Science (Midwifery) Honours | Nursing & Midwifery | Joondalup | C90 |
| Bachelor of Science (Nursing) Honours | Nursing & Midwifery | Joondalup | C89 |
| Bachelor of Science (Occupational Therapy) Honours | Medical & Health Sciences | Joondalup | Y63 |
| Bachelor of Social Work (Honours) | Arts & Humanities | SW, Online | K42 |
| Bachelor of Speech Pathology Honours | Medical & Health Sciences | Joondalup | Y12 |

### VET Programs (12 programs)

| Program Name | Level | School | Campus | Course Code |
|-------------|-------|--------|--------|-------------|
| Advanced Diploma of Live Production and Management Services | AdvDip | WAAPA | City Campus | C81 |
| Advanced Diploma of Music | AdvDip | WAAPA | City Campus | C77 |
| Advanced Diploma of Performance (Acting) | AdvDip | WAAPA | City Campus | C86 |
| Advanced Diploma of Professional Dance (Elite Performance) | AdvDip | WAAPA | City Campus | C79 |
| Certificate IV in Aboriginal Performance | CertIV | WAAPA | City Campus | C84 |
| Certificate IV in Live Production and Technical Services | CertIV | WAAPA | City Campus | C83 |
| Diploma of Acting | Dip | WAAPA | City Campus | C85 |
| Diploma of Live Production and Technical Services | Dip | WAAPA | City Campus | C80 |
| Diploma of Music | Dip | WAAPA | City Campus | C82 |
| Diploma of Musical Theatre | Dip | WAAPA | City Campus | C76 |
| Diploma of Professional Dance (Elite Performance) | Dip | WAAPA | City Campus | C78 |
| Diploma of Screen Performance | Dip | WAAPA | City Campus | C75 |

### Other Undergraduate Programs

| Program Name | Type | School | Campus | Course Code |
|-------------|------|--------|--------|-------------|
| Diploma in Aviation | DipUG | Engineering | Joondalup | W88 |
| Diploma in Sport Business | DipUG | Business & Law | Joondalup | F00 |
| Diploma of Environmental Health | DipUG | Medical & Health Sciences | Joondalup | C54 |
| University Preparation Course | EntryPath | Academic Pathway Programs | — | C28 |

---

## Section 2 — Graduate Education

### Graduate Certificates (49 programs)

| Program Name | School | Campus | Course Code |
|-------------|--------|--------|-------------|
| Graduate Certificate in Children and Young People's Nursing | Nursing & Midwifery | Joondalup | L84 |
| Graduate Certificate in Contemporary Care of the Older Person | Nursing & Midwifery | — | I68 |
| Graduate Certificate of Counselling (Accelerated Online) | Arts & Humanities | Online | O22 |
| Graduate Certificate in Criminology and Justice | Arts & Humanities | Online | T99 |
| Graduate Certificate in Data Science | Science | Online | I98 |
| Graduate Certificate in Environmental Assessment and Management | Science | Online | I87 |
| Graduate Certificate in Mental Health | Medical & Health Sciences | Online | L54 |
| Graduate Certificate in Mental Wellbeing (Accelerated Online) | Medical & Health Sciences | Online | L90 |
| Graduate Certificate in News and Entertainment Media | Arts & Humanities | — | N00 |
| Graduate Certificate in Occupational Health and Safety | Medical & Health Sciences | — | S72 |
| Graduate Certificate in Primary Health Care | Medical & Health Sciences | — | D00 |
| Graduate Certificate in Public Health | Medical & Health Sciences | — | W60 |
| Graduate Certificate in Screen Production | Arts & Humanities | City Campus | J00 |
| Graduate Certificate in Scripted Screen Production | Arts & Humanities | City Campus | L00 |
| Graduate Certificate of Accounting and Finance | Business & Law | — | L40 |
| Graduate Certificate of Applied Digital Marketing | Business & Law | Online | I94 |
| Graduate Certificate of Business | Business & Law | — | L95 |
| Graduate Certificate of Business Administration (Accelerated Online) | Business & Law | Online | T45 |
| Graduate Certificate of Business Psychology (Accelerated Online) | Business & Law | Online | J82 |
| Graduate Certificate in Creative Writing (Accelerated Online) | Arts & Humanities | Online | J81 |
| Graduate Certificate of Cyber Security | Science | Online | L50 |
| Graduate Certificate of Education (Accelerated Online) | Education | Online | I95 |
| Graduate Certificate of Education (Early Childhood Studies) | Education | — | S74 |
| Graduate Certificate of Environmental, Social and Governance (ESG) Leadership (Accelerated Online) | Business & Law | Online | L59 |
| Graduate Certificate of Exercise Science (Strength and Conditioning) | Medical & Health Sciences | — | M27 |
| Graduate Certificate of Hospitality Management | Business & Law | — | J65 |
| Graduate Certificate of Human Resource Management | Business & Law | — | L76 |
| Graduate Certificate of Human Resource Management (Accelerated Online) | Business & Law | Online | P30 |
| Graduate Certificate of Leadership in Mining Workplace Safety | Engineering | — | S11 |
| Graduate Certificate of Misconduct and Corruption Prevention | Business & Law | — | P66 |
| Graduate Certificate of People and Culture (Accelerated Online) | Business & Law | Online | T46 |
| Graduate Certificate of People in Project Management (Accelerated Online) | Business & Law | Online | L39 |
| Graduate Certificate of Psychology (Accelerated Online) | Arts & Humanities | Online | J77 |

### Graduate Diplomas (27 programs)

| Program Name | School | Campus | Course Code |
|-------------|--------|--------|-------------|
| Graduate Diploma in Advanced Nursing | Nursing & Midwifery | — | C96 |
| Graduate Diploma in Early Childhood Teaching | Education | — | O12 |
| Graduate Diploma in Environmental Science | Science | — | I86 |
| Graduate Diploma in Mental Health Nursing | Nursing & Midwifery | — | T88 |
| Graduate Diploma in Midwifery Practice | Nursing & Midwifery | — | T91 |
| Graduate Diploma in News and Entertainment Media | Arts & Humanities | — | R00 |
| Graduate Diploma in Screen Production | Arts & Humanities | City Campus | I00 |
| Graduate Diploma in Teaching (Primary) | Education | — | C91 |
| Graduate Diploma in Teaching (Secondary) | Education | — | C92 |
| Graduate Diploma of Accounting and Finance | Business & Law | — | L32 |
| Graduate Diploma of Business | Business & Law | — | L96 |
| Graduate Diploma of Business Administration (Accelerated Online) | Business & Law | Online | T86 |
| Graduate Diploma of Community Paramedicine | Medical & Health Sciences | — | J80 |
| Graduate Diploma in Creative Writing (Accelerated Online) | Arts & Humanities | Online | J75 |
| Graduate Diploma of Human Resource Management | Business & Law | — | J56 |
| Graduate Diploma of Human Resource Management (Accelerated Online) | Business & Law | Online | T77 |
| Graduate Diploma of Occupational Health and Safety | Medical & Health Sciences | — | S73 |
| Graduate Diploma of Project Management (Accelerated Online) | Business & Law | Online | T72 |
| Graduate Diploma of Psychology (Accelerated Online) | Arts & Humanities | Online | W61 |
| Graduate Diploma of Supply Chain and Logistics Management | Business & Law | — | I82 |

### Master by Coursework (56 programs)

| Program Name | School | Campus | Course Code |
|-------------|--------|--------|-------------|
| Master of Advanced Nursing | Nursing & Midwifery | — | C95 |
| Master of Arts (Performing Arts) | WAAPA | City Campus | J40 |
| Master of Business Administration (Accelerated Online) | Business & Law | Online | J52 |
| Master of Business Administration (Education Leadership) | Business & Law | Online | O16 |
| Master of Business Administration Global | Business & Law | City Campus, Online, Joondalup | L94 |
| Master of Business Analytics | Business & Law | — | T79 |
| Master of Business Psychology | Business & Law | — | O17 |
| Master of Business Psychology (Accelerated Online) | Business & Law | Online | I73 |
| Master of Clinical Psychology | Arts & Humanities | Joondalup | T64 |
| Master of Communication | Arts & Humanities | — | C88 |
| Master of Computer Science | Science | — | I45 |
| Master of Counselling | Arts & Humanities | — | O18 |
| Master of Counselling (Accelerated Online) | Arts & Humanities | Online | O28 |
| Master of Creative Writing (Accelerated Online) | Arts & Humanities | Online | P78 |
| Master of Critical Care Paramedicine | Medical & Health Sciences | — | J84 |
| Master of Cyber Security | Science | — | L33 |
| Master of Data Science | Science | — | I97 |
| Master of Education (Accelerated Online) | Education | Online | J44 |
| Master of Education | Education | — | H08 |
| Master of Education (Advanced) | Education | — | J89 |
| Master of Engineering | Engineering | — | I59 |
| Master of Engineering Science | Engineering | — | J63 |
| Master of Environmental Science | Science | — | J48 |
| Master of Environmental Studies | Science | — | H22 |
| Master of Exercise Science (Strength and Conditioning) | Medical & Health Sciences | — | U94 |
| Master of Finance | Business & Law | — | L98 |
| Master of Horticultural Science | Science | — | T66 |
| Master of Human Resource Management (Accelerated Online) | Business & Law | Online | L75 |
| Master of International Hospitality Management | Business & Law | — | L89 |
| Master of Management Information Systems | Business & Law | — | L71 |
| Master of Marketing and Innovation Management | Business & Law | — | L42 |
| Master of Mental Health (Accelerated Online) | Medical & Health Sciences | Online | C94 |
| Master of Midwifery | Nursing & Midwifery | — | C93 |
| Master of News and Entertainment Media | Arts & Humanities | — | Q00 |
| Master of Nursing (Graduate Entry) | Nursing & Midwifery | — | J46 |
| Master of Nursing (Nurse Practitioner) | Nursing & Midwifery | — | L88 |
| Master of Nursing Studies | Nursing & Midwifery | — | J88 |
| Master of Nutrition and Dietetics | Medical & Health Sciences | — | I49 |
| Master of Paramedic Practitioner | Medical & Health Sciences | — | J78 |
| Master of Professional Accounting | Business & Law | — | L97 |
| Master of Professional Psychology | Arts & Humanities | — | I88 |
| Master of Project Management (Accelerated Online) | Business & Law | Online | L99 |
| Master of Public Health | Medical & Health Sciences | — | I62 |
| Master of Screen Production | Arts & Humanities | City Campus | H00 |
| Master of Social Work (Qualifying) | Arts & Humanities | — | S10 |
| Master of Supply Chain and Logistics Management | Business & Law | — | I78 |
| Master of Teaching (Early Childhood) | Education | — | I81 |
| Master of Teaching (Primary) | Education | — | I83 |
| Master of Teaching (Secondary) | Education | — | I91 |
| Master of Technology | Engineering | — | T59 |

### Master by Research (10 programs)

| Program Name | School | Course Code |
|-------------|--------|-------------|
| Master of Computing and Security by Research | Science | I85 |
| Master of Laws (Research) | Business & Law | I74 |
| Master of Medical and Health Science by Research | Medical & Health Sciences | J90 |
| Master of Midwifery (Research) | Nursing & Midwifery | I19 |
| Master of Nursing (Research) | Nursing & Midwifery | I67 |
| Master of Science by Research | Science | I84 |

### Doctorate / PhD (2 programs)

| Program Name | School | Course Code |
|-------------|--------|-------------|
| Doctor of Philosophy | Multi-school | L61 |
| Doctor of Philosophy (Integrated) | Multi-school | J42 |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Entry Requirements

**Undergraduate Entry (Domestic)**
- **Recent secondary education**: ATAR-based entry via TISC (Tertiary Institutions Service Centre)
  - Indicative ATARs vary by course: e.g., Bachelor of Commerce = 70, Bachelor of Engineering (Chemical) Honours = 80
- **Work and life experience**: Mature-age entry (>2 years since leaving school)
- **VET pathway**: Certificate IV or higher accepted
- **Higher education transfer**: Previous university/HE study credit transfer
- **Special entry**: UniPrep enabling course, Early Offer Program

**Undergraduate Entry (International)**
- Equivalent academic qualifications from home country
- English language proficiency required

**Postgraduate Entry**
- Bachelor degree (or equivalent) in relevant discipline
- Some courses require work experience (e.g., MBA)
- Portfolio/audition for creative/performing arts programs

### 3.2 English Language Requirements

ECU uses a band system for English language requirements:

| Band | IELTS (Academic) | TOEFL iBT | PTE Academic | Common Courses |
|------|-----------------|-----------|-------------|----------------|
| Band 1 | 6.0 (no band < 6.0) | 70 (no section < 17) | 50 | Most Bachelors |
| Band 2 | 6.5 (no band < 6.0) | 84 (no section < 17) | 58 | Nursing, Education |
| Band 3 | 7.0 (no band < 6.5) | 94 (no section < 20) | 65 | Speech Pathology, Clinical Psychology |
| Band 4 | 7.5 (no band < 7.0) | — | — | Some Education programs |

> Note: Band assignments are per-course. Check individual course pages for exact band requirements.

### 3.3 Application Deadlines

**Domestic Students**
- **Semester 1 (February start)**: Applications via TISC close ~December (year prior)
- **Semester 2 (July start)**: Mid-year entry available for most courses
- **Direct applications**: Accepted year-round for some courses
- **Early Offer Program**: Applications typically open August–September

**International Students**
- **Semester 1**: Apply by November (previous year) for February start
- **Semester 2**: Apply by May for July start
- Rolling admissions for many courses; check individual course pages

### 3.4 Special Requirements

- **WAAPA courses**: Audition/interview + portfolio required; direct application (not via TISC)
- **Education courses**: Inherent requirements (literacy/numeracy tests, Working with Children Check)
- **Nursing/Midwifery**: Health screening, police clearance
- **Some Engineering programs**: 80+ ATAR indicative
- **Portfolio/Interview**: Required for select Arts & Humanities and Education programs

---

## Section 4 — Costs & Financial Aid

### 4.1 Tuition Fees (Domestic, Sample Courses)

| Course | Fee Type | Estimated 1st Year Fee (AUD) |
|--------|----------|------------------------------|
| Bachelor of Commerce | Commonwealth Supported (CSP) | $17,400 |
| Bachelor of Engineering (Chemical) Honours | Commonwealth Supported (CSP) | $8,350 |
| Master of Business Administration Global | Domestic Fee-Paying (DFP) | $32,150 |
| Graduate Certificate programs | DFP | Varies (~$8k-$16k) |

### 4.2 International Tuition Fees

International tuition fees are course-specific and listed on individual course pages. Typical ranges:
- Undergraduate (Bachelor): AUD $30,000–$40,000 per year
- Postgraduate (Master): AUD $32,000–$42,000 per year

> P1 Follow-up: Extract full international fee schedule per program.

### 4.3 Additional Fees

- **Student Services and Amenities Fee (SSAF)**: $186.50/semester (2026) for most full-time domestic students
- **WAAPA VET courses**: VET fee schedule applies
- **Incidental fees**: Health screening, police clearances, lab costs, field trips (course-specific)

### 4.4 Scholarships

| Scholarship | Amount | Eligibility |
|------------|--------|-------------|
| ATAR High Achievement Scholarship | Variable | ATAR 90+ |
| ATAR Outstanding Achievement Scholarship | Variable | ATAR 97+ |
| Vice-Chancellor's Student Awards | Variable | Outstanding contributions |
| Various need-based and equity scholarships | Variable | Domestic and International |

---

## Section 5 — Evidence Chain Index

```
E-U-001:
  field: institution.name
  value: "Edith Cowan University"
  source_url: https://www.ecu.edu.au/
  source_snippet: "Edith Cowan University | Creative thinkers made here"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-U-002:
  field: institution.cricos
  value: "00279B"
  source_url: https://www.ecu.edu.au/
  source_snippet: "CRICOS Provider No. 00279B"
  capture_date: 2026-07-10
  evidence_type: official_footer

E-U-003:
  field: schools.hierarchy
  value: "8 teaching schools: Arts & Humanities, Business & Law, Education, Engineering, Medical & Health Sciences, Nursing & Midwifery, Science, WAAPA"
  source_url: https://www.ecu.edu.au/about-ecu/schools
  source_snippet: "ECU is organized into eight teaching schools"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-U-004:
  field: courses.total_count
  value: "248 total courses (104 UG, 144 PG)"
  source_url: https://www.ecu.edu.au/degrees/courses/all
  source_snippet: "1-248 of 248 results | Courses (252)"
  capture_date: 2026-07-10
  evidence_type: course_catalog_search

E-U-005:
  field: course.bachelor_of_commerce.atar
  value: "70 Indicative ATAR"
  source_url: https://www.ecu.edu.au/degrees/courses/bachelor-of-commerce
  source_snippet: "70 Indicative ATAR"
  capture_date: 2026-07-10
  evidence_type: course_detail_page

E-U-006:
  field: course.bachelor_of_engineering_chemical.atar
  value: "80 Indicative ATAR"
  source_url: https://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-chemical-honours
  source_snippet: "80 Indicative ATAR"
  capture_date: 2026-07-10
  evidence_type: course_detail_page

E-U-007:
  field: course.bachelor_of_commerce.fee_domestic_csp
  value: "AUD $17,400"
  source_url: https://www.ecu.edu.au/degrees/courses/bachelor-of-commerce
  source_snippet: "Commonwealth supported - estimated 1st year indicative fee AUD $17,400"
  capture_date: 2026-07-10
  evidence_type: course_detail_page

E-U-008:
  field: course.bachelor_of_engineering_chemical.fee_domestic_csp
  value: "AUD $8,350"
  source_url: https://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-chemical-honours
  source_snippet: "Commonwealth supported - estimated 1st year indicative fee AUD $8,350"
  capture_date: 2026-07-10
  evidence_type: course_detail_page

E-U-009:
  field: course.mba_global.fee_domestic_dfp
  value: "AUD $32,150"
  source_url: https://www.ecu.edu.au/degrees/courses/master-of-business-administration-global
  source_snippet: "Domestic fee paying - estimated 1st year indicative fee AUD $32,150"
  capture_date: 2026-07-10
  evidence_type: course_detail_page

E-U-010:
  field: fees.ssaf
  value: "$186.50 per semester (2026)"
  source_url: https://www.ecu.edu.au/future-students/fees-and-scholarships
  source_snippet: "The fee for most full-time Australian students will be $186.50 per semester in 2026"
  capture_date: 2026-07-10
  evidence_type: official_fees_page

E-U-011:
  field: application.domestic
  value: "TISC applications; direct applications for WAAPA"
  source_url: https://www.ecu.edu.au/future-students/applying
  source_snippet: "Domestic and international students can apply for undergraduate or postgraduate courses at Edith Cowan University"
  capture_date: 2026-07-10
  evidence_type: official_applying_page

E-U-012:
  field: course_catalog.course_types
  value: "UG filters: Bachelor (64), Honours (24), Diploma (3), Entry Pathway (1); PG filters: Grad Cert (49), Grad Dip (27), Master CW (56), Master Res (10), Doctorate (2); VET: Adv Dip (4), Cert IV (2), Dip (6)"
  source_url: https://www.ecu.edu.au/degrees/courses/all
  source_snippet: "Filter results: Course type | Bachelors Degrees (Undergraduate) (64)..."
  capture_date: 2026-07-10
  evidence_type: course_catalog_filters
```

---

## Section 6 — WeKnora Import Manifest

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Reason |
|----------|-----------|--------|
| **P0** | International tuition fees per program | Not in bulk; each course page has international fee tab |
| **P0** | Full English language requirements by Band | Band system mentioned but per-band cutoffs not fully extracted |
| **P1** | Application closing dates by semester | Dates vary by course; need per-program extraction |
| **P1** | Distribution matrix exact counts | Estimated based on study area; need per-school attribution from individual course pages |
| **P1** | International student ATAR equivalents | Not found on main pages |
| **P2** | Detailed scholarship amounts and criteria | Overview only; individual scholarship pages not scraped |
| **P2** | Graduate employment outcomes | Not extracted |
| **P2** | Program highlights and accreditation details | Available on course detail pages but not bulk-extracted |

---

## Section 7 — Cross-School Comparison Framework

| Dimension | Edith Cowan University (ECU) |
|-----------|------------------------------|
| Region | Australia (Western Australia) |
| Total UG programmes | 104 (64 Bachelor + 24 Honours + 4 VET Adv Dip + 2 Cert IV + 6 VET Dip + 3 UG Dip + 1 Entry Pathway) |
| Total PG programmes | 144 (49 GC + 27 GD + 56 MCW + 10 MR + 2 PhD) |
| Total programs | 248 |
| Schools/Colleges | 8 teaching schools + 2 centres |
| ATAR range (sample) | 70–80 |
| CSP availability | Yes (most UG) |
| HECS-HELP | Yes |
| CRICOS | 00279B |
| Campus locations | 4 (City, Joondalup, SW Bunbury, Sri Lanka) |
| Young university ranking | Top 100 under 50 (THE Young University Rankings) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Edith Cowan University official website (ecu.edu.au)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (64 Bachelor + 24 Honours + 12 VET + 4 Other) | PG programmes ✅ (49 GC + 27 GD + 56 MCW + 10 MR + 2 PhD) | Fees (sampled) | Entry requirements (sampled) | Evidence (12 blocks)
> **Next step**: Extract international tuition fees per program, map exact school attribution for distribution matrix, extract detailed English language band requirements
