# Arizona State University (ASU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 490 |
| 本科辅修 (Minor) | N/A (see note) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 554 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 140 |
| **学位项目总计 (UG + Grad)** | **1184** |
| 学院 / 独立系所总数 | 17+ |

> Note: ASU does not publish a separate minors catalog in the same format as majors. Minors are listed within individual program pages but not aggregated in the degrees.apps.asu.edu system.

### 0.2 学院 / 系层级结构

```
Arizona State University
├── The College of Liberal Arts and Sciences (CLA)              [学院]
│   ├── School of Earth and Space Exploration                   [系]
│   ├── School of Historical, Philosophical and Religious Studies [系]
│   ├── School of Human Evolution and Social Change              [系]
│   ├── School of International Letters and Cultures             [系]
│   ├── School of Life Sciences                                  [系]
│   ├── School of Mathematical and Natural Sciences              [系]
│   ├── School of Molecular Sciences                             [系]
│   ├── School of Politics and Global Studies                    [系]
│   ├── School of Social and Behavioral Sciences                 [系]
│   └── School of Social Transformation                          [系]
├── Ira A. Fulton Schools of Engineering (CES)                  [学院]
│   ├── School of Biological and Health Systems Engineering      [系]
│   ├── School of Computing and Augmented Intelligence           [系]
│   ├── School of Electrical, Computer and Energy Engineering    [系]
│   ├── School for Engineering of Matter, Transport and Energy   [系]
│   ├── School of Manufacturing Systems and Networks             [系]
│   ├── School of Materials Science, Chemical and Energy Engineering [系]
│   ├── School of Sustainable Engineering and the Built Environment [系]
│   └── Polytechnic School                                       [系]
├── Herberger Institute for Design and the Arts (CHI)           [学院]
│   ├── School of Art                                           [系]
│   ├── School of Arts, Media and Engineering                    [系]
│   ├── School of Music                                         [系]
│   ├── School of Film, Dance and Theatre                       [系]
│   ├── The Design School                                       [系]
│   └── School of Arts and Cultural Leadership                   [系]
├── W. P. Carey School of Business (CBA)                       [学院]
│   ├── Department of Accountancy                                [系]
│   ├── Department of Finance                                    [系]
│   ├── Department of Information Systems                       [系]
│   ├── Department of Management and Entrepreneurship            [系]
│   └── Department of Marketing                                  [系]
├── Watts College of Public Service & Community Solutions (CPP) [学院]
│   ├── School of Community Resources and Development            [系]
│   ├── School of Criminology and Criminal Justice               [系]
│   ├── School of Public Affairs                                 [系]
│   └── School of Social Work                                   [系]
├── Edson College of Nursing and Health Innovation (CNU)        [学院]
├── College of Health Solutions (CHL)                           [学院]
├── College of Integrative Sciences and Arts (CLS)              [学院]
├── New College of Interdisciplinary Arts and Sciences (CAS)    [学院]
├── Mary Lou Fulton College for Teaching and Learning Innovation (CTE) [学院]
├── Walter Cronkite School of Journalism and Mass Communication (CCS) [学院]
├── Rob Walton College of Global Futures (CGF)                  [学院]
├── Thunderbird School of Global Management (CTB)               [学院]
├── Sandra Day O'Connor College of Law (LW)                     [学院]
├── John Shufeldt School of Medicine and Medical Engineering    [学院]
├── School of Technology for Public Health                      [学院]
├── Barrett, The Honors College (CHO)                           [学院]
└── University College (CUC)                                    [学院]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 204 |
| MS | Master of Science | 研究生 | 175 |
| BA | Bachelor of Arts | 本科 | 163 |
| Graduate Certificate | Graduate Certificate | 研究生 | 140 |
| PhD | Doctor of Philosophy | 研究生 | 123 |
| MA | Master of Arts | 研究生 | 83 |
| BSE | Bachelor of Science in Engineering | 本科 | 28 |
| BFA | Bachelor of Fine Arts | 本科 | 21 |
| Unknown |  | graduate | 19 |
| MGM | Master of Global Management | 研究生 | 19 |
| BAS | Bachelor of Applied Science | 本科 | 17 |
| MEd | Master of Education | 研究生 | 16 |
| BAE | Bachelor of Arts in Education | 本科 | 15 |
| BMUS | Bachelor of Music | 本科 | 11 |
| DNP | Doctor of Nursing Practice | 研究生 | 10 |
| MFA | Master of Fine Arts | 研究生 | 10 |
| MAS | Master of Advanced Study | 研究生 | 8 |
| MM | Master of Music | 研究生 | 8 |
| AA | Associate of Arts | 本科 | 6 |
| MSD | Master of Science in Design | 研究生 | 6 |
| MPA | Master of Public Administration | 研究生 | 5 |
| BSD | Bachelor of Science in Design | 本科 | 4 |
| LLM | Master of Laws | 研究生 | 4 |
| DMA | Doctor of Musical Arts | 研究生 | 4 |
| MSE | Master of Science in Engineering | 研究生 | 4 |
| MPP | Master of Public Policy | 研究生 | 4 |
| MPSLA |  | graduate | 4 |
| MSW | Master of Social Work | 研究生 | 4 |
| AS | Associate of Science | 本科 | 3 |
| DBA | Doctor of Business Administration | 研究生 | 3 |
| MCS | Master of Computer Science | 研究生 | 3 |
| DBH | Doctor of Behavioral Health | 研究生 | 2 |
| MC |  | graduate | 2 |
| EdD | Doctor of Education | 研究生 | 2 |
| PSM |  | graduate | 2 |
| DPP | Doctor of Public Policy | 研究生 | 2 |
| MGLS |  | graduate | 2 |
| MLS |  | graduate | 2 |
| MLM |  | graduate | 2 |
| MNS |  | graduate | 2 |
| MSTech |  | graduate | 2 |
| BGM | Bachelor of Global Management | 本科 | 1 |
| BIPH | Bachelor of Interdisciplinary Studies (Public Health) | 本科 | 1 |
| BSLA | Bachelor of Science in Landscape Architecture | 本科 | 1 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| BSP | Bachelor of Science in Planning | 本科 | 1 |
| MACC | Master of Accountancy | 研究生 | 1 |
| MALM |  | graduate | 1 |
| MArch |  | graduate | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| DCJ | Doctor of Criminal Justice | 研究生 | 1 |
| DEng | Doctor of Engineering | 研究生 | 1 |
| MEng | Master of Engineering | 研究生 | 1 |
| MHI |  | graduate | 1 |
| MHREL |  | graduate | 1 |
| MID |  | graduate | 1 |
| DIT | Doctor of Integrated Technology | 研究生 | 1 |
| MIA |  | graduate | 1 |
| MIHM |  | graduate | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| MLA |  | graduate | 1 |
| MLSt |  | graduate | 1 |
| MMC | Master of Mass Communication | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| MNLM |  | graduate | 1 |
| MPM |  | graduate | 1 |
| EMPA |  | graduate | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MRED |  | graduate | 1 |
| MSTP |  | graduate | 1 |
| MSLB |  | graduate | 1 |
| EMSL |  | graduate | 1 |
| MSL |  | graduate | 1 |
| MSUS |  | graduate | 1 |
| MST |  | graduate | 1 |
| MTax |  | graduate | 1 |
| MTESOL |  | graduate | 1 |
| MUD |  | graduate | 1 |
| MUEP |  | graduate | 1 |
| MVCD |  | graduate | 1 |

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院 \ 级别 | BA | BS | BSE | BFA | BMUS | BSD | MS | MA | PhD | Graduate Certificate | MEd | DNP | MFA | MGM | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|
| The College of Liberal Arts and Sciences | 55 | 50 | 0 | 0 | 0 | 0 | 33 | 39 | 54 | 32 | 0 | 0 | 1 | 0 | **280** |
| Ira A. Fulton Schools of Engineering | 0 | 25 | 28 | 0 | 0 | 0 | 64 | 0 | 24 | 13 | 0 | 0 | 0 | 0 | **170** |
| Herberger Institute for Design and the Arts | 28 | 5 | 0 | 21 | 11 | 4 | 7 | 9 | 12 | 6 | 0 | 0 | 9 | 0 | **142** |
| Watts College of Public Service & Community Solutions | 1 | 27 | 0 | 0 | 0 | 0 | 8 | 7 | 3 | 18 | 0 | 0 | 0 | 0 | **88** |
| New College of Interdisciplinary Arts and Sciences | 29 | 25 | 0 | 0 | 0 | 0 | 9 | 5 | 1 | 9 | 0 | 0 | 0 | 0 | **85** |
| W. P. Carey School of Business | 24 | 14 | 0 | 0 | 0 | 0 | 11 | 0 | 8 | 3 | 0 | 0 | 0 | 0 | **74** |
| College of Integrative Sciences and Arts | 14 | 24 | 0 | 0 | 0 | 0 | 9 | 1 | 1 | 5 | 0 | 0 | 0 | 0 | **65** |
| Mary Lou Fulton College for Teaching and Learning Innovation | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 11 | 4 | 12 | 15 | 0 | 0 | 0 | **63** |
| College of Health Solutions | 0 | 19 | 0 | 0 | 0 | 0 | 13 | 0 | 5 | 7 | 1 | 0 | 0 | 0 | **52** |
| Edson College of Nursing and Health Innovation | 0 | 5 | 0 | 0 | 0 | 0 | 10 | 0 | 1 | 15 | 0 | 10 | 0 | 0 | **45** |
| Rob Walton College of Global Futures | 2 | 6 | 0 | 0 | 0 | 0 | 7 | 1 | 6 | 7 | 0 | 0 | 0 | 0 | **32** |
| Thunderbird School of Global Management | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 19 | **32** |
| Walter Cronkite School of Journalism and Mass Communication | 8 | 1 | 0 | 0 | 0 | 0 | 2 | 8 | 1 | 1 | 0 | 0 | 0 | 0 | **22** |
| Sandra Day O'Connor College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | **13** |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | **9** |
| University College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **5** |
| Ira A. Fulton Schools of Engineering New College of Interdisciplinary Arts and Sciences | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| School of Technology for Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| Barrett, The Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| College of Integrative Sciences and Arts Ira A. Fulton Schools of Engineering | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| John Shufeldt School of Medicine and Medical Engineering | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| **合计** | 163 | 204 | 28 | 21 | 11 | 4 | 175 | 83 | 123 | 140 | 16 | 10 | 10 | 19 | **1184** |

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

ASU has 17+ colleges and schools offering undergraduate programs. The full hierarchy is shown in Section 0.2. Programs are grouped below by 学院 > 学位级别.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

#### Barrett, The Honors College
#### College of Health Solutions
##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Applied Nutrition and Health) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ECNTRBAS/applied-science-applied-nutrition-and-health |
| 2 | Applied Science (Health Sciences) | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHSCBAS/applied-science-health-sciences |
| 3 | Applied Science (Medical Laboratory Science) | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUMLSBAS/applied-science-medical-laboratory-science |

##### BIPH
| # | 专业 | URL |
|---|------|-----|
| 1 | International Public Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHIPHBIPH/international-public-health |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Nutrition and Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHFNUENBS/applied-nutrition-and-health |
| 2 | Biomedical Informatics and Data Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESBMIBS/biomedical-informatics-and-data-science |
| 3 | Clinical Exercise Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ECEXERBS/clinical-exercise-science |
| 4 | Dietetics | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHDIETCSBS/dietetics |
| 5 | Health Care Administration and Policy | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHHCDBS/health-care-administration-and-policy |
| 6 | Health Education and Health Promotion | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHHEHPBS/health-education-and-health-promotion |
| 7 | Health Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHHSCBS/health-sciences |
| 8 | Health Sciences (Healthy Lifestyles and Fitness Science) | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHSCHLCBS/health-sciences-healthy-lifestyles-and-fitness-science |
| 9 | Health Sciences (Pre-professional) | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHSCPREBS/health-sciences-pre-professional |
| 10 | Kinesiology | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUKINBS/kinesiology |
| 11 | Medical Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHMEDBS/medical-studies |
| 12 | Nutrition | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHNTRBS/nutrition |
| 13 | Nutrition (Dietetics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ECNTRDBS/nutrition-dietetics |
| 14 | Nutritional Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHNUSCIBS/nutritional-science |
| 15 | Population Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHPOPHLBS/population-health |
| 16 | Public Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHPBHBS/public-health |
| 17 | Speech and Hearing Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASHSBS/speech-and-hearing-science |
| 18 | Sports Science and Performance Programming | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHSPTSPPBS/sports-science-and-performance-programming |
| 19 | Sports Science and Performance Programming (Strength and Conditioning) | https://degrees.apps.asu.edu/bachelors/major/ASU00/NHSSPPSCBS/sports-science-and-performance-programming-strength-and-conditioning |

#### College of Integrative Sciences and Arts
##### AA
| # | 专业 | URL |
|---|------|-----|
| 1 | Military Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSMILSTAA/military-studies |
| 2 | Organizational Leadership | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSORGLAA/organizational-leadership |
| 3 | Professional Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSPRFSTAA/professional-studies |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Military and Veterans Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSAMVSBA/applied-military-and-veterans-studies |
| 2 | Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSCOMBA/communication |
| 3 | English | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSENGBA/english |
| 4 | General Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSGNSBGS/general-studies |
| 5 | History | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSHISBA/history |
| 6 | History (Military and Veterans Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSHISVSSBA/history-military-and-veterans-studies |
| 7 | History of Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSHSIIBA/history-of-science-technology-and-innovation |
| 8 | Interdisciplinary Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSBISBIS/interdisciplinary-studies |
| 9 | Interdisciplinary Studies (Organizational Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSORGBIS/interdisciplinary-studies-organizational-studies |
| 10 | Liberal Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABLSBLS/liberal-studies |
| 11 | Organizational Leadership | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSORGLBA/organizational-leadership |
| 12 | Organizational Leadership (Military and Veterans Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSORGLVSBA/organizational-leadership-military-and-veterans-studies |
| 13 | Organizational Leadership (Project Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSORGLPMBA/organizational-leadership-project-management |
| 14 | Psychology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSPGSBA/psychology |

##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Animal Biology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSANBIOBAS/applied-science-animal-biology |
| 2 | Applied Science (Applied Leadership) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSALSBAS/applied-science-applied-leadership |
| 3 | Applied Science (Project Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSAPSPMBAS/applied-science-project-management |
| 4 | Applied Science (Technical Communication) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSTECBAS/applied-science-technical-communication |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Biological Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSABSABS/applied-biological-sciences |
| 2 | Applied Biological Sciences (Natural Resource Ecology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSABSNRBS/applied-biological-sciences-natural-resource-ecology |
| 3 | Applied Biological Sciences (Pre-Dental) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSABSPDBS/applied-biological-sciences-pre-dental |
| 4 | Applied Biological Sciences (Preveterinary Medicine) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSABSPMBS/applied-biological-sciences-preveterinary-medicine |
| 5 | Applied Biological Sciences (Secondary Education in Biology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSABSSBS/applied-biological-sciences-secondary-education-in-biology |
| 6 | Applied Biological Sciences (Sustainable Horticulture) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSABSUBS/applied-biological-sciences-sustainable-horticulture |
| 7 | Applied Mathematics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSMATBS/applied-mathematics |
| 8 | Applied Physics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSAPHYBS/applied-physics |
| 9 | Applied Quantitative Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSAQSBS/applied-quantitative-science |
| 10 | Counseling and Applied Psychological Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSCAPSBS/counseling-and-applied-psychological-science |
| 11 | Counseling and Applied Psychological Science (Counseling Military Members and Veterans) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSCAPSMVBS/counseling-and-applied-psychological-science-counseling-military-members-and-veterans |
| 12 | Counseling and Applied Psychological Science (Sexuality and Gender Issues in Counseling) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSCAPSSGBS/counseling-and-applied-psychological-science-sexuality-and-gender-issues-in-counseling |
| 13 | Counseling and Applied Psychological Science (Sport and Performance Counseling) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSCAPSSPBS/counseling-and-applied-psychological-science-sport-and-performance-counseling |
| 14 | Counseling and Applied Psychological Science (Substance Abuse and Addictions) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSCAPSAABS/counseling-and-applied-psychological-science-substance-abuse-and-addictions |
| 15 | Integrative Social Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSISSBS/integrative-social-science |
| 16 | Political Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSPOLBS/political-science |
| 17 | Project Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSPMGBS/project-management |
| 18 | Psychology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSPGSBS/psychology |
| 19 | Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ECSTSBS/science-technology-and-society |
| 20 | Technical Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSTECBS/technical-communication |
| 21 | Technical Communication (Data Visualization) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSTECDVBS/technical-communication-data-visualization |
| 22 | Technical Communication (Medical and Health) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSTECMHBS/technical-communication-medical-and-health |
| 23 | Technical Communication (Social Media Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSTECSMMBS/technical-communication-social-media-management |
| 24 | Technical Communication (User Experience) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSTECUBS/technical-communication-user-experience |

#### College of Integrative Sciences and Arts Ira A. Fulton Schools of Engineering
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | User Experience | https://degrees.apps.asu.edu/bachelors/major/ASU00/LSUSEXBS/user-experience |

#### Edson College of Nursing and Health Innovation
##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Health Entrepreneurship and Innovation) | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHCIBAS/applied-science-health-entrepreneurship-and-innovation |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUCHLTBS/community-health |
| 2 | Health Care Compliance and Regulations | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHCCRBS/health-care-compliance-and-regulations |
| 3 | Health Care Coordination | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHCCOBS/health-care-coordination |
| 4 | Health Entrepreneurship and Innovation | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUHCIBS/health-entrepreneurship-and-innovation |
| 5 | Integrative Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUIHLTBS/integrative-health |

##### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://degrees.apps.asu.edu/bachelors/major/ASU00/NUNURDBSN/nursing |

#### Herberger Institute for Design and the Arts
##### AA
| # | 专业 | URL |
|---|------|-----|
| 1 | Apparel Technical Design | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIATDAA/apparel-technical-design |
| 2 | Fashion Styling | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFSHAA/fashion-styling |
| 3 | Merchandising | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIMERCHAA/merchandising |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art (Art History) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTHBA/art-art-history |
| 2 | Art (Art Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTSTDBA/art-art-studies |
| 3 | Art (Museum and Curatorial Practices) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTMSBA/art-museum-and-curatorial-practices |
| 4 | Arts (BA in the Arts) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAATSBA/arts-ba-in-the-arts |
| 5 | Fashion | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFSHBA/fashion |
| 6 | Fashion (Apparel Product Development) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFSHAPDBA/fashion-apparel-product-development |
| 7 | Fashion (Apparel Technical Design) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFSHATDBA/fashion-apparel-technical-design |
| 8 | Fashion (Design) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFSHDBA/fashion-design |
| 9 | Fashion (Merchandising) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFSHMBA/fashion-merchandising |
| 10 | Film (Film and Media Production) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAFLMBA/film-film-and-media-production |
| 11 | Film (Filmmaking Practices) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAFPRBA/film-filmmaking-practices |
| 12 | Media Arts and Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCBA/media-arts-and-sciences |
| 13 | Media Arts and Sciences (Art) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCABA/media-arts-and-sciences-art |
| 14 | Media Arts and Sciences (Design) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCDBA/media-arts-and-sciences-design |
| 15 | Media Arts and Sciences (Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIMASEDBA/media-arts-and-sciences-education |
| 16 | Media Arts and Sciences (English) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCENBA/media-arts-and-sciences-english |
| 17 | Media Arts and Sciences (Film) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCFBA/media-arts-and-sciences-film |
| 18 | Media Arts and Sciences (Graphic Information Technology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCTEBA/media-arts-and-sciences-graphic-information-technology |
| 19 | Media Arts and Sciences (Interdisciplinary Arts and Performance) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDCIAPBA/media-arts-and-sciences-interdisciplinary-arts-and-performance |
| 20 | Media Arts and Sciences (Music) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCMBA/media-arts-and-sciences-music |
| 21 | Media Arts and Sciences (Theatre) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCTBA/media-arts-and-sciences-theatre |
| 22 | Music | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSBA/music |
| 23 | Music (Music and Culture) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIMUSMCBA/music-music-and-culture |
| 24 | Music (Popular Music) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIMUSPMBA/music-popular-music |
| 25 | Performance and Movement | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIPERMVBA/performance-and-movement |
| 26 | Theatre | https://degrees.apps.asu.edu/bachelors/major/ASU00/FATHEBA/theatre |
| 27 | Theatre (Acting) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FATHEABA/theatre-acting |
| 28 | Theatre (Design and Production) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FADSNPRBA/theatre-design-and-production |

##### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art (Animation) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIARTANBFA/art-animation |
| 2 | Art (Art Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTEBFA/art-art-education |
| 3 | Art (Art Therapy) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIARTATBFA/art-art-therapy |
| 4 | Art (Ceramics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTCBFA/art-ceramics |
| 5 | Art (Craft and Sculptural Practices) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTSBFA/art-craft-and-sculptural-practices |
| 6 | Art (Digital Photography) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIARTDPBFA/art-digital-photography |
| 7 | Art (Drawing) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTDBFA/art-drawing |
| 8 | Art (Expanded Arts) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTIBFA/art-expanded-arts |
| 9 | Art (Painting | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIARTPDBFA/art-painting-drawing-and-printmaking |
| 10 | Art (Painting) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTPABFA/art-painting |
| 11 | Art (Photography) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTPHBFA/art-photography |
| 12 | Art (Printmaking) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTPMBFA/art-printmaking |
| 13 | Art (Textiles) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAARTFBFA/art-textiles |
| 14 | Costume Design and Technology for the Creative Industries | https://degrees.apps.asu.edu/bachelors/major/ASU00/HICOSBFA/costume-design-and-technology-for-the-creative-industries |
| 15 | Dance | https://degrees.apps.asu.edu/bachelors/major/ASU00/FADANBFA/dance |
| 16 | Dance (Dance Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FADANEBFA/dance-dance-education |
| 17 | Film and Media Production | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFMPBFA/film-and-media-production |
| 18 | Film and Media Production (Cinematography) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFMPCBFA/film-and-media-production-cinematography |
| 19 | Film and Media Production (Directing) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFMPDBFA/film-and-media-production-directing |
| 20 | Film and Media Production (Post-Production) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFMPPBFA/film-and-media-production-post-production |
| 21 | Film and Media Production (Screenwriting) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIFMPSBFA/film-and-media-production-screenwriting |

##### BMUS
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Learning and Teaching | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSEBM/music-learning-and-teaching |
| 2 | Music Therapy | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSTHBM/music-therapy |
| 3 | Performance (Collaborative Piano) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPPBM/performance-collaborative-piano |
| 4 | Performance (Guitar) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPGBM/performance-guitar |
| 5 | Performance (Jazz) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPJBM/performance-jazz |
| 6 | Performance (Keyboard) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPKBM/performance-keyboard |
| 7 | Performance (Music Theatre) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPMBM/performance-music-theatre |
| 8 | Performance (Orchestral Instrument) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPOBM/performance-orchestral-instrument |
| 9 | Performance (Voice) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSPVBM/performance-voice |
| 10 | Theory and Composition (Composition) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSTCBM/theory-and-composition-composition |
| 11 | Theory and Composition (Theory) | https://degrees.apps.asu.edu/bachelors/major/ASU00/FAMUSTTBM/theory-and-composition-theory |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Design | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIEDSBS/environmental-design |
| 2 | Game Design | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIGMDESBS/game-design |
| 3 | Game Studio Production | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIGSPBS/game-studio-production |
| 4 | Media Arts and Sciences (Games and Interactive Media) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIMASGIMBS/media-arts-and-sciences-games-and-interactive-media |
| 5 | Media Arts and Sciences (Media Processing) | https://degrees.apps.asu.edu/bachelors/major/ASU00/HIDGCMPBS/media-arts-and-sciences-media-processing |

##### BSD
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/ARSTDBSD/architectural-studies |
| 2 | Graphic Design | https://degrees.apps.asu.edu/bachelors/major/ASU00/ARGRABSD/graphic-design |
| 3 | Industrial Design | https://degrees.apps.asu.edu/bachelors/major/ASU00/ARINDBSD/industrial-design |
| 4 | Interior Design | https://degrees.apps.asu.edu/bachelors/major/ASU00/ARINTBSD/interior-design |

##### BSLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://degrees.apps.asu.edu/bachelors/major/ASU00/ARPLABSLA/landscape-architecture |

#### Ira A. Fulton Schools of Engineering
##### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science and Artificial Intelligence | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEAIAS/computer-science-and-artificial-intelligence |

##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Aviation) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSAMTABAS/applied-science-aviation |
| 2 | Applied Science (Graphic Information Technology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSGITBAS/applied-science-graphic-information-technology |
| 3 | Applied Science (Internet and Web Development) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSIWDBAS/applied-science-internet-and-web-development |
| 4 | Applied Science (Operations Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSIMCOBAS/applied-science-operations-management |
| 5 | Manufacturing Systems | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESMFGSYBAS/manufacturing-systems |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aeronautical Management Technology (Air Traffic Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESAMTATBS/aeronautical-management-technology-air-traffic-management |
| 2 | Aeronautical Management Technology (Air Transportation Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSAMTMBS/aeronautical-management-technology-air-transportation-management |
| 3 | Aeronautical Management Technology (Professional Flight) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSAMTFBS/aeronautical-management-technology-professional-flight |
| 4 | Aeronautical Management Technology (Unmanned Aerial Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSAMTUASBS/aeronautical-management-technology-unmanned-aerial-systems |
| 5 | Computer Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEBS/computer-science |
| 6 | Computer Science (Artificial Intelligence) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEAIBS/computer-science-artificial-intelligence |
| 7 | Computer Science (Cybersecurity) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEIBS/computer-science-cybersecurity |
| 8 | Computer Science (Software Engineering) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSESBS/computer-science-software-engineering |
| 9 | Construction Management and Technology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCONMGTBS/construction-management-and-technology |
| 10 | Engineering Science (Business) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESESCBUSBS/engineering-science-business |
| 11 | Engineering Science (Microelectronics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESESCMEBS/engineering-science-microelectronics |
| 12 | Environmental and Resource Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSETMBS/environmental-and-resource-management |
| 13 | Graphic Information Technology | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSGITBS/graphic-information-technology |
| 14 | Graphic Information Technology (Full-Stack Web Development) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESGITFSWBS/graphic-information-technology-full-stack-web-development |
| 15 | Graphic Information Technology (User Experience) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESGITUEBS/graphic-information-technology-user-experience |
| 16 | Human Systems Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESHSEBS/human-systems-engineering |
| 17 | Human Systems Engineering (User Experience) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESHSEUEBS/human-systems-engineering-user-experience |
| 18 | Informatics | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCPIBS/informatics |
| 19 | Information Technology | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSIFTBS/information-technology |
| 20 | Information Technology (Cybersecurity) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESIFTCSBS/information-technology-cybersecurity |
| 21 | Information Technology (Networking) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESIFTNBS/information-technology-networking |
| 22 | Manufacturing Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSMEGRBS/manufacturing-engineering |
| 23 | Robotics and Autonomous Systems | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESRASBS/robotics-and-autonomous-systems |
| 24 | Software Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSSERBS/software-engineering |
| 25 | Technological Entrepreneurship and Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSTEMBS/technological-entrepreneurship-and-management |

##### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (Aeronautics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESAEROBSE/aerospace-engineering-aeronautics |
| 2 | Aerospace Engineering (Astronautics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESAEASBSE/aerospace-engineering-astronautics |
| 3 | Aerospace Engineering (Autonomous Vehicle Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESAEAVSBSE/aerospace-engineering-autonomous-vehicle-systems |
| 4 | Biomedical Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESBMEBSE/biomedical-engineering |
| 5 | Biomedical Engineering (Biological Devices) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESBMEBDBSE/biomedical-engineering-biological-devices |
| 6 | Biomedical Engineering (Biomedical Devices) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESBMEMDBSE/biomedical-engineering-biomedical-devices |
| 7 | Chemical Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCHEBSE/chemical-engineering |
| 8 | Civil Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCEEBSE/civil-engineering |
| 9 | Civil Engineering (Sustainable Engineering) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCEESUBSE/civil-engineering-sustainable-engineering |
| 10 | Computer Systems Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEBSE/computer-systems-engineering |
| 11 | Computer Systems Engineering (Cybersecurity) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEIBSE/computer-systems-engineering-cybersecurity |
| 12 | Construction Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCONBSE/construction-engineering |
| 13 | Electrical Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESEEEBSE/electrical-engineering |
| 14 | Electrical Engineering (Electric Power and Energy Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESEEEPBSE/electrical-engineering-electric-power-and-energy-systems |
| 15 | Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSEGRBSE/engineering |
| 16 | Engineering (Automotive Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSEGRASBSE/engineering-automotive-systems |
| 17 | Engineering (Clean Energy Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESEGRCEBSE/engineering-clean-energy-systems |
| 18 | Engineering (Electrical Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSEGRESBSE/engineering-electrical-systems |
| 19 | Engineering (Mechanical Engineering Systems) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSEGRMEBSE/engineering-mechanical-engineering-systems |
| 20 | Engineering (Robotics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TSEGRRBSE/engineering-robotics |
| 21 | Engineering Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESEMGBSE/engineering-management |
| 22 | Environmental Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESEVEBSE/environmental-engineering |
| 23 | Industrial Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESIEEBSE/industrial-engineering |
| 24 | Materials Science and Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESMSEBSE/materials-science-and-engineering |
| 25 | Mechanical Engineering | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESMAEMBSE/mechanical-engineering |
| 26 | Mechanical Engineering (Computational Mechanics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESMAECBSE/mechanical-engineering-computational-mechanics |
| 27 | Mechanical Engineering (Energy and Environment) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESMAEEBSE/mechanical-engineering-energy-and-environment |
| 28 | Robotics and Autonomous Systems | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESRASBSE/robotics-and-autonomous-systems |

#### Ira A. Fulton Schools of Engineering New College of Interdisciplinary Arts and Sciences
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEBA/computer-science |
| 2 | Computer Science (Cybersecurity) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ESCSEIBA/computer-science-cybersecurity |

#### Mary Lou Fulton College for Teaching and Learning Innovation
##### BAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEECDEDBAE/early-childhood-education |
| 2 | Educational Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/EDSLSTBAE/educational-studies |
| 3 | Educational Studies (Early Childhood Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEESECEBAE/educational-studies-early-childhood-studies |
| 4 | Educational Studies (Instructional Design) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEEDUSTBAE/educational-studies-instructional-design |
| 5 | Elementary Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEEEDBAE/elementary-education |
| 6 | Elementary Multilingual Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEEMLEBAE/elementary-multilingual-education |
| 7 | Middle Grades Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEMGEBAE/middle-grades-education |
| 8 | Physical Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEPPEBAE/physical-education |
| 9 | Secondary Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TESEDBAE/secondary-education |
| 10 | Secondary Education (Biological Sciences) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEBIOBAE/secondary-education-biological-sciences |
| 11 | Secondary Education (Earth and Space Sciences) | https://degrees.apps.asu.edu/bachelors/major/ASU00/EDESSBAE/secondary-education-earth-and-space-sciences |
| 12 | Secondary Education (English) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEENGBAE/secondary-education-english |
| 13 | Secondary Education (History) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEHISBAE/secondary-education-history |
| 14 | Secondary Education (Mathematics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEMATBAE/secondary-education-mathematics |
| 15 | Special Education | https://degrees.apps.asu.edu/bachelors/major/ASU00/TESPCEDBAE/special-education |

##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Early Childhood Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEAPSECBAS/applied-science-early-childhood-studies |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Behavior Analysis | https://degrees.apps.asu.edu/bachelors/major/ASU00/TEBEHANBS/behavior-analysis |

#### New College of Interdisciplinary Arts and Sciences
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASLSCBA/biology |
| 2 | Biology (Environmental Justice) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASLSCEJBA/biology-environmental-justice |
| 3 | Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASCOMMBA/communication |
| 4 | Conflict Resolution | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASCNRBA/conflict-resolution |
| 5 | Disability Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASDISASBA/disability-studies |
| 6 | English | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASENGBA/english |
| 7 | English (Secondary Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASENGSEBA/english-secondary-education |
| 8 | Environmental Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASENVBA/environmental-studies |
| 9 | Environmental Studies (Environmental Justice) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASENVEJBA/environmental-studies-environmental-justice |
| 10 | History | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASHISBA/history |
| 11 | History (Secondary Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASHISSEBA/history-secondary-education |
| 12 | Interdisciplinary Arts and Performance | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASIAPBA/interdisciplinary-arts-and-performance |
| 13 | Interdisciplinary Arts and Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASIASBA/interdisciplinary-arts-and-sciences |
| 14 | Philosophy | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASRELBA/philosophy-religion-and-society |
| 15 | Political Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPOLBA/political-science |
| 16 | Psychology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSBA/psychology |
| 17 | Psychology (Forensic Psychology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSFPBA/psychology-forensic-psychology |
| 18 | Psychology (Industrial and Organizational Psychology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSIOPBA/psychology-industrial-and-organizational-psychology |
| 19 | Psychology (Positive Psychology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSPPBA/psychology-positive-psychology |
| 20 | Social Justice and Human Rights | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASJHRBA/social-justice-and-human-rights |
| 21 | Social and Behavioral Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSBSBA/social-and-behavioral-sciences |
| 22 | Social and Cultural Analysis (American Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSCAASBA/social-and-cultural-analysis-american-studies |
| 23 | Social and Cultural Analysis (Ethnicity | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSCAERBA/social-and-cultural-analysis-ethnicity-race-and-indigenous-studies |
| 24 | Social and Cultural Analysis (Latin American Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSCALABA/social-and-cultural-analysis-latin-american-studies |
| 25 | Social and Cultural Analysis (Peace Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSCAPSBA/social-and-cultural-analysis-peace-studies |
| 26 | Social and Cultural Analysis (Queer and Sexuality Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSCAQSBA/social-and-cultural-analysis-queer-and-sexuality-studies |
| 27 | Social and Cultural Analysis (Women and Gender Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSCAWSBA/social-and-cultural-analysis-women-and-gender-studies |
| 28 | Sociology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSOCBA/sociology |
| 29 | Spanish | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSPABA/spanish |

##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASBASBAS/applied-science |
| 2 | Applied Science (Biotechnology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASBASBTBAS/applied-science-biotechnology |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aging | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASALDBS/aging |
| 2 | Applied Computing | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASACOBS/applied-computing |
| 3 | Applied Computing (Cybersecurity) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASACOCBS/applied-computing-cybersecurity |
| 4 | Applied Mathematics | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASMATBS/applied-mathematics |
| 5 | Biology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASLSCBS/biology |
| 6 | Biology (Environmental Justice) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASLSCEJBS/biology-environmental-justice |
| 7 | Biology (Pharmacology/Toxicology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASLSCPBS/biology-pharmacology-toxicology |
| 8 | Biotechnology and Bioenterprise | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASBITEBS/biotechnology-and-bioenterprise |
| 9 | Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASCOMMBS/communication |
| 10 | Digital Forensics | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASCPFBS/digital-forensics |
| 11 | Environmental Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASENVBS/environmental-science |
| 12 | Environmental Science (Environmental Justice) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASENVEJBS/environmental-science-environmental-justice |
| 13 | Forensic Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASFOREBS/forensic-science |
| 14 | Forensic Science (Death Investigations) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASFOREDIBS/forensic-science-death-investigations |
| 15 | Gender | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASWSTBS/gender-women-and-sexuality-studies |
| 16 | Pharmacology and Toxicology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPTXBS/pharmacology-and-toxicology |
| 17 | Pharmacology and Toxicology (Environmental Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPTXEJBS/pharmacology-and-toxicology-environmental-studies |
| 18 | Political Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPOLBS/political-science |
| 19 | Psychology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSBS/psychology |
| 20 | Psychology (Forensic Psychology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSFPBS/psychology-forensic-psychology |
| 21 | Psychology (Industrial and Organizational Psychology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSIOPBS/psychology-industrial-and-organizational-psychology |
| 22 | Psychology (Positive Psychology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASPGSPPBS/psychology-positive-psychology |
| 23 | Social and Behavioral Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSBSBS/social-and-behavioral-sciences |
| 24 | Sociology | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSOCBS/sociology |
| 25 | Statistics | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASSTABS/statistics |

#### Rob Walton College of Global Futures
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Innovation in Society | https://degrees.apps.asu.edu/bachelors/major/ASU00/FIFISBA/innovation-in-society |
| 2 | Sustainability | https://degrees.apps.asu.edu/bachelors/major/ASU00/SUSUSTBA/sustainability |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Complexity Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAAMLBS/complexity-science |
| 2 | Innovation in Society | https://degrees.apps.asu.edu/bachelors/major/ASU00/FIFISBS/innovation-in-society |
| 3 | Ocean Futures | https://degrees.apps.asu.edu/bachelors/major/ASU00/GFSEABS/ocean-futures |
| 4 | Ocean Futures (Coastal and Marine Science) | https://degrees.apps.asu.edu/bachelors/major/ASU00/GFSEACMSBS/ocean-futures-coastal-and-marine-science |
| 5 | Sustainability | https://degrees.apps.asu.edu/bachelors/major/ASU00/SUSUSTBS/sustainability |
| 6 | Sustainable Food Systems | https://degrees.apps.asu.edu/bachelors/major/ASU00/SUSFOSYSBS/sustainable-food-systems |

#### The College of Liberal Arts and Sciences
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African and African American Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAAFRBA/african-and-african-american-studies |
| 2 | American Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAAMRSTBA/american-studies |
| 3 | Anthropology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAASBBA/anthropology |
| 4 | Asia Studies (East Asia) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAHSTEABA/asia-studies-east-asia |
| 5 | Asia Studies (South Asia) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAHSTSABA/asia-studies-south-asia |
| 6 | Asian Languages (Chinese) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACHIBA/asian-languages-chinese |
| 7 | Asian Languages (Japanese) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAJPNBA/asian-languages-japanese |
| 8 | Asian Pacific American Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAAPABA/asian-pacific-american-studies |
| 9 | Biochemistry | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABCHBA/biochemistry |
| 10 | Chemistry | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACHMBA/chemistry |
| 11 | Civic and Economic Thought and Leadership | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACELBA/civic-and-economic-thought-and-leadership |
| 12 | Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACOMBA/communication |
| 13 | Culture | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACTEBA/culture-technology-and-environment |
| 14 | Earth and Environmental Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAEESBA/earth-and-environmental-sciences |
| 15 | English | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGBA/english |
| 16 | English (Creative Writing) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGCBA/english-creative-writing |
| 17 | English (Linguistics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGNBA/english-linguistics |
| 18 | English (Literature) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGTBA/english-literature |
| 19 | English (Narrative Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGNSBA/english-narrative-studies |
| 20 | English (Secondary Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGSEBA/english-secondary-education |
| 21 | English (Writing | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAENGWBA/english-writing-rhetorics-and-literacies |
| 22 | Film (Film and Media Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAFMSBA/film-film-and-media-studies |
| 23 | French | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAFREBA/french |
| 24 | Gender | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAWSTBA/gender-women-and-sexuality-studies |
| 25 | Geography | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAGCUBA/geography |
| 26 | German | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAGERBA/german |
| 27 | Global Asia Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAASIABA/global-asia-studies |
| 28 | Global Citizenship | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAGCZBA/global-citizenship |
| 29 | Global Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASSHBA/global-health |
| 30 | Global Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASGSBA/global-studies |
| 31 | History | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAHISBA/history |
| 32 | History (Secondary Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAHISSEBA/history-secondary-education |
| 33 | Integrated Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAISTBA/integrated-studies |
| 34 | International Letters and Cultures | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASLCBA/international-letters-and-cultures |
| 35 | International Letters and Cultures (Arabic Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASLCASBA/international-letters-and-cultures-arabic-studies |
| 36 | International Letters and Cultures (Classical Civilization) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASLCVBA/international-letters-and-cultures-classical-civilization |
| 37 | International Letters and Cultures (Classics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASLCCBA/international-letters-and-cultures-classics |
| 38 | International Relations | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAINRBA/international-relations |
| 39 | Italian | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAITABA/italian |
| 40 | Jewish Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAJSTBA/jewish-studies |
| 41 | Justice Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAJUSBA/justice-studies |
| 42 | Latin American Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/ASLASBA/latin-american-studies |
| 43 | Mathematics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMATBA/mathematics |
| 44 | Philosophy | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPHIBA/philosophy |
| 45 | Philosophy (Morality | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPHIMPBA/philosophy-morality-politics-and-law |
| 46 | Philosophy (Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPHISNMBA/philosophy-science-nature-and-mind |
| 47 | Physics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPHYBA/physics |
| 48 | Political Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPOSBA/political-science |
| 49 | Psychology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPGSBA/psychology |
| 50 | Religious Studies (Religion | https://degrees.apps.asu.edu/bachelors/major/ASU00/LARELCPBA/religious-studies-religion-culture-and-public-life |
| 51 | Religious Studies (Religion | https://degrees.apps.asu.edu/bachelors/major/ASU00/LARELPGBA/religious-studies-religion-politics-and-global-affairs |
| 52 | Russian | https://degrees.apps.asu.edu/bachelors/major/ASU00/LARUSBA/russian |
| 53 | Spanish | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASPABA/spanish |
| 54 | Transborder Chicana/o and Latina/o Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LATCLBA/transborder-chicana-o-and-latina-o-studies |
| 55 | Transborder Chicana/o and Latina/o Studies (US and Mexican Regional Immigration Policy and Economy) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LATCLUBA/transborder-chicana-o-and-latina-o-studies-us-and-mexican-regional-immigration-policy-and-economy |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAACTBS/actuarial-science |
| 2 | American Indian Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAAISBS/american-indian-studies |
| 3 | Anthropology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAASBBS/anthropology |
| 4 | Astronomical and Planetary Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAASTPLSBS/astronomical-and-planetary-sciences |
| 5 | Astronomical and Planetary Sciences (Astrophysics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAASTPLABS/astronomical-and-planetary-sciences-astrophysics |
| 6 | Biochemistry | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABCHBS/biochemistry |
| 7 | Biochemistry (Medicinal Chemistry) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABCHMBS/biochemistry-medicinal-chemistry |
| 8 | Biological Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABSCBS/biological-sciences |
| 9 | Biological Sciences (Biology and Society) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABSCSBS/biological-sciences-biology-and-society |
| 10 | Biological Sciences (Biomedical Sciences) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABSCMBS/biological-sciences-biomedical-sciences |
| 11 | Biological Sciences (Conservation Biology and Ecology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABSCCBS/biological-sciences-conservation-biology-and-ecology |
| 12 | Biological Sciences (Genetics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABSCGBS/biological-sciences-genetics-cell-and-developmental-biology |
| 13 | Biological Sciences (Neurobiology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABSCABS/biological-sciences-neurobiology-physiology-and-behavior |
| 14 | Biophysics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABIPHBS/biophysics |
| 15 | Chemistry | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACHMBS/chemistry |
| 16 | Chemistry (Environmental Chemistry) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACHMEBS/chemistry-environmental-chemistry |
| 17 | Civic and Economic Thought and Leadership | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACETLBS/civic-and-economic-thought-and-leadership |
| 18 | Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACOMBS/communication |
| 19 | Computational Mathematical Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/LACMSBS/computational-mathematical-sciences |
| 20 | Data Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LADATSCIBS/data-science |
| 21 | Earth and Environmental Sciences | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAEESBS/earth-and-environmental-sciences |
| 22 | Earth and Space Exploration | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASESBS/earth-and-space-exploration |
| 23 | Earth and Space Exploration (Astrobiology and Biogeosciences) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASESABBS/earth-and-space-exploration-astrobiology-and-biogeosciences |
| 24 | Earth and Space Exploration (Astrophysics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASESABS/earth-and-space-exploration-astrophysics |
| 25 | Earth and Space Exploration (Exploration Systems Design) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASESESDBS/earth-and-space-exploration-exploration-systems-design |
| 26 | Earth and Space Exploration (Geological and Planetary Sciences) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASESGSBS/earth-and-space-exploration-geological-and-planetary-sciences |
| 27 | Economics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAECNBS/economics |
| 28 | Economics (Politics and the Economy) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAECNPECBS/economics-politics-and-the-economy |
| 29 | Family and Human Development | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAFASBS/family-and-human-development |
| 30 | Geographic Information Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAGISBS/geographic-information-science |
| 31 | Geography | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAGCUBS/geography |
| 32 | Geography (Meteorology-Climatology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAGCUMBS/geography-meteorology-climatology |
| 33 | Global Health | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASSHBS/global-health |
| 34 | Integrated Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAISTBS/integrated-studies |
| 35 | International Relations | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAINRBS/international-relations |
| 36 | Justice Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAJUSBS/justice-studies |
| 37 | Mathematics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMATBS/mathematics |
| 38 | Mathematics (Secondary Education) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMATSBS/mathematics-secondary-education |
| 39 | Mathematics (Statistics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMATTBS/mathematics-statistics |
| 40 | Microbiology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMICBS/microbiology |
| 41 | Microbiology (Medical Microbiology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMICMBS/microbiology-medical-microbiology |
| 42 | Molecular Biosciences and Biotechnology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAMBBBS/molecular-biosciences-and-biotechnology |
| 43 | Neuroscience | https://degrees.apps.asu.edu/bachelors/major/ASU00/LABMENBS/neuroscience |
| 44 | Physics | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPHYBS/physics |
| 45 | Political Science | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPOSBS/political-science |
| 46 | Politics and the Economy | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPECBS/politics-and-the-economy |
| 47 | Psychology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPGSBS/psychology |
| 48 | Psychology (Psychological Science) | https://degrees.apps.asu.edu/bachelors/major/ASU00/LAPGSPSBS/psychology-psychological-science |
| 49 | Sociology | https://degrees.apps.asu.edu/bachelors/major/ASU00/LASOCBS/sociology |
| 50 | Technological Leadership | https://degrees.apps.asu.edu/bachelors/major/ASU00/LATECLDRBS/technological-leadership |

##### BSP
| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Planning | https://degrees.apps.asu.edu/bachelors/major/ASU00/ARPUPBSP/urban-planning |

#### Thunderbird School of Global Management
##### BGM
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/TBTGMBGM/global-management |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | International Trade | https://degrees.apps.asu.edu/bachelors/major/ASU00/TBINTRABS/international-trade |

#### University College
#### W. P. Carey School of Business
##### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Logistics (Maritime) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BALGMARAS/logistics-maritime |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Business and Technology Solutions | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAAPBTSBA/applied-business-and-technology-solutions |
| 2 | Business | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSBA/business |
| 3 | Business (Accounting and Business Decisions) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSCABA/business-accounting-and-business-decisions |
| 4 | Business (Agribusiness Innovation and Technology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSGAGBA/business-agribusiness-innovation-and-technology |
| 5 | Business (Applied Supply Chains) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSGLBA/business-applied-supply-chains |
| 6 | Business (Business Administration) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSBABA/business-business-administration |
| 7 | Business (Communication) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSCBA/business-communication |
| 8 | Business (Financial Planning) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSFPBA/business-financial-planning |
| 9 | Business (Food Industry Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSFIMBA/business-food-industry-management |
| 10 | Business (Global Leadership) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSGBA/business-global-leadership |
| 11 | Business (Global Politics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSGPBA/business-global-politics |
| 12 | Business (Health Care) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSHCBA/business-health-care |
| 13 | Business (Human Resources) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSHRBA/business-human-resources |
| 14 | Business (Information Security) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSISBA/business-information-security |
| 15 | Business (Language and Culture) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABSLACUBA/business-language-and-culture |
| 16 | Business (Law) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSLBA/business-law |
| 17 | Business (Public Service and Public Policy) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSPBA/business-public-service-and-public-policy |
| 18 | Business (Retail Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSRBA/business-retail-management |
| 19 | Business (Sports Business) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSMSBA/business-sports-business |
| 20 | Business (Statistics) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSTABA/business-statistics |
| 21 | Business (Sustainability) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSSBA/business-sustainability |
| 22 | Business (Technology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSTCBA/business-technology |
| 23 | Business (Tourism) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUSTBA/business-tourism |
| 24 | Entrepreneurial Leadership | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAENTLBA/entrepreneurial-leadership |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAACCBS/accountancy |
| 2 | Artificial Intelligence in Business | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAAIBBS/artificial-intelligence-in-business |
| 3 | Business Data Analytics | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABDABS/business-data-analytics |
| 4 | Business Entrepreneurship | https://degrees.apps.asu.edu/bachelors/major/ASU00/BABUENTBS/business-entrepreneurship |
| 5 | Computer Information Systems | https://degrees.apps.asu.edu/bachelors/major/ASU00/BACISBS/computer-information-systems |
| 6 | Economics | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAECNBS/economics |
| 7 | Finance | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAFINBS/finance |
| 8 | Financial Technology | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAFINTBS/financial-technology |
| 9 | Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAMGTBS/management |
| 10 | Marketing | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAMKTBS/marketing |
| 11 | Marketing (Digital) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAMKDIMCBS/marketing-digital |
| 12 | Marketing (Professional Sales) | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAMKTPSBS/marketing-professional-sales |
| 13 | Real Estate and Applied Finance | https://degrees.apps.asu.edu/bachelors/major/ASU00/BAREAFBS/real-estate-and-applied-finance |
| 14 | Supply Chain Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/BASCMBS/supply-chain-management |

#### Walter Cronkite School of Journalism and Mass Communication
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Content Creation | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSCCBA/content-creation |
| 2 | Journalism | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSJMCBA/journalism |
| 3 | Mass Communication and Media Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSMCMSTBA/mass-communication-and-media-studies |
| 4 | Media Literacy | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSDMLBA/media-literacy |
| 5 | Science Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSSCOMBA/science-communication |
| 6 | Sports Journalism | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSSPJBA/sports-journalism |
| 7 | Sports Strategic Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSSPSTCOBA/sports-strategic-communication |
| 8 | Strategic Communication | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSSTRCOMBA/strategic-communication |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Strategy and Audience Engagement | https://degrees.apps.asu.edu/bachelors/major/ASU00/CSDIGABS/digital-strategy-and-audience-engagement |

#### Watts College of Public Service & Community Solutions
##### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Emergency Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPEMEAS/emergency-management |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Advocacy and Social Policy | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPCASPBA/community-advocacy-and-social-policy |

##### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science (Emergency Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPEMGBAS/applied-science-emergency-management |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Sports Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPCSMBS/community-sports-management |
| 2 | Community Sports Management (Events) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPCSMEBS/community-sports-management-events |
| 3 | Criminology and Criminal Justice | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPCRIMJBS/criminology-and-criminal-justice |
| 4 | Criminology and Criminal Justice (Community Safety | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPCRJCSLBS/criminology-and-criminal-justice-community-safety-law-and-social-change |
| 5 | Criminology and Criminal Justice (Policing) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPCRJPOLBS/criminology-and-criminal-justice-policing |
| 6 | Emergency Management and Homeland Security | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPEMHSBS/emergency-management-and-homeland-security |
| 7 | Nonprofit Leadership and Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPNLMBS/nonprofit-leadership-and-management |
| 8 | Nonprofit Leadership and Management (American Indian Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPNLMAIBS/nonprofit-leadership-and-management-american-indian-studies |
| 9 | Parks | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPRMBS/parks-recreation-and-sport-management |
| 10 | Public Service and Public Policy | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFBS/public-service-and-public-policy |
| 11 | Public Service and Public Policy (American Indian Studies) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFAISBS/public-service-and-public-policy-american-indian-studies |
| 12 | Public Service and Public Policy (Business) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFBUBS/public-service-and-public-policy-business |
| 13 | Public Service and Public Policy (Criminology) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFCBS/public-service-and-public-policy-criminology |
| 14 | Public Service and Public Policy (Emergency Management and Homeland Security) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFEHBS/public-service-and-public-policy-emergency-management-and-homeland-security |
| 15 | Public Service and Public Policy (Health Policy) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFHPBS/public-service-and-public-policy-health-policy |
| 16 | Public Service and Public Policy (Law and Policy) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFLPBS/public-service-and-public-policy-law-and-policy |
| 17 | Public Service and Public Policy (Nonprofit Leadership and Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPANLMBS/public-service-and-public-policy-nonprofit-leadership-and-management |
| 18 | Public Service and Public Policy (Parks and Recreation Management) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAPRMBS/public-service-and-public-policy-parks-and-recreation-management |
| 19 | Public Service and Public Policy (Social Services Delivery) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFSSBS/public-service-and-public-policy-social-services-delivery |
| 20 | Public Service and Public Policy (Sustainability) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPPAFSBS/public-service-and-public-policy-sustainability |
| 21 | Recreational Therapy | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPRECTBS/recreational-therapy |
| 22 | Sport and Recreation Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPTRMBS/sport-and-recreation-management |
| 23 | Tourism Development and Management | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPTDMBS/tourism-development-and-management |
| 24 | Tourism Development and Management (Meetings and Events) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPTDMMEBS/tourism-development-and-management-meetings-and-events |
| 25 | Tourism Development and Management (Resort and Hotel Leadership) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPTDMRBS/tourism-development-and-management-resort-and-hotel-leadership |
| 26 | Tourism Development and Management (Sustainable Tourism) | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPTDMSBS/tourism-development-and-management-sustainable-tourism |
| 27 | Urban and Metropolitan Studies | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPURBBS/urban-and-metropolitan-studies |

##### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://degrees.apps.asu.edu/bachelors/major/ASU00/PPSWUSWU/social-work |

---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别

#### College of Health Solutions
##### DBH
| # | 项目 | URL |
|---|------|-----|
| 1 | Behavioral Health (Clinical) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHBVHCDBH/behavioral-health-clinical-dbh |
| 2 | Behavioral Health (Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHBVHMDBH/behavioral-health-management-dbh |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Molecular Diagnostics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHCMDGRCT/clinical-molecular-diagnostics-graduate-certificate |
| 2 | Communication Disorders in Multilingual/Multicultural Populations | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHCDMPGRCT/communication-disorders-in-multilingual-multicultural-populations-graduate-certificate |
| 3 | Integrated Behavioral Health - Clinical | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHIBHCGRCT/integrated-behavioral-health---clinical-graduate-certificate |
| 4 | Integrated Behavioral Health - Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHIBHMGRCT/integrated-behavioral-health---management-graduate-certificate |
| 5 | Medical Nutrition | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHMNTRGRCT/medical-nutrition-graduate-certificate |
| 6 | Science of Health Care Delivery | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHHCDGRCT/science-of-health-care-delivery-graduate-certificate |
| 7 | Trauma and Bereavement | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HSCTBGRCT/trauma-and-bereavement-graduate-certificate |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Special Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ECSPEDMED/special-education-med |

##### MIHM
| # | 项目 | URL |
|---|------|-----|
| 1 | International Health Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHIHMIHM/international-health-management-mihm |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Auditory and Language Neuroscience | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHALNEUMS/auditory-and-language-neuroscience-ms |
| 2 | Biomedical Diagnostics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHBMDMS/biomedical-diagnostics-ms |
| 3 | Biostatistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHBSTMS/biostatistics-ms |
| 4 | Clinical Exercise Physiology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHCEPMS/clinical-exercise-physiology-ms |
| 5 | Cytology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHCYTOLMS/cytology-ms |
| 6 | Genetic Counseling | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHGCOMS/genetic-counseling-ms |
| 7 | Health Care Administration and Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHSHCDMS/health-care-administration-and-policy-ms |
| 8 | Human Systems Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ECAPSYCHMS/human-systems-engineering-ms |
| 9 | Medical Nutrition | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHMNTRMS/medical-nutrition-ms |
| 10 | Nutritional Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ECHNUTMS/nutritional-science-ms |
| 11 | Nutritional Science (Dietetics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ECNTRDMS/nutritional-science-dietetics-ms |
| 12 | Population Health | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHPOPHLMS/population-health-ms |
| 13 | Strength and Conditioning | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHSTRCDMS/strength-and-conditioning-ms |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHBSTPHD/biostatistics-phd |
| 2 | Exercise and Nutritional Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ECNUTRIPHD/exercise-and-nutritional-sciences-phd |
| 3 | Population Health | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHPOPHLPHD/population-health-phd |
| 4 | Speech and Hearing Science (Auditory and Language Neuroscience) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHSHSALPHD/speech-and-hearing-science-auditory-and-language-neuroscience-phd |
| 5 | Speech and Hearing Science (Translational Genetics of Communication Abilities) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NHSHSTGPHD/speech-and-hearing-science-translational-genetics-of-communication-abilities-phd |

#### College of Integrative Sciences and Arts
##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Narrative Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSNRSGRCT/narrative-studies-graduate-certificate |
| 2 | Organizational Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSORGLGRCT/organizational-leadership-graduate-certificate |
| 3 | Project Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSPMGGRCT/project-management-graduate-certificate |
| 4 | Strategic Project Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSSPMGRCT/strategic-project-management-graduate-certificate |
| 5 | Technical Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSTECGRCT/technical-communication-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Narrative Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSNRSMA/narrative-studies-ma |

##### MC
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling (School Counseling) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSCOUNSCMC/counseling-school-counseling-mc |

##### MPM
| # | 项目 | URL |
|---|------|-----|
| 1 | Project Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSPMGMPM/project-management-mpm |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Biological Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSAPBIOSMS/applied-biological-sciences-ms |
| 2 | Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSEGRMS/engineering-ms |
| 3 | Global Technology and Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSGTDMS/global-technology-and-development-ms |
| 4 | Information Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSIFTMS/information-technology-ms |
| 5 | Integrative Social Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSISSMS/integrative-social-science-ms |
| 6 | Manufacturing Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSMEGRMS/manufacturing-engineering-ms |
| 7 | Organizational Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSORGLMS/organizational-leadership-ms |
| 8 | Software Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSSERMS/software-engineering-ms |
| 9 | Technical Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LSTCCMMS/technical-communication-ms |

##### MSTech
| # | 项目 | URL |
|---|------|-----|
| 1 | Technology (Aviation Management and Human Factors) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSHFMSTECH/technology-aviation-management-and-human-factors-mstech |
| 2 | Technology (Management of Technology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSMRMSTECH/technology-management-of-technology-mstech |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Systems Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TSSMACSPHD/human-systems-engineering-phd |

#### Edson College of Nursing and Health Innovation
##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Nursing Practice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPDNP/advanced-nursing-practice-dnp |
| 2 | Advanced Nursing Practice (Acute Care Pediatric Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPACDNP/advanced-nursing-practice-acute-care-pediatric-nurse-practitioner-dnp |
| 3 | Advanced Nursing Practice (Adult-Gerontology Acute Care Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPGDNP/advanced-nursing-practice-adult-gerontology-acute-care-nurse-practitioner-dnp |
| 4 | Advanced Nursing Practice (Adult-Gerontology Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPAGDNP/advanced-nursing-practice-adult-gerontology-nurse-practitioner-dnp |
| 5 | Advanced Nursing Practice (Family Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPFNDNP/advanced-nursing-practice-family-nurse-practitioner-dnp |
| 6 | Advanced Nursing Practice (Innovation Leadership) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPILDNP/advanced-nursing-practice-innovation-leadership-dnp |
| 7 | Advanced Nursing Practice (Neonatal Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPNDNP/advanced-nursing-practice-neonatal-nurse-practitioner-dnp |
| 8 | Advanced Nursing Practice (Primary Care Pediatric Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPPDNP/advanced-nursing-practice-primary-care-pediatric-nurse-practitioner-dnp |
| 9 | Advanced Nursing Practice (Psychiatric Mental Health Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPCFDNP/advanced-nursing-practice-psychiatric-mental-health-nurse-practitioner-dnp |
| 10 | Advanced Nursing Practice (Women's Health Nurse Practitioner) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUANPWHDNP/advanced-nursing-practice-women's-health-nurse-practitioner-dnp |

##### DPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Regulatory and Clinical Research Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NURCRMDPP/regulatory-and-clinical-research-management-dpp |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Acute Care Pediatric Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUACPNGRCT/acute-care-pediatric-nurse-practitioner-graduate-certificate |
| 2 | Adult Gerontology Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUAGNPGRCT/adult-gerontology-nurse-practitioner-graduate-certificate |
| 3 | Clinical Research Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUHCRGRCC/clinical-research-management-graduate-certificate |
| 4 | Emergency Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUEMNPGRCT/emergency-nurse-practitioner-graduate-certificate |
| 5 | Family Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUFMPGRCE/family-nurse-practitioner-graduate-certificate |
| 6 | Food Safety and Protection | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUFDSPGRCT/food-safety-and-protection-graduate-certificate |
| 7 | Health Care Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUHCINGRCT/health-care-innovation-graduate-certificate |
| 8 | Health Care Simulation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUHCSGRCT/health-care-simulation-graduate-certificate |
| 9 | Innovation Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUINLSGRCT/innovation-leadership--graduate-certificate |
| 10 | International Health for Healthcare Professionals | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUHCRGRCI/international-health-for-healthcare-professionals-graduate-certificate |
| 11 | Interprofessional Healthy Aging | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUGNCERT/interprofessional-healthy-aging-graduate-certificate |
| 12 | Nurse Education in Academic and Practice Settings | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNURSEDCE/nurse-education-in-academic-and-practice-settings-graduate-certificate |
| 13 | Primary Care Pediatric Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUPDNPGRCT/primary-care-pediatric-nurse-practitioner-graduate-certificate |
| 14 | Psychiatric Mental Health Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUPMNUPRCE/psychiatric-mental-health-nurse-practitioner-graduate-certificate |
| 15 | Women's Health Nurse Practitioner | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUWHNPGRCT/women's-health-nurse-practitioner-graduate-certificate |

##### MHI
| # | 项目 | URL |
|---|------|-----|
| 1 | Healthcare Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUHCINNMHI/healthcare-innovation-mhi |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Research Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUCRMMS/clinical-research-management-ms |
| 2 | Clinical Research Management (Regulatory Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUCRMRSMS/clinical-research-management-regulatory-science-ms |
| 3 | Health Care Simulation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUHCSMS/health-care-simulation-ms |
| 4 | Nursing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNURDTMS/nursing-ms |
| 5 | Nursing (Clinical Research Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNURCRMMS/nursing-clinical-research-management-ms |
| 6 | Nursing (Entry to Nursing Practice) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNRENPRMS/nursing-entry-to-nursing-practice-ms |
| 7 | Nursing (Health Care Innovation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNURHCIMS/nursing-health-care-innovation-ms |
| 8 | Nursing (Nursing Education) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNURSEDMS/nursing-nursing-education-ms |
| 9 | Regulatory Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NURSHSMS/regulatory-science-ms |
| 10 | Regulatory Science (Food Safety) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NURGSCFSMS/regulatory-science-food-safety-ms |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing and Healthcare Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/NUNHIPHD/nursing-and-healthcare-innovation-phd |

#### Graduate College
##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Responsible Innovation in Science, Engineering and Society | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCRSESGRCT/responsible-innovation-in-science-engineering-and-society-graduate-certificate |
| 2 | Statistics and Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCSTATCE/statistics-and-data-science-graduate-certificate |
| 3 | Transdisciplinary Transportation Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCTRANSCE/transdisciplinary-transportation-studies-graduate-certificate |

##### MAS
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCADVSTMAS/advanced-studies-mas |
| 2 | Health Informatics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCHLHINMAS/health-informatics-mas |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCSTATMS/statistics-ms |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCBDSPHD/biological-design-phd |
| 2 | Human and Social Dimensions of Science and Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCHSDSTPHD/human-and-social-dimensions-of-science-and-technology-phd |
| 3 | Neuroscience | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GCBMENPHD/neuroscience-phd |

#### Herberger Institute for Design and the Arts
##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Conducting | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FACONDDMA/conducting-dma |
| 2 | Music (Interdisciplinary Digital Media) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAINTDDMA/music-interdisciplinary-digital-media-dma |
| 3 | Music (Performance) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAPERFDMA/music-performance-dma |
| 4 | Music Composition | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FACOMPDMA/music-composition-dma |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | CLO 3D Virtual Fashion Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HICLOGRCT/clo-3d-virtual-fashion-design-graduate-certificate |
| 2 | Community-Engaged Practices in Design and the Arts | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HISEPGRCT/community-engaged-practices-in-design-and-the-arts-graduate-certificate |
| 3 | Dance Teaching Artist Praxis | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDTAPGRCT/dance-teaching-artist-praxis-graduate-certificate |
| 4 | Music Entrepreneurship | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIMERTGRCT/music-entrepreneurship-graduate-certificate |
| 5 | Music Theory Pedagogy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIMTPGRCT/music-theory-pedagogy-graduate-certificate |
| 6 | The Art of Bespoke Tailoring | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIBTGRCT/the-art-of-bespoke-tailoring-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAARTMA/art-ma |
| 2 | Art (Art Education) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAARTEDMA/art-art-education-ma |
| 3 | Art (Art History) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAARTHISMA/art-art-history-ma |
| 4 | Creative Enterprise and Cultural Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HICECLMA/creative-enterprise-and-cultural-leadership-ma |
| 5 | Digital Culture | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDGCMA/digital-culture-ma |
| 6 | Museum and Curatorial Practices | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIMCPMA/museum-and-curatorial-practices-ma |
| 7 | Music (Ethnomusicology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAETHNMA/music-ethnomusicology-ma |
| 8 | Music (Musicology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMHISTMA/music-musicology-ma |
| 9 | Theatre | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FATHEAMA/theatre-ma |

##### MArch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARARCMARCH/architecture-march |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIARTMFA/art-mfa |
| 2 | Art (Digital Technology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FADIGITMFA/art-digital-technology-mfa |
| 3 | Dance | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FADANCEMFA/dance-mfa |
| 4 | Dance (Interdisciplinary Digital Media and Performance) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FADANDIMFA/dance-interdisciplinary-digital-media-and-performance-mfa |
| 5 | Theatre (Directing) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FADIRMFA/theatre-directing-mfa |
| 6 | Theatre (Dramatic Writing) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FADRWRTMFA/theatre-dramatic-writing-mfa |
| 7 | Theatre (Interdisciplinary Digital Media) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FATHEADMFA/theatre-interdisciplinary-digital-media-mfa |
| 8 | Theatre (Performance) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAPERFMFA/theatre-performance-mfa |
| 9 | Theatre (Theatre for Youth and Community) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAYOUTHMFA/theatre-theatre-for-youth-and-community-mfa |

##### MIA
| # | 项目 | URL |
|---|------|-----|
| 1 | Interior Architecture | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIIAMIA/interior-architecture-mia |

##### MID
| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIINDMID/industrial-design-mid |

##### MLA
| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARLDEMLA/landscape-architecture-mla |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Composition | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMCOMPMM/composition-mm |
| 2 | Composition (Interdisciplinary Digital Media) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FADIGITMM/composition-interdisciplinary-digital-media-mm |
| 3 | Music Learning and Teaching | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMUSEDMM/music-learning-and-teaching-mm |
| 4 | Music Therapy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMTHERMM/music-therapy-mm |
| 5 | Performance (Collaborative Piano) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FACPIANOMM/performance-collaborative-piano-mm |
| 6 | Performance (Conducting) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIPERCOMM/performance-conducting-mm |
| 7 | Performance (Performance Pedagogy) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAPPEDMM/performance-performance-pedagogy-mm |
| 8 | Performance (Voice, Music Theatre, Opera) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMUTPOMM/performance-voice-music-theatre-opera-mm |

##### MRED
| # | 项目 | URL |
|---|------|-----|
| 1 | Real Estate Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARREMREDEV/real-estate-development-mred |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture (Energy Perf/Climate Responsive Arch) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARENERGYMS/architecture-energy-perf-climate-responsive-arch-ms |
| 2 | Entertainment Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIEEMS/entertainment-engineering-ms |
| 3 | Entrepreneurship and Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIIVDMS/entrepreneurship-and-innovation-ms |
| 4 | Immersive Experience Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIIMEXDMS/immersive-experience-design-ms |
| 5 | Indigenous Placekeeping and Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIIPDMS/indigenous-placekeeping-and-design-ms |
| 6 | Media Arts and Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDGCMS/media-arts-and-sciences-ms |
| 7 | Media Arts and Sciences (Extended Reality Technologies) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDGCERTMS/media-arts-and-sciences-extended-reality-technologies-ms |

##### MSD
| # | 项目 | URL |
|---|------|-----|
| 1 | Design (Experience Design) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDEDMSD/design-experience-design-msd |
| 2 | Design (Space Architecture and Extreme Environments) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDSCSMSD/design-space-architecture-and-extreme-environments-msd |
| 3 | Design (Visual Communication Design) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARVCDMSD/design-visual-communication-design-msd |
| 4 | Healthcare and Healing Environments | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARHHEMSD/healthcare-and-healing-environments-msd |
| 5 | Industrial Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARINDDEMSD/industrial-design-msd |
| 6 | Interior Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARINTDEMSD/interior-design-msd |

##### MUD
| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARMUDMUD/urban-design-mud |

##### MUEP
| # | 项目 | URL |
|---|------|-----|
| 1 | Urban and Environmental Planning | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARURBMUEP/urban-and-environmental-planning-muep |

##### MVCD
| # | 项目 | URL |
|---|------|-----|
| 1 | Visual Communication Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIVCDMVCD/visual-communication-design-mvcd |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIARSPHD/art-history-phd |
| 2 | Design, Environment and the Arts | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDEAPHD/design-environment-and-the-arts-phd |
| 3 | Design, Environment and the Arts (Design) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDEADSPHD/design-environment-and-the-arts-design-phd |
| 4 | Design, Environment and the Arts (Digital Culture in Design) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIENVDGPHD/design-environment-and-the-arts-digital-culture-in-design-phd |
| 5 | Design, Environment and the Arts (Healthcare and Healing Environments) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARENHHEPHD/design-environment-and-the-arts-healthcare-and-healing-environments-phd |
| 6 | Design, Environment and the Arts (History, Theory and Criticism) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIDEAHTPHD/design-environment-and-the-arts-history-theory-and-criticism-phd |
| 7 | Media Arts and Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMASPHD/media-arts-and-sciences-phd |
| 8 | Music (Music Learning and Teaching) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAMUSEDPHD/music-music-learning-and-teaching-phd |
| 9 | Music (Musicology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/HIMUSMPHD/music-musicology-phd |
| 10 | Theatre (Theatre and Performance of the Americas) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAPERAMPHD/theatre-theatre-and-performance-of-the-americas-phd |
| 11 | Theatre (Theatre for Youth and Community) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FAYOUTHPHD/theatre-theatre-for-youth-and-community-phd |
| 12 | Urban Planning | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ARPUPPHD/urban-planning-phd |

#### Ira A. Fulton Schools of Engineering
##### DEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEGRDENG/engineering-deng |

##### DIT
| # | 项目 | URL |
|---|------|-----|
| 1 | Information Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESIFTDIT/information-technology-dit |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Machine Learning | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIMLGRCT/artificial-intelligence-and-machine-learning-graduate-certificate |
| 2 | Big Data | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESBDTAGRCT/big-data-graduate-certificate |
| 3 | Cloud Security Architecture | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCLARGRCT/cloud-security-architecture-graduate-certificate |
| 4 | Cybersecurity | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCYSCGRCT/cybersecurity-graduate-certificate |
| 5 | Foundations of Computing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESFOCGRCT/foundations-of-computing-graduate-certificate |
| 6 | Lean Six Sigma Black Belt | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESLSSBGRCT/lean-six-sigma-black-belt-graduate-certificate |
| 7 | Learning Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESLEGRCT/learning-engineering-graduate-certificate |
| 8 | Molecular, Cellular, Tissue and Biomaterials Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMCTBGRCT/molecular-cellular-tissue-and-biomaterials-engineering-graduate-certificate |
| 9 | Neural Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESNENGRCT/neural-engineering-graduate-certificate |
| 10 | Nuclear Power Generation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESNPGGRCT/nuclear-power-generation-graduate-certificate |
| 11 | Semiconductor Processing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSCPRGRCT/semiconductor-processing-graduate-certificate |
| 12 | Sensor Signal and Information Processing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSSIPGRCT/sensor-signal-and-information-processing-graduate-certificate |
| 13 | Software Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSERGRCT/software-engineering-graduate-certificate |

##### MCS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCOMSCMCS/computer-science-mcs |
| 2 | Computer Science (Big Data Systems) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSEBDMCS/computer-science-big-data-systems-mcs |
| 3 | Computer Science (Cybersecurity) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSEIMCS/computer-science-cybersecurity-mcs |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESENGRMENG/engineering-meng |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAEROSPMS/aerospace-engineering-ms |
| 2 | Artificial Intelligence | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIMS/artificial-intelligence-ms |
| 3 | Artificial Intelligence Engineering (Aerospace Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEAEMS/artificial-intelligence-engineering-aerospace-engineering-ms |
| 4 | Artificial Intelligence Engineering (Chemical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIECEMS/artificial-intelligence-engineering-chemical-engineering-ms |
| 5 | Artificial Intelligence Engineering (Computing Sciences) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIECSMS/artificial-intelligence-engineering-computing-sciences-ms |
| 6 | Artificial Intelligence Engineering (Electrical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEEEMS/artificial-intelligence-engineering-electrical-engineering-ms |
| 7 | Artificial Intelligence Engineering (Human-Centered Artificial Intelligence) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEHCMS/artificial-intelligence-engineering-human-centered-artificial-intelligence-ms |
| 8 | Artificial Intelligence Engineering (Intelligent Biomedical Systems Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEBSEMS/artificial-intelligence-engineering-intelligent-biomedical-systems-engineering-ms |
| 9 | Artificial Intelligence Engineering (Manufacturing) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEMMS/artificial-intelligence-engineering-manufacturing-ms |
| 10 | Artificial Intelligence Engineering (Materials Science and Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEMSEMS/artificial-intelligence-engineering-materials-science-and-engineering-ms |
| 11 | Artificial Intelligence Engineering (Mechanical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEMEMS/artificial-intelligence-engineering-mechanical-engineering-ms |
| 12 | Artificial Intelligence Engineering (Operations and Decision Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIEODSMS/artificial-intelligence-engineering-operations-and-decision-science-ms |
| 13 | Artificial Intelligence Engineering (Robotics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIERMS/artificial-intelligence-engineering-robotics-ms |
| 14 | Artificial Intelligence Engineering (Software Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIESEMS/artificial-intelligence-engineering-software-engineering-ms |
| 15 | Artificial Intelligence Engineering (Sustainable Engineering and Built Environment) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIESUBMS/artificial-intelligence-engineering-sustainable-engineering-and-built-environment-ms |
| 16 | Artificial Intelligence in Information Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIITMS/artificial-intelligence-in-information-technology-ms |
| 17 | Biological Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESBDEMS/biological-design-ms |
| 18 | Biomedical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESBIOENMS/biomedical-engineering-ms |
| 19 | Biomedical Informatics and Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESBIOINFMS/biomedical-informatics-and-data-science-ms |
| 20 | Chemical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCHEMEMS/chemical-engineering-ms |
| 21 | Civil, Environmental and Sustainable Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCIVILMS/civil-environmental-and-sustainable-engineering-ms |
| 22 | Clean Energy Systems | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCESMS/clean-energy-systems-ms |
| 23 | Computer Engineering (Computer Systems) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCENCMS/computer-engineering-computer-systems-ms |
| 24 | Computer Engineering (Electrical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCENEMS/computer-engineering-electrical-engineering-ms |
| 25 | Computer Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCOMSCMS/computer-science-ms |
| 26 | Computer Science (Artificial Intelligence) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSEAIMS/computer-science-artificial-intelligence-ms |
| 27 | Computer Science (Big Data Systems) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSEBDMS/computer-science-big-data-systems-ms |
| 28 | Computer Science (Biomedical Informatics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSBIOIMS/computer-science-biomedical-informatics-ms |
| 29 | Computer Science (Cybersecurity) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSEIAMS/computer-science-cybersecurity-ms |
| 30 | Computer Science (Media Arts and Sciences) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAMECSMS/computer-science-media-arts-and-sciences-ms |
| 31 | Construction Management and Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCONSTMS/construction-management-and-technology-ms |
| 32 | Data Science, Analytics and Engineering (Bayesian Machine Learning) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSEBMLMS/data-science-analytics-and-engineering-bayesian-machine-learning-ms |
| 33 | Data Science, Analytics and Engineering (Computational Mathematics and Data) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSECMDMS/data-science-analytics-and-engineering-computational-mathematics-and-data-ms |
| 34 | Data Science, Analytics and Engineering (Computing and Decision Analytics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSECDAMS/data-science-analytics-and-engineering-computing-and-decision-analytics-ms |
| 35 | Data Science, Analytics and Engineering (Electrical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSEEEMS/data-science-analytics-and-engineering-electrical-engineering-ms |
| 36 | Data Science, Analytics and Engineering (Human-Centered Applications) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSEHCAMS/data-science-analytics-and-engineering-human-centered-applications-ms |
| 37 | Data Science, Analytics and Engineering (Materials Science and Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSEMSEMS/data-science-analytics-and-engineering-materials-science-and-engineering-ms |
| 38 | Data Science, Analytics and Engineering (Mechanical and Aerospace Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSEMAEMS/data-science-analytics-and-engineering-mechanical-and-aerospace-engineering-ms |
| 39 | Data Science, Analytics and Engineering (Sustainable Engineering and Built Environment) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSESEBMS/data-science-analytics-and-engineering-sustainable-engineering-and-built-environment-ms |
| 40 | Electrical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEEMS/electrical-engineering-ms |
| 41 | Electrical Engineering (Media Arts and Sciences) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAMEMS/electrical-engineering-media-arts-and-sciences-ms |
| 42 | Environmental Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEVEMS/environmental-engineering-ms |
| 43 | Environmental and Resource Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESERMMS/environmental-and-resource-management-ms |
| 44 | Environmental and Resource Management (Water Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESERMWTMS/environmental-and-resource-management-water-management-ms |
| 45 | Graphic Information Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESGITMS/graphic-information-technology-ms |
| 46 | Human Systems Engineering (Aviation Human Factors) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESHSEAHFMS/human-systems-engineering-aviation-human-factors-ms |
| 47 | Human Systems Engineering (Health Systems) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESHSEHSMS/human-systems-engineering-health-systems-ms |
| 48 | Human Systems Engineering (Intelligent Systems) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESHSEISMS/human-systems-engineering-intelligent-systems-ms |
| 49 | Human Systems Engineering (User Experience Research) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESHSEUERMS/human-systems-engineering-user-experience-research-ms |
| 50 | Industrial Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESINDENMS/industrial-engineering-ms |
| 51 | Innovations in Medical and Patient Care Technologies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESIMPCTMS/innovations-in-medical-and-patient-care-technologies-ms |
| 52 | Management of Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMGMTCHMS/management-of-technology-ms |
| 53 | Materials Science and Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMATEMS/materials-science-and-engineering-ms |
| 54 | Mechanical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMEMS/mechanical-engineering-ms |
| 55 | Medical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMEDENMS/medical-engineering-ms |
| 56 | Modern Energy Production and Sustainable Use | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMEPSUMS/modern-energy-production-and-sustainable-use-ms |
| 57 | Robotics and Autonomous Systems (Artificial Intelligence) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESRASAIMS/robotics-and-autonomous-systems-artificial-intelligence-ms |
| 58 | Robotics and Autonomous Systems (Biomedical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESRASBEMS/robotics-and-autonomous-systems-biomedical-engineering-ms |
| 59 | Robotics and Autonomous Systems (Electrical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESRASEEMS/robotics-and-autonomous-systems-electrical-engineering-ms |
| 60 | Robotics and Autonomous Systems (Mechanical and Aerospace Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESRASMAEMS/robotics-and-autonomous-systems-mechanical-and-aerospace-engineering-ms |
| 61 | Robotics and Autonomous Systems (Systems Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESRASSEMS/robotics-and-autonomous-systems-systems-engineering-ms |
| 62 | Software Engineering (Cybersecurity) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSERCSMS/software-engineering-cybersecurity-ms |
| 63 | Software Engineering (Data Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSERDSMS/software-engineering-data-science-ms |
| 64 | User Experience | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESUSEXMS/user-experience-ms |

##### MSE
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCONEMSE/construction-engineering-mse |
| 2 | Electrical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEEMSE/electrical-engineering-mse |
| 3 | Engineering Science (Software Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSFEMSE/engineering-science-software-engineering-mse |
| 4 | Sustainable Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSUEMSE/sustainable-engineering-mse |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAERSPPHD/aerospace-engineering-phd |
| 2 | Artificial Intelligence | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAIPHD/artificial-intelligence-phd |
| 3 | Biomedical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESBIOENPHD/biomedical-engineering-phd |
| 4 | Biomedical Informatics and Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESBMIPHD/biomedical-informatics-and-data-science-phd |
| 5 | Chemical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCHEMEPHD/chemical-engineering-phd |
| 6 | Civil, Environmental and Sustainable Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCIVILPHD/civil-environmental-and-sustainable-engineering-phd |
| 7 | Clean Energy Systems | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCESPHD/clean-energy-systems-phd |
| 8 | Computer Engineering (Computer Systems) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCENCPHD/computer-engineering-computer-systems-phd |
| 9 | Computer Engineering (Electrical Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCENEPHD/computer-engineering-electrical-engineering-phd |
| 10 | Computer Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCOMSCPHD/computer-science-phd |
| 11 | Computer Science (Cybersecurity) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCSEIAPHD/computer-science-cybersecurity-phd |
| 12 | Computer Science (Media Arts and Sciences) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAMECSPHD/computer-science-media-arts-and-sciences-phd |
| 13 | Construction Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCONPHD/construction-management-phd |
| 14 | Data Science, Analytics and Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESDSEPHD/data-science-analytics-and-engineering-phd |
| 15 | Electrical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEEPHD/electrical-engineering-phd |
| 16 | Electrical Engineering (Media Arts and Sciences) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESAMEPHD/electrical-engineering-media-arts-and-sciences-phd |
| 17 | Engineering Education Systems and Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEESDPHD/engineering-education-systems-and-design-phd |
| 18 | Environmental Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESEVEPHD/environmental-engineering-phd |
| 19 | Industrial Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESINDENPHD/industrial-engineering-phd |
| 20 | Manufacturing Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMFGPHD/manufacturing-engineering-phd |
| 21 | Materials Science and Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESENMATPHD/materials-science-and-engineering-phd |
| 22 | Mechanical Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESMEPHD/mechanical-engineering-phd |
| 23 | Robotics and Autonomous Systems (Mechatronics and Automation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESRASMAPHD/robotics-and-autonomous-systems-mechatronics-and-automation-phd |
| 24 | Systems Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESSYSPHD/systems-engineering-phd |

#### John Shufeldt School of Medicine and Medical Engineering
##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://degrees.apps.asu.edu/masters-phd/major/ASU00/MDMEDMD/medicine-md |

#### Mary Lou Fulton College for Teaching and Learning Innovation
##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership and Innovation (Policy/Admin) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEINNPAEDD/educational-leadership-and-innovation-policy-admin-edd |
| 2 | Leadership and Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TELINEDD/leadership-and-innovation-edd |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEABAGRCT/applied-behavior-analysis-graduate-certificate |
| 2 | Autism Spectrum Disorders | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDSPEGRCA/autism-spectrum-disorders-graduate-certificate |
| 3 | Educating Multilingual Learners | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEESLGRCT/educating-multilingual-learners-graduate-certificate |
| 4 | Environmental Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEEVEDGRCT/environmental-education-graduate-certificate |
| 5 | Fundamentals of Environmental Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEFDEDGRCT/fundamentals-of-environmental-education-graduate-certificate |
| 6 | Gifted Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEGEDGRCT/gifted-education-graduate-certificate |
| 7 | Institutional Research and Policy Analysis | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDINSRESCE/institutional-research-and-policy-analysis-graduate-certificate |
| 8 | Learning Design and Technologies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDEDTGRCT/learning-design-and-technologies-graduate-certificate |
| 9 | Online Teaching for Grades K-12 | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEEDTGRCT/online-teaching-for-grades-k-12-graduate-certificate |
| 10 | Organizational Behavior Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEOBMGRCT/organizational-behavior-management-graduate-certificate |
| 11 | Teacher Certification | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TETEACGRCT/teacher-certification-graduate-certificate |
| 12 | Technology for Teaching and Learning | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDEDTTGRCT/technology-for-teaching-and-learning-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEEDUMA/education-ma |
| 2 | Education (Accomplished Teaching) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDACCTCMA/education-accomplished-teaching-ma |
| 3 | Education (Educating Multilingual Learners) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDESLMA/education-educating-multilingual-learners-ma |
| 4 | Education (Literacy Education) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDLANGMA/education-literacy-education-ma |
| 5 | Education for Planetary Futures | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEEPFMA/education-for-planetary-futures-ma |
| 6 | Educational Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDSPFMA/educational-policy-ma |
| 7 | Interdisciplinary Education on Community Health and Wellbeing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEIECHWMA/interdisciplinary-education-on-community-health-and-wellbeing-ma |
| 8 | Learning Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDPSYCHMA/learning-sciences-ma |
| 9 | Special Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDSPEDMA/special-education-ma |
| 10 | Special Education (Applied Behavior Analysis) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TESPEABAMA/special-education-applied-behavior-analysis-ma |
| 11 | Special Education (Autism Spectrum Disorders) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TESPEASDMA/special-education-autism-spectrum-disorders-ma |

##### MC
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDCOUNMC/counseling-mc |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction (Gifted Education) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEGEDMED/curriculum-and-instruction-gifted-education-med |
| 2 | Early Childhood Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEECEDMED/early-childhood-education-med |
| 3 | Early Childhood Education (Teacher Certification) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEECDTCMED/early-childhood-education-teacher-certification-med |
| 4 | Early Childhood Special Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEECSMED/early-childhood-special-education-med |
| 5 | Early Childhood Special Education (Teacher Certification) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEECSTCMED/early-childhood-special-education-teacher-certification-med |
| 6 | Educational Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDSUPVMED/educational-leadership-med |
| 7 | Educational Leadership (Principalship) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEPRINMED/educational-leadership-principalship-med |
| 8 | Elementary Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEELEMMED/elementary-education-med |
| 9 | Elementary Education (Teacher Certification) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEEEACLMED/elementary-education-teacher-certification-med |
| 10 | Global Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TEGLOEDMED/global-education-med |
| 11 | Higher and Postsecondary Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDPOSTMED/higher-and-postsecondary-education-med |
| 12 | Learning Design and Technologies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDTECHMED/learning-design-and-technologies-med |
| 13 | Secondary Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TESECEDMED/secondary-education-med |
| 14 | Secondary Education (Teacher Certification) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TESCERTMED/secondary-education-teacher-certification-med |
| 15 | Special Education (Teacher Certification) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TESECRTMED/special-education-teacher-certification-med |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDCPSYPHD/counseling-psychology-phd |
| 2 | Educational Policy and Evaluation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDLDRSHPHD/educational-policy-and-evaluation-phd |
| 3 | Educational Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDTECHPHD/educational-technology-phd |
| 4 | Learning, Literacies and Technologies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/EDCIPHD/learning-literacies-and-technologies-phd |

#### New College of Interdisciplinary Arts and Sciences
##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Behavioral Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASBHDSGRCT/behavioral-data-science-graduate-certificate |
| 2 | Biological Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASBDSGRCT/biological-data-science-graduate-certificate |
| 3 | Human Factors in Forensic Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASHFFSGRCT/human-factors-in-forensic-science-graduate-certificate |
| 4 | Industrial and Organizational Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASIOPGRCT/industrial-and-organizational-psychology-graduate-certificate |
| 5 | Positive Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPPSYGRCT/positive-psychology-graduate-certificate |
| 6 | Psychological Fundamentals of Well-being | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPFWBGRCT/psychological-fundamentals-of-well-being-graduate-certificate |
| 7 | Psychological Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPSYSGRCT/psychological-science-graduate-certificate |
| 8 | Science Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASSCOMGRCT/science-communication-graduate-certificate |
| 9 | Social Justice and Human Rights | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASJHRGRCT/social-justice-and-human-rights-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASCOMSTMA/communication-studies-ma |
| 2 | English | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASENGLMA/english-ma |
| 3 | Interdisciplinary Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASINTERMA/interdisciplinary-studies-ma |
| 4 | Social Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASSTCMA/social-data-science-ma |
| 5 | Social Justice and Human Rights | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASJHRMA/social-justice-and-human-rights-ma |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASBDSMS/biological-data-science-ms |
| 2 | Biological Data Science (Biotechnology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASBDSTECMS/biological-data-science-biotechnology-ms |
| 3 | Forensic Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASFPSYMS/forensic-psychology-ms |
| 4 | Forensic Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASFOREMS/forensic-science-ms |
| 5 | Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPGSMS/psychology-ms |
| 6 | Psychology (Data Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPSYDTSMS/psychology-data-science-ms |
| 7 | Psychology (Industrial and Organizational Psychology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPGSIOPMS/psychology-industrial-and-organizational-psychology-ms |
| 8 | Psychology (Positive Psychology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPGSPPMS/psychology-positive-psychology-ms |
| 9 | Psychology (Sport Psychology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASPGSSPMS/psychology-sport-psychology-ms |

##### PSM
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASFRSCIPSM/forensic-science-psm |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law and Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/ASLPSYPHD/law-and-psychology-phd |

#### Rob Walton College of Global Futures
##### EMSL
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability Leadership - Executive | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUEMSLEMSL/sustainability-leadership---executive-emsl |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Complex Adaptive Systems Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUCASGRCT/complex-adaptive-systems-science-graduate-certificate |
| 2 | Energy and Sustainability | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUERGSGRCT/energy-and-sustainability-graduate-certificate |
| 3 | Environmental and Sustainability Economics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUESECGRCT/environmental-and-sustainability-economics-graduate-certificate |
| 4 | Food Policy and Sustainability Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUFPSLGRCT/food-policy-and-sustainability-leadership-graduate-certificate |
| 5 | Global Development and Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FIGDIGRCT/global-development-and-innovation-graduate-certificate |
| 6 | Sustainability | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSGRCT/sustainability-graduate-certificate |
| 7 | Sustainability and Enterprise | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GFSEGRCT/sustainability-and-enterprise-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSTMA/sustainability-ma |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Coastal and Marine Science and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GFCMSMMS/coastal-and-marine-science-and-management-ms |
| 2 | Complex Systems Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GFCMPXSSMS/complex-systems-science-ms |
| 3 | Futures and Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GFFDMS/futures-and-design-ms |
| 4 | Global Technology and Development (Applied International Development) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FIGTDAIDMS/global-technology-and-development-applied-international-development-ms |
| 5 | Public Interest Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FIPITCHMS/public-interest-technology-ms |
| 6 | Sustainability | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSTMS/sustainability-ms |
| 7 | Sustainable Food Systems | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSFSMS/sustainable-food-systems-ms |

##### MSL
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSLMSL/sustainability-leadership-msl |

##### MSUS
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability Solutions | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSOMSUS/sustainability-solutions-msus |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Complex Adaptive Systems Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GFCASPHD/complex-adaptive-systems-science-phd |
| 2 | Innovation in Global Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/FIIGDPHD/innovation-in-global-development-phd |
| 3 | Ocean Futures | https://degrees.apps.asu.edu/masters-phd/major/ASU00/GFSEAPHD/ocean-futures-phd |
| 4 | Sustainability | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSTPHD/sustainability-phd |
| 5 | Sustainability (Complex Adaptive Systems Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUSTCPHD/sustainability-complex-adaptive-systems-science-phd |
| 6 | Sustainable Energy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/SUSUEPHD/sustainable-energy-phd |

#### Sandra Day O'Connor College of Law
##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Law and Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWHLPGRCT/health-law-and-policy-graduate-certificate |
| 2 | Indian Law | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWLAWGRCI/indian-law-graduate-certificate |
| 3 | Intellectual Property Law | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWIPLGRCT/intellectual-property-law-graduate-certificate |
| 4 | Law and Sustainability | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWLSUSGRCT/law-and-sustainability-graduate-certificate |
| 5 | Law, Science and Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWLAWSTCE/law-science-and-technology-graduate-certificate |
| 6 | Trial Advocacy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWTAGRCT/trial-advocacy-graduate-certificate |

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWJDJD/juris-doctor-jd |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Biotechnology and Genomics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWGENOMLLM/biotechnology-and-genomics-llm |
| 2 | Tribal Policy, Law and Government | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWTBLMLAWS/tribal-policy-law-and-government-llm |

##### MHREL
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Resources and Employment Law | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWHREMHREL/human-resources-and-employment-law-mhrel |

##### MLS
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Care Compliance and Administration | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWHCCMLS/health-care-compliance-and-administration-mls |
| 2 | Legal Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWLGSMLEGS/legal-studies-mls |

##### MSLB
| # | 项目 | URL |
|---|------|-----|
| 1 | Sports Law and Business | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LWSLBMSLB/sports-law-and-business-mslb |

#### School of Technology for Public Health
##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health (Public Health Technology) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/THPHPHTMPH/public-health-public-health-technology-mph |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/THPHTMS/public-health-technology-ms |

#### The College of Liberal Arts and Sciences
##### AuD
| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAUDAUDD/audiology-aud |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Addiction and Substance-Use Related Disorders | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAASRDGRCT/addiction-and-substance-use-related-disorders-graduate-certificate |
| 2 | African and African American Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAFRICACE/african-and-african-american-studies-graduate-certificate |
| 3 | American Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAMSGRCT/american-studies-graduate-certificate |
| 4 | Applied Prevention Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAPSGRCT/applied-prevention-science-graduate-certificate |
| 5 | Asian Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAASIANCE/asian-studies-graduate-certificate |
| 6 | Atmospheric Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAATMOSCE/atmospheric-science-graduate-certificate |
| 7 | Biomimicry | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABMYGRCT/biomimicry-graduate-certificate |
| 8 | Computational Life Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACMLSGRCT/computational-life-sciences-graduate-certificate |
| 9 | Computer-Assisted Language Learning | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACALLGRCT/computer-assisted-language-learning-graduate-certificate |
| 10 | Critical Theory | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACRTGRCT/critical-theory-graduate-certificate |
| 11 | Digital Humanities | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACDHGRCT/digital-humanities-graduate-certificate |
| 12 | Disability Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LADISGRCT/disability-studies-graduate-certificate |
| 13 | Environmental Communication and Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAECLGRCT/environmental-communication-and-leadership-graduate-certificate |
| 14 | Evolutionary Medicine | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAEVMDGRCT/evolutionary-medicine-graduate-certificate |
| 15 | Gender Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAWSTGRCT/gender-studies-graduate-certificate |
| 16 | Geographic Information Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGEOGISCE/geographic-information-science-graduate-certificate |
| 17 | Global Security and Competitive Statecraft | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGSCSGRCT/global-security-and-competitive-statecraft-graduate-certificate |
| 18 | Holocaust and Genocide Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAHGSGRCT/holocaust-and-genocide-studies-graduate-certificate |
| 19 | Immigration Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAIMMSTUCE/immigration-studies-graduate-certificate |
| 20 | Indigenous Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAIEDGRCT/indigenous-education-graduate-certificate |
| 21 | Linguistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LALINGUICE/linguistics-graduate-certificate |
| 22 | Medieval Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMEDSTCE/medieval-studies-graduate-certificate |
| 23 | Museum Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMUSEUMCE/museum-studies-graduate-certificate |
| 24 | Nonfiction Writing and Publishing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LANWPGRCT/nonfiction-writing-and-publishing-graduate-certificate |
| 25 | Public History | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPHGRCT/public-history-graduate-certificate |
| 26 | Scientific Teaching in Higher Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASTHEGRCT/scientific-teaching-in-higher-education-graduate-certificate |
| 27 | Sexuality Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASXSGRCT/sexuality-studies-graduate-certificate |
| 28 | Social Science Research Methods | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASSRMGRCT/social-science-research-methods-graduate-certificate |
| 29 | Social Transformation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASOTGRCT/social-transformation-graduate-certificate |
| 30 | Socio-Economic Justice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAECJUGRCT/socio-economic-justice-graduate-certificate |
| 31 | Spanish Language Pedagogy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASPAPGRCT/spanish-language-pedagogy-graduate-certificate |
| 32 | Translation Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LALTSGRCT/translation-studies-graduate-certificate |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Laws | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAWLAWSLLM/laws-llm |
| 2 | Laws (Global Legal Studies) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAWLGLPLLM/laws-global-legal-studies-llm |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAMSTMA/american-studies-ma |
| 2 | Applied Ethics and the Professions (Biomedical and Health Ethics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAEPMEMA/applied-ethics-and-the-professions-biomedical-and-health-ethics-ma |
| 3 | Applied Ethics and the Professions (Ethics and Emerging Technologies) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAEPEETMA/applied-ethics-and-the-professions-ethics-and-emerging-technologies-ma |
| 4 | Applied Ethics and the Professions (Science, Technology and Ethics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAEPSEEMA/applied-ethics-and-the-professions-science-technology-and-ethics-ma |
| 5 | Asian Languages/Civilizations (Chinese) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACHINAMA/asian-languages-civilizations-chinese-ma |
| 6 | Asian Languages/Civilizations (Japanese) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAJAPANMA/asian-languages-civilizations-japanese-ma |
| 7 | Classical Liberal Education and Civic Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACLEDLMA/classical-liberal-education-and-civic-leadership-ma |
| 8 | Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACOMMOMA/communication-ma |
| 9 | Communication (Health Communication) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACOMHEMA/communication-health-communication-ma |
| 10 | English | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAENGLMA/english-ma |
| 11 | English Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAENEDMA/english-education-ma |
| 12 | French Comparative Literature | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAFRECLMA/french-comparative-literature-ma |
| 13 | French Linguistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAFRELINMA/french-linguistics-ma |
| 14 | French Literature | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAFRELITMA/french-literature-ma |
| 15 | Gender, Women and Sexuality Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAWSTMA/gender-women-and-sexuality-studies-ma |
| 16 | Geography | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGEOGMA/geography-ma |
| 17 | German | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGERMMA/german-ma |
| 18 | Global Health | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASSHMA/global-health-ma |
| 19 | Global Security | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGSCMA/global-security-ma |
| 20 | Global Security (Cybersecurity) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGSCSECMA/global-security-cybersecurity-ma |
| 21 | Global Security (Intelligence Studies) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGSCISMA/global-security-intelligence-studies-ma |
| 22 | Global Security (Irregular Warfare) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGSCIWMA/global-security-irregular-warfare-ma |
| 23 | History | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAHISTMA/history-ma |
| 24 | Indigenous Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAIEDMA/indigenous-education-ma |
| 25 | International Affairs and Leadership | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAIALMA/international-affairs-and-leadership-ma |
| 26 | Language Teaching | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LALANTCHMA/language-teaching-ma |
| 27 | Linguistics and Applied Linguistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LALINMA/linguistics-and-applied-linguistics-ma |
| 28 | Mathematics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMATHMA/mathematics-ma |
| 29 | Museum Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMUSSTMA/museum-studies-ma |
| 30 | Philosophy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPHILMA/philosophy-ma |
| 31 | Political Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPPSMA/political-psychology-ma |
| 32 | Political Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPOLSCMA/political-science-ma |
| 33 | Political Science (Political Analytics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPOSPAMA/political-science-political-analytics-ma |
| 34 | Religious Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LARELIGMA/religious-studies-ma |
| 35 | Social and Cultural Pedagogy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASCPMA/social-and-cultural-pedagogy-ma |
| 36 | Sociology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASOCMA/sociology-ma |
| 37 | Spanish | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASPANMA/spanish-ma |
| 38 | War and Strategy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAWASMA/war-and-strategy-ma |
| 39 | World War II Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAWWSMA/world-war-ii-studies-ma |

##### MAS
| # | 项目 | URL |
|---|------|-----|
| 1 | Film and Media Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAMPCMAS/film-and-media-studies-mas |
| 2 | Geographic Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGEOEDMAS/geographic-education-mas |
| 3 | Geographic Information Systems | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGISMAS/geographic-information-systems-mas |
| 4 | Infant - Family Practice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACDEMAS/infant---family-practice-mas |
| 5 | Marriage and Family Therapy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMFTMAS/marriage-and-family-therapy-mas |
| 6 | Transborder Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LATCLMAS/transborder-studies-mas |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACWRITMFA/creative-writing-mfa |

##### MLSt
| # | 项目 | URL |
|---|------|-----|
| 1 | Liberal Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMLSMLS/liberal-studies-mlst |

##### MNS
| # | 项目 | URL |
|---|------|-----|
| 1 | Natural Science (Earth and Space Sciences) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LANATSCIMN/natural-science-earth-and-space-sciences-mns |
| 2 | Physics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPHYSMNS/physics-mns |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAACTMS/actuarial-science-ms |
| 2 | Addiction Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAADPSYMS/addiction-psychology-ms |
| 3 | Aging | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAALDMS/aging-ms |
| 4 | American Indian Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAISMS/american-indian-studies-ms |
| 5 | American Indian Studies (Cultural Resource Revitalization and Sust) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAISCMS/american-indian-studies-cultural-resource-revitalization-and-sust-ms |
| 6 | American Indian Studies (Indigenous Rights and Social Justice) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAISIMS/american-indian-studies-indigenous-rights-and-social-justice-ms |
| 7 | American Indian Studies (Tribal Leadership and Governance) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAISTMS/american-indian-studies-tribal-leadership-and-governance-ms |
| 8 | American Indian Studies (Visual and Oral Culture) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAISVMS/american-indian-studies-visual-and-oral-culture-ms |
| 9 | Applied Behavior Analysis | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAPBAMS/applied-behavior-analysis-ms |
| 10 | Applied Statistics and Data Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASTADSMS/applied-statistics-and-data-science-ms |
| 11 | Astrophysics and Astronomy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAASTPHMS/astrophysics-and-astronomy-ms |
| 12 | Biochemistry | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOCHMS/biochemistry-ms |
| 13 | Biochemistry (Medicinal Chemistry) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABCHMCMS/biochemistry-medicinal-chemistry-ms |
| 14 | Biology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOMS/biology-ms |
| 15 | Biology (Biology and Society) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOSMS/biology-biology-and-society-ms |
| 16 | Biomimicry | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABMYMS/biomimicry-ms |
| 17 | Chemistry | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACHEMMS/chemistry-ms |
| 18 | Clinical Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACLPSYMS/clinical-psychology-ms |
| 19 | Communication Disorders | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACOMDISMS/communication-disorders-ms |
| 20 | Computational Life Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACLSMS/computational-life-sciences-ms |
| 21 | Exploration Systems Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDMS/exploration-systems-design-ms |
| 22 | Exploration Systems Design (Instrumentation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDIMS/exploration-systems-design-instrumentation-ms |
| 23 | Exploration Systems Design (Sensor Networks) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDSNMS/exploration-systems-design-sensor-networks-ms |
| 24 | Exploration Systems Design (Systems Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDSEMS/exploration-systems-design-systems-engineering-ms |
| 25 | Family and Human Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAFAMHDMS/family-and-human-development-ms |
| 26 | Geological Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGEOSCMS/geological-sciences-ms |
| 27 | Global Health | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASSHMS/global-health-ms |
| 28 | Justice Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAJUSSTMS/justice-studies-ms |
| 29 | Microbiology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMICROMS/microbiology-ms |
| 30 | Molecular and Cellular Biology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACELLMS/molecular-and-cellular-biology-ms |
| 31 | Neuroscience | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABMENMS/neuroscience-ms |
| 32 | Physics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPHYSIMS/physics-ms |
| 33 | Plant Biology and Conservation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPLBIOMS/plant-biology-and-conservation-ms |

##### MSTP
| # | 项目 | URL |
|---|------|-----|
| 1 | Science and Technology Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAHSDPSM/science-and-technology-policy-mstp |

##### MTESOL
| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching English to Speakers of Other Languages | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAENGMTESL/teaching-english-to-speakers-of-other-languages-mtesol |

##### PSM
| # | 项目 | URL |
|---|------|-----|
| 1 | Nanoscience | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LANANPSM/nanoscience-psm |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Behavior | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAANBPHD/animal-behavior-phd |
| 2 | Anthropology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAANTHRPHD/anthropology-phd |
| 3 | Anthropology (Complex Adaptive Systems Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAANTHCPHD/anthropology-complex-adaptive-systems-science-phd |
| 4 | Anthropology (Urbanism) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAURBPHD/anthropology-urbanism-phd |
| 5 | Applied Mathematics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAPMPHD/applied-mathematics-phd |
| 6 | Applied Mathematics for the Life and Social Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAAMLPHD/applied-mathematics-for-the-life-and-social-sciences-phd |
| 7 | Astrophysics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAASTPHPHD/astrophysics-phd |
| 8 | Biochemistry | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOCHPHD/biochemistry-phd |
| 9 | Biology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOPHD/biology-phd |
| 10 | Biology (Biology and Society) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOSPHD/biology-biology-and-society-phd |
| 11 | Biology (Complex Adaptive Systems Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LABIOCPHD/biology-complex-adaptive-systems-science-phd |
| 12 | Chemistry | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACHEMPHD/chemistry-phd |
| 13 | Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACOMMOPHD/communication-phd |
| 14 | Comparative Culture and Language | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAILCPHD/comparative-culture-and-language-phd |
| 15 | East Asian Languages and Civilization | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAEALCPHD/east-asian-languages-and-civilization-phd |
| 16 | English (English Education) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAENEDPHD/english-english-education-phd |
| 17 | English (Literature) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAENLITPHD/english-literature-phd |
| 18 | English (Writing, Rhetorics and Literacies) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAENRHTPHD/english-writing-rhetorics-and-literacies-phd |
| 19 | Environmental Life Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAELSPHD/environmental-life-sciences-phd |
| 20 | Environmental Social Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESSPHD/environmental-social-science-phd |
| 21 | Environmental Social Science (Complex Adaptive Systems Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESSCPHD/environmental-social-science-complex-adaptive-systems-science-phd |
| 22 | Environmental Social Science (Urbanism) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESSURPHD/environmental-social-science-urbanism-phd |
| 23 | Evolutionary Biology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAEVOPHD/evolutionary-biology-phd |
| 24 | Exploration Systems Design | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDPHD/exploration-systems-design-phd |
| 25 | Exploration Systems Design (Instrumentation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDIPHD/exploration-systems-design-instrumentation-phd |
| 26 | Exploration Systems Design (Sensor Networks) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDSNPHD/exploration-systems-design-sensor-networks-phd |
| 27 | Exploration Systems Design (Systems Engineering) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAESDSEPHD/exploration-systems-design-systems-engineering-phd |
| 28 | Family and Human Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAFAMSCPHD/family-and-human-development-phd |
| 29 | Gender Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGSTPHD/gender-studies-phd |
| 30 | Geographic Information Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGISPHD/geographic-information-science-phd |
| 31 | Geography | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGEOGPHD/geography-phd |
| 32 | Geological Sciences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAGEOSCPHD/geological-sciences-phd |
| 33 | Global Health | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASSHPHD/global-health-phd |
| 34 | History | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAHISTPHD/history-phd |
| 35 | History and Philosophy of Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAHPSCIPHD/history-and-philosophy-of-science-phd |
| 36 | Justice Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAJUSSTPHD/justice-studies-phd |
| 37 | Linguistics and Applied Linguistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LALINPHD/linguistics-and-applied-linguistics-phd |
| 38 | Mathematics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMATHPHD/mathematics-phd |
| 39 | Mathematics Education | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMTEPHD/mathematics-education-phd |
| 40 | Microbiology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAMICROPHD/microbiology-phd |
| 41 | Molecular and Cellular Biology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LACELLPHD/molecular-and-cellular-biology-phd |
| 42 | Philosophy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPHILPHD/philosophy-phd |
| 43 | Physics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPHYSIPHD/physics-phd |
| 44 | Political Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPOLSCPHD/political-science-phd |
| 45 | Psychology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPSYCHPHD/psychology-phd |
| 46 | Psychology (Clinical) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPSYCLPHD/psychology-clinical-phd |
| 47 | Psychology (Quantitative Research Methods) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAPSYQUPHD/psychology-quantitative-research-methods-phd |
| 48 | Religious Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LARELIGPHD/religious-studies-phd |
| 49 | Sociology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASOCPHD/sociology-phd |
| 50 | Spanish Linguistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASPALIPHD/spanish-linguistics-phd |
| 51 | Spanish Literature and Culture | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASPANPHD/spanish-literature-and-culture-phd |
| 52 | Speech and Hearing Science | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LAHEARPHD/speech-and-hearing-science-phd |
| 53 | Statistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LASTPPHD/statistics-phd |
| 54 | Transborder Studies | https://degrees.apps.asu.edu/masters-phd/major/ASU00/LATCLPHD/transborder-studies-phd |

#### Thunderbird School of Global Management
##### DPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Leadership and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGLMDPP/global-leadership-and-management-dpp |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | AI, Analytics and FinTech Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBAFTIGRCT/ai-analytics-and-fintech-innovation-graduate-certificate |
| 2 | Foundations of Cross-cultural Leadership and Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBFCCLGRCT/foundations-of-cross-cultural-leadership-and-innovation-graduate-certificate |
| 3 | Global Management, Entrepreneurship and Innovation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBTGMGRCT/global-management-entrepreneurship-and-innovation-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Affairs and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGAMMA/global-affairs-and-management-ma |
| 2 | Global Affairs and Management - Executive | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGAMEMA/global-affairs-and-management---executive-ma |

##### MALM
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Leadership and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBALMMALM/applied-leadership-and-management-malm |

##### MGLS
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Leadership and Strategy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGLSMGLS/global-leadership-and-strategy-mgls |
| 2 | Global Leadership and Strategy - Executive | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGLSXMGLS/global-leadership-and-strategy---executive-mgls |

##### MGM
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBTGMMGM/global-management-mgm |
| 2 | Global Management (Creative Industries and Design Thinking) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMCIDMGM/global-management-creative-industries-and-design-thinking-mgm |
| 3 | Global Management (Data Science) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMDSCMGM/global-management-data-science-mgm |
| 4 | Global Management (Digital Audience Strategy) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMDASMGM/global-management-digital-audience-strategy-mgm |
| 5 | Global Management (Executive) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBTGMXMGM/global-management-executive-mgm |
| 6 | Global Management (Global Affairs) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGAMGM/global-management-global-affairs-mgm |
| 7 | Global Management (Global Business) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGBMGM/global-management-global-business-mgm |
| 8 | Global Management (Global Development and Innovation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGDIMGM/global-management-global-development-and-innovation-mgm |
| 9 | Global Management (Global Digital Transformation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGDTMGM/global-management-global-digital-transformation-mgm |
| 10 | Global Management (Global Entrepreneurship) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGEMGM/global-management-global-entrepreneurship-mgm |
| 11 | Global Management (Global Health Care Delivery) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGHDMGM/global-management-global-health-care-delivery-mgm |
| 12 | Global Management (Global Health Care Innovation) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBTGMHCMGM/global-management-global-health-care-innovation-mgm |
| 13 | Global Management (Global Legal Studies) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMGLSMGM/global-management-global-legal-studies-mgm |
| 14 | Global Management (Nonprofit Leadership and Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMNLMGM/global-management-nonprofit-leadership-and-management-mgm |
| 15 | Global Management (Public Administration) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMPAMGM/global-management-public-administration-mgm |
| 16 | Global Management (Public Policy) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMPPMGM/global-management-public-policy-mgm |
| 17 | Global Management (Sustainability Solutions) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMSSMGM/global-management-sustainability-solutions-mgm |
| 18 | Global Management (Sustainable Tourism) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMSTMGM/global-management-sustainable-tourism-mgm |
| 19 | Global Management - Executive (Space Leadership, Business and Policy) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBGMSBPMGM/global-management---executive-space-leadership-business-and-policy-mgm |

##### MLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Leadership and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBLDMGMLM/leadership-and-management-mlm |
| 2 | Leadership and Management (Global Creative Industries) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/TBLDMGCMLM/leadership-and-management-global-creative-industries-mlm |

#### W. P. Carey School of Business
##### DBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BASCMDBA/business-administration-dba |
| 2 | Business Administration (Supply Chain Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BABUASCDBA/business-administration-supply-chain-management-dba |
| 3 | Global Financial Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAGFMDBA/global-financial-management-dba |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Fundamentals of Business Analytics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BABUSAGRCT/fundamentals-of-business-analytics-graduate-certificate |
| 2 | Real Estate | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAREAGRCT/real-estate-graduate-certificate |
| 3 | Supply Chain Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BASCMCERT/supply-chain-management-graduate-certificate |

##### MACC
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy and Data Analytics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAACCMACC/accountancy-and-data-analytics-macc |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence in Business | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAAIBMS/artificial-intelligence-in-business-ms |
| 2 | Business Analytics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BABUSANMS/business-analytics-ms |
| 3 | Economics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAECONMS/economics-ms |
| 4 | Finance | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAFINMS/finance-ms |
| 5 | Global Logistics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAGLSMS/global-logistics-ms |
| 6 | Information Systems Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAINFOMS/information-systems-management-ms |
| 7 | Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BACMRMS/management-ms |
| 8 | Management in China/Corporate | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAMCCMS/management-in-china-corporate-ms |
| 9 | Marketing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAMKTCEMS/marketing-ms |
| 10 | Supply Chain Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BASCMMS/supply-chain-management-ms |
| 11 | Supply Chain Management and Engineering | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BASCMEMS/supply-chain-management-and-engineering-ms |

##### MTax
| # | 项目 | URL |
|---|------|-----|
| 1 | Taxation and Data Analytics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BATAMTAX/taxation-and-data-analytics-mtax |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAACCTPHD/accountancy-phd |
| 2 | Agribusiness | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAAGRIPHD/agribusiness-phd |
| 3 | Computer Information Systems | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAINFSYPHD/computer-information-systems-phd |
| 4 | Economics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAECONPHD/economics-phd |
| 5 | Finance | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAFINANPHD/finance-phd |
| 6 | Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAMGMTPHD/management-phd |
| 7 | Marketing | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BAMARKPHD/marketing-phd |
| 8 | Supply Chain Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/BASCMPHD/supply-chain-management-phd |

#### Walter Cronkite School of Journalism and Mass Communication
##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Audiences | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSDASGRCT/digital-audiences-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Investigative Journalism | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSINVJOUMA/investigative-journalism-ma |
| 2 | Journalism | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSJRNMA/journalism-ma |
| 3 | Narrative and Emerging Media | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSNEMMA/narrative-and-emerging-media-ma |
| 4 | Science Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSSCOMMA/science-communication-ma |
| 5 | Sports Journalism | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSSPJMA/sports-journalism-ma |
| 6 | Sports Strategic Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSSPSTCOMA/sports-strategic-communication-ma |
| 7 | Strategic Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSSTRCOMMA/strategic-communication-ma |
| 8 | Strategic Communication (Health) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSSTRCHEMA/strategic-communication-health-ma |

##### MMC
| # | 项目 | URL |
|---|------|-----|
| 1 | Mass Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSMCOMMMC/mass-communication-mmc |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Strategy and Audience Engagement | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSDASMS/digital-strategy-and-audience-engagement-ms |
| 2 | Media Research and Technology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSMRTMS/media-research-and-technology-ms |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism and Mass Communication | https://degrees.apps.asu.edu/masters-phd/major/ASU00/CSJMCPHD/journalism-and-mass-communication-phd |

#### Watts College of Public Service & Community Solutions
##### DCJ
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRIMJDCJ/criminal-justice-dcj |

##### EMPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration - Executive | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUAEMPA/public-administration---executive-empa |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Assessment of Integrative Health Modalities | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPSWGGRCH/assessment-of-integrative-health-modalities-graduate-certificate |
| 2 | Corrections Leadership and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCMGGRCT/corrections-leadership-and-management-graduate-certificate |
| 3 | Crime Analysis | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRMAGRCT/crime-analysis-graduate-certificate |
| 4 | Criminal Sentencing and Sentencing Advocacy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCSAGRCT/criminal-sentencing-and-sentencing-advocacy-graduate-certificate |
| 5 | Domestic Violence Intervention and Victim Advocacy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPDVEPGRCT/domestic-violence-intervention-and-victim-advocacy-graduate-certificate |
| 6 | Emergency Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEMEGRCT/emergency-management-graduate-certificate |
| 7 | Foundations in Gerontology | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPGNTGRCT/foundations-in-gerontology-graduate-certificate |
| 8 | Homeland Security | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPHLSGRCT/homeland-security-graduate-certificate |
| 9 | Latino Cultural Competency in Social Work | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPSWGGRCL/latino-cultural-competency-in-social-work-graduate-certificate |
| 10 | Law Enforcement Administration | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPLEAGRCT/law-enforcement-administration-graduate-certificate |
| 11 | Nonprofit Leadership and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPNONPROCE/nonprofit-leadership-and-management-graduate-certificate |
| 12 | Participatory Governance | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPGOGRCT/participatory-governance-graduate-certificate |
| 13 | Policy Informatics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPOIGRCT/policy-informatics-graduate-certificate |
| 14 | Program Evaluation | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPGEVGRCT/program-evaluation-graduate-certificate |
| 15 | Public Administration | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUAGRCT/public-administration-graduate-certificate |
| 16 | Public Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUPGRCT/public-policy-graduate-certificate |
| 17 | Social Entrepreneurship and Community Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPSECDGRCT/social-entrepreneurship-and-community-development-graduate-certificate |
| 18 | Sustainable Tourism | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPSTGRCT/sustainable-tourism-graduate-certificate |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRIMJMA/criminal-justice-ma |
| 2 | Emergency Management and Homeland Security | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEMHSMA/emergency-management-and-homeland-security-ma |
| 3 | Emergency Management and Homeland Security (Biosecurity and Threat Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEMHSBTMA/emergency-management-and-homeland-security-biosecurity-and-threat-management-ma |
| 4 | Emergency Management and Homeland Security (Community Resilience) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEMHSCRMA/emergency-management-and-homeland-security-community-resilience-ma |
| 5 | Emergency Management and Homeland Security (Cybersecurity Policy and Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEHSCPMMA/emergency-management-and-homeland-security-cybersecurity-policy-and-management-ma |
| 6 | Emergency Management and Homeland Security (Emergency Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEMHSEMMA/emergency-management-and-homeland-security-emergency-management-ma |
| 7 | Emergency Management and Homeland Security (Homeland Security) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPEMHSHSMA/emergency-management-and-homeland-security-homeland-security-ma |

##### MNLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Nonprofit Leadership and Management | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPNPSMNS/nonprofit-leadership-and-management-mnlm |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPADTMPA/public-administration-mpa |
| 2 | Public Administration (Emergency Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPAFEMPA/public-administration-emergency-management-mpa |
| 3 | Public Administration (Nonprofit Administration) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPNONPRMPA/public-administration-nonprofit-administration-mpa |
| 4 | Public Administration (Public Finance) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPAFPMPA/public-administration-public-finance-mpa |
| 5 | Public Administration (Urban Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPAFUMPA/public-administration-urban-management-mpa |

##### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUBPMPP/public-policy-mpp |
| 2 | Public Policy (Environmental Policy) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUPEPMPP/public-policy-environmental-policy-mpp |
| 3 | Public Policy (Policy Informatics) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUPPIMPP/public-policy-policy-informatics-mpp |
| 4 | Public Policy (Science and Technology Policy) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUPSTMPP/public-policy-science-and-technology-policy-mpp |

##### MPSLA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Safety Leadership and Administration | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPSLAMPSL/public-safety-leadership-and-administration-mpsla |
| 2 | Public Safety Leadership and Administration (EMS - Mobile Integrated Health Care) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPSEMMPSL/public-safety-leadership-and-administration-ems---mobile-integrated-health-care-mpsla |
| 3 | Public Safety Leadership and Administration (Executive Fire Administration) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPSEFMPSL/public-safety-leadership-and-administration-executive-fire-administration-mpsla |
| 4 | Public Safety Leadership and Administration (Executive Police Administration) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPSEPMPSL/public-safety-leadership-and-administration-executive-police-administration-mpsla |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Community Resources and Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPRECDTMS/community-resources-and-development-ms |
| 2 | Community Resources and Development (Nonprofits and NGOs) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRDNPMS/community-resources-and-development-nonprofits-and-ngos-ms |
| 3 | Community Resources and Development (Parks and Recreation Management) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRDPRMS/community-resources-and-development-parks-and-recreation-management-ms |
| 4 | Community Resources and Development (Sustainable Communities) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRDSCMS/community-resources-and-development-sustainable-communities-ms |
| 5 | Community Resources and Development (Tourism) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRDTMMS/community-resources-and-development-tourism-ms |
| 6 | Crime Analysis | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRIMANMS/crime-analysis-ms |
| 7 | Criminology and Criminal Justice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRJMS/criminology-and-criminal-justice-ms |
| 8 | Program Evaluation and Data Analytics | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPGEMS/program-evaluation-and-data-analytics-ms |

##### MST
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainable Tourism | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPSUSTMST/sustainable-tourism-mst |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work - Advanced Standing - (Policy, Administration and Community Practice) | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCPDTMSW/social-work---advanced-standing---policy-administration-and-community-practice-msw |
| 2 | Social Work - Advanced Standing - Advanced Generalist | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPASWMSW/social-work---advanced-standing---advanced-generalist-msw |
| 3 | Social Work - Advanced Standing - Direct Practice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPAPDTMSW/social-work---advanced-standing---direct-practice-msw |
| 4 | Social Work - Standard Program | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPSWDMSW/social-work---standard-program-msw |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Community Resources and Development | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRDPHD/community-resources-and-development-phd |
| 2 | Criminology and Criminal Justice | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPCRJPHD/criminology-and-criminal-justice-phd |
| 3 | Public Administration and Policy | https://degrees.apps.asu.edu/masters-phd/major/ASU00/PPPUBADPHD/public-administration-and-policy-phd |

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 |
|------|-----|
| Admissions website | https://admission.asu.edu/ |
| Application portal | ASU Application or Common Application |
| Application fee (AZ resident) | $55 |
| Application fee (domestic nonresident) | $85 |
| Application fee (international) | $90 |
| Application fee (ASU Online) | $75 |
| Priority admission date | November 1 |
| Regular admission date | January 15 |
| FAFSA priority date | January 15 |
| Barrett Honors College early action | November 1 |
| SAT/ACT policy | **Test-optional** (not required, but recommended for scholarship consideration) |
| Superscore policy | N/A (test-optional) |
| Essay required | No |
| Recommendation required | No |
| Interview | No |
| Enrollment deposit | Opens early October |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低要求 | 推荐分数 | 备注 |
|------|---------|---------|------|
| TOEFL iBT (general) | 61 / 3.5 overall | 79+ | All majors except below |
| TOEFL iBT (Engineering) | 79 / 4 overall | 79+ | Ira A. Fulton Schools |
| TOEFL iBT (Journalism) | 100 / 5 overall | 100+ | Walter Cronkite School |
| TOEFL iBT (Nursing BSN) | 76 / 4 overall | 76+ | BSN program only |
| IELTS (general) | 6.0 | 6.5+ | All majors except below |
| IELTS (Engineering) | 6.5 | 6.5+ | Ira A. Fulton Schools |
| IELTS (Journalism) | 7.0 | 7.0+ | Walter Cronkite School |
| IELTS (Nursing BSN) | 6.5 | 6.5+ | BSN program only |
| PTE (general) | 53 | 58+ | All majors except below |
| PTE (Engineering) | 58 | 58+ | Ira A. Fulton Schools |
| PTE (Journalism) | 73 | 73+ | Walter Cronkite School |
| PTE (Nursing BSN) | Not accepted | — | BSN program |
| Duolingo (general) | 95 | 105+ | All majors except below |
| Duolingo (Engineering) | 105 | 105+ | Ira A. Fulton Schools |
| Duolingo (Journalism) | 120 | 120+ | Walter Cronkite School |
| Duolingo (Nursing BSN) | 100 | 100+ | BSN program only |
| Cambridge English (general) | 170 (B2 First, C1 Advanced, C2 Proficiency) | 176+ | All majors except below |
| Cambridge English (Engineering) | 176 | 176+ | Ira A. Fulton Schools |
| Cambridge English (Journalism) | 185 | 185+ | Walter Cronkite School |
| Cambridge English (Nursing BSN) | 176 | 176+ | BSN program only |

> Applicability: Required for all international applicants whose native language is not English. Conditional admission available for up to 3 semesters.

### 3.3 Graduate — global rules

| 字段 | 值 |
|------|-----|
| Admissions model | Decentralized (each program sets own requirements) |
| Application portal | ASU Graduate Application |
| Application fee (domestic) | $70 |
| Application fee (international on visa) | $115 |
| GRE policy | Per program (ASU does NOT accept GRE at-home exam) |
| GMAT policy | Per program |
| Minimum GPA | 3.00 (last 60 semester hours) |
| English proficiency | Same as UG requirements for non-native speakers |
| Application opens (Fall) | September 1 |
| Application opens (Spring) | February 1 |
| FAFSA priority date | January 15 |
| CGS April-15 signatory | Yes |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-2027, line-itemized, Tempe campus)

| 费用项目 | Arizona Resident | Nonresident | International |
|---------|-----------------|-------------|---------------|
| Base Tuition | $12,177 | $35,715 | $39,062 |
| Tuition Surcharge | $350 | $350 | $350 |
| Advanced Technology Fee | $200 | $200 | $200 |
| Student Initiated Fees | $807 | $807 | $807 |
| Undergraduate College Fees | $0-$1,280 | $0-$2,190 | $0-$2,190 |
| Books/Course Materials | $1,320 | $1,320 | $1,320 |
| Housing | $11,473 | $11,473 | $11,473 |
| Food | $7,346 | $7,346 | $7,346 |
| Travel | $1,650 | $1,650 | $1,650 |
| Personal | $2,343 | $2,343 | $2,343 |
| Loan Fees | $72 | $72 | $72 |
| International Student Fee | — | — | $400 |
| Health Insurance | — | — | $2,765 |
| **Estimated Total** | **$37,738-$39,018** | **$59,367-$61,557** | **$67,788-$67,978** |

> Source: tuition.asu.edu/cost (AJAX view, 2026-2027 academic year, Tempe campus, on-campus housing)

### 4.2 Graduate cost (2026-2027, Tempe campus)

| 费用项目 | Arizona Resident | Nonresident | International |
|---------|-----------------|-------------|---------------|
| Base Tuition | $13,327 | $29,196 | $31,860 |
| Tuition Surcharge | $350 | $350 | $350 |
| Advanced Technology Fee | $200 | $200 | $200 |
| Student Initiated Fees | $807 | $803 | $807 |
| Graduate Student Support Fees | $300 | $290 | $300 |
| Books/Course Materials | $1,908 | $1,908 | $1,908 |
| Housing and Food | $21,087 | $21,087 | $21,087 |
| Transportation | $3,696 | $3,696 | $3,696 |
| Personal | $4,785 | $4,785 | $4,785 |
| Loan Fees | $804 | $804 | $804 |
| International Student Fee | — | — | $400 |
| Health Insurance | — | — | $3,189 |
| **Estimated Total** | **$47,265** | **$72,862** | **$69,386** |

> Source: tuition.asu.edu/cost (AJAX view, 2026-2027 academic year, 9 credits for graduates)

### 4.3 Financial aid policy

| 字段 | 值 |
|------|-----|
| Need-blind/need-aware | **Need-aware** for all students (domestic and international) |
| Meets 100% demonstrated need | No (not guaranteed) |
| Merit scholarships | Yes (New American University Scholarships, automatically considered) |
| Federal School Code | 001081 |
| FAFSA priority date | January 15 |
| Obama Scholars Program | Yes (for eligible AZ residents, deadline Jan 15) |
| Arizona Promise Program | Yes (for eligible AZ residents, deadline April 1) |
| Debt-free graduation rate | 45%+ of students graduate debt-free |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: UG Aptitude Requirements
```yaml
field: undergraduate.admissions.aptitude_requirements
value: 'Top 25% in class OR 3.0 GPA OR ACT 22 (24 nonres) OR SAT 1120 (1180 nonres)'
source_url: https://admission.asu.edu/apply/first-year/admission
source_snippet: 'To be admitted to ASU, you will need one of the following: top 25% in high school graduating class; 3.00 unweighted GPA in competency courses; ACT: 22 (24 nonresidents); SAT: 1120 (1180 nonresidents)'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: UG Test Policy
```yaml
field: undergraduate.admissions.test_policy
value: 'Test-optional (not required, but recommended for scholarship consideration)'
source_url: https://admission.asu.edu/apply/first-year/admission
source_snippet: 'ACT or SAT scores are not required for admission, but may be submitted for ASU course placement or as supplemental information.'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: UG Priority Deadline
```yaml
field: undergraduate.admissions.priority_deadline
value: 'November 1'
source_url: https://admission.asu.edu/apply/first-year/admission
source_snippet: 'Complete your application for fall 2027 admission by the Nov. 1 priority admission date to ensure you are considered for the maximum amount of scholarship opportunities.'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: UG Regular Deadline
```yaml
field: undergraduate.admissions.regular_deadline
value: 'January 15'
source_url: https://admission.asu.edu/apply/first-year/admission
source_snippet: 'ASU's regular admission date is Jan. 15, 2027.'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: UG Application Fee
```yaml
field: undergraduate.admissions.application_fee
value: '$55 AZ resident, $85 domestic nonresident, $90 international'
source_url: https://admission.asu.edu/apply/first-year/admission
source_snippet: 'Arizona residents: $55; Domestic nonresidents: $85; ASU Online: $75; International nonresidents: $90'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: UG English Proficiency (General)
```yaml
field: undergraduate.international.english_proficiency
value: 'IELTS 6.0, TOEFL 61, DET 95, PTE 53, Cambridge 170 (general); higher for Engineering/Journalism/Nursing'
source_url: https://admission.asu.edu/apply/international/first-year
source_snippet: 'All other majors/colleges: IELTS 6.0, TOEFL (iBT) 61 / 3.5 overall score, Cambridge English Exams 170, Duolingo 95, PTE 53'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: UG Cost of Attendance (AZ Resident)
```yaml
field: undergraduate.costs.tuition_resident
value: '$12,177 base tuition (2026-27)'
source_url: https://tuition.asu.edu/cost
source_snippet: 'Arizona resident, living on campus: Tempe Base Tuition* $12,177'
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: UG Cost of Attendance (Nonresident)
```yaml
field: undergraduate.costs.tuition_nonresident
value: '$35,715 base tuition (2026-27)'
source_url: https://tuition.asu.edu/cost
source_snippet: 'Nonresident undergraduate, living on campus: Tempe Base Tuition* $35,715'
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: UG Cost of Attendance (International)
```yaml
field: undergraduate.costs.tuition_international
value: '$39,062 base tuition (2026-27)'
source_url: https://tuition.asu.edu/cost
source_snippet: 'International undergraduate, living on campus: Tempe Base Tuition* $39,062'
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-001: Graduate Admissions GPA Requirement
```yaml
field: graduate.admissions.gpa_requirement
value: '3.00 GPA (last 60 semester hours)'
source_url: https://admission.asu.edu/graduate/apply
source_snippet: 'Competitive applicants typically have a "B" (3.00 on a 4.00 scale) grade point average in the last 60 semester hours or 90 quarter hours of undergraduate coursework.'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate GRE Policy
```yaml
field: graduate.admissions.gre_policy
value: 'Per program; ASU does NOT accept GRE at-home exam'
source_url: https://admission.asu.edu/graduate/apply
source_snippet: 'ASU does not accept the GRE® General Test at-home exam.'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate Application Fee
```yaml
field: graduate.admissions.application_fee
value: '$70 domestic, $115 international on visa'
source_url: https://admission.asu.edu/graduate/apply
source_snippet: '$70: U.S. citizen, U.S. permanent resident, in application for permanent residency, DACA, international online student studying outside the U.S. $115: International students on any nonimmigrant visa type studying in the U.S.'
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-004: Graduate Cost of Attendance (AZ Resident)
```yaml
field: graduate.costs.tuition_resident
value: '$13,327 base tuition (2026-27)'
source_url: https://tuition.asu.edu/cost
source_snippet: 'Arizona resident graduate student Base Tuition* $13,327'
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-005: Graduate Cost of Attendance (Nonresident)
```yaml
field: graduate.costs.tuition_nonresident
value: '$29,196 base tuition (2026-27)'
source_url: https://tuition.asu.edu/cost
source_snippet: 'Nonresident graduate student Base Tuition* $29,196'
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-006: Graduate Cost of Attendance (International)
```yaml
field: graduate.costs.tuition_international
value: '$31,860 base tuition (2026-27)'
source_url: https://tuition.asu.edu/cost
source_snippet: 'International graduate student Base Tuition* $31,860'
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-P-001: Program Counts
```yaml
field: programs.total_count
value: '1184 total (490 UG + 694 Grad)'
source_url: https://degrees.apps.asu.edu/bachelors, https://degrees.apps.asu.edu/masters-phd
source_snippet: 'ASU offers more than 400 undergraduate majors... more than 450 graduate degree and certificate programs'
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
asu-knowledge-base-v2/
├── 00-institution-overview
├── 01-ug-liberal-arts
├── 02-ug-engineering
├── 03-ug-herberger-design-arts
├── 04-ug-business
├── 05-ug-other-colleges
├── 06-grad-liberal-arts
├── 07-grad-engineering
├── 08-grad-herberger-design-arts
├── 09-grad-watts-public-service
├── 10-grad-teaching-learning
├── 11-grad-nursing
├── 12-grad-business
├── 13-grad-thunderbird
├── 14-grad-health-solutions
├── 15-grad-other-colleges
├── 16-admissions-deadlines
├── 17-costs-financial-aid
└── 18-evidence-chain
```

### Per-chunk metadata template

```yaml
metadata:
  collection: 'asu-knowledge-base-v2'
  school: '<home college>'
  degree_level: '<BA|BS|MA|MS|PhD|...>'
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | UG minors complete list | degrees.apps.asu.edu/minors |
| P0 | Graduate program detail pages (GRE/TOEFL per program) | degrees.apps.asu.edu/masters-phd/major/... |
| P1 | Barrett Honors College requirements | admission.asu.edu/barrett |
| P1 | Transfer admission requirements | admission.asu.edu/apply/transfer |
| P1 | Financial aid details (scholarship amounts) | admission.asu.edu/cost-aid |
| P2 | ASU Online programs | asuonline.asu.edu |
| P2 | Accelerated degree programs | degrees.asu.edu |

---

## SECTION 7 — Cross-school Comparison Framework

| 维度 | ASU | (Other schools) |
|------|-----|-----------------|
| Total UG cost/yr (AZ resident, on-campus) | $37,738-$39,018 | |
| Total UG cost/yr (nonresident, on-campus) | $59,367-$61,557 | |
| Total UG cost/yr (international, on-campus) | $67,788-$67,978 | |
| Tuition/yr (AZ resident) | $12,177 | |
| Tuition/yr (nonresident) | $35,715 | |
| Tuition/yr (international) | $39,062 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (rolling, priority Nov 1) | |
| RA deadline | January 15 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 61 (general), 79 (Engineering), 100 (Journalism) | |
| IELTS min | 6.0 (general), 6.5 (Engineering), 7.0 (Journalism) | |
| Grad application fee | $70 domestic, $115 intl | |
| Total program count (Rule 1) | 1184 | |
| School/department count (Rule 2) | 17+ | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admission.asu.edu, tuition.asu.edu, degrees.apps.asu.edu, asu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch AJAX
> **Granularity**: school → department → degree-level → program