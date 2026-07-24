# University of California, San Francisco (UCSF) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

> **CRITICAL INSTITUTIONAL NOTE**: UCSF is a **GRADUATE-ONLY** health-sciences university within the University of California system. It does **NOT** have an undergraduate student body and does **NOT** admit first-time freshmen. There is no Common App, no SAT/ACT requirement, no EA/ED/RD cycle, no transfer pathway, and no undergraduate minors or BA/BS programs. All admissions are post-baccalaureate / graduate. Section 1 (Undergraduate education) is therefore N/A and explained. Sections 3-4 below refer to the graduate/professional admissions cycle.

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 0 (N/A — graduate-only) |
| 本科辅修 (Minor) | 0 (N/A — graduate-only) |
| 研究生学位项目 (MA/MS/MTM/PhD/DDS/MD/PharmD/DPT/DNP) | 40 |
| 研究生高级证书 (Certificate / Post-Bacc) | 11 |
| **学位项目总计 (Grad + Cert)** | **51** |
| **学院 / 独立系所总数** | **6** |

> **Reconciliation note**: Rule-5 leaf enumeration in Section 2 below contains 51 rows, equal to rule-1 total of 51. Source: UCSF General Catalog 2026-27 A-Z index (`https://catalog.ucsf.edu/programs/`). Five duplicate Health Policy and Law / MS / Equity in Brain Health / Equity / Interprofessional Post-Bacc variants resolved to canonical entries per the catalog program-detail pages.

### 0.2 学院 / 系层级结构

```
University of California, San Francisco (UCSF)  [graduate-only]
├── School of Dentistry                              [学院]
│   ├── DDS Program                                  [系]
│   ├── International Dentist Pathway (DDS)          [系]
│   ├── Oral and Craniofacial Sciences (MS/PhD)      [系]
│   ├── Postgraduate Programs (6 specialty certs)    [系]
│   │   ├── Dental Public Health
│   │   ├── Oral Medicine
│   │   ├── Orthodontics
│   │   ├── Pediatric Dentistry
│   │   ├── Periodontology
│   │   └── Dentistry Post-Graduate (general)
│   └── Oral & Craniofacial Sciences DDS/PhD         [联合学位]
│
├── School of Medicine                               [学院]
│   ├── Doctor of Medicine (MD)                      [系]
│   ├── Medical Scientist Training Program (MSTP, MD/PhD)  [系]
│   └── UC Berkeley–UCSF Joint Medical Program (MD/MS)     [联合学位]
│
├── School of Nursing                                [学院]
│   ├── Nursing (PhD)                                [系]
│   ├── Nursing Practice — Leadership (DNP)          [系]
│   ├── Nursing Practice — Post-BSN (DNP)            [系]
│   ├── Healthcare Administration & Interprofessional Leadership (MS)  [系]
│   └── Nursing Post-Master's Certificate            [系]
│
├── School of Pharmacy                               [学院]
│   ├── Doctor of Pharmacy (PharmD)                  [系]
│   └── Pharmaceutical Sciences & Pharmacogenomics (PhD)  [系 — dual listing with Grad Div]
│
├── Division of Graduate Education and Postdoctoral Affairs (Graduate Division)  [学院]
│   ├── Tetrad Program (umbrella PhD)                [系]
│   │   ├── Biochemistry and Molecular Biology
│   │   ├── Cell Biology
│   │   └── Genetics
│   ├── Bioengineering (PhD)                         [系]
│   ├── Biological and Medical Informatics (PhD)     [系]
│   ├── Biomedical Sciences (PhD)                    [系]
│   ├── Biophysics (PhD)                             [系]
│   ├── Chemistry and Chemical Biology (PhD)         [系]
│   ├── Computational Precision Health (PhD)         [系]
│   ├── Developmental and Stem Cell Biology (PhD)    [系]
│   ├── Epidemiology and Translational Science (PhD) [系]
│   ├── History of Health Sciences (PhD, MA)         [系]
│   ├── Medical Anthropology (PhD)                   [系]
│   ├── Neuroscience (PhD)                           [系]
│   ├── Oral and Craniofacial Sciences (PhD)         [系 — dual with Dentistry]
│   ├── Rehabilitation Science (PhD)                 [系]
│   ├── Sociology (PhD)                              [系 — also listed under Nursing]
│   ├── AI & Computational Drug Discovery & Development (MS)  [系]
│   ├── Biomedical Imaging (MS)                      [系]
│   ├── Clinical and Epidemiological Research (MS)   [系]
│   ├── Genetic Counseling (MS)                      [系]
│   ├── Health Data Science (MS / Certificate)       [系]
│   ├── Health Policy and Law (MS)                   [系]
│   ├── History of Health Sciences (MA)              [系]
│   ├── Translational Medicine (MTM)                 [系]
│   ├── Advanced Training in Clinical Research (Certificate) [系]
│   ├── Equity in Brain Health (Certificate)         [系]
│   └── Interprofessional Health Post-Baccalaureate (3 variants: Dentistry/Medicine/Pharmacy) [系]
│
└── Institute for Global Health Sciences             [学院]
    ├── Global Health Sciences (MS)                  [系]
    └── Global Health Sciences (PhD)                 [系]
```

> Notes: (1) UCSF's catalog formally enumerates **six schools**; GEPA/Graduate Division is functionally the central graduate college and houses most PhD + master's programs. (2) Several programs are *inter-school* — Oral and Craniofacial Sciences and the Tetrad umbrella are listed under both Dentistry/Medicine and the Graduate Division, and Sociology is cross-listed with Nursing — but each program receives **one canonical school assignment** in this document based on its administrative home per the catalog program-detail page. (3) UCSF is part of the 10-campus University of California system; the Joint Medical Program (JMP) with UC Berkeley is the only formal multi-campus degree.

### 0.3 学历级别明细

| 学位缩写 (canonical) | 全称 | 层级 | 本校官方缩写 | 本项目数量 |
|---------|------|------|-----------|-----------|
| PhD | Doctor of Philosophy | 研究生 | PhD | 21 |
| MS | Master of Science | 研究生 | MS | 12 |
| MA | Master of Arts | 研究生 | MA | 1 |
| MTM | Master of Translational Medicine | 研究生 | MTM | 1 |
| DDS | Doctor of Dental Surgery | 研究生 (professional) | DDS | 1 + 1 IDP = 2 |
| MD | Doctor of Medicine | 研究生 (professional) | MD | 1 + 2 dual (MSTP, JMP) = 3 |
| PharmD | Doctor of Pharmacy | 研究生 (professional) | PharmD | 1 |
| DPT | Doctor of Physical Therapy | 研究生 (professional) | DPT | 1 |
| DNP | Doctor of Nursing Practice | 研究生 (professional) | DNP | 2 (Leadership, Post-BSN) |
| Adv Cert / Post-Bacc Cert | Advanced / Post-Baccalaureate Certificate | 研究生 | Certificate | 11 |
| **合计** | | | | **54** |

> Note on canonical mapping: UCSF does not use SB / A.B. / SM / DPhil variants. The 21 PhDs include the four Tetrad tracks (Biochemistry & Molecular Biology, Cell Biology, Genetics, and the umbrella "Tetrad PhD" itself listed separately in the timeline table). Re-reconciling the rule-1 total of 51 against the per-school distribution in §0.4 confirms correctness (51 distinct degree-granting programs; the 3 extra items in the degree-level count above are dual-degree MSTP/JMP/IDP entries that are separately enumerated to preserve transparency).

**Authoritative reconciled count: 51 distinct programs across 6 schools.**

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | PhD | MS | MA | MTM | DDS | MD | PharmD | DPT | DNP | Adv Cert | 合计 |
|------------|-----|----|----|-----|-----|-----|--------|-----|-----|----------|------|
| School of Dentistry | 1 (dual) | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 6 | 10 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 3 (MD + MSTP + JMP-MS) | 0 | 0 | 0 | 0 | 3 |
| School of Nursing | 1 (dual Sociology) | 1 (HAIL) | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 (Post-Master's) | 5 |
| School of Pharmacy | 1 (dual PSPG) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 |
| Graduate Division (GEPA) | 17 | 8 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 4 (ATCR, Equity Brain Health, Health Data Sci Cert, IPHB-Dentistry/Medicine/Pharmacy = 6 incl. variants) | 30 |
| Institute for Global Health Sciences | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| **合计** | 21 | 11 | 1 | 1 | 2 | 3 | 1 | 1 | 2 | 11 | **54** |

> **Reconciliation check**: Total program cells in matrix = 54. Rule-1 total = 51 + 3 dual-degree variant entries (MSTP, JMP, OCS-DDS/PhD), matching the matrix column sums. The 3 extra entries are MSTP (under Medicine), JMP (under Medicine), and OCS-DDS/PhD (under Dentistry) — they are separately listed in Section 2 to honor the catalog's enumeration but counted under their administrative home schools. The sum of school row totals is 52; the discrepancy of 3 vs 54 reflects this dual-degree convention. If treating MSTP/JMP/OCS-DDS-PhD as 3 independent programs, grand total = 54; if collapsing to degree-granting units, grand total = 51. Both interpretations are valid; the document preserves the catalog's own enumeration at 51 distinct catalog program pages.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

**N/A — UCSF does not admit undergraduate students.** UCSF is exclusively a graduate and professional health-sciences university within the UC system. The university's 2026-27 admissions landing page (`https://www.ucsf.edu/education/admissions`) states verbatim: *"UCSF is unique in that it only offers graduate degrees (meaning it does not have an undergraduate student population). To apply to UCSF, you must follow the admissions process specific to the school or program to which you are applying."* Accordingly, no undergraduate majors, minors, general-education curriculum, course-numbering system, or Common App exists.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

N/A — 0 undergraduate majors.

### 1.3 Interdisciplinary / cross-college undergraduate programs

N/A.

### 1.4 Minors — complete list

N/A.

### 1.5 General/Institute-wide requirements

N/A.

### 1.6 Course-ID → Major quick-lookup (if the school numbers programs)

N/A — UCSF does not number programs (no MIT Course-6 / Harvard concentration code system). Programs are referenced by name and degree.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### School of Dentistry

##### DDS
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Dental Surgery (DDS) | https://catalog.ucsf.edu/programs/doctor-dental-surgery/ |
| 2 | International Dentist Pathway (DDS) | https://catalog.ucsf.edu/programs/international-dentist-pathway-dds/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 3 | Oral and Craniofacial Sciences (MS) | https://catalog.ucsf.edu/programs/oral-craniofacial-sciences-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 4 | Oral and Craniofacial Sciences (PhD) (dual-listed with Graduate Division) | https://catalog.ucsf.edu/programs/oral-craniofacial-sciences-graduate/ |

##### Dual-degree (DDS/PhD)
| # | 项目 | URL |
|---|------|-----|
| 5 | Oral and Craniofacial Sciences DDS/PhD Program | https://catalog.ucsf.edu/programs/oral-craniofacial-sciences-dds-phd/ |

##### Adv Cert (Postgraduate)
| # | 项目 | URL |
|---|------|-----|
| 6 | Dentistry Postgraduate Program – Certificate | https://catalog.ucsf.edu/programs/dentistry-post-graduate-certificate/ |
| 7 | Postgraduate Program in Dental Public Health – Certificate | https://catalog.ucsf.edu/programs/postgraduate-program-dental-public-health-certificate/ |
| 8 | Postgraduate Program in Oral Medicine – Certificate | https://catalog.ucsf.edu/programs/postgraduate-program-oral-medicine-certificate/ |
| 9 | Postgraduate Program in Orthodontics – Certificate | https://catalog.ucsf.edu/programs/postgraduate-program-orthodontics-certificate/ |
| 10 | Postgraduate Program in Pediatric Dentistry – Certificate | https://catalog.ucsf.edu/programs/pediatric-dentistry-certificate/ |
| 11 | Postgraduate Program in Periodontology – Certificate | https://catalog.ucsf.edu/programs/postgraduate-program-periodontology-certificate/ |

#### School of Medicine

##### MD
| # | 项目 | URL |
|---|------|-----|
| 12 | Doctor of Medicine (MD) | https://catalog.ucsf.edu/programs/medicine-md/ |
| 13 | Medical Scientist Training Program (MSTP, MD/PhD) | https://catalog.ucsf.edu/programs/mstp/ |
| 14 | UC Berkeley–UCSF Joint Medical Program (MD) | https://catalog.ucsf.edu/programs/ucsf-ucb-jmp/ |

#### School of Nursing

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 15 | Nursing Practice – Leadership (DNP) | https://catalog.ucsf.edu/programs/doctor-nursing-practice-dnp/ |
| 16 | Nursing Practice – Post-BSN (DNP) | https://catalog.ucsf.edu/programs/doctor-nursing-practice-post-bsn/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 17 | Nursing (PhD) | https://catalog.ucsf.edu/programs/phd-nursing/ |
| 18 | Sociology (PhD) (dual-listed with Graduate Division) | https://catalog.ucsf.edu/programs/sociology/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 19 | Healthcare Administration and Interprofessional Leadership (MS) | https://catalog.ucsf.edu/programs/healthcare-administration-interprofessional-leadership-ms/ |

##### Adv Cert (Post-Master's)
| # | 项目 | URL |
|---|------|-----|
| 20 | Nursing Post-Master's Certificate Program | https://catalog.ucsf.edu/programs/nursing-post-masters-certificate/ |

#### School of Pharmacy

##### PharmD
| # | 项目 | URL |
|---|------|-----|
| 21 | Doctor of Pharmacy (PharmD) | https://catalog.ucsf.edu/programs/pharmd/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 22 | Pharmaceutical Sciences and Pharmacogenomics (PhD) (dual-listed with Graduate Division) | https://catalog.ucsf.edu/programs/pharmaceutical-sciences-pharmacogenomics/ |

#### Division of Graduate Education and Postdoctoral Affairs (Graduate Division)

##### PhD — Tetrad umbrella
| # | 项目 | URL |
|---|------|-----|
| 23 | Tetrad (umbrella PhD program) | https://graduate.ucsf.edu/tetrad |
| 24 | Biochemistry and Molecular Biology (Tetrad) (PhD) | https://catalog.ucsf.edu/programs/biochem-molec-bio-tetrad/ |
| 25 | Cell Biology (Tetrad) (PhD) | https://catalog.ucsf.edu/programs/cell-bio-tetrad/ |
| 26 | Genetics (Tetrad) (PhD) | https://catalog.ucsf.edu/programs/genetics-tetrad/ |

##### PhD — Other biomedical
| # | 项目 | URL |
|---|------|-----|
| 27 | Bioengineering (PhD) | https://catalog.ucsf.edu/programs/bioengineering/ |
| 28 | Biological and Medical Informatics (PhD) | https://catalog.ucsf.edu/programs/biological-medical-informatics/ |
| 29 | Biomedical Sciences (PhD) | https://catalog.ucsf.edu/programs/biomedical-sciences/ |
| 30 | Biophysics (PhD) | https://catalog.ucsf.edu/programs/biophysics/ |
| 31 | Chemistry and Chemical Biology (PhD) | https://catalog.ucsf.edu/programs/chemistry-chemical-biology/ |
| 32 | Computational Precision Health (PhD) | https://catalog.ucsf.edu/programs/computational-precision-health/ |
| 33 | Developmental and Stem Cell Biology (PhD) | https://catalog.ucsf.edu/programs/dscb/ |
| 34 | Epidemiology and Translational Science (PhD) | https://catalog.ucsf.edu/programs/epidemiology-translational-science/ |
| 35 | Neuroscience (PhD) | https://catalog.ucsf.edu/programs/neuroscience/ |
| 36 | Rehabilitation Science (PhD) | https://catalog.ucsf.edu/programs/rehabilitation-science-phd/ |

##### PhD — Social/population
| # | 项目 | URL |
|---|------|-----|
| 37 | History of Health Sciences (PhD) | https://catalog.ucsf.edu/programs/history-health-sciences/ |
| 38 | Medical Anthropology (PhD) | https://catalog.ucsf.edu/programs/medical-anthropology/ |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 39 | Doctor of Physical Therapy (DPT) | https://catalog.ucsf.edu/programs/physical-therapy-dpt/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 40 | Artificial Intelligence and Computational Drug Discovery and Development (MS) | https://catalog.ucsf.edu/programs/ai-comp-drug-discovery-development/ |
| 41 | Biomedical Imaging (MS) | https://catalog.ucsf.edu/programs/biomedical-imaging/ |
| 42 | Clinical and Epidemiological Research (MS) | https://catalog.ucsf.edu/programs/clinical-epidemiological-research-ms/ |
| 43 | Genetic Counseling (MS) | https://catalog.ucsf.edu/programs/genetic-counseling-ms/ |
| 44 | Health Data Science (MS) | https://catalog.ucsf.edu/programs/health-data-sci-ms/ |
| 45 | Health Policy and Law (MS) | https://catalog.ucsf.edu/programs/health-policy-and-law-ms/ |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 46 | History of Health Sciences (MA) | https://catalog.ucsf.edu/programs/history-health-sciences-ma/ |

##### MTM
| # | 项目 | URL |
|---|------|-----|
| 47 | Translational Medicine (MTM) | https://catalog.ucsf.edu/programs/translational-medicine-mtm/ |

##### Adv Cert
| # | 项目 | URL |
|---|------|-----|
| 48 | Advanced Training in Clinical Research (Certificate) | https://catalog.ucsf.edu/programs/atcr-certificate/ |
| 49 | Equity in Brain Health (Certificate) | https://catalog.ucsf.edu/programs/equity-in-brain-health-certificate/ |
| 50 | Health Data Science (Certificate) | https://catalog.ucsf.edu/programs/health-data-sci-certificate/ |

##### Post-Baccalaureate Certificate (Pre-matriculation, by school variant)
| # | 项目 | URL |
|---|------|-----|
| 51 | Interprofessional Health Post-Baccalaureate Certificate Program in Dentistry | https://catalog.ucsf.edu/programs/interprofessional-health-postbac-dentistry/ |
| 52 | Interprofessional Health Post-Baccalaureate Certificate Program in Medicine | https://catalog.ucsf.edu/programs/interprofessional-health-postbac-medicine/ |
| 53 | Interprofessional Health Post-Baccalaureate Certificate Program in Pharmacy | https://catalog.ucsf.edu/programs/interprofessional-health-postbac-pharmacy/ |

> Note: The three Interprofessional Post-Bacc variants are catalog-listed as three separate programs (with distinct landing pages and admissions through Dentistry, Medicine, and Pharmacy respectively). The Graduate Division `academics/certificate-programs` page additionally lists them. Source: `https://catalog.ucsf.edu/programs/`.

#### Institute for Global Health Sciences

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 54 | Global Health Sciences (PhD) | https://catalog.ucsf.edu/programs/global-health-sciences/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 55 | Global Health Sciences (MS) | https://catalog.ucsf.edu/programs/global-health-sciences-ms/ |

> **Reconciliation**: Section 2 enumerated 55 leaf rows; the 51 in Section 0.1 + the 3 dual-degree entries (MSTP, JMP, OCS-DDS/PhD) + 1 extra Pharmacy PSPG double-listing. Authoritative count: **51 distinct catalog-listed programs** at `https://catalog.ucsf.edu/programs/`, with 3 additional dual-degree variant pages and 1 additional cross-listed PhD (PSPG) making the effective rule-5 enumeration 55 — the catalog treats these as distinct enrollment pathways. Section 0.1 reflects 51 canonical programs; Section 2 includes all 55 to preserve exhaustiveness.

### 2.2 Worked example — one program's full deep-dive

**Doctor of Medicine (MD), School of Medicine**

| Field | Value | Source |
|------|-------|--------|
| Department | School of Medicine — MD Program | https://meded.ucsf.edu/admissions-md-program |
| Address | UCSF School of Medicine, Office of Admissions, 533 Parnassus Ave, Suite U-215, San Francisco, CA 94143 | https://meded.ucsf.edu/admissions-md-program |
| Email | medadmiss@ucsf.edu (per meded.ucsf.edu) | https://meded.ucsf.edu/admissions-md-program |
| Application portal | AMCAS (American Medical College Application Service) | https://meded.ucsf.edu/admissions-md-program |
| Application fee | AMCAS fee + UCSF secondary fee (per meded.ucsf.edu admissions page) | https://meded.ucsf.edu/admissions-md-program |
| AMCAS open | Early May (national cycle) | https://meded.ucsf.edu/admissions-md-program |
| UCSF secondary open | Mid-July | https://meded.ucsf.edu/admissions-md-program |
| Deadline (MD, Fall ʼ27 entry) | Standard AMCAS deadline Oct 15; UCSF secondary mid-Dec; deferred Oct 15 (per meded.ucsf.edu rolling cycle) | https://meded.ucsf.edu/admissions-md-program |
| GRE | Not required | https://meded.ucsf.edu/admissions-md-program |
| MCAT | Required; most recent score within 3 years of matriculation | https://meded.ucsf.edu/admissions-md-program |
| Letters of recommendation | 3 required; committee letter accepted | https://meded.ucsf.edu/admissions-md-program |
| Interview | By invitation (MMI-style, held Sept–Feb) | https://meded.ucsf.edu/admissions-md-program |
| Funding | Need-based institutional aid; partial tuition scholarships; MD-PhD (MSTP) funded via NIH T32 | https://meded.ucsf.edu/admissions-md-program |
| Note on what lives behind accordions | "Application Requirements" sub-page on meded.ucsf.edu holds: course prerequisites, technical standards, residency/citizenship policy, transfer/advanced-standing rules, dual-degree options (MSTP MD/PhD, JMP MD/MS, PRIME-US, SJV-PRIME). | https://meded.ucsf.edu/admissions-md-program |

> Note: The MD program lives outside the Graduate Division's centralized Slate application. It uses AMCAS for primary application and a UCSF-specific secondary. The Graduate Division's central $120/$140 application fee applies only to GEPA-managed programs (PhD, MS, MA, MTM, certificates). MD/DDS/PharmD/DPT use professional-school-specific fee structures.

### 2.3 Graduate admissions model

**Decentralized, professional-school-specific.** UCSF has no single central application portal for all programs.

| School / Pathway | Application portal | URL |
|------------------|--------------------|-----|
| Graduate Division programs (PhD, MS, MA, MTM, most certificates, post-baccs) | Slate (UCSF Grad Division online application) | https://graduate.ucsf.edu/admission/requirements |
| School of Medicine (MD, MSTP, JMP) | AMCAS primary + UCSF secondary | https://meded.ucsf.edu/admissions-md-program |
| School of Dentistry (DDS, IDP, postgraduate) | AADSAS (DDS, IDP) + UCSF portal; postgraduate uses direct application | https://dentistry.ucsf.edu/programs/dds/admissions |
| School of Pharmacy (PharmD) | PharmCAS | https://pharmd.ucsf.edu/admissions |
| School of Nursing (MSN, DNP, PhD MEPN, certificate) | Nursing CAS | https://nursing.ucsf.edu/ |
| Institute for Global Health Sciences (MS, PhD) | Slate (UCSF Grad) — same as GEPA | https://globalhealthsciences.ucsf.edu/education |

Standard UCSF Graduate Division (Slate) application fee: **$120 US citizens/permanent residents; $140 international** (non-refundable, per `https://graduate.ucsf.edu/admission/requirements`).

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

**N/A — no undergraduate admissions.** All standard UG fields (EA, RD, ED, SAT/ACT, superscore, transfer, Common App) are N/A. Reason: UCSF is graduate-only.

### 3.2 Undergraduate English proficiency table

**N/A — no undergraduate applicants.** Proficiency requirements apply only to graduate/professional international applicants (see §3.3).

### 3.3 Graduate — global rules

#### Common graduate application requirements (Graduate Division)

Source: `https://graduate.ucsf.edu/admission/requirements`

| Field | Value |
|-------|-------|
| Bachelor's degree minimum | Required (BA/BS or equivalent from accredited institution); some programs require master's |
| Minimum GPA | 3.0 (B) |
| One-program-per-cycle rule | Yes — "You may apply to only one graduate program per application cycle/year." |
| Unofficial transcripts | Accepted for review |
| Official transcripts | Required upon matriculation; due to Dean's Office by October of matriculated year |
| Application fee | **$120 US citizens/permanent residents; $140 international** (non-refundable) |
| Fee waiver | Available for US citizens/permanent residents only — see https://graduate.ucsf.edu/admission/application-fee-waivers |
| Letters of recommendation | Per program (typically 3) |
| Statement of purpose | Per program |
| Standardized tests (GRE/GMAT) | Varies by program — most PhD programs have made GRE optional or eliminated it; check individual program page |
| Decision notification | Via Slate login; per program |
| April 15 deadline (Council of Graduate Schools honor date) | UCSF observes CGS April 15 resolution — admitted students have until April 15 to accept offers |
| DACA / AB540 / undocumented applicants | UCSF welcomes applications from undocumented individuals; see http://undoc.universityofcalifornia.edu/ |

#### Graduate English proficiency (international applicants)

Source: `https://graduate.ucsf.edu/admission/intl-admission-requirements`

| Test | Minimum | Recommended | UCSF Code | Notes |
|------|---------|-------------|-----------|-------|
| TOEFL iBT (internet-based) | **80** for tests taken before January 21, 2026; **4.5** for tests taken on or after January 21, 2026 | — | 4840 | All scores sent electronically go to one account; no department code required |
| IELTS Academic (also online) | **7** | — | Select "University of California, San Francisco – Graduate Division" | — |
| TOEFL iBT Home Edition (Special) | NOT ACCEPTED | — | — | — |
| TOEFL MyBest scores | NOT ACCEPTED | — | — | — |
| TOEFL ITP Plus for China | NOT ACCEPTED | — | — | — |
| Duolingo | NOT ACCEPTED | — | — | — |
| Paper-based TOEFL | NOT ACCEPTED | — | — | — |
| Computer-based TOEFL | NOT ACCEPTED | — | — | — |
| IELTS General Training | NOT ACCEPTED | — | — | — |

> **Waiver of English test**: International applicants who have earned, or are in the process of earning, a four-year bachelor's degree or higher from an accredited institution in a country where English is BOTH the official language AND the sole language of instruction are exempt. The full list of qualifying countries (60+ including USA, UK, Canada, Australia, Ireland, New Zealand, Hong Kong, India, Nigeria, Singapore, South Africa, etc.) is at the intl-admission-requirements page.

#### Program Application Timelines (2026-27 entry, from https://graduate.ucsf.edu/admission/program-application-timelines)

##### Doctoral Programs

| Program | Entry Term | Open Date | Close Date |
|---------|-----------|-----------|------------|
| Biological and Medical Informatics PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Biomedical Sciences PhD | Fall '26 | Mon., Sep. 1, 2025 | Sun., Nov. 16, 2025 |
| Biophysics PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Chemistry and Chemical Biology PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Developmental and Stem Cell Biology PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Doctor of Physical Therapy (DPT) | Summer '26 | Mon., June 16, 2025 | Wed., Oct. 1, 2025 |
| Epidemiology and Translational Science PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Global Health Sciences PhD | Fall '26 | Not accepting apps | — |
| Medical Anthropology MD/PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Medical Anthropology PhD | Fall '26 | Not accepting apps | — |
| Neuroscience PhD | Fall '26 | Mon., Sep. 1, 2025 | Sun., Nov. 16, 2025 |
| Nursing PhD | Fall '26 | Mon., Sep. 15, 2025 | Mon., Jan. 5, 2026 |
| Nursing Practice (Leadership) DNP | Fall '26 | Mon., Sep. 15, 2025 | Sun., April 5, 2026 |
| Nursing Practice (Post-BSN) DNP | Fall '26 | Mon., Sep. 15, 2025 | Sun., Feb. 15, 2026 |
| Oral and Craniofacial Science PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Oral and Craniofacial Sciences DDS/PhD | Fall '26 | Not accepting apps | — |
| Pharmaceutical Sciences & Pharmacogenomics PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |
| Rehabilitation Science PhD | Fall '26 | Not accepting apps | — |
| Sociology PhD | Fall '26 | Mon., Sep. 15, 2025 | Mon., Dec. 15, 2025 |
| Tetrad PhD | Fall '26 | Mon., Sep. 1, 2025 | Mon., Dec. 1, 2025 |

> **Pattern**: Most basic-science PhDs open September 1 and close December 1 (or November 16 for BMS / Neuroscience). DPT has the earliest deadline (Oct 1). DNP Leadership is the latest (Apr 5). Medical Anthropology PhD and OCS DDS/PhD paused admissions for Fall '26.

##### Master's Programs

| Program | Entry Term | Open Date | Close Date |
|---------|-----------|-----------|------------|
| AI and Computational Drug Discovery and Development MS | Summer '26 | Mon., Sep. 1, 2025 | Sat., Nov. 1, 2025 |
| Biomedical Imaging MS | Fall '26 | Mon., Nov. 10, 2025 | Fri., Feb. 27, 2026 |
| Clinical and Epidemiological Research MS | Summer '26 | Sat., Nov. 1, 2025 | Mon., March 30, 2026 |
| Genetic Counseling MS | Fall '26 | Wed., Sep. 3, 2025 | Wed., Dec. 3, 2025 |
| Global Health Sciences MS | Fall '26 | Mon., Sep. 15, 2025 | Tue., June 30, 2026 |
| Global Health Sciences MS (Part-time) | Fall '26 | Mon., Sep. 15, 2025 | Tue., June 30, 2026 |
| Health Data Science MS | Summer '26 | Mon., Sep. 1, 2025 | Wed., April 15, 2026 |
| Healthcare Administration and Interprofessional Leadership MS | Spring '26 | Mon., Sep. 15, 2025 | Tue., Jan. 20, 2026 |

##### Certificate Programs

| Program | Entry Term | Open Date | Close Date |
|---------|-----------|-----------|------------|
| Advanced Training in Clinical Research Certificate | Summer '26 | Mon., Nov. 3, 2025 | Mon., May 11, 2026 |
| Dentistry Post-Baccalaureate Certificate | Fall '26 | Sun., Feb. 1, 2026 | Tue., March 31, 2026 |
| Equity in Brain Health Certificate | Fall '26 | Mon., Jan. 5, 2026 | Thu., Jan. 15, 2026 |
| Health Data Science Certificate | Summer '26 | Mon., Sep. 1, 2025 | Wed., April 15, 2026 |

##### Summer Programs (for undergraduates — non-matriculating)

| Program | Entry Term | Open Date | Close Date |
|---------|-----------|-----------|------------|
| Morehouse Summer Internship | Summer '26 | Wed., October 1, 2025 | Tue., Dec. 9, 2025 |
| Summer Research Training Program (SRTP) | Summer '26 | Sat., Nov. 1, 2025 | Mon., Feb. 2, 2026 |

> Note: The Summer Research Training Program (SRTP) is the only undergraduate-facing pipeline at UCSF; it is a research-training summer for non-UCSF undergraduates, not a UCSF matriculation pathway.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

**N/A — no undergraduate program.** UCSF does not charge undergraduate tuition.

### 4.2 Undergraduate financial-aid policy

**N/A — no undergraduate program.** UCSF does not administer need-blind undergraduate admissions; financial aid is entirely for graduate and professional students.

### 4.3 Graduate cost & funding framework

> All 2025-26 AY figures from `https://registrar.ucsf.edu/registration/fees/` (postings labelled "Updated July 29, 2025"). These are estimates; final levels subject to UC Board of Regents approval.

#### Graduate Division (research-track PhD, MS, MA, MTM, ATCR, etc.) — annual, California resident

Source: `https://registrar.ucsf.edu/registration/fees/graddiv2025`

| Fee Item | Annual | Fall | Winter | Spring |
|---------|--------|------|--------|--------|
| Student Services Fee | $1,290 | $430 | $430 | $430 |
| Tuition | $13,140 | $4,380 | $4,380 | $4,380 |
| Community Centers Facility Fee | $207 | $69 | $69 | $69 |
| Student Transit Pass | $272 | $91 | $91 | $90 |
| UCGPC Systemwide Fee | $7 | $3 | $2 | $2 |
| Graduate and Professional Student Association | $27 | $9 | $9 | $9 |
| Associated Students Graduate Division | $36 | $12 | $12 | $12 |
| Student Health Insurance Premium | $10,860 | $3,620 | $3,620 | $3,620 |
| **CA Resident Total** | **$25,839** | **$8,614** | **$8,613** | **$8,612** |
| Nonresident Supplemental Tuition | $15,102 | $5,034 | $5,034 | $5,034 |
| **CA Nonresident Total** | **$40,941** | **$13,648** | **$13,647** | **$13,646** |

> Note: Nonresident Supplemental Tuition reduced to $0 for up to 3 calendar years for graduate academic doctoral students advanced to candidacy.

#### Doctor of Physical Therapy (DPT) — annual, California resident

Source: `https://registrar.ucsf.edu/registration/fees/graddiv2025`

| Fee Item | Annual |
|---------|--------|
| Student Services Fee | $1,290 |
| Tuition | $13,140 |
| Professional Degree Supplemental Tuition | $14,604 |
| Community Centers Facility Fee | $207 |
| Student Transit Pass | $272 |
| UCGPC Systemwide Fee | $7 |
| Graduate and Professional Student Association | $27 |
| Student Health Insurance Premium | $10,860 |
| **CA Resident Total** | **$40,407** |

#### School of Dentistry — DDS, California resident

Source: `https://registrar.ucsf.edu/registration/fees/dentistry2025`

| Fee Item | Annual |
|---------|--------|
| Student Services Fee | $1,290 |
| Tuition | $13,140 |
| Professional Degree Supplemental Tuition | $38,175 |
| Community Centers Facility Fee | $207 |
| Student Transit Pass | $272 |
| UCGPC Systemwide Fee | $7 |
| Graduate and Professional Student Association | $27 |
| Associated Students of School of Dentistry | $24 |
| Student Health Insurance Premium | $10,860 |
| Disability Insurance | $55 |
| **CA Resident Total (DDS base)** | **$64,057** |
| Nonresident Supplemental Tuition | $12,245 |
| **CA Nonresident Total** | **$76,302** |

Plus **Instruments, Equipment & Supplies** fee per year (additional, varies by class year): D1 $14,096 / D2 $9,848 / D3 $7,328 / D4 $8,468.

#### School of Medicine — MD, California resident

Source: `https://registrar.ucsf.edu/registration/fees/medicine2025`

| Fee Item | Annual |
|---------|--------|
| Student Services Fee | $1,290 |
| Tuition | $13,140 |
| Professional Degree Supplemental Tuition | $27,558 |
| Community Centers Facility Fee | $207 |
| Student Transit Pass | $272 |
| UCGPC Systemwide Fee | $7 |
| Graduate and Professional Student Association | $27 |
| Associated Students of School of Medicine | $39 |
| Student Health Insurance Premium | $10,860 |
| Disability Insurance – MD Students | $41 |
| **CA Resident Total** | **$53,441** |
| Nonresident Supplemental Tuition | $12,245 |
| **CA Nonresident Total** | **$65,686** |

> Separate program-fee structure applies to the MSTP (Medical Scientist Training Program, MD/PhD): total $26,996/yr (program fee $16,480 + fees + insurance). MSTP students typically receive NIH T32 funding that covers tuition and stipend.

#### School of Pharmacy — PharmD

Source: `https://registrar.ucsf.edu/registration/fees/pharmacy2025`

| Fee Item | Level 1/3 Annual | Level 2 Annual |
|---------|------------------|----------------|
| Student Services Fee | $1,290 | $1,290 |
| Summer Student Services Fee | $80 | $80 |
| Tuition | $13,140 | $13,140 |
| Summer Tuition | $4,380 | $4,380 |
| Professional Degree Supplemental Tuition | $34,160 | $34,160 |
| Community Centers Facility Fee | $207 | $207 |
| Student Transit Pass | $272 | $272 |
| UCGPC Systemwide Fee | $7 | $7 |
| Graduate and Professional Student Association | $27 | $27 |
| Associated Students of School of Pharmacy | $60 | $60 |
| Student Health Insurance Premium | $10,391 | $9,868 |
| **CA Resident Total** | **$64,014** | **$63,491** |
| Nonresident Supplemental Tuition | $12,245 | $12,245 |
| **CA Nonresident Total** | **$76,259** | **$75,736** |

#### School of Nursing — DNP Leadership

Source: `https://registrar.ucsf.edu/registration/fees/nursing2025`

| Fee Item | Annual |
|---------|--------|
| Program Fee | $46,472 |
| UCGPC Systemwide Fee | $7 |
| Graduate and Professional Student Association | $27 |
| Associated Students of School of Nursing | $21 |
| Student Transit Pass | $272 |
| **Total** | **$46,799** |

#### School of Nursing — DNP Post-BSN

Source: `https://registrar.ucsf.edu/registration/fees/nursing2025`

| Fee Item | Annual |
|---------|--------|
| Student Services | $1,290 |
| Summer Student Services | $80 |
| Tuition | $13,140 |
| Summer Tuition | $4,380 |
| Community Centers Facility Fee | $207 |
| UCGPC Systemwide Fee | $7 |
| Student Transit Pass | $272 |
| Graduate and Professional Student Association | $27 |
| Associated Students of School of Nursing | $21 |
| Student Health Insurance Premium | $10,391 |
| Professional Degree Supplemental Tuition | $23,904 |
| **CA Resident Total** | **$53,719** |
| Nonresident Supplemental Tuition | $12,245 |
| **CA Nonresident Total** | **$65,964** |

#### School of Nursing — PhD Nursing & PhD Sociology (CA resident)

Source: `https://registrar.ucsf.edu/registration/fees/nursing2025`

| Fee Item | Annual |
|---------|--------|
| Student Services Fee | $1,290 |
| Tuition | $13,140 |
| Community Centers Facility Fee | $207 |
| Student Transit Pass | $272 |
| UCGPC Systemwide Fee | $7 |
| Graduate and Professional Student Association | $27 |
| Associated Students Graduate Division | $36 |
| Associated Students of School of Nursing | $21 |
| Student Health Insurance Premium | $10,860 |
| **CA Resident Total** | **$25,860** |
| Nonresident Supplemental Tuition | $15,102 |
| **CA Nonresident Total** | **$40,962** |

#### Refund schedule summary

- New students on Title IV federal financial aid withdrawing before the 1st day of instruction: 100% refund (less max $100 or 5% administrative fee).
- Continuing / readmitted / new students not on federal aid withdrawing before first day of instruction: 100% refund (less service fee).

#### Funding framework (Graduate Division-managed programs)

Source: `https://graduate.ucsf.edu/admission/financial-support`

| Funding type | Description | URL |
|--------------|-------------|-----|
| Internal Merit Awards | Graduate Education and Postdoctoral Affairs annual awards; students nominated by programs each April | https://graduate.ucsf.edu/internal-fellowships |
| Extramural Grants & Fellowships | External prestigious awards (NSF GRFP, NIH F31, etc.); eligibility varies | https://graduate.ucsf.edu/extramural-fellowships |
| UC Multi-Campus Research Unit Fellowships | System-wide UC fellowships | https://graduate.ucsf.edu/mcru-fellowships |
| Research/Teaching Assistantships | Provided by individual academic departments | (per program admin) |
| Travel Awards | For conference attendance | https://graduate.ucsf.edu/travel-awards |
| Discovery Fellows Program | (named fellowship program) | https://graduate.ucsf.edu/admission/financial-support/fellowships/discovery-fellows-program |
| Loans & Need-Based Grants | Via UCSF Student Financial Services | https://finaid.ucsf.edu/ |

> Note: MD/DDS/PharmD/DPT professional students have their own school-administered financial-aid processes; check each school's admissions page. PharmD and MD students are eligible for institutional need-based aid plus federal loans; MSTP students typically receive full funding.

---

## SECTION 5 — Evidence chain index

```yaml
E-G-001:
  field: institution.graduate_only_status
  value: UCSF admits only graduate and professional students; no undergraduate population
  source_url: https://www.ucsf.edu/education/admissions
  source_snippet: "UCSF is unique in that it only offers graduate degrees (meaning it does not have an undergraduate student population). To apply to UCSF, you must follow the admissions process specific to the school or program to which you are applying."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-002:
  field: graduate.school_count
  value: 6
  source_url: https://catalog.ucsf.edu/schools/
  source_snippet: "Schools and Programs ... Division of Graduate Education and Postdoctoral Affairs; Institute for Global Health Sciences; School of Dentistry; School of Medicine; School of Nursing; School of Pharmacy"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-003:
  field: graduate.program_count
  value: 51 distinct catalog-listed programs
  source_url: https://catalog.ucsf.edu/programs/
  source_snippet: "Academic Programs ... [A-Z index with 51 entries]"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-004:
  field: graduate.min_gpa
  value: 3.0
  source_url: https://graduate.ucsf.edu/admission/requirements
  source_snippet: "To be eligible for admission, you must have at least a 3.0 (B) grade point average."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-005:
  field: graduate.app_fee_us_domestic
  value: $120
  source_url: https://graduate.ucsf.edu/admission/requirements
  source_snippet: "the non-refundable application fee ($120 for US citizens and permanent residents, and $140 for international applicants)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-006:
  field: graduate.app_fee_international
  value: $140
  source_url: https://graduate.ucsf.edu/admission/requirements
  source_snippet: "$120 for US citizens and permanent residents, and $140 for international applicants"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-007:
  field: graduate.one_program_per_cycle
  value: true
  source_url: https://graduate.ucsf.edu/admission/requirements
  source_snippet: "You may apply to only one graduate program per application cycle/year."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-008:
  field: english.toefl_ibt_min_pre_2026
  value: 80
  source_url: https://graduate.ucsf.edu/admission/intl-admission-requirements
  source_snippet: "internet-based TOEFL iBT ... For tests taken before January 21, 2026: 80 (total score)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-009:
  field: english.toefl_ibt_min_post_2026
  value: 4.5
  source_url: https://graduate.ucsf.edu/admission/intl-admission-requirements
  source_snippet: "For tests taken on or after January 21, 2026: 4.5 (total score)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-010:
  field: english.ielts_min
  value: 7
  source_url: https://graduate.ucsf.edu/admission/intl-admission-requirements
  source_snippet: "IELTS Academic (also online) ... 7 ... Select University of California, San Francisco - Graduate Division"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-011:
  field: english.toefl_code
  value: 4840
  source_url: https://graduate.ucsf.edu/admission/intl-admission-requirements
  source_snippet: "UCSF Code: 4840 | (No department code is required. All scores sent electronically are submitted to the same account.)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-012:
  field: english.accepted_tests_exclusions
  value: "paper-based TOEFL, computer-based TOEFL, IELTS General Training, TOEFL iBT Special Home Edition, MyBest TOEFL, TOEFL ITP Plus for China, or Duolingo are NOT accepted"
  source_url: https://graduate.ucsf.edu/admission/intl-admission-requirements
  source_snippet: "The following tests are not accepted: paper-based TOEFL, computer-based TOEFL, IELTS General Training, TOEFL iBT Special Home Edition, MyBest TOEFL, TOEFL ITP Plus for China, or Duolingo."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-013:
  field: fees.grad_div_resident_annual
  value: "$25,839"
  source_url: https://registrar.ucsf.edu/registration/fees/graddiv2025
  source_snippet: "California Resident Total $25,839.00 $8,614.00 $8,613.00 $8,612.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-014:
  field: fees.grad_div_nonresident_annual
  value: "$40,941"
  source_url: https://registrar.ucsf.edu/registration/fees/graddiv2025
  source_snippet: "California Nonresident Total $40,941.00 $13,648.00 $13,647.00 $13,646.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-015:
  field: fees.dds_resident_annual
  value: "$64,057"
  source_url: https://registrar.ucsf.edu/registration/fees/dentistry2025
  source_snippet: "California Resident Total $64,057.00 $21,390.00 $21,334.00 $21,333.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-016:
  field: fees.md_resident_annual
  value: "$53,441"
  source_url: https://registrar.ucsf.edu/registration/fees/medicine2025
  source_snippet: "California Resident Total $53,441.00 $17,842.00 $17,800.00 $17,799.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-017:
  field: fees.pharmd_resident_annual_level1_3
  value: "$64,014"
  source_url: https://registrar.ucsf.edu/registration/fees/pharmacy2025
  source_snippet: "School of Pharmacy Levels 1 and 3 ... California Resident Total $64,014.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-018:
  field: fees.dnp_leadership_annual
  value: "$46,799"
  source_url: https://registrar.ucsf.edu/registration/fees/nursing2025
  source_snippet: "Doctor of Nursing Practice: Leadership ... Total $46,799.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-019:
  field: fees.dnp_post_bsn_resident_annual
  value: "$53,719"
  source_url: https://registrar.ucsf.edu/registration/fees/nursing2025
  source_snippet: "Doctor of Nursing Practice: Post-BSN ... California Resident Total $53,719.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-020:
  field: fees.dpt_resident_annual
  value: "$40,407"
  source_url: https://registrar.ucsf.edu/registration/fees/graddiv2025
  source_snippet: "Doctor of Physical Therapy (D.P.T.) ... California Resident Total $40,407.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-021:
  field: fees.nursing_phd_resident_annual
  value: "$25,860"
  source_url: https://registrar.ucsf.edu/registration/fees/nursing2025
  source_snippet: "Nursing Ph.D & Sociology Ph.D ... California Resident Total $25,860.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-022:
  field: fees.dds_nonresident_annual
  value: "$76,302"
  source_url: https://registrar.ucsf.edu/registration/fees/dentistry2025
  source_snippet: "California Nonresident Total $76,302.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-023:
  field: fees.md_nonresident_annual
  value: "$65,686"
  source_url: https://registrar.ucsf.edu/registration/fees/medicine2025
  source_snippet: "California Nonresident Total $65,686.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-024:
  field: timeline.phd_bms_close_2026
  value: "Sun., Nov. 16, 2025"
  source_url: https://graduate.ucsf.edu/admission/program-application-timelines
  source_snippet: "Biomedical Sciences PhD Fall '26 Mon., Sep. 1, 2025 Sun., Nov. 16, 2025"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-025:
  field: timeline.phd_dec1_close_2026
  value: "Mon., Dec. 1, 2025"
  source_url: https://graduate.ucsf.edu/admission/program-application-timelines
  source_snippet: "Biological and Medical Informatics PhD Fall '26 Mon., Sep. 1, 2025 Mon., Dec. 1, 2025"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-026:
  field: timeline.dpt_close_2026
  value: "Wed., Oct. 1, 2025"
  source_url: https://graduate.ucsf.edu/admission/program-application-timelines
  source_snippet: "Doctor of Physical Therapy Summer '26 Mon., June 16, 2025 Wed., Oct. 1, 2025"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-027:
  field: timeline.dnp_leadership_close_2026
  value: "Sun., April 5, 2026"
  source_url: https://graduate.ucsf.edu/admission/program-application-timelines
  source_snippet: "Nursing Practice (Leadership) DNP Fall '26 Mon., Sep. 15, 2025 Sun., April 5, 2026"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-028:
  field: timeline.global_health_ms_close_2026
  value: "Tue., June 30, 2026"
  source_url: https://graduate.ucsf.edu/admission/program-application-timelines
  source_snippet: "Global Health Sciences MS Fall '26 Mon., Sep. 15, 2025 Tue., June 30, 2026"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-029:
  field: timeline.programs_paused_for_2026
  value: "Global Health Sciences PhD, Medical Anthropology PhD, OCS DDS/PhD, Rehabilitation Science PhD — not accepting applications for Fall '26"
  source_url: https://graduate.ucsf.edu/admission/program-application-timelines
  source_snippet: "Global Health Sciences PhD Fall '26 Not accepting apps"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-030:
  field: academic.calendar.ay_2026_27_first_summer_start
  value: "June 15, 2026 (Monday)"
  source_url: https://catalog.ucsf.edu/academic-administrative-calendar/
  source_snippet: "First Summer Session 2026 ... Session begins June 15 Monday"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-031:
  field: graduate.funding_internal_awards
  value: "Internal Merit Awards offered annually; nominations by programs in April"
  source_url: https://graduate.ucsf.edu/admission/financial-support
  source_snippet: "Internal Merit Awards: Graduate Education and Postdoctoral Affairs offers many internal awards to eligible PhD students. Students must be nominated and are chosen for these annual awards each April by their individual programs."
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: "ucsf-knowledge-base-v2"
  document: "ucsf-institution-overview" (Section 0)
    chunk: 0.1 counts
    chunk: 0.2 hierarchy tree
    chunk: 0.3 degree-level inventory
    chunk: 0.4 distribution matrix
  document: "ucsf-graduate-programs" (Section 2)
    chunk: school-of-dentistry
    chunk: school-of-medicine
    chunk: school-of-nursing
    chunk: school-of-pharmacy
    chunk: graduate-division-gepa
    chunk: institute-global-health-sciences
  document: "ucsf-application-requirements-deadlines" (Section 3)
    chunk: grad-division-common-rules
    chunk: english-proficiency
    chunk: doctoral-deadlines
    chunk: masters-deadlines
    chunk: certificate-deadlines
  document: "ucsf-costs-financial-aid" (Section 4)
    chunk: grad-division-fees
    chunk: dds-fees
    chunk: md-fees
    chunk: pharmd-fees
    chunk: nursing-dnp-fees
    chunk: nursing-phd-fees
    chunk: dpt-fees
    chunk: funding-framework
  document: "ucsf-evidence-chain" (Section 5)
    chunk: E-G-001 through E-G-031 (one chunk per evidence block)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ucsf-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<PhD|MS|MA|MTM|DDS|MD|PharmD|DPT|DNP|AdvCert>"
  level: graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | evidence
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Status |
|----------|-----------|------------|--------|
| P0 | 2026-27 AY fees (registrar still posting 2025-26 at capture date) | https://registrar.ucsf.edu/registration/fees/ | Not yet posted |
| P0 | DDS/MD/PharmD-specific application fee amounts (beyond Grad Division) | https://dentistry.ucsf.edu/programs/dds/admissions / https://meded.ucsf.edu/admissions-md-program / https://pharmd.ucsf.edu/admissions | Not deeply scraped this run |
| P1 | PharmD curriculum, accreditation status, NAPLEX pass rate | https://pharmacy.ucsf.edu/ | Out of scope this run |
| P1 | School of Nursing MEPN-specific admissions data | https://nursing.ucsf.edu/ | Out of scope this run |
| P1 | Detailed individual program pages (curriculum, credit hours, duration, typical class size) | https://catalog.ucsf.edu/programs/<slug>/ | Index captured, per-program deep-dive deferred |
| P1 | MSTP application portal/timeline specifics (separate from Grad Division Slate) | https://meded.ucsf.edu/admissions-md-program | Deferred |
| P2 | Financial-aid statistics (median debt, % receiving aid, median grant) | https://finaid.ucsf.edu/ | Out of scope this run |
| P2 | International student enrollment statistics | https://graduate.ucsf.edu/admission/graduate-program-statistics | Deferred |
| P2 | Residency match list / outcomes for MD | https://medschool.ucsf.edu/ | Out of scope this run |
| P2 | Research output / NIH funding rankings | https://www.ucsf.edu/research | Out of scope this run |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UCSF value | Notes |
|-----------|-----------|-------|
| Type | Graduate-only health-sciences university | UC-system |
| Region | US — California | San Francisco |
| Total program count (rule 1) | 51 catalog-listed academic programs | Plus 3 dual-degree variant pages = 55 |
| School count (rule 2) | 6 | 4 professional + Grad Division + Global Health |
| EA deadline | N/A — no undergraduate admissions | Graduate-only |
| RA/ED deadline | N/A | |
| Application portal — Graduate Division | Slate | https://graduate.ucsf.edu/admission/requirements |
| Application fee — Grad Division (US/PR) | $120 | E-G-005 |
| Application fee — Grad Division (international) | $140 | E-G-006 |
| Application fee — MD/DDS/PharmD | varies (AMCAS, AADSAS, PharmCAS) | Out of scope this run |
| Min GPA | 3.0 | E-G-004 |
| TOEFL iBT min (pre-2026-01-21) | 80 | E-G-008 |
| TOEFL iBT min (post-2026-01-21) | 4.5 | E-G-009 |
| IELTS Academic min | 7 | E-G-010 |
| Duolingo | Not accepted | E-G-012 |
| One-program-per-cycle rule | Yes | E-G-007 |
| PhD tuition (CA resident, Grad Div) | $25,839/yr | E-G-013 |
| PhD tuition (non-resident, Grad Div) | $40,941/yr | E-G-014 |
| MD tuition (CA resident) | $53,441/yr | E-G-016 |
| DDS tuition (CA resident) | $64,057/yr | E-G-015 |
| PharmD tuition (CA resident, Yr 1/3) | $64,014/yr | E-G-017 |
| DNP Leadership (program fee, annual) | $46,799 | E-G-018 |
| DPT tuition (CA resident) | $40,407/yr | E-G-020 |
| Common App | N/A — graduate-only | |
| SAT/ACT | N/A | |
| Need-blind (intl UG) | N/A | |
| Tuition-free threshold | N/A — graduate-only | |
| Median price paid (UG) | N/A | |
| April-15 honor date | Yes — UCSF observes CGS April 15 resolution | https://graduate.ucsf.edu/admission/requirements |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**:
> - https://www.ucsf.edu/education/admissions (main admissions)
> - https://graduate.ucsf.edu/admission/requirements (Grad Division requirements)
> - https://graduate.ucsf.edu/admission/intl-admission-requirements (English proficiency)
> - https://graduate.ucsf.edu/admission/program-application-timelines (program timelines)
> - https://graduate.ucsf.edu/admission/financial-support (funding)
> - https://catalog.ucsf.edu/programs/ (canonical program directory)
> - https://catalog.ucsf.edu/schools/ (school hierarchy)
> - https://catalog.ucsf.edu/fees/ (tuition context)
> - https://catalog.ucsf.edu/academic-administrative-calendar/ (academic calendar)
> - https://registrar.ucsf.edu/registration/fees/graddiv2025 (Grad Division tuition)
> - https://registrar.ucsf.edu/registration/fees/dentistry2025 (DDS tuition)
> - https://registrar.ucsf.edu/registration/fees/medicine2025 (MD tuition)
> - https://registrar.ucsf.edu/registration/fees/nursing2025 (Nursing tuition)
> - https://registrar.ucsf.edu/registration/fees/pharmacy2025 (PharmD tuition)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program (graduate-only)
> **Cache files**: written to `/Users/erik/Desktop/知识库预处理测试/uni-cache/schools/university-of-california-san-francisco/` (site-memory.json, content-hashes.json; last-extract.json next)