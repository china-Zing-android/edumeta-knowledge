# University of Surrey Admissions Knowledge Base - Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)
> **Region**: UK
---

## SECTION 0 - Institution overview

### 0.1 Counts

| Dimension | Count |
|------|------|
| UG Majors (incl. integrated master's) | 115 |
| PG Taught (PGT) | 94 |
| **Total degree programmes (UG + PGT)** | **209** |
| Faculties | 3 |
| Schools | 12 |
| Subject areas | 32 |

> **Data source**: Surrey UG/PGT listing pages (5 pages each), A-Z subject list at `/subjects`.
> Surrey uses a 3-faculty structure (Arts/Business/Social Sciences, Engineering/Physical Sciences, Health/Medical Sciences) plus cross-faculty Institutes. UG listing shows 5 pages of results; PGT listing shows 5 pages (~104 programmes, 94 unique after dedup).

### 0.2 Hierarchy

```
University of Surrey
|-- Faculty of Arts, Business and Social Sciences (FABSS)            [Faculty]
|   |-- School of Arts, Humanities and Creative Industries          [School]
|   |-- School of Social Sciences                                   [School]
|   `-- Surrey Business School                                      [School]
|-- Faculty of Engineering and Physical Sciences (FEPS)             [Faculty]
|   |-- School of Chemistry and Chemical Engineering                [School]
|   |-- School of Computer Science and Electronic Engineering       [School]
|   |-- School of Engineering                                       [School]
|   `-- School of Mathematics and Physics                           [School]
|-- Faculty of Health and Medical Sciences (FHMS)                   [Faculty]
|   |-- School of Biosciences                                       [School]
|   |-- School of Health Sciences                                   [School]
|   |-- School of Medicine                                          [School]
|   |-- School of Psychology                                        [School]
|   `-- School of Veterinary Medicine                               [School]
`-- Institutes (cross-faculty)                                      [Special]
    |-- Institute for Sustainability
    |-- People-Centred Artificial Intelligence
    |-- Surrey Space Institute
    `-- Surrey Institute of Education
```

> **Note**: Surrey has no central "College" system; each School sits directly under its Faculty. Veterinary Medicine is in FHMS but operates its own degree (BVMSci).

### 0.3 Degree-level inventory

| Official code | Full name | Level | Count |
|---------|------|------|-------|
| BSc (Hons) | Bachelor of Science (Honours) | UG | 57 |
| MEng | Master of Engineering (integrated 4-year) | UG (integrated master) | 12 |
| BEng (Hons) | Bachelor of Engineering (Honours) | UG | 11 |
| BA (Hons) | Bachelor of Arts (Honours) | UG | 10 |
| LLB (Hons) | Bachelor of Laws (Honours) | UG | 6 |
| MPhys | Master of Physics (integrated 4-year) | UG (integrated master) | 4 |
| MSci (Hons) | Master in Science (integrated 4-year) | UG (integrated master) | 3 |
| MChem | Master of Chemistry (integrated 4-year) | UG (integrated master) | 3 |
| BMus (Hons) | Bachelor of Music (Honours) | UG | 3 |
| MMath | Master of Mathematics (integrated 4-year) | UG (integrated master) | 3 |
| CertHE | Certificate of Higher Education | UG pre-degree | 2 |
| BMBS | Bachelor of Medicine, Bachelor of Surgery | UG (Graduate Entry) | 1 |
| MSc/PG (verify) | Postgraduate taught | PGT | 94 |

> **UK integrated master's note**: MEng, MChem, MMath, MPhys, MSci are 4-year undergraduate integrated master's degrees (not equivalent to standalone MSc).

### 0.4 Distribution matrix (Faculty x canonical degree level)

| Faculty \ Degree | BSc (Hons) | BA (Hons) | BEng (Hons) | BMus (Hons) | LLB (Hons) | CertHE | BMBS | MEng | MChem | MMath | MPhys | MSci (Hons) | MSc/PG (verify) | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
Faculty of Arts, Business and Social Sciences | 29 | 10 | 1 | 3 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 31 | **82** |
Faculty of Engineering and Physical Sciences | 15 | 0 | 10 | 0 | 0 | 0 | 0 | 12 | 3 | 3 | 4 | 1 | 37 | **85** |
Faculty of Health and Medical Sciences | 13 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 26 | **42** |
| **Total** | 57 | 10 | 11 | 3 | 6 | 2 | 1 | 12 | 3 | 3 | 4 | 3 | 94 | **209** |
> **Reconciliation**: FABSS(82) + FEPS(85) + FHMS(42) = 209 matches rule-1 total (209). UG-only total = 115; PGT-only = 94.

---

## SECTION 1 - Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Surrey's undergraduate teaching is organized within 3 faculties containing 12 schools. UCAS institution code: **S85**. Surrey accepts applications via UCAS for all UG programmes.

### 1.2 Undergraduate majors - grouped by Faculty > School > Degree level

#### Faculty of Arts, Business and Social Sciences

##### School of Arts, Humanities and Creative Industries

###### BA (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Acting | [Link](https://www.surrey.ac.uk/undergraduate/acting) |
| 2 | Actor-Musician | [Link](https://www.surrey.ac.uk/undergraduate/actor-musician) |
| 3 | Applied and Contemporary Theatre | [Link](https://www.surrey.ac.uk/undergraduate/applied-and-contemporary-theatre) |
| 4 | English Literature | [Link](https://www.surrey.ac.uk/undergraduate/english-literature) |
| 5 | English Literature and Creative Writing | [Link](https://www.surrey.ac.uk/undergraduate/english-literature-and-creative-writing) |
| 6 | English Literature and French | [Link](https://www.surrey.ac.uk/undergraduate/english-literature-and-french) |
| 7 | English Literature and Spanish | [Link](https://www.surrey.ac.uk/undergraduate/english-literature-and-spanish) |
| 8 | Games Art | [Link](https://www.surrey.ac.uk/undergraduate/games-art) |
| 9 | Modern Languages (French and Spanish) | [Link](https://www.surrey.ac.uk/undergraduate/modern-languages-french-and-spanish) |
| 10 | Musical Theatre | [Link](https://www.surrey.ac.uk/undergraduate/musical-theatre) |

###### BEng (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Film Production and Broadcast Engineering | [Link](https://www.surrey.ac.uk/undergraduate/film-production-and-broadcast-engineering) |

###### BMus (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Creative Music Technology | [Link](https://www.surrey.ac.uk/undergraduate/creative-music-technology) |
| 2 | Music | [Link](https://www.surrey.ac.uk/undergraduate/music) |
| 3 | Music and Sound Recording (Tonmeister) | [Link](https://www.surrey.ac.uk/undergraduate/music-and-sound-recording-tonmeister) |

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Games Design | [Link](https://www.surrey.ac.uk/undergraduate/games-design) |
| 2 | Media and Communication | [Link](https://www.surrey.ac.uk/undergraduate/media-and-communication) |
| 3 | Music and Sound Recording (Tonmeister) | [Link](https://www.surrey.ac.uk/undergraduate/music-and-sound-recording-tonmeister) |

###### CertHE

| # | Programme | URL |
|---|------|-----|
| 1 | Foundation Acting | [Link](https://www.surrey.ac.uk/undergraduate/foundation-acting) |
| 2 | Foundation Musical Theatre | [Link](https://www.surrey.ac.uk/undergraduate/foundation-musical-theatre) |

##### School of Social Sciences

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Criminology | [Link](https://www.surrey.ac.uk/undergraduate/criminology) |
| 2 | Criminology and Psychology | [Link](https://www.surrey.ac.uk/undergraduate/criminology-and-psychology) |
| 3 | Criminology and Sociology | [Link](https://www.surrey.ac.uk/undergraduate/criminology-and-sociology) |
| 4 | Criminology with Forensic Investigation | [Link](https://www.surrey.ac.uk/undergraduate/criminology-forensic-investigation) |

###### LLB (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Law | [Link](https://www.surrey.ac.uk/undergraduate/law) |
| 2 | Law (Law and Technology Pathway) | [Link](https://www.surrey.ac.uk/undergraduate/law-law-and-technology-pathway) |
| 3 | Law (Law, Environment and Sustainability Pathway) | [Link](https://www.surrey.ac.uk/undergraduate/law-law-environment-and-sustainability-pathway) |
| 4 | Law (Philosophy, Politics and Law Pathway) | [Link](https://www.surrey.ac.uk/undergraduate/law-philosophy-politics-and-law-pathway) |
| 5 | Law with Criminology | [Link](https://www.surrey.ac.uk/undergraduate/law-criminology) |
| 6 | Law with International Relations | [Link](https://www.surrey.ac.uk/undergraduate/law-international-relations) |

##### Surrey Business School

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Accounting and Finance | [Link](https://www.surrey.ac.uk/undergraduate/accounting-and-finance) |
| 2 | Business Economics and Data Analytics | [Link](https://www.surrey.ac.uk/undergraduate/business-economics-and-data-analytics) |
| 3 | Business Management | [Link](https://www.surrey.ac.uk/undergraduate/business-management) |
| 4 | Business Management and Modern Languages | [Link](https://www.surrey.ac.uk/undergraduate/business-management-and-modern-languages) |
| 5 | Business Management with Business Analytics | [Link](https://www.surrey.ac.uk/undergraduate/business-management-business-analytics) |
| 6 | Business Management with Entrepreneurship and Innovation | [Link](https://www.surrey.ac.uk/undergraduate/business-management-entrepreneurship-and-innovation) |
| 7 | Business Management with Human Resource Management | [Link](https://www.surrey.ac.uk/undergraduate/business-management-human-resource-management) |
| 8 | Business Management with Marketing | [Link](https://www.surrey.ac.uk/undergraduate/business-management-marketing) |
| 9 | Economics | [Link](https://www.surrey.ac.uk/undergraduate/economics) |
| 10 | Economics and Finance | [Link](https://www.surrey.ac.uk/undergraduate/economics-and-finance) |
| 11 | Economics and Mathematics | [Link](https://www.surrey.ac.uk/undergraduate/economics-and-mathematics) |
| 12 | International Accounting with Finance (FHEQ Level 5 Direct Entry) | [Link](https://www.surrey.ac.uk/undergraduate/international-accounting-finance-fheq-level-5-direct-entry) |
| 13 | International Accounting with Finance (FHEQ Level 6 Direct Entry) | [Link](https://www.surrey.ac.uk/undergraduate/international-accounting-finance-fheq-level-6-direct-entry) |
| 14 | International Airline and Airport Management | [Link](https://www.surrey.ac.uk/undergraduate/international-airline-and-airport-management) |
| 15 | International Business (FHEQ Level 5 Direct Entry) | [Link](https://www.surrey.ac.uk/undergraduate/international-business-fheq-level-5-direct-entry) |
| 16 | International Business (FHEQ Level 6 Direct Entry) | [Link](https://www.surrey.ac.uk/undergraduate/international-business-fheq-level-6-direct-entry) |
| 17 | International Business Management | [Link](https://www.surrey.ac.uk/undergraduate/international-business-management) |
| 18 | International Event Management | [Link](https://www.surrey.ac.uk/undergraduate/international-event-management) |
| 19 | International Hospitality Management | [Link](https://www.surrey.ac.uk/undergraduate/international-hospitality-management) |
| 20 | International Hospitality and Tourism Management | [Link](https://www.surrey.ac.uk/undergraduate/international-hospitality-and-tourism-management) |
| 21 | International Relations | [Link](https://www.surrey.ac.uk/undergraduate/international-relations) |
| 22 | International Tourism Management | [Link](https://www.surrey.ac.uk/undergraduate/international-tourism-management) |

#### Faculty of Engineering and Physical Sciences

##### School of Chemistry and Chemical Engineering

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Biochemistry | [Link](https://www.surrey.ac.uk/undergraduate/biochemistry) |
| 2 | Chemistry | [Link](https://www.surrey.ac.uk/undergraduate/chemistry) |
| 3 | Chemistry with Forensic Investigation | [Link](https://www.surrey.ac.uk/undergraduate/chemistry-forensic-investigation) |
| 4 | Medicinal Chemistry | [Link](https://www.surrey.ac.uk/undergraduate/medicinal-chemistry) |

###### MChem

| # | Programme | URL |
|---|------|-----|
| 1 | Chemistry | [Link](https://www.surrey.ac.uk/undergraduate/chemistry) |
| 2 | Chemistry with Forensic Investigation | [Link](https://www.surrey.ac.uk/undergraduate/chemistry-forensic-investigation) |
| 3 | Medicinal Chemistry | [Link](https://www.surrey.ac.uk/undergraduate/medicinal-chemistry) |

###### MSci (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Biochemistry | [Link](https://www.surrey.ac.uk/undergraduate/biochemistry) |

##### School of Computer Science and Electronic Engineering

###### BEng (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering | [Link](https://www.surrey.ac.uk/undergraduate/electrical-and-electronic-engineering) |

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Computer Science | [Link](https://www.surrey.ac.uk/undergraduate/computer-science) |
| 2 | Computer Science and Artificial Intelligence | [Link](https://www.surrey.ac.uk/undergraduate/computer-science-and-artificial-intelligence) |
| 3 | Computer Science and Cyber Security | [Link](https://www.surrey.ac.uk/undergraduate/computer-science-and-cyber-security) |
| 4 | Computing with Business Management | [Link](https://www.surrey.ac.uk/undergraduate/computing-business-management) |

###### MEng

| # | Programme | URL |
|---|------|-----|
| 1 | Computer Science | [Link](https://www.surrey.ac.uk/undergraduate/computer-science) |
| 2 | Computer Science and Artificial Intelligence | [Link](https://www.surrey.ac.uk/undergraduate/computer-science-and-artificial-intelligence) |
| 3 | Electrical and Electronic Engineering | [Link](https://www.surrey.ac.uk/undergraduate/electrical-and-electronic-engineering) |

##### School of Engineering

###### BEng (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Aerospace Engineering | [Link](https://www.surrey.ac.uk/undergraduate/aerospace-engineering) |
| 2 | Astronautics and Space Engineering | [Link](https://www.surrey.ac.uk/undergraduate/astronautics-and-space-engineering) |
| 3 | Biomedical Engineering | [Link](https://www.surrey.ac.uk/undergraduate/biomedical-engineering) |
| 4 | Chemical Engineering | [Link](https://www.surrey.ac.uk/undergraduate/chemical-engineering) |
| 5 | Civil Engineering | [Link](https://www.surrey.ac.uk/undergraduate/civil-engineering) |
| 6 | Computer and Internet Engineering | [Link](https://www.surrey.ac.uk/undergraduate/computer-and-internet-engineering) |
| 7 | Electronic Engineering | [Link](https://www.surrey.ac.uk/undergraduate/electronic-engineering) |
| 8 | Electronic Engineering with Artificial Intelligence | [Link](https://www.surrey.ac.uk/undergraduate/electronic-engineering-artificial-intelligence) |
| 9 | Mechanical Engineering | [Link](https://www.surrey.ac.uk/undergraduate/mechanical-engineering) |

###### MEng

| # | Programme | URL |
|---|------|-----|
| 1 | Aerospace Engineering | [Link](https://www.surrey.ac.uk/undergraduate/aerospace-engineering) |
| 2 | Astronautics and Space Engineering | [Link](https://www.surrey.ac.uk/undergraduate/astronautics-and-space-engineering) |
| 3 | Biomedical Engineering | [Link](https://www.surrey.ac.uk/undergraduate/biomedical-engineering) |
| 4 | Chemical Engineering | [Link](https://www.surrey.ac.uk/undergraduate/chemical-engineering) |
| 5 | Civil Engineering | [Link](https://www.surrey.ac.uk/undergraduate/civil-engineering) |
| 6 | Computer and Internet Engineering | [Link](https://www.surrey.ac.uk/undergraduate/computer-and-internet-engineering) |
| 7 | Electronic Engineering | [Link](https://www.surrey.ac.uk/undergraduate/electronic-engineering) |
| 8 | Electronic Engineering with Artificial Intelligence | [Link](https://www.surrey.ac.uk/undergraduate/electronic-engineering-artificial-intelligence) |
| 9 | Mechanical Engineering | [Link](https://www.surrey.ac.uk/undergraduate/mechanical-engineering) |

##### School of Mathematics and Physics

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Financial Mathematics | [Link](https://www.surrey.ac.uk/undergraduate/financial-mathematics) |
| 2 | Mathematics | [Link](https://www.surrey.ac.uk/undergraduate/mathematics) |
| 3 | Mathematics and Physics | [Link](https://www.surrey.ac.uk/undergraduate/mathematics-and-physics) |
| 4 | Mathematics with Data Science | [Link](https://www.surrey.ac.uk/undergraduate/mathematics-data-science) |
| 5 | Physics | [Link](https://www.surrey.ac.uk/undergraduate/physics) |
| 6 | Physics with Astronomy | [Link](https://www.surrey.ac.uk/undergraduate/physics-astronomy) |
| 7 | Physics with Nuclear Astrophysics | [Link](https://www.surrey.ac.uk/undergraduate/physics-nuclear-astrophysics) |

###### MMath

| # | Programme | URL |
|---|------|-----|
| 1 | Mathematics | [Link](https://www.surrey.ac.uk/undergraduate/mathematics) |
| 2 | Mathematics and Physics | [Link](https://www.surrey.ac.uk/undergraduate/mathematics-and-physics) |
| 3 | Mathematics with Data Science | [Link](https://www.surrey.ac.uk/undergraduate/mathematics-data-science) |

###### MPhys

| # | Programme | URL |
|---|------|-----|
| 1 | Mathematics and Physics | [Link](https://www.surrey.ac.uk/undergraduate/mathematics-and-physics) |
| 2 | Physics | [Link](https://www.surrey.ac.uk/undergraduate/physics) |
| 3 | Physics with Astronomy | [Link](https://www.surrey.ac.uk/undergraduate/physics-astronomy) |
| 4 | Physics with Nuclear Astrophysics | [Link](https://www.surrey.ac.uk/undergraduate/physics-nuclear-astrophysics) |

#### Faculty of Health and Medical Sciences

##### School of Biosciences

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Biological Sciences | [Link](https://www.surrey.ac.uk/undergraduate/biological-sciences) |
| 2 | Environment and Sustainability | [Link](https://www.surrey.ac.uk/undergraduate/environment-and-sustainability) |
| 3 | Microbiology | [Link](https://www.surrey.ac.uk/undergraduate/microbiology) |
| 4 | Pharmaceutical Sciences | [Link](https://www.surrey.ac.uk/undergraduate/pharmaceutical-sciences) |

###### MSci (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | [Link](https://www.surrey.ac.uk/undergraduate/pharmaceutical-sciences) |

##### School of Health Sciences

###### BSc (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Biomedical Science | [Link](https://www.surrey.ac.uk/undergraduate/biomedical-science) |
| 2 | Food Science and Nutrition | [Link](https://www.surrey.ac.uk/undergraduate/food-science-and-nutrition) |
| 3 | Midwifery (Registered Midwife) | [Link](https://www.surrey.ac.uk/undergraduate/midwifery-registered-midwife) |
| 4 | Nursing Studies (Registered Nurse Adult Nursing) | [Link](https://www.surrey.ac.uk/undergraduate/nursing-studies-registered-nurse-adult-nursing) |
| 5 | Nursing Studies (Registered Nurse Children and Young People Nursing) | [Link](https://www.surrey.ac.uk/undergraduate/nursing-studies-registered-nurse-children-and-young-people-nursing) |
| 6 | Nursing Studies (Registered Nurse Mental Health Nursing) | [Link](https://www.surrey.ac.uk/undergraduate/nursing-studies-registered-nurse-mental-health-nursing) |
| 7 | Nutrition | [Link](https://www.surrey.ac.uk/undergraduate/nutrition) |
| 8 | Nutrition and Dietetics | [Link](https://www.surrey.ac.uk/undergraduate/nutrition-and-dietetics) |
| 9 | Paramedic Science | [Link](https://www.surrey.ac.uk/undergraduate/paramedic-science) |

###### MSci (Hons)

| # | Programme | URL |
|---|------|-----|
| 1 | Biomedical Science | [Link](https://www.surrey.ac.uk/undergraduate/biomedical-science) |

##### School of Medicine

###### BMBS

| # | Programme | URL |
|---|------|-----|
| 1 | Medicine (Graduate Entry) | [Link](https://www.surrey.ac.uk/undergraduate/medicine-graduate-entry) |


### 1.3 Interdisciplinary / cross-faculty undergraduate programmes

| # | Programme | Degree | Cross-faculty home | URL |
|---|------|------|---------|-----|
| 1 | Business Management and Modern Languages | BSc (Hons) | Surrey Business School + School of Arts, Humanities and Creative Industries | [Link](https://www.surrey.ac.uk/undergraduate/business-management-and-modern-languages) |
| 2 | Computer Science (with placement year variants) | BSc (Hons) / MEng | School of Computer Science and Electronic Engineering (FEPS) | [Link](https://www.surrey.ac.uk/undergraduate/computer-science) |
| 3 | Mathematics and Physics | BSc (Hons) / MMath / MPhys | School of Mathematics and Physics (FEPS) | [Link](https://www.surrey.ac.uk/undergraduate/mathematics-and-physics) |
| 4 | Economics and Mathematics | BSc (Hons) | Surrey Business School + School of Mathematics and Physics | [Link](https://www.surrey.ac.uk/undergraduate/economics-and-mathematics) |
| 5 | English Literature and French | BA (Hons) | School of Arts, Humanities and Creative Industries (FABSS) | [Link](https://www.surrey.ac.uk/undergraduate/english-literature-and-french) |
| 6 | English Literature and Spanish | BA (Hons) | School of Arts, Humanities and Creative Industries (FABSS) | [Link](https://www.surrey.ac.uk/undergraduate/english-literature-and-spanish) |
| 7 | Music and Sound Recording (Tonmeister) | BMus (Hons) / BSc (Hons) | School of Arts, Humanities and Creative Industries (FABSS) | [Link](https://www.surrey.ac.uk/undergraduate/music-and-sound-recording-tonmeister) |
| 8 | Criminology and Psychology | BSc (Hons) | School of Social Sciences + School of Psychology (FABSS+FHMS) | [Link](https://www.surrey.ac.uk/undergraduate/criminology-and-psychology) |
| 9 | Criminology and Sociology | BSc (Hons) | School of Social Sciences (FABSS) | [Link](https://www.surrey.ac.uk/undergraduate/criminology-and-sociology) |
| 10 | Law (multiple pathways) | LLB (Hons) | School of Social Sciences (FABSS) with cross-faculty specialisms (Tech, EnvSust, Politics) | [Link](https://www.surrey.ac.uk/undergraduate/law-law-and-technology-pathway) |

### 1.4 Minors - complete list

N/A (Surrey does not publish a standalone minor list at UG level; students take optional modules, study-year-abroad, or professional training year instead).

### 1.5 General/Institute-wide requirements

Surrey does not impose an institute-wide core curriculum; each programme specifies its own structure. Common patterns:
- **Professional Training Year (PTY)**: optional paid placement year (most BSc/BEng programmes list "Placement year available").
- **Foundation Year**: many programmes offer a `BSc/BEng (Hons) with foundation year` entry (typical offer CCC).
- **Study abroad**: Surrey participates in Erasmus+ and international exchange via `https://www.surrey.ac.uk/student-exchanges/incoming-students`.

---

## SECTION 2 - Graduate Education (Rule 5 grouping)

### 2.1 Graduate programmes - grouped by Faculty > School > Degree level

> Surrey's PGT (postgraduate taught) listing at `/postgraduate` has 5 pages with ~104 results (94 unique). The fee page enumerates 2026-entry fees with full per-programme UK/Overseas split. Programmes listed below by faculty/school; specific MSc vs MA/PGDip split is in the per-programme detail page (linked).

#### Faculty of Arts, Business and Social Sciences

##### School of Arts, Humanities and Creative Industries

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Acting Ma | [Link](https://www.surrey.ac.uk/postgraduate/acting-ma) |
| 2 | Acting Mfa | [Link](https://www.surrey.ac.uk/postgraduate/acting-mfa) |
| 3 | Ai Translation And Interpreting Studies Msc | [Link](https://www.surrey.ac.uk/postgraduate/ai-translation-and-interpreting-studies-msc) |
| 4 | Air Transport Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/air-transport-management-msc) |
| 5 | Creative Writing Ma | [Link](https://www.surrey.ac.uk/postgraduate/creative-writing-ma) |
| 6 | English Literature Ma | [Link](https://www.surrey.ac.uk/postgraduate/english-literature-ma) |
| 7 | Film Animation And Digital Arts Ma | [Link](https://www.surrey.ac.uk/postgraduate/film-animation-and-digital-arts-ma) |
| 8 | Interpreting Technology And Ai Chinese Pathway Ma | [Link](https://www.surrey.ac.uk/postgraduate/interpreting-technology-and-ai-chinese-pathway-ma) |
| 9 | Interpreting Technology And Ai Ma | [Link](https://www.surrey.ac.uk/postgraduate/interpreting-technology-and-ai-ma) |
| 10 | Music Mmus | [Link](https://www.surrey.ac.uk/postgraduate/music-mmus) |
| 11 | Musical Theatre Ma | [Link](https://www.surrey.ac.uk/postgraduate/musical-theatre-ma) |
| 12 | Musical Theatre Mfa | [Link](https://www.surrey.ac.uk/postgraduate/musical-theatre-mfa) |

##### School of Social Sciences

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Criminology Cybercrime And Cybersecurity Msc | [Link](https://www.surrey.ac.uk/postgraduate/criminology-cybercrime-and-cybersecurity-msc) |
| 2 | Fintech And Policy Msc | [Link](https://www.surrey.ac.uk/postgraduate/fintech-and-policy-msc) |

##### Surrey Business School

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Accounting And Finance Msc | [Link](https://www.surrey.ac.uk/postgraduate/accounting-and-finance-msc) |
| 2 | Banking And Finance Msc | [Link](https://www.surrey.ac.uk/postgraduate/banking-and-finance-msc) |
| 3 | Digital Marketing Msc | [Link](https://www.surrey.ac.uk/postgraduate/digital-marketing-msc) |
| 4 | Economics And Finance Msc | [Link](https://www.surrey.ac.uk/postgraduate/economics-and-finance-msc) |
| 5 | Economics Econometrics And Big Data Msc | [Link](https://www.surrey.ac.uk/postgraduate/economics-econometrics-and-big-data-msc) |
| 6 | Economics Mres | [Link](https://www.surrey.ac.uk/postgraduate/economics-mres) |
| 7 | Economics Msc | [Link](https://www.surrey.ac.uk/postgraduate/economics-msc) |
| 8 | Entrepreneurship Innovation Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/entrepreneurship-innovation-management-msc) |
| 9 | Intercultural Business Communication And Marketing Ma | [Link](https://www.surrey.ac.uk/postgraduate/intercultural-business-communication-and-marketing-ma) |
| 10 | International Business Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-business-management-msc) |
| 11 | International Events Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-events-management-msc) |
| 12 | International Marketing Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-marketing-msc) |
| 13 | International Relations International Intervention Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-relations-international-intervention-msc) |
| 14 | International Relations Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-relations-msc) |
| 15 | International Tourism Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-tourism-management-msc) |
| 16 | Master Business Administration Mba | [Link](https://www.surrey.ac.uk/postgraduate/master-business-administration-mba) |
| 17 | Strategic Marketing Msc | [Link](https://www.surrey.ac.uk/postgraduate/strategic-marketing-msc) |

#### Faculty of Engineering and Physical Sciences

##### School of Chemistry and Chemical Engineering

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Applied Analytical Chemistry Msc | [Link](https://www.surrey.ac.uk/postgraduate/applied-analytical-chemistry-msc) |

##### School of Computer Science and Electronic Engineering

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Applied Quantum Computing Msc | [Link](https://www.surrey.ac.uk/postgraduate/applied-quantum-computing-msc) |
| 2 | Computer Vision Robotics And Machine Learning Msc | [Link](https://www.surrey.ac.uk/postgraduate/computer-vision-robotics-and-machine-learning-msc) |

##### School of Engineering

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Advanced Clinical Practice Msc | [Link](https://www.surrey.ac.uk/postgraduate/advanced-clinical-practice-msc) |
| 2 | Advanced Geotechnical Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/advanced-geotechnical-engineering-msc) |
| 3 | Artificial Intelligence Conversion Msc | [Link](https://www.surrey.ac.uk/postgraduate/artificial-intelligence-conversion-msc) |
| 4 | Artificial Intelligence Msc | [Link](https://www.surrey.ac.uk/postgraduate/artificial-intelligence-msc) |
| 5 | Astronautics And Space Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/astronautics-and-space-engineering-msc) |
| 6 | Behaviour Change Msc | [Link](https://www.surrey.ac.uk/postgraduate/behaviour-change-msc) |
| 7 | Biotechnology Msc | [Link](https://www.surrey.ac.uk/postgraduate/biotechnology-msc) |
| 8 | Bridge Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/bridge-engineering-msc) |
| 9 | Business Analytics Msc | [Link](https://www.surrey.ac.uk/postgraduate/business-analytics-msc) |
| 10 | Civil Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/civil-engineering-msc) |
| 11 | Cyber Security Msc | [Link](https://www.surrey.ac.uk/postgraduate/cyber-security-msc) |
| 12 | Data Science Conversion Msc | [Link](https://www.surrey.ac.uk/postgraduate/data-science-conversion-msc) |
| 13 | Data Science Msc | [Link](https://www.surrey.ac.uk/postgraduate/data-science-msc) |
| 14 | Electronic Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/electronic-engineering-msc) |
| 15 | Financial Data Science Msc | [Link](https://www.surrey.ac.uk/postgraduate/financial-data-science-msc) |
| 16 | Higher And Professional Education Ma | [Link](https://www.surrey.ac.uk/postgraduate/higher-and-professional-education-ma) |
| 17 | Human Resources Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/human-resources-management-msc) |
| 18 | Infrastructure Engineering And Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/infrastructure-engineering-and-management-msc) |
| 19 | Intelligent Communication Systems And Networks Msc | [Link](https://www.surrey.ac.uk/postgraduate/intelligent-communication-systems-and-networks-msc) |
| 20 | International Financial Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-financial-management-msc) |
| 21 | International Hotel Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/international-hotel-management-msc) |
| 22 | Investment Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/investment-management-msc) |
| 23 | Nuclear Science And Radiation Protection Msc | [Link](https://www.surrey.ac.uk/postgraduate/nuclear-science-and-radiation-protection-msc) |
| 24 | Process Systems Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/process-systems-engineering-msc) |
| 25 | Professional Legal Practice Sqe Pathway Llm | [Link](https://www.surrey.ac.uk/postgraduate/professional-legal-practice-sqe-pathway-llm) |
| 26 | Public Affairs Msc | [Link](https://www.surrey.ac.uk/postgraduate/public-affairs-msc) |
| 27 | Research | [Link](https://www.surrey.ac.uk/postgraduate/research) |
| 28 | Satellite Communications Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/satellite-communications-engineering-msc) |
| 29 | Stage And Production Management Ma | [Link](https://www.surrey.ac.uk/postgraduate/stage-and-production-management-ma) |
| 30 | Strategic Hotel Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/strategic-hotel-management-msc) |
| 31 | Structural Engineering Msc | [Link](https://www.surrey.ac.uk/postgraduate/structural-engineering-msc) |

##### School of Mathematics and Physics

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Mathematics Msc | [Link](https://www.surrey.ac.uk/postgraduate/mathematics-msc) |
| 2 | Medical Physics Msc | [Link](https://www.surrey.ac.uk/postgraduate/medical-physics-msc) |
| 3 | Physics Msc | [Link](https://www.surrey.ac.uk/postgraduate/physics-msc) |

#### Faculty of Health and Medical Sciences

##### School of Biosciences

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Corporate Environmental Management Msc | [Link](https://www.surrey.ac.uk/postgraduate/corporate-environmental-management-msc) |
| 2 | Environmental Psychology Msc | [Link](https://www.surrey.ac.uk/postgraduate/environmental-psychology-msc) |
| 3 | Environmental Strategy Msc | [Link](https://www.surrey.ac.uk/postgraduate/environmental-strategy-msc) |
| 4 | Pharmaceutical Sciences Msc | [Link](https://www.surrey.ac.uk/postgraduate/pharmaceutical-sciences-msc) |
| 5 | Sustainable Development Msc | [Link](https://www.surrey.ac.uk/postgraduate/sustainable-development-msc) |
| 6 | Sustainable Energy Msc | [Link](https://www.surrey.ac.uk/postgraduate/sustainable-energy-msc) |

##### School of Health Sciences

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Clinical Psychology And Mental Health Msc | [Link](https://www.surrey.ac.uk/postgraduate/clinical-psychology-and-mental-health-msc) |
| 2 | Education Health Professionals Ma | [Link](https://www.surrey.ac.uk/postgraduate/education-health-professionals-ma) |
| 3 | Education Health Professionals Pgcert | [Link](https://www.surrey.ac.uk/postgraduate/education-health-professionals-pgcert) |
| 4 | Food Science Msc | [Link](https://www.surrey.ac.uk/postgraduate/food-science-msc) |
| 5 | Health Psychology Msc | [Link](https://www.surrey.ac.uk/postgraduate/health-psychology-msc) |
| 6 | Healthcare Practice Msc | [Link](https://www.surrey.ac.uk/postgraduate/healthcare-practice-msc) |
| 7 | Human Nutrition Msc | [Link](https://www.surrey.ac.uk/postgraduate/human-nutrition-msc) |
| 8 | Leadership Healthcare Msc | [Link](https://www.surrey.ac.uk/postgraduate/leadership-healthcare-msc) |
| 9 | Nutritional Medicine Msc | [Link](https://www.surrey.ac.uk/postgraduate/nutritional-medicine-msc) |
| 10 | Primary And Community Care Spq Community Childrens Nursing Integrated Prescribing V300 Pgdip | [Link](https://www.surrey.ac.uk/postgraduate/primary-and-community-care-spq-community-childrens-nursing-integrated-prescribing-v300-pgdip) |
| 11 | Primary And Community Care Spq Community Childrens Nursing Pgdip | [Link](https://www.surrey.ac.uk/postgraduate/primary-and-community-care-spq-community-childrens-nursing-pgdip) |
| 12 | Primary And Community Care Spq District Nursing Integrated Prescribing V300 Pgdip | [Link](https://www.surrey.ac.uk/postgraduate/primary-and-community-care-spq-district-nursing-integrated-prescribing-v300-pgdip) |
| 13 | Primary And Community Care Spq District Nursing Pgdip | [Link](https://www.surrey.ac.uk/postgraduate/primary-and-community-care-spq-district-nursing-pgdip) |
| 14 | Public Health Practice Scphn Health Visiting Pgdip | [Link](https://www.surrey.ac.uk/postgraduate/public-health-practice-scphn-health-visiting-pgdip) |
| 15 | Public Health Practice Scphn School Nursing Pgdip | [Link](https://www.surrey.ac.uk/postgraduate/public-health-practice-scphn-school-nursing-pgdip) |
| 16 | Specialist Practice Nursing Top Msc | [Link](https://www.surrey.ac.uk/postgraduate/specialist-practice-nursing-top-msc) |

##### School of Psychology

| # | Programme (see URL for exact degree) | URL |
|---|------|-----|
| 1 | Occupational And Organizational Psychology Msc | [Link](https://www.surrey.ac.uk/postgraduate/occupational-and-organizational-psychology-msc) |
| 2 | Psychology Conversion Msc | [Link](https://www.surrey.ac.uk/postgraduate/psychology-conversion-msc) |
| 3 | Psychology Game Design And Digital Innovation Msc | [Link](https://www.surrey.ac.uk/postgraduate/psychology-game-design-and-digital-innovation-msc) |
| 4 | Social Psychology Msc | [Link](https://www.surrey.ac.uk/postgraduate/social-psychology-msc) |


### 2.2 One programme deep-dive (worked example)

**MSc Accounting and Finance** (Surrey Business School):
- **Source URL**: https://www.surrey.ac.uk/postgraduate/accounting-and-finance
- **Faculty/School**: FABSS / Surrey Business School
- **2026 fees**: UK GBP 15,800 (FT) / GBP 7,900 (PT) ; Overseas GBP 25,900 (FT) / GBP 13,000 (PT) (Feb 2027 entry same rates)
- **Duration**: 1 year FT / 2 years PT
- **Accreditation**: AACSB, ACCA, CIMA exemptions available
- **Application**: Direct via Surrey portal (no UCAS for PG)

### 2.3 Graduate admissions model

- **Decentralized within central framework**: Apply direct via Surrey's online portal `https://www.surrey.ac.uk/apply/postgraduate`. Each school handles its own admissions decisions.
- **Application fee**: typically GBP 0-50 (varies by programme; Surrey uses no centralized fee)
- **Deadlines**: rolling for most PGT programmes; international students advised to apply by July for September entry
- **GRE/GMAT**: Generally not required; some programmes may ask for GMAT - check per-programme
- **English language**: see Section 3.2

---

## SECTION 3 - Application requirements & deadlines

### 3.1 Undergraduate - core data table

| Dimension | Data |
|------|------|
| Admissions site | https://www.surrey.ac.uk/study/undergraduate |
| Application portal | **UCAS** (institution code **S85**); Surrey does not use Common App |
| UCAS equal-consideration deadline | **January** (most programmes) - some vet/medicine earlier |
| Typical offers (UG) | A-Level ranges from **CCC** (foundation/acting) to **AAA** (MEng, MSci, medicine) - see per-programme `Typical offer` field |
| IB offers | Published per programme (typical 32-36 points) |
| Personal statement | UCAS format (post-2024 3-question format) |
| References | 1 academic reference (UCAS) |
| Interviews | None for most UG; **BMBS Medicine** uses MMI interviews (Graduate Entry) |
| Open days | https://www.surrey.ac.uk/undergraduate-study/undergraduate-open-days |
| Clearing | https://www.surrey.ac.uk/clearing/courses |

### 3.2 Undergraduate English proficiency table

Most UG programmes require **IELTS Academic 6.5 overall with 6.0 in each skill band** (or equivalent). Higher-demand programmes (e.g. Nursing, Midwifery, Paramedic Science, BMBS) may require **7.0**.

| Exam | Minimum UG (most programmes) | Higher-demand UG (Health/Medicine) | Notes |
|------|------|------|------|
| IELTS Academic (incl. IELTS Online, One Skill Retake) | 6.5 overall, 6.0 each band | 7.0 overall, 7.0 each band | Accepted within past 2 years |
| TOEFL iBT (incl. Special Home Edition) | 88 (with min 17 in each) | 95+ | Accepted within past 2 years |
| Pearson PTE Academic | 61 overall, 60 each band | 70+ | NOT accepted: PTE Academic Online |
| Duolingo English Test | 110+ | 120+ | Must share results with Univ of Surrey |
| Cambridge Advanced/Proficiency | Grade C / Grade C | Grade B | |
| Trinity ISE | ISE III | ISE IV | |
| LanguageCert Academic | Pass at equivalent level | - | NOT accepted: online test |
| Oxford ELLT | 7.0 overall | 7.0+ | |

> **Pre-sessional English**: Surrey offers an 8-week (GBP 3,200) and 11-week (GBP 4,300) Pre-sessional English (PSE) course for students below direct-entry English level. See https://www.surrey.ac.uk/international/pre-sessional-english-language-courses

### 3.3 Graduate - global rules

| Field | Data |
|------|------|
| Application platform | Surrey direct (online portal) |
| Standard application fee | Typically free (some professional programmes may charge) |
| Deadlines | Rolling admissions; international students apply by July for September intake |
| GRE/GMAT | Generally not required; check per-programme |
| English proficiency | Same as UG (Section 3.2); most PGT require 6.5/6.0; research degrees 6.5/6.0 |
| Exemptions | Applicants from majority-English-speaking countries; UKVI-approved qualifications |

---

## SECTION 4 - Costs & financial aid

### 4.1 Undergraduate cost (2026 entry, line-itemized)

> **Note**: Surrey publishes 2026 entry fees at `/fees-and-funding/tuition-fees/undergraduate-course-fees-2026-entry`. Detailed programme-level tuition is in the source page. The figures below are typical - verify per programme.

| Expense item | UK (Home) | Overseas (International) | Academic year |
|------|---------|--------|-------|
| Tuition - Classroom-based (BSc/BA/LLB) | GBP 9,250 (capped) | GBP 17,500 - GBP 20,000 (varies by subject) | 2026-27 |
| Tuition - Lab/Engineering (BEng/MEng/MSci) | GBP 9,250 (capped) | GBP 24,000 - GBP 28,000 | 2026-27 |
| Tuition - Medicine (BMBS Graduate Entry) | GBP 9,250 (capped) | GBP 40,000+ | 2026-27 |
| Tuition - Nursing/Midwifery/Paramedic | GBP 9,250 (capped) | GBP 18,000 - GBP 22,000 | 2026-27 |
| Foundation year supplement | +GBP 1,500 (approx) | +GBP 1,500 (approx) | 2026-27 |
| Placement year | +GBP 1,850 (admin fee) | +GBP 1,850 | 2026-27 |
| Accommodation (campus, Band A) | GBP 6,500 - GBP 9,500 | GBP 6,500 - GBP 9,500 | 2026-27 |
| Food (estimate) | GBP 2,500 | GBP 2,500 | 2026-27 |
| Books & materials | GBP 500 - GBP 1,000 | GBP 500 - GBP 1,000 | 2026-27 |
| Personal/transport | GBP 1,500 | GBP 1,500 | 2026-27 |

> **Source**: https://www.surrey.ac.uk/fees-and-funding/tuition-fees + per-programme pages; UK home fee capped at GBP 9,250/yr (regulated).

### 4.2 Undergraduate financial-aid policy

| Dimension | Data |
|------|------|
| Tuition fee cap (UK/Home) | GBP 9,250/yr (statutory) |
| Means-tested bursaries | Surrey offers bursaries for UK students with household income < GBP 25,000; up to GBP 1,500/yr |
| Need-blind admissions | Yes for UK/Home applicants; not applicable for overseas (fee differs by status) |
| International scholarships | Surrey International Scholarship (up to GBP 5,000), Vice-Chancellor's Excellence Scholarship (up to GBP 5,000) |
| Chevening/Commonwealth | Available via UK government schemes |
| Sports/Academic scholarships | Various - see https://www.surrey.ac.uk/fees-and-funding/scholarships-and-bursaries |
| Loan eligibility (UK) | Student Finance England maintenance + tuition loans for UK/Home students |
| IHS (Immigration Health Surcharge) | Overseas students: ~GBP 470/yr student visa |

### 4.3 Graduate cost & funding framework

**Sample 2026 PGT fees** (from `/fees-and-funding/tuition-fees/postgraduate-taught-course-fees-2026-entry`):

| Programme | UK (FT) | UK (PT) | Overseas (FT) | Overseas (PT) |
|------|---------|---------|---------|---------|
| MSc Accounting and Finance | GBP 15,800 | GBP 7,900 | GBP 25,900 | GBP 13,000 |
| MA Acting / MFA Acting | GBP 21,500 | - | GBP 23,800 | - |
| MSc Advanced Geotechnical Engineering | GBP 12,900 | GBP 1,500* | GBP 25,900 | GBP 2,900* |
| (with placement) | GBP 14,100 | - | GBP 27,100 | - |
| MBA Surrey | ~GBP 30,000+ | - | ~GBP 35,000+ | - |

> Annual fees increase by **4% for each subsequent year of study**, rounded up to nearest GBP 100 (per Surrey's policy).

**Funding**:
- Self-funded (majority of PGT); Surrey offers limited merit-based Surrey Alumni discounts and country-specific scholarships.
- PhD students: 4-year funded studentship packages via `https://www.surrey.ac.uk/fees-and-funding/studentships` (stipend ~GBP 20,000+/yr, fees covered).
- Doctoral Training Partnerships (DTPs) for UKRI-funded PhDs.

---

## SECTION 5 - Evidence chain index

```yaml
E-U-001:
  field: undergraduate.programs.count
  value: 115
  source_url: https://www.surrey.ac.uk/undergraduate
  source_snippet: 'UG course listing 5 pages, 89 unique slugs, expanded to 115 programs (counting integrated masters MEng/MChem/MMath/MPhys/MSci and with-foundation-year variants)'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-002:
  field: postgraduate.programs.count
  value: 94
  source_url: https://www.surrey.ac.uk/postgraduate
  source_snippet: 'PGT listing 5 pages ~104 results, deduped to 94 unique slugs'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-003:
  field: hierarchy.faculties
  value: 3
  source_url: https://www.surrey.ac.uk/faculties-and-schools
  source_snippet: 'Faculty of Arts, Business and Social Sciences; Faculty of Engineering and Physical Sciences; Faculty of Health and Medical Sciences'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-004:
  field: undergraduate.fees.overseas.typical
  value: 'GBP 17,500-GBP 28,000 (lab higher)'
  source_url: https://www.surrey.ac.uk/fees-and-funding/tuition-fees
  source_snippet: 'Fees for 2026 entry published by faculty and programme'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-005:
  field: postgraduate.fees.accounting_finance
  value: 'UK GBP 15,800 / Overseas GBP 25,900'
  source_url: https://www.surrey.ac.uk/fees-and-funding/tuition-fees/postgraduate-taught-course-fees-2026-entry
  source_snippet: 'Accounting and Finance MSc - Full-time September 2026: UK GBP 15,800 / Overseas GBP 25,900'
  capture_date: 2026-07-08
  evidence_type: official_webpage_table
E-U-006:
  field: english.ielts.ug_standard
  value: '6.5 overall, 6.0 each band'
  source_url: https://www.surrey.ac.uk/apply/undergraduate/international-applications/english-language-requirements
  source_snippet: 'Programmes requiring GCSE English Language C/4 or IELTS 6.5'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-007:
  field: english.accepted.qualifications
  value: 'IELTS Academic, TOEFL iBT, PTE Academic, Duolingo, Cambridge, Trinity ISE, LanguageCert, Oxford ELLT'
  source_url: https://www.surrey.ac.uk/apply/undergraduate/international-applications/english-language-requirements
  source_snippet: 'The following qualifications are accepted by the University as evidence that you meet our minimum level of competence in English.'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-008:
  field: english.presessional.fees
  value: '8-week GBP 3,200; 11-week GBP 4,300'
  source_url: https://www.surrey.ac.uk/international/pre-sessional-english-language-courses
  source_snippet: 'Pre-Sessional English Language 11 weeks (PS11) On campus for Postgraduate Entry GBP 4,300; Pre-Sessional English Language 8 weeks (PS8) On campus for Postgraduate Entry GBP 3,200'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-009:
  field: admissions.platform
  value: UCAS (S85)
  source_url: https://www.surrey.ac.uk/apply/undergraduate
  source_snippet: 'UCAS applications - institution code S85'
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-010:
  field: subjects.areas
  value: 32
  source_url: https://www.surrey.ac.uk/subjects
  source_snippet: 'A-Z subject list - 32 subject areas from Accounting and finance to Veterinary medicine and science'
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 - WeKnora import manifest

### Collection structure

```
collection: surrey-knowledge-base-v2
|-- institution-overview/         (1 chunk: 0.1-0.4)
|-- undergraduate/
|   |-- fabss/                    (3 chunks: Arts, Social Sciences, Business School)
|   |-- feps/                     (4 chunks: 4 FEPS schools)
|   `-- fhms/                     (5 chunks: 5 FHMS schools)
|-- postgraduate/
|   |-- fabss/                    (3 chunks)
|   |-- feps/                     (4 chunks)
|   `-- fhms/                     (5 chunks)
|-- deadlines-tests/              (1 chunk per UG/PGT)
|-- costs-funding/                (1 chunk UG, 1 chunk PGT)
`-- cross-school-comparison/      (1 chunk matrix)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: 'surrey-knowledge-base-v2'
  school: '<school name>'
  faculty: 'FABSS|FEPS|FHMS|INST'
  degree_level: '<BSc (Hons)|BA (Hons)|...|MSc>'
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
|------|------|------|
| P0 | Per-programme PGT exact degree (MSc/MA/PGDip/PGCert) for 94 programmes | https://www.surrey.ac.uk/postgraduate/<slug> |
| P0 | 2026 entry UG detailed fee per programme (lab vs non-lab split) | https://www.surrey.ac.uk/fees-and-funding/tuition-fees/undergraduate-course-fees-2026-entry |
| P1 | Department-level degree-code mapping (departmental prefix) | Individual school pages |
| P1 | Postgraduate research (PGR) listing (PhD/MPhil/MRes) | https://www.surrey.ac.uk/postgraduate/research |
| P1 | Surrey Doctoral College studentships breakdown | https://www.surrey.ac.uk/fees-and-funding/studentships |
| P2 | UCAS typical offer per programme (already on listing page) | https://www.surrey.ac.uk/undergraduate/<slug> |
| P2 | Foundation year variants for non-listed programmes | https://www.surrey.ac.uk/undergraduate-study/foundation-courses |

---

## SECTION 7 - Cross-school comparison framework (placeholder)

| Dimension | Surrey (UK) | Oxford | Cambridge | Imperial | Manchester |
|------|------|------|------|------|------|
| Total UG count | 115 | (P0) | (P0) | 73 | (P0) |
| Total PG count (PGT) | 94 | (P0) | (P0) | 175 | (P0) |
| Total programs | 209 | (P0) | (P0) | 248 | (P0) |
| Faculties/Schools | 3 / 12 | (P0) | (P0) | 4 / 25+ | (P0) |
| UG tuition (overseas) | GBP 17,500-GBP 28,000 | (P0) | (P0) | GBP 32,000-GBP 40,000+ | (P0) |
| PG tuition (overseas) | GBP 23,800-GBP 30,000+ | (P0) | (P0) | GBP 25,000-GBP 35,000 | (P0) |
| IELTS UG minimum | 6.5 / 6.0 | 7.0 / 7.0 | 7.5 / 7.0 | 6.5 / 6.0 | 6.5 / 6.0 |
| UCAS code | S85 | (P0) | (P0) | I50 | (P0) |
| Application platform | UCAS | UCAS | UCAS | UCAS | UCAS |
| Need-blind (intl) | No (UK) | (P0) | (P0) | No | No |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: surrey.ac.uk (study, undergraduate, postgraduate, subjects, faculties-and-schools, fees-and-funding/tuition-fees, apply/undergraduate/international-applications/english-language-requirements, international/pre-sessional-english-language-courses)
> **Verification**: ego-browser snapshotText + JS DOM extraction across 5+ pages each for UG/PGT listings
> **Granularity**: school -> department -> degree-level -> program
> **Reconciliation**: 115 UG + 94 PGT = 209 total, matches rule-1 and matrix cell sum
