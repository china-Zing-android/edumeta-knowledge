# University of St Andrews Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: Funnelback search API + ego-browser
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep, full extraction)
> **Region**: UK (Scotland)
> **Source URL**: https://www.st-andrews.ac.uk/subjects/

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 来源 |
|------|------|------|
| 本科专业 (UG, unique URLs) | **96** | Funnelback API |
| 研究生授课型 (PGT, unique URLs) | **(subset of 109 PG total)** | Funnelback API |
| 研究生研究型 (PGR, individual pages) | not in search index | School research-degree pages |
| **总项目数 (UG + PG, unique URLs)** | **205** | Funnelback search API |
| Funnelback 报告的 UG 原始结果数 | 152 | Funnelback search API count_match |

**Counting notes:**

- **UG (96 unique URLs from 152 raw results)**: Funnelback returns programme variants (e.g. single + joint honours share the same course page for many subjects). Dedup by URL yields 96 unique course pages.
- **PG (109 unique URLs)**: Each PG programme has a distinct course page (MSc, MLitt, MRes, PGDip, PGCert, DProf).
- **PGR (PhD/MPhil/EngD/MD)**: Available across all schools via individual school research-degree pages; not listed in the course search index.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

St Andrews has **4 Faculties** (Arts, Science, Social Sciences, Divinity) + a separate **School of Medicine** and an **Interdisciplinary Graduate School**.

```
University of St Andrews
├── Faculty of Arts (25 subjects, 69 programmes)
│   ├── International Education & Lifelong Learning Institute — 3 subjects, 15 programmes
│   ├── International Education and Lifelong Learning Institute (IELLI) — 1 subjects, 1 programmes
│   ├── School of Art History — 1 subjects, 4 programmes
│   ├── School of Classics — 4 subjects, 8 programmes
│   ├── School of English — 1 subjects, 5 programmes
│   ├── School of History — 3 subjects, 17 programmes
│   ├── School of Modern Languages — 10 subjects, 12 programmes
│   ├── School of Philosophical, Anthropological and Film Studies — 2 subjects, 7 programmes
├── Faculty of Divinity (2 subjects, 15 programmes)
│   ├── Music Centre — 1 subjects, 1 programmes
│   ├── School of Divinity — 1 subjects, 14 programmes
├── Faculty of Science (15 subjects, 75 programmes)
│   ├── (no school) — 1 subjects, 1 programmes
│   ├── Graduate School — 1 subjects, 1 programmes
│   ├── School of Biology — 2 subjects, 16 programmes
│   ├── School of Chemistry — 1 subjects, 8 programmes
│   ├── School of Computer Science — 2 subjects, 12 programmes
│   ├── School of Earth and Environmental Sciences — 1 subjects, 5 programmes
│   ├── School of Geography and Sustainable Development — 2 subjects, 5 programmes
│   ├── School of Mathematics and Statistics — 2 subjects, 13 programmes
│   ├── School of Physics and Astronomy — 1 subjects, 6 programmes
│   ├── School of Psychology and Neuroscience — 2 subjects, 8 programmes
├── Faculty of Social Sciences (6 subjects, 34 programmes)
│   ├── (no school) — 1 subjects, 3 programmes
│   ├── Business School — 3 subjects, 18 programmes
│   ├── School of International Relations — 1 subjects, 10 programmes
│   ├── School of Philosophical, Anthropological and Film Studies — 1 subjects, 3 programmes
├── Interdisciplinary (1 subjects, 6 programmes)
│   ├── Graduate School — 1 subjects, 6 programmes
├── School of Medicine (1 subjects, 6 programmes)
│   ├── School of Medicine — 1 subjects, 6 programmes
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Degree level | Count | Description |
|-------------|-------|-------------|
| PGT Masters (MA/MLitt/MSc/MTh) | 78 | Taught postgraduate — typically 1 year full-time |
| Other: honours | 76 | Other |
| Bachelors (Honours) | 31 | 4-year Scottish MA (Hons) / BSc (Hons) / BTh (Honours) — single honours or unspecified structure |
| UG — joint/with/scotcom | 8 | Joint honours, with/honours degree, Scottish joint degree |
| Bachelors (International Honours) | 6 | 4-year BA (International Honours) — foreign language + home degree |
| PGT — MRes | 3 | Master of Research — 1 year, more research-focused than MSc |
| PG Diploma | 1 | PG Diploma — half-master's level, often 9 months |
| PG Certificate | 1 | PG Certificate — quarter-master's level, often 3-4 months |
| PGT — MPP | 1 | Master of Public Policy (or similar) |

### 0.4 分布矩阵 (Rule 4 — Faculty × Degree-level cross-tab)

| Faculty | BA/BSc (Hons) | BA (Int Hons) | Other: honours | PGCert | PGDip | PGT (MA/MSc) | PGT MPP | PGT MRes | UG joint/with | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Faculty of Arts | 13 | 4 | 20 | 0 | 1 | 27 | 0 | 0 | 4 | 69 |
| Faculty of Divinity | 0 | 0 | 4 | 1 | 0 | 6 | 0 | 0 | 4 | 15 |
| Faculty of Science | 9 | 0 | 44 | 0 | 0 | 21 | 0 | 1 | 0 | 75 |
| Faculty of Social Sciences | 2 | 2 | 8 | 0 | 0 | 19 | 1 | 2 | 0 | 34 |
| Interdisciplinary | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 6 |
| School of Medicine | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| **TOTAL** | 31 | 6 | 76 | 1 | 1 | 78 | 1 | 3 | 8 | **205** |

**Reconciliation**: matrix total = 205 | UG+PG count = 205 | **Match: True**

### 0.5 院校基本背景 (Institutional context)

| Item | Value |
|------|-------|
| Name | University of St Andrews |
| Country / Region | UK (Scotland) |
| Founded | 1413 (third-oldest university in the English-speaking world) |
| QS World Ranking | Top 100 globally (ranking varies by year) |
| Russell Group | Yes (member since 2012) |
| Total students | ~11,500 (UG ~8,500; PG ~3,000) |
| Campuses | Single campus in St Andrews, Fife (small coastal town) |
| Faculties | 4 (Arts, Science, Social Sciences, Divinity) + School of Medicine |
| Schools/Departments | 18+ academic schools |
| Mode of study | Full-time in-person; some online PG |
| Term system | Semester-based (Martinmas Sep-Dec; Candlemas Jan-May) |

---

## SECTION 1 — Undergraduate education

**Total UG programmes**: 96 unique course pages.
**Duration**: Most UG programmes are **4 years full-time** (Scottish MA/BSc Hons = 4 years, longer than the 3-year English BA/BSc).
**Modes**: In-person (St Andrews campus). Some joint programmes allow a year abroad.

### Faculty of Arts — UG programmes (29)

#### School of Art History
**Art History** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Art History MA](https://www.st-andrews.ac.uk/subjects/art-history/art-history-ma) | Honours | Four years full time | School of Art History |

#### School of Classics
**Ancient History** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Ancient History MA](https://www.st-andrews.ac.uk/subjects/ancient-history/ancient-history-ma) | Honours | Four years full time | School of Classics |

**Archaeology** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Ancient History and Archaeology MA](https://www.st-andrews.ac.uk/subjects/archaeology/ancient-history-archaeology-ma) | Honours | Four years full time | School of Classics |

**Classical Studies** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Classical Studies BA](https://www.st-andrews.ac.uk/subjects/classical-studies/classical-studies-ba) | International Honours | Four years full time | School of Classics |
| [Classical Studies MA](https://www.st-andrews.ac.uk/subjects/classical-studies/classical-studies-ma) | Honours | Four years full time | School of Classics |

**Classics, Greek and Latin** — 3 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Classics MA](https://www.st-andrews.ac.uk/subjects/classics-greek-latin/classics-ma) | Honours | Four years full time | School of Classics |
| [Greek MA](https://www.st-andrews.ac.uk/subjects/classics-greek-latin/greek-ma) | Honours | Four years full time | School of Classics |
| [Latin MA](https://www.st-andrews.ac.uk/subjects/classics-greek-latin/latin-ma) | Honours | Four years full time | School of Classics |

#### School of English
**English** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [English BA](https://www.st-andrews.ac.uk/subjects/english/english-ba) | International Honours | Four years full time | School of English |
| [English MA](https://www.st-andrews.ac.uk/subjects/english/english-ma) | Honours | Four years full time | School of English |

#### School of History
**Archaeology** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Medieval History and Archaeology MA](https://www.st-andrews.ac.uk/subjects/archaeology/medieval-history-archaeology-ma) | Honours | Four years full time | School of History |

**History** — 5 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [History BA](https://www.st-andrews.ac.uk/subjects/history/history-ba) | International Honours | Four years full time | School of History |
| [History MA](https://www.st-andrews.ac.uk/subjects/history/history-ma) | Honours | Four years full time | School of History |
| [Medieval History MA](https://www.st-andrews.ac.uk/subjects/history/medieval-history-ma) | Honours | Four years full time | School of History |
| [Modern History MA](https://www.st-andrews.ac.uk/subjects/history/modern-history-ma) | Honours | Four years full time | School of History |
| [Scottish History MA](https://www.st-andrews.ac.uk/subjects/history/scottish-history-ma) | Honours | Four years full time | School of History |

**Middle East Studies** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Middle East Studies MA](https://www.st-andrews.ac.uk/subjects/middle-east-studies/middle-east-studies-ma) | joint degree | Four years full time | School of History |

#### School of Modern Languages
**Arabic** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Arabic MA](https://www.st-andrews.ac.uk/subjects/arabic/arabic-ma) | joint degree | Four years full time | School of Modern Languages |

**Chinese Studies** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Chinese Studies MA](https://www.st-andrews.ac.uk/subjects/chinese-studies/chinese-studies-ma) | joint degree | Four years full time | School of Modern Languages |

**Comparative Literature** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Comparative Literature MA](https://www.st-andrews.ac.uk/subjects/comparative-literature/comparative-literature-ma) | (Honours) | Four years full time | School of Modern Languages |

**French** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [French MA](https://www.st-andrews.ac.uk/subjects/french/french-ma) | Honours | Four years full time | School of Modern Languages |

**German** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [German MA](https://www.st-andrews.ac.uk/subjects/german/german-ma) | Honours | Four years full time | School of Modern Languages |

**Italian** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Italian MA](https://www.st-andrews.ac.uk/subjects/italian/italian-ma) | Honours | Four years full time | School of Modern Languages |

**Persian** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Persian MA](https://www.st-andrews.ac.uk/subjects/persian/persian-ma) | joint degree | Four years full time | School of Modern Languages |

**Russian** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Russian MA](https://www.st-andrews.ac.uk/subjects/russian/russian-ma) | Honours | Four years full time | School of Modern Languages |

**Spanish** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Spanish MA](https://www.st-andrews.ac.uk/subjects/spanish/spanish-ma) | Honours | Four years full time | School of Modern Languages |

#### School of Philosophical, Anthropological and Film Studies
**Film Studies** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Film Studies BA](https://www.st-andrews.ac.uk/subjects/film-studies/film-studies-ba) | International Honours | Four years full time | School of Philosophical, Anthropological and Film Studies |
| [Film Studies MA](https://www.st-andrews.ac.uk/subjects/film-studies/film-studies-ma) | Honours | Four years full time | School of Philosophical, Anthropological and Film Studies |

**Philosophy** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Philosophy MA](https://www.st-andrews.ac.uk/subjects/philosophy/philosophy-ma) | Honours | Four years full time | School of Philosophical, Anthropological and Film Studies |

### Faculty of Divinity — UG programmes (8)

#### School of Divinity
**Divinity** — 8 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Bible and Culture MA](https://www.st-andrews.ac.uk/subjects/divinity/bible-and-culture-ma) | \'with\' degree | Four years full time | School of Divinity |
| [Biblical Studies MA](https://www.st-andrews.ac.uk/subjects/divinity/biblical-studies-ma) | Honours | Four years full time | School of Divinity |
| [Divinity BD](https://www.st-andrews.ac.uk/subjects/divinity/divinity-bd) | Honours | Three years full time | School of Divinity |
| [Hebrew MA](https://www.st-andrews.ac.uk/subjects/divinity/hebrew-ma) | joint degree | Four years full time | School of Divinity |
| [New Testament MA](https://www.st-andrews.ac.uk/subjects/divinity/new-testament-ma) | joint degree | Four years full time | School of Divinity |
| [Religion in Society MA](https://www.st-andrews.ac.uk/subjects/divinity/religion-in-society-ma) | \'with\' degree | Four years full time | School of Divinity |
| [Theological Studies MA](https://www.st-andrews.ac.uk/subjects/divinity/theological-studies-ma) | Honours | Four years full time | School of Divinity |
| [Theology MTheol](https://www.st-andrews.ac.uk/subjects/divinity/theology-mtheol) | Honours | Four years full time | School of Divinity |

### Faculty of Science — UG programmes (44)

#### School of Biology
**Biology** — 10 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Animal Behaviour BSc](https://www.st-andrews.ac.uk/subjects/biology/animal-behaviour-bsc) | Honours | Four years full time | School of Biology |
| [Biochemistry BSc](https://www.st-andrews.ac.uk/subjects/biology/biochemistry-bsc) | Honours | Four years full time | School of Biology |
| [Biochemistry MBiochem](https://www.st-andrews.ac.uk/subjects/biology/biochemistry-mbiochem) | Honours | Five years full time | School of Biology |
| [Biology BSc](https://www.st-andrews.ac.uk/subjects/biology/biology-bsc) | Honours | Four years full time | School of Biology |
| [Biology MBiol](https://www.st-andrews.ac.uk/subjects/biology/biology-mbiol) | Honours | Five years full time | School of Biology |
| [Cell Biology BSc](https://www.st-andrews.ac.uk/subjects/biology/cell-biology-bsc) | Honours | Four years full time | School of Biology |
| [Ecology and Conservation BSc](https://www.st-andrews.ac.uk/subjects/biology/ecology-conservation-bsc) | Honours | Four years full time | School of Biology |
| [Evolutionary Biology BSc](https://www.st-andrews.ac.uk/subjects/biology/evolutionary-biology-bsc) | Honours | Four years full time | School of Biology |
| [Molecular Biology Bsc](https://www.st-andrews.ac.uk/subjects/biology/molecular-biology-bsc) | Honours | Four years full time | School of Biology |
| [Zoology BSc](https://www.st-andrews.ac.uk/subjects/biology/zoology-bsc) | Honours | Four years full time | School of Biology |

**Marine Biology** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Marine Biology BSc](https://www.st-andrews.ac.uk/subjects/marine-biology/marine-biology-bsc) | Honours | Four years full time | School of Biology |
| [Marine Biology MMarBiol](https://www.st-andrews.ac.uk/subjects/marine-biology/marine-biology-mmarbiol) | Honours | Five years full time | School of Biology |

#### School of Chemistry
**Chemistry** — 7 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Chemical Sciences BSc](https://www.st-andrews.ac.uk/subjects/chemistry/chemical-sciences-bsc) | Honours | Four years full time | School of Chemistry |
| [Chemistry BSc](https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-bsc) | Honours | Four years full time | School of Chemistry |
| [Chemistry MChem](https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-mchem) | Honours | Five years full time | School of Chemistry |
| [Chemistry with Medicinal Chemistry BSc](https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-with-medicinal-chemistry-bsc) | Honours | Four years full time | School of Chemistry |
| [Chemistry with Medicinal Chemistry MChem](https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-with-medicinal-chemistry-mchem) | Honours | Five years full time | School of Chemistry |
| [Materials Chemistry BSc](https://www.st-andrews.ac.uk/subjects/chemistry/materials-chemistry-bsc) | Honours | Four years full time | School of Chemistry |
| [Materials Chemistry MChem](https://www.st-andrews.ac.uk/subjects/chemistry/materials-chemistry-mchem) | Honours | Five years full time | School of Chemistry |

#### School of Computer Science
**Computer Science** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Computer Science BSc](https://www.st-andrews.ac.uk/subjects/computer-science/computer-science-bsc) | Honours | Four years full time | School of Computer Science |
| [Computer Science MSci](https://www.st-andrews.ac.uk/subjects/computer-science/computer-science-msci) | Honours | Five years full time | School of Computer Science |

#### School of Earth and Environmental Sciences
**Earth and Environmental Sciences** — 3 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Earth Sciences MGeol](https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/earth-sciences-mgeol) | Honours | Five years full time | School of Earth and Environmental Sciences |
| [Environmental Earth Sciences BSc](https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/environmental-earth-sciences-bsc) | Honours | Four years full time | School of Earth and Environmental Sciences |
| [Geology BSc](https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/geology-bsc) | Honours | Four years full time | School of Earth and Environmental Sciences |

#### School of Geography and Sustainable Development
**Geography** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Geography BSc](https://www.st-andrews.ac.uk/subjects/geography/geography-bsc) | Honours | Four years full time | School of Geography and Sustainable Development |
| [Geography MA](https://www.st-andrews.ac.uk/subjects/geography/geography-ma) | Honours | Four years full time | School of Geography and Sustainable Development |

**Sustainable Development** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Sustainable Development BSc](https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-bsc) | Honours | Four years full time | School of Geography and Sustainable Development |
| [Sustainable Development MA](https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-ma) | Honours | Four years full time | School of Geography and Sustainable Development |

#### School of Mathematics and Statistics
**Mathematics** — 5 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Applied Mathematics MMath](https://www.st-andrews.ac.uk/subjects/mathematics/applied-mathematics-mmath) | Honours | Five years full time | School of Mathematics and Statistics |
| [Mathematics BSc](https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-bsc) | Honours | Four years full time | School of Mathematics and Statistics |
| [Mathematics MA](https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-ma) | Honours | Four years full time | School of Mathematics and Statistics |
| [Mathematics MMath](https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-mmath) | Honours | Five years full time | School of Mathematics and Statistics |
| [Pure Mathematics MMath](https://www.st-andrews.ac.uk/subjects/mathematics/pure-mathematics-mmath) | Honours | Five years full time | School of Mathematics and Statistics |

**Statistics** — 3 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Statistics BSc](https://www.st-andrews.ac.uk/subjects/statistics/statistics-bsc) | Honours | Four years full time | School of Mathematics and Statistics |
| [Statistics MA](https://www.st-andrews.ac.uk/subjects/statistics/statistics-ma) | Honours | Four years full time | School of Mathematics and Statistics |
| [Statistics MMath](https://www.st-andrews.ac.uk/subjects/statistics/statistics-mmath) | Honours | Five years full time | School of Mathematics and Statistics |

#### School of Physics and Astronomy
**Physics and Astronomy** — 5 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Astrophysics BSc](https://www.st-andrews.ac.uk/subjects/physics/astrophysics-bsc) | Honours | Four years full time | School of Physics and Astronomy |
| [Astrophysics MPhys](https://www.st-andrews.ac.uk/subjects/physics/astrophysics-mphys) | Honours | Five years full time | School of Physics and Astronomy |
| [Physics BSc](https://www.st-andrews.ac.uk/subjects/physics/physics-bsc) | Honours | Four years full time | School of Physics and Astronomy |
| [Physics MPhys](https://www.st-andrews.ac.uk/subjects/physics/physics-mphys) | Honours | Five years full time | School of Physics and Astronomy |
| [Theoretical Physics MPhys](https://www.st-andrews.ac.uk/subjects/physics/theoretical-physics-mphys) | Honours | Five years full time | School of Physics and Astronomy |

#### School of Psychology and Neuroscience
**Neuroscience** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Neuroscience BSc](https://www.st-andrews.ac.uk/subjects/neuroscience/neuroscience-bsc) | Honours | Four years full time | School of Psychology and Neuroscience |

**Psychology** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Psychology BSc](https://www.st-andrews.ac.uk/subjects/psychology/psychology-bsc) | Honours | Four years full time | School of Psychology and Neuroscience |
| [Psychology MA](https://www.st-andrews.ac.uk/subjects/psychology/psychology-ma) | Honours | Four years full time | School of Psychology and Neuroscience |

### Faculty of Social Sciences — UG programmes (10)

#### Business School
**Economics** — 3 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Economics BA](https://www.st-andrews.ac.uk/subjects/economics/economics-ba) | International Honours | Four years full time | Business School |
| [Economics BSc](https://www.st-andrews.ac.uk/subjects/economics/economics-bsc) | Honours | Four years full time | Business School |
| [Economics MA](https://www.st-andrews.ac.uk/subjects/economics/economics-ma) | Honours | Four years full time | Business School |

**Finance** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Financial Economics BSc](https://www.st-andrews.ac.uk/subjects/finance/financial-economics-bsc) | Honours | Four years full time | Business School |
| [Financial Economics MA](https://www.st-andrews.ac.uk/subjects/finance/financial-economics-ma) | Honours | Four years full time | Business School |

**Management** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Management BSc](https://www.st-andrews.ac.uk/subjects/management/management-bsc) | Honours | Four years full time | Business School |
| [Management MA](https://www.st-andrews.ac.uk/subjects/management/management-ma) | Honours | Four years full time | Business School |

#### School of International Relations
**International Relations** — 2 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [International Relations BA](https://www.st-andrews.ac.uk/subjects/international-relations/international-relations-ba) | International Honours | Four years full time | School of International Relations |
| [International Relations MA](https://www.st-andrews.ac.uk/subjects/international-relations/international-relations-ma) | Honours | Four years full time | School of International Relations |

#### School of Philosophical, Anthropological and Film Studies
**Social Anthropology** — 1 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Social Anthropology MA](https://www.st-andrews.ac.uk/subjects/social-anthropology/social-anthropology-ma) | Honours | Four years full time | School of Philosophical, Anthropological and Film Studies |

### Faculty of School of Medicine — UG programmes (5)

#### School of Medicine
**Medicine** — 5 programme(s)

| Programme | Degree | Duration | School |
|-----------|--------|----------|--------|
| [Gateway to Medicine](https://www.st-andrews.ac.uk/subjects/medicine/gateway-to-medicine) | (Honours) | One year | School of Medicine |
| [Medicine A100 BSc](https://www.st-andrews.ac.uk/subjects/medicine/medicine-bsc-a100) | Hons | Three years full time, plus three years training with a partner medical school | School of Medicine |
| [Medicine A990 BSc](https://www.st-andrews.ac.uk/subjects/medicine/medicine-bsc-a990) | Hons | Three years full time, plus three years of training with partner medical school | School of Medicine |
| [Medicine MBChB Scottish Community Orientated Medicine](https://www.st-andrews.ac.uk/subjects/medicine/medicine-mbchb-scotcom) | ScotCOM | Five years full time | School of Medicine |
| [Scottish Graduate Entry Medicine (ScotGEM) MBChB](https://www.st-andrews.ac.uk/subjects/medicine/scotgem-mbchb) | (Honours) | Four years full time | School of Medicine |

---

## SECTION 2 — Postgraduate education

**Total PG programmes (taught)**: 109 unique course pages (MSc, MLitt, MRes, PGDip, PGCert, DProf).
**PG Research (PGR)**: PhD/MPhil/EngD/MD available across all schools — listed on individual school research-degree pages, not the course search index.
**Duration**: Taught Masters usually **1 year full-time** (or 2 years part-time). PhD = 3-4 years full-time.
**Modes**: In-person, online (some MSc/PGDip/PGCert), part-time variants.

### Faculty of Arts — PG programmes (40)

#### International Education & Lifelong Learning Institute
**Digital Education** — 5 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Digital Education](https://www.st-andrews.ac.uk/subjects/digital-education/digital-education-september) | MSc, PGDip, PGCert | International Education & Lifelong Learning Institute |
| [Digital Education (MSc, PGDip, PGCert, modular) - online](https://www.st-andrews.ac.uk/subjects/digital-education/digital-education-september-online) | See page | International Education & Lifelong Learning Institute |
| [Digital Education MSc, PGDip](https://www.st-andrews.ac.uk/subjects/digital-education/digital-education-january) | See page | International Education & Lifelong Learning Institute |
| [Digital Education MSc, PGDip, PGCert, single module - online](https://www.st-andrews.ac.uk/subjects/digital-education/digital-education-january-online) | See page | International Education & Lifelong Learning Institute |
| [English and Digital Education MSc](https://www.st-andrews.ac.uk/subjects/digital-education/english-digital-education-msc-september) | See page | International Education & Lifelong Learning Institute |

**International Education** — 5 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [English and International Education](https://www.st-andrews.ac.uk/subjects/international-education/english-international-education-msc-september) | MSc | International Education & Lifelong Learning Institute |
| [International Education](https://www.st-andrews.ac.uk/subjects/international-education/international-education-january) | MSc, PGDip, PGCert | International Education & Lifelong Learning Institute |
| [International Education](https://www.st-andrews.ac.uk/subjects/international-education/international-education-september) | MSc, PGDip, PGCert | International Education & Lifelong Learning Institute |
| [International Education (MSc, PGDip, PGCert, modular) - Online](https://www.st-andrews.ac.uk/subjects/international-education/international-education-distance-september) | See page | International Education & Lifelong Learning Institute |
| [International Education (MSc, PGDip, PGCert, single module) - online](https://www.st-andrews.ac.uk/subjects/international-education/international-education-january-online) | See page | International Education & Lifelong Learning Institute |

**TESOL** — 5 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [English and Teaching English to Speakers of Other Languages (TESOL) MSc](https://www.st-andrews.ac.uk/subjects/tesol/english-tesol-msc-september) | See page | International Education & Lifelong Learning Institute |
| [Teaching English to Speakers of Other Language TESOL (MSc, PGDip, PGCert, modular) - online](https://www.st-andrews.ac.uk/subjects/tesol/tesol-msc-distance-learning-september) | See page | International Education & Lifelong Learning Institute |
| [Teaching English to Speakers of Other Languages (TESOL) - online with optional specialism](https://www.st-andrews.ac.uk/subjects/tesol/tesol-msc-distance-learning-january) | MSc, PGDip, PGCert, single module | International Education & Lifelong Learning Institute |
| [Teaching English to Speakers of Other Languages (TESOL) - with optional specialism](https://www.st-andrews.ac.uk/subjects/tesol/tesol-msc-january) | MSc, PGDip, PGCert | International Education & Lifelong Learning Institute |
| [Teaching English to Speakers of Other Languages (TESOL) - with optional specialism](https://www.st-andrews.ac.uk/subjects/tesol/tesol-msc-september) | MSc, PGDip, PGCert | International Education & Lifelong Learning Institute |

#### International Education and Lifelong Learning Institute (IELLI)
**TESOL** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Doctor of Professional Practice in Teaching English to Speakers of Other Languages (DProf TESOL) – Online](https://www.st-andrews.ac.uk/subjects/tesol/tesol-dprof-september-and-january) | See page | International Education and Lifelong Learning Institute (IELLI) |

#### School of Art History
**Art History** — 3 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Art History](https://www.st-andrews.ac.uk/subjects/art-history/art-history-mlitt) | MLitt | School of Art History |
| [Digital Art History - online](https://www.st-andrews.ac.uk/subjects/art-history/digital-art-history-online) | See page | School of Art History |
| [History of Photography](https://www.st-andrews.ac.uk/subjects/art-history/history-photography-mlitt) | MLitt | School of Art History |

#### School of Classics
**Classics, Greek and Latin** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Classics](https://www.st-andrews.ac.uk/subjects/classics-greek-latin/classics-mlitt) | MLitt | School of Classics |

#### School of English
**English** — 3 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Creative Writing](https://www.st-andrews.ac.uk/subjects/english/creative-writing-mlitt) | MLitt | School of English |
| [English Literature](https://www.st-andrews.ac.uk/subjects/english/english-mlitt) | MLitt | School of English |
| [Playwriting and Screenwriting](https://www.st-andrews.ac.uk/subjects/english/playwriting-screenwriting-mlitt) | MLitt | School of English |

#### School of History
**History** — 8 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Early Modern and Reformation History](https://www.st-andrews.ac.uk/subjects/history/early-modern-reformation-history-mlitt) | MLitt | School of History |
| [Intellectual History](https://www.st-andrews.ac.uk/subjects/history/intellectual-history-mlitt) | MLitt | School of History |
| [Legal and Constitutional Studies](https://www.st-andrews.ac.uk/subjects/history/legal-constitutional-studies-mlitt) | MLitt | School of History |
| [Medieval History](https://www.st-andrews.ac.uk/subjects/history/medieval-history-mlitt) | MLitt | School of History |
| [Medieval Studies](https://www.st-andrews.ac.uk/subjects/history/medieval-studies-mlitt) | MLitt | School of History |
| [Middle Eastern History](https://www.st-andrews.ac.uk/subjects/history/middle-eastern-history-mlitt) | MLitt | School of History |
| [Modern History](https://www.st-andrews.ac.uk/subjects/history/modern-history-mlitt) | MLitt | School of History |
| [The Book. History and Techniques of Analysis](https://www.st-andrews.ac.uk/subjects/history/book-history-mlitt) | MLitt | School of History |

**Middle East Studies** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Iranian Studies](https://www.st-andrews.ac.uk/subjects/middle-east-studies/iranian-studies-mlitt) | MLitt | School of History |
| [Iranian Studies (MLitt) - online](https://www.st-andrews.ac.uk/subjects/middle-east-studies/iranian-studies-mlitt-online) | See page | School of History |

#### School of Modern Languages
**Comparative Literature** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Comparative Literature](https://www.st-andrews.ac.uk/subjects/comparative-literature/comparative-literature-mlitt) | MLitt | School of Modern Languages |

**Digital Humanities** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Global Digital Humanities (MSc, PGDip, PGCert) - online](https://www.st-andrews.ac.uk/subjects/digital-humanities/global-digital-humanities) | See page | School of Modern Languages |

**German** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [German and Comparative Literature](https://www.st-andrews.ac.uk/subjects/german/german-comparative-literature-mlitt) | MLitt | School of Modern Languages |

#### School of Philosophical, Anthropological and Film Studies
**Film Studies** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Film Studies](https://www.st-andrews.ac.uk/subjects/film-studies/film-studies-mlitt) | MLitt | School of Philosophical, Anthropological and Film Studies |
| [IMACS: International Master in Audiovisual and Cinema Studies](https://www.st-andrews.ac.uk/subjects/film-studies/imacs-mlitt) | MLitt | School of Philosophical, Anthropological and Film Studies |

**Philosophy** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Conversion in Philosophy](https://www.st-andrews.ac.uk/subjects/philosophy/conversion-philosophy-graddip) | Graduate Diploma | School of Philosophical, Anthropological and Film Studies |
| [Philosophy](https://www.st-andrews.ac.uk/subjects/philosophy/philosophy-mlitt) | MLitt | School of Philosophical, Anthropological and Film Studies |

### Faculty of Divinity — PG programmes (7)

#### Music Centre
**Divinity** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Sacred Music](https://www.st-andrews.ac.uk/subjects/divinity/sacred-music-pgcert-online) | PGCert | Music Centre |

#### School of Divinity
**Divinity** — 6 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Bible and the Contemporary World - online](https://www.st-andrews.ac.uk/subjects/divinity/bible-contemporary-world-online) | MLitt, PGDip, modular | School of Divinity |
| [Biblical Languages and Literature](https://www.st-andrews.ac.uk/subjects/divinity/biblical-languages-literature-mlitt) | MLitt | School of Divinity |
| [Christian Theology](https://www.st-andrews.ac.uk/subjects/divinity/christian-theology-mlitt) | MLitt | School of Divinity |
| [Sacred Music](https://www.st-andrews.ac.uk/subjects/divinity/sacred-music-mlitt) | MLitt | School of Divinity |
| [The Study of Judaism and Christianity](https://www.st-andrews.ac.uk/subjects/divinity/judaism-and-christianity-mlitt) | MLitt | School of Divinity |
| [Theology and the Arts](https://www.st-andrews.ac.uk/subjects/divinity/theology-arts-mlitt) | MLitt | School of Divinity |

### Faculty of Science — PG programmes (31)

#### (no school)
**Earth and Environmental Sciences** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Environmental Science MSc](https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/environmental-science-msc) | See page | (no school) |

#### Graduate School
**Sustainable Development** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Global Sustainable Development](https://www.st-andrews.ac.uk/subjects/sustainable-development/global-sustainable-development-msc) | MSc | Graduate School |

#### School of Biology
**Biology** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Animal Behaviour](https://www.st-andrews.ac.uk/subjects/biology/animal-behaviour-msc) | MSc | School of Biology |

**Marine Biology** — 3 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Marine Ecosystem Management](https://www.st-andrews.ac.uk/subjects/marine-biology/marine-ecosystem-management-msc) | MSc | School of Biology |
| [Marine Mammal Science](https://www.st-andrews.ac.uk/subjects/marine-biology/marine-mammal-science-msc) | MSc | School of Biology |
| [Sustainable Aquaculture (MSc, PGDip, PGCert, Modular) - online](https://www.st-andrews.ac.uk/subjects/marine-biology/sustainable-aquaculture) | See page | School of Biology |

#### School of Chemistry
**Chemistry** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Catalysis](https://www.st-andrews.ac.uk/subjects/chemistry/catalysis-msc) | MSc | School of Chemistry |

#### School of Computer Science
**Computer Science** — 9 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Artificial Intelligence](https://www.st-andrews.ac.uk/subjects/computer-science/artificial-intelligence-msc) | MSc | School of Computer Science |
| [Artificial Intelligence (MSc) - conversion](https://www.st-andrews.ac.uk/subjects/computer-science/artificial-intelligence-msc-conversion) | See page | School of Computer Science |
| [Computer Science](https://www.st-andrews.ac.uk/subjects/computer-science/computer-science-msc) | MSc | School of Computer Science |
| [Computer Science (MSc) - conversion](https://www.st-andrews.ac.uk/subjects/computer-science/computer-science-msc-conversion) | See page | School of Computer Science |
| [Computing and Information Technology](https://www.st-andrews.ac.uk/subjects/computer-science/computing-information-technology-msc) | MSc | School of Computer Science |
| [Data Science (MSc, PGDip, PGCert) - online](https://www.st-andrews.ac.uk/subjects/computer-science/data-science) | See page | School of Computer Science |
| [Human Computer Interaction](https://www.st-andrews.ac.uk/subjects/computer-science/human-computer-interaction-msc) | MSc | School of Computer Science |
| [Machine Learning (MSc) - conversion](https://www.st-andrews.ac.uk/subjects/computer-science/machine-learning-msc-conversion) | See page | School of Computer Science |
| [Software Engineering](https://www.st-andrews.ac.uk/subjects/computer-science/software-engineering-msc) | MSc | School of Computer Science |

**Statistics** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Data-Intensive Analysis](https://www.st-andrews.ac.uk/subjects/statistics/data-intensive-analysis-msc) | MSc | School of Computer Science |

#### School of Earth and Environmental Sciences
**Earth and Environmental Sciences** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Applied Environmental Sciences MSc](https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/applied-environmental-sciences-msc) | See page | School of Earth and Environmental Sciences |
| [Geochemistry](https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/geochemistry-msc) | MSc | School of Earth and Environmental Sciences |

#### School of Geography and Sustainable Development
**Geography** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Data Literacy for Justice MSc, PGDip, PGCert - online](https://www.st-andrews.ac.uk/subjects/geography/data-for-justice) | See page | School of Geography and Sustainable Development |

#### School of Mathematics and Statistics
**Mathematics** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Mathematical Biology](https://www.st-andrews.ac.uk/subjects/mathematics/mathematical-biology-msc) | MSc | School of Mathematics and Statistics |
| [Mathematics](https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-msc) | MSc | School of Mathematics and Statistics |

**Statistics** — 3 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Applied Statistics and Datamining](https://www.st-andrews.ac.uk/subjects/statistics/applied-statistics-datamining-msc) | MSc | School of Mathematics and Statistics |
| [Statistical Ecology](https://www.st-andrews.ac.uk/subjects/statistics/statistical-ecology-msc) | MSc | School of Mathematics and Statistics |
| [Statistics](https://www.st-andrews.ac.uk/subjects/statistics/statistics-msc) | MSc | School of Mathematics and Statistics |

#### School of Physics and Astronomy
**Physics and Astronomy** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Astrophysics](https://www.st-andrews.ac.uk/subjects/physics/astrophysics-msc) | MSc | School of Physics and Astronomy |

#### School of Psychology and Neuroscience
**Neuroscience** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Neuroscience](https://www.st-andrews.ac.uk/subjects/neuroscience/neuroscience-mres) | MRes | School of Psychology and Neuroscience |

**Psychology** — 4 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Origins of Mind: Evolutionary and Developmental Perspectives](https://www.st-andrews.ac.uk/subjects/psychology/evolutionary-psychology-msc) | MSc | School of Psychology and Neuroscience |
| [Psychology Conversion](https://www.st-andrews.ac.uk/subjects/psychology/psychology-conversion-msc) | MSc | School of Psychology and Neuroscience |
| [Research Methods in Psychology](https://www.st-andrews.ac.uk/subjects/psychology/research-psychology-msc) | MSc | School of Psychology and Neuroscience |
| [The Psychology of Dementia Care PGCert - online](https://www.st-andrews.ac.uk/subjects/psychology/dementia-care-pgcert) | See page | School of Psychology and Neuroscience |

### Faculty of Social Sciences — PG programmes (24)

#### (no school)
**Management** — 3 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [International Business](https://www.st-andrews.ac.uk/subjects/management/international-business-mlitt) | MLitt | (no school) |
| [Management](https://www.st-andrews.ac.uk/subjects/management/management-mlitt) | MLitt | (no school) |
| [Marketing](https://www.st-andrews.ac.uk/subjects/management/marketing-mlitt) | MLitt | (no school) |

#### Business School
**Economics** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Economics](https://www.st-andrews.ac.uk/subjects/economics/economics-msc) | MSc | Business School |
| [Master of Public Policy](https://www.st-andrews.ac.uk/subjects/economics/master-public-policy) | MPP | Business School |

**Finance** — 5 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Accounting and Finance](https://www.st-andrews.ac.uk/subjects/finance/accounting-finance-msc) | MSc | Business School |
| [Banking and Finance](https://www.st-andrews.ac.uk/subjects/finance/banking-finance-msc) | MSc | Business School |
| [Finance](https://www.st-andrews.ac.uk/subjects/finance/finance-msc) | MSc | Business School |
| [Finance and Economics](https://www.st-andrews.ac.uk/subjects/finance/finance-economics-msc) | MSc | Business School |
| [Finance and Management](https://www.st-andrews.ac.uk/subjects/finance/finance-management-msc) | MSc | Business School |

**Management** — 4 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Entrepreneurship](https://www.st-andrews.ac.uk/subjects/management/entrepreneurship-msc) | MSc | Business School |
| [International Business](https://www.st-andrews.ac.uk/subjects/management/international-business-msc) | MSc | Business School |
| [Management](https://www.st-andrews.ac.uk/subjects/management/management-msc) | MSc | Business School |
| [Marketing](https://www.st-andrews.ac.uk/subjects/management/marketing-msc) | MSc | Business School |

#### School of International Relations
**International Relations** — 8 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Conflict and Security in Policy and Practice (MSc, PGCert, PGDip) - online](https://www.st-andrews.ac.uk/subjects/international-relations/conflict-security-policy-practice) | See page | School of International Relations |
| [International Political Theory](https://www.st-andrews.ac.uk/subjects/international-relations/international-political-theory-mlitt) | MLitt | School of International Relations |
| [International Security Studies](https://www.st-andrews.ac.uk/subjects/international-relations/international-security-studies-mlitt) | MLitt | School of International Relations |
| [Middle East, Caucasus and Central Asian Security Studies](https://www.st-andrews.ac.uk/subjects/international-relations/meccass-mlitt) | MLitt | School of International Relations |
| [Peacebuilding and Mediation](https://www.st-andrews.ac.uk/subjects/international-relations/peacebuilding-and-mediation-mlitt) | MLitt | School of International Relations |
| [Strategic Studies](https://www.st-andrews.ac.uk/subjects/international-relations/strategic-studies-mlitt) | MLitt | School of International Relations |
| [Terrorism and Political Violence](https://www.st-andrews.ac.uk/subjects/international-relations/terrorism-mlitt) | MLitt | School of International Relations |
| [Terrorism, Extremism and Political Violence (MLitt) - online](https://www.st-andrews.ac.uk/subjects/international-relations/terrorism-online-mlitt) | See page | School of International Relations |

#### School of Philosophical, Anthropological and Film Studies
**Social Anthropology** — 2 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Anthropology, Art and Perception](https://www.st-andrews.ac.uk/subjects/social-anthropology/anthropology-art-perception-mres) | MRes | School of Philosophical, Anthropological and Film Studies |
| [Social Anthropology](https://www.st-andrews.ac.uk/subjects/social-anthropology/social-anthropology-mres) | MRes | School of Philosophical, Anthropological and Film Studies |

### Faculty of Interdisciplinary — PG programmes (6)

#### Graduate School
**Interdisciplinary Studies** — 6 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Energy Policy and Finance](https://www.st-andrews.ac.uk/subjects/interdisciplinary/energy-policy-finance-msc) | MSc | Graduate School |
| [Gender Studies](https://www.st-andrews.ac.uk/subjects/interdisciplinary/gender-studies-mlitt) | MLitt | Graduate School |
| [Global Social and Political Thought](https://www.st-andrews.ac.uk/subjects/interdisciplinary/global-thought-mlitt) | MLitt | Graduate School |
| [Health Data Science](https://www.st-andrews.ac.uk/subjects/interdisciplinary/health-data-science-msc) | MSc | Graduate School |
| [Museum and Heritage Studies](https://www.st-andrews.ac.uk/subjects/interdisciplinary/museum-and-heritage-studies-mlitt) | MLitt | Graduate School |
| [Museums, Heritage and Society (MLitt, PGDip, PGCert) - online](https://www.st-andrews.ac.uk/subjects/interdisciplinary/museums-heritage-and-society-pg-online) | See page | Graduate School |

### Faculty of School of Medicine — PG programmes (1)

#### School of Medicine
**Medicine** — 1 programme(s)

| Programme | Degree | School |
|-----------|--------|--------|
| [Health Professions Education (PGCert, PGDip, MSc) - online](https://www.st-andrews.ac.uk/subjects/medicine/health-professions-education) | See page | School of Medicine |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 学术成绩要求 (Academic entry requirements)

Standard minimum academic entry requirements for **undergraduate** (range by programme):

| Qualification | Minimum |
|---------------|---------|
| SQA Highers | BBBB to AAAAB |
| A-Level | ABB to A*A*A |
| International Baccalaureate (IB) | 36 (HL 6,5,5) to 38 (HL 6,6,6 plus SL 6,6,6) |
| Cambridge Pre-U | D2 for A*, D3 for A, M1 for B |
| Welsh Baccalaureate | A in Advanced Skills Baccalaureate + AA at A-level (for AAA) |

> Source: https://www.st-andrews.ac.uk/subjects/entry/ — verified 2026-07-08
> Specific grades vary by programme; check individual programme pages.

### 3.2 英语语言要求 (English language requirements)

St Andrews uses a **profile system** — each school/subject area is assigned a profile (1-D to 7-D, plus 2-M for Medicine).

**UG profiles by faculty:**

| Faculty | Profile |
|---------|---------|
| Arts and Divinity (all Schools except School of English) | 3-D |
| Arts and Divinity (School of English) | 1-D |
| Medicine | 2-M |
| Science | 7-D |

**Test score thresholds (per profile):**

| Profile | IELTS Academic (min) | TOEFL iBT (min) | PTE Academic (min) | Cambridge (min) |
|---------|----------------------|-----------------|--------------------|-----------------|
| 1-D (UG/PG) | 7.0 (each 7.0) | 100 (L22/R22/W26/S24) | 76 (W80) | 185 / 191 |
| 2-M (Medicine) | 7.0 (each 7.0) | — | — | — |
| 3-D (UG) | 6.5 (each min varies) | 91 (L19/R19/W23/S22) | 70 (W76) | 176 / 185 |
| 4-D (UG) | 7.0 (L6.0/R6.0/S6.0/W7.0) | 91 (L16/R16/S19/W26) | 64 (W76) | 169 (W185) |
| 5-D (UG) | 6.0 (each 6.0) | 91 (L16/R16/S19/W19) | 64 (W76) | 169 / 185 |
| 6-D (UG) | 6.5 (L6.0/R6.0/W6.5/S6.0) | 81 (L16/R16/W23/S19) | 64 (W70) | 169 (W176) |
| 7-D (UG) | 6.0 (each 6.0) | 81 (L16/R16/W19/S19) | 64 (W70) | 169 / 176 |

> Sources: https://www.st-andrews.ac.uk/subjects/entry/language-requirements/profiles/{1-d, 2-m, 3-d, 4-d, 5-d, 6-d, 7-d}/ — verified 2026-07-08
> Test scores accepted if obtained within **2 years** of programme start date.
> Online versions of IELTS/TOEFL accepted for PG applicants only; UG must be in-person.

### 3.3 申请流程 (Application process)

- **UCAS** (UK undergraduates): all UG applications via UCAS. UCAS codes vary by programme (e.g. VV14 for Ancient History and Archaeology MA).
- **Direct application** (PG): via St Andrews postgraduate applicant portal.
- **Application portal**: https://www.st-andrews.ac.uk/study/apply/
- **Contact**: Admissions, St Katharine's West, The Scores, St Andrews, KY16 9AX | +44 (0)1334 46 2150

---

## SECTION 4 — Costs & financial aid

### 4.1 本科学费 (Undergraduate tuition fees)

| Fee status | 2024-25 | 2025-26 | 2026-27 | Notes |
|------------|---------|---------|---------|-------|
| Home (Scotland, SAAS-funded) | £1,820 | £1,820 | TBC | Paid by Scottish Government via SAAS |
| RUK (England, Wales, NI, RoI) | £9,250 | £9,535 | £9,790 (TBC) | Set by Westminster |
| Islands (Channel Islands, IoM) | £9,250 | £9,535 | £9,790 (TBC) | Aligned to RUK |
| **Overseas (Arts, Divinity, Science)** | £30,160 (2024 entry) | £31,670 | **£33,250** | Adjusts 3-5% annually |
| **Overseas (Medicine)** | £36,310 (pre-2023) | £37,730 | **£39,620** | Higher band |
| Part-time (Home, per 60 credits) | £910 | £910 | TBC | Arts/Divinity/Science |

> Source: https://www.st-andrews.ac.uk/study/tuition-fees/undergraduate/ — verified 2026-07-08
> Digital documentation registration fee: £20 one-off

### 4.2 研究生学费 (Postgraduate tuition fees, 2026-2027 entry)

**PGT Home (Scotland/UK) — by subject band:**

| Schools | 2024-25 | 2025-26 | 2026-27 |
|---------|---------|---------|---------|
| Most Arts, Science, Divinity, Medicine | £11,680 | £12,030 | £12,630 |
| IR, Economics, Finance, Management, Earth Sciences, Graduate School | £14,140 | £14,850 | £15,590 |

**PGT Overseas — by subject band:**

| Schools | 2024-25 | 2025-26 | 2026-27 |
|---------|---------|---------|---------|
| Art History, Classics, Divinity, English, History, Maths, Modern Languages, PAFS, Graduate School | £25,880 | £25,900 | £27,200 |
| Biology, Chemistry, Computer Science, Earth & Env Sci, IR, Medicine, Physics, Psychology, Management, Economics, Finance, Graduate School | £29,950 | £29,990 | £31,450 |

**PGR (Home) — 2026-27:**

| Degree | 2024-25 | 2025-26 | 2026-27 |
|--------|---------|---------|---------|
| PhD, MSt (Res), EngD, MD | £4,786 | £5,006 | £5,238 |
| MSc (Res) | £6,711 | £7,126 | £7,568 |
| DProf TESOL | £5,620 | £5,845 | £6,020 |
| DProf International Relations (Part time) | £2,393 | £2,503 | £2,619 |

**PGR (Overseas) — 2026-27:**

| Year of entry | 2024-25 | 2025-26 | 2026-27 |
|---------------|---------|---------|---------|
| 2026 entry | — | — | £22,220 |
| 2025 entry | — | £21,570 | £21,570 |
| 2024 entry | £20,940 | £20,940 | £20,940 |
| 2023 entry | £20,330 | £20,330 | £20,330 |
| 2022 entry | £19,360 | £19,360 | £19,360 |

> Source: https://www.st-andrews.ac.uk/study/tuition-fees/postgraduate/ — verified 2026-07-08

### 4.3 生活成本 (Living costs)

St Andrews is a small town; accommodation is competitive. Indicative annual costs:

- **Accommodation**: £5,000-£8,500 (varies by hall/catered/self-catered) — https://www.st-andrews.ac.uk/study/accommodation/
- **Food, travel, laundry, books**: budget separately
- **Scholarships**: https://www.st-andrews.ac.uk/study/scholarships/

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of St Andrews"
  source_url: https://www.st-andrews.ac.uk
  source_snippet: "University of St Andrews"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: ug_programme_count_unique
  value: 96
  source_url: https://standrews-search.funnelback.squiz.cloud/s/search.json?collection=standrews~sp-web-course--search&query=!null&num_ranks=200&sort=metatitle&f.tabs%7Ctype=Undergraduate
  source_snippet: "152 results returned by Funnelback; deduped to 96 unique programme URLs"
  capture_date: 2026-07-08
  evidence_type: api_response

E-U-003:
  field: pg_programme_count_unique
  value: 109
  source_url: https://standrews-search.funnelback.squiz.cloud/s/search.json?collection=standrews~sp-web-course--search&query=!null&num_ranks=200&sort=metatitle&f.tabs%7Ctype=Postgraduate
  source_snippet: "109 unique programme URLs returned by Funnelback"
  capture_date: 2026-07-08
  evidence_type: api_response

E-U-004:
  field: ug_overseas_fee_arts_div_science_2026
  value: "£33,250"
  source_url: https://www.st-andrews.ac.uk/study/tuition-fees/undergraduate/
  source_snippet: "2026 | — | — | £33,250 | Fees will be adjusted annually, with increases typically ranging from 3% to 5%"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-005:
  field: ug_overseas_fee_medicine_2026
  value: "£39,620"
  source_url: https://www.st-andrews.ac.uk/study/tuition-fees/undergraduate/
  source_snippet: "2026 | — | — | £39,620 | Tuition fees may increase each year..."
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-006:
  field: pg_pgt_overseas_arts_divinity_2026
  value: "£27,200"
  source_url: https://www.st-andrews.ac.uk/study/tuition-fees/postgraduate/
  source_snippet: "Art History Classics Divinity English... | £25,880 | £25,900 | £27,200"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-007:
  field: pgr_phd_home_2026
  value: "£5,238"
  source_url: https://www.st-andrews.ac.uk/study/tuition-fees/postgraduate/
  source_snippet: "PhD, MSt (Res), EngD, MD | £4,786 | £5,006 | £5,238"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-008:
  field: english_language_ielts_profile_1d
  value: "7.0 overall (7.0 each)"
  source_url: https://www.st-andrews.ac.uk/subjects/entry/language-requirements/profiles/1-d/
  source_snippet: "IELTS Academic (including IELTS One Skill retake) | 7.0 | 7.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-009:
  field: english_language_ielts_profile_3d_ug
  value: "6.5 overall"
  source_url: https://www.st-andrews.ac.uk/subjects/entry/language-requirements/profiles/3-d/
  source_snippet: "IELTS Academic | 6.5 | 7.0"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-010:
  field: english_language_ielts_profile_7d_ug
  value: "6.0 overall (6.0 each)"
  source_url: https://www.st-andrews.ac.uk/subjects/entry/language-requirements/profiles/7-d/
  source_snippet: "IELTS Academic | 6.0 | 6.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-011:
  field: a_level_minimum_ug
  value: "ABB to A*A*A"
  source_url: https://www.st-andrews.ac.uk/subjects/entry/
  source_snippet: "A-Level: ABB to A*A*A"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: ib_minimum_ug
  value: "36 (HL 6,5,5) to 38 (HL 6,6,6 plus SL 6,6,6)"
  source_url: https://www.st-andrews.ac.uk/subjects/entry/
  source_snippet: "International Baccalaureate (IB): 36 (HL 6,5,5) to 38 (HL 6,6,6 plus SL 6,6,6)"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### 6.1 Chunk boundaries

Document is split into chunks at the **faculty → school → subject** level. Each subject gets a chunk grouping all UG and PG programmes in that subject.

### 6.2 Chunk list

- **Chunk 001**: `Faculty of Arts / International Education & Lifelong Learning Institute / Digital Education` — 0 UG + 5 PG programmes
- **Chunk 002**: `Faculty of Arts / International Education & Lifelong Learning Institute / International Education` — 0 UG + 5 PG programmes
- **Chunk 003**: `Faculty of Arts / International Education & Lifelong Learning Institute / TESOL` — 0 UG + 5 PG programmes
- **Chunk 004**: `Faculty of Arts / International Education and Lifelong Learning Institute (IELLI) / TESOL` — 0 UG + 1 PG programmes
- **Chunk 005**: `Faculty of Arts / School of Art History / Art History` — 1 UG + 3 PG programmes
- **Chunk 006**: `Faculty of Arts / School of Classics / Ancient History` — 1 UG + 0 PG programmes
- **Chunk 007**: `Faculty of Arts / School of Classics / Archaeology` — 1 UG + 0 PG programmes
- **Chunk 008**: `Faculty of Arts / School of Classics / Classical Studies` — 2 UG + 0 PG programmes
- **Chunk 009**: `Faculty of Arts / School of Classics / Classics, Greek and Latin` — 3 UG + 1 PG programmes
- **Chunk 010**: `Faculty of Arts / School of English / English` — 2 UG + 3 PG programmes
- **Chunk 011**: `Faculty of Arts / School of History / Archaeology` — 1 UG + 0 PG programmes
- **Chunk 012**: `Faculty of Arts / School of History / History` — 5 UG + 8 PG programmes
- **Chunk 013**: `Faculty of Arts / School of History / Middle East Studies` — 1 UG + 2 PG programmes
- **Chunk 014**: `Faculty of Arts / School of Modern Languages / Arabic` — 1 UG + 0 PG programmes
- **Chunk 015**: `Faculty of Arts / School of Modern Languages / Chinese Studies` — 1 UG + 0 PG programmes
- **Chunk 016**: `Faculty of Arts / School of Modern Languages / Comparative Literature` — 1 UG + 1 PG programmes
- **Chunk 017**: `Faculty of Arts / School of Modern Languages / Digital Humanities` — 0 UG + 1 PG programmes
- **Chunk 018**: `Faculty of Arts / School of Modern Languages / French` — 1 UG + 0 PG programmes
- **Chunk 019**: `Faculty of Arts / School of Modern Languages / German` — 1 UG + 1 PG programmes
- **Chunk 020**: `Faculty of Arts / School of Modern Languages / Italian` — 1 UG + 0 PG programmes
- **Chunk 021**: `Faculty of Arts / School of Modern Languages / Persian` — 1 UG + 0 PG programmes
- **Chunk 022**: `Faculty of Arts / School of Modern Languages / Russian` — 1 UG + 0 PG programmes
- **Chunk 023**: `Faculty of Arts / School of Modern Languages / Spanish` — 1 UG + 0 PG programmes
- **Chunk 024**: `Faculty of Arts / School of Philosophical, Anthropological and Film Studies / Film Studies` — 2 UG + 2 PG programmes
- **Chunk 025**: `Faculty of Arts / School of Philosophical, Anthropological and Film Studies / Philosophy` — 1 UG + 2 PG programmes
- **Chunk 026**: `Faculty of Divinity / Music Centre / Divinity` — 0 UG + 1 PG programmes
- **Chunk 027**: `Faculty of Divinity / School of Divinity / Divinity` — 8 UG + 6 PG programmes
- **Chunk 028**: `Faculty of Science / (no school) / Earth and Environmental Sciences` — 0 UG + 1 PG programmes
- **Chunk 029**: `Faculty of Science / Graduate School / Sustainable Development` — 0 UG + 1 PG programmes
- **Chunk 030**: `Faculty of Science / School of Biology / Biology` — 10 UG + 1 PG programmes
- **Chunk 031**: `Faculty of Science / School of Biology / Marine Biology` — 2 UG + 3 PG programmes
- **Chunk 032**: `Faculty of Science / School of Chemistry / Chemistry` — 7 UG + 1 PG programmes
- **Chunk 033**: `Faculty of Science / School of Computer Science / Computer Science` — 2 UG + 9 PG programmes
- **Chunk 034**: `Faculty of Science / School of Computer Science / Statistics` — 0 UG + 1 PG programmes
- **Chunk 035**: `Faculty of Science / School of Earth and Environmental Sciences / Earth and Environmental Sciences` — 3 UG + 2 PG programmes
- **Chunk 036**: `Faculty of Science / School of Geography and Sustainable Development / Geography` — 2 UG + 1 PG programmes
- **Chunk 037**: `Faculty of Science / School of Geography and Sustainable Development / Sustainable Development` — 2 UG + 0 PG programmes
- **Chunk 038**: `Faculty of Science / School of Mathematics and Statistics / Mathematics` — 5 UG + 2 PG programmes
- **Chunk 039**: `Faculty of Science / School of Mathematics and Statistics / Statistics` — 3 UG + 3 PG programmes
- **Chunk 040**: `Faculty of Science / School of Physics and Astronomy / Physics and Astronomy` — 5 UG + 1 PG programmes
- **Chunk 041**: `Faculty of Science / School of Psychology and Neuroscience / Neuroscience` — 1 UG + 1 PG programmes
- **Chunk 042**: `Faculty of Science / School of Psychology and Neuroscience / Psychology` — 2 UG + 4 PG programmes
- **Chunk 043**: `Faculty of Social Sciences / (no school) / Management` — 0 UG + 3 PG programmes
- **Chunk 044**: `Faculty of Social Sciences / Business School / Economics` — 3 UG + 2 PG programmes
- **Chunk 045**: `Faculty of Social Sciences / Business School / Finance` — 2 UG + 5 PG programmes
- **Chunk 046**: `Faculty of Social Sciences / Business School / Management` — 2 UG + 4 PG programmes
- **Chunk 047**: `Faculty of Social Sciences / School of International Relations / International Relations` — 2 UG + 8 PG programmes
- **Chunk 048**: `Faculty of Social Sciences / School of Philosophical, Anthropological and Film Studies / Social Anthropology` — 1 UG + 2 PG programmes
- **Chunk 049**: `Interdisciplinary / Graduate School / Interdisciplinary Studies` — 0 UG + 6 PG programmes
- **Chunk 050**: `School of Medicine / School of Medicine / Medicine` — 5 UG + 1 PG programmes

**Total chunks**: 50 (one per faculty/school/subject triple)

---

## SECTION 7 — Cross-school comparison framework

| Axis | St Andrews | Note |
|------|-----------|------|
| Region | UK (Scotland) | 4-year Scottish MA = longer than 3-year English BA |
| UG duration | 4 years (most) | Distinct from rest of UK |
| PG duration | 1 year (most PGT) | Aligned with UK norm |
| Russell Group | **Yes** | Member since 2012 |
| Faculty structure | 4 faculties + 1 medical school | Distinct from many UK universities |
| Campus | Single (St Andrews town) | No London/multiple campuses |
| International fees (UG 2026) | £33,250 (most) | High end |
| International fees (PG 2026) | £27,200-£31,450 | High |
| Home fees (UG 2026) | £1,820 (Scotland), £9,790 (RUK) | Scotland much cheaper |
| Home fees (PG 2026) | £12,030-£15,590 | Mid-range UK |
| English language | 7 profiles (1-D to 7-D + 2-M) | 6.0-7.5 IELTS; selective |
| Academic entry | ABB to A*A*A | Selective |
| Total programmes | 205 (96 UG + 109 PG) | Smaller than large multi-campus universities |

### 7.1 Monitoring watchlist

| Frequency | URL pattern | Reason |
|-----------|-------------|--------|
| **High (monthly)** | `https://www.st-andrews.ac.uk/study/tuition-fees/{undergraduate,postgraduate}/` | Fees change annually |
| **High (monthly)** | `https://www.st-andrews.ac.uk/subjects/entry/language-requirements/profiles/*` | Language requirements |
| **High (monthly)** | `https://www.st-andrews.ac.uk/subjects/entry/` | Deadlines, requirements |
| **Medium (quarterly)** | `https://standrews-search.funnelback.squiz.cloud/...f.tabs%7Ctype=Undergraduate` | Programme list changes |
| **Medium (quarterly)** | `https://standrews-search.funnelback.squiz.cloud/...f.tabs%7Ctype=Postgraduate` | Programme list changes |
| **Low (annual)** | `https://www.st-andrews.ac.uk/about/` | University background |
| **Low (annual)** | `https://www.st-andrews.ac.uk/about/schools/` | School list |

