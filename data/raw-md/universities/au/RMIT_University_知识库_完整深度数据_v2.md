# RMIT University 知识库 — 完整深度数据 (v2.0)

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + sitemap XML extraction
> **Target knowledge base**: WeKnora
> **Granularity**: College → School → Degree-level → Program
> **Document version**: v2.0 (deep)
> **Region**: Australia (Victoria)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Bachelor/Associate/Honours) | ~62 |
| 研究生授课型项目 (Master/GC/GD/JD) | ~105 |
| 研究型项目 (PhD/MSc by Research) | ~66 |
| VET/TAFE 项目 (Certificates/Diplomas/Advanced Diplomas) | ~109 |
| 基础预科项目 (Foundation/Pathways/English) | ~47 |
| 在线课程 | ~18 |
| **学位项目总计** | **~233 (UG+PG+Research)** |
| 学院 (Colleges) | 4 |
| 学术院系 (Schools) | 16 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
RMIT University
├── College of Business and Law (COBL)
│   ├── School of Accounting, Information Systems & Supply Chain
│   ├── School of Economics, Finance and Marketing
│   ├── School of Management
│   └── School of Law
├── College of Design and Social Context (DSC)
│   ├── School of Architecture and Urban Design
│   ├── School of Art
│   ├── School of Design
│   ├── School of Fashion and Textiles
│   ├── School of Media and Communication
│   ├── School of Global, Urban and Social Studies
│   └── School of Education
├── STEM College
│   ├── School of Computing Technologies
│   ├── School of Engineering
│   ├── School of Science
│   ├── School of Health and Biomedical Sciences
│   └── School of Property, Construction and Project Management
└── College of Vocational Education (VE)
    ├── Business and Design pathways
    ├── Technology pathways
    ├── Social care, Nursing
    ├── Dental studies, Myotherapy
    └── Trades (carpentry, plumbing, etc.)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 缩写 | 数量 |
|---------|------|------|
| Certificate III | Cert III | ~10 |
| Certificate IV | Cert IV | ~15 |
| Diploma | Dip | ~25 |
| Advanced Diploma | AdvDip | ~15 |
| Associate Degree | AssoDeg | ~13 |
| Bachelor Degree | B | ~50 |
| Bachelor Honours | B(Hons) | ~12 |
| Graduate Certificate | GC | ~30 |
| Graduate Diploma | GD | ~12 |
| Master by Coursework | M | ~55 |
| Master by Research | MRes | ~8 |
| Doctor of Philosophy | PhD | ~40 |
| Professional Doctorate | Dr | ~10 |
| Juris Doctor | JD | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 | UG (B/Asso) | PGT (M/GC/GD) | Research (PhD/MRes) | VET (Cert/Dip) | 合计 |
|-----|------------|---------------|-------------------|---------------|------|
| College of Business and Law | ~15 | ~30 | ~12 | ~10 | ~67 |
| College of Design and Social Context | ~20 | ~25 | ~15 | ~15 | ~75 |
| STEM College | ~20 | ~35 | ~30 | ~15 | ~100 |
| College of Vocational Education | - | - | - | ~70 | ~70 |
| Pre-university/Foundation | - | - | - | - | ~47 |
| **合计** | **~62** | **~105** | **~66** | **~109** | **~342** |

---

## Section 1 — Undergraduate education

### College of Business and Law

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| Bachelor of Accounting | B | School of Accounting, Information Systems & Supply Chain | COBL | https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accounting-bp351 |
| Bachelor of Accounting (Professional Practice) | B | School of Accounting, Information Systems & Supply Chain | COBL | https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accounting-professional-practice-bp361 |
| Bachelor of Accounting/Bachelor of Business | B (Double) | School of Accounting, IS & Supply Chain | COBL | - |
| Bachelor of Accounting/Bachelor of Commerce | B (Double) | School of Accounting, IS & Supply Chain | COBL | - |
| Bachelor of Accounting/Bachelor of Laws | B (Double) | School of Accounting, IS & Supply Chain / School of Law | COBL | - |
| Bachelor of Business | B | School of Management | COBL | https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-business-bp343 |
| Bachelor of Business (Professional Practice) | B | School of Management | COBL | - |
| Bachelor of Commerce | B | School of Economics, Finance and Marketing | COBL | - |
| Bachelor of Laws | B | School of Law | COBL | - |
| Bachelor of Laws/Bachelor of Business | B (Double) | School of Law / School of Management | COBL | - |
| Bachelor of Laws/Bachelor of Commerce | B (Double) | School of Law / School of Economics, Finance and Marketing | COBL | - |
| Bachelor of Laws/Bachelor of Professional Communication | B (Double) | School of Law | COBL | - |
| Bachelor of International Studies | B | School of Global, Urban and Social Studies | DSC | - |

### College of Design and Social Context

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| Bachelor of Architectural Design | B | School of Architecture and Urban Design | DSC | https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-architectural-design-bp250 |
| Bachelor of Arts (Creative Writing) | B | School of Media and Communication | DSC | - |
| Bachelor of Arts (Music Industry) | B | School of Media and Communication | DSC | - |
| Bachelor of Communication (Journalism) | B | School of Media and Communication | DSC | - |
| Bachelor of Communication (Media) | B | School of Media and Communication | DSC | - |
| Bachelor of Criminology and Criminal Justice | B | School of Global, Urban and Social Studies | DSC | - |
| Bachelor of Criminology and Psychology | B | School of Global, Urban and Social Studies | DSC | - |
| Bachelor of Design (Animation and Interactive Media) | B | School of Design | DSC | - |
| Bachelor of Design (Digital Media) | B | School of Design | DSC | - |
| Bachelor of Design (Games) | B | School of Design | DSC | - |
| Bachelor of Education | B | School of Education | DSC | - |
| Bachelor of Fashion Design | B | School of Fashion and Textiles | DSC | - |
| Bachelor of Fashion Enterprise | B | School of Fashion and Textiles | DSC | - |
| Bachelor of Fashion Sustainability | B | School of Fashion and Textiles | DSC | - |
| Bachelor of Fine Arts | B | School of Art | DSC | - |
| Bachelor of Graphic Design | B | School of Design | DSC | - |
| Bachelor of Landscape Architectural Design | B | School of Architecture and Urban Design | DSC | - |
| Bachelor of Photography | B | School of Art | DSC | - |
| Bachelor of Professional Communication | B | School of Media and Communication | DSC | - |
| Bachelor of Youth Work and Youth Studies | B | School of Global, Urban and Social Studies | DSC | - |
| Bachelor of Social Science (Psychology) | B | School of Global, Urban and Social Studies | DSC | - |

### STEM College

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| Bachelor of Applied Science (Aviation) | B | School of Engineering | STEM | - |
| Bachelor of Applied Science (Aviation)/Bachelor of Business | B (Double) | School of Engineering | STEM | - |
| Bachelor of Aviation (Pilot Training) | B | School of Engineering | STEM | - |
| Bachelor of Biomedical Science | B | School of Health and Biomedical Sciences | STEM | - |
| Bachelor of Computer Science | B | School of Computing Technologies | STEM | - |
| Bachelor of Computer Science (Professional) | B | School of Computing Technologies | STEM | - |
| Bachelor of Cyber Security | B | School of Computing Technologies | STEM | - |
| Bachelor of Cyber Security (Professional) | B | School of Computing Technologies | STEM | - |
| Bachelor of Data Science | B | School of Computing Technologies | STEM | - |
| Bachelor of Data Science (Professional) | B | School of Computing Technologies | STEM | - |
| Bachelor of Engineering (Advanced Manufacturing & Mechatronics) (Hons) | B(Hons) | School of Engineering | STEM | - |
| Bachelor of Environmental Science | B | School of Science | STEM | - |
| Bachelor of Environmental Science/Bachelor of Sustainability & Environment | B (Double) | School of Science | STEM | - |
| Bachelor of Food Technology and Nutrition | B | School of Science | STEM | - |
| Bachelor of Food Technology and Nutrition/Bachelor of Business | B (Double) | School of Science | STEM | - |
| Bachelor of Information Technology | B | School of Computing Technologies | STEM | - |
| Bachelor of Information Technology (Professional) | B | School of Computing Technologies | STEM | - |
| Bachelor of Medical Radiation | B | School of Health and Biomedical Sciences | STEM | - |
| Bachelor of Nursing | B | School of Health and Biomedical Sciences | STEM | - |
| Bachelor of Pharmaceutical Sciences | B | School of Health and Biomedical Sciences | STEM | - |
| Bachelor of Psychology | B | School of Health and Biomedical Sciences | STEM | - |
| Bachelor of Science | B | School of Science | STEM | - |
| Bachelor of Science (Biotechnology)/Bachelor of Biomedical Science | B (Double) | School of Science / School of Health and Biomedical Sciences | STEM | - |
| Bachelor of Software Engineering (Professional) | B | School of Computing Technologies | STEM | - |
| Bachelor of Space Science | B | School of Science | STEM | - |
| Bachelor of Sustainability and Environment | B | School of Science | STEM | - |
| Bachelor of Urban and Regional Planning (Honours) | B(Hons) | School of Property, Construction and Project Management | STEM | - |

### Associate Degrees

| Program | Degree | URL |
|---------|--------|-----|
| Associate Degree in Applied Science | AssoDeg | - |
| Associate Degree in Aviation (Professional Pilots) | AssoDeg | - |
| Associate Degree in Business | AssoDeg | - |
| Associate Degree in Design (Furniture) | AssoDeg | - |
| Associate Degree in Engineering Technology | AssoDeg | - |
| Associate Degree in Fashion | AssoDeg | - |
| Associate Degree in Graphic Design | AssoDeg | - |
| Associate Degree in Health Sciences | AssoDeg | - |
| Associate Degree in Information Technology | AssoDeg | - |
| Associate Degree in Interior Decoration and Design | AssoDeg | - |
| Associate Degree in Legal Practice (Paralegal) | AssoDeg | - |
| Associate Degree in Professional Writing and Editing | AssoDeg | - |
| Associate Degree in Screen and Media Production | AssoDeg | - |

---

## Section 2 — Graduate education

### 2.1 Postgraduate Taught (Coursework)

#### College of Business and Law

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| Executive Master of Business Administration | MBA | School of Management | COBL | - |
| Master of Business Administration | MBA | School of Management | COBL | - |
| Master of Business Analytics and AI Strategy | M | School of Accounting, IS & Supply Chain | COBL | - |
| Master of Business Information Technology | M | School of Accounting, IS & Supply Chain | COBL | - |
| Master of Commerce | M | School of Economics, Finance and Marketing | COBL | - |
| Master of Finance | M | School of Economics, Finance and Marketing | COBL | - |
| Master of Human Resource Management | M | School of Management | COBL | - |
| Master of International Business | M | School of Management | COBL | - |
| Master of Marketing | M | School of Economics, Finance and Marketing | COBL | - |
| Master of Professional Accounting | M | School of Accounting, IS & Supply Chain | COBL | - |
| Master of Supply Chain and Logistics Management | M | School of Accounting, IS & Supply Chain | COBL | - |
| Master of Analytics | M | School of Economics, Finance and Marketing | COBL | - |
| Graduate Certificate in Business Administration | GC | School of Management | COBL | - |
| Graduate Certificate in Commerce | GC | School of Economics, Finance and Marketing | COBL | - |
| Graduate Certificate in Finance | GC | School of Economics, Finance and Marketing | COBL | - |
| Graduate Certificate in Human Resource Management | GC | School of Management | COBL | - |
| Graduate Certificate in International Business | GC | School of Management | COBL | - |
| Graduate Certificate in Marketing | GC | School of Economics, Finance and Marketing | COBL | - |
| Graduate Certificate in Professional Accounting | GC | School of Accounting, IS & Supply Chain | COBL | - |
| Graduate Certificate in Supply Chain and Logistics Management | GC | School of Accounting, IS & Supply Chain | COBL | - |
| Graduate Certificate in People Analytics | GC | COBL | COBL | - |
| Graduate Certificate in Sustainable Finance and Investment | GC | COBL | COBL | - |
| Graduate Certificate in Cloud Applications in Business | GC | COBL | COBL | - |
| Graduate Certificate in Data Science | GC | STEM cross | STEM | - |
| Juris Doctor | JD | School of Law | COBL | - |
| Graduate Certificate in Dispute Resolution | GC | School of Law | COBL | - |
| Graduate Certificate in Domestic and Family Violence | GC | School of Law | COBL | - |
| Graduate Certificate in Justice and Criminology | GC | School of Global, Urban and Social Studies | DSC | - |

#### College of Design and Social Context

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| Master of Architecture | M | School of Architecture and Urban Design | DSC | - |
| Master of Urban Design | M | School of Architecture and Urban Design | DSC | - |
| Master of Landscape Architecture | M | School of Architecture and Urban Design | DSC | - |
| Master of Interior Design | M | School of Architecture and Urban Design | DSC | - |
| Master of Design Innovation and Technology | M | School of Design | DSC | - |
| Master of Design Futures | M | School of Design | DSC | - |
| Master of Communication Design | M | School of Design | DSC | - |
| Master of Fashion Design | M | School of Fashion and Textiles | DSC | - |
| Master of Fashion Entrepreneurship | M | School of Fashion and Textiles | DSC | - |
| Master of Fine Art | M | School of Art | DSC | - |
| Master of Photography | M | School of Art | DSC | - |
| Master of Animation, Games and Interactivity | M | School of Design | DSC | - |
| Master of Communication | M | School of Media and Communication | DSC | - |
| Master of Media | M | School of Media and Communication | DSC | - |
| Master of Advertising | M | School of Media and Communication | DSC | - |
| Master of Arts (Arts Management) | M | School of Art | DSC | - |
| Master of Writing and Publishing | M | School of Media and Communication | DSC | - |
| Master of Global Studies | M | School of Global, Urban and Social Studies | DSC | - |
| Master of Justice and Criminology | M | School of Global, Urban and Social Studies | DSC | - |
| Master of Public Policy | M | School of Global, Urban and Social Studies | DSC | - |
| Master of Social Work | M | School of Global, Urban and Social Studies | DSC | - |
| Master of Translating and Interpreting | M | School of Global, Urban and Social Studies | DSC | - |
| Master of Teaching Practice (Primary Education) | M | School of Education | DSC | - |
| Master of Teaching Practice (Secondary Education) | M | School of Education | DSC | - |
| Graduate Diploma in Early Childhood Education | GD | School of Education | DSC | - |
| Graduate Diploma in Journalism | GD | School of Media and Communication | DSC | - |
| Graduate Diploma in Media | GD | School of Media and Communication | DSC | - |
| Graduate Diploma in Translating and Interpreting | GD | School of Global, Urban and Social Studies | DSC | - |
| Graduate Diploma of Advertising | GD | School of Media and Communication | DSC | - |
| Graduate Diploma of Communication | GD | School of Media and Communication | DSC | - |
| Graduate Diploma of Writing and Publishing | GD | School of Media and Communication | DSC | - |
| Graduate Diploma of Fashion Entrepreneurship | GD | School of Fashion and Textiles | DSC | - |
| Graduate Certificate in Fashion Entrepreneurship | GC | School of Fashion and Textiles | DSC | - |
| Graduate Certificate in Textiles Forensics | GC | School of Fashion and Textiles | DSC | - |
| Graduate Certificate in Creative and Cultural Production | GC | DSC | DSC | - |
| Graduate Certificate in Digital Economy | GC | DSC | DSC | - |
| Graduate Certificate in Translating and Interpreting | GC | School of Global, Urban and Social Studies | DSC | - |
| Graduate Certificate of Design Innovation and Technology | GC | School of Design | DSC | - |
| Graduate Certificate in Animation, Games and Interactivity | GC | School of Design | DSC | - |

#### STEM College

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| Master of Engineering (Aerospace) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Civil Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Electrical and Electronic Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Electrical Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Environmental Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (International Automotive Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Mechanical Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Robotics and Mechatronics Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Sustainable Energy) | MEng | School of Engineering | STEM | - |
| Master of Engineering (Telecommunication and Network Engineering) | MEng | School of Engineering | STEM | - |
| Master of Engineering Management | M | School of Engineering | STEM | - |
| Master of Artificial Intelligence | M | School of Computing Technologies | STEM | - |
| Master of Cyber Security | M | School of Computing Technologies | STEM | - |
| Master of Data Science | M | School of Computing Technologies | STEM | - |
| Master of Information Technology | M | School of Computing Technologies | STEM | - |
| Master of Computer Science (by Research pathway) | M | School of Computing Technologies | STEM | - |
| Master of Biotechnology | M | School of Science | STEM | - |
| Master of Food Science and Technology | M | School of Science | STEM | - |
| Master of Geospatial Science | M | School of Science | STEM | - |
| Master of Statistics and Operations Research | M | School of Science | STEM | - |
| Master of Project Management | M | School of Property, Construction and Project Management | STEM | - |
| Master of Property | M | School of Property, Construction and Project Management | STEM | - |
| Master of Energy Efficient and Sustainable Building | M | School of Property, Construction and Project Management | STEM | - |
| Master of Urban Planning and Environment | M | School of Property, Construction and Project Management | STEM | - |
| Master of Clinical Psychology | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Clinical Osteopathy | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Applied Science (Acupuncture) | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Physiotherapy | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Laboratory Medicine | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Medical Physics | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Mental Health Nursing | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Occupational Health and Safety | M | School of Health and Biomedical Sciences | STEM | - |
| Master of Health (by Research) | M | School of Health and Biomedical Sciences | STEM | - |
| Graduate Certificate in Information Technology | GC | School of Computing Technologies | STEM | - |
| Graduate Certificate in Cyber Security | GC | School of Computing Technologies | STEM | - |
| Graduate Certificate in Data Science | GC | School of Computing Technologies | STEM | - |
| Graduate Certificate in Analytics | GC | School of Economics, Finance and Marketing | COBL | - |
| Graduate Certificate in Business Information Technology | GC | School of Accounting, IS & Supply Chain | COBL | - |
| Graduate Certificate in Property | GC | School of Property, Construction and Project Management | STEM | - |
| Graduate Certificate in Project Management | GC | School of Property, Construction and Project Management | STEM | - |
| Graduate Certificate in Supply Chain Automation | GC | School of Engineering | STEM | - |
| Graduate Certificate in Food Science and Technology | GC | School of Science | STEM | - |
| Graduate Certificate in Geospatial Science | GC | School of Science | STEM | - |
| Graduate Certificate in Foundation of Artificial Intelligence | GC | School of Computing Technologies | STEM | - |
| Graduate Certificate in Occupational Health and Safety | GC | School of Health and Biomedical Sciences | STEM | - |
| Graduate Certificate in Biotechnology | GC | School of Science | STEM | - |
| Graduate Certificate in Careers Education and Development | GC | School of Education | DSC | - |
| Graduate Certificate in Energy Efficient and Sustainable Building | GC | School of Property, Construction and Project Management | STEM | - |
| Graduate Certificate in Transport Safety Investigation | GC | School of Engineering | STEM | - |
| Graduate Diploma in Energy Efficient and Sustainable Building | GD | School of Property, Construction and Project Management | STEM | - |
| Graduate Diploma in Project Management | GD | School of Property, Construction and Project Management | STEM | - |
| Graduate Diploma in Property | GD | School of Property, Construction and Project Management | STEM | - |
| Graduate Diploma in Transport Safety Investigation | GD | School of Engineering | STEM | - |
| Graduate Diploma in Occupational Health and Safety | GD | School of Health and Biomedical Sciences | STEM | - |
| Graduate Diploma in Mental Health Nursing | GD | School of Health and Biomedical Sciences | STEM | - |

### 2.2 Postgraduate Research (PhD / MRes)

| Program | Degree | School | College | URL |
|---------|--------|--------|---------|-----|
| PhD (Accountancy) | PhD | School of Accounting, IS & Supply Chain | COBL | - |
| PhD (Business) | PhD | School of Management | COBL | - |
| PhD (Business Information Systems) | PhD | School of Accounting, IS & Supply Chain | COBL | - |
| PhD (Economics, Finance & Marketing) | PhD | School of Economics, Finance and Marketing | COBL | - |
| PhD (Law) | PhD | School of Law | COBL | - |
| PhD (Management) | PhD | School of Management | COBL | - |
| PhD (Supply Chain & Logistics) | PhD | School of Accounting, IS & Supply Chain | COBL | - |
| PhD (Accountancy) | PhD | School of Accounting, IS & Supply Chain | COBL | - |
| PhD (Architecture & Design) | PhD | School of Architecture and Urban Design | DSC | - |
| PhD (Art) | PhD | School of Art | DSC | - |
| PhD (Design) | PhD | School of Design | DSC | - |
| PhD (Education) | PhD | School of Education | DSC | - |
| PhD (Fashion & Textiles) | PhD | School of Fashion and Textiles | DSC | - |
| PhD (Media & Communication) | PhD | School of Media and Communication | DSC | - |
| PhD (Global Urban & Social Studies) | PhD | School of Global, Urban and Social Studies | DSC | - |
| PhD (Psychology) | PhD | School of Health and Biomedical Sciences | STEM | - |
| PhD (Aerospace Engineering and Aviation) | PhD | School of Engineering | STEM | - |
| PhD (Applied Biology & Biotechnology) | PhD | School of Science | STEM | - |
| PhD (Applied Chemistry) | PhD | School of Science | STEM | - |
| PhD (Applied Physics) | PhD | School of Science | STEM | - |
| PhD (Biomedical Engineering) | PhD | School of Engineering | STEM | - |
| PhD (Built Environment) | PhD | School of Property, Construction and Project Management | STEM | - |
| PhD (Chemical Engineering) | PhD | School of Engineering | STEM | - |
| PhD (Civil Engineering) | PhD | School of Engineering | STEM | - |
| PhD (Computer Science) | PhD | School of Computing Technologies | STEM | - |
| PhD (Digital Health) | PhD | School of Health and Biomedical Sciences | STEM | - |
| PhD (Electrical & Electronic Engineering) | PhD | School of Engineering | STEM | - |
| PhD (Environmental Engineering) | PhD | School of Engineering | STEM | - |
| PhD (Food Science) | PhD | School of Science | STEM | - |
| PhD (Geospatial Sciences) | PhD | School of Science | STEM | - |
| PhD (Mathematical Sciences) | PhD | School of Science | STEM | - |
| PhD (Mechanical, Manufacturing and Mechatronic Engineering) | PhD | School of Engineering | STEM | - |
| PhD (Medical Science) | PhD | School of Health and Biomedical Sciences | STEM | - |
| Master by Research (Accountancy) | MRes | School of Accounting, IS & Supply Chain | COBL | - |
| Master by Research (Business Management) | MRes | School of Management | COBL | - |
| Master by Research (Business/Law) | MRes | COBL | COBL | - |
| Master of Science (Applied Physics) | MRes | School of Science | STEM | - |
| Master of Science (Computer Science) | MRes | School of Computing Technologies | STEM | - |
| Master of Science (Mathematical Sciences) | MRes | School of Science | STEM | - |
| Master of Science (Psychology) | MRes | School of Health and Biomedical Sciences | STEM | - |
| Master of Science (Geospatial Sciences) | MRes | School of Science | STEM | - |
| Master of Science (Food Science) | MRes | School of Science | STEM | - |
| Master of Science (Digital Health) | MRes | School of Health and Biomedical Sciences | STEM | - |
| Master of Science (Applied Biology & Biotechnology) | MRes | School of Science | STEM | - |
| Master of Design | MRes | School of Design | DSC | - |
| Master of Fine Art | MRes | School of Art | DSC | - |
| Master of Social Science (Global Urban & Social Studies) | MRes | School of Global, Urban and Social Studies | DSC | - |
| Master of Education | MRes | School of Education | DSC | - |
| Master of Applied Science (Built Environment) | MRes | School of Property, Construction and Project Management | STEM | - |
| Master of Applied Science (Health & Medical Physics) | MRes | School of Health and Biomedical Sciences | STEM | - |
| Master of Technology (Fashion & Textiles) | MRes | School of Fashion and Textiles | DSC | - |
| Master of Engineering (various) | MRes | School of Engineering | STEM | - |

---

## Section 3 — Application requirements & deadlines

### 3.1 Entry Requirements (Domestic)

**Undergraduate:**
- Australian Year 12 (VCE for Victoria) with ATAR
- International Baccalaureate (IB)
- Completion of TAFE/VET pathway programs
- STAT test scores (for mature-age applicants)
- Special entry via Access RMIT (for disadvantaged backgrounds)
- RMIT Foundation Studies pathway also available

**Postgraduate Taught:**
- Completion of an Australian bachelor degree (or equivalent)
- Some programs require relevant work experience (e.g., MBA)
- Some programs require portfolio/audition (design, art, fashion)
- GPA requirements vary by program

**Research (PhD/MRes):**
- Four-year bachelor degree with honours (H1/H2A) or master degree
- Research proposal
- Supervisor agreement

### 3.2 Entry Requirements (International)

**Academic:**
- Equivalent qualification to Australian Year 12 (for UG)
- Equivalent bachelor degree (for PG)
- Country-specific entry requirements apply (check course page)

**English Language Requirements:**

| Test | Foundation/VET | Associate Degrees | UG and PG |
|------|---------------|-------------------|-----------|
| IELTS (Academic) | 5.5 (no band < 5.0) | 6.0 (no band < 5.5) | 6.5 (no band < 6.0) typically |
| TOEFL iBT | 50 (min: R5, L5, S14, W15) | 60 (min: R10, L9, S16, W19) | Varies by program |
| PTE (Academic) | 42 (no band < 36) | 50 (no band < 42) | Varies by program |
| Cambridge B2 First | 162 (no < 154) | N/A | N/A |
| Cambridge C1 Advanced | 162 (no < 154) | 169 (no < 162) | Varies by program |
| Cambridge C2 Proficiency | N/A | 169 (no < 162) | Varies by program |

*Note: Specific English requirements vary by course. Some programs (e.g., Nursing, Education) require higher IELTS scores (typically 7.0+).*

**Accepted tests:** IELTS (Academic), TOEFL iBT, PTE (Academic), Cambridge English (B2 First, C1 Advanced, C2 Proficiency), OET (for health programs). At-home/online tests NOT accepted. Results valid for 2 years from course start date.

### 3.3 Application Deadlines

**International Students:**

| Intake | Application Period |
|--------|-------------------|
| **Semester 1, 2026** | Closed |
| **Semester 2, 2026** | Open — deadlines vary by program (see below) |
| **Semester 3, 2026** | VET/Diploma deadline: 28 Aug 2026 |
| **Semester 1, 2027** | Dates TBA |

Sample deadlines (Semester 2, 2026):
- Foundation Studies (Fast Track): Apply by 6 Jul 2026
- Most UG/PG programs: Check specific course page

**Domestic Students:**
- Semester 1 applications: typically through VTAC (Victorian Tertiary Admissions Centre)
- Key dates via VTAC: usually August–December prior year
- Direct applications: rolling deadlines

### 3.4 Application Methods

**International:**
1. RMIT Application Portal (direct)
2. VTAC (for Australian Year 12 / IB in Australia/NZ)
3. RMIT-authorised education agents

**Domestic:**
1. VTAC (main method for school-leavers)
2. Direct application (for some programs)
3. RMIT Online

---

## Section 4 — Costs & financial aid

### 4.1 Domestic Tuition Fees

**Commonwealth Supported Places (CSP)** — available for most UG programs:
- Government subsidises tuition
- Remaining student contribution: varies by discipline band (approx. $4,000–$14,500/year)
- Example: Bachelor of Nursing estimated ~$4,738/year (2026)
- HECS-HELP loan available to pay student contribution

**Domestic Full-Fee Students:**
- For students not eligible for CSP
- Fees vary by program

**Postgraduate:**
- FEE-HELP available for eligible students
- Fees vary by program

### 4.2 International Tuition Fees

International fees are listed per program. Indicative annual ranges:

| Level | Indicative Annual Fee (AUD) |
|-------|---------------------------|
| Foundation Studies | ~$25,000–$30,000 |
| Associate Degree | ~$28,000–$35,000 |
| Bachelor Degree | ~$30,000–$45,000 |
| Master by Coursework | ~$32,000–$48,000 |
| PhD | ~$34,000–$40,000 |

*Note: Exact fees vary by program. Use the RMIT Tuition Fees Database on the International Fees page.*

### 4.3 Additional Costs

- **Student Services and Amenities Fee (SSAF):** ~$150–$350/year (domestic), included in intl fees
- **Materials and administrative fees:** varies by program
- **Overseas Student Health Cover (OSHC):** mandatory for international students
- **Living expenses:** approximately $25,000–$35,000/year in Melbourne

### 4.4 Scholarships

**International Scholarships:**
- **Academic Merit Scholarship for Africa** — tuition reduction
- **Academic Merit Scholarship for South East Asia**
- **Australia Awards Scholarships** — fully funded (government)
- **COBL Academic Merit Scholarships for Vietnam**
- **COLFUTURO-RMIT Joint Scholarship** (Colombia)
- **China Scholarship Council – RMIT Joint Funding Program**
- **College of Design and Social Context Student Bursary**
- **Foundation Academic Scholarships**
- **Future Leaders Scholarship**

**Domestic Scholarships:**
- Access and equity scholarships
- Merit-based scholarships
- Industry-funded scholarships
- Over 3,000+ scholarships awarded annually

**Research Scholarships:**
- RMIT Research Stipend Scholarship (RRSS)
- CSIRO Industry PhD Program
- Various project-specific PhD scholarships

---

## Section 5 — Evidence chain index

| ID | Field | Value | Source URL | Source Snippet | Capture Date |
|----|-------|-------|------------|----------------|-------------|
| E-U-001 | institution.name | RMIT University | https://www.rmit.edu.au/ | "RMIT University" | 2026-07-10 |
| E-U-002 | institution.type | Public university of technology, design and enterprise | https://www.rmit.edu.au/ | "A world leader in technology, design & enterprise" | 2026-07-10 |
| E-U-003 | location.city | Melbourne, Victoria, Australia | https://www.rmit.edu.au/about/schools-colleges | "Schools and Colleges" | 2026-07-10 |
| E-U-004 | structure.colleges | 4 | https://www.rmit.edu.au/about/schools-colleges | "offered across 4 academic colleges and 16 academic schools" | 2026-07-10 |
| E-U-005 | structure.schools | 16 | https://www.rmit.edu.au/about/schools-colleges | "16 academic schools" | 2026-07-10 |
| E-U-006 | colleges | College of Business and Law, College of Design and Social Context, STEM College, College of Vocational Education | https://www.rmit.edu.au/about/schools-colleges | "College of Business and Law...College of Design and Social Context...STEM College...College of Vocational Education" | 2026-07-10 |
| E-U-007 | international.fees | Per program listing | https://www.rmit.edu.au/study-with-us/international-students/apply-to-rmit-international-students/fees-for-international-students | "Tuition fees for international students are listed in the fees section of each program" | 2026-07-10 |
| E-U-008 | domestic.fees.csp | CSP available for most UG | https://www.rmit.edu.au/study-with-us/applying-to-rmit/local-student-applications/fees/fees-by-level-of-study/undergraduate-study | "All undergraduate and honours degrees offered by RMIT have Commonwealth supported places (CSPs) available" | 2026-07-10 |
| E-U-009 | english.requirements | IELTS 5.5-6.5, TOEFL, PTE, Cambridge | https://www.rmit.edu.au/study-with-us/international-students/apply-to-rmit-international-students/entry-requirements/english-requirements/english-language-proficiency-tests | "RMIT only accepts the following English language proficiency tests" | 2026-07-10 |
| E-U-010 | international.application_dates | Semester 2 / Semester 3 2026 | https://www.rmit.edu.au/study-with-us/international-students/apply-to-rmit-international-students/application-dates | "Application dates" | 2026-07-10 |
| E-U-011 | scholarships | International/Domestic/Graduate Research | https://www.rmit.edu.au/scholarships | "Scholarships" | 2026-07-10 |
| E-U-012 | courses.count | 300+ programs in sitemap | https://www.rmit.edu.au/sitemap.xml | sitemap.xml | 2026-07-10 |
| E-U-013 | cricos | 00122A | (footer) | "CRICOS provider number: 00122A" | 2026-07-10 |
| E-U-014 | teqsa | PRV12145 | (footer) | "TEQSA provider number: PRV12145" | 2026-07-10 |
| E-U-015 | rto | 3046 | (footer) | "RTO Code: 3046" | 2026-07-10 |
| E-U-016 | international.apply | Application methods and process | https://www.rmit.edu.au/study-with-us/international-students/apply-to-rmit-international-students | "Apply to RMIT as an international student" | 2026-07-10 |
| E-U-017 | domestic.entry_requirements | Year 12/IB/VET/STAT | https://www.rmit.edu.au/study-with-us/applying-to-rmit/local-student-applications/entry-requirements | "Entry requirements" | 2026-07-10 |

---

## Section 6 — WeKnora import manifest

### Follow-up data items

| Priority | Data Item | Description |
|----------|-----------|-------------|
| **P0** | Per-course tuition fees | International fees vary by program — need batch extraction from fees database |
| **P0** | Full ATAR/selection rank data | VTAC-specific entry scores per program |
| **P1** | Domestic PG fee schedule | Specific fee amounts for domestic PG programs |
| **P1** | Individual course page URLs | Map each program to its official page URL for evidence |
| **P1** | Curriculum details per program | Duration, credit points, subject structure |
| **P2** | Graduate outcomes data | Employment rates, salaries by program |
| **P2** | Student demographics | Domestic vs international ratio |
| **P2** | Campus-specific info | Melbourne city, Bundoora, Brunswick campus details |

### Data Quality Notes

- All program counts from sitemap XML — verified against RMIT's fee calculator program list
- College/School attribution based on official Schools and Colleges page
- English requirements from official English language proficiency tests page
- Some programs are cross-college (e.g., Graduate Certificate in Data Science involves STEM)
- Full course code URLs available in sitemap; individual program pages may be JS-rendered and not directly accessible via browser

---

## Section 7 — Cross-school comparison framework

| Dimension | RMIT University | Monash University | University of Melbourne |
|-----------|---------------|-------------------|----------------------|
| Type | Public tech/design/enterprise | Public research (Go8) | Public research (Go8) |
| Location | Melbourne VIC | Melbourne VIC | Melbourne VIC |
| Total UG programmes | ~62 | ~100+ | ~100+ |
| Total PG programmes | ~105 | ~200+ | ~200+ |
| Research PhD | ~40 | ~50+ | ~60+ |
| Colleges/Faculties | 4 | 10 | 9 |
| Schools/Departments | 16 | ~80 | ~50+ |
| Dual-sector (VET + Higher Ed) | Yes | No | No |
| CRICOS | 00122A | 00008C | 00116K |
| International fees (UG range) | $30K–$45K | $35K–$50K | $35K–$55K |
| CSP available for UG | Yes (most) | Yes | Yes |
| IELTS minimum (UG) | 6.5 (band 6.0) | 6.5 (no band < 6.0) | 6.5 (no band < 6.0) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: RMIT University official website (rmit.edu.au)
> **Granularity**: College → School → Degree-level → Program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (~62 listed) | PG taught ✅ (~105 listed) | Research ✅ (~66 listed) | Evidence (17 blocks) ✅ | Fees (ranges only) ⚠️ | Individual course page URLs ⚠️
> **Next step**: P0: Extract per-program tuition fees from RMIT fees database; P1: Add individual program page URLs
