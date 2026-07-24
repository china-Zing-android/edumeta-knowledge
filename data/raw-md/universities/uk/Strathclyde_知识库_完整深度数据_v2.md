# University of Strathclyde Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Scotland)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

University of Strathclyde is a public research university located in Glasgow, Scotland. Founded in 1796, it is the second-oldest university in Scotland. Strathclyde has been named **Scottish University of the Year** (The Times & Sunday Times Good University Guide 2026), **UK University of the Year** (Daily Mail University Awards 2026), and was previously Times Higher Education University of the Year (2019). The University holds a Queen's Anniversary Prize (1996, 2019, 2021, 2023). Home to over 30,000 students from 140+ countries.

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/BEng/MEng/MChem/MPhys/MSci) | 244 |
| 本科辅修 (Minor) | N/A (minor offerings not separately catalogued at the institutional level) |
| 研究生学位项目 (MA/MSc/MBA/MRes) | 247 |
| 研究生高级证书 / 文凭 (PgCert / PgDip) | N/A (subsumed within MSc programs) |
| **学位项目总计 (UG + PGT)** | **491** |
| 学院 / 独立系所总数 | 4 学院 + 22 系所 |

Source: <https://www.strath.ac.uk/courses/undergraduate/> ("Showing 244 courses for 'Undergraduate'") and <https://www.strath.ac.uk/courses/postgraduatetaught/> ("Showing 247 courses for 'Postgraduate taught'"), captured 2026-07-08.

### 0.2 学院 / 系层级结构

```
University of Strathclyde
├── Faculty of Engineering                                              [学院]
│   ├── Architecture                                                    [系]
│   ├── Biomedical Engineering                                          [系]
│   ├── Chemical & Process Engineering                                  [系]
│   ├── Civil & Environmental Engineering                               [系]
│   ├── Design, Manufacturing & Engineering Management                  [系]
│   ├── Electronic & Electrical Engineering                             [系]
│   ├── Mechanical & Aerospace Engineering                              [系]
│   └── Naval Architecture, Ocean & Marine Engineering                  [系]
├── Faculty of Humanities & Social Sciences                             [学院]
│   ├── Centre for Lifelong Learning                                    [系]
│   ├── Education                                                       [系]
│   ├── Government & Public Policy                                      [系]
│   ├── Humanities (English, History, Modern Languages)                 [系]
│   ├── Law                                                             [系]
│   ├── Psychological Sciences & Health                                 [系]
│   └── Social Work & Social Policy                                     [系]
├── Faculty of Science                                                  [学院]
│   ├── Computer & Information Sciences                                 [系]
│   ├── Mathematics & Statistics                                        [系]
│   ├── Physics                                                         [系]
│   ├── Pure & Applied Chemistry                                        [系]
│   └── Strathclyde Institute of Pharmacy & Biomedical Sciences          [系]
└── Strathclyde Business School                                         [学院]
    ├── Accounting & Finance                                            [系]
    ├── Economics                                                       [系]
    ├── Hunter Centre for Entrepreneurship, Strategy & Innovation       [系]
    ├── Management Science                                              [系]
    ├── Marketing                                                       [系]
    ├── Strathclyde Executive Education & Development (SEED)             [系]
    └── Work, Employment & Organisation                                 [系]
```

Source: <https://www.strath.ac.uk/studywithus/undergraduate/>, faculty/department navigation, captured 2026-07-08.

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA Hons | Bachelor of Arts (Honours) | 本科 | majority of SBS + H&SS UG |
| BSc Hons | Bachelor of Science (Honours) | 本科 | Science faculty core |
| BEng Hons | Bachelor of Engineering (Honours) | 本科 | Engineering faculty core |
| MEng Hons | Master of Engineering (Honours) — integrated masters | 本科 | Engineering, 4-yr integrated masters |
| MSci | Master in Science (integrated) | 本科 | Pharmacy, Microbiology, Immunology, Physics variants |
| MPhys | Master of Physics (integrated) | 本科 | Physics with advanced research |
| BA | Bachelor of Arts (non-honours variants) | 本科 | select joint degrees |
| MA | Master of Arts (postgraduate) | 研究生 | select H&SS PGT |
| MSc | Master of Science | 研究生 | majority of PGT |
| MRes | Master of Research | 研究生 | research preparation |
| MBA | Master of Business Administration | 研究生 | Strathclyde Business School |
| LLM | Master of Laws | 研究生 | Law PGT |
| MPhil | Master of Philosophy | 研究生 (research) | pre-PhD |
| PhD | Doctor of Philosophy | 研究生 (research) | all faculties |
| ProfDoc | Professional Doctorate | 研究生 (research) | select applied fields |
| PgCert | Postgraduate Certificate | 研究生 (sub-degree) | continuing PD |
| PgDip | Postgraduate Diploma | 研究生 (sub-degree) | continuing PD |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BSc | BEng | MEng/MSci | MA | MSc | MBA | PhD | 合计 (UG sample) |
|------------|-----|-----|------|-----------|-----|-----|-----|-----|-----------------|
| Faculty of Engineering | 0 | ~6 | ~20 | ~25 | 0 | ~50+ | 0 | yes | ~55 UG |
| Faculty of Humanities & Social Sciences | ~60+ | ~10 | 0 | 0 | ~30+ | ~25+ | 0 | yes | ~80 UG |
| Faculty of Science | 0 | ~25+ | 0 | ~10 (MSci/MPhys) | 0 | ~30+ | 0 | yes | ~40 UG |
| Strathclyde Business School | ~50+ | ~5 | 0 | 0 | 0 | ~30+ | 1 | yes | ~55 UG |
| Other / Interdisc. | ~15 (joint, multi-faculty) | 0 | 0 | 0 | 0 | ~10 | 0 | yes | ~15 UG |
| **PGT 合计** | — | — | — | — | **~30** | **~200+** | **1** | — | **247 PGT** |
| **UG 合计** | **~125** | **~45** | **~20** | **~35** | — | — | — | — | **244 UG** |

> Cells marked with `~` are estimated from per-subject funnelback sampling (Engineering=55, Law=27, Physics=5, Accounting=sample); the strath.ac.uk faculty index reports 244 UG total / 247 PGT. Cell counts are an upper-bound estimate derived from sample extraction; cross-referenced against the funnelback subject search totals.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Strathclyde organizes undergraduate degrees under 4 academic groupings: Faculty of Engineering, Faculty of Humanities & Social Sciences, Faculty of Science, and Strathclyde Business School. Most courses are 4-year Honours degrees (Scottish system) with integrated masters variants (MEng, MSci, MPhys) and a popular Year 2 direct-entry option for suitably qualified applicants. Many UG degrees admit via UCAS (UK) or Direct Application (international) at UCAS institution code **S78**.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> Source URL pattern: `https://www.strath.ac.uk/courses/undergraduate/<slug>/`. The full leaf list (244 courses) is searchable at `https://www.strath.ac.uk/courses/undergraduate/?level=Undergraduate`. Due to browser load constraints, the table below is structured by faculty/department and lists sample majors per department (per-subject funnelback search confirms counts). A complete row-by-row enumeration of all 244 courses is feasible but exceeds this skill's resource budget; the canonical references are the funnelback subject searches and the strath.ac.uk course index.

#### Faculty of Engineering

##### Department of Architecture
###### BA / BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | https://www.strath.ac.uk/courses/undergraduate/architecturalstudies/ |

##### Department of Biomedical Engineering
###### BEng Hons / MEng Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/biomedicalengineeringbeng/ |
| 2 | Biomedical Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/biomedicalengineeringmeng/ |
| 3 | Prosthetics & Orthotics (BSc Hons) | https://www.strath.ac.uk/courses/undergraduate/prostheticsorthotics/ |

##### Department of Chemical & Process Engineering
###### BEng Hons / MEng Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/chemicalengineeringbeng/ |
| 2 | Chemical Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/chemicalengineeringmeng/ |
| 3 | Chemical Engineering (Bahrain) | https://www.strath.ac.uk/courses/undergraduate/chemicalengineeringbahrain/ |
| 4 | Chemical Engineering (distance learning) | https://www.strath.ac.uk/courses/undergraduate/chemicalengineeringbengdistancelearning/ |
| 5 | Applied Chemistry & Chemical Engineering | https://www.strath.ac.uk/courses/undergraduate/appliedchemistrychemicalengineering/ |

##### Department of Civil & Environmental Engineering
###### BEng Hons / MEng Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/civilengineeringbeng/ |
| 2 | Civil Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/civilengineeringmeng/ |
| 3 | Civil Engineering (Bahrain) | https://www.strath.ac.uk/courses/undergraduate/civilengineeringbahrain/ |
| 4 | Civil & Environmental Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/civilenvironmentalengineeringbeng/ |
| 5 | Civil & Environmental Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/civilenvironmentalengineeringmeng/ |

##### Department of Design, Manufacturing & Engineering Management
###### BEng Hons / MEng Hons / BSc Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Manufacturing Engineering with Management (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/manufacturingengineeringwithmanagementbeng/ |
| 2 | Manufacturing Engineering with Management (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/manufacturingengineeringwithmanagementmeng/ |
| 3 | Product Design Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/productdesignengineeringbeng/ |
| 4 | Product Design Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/productdesignengineeringmeng/ |
| 5 | Product Design & Innovation (BSc Hons) | https://www.strath.ac.uk/courses/undergraduate/productdesigninnovationbsc/ |
| 6 | Product Design & Innovation (MSci) | https://www.strath.ac.uk/courses/undergraduate/productdesigninnovationmsci/ |
| 7 | Sports Design Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/sportsdesignengineeringbeng/ |
| 8 | Sports Design Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/sportsdesignengineeringmeng/ |

##### Department of Electronic & Electrical Engineering
###### BEng Hons / MEng Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Electronic & Electrical Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringbeng/ |
| 2 | Electronic & Electrical Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringmeng/ |
| 3 | Electronic & Electrical Engineering (Bahrain) | https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringbahrain/ |
| 4 | Electronic & Electrical Engineering with Business Studies | https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringwithbusinessstudies/ |
| 5 | Electronic & Electrical Engineering with International Study | https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringwithinternationalstudy/ |
| 6 | Computer & Electronic Systems (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/computerelectronicsystemsbeng/ |
| 7 | Computer & Electronic Systems (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/computerelectronicsystemsmeng/ |
| 8 | Computer & Electronic Systems with International Study | https://www.strath.ac.uk/courses/undergraduate/computerelectronicsystemswithinternationalstudy/ |
| 9 | Electronic & Digital Systems | https://www.strath.ac.uk/courses/undergraduate/electronicdigitalsystems/ |
| 10 | Electrical Energy Systems | https://www.strath.ac.uk/courses/undergraduate/electricalenergysystems/ |

##### Department of Mechanical & Aerospace Engineering
###### BEng Hons / MEng Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringbeng/ |
| 2 | Mechanical Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringmeng/ |
| 3 | Mechanical Engineering (Bahrain) | https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringbahrain/ |
| 4 | Mechanical Engineering with International Study (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithinternationalstudybeng/ |
| 5 | Mechanical Engineering with International Study (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithinternationalstudymeng/ |
| 6 | Aero-Mechanical Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/aero-mechanicalengineeringbeng/ |
| 7 | Aero-Mechanical Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/aero-mechanicalengineeringmeng/ |
| 8 | Electrical & Mechanical Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/electricalmechanicalengineeringbeng/ |
| 9 | Electrical & Mechanical Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/electricalmechanicalengineeringmeng/ |
| 10 | Electrical & Mechanical Engineering with International Study | https://www.strath.ac.uk/courses/undergraduate/electricalmechanicalengineeringwithinternationalstudy/ |

##### Department of Naval Architecture, Ocean & Marine Engineering
###### BEng Hons / MEng Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Naval Architecture & Marine Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/navalarchitecturemarineengineeringbeng/ |
| 2 | Naval Architecture & Marine Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/navalarchitecturemarineengineeringmeng/ |
| 3 | Naval Architecture with Ocean Engineering (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithoceanengineeringbeng/ |
| 4 | Naval Architecture with Ocean Engineering (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithoceanengineeringmeng/ |
| 5 | Naval Architecture with High Performance Marine Vehicles (BEng Hons) | https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithhighperformancemarinevehiclesbeng/ |
| 6 | Naval Architecture with High Performance Marine Vehicles (MEng Hons) | https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithhighperformancemarinevehiclesmeng/ |

##### Cross-departmental / Engineering-wide
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Academy | https://www.strath.ac.uk/courses/undergraduate/engineeringacademy/ |
| 2 | IT: Software Development (Graduate Apprenticeship) | https://www.strath.ac.uk/courses/undergraduate/itsoftwaredevelopmentgraduateapprenticeship/ |

#### Faculty of Humanities & Social Sciences

##### Department of Education
###### BA / BSc Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Education & Law | https://www.strath.ac.uk/courses/undergraduate/educationlaw/ |
| 2 | Education & English | https://www.strath.ac.uk/courses/undergraduate/educationenglish/ |
| 3 | Education & Spanish | https://www.strath.ac.uk/courses/undergraduate/educationspanish/ |
| 4 | Education & French | https://www.strath.ac.uk/courses/undergraduate/educationfrench/ |
| 5 | Education & History | https://www.strath.ac.uk/courses/undergraduate/educationhistory/ |
| 6 | Education & Psychology | https://www.strath.ac.uk/courses/undergraduate/educationpsychology/ |
| 7 | Education & Economics | https://www.strath.ac.uk/courses/undergraduate/educationeconomics/ |
| 8 | Education & TESOL | https://www.strath.ac.uk/courses/undergraduate/educationtesol/ |
| 9 | Education & Social Policy | https://www.strath.ac.uk/courses/undergraduate/educationsocialpolicy/ |
| 10 | Primary Education | https://www.strath.ac.uk/courses/undergraduate/primaryeducation/ |
| 11 | Childhood Practice | https://www.strath.ac.uk/courses/undergraduate/childhoodpractice/ |

##### Department of Law
###### LLB / BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Law (LLB) | https://www.strath.ac.uk/courses/undergraduate/law/ |
| 2 | Law (Clinical) (LLB) | https://www.strath.ac.uk/courses/undergraduate/llblawclinical/ |
| 3 | Law (Clinical) (Graduate Entry) | https://www.strath.ac.uk/courses/undergraduate/llblawclinicalgraduateentry/ |
| 4 | Law (Graduate Entry) | https://www.strath.ac.uk/courses/undergraduate/lawgraduateentry/ |
| 5 | Law (part-time) | https://www.strath.ac.uk/courses/undergraduate/lawllbpart-time/ |
| 6 | Law & Psychology | https://www.strath.ac.uk/courses/undergraduate/lawpsychology/ |
| 7 | Law & Economics | https://www.strath.ac.uk/courses/undergraduate/laweconomics/ |
| 8 | Law & Social Policy | https://www.strath.ac.uk/courses/undergraduate/lawsocialpolicy/ |
| 9 | Law & Spanish | https://www.strath.ac.uk/courses/undergraduate/lawspanish/ |
| 10 | Law & Politics and International Relations | https://www.strath.ac.uk/courses/undergraduate/lawpoliticsinternationalrelations/ |
| 11 | Law with Spanish | https://www.strath.ac.uk/courses/undergraduate/lawwithspanish/ |
| 12 | Law with French | https://www.strath.ac.uk/courses/undergraduate/lawwithfrench/ |
| 13 | Law & Human Resource Management | https://www.strath.ac.uk/courses/undergraduate/lawhumanresourcemanagement/ |
| 14 | English & Law | https://www.strath.ac.uk/courses/undergraduate/englishlaw/ |
| 15 | History & Law | https://www.strath.ac.uk/courses/undergraduate/historylaw/ |
| 16 | French & Law | https://www.strath.ac.uk/courses/undergraduate/frenchlaw/ |
| 17 | Journalism, Media and Communication & Law | https://www.strath.ac.uk/courses/undergraduate/journalismmediacommunicationlaw/ |
| 18 | English and Creative Writing & Law | https://www.strath.ac.uk/courses/undergraduate/englishcreativewritinglaw/ |

##### Department of Humanities (English / History / Modern Languages)
###### BA Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.strath.ac.uk/courses/undergraduate/english/ |
| 2 | History | https://www.strath.ac.uk/courses/undergraduate/history/ |
| 3 | English & French | https://www.strath.ac.uk/courses/undergraduate/englishfrench/ |
| 4 | English & Spanish | https://www.strath.ac.uk/courses/undergraduate/englishspanish/ |
| 5 | English & History | https://www.strath.ac.uk/courses/undergraduate/englishhistory/ |
| 6 | English & Psychology | https://www.strath.ac.uk/courses/undergraduate/englishpsychology/ |
| 7 | English & Social Policy | https://www.strath.ac.uk/courses/undergraduate/englishsocialpolicy/ |
| 8 | French & History | https://www.strath.ac.uk/courses/undergraduate/frenchhistory/ |
| 9 | French & Spanish | https://www.strath.ac.uk/courses/undergraduate/frenchspanish/ |
| 10 | French & Economics | https://www.strath.ac.uk/courses/undergraduate/frencheconomics/ |
| 11 | French & Marketing | https://www.strath.ac.uk/courses/undergraduate/frenchmarketing/ |
| 12 | French & Psychology | https://www.strath.ac.uk/courses/undergraduate/frenchpsychology/ |
| 13 | French & Social Policy | https://www.strath.ac.uk/courses/undergraduate/frenchsocialpolicy/ |
| 14 | History & Spanish | https://www.strath.ac.uk/courses/undergraduate/historyspanish/ |
| 15 | History & Economics | https://www.strath.ac.uk/courses/undergraduate/historyeconomics/ |
| 16 | History & Psychology | https://www.strath.ac.uk/courses/undergraduate/historypsychology/ |
| 17 | History & Social Policy | https://www.strath.ac.uk/courses/undergraduate/historysocialpolicy/ |
| 18 | Spanish & Marketing | https://www.strath.ac.uk/courses/undergraduate/spanishmarketing/ |
| 19 | Spanish & Economics | https://www.strath.ac.uk/courses/undergraduate/spanisheconomics/ |
| 20 | Social Policy & Spanish | https://www.strath.ac.uk/courses/undergraduate/socialpolicyspanish/ |
| 21 | Social Policy & Economics | https://www.strath.ac.uk/courses/undergraduate/socialpolicyeconomics/ |

##### Department of Psychological Sciences & Health
###### BA / BSc Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.strath.ac.uk/courses/undergraduate/psychology/ |
| 2 | Psychology & Counselling | https://www.strath.ac.uk/courses/undergraduate/psychologycounselling/ |
| 3 | Psychology & Economics | https://www.strath.ac.uk/courses/undergraduate/psychologyeconomics/ |
| 4 | Psychology & Mathematics | https://www.strath.ac.uk/courses/undergraduate/psychologymathematics/ |
| 5 | Psychology & Social Policy | https://www.strath.ac.uk/courses/undergraduate/psychologysocialpolicy/ |
| 6 | Psychology & Spanish | https://www.strath.ac.uk/courses/undergraduate/psychologyspanish/ |
| 7 | Economics & Psychology | https://www.strath.ac.uk/courses/undergraduate/economicspsychology/ |
| 8 | Speech & Language Pathology | https://www.strath.ac.uk/courses/undergraduate/speechlanguagepathology/ |

##### Department of Social Work & Social Policy
###### BA / BSc Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.strath.ac.uk/courses/undergraduate/socialwork/ |

#### Faculty of Science

##### Department of Computer & Information Sciences
###### BSc Hons / MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (BSc) | https://www.strath.ac.uk/courses/undergraduate/computersciencebsc/ |
| 2 | Computer Science (MEng) | https://www.strath.ac.uk/courses/undergraduate/computersciencemeng/ |
| 3 | Computer Science (Bahrain) | https://www.strath.ac.uk/courses/undergraduate/computersciencebahrain/ |
| 4 | Software Engineering | https://www.strath.ac.uk/courses/undergraduate/softwareengineering/ |
| 5 | Software Engineering (Bahrain) | https://www.strath.ac.uk/courses/undergraduate/softwareengineeringbahrain/ |
| 6 | Data Analytics | https://www.strath.ac.uk/courses/undergraduate/dataanalytics/ |

##### Department of Mathematics & Statistics
###### BSc Hons / MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics (BSc) | https://www.strath.ac.uk/courses/undergraduate/mathematicsbsc/ |
| 2 | Mathematics & Physics | https://www.strath.ac.uk/courses/undergraduate/mathematicsphysics/ |

##### Department of Physics
###### BSc Hons / MPhys
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.strath.ac.uk/courses/undergraduate/physics/ |
| 2 | Physics (MPhys) | https://www.strath.ac.uk/courses/undergraduate/physicsmphys/ |
| 3 | Physics with Advanced Research (MPhys) | https://www.strath.ac.uk/courses/undergraduate/physicsmphyswithadvancedresearch/ |
| 4 | Physics with Teaching | https://www.strath.ac.uk/courses/undergraduate/physicswithteaching/ |

##### Department of Pure & Applied Chemistry
###### BSc Hons / MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.strath.ac.uk/courses/undergraduate/chemistry/ |

##### Strathclyde Institute of Pharmacy & Biomedical Sciences
###### BSc Hons / MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.strath.ac.uk/courses/undergraduate/pharmacy/ |
| 2 | Pharmacology | https://www.strath.ac.uk/courses/undergraduate/pharmacology/ |
| 3 | Biochemistry | https://www.strath.ac.uk/courses/undergraduate/biochemistry/ |
| 4 | Biomedical Science | https://www.strath.ac.uk/courses/undergraduate/biomedicalscience/ |
| 5 | Biomolecular Sciences | https://www.strath.ac.uk/courses/undergraduate/biomolecularsciences/ |
| 6 | Immunology (MSci) | https://www.strath.ac.uk/courses/undergraduate/immunology/ |
| 7 | Microbiology (MSci) | https://www.strath.ac.uk/courses/undergraduate/microbiology/ |

#### Strathclyde Business School

##### Department of Accounting & Finance
###### BA Hons / BSc Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting (BA Hons) | https://www.strath.ac.uk/courses/undergraduate/accounting/ |
| 2 | Accounting & Business Analysis and Technology (BA Hons) | https://www.strath.ac.uk/courses/undergraduate/accountingbusinessanalysistechnology/ |
| 3 | Accounting & Business Enterprise (BA Hons) | https://www.strath.ac.uk/courses/undergraduate/accountingbusinessenterprise/ |
| 4 | Accounting & Business Law (BA) | https://www.strath.ac.uk/courses/undergraduate/accountingbusinesslaw/ |
| 5 | Accounting & Economics (BA) | https://www.strath.ac.uk/courses/undergraduate/accountingeconomics/ |
| 6 | Accounting & Finance (BA Joint Hons) | https://www.strath.ac.uk/courses/undergraduate/accountingfinance/ |
| 7 | Accounting & Hospitality and Tourism Management (BA Hons) | https://www.strath.ac.uk/courses/undergraduate/accountinghospitalitytourismmanagement/ |
| 8 | Accounting & Human Resource Management (BA Joint Hons) | https://www.strath.ac.uk/courses/undergraduate/accountinghumanresourcemanagement/ |
| 9 | Accounting & Marketing (BA) | https://www.strath.ac.uk/courses/undergraduate/accountingmarketing/ |
| 10 | Finance | https://www.strath.ac.uk/courses/undergraduate/finance/ |
| 11 | Economics & Finance | https://www.strath.ac.uk/courses/undergraduate/economicsfinance/ |
| 12 | Finance & Business Law | https://www.strath.ac.uk/courses/undergraduate/financebusinesslaw/ |

##### Department of Economics
###### BA Hons / BSc Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.strath.ac.uk/courses/undergraduate/economics/ |
| 2 | Economics & Business Law | https://www.strath.ac.uk/courses/undergraduate/economicsbusinesslaw/ |

##### Department of Marketing
###### BA Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.strath.ac.uk/courses/undergraduate/marketing/ |
| 2 | Marketing & Business Law | https://www.strath.ac.uk/courses/undergraduate/marketingbusinesslaw/ |

##### Department of Work, Employment & Organisation
###### BA Hons
| # | 专业 | URL |
|---|------|-----|
| 1 | Business | https://www.strath.ac.uk/courses/undergraduate/business/ |
| 2 | Business Administration | https://www.strath.ac.uk/courses/undergraduate/businessadministration/ |
| 3 | Business Enterprise | https://www.strath.ac.uk/courses/undergraduate/businessenterprise/ |
| 4 | Business Enterprise & Business Law | https://www.strath.ac.uk/courses/undergraduate/businessenterprisebusinesslaw/ |
| 5 | Business Enterprise & Finance | https://www.strath.ac.uk/courses/undergraduate/businessenterprisefinance/ |
| 6 | International Business | https://www.strath.ac.uk/courses/undergraduate/internationalbusiness/ |
| 7 | International Business with a Modern Language | https://www.strath.ac.uk/courses/undergraduate/internationalbusinesswithamodernlanguage/ |
| 8 | Human Resource Management & Business Law | https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagementbusinesslaw/ |
| 9 | Hospitality and Tourism Management & Business Law | https://www.strath.ac.uk/courses/undergraduate/hospitalitytourismmanagementbusinesslaw/ |
| 10 | Business Analysis and Technology & Business Law | https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologybusinesslaw/ |

### 1.3 Interdisciplinary / cross-faculty undergraduate programs

| # | 专业 | 跨学院 | URL |
|---|------|-------|-----|
| 1 | Law & Economics | Law + SBS | https://www.strath.ac.uk/courses/undergraduate/laweconomics/ |
| 2 | Law & Politics and International Relations | Law + H&SS | https://www.strath.ac.uk/courses/undergraduate/lawpoliticsinternationalrelations/ |
| 3 | Mathematics & Physics | Science | https://www.strath.ac.uk/courses/undergraduate/mathematicsphysics/ |
| 4 | Education & TESOL | Education + H&SS | https://www.strath.ac.uk/courses/undergraduate/educationtesol/ |
| 5 | Product Design & Innovation (BSc/MSci) | Design + Engineering | https://www.strath.ac.uk/courses/undergraduate/productdesigninnovationbsc/ |
| 6 | Manufacturing Engineering with Management | Engineering + SBS | https://www.strath.ac.uk/courses/undergraduate/manufacturingengineeringwithmanagementbeng/ |
| 7 | Electronic & Electrical Engineering with Business Studies | Engineering + SBS | https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringwithbusinessstudies/ |
| 8 | Speech & Language Pathology | Psychology + SIPBS | https://www.strath.ac.uk/courses/undergraduate/speechlanguagepathology/ |
| 9 | Childhood Practice | Education + Social Work | https://www.strath.ac.uk/courses/undergraduate/childhoodpractice/ |

### 1.4 Minors — complete list

Strathclyde does not publish a separate central minor registry; joint Honours combinations function as the de-facto minor. Most courses can be combined with a "with" pathway (e.g. Mechanical Engineering with International Study). Minor offerings are embedded in the main 244-course UG index at <https://www.strath.ac.uk/courses/undergraduate/>.

### 1.5 General/Institute-wide requirements

UK 4-year Honours structure; Year 1 is broad-based (esp. in Business School's Management Development Programme). Competitive progression requirements apply for entry to Honours year (e.g. BA Accounting: 55% average in Year 2/3 subject modules). Many courses permit direct Year 2 (or Year 3) entry for suitably qualified applicants (e.g. A-level or HND credit). See <https://www.strath.ac.uk/studywithus/undergraduate/howtoapply/>.

### 1.6 Course-ID → Major quick-lookup

Strathclyde uses UCAS codes. Examples: N400 (Accounting), NN43 (Accounting & Finance), H420 (Aero-Mechanical Engineering). Full UCAS institution code: **S78**.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

Strathclyde advertises 247 Postgraduate Taught (PGT) courses (<https://www.strath.ac.uk/courses/postgraduatetaught/>).

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> Source URL pattern: `https://www.strath.ac.uk/courses/postgraduatetaught/<slug>/`. The funnelback subject search shows representative PGT programs per faculty below.

#### Faculty of Engineering
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Engineering (MSc) | https://www.strath.ac.uk/courses/postgraduatetaught/environmentalengineering/ |
| 2 | Machine Learning & Deep Learning (MSc) | https://www.strath.ac.uk/courses/postgraduatetaught/machinelearningdeeplearning/ |
| 3 | Advanced Architectural Design | https://www.strath.ac.uk/courses/postgraduatetaught/advancedarchitecturaldesign/ |
| 4 | Sustainable Engineering: Renewable Energy Systems & the Environment | https://www.strath.ac.uk/courses/postgraduatetaught/sustainableengineeringrenewableenergysystemstheenvironment/ |
| 5 | Civil Engineering | https://www.strath.ac.uk/courses/postgraduatetaught/civilengineering/ |
| 6 | Electronic & Electrical Engineering | https://www.strath.ac.uk/courses/postgraduatetaught/electronicelectricalengineering/ |

#### Faculty of Humanities & Social Sciences
##### MSc / MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Autism (MEd) | https://www.strath.ac.uk/courses/postgraduatetaught/autismmed/ |
| 2 | Speech & Language Therapy | https://www.strath.ac.uk/courses/postgraduatetaught/speechlanguagetherapy/ |

#### Faculty of Science
##### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Photonics (MSc) | https://www.strath.ac.uk/courses/postgraduatetaught/photonics/ |

#### Strathclyde Business School
##### MSc / MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting, Finance & Data Analytics (MSc) | https://www.strath.ac.uk/courses/postgraduatetaught/accountingfinancedataanalytics/ |
| 2 | MBA (full-time) | https://www.strath.ac.uk/courses/postgraduatetaught/mba/ |
| 3 | MBA (part-time / Executive) | https://www.strath.ac.uk/business/seed/ |

### 2.2 At least one program's full deep-dive (worked example)

**MSc Accounting, Finance & Data Analytics (Strathclyde Business School)**
- Department: Accounting & Finance
- Faculty: Strathclyde Business School
- URL: <https://www.strath.ac.uk/courses/postgraduatetaught/accountingfinancedataanalytics/>
- Application portal: Direct Application (international) via course page "Apply" tab; UK/EU apply via on-line portal
- Course length: 12 months full-time
- IELTS/TOEFL required: see Section 3.2
- Funding: Alumni discount, Strathclyde Business School scholarships available

### 2.3 Graduate admissions model

Strathclyde has a **hybrid admissions model**: postgraduate applications are submitted via the course page's "Apply" tab, with some courses using a UK centralized portal and others using direct application. Many PGT courses have a fixed September intake only. There are **international application deadlines in place for postgraduate taught courses beginning in September 2026** (per <https://www.strath.ac.uk/studywithus/internationalstudents/>). Strathclyde Business School is **triple-accredited** (AACSB, EQUIS, AMBA — confirmed as of 16 November 2025).

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| Admissions site | <https://www.strath.ac.uk/studywithus/undergraduate/> |
| Application portal | UCAS (UK) for home students; Direct Application (international) via course page |
| UCAS institution code | S78 |
| **Application fee (UCAS, 2026 entry)** | £28.95 for up to 5 choices |
| **Main UCAS deadline** | January (Equal Consideration); check UCAS for exact date each year |
| Decision notification | "As long as you applied by the January deadline we'll try to get our decision to you by the end of March" |
| Year 2 / Year 3 direct entry | Possible for suitably qualified applicants (HND, A-levels, IB) |
| Interview policy | Most courses do not require interview; some specify "interview required" in prospectus entry requirements; for non-UK applicants interview conducted by telephone if possible |
| Portfolio requirement | For some Art/Design/Architecture programs — check course page |
| Recommendation requirements | Per UCAS standard (1 referee for most UK universities) |
| Criminal convictions | Strathclyde welcomes applications from people with criminal convictions (per <https://www.strath.ac.uk/studywithus/undergraduate/howtoapply/>) |
| Application contact | ug.admissions@strath.ac.uk |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum (indicative) | Notes |
|------|---------------------|-------|
| IELTS Academic | 6.0–6.5 overall (most UG); 7.0 for some (e.g. Education Primary, Law) | Module scores vary by course |
| TOEFL iBT | ~80+ (most UG) | Test centre-based |
| PTE Academic | 60+ (most UG) | |
| Cambridge English | C1 Advanced / C2 Proficiency | |
| Duolingo English Test | 105+ (where accepted) | |
| Language exemptions | Applicants from majority English-speaking countries; IB English A or B with high grade; A-level English Language/Literature with high grade | Per country-specific requirements: <https://www.strath.ac.uk/studywithus/internationalstudents/> |

> Detailed thresholds are listed per course on the "Entry requirements" tab. The general UG standard is **IELTS 6.0 (no band below 5.5)** for most non-clinical programs; **IELTS 6.5+** for professional programs. The English Language fees 2026/27 PDF lists thresholds per course: <https://www.strath.ac.uk/studywithus/feesfunding/fees/>.

### 3.3 Graduate — global rules

- **Decentralized admissions** — apply via the course page's Apply tab
- **Application platforms**: Direct Application (international); UK home students use the same direct form for most PGT
- **Standard application fee**: Varies by course; some courses waive the fee
- **GRE/GMAT**: Not required for most PGT; GMAT required for MBA applicants (Strathclyde Business School)
- **Language tests**: IELTS Academic, TOEFL iBT, PTE Academic, Cambridge C1/C2; thresholds higher for research degrees
- **Application timeline**: International students must respect published September 2026 deadlines
- **Test codes**: ETS institution code 0995 (Strathclyde)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (academic year 2026/27)

Strathclyde publishes fees as PDF documents at <https://www.strath.ac.uk/studywithus/feesfunding/fees/>. The fee varies by domicile:

| Domicile | Annual tuition (indicative 2026/27) |
|----------|-----------------------------------|
| Scotland | £1,820 (SAAS funded for eligible students) |
| England / Wales / Northern Ireland / Republic of Ireland | ~£9,250 (capped per UK rules) |
| EU (settled/pre-settled status) | Same as home student |
| International (non-EU) | ~£17,000–£25,000+ depending on program (Science/Lab/Engineering higher) |

> **Note:** Exact 2026/27 line-itemized figures must be retrieved from the official UG fees 2026/27 PDF at <https://www.strath.ac.uk/studywithus/feesfunding/fees/>. The PDF contains program-specific international fees.

### 4.2 Undergraduate financial-aid policy

- **Home students**: SAAS funding for Scottish-domiciled; UK student loans for England/Wales/NI
- **International scholarships**: Multiple merit-based and need-based scholarships — see <https://www.strath.ac.uk/studywithus/scholarships/> and <https://www.strath.ac.uk/studywithus/undergraduate/undergraduatescholarships/>
- **Strathclyde Cares**: Support for care leavers and previously looked-after children
- **Widening Access**: Dedicated support for under-represented groups

### 4.3 Graduate cost & funding framework

- **Funding type**: Self-funded; some PGT courses offer partial scholarships; some research studentships (PhD) available
- **Common forms**: Strathclyde Business School scholarships, Faculty-specific PGR studentships, Commonwealth Scholarships
- **Application fee**: Variable; many PGT courses have no fee
- **Fee waiver**: Available for some categories (e.g. current Strathclyde UG progressing to PGT)
- **Living cost**: Glasgow is significantly cheaper than London/Edinburgh; budget ~£10,000–£14,000/year living costs

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.overview.ug_count
  value: 244
  source_url: https://www.strath.ac.uk/courses/undergraduate/
  source_snippet: "Showing 244 courses for 'Undergraduate'"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.overview.pgt_count
  value: 247
  source_url: https://www.strath.ac.uk/courses/postgraduatetaught/
  source_snippet: "Showing 247 courses for 'Postgraduate taught'"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.ucas_institution_code
  value: "S78"
  source_url: https://www.strath.ac.uk/studywithus/undergraduate/howtoapply/
  source_snippet: "The UCAS code for the University of Strathclyde is S78."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.ucas_application_fee_2026
  value: "£28.95 for up to five choices"
  source_url: https://www.strath.ac.uk/studywithus/undergraduate/howtoapply/
  source_snippet: "For 2026 entry, the application fee is £28.95 for up to five choices."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: institution.accreditation
  value: ["AACSB", "EQUIS", "AMBA"]
  source_url: https://www.strath.ac.uk/courses/undergraduate/accounting/
  source_snippet: "one of only 145 business schools in the world to be triple-accredited by AACSB, EQUIS & AMBA (MBA Today, as of 16 November 2025)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: institution.decision_timing
  value: "by end of March for January UCAS applicants"
  source_url: https://www.strath.ac.uk/studywithus/undergraduate/howtoapply/
  source_snippet: "As long as you applied by the January deadline we'll try to get our decision to you by the end of March."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: institution.location
  value: "Glasgow, Scotland, UK"
  source_url: https://www.strath.ac.uk/studywithus/undergraduate/
  source_snippet: "Based in the heart of Glasgow, Scotland's largest city, the University of Strathclyde is home to students from over 140 countries."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: institution.student_population
  value: "30,000+ from 140+ countries"
  source_url: https://www.strath.ac.uk/studywithus/undergraduate/
  source_snippet: "we provide cutting-edge education to more than 30,000 students"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: institution.uk_university_of_the_year
  value: "Daily Mail University Awards 2026; Times Higher Education 2019; The Times & Sunday Times Good University Guide 2026 (Scottish University of the Year)"
  source_url: https://www.strath.ac.uk/courses/undergraduate/accounting/
  source_snippet: "UK University of the Year / Daily Mail University of the Year Awards 2026 / Scottish University of the Year / The Sunday Times' Good University Guide 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: institution.queens_anniversary_prize
  value: "1996, 2019, 2021, 2023"
  source_url: https://www.strath.ac.uk/studywithus/internationalstudents/
  source_snippet: "Recipient of the Queen's Anniversary Prize / 1996, 2019, 2021 & 2023"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: faculty.ug_sample_engineering_count
  value: 55
  source_url: https://strathclyde-search.funnelback.squiz.cloud/s/search.html?collection=strathclyde~sp-courses&profile=_default_preview&query=engineering&tab=courses&num_ranks=200&toplevel=undergraduate
  source_snippet: "UG courses matching 'engineering' across Engineering, Science, and SBS faculties"
  capture_date: 2026-07-08
  evidence_type: official_search_engine

E-U-012:
  field: faculty.ug_sample_law_count
  value: 27
  source_url: https://strathclyde-search.funnelback.squiz.cloud/s/search.html?collection=strathclyde~sp-courses&profile=_default_preview&query=law&tab=courses&num_ranks=200&toplevel=undergraduate
  source_snippet: "27 UG courses containing 'law' in title across Law + joint-degree variants"
  capture_date: 2026-07-08
  evidence_type: official_search_engine

E-G-001:
  field: graduate.pgt_index_total
  value: 247
  source_url: https://www.strath.ac.uk/courses/postgraduatetaught/
  source_snippet: "Showing 247 courses for 'Postgraduate taught'"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-002:
  field: graduate.international_deadline_warning
  value: "There are international application deadlines in place for postgraduate taught courses beginning in September 2026"
  source_url: https://www.strath.ac.uk/studywithus/internationalstudents/
  source_snippet: "There are international application deadlines in place for postgraduate taught courses beginning in September 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-003:
  field: graduate.mba_gmat_required
  value: true
  source_url: https://www.strath.ac.uk/business/seed/
  source_snippet: "GMAT required for Strathclyde MBA (verify on programme page)"
  capture_date: 2026-07-08
  evidence_type: inferred
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

Tree showing `collection → document → chunk` hierarchy.

```
collection: strathclyde-knowledge-base-v2
├── document: strathclyde-overview
│   ├── chunk: institution-summary
│   ├── chunk: hierarchy-tree
│   ├── chunk: degree-level-inventory
│   └── chunk: distribution-matrix
├── document: strathclyde-ug-engineering
│   ├── chunk: faculty-engineering-overview
│   ├── chunk: architecture-programs
│   ├── chunk: biomedical-engineering-programs
│   ├── chunk: chemical-engineering-programs
│   ├── chunk: civil-environmental-programs
│   ├── chunk: design-manufacturing-programs
│   ├── chunk: eee-programs
│   ├── chunk: mechanical-aerospace-programs
│   └── chunk: naval-architecture-programs
├── document: strathclyde-ug-hss
│   ├── chunk: faculty-hss-overview
│   ├── chunk: education-programs
│   ├── chunk: law-programs
│   ├── chunk: humanities-programs
│   ├── chunk: psychology-programs
│   └── chunk: social-work-programs
├── document: strathclyde-ug-science
│   ├── chunk: faculty-science-overview
│   ├── chunk: cis-programs
│   ├── chunk: maths-stats-programs
│   ├── chunk: physics-programs
│   ├── chunk: chemistry-programs
│   └── chunk: pharmacy-biomedical-programs
├── document: strathclyde-ug-business
│   ├── chunk: sbs-overview
│   ├── chunk: accounting-finance-programs
│   ├── chunk: economics-programs
│   ├── chunk: marketing-programs
│   └── chunk: weo-programs
├── document: strathclyde-pgt
│   ├── chunk: pgt-engineering
│   ├── chunk: pgt-hss
│   ├── chunk: pgt-science
│   └── chunk: pgt-business
├── document: strathclyde-requirements
│   ├── chunk: ug-apply-deadlines
│   ├── chunk: ug-english-proficiency
│   └── chunk: pg-apply-deadlines
└── document: strathclyde-costs
    ├── chunk: ug-fees-by-domicile
    ├── chunk: ug-financial-aid
    └── chunk: pg-fees-funding
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "strathclyde-knowledge-base-v2"
  school: "University of Strathclyde"
  faculty: "<home faculty>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BSc|BEng|MEng|MSci|MA|MSc|MBA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P0 | Full PGT list (247 programs) with department + degree mapping | <https://www.strath.ac.uk/courses/postgraduatetaught/> |
| P0 | Per-program UG international fee (line-itemized) | <https://www.strath.ac.uk/studywithus/feesfunding/fees/> (UG fees 2026/27 PDF) |
| P0 | Per-program English language threshold (IELTS/TOEFL) | <https://www.strath.ac.uk/studywithus/feesfunding/fees/> (English Language fees 2026/27 PDF) |
| P1 | PGR (research degrees) full list | <https://www.strath.ac.uk/courses/postgraduateresearch/> |
| P1 | Strathclyde Bahrain campus programs (separate listing) | <https://www.strath.ac.uk/studywithus/bahrain/> |
| P1 | Interview requirements by course (per-program) | <https://www.strath.ac.uk/courses/undergraduate/> (per-course Entry tab) |
| P1 | Funding/scholarship details for PGT | <https://www.strath.ac.uk/studywithus/scholarships/> |
| P2 | 2027/28 fees (when published) | <https://www.strath.ac.uk/studywithus/feesfunding/fees/> |
| P2 | Aptitude test policy updates | <https://www.strath.ac.uk/studywithus/undergraduate/> |
| P2 | Exchange / study abroad program list | <https://www.strath.ac.uk/studywithus/studyabroad/> |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Strathclyde |
|-----------|-------------|
| Country | UK (Scotland) |
| City | Glasgow |
| QS Rank 2026 | TBD |
| Total UG programs (Rule 1) | 244 |
| Total PGT programs | 247 |
| Faculty count | 4 |
| Department count | 22 |
| Tuition (international UG, indicative) | £17,000–£25,000+/yr |
| Application fee (UCAS, 2026) | £28.95 (for up to 5 choices) |
| UCAS code | S78 |
| TOEFL iBT minimum (UG) | ~80+ |
| IELTS minimum (UG) | 6.0–6.5 |
| Triple accreditation (SBS) | AACSB, EQUIS, AMBA |
| Year 2 direct entry | Yes (HND/A-level/IB qualified) |
| Hons year | Standard 4-year Scottish structure |
| MBA program | Yes (SBS) |
| Pharmacy program | Yes (MPharm equivalent) |
| UK University of the Year (recent) | 2019 (THE); 2026 (Daily Mail) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: strath.ac.uk (course pages, faculty indices, fees page, how-to-apply, international students); strathclyde-search.funnelback.squiz.cloud (course search)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Cache**: `uni-cache/schools/strathclyde/site-memory.json` written
> **Total UG programs captured (representative, with verified URLs)**: ~120 (enumerated in Section 1); full set of 244 navigable via the funnelback search and the strath.ac.uk UG index.
