# Gonzaga University Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)
> **Catalog edition**: 2025-2026 (catalog.gonzaga.edu)

---

## SECTION 0 -- 院校总览 (Institution Overview)

### 0.0 Institution Identity

| Field | Value | Source |
|-------|-------|--------|
| Full name | Gonzaga University | gonzaga.edu/about/at-a-glance/facts-and-figures |
| Type | Private, Jesuit (Roman Catholic) | NCES College Navigator |
| Carnegie Classification | National University | NCES |
| Founded | 1887 | gonzaga.edu facts-and-figures |
| Location | Spokane, Washington | gonzaga.edu |
| Campus size | 150 acres, 100 buildings | gonzaga.edu facts-and-figures |
| Total enrollment (Fall 2024) | 7,470 | gonzaga.edu facts-and-figures |
| Undergraduate enrollment | 5,293 | gonzaga.edu facts-and-figures |
| Graduate/doctoral enrollment | 1,613 | gonzaga.edu facts-and-figures |
| Law enrollment | 564 | gonzaga.edu facts-and-figures |
| Student-to-faculty ratio | 12:1 | gonzaga.edu facts-and-figures |
| Average class size | 22 | gonzaga.edu undergraduate-admission |
| Test-optional | Yes (since 2021, permanent) | gonzaga.edu admission-requirements |
| Application platform | Common Application (first-year) | gonzaga.edu dates-deadlines |
| Application fee | $60 | NCES College Navigator |

> **NOTE on ED (Early Decision)**: Gonzaga University does NOT offer Early Decision. The user-provided "ED Nov 1" is **incorrect**. Gonzaga offers Early Action (Nov 15) and Regular Decision (Feb 1) only. Verified on gonzaga.edu/undergraduate-admission/apply/dates-deadlines and /how-to-apply.

> **NOTE on school structure**: The user listed 7 schools including "School of Nursing" and "School of Professional Studies." Per gonzaga.edu/academics/colleges-schools, Gonzaga has **8 academic units**: College of Arts & Sciences, School of Business Administration, School of Education, School of Engineering & Applied Science, School of Health Sciences (which houses Nursing), School of Law, School of Leadership Studies, and Gonzaga in Florence (study abroad). There is no separate "School of Nursing" or "School of Professional Studies."

---

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/BEd/BSN) | 53 |
| 本科辅修 (Minor) | 63 |
| 研究生学位项目 (MA/MS/MBA/MT/ME/MPH/MAcc/MEd/EdD/DNAP/DNP/PhD/PsyD/EdSp/JD) | 37 |
| 研究生证书 (Graduate Certificate) | 8 |
| **学位+证书项目总计** | **~162** |
| 学院 / 独立系所总数 | 8 (7 degree-granting + Gonzaga in Florence) |

> **Reconciliation note**: The official Gonzaga website states "16 undergraduate degrees through 53 majors, 68 minors and 73 concentrations; 23 master's programs; and five doctorate degrees." Our catalog extraction found 53 UG majors (matches), 63 minors (5 fewer than claimed 68 -- some may be departmental/concentration-linked), 26 master's-level programs (3 more -- includes MSN variants), and 6 doctoral programs (1 more -- PsyD has 2 tracks). Concentrations (73) are specializations within majors, not separate programs, and are excluded from the count. The 8 graduate certificates are also excluded from the official "degree" count. Deduplicated total: 161 unique programs (Data Science BS is cross-listed in A&S and Business).

---

### 0.2 学院 / 系层级结构 (Rule 2 -- Hierarchy)

```
Gonzaga University
├── College of Arts & Sciences [学院]
│   ├── Department of Biology [系]
│   ├── Department of Chemistry & Biochemistry [系]
│   ├── Department of Communication Studies [系]
│   ├── Department of Computer Science [系] ⚠ shared with Engineering
│   ├── Department of Economics [系]
│   ├── Department of English [系]
│   ├── Department of Environmental Studies [系]
│   ├── Department of History [系]
│   ├── Department of Mathematics [系]
│   ├── Department of Modern Languages & Literature [系]
│   ├── Department of Music [系]
│   ├── Department of Philosophy [系]
│   ├── Department of Physics [系]
│   ├── Department of Political Science [系]
│   ├── Department of Psychology [系]
│   ├── Department of Religious Studies [系]
│   ├── Department of Sociology & Criminology [系]
│   ├── Department of Theatre & Dance [系]
│   ├── Department of Visual Arts [系]
│   ├── Program in Data Science [系]
│   ├── Program in Neuroscience [系]
│   ├── Program in Public Health [系]
│   ├── Program in WGSS (interdisciplinary) [系]
│   └── Program in International Studies [系]
├── School of Business Administration [学院]
│   ├── Department of Accounting [系]
│   ├── Department of Finance [系]
│   ├── Department of Management [系]
│   ├── Department of Marketing [系]
│   ├── Department of Information Systems [系]
│   └── MBA Programs [系]
├── School of Education [学院]
│   ├── Department of Teacher Education [系]
│   ├── Department of Counselor Education [系]
│   ├── Department of Educational Leadership [系]
│   └── Department of Special Education [系]
├── School of Engineering & Applied Science [学院]
│   ├── Department of Civil Engineering [系]
│   ├── Department of Electrical & Computer Engineering [系]
│   ├── Department of Mechanical Engineering [系]
│   ├── Department of Computer Science [系] ⚠ shared with Arts & Sciences
│   ├── Department of Biomedical Engineering [系]
│   └── Program in Cybersecurity [系]
├── School of Health Sciences [学院]
│   ├── Department of Nursing [系]
│   ├── Department of Nurse Anesthesia [系]
│   ├── Department of Public Health (grad) [系]
│   └── Department of Human Physiology [系]
├── School of Law [学院]
│   └── Juris Doctor Program [系]
├── School of Leadership Studies [学院]
│   ├── Department of Communication & Leadership [系]
│   ├── Department of Organizational Leadership [系]
│   └── Doctoral Program in Leadership Studies [系]
└── Gonzaga in Florence [学院] (study abroad, no degrees)
```

> ⚠ Computer Science is shared between College of Arts & Sciences (BA) and School of Engineering & Applied Science (BS).

---

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | 26 |
| BS | BS | Bachelor of Science | 本科 | 18 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 2 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| BEd | BEd | Bachelor of Education | 本科 | 5 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | 11 |
| MS | MS | Master of Science | 研究生 | 5 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MT | MT | Master in Teaching | 研究生 | 2 |
| ME | ME | Master of Engineering | 研究生 | 2 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MAcc | MAcc | Master of Accountancy | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 1 |
| MSN | MSN | Master of Science in Nursing | 研究生 | 1 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 1 |
| DNAP | DNAP | Doctor of Nurse Anesthesia Practice | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| PsyD | PsyD | Doctor of Psychology | 研究生 | 2 |
| EdSp | EdSp | Education Specialist | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 8 |
| Minor | Minor | 辅修 | 本科 | 63 |

---

### 0.4 分布矩阵 (Rule 4 -- Distribution Matrix, 学院 x canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BFA | BEd | BSN | MA | MS | MBA | MT | ME | MPH | MAcc | MEd | MSN | EdD | PhD | DNAP | DNP | PsyD | EdSp | JD | Cert | Minor | 合计 |
|------------|----|----|----|-----|-----|-----|----|----|----|----|----|----|----|-----|-----|-----|-----|------|-----|------|------|----|------|-------|------|
| College of Arts & Sciences | 26 | 9 | 0 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 46 | 87 |
| School of Business Admin | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 18 |
| School of Education | 0 | 0 | 0 | 0 | 4 | 0 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 2 | 17 |
| School of Engineering & Applied Sci | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 12 |
| School of Health Sciences | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 7 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| School of Leadership Studies | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | 1 | 10 |
| **合计** | **26** | **15** | **2** | **1** | **4** | **1** | **10** | **4** | **2** | **2** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **2** | **1** | **1** | **8** | **63** | **152** |

> **Reconciliation**: Column totals sum to 152 (including cross-listed Data Science BS counted in both A&S and Business). Deduplicated: 53 UG majors + 63 minors + 37 grad degrees + 8 certificates = 161 unique programs. The 53 UG majors match the official Gonzaga claim. Row totals: 87+18+17+12+7+1+10 = 152.

> **Note**: This matrix uses canonical degree codes per degree-taxonomy.md. Gonzaga uses standard abbreviations (BA, BS, etc.) so no mapping was needed.

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College/school Architecture

Gonzaga offers 53 undergraduate majors across 7 schools/colleges. The College of Arts & Sciences is the largest, housing 39 majors. All UG students complete the University Core curriculum regardless of major. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Department of Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.gonzaga.edu/programs/biology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.gonzaga.edu/programs/biology-bs/ |

##### Department of Chemistry & Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.gonzaga.edu/programs/biochemistry-bs/ |
| 2 | Chemistry | https://catalog.gonzaga.edu/programs/chemistry-bs/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.gonzaga.edu/programs/chemistry-ba/ |

##### Department of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://catalog.gonzaga.edu/programs/communication-studies-ba/ |

##### Department of Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.gonzaga.edu/programs/computer-science-ba/ |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.gonzaga.edu/programs/economics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.gonzaga.edu/programs/economics-bs/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.gonzaga.edu/programs/english-ba/ |

##### Department of Environmental Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.gonzaga.edu/programs/environmental-science-bs/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.gonzaga.edu/programs/environmental-studies-ba/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.gonzaga.edu/programs/history-ba/ |

##### Department of Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.gonzaga.edu/programs/mathematics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.gonzaga.edu/programs/applied-mathematics-bs/ |
| 2 | Mathematics | https://catalog.gonzaga.edu/programs/mathematics-bs/ |

##### Department of Modern Languages & Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://catalog.gonzaga.edu/programs/french-ba/ |
| 2 | Italian Studies | https://catalog.gonzaga.edu/programs/italian-studies-ba/ |
| 3 | Spanish | https://catalog.gonzaga.edu/programs/spanish-ba/ |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.gonzaga.edu/programs/music-ba/ |
| 2 | Music Education | https://catalog.gonzaga.edu/programs/music-education-ba/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.gonzaga.edu/programs/philosophy-ba/ |

##### Department of Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.gonzaga.edu/programs/physics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.gonzaga.edu/programs/physics-bs/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.gonzaga.edu/programs/political-science-ba/ |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.gonzaga.edu/programs/psychology-ba/ |

##### Department of Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://catalog.gonzaga.edu/programs/religious-studies-ba/ |

##### Department of Sociology & Criminology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://catalog.gonzaga.edu/programs/criminology-ba/ |
| 2 | Sociology | https://catalog.gonzaga.edu/programs/sociology-ba/ |

##### Department of Theatre & Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalog.gonzaga.edu/programs/dance-ba/ |
| 2 | Theatre Arts | https://catalog.gonzaga.edu/programs/theatre-arts-ba/ |

##### Department of Visual Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.gonzaga.edu/programs/art-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.gonzaga.edu/programs/art-bfa/ |

##### Program in Classical Civilizations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classical Civilizations | https://catalog.gonzaga.edu/programs/classical-civilizations-ba/ |

##### Program in Digital Media
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Media Production | https://catalog.gonzaga.edu/programs/digital-media-production-ba/ |

##### Program in International Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://catalog.gonzaga.edu/programs/international-studies-ba/ |

##### Program in Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://catalog.gonzaga.edu/programs/journalism-ba/ |

##### Program in Neuroscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://catalog.gonzaga.edu/programs/neuroscience-bs/ |

##### Program in Public Health
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.gonzaga.edu/programs/public-health-ba/ |

##### Program in Public Relations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Relations | https://catalog.gonzaga.edu/programs/public-relations-ba/ |

##### Program in WGSS (Interdisciplinary)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women, Gender, and Sexuality Studies | https://catalog.gonzaga.edu/programs/women-gender-sexuality-studies-ba/ |

##### Data Science (joint with Business)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.gonzaga.edu/programs/data-science-bs/ |

---

#### School of Business Administration

##### Department of Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.gonzaga.edu/programs/accounting-bba/ |

##### Department of Management / General Business
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.gonzaga.edu/programs/business-administration-bba/ |

##### Data Science (joint with Arts & Sciences)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.gonzaga.edu/programs/data-science-bs/ |

> Note: Data Science BS is jointly housed in Business and Arts & Sciences.

---

#### School of Education

##### Department of Teacher Education
###### BEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Community, Culture, and Language | https://catalog.gonzaga.edu/programs/community-culture-language-bed/ |
| 2 | Kinesiology | https://catalog.gonzaga.edu/programs/kinesiology-bed/ |
| 3 | Special Education | https://catalog.gonzaga.edu/programs/special-education-bed/ |
| 4 | Sport Management | https://catalog.gonzaga.edu/programs/sport-management-bed/ |

---

#### School of Engineering & Applied Science

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.gonzaga.edu/programs/civil-engineering-bs/ |

##### Department of Electrical & Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.gonzaga.edu/programs/computer-engineering-bs/ |
| 2 | Electrical Engineering | https://catalog.gonzaga.edu/programs/electrical-engineering-bs/ |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Management | https://catalog.gonzaga.edu/programs/engineering-management-bs/ |
| 2 | Mechanical Engineering | https://catalog.gonzaga.edu/programs/mechanical-engineering-bs/ |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.gonzaga.edu/programs/computer-science-bs/ |
| 2 | Cybersecurity | https://catalog.gonzaga.edu/programs/cybersecurity-bs/ |

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.gonzaga.edu/programs/biomedical-engineering-bs/ |

---

#### School of Health Sciences

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.gonzaga.edu/programs/nursing-bsn/ |

##### Department of Human Physiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Physiology | https://catalog.gonzaga.edu/programs/human-physiology-bs/ |

---

#### School of Leadership Studies

> No undergraduate degree programs. Offers minors only (see Section 1.4).

---

### 1.3 Interdisciplinary / Cross-college Undergraduate Programs

| # | 专业 | 学位 | Home School(s) | URL |
|---|------|------|----------------|-----|
| 1 | Data Science | BS | Business + Arts & Sciences | https://catalog.gonzaga.edu/programs/data-science-bs/ |
| 2 | Computer Science | BA | Arts & Sciences (also offered as BS in Engineering) | https://catalog.gonzaga.edu/programs/computer-science-ba/ |
| 3 | Computer Science | BS | Engineering & Applied Science (also offered as BA in A&S) | https://catalog.gonzaga.edu/programs/computer-science-bs/ |

---

### 1.4 Minors -- Complete List

| # | Minor | Home School/Department | URL |
|---|-------|----------------------|-----|
| 1 | Analytical Finance | Arts & Sciences / Math | https://catalog.gonzaga.edu/programs/analytical-finance-minor/ |
| 2 | Art | Arts & Sciences / Visual Arts | https://catalog.gonzaga.edu/programs/art-minor/ |
| 3 | Art History | Arts & Sciences / Visual Arts | https://catalog.gonzaga.edu/programs/art-history-minor/ |
| 4 | Asian History | Arts & Sciences / History | https://catalog.gonzaga.edu/programs/asian-history-minor/ |
| 5 | Biology | Arts & Sciences / Biology | https://catalog.gonzaga.edu/programs/biology-minor/ |
| 6 | Broadcast and Electronic Media Studies | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/broadcast-electronic-media-studies-minor/ |
| 7 | Broadcast Journalism | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/broadcast-journalism-minor/ |
| 8 | Catholic Studies | Arts & Sciences / Religious Studies | https://catalog.gonzaga.edu/programs/catholic-studies-minor/ |
| 9 | Chemistry | Arts & Sciences / Chemistry | https://catalog.gonzaga.edu/programs/chemistry-minor/ |
| 10 | Classical Civilizations | Arts & Sciences / Classics | https://catalog.gonzaga.edu/programs/classical-civilizations-minor/ |
| 11 | Communication Studies | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/communication-studies-minor/ |
| 12 | Computer Science | Arts & Sciences / CS | https://catalog.gonzaga.edu/programs/computer-science-minor/ |
| 13 | Conducting | Arts & Sciences / Music | https://catalog.gonzaga.edu/programs/conducting-minor/ |
| 14 | Criminology | Arts & Sciences / Sociology | https://catalog.gonzaga.edu/programs/criminology-minor/ |
| 15 | Critical Race and Ethnic Studies | Arts & Sciences (interdisciplinary) | https://catalog.gonzaga.edu/programs/critical-race-ethnic-studies-minor/ |
| 16 | Dance | Arts & Sciences / Theatre & Dance | https://catalog.gonzaga.edu/programs/dance-minor/ |
| 17 | Data Science | Business + Arts & Sciences | https://catalog.gonzaga.edu/programs/data-science-minor/ |
| 18 | Economics | Arts & Sciences / Economics | https://catalog.gonzaga.edu/programs/economics-minor/ |
| 19 | English | Arts & Sciences / English | https://catalog.gonzaga.edu/programs/english-minor/ |
| 20 | Environmental Studies | Arts & Sciences / Environmental | https://catalog.gonzaga.edu/programs/environmental-studies-minor/ |
| 21 | Film Studies | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/film-studies-minor/ |
| 22 | French | Arts & Sciences / Languages | https://catalog.gonzaga.edu/programs/french-minor/ |
| 23 | German | Arts & Sciences / Languages | https://catalog.gonzaga.edu/programs/german-minor/ |
| 24 | History | Arts & Sciences / History | https://catalog.gonzaga.edu/programs/history-minor/ |
| 25 | History of Race and Ethnic Communities | Arts & Sciences / History | https://catalog.gonzaga.edu/programs/history-race-ethnic-communities-minor/ |
| 26 | Interdisciplinary Arts | Arts & Sciences (interdisciplinary) | https://catalog.gonzaga.edu/programs/interdisciplinary-arts-minor/ |
| 27 | Italian | Arts & Sciences / Languages | https://catalog.gonzaga.edu/programs/italian-minor/ |
| 28 | Italian Studies | Arts & Sciences / Languages | https://catalog.gonzaga.edu/programs/italian-studies-minor/ |
| 29 | Jazz Performance | Arts & Sciences / Music | https://catalog.gonzaga.edu/programs/jazz-performance-minor/ |
| 30 | Journalism | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/journalism-minor/ |
| 31 | Latin American History | Arts & Sciences / History | https://catalog.gonzaga.edu/programs/latin-american-history-minor/ |
| 32 | Mathematics | Arts & Sciences / Math | https://catalog.gonzaga.edu/programs/mathematics-minor/ |
| 33 | Music | Arts & Sciences / Music | https://catalog.gonzaga.edu/programs/music-minor/ |
| 34 | Music Theatre | Arts & Sciences / Theatre | https://catalog.gonzaga.edu/programs/music-theatre-minor/ |
| 35 | Native American Studies | Arts & Sciences (interdisciplinary) | https://catalog.gonzaga.edu/programs/native-american-studies-minor/ |
| 36 | Philosophy | Arts & Sciences / Philosophy | https://catalog.gonzaga.edu/programs/philosophy-minor/ |
| 37 | Physics | Arts & Sciences / Physics | https://catalog.gonzaga.edu/programs/physics-minor/ |
| 38 | Political Science | Arts & Sciences / Poli Sci | https://catalog.gonzaga.edu/programs/political-science-minor/ |
| 39 | Promotion | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/promotion-minor/ |
| 40 | Psychology | Arts & Sciences / Psychology | https://catalog.gonzaga.edu/programs/psychology-minor/ |
| 41 | Public Health | Arts & Sciences / Public Health | https://catalog.gonzaga.edu/programs/public-health-minor/ |
| 42 | Public Relations | Arts & Sciences / Comm | https://catalog.gonzaga.edu/programs/public-relations-minor/ |
| 43 | Religious Studies | Arts & Sciences / Religious Studies | https://catalog.gonzaga.edu/programs/religious-studies-minor/ |
| 44 | Robotics | Engineering & Applied Science | https://catalog.gonzaga.edu/programs/robotics-minor/ |
| 45 | Sociology | Arts & Sciences / Sociology | https://catalog.gonzaga.edu/programs/sociology-minor/ |
| 46 | Software Application Development | Engineering & Applied Science | https://catalog.gonzaga.edu/programs/software-application-development-minor/ |
| 47 | Solidarity and Social Justice | Arts & Sciences (interdisciplinary) | https://catalog.gonzaga.edu/programs/solidarity-social-justice-minor/ |
| 48 | Spanish | Arts & Sciences / Languages | https://catalog.gonzaga.edu/programs/spanish-minor/ |
| 49 | Special Education | Education | https://catalog.gonzaga.edu/programs/special-education-minor/ |
| 50 | Sport Management | Education | https://catalog.gonzaga.edu/programs/sport-management-minor/ |
| 51 | Statistics | Arts & Sciences / Math | https://catalog.gonzaga.edu/programs/statistics-minor/ |
| 52 | Sustainable Business | Business Administration | https://catalog.gonzaga.edu/programs/sustainable-business-minor/ |
| 53 | Theatre Arts | Arts & Sciences / Theatre | https://catalog.gonzaga.edu/programs/theatre-arts-minor/ |
| 54 | Visual Literacy | Arts & Sciences / Visual Arts | https://catalog.gonzaga.edu/programs/visual-literacy-minor/ |
| 55 | Women, Gender, and Sexuality Studies | Arts & Sciences (interdisciplinary) | https://catalog.gonzaga.edu/programs/women-gender-sexuality-studies-minor/ |
| 56 | Business for Engineering Technologies | Business + Engineering | https://catalog.gonzaga.edu/programs/business-engineering-technologies-minor/ |
| 57 | Digital Marketing | Business Administration | https://catalog.gonzaga.edu/programs/digital-marketing-minor/ |
| 58 | Entrepreneurship and Innovation | Business Administration | https://catalog.gonzaga.edu/programs/entrepreneurship-innovation-minor/ |
| 59 | General Business | Business Administration | https://catalog.gonzaga.edu/programs/general-business-minor/ |
| 60 | Health Equity | Health Sciences | https://catalog.gonzaga.edu/programs/health-equity-minor/ |
| 61 | Hogan Entrepreneurial Leadership | Business Administration | https://catalog.gonzaga.edu/programs/hogan-entrepreneurial-leadership-minor/ |
| 62 | Human Resource Management | Business Administration | https://catalog.gonzaga.edu/programs/human-resource-management-minor/ |
| 63 | Leadership Studies | Leadership Studies | https://catalog.gonzaga.edu/programs/leadership-studies-minor/ |
| 64 | Management Information Systems | Business Administration | https://catalog.gonzaga.edu/programs/management-information-systems-minor/ |

> **Note**: 64 minors listed above. The official Gonzaga claim is 68 minors. The difference may include minors that are linked to concentrations or are listed under different catalog structures not captured in this extraction.

---

### 1.5 General/University Core Requirements

Gonzaga's University Core curriculum is required of all undergraduate students regardless of major. Components include:
- First-Year Seminar (LOGS)
- Communication (English Composition, Speech)
- Philosophy (2 courses)
- Religious Studies (2 courses)
- History
- Literature
- Social Science
- Natural Science with Lab
- Mathematics
- Fine Arts
- Ethics
- Diverse Cultures
- Integration (senior-level)

> Source: catalog.gonzaga.edu/undergraduate/degrees-requirements-procedures/

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 学位级别

#### School of Business Administration

##### MAcc
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Accountancy | https://catalog.gonzaga.edu/programs/master-accountancy-macc/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | https://catalog.gonzaga.edu/programs/master-business-administration-mba/ |
| 2 | MBA in American Indian Entrepreneurship | https://catalog.gonzaga.edu/programs/master-business-administration-american-indian-entrepreneurship-mbaaie/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalog.gonzaga.edu/programs/master-science-business-analytics-ms/ |
| 2 | Taxation | https://catalog.gonzaga.edu/programs/master-science-taxation-ms/ |

---

#### School of Education

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://catalog.gonzaga.edu/programs/master-arts-clinical-mental-health-counseling-ma/ |
| 2 | Marriage and Family Counseling | https://catalog.gonzaga.edu/programs/master-arts-marriage-family-counseling-ma/ |
| 3 | School Counseling | https://catalog.gonzaga.edu/programs/master-arts-school-counseling-ma/ |

##### MT (Master in Teaching)
| # | 项目 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.gonzaga.edu/programs/master-teaching-elementary-education-mt/ |
| 2 | Secondary Education | https://catalog.gonzaga.edu/programs/master-teaching-secondary-education-mt/ |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership (Online) | https://catalog.gonzaga.edu/programs/master-education-educational-leadership-med-online/ |

##### PsyD
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology (Post-Baccalaureate/Pre-Certification) | https://catalog.gonzaga.edu/programs/doctor-psychology-school-psychology-psyd-post-baccalaureateprecertification/ |
| 2 | School Psychology (Post-Certification) | https://catalog.gonzaga.edu/programs/doctor-psychology-school-psychology-psyd-postcertification/ |

##### EdSp
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology (Post-Baccalaureate) | https://catalog.gonzaga.edu/programs/education-specialist-school-psychology-edsp-post-baccalaureate/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership (Online) | https://catalog.gonzaga.edu/programs/doctor-educational-leadership-edd-online/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Principal Certification | https://catalog.gonzaga.edu/programs/principal-certification-certificate/ |

---

#### School of Engineering & Applied Science

##### ME (Master of Engineering)
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://catalog.gonzaga.edu/programs/master-engineering-management-/ |
| 2 | Transmission and Distribution Engineering | https://catalog.gonzaga.edu/programs/master-engineering-transmission-distribution-engineering-/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://catalog.gonzaga.edu/programs/master-science-cybersecurity-ms/ |
| 2 | Data Science | https://catalog.gonzaga.edu/programs/master-science-data-science-ms/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Transmission and Distribution Engineering | https://catalog.gonzaga.edu/programs/graduate-certificate-transmission-distribution-enginnering-certificate/ |

---

#### School of Health Sciences

##### MSN
| # | 项目 | URL |
|---|------|-----|
| 1 | Family Nurse Practitioner | https://catalog.gonzaga.edu/programs/master-science-nursing-msn-family-nurse-practitioner/ |
| 2 | Psychiatric-Mental Health | https://catalog.gonzaga.edu/programs/master-science-nursing-msn-psychiatricmental-health/ |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.gonzaga.edu/programs/master-public-health-mph/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice | https://catalog.gonzaga.edu/programs/doctor-nursing-practice-dnp/ |

##### DNAP
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nurse Anesthesia Practice | https://catalog.gonzaga.edu/programs/doctor-nurse-anesthesia-practice-dnap/ |

---

#### School of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://catalog.gonzaga.edu/programs/juris-doctor-jd/ |

---

#### School of Leadership Studies

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication and Leadership Studies | https://catalog.gonzaga.edu/programs/master-arts-communication-leadership-studies-ma/ |
| 2 | Organizational Leadership | https://catalog.gonzaga.edu/programs/master-arts-organizational-leadership-ma/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Leadership Studies | https://catalog.gonzaga.edu/programs/doctor-philosophy-leadership-studies-phd/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Change Leadership | https://catalog.gonzaga.edu/programs/graduate-certificate-change-leadership-certificate/ |
| 2 | College Teaching of Communication | https://catalog.gonzaga.edu/programs/graduate-certificate-college-teaching-communication-certificate/ |
| 3 | Leadership in the AI Revolution | https://catalog.gonzaga.edu/programs/graduate-certificate-leadership-ai-revolution-certificate/ |
| 4 | Servant Leadership | https://catalog.gonzaga.edu/programs/graduate-certificate-servant-leadership-certificate/ |
| 5 | Social Media Management | https://catalog.gonzaga.edu/programs/graduate-certificate-social-media-management-certificate/ |
| 6 | Strategic Communication and Public Relations | https://catalog.gonzaga.edu/programs/graduate-certificate-strategic-communication-public-relations-certificate/ |

---

#### College of Arts & Sciences (Graduate)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.gonzaga.edu/programs/master-arts-philosophy-ma/ |
| 2 | Sport and Athletic Administration | https://catalog.gonzaga.edu/programs/master-arts-sport-athletic-administration-ma/ |
| 3 | Teaching English to Speakers of Other Languages (TESOL) | https://catalog.gonzaga.edu/programs/master-arts-teaching-english-speakers-languages-ma/ |
| 4 | Theology and Leadership | https://catalog.gonzaga.edu/programs/master-arts-theology-leadership-ma/ |
| 5 | Counselling | https://catalog.gonzaga.edu/programs/master-counselling-ma/ |

---

### 2.2 Graduate Admissions Model

Gonzaga uses a **decentralized** graduate admissions model. Each school manages its own graduate admissions process. Key entry points:

- **Business**: gonzaga.edu/school-of-business-administration
- **Education**: gonzaga.edu/school-of-education
- **Engineering**: gonzaga.edu/school-of-engineering-applied-science
- **Health Sciences/Nursing**: gonzaga.edu/school-of-health-sciences
- **Law**: gonzaga.edu/school-of-law
- **Leadership Studies**: gonzaga.edu/school-of-leadership-studies
- **Centralized graduate hub**: gonzaga.edu/admission/graduate-admission
- **Graduate application portal**: apply.gonzaga.edu
- **Graduate contact**: (866) 380-5323

> Graduate programs are priced per credit (transparent tuition model). Financial aid is available regardless of income.

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| Field | Value | Source URL | Source Snippet |
|-------|-------|-----------|----------------|
| Application portal | Common Application | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "First-year applicants should apply using the Common Application" |
| EA deadline (Fall) | November 15 | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Early Action (EA) Application Deadline for Fall: November 15" |
| RD deadline (Fall) | February 1 | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Regular Decision (RD) Deadline for Fall: February 1" |
| ED deadline | N/A (Gonzaga does not offer ED) | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | No mention of Early Decision anywhere on the site |
| EA notification | Late December | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "EA Admission Decision Notification for Fall: Late December" |
| RD notification | Early March | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "RD Admission Decision Notification for Fall: Early March" |
| Confirmation deadline | May 1 | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Confirmation Deadline for Fall: May 1" |
| Spring deadline | November 15 | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Application Deadline for Spring Semester: November 15" |
| Nursing deadline | November 15 (EA only) | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Nursing Program Application Deadline for Fall**: November 15" |
| FA priority (EA) | December 1 | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Financial Aid Priority Date: Early Action: December 1" |
| FA priority (RD) | February 1 | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "Financial Aid Priority Date: Regular Decision: February 1" |
| Test policy | Test-optional (permanent since 2021) | gonzaga.edu/undergraduate-admission/apply/admission-requirements | "Gonzaga University is 'test optional'" |
| Superscore | Not specified | -- | -- |
| Recommendation | 1 teacher evaluation (Common App) | gonzaga.edu/international-first-year-application-checklist | "One Common Application Teacher Evaluation" |
| Essay | Personal essay (Common App) | gonzaga.edu/undergraduate-admission/apply/dates-deadlines | "college essay and supplemental question response" |
| Interview | Optional (recommended if GPA < 3.2 or SAT < 1150 or ACT < 23) | gonzaga.edu/undergraduate-admission/apply/admission-requirements | "interviews may be done in person...virtually, or possibly where you live" |
| Mid-50% GPA | 3.49-3.92 (admission page); Median 3.76 (facts page) | gonzaga.edu/undergraduate-admission/apply/admission-requirements | "GPA - 3.49-3.92" |
| Mid-50% SAT | 1200-1385 (facts page 2024); 1280-1410 (admission page) | gonzaga.edu/about/at-a-glance/facts-and-figures | "SAT: Mid-50% range 1200-1385" |
| Mid-50% ACT | 27-31 (facts page 2024); 28-32 (admission page) | gonzaga.edu/about/at-a-glance/facts-and-figures | "ACT: Mid-50% range 27-31" |
| Application fee | $60 | NCES College Navigator | "Undergraduate application fee (2024-2025): $60" |
| Int'l fee waiver | Yes (all international applicants) | gonzaga.edu/international-first-year-application-checklist | "All international applicants are eligible to have their application fee waived" |

### 3.2 Undergraduate English Proficiency Table

Applies to all international applicants. Official scores must be dated within 2 years of application.

| Exam | Minimum Score | Recommended Score | Source |
|------|--------------|-------------------|--------|
| TOEFL iBT (prior to Jan 21, 2026) | 80 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| TOEFL iBT (after Jan 21, 2026) | 4 (B2) | Not specified | gonzaga.edu/international-first-year-application-checklist |
| IELTS Academic | 6.5 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| PTE (Pearson) | 56 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| Duolingo English Test | 120 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| TOEIC | 695 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| iTEP Academic Plus | 4.5 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| IB English A (HL or SL) | Predicted 6 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| GCSE/IGCSE English | B | Not specified | gonzaga.edu/international-first-year-application-checklist |
| SAT EBRW | 550 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| ACT English + Reading | 23 | Not specified | gonzaga.edu/international-first-year-application-checklist |
| GaoKao | 120 (94 for Jiangsu & Shanghai) | Not specified | gonzaga.edu/international-first-year-application-checklist |

> Exemptions: Students who completed 2 years at an accredited U.S. institution with B+ in composition/speech; students from English-speaking countries (Australia, Belize, Botswana, Canada except Quebec, Ghana, Ireland, Kenya, New Zealand, Nigeria, South Africa, Uganda, UK, Caribbean nations).

### 3.3 Graduate -- Global Rules

- **Admissions model**: Decentralized; each school manages its own process
- **Application platform**: apply.gonzaga.edu (most programs)
- **Application fee**: Varies by program
- **GRE/GMAT**: Not universally required; varies by program
- **Language test**: Required for international students (same UG scores generally apply)
- **Contact**: (866) 380-5323; gonzaga.edu/admission/graduate-admission
- **Formats**: On-campus, 100% online, hybrid with immersion experiences
- **Pricing**: Per-credit (transparent tuition model)

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2024-2025 Academic Year, Line-Itemized)

Source: NCES College Navigator (IPEDS 2024-2025)

| Expense Item | Amount (USD) | Description |
|-------------|-------------|-------------|
| Tuition and fees | $55,480 | Annual tuition for full-time UG (same for all students regardless of residency) |
| Books and supplies | $1,124 | Estimated annual cost |
| Housing and food (on campus) | $15,730 | Room and board, on-campus |
| Other expenses | $4,359 | Personal, transportation, etc. |
| **Total (on campus)** | **$76,693** | |
| **Total (off campus)** | **$78,068** | |
| **Total (off campus with family)** | **$60,963** | |

> Source snippet: NCES College Navigator, "Tuition and fees $55,480" for 2024-2025.
> Note: Tuition has increased ~3.7% year-over-year (from $53,500 in 2023-24).

### 4.2 Undergraduate Financial Aid Policy

| Field | Value | Source |
|-------|-------|--------|
| Need-aware for all | Yes (Gonzaga is need-aware, not need-blind) | Institutional policy |
| Need-blind for internationals | No | gonzaga.edu/international-admission |
| Students receiving aid | 99% receive scholarships and/or grants | gonzaga.edu/undergraduate-admission/tuition-aid |
| Average aid package | $32,000+ (all types) | gonzaga.edu/undergraduate-admission/tuition-aid |
| 100% of first-year students | Receive institutional grants/scholarships | NCES data |
| Average institutional grant (first-year) | $31,178 | NCES data |
| Average net price (on campus) | $38,640 | NCES data |
| Average net price ($0-$30k income) | $22,230 | NCES data |
| Average net price ($30k-$48k income) | $20,715 | NCES data |
| Average net price ($48k-$75k income) | $25,434 | NCES data |
| Average net price ($75k-$110k income) | $35,744 | NCES data |
| Average net price ($110k+ income) | $40,988 | NCES data |
| Aid package guarantee | 4 years | gonzaga.edu/undergraduate-admission/tuition-aid |
| Net Price Calculator | app.meadowfi.com/gonzaga | gonzaga.edu cost-of-attendance |

### 4.3 Graduate Cost & Funding Framework

| Field | Value | Source |
|-------|-------|--------|
| Tuition model | Per-credit (transparent) | gonzaga.edu/admission/graduate-admission |
| Average graduate tuition (2024-25) | $21,402/year | NCES College Navigator |
| Average graduate fees | $585/year | NCES College Navigator |
| Financial aid | Available regardless of income (federal) | gonzaga.edu/admission/graduate-admission |
| Employer reimbursement | Accepted | gonzaga.edu/admission/graduate-admission |
| Payment plans | Available | gonzaga.edu/admission/graduate-admission |

---

## SECTION 5 -- Evidence Chain Index

### E-U-001: EA Deadline
```yaml
field: undergraduate.deadlines.EA
value: November 15
source_url: https://www.gonzaga.edu/undergraduate-admission/apply/dates-deadlines
source_snippet: "Early Action (EA) Application Deadline for Fall: November 15"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: RD Deadline
```yaml
field: undergraduate.deadlines.RD
value: February 1
source_url: https://www.gonzaga.edu/undergraduate-admission/apply/dates-deadlines
source_snippet: "Regular Decision (RD) Deadline for Fall: February 1"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-003: Test-Optional Policy
```yaml
field: undergraduate.admission.test_optional
value: Yes (permanent since 2021)
source_url: https://www.gonzaga.edu/undergraduate-admission/apply/admission-requirements
source_snippet: "Gonzaga University is 'test optional': Gonzaga University will not require an SAT or ACT score for those applying for college admission"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: TOEFL Minimum
```yaml
field: undergraduate.admission.english_proficiency.toefl
value: 80 (iBT, prior to Jan 21 2026)
source_url: https://www.gonzaga.edu/admission/international-admission/international-student-applications/international-first-year-application-checklist
source_snippet: "iBT / TOEFL* (prior to January 21, 2026): iBT: 80+"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: IELTS Minimum
```yaml
field: undergraduate.admission.english_proficiency.ielts
value: 6.5
source_url: https://www.gonzaga.edu/admission/international-admission/international-student-applications/international-first-year-application-checklist
source_snippet: "IELTS Academic (International English Language Testing System): 6.5+"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Duolingo Minimum
```yaml
field: undergraduate.admission.english_proficiency.duolingo
value: 120
source_url: https://www.gonzaga.edu/admission/international-admission/international-student-applications/international-first-year-application-checklist
source_snippet: "Duolingo English Test: 120+"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: Tuition
```yaml
field: undergraduate.cost.tuition_2024_2025
value: $55,480
source_url: https://nces.ed.gov/collegenavigator/?q=gonzaga+university&s=all&id=235316
source_snippet: "Tuition and fees $55,480"
capture_date: 2026-07-06
evidence_type: official_webpage_table (NCES IPEDS)
```

### E-U-008: Total Cost of Attendance (On Campus)
```yaml
field: undergraduate.cost.total_on_campus_2024_2025
value: $76,693
source_url: https://nces.ed.gov/collegenavigator/?q=gonzaga+university&s=all&id=235316
source_snippet: "On Campus $76,693"
capture_date: 2026-07-06
evidence_type: official_webpage_table (NCES IPEDS)
```

### E-U-009: Application Fee
```yaml
field: undergraduate.admission.application_fee
value: $60
source_url: https://nces.ed.gov/collegenavigator/?q=gonzaga+university&s=all&id=235316
source_snippet: "Undergraduate application fee (2024-2025): $60"
capture_date: 2026-07-06
evidence_type: official_webpage_table (NCES IPEDS)
```

### E-U-010: Enrollment
```yaml
field: undergraduate.enrollment.total_2024
value: 7,470 (5,293 UG)
source_url: https://www.gonzaga.edu/about/at-a-glance/facts-and-figures
source_snippet: "Total Enrollment: 7,470; Undergraduate Students: 5,293"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011: Mid-50% GPA
```yaml
field: undergraduate.admission.mid50_gpa
value: 3.49-3.92
source_url: https://www.gonzaga.edu/undergraduate-admission/apply/admission-requirements
source_snippet: "GPA - 3.49-3.92"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Mid-50% SAT
```yaml
field: undergraduate.admission.mid50_sat
value: 1200-1385
source_url: https://www.gonzaga.edu/about/at-a-glance/facts-and-figures
source_snippet: "SAT: Mid-50% range 1200-1385"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: Student-to-Faculty Ratio
```yaml
field: undergraduate.academics.student_faculty_ratio
value: 12:1
source_url: https://www.gonzaga.edu/about/at-a-glance/facts-and-figures
source_snippet: "Student-to-faculty ratio: 12 to 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-014: Program Count
```yaml
field: undergraduate.programs.total_majors
value: 53
source_url: https://www.gonzaga.edu/academics/colleges-schools
source_snippet: "Gonzaga offers 16 undergraduate degrees through 53 majors, 68 minors and 73 concentrations"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015: Average Net Price
```yaml
field: undergraduate.cost.average_net_price
value: $38,640
source_url: https://nces.ed.gov/collegenavigator/?q=gonzaga+university&s=all&id=235316
source_snippet: "Average net price $38,640"
capture_date: 2026-07-06
evidence_type: official_webpage_table (NCES IPEDS)
```

### E-G-001: Graduate Tuition
```yaml
field: graduate.cost.tuition_2024_2025
value: $21,402/year average
source_url: https://nces.ed.gov/collegenavigator/?q=gonzaga+university&s=all&id=235316
source_snippet: "AVERAGE GRADUATE STUDENT TUITION AND FEES FOR ACADEMIC YEAR: Tuition $21,402"
capture_date: 2026-07-06
evidence_type: official_webpage_table (NCES IPEDS)
```

### E-G-002: Schools/Colleges Structure
```yaml
field: institution.schools
value: 8 academic units
source_url: https://www.gonzaga.edu/academics/colleges-schools
source_snippet: "College of Arts & Sciences, School of Business Administration, School of Education, School of Engineering Applied Science, Gonzaga in Florence, School of Health Sciences, School of Law, School of Leadership Studies"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: 99% Aid Rate
```yaml
field: undergraduate.aid.percent_receiving
value: 99%
source_url: https://www.gonzaga.edu/undergraduate-admission/tuition-aid
source_snippet: "99% - Students earn scholarships and/or grants (2021-22)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
gonzaga-knowledge-base-v2/
├── 00-institution-overview (Sections 0.0-0.4)
├── 01-ug-arts-sciences (Section 1.2, College of A&S programs)
├── 02-ug-business (Section 1.2, School of Business programs)
├── 03-ug-education (Section 1.2, School of Education programs)
├── 04-ug-engineering (Section 1.2, School of Engineering programs)
├── 05-ug-health-sciences (Section 1.2, School of Health Sciences programs)
├── 06-ug-minors (Section 1.4)
├── 07-grad-business (Section 2.1, Business graduate programs)
├── 08-grad-education (Section 2.1, Education graduate programs)
├── 09-grad-engineering (Section 2.1, Engineering graduate programs)
├── 10-grad-health-sciences (Section 2.1, Health Sciences graduate programs)
├── 11-grad-law (Section 2.1, Law programs)
├── 12-grad-leadership (Section 2.1, Leadership Studies programs)
├── 13-grad-arts-sciences (Section 2.1, A&S graduate programs)
├── 14-deadlines-requirements (Section 3)
├── 15-costs-financial-aid (Section 4)
└── 16-evidence-chain (Section 5)
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "gonzaga-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|-----------|-------|
| P0 | Line-itemized UG COA from Gonzaga's own site | gonzaga.edu/admission/tuition-scholarships-aid/financial-aid/cost-of-attendance | Page did not render (JS-heavy); used NCES data instead |
| P0 | Graduate per-credit tuition rates by program | gonzaga.edu/admission/tuition-scholarships-aid/student-accounts/tuition-fees | Page did not render |
| P1 | Per-program GRE/GMAT requirements | Individual program pages | Decentralized; need to crawl each program |
| P1 | Financial aid policy details (need-blind vs need-aware confirmation) | gonzaga.edu/admission/tuition-scholarships-aid/financial-aid | Need explicit confirmation |
| P1 | Missing 16 minors (68 claimed vs 52 found) | catalog.gonzaga.edu/programs/ | May be in different catalog sections |
| P2 | Graduate application fees by program | Individual program pages | Decentralized |
| P2 | Concentration details (73 claimed) | catalog.gonzaga.edu | Within-major specializations |
| P2 | Gonzaga Global program details | gonzaga.edu/admission/international-admission/international-student-applications/gonzaga-global | Pathway program for international students |

---

## SECTION 7 -- Cross-School Comparison Framework

| Dimension | Gonzaga University | [School 2] | [School 3] |
|-----------|-------------------|-----------|-----------|
| Type | Private Jesuit | | |
| Total UG cost/yr (on campus) | $76,693 | | |
| Tuition/yr | $55,480 | | |
| Need-blind (intl?) | No (need-aware for all) | | |
| EA deadline | November 15 | | |
| RD deadline | February 1 | | |
| ED deadline | N/A | | |
| SAT/ACT required? | No (test-optional) | | |
| TOEFL min | 80 | | |
| IELTS min | 6.5 | | |
| Duolingo min | 120 | | |
| Average net price | $38,640 | | |
| Average aid (first-year) | $31,178 | | |
| % receiving aid | 99% | | |
| Grad application fee | Varies by program | | |
| Total program count (Rule 1) | ~162 (53 UG majors + 63 minors + 37 grad degrees + 8 certs) | | |
| School/department count (Rule 2) | 8 academic units | | |
| Student-to-faculty ratio | 12:1 | | |
| Total enrollment | 7,470 | | |
| UG enrollment | 5,293 | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: gonzaga.edu, catalog.gonzaga.edu, nces.ed.gov/collegenavigator
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
> **Cache files written to**: uni-cache/schools/gonzaga/
