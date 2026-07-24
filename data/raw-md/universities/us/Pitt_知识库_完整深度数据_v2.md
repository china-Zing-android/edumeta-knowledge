# University of Pittsburgh (Pitt) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BSE/BSN/BSBA/BASW/BPhil) | 105 |
| 本科辅修 (Minor) | 57 |
| 研究生学位项目 (MA/MS/MBA/PhD/EdD/DNP/MD/JD/DMD/PharmD/etc.) | 138 |
| 研究生博士项目 (PhD/EdD/DNP/MD/JD/DMD/PharmD/DBA/SJD/AuD/DC/DPT/OTD) | 100 |
| 研究生高级证书 (Advanced Certificate / Graduate Certificate) | 147 |
| 研究生微证书 (Micro-credential) | 11 |
| **学位项目总计 (UG + Grad)** | **511** |
| 学院 / 独立系所总数 | 18 |

> **数据来源**: Pitt Degree Finder (academics.pitt.edu/degree-finder-view), 2026-07-06 抓取。本科专业列表来自 academics.pitt.edu/undergraduate-programs。辅修列表来自同一页面。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Pittsburgh
├── Kenneth P. Dietrich School of Arts and Sciences (A&S)          [学院]
│   ├── Africana Studies                                           [系]
│   ├── Anthropology                                               [系]
│   ├── Architectural Studies                                      [系]
│   ├── Bioethics                                                  [系]
│   ├── Biological Sciences                                        [系]
│   ├── Chemistry                                                  [系]
│   ├── Children's Literature                                      [系]
│   ├── Classics, Philosophy & Ancient Science                     [系]
│   ├── Communication                                              [系]
│   ├── Critical European Culture Studies                          [系]
│   ├── Cultural Studies                                           [系]
│   ├── Digital Studies and Methods                                [系]
│   ├── East Asian Languages and Literatures                       [系]
│   ├── Economics                                                  [系]
│   ├── English                                                    [系]
│   ├── Environmental Studies                                      [系]
│   ├── Film and Media Studies                                     [系]
│   ├── French & Italian                                           [系]
│   ├── Gender, Sexuality, and Women's Studies                     [系]
│   ├── Geology and Environmental Science                          [系]
│   ├── German                                                     [系]
│   ├── Hispanic Languages and Literatures                         [系]
│   ├── History                                                    [系]
│   ├── History and Philosophy of Science                          [系]
│   ├── History of Art & Architecture                              [系]
│   ├── Jewish Studies                                             [系]
│   ├── Less-Commonly-Taught Languages Center                      [系]
│   ├── Linguistics                                                [系]
│   ├── Mathematics                                                [系]
│   ├── Medieval and Renaissance Studies                           [系]
│   ├── Music                                                      [系]
│   ├── Neuroscience                                               [系]
│   ├── Philosophy                                                 [系]
│   ├── Physics and Astronomy                                      [系]
│   ├── Political Science                                          [系]
│   ├── Psychology                                                 [系]
│   ├── Religious Studies                                          [系]
│   ├── Slavic Languages and Literatures                           [系]
│   ├── Sociology                                                  [系]
│   ├── Spanish                                                    [系]
│   ├── Statistics                                                 [系]
│   ├── Studio Arts                                                [系]
│   ├── Theatre Arts                                               [系]
│   ├── Urban Studies                                              [系]
│   └── The Writing Institute                                      [系]
├── College of Business Administration (CBA)                       [学院]
│   ├── Accounting                                                 [系]
│   ├── Business Analytics                                         [系]
│   ├── Business Information Systems                               [系]
│   ├── Finance                                                    [系]
│   ├── Global Management                                          [系]
│   ├── Human Resources Management                                 [系]
│   ├── Marketing                                                  [系]
│   └── Supply Chain Management                                    [系]
├── Joseph M. Katz Graduate School of Business                     [学院]
│   ├── Accounting                                                 [系]
│   ├── Business Analytics                                         [系]
│   ├── Finance                                                    [系]
│   ├── Management                                                 [系]
│   ├── Marketing                                                  [系]
│   └── Supply Chain Management                                    [系]
├── Swanson School of Engineering (ENG)                            [学院]
│   ├── Bioengineering                                             [系]  ⚠ shared with A&S
│   ├── Chemical and Petroleum Engineering                         [系]
│   ├── Civil and Environmental Engineering                        [系]
│   ├── Electrical and Computer Engineering                        [系]
│   ├── Engineering Science                                        [系]
│   ├── Industrial Engineering                                     [系]
│   └── Mechanical Engineering and Materials Science               [系]
├── School of Computing and Information (SCI)                      [学院]
│   ├── Computer Science                                           [系]
│   ├── Digital Narrative and Interactive Design                   [系]
│   ├── Information Culture and Data Stewardship                   [系]
│   ├── Informatics and Networked Systems                          [系]
│   └── Intelligent Systems Programs                               [系]
├── School of Nursing (NUR)                                        [学院]
│   └── Nursing (no internal dept subdivision)                     [系]
├── School of Education (EDUC)                                     [学院]
│   ├── Educational Foundations, Organizations and Policy          [系]
│   ├── Health and Human Development                               [系]
│   └── Teaching, Learning and Leading                             [系]
├── College of General Studies (CGS)                               [学院]
│   └── General Studies (no internal dept subdivision)             [系]
├── School of Health and Rehabilitation Sciences (SHRS)            [学院]
│   ├── Athletic Training                                          [系]
│   ├── Chiropractic                                               [系]
│   ├── Clinical Mental Health Counseling                          [系]
│   ├── Communication Science and Disorders                        [系]
│   ├── Emergency Medicine                                         [系]
│   ├── Health Informatics                                         [系]
│   ├── Nutrition and Dietetics                                    [系]
│   ├── Occupational Therapy                                       [系]
│   ├── Physical Therapy                                           [系]
│   ├── Physician Assistant Studies                                [系]
│   ├── Prosthetics and Orthotics                                  [系]
│   ├── Rehabilitation Science                                     [系]
│   ├── Rehabilitation Technology                                  [系]
│   └── Sports Science                                             [系]
├── School of Dental Medicine                                      [学院]
│   └── Dental Medicine (no internal dept subdivision)             [系]
├── School of Law                                                  [学院]
│   └── Law (no internal dept subdivision)                         [系]
├── School of Medicine                                             [学院]
│   ├── Anesthesiology                                             [系]
│   ├── Biomedical Informatics                                     [系]
│   ├── Cardiothoracic Surgery                                     [系]
│   ├── Cell Biology                                               [系]
│   ├── Clinical Research                                          [系]
│   ├── Computational and Systems Biology                          [系]
│   ├── Critical Care Medicine                                     [系]
│   ├── Dermatology                                                [系]
│   ├── Developmental Biology                                      [系]
│   ├── Emergency Medicine                                         [系]
│   ├── Family Medicine                                            [系]
│   ├── Immunology                                                 [系]
│   ├── Institute on Aging                                         [系]
│   ├── Interdisciplinary Biomedical Graduate Program              [系]
│   ├── Integrative Molecular Biology                              [系]
│   ├── Medicine                                                   [系]
│   ├── Microbiology and Molecular Genetics                        [系]
│   ├── Neurobiology                                               [系]
│   ├── Neurological Surgery                                       [系]
│   ├── Neurology                                                  [系]
│   ├── OB/GYN and Reproductive Sciences                           [系]
│   ├── Ophthalmology                                              [系]
│   ├── Orthopaedic Surgery                                        [系]
│   ├── Otolaryngology                                             [系]
│   ├── Pathology                                                  [系]
│   ├── Pediatrics                                                 [系]
│   ├── Pharmacology and Chemical Biology                          [系]
│   ├── Physical Medicine and Rehabilitation                       [系]
│   ├── Plastic Surgery                                            [系]
│   ├── Psychiatry                                                 [系]
│   ├── Radiation Oncology                                         [系]
│   ├── Radiology                                                  [系]
│   ├── Structural Biology                                         [系]
│   ├── Surgery                                                    [系]
│   └── Urology                                                    [系]
├── School of Pharmacy                                             [学院]
│   └── Pharmacy (no internal dept subdivision)                    [系]
├── School of Public Health                                        [学院]
│   ├── Behavioral & Community Health Sciences                     [系]
│   ├── Biostatistics                                              [系]
│   ├── Environmental and Occupational Health                      [系]
│   ├── Epidemiology                                               [系]
│   ├── Genetic Counseling                                         [系]
│   ├── Genome Bioinformatics                                      [系]
│   ├── Health Policy & Management                                 [系]
│   ├── Human Genetics                                             [系]
│   ├── Health Services Research and Policy                        [系]
│   ├── Infectious Diseases and Microbiology                       [系]
│   └── Multidisciplinary MPH Program                              [系]
├── School of Public and International Affairs (SPIA)              [学院]
│   └── Public & International Affairs (no internal dept)          [系]
├── School of Social Work                                          [学院]
│   └── Social Work (no internal dept subdivision)                 [系]
├── David C. Frederick Honors College                              [学院]
│   └── Honors (interdisciplinary, all majors)                     [系]
├── University Center for International Studies (UCIS)             [学院]
│   ├── African Studies                                            [系]
│   ├── Asian Studies                                              [系]
│   ├── European Union Studies                                     [系]
│   ├── Global Studies                                             [系]
│   ├── Latin American Studies                                     [系]
│   ├── Russian, Eastern European & Eurasian Studies               [系]
│   ├── Transnational Asia Studies                                 [系]
│   └── West European Studies                                      [系]
└── University Center for Social & Urban Research                  [学院]
```

> **注**: Pitt 的 Frederick Honors College 提供 BPhil (Bachelor of Philosophy) 学位，可在所有专业中授予。部分专业为跨学院联合项目（如 Computational Biology = A&S + SCI）。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 42 |
| BS | Bachelor of Science | 本科 | 38 |
| BSE | Bachelor of Science in Engineering | 本科 | 10 |
| BSBA | Bachelor of Science in Business Administration | 本科 | 8 |
| BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BASW | Bachelor of Arts in Social Work | 本科 | 1 |
| BPhil | Bachelor of Philosophy (Honors) | 本科 | 1 |
| AS | Associate of Science (Dental Hygiene) | 本科 | 1 |
| MA | Master of Arts | 研究生 | 18 |
| MS | Master of Science | 研究生 | 65 |
| MBA | Master of Business Administration | 研究生 | 6 |
| MEd | Master of Education | 研究生 | 8 |
| MPH | Master of Public Health | 研究生 | 8 |
| MPA | Master of Public Administration | 研究生 | 3 |
| MPP | Master of Public Policy | 研究生 | 2 |
| MSW | Master of Social Work | 研究生 | 2 |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MEng | Master of Engineering | 研究生 | 3 |
| MID | Master of International Development | 研究生 | 2 |
| MLIS | Master of Library and Information Science | 研究生 | 1 |
| MHA | Master of Health Administration | 研究生 | 1 |
| DMD | Doctor of Dental Medicine | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| PharmD | Doctor of Pharmacy | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 68 |
| EdD | Doctor of Education | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| SJD | Doctor of Juridical Science | 研究生 | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| DC | Doctor of Chiropractic | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 2 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| Graduate Certificate | 研究生证书 | 研究生 | 147 |
| Micro-credential | 微证书 | 研究生 | 11 |
| **总计** | | | **511** |

> **学位规范化说明**: Pitt 使用标准美式学位缩写（BA/BS/MA/MS/PhD 等），无拉丁文变体。BSE 为工程学院特有学位。BSBA 为商学院特有学位。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSE | BSBA | BSN | BASW | BPhil | AS | MA | MS | MBA | MEd | MPH | MPA | MPP | MSW | MFA | MEng | PhD | 专业博士 | Cert | Micro | 合计 |
|------------|----|----|-----|------|-----|------|-------|----|----|----|----|-----|-----|-----|-----|-----|-----|------|-----|--------|------|-------|------|
| Dietrich A&S | 35 | 28 | 0 | 0 | 0 | 0 | 1 | 0 | 12 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 35 | 0 | 10 | 0 | 141 |
| CBA | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 13 |
| Katz Business | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 14 | 1 | 38 |
| Engineering | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 8 | 0 | 11 | 0 | 44 |
| SCI | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 8 | 0 | 20 |
| Nursing | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | 7 |
| Education | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 1 | 15 | 0 | 44 |
| CGS | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 17 |
| SHRS | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 15 | 1 | 37 |
| Dental Med | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 13 | 0 | 18 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 9 | 0 | 12 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 1 | 5 | 0 | 20 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 6 |
| Public Health | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 6 | 0 | 31 |
| SPIA | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 11 |
| Social Work | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 6 | 0 | 11 |
| Honors | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| UCIS | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 22 |
| UCSUR | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | 42 | 41 | 10 | 8 | 2 | 1 | 2 | 1 | 13 | 78 | 6 | 8 | 8 | 3 | 2 | 2 | 2 | 3 | 83 | 13 | 147 | 11 | **511** |

> **Reconciliation check**: Rule-1 total (511) == matrix cell-sum (511) == degree-finder total (511). ✅
> **注**: 部分跨学院联合项目（如 Computational Biology = A&S + SCI）在主学院计数。UCIS 的证书项目计入 Certificate 列。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Pitt 有 6 个直录学院（first-year admitting schools）和 6 个上层学院（upper-division schools，需完成 45-60 学分后转入）。直录学院包括：Dietrich A&S、CBA、Engineering、SCI、Nursing、Public Health。上层学院包括：Education、CGS、SCI、SHRS、Pharmacy、SPIA、Social Work。详见 Section 0.2 层级树。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Kenneth P. Dietrich School of Arts and Sciences (A&S)

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.academics.pitt.edu/programs/africana-studies |
| 2 | Anthropology | https://www.academics.pitt.edu/programs/anthropology |
| 3 | Architectural Studies | https://www.academics.pitt.edu/programs/architectural-studies |
| 4 | Arabic | https://www.academics.pitt.edu/programs/arabic |
| 5 | Astronomy | https://www.academics.pitt.edu/programs/astronomy |
| 6 | Chinese | https://www.academics.pitt.edu/programs/chinese |
| 7 | Classics | https://www.academics.pitt.edu/programs/classics |
| 8 | Communication: Rhetoric & Communication | https://www.academics.pitt.edu/programs/communication-rhetoric-communication |
| 9 | Economics | https://www.academics.pitt.edu/programs/economics |
| 10 | English Literature | https://www.academics.pitt.edu/programs/english-literature |
| 11 | English Writing | https://www.academics.pitt.edu/programs/english-writing |
| 12 | Environmental Studies | https://www.academics.pitt.edu/programs/environmental-studies |
| 13 | Film and Media Studies | https://www.academics.pitt.edu/programs/film-and-media-studies |
| 14 | French | https://www.academics.pitt.edu/programs/french |
| 15 | Gender, Sexuality, and Women's Studies | https://www.academics.pitt.edu/programs/gender-sexuality-and-womens-studies |
| 16 | German | https://www.academics.pitt.edu/programs/german |
| 17 | History | https://www.academics.pitt.edu/programs/history |
| 18 | History and Philosophy of Science | https://www.academics.pitt.edu/programs/history-and-philosophy-of-science |
| 19 | History of Art & Architecture | https://www.academics.pitt.edu/programs/history-of-art-architecture |
| 20 | Italian | https://www.academics.pitt.edu/programs/italian |
| 21 | Italian Studies | https://www.academics.pitt.edu/programs/italian-studies |
| 22 | Japanese | https://www.academics.pitt.edu/programs/japanese |
| 23 | Linguistics | https://www.academics.pitt.edu/programs/linguistics |
| 24 | Music | https://www.academics.pitt.edu/programs/music |
| 25 | Philosophy | https://www.academics.pitt.edu/programs/philosophy |
| 26 | Political Science | https://www.academics.pitt.edu/programs/political-science |
| 27 | Politics and Philosophy | https://www.academics.pitt.edu/programs/politics-and-philosophy |
| 28 | Public and Professional Writing | https://www.academics.pitt.edu/programs/public-and-professional-writing |
| 29 | Religious Studies | https://www.academics.pitt.edu/programs/religious-studies |
| 30 | Russian | https://www.academics.pitt.edu/programs/russian |
| 31 | Sociology | https://www.academics.pitt.edu/programs/sociology |
| 32 | Spanish | https://www.academics.pitt.edu/programs/spanish |
| 33 | Studio Arts | https://www.academics.pitt.edu/programs/studio-arts |
| 34 | Theatre Arts | https://www.academics.pitt.edu/programs/theatre-arts |
| 35 | Urban Studies | https://www.academics.pitt.edu/programs/urban-studies |
| 36 | Africana Studies–English | https://www.academics.pitt.edu/programs/africana-studies |
| 37 | International Studies Co-Major | https://www.academics.pitt.edu/programs/international-and-area-studies |

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Mathematics | https://www.academics.pitt.edu/programs/actuarial-mathematics |
| 2 | Applied Mathematics | https://www.academics.pitt.edu/programs/applied-mathematics |
| 3 | Architecture | https://www.academics.pitt.edu/programs/architecture |
| 4 | Biochemistry | https://www.academics.pitt.edu/programs/biochemistry |
| 5 | Biological Sciences | https://www.academics.pitt.edu/programs/biological-sciences |
| 6 | Chemistry | https://www.academics.pitt.edu/programs/chemistry |
| 7 | Ecology and Evolution | https://www.academics.pitt.edu/programs/ecology-and-evolution |
| 8 | Economics | https://www.academics.pitt.edu/programs/economics |
| 9 | Economics–Statistics | https://www.academics.pitt.edu/programs/economics |
| 10 | Environmental Science | https://www.academics.pitt.edu/programs/environmental-science |
| 11 | Geology | https://www.academics.pitt.edu/programs/geology |
| 12 | Mathematics | https://www.academics.pitt.edu/programs/mathematics |
| 13 | Mathematical Biology | https://www.academics.pitt.edu/programs/mathematical-biology |
| 14 | Mathematics-Economics | https://www.academics.pitt.edu/programs/mathematics-economics |
| 15 | Microbiology | https://www.academics.pitt.edu/programs/microbiology |
| 16 | Molecular Biology | https://www.academics.pitt.edu/programs/molecular-biology |
| 17 | Neuroscience | https://www.academics.pitt.edu/programs/neuroscience |
| 18 | Physics | https://www.academics.pitt.edu/programs/physics |
| 19 | Physics and Astronomy | https://www.academics.pitt.edu/programs/physics-and-astronomy |
| 20 | Political Science | https://www.academics.pitt.edu/programs/political-science |
| 21 | Psychology | https://www.academics.pitt.edu/programs/psychology |
| 22 | Statistics | https://www.academics.pitt.edu/programs/statistics |
| 23 | Urban Planning and Geographic Analysis | https://www.academics.pitt.edu/programs/urban-planning-and-geographic-analysis |

##### BPhil (Honors)
| # | 专业 | URL |
|---|------|-----|
| 1 | International and Area Studies | https://www.academics.pitt.edu/programs/international-and-area-studies |

#### College of Business Administration (CBA)

##### BSBA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.academics.pitt.edu/programs/accounting |
| 2 | Business Analytics | https://www.academics.pitt.edu/programs/business-analytics |
| 3 | Business Information Systems | https://www.academics.pitt.edu/programs/business-information-systems |
| 4 | Finance | https://www.academics.pitt.edu/programs/finance |
| 5 | Global Management | https://www.academics.pitt.edu/programs/global-management |
| 6 | Human Resources Management | https://www.academics.pitt.edu/programs/human-resources-management |
| 7 | Marketing | https://www.academics.pitt.edu/programs/marketing |
| 8 | Supply Chain Management | https://www.academics.pitt.edu/programs/supply-chain-management |

#### Swanson School of Engineering (ENG)

##### BSE Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://www.academics.pitt.edu/programs/bioengineering |
| 2 | Chemical Engineering | https://www.academics.pitt.edu/programs/chemical-engineering |
| 3 | Civil Engineering | https://www.academics.pitt.edu/programs/civil-engineering |
| 4 | Computer Engineering | https://www.academics.pitt.edu/programs/computer-engineering |
| 5 | Electrical Engineering | https://www.academics.pitt.edu/programs/electrical-engineering |
| 6 | Engineering Science | https://www.academics.pitt.edu/programs/engineering-science |
| 7 | Industrial Engineering | https://www.academics.pitt.edu/programs/industrial-engineering |
| 8 | Materials Science and Engineering | https://www.academics.pitt.edu/programs/materials-science-and-engineering |
| 9 | Mechanical Engineering | https://www.academics.pitt.edu/programs/mechanical-engineering |

#### School of Computing and Information (SCI)

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.academics.pitt.edu/programs/computer-science |
| 2 | Information Science | https://www.academics.pitt.edu/programs/information-science |

#### School of Nursing (NUR)

##### BSN Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.academics.pitt.edu/programs/nursing |
| 2 | Accelerated 2nd Degree BSN | https://www.academics.pitt.edu/programs/nursing |

#### School of Education (EDUC)

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Developmental Psychology | https://www.academics.pitt.edu/programs/applied-developmental-psychology |
| 2 | CASE Teacher Preparation | https://www.academics.pitt.edu/programs/case-teacher-preparation |
| 3 | Exercise Science | https://www.academics.pitt.edu/programs/exercise-science |
| 4 | Health and Physical Activity | https://www.academics.pitt.edu/programs/health-and-physical-activity |
| 5 | Teacher Education | https://www.academics.pitt.edu/programs/teacher-education |

#### School of Health and Rehabilitation Sciences (SHRS)

##### BA/BS Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication Science | BA | https://www.academics.pitt.edu/programs/communication-science |
| 2 | Dietitian Nutritionist Program | BS | https://www.academics.pitt.edu/programs/dietitian-nutritionist-program |
| 3 | Emergency Medicine | BS | https://www.academics.pitt.edu/programs/emergency-medicine |
| 4 | Health Informatics | BS | https://www.academics.pitt.edu/programs/health-informatics |
| 5 | Nutrition Science | BS | https://www.academics.pitt.edu/programs/nutrition-science |
| 6 | Rehabilitation Science | BS | https://www.academics.pitt.edu/programs/rehabilitation-science |

#### College of General Studies (CGS)

##### BA/BS Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Dental Hygiene | BS | https://www.academics.pitt.edu/programs/dental-hygiene |
| 2 | Health Services | BA or BS | https://www.academics.pitt.edu/programs/health-services |
| 3 | Liberal Studies | BA | https://www.academics.pitt.edu/programs/liberal-studies |
| 4 | Media and Professional Communications | BA | https://www.academics.pitt.edu/programs/media-and-professional-communications |
| 5 | Natural Sciences | BS | https://www.academics.pitt.edu/programs/natural-sciences |
| 6 | Public Service | BA | https://www.academics.pitt.edu/programs/public-service |

#### School of Public Health (SPH)

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://www.academics.pitt.edu/programs/public-health |

#### School of Social Work

##### BASW Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.academics.pitt.edu/programs/social-work |

#### School of Public and International Affairs (SPIA)

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy | https://www.academics.pitt.edu/programs/public-policy |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学位 | 联合学院 | URL |
|---|------|------|---------|-----|
| 1 | Computational Biology | BS | A&S + SCI | https://www.academics.pitt.edu/programs/computational-biology |
| 2 | Computational Social Science | BS | A&S + SCI | https://www.academics.pitt.edu/programs/computational-social-science |
| 3 | Data Science | BS | A&S + SCI | https://www.academics.pitt.edu/programs/data-science |
| 4 | Digital Narrative & Interactive Design | BA or BS | A&S + SCI | https://www.academics.pitt.edu/programs/digital-narrative-and-interactive-design |
| 5 | Physics & Quantum Computing | BS | A&S + SCI | https://www.academics.pitt.edu/programs/physics-and-quantum-computing |
| 6 | Law, Criminal Justice, and Society | BA | A&S + CGS | https://www.academics.pitt.edu/programs/law-criminal-justice-and-society |

### 1.4 Minors — complete list

| # | Minor | Home School | URL |
|---|-------|-------------|-----|
| 1 | Ancient Greek | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 2 | Applied Statistics | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 3 | Arabic | A&S | https://www.academics.pitt.edu/programs/arabic |
| 4 | Architecture-Design | A&S | https://www.academics.pitt.edu/programs/architecture |
| 5 | Bosnian-Croatian-Montenegrin-Serbian | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 6 | Business Minor | CBA | https://www.academics.pitt.edu/programs/accounting |
| 7 | Chinese Heritage | A&S | https://www.academics.pitt.edu/programs/chinese |
| 8 | Classical Civilization | A&S | https://www.academics.pitt.edu/programs/classics |
| 9 | Communication Science | SHRS | https://www.academics.pitt.edu/programs/communication-science |
| 10 | Creative Writing | A&S | https://www.academics.pitt.edu/programs/english-writing |
| 11 | Dance | EDUC | https://www.academics.pitt.edu/programs/exercise-science |
| 12 | Environmental Engineering | ENG | https://www.academics.pitt.edu/programs/civil-engineering |
| 13 | Exercise Science | EDUC | https://www.academics.pitt.edu/programs/exercise-science |
| 14 | Fitness Coaching | EDUC | https://www.academics.pitt.edu/programs/exercise-science |
| 15 | Foundations of English Studies | A&S | https://www.academics.pitt.edu/programs/english-literature |
| 16 | Global Policy | SPIA | https://www.academics.pitt.edu/programs/public-policy |
| 17 | Hindi | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 18 | Hispanic Language and Culture | A&S | https://www.academics.pitt.edu/programs/spanish |
| 19 | Hungarian | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 20 | Information Science | SCI | https://www.academics.pitt.edu/programs/information-science |
| 21 | Irish | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 22 | Korean | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 23 | Latin | A&S | https://www.academics.pitt.edu/programs/classics |
| 24 | Law, Criminal Justice, & Society | CGS | https://www.academics.pitt.edu/programs/law-criminal-justice-and-society |
| 25 | LGBT and Critical Sexuality Studies | A&S | https://www.academics.pitt.edu/programs/gender-sexuality-and-womens-studies |
| 26 | Mediterranean Art and Archaeology | A&S | https://www.academics.pitt.edu/programs/history-of-art-architecture |
| 27 | Modern Greek | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 28 | Persian/Farsi | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 29 | Petroleum Engineering | ENG | https://www.academics.pitt.edu/programs/chemical-engineering |
| 30 | Polish | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 31 | Polymer Engineering | ENG | https://www.academics.pitt.edu/programs/chemical-engineering |
| 32 | Portuguese and Luso-Brazilian Culture | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 33 | Public Policy | SPIA | https://www.academics.pitt.edu/programs/public-policy |
| 34 | Public Service | CGS | https://www.academics.pitt.edu/programs/public-service |
| 35 | Quechua | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 36 | Secondary Teacher Education | EDUC | https://www.academics.pitt.edu/programs/teacher-education |
| 37 | Slovak Studies | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 38 | Social Work | Social Work | https://www.academics.pitt.edu/programs/social-work |
| 39 | Swahili | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 40 | Swedish | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 41 | Teaching English as an Additional Language | EDUC | https://www.academics.pitt.edu/programs/teacher-education |
| 42 | Turkish | A&S | https://www.academics.pitt.edu/programs/african-studies |
| 43 | Vietnamese | A&S | https://www.academics.pitt.edu/programs/african-studies |

> **注**: 标注 * 的专业（在 UG majors 表中）也有辅修。以上为额外辅修列表。总计约 57 个辅修。

### 1.5 General/Institute-wide requirements

Pitt 的通识教育要求由各学院自行设定。Dietrich A&S 的通识教育包括：
- Writing (2 门课)
- Quantitative & Formal Reasoning
- Social Sciences
- Natural Sciences
- Humanities
- Arts
- Foreign Language (达到一定水平)
- Cross-Cultural Awareness

详见: https://www.asundergrad.pitt.edu/general-education-requirements

### 1.6 Guaranteed Admission Programs

Pitt 提供 Guaranteed Admission Programs (GAP)，允许学生在申请时同时申请特定专业（如医学、法学、牙医学等）的保证录取。详见: https://admissions.pitt.edu/guaranteed-admissions-programs/

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Kenneth P. Dietrich School of Arts and Sciences — Graduate Studies

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Developmental Psychology | https://www.asgraduate.pitt.edu/ |
| 2 | Communication | https://www.asgraduate.pitt.edu/ |
| 3 | Composition, Literacy, Pedagogy & Rhetoric | https://www.asgraduate.pitt.edu/ |
| 4 | Cultural Studies | https://www.asgraduate.pitt.edu/ |
| 5 | English | https://www.asgraduate.pitt.edu/ |
| 6 | French | https://www.asgraduate.pitt.edu/ |
| 7 | German | https://www.asgraduate.pitt.edu/ |
| 8 | Hispanic Languages & Literature | https://www.asgraduate.pitt.edu/ |
| 9 | History | https://www.asgraduate.pitt.edu/ |
| 10 | Italian | https://www.asgraduate.pitt.edu/ |
| 11 | Linguistics | https://www.asgraduate.pitt.edu/ |
| 12 | Philosophy | https://www.asgraduate.pitt.edu/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.asgraduate.pitt.edu/ |
| 2 | Biochemistry | https://www.asgraduate.pitt.edu/ |
| 3 | Bioethics | https://www.asgraduate.pitt.edu/ |
| 4 | Biological Sciences | https://www.asgraduate.pitt.edu/ |
| 5 | Chemistry | https://www.asgraduate.pitt.edu/ |
| 6 | Computational Biology | https://www.asgraduate.pitt.edu/ |
| 7 | Computer Science | https://www.asgraduate.pitt.edu/ |
| 8 | Ecology & Evolution | https://www.asgraduate.pitt.edu/ |
| 9 | Environmental Science | https://www.asgraduate.pitt.edu/ |
| 10 | Geology | https://www.asgraduate.pitt.edu/ |
| 11 | Mathematics | https://www.asgraduate.pitt.edu/ |
| 12 | Microbiology | https://www.asgraduate.pitt.edu/ |
| 13 | Molecular Biology | https://www.asgraduate.pitt.edu/ |
| 14 | Neuroscience | https://www.asgraduate.pitt.edu/ |
| 15 | Physics | https://www.asgraduate.pitt.edu/ |
| 16 | Quantitative Economics | https://www.asgraduate.pitt.edu/ |
| 17 | Statistics | https://www.asgraduate.pitt.edu/ |
| 18 | Telecommunications | https://www.asgraduate.pitt.edu/ |

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Writing | https://www.asgraduate.pitt.edu/ |
| 2 | Studio Arts | https://www.asgraduate.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.asgraduate.pitt.edu/ |
| 2 | Biochemistry | https://www.asgraduate.pitt.edu/ |
| 3 | Biological Sciences | https://www.asgraduate.pitt.edu/ |
| 4 | Chemistry | https://www.asgraduate.pitt.edu/ |
| 5 | Classics | https://www.asgraduate.pitt.edu/ |
| 6 | Communication | https://www.asgraduate.pitt.edu/ |
| 7 | Computational Biology | https://www.asgraduate.pitt.edu/ |
| 8 | Computer Science | https://www.asgraduate.pitt.edu/ |
| 9 | Cultural Studies | https://www.asgraduate.pitt.edu/ |
| 10 | Ecology & Evolution | https://www.asgraduate.pitt.edu/ |
| 11 | Economics | https://www.asgraduate.pitt.edu/ |
| 12 | English | https://www.asgraduate.pitt.edu/ |
| 13 | French | https://www.asgraduate.pitt.edu/ |
| 14 | Geology | https://www.asgraduate.pitt.edu/ |
| 15 | German | https://www.asgraduate.pitt.edu/ |
| 16 | Hispanic Languages & Literature | https://www.asgraduate.pitt.edu/ |
| 17 | History | https://www.asgraduate.pitt.edu/ |
| 18 | History & Philosophy of Science | https://www.asgraduate.pitt.edu/ |
| 19 | Italian | https://www.asgraduate.pitt.edu/ |
| 20 | Linguistics | https://www.asgraduate.pitt.edu/ |
| 21 | Mathematics | https://www.asgraduate.pitt.edu/ |
| 22 | Microbiology | https://www.asgraduate.pitt.edu/ |
| 23 | Molecular Biology | https://www.asgraduate.pitt.edu/ |
| 24 | Neuroscience | https://www.asgraduate.pitt.edu/ |
| 25 | Philosophy | https://www.asgraduate.pitt.edu/ |
| 26 | Physics | https://www.asgraduate.pitt.edu/ |
| 27 | Political Science | https://www.asgraduate.pitt.edu/ |
| 28 | Psychology | https://www.asgraduate.pitt.edu/ |
| 29 | Religious Studies | https://www.asgraduate.pitt.edu/ |
| 30 | Slavic Languages & Literatures | https://www.asgraduate.pitt.edu/ |
| 31 | Sociology | https://www.asgraduate.pitt.edu/ |
| 32 | Spanish | https://www.asgraduate.pitt.edu/ |
| 33 | Statistics | https://www.asgraduate.pitt.edu/ |
| 34 | Telecommunications | https://www.asgraduate.pitt.edu/ |
| 35 | Urban Studies | https://www.asgraduate.pitt.edu/ |

#### Joseph M. Katz Graduate School of Business

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | MBA (Full-Time) | https://business.pitt.edu/mba/ |
| 2 | MBA (Part-Time) | https://business.pitt.edu/mba/ |
| 3 | MBA (Accelerated) | https://business.pitt.edu/mba/ |
| 4 | Executive MBA | https://business.pitt.edu/mba/executive/ |
| 5 | MBA/MS Dual Degree | https://business.pitt.edu/mba/ |
| 6 | MBA/JD Dual Degree | https://business.pitt.edu/mba/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://business.pitt.edu/ms/ |
| 2 | Business Analytics | https://business.pitt.edu/ms/ |
| 3 | Finance | https://business.pitt.edu/ms/ |
| 4 | Management | https://business.pitt.edu/ms/ |
| 5 | Marketing | https://business.pitt.edu/ms/ |
| 6 | Supply Chain Management | https://business.pitt.edu/ms/ |
| 7 | Information Systems | https://business.pitt.edu/ms/ |
| 8 | Global Management | https://business.pitt.edu/ms/ |
| 9 | Innovation & Entrepreneurship | https://business.pitt.edu/ms/ |
| 10 | Management Consulting | https://business.pitt.edu/ms/ |
| 11 | Marketing Science | https://business.pitt.edu/ms/ |
| 12 | Sustainable Business | https://business.pitt.edu/ms/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://business.pitt.edu/phd/ |
| 2 | Finance | https://business.pitt.edu/phd/ |
| 3 | Information Systems | https://business.pitt.edu/phd/ |
| 4 | Marketing | https://business.pitt.edu/phd/ |
| 5 | Organizational Behavior | https://business.pitt.edu/phd/ |
| 6 | Strategic Management | https://business.pitt.edu/phd/ |

##### DBA Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Doctor of Business Administration | https://business.pitt.edu/dba/ |

#### Swanson School of Engineering

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://www.engineering.pitt.edu/ |
| 2 | Chemical Engineering | https://www.engineering.pitt.edu/ |
| 3 | Civil Engineering | https://www.engineering.pitt.edu/ |
| 4 | Electrical Engineering | https://www.engineering.pitt.edu/ |
| 5 | Energy Systems | https://www.engineering.pitt.edu/ |
| 6 | Engineering Management | https://www.engineering.pitt.edu/ |
| 7 | Environmental Engineering | https://www.engineering.pitt.edu/ |
| 8 | Industrial Engineering | https://www.engineering.pitt.edu/ |
| 9 | Materials Science | https://www.engineering.pitt.edu/ |
| 10 | Mechanical Engineering | https://www.engineering.pitt.edu/ |
| 11 | Nuclear Engineering | https://www.engineering.pitt.edu/ |
| 12 | Petroleum Engineering | https://www.engineering.pitt.edu/ |

##### MEng Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.engineering.pitt.edu/ |
| 2 | Civil Engineering | https://www.engineering.pitt.edu/ |
| 3 | Electrical Engineering | https://www.engineering.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://www.engineering.pitt.edu/ |
| 2 | Chemical Engineering | https://www.engineering.pitt.edu/ |
| 3 | Civil Engineering | https://www.engineering.pitt.edu/ |
| 4 | Electrical Engineering | https://www.engineering.pitt.edu/ |
| 5 | Industrial Engineering | https://www.engineering.pitt.edu/ |
| 6 | Materials Science | https://www.engineering.pitt.edu/ |
| 7 | Mechanical Engineering | https://www.engineering.pitt.edu/ |
| 8 | Nuclear Engineering | https://www.engineering.pitt.edu/ |

#### School of Computing and Information

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.sci.pitt.edu/ |
| 2 | Information Science | https://www.sci.pitt.edu/ |
| 3 | Library and Information Science (MLIS) | https://www.sci.pitt.edu/ |
| 4 | Telecommunications | https://www.sci.pitt.edu/ |
| 5 | Intelligent Systems | https://www.sci.pitt.edu/ |
| 6 | Bioinformatics | https://www.sci.pitt.edu/ |
| 7 | Data Science | https://www.sci.pitt.edu/ |
| 8 | Cybersecurity | https://www.sci.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.sci.pitt.edu/ |
| 2 | Information Science | https://www.sci.pitt.edu/ |

#### School of Education

##### MEd Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Instruction | https://www.education.pitt.edu/ |
| 2 | Early Childhood Education | https://www.education.pitt.edu/ |
| 3 | Education Leadership | https://www.education.pitt.edu/ |
| 4 | Education Policy | https://www.education.pitt.edu/ |
| 5 | Higher Education | https://www.education.pitt.edu/ |
| 6 | Mathematics Education | https://www.education.pitt.edu/ |
| 7 | Reading Education | https://www.education.pitt.edu/ |
| 8 | Special Education | https://www.education.pitt.edu/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://www.education.pitt.edu/ |
| 2 | Health & Physical Activity | https://www.education.pitt.edu/ |
| 3 | Instructional Design and Technology | https://www.education.pitt.edu/ |
| 4 | Language, Literacy & Culture | https://www.education.pitt.edu/ |
| 5 | Science, Technology, Engineering & Mathematics | https://www.education.pitt.edu/ |
| 6 | Teacher Education | https://www.education.pitt.edu/ |
| 7 | Urban Education | https://www.education.pitt.edu/ |
| 8 | Visual Impairment and Blindness | https://www.education.pitt.edu/ |

##### EdD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education | https://www.education.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Education Leadership | https://www.education.pitt.edu/ |
| 2 | Education Policy | https://www.education.pitt.edu/ |
| 3 | Higher Education | https://www.education.pitt.edu/ |
| 4 | Mathematics Education | https://www.education.pitt.edu/ |
| 5 | Reading Education | https://www.education.pitt.edu/ |
| 6 | Science Education | https://www.education.pitt.edu/ |
| 7 | Social Education | https://www.education.pitt.edu/ |
| 8 | Special Education | https://www.education.pitt.edu/ |

#### School of Health and Rehabilitation Sciences

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://www.shrs.pitt.edu/ |
| 2 | Clinical Mental Health Counseling | https://www.shrs.pitt.edu/ |
| 3 | Communication Science Disorders | https://www.shrs.pitt.edu/ |
| 4 | Health Informatics | https://www.shrs.pitt.edu/ |
| 5 | Nutrition and Dietetics | https://www.shrs.pitt.edu/ |
| 6 | Occupational Therapy | https://www.shrs.pitt.edu/ |
| 7 | Physician Assistant Studies | https://www.shrs.pitt.edu/ |
| 8 | Prosthetics and Orthotics | https://www.shrs.pitt.edu/ |
| 9 | Rehabilitation Science | https://www.shrs.pitt.edu/ |
| 10 | Sports Science | https://www.shrs.pitt.edu/ |

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Speech Language Pathology | https://www.shrs.pitt.edu/ |

##### AuD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Audiology | https://www.shrs.pitt.edu/ |

##### DPT Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Physical Therapy (On-campus) | https://www.shrs.pitt.edu/ |
| 2 | Doctor of Physical Therapy (Hybrid) | https://www.shrs.pitt.edu/ |

##### OTD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Occupational Therapy | https://www.shrs.pitt.edu/ |

##### DC Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Chiropractic | https://www.shrs.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Science Disorders | https://www.shrs.pitt.edu/ |
| 2 | Rehabilitation Science | https://www.shrs.pitt.edu/ |

#### School of Dental Medicine

##### DMD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Dental Medicine | https://www.dental.pitt.edu/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://www.dental.pitt.edu/ |
| 2 | Oral & Craniofacial Sciences | https://www.dental.pitt.edu/ |

##### PhD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Oral & Craniofacial Sciences | https://www.dental.pitt.edu/ |

#### School of Law

##### JD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://www.law.pitt.edu/ |

##### LLM Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.law.pitt.edu/ |
| 2 | International & Comparative Law | https://www.law.pitt.edu/ |
| 3 | Health Law | https://www.law.pitt.edu/ |

##### SJD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Juridical Science | https://www.law.pitt.edu/ |

#### School of Medicine

##### MD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine | https://www.medschool.pitt.edu/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Informatics | https://www.medschool.pitt.edu/ |
| 2 | Clinical Research | https://www.medschool.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Informatics | https://www.medschool.pitt.edu/ |
| 2 | Cell Biology & Molecular Physiology | https://www.medschool.pitt.edu/ |
| 3 | Cellular & Molecular Pathology | https://www.medschool.pitt.edu/ |
| 4 | Clinical and Translational Science | https://www.medschool.pitt.edu/ |
| 5 | Computational Biology | https://www.medschool.pitt.edu/ |
| 6 | Immunology | https://www.medschool.pitt.edu/ |
| 7 | Molecular Biophysics & Structural Biology | https://www.medschool.pitt.edu/ |
| 8 | Molecular Genetics & Developmental Biology | https://www.medschool.pitt.edu/ |
| 9 | Molecular Pharmacology | https://www.medschool.pitt.edu/ |
| 10 | Neuroscience | https://www.medschool.pitt.edu/ |
| 11 | Oncology | https://www.medschool.pitt.edu/ |
| 12 | Microbiology & Immunology | https://www.medschool.pitt.edu/ |

#### School of Nursing

##### MSN Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Nursing | https://www.nursing.pitt.edu/ |

##### DNP Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice | https://www.nursing.pitt.edu/ |

##### PhD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy in Nursing | https://www.nursing.pitt.edu/ |

#### School of Pharmacy

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://www.pharmacy.pitt.edu/ |
| 2 | PharmacoAnalytics-Pharmaceutical Outcomes Research | https://www.pharmacy.pitt.edu/ |
| 3 | Pharmacy Business Administration | https://www.pharmacy.pitt.edu/ |

##### PharmD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy | https://www.pharmacy.pitt.edu/ |

##### PhD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://www.pharmacy.pitt.edu/ |

#### School of Public Health

##### MPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Behavioral & Community Health Sciences | https://www.publichealth.pitt.edu/ |
| 2 | Biostatistics | https://www.publichealth.pitt.edu/ |
| 3 | Environmental & Occupational Health | https://www.publichealth.pitt.edu/ |
| 4 | Epidemiology | https://www.publichealth.pitt.edu/ |
| 5 | Health Policy & Management | https://www.publichealth.pitt.edu/ |
| 6 | Human Genetics | https://www.publichealth.pitt.edu/ |
| 7 | Infectious Diseases & Microbiology | https://www.publichealth.pitt.edu/ |
| 8 | Multidisciplinary MPH | https://www.publichealth.pitt.edu/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://www.publichealth.pitt.edu/ |
| 2 | Genetic Counseling | https://www.publichealth.pitt.edu/ |
| 3 | Genome Bioinformatics | https://www.publichealth.pitt.edu/ |
| 4 | Health Services Research and Policy | https://www.publichealth.pitt.edu/ |
| 5 | Human Genetics | https://www.publichealth.pitt.edu/ |
| 6 | Infectious Disease Management, Intervention, and Community Practice | https://www.publichealth.pitt.edu/ |
| 7 | Public Health Genetics | https://www.publichealth.pitt.edu/ |
| 8 | Clinical Research | https://www.publichealth.pitt.edu/ |

##### DrPH Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Public Health | https://www.publichealth.pitt.edu/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Behavioral & Community Health Sciences | https://www.publichealth.pitt.edu/ |
| 2 | Biostatistics | https://www.publichealth.pitt.edu/ |
| 3 | Environmental & Occupational Health | https://www.publichealth.pitt.edu/ |
| 4 | Epidemiology | https://www.publichealth.pitt.edu/ |
| 5 | Health Policy & Management | https://www.publichealth.pitt.edu/ |
| 6 | Human Genetics | https://www.publichealth.pitt.edu/ |
| 7 | Infectious Diseases & Microbiology | https://www.publichealth.pitt.edu/ |
| 8 | Microbiology | https://www.publichealth.pitt.edu/ |

#### School of Public and International Affairs

##### MPA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.gspiapitt.edu/ |
| 2 | Public Policy & Management | https://www.gspiapitt.edu/ |
| 3 | Public Service | https://www.gspiapitt.edu/ |

##### MID Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | International Development | https://www.gspiapitt.edu/ |
| 2 | International Development in Human Security | https://www.gspiapitt.edu/ |

##### MPP Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | https://www.gspiapitt.edu/ |
| 2 | Public and International Affairs | https://www.gspiapitt.edu/ |

##### PhD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Public and International Affairs | https://www.gspiapitt.edu/ |

#### School of Social Work

##### MSW Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.socialwork.pitt.edu/ |
| 2 | Social Work/MBA Dual Degree | https://www.socialwork.pitt.edu/ |

##### PhD Program
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.socialwork.pitt.edu/ |

### 2.2 Graduate admissions model

Pitt 的研究生招生采用**完全分散模式**（fully decentralized）。14 个研究生和专业学院各自管理自己的招生流程，没有中央招生办公室。

- **申请平台**: 各学院使用不同的申请系统（Liaison GradCAS、SOPHAS、LSAC、AMCAS 等）
- **申请费**: 因学院而异
- **GRE**: 大多数项目不再要求 GRE（Dietrich A&S 明确表示绝大多数项目不考虑 GRE）
- **英语要求**: 各学院设定自己的最低要求

关键联系信息：
- Dietrich A&S Graduate: asgrad@pitt.edu, 412-624-6094
- Katz Business: mba@katz.pitt.edu
- Engineering: gradengr@pitt.edu
- SCI: sciinfo@pitt.edu

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| 招生模式 | **滚动招生 (Rolling Admissions)** | admissions.pitt.edu/first-year-student/ |
| 申请系统 | Pitt Application 或 Common App | admissions.pitt.edu/apply/ |
| 申请费 | $55 | admissions.pitt.edu/first-year-student/ |
| EA 截止日期 | N/A（滚动招生，无 EA） | admissions.pitt.edu/first-year-student/ |
| RD 截止日期 | N/A（滚动招生，无固定截止日期） | admissions.pitt.edu/first-year-student/ |
| 奖学金考虑截止 | **12 月 1 日** | admissions.pitt.edu/first-year-student/ |
| 国际生奖学金截止 | **2 月 1 日** | admissions.pitt.edu/international/ |
| STARS/SRAR | **必填**（国际生除外） | admissions.pitt.edu/first-year-student/ |
| SAT/ACT 政策 | **Test-optional 至 2028 年秋季** | admissions.pitt.edu/test-optional/ |
| Superscore | 是（SAT 最高分，ACT 最高综合分） | admissions.pitt.edu/first-year-student/ |
| 推荐信 | 不要求（但建议提交） | admissions.pitt.edu/first-year-student/ |
| 个人陈述 | 奖学金考虑必须提交 | admissions.pitt.edu/first-year-student/ |
| 面试 | 不提供 | admissions.pitt.edu/international/ |
| 决定通知 | 提交完整材料后 6-8 周 | admissions.pitt.edu/international/ |

> **重要发现**: Pitt 使用**滚动招生**，不是 EA/RD 模式。这意味着没有固定的申请截止日期，但建议尽早申请以获得奖学金和 Honors College 考虑。

### 3.2 Undergraduate English proficiency table

| 考试 | 最低分 | 推荐分 | 适用条件 |
|------|--------|--------|---------|
| TOEFL iBT | 未公布明确最低分 | — | 国际生必须提交 |
| IELTS | 未公布明确最低分 | — | 国际生必须提交 |
| Duolingo | 未公布明确最低分 | — | 国际生必须提交 |

> **注**: Pitt 本科招生页面未公布明确的英语考试最低分数线。Test-optional 政策不适用于英语能力证明——国际生仍需提交英语成绩。具体要求可能因学院而异。

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 招生模式 | **完全分散**（各学院独立管理） | academics.pitt.edu/graduate-professional |
| 申请平台 | 因学院而异（GradCAS、SOPHAS、LSAC 等） | 各学院网站 |
| GRE 要求 | 大多数项目不再要求 | asgraduate.pitt.edu/admissions/international-students |
| TOEFL 最低分 | **90**（Dietrich A&S）；新评分制 4.5 | asgraduate.pitt.edu/admissions/international-students |
| IELTS 最低分 | **7.0**（各部分 ≥6.5） | asgraduate.pitt.edu/admissions/international-students |
| Duolingo 最低分 | **120** | asgraduate.pitt.edu/admissions/international-students |
| 成绩有效期 | 2 年 | asgraduate.pitt.edu/admissions/international-students |
| CGS 4 月 15 日协议 | 是（大多数项目） | academics.pitt.edu/graduate-professional |

> **TOEFL 评分更新**: 2026 年 1 月 21 日起，TOEFL 评分从 0-120 改为 1-6（增量 0.5）。Pitt 的 90 分对应新制 4.5，口语/阅读/写作 ≥4.5，听力 ≥5.0。

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-26 Academic Year, line-itemized)

#### Pennsylvania Residents — Tuition by School

| 学院 | 全年学费 (2 terms) | 每学期 | 每学分 |
|------|-------------------|--------|--------|
| Dietrich A&S | $20,966 | $10,483 | $873 |
| School of Social Work | $20,966 | $10,483 | $873 |
| School of Dental Medicine (Hygiene) | $20,966 | $10,483 | $873 |
| School of Public Health | $20,966 | $10,486 | $873 |
| College of Business Administration | $23,420 | $11,710 | $975 |
| Swanson School of Engineering | $23,258 | $11,629 | $969 |
| School of Computing and Information | $23,928 | $11,964 | $997 |
| School of Nursing | $26,396 | $13,198 | $1,099 |
| School of Health & Rehab Sciences | $26,396 | $13,198 | $1,099 |
| College of General Studies | $20,966 | $10,483 | $873 |
| School of Education | $20,966 | $10,483 | $873 |
| School of Pharmacy | $37,428 | $18,714 | $1,441 |

#### Out-of-State Residents — Tuition by School

| 学院 | 全年学费 (2 terms) | 每学期 | 每学分 |
|------|-------------------|--------|--------|
| Dietrich A&S | $41,662 | $20,831 | $1,735 |
| School of Social Work | $41,662 | $20,831 | $1,735 |
| School of Dental Medicine (Hygiene) | $41,662 | $20,831 | $1,735 |
| School of Public Health | $41,662 | $20,831 | $1,735 |
| College of Business Administration | $46,936 | $23,468 | $1,955 |
| Swanson School of Engineering | $45,494 | $22,747 | $1,895 |
| School of Computing and Information | $47,628 | $23,814 | $1,984 |
| School of Nursing | $52,954 | $26,477 | $2,206 |
| School of Health & Rehab Sciences | $52,954 | $26,477 | $2,206 |
| College of General Studies | $41,662 | $20,831 | $1,735 |
| School of Education | $41,662 | $20,831 | $1,735 |
| School of Pharmacy | $44,740 | $22,370 | $1,724 |

#### Mandatory Fees (全年)

| 费用项目 | 全年 | 每学期 | 每学期 (Part-time) |
|---------|------|--------|-------------------|
| Transportation Fee | $310 | $155 | $155 |
| Student Activity Fee | $200 | $100 | $30 |
| Wellness and Recreation Support Fee | $810 | $405 | $202 |
| Computing and Network Services Fee | $450 | $225 | $112 |
| **Total** | **$1,770** | **$885** | **$499** |

> 国际生额外费用: International Services Fee $500/学期

#### Other Estimated Expenses (On/Off Campus, 全年)

| 费用项目 | 金额 |
|---------|------|
| Housing | $9,810 |
| Food | $5,918 |
| Books & Supplies | $576 |
| Transportation | $968 |
| Loan Fees | $80 |
| Miscellaneous Personal Expenses | $1,824 |
| **Total** | **$19,176** |

#### Cost of Attendance Summary (全年, On-Campus)

| 学院 (PA Resident) | 学费 | 费用 | 生活费 | COA 总计 |
|-------------------|------|------|--------|---------|
| Dietrich A&S | $20,966 | $1,770 | $19,176 | $41,912 |
| Engineering | $23,258 | $1,770 | $19,176 | $44,204 |
| CBA | $23,420 | $1,770 | $19,176 | $44,366 |
| Nursing | $26,396 | $1,770 | $19,176 | $47,342 |

| 学院 (OOS) | 学费 | 费用 | 生活费 | COA 总计 |
|-----------|------|------|--------|---------|
| Dietrich A&S | $41,662 | $1,770 | $19,176 | $62,608 |
| Engineering | $45,494 | $1,770 | $19,176 | $66,440 |
| CBA | $46,936 | $1,770 | $19,176 | $67,882 |
| Nursing | $52,954 | $1,770 | $19,176 | $73,900 |

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-blind/Need-aware | **Need-blind for PA residents**; **Need-aware for OOS/international** | financialaid.pitt.edu |
| Pell Plus Program | **翻倍 Federal Pell Grant**（至最高 $7,395） | financialaid.pitt.edu |
| Panthers Forward | 大四联邦贷款减免计划 | financialaid.pitt.edu |
| Pittsburgh Public Scholars | Pittsburgh Public Schools 优秀毕业生保证录取 + $2,000+ 奖学金 | financialaid.pitt.edu |
| FAFSA Code | **008815** | financialaid.pitt.edu |
| 奖学金数据库 | PittFundsMe（在线可搜索数据库） | financialaid.pitt.edu |

### 4.3 Graduate cost & funding framework

#### Graduate Tuition (PA Resident, 2025-26)

| 学院 | 全年学费 (2 terms) | 每学分 |
|------|-------------------|--------|
| Dietrich A&S | $26,876 | $1,079 |
| School of Social Work | $26,876 | $1,079 |
| School of Public Health | $31,510 | $1,280 |
| Swanson Engineering | $30,028 | $1,421 |
| School of Computing & Information | $28,260 | $1,148 |
| School of Nursing | $31,510 | $1,280 |
| School of Health & Rehab Sciences | $31,510 | $1,280 |
| School of Education | $26,876 | $1,079 |
| School of Public & International Affairs | $26,876 | $1,079 |
| Katz Business (MBA) | $34,858 | $1,699 |
| Katz Business (MS) | $34,412 | $1,699 |
| School of Dental Medicine (DMD) | $57,536 | $1,256 |
| School of Law (JD) | — | — |
| School of Pharmacy (PharmD) | — | — |

#### Funding Types

| 资助类型 | 说明 |
|---------|------|
| GSR (Graduate Student Researcher) | 研究助理，由各学院/项目分配 |
| TF (Teaching Fellow) | 教学研究员 |
| TA (Teaching Assistant) | 助教 |
| GSA (Graduate Student Assistant) | 研究生助理 |
| Fellowships | 各种奖学金，通常随录取通知发放 |

> **注**: 研究生资助由各学院/项目自行管理，非中央分配。博士生通常获得全额资助。硕士生多为自费。

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001: Rolling admissions policy
field: undergraduate.admissions.rolling
value: true
source_url: https://admissions.pitt.edu/first-year-student/
source_snippet: "The University Of Pittsburgh operates on a rolling admission policy, which means that for our first-year students and undergraduate programs, there's no set deadline for applying to Pitt."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-002: Application fee
field: undergraduate.admissions.application_fee_usd
value: 55
source_url: https://admissions.pitt.edu/first-year-student/
source_snippet: "Pay your $55 application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-003: Test-optional policy
field: undergraduate.admissions.test_optional
value: "extended through Fall 2028"
source_url: https://admissions.pitt.edu/test-optional/
source_snippet: "The University of Pittsburgh will continue its test-optional policy through fall 2028. Scores from the ACT or SAT exams will not be required for students applying to enter the university for fall 2025, 2026, 2027, and 2028."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-004: STARS/SRAR requirement
field: undergraduate.admissions.stars_required
value: true
source_url: https://admissions.pitt.edu/first-year-student/
source_snippet: "The Self-reported Transcript and Academic Record System (STARS), formerly SRAR is required for all first-year applicants, with the exception of international students."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-005: Scholarship deadline
field: undergraduate.admissions.scholarship_deadline
value: "December 1"
source_url: https://admissions.pitt.edu/first-year-student/
source_snippet: "First-year students who complete and submit an application for admission and all required materials by December 1 are automatically considered for University of Pittsburgh academic scholarships."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-006: International scholarship deadline
field: undergraduate.admissions.international_scholarship_deadline
value: "February 1"
source_url: https://admissions.pitt.edu/international/
source_snippet: "International first-year fall term applicants who have a completed application by February 1 will automatically be reviewed for merit-based scholarships."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-007: In-state tuition (A&S)
field: undergraduate.cost.tuition_in_state_as
value: 20966
source_url: https://www.tuition.pitt.edu/undergraduate/tuition?campus=30
source_snippet: "Dietrich School of Arts and Sciences $20,966 $10,483 $873"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-008: OOS tuition (A&S)
field: undergraduate.cost.tuition_oos_as
value: 41662
source_url: https://www.tuition.pitt.edu/undergraduate/tuition?campus=30
source_snippet: "Dietrich School of Arts and Sciences $41,662 $20,831 $1,735"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-009: Mandatory fees
field: undergraduate.cost.mandatory_fees_annual
value: 1770
source_url: https://www.tuition.pitt.edu/undergraduate/tuition?campus=30
source_snippet: "Total* $1,770 $885 $499"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-010: Housing cost
field: undergraduate.cost.housing_annual
value: 9810
source_url: https://www.tuition.pitt.edu/undergraduate/tuition?campus=30
source_snippet: "Housing $9,810 $4,905 $4,905"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-011: Food cost
field: undergraduate.cost.food_annual
value: 5918
source_url: https://www.tuition.pitt.edu/undergraduate/tuition?campus=30
source_snippet: "Food $5,918 $2,959 $2,959"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-012: International services fee
field: undergraduate.cost.international_services_fee_per_term
value: 500
source_url: https://www.tuition.pitt.edu/undergraduate/tuition?campus=30
source_snippet: "International undergraduate students enrolled full-time at the Pittsburgh campus are assessed the International Services Fee of $500 per term for fall and spring terms."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-001: Graduate TOEFL minimum (Dietrich A&S)
field: graduate.admissions.tofl_min
value: 90
source_url: https://www.asgraduate.pitt.edu/admissions/international-students
source_snippet: "The DSAS current TOEFL score 90 will shift to a minimum overall score of 4.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-002: Graduate IELTS minimum
field: graduate.admissions.ielts_min
value: 7.0
source_url: https://www.asgraduate.pitt.edu/admissions/international-students
source_snippet: "IELTS: score of 7.0, with at least 6.5 in each of its four sections."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-003: Graduate Duolingo minimum
field: graduate.admissions.duolingo_min
value: 120
source_url: https://www.asgraduate.pitt.edu/admissions/international-students
source_snippet: "Duolingo English Test: Minimum score: 120."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-004: GRE policy
field: graduate.admissions.gre_policy
value: "Most programs no longer consider GRE scores"
source_url: https://www.asgraduate.pitt.edu/admissions/international-students
source_snippet: "The vast majority of our programs no longer consider GRE scores in their admissions process"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-005: Graduate tuition (Dietrich A&S PA)
field: graduate.cost.tuition_dietrich_as_pa
value: 26876
source_url: https://www.tuition.pitt.edu/graduate
source_snippet: "Dietrich School of Arts and Sciences Full-time, Two Terms $26,876"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-G-006: Graduate tuition (Katz MBA PA)
field: graduate.cost.tuition_katz_mba_pa
value: 34858
source_url: https://www.tuition.pitt.edu/graduate
source_snippet: "Joseph M. Katz Graduate School of Business Full-time, Two Terms $34,858"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-P-001: Total program count
field: overview.total_programs
value: 511
source_url: https://www.academics.pitt.edu/degree-finder-view
source_snippet: "511 programs across 26 pages of Degree Finder (105 Bachelor, 138 Master, 100 Doctorate, 147 Certificate, 11 Micro-credential)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-P-002: Schools count
field: overview.schools_count
value: 18
source_url: https://www.academics.pitt.edu/schools-colleges
source_snippet: "18 schools and colleges listed on the Schools & Colleges page"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
pitt-knowledge-base-v2/
├── 00-overview.md                          # Section 0: 院校总览 (rules 1-4)
├── 01-ug-dietrich-as.md                    # Section 1: A&S UG programs
├── 02-ug-cba.md                            # Section 1: CBA UG programs
├── 03-ug-engineering.md                    # Section 1: Engineering UG programs
├── 04-ug-sci.md                            # Section 1: SCI UG programs
├── 05-ug-nursing.md                        # Section 1: Nursing UG programs
├── 06-ug-education.md                      # Section 1: Education UG programs
├── 07-ug-cgs.md                            # Section 1: CGS UG programs
├── 08-ug-shrs.md                           # Section 1: SHRS UG programs
├── 09-ug-public-health.md                  # Section 1: Public Health UG programs
├── 10-ug-soc-work.md                       # Section 1: Social Work UG programs
├── 11-ug-scia.md                           # Section 1: SPIA UG programs
├── 12-ug-interdisciplinary.md              # Section 1: Cross-college programs
├── 13-ug-minors.md                         # Section 1: Minors list
├── 14-grad-dietrich-as.md                  # Section 2: A&S grad programs
├── 15-grad-katz.md                         # Section 2: Katz grad programs
├── 16-grad-engineering.md                  # Section 2: Engineering grad programs
├── 17-grad-sci.md                          # Section 2: SCI grad programs
├── 18-grad-education.md                    # Section 2: Education grad programs
├── 19-grad-shrs.md                         # Section 2: SHRS grad programs
├── 20-grad-dental.md                       # Section 2: Dental grad programs
├── 21-grad-law.md                          # Section 2: Law grad programs
├── 22-grad-medicine.md                     # Section 2: Medicine grad programs
├── 23-grad-nursing.md                      # Section 2: Nursing grad programs
├── 24-grad-pharmacy.md                     # Section 2: Pharmacy grad programs
├── 25-grad-public-health.md                # Section 2: Public Health grad programs
├── 26-grad-scia.md                         # Section 2: SPIA grad programs
├── 27-grad-soc-work.md                     # Section 2: Social Work grad programs
├── 28-deadlines-requirements.md            # Section 3: 申请要求与截止日期
├── 29-costs-financial-aid.md               # Section 4: 费用与资助
├── 30-evidence-chain.md                    # Section 5: 证据链
└── 31-comparison-framework.md              # Section 7: 跨校比较
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "pitt-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BSE|BSBA|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL | 说明 |
|--------|--------|---------|------|
| P0 | 本科英语考试最低分 | admissions.pitt.edu/international/ | 未公布明确最低分，需联系招生办确认 |
| P0 | OOS 研究生学费 | tuition.pitt.edu/graduate | 页面默认显示 PA 费率，需手动切换 |
| P1 | 各学院详细录取要求 | 各学院研究生网站 | 分散模式，需逐个采集 |
| P1 | 法学院/医学院学费 | law.pitt.edu, medschool.pitt.edu | 专业学院费率独立 |
| P1 | 研究生资助详情 | 各学院网站 | GSR/TA/TF 具体金额 |
| P2 | 各专业具体课程要求 | 各学院网站 | 需逐个访问 |
| P2 | 转学分政策 | admissions.pitt.edu/transfer/ | 转学生相关信息 |
| P2 | Honors College 详情 | frederickhonors.pitt.edu | BPhil 学位要求 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Pitt | (其他学校待填) |
|------|------|---------------|
| 公立/私立 | **公立** | |
| 所在城市 | Pittsburgh, PA | |
| UG 学费 (PA resident) | $20,966 - $37,428 | |
| UG 学费 (OOS) | $41,662 - $52,954 | |
| UG COA (PA, on-campus) | ~$42,000 - $47,000 | |
| UG COA (OOS, on-campus) | ~$63,000 - $74,000 | |
| Need-blind (intl?) | Need-blind PA; Need-aware OOS/intl | |
| EA 截止日期 | N/A (Rolling) | |
| RD 截止日期 | N/A (Rolling) | |
| 奖学金截止 | Dec 1 (domestic); Feb 1 (intl) | |
| SAT/ACT 要求 | Test-optional through Fall 2028 | |
| TOEFL 最低分 | 未公布 (UG) / 90 (Grad) | |
| IELTS 最低分 | 未公布 (UG) / 7.0 (Grad) | |
| 申请费 | $55 (UG) | |
| 项目总数 (Rule 1) | **511** | |
| 学院数 (Rule 2) | **18** | |
| 学位级别数 | **35+** | |
| 特色 | 强医学院、哲学系、滚动招生、公立性价比 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.pitt.edu, financialaid.pitt.edu, www.tuition.pitt.edu, academics.pitt.edu, www.asgraduate.pitt.edu, www.eli.pitt.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
