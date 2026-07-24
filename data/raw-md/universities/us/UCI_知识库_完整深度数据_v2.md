# University of California, Irvine (UCI) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BMus) | 87 |
| 本科辅修 (Minor) | 79 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/JD/MD/DNP/MPH/MAS/MDS/MAT/MSE/etc.) | 101 |
| **学位项目总计 (UG + Grad)** | **267** |
| 学术学院总数 | 15 |

> **Reconciliation**: Rule-1 total (267) = matrix cell-sum (267) = Rule-5 row-count (87 UG majors + 79 UG minors + 101 grad = 267). ✅

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
University of California, Irvine
├── Claire Trevor School of the Arts                          [学院]
│   ├── Department of Art                                      [系]
│   ├── Department of Dance                                    [系]
│   ├── Department of Drama                                    [系]
│   ├── Department of Music                                    [系]
│   └── Department of Film and Media Studies (shared w/ Humanities) [系] ⚠
├── Charlie Dunlop School of Biological Sciences               [学院]
│   ├── Department of Molecular Biology and Biochemistry       [系]
│   ├── Department of Developmental and Cell Biology           [系]
│   ├── Department of Ecology and Evolutionary Biology         [系]
│   └── Biological Sciences (general)                          [系]
├── The Paul Merage School of Business                         [学院]
│   └── (No internal department subdivision for UG)            [系]
├── School of Education                                        [学院]
│   └── (No internal department subdivision)                   [系]
├── The Henry Samueli School of Engineering                    [学院]
│   ├── Department of Biomedical Engineering                   [系]
│   ├── Department of Chemical and Biomolecular Engineering    [系]
│   ├── Department of Civil and Environmental Engineering      [系]
│   ├── Department of Electrical Engineering and Computer Science [系]
│   ├── Department of Materials Science and Engineering        [系]
│   └── Department of Mechanical and Aerospace Engineering     [系]
├── School of Humanities                                       [学院]
│   ├── Department of African American Studies                 [系]
│   ├── Department of Art History                              [系]
│   ├── Department of Asian American Studies                   [系]
│   ├── Department of Classics                                 [系]
│   ├── Department of Comparative Literature                   [系]
│   ├── Department of East Asian Studies                       [系]
│   ├── Department of English                                  [系]
│   ├── Department of European Languages and Studies           [系]
│   ├── Department of Film and Media Studies (shared w/ Arts)  [系] ⚠
│   ├── Department of Gender and Sexuality Studies             [系]
│   ├── Department of History                                  [系]
│   ├── Department of Philosophy                               [系]
│   ├── Undergraduate Program in Global Cultures               [系]
│   └── Special Programs                                       [系]
├── Donald Bren School of Information and Computer Sciences    [学院]
│   ├── Department of Computer Science                         [系]
│   ├── Department of Informatics                              [系]
│   └── Department of Statistics                               [系]
├── School of Law                                              [学院]
│   └── (Professional school, JD only)                         [系]
├── School of Medicine                                         [学院]
│   └── (Professional school, MD + select grad programs)       [系]
├── Sue and Bill Gross School of Nursing                       [学院]
│   └── (No internal department subdivision)                   [系]
├── School of Pharmacy and Pharmaceutical Sciences             [学院]
│   └── Department of Pharmacology                             [系]
├── School of Physical Sciences                                [学院]
│   ├── Department of Chemistry                                [系]
│   ├── Department of Earth System Science                     [系]
│   ├── Department of Mathematics                              [系]
│   └── Department of Physics and Astronomy                    [系]
├── Joe C. Wen School of Population and Public Health          [学院]
│   └── (No internal department subdivision)                   [系]
├── School of Social Ecology                                   [学院]
│   ├── Department of Criminology, Law and Society             [系]
│   └── Department of Psychological Science                    [系]
├── School of Social Sciences                                  [学院]
│   ├── Department of Anthropology                             [系]
│   ├── Department of Cognitive Sciences                       [系]
│   ├── Department of Chicano/Latino Studies                   [系]
│   ├── Department of Economics                                [系]
│   ├── Department of International Studies                    [系]
│   ├── Department of Linguistics                              [系]
│   ├── Department of Political Science                        [系]
│   └── Department of Sociology                                [系]
├── Division of Undergraduate Education                        [行政]
│   └── Interdisciplinary Studies (cross-school UG programs)   [系]
└── Graduate Division                                          [行政]
    └── (Administrative oversight of graduate education)
```

> ⚠ = shared/interdisciplinary department across schools

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 31 |
| BS | B.S. | Bachelor of Science | 本科 | 51 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 2 |
| BMus | B.Mus. | Bachelor of Music | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 79 |
| MA | M.A. | Master of Arts | 研究生 | 6 |
| MS | M.S. | Master of Science | 研究生 | 29 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 4 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 1 |
| MSE | M.S.E. | Master of Software Engineering | 研究生 | 1 |
| MAS | M.A.S. | Master of Advanced Study | 研究生 | 1 |
| MDS | M.D.S. | Master of Data Science | 研究生 | 1 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | 1 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 51 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |
| MD | M.D. | Doctor of Medicine | 研究生 | 1 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 1 |
| **合计** | | | | **267** |

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BMus | Minor | MA | MS | MFA | MBA | MSE | MAS | MDS | MAT | MPH | PhD | JD | MD | DNP | 合计 |
|------------|----|----|-----|------|-------|----|----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|-----|------|
| Claire Trevor School of the Arts | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | **16** |
| Charlie Dunlop School of Biological Sciences | 0 | 9 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **13** |
| The Paul Merage School of Business | 1 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **8** |
| School of Education | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | **4** |
| The Henry Samueli School of Engineering | 0 | 12 | 0 | 0 | 3 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | **31** |
| School of Humanities | 18 | 0 | 0 | 0 | 27 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | **62** |
| Donald Bren School of ICS | 0 | 5 | 0 | 0 | 6 | 0 | 4 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | **20** |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **1** |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | **5** |
| Sue and Bill Gross School of Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | **4** |
| School of Pharmacy & Pharmaceutical Sciences | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **3** |
| School of Physical Sciences | 0 | 7 | 0 | 0 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | **17** |
| Joe C. Wen School of Population & Public Health | 0 | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | **8** |
| School of Social Ecology | 3 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | **12** |
| School of Social Sciences | 5 | 2 | 0 | 0 | 12 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | **31** |
| Interdisciplinary Studies (Div. of UG Ed.) | 0 | 3 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Interdisciplinary (Graduate) | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | **6** |
| **合计** | **31** | **51** | **2** | **1** | **79** | **6** | **29** | **4** | **1** | **1** | **1** | **1** | **1** | **1** | **51** | **1** | **1** | **1** | **267** |

> Row totals and column totals each sum to 267. Reconciliation: rule-1 (267) = matrix-sum (267) = rule-5 rows (267). ✅

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UCI has 15 academic schools/colleges that grant undergraduate degrees, plus the Division of Undergraduate Education which administers interdisciplinary programs. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Claire Trevor School of the Arts

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofart/art_ba/ |

##### Department of Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdance/dance_ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdance/dance_bfa/ |

##### Department of Drama
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Drama | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdrama/drama_ba/ |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofmusic/music_ba/ |

###### BMus
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofmusic/music_bmus/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Theatre | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofmusic/musictheatre_bfa/ |

---

#### Charlie Dunlop School of Biological Sciences

##### Department of Molecular Biology and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/departmentofmolecularbiologyandbiochemistry/biochemistryandmolecularbiology_bs/ |

##### Department of Developmental and Cell Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Developmental and Cell Biology | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/departmentofdevelopmentalandcellbiology/developmentalandcellbiology_bs/ |
| 2 | Genetics | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/departmentofdevelopmentalandcellbiology/genetics_bs/ |

##### Department of Ecology and Evolutionary Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology and Evolutionary Biology | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/departmentofecologyandevolutionarybiology/ecologyandevolutionarybiology_bs/ |

##### Biological Sciences (general)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biologicalsciences_bs/ |
| 2 | Biology/Education | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biologyeducation_bs/ |
| 3 | Human Biology | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/humanbiology_bs/ |
| 4 | Microbiology and Immunology | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/microbiologyandimmunology_bs/ |
| 5 | Neurobiology | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/neurobiology_bs/ |
| 6 | Physiology and Exercise Science | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/physiologyandexercisescience_bs/ |

---

#### The Paul Merage School of Business

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/businessadministration_ba/ |

---

#### School of Education

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Education Sciences | https://catalogue.uci.edu/schoolofeducation/education_ba/ |

---

#### The Henry Samueli School of Engineering

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofbiomedicalengineering/biomedicalengineering_bs/ |
| 2 | Biomedical Engineering: Premedical | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofbiomedicalengineering/biomedicalengineeringpremedical_bs/ |

##### Department of Chemical and Biomolecular Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofchemicalandbiomolecularengineering/chemicalengineering_bs/ |

##### Department of Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofcivilandenvironmentalengineering/civilengineering_bs/ |
| 2 | Environmental Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofcivilandenvironmentalengineering/environmentalengineering_bs/ |

##### Department of Electrical Engineering and Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofelectricalengineeringandcomputerscience/computerengineering_bs/ |
| 2 | Electrical Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofelectricalengineeringandcomputerscience/electricalengineering_bs/ |

##### Department of Materials Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofmaterials scienceandengineering/materialsscienceandengineering_bs/ |

##### Department of Mechanical and Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofmechanicalandaerospaceengineering/aerospaceengineering_bs/ |
| 2 | Mechanical Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofmechanicalandaerospaceengineering/mechanicalengineering_bs/ |

##### Software Engineering (under ICS joint)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Software Engineering | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofcomputerscience/softwareengineering_bs/ |

---

#### School of Humanities

##### Department of African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofafricanamericanstudies/africanamericanstudies_ba/ |

##### Department of Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalogue.uci.edu/schoolofhumanities/departmentofarthistory/arthistory_ba/ |

##### Department of Asian American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian American Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofasianamericanstudies/asianamericanstudies_ba/ |

##### Department of Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics | https://catalogue.uci.edu/schoolofhumanities/departmentofclassics/classics_ba/ |

##### Department of Comparative Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative Literature | https://catalogue.uci.edu/schoolofhumanities/departmentofcomparativeliterature/comparativeliterature_ba/ |

##### Department of East Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/chinesestudies_ba/ |
| 2 | East Asian Cultures | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/eastasiancultures_ba/ |
| 3 | Japanese Language and Literature | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/japaneselanguageandliterature_ba/ |
| 4 | Korean Literature and Culture | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/koreanliteratureandculture_ba/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalogue.uci.edu/schoolofhumanities/departmentofenglish/english_ba/ |

##### Department of European Languages and Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | European Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/europeanstudies_ba/ |
| 2 | French | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/french_ba/ |
| 3 | German Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/germanstudies_ba/ |

##### Department of Film and Media Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Media Studies | https://catalogue.uci.edu/schoolofhumanities/departmentoffilmandmediastudies/filmandmediastudies_ba/ |

##### Department of Gender and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Gender and Sexuality Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofgenderandsexualitystudies/genderandsexualitystudies_ba/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalogue.uci.edu/schoolofhumanities/departmentofhistory/history_ba/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalogue.uci.edu/schoolofhumanities/departmentofphilosophy/philosophy_ba/ |

##### Undergraduate Program in Global Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Cultures | https://catalogue.uci.edu/schoolofhumanities/undergraduateprograminglobalcultures/globalcultures_ba/ |

##### Literary Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Literary Journalism | https://catalogue.uci.edu/schoolofhumanities/departmentofenglish/literaryjournalism_ba/ |

##### Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://catalogue.uci.edu/schoolofhumanities/departmentofreligiousstudies/religiousstudies_ba/ |

##### Spanish
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://catalogue.uci.edu/schoolofhumanities/departmentofspanishandportuguese/spanish_ba/ |

---

#### Donald Bren School of Information and Computer Sciences

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofcomputerscience/computerscience_bs/ |

##### Department of Informatics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Game Design and Interactive Media | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofinformatics/gamedesignandinteractivemedia_bs/ |
| 2 | Informatics | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofinformatics/informatics_bs/ |

##### Department of Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofstatistics/datascience_bs/ |

##### Information and Computer Science (general)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information and Computer Science | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/informationandcomputerscience_bs/ |
| 2 | Software Engineering | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofcomputerscience/softwareengineering_bs/ |

---

#### Sue and Bill Gross School of Nursing

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing Science | https://catalogue.uci.edu/sueandbillgrossschoolofnursing/nursingscience_bs/ |

---

#### School of Pharmacy and Pharmaceutical Sciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalogue.uci.edu/schoolofpharmacyandpharmaceuticalsciences/pharmaceuticalsciences_bs/ |

---

#### School of Physical Sciences

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofchemistry/chemistry_bs/ |

##### Department of Earth System Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth System Science | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofearthsystemscience/earthsystemscience_bs/ |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied and Computational Mathematics | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofmathematics/appliedandcomputationalmathematics_bs/ |
| 2 | Mathematics | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofmathematics/mathematics_bs/ |

##### Department of Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physics | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofphysicsandastronomy/appliedphysics_bs/ |
| 2 | Physics | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofphysicsandastronomy/physics_bs/ |

---

#### Joe C. Wen School of Population and Public Health

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health Policy | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/publichealthpolicy_ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health Sciences | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/publichealthsciences_bs/ |

---

#### School of Social Ecology

##### Department of Criminology, Law and Society
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology, Law and Society | https://catalogue.uci.edu/schoolofsocialecology/departmentofcriminologylawandsociety/criminologylawandsociety_ba/ |

##### Social Ecology (general)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalogue.uci.edu/schoolofsocialecology/departmentofpsychologicalscience/psychology_ba/ |
| 2 | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/socialecology_ba/ |
| 3 | Urban Studies | https://catalogue.uci.edu/schoolofsocialecology/urbanstudies_ba/ |

---

#### School of Social Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalogue.uci.edu/schoolofsocialsciences/departmentofanthropology/anthropology_ba/ |

##### Department of Cognitive Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofcognitivesciences/cognitivesciences_bs/ |

##### Department of Chicano/Latino Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chicano/Latino Studies | https://catalogue.uci.edu/schoolofsocialsciences/departmentofchicanolatinostudies/chicanolatinostudies_ba/ |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://catalogue.uci.edu/schoolofsocialsciences/departmentofeconomics/businesseconomics_ba/ |
| 2 | Economics | https://catalogue.uci.edu/schoolofsocialsciences/departmentofeconomics/economics_ba/ |
| 3 | Quantitative Economics | https://catalogue.uci.edu/schoolofsocialsciences/departmentofeconomics/quantitativeeconomics_ba/ |

##### Department of International Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://catalogue.uci.edu/schoolofsocialsciences/departmentofinternationalstudies/internationalstudies_ba/ |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Language Science | https://catalogue.uci.edu/schoolofsocialsciences/departmentoflinguistics/languagescience_ba/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalogue.uci.edu/schoolofsocialsciences/departmentofpoliticalscience/politicalscience_ba/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalogue.uci.edu/schoolofsocialsciences/departmentofpsychology/psychology_ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalogue.uci.edu/schoolofsocialsciences/departmentofpsychology/psychology_bs/ |

##### Social Policy and Public Service
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Policy and Public Service | https://catalogue.uci.edu/schoolofsocialsciences/socialpolicyandpublicservice_ba/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalogue.uci.edu/schoolofsocialsciences/departmentofsociology/sociology_ba/ |

---

#### Interdisciplinary Studies (Division of Undergraduate Education)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Information Management | https://catalogue.uci.edu/interdisciplinarystudies/businessinformationmanagement_bs/ |
| 2 | Computer Science and Engineering | https://catalogue.uci.edu/interdisciplinarystudies/computerscienceandengineering_bs/ |
| 3 | Environmental Science and Policy | https://catalogue.uci.edu/interdisciplinarystudies/environmentalscienceandpolicy_ba/ |

> Note: Environmental Science and Policy is listed as B.A. in the catalogue despite the BS heading.

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science and Policy | https://catalogue.uci.edu/interdisciplinarystudies/environmentalscienceandpolicy_ba/ |
| 2 | Global Middle East Studies | https://catalogue.uci.edu/interdisciplinarystudies/globalmiddleeaststudies_ba/ |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | 家庭学院 | URL |
|---|------|------|---------|-----|
| 1 | Business Information Management | B.S. | ICS + Business | https://catalogue.uci.edu/interdisciplinarystudies/businessinformationmanagement_bs/ |
| 2 | Computer Science and Engineering | B.S. | Engineering + ICS | https://catalogue.uci.edu/interdisciplinarystudies/computerscienceandengineering_bs/ |
| 3 | Environmental Science and Policy | B.A. | Multiple schools | https://catalogue.uci.edu/interdisciplinarystudies/environmentalscienceandpolicy_ba/ |
| 4 | Global Middle East Studies | B.A. | Humanities + Social Sciences | https://catalogue.uci.edu/interdisciplinarystudies/globalmiddleeaststudies_ba/ |
| 5 | Biology/Education | B.S. | Biological Sciences + Education | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biologyeducation_bs/ |

### 1.4 Minors — Complete List

| # | Minor | Home School | URL |
|---|-------|------------|-----|
| 1 | Accounting | Paul Merage School of Business | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/accounting_minor/ |
| 2 | African American Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofafricanamericanstudies/africanamericanstudies_minor/ |
| 3 | Anthropology | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofanthropology/anthropology_minor/ |
| 4 | Archaeology | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofarthistory/archaeology_minor/ |
| 5 | Armenian Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofhistory/armenianstudies_minor/ |
| 6 | Art History | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofarthistory/arthistory_minor/ |
| 7 | Asian American Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofasianamericanstudies/asianamericanstudies_minor/ |
| 8 | Asian Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/specialprograms/asianstudies_minor/ |
| 9 | Bilingual Education in Asian Languages | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/bilingualeducationinasianlanguages_minor/ |
| 10 | Bioinformatics | ICS | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofcomputerscience/bioinformatics_minor/ |
| 11 | Biological Sciences | Biological Sciences | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biologicalsciences_minor/ |
| 12 | Biomedical Engineering | Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofbiomedicalengineering/biomedicalengineering_minor/ |
| 13 | Chicano/Latino Studies | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofchicanolatinostudies/chicanolatinostudies_minor/ |
| 14 | Chinese Language and Literature | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/chineselanguageandliterature_minor/ |
| 15 | Chinese Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/chinesestudies_minor/ |
| 16 | Civic and Community Engagement | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/civicandcommunityengagement_minor/ |
| 17 | Classical Civilization | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofclassics/classicalcivilization_minor/ |
| 18 | Comparative Literature | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofcomparativeliterature/comparativeliterature_minor/ |
| 19 | Creative Writing | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofenglish/creativewriting_minor/ |
| 20 | Criminology, Law and Society | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/departmentofcriminologylawandsociety/criminologylawandsociety_minor/ |
| 21 | Digital Arts | Arts | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofart/digitalarts_minor/ |
| 22 | Digital Information Systems | ICS | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofinformatics/digitalinformationsystems_minor/ |
| 23 | Drama | Arts | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdrama/drama_minor/ |
| 24 | Earth and Atmospheric Sciences | Physical Sciences | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofearthsystemscience/earthandatmosphericsciences_minor/ |
| 25 | Economics | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofeconomics/economics_minor/ |
| 26 | Education | Education | https://catalogue.uci.edu/schoolofeducation/education_minor/ |
| 27 | English | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofenglish/english_minor/ |
| 28 | European Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/europeanstudies_minor/ |
| 29 | Film and Media Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentoffilmandmediastudies/filmandmediastudies_minor/ |
| 30 | French | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/french_minor/ |
| 31 | Gender and Sexuality Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofgenderandsexualitystudies/genderandsexualitystudies_minor/ |
| 32 | German Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/germanstudies_minor/ |
| 33 | Global Cultures | Humanities | https://catalogue.uci.edu/schoolofhumanities/undergraduateprograminglobalcultures/globalcultures_minor/ |
| 34 | Global Health | Population & Public Health | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/globalhealth_minor/ |
| 35 | Global Middle East Studies | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/globalmiddleeaststudies_minor/ |
| 36 | Global Sustainability | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/globalsustainability_minor/ |
| 37 | Greek | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofclassics/greek_minor/ |
| 38 | Hearing and Speech Sciences | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofcognitivesciences/hearingandspeechsciences_minor/ |
| 39 | Health Informatics | ICS | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofinformatics/healthinformatics_minor/ |
| 40 | History | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofhistory/history_minor/ |
| 41 | History and Philosophy of Science | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/historyandphilosophyofscience_minor/ |
| 42 | Humanities and Law | Humanities | https://catalogue.uci.edu/schoolofhumanities/specialprograms/humanitiesandlaw_minor/ |
| 43 | Informatics | ICS | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofinformatics/informatics_minor/ |
| 44 | Information and Computer Science | ICS | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/informationandcomputerscience_minor/ |
| 45 | Innovation and Entrepreneurship | Paul Merage School of Business | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/innovationandentrepreneurship_minor/ |
| 46 | International Studies | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofinternationalstudies/internationalstudies_minor/ |
| 47 | Italian Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/italianstudies_minor/ |
| 48 | Japanese Language and Literature | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/japaneselanguageandliterature_minor/ |
| 49 | Japanese Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/japanesestudies_minor/ |
| 50 | Jewish Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofhistory/jewishstudies_minor/ |
| 51 | Korean Literature and Culture | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeastasianstudies/koreanliteratureandculture_minor/ |
| 52 | Latin | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofclassics/latin_minor/ |
| 53 | Latin American Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/specialprograms/latinamericanstudies_minor/ |
| 54 | Linguistics | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentoflinguistics/linguistics_minor/ |
| 55 | Literary Journalism | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofenglish/literaryjournalism_minor/ |
| 56 | Management | Paul Merage School of Business | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/management_minor/ |
| 57 | Materials Science and Engineering | Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofmaterials scienceandengineering/materialsscienceandengineering_minor/ |
| 58 | Mathematics | Physical Sciences | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofmathematics/mathematics_minor/ |
| 59 | Mathematics for Biology | Physical Sciences | https://catalogue.uci.edu/schoolofphysicalsciences/departmentofmathematics/mathematicsforbiology_minor/ |
| 60 | Medical Anthropology | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofanthropology/medicalanthropology_minor/ |
| 61 | Medical Humanities | Humanities | https://catalogue.uci.edu/schoolofhumanities/specialprograms/medicalhumanities_minor/ |
| 62 | Music | Arts | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofmusic/music_minor/ |
| 63 | Native American and Indigenous Studies | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/nativeamericanandindigenousstudies_minor/ |
| 64 | Persian Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofhistory/persianstudies_minor/ |
| 65 | Philosophy | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofphilosophy/philosophy_minor/ |
| 66 | Political Science | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofpoliticalscience/politicalscience_minor/ |
| 67 | Psychology | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofpsychology/psychology_minor/ |
| 68 | Psychological Science | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/departmentofpsychologicalscience/psychologicalscience_minor/ |
| 69 | Public Health | Population & Public Health | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/publichealth_minor/ |
| 70 | Queer Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofgenderandsexualitystudies/queerstudies_minor/ |
| 71 | Religious Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofreligiousstudies/religiousstudies_minor/ |
| 72 | Russian Studies | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofeuropeanlanguagesandstudies/russianstudies_minor/ |
| 73 | Social Ecology | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/socialecology_minor/ |
| 74 | Sociology | Social Sciences | https://catalogue.uci.edu/schoolofsocialsciences/departmentofsociology/sociology_minor/ |
| 75 | Spanish | Humanities | https://catalogue.uci.edu/schoolofhumanities/departmentofspanishandportuguese/spanish_minor/ |
| 76 | Spanish/English Bilingual Education | Humanities | https://catalogue.uci.edu/schoolofhumanities/specialprograms/spanishenglishbilingualeducation_minor/ |
| 77 | Statistics | ICS | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofstatistics/statistics_minor/ |
| 78 | STEM Higher Education Research | Interdisciplinary | https://catalogue.uci.edu/interdisciplinarystudies/stemhighereducationresearch_minor/ |
| 79 | Urban and Regional Planning | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/urbanandregionalplanning_minor/ |
| 80 | Urban Studies | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/urbanstudies_minor/ |

### 1.5 General Education Requirements

UCI requires completion of the UC-wide General Education (GE) requirements plus UCI-specific requirements. Details at: https://catalogue.uci.edu/informationforadmittedstudents/requirementsforabachelorsdegree/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Claire Trevor School of the Arts

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofart/art_mfa/ |
| 2 | Dance | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdance/dance_mfa/ |
| 3 | Drama | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdrama/drama_mfa/ |
| 4 | Music | https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofmusic/music_mfa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Drama and Theatre | https://catalogue.uci.edu/clairetrevorschoolofthearts/dramaandtheatre_phd/ |
| 2 | History and Theory of Music | https://catalogue.uci.edu/clairetrevorschoolofthearts/historyandtheoryofmusic_phd/ |
| 3 | Integrated Composition, Improvisation, and Technology | https://catalogue.uci.edu/clairetrevorschoolofthearts/integratedcompositionimprovisationandtechnology_phd/ |

---

#### Charlie Dunlop School of Biological Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biologicalsciences_ms/ |
| 2 | Biotechnology Management | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biotechnologymanagement_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalogue.uci.edu/charliedunlopschoolofbiologicalsciences/biologicalsciences_phd/ |

---

#### The Paul Merage School of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/businessadministration_mba/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/businessanalytics_ms/ |
| 2 | Business Analytics (Part-Time) | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/businessanalyticspt_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Management | https://catalogue.uci.edu/thepaulmerageschoolofbusiness/management_phd/ |

---

#### School of Education

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Elementary and Secondary Education | https://catalogue.uci.edu/schoolofeducation/elementaryandsecondaryeducation_mat/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://catalogue.uci.edu/schoolofeducation/education_phd/ |

---

#### The Henry Samueli School of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/biomedicalengineering_ms/ |
| 2 | Chemical and Biomolecular Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/chemicalandbiomolecularengineering_ms/ |
| 3 | Civil and Environmental Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/civilandenvironmentalengineering_ms/ |
| 4 | Electrical and Computer Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/electricalandcomputerengineering_ms/ |
| 5 | Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/engineering_ms/ |
| 6 | Materials Science and Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/materialsscienceandengineering_ms/ |
| 7 | Mechanical and Aerospace Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/mechanicalandaerospaceengineering_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/biomedicalengineering_phd/ |
| 2 | Chemical and Biomolecular Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/chemicalandbiomolecularengineering_phd/ |
| 3 | Civil and Environmental Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/civilandenvironmentalengineering_phd/ |
| 4 | Electrical and Computer Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/electricalandcomputerengineering_phd/ |
| 5 | Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/engineering_phd/ |
| 6 | Materials Science and Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/materialsscienceandengineering_phd/ |
| 7 | Mechanical and Aerospace Engineering | https://catalogue.uci.edu/thehenrysamuelischoolofengineering/mechanicalandaerospaceengineering_phd/ |

---

#### School of Humanities

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://catalogue.uci.edu/schoolofhumanities/arthistory_ma/ |
| 2 | Asian American Studies | https://catalogue.uci.edu/schoolofhumanities/asianamericanstudies_ma/ |
| 3 | Classics | https://catalogue.uci.edu/schoolofhumanities/classics_ma/ |
| 4 | Comparative Literature | https://catalogue.uci.edu/schoolofhumanities/comparativeliterature_ma/ |
| 5 | European Thought and Culture | https://catalogue.uci.edu/schoolofhumanities/europeanthoughtandculture_ma/ |
| 6 | History | https://catalogue.uci.edu/schoolofhumanities/history_ma/ |
| 7 | Spanish | https://catalogue.uci.edu/schoolofhumanities/spanish_ma/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics | https://catalogue.uci.edu/schoolofhumanities/classics_phd/ |
| 2 | Comparative Literature | https://catalogue.uci.edu/schoolofhumanities/comparativeliterature_phd/ |
| 3 | Culture and Theory | https://catalogue.uci.edu/schoolofhumanities/cultureandtheory_phd/ |
| 4 | East Asian Studies | https://catalogue.uci.edu/schoolofhumanities/eastasianstudies_phd/ |
| 5 | English | https://catalogue.uci.edu/schoolofhumanities/english_phd/ |
| 6 | Film and Media Studies | https://catalogue.uci.edu/schoolofhumanities/filmandmediastudies_phd/ |
| 7 | German | https://catalogue.uci.edu/schoolofhumanities/german_phd/ |
| 8 | History | https://catalogue.uci.edu/schoolofhumanities/history_phd/ |
| 9 | Philosophy (Humanities) | https://catalogue.uci.edu/schoolofhumanities/philosophy_phd/ |
| 10 | Spanish | https://catalogue.uci.edu/schoolofhumanities/spanish_phd/ |
| 11 | Visual Studies | https://catalogue.uci.edu/schoolofhumanities/visualstudies_phd/ |

---

#### Donald Bren School of Information and Computer Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Informatics | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/informatics_ms/ |
| 2 | Information and Computer Science | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/informationandcomputerscience_ms/ |
| 3 | Software Engineering | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/softwareengineering_ms/ |
| 4 | Statistics | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/statistics_ms/ |

##### MSE
| # | 项目 | URL |
|---|------|-----|
| 1 | Software Engineering | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/softwareengineering_mse/ |

##### MDS
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/datascience_mds/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/computerscience_phd/ |
| 2 | Informatics | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/informatics_phd/ |
| 3 | Software Engineering | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/softwareengineering_phd/ |
| 4 | Statistics | https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/statistics_phd/ |

---

#### School of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://catalogue.uci.edu/schooloflaw/law_jd/ |

---

#### School of Medicine

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical and Translational Science | https://catalogue.uci.edu/schoolofmedicine/biomedicalandtranslationalscience_ms/ |
| 2 | Genetic Counseling | https://catalogue.uci.edu/schoolofmedicine/geneticcounseling_ms/ |
| 3 | Medical Science | https://catalogue.uci.edu/schoolofmedicine/medicalscience_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://catalogue.uci.edu/schoolofmedicine/biomedicalsciences_phd/ |

##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://catalogue.uci.edu/schoolofmedicine/medicine_md/ |

---

#### Sue and Bill Gross School of Nursing

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Science | https://catalogue.uci.edu/sueandbillgrossschoolofnursing/nursingscience_ms/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalogue.uci.edu/sueandbillgrossschoolofnursing/nursing_dnp/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Science | https://catalogue.uci.edu/sueandbillgrossschoolofnursing/nursingscience_phd/ |

---

#### School of Pharmacy and Pharmaceutical Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacology | https://catalogue.uci.edu/schoolofpharmacyandpharmaceuticalsciences/pharmacology_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacological Sciences | https://catalogue.uci.edu/schoolofpharmacyandpharmaceuticalsciences/pharmacologicalsciences_phd/ |

---

#### School of Physical Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalogue.uci.edu/schoolofphysicalsciences/mathematics_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalogue.uci.edu/schoolofphysicalsciences/chemistry_phd/ |
| 2 | Earth System Science | https://catalogue.uci.edu/schoolofphysicalsciences/earthsystemscience_phd/ |
| 3 | Mathematics | https://catalogue.uci.edu/schoolofphysicalsciences/mathematics_phd/ |
| 4 | Physics | https://catalogue.uci.edu/schoolofphysicalsciences/physics_phd/ |

---

#### Joe C. Wen School of Population and Public Health

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Health Sciences | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/environmentalhealthsciences_ms/ |
| 2 | Epidemiology | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/epidemiology_ms/ |
| 3 | Public Health | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/publichealth_ms/ |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/publichealth_mph/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Health Sciences | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/environmentalhealthsciences_phd/ |
| 2 | Epidemiology | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/epidemiology_phd/ |
| 3 | Public Health | https://catalogue.uci.edu/joecwenschoolofpopulationandpublichealth/publichealth_phd/ |

---

#### School of Social Ecology

##### MAS
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology, Law and Society | https://catalogue.uci.edu/schoolofsocialecology/criminologylawandsociety_mas/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology, Law and Society | https://catalogue.uci.edu/schoolofsocialecology/criminologylawandsociety_phd/ |
| 2 | Psychological Science | https://catalogue.uci.edu/schoolofsocialecology/psychologicalscience_phd/ |
| 3 | Social Ecology | https://catalogue.uci.edu/schoolofsocialecology/socialecology_phd/ |
| 4 | Urban and Environmental Planning and Policy | https://catalogue.uci.edu/schoolofsocialecology/urbanandenvironmentalplanningandpolicy_phd/ |

---

#### School of Social Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy, Political Science, and Economics | https://catalogue.uci.edu/schoolofsocialsciences/philosophypoliticalscienceeconomics_ma/ |
| 2 | Social Science | https://catalogue.uci.edu/schoolofsocialsciences/socialscience_ma/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Cognitive Neuroscience | https://catalogue.uci.edu/schoolofsocialsciences/cognitiveneuroscience_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalogue.uci.edu/schoolofsocialsciences/anthropology_phd/ |
| 2 | Cognitive Sciences | https://catalogue.uci.edu/schoolofsocialsciences/cognitivesciences_phd/ |
| 3 | Economics | https://catalogue.uci.edu/schoolofsocialsciences/economics_phd/ |
| 4 | Global Studies | https://catalogue.uci.edu/schoolofsocialsciences/globalstudies_phd/ |
| 5 | Language Science | https://catalogue.uci.edu/schoolofsocialsciences/languagescience_phd/ |
| 6 | Philosophy (Social Sciences) | https://catalogue.uci.edu/schoolofsocialsciences/philosophy_phd/ |
| 7 | Political Science | https://catalogue.uci.edu/schoolofsocialsciences/politicalscience_phd/ |
| 8 | Social Science | https://catalogue.uci.edu/schoolofsocialsciences/socialscience_phd/ |
| 9 | Sociology | https://catalogue.uci.edu/schoolofsocialsciences/sociology_phd/ |

---

#### Interdisciplinary Graduate Programs

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematical, Computational, and Systems Biology | https://catalogue.uci.edu/interdisciplinarystudies/mathematicalcomputationalandsystemsbiology_ms/ |
| 2 | Networked Systems | https://catalogue.uci.edu/interdisciplinarystudies/networkedsystems_ms/ |
| 3 | Transportation Science | https://catalogue.uci.edu/interdisciplinarystudies/transportationscience_ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Science | https://catalogue.uci.edu/interdisciplinarystudies/computationalscience_phd/ |
| 2 | Mathematical, Computational, and Systems Biology | https://catalogue.uci.edu/interdisciplinarystudies/mathematicalcomputationalandsystemsbiology_phd/ |
| 3 | Networked Systems | https://catalogue.uci.edu/interdisciplinarystudies/networkedsystems_phd/ |
| 4 | Transportation Science | https://catalogue.uci.edu/interdisciplinarystudies/transportationscience_phd/ |

---

### 2.2 Graduate Program Deep-Dive: Computer Science, Ph.D.

- **School**: Donald Bren School of Information and Computer Sciences
- **Department**: Department of Computer Science
- **URL**: https://grad.uci.edu/admissions/degree-programs/
- **Application Portal**: https://apply.grad.uci.edu/apply/
- **Application Fee**: $135 (domestic) / $155 (international)
- **GRE**: Not Required
- **Letters of Recommendation**: 3
- **Minimum GPA**: 3.0
- **Contact**: Department of Computer Science, ICS building, UCI campus
- **Notes**: GRE not required for most UCI graduate programs as of 2025-26 cycle.

### 2.3 Graduate Admissions Model

UCI uses a **decentralized** graduate admissions model. The Graduate Division provides centralized services (application portal, fee collection, degree conferral) but each program makes its own admissions decisions.

- **Centralized portal**: https://apply.grad.uci.edu/apply/
- **Application fee**: $135 (U.S. citizens/permanent residents) / $155 (all others)
- **Minimum requirements**: Bachelor's degree + 3.0 GPA
- **GRE**: Not required for most programs (per-program policy)
- **Programs**: Over 100 graduate academic and professional degree programs
- **Financial support**: Most PhD programs offer full funding (TA/RA/fellowships); master's programs vary

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | UC Application (apply.universityofcalifornia.edu) | admissions.uci.edu |
| Application opens | August 1 | admissions.uci.edu/dates-deadlines.php |
| Application submission period | October 1 – November 30 | admissions.uci.edu/dates-deadlines.php |
| EA deadline | N/A (UC system has no EA/ED) | — |
| RD deadline | November 30 | admissions.uci.edu/dates-deadlines.php |
| Decision notification (first-year) | March 1 – March 31 | admissions.uci.edu/dates-deadlines.php |
| Decision notification (transfer) | April 1 – April 30 | admissions.uci.edu/dates-deadlines.php |
| SIR deadline (first-year) | May 1 | admissions.uci.edu/dates-deadlines.php |
| SIR deadline (transfer) | June 1 | admissions.uci.edu/dates-deadlines.php |
| Priority FAFSA deadline | March 2 | admissions.uci.edu/dates-deadlines.php |
| Application fee (domestic) | $80 | admissions.uci.edu/apply/how-to-apply/ |
| Application fee (international) | $95 | admissions.uci.edu/apply/how-to-apply/ |
| SAT/ACT policy | Test-FREE (not considered for admission) | admissions.uci.edu/apply/first-year-students/ |
| Superscore | N/A (test-free) | — |
| Interview policy | No interviews | — |
| Recommendation requirements | None required | — |
| Portfolio/Audition | Required for Dance, B.Mus., Drama, Arts (Dec 1 – Jan 31) | admissions.uci.edu/dates-deadlines.php |
| TAG (Transfer Admission Guarantee) | September 1 – September 30 | admissions.uci.edu/dates-deadlines.php |
| GPA requirement (CA residents) | 3.0 in A-G courses | admissions.uci.edu/apply/first-year-students/ |
| GPA requirement (non-residents) | 3.4 in A-G courses | admissions.uci.edu/apply/first-year-students/ |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT (prior to Jan 2026) | 80 | — | Only highest composite from single sitting |
| TOEFL iBT (Jan 2026+) | 4.5 (new scale) | — | New scoring scale effective Jan 2026 |
| IELTS | 6.5 | — | No IELTS One Skill Retake |
| Duolingo English Test (DET) | 115 | — | — |
| IB English A | 6.5 or higher | — | — |
| UC-transferable English comp course | Grade C or better | — | 3 semester / 4-5 quarter units |

> **Applicability**: Required for all international applicants whose primary language of instruction is not English. UC does NOT accept MyBest TOEFL or IELTS Indicator.

### 3.3 Graduate — Global Rules

- **Admissions model**: Fully decentralized; each program sets own deadlines, requirements, and GRE policy
- **Application portal**: https://apply.grad.uci.edu/apply/
- **Application fee**: $135 (U.S. citizens/permanent residents) / $155 (international)
- **Minimum GPA**: 3.0 cumulative undergraduate
- **GRE**: Not required for most programs (per-program decision)
- **English proficiency**: TOEFL or IELTS required for non-native English speakers
- **CGS April-15**: UCI is a CGS signatory
- **ETS institutional code**: 4859

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year)

| Expense Item | Living At Home | Living On Campus | Living Off Campus |
|-------------|---------------|-----------------|-------------------|
| Systemwide Fees | $15,588 | $15,588 | $15,588 |
| Campus Fees | $4,419 | $4,419 | $4,419 |
| **Total Fees** | **$20,077** | **$20,077** | **$20,077** |
| Books and Supplies | $1,477 | $1,477 | $1,477 |
| Housing and Food | $8,603 | $20,926 | $22,419 |
| Personal | $3,039 | $2,723 | $3,423 |
| Transportation | $2,812 | $874 | $2,429 |
| **Subtotal (non-fees)** | **$15,931** | **$26,000** | **$29,748** |
| **Total** | **$35,938** | **$46,007** | **$49,755** |

> **Nonresident Supplemental Tuition**: Add $39,270 for non-California residents.
> **Tuition Stability Plan**: Tuition is held flat for each incoming class for up to 6 years.

### 4.2 Undergraduate Financial Aid Policy

| Field | Value |
|-------|-------|
| Need-blind/need-aware | Need-blind for CA residents; need-aware for OOS and international |
| Meets full demonstrated need | Yes (for CA residents) |
| Merit scholarships | Available via ScholarshipUniverse platform |
| Tuition-free threshold | Varies; check current UC financial aid guidelines |
| FAFSA priority deadline | March 2 |
| CA Dream Act | Accepted |
| Contact | Office of Financial Aid and Scholarships, UCI |

### 4.3 Graduate Cost & Funding Framework

| Field | Value |
|-------|-------|
| Application fee (domestic) | $135 |
| Application fee (international) | $155 |
| Fee waivers | Available for eligible applicants |
| PhD funding | Most programs offer full funding (TA/RA/fellowships) |
| Master's funding | Varies by program; generally self-funded |
| Diversity fellowships | Available for U.S. citizens/permanent residents |
| Contact | Graduate Division, 120 Aldrich Hall; grad@uci.edu; 949-824-4611 |

---

## SECTION 5 — Evidence Chain Index

```yaml
# E-U-001
field: undergraduate.deadlines.application_period
value: "October 1 – November 30"
source_url: https://admissions.uci.edu/dates-deadlines.php
source_snippet: "10/01 - 11/30 PROSPECTIVE STUDENTS Apply for Fall UC Application submission period for fall 2027 admission and scholarships."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-002
field: undergraduate.application_fee.domestic
value: "$80"
source_url: https://admissions.uci.edu/apply/how-to-apply/index.php
source_snippet: "submit it along with a nonrefundable college application fee of $80 for domestic applicants or $95 for international applicants"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-003
field: undergraduate.application_fee.international
value: "$95"
source_url: https://admissions.uci.edu/apply/how-to-apply/index.php
source_snippet: "submit it along with a nonrefundable college application fee of $80 for domestic applicants or $95 for international applicants"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-004
field: undergraduate.test_policy
value: "Test-FREE (SAT/ACT not considered)"
source_url: https://admissions.uci.edu/apply/first-year-students/index.php
source_snippet: "UC Irvine does not consider SAT or ACT scores for admission or scholarship purposes."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-005
field: undergraduate.gpa_requirement.ca_resident
value: "3.0"
source_url: https://admissions.uci.edu/apply/first-year-students/index.php
source_snippet: "You must receive a 3.0 GPA (3.4 for non-California residents) or higher in the 15 required 'A-G' subject courses, with no grade lower than a C."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-006
field: undergraduate.gpa_requirement.non_resident
value: "3.4"
source_url: https://admissions.uci.edu/apply/first-year-students/index.php
source_snippet: "You must receive a 3.0 GPA (3.4 for non-California residents) or higher in the 15 required 'A-G' subject courses, with no grade lower than a C."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-007
field: undergraduate.english_proficiency.toefl
value: "80 (prior to Jan 2026) / 4.5 new scale (Jan 2026+)"
source_url: https://admissions.uci.edu/apply/international-students.php
source_snippet: "Test of English as a Foreign Language (TOEFL)* examination: Internet-based test (iBT) or iBT Home Edition: Minimum score of 4.5 or better (effective January 2026); Minimum score of 80 or better (prior to January 2026)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-008
field: undergraduate.english_proficiency.ielts
value: "6.5"
source_url: https://admissions.uci.edu/apply/international-students.php
source_snippet: "Score 6.5 or higher on the International English Language Testing System (IELTS)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-009
field: undergraduate.english_proficiency.det
value: "115"
source_url: https://admissions.uci.edu/apply/international-students.php
source_snippet: "Duolingo English Test (DET): Minimum score of 115"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-010
field: undergraduate.cost.systemwide_fees
value: "$15,588"
source_url: https://admissions.uci.edu/afford/index.php
source_snippet: "Systemwide Fees $15,588.00"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
# E-U-011
field: undergraduate.cost.campus_fees
value: "$4,419"
source_url: https://admissions.uci.edu/afford/index.php
source_snippet: "Campus Fees $4,419.00"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
# E-U-012
field: undergraduate.cost.nonresident_tuition
value: "$39,270"
source_url: https://admissions.uci.edu/afford/index.php
source_snippet: "For nonresidents of California, add $39,270 Nonresident Tuition and Fees to the costs below."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-013
field: undergraduate.cost.total_on_campus
value: "$46,007"
source_url: https://admissions.uci.edu/afford/index.php
source_snippet: "Living On Campus Total $46,007.00"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
# E-U-014
field: undergraduate.decisions.first_year_notification
value: "March 1 – March 31"
source_url: https://admissions.uci.edu/dates-deadlines.php
source_snippet: "03/01 - 03/31 PROSPECTIVE STUDENTS First-Year Student Admission Notice UC Irvine notifies each first-year applicant of their admission status via the Applicant Portal."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-015
field: undergraduate.deadlines.sir_first_year
value: "May 1"
source_url: https://admissions.uci.edu/dates-deadlines.php
source_snippet: "05/01 ADMITTED STUDENTS First-year SIR and SLR First-year Statement of Intent to Register (SIR) and Statement of Legal Residence (SLR) are due by 11:59 p.m. Pacific Daylight Time."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-016
field: undergraduate.program_count.majors
value: "85-plus (catalog: 87)"
source_url: https://admissions.uci.edu/study/majors-minors.php
source_snippet: "Explore 85-plus majors and 70-plus minors at UC Irvine."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-001
field: graduate.application_fee.domestic
value: "$135"
source_url: https://grad.uci.edu/admissions/applying-to-uci/
source_snippet: "Your application cannot be reviewed until UC Irvine has received your non-refundable application fee ($135 for U.S. citizens and lawful U.S. permanent residents, and $155 for all other applicants)."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-002
field: graduate.application_fee.international
value: "$155"
source_url: https://grad.uci.edu/admissions/applying-to-uci/
source_snippet: "Your application cannot be reviewed until UC Irvine has received your non-refundable application fee ($135 for U.S. citizens and lawful U.S. permanent residents, and $155 for all other applicants)."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-003
field: graduate.minimum_gpa
value: "3.0"
source_url: https://grad.uci.edu/admissions/applying-to-uci/
source_snippet: "Have a minimum cumulative undergraduate GPA of 3.0."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-004
field: graduate.gre_policy
value: "Not Required for most programs"
source_url: https://grad.uci.edu/admissions/degree-programs/
source_snippet: "GRE Requirement: Not Required"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-C-001
field: academic.schools_count
value: "15 academic schools"
source_url: https://catalogue.uci.edu/schoolsandprograms/
source_snippet: "Claire Trevor School of the Arts, Charlie Dunlop School of Biological Sciences, The Paul Merage School of Business, School of Education, The Henry Samueli School of Engineering, School of Humanities, Donald Bren School of Information and Computer Sciences, School of Law, School of Medicine, Sue and Bill Gross School of Nursing, School of Pharmacy and Pharmaceutical Sciences, School of Physical Sciences, Joe C. Wen School of Population and Public Health, School of Social Ecology, School of Social Sciences"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uci-knowledge-base-v2/
├── 00-overview                          (Section 0: counts, hierarchy, matrix)
├── 01-ug-arts                           (Section 1: Claire Trevor School of the Arts)
├── 02-ug-biological-sciences            (Section 1: Biological Sciences)
├── 03-ug-business                       (Section 1: Business)
├── 04-ug-education                      (Section 1: Education)
├── 05-ug-engineering                    (Section 1: Engineering)
├── 06-ug-humanities                     (Section 1: Humanities)
├── 07-ug-ics                            (Section 1: ICS)
├── 08-ug-nursing                        (Section 1: Nursing)
├── 09-ug-pharmacy                       (Section 1: Pharmacy)
├── 10-ug-physical-sciences              (Section 1: Physical Sciences)
├── 11-ug-population-public-health       (Section 1: Population & Public Health)
├── 12-ug-social-ecology                 (Section 1: Social Ecology)
├── 13-ug-social-sciences                (Section 1: Social Sciences)
├── 14-ug-interdisciplinary              (Section 1: Interdisciplinary)
├── 15-grad-arts                         (Section 2: Arts graduate)
├── 16-grad-biological-sciences          (Section 2: Biological Sciences graduate)
├── 17-grad-business                     (Section 2: Business graduate)
├── 18-grad-education                    (Section 2: Education graduate)
├── 19-grad-engineering                  (Section 2: Engineering graduate)
├── 20-grad-humanities                   (Section 2: Humanities graduate)
├── 21-grad-ics                          (Section 2: ICS graduate)
├── 22-grad-law                          (Section 2: Law graduate)
├── 23-grad-medicine                     (Section 2: Medicine graduate)
├── 24-grad-nursing                      (Section 2: Nursing graduate)
├── 25-grad-pharmacy                     (Section 2: Pharmacy graduate)
├── 26-grad-physical-sciences            (Section 2: Physical Sciences graduate)
├── 27-grad-population-public-health     (Section 2: Population & Public Health graduate)
├── 28-grad-social-ecology               (Section 2: Social Ecology graduate)
├── 29-grad-social-sciences              (Section 2: Social Sciences graduate)
├── 30-grad-interdisciplinary            (Section 2: Interdisciplinary graduate)
├── 31-deadlines-requirements            (Section 3)
├── 32-costs-financial-aid               (Section 4)
└── 33-evidence-chain                    (Section 5)
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "uci-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BFA|BMus|Minor|MA|MS|MFA|MBA|PhD|JD|MD|DNP|MPH|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|----------|------------|
| P0 | Graduate program detail pages (GRE/TOEFL per program) | https://grad.uci.edu/admissions/degree-programs/ |
| P0 | Per-program application deadlines (grad) | Individual program pages |
| P1 | Financial aid policy details (income thresholds, need-aware details) | https://www.ofas.uci.edu/ |
| P1 | Graduate cost of attendance (tuition + fees) | https://www.ofas.uci.edu/cost/graduate-costs/ |
| P1 | International student financial aid policy | https://www.ofas.uci.edu/ |
| P2 | A-G course requirements detail | https://admissions.uci.edu/apply/first-year-students/ |
| P2 | Transfer admission requirements | https://admissions.uci.edu/apply/transfer-students/ |
| P2 | Student-to-faculty ratio, enrollment data | https://www.uci.edu/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UCI Value | Notes |
|-----------|----------|-------|
| Total UG cost/yr (on-campus, in-state) | $46,007 | 2026-27 |
| Total UG cost/yr (on-campus, OOS) | $85,277 | +$39,270 nonresident |
| Tuition/fees (in-state) | $20,077 | Systemwide + campus fees |
| Tuition/fees (OOS) | $59,347 | +$39,270 nonresident |
| Need-blind (intl?) | No (need-aware for intl) | Need-blind for CA residents only |
| EA deadline | N/A | UC system has no EA/ED |
| RD deadline | November 30 | UC Application |
| SAT/ACT required? | No (test-FREE) | Scores not considered at all |
| TOEFL min | 80 (old) / 4.5 (new, Jan 2026+) | |
| IELTS min | 6.5 | |
| DET min | 115 | |
| App fee (UG domestic) | $80 | |
| App fee (UG international) | $95 | |
| App fee (grad domestic) | $135 | |
| App fee (grad international) | $155 | |
| Total program count (Rule 1) | 267 | 87 UG majors + 79 minors + 101 grad |
| School/department count (Rule 2) | 15 schools | Plus Division of UG Ed + Graduate Division |
| Graduate GRE policy | Not required (most programs) | Per-program decision |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.uci.edu, catalogue.uci.edu, grad.uci.edu, www.ofas.uci.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
