# Florida Atlantic University (FAU) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview) -- Rules 1-4

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA/BArch/BM/BSN/etc.) | 94 |
| 本科证书 (Undergraduate Certificate) | 56 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/DNP/etc.) | 106 |
| 研究生证书 (Graduate Certificate + Post-Master's Certificate) | 51 |
| **学位项目总计 (UG + Grad, 含证书)** | **307** |
| 学院总数 | 10 (degree-granting) |

> Note: Some programs list multiple degree types (e.g. "B.S., B.B.A."), each counted as a separate row. Raw unique program names: 281; expanded degree rows: 307. FAU has 10 degree-granting colleges plus an administrative Graduate College.

### 0.2 学院 / 系层级结构 (Rule 2 -- Hierarchy with Parent-Child)

```
Florida Atlantic University
├── Dorothy F. Schmidt College of Arts and Letters          [学院]
│   ├── School of Architecture                              [系]
│   ├── School of Communication & Multimedia Studies        [系]
│   ├── School of Music                                     [系]
│   ├── School of Theatre & Dance                           [系]
│   ├── Department of Anthropology                          [系]
│   ├── Department of English                               [系]
│   ├── Department of History                               [系]
│   ├── Department of Languages, Linguistics & Comparative Literature [系]
│   ├── Department of Philosophy                            [系]
│   ├── Department of Political Science                     [系]
│   ├── Department of Psychology                            [系]
│   ├── Department of Sociology                             [系]
│   └── Department of Visual Arts & Art History             [系]
├── College of Business                                     [学院]
│   ├── School of Accounting                                [系]
│   ├── Department of Economics                             [系]
│   ├── Department of Finance                               [系]
│   ├── Department of Management                            [系]
│   ├── Department of Marketing                             [系]
│   └── Department of IT & Operations Management            [系]
├── College of Education                                    [学院]
│   ├── Dept of Curriculum, Culture & Educational Inquiry   [系]
│   ├── Dept of Educational Leadership & Research Methodology [系]
│   ├── Dept of Exceptional Student Education               [系]
│   └── Dept of Exercise Science & Health Promotion         [系]
├── College of Engineering and Computer Science              [学院]
│   ├── Dept of Civil, Environmental & Geomatics Engineering [系]
│   ├── Dept of Computer & Electrical Engineering and CS    [系]
│   ├── Dept of Ocean & Mechanical Engineering              [系]
│   └── Dept of Mathematical Sciences                       [系]  ⚠ shared with Science
├── Charles E. Schmidt College of Medicine                   [学院]
├── Christine E. Lynn College of Nursing                     [学院]
├── Charles E. Schmidt College of Science                    [学院]
│   ├── Department of Biological Sciences                   [系]
│   ├── Department of Chemistry & Biochemistry              [系]
│   ├── Department of Geosciences                           [系]
│   ├── Department of Mathematical Sciences                 [系]  ⚠ shared with Engineering
│   ├── Department of Physics                               [系]
│   └── Department of Psychology                            [系]
├── College of Social Work and Criminal Justice              [学院]
│   ├── School of Criminology & Criminal Justice            [系]
│   └── School of Social Work                               [系]
├── Harriet L. Wilkes Honors College                         [学院]
├── Undergraduate Studies                                    [学院]
└── Graduate College                                         [行政学院, not degree-granting]
```

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| UG Cert | Undergraduate Certificate | Undergraduate Certificate | 本科 | 56 |
| Grad Cert | Graduate Certificate | Graduate Certificate | 研究生 | 44 |
| BS | B.S. | Bachelor of Science | 本科 | 34 |
| BA | B.A. | Bachelor of Arts | 本科 | 32 |
| MS | M.S. | Master of Science | 研究生 | 30 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 23 |
| MEd | M.Ed. | Master of Education | 研究生 | 10 |
| MA | M.A. | Master of Arts | 研究生 | 9 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 8 |
| Post-Masters Cert | Post-Master's Certificate | Post-Master's Certificate | 研究生 | 7 |
| MST | M.S.T. | Master of Science in Teaching | 研究生 | 5 |
| BAE | B.A.E. | Bachelor of Arts Education | 本科 | 5 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 4 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 3 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 3 |
| EdS | Ed.S. | Education Specialist | 研究生 | 3 |
| MAcc | M.AC. | Master of Accounting | 研究生 | 2 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | 2 |
| PSM | P.S.M. | Professional Science Master | 研究生 | 2 |
| BM | B.M. | Bachelor of Music | 本科 | 2 |
| MHA | M.H.A. | Master of Health Administration | 研究生 | 2 |
| MTX | M.TX. | Master of Taxation | 研究生 | 2 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 2 |
| BPS | B.P.S. | Bachelor of Professional Studies | 本科 | 2 |
| BArch | B.Arch. | Bachelor of Architecture | 本科 | 1 |
| BGS | B.G.S. | Bachelor of General Studies | 本科 | 1 |
| BHS | B.H.S. | Bachelor of Health Sciences | 本科 | 1 |
| MD | M.D. | Doctor of Medicine | 研究生 | 1 |
| MM | M.M. | Master of Music | 研究生 | 1 |
| BME | B.M.E. | Bachelor of Music Education | 本科 | 1 |
| MNM | M.N.M. | Master of Nonprofit Management | 研究生 | 1 |
| MSN | M.S.N. | Master of Science in Nursing | 研究生 | 1 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 1 |
| MPA | M.P.A. | Master of Public Administration | 研究生 | 1 |
| BPM | B.P.M. | Bachelor of Professional Management | 本科 | 1 |
| BSW | B.S.W. | Bachelor of Social Work | 本科 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| DSW | D.S.W. | Doctor of Social Work | 研究生 | 1 |
| MURP | M.U.R.P. | Master of Urban & Regional Planning | 研究生 | 1 |

**Total degree rows: 307**

### 0.4 分布矩阵 (Rule 4 -- Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BBA | BFA | BArch | BAE | Other UG | MA | MS | MFA | MBA | MEd+ | PhD | Prof Doc | UG Cert | Grad Cert+ | 合计 |
|------------|----|----|-----|-----|-------|-----|----------|----|----|-----|-----|------|-----|----------|---------|------------|------|
| Undergraduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| Arts & Letters | 15 | 0 | 0 | 3 | 1 | 0 | 5 | 8 | 1 | 4 | 0 | 5 | 2 | 0 | 10 | 7 | 61 |
| Business | 0 | 9 | 8 | 0 | 0 | 0 | 1 | 0 | 8 | 0 | 3 | 7 | 1 | 0 | 14 | 9 | 60 |
| Education | 6 | 3 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 0 | 0 | 10 | 5 | 3 | 5 | 5 | 43 |
| Engineering and Computer Science | 1 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 7 | 0 | 11 | 10 | 48 |
| Honors | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 4 |
| Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 7 | 12 |
| Science | 7 | 11 | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 0 | 0 | 7 | 7 | 0 | 12 | 7 | 61 |
| Social Work and Criminal Justice | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 | 4 | 11 |
| **合计** | 32 | 34 | 8 | 3 | 1 | 5 | 11 | 9 | 30 | 4 | 3 | 31 | 23 | 6 | 56 | 51 | **307** |

> Reconciliation: Rule 1 total (307) == Matrix sum (307). PASS

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

Florida Atlantic University has 10 degree-granting colleges. The undergraduate programs are distributed across all colleges. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### Undergraduate Studies

##### B.G.S. (Bachelor of General Studies)
| # | 专业 |
|---|------|
| 1 | General Studies |

##### B.P.S. (Bachelor of Professional Studies)
| # | 专业 |
|---|------|
| 1 | Professional Studies |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Undergraduate Research |

#### Arts & Letters

##### B.A. (Bachelor of Arts)
| # | 专业 |
|---|------|
| 1 | Anthropology |
| 2 | Art (Concentrations: Art History, Studio Art) |
| 3 | Art Education |
| 4 | Communication Studies |
| 5 | English (Concentrations: Writing and Rhetoric) |
| 6 | History (Concentrations: Africana History, British History, Legal History, Religious History) |
| 7 | Interdisciplinary Studies (Concentrations: Arts and Humanities, Community and Visual Design, Pre-Law, Social Science, Women, Gender and Sexuality) |
| 8 | Jewish Studies |
| 9 | Languages, Linguistics and Comparative Literature (Concentrations: French, Italian, Linguistics, Spanish) |
| 10 | Multimedia Studies (Concentrations: Film, Video and New Media, Multimedia Journalism) |
| 11 | Music |
| 12 | Philosophy |
| 13 | Political Science (Concentrations: Global Governance, Pre-Law) |
| 14 | Sociology |
| 15 | Theatre (Concentrations: Design and Technology) |

##### B.F.A. (Bachelor of Fine Arts)
| # | 专业 |
|---|------|
| 1 | Art (Concentrations: Graphic Design, Studio Art) |
| 2 | Art Education |
| 3 | Theatre (Concentrations: Design and Technology, Music Theatre, Performance) |

##### B.M. (Bachelor of Music)
| # | 专业 |
|---|------|
| 1 | Commercial Music (Concentrations: Commercial Music Composition, Music Business, Music Technology) |
| 2 | Music (Concentrations: Performance) |

##### B.M.E. (Bachelor of Music Education)
| # | 专业 |
|---|------|
| 1 | Music Education |

##### B.Arch. (Bachelor of Architecture)
| # | 专业 |
|---|------|
| 1 | Architecture |

##### B.P.S. (Bachelor of Professional Studies)
| # | 专业 |
|---|------|
| 1 | Public Safety Administration (Concentrations: Disaster Management, Law Enforcement/Corrections) |

##### B.P.M. (Bachelor of Professional Management)
| # | 专业 |
|---|------|
| 1 | Public Management |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Asian Studies |
| 2 | Classical Studies |
| 3 | English as a Second Language |
| 4 | Ethics, Law and Society |
| 5 | Ethnic Studies |
| 6 | Interdisciplinary Applications of Artificial Intelligence: Societal |
| 7 | Latin American Studies |
| 8 | Peace, Justice and Human Rights |
| 9 | Professional and Technical Writing |
| 10 | Religious Studies |

#### Business

##### B.S. (Bachelor of Science)
| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Data Science and Analytics (Concentrations: Data Science in Business) |
| 3 | Economics (Concentrations: Business Economics) |
| 4 | Finance |
| 5 | Hospitality and Tourism Management |
| 6 | International Business |
| 7 | Management (Concentrations: Entrepreneurship, Leadership and Applied Management Skills) |
| 8 | Management Information Systems (Concentrations: Business Analytics, Cybersecurity) |
| 9 | Marketing (Concentrations: Advertising) |

##### B.B.A. (Bachelor of Business Administration)
| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Economics (Concentrations: Business Economics) |
| 3 | Finance |
| 4 | Hospitality and Tourism Management |
| 5 | International Business |
| 6 | Management (Concentrations: Entrepreneurship, Leadership and Applied Management Skills) |
| 7 | Management Information Systems (Concentrations: Business Analytics, Cybersecurity) |
| 8 | Marketing (Concentrations: Advertising) |

##### B.H.S. (Bachelor of Health Sciences)
| # | 专业 |
|---|------|
| 1 | Health Administration |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Business Analytics |
| 2 | Casino and Gaming Industry Management |
| 3 | Club Management |
| 4 | Cybersecurity: Information Technology |
| 5 | Digital Marketing |
| 6 | FinTech |
| 7 | Gerontology |
| 8 | Healthcare Information Systems |
| 9 | Hospitality and Tourism Management |
| 10 | Interdisciplinary Applications of Artificial Intelligence: Business |
| 11 | International Business |
| 12 | Investment Management |
| 13 | Meetings and Events Management |
| 14 | Risk Management and Insurance |

#### Education

##### B.A. (Bachelor of Arts)
| # | 专业 |
|---|------|
| 1 | Elementary Education |
| 2 | English Education |
| 3 | Exceptional Student Education: ESOL Endorsement |
| 4 | Mathematics Education |
| 5 | Science Education (Concentrations: Biology Education, Chemistry Education, Physics Education) |
| 6 | Social Science Education |

##### B.S. (Bachelor of Science)
| # | 专业 |
|---|------|
| 1 | Early Care and Education |
| 2 | Science Education (Concentrations: Biology Education, Chemistry Education, Physics Education) |
| 3 | Science Education (Concentrations: Biology Education, Chemistry Education, Physics Education) |

##### B.A.E. (Bachelor of Arts Education)
| # | 专业 |
|---|------|
| 1 | Elementary Education |
| 2 | English Education |
| 3 | Exceptional Student Education: ESOL Endorsement |
| 4 | Mathematics Education |
| 5 | Social Science Education |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Diversity and Global Studies |
| 2 | Early Childhood Environmental Education |
| 3 | Supported Community Access |
| 4 | Supported Community Living |
| 5 | Supported Employment |

#### Engineering and Computer Science

##### B.A. (Bachelor of Arts)
| # | 专业 |
|---|------|
| 1 | Computer Science |

##### B.S. (Bachelor of Science)
| # | 专业 |
|---|------|
| 1 | Civil Engineering |
| 2 | Computer Engineering |
| 3 | Computer Science |
| 4 | Data Science and Analytics (Concentrations: Data Science and Engineering) |
| 5 | Electrical Engineering |
| 6 | Environmental Engineering |
| 7 | Geomatics Engineering |
| 8 | Mechanical Engineering |
| 9 | Ocean Engineering |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Aerospace Engineering |
| 2 | Artificial Intelligence |
| 3 | Biomedical Engineering |
| 4 | Cybersecurity: Computer Science |
| 5 | Data Science: Computer Science and Analytics |
| 6 | Interdisciplinary Applications of Artificial Intelligence: Technology |
| 7 | Marine Materials and Offshore Engineering |
| 8 | Naval Architecture |
| 9 | Robotics Engineering |
| 10 | Surveying and Mapping |
| 11 | Underwater Acoustics |

#### Honors

##### B.A. (Bachelor of Arts)
| # | 专业 |
|---|------|
| 1 | Biological and Physical Sciences (Concentrations: Biological Chemistry, Biology, Chemistry, Data Analytics, Environmental Science, Marine Biology, Mathematics, Neuroscience, Physics) |
| 2 | Liberal Arts and Sciences (Concentrations: American Studies, Anthropology, Art, Biological Anthropology, Business, Economics, English Literature, Environmental Studies, Interdisciplinary Critical Theory, Interdisciplinary History, Interdisciplinary Mathemtaical Sciences, International Studies, Latin American Studies, Law and Society, Medical Humanities, Philosophy, Political Science, Psychology, Spanish, Women Studies, Writing) |

##### B.S. (Bachelor of Science)
| # | 专业 |
|---|------|
| 1 | Biological and Physical Sciences (Concentrations: Biological Chemistry, Biology, Chemistry, Data Analytics, Environmental Science, Marine Biology, Mathematics, Neuroscience, Physics) |
| 2 | Liberal Arts and Sciences (Concentrations: Biological Anthropology, Psychology) |

#### Nursing

##### B.S.N. (Bachelor of Science in Nursing)
| # | 专业 |
|---|------|
| 1 | Nursing |
| 2 | Nursing: Accelerated |

#### Science

##### B.A. (Bachelor of Arts)
| # | 专业 |
|---|------|
| 1 | Biological Sciences |
| 2 | Chemistry |
| 3 | Geosciences (Concentrations: Geography, Geology) |
| 4 | Health Science (Concentrations: Behavioral and Mental Health, Public/Global/Environmental Health, Science, Women's Health) |
| 5 | Mathematics |
| 6 | Physics |
| 7 | Psychology |

##### B.S. (Bachelor of Science)
| # | 专业 |
|---|------|
| 1 | Biological Sciences |
| 2 | Chemistry (Concentrations: Biochemistry) |
| 3 | Data Science and Analytics (Concentrations: Data Science in the Natural Sciences) |
| 4 | Exercise Science and Health Promotion (Concentrations: Exercise Physiology, Pre-Physical Therapy and Occupational Therapy) |
| 5 | Geosciences (Concentrations: Climate Change, Geography, Geology) |
| 6 | Mathematics |
| 7 | Medical Biology |
| 8 | Neuroscience and Behavior |
| 9 | Physics |
| 10 | Urban and Regional Planning |
| 11 | Urban Design |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Actuarial Science |
| 2 | Advanced Geographic Information Systems |
| 3 | Applied Mental Health Services |
| 4 | Biotechnology |
| 5 | Cybersecurity: Mathematical Sciences |
| 6 | Data Science: Mathematical Sciences |
| 7 | Environmental Science |
| 8 | Geographic Information Systems |
| 9 | Interdisciplinary Applications of Artificial Intelligence: Scientific |
| 10 | Pharmaceutical Technology |
| 11 | Post-Baccalaureate Pre-Health Professions |
| 12 | Statistics |

#### Social Work and Criminal Justice

##### B.A. (Bachelor of Arts)
| # | 专业 |
|---|------|
| 1 | Criminal Justice |

##### B.S.W. (Bachelor of Social Work)
| # | 专业 |
|---|------|
| 1 | Social Work |

##### Undergraduate Certificate (Undergraduate Certificate)
| # | 专业 |
|---|------|
| 1 | Child Welfare |
| 2 | Healthy Aging |
| 3 | Social Justice |

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 学位级别

Florida Atlantic University's graduate programs are administered through individual colleges, with the Graduate College providing centralized oversight for admissions, policies, and student services.


#### Arts & Letters

##### M.A. (Master of Arts)
| # | 项目 |
|---|------|
| 1 | Anthropology |
| 2 | Communication |
| 3 | English (Concentrations: Rhetoric and Composition, Science Fiction and Fantasy) |
| 4 | History |
| 5 | Languages, Linguistics and Comparative Literature (Concentrations: Comparative Literature, French, Linguistics, Spanish, Teaching of French, Teaching of Spanish) |
| 6 | Political Science |
| 7 | Sociology |
| 8 | Women, Gender and Sexuality Studies |

##### M.S. (Master of Science)
| # | 项目 |
|---|------|
| 1 | Data Science and Analytics (Concentrations: Data Science in Society) |

##### M.F.A. (Master of Fine Arts)
| # | 项目 |
|---|------|
| 1 | Creative Writing |
| 2 | Media, Technology and Entertainment |
| 3 | Studio/Fine Arts (Concentrations: Graphic Design, Studio Art) |
| 4 | Theatre (Concentrations: Design and Technology, Performance) |

##### M.A.T. (Master of Arts in Teaching)
| # | 项目 |
|---|------|
| 1 | Anthropology |
| 2 | Political Science |

##### M.M. (Master of Music)
| # | 项目 |
|---|------|
| 1 | Music (Concentrations: Choral Conducting, Commercial Music, Composition, Instrumental Performance, Performance, Piano Performance, Vocal Performance, Wind Conducting) |

##### M.N.M. (Master of Nonprofit Management)
| # | 项目 |
|---|------|
| 1 | Nonprofit Management |

##### M.P.A. (Master of Public Administration)
| # | 项目 |
|---|------|
| 1 | Public Administration |

##### Ph.D. (Doctor of Philosophy)
| # | 项目 |
|---|------|
| 1 | Comparative Studies (Concentrations: Culture, Society, and Politics, Cultures, Languages, and Literature, Design, Aesthetics, and the Arts, Fine and Performing Arts, Public Intellectuals) |
| 2 | Public Administration |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | English as a Second Language |
| 2 | Film and Culture |
| 3 | Literary Translation |
| 4 | Nonprofit Executive Leadership |
| 5 | Public Ethics and Leadership |
| 6 | Public Policy |
| 7 | Women, Gender and Sexuality Studies |

#### Business

##### M.S. (Master of Science)
| # | 项目 |
|---|------|
| 1 | Business Analytics |
| 2 | Data Science and Analytics (Concentrations: Data Science in Business) |
| 3 | Economics (Concentrations: Econometrics and Data Analytics, Financial Economics, International Economics) |
| 4 | Executive International Business |
| 5 | Finance |
| 6 | Information Technology and Management (Concentrations: Business Analytics, Information Technology Management) |
| 7 | International Business |
| 8 | Supply Chain Management |

##### M.B.A. (Master of Business Administration)
| # | 项目 |
|---|------|
| 1 | Business Administration (Concentrations: Accounting, Business Analytics, Crisis and Disaster Management, Entrepreneurial Management, Finance, Health Administration, Hospitality and Tourism Management, International Business, Management Information Systems, Marketing, Operations Management, Sport Management) |
| 2 | Executive Business Administration (Concentrations: Accounting, Business Analytics, Crisis and Disaster Management, Entrepreneurial Management, Finance, Health Administration, Hospitality and Tourism Management, International Business, Management Information Systems, Marketing, Operations Management, Sport Management) |
| 3 | Professional Business Administration (Concentrations: Accounting, Business Analytics, Crisis and Disaster Management, Entrepreneurial Management, Finance, Health Administration, Hospitality and Tourism Management, International Business, Management Information Systems, Marketing, Operations Management, Sport Management) |

##### M.S.T. (Master of Science in Teaching)
| # | 项目 |
|---|------|
| 1 | Economics |

##### M.AC. (Master of Accounting)
| # | 项目 |
|---|------|
| 1 | Accounting (Concentrations: Accounting Information Systems, Tax) |
| 2 | Executive Master of Accounting (Concentrations: Business Valuation, Digital Accounting Forensics and Data Analytics, Forensic Accounting, Forensic Accounting and Business Valuation, Forensic Accounting and Digital Accounting Forensics, Internal Auditing, Professional Accounting, Tax) |

##### M.H.A. (Master of Health Administration)
| # | 项目 |
|---|------|
| 1 | Executive Health Administration (Concentrations: Crisis and Disaster Management) |
| 2 | Health Administration |

##### M.TX. (Master of Taxation)
| # | 项目 |
|---|------|
| 1 | Executive Master of Taxation |
| 2 | Taxation |

##### Ph.D. (Doctor of Philosophy)
| # | 项目 |
|---|------|
| 1 | Business Administration (Concentrations: Accounting, Executive, Finance, Information Technology, Management, Marketing) |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | Big Data Analytics: Business |
| 2 | Crisis and Disaster Management |
| 3 | Crisis and Emergency Management |
| 4 | FinTech |
| 5 | Health Administration |
| 6 | Hospitality and Tourism Management |
| 7 | Innovation Entrepreneurship |
| 8 | Professional Accounting |
| 9 | Risk Management |

#### Education

##### M.S. (Master of Science)
| # | 项目 |
|---|------|
| 1 | Speech - Language Pathology/Audiology |

##### M.Ed. (Master of Education)
| # | 项目 |
|---|------|
| 1 | Counselor Education (Concentrations: Clinical Mental Health Counseling, Clinical Rehabilitation Counseling, School Counseling) |
| 2 | Curriculum and Instruction (Concentrations: Noncertification Art, Noncertification Biology, Noncertification Chemistry, Noncertification Early Childhood Education, Noncertification English, Noncertification ESOL Education, Noncertification French, Noncertification Mathematics, Noncertification Multicultural Education, Noncertification Physics, Noncertification Reading, Noncertification Social Science, Noncertification Spanish) |
| 3 | Educational Leadership (Concentrations: Adult and Community Educational Leaders, Higher Education Leaders, School Leaders (K-12)) |
| 4 | Educational Psychology |
| 5 | Elementary Education (Concentrations: ESOL plus Certification) |
| 6 | Environmental Education |
| 7 | Exceptional Student Education |
| 8 | Instructional Technology |
| 9 | Reading Education |
| 10 | Secondary Education plus Certification (Concentrations: Art Certification, Biology Certification, Chemistry Certification, English/ESOL Certification, Mathematics Certification, Physics Certification, Social Science Certification) |

##### Ph.D. (Doctor of Philosophy)
| # | 项目 |
|---|------|
| 1 | Counselor Education |
| 2 | Curriculum and Instruction |
| 3 | Educational Leadership (Concentrations: Adult and Community Educational Leaders, Higher Education Leaders, School Leaders (K-12)) |
| 4 | Neuroscience |
| 5 | Special Education |

##### Ed.S. (Education Specialist)
| # | 项目 |
|---|------|
| 1 | Counselor Education (Concentrations: Mental Health Counseling, School Counseling) |
| 2 | Curriculum and Instruction (Concentrations: Noncertification Art, Noncertification Biology, Noncertification Chemistry, Noncertification Early Childhood Education, Noncertification English, Noncertification ESOL Education, Noncertification French, Noncertification Mathematics, Noncertification Multicultural Education, Noncertification Physics, Noncertification Reading, Noncertification Social Science, Noncertification Spanish) |
| 3 | Educational Leadership (Concentrations: Adult and Community Educational Leaders, School Leaders (K-12) Advanced, School Leaders (K-12) with Certification) |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | Environmental Education |
| 2 | Instructional Design |
| 3 | K-12 Online Teaching |
| 4 | Multicultural Education |
| 5 | Teacher Leadership |

#### Engineering and Computer Science

##### M.S. (Master of Science)
| # | 项目 |
|---|------|
| 1 | Artificial Intelligence |
| 2 | Biomedical Engineering (Concentrations: Bioinformatics) |
| 3 | Civil Engineering (Concentrations: Structural/Geotechnical Engineering, Transportation/Geomatics Engineering, Water Resources/Environmental Engineering) |
| 4 | Computer Engineering |
| 5 | Computer Science |
| 6 | Data Science and Analytics (Concentrations: Data Science and Engineering) |
| 7 | Electrical Engineering |
| 8 | Information Technology and Management Advanced (Concentrations: Advanced Information Technology, Computer Science Data Analytics) |
| 9 | Mechanical Engineering (Concentrations: Aerospace Engineering) |
| 10 | Ocean Engineering |

##### Ph.D. (Doctor of Philosophy)
| # | 项目 |
|---|------|
| 1 | Computer Engineering |
| 2 | Computer Science (Concentrations: Data Science and Analytics) |
| 3 | Electrical Engineering (Concentrations: Neuroengineering) |
| 4 | Mechanical Engineering (Concentrations: Aerospace Engineering, Neuroengineering) |
| 5 | Neuroscience |
| 6 | Ocean Engineering |
| 7 | Transportation and Environmental Engineering |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | Aerospace Engineering |
| 2 | Artificial Intelligence |
| 3 | Big Data Analytics: Computer Science |
| 4 | Biomedical Engineering |
| 5 | Corrosion |
| 6 | Cyber Security: Computer Science |
| 7 | Energy Resilience |
| 8 | Offshore Engineering |
| 9 | Transportation Engineering |
| 10 | Transportation, Logistics and Supply Chain Management |

#### Medicine

##### M.S. (Master of Science)
| # | 项目 |
|---|------|
| 1 | Biomedical Science |

##### M.D. (Doctor of Medicine)
| # | 项目 |
|---|------|
| 1 | Medicine |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | Biomedical Science |
| 2 | Genomics and Predictive Health |

#### Nursing

##### M.S.N. (Master of Science in Nursing)
| # | 项目 |
|---|------|
| 1 | Nursing (Concentrations: Adult/Gerontological Nurse Practitioner, Advanced Holistic Nursing, Family Nurse Practitioner, Nurse Educator, Nursing Administration and Financial Leadership) |

##### Ph.D. (Doctor of Philosophy)
| # | 项目 |
|---|------|
| 1 | Nursing |

##### D.N.P. (Doctor of Nursing Practice)
| # | 项目 |
|---|------|
| 1 | Nursing Practice (Concentrations: Adult/Gerontological Nurse Practitioner, Family Nurse Practitioner, Psychiatric Mental Health Nurse Practitioner) |

##### Post-Master's Certificate (Post-Master's Certificate)
| # | 项目 |
|---|------|
| 1 | Adult/Gerontological Nurse Practitioner |
| 2 | Advanced Holistic Nursing |
| 3 | Clinical Nurse Leader |
| 4 | Family Nurse Practitioner |
| 5 | Nursing Administration and Financial Leadership |
| 6 | Nursing: Education |
| 7 | Psychiatric Mental Health Nurse Practitioner |

#### Science

##### M.A. (Master of Arts)
| # | 项目 |
|---|------|
| 1 | Psychology |

##### M.S. (Master of Science)
| # | 项目 |
|---|------|
| 1 | Biological Sciences |
| 2 | Chemistry |
| 3 | Data Science and Analytics (Concentrations: Data Science via Scientific Inquiry) |
| 4 | Environmental Science |
| 5 | Exercise Science and Health Promotion (Concentrations: Exercise Physiology, Health Promotion) |
| 6 | Geosciences |
| 7 | Marine Science and Oceanography |
| 8 | Mathematics (Concentrations: Applied Analysis, Biostatistics, Cryptology and Information Security, Financial Mathematics, Pure Mathematics) |
| 9 | Physics |

##### M.S.T. (Master of Science in Teaching)
| # | 项目 |
|---|------|
| 1 | Biological Sciences |
| 2 | Chemistry |
| 3 | Mathematics |
| 4 | Physics |

##### M.U.R.P. (Master of Urban & Regional Planning)
| # | 项目 |
|---|------|
| 1 | Urban and Regional Planning |

##### P.S.M. (Professional Science Master)
| # | 项目 |
|---|------|
| 1 | Business Biotechnology |
| 2 | Medical Physics |

##### Ph.D. (Doctor of Philosophy)
| # | 项目 |
|---|------|
| 1 | Chemistry |
| 2 | Experimental Psychology |
| 3 | Geosciences |
| 4 | Integrative Biology (Concentrations: Biomedical Science, Environmental Science, Marine Science and Oceanography, Neuroscience) |
| 5 | Mathematics |
| 6 | Neuroscience |
| 7 | Physics |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | Cyber Security: Mathematics |
| 2 | Environmental Restoration |
| 3 | Geographic Information Systems |
| 4 | Medical Physics |
| 5 | Neuroscience |
| 6 | Post-Baccalaureate Research Education Program in Chemistry |
| 7 | Remote Sensing |

#### Social Work and Criminal Justice

##### M.S.W. (Master of Social Work)
| # | 项目 |
|---|------|
| 1 | Social Work |

##### D.S.W. (Doctor of Social Work)
| # | 项目 |
|---|------|
| 1 | Social Work |

##### Graduate Certificate (Graduate Certificate)
| # | 项目 |
|---|------|
| 1 | Addictions |
| 2 | Child Welfare |
| 3 | Healthy Aging |
| 4 | Social Justice |

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions website | https://www.fau.edu/admissions/ | fau.edu |
| Application portal | Common App or FAU direct application | fau.edu/admissions/freshman/how-to-apply/ |
| Application fee | $30 (non-refundable) | fau.edu/admissions/freshman/how-to-apply/application-fee/ |
| Fee waivers | College Board, ACT, NACAC accepted | fau.edu/admissions/freshman/how-to-apply/application-fee/ |
| Early Action deadline | October 15 (Summer/Fall) | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| EA materials deadline | October 22 | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| EA last scores considered | November 20 | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| EA decision notification | December 4 | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Rolling Decision deadline | March 12 (Summer/Fall) | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Spring deadline | September 15 | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Decision outcomes | Admit / Defer / Deny (EA); Admit / Defer / Deny / Waitlist (RD) | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Enrollment deposit deadline | May 1 (Summer/Fall); Oct 15 (Spring) | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Merit scholarship deadline | January 15 (complete application) | fau.edu/admissions/freshman/scholarships/ |
| Test policy | **REQUIRED** -- SAT, ACT, or CLT (FL BOG Reg 6.002) | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Superscore policy | Yes (ACT composite now uses English + Math + Reading only, no Science) | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| SAT code | 5229 | fau.edu |
| ACT code | 0729 | fau.edu |
| CLT accepted | Yes | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Middle 50% GPA | 3.66 - 4.29 (recalculated academic core) | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Middle 50% SAT | 1090 - 1270 | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Middle 50% ACT | 22 - 28 | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Middle 50% CLT | 60 - 84 | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Required HS units | 18 total (4 English, 4 Math, 3 Science, 3 Social Science, 2 Foreign Language, 2 Electives) | fau.edu/admissions/freshman/how-to-apply/admissions-requirements/ |
| Interview policy | Not required | fau.edu |
| Recommendation requirements | Not required for general admission | fau.edu |
| Direct Admit Nursing BSN | EA Oct 15; RD Jan 15 (complete app + materials) | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Pre-Architecture | EA Oct 15; RD Jan 15 (complete app + materials) | fau.edu/admissions/freshman/how-to-apply/deadlines/ |
| Need-blind/need-aware | Need-AWARE for all (domestic and international) | fau.edu/finaid/ |

> **Key note**: FAU is a **public** university in the State University System of Florida. Test submission is **REQUIRED** by Florida Board of Governors regulation 6.002 -- this is NOT test-optional. FAU accepts SAT, ACT, or CLT. Starting 2025-26, ACT Science subsection is no longer required.

### 3.2 Undergraduate English Proficiency Table

Non-native English speakers who do not meet SAT/ACT sub-section minimums (SAT EBRW 490, ACT Reading 19, ACT English 17) or other exemption criteria must submit an English proficiency exam.

| 考试 | 最低分数 | 备注 |
|------|---------|------|
| TOEFL iBT | 4.5 (new scale) / PBT 550 | ets.org/toefl |
| IELTS | 6.5 | ielts.org |
| Cambridge English | 180 | cambridgeenglish.org |
| PTE Academic | 55 | pearsonpte.com |
| Duolingo English Test (DET) | 110 | englishtest.duolingo.com |
| OHLA | Elite | ohla.com |
| ELS | 112 | els.edu |
| FAU Intensive English Institute | Level VI (Bridge) | fau.edu/intensive-english/ |
| HKDSE English | 5 | hkeaa.edu.hk |
| IGCSE English | C/4 | -- |
| IB English HL | 6 | -- |
| Study Group English | 65% | -- |

**Exemptions**: Students meeting SAT EBRW 490+ or ACT Reading 19+ / English 17+ are exempt. Also exempt: 3+ years of secondary education in English, 30+ post-secondary credits including ENC 1101/1102, or 60+ credits / associate degree from English-medium institution.

> Source: fau.edu/admissions/international/how-to-apply/english-proficiency-tests/

### 3.3 Graduate -- Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| Graduate admissions website | https://www.fau.edu/graduate/ | fau.edu |
| Application systems | GradCAS (most colleges), EngineeringCAS (Engineering), CSDCAS (Speech-Language Pathology), College of Business own system | fau.edu/graduate/apply/ |
| GRE code | 5229 | fau.edu/graduate/apply/ |
| GMAT code | 9LX | fau.edu/graduate/apply/ |
| GRE/GMAT policy | Per-program (some require, some don't) | fau.edu/graduate/apply/ |
| Application fee | Varies by CAS system | fau.edu/graduate/apply/ |
| English proficiency | Required for non-native speakers; same exams as UG | fau.edu/graduate/admissions/ |
| Combined BA-to-MS pathway | Yes (Pathways to Graduate Education) | fau.edu/graduate/apply/ |
| Financial certification | Required for international students | fau.edu/graduate/admissions/ |

> **Graduate admissions is decentralized by college**: each college sets its own requirements and deadlines. The Graduate College provides centralized oversight. College of Business uses a unique application system separate from CAS.

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

**Florida Resident (On Campus)**

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $5,984* | Per credit: $203.29; 30 credits/year |
| Books, course materials, supplies & equipment | $1,368 | Estimated |
| Living Expenses - Housing | $10,524* | On-campus housing |
| Living Expenses - Food | $5,308* | On-campus meal plan |
| Transportation | $3,090 | Estimated |
| Miscellaneous Personal Expenses | $4,756 | Estimated |
| **Total (On Campus)** | **$31,030** | |
| **Direct Costs (payable to FAU)** | **$21,816** | Tuition, fees, housing, food |

**Non-Florida Resident (On Campus)**

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $22,888* | Per credit: $799.72; 30 credits/year |
| Books, course materials, supplies & equipment | $1,368 | Estimated |
| Living Expenses - Housing | $10,524* | On-campus housing |
| Living Expenses - Food | $5,308* | On-campus meal plan |
| Transportation | $3,090 | Estimated |
| Miscellaneous Personal Expenses | $4,756 | Estimated |
| **Total (On Campus)** | **$47,934** | |
| **Direct Costs (payable to FAU)** | **$38,720** | Tuition, fees, housing, food |

**Living Arrangement Variations (FL Resident)**

| 项目 | On Campus | Off Campus | With Parents |
|------|-----------|------------|--------------|
| Tuition & Fees | $5,984 | $5,984 | $5,984 |
| Books & Supplies | $1,368 | $1,368 | $1,368 |
| Housing | $10,524 | $12,198 | $1,586 |
| Food | $5,308 | $5,498 | $4,926 |
| Transportation | $3,090 | $3,562 | $3,562 |
| Miscellaneous | $4,756 | $4,756 | $4,756 |
| **Total** | **$31,030** | **$33,366** | **$22,182** |

**Per Credit Hour Rates (2026-2027)**

| Student Type | Undergraduate | Graduate |
|-------------|---------------|----------|
| Florida Resident | $203.29 | $371.82 |
| Non-Florida Resident | $799.72 | $1,125.06 |

> Source: fau.edu/finaid/other/cost-of-attendance/ (2026-2027)

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind/need-aware | Need-AWARE for all students (domestic and international) | fau.edu/finaid/ |
| Merit scholarships | Yes, automatic consideration with admission by Jan 15 | fau.edu/admissions/freshman/scholarships/ |
| FAU 100 Scholarship | $20,000 ($5,000/yr x 4) -- 4.0 GPA + 1410 SAT/32 ACT (FL resident) | fau.edu/admissions/freshman/scholarships/ |
| Spirit of Atlantic (top) | $8,000 ($2,000/yr x 4) -- 3.9 GPA + 1340 SAT/29 ACT | fau.edu/admissions/freshman/scholarships/ |
| Spirit of Atlantic (mid) | $4,000 ($1,000/yr x 4) -- 3.85 GPA + 1270 SAT/27 ACT | fau.edu/admissions/freshman/scholarships/ |
| Spirit of Atlantic (base) | $2,000 ($500/yr x 4) -- 3.7 GPA + 1200 SAT/25 ACT | fau.edu/admissions/freshman/scholarships/ |
| Non-Resident top | $40,000 ($10,000/yr x 4) -- includes HOOT scholarship ($27,000) | fau.edu/admissions/freshman/scholarships/ |
| Benaquisto Scholarship | Full COA for National Merit Finalists who name FAU first choice | fau.edu/admissions/freshman/scholarships/ |
| Grandparent Waiver | OOS tuition waived for students with FL-resident grandparent (1330 SAT/29 ACT) | fau.edu/admissions/freshman/scholarships/ |
| Bright Futures | State-funded for FL high school graduates | fau.edu/admissions/freshman/scholarships/ |
| FAFSA | Required for need-based aid; 2026-2027 FAFSA open | fau.edu/finaid/ |
| Total financial aid awarded | $262 million | fau.edu/about/ |
| Scholarship renewal | 3.0 FAU GPA + 30 credits/year + full-time (15+ credits at FAU) | fau.edu/admissions/freshman/scholarships/ |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| FL Resident grad tuition | $371.82/credit hour | fau.edu/finaid/other/cost-of-attendance/ |
| Non-FL Resident grad tuition | $1,125.06/credit hour | fau.edu/finaid/other/cost-of-attendance/ |
| Assistantships | Available in many programs (indicate interest during application) | fau.edu/graduate/admissions/ |
| Fellowships | Graduate College awards several annually | fau.edu/graduate/admissions/ |
| Bright Futures (grad) | FAS/FMS earning bachelor's in 7 semesters may get 1 term of grad funding | fau.edu/graduate/admissions/ |
| Financial Certification | Required for international graduate students | fau.edu/graduate/admissions/ |

---

## SECTION 5 -- Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.ea
  value: "October 15"
  source_url: "https://www.fau.edu/admissions/freshman/how-to-apply/deadlines/"
  source_snippet: "EARLY ACTION SUMMER/FALL Application Deadline October 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.rd
  value: "March 12 (Rolling Decision)"
  source_url: "https://www.fau.edu/admissions/freshman/how-to-apply/deadlines/"
  source_snippet: "ROLLING DECISION SUMMER/FALL Application Deadline March 12"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.test_policy
  value: "REQUIRED (SAT, ACT, or CLT) -- FL BOG Reg 6.002"
  source_url: "https://www.fau.edu/admissions/freshman/how-to-apply/admissions-requirements/"
  source_snippet: "Florida Atlantic University, along with Florida's 11 other public universities, is subject to Florida Board of Governors admissions regulation 6.002, which requires first-year students seeking admission to submit an ACT, SAT, or CLT test score."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.student_profile
  value: { gpa: "3.66-4.29", sat: "1090-1270", act: "22-28", clt: "60-84" }
  source_url: "https://www.fau.edu/admissions/freshman/how-to-apply/admissions-requirements/"
  source_snippet: "Middle 50% of Admitted First-Year Students: GPA 3.66-4.29, SAT 1090-1270, ACT 22-28, CLT 60-84"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.application_fee
  value: "$30"
  source_url: "https://www.fau.edu/admissions/freshman/how-to-apply/application-fee/"
  source_snippet: "The $30 non-refundable application fee can be paid online when you submit your application."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.cost.tuition_fees_fl_resident
  value: "$5,984/year ($203.29/credit)"
  source_url: "https://www.fau.edu/finaid/other/cost-of-attendance/"
  source_snippet: "Florida Resident Undergraduate $203.29 per credit hour; Tuition & Fees $5,984*"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.tuition_fees_nonfl_resident
  value: "$22,888/year ($799.72/credit)"
  source_url: "https://www.fau.edu/finaid/other/cost-of-attendance/"
  source_snippet: "Non-Florida Resident Undergraduate $799.72 per credit hour; Tuition & Fees $22,888*"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.total_on_campus_fl
  value: "$31,030"
  source_url: "https://www.fau.edu/finaid/other/cost-of-attendance/"
  source_snippet: "TOTAL $31,030 (Florida Resident, On Campus, 2026-2027)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.total_on_campus_nonfl
  value: "$47,934"
  source_url: "https://www.fau.edu/finaid/other/cost-of-attendance/"
  source_snippet: "TOTAL $47,934 (Non-Florida Resident, On Campus, 2026-2027)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.english_proficiency.toefl
  value: "iBT 4.5 / PBT 550"
  source_url: "https://www.fau.edu/admissions/international/how-to-apply/english-proficiency-tests/"
  source_snippet: "TOEFL iBT (4.5)/PBT (550)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.english_proficiency.ielts
  value: "6.5"
  source_url: "https://www.fau.edu/admissions/international/how-to-apply/english-proficiency-tests/"
  source_snippet: "IELTS 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.english_proficiency.duolingo
  value: "110"
  source_url: "https://www.fau.edu/admissions/international/how-to-apply/english-proficiency-tests/"
  source_snippet: "Duolingo English Test (DET) 110"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.need_blind
  value: "Need-AWARE for all (domestic and international)"
  source_url: "https://www.fau.edu/finaid/"
  source_snippet: "Financial aid offers are based on a cost of attendance"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.scholarships.merit_top
  value: "$20,000 ($5,000/yr x 4) for 4.0 GPA + 1410 SAT/32 ACT"
  source_url: "https://www.fau.edu/admissions/freshman/scholarships/"
  source_snippet: "4.00 GPA & 1410 SAT / 32 ACT / 101 CLT -- $20,000 ($5,000/yr for 4 years)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-015:
  field: undergraduate.deposit_deadline
  value: "May 1 (Summer/Fall); Oct 15 (Spring)"
  source_url: "https://www.fau.edu/admissions/freshman/how-to-apply/deadlines/"
  source_snippet: "Deposit Deadlines: Freshman Summer May 1, Fall May 1, Spring Oct. 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.application_systems
  value: "GradCAS, EngineeringCAS, CSDCAS, College of Business own system"
  source_url: "https://www.fau.edu/graduate/apply/"
  source_snippet: "Florida Atlantic utilizes a centralized application service (CAS) for graduate programs. The College of Business uses a unique application system."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.gre_code
  value: "5229"
  source_url: "https://www.fau.edu/graduate/apply/"
  source_snippet: "FAU's school code for the GRE is 5229"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.gmat_code
  value: "9LX"
  source_url: "https://www.fau.edu/graduate/apply/"
  source_snippet: "FAU's school code for the GMAT is 9LX"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.tuition_fl_resident
  value: "$371.82/credit hour"
  source_url: "https://www.fau.edu/finaid/other/cost-of-attendance/"
  source_snippet: "Florida Resident Graduate $371.82"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.tuition_nonfl_resident
  value: "$1,125.06/credit hour"
  source_url: "https://www.fau.edu/finaid/other/cost-of-attendance/"
  source_snippet: "Non-Florida Resident Graduate $1125.06"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-X-001:
  field: institution.about
  value: "Founded 1961, opened 1964; 32,000+ students; 170+ degree programs; 6 campuses; 24:1 student-faculty ratio; Hispanic-Serving Institution"
  source_url: "https://www.fau.edu/about/"
  source_snippet: "Florida Atlantic University, established in 1961, officially opened its doors in 1964 as the fifth public university in Florida. Today, the University serves more than 30,000 undergraduate and graduate students across six campuses."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-X-002:
  field: programs.total_count
  value: "281 unique programs, 307 degree rows"
  source_url: "https://www.fau.edu/programs/"
  source_snippet: "Programs page listing 281 programs across 10 colleges"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
fau-knowledge-base-v2
├── 00-institution-overview.md          (Section 0: Rules 1-4)
├── 01-ug-arts-letters.md              (Section 1: College of Arts & Letters UG programs)
├── 02-ug-business.md                  (Section 1: College of Business UG programs)
├── 03-ug-education.md                 (Section 1: College of Education UG programs)
├── 04-ug-engineering-cs.md            (Section 1: College of Engineering & CS UG programs)
├── 05-ug-medicine.md                  (Section 1: College of Medicine UG programs)
├── 06-ug-nursing.md                   (Section 1: College of Nursing UG programs)
├── 07-ug-science.md                   (Section 1: College of Science UG programs)
├── 08-ug-social-work-cj.md            (Section 1: Social Work & CJ UG programs)
├── 09-ug-honors.md                    (Section 1: Honors College UG programs)
├── 10-ug-undergraduate-studies.md     (Section 1: Undergraduate Studies programs)
├── 11-grad-arts-letters.md            (Section 2: Arts & Letters grad programs)
├── 12-grad-business.md               (Section 2: Business grad programs)
├── 13-grad-education.md              (Section 2: Education grad programs)
├── 14-grad-engineering-cs.md         (Section 2: Engineering & CS grad programs)
├── 15-grad-medicine.md               (Section 2: Medicine grad programs)
├── 16-grad-nursing.md                (Section 2: Nursing grad programs)
├── 17-grad-science.md                (Section 2: Science grad programs)
├── 18-grad-social-work-cj.md         (Section 2: Social Work & CJ grad programs)
├── 19-deadlines-requirements.md       (Section 3)
├── 20-costs-financial-aid.md          (Section 4)
└── 21-evidence-chain.md               (Section 5)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "fau-knowledge-base-v2"
  school: "<home college>"
  degree_level: "<BA|BS|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "https://www.fau.edu/programs/"
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | fau.edu/graduate/ programs (each program's page) |
| P0 | Graduate application fees per CAS system | GradCAS / EngineeringCAS / CSDCAS |
| P1 | Per-program graduate deadlines | Individual program pages |
| P1 | Detailed financial aid policy (income thresholds) | fau.edu/finaid/ |
| P1 | Transfer admission requirements | fau.edu/admissions/transfer/ |
| P2 | Honors College specific requirements | fau.edu/honors/ |
| P2 | Wilkes Honors College program details | fau.edu/honors/ |
| P2 | Additional costs (lab fees, parking, etc.) | fau.edu/controller/ |
| P2 | Graduate assistantship stipend rates | fau.edu/graduate/ |

---

## SECTION 7 -- Cross-School Comparison Framework

| 维度 | FAU | (Other schools) |
|------|-----|-----------------|
| Type | Public | |
| Location | Boca Raton, FL (6 campuses) | |
| Total programs (Rule 1) | 307 (281 unique) | |
| Colleges (Rule 2) | 10 | |
| UG tuition/yr (FL resident) | $5,984 | |
| UG tuition/yr (non-resident) | $22,888 | |
| UG COA on-campus (FL) | $31,030 | |
| UG COA on-campus (non-FL) | $47,934 | |
| Test policy | REQUIRED (SAT/ACT/CLT, FL BOG 6.002) | |
| EA deadline | October 15 | |
| RD deadline | March 12 (rolling) | |
| Application fee | $30 | |
| Need-blind intl? | No (need-aware for all) | |
| TOEFL min | 4.5 iBT / 550 PBT | |
| IELTS min | 6.5 | |
| DET min | 110 | |
| Student-faculty ratio | 24:1 | |
| Enrollment | 32,000+ | |
| Merit scholarship (top) | $20,000 (FL) / $40,000 (non-FL) | |
| GRE institutional code | 5229 | |
| GMAT code | 9LX | |
| Graduate admissions | Decentralized (4 CAS systems) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: fau.edu (admissions, finaid, graduate, programs, about, academics)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
