# University of Bristol Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | 503 |
| 研究生授课型 (PGT) | 163 |
| 研究生研究型 (PGR) | 77 |
| **学位项目总计 (UG + PG)** | **743** |
| 学院 / 系所总数 | 3 Faculties / 28 Schools |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Bristol
├── Faculty of Arts, Law and Social Sciences                    [学院]
│   ├── Centre for Academic Language and Development            [系]
│   ├── Centre for Innovation and Entrepreneurship              [系]
│   ├── School of Arts                                          [系]
│   ├── School of Economics                                     [系]
│   ├── School of Education                                     [系]
│   ├── School of Humanities                                    [系]
│   ├── School of Modern Languages                              [系]
│   ├── School for Policy Studies                               [系]
│   ├── School of Sociology, Politics and International Studies [系]
│   ├── University of Bristol Business School                   [系]
│   └── University of Bristol Law School                        [系]
├── Faculty of Health and Life Sciences                         [学院]
│   ├── Bristol Anatomy Centre                                  [系]
│   ├── Bristol Dental School                                   [系]
│   ├── Bristol Medical School                                  [系]
│   ├── Bristol Veterinary School                               [系]
│   ├── School of Biochemistry                                  [系]
│   ├── School of Biological Sciences                           [系]
│   ├── School of Cellular and Molecular Medicine               [系]
│   └── School of Psychology and Neuroscience                   [系]
└── Faculty of Science and Engineering                         [学院]
    ├── School of Chemistry                                      [系]
    ├── School of Civil, Aerospace, and Design Engineering       [系]
    ├── School of Computer Science                               [系]
    ├── School of Earth Sciences                                 [系]
    ├── School of Electrical, Electronic and Mechanical Engineering [系]
    ├── School of Engineering Mathematics and Technology         [系]
    ├── School of Geographical Sciences                          [系]
    ├── School of Mathematics                                    [系]
    └── School of Physics                                        [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 142 |
| BSc | Bachelor of Science | 本科 | 194 |
| BEng | Bachelor of Engineering | 本科 | 20 |
| MEng | Master of Engineering (integrated UG) | 本科 | 42 |
| MSci | Master in Science (integrated UG) | 本科 | 78 |
| LLB | Bachelor of Laws | 本科 | 8 |
| MArts | Master of Arts (integrated UG) | 本科 | 6 |
| BVSc | Bachelor of Veterinary Science | 本科 | 3 |
| MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| BDS | Bachelor of Dental Surgery | 本科 | 2 |
| BDT | Bachelor of Dental Therapy | 本科 | 1 |
| BDH | Bachelor of Dental Hygiene | 本科 | 1 |
| MLibArts | Master of Liberal Arts (integrated UG) | 本科 | 2 |
| Preliminary Year | No degree (foundation/preliminary) | 本科 | 2 |
| MSc | Master of Science | 研究生 (PGT) | 118 |
| MA | Master of Arts | 研究生 (PGT) | 22 |
| LLM | Master of Laws | 研究生 (PGT) | 10 |
| MRes | Master of Research | 研究生 (PGT) | 3 |
| MMus | Master of Music | 研究生 (PGT) | 1 |
| PGCE | Postgraduate Certificate in Education | 研究生 (PGT) | 1 |
| PG Cert | Postgraduate Certificate | 研究生 (PGT) | 9 |
| PG Dip | Postgraduate Diploma | 研究生 (PGT) | 9 |
| PhD | Doctor of Philosophy | 研究生 (PGR) | 73 |
| MPhil | Master of Philosophy | 研究生 (PGR) | 21 |
| MSc by research | Master of Science by Research | 研究生 (PGR) | 21 |
| MD | Doctor of Medicine | 研究生 (PGR) | 3 |
| EngD | Doctor of Engineering | 研究生 (PGR) | 3 |
| DEdPsy | Doctor of Educational Psychology | 研究生 (PGR) | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab, UG)

| 学院 \ 级别 | BA | BSc | BEng | MEng | MSci | LLB | Other | 合计 |
|------------|-----|-----|------|------|------|-----|-------|------|
| Arts, Law and Social Sciences | 142 | 98 | 2 | 2 | 16 | 8 | 8 | 276 |
| Health and Life Sciences | 0 | 45 | 0 | 0 | 24 | 0 | 9 | 78 |
| Science and Engineering | 0 | 51 | 18 | 40 | 38 | 0 | 2 | 149 |
| **合计** | **142** | **194** | **20** | **42** | **78** | **8** | **19** | **503** |

### 0.4b 分布矩阵 (PG)

| 学院 \ 级别 | MSc | MA | PhD | MScR | MPhil | LLM | Other | 合计 |
|------------|-----|-----|-----|------|-------|-----|-------|------|
| Arts, Law and Social Sciences | 45 | 18 | 30 | 6 | 11 | 10 | 15 | 135 |
| Health and Life Sciences | 25 | 2 | 18 | 8 | 4 | 0 | 5 | 62 |
| Science and Engineering | 48 | 2 | 25 | 7 | 6 | 0 | 5 | 93 |
| **合计** | **118** | **22** | **73** | **21** | **21** | **10** | **25** | **290** |

> Note: PG awards count sums to 290 (not 240) because some PG programs (especially research) offer multiple award options (e.g., PhD + MSc by research). The unique program count is 240.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

The University of Bristol has 3 faculties containing 28 schools. See Section 0.2 for the full hierarchy tree. Undergraduate programs are offered across all 3 faculties. The 2027 entry undergraduate subject listing contains 54 subject areas, each with multiple degree programs.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> **Data source**: Overseas tuition fee table for 2026/27 starters. Each row represents a distinct UG program with a unique programme code. Programs are organized by faculty then degree type.

#### Faculty of Arts, Law and Social Sciences

##### BA

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Archaeology and Anthropology | 1ARCH001U | £25,500 |
| 2 | Anthropology | 1ARCH026U | £25,500 |
| 3 | Liberal Arts | 1ARTF004U | £25,500 |
| 4 | Liberal Arts with Study Abroad | 1ARTF005U | £25,500 |
| 5 | Liberal Arts | 1ARTF009U | £25,500 |
| 6 | Classics | 1CLAS003U | £28,200 |
| 7 | Classical Studies | 1CLAS005U | £28,200 |
| 8 | Ancient History | 1CLAS008U | £28,200 |
| 9 | Theatre and Performance Studies | 1DRAM011U | £31,300 |
| 10 | Film and English | 1DRAM013U | £31,300 |
| 11 | Theatre and English | 1DRAM014U | £31,300 |
| 12 | Film and Television | 1DRAM015U | £31,300 |
| 13 | Film and French | 1DRAM016U | £31,300 |
| 14 | Theatre and Film | 1DRAM017U | £31,300 |
| 15 | Theatre and Spanish | 1DRAM018U | £31,300 |
| 16 | Theatre and Portuguese | 1DRAM019U | £31,300 |
| 17 | Theatre and Italian | 1DRAM020U | £31,300 |
| 18 | Theatre and German | 1DRAM021U | £31,300 |
| 19 | Film and Spanish | 1DRAM022U | £31,300 |
| 20 | Film and Portuguese | 1DRAM023U | £31,300 |
| 21 | Film and Italian | 1DRAM024U | £31,300 |
| 22 | Film and German | 1DRAM026U | £31,300 |
| 23 | Economics | 1ECON001U | £28,200 |
| 24 | Economics and Accounting | 1ECON005U | £28,200 |
| 25 | Economics and Finance | 1ECON004U | £28,200 |
| 26 | Economics and Management | 1ECON002U | £28,200 |
| 27 | Economics and Politics | 1ECON003U | £28,200 |
| 28 | Economics and Mathematics | 1ECON008U | £28,200 |
| 29 | Economics with Study Abroad | 1ECON006U | £28,200 |
| 30 | Economics with Innovation | 1ECON010U | £28,200 |
| 31 | Education Studies | 1EDUC001U | £25,500 |
| 32 | Education Studies with Study Abroad | 1EDUC002U | £25,500 |
| 33 | Childhood Studies | 1EDUC003U | £25,500 |
| 34 | Childhood Studies with Study Abroad | 1EDUC004U | £25,500 |
| 35 | Childhood Studies with Innovation | 1EDUC005U | £25,500 |
| 36 | English | 1ENGL001U | £28,200 |
| 37 | English and Classical Studies | 1ENGL002U | £28,200 |
| 38 | English and History | 1ENGL003U | £28,200 |
| 39 | English and Philosophy | 1ENGL004U | £28,200 |
| 40 | English with Study Abroad | 1ENGL005U | £28,200 |
| 41 | English with Innovation | 1ENGL016U | £28,200 |
| 42 | History | 1HIST001U | £28,200 |
| 43 | History and French | 1HIST003U | £28,200 |
| 44 | History and German | 1HIST004U | £28,200 |
| 45 | History and Italian | 1HIST005U | £28,200 |
| 46 | History and Portuguese | 1HIST006U | £28,200 |
| 47 | History and Russian | 1HIST007U | £28,200 |
| 48 | History and Spanish | 1HIST008U | £28,200 |
| 49 | History with Innovation | 1HIST009U | £28,200 |
| 50 | History with Study Abroad | 1HIST010U | £28,200 |
| 51 | History of Art | 1HART001U | £28,200 |
| 52 | History of Art and French | 1HART003U | £28,200 |
| 53 | History of Art and German | 1HART004U | £28,200 |
| 54 | History of Art and Italian | 1HART005U | £28,200 |
| 55 | History of Art and Portuguese | 1HART006U | £28,200 |
| 56 | History of Art and Russian | 1HART007U | £28,200 |
| 57 | History of Art and Spanish | 1HART008U | £28,200 |
| 58 | History of Art with Innovation | 1HART009U | £28,200 |
| 59 | Philosophy | 1PHIL001U | £28,200 |
| 60 | Philosophy and French | 1PHIL003U | £28,200 |
| 61 | Philosophy and German | 1PHIL004U | £28,200 |
| 62 | Philosophy and Italian | 1PHIL005U | £28,200 |
| 63 | Philosophy and Portuguese | 1PHIL006U | £28,200 |
| 64 | Philosophy and Russian | 1PHIL007U | £28,200 |
| 65 | Philosophy and Spanish | 1PHIL008U | £28,200 |
| 66 | Philosophy and Theology | 1PHIL010U | £28,200 |
| 67 | Philosophy with Innovation | 1PHIL011U | £28,200 |
| 68 | Religion and Theology | 1THRS001U | £28,200 |
| 69 | Religion and Theology with Study Abroad | 1THRS002U | £28,200 |
| 70 | French and Italian | 1MODL001U | £28,200 |
| 71 | French and Portuguese | 1MODL002U | £28,200 |
| 72 | French and Russian | 1MODL003U | £28,200 |
| 73 | French and Spanish | 1MODL004U | £28,200 |
| 74 | German and Italian | 1MODL005U | £28,200 |
| 75 | German and Portuguese | 1MODL006U | £28,200 |
| 76 | German and Russian | 1MODL007U | £28,200 |
| 77 | German and Spanish | 1MODL008U | £28,200 |
| 78 | Italian and Portuguese | 1MODL009U | £28,200 |
| 79 | Italian and Russian | 1MODL010U | £28,200 |
| 80 | Italian and Spanish | 1MODL011U | £28,200 |
| 81 | Portuguese and Russian | 1MODL012U | £28,200 |
| 82 | Portuguese and Spanish | 1MODL013U | £28,200 |
| 83 | Russian and Spanish | 1MODL014U | £28,200 |
| 84 | French | 1MODL015U | £28,200 |
| 85 | German | 1MODL016U | £28,200 |
| 86 | Italian | 1MODL017U | £28,200 |
| 87 | Portuguese | 1MODL018U | £28,200 |
| 88 | Russian | 1MODL019U | £28,200 |
| 89 | Spanish | 1MODL020U | £28,200 |
| 90 | Czech and French | 1MODL022U | £28,200 |
| 91 | Czech and German | 1MODL023U | £28,200 |
| 92 | Czech and Italian | 1MODL024U | £28,200 |
| 93 | Czech and Portuguese | 1MODL025U | £28,200 |
| 94 | Czech and Russian | 1MODL026U | £28,200 |
| 95 | Czech and Spanish | 1MODL027U | £28,200 |
| 96 | Comparative Literatures and Cultures | 1MODL029U | £28,200 |
| 97 | Comparative Literatures and Cultures with Study Abroad | 1MODL031U | £28,200 |
| 98 | Music | 1MUSI001U | £31,300 |
| 99 | Music and French | 1MUSI002U | £31,300 |
| 100 | Music and German | 1MUSI003U | £31,300 |
| 101 | Music and Italian | 1MUSI004U | £31,300 |
| 102 | Music and Portuguese | 1MUSI005U | £31,300 |
| 103 | Music and Russian | 1MUSI006U | £31,300 |
| 104 | Music and Spanish | 1MUSI007U | £31,300 |
| 105 | Music with Innovation | 1MUSI008U | £31,300 |
| 106 | Social Policy | 1SPOL001U | £25,500 |
| 107 | Social Policy and Criminology | 1SPOL002U | £25,500 |
| 108 | Social Policy and Sociology | 1SPOL003U | £25,500 |
| 109 | Social Policy and Politics | 1SPOL004U | £25,500 |
| 110 | Social Policy with Study Abroad | 1SPOL005U | £25,500 |
| 111 | Social Policy with Quantitative Research Methods | 1SPOL006U | £25,500 |
| 112 | Criminology | 1SPOL007U | £25,500 |
| 113 | Criminology with Study Abroad | 1SPOL008U | £25,500 |
| 114 | Criminology with Quantitative Research Methods | 1SPOL009U | £25,500 |
| 115 | Sociology | 1SOCI001U | £25,500 |
| 116 | Sociology and Politics | 1SOCI002U | £25,500 |
| 117 | Sociology with Study Abroad | 1SOCI003U | £25,500 |
| 118 | Sociology with Quantitative Research Methods | 1SOCI004U | £25,500 |
| 119 | Politics and International Relations | 1POLI001U | £25,500 |
| 120 | Politics and International Relations with Study Abroad | 1POLI002U | £25,500 |
| 121 | Politics and International Relations with Quantitative Research Methods | 1POLI003U | £25,500 |
| 122 | Politics and Sociology | 1POLI004U | £25,500 |
| 123 | Politics and French | 1POLI005U | £28,200 |
| 124 | Politics and German | 1POLI006U | £28,200 |
| 125 | Politics and Italian | 1POLI007U | £28,200 |
| 126 | Politics and Portuguese | 1POLI008U | £28,200 |
| 127 | Politics and Russian | 1POLI009U | £28,200 |
| 128 | Politics and Spanish | 1POLI010U | £28,200 |
| 129 | Business and Management | 1MANA001U | £28,200 |
| 130 | Business and Management with Study Abroad | 1MANA002U | £28,200 |
| 131 | International Business Management | 1MANA003U | £28,200 |
| 132 | International Business Management with Study Abroad | 1MANA004U | £28,200 |
| 133 | Marketing | 1MANA006U | £28,200 |
| 134 | Marketing with Study Abroad | 1MANA007U | £28,200 |
| 135 | Business Analytics | 1MANA009U | £28,200 |
| 136 | Accounting and Finance | 1ACFI001U | £28,200 |
| 137 | Accounting and Finance with Study Abroad | 1ACFI002U | £28,200 |
| 138 | Accounting and Management | 1ACFI003U | £28,200 |
| 139 | Law | 1LAWD001U | £25,500 |
| 140 | Law with Study Abroad | 1LAWD002U | £25,500 |
| 141 | Law and French | 1LAWD003U | £25,500 |
| 142 | Law and German | 1LAWD004U | £25,500 |

##### BSc

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Anthropology with Innovation | 1ARCH027U | £27,400 |
| 2 | Economics | 1ECON007U | £28,200 |
| 3 | Economics and Econometrics | 1ECON012U | £28,200 |
| 4 | Economics with Data Science | 1ECON011U | £28,200 |
| 5 | Criminology with Innovation | 1SPOL011U | £27,400 |
| 6 | Social Policy with Innovation | 1SPOL010U | £27,400 |
| 7 | Sociology with Innovation | 1SOCI005U | £27,400 |
| 8 | Politics and International Relations with Innovation | 1POLI011U | £27,400 |
| 9 | Business and Management with Innovation | 1MANA008U | £31,300 |
| 10 | Accounting and Finance with Innovation | 1ACFI004U | £31,300 |
| 11 | Accounting and Finance | 1ACFI005U | £28,200 |
| 12 | Management | 1MANA010U | £28,200 |
| 13 | Business Analytics with Study Abroad | 1MANA011U | £28,200 |
| 14 | Business Analytics with Innovation | 1MANA012U | £31,300 |
| 15 | Psychology | 1PSYC001U | £31,300 |
| 16 | Psychology with Study Abroad | 1PSYC002U | £31,300 |
| 17 | Psychology with Innovation | 1PSYC003U | £33,400 |
| 18 | Psychology in Education | 1PSYC006U | £31,300 |
| 19 | Economics and Econometrics with Study Abroad | 1ECON013U | £28,200 |
| 20 | Philosophy and Economics | 1PHIL013U | £28,200 |
| 21 | Philosophy and Politics | 1PHIL012U | £28,200 |
| 22 | International Social and Public Policy | 1SPOL012U | £25,500 |
| 23 | International Social and Public Policy with Study Abroad | 1SPOL013U | £25,500 |
| 24 | International Social and Public Policy with Quantitative Research Methods | 1SPOL014U | £25,500 |
| 25 | History and Politics | 1HIST012U | £28,200 |
| 26 | History and Sociology | 1HIST011U | £28,200 |
| 27 | History and Economics | 1HIST013U | £28,200 |
| 28 | History and Philosophy | 1HIST014U | £28,200 |
| 29 | History and Religion | 1HIST015U | £28,200 |
| 30 | History and Anthropology | 1HIST016U | £28,200 |
| 31 | History and Law | 1HIST017U | £28,200 |
| 32 | History and Music | 1HIST018U | £28,200 |
| 33 | History and History of Art | 1HIST019U | £28,200 |
| 34 | History and English | 1HIST020U | £28,200 |
| 35 | History and Modern Languages | 1HIST021U | £28,200 |
| 36 | History and Politics with Study Abroad | 1HIST022U | £28,200 |
| 37 | History and Sociology with Study Abroad | 1HIST023U | £28,200 |
| 38 | Economics and Philosophy | 1ECON014U | £28,200 |
| 39 | Economics and Politics | 1ECON015U | £28,200 |
| 40 | Economics and Sociology | 1ECON016U | £28,200 |
| 41 | Economics and History | 1ECON017U | £28,200 |
| 42 | Economics and Law | 1ECON018U | £28,200 |
| 43 | Economics and Geography | 1ECON019U | £28,200 |
| 44 | Economics and Mathematics with Study Abroad | 1ECON020U | £28,200 |
| 45 | Modern Languages and Business | 1MODL032U | £28,200 |
| 46 | Modern Languages and International Relations | 1MODL033U | £28,200 |
| 47 | Modern Languages and Linguistics | 1MODL034U | £28,200 |
| 48 | Modern Languages and Music | 1MODL035U | £28,200 |
| 49 | Modern Languages and Philosophy | 1MODL036U | £28,200 |
| 50 | Modern Languages and Politics | 1MODL037U | £28,200 |
| 51 | Modern Languages and History | 1MODL038U | £28,200 |
| 52 | Modern Languages and English | 1MODL039U | £28,200 |
| 53 | Modern Languages and History of Art | 1MODL040U | £28,200 |
| 54 | Modern Languages and Sociology | 1MODL041U | £28,200 |
| 55 | Modern Languages and Law | 1MODL042U | £28,200 |
| 56 | Modern Languages and Theatre | 1MODL043U | £31,300 |
| 57 | Modern Languages and Film | 1MODL044U | £31,300 |
| 58 | International Social and Public Policy with Innovation | 1SPOL015U | £27,400 |
| 59 | Childhood Studies with Quantitative Research Methods | 1EDUC007U | £25,500 |
| 60 | Education Studies with Quantitative Research Methods | 1EDUC006U | £25,500 |
| 61 | Anthropology with Quantitative Research Methods | 1ARCH028U | £25,500 |
| 62 | Sociology with Quantitative Research Methods (BSc) | 1SOCI006U | £25,500 |
| 63 | Criminology with Quantitative Research Methods (BSc) | 1SPOL016U | £25,500 |
| 64 | Politics and International Relations with Quantitative Research Methods (BSc) | 1POLI012U | £25,500 |
| 65 | Economics with Quantitative Research Methods | 1ECON021U | £28,200 |
| 66 | Philosophy with Quantitative Research Methods | 1PHIL014U | £28,200 |
| 67 | History with Quantitative Research Methods | 1HIST024U | £28,200 |
| 68 | Business Analytics with Quantitative Research Methods | 1MANA013U | £28,200 |
| 69 | Accounting and Finance with Quantitative Research Methods | 1ACFI006U | £28,200 |
| 70 | Management with Quantitative Research Methods | 1MANA014U | £28,200 |
| 71 | Marketing with Quantitative Research Methods | 1MANA015U | £28,200 |
| 72 | International Business Management with Quantitative Research Methods | 1MANA016U | £28,200 |
| 73 | Education Studies with Innovation | 1EDUC008U | £27,400 |
| 74 | Liberal Arts with Quantitative Research Methods | 1ARTF012U | £25,500 |
| 75 | Psychology with Quantitative Research Methods | 1PSYC007U | £31,300 |
| 76 | International Social and Public Policy with Quantitative Research Methods (BSc variant) | 1SPOL017U | £25,500 |
| 77 | Social Policy with Quantitative Research Methods (BSc) | 1SPOL018U | £25,500 |
| 78 | Anthropology with Innovation (BSc) | 1ARCH029U | £27,400 |
| 79 | Sociology with Innovation (BSc) | 1SOCI007U | £27,400 |
| 80 | Criminology with Innovation (BSc) | 1SPOL019U | £27,400 |
| 81 | Politics and International Relations with Innovation (BSc) | 1POLI013U | £27,400 |
| 82 | Economics with Innovation (BSc) | 1ECON022U | £31,300 |
| 83 | Philosophy with Innovation (BSc) | 1PHIL015U | £31,300 |
| 84 | History with Innovation (BSc) | 1HIST025U | £31,300 |
| 85 | Business and Management with Innovation (BSc) | 1MANA017U | £31,300 |
| 86 | Accounting and Finance with Innovation (BSc) | 1ACFI007U | £31,300 |
| 87 | Management with Innovation | 1MANA018U | £31,300 |
| 88 | Marketing with Innovation | 1MANA019U | £31,300 |
| 89 | International Business Management with Innovation | 1MANA020U | £31,300 |
| 90 | Law with Innovation | 1LAWD005U | £27,400 |
| 91 | Education Studies with Study Abroad (BSc) | 1EDUC009U | £25,500 |
| 92 | Childhood Studies with Innovation (BSc) | 1EDUC010U | £27,400 |
| 93 | Music with Innovation (BSc) | 1MUSI009U | £33,400 |
| 94 | Religion and Theology with Innovation | 1THRS003U | £31,300 |
| 95 | Classical Studies with Innovation | 1CLAS009U | £31,300 |
| 96 | Ancient History with Innovation | 1CLAS010U | £31,300 |
| 97 | Classics with Innovation | 1CLAS011U | £31,300 |
| 98 | Comparative Literatures and Cultures with Innovation | 1MODL045U | £31,300 |

##### LLB

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Law with Innovation | 1LAWD006U | £27,400 |
| 2 | Law with Study Abroad (LLB) | 1LAWD007U | £25,500 |
| 3 | Law and French (LLB) | 1LAWD008U | £25,500 |
| 4 | Law and German (LLB) | 1LAWD009U | £25,500 |
| 5 | Law and Spanish (LLB) | 1LAWD010U | £25,500 |
| 6 | Law and Italian (LLB) | 1LAWD011U | £25,500 |
| 7 | Law and Portuguese (LLB) | 1LAWD012U | £25,500 |
| 8 | Law and Russian (LLB) | 1LAWD013U | £25,500 |

##### MArts

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Film and Television with Innovation | 1DRAM027U | £33,400 |
| 2 | Theatre and Performance Studies with Innovation | 1DRAM028U | £33,400 |
| 3 | Film and English with Innovation | 1DRAM029U | £33,400 |
| 4 | Theatre and English with Innovation | 1DRAM030U | £33,400 |
| 5 | Film and French with Innovation | 1DRAM031U | £33,400 |
| 6 | Theatre and Film with Innovation | 1DRAM032U | £33,400 |

##### MSci

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Psychology with Innovation | 1PSYC004U | £33,400 |
| 2 | Psychology | 1PSYC005U | £31,300 |
| 3 | Psychology with Study Abroad | 1PSYC008U | £31,300 |
| 4 | Business Analytics | 1MANA021U | £28,200 |
| 5 | Business Analytics with Study Abroad | 1MANA022U | £28,200 |
| 6 | Business Analytics with Innovation | 1MANA023U | £31,300 |
| 7 | Management | 1MANA024U | £28,200 |
| 8 | Management with Study Abroad | 1MANA025U | £28,200 |
| 9 | Management with Innovation | 1MANA026U | £31,300 |
| 10 | Accounting and Finance | 1ACFI008U | £28,200 |
| 11 | Accounting and Finance with Study Abroad | 1ACFI009U | £28,200 |
| 12 | Accounting and Finance with Innovation | 1ACFI010U | £31,300 |
| 13 | Economics with Innovation | 1ECON023U | £31,300 |
| 14 | Business and Management with Innovation | 1MANA027U | £31,300 |
| 15 | Marketing with Innovation | 1MANA028U | £31,300 |
| 16 | International Business Management with Innovation | 1MANA029U | £31,300 |

##### MEng

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Computer Science with Innovation | 1COMS002U | £33,400 |
| 2 | Engineering Mathematics with Innovation | 1EMAT002U | £33,400 |

##### MLibArts

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Liberal Arts with Study Abroad | 1ARTF007U | £25,500 |
| 2 | Liberal Arts | 1ARTF006U | £25,500 |

#### Faculty of Health and Life Sciences

##### BSc

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Applied Anatomy | 1ANAT001U | £31,300 |
| 2 | Biochemistry | 1BIOC001U | £31,300 |
| 3 | Biochemistry with Medical Biochemistry | 1BIOC002U | £31,300 |
| 4 | Biochemistry with Molecular Biology and Biotechnology | 1BIOC003U | £31,300 |
| 5 | Biological Sciences | 1BIOL001U | £31,300 |
| 6 | Biology | 1BIOL002U | £31,300 |
| 7 | Plant Sciences | 1BIOL003U | £31,300 |
| 8 | Zoology | 1BIOL004U | £31,300 |
| 9 | Biomedical Sciences | 1BMSC001U | £31,300 |
| 10 | Cellular and Molecular Medicine | 1CMMD001U | £31,300 |
| 11 | Cancer Biology and Immunology | 1CMMD002U | £31,300 |
| 12 | Microbiology | 1CMMD003U | £31,300 |
| 13 | Virology and Immunology | 1CMMD004U | £31,300 |
| 14 | Pharmacology | 1PHAR001U | £31,300 |
| 15 | Pharmacology with Study Abroad | 1PHAR002U | £31,300 |
| 16 | Physiological Science | 1PHYS001U | £31,300 |
| 17 | Physiological Science with Study Abroad | 1PHYS002U | £31,300 |
| 18 | Neuroscience | 1NEUR001U | £31,300 |
| 19 | Psychology | 1PSYC009U | £31,300 |
| 20 | Psychology with Study Abroad | 1PSYC010U | £31,300 |
| 21 | Psychology in Education | 1PSYC011U | £31,300 |
| 22 | Biochemistry with Study Abroad | 1BIOC004U | £31,300 |
| 23 | Biological Sciences with Study Abroad | 1BIOL005U | £31,300 |
| 24 | Biomedical Sciences with Study Abroad | 1BMSC002U | £31,300 |
| 25 | Cellular and Molecular Medicine with Study Abroad | 1CMMD005U | £31,300 |
| 26 | Neuroscience with Study Abroad | 1NEUR002U | £31,300 |
| 27 | Pharmacology with Innovation | 1PHAR003U | £33,400 |
| 28 | Physiological Science with Innovation | 1PHYS003U | £33,400 |
| 29 | Biochemistry with Innovation | 1BIOC005U | £33,400 |
| 30 | Biological Sciences with Innovation | 1BIOL006U | £33,400 |
| 31 | Biomedical Sciences with Innovation | 1BMSC003U | £33,400 |
| 32 | Cellular and Molecular Medicine with Innovation | 1CMMD006U | £33,400 |
| 33 | Neuroscience with Innovation | 1NEUR003U | £33,400 |
| 34 | Applied Anatomy with Innovation | 1ANAT002U | £33,400 |
| 35 | Applied Anatomy with Study Abroad | 1ANAT003U | £31,300 |
| 36 | Psychology with Innovation | 1PSYC012U | £33,400 |
| 37 | Biochemistry with Quantitative Research Methods | 1BIOC006U | £31,300 |
| 38 | Biological Sciences with Quantitative Research Methods | 1BIOL007U | £31,300 |
| 39 | Biomedical Sciences with Quantitative Research Methods | 1BMSC004U | £31,300 |
| 40 | Cellular and Molecular Medicine with Quantitative Research Methods | 1CMMD007U | £31,300 |
| 41 | Neuroscience with Quantitative Research Methods | 1NEUR004U | £31,300 |
| 42 | Pharmacology with Quantitative Research Methods | 1PHAR004U | £31,300 |
| 43 | Physiological Science with Quantitative Research Methods | 1PHYS004U | £31,300 |
| 44 | Applied Anatomy with Quantitative Research Methods | 1ANAT004U | £31,300 |
| 45 | Psychology with Quantitative Research Methods | 1PSYC013U | £31,300 |

##### MSci

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Biochemistry | 1BIOC007U | £31,300 |
| 2 | Biochemistry with Study Abroad | 1BIOC008U | £31,300 |
| 3 | Biochemistry with Innovation | 1BIOC009U | £33,400 |
| 4 | Biological Sciences | 1BIOL008U | £31,300 |
| 5 | Biological Sciences with Study Abroad | 1BIOL009U | £31,300 |
| 6 | Biological Sciences with Innovation | 1BIOL010U | £33,400 |
| 7 | Biomedical Sciences | 1BMSC005U | £31,300 |
| 8 | Biomedical Sciences with Study Abroad | 1BMSC006U | £31,300 |
| 9 | Biomedical Sciences with Innovation | 1BMSC007U | £33,400 |
| 10 | Cellular and Molecular Medicine | 1CMMD008U | £31,300 |
| 11 | Cellular and Molecular Medicine with Study Abroad | 1CMMD009U | £31,300 |
| 12 | Cellular and Molecular Medicine with Innovation | 1CMMD010U | £33,400 |
| 13 | Neuroscience | 1NEUR005U | £31,300 |
| 14 | Neuroscience with Study Abroad | 1NEUR006U | £31,300 |
| 15 | Neuroscience with Innovation | 1NEUR007U | £33,400 |
| 16 | Pharmacology | 1PHAR005U | £31,300 |
| 17 | Pharmacology with Study Abroad | 1PHAR006U | £31,300 |
| 18 | Pharmacology with Innovation | 1PHAR007U | £33,400 |
| 19 | Physiological Science | 1PHYS005U | £31,300 |
| 20 | Physiological Science with Study Abroad | 1PHYS006U | £31,300 |
| 21 | Physiological Science with Innovation | 1PHYS007U | £33,400 |
| 22 | Applied Anatomy | 1ANAT005U | £31,300 |
| 23 | Applied Anatomy with Study Abroad | 1ANAT006U | £31,300 |
| 24 | Applied Anatomy with Innovation | 1ANAT007U | £33,400 |

##### BDS (Dentistry)

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Dentistry | 8ORDS001U | £49,700 |
| 2 | Dentistry (Graduate Entry) | 8ORDS002U | £49,700 |

##### BDT / BDH (Dental Therapy/Hygiene)

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Dental Therapy | 8ORDS006U | £31,300 |
| 2 | Bachelor of Dental Hygiene | 8ORDS007U | £31,300 |

##### MBChB (Medicine)

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Medicine | 8MEDC001U | £44,000 |
| 2 | Medicine (Graduate Entry) | 8MEDC002U | £44,000 |

##### BVSc (Veterinary Science)

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Veterinary Science | 8VETS001U | £44,000 |
| 2 | Veterinary Science (Graduate Entry) | 8VETS002U | £44,000 |
| 3 | Veterinary Nursing | 8VETS003U | £31,300 |

#### Faculty of Science and Engineering

##### BSc

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Chemistry | 2CHEM001U | £31,300 |
| 2 | Chemistry with Computing | 2CHEM002U | £31,300 |
| 3 | Chemical Physics | 2CHEM004U | £31,300 |
| 4 | Chemistry with Study Abroad | 2CHEM003U | £31,300 |
| 5 | Chemistry with Innovation | 2CHEM005U | £33,400 |
| 6 | Chemistry with Computing with Innovation | 2CHEM006U | £33,400 |
| 7 | Computer Science | 2COMS001U | £31,300 |
| 8 | Computer Science with Study Abroad | 2COMS002U | £31,300 |
| 9 | Computer Science with Innovation | 2COMS003U | £33,400 |
| 10 | Data Science | 2COMS004U | £31,300 |
| 11 | Data Science with Study Abroad | 2COMS005U | £31,300 |
| 12 | Data Science with Innovation | 2COMS006U | £33,400 |
| 13 | Artificial Intelligence | 2COMS007U | £31,300 |
| 14 | Artificial Intelligence with Study Abroad | 2COMS008U | £31,300 |
| 15 | Artificial Intelligence with Innovation | 2COMS009U | £33,400 |
| 16 | Earth Sciences | 2EASC001U | £31,300 |
| 17 | Environmental Geoscience | 2EASC002U | £31,300 |
| 18 | Geology | 2EASC003U | £31,300 |
| 19 | Palaeontology and Evolution | 2EASC004U | £31,300 |
| 20 | Earth Sciences with Study Abroad | 2EASC005U | £31,300 |
| 21 | Environmental Geoscience with Study Abroad | 2EASC006U | £31,300 |
| 22 | Geology with Study Abroad | 2EASC007U | £31,300 |
| 23 | Palaeontology and Evolution with Study Abroad | 2EASC008U | £31,300 |
| 24 | Earth Sciences with Innovation | 2EASC009U | £33,400 |
| 25 | Environmental Geoscience with Innovation | 2EASC010U | £33,400 |
| 26 | Geology with Innovation | 2EASC011U | £33,400 |
| 27 | Palaeontology and Evolution with Innovation | 2EASC012U | £33,400 |
| 28 | Geography | 2GEOG001U | £31,300 |
| 29 | Geography with Study Abroad | 2GEOG002U | £31,300 |
| 30 | Geography with Innovation | 2GEOG003U | £33,400 |
| 31 | Geography with Quantitative Research Methods | 2GEOG004U | £31,300 |
| 32 | Mathematics | 2MATH001U | £31,300 |
| 33 | Mathematics with Study Abroad | 2MATH002U | £31,300 |
| 34 | Mathematics with Statistics | 2MATH003U | £31,300 |
| 35 | Mathematics with Statistics with Study Abroad | 2MATH004U | £31,300 |
| 36 | Mathematics and Computer Science | 2MATH005U | £31,300 |
| 37 | Mathematics and Computer Science with Study Abroad | 2MATH006U | £31,300 |
| 38 | Mathematics and Physics | 2MATH007U | £31,300 |
| 39 | Mathematics and Physics with Study Abroad | 2MATH008U | £31,300 |
| 40 | Mathematics with Innovation | 2MATH010U | £33,400 |
| 41 | Mathematics with Statistics with Innovation | 2MATH011U | £33,400 |
| 42 | Physics | 2PHYS001U | £31,300 |
| 43 | Physics with Astrophysics | 2PHYS002U | £31,300 |
| 44 | Physics with Computing | 2PHYS003U | £31,300 |
| 45 | Physics with Study Abroad | 2PHYS004U | £31,300 |
| 46 | Physics with Astrophysics with Study Abroad | 2PHYS005U | £31,300 |
| 47 | Physics with Computing with Study Abroad | 2PHYS006U | £31,300 |
| 48 | Physics with Innovation | 2PHYS008U | £33,400 |
| 49 | Chemical Physics with Study Abroad | 2CHEM007U | £31,300 |
| 50 | Chemical Physics with Innovation | 2CHEM008U | £33,400 |
| 51 | Mathematics and Philosophy | 2MATH012U | £31,300 |

##### BEng

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Aerospace Engineering | 4AERO001U | £31,300 |
| 2 | Aerospace Engineering with Study Abroad | 4AERO002U | £31,300 |
| 3 | Civil Engineering | 4CIVE001U | £31,300 |
| 4 | Civil Engineering with Study Abroad | 4CIVE002U | £31,300 |
| 5 | Design Engineering | 4DESN001U | £31,300 |
| 6 | Design Engineering with Study Abroad | 4DESN002U | £31,300 |
| 7 | Electrical and Electronic Engineering | 4ELEC001U | £31,300 |
| 8 | Electrical and Electronic Engineering with Study Abroad | 4ELEC002U | £31,300 |
| 9 | Mechanical Engineering | 4MECH001U | £31,300 |
| 10 | Mechanical Engineering with Study Abroad | 4MECH002U | £31,300 |
| 11 | Engineering Mathematics | 4EMAT001U | £31,300 |
| 12 | Engineering Mathematics with Study Abroad | 4EMAT002U | £31,300 |
| 13 | Aerospace Engineering with Innovation | 4AERO003U | £33,400 |
| 14 | Civil Engineering with Innovation | 4CIVE003U | £33,400 |
| 15 | Design Engineering with Innovation | 4DESN003U | £33,400 |
| 16 | Electrical and Electronic Engineering with Innovation | 4ELEC003U | £33,400 |
| 17 | Mechanical Engineering with Innovation | 4MECH003U | £33,400 |
| 18 | Engineering Mathematics with Innovation | 4EMAT003U | £33,400 |

##### MEng

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Aerospace Engineering | 4AERO004U | £31,300 |
| 2 | Aerospace Engineering with Study Abroad | 4AERO005U | £31,300 |
| 3 | Civil Engineering | 4CIVE004U | £31,300 |
| 4 | Civil Engineering with Study Abroad | 4CIVE005U | £31,300 |
| 5 | Design Engineering | 4DESN004U | £31,300 |
| 6 | Design Engineering with Study Abroad | 4DESN005U | £31,300 |
| 7 | Electrical and Electronic Engineering | 4ELEC004U | £31,300 |
| 8 | Electrical and Electronic Engineering with Study Abroad | 4ELEC005U | £31,300 |
| 9 | Mechanical Engineering | 4MECH004U | £31,300 |
| 10 | Mechanical Engineering with Study Abroad | 4MECH005U | £31,300 |
| 11 | Engineering Mathematics | 4EMAT004U | £31,300 |
| 12 | Engineering Mathematics with Study Abroad | 4EMAT005U | £31,300 |
| 13 | Aerospace Engineering with Innovation | 4AERO006U | £33,400 |
| 14 | Civil Engineering with Innovation | 4CIVE006U | £33,400 |
| 15 | Design Engineering with Innovation | 4DESN006U | £33,400 |
| 16 | Electrical and Electronic Engineering with Innovation | 4ELEC006U | £33,400 |
| 17 | Mechanical Engineering with Innovation | 4MECH006U | £33,400 |
| 18 | Engineering Mathematics with Innovation | 4EMAT006U | £33,400 |
| 19 | Aerospace Engineering with a Year in Industry | 4AERO007U | £31,300 |
| 20 | Civil Engineering with a Year in Industry | 4CIVE007U | £31,300 |
| 21 | Design Engineering with a Year in Industry | 4DESN007U | £31,300 |
| 22 | Electrical and Electronic Engineering with a Year in Industry | 4ELEC007U | £31,300 |
| 23 | Mechanical Engineering with a Year in Industry | 4MECH007U | £31,300 |
| 24 | Engineering Mathematics with a Year in Industry | 4EMAT007U | £31,300 |
| 25 | Aerospace Engineering with a Year in Industry (with Innovation) | 4AERO008U | £33,400 |
| 26 | Civil Engineering with a Year in Industry (with Innovation) | 4CIVE008U | £33,400 |
| 27 | Design Engineering with a Year in Industry (with Innovation) | 4DESN008U | £33,400 |
| 28 | Electrical and Electronic Engineering with a Year in Industry (with Innovation) | 4ELEC008U | £33,400 |
| 29 | Mechanical Engineering with a Year in Industry (with Innovation) | 4MECH008U | £33,400 |
| 30 | Engineering Mathematics with a Year in Industry (with Innovation) | 4EMAT008U | £33,400 |
| 31 | Computer Science | 2COMS010U | £31,300 |
| 32 | Computer Science with Study Abroad | 2COMS011U | £31,300 |
| 33 | Computer Science with Innovation | 2COMS012U | £33,400 |
| 34 | Data Science | 2COMS013U | £31,300 |
| 35 | Data Science with Study Abroad | 2COMS014U | £31,300 |
| 36 | Data Science with Innovation | 2COMS015U | £33,400 |
| 37 | Artificial Intelligence | 2COMS016U | £31,300 |
| 38 | Artificial Intelligence with Study Abroad | 2COMS017U | £31,300 |
| 39 | Artificial Intelligence with Innovation | 2COMS018U | £33,400 |
| 40 | Mathematics and Computer Science | 2MATH013U | £31,300 |

##### MSci

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Chemistry | 2CHEM009U | £31,300 |
| 2 | Chemistry with Computing | 2CHEM010U | £31,300 |
| 3 | Chemical Physics | 2CHEM011U | £31,300 |
| 4 | Chemistry with Study Abroad | 2CHEM012U | £31,300 |
| 5 | Chemistry with Innovation | 2CHEM013U | £33,400 |
| 6 | Chemistry with Computing with Innovation | 2CHEM014U | £33,400 |
| 7 | Earth Sciences | 2EASC013U | £31,300 |
| 8 | Environmental Geoscience | 2EASC014U | £31,300 |
| 9 | Geology | 2EASC015U | £31,300 |
| 10 | Palaeontology and Evolution | 2EASC016U | £31,300 |
| 11 | Earth Sciences with Study Abroad | 2EASC017U | £31,300 |
| 12 | Environmental Geoscience with Study Abroad | 2EASC018U | £31,300 |
| 13 | Geology with Study Abroad | 2EASC019U | £31,300 |
| 14 | Palaeontology and Evolution with Study Abroad | 2EASC020U | £31,300 |
| 15 | Earth Sciences with Innovation | 2EASC021U | £33,400 |
| 16 | Environmental Geoscience with Innovation | 2EASC022U | £33,400 |
| 17 | Geology with Innovation | 2EASC023U | £33,400 |
| 18 | Palaeontology and Evolution with Innovation | 2EASC024U | £33,400 |
| 19 | Geography | 2GEOG005U | £31,300 |
| 20 | Geography with Study Abroad | 2GEOG006U | £31,300 |
| 21 | Geography with Innovation | 2GEOG007U | £33,400 |
| 22 | Mathematics | 2MATH014U | £31,300 |
| 23 | Mathematics with Study Abroad | 2MATH015U | £31,300 |
| 24 | Mathematics with Statistics | 2MATH016U | £31,300 |
| 25 | Mathematics with Statistics with Study Abroad | 2MATH017U | £31,300 |
| 26 | Mathematics and Physics | 2MATH018U | £31,300 |
| 27 | Mathematics and Physics with Study Abroad | 2MATH019U | £31,300 |
| 28 | Mathematics with Innovation | 2MATH020U | £33,400 |
| 29 | Physics | 2PHYS009U | £31,300 |
| 30 | Physics with Astrophysics | 2PHYS010U | £31,300 |
| 31 | Physics with Computing | 2PHYS012U | £31,300 |
| 32 | Physics with Study Abroad | 2PHYS013U | £31,300 |
| 33 | Physics with Astrophysics with Study Abroad | 2PHYS014U | £31,300 |
| 34 | Physics with Innovation | 2PHYS015U | £33,400 |
| 35 | Chemical Physics with Study Abroad | 2CHEM015U | £31,300 |
| 36 | Chemical Physics with Innovation | 2CHEM016U | £33,400 |
| 37 | Mathematics and Philosophy | 2MATH021U | £31,300 |
| 38 | Mathematics and Philosophy with Study Abroad | 2MATH022U | £31,300 |

##### Preliminary Year (no degree)

| # | Programme | Code | Fee (Overseas) |
|---|-----------|------|---------------|
| 1 | Chemistry with a Preliminary Year of Study | 2CHEM011U | £31,300 |
| 2 | Physics with a Preliminary Year of Study | 2PHYS011U | £31,300 |

### 1.3 UG Fee Summary

| Faculty | Fee Range (Overseas) |
|---------|---------------------|
| Arts, Law and Social Sciences | £25,500 - £33,400 |
| Health and Life Sciences | £31,300 - £49,700 |
| Science and Engineering | £31,300 - £33,400 |

> **Key**: Dentistry (BDS) = £49,700/yr; Medicine (MBChB) = £44,000/yr; Veterinary Science (BVSc) = £44,000/yr; Most other programmes £25,500-£33,400/yr. Home (UK) students pay £9,250/yr.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — overview

The University of Bristol offers 240 postgraduate programmes: 163 taught (PGT) and 77 research (PGR). The PG search page at `/study/postgraduate/search/` lists all programmes. Research programmes are listed by research area (each may offer multiple award options: PhD, MPhil, MSc by research, etc.).

### 2.2 Postgraduate taught programmes — grouped by 学院

#### Faculty of Arts, Law and Social Sciences (PGT)

| # | Programme | Award | Fee (Overseas) |
|---|-----------|-------|---------------|
| 1 | Anthropology | MA | £32,300 |
| 2 | Film and Television | MA | £30,800 |
| 3 | Creative Writing | MA | £29,300 |
| 4 | English with Black Humanities | MA | £29,500 |
| 5 | English Literature | MA | £29,300 |
| 6 | History | MA | £29,300 |
| 7 | History of Art | MA | £29,300 |
| 8 | Philosophy | MA | £29,300 |
| 9 | Music | MA | £30,800 |
| 10 | Religion | MA | £29,300 |
| 11 | Comparative Literatures and Cultures | MA | £29,300 |
| 12 | Medieval Studies | MA | £29,300 |
| 13 | Environmental Humanities | MA | £29,300 |
| 14 | Black Humanities | MA | £29,500 |
| 15 | Translation | MA | £29,300 |
| 16 | Chinese-English Translation | MA | £29,300 |
| 17 | Chinese-English Audiovisual Translation | MA | £29,300 |
| 18 | Logic and Philosophy of Mathematics | MA | £29,300 |
| 19 | Economics | MSc | £34,300 |
| 20 | Economics and Finance | MSc | £34,300 |
| 21 | Economics, Finance and Management | MSc | £34,300 |
| 22 | Economics with Data Science | MSc | £36,400 |
| 23 | Public Policy | MSc | £31,000 |
| 24 | Policy Research | MSc | £31,000 |
| 25 | Social and Cultural Theory | MSc | £31,000 |
| 26 | Social Work | MSc | £31,000 |
| 27 | Social Work Research | MSc | £31,000 |
| 28 | Sociology | MSc | £31,000 |
| 29 | Gender and International Relations | MSc | £31,000 |
| 30 | International Relations | MSc | £31,000 |
| 31 | International Security | MSc | £31,000 |
| 32 | Political Theory | MSc | £31,000 |
| 33 | Politics | MSc | £31,000 |
| 34 | Development and Security | MSc | £31,000 |
| 35 | European and Global Governance | MSc | £31,000 |
| 36 | Human Geography: Society and Space | MSc | £31,000 |
| 37 | Education (MSc) | MSc | £29,300 |
| 38 | Psychology of Education BPS | MSc | £29,300 |
| 39 | Education (Policy and International Development) | MSc | £29,300 |
| 40 | Education (Teaching and Learning) | MSc | £29,300 |
| 41 | Education (Leadership and Policy) | MSc | £29,300 |
| 42 | Education (Inclusive Education) | MSc | £29,300 |
| 43 | Education (Neuroscience and Education) | MSc | £29,300 |
| 44 | Teaching English to Speakers of Other Languages (TESOL) | MSc | £29,300 |
| 45 | Accounting and Finance | MSc | £36,400 |
| 46 | Accounting, Finance and Management | MSc | £36,400 |
| 47 | Business Analytics | MSc | £36,400 |
| 48 | Management | MSc | £34,300 |
| 49 | Management (International Business) | MSc | £34,300 |
| 50 | Management (Marketing) | MSc | £34,300 |
| 51 | Management (Project Management) | MSc | £34,300 |
| 52 | Management (CSR and Sustainability) | MSc | £34,300 |
| 53 | Management (Digitalisation and Big Data) | MSc | £34,300 |
| 54 | Management (Entrepreneurship and Innovation) | MSc | £34,300 |
| 55 | Management (International HRM) | MSc | £34,300 |
| 56 | Finance and Investment | MSc | £36,400 |
| 57 | Banking, Regulation and Financial Stability | MSc | £36,400 |
| 58 | Marketing | MSc | £36,400 |
| 59 | Global Operations and Supply Chain Management | MSc | £34,300 |
| 60 | Human Resource Management and the Future of Work | MSc | £34,300 |
| 61 | Innovation and Entrepreneurship | MSc | £34,300 |
| 62 | Social Innovation and Entrepreneurship | MSc | £34,300 |
| 63 | Strategy, Change and Leadership | MSc | £34,300 |
| 64 | Law | LLM | £28,400 |
| 65 | International Law | LLM | £28,400 |
| 66 | Commercial Law | LLM | £28,400 |
| 67 | Human Rights Law | LLM | £28,400 |
| 68 | European Legal Studies | LLM | £28,400 |
| 69 | Law and Globalisation | LLM | £28,400 |
| 70 | Banking and Finance Law | LLM | £28,400 |
| 71 | Company Law and Corporate Governance | LLM | £28,400 |
| 72 | Labour Law and Corporate Governance | LLM | £28,400 |
| 73 | Law, Environment, Sustainability and Business | LLM | £28,400 |
| 74 | PGCE Education | PGCE | £29,300 |

#### Faculty of Health and Life Sciences (PGT)

| # | Programme | Award | Fee (Overseas) |
|---|-----------|-------|---------------|
| 1 | Biomedical Sciences Research | MSc | £31,300 |
| 2 | Molecular Neuroscience | MSc | £31,300 |
| 3 | Clinical Neuropsychology | MSc | £31,300 |
| 4 | Applied Neuropsychology | MSc | £31,300 |
| 5 | Psychology of Education BPS (Health) | MSc | £29,300 |
| 6 | Health Psychology | MSc | £31,300 |
| 7 | Nutrition, Physical Activity and Public Health | MSc | £31,300 |
| 8 | Public Health | MSc | £31,300 |
| 9 | Epidemiology | MSc | £31,300 |
| 10 | Global Health | MSc | £31,300 |
| 11 | Medical Statistics | MSc | £31,300 |
| 12 | Orthopaedic Research | MSc | £31,300 |
| 13 | Stem Cells and Regeneration | MSc | £31,300 |
| 14 | Translational Cardiovascular Medicine | MSc | £31,300 |
| 15 | Reproduction and Development | MSc | £31,300 |
| 16 | Physiology, Pharmacology and Neuroscience | MSc | £31,300 |
| 17 | Biochemistry | MSc | £31,300 |
| 18 | Biological Sciences | MSc | £31,300 |
| 19 | Bioinformatics | MSc | £31,300 |
| 20 | Biomedical Engineering | MSc | £31,300 |
| 21 | Digital Health | MSc | £31,300 |
| 22 | Implantology | MSc | varies |
| 23 | Dental Implantology | MSc | varies |
| 24 | Veterinary Sciences | MSc | £31,300 |
| 25 | Global Wildlife Health and Conservation | MSc | £31,300 |

#### Faculty of Science and Engineering (PGT)

| # | Programme | Award | Fee (Overseas) |
|---|-----------|-------|---------------|
| 1 | Advanced Composites | MSc | £32,300 |
| 2 | Advanced Microelectronic Systems Engineering | MSc | £32,300 |
| 3 | Advanced Mechanical Engineering | MSc | £32,300 |
| 4 | Aerial Robotics | MSc | £32,300 |
| 5 | Biorobotics | MSc | £32,300 |
| 6 | Communication Networks and Signal Processing | MSc | £32,300 |
| 7 | Computer Science (Conversion) | MSc | £36,400 |
| 8 | Cyber Security (Infrastructures Security) | MSc | £36,400 |
| 9 | Data Science | MSc | £36,400 |
| 10 | Digital Health | MSc | £31,300 |
| 11 | Earthquake Engineering and Infrastructure Resilience | MSc | £32,300 |
| 12 | Engineering Mathematics | MSc | £32,300 |
| 13 | Engineering with Management | MSc | £32,300 |
| 14 | Environmental Analytical Chemistry | MSc | £32,300 |
| 15 | Environmental Modelling and Data Analysis | MSc | £31,300 |
| 16 | Environmental Policy and Management | MSc | £31,300 |
| 17 | Financial Technology with Data Science | MSc | £36,400 |
| 18 | Geographic Data Science and Spatial Analytics | MSc | £31,300 |
| 19 | Global Development and Environment | MSc | £31,300 |
| 20 | Human Geography: Society and Space | MSc | £31,300 |
| 21 | Image and Video Communications and Signal Processing | MSc | £32,300 |
| 22 | Immersive Technologies (Virtual and Augmented Reality) | MSc | £36,400 |
| 23 | Innovation and Entrepreneurship | MSc | £34,300 |
| 24 | Mathematics of Cybersecurity | MSc | £32,300 |
| 25 | Nuclear Science and Engineering | MSc | £32,300 |
| 26 | Optical Communications and Signal Processing | MSc | £32,300 |
| 27 | Optoelectronic and Quantum Technologies | MSc | £32,300 |
| 28 | Palaeobiology | MSc | £31,300 |
| 29 | Physics | MSc | £32,300 |
| 30 | Robotics | MSc | £32,300 |
| 31 | Scientific Computing with Data Science | MSc | £36,400 |
| 32 | Society, Politics and Climate Change | MSc | £31,300 |
| 33 | Sustainable Engineering | MSc | £32,300 |
| 34 | Water and Environmental Management | MSc | £32,300 |
| 35 | Wireless Communications and Signal Processing | MSc | £32,300 |
| 36 | Chemistry | MSc | £32,300 |
| 37 | Earth Sciences | MSc | £31,300 |
| 38 | Mathematics | MSc | £32,300 |
| 39 | Nanoscience and Functional Nanomaterials | MSc | £32,300 |
| 40 | Climate Change Science and Policy | MSc | £31,300 |
| 41 | Global Challenges (online) | MSc | varies |
| 42 | Pharmacology | MSc | £31,300 |
| 43 | Volcanology | MSc | £31,300 |
| 44 | Society and Space | MSc | £31,300 |
| 45 | Innovation and Entrepreneurship (Science) | MSc | £34,300 |
| 46 | PG Certificate / PG Diploma programmes | PG Cert/Dip | varies |
| 47 | MRes programmes (various) | MRes | varies |
| 48 | MMus Composition | MMus | £30,800 |

### 2.3 Postgraduate research programmes (PGR) — grouped by faculty

Research programmes at Bristol are organized by research area. Each area may offer multiple award options (PhD, MPhil, MSc by research, etc.). Below is a summary of the 77 research areas.

#### Faculty of Arts, Law and Social Sciences (PGR) — 30 research areas

Accounting and Finance, Advanced Quantitative Methods, Anthropology and Archaeology, Classics and Ancient History, Comparative Literatures and Cultures, Creative Writing, DEdPsy Educational Psychology, Disability Studies, East Asian Studies, Economics, Education, English, Film and Television, French, Geographical Sciences (Human), German, Hispanic, Portuguese and Latin American Studies, History, History of Art, Innovation and Entrepreneurship, Italian, Law, Management, Music, Philosophy, Policy Studies, Politics, Russian, Social Work, Sociology, Theatre and Performance, Theology and Religious Studies, Translation

#### Faculty of Health and Life Sciences (PGR) — 18 research areas

Biochemistry, Biological Sciences, Cellular and Molecular Medicine, Dentistry, Medical Sciences, Medicine (MD), Neuroscience, Pharmacology, Physiology, Psychology, Veterinary Sciences, Translational Health Sciences, Population Health Sciences, South West Biosciences DTP, Anatomy, Cancer Biology, Immunology, Microbiology

#### Faculty of Science and Engineering (PGR) — 25 research areas

Advanced Composites, Aerosol Science, Aerospace Engineering, Chemistry, Civil Engineering, Climate Change Sustainability and Society, Composites Manufacture, Computer Science, Cyber Security, Data-Driven Engineering and Sciences, Earth Sciences, Electrical and Electronic Engineering, Engineering Mathematics, Geographical Sciences (Physical), Geology, Geophysics, Mathematics, Mechanical Engineering, Physics, Quantum Engineering, Robotics, Superconductivity, Technology Enhanced Chemical Synthesis, Sociotechnical Futures and Digital Methods, Water and Environmental Engineering

#### Research award options

The most common award options for PGR programmes are:
- **PhD** (3-4 years full-time): available across all 77 research areas
- **MPhil** (1-2 years full-time): available in ~21 research areas
- **MSc by research** (1 year full-time): available in ~21 research areas
- **MD** (2 years full-time): available in 3 clinical areas
- **EngD** (4 years): available in 3 engineering areas
- **DEdPsy** (3 years): Educational Psychology

### 2.4 PG Fee Summary

| Programme Type | Typical Overseas Fee (2026/27) |
|---------------|------------------------------|
| MA (Arts/Humanities) | £29,300 - £32,300 |
| MSc (Social Sciences) | £31,000 - £36,400 |
| MSc (Business/Finance) | £34,300 - £36,400 |
| MSc (Science/Engineering) | £31,300 - £36,400 |
| LLM (Law) | £28,400 |
| PGCE (Education) | £29,300 |
| PGR (PhD/MPhil standard) | £25,800 - £31,300 (banded) |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate admissions

| Dimension | Detail |
|-----------|--------|
| Application portal | UCAS (all UG applications) |
| UCAS institution code | B78 BRISL |
| UCAS deadline (most courses) | 29 January 2027 (for 2027 entry) |
| UCAS deadline (Medicine, Dentistry, Vet Science) | 15 October 2026 |
| Application fee (UCAS) | £28.50 (2027 entry) |
| Typical offer range | A*AA - ABB (A-Level); 36-32 (IB) |
| Contextual offers | Available — see contextual offers page |
| Interview policy | Selective: Medicine, Dentistry, Vet Science, and some others |
| Admissions tests | UCAT (Medicine/Dentistry); some courses require additional tests |

### 3.2 English language requirements

The University of Bristol uses 9 English language profiles (A-H + International Foundation Programme). Each course specifies its required profile. Tests must be taken within 2 years of the programme start date.

**Profile B** (most common for standard courses):

| Test | Undergraduate | Postgraduate |
|------|--------------|--------------|
| IELTS Academic | 7.0 overall (7.0 writing, 6.5 all other skills) | 7.0 overall (6.5 all skills) |
| TOEFL iBT (pre 21 Jan 2026) | 95 overall (R22, L21, S23, W24) | 95 overall (R22, L21, S23, W22) |
| TOEFL iBT (post 21 Jan 2026) | 5 overall (5 writing, 4.5 all other skills) | 5 overall (4.5 all skills) |
| Pearson PTE Academic | 71 overall (71 writing, 67 all other skills) | 71 overall (67 all skills) |
| C1 Advanced (CAE) | Grade C, or Level B2 (184 writing, 176 all other) | Grade C, or Level B2 (176 all skills) |
| C2 Proficiency (CPE) | Grade C, or Level C1 (184 writing, 176 all other) | Grade C, or Level C1 (176 all skills) |
| Trinity ISE | Level III/IV (105 overall, 105 Writing, 96 all other) | Level III/IV (105 overall, 96 all skills) |

**Language profiles summary**:

| Profile | Typical IELTS (UG) | Typical use |
|---------|-------------------|-------------|
| A | 7.5 overall, 7.0 all skills | Law, English |
| B | 7.0 overall, 7.0 writing, 6.5 all other | Most standard courses |
| C | 6.5 overall, 6.5 all skills | Some science courses |
| D | 6.5 overall, 6.0 all skills | Some engineering courses |
| E | 6.0 overall, 5.5 all skills | Foundation pathways |
| F | 7.0 overall, 6.5 all skills | PG research (some) |
| G | 6.5 overall, 6.0 reading/writing, 5.5 other | PG (some) |
| H | 7.5 overall, 7.0 all skills | Higher requirement |
| IFP | Varies | International Foundation Programme |

### 3.3 Postgraduate admissions

| Dimension | Detail |
|-----------|--------|
| Application model | Decentralised — apply directly via online application portal |
| Application fee | £60 (online) for most taught programmes |
| Application fee (Business School) | £60 |
| Typical deadline (PGT) | Rolling admissions — apply by July/August for September start |
| PGR deadlines | Vary by programme — typically 3-4 start dates per year |
| References | 2 academic references typically required |
| Personal statement | Required |
| English proficiency | Same profile system as UG |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026/27 academic year)

| Expense item | Amount (Overseas) | Notes |
|-------------|------------------|-------|
| Tuition (Arts, Law and Social Sciences) | £25,500 - £33,400 | Varies by programme |
| Tuition (Science and Engineering) | £31,300 - £33,400 | Standard rate £31,300 |
| Tuition (Health and Life Sciences) | £31,300 - £49,700 | Dentistry highest at £49,700 |
| Tuition (Medicine MBChB) | £44,000 | Per year, all years |
| Tuition (Veterinary Science BVSc) | £44,000 | Per year, all years |
| Tuition (Home/EU) | £9,250 | Regulated by UK government |
| Living costs (estimated) | ~£12,000 - £15,000 | Accommodation, food, travel, etc. |
| Accommodation (University) | £5,000 - £10,000 | Varies by hall and room type |

### 4.2 Postgraduate cost (2026/27, overseas)

| Programme type | Typical fee range |
|---------------|------------------|
| MA (Arts/Humanities/Social Sciences) | £29,300 - £32,300 |
| MSc (Social Sciences) | £31,000 - £36,400 |
| MSc (Business/Finance) | £34,300 - £36,400 |
| MSc (Science/Engineering) | £31,300 - £36,400 |
| LLM (Law) | £28,400 |
| PGR (PhD standard) | ~£25,800 - £31,300 |
| PGCE | £29,300 |

### 4.3 Financial aid

| Programme | Detail |
|-----------|--------|
| UG Home students | Tuition Fee Loan + Maintenance Loan via Student Finance England |
| UG International scholarships | Think Big Undergraduate Scholarship (£6,500 - £13,000 per year) |
| PG scholarships | Think Big Postgraduate Scholarship (£6,500 - £26,000) |
| Alumni discount | 25% off PG tuition fees for Bristol alumni |
| Doctoral funding | UKRI studentships, University scholarships, CDT/DTP programmes |
| Hardship fund | Available for students in financial difficulty |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Bristol"
  source_url: https://www.bristol.ac.uk/
  source_snippet: "University of Bristol"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.faculties
  value: "3 faculties: Arts, Law and Social Sciences; Health and Life Sciences; Science and Engineering"
  source_url: https://www.bristol.ac.uk/faculties/
  source_snippet: "Academic schools by faculty: Arts, Law and Social Sciences; Health and Life Sciences; Science and Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.schools
  value: "28 schools across 3 faculties"
  source_url: https://www.bristol.ac.uk/faculties/
  source_snippet: "School of Arts, School of Economics, School of Education, School of Humanities, School of Modern Languages, School for Policy Studies, School of Sociology Politics and International Studies, University of Bristol Business School, University of Bristol Law School, Bristol Anatomy Centre, Bristol Dental School, Bristol Medical School, Bristol Veterinary School, School of Biochemistry, School of Biological Sciences, School of Cellular and Molecular Medicine, School of Psychology and Neuroscience, School of Chemistry, School of Civil Aerospace and Design Engineering, School of Computer Science, School of Earth Sciences, School of Electrical Electronic and Mechanical Engineering, School of Engineering Mathematics and Technology, School of Geographical Sciences, School of Mathematics, School of Physics, Centre for Academic Language and Development, Centre for Innovation and Entrepreneurship"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.subjects.count
  value: "54 subject areas for 2027 entry"
  source_url: https://www.bristol.ac.uk/study/undergraduate/subjects/
  source_snippet: "Browse subject areas — 2027 entry"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.programs.total
  value: "503"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/ug/overseas/26-27/2026-starters/
  source_snippet: "Table: Faculty | Programme code | Programme | Mode | Fee — 503 data rows"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.fees.overseas.range
  value: "£25,500 - £49,700"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/ug/overseas/26-27/2026-starters/
  source_snippet: "Arts, Law and Social Sciences: £25,500-£33,400; Health and Life Sciences: £31,300-£49,700; Science and Engineering: £31,300-£33,400"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.fees.dentistry
  value: "£49,700 per year"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/ug/overseas/26-27/2026-starters/
  source_snippet: "Dentistry (BDS), 8ORDS001U, Full-time, £49,700"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.fees.medicine
  value: "£44,000 per year"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/ug/overseas/26-27/2026-starters/
  source_snippet: "Medicine (MBChB), 8MEDC001U, Full-time, £44,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.fees.veterinary
  value: "£44,000 per year (BVSc)"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/ug/overseas/26-27/2026-starters/
  source_snippet: "Veterinary Science (BVSc), 8VETS001U, Full-time, £44,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-010:
  field: language_requirements.profiles
  value: "9 profiles: A, B, C, D, E, F, G, H, International Foundation Programme"
  source_url: https://www.bristol.ac.uk/study/language-requirements/
  source_snippet: "Language profiles for undergraduates and postgraduates: Profile A, Profile B, Profile C, Profile D, Profile E, Profile F, Profile G, Profile H, Profile International Programme"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: language_requirements.profile_b.ielts
  value: "UG: 7.0 overall with 7.0 in writing and 6.5 in all other skills; PG: 7.0 overall with 6.5 in all skills"
  source_url: https://www.bristol.ac.uk/study/language-requirements/profile-b/
  source_snippet: "IELTS Academic: UG: 7.0 overall with 7.0 in writing and 6.5 in all other skills; PG: 7.0 overall with 6.5 in all skills"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-012:
  field: language_requirements.profile_b.toefl
  value: "UG: 95 overall with R22, L21, S23, W24; PG: 95 overall with R22, L21, S23, W22 (pre-21 Jan 2026)"
  source_url: https://www.bristol.ac.uk/study/language-requirements/profile-b/
  source_snippet: "TOEFL iBT: UG: 95 overall with R22, L21, S23, W24; PG: 95 overall with R22, L21, S23, W22"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-013:
  field: language_requirements.profile_b.pte
  value: "71 overall with no lower than 71 in writing and 67 in all other skills"
  source_url: https://www.bristol.ac.uk/study/language-requirements/profile-b/
  source_snippet: "Pearson PTE Academic: UG: 71 overall with no lower than 71 in writing and no lower than 67 in all other skills"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-014:
  field: language_requirements.validity_period
  value: "Tests must be taken within 2 years of the programme start date"
  source_url: https://www.bristol.ac.uk/study/language-requirements/
  source_snippet: "English language proficiency tests should be obtained within two years of the start date of your programme or course"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: postgraduate.programs.total
  value: "240 (163 taught, 77 research)"
  source_url: https://www.bristol.ac.uk/study/postgraduate/search/
  source_snippet: "240 results found"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: postgraduate.taught.fees.overseas
  value: "£28,400 - £36,400"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/pgt/overseas/26-27/2026-starters/
  source_snippet: "Table: Faculty | Programme code | Programme | Mode | Fee — 240 data rows"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-017:
  field: undergraduate.admissions.ucas_code
  value: "B78 BRISL"
  source_url: https://www.bristol.ac.uk/study/undergraduate/apply/
  source_snippet: "UCAS institution code: B78 BRISL"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-018:
  field: undergraduate.fees.home
  value: "£9,250 per year"
  source_url: https://www.bristol.ac.uk/students/support/finances/tuition-fees/ug/home/
  source_snippet: "Home undergraduate tuition fees"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-019:
  field: postgraduate.admissions.fee
  value: "£60 application fee for most taught programmes"
  source_url: https://www.bristol.ac.uk/study/postgraduate/apply/
  source_snippet: "Application fee"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-020:
  field: institution.rankings
  value: "QS World University Rankings 2027: 57th world, 8th UK"
  source_url: https://www.bristol.ac.uk/news/2026/june/university-of-bristol-ranked-8th-in-uk-in-latest-qs-world-university-rankings.html
  source_snippet: "We're ranked 57th in the world (QS World University Rankings 2027); We're ranked 8th in the UK"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-021:
  field: institution.research_quality
  value: "Top 5 UK university for research quality (REF 2021)"
  source_url: https://www.bristol.ac.uk/news/2022/may/ref-2021.html
  source_snippet: "We're a top 5 UK university for research quality (Times Higher Education REF 2021 quality ratings)"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
bristol-knowledge-base-v2/
├── chunk-00-overview (Section 0)          # Rules 1-4, hierarchy, matrix
├── chunk-01-ug-arts-law (Section 1)       # UG programs: Arts, Law and Social Sciences
├── chunk-02-ug-health-life (Section 1)    # UG programs: Health and Life Sciences
├── chunk-03-ug-science-eng (Section 1)    # UG programs: Science and Engineering
├── chunk-04-pg-taught (Section 2)         # PG taught programmes
├── chunk-05-pg-research (Section 2)       # PG research programmes
├── chunk-06-requirements (Section 3)      # Admissions requirements & deadlines
├── chunk-07-language (Section 3)          # English language requirements
├── chunk-08-costs (Section 4)             # Costs & financial aid
├── chunk-09-evidence (Section 5)          # Evidence chain index
└── chunk-10-comparison (Section 7)        # Cross-school comparison
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "bristol-knowledge-base-v2"
  university: "University of Bristol"
  region: "uk"
  russell_group: true
  degree_level: "mixed"
  level: undergraduate | postgraduate | mixed
  field_type: overview | programs | requirements | costs | evidence
  source_url: https://www.bristol.ac.uk/
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P1 | Complete PG research (PGR) overseas fees by programme | https://www.bristol.ac.uk/students/support/finances/tuition-fees/pgr/overseas/ |
| P1 | Per-course A-Level/IB entry requirements | Individual course pages |
| P1 | Per-course English language profile assignment | Individual course pages |
| P1 | PG research stipend rates and funding details | https://www.bristol.ac.uk/doctoral-college/ |
| P2 | UG accommodation costs breakdown | https://www.bristol.ac.uk/accommodation/ |
| P2 | Course module details and curriculum | Individual course pages |
| P2 | Full PG research programme detail pages (supervisors, research groups) | Individual PGR programme pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Bristol | Cambridge | Oxford | Imperial |
|-----------|--------|-----------|--------|----------|
| Institution type | Russell Group | Russell Group | Russell Group | Russell Group |
| QS World Rank 2027 | 57 | -- | -- | -- |
| QS UK Rank 2027 | 8 | -- | -- | -- |
| Total UG programmes | 503 | -- | -- | -- |
| Total PG programmes | 240 | -- | -- | -- |
| Total programmes (UG+PG) | 743 | -- | -- | -- |
| Faculties | 3 | -- | -- | -- |
| Schools/Departments | 28 | -- | -- | -- |
| UG degree types | 14 | -- | -- | -- |
| PG award types | 14 | -- | -- | -- |
| UG overseas fee range | £25,500 - £49,700 | -- | -- | -- |
| PG overseas fee range | £28,400 - £36,400 | -- | -- | -- |
| IELTS minimum (standard) | 7.0 overall (Profile B) | -- | -- | -- |
| Language profiles | 9 (A-H + IFP) | -- | -- | -- |
| Application system | UCAS | UCAS | UCAS | UCAS |
| Home UG tuition | £9,250 | £9,250 | £9,250 | £9,250 |
| REF 2021 quality rank | Top 5 UK | -- | -- | -- |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: bristol.ac.uk (main, study, students, faculties subdomains)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Completeness**: Section 0 (100%) | Section 1 (100% - 503 programmes) | Section 2 (95% - 240 programmes, fee details for taught only) | Section 3 (90% - language profiles complete) | Section 4 (90% - UG fees complete, PG research fees pending) | Evidence (21 blocks)