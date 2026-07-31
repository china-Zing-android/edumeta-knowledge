export type FieldNote = {
  description: string
  example: string
}

const commonFieldNotes: Record<string, FieldNote> = {
  university_id: { description: '院校的稳定机器标识，用于把同一院校的版本、记录和检索范围串起来。', example: 'mit' },
  program_id: { description: '外部或上游提供的专业标识。没有稳定标识时可以为空。', example: 'null' },
  entry_id: { description: '专业目录记录的稳定 ID，供专业、事实和上下文之间关联。', example: 'ent_mit_undergraduate_sb_18_computer_science' },
  source_id: { description: '官网来源的稳定 ID，指向 source_registry 中的一条来源记录。', example: 'src_mit_catalog_mit_edu_degree_charts_computer_science' },
  source_url: { description: '抓取或发现该记录时使用的原始 URL，保留证据入口。', example: 'https://catalog.mit.edu/degree-charts/computer-science-course-6-3' },
  canonical_url: { description: '归一化后的官网 URL，用于去重、版本比较和精确检索。', example: 'https://catalog.mit.edu/degree-charts/computer-science-course-6-3' },
  topics: { description: '这条记录覆盖的主题标签，用于主题过滤和检索路由。', example: '["catalog", "programs", "computer_science"]' },
  entry_ids: { description: '与一个来源或 URL 关联的专业目录记录 ID 列表。', example: '["ent_mit_undergraduate_sb_18_computer_science"]' },
  source_ids: { description: '上下文或主题可用的来源 ID 列表，用于继续查看证据。', example: '["src_mit_catalog_mit_edu_degree_charts_computer_science"]' },
  official_source: { description: '是否确认来自院校官方域名或官方维护的页面。', example: 'true' },
  priority: { description: '来源优先级，数值越小通常越优先作为主证据。', example: '1' },
  capture_date: { description: '这条数据被解析或采集的日期。', example: '"2026-07-04"' },
  last_verified: { description: '最近一次验证来源仍有效且内容可用的日期。', example: '"2026-07-04"' },
  dataset_version: { description: '产物所属的数据集版本，用于跨 JSONL 对齐和回滚。', example: '"mit_20260704_v2"' },
  source_version: { description: '来源自身的版本信息，没有时为空。', example: 'null' },
  status: { description: '记录生命周期状态，常见值为 active、inactive、deprecated 或 superseded。', example: '"active"' },
  content_hash: { description: '来源内容的哈希值，用于判断内容是否变化。', example: 'null' },
  error_message: { description: '解析、抓取或导入失败时的人类可读错误信息。', example: 'null' },
}

const fieldNotes: Record<string, Record<string, FieldNote>> = {
  catalog_entries: {
    entry_id: { description: '一条专业或学位目录记录的稳定 ID。它是专业检索结果的主键。', example: '"ent_mit_undergraduate_sb_18_computer_science"' },
    school: { description: '负责该专业的学校或学院名称。', example: '"School of Engineering"' },
    department: { description: '负责该专业的院系、部门或学术单位。', example: '"Electrical Engineering and Computer Science"' },
    level: { description: '教育层级，用来区分本科、研究生和非学位项目。', example: '"undergraduate"' },
    degree_level: { description: '学位或项目类型，例如 SB、SM、MEng、PhD 或 Minor。', example: '"SB"' },
    degree_full_name: { description: '学位类型的完整名称。结构化代码不足以表达含义时使用。', example: '"Bachelor of Science"' },
    course_code: { description: '院校目录中的课程或专业编号。', example: '"6-3"' },
    program_name: { description: '面向用户展示和检索的专业名称。', example: '"Computer Science and Engineering"' },
    canonical_program_name: { description: '归一化后的专业名称，用于合并别名和比较。', example: '"Computer Science and Engineering"' },
    aliases: { description: '专业的别名、缩写或历史名称列表。', example: '["Course 6-3", "6-3"]' },
    discipline_ids: { description: '标准学科分类 ID 列表，用于按学科筛选。', example: '["computer_science"]' },
    discipline_labels: { description: '标准学科分类的可读名称列表。', example: '["Computer Science"]' },
    search_text: { description: '为全文检索拼接的搜索文本，包含院校、学院、专业和学位信息。', example: '"MIT School of Engineering Computer Science and Engineering SB 6-3"' },
    cross_school: { description: '该专业是否跨学院或跨学校组织。', example: 'false' },
    cross_school_names: { description: '跨学院记录涉及的其他学校或学院名称。', example: '[]' },
    raw_section_path: { description: '原始 Markdown 中该记录所在的章节路径，便于回溯。', example: '"SECTION 1 > School of Engineering > EECS"' },
  },
  quick_facts: {
    fact_id: { description: '一条确定性事实的稳定 ID。', example: '"fact_mit_application_fee_20260704_v2"' },
    fact_type: { description: '事实类别，例如 deadline、tuition、english_requirement 或 funding_model。', example: '"deadline"' },
    fact_key: { description: '同一事实类别下更具体的键，例如 application_deadline。', example: '"application_deadline"' },
    raw_value: { description: '从来源中原样提取的事实值，保留原始表述。', example: '"December 1 at 11:59 PM Eastern Time"' },
    normalized_value: { description: '便于程序比较和过滤的结构化事实值。', example: '{"date":"2026-12-01","timezone":"America/New_York"}' },
    unit: { description: '数值事实的单位，例如 USD、percent 或 credits。', example: 'null' },
    currency: { description: '金额事实使用的货币代码。', example: '"USD"' },
    admission_cycle: { description: '事实适用的招生周期。', example: '"2026-2027"' },
    term: { description: '事实适用的学期或入学季。', example: '"Fall"' },
    evidence_ids: { description: '支持该事实的证据片段或审计记录 ID。', example: '["E-G-008"]' },
    weknora_chunk_ids: { description: 'WeKnora 中对应的远程片段 ID，用于下游引用。', example: '[]' },
    confidence: { description: '解析器对事实抽取结果的置信度，范围为 0 到 1。', example: '0.9' },
    review_status: { description: '事实的人工或自动审核状态。', example: '"review_required"' },
    conflict_status: { description: '同一事实是否存在冲突，以及冲突是否已解决。', example: '"none"' },
  },
  source_registry: {
    source_id: { description: '官网来源的稳定主键，是来源生命周期和导入状态的入口。', example: '"src_mit_catalog_mit_edu_degree_charts_computer_science"' },
    url_type: { description: '来源的业务类型，例如 catalog、curriculum、deadline 或 funding。', example: '"degree_chart"' },
    weknora_content_hash: { description: '最近一次成功导入 WeKnora 的内容哈希。', example: '"37f23be845f9129a74e12ab46c0a7ef7"' },
    weknora_import_job_id: { description: '对应的 WeKnora 导入任务 ID。', example: '"wkj_mit_catalog_001"' },
    crawl_status: { description: '来源抓取状态。若来源来自已上传 Markdown，通常为 not_applicable。', example: '"not_applicable"' },
    parser_status: { description: '来源内容解析状态。', example: '"parsed"' },
    weknora_import_status: { description: '该来源的 WeKnora 导入状态，不影响 L1 是否发布。', example: '"success"' },
  },
  url_manifest: {
    url_id: { description: 'URL 关联清单记录的稳定主键。', example: '"url_src_mit_catalog_mit_edu_degree_charts_computer_science"' },
    url_type: { description: 'URL 主要回答的问题类型，例如 degree_chart、deadline 或 tuition_fee。', example: '"degree_chart"' },
    weknora_collection_id: { description: 'WeKnora 中的集合或知识库标识。', example: '"1b91fcff-ce72-4e97-9de0-f23a8ba419d9"' },
    weknora_knowledge_id: { description: 'WeKnora 中对应知识条目的标识。', example: '"43d1e972-cda3-480f-9df4-1bae4c9570ff"' },
    weknora_document_id: { description: 'WeKnora 中对应远程文档的标识。', example: '"43d1e972-cda3-480f-9df4-1bae4c9570ff"' },
    weknora_import_job_id: { description: '该 URL 的 WeKnora 导入任务标识。', example: '"wkj_mit_catalog_001"' },
    weknora_chunk_ids: { description: '该 URL 在 WeKnora 中生成的片段 ID 列表。', example: '[]' },
    import_status: { description: '该 URL 的显式导入状态。', example: '"success"' },
    import_error: { description: '导入失败时的详细原因，成功时为空。', example: 'null' },
  },
  entity_contexts: {
    context_id: { description: '学校或专业上下文的稳定主键。', example: '"ctx_mit_university_mit"' },
    entity_type: { description: '上下文对应的实体类型，通常是 university 或 program。', example: '"university"' },
    entity_id: { description: '当前上下文对应的实体 ID。', example: '"mit"' },
    title: { description: '上下文的正式标题。', example: '"Massachusetts Institute of Technology"' },
    display_label: { description: '面向结果页展示的简短标签。', example: '"Massachusetts Institute of Technology"' },
    attributes: { description: '实体的轻量属性，如国家和地区，不承担完整事实存储。', example: '{"country_code":"US","region":"Massachusetts"}' },
    highlights: { description: '用于概览展示的计数或亮点列表。', example: '[{"kind":"catalog_count","label":"Undergraduate programs","value":55}]' },
    sample_children: { description: '实体下属学院、院系或专业的少量示例，用于引导继续检索。', example: '[{"entity_id":"school_school_of_engineering","title":"School of Engineering"}]' },
    related_entities: { description: '与当前实体有业务关联的其他实体。', example: '[]' },
    available_topics: { description: '该实体可继续查询的主题，以及每个主题的来源范围。', example: '[{"topic":"curriculum","availability":"weknora","source_count":55}]' },
    source_ids: { description: '构建上下文时使用的来源 ID 列表。', example: '["src_mit_catalog_mit_edu_degree_charts_computer_science"]' },
    md_section_paths: { description: '来源 Markdown 中可回溯的章节路径。', example: '["SECTION 1 > School of Engineering > EECS"]' },
  },
}

const genericExamples: Record<string, string> = {
  aliases: '["Course 6-3"]',
  canonical_program_name: '"Computer Science and Engineering"',
  course_code: '"6-3"',
  degree_full_name: '"Bachelor of Science"',
  discipline_ids: '["computer_science"]',
  discipline_labels: '["Computer Science"]',
  cross_school_names: '[]',
  raw_section_path: '"SECTION 1 > School of Engineering > EECS"',
  evidence_ids: '["E-G-008"]',
  normalized_value: '{"value":"example"}',
  unit: 'null',
  currency: '"USD"',
  admission_cycle: '"2026-2027"',
  term: '"Fall"',
  confidence: '0.9',
  review_status: '"review_required"',
  conflict_status: '"none"',
  weknora_chunk_ids: '[]',
  weknora_content_hash: 'null',
  weknora_import_job_id: 'null',
  crawl_status: '"not_applicable"',
  parser_status: '"parsed"',
  weknora_import_status: '"success"',
  url_id: '"url_src_mit_catalog_001"',
  weknora_collection_id: 'null',
  weknora_knowledge_id: 'null',
  weknora_document_id: 'null',
  import_status: '"success"',
  import_error: 'null',
  context_id: '"ctx_mit_university_mit"',
  entity_type: '"university"',
  entity_id: '"mit"',
  title: '"Massachusetts Institute of Technology"',
  display_label: '"Massachusetts Institute of Technology"',
  attributes: '{"country_code":"US","region":"Massachusetts"}',
  highlights: '[{"kind":"catalog_count","label":"Undergraduate programs","value":55}]',
  sample_children: '[]',
  related_entities: '[]',
  available_topics: '[{"topic":"curriculum","availability":"weknora","source_count":55}]',
  source_ids: '["src_mit_catalog_001"]',
  md_section_paths: '["SECTION 1 > School of Engineering > EECS"]',
}

export function getFieldNote(entity: string, field: string): FieldNote {
  return fieldNotes[entity]?.[field] ?? commonFieldNotes[field] ?? {
    description: `用于记录 ${field} 的结构化值，供校验、关联或检索使用。`,
    example: genericExamples[field] ?? `"${field}_example"`,
  }
}

export const MINIMUM_EXAMPLES: Record<string, string> = {
  catalog_entries: `{
  "entry_id": "ent_mit_undergraduate_sb_18_computer_science", // 专业记录主键
  "university_id": "mit", // 院校稳定标识
  "school": "School of Engineering", // 学院
  "department": "Electrical Engineering and Computer Science", // 院系
  "level": "undergraduate", // 教育层级
  "degree_level": "SB", // 学位类型
  "program_name": "Computer Science and Engineering", // 专业名称
  "discipline_ids": ["computer_science"], // 标准学科 ID
  "discipline_labels": ["Computer Science"], // 标准学科名称
  "source_id": "src_mit_catalog_001", // 证据来源 ID
  "source_url": "https://catalog.mit.edu/degree-charts/computer-science-course-6-3", // 证据 URL
  "topics": ["catalog", "programs", "computer_science"], // 主题标签
  "search_text": "MIT Computer Science and Engineering SB 6-3", // 检索文本
  "capture_date": "2026-07-04", // 采集日期
  "dataset_version": "mit_20260704_v2", // 数据集版本
  "status": "active" // 生命周期状态
}`,
  quick_facts: `{
  "fact_id": "fact_mit_application_deadline_20260704_v2", // 事实主键
  "university_id": "mit", // 院校稳定标识
  "fact_type": "deadline", // 事实类别
  "fact_key": "application_deadline", // 事实键
  "raw_value": "December 1 at 11:59 PM Eastern Time", // 来源原文
  "source_id": "src_mit_admissions_001", // 证据来源 ID
  "source_url": "https://mitadmissions.org/apply/firstyear/deadlines-requirements/", // 证据 URL
  "capture_date": "2026-07-04", // 采集日期
  "dataset_version": "mit_20260704_v2", // 数据集版本
  "review_status": "review_required", // 审核状态
  "conflict_status": "none" // 冲突状态
}`,
  source_registry: `{
  "source_id": "src_mit_catalog_001", // 来源主键
  "university_id": "mit", // 院校稳定标识
  "canonical_url": "https://catalog.mit.edu/degree-charts/computer-science-course-6-3", // 归一化 URL
  "url_type": "degree_chart", // 来源类型
  "topics": ["catalog", "programs"], // 来源主题
  "official_source": true, // 是否官网来源
  "priority": 1, // 来源优先级
  "status": "active", // 生命周期状态
  "parser_status": "parsed", // 解析状态
  "weknora_import_status": "success", // WeKnora 导入状态
  "capture_date": "2026-07-04", // 采集日期
  "last_verified": "2026-07-04", // 最近验证日期
  "dataset_version": "mit_20260704_v2" // 数据集版本
}`,
  url_manifest: `{
  "url_id": "url_src_mit_catalog_001", // URL 关联主键
  "source_id": "src_mit_catalog_001", // 来源主键
  "university_id": "mit", // 院校稳定标识
  "entry_ids": ["ent_mit_undergraduate_sb_18_computer_science"], // 关联专业
  "source_url": "https://catalog.mit.edu/degree-charts/computer-science-course-6-3", // 原始 URL
  "canonical_url": "https://catalog.mit.edu/degree-charts/computer-science-course-6-3", // 归一化 URL
  "url_type": "degree_chart", // URL 类型
  "topics": ["catalog", "programs"], // URL 覆盖主题
  "official_source": true, // 是否官网来源
  "import_status": "success", // 导入状态
  "capture_date": "2026-07-04", // 采集日期
  "dataset_version": "mit_20260704_v2" // 数据集版本
}`,
  entity_contexts: `{
  "context_id": "ctx_mit_university_mit", // 上下文主键
  "entity_type": "university", // 实体类型
  "entity_id": "mit", // 实体 ID
  "university_id": "mit", // 院校稳定标识
  "title": "Massachusetts Institute of Technology", // 正式标题
  "display_label": "Massachusetts Institute of Technology", // 展示名称
  "attributes": {"country_code": "US", "region": "Massachusetts"}, // 轻量属性
  "highlights": [{"kind": "catalog_count", "label": "Undergraduate programs", "value": 55}], // 概览亮点
  "sample_children": [{"entity_id": "school_school_of_engineering", "title": "School of Engineering"}], // 下属示例
  "related_entities": [], // 关联实体
  "available_topics": [{"topic": "curriculum", "availability": "weknora", "source_count": 55}], // 可查主题
  "source_ids": ["src_mit_catalog_001"], // 支撑来源
  "md_section_paths": ["SECTION 1 > School of Engineering > EECS"], // 原文路径
  "dataset_version": "mit_20260704_v2", // 数据集版本
  "status": "active" // 生命周期状态
}`,
}

export type RetrievalFlowStep = {
  label: string
  title: string
  detail: string
}

export const RETRIEVAL_FLOW: RetrievalFlowStep[] = [
  { label: '问题进入', title: 'MIT 里有哪些计算机相关的学科', detail: '识别院校实体 MIT，提取主题 Computer Science，并判断用户要的是专业目录而不是截止日期或学费。' },
  { label: '实体定位', title: 'entity_contexts', detail: '确认 mit 对应的学校上下文、可用主题和下属学院，给后续检索提供边界。' },
  { label: '专业检索', title: 'catalog_entries', detail: '按 university_id=mit 和 discipline_ids / discipline_labels 过滤，返回 Computer Science、Mathematics with Computer Science 等专业记录。' },
  { label: '来源绑定', title: 'source_registry + url_manifest', detail: '把专业记录绑定到官方来源，确定哪些 URL 能支撑答案，并保留精确证据入口。' },
  { label: '事实补充', title: 'quick_facts', detail: '本问题不需要事实表；如果继续问申请截止日期、学费或语言要求，才沿同一院校边界查询 quick_facts。' },
  { label: '回答生成', title: '专业清单 + 证据', detail: '合并去重后的专业名称、学院和学位层级，附官方来源，不把 unrelated 的事实混入答案。' },
]

export const RETRIEVAL_ROLES = [
  { entity: 'entity_contexts', role: '先定位院校和可查主题', questions: '这是谁？有哪些学院？还能继续问课程、截止日期还是资助？' },
  { entity: 'catalog_entries', role: '回答专业、学科和学位目录', questions: '有哪些计算机相关专业？属于哪个学院？是本科还是研究生？' },
  { entity: 'source_registry', role: '确认来源权威性和生命周期', questions: '这条答案来自哪个官方页面？来源是否解析成功、是否仍有效？' },
  { entity: 'url_manifest', role: '做 URL 到专业和主题的精准映射', questions: '哪个 URL 支撑这个专业？一个来源覆盖哪些专业或主题？' },
  { entity: 'quick_facts', role: '回答明确的数值和规则事实', questions: '截止日期、学费、申请费、语言要求和资助政策是什么？' },
]
