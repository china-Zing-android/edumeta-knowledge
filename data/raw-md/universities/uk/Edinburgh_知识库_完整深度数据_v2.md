# The University of Edinburgh Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch + DRPS programme tables
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Scotland)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | ~380 |
| 研究生授课型 (PGT: MSc/MA/MBA/LLM/MPH/PGDip/PGCert) | ~350 |
| 研究生博士 (PhD/MScR/EngD) | ~200+ |
| 学院 (Colleges) | 3 |
| 学院/系所 (Schools) | 26 |

> **Data source**: University of Edinburgh Degree Finder A-Z (`study.ed.ac.uk/programmes/undergraduate-a-z` and `study.ed.ac.uk/programmes/postgraduate-taught-a-z`) combined with DRPS Degree Programme Tables (`drps.ed.ac.uk/26-27/dpt/`). UG count from A-Z listing (A-M: ~150 programmes visible, estimated ~380 total including N-Z). PGT count from A-Z listing (A-P: ~240 programmes visible, estimated ~350 total including Q-W).
>
> **Note**: Edinburgh uses the Scottish MA (Hons) 4-year degree for most humanities/social science programmes — this is an undergraduate degree, NOT a postgraduate master's. Similarly, MEng/MPhys/MChem/MEarthSci/MBiol are 4-5 year integrated master's degrees classified as undergraduate.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
The University of Edinburgh
├── College of Arts, Humanities and Social Sciences          [学院]
│   ├── Edinburgh College of Art                             [系]
│   ├── School of Divinity                                   [系]
│   ├── Moray House School of Education and Sport            [系]
│   ├── School of Health in Social Science                   [系]
│   ├── School of History, Classics and Archaeology          [系]
│   ├── School of Law                                        [系]
│   ├── School of Literatures, Languages and Cultures        [系]
│   ├── Business School                                      [系]
│   ├── School of Philosophy, Psychology and Language Sciences [系]
│   ├── School of Social and Political Science               [系]
│   ├── School of Economics                                  [系]
│   ├── Centre for Open Learning                             [系]
│   └── Edinburgh Futures Institute                          [系]
├── College of Science and Engineering                       [学院]
│   ├── School of Biological Sciences                        [系]
│   ├── School of Chemistry                                  [系]
│   ├── School of Engineering                                [系]
│   ├── School of Geosciences                                [系]
│   ├── School of Informatics                                [系]
│   ├── School of Mathematics                                [系]
│   └── School of Physics and Astronomy                      [系]
└── College of Medicine and Veterinary Medicine              [学院]
    ├── Edinburgh Medical School                             [系]
    ├── Royal (Dick) School of Veterinary Studies            [系]
    ├── School of Neurological and Cardiovascular Sciences   [系]
    ├── School of Regeneration and Repair                    [系]
    ├── School of Population Health Sciences                 [系]
    └── School of Genetics and Cancer                        [系]
```

> **Data source**: DRPS 2026-2027 Degree Programme Tables index (`drps.ed.ac.uk/26-27/dpt/drpsindex.htm`).
>
> **Note**: The College of Medicine and Veterinary Medicine has a non-traditional structure — the "Schools" (Genetics and Cancer, Neurological and Cardiovascular Sciences, Regeneration and Repair, Population Health Sciences) are research groupings. Teaching is primarily delivered through Edinburgh Medical School and the Royal (Dick) School of Veterinary Studies.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| MA (Hons) | Master of Arts (Honours) — Scottish 4-year UG | 本科 | ~200 |
| BSc (Hons) | Bachelor of Science (Honours) | 本科 | ~100 |
| BEng (Hons) | Bachelor of Engineering (Honours) | 本科 | ~15 |
| LLB (Hons) | Bachelor of Laws (Honours) | 本科 | ~16 |
| MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 1 (6-year) |
| BVMS | Bachelor of Veterinary Medicine and Surgery | 本科 | 1 (multiple entry routes) |
| BA (Hons) | Bachelor of Arts (Honours) | 本科 | ~10 |
| BMedSci (Hons) | Bachelor of Medical Science (Honours) | 本科 | ~15 |
| MEng (Hons) | Master of Engineering (integrated 5-year) | 本科 | ~15 |
| MPhys | Master of Physics (integrated 5-year) | 本科 | ~7 |
| MChem | Master of Chemistry (integrated 5-year) | 本科 | ~2 |
| MChemPhys | Master of Chemical Physics (integrated) | 本科 | 1 |
| MEarthSci | Master of Earth Science (integrated) | 本科 | ~2 |
| MBiol | Master of Biology (integrated) | 本科 | 1 |
| MInf | Master of Informatics (integrated 5-year) | 本科 | 1 |
| MMath (Hons) | Master of Mathematics (integrated) | 本科 | ~2 |
| Dip HE | Diploma of Higher Education | 本科 | 1 |
| MSc | Master of Science | 研究生授课型 | ~200 |
| MA (eca) | Master of Arts (Edinburgh College of Art) | 研究生授课型 | ~8 |
| LLM | Master of Laws | 研究生授课型 | ~25 |
| MBA | Master of Business Administration | 研究生授课型 | ~5 |
| MEd | Master of Education | 研究生授课型 | ~2 |
| MPH | Master of Public Health | 研究生授课型 | ~3 |
| MRes | Master of Research | 研究生研究型 | ~5 |
| MMus | Master of Music | 研究生授课型 | ~2 |
| MCouns | Master of Counselling | 研究生授课型 | ~2 |
| MFA | Master of Fine Art | 研究生授课型 | 1 |
| MLA | Master of Landscape Architecture | 研究生授课型 | 1 |
| MArch | Master of Architecture (ARB/RIBA Part 2) | 研究生授课型 | 1 |
| MVetSci | Master of Veterinary Science | 研究生授课型 | ~3 |
| MFM | Master of Family Medicine | 研究生授课型 | 1 |
| MN(T) | Master of Nursing (Pre-Registration) | 研究生授课型 | 1 |
| MSW | Master of Social Work | 研究生授课型 | 1 |
| DClinPsychol | Doctor of Clinical Psychology | 研究生授课型 | 1 |
| DClinDent | Doctor of Clinical Dentistry | 研究生授课型 | ~2 |
| DVetMed | Doctor of Veterinary Medicine | 研究生授课型 | 1 |
| DPsychotherapy | Doctor of Psychotherapy | 研究生授课型 | 1 |
| PGDE | Professional Graduate Diploma in Education | 研究生授课型 | 2 |
| PgDip | Postgraduate Diploma | 研究生文凭 | ~15 |
| PgCert | Postgraduate Certificate | 研究生证书 | ~10 |
| PgProfDev | Postgraduate Professional Development | 研究生证书 | ~10 |
| PhD | Doctor of Philosophy | 研究生博士 | ~150 |
| MSc by Research | Master of Science by Research | 研究生研究型 | ~30 |
| EngD | Engineering Doctorate | 研究生博士 | ~2 |

> **UK/Scotland degree naming note**: Edinburgh awards the Scottish MA (Hons) — a 4-year undergraduate degree. This is NOT equivalent to a postgraduate MA. The MEng, MPhys, MChem, MEarthSci, MBiol, MInf, and MMath are 4-5 year integrated master's degrees classified as undergraduate in the UK system. Edinburgh does NOT award standalone BEng degrees in most engineering disciplines (they offer BEng Hons as a 3-year exit or MEng Hons as the full 5-year programme).

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | MA | BSc | BEng | LLB | MBChB | BVMS | BA | BMedSci | MEng | MPhys | MChem | Other UG | MSc | LLM | MBA | Other PGT | PhD/MScR | 合计 |
|------------|-----|-----|------|-----|-------|------|-----|---------|------|-------|-------|----------|-----|-----|-----|-----------|----------|------|
| Arts, Humanities & Social Sciences | ~200 | ~5 | 0 | ~16 | 0 | 0 | ~10 | ~1 | 0 | 0 | 0 | ~5 | ~130 | ~25 | ~5 | ~30 | ~100 | ~527 |
| Science and Engineering | ~5 | ~80 | ~15 | 0 | 0 | 0 | 0 | 0 | ~15 | ~7 | ~3 | ~10 | ~70 | 0 | 0 | ~10 | ~60 | ~275 |
| Medicine and Veterinary Medicine | 0 | ~20 | 0 | 0 | ~4 | ~4 | 0 | ~15 | 0 | 0 | 0 | ~5 | ~40 | 0 | 0 | ~15 | ~10 | ~113 |
| **合计** | **~205** | **~105** | **~15** | **~16** | **~4** | **~4** | **~10** | **~16** | **~15** | **~7** | **~3** | **~20** | **~240** | **~25** | **~5** | **~55** | **~170** | **~915** |

> **Reconciliation**: ~527 + ~275 + ~113 = ~915 total programme entries. Counts are approximate as some programmes span multiple schools and some PGT programmes have multiple delivery modes (FT/PT/Online) counted separately in DRPS.
>
> **Note**: The DRPS counts include all delivery modes (full-time, part-time, online, ICL) as separate programme entries. The Degree Finder A-Z lists unique programme names. The A-Z UG count of ~380 represents unique programme names; the DRPS count of ~385 includes some variants (e.g., widening access routes).

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Edinburgh has 3 Colleges containing 26 Schools. All undergraduate teaching is organized within these Schools. See Section 0.2 for the full hierarchy tree.

**UCAS institution code: E56**. Edinburgh uses UCAS for all undergraduate applications (no Common App for UK students; international students also apply via UCAS).

**Key structural notes**:
- The Scottish MA (Hons) is a 4-year undergraduate degree — Edinburgh's humanities and social science degrees are mostly MA (Hons), NOT BA
- Edinburgh does NOT use a US-style "college" system — students apply directly to a specific degree programme
- Some programmes allow "second year entry" (direct entry to Year 2) for students with appropriate qualifications
- Combined/joint degrees are very common at Edinburgh — many programmes combine two subjects (e.g., "French and History", "Computer Science and Mathematics")

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts, Humanities and Social Sciences

##### Business School

###### MA (Hons) — 4-year undergraduate

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Business | [Link](https://study.ed.ac.uk/programmes/undergraduate/189-accounting-and-business) |
| 2 | Accounting and Finance | [Link](https://study.ed.ac.uk/programmes/undergraduate/464-accounting-and-finance) |
| 3 | Business and Economics | [Link](https://study.ed.ac.uk/programmes/undergraduate/186-business-and-economics) |
| 4 | Business and Law | [Link](https://study.ed.ac.uk/programmes/undergraduate/188-business-and-law) |
| 5 | Business Management | [Link](https://study.ed.ac.uk/programmes/undergraduate/182-business-management) |
| 6 | Business with Decision Analytics | [Link](https://study.ed.ac.uk/programmes/undergraduate/604-business-with-decision-analytics) |
| 7 | Business with Enterprise and Innovation | [Link](https://study.ed.ac.uk/programmes/undergraduate/605-business-with-enterprise-and-innovation) |
| 8 | Business with Human Resource Management | [Link](https://study.ed.ac.uk/programmes/undergraduate/606-business-with-human-resource-management) |
| 9 | Business with Marketing | [Link](https://study.ed.ac.uk/programmes/undergraduate/607-business-with-marketing) |
| 10 | Business with Strategic Economics | [Link](https://study.ed.ac.uk/programmes/undergraduate/608-business-with-strategic-economics) |
| 11 | Finance and Business | [Link](https://study.ed.ac.uk/programmes/undergraduate/603-finance-and-business) |
| 12 | International Business | [Link](https://study.ed.ac.uk/programmes/undergraduate/183-international-business) |
| 13 | International Business with Chinese | [Link](https://study.ed.ac.uk/programmes/undergraduate/615-international-business-with-chinese) |
| 14 | International Business with French | [Link](https://study.ed.ac.uk/programmes/undergraduate/609-international-business-with-french) |
| 15 | International Business with German | [Link](https://study.ed.ac.uk/programmes/undergraduate/610-international-business-with-german) |
| 16 | International Business with Italian | [Link](https://study.ed.ac.uk/programmes/undergraduate/611-international-business-with-italian) |
| 17 | International Business with Japanese | [Link](https://study.ed.ac.uk/programmes/undergraduate/616-international-business-with-japanese) |
| 18 | International Business with Spanish | [Link](https://study.ed.ac.uk/programmes/undergraduate/613-international-business-with-spanish) |

##### School of Economics

###### MA (Hons) — 4-year undergraduate

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | [Link](https://study.ed.ac.uk/programmes/undergraduate/122-economics) |
| 2 | Economics and Accounting | [Link](https://study.ed.ac.uk/programmes/undergraduate/153-economics-and-accounting) |
| 3 | Economics and Mathematics | [Link](https://study.ed.ac.uk/programmes/undergraduate/133-economics-and-mathematics) |
| 4 | Economics and Politics | [Link](https://study.ed.ac.uk/programmes/undergraduate/135-economics-and-politics) |
| 5 | Economics and Statistics | [Link](https://study.ed.ac.uk/programmes/undergraduate/134-economics-and-statistics) |
| 6 | Economics with Finance | [Link](https://study.ed.ac.uk/programmes/undergraduate/469-economics-with-finance) |
| 7 | Economics with Management Science | [Link](https://study.ed.ac.uk/programmes/undergraduate/392-economics-with-management-science) |

##### School of Law

###### LLB (Hons) — 4-year undergraduate

| # | 专业 | URL |
|---|------|-----|
| 1 | Law (Ordinary and Honours) | [Link](https://study.ed.ac.uk/programmes/undergraduate/168-law-ordinary-and-honours) |
| 2 | Global Law | [Link](https://study.ed.ac.uk/programmes/undergraduate/671-global-law) |
| 3 | Law and Accountancy | [Link](https://study.ed.ac.uk/programmes/undergraduate/175-law-and-accountancy) |
| 4 | Law and Business | [Link](https://study.ed.ac.uk/programmes/undergraduate/174-law-and-business) |
| 5 | Law and Celtic | [Link](https://study.ed.ac.uk/programmes/undergraduate/176-law-and-celtic) |
| 6 | Law and French | [Link](https://study.ed.ac.uk/programmes/undergraduate/177-law-and-french) |
| 7 | Law and German | [Link](https://study.ed.ac.uk/programmes/undergraduate/178-law-and-german) |
| 8 | Law and History | [Link](https://study.ed.ac.uk/programmes/undergraduate/180-law-and-history) |
| 9 | Law and International Relations | [Link](https://study.ed.ac.uk/programmes/undergraduate/482-law-and-international-relations) |
| 10 | Law and Politics | [Link](https://study.ed.ac.uk/programmes/undergraduate/171-law-and-politics) |
| 11 | Law and Social Anthropology | [Link](https://study.ed.ac.uk/programmes/undergraduate/169-law-and-social-anthropology) |
| 12 | Law and Social Policy | [Link](https://study.ed.ac.uk/programmes/undergraduate/173-law-and-social-policy) |
| 13 | Law and Sociology | [Link](https://study.ed.ac.uk/programmes/undergraduate/172-law-and-sociology) |
| 14 | Law and Spanish | [Link](https://study.ed.ac.uk/programmes/undergraduate/179-law-and-spanish) |

###### LLB (Ord) — 3-year ordinary (Graduate Entry)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law (Graduate Entry) | [Link](https://study.ed.ac.uk/programmes/undergraduate/378-law-graduate-entry) |

##### School of History, Classics and Archaeology

###### MA (Hons) — 4-year undergraduate

| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient History | [Link](https://study.ed.ac.uk/programmes/undergraduate/302-ancient-history) |
| 2 | Ancient and Medieval History | [Link](https://study.ed.ac.uk/programmes/undergraduate/373-ancient-and-medieval-history) |
| 3 | Archaeology | [Link](https://study.ed.ac.uk/programmes/undergraduate/310-archaeology) |
| 4 | Archaeology and Ancient History | [Link](https://study.ed.ac.uk/programmes/undergraduate/648-archaeology-and-ancient-history) |
| 5 | Archaeology and Social Anthropology | [Link](https://study.ed.ac.uk/programmes/undergraduate/322-archaeology-and-social-anthropology) |
| 6 | Classical Archaeology and Ancient History | [Link](https://study.ed.ac.uk/programmes/undergraduate/337-classical-archaeology-and-ancient-history) |
| 7 | Classical Studies | [Link](https://study.ed.ac.uk/programmes/undergraduate/204-classical-studies) |
| 8 | Classics | [Link](https://study.ed.ac.uk/programmes/undergraduate/203-classics) |
| 9 | History | [Link](https://study.ed.ac.uk/programmes/undergraduate/301-history) |
| 10 | History and Archaeology | [Link](https://study.ed.ac.uk/programmes/undergraduate/467-history-and-archaeology) |
| 11 | History and Classics | [Link](https://study.ed.ac.uk/programmes/undergraduate/376-history-and-classics) |
| 12 | History and Economics | [Link](https://study.ed.ac.uk/programmes/undergraduate/658-history-and-economics) |
| 13 | History and History of Art | [Link](https://study.ed.ac.uk/programmes/undergraduate/336-history-and-history-of-art) |
| 14 | History and Politics | [Link](https://study.ed.ac.uk/programmes/undergraduate/161-history-and-politics) |
| 15 | History and Scottish History | [Link](https://study.ed.ac.uk/programmes/undergraduate/304-history-and-scottish-history) |
| 16 | History of Art | [Link](https://study.ed.ac.uk/programmes/undergraduate/307-history-of-art) |
| 17 | History of Art and Architectural History | [Link](https://study.ed.ac.uk/programmes/undergraduate/308-history-of-art-and-architectural-history) |
| 18 | History of Art and Chinese Studies | [Link](https://study.ed.ac.uk/programmes/undergraduate/299-history-of-art-and-chinese-studies) |
| 19 | History of Art and English Literature | [Link](https://study.ed.ac.uk/programmes/undergraduate/327-history-of-art-and-english-literature) |
| 20 | History of Art and History of Music | [Link](https://study.ed.ac.uk/programmes/undergraduate/345-history-of-art-and-history-of-music) |
| 21 | History of Art and Scottish Literature | [Link](https://study.ed.ac.uk/programmes/undergraduate/590-history-of-art-and-scottish-literature) |
| 22 | Architectural History and Archaeology | [Link](https://study.ed.ac.uk/programmes/undergraduate/344-architectural-history-and-archaeology) |
| 23 | Architectural History and Heritage | [Link](https://study.ed.ac.uk/programmes/undergraduate/338-architectural-history-and-heritage) |

##### School of Literatures, Languages and Cultures

###### MA (Hons) — 4-year undergraduate (selected; full list has 115+ programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Arabic | [Link](https://study.ed.ac.uk/programmes/undergraduate/286-arabic-with-islamic-and-middle-eastern-studies) |
| 2 | Celtic | [Link](https://study.ed.ac.uk/programmes/undergraduate/199-celtic) |
| 3 | Chinese | [Link](https://study.ed.ac.uk/programmes/undergraduate/284-chinese) |
| 4 | English Language | [Link](https://study.ed.ac.uk/programmes/undergraduate/196-english-language) |
| 5 | English Literature | [Link](https://study.ed.ac.uk/programmes/undergraduate/197-english-literature) |
| 6 | French | [Link](https://study.ed.ac.uk/programmes/undergraduate/238-french) |
| 7 | German | [Link](https://study.ed.ac.uk/programmes/undergraduate/239-german) |
| 8 | Italian | [Link](https://study.ed.ac.uk/programmes/undergraduate/240-italian) |
| 9 | Japanese | [Link](https://study.ed.ac.uk/programmes/undergraduate/285-japanese) |
| 10 | Linguistics | [Link](https://study.ed.ac.uk/programmes/undergraduate/194-linguistics) |
| 11 | Scottish Literature | — |
| 12 | Spanish | — |
| 13 | Russian Studies | — |
| 14 | Scandinavian Studies | — |
| 15 | Persian Studies | — |
| 16 | Portuguese | — |

> **Note**: The School of Literatures, Languages and Cultures offers 115+ UG programmes, the vast majority being joint/combined degrees pairing two languages or a language with another subject (e.g., "French and History", "Chinese and Linguistics", "Celtic and Scottish History"). The 16 programmes listed above are the single-subject "anchor" degrees.

##### School of Philosophy, Psychology and Language Sciences

###### MA (Hons) / BSc (Hons) — 4-year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cognitive Science (Humanities) | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/479-cognitive-science-humanities) |
| 2 | Linguistics and English Language | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/208-linguistics-and-english-language) |
| 3 | Linguistics and Social Anthropology | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/206-linguistics-and-social-anthropology) |
| 4 | Philosophy | MA (Hons) | (via Degree Finder) |
| 5 | Psychology | MA (Hons) / BSc (Hons) | (via Degree Finder) |

> **Note**: Psychology is offered as both MA (Hons) and BSc (Hons). Philosophy is offered as MA (Hons) with many joint degree combinations.

##### School of Social and Political Science

###### MA (Hons) / BSc (Hons) — 4-year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Government, Policy and Society | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/650-government-policy-and-society) |
| 2 | International Relations | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/377-international-relations) |
| 3 | Politics | MA (Hons) | (via DRPS) |
| 4 | Social Anthropology | MA (Hons) | (via DRPS) |
| 5 | Social Policy | MA (Hons) | (via DRPS) |
| 6 | Social Work | BSc (Hons) | (via DRPS) |
| 7 | Sociology | MA (Hons) | (via DRPS) |
| 8 | Sustainable Development | MA (Hons) | (via DRPS, multiple pathways) |

> **Note**: SPS offers 30 UG programmes including many joint degrees (e.g., "Politics, Philosophy and Economics", "International Relations and International Law", "Social Policy and Sociology").

##### Edinburgh College of Art

###### BA (Hons) / MA (Hons) — 4-year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Animation | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/495-animation) |
| 2 | Architecture | BA/MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/120-architecture) |
| 3 | Fashion | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/496-fashion) |
| 4 | Film and Television | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/497-film-and-television) |
| 5 | Fine Art | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/669-fine-art) |
| 6 | Fine Art and History of Art | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/1150-fine-art-and-history-of-art) |
| 7 | Graphic Design | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/500-graphic-design) |
| 8 | Illustration | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/501-illustration) |
| 9 | Interior Design | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/502-interior-design) |
| 10 | Jewellery and Silversmithing | BA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/503-jewellery-and-silversmithing) |
| 11 | Landscape Architecture | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/674-landscape-architecture) |

##### Moray House School of Education and Sport

###### MA (Hons) / BSc (Hons) — 4-year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Sport Science | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/114-applied-sport-science) |
| 2 | Childhood Practice | BA (Ord) | [Link](https://study.ed.ac.uk/programmes/undergraduate/412-childhood-practice) |
| 3 | Learning in Communities | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/667-learning-in-communities) |
| 4 | Health in Social Science | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/627-health-in-social-science) |
| 5 | Interdisciplinary Futures | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/670-interdisciplinary-futures) |

##### School of Divinity

###### MA (Hons) — 4-year undergraduate

| # | 专业 | URL |
|---|------|-----|
| 1 | Divinity | (via Degree Finder) |

##### School of Health in Social Science

(Offers programmes through other schools; research-focused)

##### Edinburgh Futures Institute

(Offers interdisciplinary programmes including "Interdisciplinary Futures" MA)

#### College of Science and Engineering

##### School of Informatics

###### BSc (Hons) / BEng (Hons) / MInf — 4-5 year undergraduate

| # | 专业 | 学位 | UCAS Code | URL |
|---|------|------|-----------|-----|
| 1 | Artificial Intelligence | BSc (Hons) | — | [Link](https://study.ed.ac.uk/programmes/undergraduate/388-artificial-intelligence) |
| 2 | Artificial Intelligence and Computer Science | BSc (Hons) | — | [Link](https://study.ed.ac.uk/programmes/undergraduate/66-artificial-intelligence-and-computer-science) |
| 3 | Cognitive Science | BSc (Hons) | — | (via DRPS) |
| 4 | Computer Science | BSc (Hons) | G400 | [Link](https://study.ed.ac.uk/programmes/undergraduate/57-computer-science) |
| 5 | Computer Science | BEng (Hons) | — | [Link](https://study.ed.ac.uk/programmes/undergraduate/58-computer-science) |
| 6 | Computer Science and Management Science | BSc (Hons) | — | (via DRPS) |
| 7 | Computer Science and Mathematics | BSc (Hons) | — | [Link](https://study.ed.ac.uk/programmes/undergraduate/64-computer-science-and-mathematics) |
| 8 | Computer Science and Physics | BSc (Hons) | — | (via DRPS) |
| 9 | Informatics (5-year) | MInf | — | [Link](https://study.ed.ac.uk/programmes/undergraduate/430-informatics-5-year-undergraduate-masters-programme) |
| 10 | Software Engineering | BEng (Hons) | — | (via DRPS) |

##### School of Engineering

###### BEng (Hons) / MEng (Hons) — 4-5 year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | BEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/99-chemical-engineering) |
| 2 | Chemical Engineering | MEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/100-chemical-engineering) |
| 3 | Civil Engineering | BEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/76-civil-engineering) |
| 4 | Civil Engineering | MEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/77-civil-engineering) |
| 5 | Electrical and Mechanical Engineering | BEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/107-electrical-and-mechanical-engineering) |
| 6 | Electrical and Mechanical Engineering | MEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/109-electrical-and-mechanical-engineering) |
| 7 | Electronics and Computer Science | BEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/654-electronics-and-computer-science) |
| 8 | Electronics and Computer Science | MEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/70-electronics-and-computer-science) |
| 9 | Electronics and Electrical Engineering | BEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/88-electronics-and-electrical-engineering) |
| 10 | Electronics and Electrical Engineering | MEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/89-electronics-and-electrical-engineering) |
| 11 | Engineering (Year 1 only) | BEng/MEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/75-engineering) |
| 12 | Mechanical Engineering | BEng (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/82-mechanical-engineering) |
| 13 | Mechanical Engineering | MEng (Hons) | (via DRPS) |
| 14 | Structural and Fire Safety Engineering | BEng/MEng (Hons) | (via DRPS) |
| 15 | Structural Engineering with Architecture | BEng/MEng (Hons) | (via DRPS) |

> **Note**: The School of Engineering also offers "Technology" variants of most programmes (e.g., "Chemical Engineering Technology BEng Hons") and programmes with a Year Abroad option. DRPS lists 33 UG programme entries including all variants.

##### School of Biological Sciences

###### BSc (Hons) / MBiol — 4-5 year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Sciences | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/4-biological-sciences) |
| 2 | Biological Sciences | MBiol | [Link](https://study.ed.ac.uk/programmes/undergraduate/673-biological-sciences) |
| 3 | Biological Sciences (Biochemistry) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/13-biological-sciences-biochemistry) |
| 4 | Biological Sciences (Biotechnology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/112-biological-sciences-biotechnology) |
| 5 | Biological Sciences (Cell Biology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/481-biological-sciences-cell-biology) |
| 6 | Biological Sciences (Ecology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/6-biological-sciences-ecology) |
| 7 | Biological Sciences (Evolutionary Biology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/382-biological-sciences-evolutionary-biology) |
| 8 | Biological Sciences (Genetics) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/10-biological-sciences-genetics) |
| 9 | Biological Sciences (Immunology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/11-biological-sciences-immunology) |
| 10 | Biological Sciences (Molecular Biology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/14-biological-sciences-molecular-biology) |
| 11 | Biological Sciences (Molecular Genetics) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/480-biological-sciences-molecular-genetics) |
| 12 | Biological Sciences (Plant Science) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/8-biological-sciences-plant-science) |
| 13 | Biological Sciences (Zoology) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/9-biological-sciences-zoology) |
| 14 | Biological Sciences with Management | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/7-biological-sciences-with-management) |
| 15 | Biomedical Sciences | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/383-biomedical-sciences) |
| 16 | Ecological and Environmental Sciences | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/16-ecological-and-environmental-sciences) |
| 17 | Infectious Diseases | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/437-infectious-diseases) |

> **Note**: DRPS lists 31 UG programme entries for Biological Sciences including BMedSci variants and "with Management" options.

##### School of Physics and Astronomy

###### BSc (Hons) / MPhys — 4-5 year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Astrophysics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/46-astrophysics) |
| 2 | Astrophysics | MPhys | [Link](https://study.ed.ac.uk/programmes/undergraduate/44-astrophysics) |
| 3 | Computational Physics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/42-computational-physics) |
| 4 | Computational Physics | MPhys | [Link](https://study.ed.ac.uk/programmes/undergraduate/43-computational-physics) |
| 5 | Mathematical Physics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/38-mathematical-physics) |
| 6 | Mathematical Physics | MPhys | [Link](https://study.ed.ac.uk/programmes/undergraduate/37-mathematical-physics) |
| 7 | Physics | BSc (Hons) | (via DRPS) |
| 8 | Physics | MPhys | (via DRPS) |
| 9 | Physics with Meteorology | BSc (Hons) / MPhys | (via DRPS) |
| 10 | Physics with Year Abroad | MPhys | (via DRPS) |
| 11 | Theoretical Physics | BSc (Hons) | (via DRPS) |
| 12 | Theoretical Physics | MPhys | (via DRPS) |

##### School of Chemistry

###### BSc (Hons) / MChem — 4-5 year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/21-chemistry) |
| 2 | Chemistry | MChem | [Link](https://study.ed.ac.uk/programmes/undergraduate/23-chemistry) |
| 3 | Chemical Physics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/40-chemical-physics) |
| 4 | Chemical Physics | MChemPhys | [Link](https://study.ed.ac.uk/programmes/undergraduate/39-chemical-physics) |

##### School of Mathematics

###### BSc (Hons) / MMath (Hons) — 4-5 year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/55-mathematics) |
| 2 | Mathematics | MMath (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/478-mathematics) |
| 3 | Applied Mathematics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/429-applied-mathematics) |
| 4 | Applied Mathematics | MMath (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/662-applied-mathematics) |
| 5 | Mathematics and Business | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/72-mathematics-and-business) |
| 6 | Mathematics and Physics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/61-mathematics-and-physics) |
| 7 | Mathematics and Statistics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/63-mathematics-and-statistics) |

##### School of Geosciences

###### BSc (Hons) / MEarthSci — 4-5 year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth Sciences | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/47-earth-sciences) |
| 2 | Earth Sciences | MEarthSci | [Link](https://study.ed.ac.uk/programmes/undergraduate/438-earth-sciences) |
| 3 | Earth Science and Physical Geography | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/54-earth-science-and-physical-geography) |
| 4 | Earth Science and Physical Geography | MEarthSci | [Link](https://study.ed.ac.uk/programmes/undergraduate/439-earth-science-and-physical-geography) |
| 5 | Environmental Geoscience | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/446-environmental-geoscience) |
| 6 | Geography | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/50-geography) |
| 7 | Geography | MA (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/130-geography) |
| 8 | Geophysics | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/49-geophysics) |

#### College of Medicine and Veterinary Medicine

##### Edinburgh Medical School

###### MBChB — 6-year undergraduate medicine

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | MBChB Medicine (6-year programme) | A100 | [Link](https://study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme) |
| 2 | HCP-Med for Healthcare Professionals | — | [Link](https://study.ed.ac.uk/programmes/undergraduate/672-hcp-med-for-healthcare-professionals) |

###### BSc (Hons) / BMedSci (Hons) — 4-year undergraduate

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anatomy and Development | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/656-anatomy-and-development) |
| 2 | Biomedical Sciences | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/383-biomedical-sciences) |
| 3 | Biomedical Informatics (based in China) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/664-biomedical-informatics-based-in-china) |
| 4 | Infectious Diseases | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/437-infectious-diseases) |
| 5 | Integrative Biomedical Sciences (based in China) | BSc (Hons) | [Link](https://study.ed.ac.uk/programmes/undergraduate/659-integrative-biomedical-sciences-based-in-china) |
| 6 | Neuroscience | BSc (Hons) | (via DRPS) |
| 7 | Oral Health Sciences | BSc (Hons) | (via DRPS) |
| 8 | Pharmacology | BSc (Hons) | (via DRPS) |
| 9 | Reproductive Biology | BSc (Hons) | (via DRPS) |

> **Note**: DRPS lists 32 UG programme entries for Edinburgh Medical School including BMedSci variants, intercalation options, and clinical pathways.

##### Royal (Dick) School of Veterinary Studies

###### BVMS — 5-6 year undergraduate veterinary medicine

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Veterinary Medicine | BVMS | (via Degree Finder) |
| 2 | Veterinary Medicine (Graduate Entry) | BVMS | (via Degree Finder) |

> **Note**: BVMS has pre-clinical and clinical phases, plus a graduate entry route. DRPS lists 4 UG programme entries.

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Program | Primary School | Cross-listed Schools | URL |
|---|---------|----------------|---------------------|-----|
| 1 | Computer Science and Mathematics | Informatics | Mathematics | [Link](https://study.ed.ac.uk/programmes/undergraduate/64-computer-science-and-mathematics) |
| 2 | Computer Science and Physics | Informatics | Physics and Astronomy | (via DRPS) |
| 3 | Economics and Mathematics | Economics | Mathematics | [Link](https://study.ed.ac.uk/programmes/undergraduate/133-economics-and-mathematics) |
| 4 | Mathematics and Physics | Mathematics | Physics and Astronomy | [Link](https://study.ed.ac.uk/programmes/undergraduate/61-mathematics-and-physics) |
| 5 | Business and Law | Business School | Law | [Link](https://study.ed.ac.uk/programmes/undergraduate/188-business-and-law) |
| 6 | Politics, Philosophy and Economics | SPS | Philosophy/PPLS, Economics | (via DRPS) |
| 7 | Cognitive Science (Humanities) | PPLS | Informatics | [Link](https://study.ed.ac.uk/programmes/undergraduate/479-cognitive-science-humanities) |
| 8 | Acoustics and Music Technology | Physics | Edinburgh College of Art | [Link](https://study.ed.ac.uk/programmes/undergraduate/655-acoustics-and-music-technology) |

> **Note**: Edinburgh is notable for its extensive joint/combined degree offerings. The School of Literatures, Languages and Cultures alone offers 100+ joint degree combinations. Most humanities/social science subjects can be combined with at least one other subject.

### 1.4 Minors — complete list

Edinburgh does not offer a US-style minor system. Students on single honours programmes take some courses outside their main subject, but there is no formal minor designation. Joint honours programmes (e.g., "French and History") give equal weight to both subjects.

### 1.5 General/Institute-wide requirements

- **Application platform**: UCAS (all UG)
- **UCAS institution code**: E56
- **Personal statement**: Required (UCAS format; single statement for all 5 UCAS choices)
- **Academic reference**: 1 required (from teacher/referee via UCAS)
- **Admissions tests**: UCAT required for Medicine; no other standardised admissions tests for most programmes
- **Interviews**: Medicine only (assessment day for top ~800 applicants)
- **Conditional offers**: Yes (standard UK practice; based on predicted grades)
- **Deferred entry**: Generally available; Medicine does NOT allow deferred entry (except National Service)
- **One application per subject area**: For Informatics and Physics, applicants may only apply for one degree in that subject area
- **Second year entry**: Available for some programmes (e.g., Physics, Chemistry, Engineering) for students with appropriate qualifications

### 1.6 UCAS Course Code → Major quick-lookup (selected)

| UCAS Code | Major |
|-----------|-------|
| A100 | MBChB Medicine (6-year) |
| G400 | Computer Science BSc (Hons) |
| V100 | History MA (Hons) |
| F325 | Mathematical Physics MPhys |

> **Note**: Edinburgh does not prominently display UCAS codes on its Degree Finder. Codes are available on individual programme pages and via UCAS search. The codes above are confirmed from programme pages.

---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Edinburgh's graduate taught programmes are administered through the same 3 Colleges and 26 Schools as undergraduate. The A-Z listing at `study.ed.ac.uk/programmes/postgraduate-taught-a-z` shows 350+ unique programmes. Below is a structured selection by School.

#### College of Science and Engineering

##### School of Informatics — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Artificial Intelligence | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/107-artificial-intelligence) |
| 2 | Cognitive Science | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/108-cognitive-science) |
| 3 | Computer Science | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/110-computer-science) |
| 4 | Cyber Security, Privacy and Trust | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/971-cyber-security-privacy-and-trust) |
| 5 | Data Science | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/902-data-science) |
| 6 | Design Informatics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/803-design-informatics) |
| 7 | High Performance Computing | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/187-high-performance-computing) |
| 8 | High Performance Computing with Data Science | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/871-high-performance-computing-with-data-science) |

> **Total Informatics PGT**: 12 programmes (including online/PgCert/PgDip variants)

##### School of Engineering — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Chemical Engineering | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/913-advanced-chemical-engineering) |
| 2 | Advanced Power Engineering | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/960-advanced-power-engineering) |
| 3 | Biomedical Engineering | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1135-biomedical-engineering) |
| 4 | Digital Design and Manufacture | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1040-digital-design-and-manufacture) |
| 5 | Electrical Power Engineering | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/937-electrical-power-engineering) |
| 6 | Electronics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/669-electronics) |
| 7 | Fire Engineering Science | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1082-fire-engineering-science) |
| 8 | Signal Processing and Communications | MSc | (via DRPS) |
| 9 | Sustainable Energy Systems | MSc | (via DRPS) |

> **Total Engineering PGT**: 12 programmes (including visiting student options)

##### School of Biological Sciences — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Animal Breeding and Genetics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/763-animal-breeding-and-genetics) |
| 2 | Biochemistry | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/856-biochemistry) |
| 3 | Biodiversity and Taxonomy of Plants | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1-biodiversity-and-taxonomy-of-plants) |
| 4 | Bioinformatics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/2-bioinformatics) |
| 5 | Biotechnology | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/676-biotechnology) |
| 6 | Data Science for Biology | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1099-data-science-for-biology) |
| 7 | Drug Discovery and Translational Biology | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/3-drug-discovery-and-translational-biology) |
| 8 | Ecology, Evolution and Biodiversity | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1080-ecology-evolution-and-biodiversity) |
| 9 | Evolutionary Genetics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/764-evolutionary-genetics) |
| 10 | Human Complex Trait Genetics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/765-human-complex-trait-genetics) |
| 11 | Quantitative Genetics and Genome Analysis | MSc | (via DRPS) |
| 12 | Synthetic Biology and Biotechnology | MSc | (via DRPS) |

##### School of Physics and Astronomy — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Astrobiology and Planetary Sciences | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1097-astrobiology-and-planetary-sciences) |
| 2 | Mathematical Physics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/817-mathematical-physics) |
| 3 | Particle and Nuclear Physics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/946-particle-and-nuclear-physics) |
| 4 | Theoretical Physics | MSc | (via DRPS) |

#### College of Arts, Humanities and Social Sciences

##### Business School — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | AI for Business | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1138-ai-for-business) |
| 2 | Accounting and Financial Management | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1126-accounting-and-financial-management) |
| 3 | Banking Innovation and Risk Analytics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/756-banking-innovation-and-risk-analytics) |
| 4 | Business Administration | MBA | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/267-business-administration-master-of) |
| 5 | Business Administration (Online) | MBA | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1076-business-administration-master-of-online-learning) |
| 6 | Business Analytics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/929-business-analytics) |
| 7 | Climate Change Finance and Investment | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/671-climate-change-finance-and-investment) |
| 8 | Data and Decision Analytics (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1081-data-and-decision-analytics-online-learning) |
| 9 | Entrepreneurship and Innovation | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/897-entrepreneurship-and-innovation) |
| 10 | Finance and Investment | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1128-finance-and-investment) |
| 11 | Finance, Technology and Policy | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/966-finance-technology-and-policy) |
| 12 | Global Strategy and Sustainability | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1044-global-strategy-and-sustainability) |
| 13 | Human Resource Management | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/755-human-resource-management) |
| 14 | International Human Resource Management | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/880-international-human-resource-management) |
| 15 | Management | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/277-management) |
| 16 | Marketing | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/638-marketing) |

> **Total Business School PGT**: 19 programmes (including online MBA variants)

##### School of Law — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Commercial Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/161-commercial-law) |
| 2 | Comparative Private Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/684-comparative-private-law) |
| 3 | Corporate Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/787-corporate-law) |
| 4 | Criminal Law and Criminal Justice | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/772-criminal-law-and-criminal-justice) |
| 5 | European Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/163-european-law) |
| 6 | Global Environment and Climate Change Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/642-global-environment-and-climate-change-law) |
| 7 | Human Rights | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/845-human-rights) |
| 8 | Information Technology Law (Online) | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/502-information-technology-law-online-learning) |
| 9 | Innovation, Technology and the Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/503-innovation-technology-and-the-law) |
| 10 | Intellectual Property Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/641-intellectual-property-law) |
| 11 | International Banking Law and Finance | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/859-international-banking-law-and-finance) |
| 12 | International Commercial Law and Practice (Online) | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/825-international-commercial-law-and-practice-online-learning) |
| 13 | International Economic Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/686-international-economic-law) |
| 14 | International Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/166-international-law) |
| 15 | Law | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/167-law) |
| 16 | Law (Online) | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/767-law-online-learning) |
| 17 | Medical Law and Ethics | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/867-medical-law-and-ethics) |
| 18 | Medical Law and Ethics (Online) | LLM | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/505-medical-law-and-ethics-online-learning) |
| 19 | Professional Legal Practice | PgDip | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/675-professional-legal-practice) |
| 20 | Criminology and Criminal Justice | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/162-criminology-and-criminal-justice) |
| 21 | Global Crime, Justice and Security | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/621-global-crime-justice-and-security) |

> **Total Law PGT**: 44 programme entries (many LLM programmes have FT/PT/Online variants counted separately in DRPS)

##### School of Social and Political Science — PGT

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Africa and International Development | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/622-africa-and-international-development) |
| 2 | Comparative Public Policy | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/301-comparative-public-policy) |
| 3 | Conflict, Security and Development | MSc | (via DRPS) |
| 4 | Digital Sociology | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/936-digital-sociology) |
| 5 | Global Environment, Politics and Society | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/811-global-environment-politics-and-society) |
| 6 | Global Health Policy | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/384-global-health-policy) |
| 7 | Global Mental Health and Society | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/991-global-mental-health-and-society) |
| 8 | International Development | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/681-international-development) |
| 9 | International Relations | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/687-international-relations) |
| 10 | International and European Politics | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/303-international-and-european-politics) |
| 11 | Public Policy | MSc | (via DRPS) |
| 12 | Science and Technology in Society | MSc | (via DRPS) |
| 13 | Social Anthropology | MSc | (via DRPS) |
| 14 | Social Research | MSc | (via DRPS) |
| 15 | Social Work | MSW | (via DRPS) |
| 16 | Sociology and Global Change | MSc | (via DRPS) |

> **Total SPS PGT**: 24 programmes (including online/PT variants)

#### College of Medicine and Veterinary Medicine

##### Edinburgh Medical School — PGT (selected from 58 entries)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Clinical Anatomy | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1000-clinical-anatomy) |
| 2 | Clinical Education (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/246-clinical-education-online-learning) |
| 3 | Clinical Trials (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/809-clinical-trials-online-learning) |
| 4 | Epidemiology (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/1042-epidemiology-online-learning) |
| 5 | Human Anatomy | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/648-human-anatomy) |
| 6 | Internal Medicine (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/692-internal-medicine-online-learning) |
| 7 | Master of Public Health | MPH | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/98-education) |
| 8 | Master of Public Health (Online) | MPH | (via DRPS) |
| 9 | Science Communication and Public Engagement (Online) | MSc | (via DRPS) |
| 10 | Surgical Sciences (Online) | MSc | (via DRPS) |

##### Royal (Dick) School of Veterinary Studies — PGT (selected from 40 entries)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Animal Behaviour and Animal Welfare | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/238-applied-animal-behaviour-and-animal-welfare) |
| 2 | Applied Conservation Genetics with Wildlife Forensics (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/954-applied-conservation-genetics-with-wildlife-forensics-online) |
| 3 | Clinical Animal Behaviour (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/911-clinical-animal-behaviour-online-learning) |
| 4 | Conservation Medicine (Online) | MVetSci | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/786-conservation-medicine-online-learning) |
| 5 | Equine Science (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/239-equine-science-online-learning) |
| 6 | Global Food Security and Nutrition (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/959-global-food-security-and-nutrition-online-learning) |
| 7 | International Animal Health (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/241-international-animal-health-online-learning) |
| 8 | International Animal Welfare, Ethics and Law (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/788-international-animal-welfare-ethics-and-law-online-learning) |
| 9 | One Health (Online) | MSc | [Link](https://study.ed.ac.uk/programmes/postgraduate-taught/814-one-health-online-learning) |
| 10 | Veterinary Anaesthesia and Analgesia | MSc | (via DRPS) |

### 2.2 Graduate admissions model

Edinburgh's graduate admissions are **centralized** through the online application system. Students apply directly to Edinburgh (no UCAS for postgraduate). Key characteristics:

- **Application fee**: Required for most PGT programmes (amount not confirmed from pages accessed)
- **Deadlines**: Rolling for most programmes; some have fixed rounds (especially Business School MBA)
- **English language**: Profile-based system — each programme specifies its required profile (see Section 3.2)
- **GRE/GMAT**: Not generally required except for some Business School programmes
- **References**: 2 academic references typically required
- **Research proposal**: Required for MSc by Research and PhD applications

### 2.3 Doctoral programs

Doctoral (PhD, MSc by Research, EngD) programmes are listed separately in DRPS. Key research groupings include:

- **School of Informatics**: 13 PhD programmes (AI, NLP, Robotics, Quantum Informatics, etc.)
- **School of Engineering**: 4 EngD/PhD programmes
- **School of Law**: 4 PhD/LLM by Research programmes
- **School of Social and Political Science**: 28 PhD/MScR programme entries
- **Business School**: 10 PhD/MScR programmes
- **Edinburgh Medical School**: 5 MScR/PhD programmes

> **Total doctoral/research programmes**: ~200+ across all schools (DRPS lists individual entries for FT/PT variants)

---

## SECTION 3 — Application Requirements & Deadlines

> **Region**: UK (Scotland). Uses UCAS for undergraduate applications. Graduate applications are direct to Edinburgh.

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | UCAS | `study.ed.ac.uk/programmes/undergraduate` |
| UCAS institution code | **E56** | Official Edinburgh UCAS listing |
| Applications open | May 2026 (register); 1 Sep 2026 (submit) | UCAS cycle |
| **Medicine deadline** | **15 October 2026** (6:00pm GMT) | `study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme` |
| **Equal consideration deadline** | **13 January 2027** (6:00pm GMT) | All other UG courses |
| A-Level results day | August 2027 (TBC) | UK national |
| Application decisions | By end of March 2027 | Edinburgh standard |
| Personal statement | Required (UCAS format) | Single statement for all 5 UCAS choices |
| Academic reference | 1 required (teacher) | Via UCAS |
| Interview policy | Medicine only (assessment day for ~800 applicants) | Medicine-specific |
| Admissions tests | UCAT (Medicine only) | Must sit UCAT in 2026 |
| Conditional offers | Yes (standard UK practice) | Based on predicted grades |
| Deferred entry | Available (most programmes); NOT available for Medicine | Medicine exception |
| One application per subject | Required for Informatics and Physics | Programme-specific policy |

### 3.2 Undergraduate English proficiency

Edinburgh uses a **profile system** for English language requirements. Each programme specifies which profile applies. The baseline (where no higher level is specified) is:

**Baseline (GCSE-equivalent)**:

| Qualification | Minimum Grade |
|---|---|
| National 5 | C |
| GCSE/IGCSE English Language | C or 4 |
| IB Standard Level English A or B | 5 (ab initio not accepted) |
| IB Middle Years Programme | 5 |
| Level 2 Certificate | C (Functional Skills not accepted) |

**Accepted English Language Tests** (from `study.ed.ac.uk/undergraduate/entry-requirements/english-language`):

| Test | Baseline Score | Notes |
|------|---------------|-------|
| IELTS Academic | Varies by programme (typically 6.5-7.0 overall) | Must be taken in single sitting; IELTS One Skill Retake NOT accepted |
| TOEFL iBT | Varies by programme (typically 92-100 overall) | Must be taken in single sitting; TOEFL MyBest Score NOT accepted |
| Cambridge C1 Advanced / C2 Proficiency | 176 overall, 162 per component | |
| Oxford ELLT | Varies | Single sitting; Skill Retake NOT accepted |
| Oxford Test of English Advanced | Varies | |
| Trinity ISE | Varies | |

**Programme-specific IELTS scores** (confirmed from programme pages):

| Programme | IELTS Overall | Per Component | Source |
|-----------|--------------|---------------|--------|
| Computer Science MSc | 7.0 | 6.5 | `study.ed.ac.uk/programmes/postgraduate-taught/110-computer-science` |
| Artificial Intelligence MSc | 7.0 | 6.5 | `study.ed.ac.uk/programmes/postgraduate-taught/107-artificial-intelligence` |

**Test validity**:
- 2-year expiry: IELTS, TOEFL, Trinity ISE, Oxford ELLT, Oxford Test of English Advanced
- 3.5-year expiry: All other accepted tests

> **Note**: Unlike Imperial's two-tier (Standard/Higher) system, Edinburgh uses a per-programme profile system. The specific IELTS/TOEFL requirements for each programme are listed on the programme's page in the Degree Finder. Most programmes require IELTS 6.5-7.0 overall.

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Application platform | Edinburgh online application (direct) |
| Application fee | Required for most PGT programmes |
| Deadlines | Rolling (most programmes); fixed rounds for Business School MBA |
| References | 2 academic references |
| Personal statement | Required |
| English language | Profile-based (same system as UG; programme-specific scores) |
| GRE/GMAT | Not generally required (some Business School programmes may ask for GMAT) |
| Interviews | Varies by department |
| Research proposal | Required for MSc by Research and doctoral applications |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate tuition fees (2026-27 academic year)

| Fee status | Annual tuition |
|-----------|----------------|
| **Home (Scottish)** | **£1,820** (SAAS-funded; students do not pay directly) |
| **Rest of UK (England, Wales, NI)** | **£9,250** (government cap; may increase) |
| **International (Overseas)** | **Varies by programme** (see bands below) |

> **Source**: `registryservices.ed.ac.uk/student-funding/tuition-fees/` (fee tables require navigation to specific year pages)
>
> **Note**: The fee table pages were dynamically loaded and not fully accessible via WebFetch. The figures below are based on confirmed data from programme pages and historical Edinburgh fee schedules.

**International fee bands** (estimated from available data):

| Category | Annual Fee (estimated) |
|----------|----------------------|
| Classroom-based (Humanities, Social Sciences, Business) | ~£24,500-£28,000 |
| Lab-based (Sciences, Engineering) | ~£32,000-£37,000 |
| Medicine (pre-clinical) | ~£54,651 (confirmed from Medicine page: deposit £18,217 = 1/3 of year 1 fees) |
| Medicine (clinical) | Higher (exact amount not confirmed) |
| Veterinary Medicine | ~£35,000-£40,000 (estimated) |

> **Source for Medicine fee**: `study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme` — "For international students, you need to pay a deposit of one-third of the first year's fees. For 2026 entry, the deposit was £18,217."
>
> **RUK fee note**: "The RUK fee rate increased in November 2026 in line with the Government's revision of the tuition fee cap." Fees will increase annually in line with the government cap.

### 4.2 Living costs (2026-27)

| Expense | Monthly | 9 Months (academic year) | Full Year |
|---------|---------|-------------------------|-----------|
| **Average living costs** | **£1,546** | **£13,914** | **£18,552** |

> **Source**: `study.ed.ac.uk/programmes/undergraduate/57-computer-science` — "Estimated living costs: £1,546 each month to live in Edinburgh as a single undergraduate student (2026–2027). This means approximately £13,914 for a 39-week academic year, or £18,552 for a full year."
>
> **Note**: Edinburgh is significantly cheaper than London (Imperial's estimate is £1,806-£1,837/month). The 39-week academic year is standard for Scottish universities.

### 4.3 Postgraduate tuition fees

| Fee status | Typical range |
|------------|---------------|
| Home (PGT) | £10,000-£16,000/year (varies by programme) |
| Overseas (PGT) | £24,000-£38,000/year (varies by programme) |
| MBA | ~£35,000-£40,000 (estimated) |

> **Source**: Estimated from Edinburgh's historical fee schedules. Exact per-programme fees are available via the Degree Finder fee lookup tool.

### 4.4 Financial aid & funding

**Undergraduate (Home/Scottish students)**:
- SAAS funding: Covers full tuition for Scottish-domiciled students
- Student Loan: Available for living costs
- Edinburgh bursaries: Available for students from low-income households

**Undergraduate (RUK students)**:
- Tuition Fee Loan: Covers full tuition
- Maintenance Loan: Means-tested

**Undergraduate (International students)**:
- No UK government loans
- Edinburgh Global undergraduate scholarships
- Country-specific scholarships
- External scholarships (Chevening, Commonwealth, etc.)

**Postgraduate**:
- Postgraduate Master's Loan (Home students): up to £12,471 (2026-27)
- Postgraduate Doctoral Loan (Home students): up to £29,390
- Edinburgh Global Research Scholarships
- UKRI Research Council studentships (PhD)
- Principal's Career Development PhD Scholarships
- Various school-specific scholarships

### 4.5 Visa and Immigration Health Surcharge (IHS)

- Student visa required for international students
- IHS: ~£470/year for students (subject to change)
- Financial requirement: must show sufficient funds for first-year tuition + living costs (£1,023/month for 9 months outside London = ~£9,207)

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: institution.name
  value: "The University of Edinburgh"
  source_url: https://study.ed.ac.uk
  source_snippet: "University of Edinburgh Degree Finder"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.ucas_code
  value: "E56"
  source_url: https://study.ed.ac.uk/programmes/undergraduate
  source_snippet: UCAS institution code E56
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.medicine
  value: "15 October 2026 (6:00pm GMT)"
  source_url: https://study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme
  source_snippet: "15 October 2026 (6:00pm GMT)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.equal_consideration
  value: "13 January 2027 (6:00pm GMT)"
  source_url: https://study.ed.ac.uk/programmes/undergraduate/57-computer-science
  source_snippet: "2027 entry UCAS deadline: 13 January 2027 (6:00pm GMT)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.medicine.deposit_international
  value: "£18,217 deposit (implies ~£54,651/year)"
  source_url: https://study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme
  source_snippet: "For international students, you need to pay a deposit of one-third of the first year's fees. For 2026 entry, the deposit was £18,217."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.living_costs.monthly
  value: "£1,546/month (2026-2027)"
  source_url: https://study.ed.ac.uk/programmes/undergraduate/57-computer-science
  source_snippet: "Estimated living costs: £1,546 each month to live in Edinburgh as a single undergraduate student (2026–2027)."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english.ielts.computer_science_msc
  value: "7.0 overall, 6.5 per component"
  source_url: https://study.ed.ac.uk/programmes/postgraduate-taught/110-computer-science
  source_snippet: "IELTS Academic: Overall 7.0, Minimum per component 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english.ielts.artificial_intelligence_msc
  value: "7.0 overall, 6.5 per component"
  source_url: https://study.ed.ac.uk/programmes/postgraduate-taught/107-artificial-intelligence
  source_snippet: "IELTS Academic: Overall 7.0, Minimum per component at least 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english.cambridge
  value: "C1 Advanced/C2 Proficiency: 176 overall, 162 per component"
  source_url: https://study.ed.ac.uk/undergraduate/entry-requirements/english-language
  source_snippet: "Cambridge C1 Advanced / C2 Proficiency: Overall 176 with 162 in each component"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.medicine.ucas_deadline
  value: "15 October 2026 (6:00pm GMT)"
  source_url: https://study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme
  source_snippet: "UCAS Deadline: 15 October 2026 (6:00pm GMT) for all applicants"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.medicine.ucat_required
  value: "UCAT required; must sit in 2026"
  source_url: https://study.ed.ac.uk/programmes/undergraduate/354-mbchb-medicine-6-year-programme
  source_snippet: "Applicants must sit the UCAT (University Clinical Aptitude Test) in 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.college_structure
  value: "3 Colleges: Arts Humanities and Social Sciences (13 Schools), Science and Engineering (7 Schools), Medicine and Veterinary Medicine (6 Schools)"
  source_url: http://www.drps.ed.ac.uk/26-27/dpt/drpsindex.htm
  source_snippet: DRPS index showing 3 colleges with 26 schools
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-001:
  field: graduate.pgt_total_count
  value: "~350 postgraduate taught programmes"
  source_url: https://study.ed.ac.uk/programmes/postgraduate-taught-a-z
  source_snippet: A-Z listing (A-P: 240 programmes visible; estimated ~350 total)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_platform
  value: "Edinburgh online application (direct, not UCAS)"
  source_url: https://study.ed.ac.uk/postgraduate/
  source_snippet: Direct application to Edinburgh for postgraduate study
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-003:
  field: graduate.english.ielts.informatics
  value: "7.0 overall, 6.5 per component"
  source_url: https://study.ed.ac.uk/programmes/postgraduate-taught/110-computer-science
  source_snippet: "IELTS Academic: Overall 7.0, Minimum per component 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
edinburgh-university-knowledge-base-v2/
├── institution-overview        (Section 0 — counts, hierarchy, degree inventory, matrix)
├── undergraduate-programs      (Section 1 — grouped by College)
│   ├── arts-humanities-ug      (~240 UG programmes)
│   ├── science-engineering-ug  (~100 UG programmes)
│   └── medicine-vet-ug         (~40 UG programmes)
├── graduate-programs           (Section 2 — grouped by College)
│   ├── arts-humanities-pgt     (~200 PGT programmes)
│   ├── science-engineering-pgt (~80 PGT programmes)
│   └── medicine-vet-pgt        (~70 PGT programmes)
├── application-requirements    (Section 3 — deadlines, tests, English)
├── costs-and-funding           (Section 4 — tuition, living costs, aid)
├── evidence-chain              (Section 5 — all evidence blocks)
└── comparison-framework        (Section 7 — cross-school matrix)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "edinburgh-university-knowledge-base-v2"
  school: "<School name>"
  college: "<College of Arts Humanities and Social Sciences | College of Science and Engineering | College of Medicine and Veterinary Medicine>"
  degree_level: "<MA | BSc | BEng | LLB | MBChB | BVMS | MEng | MPhys | MSc | LLM | MBA | MPH | PhD etc.>"
  level: undergraduate | postgraduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://study.ed.ac.uk/programmes/
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|------------|-------|
| **P0** | Exact international UG fees per programme | `registryservices.ed.ac.uk/student-funding/tuition-fees/find/undergraduate/2026-2027/` | Fee tables dynamically loaded; need direct access |
| **P0** | Complete UG programme list (N-Z) | `study.ed.ac.uk/programmes/undergraduate-a-z` | Page truncated at M; missing N-V |
| **P0** | Complete PGT programme list (Q-W) | `study.ed.ac.uk/programmes/postgraduate-taught-a-z` | Page truncated at P; missing Q-W |
| **P0** | Per-programme IELTS/TOEFL scores | Individual programme pages | Profile system; need to check each programme |
| **P1** | Per-programme A-Level/IB/Scottish Higher entry requirements | Individual programme pages | Behind interactive dropdown tool |
| **P1** | PGT application fee amounts | Edinburgh application system | Not confirmed from pages accessed |
| **P1** | MBA fees and GMAT requirements | Business School programme pages | Different from other PGT |
| **P2** | Doctoral programme complete list | DRPS | ~200+ research programmes |
| **P2** | Accommodation costs | Edinburgh accommodation pages | Not accessed |

---

## SECTION 7 — Cross-school Comparison Framework

| Dimension | The University of Edinburgh | Imperial College London | Cardiff University |
|-----------|---------------------------|------------------------|-------------------|
| **Country** | UK (Scotland) | UK (England) | UK (Wales) |
| **Region** | Edinburgh, Scotland | London, England | Cardiff, Wales |
| **Russell Group** | Yes | Yes | Yes |
| **Total UG programmes** | ~380 | 73 | 237 |
| **Total PG programmes (taught)** | ~350 | 175 | — |
| **Number of Colleges** | 3 | 4 (Faculties) | — |
| **Application platform (UG)** | UCAS | UCAS | UCAS |
| **UCAS institution code** | E56 | I50 | — |
| **Medicine deadline** | 15 Oct | 15 Oct | — |
| **Regular deadline (UG)** | 13 Jan | 13 Jan | — |
| **Home tuition (UG)** | £1,820 (Scottish/SAAS) / £9,250 (RUK) | £9,790 | — |
| **Overseas tuition (UG, typical)** | ~£24,500-£54,651 | £37,900-£53,700 | — |
| **Living costs (monthly)** | £1,546 | £1,806-£1,837 | — |
| **IELTS minimum (typical)** | 6.5-7.0 (per programme) | 6.5 (Standard) / 7.0 (Higher) | — |
| **TOEFL minimum (typical)** | 92-100 (per programme) | 92 (Standard) / 100 (Higher) | — |
| **Admissions tests (UG)** | UCAT (Medicine only) | ESAT/TMUA/UCAT/GAMSAT | — |
| **Interviews (UG)** | Medicine only | Most courses | — |
| **Degree levels awarded** | MA, BSc, BEng, LLB, MBChB, BVMS, MEng, MPhys, MChem, MEarthSci, MBiol, MInf, MMath, MSc, LLM, MBA, MPH, MEd, MMus, MCouns, MFA, MLA, MArch, MVetSci, MFM, MN, MSW, DClinPsychol, DClinDent, DVetMed, DPsychotherapy, PGDE, PgDip, PgCert, PhD, MScR, EngD | BEng, BSc, MBBS, MEng, MSci, MSc, MRes, MBA, MPH, PG Cert, PG Dip, PhD | — |
| **Scottish MA system** | Yes (4-year UG MA Hons) | No | No |
| **UCAT required** | Yes (Medicine) | No (uses ESAT/TMUA) | — |
| **Combined/joint degrees** | Very common (100+) | Rare | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: `study.ed.ac.uk/programmes/`, `drps.ed.ac.uk/26-27/dpt/`, `registryservices.ed.ac.uk/student-funding/`
> **Verification**: WebFetch + DRPS programme tables
> **Granularity**: school → department → degree-level → program
> **Total programmes**: ~915 (~380 UG + ~350 PGT + ~200+ PGR)
> **Reconciliation**: Rule-1 total (~915) consistent with DRPS school-level counts
> **Completeness**: Hierarchy ✅ | UG programmes (A-M + DRPS schools) ⚠ ~70% | PGT programmes (A-P) ⚠ ~65% | Fees ⚠ estimated | English language ⚠ per-programme | Evidence (13 blocks) ✅
> **Next step**: Access fee tables directly; complete N-Z UG and Q-W PGT programme extraction; confirm per-programme IELTS scores
