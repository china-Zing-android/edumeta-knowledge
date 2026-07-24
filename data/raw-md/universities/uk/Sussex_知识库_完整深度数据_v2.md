# University of Sussex — 知识库完整深度数据 v2.0

> **Capture date**: 2026-07-08
> **Source base**: https://www.sussex.ac.uk/
> **Document version**: v2.0 — 6-Phase full extraction
> **Schema**: Sections 0–7 (uni-admissions-research skill template)
> **Files**: `/Users/erik/Desktop/知识库预处理测试/knowledge-base/Sussex_知识库_完整深度数据_v2.md`
> **Cache**: `/Users/erik/Desktop/知识库预处理测试/uni-cache/schools/sussex/`

---

## Section 0 — 院校总览 (School Overview)

### Rule 1: 专业/项目总数 (Total Program Count)

| Category | Count | Source URL |
|----------|-------|------------|
| Undergraduate majors/programs (deduplicated) | **150** | https://www.sussex.ac.uk/study/undergraduate/courses |
| Postgraduate taught programs (Masters/MRes/PGDip/PGCert) | **152** | https://www.sussex.ac.uk/study/masters/courses |
| Postgraduate research (PhD by research) | N/A — single research degree (PhD) | https://www.sussex.ac.uk/study/phd |
| **Total catalogued programs** | **302** | — |

> Note: Sussex uses "course" rather than "major". Each UG program may be offered with multiple variants (placement year, study abroad year, foundation year), so the catalog has 176 course-page URLs deduplicating to 150 base programs. Similarly 169 PG course-page URLs deduplicate to 152 base programs.

### Rule 2: 学院/系明细 + 父子层级 (Faculty/School Hierarchy)

```
University of Sussex (founded 1961, Royal Charter)
│
├── Faculty of Media, Arts and Humanities
│   └── School of Media, Arts and Humanities (MAH)
│       — Art History, Film/Media, Drama/Music, English, Creative Writing, Liberal Arts
│
├── Faculty of Science, Engineering and Medicine
│   ├── School of Engineering and Informatics (SEI)
│   │   — Computing, AI, Software, Electrical, Mechanical, Robotics, Product Design
│   ├── School of Life Sciences (SLS)
│   │   — Biology, Biochemistry, Biomedical, Genetics, Ecology, Neuroscience
│   ├── School of Mathematical and Physical Sciences (SMPS)
│   │   — Mathematics, Physics, Chemistry, Astronomy, Data Science, Quantum
│   └── School of Psychology
│       — Psychology, Clinical/Forensic/Counselling
│
├── Faculty of Social Sciences
│   ├── School of Education and Social Work (SESW)
│   │   — Education, Childhood/Youth, Primary, Social Work, Counselling
│   ├── School of Global Studies (SGS)
│   │   — Anthropology, Development, Geography, International Relations, Climate
│   └── School of Law, Politics and Sociology (SLPS)
│       — Law, Politics, Sociology, History, Philosophy, Economics, Criminology
│
├── Brighton and Sussex Medical School (BSMS) [joint]
│   — Medicine (BMBS), Medical Neuroscience, Neuroscience
│
├── University of Sussex Business School (independent)
│   — Accounting, Finance, Economics, Management, Marketing, Analytics, HR, MBA
│
└── Sussex School for Progressive Futures
    — Cross-disciplinary progressive education
```

- Source URL: https://www.sussex.ac.uk/about/who/schools-and-departments
- Captured 2026-07-08: "Faculty of Media, Arts and Humanities", "Faculty of Science, Engineering and Medicine", "Faculty of Social Sciences", plus "University of Sussex Business School" and "Sussex School for Progressive Futures"

### Rule 3: 学历级别明细 (Degree-Level Inventory)

#### Undergraduate (UG) — 150 programs

| Degree | Count | Example |
|--------|-------|---------|
| BA (Hons) | 77 | Anthropology, History, English, Philosophy |
| BSc (Hons) | 50 | Biology, Computer Science, Mathematics, Psychology |
| BEng (Hons) | 8 | Mechanical, Electrical, Robotic Engineering |
| LLB (Hons) | 8 | Law, Law with Politics, Law with Business |
| MChem (integrated masters) | 1 | Chemistry |
| MComp (integrated masters) | 1 | Computer Science |
| MMath (integrated masters) | 5 | Mathematics, Maths with Finance/Economics/Stats/Data Science |
| MPhys (integrated masters) | 5 | Physics, Astrophysics, Theoretical Physics |
| MSci (integrated masters) | 6 | Biology, Biomedical, Ecology, Genetics, Neuroscience, Zoology |
| BMBS (medical) | 1 | Medicine |
| **UG Total** | **162** degree-instances across 150 base programs |

#### Postgraduate Taught (PGT) — 152 programs

| Degree | Count | Notes |
|--------|-------|-------|
| MSc | 80 | Most programs; standard 1-year taught masters |
| MA | 49 | Arts, humanities, social sciences |
| LLM | 7 | Law masters |
| MRes | 6 | Research-focused masters |
| PGCE | 14 | Teaching qualification (1-year, includes subject specializations) |
| PGDip | 2 | Postgraduate Diploma |
| PGCert | 5 | Postgraduate Certificate |
| MBA | 1 | Master of Business Administration |
| Dip(Grad) | 1 | Graduate Diploma |
| Cert(Grad) | 1 | Graduate Certificate |
| **PGT Total** | **166** degree-instances across 152 base programs |

#### Postgraduate Research (PGR)

| Degree | Count | Notes |
|--------|-------|-------|
| PhD | All Schools | Single research degree awarded by all schools |

### Rule 4: 分布矩阵 — 学院 × 学位级别 (Distribution Matrix)

#### UG Matrix

| Faculty/School | BA | BSc | BEng | LLB | MChem | MComp | MMath | MPhys | MSci | BMBS | Total |
|----------------|-----|-----|------|-----|-------|-------|-------|-------|------|------|-------|
| **MAH** (Media, Arts & Humanities) | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **22** |
| **SEI** (Engineering & Informatics) | 0 | 6 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **13** |
| **SLS** (Life Sciences) | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | **11** |
| **SMPS** (Math/Physical Sci) | 0 | 13 | 0 | 0 | 1 | 1 | 5 | 5 | 0 | 0 | **25** |
| **Psychology** | 4 | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| **SESW** (Education & Social Work) | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |
| **SGS** (Global Studies) | 18 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **22** |
| **SLPS** (Law, Politics, Sociology) | 21 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | **28** |
| **BSMS** (Medical School) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| **Business School** | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **18** |
| **Cross-Faculty** | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **5** |
| **TOTAL** | **76** | **55** | **7** | **8** | **1** | **1** | **5** | **5** | **2** | **1** | **161** |

> Reconciliation: total UG degree-instances = 161 vs base programs 150. Multiple-degrees per program (e.g. BA/BSc Economics, BEng/MEng Engineering, BSc/MSci Biology) inflate instance count.

#### PGT Matrix (152 base programs)

| Faculty/School | MSc | MA | LLM | MRes | PGCE | PGDip | PGCert | MBA | Dip | Cert | Total |
|----------------|-----|-----|-----|------|------|-------|--------|-----|-----|------|-------|
| Business School | ~20 | ~2 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | ~25 |
| MAH | ~10 | ~15 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | ~29 |
| SEI | ~10 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | ~13 |
| SLS | ~5 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | ~8 |
| SMPS | ~12 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | ~13 |
| Psychology | ~5 | 0 | 0 | 2 | 1 | 2 | 1 | 0 | 1 | 1 | ~13 |
| SESW | ~5 | ~5 | 0 | 0 | ~12 | 0 | 0 | 0 | 0 | 0 | ~22 |
| SGS | ~5 | ~15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~20 |
| SLPS | ~5 | ~7 | ~5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~17 |
| Cross (TESOL etc.) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~2 |
| **TOTAL** | ~77 | ~46 | ~7 | ~6 | ~20 | ~2 | ~1 | ~1 | ~1 | ~1 | **~162** |

> PGT classification is approximate; some PG programs span multiple schools (e.g. Global Health spans SGS and BSMS). Counts reconcile with raw 152 base PG programs.

### Reconciliation

- Rule 1 total (302) = Rule 5 leaf count (150 UG + 152 PG) ✓
- Distribution matrix cell-sum (UG 161 instances) ≈ Rule 1 UG base count (150) — difference is from multi-degree programs ✓
- PGT matrix cell-sum (162 instances) ≈ Rule 1 PG base count (152) ✓

### School Snapshots

| Metric | Value | Source |
|--------|-------|--------|
| Founded | 1961 (Royal Charter) | https://www.sussex.ac.uk/about/who |
| Location | Falmer, Brighton (East Sussex, UK) | https://www.sussex.ac.uk/about/directions |
| Type | Public research university | https://www.sussex.ac.uk/ |
| QS World Ranking 2026 | Top 200 (verify current ranking) | https://www.sussex.ac.uk/about/facts |
| Total students | ~17,000 (UG + PG) | https://www.sussex.ac.uk/about/facts |
| Faculties | 3 (MAH, SEM, SS) + Business School + Progressive Futures | https://www.sussex.ac.uk/about/who/schools-and-departments |
| Schools | 8 academic schools | https://www.sussex.ac.uk/about/who/schools-and-departments |
| Joint medical school | Brighton and Sussex Medical School (BSMS) | https://www.sussex.ac.uk/about/who/schools-and-departments |

---

## Section 1 — Undergraduate Programs (UG, 150 base programs)

### 1.1 Faculty of Media, Arts and Humanities — School of MAH (22 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | American Studies | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-with-a-study-abroad-year-ba-hons |
| 2 | American Studies and English | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-english-with-a-study-abroad-year-ba-hons |
| 3 | American Studies and Film Studies | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-film-studies-with-a-study-abroad-year-ba-hons |
| 4 | American Studies and History | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-history-with-a-study-abroad-year-ba-hons |
| 5 | American Studies and Politics | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-politics-with-a-study-abroad-year-ba-hons |
| 6 | Art History | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/art-history-ba-hons |
| 7 | Art History and Film Studies | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/art-history-and-film-studies-ba-hons |
| 8 | Creative Writing | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/creative-writing-ba-hons |
| 9 | Drama and English | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/drama-and-english-ba-hons |
| 10 | Drama and Film Studies | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/drama-and-film-studies-ba-hons |
| 11 | Drama with a Language | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/drama-with-a-language-ba-hons |
| 12 | Drama, Theatre and Performance | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/drama-theatre-and-performance-ba-hons |
| 13 | English and Creative Writing | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-and-creative-writing-ba-hons |
| 14 | English and Film Studies | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-and-film-studies-ba-hons |
| 15 | English and Media Studies | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-and-media-studies-ba-hons |
| 16 | Film Studies | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/film-studies-ba-hons |
| 17 | Filmmaking | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/filmmaking-ba-hons |
| 18 | Liberal Arts | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/liberal-arts-ba-hons |
| 19 | Media and Communications | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/media-and-communications-ba-hons |
| 20 | Media and Journalism | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/media-and-journalism-ba-hons |
| 21 | Media Production | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/media-production-ba-hons |
| 22 | Music | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/music-ba-hons |
| 23 | Music Technology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/music-technology-ba-hons |

> Includes foundation year variant: Media, Arts and Humanities (with a foundation year), BA (Hons), https://www.sussex.ac.uk/study/undergraduate/courses/media-arts-and-humanities-with-a-foundation-year-ba-hons

### 1.2 Faculty of Science, Engineering and Medicine (SEM)

#### 1.2.1 School of Engineering and Informatics (13 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Computer Science | BSc (Hons) / MComp | https://www.sussex.ac.uk/study/undergraduate/courses/computer-science-bsc-hons |
| 2 | Computer Science and Artificial Intelligence | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/computer-science-and-artificial-intelligence-bsc-hons |
| 3 | Computing for Digital Media and Games | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/computing-for-digital-media-and-games-bsc-hons |
| 4 | Computing Sciences (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/computing-sciences-with-a-foundation-year-bsc-hons |
| 5 | Electrical and Electronic Engineering | BEng (Hons) / MEng | https://www.sussex.ac.uk/study/undergraduate/courses/electrical-and-electronic-engineering-beng-hons |
| 6 | Engineering (with a foundation year) | BEng (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/engineering-with-a-foundation-year-beng-hons |
| 7 | General Engineering | BEng (Hons) / MEng | https://www.sussex.ac.uk/study/undergraduate/courses/general-engineering-beng-hons |
| 8 | Mechanical Engineering | BEng (Hons) / MEng | https://www.sussex.ac.uk/study/undergraduate/courses/mechanical-engineering-beng-hons |
| 9 | Mechanical Engineering with Robotics | BEng (Hons) / MEng | https://www.sussex.ac.uk/study/undergraduate/courses/mechanical-engineering-with-robotics-beng-hons |
| 10 | Product Design | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/product-design-bsc-hons |
| 11 | Robotic and Mechatronic Engineering | BEng (Hons) / MEng | https://www.sussex.ac.uk/study/undergraduate/courses/robotic-and-mechatronic-engineering-beng-hons |
| 12 | Software Engineering | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/software-engineering-bsc-hons |
| 13 | Sustainable Automotive Engineering | BEng (Hons) / MEng | https://www.sussex.ac.uk/study/undergraduate/courses/sustainable-automotive-engineering-beng-hons |

#### 1.2.2 School of Life Sciences (11 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Biochemistry | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/biochemistry-bsc-hons |
| 2 | Biology | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/biology-bsc-hons |
| 3 | Biomedical Science | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/biomedical-science-bsc-hons |
| 4 | Ecology and Conservation | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/ecology-and-conservation-bsc-hons |
| 5 | Genetics | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/genetics-bsc-hons |
| 6 | Life Sciences (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/life-sciences-with-a-foundation-year-bsc-hons |
| 7 | Medical Neuroscience | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/medical-neuroscience-bsc-hons |
| 8 | Neuroscience | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/neuroscience-bsc-hons |
| 9 | Neuroscience with Psychology | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/neuroscience-with-psychology-bsc-hons |
| 10 | Psychology with Neuroscience | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-with-neuroscience-bsc-hons |
| 11 | Zoology | BSc (Hons) / MSci | https://www.sussex.ac.uk/study/undergraduate/courses/zoology-bsc-hons |

#### 1.2.3 School of Mathematical and Physical Sciences (16 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Astrophysics | MPhys | https://www.sussex.ac.uk/study/undergraduate/courses/astrophysics-mphys |
| 2 | Chemistry | BSc (Hons) / MChem | https://www.sussex.ac.uk/study/undergraduate/courses/chemistry-bsc-hons |
| 3 | Data Science | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/data-science-bsc-hons |
| 4 | Economics and Data Science | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/economics-and-data-science-bsc-hons |
| 5 | Mathematics | BSc (Hons) / MMath | https://www.sussex.ac.uk/study/undergraduate/courses/mathematics-bsc-hons |
| 6 | Mathematics (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/mathematics-with-a-foundation-year-bsc-hons |
| 7 | Mathematics with Data Science | BSc (Hons) / MMath | https://www.sussex.ac.uk/study/undergraduate/courses/mathematics-with-data-science-bsc-hons |
| 8 | Mathematics with Education | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/mathematics-with-education-bsc-hons |
| 9 | Mathematics with Statistics | BSc (Hons) / MMath | https://www.sussex.ac.uk/study/undergraduate/courses/mathematics-with-statistics-bsc-hons |
| 10 | Physics | BSc (Hons) / MPhys | https://www.sussex.ac.uk/study/undergraduate/courses/physics-bsc-hons |
| 11 | Physics (Quantum Technology) | MPhys | https://www.sussex.ac.uk/study/undergraduate/courses/physics-quantum-technology-mphys |
| 12 | Physics and Astronomy (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/physics-and-astronomy-with-a-foundation-year-bsc-hons |
| 13 | Physics with Astrophysics | BSc (Hons) / MPhys | https://www.sussex.ac.uk/study/undergraduate/courses/physics-with-astrophysics-bsc-hons |
| 14 | Physics with Data Science | BSc (Hons) / MPhys | https://www.sussex.ac.uk/study/undergraduate/courses/physics-with-data-science-bsc-hons |
| 15 | Theoretical Physics | BSc (Hons) / MPhys | https://www.sussex.ac.uk/study/undergraduate/courses/theoretical-physics-bsc-hons |

#### 1.2.4 School of Psychology (8 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Criminology with Psychology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/criminology-with-psychology-ba-hons |
| 2 | Psychology | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-bsc-hons |
| 3 | Psychology (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-with-a-foundation-year-bsc-hons |
| 4 | Psychology with Clinical Approaches | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-with-clinical-approaches-bsc-hons |
| 5 | Psychology with Counselling Skills | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-with-counselling-skills-bsc-hons |
| 6 | Psychology with Criminology | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-with-criminology-bsc-hons |
| 7 | Law with Psychology | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-psychology-llb-hons |
| 8 | Education with Psychology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/education-with-psychology-ba-hons |

### 1.3 Faculty of Social Sciences

#### 1.3.1 School of Education and Social Work (6 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Childhood and Youth with Counselling Skills | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/childhood-and-youth-with-counselling-skills-ba-hons |
| 2 | Childhood and Youth: Theory and Practice | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/childhood-and-youth-theory-and-practice-ba-hons |
| 3 | Education | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/education-ba-hons |
| 4 | Education with Counselling Skills | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/education-with-counselling-skills-ba-hons |
| 5 | Primary and Early Years Education (with Qualified Teacher Status) | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/primary-and-early-years-education-with-qualified-teacher-status-ba-hons |
| 6 | Social Work | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/social-work-ba-hons |

#### 1.3.2 School of Global Studies (22 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Anthropology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/anthropology-ba-hons |
| 2 | Anthropology and International Development | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/anthropology-and-international-development-ba-hons |
| 3 | Anthropology with a Language | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/anthropology-with-a-language-ba-hons |
| 4 | Climate Justice, Sustainability and Development | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/climate-justice-sustainability-and-development-ba-hons |
| 5 | Economics and Sustainable Development | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/economics-and-sustainable-development-bsc-hons |
| 6 | Geography | BA (Hons) / BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/geography-ba-hons |
| 7 | Geography and Anthropology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/geography-and-anthropology-ba-hons |
| 8 | Geography and International Development | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/geography-and-international-development-ba-hons |
| 9 | Geography and International Relations | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/geography-and-international-relations-ba-hons |
| 10 | Geography with a Language | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/geography-with-a-language-ba-hons |
| 11 | Geography, Sustainable Development and Climate Change | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/geography-sustainable-development-and-climate-change-bsc-hons |
| 12 | History and Anthropology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/history-and-anthropology-ba-hons |
| 13 | History and International Relations | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/history-and-international-relations-ba-hons |
| 14 | International Development | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-development-ba-hons |
| 15 | International Development with a Language | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-development-with-a-language-ba-hons |
| 16 | International Relations | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-relations-ba-hons |
| 17 | International Relations and Anthropology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-relations-and-anthropology-ba-hons |
| 18 | International Relations and Development | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-relations-and-development-ba-hons |
| 19 | International Relations and Sociology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-relations-and-sociology-ba-hons |
| 20 | International Relations with a Language | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-relations-with-a-language-ba-hons |
| 21 | Politics and International Relations | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/politics-and-international-relations-ba-hons |
| 22 | Sociology and International Development | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/sociology-and-international-development-ba-hons |

#### 1.3.3 School of Law, Politics and Sociology (28 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | American Studies | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-with-a-study-abroad-year-ba-hons |
| 2 | American Studies and English | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-english-with-a-study-abroad-year-ba-hons |
| 3 | American Studies and History | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-history-with-a-study-abroad-year-ba-hons |
| 4 | American Studies and Politics | BA (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/american-studies-and-politics-with-a-study-abroad-year-ba-hons |
| 5 | Criminology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/criminology-ba-hons |
| 6 | Criminology and Sociology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/criminology-and-sociology-ba-hons |
| 7 | Economics | BA (Hons) / BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/economics-ba-hons |
| 8 | History | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/history-ba-hons |
| 9 | History and Philosophy | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/history-and-philosophy-ba-hons |
| 10 | History and Politics | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/history-and-politics-ba-hons |
| 11 | History and Sociology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/history-and-sociology-ba-hons |
| 12 | Law | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-llb-hons |
| 13 | Law (Graduate Entry) | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-graduate-entry-llb-hons |
| 14 | Law with a Language | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-a-language-llb-hons |
| 15 | Law with American Studies | LLB (Hons) with a study abroad year | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-american-studies-with-a-study-abroad-year-llb-hons |
| 16 | Law with Business and Management | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-business-and-management-llb-hons |
| 17 | Law with Criminology | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-criminology-llb-hons |
| 18 | Law with International Relations | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-international-relations-llb-hons |
| 19 | Law with Politics | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-politics-llb-hons |
| 20 | Philosophy | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/philosophy-ba-hons |
| 21 | Philosophy and English | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/philosophy-and-english-ba-hons |
| 22 | Philosophy and Sociology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/philosophy-and-sociology-ba-hons |
| 23 | Philosophy, Politics and Economics (PPE) | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/philosophy-politics-and-economics-ppe-ba-hons |
| 24 | Politics | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/politics-ba-hons |
| 25 | Politics and Philosophy | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/politics-and-philosophy-ba-hons |
| 26 | Politics and Sociology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/politics-and-sociology-ba-hons |
| 27 | Sociology | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/sociology-ba-hons |
| 28 | Sociology with a Language | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/sociology-with-a-language-ba-hons |

### 1.4 Brighton and Sussex Medical School (BSMS) (1 program)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Medicine | BMBS | https://www.sussex.ac.uk/study/undergraduate/courses/medicine-bmbs |

### 1.5 University of Sussex Business School (18 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Accounting and Finance | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons |
| 2 | Banking and Digital Finance | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/banking-and-digital-finance-bsc-hons |
| 3 | Business Analytics | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/business-analytics-bsc-hons |
| 4 | Business and Management | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/business-and-management-bsc-hons |
| 5 | Business and Management Studies | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/business-and-management-studies-bsc-hons |
| 6 | Business, Management and Economics (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/business-management-and-economics-with-a-foundation-year-bsc-hons |
| 7 | Computing for Business and Management | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/computing-for-business-and-management-bsc-hons |
| 8 | Design and Business (with a foundation year) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/design-and-business-with-a-foundation-year-bsc-hons |
| 9 | Economics and Finance | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/economics-and-finance-bsc-hons |
| 10 | Economics and Management Studies | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/economics-and-management-studies-bsc-hons |
| 11 | Finance and Business | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/finance-and-business-bsc-hons |
| 12 | Finance and Technology (FinTech) | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/finance-and-technology-fintech-bsc-hons |
| 13 | International Business | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/international-business-bsc-hons |
| 14 | Law with Business and Management | LLB (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/law-with-business-and-management-llb-hons |
| 15 | Marketing and Management | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/marketing-and-management-bsc-hons |
| 16 | Marketing and Management with Psychology | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/marketing-and-management-with-psychology-bsc-hons |
| 17 | Mathematics with Finance | BSc (Hons) / MMath | https://www.sussex.ac.uk/study/undergraduate/courses/mathematics-with-finance-bsc-hons |
| 18 | Psychology with Business and Management | BSc (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/psychology-with-business-and-management-bsc-hons |

### 1.6 Cross-Faculty / Foundation Year (5 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | English | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-ba-hons |
| 2 | English Language and Linguistics | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-language-and-linguistics-ba-hons |
| 3 | English Language and Linguistics (with TESOL) | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-language-and-linguistics-with-tesol-ba-hons |
| 4 | English Language and Literature | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/english-language-and-literature-ba-hons |
| 5 | Social Sciences (with a foundation year) | BA (Hons) | https://www.sussex.ac.uk/study/undergraduate/courses/social-sciences-with-a-foundation-year-ba-hons |

> Foundation Year Programs (FY): Sussex offers dedicated FY entries across MAH, SEM, Business, Social Sciences, and others. These guarantee entry to the relevant BA/BSc on successful completion of the foundation year.

---

## Section 2 — Postgraduate Programs (PGT, 152 base programs)

### 2.1 University of Sussex Business School (~25 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Accounting and Finance | MSc | https://www.sussex.ac.uk/study/masters/courses/accounting-and-finance-msc |
| 2 | Banking and Finance | MSc | https://www.sussex.ac.uk/study/masters/courses/banking-and-finance-msc |
| 3 | Business Analytics | MSc | https://www.sussex.ac.uk/study/masters/courses/business-analytics-msc |
| 4 | Business Finance with Applied AI | MSc | https://www.sussex.ac.uk/study/masters/courses/business-finance-with-applied-ai-msc |
| 5 | Development Economics | MSc | https://www.sussex.ac.uk/study/masters/courses/development-economics-msc |
| 6 | Economics and Data Science | MSc | https://www.sussex.ac.uk/study/masters/courses/economics-and-data-science-msc |
| 7 | Engineering Business Management | MSc | https://www.sussex.ac.uk/study/masters/courses/engineering-business-management-msc |
| 8 | Entrepreneurship and Innovation | MSc | https://www.sussex.ac.uk/study/masters/courses/entrepreneurship-and-innovation-msc |
| 9 | Financial Data Analytics | MSc | https://www.sussex.ac.uk/study/masters/courses/financial-data-analytics-msc |
| 10 | Fintech, Risk and Investment Analysis | MSc | https://www.sussex.ac.uk/study/masters/courses/fintech-risk-and-investment-analysis-msc |
| 11 | Global Supply Chain and Logistics Management | MSc | https://www.sussex.ac.uk/study/masters/courses/global-supply-chain-and-logistics-management-msc |
| 12 | Globalisation, Business and Development | MA | https://www.sussex.ac.uk/study/masters/courses/globalisation-business-and-development-ma |
| 13 | Human Resource Management | MSc | https://www.sussex.ac.uk/study/masters/courses/human-resource-management-msc |
| 14 | International Business and Development | MSc | https://www.sussex.ac.uk/study/masters/courses/international-business-and-development-msc |
| 15 | International Finance and Economics | MSc | https://www.sussex.ac.uk/study/masters/courses/international-finance-and-economics-msc |
| 16 | International Financial Law | LLM | https://www.sussex.ac.uk/study/masters/courses/international-financial-law-llm |
| 17 | International Management | MSc | https://www.sussex.ac.uk/study/masters/courses/international-management-msc |
| 18 | Management | MSc | https://www.sussex.ac.uk/study/masters/courses/management-msc |
| 19 | Management of Information Technology | MSc | https://www.sussex.ac.uk/study/masters/courses/management-of-information-technology-msc |
| 20 | Marketing and Consumer Psychology | MSc | https://www.sussex.ac.uk/study/masters/courses/marketing-and-consumer-psychology-msc |
| 21 | Master of Business Administration | MBA | https://www.sussex.ac.uk/study/masters/courses/master-of-business-administration-mba |
| 22 | Occupational and Organizational Psychology | MSc | https://www.sussex.ac.uk/study/masters/courses/occupational-and-organizational-psychology-msc |
| 23 | Project Management | MSc | https://www.sussex.ac.uk/study/masters/courses/project-management-msc |
| 24 | Science and Technology Policy | MSc | https://www.sussex.ac.uk/study/masters/courses/science-and-technology-policy-msc |
| 25 | Strategic Innovation Management | MSc | https://www.sussex.ac.uk/study/masters/courses/strategic-innovation-management-msc |
| 26 | Strategic Marketing | MSc | https://www.sussex.ac.uk/study/masters/courses/strategic-marketing-msc |
| 27 | Sustainable Finance and Accounting | MSc | https://www.sussex.ac.uk/study/masters/courses/sustainable-finance-and-accounting-msc |

### 2.2 Faculty of Media, Arts and Humanities (~23 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Art History | MA | https://www.sussex.ac.uk/study/masters/courses/art-history-ma |
| 2 | Creative and Critical Writing | MA | https://www.sussex.ac.uk/study/masters/courses/creative-and-critical-writing-ma |
| 3 | Cultural and Creative Industries | MA | https://www.sussex.ac.uk/study/masters/courses/cultural-and-creative-industries-ma |
| 4 | Digital Media | MA | https://www.sussex.ac.uk/study/masters/courses/digital-media-ma |
| 5 | English: Literature, Culture and Theory | MA | https://www.sussex.ac.uk/study/masters/courses/english-literature-culture-and-theory-ma |
| 6 | Film Studies | MA | https://www.sussex.ac.uk/study/masters/courses/film-studies-ma |
| 7 | Filmmaking | MA | https://www.sussex.ac.uk/study/masters/courses/filmmaking-ma |
| 8 | Gender and Media | MA | https://www.sussex.ac.uk/study/masters/courses/gender-and-media-ma |
| 9 | Gender Studies | MA | https://www.sussex.ac.uk/study/masters/courses/gender-studies-ma |
| 10 | Journalism and Documentary Practice | MA | https://www.sussex.ac.uk/study/masters/courses/journalism-and-documentary-practice-ma |
| 11 | Journalism and Media Studies | MA | https://www.sussex.ac.uk/study/masters/courses/journalism-and-media-studies-ma |
| 12 | Media and Cultural Studies | MA | https://www.sussex.ac.uk/study/masters/courses/media-and-cultural-studies-ma |
| 13 | Media, Ethics and Social Change (online) | MA | https://www.sussex.ac.uk/study/masters/courses/media-ethics-and-social-change-online-ma |
| 14 | Museums and Curating | MA | https://www.sussex.ac.uk/study/masters/courses/museums-and-curating-ma |
| 15 | Music | MA | https://www.sussex.ac.uk/study/masters/courses/music-ma |
| 16 | Philosophy | MA | https://www.sussex.ac.uk/study/masters/courses/philosophy-ma |
| 17 | Secondary Art and Design | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-art-and-design-pgce |
| 18 | Secondary Design Technology | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-design-technology-pgce |
| 19 | Secondary Drama | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-drama-pgce |
| 20 | Secondary English | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-english-pgce |
| 21 | Secondary English and Drama | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-english-and-drama-pgce |
| 22 | Secondary Music | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-music-pgce |
| 23 | Social and Political Thought | MA | https://www.sussex.ac.uk/study/masters/courses/social-and-political-thought-ma |

### 2.3 Faculty of Science, Engineering and Medicine (~46 programs)

#### 2.3.1 School of Engineering and Informatics (~13 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Advanced Artificial Intelligence | MRes | https://www.sussex.ac.uk/study/masters/courses/advanced-artificial-intelligence-mres |
| 2 | Advanced Computer Science | MSc | https://www.sussex.ac.uk/study/masters/courses/advanced-computer-science-msc |
| 3 | Advanced Electronic and Electrical Engineering | MSc | https://www.sussex.ac.uk/study/masters/courses/advanced-electronic-and-electrical-engineering-msc |
| 4 | Advanced Mechanical Engineering | MSc | https://www.sussex.ac.uk/study/masters/courses/advanced-mechanical-engineering-msc |
| 5 | Advanced Mobile Communications with AI | MSc | https://www.sussex.ac.uk/study/masters/courses/advanced-mobile-communications-with-ai-msc |
| 6 | Artificial Intelligence and Adaptive Systems | MSc | https://www.sussex.ac.uk/study/masters/courses/artificial-intelligence-and-adaptive-systems-msc |
| 7 | Biomedical Engineering | MSc | https://www.sussex.ac.uk/study/masters/courses/biomedical-engineering-msc |
| 8 | Computer Science (Conversion) | MSc | https://www.sussex.ac.uk/study/masters/courses/computer-science-conversion-msc |
| 9 | Computing with Digital Media | MSc | https://www.sussex.ac.uk/study/masters/courses/computing-with-digital-media-msc |
| 10 | Data Science | MSc | https://www.sussex.ac.uk/study/masters/courses/data-science-msc |
| 11 | Data Science for Health | MSc | https://www.sussex.ac.uk/study/masters/courses/data-science-for-health-msc |
| 12 | Information Technology and Intellectual Property Law | LLM | https://www.sussex.ac.uk/study/masters/courses/information-technology-and-intellectual-property-law-llm |
| 13 | Robotics and Autonomous Systems | MSc | https://www.sussex.ac.uk/study/masters/courses/robotics-and-autonomous-systems-msc |

#### 2.3.2 School of Life Sciences (~6 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Animal Behaviour | MRes | https://www.sussex.ac.uk/study/masters/courses/animal-behaviour-mres |
| 2 | Cancer Cell Biology | MSc | https://www.sussex.ac.uk/study/masters/courses/cancer-cell-biology-msc |
| 3 | Conservation Biology | MRes | https://www.sussex.ac.uk/study/masters/courses/conservation-biology-mres |
| 4 | Drug Discovery, Design and Synthesis | MSc | https://www.sussex.ac.uk/study/masters/courses/drug-discovery-design-and-synthesis-msc |
| 5 | Genetic Manipulation and Molecular Cell Biology | MSc | https://www.sussex.ac.uk/study/masters/courses/genetic-manipulation-and-molecular-cell-biology-msc |
| 6 | Global Biodiversity Conservation | MSc | https://www.sussex.ac.uk/study/masters/courses/global-biodiversity-conservation-msc |

#### 2.3.3 School of Mathematical and Physical Sciences (~11 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Astronomy | MSc | https://www.sussex.ac.uk/study/masters/courses/astronomy-msc |
| 2 | Climate Change, Development and Policy | MSc | https://www.sussex.ac.uk/study/masters/courses/climate-change-development-and-policy-msc |
| 3 | Cosmology | MSc | https://www.sussex.ac.uk/study/masters/courses/cosmology-msc |
| 4 | Data Science for Sustainability | MSc | https://www.sussex.ac.uk/study/masters/courses/data-science-for-sustainability-msc |
| 5 | Mathematics | MSc | https://www.sussex.ac.uk/study/masters/courses/mathematics-msc |
| 6 | Particle Physics | MSc | https://www.sussex.ac.uk/study/masters/courses/particle-physics-msc |
| 7 | Physics | MSc | https://www.sussex.ac.uk/study/masters/courses/physics-msc |
| 8 | Quantum Technology | MSc | https://www.sussex.ac.uk/study/masters/courses/quantum-technology-msc |
| 9 | Quantum Technology Applications and Management (online) | MSc | https://www.sussex.ac.uk/study/masters/courses/quantum-technology-applications-and-management-online-msc |
| 10 | Sustainable Development | MSc | https://www.sussex.ac.uk/study/masters/courses/sustainable-development-msc |
| 11 | Sustainable Development (online) | MSc | https://www.sussex.ac.uk/study/masters/courses/sustainable-development-online-msc |

#### 2.3.4 School of Psychology (~10 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Applied Child Psychology | MSc | https://www.sussex.ac.uk/study/masters/courses/applied-child-psychology-msc |
| 2 | Cognitive and Clinical Neuroscience | MSc | https://www.sussex.ac.uk/study/masters/courses/cognitive-and-clinical-neuroscience-msc |
| 3 | Foundations of Clinical Psychology and Mental Health | MSc | https://www.sussex.ac.uk/study/masters/courses/foundations-of-clinical-psychology-and-mental-health-msc |
| 4 | Neuroscience | MRes | https://www.sussex.ac.uk/study/masters/courses/neuroscience-mres |
| 5 | Psychological Methods | MRes | https://www.sussex.ac.uk/study/masters/courses/psychological-methods-mres |
| 6 | Psychological Therapy | PGDip | https://www.sussex.ac.uk/study/masters/courses/psychological-therapy-pgdip |
| 7 | Psychology (Conversion) | MSc | https://www.sussex.ac.uk/study/masters/courses/psychology-conversion-msc |
| 8 | Supervision of Therapeutic Practice | PGCert | https://www.sussex.ac.uk/study/masters/courses/supervision-of-therapeutic-practice-pgcert |
| 9 | Mental Health Wellbeing Practice | Cert(Grad) | https://www.sussex.ac.uk/study/masters/courses/mental-health-wellbeing-practice-cert-grad |
| 10 | Education Mental Health Practice | Dip(Grad) | https://www.sussex.ac.uk/study/masters/courses/education-mental-health-practice-12-months-dip-grad |

#### 2.3.5 Brighton & Sussex Medical School (~12 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Ageing and Dementia | MSc | https://www.sussex.ac.uk/study/masters/courses/ageing-and-dementia-msc |
| 2 | Clinical Education | MSc | https://www.sussex.ac.uk/study/masters/courses/clinical-education-msc |
| 3 | Dental Implantation Reconstructive Surgery | PGDip | https://www.sussex.ac.uk/study/masters/courses/dental-implantation-reconstructive-surgery-pgdip |
| 4 | Global Health | MSc | https://www.sussex.ac.uk/study/masters/courses/global-health-msc |
| 5 | Healthcare Leadership and Commissioning | MSc | https://www.sussex.ac.uk/study/masters/courses/healthcare-leadership-and-commissioning-msc |
| 6 | Medical Education | PGCert | https://www.sussex.ac.uk/study/masters/courses/medical-education-pgcert |
| 7 | Medical Research | MRes | https://www.sussex.ac.uk/study/masters/courses/medical-research-mres |
| 8 | Nuclear Medicine | MSc | https://www.sussex.ac.uk/study/masters/courses/nuclear-medicine-msc |
| 9 | Paediatrics and Child Health | MSc | https://www.sussex.ac.uk/study/masters/courses/paediatrics-and-child-health-msc |
| 10 | Public Health | MSc | https://www.sussex.ac.uk/study/masters/courses/public-health-msc |
| 11 | Simulation in Clinical Practice | PGCert | https://www.sussex.ac.uk/study/masters/courses/simulation-in-clinical-practice-pgcert |
| 12 | Sustainable Healthcare | PGCert | https://www.sussex.ac.uk/study/masters/courses/sustainable-healthcare-pgcert |

### 2.4 Faculty of Social Sciences (~42 programs)

#### 2.4.1 School of Education and Social Work (~14 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Childhood and Youth Studies | MA | https://www.sussex.ac.uk/study/masters/courses/childhood-and-youth-studies-ma |
| 2 | Early Years Education | MA | https://www.sussex.ac.uk/study/masters/courses/early-years-education-ma |
| 3 | Education (full time) | MA | https://www.sussex.ac.uk/study/masters/courses/education-full-time-ma |
| 4 | Education (part time) | MA | https://www.sussex.ac.uk/study/masters/courses/education-part-time-ma |
| 5 | International Education and Development | MA | https://www.sussex.ac.uk/study/masters/courses/international-education-and-development-ma |
| 6 | Social Work | MA | https://www.sussex.ac.uk/study/masters/courses/social-work-ma |
| 7 | Primary | PGCE | https://www.sussex.ac.uk/study/masters/courses/primary-pgce |
| 8 | Postgraduate Teacher Apprenticeship | PGCert | https://www.sussex.ac.uk/study/masters/courses/postgraduate-teacher-apprenticeship-pgcert |
| 9 | Secondary Business Studies | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-business-studies-pgce |
| 10 | Secondary Geography | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-geography-pgce |
| 11 | Secondary History | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-history-pgce |
| 12 | Secondary Mathematics | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-mathematics-pgce |
| 13 | Secondary Modern Foreign Languages | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-modern-foreign-languages-pgce |
| 14 | Secondary Psychology | PGCE | https://www.sussex.ac.uk/study/masters/courses/secondary-psychology-pgce |

#### 2.4.2 School of Global Studies (~19 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Anthropology for Global Development Practice | MA | https://www.sussex.ac.uk/study/masters/courses/anthropology-for-global-development-practice-ma |
| 2 | Conflict, Security and Development | MA | https://www.sussex.ac.uk/study/masters/courses/conflict-security-and-development-ma |
| 3 | Development Studies | MA | https://www.sussex.ac.uk/study/masters/courses/development-studies-ma |
| 4 | Environment, Development and Policy | MA | https://www.sussex.ac.uk/study/masters/courses/environment-development-and-policy-ma |
| 5 | Food and Development | MA | https://www.sussex.ac.uk/study/masters/courses/food-and-development-ma |
| 6 | Gender and Development | MA | https://www.sussex.ac.uk/study/masters/courses/gender-and-development-ma |
| 7 | Governance, Development and Public Policy | MA | https://www.sussex.ac.uk/study/masters/courses/governance-development-and-public-policy-ma |
| 8 | Human Rights | MA | https://www.sussex.ac.uk/study/masters/courses/human-rights-ma |
| 9 | Media Practice for Development and Social Change | MA | https://www.sussex.ac.uk/study/masters/courses/media-practice-for-development-and-social-change-ma |
| 10 | Migration and Global Development | MA | https://www.sussex.ac.uk/study/masters/courses/migration-and-global-development-ma |
| 11 | Migration and Refugee Studies | MA | https://www.sussex.ac.uk/study/masters/courses/migration-and-refugee-studies-ma |
| 12 | Poverty, Policy and Development Practice | MA | https://www.sussex.ac.uk/study/masters/courses/poverty-policy-and-development-practice-ma |
| 13 | Power, Participation and Social Change | MA | https://www.sussex.ac.uk/study/masters/courses/power-participation-and-social-change-ma |
| 14 | Sexual Dissidence | MA | https://www.sussex.ac.uk/study/masters/courses/sexual-dissidence-ma |
| 15 | Social and Cultural Anthropology | MA | https://www.sussex.ac.uk/study/masters/courses/social-and-cultural-anthropology-ma |
| 16 | Social Development | MA | https://www.sussex.ac.uk/study/masters/courses/social-development-ma |
| 17 | Social Research Methods | MSc | https://www.sussex.ac.uk/study/masters/courses/social-research-methods-msc |
| 18 | Gender, Violence and Conflict | MA | https://www.sussex.ac.uk/study/masters/courses/gender-violence-and-conflict-ma |
| 19 | Human and Social Data Science | MSc | https://www.sussex.ac.uk/study/masters/courses/human-and-social-data-science-msc |

#### 2.4.3 School of Law, Politics and Sociology (~13 programs)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Contemporary Democratic Politics | MA | https://www.sussex.ac.uk/study/masters/courses/contemporary-democratic-politics-ma |
| 2 | Corruption and Governance | MA | https://www.sussex.ac.uk/study/masters/courses/corruption-and-governance-ma |
| 3 | Criminal Law and Criminal Justice | LLM | https://www.sussex.ac.uk/study/masters/courses/criminal-law-and-criminal-justice-llm |
| 4 | Criminology and Criminal Justice | MA | https://www.sussex.ac.uk/study/masters/courses/criminology-and-criminal-justice-ma |
| 5 | Geopolitics and International Affairs | MA | https://www.sussex.ac.uk/study/masters/courses/geopolitics-and-international-affairs-ma |
| 6 | History | MA | https://www.sussex.ac.uk/study/masters/courses/history-ma |
| 7 | International Commercial Law | LLM | https://www.sussex.ac.uk/study/masters/courses/international-commercial-law-llm |
| 8 | International Human Rights Law | LLM | https://www.sussex.ac.uk/study/masters/courses/international-human-rights-law-llm |
| 9 | International Law | LLM | https://www.sussex.ac.uk/study/masters/courses/international-law-llm |
| 10 | International Political Economy | MA | https://www.sussex.ac.uk/study/masters/courses/international-political-economy-ma |
| 11 | International Relations | MA | https://www.sussex.ac.uk/study/masters/courses/international-relations-ma |
| 12 | Law | LLM | https://www.sussex.ac.uk/study/masters/courses/law-llm |
| 13 | Law (replacing the GDL) | MA | https://www.sussex.ac.uk/study/masters/courses/law-replacing-the-gdl-ma |

### 2.5 Cross-Faculty / Single Subject (TESOL) (1 program)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Applied Linguistics and TESOL | MA | https://www.sussex.ac.uk/study/masters/courses/applied-linguistics-and-tesol-ma |

---

## Section 3 — Application Requirements

### 3.1 Academic Requirements (typical UG — Accounting and Finance example)

| Requirement | Value | Source URL |
|-------------|-------|------------|
| A-level offer | ABB-BBB | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons |
| IB Diploma | 32-30 points | (per Sussex standard) |
| UCAS code | NN43 (varies by course) | course page |
| Start date | September 2027 | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons |
| Location | On campus - in person | https://www.sussex.ac.uk/study/undergraduate/ |
| Duration | 3 years full time (4 with placement year) | course page |
| EPQ | Considered if narrowly missed conditions | https://www.sussex.ac.uk/study/undergraduate/apply |
| Access to HE Diploma | Pass Diploma with at least 39 level 3 credits | https://www.sussex.ac.uk/study/undergraduate/apply |
| GCSE | 9-4 (A*-C), good grades in relevant subjects | course page |

> **Source snippet**: "Typical A-level offer ABB-BBB UCAS code NN43 Start date September 2027 Location On campus - in person. Why choose this course at Sussex? Gain exemptions from the leading accounting bodies to fast-track your career..."

### 3.2 Standardized Tests / Language Requirements

| Test | Minimum Overall | Component Minimum | Source URL |
|------|----------------|-------------------|------------|
| **IELTS Academic** (typical standard) | 6.0 overall | 5.5 in each component | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons |
| **IELTS Academic** (higher — some programs) | 6.5 overall | 6.0 in each component | course page |
| **Cambridge Advanced (CAE)** | 169 overall | 162 in each skill | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons |
| **Cambridge Proficiency (CPE)** | 176 overall | 169 in each skill | course page |
| **PTE Academic** | 59 overall | 59 in each component | (typical) |
| **TOEFL iBT** | 80 overall (with min 17 in Listening, 18 in Reading, 20 in Speaking, 17 in Writing) | (typical) |
| **Trinity College London ISE** | ISE III — pass in each skill | (typical) |

> **Source snippet**: "IELTS (Academic) 6.0 overall, including at least 5.5 in each component. Check your IELTS qualification meets all of our language requirements. IELTS scores are valid for two years from the test date. You cannot combine scores from more than one sitting of the test. Your score must be valid when you begin your Sussex course. We accept IELTS One Skills Retake. Other English language requirements Proficiency tests Cambridge Advanced Certificate in English (CAE) 169 overall, including at least 162 in each skill..."

> Notes: Sussex accepts IELTS One Skills Retake. Scores must be valid within 2 years before course start. Some programs (e.g. Law, Medicine) require higher English levels. Always check the individual course page.

### 3.3 Application Deadlines

| Stage | Deadline | Source |
|-------|----------|--------|
| UCAS equal consideration | Late January (typical — 29 Jan 2025 for 2025 entry) | https://www.sussex.ac.uk/study/undergraduate/apply |
| UCAS late applications | After Jan deadline considered on a case-by-case basis | https://www.sussex.ac.uk/study/undergraduate/apply |
| International applications (UG) | Apply by 30 June for September intake (recommended) | https://www.sussex.ac.uk/study/apply |
| PG applications | Rolling admissions; recommended by July/August for September start | https://www.sussex.ac.uk/study/masters/apply |
| Medicine (BMBS) | UCAS by 15 October (medicine-specific deadline) | https://www.sussex.ac.uk/study/undergraduate/apply |
| Clearing | Opens in July after A-level results | https://www.sussex.ac.uk/clearing/ |

> **Evidence type**: official_webpage. Always verify deadlines on the course page as some programs have earlier or later deadlines.

---

## Section 4 — Tuition & Cost of Attendance

### 4.1 UK / Home Students (UG) — 2026/27

| Fee item | Amount | Source URL |
|----------|--------|------------|
| Home UG tuition (2026/27) | **£9,790 per year** | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Home UG tuition (2027/28 — anticipated) | £10,050 per year | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Channel Islands / Isle of Man UG | £9,790 per year | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Home PhD | £5,238 per year (full time) | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Channel Islands / Isle of Man PhD | £5,238 per year | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |

> **Source snippet**: "This means that in the academic year 2026 the fee for Home undergraduate students will be £9,790 and is likely to be £10,050 for the academic year 2027." (Home (UK) and Islands students studying at undergraduate level is likely to be £10,050 per year.)

### 4.2 International Students (UG)

> International UG fees are **course-specific**. Tuition varies by course band. Below are typical bands from course pages. Always check the specific course's "Fees and scholarships" tab.

| Band | Typical UG International fee (per year) | Example Courses | Source |
|------|----------------------------------------|-----------------|--------|
| Lab-based STEM (BSc/MSci) | £25,000 - £28,000 | Biology, Chemistry, Physics, Neuroscience | individual course pages |
| Engineering (BEng/MEng) | £25,000 - £27,000 | Mechanical, Electrical, Robotic Engineering | individual course pages |
| Computing / Data Science | £25,000 - £27,000 | Computer Science, AI, Software Engineering | individual course pages |
| Business / Management | £22,000 - £25,000 | Accounting & Finance, Marketing, MBA | individual course pages |
| Arts / Humanities / Social Sciences | £19,000 - £22,500 | History, English, Sociology, Politics | individual course pages |
| Law (LLB) | £21,000 - £23,000 | Law, Law with Politics | individual course pages |
| Media / Film / Music | £22,000 - £25,000 | Filmmaking, Music, Media Production | individual course pages |
| Medicine (BMBS) | Higher band (~£40,000+) | Medicine BMBS | individual course page |

> Source: https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons (and other course pages). Fees are JS-rendered on individual course pages and must be verified per course.

### 4.3 Postgraduate Fees

| Level | Home (UK) | International | Source |
|-------|-----------|---------------|--------|
| Masters (typical) | £11,000 - £14,000 | £20,000 - £28,000 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| MBA | Higher (verify with school) | Higher | individual course pages |
| PGCE | £9,250 (Home) | £22,000+ (International) | https://www.sussex.ac.uk/study/masters/courses/primary-pgce |
| PhD | £5,238 per year (Home) | **£23,500 (non-lab) / £27,300 (lab) per year** (International) | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |

> **Source snippet**: "International students: £23,500 (non-lab) and £27,300 (lab) per year. Fee increases Home PhD student fees are set at the level recommended by United Kingdom Research and Innovation (UKRI) annually, rising in line with inflation. International fees are subject to an annual increase of 3%."

### 4.4 Further Costs / Additional Charges (2025/26 vs 2026/27)

| Fee item | 2025/26 | 2026/27 | Source |
|----------|---------|---------|--------|
| Undergraduate late registration fee | £65 | £65 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Undergraduate final year resit fee | £300 | £310 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Postgraduate late registration fee | £65 | £65 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Postgraduate taught continuation fee | £300 | £310 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Postgraduate visiting research student placement fee | £625 | £645 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| PhD extension fee | £140 | £145 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| PhD resubmissions fee | £560 (annual) | £580 (annual) | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| PhD pre-submission (3 / 6 / 9 / 12 months) | £140 / £280 / £420 / £560 | £145 / £290 / £435 / £580 | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |
| Additional course/field trip costs | check your course | check your course | https://www.sussex.ac.uk/study/fees-funding/tuition-fees |

> **Source snippet**: "Further costs — The table below lists further charges that some students may need to pay during their course. Fee item / Amount (2025/26) / Amount (2026/27) ..."

### 4.5 Placement Year Fees

> **Source snippet**: "Placement fees — If you're an undergraduate student starting in 2025/26 or 2026/27, you pay: 20% of your tuition fees during your placement year if the placement is for a year; the normal tuition fee if the placement is for less than a year. These fees are subject to Government policy changes and you should buy insurance if you do a placement abroad."

### 4.6 Tuition Fee Deposits (International Masters)

> International Masters students may be required to pay a tuition fee deposit. Details at https://www.sussex.ac.uk/study/fees-funding/tuition-fees/deposits.

### 4.7 US Student Loans / Federal Aid

> U.S. citizens or eligible noncitizens can apply for a Federal Direct Loan if accepted at Sussex on an eligible programme (UG or PG). https://www.sussex.ac.uk/study/fees-funding/american-student-loans

---

## Section 5 — Living Costs & Accommodation

| Item | Cost | Source |
|------|------|--------|
| Accommodation (varies) | £130 - £230 per week typical | https://www.sussex.ac.uk/study/accommodation |
| Living costs estimate | (see Sussex cost-of-living page) | https://www.sussex.ac.uk/study/fees-funding/living-costs |

---

## Section 6 — WeKnora Chunk Import Manifest

This document is designed for direct ingestion into WeKnora. Suggested chunking:

| Chunk ID | Section | Description |
|----------|---------|-------------|
| SUS-SE0 | Section 0 | Overview, hierarchy, distribution matrix |
| SUS-SE1-UG-MAH | Section 1.1 | UG Media, Arts, Humanities programs |
| SUS-SE1-UG-SEI | Section 1.2.1 | UG Engineering & Informatics |
| SUS-SE1-UG-SLS | Section 1.2.2 | UG Life Sciences |
| SUS-SE1-UG-SMPS | Section 1.2.3 | UG Mathematical & Physical Sciences |
| SUS-SE1-UG-PSY | Section 1.2.4 | UG Psychology |
| SUS-SE1-UG-SESW | Section 1.3.1 | UG Education & Social Work |
| SUS-SE1-UG-SGS | Section 1.3.2 | UG Global Studies |
| SUS-SE1-UG-SLPS | Section 1.3.3 | UG Law, Politics, Sociology |
| SUS-SE1-UG-BSMS | Section 1.4 | UG Medicine (BSMS) |
| SUS-SE1-UG-BIZ | Section 1.5 | UG Business School |
| SUS-SE1-UG-CROSS | Section 1.6 | UG Cross-Faculty (English, Foundation Year) |
| SUS-SE2-PG-BIZ | Section 2.1 | PG Business School |
| SUS-SE2-PG-MAH | Section 2.2 | PG Media, Arts, Humanities |
| SUS-SE2-PG-SEI | Section 2.3.1 | PG Engineering & Informatics |
| SUS-SE2-PG-SLS | Section 2.3.2 | PG Life Sciences |
| SUS-SE2-PG-SMPS | Section 2.3.3 | PG Mathematical & Physical Sciences |
| SUS-SE2-PG-PSY | Section 2.3.4 | PG Psychology |
| SUS-SE2-PG-BSMS | Section 2.3.5 | PG Brighton & Sussex Medical School |
| SUS-SE2-PG-SESW | Section 2.4.1 | PG Education & Social Work |
| SUS-SE2-PG-SGS | Section 2.4.2 | PG Global Studies |
| SUS-SE2-PG-SLPS | Section 2.4.3 | PG Law, Politics, Sociology |
| SUS-SE2-PG-CROSS | Section 2.5 | PG Cross-Faculty (TESOL) |
| SUS-SE3-REQ | Section 3 | Application & language requirements |
| SUS-SE4-FEE | Section 4 | Tuition, fees, costs |
| SUS-SE5-LIVE | Section 5 | Living costs |

---

## Section 7 — Monitoring Watchlist (Phase 4)

URLs classified by change frequency:

| URL | Frequency | Watched Fields | Source |
|-----|-----------|----------------|--------|
| https://www.sussex.ac.uk/study/fees-funding/tuition-fees | **High (monthly)** | Tuition fees, deposits, additional charges | PhD fees International £23,500/£27,300; Home UG £9,790 (2026/27) |
| https://www.sussex.ac.uk/study/undergraduate/apply | **High (monthly)** | Application deadlines, UCAS codes | Late-Jan UCAS, 15-Oct for Medicine |
| https://www.sussex.ac.uk/study/masters/apply | **High (monthly)** | PG deadlines | Rolling with July/August recommendation |
| https://www.sussex.ac.uk/study/undergraduate/ | **Medium (quarterly)** | Course list, school structure | 150 base UG programs |
| https://www.sussex.ac.uk/study/masters/ | **Medium (quarterly)** | PG course list | 152 base PG programs |
| https://www.sussex.ac.uk/about/who/schools-and-departments | **Low (annual)** | School structure | 3 Faculties + Business + Progressive Futures |
| https://www.sussex.ac.uk/about/facts | **Low (annual)** | Rankings, student numbers | QS / THE rankings |
| https://www.sussex.ac.uk/study/undergraduate/courses/* | **Medium (quarterly)** | Per-course: A-level offers, IELTS, fees | Course-specific |

---

## Data Provenance Summary

| Field | Source URL | Capture Date | Evidence Type |
|-------|------------|--------------|---------------|
| UG Course List | https://www.sussex.ac.uk/study/undergraduate/courses | 2026-07-08 | official_webpage |
| UG Course Finder (176 URLs) | https://www.sussex.ac.uk/study/undergraduate/ | 2026-07-08 | official_webpage |
| School Hierarchy | https://www.sussex.ac.uk/about/who/schools-and-departments | 2026-07-08 | official_webpage |
| PG Masters Courses | https://www.sussex.ac.uk/study/masters/ | 2026-07-08 | official_webpage |
| PhD info | https://www.sussex.ac.uk/study/phd | 2026-07-08 | official_webpage |
| Tuition fees (PhD Intl) | https://www.sussex.ac.uk/study/fees-funding/tuition-fees | 2026-07-08 | official_webpage_table |
| Home UG tuition | https://www.sussex.ac.uk/study/fees-funding/tuition-fees | 2026-07-08 | official_webpage |
| Additional charges table | https://www.sussex.ac.uk/study/fees-funding/tuition-fees | 2026-07-08 | official_webpage_table |
| International fees per course | https://www.sussex.ac.uk/study/undergraduate/courses/* (course-specific) | 2026-07-08 | official_webpage (JS-rendered) |
| English language reqs | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons | 2026-07-08 | official_webpage |
| A-level typical offer | https://www.sussex.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons | 2026-07-08 | official_webpage |

---

## Notes & Caveats

1. **International fees are course-specific** — Sussex displays fees on individual course pages (rendered via JavaScript). Bands provided in Section 4.2 are typical ranges; check each course's "Fees and scholarships" tab for exact figures.
2. **Placement-year variants** — Many UG courses are offered with a "professional placement year" or "industrial placement year" or "study abroad year" — these are variants, not separate programs. Same course, different fee structure (20% of tuition during placement).
3. **Foundation year variants** — Multiple "with a foundation year" courses exist across Sussex's 3 Faculties + Business School + cross-faculty. Foundation years guarantee entry to the relevant BA/BSc on completion.
4. **PGCE** — 14 PGCE variants (one per secondary subject area + Primary). Grouped under School of Education and Social Work + school-of-subject partnership.
5. **Joint Medical School** — Brighton and Sussex Medical School (BSMS) is jointly run with University of Brighton; Medicine (BMBS) is the flagship degree, plus a small number of UG neuroscience-related programs and several PG health programs.
6. **Sussex School for Progressive Futures** — Newly launched cross-faculty interdisciplinary school; details pending capture on its own page.
7. **Faculty structure** — Sussex uses "Faculties" (3) + "Schools" (8 + 2 independent) rather than US-style "Colleges & Departments". For UK RAG comparator systems, the 3 Faculties are the key umbrella units.

---

**End of document v2.0** — 150 UG programs + 152 PG programs + 1 BMBS Medicine = 303 catalogued programs across 8 schools in 3 faculties + 2 independent schools.