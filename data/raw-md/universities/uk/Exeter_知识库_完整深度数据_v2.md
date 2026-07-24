# University of Exeter Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch (multi-page extraction)
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 基本信息

| 维度 | 值 |
|------|-----|
| 学校全称 | University of Exeter |
| QS 世界排名 | ~150 (2026) |
| 罗素集团 | Yes |
| TEF 评级 | Gold |
| 所在城市 | Exeter, Devon, England |
| 校区 | Streatham Campus (Exeter), St Luke's Campus (Exeter), Penryn Campus (Cornwall) |
| UCAS 代码 | E84 EXETR |
| 创校年份 | 1955 (received Royal Charter) |
| 学校类型 | Public research university |

### 0.2 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | 252 (200-210 unique by URL) |
| 研究生授课型 (PGT) | 216 (~170 unique) |
| 研究生研究型 (PGR) | 42 research areas |
| 学院总数 | 3 faculties |
| 系所/学院总数 | ~25 departments/schools |

### 0.3 学院 / 系层级结构 (Rule 2 — hierarchy)

#### Faculty of Environment, Science and Economy
- Computer Science
- Earth and Environmental Sciences (including Camborne School of Mines)
- Ecology and Conservation
- Engineering
- Geography
- Mathematics and Statistics
- Physics and Astronomy
- University of Exeter Business School
  - Economics
  - Finance and Accounting
  - Management
- Research Institutes: Environment and Sustainability Institute, Institute for Data Science and Artificial Intelligence, Global Systems Institute

#### Faculty of Humanities, Arts and Social Sciences
- Arab and Islamic Studies
- Archaeology and History
- Classics, Ancient History, Religion and Theology
- Communications, Drama and Film
- English and Creative Writing
- Humanities and Social Sciences, Cornwall
- Languages, Cultures and Visual Studies
- School of Education
- Social and Political Sciences, Philosophy, and Anthropology
- Law School
- Research Institute: Societies and Cultures Institute

#### Faculty of Health and Life Sciences
- Biosciences
- Health and Care Professions
- Psychology
- University of Exeter Medical School
  - Clinical and Biomedical Sciences
  - Health and Community Sciences
  - Public Health and Sport Sciences
- Research Institute: Living Systems Institute

### 0.4 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 级别 | 数量 |
|---------|------|------|
| BA | UG | ~89 |
| BSc | UG | ~98 |
| BEng | UG | ~22 |
| MEng | UG | ~15 |
| MSci | UG | ~18 |
| MPhys | UG | ~5 |
| MMath | UG | ~1 |
| LLB | UG | ~10 |
| BBL | UG | 1 |
| BMBS | UG | 1 |
| BA/BSc | UG | ~2 |
| Foundation | UG | ~10 |
| MSc | PGT | ~120 |
| MA | PGT | ~45 |
| LLM | PGT | ~12 |
| MRes | PGT | ~6 |
| MBA | PGT | 1 |
| MFA | PGT | 1 |
| MPH | PGT | 1 |
| MPA | PGT | 1 |
| MEd | PGT | 1 |
| PGCE | PGT | 1 |
| PhD | PGR | 42 areas |
| MPhil | PGR | 42 areas |

### 0.5 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 | BA | BSc | BEng | MEng | MSci | MPhys | LLB | BBL | BMBS | 其他 |
|------|-----|------|------|------|------|-------|-----|-----|------|------|
| Environment, Science and Economy | 5 | 95 | 22 | 15 | 18 | 5 | 0 | 0 | 0 | 1 (MMath) |
| Humanities, Arts and Social Sciences | 82 | 3 | 0 | 0 | 0 | 0 | 10 | 1 | 0 | 1 (BA/BSc) |
| Health and Life Sciences | 0 | 8 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |

### 0.6 结构性规则 (Rule 5 — structural rules)

1. **UG 课程命名**: URL 模式为 `/undergraduate-degrees/{degree}-{program-name}/`，学位缩写在 URL 开头
2. **PGT 课程命名**: URL 模式为 `/masters-degrees/{degree}-{program-name}/`
3. **学位层级**: MSci/MEng/MPhys/MMath 是 4 年制综合硕士，BEng 是 3 年制工程学士
4. **Cornwall 校区**: 部分课程标注 (Cornwall)，在 Penryn 校区授课
5. **中外合作**: 部分课程标注 (at ZJUT, China)，与浙江工业大学联合办学

---

## SECTION 1 — Undergraduate education

### 1.1 本科课程完整列表

#### Accounting and Finance (6 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Accounting and Business | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-accounting-and-business/ |
| Accounting and Finance | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-accounting-and-finance/ |
| Finance | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-finance/ |
| Finance: Business Management | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-finance-business-management/ |
| Finance: Data Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-finance-data-science/ |
| Finance: Investment Banking | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-finance-investment-banking/ |

#### Anthropology (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Anthropology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-anthropology/ |
| Archaeology and Anthropology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-archaeology-and-anthropology/ |
| Sociology and Anthropology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology-and-anthropology/ |

#### Arab and Islamic Studies (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Arabic and Islamic Studies | MArabic | https://www.exeter.ac.uk/undergraduate-degrees/marabic-arab-and-islamic-studies/ |
| Arabic and Politics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-arabic-and-politics/ |
| Middle East Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-middle-east-studies/ |
| Modern Languages and Arabic | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-modern-languages-and-arabic/ |

#### Archaeology (6 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Archaeology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-archaeology/ |
| Archaeological Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-archaeological-science/ |
| Archaeology with Forensic Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-archaeology-with-forensic-science/ |
| Archaeology and Anthropology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-archaeology-and-anthropology/ |
| Ancient History and Archaeology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-ancient-history-and-archaeology/ |
| History and Archaeology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-archaeology/ |

#### Art History and Visual Culture (7 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Art History & Visual Culture | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture/ |
| Art History & Visual Culture and Classical Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-classical-studies/ |
| Art History & Visual Culture and Drama | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-drama/ |
| Art History & Visual Culture and English | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-english/ |
| Art History & Visual Culture and Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-film-and-television-studies/ |
| Art History & Visual Culture and History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-history/ |
| Art History & Visual Culture and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-modern-languages/ |

#### Artificial Intelligence (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Artificial Intelligence | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-artificial-intelligence/ |
| Artificial Intelligence | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-artificial-intelligence/ |
| Artificial Intelligence with Foundation Year | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-artificial-intelligence-with-foundation-year/ |

#### Biomedical Sciences (1 course)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Biomedical Sciences | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-biomedical-sciences/ |

#### Biosciences (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Biochemistry | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-biochemistry/ |
| Biochemistry | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-biochemistry/ |
| Biological Sciences | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-biological-sciences/ |
| Biological Sciences | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-biological-sciences/ |

#### Business and Management (10 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Accounting and Business | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-accounting-and-business/ |
| Bachelor of Business and Laws (Cornwall) | BBL | https://www.exeter.ac.uk/undergraduate-degrees/bbl-bachelor-of-business-and-laws-cornwall/ |
| Business (Cornwall) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-business-cornwall/ |
| Business Analytics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-business-analytics/ |
| Business and Environment (Cornwall) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-business-and-environment-cornwall/ |
| Business and Management | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-business-and-management/ |
| International Business and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-international-business-and-modern-languages/ |
| Law with Business (Cornwall) | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-with-business-cornwall/ |
| Marketing and Management | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-marketing-and-management/ |
| Politics and Business (Cornwall) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-politics-and-business-cornwall/ |

#### Classics and Ancient History (10 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Ancient History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-ancient-history/ |
| Ancient History and Archaeology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-ancient-history-and-archaeology/ |
| Classics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classics/ |
| Classical Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies/ |
| Classical Studies and English | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-english/ |
| Classical Studies and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-modern-languages/ |
| Classical Studies and Philosophy | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-philosophy/ |
| Classical Studies and Religion | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-religion/ |
| Art History & Visual Culture and Classical Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-classical-studies/ |
| Modern Languages and Latin | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-modern-languages-and-latin/ |

#### Comparative Literatures and Cultures (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Comparative Literatures and Cultures | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-comparative-literatures-and-cultures/ |
| Comparative Literatures and Cultures and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-comparative-literatures-and-cultures-and-modern-languages/ |

#### Computer Science (6 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Computer Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-computer-science/ |
| Computer Science | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-computer-science/ |
| Computer Science with Foundation Year | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-computer-science-with-foundation-year/ |
| Computer Science and Mathematics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-computer-science-and-mathematics/ |
| Computer Science and Mathematics | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-computer-science-and-mathematics/ |
| Digital Media Technology (at ZJUT, China) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-digital-media-technology-zjut-china/ |

#### Criminology (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Criminology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-criminology/ |
| Sociology and Criminology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology-and-criminology/ |

#### Data Science (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Data Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-data-science/ |
| Data Science | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-data-science/ |
| Data Science with Foundation Year | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-data-science-with-foundation-year/ |
| Data Science (at ZJUT, China) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-data-science-zjut-china/ |

#### Drama (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Drama | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-drama/ |
| Drama and Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-drama-and-film-and-television-studies/ |
| Art History & Visual Culture and Drama | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-drama/ |
| English and Drama | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-drama/ |

#### Ecology and Conservation (9 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Animal Behaviour | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-animal-behaviour/ |
| Animal Behaviour | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-animal-behaviour/ |
| Conservation Biology and Ecology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-conservation-biology-and-ecology/ |
| Conservation Biology and Ecology | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-conservation-biology-and-ecology/ |
| Evolutionary Biology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-evolutionary-biology/ |
| Evolutionary Biology | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-evolutionary-biology/ |
| Global Sustainability | BA/BSc | https://www.exeter.ac.uk/undergraduate-degrees/ba-bsc-global-sustainability/ |
| Zoology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-zoology/ |
| Zoology | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-zoology/ |

#### Economics (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Business Economics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-business-economics/ |
| Economics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-economics/ |
| Economics and Finance | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-economics-and-finance/ |
| Economics and Politics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-economics-and-politics/ |

#### Engineering (35 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Biomedical Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-biomedical-engineering/ |
| Biomedical Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-biomedical-engineering/ |
| Biomedical Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-biomedical-engineering-with-foundation-year/ |
| Chemical Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-chemical-engineering/ |
| Chemical Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-chemical-engineering/ |
| Chemical Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-chemical-engineering-with-foundation-year/ |
| Civil Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-civil-engineering/ |
| Civil Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-civil-engineering/ |
| Civil Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-civil-engineering-with-foundation-year/ |
| Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-engineering/ |
| Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-engineering/ |
| Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-engineering-with-foundation-year/ |
| Electrical and Electronic Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-electrical-and-electronic-engineering/ |
| Electrical and Electronic Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-electrical-and-electronic-engineering/ |
| Electrical and Electronic Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-electrical-and-electronic-engineering-with-foundation-year/ |
| Engineering and Entrepreneurship | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-engineering-and-entrepreneurship/ |
| Engineering and Entrepreneurship | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-engineering-and-entrepreneurship/ |
| Engineering and Management | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-engineering-and-management/ |
| Engineering and Management | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-engineering-and-management/ |
| Environmental Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-environmental-engineering/ |
| Environmental Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-environmental-engineering/ |
| Environmental Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-environmental-engineering-with-foundation-year/ |
| Mechanical Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-mechanical-engineering/ |
| Mechanical Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-mechanical-engineering/ |
| Mechanical Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-mechanical-engineering-with-foundation-year/ |
| Renewable Energy Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-renewable-energy-engineering/ |
| Renewable Energy Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-renewable-energy-engineering/ |
| Renewable Energy Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-renewable-energy-engineering-with-foundation-year/ |
| Robotics and Artificial Intelligence | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-robotics-and-artificial-intelligence/ |
| Robotics and Artificial Intelligence | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-robotics-and-artificial-intelligence/ |
| Robotics and Artificial Intelligence with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-robotics-and-artificial-intelligence-with-foundation-year/ |
| Systems Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-systems-engineering/ |
| Systems Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-systems-engineering/ |
| Systems Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-systems-engineering-with-foundation-year/ |
| Energy and Environmental Engineering (at ZJUT, China) | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-energy-and-environmental-engineering-zjut-china/ |

#### English (10 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| English | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english/ |
| English and Creative Writing | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-creative-writing/ |
| English and Drama | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-drama/ |
| English and Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-film-and-television-studies/ |
| English and History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-history/ |
| English and Media & Communications | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-media-and-communications/ |
| English and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-modern-languages/ |
| English with Study in North America | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-with-study-in-north-america/ |
| Art History & Visual Culture and English | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-english/ |
| Classical Studies and English | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-english/ |

#### Environmental Sciences and Humanities (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Environmental Humanities | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-environmental-humanities/ |
| Environmental Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-environmental-science/ |
| Global Sustainability | BA/BSc | https://www.exeter.ac.uk/undergraduate-degrees/ba-bsc-global-sustainability/ |

#### Film Studies (6 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-film-and-television-studies/ |
| Film & Television Studies and Media & Communications | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-film-and-television-studies-and-media-and-communications/ |
| Art History & Visual Culture and Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-film-and-television-studies/ |
| Drama and Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-drama-and-film-and-television-studies/ |
| English and Film & Television Studies | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-film-and-television-studies/ |
| Film & Television Studies and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-film-and-television-studies-and-modern-languages/ |

#### Geography (5 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Geography | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-geography/ |
| Geography | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-geography/ |
| Geography (Cornwall) | BA/BSc | https://www.exeter.ac.uk/undergraduate-degrees/ba-bsc-geography-cornwall/ |
| Geography with Applied GIS | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-geography-with-applied-gis/ |
| Politics and Geography (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-and-geography-cornwall/ |

#### Geology (8 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Engineering Geology and Geotechnics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-engineering-geology-and-geotechnics/ |
| Engineering Geology and Geotechnics | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-engineering-geology-and-geotechnics/ |
| Environmental Geoscience | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-environmental-geoscience/ |
| Environmental Geoscience | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-environmental-geoscience/ |
| Geology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-geology/ |
| Geology | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-geology/ |
| Resource and Exploration Geology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-resource-and-exploration-geology/ |
| Resource and Exploration Geology | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-resource-and-exploration-geology/ |

#### History (12 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history/ |
| History (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-cornwall/ |
| History and Ancient History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-ancient-history/ |
| History and Archaeology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-archaeology/ |
| History and Business | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-business-cornwall/ |
| History and Geography | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-geography-cornwall/ |
| History and International Relations | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-international-relations-cornwall/ |
| History and Politics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-politics-cornwall/ |
| History and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-modern-languages/ |
| Art History & Visual Culture and History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-history/ |
| English and History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-history/ |
| Philosophy and History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-and-history/ |

#### Law (11 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Law | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law/ |
| Law with Professional Placement | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-with-professional-placement/ |
| Law with European Study | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-with-european-study/ |
| English Law and French Law/Master 1 (Maitrise en Droit) | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-english-law-and-french-law/ |
| Law with Business (Cornwall) | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-with-business-cornwall/ |
| Law with Politics (Cornwall) | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-with-politics/ |
| Bachelor of Business and Laws (Cornwall) | BBL | https://www.exeter.ac.uk/undergraduate-degrees/bbl-bachelor-of-business-and-laws-cornwall/ |
| Graduate Law | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-graduate-law/ |
| Dual LLB / Juris Doctor (JD) with the Chinese University of Hong Kong | LLB | https://www.exeter.ac.uk/undergraduate-degrees/dual-llb-juris-doctor-with-cuhk/ |
| Law (for Brickfields Asia College only) | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-brickfields/ |
| Politics and Law (Cornwall) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-politics-and-law/ |

#### Liberal Arts (1 course)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Liberal Arts | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-liberal-arts/ |

#### Marine Studies (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Marine Biology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-marine-biology/ |
| Marine Biology | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-marine-biology/ |
| Oceanography | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-oceanography/ |

#### Mathematics (11 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Mathematics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-mathematics/ |
| Mathematics | MMath | https://www.exeter.ac.uk/undergraduate-degrees/mmath-mathematics/ |
| Mathematics with Foundation Year | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-mathematics-with-foundation-year/ |
| Mathematics and Data Science | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-mathematics-and-data-science/ |
| Mathematics and Data Science | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-mathematics-and-data-science/ |
| Mathematics with Economics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-mathematics-with-economics/ |
| Mathematics with Economics | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-mathematics-with-economics/ |
| Mathematics with Finance | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-mathematics-with-finance/ |
| Mathematics with Finance | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-mathematics-with-finance/ |
| Computer Science and Mathematics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-computer-science-and-mathematics/ |
| Computer Science and Mathematics | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-computer-science-and-mathematics/ |

#### Media and Communications (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Media and Communications | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-media-and-communications/ |
| Media & Communications and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-media-and-communications-and-modern-languages/ |
| English and Media & Communications | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-media-and-communications/ |
| Film & Television Studies and Media & Communications | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-film-and-television-studies-and-media-and-communications/ |

#### Medicine and Radiography (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Medicine | BMBS | https://www.exeter.ac.uk/undergraduate-degrees/bmbs-medicine/ |
| Medical Imaging (Diagnostic Radiography) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-medical-imaging-radiography/ |

#### Mining Engineering (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Mining Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-mining-engineering/ |
| Mining Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-mining-engineering/ |
| Mining Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-mining-engineering-with-foundation-year/ |
| Mining Engineering (Part-time) | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-mining-engineering-part-time/ |

#### Modern Languages and Cultures (14 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-modern-languages/ |
| Modern Languages and Arabic | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-modern-languages-and-arabic/ |
| Modern Languages and Latin | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-modern-languages-and-latin/ |
| Art History & Visual Culture and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-art-history-and-visual-culture-and-modern-languages/ |
| Classical Studies and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-modern-languages/ |
| English and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-english-and-modern-languages/ |
| Film & Television Studies and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-film-and-television-studies-and-modern-languages/ |
| History and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-modern-languages/ |
| International Business and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-international-business-and-modern-languages/ |
| International Relations and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-international-relations-and-modern-languages/ |
| Media & Communications and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-media-and-communications-and-modern-languages/ |
| Philosophy and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-and-modern-languages/ |
| Politics and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-and-modern-languages/ |
| Sociology and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology-and-modern-languages/ |

#### Natural Sciences (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Natural Sciences | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-natural-sciences/ |
| Natural Sciences | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-natural-sciences/ |
| Natural Sciences with Foundation Year | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-natural-sciences-with-foundation-year/ |

#### Neuroscience (1 course)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Neuroscience | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-neuroscience/ |

#### Nursing (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Adult Nursing | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-adult-nursing/ |
| Nursing | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-nursing/ |

#### Philosophy (9 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Philosophy | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy/ |
| Philosophy and History | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-and-history/ |
| Philosophy and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-and-modern-languages/ |
| Philosophy and Politics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-and-politics/ |
| Philosophy and Sociology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-and-sociology/ |
| Philosophy, Religion and Ethics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-religion-and-ethics/ |
| Classical Studies and Philosophy | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-philosophy/ |
| Politics, Philosophy and Economics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-philosophy-and-economics/ |
| Religion, Culture and Society | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-religion-culture-and-society/ |

#### Physics and Astronomy (11 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Physics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-physics/ |
| Physics | MPhys | https://www.exeter.ac.uk/undergraduate-degrees/mphys-physics/ |
| Physics with Foundation Year | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-physics-with-foundation-year/ |
| Physics with Astrophysics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-physics-with-astrophysics/ |
| Physics with Astrophysics | MPhys | https://www.exeter.ac.uk/undergraduate-degrees/mphys-physics-with-astrophysics/ |
| Physics with Biophysics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-physics-with-biophysics/ |
| Physics with Biophysics | MPhys | https://www.exeter.ac.uk/undergraduate-degrees/mphys-physics-with-biophysics/ |
| Physics with Quantum Technology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-physics-with-quantum-technology/ |
| Physics with Quantum Technology | MPhys | https://www.exeter.ac.uk/undergraduate-degrees/mphys-physics-with-quantum-technology/ |
| Theoretical Physics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-theoretical-physics/ |
| Theoretical Physics | MPhys | https://www.exeter.ac.uk/undergraduate-degrees/mphys-theoretical-physics/ |

#### Politics and International Relations (17 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Politics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics/ |
| Global Politics (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-global-politics-cornwall/ |
| International Relations | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-international-relations/ |
| International Relations and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-international-relations-and-modern-languages/ |
| Politics and Business (Cornwall) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-politics-and-business-cornwall/ |
| Politics and International Relations | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-politics-and-international-relations/ |
| Politics and International Relations (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-and-international-relations-cornwall/ |
| Politics and Geography (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-and-geography-cornwall/ |
| Politics and Law (Cornwall) | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-politics-and-law/ |
| Politics and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-and-modern-languages/ |
| Politics and Sociology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-and-sociology/ |
| Politics, Philosophy and Economics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-politics-philosophy-and-economics/ |
| Arabic and Politics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-arabic-and-politics/ |
| Economics and Politics | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-economics-and-politics/ |
| History and International Relations (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-international-relations-cornwall/ |
| History and Politics (Cornwall) | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-history-and-politics-cornwall/ |
| Law with Politics (Cornwall) | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-law-with-politics/ |

#### Psychology (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Applied Psychology (Clinical) | MSci | https://www.exeter.ac.uk/undergraduate-degrees/msci-applied-psychology/ |
| Psychology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-psychology/ |

#### Renewable Energy (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Renewable Energy Engineering | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-renewable-energy-engineering/ |
| Renewable Energy Engineering | MEng | https://www.exeter.ac.uk/undergraduate-degrees/meng-renewable-energy-engineering/ |
| Renewable Energy Engineering with Foundation Year | BEng | https://www.exeter.ac.uk/undergraduate-degrees/beng-renewable-energy-engineering-with-foundation-year/ |

#### Sociology (5 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Sociology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology/ |
| Sociology | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-sociology/ |
| Sociology and Anthropology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology-and-anthropology/ |
| Sociology and Criminology | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology-and-criminology/ |
| Sociology and Modern Languages | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-sociology-and-modern-languages/ |

#### Sport and Health Sciences (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Exercise and Sport Sciences | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-exercise-and-sport-sciences/ |
| Sport Business Management | BSc | https://www.exeter.ac.uk/undergraduate-degrees/bsc-sport-business-management/ |

#### Theology and Religion (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Theology and Religion | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-theology-and-religion/ |
| Religion, Culture and Society | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-religion-culture-and-society/ |
| Classical Studies and Religion | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-classical-studies-and-religion/ |
| Philosophy, Religion and Ethics | BA | https://www.exeter.ac.uk/undergraduate-degrees/ba-philosophy-religion-and-ethics/ |

#### International Study Centre (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Exeter International Foundation | Foundation | https://www.exeter.ac.uk/study/international-study-centre/foundation/ |
| International Year One | Year One | https://www.exeter.ac.uk/study/international-study-centre/year-one/ |

---

## SECTION 2 — Graduate education

### 2.1 授课型硕士 (PGT) 课程列表

#### Accounting and Finance (8 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Accounting and Finance | MSc | https://www.exeter.ac.uk/masters-degrees/msc-accounting-and-finance/ |
| Finance | MSc | https://www.exeter.ac.uk/masters-degrees/msc-finance/ |
| Finance and Investment | MSc | https://www.exeter.ac.uk/masters-degrees/msc-finance-and-investment/ |
| Finance and Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-finance-and-data-science/ |
| Finance and Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-finance-and-management/ |
| Finance (Pathway to PhD) | MRes | https://www.exeter.ac.uk/masters-degrees/mres-finance/ |
| Financial Technology (Fintech) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-financial-technology-fintech/ |
| Sustainable Finance and Climate Change | MSc | https://www.exeter.ac.uk/masters-degrees/msc-sustainable-finance-and-climate-change/ |

#### Anthropology (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Anthrozoology | MA | https://www.exeter.ac.uk/masters-degrees/ma-anthrozoology/ |
| Food Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-food-studies/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |

#### Arab and Islamic Studies (7 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Islamic Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-islamic-studies/ |
| Kurdish Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-kurdish-studies/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |
| Middle East Politics | MA | https://www.exeter.ac.uk/masters-degrees/ma-middle-east-politics/ |
| Middle East Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-middle-east-studies/ |
| Middle East Studies (Social Studies) | MRes | https://www.exeter.ac.uk/masters-degrees/mres-middle-east-studies/ |
| Palestine Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-palestine-studies/ |

#### Archaeology (6 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Archaeology | MA | https://www.exeter.ac.uk/masters-degrees/ma-archaeology/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |
| Bioarchaeology: Zooarchaeology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-bioarchaeology-zooarchaeology/ |
| Bioarchaeology: Forensic Anthropology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-bioarchaeology-forensic-anthropology/ |
| Bioarchaeology: Human Osteology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-bioarchaeology-human-osteology/ |
| Forensic Investigations | MSc | https://www.exeter.ac.uk/masters-degrees/msc-forensic-investigations/ |

#### Biosciences (10 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Advanced Biological Sciences | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-biological-sciences/ |
| Advanced Biological Sciences | MRes | https://www.exeter.ac.uk/masters-degrees/mres-advanced-biological-sciences/ |
| Advanced Biological Sciences and Business | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-biological-sciences-and-business/ |
| Conservation and Biodiversity | MSc | https://www.exeter.ac.uk/masters-degrees/msc-conservation-and-biodiversity/ |
| Evolution, Behaviour and Ecology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-evolution-behaviour-and-ecology/ |
| Immunology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-immunology/ |
| Island Biodiversity and Conservation | MSc | https://www.exeter.ac.uk/masters-degrees/msc-island-biodiversity-and-conservation/ |
| Marine Environmental Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-marine-environmental-management/ |
| Marine Vertebrate Ecology and Conservation | MSc | https://www.exeter.ac.uk/masters-degrees/msc-marine-vertebrate-ecology-and-conservation/ |
| Medical Mycology (online) | MSc | https://www.exeter.ac.uk/online-courses/medical-mycology/ |

#### Business and Management (21 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Business Analytics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-business-analytics/ |
| Business and Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-business-and-management/ |
| Digital Marketing | MSc | https://www.exeter.ac.uk/masters-degrees/msc-digital-marketing/ |
| Global Healthcare Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-global-healthcare-management/ |
| Human Resource Management | MSc/PgDip | https://www.exeter.ac.uk/masters-degrees/msc-human-resource-management/ |
| Innovation and Entrepreneurship | MSc | https://www.exeter.ac.uk/masters-degrees/msc-innovation-and-entrepreneurship/ |
| Intercultural Communication and International Business | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-international-business/ |
| International Business (Online) | MSc | https://www.exeter.ac.uk/online-courses/msc-international-business/ |
| International Business | MSc | https://www.exeter.ac.uk/masters-degrees/msc-international-business/ |
| International Business and Strategy | MSc | https://www.exeter.ac.uk/masters-degrees/msc-international-business-and-strategy/ |
| Management (Pathway to PhD) | MRes | https://www.exeter.ac.uk/masters-degrees/mres-management/ |
| Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-management/ |
| Marketing and Business Analytics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-marketing-and-business-analytics/ |
| Marketing | MSc | https://www.exeter.ac.uk/masters-degrees/msc-marketing/ |
| Marketing Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-marketing-management/ |
| Law and Business | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-business/ |
| Law and Business: Finance and Accounting | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-business-finance-and-accounting/ |
| Law and Business: Management | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-business-management/ |
| Social Media and Digital Marketing | MA | https://www.exeter.ac.uk/masters-degrees/ma-social-media-and-digital-marketing/ |
| Sports Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-sports-management/ |
| One Planet MBA | MBA | https://www.exeter.ac.uk/masters-degrees/one-planet-mba/ |

#### Classics and Ancient History (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Classics and Ancient History | MA | https://www.exeter.ac.uk/masters-degrees/ma-classics-and-ancient-history/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |

#### Climate Change (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Global Sustainability Solutions | MSc | https://www.exeter.ac.uk/masters-degrees/msc-global-sustainability-solutions/ |
| Weather and Climate Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-weather-and-climate-science/ |

#### Computer Science (11 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Advanced Computer Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-computer-science/ |
| Advanced Computer Science with Business | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-computer-science-with-business/ |
| Advanced Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-data-science/ |
| Advanced Machine Learning | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-machine-learning/ |
| Artificial Intelligence | MSc | https://www.exeter.ac.uk/masters-degrees/msc-artificial-intelligence/ |
| Artificial Intelligence for the Environment | MSc | https://www.exeter.ac.uk/masters-degrees/msc-artificial-intelligence-for-the-environment/ |
| Computer Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-computer-science/ |
| Cyber Security Analytics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-cyber-security-analytics/ |
| Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-data-science/ |
| Generative Artificial Intelligence | MSc | https://www.exeter.ac.uk/masters-degrees/msc-generative-artificial-intelligence/ |
| Human Centred Artificial Intelligence | MSc | https://www.exeter.ac.uk/masters-degrees/msc-human-centred-artificial-intelligence/ |

#### Creative Industries: Art, Drama, and Film (7 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Creative Industries | MA | https://www.exeter.ac.uk/masters-degrees/ma-creative-industries/ |
| Curation: Contemporary Art and Cultural Management | MA | https://www.exeter.ac.uk/masters-degrees/ma-curation-contemporary-art-and-cultural-management/ |
| Film and Screen Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-film-and-screen-studies/ |
| Interactive Storytelling Design: Video Games and Beyond | MA | https://www.exeter.ac.uk/masters-degrees/ma-interactive-storytelling-design-video-games/ |
| International Film Business | MA | https://www.exeter.ac.uk/masters-degrees/ma-international-film-business/ |
| Theatre Practice | MA | https://www.exeter.ac.uk/masters-degrees/ma-theatre-practice/ |
| Theatre Practice | MFA | https://www.exeter.ac.uk/masters-degrees/mfa-theatre-practice/ |

#### Data Science and Analytics (13 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Advanced Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-data-science/ |
| Applied Data Science and Statistics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-applied-data-science-and-statistics/ |
| Artificial Intelligence for the Environment | MSc | https://www.exeter.ac.uk/masters-degrees/msc-artificial-intelligence-for-the-environment/ |
| Business Analytics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-business-analytics/ |
| Cyber Security Analytics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-cyber-security-analytics/ |
| Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-data-science/ |
| Finance and Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-finance-and-data-science/ |
| Generative Artificial Intelligence | MSc | https://www.exeter.ac.uk/masters-degrees/msc-generative-artificial-intelligence/ |
| Health Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-health-data-science/ |
| Human Centred Artificial Intelligence | MSc | https://www.exeter.ac.uk/masters-degrees/msc-human-centred-artificial-intelligence/ |
| Security and Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-security-and-data-science/ |
| Social Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-social-data-science/ |
| Statistics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-statistics/ |

#### Economics (7 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Economics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-economics/ |
| Economics (Behavioural Insights) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-economics-behavioural-insights/ |
| Economics (Environmental Policy) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-economics-environmental-policy/ |
| Economics (International Development) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-economics-international-development/ |
| Economics (Pathway to PhD) | MRes | https://www.exeter.ac.uk/masters-degrees/mres-economics/ |
| Financial Economics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-financial-economics/ |
| Financial Technology (Fintech) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-financial-technology-fintech/ |

#### Education and Teacher Training (11 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Creative Arts in Education | MA | https://www.exeter.ac.uk/masters-degrees/ma-creative-arts-in-education/ |
| Educational Child and Community Psychology | DEdPsych | https://www.exeter.ac.uk/subjects/education/dedpsych-educational-child-and-community-psychology/ |
| Education | MA | https://www.exeter.ac.uk/masters-degrees/ma-education/ |
| Education (online) | MA | https://www.exeter.ac.uk/online-courses/ma-education/ |
| Education Leadership and Management | MA | https://www.exeter.ac.uk/masters-degrees/ma-education-leadership-and-management/ |
| Intercultural Communication and Education | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-education/ |
| International Education | MA | https://www.exeter.ac.uk/masters-degrees/ma-international-education/ |
| Special Educational Needs | MA | https://www.exeter.ac.uk/masters-degrees/ma-special-educational-needs/ |
| Teaching English to Speakers of Other Languages (TESOL) | MEd | https://www.exeter.ac.uk/masters-degrees/med-tesol/ |
| Technology and Education Futures | MA | https://www.exeter.ac.uk/masters-degrees/ma-technology-and-education-futures/ |
| PGCE Teacher Training Courses | PGCE | https://www.exeter.ac.uk/teacher-training/ |

#### Engineering (9 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Biomedical Engineering | MSc | https://www.exeter.ac.uk/masters-degrees/msc-biomedical-engineering/ |
| Civil Engineering | MSc | https://www.exeter.ac.uk/subjects/engineering/civil-engineering/ |
| Electrical Power and Smart Grids | MSc | https://www.exeter.ac.uk/masters-degrees/msc-electrical-power-and-smart-grids/ |
| Engineering Business Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-engineering-business-management/ |
| International Supply Chain Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-international-supply-chain-management/ |
| Mechanical Engineering | MSc | https://www.exeter.ac.uk/masters-degrees/msc-mechanical-engineering/ |
| Renewable Energy Engineering | MSc | https://www.exeter.ac.uk/masters-degrees/msc-renewable-energy-engineering/ |
| Electronic Information (at ZJUT, China) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-electronic-information-zjut-china/ |
| Energy and Power Engineering (at ZJUT, China) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-energy-and-power-engineering-zjut-china/ |

#### English (5 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Creative Writing | MA | https://www.exeter.ac.uk/masters-degrees/ma-creative-writing/ |
| Creative Writing (Online) | MA | https://www.exeter.ac.uk/online-courses/ma-creative-writing/ |
| English Literary Studies | MA | https://www.exeter.ac.uk/masters-degrees/ma-english-literary-studies/ |
| Interactive Storytelling Design: Video Games and Beyond | MA | https://www.exeter.ac.uk/masters-degrees/ma-interactive-storytelling-design-video-games/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |

#### Law (15 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Graduate Law | LLB | https://www.exeter.ac.uk/undergraduate-degrees/llb-graduate-law/ |
| Master of Laws | LLM | https://www.exeter.ac.uk/masters-degrees/llm-master-of-laws/ |
| Commercial Law | LLM | https://www.exeter.ac.uk/masters-degrees/llm-commercial-law/ |
| International Law | LLM | https://www.exeter.ac.uk/masters-degrees/llm-international-law/ |
| International Commercial Law | LLM | https://www.exeter.ac.uk/masters-degrees/llm-international-commercial-law/ |
| Law and Business | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-business/ |
| Law and Business: Finance and Accounting | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-business-finance-and-accounting/ |
| Law and Business: Management | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-business-management/ |
| Law and Technology | LLM | https://www.exeter.ac.uk/masters-degrees/llm-law-and-technology/ |
| Dual Masters in Intellectual Property Law | LLM | https://www.exeter.ac.uk/masters-degrees/erasmus-intellectual-property-and-data-law/ |
| The University of Law at Exeter | Various | https://www.exeter.ac.uk/subjects/law/university-of-law/ |
| Companies, Competition and Digital Markets | LLM | https://www.exeter.ac.uk/masters-degrees/llm-companies-competition-and-digital-markets/ |
| Intellectual Property and Technology | LLM | https://www.exeter.ac.uk/masters-degrees/llm-intellectual-property-and-technology/ |
| International Human Rights | LLM | https://www.exeter.ac.uk/masters-degrees/llm-international-human-rights/ |
| Social Science Research | MRes | https://www.exeter.ac.uk/masters-degrees/mres-social-science-research/ |

#### Healthcare and Medicine (20 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Advanced Practice | MSc | https://www.exeter.ac.uk/masters-degrees/msc-advanced-clinical-practice/ |
| Clinical Education | MSc | https://www.exeter.ac.uk/masters-degrees/msc-clinical-education/ |
| Extreme Medicine (Distance) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-extreme-medicine-distance/ |
| Genomic Medicine | MSc | https://www.exeter.ac.uk/masters-degrees/msc-genomic-medicine/ |
| Genomic Medicine (online) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-genomic-medicine-online/ |
| Genomic Medicine (Data Science) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-genomic-medicine-data-science/ |
| Global Healthcare Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-global-healthcare-management/ |
| Health Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-health-data-science/ |
| Health Data Science (Online) | MSc | https://www.exeter.ac.uk/online-courses/msc-health-data-science/ |
| Health Research Methods | MSc | https://www.exeter.ac.uk/masters-degrees/msc-health-research-methods/ |
| Immunology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-immunology/ |
| Leading Clinical Research Delivery (Online) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-leading-clinical-research-delivery-online/ |
| Public Health (MPH) | MPH | https://www.exeter.ac.uk/masters-degrees/mph-master-of-public-health/ |
| Medical Imaging | MSc | https://www.exeter.ac.uk/masters-degrees/msc-medical-imaging/ |
| Neuroscience | MSc | https://www.exeter.ac.uk/masters-degrees/msc-neuroscience/ |
| Neuroscience (Data Science) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-neuroscience-data-science/ |
| Independent and Supplementary Prescribing | Practice Cert | https://www.exeter.ac.uk/masters-degrees/independent-prescribing-course/ |
| MRI: Integrated Theory and Practice | MRI cert | https://www.exeter.ac.uk/masters-degrees/mri-integrated-theory-and-practice-course/ |
| Principles of Advanced Clinical Practice | Certificate | https://www.exeter.ac.uk/masters-degrees/principles-of-advanced-clinical-practice-course/ |
| Principles of Supervision, Mentoring and Coaching | Certificate | https://www.exeter.ac.uk/masters-degrees/principles-of-supervision-mentoring-and-coaching-course/ |

#### History (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| History | MA | https://www.exeter.ac.uk/masters-degrees/ma-history/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |

#### Mathematics (7 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Applied Data Science and Statistics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-applied-data-science-and-statistics/ |
| Biomedical Data and Artificial Intelligence | MSc | https://www.exeter.ac.uk/masters-degrees/msc-biomedical-data-and-artificial-intelligence/ |
| Finance and Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-finance-and-data-science/ |
| Mathematical Finance | MSc | https://www.exeter.ac.uk/masters-degrees/msc-mathematical-finance/ |
| Mathematics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-mathematics/ |
| Statistics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-statistics/ |
| Weather and Climate Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-weather-and-climate-science/ |

#### Media and Communications (7 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Media and Communications | MA | https://www.exeter.ac.uk/masters-degrees/ma-media-and-communications/ |
| Media and Public Relations | MA | https://www.exeter.ac.uk/masters-degrees/ma-media-and-public-relations/ |
| Intercultural Communication and International Business | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-international-business/ |
| Intercultural Communication and Education | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-education/ |
| Intercultural Communication and Migration | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-migration/ |
| Intercultural Communication and Public Administration | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-public-administration/ |
| Social Media and Digital Marketing | MA | https://www.exeter.ac.uk/masters-degrees/ma-social-media-and-digital-marketing/ |

#### Mining Engineering (4 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Exploration and Mining Geology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-exploration-and-mining-geology/ |
| Minerals Processing | MSc | https://www.exeter.ac.uk/masters-degrees/msc-minerals-processing/ |
| Mining Engineering | MSc | https://www.exeter.ac.uk/masters-degrees/msc-mining-engineering/ |
| Mining Environmental Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-mining-environmental-management/ |

#### Philosophy, Theology, and Religion (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Philosophy | MA | https://www.exeter.ac.uk/masters-degrees/ma-philosophy/ |
| Theology and Religion | MA | https://www.exeter.ac.uk/masters-degrees/ma-theology-and-religion/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |

#### Physics and Astronomy (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Physics | MSc | https://www.exeter.ac.uk/masters-degrees/msc-physics/ |
| Metamaterials | MSc | https://www.exeter.ac.uk/masters-degrees/msc-metamaterials/ |

#### Politics and International Relations (13 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Applied Security and Strategy (MStrat) | MA | https://www.exeter.ac.uk/masters-degrees/ma-applied-security-and-strategy/ |
| Conflict, Security and Development | MA | https://www.exeter.ac.uk/masters-degrees/ma-conflict-security-and-development/ |
| Diplomacy and Foreign Policy | MA | https://www.exeter.ac.uk/masters-degrees/ma-diplomacy-and-foreign-policy/ |
| Intercultural Communication and Migration | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-migration/ |
| Intercultural Communication and Public Administration | MA | https://www.exeter.ac.uk/masters-degrees/ma-intercultural-communication-and-public-administration/ |
| International Development | MA | https://www.exeter.ac.uk/masters-degrees/ma-international-development/ |
| International Relations | MA | https://www.exeter.ac.uk/masters-degrees/ma-international-relations/ |
| Master of Public Administration | MPA | https://www.exeter.ac.uk/masters-degrees/mpa-master-of-public-administration/ |
| Public Policy and Public Administration | MSc | https://www.exeter.ac.uk/masters-degrees/msc-public-policy/ |
| Security and Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-security-and-data-science/ |
| Social and Political Theory | MA | https://www.exeter.ac.uk/masters-degrees/ma-social-and-political-theory/ |
| Social Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-social-data-science/ |
| Social Science Research | MRes | https://www.exeter.ac.uk/masters-degrees/mres-social-science-research/ |

#### Psychology (8 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Psychology (Conversion) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-psychology-conversion/ |
| Psychology (Conversion) (Online) | MSc | https://www.exeter.ac.uk/online-courses/msc-psychology-conversion/ |
| Psychology (Conversion) (Sport) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-psychology-conversion-sport/ |
| Psychological Therapies Practice and Research (Systemic Therapy) | MSc | https://www.exeter.ac.uk/masters-degrees/msc-psychological-therapies-practice-and-research-systemic-therapy/ |
| Clinical Psychology | MSc | https://www.exeter.ac.uk/masters-degrees/msc-clinical-psychology/ |
| Psychedelics: Mind, Medicine, and Culture | MSc | https://www.exeter.ac.uk/masters-degrees/msc-psychedelics-mind-medicine-and-culture/ |
| Psychedelics: Mind, Medicine, and Culture (Online) | MSc | https://www.exeter.ac.uk/online-courses/msc-psychedelics/ |
| Psychedelics: Mind, Medicine, and Culture (Online) | PGCert | https://www.exeter.ac.uk/online-courses/pgcert-psychedelics/ |

#### Sociology (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Sociology | MA | https://www.exeter.ac.uk/masters-degrees/ma-sociology/ |
| Social Data Science | MSc | https://www.exeter.ac.uk/masters-degrees/msc-social-data-science/ |
| Magic and Occult Science | MA | https://www.exeter.ac.uk/masters-degrees/ma-magic-and-occult-science/ |

#### Sport and Health Sciences (2 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Sport and Exercise Medicine | MSc | https://www.exeter.ac.uk/masters-degrees/msc-sport-and-exercise-medicine/ |
| Sports Management | MSc | https://www.exeter.ac.uk/masters-degrees/msc-sports-management/ |

#### International Study Centre (3 courses)
| 课程名称 | 学位 | URL |
|---------|------|-----|
| Exeter International Pre-Masters Programme | Pre-Masters | https://www.exeter.ac.uk/study/international-study-centre/pre-masters-progression/ |
| Pre-sessional English | Pre-sessional | https://www.exeter.ac.uk/study/international-study-centre/pre-sessional-english/ |
| INTO Postgraduate Degree with One Term Pre-Master's for Business | Pre-Masters | https://www.exeter.ac.uk/study/international-study-centre/pre-masters-progression/ |

### 2.2 研究型博士 (PGR) 课程列表

| 研究领域 | URL |
|---------|-----|
| Accountancy | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Arab and Islamic Studies | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Archaeology | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Art History and Visual Culture | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Biological Sciences | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Business and Management | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Classics and Ancient History | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Climate Change and Environment | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Clinical and Biomedical Sciences | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Complex Living Systems | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Computer Science | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Drama | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Economics | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Education | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Engineering | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| English | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Film Studies | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Finance | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Food, Nutrition and Health | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Genetics and Genomics | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Geography | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Geology | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Healthcare and Medicine | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| History | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Law | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Magic and Occult Science | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Mathematics | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Media and Communications | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Medical Imaging | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Mining and Minerals Engineering | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Modern Languages | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Neuroscience | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Nursing Science | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Physics | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Politics and International Relations | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Psychology | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Public Health | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Renewable Energy | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Sociology, Philosophy and Anthropology | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Sport and Health Sciences | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Strategy and Security | https://www.exeter.ac.uk/study/pg-research/degrees/ |
| Theology and Religion | https://www.exeter.ac.uk/study/pg-research/degrees/ |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 本科申请要求

| 维度 | 要求 |
|------|------|
| 申请系统 | UCAS |
| UCAS 代码 | E84 EXETR |
| 标准 UCAS 截止日期 | 2027年1月29日 |
| 医学 UCAS 截止日期 | 2026年10月15日 |
| A-Level 典型要求 | 因课程而异，详见各课程页面 |
| IB 要求 | 因课程而异，详见各课程页面 |
| 英语语言要求 | 见 3.3 节 |
| 上下文优惠 | 见 3.4 节 |

### 3.2 研究生申请要求

| 维度 | 要求 |
|------|------|
| 申请系统 | 在线直接申请 |
| 录取模式 | 分散式（各学院自行审核） |
| 滚动录取 | Yes |
| 申请费 | 无 |
| 学位要求 | 因课程而异，通常要求 2:1 或以上 |

### 3.3 英语语言要求

Exeter 使用 8 个语言要求等级（Profile A 至 G）：

| Profile | IELTS 总分 | IELTS 单项最低 | TOEFL iBT 总分 | TOEFL 单项最低 |
|---------|-----------|---------------|---------------|---------------|
| A | 6.0 | 6.0 | 87 | 21 |
| B1 | 6.5 | 5.5 | 90 | Speaking 20, Other 18 |
| B2 | 6.5 | 6.0 | 90 | 21 |
| C | 6.5 | 6.5 | 90 | 25 |
| D | 7.0 | 6.0 | 100 | 21 |
| E | 7.0 | Writing 6.5, Other 6.0 | 100 | Writing 25, Other 21 |
| F | 7.0 | 6.5 | 100 | 25 |
| G | 7.5 | Speaking/Listening 7.0, Other 6.0 | 110 | Speaking/Listening 25, Other 21 |

**TOEFL 新评分标准**: 2026年1月21日起的 TOEFL iBT 使用新评分标准（总分 6 分制），各 Profile 的最低要求相应调整。

**豁免条件**:
- 英语为母语国家的公民（美国、澳大利亚、加拿大、爱尔兰、牙买加、新西兰、英国等）
- 7 年内在以英语授课的机构完成学位
- 2+2 或 3+1 项目中最后阶段在英语国家完成
- 提供教学媒介证明（Medium of Instruction letter）加上认可的高中英语资格

### 3.4 上下文优惠 (Contextual Offers)

| 优惠类型 | 降分幅度 | 适用条件 |
|---------|---------|---------|
| 标准上下文优惠 | 降低 2 个等级 | POLAR4 低参与地区、IMD 贫困地区、指定学校、免费校餐、Elephant Group/IntoUniversity/Bridges to HE 合作机构、SEREN 合作项目、护理人员/独立学生、Exeter 进阶项目 |
| 扩大上下文优惠 | 降低 3 个等级 | 护理经验学生、寻求庇护者/难民、Exeter Scholars/Realising Opportunities/Sutton Trust 项目 |

**注意**: 上下文优惠不适用于 GCSE 要求，且竞争性录取不保证获得 offer。

---

## SECTION 4 — Costs & financial aid

### 4.1 国际学生本科学费 (2026-27 学年)

| 课程类别 | 年学费 (GBP) |
|---------|-------------|
| BMBS 医学 | £48,900 |
| 计算机科学、工程、物理、地质、采矿、生物科学、心理学等 | £31,200 |
| 数学与统计 | £30,100 |
| 体育与健康科学 | £29,900 |
| 灵活联合荣誉 | £25,750 |
| 人文、艺术、社会科学（含法学） | £24,950 |
| 会计、金融、商业与管理、经济学、市场营销 | £24,900 |

### 4.2 英国本土学生学费

| 类别 | 年学费 (GBP) |
|------|-------------|
| 本科 (Home) | £9,250 |

### 4.3 学费增长政策

- 大学政策是在学习期间每年增加学费
- 多年制课程的学费预计将根据每年 3 月的消费者价格指数适度增长

### 4.4 奖学金与资助

- 提供基于家庭收入的助学金（£16,000-£35,000 区间）
- 国际学生奖学金计划详见 https://www.exeter.ac.uk/study/funding/undergraduate/

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Exeter"
  source_url: https://www.exeter.ac.uk
  source_snippet: "University of Exeter"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.russell_group
  value: true
  source_url: https://www.exeter.ac.uk/study/undergraduate/
  source_snippet: "Russell Group university"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.tef_rating
  value: "Gold"
  source_url: https://www.exeter.ac.uk/study/undergraduate/
  source_snippet: "TEF Gold"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: ug.total_programs
  value: 252
  source_url: https://www.exeter.ac.uk/study/undergraduate/
  source_snippet: "252 course listings across 44 subject areas"
  capture_date: 2026-07-08
  evidence_type: course_listing_page

E-U-005:
  field: pg_taught.total_programs
  value: 216
  source_url: https://www.exeter.ac.uk/masters-degrees/
  source_snippet: "216 course entries across 35 subject areas"
  capture_date: 2026-07-08
  evidence_type: course_listing_page

E-U-006:
  field: pg_research.total_areas
  value: 42
  source_url: https://www.exeter.ac.uk/study/pg-research/degrees/
  source_snippet: "42 research topic areas"
  capture_date: 2026-07-08
  evidence_type: course_listing_page

E-U-007:
  field: hierarchy.faculties
  value: 3
  source_url: https://www.exeter.ac.uk/departments/
  source_snippet: "Faculty of Environment, Science and Economy; Faculty of Humanities, Arts and Social Sciences; Faculty of Health and Life Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: costs.ug_international_arts
  value: "£24,950"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/fees/
  source_snippet: "Arts, Humanities, Social Sciences (including Law) £24,950"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: costs.ug_international_business
  value: "£24,900"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/fees/
  source_snippet: "Accounting, Finance, Business & Management, Economics and Marketing £24,900"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: costs.ug_international_science
  value: "£31,200"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/fees/
  source_snippet: "Computer Science, Engineering, Physics... £31,200"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: costs.ug_international_medicine
  value: "£48,900"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/fees/
  source_snippet: "BMBS Medicine £48,900"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: costs.ug_home
  value: "£9,250"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/fees/
  source_snippet: "Home (UK) £9,250"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: language.profile_a.ielts
  value: "6.0 overall, 6.0 minimum"
  source_url: https://www.exeter.ac.uk/study/englishlanguagerequirements/profile-a/
  source_snippet: "6.0 overall and no less than 6.0 in any section"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: language.profile_d.ielts
  value: "7.0 overall, 6.0 minimum"
  source_url: https://www.exeter.ac.uk/study/englishlanguagerequirements/profile-d/
  source_snippet: "7.0 overall and no less than 6.0 in any section"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: language.profile_g.ielts
  value: "7.5 overall, Speaking/Listening 7.0"
  source_url: https://www.exeter.ac.uk/study/englishlanguagerequirements/profile-g/
  source_snippet: "7.5 overall, no less than 7.0 in speaking and listening"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: deadlines.ucas_standard
  value: "29 January 2027"
  source_url: https://www.exeter.ac.uk/study/undergraduate/
  source_snippet: "UCAS deadline for 2027 entry"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-017:
  field: deadlines.ucas_medicine
  value: "15 October 2026"
  source_url: https://www.exeter.ac.uk/study/undergraduate/
  source_snippet: "Medicine application deadline"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-018:
  field: contextual_offers.reduction_standard
  value: "2 grades"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/entry-requirements/contextual-offers/
  source_snippet: "Two-grade adjustment"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-019:
  field: contextual_offers.reduction_extended
  value: "3 grades"
  source_url: https://www.exeter.ac.uk/undergraduate-degrees/entry-requirements/contextual-offers/
  source_snippet: "Three-grade adjustment for care leavers"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-020:
  field: institution.campuses
  value: "Streatham, St Luke's, Penryn (Cornwall)"
  source_url: https://www.exeter.ac.uk/study/undergraduate/
  source_snippet: "Our campuses: Streatham, St Luke's, Penryn"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### 数据完整性状态

| 数据项 | 状态 | 完成度 |
|-------|------|--------|
| UG 课程列表 | 完成 | 100% |
| PGT 课程列表 | 完成 | 100% |
| PGR 研究领域 | 完成 | 100% |
| 学院/系所层级 | 完成 | 100% |
| 学位类型分布 | 完成 | 100% |
| 国际学生学费 | 完成 | 100% |
| 英语语言要求 | 完成 | 100% |
| 上下文优惠 | 完成 | 100% |
| A-Level/IB 具体要求 | 未完成 | 0% (需逐课程提取) |
| 奖学金详情 | 部分完成 | 30% |
| 生活费用 | 未完成 | 0% (页面 404) |

### 后续数据项 (按优先级)

| 优先级 | 数据项 |
|--------|-------|
| P1 | 每门课程的 A-Level/IB 具体入学要求 |
| P1 | 奖学金和资助详细信息 |
| P2 | 生活费用估算 |
| P2 | 课程模块详情和课程结构 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | University of Exeter | Bristol | Cardiff | Newcastle |
|------|---------------------|---------|---------|-----------|
| UG 课程总数 | 252 | 503 | 237 | 147 |
| PGT 课程总数 | 216 | 163 | ~150 | ~120 |
| PGR 研究领域 | 42 | 77 | ~40 | ~35 |
| 罗素集团 | Yes | Yes | Yes | Yes |
| TEF 评级 | Gold | Gold | Gold | Gold |
| 学院数 | 3 | 3 | 3 | 3 |
| 语言要求体系 | 8 Profiles (A-G) | 9 Profiles (A-H) | Band 系统 | Band 系统 |
| 国际 UG 学费范围 | £24,900-£48,900 | £25,500-£49,700 | £20,000-£35,000 | £20,000-£35,000 |
| 校区数 | 3 (Exeter + Cornwall) | 1 | 2 | 2 |
| 特色学科 | Mining Engineering, Camborne School of Mines | Veterinary, Dentistry | Journalism, Optometry | Marine Engineering, Urban Planning |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: University of Exeter official website (www.exeter.ac.uk)
> **Granularity**: faculty → department → degree-level → program
> **Completeness**: UG programmes 100% | PGT programmes 100% | PGR areas 100% | Fees 100% | Language reqs 100% | Evidence (20 blocks) 100%
> **Cache**: uni-cache/schools/exeter/ (site-memory.json, last-extract.json, content-hashes.json)
