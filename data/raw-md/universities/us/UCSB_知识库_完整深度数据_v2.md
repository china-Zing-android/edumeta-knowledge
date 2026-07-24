# University of California, Santa Barbara (UCSB) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BMus) | 178 |
| 本科辅修 (Minor) | 54 |
| 研究生学位项目 (MA/MS/MFA/MEd/PhD/etc.) | 152 |
| **学位项目总计 (UG + Grad)** | **384** |
| 学院 / 独立系所总数 | 6 |

### 0.2 学院 / 系层级结构

```
UC Santa Barbara
├── College of Creative Studies [29 programs]
│   └── Creative StdsCR [29 programs]
├── College of Engineering [21 programs]
│   ├── Bioengineering [2 programs]
│   ├── Chemical Engr [3 programs]
│   ├── Computer Sci [4 programs]
│   ├── Elect Comp Engr [4 programs]
│   ├── Materials [2 programs]
│   ├── Mechanical Engr [3 programs]
│   ├── Tech Management [2 programs]
│   └── Unknown [1 programs]
├── College of Letters and Science [313 programs]
│   ├── Anthropology [7 programs]
│   ├── Art [2 programs]
│   ├── Asian Amer Stds [2 programs]
│   ├── Black Studies [2 programs]
│   ├── Chem & Biochem [9 programs]
│   ├── Chicano Studies [4 programs]
│   ├── Classics [13 programs]
│   ├── Communication [4 programs]
│   ├── Comparative Lit [6 programs]
│   ├── Creative StdsCR [3 programs]
│   ├── Dynamical Neuroscience [2 programs]
│   ├── E As Lng & Clt [8 programs]
│   ├── Earth Science [8 programs]
│   ├── Ecol Ev Mar Bio [11 programs]
│   ├── Economics [6 programs]
│   ├── English [5 programs]
│   ├── Environ Studies [3 programs]
│   ├── Feminist Stds [5 programs]
│   ├── Film & Media St [4 programs]
│   ├── French and Italian [5 programs]
│   ├── Geography [6 programs]
│   ├── German & Slavic [4 programs]
│   ├── Global Studies [4 programs]
│   ├── Hist of Art&Arc [9 programs]
│   ├── History [11 programs]
│   ├── Int Prg Qnt Bio [2 programs]
│   ├── Interdisciplinary [3 programs]
│   ├── Lat Amer & Iber [3 programs]
│   ├── Letters & Sci [1 programs]
│   ├── Linguistics [18 programs]
│   ├── Marine Science [2 programs]
│   ├── Mathematics [13 programs]
│   ├── Media Arts & Te [3 programs]
│   ├── Medieval Stds [2 programs]
│   ├── Mol Cel Dev Bio [10 programs]
│   ├── Music [39 programs]
│   ├── Philosophy [4 programs]
│   ├── Physics [8 programs]
│   ├── Political Sci [8 programs]
│   ├── Psy & Brain Sci [10 programs]
│   ├── Religious Stds [8 programs]
│   ├── Sociology [4 programs]
│   ├── Spanish & Port [7 programs]
│   ├── Stats Appl Prob [11 programs]
│   ├── Theater & Dance [9 programs]
│   ├── Unknown [4 programs]
│   └── Writing Program [1 programs]
├── Graduate School of Education [16 programs]
│   ├── Couns/Clin/Schl [6 programs]
│   └── Education [10 programs]
├── L&S [1 programs]
│   └── Chem & Biochem [1 programs]
├── School of Environmental Science & Management [4 programs]
│   └── Env. Sci. & Mgm [4 programs]
```

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | 108 |
| BS | BS | Bachelor of Science | 本科 | 52 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BMus | BMus | Bachelor of Music | 本科 | 16 |
| MA | MA | Master of Arts | 研究生 | 47 |
| MS | MS | Master of Science | 研究生 | 18 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 7 |
| MMus | MMus | Master of Music | 研究生 | 8 |
| MEDS | MEDS | Master of Environmental Data Science | 研究生 | 1 |
| MESM | MESM | Master of Environmental Science and Management | 研究生 | 1 |
| MTM | MTM | Master of Technology Management | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 67 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 |
| Minor | Minor | Minor | 本科辅修 | 54 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BMus | MA | MS | MFA | MEd | MMus | MEDS | MESM | MTM | PhD | DMA | Minor | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|
| College of Creative Studies | 20 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 29 |
| College of Engineering | 0 | 6 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 0 | 21 |
| College of Letters and Science | 88 | 37 | 2 | 16 | 45 | 11 | 1 | 0 | 8 | 0 | 0 | 0 | 53 | 1 | 51 | 313 |
| Graduate School of Education | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 4 | 0 | 3 | 16 |
| L&S | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| School of Environmental Science & Management | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 4 |
| **合计** | 108 | 52 | 2 | 16 | 47 | 18 | 1 | 7 | 8 | 1 | 1 | 1 | 67 | 1 | 54 | **384** |

> **Reconciliation check**: Rule 1 total = 384, Matrix sum = 384, Match: YES

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

UCSB has three undergraduate colleges: College of Letters and Science (largest, most majors), College of Engineering (engineering and CS programs), and College of Creative Studies (intensive arts and sciences programs). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Creative Studies
##### Creative StdsCR
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art - Painting Emphasis | <https://catalog.ucsb.edu/programs/BAARTCSPAINTING> |
| 2 | Art - Sculpture Emphasis | <https://catalog.ucsb.edu/programs/BAARTCSSCULPT> |
| 3 | Art | <https://catalog.ucsb.edu/programs/BAARTCS> |
| 4 | Biology | <https://catalog.ucsb.edu/programs/BABIOCS> |
| 5 | Chemistry and Biochemistry | <https://catalog.ucsb.edu/programs/BACHBCS> |
| 6 | Creative Studies | <https://catalog.ucsb.edu/programs/BACRTST> |
| 7 | Creative Studies - Art Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTART> |
| 8 | Creative Studies - Biology Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTBIOL> |
| 9 | Creative Studies - Book Arts Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTBOOKARTS> |
| 10 | Creative Studies - Literature Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTLIT> |
| 11 | Creative Studies - Mathematics Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTMATH> |
| 12 | Creative Studies - Music Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTMUSIC> |
| 13 | Creative Studies - Painting Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTPAINTING> |
| 14 | Creative Studies - Physics Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTPHYS> |
| 15 | Creative Studies - Sculpture Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTSCULPT> |
| 16 | Marine Science | <https://catalog.ucsb.edu/programs/BAMRNCS> |
| 17 | Mathematics | <https://catalog.ucsb.edu/programs/BAMATCS> |
| 18 | Music Composition | <https://catalog.ucsb.edu/programs/BAMUSCS> |
| 19 | Physics | <https://catalog.ucsb.edu/programs/BAPHYCS> |
| 20 | Writing and Literature | <https://catalog.ucsb.edu/programs/BAWTLCS> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry and Biochemistry | <https://catalog.ucsb.edu/programs/BSCHBCS> |
| 2 | Computing | <https://catalog.ucsb.edu/programs/BSCPTCS> |
| 3 | Creative Studies - Chemistry Emphasis | <https://catalog.ucsb.edu/programs/BSCRTSTCHEM> |
| 4 | Creative Studies - Chemistry and Biochemistry Emphasis | <https://catalog.ucsb.edu/programs/BSCRTSTCHEMBCHM> |
| 5 | Creative Studies - Computer Science Emphasis | <https://catalog.ucsb.edu/programs/BSCRTSTCOMPSCI> |
| 6 | Creative Studies - Mathematics Emphasis | <https://catalog.ucsb.edu/programs/BSCRTSTMATH> |
| 7 | Creative Studies - Physics Emphasis | <https://catalog.ucsb.edu/programs/BSCRTSTPHYS> |
| 8 | Mathematics | <https://catalog.ucsb.edu/programs/BSMATCS> |
| 9 | Physics | <https://catalog.ucsb.edu/programs/BSPHYCS> |

#### College of Engineering
##### Chemical Engr
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | <https://catalog.ucsb.edu/programs/BSCHEME> |

##### Computer Sci
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | <https://catalog.ucsb.edu/programs/BSCMPSC> |

##### Elect Comp Engr
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | <https://catalog.ucsb.edu/programs/BSCMPEN> |
| 2 | Electrical Engineering | <https://catalog.ucsb.edu/programs/BSEE> |

##### Mechanical Engr
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | <https://catalog.ucsb.edu/programs/BSME> |

##### Unknown
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Individual | <https://catalog.ucsb.edu/programs/BSINDV> |

#### College of Letters and Science
##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | <https://catalog.ucsb.edu/programs/BAANTH> |
| 2 | Anthropology - Archaeology Emphasis | <https://catalog.ucsb.edu/programs/BAANTHARCHAEOL> |
| 3 | Anthropology - Biological Emphasis | <https://catalog.ucsb.edu/programs/BAANTHBIOLGICL> |
| 4 | Anthropology - Cultural Emphasis | <https://catalog.ucsb.edu/programs/BAANTHCULTURAL> |

##### Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | <https://catalog.ucsb.edu/programs/BAART> |

##### Asian Amer Stds
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian American Studies | <https://catalog.ucsb.edu/programs/BAASAM> |

##### Black Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Black Studies | <https://catalog.ucsb.edu/programs/BABLKST> |

##### Chem & Biochem
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | <https://catalog.ucsb.edu/programs/BACHEM> |
| 2 | Pre-Chemistry | <https://catalog.ucsb.edu/programs/BAPRCHM> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | <https://catalog.ucsb.edu/programs/BSBCHEM> |
| 2 | Chemistry | <https://catalog.ucsb.edu/programs/BSCHEM> |
| 3 | Pre-Chemistry | <https://catalog.ucsb.edu/programs/BSPRCHM> |

##### Chicano Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chicana and Chicano Studies | <https://catalog.ucsb.edu/programs/BACHAST> |

##### Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics - Ancient Greek Philosophy Emphasis | <https://catalog.ucsb.edu/programs/ABW8eM1cgyNrdxM30jua> |
| 2 | Classics - Classical Archaeology Emphasis | <https://catalog.ucsb.edu/programs/BACLASSCLASARCH> |
| 3 | Classics - Classical Language & Literature Emphasis | <https://catalog.ucsb.edu/programs/BACLASSCLASLNLT> |
| 4 | Classics - Greek and Roman Culture Emphasis | <https://catalog.ucsb.edu/programs/BACLASSGRECOROM> |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | <https://catalog.ucsb.edu/programs/BACOMM> |
| 2 | Pre-Communication | <https://catalog.ucsb.edu/programs/BAPRCOM> |

##### Comparative Lit
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative Literature - Interdisciplinary Emphasis | <https://catalog.ucsb.edu/programs/BACLITINTERDIS> |
| 2 | Comparative Literature - Multilingual Emphasis | <https://catalog.ucsb.edu/programs/avrAly5uyebjpiuugFLU> |

##### Creative StdsCR
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art - Book Arts Emphasis | <https://catalog.ucsb.edu/programs/BAARTCSBOOKARTS> |
| 2 | Creative Studies - Chemistry Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTCHEM> |
| 3 | Creative Studies - Chemistry and Biochemistry Emphasis | <https://catalog.ucsb.edu/programs/BACRTSTCHEMBCHM> |

##### E As Lng & Clt
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | <https://catalog.ucsb.edu/programs/BAASNST> |
| 2 | Chinese | <https://catalog.ucsb.edu/programs/BACHIN> |
| 3 | Japanese | <https://catalog.ucsb.edu/programs/BAJAPAN> |

##### Earth Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Science | <https://catalog.ucsb.edu/programs/BAEARTH> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Science -  Geobiology & Paleobiology Emphasis | <https://catalog.ucsb.edu/programs/1Y81tx7rjeP3wMSGIBfV> |
| 2 | Earth Science - Climate and Environment Emphasis | <https://catalog.ucsb.edu/programs/BSEARTHCLIMATE> |
| 3 | Earth Science - Geology Emphasis | <https://catalog.ucsb.edu/programs/BSEARTHGEOL> |
| 4 | Earth Science - Geophysics Emphasis | <https://catalog.ucsb.edu/programs/BSEARTHGEOPHYS> |

##### Ecol Ev Mar Bio
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | <https://catalog.ucsb.edu/programs/BABIOSC> |
| 2 | Ecology and Evolution | <https://catalog.ucsb.edu/programs/BAECOEV> |
| 3 | Pre-Biology | <https://catalog.ucsb.edu/programs/BAPRBIO> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aquatic Biology | <https://catalog.ucsb.edu/programs/BSAQBIO> |
| 2 | Biological Sciences | <https://catalog.ucsb.edu/programs/BSBIOSC> |
| 3 | Ecology and Evolution | <https://catalog.ucsb.edu/programs/BSECOEV> |
| 4 | Physiology | <https://catalog.ucsb.edu/programs/BSPHYSY> |
| 5 | Pre-Biology | <https://catalog.ucsb.edu/programs/BSPRBIO> |
| 6 | Zoology | <https://catalog.ucsb.edu/programs/BSZOOL> |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | <https://catalog.ucsb.edu/programs/BAECON> |
| 2 | Economics and Accounting | <https://catalog.ucsb.edu/programs/BAECACC> |
| 3 | Pre-Economics | <https://catalog.ucsb.edu/programs/BAPRECO> |
| 4 | Pre-Economics and Accounting | <https://catalog.ucsb.edu/programs/BAPRECA> |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | <https://catalog.ucsb.edu/programs/BAENGL> |

##### Environ Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | <https://catalog.ucsb.edu/programs/BAENVST> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | <https://catalog.ucsb.edu/programs/BSENVST> |
| 2 | Hydrologic Sciences and Policy | <https://catalog.ucsb.edu/programs/bEPFehP7qK6iYVaHZbHD> |

##### Feminist Stds
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Feminist Studies | <https://catalog.ucsb.edu/programs/BAFEMST> |

##### Film & Media St
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Media Studies | <https://catalog.ucsb.edu/programs/BAFAMST> |
| 2 | Pre-Film and Media Studies | <https://catalog.ucsb.edu/programs/BAPRFAM> |

##### French and Italian
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | <https://catalog.ucsb.edu/programs/BAFR> |
| 2 | Italian Studies | <https://catalog.ucsb.edu/programs/BAITALS> |
| 3 | Italian Studies - Transnational Emphasis | <https://catalog.ucsb.edu/programs/BAITALSTRANSNAT> |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | <https://catalog.ucsb.edu/programs/BAGEOG> |
| 2 | Geography - Geographic Information Science Emphasis | <https://catalog.ucsb.edu/programs/BAGEOGGEOGISCI> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physical Geography | <https://catalog.ucsb.edu/programs/BSGEOGP> |
| 2 | Physical Geography - Ocean Science Emphasis | <https://catalog.ucsb.edu/programs/BSGEOGPOCEANSCI> |

##### German & Slavic
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | German | <https://catalog.ucsb.edu/programs/BAGERM> |
| 2 | Russian and East European Studies | <https://catalog.ucsb.edu/programs/BARUSEU> |

##### Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Studies | <https://catalog.ucsb.edu/programs/BAGLOBL> |
| 2 | Pre-Global Studies | <https://catalog.ucsb.edu/programs/BAPRGLB> |

##### Hist of Art&Arc
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History of Art and Architecture | <https://catalog.ucsb.edu/programs/BAHSART> |
| 2 | History of Art and Architecture - Architecture and Environment Emphasis | <https://catalog.ucsb.edu/programs/BAHSARTARCHENVO> |
| 3 | History of Art and Architecture - Museum Studies Emphasis | <https://catalog.ucsb.edu/programs/BAHSARTMUSEUMST> |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | <https://catalog.ucsb.edu/programs/BAHIST> |
| 2 | History of Policy, Law, and Governance | <https://catalog.ucsb.edu/programs/BAHISPL> |

##### Interdisciplinary
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | <https://catalog.ucsb.edu/programs/BAINTST> |

##### Lat Amer & Iber
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American and Iberian Studies | <https://catalog.ucsb.edu/programs/BALAIS> |

##### Letters & Sci
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Undeclared (Letters and Science) | <https://catalog.ucsb.edu/programs/BAUNDEC> |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Language, Culture, and Society | <https://catalog.ucsb.edu/programs/BALC&S> |
| 2 | Linguistics | <https://catalog.ucsb.edu/programs/BALING> |
| 3 | Linguistics - Chinese Emphasis | <https://catalog.ucsb.edu/programs/BALINGCHINESE> |
| 4 | Linguistics - English Emphasis | <https://catalog.ucsb.edu/programs/BALINGENGLISH> |
| 5 | Linguistics - French Emphasis | <https://catalog.ucsb.edu/programs/BALINGFRENCH> |
| 6 | Linguistics - German Emphasis | <https://catalog.ucsb.edu/programs/BALINGGERMAN> |
| 7 | Linguistics - Japanese Emphasis | <https://catalog.ucsb.edu/programs/BALINGJAPANESE> |
| 8 | Linguistics - Language and Speech Technologies Emphasis | <https://catalog.ucsb.edu/programs/BALINGLASPTECH> |
| 9 | Linguistics - Slavic Emphasis | <https://catalog.ucsb.edu/programs/BALINGSLAVIC> |
| 10 | Linguistics - Spanish Emphasis | <https://catalog.ucsb.edu/programs/BALINGSPANISH> |
| 11 | Linguistics - Speech-Language Sciences and Disorders Emphasis | <https://catalog.ucsb.edu/programs/BALINGSLDS> |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | <https://catalog.ucsb.edu/programs/BAMATH> |
| 2 | Pre-Mathematics | <https://catalog.ucsb.edu/programs/BAPRMTH> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | <https://catalog.ucsb.edu/programs/BSAMATH> |
| 2 | Financial Mathematics and Statistics | <https://catalog.ucsb.edu/programs/BSFINMS> |
| 3 | Mathematics | <https://catalog.ucsb.edu/programs/BSMATH> |
| 4 | Pre-Applied Mathematics | <https://catalog.ucsb.edu/programs/BSPRAMA> |
| 5 | Pre-Financial Mathematics and Statistics | <https://catalog.ucsb.edu/programs/BSPRFMS> |
| 6 | Pre-Mathematics | <https://catalog.ucsb.edu/programs/BSPRMTH> |

##### Medieval Stds
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Medieval Studies | <https://catalog.ucsb.edu/programs/BAMDVST> |

##### Mol Cel Dev Bio
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Molecular and Cellular Biology | <https://catalog.ucsb.edu/programs/cDXDJG2Jiu7hyppVLcfO> |
| 2 | Molecular and Cellular Biology - Biochemistry-Molecular Biology Emphasis | <https://catalog.ucsb.edu/programs/9GCeZFXiS6lY2nFFQDOc> |
| 3 | Molecular and Cellular Biology - Cell and Developmental Biology Emphasis | <https://catalog.ucsb.edu/programs/Uk1mfwnooFHJHmTzD8k0> |
| 4 | Molecular and Cellular Biology - Microbiology Emphasis | <https://catalog.ucsb.edu/programs/82ybjnc0qwzpDGaiQEhb> |
| 5 | Molecular and Cellular Biology - Pharmacology Emphasis | <https://catalog.ucsb.edu/programs/Pjcvn8IvyZnbKFI03Egy> |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Studies | <https://catalog.ucsb.edu/programs/BAMUSST> |
| 2 | Music Studies - Ethnomusicology Emphasis | <https://catalog.ucsb.edu/programs/BAMUSSTETHNOMUS> |
| 3 | Music Studies - Interdisciplinary Studies of Music Emphasis | <https://catalog.ucsb.edu/programs/BAMUSSTINTRDSTD> |
| 4 | Music Studies - Western Art Music Emphasis | <https://catalog.ucsb.edu/programs/BAMUSSTWESTART> |

###### BMus
| # | 专业 | URL |
|---|------|-----|
| 1 | Music - Bassoon Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICBASSOON> |
| 2 | Music - Cello Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICCELLO> |
| 3 | Music - Clarinet Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICCLARINET> |
| 4 | Music - Composition Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICCOMPOSTN> |
| 5 | Music - Double Bass Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICDBLBASS> |
| 6 | Music - Flute Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICFLUTE> |
| 7 | Music - French Horn Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICFRHORN> |
| 8 | Music - Oboe Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICOBOE> |
| 9 | Music - Percussion Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICPERCUSSN> |
| 10 | Music - Piano Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICPIANO> |
| 11 | Music - Trombone Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICTROMBONE> |
| 12 | Music - Trumpet Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICTRUMPET> |
| 13 | Music - Tuba Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICTUBA> |
| 14 | Music - Viola Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICVIOLA> |
| 15 | Music - Violin Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICVIOLIN> |
| 16 | Music - Voice Emphasis | <https://catalog.ucsb.edu/programs/BMMUSICVOICE> |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | <https://catalog.ucsb.edu/programs/BAPHIL> |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | <https://catalog.ucsb.edu/programs/BAPHYS> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | <https://catalog.ucsb.edu/programs/BSPHYS> |

##### Political Sci
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | <https://catalog.ucsb.edu/programs/BAPOLS> |
| 2 | Pre-Political Science | <https://catalog.ucsb.edu/programs/BAPRPOL> |

##### Psy & Brain Sci
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biopsychology | <https://catalog.ucsb.edu/programs/BSBIPSY> |
| 2 | Pre-Biopsychology | <https://catalog.ucsb.edu/programs/BSPRBPY> |
| 3 | Pre-Psychological & Brain Sciences | <https://catalog.ucsb.edu/programs/BSPRPBS> |
| 4 | Psychological & Brain Sciences | <https://catalog.ucsb.edu/programs/BSPBS> |

##### Religious Stds
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Middle East Studies | <https://catalog.ucsb.edu/programs/BAMESTD> |
| 2 | Religious Studies | <https://catalog.ucsb.edu/programs/BARGSTD> |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-Sociology | <https://catalog.ucsb.edu/programs/BAPRSOC> |
| 2 | Sociology | <https://catalog.ucsb.edu/programs/BASOC> |

##### Spanish & Port
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Portuguese | <https://catalog.ucsb.edu/programs/BAPORT> |
| 2 | Spanish | <https://catalog.ucsb.edu/programs/BASPAN> |

##### Stats Appl Prob
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-Statistics and Data Science | <https://catalog.ucsb.edu/programs/BAPRSDS> |
| 2 | Statistics and Data Science | <https://catalog.ucsb.edu/programs/BASTSDS> |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | <https://catalog.ucsb.edu/programs/BSACTSC> |
| 2 | Pre-Actuarial Science | <https://catalog.ucsb.edu/programs/BSPRACT> |
| 3 | Pre-Statistics and Data Science | <https://catalog.ucsb.edu/programs/BSPRSDS> |
| 4 | Statistics and Data Science | <https://catalog.ucsb.edu/programs/BSSTSDS> |

##### Theater & Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | <https://catalog.ucsb.edu/programs/BADANCE> |
| 2 | Theater | <https://catalog.ucsb.edu/programs/BATHTR> |
| 3 | Theater - Theater Design Emphasis | <https://catalog.ucsb.edu/programs/xciwnIercvhw9dsRYQpE> |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | <https://catalog.ucsb.edu/programs/BFADANCE> |
| 2 | Theater - Acting Emphasis | <https://catalog.ucsb.edu/programs/BFATHTRACTING> |

##### Unknown
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Individual | <https://catalog.ucsb.edu/programs/BAINDIV> |

### 1.3 Interdisciplinary / cross-college undergraduate programs

UCSB's College of Creative Studies (CCS) offers programs that cross-list with Letters & Science and Engineering. CCS programs are listed under the CCS college section above.

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | American Indian and Indigenous Studies | College of Letters and Science / Religious Stds | <https://catalog.ucsb.edu/programs/6jRikJ0kTEiFJgF5KRqY> |
| 2 | Anthropology | College of Letters and Science / Anthropology | <https://catalog.ucsb.edu/programs/TvgU9p4DW3QV32DgILsL> |
| 3 | Applied Psychology | Graduate School of Education / Couns/Clin/Schl | <https://catalog.ucsb.edu/programs/Mh7tNXlDWPz5nIQRR94e> |
| 4 | Architecture & Urban History | College of Letters and Science / Hist of Art&Arc | <https://catalog.ucsb.edu/programs/vWNTsyXphvYy0lSOkCEn> |
| 5 | Asian American Studies | College of Letters and Science / Asian Amer Stds | <https://catalog.ucsb.edu/programs/ScOPB2IWbUnIRzvRleMq> |
| 6 | Astronomy and Planetary Science | College of Letters and Science / Physics | <https://catalog.ucsb.edu/programs/gEIEmbbwlSAWFuGAZIs3> |
| 7 | Black Studies | College of Letters and Science / Black Studies | <https://catalog.ucsb.edu/programs/tTxCJdRNvQDoqKlBBkLi> |
| 8 | Chemistry | College of Letters and Science / Chem & Biochem | <https://catalog.ucsb.edu/programs/OnVSShnabOoErNazCEMl> |
| 9 | Chicana and Chicano Studies | College of Letters and Science / Chicano Studies | <https://catalog.ucsb.edu/programs/WekJwhc027jYXvSB3hkl> |
| 10 | Chinese | College of Letters and Science / E As Lng & Clt | <https://catalog.ucsb.edu/programs/BqJdshkEB6vyuzcTwTWP> |
| 11 | Classics | College of Letters and Science / Classics | <https://catalog.ucsb.edu/programs/bkxoln9NJWDwz0TH2qyz> |
| 12 | Comparative Literature | College of Letters and Science / Comparative Lit | <https://catalog.ucsb.edu/programs/G6p9MJv0pDXsRUZXe8vw> |
| 13 | Earth Science | College of Letters and Science / Earth Science | <https://catalog.ucsb.edu/programs/5GXc6rr7lBk2tnzXriiM> |
| 14 | Educational Studies | Graduate School of Education / Education | <https://catalog.ucsb.edu/programs/JbuncR3fvgtCcGMntnjz> |
| 15 | English | College of Letters and Science / English | <https://catalog.ucsb.edu/programs/m3ZHQZLHiTKeKmI76gF3> |
| 16 | Feminist Studies | College of Letters and Science / Feminist Stds | <https://catalog.ucsb.edu/programs/EK5TKmYnukwvbarMYnkv> |
| 17 | French | College of Letters and Science / French and Italian | <https://catalog.ucsb.edu/programs/ltjmqnexV25zw1T3YIQ8> |
| 18 | Game Studies | College of Letters and Science / Hist of Art&Arc | <https://catalog.ucsb.edu/programs/LtHXjlgdOjhIa1etL80U> |
| 19 | German Studies | College of Letters and Science / German & Slavic | <https://catalog.ucsb.edu/programs/NHNmHVOGJjYrzTN7YUpM> |
| 20 | History | College of Letters and Science / History | <https://catalog.ucsb.edu/programs/ihw0fKkjh8z4pCIEWq5A> |
| 21 | History of Art & Architecture | College of Letters and Science / Hist of Art&Arc | <https://catalog.ucsb.edu/programs/AXni4dsrCMDpQ9DHAxdG> |
| 22 | Iranian Studies | College of Letters and Science / Religious Stds | <https://catalog.ucsb.edu/programs/yhWlSEg2CDzz84k4AqlQ> |
| 23 | Italian | College of Letters and Science / French and Italian | <https://catalog.ucsb.edu/programs/FmzNQxQruftko7PYc6GU> |
| 24 | Japanese | College of Letters and Science / E As Lng & Clt | <https://catalog.ucsb.edu/programs/YOEKriTnzMICe7gzkvN1> |
| 25 | Jewish Studies | College of Letters and Science / Religious Stds | <https://catalog.ucsb.edu/programs/l0T2AKxZV6exHw8q3HzD> |
| 26 | Labor Studies | College of Letters and Science / History | <https://catalog.ucsb.edu/programs/RR5QOChfokC7bLMu9qre> |
| 27 | Language & Speech Technologies | College of Letters and Science / Linguistics | <https://catalog.ucsb.edu/programs/F8N6GPVhwoni0ywNg2Cp> |
| 28 | Latin American & Iberian Studies | College of Letters and Science / Lat Amer & Iber | <https://catalog.ucsb.edu/programs/vCUbrNOAhXsbxWVqDrg5> |
| 29 | Legal Humanities | College of Letters and Science / Interdisciplinary | <https://catalog.ucsb.edu/programs/Ww0LJ9rq4EamyT5dYkhC> |
| 30 | Legal Humanities | College of Letters and Science / Interdisciplinary | <https://catalog.ucsb.edu/programs/FF7Syj8QgIubR9MRXeVD> |
| 31 | Lesbian, Gay, Bisexual, Transgender, & Queer Studies | College of Letters and Science / Feminist Stds | <https://catalog.ucsb.edu/programs/tJzCBDDqgU7GVc5XTwbz> |
| 32 | Linguistics | College of Letters and Science / Linguistics | <https://catalog.ucsb.edu/programs/VeH4o1l3qkynM7REkGLP> |
| 33 | Mathematics | College of Letters and Science / Mathematics | <https://catalog.ucsb.edu/programs/hRoE0M3erWvxWAcOTOFJ> |
| 34 | Mathematics for High School Teaching | College of Letters and Science / Mathematics | <https://catalog.ucsb.edu/programs/MuHphlTKZnEnZQXTRz3y> |
| 35 | Media Arts and Design- Minor | College of Letters and Science / Media Arts & Te | <https://catalog.ucsb.edu/programs/LFTURyih1ii2pmVp0VT3> |
| 36 | Medieval Studies | College of Letters and Science / Medieval Stds | <https://catalog.ucsb.edu/programs/EIQ4TR7moZGokxM6aSiE> |
| 37 | Museum Studies | College of Letters and Science / Hist of Art&Arc | <https://catalog.ucsb.edu/programs/u7cr9KDjDnnB8CYvYhAY> |
| 38 | Music | College of Letters and Science / Music | <https://catalog.ucsb.edu/programs/9OhtTSghSQhujt3wDlFC> |
| 39 | Philosophy | College of Letters and Science / Philosophy | <https://catalog.ucsb.edu/programs/ozX6BAQklI0AShzhWhIc> |
| 40 | Physics | College of Letters and Science / Physics | <https://catalog.ucsb.edu/programs/jElvmKTTVASrWw6PIDxB> |
| 41 | Portuguese | College of Letters and Science / Spanish & Port | <https://catalog.ucsb.edu/programs/CXqhbw3y6MCIfK2CNdvD> |
| 42 | Poverty, Inequality, and Social Justice | College of Letters and Science / History | <https://catalog.ucsb.edu/programs/1iNwTTWHMydrGXDxDxRh> |
| 43 | Professional Writing | College of Letters and Science / Writing Program | <https://catalog.ucsb.edu/programs/GSPARUgBEnhMtzTOM6bg> |
| 44 | Religious Studies | College of Letters and Science / Religious Stds | <https://catalog.ucsb.edu/programs/zdijRccrH4dKMxKgbxij> |
| 45 | Russian | College of Letters and Science / German & Slavic | <https://catalog.ucsb.edu/programs/AzDfCkZPBQVO46OKZWB7> |
| 46 | Science and Mathematics Education | Graduate School of Education / Education | <https://catalog.ucsb.edu/programs/zWFHL9VhUscWE7goOJdZ> |
| 47 | Sociocultural Linguistics | College of Letters and Science / Linguistics | <https://catalog.ucsb.edu/programs/NLTsDYuNyLY7au8k23hy> |
| 48 | Spanish | College of Letters and Science / Spanish & Port | <https://catalog.ucsb.edu/programs/c6N2E3aQxD7OvvrKFdED> |
| 49 | Speech-Language Sciences & Disorders | College of Letters and Science / Linguistics | <https://catalog.ucsb.edu/programs/Dr8c5wOyIVohltlqftKe> |
| 50 | Statistical Science | College of Letters and Science / Stats Appl Prob | <https://catalog.ucsb.edu/programs/HktKyCJK0ZSb1IoIKtyk> |
| 51 | Teaching English to Speakers of Other Languages (TESOL) | College of Letters and Science / Linguistics | <https://catalog.ucsb.edu/programs/qY2bh5NBNGjWWrq7VuPP> |
| 52 | Theater | College of Letters and Science / Theater & Dance | <https://catalog.ucsb.edu/programs/pfWK2EPxmqo8cGj7TKMc> |
| 53 | Theater Production and Design | College of Letters and Science / Theater & Dance | <https://catalog.ucsb.edu/programs/6fk4UKjpKspAWZO8zMdq> |
| 54 | Translation Studies | College of Letters and Science / Comparative Lit | <https://catalog.ucsb.edu/programs/IauVsyBBgzZV9DfR5gVP> |

---

## SECTION 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Engineering
##### Bioengineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Engineering | <https://catalog.ucsb.edu/programs/MSBIOE> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Engineering | <https://catalog.ucsb.edu/programs/PHDBIOE> |

##### Chemical Engr
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | <https://catalog.ucsb.edu/programs/MSCHEME> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | <https://catalog.ucsb.edu/programs/PHDCHEME> |

##### Computer Sci
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | <https://catalog.ucsb.edu/programs/MSCMPSC> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science - Technology & Society Emphasis | <https://catalog.ucsb.edu/programs/PHDCMPSCTECHNSOC> |
| 2 | Computer Science | <https://catalog.ucsb.edu/programs/PHDCMPSC> |

##### Elect Comp Engr
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | <https://catalog.ucsb.edu/programs/MSECE> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | <https://catalog.ucsb.edu/programs/PHDECE> |

##### Materials
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Materials | <https://catalog.ucsb.edu/programs/MSMATRL> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Materials | <https://catalog.ucsb.edu/programs/PHDMATRL> |

##### Mechanical Engr
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | <https://catalog.ucsb.edu/programs/MSME> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | <https://catalog.ucsb.edu/programs/PHDME> |

##### Tech Management
###### MTM
| # | 项目 | URL |
|---|------|-----|
| 1 | Technology Management | <https://catalog.ucsb.edu/programs/MTMTM> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Technology Management | <https://catalog.ucsb.edu/programs/PHDTM> |

#### College of Letters and Science
##### Anthropology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | <https://catalog.ucsb.edu/programs/MAANTH> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | <https://catalog.ucsb.edu/programs/PHDANTH> |

##### Art
###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | <https://catalog.ucsb.edu/programs/MFAART> |

##### Chem & Biochem
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | <https://catalog.ucsb.edu/programs/MACHEM> |
| 2 | Chemistry - Chemical Education Emphasis | <https://catalog.ucsb.edu/programs/MACHEMCHEMEDUC> |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | <https://catalog.ucsb.edu/programs/MSCHEM> |

##### Chicano Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Chicana and Chicano Studies | <https://catalog.ucsb.edu/programs/MACHAST> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chicana and Chicano Studies | <https://catalog.ucsb.edu/programs/PHDCHAST> |

##### Classics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics | <https://catalog.ucsb.edu/programs/MACLASS> |
| 2 | Classics - Ancient History Emphasis | <https://catalog.ucsb.edu/programs/MACLASSANCNHIST> |
| 3 | Classics - Greek Emphasis | <https://catalog.ucsb.edu/programs/MACLASSGREEK> |
| 4 | Classics - Latin Emphasis | <https://catalog.ucsb.edu/programs/MACLASSLATIN> |
| 5 | Classics - Literature and Theory Emphasis | <https://catalog.ucsb.edu/programs/MACLASSLITTHRY> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics - Ancient History Emphasis | <https://catalog.ucsb.edu/programs/PHDCLASSANCNHIST> |
| 2 | Classics - Literature and Theory Emphasis | <https://catalog.ucsb.edu/programs/PHDCLASSLITTHRY> |
| 3 | Classics | <https://catalog.ucsb.edu/programs/PHDCLASS> |

##### Communication
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | <https://catalog.ucsb.edu/programs/MACOMM> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | <https://catalog.ucsb.edu/programs/PHDCOMM> |

##### Comparative Lit
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Literature | <https://catalog.ucsb.edu/programs/MACLIT> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Literature | <https://catalog.ucsb.edu/programs/PHDCLIT> |

##### Dynamical Neuroscience
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Dynamical Neuroscience | <https://catalog.ucsb.edu/programs/MADYNS> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Dynamical Neuroscience | <https://catalog.ucsb.edu/programs/PHDDYNS> |

##### E As Lng & Clt
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Asian Studies | <https://catalog.ucsb.edu/programs/MAASNST> |
| 2 | Asian Studies - East Asian Languages and Cultural Studies Emphasis | <https://catalog.ucsb.edu/programs/MAASNSTEASIANLC> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | East Asian Languages & Cultural Studies | <https://catalog.ucsb.edu/programs/PHDEALCS> |

##### Earth Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Earth Science | <https://catalog.ucsb.edu/programs/MSEARTH> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Earth Science | <https://catalog.ucsb.edu/programs/PHDEARTH> |

##### Ecol Ev Mar Bio
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology, Evolution, and Marine Biology | <https://catalog.ucsb.edu/programs/BwhQpek2wvpANDwtPUGu> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology, Evolution, and Marine Biology | <https://catalog.ucsb.edu/programs/PHDEEMB> |

##### Economics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | <https://catalog.ucsb.edu/programs/MAECON> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | <https://catalog.ucsb.edu/programs/PHDECON> |

##### English
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | <https://catalog.ucsb.edu/programs/MAENGL> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | English - Technology & Society Emphasis | <https://catalog.ucsb.edu/programs/PHDENGLTECHNSOC> |
| 2 | English | <https://catalog.ucsb.edu/programs/PHDENGL> |

##### Feminist Stds
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Feminist Studies | <https://catalog.ucsb.edu/programs/MAFEMST> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Feminist Studies | <https://catalog.ucsb.edu/programs/PHDFEMST> |

##### Film & Media St
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Film and Media Studies | <https://catalog.ucsb.edu/programs/MAFAMST> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Film and Media Studies | <https://catalog.ucsb.edu/programs/PHDFAMST> |

##### Geography
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography | <https://catalog.ucsb.edu/programs/MAGEOG> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography | <https://catalog.ucsb.edu/programs/PHDGEOG> |

##### Global Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Studies | <https://catalog.ucsb.edu/programs/MAGLOBL> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Studies | <https://catalog.ucsb.edu/programs/PHDGLOBL> |

##### Hist of Art&Arc
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | History of Art and Architecture | <https://catalog.ucsb.edu/programs/MAHSART> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History of Art and Architecture | <https://catalog.ucsb.edu/programs/PHDHSART> |

##### History
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | History | <https://catalog.ucsb.edu/programs/MAHIST> |
| 2 | History - Public Historical Studies Emphasis | <https://catalog.ucsb.edu/programs/MAHISTPBHISTSD> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History - Labor Studies Emphasis | <https://catalog.ucsb.edu/programs/PHDHISTLABOR> |
| 2 | History - Public Historical Studies Emphasis | <https://catalog.ucsb.edu/programs/PHDHISTPBHISTSD> |
| 3 | History - Public History Emphasis | <https://catalog.ucsb.edu/programs/PHDHISTPBHISTSA> |
| 4 | History | <https://catalog.ucsb.edu/programs/PHDHIST> |

##### Int Prg Qnt Bio
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry/Molecular Biology | <https://catalog.ucsb.edu/programs/MSBMB> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry/Molecular Biology | <https://catalog.ucsb.edu/programs/PHDBMB> |

##### Lat Amer & Iber
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Latin American and Iberian Studies | <https://catalog.ucsb.edu/programs/MALAIS> |

##### Linguistics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Linguistics | <https://catalog.ucsb.edu/programs/MALING> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Linguistics | <https://catalog.ucsb.edu/programs/PHDLING> |

##### Marine Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Science | <https://catalog.ucsb.edu/programs/MSMARSC> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Science | <https://catalog.ucsb.edu/programs/PHDMARSC> |

##### Mathematics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | <https://catalog.ucsb.edu/programs/MAAMATH> |
| 2 | Mathematics | <https://catalog.ucsb.edu/programs/MAMATH> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | <https://catalog.ucsb.edu/programs/PHDMATH> |

##### Media Arts & Te
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Media Arts and Technology | <https://catalog.ucsb.edu/programs/MSMAT> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Media Arts and Technology | <https://catalog.ucsb.edu/programs/PHDMAT> |

##### Mol Cel Dev Bio
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Molecular, Cellular, & Develop. Biology | <https://catalog.ucsb.edu/programs/Xl5JAOeFtyCohSEh33pV> |
| 2 | Molecular, Cellular, & Develop. Biology - Biological Education Emphasis | <https://catalog.ucsb.edu/programs/rfHaftFDkEGOu7Rp3QsF> |
| 3 | Molecular, Cellular, & Develop. Biology - Pharmacology and Biotechnology Emphasis | <https://catalog.ucsb.edu/programs/FZiSRS2aqDciykdc9qqb> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry-Molecular Biology | <https://catalog.ucsb.edu/programs/PHDBIOCM> |
| 2 | Molecular, Cellular, & Develop. Biology | <https://catalog.ucsb.edu/programs/PHDMCDB> |

##### Music
###### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | <https://catalog.ucsb.edu/programs/DMAMUSIC> |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | <https://catalog.ucsb.edu/programs/MAMUSIC> |
| 2 | Music - Composition Emphasis | <https://catalog.ucsb.edu/programs/MAMUSICCOMPOSTN> |
| 3 | Music - Ethnomusicology Emphasis | <https://catalog.ucsb.edu/programs/MAMUSICETHNOMUS> |
| 4 | Music - Musicology Emphasis | <https://catalog.ucsb.edu/programs/MAMUSICMUSCLGY> |
| 5 | Music - Theory Emphasis | <https://catalog.ucsb.edu/programs/MAMUSICTHEORY> |

###### MMus
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | <https://catalog.ucsb.edu/programs/MMMUSIC> |
| 2 | Music - Brass Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICBRASS> |
| 3 | Music - Conducting Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICCONDUCT> |
| 4 | Music - Keyboard Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICKEYBOARD> |
| 5 | Music - Piano Accompanying Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICPIANOACC> |
| 6 | Music - Strings Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICSTRINGS> |
| 7 | Music - Voice Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICVOICE> |
| 8 | Music - Woodwinds and Brass Emphasis | <https://catalog.ucsb.edu/programs/MMMUSICWDWNDBRS> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music - Composition Emphasis | <https://catalog.ucsb.edu/programs/PHDMUSICCOMPOSTN> |
| 2 | Music - Ethnomusicology Emphasis | <https://catalog.ucsb.edu/programs/PHDMUSICETHNOMUS> |
| 3 | Music - Musicology Emphasis | <https://catalog.ucsb.edu/programs/PHDMUSICMUSCLGY> |
| 4 | Music - Theory Emphasis | <https://catalog.ucsb.edu/programs/PHDMUSICTHEORY> |

##### Philosophy
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | <https://catalog.ucsb.edu/programs/MAPHIL> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | <https://catalog.ucsb.edu/programs/PHDPHIL> |

##### Physics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | <https://catalog.ucsb.edu/programs/MAPHYS> |
| 2 | Physics - Astrophysics Emphasis | <https://catalog.ucsb.edu/programs/MAPHYSASTRPHYS> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics - Astrophysics Emphasis | <https://catalog.ucsb.edu/programs/PHDPHYSASTRPHYS> |
| 2 | Physics | <https://catalog.ucsb.edu/programs/PHDPHYS> |

##### Political Sci
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | <https://catalog.ucsb.edu/programs/MAPOLS> |
| 2 | Political Science - International Relations Emphasis | <https://catalog.ucsb.edu/programs/MAPOLSINTRREL> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science - International Relations Emphasis | <https://catalog.ucsb.edu/programs/PHDPOLSINTRREL> |
| 2 | Political Science - Technology & Society Emphasis | <https://catalog.ucsb.edu/programs/PHDPOLSTECHNSOC> |
| 3 | Political Science - Women's Studies Emphasis | <https://catalog.ucsb.edu/programs/PHDPOLSWOMST> |
| 4 | Political Science | <https://catalog.ucsb.edu/programs/PHDPOLS> |

##### Psy & Brain Sci
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychological & Brain Sciences | <https://catalog.ucsb.edu/programs/MAPBS> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychological & Brain Sciences | <https://catalog.ucsb.edu/programs/PHDPBS> |
| 2 | Psychological & Brain Sciences - Technology & Society Emphasis | <https://catalog.ucsb.edu/programs/PHDPBSTECHNSOC> |
| 3 | Psychology | <https://catalog.ucsb.edu/programs/PHDPSY> |
| 4 | Psychology - Human Development Emphasis | <https://catalog.ucsb.edu/programs/PHDPSYHUMDEV> |
| 5 | Psychology - Technology & Society Emphasis | <https://catalog.ucsb.edu/programs/PHDPSYTECHNSOC> |

##### Religious Stds
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Religious Studies | <https://catalog.ucsb.edu/programs/MARGSTD> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Religious Studies | <https://catalog.ucsb.edu/programs/PHDRGSTD> |

##### Sociology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | <https://catalog.ucsb.edu/programs/MASOC> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | <https://catalog.ucsb.edu/programs/PHDSOC> |

##### Spanish & Port
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Portuguese | <https://catalog.ucsb.edu/programs/MAPORT> |
| 2 | Spanish | <https://catalog.ucsb.edu/programs/MASPAN> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Hispanic Languages and Literatures | <https://catalog.ucsb.edu/programs/PHDHSPLL> |

##### Stats Appl Prob
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | <https://catalog.ucsb.edu/programs/MASTATS> |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Science | <https://catalog.ucsb.edu/programs/MSACTSC> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics and Applied Probability - Financial Mathematics and Statistics Emphasis | <https://catalog.ucsb.edu/programs/PHDSTSAPFINMS> |
| 2 | Statistics and Applied Probability | <https://catalog.ucsb.edu/programs/PHDSTSAP> |

##### Theater & Dance
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Theater, Dance, and Performance Studies | <https://catalog.ucsb.edu/programs/MATHDPS> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Theater, Dance, and Performance Studies | <https://catalog.ucsb.edu/programs/PHDTHDPS> |

##### Unknown
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Individual | <https://catalog.ucsb.edu/programs/MAINDIV> |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Geological Sciences | <https://catalog.ucsb.edu/programs/MSGEOL> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Individual | <https://catalog.ucsb.edu/programs/PHDINDIV> |

#### Graduate School of Education
##### Couns/Clin/Schl
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling Psychology | <https://catalog.ucsb.edu/programs/MACNPSY> |

###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology | <https://catalog.ucsb.edu/programs/MEDSCLP> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling/Clinical/School Psychology - Clinical Psychology Emphasis | <https://catalog.ucsb.edu/programs/PHDCNCSPCLINICAL> |
| 2 | Counseling/Clinical/School Psychology - Counseling Psychology Emphasis | <https://catalog.ucsb.edu/programs/PHDCNCSPCOUNPSY> |
| 3 | School Psychology | <https://catalog.ucsb.edu/programs/PHDSCLP> |

##### Education
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | <https://catalog.ucsb.edu/programs/MAEDUC> |

###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | <https://catalog.ucsb.edu/programs/MEDEDUC> |
| 2 | Education - Confluent Education Emphasis | <https://catalog.ucsb.edu/programs/MEDEDUCCONFLUNT> |
| 3 | Education - Counseling Psychology Emphasis | <https://catalog.ucsb.edu/programs/MEDEDUCCOUNPSY> |
| 4 | Education - School Psychology Emphasis | <https://catalog.ucsb.edu/programs/MEDEDUCSCHLPSY> |
| 5 | Education - Special Education Emphasis | <https://catalog.ucsb.edu/programs/MEDEDUCSPECEDUC> |
| 6 | Education - Teaching Emphasis | <https://catalog.ucsb.edu/programs/MEDEDUCTEACHING> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | <https://catalog.ucsb.edu/programs/PHDEDUC> |

#### L&S
##### Chem & Biochem
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | <https://catalog.ucsb.edu/programs/PHDCHEM> |

#### School of Environmental Science & Management
##### Env. Sci. & Mgm
###### MEDS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Data Science | <https://catalog.ucsb.edu/programs/MDSEDS> |

###### MESM
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science and Management | <https://catalog.ucsb.edu/programs/MESESM> |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science and Management | <https://catalog.ucsb.edu/programs/Yyj4T9Sj5UcZwSYGAjxY> |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Science and Management | <https://catalog.ucsb.edu/programs/PHDESM> |

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 |
|------|-----|
| 申请系统 | UC Application (https://admission.universityofcalifornia.edu/apply-now.html) |
| 申请开放日期 | August 1 |
| 申请提交窗口 | October 1 - November 30 |
| EA/ED | N/A (UC系统无EA/ED) |
| RD 截止日期 | November 30 |
| 决定通知 | Mid-March |
| SIR 截止日期 | May 1 (First-Year) / June 1 (Transfer) |
| SAT/ACT 政策 | Test-FREE — 不用于录取决定，仅用于入学后课程 placement |
| 推荐信 | 不要求 |
| 面试 | 不要求 |
| 申请费 | $80 (每个UC校区) |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低要求 | 备注 |
|------|---------|------|
| TOEFL iBT (2026年1月前考试) | 80 | 从考试机构直接发送 |
| TOEFL iBT (2026年1月及之后考试) | 4.5 (新评分标准) | 从考试机构直接发送 |
| IELTS | 6.5 | 不接受IELTS One Skill Retake |
| Duolingo English Test (DET) | 115 | 从考试机构直接发送 |
| AP English (Language or Literature) | 3, 4, or 5 | |
| IB English (Language A only) | SL 6-7 / HL 5-7 | |
| SAT Writing and Language | 31+ | 数字SAT Reading and Writing不适用 |
| ACT English Language Arts | 24+ | |
| UC-transferable English composition course | C or better | 3学期或4学分单位 |

> 适用条件: 母语非英语且高中/大学教育非英语授课，或英语教育不满3年
> 成绩有效期: 2年；必须在入学前7月前可用

### 3.3 Graduate — global rules

| 维度 | 值 |
|------|-----|
| 申请方式 | 各研究生项目独立审核，通过UCSB Graduate Division申请门户 |
| 申请门户 | https://www.graddiv.ucsb.edu/eapp/Login.aspx |
| 申请费 | $135 (国际学生) / $120 (国内学生) |
| GRE 政策 | 因项目而异，部分项目optional或not required |
| 语言要求 | 因项目而异，通常TOEFL 80+ / IELTS 6.5+ |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

| 费用项目 | 金额 (CA Resident) | 说明 |
|---------|-------------------|------|
| Tuition and Student Services Fee | $15,588 | 注册费 + 学生服务费 |
| Campus Based Fees | $2,085 | 校园设施费 |
| Book & Supplies | $1,515 | 书本和学习用品 |
| Rent | $13,203 | 校内宿舍 (Residence Halls) |
| Food | $10,782 | 餐饮 |
| Utilities | $0 | 宿舍含水电 |
| Transportation | $789 | 交通 |
| Health Care Allowance | $4,008 | 医疗保险 |
| Personal Expenses | $2,652 | 个人开支 |
| Telephone/Cell Phone | $324 | 通讯 |
| **Total (CA Resident)** | **$50,946** | |
| Non-Resident Supplemental Tuition | $39,270 | 非加州居民附加学费 |
| **Total (Non-Resident)** | **$90,216** | |

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 |
|------|-----|
| Need-blind/Need-aware | Need-aware for international students |
| 国际学生经济援助 | 有限，need-aware |
| UC Blue and Gold Opportunity Plan | 家庭收入<$80,000的CA居民学费全免 |
| Promise Scholars Program | 针对first-generation和low-income学生 |

### 4.3 Graduate cost & funding framework

| 费用项目 | 金额 (CA Resident) | 说明 |
|---------|-------------------|------|
| Tuition and Student Services Fee | $15,066 | |
| Campus Based Fees | $1,389 | |
| Book & Supplies | $1,611 | |
| Rent | $9,261 | San Clemente Apartments |
| Food | $9,402 | |
| Utilities (includes Phone) | $1,932 | |
| Transportation | $4,362 | |
| Health Care Allowance | $9,384 | |
| Personal Expenses | $3,450 | |
| **Total (CA Resident)** | **$55,857** | |
| Non-Resident Supplemental Tuition | $15,102 | |
| **Total (Non-Resident)** | **$70,959** | |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.application_window
  value: October 1 - November 30
  source_url: https://admissions.sa.ucsb.edu/deadlines
  source_snippet: "October 1 - November 30: Submit your fall 2027 UC Application"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

```yaml
E-U-002:
  field: undergraduate.costs.tuition_in_state
  value: $15,588
  source_url: https://www.finaid.ucsb.edu/costs-estimated-aid/cost-attendance/ucsb-undergraduate-cost-attendance-budget
  source_snippet: "Tuition and Student Services Fee ... $ 15,588"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```

```yaml
E-U-003:
  field: undergraduate.costs.total_ca_resident
  value: $50,946
  source_url: https://www.finaid.ucsb.edu/costs-estimated-aid/cost-attendance/ucsb-undergraduate-cost-attendance-budget
  source_snippet: "Total (CA Resident) ... $ 50,946"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```

```yaml
E-U-004:
  field: undergraduate.costs.total_nonresident
  value: $90,216
  source_url: https://www.finaid.ucsb.edu/costs-estimated-aid/cost-attendance/ucsb-undergraduate-cost-attendance-budget
  source_snippet: "Total (Non-Resident) ... $ 90,216"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```

```yaml
E-U-005:
  field: undergraduate.tests.sat_act_policy
  value: Test-FREE (not used in admission)
  source_url: https://admissions.sa.ucsb.edu/freshman-eligibility-selection
  source_snippet: "UCSB will not use SAT/ACT scores in our admission decisions or scholarship selection process"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

```yaml
E-U-006:
  field: undergraduate.tests.english.tofl_min
  value: 80 (iBT before Jan 2026) / 4.5 (new scale Jan 2026+)
  source_url: https://admissions.sa.ucsb.edu/english-language-proficiency
  source_snippet: "Internet-based test (iBT) or iBT Home Edition test taken before January 2026: Minimum score of 80 or better"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

```yaml
E-U-007:
  field: undergraduate.tests.english.ielts_min
  value: 6.5
  source_url: https://admissions.sa.ucsb.edu/english-language-proficiency
  source_snippet: "Score 6.5 or higher on the International English Language Testing System (IELTS)"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

```yaml
E-U-008:
  field: undergraduate.tests.english.det_min
  value: 115
  source_url: https://admissions.sa.ucsb.edu/english-language-proficiency
  source_snippet: "Duolingo English Test (DET): Minimum score of 115"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

```yaml
E-U-009:
  field: undergraduate.eligibility.gpa
  value: 3.0 minimum (3.4 for non-CA residents)
  source_url: https://admissions.sa.ucsb.edu/freshman-eligibility-selection
  source_snippet: "Students must earn a minimum GPA of 3.0 (3.4 for non-California residents) in all A-G courses"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

```yaml
E-U-010:
  field: undergraduate.programs.total
  value: 384 (178 UG majors + 54 minors + 152 grad programs)
  source_url: https://catalog.ucsb.edu/programs
  source_snippet: "329 results found" (catalog page); API returns 384 active programs
  capture_date: 2026-07-05
  evidence_type: official_webpage (Coursedog API)
```

```yaml
E-G-001:
  field: graduate.costs.tuition_in_state
  value: $15,066
  source_url: https://www.finaid.ucsb.edu/costs-estimated-aid/cost-attendance/ucsb-graduate-cost-attendance-budget
  source_snippet: "Tuition and Student Services Fee ... $ 15,066"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
ucsb-knowledge-base-v2/
├── 00-institution-overview
│   ├── counts-hierarchy.md
│   ├── degree-inventory.md
│   └── distribution-matrix.md
├── 01-undergraduate-education
│   ├── college-of-creative-studies-majors.md
│   ├── college-of-engineering-majors.md
│   ├── college-of-letters-and-science-majors.md
│   └── minors-complete-list.md
├── 02-graduate-education
│   ├── college-of-engineering-programs.md
│   ├── college-of-letters-and-science-programs.md
│   ├── graduate-school-of-education-programs.md
│   ├── l&s-programs.md
│   ├── school-of-environmental-science-&-management-programs.md
├── 03-requirements-deadlines
│   ├── ug-deadlines-requirements.md
│   ├── english-proficiency.md
│   └── graduate-admissions.md
├── 04-costs-financial-aid
│   ├── ug-cost-breakdown.md
│   ├── grad-cost-breakdown.md
│   └── financial-aid-policy.md
├── 05-evidence-chain
│   └── evidence-index.md
└── 06-monitoring-watchlist
    └── change-detection.md
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标URL |
|--------|--------|---------|
| P0 | 各研究生项目详细申请要求 (GRE/GPA/推荐信) | 各项目详情页 |
| P0 | 国际学生经济援助详细政策 | https://admissions.sa.ucsb.edu/international |
| P1 | Transfer admission requirements | https://admissions.sa.ucsb.edu/transfer |
| P1 | TAG (Transfer Admission Guarantee) 详情 | https://uctap.universityofcalifornia.edu/ |
| P2 | 校园住宿详情和费用 | https://www.housing.ucsb.edu/ |
| P2 | 奖学金详情 | https://www.finaid.ucsb.edu/types-aid |

---

## SECTION 7 — Cross-school Comparison Framework

| 维度 | UCSB | (其他学校列) |
|------|------|-------------|
| 总项目数 (Rule 1) | 384 | |
| UG 学位专业 | 178 | |
| UG 辅修 | 54 | |
| 研究生项目 | 152 | |
| 学院数 | 6 (含L&S重复) / 5 unique | |
| UG 学费/年 (CA Resident) | $15,588 | |
| UG 总费用/年 (CA Resident) | $50,946 | |
| UG 总费用/年 (Non-Resident) | $90,216 | |
| Need-blind (intl?) | No (need-aware) | |
| 申请系统 | UC Application | |
| 申请窗口 | Oct 1 - Nov 30 | |
| SAT/ACT 政策 | Test-FREE | |
| TOEFL 最低 | 80 (iBT) / 4.5 (new) | |
| IELTS 最低 | 6.5 | |
| DET 最低 | 115 | |
| 研究生申请费 | $135 (intl) / $120 (domestic) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.sa.ucsb.edu, finaid.ucsb.edu, graddiv.ucsb.edu, catalog.ucsb.edu, www.ucsb.edu
> **Verification**: ego-browser snapshotText + Coursedog API extraction
> **Granularity**: school → department → degree-level → program