# Imperial College London Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科专业 (UG Majors) | 73 |
| 本科辅修 (Minors) | N/A (Imperial does not offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MRes/MBA/MPH/PG Cert/PG Dip) | 175 |
| 研究生博士项目 (PhD/Doctoral) | P0 follow-up (listed separately from main course search) |
| **学位项目总计 (UG + PGT)** | **248** |
| 学院 (Faculties) | 4 |

> **Data source**: Imperial course search page (`imperial.ac.uk/study/courses/`), 21 pages of results confirming "Showing 248 results".
> 
> **Note**: Imperial's 4-faculty structure means "学院" = Faculty (Engineering, Medicine, Natural Sciences, Business School). Doctoral (PhD) programs are not included in the main course search — they are listed under `imperial.ac.uk/study/apply/postgraduate-doctoral/` and require separate extraction.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Imperial College London
├── Faculty of Engineering                              [学院]
│   ├── Department of Aeronautics                       [系]
│   ├── Department of Bioengineering                    [系]
│   ├── Department of Chemical Engineering              [系]
│   ├── Department of Civil and Environmental Engineering [系]
│   ├── Department of Computing                         [系]
│   ├── Department of Earth Science and Engineering     [系]
│   ├── Department of Electrical and Electronic Engineering [系]
│   ├── Department of Materials                         [系]
│   ├── Department of Mechanical Engineering            [系]
│   └── Dyson School of Design Engineering              [系]
├── Faculty of Medicine                                 [学院]
│   ├── School of Medicine                              [系]
│   ├── School of Public Health                         [系]
│   ├── Department of Brain Sciences                    [系]
│   ├── Department of Immunology and Inflammation       [系]
│   ├── Department of Infectious Disease                [系]
│   ├── Department of Infectious Disease Epidemiology   [系]
│   ├── Department of Metabolism, Digestion and Reproduction [系]
│   ├── Department of Surgery and Cancer                [系]
│   ├── National Heart and Lung Institute (NHLI)        [系]
│   └── Centre for Paediatrics and Child Health         [系]
├── Faculty of Natural Sciences                         [学院]
│   ├── Department of Chemistry                         [系]
│   ├── Department of Life Sciences                     [系]
│   ├── Department of Mathematics                       [系]
│   ├── Department of Physics                           [系]
│   ├── Centre for Environmental Policy                 [系]
│   └── Science Communication Unit                      [系]
└── Imperial College Business School                    [学院]
    └── Imperial Business School (no internal dept. split for taught programs) [系]
```

> ⚠ **Cross-faculty notes**: Mathematics and Computer Science joint degrees are administered by the Department of Computing (Faculty of Engineering), not Mathematics. Economics, Finance and Data Science BSc is administered by the Business School. Medical Biosciences with Management BSc is also Business School.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BEng | Bachelor of Engineering | 本科 | 6 |
| BSc | Bachelor of Science | 本科 | 28 |
| MBBS | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| MEng | Master of Engineering (integrated) | 本科 (4-year integrated master's) | 23 |
| MSci | Master in Science (integrated) | 本科 (4-year integrated master's) | 13 |
| PhD | Doctor of Philosophy (intercalated) | 本科/研究生 | 1 |
| MSc | Master of Science | 研究生授课型 | 123 |
| MRes | Master of Research | 研究生研究型 | 41 |
| MBA | Master of Business Administration | 研究生授课型 | 4 |
| MPH | Master of Public Health | 研究生授课型 | 2 |
| PG Cert | Postgraduate Certificate | 研究生证书 | 3 |
| PG Dip | Postgraduate Diploma | 研究生文凭 | 2 |

> **UK degree naming note**: MEng and MSci are 4-year **integrated master's** degrees classified as undergraduate in the UK system. They are NOT equivalent to standalone MSc degrees. Imperial does NOT award BA degrees.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BEng | BSc | MBA | MBBS | MEng | MPH | MRes | MSc | MSci | PG Cert | PG Dip | PhD | 合计 |
|------------|------|-----|-----|------|------|-----|------|-----|------|---------|--------|-----|------|
| Faculty of Engineering | 6 | 4 | 0 | 0 | 23 | 0 | 7 | 57 | 3 | 0 | 0 | 0 | **100** |
| Faculty of Medicine | 0 | 1 | 0 | 2 | 0 | 2 | 13 | 21 | 1 | 3 | 2 | 1 | **46** |
| Faculty of Natural Sciences | 0 | 21 | 0 | 0 | 0 | 0 | 20 | 30 | 9 | 0 | 0 | 0 | **80** |
| Imperial College Business School | 0 | 2 | 4 | 0 | 0 | 0 | 1 | 15 | 0 | 0 | 0 | 0 | **22** |
| **合计** | **6** | **28** | **4** | **2** | **23** | **2** | **41** | **123** | **13** | **3** | **2** | **1** | **248** |

> **Reconciliation**: 100 + 46 + 80 + 22 = 248 ✓ (matches rule-1 total and rule-5 row count)

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Imperial College London has 4 faculties, each subdivided into departments. All undergraduate teaching is organized within these faculties. See Section 0.2 for the full hierarchy tree. Imperial does not have a separate "undergraduate college" — UG programs sit directly within the faculty and department structure.

UCAS institution code: **I50**. Imperial uses UCAS for all undergraduate applications (no Common App).

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Engineering

##### Department of Aeronautics

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Aeronautical Engineering MEng | H401 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/aeronautical-engineering/) |
| 2 | Aeronautics with Spacecraft Engineering MEng | Apply to H401 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/aeronautics-spacecraft-engineering/) |

##### Department of Bioengineering

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biomedical Engineering MEng | BH9C | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biomedical-engineering/) |
| 2 | Molecular Bioengineering MEng | H160 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/molecular-bioengineering/) |

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biomedical Technology Ventures BSc | B800 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biomedical-technology-ventures/) |

##### Department of Chemical Engineering

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemical Engineering MEng | H801 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemical-engineering/) |

##### Department of Civil and Environmental Engineering

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Civil Engineering MEng | H201 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/civil-engineering/) |

##### Department of Computing

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Computing MEng | G401 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-meng/) |
| 2 | Computing (Artificial Intelligence and Machine Learning) MEng | G700 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-artificial-intelligence-meng/) |
| 3 | Computing (International Programme of Study) MEng | G402 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-international-programme-of-study/) |
| 4 | Computing (Security and Reliability) MEng | G610 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-security-reliability-meng/) |
| 5 | Computing (Software Engineering) MEng | G600 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-software-engineering-meng/) |
| 6 | Computing (Visual Computing and Robotics) MEng | GG47 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-visual-computing-robotics-meng/) |
| 7 | Mathematics and Computer Science MEng | GG41 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computer-science-meng/) |
| 8 | Mathematics and Computer Science for AI MEng | GG03 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computer-science-ai-meng/) |

###### BEng (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Computing BEng | G400 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/computing-beng/) |
| 2 | Mathematics and Computer Science BEng | GG14 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computer-science-beng/) |
| 3 | Mathematics and Computer Science for AI BEng | GG02 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computer-science-ai-beng/) |

> ⚠ Mathematics and Computer Science joint degrees are administered by Computing (Engineering), not Mathematics (Natural Sciences).

##### Department of Earth Science and Engineering

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Earth and Planetary Science BSc | F64B | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/earth-planetary-science-bsc/) |
| 2 | Geology BSc | F600 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/geology-bsc/) |
| 3 | Geophysics BSc | F662 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/geophysics-bsc/) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Earth and Planetary Science MSci | F647 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/earth-planetary-science-msci/) |
| 2 | Geology MSci | F640 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/geology-msci/) |
| 3 | Geophysics MSci | F660 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/geophysics-msci/) |

##### Department of Electrical and Electronic Engineering

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Electrical and Electronic Engineering MEng | H604 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/electrical-electronic-engineering-meng/) |
| 2 | Electrical and Electronic Engineering with Management MEng | H6N2 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/electrical-electronic-engineering-management/) |
| 3 | Electronic and Information Engineering MEng | GH56 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/electronic-information-meng/) |

###### BEng (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Electrical and Electronic Engineering BEng | H600 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/electrical-electronic-engineering-beng/) |
| 2 | Electronic and Information Engineering BEng | HG65 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/electronic-information-beng/) |

##### Department of Materials

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biomaterials and Tissue Engineering MEng | BJ95 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biomaterials-tissue-engineering-meng/) |
| 2 | Materials Science and Engineering MEng | JFM2 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/materials-science-engineering-meng/) |
| 3 | Materials with Nuclear Engineering MEng | J5H8 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/materials-nuclear-engineering/) |

###### BEng (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Materials Science and Engineering BEng | JF52 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/materials-science-engineering-beng/) |

##### Department of Mechanical Engineering

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Mechanical Engineering MEng | H301 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mechanical-engineering/) |
| 2 | Mechanical Engineering with Nuclear Engineering MEng | Apply to H301 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mechanical-engineering-nuclear/) |

##### Dyson School of Design Engineering

###### MEng (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Design Engineering MEng | 28G3 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/design-engineering/) |

#### Faculty of Medicine

##### School of Medicine

###### MBBS (6-year undergraduate medicine)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Medicine MBBS/BSc | A100 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medicine/) |
| 2 | Medicine (Graduate Entry) MBBS (4YFT) | A102 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medicine-graduate-entry/) |

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Medical Biosciences BSc | B101 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medical-biosciences/) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Medical Science and Innovation MSci | B980 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medical-science-innovation/) |

###### PhD (Intercalated)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Intercalated PhD option for Medical Students MBBS/PhD | Apply to A100 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medicine-phd/) |

#### Faculty of Natural Sciences

##### Department of Chemistry

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemistry BSc | F100 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemistry-bsc/) |
| 2 | Chemistry with Management BSc | F1NF | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemistry-management/) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Chemistry MSci | F103 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemistry-msci/) |
| 2 | Chemistry with Medicinal Chemistry MSci | F124 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemistry-medicinal/) |
| 3 | Chemistry with Molecular Physics MSci | F1F3 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemistry-molecular-physics/) |

##### Department of Life Sciences

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biochemistry BSc | C700 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biochemistry-bsc/) |
| 2 | Biochemistry with a Language for Science BSc | C7R1 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biochemistry-language/) |
| 3 | Biochemistry with Management BSc | Apply to C700 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biochemistry-management/) |
| 4 | Biological Sciences BSc | C100 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biological-sciences/) |
| 5 | Biological Sciences with a Language for Science BSc | C1R1 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biological-sciences-language/) |
| 6 | Biological Sciences with Management BSc | Apply to C100 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biological-sciences-management/) |
| 7 | Biotechnology BSc | J700 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biotechnology/) |
| 8 | Biotechnology with a Language for Science BSc | J7R1 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biotechnology-language/) |
| 9 | Biotechnology with Management BSc | Apply to J700 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biotechnology-management/) |
| 10 | Ecology and Environmental Biology BSc | C180 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/ecology-environmental-biology/) |
| 11 | Microbiology BSc | C500 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/microbiology/) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Biochemistry MSci | C703 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biochemistry-msci/) |
| 2 | Biological Sciences MSci | C103 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biological-sciences-msci/) |
| 3 | Biotechnology MSci | J703 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/biotechnology-msci/) |

##### Department of Mathematics

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Mathematics BSc | G100 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-bsc/) |
| 2 | Mathematics (Pure Mathematics) BSc | G125 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/pure-mathematics-bsc/) |
| 3 | Mathematics with Applied Mathematics/Mathematical Physics BSc | G1F3 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-applied-physics/) |
| 4 | Mathematics with Mathematical Computation BSc | G102 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computation/) |
| 5 | Mathematics with Statistics BSc | G1G3 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-statistics/) |
| 6 | Mathematics with Statistics for Finance BSc | G1GH | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-statistics-finance/) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Mathematics MSci | G103 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-msci/) |

##### Department of Physics

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Physics BSc | F300 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/physics-bsc/) |
| 2 | Physics with Theoretical Physics BSc | F325 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/physics-theoretical-bsc/) |

###### MSci (4-year integrated master's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Physics MSci | F303 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/physics-msci/) |
| 2 | Physics with Theoretical Physics MSci | F390 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/physics-theoretical-msci/) |

#### Imperial College Business School

###### BSc (3-year bachelor's)

| # | 专业 | UCAS Code | URL |
|---|------|-----------|-----|
| 1 | Economics, Finance and Data Science BSc | L1N3 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/economics-finance-data-science/) |
| 2 | Medical Biosciences with Management BSc | B111 | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medical-biosciences-management/) |

> Note: Medical Biosciences with Management is a joint program between the School of Medicine and the Business School, administered by the Business School.

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Program | Primary Admin | Cross-listed Faculties | URL |
|---|---------|---------------|----------------------|-----|
| 1 | Mathematics and Computer Science (MEng/BEng) | Computing (Engineering) | Natural Sciences (Mathematics) | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computer-science-meng/) |
| 2 | Mathematics and Computer Science for AI (MEng/BEng) | Computing (Engineering) | Natural Sciences (Mathematics) | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/mathematics-computer-science-ai-meng/) |
| 3 | Medical Biosciences with Management BSc | Business School | Medicine | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/medical-biosciences-management/) |
| 4 | Chemistry with Molecular Physics MSci | Chemistry (Natural Sciences) | Physics (Natural Sciences) | [Link](https://www.imperial.ac.uk/study/courses/undergraduate/2027/chemistry-molecular-physics/) |

### 1.4 Minors — complete list

Imperial College London does not offer standalone minors in the US sense. Some programs offer "with Management" or "with a Language for Science" variants (listed above under their home departments). The I-Explore program provides breadth modules outside the main discipline.

### 1.5 General/Institute-wide requirements

- **Application platform**: UCAS (all UG)
- **Personal statement**: Required (UCAS format; single statement for all 5 UCAS choices)
- **Academic reference**: 1 required (from teacher/referee via UCAS)
- **Admissions tests**: Course-specific (ESAT for most engineering/science; TMUA for Computing/Mathematics; UCAT for Medicine; GAMSAT for Graduate Entry Medicine)
- **Interviews**: Conducted for most courses (not universal — varies by department)
- **Conditional offers**: Typical; based on predicted A-Level/IB grades
- **I-Explore**: All UG students take I-Explore modules outside their main discipline (breadth requirement)

### 1.6 UCAS Course Code → Major quick-lookup

| UCAS Code | Major |
|-----------|-------|
| A100 | Medicine MBBS/BSc |
| A102 | Medicine (Graduate Entry) MBBS |
| B101 | Medical Biosciences BSc |
| B111 | Medical Biosciences with Management BSc |
| B800 | Biomedical Technology Ventures BSc |
| B980 | Medical Science and Innovation MSci |
| BH9C | Biomedical Engineering MEng |
| BJ95 | Biomaterials and Tissue Engineering MEng |
| C100 | Biological Sciences BSc |
| C103 | Biological Sciences MSci |
| C180 | Ecology and Environmental Biology BSc |
| C500 | Microbiology BSc |
| C700 | Biochemistry BSc |
| C703 | Biochemistry MSci |
| C7R1 | Biochemistry with Language for Science BSc |
| C1R1 | Biological Sciences with Language for Science BSc |
| F100 | Chemistry BSc |
| F103 | Chemistry MSci |
| F124 | Chemistry with Medicinal Chemistry MSci |
| F1F3 | Chemistry with Molecular Physics MSci |
| F1NF | Chemistry with Management BSc |
| F300 | Physics BSc |
| F303 | Physics MSci |
| F325 | Physics with Theoretical Physics BSc |
| F390 | Physics with Theoretical Physics MSci |
| F600 | Geology BSc |
| F640 | Geology MSci |
| F64B | Earth and Planetary Science BSc |
| F647 | Earth and Planetary Science MSci |
| F660 | Geophysics MSci |
| F662 | Geophysics BSc |
| G100 | Mathematics BSc |
| G102 | Mathematics with Mathematical Computation BSc |
| G103 | Mathematics MSci |
| G125 | Mathematics (Pure Mathematics) BSc |
| G1F3 | Mathematics with Applied Mathematics BSc |
| G1G3 | Mathematics with Statistics BSc |
| G1GH | Mathematics with Statistics for Finance BSc |
| G400 | Computing BEng |
| G401 | Computing MEng |
| G402 | Computing (International) MEng |
| G600 | Computing (Software Engineering) MEng |
| G610 | Computing (Security and Reliability) MEng |
| G700 | Computing (AI and ML) MEng |
| GG02 | Mathematics and Computer Science for AI BEng |
| GG03 | Mathematics and Computer Science for AI MEng |
| GG14 | Mathematics and Computer Science BEng |
| GG41 | Mathematics and Computer Science MEng |
| GG47 | Computing (Visual Computing and Robotics) MEng |
| GH56 | Electronic and Information Engineering MEng |
| H160 | Molecular Bioengineering MEng |
| H201 | Civil Engineering MEng |
| H301 | Mechanical Engineering MEng |
| H401 | Aeronautical Engineering MEng |
| H600 | Electrical and Electronic Engineering BEng |
| H604 | Electrical and Electronic Engineering MEng |
| H6N2 | EEE with Management MEng |
| H801 | Chemical Engineering MEng |
| HG65 | Electronic and Information Engineering BEng |
| J5H8 | Materials with Nuclear Engineering MEng |
| J700 | Biotechnology BSc |
| J703 | Biotechnology MSci |
| J7R1 | Biotechnology with Language for Science BSc |
| JF52 | Materials Science and Engineering BEng |
| JFM2 | Materials Science and Engineering MEng |
| L1N3 | Economics, Finance and Data Science BSc |
| 28G3 | Design Engineering MEng |

---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Imperial's graduate taught programs are administered through the same 4 faculties as undergraduate. Programs carry degree designations MSc, MRes, MBA, MPH, PG Cert, or PG Dip. Note that doctoral (PhD) programs are listed separately at `imperial.ac.uk/study/apply/postgraduate-doctoral/` and are NOT included in the 175 PGT programs below.

#### Faculty of Engineering

##### Department of Aeronautics

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Aeronautical Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/advanced-aeronautical-engineering/) |
| 2 | Advanced Computational Methods for Aeronautics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computational-methods/) |
| 3 | Composites MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/composites/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Sciences MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/aerospace-sciences/) |

##### Department of Bioengineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (Biomaterials) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biomedical-engineering-biomaterials/) |
| 2 | Biomedical Engineering (Biomechanics and Mechanobiology) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biomedical-engineering-biomechanics/) |
| 3 | Biomedical Engineering (Computational Bioengineering) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biomedical-engineering-computational/) |
| 4 | Biomedical Engineering (Medical Physics) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biomedical-engineering-medical/) |
| 5 | Biomedical Engineering (Neurotechnology) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biomedical-engineering-neurotechnology/) |
| 6 | Engineering for Biomedicine MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/engineering-biomedicine/) |
| 7 | Human and Biological Robotics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/human-biological-robotics/) |
| 8 | Medical Device Design and Entrepreneurship MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/medical-device-design/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/bioengineering-mres/) |
| 2 | Alternative Protein MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/alternative-protein/) |
| 3 | Cancer Technology MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/cancer-technology/) |
| 4 | Neurotechnology MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/neurotechnology/) |

##### Department of Chemical Engineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Chemical Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/advanced-chemical-engineering/) |
| 2 | Advanced Chemical Engineering with Biotechnology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/chemical-engineering-biotechnology/) |
| 3 | Machine Learning and Process Systems Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/process-systems-engineering/) |

##### Department of Civil and Environmental Engineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Materials for Sustainable Infrastructure MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/advanced-materials-sustainable-infrastructure/) |
| 2 | Concrete Structures MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/concrete-structures/) |
| 3 | Earthquake Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/earthquake-engineering/) |
| 4 | Engineering Fluid Mechanics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/fluid-mechanics/) |
| 5 | Environmental Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/environmental-engineering/) |
| 6 | Environmental Engineering with Data Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/environmental-engineering-data-science/) |
| 7 | General Structural Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/general-structural-engineering/) |
| 8 | General Structural Engineering with Data Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/structural-engineering-data-science/) |
| 9 | Geotechnical and Earthquake Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/geotechnical-earthquake-engineering/) |
| 10 | Geotechnical and Geoenvironmental Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/geotechnical-geoenvironmental-engineering/) |
| 11 | Geotechnical and Geological Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/geotechnical-geological-engineering/) |
| 12 | Geotechnical Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/geotechnical-engineering/) |
| 13 | Geotechnical Engineering with Data Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/geotechnical-engineering-data-science/) |
| 14 | Geotechnical Engineering with Offshore Renewables MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/offshore-renewables/) |
| 15 | Hydrology and Water Resources Management MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/hydrology/) |
| 16 | Structural Steel Design MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/structural-steel-design/) |
| 17 | Transport MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/transport/) |
| 18 | Transport with Data Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/transport-data-science/) |

##### Department of Computing

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Computing MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/advanced-computing/) |
| 2 | Artificial Intelligence MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/artificial-intelligence/) |
| 3 | Computing MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computing/) |
| 4 | Computing (AI and Machine Learning) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computing-artificial-intelligence-msc/) |
| 5 | Computing (Management and Finance) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computing-management-finance/) |
| 6 | Computing (Security and Reliability) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computing-security-reliability-msc/) |
| 7 | Computing (Software Engineering) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computing-software-engineering-msc/) |
| 8 | Computing (Visual Computing and Robotics) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computing-visual-computing-robotics-msc/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Machine Learning MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/artificial-intelligence-machine-learning/) |

##### Department of Earth Science and Engineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Computational Science and Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applied-computational-science/) |
| 2 | Environmental Data Science and Machine Learning MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/environmental-data-science-machine-learning/) |
| 3 | Geo-Energy with Machine Learning and Data Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/geo-energy-machine-learning-data-science/) |
| 4 | Renewable Energy with AI and Data Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/renewable-energy/) |

##### Department of Electrical and Electronic Engineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Analogue and Digital Integrated Circuit Design MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/analogue-digital-circuit-design/) |
| 2 | Applied Machine Learning MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applied-machine-learning/) |
| 3 | Communications and Signal Processing MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/communications-signal-processing/) |
| 4 | Control and Optimisation MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/control-optimisation/) |
| 5 | Future Power Networks MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/future-power-networks/) |
| 6 | Sensor Systems Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/sensor-systems/) |

##### Department of Materials

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Materials Science and Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/advanced-materials/) |

##### Department of Mechanical Engineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Mechanical Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/advanced-mechanical-engineering/) |
| 2 | Sustainable Energy Futures MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/sustainable-energy-futures/) |

##### Dyson School of Design Engineering

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Cleantech Innovation MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/cleantech-innovation/) |
| 2 | Design Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/design-engineering-msc/) |
| 3 | Design with Behaviour Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/design-behaviour/) |
| 4 | Innovation Design Engineering MA/MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/innovation-design-engineering/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Design Engineering Research MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/design-engineering-mres/) |

#### Faculty of Medicine

##### School of Public Health

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Epidemiology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/epidemiology/) |
| 2 | Health Data Analytics and Machine Learning MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/health-data-analytics/) |

###### MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/public-health-masters/) |
| 2 | Master of Public Health (Online) | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/mph-online/) |

##### Department of Brain Sciences

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Translational Neuroscience MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/translational-neuroscience/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Experimental Neuroscience MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/experimental-neuroscience/) |

###### PG Cert

| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Biomedicine (Brain Sciences) (Online) | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computational-biomedicine-brain-sciences/) |
| 2 | Computational Biomedicine (Genomics) (Online) | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computational-biomedicine-genomics/) |

##### Department of Immunology and Inflammation

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Experimental Biomolecular Sciences MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/experimental-biomolecular-sciences/) |
| 2 | Immunology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/immunology/) |

##### Department of Infectious Disease

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Molecular Biology and Pathology of Viruses MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/molecular-biology/) |
| 2 | Molecular Medicine MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/molecular-medicine/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Research (Bacterial Pathogenesis and Infection) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/bacterial-pathogenesis-infection/) |
| 2 | Biomedical Research (Molecular Basis of Human Disease) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/molecular-basis-of-human-disease/) |

##### Department of Infectious Disease Epidemiology

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Research (Epidemiology, Evolution and Control of Infectious Diseases) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/epidemiology-evolution-control-infectious-diseases/) |

##### Department of Metabolism, Digestion and Reproduction

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Multiomics in Biomedicine MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applied-multiomics-biomedicine/) |
| 2 | Clinical Research (Human Nutrition) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/human-nutrition/) |
| 3 | Clinical Research (Diabetes and Obesity) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/diabetes-obesity/) |
| 4 | Clinical Research (Multiple Long-Term Conditions) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/multiple-long-term-conditions/) |
| 5 | Clinical Research (Translational Medicine) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/clinical-research/) |
| 6 | Human Molecular Genetics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/human-molecular-genetics/) |
| 7 | Reproductive and Developmental Biology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/reproductive-developmental-biology/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Research MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biomedical-research/) |
| 2 | Biomedical Research (Data Science) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/data-science/) |
| 3 | Biomedical Research (Microbiome in Health and Disease) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/microbiome-health-disease/) |
| 4 | Biomedical Research (Respiratory and Cardiovascular Science) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/respiratory-cardiovascular-science/) |

##### Department of Surgery and Cancer

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Translational Research in Surgery, Perioperative and Critical Care MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/translational-research-perioperative/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Cancer Biology MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/cancer-biology/) |
| 2 | Cancer Biology (Cancer Informatics) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/cancer-informatics/) |
| 3 | Cancer Biology (Cancer Innovation) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/cancer-innovation/) |
| 4 | Medical Robotics and Image-Guided Intervention MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/medical-robotics/) |
| 5 | Medical Robotics (Clinical Robotics and AI) MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/clinical-robotics-ai/) |

###### PG Dip

| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Health Leadership PG Dip | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/digital-health-leadership/) |
| 2 | Health Policy PG Dip | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/health-policy/) |

##### National Heart and Lung Institute (NHLI)

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioscience Futures MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/bioscience-futures/) |
| 2 | Cardiovascular and Respiratory Healthcare MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/cardiovascular-healthcare/) |
| 3 | Genes, Drugs and Stem Cells MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/genes-drugs-stem-cells/) |
| 4 | Genomic Medicine MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/genomic-medicine/) |
| 5 | Medical Ultrasound (Echocardiography) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/medical-ultrasound-echocardiography/) |
| 6 | Medical Ultrasound (Vascular) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/medical-ultrasound-vascular/) |

##### Centre for Paediatrics and Child Health

###### PG Cert

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Paediatrics PG Cert | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applied-paediatrics/) |

#### Faculty of Natural Sciences

##### Department of Chemistry

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Chemistry with AI and Automation MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/digital-chemistry/) |
| 2 | Synthetic Cell Science MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/synthetic-cell-science/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Molecular Synthesis MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/molecular-synthesis/) |
| 2 | Biological and Physical Chemistry MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biological-physical-chemistry/) |
| 3 | Catalysis: Chemistry and Engineering MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/catalysis/) |
| 4 | Chemical Biology and Bio-Entrepreneurship MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/chemical-biology/) |
| 5 | Drug Discovery and Development MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/drug-discovery-development/) |
| 6 | Green Chemistry, Energy and the Environment MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/green-chemistry/) |
| 7 | Nanomaterials MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/nanomaterials/) |
| 8 | Nanomedicine and Nanodiagnostics MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/nanomedicine/) |

##### Department of Life Sciences

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Biosciences and Biotechnology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biosciences-biotechnology/) |
| 2 | Living Planet with Computational Methods in Ecology and Evolution MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computational-methods-ecology-evolution-msc/) |
| 3 | Living Planet with Ecology, Evolution and Conservation MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/ecology-evolution-conservation/) |
| 4 | Living Planet with Nature-based Solutions MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/nature-based-solutions/) |
| 5 | Living Planet with Sustainable Agriculture and Technology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/sustainable-agriculture-technology/) |
| 6 | Taxonomy, Biodiversity and Evolution MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/taxonomy-biodiversity/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics and Theoretical Systems Biology MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/bioinformatics/) |
| 2 | Biosystematics MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/biosystematics/) |
| 3 | Living Planet with Computational Methods in Ecology and Evolution MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/computational-methods-ecology-evolution-mres/) |
| 4 | Living Planet with Ecology, Evolution and Conservation MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/ecology-evolution-conservation-research/) |
| 5 | Living Planet with Ecosystem and Environmental Change MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/ecosystems/) |
| 6 | Molecular and Cellular Biosciences MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/molecular-cellular-biosciences/) |
| 7 | Molecular Plant and Microbial Sciences MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/molecular-plant-microbial-sciences/) |
| 8 | Structural Biology MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/structural-biology/) |
| 9 | Systems and Synthetic Biology MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/systems-synthetic-biology/) |

##### Department of Mathematics

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applied-mathematics/) |
| 2 | Machine Learning and Data Science (Online) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/machine-learning-data-science/) |
| 3 | Mathematics and Finance MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/mathematics-finance/) |
| 4 | Pure Mathematics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/pure-mathematics-msc/) |
| 5 | Pure Mathematics (Formalisation of Mathematics) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/pure-mathematics-formalisation-msc/) |
| 6 | Statistics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/statistics/) |
| 7 | Statistics (Applied Statistics) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/statistics-applied-statistics/) |
| 8 | Statistics (Biostatistics) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/statistics-biostatistics/) |
| 9 | Statistics (Data Science and Machine Learning) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/statistics-data-science/) |
| 10 | Statistics (Statistical Finance) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/statistics-statistical-finance/) |
| 11 | Statistics (Theory and Methods) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/statistics-theory-methods/) |

##### Department of Physics

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Optics and Photonics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/optics-photonics/) |
| 2 | Physics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/physics/) |
| 3 | Physics with Extended Research MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/physics-extended-research/) |
| 4 | Physics with Fusion and Plasma Physics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/fusion-plasma/) |
| 5 | Physics with Quantum Dynamics MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/physics-quantum-dynamics/) |
| 6 | Quantum Fields and Fundamental Forces MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/quantum-fields-fundamental-forces/) |
| 7 | Security and Resilience: Science and Technology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/security-resilience-science-technology/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Machine Learning and Big Data in the Physical Sciences MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/machine-learning-physical-sciences/) |
| 2 | Photonics MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/photonics/) |
| 3 | Soft Electronic Materials MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/soft-electronic-materials/) |

##### Centre for Environmental Policy

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Conservation Science and Practice MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/conservation-science-practice/) |
| 2 | Environmental Technology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/environmental-technology/) |

##### Science Communication Unit

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Science Communication MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/science-communication/) |
| 2 | Science Media Production MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/science-media-production/) |

#### Imperial College Business School

The Business School has no internal departmental split for taught programs. All programs are administered centrally.

###### MSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Applications and Innovation MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applications-innovation/) |
| 2 | Business Analytics and AI MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/business-analytics/) |
| 3 | Climate Change, Management and Finance MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/climate-change-management-finance/) |
| 4 | Economics and Strategy for Business MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/economics-strategy-business/) |
| 5 | Finance MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/finance/) |
| 6 | Finance and Accounting MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/finance-accounting/) |
| 7 | Financial Technology MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/financial-technology/) |
| 8 | Global Health Management MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/global-health-management/) |
| 9 | Innovation, Entrepreneurship and Management MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/innovation-entrepreneurship-management/) |
| 10 | Investment and Wealth Management MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/investment-wealth-management/) |
| 11 | MSc in Management | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/management/) |
| 12 | Responsible Mining and Metals Finance MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/responsible-mining-metals-finance/) |
| 13 | Risk Management and Financial Engineering MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/risk-management-financial-engineering/) |
| 14 | Strategic Marketing MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/strategic-marketing/) |
| 15 | Strategic Marketing (Online) MSc | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/strategic-marketing-online/) |

###### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Full-Time MBA | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/full-time-mba/) |
| 2 | Executive MBA | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/executive-mba/) |
| 3 | Global Online MBA | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/global-mba/) |
| 4 | Weekend MBA | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/weekend-mba/) |

###### MRes

| # | 项目 | URL |
|---|------|-----|
| 1 | Business MRes | [Link](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/business-mres/) |

### 2.2 Graduate admissions model

Imperial's graduate admissions are **centralized** through the online application system. Students apply directly to Imperial (no UCAS for postgraduate). Key characteristics:

- **Application fee**: Required for most PGT programs (varies by program; Business School programs typically have higher fees)
- **Deadlines**: Rolling for most programs; some have fixed rounds (especially Business School)
- **English language**: Same two-tier system as UG (Standard / Higher)
- **GRE/GMAT**: Not generally required except for some Business School programs
- **References**: 2 academic references typically required

### 2.3 Doctoral programs (P0 follow-up)

Doctoral (PhD, MPhil, EngD) programs are NOT included in the 248 course search results. They are listed at:
- `imperial.ac.uk/study/apply/postgraduate-doctoral/`
- PhD types: Standard PhD, Split PhD, Professional Doctorate, Integrated PhD

This is a P0 gap for a future extraction run.

---

## SECTION 3 — Application Requirements & Deadlines

> **Region**: UK. Uses UCAS for undergraduate applications. Graduate applications are direct to Imperial.

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | UCAS | `imperial.ac.uk/study/apply/undergraduate/` |
| UCAS institution code | **I50** | Official Imperial UCAS listing |
| Applications open | 12 May 2026 (register); 1 Sep 2026 (submit) | `imperial.ac.uk/study/apply/undergraduate/process/deadlines/` |
| **Medicine deadline** | **15 October 2026** (18:00 UK time) | Same as Oxbridge deadline |
| **Equal consideration deadline** | **13 January 2027** (18:00 UK time) | All other UG courses |
| A-Level results day | August 2027 (TBC) | UK national |
| Application decisions | By late March 2027 | Imperial aims to decide by end of March |
| Personal statement | Required (UCAS format) | Single statement for all 5 UCAS choices |
| Academic reference | 1 required (teacher) | Via UCAS |
| Interview policy | Varies by department (most courses interview) | Check per-course pages |
| Admissions tests | ESAT (Engineering/Science), TMUA (Computing/Maths), UCAT (Medicine), GAMSAT (Grad Entry Medicine) | `imperial.ac.uk/study/apply/undergraduate/process/admissions-tests/` |
| Conditional offers | Yes (standard UK practice) | Based on predicted A-Level/IB grades |
| Deferred entry | Available (request via offer holder portal) | `imperial.ac.uk/study/apply/undergraduate/offer-holders/next-steps/deferred-entry/` |

### 3.2 Undergraduate English proficiency

Imperial uses a **two-tier** system: Standard and Higher level. Which level applies depends on the course.

| Exam | Standard Level | Higher Level |
|------|---------------|--------------|
| IELTS Academic | 6.5 overall (min 6.0 all elements) | 7.0 overall (min 6.5 all elements) |
| TOEFL iBT | 92 overall (min 20 all elements) | 100 overall (min 22 all elements) |
| PTE Academic | 62 overall (min 56 all elements) | 69 overall (min 62 all elements) |
| LanguageCert Academic | B2 Communicator (min 33 all skills) | C1 Expert (min 33 all skills) |
| Oxford Test of English (OTE) | 130 overall (min 120 all skills) | 140 overall (min 130 all skills) |
| Trinity ISE Level III | Pass | N/A |
| Trinity ISE Level IV | N/A | Pass |

> **Source**: `imperial.ac.uk/study/apply/english-language/`
> 
> **Exemptions**: Students who completed a qualification equivalent to a UK degree in certain English-speaking countries may be exempt. See English language exemption page.
> 
> **Pre-sessional English**: Imperial offers a Pre-Sessional English Programme for postgraduate students who have met offer conditions but need additional language support. The Business School does NOT accept pre-sessional courses.

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Application platform | Imperial online application (direct) |
| Application fee | Varies by program (typically £80-£150; Business School higher) |
| Fee waiver | Available for eligible applicants |
| Deadlines | Rolling (most programs); fixed rounds for Business School |
| References | 2 academic references |
| Personal statement | Required |
| English language | Same Standard/Higher two-tier system as UG |
| GRE/GMAT | Not generally required (some Business School programs may ask for GMAT) |
| Interviews | Varies by department |
| Research proposal | Required for MRes and doctoral applications |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate tuition fees (2026-27 academic year)

| Fee status | Annual tuition |
|------------|---------------|
| **Home (UK)** | **£9,790** (government cap for 2026-27) |
| Home (2027-28) | £10,050 (confirmed increase) |
| Placement year (Home) | Up to 20% of standard fee |
| Overseas study year (Home) | Up to 15% of standard fee |
| **Overseas (International)** | **Varies by course** (typically £37,900-£53,700) |

> **Source**: `imperial.ac.uk/study/fees-and-funding/undergraduate/tuition-fees/`
> 
> **Overseas fee range**: Overseas fees are per-course and listed on individual course pages. Typical 2026-27 ranges:
> - Classroom-based courses: ~£37,900/year
> - Lab-based courses: ~£40,700/year
> - Clinical (Medicine years 4-6): ~£53,700/year
> 
> Note: Overseas fees confirmed on individual course pages — this is a P1 follow-up for exact per-course values.

### 4.2 Living costs (2026, 9-month academic year)

| Expense | Weekly | Monthly | 9 Months |
|---------|--------|---------|----------|
| Accommodation (College-run) | £250 | £1,084 | £9,753 |
| Accommodation (Private sector) | £257 | £1,114 | £10,023 |
| Food | £71 | £307 | £2,764 |
| Travel (zone 1-2) | £27 | £119 | £1,071 |
| Personal and leisure | £69 | £297 | £2,672 |
| **Total (average)** | **£417-£424** | **£1,806-£1,837** | **£16,250-£16,530** |

| Range | Weekly | Monthly | 9 Months |
|-------|--------|---------|----------|
| Lower range | £292 | £1,264 | £11,375 |
| Average range | £397-£424 | £1,719-£1,837 | £15,470-£16,530 |
| Upper range | £489 | £2,118 | £19,055 |

> **Source**: `imperial.ac.uk/study/fees-and-funding/living-costs/`
> 
> **London premium**: Imperial is in South Kensington, one of the most expensive areas of London. The Student visa financial requirement mandates sufficient funds for first-year tuition + living costs.

### 4.3 Postgraduate tuition fees

| Fee status | Typical range |
|------------|---------------|
| Home (PGT) | £12,000-£20,000/year (varies by program) |
| Overseas (PGT) | £30,000-£45,000/year (varies by program) |
| MBA (Full-Time) | ~£67,500 total |
| PGT application deposit | Required for some programs |

> **Source**: `imperial.ac.uk/study/fees-and-funding/postgraduate-taught/tuition-fees/`
> 
> Doctoral fees are listed separately at `imperial.ac.uk/study/fees-and-funding/postgraduate-doctoral/tuition-fees/`.

### 4.4 Financial aid & funding

**Undergraduate (Home students)**:
- Tuition Fee Loan (becoming Lifelong Learning Entitlement from 2027): covers 100% of tuition
- Maintenance Loan: means-tested, higher for London
- Imperial Bursary: up to £5,000/year for Home students from low-income households
- NHS Bursary: for Medicine students in years 5-6

**Undergraduate (International students)**:
- No UK government loans
- Imperial Inspires scholarships (merit-based)
- IB Excellence scholarships
- Presidential scholarships for students of Black heritage
- External scholarships (Chevening, Commonwealth, country-specific)

**Postgraduate**:
- Postgraduate Master's Loan (Home students): up to £12,471 (2026-27)
- Postgraduate Doctoral Loan (Home students): up to £29,390
- President's PhD scholarships: full funding for exceptional candidates
- UKRI Research Council studentships (PhD)
- GREAT-Imperial scholarships (international)
- DAAD scholarships (German students)
- COLFUTURO loan-scholarships (Colombian students)
- Women in STEM Scholarships (ASEAN-UK SAGE)

**Key policy**: Imperial is NOT need-blind for international students. Fee status determines cost. Most UK universities are not need-blind.

### 4.5 Visa and Immigration Health Surcharge (IHS)

- Student visa required for international students
- IHS: ~£470/year for students (subject to change)
- Financial requirement: must show sufficient funds for first-year tuition + living costs (£1,334/month for 9 months in London = ~£12,006)

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.total_count
  value: 73 undergraduate programs
  source_url: https://www.imperial.ac.uk/study/courses/
  source_snippet: "Showing 248 results" (73 UG when filtered)
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.medicine
  value: "15 October 2026 (18.00 UK time)"
  source_url: https://www.imperial.ac.uk/study/apply/undergraduate/process/deadlines/
  source_snippet: "15 October 2026 (18.00 UK time) – Deadline for MBBS Medicine and Graduate Entry Medicine"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.equal_consideration
  value: "13 January 2027 (18.00 UK time)"
  source_url: https://www.imperial.ac.uk/study/apply/undergraduate/process/deadlines/
  source_snippet: "13 January 2027 (18.00 UK time) – Equal consideration deadline"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.tuition.home_2026_27
  value: "£9,790 per year"
  source_url: https://www.imperial.ac.uk/study/fees-and-funding/undergraduate/tuition-fees/
  source_snippet: "2026–27 academic year: Maximum fee for standard full-time courses will be £9,790 per year."
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.tuition.home_2027_28
  value: "£10,050 per year"
  source_url: https://www.imperial.ac.uk/study/fees-and-funding/undergraduate/tuition-fees/
  source_snippet: "2027–28 academic year: Maximum fee for standard full-time courses will increase to £10,050 per year."
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english.ielts.standard
  value: "6.5 overall (minimum 6.0 in all elements)"
  source_url: https://www.imperial.ac.uk/study/apply/english-language/
  source_snippet: "IELTS Academic: Standard level — 6.5 overall (minimum 6.0 in all elements)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english.ielts.higher
  value: "7.0 overall (minimum 6.5 in all elements)"
  source_url: https://www.imperial.ac.uk/study/apply/english-language/
  source_snippet: "IELTS Academic: Higher level — 7.0 overall (minimum 6.5 in all elements)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.ucas_code
  value: "I50"
  source_url: https://www.imperial.ac.uk/study/apply/undergraduate/
  source_snippet: "UCAS institution code: I50"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.admissions_tests
  value: "ESAT (Engineering/Science), TMUA (Computing/Maths), UCAT (Medicine), GAMSAT (Grad Entry Medicine)"
  source_url: https://www.imperial.ac.uk/study/apply/undergraduate/process/admissions-tests/
  source_snippet: "The test you could need to take for your application depends on which course you're applying for."
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.living_costs.average_9month
  value: "£16,250–£16,530 for 9 months"
  source_url: https://www.imperial.ac.uk/study/fees-and-funding/living-costs/
  source_snippet: "Totals: £417 to £424 weekly, £1,806 to £1,837 monthly, £16,250 to £16,530 9 months"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-G-001:
  field: graduate.pgt_total_count
  value: 175 postgraduate taught programs
  source_url: https://www.imperial.ac.uk/study/courses/
  source_snippet: "Showing 248 results" (175 PGT when filtered by Postgraduate taught)
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-G-002:
  field: graduate.faculty_structure
  value: "4 Faculties: Engineering, Medicine, Natural Sciences, Imperial College Business School"
  source_url: https://www.imperial.ac.uk/study/courses/
  source_snippet: Navigation structure shows Faculty of Engineering, Faculty of Medicine, Faculty of Natural Sciences, Imperial Business School
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-G-003:
  field: graduate.application_platform
  value: "Imperial online application (direct, not UCAS)"
  source_url: https://www.imperial.ac.uk/study/apply/postgraduate-taught/application-process/
  source_snippet: "Apply directly to Imperial for postgraduate study"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-G-004:
  field: graduate.application_fee
  value: "Varies by program (£80-£150 typical; Business School higher)"
  source_url: https://www.imperial.ac.uk/study/apply/postgraduate-taught/application-process/application-fee/
  source_snippet: "Application fee information for postgraduate taught courses"
  capture_date: 2026-07-04
  evidence_type: official_webpage

E-G-005:
  field: graduate.english.same_as_ug
  value: "Same Standard/Higher two-tier system as undergraduate"
  source_url: https://www.imperial.ac.uk/study/apply/english-language/
  source_snippet: "Standard level and Higher level requirements apply to all applicants"
  capture_date: 2026-07-04
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
imperial-college-london-knowledge-base-v2/
├── institution-overview        (Section 0 — counts, hierarchy, degree inventory, matrix)
├── undergraduate-programs      (Section 1 — chunked by faculty)
│   ├── engineering-ug          (100 UG programs)
│   ├── medicine-ug             (5 UG programs)
│   ├── natural-sciences-ug     (29 UG programs)
│   └── business-school-ug      (2 UG programs)
├── graduate-programs           (Section 2 — chunked by faculty)
│   ├── engineering-pgt         (50 PGT programs)
│   ├── medicine-pgt            (41 PGT programs)
│   ├── natural-sciences-pgt    (51 PGT programs)
│   └── business-school-pgt     (22 PGT programs)
├── application-requirements    (Section 3 — deadlines, tests, English)
├── costs-and-funding           (Section 4 — tuition, living costs, aid)
├── evidence-chain              (Section 5 — all evidence blocks)
└── comparison-framework        (Section 7 — cross-school matrix)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "imperial-college-london-knowledge-base-v2"
  school: "<Faculty of Engineering | Faculty of Medicine | Faculty of Natural Sciences | Imperial College Business School>"
  department: "<home department>"
  degree_level: "<BEng | BSc | MBBS | MEng | MSci | MSc | MRes | MBA | MPH | PG Cert | PG Dip>"
  level: undergraduate | postgraduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://www.imperial.ac.uk/study/courses/
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|------------|-------|
| **P0** | Doctoral (PhD/MPhil/EngD) program list | `imperial.ac.uk/study/apply/postgraduate-doctoral/` | Not in main 248 course search |
| **P0** | Per-course overseas tuition fees | Individual course pages | Overseas fees vary by course |
| **P0** | Per-course English level (Standard vs Higher) | Individual course pages | Which courses require Higher level |
| **P1** | Per-course A-Level/IB entry requirements | Individual course pages | Full details beyond headline grades |
| **P1** | Per-course admissions test requirements | Individual course pages | ESAT vs TMUA vs UCAT assignment |
| **P1** | Postgraduate application fee amounts | Per-program pages | Exact fee per program |
| **P1** | Business School MBA fees and GMAT requirements | Business School program pages | Different from other PGT |
| **P2** | Graduate teaching assistantship / stipend rates | Departmental pages | For doctoral students |
| **P2** | Accommodation costs by hall | Accommodation pages | More granular cost data |

---

## SECTION 7 — Cross-school Comparison Framework

| Dimension | Imperial College London | (Other School 1) | (Other School 2) |
|-----------|------------------------|-------------------|-------------------|
| **Country** | UK | | |
| **Region** | uk | | |
| **Total UG programs** | 73 | | |
| **Total PG programs (taught)** | 175 | | |
| **Total doctoral programs** | P0 follow-up | | |
| **Number of faculties** | 4 | | |
| **Application platform (UG)** | UCAS | | |
| **Early deadline** | 15 Oct (Medicine only) | | |
| **Regular deadline (UG)** | 13 Jan | | |
| **Home tuition (UG)** | £9,790 (2026-27) | | |
| **Overseas tuition (UG, typical)** | £37,900-£53,700 | | |
| **Living costs (9 months)** | £16,250-£16,530 | | |
| **IELTS minimum (Standard)** | 6.5 (min 6.0 each) | | |
| **IELTS minimum (Higher)** | 7.0 (min 6.5 each) | | |
| **TOEFL minimum (Standard)** | 92 (min 20 each) | | |
| **TOEFL minimum (Higher)** | 100 (min 22 each) | | |
| **Need-blind for internationals** | No | | |
| **Admissions tests (UG)** | ESAT/TMUA/UCAT/GAMSAT | | |
| **Interviews (UG)** | Most courses | | |
| **PGT application fee** | £80-£150 | | |
| **MBA tuition** | ~£67,500 | | |
| **Degree levels awarded** | BEng, BSc, MBBS, MEng, MSci, MSc, MRes, MBA, MPH, PG Cert, PG Dip, PhD | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: `imperial.ac.uk/study/` (single domain — all admissions, course, and finance data)
> **Verification**: ego-browser browserFetch + snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Total programs**: 248 (73 UG + 175 PGT)
> **Reconciliation**: Rule-1 total (248) == Matrix cell-sum (248) == Rule-5 row count (248) ✓
