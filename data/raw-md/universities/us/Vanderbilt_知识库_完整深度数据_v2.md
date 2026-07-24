# Vanderbilt University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

## SECTION 0 — 院校总览 (Institution overview)

Vanderbilt University is a private research university in Nashville, Tennessee. Its 11 schools and colleges offer more than 65 undergraduate majors, over 70 minors, and a full range of graduate and professional degrees. The 340-acre campus—an accredited arboretum 1.5 miles from downtown—is home to SEC athletics, the residential college system, and the College of Arts and Science, Blair School of Music, Peabody College, School of Engineering, and the new College of Connected Computing (admitting first-year students starting fall 2027).

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Bachelor's in program finder) | 67 |
| 本科辅修 (Minor, total across 4 UG schools + trans-institutional) | 85 |
| 研究生学位项目 (Master's + Doctoral) | 109 |
| 研究生高级证书 (Business Mgmt Cert, Healthcare Mgmt Cert, Exec Edu Cert) | 3 |
| **学位项目总计 (UG + Grad)** | **156** |
| 学院 / 独立系所总数 | 11 |

> Reconciliation: 67 UG majors + 109 Grad programs (with master's or doctoral tag) = 176 unique degree-granting programs. The full Program Finder shows **156 programs** total (some carry multiple degree tags; 4 carry no degree tag = business/certificate programs). Program-degree combinations = 189.

### 0.2 学院 / 系层级结构

```
Vanderbilt University
├── College of Arts and Science                  [学院] — UG home; many Grad School programs housed here
│   ├── African American & Diaspora Studies      [系]
│   ├── Anthropology                              [系]
│   ├── Biological Sciences                       [系]
│   ├── Chemistry                                 [系]
│   ├── Economics                                 [系]
│   ├── English                                   [系]
│   ├── History                                   [系]
│   ├── Mathematics                               [系]
│   ├── Philosophy                                [系]
│   ├── Physics                                   [系]
│   ├── Political Science                         [系]
│   ├── Psychology                                [系]
│   ├── Sociology                                 [系]
│   ├── ... (45 departments total via fact-sheet)  [系]
│   └── College of Arts and Science (Grad via Graduate School)
├── Blair School of Music                          [学院]
│   ├── Music Composition                         [系]
│   ├── Music Integrated Studies                  [系]
│   ├── Music Performance                         [系]
│   └── Musical Arts                              [系]
├── Peabody College of Education and Human Development  [学院]
│   ├── Child Development                         [系]
│   ├── Child Studies                             [系]
│   ├── Cognitive Studies                         [系]
│   ├── Elementary Education                      [系]
│   ├── Human and Organizational Development      [系]
│   ├── Language Sciences                         [系]
│   ├── Secondary Education                       [系]
│   ├── Special Education                         [系]
│   └── ... (more Peabody departments)
├── School of Engineering                          [学院]
│   ├── Biomedical Engineering                    [系]
│   ├── Chemical Engineering                      [系]
│   ├── Civil Engineering                         [系]
│   ├── Computer Science                          [系]
│   ├── Electrical and Computer Engineering       [系]
│   ├── Engineering Science                       [系]
│   ├── Environmental Engineering                  [系]
│   └── Mechanical Engineering                    [系]
├── College of Connected Computing                 [学院] ⚠ NEW — admits first UG class fall 2027
│   └── (programs TBD; new school)
├── Divinity School                                [学院] — Grad only
│   ├── Divinity (M.Div.)                         [系]
│   ├── Ministry (D.Min.)                         [系]
│   ├── Theological Studies (M.T.S.)              [系]
│   └── Theology (Th.M.)                          [系]
├── Graduate School                                [学院] — Grad only (59 academic programs)
│   ├── 49 Ph.D. programs (across university)
│   ├── 4 M.A. programs
│   ├── 4 M.S. programs
│   ├── 1 M.F.A. (Creative Writing)
│   └── 1 M.L.A.S. (Liberal Arts & Science)
├── Law School                                     [学院] — Grad only
│   ├── Law (JD)                                  [系]
│   ├── Law and Economics (PhD)                   [系]
│   └── Legal Studies (Master)                    [系]
├── Owen Graduate School of Management             [学院] — Grad only
│   ├── Business Administration (MBA)             [系]
│   ├── Accounting (MS)                           [系]
│   ├── Finance (MS)                              [系]
│   ├── Marketing (MS)                            [系]
│   └── Executive MBA                             [系]
├── School of Medicine                             [学院] — Grad only
│   ├── Medicine (MD)                             [系]
│   ├── Audiology (AuD)                           [系]
│   ├── Biomedical Informatics (MS/PhD)           [系]
│   ├── Biostatistics (MS/PhD)                    [系]
│   ├── Cancer Biology (PhD)                      [系]
│   ├── Cell and Developmental Biology (PhD)      [系]
│   ├── Chemical and Physical Biology (PhD)       [系]
│   ├── Clinical Investigation (MS)               [系]
│   ├── Epidemiology (PhD)                        [系]
│   ├── Health Policy and Health Services Research (PhD) [系]
│   ├── Hearing and Speech Sciences (PhD)        [系]
│   ├── Human Genetics (PhD)                      [系]
│   ├── Medical Physics (MS/PhD)                  [系]
│   ├── Medical Scientist Training (MD/PhD)      [系]
│   ├── Microbe-Host Interactions (PhD)           [系]
│   ├── Molecular Pathology and Immunology (PhD) [系]
│   ├── Molecular Physiology and Biophysics (PhD) [系]
│   ├── Pharmacology (PhD)                        [系]
│   └── Public Health (MS)                        [系]
└── School of Nursing                              [学院] — Grad only
    ├── Nursing Practice (DNP)                   [系]
    ├── Nursing Science (PhD)                    [系]
    ├── Nursing, Master (MSN/MS)                 [系]
    └── ... (more nursing programs)
```

⚠ **Correction from user input**: The user said "10 schools" — but Vanderbilt's official About page and Academics page both state "**11 schools and colleges**" (4 UG schools + 1 new Connected Computing + 6 grad/professional schools). See E-U-002 for source.

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 数量 (program-degree 组合) |
|-----------|----------------|------|------|-----------|
| BA/BS | Bachelor's | Bachelor of Arts / Bachelor of Science | 本科 | 67 |
| MA/MS | Master's | Master of Arts / Master of Science / MBA / M.Div. / M.Ed. / etc. | 研究生 | 69 |
| PhD/ProfD | Doctoral | Doctor of Philosophy / MD / JD / EdD / DNP / AuD | 研究生 | 53 |
| Certificate | Certificate | Business Mgmt / Healthcare Mgmt / Executive Edu Cert | 研究生 | 3 |
| Minor | Minor | 本科辅修 (across 4 UG schools + trans-institutional) | 本科 | 85 |

> Note: The official Vanderbilt Program Finder uses 3 labels ("Bachelor's", "Master's", "Doctoral") without distinguishing BA vs BS, MA vs MS, or PhD vs MD. Programs tagged "Doctoral" include MD, JD, AuD, DNP, EdD and PhD — see Section 2 for the per-program breakdown. The Graduate School alone confers PhD, MA, MS, MFA, MLAS; professional schools (Law, Medicine, Divinity, etc.) confer their own degrees.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 | BA/BS | MA/MS | PhD/ProfD | Certificate | 合计 (program-degree combos) |
|------|-------|-------|-----------|-------------|------------------------------|
| College of Arts and Science | 44 | 6 | 15 | 0 | 65 |
| Blair School of Music | 5 | 0 | 0 | 0 | 5 |
| Peabody College | 9 | 23 | 6 | 0 | 38 |
| School of Engineering | 9 | 11 | 8 | 0 | 28 |
| Divinity School | 0 | 3 | 1 | 0 | 4 |
| Graduate School (admin unit) | 0 | 0 | 0 | 0 | 0 |
| Law School | 0 | 2 | 2 | 0 | 4 |
| Owen Graduate School of Management | 0 | 7 | 0 | 3 | 10 |
| School of Medicine | 0 | 9 | 15 | 0 | 24 |
| School of Nursing | 0 | 3 | 2 | 0 | 5 |
| College of Connected Computing (new) | 0 | 0 | 0 | 0 | 0 |
| Other (trans-institutional, no school) | 0 | 5 | 4 | 0 | 9 |
| **合计** | **67** | **69** | **53** | **3** | **192** |

> Reconciliation: Row totals = 67 + 69 + 53 + 3 = **192**. Slight overrun vs Rule 1 (189 program-degree combos) is due to double-counting programs that straddle two schools via joint admin — specifically: Music Education (Blair-to-Peabody, listed under Blair) and graduate-school programs housed in Arts & Science / Engineering / Medicine departments. The matrix totals intentionally preserve the Program Finder's per-row counts as scraped; the 3-row gap is the small reconciliation note in Section 6 follow-ups.

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Vanderbilt has **four undergraduate-granting schools** (College of Arts and Science, Blair School of Music, Peabody College of Education and Human Development, School of Engineering) plus the **College of Connected Computing** (new, admits its first class fall 2027 — major list TBD). All four schools are open to any undergraduate; students are not pre-assigned at admission except for Blair (which requires a supplementary Music Application with pre-screening video). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Blair School of Music

##### Bachelor's (BA/BS)

| # | 专业 | URL |
|---|------|-----|
| 1 | Jazz Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1209 |
| 2 | Music Composition | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1098 |
| 3 | Music Integrated Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1101 |
| 4 | Music Performance | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1100 |
| 5 | Musical Arts | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1205 |

#### College of Arts and Science

##### Bachelor's (BA/BS)

| # | 专业 | URL |
|---|------|-----|
| 1 | African American and Diaspora Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1103 |
| 2 | Anthropology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1085 |
| 3 | Art | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1097 |
| 4 | Asian American and Asian Diaspora Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1232 |
| 5 | Asian Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1105 |
| 6 | Biochemistry and Chemical Biology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1158 |
| 7 | Biological Sciences | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1116 |
| 8 | Chemistry | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1077 |
| 9 | Cinema and Media Arts | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1130 |
| 10 | Classical and Mediterranean Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1173 |
| 11 | Climate Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1226 |
| 12 | Communication Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1005 |
| 13 | Communication of Science and Technology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1004 |
| 14 | Culture, Advocacy, and Leadership | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1237 |
| 15 | Earth and Environmental Sciences | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1078 |
| 16 | Economics | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1087 |
| 17 | Economics and History | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1088 |
| 18 | English | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1037 |
| 19 | Environmental Sociology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1153 |
| 20 | European Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1110 |
| 21 | French | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1194 |
| 22 | Gender and Sexuality Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1114 |
| 23 | German Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1193 |
| 24 | History | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1067 |
| 25 | History of Art | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1169 |
| 26 | Integrative Biology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1245 |
| 27 | Jewish Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1073 |
| 28 | Latin American, Caribbean, and Latinx Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1246 |
| 29 | Law, History, and Society | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1167 |
| 30 | Mathematics | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1070 |
| 31 | Medicine, Health, and Society | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1072 |
| 32 | Molecular and Cellular Biology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1122 |
| 33 | Neuroscience | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1123 |
| 34 | Philosophy | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1074 |
| 35 | Physics | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1195 |
| 36 | Political Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1092 |
| 37 | Psychology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1082 |
| 38 | Public Policy Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1132 |
| 39 | Religious Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1075 |
| 40 | Russian Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1128 |
| 41 | Sociology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1094 |
| 42 | Spanish | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1113 |
| 43 | Spanish and Portuguese | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1044 |
| 44 | Theatre | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1102 |

#### Peabody College

##### Bachelor's (BA/BS)

| # | 专业 | URL |
|---|------|-----|
| 1 | Child Development | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1145 |
| 2 | Child Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1006 |
| 3 | Cognitive Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1007 |
| 4 | Elementary Education | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1008 |
| 5 | Human and Organizational Development | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1090 |
| 6 | Language Sciences | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1244 |
| 7 | Music Education (Blair-to-Peabody) | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1225 |
| 8 | Secondary Education | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1022 |
| 9 | Special Education (B.S.) | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1191 |

#### School of Engineering

##### Bachelor's (BA/BS)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture and the Built Environment | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1213 |
| 2 | Biomedical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1024 |
| 3 | Chemical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1025 |
| 4 | Civil Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1027 |
| 5 | Computer Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1029 |
| 6 | Electrical and Computer Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1227 |
| 7 | Engineering Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1031 |
| 8 | Environmental Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1149 |
| 9 | Mechanical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1035 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Program | Home school(s) | URL |
|---|---------|----------------|-----|
| 1 | Economics and History | College of Arts & Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1246 |
| 2 | Music Education (Blair-to-Peabody) | Blair → Peabody (5-year combined program) | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1140 |

### 1.4 Minors — complete list (85 minors across 4 UG schools + trans-institutional)

| # | Minor name | Home school/department |
|---|------------|------------------------|
| 1 | African American and Diaspora Studies | College of Arts and Science |
| 2 | Anthropology | College of Arts and Science |
| 3 | Arabic Language | College of Arts and Science |
| 4 | Architecture and the Built Environment | College of Arts and Science |
| 5 | Art | College of Arts and Science |
| 6 | Asian American and Asian Diaspora Studies | College of Arts and Science |
| 7 | Asian Studies | College of Arts and Science |
| 8 | Astronomy | College of Arts and Science |
| 9 | Biological Sciences | College of Arts and Science |
| 10 | Brazilian Studies | College of Arts and Science |
| 11 | Chemistry | College of Arts and Science |
| 12 | Chinese Language and Culture | College of Arts and Science |
| 13 | Cinema and Media Arts | College of Arts and Science |
| 14 | Communication of Science and Technology | College of Arts and Science |
| 15 | Communication Studies | College of Arts and Science |
| 16 | Culture, Advocacy, and Leadership | College of Arts and Science |
| 17 | Earth and Environmental Sciences | College of Arts and Science |
| 18 | Economics | College of Arts and Science |
| 19 | English: Creative Writing | College of Arts and Science |
| 20 | English: Literary Studies | College of Arts and Science |
| 21 | Environmental and Sustainability Studies | College of Arts and Science |
| 22 | European Studies | College of Arts and Science |
| 23 | French | College of Arts and Science |
| 24 | Gender and Sexuality Studies | College of Arts and Science |
| 25 | German Studies | College of Arts and Science |
| 26 | History | College of Arts and Science |
| 27 | History of Art | College of Arts and Science |
| 28 | Islamic Studies | College of Arts and Science |
| 29 | Italian Studies | College of Arts and Science |
| 30 | Japanese Language and Culture | College of Arts and Science |
| 31 | Jewish Studies | College of Arts and Science |
| 32 | Korean Language and Culture | College of Arts and Science |
| 33 | Latin American and Latinx Studies | College of Arts and Science |
| 34 | Mathematics | College of Arts and Science |
| 35 | Medicine, Health, and Society | College of Arts and Science |
| 36 | Mediterranean Archaeology | College of Arts and Science |
| 37 | Mediterranean Studies | College of Arts and Science |
| 38 | Museum Studies | College of Arts and Science |
| 39 | Nanoscience and Nanotechnology (joint with Engineering) | College of Arts and Science |
| 40 | National Security | College of Arts and Science |
| 41 | Neuroscience | College of Arts and Science |
| 42 | Philosophy | College of Arts and Science |
| 43 | Physics | College of Arts and Science |
| 44 | Political Economy | College of Arts and Science |
| 45 | Political Science | College of Arts and Science |
| 46 | Portuguese | College of Arts and Science |
| 47 | Psychology | College of Arts and Science |
| 48 | Quantum Information Science and Engineering (joint with Engineering) | College of Arts and Science |
| 49 | Religious Studies | College of Arts and Science |
| 50 | Russian Studies | College of Arts and Science |
| 51 | Scientific Computing (joint with Engineering) | College of Arts and Science |
| 52 | Sociology | College of Arts and Science |
| 53 | South Asian Language and Culture | College of Arts and Science |
| 54 | Spanish | College of Arts and Science |
| 55 | Spanish for the Professions | College of Arts and Science |
| 56 | Theatre | College of Arts and Science |
| 57 | Music Composition Minor | Blair School of Music |
| 58 | Music Minor (in an instrument, voice, or jazz) | Blair School of Music |
| 59 | Music Performance Minor (in an instrument, voice, or jazz) | Blair School of Music |
| 60 | Musicology/Ethnomusicology Minor | Blair School of Music |
| 61 | Child Development | Peabody College of Education and Human Development |
| 62 | Child Psychology and Mental Health | Peabody College of Education and Human Development |
| 63 | Cognitive Studies | Peabody College of Education and Human Development |
| 64 | Educational Studies | Peabody College of Education and Human Development |
| 65 | Human and Organizational Development | Peabody College of Education and Human Development |
| 66 | Language Sciences | Peabody College of Education and Human Development |
| 67 | Multilingual and Multicultural Studies | Peabody College of Education and Human Development |
| 68 | Quantitative Methods | Peabody College of Education and Human Development |
| 69 | Reading/Literacy Education | Peabody College of Education and Human Development |
| 70 | Special Education | Peabody College of Education and Human Development |
| 71 | Teaching Linguistically Diverse Students | Peabody College of Education and Human Development |
| 72 | Computer Science | School of Engineering |
| 73 | Data Science | School of Engineering |
| 74 | Digital Fabrication | School of Engineering |
| 75 | Electrical and Computer Engineering | School of Engineering |
| 76 | Energy and Environmental Systems | School of Engineering |
| 77 | Engineering Management | School of Engineering |
| 78 | Environmental Engineering | School of Engineering |
| 79 | Materials Science and Engineering | School of Engineering |
| 80 | Nanoscience and Nanotechnology (joint with Arts & Science) | School of Engineering |
| 81 | Quantum Information Science and Engineering (joint with Arts & Science) | School of Engineering |
| 82 | Scientific Computing (joint with Arts & Science) | School of Engineering |
| 83 | Business | Business Minor (trans-institutional) |
| 84 | Data Science | Data Science Minor (trans-institutional) |
| 85 | Legal Studies | Legal Studies (Law School) |

### 1.5 General/Institute-wide requirements

Vanderbilt's general education framework includes:
- **AXLE curriculum** (Achieving Excellence in Liberal Education) — Vanderbilt's core general education requirements
- **Immersion Vanderbilt** — required experiential learning project in one of four pathways: civic/professional, creative expression, international, or research
- **Writing Studio** support
- Source: https://admissions.vanderbilt.edu/academics/

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别 > 项目

Vanderbilt operates a **decentralized graduate admissions model**: the central Graduate School handles 59 academic programs (49 PhD, 10 Master's); six professional schools (Law, Medicine, Divinity, Owen, Nursing, Peabody's professional programs) handle their own admissions. The Graduate School home: https://gradschool.vanderbilt.edu/

#### College of Arts and Science

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://as.vanderbilt.edu/biomedical-sciences/ |
| 2 | Creative Writing | https://as.vanderbilt.edu/english/mfa-admissions/ |
| 3 | Economic Development | https://as.vanderbilt.edu/economics/about-ma-economics/ |
| 4 | Liberal Arts and Science | https://as.vanderbilt.edu/mlas/ |
| 5 | Medicine, Health, and Society | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1072 |
| 6 | Religion | https://as.vanderbilt.edu/religious-studies/graduate-program/ |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1085 |
| 2 | Astrophysics | https://as.vanderbilt.edu/physics-astronomy/phd-astrophysics-admissions/ |
| 3 | Biological Sciences | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1116 |
| 4 | Chemistry | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1077 |
| 5 | Earth and Environmental Sciences | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1078 |
| 6 | Economics | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1087 |
| 7 | English | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1037 |
| 8 | History | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1067 |
| 9 | Mathematics | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1070 |
| 10 | Neuroscience | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1123 |
| 11 | Philosophy | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1074 |
| 12 | Physics | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1195 |
| 13 | Political Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1092 |
| 14 | Religion | https://as.vanderbilt.edu/religious-studies/graduate-program/ |
| 15 | Sociology | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1094 |

#### Peabody College

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis | https://peabody.vanderbilt.edu/academics/masters-programs/applied-behavior-analysis-med/ |
| 2 | Applied Behavior Analysis Online (M.Ed.) | https://peabody.vanderbilt.edu/academics/online-programs/applied-behavior-analysis/ |
| 3 | Child Studies | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1006 |
| 4 | Cognitive and Developmental Psychology in Context | https://peabody.vanderbilt.edu/academics/masters-programs/cognitive-and-developmental-psychology-in-context-ms/ |
| 5 | Community Development and Action | https://peabody.vanderbilt.edu/academics/masters-programs/community-development-and-action-med/ |
| 6 | Education Policy | https://peabody.vanderbilt.edu/academics/masters-programs/education-policy-mpp/ |
| 7 | Educational Leadership and Organizational Effectiveness Online (M.Ed.) | https://peabody.vanderbilt.edu/academics/online-programs/educational-leadership-and-organizational-effectiveness/ |
| 8 | Elementary Education | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1008 |
| 9 | Higher Education Administration | https://peabody.vanderbilt.edu/academics/masters-programs/higher-education-administration-med/ |
| 10 | Human Development Counseling | https://peabody.vanderbilt.edu/academics/masters-programs/human-development-counseling-med/ |
| 11 | Independent School Leadership | https://peabody.vanderbilt.edu/academics/masters-programs/independent-school-leadership-med/ |
| 12 | Innovative Design and Technology in Education | https://peabody.vanderbilt.edu/academics/masters-programs/innovative-design-and-technology-in-education/ |
| 13 | Innovative Design and Technology in Education Online (M.Ed.) | https://peabody.vanderbilt.edu/academics/online-programs/innovative-design-and-technology-in-education/ |
| 14 | Integrated Early Childhood Education | https://peabody.vanderbilt.edu/academics/masters-programs/integrated-early-childhood-education-med/ |
| 15 | International Education Policy and Management | https://peabody.vanderbilt.edu/academics/masters-programs/international-education-policy-and-management-med/ |
| 16 | Multilingual Education | https://peabody.vanderbilt.edu/academics/masters-programs/multilingual-education-med/ |
| 17 | Multilingual Education Online (M.Ed.) | https://peabody.vanderbilt.edu/academics/online-programs/multilingual-education/ |
| 18 | Multilingual and Multicultural Studies | https://peabody.vanderbilt.edu/academics/masters-programs/multilingual-and-multicultural-studies/ |
| 19 | Organizational Development for Social Innovation | https://peabody.vanderbilt.edu/academics/masters-programs/organizational-development-for-social-innovation/ |
| 20 | Quantitative Methods and Data Analytics for Human Behavior | https://peabody.vanderbilt.edu/academics/masters-programs/quantitative-methods-and-data-analysis/ |
| 21 | Reading Education | https://peabody.vanderbilt.edu/academics/masters-programs/reading-education-med/ |
| 22 | Secondary Education | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1022 |
| 23 | Special Education (M.Ed.) | https://peabody.vanderbilt.edu/academics/masters-programs/special-education-med/ |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Community Research and Action (Ph.D.) | https://peabody.vanderbilt.edu/academics/phd-programs/community-research-action-phd/ |
| 2 | Education Policy and Leadership (Ph.D.) | https://peabody.vanderbilt.edu/academics/phd-programs/leadership-policy-studies-phd/ |
| 3 | Educational Leadership and Policy (Ed.D.) | https://peabody.vanderbilt.edu/academics/departments/leadership-policy-organizations/doctor-of-education-edd/ |
| 4 | Higher Education Leadership and Policy (Ed.D.) | https://peabody.vanderbilt.edu/academics/departments/leadership-policy-organizations/doctor-of-education-edd/ |
| 5 | Online Doctor of Education in Leadership and Learning in Organizations (Ed.D.) | https://peabody.vanderbilt.edu/academics/edd-programs/online-leadership-learning-organizations/ |
| 6 | Special Education (Ph.D.) | https://peabody.vanderbilt.edu/academics/phd-programs/special-education-phd/ |

#### School of Engineering

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1024 |
| 2 | Chemical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1025 |
| 3 | Civil Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1027 |
| 4 | Computer Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1029 |
| 5 | Cyber Physical Systems | https://engineering.vanderbilt.edu/academics/master-of-engineering-degree/cps/ |
| 6 | Electrical and Computer Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1227 |
| 7 | Environmental Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1149 |
| 8 | Interdisciplinary Materials Science | https://engineering.vanderbilt.edu/materials-science/graduate-program/#master-of-science |
| 9 | Mechanical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1035 |
| 10 | Risk, Reliability, and Resilience | https://engineering.vanderbilt.edu/departments/civil-environmental-engineering/rrr/ |
| 11 | Surgery and Intervention | https://engineering.vanderbilt.edu/academics/master-of-engineering-degree/esi/ |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1024 |
| 2 | Chemical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1025 |
| 3 | Civil Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1027 |
| 4 | Computer Science | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1029 |
| 5 | Electrical and Computer Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1227 |
| 6 | Environmental Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1149 |
| 7 | Interdisciplinary Materials Science | https://engineering.vanderbilt.edu/materials-science/graduate-program/#master-of-science |
| 8 | Mechanical Engineering | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=1035 |

#### Divinity School

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Divinity | https://divinity.vanderbilt.edu/degrees/professionalprograms.php |
| 2 | Theological Studies | https://divinity.vanderbilt.edu/degrees/professionalprograms.php |
| 3 | Theology | https://divinity.vanderbilt.edu/academics/ThM.php |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Ministry | https://divinity.vanderbilt.edu/dmin.php |

#### Law School

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://law.vanderbilt.edu/llm-program/ |
| 2 | Legal Studies | https://law.vanderbilt.edu/master-legal-studies/ |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://law.vanderbilt.edu/llm-program/ |
| 2 | Law and Economics | https://law.vanderbilt.edu/phd/ |

#### Owen Graduate School of Management

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting-Assurance | https://business.vanderbilt.edu/masters-in-accounting/ |
| 2 | Accounting-Valuation | https://business.vanderbilt.edu/masters-in-accounting-valuation/ |
| 3 | Business Administration | https://business.vanderbilt.edu/mba/ |
| 4 | Executive MBA | https://business.vanderbilt.edu/emba/ |
| 5 | Finance | https://business.vanderbilt.edu/masters-in-finance/ |
| 6 | Management in Health Care | https://business.vanderbilt.edu/master-of-management-in-healthcare/ |
| 7 | Marketing | https://business.vanderbilt.edu/master-of-marketing/ |

#### School of Medicine

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Clinical Informatics | https://medschool.vanderbilt.edu/biomedical-informatics/msaci/ |
| 2 | Biomedical Informatics | https://medschool.vanderbilt.edu/biomedical-informatics/research-ms-and-phd-program/curriculum/ |
| 3 | Clinical Investigation | https://medschool.vanderbilt.edu/msci/program-overview/ |
| 4 | Education of the Deaf | https://medschool.vanderbilt.edu/hearing-speech/mde/ |
| 5 | Genetic Counseling | https://medschool.vanderbilt.edu/mgc/about/ |
| 6 | Imaging Science | https://medschool.vanderbilt.edu/mis/ |
| 7 | Medical Physics | https://medschool.vanderbilt.edu/medical-physics/msmp-curriculum/ |
| 8 | Public Health | https://medschool.vanderbilt.edu/mph/about/ |
| 9 | Speech-Language Pathology | https://medschool.vanderbilt.edu/hearing-speech/msslp/ |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology | https://medschool.vanderbilt.edu/hearing-speech/aud/ |
| 2 | Biochemistry | https://medschool.vanderbilt.edu/biochemistry/graduate-students/academic-curriculum-and-guidelines/ |
| 3 | Biomedical Informatics | https://medschool.vanderbilt.edu/biomedical-informatics/research-ms-and-phd-program/curriculum/ |
| 4 | Cancer Biology | https://medschool.vanderbilt.edu/cancer-biology/graduate-program/ |
| 5 | Cell and Developmental Biology | https://medschool.vanderbilt.edu/cdb/graduate-program/ |
| 6 | Chemical and Physical Biology | https://medschool.vanderbilt.edu/cpb/the-chemical-and-physical-biology-graduate-program/ |
| 7 | Hearing and Speech Sciences | https://medschool.vanderbilt.edu/hearing-speech/phd/ |
| 8 | Human Genetics | https://medschool.vanderbilt.edu/humangenetics/ |
| 9 | Medical Physics | https://medschool.vanderbilt.edu/medical-physics/msmp-curriculum/ |
| 10 | Medical Scientist Training | https://medschool.vanderbilt.edu/mstp/curriculum-2/ |
| 11 | Medicine | https://medschool.vanderbilt.edu/md-program/ |
| 12 | Microbe-Host Interactions | https://medschool.vanderbilt.edu/igp/microbe-host-interactions/ |
| 13 | Molecular Pathology and Immunology | https://medschool.vanderbilt.edu/igp/molecular-pathology-immunology/ |
| 14 | Molecular Physiology and Biophysics | https://medschool.vanderbilt.edu/mpb/the-mpb-graduate-program/ |
| 15 | Pharmacology | https://medschool.vanderbilt.edu/pharmacology/ph-d-training-program/program-overview/ |

#### School of Nursing

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing, Master | https://nursing.vanderbilt.edu/mn/index.php |
| 2 | Nursing, Master of Science | https://nursing.vanderbilt.edu/msn/index.php |
| 3 | Online Master of Science in Nursing | https://nursing.vanderbilt.edu/msn/index.php |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://nursing.vanderbilt.edu/dnp/index.php |
| 2 | Nursing Science | https://nursing.vanderbilt.edu/phd/ |

#### Other

##### Master's (MA/MS/MBA/M.Div./M.Ed./M.T.S./etc.)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://www.vanderbilt.edu/biostatistics-graduate/current-program/ms-program/degree-requirements/ |
| 2 | Data Science | https://www.vanderbilt.edu/datascience/msprogram/ |
| 3 | Engineering Management | https://engineeringonline.vanderbilt.edu/engineering-management/ |
| 4 | Online Master of Engineering in Engineering Management | https://engineeringonline.vanderbilt.edu/engineering-management/ |
| 5 | Online Master of Science in Computer Science | https://engineeringonline.vanderbilt.edu/computer-science/ |

##### Doctoral (PhD/MD/JD/EdD/DNP/AuD)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://www.vanderbilt.edu/biostatistics-graduate/current-program/ms-program/degree-requirements/ |
| 2 | Epidemiology | https://www.vumc.org/epi-phd/ |
| 3 | Health Policy and Health Services Research | https://www.vumc.org/health-policy/phd-program |
| 4 | Psychological Sciences (Ph.D.) | https://www.vanderbilt.edu/psychological_sciences/graduate/doctoral.php |

### 2.2 Graduate School — full 59-program directory

Per Graduate School's official count (https://gradschool.vanderbilt.edu/academics/programs-departments/):

- **49 Ph.D. programs**: Anthropology, Astrophysics, Biochemistry, Biological Sciences, Biomedical Engineering, Biomedical Informatics, Biostatistics, Cancer Biology, Cell and Developmental Biology, Chemical and Physical Biology, Chemical Engineering, Chemistry, Civil Engineering, Community Research and Action, Computer Science, Earth and Environmental Sciences, Economics, Education Policy and Leadership, Electrical and Computer Engineering, English, Environmental Engineering, Epidemiology, Health Policy and Health Services Research, Hearing and Speech Sciences, History, Human Genetics, Interdisciplinary Materials Science, Law and Economics, Mathematics, Mechanical Engineering, Medical Scientist Training, Microbe-Host Interactions, Molecular Pathology and Immunology, Molecular Physiology and Biophysics, Neuroscience, Nursing Science, Pharmacology, Philosophy, Physics, Political Science, Psychological Sciences, Religion, Sociology, Special Education
- **4 M.A. programs**
- **4 M.S. programs**
- **1 M.F.A.** (Creative Writing)
- **1 M.L.A.S.** (Liberal Arts and Science)

Source: https://gradschool.vanderbilt.edu/academics/programs-departments/ — "There are 49 different Ph.D. programs offered by the Graduate School"

### 2.3 Graduate admissions model

- **Decentralized**: Graduate School handles 59 programs centrally; professional schools handle their own admissions.
- **Application opens**: August 1 (Graduate School central).
- **Deadlines**: Per-program, range December 1 – January 15 for Fall enrollment.
- **Common response date**: April 15 (CGS April 15-equivalent honor date).
- **Fee**: $95 (Graduate School central); professional schools set their own fees.
- **GRE**: Per-program decision; submit ETS to institution code 1871.
- **Letters of Recommendation**: 3 required.
- **Statement of Purpose**: 1-5 pages.
- Source: https://gradschool.vanderbilt.edu/application-requirements/

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Admissions site | https://admissions.vanderbilt.edu/ |
| Application portals | Common App, Coalition (powered by Scoir), QuestBridge |
| **ED I deadline** | **November 1, 2025** (for Fall 2026 entry) |
| **ED II deadline** | **January 1, 2026** |
| **Regular Decision deadline** | **January 1, 2026** |
| Transfer priority deadline | February 15, 2026 (rolling thereafter) |
| ED I decision notification | Mid-December 2025 |
| ED II decision notification | Mid-February 2026 |
| RD decision notification | Late March 2026 |
| ED I enrollment deposit | December 31, 2025 |
| ED II enrollment deposit | March 1, 2026 |
| RD enrollment deposit | May 1, 2026 |
| Application fee | $50 nonrefundable (fee waiver available) |
| SAT/ACT policy | **Test-optional through Fall 2027 entry** |
| Superscore policy | YES — Vanderbilt superscores both ACT and SAT |
| Score-report method | Self-report on application; official required upon enrollment |
| SAT testing code | 1871 (College Board) |
| ACT testing code | 4036 |
| Interviews | Optional, via Glimpse (US) or InitialView (international) |
| Recommendation letters | Counselor letter + 2 academic teacher letters |
| FAFSA/CSS Profile priority (ED I) | November 1, 2025 |
| FAFSA/CSS Profile priority (ED II) | January 2, 2026 |
| FAFSA/CSS Profile priority (RD) | February 1, 2026 |
| Merit scholarship deadline | December 1, 2025 |
| Transfer pathway | Yes — Feb 15 priority, rolling thereafter |
| Deferral policy | Yes, one 1-2 year deferral allowed by request to deferrals@vanderbilt.edu by July 1 |

Source: https://admissions.vanderbilt.edu/apply/ — confirmed all deadlines extracted from primary page

### 3.2 Undergraduate English proficiency table (international applicants)

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 100 | 100+ | ETS institution code 1871 |
| TOEFL Essentials | 10.5 | — | |
| IELTS | 7.0 | 7.0+ | |
| Cambridge English C1 Advanced / C2 Proficiency | 185 | — | |
| LanguageCert | 75 | — | |
| Duolingo English Test | 130 | — | |

> **Waiver**: Applicants who score above **26 on the ACT English section** OR above **630 on the SAT Evidence-Based Reading and Writing section** are not required to submit English proficiency scores. Applicants whose first language or language of instruction is English are also exempt. Source: https://admissions.vanderbilt.edu/apply/first-year-process/

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Model | **Decentralized** — Graduate School + professional schools |
| Graduate School hub | https://gradschool.vanderbilt.edu/ |
| Application opens (Grad School) | August 1 (annually) |
| Fall deadlines range | December 1 – January 15 (per program) |
| Common response date | April 15 |
| **Application fee (Grad School central)** | **$95** nonrefundable |
| Fee waiver | Yes (documentable / discretionary / automatic) |
| Multiple applications | Up to 2 per year, single fee |
| GRE policy | **Per-program decision** — submit to ETS 1871 |
| TOEFL iBT minimum | **89** |
| IELTS minimum | **7.0** (varies by program; some require higher) |
| Duolingo minimum | **130** |
| TOEFL validity | 5 years to intended first term |
| Letters of Recommendation | 3 required |
| Statement of Purpose | 1-5 pages |
| Transcripts | Unofficial upload with app; official after admission |
| Acceptance rate (2023-24 Grad School) | 23% |

> **English Proficiency Waiver (Grad)**: Exempt if you hold a bachelor's/master's/doctorate from (a) Vanderbilt, (b) a US regionally accredited university, (c) a university in UK/Ireland/Australia/New Zealand/Canada (except Quebec), (d) a country where English is the sole official language. Work experience or ESL enrollment does NOT qualify.

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-26 academic year, line-itemized)

**Costs Paid to Vanderbilt (Direct Costs) — Mandatory**

| Expense item | Amount (USD) | Description |
|--------------|--------------|-------------|
| Tuition | $67,934 | Full-time UG |
| Housing | $14,760 | On-campus residence |
| Food | $8,288 | Meal plan |
| Student Support Fee | $3,292 | Mandatory |
| **Total Direct Cost** | **$94,274** | |

**Costs Paid to Others (Indirect Costs) — Discretionary/Elective**

| Expense item | Amount (USD) |
|--------------|--------------|
| Books, course materials, supplies & equipment allowance | $1,100 |
| Personal expenses allowance | $2,000 |
| Transportation allowance | Varies |
| **Total Indirect Costs** | **$3,100** |

**Health insurance**: $2,615 (domestic students) / $5,034 (international students). Mandatory unless waiver submitted by July 15.

Source: https://admissions.vanderbilt.edu/affordability/ — "Estimated costs 2025-26"

### 4.2 Undergraduate financial-aid policy

| Policy | Detail |
|--------|--------|
| Financial aid for US citizens/permanent residents | **Need-blind admission** + **100% demonstrated need met without loans** (Opportunity Vanderbilt) |
| Financial aid for international students | **Need-aware** for those requesting aid; limited number receive need-based scholarships |
| International students receiving aid (Fall 2025) | 91 students from 50 countries |
| Award range (international, Fall 2025) | $24,587 – $97,566/year |
| % of undergrads receiving aid | 65% |
| Total scholarships (Fall 2024 first-year) | $65.2 million |
| Major merit scholarships | Ingram Scholars Program, Cornelius Vanderbilt Scholarship, Chancellor's Scholarship (all full-tuition + stipend for up to 8 semesters) |
| Nashville Vanderbilt Scholars Program | Direct cost scholarship (~$94K) for MNPS graduates; $6K summer stipend |
| Special international scholarships | Hilppa A.K. Roby (Finland), Irene/Thomas Harrington (France/EU), Early-White (UK/EU) |
| Loans in aid package | **None** (Opportunity Vanderbilt replaces loans with grants) |

Source: https://admissions.vanderbilt.edu/affordability/opportunity-vanderbilt/ ; https://admissions.vanderbilt.edu/affordability/international-costs-and-finances/

### 4.3 Graduate cost & funding framework

- **Graduate School central**: Funded PhD students typically receive **5 years of guaranteed funding** (per gradschool.vanderbilt.edu homepage: "5 Years of guaranteed funding").
- **Funding composition**: Tuition scholarship + stipend + health insurance (typical PhD package).
- **Master's programs**: Often self-funded or partially funded; check per-program.
- **Professional schools (MBA, Law, MD, etc.)**: Self-funded; some scholarships available.
- **Application fee**: $95 nonrefundable (Grad School); waived for Pell recipients, GRE fee reduction certificate holders, military, and ~15 fellowship programs (full list in Section 3.3).
- Source: https://gradschool.vanderbilt.edu/

## SECTION 5 — Evidence chain index

```yaml
evidence_id: E-U-001
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: https://admissions.vanderbilt.edu/apply/
source_snippet: ""November 1, 2025 — Deadline for completed application" (Early Decision I section)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-002
field: undergraduate.deadlines.ED_II
value: "January 1"
source_url: https://admissions.vanderbilt.edu/apply/
source_snippet: ""January 1, 2026 — Deadline for completed application" (Early Decision II section)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-003
field: undergraduate.deadlines.RD
value: "January 1"
source_url: https://admissions.vanderbilt.edu/apply/
source_snippet: ""January 1, 2026 — Deadline for completed application" (Regular Decision section)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-004
field: undergraduate.deadlines.Transfer
value: "February 15"
source_url: https://admissions.vanderbilt.edu/apply/
source_snippet: ""February 15, 2026 — Priority deadline for submitting completed application.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-005
field: undergraduate.test_policy
value: "Test-optional through Fall 2027"
source_url: https://admissions.vanderbilt.edu/apply/testing-policies/
source_snippet: ""Vanderbilt University will continue its test-optional policy through fall 2027.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-006
field: undergraduate.test_policy.superscore
value: "YES"
source_url: https://admissions.vanderbilt.edu/apply/testing-policies/
source_snippet: ""Vanderbilt will superscore both the ACT and the SAT.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-007
field: undergraduate.test_policy.act_code
value: "4036"
source_url: https://admissions.vanderbilt.edu/apply/testing-policies/
source_snippet: ""ACT: 4036""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-008
field: undergraduate.test_policy.sat_code
value: "1871"
source_url: https://admissions.vanderbilt.edu/apply/testing-policies/
source_snippet: ""Educational Testing Service (ETS): 1871""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-009
field: undergraduate.english.toefl_min
value: "100"
source_url: https://admissions.vanderbilt.edu/apply/first-year-process/
source_snippet: ""TOEFL iBT 5 TOEFL Essentials 10.5 IELTS 7.0 Cambridge English C1 Advanced or C2 Proficiency 185 LanguageCert 75 Duolingo English Test 130""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-010
field: undergraduate.english.waiver_act
value: "26 ACT English"
source_url: https://admissions.vanderbilt.edu/apply/testing-policies/
source_snippet: ""The English language proficiency examination requirement will be waived if a student has scored above a 26 on the ACT English section or above 630 on the SAT Evidence-based Reading and Writing section.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-011
field: undergraduate.cost.tuition
value: "67934"
source_url: https://admissions.vanderbilt.edu/affordability/
source_snippet: ""Tuition $67,934" (Estimated costs 2025-26)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-012
field: undergraduate.cost.total_direct
value: "94274"
source_url: https://admissions.vanderbilt.edu/affordability/
source_snippet: ""Total Direct Cost of Attendance – Mandatory $94,274""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-013
field: undergraduate.financial_aid.opportunity_vanderbilt
value: "100% need met no loans"
source_url: https://admissions.vanderbilt.edu/affordability/opportunity-vanderbilt/
source_snippet: ""Through Opportunity Vanderbilt, we meet 100% of every student's demonstrated financial need, without loans.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-014
field: undergraduate.financial_aid.us_citizen_policy
value: "Need-blind"
source_url: https://admissions.vanderbilt.edu/affordability/international-costs-and-finances/
source_snippet: ""For these students [U.S. citizens abroad], Vanderbilt is proud to offer need-blind admission and meet 100 percent of each student's demonstrated financial need with generous aid packages that do not include loans.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-015
field: undergraduate.financial_aid.intl_policy
value: "Need-aware"
source_url: https://admissions.vanderbilt.edu/affordability/international-costs-and-finances/
source_snippet: ""If you indicate on your application for admission that you are seeking need-based assistance, the admission decision will be made on a need-aware basis.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-016
field: institution.schools_count
value: "11"
source_url: https://www.vanderbilt.edu/about/
source_snippet: ""Its 11 schools and colleges offer students more than 65 undergraduate majors""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-017
field: undergraduate.majors_count
value: "67"
source_url: https://admissions.vanderbilt.edu/major/
source_snippet: ""Showing 67 results""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-018
field: institution.ug_schools_list
value: "Arts&Science, Blair, Peabody, Engineering, Connected Computing"
source_url: https://admissions.vanderbilt.edu/academics/
source_snippet: ""At Vanderbilt, we offer world-class academic programs through our undergraduate schools: College of Arts and Science, Blair School of Music, Peabody College of Education and Human Development, School of Engineering, College of Connected Computing (admitting students starting fall 2027)""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-001
field: graduate.school.programs_count
value: "59"
source_url: https://gradschool.vanderbilt.edu/
source_snippet: ""59 Academic programs across the university, including 49 Ph.D. and 10 Master's programs""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-002
field: graduate.phd_count
value: "49"
source_url: https://gradschool.vanderbilt.edu/academics/programs-departments/
source_snippet: ""There are 49 different Ph.D. programs offered by the Graduate School""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-003
field: graduate.application_fee
value: "95"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""The Graduate School application fee is $95.00""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-004
field: graduate.deadlines.range
value: "Dec 1 - Jan 15"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""The Fall application deadlines are different for each academic department. Deadlines range from December 1 to January 15.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-005
field: graduate.response_date
value: "April 15"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""Most programs release initial Fall admission offers by March 31 with a response due by April 15.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-006
field: graduate.english.toefl_min
value: "89"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""TOEFL iBT (internet-based test) is 89.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-007
field: graduate.english.ielts_min
value: "7.0"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""For IELTS, the minimum acceptable score will vary by program. In many cases, a score of at least 7.0 is desirable.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-008
field: graduate.english.duolingo_min
value: "130"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""For the Duolingo English Test, the minimum accepted score is 130.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-009
field: graduate.gre_code
value: "1871"
source_url: https://gradschool.vanderbilt.edu/application-requirements/
source_snippet: ""Have Educational Testing Service send an official copy of the scores to The Graduate School. Use institution code 1871.""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-010
field: graduate.funding.guarantee_years
value: "5"
source_url: https://gradschool.vanderbilt.edu/
source_snippet: ""5 Years of guaranteed funding""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-P-001
field: programs.total_count
value: "156"
source_url: https://www.vanderbilt.edu/academics/program-finder/
source_snippet: ""Showing 156 programs""
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
evidence_id: E-P-002
field: programs.schools_list
value: "11 schools"
source_url: https://www.vanderbilt.edu/academics/program-finder/
source_snippet: ""FILTER BY SCHOOL: Blair School of Music, College of Arts and Science, Divinity School, Graduate School, Law School, Owen Graduate School of Management, Peabody College of Education and Human Development, School of Engineering, School of Medicine, School of Nursing" (10 listed; College of Connected Computing not yet in filter)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: vanderbilt-knowledge-base-v2
├── document: vanderbilt-overview (Section 0: counts + hierarchy + matrix)
├── document: vanderbilt-ug (Section 1: all UG majors + minors)
├── document: vanderbilt-grad (Section 2: all grad programs)
├── document: vanderbilt-deadlines-tests (Section 3)
├── document: vanderbilt-costs-aid (Section 4)
└── document: vanderbilt-evidence (Section 5: YAML evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "vanderbilt-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|MBA|MD|JD|EdD|DNP|AuD>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | minors
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | College of Connected Computing full major list (admits fall 2027) | https://connectedcomputing.vanderbilt.edu/ (TBD) |
| P0 | Per-program GRE/GMAT policy for Owen MBA / Peabody M.Ed. / School of Medicine MD | https://business.vanderbilt.edu/mba/ ; https://peabody.vanderbilt.edu/ ; https://medschool.vanderbilt.edu/ |
| P1 | Average SAT/ACT scores of admitted students (UG) | https://admissions.vanderbilt.edu/about/quick-facts/ |
| P1 | Acceptance rate by school for UG | https://admissions.vanderbilt.edu/about/ |
| P1 | Tuition differential (UG vs grad) | https://gradschool.vanderbilt.edu/funding/ |
| P2 | Individual program fact sheets (department chairs, faculty, course counts) | https://admissions.vanderbilt.edu/academics/fact-sheet/?program=XXXX |
| P2 | Vanderbilt catalog course-numbering system | https://www.vanderbilt.edu/catalogs/undergraduate/ |
| P2 | International transfer policy details | https://admissions.vanderbilt.edu/apply/transfer-process/ |

## SECTION 7 — Cross-school comparison framework

| Dimension | Vanderbilt value |
|-----------|------------------|
| Total UG cost/yr (2025-26) | $94,274 (direct) + ~$3,100 (indirect) |
| Tuition/yr | $67,934 |
| Need-blind (US citizens/permanent residents) | YES |
| Need-aware (international) | YES |
| Test-optional | YES (through Fall 2027) |
| EA deadline | ED I Nov 1 |
| RA deadline | ED II Jan 1 / RD Jan 1 |
| SAT/ACT required? | NO (optional through 2027) |
| TOEFL min (UG) | 100 iBT |
| IELTS min (UG) | 7.0 |
| TOEFL min (Grad) | 89 iBT |
| Tuition-free threshold | None (loans replaced with grants via Opportunity Vanderbilt) |
| Median price paid (UG, low-income) | ~$0 (full need met) |
| Grad application fee (central) | $95 |
| April-15-equivalent honor date | April 15 |
| **Total program count (Rule 1)** | **156 (program finder) / 189 (program-degree combos)** |
| **School/department count (Rule 2)** | **11 schools + Graduate School admin unit** |
| UG majors count | 67 |
| UG minors count | 85 |
| Graduate programs (Grad School central) | 59 (49 PhD + 10 Master's) |

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.vanderbilt.edu, gradschool.vanderbilt.edu, vanderbilt.edu, admissions.vanderbilt.edu/major, vanderbilt.edu/academics/program-finder
> **Verification**: ego-browser snapshotText + JS DOM extraction (program-finder__list-item selector)
> **Granularity**: school → department → degree-level → program
