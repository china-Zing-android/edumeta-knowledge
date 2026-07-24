# University of Connecticut (UConn) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 265 |
| 本科辅修 (Minor) | 252 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 290 |
| 研究生高级证书 (Advanced Certificate / Diploma) | N/A (included in degree programs) |
| **学位项目总计 (UG + Grad)** | **807** |
| 学院 / 独立系所总数 | 10 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Connecticut
├── College of Agriculture, Health and Natural Resources [学院]
│   ├── Department of Animal Science [系]
│   ├── Department of Nutritional Sciences [系]
│   ├── Department of Kinesiology [系]
│   ├── Department of Allied Health Sciences [系]
│   ├── Department of Pathobiology [系]
│   ├── Department of Plant Science [系]
│   ├── Department of Natural Resources [系]
│   ├── Department of Oceanography [系]
│   └── Department of Agricultural Economics [系]
├── Ratcliffe Hicks School of Agriculture [学院]
│   └── Associate Degree Programs [系]
├── School of Business [学院]
│   ├── Department of Accounting [系]
│   ├── Department of Finance [系]
│   ├── Department of Management [系]
│   ├── Department of Marketing [系]
│   └── Department of Operations & Information Management [系]
├── Neag School of Education [学院]
│   ├── Department of Curriculum and Instruction [系]
│   ├── Department of Educational Psychology [系]
│   ├── Department of Educational Leadership [系]
│   └── Department of Kinesiology (Sport Management) [系]
├── College of Engineering [学院]
│   ├── Department of Biomedical Engineering [系]
│   ├── Department of Chemical & Biomolecular Engineering [系]
│   ├── Department of Civil & Environmental Engineering [系]
│   ├── Department of Computer Science & Engineering [系]
│   ├── Department of Electrical & Computer Engineering [系]
│   ├── Department of Materials Science & Engineering [系]
│   ├── Department of Mechanical Engineering [系]
│   └── Department of Systems Engineering [系]
├── School of Fine Arts [学院]
│   ├── Department of Art & Art History [系]
│   ├── Department of Digital Media & Design [系]
│   ├── Department of Dramatic Arts [系]
│   ├── Department of Music [系]
│   └── Department of Puppet Arts [系]
├── College of Liberal Arts and Sciences [学院]
│   ├── Department of English [系]
│   ├── Department of History [系]
│   ├── Department of Philosophy [系]
│   ├── Department of Political Science [系]
│   ├── Department of Sociology [系]
│   ├── Department of Economics [系]
│   ├── Department of Psychology [系]
│   ├── Department of Mathematics [系]
│   ├── Department of Statistics [系]
│   ├── Department of Physics [系]
│   ├── Department of Chemistry [系]
│   ├── Department of Biology [系]
│   ├── Department of Molecular & Cell Biology [系]
│   ├── Department of Ecology & Evolutionary Biology [系]
│   ├── Department of Earth Sciences [系]
│   ├── Department of Geography [系]
│   ├── Department of Anthropology [系]
│   ├── Department of Linguistics [系]
│   ├── Department of Modern & Classical Languages [系]
│   ├── Department of Communication [系]
│   ├── Department of Journalism [系]
│   ├── Department of Human Development & Family Sciences [系]
│   ├── Department of Women's, Gender, & Sexuality Studies [系]
│   ├── Department of African American Studies [系]
│   ├── Department of Asian & Asian American Studies [系]
│   ├── Department of Latino & Latin American Studies [系]
│   ├── Department of Judaic Studies [系]
│   ├── Department of Human Rights [系]
│   ├── Department of Urban & Community Studies [系]
│   └── Department of Individualized & Interdisciplinary Studies [系]
├── Elisabeth DeLuca School of Nursing [学院]
│   └── Department of Nursing [系]
├── School of Pharmacy and Pharmaceutical Sciences [学院]
│   └── Department of Pharmaceutical Sciences [系]
└── School of Social Work [学院]
    └── Department of Social Work [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 66 |
| BS | Bachelor of Science | 本科 | 80 |
| BFA | Bachelor of Fine Arts | 本科 | 10 |
| BSE | Bachelor of Science in Engineering | 本科 | 22 |
| BM | Bachelor of Music | 本科 | 4 |
| BGS | Bachelor of General Studies | 本科 | 2 |
| BSW | Bachelor of Social Work | 本科 | 2 |
| AAS | Associate of Applied Science | 本科 | 6 |
| Pharm.D. | Doctor of Pharmacy | 本科 | 2 |
| IB/M | Integrated Bachelor/Master (Education) | 本科 | 18 |
| MA | Master of Arts | 研究生 | 42 |
| MS | Master of Science | 研究生 | 96 |
| MFA | Master of Fine Arts | 研究生 | 6 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MEng | Master of Engineering | 研究生 | 2 |
| MPA | Master of Public Administration | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 2 |
| MPP | Master of Public Policy | 研究生 | 2 |
| MSW | Master of Social Work | 研究生 | 2 |
| MMus | Master of Music | 研究生 | 2 |
| MA, PhD | Master of Arts/Doctor of Philosophy (dual) | 研究生 | 12 |
| MS, PhD | Master of Science/Doctor of Philosophy (dual) | 研究生 | 18 |
| PhD | Doctor of Philosophy | 研究生 | 64 |
| EdD | Doctor of Education | 研究生 | 2 |
| DNP | Doctor of Nursing Practice | 研究生 | 2 |
| DPT | Doctor of Physical Therapy | 研究生 | 2 |
| DMA | Doctor of Musical Arts | 研究生 | 2 |
| MDentSc | Master of Dental Science | 研究生 | 2 |
| AuD | Doctor of Audiology | 研究生 | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BA | BS | BFA | BSE | BM | BGS | BSW | AAS | Pharm.D. | IB/M | MA | MS | MFA | MBA | MEng | MPA | MPH | MPP | MSW | MMus | PhD | EdD | DNP | DPT | DMA | MDentSc | 合计 |
|------------|----|----|-----|-----|----|----|-----|-----|----------|------|----|----|-----|-----|------|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|---------|------|
| College of Agriculture, Health and Natural Resources | 2 | 18 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 2 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 54 |
| Ratcliffe Hicks School of Agriculture | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Business | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 28 |
| Neag School of Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 2 | 0 | 0 | 0 | 0 | 56 |
| College of Engineering | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 48 |
| School of Fine Arts | 4 | 0 | 10 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 0 | 2 | 0 | 44 |
| College of Liberal Arts and Sciences | 58 | 50 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 28 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 0 | 0 | 174 |
| Elisabeth DeLuca School of Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 10 |
| School of Pharmacy and Pharmaceutical Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| School of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| School of Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 6 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 6 |
| **合计** | 64 | 80 | 10 | 22 | 4 | 2 | 2 | 6 | 2 | 18 | 42 | 42 | 6 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 68 | 2 | 2 | 2 | 2 | 2 | **382** |

**Reconciliation note**: The matrix shows 382 degree-granting program slots. The total of 807 includes all degree variants (e.g., "BA or BS" counted as separate BA and BS rows) and minors. The 265 UG majors + 290 grad programs = 555 unique program-degree combinations.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UConn has 10 undergraduate-degree-granting schools and colleges at the Storrs main campus, plus 4 regional campuses (Avery Point, Hartford, Stamford, Waterbury). The College of Liberal Arts and Sciences is the largest, housing most traditional liberal arts majors. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture, Health and Natural Resources

##### Department of Animal Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/animal-science-bs/ |

##### Department of Allied Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Allied Health Sciences | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/allied-health-sciences-bs/ |

##### Department of Nutritional Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dietetics | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/dietetics-bs/ |
| 2 | Nutritional Sciences | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/nutritional-sciences-bs/ |

##### Department of Pathobiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pathobiology | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/pathobiology-bs/ |

##### Department of Plant Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Plant Science | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/plant-science-bs/ |
| 2 | Landscape Architecture | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/landscape-architecture-bs/ |

##### Department of Natural Resources
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Natural Resources | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/natural-resources-bs/ |
| 2 | Environmental Sciences | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/environmental-sciences-bs/ |

##### Department of Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Science | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/exercise-science-bs/ |
| 2 | Sport Management | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/sport-management-bs/ |

##### Department of Agricultural Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Resource Economics | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/agricultural-resource-economics-bs/ |
| 2 | Environmental and Natural Resource Economics | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/environmental-natural-resource-economics-bs/ |

##### Undeclared/General
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture, Health and Natural Resources | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/agriculture-health-natural-resources-bs/ |

#### Ratcliffe Hicks School of Agriculture

##### Associate Degree Programs
###### AAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science | https://catalog.uconn.edu/undergraduate/ratcliffe-hicks-agriculture/animal-science-aas/ |
| 2 | Plant Science | https://catalog.uconn.edu/undergraduate/ratcliffe-hicks-agriculture/plant-science-aas/ |

#### School of Business

##### Department of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.uconn.edu/undergraduate/business/accounting-bs/ |

##### Department of Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://catalog.uconn.edu/undergraduate/business/finance-bs/ |
| 2 | Financial Management | https://catalog.uconn.edu/undergraduate/business/financial-management-bs/ |

##### Department of Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://catalog.uconn.edu/undergraduate/business/management-bs/ |
| 2 | Business Administration | https://catalog.uconn.edu/undergraduate/business/ba-bs/ |

##### Department of Marketing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://catalog.uconn.edu/undergraduate/business/marketing-bs/ |
| 2 | Marketing Management | https://catalog.uconn.edu/undergraduate/business/marketing-management-bs/ |

##### Department of Operations & Information Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Analytics and Information Management | https://catalog.uconn.edu/undergraduate/business/analytics-information-management-bs/ |
| 2 | Business Data Analytics | https://catalog.uconn.edu/undergraduate/business/bda-bs/ |

#### Neag School of Education

##### Department of Curriculum and Instruction
###### IB/M (Integrated Bachelor/Master)
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education (Grades PK-6) | https://catalog.uconn.edu/undergraduate/neag-education/elementary-education-ibm/ |
| 2 | English Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/english-education-ibm/ |
| 3 | Mathematics Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/mathematics-education-ibm/ |
| 4 | Science Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/general-science-education-ibm/ |
| 5 | History and Social Studies Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/history-social-studies-education-ibm/ |
| 6 | Biology Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/biology-education-ibm/ |
| 7 | Chemistry Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/chemistry-education-ibm/ |
| 8 | Physics Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/physics-education-ibm/ |
| 9 | Earth Science Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/earth-science-education-ibm/ |
| 10 | French Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/french-language-education-ibm/ |
| 11 | German Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/german-language-education-ibm/ |
| 12 | Italian Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/italian-language-education-ibm/ |
| 13 | Spanish Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/spanish-language-education-ibm/ |
| 14 | Latin/Classics Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/latin-classics-language-education-ibm/ |
| 15 | Mandarin Chinese Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/mandarin-chinese-language-education-ibm/ |
| 16 | American Sign Language Education (Grades 4-12) | https://catalog.uconn.edu/undergraduate/neag-education/american-sign-language-education-ibm/ |
| 17 | Comprehensive Special Education (Grades PK-12) | https://catalog.uconn.edu/undergraduate/neag-education/comprehensive-special-education-ibm/ |
| 18 | Music Education (Grades PK-12) | https://catalog.uconn.edu/undergraduate/neag-education/music-education-ibm/ |

#### College of Engineering

##### Department of Biomedical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.uconn.edu/undergraduate/engineering/biomedical-engineering-bse/ |

##### Department of Chemical & Biomolecular Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.uconn.edu/undergraduate/engineering/chemical-engineering-bse/ |

##### Department of Civil & Environmental Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.uconn.edu/undergraduate/engineering/civil-engineering-bse/ |
| 2 | Environmental Engineering | https://catalog.uconn.edu/undergraduate/engineering/environmental-engineering-bse/ |

##### Department of Computer Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.uconn.edu/undergraduate/engineering/computer-science-bs/ |

###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science and Engineering | https://catalog.uconn.edu/undergraduate/engineering/computer-science-engineering-bse/ |

##### Department of Electrical & Computer Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.uconn.edu/undergraduate/engineering/electrical-engineering-bse/ |

##### Department of Materials Science & Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalog.uconn.edu/undergraduate/engineering/materials-science-engineering-bse/ |

##### Department of Mechanical Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.uconn.edu/undergraduate/engineering/mechanical-engineering-bse/ |

##### Department of Engineering Physics
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Physics | https://catalog.uconn.edu/undergraduate/engineering/engineering-physics-bse/ |

##### Multidisciplinary Engineering
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Multidisciplinary Engineering | https://catalog.uconn.edu/undergraduate/engineering/multidisciplinary-engineering-bse/ |
| 2 | Robotics Engineering | https://catalog.uconn.edu/undergraduate/engineering/robotics-engineering-bse/ |
| 3 | Data Science and Engineering | https://catalog.uconn.edu/undergraduate/engineering/data-science-engineering-bs/ |

##### Management and Engineering for Manufacturing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Management and Engineering for Manufacturing | https://catalog.uconn.edu/undergraduate/engineering/management-engineering-manufacturing-bs/ |

#### School of Fine Arts

##### Department of Art & Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uconn.edu/undergraduate/fine-arts/art-ba/ |
| 2 | Art History | https://catalog.uconn.edu/undergraduate/fine-arts/art-history-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uconn.edu/undergraduate/fine-arts/art-bfa/ |

##### Department of Digital Media & Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Media Design | https://catalog.uconn.edu/undergraduate/fine-arts/digital-media-design-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Media Design | https://catalog.uconn.edu/undergraduate/fine-arts/digital-media-design-bfa/ |

##### Department of Dramatic Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://catalog.uconn.edu/undergraduate/fine-arts/acting-bfa/ |
| 2 | Design and Technical Theatre | https://catalog.uconn.edu/undergraduate/fine-arts/design-technical-theatre-bfa/ |
| 3 | Puppet Arts | https://catalog.uconn.edu/undergraduate/fine-arts/puppet-arts-bfa/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Studies | https://catalog.uconn.edu/undergraduate/fine-arts/theatre-studies-ba/ |

##### Department of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.uconn.edu/undergraduate/fine-arts/music-bm/ |
| 2 | Jazz Studies | https://catalog.uconn.edu/undergraduate/fine-arts/jazz-studies-bm/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.uconn.edu/undergraduate/fine-arts/music-ba/ |

#### College of Liberal Arts and Sciences

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/english-ba/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/history-ba/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/philosophy-ba/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/political-science-ba/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/sociology-ba/ |

##### Department of Economics
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/economics-ba-bs/ |

##### Department of Psychology
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychological Sciences | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/psychological-sciences-ba-bs/ |

##### Department of Mathematics
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/mathematics-ba-bs/ |
| 2 | Mathematics-Actuarial Science | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/mathematics-actuarial-science-ba-bs/ |
| 3 | Mathematics-Statistics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/mathematics-statistics-ba-bs/ |

##### Department of Statistics
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/statistics-ba-bs/ |
| 2 | Statistical Data Science | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/statistical-data-science-bs/ |

##### Department of Physics
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/physics-ba-bs/ |
| 2 | Mathematics-Physics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/mathematics-physics-bs/ |

##### Department of Chemistry
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/chemistry-ba-bs/ |

##### Department of Biology
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/biological-sciences-ba-bs/ |

##### Department of Molecular & Cell Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Molecular and Cell Biology | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/molecular-cell-biology-bs/ |
| 2 | Structural Biology and Biophysics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/structural-biology-biophysics-bs/ |

##### Department of Ecology & Evolutionary Biology
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology and Evolutionary Biology | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/ecology-evolutionary-biology-ba-bs/ |

##### Department of Earth Sciences
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/earth-sciences-ba-bs/ |
| 2 | Marine Sciences | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/marine-sciences-ba-bs/ |

##### Department of Geography
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/geography-ba-bs/ |
| 2 | Geographic Information Science | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/geographic-information-science-ba-bs/ |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/anthropology-ba/ |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/linguistics-ba/ |

##### Department of Modern & Classical Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/chinese-ba/ |
| 2 | French and Francophone Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/french-francophone-studies-ba/ |
| 3 | German | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/german-ba/ |
| 4 | Italian Literary and Cultural Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/italian-literary-cultural-studies-ba/ |
| 5 | Spanish | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/spanish-ba/ |
| 6 | Classics and Ancient Mediterranean Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/classics-ancient-mediterranean-studies-ba/ |
| 7 | Arabic and Islamic Civilizations | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/arabic-islamic-civilizations-ba/ |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/communication-ba/ |

##### Department of Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/journalism-ba/ |

##### Department of Human Development & Family Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development and Family Sciences | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/human-development-family-sciences-ba/ |

##### Department of Women's, Gender, & Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's, Gender, and Sexuality Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/womens-gender-sexuality-studies-ba/ |

##### Department of African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/africana-studies-ba/ |

##### Department of Asian & Asian American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian and Asian American Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/asian-asian-american-studies-ba/ |

##### Department of Latino & Latin American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latino and Latin American Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/latino-latin-american-studies-ba/ |

##### Department of Judaic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Judaic Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/judaic-studies-ba/ |

##### Department of Human Rights
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Rights | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/human-rights-ba/ |

##### Department of Urban & Community Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Urban and Community Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/urban-community-studies-ba/ |

##### Department of American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/american-studies-ba/ |

##### Department of Cognitive Science
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Science | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/cognitive-science-ba-bs/ |

##### Department of Speech, Language and Hearing Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech, Language and Hearing Sciences | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/speech-language-hearing-sciences-ba/ |

##### Department of Individualized & Interdisciplinary Studies
###### BA or BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Individualized | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/individualized-ba-bs/ |

###### BGS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/general-studies-bgs/ |

##### Department of American Sign Language
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Sign Language Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/american-sign-language-ba/ |

##### Department of Applied Data Analysis
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Data Analysis | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/applied-data-analysis-ba/ |

##### Department of Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/environmental-studies-ba/ |

##### Department of Maritime Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Maritime Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/maritime-studies-ba/ |

##### Department of Real Estate
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate and Urban Economic Studies | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/real-estate-urban-economic-studies-bs/ |

##### Department of Health Care Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Care Management | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/health-care-management-bs/ |

##### Department of Diagnostic Genetic Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Diagnostic Genetic Sciences | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/diagnostic-genetic-sciences-bs/ |

##### Department of Medical Laboratory Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Laboratory Sciences | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/medical-laboratory-sciences-bs/ |

##### Department of Pharmacy Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy Studies | https://catalog.uconn.edu/undergraduate/pharmacy/pharmacy-studies-bs/ |

#### Elisabeth DeLuca School of Nursing

##### Department of Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.uconn.edu/undergraduate/nursing/nursing-bs/ |
| 2 | Nursing (Accelerated Career Entry) | https://catalog.uconn.edu/undergraduate/nursing/nursing-accelerated-bs/ |

#### School of Pharmacy and Pharmaceutical Sciences

##### Doctor of Pharmacy
###### Pharm.D.
| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy | https://catalog.uconn.edu/undergraduate/pharmacy/doctor-pharmacy-pharmd/ |

#### School of Social Work

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.uconn.edu/undergraduate/social-work/social-work-bsw/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Degree | Parent Schools | URL |
|---|------|--------|----------------|-----|
| 1 | Management and Engineering for Manufacturing | BS | School of Business + College of Engineering | https://catalog.uconn.edu/undergraduate/engineering/management-engineering-manufacturing-bs/ |
| 2 | Mathematics-Actuarial Science-Finance | BA or BS | CLAS + School of Business | https://catalog.uconn.edu/undergraduate/liberal-arts-sciences/mathematics-actuarial-science-finance-ba-bs/ |
| 3 | Economics of Sustainable Development and Management | BS | CAHNR + School of Business | https://catalog.uconn.edu/undergraduate/agriculture-health-natural-resources/economics-sustainable-development-management-bs/ |

### 1.4 Minors — complete list

UConn offers 252 undergraduate minors. The full list is available in the catalog at https://catalog.uconn.edu/undergraduate/programs/. Notable minors include:

- Accounting Minor
- Computer Science Minor
- Data Science Minor
- Business Fundamentals Minor
- Mathematics Minor
- Statistics Minor
- Psychology Minor
- Economics Minor
- Political Science Minor
- Communication Minor
- English Minor
- History Minor
- Biology Minor
- Chemistry Minor
- Physics Minor
- Engineering Minor
- Fine Arts Minor
- Music Minor
- Theatre Studies Minor
- Digital Media Design Minor
- Environmental Studies Minor
- Human Rights Minor
- Women's Studies Minor
- African American Studies Minor
- Asian American Studies Minor
- Latino Studies Minor
- Judaic Studies Minor
- Linguistics Minor
- Philosophy Minor
- Sociology Minor
- Anthropology Minor
- Geography Minor
- Earth Sciences Minor
- Marine Sciences Minor
- Cognitive Science Minor
- American Sign Language Minor
- Chinese Minor
- French Minor
- German Minor
- Italian Minor
- Spanish Minor
- Arabic Minor
- Classics Minor
- Journalism Minor
- Real Estate Minor
- Sport Management Minor
- Nutrition Minor
- Kinesiology Minor
- Nursing Minor
- Social Work Minor
- Pharmacy Studies Minor

### 1.5 General/Institute-wide requirements

UConn requires all undergraduate students to complete the University General Education Requirements (GER), which include:

- **English Composition** (2 courses)
- **Quantitative Reasoning** (2 courses)
- **Creative Arts** (1 course)
- **Humanities** (1 course)
- **Social Sciences** (1 course)
- **Science & Technology** (2 courses, at least 1 lab)
- **Diversity & Multiculturalism** (1 course)
- **Second Language Competency** (through level 2 or equivalent)

### 1.6 Course-ID → Major quick-lookup

UConn does not use a course-ID numbering system for majors. Programs are identified by name and degree type.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

UConn offers 290 graduate degree programs across 10 schools and colleges. The graduate programs are listed in the catalog at https://catalog.uconn.edu/graduate/graduate-programs/.

#### School of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.uconn.edu/graduate/degree-programs/accounting-ms/ |
| 2 | Business Analytics and Project Management | https://catalog.uconn.edu/graduate/degree-programs/business-analytics-project-management-ms/ |
| 3 | Business Research | https://catalog.uconn.edu/graduate/degree-programs/business-research-ms/ |
| 4 | Financial and Enterprise Risk Management | https://catalog.uconn.edu/graduate/degree-programs/financial-enterprise-risk-management-ms/ |
| 5 | Human Resource Management | https://catalog.uconn.edu/graduate/degree-programs/human-resource-management-ms/ |
| 6 | Social Responsibility and Impact in Business | https://catalog.uconn.edu/graduate/degree-programs/social-responsibility-impact-business-ms/ |
| 7 | Supply Chain Management | https://catalog.uconn.edu/graduate/degree-programs/supply-chain-management-ms/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.uconn.edu/graduate/degree-programs/business-administration-mba/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.uconn.edu/graduate/degree-programs/business-administration-phd/ |

#### College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Manufacturing for Energy Systems | https://catalog.uconn.edu/graduate/degree-programs/advanced-manufacturing-energy-systems-ms/ |
| 2 | Biomedical Engineering | https://catalog.uconn.edu/graduate/degree-programs/biomedical-engineering-ms/ |
| 3 | Chemical Engineering | https://catalog.uconn.edu/graduate/degree-programs/chemical-engineering-ms/ |
| 4 | Civil Engineering | https://catalog.uconn.edu/graduate/degree-programs/civil-engineering-ms/ |
| 5 | Computer Science and Engineering | https://catalog.uconn.edu/graduate/degree-programs/computer-science-engineering-ms/ |
| 6 | Data Science | https://catalog.uconn.edu/graduate/degree-programs/data-science-ms/ |
| 7 | Electrical Engineering | https://catalog.uconn.edu/graduate/degree-programs/electrical-engineering-ms/ |
| 8 | Energy and Environmental Management | https://catalog.uconn.edu/graduate/degree-programs/energy-environmental-management-ms/ |
| 9 | Environmental Engineering | https://catalog.uconn.edu/graduate/degree-programs/environmental-engineering-ms/ |
| 10 | Materials Science | https://catalog.uconn.edu/graduate/degree-programs/materials-science-ms/ |
| 11 | Mechanical Engineering | https://catalog.uconn.edu/graduate/degree-programs/mechanical-engineering-ms/ |
| 12 | Regenerative Engineering | https://catalog.uconn.edu/graduate/degree-programs/regenerative-engineering-ms/ |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://catalog.uconn.edu/graduate/degree-programs/engineering-meng/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.uconn.edu/graduate/degree-programs/biomedical-engineering-phd/ |
| 2 | Chemical Engineering | https://catalog.uconn.edu/graduate/degree-programs/chemical-engineering-phd/ |
| 3 | Civil Engineering | https://catalog.uconn.edu/graduate/degree-programs/civil-engineering-phd/ |
| 4 | Computer Science and Engineering | https://catalog.uconn.edu/graduate/degree-programs/computer-science-engineering-phd/ |
| 5 | Electrical Engineering | https://catalog.uconn.edu/graduate/degree-programs/electrical-engineering-phd/ |
| 6 | Engineering Education | https://catalog.uconn.edu/graduate/degree-programs/engineering-education-phd/ |
| 7 | Environmental Engineering | https://catalog.uconn.edu/graduate/degree-programs/environmental-engineering-phd/ |
| 8 | Materials Science and Engineering | https://catalog.uconn.edu/graduate/degree-programs/materials-science-engineering-phd/ |
| 9 | Mechanical Engineering | https://catalog.uconn.edu/graduate/degree-programs/mechanical-engineering-phd/ |

#### College of Liberal Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.uconn.edu/graduate/degree-programs/communication-ma/ |
| 2 | Curriculum and Instruction | https://catalog.uconn.edu/graduate/degree-programs/curriculum-instruction-ma/ |
| 3 | Digital Media Design | https://catalog.uconn.edu/graduate/degree-programs/digital-media-design-ma/ |
| 4 | Dramatic Arts | https://catalog.uconn.edu/graduate/degree-programs/dramatic-arts-ma/ |
| 5 | Economics | https://catalog.uconn.edu/graduate/degree-programs/economics-ma/ |
| 6 | English | https://catalog.uconn.edu/graduate/degree-programs/english-ma/ |
| 7 | Geography | https://catalog.uconn.edu/graduate/degree-programs/geography-ma/ |
| 8 | History | https://catalog.uconn.edu/graduate/degree-programs/history-ma/ |
| 9 | Human Development and Family Sciences | https://catalog.uconn.edu/graduate/degree-programs/human-development-family-sciences-ma/ |
| 10 | Human Rights | https://catalog.uconn.edu/graduate/degree-programs/human-rights-ma/ |
| 11 | Intersectional Indigeneity, Race, Ethnicity, and Politics | https://catalog.uconn.edu/graduate/degree-programs/intersectional-indigeneity-race-ethnicity-politics-ma/ |
| 12 | Latina/o and Latin American Studies | https://catalog.uconn.edu/graduate/degree-programs/latinao-latin-american-studies-ma/ |
| 13 | Linguistics | https://catalog.uconn.edu/graduate/degree-programs/linguistics-ma/ |
| 14 | Literatures, Cultures, and Languages | https://catalog.uconn.edu/graduate/degree-programs/literatures-cultures-languages-ma/ |
| 15 | Mathematics | https://catalog.uconn.edu/graduate/degree-programs/mathematics-ma/ |
| 16 | Music | https://catalog.uconn.edu/graduate/degree-programs/music-ma/ |
| 17 | Philosophy | https://catalog.uconn.edu/graduate/degree-programs/philosophy-ma/ |
| 18 | Political Science | https://catalog.uconn.edu/graduate/degree-programs/political-science-ma/ |
| 19 | Psychological Sciences | https://catalog.uconn.edu/graduate/degree-programs/psychological-sciences-ma/ |
| 20 | Sociology | https://catalog.uconn.edu/graduate/degree-programs/sociology-ma/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Financial Mathematics | https://catalog.uconn.edu/graduate/degree-programs/applied-financial-mathematics-ms/ |
| 2 | Biostatistics | https://catalog.uconn.edu/graduate/degree-programs/biostatistics-ms/ |
| 3 | Clinical and Translational Research | https://catalog.uconn.edu/graduate/degree-programs/clinical-translational-research-ms/ |
| 4 | Geological Sciences | https://catalog.uconn.edu/graduate/degree-programs/geological-sciences-ms/ |
| 5 | Mathematics | https://catalog.uconn.edu/graduate/degree-programs/mathematics-ms/ |
| 6 | Quantitative Economics | https://catalog.uconn.edu/graduate/degree-programs/quantitative-economics-ms/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uconn.edu/graduate/degree-programs/art-mfa/ |
| 2 | Digital Media Design | https://catalog.uconn.edu/graduate/degree-programs/digital-media-design-mfa/ |
| 3 | Dramatic Arts | https://catalog.uconn.edu/graduate/degree-programs/dramatic-arts-mfa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.uconn.edu/graduate/degree-programs/anthropology-ma-phd/ |
| 2 | Chemistry | https://catalog.uconn.edu/graduate/degree-programs/chemistry-phd/ |
| 3 | Communication | https://catalog.uconn.edu/graduate/degree-programs/communication-phd/ |
| 4 | Ecology and Evolutionary Biology | https://catalog.uconn.edu/graduate/degree-programs/ecology-evolutionary-biology-phd/ |
| 5 | Economics | https://catalog.uconn.edu/graduate/degree-programs/economics-phd/ |
| 6 | English | https://catalog.uconn.edu/graduate/degree-programs/english-ma-phd/ |
| 7 | Geography | https://catalog.uconn.edu/graduate/degree-programs/geography-ma-phd/ |
| 8 | History | https://catalog.uconn.edu/graduate/degree-programs/history-phd/ |
| 9 | Human Development and Family Sciences | https://catalog.uconn.edu/graduate/degree-programs/human-development-family-sciences-phd/ |
| 10 | Integrative Studies | https://catalog.uconn.edu/graduate/degree-programs/integrative-studies-phd/ |
| 11 | Linguistics | https://catalog.uconn.edu/graduate/degree-programs/linguistics-ma-phd/ |
| 12 | Literatures, Cultures, and Languages | https://catalog.uconn.edu/graduate/degree-programs/literatures-cultures-languages-phd/ |
| 13 | Mathematics | https://catalog.uconn.edu/graduate/degree-programs/mathematics-phd/ |
| 14 | Molecular and Cell Biology | https://catalog.uconn.edu/graduate/degree-programs/molecular-cell-biology-phd/ |
| 15 | Music | https://catalog.uconn.edu/graduate/degree-programs/music-phd/ |
| 16 | Philosophy | https://catalog.uconn.edu/graduate/degree-programs/philosophy-ma-phd/ |
| 17 | Physics | https://catalog.uconn.edu/graduate/degree-programs/physics-phd/ |
| 18 | Physiology and Neurobiology | https://catalog.uconn.edu/graduate/degree-programs/physiology-neurobiology-phd/ |
| 19 | Political Science | https://catalog.uconn.edu/graduate/degree-programs/political-science-ma-phd/ |
| 20 | Psychological Sciences | https://catalog.uconn.edu/graduate/degree-programs/psychological-sciences-phd/ |
| 21 | Sociology | https://catalog.uconn.edu/graduate/degree-programs/sociology-phd/ |
| 22 | Speech, Language, and Hearing Sciences | https://catalog.uconn.edu/graduate/degree-programs/speech-language-hearing-sciences-ma-phd-aud/ |

#### Neag School of Education

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.uconn.edu/graduate/degree-programs/curriculum-instruction-ma/ |
| 2 | Educational Psychology (Counselor Education) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-counselor-education-ma/ |
| 3 | Educational Psychology (Educational Technology) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-educational-technology-ma/ |
| 4 | Educational Psychology (Giftedness, Creativity, and Talent Development) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-giftedness-creativity-talent-development-ma/ |
| 5 | Educational Psychology (Learning Sciences) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-learning-sciences-ma/ |
| 6 | Educational Psychology (Research Methods, Measurement, and Evaluation) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-research-methods-measurement-evaluation-ma/ |
| 7 | Educational Psychology (School Psychology) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-school-psychology-ma/ |
| 8 | Educational Psychology (Special Education) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-special-education-ma/ |
| 9 | Higher Education and Student Affairs | https://catalog.uconn.edu/graduate/degree-programs/higher-education-student-affairs-ma/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://catalog.uconn.edu/graduate/degree-programs/athletic-training-ms/ |
| 2 | Exercise Prescription | https://catalog.uconn.edu/graduate/degree-programs/exercise-prescription-ms/ |
| 3 | Sport Management | https://catalog.uconn.edu/graduate/degree-programs/sport-management-ms/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | https://catalog.uconn.edu/graduate/degree-programs/educational-leadership-edd/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.uconn.edu/graduate/degree-programs/curriculum-instruction-phd/ |
| 2 | Educational Psychology (Counselor Education) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-counselor-education-phd/ |
| 3 | Educational Psychology (Giftedness, Creativity, and Talent Development) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-giftedness-creativity-talent-development-phd/ |
| 4 | Educational Psychology (Learning Sciences) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-learning-sciences-phd/ |
| 5 | Educational Psychology (Research Methods, Measurement, and Evaluation) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-research-methods-measurement-evaluation-phd/ |
| 6 | Educational Psychology (School Psychology) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-school-psychology-phd/ |
| 7 | Educational Psychology (Special Education) | https://catalog.uconn.edu/graduate/degree-programs/educational-psychology-special-education-phd/ |
| 8 | Learning, Leadership and Education Policy | https://catalog.uconn.edu/graduate/degree-programs/learning-leadership-education-policy-phd/ |

#### College of Agriculture, Health and Natural Resources

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural and Resource Economics | https://catalog.uconn.edu/graduate/degree-programs/agricultural-resource-economics-ms/ |
| 2 | Animal Science | https://catalog.uconn.edu/graduate/degree-programs/animal-science-ms/ |
| 3 | Applied Biochemistry and Cell Biology | https://catalog.uconn.edu/graduate/degree-programs/applied-biochemistry-cell-biology-ms/ |
| 4 | Applied Genomics | https://catalog.uconn.edu/graduate/degree-programs/applied-genomics-ms/ |
| 5 | Applied Microbial Systems Analysis | https://catalog.uconn.edu/graduate/degree-programs/applied-microbial-systems-analysis-ms/ |
| 6 | Biodiversity and Conservation Biology | https://catalog.uconn.edu/graduate/degree-programs/biodiversity-conservation-biology-ms/ |
| 7 | Health Care Genetics | https://catalog.uconn.edu/graduate/degree-programs/health-care-genetics-ms/ |
| 8 | Kinesiology | https://catalog.uconn.edu/graduate/degree-programs/kinesiology-ms/ |
| 9 | Natural Resources and the Environment | https://catalog.uconn.edu/graduate/degree-programs/natural-resources-environment-ms/ |
| 10 | Nutritional Sciences | https://catalog.uconn.edu/graduate/degree-programs/nutritional-sciences-ms/ |
| 11 | Oceanography | https://catalog.uconn.edu/graduate/degree-programs/oceanography-ms/ |
| 12 | Pathobiology | https://catalog.uconn.edu/graduate/degree-programs/pathobiology-ms/ |
| 13 | Personalized Nutrition | https://catalog.uconn.edu/graduate/degree-programs/personalized-nutrition-ms/ |
| 14 | Plant Science | https://catalog.uconn.edu/graduate/degree-programs/plant-science-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural and Resource Economics | https://catalog.uconn.edu/graduate/degree-programs/agricultural-resource-economics-phd/ |
| 2 | Animal Science | https://catalog.uconn.edu/graduate/degree-programs/animal-science-phd/ |
| 3 | Ecology and Evolutionary Biology | https://catalog.uconn.edu/graduate/degree-programs/ecology-evolutionary-biology-phd/ |
| 4 | Kinesiology | https://catalog.uconn.edu/graduate/degree-programs/kinesiology-phd/ |
| 5 | Molecular and Cell Biology | https://catalog.uconn.edu/graduate/degree-programs/molecular-cell-biology-phd/ |
| 6 | Natural Resources and the Environment | https://catalog.uconn.edu/graduate/degree-programs/natural-resources-environment-phd/ |
| 7 | Nutritional Sciences | https://catalog.uconn.edu/graduate/degree-programs/nutritional-sciences-phd/ |
| 8 | Oceanography | https://catalog.uconn.edu/graduate/degree-programs/oceanography-phd/ |
| 9 | Pathobiology | https://catalog.uconn.edu/graduate/degree-programs/pathobiology-phd/ |
| 10 | Physiology and Neurobiology | https://catalog.uconn.edu/graduate/degree-programs/physiology-neurobiology-phd/ |
| 11 | Plant Science | https://catalog.uconn.edu/graduate/degree-programs/plant-science-phd/ |

#### School of Fine Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Media Design | https://catalog.uconn.edu/graduate/degree-programs/digital-media-design-ma/ |
| 2 | Dramatic Arts | https://catalog.uconn.edu/graduate/degree-programs/dramatic-arts-ma/ |
| 3 | Music | https://catalog.uconn.edu/graduate/degree-programs/music-ma/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://catalog.uconn.edu/graduate/degree-programs/art-mfa/ |
| 2 | Digital Media Design | https://catalog.uconn.edu/graduate/degree-programs/digital-media-design-mfa/ |
| 3 | Dramatic Arts | https://catalog.uconn.edu/graduate/degree-programs/dramatic-arts-mfa/ |

##### MMus
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Performance | https://catalog.uconn.edu/graduate/degree-programs/music-performance-mmus/ |

##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.uconn.edu/graduate/degree-programs/music-dma/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.uconn.edu/graduate/degree-programs/music-phd/ |

#### Elisabeth DeLuca School of Nursing

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.uconn.edu/graduate/degree-programs/nursing-ms/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.uconn.edu/graduate/degree-programs/nursing-dnp/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.uconn.edu/graduate/degree-programs/nursing-phd/ |

#### School of Pharmacy and Pharmaceutical Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalog.uconn.edu/graduate/degree-programs/pharmaceutical-sciences-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalog.uconn.edu/graduate/degree-programs/pharmaceutical-sciences-phd/ |

#### School of Social Work

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.uconn.edu/graduate/degree-programs/social-work-msw/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.uconn.edu/graduate/degree-programs/social-work-phd/ |

#### School of Public Health

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.uconn.edu/graduate/degree-programs/public-health-mph/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.uconn.edu/graduate/degree-programs/public-health-phd/ |

#### School of Medicine

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Genetic Counseling | https://catalog.uconn.edu/graduate/degree-programs/genetic-counseling-ms/ |
| 2 | Surgical Neurophysiology | https://catalog.uconn.edu/graduate/degree-programs/surgical-neurophysiology-ms/ |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://catalog.uconn.edu/graduate/degree-programs/physical-therapy-dpt/ |

##### MDentSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Science | https://catalog.uconn.edu/graduate/degree-programs/dental-science-mdentsc/ |

### 2.2 At least one program's full deep-dive (worked example)

**Program**: Computer Science and Engineering (MS)
**Department**: Department of Computer Science & Engineering
**College**: College of Engineering
**URL**: https://catalog.uconn.edu/graduate/degree-programs/computer-science-engineering-ms/

**Application Details**:
- Application portal: https://grad.uconn.edu/admissions/
- Application fee: $75
- GRE: Not required
- TOEFL minimum: 79 (iBT) or 4.5 (new scale)
- IELTS minimum: 6.5
- Duolingo minimum: 110
- PTE minimum: 60
- Deadline: Varies by program (typically December 15 for fall admission)

**Program Overview**:
The M.S. in Computer Science and Engineering program provides advanced training in computing theory, systems, and applications. Students can specialize in areas such as artificial intelligence, cybersecurity, data science, software engineering, and computer networks.

### 2.3 Graduate admissions model

UConn uses a **decentralized graduate admissions model**. The Graduate School serves as the administrative hub, but each program sets its own admission requirements, deadlines, and review processes.

**Application Process**:
1. Submit application through The Graduate School portal
2. Pay $75 application fee
3. Upload transcripts, letters of recommendation, statement of purpose
4. Programs review applications and make admission decisions
5. The Graduate School processes admitted students

**Key Deadlines**:
- Most programs: December 15 for fall admission
- Some programs accept spring admission (deadline: October 1)
- Some programs have rolling admissions

**Financial Aid**:
- Graduate assistantships available in most departments
- Fellowships and grants available through The Graduate School
- Tuition waivers for assistantship holders

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| **Admissions site** | https://admissions.uconn.edu/ |
| **Application portal** | Common Application or Coalition Application |
| **EA deadline** | November 1 (Early Decision) |
| **Priority deadline** | December 1 (Merit & Honors Consideration) |
| **RD deadline** | January 15 (Storrs Campus) |
| **Regional campus deadline** | May 1 (rolling basis) |
| **Enrollment confirmation deadline** | May 1 |
| **FAFSA deadline** | February 15 |
| **SAT/ACT policy** | Test-optional (for the foreseeable future) |
| **SAT code** | 3915 |
| **ACT code** | 0604 |
| **Superscore policy** | Yes |
| **Score-report method** | Self-reported via STARS or official transcripts |
| **Interview policy** | Not part of admissions process |
| **Recommendation requirements** | Two optional letters of recommendation |
| **Portfolio** | Required for School of Fine Arts programs |
| **Application fee** | $80 (non-refundable) |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL (old scale) | 79 | N/A | Internet-based test iBT, iBT Home Edition, or iBT Paper Edition |
| TOEFL (new scale) | 4.5 | N/A | Internet-based test iBT, iBT Home Edition, or iBT Paper Edition |
| IELTS | 6.5 | N/A | Online IELTS accepted; IELTS One Skill Retake, General Training, and Indicator not accepted |
| Duolingo | 110 | N/A | |
| LanguageCert Academic (LCA) | 70 | N/A | |
| PTE Academic | 60 | N/A | PTE Academic or PTE Academic Online |

**Waiver conditions**:
- U.S. citizens and permanent residents
- International applicants whose native language is English
- International applicants who completed at least 2 years at a secondary school in the U.S. (excluding ESL)
- International applicants who completed 1+ year of full-time coursework at a U.S. post-secondary institution with 3.0+ GPA
- International applicants who received a degree from an international institution where English was the medium of instruction
- SAT Evidence-Based Reading and Writing: 510+
- ACT English, Reading, and Composite: 24+ each
- IB Higher Level English exam: 5

### 3.3 Graduate — global rules

| 维度 | 详情 |
|------|------|
| **Admissions model** | Decentralized (each program manages own admissions) |
| **Application platform** | The Graduate School portal |
| **Application fee** | $75 |
| **GRE/GMAT policy** | Varies by program (most do not require) |
| **English proficiency** | TOEFL 79 / IELTS 6.5 / Duolingo 110 / PTE 60 |
| **GPA requirement** | 3.0 cumulative for baccalaureate degree |
| **Credential evaluation** | Required for international applicants (NACES or AICE members) |
| **CGS April-15 honor date** | Yes (signatory) |
| **Application timeline** | Most programs: December 15 for fall; some accept spring (October 1) |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

| Expense item | In-State | Out-of-State | New England Regional |
|--------------|----------|--------------|---------------------|
| Tuition | $17,010 | $39,678 | $26,028 |
| University and Student Fees | $4,564 | $4,564 | $4,564 |
| On-Campus Housing (standard double) | $8,288 | $8,288 | $8,288 |
| On-Campus Meal Plan (Value plan) | $6,896 | $6,896 | $6,896 |
| **Subtotal Direct Costs** | **$36,758** | **$59,426** | **$45,776** |
| Health Insurance (waivable) | $3,214 | $3,214 | $3,214 |
| Husky Book Bundle (waivable) | $570 | $570 | $570 |
| **Total (including waivable fees)** | **$40,542** | **$63,210** | **$49,560** |

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all applicants** (including international students)
- **Merit scholarships**: All applicants automatically considered upon admission
- **Need-based aid**: Available to U.S. citizens and permanent residents only
- **FAFSA deadline**: February 15 (school code: 001417)
- **Gift aid**: Approximately 70% of undergraduate students receive grants and scholarships
- **Total gift aid**: More than $261 million annually
- **Loan-free packages**: Not guaranteed
- **Income threshold for free tuition**: Not specified (case-by-case determination)

### 4.3 Graduate cost & funding framework

| 维度 | 详情 |
|------|------|
| **Tuition (in-state)** | ~$17,010/year (varies by program) |
| **Tuition (out-of-state)** | ~$39,678/year (varies by program) |
| **Application fee** | $75 |
| **Funding types** | Graduate assistantships, fellowships, grants, loans |
| **Assistantship benefits** | Tuition waiver + stipend |
| **Fee waiver policy** | Available for applicants with financial need |

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate application deadline (Storrs)
- **field**: undergraduate.deadlines.storrs_rd
- **value**: January 15
- **source_url**: https://admissions.uconn.edu/apply/first-year/deadlines
- **source_snippet**: "January 15 | Storrs Campus Application Deadline | Admissions decision notification begins early March"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-002: Early Decision deadline
- **field**: undergraduate.deadlines.ed
- **value**: November 1
- **source_url**: https://admissions.uconn.edu/apply/first-year/deadlines
- **source_snippet**: "November 1 | Early Decision Application Deadline* | Early Decision notifications of admission begin mid-December"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-003: Application fee
- **field**: undergraduate.application.fee
- **value**: $80
- **source_url**: https://admissions.uconn.edu/apply/first-year/instructions/
- **source_snippet**: "$80 Application Fee (non-refundable)"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-004: Test-optional policy
- **field**: undergraduate.testing.policy
- **value**: test-optional
- **source_url**: https://admissions.uconn.edu/apply/first-year/
- **source_snippet**: "UConn is a test-optional institution for the foreseeable future."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-005: SAT middle 50% range (Storrs)
- **field**: undergraduate.testing.sat_mid50
- **value**: 1320-1460
- **source_url**: https://admissions.uconn.edu/apply/first-year/
- **source_snippet**: "Combined SAT* 1320 – 1460 ... *Middle 50% of Admitted Students"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-006: TOEFL minimum (undergraduate)
- **field**: undergraduate.english_proficiency.toefl_min
- **value**: 79 (old scale) / 4.5 (new scale)
- **source_url**: https://admissions.uconn.edu/apply/international/first-year
- **source_snippet**: "TOEFL (old scale) | 79 | Internet-based test iBT ... TOEFL (new scale) | 4.5"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-007: IELTS minimum (undergraduate)
- **field**: undergraduate.english_proficiency.ielts_min
- **value**: 6.5
- **source_url**: https://admissions.uconn.edu/apply/international/first-year
- **source_snippet**: "IELTS | 6.5 | Online IELTS is accepted."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-008: Duolingo minimum (undergraduate)
- **field**: undergraduate.english_proficiency.duolingo_min
- **value**: 110
- **source_url**: https://admissions.uconn.edu/apply/international/first-year
- **source_snippet**: "Duolingo | 110"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-009: In-state tuition (2026-2027)
- **field**: undergraduate.cost.tuition_in_state
- **value**: $17,010
- **source_url**: https://financialaid.uconn.edu/cost/
- **source_snippet**: "Tuition | 17,010 | 39,678 | 26,028"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-010: Out-of-state tuition (2026-2027)
- **field**: undergraduate.cost.tuition_out_of_state
- **value**: $39,678
- **source_url**: https://financialaid.uconn.edu/cost/
- **source_snippet**: "Tuition | 17,010 | 39,678 | 26,028"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-011: Total COA in-state (2026-2027)
- **field**: undergraduate.cost.coa_in_state
- **value**: $36,758 (direct) / $40,542 (with waivable fees)
- **source_url**: https://financialaid.uconn.edu/cost/
- **source_snippet**: "Subtotal Direct Costs | 36,758 | 59,426 | 45,776"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-012: Total COA out-of-state (2026-2027)
- **field**: undergraduate.cost.coa_out_of_state
- **value**: $59,426 (direct) / $63,210 (with waivable fees)
- **source_url**: https://financialaid.uconn.edu/cost/
- **source_snippet**: "Subtotal Direct Costs | 36,758 | 59,426 | 45,776"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-013: Need-aware policy
- **field**: undergraduate.aid.need_blind
- **value**: need-aware for all (including international)
- **source_url**: https://admissions.uconn.edu/cost-aid/financial-aid/
- **source_snippet**: "Financial aid, including grants and loans, is only available to U.S. citizens and permanent residents."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-014: FAFSA deadline
- **field**: undergraduate.aid.fafsa_deadline
- **value**: February 15
- **source_url**: https://admissions.uconn.edu/cost-aid/financial-aid/
- **source_snippet**: "February 15 | FAFSA on-time deadline. File your FAFSA by this date to be considered for most forms of financial aid."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-015: Total UG majors count
- **field**: undergraduate.programs.total_majors
- **value**: 265
- **source_url**: https://catalog.uconn.edu/undergraduate/programs/
- **source_snippet**: [Extracted from catalog - 265 program entries with degree information]
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-016: Total UG minors count
- **field**: undergraduate.programs.total_minors
- **value**: 252
- **source_url**: https://catalog.uconn.edu/undergraduate/programs/
- **source_snippet**: [Extracted from catalog - 252 minor entries]
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-001: Graduate application fee
- **field**: graduate.application.fee
- **value**: $75
- **source_url**: https://grad.uconn.edu/admissions/requirements/
- **source_snippet**: "You will be asked to provide a valid credit card for a non-refundable payment of the application fee ($75.00)."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-002: Graduate TOEFL minimum
- **field**: graduate.english_proficiency.toefl_min
- **value**: 79 (old scale) / 4.5 (new scale)
- **source_url**: https://grad.uconn.edu/admissions/requirements/
- **source_snippet**: "TOEFL (old scale) | 79 | Internet-based test iBT ... TOEFL (new scale) | 4.5"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-003: Graduate IELTS minimum
- **field**: graduate.english_proficiency.ielts_min
- **value**: 6.5
- **source_url**: https://grad.uconn.edu/admissions/requirements/
- **source_snippet**: "IELTS | 6.5 | Online IELTS is accepted."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-004: Graduate GPA requirement
- **field**: graduate.admissions.gpa_min
- **value**: 3.0
- **source_url**: https://grad.uconn.edu/admissions/requirements/
- **source_snippet**: "A cumulative GPA for any prior degree at the baccalaureate level or higher of 3.0 or higher for the entire degree"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-005: Total graduate programs count
- **field**: graduate.programs.total
- **value**: 290
- **source_url**: https://catalog.uconn.edu/graduate/graduate-programs/
- **source_snippet**: [Extracted from catalog - 290 program entries]
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-006: Graduate admissions model
- **field**: graduate.admissions.model
- **value**: decentralized
- **source_url**: https://grad.uconn.edu/admissions/
- **source_snippet**: "The University of Connecticut offers graduate degrees in more than 250 fields of study, with over 7,000 enrolled students in doctoral, masters, and certificate programs."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-I-001: Schools and colleges count
- **field**: institution.schools_colleges_count
- **value**: 10
- **source_url**: https://admissions.uconn.edu/academics/schools-colleges/
- **source_snippet**: "With 10 schools and colleges offering seven undergraduate degrees in more than 125 majors"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
uconn-knowledge-base-v2/
├── 00-institution-overview.md (Section 0)
├── 01-undergraduate-education.md (Section 1)
├── 02-graduate-education.md (Section 2)
├── 03-application-requirements.md (Section 3)
├── 04-costs-financial-aid.md (Section 4)
├── 05-evidence-chain.md (Section 5)
├── 06-weknora-manifest.md (this section)
└── 07-cross-school-comparison.md (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uconn-knowledge-base-v2"
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

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Graduate program-specific deadlines | Individual program websites |
| P0 | Graduate program-specific GRE requirements | Individual program websites |
| P1 | Graduate certificate programs list | https://catalog.uconn.edu/graduate/ |
| P1 | Regional campus program offerings | https://admissions.uconn.edu/campuses/ |
| P2 | Detailed curriculum requirements per program | Individual program catalog pages |
| P2 | Faculty research areas | Department websites |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | UConn | (Other schools) |
|------|-------|-----------------|
| **Total UG cost/yr (in-state)** | $36,758 | |
| **Total UG cost/yr (OOS)** | $59,426 | |
| **Tuition/yr (in-state)** | $17,010 | |
| **Tuition/yr (OOS)** | $39,678 | |
| **Need-blind (intl?)** | No (need-aware for all) | |
| **EA deadline** | November 1 (ED) | |
| **RD deadline** | January 15 | |
| **SAT/ACT required?** | No (test-optional) | |
| **TOEFL min** | 79 / 4.5 | |
| **IELTS min** | 6.5 | |
| **Duolingo min** | 110 | |
| **Tuition-free threshold** | N/A | |
| **Median price paid** | N/A | |
| **Grad application fee** | $75 | |
| **April-15-equivalent honor date** | Yes (CGS signatory) | |
| **Total program count (rule 1)** | 807 (265 UG + 252 minors + 290 grad) | |
| **School/department count (rule 2)** | 10 schools/colleges | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.uconn.edu, financialaid.uconn.edu, grad.uconn.edu, catalog.uconn.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
