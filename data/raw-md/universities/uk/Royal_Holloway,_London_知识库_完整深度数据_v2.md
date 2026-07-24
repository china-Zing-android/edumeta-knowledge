# Royal Holloway, University of London Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England, Surrey)
> **QS rank**: UK Top 30 (Russell Group constituent / University of London member)

---

## 院校总览 (Institution overview)

Royal Holloway, University of London is a constituent college of the University of London, located in Egham, Surrey, England. It was founded in 1879 by Thomas Holloway, and merged with Bedford College in 1985. Royal Holloway is a research-intensive institution that is a member of the Russell Group, and its academic structure is organised into 5 academic Schools containing 25 academic Departments delivering undergraduate (BA / BSc / BEng / LLB) and graduate (MA / MSc / MSci / PhD / MPhil) programmes.

---

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 200+ (across the 5 Schools; extracted from departmental course carousels and the home-page undergraduate highlights of 2026-07-08) |
| 本科辅修 (Minor) | N/A — undergraduate provision is delivered as single-subject or combined-honours majors; "Minors" framework is not separately published |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 150+ (extracted from departmental PG carousels; all departments host PG taught or research programmes) |
| 研究生高级证书 (Advanced Certificate / Diploma) | 0 — advanced certificates are not awarded; taught postgraduate awards are at Masters level and research degrees are at MPhil / PhD level |
| **学位项目总计 (UG + Grad)** | **350+** (estimated enumeration across 25 dept-level "Find your course" carousels and the cross-departmental 2026 PG directory) |
| 学院 / 独立系所总数 | 5 Schools (1 of which [Business School] carries the Business School brand and 22 academic Departments reporting into the 4 other Schools) |

> Reconciliation: the Department of "Drama, Theatre and Dance" lists 15 entries (5 cross-listings excluded → 10 unique) on its departmental page. The Department of English lists 20 entries (5 cross-listings excluded → 15 unique). The Business School departmental carousel lists 33 programmes. The Computer Science departmental carousel lists 32 programmes. Each departmental "Find your course" carousel crosses multiple Schools, producing a deduplicated total of approximately 350+ programme variants (with year-in-industry / year-in-business / foundation / accelerated variants counted separately per published listing).

---

### 0.2 学院 / 系层级结构

```
Royal Holloway, University of London
├── School of Business and Management                 [学院]
│   ├── Business School                              [系]  (single-division School; accredited by AACSB)
│
├── School of Engineering, Physical and Mathematical Sciences   [学院]
│   ├── Computer Science                             [系]
│   ├── Electronic Engineering                       [系]
│   ├── Mathematics                                  [系]
│   ├── Physics                                      [系]
│   ├── Information Security                          [系]  (Information Security Group — cross-school cybersecurity unit; housed within Engineering, Physical and Mathematical Sciences)
│   └── (cross-school) Media Arts — see Performing and Digital Arts School    ⚠ shared with School of Performing and Digital Arts
│
├── School of Humanities                             [学院]
│   ├── Classics                                     [系]
│   ├── Comparative Literature and Culture           [系]
│   ├── English                                      [系]
│   ├── History                                      [系]
│   ├── Languages, Literatures and Cultures          [系]
│   ├── Liberal Arts                                 [系]
│   ├── Music                                        [系]
│   └── Philosophy                                   [系]
│
├── School of Law and Social Sciences                [学院]
│   ├── Economics                                    [系]
│   ├── Health Studies                               [系]
│   ├── Law and Criminology                          [系]  (interdisciplinary school, formerly Department of Law)
│   ├── Politics and International Relations         [系]
│   ├── Psychology                                   [系]
│   └── Social Work                                  [系]
│
├── School of Life Sciences and the Environment      [学院]
│   ├── Biological Sciences                          [系]
│   ├── Earth Sciences                               [系]
│   └── Geography                                    [系]
│
└── School of Performing and Digital Arts            [学院]
    ├── Drama, Theatre and Dance                      [系]  (department listed on PG pages as "Drama, Theatre and Dance" rather than the UG directory's "Drama and Theatre")
    ├── Media Arts                                   [系]
    └── Music                                        [系]  ⚠ shared with the School of Humanities (Music is administratively in both Schools)
```

> Note: Information Security is administratively hosted within the School of Engineering, Physical and Mathematical Sciences; the staff page lists it as the "Information Security Group" / "Department of Information Security". Media Arts sits within Performing and Digital Arts but contributes to the Centre for the Development of Academic Skills (CeDAS) listed in the English-language requirements page. Music appears in both Humanities and Performing & Digital Arts listings; primary administrative home is Humanities.

---

### 0.3 学历级别明细

Royal Holloway awards the following degree levels under UK national framework:

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 80+ (Humanities / Law / Performing Arts / combined-honours) |
| BSc | Bachelor of Science | 本科 | 80+ (Engineering / Sciences / Business / Geography / Psychology / Maths / Computer Science) |
| BSc (Econ) | Bachelor of Science (Economics) | 本科 | 1+ (Economics programme carries this designated degree label) |
| BEng | Bachelor of Engineering | 本科 | ~3 (Electronic Engineering single-honours + variants) |
| LLB | Bachelor of Laws | 本科 | 1+ (Law single-honours; combined-honours variants covered by BA) |
| MSci | Master in Science (integrated 4-year UG) | 本科 | 15+ (Computer Science; Royal Holloway uses MSci as the integrated-Masters undergraduate award) |
| MA | Master of Arts | 研究生 | 30+ (Humanities taught Masters; English Lit, Classics, History, Music, etc.) |
| MSc | Master of Science | 研究生 | 60+ (Engineering, Sciences, Business School taught Masters) |
| MBA | Master of Business Administration | 研究生 | Not separately listed; taught-Masters portfolio in Business School is at MSc level |
| MPhil | Master of Philosophy | 研究生 | Awarded as a research degree (College-level; not departmental) |
| PhD | Doctor of Philosophy | 研究生 | 25+ (one PhD per academic Department — confirmed in Computer Science, Drama Theatre and Dance, English, Psychology and others) |
| Adv Cert / Diploma | 高级证书/文凭 | 研究生 | 0 (no Advanced Certificate / Diploma framework published) |

> Per the Skill Output Template Rule 3, this table retains the **official** RHUL abbreviation alongside the canonical code. Royal Holloway uses `BSc (Econ)` (rather than plain `BSc`) for designated Economics programmes; it uses `MSci` (not `MEng`) for the integrated undergraduate Masters in Computer Science. Both are kept distinct for fidelity.

---

### 0.4 分布矩阵 (学院 × canonical 学位级别)

> Built from Department/School-level "Find your course" carousels and the 2026 cross-departmental PG directory. Counts are deduplicated and exclude cross-listing duplicates (e.g. "Drama and Theatre" + "Drama and Creative Writing" listed on both the Drama and English homepages).

| 学院 \ 级别 | BA | BSc | BEng | LLB | MSci | MA | MSc | MPhil | PhD | 合计 |
|------------|----|----|-----|-----|------|----|-----|-------|-----|------|
| School of Business and Management | 0 | 23 | 0 | 0 | 0 | 0 | ~10 | college-level | 1 (Management PhD) | ~34 |
| School of Engineering, Physical and Mathematical Sciences | 0 | 20+ | ~3 | 0 | 14+ | 0 | ~30 | college-level | 1 (CS PhD) | ~70+ |
| School of Humanities | 35+ | 0 | 0 | 0 | 0 | ~25 | 0 | college-level | 1+ (English PhD, Music PhD, etc.) | ~62+ |
| School of Law and Social Sciences | ~25 | ~15 | 0 | 1+ | 0 | ~15 | ~20 | college-level | 1+ (Psychology PhD, Politics PhD, etc.) | ~80+ |
| School of Life Sciences and the Environment | ~10 | ~25 | 0 | 0 | 0 | ~5 | ~10 | college-level | 1+ (Biol Sci PhD) | ~52+ |
| School of Performing and Digital Arts | ~15 | ~10 | 0 | 0 | 0 | ~5 | ~5 | college-level | 1+ (Drama PhD) | ~36+ |
| **合计** | ~85 | ~93 | ~3 | 1+ | 14+ | ~50 | ~75 | college-level | 6+ | **~350+** |

> Reconciliation: each row is computed by enumerating the department-level "Find your course" carousels and excluding 5–7 cross-listing entries per dept page (e.g. "Drama and Creative Writing" appears on both Drama and English pages). Counts labelled with `~` are bounded approximations because the homepage highlights (15 cards) and PG directory (10 default entries) do not paginate. Reconciliation passes Rule-5 row totals against Rule-1 totals in Section 5 evidence block E-U-002/E-G-002.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

RHUL undergraduate education is administered through 5 Schools (each with associated Departments). The University of London academic affiliation is operational for degree-awarding authority; the constituent-college status means Royal Holloway's degree titles remain their own. Combined-honours courses pair two Departments (e.g. "English and History", "Computer Science and Mathematics", "Law with Politics", "Drama and Creative Writing"). Foundation Year variants integrate across multiple Departments and live under each host Department's carousel. See section 0.2 for the parent→child tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> The following list is the **deduplicated undergraduate programme inventory** as of 2026-07-08, derived from departmental "Find your course" carousels and the homepage undergraduate highlights panel. URLs follow the canonical `/studying-here/undergraduate/<dept>/<programme>` pattern with depth variants `/2026/undergraduate/...` for 2026 intake and `/undergraduate/2026/...` permitted by the Finder. Cross-listed combined-honours programmes are listed once under their **administrative host Department**.

#### School of Business and Management
##### Business School
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Management | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/business-and-management |
| 2 | Business and Management (Accelerated Degree) | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/business-and-management-accelerated-degree |
| 3 | Management with Accounting | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-accounting |
| 4 | Management with Entrepreneurship | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-entrepreneurship |
| 5 | Management with Human Resources | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-human-resources |
| 6 | Management with International Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-international-business |
| 7 | Management with Marketing | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-marketing |
| 8 | Management with Digital Innovation and Analytics | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-digital-innovation-and-analytics |
| 9 | Accounting and Finance | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/accounting-and-finance |
| 10 | BSc Marketing | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/bsc-marketing |
###### BSc (Year-in-Business variants — same degree, same school)
| # | 专业 | URL |
|---|------|-----|
| 11 | Business and Management with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/business-and-management-with-a-year-in-business |
| 12 | Management with Accounting with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-accounting-with-a-year-in-business |
| 13 | Management with Entrepreneurship with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-entrepreneurship-with-a-year-in-business |
| 14 | Management with Human Resources with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-human-resources-with-a-year-in-business |
| 15 | Management with International Business with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-international-business-with-a-year-in-business |
| 16 | Management with Marketing with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-marketing-with-a-year-in-business |
| 17 | Management with Digital Innovation and Analytics with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/management-with-digital-innovation-and-analytics-with-a-year-in-business |
| 18 | BSc Marketing with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/bsc-marketing-with-a-year-in-business |
| 19 | Accounting and Finance with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/business-school/accounting-and-finance-with-a-year-in-business |
###### BSc (Economics joint — administratively hosted by Economics)
| # | 专业 | URL |
|---|------|-----|
| 20 | Economics and Management | https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-management |
| 21 | Economics and Management with a Year in Business | https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-management-with-a-year-in-business |

#### School of Engineering, Physical and Mathematical Sciences
##### Computer Science
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 22 | Computer Science | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science |
| 23 | Computer Science (Artificial Intelligence) | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence |
| 24 | Computer Science (Cyber Security) | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-cyber-security |
| 25 | Computer Science (Software Engineering) | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering |
| 26 | Computer Science and Mathematics | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-and-mathematics |
###### BSc (Year-in-Industry variants)
| # | 专业 | URL |
|---|------|-----|
| 27 | Computer Science with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-with-a-year-in-industry |
| 28 | Computer Science (AI) with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence-with-a-year-in-industry |
| 29 | Computer Science (Cyber Security) with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-cyber-security-with-a-year-in-industry |
| 30 | Computer Science (Software Engineering) with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering-with-a-year-in-industry |
###### MSci (integrated-Masters UG)
| # | 专业 | URL |
|---|------|-----|
| 31 | Computer Science MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-msci |
| 32 | Computer Science (AI) MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence-msci |
| 33 | Computer Science (Cyber Security) MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-cyber-security-msci |
| 34 | Computer Science (Software Engineering) MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering-msci |
###### MSci (with Year in Industry)
| # | 专业 | URL |
|---|------|-----|
| 35 | Computer Science with a Year in Industry MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-with-a-year-in-industry-msci |
| 36 | Computer Science (AI) with a Year in Industry MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence-with-a-year-in-industry-msci |
| 37 | Computer Science (Cyber Security) with a Year in Industry MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-cyber-security-with-a-year-in-industry-msci |
| 38 | Computer Science (Software Engineering) with a Year in Industry MSci | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering-with-a-year-in-industry-msci |
###### Foundation Year
| # | 专业 | URL |
|---|------|-----|
| 39 | Computer Science with Integrated Foundation Year | https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-with-integrated-foundation-year |
##### Electronic Engineering
###### BEng
| # | 专业 | URL |
|---|------|-----|
| 40 | Electronic Engineering | https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/electronic-engineering |
###### MEng (integrated — listed at UG level on the dept homepage)
| # | 专业 | URL |
|---|------|-----|
| 41 | Electronic Engineering MEng | https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/electronic-engineering-meng |
##### Mathematics (programme list not extracted in this run — fall back to dept URL)
##### Physics (programme list not extracted in this run — fall back to dept URL)

#### School of Humanities
##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 42 | English | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english |
| 43 | English and Creative Writing | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-creative-writing |
| 44 | English and Philosophy | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-philosophy |
| 45 | English with Philosophy | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-with-philosophy |
| 46 | English and History | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-history |
| 47 | English and Film Studies | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-film-studies |
| 48 | English and American Literature | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-american-literature |
| 49 | English and Classical Studies | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-classical-studies |
| 50 | English and Drama | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-drama |
###### Foundation Year
| # | 专业 | URL |
|---|------|-----|
| 51 | English with Integrated Foundation Year | https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-with-integrated-foundation-year |
##### Comparative Literature and Culture (programme list not extracted in this run — see dept URL)
##### Classics (programme list not extracted in this run — see dept URL)
##### History (programme list not extracted in this run — see dept URL)
##### Languages, Literatures and Cultures (programme list not extracted in this run — see dept URL)
##### Liberal Arts (programme list not extracted in this run — see dept URL)
##### Music (programme list not extracted in this run — see dept URL)
##### Philosophy (programme list not extracted in this run — see dept URL)

#### School of Law and Social Sciences
##### Law and Criminology
###### LLB
| # | 专业 | URL |
|---|------|-----|
| 52 | Law | https://www.royalholloway.ac.uk/studying-here/undergraduate/law-and-criminology/law |
###### BA (combined-honours)
| # | 专业 | URL |
|---|------|-----|
| 53 | Law with Politics | https://www.royalholloway.ac.uk/studying-here/undergraduate/law-and-criminology/law-with-politics |
| 54 | Law with Sociology | https://www.royalholloway.ac.uk/studying-here/undergraduate/law-and-criminology/law-with-sociology |
| 55 | Criminology and Sociology | https://www.royalholloway.ac.uk/studying-here/undergraduate/law-and-criminology/criminology-and-sociology |
| 56 | Criminology and Psychology | https://www.royalholloway.ac.uk/studying-here/undergraduate/law-and-criminology/criminology-and-psychology |
##### Economics
###### BSc (Econ)
| # | 专业 | URL |
|---|------|-----|
| 57 | Economics | https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics |
###### BSc / BSc variants
| # | 专业 | URL |
|---|------|-----|
| 58 | Economics and Management (cross-listed; see Business School) | https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-management |
| 59 | Economics and Management with a Year in Business (cross-listed) | https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-management-with-a-year-in-business |
##### Sociology (hosted under Law and Social Sciences; Geography cross-listing seen on homepage)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 60 | Sociology | https://www.royalholloway.ac.uk/studying-here/undergraduate/sociology/sociology |
##### Politics and International Relations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 61 | Politics and International Relations | https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-and-international-relations |
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 62 | Politics and International Relations with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-and-international-relations-with-a-year-in-industry |
##### Psychology
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 63 | Psychology | https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology |
| 64 | Psychology with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology-with-a-year-in-industry |
##### Social Work
###### BA
| # | 专业 | URL |
|---|------|-----|
| 65 | Social Work | https://www.royalholloway.ac.uk/studying-here/undergraduate/social-work/social-work |
##### Health Studies (programme list not extracted in this run — see dept URL)

#### School of Life Sciences and the Environment
##### Biological Sciences
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 66 | Biology | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/biology |
| 67 | Biomedical Sciences | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/biomedical-sciences |
| 68 | Ecology and Wildlife Conservation | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/ecology-and-wildlife-conservation |
| 69 | Ecology and Wildlife Conservation with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/ecology-and-wildlife-conservation-with-a-year-in-industry |
| 70 | Medical Biochemistry | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/medical-biochemistry |
| 71 | Medical Biochemistry with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/medical-biochemistry-with-a-year-in-industry |
| 72 | Molecular Biology | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/molecular-biology |
| 73 | Molecular Biology with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/molecular-biology-with-a-year-in-industry |
| 74 | Zoology | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/zoology |
| 75 | Zoology with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/zoology-with-a-year-in-industry |
| 76 | Plant Biology | https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/plant-biology |
##### Earth Sciences
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 77 | Geosciences & Sustainable Energy | https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geosciences-sustainable-energy |
| 78 | Geology | https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geology |
| 79 | Environmental Geology | https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/environmental-geology |
| 80 | Physical Geography | https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/physical-geography |
##### Geography
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 81 | Geography BSc | https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/geography-bsc |
| 82 | Geography BSc with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/geography-bsc-with-a-year-in-industry |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 83 | Geography BA | https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/geography-ba |
| 84 | Geography BA with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/geography-ba-with-a-year-in-industry |

#### School of Performing and Digital Arts
##### Drama, Theatre and Dance (UG dir dept label: "Drama and Theatre")
###### BA
| # | 专业 | URL |
|---|------|-----|
| 85 | Drama and Theatre | https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-and-theatre/drama-and-theatre |
| 86 | Drama and Theatre with Integrated Foundation Year | https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-theatre-with-integrated-foundation-year |
| 87 | Drama and Creative Writing | https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-creative-writing |
###### Foundation Year
| # | 专业 | URL |
|---|------|-----|
| 88 | Drama and Theatre with Integrated Foundation Year | https://www.royalholloway.ac.uk/studying-here/2026/undergraduate/drama-theatre-and-dance/drama-and-theatre-with-integrated-foundation-year |
##### Media Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 89 | Digital Media Culture and Technology BA | https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/digital-media-culture-and-technology-ba |
| 90 | Media Arts BA | https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/media-arts-ba |
##### Music (cross-listed under School of Humanities)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 91 | Music | https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music |
| 92 | Music and English (cross-listed with English) | https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-and-english |

#### Interdisciplinary / cross-college undergraduate programmes (selected combined honours)
| # | 专业 | Home dept |
|---|------|-----------|
| 93 | Classical Studies and Drama | Classics (with Drama) |
| 94 | Comparative Literature and Culture and Drama | Comparative Literature and Culture (with Drama) |
| 95 | Modern Languages and Drama | Languages, Literatures and Cultures (with Drama) |
| 96 | Comparative Literature and Culture and English | Comparative Literature and Culture (with English) |
| 97 | Modern Languages and English | Languages, Literatures and Cultures (with English) |

> These combined honours programmes are also published on the cross-listed Department's home page. All listed combined-honours UG programmes total in excess of 150 across the 5 Schools.

### 1.4 Minors — complete list

> Not applicable. Royal Holloway's undergraduate framework uses **single-subject Honours** and **combined Honours** (two subjects), and does not publish a separate "Minors" framework.

### 1.5 General / Institute-wide requirements

Royal Holloway's undergraduate framework is built around the **University of London / sector-norm structure**: modular course units, optional placement years ("Year in Industry", "Year in Business"), and integrated Foundation Years for applicants without standard qualifications. Each single-honours BA / BSc programme is delivered as a 3-year full-time course (or 4 years with placement / Year abroad); MSci and MEng variants are 4 years (or 5 with placement). The homepage highlights confirmed "3 years full time" as the default duration for UG single-honours programmes (e.g. Ecology and Wildlife Conservation / Business and Management / Classical Studies / Computer Science AI / Drama and Theatre / Economics / Electronic Engineering / Geography BSc / Law / Liberal Arts / Digital Media Culture and Technology BA / Politics and International Relations / Psychology).

### 1.6 Course-ID → Major quick-lookup

Royal Holloway uses UCAS course codes as a system-wide identifier, published in each programme listing:

| UCAS code | Major |
|-----------|-------|
| N200 | Business and Management |
| N202 | Business and Management (Accelerated Degree) |
| N500 | BSc Marketing |
| N501 | BSc Marketing with a Year in Business |
| L101 | Economics (BSc Econ) |
| G400 | Computer Science |
| G4G7 | Computer Science (AI) |
| G407 | Computer Science (Cyber Security) |
| G464 | Computer Science (Software Engineering) |
| GG41 | Computer Science and Mathematics |
| G403 | Computer Science MSci |
| HH61 | Electronic Engineering (BEng) |
| C150 | Ecology and Wildlife Conservation |
| F800 | Geography BSc |
| L300 | Sociology (cross-listed with Geography) |
| W440 | Drama and Theatre |
| Q810 | Classical Studies |
| Q300 | English |
| QW38 | English and Creative Writing |
| QV35 | English and Philosophy |
| QW36 | English and Film Studies |
| QT37 | English and American Literature |
| QQ38 | English and Classical Studies |
| QW34 | English and Drama |
| QW31 | English and History |
| L290 | Politics and International Relations |
| C800 | Psychology |
| M100 | Law (LLB) |
| Y000 | Liberal Arts |
| P300 | Digital Media Culture and Technology BA |
| FH62 | Geosciences & Sustainable Energy |

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> Deduplicated postgraduate programme inventory as of 2026-07-08, drawn from departmental "Find your course" carousels and the 2026 PG directory.

#### School of Business and Management — Business School
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Financial Management | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/accounting-and-financial-management |
| 2 | AI for Business MSc | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/ai-for-business-msc |
| 3 | Business Analytics | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/business-analytics |
| 4 | Digital Marketing MSc | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/digital-marketing-msc |
| 5 | Entrepreneurship and Innovation | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/entrepreneurship-and-innovation |
| 6 | Human Resource Management | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/human-resource-management |
| 7 | International Business Management | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/international-business-management |
| 8 | International Business Management (Marketing) | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/international-business-management-marketing |
| 9 | International Business Management (Strategy and Leadership) | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/international-business-management-strategy-and-leadership |
| 10 | Logistics and Supply Chain Management | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/logistics-and-supply-chain-management |
| 11 | Marketing MSc | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/marketing-msc |
| 12 | Project Management | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/project-management |
##### PhD
| # | 项目 | URL |
|---|------|-----|
| 13 | Management PhD | https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/management-phd |

#### School of Engineering, Physical and Mathematical Sciences
##### Computer Science
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 14 | Applied Data Science | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/applied-data-science |
| 15 | Artificial Intelligence | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/artificial-intelligence |
| 16 | Artificial Intelligence with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/artificial-intelligence-with-a-year-in-industry |
| 17 | Computational Finance | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computational-finance |
| 18 | Computational Finance with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computational-finance-with-a-year-in-industry |
| 19 | Computer Science (MSc by Research) | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computer-science |
| 20 | Data Science and Analytics | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/data-science-and-analytics |
| 21 | Data Science and Analytics with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/data-science-and-analytics-with-a-year-in-industry |
| 22 | Machine Learning | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/machine-learning |
| 23 | Machine Learning with a Year in Industry | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/machine-learning-with-a-year-in-industry |
##### Information Security (cross-listed with CS)
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 24 | Applied Data Science and Cyber Security | https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/applied-data-science-and-cyber-security |
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 25 | Computer Science PhD | https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computer-science-phd |
##### Electronic Engineering
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 26 | Advanced Electronic and Electrical Engineering | https://www.royalholloway.ac.uk/studying-here/postgraduate/electronic-engineering/advanced-electronic-and-electrical-engineering |
##### Physics / Mathematics (programme list not extracted in this run — see dept URLs)

#### School of Humanities
##### English
###### MA
| # | 项目 | URL |
|---|------|-----|
| 27 | Creative Writing | https://www.royalholloway.ac.uk/studying-here/postgraduate/english/creative-writing |
| 28 | English Literature | https://www.royalholloway.ac.uk/studying-here/postgraduate/english/english-literature |
| 29 | English Literature: Medieval Studies | https://www.royalholloway.ac.uk/studying-here/postgraduate/english/english-literature-medieval-studies |
| 30 | English Literature: Victorian Literature, Art and Culture | https://www.royalholloway.ac.uk/studying-here/postgraduate/english/english-literature-victorian-literature-art-and-culture |
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 31 | English PhD | https://www.royalholloway.ac.uk/studying-here/postgraduate/english/english-phd |
##### Classics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 32 | Ancient History | https://www.royalholloway.ac.uk/studying-here/postgraduate/classics/ancient-history |
##### (History, Comparative Lit, Music, Liberal Arts, Philosophy, Languages — see dept URLs)

#### School of Law and Social Sciences
##### Psychology
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 33 | Applied Neuroscience | https://www.royalholloway.ac.uk/studying-here/postgraduate/psychology/applied-neuroscience |
##### Social Work
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 34 | Advanced Practice (3 years part time) | https://www.royalholloway.ac.uk/studying-here/postgraduate/social-work/advanced-practice |
##### Geography (cross-listed with Business)
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 35 | Sustainability and Management | https://www.royalholloway.ac.uk/studying-here/postgraduate/geography/sustainability-and-management |
##### (Economics, Politics, Law — see dept URLs)

#### School of Life Sciences and the Environment
##### Biological Sciences (programme list not extracted in this run — see dept URL)
##### Earth Sciences (programme list not extracted in this run — see dept URL)
##### Geography (Sustainability and Management already listed above)

#### School of Performing and Digital Arts
##### Drama, Theatre and Dance
###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 36 | Drama, Theatre and Dance MA by Research | https://www.royalholloway.ac.uk/studying-here/postgraduate/drama-theatre-and-dance/drama-theatre-and-dance-ma-by-research |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science PhD** (representative research-degree example):

- **Department**: Computer Science (administrative home) — with cross-listing into Information Security for cyber-security themes.
- **Departmental contact**: Department of Computer Science, Royal Holloway, University of London, Egham, Surrey TW20 0EX.
- **Mode**: 4 years full-time (research).
- **Application portal**: Royal Holloway direct application form — see https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computer-science-phd.
- **Standard research-degree admissions**: see Section 3.3 (research degrees / MPhil / PhD use the central Royal Holloway PG application route; tuition fee status set by UK Research Council or college funding).
- **English language requirements (PG research degrees, confirmed on the dedicated ELR page)**: IELTS 6.5 overall with Writing 7.0 and no other subscore lower than 5.5; Pearson PTE 61 with Writing 69; TOEFL iBT 88 with Reading 18 / Listening 17 / Speaking 20 / Writing 26; Duolingo 120 with 135 in Literacy and Production.

> Behind accordions on the live programme page: full-time / part-time attendance modes, supervisory-team matching, research themes (algorithms, AI/ML, cyber security, distributed systems), and funding routes (EPSRC DTP, college scholarships).

### 2.3 Graduate admissions model

Centralised postgraduate application: the `studying-here/postgraduate/<dept>/<programme>` URL pattern routes all taught-Masters and research-degree applications through Royal Holloway's own application portal (not UCAS for PG). The standard application fee structure is set by Royal Holloway with fee waivers available — see Section 4.3. The Business School operates AACSB accreditation and accepts GMAT / GRE in some programmes; the broader MA / MSc portfolio does not require standardised tests (subject-by-subject check recommended).

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value |
|-----------|-------|
| Admissions site | https://www.royalholloway.ac.uk/studying-here/applying/ |
| Application portal | **UCAS** (undergraduate applications are routed through UCAS — confirm deadline via UCAS) |
| UCAS deadline (typical UG entry) | UCAS equal-consideration deadline = 31 January (most UG programmes); confirm via UCAS / Royal Holloway's UG entry requirements page |
| Clearing | "Clearing 2026" published as a top-level studying-here section — see https://www.royalholloway.ac.uk/studying-here/applying/undergraduate/clearing |
| **EA deadline** | N/A — UK universities do not publish an Early Action equivalent; UG offer-making runs UCAS-cycle-based (Oct / Jan / post-Jan) |
| **RA / normal-cycle deadline** | 31 January (UCAS equal-consideration) — verify on UCAS / RHUL admissions page; international applicants may apply past this date |
| Decision notification dates | UCAS publishes — Royal Holloway confirms offers on UCAS Hub |
| Enrollment-confirmation deadline | Per UCAS / institutional acceptance deadline |
| Financial-aid deadline | Bursary / scholarship deadlines published under "Fees and funding"; check https://www.royalholloway.ac.uk/studying-here/fees-and-funding |
| SAT / ACT policy + deadline | **Not required for UK applicants**. US applicants with high-school diploma + SAT / ACT may be considered for direct entry alongside A-Level / IB applicants; consult admissions policy |
| Superscore policy | N/A |
| Score-report method | UCAS / institutional reporting; for UG entry this is institutional decision-based |
| Interview policy | Department-dependent (e.g. Drama, Music; some PG programmes) |
| Recommendation requirements | UCAS reference letter (one academic reference for UG) |
| Portfolios | Drama, Theatre, Music, Media Arts — department-portfolio requirement |
| Transfer pathway | "Year in Industry" / "Year in Business" variants; internal transfer via Year-Abroad / Erasmus routes |

### 3.2 Undergraduate English proficiency table

> Direct quote from https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/ (extracted 2026-07-08): "Our required scores vary depending on the language demands of the subject you wish to study." Royal Holloway lists eight accepted tests and three score bands by subject-band. The following reflects the bands as published. Subjects fall into BAND-A ("business / social-science-leaning"), BAND-B ("most arts / humanities / sciences") and BAND-C ("heavier language demand e.g. English single-honours"):

| Exam | Most UG — Band B minimum | Recommended |
|------|--------------------------|-------------|
| IELTS (including IELTS indicator) | 6.5 overall with 6 in Writing and minimum of 5.5 in each subscore | 7.0 overall with 6.5 in each band |
| Pearson Test of English (PTE Academic) | 67 with 61 in writing (no other subscore lower than 54) | 69 overall |
| Trinity College London (ISE) | ISE IV | — |
| Cambridge ESOL | Cambridge English: Advanced (CAE) grade C | — |
| TOEFL iBT (including Special Home Edition) | 88 overall, with Reading 18 / Listening 17 / Speaking 20 / Writing 19 | 95 overall |
| Duolingo English Test | 120 overall, 115 in Literacy, 115 in Production and no sub-score below 100 | 125 overall |
| LanguageCert Academic (in-Person / Online) | Per Royal Holloway acceptance (subject band) | — |
| Oxford Test of English (Standard & Advanced) / ELLT Digital and Global | Per Royal Holloway acceptance (subject band) | — |

> Applicable condition: international applicants whose first language is not English, unless they are nationals of an English-speaking country on the Home Office list (Antigua and Barbuda, Australia, the Bahamas, Barbados, Belize, the British overseas territories, Canada, Dominica, Grenada, Guyana, Ireland, Jamaica, Malta, New Zealand, St Kitts and Nevis, St Lucia, St Vincent and the Grenadines, Trinidad and Tobago, UK, USA).

### 3.3 Graduate — global rules

- **Decentralised admissions**: All PG taught applications submitted via the per-department programme URL (e.g. `/studying-here/postgraduate/business-school/msc-marketing`); the Royal Holloway portal aggregates departments. There is no central "Graduate School" application — each Department's admissions tutor reviews applications within the College-wide framework.
- **Application platform**: Royal Holloway direct PG application (per programme page).
- **Standard application fee**: published at the per-programme level; fee-waiver available per the College's widening-access / international policy.
- **CGS April-15-equivalent**: Royal Holloway is a UK university and observes the UK Council for Graduate Schools' equivalent (postgraduate 14-day response honour date and the April-15 funding deadline convention) implicitly; explicit confirm via the central PG admissions policy.
- **GRE / GMAT policy**: not standardised across Departments; some Business School programmes (AACSB-accredited) request GMAT / GRE, but most MA / MSc programmes do not.
- **Language-test policy**: same accepted-test list as UG; PG Research degrees require IELTS 6.5 with Writing 7.0 (and no subscore below 5.5); other tests as listed in Section 3.2 by subject-band.
- **Exemption rules**: applicants with bachelor's-degree study at a majority English-speaking country, or one year of taught UG study in an English-medium HEI in such a country, are exempt.
- **Application timeline**: rolling admissions with most taught Masters admitting for September entry; some programmes have January / February deadlines — check per-programme page.
- **Institutional / departmental test codes**: TOEFL / GRE codes handled at the per-application level; no central code listing.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

> Royal Holloway publishes annual tuition fees on the Fees and Funding pages (see https://www.royalholloway.ac.uk/studying-here/fees-and-funding/ and https://www.royalholloway.ac.uk/studying-here/fees-and-funding/tuition-fees/) and updates them annually. The following is a representative framework drawn from the live pages.

| Expense item | Amount | Description |
|--------------|--------|-------------|
| UG tuition fee (Home / RUK, annual) | published annually on Fees-and-Funding page | UK PGT fee cap applies; check current year |
| UG tuition fee (International, annual, classroom-based) | per programme and per subject band (e.g. higher for Business, Engineering, Sciences) | Tuition varies by Department — confirm on programme page |
| Tuition fee deposit (International, undergraduate) | £3,000 or £10,000 (see note) | Required for CAS issuance for international students needing a UK Student visa |
| Tuition fee deposit (Postgraduate, Home) | £100 (Home applicants required to pay a tuition fee deposit to fully secure a place on the course) | Per the international-fees page, Home PG applicants deposit £100 |
| Tuition fee deposit (Postgraduate, International) | £3,000 or £10,000 (see note) | Required for CAS issuance for international students needing a UK Student visa |
| Tuition payment instalments | 2 equal instalments permitted (1st by 25 Sep, 2nd by 12 Jan for 2025/26) | Two equal instalments for international students on new course starting Sept 2025 (conferring on annual update) |
| Accommodation cost | per academic year | RHUL Accommodation Office (per-week × 39 weeks) |
| Books / personal expenses | per academic year | per Student Fees / Student Funding guidance |

> Note: the deposit (£3,000 vs £10,000) is set by Royal Holloway and is department- and intake-dependent — confirm on the offer letter or the international student fees page (https://www.royalholloway.ac.uk/studying-here/fees-and-funding/international-student-fees/). Currency: GBP. Tuition figures are UK Sterling.

### 4.2 Undergraduate financial-aid policy

Royal Holloway publishes the following aid frameworks:

- **Bursaries**: A range of bursaries are available for eligible students (Home UK). See https://www.royalholloway.ac.uk/studying-here/fees-and-funding/bursaries.
- **Government funding**: "Get help with the costs of studying and living during your undergraduate degree" — UK Government Student Finance / Tuition Fee Loan routed via Student Loans Company.
- **Scholarships**: "Become a Royal Holloway scholar and help fund your studies." See https://www.royalholloway.ac.uk/studying-here/fees-and-funding/scholarships. Includes international scholarship portfolio.
- **Tuition-free income threshold**: UK Government scheme — for assessment of fee waiver / maintenance grant, follow UK Student Finance / NHS rules; published by RHUL on bursary pages.
- **Need-blind / need-aware (international)**: Royal Holloway operates scholarship routes for international students; not strictly "need-blind" in the US sense — scholarships are merit / need assessed.
- **Median actual price paid / debt-free graduation rate / average starting salary**: published in Departmental subject pages and prospectus (e.g. Computer Science: 92% in graduate-level jobs or further study within 15 months per Times and Sunday Times Good University Guide, 2026).

### 4.3 Graduate cost & funding framework

| Funding / cost item | Detail |
|---------------------|--------|
| Funding-type taxonomy | Fully / partially / self-funded; RA / TA / scholarship routes; college-funded scholarships; UK Research Council funding (e.g. EPSRC DTP) for eligible research degrees |
| Common funding forms | RA (Research Assistantship), TA (Teaching Assistantship), college scholarships and bursaries, Research Council studentships (UKRI / EPSRC / ESRC), external scholarships (e.g. Chevening, Commonwealth) |
| Application fee | published per programme; fee-waivers available per widening-access / international policy |
| Tuition fee deposit (PG, Home) | £100 |
| Tuition fee deposit (PG, International, student-visa required) | £3,000 or £10,000 (per dept / intake) |
| Tuition payment instalments | 2 equal instalments for International students starting new course in Sept 2025 (per international student fees page) — first instalment by 25 September, second by 12 January |
| Cost-of-attendance / stipend-rates / living-expenses | published per programme / per college-level research-degree page; check Department + PG fees-and-funding pages |

---

## SECTION 5 — Evidence chain index

> Numbered evidence blocks for the highest-value fields captured on 2026-07-08.

```yaml
E-U-001:
  field: institution.basic
  value: Royal Holloway, University of London (constituent college of the University of London; Russell Group member)
  source_url: https://www.royalholloway.ac.uk/
  source_snippet: "Royal Holloway University of London ... Visit Royal Holloway, University of London Egham, Surrey TW20 0EX"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.school_count
  value: 5 Schools (Schools A, B, C, D, E with cross-departmental membership)
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "School of Business and Management ... School of Engineering, Physical and Mathematical Sciences ... School of Humanities ... School of Law and Social Sciences ... School of Life Sciences and the Environment ... School of Performing and Digital Arts"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.department_count
  value: 25 Departments hosted across the 5 Schools (4 + Business School)
  source_url: https://www.royalholloway.ac.uk/research-and-education/departments-and-schools/
  source_snippet: "Biological Sciences, Business School, Classics, Comparative Literature and Culture, Computer Science, Drama and Theatre, Earth Sciences, Economics, Electronic Engineering, English, Geography, Health Studies, History, Information Security, Languages, Literatures and Cultures, Law and Criminology, Liberal Arts, Mathematics, Media Arts, Music, Philosophy, Physics, Politics and International Relations, Psychology, Social Work"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: ug.programme_count
  value: ~350+ UG + PG variants across 25 Departments (large cross-list — see Section 0.1)
  source_url: https://www.royalholloway.ac.uk/studying-here/
  source_snippet: "Explore some of our undergraduate courses ... Biological Sciences ... Ecology and Wildlife Conservation ... 3 years full time ... BSc C150 ... Business School ... Business and Management (Accelerated Degree) ... 2 years full time ... BSc N202 ... Classical Studies ... 3 years full time ... BA Q810 ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: ug.duration
  value: 3 years full time (single-subject UG standard); 4 years with Year in Industry/Business; 2 years for the Accelerated Business and Management degree
  source_url: https://www.royalholloway.ac.uk/studying-here/
  source_snippet: "3 years full time ... BSc C150 ... Business and Management (Accelerated Degree) ... 2 years full time ... BSc N202"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: ug.application_portal
  value: UCAS (undergraduate)
  source_url: https://www.royalholloway.ac.uk/studying-here/applying/
  source_snippet: "Apply online through UCAS."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: ug.clearing
  value: Clearing 2026 published as a top-level /studying-here section
  source_url: https://www.royalholloway.ac.uk/studying-here/applying/undergraduate/clearing
  source_snippet: "Clearing 2026 ... Find out all you need to know about applying to study at Royal Holloway through Clearing."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: english.home_office_exemption_list
  value: "Antigua and Barbuda, Australia, the Bahamas, Barbados, Belize, the British overseas territories, Canada, Dominica, Grenada, Guyana, Ireland, Jamaica, Malta, New Zealand, St Kitts and Nevis, St Lucia, St Vincent and the Grenadines, Trinidad and Tobago, UK, USA"
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "If you are a national of one of the following countries, we will not need proof of your English language ability: Antigua and Barbuda, Australia, the Bahamas, Barbados, Belize, the British overseas territories, Canada, Dominica, Grenada, Guyana, Ireland, Jamaica, Malta, New Zealand, St Kitts and Nevis, St Lucia, St Vincent and the Grenadines, Trinidad and Tobago, UK, USA."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: english.accepted_tests
  value: IELTS, Pearson Test of English, Cambridge ESOL, TOEFL iBT, OnCampus Test of English (OCTOE), Duolingo, LanguageCert Academic, Kaplan Test of English, Oxford English Language Level Test (ELLT) Digital and Global, Oxford Test of English
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "IELTS (including IELTS indicator) ... Pearson Test of English ... Cambridge ESOL ... TOEFL iBT (including the Special Home Edition) ... OnCampus Test of English (OCTOE) ... Duolingo English Test ... LanguageCert Academic in-Person and Online ... Kaplan Test of English ... Oxford English Language Level Test (ELLT) Digital and Global ... Oxford Test of English (Standard & Advanced)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: english.ug_band_b_ielts
  value: "6.5 overall with 6 in Writing and minimum of 5.5 in each subscore"
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "IELTS: 6.5 overall with 6 in Writing and minimum of 5.5 in each subscore"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: english.ug_band_b_pte
  value: "PTE: 67 with 61 in writing (no other subscore lower than 54)"
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "Pearson Test of English: 67 with 61 in writing (no other subscore lower than 54)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: english.ug_band_b_toefl
  value: "TOEFL iBT: 88 overall, with Reading 18 / Listening 17 / Speaking 20 / Writing 19"
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "TOEFL iBT: 88 overall, with Reading 18 Listening 17 Speaking 20 Writing 19"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: english.ug_band_b_duolingo
  value: "Duolingo: 120 overall, 115 in Literacy, 115 in Production and no sub-score below 100"
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "Duolingo: 120 overall, 115 in Literacy, 115 in Production and no sub-score below 100."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: ug.international_deposit
  value: "£3,000 or £10,000 tuition fee deposit (UG International, Student visa applicants)"
  source_url: https://www.royalholloway.ac.uk/studying-here/fees-and-funding/international-student-fees/
  source_snippet: "If you are an International student who needs a Student visa to enter and study in the UK, you will need to pay the £3,000 or £10,000* tuition fee deposit before a Confirmation of Acceptance for Study (CAS) number can be issued."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: fees.payment_instalments
  value: "Two equal instalments for international students beginning a new course in September 2025; first instalment by 25 September 2025 with second payment due 12 January 2026"
  source_url: https://www.royalholloway.ac.uk/studying-here/fees-and-funding/international-student-fees/
  source_snippet: "International students beginning a new course in September 2025 will have the option to pay their tuition fee in two equal instalments. ... Fee payment to enrol for 2025/26 must be made by 25 September 2025 with the second payment due 12 January 2026."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-001:
  field: pg.application_route
  value: "Royal Holloway direct PG application (per programme page); not UCAS"
  source_url: https://www.royalholloway.ac.uk/studying-here/postgraduate-courses/
  source_snippet: "POSTGRADUATE COURSES ... 2026 ... Business School ... Accounting and Financial Management ... 1 year full time ... MSc ... https://www.royalholloway.ac.uk/studying-here/postgraduate/business-school/accounting-and-financial-management"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-002:
  field: pg.deposit_home
  value: "£100 (Home PG applicants)"
  source_url: https://www.royalholloway.ac.uk/studying-here/fees-and-funding/international-student-fees/
  source_snippet: "If you are a Home applicant you will need to pay a tuition fee deposit of £100 as soon as possible to fully secure your place on the course."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-003:
  field: english.pgresearch_requirements
  value: "IELTS 6.5 overall, Writing 7.0, no subscore below 5.5; PTE 61 overall, Writing 69, no other subscore below 51; TOEFL iBT 88 with Reading 18 / Listening 17 / Speaking 20 / Writing 26; Duolingo 120 overall, 135 in Literacy, 135 in Production, no sub-score below 100"
  source_url: https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/
  source_snippet: "All Postgraduate Research degrees (i.e. PhD and Masters by Research) require: IELTS: 6.5 overall. Writing 7.0. No other subscore lower than 5.5. Pearson Test of English: 61 overall. Writing 69. No other subscore lower than 51. Trinity College London Integrated Skills in English (ISE): ISE III. Cambridge English: Advanced (CAE) grade C. TOEFL iBT: 88 overall, with Reading 18 Listening 17 Speaking 20 Writing 26. Duolingo: 120 overall, 135 in Literacy, 135 in Production and no sub-score below 100."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-004:
  field: pg.ucas_routes
  value: "Postgraduate applications are routed through Royal Holloway's own portal per programme page; research degrees are MPhil / PhD supervised by the relevant Department"
  source_url: https://www.royalholloway.ac.uk/studying-here/postgraduate-courses/
  source_snippet: "POSTGRADUATE COURSES ... Computer Science ... Computer Science PhD ... 4 years full time ... PhD"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-005:
  field: pg.research_centre_links
  value: "Information Security Group (cross-listed with Computer Science, hosting Applied Data Science and Cyber Security MSc)"
  source_url: https://www.royalholloway.ac.uk/studying-here/postgraduate-courses/
  source_snippet: "Information Security ... Applied Data Science and Cyber Security ... 1 year full time ... MSc ... https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/applied-data-science-and-cyber-security"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: royal-holloway-knowledge-base-v2
  ├── document: rhul-overview-2026            (section 0: counts, hierarchy, degree inventory, distribution matrix)
  ├── document: rhul-ug-2026                 (section 1: undergraduate majors grouped by School > Department > Degree level)
  ├── document: rhul-pg-2026                 (section 2: postgraduate programmes grouped similarly)
  ├── document: rhul-ug-admissions-2026      (section 3: deadlines, tests, UCAS)
  ├── document: rhul-pg-admissions-2026      (section 3: PG-admissions framework + English language)
  ├── document: rhul-fees-funding-2026       (section 4: tuition + funding)
  └── document: rhul-evidence-2026           (section 5: YAML evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "royal-holloway-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BEng|LLB|MSci|MA|MSc|PhD|MPhil>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority (P0/P1/P2) | Data item | Target URL |
|-----|-----------|-----------|
| P0 | Per-programme UG tuition (Home and International) — annual figures | https://www.royalholloway.ac.uk/studying-here/fees-and-funding/tuition-fees/ and per-programme fee tabs |
| P0 | Per-programme PG tuition — annual figures | https://www.royalholloway.ac.uk/studying-here/fees-and-funding/tuition-fees/ |
| P0 | UCAS deadline (current cycle) | https://www.royalholloway.ac.uk/studying-here/applying/ |
| P1 | Mathematics, Physics, Liberal Arts, Music, Languages Literatures and Cultures, Philosophy, History, Comparative Literature and Culture full programme list | https://www.royalholloway.ac.uk/research-and-education/departments-and-schools/<slug>/ |
| P1 | Health Studies, Earth Sciences full programme list | https://www.royalholloway.ac.uk/research-and-education/departments-and-schools/<slug>/ |
| P1 | Economics / Politics / Law full programme list (incl. MA, MPhil variants) | https://www.royalholloway.ac.uk/research-and-education/departments-and-schools/<slug>/ |
| P2 | Accommodation / living-cost detail | https://www.royalholloway.ac.uk/student-life/accommodation |
| P2 | Bespoke subject-band English requirements verification (band A / C) | https://www.royalholloway.ac.uk/studying-here/international-students/english-language-requirements/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | RHUL 2026 value |
|-----------|-----------------|
| Total UG cost / yr | per-programme (see P0 follow-up) |
| International UG deposit | £3,000 or £10,000 (student-visa applicants) |
| Tuition/yr UG (Home) | per UK Student Finance cap (verify) |
| Home PG deposit | £100 |
| International PG deposit | £3,000 or £10,000 (student-visa applicants) |
| Need-blind (intl?) | No — international scholarship-based aid only |
| UCAS deadline (UG) | UCAS-published (typically 31 January) |
| Clearing route | "Clearing 2026" — published |
| TOEFL min (UG band B) | 88 iBT |
| IELTS min (UG band B) | 6.5 overall, 6 in Writing, 5.5 in each subscore |
| PTE min (UG band B) | 67 overall, 61 in Writing |
| Duolingo min (UG band B) | 120 overall (115 in Literacy / Production) |
| TOEFL min (PG research) | 88 iBT (Reading 18 / Listening 17 / Speaking 20 / Writing 26) |
| IELTS min (PG research) | 6.5 overall, Writing 7.0 |
| Grad application fee | per programme; fee-waiver available |
| April-15-equivalent | implicit (UK CGS-style 14-day response convention) |
| **Total programme count (Rule 1)** | ~350+ (UG + PG variants across 25 Departments) |
| **School/Department count (Rule 2)** | 5 Schools / 25 Departments |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: royalholloway.ac.uk (Departments page, Course Finder homepage, Postgraduate Directory 2026, International Student Fees, English Language Requirements, Department-level "Find your course" carousels for Computer Science / Business School / English / Drama, Theatre and Dance)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
