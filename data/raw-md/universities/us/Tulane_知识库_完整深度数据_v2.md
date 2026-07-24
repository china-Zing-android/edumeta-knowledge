# Tulane University Admissions Knowledge Base - Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school - department - degree-level - program
> **Document version**: v2.0 (deep)

---

## 0. 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BSM/B.Arch/BSPH/BIS) | 104 |
| 本科辅修 (Minor) | 89 |
| 本科证书 (Certificate) | 16 |
| 研究生学位项目 (MA/MS/PhD/MBA/MPH/JD/MD/etc.) | 192 |
| 研究生证书 (Graduate Certificate) | 43 |
| **学位项目总计 (UG + Grad)** | **452** |
| 学院总数 | 9 |

### 0.2 学院/系层级结构

```
Tulane University
+- Newcomb-Tulane College (统一本科生学院) [学院]
+- School of Liberal Arts (UG/Grad, 138 programs) [学院]
|   +- liberal-arts (135 programs) [系]
|   +- medicine (1 programs) [系]
|   +-- newcomb-tulane (2 programs) [系]
+- School of Science and Engineering (UG/Grad, 84 programs) [学院]
|   +- architecture (1 programs) [系]
|   +- newcomb-tulane (1 programs) [系]
|   +-- science-engineering (82 programs) [系]
+- School of Professional Advancement (UG/Grad, 73 programs) [学院]
|   +- medicine (1 programs) [系]
|   +-- professional-advancement (72 programs) [系]
+- Celia Scott Weatherhead School of Public Health and Tropical Medicine (UG/Grad, 50 programs) [学院]
|   +-- public-health-tropical-medicine (50 programs) [系]
+- A. B. Freeman School of Business (UG/Grad, 31 programs) [学院]
|   +-- business (31 programs) [系]
+- School of Medicine (Grad, 31 programs) [学院]
|   +-- medicine (31 programs) [系]
+- School of Architecture and Built Environment (UG/Grad, 21 programs) [学院]
|   +-- architecture (21 programs) [系]
+- School of Law (Grad, 16 programs) [学院]
|   +-- law (16 programs) [系]
+- School of Social Work (UG/Grad, 6 programs) [学院]
|   +- public-health-tropical-medicine (1 programs) [系]
|   +-- social-work (5 programs) [系]
+- (9 schools total)
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 项目数量 |
|---------|------|------|---------|
| Minor | 辅修 (Minor) | 本科 | 92 |
| BA | Bachelor of Arts | 本科 | 73 |
| MS | Master of Science | 研究生 | 55 |
| Certificate | 本科证书 | 本科 | 46 |
| PhD | Doctor of Philosophy | 研究生 | 41 |
| MA | Master of Arts | 研究生 | 22 |
| Grad Cert | 研究生证书 | 研究生 | 21 |
| BS | Bachelor of Science | 本科 | 12 |
| MPH | Master of Public Health | 研究生 | 11 |
| MFA | Master of Fine Arts | 研究生 | 6 |
| BSM | Bachelor of Science in Management | 本科 | 5 |
| MHA | Master of Health Administration | 研究生 | 5 |
| MBA | Master of Business Administration | 研究生 | 5 |
| BFA | Bachelor of Fine Arts | 本科 | 4 |
| M.Arch | Master of Architecture | 研究生 | 3 |
| MSPH | MS in Public Health | 研究生 | 3 |
| MPHTM | MPH in Tropical Medicine | 研究生 | 3 |
| MJ | Master of Jurisprudence | 研究生 | 3 |
| MPA | Master of Public Administration | 研究生 | 3 |
| MPS | Master of Professional Studies | 研究生 | 2 |
| MFN | Master of Finance | 研究生 | 2 |
| BIS | Bachelor of Interdisciplinary Studies | 本科 | 2 |
| DrPH | Doctor of Public Health | 研究生 | 2 |
| MME | Master of Management & Energy | 研究生 | 2 |
| MACCT | Master of Accounting | 研究生 | 1 |
| LMA | LLM in Admiralty | 研究生 | 1 |
| Special | Special Program | 特殊 | 1 |
| AML | LLM in American Law | 研究生 | 1 |
| M.S.Arc | MS in Architectural Research & Design | 研究生 | 1 |
| B.Arch | Bachelor of Architecture | 本科 | 1 |
| BSA | BS in Architecture | 本科 | 1 |
| BSM/MACCT | Dual: BSM + MACCT | 研究生 | 1 |
| MAN | Master of Analytics | 研究生 | 1 |
| DI | Dietetic Internship | 研究生 | 1 |
| SJD | Doctor of Juridical Science | 研究生 | 1 |
| MLAN/MS | Dual: MLAN + MS | 研究生 | 1 |
| MEL | Master of Engineering Leadership | 研究生 | 1 |
| MJL | MJ in Law | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| LMI | LLM in International Law | 研究生 | 1 |
| MFA/MA | Dual: MFA + MA | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| MLA | Master of Liberal Arts | 研究生 | 1 |
| MEd | Master of Education | 研究生 | 1 |
| MMG | Master of Marketing | 研究生 | 1 |
| MSW/MPH | Dual: MSW + MPH | 研究生 | 1 |
| MD/MBA | Dual: MD + MBA | 研究生 | 1 |
| MD/MS | Dual: MD + MS | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| BSPH | BS in Public Health | 本科 | 1 |
| DSW | Doctor of Social Work | 研究生 | 1 |
| MSR | MS in Research | 研究生 | 1 |

### 0.4 分布矩阵 (学院 x canonical 学位级别)

| 学院 \ 级别 | BA/BS/BFA | Minor | UG Cert | MA/MS | MFA | MBA | MPH/DrPH | MHA/MSW | M.Arch | Law | MEL/DI | PhD | MD | Grad Cert | Dual/Other | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| School of Liberal Arts | 52 | 41 | 6 | 19 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 2 | 138 |
| School of Science and Engineering | 16 | 20 | 7 | 26 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 1 | 84 |
| School of Professional Advancement | 18 | 14 | 7 | 10 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 21 | 0 | 73 |
| Celia Scott Weatherhead School of Public Health and Tropical Medicine | 3 | 3 | 5 | 7 | 0 | 0 | 18 | 5 | 0 | 0 | 1 | 8 | 0 | 0 | 0 | 50 |
| A. B. Freeman School of Business | 5 | 7 | 5 | 1 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 31 |
| School of Medicine | 0 | 0 | 5 | 16 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 6 | 1 | 0 | 2 | 31 |
| School of Architecture and Built Environment | 5 | 6 | 4 | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 21 |
| School of Law | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 1 | 0 | 0 | 0 | 0 | 16 |
| School of Social Work | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| **合计** | **99** | **92** | **46** | **83** | **6** | **15** | **19** | **7** | **3** | **10** | **2** | **41** | **1** | **21** | **7** | **452** |

> **Reconciliation**: Rule 1 total (452) == Matrix sum (452). PASS.

---

## 1. 本科教育 (Undergraduate Education)

### 1.1 学院架构

Tulane所有本科生通过Newcomb-Tulane College统一入学，在大二春季学期选择主修后隶属于以下五所本科学院之一：School of Liberal Arts, School of Science and Engineering, School of Architecture and Built Environment, A. B. Freeman School of Business, Celia Scott Weatherhead School of Public Health and Tropical Medicine. School of Professional Advancement (SoPA) 提供面向成人学生的本科项目。

### 1.2 本科主修 - 按学院 > 系 > 学位级别分组

#### School of Liberal Arts
##### Africana Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Africana Studies | BA | [africana-studies-major](https://catalog.tulane.edu/liberal-arts/africana-studies/africana-studies-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Africana Studies | Minor | [africana-studies-minor](https://catalog.tulane.edu/liberal-arts/africana-studies/africana-studies-minor/) |

##### Ai Literacy Minor
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | AI Literacy | Minor | [ai-literacy-minor](https://catalog.tulane.edu/newcomb-tulane/ai-literacy-minor/) |

##### Altman Program
###### Coordinate Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Altman Program in International Studies and Business | Special | [altman-program](https://catalog.tulane.edu/newcomb-tulane/altman-program/) |

##### Anthropology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | BA | [anthropology-ba](https://catalog.tulane.edu/liberal-arts/anthropology/anthropology-ba/) |
| 2 | Anthropology | BS | [anthropology-bs](https://catalog.tulane.edu/liberal-arts/anthropology/anthropology-bs/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | Minor | [anthropology-minor](https://catalog.tulane.edu/liberal-arts/anthropology/anthropology-minor/) |

##### Art
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History | BA | [art-history-major](https://catalog.tulane.edu/liberal-arts/art/art-history-major/) |
| 2 | Studio Art | BA | [art-studio-ba](https://catalog.tulane.edu/liberal-arts/art/art-studio-ba/) |
| 3 | Studio Art | BFA | [art-studio-bfa](https://catalog.tulane.edu/liberal-arts/art/art-studio-bfa/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History | Minor | [art-history-minor](https://catalog.tulane.edu/liberal-arts/art/art-history-minor/) |
| 2 | Studio Art | Minor | [studio-art-minor](https://catalog.tulane.edu/liberal-arts/art/studio-art-minor/) |

##### Classical Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Classical Studies | BA | [classical-studies-major](https://catalog.tulane.edu/liberal-arts/classical-studies/classical-studies-major/) |
| 2 | Greek | BA | [greek-major](https://catalog.tulane.edu/liberal-arts/classical-studies/greek-major/) |
| 3 | Latin | BA | [latin-major](https://catalog.tulane.edu/liberal-arts/classical-studies/latin-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Classical Studies | Minor | [classical-studies-minor](https://catalog.tulane.edu/liberal-arts/classical-studies/classical-studies-minor/) |
| 2 | Greek | Minor | [greek-minor](https://catalog.tulane.edu/liberal-arts/classical-studies/greek-minor/) |
| 3 | Latin | Minor | [latin-minor](https://catalog.tulane.edu/liberal-arts/classical-studies/latin-minor/) |

##### Communication
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cinema Studies | BA | [cinema-studies-major](https://catalog.tulane.edu/liberal-arts/communication/cinema-studies-major/) |
| 2 | Communication | BA | [communication-major](https://catalog.tulane.edu/liberal-arts/communication/communication-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cinema Studies | Minor | [cinema-studies-minor](https://catalog.tulane.edu/liberal-arts/communication/cinema-studies-minor/) |

##### Comparative Literature
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Comparative Literature | BA | [comparative-literature-ba](https://catalog.tulane.edu/liberal-arts/comparative-literature/comparative-literature-ba/) |
| 2 | German Studies | BA | [german-studies-major](https://catalog.tulane.edu/liberal-arts/comparative-literature/german-studies-major/) |
| 3 | Russian | BA | [russian-major](https://catalog.tulane.edu/liberal-arts/comparative-literature/russian-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Comparative Literature | Minor | [comparative-literature-minor](https://catalog.tulane.edu/liberal-arts/comparative-literature/comparative-literature-minor/) |
| 2 | German Studies | Minor | [german-studies-minor](https://catalog.tulane.edu/liberal-arts/comparative-literature/german-studies-minor/) |
| 3 | Russian | Minor | [russian-minor](https://catalog.tulane.edu/liberal-arts/comparative-literature/russian-minor/) |

##### Economics
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Economics | BA | [economics-ba](https://catalog.tulane.edu/liberal-arts/economics/economics-ba/) |
| 2 | Economics | BS | [economics-bs](https://catalog.tulane.edu/liberal-arts/economics/economics-bs/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Economics | Minor | [economics-minor](https://catalog.tulane.edu/liberal-arts/economics/economics-minor/) |

##### English
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | English | BA | [english-major](https://catalog.tulane.edu/liberal-arts/english/english-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Creative Writing | Minor | [creative-writing-minor](https://catalog.tulane.edu/liberal-arts/english/creative-writing-minor/) |
| 2 | English | Minor | [english-minor](https://catalog.tulane.edu/liberal-arts/english/english-minor/) |

##### French Italian
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | French | BA | [french-major](https://catalog.tulane.edu/liberal-arts/french-italian/french-major/) |
| 2 | Italian | BA | [italian-major](https://catalog.tulane.edu/liberal-arts/french-italian/italian-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | French | Minor | [french-minor](https://catalog.tulane.edu/liberal-arts/french-italian/french-minor/) |
| 2 | Italian | Minor | [italian-minor](https://catalog.tulane.edu/liberal-arts/french-italian/italian-minor/) |

##### History
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | History | BA | [history-major](https://catalog.tulane.edu/liberal-arts/history/history-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | History | Minor | [history-minor](https://catalog.tulane.edu/liberal-arts/history/history-minor/) |

##### Interdisciplinary Programs Coordinate Majors
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Asian Studies | BA | [asian-studies-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/asian-studies-major/) |
| 2 | Environmental Studies | BA | [environmental-studies-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/environmental-studies-major/) |
| 3 | Gender and Sexuality Studies | BA | [gender-sexuality-studies-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/gender-sexuality-studies/gender-sexuality-studies-major/) |
| 4 | Latin American Studies Certificate for Public Health Majors | Certificate | [latin-american-studies-certificate-public-health-majors](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-studies-certificate-public-health-majors/) |
| 5 | Latin American Studies | BA | [latin-american-studies-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-studies-major/) |
| 6 | Linguistics | BA | [linguistics-ba](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/linguistics/linguistics-ba/) |
| 7 | Linguistics | BS | [linguistics-bs](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/linguistics/linguistics-bs/) |
| 8 | Medieval and Early Modern Studies | BA | [medieval-early-modern-studies-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/medieval-early-modern-studies-major/) |
| 9 | Middle East & North African Studies | BA | [middle-east-north-african-studies-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/middle-east-and-north-african-studies/middle-east-north-african-studies-major/) |
| 10 | Political Economy Major with Concentration in Economics and Public Policy | BA | [political-economy-major-concentration-economics-public-policy](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/political-economy/political-economy-major-concentration-economics-public-policy/) |
| 11 | Political Economy Major with Concentration in International Perspectives | BA | [political-economy-major-concentration-international-persepectives](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/political-economy/political-economy-major-concentration-international-persepectives/) |
| 12 | Political Economy Major with Concentration in Law | BA | [political-economy-major-concentration-law-economics-policy](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/political-economy/political-economy-major-concentration-law-economics-policy/) |
| 13 | Political Economy Major with Concentration in Moral and Historical Perspectives | BA | [political-economy-major-concentration-moral-historical-persepectives](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/political-economy/political-economy-major-concentration-moral-historical-persepectives/) |

###### Coordinate Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cognitive Studies Coordinate | BA | [cognitive-studies-coordinate-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/cognitive-studies-coordinate-major/) |
| 2 | Digital Media Practices Coordinate | BA | [digital-media-practices-coordinate-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/digital-media-practices-coordinate-major/) |
| 3 | Social Policy and Practice Coordinate | BA | [social-policy-practice-coordinate-major](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/social-policy-practice-coordinate-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Arabic Studies | Minor | [arabic-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/middle-east-and-north-african-studies/arabic-studies-minor/) |
| 2 | Asian Studies | Minor | [asian-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/asian-studies-minor/) |
| 3 | Chinese Language | Minor | [chinese-language-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/chinese-language-minor/) |
| 4 | Environmental Studies | Minor | [environmental-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/environmental-studies-minor/) |
| 5 | Gender and Sexuality Studies | Minor | [gender-sexuality-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/gender-sexuality-studies/gender-sexuality-studies-minor/) |
| 6 | Japanese Language | Minor | [japanese-language-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/japanese-language-minor/) |
| 7 | Latin American Studies | Minor | [latin-american-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-studies-minor/) |
| 8 | Medieval and Early Modern Studies | Minor | [medieval-early-modern-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/medieval-early-modern-studies-minor/) |
| 9 | Native American and Indigenous Studies | Minor | [native-american-and-indigenous-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/native-american-and-indigenous-studies/native-american-and-indigenous-studies-minor/) |
| 10 | Religious Studies | Minor | [religious-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/religious-studies-minor/) |
| 11 | Strategy | Minor | [strategy-leadership-analytics-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/strategy-leadership-analytics-minor/) |
| 12 | Urban Studies | Minor | [urban-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/urban-studies-minor/) |
| 13 | US Public Policy | Minor | [us-public-policy-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/us-public-policy-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Creative Industries | Certificate | [creative-industries-certificate](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/creative-industries-certificate/) |
| 2 | Gender Based Violence | Certificate | [gender-based-violence](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/gender-based-violence/) |

##### Jewish Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Jewish Studies | BA | [jewish-studies-major](https://catalog.tulane.edu/liberal-arts/jewish-studies/jewish-studies-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Jewish Studies | Minor | [jewish-studies-minor](https://catalog.tulane.edu/liberal-arts/jewish-studies/jewish-studies-minor/) |

##### Music
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | BA | [music-ba](https://catalog.tulane.edu/liberal-arts/music/music-ba/) |
| 2 | Music | BFA | [music-bfa](https://catalog.tulane.edu/liberal-arts/music/music-bfa/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | Minor | [music-minor](https://catalog.tulane.edu/liberal-arts/music/music-minor/) |
| 2 | Music Science and Technology | Minor | [music-science-technology-minor](https://catalog.tulane.edu/liberal-arts/music/music-science-technology-minor/) |

##### Philosophy
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | BA | [philosophy-major](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-major/) |
| 2 | Philosophy Major with Concentration in Language | BA | [philosophy-major-concentration-language-mind-knowledge](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-major-concentration-language-mind-knowledge/) |
| 3 | Philosophy Major with Concentration in Law | BA | [philosophy-major-concentration-law-morality-society](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-major-concentration-law-morality-society/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | Minor | [philosophy-minor](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-minor/) |

##### Political Science
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | BA | [political-science-major](https://catalog.tulane.edu/liberal-arts/political-science/political-science-major/) |
| 2 | Political Science/ International Development | BA | [political-science-international-development-major](https://catalog.tulane.edu/liberal-arts/political-science/political-science-international-development-major/) |
| 3 | Political Science/ International Relations | BA | [political-science-international-relations-major](https://catalog.tulane.edu/liberal-arts/political-science/political-science-international-relations-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | Minor | [political-science-minor](https://catalog.tulane.edu/liberal-arts/political-science/political-science-minor/) |
| 2 | Political Science/ International Development | Minor | [political-science-international-development-minor](https://catalog.tulane.edu/liberal-arts/political-science/political-science-international-development-minor/) |

##### Sociology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | BA | [sociology-major](https://catalog.tulane.edu/liberal-arts/sociology/sociology-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | Minor | [sociology-minor](https://catalog.tulane.edu/liberal-arts/sociology/sociology-minor/) |

##### Spanish Portuguese
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Spanish and Portuguese | BA | [spanish-portuguese-major](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-portuguese-major/) |
| 2 | Spanish | BA | [spanish-major](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-major/) |

###### Coordinate Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Portuguese Coordinate | BA | [portuguese-coordinate-major](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/portuguese-coordinate-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Portuguese | Minor | [portuguese-minor](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/portuguese-minor/) |
| 2 | Spanish | Minor | [spanish-minor](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-minor/) |

##### Theatre Dance
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Dance | BA | [dance-ba](https://catalog.tulane.edu/liberal-arts/theatre-dance/dance-ba/) |
| 2 | Dance | BFA | [dance-bfa](https://catalog.tulane.edu/liberal-arts/theatre-dance/dance-bfa/) |
| 3 | Theatre Design | BFA | [theatre-bfa](https://catalog.tulane.edu/liberal-arts/theatre-dance/theatre-bfa/) |
| 4 | Theatre | BA | [theatre-ba](https://catalog.tulane.edu/liberal-arts/theatre-dance/theatre-ba/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Theatre | Minor | [theatre-minor](https://catalog.tulane.edu/liberal-arts/theatre-dance/theatre-minor/) |

#### School of Science and Engineering
##### Biological Chemistry Program
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Chemistry | BA | [biological-chemistry-major](https://catalog.tulane.edu/science-engineering/biological-chemistry-program/biological-chemistry-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Chemistry | Minor | [biological-chemistry-minor](https://catalog.tulane.edu/science-engineering/biological-chemistry-program/biological-chemistry-minor/) |

##### Biomedical Engineering
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | BA | [biomedical-engineering-major](https://catalog.tulane.edu/science-engineering/biomedical-engineering/biomedical-engineering-major/) |
| 2 | Biomedical Engineering Minor for Non-Engineering Majors | Minor | [biomedical-engineering-minor-non-engineering-majors](https://catalog.tulane.edu/science-engineering/biomedical-engineering/biomedical-engineering-minor-non-engineering-majors/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | Minor | [biomedical-engineering-minor](https://catalog.tulane.edu/science-engineering/biomedical-engineering/biomedical-engineering-minor/) |

##### Cell Molecular Biology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cell and Molecular Biology | BA | [cell-molecular-biology-major](https://catalog.tulane.edu/science-engineering/cell-molecular-biology/cell-molecular-biology-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cell and Molecular Biology | Minor | [cell-molecular-biology-minor](https://catalog.tulane.edu/science-engineering/cell-molecular-biology/cell-molecular-biology-minor/) |

##### Chemical Biomolecular Engineering
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | BA | [chemical-engineering-major](https://catalog.tulane.edu/science-engineering/chemical-biomolecular-engineering/chemical-engineering-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | Minor | [chemical-engineering-minor](https://catalog.tulane.edu/science-engineering/chemical-biomolecular-engineering/chemical-engineering-minor/) |

##### Chemistry
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | BA | [chemistry-major](https://catalog.tulane.edu/science-engineering/chemistry/chemistry-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | Minor | [chemistry-minor](https://catalog.tulane.edu/science-engineering/chemistry/chemistry-minor/) |

##### Climate Change Science And Practice Minor
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Climate Change: Science and Practice | Minor | [climate-change-science-and-practice-minor](https://catalog.tulane.edu/newcomb-tulane/climate-change-science-and-practice-minor/) |

##### Computer Science
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | BS | [computer-science-bs](https://catalog.tulane.edu/science-engineering/computer-science/computer-science-bs/) |

###### Coordinate Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science Interdisciplinary Coordinate | BA | [computer-science-interdisciplinary-coordinate-major](https://catalog.tulane.edu/science-engineering/computer-science/computer-science-interdisciplinary-coordinate-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Artificial Intelligence | Minor | [artificial-intelligence-minor](https://catalog.tulane.edu/science-engineering/computer-science/artificial-intelligence-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | Certificate | [computer-science-undergraduate-certificate](https://catalog.tulane.edu/science-engineering/computer-science/computer-science-undergraduate-certificate/) |

##### Earth Environmental Sciences
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth and Environmental Sciences | BA | [earth-and-environmental-sciences-major](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/earth-and-environmental-sciences-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Earth and Environmental Sciences | Minor | [earth-and-environmental-sciences-minor](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/earth-and-environmental-sciences-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Geographic Information Systems | Certificate | [geographic-information-systems-certificate](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/geographic-information-systems-certificate/) |

##### Ecology Evolutionary Biology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Ecology and Evolutionary Biology | BA | [ecology-evolutionary-biology-major](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/ecology-evolutionary-biology-major/) |
| 2 | Environmental Biology | BA | [environmental-biology-major](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/environmental-biology-major/) |
| 3 | Marine Biology Minor for Biology Majors | Minor | [marine-biology-minor-biology-majors](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/marine-biology-minor-biology-majors/) |
| 4 | Marine Biology Minor for Non-Biology Majors | Minor | [marine-biology-minor-non-biology-majors](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/marine-biology-minor-non-biology-majors/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Ecology and Evolutionary Biology | Minor | [ecology-and-evolutionary-biology-minor](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/ecology-and-evolutionary-biology-minor/) |

##### Mathematics
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | BA | [mathematics-major](https://catalog.tulane.edu/science-engineering/mathematics/mathematics-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | Minor | [mathematics-minor](https://catalog.tulane.edu/science-engineering/mathematics/mathematics-minor/) |

##### Neuroscience Program
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Neuroscience | BA | [neuroscience-major](https://catalog.tulane.edu/science-engineering/neuroscience-program/neuroscience-major/) |

##### Physics Engineering
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Engineering Physics | BA | [engineering-physics-major](https://catalog.tulane.edu/science-engineering/physics-engineering/engineering-physics-major/) |
| 2 | Physics | BA | [physics-major](https://catalog.tulane.edu/science-engineering/physics-engineering/physics-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical Engineering | Minor | [electrical-engineering-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/electrical-engineering-minor/) |
| 2 | Engineering Science | Minor | [engineering-science-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/engineering-science-minor/) |
| 3 | Materials Engineering | Minor | [materials-engineering-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/materials-engineering-minor/) |
| 4 | Mechanical Engineering | Minor | [mechanical-engineering-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/mechanical-engineering-minor/) |
| 5 | Physics | Minor | [physics-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/physics-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computational Engineering | Certificate | [computational-engineering-certificate](https://catalog.tulane.edu/science-engineering/physics-engineering/computational-engineering-certificate/) |

##### Psychology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology | BA | [psychology-major](https://catalog.tulane.edu/science-engineering/psychology/psychology-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology | Minor | [psychology-minor](https://catalog.tulane.edu/science-engineering/psychology/psychology-minor/) |

##### River Coastal Science Engineering
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering - Water and Environment | BA | [civil-engineering-water-and-environment-major](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/civil-engineering-water-and-environment-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering - Water and Environment | Minor | [civil-engineering-water-and-environment-minor](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/civil-engineering-water-and-environment-minor/) |

#### School of Professional Advancement
##### Business Leadership Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Human Resources | BA | [human-resources-ba](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/human-resources-ba/) |
| 2 | Organizational Behavior and Management Studies | BS | [organizational-behavior-and-management-studies-bs](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/organizational-behavior-and-management-studies-bs/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Business Studies | Minor | [applied-business-studies-minor](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/applied-business-studies-minor/) |
| 2 | Human Resource Development | Minor | [human-resource-development-minor](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/human-resource-development-minor/) |
| 3 | Small Business Development | Minor | [small-business-development-minor](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/small-business-development-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting Fundamentals | Certificate | [accounting-fundamentals-certificate](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/accounting-fundamentals-certificate/) |
| 2 | Applied Business Studies | Certificate | [business-certificate](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/business-certificate/) |
| 3 | Human Resource Fundamentals | Certificate | [human-resources-fundamentals-certificate](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/human-resources-fundamentals-certificate/) |
| 4 | Small Business Development | Certificate | [small-business-development-certificate](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/small-business-development-certificate/) |

##### Education
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Elementary Education | BA | [elementary-education-major](https://catalog.tulane.edu/professional-advancement/education/elementary-education-major/) |
| 2 | Secondary Education | BA | [secondary-education-major](https://catalog.tulane.edu/professional-advancement/education/secondary-education-major/) |

###### Coordinate Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Secondary Education (Grades 6-12) | BA | [secondary-education-coordinate-major](https://catalog.tulane.edu/professional-advancement/education/secondary-education-coordinate-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Teaching English Learners | Minor | [teaching-english-learners](https://catalog.tulane.edu/professional-advancement/education/teaching-english-learners/) |
| 2 | Teaching | Minor | [teaching-learning-training-minor](https://catalog.tulane.edu/professional-advancement/education/teaching-learning-training-minor/) |

##### Emergency Security Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Homeland Security | BA | [homeland-security-major](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/homeland-security-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Homeland Security Studies | Minor | [homeland-security-studies-minor](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/homeland-security-studies-minor/) |

##### Humanities Social Sciences
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Humanities | BA | [humanities-ba](https://catalog.tulane.edu/professional-advancement/humanities-social-sciences/humanities-ba/) |
| 2 | Interdisciplinary Studies with Concentrations | BIS | [interdisciplinary-studies-major](https://catalog.tulane.edu/professional-advancement/humanities-social-sciences/interdisciplinary-studies-major/) |
| 3 | Social Sciences | BA | [social-sciences-ba](https://catalog.tulane.edu/professional-advancement/humanities-social-sciences/social-sciences-ba/) |

##### Information Technology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Information Technology | BS | [information-technology-major](https://catalog.tulane.edu/professional-advancement/information-technology/information-technology-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Information Technology | Minor | [information-technology-minor](https://catalog.tulane.edu/professional-advancement/information-technology/information-technology-minor/) |

##### Kinesiology
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Exercise Science | BS | [exercise-science-major](https://catalog.tulane.edu/professional-advancement/kinesiology/exercise-science-major/) |
| 2 | Health and Wellness | BA | [health-wellness-major](https://catalog.tulane.edu/professional-advancement/kinesiology/health-wellness-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Exercise Science | Minor | [exercise-science-minor](https://catalog.tulane.edu/professional-advancement/kinesiology/exercise-science-minor/) |
| 2 | Health and Wellness | Minor | [health-wellness-minor](https://catalog.tulane.edu/professional-advancement/kinesiology/health-wellness-minor/) |

##### Media Design
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Digital Design | BA | [digital-design-ba](https://catalog.tulane.edu/professional-advancement/media-design/digital-design-ba/) |
| 2 | Digital Media & Marketing Communications | BA | [digital-media-marketing-communications](https://catalog.tulane.edu/professional-advancement/media-design/digital-media-marketing-communications/) |
| 3 | Public Relations | BA | [public-relations-ba](https://catalog.tulane.edu/professional-advancement/media-design/public-relations-ba/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Digital Media & Marketing Communications | Minor | [digital-media-marketing-communications-minor](https://catalog.tulane.edu/professional-advancement/media-design/digital-media-marketing-communications-minor/) |
| 2 | Graphic Design | Minor | [graphic-design-minor](https://catalog.tulane.edu/professional-advancement/media-design/graphic-design-minor/) |
| 3 | Interactive UX/UI Design | Minor | [interactive-design-minor](https://catalog.tulane.edu/professional-advancement/media-design/interactive-design-minor/) |
| 4 | Public Relations | Minor | [public-relations-minor](https://catalog.tulane.edu/professional-advancement/media-design/public-relations-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Digital Media & Marketing Communications | Certificate | [digital-media-marketing-certificate](https://catalog.tulane.edu/professional-advancement/media-design/digital-media-marketing-certificate/) |
| 2 | Public Relations | Certificate | [public-relations-certificate](https://catalog.tulane.edu/professional-advancement/media-design/public-relations-certificate/) |

##### Paralegal Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Paralegal Studies | BA | [paralegal-studies-ba](https://catalog.tulane.edu/professional-advancement/paralegal-studies/paralegal-studies-ba/) |
| 2 | Paralegal Studies | BIS | [paralegal-studies-bis](https://catalog.tulane.edu/professional-advancement/paralegal-studies/paralegal-studies-bis/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Paralegal Studies | Minor | [paralegal-studies-minor](https://catalog.tulane.edu/professional-advancement/paralegal-studies/paralegal-studies-minor/) |

##### Program Of Nursing
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | BS | [nursing-bsn](https://catalog.tulane.edu/medicine/program-of-nursing/nursing-bsn/) |

#### Celia Scott Weatherhead School of Public Health and Tropical Medicine
##### Undergraduate Public Health
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Health Policy and Management | BS | [health-policy-management](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/health-policy-management/) |
| 2 | Nutrition Science | BS | [nutrition-sciences-bs](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/nutrition-sciences-bs/) |
| 3 | Public Health | BSPH | [public-health-bsph](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-bsph/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Health Healthcare Administration | Minor | [public-health-healthcare-administration-minor](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-healthcare-administration-minor/) |
| 2 | Public Health | Minor | [public-health-minor](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-minor/) |
| 3 | Public Health Nutrition | Minor | [public-health-nutrition-minor](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-nutrition-minor/) |

#### A. B. Freeman School of Business
##### Accounting
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | BSM | [accounting-major](https://catalog.tulane.edu/business/accounting/accounting-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting Minor for BSMs | Minor | [accounting-minor](https://catalog.tulane.edu/business/accounting/accounting-minor/) |

##### Business Analytics
###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Analytics and AI | Certificate | [business-analytics-and-ai-certificate](https://catalog.tulane.edu/business/business-analytics/business-analytics-and-ai-certificate/) |

##### Business Minor
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Freeman Business | Minor | [freeman-business-minor](https://catalog.tulane.edu/business/business-minor/freeman-business-minor/) |

##### Energy
###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Energy | Certificate | [energy-certificate](https://catalog.tulane.edu/business/energy/energy-certificate/) |

##### Entrepreneurship
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Minor in Entrepreneurial Business (available to BSM's and non-BSM's) | Minor | [entrepreneurial-business-minor](https://catalog.tulane.edu/business/entrepreneurship/entrepreneurial-business-minor/) |

##### Finance
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Finance | BSM | [finance-major](https://catalog.tulane.edu/business/finance/finance-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Finance Minor for BSMs | Minor | [finance-minor](https://catalog.tulane.edu/business/finance/finance-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Real Estate Finance and Investment | Certificate | [real-estate-finance-and-investment-certificate](https://catalog.tulane.edu/business/finance/real-estate-finance-and-investment-certificate/) |

##### Hospitality Management And Entrepreneurship Certificate
###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Hospitality Management and Entrepreneurship | Certificate | [hospitality-management-and-entrepreneurship-certificate](https://catalog.tulane.edu/business/hospitality-management-and-entrepreneurship-certificate/) |

##### Legal Studies
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Legal Studies in Business | BSM | [legal-studies-major](https://catalog.tulane.edu/business/legal-studies/legal-studies-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Legal Studies in Business Minor for BSMs | Minor | [legal-studies-minor](https://catalog.tulane.edu/business/legal-studies/legal-studies-minor/) |

##### Management
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Management | BSM | [management-major](https://catalog.tulane.edu/business/management/management-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Management Minor for BSMs | Minor | [management-minor](https://catalog.tulane.edu/business/management/management-minor/) |

###### Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sports Management | Certificate | [sports-management-certificate](https://catalog.tulane.edu/business/management/sports-management-certificate/) |

##### Marketing
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Marketing | BSM | [marketing-major](https://catalog.tulane.edu/business/marketing/marketing-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Marketing Minor for BSMs | Minor | [marketing-minor](https://catalog.tulane.edu/business/marketing/marketing-minor/) |

#### School of Architecture and Built Environment
##### Architecture
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | B.Arch | [architecture-barch](https://catalog.tulane.edu/architecture/architecture/architecture-barch/) |
| 2 | Architecture | BSA | [architecture-bsa](https://catalog.tulane.edu/architecture/architecture/architecture-bsa/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | Minor | [architecture-minor](https://catalog.tulane.edu/architecture/architecture/architecture-minor/) |

##### Design
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Design | BA | [design-ba](https://catalog.tulane.edu/architecture/design/design-ba/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Design | Minor | [design-minor](https://catalog.tulane.edu/architecture/design/design-minor/) |

##### Preservation
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Historic Preservation | Minor | [historic-preservation-minor](https://catalog.tulane.edu/architecture/preservation/historic-preservation-minor/) |

##### Real Estate Development
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Real Estate | BS | [real-estate-major](https://catalog.tulane.edu/architecture/real-estate-development/real-estate-major/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Real Estate | Minor | [real-estate-minor](https://catalog.tulane.edu/architecture/real-estate-development/real-estate-minor/) |

##### Social Innovation Entrepreneurship
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Innovation & Social Entrepreneurship | Minor | [social-innovation-entrepreneurship-minor](https://catalog.tulane.edu/architecture/social-innovation-entrepreneurship/social-innovation-entrepreneurship-minor/) |

##### Sustainable Urbanism
###### Major
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sustainable Urbanism | BS | [sustainable-urbanism-bs](https://catalog.tulane.edu/architecture/sustainable-urbanism/sustainable-urbanism-bs/) |

###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sustainable Urbanism | Minor | [sustainable-urbanism-minor](https://catalog.tulane.edu/architecture/sustainable-urbanism/sustainable-urbanism-minor/) |

#### School of Social Work
##### Social Work
###### Minor
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | Minor | [social-work-minor](https://catalog.tulane.edu/social-work/social-work/social-work-minor/) |

### 1.3 本科辅修 - 完整列表

| # | 辅修名称 | 所属学院 | URL |
|---|---------|---------|-----|
| 1 | Accounting for BSMs | A. B. Freeman School of Business | [accounting-minor](https://catalog.tulane.edu/business/accounting/accounting-minor/) |
| 2 | Africana Studies | School of Liberal Arts | [africana-studies-minor](https://catalog.tulane.edu/liberal-arts/africana-studies/africana-studies-minor/) |
| 3 | AI Literacy | School of Liberal Arts | [ai-literacy-minor](https://catalog.tulane.edu/newcomb-tulane/ai-literacy-minor/) |
| 4 | Anthropology | School of Liberal Arts | [anthropology-minor](https://catalog.tulane.edu/liberal-arts/anthropology/anthropology-minor/) |
| 5 | Applied Business Studies, | School of Professional Advancement | [applied-business-studies-minor](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/applied-business-studies-minor/) |
| 6 | Arabic Studies | School of Liberal Arts | [arabic-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/middle-east-and-north-african-studies/arabic-studies-minor/) |
| 7 | Architecture | School of Architecture and Built Environment | [architecture-minor](https://catalog.tulane.edu/architecture/architecture/architecture-minor/) |
| 8 | Art History | School of Liberal Arts | [art-history-minor](https://catalog.tulane.edu/liberal-arts/art/art-history-minor/) |
| 9 | Artificial Intelligence | School of Science and Engineering | [artificial-intelligence-minor](https://catalog.tulane.edu/science-engineering/computer-science/artificial-intelligence-minor/) |
| 10 | Asian Studies | School of Liberal Arts | [asian-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/asian-studies-minor/) |
| 11 | Biological Chemistry | School of Science and Engineering | [biological-chemistry-minor](https://catalog.tulane.edu/science-engineering/biological-chemistry-program/biological-chemistry-minor/) |
| 12 | Biomedical Engineering | School of Science and Engineering | [biomedical-engineering-minor](https://catalog.tulane.edu/science-engineering/biomedical-engineering/biomedical-engineering-minor/) |
| 13 | Cell and Molecular Biology | School of Science and Engineering | [cell-molecular-biology-minor](https://catalog.tulane.edu/science-engineering/cell-molecular-biology/cell-molecular-biology-minor/) |
| 14 | Chemical Engineering | School of Science and Engineering | [chemical-engineering-minor](https://catalog.tulane.edu/science-engineering/chemical-biomolecular-engineering/chemical-engineering-minor/) |
| 15 | Chemistry | School of Science and Engineering | [chemistry-minor](https://catalog.tulane.edu/science-engineering/chemistry/chemistry-minor/) |
| 16 | Chinese Language | School of Liberal Arts | [chinese-language-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/chinese-language-minor/) |
| 17 | Cinema Studies | School of Liberal Arts | [cinema-studies-minor](https://catalog.tulane.edu/liberal-arts/communication/cinema-studies-minor/) |
| 18 | Civil Engineering - Water and Environment | School of Science and Engineering | [civil-engineering-water-and-environment-minor](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/civil-engineering-water-and-environment-minor/) |
| 19 | Classical Studies | School of Liberal Arts | [classical-studies-minor](https://catalog.tulane.edu/liberal-arts/classical-studies/classical-studies-minor/) |
| 20 | Climate Change: Science and Practice | School of Science and Engineering | [climate-change-science-and-practice-minor](https://catalog.tulane.edu/newcomb-tulane/climate-change-science-and-practice-minor/) |
| 21 | Comparative Literature | School of Liberal Arts | [comparative-literature-minor](https://catalog.tulane.edu/liberal-arts/comparative-literature/comparative-literature-minor/) |
| 22 | Creative Writing | School of Liberal Arts | [creative-writing-minor](https://catalog.tulane.edu/liberal-arts/english/creative-writing-minor/) |
| 23 | Design | School of Architecture and Built Environment | [design-minor](https://catalog.tulane.edu/architecture/design/design-minor/) |
| 24 | Digital Media & Marketing Communications, | School of Professional Advancement | [digital-media-marketing-communications-minor](https://catalog.tulane.edu/professional-advancement/media-design/digital-media-marketing-communications-minor/) |
| 25 | Earth and Environmental Sciences | School of Science and Engineering | [earth-and-environmental-sciences-minor](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/earth-and-environmental-sciences-minor/) |
| 26 | Ecology and Evolutionary Biology | School of Science and Engineering | [ecology-and-evolutionary-biology-minor](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/ecology-and-evolutionary-biology-minor/) |
| 27 | Economics | School of Liberal Arts | [economics-minor](https://catalog.tulane.edu/liberal-arts/economics/economics-minor/) |
| 28 | Electrical Engineering | School of Science and Engineering | [electrical-engineering-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/electrical-engineering-minor/) |
| 29 | Engineering Science | School of Science and Engineering | [engineering-science-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/engineering-science-minor/) |
| 30 | English | School of Liberal Arts | [english-minor](https://catalog.tulane.edu/liberal-arts/english/english-minor/) |
| 31 | Environmental Studies | School of Liberal Arts | [environmental-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/environmental-studies-minor/) |
| 32 | Exercise Science, | School of Professional Advancement | [exercise-science-minor](https://catalog.tulane.edu/professional-advancement/kinesiology/exercise-science-minor/) |
| 33 | Finance for BSMs | A. B. Freeman School of Business | [finance-minor](https://catalog.tulane.edu/business/finance/finance-minor/) |
| 34 | Freeman Business | A. B. Freeman School of Business | [freeman-business-minor](https://catalog.tulane.edu/business/business-minor/freeman-business-minor/) |
| 35 | French | School of Liberal Arts | [french-minor](https://catalog.tulane.edu/liberal-arts/french-italian/french-minor/) |
| 36 | Gender and Sexuality Studies | School of Liberal Arts | [gender-sexuality-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/gender-sexuality-studies/gender-sexuality-studies-minor/) |
| 37 | German Studies | School of Liberal Arts | [german-studies-minor](https://catalog.tulane.edu/liberal-arts/comparative-literature/german-studies-minor/) |
| 38 | Graphic Design, | School of Professional Advancement | [graphic-design-minor](https://catalog.tulane.edu/professional-advancement/media-design/graphic-design-minor/) |
| 39 | Greek | School of Liberal Arts | [greek-minor](https://catalog.tulane.edu/liberal-arts/classical-studies/greek-minor/) |
| 40 | Health and Wellness, | School of Professional Advancement | [health-wellness-minor](https://catalog.tulane.edu/professional-advancement/kinesiology/health-wellness-minor/) |
| 41 | Historic Preservation | School of Architecture and Built Environment | [historic-preservation-minor](https://catalog.tulane.edu/architecture/preservation/historic-preservation-minor/) |
| 42 | History | School of Liberal Arts | [history-minor](https://catalog.tulane.edu/liberal-arts/history/history-minor/) |
| 43 | Homeland Security Studies, | School of Professional Advancement | [homeland-security-studies-minor](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/homeland-security-studies-minor/) |
| 44 | Human Resource Development, | School of Professional Advancement | [human-resource-development-minor](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/human-resource-development-minor/) |
| 45 | Information Technology, | School of Professional Advancement | [information-technology-minor](https://catalog.tulane.edu/professional-advancement/information-technology/information-technology-minor/) |
| 46 | Interactive UX/UI Design, | School of Professional Advancement | [interactive-design-minor](https://catalog.tulane.edu/professional-advancement/media-design/interactive-design-minor/) |
| 47 | Italian | School of Liberal Arts | [italian-minor](https://catalog.tulane.edu/liberal-arts/french-italian/italian-minor/) |
| 48 | Japanese Language | School of Liberal Arts | [japanese-language-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/asian-studies/japanese-language-minor/) |
| 49 | Jewish Studies | School of Liberal Arts | [jewish-studies-minor](https://catalog.tulane.edu/liberal-arts/jewish-studies/jewish-studies-minor/) |
| 50 | Latin American Studies | School of Liberal Arts | [latin-american-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-studies-minor/) |
| 51 | Latin | School of Liberal Arts | [latin-minor](https://catalog.tulane.edu/liberal-arts/classical-studies/latin-minor/) |
| 52 | Legal Studies in Business for BSMs | A. B. Freeman School of Business | [legal-studies-minor](https://catalog.tulane.edu/business/legal-studies/legal-studies-minor/) |
| 53 | Management for BSMs | A. B. Freeman School of Business | [management-minor](https://catalog.tulane.edu/business/management/management-minor/) |
| 54 | Marketing for BSMs | A. B. Freeman School of Business | [marketing-minor](https://catalog.tulane.edu/business/marketing/marketing-minor/) |
| 55 | Materials Engineering | School of Science and Engineering | [materials-engineering-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/materials-engineering-minor/) |
| 56 | Mathematics | School of Science and Engineering | [mathematics-minor](https://catalog.tulane.edu/science-engineering/mathematics/mathematics-minor/) |
| 57 | Mechanical Engineering | School of Science and Engineering | [mechanical-engineering-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/mechanical-engineering-minor/) |
| 58 | Medieval and Early Modern Studies | School of Liberal Arts | [medieval-early-modern-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/medieval-early-modern-studies-minor/) |
| 59 | Minor in Entrepreneurial Business (available to BSM's and non-BSM's) | A. B. Freeman School of Business | [entrepreneurial-business-minor](https://catalog.tulane.edu/business/entrepreneurship/entrepreneurial-business-minor/) |
| 60 | Music | School of Liberal Arts | [music-minor](https://catalog.tulane.edu/liberal-arts/music/music-minor/) |
| 61 | Music Science and Technology | School of Liberal Arts | [music-science-technology-minor](https://catalog.tulane.edu/liberal-arts/music/music-science-technology-minor/) |
| 62 | Native American and Indigenous Studies | School of Liberal Arts | [native-american-and-indigenous-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/native-american-and-indigenous-studies/native-american-and-indigenous-studies-minor/) |
| 63 | Paralegal Studies, | School of Professional Advancement | [paralegal-studies-minor](https://catalog.tulane.edu/professional-advancement/paralegal-studies/paralegal-studies-minor/) |
| 64 | Philosophy | School of Liberal Arts | [philosophy-minor](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-minor/) |
| 65 | Physics | School of Science and Engineering | [physics-minor](https://catalog.tulane.edu/science-engineering/physics-engineering/physics-minor/) |
| 66 | Political Science | School of Liberal Arts | [political-science-minor](https://catalog.tulane.edu/liberal-arts/political-science/political-science-minor/) |
| 67 | Political Science/ International Development | School of Liberal Arts | [political-science-international-development-minor](https://catalog.tulane.edu/liberal-arts/political-science/political-science-international-development-minor/) |
| 68 | Portuguese | School of Liberal Arts | [portuguese-minor](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/portuguese-minor/) |
| 69 | Psychology | School of Science and Engineering | [psychology-minor](https://catalog.tulane.edu/science-engineering/psychology/psychology-minor/) |
| 70 | Public Health Healthcare Administration | Celia Scott Weatherhead School of Public Health and Tropical Medicine | [public-health-healthcare-administration-minor](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-healthcare-administration-minor/) |
| 71 | Public Health | Celia Scott Weatherhead School of Public Health and Tropical Medicine | [public-health-minor](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-minor/) |
| 72 | Public Health Nutrition | Celia Scott Weatherhead School of Public Health and Tropical Medicine | [public-health-nutrition-minor](https://catalog.tulane.edu/public-health-tropical-medicine/undergraduate-public-health/public-health-nutrition-minor/) |
| 73 | Public Relations, | School of Professional Advancement | [public-relations-minor](https://catalog.tulane.edu/professional-advancement/media-design/public-relations-minor/) |
| 74 | Real Estate | School of Architecture and Built Environment | [real-estate-minor](https://catalog.tulane.edu/architecture/real-estate-development/real-estate-minor/) |
| 75 | Religious Studies | School of Liberal Arts | [religious-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/religious-studies-minor/) |
| 76 | Russian | School of Liberal Arts | [russian-minor](https://catalog.tulane.edu/liberal-arts/comparative-literature/russian-minor/) |
| 77 | Small Business Development, | School of Professional Advancement | [small-business-development-minor](https://catalog.tulane.edu/professional-advancement/business-leadership-studies/small-business-development-minor/) |
| 78 | Social Innovation & Social Entrepreneurship | School of Architecture and Built Environment | [social-innovation-entrepreneurship-minor](https://catalog.tulane.edu/architecture/social-innovation-entrepreneurship/social-innovation-entrepreneurship-minor/) |
| 79 | Social Work | School of Social Work | [social-work-minor](https://catalog.tulane.edu/social-work/social-work/social-work-minor/) |
| 80 | Sociology | School of Liberal Arts | [sociology-minor](https://catalog.tulane.edu/liberal-arts/sociology/sociology-minor/) |
| 81 | Spanish | School of Liberal Arts | [spanish-minor](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-minor/) |
| 82 | Strategy, Leadership & Analytics | School of Liberal Arts | [strategy-leadership-analytics-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/strategy-leadership-analytics-minor/) |
| 83 | Studio Art | School of Liberal Arts | [studio-art-minor](https://catalog.tulane.edu/liberal-arts/art/studio-art-minor/) |
| 84 | Sustainable Urbanism | School of Architecture and Built Environment | [sustainable-urbanism-minor](https://catalog.tulane.edu/architecture/sustainable-urbanism/sustainable-urbanism-minor/) |
| 85 | Teaching English Learners, | School of Professional Advancement | [teaching-english-learners](https://catalog.tulane.edu/professional-advancement/education/teaching-english-learners/) |
| 86 | Teaching, Learning, and Training, | School of Professional Advancement | [teaching-learning-training-minor](https://catalog.tulane.edu/professional-advancement/education/teaching-learning-training-minor/) |
| 87 | Theatre | School of Liberal Arts | [theatre-minor](https://catalog.tulane.edu/liberal-arts/theatre-dance/theatre-minor/) |
| 88 | Urban Studies | School of Liberal Arts | [urban-studies-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/urban-studies-minor/) |
| 89 | US Public Policy | School of Liberal Arts | [us-public-policy-minor](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/us-public-policy-minor/) |

### 1.4 Core Curriculum

Tulane的Core Curriculum要求包括：Writing, Formal Reasoning, Foreign Language, Scientific Inquiry, Cultural Knowledge & Expression, 以及Public Service。详见 https://advising.tulane.edu/resources/core-curriculum

---

## 2. 研究生教育 (Graduate Education)

### 2.1 研究生项目 - 按学院 > 学位级别分组

Tulane的研究生招生由各学院独立管理。Office of Graduate and Postdoctoral Studies (OGPS) 提供协调服务。

#### School of Liberal Arts
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Africana Studies and Art History | [africana-studies-and-art-history-ma](https://catalog.tulane.edu/liberal-arts/art/africana-studies-and-art-history-ma/) |
| 2 | Anthropology | [anthropology-ma](https://catalog.tulane.edu/liberal-arts/anthropology/anthropology-ma/) |
| 3 | Art History | [art-history-ma](https://catalog.tulane.edu/liberal-arts/art/art-history-ma/) |
| 4 | Classical Studies | [classical-studies-ma](https://catalog.tulane.edu/liberal-arts/classical-studies/classical-studies-ma/) |
| 5 | Computational Linguistics | [computationallinguistics-ma](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/linguistics/computationallinguistics-ma/) |
| 6 | English | [english-ma](https://catalog.tulane.edu/liberal-arts/english/english-ma/) |
| 7 | French/Francophone Studies | [french-studies-ma](https://catalog.tulane.edu/liberal-arts/french-italian/french-studies-ma/) |
| 8 | History | [history-ma](https://catalog.tulane.edu/liberal-arts/history/history-ma/) |
| 9 | Latin American Studies | [latin-american-studies-ma](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-studies-ma/) |
| 10 | Linguistics | [linguistics-ma](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/linguistics/linguistics-ma/) |
| 11 | Music | [music-ma](https://catalog.tulane.edu/liberal-arts/music/music-ma/) |
| 12 | Philosophy | [philosophy-ma](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-ma/) |
| 13 | Policy Economics | [policy-economics-ma](https://catalog.tulane.edu/liberal-arts/economics/policy-economics-ma/) |
| 14 | Political Economy with Data Analytics | [data-analytics-ma](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/political-economy/data-analytics-ma/) |
| 15 | Political Science | [political-science-ma](https://catalog.tulane.edu/liberal-arts/political-science/political-science-ma/) |
| 16 | Sociology | [sociology-ma](https://catalog.tulane.edu/liberal-arts/sociology/sociology-ma/) |
| 17 | Spanish and Portuguese | [spanish-portuguese-ma](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-portuguese-ma/) |
| 18 | Spanish | [spanish-ma](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-ma/) |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | [anthropology-phd](https://catalog.tulane.edu/liberal-arts/anthropology/anthropology-phd/) |
| 2 | City | [city-culture-community-phd](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/city-culture-community-phd/) |
| 3 | Economics | [economics-analysis-policy-phd](https://catalog.tulane.edu/liberal-arts/economics/economics-analysis-policy-phd/) |
| 4 | French and Francophone Studies | [french-studies-phd](https://catalog.tulane.edu/liberal-arts/french-italian/french-studies-phd/) |
| 5 | History | [history-phd](https://catalog.tulane.edu/liberal-arts/history/history-phd/) |
| 6 | Latin American Studies and Art History | [latin-american-art-phd](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-art-phd/) |
| 7 | Latin American Studies | [latin-american-studies-phd](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/latin-american-studies/latin-american-studies-phd/) |
| 8 | Linguistics | [linguistics-phd](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/linguistics/linguistics-phd/) |
| 9 | Philosophy | [philosophy-phd](https://catalog.tulane.edu/liberal-arts/philosophy/philosophy-phd/) |
| 10 | Political Science | [political-science-phd](https://catalog.tulane.edu/liberal-arts/political-science/political-science-phd/) |
| 11 | Sociology | [sociology-phd](https://catalog.tulane.edu/liberal-arts/sociology/sociology-phd/) |
| 12 | Spanish and Portuguese | [spanish-portuguese-phd](https://catalog.tulane.edu/liberal-arts/spanish-portuguese/spanish-portuguese-phd/) |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Studio | [art-studio-mfa](https://catalog.tulane.edu/liberal-arts/art/art-studio-mfa/) |
| 2 | Interdisciplinary Dance Performance | [interdisciplinary-dance-performance-mfa](https://catalog.tulane.edu/liberal-arts/theatre-dance/interdisciplinary-dance-performance-mfa/) |
| 3 | Music | [music-mfa](https://catalog.tulane.edu/liberal-arts/music/music-mfa/) |
| 4 | Music | [music-mfa-concentration-black-american-music](https://catalog.tulane.edu/liberal-arts/music/music-mfa-concentration-black-american-music/) |
| 5 | Studio Art with a concentration in Africana Studies | [studio-art-concentration-africana-studies-mfa](https://catalog.tulane.edu/liberal-arts/art/studio-art-concentration-africana-studies-mfa/) |
| 6 | Theatre Design and Production | [theatre-design-production-mfa](https://catalog.tulane.edu/liberal-arts/theatre-dance/theatre-design-production-mfa/) |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Industries Certificate (Graduate) | [creative-industries-graduate-certificate](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/creative-industries-graduate-certificate/) |
| 2 | Gender and Sexuality Studies Certificate (Graduate) | [gender-and-sexuality-studies-graduate-certificate](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/gender-sexuality-studies/gender-and-sexuality-studies-graduate-certificate/) |
| 3 | Publicly Engaged Scholarship Certificate (Graduate) | [publicly-engaged-scholarship-graduate-certificate](https://catalog.tulane.edu/liberal-arts/interdisciplinary-programs-coordinate-majors/publicly-engaged-scholarship-graduate-certificate/) |

##### MFA/MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Joint Degree in Studio Art and Africana Studies | [studio-art-africana-studies-mfa-ma](https://catalog.tulane.edu/liberal-arts/art/studio-art-africana-studies-mfa-ma/) |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy and Bioethics | [philosophy-bioethics-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/philosophy-bioethics-ms/) |

#### School of Science and Engineering
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | [applied-mathematics-ms](https://catalog.tulane.edu/science-engineering/mathematics/applied-mathematics-ms/) |
| 2 | Behavioral Health | [behavioral-health-ms](https://catalog.tulane.edu/science-engineering/psychology/behavioral-health-ms/) |
| 3 | Bioinnovation | [bioinnovation-ms](https://catalog.tulane.edu/science-engineering/interdisciplinary-graduate-programs/bioinnovation-ms/) |
| 4 | Biomedical Engineering | [biomedical-engineering-ms](https://catalog.tulane.edu/science-engineering/biomedical-engineering/biomedical-engineering-ms/) |
| 5 | Cell and Molecular Biology Thesis Research | [cell-molecular-biology-thesis-research-ms](https://catalog.tulane.edu/science-engineering/cell-molecular-biology/cell-molecular-biology-thesis-research-ms/) |
| 6 | Cell and Molecular Biology | [cell-molecular-biology-ms](https://catalog.tulane.edu/science-engineering/cell-molecular-biology/cell-molecular-biology-ms/) |
| 7 | Chemical and Biomolecular Engineering | [chemical-biomolecular-engineering-ms](https://catalog.tulane.edu/science-engineering/chemical-biomolecular-engineering/chemical-biomolecular-engineering-ms/) |
| 8 | Chemistry | [chemistry-ms](https://catalog.tulane.edu/science-engineering/chemistry/chemistry-ms/) |
| 9 | Computational Science | [computational-science-ms](https://catalog.tulane.edu/science-engineering/center-for-computational-science/computational-science-ms/) |
| 10 | Computer Science | [computer-science-ms](https://catalog.tulane.edu/science-engineering/computer-science/computer-science-ms/) |
| 11 | Data Science | [data-science-ms](https://catalog.tulane.edu/science-engineering/mathematics/data-science-ms/) |
| 12 | Earth and Environmental Sciences Thesis Research | [earth-environmental-sciences-thesis-research-ms](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/earth-environmental-sciences-thesis-research-ms/) |
| 13 | Earth and Environmental Sciences | [earth-environmental-sciences-ms](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/earth-environmental-sciences-ms/) |
| 14 | Ecology and Evolutionary Biology | [ecology-evolutionary-biology-ms](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/ecology-evolutionary-biology-ms/) |
| 15 | Electrical Engineering | [electrical-engineering-ms](https://catalog.tulane.edu/science-engineering/physics-engineering/electrical-engineering-ms/) |
| 16 | Interdisciplinary | [interdisciplinary-ms](https://catalog.tulane.edu/science-engineering/interdisciplinary-graduate-programs/interdisciplinary-ms/) |
| 17 | Materials Science and Engineering | [materials-science-engineering-ms](https://catalog.tulane.edu/science-engineering/physics-engineering/materials-science-engineering-ms/) |
| 18 | Mathematics | [mathematics-ms](https://catalog.tulane.edu/science-engineering/mathematics/mathematics-ms/) |
| 19 | Mechanical Engineering | [mechanical-engineering-ms](https://catalog.tulane.edu/science-engineering/physics-engineering/mechanical-engineering-ms/) |
| 20 | Neuroscience | [neuroscience-ms](https://catalog.tulane.edu/science-engineering/interdisciplinary-graduate-programs/neuroscience-ms/) |
| 21 | Physics | [physics-ms](https://catalog.tulane.edu/science-engineering/physics-engineering/physics-ms/) |
| 22 | Psychological Science | [psychological-science-ms](https://catalog.tulane.edu/science-engineering/psychology/psychological-science-ms/) |
| 23 | Psychology | [psychology-ms](https://catalog.tulane.edu/science-engineering/psychology/psychology-ms/) |
| 24 | River-Coastal Science and Engineering | [river-coastal-science-and-engineering-ms-non-residential](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/river-coastal-science-and-engineering-ms-non-residential/) |
| 25 | River-Coastal Science and Engineering | [river-coastal-science-and-engineering-ms-residential](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/river-coastal-science-and-engineering-ms-residential/) |
| 26 | Statistics | [statistics-ms](https://catalog.tulane.edu/science-engineering/mathematics/statistics-ms/) |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinnovation | [bioinnovation-phd](https://catalog.tulane.edu/science-engineering/interdisciplinary-graduate-programs/bioinnovation-phd/) |
| 2 | Biomedical Engineering | [biomedical-engineering-phd](https://catalog.tulane.edu/science-engineering/biomedical-engineering/biomedical-engineering-phd/) |
| 3 | Cell and Molecular Biology | [cell-molecular-biology-phd](https://catalog.tulane.edu/science-engineering/cell-molecular-biology/cell-molecular-biology-phd/) |
| 4 | Chemical and Biomolecular Engineering | [chemical-biomolecular-engineering-phd](https://catalog.tulane.edu/science-engineering/chemical-biomolecular-engineering/chemical-biomolecular-engineering-phd/) |
| 5 | Chemistry | [chemistry-phd](https://catalog.tulane.edu/science-engineering/chemistry/chemistry-phd/) |
| 6 | Computer Science | [computer-science-phd](https://catalog.tulane.edu/science-engineering/computer-science/computer-science-phd/) |
| 7 | Earth and Environmental Sciences | [earth-environmental-sciences-phd](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/earth-environmental-sciences-phd/) |
| 8 | Ecology and Evolutionary Biology | [ecology-evolutionary-biology-phd](https://catalog.tulane.edu/science-engineering/ecology-evolutionary-biology/ecology-evolutionary-biology-phd/) |
| 9 | Materials Physics and Engineering | [materials-physics-engineering-phd](https://catalog.tulane.edu/science-engineering/physics-engineering/materials-physics-engineering-phd/) |
| 10 | Mathematics | [mathematics-phd](https://catalog.tulane.edu/science-engineering/mathematics/mathematics-phd/) |
| 11 | Neuroscience | [neuroscience-phd](https://catalog.tulane.edu/science-engineering/interdisciplinary-graduate-programs/neuroscience-phd/) |
| 12 | Physics | [physics-phd](https://catalog.tulane.edu/science-engineering/physics-engineering/physics-phd/) |
| 13 | Psychology | [psychology-phd](https://catalog.tulane.edu/science-engineering/psychology/psychology-phd/) |
| 14 | River-Coastal Science and Engineering | [river-coastal-science-and-engineering-phd](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/river-coastal-science-and-engineering-phd/) |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Geographic Information Systems Certificate (Graduate) | [geographic-information-systems-certificate-graduate](https://catalog.tulane.edu/science-engineering/earth-environmental-sciences/geographic-information-systems-certificate-graduate/) |
| 2 | Health Psychology Certificate (Graduate) | [health-psychology-certificate-graduate](https://catalog.tulane.edu/science-engineering/psychology/health-psychology-certificate-graduate/) |
| 3 | River-Coastal Science and Engineering Certificate (Graduate) | [river-coastal-science-and-engineering-certificate-graduate](https://catalog.tulane.edu/science-engineering/river-coastal-science-engineering/river-coastal-science-and-engineering-certificate-graduate/) |
| 4 | Trauma Focused School Psychology Certificate (Graduate) | [trauma-focused-school-psychology-certificate-graduate](https://catalog.tulane.edu/science-engineering/psychology/trauma-focused-school-psychology-certificate-graduate/) |

##### MLAN/MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Degree in Landscape Architecture / River-Coastal Science and Engineering | [landscape-architecture-river-coastal-science-engineering-mlan-ms](https://catalog.tulane.edu/architecture/landscape-architecture/landscape-architecture-river-coastal-science-engineering-mlan-ms/) |

#### School of Professional Advancement
##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Emergency Management | [advanced-emergency-management-certificate-graduate](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/advanced-emergency-management-certificate-graduate/) |
| 2 | Cyber Technology Fundamentals | [cyber-technology-fundamentals-cer](https://catalog.tulane.edu/professional-advancement/information-technology/cyber-technology-fundamentals-cer/) |
| 3 | Cybersecurity | [cybersecurity-cer](https://catalog.tulane.edu/professional-advancement/information-technology/cybersecurity-cer/) |
| 4 | Data and Artificial Intelligence | [data-and-artificial-intelligence-cer](https://catalog.tulane.edu/professional-advancement/information-technology/data-and-artificial-intelligence-cer/) |
| 5 | Economic Development | [economic-development-cert](https://catalog.tulane.edu/professional-advancement/john-lewis-public-administration-program/economic-development-cert/) |
| 6 | Educational Leadership | [educational-leadership-certificate](https://catalog.tulane.edu/professional-advancement/education/educational-leadership-certificate/) |
| 7 | Emergency Management | [emergency-management-certificate-graduate](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/emergency-management-certificate-graduate/) |
| 8 | Environmental Management & Resilience | [environmental-management-resilience-cert](https://catalog.tulane.edu/professional-advancement/john-lewis-public-administration-program/environmental-management-resilience-cert/) |
| 9 | Homeland Security Defense | [homeland-security-defense-certificate-graduate](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/homeland-security-defense-certificate-graduate/) |
| 10 | Intelligence Studies | [intelligence-studies-certificate](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/intelligence-studies-certificate/) |
| 11 | Learning Experience Design | [learning-experience-design-certificate](https://catalog.tulane.edu/professional-advancement/education/learning-experience-design-certificate/) |
| 12 | Nonprofit and Strategic Philanthropy Management | [nonprofit-strategic-philanthropy-management-cert](https://catalog.tulane.edu/professional-advancement/john-lewis-public-administration-program/nonprofit-strategic-philanthropy-management-cert/) |
| 13 | Open Source Intelligence | [open-source-intelligence-cer](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/open-source-intelligence-cer/) |
| 14 | Security Management | [security-management-certificate-graduate](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/security-management-certificate-graduate/) |
| 15 | Special Education | [special-education-certificate](https://catalog.tulane.edu/professional-advancement/education/special-education-certificate/) |
| 16 | Sport Administration | [sport-administration-cert](https://catalog.tulane.edu/professional-advancement/kinesiology/sport-administration-cert/) |
| 17 | Sport Coaching | [sport-coaching-cert](https://catalog.tulane.edu/professional-advancement/kinesiology/sport-coaching-cert/) |
| 18 | Sport Security | [sport-security-certificate-graduate](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/sport-security-certificate-graduate/) |
| 19 | Strategic Communication Graduate Certificate | [strategic-communication-cer](https://catalog.tulane.edu/professional-advancement/media-design/strategic-communication-cer/) |
| 20 | Teaching English Learners | [teaching-english-learners-certificate](https://catalog.tulane.edu/professional-advancement/education/teaching-english-learners-certificate/) |
| 21 | Technology Leadership | [tech-leadership-cer](https://catalog.tulane.edu/professional-advancement/information-technology/tech-leadership-cer/) |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Cyber Technology | [cyber-technology-ms](https://catalog.tulane.edu/professional-advancement/information-technology/cyber-technology-ms/) |
| 2 | Sport Administration | [sports-administration-ms](https://catalog.tulane.edu/professional-advancement/kinesiology/sports-administration-ms/) |
| 3 | Sport Studies | [sport-studies-mpr](https://catalog.tulane.edu/professional-advancement/kinesiology/sport-studies-mpr/) |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Early Childhood Education | [early-childhood-education-mat](https://catalog.tulane.edu/professional-advancement/education/early-childhood-education-mat/) |
| 2 | Elementary Education | [elementary-education-mat](https://catalog.tulane.edu/professional-advancement/education/elementary-education-mat/) |
| 3 | Secondary Education | [secondary-education-mat](https://catalog.tulane.edu/professional-advancement/education/secondary-education-mat/) |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration (Emergency Management Concentration) | [public-administration-concentration-emergency-management-mpa](https://catalog.tulane.edu/professional-advancement/john-lewis-public-administration-program/public-administration-concentration-emergency-management-mpa/) |
| 2 | Public Administration (Public Health Concentration) | [public-administration-concentration-public-health-mpa](https://catalog.tulane.edu/professional-advancement/john-lewis-public-administration-program/public-administration-concentration-public-health-mpa/) |
| 3 | Public Administration | [public-administration-mpa](https://catalog.tulane.edu/professional-advancement/john-lewis-public-administration-program/public-administration-mpa/) |

##### MPS
| # | 项目 | URL |
|---|------|-----|
| 1 | Emergency Management | [emergency-management-mpr](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/emergency-management-mpr/) |
| 2 | Homeland Security Studies | [homeland-security-studies-mpr](https://catalog.tulane.edu/professional-advancement/emergency-security-studies/homeland-security-studies-mpr/) |

##### MLA
| # | 项目 | URL |
|---|------|-----|
| 1 | Liberal Arts | [liberal-arts-mla](https://catalog.tulane.edu/professional-advancement/humanities-social-sciences/liberal-arts-mla/) |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Education | [master-of-education-med](https://catalog.tulane.edu/professional-advancement/education/master-of-education-med/) |

#### Celia Scott Weatherhead School of Public Health and Tropical Medicine
##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | [biostatistics-mph](https://catalog.tulane.edu/public-health-tropical-medicine/biostatistics-data-science/biostatistics-mph/) |
| 2 | Community Health Sciences | [community-health-sciences-mph](https://catalog.tulane.edu/public-health-tropical-medicine/social--behavioral--and-population-sciences/community-health-sciences-mph/) |
| 3 | Disaster Management | [disaster-management-mph](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/disaster-management-mph/) |
| 4 | Environmental Health Sciences | [environmental-health-sciences-mph](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/environmental-health-sciences-mph/) |
| 5 | Epidemiology | [epidemiology-mph](https://catalog.tulane.edu/public-health-tropical-medicine/epidemiology/epidemiology-mph/) |
| 6 | Health Policy | [health-policy-mph](https://catalog.tulane.edu/public-health-tropical-medicine/health-policy-management/health-policy-mph/) |
| 7 | Health Systems Management | [health-systems-management-mph](https://catalog.tulane.edu/public-health-tropical-medicine/health-policy-management/health-systems-management-mph/) |
| 8 | International Health & Sustainable Development | [international-health-mph](https://catalog.tulane.edu/public-health-tropical-medicine/international-health--sustainable-development/international-health-mph/) |
| 9 | Maternal and Child Health | [maternal-child-health-mph](https://catalog.tulane.edu/public-health-tropical-medicine/social--behavioral--and-population-sciences/maternal-child-health-mph/) |
| 10 | Social | [social-behavioral-and-population-sciences-mph](https://catalog.tulane.edu/public-health-tropical-medicine/social--behavioral--and-population-sciences/social-behavioral-and-population-sciences-mph/) |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | [biostatistics-phd](https://catalog.tulane.edu/public-health-tropical-medicine/biostatistics-data-science/biostatistics-phd/) |
| 2 | Clinical Investigation | [clinical-investigation-phd](https://catalog.tulane.edu/public-health-tropical-medicine/epidemiology/clinical-investigation-phd/) |
| 3 | Environmental Health Sciences | [global-environmental-health-science-phd](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/global-environmental-health-science-phd/) |
| 4 | Epidemiology | [epidemiology-phd](https://catalog.tulane.edu/public-health-tropical-medicine/epidemiology/epidemiology-phd/) |
| 5 | Health Policy and Management | [health-policy-management-phd](https://catalog.tulane.edu/public-health-tropical-medicine/health-policy-management/health-policy-management-phd/) |
| 6 | International Health & Sustainable Development | [international-health-and-sustainable-development-phd](https://catalog.tulane.edu/public-health-tropical-medicine/international-health--sustainable-development/international-health-and-sustainable-development-phd/) |
| 7 | Social | [global-community-health-science-behavior-phd](https://catalog.tulane.edu/public-health-tropical-medicine/social--behavioral--and-population-sciences/global-community-health-science-behavior-phd/) |
| 8 | Tropical Medicine | [tropical-medicine-phd](https://catalog.tulane.edu/public-health-tropical-medicine/tropical-medicine-and-infectious-disease/tropical-medicine-phd/) |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | [biostatistics-ms](https://catalog.tulane.edu/public-health-tropical-medicine/biostatistics-data-science/biostatistics-ms/) |
| 2 | Clinical Investigation | [clinical-investigation-ms](https://catalog.tulane.edu/public-health-tropical-medicine/epidemiology/clinical-investigation-ms/) |
| 3 | Data Modeling and Analytics for Health | [data-modeling-and-analytics-for-health-ms](https://catalog.tulane.edu/public-health-tropical-medicine/biostatistics-data-science/data-modeling-and-analytics-for-health-ms/) |
| 4 | Epidemiology | [epidemiology-ms](https://catalog.tulane.edu/public-health-tropical-medicine/epidemiology/epidemiology-ms/) |
| 5 | Health Security | [health-security-ms](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/health-security-ms/) |
| 6 | Occupational and Environmental Health Sciences | [occupational-and-environmental-health-sciences-ms](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/occupational-and-environmental-health-sciences-ms/) |
| 7 | Tropical Medicine | [tropical-medicine-ms](https://catalog.tulane.edu/public-health-tropical-medicine/tropical-medicine-and-infectious-disease/tropical-medicine-ms/) |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics Certificate (Graduate) | [biostatistics-certificate](https://catalog.tulane.edu/public-health-tropical-medicine/biostatistics-data-science/biostatistics-certificate/) |
| 2 | Clinical Tropical Medicine Certificate (Graduate) | [tropical-medicine-certificate](https://catalog.tulane.edu/public-health-tropical-medicine/tropical-medicine-and-infectious-disease/tropical-medicine-certificate/) |
| 3 | Disaster Management Certificate (Graduate) | [disaster-management-certificate](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/disaster-management-certificate/) |
| 4 | Industrial Hygiene Certificate (Graduate) | [industrial-hygiene-certificate](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/industrial-hygiene-certificate/) |
| 5 | Public Health Certificate (Graduate) | [public-health-certificate-graduate](https://catalog.tulane.edu/public-health-tropical-medicine/public-health-certificate-graduate/) |

##### MHA
| # | 项目 | URL |
|---|------|-----|
| 1 | BS/MHA or BSM/MHA Accelerated Degrees | [bs-mha](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/bs-mha/) |
| 2 | BSPH/MPH or MSPH or MPHTM or MHA Accelerated Degree | [bsph-mph-msph-mphtm-mha](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/bsph-mph-msph-mphtm-mha/) |
| 3 | Health Administration | [master-health-administration-mha](https://catalog.tulane.edu/public-health-tropical-medicine/health-policy-management/master-health-administration-mha/) |
| 4 | JD/MPH or MHA Dual Degrees | [jd-mph-mha](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/jd-mph-mha/) |
| 5 | MBA/MHA Dual Degree | [mba-mha](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/mba-mha/) |

##### MSPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | [biostatistics-msp](https://catalog.tulane.edu/public-health-tropical-medicine/biostatistics-data-science/biostatistics-msp/) |
| 2 | Industrial Hygiene | [environmental-health-industrial-hygiene-msp](https://catalog.tulane.edu/public-health-tropical-medicine/environmental-health-sciences/environmental-health-industrial-hygiene-msp/) |
| 3 | Nutrition | [nutrition-msph](https://catalog.tulane.edu/public-health-tropical-medicine/social--behavioral--and-population-sciences/nutrition-msph/) |

##### MPHTM
| # | 项目 | URL |
|---|------|-----|
| 1 | BS or BSM/MPH | [bs-mph-msph-mphtm](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/bs-mph-msph-mphtm/) |
| 2 | MD/MPH or MSPH or MPHTM Dual Degree | [md-mph-msph-mphtm](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/md-mph-msph-mphtm/) |
| 3 | Public Health and Tropical Medicine | [public-health-tropical-medicine-mphtm](https://catalog.tulane.edu/public-health-tropical-medicine/tropical-medicine-and-infectious-disease/public-health-tropical-medicine-mphtm/) |

##### DrPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Leadership for International Health and Sustainable Development | [leadership-for-international-health-and-sustainable-development-drph](https://catalog.tulane.edu/public-health-tropical-medicine/international-health--sustainable-development/leadership-for-international-health-and-sustainable-development-drph/) |
| 2 | Leadership in Social and Behavioral Sciences | [leadership-in-social-and-behavioral-sciencesdrph](https://catalog.tulane.edu/public-health-tropical-medicine/leadership-in-social-and-behavioral-sciencesdrph/) |

##### DI
| # | 项目 | URL |
|---|------|-----|
| 1 | Dietetic Internship | [dietetic-internship](https://catalog.tulane.edu/public-health-tropical-medicine/social--behavioral--and-population-sciences/dietetic-internship/) |

#### A. B. Freeman School of Business
##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | [business-executive-mba](https://catalog.tulane.edu/business/mba/business-executive-mba/) |
| 2 | Business Administration | [business-full-time-mba](https://catalog.tulane.edu/business/mba/business-full-time-mba/) |
| 3 | Business Administration | [business-online-mba](https://catalog.tulane.edu/business/mba/business-online-mba/) |
| 4 | Business Administration | [business-professional-mba](https://catalog.tulane.edu/business/mba/business-professional-mba/) |
| 5 | Executive Master of Business Administration (EMBA) | [business-international-executive-mba](https://catalog.tulane.edu/business/mba/business-international-executive-mba/) |

##### MFN
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance | [finance-mfn](https://catalog.tulane.edu/business/finance/finance-mfn/) |
| 2 | Master of Finance (MFN) | [international-finance-mfn](https://catalog.tulane.edu/business/finance/international-finance-mfn/) |

##### MME
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Management in Energy (MME) | [business-international-mme](https://catalog.tulane.edu/business/energy/business-international-mme/) |
| 2 | Master of Management in Energy | [energy-mme](https://catalog.tulane.edu/business/energy/energy-mme/) |

##### MACCT
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | [accounting-mac](https://catalog.tulane.edu/business/accounting/accounting-mac/) |

##### MAN
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics and AI | [business-analytics-and-ai-man](https://catalog.tulane.edu/business/business-analytics/business-analytics-and-ai-man/) |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business | [business-phd](https://catalog.tulane.edu/business/finance/business-phd/) |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Global Management (MGM) | [global-management-mgm](https://catalog.tulane.edu/business/global-management/global-management-mgm/) |

##### MMG
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Management | [master-management-mmg](https://catalog.tulane.edu/business/management/master-management-mmg/) |

#### School of Medicine
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomic Pathology | [anatomic-pathology-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/anatomic-pathology-ms/) |
| 2 | Anatomy Research | [anatomy-research-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/anatomy-research-ms/) |
| 3 | Anatomy | [anatomy-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/anatomy-ms/) |
| 4 | Biochemistry and Applied Bioinformatics | [biochemistry-and-applied-bioinformatics](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biochemistry-and-applied-bioinformatics/) |
| 5 | Biochemistry and Molecular Biology | [biochemistry-molecular-biology-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biochemistry-molecular-biology-ms/) |
| 6 | Bioethics and Medical Humanities | [bioethics-medical-humanities-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/bioethics-medical-humanities-ms/) |
| 7 | Biomedical Informatics | [biomedical-bioinformatics-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biomedical-bioinformatics-ms/) |
| 8 | Clinical Anatomy | [clinical-anatomy-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/clinical-anatomy-ms/) |
| 9 | Clinical Research Methods | [clinical-research-methods-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/clinical-research-methods-ms/) |
| 10 | Clinical Research | [clinical-research-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/clinical-research-ms/) |
| 11 | Medical Genetics and Genomics | [medical-genetics-genomics-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/medical-genetics-genomics-ms/) |
| 12 | Medical Sciences | [medical-sciences-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/medical-sciences-ms/) |
| 13 | Microbiology and Immunology | [microbiology-immunology-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/microbiology-immunology-ms/) |
| 14 | Molecular Medicine and Health Sciences | [molecular-medicine-and-health-sciences-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/molecular-medicine-and-health-sciences-ms/) |
| 15 | Pharmacology | [pharmacology-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/pharmacology-ms/) |
| 16 | Physiology | [physiology-ms](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/physiology-ms/) |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aging Studies | [aging-studies-phd](https://catalog.tulane.edu/medicine/tulane-center-for-aging/aging-studies-phd/) |
| 2 | Biomedical Sciences | [biomedical-sciences-phd](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biomedical-sciences-phd/) |
| 3 | Biomedical Sciences | [biomedical-sciences-phd-biomedical-informatics-concentration](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biomedical-sciences-phd-biomedical-informatics-concentration/) |
| 4 | Biomedical Sciences | [biomedical-sciences-phd-microbiology-and-immunology-concentration](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biomedical-sciences-phd-microbiology-and-immunology-concentration/) |
| 5 | Biomedical Sciences | [biomedical-sciences-phd-pharmacology-concentration](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/biomedical-sciences-phd-pharmacology-concentration/) |
| 6 | MD/PhD | [md-phd](https://catalog.tulane.edu/medicine/combined-degrees/md-phd/) |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Ethics Certificate (Graduate) | [clinical-ethics-cer](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/clinical-ethics-cer/) |
| 2 | Clinical Research Certificate (Graduate) | [clinical-research-certificate](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/clinical-research-certificate/) |
| 3 | Medical Humanities Certificate (Graduate) | [medical-humanities-cer](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/medical-humanities-cer/) |
| 4 | Research Ethics Certificate (Graduate) | [research-ethics-cer](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/research-ethics-cer/) |
| 5 | Sports Medicine Certificate (Graduate) | [sports-medicine-cer](https://catalog.tulane.edu/medicine/biomedical-sciences-graduate-program/sports-medicine-cer/) |

##### MD/MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | MD/MBA | [md-mba](https://catalog.tulane.edu/medicine/combined-degrees/md-mba/) |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | MD/MPH | [md-mph](https://catalog.tulane.edu/medicine/combined-degrees/md-mph/) |

##### MD/MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MD/MS in Bioethics and Medical Humanities | [md-ms-bioethics-medical-humanities](https://catalog.tulane.edu/medicine/combined-degrees/md-ms-bioethics-medical-humanities/) |

##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | [medicine-md](https://catalog.tulane.edu/medicine/medicine/medicine-md/) |

#### School of Architecture and Built Environment
##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Historic Preservation | [historic-preservation-cer](https://catalog.tulane.edu/architecture/preservation/historic-preservation-cer/) |
| 2 | Public Interest Design Certificate (Graduate) | [public-interest-design-cer](https://catalog.tulane.edu/architecture/social-innovation-entrepreneurship/public-interest-design-cer/) |
| 3 | Sustainable Real Estate Development Certificate (Graduate) | [sustainable-real-estate-development-cer](https://catalog.tulane.edu/architecture/real-estate-development/sustainable-real-estate-development-cer/) |
| 4 | Sustainable Urbanism Certificate (Graduate) | [sustainable-urbanism-certificate-graduate](https://catalog.tulane.edu/architecture/sustainable-urbanism/sustainable-urbanism-certificate-graduate/) |

##### M.Arch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | [architecture-march](https://catalog.tulane.edu/architecture/architecture/architecture-march/) |
| 2 | Master of Architecture / Master of Science in Historic Preservation | [march-ms](https://catalog.tulane.edu/architecture/combined-degrees/march-ms/) |
| 3 | Master of Architecture / Master of Sustainable Real Estate Development | [march-msred](https://catalog.tulane.edu/architecture/combined-degrees/march-msred/) |

##### M.S.Arc
| # | 项目 | URL |
|---|------|-----|
| 1 | Architectural Research and Design | [architecture-research-design](https://catalog.tulane.edu/architecture/architecture/architecture-research-design/) |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Historic Preservation | [historic-preservation-ms](https://catalog.tulane.edu/architecture/preservation/historic-preservation-ms/) |

##### MSR
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainable Real Estate Development | [sustainable-real-estate-development-msr](https://catalog.tulane.edu/architecture/real-estate-development/sustainable-real-estate-development-msr/) |

#### School of Law
##### MJ
| # | 项目 | URL |
|---|------|-----|
| 1 | Energy Law | [energy-law](https://catalog.tulane.edu/law/master-jurisprudence/energy-law/) |
| 2 | Labor and Employment | [labor-and-employment](https://catalog.tulane.edu/law/master-jurisprudence/labor-and-employment/) |
| 3 | Master of Jurisprudence | [master-jurisprudence](https://catalog.tulane.edu/law/master-jurisprudence/) |

##### LMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Admiralty | [admiralty-lma](https://catalog.tulane.edu/law/master-laws/admiralty-lma/) |

##### AML
| # | 项目 | URL |
|---|------|-----|
| 1 | American Law | [american-law-aml](https://catalog.tulane.edu/law/master-laws/american-law-aml/) |

##### SJD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Juridical Science | [doctor-juridical-studies](https://catalog.tulane.edu/law/doctor-juridical-studies/) |

##### MEL
| # | 项目 | URL |
|---|------|-----|
| 1 | Energy & Environment | [environmental-law-mel](https://catalog.tulane.edu/law/master-laws/environmental-law-mel/) |

##### MJL
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Law | [environmental-law](https://catalog.tulane.edu/law/master-jurisprudence/environmental-law/) |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | General Law | [general-law-llm](https://catalog.tulane.edu/law/master-laws/general-law-llm/) |

##### LMI
| # | 项目 | URL |
|---|------|-----|
| 1 | International and Comparative Law | [international-law-lmi](https://catalog.tulane.edu/law/master-laws/international-law-lmi/) |

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | [juris-doctor](https://catalog.tulane.edu/law/juris-doctor/) |

#### School of Social Work
##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Disaster Resilience Leadership Studies Certificate (Graduate) | [disaster-resilience-leadership-studies-certificate](https://catalog.tulane.edu/social-work/disaster-resilience/disaster-resilience-leadership-studies-certificate/) |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Disaster Resilience Leadership Studies | [disaster-resilience-leadership-studies-ms](https://catalog.tulane.edu/social-work/disaster-resilience/disaster-resilience-leadership-studies-ms/) |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Integrated Clinical in Community Practice in Social Work | [integrated-clinical-community-practice-social-work-msw](https://catalog.tulane.edu/social-work/social-work/integrated-clinical-community-practice-social-work-msw/) |

##### MSW/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Public Health Dual Degree | [msw-mph](https://catalog.tulane.edu/public-health-tropical-medicine/joint-combined-degrees/msw-mph/) |

##### DSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | [social-work-dsw](https://catalog.tulane.edu/social-work/social-work/social-work-dsw/) |

### 2.2 研究生招生模式

Tulane的研究生招生完全去中心化（fully decentralized）：各学院独立管理招生、设定截止日期、收取申请费。没有统一的研究生申请门户。OGPS (ogps.tulane.edu) 提供协调服务。

---

## 3. 申请要求与截止日期

### 3.1 本科申请 - 核心数据表

| 维度 | 内容 |
|------|------|
| 招生网站 | https://admission.tulane.edu/ |
| 申请系统 | Common Application |
| Early Decision (ED) | November 1 (binding) |
| ED 决定发布 | by December 15 |
| ED 押金截止 | January 15 |
| Early Action (EA) | November 10 (non-binding) |
| EA 决定发布 | by January 10 |
| EA 押金截止 | May 1 |
| Early Decision II (ED II) | January 15 (binding) |
| ED II 决定发布 | by February 15 |
| ED II 押金截止 | March 1 |
| Regular Decision (RD) | January 15 |
| RD 决定发布 | by April 1 |
| RD 押金截止 | May 1 |
| SAT/ACT | Optional (test-optional for Fall 2027) |
| 推荐提交分数 | SAT 1300+ / ACT 28+ |
| Superscore | Yes (SAT and ACT) |
| SAT Code | 6832 |
| ACT Code | 1614 |
| 推荐信 | 仅需School Counselor Recommendation |
| 面试 | 不要求 (国际生可选InitialView/Vericant) |
| CSS Profile Code | 6832 |
| FAFSA Code | 002029 |

### 3.2 本科英语能力要求

| 考试 | 最低要求 | 推荐分数 | 备注 |
|------|---------|---------|------|
| TOEFL iBT | 95 | - | Institution code: 6832 |
| IELTS | Accepted | - | 未公布最低分 |
| Duolingo English Test | Accepted | - | 未公布最低分 |
| Cambridge C1/C2 | Accepted | - | 未公布最低分 |

> 适用于非英语母语申请者。

### 3.3 研究生申请 - 通用规则

- 招生模式: 完全去中心化，各学院独立管理
- GRE/GMAT: 因项目而异
- TOEFL/IELTS: 因项目而异
- OGPS: ogps.tulane.edu (协调服务)

---

## 4. 费用与财务援助

### 4.1 本科费用 (2026-2027学年)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition (学费) | $70,622 | |
| Mandatory Fees (必缴费用) | $4,514 | Academic Service, Health Center, Student Activity, Reily Recreation Center |
| Housing (住宿) | $11,738 | 双人间communal-style |
| Meals (餐饮) | $8,780 | 最低meal plan |
| Books & Supplies | $1,200 | NTC Undergrad Bundle |
| Transportation | varies | |
| Miscellaneous | $1,778 | |
| Loan Fees | $58 | |
| **总计 (Total COA)** | **$98,710** | |

> Source: https://admission.tulane.edu/tuition-aid/cost

### 4.2 本科财务援助政策

- Need-aware (国际): 国际生最多可获得$30,000 need-based aid
- Merit Scholarships: 所有申请者自动考虑，范围$1,000至全额学费
- No-Loan Program: NOLA Scholarship为中低收入家庭提供无贷款方案
- 国际生奖学金: Global Scholarship, Latin American Scholars Award, South Asian Scholars Award, Sub-Saharan Africa Leadership Award
- CSS Profile + FAFSA: 均需提交
- Net Price Calculator: https://admission.tulane.edu/tuition-aid/net-price-calculator

### 4.3 研究生费用与资助

- 资助类型: 因项目而异（Fully funded PhD / Self-funded masters）
- 常见资助形式: RA, TA, Fellowship, Grant
- 详细费用: https://studentaccounts.tulane.edu/tuition-and-fees

---

## 5. 证据链索引 (Evidence Chain Index)

#### E-U-001
```yaml
field: undergraduate.deadlines.ED
value: "November 1"
source_url: https://admission.tulane.edu/apply/deadlines-forms
source_snippet: "First-Year Early Decision Application Due"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-002
```yaml
field: undergraduate.deadlines.EA
value: "November 10"
source_url: https://admission.tulane.edu/apply/deadlines-forms
source_snippet: "First-Year Early Action Application Due"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-003
```yaml
field: undergraduate.deadlines.ED_II
value: "January 15"
source_url: https://admission.tulane.edu/apply/deadlines-forms
source_snippet: "First-Year Early Decision II Application Due"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-004
```yaml
field: undergraduate.deadlines.RD
value: "January 15"
source_url: https://admission.tulane.edu/apply/deadlines-forms
source_snippet: "First-Year Regular Decision Application Due"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-005
```yaml
field: undergraduate.test_policy
value: "Test-Optional"
source_url: https://admission.tulane.edu/apply/instructions/standardized-tests
source_snippet: "The submission of SAT or ACT scores will remain optional for Fall 2027"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-006
```yaml
field: undergraduate.test_policy.recommended
value: "SAT 1300+ / ACT 28+"
source_url: https://admission.tulane.edu/apply/instructions/standardized-tests
source_snippet: "we will encourage students with a 1300 or higher on the SAT and a 28 on the ACT"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-007
```yaml
field: undergraduate.english.tofl_min
value: "95"
source_url: https://admission.tulane.edu/international
source_snippet: "TOEFL iBT minimum score: 95"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-008
```yaml
field: undergraduate.cost.tuition
value: "$70,622"
source_url: https://admission.tulane.edu/tuition-aid/cost
source_snippet: "Tuition $70,622"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-009
```yaml
field: undergraduate.cost.total
value: "$98,710"
source_url: https://admission.tulane.edu/tuition-aid/cost
source_snippet: "TOTAL $98,710"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-U-010
```yaml
field: undergraduate.aid.intl
value: "Up to $30,000"
source_url: https://admission.tulane.edu/international/aid
source_snippet: "Tulane offers up to $30,000 in need-based financial aid to international students"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-G-001
```yaml
field: graduate.admissions.model
value: "Fully decentralized"
source_url: https://admission.tulane.edu/apply
source_snippet: "Each school at Tulane administers its own admission process for graduate students"
capture_date: 2026-07-06
evidence_type: official_webpage
```

#### E-G-002
```yaml
field: programs.total
value: "452"
source_url: https://catalog.tulane.edu/programs/
source_snippet: "Catalog extraction: 452 program items"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## 6. WeKnora导入清单

### Collection结构

```
tulane-knowledge-base-v2/
+- 00-institution-overview.md
+- 01-ug-liberal-arts.md
+- 02-ug-science-engineering.md
+- 03-ug-architecture.md
+- 04-ug-business.md
+- 05-ug-public-health.md
+- 06-ug-sopa.md
+- 07-grad-liberal-arts.md
+- 08-grad-science-engineering.md
+- 09-grad-business.md
+- 10-grad-public-health.md
+- 11-grad-medicine.md
+- 12-grad-law.md
+- 13-grad-social-work.md
+- 14-grad-architecture.md
+- 15-grad-sopa.md
+- 16-deadlines-requirements.md
+- 17-costs-financial-aid.md
+- 18-evidence-chain.md
```

### Follow-up data items

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | 确认Need-blind政策（国内） | financialaid.tulane.edu |
| P0 | 确认申请费金额 | admission.tulane.edu/apply |
| P1 | 各研究生项目详细截止日期 | 各学院网站 |
| P1 | TOEFL/IELTS具体最低分 | admission.tulane.edu/international |
| P2 | 各研究生项目学费 | studentaccounts.tulane.edu |

---

## 7. 跨校比较框架

| 维度 | Tulane |
|------|--------|
| 类型 | Private R1 |
| 位置 | New Orleans, LA |
| 本科COA/年 | $98,710 (2026-2027) |
| 学费/年 | $70,622 |
| Need-aware (国际) | Yes (up to $30k) |
| EA截止 | November 10 |
| ED截止 | November 1 |
| RD截止 | January 15 |
| SAT/ACT | Optional |
| TOEFL最低 | 95 |
| 项目总数 | 452 |
| 学院数 | 9 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admission.tulane.edu, catalog.tulane.edu, tulane.edu, financialaid.tulane.edu, ogps.tulane.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school - department - degree-level - program