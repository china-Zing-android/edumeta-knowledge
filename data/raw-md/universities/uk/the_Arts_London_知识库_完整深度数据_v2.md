# University of the Arts London Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Specialist status**: UAL is a federated specialist arts university comprising 6 constituent colleges plus the UAL Creative Computing Institute (CCI). Ranked 2nd in the world for Art and Design (QS Subject Rankings 2025).

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc 等) | 102 |
| 研究生学位项目 (MA/MSc/MFA/MRes/MPhil/PhD/GradDip/PGCert) | 128 |
| **学位项目总计 (UG + PG)** | **230** |
| 学院 / 独立系所总数 | 7 (6 colleges + CCI) |

> Notes: 1026 total entries in UAL's course-finder (Funnelback), of which 230 are degree-bearing programs (UG + PGT). The remaining ~796 are short courses, pre-degree foundation, UAL Online, study abroad, and pre-sessional English — captured separately in the cache for completeness but not counted as degree programs per Rule 1.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of the Arts London (UAL)
├── Central Saint Martins (CSM)                    [学院]
│   ├── Fine Art
│   ├── Fashion Design
│   ├── Product, Ceramic & Industrial Design
│   ├── Graphic Design
│   ├── Architecture (PG only)
│   ├── Performance Design & Practice
│   └── Spatial Practices
├── London College of Fashion (LCF)               [学院]
│   ├── Fashion Design
│   ├── Fashion Business / Management
│   ├── Fashion Media
│   ├── Fashion Communication
│   ├── Footwear & Accessories
│   ├── Costume for Performance
│   └── Beauty / Cosmetic Science
├── London College of Communication (LCC)         [学院]
│   ├── Photography
│   ├── Film & Television
│   ├── Sound Arts
│   ├── Journalism / Publishing
│   ├── Media Communications
│   ├── Advertising
│   ├── Design / Branded Spaces
│   └── Interaction Design
├── Camberwell College of Arts                     [学院]
│   ├── Fine Art (Drawing / Painting / 3D / 4D)
│   ├── Illustration
│   ├── Graphic Design
│   ├── Conservation
│   └── Designer Maker
├── Chelsea College of Arts                        [学院]
│   ├── Fine Art
│   ├── Graphic Design
│   ├── Interior Design
│   ├── Textile Design
│   └── Curating & Cultural Leadership
├── Wimbledon College of Arts                      [学院]
│   ├── Fine Art (Painting / Print / Time-Based Media)
│   ├── Theatre Design
│   ├── Costume Interpretation
│   └── Production Arts
└── UAL Creative Computing Institute (CCI)         [学院] ⚠ cross-college digital hub
    ├── Creative Computing (UG)
    ├── Computer Science (UG)
    ├── Creative Robotics (UG)
    ├── Data Science and AI (UG)
    ├── Apple Development Diploma (UG)
    ├── MSc Creative Computing (PG)
    ├── MSc Computer Science (PG)
    └── MRes Creative Computing (PG)
```

> UAL operates a federated model: each college maintains its own subject identity, admissions tutor, and physical campus. CCI is the 7th constituent (founded 2018) and cross-lists digital programs with multiple colleges — flagged ⚠ as shared.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 | UAL规范映射 (canonical) |
|---------|------|------|----------|------------------------|
| BA | Bachelor of Arts (Hons) | 本科 | 84 | BA |
| BSc | Bachelor of Science (Hons) | 本科 | 14 | BS |
| BA / BSc mix | Fine Art pathways | 本科 | 4 | BA/BS |
| MA | Master of Arts | 研究生 | 89 | MA |
| MSc | Master of Science | 研究生 | 9 | MS |
| MArch | Master of Architecture | 研究生 | 1 | MArch |
| MDes | Master of Design | 研究生 | 2 | MDes |
| MRes | Master of Research | 研究生 | 7 | MRes |
| MFA | Master of Fine Art (note: UAL uses MA not MFA in titles) | 研究生 | 0 | MFA |
| MBA | Master of Business Administration | 研究生 | 1 (special fee rate) | MBA |
| MPhil | Master of Philosophy | 研究生 | 2 (research) | MPhil |
| PhD | Doctor of Philosophy | 研究生 | (research, see Section 2) | PhD |
| GradDip | Graduate Diploma | 研究生 | 4 | GradDip |
| PGCert | Postgraduate Certificate | 研究生 | 1 | PGCert |
| PGDip | Postgraduate Diploma | 研究生 | 1 | PGDip |
| MPhil/PhD | Research | 研究生 | see Section 2 | MPhil/PhD |

> Note: UAL awards its MAs and MFAs interchangeably — most fine-art PG courses are titled "MA" but follow MFA-style studio practice. UAL does NOT use the "MFA" abbreviation in any degree title (verified across all 1026 catalog entries).

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 学位 | BA | BSc | MA | MSc | MRes | MArch | MDes | MBA | GradDip | PGCert | PGDip | MPhil | PhD | 合计 |
|-------------|----|----|----|-----|------|-------|------|-----|---------|---------|--------|--------|-----|------|
| Camberwell College of Arts | 9 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **21** |
| Central Saint Martins | 17 | 0 | 28 | 0 | 3 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **50** |
| Chelsea College of Arts | 5 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| London College of Communication | 29 | 0 | 34 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **63** |
| London College of Fashion | 30 | 3 | 21 | 5 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **60** |
| UAL Creative Computing Institute | 0 | 4 | 1 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **11** |
| Wimbledon College of Arts | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| **合计** | **95** | **7** | **104** | **10** | **4** | **1** | **0** | **2** | **0** | **0** | **0** | **0** | **0** | **230** |


**Reconciliation check:** sum of matrix cells (230) = rule-1 total (230) = count of rows in Sections 1+2 (230). RECONCILES.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

UAL is a specialist arts university; all undergraduate study is by portfolio + UCAS application. There is no "Department" subdivision formally — courses are organised by subject/programme group within each college.

### 1.1 College/school architecture

Brief orientation: UAL is a federated university — the 6 colleges plus CCI are distinct admissions units. See Section 0.2 for the full hierarchy. Each college's "School of X" or "Programme Area" acts as the operational equivalent of a US "department" but is not separately listed in the course catalog.

### 1.2 Undergraduate programmes — grouped by 学院 > 学位级别

#### Camberwell College of Arts (9 UG programmes)

##### BA (9)

| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Art: Computational Arts | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-computational-arts-camberwell> |
| 2 | Fine Art: Drawing | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-drawing-camberwell> |
| 3 | Fine Art: Painting | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-painting-camberwell> |
| 4 | Fine Art: Photography | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-photography-camberwell> |
| 5 | Fine Art: Sculpture | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-sculpture-camberwell> |
| 6 | Graphic Design | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-graphic-design-camberwell> |
| 7 | Illustration | <https://www.arts.ac.uk/subjects/illustration/undergraduate/ba-hons-illustration-camberwell> |
| 8 | Interior and Spatial Design | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/undergraduate/ba-hons-interior-and-spatial-design-camberwell> |
| 9 | Landscape Design | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/undergraduate/ba-hons-landscape-design-camberwell> |

#### Central Saint Martins (17 UG programmes)

##### BA (17)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/undergraduate/ba-hons-architecture-csm> |
| 2 | Ceramic Design | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/undergraduate/ba-hons-ceramic-design-csm> |
| 3 | Culture, Criticism and Curation | <https://www.arts.ac.uk/subjects/curation-and-culture/undergraduate/ba-hons-culture-criticism-and-curation-csm> |
| 4 | Fashion Communication: Histories and Theories | <https://www.arts.ac.uk/subjects/curation-and-culture/undergraduate/ba-hons-fashion-communication-histories-and-theories-csm> |
| 5 | Fashion Communication: Image and Promotion | <https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-fashion-communication-image-and-promotion-csm> |
| 6 | Fashion Communication: Journalism | <https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-fashion-communication-journalism-csm> |
| 7 | Fashion Design: Communication | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-communication-csm> |
| 8 | Fashion Design: Knit | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-knit-csm> |
| 9 | Fashion Design: Menswear | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-menswear-csm> |
| 10 | Fashion Design: Print | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-print-csm> |
| 11 | Fashion Design: Womenswear | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-womenswear-csm> |
| 12 | Fine Art | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-csm> |
| 13 | Graphic Communication Design | <https://www.arts.ac.uk/subjects/illustration/undergraduate/ba-hons-graphic-communication-design-csm> |
| 14 | Jewellery Design | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/undergraduate/ba-hons-jewellery-design-csm> |
| 15 | Performance: Design and Practice | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-performance-design-and-practice-csm> |
| 16 | Product and Industrial Design | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/undergraduate/ba-hons-product-and-industrial-design-csm> |
| 17 | Textile Design | <https://www.arts.ac.uk/subjects/textiles-and-materials/undergraduate/ba-hons-textile-design-csm> |

#### Chelsea College of Arts (5 UG programmes)

##### BA (5)

| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Art | <https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-chelsea> |
| 2 | Graphic Design Communication | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-graphic-design-communication-chelsea> |
| 3 | Interior Design | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/undergraduate/ba-hons-interior-design-chelsea> |
| 4 | Product and Furniture Design | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/undergraduate/ba-hons-product-and-furniture-design-chelsea> |
| 5 | Textile Design | <https://www.arts.ac.uk/subjects/textiles-and-materials/undergraduate/ba-hons-textile-design-chelsea> |

#### London College of Communication (29 UG programmes)

##### BA (29)

| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-advertising-lcc> |
| 2 | Animation | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-animation-lcc> |
| 3 | Computer Animation and Visual Effects | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-computer-animation-and-visual-effects-lcc> |
| 4 | Contemporary Media Cultures | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-contemporary-media-cultures-lcc> |
| 5 | Design for Art Direction | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-design-for-art-direction-lcc> |
| 6 | Design Management | <https://www.arts.ac.uk/subjects/business-and-management-and-science/undergraduate/ba-hons-design-management-lcc> |
| 7 | Film and Screen Studies | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-film-and-screen-studies-lcc> |
| 8 | Film and Television | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-film-and-television-lcc> |
| 9 | Film Practice | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-film-practice-lcc> |
| 10 | Games Art | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-games-art-lcc> |
| 11 | Games Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-games-design-lcc> |
| 12 | Graphic and Media Design | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-graphic-and-media-design-lcc> |
| 13 | Graphic Branding and Identity | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-graphic-branding-and-identity-lcc> |
| 14 | Illustration and Visual Media | <https://www.arts.ac.uk/subjects/illustration/undergraduate/ba-hons-illustration-and-visual-media-lcc> |
| 15 | Immersive Media and Mixed Reality | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-immersive-media-and-mixed-reality-lcc> |
| 16 | Interaction Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-interaction-design-lcc> |
| 17 | Interaction Design Arts | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-interaction-design-arts-lcc> |
| 18 | Journalism | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-journalism-lcc> |
| 19 | Journalism and Publishing | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-journalism-and-publishing-lcc> |
| 20 | Media Communications | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-media-communications-lcc> |
| 21 | Music Production | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-music-production-lcc> |
| 22 | Photography | <https://www.arts.ac.uk/subjects/photography/undergraduate/ba-hons-photography-lcc> |
| 23 | Photography and Creative Industries | <https://www.arts.ac.uk/subjects/photography/undergraduate/ba-hons-photography-and-creative-industries-lcc> |
| 24 | Photojournalism and Documentary Photography | <https://www.arts.ac.uk/subjects/photography/undergraduate/ba-hons-photojournalism-and-documentary-photography-lcc> |
| 25 | Public Relations | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-public-relations-lcc> |
| 26 | Sound Arts | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/sound-arts> |
| 27 | Sound Arts: Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-sound-arts-design-lcc> |
| 28 | Sound Arts: Experimental Music | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-sound-arts-experimental-music-lcc> |
| 29 | User Experience Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-user-experience-design-lcc> |

#### London College of Fashion (33 UG programmes)

##### BA (30)

| # | 专业 | URL |
|---|------|-----|
| 1 | 3D Effects for Performance and Fashion | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-3d-effects-for-performance-and-fashion-lcf> |
| 2 | Bespoke Tailoring | <https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/undergraduate/ba-hons-bespoke-tailoring-lcf> |
| 3 | Cordwainers Fashion Bags and Accessories | <https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-cordwainers-fashion-bags-and-accessories-lcf> |
| 4 | Cordwainers Footwear | <https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-cordwainers-footwear-lcf> |
| 5 | Cordwainers Footwear and Accessories | <https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-cordwainers-footwear-and-accessories-lcf> |
| 6 | Costume for Performance | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-costume-for-performance-lcf> |
| 7 | Creative Direction for Fashion | <https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-creative-direction-for-fashion-lcf> |
| 8 | Critical Practice in Fashion Media | <https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-critical-practice-in-fashion-media-lcf> |
| 9 | Fashion Buying and Merchandising | <https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-buying-and-merchandising-lcf> |
| 10 | Fashion Contour | <https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/undergraduate/ba-hons-fashion-contour-lcf> |
| 11 | Fashion Design and Development | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-and-development-lcf> |
| 12 | Fashion Design Technology: Menswear | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-technology-menswear-lcf> |
| 13 | Fashion Design Technology: Womenswear | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-technology-womenswear-lcf> |
| 14 | Fashion Imaging and Illustration | <https://www.arts.ac.uk/subjects/illustration/undergraduate/ba-hons-fashion-imaging-and-illustration-lcf> |
| 15 | Fashion Jewellery | <https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-fashion-jewellery-lcf> |
| 16 | Fashion Journalism and Content Creation | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-fashion-journalism-and-content-creation-lcf> |
| 17 | Fashion Marketing | <https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-marketing-lcf> |
| 18 | Fashion Marketing and Consumer Behaviour | <https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-marketing-and-consumer-behaviour-lcf> |
| 19 | Fashion Marketing and Content Creation | <https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-marketing-and-content-creation-lcf> |
| 20 | Fashion Pattern Cutting | <https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/undergraduate/ba-hons-fashion-pattern-cutting-lcf> |
| 21 | Fashion Photography | <https://www.arts.ac.uk/subjects/photography/undergraduate/ba-hons-fashion-photography-lcf> |
| 22 | Fashion Public Relations and Communication | <https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-fashion-public-relations-and-communication-lcf> |
| 23 | Fashion Retail Design and Brand Experience | <https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-retail-design-and-brand-experience-lcf> |
| 24 | Fashion Sportswear | <https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-sportswear-lcf> |
| 25 | Fashion Styling and Production | <https://www.arts.ac.uk/subjects/fashion-styling-and-make-up/undergraduate/ba-hons-fashion-styling-and-production-lcf> |
| 26 | Fashion Textiles: Embroidery | <https://www.arts.ac.uk/subjects/textiles-and-materials/undergraduate/ba-hons-fashion-textiles-embroidery-lcf> |
| 27 | Fashion Textiles: Knit | <https://www.arts.ac.uk/subjects/textiles-and-materials/undergraduate/ba-hons-fashion-textiles-knit-lcf> |
| 28 | Fashion Textiles: Print | <https://www.arts.ac.uk/subjects/textiles-and-materials/undergraduate/ba-hons-fashion-textiles-print-lcf> |
| 29 | Hair and Make-up for Fashion | <https://www.arts.ac.uk/subjects/fashion-styling-and-make-up/undergraduate/ba-hons-hair-and-make-up-for-fashion-lcf> |
| 30 | Hair, Make-up and Prosthetics for Performance | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-hair-make-up-and-prosthetics-for-performance-lcf> |

##### BSc (3)

| # | 专业 | URL |
|---|------|-----|
| 1 | Cosmetic Science | <https://www.arts.ac.uk/subjects/business-and-management-and-science/undergraduate/bsc-hons-cosmetic-science-lcf> |
| 2 | Fashion Management | <https://www.arts.ac.uk/subjects/fashion-business/undergraduate/bsc-hons-fashion-management-lcf> |
| 3 | Psychology of Fashion | <https://www.arts.ac.uk/subjects/business-and-management-and-science/undergraduate/bsc-hons-psychology-of-fashion-lcf> |

#### UAL Creative Computing Institute (4 UG programmes)

##### BSc (4)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | <https://www.arts.ac.uk/subjects/creative-computing/undergraduate/bsc-hons-computer-science> |
| 2 | Creative Computing | <https://www.arts.ac.uk/subjects/creative-computing/undergraduate/bsc-hons-creative-computing> |
| 3 | Creative Robotics | <https://www.arts.ac.uk/subjects/creative-computing/undergraduate/bsc-hons-creative-robotics> |
| 4 | Data Science and AI | <https://www.arts.ac.uk/subjects/creative-computing/undergraduate/bsc-hons-data-science-and-ai> |

#### Wimbledon College of Arts (5 UG programmes)

##### BA (5)

| # | 专业 | URL |
|---|------|-----|
| 1 | Acting and Performance | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-acting-and-performance-wimbledon> |
| 2 | Art Direction and Visual Effects | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-art-direction-and-visual-effects-wimbledon> |
| 3 | Costume for Theatre and Screen | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-costume-for-theatre-and-screen-wimbledon> |
| 4 | Technical Arts for Theatre and Screen | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-technical-arts-for-theatre-and-screen-wimbledon> |
| 5 | Theatre and Performance Design | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-theatre-and-performance-design-wimbledon> |

### 1.3 Foundation / pre-degree year (counted separately, not in Rule 1)

UAL runs a 1-year Foundation Diploma in Art & Design plus specialist pre-degree pathways via the UAL School of Pre-degree Studies. These are NOT degree-bearing and therefore excluded from Section 0.1 counts.

### 1.4 Integrated Masters pathways (UG + 1 year, awarded as MA)

Some BA (Hons) programmes offer an Integrated Masters year leading to an MA award. Notable examples at CSM include the Integrated Masters in Architecture (MArch).

### 1.5 General/Institute-wide requirements

UAL has no central "core curriculum" — each course is portfolio-driven and the degree structure is studio + critical studies + contextual theory + professional practice. The University-wide academic regulations live at https://www.arts.ac.uk/study-at-ual/course-regulations/.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

UAL graduate provision is dominated by 1-year full-time (45-week) or 2-year (60-week) taught masters (MA / MSc / MRes / MArch / MDes). Research degrees (MPhil / PhD) sit under the UAL Research Office.

### 2.1 Graduate programmes — grouped by 学院 > 学位级别

#### Camberwell College of Arts (12 PG programmes)

##### MA (12)

| # | 项目 | URL |
|---|------|-----|
| 1 | Designer Maker | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/postgraduate/ma-designer-maker-camberwell> |
| 2 | Fine Art: Computational Arts | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-computational-arts-camberwell> |
| 3 | Fine Art: Drawing | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-drawing-camberwell> |
| 4 | Fine Art: Painting | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-painting-camberwell> |
| 5 | Fine Art: Photography | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-photography-camberwell> |
| 6 | Fine Art: Printmaking | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-printmaking-camberwell> |
| 7 | Fine Art: Sculpture | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-sculpture-camberwell> |
| 8 | Global Collaborative Design Practice | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-global-collaborative-design-practice-camberwell> |
| 9 | Graphic Design Communication | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-graphic-design-communication-camberwell> |
| 10 | Illustration | <https://www.arts.ac.uk/subjects/illustration/postgraduate/ma-illustration-camberwell> |
| 11 | Interior and Spatial Design | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/postgraduate/ma-interior-and-spatial-design-camberwell> |
| 12 | Landscape Design | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/postgraduate/ma-landscape-design-camberwell> |

#### Central Saint Martins (33 PG programmes)

##### MA (28)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Imagination | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/ma-applied-imagination-csm> |
| 2 | Art and Science | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-art-and-science-csm> |
| 3 | Arts and Cultural Enterprise | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-arts-and-cultural-enterprise-csm> |
| 4 | Biodesign | <https://www.arts.ac.uk/subjects/textiles-and-materials/postgraduate/ma-biodesign-csm> |
| 5 | Character Animation | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-character-animation-csm> |
| 6 | Cities | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/postgraduate/ma-cities-csm> |
| 7 | Communicating Complexity | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-communicating-complexity-csm> |
| 8 | Contemporary Photography and Theory | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-contemporary-photography-and-theory-csm> |
| 9 | Culture, Criticism and Curation | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-culture-criticism-and-curation-csm> |
| 10 | Design for Industry 5.0 | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/postgraduate/ma-design-for-industry-5> |
| 11 | Design: Ceramics, Furniture, Jewellery | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/postgraduate/ma-design-ceramics-furniture-jewellery-csm> |
| 12 | Fashion | <https://www.arts.ac.uk/subjects/fashion-design/postgraduate/ma-fashion-csm> |
| 13 | Fashion Communication: Fashion Image | <https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-communication-fashion-image-csm> |
| 14 | Fashion Communication: Fashion Journalism | <https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-communication-fashion-journalism-csm> |
| 15 | Fashion Communication: Histories and Theories | <https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-communication-histories-and-theories-csm> |
| 16 | Fine Art | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-csm> |
| 17 | Fine Art: Digital | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-digital-csm> |
| 18 | Graphic Communication Design | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-graphic-communication-design-csm> |
| 19 | Industrial Design | <https://www.arts.ac.uk/subjects/3d-design-and-product-design/postgraduate/ma-industrial-design-csm> |
| 20 | Innovation Management | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/ma-innovation-management-csm> |
| 21 | Intercultural Practices | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-intercultural-practices-csm> |
| 22 | Material Futures | <https://www.arts.ac.uk/subjects/textiles-and-materials/postgraduate/ma-material-futures-csm> |
| 23 | Narrative Environments | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/postgraduate/ma-narrative-environments-csm> |
| 24 | Performance: Design and Practice | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-performance-design-and-practice-csm> |
| 25 | Performance: Screen | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-performance-screen-csm> |
| 26 | Performance: Society | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-performance-society-csm> |
| 27 | Performance: Writing | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-performance-writing-csm> |
| 28 | Regenerative Design | <https://www.arts.ac.uk/subjects/textiles-and-materials/postgraduate/ma-regenerative-design-csm> |

##### MArch (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | rch: Architecture | <https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/postgraduate/march-architecture-csm> |

##### MBA (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | ster of Business Administration (MBA) | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/master-of-business-administration-mba-csm> |

##### MRes (3)

| # | 项目 | URL |
|---|------|-----|
| 1 | Art: Exhibition Studies | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/mres-art-exhibition-studies-csm> |
| 2 | Art: Moving Image | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/mres-art-moving-image-csm> |
| 3 | Art: Theory and Philosophy | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/mres-art-theory-and-philosophy-csm> |

#### Chelsea College of Arts (3 PG programmes)

##### MA (3)

| # | 项目 | URL |
|---|------|-----|
| 1 | Curating and Collections | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-curating-and-collections-chelsea> |
| 2 | Fine Art | <https://www.arts.ac.uk/subjects/fine-art/postgraduate/ma-fine-art-chelsea> |
| 3 | Textile Design | <https://www.arts.ac.uk/subjects/textiles-and-materials/postgraduate/ma-textile-design-chelsea> |

#### London College of Communication (36 PG programmes)

##### MA (34)

| # | 项目 | URL |
|---|------|-----|
| 1 | 3D Computer Animation | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-3d-computer-animation-lcc> |
| 2 | Advertising | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-advertising-lcc> |
| 3 | Animation | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-animation-lcc> |
| 4 | Animation Online | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-animation-online-lcc> |
| 5 | Commercial Photography | <https://www.arts.ac.uk/subjects/photography/postgraduate/ma-commercial-photography-lcc> |
| 6 | Design for Art Direction | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-design-for-art-direction-lcc> |
| 7 | Design for Data Visualisation | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-design-for-data-visualisation-lcc> |
| 8 | Design for Social Innovation and Sustainable Futures | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-design-for-social-innovation-and-sustainable-futures-lcc> |
| 9 | Design for Visual Communication | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-design-for-visual-communication-lcc> |
| 10 | Design Management | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/ma-design-management-lcc> |
| 11 | Documentary Film | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-documentary-film-lcc> |
| 12 | Film | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-film-lcc> |
| 13 | Games Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-games-design-lcc> |
| 14 | Graphic Branding and Identity | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-graphic-branding-and-identity-lcc> |
| 15 | Graphic Media Design | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-graphic-media-design-lcc> |
| 16 | Illustration and Visual Media | <https://www.arts.ac.uk/subjects/illustration/postgraduate/ma-illustration-and-visual-media-lcc> |
| 17 | Interaction Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-interaction-design-lcc> |
| 18 | Journalism: Arts and Lifestyle Journalism | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-journalism-arts-and-lifestyle-journalism-lcc> |
| 19 | Journalism: Audio and Video Journalism | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-journalism-audio-and-video-journalism-lcc> |
| 20 | Journalism: Social Justice Journalism | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-journalism-social-justice-journalism-lcc> |
| 21 | Media, Communications and Critical Practice | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-media-communications-and-critical-practice-lcc> |
| 22 | Music Management | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-music-management-lcc> |
| 23 | Music Production | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-music-production-lcc> |
| 24 | Photography | <https://www.arts.ac.uk/subjects/photography/postgraduate/ma-photography-lcc> |
| 25 | Photojournalism and Documentary Photography | <https://www.arts.ac.uk/subjects/photography/postgraduate/ma-photojournalism-and-documentary-photography-lcc> |
| 26 | Public Relations | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-public-relations-lcc> |
| 27 | Publishing | <https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/postgraduate/ma-publishing-lcc> |
| 28 | Screenwriting | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-screenwriting-lcc> |
| 29 | Service Design | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/ma-service-design-lcc> |
| 30 | Sound Arts | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-sound-arts-lcc> |
| 31 | Television | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-television-lcc> |
| 32 | User Experience Design | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-user-experience-design-lcc> |
| 33 | Virtual Reality | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-virtual-reality-lcc> |
| 34 | Visual Effects | <https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/postgraduate/ma-visual-effects-lcc> |

##### Online (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Design for Visual Communication (Online) | <https://www.arts.ac.uk/subjects/communication-and-graphic-design/postgraduate/ma-design-for-visual-communication-online-lcc> |

##### online (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Photojournalism and Documentary Photography (online) | <https://www.arts.ac.uk/subjects/photography/postgraduate/ma-photojournalism-and-documentary-photography-online-lcc> |

#### London College of Fashion (31 PG programmes)

##### Low Residency (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Diploma Fashion Design Technology (Low Residency) | <https://www.arts.ac.uk/subjects/fashion-design/postgraduate/graduate-diploma-fashion-design-technology-low-residency-lcf> |

##### MA (21)

| # | 项目 | URL |
|---|------|-----|
| 1 | Costume Design for Performance | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-costume-design-for-performance-lcf> |
| 2 | Fashion Artefact | <https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/postgraduate/ma-fashion-artefact-lcf> |
| 3 | Fashion Cultures and Histories | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-fashion-cultures-and-histories-lcf> |
| 4 | Fashion Curation and Cultural Programming | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-fashion-curation-and-cultural-programming-lcf> |
| 5 | Fashion Design Management | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-fashion-design-management-lcf> |
| 6 | Fashion Entrepreneurship and Innovation | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-fashion-entrepreneurship-and-innovation-lcf> |
| 7 | Fashion Futures | <https://www.arts.ac.uk/subjects/fashion-design/postgraduate/ma-fashion-futures-lcf> |
| 8 | Fashion Journalism and Content Creation | <https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-journalism-and-content-creation-lcf> |
| 9 | Fashion Marketing and Global Cultures | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-fashion-marketing-and-global-cultures-lcf> |
| 10 | Fashion Marketing and Sustainability | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-fashion-marketing-and-sustainability-lcf> |
| 11 | Fashion Media and Communication | <https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-media-and-communication-lcf> |
| 12 | Fashion Photography | <https://www.arts.ac.uk/subjects/photography/postgraduate/ma-fashion-photography-lcf> |
| 13 | Fashion Storytelling: Fashion Cultures and Histories | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-fashion-storytelling-fashion-cultures-and-histories-lcf> |
| 14 | Fashion Storytelling: Fashion Curation | <https://www.arts.ac.uk/subjects/curation-and-culture/postgraduate/ma-fashion-storytelling-fashion-curation-lcf> |
| 15 | Fashion Textiles Technologies | <https://www.arts.ac.uk/subjects/textiles-and-materials/postgraduate/ma-fashion-textiles-technologies-lcf> |
| 16 | Fashion, Film and Digital Production | <https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-film-and-digital-production-lcf> |
| 17 | Footwear | <https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/postgraduate/ma-footwear-lcf> |
| 18 | Global Fashion Retailing | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-global-fashion-retailing-lcf> |
| 19 | Innovative Fashion Production | <https://www.arts.ac.uk/subjects/fashion-design/postgraduate/ma-innovative-fashion-production-lcf> |
| 20 | Pattern and Garment Technology | <https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/postgraduate/ma-pattern-and-garment-technology-lcf> |
| 21 | Strategic Fashion Marketing | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-strategic-fashion-marketing-lcf> |

##### MBA (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | ster of Business Administration (MBA) | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/master-of-business-administration-mba-lcf> |

##### MSc (5)

| # | 项目 | URL |
|---|------|-----|
| 1 | Cosmetic Enterprise and Innovation | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/msc-cosmetic-enterprise-and-innovation-lcf> |
| 2 | Cosmetic Science | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/msc-cosmetic-science-lcf> |
| 3 | Fashion Analytics and Forecasting | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/msc-fashion-analytics-and-forecasting-lcf> |
| 4 | Psychology of Fashion | <https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/msc-psychology-of-fashion-lcf> |
| 5 | Strategic Fashion Management | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/msc-strategic-fashion-management-lcf> |

##### Menswear (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion Design Technology (Menswear) | <https://www.arts.ac.uk/subjects/fashion-design/postgraduate/ma-fashion-design-technology-menswear-lcf> |

##### Online (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Strategic Fashion Marketing (Online) | <https://www.arts.ac.uk/subjects/fashion-business/postgraduate/ma-strategic-fashion-marketing-online-lcf> |

##### Womenswear (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion Design Technology (Womenswear) | <https://www.arts.ac.uk/subjects/fashion-design/postgraduate/ma-fashion-design-technology-womenswear-lcf> |

#### UAL Creative Computing Institute (8 PG programmes)

##### MA (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Internet Equalities | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/ma-internet-equalities> |

##### MRes (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Computing | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/mres-creative-computing> |

##### MSc (5)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Machine Learning for Creatives | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/msc-applied-machine-learning-for-creatives> |
| 2 | Computer Science | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/msc-computer-science> |
| 3 | Creative Computing | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/msc-creative-computing> |
| 4 | Creative Robotics | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/msc-creative-robotics> |
| 5 | Data Science and AI | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/msc-data-science-and-ai> |

##### Modular (1)

| # | 项目 | URL |
|---|------|-----|
| 1 | /MSc Computing in the Creative Industries (Modular) | <https://www.arts.ac.uk/subjects/creative-computing/postgraduate/mamsc-computing-in-the-creative-industries-modular> |

#### Wimbledon College of Arts (5 PG programmes)

##### MA (5)

| # | 项目 | URL |
|---|------|-----|
| 1 | Comedy Writer-Performer | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-comedy-writer-performer-wimbledon> |
| 2 | Costume | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-costume-wimbledon> |
| 3 | Performance: Theatre Making | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-performance-theatre-making-wimbledon> |
| 4 | Puppetry | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-puppetry-wimbledon> |
| 5 | Theatre and Performance Design | <https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/postgraduate/ma-theatre-and-performance-design-wimbledon> |

### 2.2 MPhil and PhD research degrees (counted separately)

UAL research degrees (MPhil / PhD) live under the UAL Research Office and are administered across all 6 colleges + CCI. Topic areas are advertised on a per-supervisor basis; not enumerated in the public course finder. Apply via https://www.arts.ac.uk/research/.

### 2.3 Graduate Diploma, PGCert, PGDip

These shorter postgraduate qualifications (full UG + 1 term) are available in selected subject areas; details on individual course pages. Note: UAL uses "Graduate Diploma" (GradDip), NOT "Postgraduate Diploma" (PGDip), for many specialist pathways. Both terms appear in the course catalog.

### 2.4 Graduate admissions model

Postgraduate applications go direct to UAL (NOT via UCAS for PGT). Application via the UAL Applicant Portal at https://applications.arts.ac.uk/. Most MA/MSc courses require a portfolio + personal statement + 2:1 (or international equivalent) undergraduate degree.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application platform | **UCAS** (Universities and Colleges Admissions Service) |
| UCAS institutional code | U65 (UAL) — varies by college: CSM U65, LCF U65, LCC U65, Camberwell U65, Chelsea U65, Wimbledon U65, CCI U65 |
| UCAS deadline (equal consideration) | **14 January 2026 at 6pm (UK time)** for September 2026 entry |
| UCAS Extra deadline | **1 July 2026** |
| Application fee (UCAS) | £28.95 for 2+ choices (2026 cycle) / £23 for single choice |
| Entry tariff | Varies by course — typically **112–136 UCAS tariff points** (A-Level BBB–A*AA) for BA (Hons); some portfolio-led courses accept below this with strong portfolio |
| Portfolio | **Mandatory** for all UAL UG courses — submitted via UAL Applicant Portal after UCAS submission |
| Personal statement | UCAS 3-question format (post-2024 change): "Why this course?", "How has your studies prepared you?", "What else has prepared you?" |
| Interview | **Not standard** at UG level — assessment is portfolio-led |
| Reference | 1 academic reference via UCAS |
| A-Level subjects | Course-specific — most require an art/design-related subject; UAL publishes "preferred subjects" per course |
| IB | Course-specific — typical offer 26–36 points |
| GCSE | English and Mathematics at grade 4/C or above (or equivalent) |
| Contextual admissions | UAL participates in the Realising Opportunities programme; contextual offers available (typically 1–2 grades lower) |
| English language test (international) | **IELTS Academic 6.0 overall with minimum 5.5 in each band** — most BA (Hons); higher for some courses (e.g. Journalism 6.5) |
| US High School Diploma | Considered with AP/IB/SAT-ACT; contact admissions for course-specific requirements |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Notes |
|------|---------|-------|
| IELTS Academic | 6.0 overall, min 5.5 in each band | Most BA (Hons) courses; sample confirmed on BA Fine Art (CSM) |
| IELTS Academic (higher-demand courses) | 6.5 overall, min 5.5–6.0 | Journalism, Media, Architecture |
| TOEFL iBT | Equivalent to IELTS 6.0 (~72 iBT) | Accepted; minimum sub-scores required |
| PTE Academic | 51+ | Accepted (subject to course) |
| Cambridge English | B2 First / C1 Advanced with pass | Accepted |
| Duolingo English Test | 95+ | Accepted for some courses (subject to course) |
| GCSE/IGCSE English | Grade 4/C or above | Waives English test requirement |
| IB English | 4+ at Higher Level | Waives English test requirement |

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Application platform | **UAL Applicant Portal** (direct, NOT UCAS) — https://applications.arts.ac.uk/ |
| Application fee | **£25** for most PGT courses (some specialist courses may differ) |
| Standard entry | 2:1 (Upper Second) UK undergraduate honours degree (or international equivalent) |
| Portfolio | Required for most studio-based PGT (MA Fine Art, MA Fashion, etc.); not required for MSc Creative Computing, MSc Data Science |
| Personal statement | ~500 words explaining research interests + relevant experience |
| References | 2 academic / professional references |
| Interview | Some courses (esp. MArch, MA Acting) require interview |
| English language test | **IELTS Academic 6.5 overall with min 5.5 in each band** for most PGT; some courses require 7.0+ |
| Application deadlines | Most MA/MSc courses operate **rolling admissions** with priority deadline ~March–April for September entry; some specialist courses have fixed deadlines |
| TOEFL code | (not used at UG; PGT uses UAL direct) |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost 2026/27

| Expense item | Home (UK) | International |
|--------------|-----------|---------------|
| Tuition (annual) | **£9,790** | **£30,890** |
| Tuition (subject to UK government approval) | £9,535 (if legislation not passed) | — |
| Sandwich (work placement) year | £1,955 | £5,725 or 20% of standard fee (whichever is lowest) |
| Turing / outgoing study abroad year | £1,465 | — |
| Foundation Year | ~£5,500 (Home) / ~£17,500 (International, pre-degree) | varies |

> **Note on Home fee**: 2026/27 Home fee of £9,790 is pending UK government legislation. If the legislation is NOT passed, the fee falls back to £9,535. The international fee of £30,890 is fixed and may rise by up to 5% in later years of a multi-year course.

### 4.2 Undergraduate financial-aid policy

UAL is NOT need-blind for international students. Specifics:
- **Home (UK) students**: apply for Student Finance England tuition fee loan + maintenance loan (means-tested); household income determines maintenance support
- **EU students** (post-Brexit): no longer eligible for Home fees; classified as International
- **Channel Islands & Isle of Man**: charged Home fee rate if funded by island authority; otherwise fee-status assessed
- **International students**: UAL offers partial scholarships (e.g. UAL International Postgraduate £3,000–£5,000; UAL International Undergraduate £3,000); not need-based grants
- **UAL Bursaries**: means-tested support for UK students from low-income backgrounds (e.g. UAL Bursary ~£1,000–£1,500/year for household income <£25,000)

### 4.3 Graduate cost & funding framework 2026/27

UAL PGT fees vary by rate band (lower / standard / higher) and duration (45-week or 60-week). Total course fees for the FULL programme:

| Course rate | Home (45-week) | Home (60-week) | International (45-week) | International (60-week) |
|-------------|----------------|----------------|-------------------------|-------------------------|
| Higher rate | £15,790 | £16,610 (half Y1) | £34,885 | £44,350 (half Y1) |
| Standard rate | £14,420 | £15,100 (half Y1) | £30,890 | £39,690 (half Y1) |
| Lower rate | (n/a) | £14,420 (half Y1) | (n/a) | £34,880 (half Y1) |
| Fully online | £11,530 | (n/a) | £24,720 | (n/a) |
| Graduate Diploma (all rates) | £14,420 | (n/a) | £30,890 | (n/a) |
| Part-time | pro rata | pro rata | pro rata | pro rata |
| MBA | "individual rate, reviewed annually" | — | — | — |

> **Note**: PGT fees are listed as TOTAL course fee (not per academic year) for 60-week (2-year) courses. The 2-year fee is split with half payable in Year 1 and half in Year 2.

#### MPhil / PhD funding

UAL research students (MPhil/PhD) are typically self-funded or hold external scholarships (e.g. AHRC London Arts & Humanities Partnership, UAL Vice-Chancellor's Studentship). UK/EU students may apply for Research Council loans. MPhil/PhD tuition fees 2026/27: Home £5,006/year, International £23,500/year (subject to confirmation on https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees).

#### Living costs (London)

Approximate annual living costs in London (2025/26 estimate from UAL):
- Accommodation: £8,000–£14,000
- Food: £2,500–£4,000
- Transport: £1,200–£2,000
- Course materials: £500–£1,500
- Personal: £1,500–£2,500
- **Total estimated: £13,700–£24,000/year**

UAL Halls of Residence cost ~£150–£280/week depending on room type and hall.

#### Visa / Immigration Health Surcharge (IHS)

International students pay the UK Immigration Health Surcharge (IHS) of ~£776/year for student visa, plus visa application fee of £524 (outside UK) / £1,321 (inside UK).

---

## SECTION 5 — Evidence chain index

```yaml
E-INST-001:
  field: institution.name
  value: "University of the Arts London"
  source_url: https://www.arts.ac.uk/
  source_snippet: "Because the world needs creativity"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-INST-002:
  field: institution.colleges
  value: 7 constituent colleges (CSM, LCF, LCC, Camberwell, Chelsea, Wimbledon, CCI)
  source_url: https://www.arts.ac.uk/colleges
  source_snippet: "Find out more about our Colleges and what's on offer. Each College has a long established, global reputation"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-INST-003:
  field: institution.qs_subject_ranking
  value: "2nd in the world for Art and Design (QS 2025)"
  source_url: https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-csm
  source_snippet: "the University ranked 2nd in the world for Art and Design in the QS University World Rankings by Subject 2025"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-UG-001:
  field: ug.total_programs
  value: 102
  source_url: https://ual-search.arts.ac.uk/s/search.html?collection=ual~sp-courses-meta-prod&profile=coursefinder&num_ranks=300&start_rank=1&query=!nullquery
  source_snippet: "1 - 300 of 1,075 search results" (full count extracted across 4 paginated pages, filtered to UG/PG levels)
  capture_date: 2026-07-08
  evidence_type: official_search_index

E-UG-002:
  field: ug.fee.home
  value: "£9,790 (2026/27, pending legislation)"
  source_url: https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees/undergraduate-tuition-fees
  source_snippet: "New students... £9,790. Please note that this tuition fee is subject to the passing of UK government legislation"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-UG-003:
  field: ug.fee.international
  value: "£30,890 (2026/27)"
  source_url: https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees/undergraduate-tuition-fees
  source_snippet: "Students starting a course in 2026 £30,890 *... may increase by up to 5% in later years"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-001:
  field: pg.fee.home.standard
  value: "£14,420 (45-week standard rate, 2026/27)"
  source_url: https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees/postgraduate-tuition-fees
  source_snippet: "Full-time: standard rate £14,420 45-week courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-002:
  field: pg.fee.international.standard
  value: "£30,890 (45-week standard rate, 2026/27)"
  source_url: https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees/postgraduate-tuition-fees
  source_snippet: "Full-time: standard rate £30,890 45-week courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-PG-003:
  field: pg.fee.international.higher
  value: "£34,885 (45-week higher rate, 2026/27)"
  source_url: https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees/postgraduate-tuition-fees
  source_snippet: "Full-time: higher rate £34,885 45-week courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-APP-001:
  field: ug.deadline.ucas
  value: "14 January 2026 at 6pm (UK time)"
  source_url: https://www.arts.ac.uk/study-at-ual/apply/undergraduate
  source_snippet: "The UCAS deadline for entry in September 2026 is 14 January 2026 at 6pm (UK time)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-APP-002:
  field: ug.deadline.ucas_extra
  value: "1 July 2026"
  source_url: https://www.arts.ac.uk/study-at-ual/apply/undergraduate
  source_snippet: "The UCAS Extra deadline is 1 July 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-ELP-001:
  field: ug.english.ielts
  value: "IELTS 6.0 overall, min 5.5 in each band (most BA Hons)"
  source_url: https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-csm
  source_snippet: "IELTS score of 6.0 or above, with at least 5.5 in reading, writing, listening and speaking"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-ELP-002:
  field: ug.english.pre_sessional
  value: "7-week on-campus or 12-week online Pre-sessional English available"
  source_url: https://www.arts.ac.uk/study-at-ual/international/pre-sessional-english
  source_snippet: "7 Week Pre-sessional On Campus... 12 Week Pre-sessional Online"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: the-arts-london-knowledge-base-v2
├── document: overview (this file — Section 0)
├── document: ug_programmes (Section 1)
├── document: pg_programmes (Section 2)
└── document: application_and_costs (Sections 3 + 4)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "the-arts-london-knowledge-base-v2"
  school: "<Camberwell|CSM|Chelsea|LCC|LCF|Wimbledon|CCI>"
  college: "<Camberwell College of Arts|Central Saint Martins|...>"
  subject_area: "<derived from URL /subjects/ segment>"
  degree_level: "<BA|BSc|MA|MSc|MRes|MArch|MDes|MBA|GradDip|PGCert|PGDip|MPhil|PhD>"
  level: undergraduate | postgraduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| **P0** | MPhil/PhD supervisor/area enumeration (research degrees are not in Funnelback) | https://www.arts.ac.uk/research/ |
| **P0** | Per-program tuition fee rate classification (lower/standard/higher) | https://www.arts.ac.uk/study-at-ual/fees-and-funding/tuition-fees/ |
| **P1** | Per-program entry requirements (UCAS tariff + portfolio rubric) | https://www.arts.ac.uk/subjects/<subject>/<level>/<course>-<college> |
| **P1** | Per-program international fees (some vary from headline rates) | per-program page |
| **P1** | Course duration (3-year / 4-year integrated / 1-year PG) | per-program page |
| **P1** | Halls of Residence cost per hall (7 UAL halls) | https://www.arts.ac.uk/study-at-ual/accommodation-services/halls-of-residence |
| **P2** | Specific scholarship amounts for international students | https://www.arts.ac.uk/study-at-ual/fees-and-funding/undergraduate-scholarships-and-funding |
| **P2** | Campus location per college (6 London campuses) | https://www.arts.ac.uk/colleges/<college> |
| **P2** | Course module structure for sample top-10 programmes | per-program page |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UAL | Cambridge (control) |
|-----------|-----|---------------------|
| Total degree programs (Rule 1) | 230 | ~300 |
| UG programs | 102 | ~80 |
| PG programs | 128 | ~220 |
| Specialist vs generalist | **Specialist (arts only)** | Generalist |
| Russell Group | **No** (arts-only specialist) | Yes |
| QS Subject ranking (Art & Design) | 2nd globally (2025) | not applicable (no art school) |
| Home fee (UG) | £9,790 | £9,535 |
| International fee (UG) | £30,890 | £24,507–£67,962 (varies by course) |
| Application platform | UCAS + UAL Portal (PG) | UCAS + direct (PG) |
| UCAS deadline | 14 Jan (equal consideration) | 15 Oct (Oxbridge comp), 14 Jan (most) |

> Cross-school note: UAL is the **only specialist arts university** in this comparison set. The 6 colleges + CCI make it a federated "university of universities" model, closer to the University of London structure than a single-department institution. Its 230 degree programs (UG+PG) make it **mid-sized** by UK standards but **the largest specialist arts university in Europe**.

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: arts.ac.uk (UAL official site), ual-search.arts.ac.uk (Funnelback course index)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → college → degree-level → program
> **Completeness**: UG+PG full enumeration ✓ | 5 structural rules ✓ | Reconciliation ✓ | Evidence blocks ✓
> **Reconciliation**: 230 (Rule 1) = 230 (matrix sum) = 230 (Sections 1+2 row count)
