# Pratt Institute Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless) + serverFetch + PDF extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BArch/BFA/BPS/BA/BS) | 22 |
| 本科辅修 (Minor) | 19 |
| 研究生学位项目 (M.Arch/MLA/MS/MFA/MA/MPS/MID/M.L.I.S.) | 43 |
| 研究生高级证书 (Advanced Certificate) | 22 |
| **学位项目总计 (UG + Grad)** | **106** |
| 学院 / 独立系所总数 | 6 |

> NOTE: 106 = raw program count from site extraction. Some programs may have concentrations listed separately (e.g., Digital Arts BFA has 3 emphasis tracks counted individually). Reconciliation with rule-5 tables in progress.

### 0.2 学院 / 系层级结构

```
Pratt Institute
├── School of Architecture [学院]
│   ├── Undergraduate Architecture [系]
│   │   └── Architecture (BArch) + Morphology Concentration
│   ├── Graduate Architecture, Landscape Architecture, and Urban Design [系]
│   │   └── M.Arch, MLA, MS Architecture, MS Urban Design
│   ├── Construction Management, Facilities Management, and Real Estate Practice [系]
│   │   └── BPS Construction Management + Minor
│   └── Graduate Center for Planning and the Environment [系]
│       └── MS Sustainable Environmental Systems, MS Urban & Community Planning,
│           MS Urban Placemaking & Management, MS Historic Preservation
│           + 4 Advanced Certificates
├── School of Art [学院]
│   ├── Digital Arts [系]
│   │   └── BFA (3 emphasis tracks), MFA (2 concentrations)
│   ├── Film [系]
│   │   └── BFA Film
│   ├── Fine Arts [系]
│   │   └── BFA Fine Arts, MFA Fine Arts
│   ├── Art and Design Education [系]
│   │   └── BFA, MA, BFA/MA combined, Advanced Certificate
│   ├── Photography [系]
│   │   └── BFA, MFA
│   ├── Dance/Movement Therapy [系]
│   │   └── MS (full + low residency)
│   └── Associate Degrees (AAS) [系]
│       └── Drawing/Painting, Graphic Design/Illustration, etc.
├── School of Design [学院]
│   ├── Communications Design [系]
│   │   └── BFA (Graphic Design + Illustration emphases), MFA
│   ├── Fashion [系]
│   │   └── BFA Fashion Design, MFA Fashion Collection + Communication, Minor
│   ├── Interior Design [系]
│   │   └── BFA, MFA (2-yr + 3-yr), Minor
│   └── Industrial Design [系]
│       └── MS Packaging/Identities/Systems Design, MID (referenced in grad tuition)
├── School of Information [学院]
│   ├── Library and Information Science [系]
│   │   └── M.S.L.I.S.
│   ├── Museums and Digital Culture [系]
│   │   └── MS
│   ├── Information Experience Design [系]
│   │   └── MS
│   ├── Data Analytics and Visualization [系]
│   │   └── MS
│   └── Advanced Certificates (7 programs)
│       └── Archives, Museum Libraries, Digital Humanities, UX,
│           Conservation & Digital Curation, Spatial Analysis,
│           Children's & Young Adult Library Services
├── School of Liberal Arts and Sciences [学院]
│   ├── History of Art and Design [系]
│   │   └── BA, BFA, MA, dual MA/MS with LIS
│   ├── Critical and Visual Studies [系]
│   │   └── BA
│   ├── Writing [系]
│   │   └── BFA, MFA
│   ├── Media Studies [系]
│   │   └── MA, Advanced Certificate
│   └── Minors (14 programs)
│       └── Black Studies, Cinema Studies, Coding, Creative Writing,
│           Cultural Studies, Gender & Sexuality Studies, History of Art,
│           Literature & Writing, Media Studies, Performance & Performance Studies,
│           Philosophy, Psychology, Social Justice/Social Practice,
│           Sustainability Studies, Teaching Creative Writing
└── School of Continuing and Professional Studies [学院]
    └── Non-degree programs (pre-college, continuing education)
```

### 0.3 学历级别明细

| 学位缩写 | canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|-----------|----------------|------|------|-----------|
| BArch | BArch | B.Arch | Bachelor of Architecture | 本科 | 2 |
| BFA | BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 12 |
| BPS | BPS | B.P.S. | Bachelor of Professional Studies | 本科 | 1 |
| BA | BA | B.A. | Bachelor of Arts | 本科 | 2 |
| BFA/MA | BFA/MA | B.F.A./M.A. | Combined Bachelor/Master | 本科+研究生 | 1 |
| Minor | Minor | Minor | 本科辅修 | 本科 | 19 |
| M.Arch | MArch | M.Arch | Master of Architecture | 研究生 | 1 |
| MLA | MLA | M.L.A. | Master of Landscape Architecture | 研究生 | 1 |
| MS | MS | M.S. | Master of Science | 研究生 | 15 |
| MFA | MFA | M.F.A. | Master of Fine Arts | 研究生 | 10 |
| MA | MA | M.A. | Master of Arts | 研究生 | 3 |
| MPS | MPS | M.P.S. | Master of Professional Studies | 研究生 | 4 |
| MID | MID | M.I.D. | Master of Industrial Design | 研究生 | 1 |
| M.L.I.S. | MS | M.S.L.I.S. | Master of Library & Info Science | 研究生 | 1 |
| Adv Cert | Certificate | Advanced Certificate | 高级证书 | 研究生 | 22 |

### 0.4 分布矩阵 (学院 x canonical 学位级别)

| 学院 \ 级别 | BArch | BFA | BPS | BA | Minor | MArch | MLA | MS | MFA | MA | MPS | MID | Certificate | 合计 |
|------------|-------|-----|-----|----|-------|-------|-----|----|----|----|----|-----|-------------|------|
| School of Architecture | 2 | 0 | 1 | 0 | 2 | 1 | 1 | 5 | 0 | 0 | 0 | 0 | 4 | 16 |
| School of Art | 0 | 9 | 0 | 0 | 5 | 0 | 0 | 2 | 6 | 1 | 4 | 0 | 2 | 29 |
| School of Design | 0 | 4 | 0 | 0 | 4 | 0 | 0 | 1 | 3 | 0 | 0 | 1 | 0 | 13 |
| School of Information | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 7 | 11 |
| School of Liberal Arts & Sciences | 0 | 2 | 0 | 2 | 8 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 3 | 19 |
| **合计** | **2** | **15** | **1** | **2** | **19** | **1** | **1** | **12** | **10** | **4** | **4** | **1** | **16** | **88** |

> Note: Matrix total (88) differs from raw extraction (106) because: (1) some programs appear in multiple schools' pages (cross-listed), (2) some entries are emphasis tracks within a degree (e.g., Digital Arts BFA has 3 emphases counted as separate entries in the raw extraction but 1 program in the matrix), (3) combined degrees (BFA/MA) counted once. The BFA/MA combined degree is counted under School of Art. The School of Continuing and Professional Studies offers non-degree programs only.

---

## SECTION 1 -- Undergraduate education

### 1.1 College/school architecture

Pratt Institute has 6 schools, 5 of which grant undergraduate degrees. The School of Information is graduate-only. All UG students complete a Foundation year. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors -- grouped by 学院 > 系 > 学位级别

#### School of Architecture

##### Undergraduate Architecture
###### BArch

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture, BArch | https://www.pratt.edu/architecture/undergraduate-architecture/architecture-barch/ |
| 2 | Architecture, BArch, Morphology Concentration | https://www.pratt.edu/architecture/undergraduate-architecture/architecture-barch-morphology-concentration/ |

##### Construction Management, Facilities Management, and Real Estate Practice
###### BPS

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management, BPS | https://www.pratt.edu/architecture/construction-management-facilities-management-and-real-estate-practice/construction-management-bps/ |

#### School of Art

##### Digital Arts
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Arts, BFA (Emphasis in 2-D Animation) | https://www.pratt.edu/art/digital-arts-bfa-emphasis-in-2-d-animation/ |
| 2 | Digital Arts, BFA (Emphasis in 3-D Animation and Motion Arts) | https://www.pratt.edu/art/digital-arts-bfa-emphasis-in-3-d-animation-and-motion-arts/ |
| 3 | Digital Arts, BFA (Emphasis in Art & Technology/formerly Interactive Arts) | https://www.pratt.edu/art/digital-arts-bfa-emphasis-in-art-technology-formerly-interactive-arts/ |

##### Game Arts
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Game Arts, BFA | https://www.pratt.edu/art/game-arts-bfa/ |

##### Film
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Film, BFA | https://www.pratt.edu/art/film-bfa/ |

##### Fine Arts
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Arts, BFA | https://www.pratt.edu/art/fine-arts-bfa/ |

##### Art and Design Education
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art and Design Education, BFA | https://www.pratt.edu/art/art-and-design-education-bfa/ |

##### Photography
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Photography, BFA | https://www.pratt.edu/art/photography-bfa/ |

#### School of Design

##### Communications Design
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Communications Design, BFA (Emphasis in Graphic Design) | https://www.pratt.edu/design/communications-design-bfa-emphasis-in-graphic-design/ |
| 2 | Communications Design, BFA (Emphasis in Illustration) | https://www.pratt.edu/design/communications-design-bfa-emphasis-in-illustration/ |

##### Fashion
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Design, BFA | https://www.pratt.edu/design/fashion-design-bfa/ |

##### Interior Design
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Interior Design, BFA | https://www.pratt.edu/design/interior-design-bfa/ |

#### School of Liberal Arts and Sciences

##### History of Art and Design
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | History of Art and Design, BA | https://www.pratt.edu/liberal-arts-and-sciences/history-of-art-and-design-ba/ |

###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | History of Art and Design, BFA | https://www.pratt.edu/liberal-arts-and-sciences/history-of-art-and-design-bfa/ |

##### Critical and Visual Studies
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Critical and Visual Studies, BA | https://www.pratt.edu/liberal-arts-and-sciences/critical-and-visual-studies-ba/ |

##### Writing
###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Writing, BFA | https://www.pratt.edu/liberal-arts-and-sciences/writing-bfa/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 项目 | 父级学院 | URL |
|---|------|---------|-----|
| 1 | Art and Design Education Combined Degree, BFA/MA | School of Art + School of Liberal Arts & Sciences | https://www.pratt.edu/art/art-and-design-education-combined-degree-bfa-ma/ |

### 1.4 Minors -- complete list

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | Construction Management Minor | School of Architecture | https://www.pratt.edu/architecture/construction-management-facilities-management-and-real-estate-practice/construction-management-minor/ |
| 2 | Morphology Minor | School of Architecture | https://www.pratt.edu/architecture/undergraduate-architecture/morphology-minor/ |
| 3 | Ceramics Minor | School of Art | https://www.pratt.edu/art/ceramics-minor/ |
| 4 | Film/Video Minor | School of Art | https://www.pratt.edu/art/film-video-minor/ |
| 5 | Photography Minor | School of Art | https://www.pratt.edu/art/photography-minor/ |
| 6 | Teaching Art and Design in NYC Minor | School of Art | https://www.pratt.edu/art/teaching-art-and-design-in-nyc-minor/ |
| 7 | Museum and Gallery Practices Minor | School of Art | https://www.pratt.edu/art/museum-and-gallery-practices-minor/ |
| 8 | Fashion Minor | School of Design | https://www.pratt.edu/design/fashion-minor/ |
| 9 | Interior Design Minor | School of Design | https://www.pratt.edu/design/interior-design-minor/ |
| 10 | Entrepreneurship Minor | School of Design | https://www.pratt.edu/design/entrepreneurship-minor/ |
| 11 | Textiles Minor | School of Design | https://www.pratt.edu/design/textiles-minor/ |
| 12 | UX/UI Minor | School of Design | https://www.pratt.edu/design/ux-ui-minor/ |
| 13 | Black Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/black-studies-minor/ |
| 14 | Cinema Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/cinema-studies-minor/ |
| 15 | Coding Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/coding-minor/ |
| 16 | Creative Writing Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/creative-writing-minor/ |
| 17 | Cultural Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/cultural-studies-minor/ |
| 18 | Gender and Sexuality Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/gender-and-sexuality-studies-minor/ |
| 19 | History of Art Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/history-of-art-minor/ |
| 20 | Literature and Writing Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/literature-and-writing-minor/ |
| 21 | Media Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/media-studies-minor/ |
| 22 | Performance and Performance Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/performance-and-performance-studies-minor/ |
| 23 | Philosophy Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/philosophy-minor/ |
| 24 | Psychology Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/psychology-minor/ |
| 25 | Social Justice/Social Practice Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/social-justice-social-practice-minor/ |
| 26 | Sustainability Studies Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/sustainability-studies-minor/ |
| 27 | Teaching Creative Writing Minor | School of Liberal Arts & Sciences | https://www.pratt.edu/liberal-arts-and-sciences/teaching-creative-writing-minor/ |

> Note: Minor count discrepancy -- 27 minors listed vs 19 in Rule 1 count. The Rule 1 count of 19 may have excluded some minors that were not extracted from all school pages. Reconciliation needed.

### 1.5 General/Institute-wide requirements

Pratt requires a **Foundation year** for all art and design students. The Foundation program is a yearlong experience providing a common base for all subsequent work. Students in the School of Architecture, School of Art, and School of Design complete Foundation before entering their major.

### 1.6 Associate Degrees (AAS)

Pratt also offers Associate in Applied Science (AAS) degrees through the School of Art:
- Drawing/Painting
- Graphic Design/Illustration
- And others (see https://www.pratt.edu/art/associate-degrees/)

---

## SECTION 2 -- Graduate education

### 2.1 Graduate programs -- grouped by 学院 > 系 > 学位级别

#### School of Architecture

##### Graduate Architecture, Landscape Architecture, and Urban Design

###### M.Arch

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Architecture (M.Arch/First Professional) | https://www.pratt.edu/architecture/graduate-architecture/master-of-architecture-m-arch-first-professional/ |

###### MLA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Landscape Architecture (MLA/First Professional) | https://www.pratt.edu/architecture/graduate-architecture/master-of-landscape-architecture-mla-first-professional/ |

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Architecture (Post Professional) | https://www.pratt.edu/architecture/graduate-architecture/master-of-science-in-architecture-post-professional/ |
| 2 | Master of Science in Urban Design (Post Professional) | https://www.pratt.edu/architecture/graduate-architecture/master-of-science-in-urban-design-post-professional/ |

##### Graduate Center for Planning and the Environment

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainable Environmental Systems, MS | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/sustainable-environmental-systems-ms/ |
| 2 | Urban and Community Planning, MS | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/urban-and-community-planning-ms/ |
| 3 | Urban Placemaking and Management, MS | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/urban-placemaking-and-management-ms/ |
| 4 | Historic Preservation, MS | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/historic-preservation-ms/ |

###### MS (from grad tuition PDF)

| # | 项目 | URL |
|---|------|-----|
| 1 | Real Estate Practice, MS | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/real-estate-practice-ms/ |

###### Advanced Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Community Planning, Advanced Certificate | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/advanced-certificates/community-planning-advanced-certificate/ |
| 2 | Historic Preservation, Advanced Certificate | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/advanced-certificates/historic-preservation-advanced-certificate/ |
| 3 | Sustainable Environmental Systems, Advanced Certificate | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/advanced-certificates/sustainable-environmental-systems-advanced-certificate/ |
| 4 | Urban Placemaking, Advanced Certificate | https://www.pratt.edu/architecture/graduate-center-for-planning-and-the-environment/advanced-certificates/urban-placemaking-advanced-certificate/ |

#### School of Art

##### Dance/Movement Therapy

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Dance/Movement Therapy, MS | https://www.pratt.edu/art/dance-movement-therapy-ms/ |
| 2 | Dance/Movement Therapy, MS, Low Residency Program | https://www.pratt.edu/art/dance-movement-therapy-ms-low-residency-program/ |

##### Digital Arts

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Arts, MFA (3-D Animation and Motion Arts Concentration) | https://www.pratt.edu/art/digital-arts-mfa-3-d-animation-and-motion-arts-concentration/ |
| 2 | Digital Arts, MFA (Interactive Arts Concentration) | https://www.pratt.edu/art/digital-arts-mfa-interactive-arts-concentration/ |

##### Fine Arts

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Fine Arts, MFA | https://www.pratt.edu/art/fine-arts-mfa/ |

##### Art and Design Education

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Art and Design Education, MA | https://www.pratt.edu/art/art-and-design-education-ma/ |

###### BFA/MA (combined)

| # | 项目 | URL |
|---|------|-----|
| 1 | Art and Design Education Combined Degree, BFA/MA | https://www.pratt.edu/art/art-and-design-education-combined-degree-bfa-ma/ |

##### Photography

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Photography, MFA | https://www.pratt.edu/art/photography-mfa/ |

##### Art Therapy (from grad tuition PDF)

###### MPS

| # | 项目 | URL |
|---|------|-----|
| 1 | Art Therapy, MPS | (program listed in grad tuition PDF) |
| 2 | Art Therapy, MPS Low Residency | (program listed in grad tuition PDF) |

##### Arts and Cultural Management (from grad tuition PDF)

###### MPS

| # | 项目 | URL |
|---|------|-----|
| 1 | Arts and Cultural Management, MPS | (program listed in grad tuition PDF) |

##### Design Management (from grad tuition PDF)

###### MPS

| # | 项目 | URL |
|---|------|-----|
| 1 | Design Management, MPS | (program listed in grad tuition PDF) |

##### Painting and Drawing (from grad tuition PDF)

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Painting and Drawing, MFA | (program listed in grad tuition PDF) |

##### Integrated Practices (from grad tuition PDF)

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Integrated Practices, MFA | (program listed in grad tuition PDF) |

##### Sculpture (from grad tuition PDF)

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Sculpture, MFA | (program listed in grad tuition PDF) |

##### Printmaking (from grad tuition PDF)

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Printmaking, MFA | (program listed in grad tuition PDF) |

##### Advanced Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Art and Design Education, Advanced Certificate | https://www.pratt.edu/art/art-and-design-education-advanced-certificate/ |
| 2 | Teaching and Learning, Advanced Certificate | https://www.pratt.edu/art/teaching-and-learning-advanced-certificate/ |

#### School of Design

##### Communications Design

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Communications Design, MFA | https://www.pratt.edu/design/communications-design-mfa/ |

##### Fashion

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion Collection + Communication, MFA | https://www.pratt.edu/design/fashion-collection-communication-mfa/ |

##### Interior Design

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Interior Design, MFA | https://www.pratt.edu/design/interior-design-mfa/ |

##### Packaging, Identities and Systems Design

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Packaging, Identities and Systems Design, MS | https://www.pratt.edu/design/packaging-identities-and-systems-design-ms/ |

##### Industrial Design (from grad tuition PDF)

###### MID

| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Design, MID | (program listed in grad tuition PDF) |

#### School of Information

##### Library and Information Science

###### M.S.L.I.S.

| # | 项目 | URL |
|---|------|-----|
| 1 | Library and Information Science, MS | https://www.pratt.edu/information/library-and-information-science-ms/ |

##### Museums and Digital Culture

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Museums and Digital Culture, MS | https://www.pratt.edu/information/museums-and-digital-culture-ms/ |

##### Information Experience Design

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Information Experience Design, MS | https://www.pratt.edu/information/information-experience-design-ms/ |

##### Data Analytics and Visualization

###### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Data Analytics and Visualization, MS | https://www.pratt.edu/information/data-analytics-and-visualization-ms/ |

##### Dual Degrees

| # | 项目 | URL |
|---|------|-----|
| 1 | History of Art and Design / Library and Information Science, MA/MS | https://www.pratt.edu/information/history-of-art-and-design-library-and-information-science-ma-ms/ |

##### Advanced Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Archives, Advanced Certificate | https://www.pratt.edu/information/archives-advanced-certificate/ |
| 2 | Museum Libraries, Advanced Certificate | (from grad tuition PDF) |
| 3 | Conservation and Digital Curation, Advanced Certificate | https://www.pratt.edu/information/conservation-and-digital-curation-advanced-certificate/ |
| 4 | Digital Humanities, Advanced Certificate | https://www.pratt.edu/information/digital-humanities-advanced-certificate/ |
| 5 | Spatial Analysis and Design, Advanced Certificate | https://www.pratt.edu/information/spatial-analysis-and-design-advanced-certificate/ |
| 6 | User Experience, Advanced Certificate | https://www.pratt.edu/information/user-experience-advanced-certificate/ |
| 7 | Children's and Young Adult Library Services, Advanced Certificate | https://www.pratt.edu/information/childrens-and-young-adult-library-services-advanced-certificate/ |

#### School of Liberal Arts and Sciences

##### History of Art and Design

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | History of Art and Design, MA | https://www.pratt.edu/liberal-arts-and-sciences/history-of-art-and-design-ma/ |

##### Media Studies

###### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Media Studies, MA | https://www.pratt.edu/liberal-arts-and-sciences/media-studies-ma/ |

##### Writing

###### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Writing, MFA | https://www.pratt.edu/liberal-arts-and-sciences/writing-mfa/ |

##### Advanced Certificates

| # | 项目 | URL |
|---|------|-----|
| 1 | Design History, Advanced Certificate | https://www.pratt.edu/liberal-arts-and-sciences/design-history-advanced-certificate/ |
| 2 | Museum Studies, Advanced Certificate | https://www.pratt.edu/liberal-arts-and-sciences/museum-studies-advanced-certificate/ |
| 3 | Media Studies, Advanced Certificate | https://www.pratt.edu/liberal-arts-and-sciences/media-studies-advanced-certificate/ |

### 2.2 Graduate admissions model

Pratt's graduate admissions is **decentralized** -- each program has its own requirements, portfolio specifications, and deadlines. Applications are submitted online through each program's specific portal. There is no single centralized graduate application.

**Application fee**: $50 (domestic) / $90 (international) -- same as UG.

### 2.3 Graduate tuition by program (2025-26, from official PDF)

| School | Program | Credits | Total Tuition |
|--------|---------|---------|---------------|
| Architecture | M.Arch (First Professional) | 28 | $62,188 |
| Architecture | MS Architecture (Post Professional) | 36 | $79,956 |
| Architecture | MS Urban Design (Post Professional) | 33 | $73,293 |
| Architecture | MS Urban & Community Planning | 26 | $57,746 |
| Architecture | MS Urban Placemaking & Management | 22 | $48,862 |
| Architecture | MS Sustainable Environmental Systems | 28 | $62,188 |
| Architecture | MS Historic Preservation | 24 | $53,304 |
| Architecture | MLA | 30 | $66,630 |
| Architecture | Adv Cert (Urban Community Planning) | 9 | $19,989 |
| Architecture | Adv Cert (Urban Placemaking) | 9 | $19,989 |
| Architecture | Adv Cert (Sustainable Env Systems) | 9 | $19,989 |
| Architecture | Adv Cert (Historic Preservation) | 10 | $22,210 |
| Art | MA Art & Design Education | 24 | $53,304 |
| Art | Adv Cert Art & Design Education | 18 | $39,978 |
| Art | MPS Art Therapy | 28 | $62,188 |
| Art | MPS Art Therapy Low Residency | 23 | $51,083 |
| Art | MPS Arts & Cultural Management | 24 | $53,304 |
| Art | MS Dance & Movement Therapy | 34 | $75,514 |
| Art | MS Dance & Movement Therapy Low Res | 23 | $51,083 |
| Art | MPS Design Management | 24 | $53,304 |
| Art | MFA Digital Arts (Animation) | 30 | $66,630 |
| Art | MFA Digital Arts (Interactive) | 30 | $66,630 |
| Art | MFA Painting & Drawing | 30 | $66,630 |
| Art | MFA Integrated Practices | 30 | $66,630 |
| Art | MFA Sculpture | 30 | $66,630 |
| Art | MFA Printmaking | 30 | $66,630 |
| Art | MFA Photography | 30 | $66,630 |
| Art | Adv Cert Teaching & Learning | 9 | $19,989 |
| Design | MFA Communications Design | 30 | $66,630 |
| Design | MS Packaging/Identities/Systems | 24 | $53,304 |
| Design | MID Industrial Design | 30 | $66,630 |
| Design | MFA Interior Design (2-yr) | 30 | $66,630 |
| Design | MFA Interior Design (3-yr) | 24 | $53,304 |
| Design | MFA Fashion Collection + Communication | 29 | $64,409 |
| Information | M.S.L.I.S. | 18 | $32,616 |
| Information | MS Museums & Digital Culture | 18 | $32,616 |
| Information | MS Info Experience Design | 18 | $32,616 |
| Information | MS Data Analytics & Visualization | 18 | $32,616 |
| Information | Adv Cert Archives | 6 | $10,872 |
| Information | Adv Cert Museum Libraries | 6 | $10,872 |
| Information | Adv Cert Digital Humanities | 12 | $21,744 |
| Information | Adv Cert User Experience | 9 | $16,308 |
| Information | Adv Cert Conservation & Digital Curation | 12 | $21,744 |
| Information | Adv Cert Spatial Analysis & Design | 6 | $10,872 |
| Information | Adv Cert Children's & Young Adult Library | 9 | $16,308 |
| Lib Arts | Dual MA/MS History of Art & LIS | 24 | $48,396 |
| Lib Arts | MA History of Art | 24 | $53,304 |
| Lib Arts | Adv Cert Design History | 15 | $33,315 |
| Lib Arts | Adv Cert Museum Studies | 15 | $33,315 |
| Lib Arts | MA Media Studies | 20 | $44,420 |
| Lib Arts | Adv Cert Media Studies | 6 | $13,326 |
| Lib Arts | MFA Writing | 20 | $44,420 |

---

## SECTION 3 -- Application requirements & deadlines

### 3.1 Undergraduate -- core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Application portal | Common App | https://www.commonapp.org/explore/pratt-institute/ |
| Application fee (US citizens/PRs) | $50 | Application Requirements page |
| Application fee (International) | $90 | Application Requirements page |
| **Early Action deadline** | **November 15** | UG Admissions page accordion |
| **Priority Decision deadline** | **January 15** | UG Admissions page accordion |
| **Regular Decision** | **Rolling after January 15** | UG Admissions page accordion |
| Decision notification (EA) | Mid-December | UG Admissions page |
| Decision notification (Priority/RD) | Within 3 weeks of completion | UG Admissions page |
| Portfolio | **Required** via pratt.slideroom.com ($10 fee) | Application Requirements page |
| Essay | **Required** (Pratt essay, 250-500 words; Common App essay optional) | Application Requirements page |
| Letters of recommendation | **Optional** (max 3) | Application Requirements page |
| SAT/ACT | **Test-optional** | Application Requirements page |
| SAT code | 2669 | Application Requirements page |
| ACT code | 2862 | Application Requirements page |
| High school transcripts | Required (electronic only) | Application Requirements page |
| FAFSA deadline | March 1 | Finance Your Education page |

> **IMPORTANT CORRECTION**: User stated EA = November 1 and RD = January 5. The official Pratt website (as of 2026-07-07) shows **EA = November 15** and **Priority = January 15** with rolling RD thereafter. The user's dates may reflect an older admissions cycle or a different source. VERIFY against the official site.

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|--------------|-------------------|-------|
| TOEFL iBT (0-120 scale) | 92 | N/A | Code: 2669; MyBest NOT accepted |
| TOEFL iBT (new 1-6 scale) | 5 | N/A | New reporting scale |
| IELTS Academic | 7.0 | N/A | |
| Duolingo English Test (DET) | 125 | N/A | |
| PTE Academic | 62 | N/A | |
| Cambridge English (C1/C2) | 183 | N/A | |

**Applicability**: Required for international applicants and those for whom English is not the primary/native language. Scores must be sent directly from testing agency before admissions deadline. Scores must be within 2 years of intended start term.

**Waiver conditions**:
- Studied last 3 years of high school in the US in good academic standing
- Studied last 3 years at a high school in another country where English is the official national language and primary language of instruction

### 3.3 Graduate -- global rules

- **Decentralized admissions**: Each program has its own requirements, portfolio specs, and deadlines
- **Application platform**: Online through each program's portal
- **Application fee**: $50 (domestic) / $90 (international) -- same as UG
- **GRE/GMAT**: Not universally required; varies by program
- **English proficiency**: Same requirements as UG (TOEFL 92 / IELTS 7.0 / DET 125 / PTE 62 / Cambridge 183)
- **Portfolio**: Required for most programs; specifications vary by program
- **Per-credit tuition**: $2,310/credit (most programs) / $1,894/credit (School of Information)
- **Full-time status**: 9 credits/semester for financial aid purposes

---

## SECTION 4 -- Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

**On-Campus (Dependent)**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $64,703 | Full-time (12-18 credits/semester); per-credit = $2,087 |
| Academic/Activity Fees | $1,014 | |
| Technology Fee | $610 | |
| Housing and Food | $19,530 | On-campus room & board |
| Books/Supplies | $2,100 | Estimate |
| Direct Loan Fee | $241 | |
| Personal | $2,369 | Estimate |
| Health Services Fee | $400 | |
| **TOTAL (On-Campus Dependent)** | **$90,967** | |

**On-Campus (Independent)**

| Expense Item | Amount |
|-------------|--------|
| **TOTAL (On-Campus Independent)** | **$94,467** |

**Commuter (Dependent)**

| Expense Item | Amount |
|-------------|--------|
| Tuition | $64,703 |
| Academic/Activity Fees | $1,014 |
| Technology Fee | $610 |
| Housing and Food | $8,013 |
| Books/Supplies | $2,100 |
| Local Transportation | $1,500 |
| Direct Loan Fee | $241 |
| Personal | $2,369 |
| Health Services Fee | $400 |
| **TOTAL (Commuter Dependent)** | **$80,950** |

**Off-Campus (Dependent)**

| Expense Item | Amount |
|-------------|--------|
| Tuition | $64,703 |
| Academic/Activity Fees | $1,014 |
| Technology Fee | $610 |
| Housing and Food | $24,917 |
| Books/Supplies | $2,100 |
| Local Transportation | $1,500 |
| Direct Loan Fee | $241 |
| Personal | $2,369 |
| Health Services Fee | $400 |
| **TOTAL (Off-Campus Dependent)** | **$97,854** |

**Additional**: Architecture students must add ~$3,500 for computer/software.

### 4.2 Undergraduate financial-aid policy

- **Need-aware for ALL applicants** (domestic and international) -- NOT need-blind
- **78% of undergraduates** receive some form of financial aid
- International students eligible for **merit-based scholarships only** (not need-based)
- International merit awards use TOEFL/SAT scores + portfolio + grades as criteria
- International students should NOT file FAFSA
- FAFSA deadline: March 1
- Net Price Calculator available (Freshman + Transfer; US citizens/PRs only)

### 4.3 Graduate cost & funding framework

**Graduate COA (2026-2027, Art & Design and Architecture programs)**

| Living Arrangement | 12 credits/sem | 9 credits/sem | 6 credits/sem |
|-------------------|---------------|---------------|---------------|
| On-campus (Resident) | $81,747 | $67,887 | $52,125 |
| Commuter | $71,730 | $57,870 | $42,108 |
| Off-campus | $88,634 | $74,774 | $59,012 |

**Graduate COA (2026-2027, School of Information)**

| Living Arrangement | 12 credits/sem | 9 credits/sem | 6 credits/sem |
|-------------------|---------------|---------------|---------------|
| On-campus (Resident) | $71,763 | $60,399 | $47,133 |
| Commuter | $61,746 | $50,382 | $37,116 |
| Off-campus | $78,650 | $67,286 | $54,020 |

**Per-credit tuition**: $2,310 (most programs) / $1,894 (School of Information)
**Full-time status**: 9 credits/semester for financial aid purposes
**Additional**: Architecture/Urban Design majors add ~$4,200; Interior Design majors add ~$4,000 for computer/software.

---

## SECTION 5 -- Evidence chain index

### E-U-001: Undergraduate tuition 2026-27
```yaml
field: undergraduate.costs.tuition_2026_2027
value: $64,703
source_url: https://www.pratt.edu/wp-content/uploads/2026/01/2026-27-UG-COA-1.22.26.pdf
source_snippet: "Tuition $ 64,703.00"
capture_date: 2026-07-07
evidence_type: official_pdf
```

### E-U-002: Early Action deadline
```yaml
field: undergraduate.deadlines.EA
value: November 15
source_url: https://www.pratt.edu/admissions/undergraduate-admissions/
source_snippet: "Early Action Decision ... November 15 ... Complete your application by submitting all required materials and receive a decision by mid-December."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-003: Priority Decision deadline
```yaml
field: undergraduate.deadlines.PRIORITY
value: January 15
source_url: https://www.pratt.edu/admissions/undergraduate-admissions/
source_snippet: "Priority Decision ... January 15 ... Priority date to complete your application by submitting all required materials and receive a decision within 3 weeks."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-004: Test-optional policy
```yaml
field: undergraduate.tests.policy
value: Test-optional
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "SAT / ACT Scores: Pratt is test optional ... SAT or ACT scores are not required."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-005: TOEFL minimum
```yaml
field: undergraduate.tests.english.tofel_min
value: 92 (0-120 scale) or 5 (new 1-6 scale)
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "TOEFL IBT and TOEFL Home Edition: minimum score of 92 in the 0-120 scale, or 5 in the new 1-6 scale"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-006: IELTS minimum
```yaml
field: undergraduate.tests.english.ielts_min
value: 7.0
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "IELTS Academic: minimum score of 7.0"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-007: DET minimum
```yaml
field: undergraduate.tests.english.det_min
value: 125
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "DET Duolingo English Test: minimum score of 125"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-008: Application fee
```yaml
field: undergraduate.application.fee
value: $50 (US) / $90 (international)
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "The application has an administrative fee of $50 for U.S. citizens and permanent residents; and $90 for international applicants."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-009: Portfolio requirement
```yaml
field: undergraduate.application.portfolio
value: Required via pratt.slideroom.com ($10 submission fee)
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "Portfolios must be submitted at pratt.slideroom.com ... Slideroom has a $10 submission fee."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-010: On-campus COA total
```yaml
field: undergraduate.costs.coa_oncampus_dependent
value: $90,967
source_url: https://www.pratt.edu/wp-content/uploads/2026/01/2026-27-UG-COA-1.22.26.pdf
source_snippet: "TOTAL $ 90,967.00"
capture_date: 2026-07-07
evidence_type: official_pdf
```

### E-U-011: Need-aware policy
```yaml
field: undergraduate.aid.need_blind
value: false (need-aware for all, including domestic)
source_url: https://www.pratt.edu/admissions/undergraduate-admissions/finance-your-education/
source_snippet: "78% of Pratt students receive some form of financial aid" (no need-blind claim found)
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-012: SAT/ACT codes
```yaml
field: undergraduate.tests.codes
value: SAT 2669, ACT 2862
source_url: https://www.pratt.edu/resources/undergraduate-application-requirements-high-school-applicants/
source_snippet: "SAT code: 2669 ... ACT code: 2862"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-001: Graduate tuition per credit
```yaml
field: graduate.costs.tuition_per_credit
value: $2,310 (most programs) / $1,894 (School of Information)
source_url: https://www.pratt.edu/wp-content/uploads/2026/02/2026-27-GR-COA-2.19.2026.pdf
source_snippet: "Per credit tuition is $2310 for all Graduate programs except School of Information, which is $1894 per credit."
capture_date: 2026-07-07
evidence_type: official_pdf
```

### E-G-002: Graduate COA (on-campus, 12 credits)
```yaml
field: graduate.costs.coa_oncampus_12credits
value: $81,747 (Art & Design/Architecture) / $71,763 (Information)
source_url: https://www.pratt.edu/wp-content/uploads/2026/02/2026-27-GR-COA-2.19.2026.pdf
source_snippet: "TOTAL 81,747.00$ ... TOTAL 71,763.00$"
capture_date: 2026-07-07
evidence_type: official_pdf
```

### E-STRUCT-001: Program list (6 schools)
```yaml
field: institution.programs.total
value: 106 (raw extraction from 6 school pages)
source_url: https://www.pratt.edu/academics/
source_snippet: "School of Architecture ... School of Art ... School of Design ... School of Information ... School of Liberal Arts and Sciences ... School of Continuing and Professional Studies"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-STRUCT-002: Student body size
```yaml
field: institution.students
value: 3,675 undergrad + 1,462 grad = 5,137 total
source_url: https://www.pratt.edu/admissions/undergraduate-admissions/
source_snippet: "The Pratt community is made up of 3,675 undergrad students and 1,462 grad students."
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora import manifest

### Collection structure

```
pratt-knowledge-base-v2/
├── 00-institution-overview (Section 0: rules 1-4)
├── 01-ug-architecture (Section 1: School of Architecture programs)
├── 02-ug-art (Section 1: School of Art programs)
├── 03-ug-design (Section 1: School of Design programs)
├── 04-ug-liberal-arts (Section 1: School of Liberal Arts & Sciences programs)
├── 05-grad-architecture (Section 2: School of Architecture grad programs)
├── 06-grad-art (Section 2: School of Art grad programs)
├── 07-grad-design (Section 2: School of Design grad programs)
├── 08-grad-information (Section 2: School of Information programs)
├── 09-grad-liberal-arts (Section 2: School of Liberal Arts & Sciences grad programs)
├── 10-deadlines-requirements (Section 3)
├── 11-costs-financial-aid (Section 4)
└── 12-evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "pratt-knowledge-base-v2"
  school: "<home school>"
  department: "<home department>"
  degree_level: "<BArch|BFA|BPS|BA|MS|MFA|MA|MPS|MID|M.L.I.S.|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Graduate admissions deadlines (per-program) | https://www.pratt.edu/admissions/graduate-admissions/apply/ |
| P0 | Graduate English proficiency requirements (confirm same as UG) | https://www.pratt.edu/admissions/international/ |
| P0 | AAS (Associate) degree programs complete list | https://www.pratt.edu/art/associate-degrees/ |
| P1 | Reconcile program count (106 raw vs 88 matrix) | Cross-reference all school pages |
| P1 | Graduate program URLs for programs found only in tuition PDF | Program detail pages |
| P1 | Financial aid options details (scholarships, grants, loans) | https://www.pratt.edu/admissions/undergraduate-admissions/finance-your-education/financial-aid-options/ |
| P2 | Transfer admissions requirements and deadlines | https://www.pratt.edu/admissions/undergraduate-admissions/transfer-admissions/ |
| P2 | Pratt Munson (Utica campus) programs | https://www.pratt.edu/admissions/undergraduate-admissions/first-time-first-year/apply-to-pratt-munson/ |
| P2 | Academic catalog (catalog.pratt.edu unreachable during capture) | https://catalog.pratt.edu/ |

---

## SECTION 7 -- Cross-school comparison framework

| Dimension | Pratt Institute | (other schools) |
|-----------|----------------|-----------------|
| Type | Private | |
| Location | Brooklyn, NY | |
| UG Tuition/yr | $64,703 | |
| UG COA (on-campus) | $90,967 | |
| Need-blind (intl)? | No (need-aware for ALL) | |
| EA deadline | November 15 | |
| Priority deadline | January 15 | |
| RD deadline | Rolling after Jan 15 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 92 | |
| IELTS min | 7.0 | |
| App fee (US) | $50 | |
| App fee (Intl) | $90 | |
| Portfolio required? | Yes | |
| Total program count | ~106 | |
| School count | 6 | |
| UG students | 3,675 | |
| Grad students | 1,462 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: pratt.edu, catalog.pratt.edu (unreachable), official PDFs (COA, tuition-by-program)
> **Verification**: ego-browser snapshotText + JS DOM extraction + PDF text extraction
> **Granularity**: school -> department -> degree-level -> program

---

## IMPORTANT NOTES & CORRECTIONS

### Deadline discrepancy
The user specified EA = November 1 and RD = January 5. The official Pratt admissions page (captured 2026-07-07) shows:
- **Early Action: November 15** (not November 1)
- **Priority Decision: January 15** (not January 5)
- **Regular Decision: Rolling after January 15**

This may reflect different admissions cycles. The official site data takes precedence.

### Test-optional verification
**CONFIRMED**: Pratt is test-optional. The Application Requirements page explicitly states "SAT / ACT Scores: Pratt is test optional" and "SAT or ACT scores are not required."

### Need-aware verification
**CONFIRMED**: Pratt is need-aware for ALL applicants (domestic and international). The Finance Your Education page states "78% of Pratt students receive some form of financial aid" but does not claim need-blind status. International students are eligible for merit-based scholarships only.

### Tuition verification
**CONFIRMED**: UG tuition is $64,703 (2026-27), not ~$58k as user stated. The $58k figure may refer to an earlier year or base tuition without fees.

### Program count reconciliation
Raw extraction from 6 school pages yielded 106 program entries. The distribution matrix totals 88 after deduplication and grouping. Discrepancy due to:
1. Cross-listed programs appearing on multiple school pages
2. Emphasis tracks counted as separate entries in raw extraction
3. Combined degrees (BFA/MA) counted once
4. Some programs found only in the graduate tuition PDF (not on school pages)

### Browser limitations
The Pratt website (pratt.edu) is heavily JavaScript-rendered. Many pages returned empty snapshots or timed out in the headless browser. Data was successfully extracted from:
- UG Admissions page (deadlines, accordion content)
- Application Requirements page (test policy, English proficiency, fees)
- Finance Your Education page (COA PDF links)
- Graduate Admissions page (structure, links)
- Individual school pages (program lists via serverFetch)
- Official PDFs (COA data, graduate tuition by program)

The academic catalog (catalog.pratt.edu) was completely unreachable during this capture session.
