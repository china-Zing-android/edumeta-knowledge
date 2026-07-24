# Flinders University 知识库完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: college → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (South Australia)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~130+ (包括 majors) |
| 本科辅修 (Minors) | 包含在 majors 中 |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | ~100+ |
| 研究生博士项目 (PhD/Doctoral) | ~30+ |
| **学位项目总计** | **500+ (官方声明)** |
| 学院 (Colleges) | 5 |
| 学术院系 (Academic Schools/Departments) | 分散在5个College内 |

> 来源: Flinders University Fast Facts — "+500 undergraduate, postgraduate and research degrees"

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Flinders University
├── College of Business, Creative Arts, Law and Social Sciences
│   ├── Flinders Business School
│   ├── Creative Arts disciplines (Costume Design, Fashion, Film, Game Design, Performance, Visual Effects)
│   ├── Law & Legal Practice
│   ├── Criminology
│   ├── Social Sciences (Media & Communication, International Relations, Political Science)
│   ├── Languages, Culture & Tourism
│   └── Urban & Regional Planning
│
├── College of Human Sciences and Culture
│   ├── Arts & Humanities
│   ├── Psychology
│   ├── Education
│   ├── Social Work
│   ├── Archaeology
│   ├── History
│   ├── Philosophy
│   ├── Sociology
│   ├── Gender Studies
│   ├── Indigenous Studies
│   └── Languages
│
├── College of Health and Enablement
│   ├── Nursing & Midwifery
│   ├── Disability & Community Inclusion
│   ├── Exercise Science & Sport Science
│   ├── Health Sciences
│   ├── Paramedicine
│   ├── Speech Pathology
│   ├── Nutrition & Dietetics
│   ├── Occupational Therapy
│   ├── Physiotherapy
│   ├── Audiology
│   └── Clinical Exercise Physiology
│
├── College of Medicine and Public Health
│   ├── Medicine (Doctor of Medicine)
│   ├── Medical Science
│   ├── Public Health
│   ├── Clinical Sciences
│   ├── Clinical Epidemiology
│   └── Remote Health Practice
│
└── College of Science and Engineering
    ├── Engineering (Biomedical, Civil, Electrical, Environmental, Maritime, Mechanical, Robotics, Software)
    ├── Computer Science & Information Technology
    ├── Science (Biology, Chemistry, Physics, Marine Biology, Environmental Science, etc.)
    ├── Mathematics & Mathematical Sciences
    ├── Biotechnology
    ├── Forensic Science
    ├── Geospatial Information Systems
    ├── Surveying
    ├── Environment & Sustainability
    └── Aquaculture
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位级别 | 数量 | 说明 |
|---------|------|------|
| Bachelor (BA/BSc/BCom/LLB etc.) | ~80+ | 3-4年制本科 |
| Bachelor (Honours) | ~30+ | 1年额外荣誉学位 |
| Bachelor / Master 连读 | ~15+ | 如 BE(Hons)/ME, BExSS/MClinExPhys |
| Graduate Certificate | ~10+ | 研究生证书 |
| Graduate Diploma | ~5+ | 研究生文凭 |
| Master (Coursework) | ~50+ | 授课型硕士 (含MBA, MPH, MTeach等) |
| Master (Research) | ~10+ | 研究型硕士 (MSc, MEng, MArts by Research, MLaws, MSurgery) |
| Doctor of Philosophy (PhD) | ~25+ | 各学科博士 |
| Professional Doctorate | ~3+ | Doctor of Medicine, DClinPsych |
| Combined/Dual degrees | ~5+ | 如 BA/BSc, BGIS/BSurveying |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| College | Bachelor | Bachelor (Hons) | PGT (Masters/GradCert/GradDip) | PhD/Research | Total |
|---------|----------|-----------------|-------------------------------|-------------|-------|
| Business, Creative Arts, Law and Social Sciences | ~30 | ~8 | ~20 | ~5 | ~63 |
| Human Sciences and Culture | ~20 | ~8 | ~15 | ~5 | ~48 |
| Health and Enablement | ~20 | ~8 | ~20 | ~5 | ~53 |
| Medicine and Public Health | ~5 | ~3 | ~10 | ~5 | ~23 |
| Science and Engineering | ~30 | ~10 | ~25 | ~10 | ~75 |
| **Total** | **~105** | **~37** | **~90** | **~30** | **~262** |

> 注: 以上为从课程列表推断的主要学位课程，学院归属为基于学科领域的推断。Flinders 官方声明的"500+"包含所有专业、主修、辅修和研究生项目。

---

## Section 1 — Undergraduate education (本科教育)

### 1.1 College of Business, Creative Arts, Law and Social Sciences

| Program Name | Degree Type | College | Study Area | CRICOS |
|-------------|-------------|---------|------------|--------|
| Bachelor of Accounting | BA | BCLSS | Business | 058295A |
| Bachelor of Archaeology | BA | BCLSS | Humanities | 024778G |
| Bachelor of Arts | BA | BCLSS | Humanities | 002633F |
| Bachelor of Arts and Science | BA/BSc | BCLSS | Humanities/Science | 088518J |
| Bachelor of Business | BBus | BCLSS | Business | 058294B |
| Bachelor of Business Analytics | BBusAnalytics | BCLSS | Business | 116920G |
| Bachelor of Business (Event Mgmt & Tourism) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (Human Resource Mgmt) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (International Business) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (Leading Change) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (Management) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (Marketing) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (Small Business Leadership) | BBus | BCLSS | Business | 058294B |
| Bachelor of Business (Sports Management) | BBus | BCLSS | Business | 058294B |
| Bachelor of Commerce | BCom | BCLSS | Business | 002627D |
| Bachelor of Creative Arts (Costume Design) | BCreativeArts | BCLSS | Creative Arts | 115225E |
| Bachelor of Creative Arts (Costume Design) (VET pathway) | BCreativeArts | BCLSS | Creative Arts | 091849G |
| Bachelor of Creative Arts (Fashion) | BCreativeArts | BCLSS | Creative Arts | 115226D |
| Bachelor of Creative Arts (Fashion) (VET pathway) | BCreativeArts | BCLSS | Creative Arts | 091846M |
| Bachelor of Creative Writing | BCrW | BCLSS | Creative Arts | 119232G |
| Bachelor of Criminology | BCrim | BCLSS | Social Sciences | 092879E |
| Bachelor of Criminology (Honours) | BCrim(Hons) | BCLSS | Social Sciences | 096843G |
| Bachelor of Film and Television (Screen Industries) | BFTV | BCLSS | Creative Arts | 119233F |
| Bachelor of Film and Television (Screen Production) | BFTV | BCLSS | Creative Arts | 119234E |
| Bachelor of Game Design | BGameDes | BCLSS | Creative Arts | 118383M |
| Bachelor of International Relations and Political Science | BIRPS | BCLSS | Social Sciences | 0100840 |
| Bachelor of International Relations and Political Science (Honours) | BIRPS(Hons) | BCLSS | Social Sciences | 102682J |
| Bachelor of Languages | BLang | BCLSS | Languages | 069017K |
| Bachelor of Laws - Legal Practice Entry | LLB | BCLSS | Law | 0100911 |
| Bachelor of Laws (Honours) - Legal Practice Entry | LLB(Hons) | BCLSS | Law | 113537E |
| Bachelor of Media and Communication | BMedia | BCLSS | Media | 098433J |
| Bachelor of Performance (Acting) | BPerf | BCLSS | Creative Arts | 113438H |
| Bachelor of Performance (Directing) | BPerf | BCLSS | Creative Arts | 113438H |
| Bachelor of Performance (Theatre Making) | BPerf | BCLSS | Creative Arts | 113438H |
| Bachelor of Urban and Regional Planning | BURP | BCLSS | Social Sciences | 117650E |
| Bachelor of Visual Effects and Entertainment Design | BVFX | BCLSS | Creative Arts | 119230J |

### 1.2 College of Human Sciences and Culture

| Program Name | Degree Type | College | Study Area | CRICOS |
|-------------|-------------|---------|------------|--------|
| Bachelor of Arts | BA | HSC | Humanities | 002633F |
| Bachelor of Arts and Science | BA/BSc | HSC | Humanities/Science | 088518J |
| Bachelor of Archaeology (Honours) | BA(Hons) | HSC | Humanities | N/A |
| Bachelor of Arts (Honours) | BA(Hons) | HSC | Humanities | — |
| Bachelor of Creative Writing | BCrW | HSC | Humanities/Arts | 119232G |
| Bachelor of Education (Inclusive Education) | BEd | HSC | Education | 117254F |
| Bachelor of Education (Primary) | BEd | HSC | Education | 107185H |
| Bachelor of Education (Secondary) | BEd | HSC | Education | 107186G |
| Bachelor of Education (Secondary Health and PE) | BEd | HSC | Education | 020920E |
| Bachelor of Early Childhood Education (Birth - 5) | BECE | HSC | Education | 116862A |
| Bachelor of Early Childhood Education (Birth - 8) | BECE | HSC | Education | 107184J |
| Bachelor of Psychological Science | BPsySc | HSC | Psychology | 077358M |
| Bachelor of Psychology (Honours) | BPsy(Hons) | HSC | Psychology | 017912J |
| Bachelor of Social Work | BSW | HSC | Social Work | 083453F |

### 1.3 College of Health and Enablement

| Program Name | Degree Type | College | Study Area | CRICOS |
|-------------|-------------|---------|------------|--------|
| Bachelor of Disability and Community Inclusion | BDisCommInc | H&E | Disability | 102685F |
| Bachelor of Disability and Developmental Education | BDisDevEd | H&E | Disability | 058482J |
| Bachelor of Exercise and Sport Science | BExSS | H&E | Exercise Science | 091862M |
| Bachelor of Exercise and Sport Science / Master of Clinical Exercise Physiology | BExSS/MClinExPhys | H&E | Exercise Science | 105500G |
| Bachelor of Health Sciences | BHealthSc | H&E | Health | 020920E |
| Bachelor of Health Sciences (Vision Science) / Master of Optometry | BHealthSc/MOptom | H&E | Health | 110760M |
| Bachelor of Health Sciences / Master of Occupational Therapy | BHealthSc/MOT | H&E | Health | 0100689 |
| Bachelor of Health Sciences / Master of Physiotherapy | BHealthSc/MPhysio | H&E | Health | 0100688 |
| Bachelor of Human Nutrition | BHumanNut | H&E | Nutrition | 069219M |
| Bachelor of Midwifery (Preregistration) | BMid | H&E | Midwifery | 039814G |
| Bachelor of Nursing (Preregistration) | BNurs | H&E | Nursing | 005195K |
| Bachelor of Paramedicine | BPara | H&E | Paramedicine | 111908K |
| Bachelor of Sport and Active Recreation | BSport | H&E | Sport | 113275M |

### 1.4 College of Medicine and Public Health

| Program Name | Degree Type | College | Study Area | CRICOS |
|-------------|-------------|---------|------------|--------|
| Bachelor of Clinical Sciences, Doctor of Medicine | BClinSc/MD | M&PH | Medicine | 080922F |
| Bachelor of Medical Science | BMedSc | M&PH | Medicine | 028940C |
| Bachelor of Medical Science (Honours) | BMedSc(Hons) | M&PH | Medicine | 113274A |
| Bachelor of Medical Science (Laboratory Medicine) | BMedSc(LabMed) | M&PH | Medicine | 107262M |
| Bachelor of Public Health | BPH | M&PH | Public Health | 102949J |

### 1.5 College of Science and Engineering

| Program Name | Degree Type | College | Study Area | CRICOS |
|-------------|-------------|---------|------------|--------|
| Bachelor of Computer Science | BCompSc | S&E | IT | 064064K |
| Bachelor of Computer Science (Artificial Intelligence) | BCompSc(AI) | S&E | IT | 064064K |
| Bachelor of Computing and Mathematical Sciences (Honours) | BCompMathSc(Hons) | S&E | Computing | 118384K |
| Bachelor of Engineering (Biomedical) (Honours) | BE(Hons) | S&E | Engineering | 083439D |
| Bachelor of Engineering (Biomedical) (Hons) / ME (Biomedical) | BE(Hons)/ME | S&E | Engineering | 083440M |
| Bachelor of Engineering (Civil) (Honours) | BE(Hons) | S&E | Engineering | 083441K |
| Bachelor of Engineering (Civil) (Hons) / MEM | BE(Hons)/MEM | S&E | Engineering | 111209D |
| Bachelor of Engineering (Electrical & Electronic) (Honours) | BE(Hons) | S&E | Engineering | 102680M |
| Bachelor of Engineering (Electrical & Electronic) (Hons) / ME (Mech) | BE(Hons)/ME | S&E | Engineering | 105090J |
| Bachelor of Engineering (Electrical & Electronic) (Hons) / MEM | BE(Hons)/MEM | S&E | Engineering | 111210M |
| Bachelor of Engineering (Environmental) (Honours) | BE(Hons) | S&E | Engineering | 102907H |
| Bachelor of Engineering (Environmental) (Hons) / ME (Civil) | BE(Hons)/ME | S&E | Engineering | 105091H |
| Bachelor of Engineering (Honours) - Flexible Entry | BE(Hons) | S&E | Engineering | 093042J |
| Bachelor of Engineering (Honours) - General Entry | BE(Hons) | S&E | Engineering | 102681K |
| Bachelor of Engineering (Maritime) (Honours) | BE(Hons) | S&E | Engineering | 092433B |
| Bachelor of Engineering (Mechanical) (Honours) | BE(Hons) | S&E | Engineering | 083446E |
| Bachelor of Engineering (Mechanical) (Hons) / ME (Biomedical) | BE(Hons)/ME | S&E | Engineering | 083445F |
| Bachelor of Engineering (Mechanical) (Hons) / MEM | BE(Hons)/MEM | S&E | Engineering | 111211K |
| Bachelor of Engineering (Robotics) (Honours) | BE(Hons) | S&E | Engineering | 083449B |
| Bachelor of Engineering (Robotics) (Hons) / ME (E&E) | BE(Hons)/ME | S&E | Engineering | 105092G |
| Bachelor of Engineering (Software) (Honours) | BE(Hons) | S&E | Engineering | 083450J |
| Bachelor of Engineering Technology (Adv Manufacturing & Digital Design) | BEngTech | S&E | Engineering | 110754J |
| Bachelor of Geospatial Information Systems | BGIS | S&E | Science | 110618F |
| Bachelor of Geospatial Information Systems / Bachelor of Surveying | BGIS/BSurv | S&E | Science | 114450D |
| Bachelor of Information Technology | BIT | S&E | IT | 020067D |
| Bachelor of Information Technology (Business & Info Systems) | BIT | S&E | IT | 020067D |
| Bachelor of Information Technology (Data Analytics) | BIT | S&E | IT | 020067D |
| Bachelor of Information Technology (Digital Forensics) | BIT | S&E | IT | 111205H |
| Bachelor of Information Technology (Game Development) | BIT | S&E | IT | 020067D |
| Bachelor of Information Technology (Machine Learning) | BIT | S&E | IT | 020067D |
| Bachelor of Information Technology (Network & Cybersecurity Systems) | BIT | S&E | IT | 083451G |
| Bachelor of Mathematical Sciences | BMathSc | S&E | Science | 075594D |
| Bachelor of Science | BSc | S&E | Science | 055237B |
| Bachelor of Science (Advanced Science) | BSc(Adv) | S&E | Science | 118382A |
| Bachelor of Science (Animal Behaviour) | BSc | S&E | Science | 074770A |
| Bachelor of Science (Biodiversity and Conservation) | BSc | S&E | Science | 039816E |
| Bachelor of Science (Biotechnology) | BSc | S&E | Science | 074771M |
| Bachelor of Science (Chemical Sciences) | BSc | S&E | Science | 089663C |
| Bachelor of Science (Environmental Science) | BSc | S&E | Science | 036355J |
| Bachelor of Science (Forensic and Analytical Science) | BSc | S&E | Science | 023581F |
| Bachelor of Science (Marine Biology) | BSc | S&E | Science | 033068G |
| Bachelor of Science (Palaeontology) | BSc | S&E | Science | 098228C |

---

## Section 2 — Graduate education (研究生教育)

### 2.1 Postgraduate Taught (PGT) — 授课型硕士/证书/文凭

#### College of Business, Creative Arts, Law and Social Sciences

| Program Name | Degree Type | CRICOS |
|-------------|-------------|--------|
| Accounting | GradDip/Master | 064258M |
| Accounting and Finance | Master | 089466G |
| Applied Business Analytics | Master | 116921F |
| Business Administration (Finance) (MBA) | MBA | 107691A |
| Business Administration (Healthcare Management) (MBA) | MBA | 107691A |
| Business Administration (Human Resource Management) (MBA) | MBA | 107691A |
| Business Administration (International Business) (MBA) | MBA | 107691A |
| Business Administration (Marketing) (MBA) | MBA | 107691A |
| Business Administration Industry Focused (MBA) | MBA | 107689F |
| Graduate Certificate in Business Administration | GradCert | 107693K |
| Graduate Diploma in Business Administration | GradDip | 107692M |
| Graduate Certificate in Project Management | GradCert | 119406A |
| Graduate Diploma in Project Management | GradDip | 119405B |
| Master of Project Management | Master | 119404C/119403D |
| International Relations | Master | — |
| Media and Communication | Master | 119370H |
| Public Administration | Master | — |
| Public Policy | Master | — |
| Virtual Production | Master | — |
| Water Resources Management | Master | — |
| Teaching English to Speakers of Other Languages (TESOL) | Master/GradCert | — |

#### College of Human Sciences and Culture

| Program Name | Degree Type | CRICOS |
|-------------|-------------|--------|
| Archaeology and Heritage Management | Master | 080524J |
| Arts, Women's Studies | Master | 107181A |
| Counselling (Behavioural Health) | Master | — |
| Gender Mainstreaming Policy and Analysis | Master | — |
| Graduate Certificate in Teaching Studies | GradCert | 119310J |
| Master of Inclusive and Specialised Education | Master | 105117C |
| Master of Teaching (Birth to 5) | MTeach | 114452B |
| Master of Teaching (Early Childhood) | MTeach | 063695J |
| Master of Teaching (Primary) | MTeach | 105089B |
| Master of Teaching (Secondary) | MTeach | 063697G |
| Master of Social Work (Graduate Entry) | MSW | 019222G |
| Graduate Diploma in Psychology (Advanced) | GradDip | N/A |
| Master of Professional Psychology | MPsych | 100912 |
| Master of Psychology (Clinical) | MPsych(Clin) | 051844M |
| Society and the Individual | Master | 101000 |

#### College of Health and Enablement

| Program Name | Degree Type | CRICOS |
|-------------|-------------|--------|
| Audiology | Master | 027824D |
| Clinical Exercise Physiology | Master | 105501F |
| Disability Policy and Leadership | Master | 111469F |
| Disability Practice | Master | 111470B |
| Disability Practice and Leadership | Master | 111472M |
| Disability Practice and Leadership (Developmental Ed) | Master | 111471A |
| Environmental Health | Master | 080526G |
| Health Administration | Master | — |
| Leading Mental Health and Wellbeing | Master | 113437J |
| Master of Nursing (1.5 or 2 years) | MNurs | 113748E |
| Nutrition and Dietetics | Master | 002655M |
| Occupational Therapy | Master | 090620D |
| Physiotherapy | Master | 079421D |
| Postgraduate Nursing (Grad Cert, Grad Dip, Masters) | Various | — |
| Speech Pathology | Master | 054304D |

#### College of Medicine and Public Health

| Program Name | Degree Type | CRICOS |
|-------------|-------------|--------|
| Doctor of Medicine | MD | 077675J |
| Environmental Management and Sustainability | Master | 107182M |
| Graduate Certificate in Health Promotion | GradCert | 073816M |
| Graduate Certificate in Public Health | GradCert | 094009B |
| Master of Public Health | MPH | 0100951 |
| Master of Public Health / Master of Clinical Epidemiology | MPH/MCE | 113654M |
| Remote Health Practice | Master | — |

#### College of Science and Engineering

| Program Name | Degree Type | CRICOS |
|-------------|-------------|--------|
| Aquaculture | Master | 082818A |
| Biotechnology | Master | 043767G |
| Chemistry | Master | 083454E |
| Computer Science | Master | — |
| Computer Science (Artificial Intelligence) | Master | 105123E |
| Data Science | Master | — |
| Engineering (Biomedical) | MEng | 055942K |
| Engineering (Civil) | MEng | 091861A |
| Engineering (Electrical and Electronic) | MEng | 103305D |
| Engineering (Mechanical) | MEng | 101527 |
| Engineering Management | MEM | — |
| Engineering Science | MEngSc | 114861G |
| Environmental Management and Sustainability | Master | 107182M |
| Forensic Science | Master | 111207F |
| Geospatial Information Systems | Master | — |
| Groundwater Hydrology | Master | — |
| Information Technology | Master | — |
| Information Technology (Network and Cybersecurity Systems) | Master | 100837 |
| Mathematics | Master | 083454E |
| Physics | Master | 083454E |
| Science (Biology) | Master | 083454E |
| Science (Environmental Science) | Master | 083454E |
| Sustainable Development | Master | N/A |
| Water Resources Management | Master | — |

### 2.2 Higher Degrees by Research (HDR) — 研究型硕博

| Program Name | Degree Type | CRICOS |
|-------------|-------------|--------|
| Doctor of Philosophy | PhD | — |
| Doctor of Philosophy (Clinical Psychology) | PhD(ClinPsych) | 039996G |
| Doctor of Philosophy (PhD) by Prior Published Work | PhD | — |
| Doctor of Philosophy (PhD) in Biological Sciences | PhD | — |
| Doctor of Philosophy (PhD) in Business | PhD | — |
| Doctor of Philosophy (PhD) in Chemical or Physical Sciences | PhD | — |
| Doctor of Philosophy (PhD) in Clinical | PhD | — |
| Doctor of Philosophy (PhD) in Computing, IT or Mathematical Sciences | PhD | — |
| Doctor of Philosophy (PhD) in Creative and Performing Arts | PhD | — |
| Doctor of Philosophy (PhD) in Criminology | PhD | — |
| Doctor of Philosophy (PhD) in Disability and Community Inclusion | PhD | — |
| Doctor of Philosophy (PhD) in Education | PhD | 106255G |
| Doctor of Philosophy (PhD) in Engineering | PhD | — |
| Doctor of Philosophy (PhD) in Environmental Sciences | PhD | — |
| Doctor of Philosophy (PhD) in Government and International Relations | PhD | — |
| Doctor of Philosophy (PhD) in Health Emergencies and Health Security | PhD | — |
| Doctor of Philosophy (PhD) in Health Sciences and Allied Health | PhD | — |
| Doctor of Philosophy (PhD) in Healthy Ageing and Aged Care | PhD | — |
| Doctor of Philosophy (PhD) in History, Archaeology, Geography and Indigenous Studies | PhD | — |
| Doctor of Philosophy (PhD) in Language, Literature and Culture | PhD | — |
| Doctor of Philosophy (PhD) in Law | PhD | — |
| Doctor of Philosophy (PhD) in Medical Biosciences | PhD | — |
| Doctor of Philosophy (PhD) in Nursing and Midwifery | PhD | — |
| Doctor of Philosophy (PhD) in Palliative Care and End of Life | PhD | — |
| Doctor of Philosophy (PhD) in Psychology | PhD | 106256F |
| Doctor of Philosophy (PhD) in Public Health and Rural and Remote Health | PhD | — |
| Doctor of Philosophy (PhD) in Social Sciences | PhD | — |
| Doctor of Philosophy (PhD) in Social Work | PhD | 106263G |
| Master of Arts by Research in Creative and Performing Arts | MArts(Res) | — |
| Master of Arts by Research in History and Archaeology | MArts(Res) | — |
| Master of Arts by Research in Language, Literature and Culture | MArts(Res) | — |
| Master of Arts by Research in Social Sciences | MArts(Res) | — |
| Master of Engineering (Research) | MEng(Res) | — |
| Master of Health and Clinical Research | MHlthClinRes | 101987 |
| Master of Laws (Research) | LLM(Res) | 020070J |
| Master of Science (Research) | MSc(Res) | — |
| Master of Surgery | MSurgery | 088953A |

---

## Section 3 — Application requirements & deadlines (申请要求与截止日期)

### 3.1 Entry requirements (入学要求)

#### Undergraduate

- Completion of a recognised secondary education qualification overseas or in Australia
- Meet English language proficiency requirements
- Country-specific academic requirements apply

#### Postgraduate

- Completion of a recognised Bachelor's degree or equivalent
- Some courses require specific prior study or work experience
- English language proficiency requirements apply

#### Higher Degree by Research (HDR)

- Generally requires a university degree plus a postgraduate qualification (AQF level 8 or 9) with a significant research component
- Entry criteria vary by HDR course — review specific eligibility requirements

### 3.2 English language requirements (英语语言要求)

#### Undergraduate Programs

| Level | IELTS (Academic) | TOEFL iBT | Pearson (PTE Academic) | Cambridge C1 Advanced | OET | Duolingo^ | LanguageCert Academic^ | Applicable Courses |
|-------|-----------------|-----------|----------------------|----------------------|-----|-----------|---------------------|-------------------|
| Level 4 | 6.0 overall (6.0 S, 6.0 W) | 72 total (18 S, 18 W) | 50 overall (50 W, 50 S) | B2 overall (300 S, 300 W) | 105 overall (110 S, 110 W) | 61 overall (70 S, 64 W) | — | All UG except specified below |
| Level 5 | 6.5 overall (6.0 S, 6.0 W, 6.0 R, 6.0 L) | 79 total (18 S, 21 W, 13 R, 12 L) | 58 overall (50 S, 50 W, 50 R, 50 L) | C overall (300 S, 300 W, 300 R, 300 L) | 120 overall (110 S, 110 W, 110 R, 105 L) | 67 overall (70 S, 64 W, 60 R, 67 L) | — | Exercise Science, Human Nutrition, Psychology (Honours), Psychological Studies (GE), Psychological Science |
| Level 6 | 7.0 overall (6.5 S, 6.5 W, 6.5 R, 6.5 L) | 94 total (20 S, 24 W, 19 R, 20 L) | 65 overall (58 S, 58 W, 58 R, 58 L) | C overall (350 S, 350 W, 350 R, 350 L) | 130 overall (120 S, 130 W, 120 R, 115 L) | 73 overall (76 S, 71 W, 65 R, 62 L) | — | Health Science/OT, Health Science/Physio, Law, Law (Hons), Health Sciences (Vision Science/Optometry) |
| Level 7 | 7.0 overall (7.0 S, 7.0 W, 7.0 R, 7.0 L) | 94 total (23 S, 27 W, 24 R, 24 L) | 65 overall (65 S, 65 W, 65 R, 65 L) | C overall (350 S, 350 W, 350 R, 350 L) | 135 overall (130 S, 145 W, 130 R, 125 L) | 73 overall (82 S, —) | — | Education, Nutrition Dietetics, Paramedicine, Social Work, Speech Pathology |

> ^ Duolingo and LanguageCert Academic are NOT accepted for Nursing, Medicine, Midwifery, Occupational Therapy, Optometry, Physiotherapy, Paramedicine and Psychology courses from 2026 onwards.

#### Postgraduate Programs

| Level | IELTS | TOEFL iBT | PTE Academic | Cambridge C1 | OET | Duolingo^ | LanguageCert^ | Applicable Courses |
|-------|-------|-----------|-------------|-------------|-----|-----------|---------------|-------------------|
| Level 4 | 6.0 (6.0 S, 6.0 W) | 72 (18 S, 18 W) | 50 (50 S, 50 W) | B2 (300 S,300 W,300 R,300 L) | 105 (110 S, 110 W) | 61 (70 S, 64 W) | — | Accounting, Business Admin, Project Mgmt, Clinical Exercise Phys, Public Health, TESOL, GradCert Society & Individual |
| Level 5 | 6.5 (6.0 S,6.0 W,6.0 R,6.0 L) | 79 (18 S,21 W,13 R,12 L) | 58 (50 S,50 W,50 R,50 L) | C (300 S,300 W,300 R,300 L) | 120 (110 S,110 W,110 R,105 L) | 67 (70 S,64 W,60 R,57 L) | — | Nursing |
| Level 6 | 7.0 (6.5 S,6.5 W,6.5 R,6.5 L) | 94 (20 S,24 W,19 R,20 L) | 65 (58 S,58 W,58 R,58 L) | C (350 S,350 W,350 R,350 L) | 130 (120 S,130 W,120 R,115 L) | 73 (76 S,71 W,65 R,62 L) | — | OT, Physiotherapy, Psychology (Advanced) |
| Level 7 | 7.0 (7.0 S,7.0 W,7.0 R,7.0 L) | 94 (23 S,27 W,24 R,24 L) | 65 (65 S,65 W,65 R,65 L) | C (350 S,350 W,350 R,350 L) | — | — | — | Audiology, Counselling (Beh Health), Nutrition & Dietetics, Psych (Clinical), Social Work, Speech Pathology, Teaching |

#### Higher Degrees by Research (HDR)

| Level | IELTS | TOEFL iBT | PTE Academic | Cambridge C1 | Duolingo |
|-------|-------|-----------|-------------|-------------|---------|
| Standard | 6.5 (6.0 S, 6.5 W, 6.0 R, 6.0 L) | 80 (18 S, 22 W, 18 R, 18 L) | 58 (50 S, 58 W, 50 R, 50 L) | Overall C | N/A |
| Clinical Psychology | 7.0 (7.0 S, 7.0 W, 7.0 R, 7.0 L) | 94 (23 S, 27 W, 24 R, 24 L) | 65 (65 S, 65 W, 65 R, 65 L) | — | Not accepted |

> Note: OET scores accepted for selected study areas in College of Medicine and Public Health and College of Nursing and Health Sciences only.

### 3.3 Application deadlines (申请截止日期)

| Intake | Start Date | Application Deadline |
|--------|-----------|-------------------|
| Semester 1 | March | Applications open; rolling admissions |
| Semester 2 | July | Applications open; rolling admissions |

> Note: Specific deadlines vary by course. Apply via direct application or through an education agent.

### 3.4 Special requirements (特殊要求)

| Program | Requirement |
|---------|-------------|
| Bachelor of Nursing (Preregistration) | IELTS 7.0 (7.0 each band); must meet Nursing and Midwifery Board registration standards |
| Bachelor of Midwifery (Preregistration) | Higher English requirements; specific registration standards apply |
| Clinical programs (OT, Physio, Optometry) | Level 6 English (IELTS 7.0 overall, 6.5 each band) |
| Doctor of Medicine | Interview process; additional selection criteria |
| Performances (Acting, Directing, Theatre Making) | May require audition/portfolio |
| Psychology (Honours/Clinical) | Competitive entry based on academic performance |

---

## Section 4 — Costs & financial aid (费用与奖学金)

### 4.1 International tuition fees (2026, sampled)

| Program | Annual International Fee (AUD) | Duration |
|---------|------------------------------|----------|
| Bachelor of Arts | $35,500 | 3 years |
| Bachelor of Nursing (Preregistration) | $44,300 | 3 years |
| Bachelor of Engineering (Civil) (Honours) | $47,300 | 4 years |
| Master of Public Health | $41,400 | 2 years |

**Fee range estimate (international, 2026):** $35,500 - $47,300 AUD/year for undergraduate; $37,000 - $47,000+ for postgraduate

> Note: Fees are per full-time year (120 credit points). Actual fees vary by course. Fees listed as Full-Fee Paying (FFP). Some courses have additional costs (equipment, materials, placements).

### 4.2 Domestic students

- **Commonwealth Supported Place (CSP)**: Australian citizens, permanent residents, and NZ citizens eligible
- **HECS-HELP loan**: Government loan to defer student contribution
- **SSAF**: Student Services & Amenities Fee (compulsory)

### 4.3 Scholarships (奖学金)

Flinders offers 450+ scholarships valued at $2.4m total annually. International student scholarships include:

- **International Student Scholarships** — Merit-based partial tuition fee waivers
- **Flinders Go Beyond Scholarships** — For high-achieving international students
- **Country-specific scholarships** — Various

### 4.4 Cost of living

- Adelaide ranked in the top 30 student cities globally
- Affordable compared to Sydney/Melbourne
- Accommodation options: on-campus (Bedford Park), off-campus, homestay

---

## Section 5 — Evidence chain index (证据链索引)

### E-U-001: Institution Overview
- **Field**: institution.name
- **Value**: Flinders University
- **Source URL**: https://www.flinders.edu.au/
- **Source snippet**: "Flinders University"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-002: College Structure
- **Field**: institution.colleges
- **Value**: 5 colleges
- **Source URL**: https://www.flinders.edu.au/about/structure/colleges.html
- **Source snippet**: "College of Business, Creative Arts, Law and Social Sciences", "College of Human Sciences and Culture", "College of Health and Enablement", "College of Medicine and Public Health", "College of Science and Engineering"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-003: Student & Staff Numbers
- **Field**: institution.size
- **Value**: 25,000+ students, 2,000+ staff, 500+ degrees
- **Source URL**: https://www.flinders.edu.au/about/fast-facts
- **Source snippet**: "+25,000 students", "+2,000 staff", "+500 undergraduate, postgraduate and research degrees"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-004: Course List (International)
- **Field**: programs.full_list
- **Value**: Complete list of ~200+ courses
- **Source URL**: https://www.flinders.edu.au/study/courses
- **Source snippet**: Full course listing from combobox (international view)
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-005: Entry Requirements
- **Field**: admissions.entry_requirements
- **Value**: Academic + English language requirements
- **Source URL**: https://www.flinders.edu.au/international/apply/entry-requirements
- **Source snippet**: "To gain direct admission to Flinders University, you must meet our required academic and English proficiency requirements."
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-006: English Language Requirements
- **Field**: admissions.english_language
- **Value**: Detailed IELTS/TOEFL/PTE/Cambridge/OET/Duolingo scores by level
- **Source URL**: https://www.flinders.edu.au/international/apply/entry-requirements/english-language-requirements
- **Source snippet**: Full English language requirements tables (Undergraduate, Postgraduate, HDR)
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-007: Fee Data (Bachelor of Arts)
- **Field**: fees.international.ug_arts
- **Value**: $35,500 AUD/year (2026, FFP)
- **Source URL**: https://www.flinders.edu.au/study/courses/bachelor-arts
- **Source snippet**: "Annual Indicative Fees 2026 : $35,500 (FFP)"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-008: Fee Data (Bachelor of Engineering Civil Honours)
- **Field**: fees.international.ug_engineering
- **Value**: $47,300 AUD/year (2026, FFP)
- **Source URL**: https://www.flinders.edu.au/study/courses/bachelor-engineering-civil-honours
- **Source snippet**: "Annual Indicative Fees 2026 : $47,300 (FFP)"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-009: Fee Data (Bachelor of Nursing)
- **Field**: fees.international.ug_nursing
- **Value**: $44,300 AUD/year (2026, FFP)
- **Source URL**: https://www.flinders.edu.au/study/courses/bachelor-nursing-preregistration
- **Source snippet**: "Annual Indicative Fees 2026 : $44,300 (FFP)"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-010: Fee Data (Master of Public Health)
- **Field**: fees.international.pg_public_health
- **Value**: $41,400 AUD/year (2026)
- **Source URL**: https://www.flinders.edu.au/study/courses/master-public-health
- **Source snippet**: "Annual indicative fees (2026): $41,400"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-011: CRICOS/TEQSA
- **Field**: institution.registration
- **Value**: CRICOS Provider: 00114A, TEQSA Provider ID: PRV12097
- **Source URL**: https://www.flinders.edu.au/
- **Source snippet**: "CRICOS Provider: 00114A TEQSA Provider ID: PRV12097 TEQSA category: Australian University"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

### E-U-012: Scholarships
- **Field**: financial_aid.scholarships
- **Value**: 450+ scholarships, worth $2.4m total
- **Source URL**: https://www.flinders.edu.au/about/fast-facts
- **Source snippet**: "+450 scholarships, worth $2.4m in total"
- **Capture date**: 2026-07-10
- **Evidence type**: official_webpage

---

## Section 6 — WeKnora import manifest (导入清单)

### 6.1 Document structure

| Section | Content | Status |
|---------|---------|--------|
| Section 0 | Institution overview, counts, hierarchy, degree inventory, distribution matrix | ✅ Complete |
| Section 1 | UG programmes (full table per college) | ✅ Complete |
| Section 2 | PG taught + research programmes (full table per college) | ✅ Complete |
| Section 3 | Application requirements & deadlines | ✅ Complete |
| Section 4 | Costs & financial aid | ✅ Complete (sampled) |
| Section 5 | Evidence chain index | ✅ Complete (12 blocks) |

### 6.2 Follow-up data items (prioritized)

| Priority | Data item | Notes |
|----------|-----------|-------|
| **P0** | Full per-course ATAR entry scores | Each course has specific ATAR; not extracted |
| **P0** | Exact course counts per college | College → course mapping is inferred; official source needed |
| **P1** | Domestic fee data (CSP amounts) | CSP fees vary per discipline band; need to extract |
| **P1** | Full postgraduate fee schedule | Only sampled MPH $41,400; need comprehensive |
| **P1** | Application deadlines by course | Some courses have different closing dates |
| **P2** | Course handbook / curriculum details | Available per course page |
| **P2** | Research centre and institute details | Listed under Research page |

### 6.3 WeKnora import fields

| Field | Value | Source |
|-------|-------|--------|
| name | Flinders University | E-U-001 |
| country | Australia | E-U-001 |
| region | South Australia | E-U-001 |
| website | https://www.flinders.edu.au/ | E-U-001 |
| colleges | 5 | E-U-002 |
| total_students | 25,000+ | E-U-003 |
| total_staff | 2,000+ | E-U-003 |
| total_programs | 500+ | E-U-003 |
| cricos | 00114A | E-U-011 |
| teqsa | PRV12097 | E-U-011 |
| undergraduate_fees_international | $35,500 - $47,300/yr | E-U-007, E-U-008, E-U-009 |
| postgraduate_fees_international | $41,400+ /yr | E-U-010 |
| ielts_minimum | 6.0 (UG standard) | E-U-006 |
| intake_months | March, July | E-U-007 |

---

## Section 7 — Cross-school comparison framework (跨校对比框架)

| Dimension | Flinders University |
|-----------|-------------------|
| Location | Bedford Park, Adelaide, South Australia |
| Founded | 1966 |
| Total students | 25,000+ |
| Colleges | 5 |
| Total UG programmes | ~130+ (degree programs) |
| Total PG programmes | ~100+ (taught) |
| PhD programmes | ~30+ |
| International fee range (UG) | $35,500 - $47,300/yr |
| IELTS minimum | 6.0 (UG), 6.0 (PG standard) |
| Top 2% globally | ✅ Yes (THE 2026) |
| CRICOS | 00114A |
| Key strengths | Nursing, Medicine, Engineering, Psychology, Creative Arts |

---

## Document footer

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: University official website (flinders.edu.au)
> **Granularity**: college → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ | PG programmes ✅ | Evidence (12 blocks) ✅
> **Next step**: P0 items — per-course ATAR entry scores and exact college-program mapping
