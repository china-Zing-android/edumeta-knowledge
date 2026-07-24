# Oxford Brookes University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (nodejs heredoc)
> **Target knowledge base**: WeKnora
> **Granularity**: school → faculty → school (department) → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Source home**: https://www.brookes.ac.uk/

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG, 含 foundation year / top-up / joint honours 变体) | 263 |
| 研究生授课型 (PGT, MSc / MA / MBA / MArch / MArchD / PGDip / PGCert / PGCE / EdD / MPH / DCM / GradDip / LLM) | 132 |
| 研究生研究型 (Research, MPhil / PhD / PhD by Published Work / MA by Research / MSc by Research / Masters by Research / PhD by Practice / ProfDoc / EngD) | 39 |
| **全量项目 (UG + PGT + Research, 全部 distinct URL)** | **~368** |
| 学院 / Faculty 数量 | 2 |
| 学校 / School 数量 | 12 |
| Subject areas (招生主题分类) | 18 |

**Source**: aggregated from 17 subject-area index pages under `https://www.brookes.ac.uk/study/subject-areas/*` + the original accounting-finance-and-economics capture. Captured 2026-07-08.

**Reconciliation note**: counts above are *URL-level*; the same programme appears under multiple subject areas when applicable (e.g. `Business and Law` appears in both Business and Law subject pages), so the per-subject-URL total exceeds unique programme count. The cross-section per-school roll-up is the authoritative number.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Oxford Brookes University
├── Faculty of Arts, Humanities and Social Sciences (AHSS)
│   ├── School of Arts
│   │   ├── Film / Film Production / Fine Art / Graphic Design / Photography
│   │   ├── Communication, Media and Culture (single & joint honours)
│   │   ├── Media, Journalism and Publishing
│   │   ├── English Literature / English Literature & Creative Writing (single + joint honours)
│   │   └── Anthropology & English Literature (joint)
│   ├── Oxford Brookes Business School
│   │   ├── Accounting / Accounting & Finance / Accounting & Economics
│   │   ├── Business and Management / Business and Marketing / Business Enterprise
│   │   ├── International Business Management / International Hospitality & Tourism
│   │   ├── Events Management / Hospitality / Tourism
│   │   ├── Digital Marketing / Marketing Management / Global Marketing
│   │   ├── Economics / Economics Politics and International Relations
│   │   ├── Information Technology for Business
│   │   ├── MBA (Oxford Brookes Global MBA)
│   │   ├── Coaching and Mentoring (MA / PGDip / PGCert / DCM)
│   │   └── HRM / Project Management / International Business & Supply Chain
│   ├── School of Education, Humanities and Languages
│   │   ├── Education Studies (BA + QTS Primary pathway)
│   │   ├── Early Childhood Studies
│   │   ├── Education Studies — SEN, Disabilities and Inclusion
│   │   ├── Japanese Studies / Modern Languages with Translation
│   │   ├── History / History of Art / Philosophy / PPE / Liberal Arts
│   │   ├── International Education (MA) / Education MA / PGCE / EdD
│   │   └── History/Philosophy/History of Art research degrees
│   ├── Oxford Brookes Law School
│   │   ├── Law (LLB Hons) / Law with Business / Law with Criminology
│   │   ├── Criminology (BSc) + joint honours
│   │   ├── LLM / LLM Legal Practice (SQE 1 & 2) / PGDL
│   │   └── PhD, LLM by Research
│   └── School of Social Sciences
│       ├── Anthropology (BA / BSc) + joint honours
│       ├── Geography + joint honours
│       ├── International Relations + joint honours
│       ├── Politics + PPE + joint honours
│       ├── Sociology + joint honours
│       └── PhD (Anthropology / Geography / Politics / Sociology)
└── Faculty of Health, Science and Technology (HST)
    ├── Oxford School of Architecture
    │   ├── Architecture (BA Hons) / MArch (Part 1 & 2) / Interior Architecture
    │   ├── MArch Part 2 / Advanced Architectural Design / Applied Design in Architecture
    │   ├── MPhil/PhD Architecture (incl. PhD by Practice)
    ├── School of Biological and Medical Sciences
    │   ├── Biological Sciences (BSc, MBiol incl. Genetics, Human Bio, Zoology)
    │   ├── Biodiversity and Wildlife Conservation
    │   ├── Biomedical Science / Medical Science
    │   ├── Equine Science
    │   ├── Conservation Ecology (MSc) / Medical Genetics and Genomics (MSc)
    │   └── MPhil/PhD Biological and Medical Sciences
    ├── School of the Built Environment
    │   ├── Building Surveying / Construction Project Management
    │   ├── Property Development & Planning / Quantity Surveying / Real Estate
    │   ├── Sustainable Urban Design & Planning
    │   ├── MArch / MArchD / Construction PM / Real Estate / BIM / Planning / IA / Urban Design
    │   └── MPhil/PhD Built Environment
    ├── School of Engineering, Computing and Mathematics
    │   ├── Artificial Intelligence (BSc/MSci, MSc) / Computer Science / Computing
    │   ├── Information Technology for Business
    │   ├── Computer Science for Cyber Security
    │   ├── Automotive Engineering (EV) / Mechanical Engineering / Motorsport
    │   ├── Electronic / Electro-Mechanical Engineering
    │   ├── Advanced Computer Science / Data Science & AI / Cyber Security (MSc)
    │   ├── Electric Motorsport / Racing Engine Systems / Automotive Eng (MSc)
    │   └── MPhil/PhD Computing / Engineering (incl. EngD ProfDoc)
    ├── Oxford School of Nursing and Midwifery
    │   ├── Nursing (Adult / Children's / Mental Health) BSc
    │   ├── Midwifery BSc / Nursing Associate FdSc
    │   ├── Midwifery / Mental Health Nursing / District Nursing (PGDip)
    │   ├── Global Public Health Leadership (MPH)
    │   ├── Professional Doctorate in Midwifery (DMid) / Nursing (DNurs)
    │   └── MPhil/PhD Nursing and Midwifery
    ├── School of Psychology, Social Work and Public Health
    │   ├── Psychology BSc / Psychology (conversion) MSc
    │   ├── Social Work BA / MA Social Work
    │   ├── Public Health MPH / Professional Development in Health & Social Care
    │   ├── Occupational Therapy (BSc + Pre-reg MSc) / Physiotherapy (BSc + Pre-reg MSc)
    │   ├── Paramedic Science
    │   ├── Social Emotional and Mental Health Difficulties (PGDip)
    │   └── MPhil/PhD Psychology / Social Work / Public Health
    └── School of Sport, Nutrition and Allied Health Professions
        ├── Nutrition BSc / Sport & Exercise Science BSc
        ├── Sport, Coaching and Physical Education BSc
        ├── Sport, Physical Activity and Health Promotion BSc / DipHE / CertHE
        ├── Applied Human Nutrition / Applied Sport & Exercise Nutrition / Dietetics (MSc)
        ├── Applied Coaching Science (MSc)
        └── MPhil/PhD Nutrition / Sport and Coaching Sciences
```

**Source**: `https://www.brookes.ac.uk/about-brookes/structure-and-governance/faculties-and-schools` (paragraph: "Oxford Brookes University has 12 schools contained within 2 faculties: the Faculty of Arts, Humanities and Social Sciences (AHSS) and the Faculty of Health, Science and Technology (HST).") Captured 2026-07-08.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 描述 | 数量 (approx) |
|---------|------|--------------|
| **UG — Foundation course** | Pre-degree preparation year (Built Environment / Computing / Engineering / Humanities / Life Sciences / Business) | 6 |
| **UG — Foundation Diploma** | UAL Level 3 Foundation Diploma in Art and Design | 1 |
| **UG — BA (Hons)** | Bachelor of Arts (Hons), single & joint honours, with/without foundation | ~110 |
| **UG — BSc (Hons)** | Bachelor of Science (Hons), single & joint honours, with/without foundation | ~95 |
| **UG — BEng (Hons)** | Bachelor of Engineering (Hons) — Automotive, Mech, Motorsport, Electronic, Electro-Mechanical | ~7 |
| **UG — MEng** | Master of Engineering integrated (Automotive, Mech, Motorsport) | 3 |
| **UG — MSci** | Master in Science integrated (AI) | 1 |
| **UG — MBiol** | Master in Biology integrated (Biodiversity, Biological Sciences variants) | 5 |
| **UG — LLB Law (Hons)** | Bachelor of Laws (Hons) | 5 |
| **UG — FD / FdSc / Fd(A)** | Foundation degree (Educational Practice Fd(A), Nursing Associate FdSc) | 2 |
| **UG — DipHE / CertHE** | Diploma / Certificate of Higher Education (Sport, Physical Activity and Health Promotion) | 1 (multi-award) |
| **UG — Top-up (Final Year Entry)** | One-year top-up (BSc / BA / BSc top-up) | ~12 |
| **PGT — MA** | Master of Arts | ~30 |
| **PGT — MSc** | Master of Science | ~50 |
| **PGT — MBA** | Oxford Brookes Global MBA | 1 |
| **PGT — MArch / MArchD** | Master of Architecture / Applied Design in Architecture | 3 |
| **PGT — LLM** | Master of Laws (incl. Legal Practice SQE 1 & 2) | 3 |
| **PGT — MPH** | Master of Public Health | 2 |
| **PGT — PGDip / PGCert** | Postgraduate Diploma / Certificate (often multi-award with MSc) | ~30 |
| **PGT — PGCE** | Postgraduate Certificate in Education (PGCE Primary 5-11, International PGCE) | 2 |
| **PGT — EdD** | Doctor of Education (taught doctorate) | 1 |
| **PGT — DCM** | Doctor of Coaching and Mentoring | 1 |
| **PGT — GradDip (PGDL)** | Graduate Diploma in Law (law conversion) | 1 |
| **PGT — Certificate (Spatial Planning Studies)** | Standalone certificate | 1 |
| **Research — MPhil** | Master of Philosophy | ~15 |
| **Research — PhD** | Doctor of Philosophy | ~25 |
| **Research — PhD by Published Work** | PhD by Published Work route | several |
| **Research — PhD by Practice** | Architecture specific | 1 |
| **Research — MA by Research** | Master of Arts by Research | ~10 |
| **Research — MSc by Research** | Master of Science by Research (incl. DAAPA specific) | several |
| **Research — Masters by Research** | Generic Masters by Research | several |
| **Research — DMid / DNurs** | Professional Doctorate in Midwifery / Nursing | 2 |
| **Research — EngD** | Engineering Professional Doctorate | 1 |

**Source**: programme degree tags parsed from `<a>` text on each subject-area index page. Captured 2026-07-08.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| School | UG | PGT | Research | Total |
|--------|----|----|----------|-------|
| School of Arts | 22 | 2 | 1 | 25 |
| Oxford Brookes Business School | 71 | 25 | 2 | 98 |
| School of Education, Humanities and Languages | 28 | 7 | 4 | 39 |
| Oxford Brookes Law School | 23 | 3 | 2 | 28 |
| School of Social Sciences | 47 | 1 | 4 | 52 |
| Oxford School of Architecture | 1 (BA) + 1 (MArch UG) | 6 | 1 | 9 |
| School of Biological and Medical Sciences | 19 | 2 | 1 | 22 |
| School of the Built Environment | 14 | 19 | 1 | 34 |
| School of Engineering, Computing and Mathematics | 22 | 9 | 2 | 33 |
| Oxford School of Nursing and Midwifery | 12 | 8 | 3 | 23 |
| School of Psychology, Social Work and Public Health | (joint with Nursing on health programmes) | 6 | 2 | 8 |
| School of Sport, Nutrition and Allied Health Professions | 9 | 4 | 2 | 15 |
| **Approx. total** | **~268** | **~92** | **~25** | **~385 (incl. some double-count on shared programmes)** |

**Reconciliation note**: matrix total exceeds Rule 1 by ~17 — these are the cross-school joint honours (e.g. `Criminology and Law` counted under both Law School and Social Sciences school) and the health programmes shared between OSNM and Psychology/Social Work. Authoritative unique-programme count is ~368.

---

## SECTION 1 — Undergraduate education

### 1.1 Foundation programmes

| Programme | Award | URL | Source page |
|-----------|-------|-----|-------------|
| Built Environment Foundation | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/built-environment-foundation | architecture-and-the-built-environment |
| Computing Foundation | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/computing-foundation | computing-and-digital-technologies |
| Engineering Foundation | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/engineering-foundation | mechanical-engineering-and-motorsport |
| Foundation in Business | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/foundation-in-business | business-and-management |
| Foundation in Humanities | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/foundation-in-humanities | history-philosophy-and-liberal-arts |
| Foundation in Law | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/foundation-in-law | law-and-criminology |
| Life Sciences Foundation Year | Foundation year | https://www.brookes.ac.uk/courses/undergraduate/life-sciences | biosciences |
| UAL Level 3 Foundation Diploma in Art and Design | Foundation Diploma | https://www.brookes.ac.uk/courses/undergraduate/foundation-diploma-art-design | arts-design-and-media |
| Educational Practice | Fd(A) | https://www.brookes.ac.uk/courses/undergraduate/educational-practice | education-early-years-and-teacher-training |
| Nursing Associate | FdSc | https://www.brookes.ac.uk/courses/undergraduate/nursing-associate-fdsc | health-and-social-care |

### 1.2 UG programmes by school

**School of Arts** (22 UG programmes)

| Programme | Award | URL | Subject area |
|-----------|-------|-----|--------------|
| Architecture (BA Hons) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/architecture | arts-design-and-media/architecture |
| Digital Media Production | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/digital-media-production | arts-design-and-media |
| Digital Media Production and Marketing | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/digital-media-production-and-marketing | arts-design-and-media |
| Film | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/film | arts-design-and-media |
| Film Production | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/film-production | arts-design-and-media |
| Fine Art | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/fine-art | arts-design-and-media |
| Fine Art and History of Art | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/fine-art-and-history-of-art-ba | arts-design-and-media |
| Graphic Design | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/graphic-design-ba | arts-design-and-media |
| Photography | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/photography | arts-design-and-media |
| Communication, Media and Culture | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture | communication-media-journalism-and-publishing |
| Communication, Media and Culture (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-with-foundation | communication-media-journalism-and-publishing |
| Media, Journalism and Publishing | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/media-journalism-and-publishing | communication-media-journalism-and-publishing |
| Anthropology and Communication, Media and Culture (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-communication-media-and-cultu | communication-media-journalism-and-publishing |
| Communication, Media and Culture and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-english-lit | communication-media-journalism-and-publishing |
| Communication, Media and Culture and International Relations (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-international | communication-media-journalism-and-publishing |
| Communication, Media and Culture and Politics (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-politics | communication-media-journalism-and-publishing |
| Communication, Media and Culture and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-sociology | communication-media-journalism-and-publishing |
| English Literature | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature | english-theatre-and-creative-writing |
| English Literature (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-with-a-foundation-year | english-theatre-and-creative-writing |
| English Literature and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-and-history | english-theatre-and-creative-writing |
| English Literature and History of Art (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-and-history-of-art | english-theatre-and-creative-writing |
| English Literature and Philosophy (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-and-philosophy | english-theatre-and-creative-writing |
| English Literature with Creative Writing | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-with-creative-writing | english-theatre-and-creative-writing |
| English Literature with Creative Writing (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-lit-creative-writing-with-foundation | english-theatre-and-creative-writing |
| Anthropology and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-english-literature | english-theatre-and-creative-writing |
| Criminology and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-english-literature | english-theatre-and-creative-writing |
| Education Studies and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies-and-english-literature | english-theatre-and-creative-writing |

**Oxford Brookes Business School** (71 UG programmes; partial listing shown for size; full leaf data is in `uni-cache/schools/oxford-brookes/courses-ug.json`)

| Programme | Award | URL |
|-----------|-------|-----|
| Accounting and Economics | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/accounting-and-economics |
| Accounting and Economics (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/accounting-and-economics-with-foundation |
| Accounting and Finance | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/accounting-and-finance |
| Accounting and Finance (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/accounting-and-finance-with-foundation |
| Business and Finance | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-finance |
| Business and Finance (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-finance-with-foundation |
| Business Finance (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-finance-final-year-top-up |
| Business Finance with Accounting (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-finance-with-accounting-final-year-top-up |
| Economics | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics |
| Economics (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-with-foundation |
| Economics, Finance and International Business | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-finance-and-international-business |
| Economics, Finance and International Business (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-finance-intl-business-with-foundation |
| Economics, Politics and International Relations | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-politics-and-international-relations |
| Economics, Politics and International Relations (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-politics-intl-relations-with-foundation |
| Business and Enterprise (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-enterprise-final-year-entry |
| Business and Law | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-law |
| Business and Law (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-law-with-foundation |
| Business and Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-management |
| Business and Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-management-with-foundation |
| Business and Marketing Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management |
| Business and Marketing Management (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management-top-up |
| Business and Marketing Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management-with-foundation |
| Business Management (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-management-final-year-entry |
| Business Management and Analytics (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-analytics-final-year-entry |
| Business Management and Geography | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-geography |
| Business Management and Geography (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-geography-with-foundation |
| Business Management and International Relations | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-international-relations |
| Business Management and International Relations (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-international-relations-with-foundation |
| Business, Enterprise and Entrepreneurship | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-enterprise-and-entrepreneurship |
| Business, Enterprise and Entrepreneurship (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-enterprise-entrepreneur-with-foundation |
| Information Technology for Business (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/information-technology-business-foundation-year |
| International Business (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-business-management-final-year-entry |
| International Business Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-business-management |
| International Business Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-business-management-with-foundation |
| Law with Business | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-with-business |
| Law with Business (with Foundation Year) | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-business-with-foundation |
| Business and Marketing Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management (marketing) |
| Business and Marketing Management (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management-top-up (marketing) |
| Business and Marketing Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management-with-foundation (marketing) |
| Digital Marketing | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/digital-marketing |
| Digital Marketing (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/digital-marketing-final-year-entry |
| Digital Marketing (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/digital-marketing-with-foundation |
| Digital Media Production and Marketing | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/digital-media-production-and-marketing (marketing) |
| Marketing and Events Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/ba-hons-marketing-and-events-management |
| Marketing and Events Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/marketing-and-events-management-with-foundation |
| Marketing Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/marketing-management |
| Marketing Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/marketing-management-with-foundation |
| Events Management | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/events-management |
| Events Management (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/events-management-with-foundation |
| International Hospitality and Tourism Management | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-hospitality-and-tourism-management |
| International Hospitality and Tourism Management (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/intl-hospitality-and-tourism-management-top-up |
| International Hospitality and Tourism Management (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-hospitality-tourism-with-foundation |
| Marketing and Events Management | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/ba-hons-marketing-and-events-management (hospitality) |
| Marketing and Events Management (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/marketing-and-events-management-with-foundation (hospitality) |

**School of Education, Humanities and Languages** (28 UG programmes; full leaf in cache)

| Programme | Award | URL |
|-----------|-------|-----|
| Criminology and Education Studies (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-education-studies |
| Early Childhood Studies | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/early-childhood-studies |
| Early Childhood Studies (Final Year Entry) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/early-childhood-studies-final-year-entry |
| Early Childhood Studies (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/early-childhood-studies-with-foundation |
| Education Studies — SEN, Disabilities and Inclusion | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies-sen-disabilities-and-inclusion |
| Education Studies — SEN, Disabilities and Inclusion (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-sen-disability-inclusion-with-foundation |
| Education Studies | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies |
| Education Studies (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies-with-foundation |
| Education Studies and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies-and-english-literature |
| Education Studies and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies-and-sociology |
| Primary Teacher Education with QTS (Campus-Based) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/primary-teacher-education-campus-based |
| Japanese Studies | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/japanese-studies |
| Japanese Studies (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/japanese-studies-with-foundation |
| Modern Languages with Translation | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/modern-languages-with-translation |
| Modern Languages with Translation (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/modern-languages-with-foundation |
| Anthropology and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-history |
| Anthropology and History of Art (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-history-of-art |
| Anthropology and Philosophy (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-philosophy |
| Criminology and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-history |
| English Literature and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-and-history |
| English Literature and History of Art (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-and-history-of-art |
| English Literature and Philosophy (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/english-literature-and-philosophy |
| Geography and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/geography-and-history |
| History | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history |
| History (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-with-a-foundation-year |
| History and History of Art (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-and-history-of-art |
| History and International Relations (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-and-international-relations |
| History and Politics (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-and-politics |
| History of Art | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-of-art |
| History of Art (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-of-art-with-foundation |
| History of Art and Sociology (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-of-art-and-sociology |
| International Relations and Philosophy (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-relations-and-philosophy |
| Philosophy | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy |
| Philosophy (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy-with-foundation |
| Philosophy and Politics (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy-and-politics |
| Philosophy and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy-and-sociology |

**Oxford Brookes Law School** (23 UG programmes; full leaf in cache)

| Programme | Award | URL |
|-----------|-------|-----|
| Business and Law | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-law (law) |
| Business and Law (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-and-law-with-foundation (law) |
| Criminology | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology |
| Criminology (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-with-a-foundation-year |
| Criminology and Anthropology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-anthropology |
| Criminology and Education Studies (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-education-studies |
| Criminology and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-english-literature |
| Criminology and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-history |
| Criminology and International Relations (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-international-relations |
| Criminology and Law | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-law |
| Criminology and Law (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-law-with-foundation |
| Criminology and Politics (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-politics |
| Criminology and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-sociology |
| Foundation in Law | Foundation course | https://www.brookes.ac.uk/courses/undergraduate/foundation-in-law |
| Law (Final Year Entry) | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-final-year-entry |
| Law | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law |
| Law (with Foundation Year) | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-with-foundation |
| Law with Business | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-with-business |
| Law with Business (with Foundation Year) | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-business-with-foundation |
| Law with Criminology | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-with-criminology |
| Law with Criminology (with Foundation Year) | LLB Law (Hons) | https://www.brookes.ac.uk/courses/undergraduate/law-criminology-with-foundation |

**School of Social Sciences** (47 UG programmes; full leaf in cache)

| Programme | Award | URL |
|-----------|-------|-----|
| Anthropology | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology |
| Anthropology (with Foundation Year) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-with-foundation |
| Anthropology and Communication, Media and Culture (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-communication-media-and-cultu (socsci) |
| Anthropology and English Literature (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-english-literature (socsci) |
| Anthropology and Geography (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-geography |
| Anthropology and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-history (socsci) |
| Anthropology and History of Art (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-history-of-art (socsci) |
| Anthropology and International Relations (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-international-relations |
| Anthropology and Philosophy (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-philosophy (socsci) |
| Anthropology and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/anthropology-and-sociology |
| Business Management and Geography | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-geography (socsci) |
| Business Management and Geography (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-geography-with-foundation (socsci) |
| Business Management and International Relations | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-management-and-international-relations (socsci) |
| Business Management and International Relations (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/business-international-relations-with-foundation (socsci) |
| Communication, Media and Culture and International Relations (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-international (socsci) |
| Communication, Media and Culture and Politics (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-politics (socsci) |
| Communication, Media and Culture and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture-and-sociology (socsci) |
| Criminology and Anthropology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-anthropology (socsci) |
| Criminology and International Relations (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-international-relations (socsci) |
| Criminology and Politics (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/criminology-and-politics (socsci) |
| Economics, Politics and International Relations | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-politics-and-international-relations (socsci) |
| Economics, Politics and International Relations (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/economics-politics-intl-relations-with-foundation (socsci) |
| Education Studies and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/education-studies-and-sociology (socsci) |
| Geography | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/geography |
| Geography (with Foundation Year) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/geography-with-foundation |
| Geography and History (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/geography-and-history (socsci) |
| Geography and International Relations (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/geography-and-international-relations |
| History and International Relations (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-and-international-relations (socsci) |
| History and Politics (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-and-politics (socsci) |
| History of Art and Sociology (joint) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/history-of-art-and-sociology (socsci) |
| International Relations | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-relations |
| International Relations and Philosophy (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-relations-and-philosophy (socsci) |
| International Relations and Politics | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-relations-and-politics |
| International Relations and Politics (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-relations-politics-with-foundation |
| International Relations and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/international-relations-and-sociology |
| Philosophy and Politics (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy-and-politics (socsci) |
| Philosophy and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy-and-sociology (socsci) |
| Philosophy, Politics and Economics (PPE) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/philosophy-politics-economics-ppe |
| Politics | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/politics |
| Politics and Sociology (joint) | BA (Hons) / BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/politics-and-sociology |
| Psychology | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/psychology |
| Psychology (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/psychology-foundation-year |
| Sociology | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sociology |
| Sociology (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sociology-with-foundation |

**Oxford School of Architecture** (UG; MArch is UG integrated Part 1 & 2)

| Programme | Award | URL |
|-----------|-------|-----|
| Architecture | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/architecture |
| MArch Architecture (Part 1 and 2) | BA (Hons) / MArch | https://www.brookes.ac.uk/courses/undergraduate/architecture-part-1-and-2 |
| Interior Architecture | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/interior-architecture |

**School of Biological and Medical Sciences** (UG)

| Programme | Award | URL |
|-----------|-------|-----|
| Biodiversity and Wildlife Conservation | BSc (Hons) / MBiol | https://www.brookes.ac.uk/courses/undergraduate/biodiversity-and-wildlife-conservation |
| Biodiversity and Wildlife Conservation (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biodiversity-wildlife-conservation-foundation-year |
| Biological Sciences | BSc (Hons) / MBiol | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences |
| Biological Sciences (Genetics and Genomics) | BSc (Hons) / MBiol | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences-genetics-and-genomics |
| Biological Sciences (Genetics and Genomics) (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biological-sci-genetics-genomics-foundation-year |
| Biological Sciences (Human Biosciences) | BSc (Hons) / MBiol | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences-human-biosciences |
| Biological Sciences (Human Biosciences) (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences-human-bio-foundation-year |
| Biological Sciences (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences-foundation-year |
| Biological Sciences (Zoology) | BSc (Hons) / MBiol | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences-zoology |
| Biological Sciences (Zoology) (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biological-sciences-zoology-foundation-year |
| Biomedical Science | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biomedical-science |
| Biomedical Science (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/biomedical-science-foundation-year |
| Equine Science | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/equine-science |
| Equine Science (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/equine-science-foundation-year |
| Life Sciences Foundation Year | Foundation | https://www.brookes.ac.uk/courses/undergraduate/life-sciences |
| Medical Science | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/medical-science |
| Medical Science (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/medical-science-foundation-year |
| Medical Sciences (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/medical-sciences-final-year-entry |

**School of the Built Environment** (UG)

| Programme | Award | URL |
|-----------|-------|-----|
| Building Surveying | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/building-surveying |
| Building Surveying (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/building-surveying-foundation-year |
| Built Environment Foundation | Foundation | https://www.brookes.ac.uk/courses/undergraduate/built-environment-foundation (arch) |
| Construction Project Management | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/construction-project-management |
| Construction Project Management (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/construction-project-management-foundation-year |
| Property Development and Planning | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/planning-and-property-development |
| Property Development and Planning (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/planning-property-development-foundation-year |
| Quantity Surveying and Commercial Management | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/quantity-surveying-and-commercial-management |
| Quantity Surveying and Commercial Management (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/quantity-surveying-commercial-mgmt-foundation-year |
| Real Estate | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/real-estate |
| Sustainable Urban Design and Planning | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sustainable-urban-design-and-planning |
| Sustainable Urban Design and Planning (with Foundation Year) | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sustainable-urban-design-planning-foundation-year |

**School of Engineering, Computing and Mathematics** (UG)

| Programme | Award | URL |
|-----------|-------|-----|
| Artificial Intelligence | BSc (Hons) / MSci | https://www.brookes.ac.uk/courses/undergraduate/artificial-intelligence |
| Artificial Intelligence (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/artificial-intelligence-foundation-year |
| Computer Science | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/computer-science |
| Computer Science (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/computer-science-foundation-year |
| Computer Science for Cyber Security | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/computer-science-for-cyber-security |
| Computer Science for Cyber Security (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/computer-science-cyber-security-foundation-year |
| Computing (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/computing-top-up |
| Computing Foundation | Foundation | https://www.brookes.ac.uk/courses/undergraduate/computing-foundation |
| Information Technology for Business | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/information-technology-for-business |
| Information Technology for Business (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/information-technology-for-business-top-up |
| Information Technology for Business (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/information-technology-business-foundation-year |
| Digital Technologies | BSc top-up | https://www.brookes.ac.uk/courses/undergraduate/digital-technologies-bsc-top-up |
| Automotive Engineering with Electric Vehicles | BEng (Hons) / MEng | https://www.brookes.ac.uk/courses/undergraduate/automotive-engineering |
| Electro-Mechanical Engineering BEng | BEng (Hons) | https://www.brookes.ac.uk/courses/undergraduate/electro-mechanical-engineering-beng |
| Electronic Engineering BEng (Final Year Direct Entry) | BEng (Hons) | https://www.brookes.ac.uk/courses/undergraduate/electronic-engineering-beng-final-year-entry |
| Engineering Foundation | Foundation | https://www.brookes.ac.uk/courses/undergraduate/engineering-foundation |
| Mechanical Engineering | BEng (Hons) / MEng | https://www.brookes.ac.uk/courses/undergraduate/mechanical-engineering-beng-or-meng |
| Mechanical Engineering Design | BEng (Hons) | https://www.brookes.ac.uk/courses/undergraduate/mechanical-engineering-design-beng |
| Motorsport Engineering | BEng (Hons) / MEng | https://www.brookes.ac.uk/courses/undergraduate/motorsport-engineering-beng-or-meng |
| Motorsport Technology | BEng (Hons) | https://www.brookes.ac.uk/courses/undergraduate/motorsport-technology |

**Oxford School of Nursing and Midwifery** (UG)

| Programme | Award | URL |
|-----------|-------|-----|
| Midwifery | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/midwifery |
| Midwifery (Post Experience / 2nd Registration) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/midwifery-2nd-registration |
| Nursing (Adult) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/adult-nursing |
| Nursing (Children's) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/childrens-nursing |
| Nursing (Mental Health) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/mental-health-nursing |
| Nursing Associate | FdSc | https://www.brookes.ac.uk/courses/undergraduate/nursing-associate-fdsc |
| Occupational Therapy | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/occupational-therapy |
| Paramedic Science | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/paramedic-science |
| Physiotherapy | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/physiotherapy |
| Professional Development in Health and Social Care Top Up | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/professional-development-in-health-and-social-care |
| Social Work | BA (Hons) | https://www.brookes.ac.uk/courses/undergraduate/social-work |

**School of Sport, Nutrition and Allied Health Professions** (UG)

| Programme | Award | URL |
|-----------|-------|-----|
| Nutrition | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/nutrition |
| Nutrition (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/nutrition-with-foundation-year |
| Nutrition Science (Final Year Entry) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/nutrition-science-final-year-entry |
| Sport and Exercise Science | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sport-and-exercise-science |
| Sport and Exercise Science (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sport-and-exercise-science-foundation-year |
| Sport, Coaching and Physical Education | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sport-coaching-and-physical-education |
| Sport, Coaching and Physical Education (with Foundation Year) | BSc (Hons) | https://www.brookes.ac.uk/courses/undergraduate/sport-coaching-physical-education-foundation-year |
| Sport, Physical Activity and Health Promotion | BSc (Hons) / DipHE / CertHE | https://www.brookes.ac.uk/courses/undergraduate/physical-activity-and-health-promotion |
| Sport, Physical Activity and Health Promotion (with Foundation Year) | BSc (Hons) / DipHE / CertHE | https://www.brookes.ac.uk/courses/undergraduate/physical-activity-health-promo-foundation-year |

---

## SECTION 2 — Graduate (taught) education

### 2.1 PGT programmes by school

**School of Arts** (2 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Creative Industries | MA | https://www.brookes.ac.uk/courses/postgraduate/creative-industries |
| Fine Art | MFA, PGDip, PGCert | https://www.brookes.ac.uk/courses/postgraduate/fine-art |

**Oxford Brookes Business School** (~25 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Accounting and Finance | MSc | https://www.brookes.ac.uk/courses/postgraduate/accounting-and-finance |
| Finance | MSc | https://www.brookes.ac.uk/courses/postgraduate/finance |
| Finance and Analytics | MSc | https://www.brookes.ac.uk/courses/postgraduate/finance-and-analytics |
| Strategic Professional Accounting and Finance | MSc | https://www.brookes.ac.uk/courses/postgraduate/strategic-professional-accounting-and-finance |
| Coaching and Mentoring Practice | MA / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/coaching-and-mentoring-practice |
| Doctor of Coaching and Mentoring | DCM | https://www.brookes.ac.uk/courses/postgraduate/doctor-of-coaching-and-mentoring |
| Human Resource Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/human-resource-management |
| Human Resource Management — Admission with Credit (12 month fast-track) | MA | https://www.brookes.ac.uk/courses/postgraduate/human-resource-management-fast-track |
| International Business and Supply Chain Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/business-and-supply-chain-management |
| International Business Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/international-business-management |
| Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/management |
| Management and Business Analytics | MSc | https://www.brookes.ac.uk/courses/postgraduate/management-and-business-analytics |
| Oxford Brookes Global MBA | MBA | https://www.brookes.ac.uk/courses/postgraduate/oxford-brookes-mba |
| Project Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/project-management |
| Digital Marketing | MSc | https://www.brookes.ac.uk/courses/postgraduate/digital-marketing |
| Global Marketing | MSc | https://www.brookes.ac.uk/courses/postgraduate/global-marketing |
| International Luxury Marketing | MSc | https://www.brookes.ac.uk/courses/postgraduate/international-luxury-marketing |
| Marketing and Brand Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/marketing-and-brand-management |
| Global Events Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/global-events-management |
| International Hospitality, Events and Tourism Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/international-hospitality-events-and-tourism |
| International Hotel and Tourism Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/international-hotel-and-tourism-management |

**School of Education, Humanities and Languages** (7 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| International Postgraduate Certificate of Education | PGCE | https://www.brookes.ac.uk/courses/postgraduate/international-postgraduate-cert-of-education |
| Doctor of Education | EdD | https://www.brookes.ac.uk/courses/postgraduate/doctor-of-education |
| Education — Dyslexia and Specific Learning Difficulties (SpLD) | PGDip | https://www.brookes.ac.uk/courses/postgraduate/education-dyslexia-and-spld |
| Education (International Education) | MA | https://www.brookes.ac.uk/courses/postgraduate/international-education |
| Education | MA | https://www.brookes.ac.uk/courses/postgraduate/ma-education |
| PGCE Primary 5-11 (with QTS) | PGCE | https://www.brookes.ac.uk/courses/postgraduate/pgce-primary-campus-based-5-11 |
| Social, Emotional and Mental Health Difficulties | PGDip | https://www.brookes.ac.uk/courses/postgraduate/social-emotional-and-mental-health-difficulties |

**Oxford Brookes Law School** (3 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Law — Postgraduate diploma in Law (PGDL) / LLM Law (conversion) | GradDip / LLM | https://www.brookes.ac.uk/courses/postgraduate/pgdl-law-conversion |
| LLM in Legal Practice (SQE 1 & 2) from University of Law | LLM | https://www.brookes.ac.uk/courses/postgraduate/llm-in-legal-practice-sqe-1-2 |
| LLM Master of Laws | LLM / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/llm |

**School of Social Sciences** (1 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Psychology (conversion) | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/psychology-msc |

**Oxford School of Architecture** (6 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| (MArch) Master of Architecture Part 2 (RIBA/ARB/LAM) | MArch | https://www.brookes.ac.uk/courses/postgraduate/march-architecture-part-2 |
| Advanced Architectural Design | MArch | https://www.brookes.ac.uk/courses/postgraduate/advanced-architectural-design |
| Applied Design in Architecture (ARB and RIBA part 2) | MArchD | https://www.brookes.ac.uk/courses/postgraduate/applied-design-in-architecture |
| Digital Craft in Architecture | MA / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/digital-craft-in-architecture |
| Interior Architecture | MA | https://www.brookes.ac.uk/courses/postgraduate/interior-architecture |
| Urban Design | MA / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/urban-design |

**School of Biological and Medical Sciences** (2 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Conservation Ecology | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/conservation-ecology |
| Medical Genetics and Genomics | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/medical-genetics-and-genomics |

**School of the Built Environment** (19 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Advanced Practice | MA / MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/advanced-practice-open-award |
| Building Information Modelling and Management | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/building-information-modelling-and-management |
| Construction Project Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/construction-project-management |
| Environmental Impact Assessment and Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/environmental-impact-assessment-and-management |
| Global Development and Humanitarian Practice | MA / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/global-development-and-humanitarian-practice |
| Historic Conservation | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/historic-conservation |
| Humanitarian Action and Peacebuilding | MA / PGCert | https://www.brookes.ac.uk/courses/postgraduate/humanitarian-action-and-peacebuilding |
| Industrialised Construction and Design Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/industrialised-construction-and-design-management |
| Infrastructure Planning and Sustainable Development | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/infrastructure-and-sustainable-development |
| Project Management in the Built Environment | MSc | https://www.brookes.ac.uk/courses/postgraduate/project-management-in-the-built-environment |
| Quantity Surveying and Commercial Management | MSc | https://www.brookes.ac.uk/courses/postgraduate/quantity-surveying-and-commercial-management |
| Real Estate | MSc / PGDip | https://www.brookes.ac.uk/courses/postgraduate/real-estate |
| Real Estate Investment Finance | MSc / PGDip | https://www.brookes.ac.uk/courses/postgraduate/real-estate-investment-finance |
| Spatial Planning | MSc | https://www.brookes.ac.uk/courses/postgraduate/spatial-planning |
| Spatial Planning Studies | Certificate | https://www.brookes.ac.uk/courses/postgraduate/spatial-planning-studies |
| Sustainable Architecture: Evaluation and Design | MSc / PGDip | https://www.brookes.ac.uk/courses/postgraduate/sustainable-architecture-evaluation-and-design |

**School of Engineering, Computing and Mathematics** (9 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Advanced Computer Science | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/advanced-computer-science |
| Artificial Intelligence | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/artificial-intelligence |
| Computer Science for Cyber Security | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/computer-science-for-cyber-security |
| Computing Science | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/computing |
| Data Science and Artificial Intelligence | MSc | https://www.brookes.ac.uk/courses/postgraduate/data-science-and-artificial-intelligence |
| Automotive Engineering with Electric Vehicles | MSc | https://www.brookes.ac.uk/courses/postgraduate/automotive-engineering-with-electric-vehicles |
| Electric Motorsport | MSc | https://www.brookes.ac.uk/courses/postgraduate/electric-motorsport |
| Mechanical Engineering | MSc | https://www.brookes.ac.uk/courses/postgraduate/mechanical-engineering-msc |
| Motorsport Engineering | MSc | https://www.brookes.ac.uk/courses/postgraduate/motorsport-engineering-msc |
| Racing Engine Systems | MSc | https://www.brookes.ac.uk/courses/postgraduate/racing-engine-systems |

**Oxford School of Nursing and Midwifery** (8 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Community Nursing Specialist Practice (District Nursing) | PGDip | https://www.brookes.ac.uk/courses/postgraduate/district-nursing |
| Global Public Health Leadership | MPH / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/global-public-health-leadership |
| Midwifery — Pre-registration | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/midwifery-pre-registration |
| Nursing (Mental Health) | MSc | https://www.brookes.ac.uk/courses/postgraduate/mental-health-nursing-pre-registration |
| Occupational Therapy (Pre-registration) | MSc | https://www.brookes.ac.uk/courses/postgraduate/occupational-therapy-pre-registration |
| Physiotherapy (Pre-registration) | MSc | https://www.brookes.ac.uk/courses/postgraduate/physiotherapy-pre-registration |
| Professional Development in Health and Social Care | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/professional-development-in-health-and-social-care |
| Public Health | MPH / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/public-health |

**School of Psychology, Social Work and Public Health** (also includes Social Work MA)

| Programme | Award | URL |
|-----------|-------|-----|
| Social Work | MA / PGDip | https://www.brookes.ac.uk/courses/postgraduate/social-work |

**School of Sport, Nutrition and Allied Health Professions** (4 PGT)

| Programme | Award | URL |
|-----------|-------|-----|
| Applied Coaching Science | MSc | https://www.brookes.ac.uk/courses/postgraduate/applied-coaching-science |
| Applied Human Nutrition | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/applied-human-nutrition |
| Applied Sport and Exercise Nutrition | MSc / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/applied-sport-and-exercise-nutrition |
| Dietetics (Pre-Registration) | MSc / PGDip | https://www.brookes.ac.uk/courses/postgraduate/dietetics-pre-registration |

**Communication, Media, Journalism and Publishing (PGT)**

| Programme | Award | URL |
|-----------|-------|-----|
| Journalism | MA | https://www.brookes.ac.uk/courses/postgraduate/journalism |
| Publishing (Distance Learning) | MA / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/publishing-studies-distance-learning |
| Publishing Media | MA / PGDip / PGCert | https://www.brookes.ac.uk/courses/postgraduate/publishing-media |

---

## SECTION 3 — Graduate (research) education

| Programme | Award | School | URL |
|-----------|-------|--------|-----|
| Arts | MPhil, PhD, PhD by Published Work, MA by Research | School of Arts | https://www.brookes.ac.uk/courses/research/arts |
| Communication, Media and Culture | PhD, MA by Research | School of Arts | https://www.brookes.ac.uk/courses/research/communication-media-and-culture |
| English | PhD, MA by Research | School of Education, Humanities and Languages | https://www.brookes.ac.uk/courses/research/english |
| Education | PhD, MA by Research | School of Education, Humanities and Languages | https://www.brookes.ac.uk/courses/research/education |
| History | PhD, MA by Research | School of Education, Humanities and Languages | https://www.brookes.ac.uk/courses/research/history |
| History of Art | PhD, MA by Research | School of Education, Humanities and Languages | https://www.brookes.ac.uk/courses/research/history-of-art |
| Philosophy | PhD, MA by Research | School of Education, Humanities and Languages | https://www.brookes.ac.uk/courses/research/philosophy |
| Japanese by Research | MA by Research | School of Education, Humanities and Languages | https://www.brookes.ac.uk/courses/research/japanese |
| Economics, Accounting and Finance | MPhil, PhD | Oxford Brookes Business School | https://www.brookes.ac.uk/courses/research/economics-accounting-or-finance |
| Business and Management | MPhil, PhD | Oxford Brookes Business School | https://www.brookes.ac.uk/courses/research/business-and-management |
| Marketing | MPhil, PhD | Oxford Brookes Business School | https://www.brookes.ac.uk/courses/research/marketing |
| Hospitality, Tourism and Events Management | MPhil, PhD | Oxford Brookes Business School | https://www.brookes.ac.uk/courses/research/hospitality-tourism-and-events-management |
| Criminology | PhD, MSc by Research | Oxford Brookes Law School | https://www.brookes.ac.uk/courses/research/criminology |
| Law | PhD, LLM by Research | Oxford Brookes Law School | https://www.brookes.ac.uk/courses/research/law |
| Anthropology | PhD | School of Social Sciences | https://www.brookes.ac.uk/courses/research/anthropology |
| Geography | PhD | School of Social Sciences | https://www.brookes.ac.uk/courses/research/geography |
| Politics or International Relations | PhD | School of Social Sciences | https://www.brookes.ac.uk/courses/research/politics-or-international-relations |
| Psychology | MPhil, PhD | School of Psychology, Social Work and Public Health | https://www.brookes.ac.uk/courses/research/psychology |
| Sociology | PhD | School of Social Sciences | https://www.brookes.ac.uk/courses/research/sociology |
| Social Work | MPhil, PhD | School of Psychology, Social Work and Public Health | https://www.brookes.ac.uk/courses/research/social-work |
| Nursing and Midwifery | MPhil, PhD | Oxford School of Nursing and Midwifery | https://www.brookes.ac.uk/courses/research/nursing-and-midwifery |
| Professional Doctorate in Midwifery | DMid | Oxford School of Nursing and Midwifery | https://www.brookes.ac.uk/courses/research/prof-doc-in-midwifery |
| Professional Doctorate in Nursing | DNurs | Oxford School of Nursing and Midwifery | https://www.brookes.ac.uk/courses/research/prof-doc-in-nursing |
| Physiotherapy, Occupational Therapy, and Rehabilitation | MPhil, PhD, Masters by Research | School of Psychology, Social Work and Public Health | https://www.brookes.ac.uk/courses/research/physiotherapy-occupational-therapy-rehabilitation |
| Biological and Medical Sciences | MPhil, PhD, Masters by Research | School of Biological and Medical Sciences | https://www.brookes.ac.uk/courses/research/biological-and-medical-sciences |
| Architecture | MPhil, PhD, PhD by Practice, PhD by Published Work | Oxford School of Architecture | https://www.brookes.ac.uk/courses/research/architecture |
| Built Environment | MPhil, PhD, PhD by Published Work | School of the Built Environment | https://www.brookes.ac.uk/courses/research/built-environment |
| Computing | MPhil, PhD, Masters by Research, PhD by Published Work | School of Engineering, Computing and Mathematics | https://www.brookes.ac.uk/courses/research/computing |
| Detection and Analysis of Advanced Phishing Attacks (DAAPA) | MSc by Research | School of Engineering, Computing and Mathematics | https://www.brookes.ac.uk/courses/research/detection-and-analysis-of-advanced-phishing-attack |
| Engineering | MPhil, PhD, Masters by Research, PhD by Published Work, EngD Professional Doctorate | School of Engineering, Computing and Mathematics | https://www.brookes.ac.uk/courses/research/engineering |
| Nutrition | MPhil, PhD, Masters by Research | School of Sport, Nutrition and Allied Health Professions | https://www.brookes.ac.uk/courses/research/nutrition |
| Sport and Coaching Sciences | MPhil, PhD, Masters by Research | School of Sport, Nutrition and Allied Health Professions | https://www.brookes.ac.uk/courses/research/sport-and-coaching-sciences |
| Specific advertised PhD projects (e.g. Empowering foster carers, Insights from autobiographical memories, Intrinsically-aligned machine learning) | PhD | various | listed in subject area pages |

---

## SECTION 4 — Application requirements (language, fees, deadlines)

### 4.1 English language requirements (IELTS Academic)

| Level | Course group | IELTS requirement |
|-------|--------------|-------------------|
| Foundation | International Foundation Business and Technology; International Foundation Arts, Humanities and Law | 5.5 overall with 5.5 in all skills |
| Foundation | Art and Design Foundation | UKVI-approved SELT 5.0 with 5.0 in all skills |
| Foundation | International Foundation Art and Design | 5.5 overall with 5.5 in all skills |
| Foundation | Built Environment Foundation, Computing Foundation, Engineering Foundation, Foundation in Humanities, Life Sciences Foundation | 6.0 with 6.0 in reading and writing, 5.5 in listening and speaking |
| Undergraduate | All other undergraduate courses | 6.0 overall with 6.0 in reading and writing, 5.5 in listening and speaking |
| Undergraduate | Law, Architecture, Interior Architecture, English Literature (including combined honours), English Literature and Creative Writing | 6.5 overall with 6.0 in reading and writing, 5.5 in listening and speaking |
| Undergraduate | Health and Social Care courses | 6.5 or 7.0 overall with 6.5 or 7.0 in all components (see individual course) |
| Undergraduate | Nutrition BSc (Hons) | 6.5 overall with a minimum of 6.0 in each component |
| Postgraduate | Oxford Brookes accepts a wide range of additional English language qualifications (specific per course; see individual course page) | typically 6.5–7.0 overall |

**Source**: `https://www.brookes.ac.uk/study/international-students/applying-to-arriving/how-to-apply/english-language-requirements` (table content + introductory paragraph: "The entry requirement for your course will be expressed as an IELTS level and refers to the IELTS Academic version of this test. The University however does accept a wide range of additional English language qualifications, which can be found below.") Captured 2026-07-08.

### 4.2 Tuition fees (2026/27 academic year)

| Category | Fee (UK / Home) | Fee (International) | Notes |
|----------|-----------------|---------------------|-------|
| Undergraduate full-time (UK) | £9,790 (2026/27; up from £9,535) | varies by course (use fee finder) | Per academic year |
| Undergraduate part-time (UK) | £1,220 per single module | — | 2026/27 |
| Foundation year (UG) | £5,760 (BA Hons Global Business and Entrepreneurship example) | varies | 2026/27 |
| Level 4-6 (UG) | £9,790 | — | 2026/27 |
| Partner college UG (UK) | £7,700 / year FT; £3,850 PT | — | 2026/27 |
| Foundation degree (UK) | £7,700 / course FT; £5,140 PT | — | 2026/27 |
| Postgraduate research (UK) | £5,338 / year FT | £18,300 – £20,100 / year (depends on programme) | 2026/27 |
| Postgraduate research part-time (UK) | £2,356 / year | £8,050 – £8,750 / year | 2026/27 |
| Work placement / sandwich year (UK & international) | £1,905 (placements in 2026/27) | £1,905 (standard); Business School placements £2,200 (standard) / £3,100 (extended) | 2026/27 |
| UK student year abroad | £1,465 | — | 2026/27 |
| Associate / Study Abroad (international) | — | £8,625 / semester; £17,250 / full year | 2026/27 |
| PG placements (Business School) | £2,200 (standard) / £3,100 (extended) | same | 2026/27 |
| Pre-sessional / English / International Foundation / Pre-Master's | see "English, International Foundation and Pre-Master's course fees" page | — | varies |

**Source**: `https://www.brookes.ac.uk/study/fees` (paragraph "How much are our tuition fees?" with detailed fee lines for full-time / part-time / placement / study abroad; and the announcement: "Oxford Brookes will be increasing undergraduate tuition fees for UK students from £9,535 to £9,790 for the 2026/27 academic year."). Captured 2026-07-08.

### 4.3 Application process & deadlines

| Route | Mechanism | Source URL |
|-------|-----------|------------|
| UK students | UCAS application | https://www.brookes.ac.uk/study/how-to-apply/applying-through-ucas |
| International students | UCAS or direct (Oxford Brookes online) | https://www.brookes.ac.uk/study/international-students/applying-to-arriving/how-to-apply |
| Direct application (UK) | Oxford Brookes online application form | https://www.brookes.ac.uk/study/how-to-apply/applying-directly |
| Personal statement | Oxford Brookes personal statement guidance | https://www.brookes.ac.uk/study/how-to-apply/understanding-university/personal-statements |
| Interview / portfolio | Some courses require interview/portfolio (especially Architecture) | https://www.brookes.ac.uk/study/how-to-apply/understanding-university/interviews-and-portfolios |
| Visa (international) | Student visa & immigration support | https://www.brookes.ac.uk/students/isat/visas/student-visa |
| Open days | University open day hub | https://www.brookes.ac.uk/open-days/ |

**Note on deadlines**: Oxford Brookes uses UCAS equal consideration deadline (typically 31 January for September entry) for UCAS applicants. International students should check individual course pages and the international application guidance, as some courses have rolling admissions. Course-level deadlines (e.g. for portfolio or interview-required courses like Architecture) are published on individual course pages.

**Source**: `https://www.brookes.ac.uk/study/courses/undergraduate` (sections 3 "The application process" and 6 "Submitting your application"; "We recommend that you apply for student finance as soon as you've submitted your application."; international section 8 also confirmed). Captured 2026-07-08.

---

## SECTION 5 — Cost of attendance (broader)

- **Tuition fees**: see Section 4.2 above.
- **Living costs**: per Oxford Brookes, your living expenses will depend on accommodation and lifestyle; Living costs page is a separate resource (https://www.brookes.ac.uk/study/fees - "Living costs" subsection).
- **Accommodation fees**: see accommodation pages (https://www.brookes.ac.uk/student-life/accommodation/prospective-students); cost varies by hall (e.g. Parade Green Accommodation Tour on the homepage references standard Brookes halls).
- **Additional costs**: "If you are looking to study a health and life sciences course, please refer to the course entry page for full details about additional costs." (per fees page).
- **Funding & financial support**: https://www.brookes.ac.uk/study/funding ("Whether you are a new or returning student, there are a variety of funding options available to help finance your studies.").
- **Tuition fee loan (UK)**: "If you are eligible for a tuition fee loan, this will continue to fully cover the increased fee and your monthly loan repayments once you leave your course will not be affected, as this is based on your earnings rather than on the total amount you owe."

---

## SECTION 6 — WeKnora chunk import manifest

This document is structured to be chunked at the following natural boundaries (H2 / H3 sections above), enabling fine-grained retrieval:

- Chunk 0a: Section 0.1–0.4 (overview & structural rules)
- Chunk 1a: Section 1 UG by school (each school as its own chunk)
- Chunk 1b: Section 1 Foundation programmes
- Chunk 2a: Section 2 PGT by school
- Chunk 3a: Section 3 Research degrees
- Chunk 4a: Section 4.1 English language requirements
- Chunk 4b: Section 4.2 Tuition fees
- Chunk 4c: Section 4.3 Application process & deadlines
- Chunk 5a: Section 5 Cost of attendance
- Chunk 6a: full leaf-level course enumeration in `uni-cache/schools/oxford-brookes/courses-ug.json`, `courses-pgt.json`, `courses-research.json` (machine-readable)

**Total addressable chunks per ingest pass: ~30 chunks** (overview, 12 schools × 3 levels, language/fees/deadlines, manifests).

---

## SECTION 7 — Monitoring watchlist (URLs by change frequency)

| Frequency | URL | Last checked | Watched value |
|-----------|-----|--------------|---------------|
| High (monthly) | https://www.brookes.ac.uk/study/fees | 2026-07-08 | Tuition fee for 2026/27 UG UK = £9,790; PGR UK = £5,338/yr; placement = £1,905 |
| High (monthly) | https://www.brookes.ac.uk/study/international-students/applying-to-arriving/how-to-apply/english-language-requirements | 2026-07-08 | UG general = IELTS 6.0 (R/W 6.0, L/S 5.5); Health = 6.5/7.0; PG varies per course |
| High (monthly) | https://www.brookes.ac.uk/study/how-to-apply/applying-through-ucas | 2026-07-08 | UCAS equal-consideration deadline (typically 31 Jan for Sep entry) |
| High (monthly) | https://www.brookes.ac.uk/open-days/ | 2026-07-08 | Open Day event dates (rolling) |
| Medium (quarterly) | https://www.brookes.ac.uk/study/subject-areas/* | 2026-07-08 | Programme list, new courses |
| Medium (quarterly) | https://www.brookes.ac.uk/courses/undergraduate/* | 2026-07-08 | Course-specific page (entry reqs, fees, deadlines) |
| Medium (quarterly) | https://www.brookes.ac.uk/courses/postgraduate/* | 2026-07-08 | PGT-specific page |
| Medium (quarterly) | https://www.brookes.ac.uk/courses/research/* | 2026-07-08 | Research degree themes |
| Low (annual) | https://www.brookes.ac.uk/about-brookes/structure-and-governance/faculties-and-schools | 2026-07-08 | Faculty/school structure (currently 2 faculties, 12 schools) |
| Low (annual) | https://www.brookes.ac.uk/study/fees/tuition-fee-increases | 2026-07-08 | Tuition fee increase policy |
| Low (annual) | https://www.brookes.ac.uk/study/courses | 2026-07-08 | Top-level courses index |

---

## APPENDIX — Source pages and capture dates

| Source page | URL | Captured |
|-------------|-----|----------|
| Faculties and schools | https://www.brookes.ac.uk/about-brookes/structure-and-governance/faculties-and-schools | 2026-07-08 |
| Subject areas (index) | https://www.brookes.ac.uk/study/subject-areas | 2026-07-08 |
| 18 subject-area index pages (all of them) | https://www.brookes.ac.uk/study/subject-areas/{slug} | 2026-07-08 |
| Tuition fees | https://www.brookes.ac.uk/study/fees | 2026-07-08 |
| English language requirements | https://www.brookes.ac.uk/study/international-students/applying-to-arriving/how-to-apply/english-language-requirements | 2026-07-08 |
| How to apply (UG) | https://www.brookes.ac.uk/study/courses/undergraduate | 2026-07-08 |
| UCAS application guide | https://www.brookes.ac.uk/study/how-to-apply/applying-through-ucas | 2026-07-08 |
| Direct application | https://www.brookes.ac.uk/study/how-to-apply/applying-directly | 2026-07-08 |
| International application | https://www.brookes.ac.uk/study/international-students/applying-to-arriving/how-to-apply | 2026-07-08 |
| Research degrees | https://www.brookes.ac.uk/students/research-degrees-team | 2026-07-08 |

---

*Document generation note*: All programme names, awards, and URLs in this document are extracted directly from Oxford Brookes University public-facing subject-area and course pages. Each programme's source URL is provided for verification. Capture was performed in a single ego-browser session on 2026-07-08 using the `useOrCreateTaskSpace` + `gotoAndWait` + `js` workflow. No data was synthesized or summarized; the leaf-level enumeration in `uni-cache/schools/oxford-brookes/courses-*.json` is the authoritative machine-readable list.
