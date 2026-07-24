# The University of Adelaide / Adelaide University — 知识库完整深度数据 (v2)

> **Data capture date**: 2026-07-10
> **Capture tool**: Curl-based extraction + Browser-based navigation (web_extract + browser_snapshot)
> **Target knowledge base**: WeKnora
> **Granularity**: school → college → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU, South Australia)
> **Official website (new)**: https://adelaide.edu.au/
> **Official website (legacy)**: https://www.adelaide.edu.au/

---

## ⚠️ Important Note: Merger Status

The **University of Adelaide** (est. 1874) and the **University of South Australia** merged in **2026** to form **Adelaide University** (also referred to as Adelaide University (AU)).

- The old University of Adelaide ceased operations on **31 March 2026** (151 years of operation).
- The new **Adelaide University** is the merged entity operating from **2026 onward**.
- CRICOS Provider Number: **04249J** (new entity)
- This document covers data from both the legacy institution (The University of Adelaide) and the new merged institution (Adelaide University) where applicable.

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Program Counts)

| Dimension | Count | Notes |
|-----------|-------|-------|
| 学习领域 (Study Areas) | **22** | Featured on the study page |
| 学院 (Colleges) | **6** | New Adelaide University structure |
| 本科专业 (Bachelor degrees) | **150+** | Estimate across 22 study areas |
| 研究生授课型项目 (PGT) | **200+** | Includes graduate certificates, diplomas, masters |
| 研究型项目 (Research) | **5+** | PhD, MPhil, MRes, Grad Cert Research |
| 校区 (Campuses) | **7** | City, Magill, Mawson Lakes, Mount Gambier, Roseworthy, Waite, Whyalla |

> **Note**: As a newly merged institution, the exact program count is in flux. The data below represents a **sampling approach** — indicative annual fees are shown for representative degrees only.

**Source**: https://adelaide.edu.au/study/ (22 study areas listing)

---

### 0.2 学院 / 系层级结构 (College/School Hierarchy)

#### New Adelaide University (2026–present): 6 Colleges

```
Adelaide University
│
├── College of Business and Law
│   ├── School of Accounting and Finance
│   ├── School of Economics
│   ├── School of Law
│   ├── School of Management
│   └── School of Marketing
│   └── Institutes/Centres: Institute for International Trade, Centre for Global Food and Resources,
│       Centre for Workplace Excellence, Centre for Markets, Values and Inclusion,
│       Centre for Enterprise Dynamics in Global Economies,
│       Centre for Sustainable Operations and Resilient Supply Chains
│
├── College of Creative Arts, Design and Humanities
│   ├── School of Art
│   ├── School of Performing Arts
│   ├── School of Architecture and Built Environment
│   ├── School of Art and Design
│   ├── School of Communication, Media and Journalism
│   ├── School of Humanities
│   └── Centres: Centre for Creative Practice, Centre for Aboriginal Studies in Music,
│       Centre for Interactive and Virtual Environments, Centre for Housing Research,
│       Centre for Research in Education and Social Inclusion
│
├── College of Education, Behavioural and Social Sciences
│   ├── School of Education
│   ├── School of Society and Culture
│   └── Centres: Centre for Child Protection, Centre for Research on Gender,
│       Centre for Housing Research, Centre for Islamic Thought and Education,
│       Centre for Change and Complexity
│
├── College of Engineering and Information Technology
│   ├── School of Chemical Engineering
│   ├── School of Civil Engineering
│   ├── School of Computer Science
│   ├── School of Electrical Engineering
│   └── Centres/Institutes: Centre for Space Resources, Institute for Machine Learning,
│       Centre for Interactive and Virtual Environments, Centre for Energy Technology,
│       Centre for Materials for Energy and Catalysts, Centre for Automotive Safety Research,
│       Institute for Sustainability, Energy and Resources
│
├── College of Health
│   ├── School of Allied Health and Human Performance
│   ├── School of Dentistry
│   ├── School of Public Health
│   ├── School of Pharmacy
│   ├── School of Nursing
│   ├── School of Medicine
│   ├── School of Psychology
│   └── Centres: Centre for Cancer Biology, Centre for Population and Oral Health,
│       Centre for Heart Rhythm Disorders, Centre for Male Health and Wellbeing,
│       Centre for Precision Health, Centre for Pharmaceutical Innovation,
│       Centre for Epigenetics, Robinson Research Institute, SAiGENCI
│
└── College of Science
    ├── School of Physics, Chemistry and Earth Sciences
    ├── School of Mathematical Sciences
    ├── School of Biological Sciences
    ├── School of Animal and Veterinary Sciences
    ├── School of Agriculture, Food and Wine
    └── Centres: Centre for Quantum Materials and Technology, Centre for Radiation Research and Education,
        Centre for Subatomic Structure of Matter, Centre of Light for Life,
        Institute for Water Research, Institute for Photonics and Advanced Sensing
```

#### Legacy The University of Adelaide (1874–2026): 3 Faculties (post-2023 restructure)

```
The University of Adelaide
│
├── Faculty of Arts, Business, Law and Economics (ABLE)
│   ├── Adelaide Business School
│   ├── Adelaide Law School
│   ├── School of Economics
│   ├── School of Humanities
│   ├── School of Social Sciences
│   └── Conservatorium of Music
│
├── Faculty of Health and Medical Sciences
│   ├── Adelaide Dental School
│   ├── Adelaide Medical School
│   ├── Adelaide Nursing School
│   ├── School of Allied Health Science and Practice
│   ├── School of Biomedicine
│   ├── School of Psychology
│   ├── School of Public Health
│   └── Robinson Research Institute
│
└── Faculty of Sciences, Engineering and Technology
    ├── School of Agriculture, Food and Wine
    ├── School of Animal and Veterinary Sciences
    ├── School of Biological Sciences
    ├── School of Chemical Engineering and Advanced Materials
    ├── School of Civil, Environmental and Mining Engineering
    ├── School of Computer and Mathematical Sciences
    ├── School of Electrical and Electronic Engineering
    ├── School of Mechanical Engineering
    ├── School of Physics, Chemistry and Earth Sciences
    └── Australian Institute for Machine Learning (AIML)
```

**Source**: https://adelaide.edu.au/about/colleges-schools/ (new); Wikipedia (legacy)

---

### 0.3 学历级别明细 (Degree-Level Inventory)

| Degree Level | Availability | Notes |
|--------------|-------------|-------|
| Undergraduate Certificate | ✅ | 6 months FT |
| Diploma | ✅ | 12 months FT |
| Associate Degree | ✅ | 2 years FT |
| Bachelor Degree | ✅ | 3 years FT (typical) |
| Bachelor (Honours) | ✅ | Additional year |
| Graduate Certificate | ✅ | 6 months FT |
| Graduate Diploma | ✅ | 12 months FT |
| Master (Coursework) | ✅ | 1-2 years FT |
| Master (Research) | ✅ | MPhil, MRes |
| Doctor of Philosophy (PhD) | ✅ | 3-4 years FT |
| Higher Doctorates | ✅ | DSc, DLitt, etc. |

---

## Section 1 — 学费信息 (Tuition Fees - International Students)

> **Important**: Adelaide University is a newly merged institution. Fee data below represents **sampled indicative annual tuition fees** for international students starting in 2026. For full fee schedules, visit individual degree pages.

### 1.1 Sampled Indicative Annual Tuition Fees (International, 2026)

| Degree | Annual Tuition (AUD) | Duration | Notes |
|--------|---------------------|----------|-------|
| Bachelor of Business (BBUSI) | **$50,500** | 3 years | ATAR 70 |
| Bachelor of Computer Science (BCOMP) | **$53,300** | 3 years | ATAR 75 |
| Bachelor of Engineering (Honours) | **~$52,000–55,000** | 4 years | Estimated range |
| Bachelor of Medical Studies/Doctor of Medicine | **~$70,000–95,000** | 6 years | Higher fee range |
| Master of Business Administration (MBA) | **~$55,000–65,000** | 1.5–2 years | Estimated |
| Master of Computer Science | **~$50,000–55,000** | 1.5–2 years | Estimated |
| Master of Public Health | **~$42,000–48,000** | 1.5–2 years | Estimated |
| Doctor of Philosophy (PhD) | **~$38,000–45,000** | 3–4 years | Research training fees vary |

### 1.2 Additional Fees

| Fee Type | Amount | Notes |
|----------|--------|-------|
| Application fee (international) | **$150 AUD** | Non-refundable, per application |
| Overseas Student Health Cover (OSHC) | **~$600–1,000/year** | Mandatory for international students |
| Student Services and Amenities Fee | **~$350/year** | Estimated |

**Source**: https://adelaide.edu.au/study/degrees/bachelor-of-business/ and https://adelaide.edu.au/study/degrees/bachelor-of-computer-science/

---

## Section 2 — 英语语言要求 (English Language Requirements)

### 2.1 Minimum IELTS/PTE Scores

| Degree Level | IELTS Academic (Minimum) | PTE Academic (Minimum) | TOEFL iBT (Minimum) |
|-------------|------------------------|----------------------|---------------------|
| Undergraduate (Bachelor) | **Overall 6.0** (no band below 6.0) | **50** | **60** (min 18 writing) |
| Postgraduate (Master by coursework) | **Overall 6.5** (no band below 6.0) | **58** | **79** (min 21 writing) |
| Research degrees (PhD/MPhil) | **Overall 6.5–7.0** | **58–65** | **79–94** |

> **Note**: English language entry requirements are **degree specific** — some programs (e.g., Medicine, Law, Nursing, Teaching) have **higher** requirements (IELTS 7.0+ or equivalent).

### 2.2 Accepted English Tests

- IELTS Academic (including One Skill Retake)
- PTE Academic
- TOEFL iBT
- Cambridge English: Advanced (CAE)
- C1 Advanced / C2 Proficiency

### 2.3 English Language Waiver

Applicants who completed previous study in English (e.g., diploma in Australia) may have the English requirement waived. The university also offers **English Language Centre** programs (ELICOS) for pathway entry.

**Source**: https://adelaide.edu.au/study/international-students/how-to-apply/entry-requirements/

---

## Section 3 — 申请截止日期 (Application Deadlines)

### 3.1 Standard Intakes

| Intake | Start Date | Application Deadline (International) |
|--------|-----------|--------------------------------------|
| **Semester 1** (February/March) | Late February 2026 | Rolling admissions recommended by **December** prior |
| **Semester 2** (July) | Late July 2026 | Rolling admissions recommended by **May** |
| Midyear intake | Various | Check individual degree pages |

> **Important**: Deadlines vary by degree and are **degree-specific**. The university uses a semester model; most degrees start in Semester 1. Some degrees (Bachelor of Medical Studies, MBA) have different start dates.

### 3.2 Application Process Timeline

1. **Before you apply**: Check academic/English requirements, prepare documents
2. **Applying**: Submit via Online Application System or Education Agent
3. **Offer**: Receive Letter of Offer (conditional or unconditional)
4. **Acceptance**: Accept offer + pay First Tuition Payment
5. **Student Visa**: Apply for Australian student visa (subclass 500)

> A non-refundable application fee of **AUD$150** applies per application.

**Source**: https://adelaide.edu.au/study/international-students/how-to-apply/

---

## Section 4 — 学术入学要求 (Academic Entry Requirements)

### 4.1 Undergraduate Entry

| Country/Qualification | Minimum Requirement |
|----------------------|-------------------|
| Australia (ATAR) | Minimum **70** (varies by degree, e.g., BCompSci: 75) |
| China (Gaokao) | 60%+ |
| Bangladesh (HSC) | 4.80+ |
| Canada (OSSD) | 65%+ |
| Denmark (Studentereksamen) | 4 (Fair) |
| France (Baccalaureate) | 12+ |
| Germany (Abitur) | 3.0+ |
| India (Standard XII) | 70%+ |
| Indonesia (SMA) | 8.0+ |
| Korea (CSAT/Ilsum) | Varies |
| Malaysia (STPM) | 3.0+ |
| Singapore (A-Levels) | 8-20 rank points |
| UK (A-Levels) | BBC-ABB |
| USA (High School Diploma + SAT) | SAT 1100+ |
| Vietnam (THPT) | 8.0+ |

### 4.2 Postgraduate Entry

| Requirement | Details |
|------------|---------|
| Master by coursework | Completed bachelor degree from recognised institution (or equivalent) |
| Graduate Diploma | Completed bachelor degree or equivalent |
| Graduate Certificate | Completed bachelor degree or equivalent |
| Master by Research (MPhil/MRes) | Bachelor degree with research component |
| PhD/Doctoral | Bachelor (Honours) or Master degree with research component |

### 4.3 Alternative Entry Pathways

- **Foundation Programs**: Available through pathway providers
- **English Language Centre**: ELICOS programs for conditional offers
- **Vocational Education (VET)**: Certificate IV+ or diploma from RTO considered
- **Mature-age entry**: Work experience considered for some programs

**Source**: https://adelaide.edu.au/study/international-students/how-to-apply/entry-requirements/

---

## Section 5 — 奖学金 (Scholarships)

### 5.1 International Student Scholarships

| Scholarship | Value | Eligibility |
|------------|-------|-------------|
| Global Citizens Scholarship | **15–30% tuition fee reduction** | High-achieving international students, automatic consideration |
| Alumni Scholarship | **10–15% tuition fee reduction** | Family of alumni |
| Country-specific scholarships | Varies | Available for specific regions |

> For most scholarships, international students are **automatically assessed** upon application — no separate application required.

### 5.2 Research Scholarships

- Adelaide University Research Scholarships (full tuition + stipend)
- Australian Government Research Training Program (RTP)
- International Research Tuition Scholarship (IRTS)

**Source**: https://adelaide.edu.au/study/scholarships/

---

## Section 6 — 院校排名与声誉 (Rankings & Reputation)

### 6.1 Global Rankings

| Ranking System | Position (New AU) | Position (Old UoA) |
|---------------|-------------------|-------------------|
| **QS World University Rankings 2027** | **#79** | #89 (2025), #82 (2024) |
| **Times Higher Education (THE) 2025** | — | #128 (7th nationally) |
| **Academic Ranking of World Universities (ARWU) 2025** | — | #151–200 |
| **U.S. News Best Global Universities 2025-26** | — | #99 (9th nationally) |
| **CWTS Leiden Ranking 2024** | — | #205 (7th nationally) |

### 6.2 Key Reputation Points

- **Group of Eight (Go8)** member — Australia's leading research-intensive universities
- **5 Nobel Laureates** among alumni/faculty (constituting 1/3 of Australia's total Nobel laureates)
- **117 Rhodes Scholars** and **168 Fulbright Scholars** produced
- **Member**: Association of Pacific Rim Universities (APRU)
- Located in **Adelaide** — one of the world's most liveable cities

---

## Section 7 — 院校基本信息 (Basic Institution Information)

### 7.1 Identity

| Field | Legacy (UoA) | New (Adelaide University) |
|-------|-------------|---------------------------|
| Name | The University of Adelaide | Adelaide University |
| Established | 6 November 1874 | **2026** (merger) |
| Type | Public research university | Public university |
| Motto | *Sub Cruce Lumen* ("The light under the Southern Cross") | Retained (on crest) |
| Vice-Chancellor | — | **Professor Nicola Phillips** (from 2026) |
| ABN | — | 41 202 953 738 |
| CRICOS | 00123M | **04249J** |
| TEQSA | — | PRV14404 |

### 7.2 Campuses

| Campus | Location | Focus |
|--------|----------|-------|
| **Adelaide City Campus** | North Terrace, Adelaide CBD | Main campus, most faculties |
| **Magill Campus** | Magill (inner suburb) | Education, social sciences |
| **Mawson Lakes Campus** | Mawson Lakes | Engineering, IT |
| **Waite Campus** | Urrbrae | Agriculture, wine, food science |
| **Roseworthy Campus** | Roseworthy (rural) | Veterinary science, animal production |
| **Mount Gambier Campus** | Mount Gambier (regional) | Regional programs |
| **Whyalla Campus** | Whyalla (regional) | Regional programs |

### 7.3 Student Body (Legacy UoA, 2023)

| Category | Number |
|----------|--------|
| Total Students | **30,279** |
| Doctoral Students | **1,700** |
| Academic Staff | ~1,600 |
| Administrative Staff | ~1,800 |

### 7.4 Contact Information

| Contact | Details |
|---------|---------|
| International Admissions Phone | **+61 8 7420 5115** |
| Address | Level 4, 108 North Terrace, Adelaide SA 5000, Australia |
| Enquiry Form | https://adelaide.edu.au/study/enquire/ |
| Website | https://adelaide.edu.au/ |

---

## Section 8 — 研究实力与研究机构 (Research Strengths & Institutes)

### 8.1 Key Research Institutes (Legacy & New)

| Institute | Focus Area |
|-----------|-----------|
| Australian Institute for Machine Learning (AIML) | AI, machine learning |
| Robinson Research Institute | Women's and children's health |
| South Australian Immunogenomics Cancer Institute (SAiGENCI) | Cancer research |
| Institute for Photonics and Advanced Sensing (IPAS) | Photonics, sensing |
| Institute for Sustainability, Energy and Resources (ISER) | Sustainability, energy |
| Stretton Institute | Public policy |
| Waite Research Institute | Agriculture, viticulture, oenology |
| Centre for Cancer Biology | Cancer biology |

### 8.2 Research Output Highlights

- ~70% of Australia's research output in viticulture and oenology
- ~80% of cereal varieties used in southern Australia created at Waite campus
- Home to the **Waite Arboretum** — 2,500+ tree specimens
- Adelaide BioMed City precinct — co-located with Royal Adelaide Hospital, SAHMRI

---

## Section 9 — 数据采集说明 (Data Collection Notes)

### 9.1 Methodology

- **Primary source**: https://adelaide.edu.au/ (new merged institution website)
- **Secondary source**: https://en.wikipedia.org/wiki/University_of_Adelaide (legacy institution)
- **Fees**: Sampled from individual degree pages (BBUSI: Bachelor of Business; BCOMP: Bachelor of Computer Science)
- **Note on merger**: The new Adelaide University website launched in 2026; some legacy data may not yet be fully migrated

### 9.2 Limitations

| Limitation | Description |
|------------|-------------|
| Merger transition | The institution is newly merged (2026); some degree listings, fees, and policies are still being finalised |
| Fee sampling | Only representative degrees were sampled — not a full catalogue |
| IELTS/PTE data | Minimum requirements are listed; individual degree pages may show higher requirements |
| Program counts | "150+" for bachelor degrees is an estimate based on 22 study areas; the exact count is not published as a single number |
| Old UoA data | Legacy student numbers (30,279) and faculty structure are from 2023/2024; post-merger student numbers TBD |

---

*Document generated on 2026-07-10 for the AU university knowledge base (Go8 series).*
*Target path: knowledge-base/au/*
*Cache path: uni-cache/schools/the-university-of-adelaide/*
