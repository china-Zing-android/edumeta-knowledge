# 2026-07 院校 Markdown 入库分级报告

> 历史报告：本页保留 `d41114f` 阶段的 345/16/78 技术口径。当前自动发布口径已升级为规则集 `2026-07-27.1`，最新结果为 276 passed / 75 needs_review / 88 failed，见 `docs/operations/incremental-quality-audit-runbook.md`。

## 1. 结论先行

本报告基于 448 份 Markdown、439 个启用院校、当前 Parser 全量 preflight，以及提交 `d41114f` 前后的 Parser 对照解析生成。

“可以入库”必须区分两个口径：

1. **技术可入库**：能够生成合法的 `catalog_entries`、`source_registry`、`url_manifest`，并通过 PostgreSQL staging 和 OpenSearch 发布链路。
2. **像 MIT 一样可验收发布**：除技术可入库外，还完成目录数量对账、事实提取、来源完整性和真实 QA。

按技术口径，当前有 345 所通过；按 MIT 完整验收口径，目前只有 MIT 通过。其余 344 所可用于 L1 院校/专业检索，但不能自动承诺学费、申请截止时间、语言要求等事实型回答与 MIT 一样完整。

| 分类 | 数量 | 当前处理 |
|---|---:|---|
| MIT 完整基线 | 1 | 可按现有 MIT 验收口径入库和测试 |
| 旧 Parser 已能通过的技术可入库院校 | 210 | 包含 MIT；可进 staging/L1，非 MIT 院校仍需业务完整性抽检 |
| 本次通用 Parser 升级后新增通过 | 135 | 可进 staging/L1，必须使用当前版本，不能退回旧 Parser |
| 已通过但目录条数仅 5-9 条 | 21 | 属于上述 345 的风险子集，建议发布前复核 |
| 条件审核 | 16 | 默认不导入；需要补齐目录来源或确认专门院校例外 |
| 当前失败 | 78 | 默认禁止导入；19 份较完整文档可修复，59 份明显是摘要/残缺版本 |
| 重复文件 | 9 | 禁止重复导入，只保留权威版本 |

机器可读的逐校结论见 `data/raw-md/universities/parser-compatibility-results.jsonl`。

## 2. 真正达到 MIT 同级标准的院校

目前只有 `mit`。

MIT 已具备：

- 157 条目录记录精确对账：55 SB + 17 Minor + 85 graduate offerings。
- 241 条 `quick_facts`，支持学费、截止日期、语言要求、考试要求、资助等快速事实查询。
- 稳定的目录、来源、URL、实体上下文关联。
- 已有真实 QA 和增量链路验证基础。

其余 344 所技术通过院校的共同差异：

- `quick_facts` 当前全部为 0，不能按 MIT Fast Path 回答事实型问题。
- 没有逐校的“官方项目总数 vs 实际解析数”对账规则。
- 通过条件目前主要是 `catalog_entries >= 5`，只能证明 Parser 有输出，不能证明内容完整。
- URL 已提取到 `source_registry/url_manifest`，但在 `WEKNORA_IMPORT_ENABLED=false` 时尚未进入 WeKnora 内容库。
- 尚未执行逐校真实 QA。

因此，非 MIT 院校当前适合验证：

- 某院校有没有某专业。
- 某专业在哪些院校存在。
- 某院校有哪些学院、专业或学位项目。
- 专业、院系、学位层级和原始来源的结构化检索。

暂时不应承诺：

- 学费、截止日期、TOEFL/IELTS、GRE/GMAT、资助等事实一定能从 Fast Path 返回。
- Markdown 中声明的全部项目都已完整入库。
- WeKnora 深度内容已经可检索。

## 3. 旧版本已经能技术入库的 210 所

这些文件在本次 Parser 修改前已经能解析出至少 5 条目录记录。本次修改不是它们能够入库的前提。

其中 `mit` 是完整验收基线，其余 209 所属于“L1 技术可入库”，不自动等于“MIT 同级完整”。

### AU (1)

`melbourne`

### CA (1)

`lakehead_university`

### CH (1)

`eth_zurich`

### SG (1)

`sutd`

### UK (47)

`aberystwyth`、`aston`、`birkbeck_london`、`birmingham`、`birmingham_city`、`bradford`、`canterbury_christ_church`、`cardiff`、`coventry`、`cranfield`、`derby`、`edinburgh`、`glasgow_caledonian`、`goldsmiths`、`hertfordshire`、`imperial`、`kcl`、`keele`、`kent`、`lancaster`、`lincoln`、`liverpool`、`london_metropolitan`、`london_school_of_hygiene_and_tropical_medicine`、`london_south_bank`、`lse`、`manchester_metropolitan`、`newcastle`、`northumbria`、`nottingham_trent`、`plymouth`、`portsmouth`、`robert_gordon`、`roehampton`、`royal_holloway_london`、`sheffield`、`sheffield_hallam`、`stirling`、`strathclyde`、`surrey`、`swansea`、`the_arts_london`、`ucl`、`university_of_lancashire`、`warwick`、`wolverhampton`、`york`

### US (159)

`arkansas`、`asu`、`au`、`auburn`、`baylor`、`baylorcom`、`berkeley`、`binghamton`、`brandeis`、`brown`、`bu`、`byu`、`calpolyslo`、`caltech`、`casewestern`、`centralmichigan`、`clark`、`clarkson`、`cmu`、`coloradostate`、`columbia`、`cornell`、`csulb`、`cuboulder`、`cudenver`、`cuny`、`dartmouth`、`depaul`、`drexel`、`duke`、`emory`、`fiu`、`fordham`、`fsu`、`georgetown`、`georgiatech`、`gonzaga`、`gsu`、`gwu`、`hartford`、`harvard`、`howard`、`iit`、`iu`、`iuindianapolis`、`jhu`、`kansasstate`、`kentstate`、`ku`、`lehigh`、`lmu`、`loyolachicago`、`lsu`、`marquette`、`memphis`、`miamioh`、`missourisandt`、`mit`、`mizzou`、`msu`、`nau`、`ncstate`、`njit`、`nmsu`、`northeastern`、`northwestern`、`notredame`、`nyu`、`ohiou`、`oklahomastate`、`olemiss`、`oregonstate`、`pennstate`、`pitt`、`pratt`、`princeton`、`purdue`、`rice`、`rpi`、`rutgers`、`scu`、`sdsu`、`sjsu`、`slu`、`stanford`、`stevens`、`stonybrook`、`swarthmore`、`syracuse`、`texasam`、`ttu`、`tufts`、`tulane`、`ua`、`uaf`、`ualbany`、`uarizona`、`ucdavis`、`ucf`、`uchicago`、`uci`、`ucincinnati`、`ucla`、`uco`、`uconn`、`ucr`、`ucsb`、`ucsc`、`ucsd`、`ucsf`、`udelaware`、`uf`、`uga`、`uh`、`uhm`、`uidaho`、`uiowa`、`ukentucky`、`umassamherst`、`umassboston`、`umiami`、`umich`、`umkc`、`umn`、`umsl`、`unc`、`unccharlotte`、`unl`、`unlv`、`unm`、`unr`、`unt`、`uofl`、`uofutah`、`upenn`、`urochester`、`usc`、`uscarolina`、`utaustin`、`utep`、`uva`、`uvm`、`uw`、`uwmadison`、`uwmilwaukee`、`uwyo`、`vanderbilt`、`wakeforest`、`washu`、`waynestate`、`wesleyan`、`wmmary`、`wmu`、`wpi`、`wsu`、`wvu`、`xavierlouisiana`、`yale`、`yeshiva`

## 4. 本次 Parser 版本升级后新增可技术入库的 135 所

这 135 所在旧 Parser 中不能达到目录闸门，在当前版本中已通过。必须使用提交 `d41114f` 或之后的版本。

修复的是通用格式类型，不是单校补丁：

- 专业表不再强制要求第一列必须是 `#` 编号。
- 支持 `/course/...` 等相对 URL，并基于院校官网补全。
- 支持表内 `School/Faculty/College/Department` 字段。
- 支持中文“生成日期、采集日期、数据捕获日期”。
- 修复同一项目在多个来源表出现时的重复 `entry_id`。

旧版失败原因分布：107 所完全解析不到目录，26 所识别不到日期，2 所只解析出 1 条目录；升级后均达到当前技术闸门。

### AU (33)

`australian_catholic_university`、`australian_national_university`、`bond_university`、`canberra`、`central_queensland_university`、`charles_darwin_university`、`charles_sturt_university`、`curtin_university`、`federation_university`、`flinders_university`、`james_cook_university`、`la_trobe_university`、`macquarie_university`、`monash_university`、`murdoch_university`、`notre_dame_australia`、`qut`、`rmit_university`、`southern_cross_university`、`swinburne_university`、`the_university_of_adelaide`、`the_university_of_sydney`、`torrens_university_australia`、`une`、`university_of_newcastle_australia`、`university_of_southern_queensland`、`university_of_tasmania`、`university_of_the_sunshine_coast`、`university_of_wollongong`、`uq`、`uwa`、`victoria_university`、`western_sydney_university`

### CA (37)

`acadia_university`、`athabasca_university`、`brock_university`、`carleton_university`、`dalhousie_university`、`emily_carr_university`、`laurentian_university`、`mcgill_university`、`mcmaster_university`、`memorial_university_of_newfoundland`、`mount_royal_university`、`nosm_university`、`ontario_tech_university`、`queens_university`、`royal_military_college`、`saint_marys_university`、`simon_fraser_university`、`st_francis_xavier_university`、`st_thomas_university`、`the_kings_university`、`toronto_metropolitan_university`、`trent_university`、`unbc`、`university_of_alberta`、`university_of_british_columbia`、`university_of_calgary`、`university_of_guelph`、`university_of_lethbridge`、`university_of_new_brunswick`、`university_of_ottawa`、`university_of_regina`、`university_of_saskatchewan`、`university_of_toronto`、`university_of_waterloo`、`upei`、`vancouver_island_university`、`western_university`

### IE (2)

`trinity_college_dublin`、`university_of_limerick`

### NZ (4)

`auckland_university_of_technology_aut`、`university_of_auckland`、`university_of_canterbury_nz`、`university_of_waikato`

### SG (6)

`insead`、`nafa`、`ntu`、`nus`、`sg_smu`、`singapore_institute_of_management`

### UK (35)

`anglia_ruskin`、`bangor`、`bristol`、`brunel_london`、`cambridge`、`city_st_george_s_london`、`de_montfort`、`dundee`、`durham`、`east_london`、`edinburgh_napier`、`greenwich`、`harper_adams`、`heriot_watt`、`huddersfield`、`hull`、`kingston`、`leeds`、`leeds_beckett`、`loughborough`、`middlesex`、`northampton`、`nottingham`、`oxford_brookes`、`reading`、`salford`、`soas_london`、`south_wales`、`st_andrews`、`st_georges`、`sussex`、`uea`、`ulster`、`uwe_bristol`、`westminster`

### US (18)

`buffalo`、`calstatela`、`ccny`、`clemson`、`denver`、`fau`、`humboldt`、`indianastate`、`isu`、`michigantech`、`mines`、`osu`、`portlandstate`、`rutgerscamden`、`uiuc`、`usf`、`utsa`、`vcu`

## 5. 已通过但需要优先抽检的 21 所

下面 21 所虽然达到当前最低闸门，但只解析出 5-9 条目录。对综合大学而言，这通常意味着 Markdown 中的项目表缺少逐行来源 URL，或 Parser 只命中了局部表。

`university_of_regina`、`auckland_university_of_technology_aut`、`bristol`、`ccny`、`flinders_university`、`isu`、`michigantech`、`rutgerscamden`、`trinity_college_dublin`、`uiuc`、`usf`、`harper_adams`、`university_of_the_sunshine_coast`、`kingston`、`middlesex`、`mines`、`royal_military_college`、`the_kings_university`、`buffalo`、`denver`、`university_of_ottawa`

处理建议：

- 可以进入 staging 做接口验证。
- 在确认“声明项目总数”和“解析目录数”一致前，不应作为完整院校发布。
- 不能因为已经大于 5 条就跳过内容完整性检查。

## 6. 条件审核的 16 所

这 16 所 schema 和引用关系合法，但只解析出 1-4 条目录，批量脚本默认拦截。

| university_id | 院校 | 解析目录 | 来源 URL | 结论 |
|---|---|---:|---:|---|
| `deakin_university` | Deakin University | 3 | 18 | 文档声明约 276 个项目，当前结果明显不完整 |
| `griffith_university` | Griffith University | 1 | 26 | 文档声明约 285 个项目，很多表内 URL 为 `-` |
| `university_of_technology_sydney` | University of Technology Sydney | 1 | 3 | 文档声明约 500 个项目，缺少逐项目来源 |
| `brandon_university` | Brandon University | 2 | 17 | 有完整专业表，但表行缺少可关联 URL |
| `universite_du_quebec` | Université du Québec | 2 | 18 | 属于大学系统而非单一校区，且文档声明 1500+ 项目 |
| `university_of_manitoba` | University of Manitoba | 2 | 20 | 主要是概览和招生内容，专业行缺少来源关联 |
| `university_of_victoria` | University of Victoria | 4 | 15 | 学院和专业以汇总文本呈现，不是逐项目证据表 |
| `wilfrid_laurier_university` | Wilfrid Laurier University | 4 | 21 | A-Z 专业清单缺少逐行 URL |
| `tu_dublin` | TU Dublin | 2 | 44 | 有大规模课程清单，但项目表与来源 URL 未关联 |
| `university_college_dublin` | University College Dublin | 2 | 17 | 学院结构完整，但目录行缺少直接来源 |
| `bournemouth` | Bournemouth University | 2 | 172 | 文档声明 88 个本科项目，实际只命中 2 条 |
| `exeter` | University of Exeter | 3 | 407 | 文档声明 252 个本科项目，实际只命中 3 条 |
| `london_business_school` | London Business School | 3 | 11 | 无本科属实，但研究生项目仍未完整关联来源 |
| `queen_margaret` | Queen Margaret University | 3 | 105 | 文档声明 94 个项目，实际只命中 3 条 |
| `rockefeller` | Rockefeller University | 2 | 9 | 研究生专门院校，项目少可能真实；需声明预期项目数后可例外放行 |
| `umbc` | UMBC | 1 | 3 | 文档声明 180+ 项目，当前结果明显不完整 |

其中只有 `rockefeller` 具备“小于 5 条可能仍然完整”的合理业务解释。它仍不能直接绕过闸门，应先在 manifest 中增加经过审核的预期目录数量或专门院校标记，再执行精确对账。

其余 15 所需要补齐逐项目 URL、统一目录表格式，或明确文档只是局部快照，不能以完整院校身份发布。

## 7. 当前失败的 78 所

### 7.1 19 份内容较多、存在修复价值的文档

这些文件不应直接入库，但不是都需要重新采集。

| 类型 | 院校 | 主要问题 | 修复后是否可能入库 |
|---|---|---|---|
| Parser 合同扩展候选 | `bath`、`brighton`、`leicester`、`maynooth_university`、`oxford`、`dublin_city_university` | 有较多课程行和 URL，但表头多使用“课程名称”等当前未作为目录合同的字段 | 可以；应增加明确的通用课程目录适配器，不能只把“课程”加入模糊词典 |
| 内容和 Parser 都需整理 | `university_of_south_australia`、`university_college_cork`、`university_of_galway`、`massey_university`、`york_university`、`ljmu` | 有项目清单，但只有部分行有 URL；部分日期不是机器可识别格式 | 可以；先补 ISO 日期和逐项目来源，再运行新适配器 |
| 来源证据不足 | `edith_cowan_university`、`university_of_windsor`、`essex_of`、`glasgow`、`manchester`、`southampton`、`ocad_university` | 文档中有项目名称，但项目表基本没有行级来源 URL；OCAD 还缺 ISO 日期 | 需要补采；不能仅靠学校首页 URL 给所有项目背书 |

日期问题的实际验证结果：

- `york_university` 补一个 ISO 日期后能解析 14 条，但文档声明 200+ 项目，仍不完整。
- `ocad_university` 补日期后只能解析 1 条，仍不满足目录完整性。
- `ljmu` 补日期后仍为 0 条，核心问题不是日期，而是目录来源关联。

### 7.2 59 份摘要或残缺版本

这 59 份文件均小于 10 KB，多数只有约 120-180 行，缺少完整项目目录和逐项目来源。它们不是 Parser 小调整就能解决的数据，当前明确禁止入库。

UK：`aberdeen`、`qmul`、`queen_s_belfast`

US：`bostoncollege`、`bucknell`、`colby`、`colgate`、`csuf`、`csus`、`gmu`、`hofstra`、`hpu`、`illinoisstate`、`iowastate`、`merrimack`、`michiganstate`、`newschool`、`nova`、`oakland`、`oberlin`、`oklahoma`、`oregon`、`pacific`、`pomona`、`rit`、`rutgersnewark`、`seattleu`、`sfsu`、`smith`、`stetson`、`tcu`、`temple`、`tennessee_knoxville`、`texasstate`、`toledo`、`tulsa`、`uab`、`uakron`、`udayton`、`uhilo`、`uic`、`umb`、`umd_collegepark`、`umontana`、`uncg`、`unh`、`uofalabama`、`upr`、`uri`、`us_smu`、`usa`、`usd`、`utahstate`、`utarlington`、`utdallas`、`virginiatech`、`williams`、`wofford`、`wwu`

必须重新提供至少以下内容后才能重新 preflight：

- 明确的 ISO 数据采集日期。
- 本科、研究生目录表，而不是精选项目或学科概览。
- 每个项目的官方 URL，或可证明覆盖整个表格的官方目录 URL。
- 院校、学院、系、学位层级和项目名称的稳定关系。

## 8. 禁止重复入库的 9 份文件

以下文件与已启用权威版本代表同一院校，保留原文用于审计，但不参与自动导入：

| 禁用文件 | 权威 university_id | 原因 |
|---|---|---|
| `ca/University_of_Northern_British_Columbia_知识库_完整深度数据_v2.md` | `unbc` | 与 UNBC 文件重复 |
| `ca/University_of_Prince_Edward_Island_知识库_完整深度数据_v2.md` | `upei` | 与 UPEI 文件重复 |
| `us/American_知识库_完整深度数据_v2.md` | `au` | 与 American University 权威文件重复 |
| `us/BostonUniversity_知识库_完整深度数据_v2.md` | `bu` | 与 BU 权威文件重复 |
| `us/BrighamYoung_知识库_完整深度数据_v2.md` | `byu` | 与 BYU 权威文件重复 |
| `us/CSU_知识库_完整深度数据_v2.md` | `coloradostate` | 与 Colorado State 权威文件重复 |
| `us/MissState_知识库_完整深度数据_v2.md` | `msu` | 与 Mississippi State 权威文件重复 |
| `us/UofSC_知识库_完整深度数据_v2.md` | `uscarolina` | 与 South Carolina 权威文件重复 |
| `us/纽约大学_知识库_完整深度数据_v2.md` | `nyu` | NYU 英文文件被选为权威版本，中文文件注明 evidence 待重新采集 |

## 9. 当前允许和禁止规则

### 自动导入允许

- manifest 中 `enabled=true`。
- preflight 为 `passed`。
- 当前 Markdown SHA-256 与 preflight 记录一致。
- 使用当前 Parser 版本。

当前批量脚本按这一技术规则会选择 345 所。

### 建议只进入 staging、暂不宣称完整发布

- 除 MIT 外的 344 所技术通过院校。
- 尤其是目录数只有 5-9 条的 21 所。
- 尚未做目录总数对账、事实层提取或真实 QA 的院校。

### 默认禁止

- 16 所 `needs_review`。
- 78 所 `failed`。
- 9 份重复文件。
- Markdown 被修改后 SHA-256 与 preflight 不一致的文件。
- 缺少项目来源 URL、缺少采集日期或只包含精选项目的文件。

禁止使用 `--allow-unverified` 绕过这些限制进行正式发布。该参数只适合受控开发调试。

## 10. 下一步应补的长期闸门

当前最重要的缺口不是继续增加关键词，而是补一层通用完整性合同：

1. 每份 Markdown 声明 `catalog_scope=complete|partial|specialized`。
2. 声明本科、研究生、辅修等预期数量或允许范围。
3. preflight 比较声明数量和实际解析数量，不能只判断是否大于 5。
4. 专门院校通过显式 `expected_catalog_count` 放行，不能写单校判断。
5. `quick_facts` 是否存在应作为事实型 Fast Path 的独立能力标记。
6. WeKnora 导入状态应作为深度检索能力标记，不与 L1 技术入库混为一谈。

完成这层闸门后，才能把“技术能导入”稳定升级为“像 MIT 一样可验收发布”。
