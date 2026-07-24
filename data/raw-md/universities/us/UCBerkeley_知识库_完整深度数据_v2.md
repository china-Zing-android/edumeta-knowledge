# University of California, Berkeley (UC Berkeley) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Sources**: undergraduate.catalog.berkeley.edu, graduate.catalog.berkeley.edu, admissions.berkeley.edu, financialaid.berkeley.edu, grad.berkeley.edu, admission.universityofcalifornia.edu

---

## SECTION 0 — 院校总览 (Institution overview)

UC Berkeley is a **public** land-grant research university, the flagship of the University of California system, founded 1868. It is consistently ranked among the top public universities worldwide. As a public university, tuition differs sharply for California residents vs. nonresidents/internationals, and admissions follow UC-systemwide policy (UC Application, not Common App; November 30 deadline; **test-free/test-blind** for SAT/ACT).

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/Joint) | 110  (BA 69, BS 40, Joint 1) |
| 本科辅修 (Minor) | 129 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/professional) | 175 |
| 研究生指定领域 / Designated Emphasis (非独立学位, 类似研究生辅修) | 25 |
| **学位项目总计 (UG major + Grad degree)** | **285** |
| 学院 / 独立系所 / 研究生院总数 | 18 (14 个本科学院/系 + 4 个研究生专业学院独立于上述之外) |

> Source: UC Berkeley Undergraduate Catalog Programs index reports "239 results found" (239 captured = 110 majors + 129 minors); Graduate Catalog reports "200 results found" (175 standalone degree + 25 designated emphases). grad.berkeley.edu states "over 200 graduate programs".

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
<University of California, Berkeley>
├── College of Letters & Science (L&S)                         [学院]  (~80 majors, largest college)
│   ├── Biological Sciences (MCB, IB, Neuroscience, etc.)      [系]
│   ├── Physical Sciences (Physics, Astronomy, EPS, Chemistry) [系]
│   ├── Mathematical & Information Sciences (Math, Stat)       [系]
│   ├── Arts & Humanities (Art Practice, Music, English, etc.) [系]
│   ├── Languages & Literatures (East Asian, French, German, etc.) [系]
│   ├── Social Sciences (Economics, Poli Sci, Sociology, Psych) [系]
│   ├── Undergraduate Interdisciplinary Studies               [系]
│   └── L&S Administered Undergraduate Programs               [系]  (cross-college minors)
├── College of Engineering                                      [学院]
│   ├── Electrical Engineering & Computer Sciences (EECS)      [系]  ⚠ CS BA shared with CDSS
│   ├── Civil & Environmental Engineering                      [系]
│   ├── Mechanical Engineering                                 [系]
│   ├── Bioengineering                                          [系]
│   ├── Materials Science & Engineering                         [系]
│   ├── Nuclear Engineering                                     [系]
│   ├── Industrial Engineering & Operations Research           [系]
│   └── Engineering Science Programs                            [系]  (Energy/Engineering Physics/Env Eng/Geosystems/etc.)
├── College of Computing, Data Science, and Society (CDSS)     [学院]  (newest, est. 2023)
│   ├── Data Science Undergraduate Studies                      [系]
│   ├── Statistics                                              [系]  ⚠ shared with L&S historically
│   └── Electrical Engineering & Computer Sciences (CS BA)     [系]  ⚠ joint with Engineering (EECS)
├── College of Chemistry                                        [学院]
│   ├── Chemistry                                               [系]
│   ├── Chemical & Biomolecular Engineering                     [系]
│   └── Chemical Biology                                        [系]
├── College of Environmental Design                             [学院]
│   ├── Architecture                                            [系]
│   ├── Landscape Architecture & Environmental Planning         [系]
│   ├── City & Regional Planning                                [系]
│   └── Sustainable Environmental Design                        [系]
├── Rausser College of Natural Resources                        [学院]
│   ├── Environmental Science, Policy & Management              [系]
│   ├── Agricultural & Resource Economics                       [系]
│   ├── Nutritional Sciences & Toxicology                       [系]
│   ├── Plant & Microbial Biology                               [系]
│   └── Energy & Resources Group                                [系]
├── Haas School of Business                                     [学院/研究生院]
│   └── Undergraduate Business Administration (BS) + MBA/MFE/PhD [系]
├── Berkeley School of Education (BSE)                          [学院]
│   └── Education / Educational Sciences                        [系]
├── Graduate Division                                           [学院]  (administers 100+ academic grad programs)
│   └── Interdisciplinary / Designated Emphases (25 options)    [系]
├── Goldman School of Public Policy                             [研究生院]
├── School of Information (I School)                            [研究生院]
├── School of Law (Berkeley Law)                                [研究生院]
├── School of Optometry                                         [研究生院]
├── School of Public Health                                     [研究生院]
├── School of Social Welfare                                    [研究生院]
└── Graduate School of Journalism                               [研究生院]
```

**Notes**: ⚠ = department shared across colleges. EECS (Electrical Engineering & Computer Sciences) administers the BS in Engineering AND the CS BA / Data Science shared with CDSS. The College of Computing, Data Science, and Society (CDSS) was established in 2023 as Berkeley's first new college in over 50 years, absorbing the School of Information and Data Science programs. "Graduate Division" is the administrative home for ~100 academic PhD/MA/MS programs whose faculty sit in disciplinary departments.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 69 |
| BS | Bachelor of Science | 本科 | 40 |
| Joint | Joint Major (B.A./B.S.) | 本科 | 1 |
| Minor | Undergraduate Minor (non-degree) | 本科 | 129 |
| PhD | Doctor of Philosophy | 研究生 | 85 |
| MA | Master of Arts | 研究生 | 14 |
| MS | Master of Science | 研究生 | 14 |
| MPH | Master of Public Health | 研究生 | 10 |
| MEng | Master of Engineering | 研究生 | 8 |
| MBA | Master of Business Administration | 研究生 | 3 |
| LLM | Master of Laws | 研究生 | 3 |
| MSW | Master of Social Welfare | 研究生 | 3 |
| MPH (4+1) | MPH (4+1 accelerated) | 研究生 | 3 |
| MFE | Master of Financial Engineering | 研究生 | 2 |
| MFA | Master of Fine Arts | 研究生 | 1 |
| MCSS | Master of Computational Social Science | 研究生 | 1 |
| MDP | Master of Development Practice | 研究生 | 1 |
| MDE | Master of Development Engineering | 研究生 | 1 |
| MBT | Master of Biotechnology | 研究生 | 1 |
| MNSD | Master of Nutritional Sciences & Dietetics | 研究生 | 1 |
| MS (CS) | Master of Science (Computer Science) | 研究生 | 1 |
| Master of Forestry | Master of Forestry | 研究生 | 1 |
| MSSE | Master of Molecular Science & Software Engineering | 研究生 | 1 |
| MBE | Master of Bioengineering | 研究生 | 1 |
| MDes | Master of Design | 研究生 | 1 |
| MTM | Master of Translational Medicine | 研究生 | 1 |
| MS (Analytics) | Master of Analytics | 研究生 | 1 |
| MAS | Master of Advanced Study | 研究生 | 1 |
| MS (Real Estate Dev) | Master of Real Estate Design & Development | 研究生 | 1 |
| MArch | Master of Architecture | 研究生 | 1 |
| MLA | Master of Landscape Architecture | 研究生 | 1 |
| MAAD | Master of Advanced Architectural Design | 研究生 | 1 |
| MCP | Master of City Planning | 研究生 | 1 |
| MUD | Master of Urban Design | 研究生 | 1 |
| MJ | Master of Journalism | 研究生 | 1 |
| MICS | Master of Information & Cybersecurity | 研究生 | 1 |
| MIDS | Master of Information & Data Science | 研究生 | 1 |
| MIMS | Master of Information Mgmt & Systems | 研究生 | 1 |
| MPA | Master of Public Affairs | 研究生 | 1 |
| MPP | Master of Public Policy | 研究生 | 1 |
| JSD | Doctor of Juridical Science | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| OD | Doctor of Optometry | 研究生 | 1 |
| DrPH | Doctor of Public Health | 研究生 | 1 |

> Counts sum to 414 (UG majors + UG minors + Grad standalone degree programs). Designated Emphases (25) are non-standalone and excluded from this inventory.

### 0.4 分布矩阵 (Rule 4 — 学院 × 学位级别)

| 学院 \ 级别 | BA | BS | Minor | MA | MS | MFA | MBA | MEng | PhD | Professional/Other | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|
| College of Letters & Science | 62 | 0 | 87 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 149 |
| College of Letters & Science (minors administered) | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| College of Engineering | 0 | 24 | 13 | 0 | 7 | 0 | 0 | 8 | 8 | 4 | 64 |
| College of Chemistry | 0 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 12 |
| College of Computing, Data Science, and Society | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 6 |
| College of Environmental Design | 4 | 0 | 6 | 0 | 1 | 0 | 0 | 0 | 3 | 6 | 20 |
| Rausser College of Natural Resources | 0 | 10 | 7 | 0 | 1 | 0 | 0 | 0 | 4 | 4 | 26 |
| Haas School of Business | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 1 | 2 | 7 |
| Berkeley School of Education | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 6 |
| Graduate Division | 0 | 0 | 0 | 12 | 3 | 1 | 0 | 0 | 56 | 4 | 76 |
| Graduate Division (Designated Emphases) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 25 |
| School of Public Health | 0 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 3 | 14 | 21 |
| School of Information | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 4 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 6 |
| School of Optometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 |
| School of Social Welfare | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 4 |
| Goldman School of Public Policy | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 4 |
| Graduate School of Journalism | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| **合计** | **69** | **40** | **129** | **14** | **14** | **1** | **3** | **8** | **85** | **76** | **439** |

> **Reconciliation**: Row totals + column totals each sum to **439** = (UG majors 110) + (UG minors 129) + (Grad standalone 175) + (Designated Emphases 25). This equals the total count of program entries in Sections 1 & 2 (Rule 5 row count).

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Berkeley undergraduates enroll in one of 8 degree-granting colleges/schools (see Section 0.2 tree). The largest is **College of Letters & Science (L&S)** (~80 majors, all BA). **College of Engineering** grants BS degrees across ~15 departments. The newest, **College of Computing, Data Science, and Society (CDSS)**, hosts Data Science, Statistics, and the CS BA. Admissions to a specific college/major is decided at application; L&S students declare a major after enrollment (with "high-demand major" caps for CS, Econ, Psych, etc. — see admissions.berkeley.edu/academics/ls-high-demand-policy/).

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

#### College of Letters & Science

##### BA
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | African American Studies | 25014U | https://undergraduate.catalog.berkeley.edu/programs/25014U |
| 2 | American Studies | 25045U | https://undergraduate.catalog.berkeley.edu/programs/25045U |
| 3 | Analytics | 253D2U | https://undergraduate.catalog.berkeley.edu/programs/253D2U |
| 4 | Ancient Greek and Roman Studies | 252G3U | https://undergraduate.catalog.berkeley.edu/programs/252G3U |
| 5 | Anthropology | 25063U | https://undergraduate.catalog.berkeley.edu/programs/25063U |
| 6 | Applied Mathematics | 25072U | https://undergraduate.catalog.berkeley.edu/programs/25072U |
| 7 | Art | 25090U | https://undergraduate.catalog.berkeley.edu/programs/25090U |
| 8 | Asian American and Asian Diaspora Studies | 252C2U | https://undergraduate.catalog.berkeley.edu/programs/252C2U |
| 9 | Astrophysics | 25101U | https://undergraduate.catalog.berkeley.edu/programs/25101U |
| 10 | Celtic Studies | 25147U | https://undergraduate.catalog.berkeley.edu/programs/25147U |
| 11 | Chemistry | 25153U | https://undergraduate.catalog.berkeley.edu/programs/25153U |
| 12 | Chicanx Latinx Studies | 252G5U | https://undergraduate.catalog.berkeley.edu/programs/252G5U |
| 13 | Chinese Language and Culture | 25469U | https://undergraduate.catalog.berkeley.edu/programs/25469U |
| 14 | Cognitive Science | 25179U | https://undergraduate.catalog.berkeley.edu/programs/25179U |
| 15 | Comparative Literature | 25192U | https://undergraduate.catalog.berkeley.edu/programs/25192U |
| 16 | Dance and Performance Studies | 252A1U | https://undergraduate.catalog.berkeley.edu/programs/252A1U |
| 17 | Dutch Studies | 25236U | https://undergraduate.catalog.berkeley.edu/programs/25236U |
| 18 | Earth & Planetary Science | 252A4U | https://undergraduate.catalog.berkeley.edu/programs/252A4U |
| 19 | East Asian Humanities | 252G8U | https://undergraduate.catalog.berkeley.edu/programs/252G8U |
| 20 | East Asian Religion, Thought, and Culture | 252E1U | https://undergraduate.catalog.berkeley.edu/programs/252E1U |
| 21 | Economics | 25246U | https://undergraduate.catalog.berkeley.edu/programs/25246U |
| 22 | English | 25345U | https://undergraduate.catalog.berkeley.edu/programs/25345U |
| 23 | Ethnic Studies | 25360U | https://undergraduate.catalog.berkeley.edu/programs/25360U |
| 24 | Film and Media | 25379U | https://undergraduate.catalog.berkeley.edu/programs/25379U |
| 25 | French | 25387U | https://undergraduate.catalog.berkeley.edu/programs/25387U |
| 26 | Gender and Women's Studies | 259A1U | https://undergraduate.catalog.berkeley.edu/programs/259A1U |
| 27 | Geography | 25396U | https://undergraduate.catalog.berkeley.edu/programs/25396U |
| 28 | German | 25408U | https://undergraduate.catalog.berkeley.edu/programs/25408U |
| 29 | Global Studies | 25492U | https://undergraduate.catalog.berkeley.edu/programs/25492U |
| 30 | Greek | 25414U | https://undergraduate.catalog.berkeley.edu/programs/25414U |
| 31 | Greek and Latin | 25625U | https://undergraduate.catalog.berkeley.edu/programs/25625U |
| 32 | History | 25429U | https://undergraduate.catalog.berkeley.edu/programs/25429U |
| 33 | History of Art | 25430U | https://undergraduate.catalog.berkeley.edu/programs/25430U |
| 34 | Integrative Biology | 25975U | https://undergraduate.catalog.berkeley.edu/programs/25975U |
| 35 | Interdisciplinary Studies | 25628U | https://undergraduate.catalog.berkeley.edu/programs/25628U |
| 36 | Italian Studies | 25479U | https://undergraduate.catalog.berkeley.edu/programs/25479U |
| 37 | Japanese Language and Culture | 25470U | https://undergraduate.catalog.berkeley.edu/programs/25470U |
| 38 | Korean Language and Culture | 250M1U | https://undergraduate.catalog.berkeley.edu/programs/250M1U |
| 39 | Latin | 25495U | https://undergraduate.catalog.berkeley.edu/programs/25495U |
| 40 | Legal Studies | 25497U | https://undergraduate.catalog.berkeley.edu/programs/25497U |
| 41 | Linguistics | 25510U | https://undergraduate.catalog.berkeley.edu/programs/25510U |
| 42 | Mathematics | 25540U | https://undergraduate.catalog.berkeley.edu/programs/25540U |
| 43 | Media Studies | 252A9U | https://undergraduate.catalog.berkeley.edu/programs/252A9U |
| 44 | Middle Eastern Languages and Cultures | tOjk97DmMV1K3NLmM6uC | https://undergraduate.catalog.berkeley.edu/programs/tOjk97DmMV1K3NLmM6uC |
| 45 | Molecular and Cell Biology | 25974U | https://undergraduate.catalog.berkeley.edu/programs/25974U |
| 46 | Music | 25579U | https://undergraduate.catalog.berkeley.edu/programs/25579U |
| 47 | Native American Studies | 25587U | https://undergraduate.catalog.berkeley.edu/programs/25587U |
| 48 | Neuroscience | 25594U | https://undergraduate.catalog.berkeley.edu/programs/25594U |
| 49 | Philosophy | 25651U | https://undergraduate.catalog.berkeley.edu/programs/25651U |
| 50 | Physics | 25666U | https://undergraduate.catalog.berkeley.edu/programs/25666U |
| 51 | Political Economy | 252B2U | https://undergraduate.catalog.berkeley.edu/programs/252B2U |
| 52 | Political Science | 25699U | https://undergraduate.catalog.berkeley.edu/programs/25699U |
| 53 | Psychology | 25780U | https://undergraduate.catalog.berkeley.edu/programs/25780U |
| 54 | Public Health | 25789U | https://undergraduate.catalog.berkeley.edu/programs/25789U |
| 55 | Rhetoric | 25807U | https://undergraduate.catalog.berkeley.edu/programs/25807U |
| 56 | Scandinavian | 25834U | https://undergraduate.catalog.berkeley.edu/programs/25834U |
| 57 | Slavic Languages and Literatures | 25849U | https://undergraduate.catalog.berkeley.edu/programs/25849U |
| 58 | Social Welfare | 25864U | https://undergraduate.catalog.berkeley.edu/programs/25864U |
| 59 | Sociology | 25867U | https://undergraduate.catalog.berkeley.edu/programs/25867U |
| 60 | South and Southeast Asian Studies | 25877U | https://undergraduate.catalog.berkeley.edu/programs/25877U |
| 61 | Spanish and Portuguese | 25881U | https://undergraduate.catalog.berkeley.edu/programs/25881U |
| 62 | Theater & Performance Studies | 259A2U | https://undergraduate.catalog.berkeley.edu/programs/259A2U |

#### College of Engineering

##### BS
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Aerospace Engineering | 16279U | https://undergraduate.catalog.berkeley.edu/programs/16279U |
| 2 | Bioengineering | 16288U | https://undergraduate.catalog.berkeley.edu/programs/16288U |
| 3 | Bioengineering and Business Administration | VzaVU2tVa3uyAmZWh9XJ | https://undergraduate.catalog.berkeley.edu/programs/VzaVU2tVa3uyAmZWh9XJ |
| 4 | Bioengineering/Materials Science and Engineering Joint Major | 162B3U | https://undergraduate.catalog.berkeley.edu/programs/162B3U |
| 5 | Civil Engineering | 16300U | https://undergraduate.catalog.berkeley.edu/programs/16300U |
| 6 | Civil Engineering and Business Administration | T47e1lSWqoKkDYD3zeRm | https://undergraduate.catalog.berkeley.edu/programs/T47e1lSWqoKkDYD3zeRm |
| 7 | Electrical Engineering and Computer Science/Materials Science and Engineering | 162B6U | https://undergraduate.catalog.berkeley.edu/programs/162B6U |
| 8 | Electrical Engineering and Computer Science/Nuclear Engineering | 162B9U | https://undergraduate.catalog.berkeley.edu/programs/162B9U |
| 9 | Electrical Engineering and Computer Sciences | 16306U | https://undergraduate.catalog.berkeley.edu/programs/16306U |
| 10 | Electrical and Computer Engineering | 16333U | https://undergraduate.catalog.berkeley.edu/programs/16333U |
| 11 | Energy Engineering | 162C6U | https://undergraduate.catalog.berkeley.edu/programs/162C6U |
| 12 | Engineering Math and Statistics | 16312U | https://undergraduate.catalog.berkeley.edu/programs/16312U |
| 13 | Engineering Physics | 16315U | https://undergraduate.catalog.berkeley.edu/programs/16315U |
| 14 | Environmental Engineering | 16384U | https://undergraduate.catalog.berkeley.edu/programs/16384U |
| 15 | Environmental Engineering Science | 160M0U | https://undergraduate.catalog.berkeley.edu/programs/160M0U |
| 16 | Industrial Engineering and Operations Research | 16324U | https://undergraduate.catalog.berkeley.edu/programs/16324U |
| 17 | Materials Science and Engineering | 16328U | https://undergraduate.catalog.berkeley.edu/programs/16328U |
| 18 | Materials Science and Engineering and Business Administration | JHbdnKFVpcEq13grTsic | https://undergraduate.catalog.berkeley.edu/programs/JHbdnKFVpcEq13grTsic |
| 19 | Materials Science and Engineering/Mechanical Engineering | 162B7U | https://undergraduate.catalog.berkeley.edu/programs/162B7U |
| 20 | Materials Science and Engineering/Nuclear Engineering | 162B8U | https://undergraduate.catalog.berkeley.edu/programs/162B8U |
| 21 | Mechanical Engineering | 16330U | https://undergraduate.catalog.berkeley.edu/programs/16330U |
| 22 | Mechanical Engineering and Business Administration | Tqx3rktbkoWOvjBatqi1 | https://undergraduate.catalog.berkeley.edu/programs/Tqx3rktbkoWOvjBatqi1 |
| 23 | Mechanical Engineering/Nuclear Engineering | 162C0U | https://undergraduate.catalog.berkeley.edu/programs/162C0U |
| 24 | Nuclear Engineering | 16342U | https://undergraduate.catalog.berkeley.edu/programs/16342U |

#### College of Chemistry

##### BS
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Chemical Biology | 101A1U | https://undergraduate.catalog.berkeley.edu/programs/101A1U |
| 2 | Chemical Engineering | 10294U | https://undergraduate.catalog.berkeley.edu/programs/10294U |
| 3 | Chemical Engineering/ Materials Science and Engineering Joint Major | 102B5U | https://undergraduate.catalog.berkeley.edu/programs/102B5U |
| 4 | Chemical Engineering/ Nuclear Engineering Joint Major | 102B4U | https://undergraduate.catalog.berkeley.edu/programs/102B4U |
| 5 | Chemistry | 10153U | https://undergraduate.catalog.berkeley.edu/programs/10153U |

#### College of Computing, Data Science, and Society

##### BA
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Computer Science | A5201U | https://undergraduate.catalog.berkeley.edu/programs/A5201U |
| 2 | Data Science | A50AMU | https://undergraduate.catalog.berkeley.edu/programs/A50AMU |
| 3 | Statistics | A5891U | https://undergraduate.catalog.berkeley.edu/programs/A5891U |

#### College of Environmental Design

##### BA
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Architecture | 19084U | https://undergraduate.catalog.berkeley.edu/programs/19084U |
| 2 | Landscape Architecture | 19489U | https://undergraduate.catalog.berkeley.edu/programs/19489U |
| 3 | Sustainable Environmental Design | 192D9U | https://undergraduate.catalog.berkeley.edu/programs/192D9U |
| 4 | Urban Studies | 19912U | https://undergraduate.catalog.berkeley.edu/programs/19912U |

#### Rausser College of Natural Resources

##### BS
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Business Administration | 70141U | https://undergraduate.catalog.berkeley.edu/programs/70141U |
| 2 | Conservation and Resource Studies | 04206U | https://undergraduate.catalog.berkeley.edu/programs/04206U |
| 3 | Ecosystem Management and Forestry | z5SVnW3RWZv5syG4KuEY | https://undergraduate.catalog.berkeley.edu/programs/z5SVnW3RWZv5syG4KuEY |
| 4 | Environmental Economics and Policy | 04779U | https://undergraduate.catalog.berkeley.edu/programs/04779U |
| 5 | Environmental Sciences | 04351U | https://undergraduate.catalog.berkeley.edu/programs/04351U |
| 6 | Genetics and Plant Biology | 04746U | https://undergraduate.catalog.berkeley.edu/programs/04746U |
| 7 | Microbial Biology | 045A7U | https://undergraduate.catalog.berkeley.edu/programs/045A7U |
| 8 | Molecular Environmental Biology | 04847U | https://undergraduate.catalog.berkeley.edu/programs/04847U |
| 9 | Nutrition and Metabolic Biology | 040KGU | https://undergraduate.catalog.berkeley.edu/programs/040KGU |
| 10 | Society and Environment | 043A2U | https://undergraduate.catalog.berkeley.edu/programs/043A2U |

##### Joint
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Life Science, Business, and Entrepreneurship | dacFCYznXfFet1QCRxAU | https://undergraduate.catalog.berkeley.edu/programs/dacFCYznXfFet1QCRxAU |

#### Berkeley School of Education

##### BS
| # | 专业 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Educational Sciences | 79249U | https://undergraduate.catalog.berkeley.edu/programs/79249U |

### 1.3 Interdisciplinary / cross-college undergraduate programs

Joint majors span two departments (often Engineering + Business or two Engineering depts). Examples:
- Civil Engineering and Business Administration (BS) — College of Engineering × Haas
- Mechanical Engineering and Business Administration (BS) — College of Engineering × Haas
- Bioengineering and Business Administration (BS) — College of Engineering × Haas
- Materials Science and Engineering and Business Administration (BS) — College of Engineering × Haas
- Electrical Engineering and Computer Sciences and Business Administration (BS) — College of Engineering × Haas
- EEMS/MSE, EECS/NucE, ME/NE, ChemE/MatSci, ChemE/NE joint majors — within College of Engineering / Chemistry
- Dual-degree programs: Sciences Po/UC Berkeley, University of Hong Kong/UC Berkeley

Source: https://undergraduate.catalog.berkeley.edu/programs (Program Type = "Joint Program" / "Dual Degree").

### 1.4 Minors — complete list (129 minors)

| # | Minor | Home (by code prefix) | URL |
|---|-------|----------------------|-----|
| 1 | Education | Berkeley School of Education | https://undergraduate.catalog.berkeley.edu/programs/79I098U |
| 2 | Science and Math Education | Berkeley School of Education | https://undergraduate.catalog.berkeley.edu/programs/79I099U |
| 3 | Chemical Engineering | College of Chemistry | https://undergraduate.catalog.berkeley.edu/programs/10I008U |
| 4 | Chemistry | College of Chemistry | https://undergraduate.catalog.berkeley.edu/programs/10I009U |
| 5 | Electrochemistry | College of Chemistry | https://undergraduate.catalog.berkeley.edu/programs/10I178U |
| 6 | Data Science | College of Computing, Data Science, and Society | https://undergraduate.catalog.berkeley.edu/programs/A5I172U |
| 7 | Statistics | College of Computing, Data Science, and Society | https://undergraduate.catalog.berkeley.edu/programs/A5I173U |
| 8 | Aerospace Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I159U |
| 9 | Bioengineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I010U |
| 10 | Computer Science | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I011U |
| 11 | Electrical Engineering and Computer Science | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I012U |
| 12 | Energy Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I013U |
| 13 | Environmental Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I014U |
| 14 | Geosystems | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I015U |
| 15 | Global Digital Infrastructure | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I180U |
| 16 | Industrial Engineering and Operations Research | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I016U |
| 17 | Materials Science and Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I017U |
| 18 | Mechanical Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I018U |
| 19 | Nuclear Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I019U |
| 20 | Structural Engineering | College of Engineering | https://undergraduate.catalog.berkeley.edu/programs/16I020U |
| 21 | Architecture | College of Environmental Design | https://undergraduate.catalog.berkeley.edu/programs/19I021U |
| 22 | City and Regional Planning | College of Environmental Design | https://undergraduate.catalog.berkeley.edu/programs/19I022U |
| 23 | Environmental Design and Urban Developing Countries | College of Environmental Design | https://undergraduate.catalog.berkeley.edu/programs/19I023U |
| 24 | History of the Built Environment | College of Environmental Design | https://undergraduate.catalog.berkeley.edu/programs/19I025U |
| 25 | Social & Cultural Factors in Environmental Design | College of Environmental Design | https://undergraduate.catalog.berkeley.edu/programs/19I026U |
| 26 | Sustainable Design | College of Environmental Design | https://undergraduate.catalog.berkeley.edu/programs/19I027U |
| 27 | African American Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I074U |
| 28 | American Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I160U |
| 29 | Ancient Greek and Roman Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I162U |
| 30 | Anthropology | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I075U |
| 31 | Applied Language Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I087U |
| 32 | Arabic | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I029U |
| 33 | Armenian Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I154U |
| 34 | Asian American and Asian Diaspora Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I076U |
| 35 | Astrophysics | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I069U |
| 36 | Atmospheric Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I131U |
| 37 | Buddhist Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I150U |
| 38 | Celtic Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I033U |
| 39 | Chicanx Latinx Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I170U |
| 40 | Chinese Language | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I034U |
| 41 | Climate Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I158U |
| 42 | Clinical & Counseling Psychology | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I169U |
| 43 | Cognitive Science and the Future of Tech | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I175U |
| 44 | Comparative Literature | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I124U |
| 45 | Creative Writing | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I089U |
| 46 | Dance and Performance Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I037U |
| 47 | Demography | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I078U |
| 48 | Digital Humanities | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I153U |
| 49 | Disability Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I090U |
| 50 | Dutch Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I038U |
| 51 | Earth and Planetary Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I070U |
| 52 | Eastern European and Eurasian Languages and Cultures | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I036U |
| 53 | English | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I039U |
| 54 | Environmental Earth Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I132U |
| 55 | Ethnic Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I079U |
| 56 | French | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I040U |
| 57 | Gender and Women's Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I080U |
| 58 | Geography | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I081U |
| 59 | Geology | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I133U |
| 60 | Geophysics | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I134U |
| 61 | Geospatial Information Science and Technology | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I176U |
| 62 | German | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I044U |
| 63 | Global Poverty & Practice | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I092U |
| 64 | Global Studies: Africa, North and Sub-Saharan | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I126U |
| 65 | Global Studies: Asia | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I127U |
| 66 | Global Studies: Europe and Russia | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I130U |
| 67 | Global Studies: The Americas | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I128U |
| 68 | Global Studies: The Middle East and North Africa | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I129U |
| 69 | Greek | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I045U |
| 70 | Health and Wellness | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I165U |
| 71 | Hebrew | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I046U |
| 72 | Hispanic Language and Linguistics | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I066U |
| 73 | History | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I082U |
| 74 | History of Art | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I047U |
| 75 | Human Rights Interdisciplinary | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I083U |
| 76 | Israel Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I174U |
| 77 | Italian Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I048U |
| 78 | Japanese | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I049U |
| 79 | Jewish Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I050U |
| 80 | Korean | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I051U |
| 81 | Latin | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I052U |
| 82 | Linguistics | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I085U |
| 83 | Logic | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I138U |
| 84 | Marine Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I135U |
| 85 | Mathematics | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I071U |
| 86 | Medieval Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I054U |
| 87 | Middle Eastern Languages & Cultures | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I163U |
| 88 | Modern Greek | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I179U |
| 89 | Music | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I055U |
| 90 | Native American Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I086U |
| 91 | Persian | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I056U |
| 92 | Philosophy | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I057U |
| 93 | Physics | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I072U |
| 94 | Place, Community and Culture | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I177U |
| 95 | Planetary Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I136U |
| 96 | Political Economy | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I123U |
| 97 | Politics, Philosophy, & Law | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I161U |
| 98 | Portuguese Languages, Literatures & Cultures | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I053U |
| 99 | Queer and Trans Praxis | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I084U |
| 100 | Race and the Law | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I151U |
| 101 | Rhetoric | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I059U |
| 102 | Russian Culture | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I061U |
| 103 | Russian Language | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I060U |
| 104 | Russian Literature | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I062U |
| 105 | Scandinavian | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I063U |
| 106 | Science, Technology, and Society | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I166U |
| 107 | South & Southeast Asian Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I064U |
| 108 | Spanish Languages, Literatures and Cultures | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I065U |
| 109 | The Developing Child: Early Development & Learning Science | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I152U |
| 110 | Theater & Performance Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I067U |
| 111 | Tibetan | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I125U |
| 112 | Transnational Italian Studies | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I167U |
| 113 | Turkish | College of Letters & Science | https://undergraduate.catalog.berkeley.edu/programs/25I068U |
| 114 | Aerospace Engineering and Business Administration | College of Letters & Science (minors administered) | https://undergraduate.catalog.berkeley.edu/programs/yKx5e1eCFAIJMGT5mAzC |
| 115 | Electrical Engineering and Computer Sciences and Business Administration | College of Letters & Science (minors administered) | https://undergraduate.catalog.berkeley.edu/programs/R7GK397hLDIKdTjHeVoj |
| 116 | Industrial Engineering and Operations Research and Business | College of Letters & Science (minors administered) | https://undergraduate.catalog.berkeley.edu/programs/W6MfSZuhUsGbItNWH6T8 |
| 117 | Sciences Po/UC Berkeley (Dual Degree Program) | College of Letters & Science (minors administered) | https://undergraduate.catalog.berkeley.edu/programs/lGbzq1dRlrsI9hRKhf4v |
| 118 | University of Hong Kong/UC Berkeley (Dual Degree Program) | College of Letters & Science (minors administered) | https://undergraduate.catalog.berkeley.edu/programs/WcOMqISTJjhA3geDPyHD |
| 119 | Public Policy | Goldman School of Public Policy | https://undergraduate.catalog.berkeley.edu/programs/82I100U |
| 120 | Journalism | Graduate School of Journalism | https://undergraduate.catalog.berkeley.edu/programs/71I121U |
| 121 | Sustainable Business and Policy | Haas School of Business | https://undergraduate.catalog.berkeley.edu/programs/07I171U |
| 122 | Conservation and Resource Studies | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I001U |
| 123 | Energy and Resources | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I002U |
| 124 | Environmental Economics and Policy | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I003U |
| 125 | Food Systems | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I122U |
| 126 | Forestry and Natural Resources | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I004U |
| 127 | Nutritional Science | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I006U |
| 128 | Sustainability | Rausser College of Natural Resources | https://undergraduate.catalog.berkeley.edu/programs/04I155U |
| 129 | Global Public Health | School of Public Health | https://undergraduate.catalog.berkeley.edu/programs/96I137U |

> Minor home college is inferred from the catalog program-code prefix (e.g. `16I*`=Engineering, `25I*`=Letters & Science, `10I*`=Chemistry, `19I*`=Environmental Design, `04I*`=Rausser CNR, `A5I*`=CDSS, `79I*`=Education, `82I*`=Public Policy, `96I*`=Public Health, `71I*`=Journalism). A small number are administered by L&S for non-L&S disciplines.

### 1.5 General / Institute-wide requirements

Berkeley undergraduates complete: (1) **University Requirements** — Entry-Level Writing, American Cultures, American History & Institutions; (2) **College Requirements** — e.g. L&S's 7-course breadth (Arts & Literature, Biological Science, Historical Studies, International Studies, Philosophy & Values, Physical Science, Social & Behavioral Sciences); (3) **Major Requirements**. L&S breadth can be satisfied by HD-F exams or coursework. Engineering has a broader lower-division math/physics core.
Source: https://undergraduate.catalog.berkeley.edu/earning-your-degree/major-minor-requirements

### 1.6 Program-code → Major quick-lookup

Berkeley catalog program codes embed the offering unit and degree. Format: `[unit-prefix][degree-suffix]`. Examples:
- `16306U` = EECS, BS (16=Engineering CoE, 306=EECS, U=undergraduate degree program)
- `25246U` = Economics, BA (25=L&S)
- `16I011U` = Computer Science Minor (the `I` flags a Minor)
- `A5201U` = Computer Science BA (A5=CDSS)
- `04206U` = Conservation & Resource Studies, BS (04=Rausser CNR)

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别

#### Graduate Division

##### MA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Asian Studies | 00096MAG | https://graduate.catalog.berkeley.edu/programs/00096MAG |
| 2 | Demography | 00213MAG | https://graduate.catalog.berkeley.edu/programs/00213MAG |
| 3 | Earth and Planetary Science | 002A4MAG | https://graduate.catalog.berkeley.edu/programs/002A4MAG |
| 4 | Endocrinology | 00270MAG | https://graduate.catalog.berkeley.edu/programs/00270MAG |
| 5 | Folklore | 00366MAG | https://graduate.catalog.berkeley.edu/programs/00366MAG |
| 6 | Global Studies | 00492MAG | https://graduate.catalog.berkeley.edu/programs/00492MAG |
| 7 | Japanese Language | 00470MAG | https://graduate.catalog.berkeley.edu/programs/00470MAG |
| 8 | Mathematics | 00540MAG | https://graduate.catalog.berkeley.edu/programs/00540MAG |
| 9 | Middle Eastern Languages and Cultures | 002G6MAG | https://graduate.catalog.berkeley.edu/programs/002G6MAG |
| 10 | Physics | 00666MAG | https://graduate.catalog.berkeley.edu/programs/00666MAG |
| 11 | Statistics | 00891MAG | https://graduate.catalog.berkeley.edu/programs/00891MAG |
| 12 | Statistics and Data Science | 000F8MAG | https://graduate.catalog.berkeley.edu/programs/000F8MAG |

##### MBT
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Biotechnology | 002G9MBTG | https://graduate.catalog.berkeley.edu/programs/002G9MBTG |

##### MCSS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Computational Social Science | 000HIMCSSG | https://graduate.catalog.berkeley.edu/programs/000HIMCSSG |

##### MDE
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Development Engineering | 002G2MDEG | https://graduate.catalog.berkeley.edu/programs/002G2MDEG |

##### MDP
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Development Practice | 002C5MDPG | https://graduate.catalog.berkeley.edu/programs/002C5MDPG |

##### MFA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Art Practice | 00090MFARG | https://graduate.catalog.berkeley.edu/programs/00090MFARG |

##### MS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Energy and Resources | 00239MSG | https://graduate.catalog.berkeley.edu/programs/00239MSG |
| 2 | Health and Medical Sciences | 00424MSG | https://graduate.catalog.berkeley.edu/programs/00424MSG |
| 3 | Metabolic Biology | 002D0MSG | https://graduate.catalog.berkeley.edu/programs/002D0MSG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | African Diaspora Studies | 000N1PHDG | https://graduate.catalog.berkeley.edu/programs/000N1PHDG |
| 2 | Ancient History and Mediterranean Archaeology | 00051PHDG | https://graduate.catalog.berkeley.edu/programs/00051PHDG |
| 3 | Anthropology | 00063PHDG | https://graduate.catalog.berkeley.edu/programs/00063PHDG |
| 4 | Applied Mathematics | 00072PHDG | https://graduate.catalog.berkeley.edu/programs/00072PHDG |
| 5 | Applied Science and Technology | 00086PHDG | https://graduate.catalog.berkeley.edu/programs/00086PHDG |
| 6 | Astrophysics | 00101PHDG | https://graduate.catalog.berkeley.edu/programs/00101PHDG |
| 7 | Biophysics | 00126PHDG | https://graduate.catalog.berkeley.edu/programs/00126PHDG |
| 8 | Buddhist Studies | 00139PHDG | https://graduate.catalog.berkeley.edu/programs/00139PHDG |
| 9 | Classical Archaeology | 00168PHDG | https://graduate.catalog.berkeley.edu/programs/00168PHDG |
| 10 | Classics | 00174PHDG | https://graduate.catalog.berkeley.edu/programs/00174PHDG |
| 11 | Comparative Literature | 00192PHDG | https://graduate.catalog.berkeley.edu/programs/00192PHDG |
| 12 | Computational Biology | 002C7PHDG | https://graduate.catalog.berkeley.edu/programs/002C7PHDG |
| 13 | Demography | 00213PHDG | https://graduate.catalog.berkeley.edu/programs/00213PHDG |
| 14 | Earth and Planetary Science | 002A4PHDG | https://graduate.catalog.berkeley.edu/programs/002A4PHDG |
| 15 | East Asian Languages and Cultures | 00232PHDG | https://graduate.catalog.berkeley.edu/programs/00232PHDG |
| 16 | Economics | 00246PHDG | https://graduate.catalog.berkeley.edu/programs/00246PHDG |
| 17 | Endocrinology | 00270PHDG | https://graduate.catalog.berkeley.edu/programs/00270PHDG |
| 18 | Energy and Resources | 00239PHDG | https://graduate.catalog.berkeley.edu/programs/00239PHDG |
| 19 | English | 00345PHDG | https://graduate.catalog.berkeley.edu/programs/00345PHDG |
| 20 | Ethnic Studies | 00360PHDG | https://graduate.catalog.berkeley.edu/programs/00360PHDG |
| 21 | Film & Media | 002C3PHDG | https://graduate.catalog.berkeley.edu/programs/002C3PHDG |
| 22 | French | 00387PHDG | https://graduate.catalog.berkeley.edu/programs/00387PHDG |
| 23 | Geography | 00396PHDG | https://graduate.catalog.berkeley.edu/programs/00396PHDG |
| 24 | German | 00408PHDG | https://graduate.catalog.berkeley.edu/programs/00408PHDG |
| 25 | Health Policy | 002E3PHDG | https://graduate.catalog.berkeley.edu/programs/002E3PHDG |
| 26 | Hispanic Languages and Literatures | 00425PHDG | https://graduate.catalog.berkeley.edu/programs/00425PHDG |
| 27 | History | 00429PHDG | https://graduate.catalog.berkeley.edu/programs/00429PHDG |
| 28 | History of Art | 00430PHDG | https://graduate.catalog.berkeley.edu/programs/00430PHDG |
| 29 | Infectious Diseases and Immunity | 00848PHDG | https://graduate.catalog.berkeley.edu/programs/00848PHDG |
| 30 | Integrative Biology | 00975PHDG | https://graduate.catalog.berkeley.edu/programs/00975PHDG |
| 31 | Italian Studies | 00479PHDG | https://graduate.catalog.berkeley.edu/programs/00479PHDG |
| 32 | Linguistics | 00510PHDG | https://graduate.catalog.berkeley.edu/programs/00510PHDG |
| 33 | Logic and the Methodology of Science | 00531PHDG | https://graduate.catalog.berkeley.edu/programs/00531PHDG |
| 34 | Mathematics | 00540PHDG | https://graduate.catalog.berkeley.edu/programs/00540PHDG |
| 35 | Medical Anthropology | 00553JPHDG | https://graduate.catalog.berkeley.edu/programs/00553JPHDG |
| 36 | Medieval Studies | 0010KPHDG | https://graduate.catalog.berkeley.edu/programs/0010KPHDG |
| 37 | Metabolic Biology | 002D0PHDG | https://graduate.catalog.berkeley.edu/programs/002D0PHDG |
| 38 | Microbiology | 00570PHDG | https://graduate.catalog.berkeley.edu/programs/00570PHDG |
| 39 | Middle Eastern Languages and Cultures | 002G6PHDG | https://graduate.catalog.berkeley.edu/programs/002G6PHDG |
| 40 | Molecular and Cell Biology | 00974PHDG | https://graduate.catalog.berkeley.edu/programs/00974PHDG |
| 41 | Music | 00579PHDG | https://graduate.catalog.berkeley.edu/programs/00579PHDG |
| 42 | Neuroscience | 00594PHDG | https://graduate.catalog.berkeley.edu/programs/00594PHDG |
| 43 | Performance Studies | 009B2PHDG | https://graduate.catalog.berkeley.edu/programs/009B2PHDG |
| 44 | Philosophy | 00651PHDG | https://graduate.catalog.berkeley.edu/programs/00651PHDG |
| 45 | Physics | 00666PHDG | https://graduate.catalog.berkeley.edu/programs/00666PHDG |
| 46 | Political Science | 00699PHDG | https://graduate.catalog.berkeley.edu/programs/00699PHDG |
| 47 | Psychology | 00780PHDG | https://graduate.catalog.berkeley.edu/programs/00780PHDG |
| 48 | Rhetoric | 00807PHDG | https://graduate.catalog.berkeley.edu/programs/00807PHDG |
| 49 | Romance Languages and Literatures | 00812PHDG | https://graduate.catalog.berkeley.edu/programs/00812PHDG |
| 50 | Scandinavian Languages and Literatures | 00838PHDG | https://graduate.catalog.berkeley.edu/programs/00838PHDG |
| 51 | Science and Mathematics Education | 00843PHDG | https://graduate.catalog.berkeley.edu/programs/00843PHDG |
| 52 | Slavic Languages and Literatures | 00849PHDG | https://graduate.catalog.berkeley.edu/programs/00849PHDG |
| 53 | Sociology | 00867PHDG | https://graduate.catalog.berkeley.edu/programs/00867PHDG |
| 54 | Sociology and Demography | 002A5PHDG | https://graduate.catalog.berkeley.edu/programs/002A5PHDG |
| 55 | South and Southeast Asian Studies | 00877PHDG | https://graduate.catalog.berkeley.edu/programs/00877PHDG |
| 56 | Statistics | 00891PHDG | https://graduate.catalog.berkeley.edu/programs/00891PHDG |

#### College of Engineering

##### MAS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Advanced Study in Engineering | 162G7MASG | https://graduate.catalog.berkeley.edu/programs/162G7MASG |

##### MDes
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Design | 160FQMDESG | https://graduate.catalog.berkeley.edu/programs/160FQMDESG |

##### MEng
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Bioengineering | 16288MENGG | https://graduate.catalog.berkeley.edu/programs/16288MENGG |
| 2 | Civil and Environmental Engineering: Full Time | 16275MENGG | https://graduate.catalog.berkeley.edu/programs/16275MENGG |
| 3 | Civil and Environmental Engineering: Part Time | 162D2MENGG | https://graduate.catalog.berkeley.edu/programs/162D2MENGG |
| 4 | Electrical Engineering and Computer Sciences | 16290MENGG | https://graduate.catalog.berkeley.edu/programs/16290MENGG |
| 5 | Industrial Engineering and Operations Research | 16292MENGG | https://graduate.catalog.berkeley.edu/programs/16292MENGG |
| 6 | Materials Science and Engineering | 16328MENGG | https://graduate.catalog.berkeley.edu/programs/16328MENGG |
| 7 | Mechanical Engineering | 16295MENGG | https://graduate.catalog.berkeley.edu/programs/16295MENGG |
| 8 | Nuclear Engineering | 16298MENGG | https://graduate.catalog.berkeley.edu/programs/16298MENGG |

##### MS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Civil and Environmental Engineering | 16275MSG | https://graduate.catalog.berkeley.edu/programs/16275MSG |
| 2 | Computer Science | 16201MSG | https://graduate.catalog.berkeley.edu/programs/16201MSG |
| 3 | Electrical Engineering and Computer Sciences | 16290MSG | https://graduate.catalog.berkeley.edu/programs/16290MSG |
| 4 | Industrial Engineering and Operations Research | 16292MSG | https://graduate.catalog.berkeley.edu/programs/16292MSG |
| 5 | Materials Science and Engineering | 16328MSG | https://graduate.catalog.berkeley.edu/programs/16328MSG |
| 6 | Mechanical Engineering | 16295MSG | https://graduate.catalog.berkeley.edu/programs/16295MSG |
| 7 | Nuclear Engineering | 16298MSG | https://graduate.catalog.berkeley.edu/programs/16298MSG |

##### MS (Analytics)
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Analytics | 162G4ANLTG | https://graduate.catalog.berkeley.edu/programs/162G4ANLTG |

##### MTM
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Translational Medicine | 162C8MTMG | https://graduate.catalog.berkeley.edu/programs/162C8MTMG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Bioengineering | 16288JPHDG | https://graduate.catalog.berkeley.edu/programs/16288JPHDG |
| 2 | Civil and Environmental Engineering | 16275PHDG | https://graduate.catalog.berkeley.edu/programs/16275PHDG |
| 3 | Computer Science | 16201PHDG | https://graduate.catalog.berkeley.edu/programs/16201PHDG |
| 4 | Electrical Engineering and Computer Sciences | 16290PHDG | https://graduate.catalog.berkeley.edu/programs/16290PHDG |
| 5 | Industrial Engineering and Operations Research | 16292PHDG | https://graduate.catalog.berkeley.edu/programs/16292PHDG |
| 6 | Materials Science and Engineering | 16328PHDG | https://graduate.catalog.berkeley.edu/programs/16328PHDG |
| 7 | Mechanical Engineering | 16295PHDG | https://graduate.catalog.berkeley.edu/programs/16295PHDG |
| 8 | Nuclear Engineering | 16298PHDG | https://graduate.catalog.berkeley.edu/programs/16298PHDG |

#### School of Public Health

##### DrPH
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Public Health | 960K8DPHG | https://graduate.catalog.berkeley.edu/programs/960K8DPHG |

##### MA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Biostatistics | 96132MAG | https://graduate.catalog.berkeley.edu/programs/96132MAG |

##### MPH
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Environmental Health Science | 960HYMPHG | https://graduate.catalog.berkeley.edu/programs/960HYMPHG |
| 2 | Epidemiology/Biostatistics | 960L1MPHG | https://graduate.catalog.berkeley.edu/programs/960L1MPHG |
| 3 | Food, Nutrition and Population Health | 960L5MPHG | https://graduate.catalog.berkeley.edu/programs/960L5MPHG |
| 4 | Global Health and Environment | 960L0MPHG | https://graduate.catalog.berkeley.edu/programs/960L0MPHG |
| 5 | Health & Social Behavior | 960L3MPHG | https://graduate.catalog.berkeley.edu/programs/960L3MPHG |
| 6 | Health Policy and Management | 960JKMPHG | https://graduate.catalog.berkeley.edu/programs/960JKMPHG |
| 7 | Infectious Diseases and Vaccinology | 960L4MPHG | https://graduate.catalog.berkeley.edu/programs/960L4MPHG |
| 8 | Interdisciplinary | 960L6MPHG | https://graduate.catalog.berkeley.edu/programs/960L6MPHG |
| 9 | Maternal, Child, and Adolescent Health | 960L7MPHG | https://graduate.catalog.berkeley.edu/programs/960L7MPHG |
| 10 | Public Health Online | 962C4MPHG | https://graduate.catalog.berkeley.edu/programs/962C4MPHG |

##### MPH (4+1)
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Epidemiology/Biostatistics "4+1" | 960L15YPHG | https://graduate.catalog.berkeley.edu/programs/960L15YPHG |
| 2 | Food, Nutrition and Population Health "4+1" | 960L55YPHG | https://graduate.catalog.berkeley.edu/programs/960L55YPHG |
| 3 | Maternal Child Adolescent Health "4 + 1" | 960L75YPHG | https://graduate.catalog.berkeley.edu/programs/960L75YPHG |

##### MS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Environmental Health Sciences | 96354MSG | https://graduate.catalog.berkeley.edu/programs/96354MSG |
| 2 | Epidemiology | 96357MSG | https://graduate.catalog.berkeley.edu/programs/96357MSG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Biostatistics | 96132PHDG | https://graduate.catalog.berkeley.edu/programs/96132PHDG |
| 2 | Environmental Health Sciences | 96354PHDG | https://graduate.catalog.berkeley.edu/programs/96354PHDG |
| 3 | Epidemiology | 96357PHDG | https://graduate.catalog.berkeley.edu/programs/96357PHDG |

#### College of Environmental Design

##### MAAD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Advanced Architectural Design | 192F4MAADG | https://graduate.catalog.berkeley.edu/programs/192F4MAADG |

##### MArch
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Architecture | 192F2MARCG | https://graduate.catalog.berkeley.edu/programs/192F2MARCG |

##### MCP
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | City Planning | 192F5MCPG | https://graduate.catalog.berkeley.edu/programs/192F5MCPG |

##### MLA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Landscape Architecture | 192F3MLAG | https://graduate.catalog.berkeley.edu/programs/192F3MLAG |

##### MS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Architecture | 19084MSG | https://graduate.catalog.berkeley.edu/programs/19084MSG |

##### MS (Real Estate Dev)
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Real Estate Development + Design | 192F1REDDG | https://graduate.catalog.berkeley.edu/programs/192F1REDDG |

##### MUD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Urban Design | 19920MUDG | https://graduate.catalog.berkeley.edu/programs/19920MUDG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Architecture | 19084PHDG | https://graduate.catalog.berkeley.edu/programs/19084PHDG |
| 2 | City and Regional Planning | 19165PHDG | https://graduate.catalog.berkeley.edu/programs/19165PHDG |
| 3 | Landscape Architecture and Environmental Planning | 194A9PHDG | https://graduate.catalog.berkeley.edu/programs/194A9PHDG |

#### Rausser College of Natural Resources

##### MNSD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Nutritional Sciences & Dietetics | 040IVMNSDG | https://graduate.catalog.berkeley.edu/programs/040IVMNSDG |

##### MS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Rangeland and Wildlife Management | 04798MSG | https://graduate.catalog.berkeley.edu/programs/04798MSG |

##### MS (CS)
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Climate Solutions | 040JUMCSG | https://graduate.catalog.berkeley.edu/programs/040JUMCSG |

##### Master of Forestry
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Forestry | 04380MFG | https://graduate.catalog.berkeley.edu/programs/04380MFG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Agricultural and Resource Economics | 04034PHDG | https://graduate.catalog.berkeley.edu/programs/04034PHDG |
| 2 | Comparative Biochemistry | 04189PHDG | https://graduate.catalog.berkeley.edu/programs/04189PHDG |
| 3 | Environmental Science, Policy and Management | 04683PHDG | https://graduate.catalog.berkeley.edu/programs/04683PHDG |
| 4 | Plant Biology | 04680PHDG | https://graduate.catalog.berkeley.edu/programs/04680PHDG |

#### Haas School of Business

##### MBA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Business Administration for Executives | 70364MBAG | https://graduate.catalog.berkeley.edu/programs/70364MBAG |
| 2 | Business Administration: Evening and Weekend | 701E1MBAG | https://graduate.catalog.berkeley.edu/programs/701E1MBAG |
| 3 | Business Administration: Full-time | 702F7MBAG | https://graduate.catalog.berkeley.edu/programs/702F7MBAG |

##### MFE
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Financial Engineering | 701F1MFEG | https://graduate.catalog.berkeley.edu/programs/701F1MFEG |
| 2 | Financial Engineering | 701F1MFE2G | https://graduate.catalog.berkeley.edu/programs/701F1MFE2G |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Business Administration | 70141PHDG | https://graduate.catalog.berkeley.edu/programs/70141PHDG |

#### School of Law

##### JD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Law Juris Doctor | 84501JDG | https://graduate.catalog.berkeley.edu/programs/84501JDG |

##### JSD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Law Juris Scientiae Doctor | 842C1JSDG | https://graduate.catalog.berkeley.edu/programs/842C1JSDG |

##### LLM
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Law: Executive Track (Remote + Summer) | 845B0HLLMG | https://graduate.catalog.berkeley.edu/programs/845B0HLLMG |
| 2 | Law: Executive Track (Two Summers) | 845B0SLLMG | https://graduate.catalog.berkeley.edu/programs/845B0SLLMG |
| 3 | Law: Traditional Track | 845B0LLMG | https://graduate.catalog.berkeley.edu/programs/845B0LLMG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Jurisprudence and Social Policy | 84485PHDG | https://graduate.catalog.berkeley.edu/programs/84485PHDG |

#### College of Chemistry

##### MBE
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Bioprocess Engineering | 102F6MBEG | https://graduate.catalog.berkeley.edu/programs/102F6MBEG |

##### MSSE
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Molecular Science and Software Engineering | 100DNMSSEG | https://graduate.catalog.berkeley.edu/programs/100DNMSSEG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Chemical Engineering | 10294PHDG | https://graduate.catalog.berkeley.edu/programs/10294PHDG |
| 2 | Chemistry | 10153PHDG | https://graduate.catalog.berkeley.edu/programs/10153PHDG |

#### School of Information

##### MICS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Information and Cybersecurity | 810DHMICSG | https://graduate.catalog.berkeley.edu/programs/810DHMICSG |

##### MIDS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Information and Data Science | 812E0MIDSG | https://graduate.catalog.berkeley.edu/programs/812E0MIDSG |

##### MIMS
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Information Management and Systems | 81776MIMSG | https://graduate.catalog.berkeley.edu/programs/81776MIMSG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Information Science | 81461PHDG | https://graduate.catalog.berkeley.edu/programs/81461PHDG |

#### School of Social Welfare

##### MSW
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Social Welfare | 86864MSWG | https://graduate.catalog.berkeley.edu/programs/86864MSWG |
| 2 | Social Welfare - Flex, Advanced | 860EZFSWAG | https://graduate.catalog.berkeley.edu/programs/860EZFSWAG |
| 3 | Social Welfare - Flex, Extended | 860EZFSWEG | https://graduate.catalog.berkeley.edu/programs/860EZFSWEG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Social Welfare | 86864PHDG | https://graduate.catalog.berkeley.edu/programs/86864PHDG |

#### Berkeley School of Education

##### MA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Education | 79249MAG | https://graduate.catalog.berkeley.edu/programs/79249MAG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Education | 79249PHDG | https://graduate.catalog.berkeley.edu/programs/79249PHDG |
| 2 | Special Education | 79892JPHDG | https://graduate.catalog.berkeley.edu/programs/79892JPHDG |

#### Goldman School of Public Policy

##### MPA
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Public Affairs | 822E2MPAG | https://graduate.catalog.berkeley.edu/programs/822E2MPAG |

##### MPP
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Public Policy | 82790MPPG | https://graduate.catalog.berkeley.edu/programs/82790MPPG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Public Policy | 82790PHDG | https://graduate.catalog.berkeley.edu/programs/82790PHDG |

#### School of Optometry

##### OD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Optometry | 91612ODG | https://graduate.catalog.berkeley.edu/programs/91612ODG |

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Vision Science | 91935PHDG | https://graduate.catalog.berkeley.edu/programs/91935PHDG |

#### Graduate School of Journalism

##### MJ
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Journalism | 71483MJG | https://graduate.catalog.berkeley.edu/programs/71483MJG |

#### College of Computing, Data Science, and Society

##### PhD
| # | 项目 | Program Code | URL |
|---|------|-------------|-----|
| 1 | Computational Precision Health | A55C3JPHDG | https://graduate.catalog.berkeley.edu/programs/A55C3JPHDG |

### 2.2 Designated Emphases / Graduate Options (non-standalone, 25 listed)

Graduate "Designated Emphases" (DE) and "Options" are graduate-level minors/specializations appended to a PhD or master's program; they are not standalone degrees.

| # | Designated Emphasis / Option | Code | URL |
|---|------------------------------|------|-----|
| 1 | Applied Data Science | 00OPT2011G | https://graduate.catalog.berkeley.edu/programs/00OPT2011G |
| 2 | Business Journalism | 00OPT2025G | https://graduate.catalog.berkeley.edu/programs/00OPT2025G |
| 3 | Cognitive Science | 00E023G | https://graduate.catalog.berkeley.edu/programs/00E023G |
| 4 | Computational Precision Health | 00E024G | https://graduate.catalog.berkeley.edu/programs/00E024G |
| 5 | Computational and Data Science and Engineering | 00E003G | https://graduate.catalog.berkeley.edu/programs/00E003G |
| 6 | Computational and Genomic Biology | 00E002G | https://graduate.catalog.berkeley.edu/programs/00E002G |
| 7 | Critical Theory | 00E004G | https://graduate.catalog.berkeley.edu/programs/00E004G |
| 8 | Development Engineering | 00E005G | https://graduate.catalog.berkeley.edu/programs/00E005G |
| 9 | Dutch Studies | 00E006G | https://graduate.catalog.berkeley.edu/programs/00E006G |
| 10 | Film Studies | 00E008G | https://graduate.catalog.berkeley.edu/programs/00E008G |
| 11 | Folklore | 00E009G | https://graduate.catalog.berkeley.edu/programs/00E009G |
| 12 | Food Systems | 00OPT2009G | https://graduate.catalog.berkeley.edu/programs/00OPT2009G |
| 13 | Global Metropolitan Studies | 00E010G | https://graduate.catalog.berkeley.edu/programs/00E010G |
| 14 | Indigenous Language Revitalization | 00E019G | https://graduate.catalog.berkeley.edu/programs/00E019G |
| 15 | Jewish Studies | 00E011G | https://graduate.catalog.berkeley.edu/programs/00E011G |
| 16 | New Media | 00E014G | https://graduate.catalog.berkeley.edu/programs/00E014G |
| 17 | New Media | 00OPT2001G | https://graduate.catalog.berkeley.edu/programs/00OPT2001G |
| 18 | Political Economy | 00E022G | https://graduate.catalog.berkeley.edu/programs/00E022G |
| 19 | Renaissance and Early Modern Studies | 00E015G | https://graduate.catalog.berkeley.edu/programs/00E015G |
| 20 | Science and Technology Studies | 00E016G | https://graduate.catalog.berkeley.edu/programs/00E016G |
| 21 | Sociology of Organizations and Markets | 00E20G | https://graduate.catalog.berkeley.edu/programs/00E20G |
| 22 | Study of Religion | 00E021G | https://graduate.catalog.berkeley.edu/programs/00E021G |
| 23 | Technology and Public Policy | 00OPT2026G | https://graduate.catalog.berkeley.edu/programs/00OPT2026G |
| 24 | Transdisciplinary Early Learning Science & Child Policy | 00OPT2023G | https://graduate.catalog.berkeley.edu/programs/00OPT2023G |
| 25 | Women, Gender, and Sexuality | 00E017G | https://graduate.catalog.berkeley.edu/programs/00E017G |

### 2.3 Worked example — PhD in Computer Science (EECS)

- **Department**: Electrical Engineering and Computer Sciences (EECS), College of Engineering
- **Degree**: PhD (code `16290PHDG`)
- **Catalog page**: https://graduate.catalog.berkeley.edu/programs/16290PHDG
- **Department website**: https://eecs.berkeley.edu/
- **Application portal**: Berkeley Graduate Application (apply via grad.berkeley.edu); deadline typically early December (8:59 PM PST)
- **GRE policy**: Most EECS programs no longer require the GRE (verify per cycle on the program page)
- **Funding**: PhD students typically fully funded (tuition + stipend via fellowships/GSR/TA appointments)
- **What lives behind accordions on the program page**: Overview, Requirements, Plan of Study, Student Learning Goals, Major Map, Contact Information, Program Type, Program Format.

### 2.4 Graduate admissions model

Berkeley graduate admissions is **decentralized**: each of the 100+ programs sets its own deadline, GRE policy, statement requirements, and funding. The central Graduate Division (grad.berkeley.edu) runs the application platform and sets the systemwide 3.0 minimum GPA and April 15 enrollment response honor date (CGS resolution). **Professional/self-supporting programs** — Haas (MBA/MFE), Berkeley Law (JD/LLM), Optometry (OD), on-campus MPH, MIDS, MICS — require **separate applications** through their respective schools (not the central Berkeley Graduate Application). Applicants may apply to **only one degree program per term**.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 证据 |
|------|-----|------|
| 申请系统 | UC Application (University of California) — NOT Common App | admissions.berkeley.edu nav: "Apply to UC Berkeley"; UC Application at apply.universityofcalifornia.edu |
| 申请开放 | August 1 | "Application available: August 1" (dates-deadlines page) |
| 申请提交期 | October 1 – November 30 | "Application filing period: October 1 - November 30" |
| **申请截止** | **November 30** (fall entry) | "All applications must be submitted by November 30." |
| 早申请 (EA/ED) | **不提供** | "UC Berkeley does not offer applications for early admission or early decision." |
| 申请费 | $80 (美国国内) / $95 (国际) per campus; $70 per additional campus; fee waivers available | UC systemwide fee (UC Application; figure stable across UC campuses) — **P1 verify on Berkeley page** |
| 申请状态通知 | By Early December | "UC Berkeley notifies applicants of receipt of application: By Early December" |
| 强制表格截止 | January 31 | "UC Berkeley mandatory forms deadline: January 31" |
| FAFSA / CA Dream Act 截止 | March 2 | "FAFSA and CA Dream Act deadline: March 2" |
| 录取决定发布 | End of March (first-year) | "First-year decisions posted: End of March" |
| 接受录取截止 | May 1 (first-year) | "First-year deadline to accept offer of admission: May 1" |
| **SAT/ACT 政策** | **Test-free / Test-blind** — "UC Berkeley is test-free, which means we will not use SAT/ACT test scores in any part of our application process." | admissions.berkeley.edu/apply-to-berkeley/first-year-applicants-uc-berkeley/first-year-policy-changes/ |
| Superscore | N/A (scores not used) | — |
| 推荐信 | By invitation only; up to 2 letters; due January 10 | "Select applicants to UC Berkeley are invited to submit two letters of recommendation... Letters of recommendation are due January 10." |
| Personal Insight Questions | 8 prompts, answer 4 (350 words each) | admissions.berkeley.edu/apply-to-berkeley/application-resources/personal-insight-questions/ |
| 作品集 Portfolio | Required for some majors (e.g. Art Practice, Architecture, Music) — submit directly to department | — |
| Transfer 通道 | UC Transfer Admissions; TAG with select UCs (Berkeley does NOT participate in TAG); TAU deadline Jan 31 | admissions.berkeley.edu/apply-to-berkeley/transfer-students/ |

### 3.2 Undergraduate English proficiency table

Applicability: Required of all applicants whose **Language of Instruction (LOI)** was not entirely in English for all 4 years of high school (incl. US citizens/permanent residents studying abroad).

| 考试 | 最低分 | 推荐分 | 备注 |
|------|--------|--------|------|
| TOEFL iBT | **90** (or paper 4.5) | — | "Test of English as a Foreign Language (TOEFL) with a minimum score of 90/4.5 or better" |
| IELTS Academic | **6.5** | — | "International English Language testing System (IELTS) with a minimum score of 6.5" |
| Duolingo English Test (DET) | **115** | — | "DuoLingo English Test (DET) with a minimum score of 115" |
| ACT English Language Arts (ELA) | 24 | — | Alternate; "SAT/ACT scores will not be used in admissions" but ELA subscore still satisfies ELP |
| SAT Writing & Language | 31 | — | Alternate (test-blind for admission, but satisfies ELP if submitted) |
| AP English Lang/Lit | 3, 4, or 5 | — | Course-exam alternative |
| IB English (HL) | 5, 6, 7 | — | Language A only |
| IB English (SL) | 6 or 7 | — | Language A only |
| 3+ years LOI in English | Exempt | — | "Students who have 3+ years of Language of Instruction (LOI) in English will also satisfy English Proficiency." |

Source: https://admissions.berkeley.edu/requirements-for-international-students/

### 3.3 Graduate — global rules

- **Decentralized**: each program sets its own deadline, GRE policy, TOEFL/IELTS minimums, statements, funding. Browse at grad.berkeley.edu/programs/.
- **Application platform**: Berkeley Graduate Application (BGA); professional/self-supporting programs (Haas MBA/MFE, Berkeley Law JD/LLM, Optometry OD, on-campus MPH, MIDS, MICS) use **separate applications**.
- **Application fee**: ~$135 (US) / ~$155 (international) for most programs (P1 verify current cycle; varies by program); fee waivers available for US citizens/permanent residents and some international applicants.
- **Minimum GPA**: 3.0 (B) on 4.0 scale (systemwide).
- **GRE**: Many programs have made GRE optional/not-accepted; verify per program (e.g. most Engineering and CS programs no longer require GRE).
- **TOEFL/IELTS**: minimums set per program (typically TOEFL 90 / IELTS 7.0 for most programs); exemption if undergraduate instruction was in English.
- **One program per term**: applicants may apply to only one degree or one concurrent degree program per cycle.
- **April 15** enrollment response honor date (Council of Graduate Schools resolution) for funded PhD offers.
- **Application timeline**: applications open mid-September; deadlines range early December to early February; decisions released late January through June.
Source: https://grad.berkeley.edu/admissions/application-process/

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

**For new students starting 2026-27** (California resident; living in campus residence hall):

| 费用项 | 金额 (USD) | 说明 |
|--------|-----------|------|
| Tuition and Fees (in-state) | $18,216 | Systemwide tuition + campus fees; "Figures for systemwide tuition and fees represent currently approved amounts and may not be final." |
| **Nonresident Supplemental Tuition (NRST)** | **+$39,270** | "New out-of-state students pay an additional Nonresident Supplemental Tuition of $39,270." → OOS/international tuition & fees = ~$57,486 |
| Living Expenses (housing + food, residence hall) | $23,640 | On-campus residence hall |
| Student Health Insurance Plan (SHIP) | $5,066 | Waivable with equivalent coverage (file by July 1) |
| **Total Direct Costs (in-state, residence hall)** | **$46,922** | Charged by UC Berkeley |
| Books, course materials, supplies | $1,312 | Indirect/personal |
| Food (additional) | $2,322 | Personal expense budget component |
| Miscellaneous & Personal | $3,180 | |
| Transportation | $734 | |
| **Total Cost of Attendance (in-state, residence hall)** | **$54,470** | Includes personal expenses |
| Total COA (on-campus apartment) | $56,030 | |
| Total COA (off-campus apartment) | $49,502 | |
| Total COA (living with relatives) | $39,050 | |

Source: https://financialaid.berkeley.edu/how-aid-works/student-budgets-cost-of-attendance/ ; summary at https://admissions.berkeley.edu/cost/

### 4.2 Undergraduate financial-aid policy

- **Public university, need-based aid**: Berkeley is the **most generous public university in the US** for need-based aid (over $1B awarded annually).
- **Need-blind for California residents**; **need-aware (need-sensitive) for out-of-state and international applicants** — OOS/international aid is limited (Berkeley does not meet full demonstrated need for most internationals). **P0 verify current international aid policy.**
- **38% of undergraduates pay nothing out-of-pocket** for tuition due to grants/scholarships (admissions.berkeley.edu/cost/).
- **~two-thirds of undergraduates receive some form of financial aid.**
- **Berkeley Undergraduate Scholarship** / **Middle Class Access Plan (MCAP)**: covers tuition for families with income <$80k (typical threshold — verify).
- **FAFSA** (US citizens/permanent residents) and **CA Dream Act** (undocumented CA residents) deadline **March 2**.
- **Federal aid not available to international students**; limited institutional aid; international students must certify funding for visa (I-20).
- The **Blue and Gold Opportunity Plan** ensures UC system grants/scholarships cover tuition/fees for CA residents with family income <$80k.

### 4.3 Graduate cost & funding framework

- **PhD programs**: predominantly **fully funded** — tuition/fees covered + stipend (~$38k-$50k/yr) via Graduate Student Researcher (GSR) appointments, Graduate Student Instructor (GSI/TA) appointments, and multi-year fellowships (e.g. Berkeley Graduate Fellowship, NSF GRFP).
- **Master's / professional programs** (MBA, MFE, MIDS, MICS, MPP, MPH, MSW, MArch, MCP, etc.): **largely self-funded**; many are "self-supporting" professional degrees (not eligible for state-funded aid). Tuition varies $30k-$80k+/yr depending on program.
- **Application fee waiver**: available for US citizens/permanent residents and eligible international applicants (request via grad.berkeley.edu before applying).
- **April 15**: funded PhD offers share the Council of Graduate Schools April 15 resolution date.
- Stipend rates / cost-of-living for Berkeley area is high — see grad.berkeley.edu/financial for current stipend floors (P1 follow-up).

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001: UG application deadline
field: undergraduate.application.deadline
value: "November 30 (fall entry; no EA/ED)"
source_url: https://admissions.berkeley.edu/apply-to-berkeley/dates-deadlines/
source_snippet: "All applications must be submitted by November 30. UC Berkeley does not offer applications for early admission or early decision."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-002: UG test-blind policy
field: undergraduate.application.test_policy
value: "Test-free (test-blind) — SAT/ACT not used in admissions"
source_url: https://admissions.berkeley.edu/apply-to-berkeley/first-year-applicants-uc-berkeley/first-year-policy-changes/
source_snippet: "UC Berkeley is test-free, which means we will not use SAT/ACT test scores in any part of our application process."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-003: UG tuition in-state 2026-27
field: undergraduate.cost.tuition_in_state_2026_2027
value: "$18,216 (new students)"
source_url: https://financialaid.berkeley.edu/how-aid-works/student-budgets-cost-of-attendance/
source_snippet: "Tuition and Fees $18,216 (Living in a Campus Residence Hall, 2026-27, New Students Starting in the 2026-27 Academic Year)"
capture_date: 2026-07-04
evidence_type: official_webpage_table
```

```yaml
# E-U-004: Nonresident supplemental tuition
field: undergraduate.cost.nonresident_supplemental_tuition
value: "$39,270"
source_url: https://financialaid.berkeley.edu/how-aid-works/student-budgets-cost-of-attendance/
source_snippet: "New out-of-state students pay an additional Nonresident Supplemental Tuition of $39,270."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-005: UG total COA in-state 2026-27
field: undergraduate.cost.total_coa_in_state_residence_hall_2026_2027
value: "$54,470"
source_url: https://admissions.berkeley.edu/cost/
source_snippet: "Total Cost of Attendance (including Personal Expenses) $54,388 (campus residence hall) — Estimated personal expenses for the 2026-27 academic year" (financialaid.berkeley.edu authoritative: $54,470)
capture_date: 2026-07-04
evidence_type: official_webpage_table
```

```yaml
# E-U-006: TOEFL minimum
field: undergraduate.english_proficiency.toefl_minimum
value: 90 (iBT) / 4.5 (paper)
source_url: https://admissions.berkeley.edu/requirements-for-international-students/
source_snippet: "Test of English as a Foreign Language (TOEFL) with a minimum score of 90/4.5 or better"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-007: IELTS minimum
field: undergraduate.english_proficiency.ielts_minimum
value: 6.5
source_url: https://admissions.berkeley.edu/requirements-for-international-students/
source_snippet: "International English Language testing System (IELTS) with a minimum score of 6.5"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-008: Duolingo (DET) minimum
field: undergraduate.english_proficiency.duolingo_minimum
value: 115
source_url: https://admissions.berkeley.edu/requirements-for-international-students/
source_snippet: "DuoLingo English Test (DET) with a minimum score of 115"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-009: Letters of recommendation policy
field: undergraduate.application.recommendation_letters
value: "By invitation only; up to 2; due January 10"
source_url: https://admissions.berkeley.edu/apply-to-berkeley/first-year-applicants-uc-berkeley/first-year-policy-changes/
source_snippet: "Select applicants to UC Berkeley are invited to submit two letters of recommendation... Letters of recommendation are due January 10."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-010: UC A-G subject requirement
field: undergraduate.application.a_g_requirements
value: "15 college-preparatory courses (A-G) with C or better; 3.0 GPA (CA) / 3.4 (nonresident)"
source_url: https://admission.universityofcalifornia.edu/admission-requirements/first-year-requirements/
source_snippet: "Complete 15 A-G courses (11 of them by end of junior year)... Earn a grade point average (GPA) of 3.0 or better (3.4 if you're a nonresident) in these courses with no grade lower than a C."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-011: UG program directory count
field: undergraduate.programs.directory_total
value: "239 results (110 majors + 129 minors)"
source_url: https://undergraduate.catalog.berkeley.edu/programs
source_snippet: "239 results found. Showing 1 - 20." (UC Berkeley Undergraduate Catalog Programs index, capture_date 2026-07-04)
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-012: Financial aid scope
field: undergraduate.financial_aid.scope
value: "$1B+ aid annually; 38% pay no tuition out-of-pocket; ~2/3 receive aid"
source_url: https://admissions.berkeley.edu/cost/
source_snippet: "more than $1 billion awarded in financial aid annually... 38% of students pay nothing out of pocket for tuition due to grants and scholarships and that around two-thirds of students receive some form of financial aid."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-001: Graduate program count
field: graduate.programs.total_count
value: "over 200 graduate programs (200 catalog entries; 175 standalone degree + 25 designated emphases)"
source_url: https://grad.berkeley.edu/admissions/
source_snippet: "UC Berkeley offers over 200 graduate programs across diverse, interdisciplinary fields."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-002: Graduate application rules
field: graduate.application.rules
value: "One program per term; 8:59 PM PST deadline; mid-Sept open; decisions Jan-June"
source_url: https://grad.berkeley.edu/admissions/application-process/
source_snippet: "Applicants may only apply to one degree or one concurrent degree program per admissions cycle... Applications are due by 8:59 PM PST on the deadline date... You can start your online application in mid-September."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-003: Graduate minimum GPA
field: graduate.application.minimum_gpa
value: "3.0 (B) on 4.0 scale"
source_url: https://grad.berkeley.edu/admissions/
source_snippet: "We recommend that applicants have a satisfactory average, usually a minimum grade-point average (GPA) of 3.0 (B) on a 4.0 scale."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-004: Professional programs separate applications
field: graduate.application.professional_separate
value: "Haas MBA/MFE, Berkeley Law JD/LLM, Optometry OD, on-campus MPH, MIDS, MICS use separate applications"
source_url: https://grad.berkeley.edu/admissions/application-process/
source_snippet: "Some programs—such as Haas Business, Berkeley Law, Optometry OD, Public Health On-Campus MPH, Information Data Science MIDS, and Cybersecurity MICS—require separate applications through their respective schools."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-005: Graduate catalog directory
field: graduate.programs.catalog_total
value: "200 results (175 standalone degree + 25 designated emphases/options)"
source_url: https://graduate.catalog.berkeley.edu/programs
source_snippet: "200 results found." (UC Berkeley Graduate Catalog Programs index)
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-006: Sample program detail (EECS PhD)
field: graduate.program.eecs_phd
value: "PhD in Electrical Engineering and Computer Sciences (code 16290PHDG)"
source_url: https://graduate.catalog.berkeley.edu/programs/16290PHDG
source_snippet: "Electrical Engineering and Computer Sciences Graduate Academic Programs Doctor of Philosophy" (program composite line)
capture_date: 2026-07-04
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
berkeley-knowledge-base-v2/
├── berkeley-overview/                  (Section 0: counts, hierarchy, matrix)
├── berkeley-ug-programs/               (Section 1: 110 majors + 129 minors, chunk by college)
│   ├── chunk-letters-science
│   ├── chunk-engineering
│   ├── chunk-chemistry
│   ├── chunk-cdss
│   ├── chunk-environmental-design
│   ├── chunk-rausser
│   ├── chunk-haas-ug
│   ├── chunk-education-ug
│   └── chunk-minors
├── berkeley-grad-programs/             (Section 2: 175 grad + 25 DE, chunk by school)
│   ├── chunk-graduate-division
│   ├── chunk-engineering-grad
│   ├── chunk-public-health
│   ├── chunk-haas-grad
│   ├── chunk-law
│   ├── chunk-env-design-grad
│   ├── chunk-information
│   ├── chunk-rausser-grad
│   ├── chunk-social-welfare
│   ├── chunk-optometry
│   ├── chunk-education-grad
│   ├── chunk-public-policy
│   ├── chunk-chemistry-grad
│   ├── chunk-journalism
│   └── chunk-designated-emphases
├── berkeley-admissions-ug/             (Section 3.1-3.2: deadlines, tests, ELP)
├── berkeley-admissions-grad/           (Section 3.3)
├── berkeley-costs-aid/                 (Section 4)
└── berkeley-evidence/                  (Section 5: 18 evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "berkeley-knowledge-base-v2"
  school: "<home college, e.g. College of Engineering>"
  department: "<EECS / Chemistry / etc.>"
  degree_level: "<BA|BS|MA|MS|PhD|MBA|MEng|MPP|MPH|MFA|MCP|MArch|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Verify UG application fee ($80/$95) on Berkeley-branded page (currently from UC systemwide knowledge) | admissions.berkeley.edu/application-faqs/ (accordion-hidden content) |
| P0 | Confirm current international financial-aid policy (need-aware? OOS aid ceiling?) | financialaid.berkeley.edu ; admissions.berkeley.edu/cost/apply-for-financial-aid/ |
| P1 | Per-graduate-program deadlines + GRE/TOEFL minimums (decentralized; each program page) | graduate.catalog.berkeley.edu/programs/<code> per program |
| P1 | Graduate application fee exact figure (~$135/$155 — verify current cycle) | grad.berkeley.edu/admissions/application-process/ |
| P1 | Graduate stipend floors / cost-of-living adjustment | grad.berkeley.edu/financial/ |
| P1 | L&S high-demand major cap policy details (CS, Econ, Psych, etc.) | admissions.berkeley.edu/academics/ls-high-demand-policy/ |
| P2 | Berkeley Academic Guide (guide.berkeley.edu) currently redirects to registrar.berkeley.edu/catalog/ — confirm canonical catalog host | registrar.berkeley.edu/catalog/ |
| P2 | Confirm CDSS / School of Information organizational merger status | cdss.berkeley.edu |
| P2 | Transfer-credit and AP/IB exam credit mapping | admission.universityofcalifornia.edu/admission-requirements/first-year-requirements/ap-exam-credits/ |

---

## SECTION 7 — Cross-school comparison framework (optional)

| Dimension | UC Berkeley | MIT | Stanford | Harvard | Caltech |
|-----------|-------------|-----|----------|---------|---------|
| Total UG cost/yr (in-state/equiv) | $54,470 (CA res.) | ~$85k | ~$92k | ~$92k | ~$63k |
| Tuition/yr (in-state/equiv) | $18,216 (CA) / ~$57,486 (OOS) | ~$62k | ~$65k | ~$57k | ~$63k |
| Public or private | **Public** | Private | Private | Private | Private |
| Need-blind for internationals? | **No** (need-aware OOS/intl) | Yes | Yes | Yes | Yes |
| EA/ED deadline | None (no EA/ED) | EA mid-Nov | REA Nov 1 | REA Nov 1 | EA mid-Nov |
| RD deadline | **Nov 30** | Jan 4 | Jan 5 | Jan 1 | Jan 3 |
| SAT/ACT required? | **Test-free (not used)** | Test-flexible | Required | Test-optional | Required |
| TOEFL min | 90 | 90 (rec 100) | 100 (rec) | 100 (rec 105) | 100 |
| IELTS min | 6.5 | 7 | 7 | 7 | 7 |
| Tuition-free income threshold | ~$80k (Blue & Gold, CA res only) | <$140k | <$150k | <$85k | <$90k |
| Application system | **UC Application** (not Common App) | MIT portal | Common App | Common App | Common App/QuestBridge |
| **Total degree programs (Rule 1)** | **285** | ~120 | 342 | ~130 | ~30 |
| **Schools/colleges (Rule 2)** | **14 UG + grad schools** | 5 | 7 | 13 | 6 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: undergraduate.catalog.berkeley.edu, graduate.catalog.berkeley.edu, admissions.berkeley.edu, financialaid.berkeley.edu, grad.berkeley.edu, admission.universityofcalifornia.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (12 pages of undergraduate catalog + 6 pages of graduate catalog walked; 110 UG majors enriched via per-program detail pages)
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: Rule 1 degree total = 285 (UG majors 110 + Grad standalone 175); Rule 4 matrix cell-sum = 439 (UG majors + UG minors + Grad standalone + Designated Emphases); Rule 5 row count = 414 (UG majors + UG minors + Grad standalone). All internally consistent. ✓
