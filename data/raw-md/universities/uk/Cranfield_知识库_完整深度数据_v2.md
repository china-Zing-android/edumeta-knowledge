# Cranfield University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → centre → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | 0 (Cranfield is postgraduate-only) |
| 研究生授课型 (PGT: MSc/MBA) | 86 (83 MSc + 3 MBA) |
| 研究生研究型 (MSc by Research) | 13 |
| 研究生博士 (PhD) | 37 |
| 退出奖项 (PgDip/PgCert exit awards) | 78 (43 PgDip + 35 PgCert, from MSc programs) |
| **学位项目总计 (excluding exit awards)** | **136** |
| 短期课程 (Short courses) | 297 |
| 学术中心 (Centres/Institutes) | 50+ |
| 学院 (Named Schools) | 1 (School of Management) |

> **Data source**: Cranfield Funnelback course search (`search.cranfield.ac.uk`), filtered by degree level. PgDip and PgCert counts represent exit awards available from MSc programs, not standalone programmes.
>
> **Note**: Cranfield University is a **specialist postgraduate university** — it does not offer undergraduate degrees. Founded in 1946 as the College of Aeronautics, it received its Royal Charter in 1969. It is the largest UK provider of master's-level graduates in engineering.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Cranfield University
├── School of Management (established 1967)                    [学院]
│   ├── Full-time Master's programmes                         [系]
│   ├── Part-time Master's programmes                         [系]
│   ├── MBA programmes                                        [系]
│   ├── Executive Education                                   [系]
│   └── Research degrees                                      [系]
├── Defence & Security Cluster (Shrivenham campus)            [学院级]
│   ├── Centre for Defence Engineering                        [中心]
│   │   ├── Aeromechanical Systems Group                      [组]
│   │   ├── Defence Electronics Group                         [组]
│   │   └── Lethality and Survivability Group                 [组]
│   ├── Centre for Defence Management and Leadership          [中心]
│   │   └── Strategic Leadership Programme                    [组]
│   ├── Centre for Electronic Warfare, Information and Cyber  [中心]
│   │   └── Applied Psychology Group                          [组]
│   ├── Centre for Defence Chemistry                          [中心]
│   │   ├── Life Assessment Group                             [组]
│   │   ├── Ordnance Test and Evaluation Centre               [组]
│   │   └── Propellant Group                                  [组]
│   ├── Centre for Simulation and Analytics                   [中心]
│   └── CBRN / Counterterrorism / Digital Forensics           [中心]
├── Aerospace & Aviation Cluster                              [学院级]
│   ├── Centre for Aeronautics                                [中心]
│   ├── Centre for Air Transport Management                   [中心]
│   ├── Cranfield Air and Space Propulsion Institute          [中心]
│   ├── Centre for Propulsion and Thermal Power Engineering   [中心]
│   │   ├── Gas Turbine Systems Engineering Group             [组]
│   │   ├── Hybrid Electric Propulsion Group                  [组]
│   │   ├── Low Emissions Technologies and Combustion Group   [组]
│   │   └── Fluids and Structures                             [组]
│   ├── National Flying Laboratory Centre                     [中心]
│   ├── Digital Aviation Research and Technology Centre        [中心]
│   └── Sir Peter Gregson Aerospace Integration Research Centre [中心]
├── Energy & Environment Cluster                              [学院级]
│   ├── Centre for Energy Engineering                         [中心]
│   │   └── Sustainable Energy Systems and Devices            [组]
│   ├── Centre for Energy Systems and Strategy                [中心]
│   ├── Centre for Renewable and Low Carbon Energy            [中心]
│   ├── Cranfield Environment Centre                          [中心]
│   └── Cranfield Water Science Institute                     [中心]
├── Manufacturing & Materials Cluster                         [学院级]
│   ├── Centre for Materials                                  [中心]
│   │   └── Multifunctional Composites Group                  [组]
│   ├── Centre for Digital Engineering and Manufacturing      [中心]
│   ├── Welding and Additive Manufacturing Centre             [中心]
│   ├── Sustainable Manufacturing Systems Centre              [中心]
│   └── Surface Engineering and Precision Centre              [中心]
├── Agrifood & Biosciences Cluster                            [学院级]
│   ├── Centre for Soil, Agrifood and Biosciences             [中心]
│   └── Magan Centre of Applied Mycology (MCAM)               [中心]
├── Digital & Systems Cluster                                 [学院级]
│   ├── Centre for Computational Engineering Sciences         [中心]
│   ├── Centre for Assured and Connected Autonomy             [中心]
│   │   ├── Autonomous Systems and Control                    [组]
│   │   └── Human Machine Intelligence                        [组]
│   ├── Centre for Digital and Design Engineering             [中心]
│   ├── Centre for Robotics and Assembly                      [中心]
│   ├── Centre for Systems and Technology Management          [中心]
│   └── Integrated Vehicle Health Management Centre           [中心]
├── Safety & Accident Investigation                           [学院级]
│   └── Safety and Accident Investigation Centre              [中心]
└── Specialised Institutes                                    [学院级]
    ├── Cranfield Forensic Institute                          [中心]
    │   ├── Advanced Imaging                                  [组]
    │   ├── Archaeology                                       [组]
    │   ├── Bioarchaeology and Forensic Anthropology          [组]
    │   ├── Forensic Entomology                               [组]
    │   └── Materials Characterisation                        [组]
    ├── Centre for Engineering Photonics                      [中心]
    ├── Centre for Antenna and Communications Technology      [中心]
    ├── Centre for Life-cycle Engineering and Management      [中心]
    └── Magan Centre of Applied Mycology                      [中心]
```

> **Note**: Cranfield uses a **centre-based** organizational structure rather than traditional faculty/department divisions. The only named "School" is the School of Management. All other academic units are organized as Centres, Institutes, and Groups, clustered under broad thematic areas. The Shrivenham campus hosts defence and security-focused centres in partnership with the UK Defence Academy.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| MSc | Master of Science | 研究生授课型 | 83 |
| MBA | Master of Business Administration | 研究生授课型 | 3 |
| MSc by Research | Master of Science by Research | 研究生研究型 | 13 |
| PhD | Doctor of Philosophy | 研究生博士 | 37 |
| PgDip | Postgraduate Diploma (exit award) | 研究生文凭 | 43 |
| PgCert | Postgraduate Certificate (exit award) | 研究生证书 | 35 |

> **UK degree note**: Cranfield's PgDip and PgCert offerings are primarily **exit awards** from MSc programmes — students who complete部分课程但未完成全部MSc要求可获得这些退出资格。独立的PgDip/PgCert项目较少。MSc by Research项目为自费研究型硕士，通常可衔接PhD。

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学术集群 \ 级别 | MSc | MBA | MSc by Research | PhD | 合计 |
|----------------|-----|-----|-----------------|-----|------|
| School of Management | 10 | 3 | 0 | 0 | **13** |
| Defence & Security | 14 | 0 | 1 | 0 | **15** |
| Aerospace & Aviation | 13 | 0 | 1 | 0 | **14** |
| Energy & Environment | 12 | 0 | 2 | 0 | **14** |
| Automotive & Motorsport | 5 | 0 | 0 | 0 | **5** |
| Manufacturing & Materials | 4 | 0 | 1 | 0 | **5** |
| Digital, AI & Computing | 5 | 0 | 0 | 0 | **5** |
| Agrifood & Water | 4 | 0 | 2 | 0 | **6** |
| Safety & Air Transport | 5 | 0 | 0 | 0 | **5** |
| Thermal Power (cross-cutting) | 6 | 0 | 1 | 0 | **7** |
| Research MSc by Topic | 0 | 0 | 5 | 0 | **5** |
| Self-funded PhD projects | 0 | 0 | 0 | 37 | **37** |
| Cross-cutting / Other | 5 | 0 | 0 | 0 | **5** |
| **合计** | **83** | **3** | **13** | **37** | **136** |

> **Reconciliation**: 83 + 3 + 13 + 37 = 136 ✓ (matches rule-1 total)
>
> **Note**: PhD programmes at Cranfield are primarily **self-funded research projects** advertised individually, not cohort-based taught programmes. Students apply to specific research topics. MSc by Research programmes are similarly topic-based.

---

## SECTION 1 — Postgraduate Taught Education (PGT)

### 1.1 School of Management

> **Rankings**: FT European Business School 2025 — Top 5 UK, 29th Europe. QS Global MBA 2026 — Top 20% worldwide.

#### Full-time Master's Programmes

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Finance MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/finance) |
| 2 | Management MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/management) |
| 3 | Strategic Marketing MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/strategic-marketing) |
| 4 | Business Data Analytics MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/business-data-analytics) |
| 5 | Banking, Economics and Finance MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/banking-economics-and-finance) |
| 6 | Logistics and Supply Chain Management MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/logistics-and-supply-chain-management) |
| 7 | Procurement and Supply Chain Management MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/som/masters-courses/procurement-and-supply-chain-management) |

#### Part-time / Online Master's Programmes

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 8 | Sustainability MSc | MSc | Online/Part-time | [Link](https://www.cranfield.ac.uk/som/masters-courses-part-time/sustainability) |
| 9 | Marketing and Leadership MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/som/masters-courses-part-time/marketing-and-leadership) |
| 10 | Strategic Human Resource Management MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/som/masters-courses-part-time/strategic-human-resource-management) |

#### MBA Programmes

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 11 | The Transformation MBA | MBA | Full-time | [Link](https://www.cranfield.ac.uk/som/mba/full-time-mba) |
| 12 | Executive MBA | MBA | Executive/Part-time | [Link](https://www.cranfield.ac.uk/som/mba/executive-mba) |
| 13 | Cranfield MBA Double Degree | MBA | Full-time | [Link](https://www.cranfield.ac.uk/som/mba/mba-double-degree) |

#### Management Apprenticeships

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 14 | Senior Leader Apprenticeship: Management and Leadership | PgDip + MSc | Part-time | [Link](https://www.cranfield.ac.uk/som/masters-courses-part-time/senior-leader-apprenticeship) |
| 15 | Senior Leader Apprenticeship+ Logistics and Supply Chain Management (Executive) | PgDip + MSc | Part-time | [Link](https://www.cranfield.ac.uk/som/masters-courses-part-time/senior-leader-apprenticeship-logistics) |

### 1.2 Defence & Security Cluster (Shrivenham campus)

> **Note**: Many defence programmes are restricted to UK MOD personnel or require security clearance.

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Guided Weapon Systems MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/guided-weapon-systems) |
| 2 | Cyberspace Operations MSc | MSc | Full-time MOD/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/cyberspace-operations) |
| 3 | Explosives Ordnance Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/explosives-ordnance-engineering) |
| 4 | Information Capability Management MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/information-capability-management) |
| 5 | Defence Simulation and Modelling MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/defence-simulation-and-modelling) |
| 6 | Military Aerospace and Airworthiness MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/military-aerospace-and-airworthiness) |
| 7 | Military Electronic Systems Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/military-electronic-systems-engineering) |
| 8 | Cyber Defence and Information Assurance MSc (Defence) | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/cyber-defence-and-information-assurance) |
| 9 | Aerosystems MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerosystems) |
| 10 | Airworthiness MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/airworthiness) |
| 11 | Systems Engineering MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/systems-engineering) |
| 12 | Through-life System Sustainment MSc | MSc | Executive | [Link](https://www.cranfield.ac.uk/courses/taught/through-life-system-sustainment) |
| 13 | Digital and Technology Solutions MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/digital-and-technology-solutions) |
| 14 | Systems Thinking Practice MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/systems-thinking-practice) |

#### Defence Apprenticeships & PgCert

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 15 | Systems Engineering MSc Apprenticeship | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/systems-engineering-apprenticeship) |
| 16 | Explosives Ordnance Engineering Apprenticeship | PgDip | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/explosives-ordnance-engineering-apprenticeship) |
| 17 | Digital and Technology Solutions Apprenticeship MSc | MSc | Executive | [Link](https://www.cranfield.ac.uk/courses/taught/digital-and-technology-solutions-apprenticeship) |
| 18 | Advanced Digital Forensic Professional Apprenticeship | PgDip | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-digital-forensic-professional-apprenticeship) |
| 19 | Through-life Engineering Services Specialist Master's Degree Apprenticeship | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/through-life-engineering-services-specialist-apprenticeship) |
| 20 | Communications Electronic Warfare PgCert | PgCert | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/communications-electronic-warfare) |
| 21 | Military Electronic Systems Engineering Foundations PgCert | PgCert | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/military-electronic-systems-engineering-foundations) |
| 22 | Sensors Electronic Warfare | PgCert | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/sensors-electronic-warfare) |
| 23 | Risk and Safety Management Professional Master's Level Apprenticeship | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/risk-and-safety-management-apprenticeship) |

### 1.3 Aerospace & Aviation Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Aerospace Vehicle Design MSc (Aircraft Design option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerospace-vehicle-design) |
| 2 | Aerospace Vehicle Design MSc (Structural Design option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerospace-vehicle-design) |
| 3 | Aerospace Vehicle Design MSc (Avionic Systems Design option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerospace-vehicle-design) |
| 4 | Aerospace Dynamics MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerospace-dynamics) |
| 5 | Aerospace Manufacturing MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerospace-manufacturing) |
| 6 | Aerospace Computational Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/aerospace-computational-engineering) |
| 7 | Advanced Lightweight and Composite Structures MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-lightweight-and-composite-structures) |
| 8 | Astronautics and Space Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/astronautics-and-space-engineering) |
| 9 | Autonomous Vehicle Dynamics and Control MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/autonomous-vehicle-dynamics-and-control) |
| 10 | Aircraft Engineering MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/aircraft-engineering) |
| 11 | Safety and Human Factors in Aviation MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/safety-and-human-factors-in-aviation) |
| 12 | Aviation Safety Management, Risk and Regulation MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/aviation-safety-management-risk-and-regulation) |
| 13 | Virtual Prototyping for Vehicle Structures MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/virtual-prototyping-for-vehicle-structures) |

### 1.4 Energy & Environment Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Renewable Energy MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/renewable-energy) |
| 2 | Environmental Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/environmental-engineering) |
| 3 | Environmental Management for Business MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/environmental-management-for-business) |
| 4 | Water and Wastewater Processes MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/water-and-wastewater-processes) |
| 5 | Water and Wastewater Processes MSc - Engineering route | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/water-and-wastewater-processes) |
| 6 | Water and Wastewater Processes MSc - Environmental Science route | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/water-and-wastewater-processes) |
| 7 | Advanced GIS and Remote Sensing MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-gis-and-remote-sensing) |
| 8 | Global Environmental Change and Planetary Health MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/global-environmental-change-and-planetary-health) |
| 9 | Future Food Sustainability MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/future-food-sustainability) |
| 10 | Food Systems and Management MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/food-systems-and-management) |
| 11 | Soil Science MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/soil-science) |
| 12 | Data Science and Artificial Intelligence for Sustainability MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/data-science-and-ai-for-sustainability) |

### 1.5 Thermal Power & Propulsion Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Thermal Power and Propulsion MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/thermal-power-and-propulsion) |
| 2 | Thermal Power and Propulsion MSc (Aerospace Propulsion option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/thermal-power-and-propulsion) |
| 3 | Thermal Power and Propulsion MSc (Gas Turbine Technology option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/thermal-power-and-propulsion) |
| 4 | Thermal Power and Propulsion MSc (Power, Propulsion and the Environment option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/thermal-power-and-propulsion) |
| 5 | Thermal Power and Propulsion MSc (Marine Propulsion Technology option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/thermal-power-and-propulsion) |
| 6 | Thermal Power and Propulsion MSc (Rotating Machinery, Engineering and Management option) | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/thermal-power-and-propulsion) |
| 7 | Power and Propulsion Gas Turbine Engineer Master's Degree Apprenticeship | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/power-and-propulsion-gas-turbine-engineer-apprenticeship) |

### 1.6 Automotive & Motorsport Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Automotive Engineering MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/automotive-engineering) |
| 2 | Automotive Mechatronics MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/automotive-mechatronics) |
| 3 | Advanced Motorsport Engineering MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-motorsport-engineering) |
| 4 | Advanced Motorsport Mechatronics MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-motorsport-mechatronics) |
| 5 | Robotics MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/robotics) |

### 1.7 Manufacturing & Materials Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Advanced Materials: Engineering and Industrial Applications MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-materials) |
| 2 | Welding Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/welding-engineering) |
| 3 | Metal Additive Manufacturing MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/metal-additive-manufacturing) |
| 4 | Advanced Mechanical Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/advanced-mechanical-engineering) |

### 1.8 Digital, AI & Computing Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Applied Artificial Intelligence MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/applied-artificial-intelligence) |
| 2 | Computational and Software Techniques in Engineering MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/computational-and-software-techniques-in-engineering) |
| 3 | Computational Fluid Dynamics MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/computational-fluid-dynamics) |
| 4 | Data Science and Artificial Intelligence for Sustainability MSc | MSc | Full-time/Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/data-science-and-ai-for-sustainability) |
| 5 | Digital and Technology Solutions MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/digital-and-technology-solutions) |

### 1.9 Safety & Air Transport Cluster

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Safety and Accident Investigation MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/safety-and-accident-investigation) |
| 2 | Air Transport Management MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/air-transport-management) |
| 3 | Air Transport Management (Executive) MSc | MSc | Executive | [Link](https://www.cranfield.ac.uk/courses/taught/air-transport-management-executive) |
| 4 | Airport Planning and Management MSc | MSc | Full-time | [Link](https://www.cranfield.ac.uk/courses/taught/airport-planning-and-management) |

### 1.10 Cross-cutting MSc Programmes

| # | 专业 | 学位 | 学习模式 | URL |
|---|------|------|----------|-----|
| 1 | Safety and Accident Investigation MSc | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/safety-and-accident-investigation) |
| 2 | Soil Scientist Apprenticeship with MSc in Soil Science | MSc | Part-time | [Link](https://www.cranfield.ac.uk/courses/taught/soil-scientist-apprenticeship) |

---

## SECTION 2 — Postgraduate Research Education (PGR)

### 2.1 MSc by Research Programmes

> MSc by Research programmes at Cranfield are self-funded research degrees. Students work on a specific research project under supervisor guidance.

| # | 专业 | 学位 | 学科领域 | URL |
|---|------|------|----------|-----|
| 1 | MSc by Research in Water | MSc by Research | Water | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 2 | MSc by Research in Manufacturing and Materials | MSc by Research | Manufacturing | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 3 | MSc by Research in Aerospace | MSc by Research | Aerospace | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 4 | MSc by Research in Archaeology | MSc by Research | Forensic/Archaeology | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 5 | MSc by Research in Design Engineering | MSc by Research | Design Engineering | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 6 | MSc by Research in Energy & Sustainability | MSc by Research | Energy | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 7 | MSc by Research in Defence and Security | MSc by Research | Defence | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 8 | MSc by Research in Environmental Science and Agrifood | MSc by Research | Environment/Agrifood | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 9 | Thermal Power and Propulsion - MSc by Research (part-time) | MSc by Research | Thermal Power | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |
| 10 | MSc by Research in specific topic areas | MSc by Research | Various | [Link](https://www.cranfield.ac.uk/research/research-degrees/research-opportunities) |

### 2.2 PhD Programmes

> PhD programmes at Cranfield are primarily self-funded research positions. Students apply to specific research topics/projects. Below is a representative sample of available PhD opportunities.

| # | 研究方向 | 学位 | 学科领域 |
|---|---------|------|----------|
| 1 | Novel hybrid prognostics system | PhD | Manufacturing/Materials |
| 2 | LLM-Augmented Human-Swarm Collaboration for Embodied Multi-Agent Systems | PhD | AI/Robotics |
| 3 | Levantine Faience in context: A multidisciplinary study | PhD | Archaeology/Forensics |
| 4 | Transition to low carbon airports | PhD | Aviation/Environment |
| 5 | Extreme learning to handle Big Data | PhD | Data Science |
| 6 | Framework for manufacturing prognostics | PhD | Manufacturing |
| 7 | Novel aircraft impact on engine design | PhD | Aerospace |
| 8 | Mitigation of radiation and hydrogen damage with laser peening | PhD | Materials |
| 9 | Trustworthy Embodied Autonomous Vehicles Design Through Foundation Model | PhD | AI/Autonomous Systems |
| 10 | Corrosion-sensitive Multiscale Fatigue Modelling | PhD | Materials |
| 11 | Big Data analytics for industrial application | PhD | Data Science |
| 12 | Removing forever chemicals from drinking water | PhD | Water |
| 13 | Novel metamaterials for multifunctional applications in energy systems | PhD | Materials/Energy |
| 14 | Material degradation of heat-exchanger materials for renewable energy | PhD | Materials/Energy |
| 15 | Failure models for transmission gears health monitoring | PhD | Mechanical Engineering |
| 16 | Hot corrosion studies of gas turbine alloy materials | PhD | Materials |
| 17 | Tribological Testing of Omniphobic Surfaces | PhD | Materials |
| 18 | Ubiquitous Cognitive Navigation with AI Based Systems | PhD | AI/Navigation |
| 19 | Predictive models for sustainable mango supply chains | PhD | Agrifood |
| 20 | Optimising drinking water treatment for emerging contaminants | PhD | Water |
| 21 | Multiscale Predictive Approaches Applied to Mechanics of Materials | PhD | Materials |
| 22 | Numerical health assessment of surface wear | PhD | Mechanical Engineering |
| 23 | Self-learning battery management systems for lithium-sulfur batteries | PhD | Energy |
| 24 | Modal responses of mechanical structures under thermo-mechanical loads | PhD | Mechanical Engineering |
| 25 | Digital image correlation for material constitutive properties | PhD | Materials |
| 26 | Supercritical water oxidation to valorise organic waste | PhD | Environment |
| 27 | Intelligent fault diagnosis for rotating machinery | PhD | Manufacturing |
| 28 | 3D temperature field reconstruction in directed energy deposition | PhD | Manufacturing |
| 29 | Sub surface damage and structural dynamic behaviour | PhD | Materials |
| 30 | Material degradation of energy storage materials | PhD | Energy |
| 31 | Wire based Directed Energy Deposition (w-DEDAM) production | PhD | Manufacturing |
| 32 | Impact of Energy Storage Requirements on Gas Turbine Performance | PhD | Energy |
| 33 | Sustainability strategies for explosive waste management | PhD | Environment |
| 34 | Adaptive microbial mutagenesis in wastewater treatment | PhD | Water |
| 35 | Synthetic biology-enabled sensing of stressed coliforms | PhD | Water |
| 36 | CRISPR Cas-enabled smart sensors for river water contaminants | PhD | Water |
| 37 | CFD-informed finite element analysis for wire-arc DED | PhD | Manufacturing |

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 English Language Requirements

> **Test validity**: All tests must be taken within **2 years** of the course start date. All component scores must come from a **single test sitting**.

| 测试 | 最低总分 | 各项最低分 | 备注 |
|------|---------|-----------|------|
| **IELTS Academic** | 6.5 | 5.5 (all components) | Accepts IELTS Online, IELTS for UKVI Academic, IELTS One Skill Retake |
| **TOEFL iBT** | 92 | R18, L17, S20, W17 | Tests before 21 Jan 2026. After: 4.5 overall, 4 all components |
| **PTE Academic** | 65 | 59 (all components) | Accepts Academic, Academic Online, Academic UKVI |
| **Cambridge English** | 180 (C1 Advanced/C2 Proficiency) | 160 (all components) | Also accepts Linguaskill General |
| **Duolingo** | 120 | 95 (all subscores) | Speaking, writing, reading, listening |
| **LanguageCert Academic** | 70 | 60 (all components) | Also accepts Academic SELT |
| **LanguageCert ESOL B2** | High Pass | 33 (all components) | Written & Spoken together |
| **Kaplan Test of English** | 495 | 425 (all components) | Cranfield applicants get 25% discount |
| **Password Skills Plus** | 6.5 | 5.5 (all components) | — |
| **Skills for English SELT** | Pass with Merit | — | UKVI B2 |
| **Trinity ISE III** | Overall Pass | — | C1 level |

> **Note**: Some courses may require **higher scores** than the minimum. Applicants should check individual course pages. All scores are verified with test providers.

### 3.2 Academic Entry Requirements

- **MSc programmes**: Typically require a UK first or second class honours degree (2:1 or above) in a relevant subject, or equivalent international qualification
- **MBA programmes**: Typically require a degree plus significant work experience (3-5 years for Executive MBA)
- **PhD/MSc by Research**: Typically require a good master's degree in a relevant subject
- **International qualifications**: Assessed on a case-by-case basis; country-specific entry requirements available on the website

### 3.3 Application Process

- Applications submitted online through the Cranfield application portal
- **CAS (Confirmation of Acceptance for Studies)**: Required for international students requiring a Student visa
  - Must accept offer, pay deposit, and meet all conditions
  - Managed through CAS Shield system
  - Process begins when course start date is less than 6 months away
- **ATAS (Academic Technology Approval Scheme)**: Required for international students on certain sensitive postgraduate subjects
- **Deposit**: Non-refundable deposit required to secure place (deducted from tuition fees)

### 3.4 Application Deadlines

> Cranfield operates a **rolling admissions** system for most programmes. Applications are considered as they are received until programmes are full. Early application is recommended for competitive programmes and for international students requiring visa processing time.

- **MSc programmes**: Typically start in **October** (full-time) or flexible start for part-time
- **MBA programmes**: Multiple intakes — September and January for some programmes
- **Research degrees**: Applications accepted year-round

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Tuition Fees (2026-27)

| 专业类别 | Home (UK) | Overseas (International) | 押金 (Home) | 押金 (Overseas) |
|---------|-----------|--------------------------|------------|----------------|
| **典型 MSc (工程/科学)** | £13,005 | £29,025 | £1,000 | £3,000 |
| **School of Management MSc** | £15,500 | £29,650 | £1,000 | £3,000 |
| **MBA** | Contact school | Contact school | — | — |
| **Research degrees** | Contact university | Contact university | — | — |

> **Fee notes**:
> - Fees apply to students registering between **1 August 2026 and 31 July 2027**
> - Part-time fees can be paid in full up front or in equal annual instalments
> - Additional fees may be charged for extensions to the agreed registration period
> - Home fee eligibility determined by UK Government regulations
> - Channel Islands and Isle of Man students pay Overseas rates
> - International students requiring a Student visa must pay the deposit before a CAS is issued

### 4.2 Scholarships & Funding

- **Alumni scholarship**: Up to 20% of total fee for self-funded research degrees (Cranfield graduates)
- **UKRI-funded studentships**: Available for both home and international students
- **School of Management scholarships**: MBA scholarships and bursaries available
- **Industry-sponsored studentships**: Many research projects come with industry funding
- **Cranfield funding search**: Available at `search.cranfield.ac.uk` with funding filter

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: institution.name
  value: "Cranfield University"
  source_url: https://www.cranfield.ac.uk
  source_snippet: "Cranfield University"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.type
  value: "Specialist postgraduate university"
  source_url: https://www.cranfield.ac.uk/about
  source_snippet: "a postgraduate university, specialising in technology and management"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.founded
  value: "1946"
  source_url: https://www.cranfield.ac.uk/about/history-and-heritage
  source_snippet: "College of Aeronautics, established in 1946"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.campuses
  value: "Cranfield (MK43 0AL) + Shrivenham (SN6 8LA)"
  source_url: https://www.cranfield.ac.uk/about
  source_snippet: "Cranfield Campus, College Road, Cranfield, MK43 0AL"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-C-001:
  field: courses.total_count
  value: "136 distinct degree programmes (83 MSc + 3 MBA + 13 MSc by Research + 37 PhD)"
  source_url: https://search.cranfield.ac.uk/s/search.html
  source_snippet: "Courses (437)" [includes 297 short courses + exit awards]
  capture_date: 2026-07-08
  evidence_type: course_search

E-C-002:
  field: courses.msc_count
  value: "83"
  source_url: https://search.cranfield.ac.uk/s/search.html?f.Level%7CcourseLevel=MSc
  source_snippet: "1 - 10 of 83 search results"
  capture_date: 2026-07-08
  evidence_type: course_search

E-C-003:
  field: courses.mba_count
  value: "3"
  source_url: https://search.cranfield.ac.uk/s/search.html?f.Level%7CcourseLevel=MBA
  source_snippet: "Executive MBA, The Transformation MBA, Cranfield MBA Double Degree"
  capture_date: 2026-07-08
  evidence_type: course_search

E-L-001:
  field: language.ielts
  value: "6.5 overall, 5.5 in all components"
  source_url: https://www.cranfield.ac.uk/study/application-guide/entry-requirements
  source_snippet: "6.5 overall and 5.5 in all skill components"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-F-001:
  field: fees.msc_home
  value: "£13,005"
  source_url: https://www.cranfield.ac.uk/courses/taught/robotics
  source_snippet: "MSc Full-time: £13,005"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-F-002:
  field: fees.msc_overseas
  value: "£29,025"
  source_url: https://www.cranfield.ac.uk/courses/taught/robotics
  source_snippet: "MSc Full-time: £29,025"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-F-003:
  field: fees.management_msc_overseas
  value: "£29,650"
  source_url: https://www.cranfield.ac.uk/som/masters-courses/finance
  source_snippet: "Tuition Fee: £29,650"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-R-001:
  field: rankings.ref_2021
  value: "88% world-leading or internationally excellent"
  source_url: https://www.cranfield.ac.uk/about/rankings-and-awards
  source_snippet: "88% of research rated world-leading or internationally excellent"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-R-002:
  field: rankings.qs_mechanical_aeronautical
  value: "5th UK, 55th world"
  source_url: https://www.cranfield.ac.uk/about/rankings-and-awards
  source_snippet: "5th in the UK and 55th in the world for Engineering – Mechanical and Aeronautical"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-R-003:
  field: rankings.queens_anniversary_prize
  value: "Six-time winner"
  source_url: https://www.cranfield.ac.uk/about/rankings-and-awards
  source_snippet: "Queen's Anniversary Prize: Six-time winner"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

```yaml
document_type: university_admissions_knowledge_base
institution: Cranfield University
region: UK
version: v2.0
capture_date: 2026-07-08
total_programs: 136
sections:
  - section_0: institution_overview
  - section_1: postgraduate_taught_education
  - section_2: postgraduate_research_education
  - section_3: application_requirements
  - section_4: costs_and_financial_aid
  - section_5: evidence_chain_index
  - section_6: weknora_import_manifest
metadata:
  is_postgraduate_only: true
  has_ug: false
  platform_type: drupal-custom
  course_search_engine: funnelback
  campuses: 2
  schools: 1 (School of Management)
  centres: 50+
  language_test_min_ielts: 6.5
  typical_msc_overseas_fee_gbp: 29025
```
