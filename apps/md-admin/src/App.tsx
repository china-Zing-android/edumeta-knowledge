import { type ReactNode, useCallback, useEffect, useRef, useState } from 'react'
import {
  Activity,
  ArrowRight,
  ArrowUp,
  Copy,
  Book,
  CheckmarkFilled,
  CloudUpload,
  Document,
  Download,
  ErrorFilled,
  FolderOpen,
  Renew,
  Search,
  Settings,
  Time,
  Undo,
} from '@carbon/icons-react'
import {
  Button,
  Dropdown,
  InlineNotification,
  Modal,
  Tag,
  Tabs,
  Tab,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
  TabList,
  TabPanel,
  TabPanels,
  TextInput,
} from '@carbon/react'
import '@carbon/styles/css/styles.css'
import {
  AdminStatus,
  apiFetch,
  Artifact,
  artifactDownloadUrl,
  Batch,
  IngestionRun,
  ProvenanceField,
  ProvenancePayload,
  Preview,
  PreviewItem,
  SourceFile,
  UniversityVersion,
} from './api'
import { getFieldNote, MINIMUM_EXAMPLES, RETRIEVAL_DECISIONS, RETRIEVAL_FLOW, RETRIEVAL_ROLES, SCHEMA_OVERVIEW } from './schemaDocs'
import './styles.css'

type Page = 'workspace' | 'files' | 'batches' | 'versions' | 'docs' | 'settings'
type ArtifactPageItem = { line: number; record?: Record<string, unknown>; text?: string; error?: string }
type ArtifactPage = { artifact: string; offset: number; limit: number; total: number; items: ArtifactPageItem[] }
type Guide = { entity: string; label: string; purpose: string; why: string; role?: string; query_rule?: string; minimum: string[]; links: string[]; schema: { required?: string[]; properties?: Record<string, { type?: string | string[]; enum?: string[] }> } }

const NAV_ITEMS: Array<{ id: Page; label: string; icon: typeof Activity }> = [
  { id: 'workspace', label: '更新院校', icon: CloudUpload },
  { id: 'files', label: '已上传文件', icon: Document },
  { id: 'batches', label: '运行批次', icon: Activity },
  { id: 'versions', label: '版本历史', icon: Time },
  { id: 'docs', label: 'JSONL 结构说明', icon: Book },
  { id: 'settings', label: '系统配置状态', icon: Settings },
]

function formatBytes(value?: number | null): string {
  if (!value) return '0 B'
  if (value < 1024) return `${value} B`
  if (value < 1024 * 1024) return `${(value / 1024).toFixed(1)} KB`
  return `${(value / 1024 / 1024).toFixed(1)} MB`
}

function formatTime(value?: string | null): string {
  if (!value) return '-'
  return new Intl.DateTimeFormat('zh-CN', { month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }).format(new Date(value))
}

const COUNTRY_NAMES: Record<string, string> = {
  AU: '澳大利亚',
  CA: '加拿大',
  CH: '瑞士',
  IE: '爱尔兰',
  NZ: '新西兰',
  SG: '新加坡',
  UK: '英国',
  US: '美国',
}

type GeographicRecord = { country_code?: string | null; region?: string | null }

function regionLabel(item: GeographicRecord): string {
  const countryCode = item.country_code?.trim().toUpperCase() ?? ''
  const country = countryCode ? `${COUNTRY_NAMES[countryCode] ?? countryCode} · ${countryCode}` : ''
  const rawRegion = item.region?.trim() ?? ''
  const region = rawRegion && rawRegion.toUpperCase() !== countryCode ? rawRegion : ''
  if (country && region) return `${country} · ${region}`
  if (country) return `${country} · 未细分地区`
  if (region) return region
  return '未分区'
}

function regionKey(item: GeographicRecord): string {
  const countryCode = item.country_code?.trim().toUpperCase() ?? ''
  const rawRegion = item.region?.trim() ?? ''
  const region = rawRegion && rawRegion.toUpperCase() !== countryCode ? rawRegion : ''
  return `${countryCode}::${region}`
}

function groupByRegion<T extends GeographicRecord>(items: T[]): Array<{ key: string; label: string; items: T[] }> {
  const groups = new Map<string, { key: string; label: string; items: T[] }>()
  items.forEach((item) => {
    const key = regionKey(item)
    const group = groups.get(key) ?? { key, label: regionLabel(item), items: [] }
    group.items.push(item)
    groups.set(key, group)
  })
  return Array.from(groups.values()).sort((left, right) => {
    if (left.key === '::') return 1
    if (right.key === '::') return -1
    return left.label.localeCompare(right.label, 'zh-CN')
  })
}

function regionFilterItems<T extends GeographicRecord>(items: T[]): string[] {
  return ['全部', ...Array.from(new Set(items.map(regionLabel))).sort((left, right) => left.localeCompare(right, 'zh-CN'))]
}

function statusLabel(status: string): string {
  const labels: Record<string, string> = {
    accepted: '排队中',
    parsing: '解析中',
    weknora_preparing: '准备 WeKnora',
    validating: '质量校验',
    publishing: '发布中',
    published: 'L1 已发布',
    failed: '失败',
    unchanged: '内容未变化',
  }
  return labels[status] ?? status
}

function statusKind(status: string): 'green' | 'red' | 'blue' | 'gray' | 'warm-gray' | 'purple' {
  if (status === 'published' || status === 'unchanged') return 'green'
  if (status === 'failed') return 'red'
  if (status === 'accepted') return 'gray'
  return 'blue'
}

function sourceStatusLabel(status: string): string {
  if (status === 'not_submitted') return '未提交'
  if (status === 'superseded') return '已替换'
  return statusLabel(status)
}

function sourceStatusKind(status: string): 'green' | 'red' | 'blue' | 'gray' {
  if (status === 'not_submitted') return 'gray'
  if (status === 'superseded') return 'gray'
  return statusKind(status) === 'green' ? 'green' : status === 'failed' ? 'red' : 'blue'
}

function provenanceStatusLabel(status?: string): string {
  return ({
    verified: '已核验',
    review_required: '需要复核',
    unavailable: '没有来源映射',
  }[status ?? 'unavailable'] ?? status ?? '没有来源映射')
}

function provenanceStatusKind(status?: string): 'green' | 'red' | 'gray' {
  if (status === 'verified') return 'green'
  if (status === 'review_required') return 'red'
  return 'gray'
}

function provenanceFieldKindLabel(kind?: string): string {
  return ({ direct: '直接来自 Markdown', derived: '按固定规则推导', system: '系统运行信息' }[kind ?? ''] ?? kind ?? '未说明')
}

function provenanceFieldKindClass(kind?: string): string {
  return kind === 'direct' ? 'is-direct' : kind === 'derived' ? 'is-derived' : 'is-system'
}

function jsonlRecordId(artifact: string, record?: Record<string, unknown>): string | null {
  if (!record || !['catalog_entries', 'quick_facts'].includes(artifact)) return null
  const key = artifact === 'catalog_entries' ? 'entry_id' : 'fact_id'
  const value = record[key]
  return typeof value === 'string' && value ? value : null
}

function displayValue(value: unknown): string {
  if (typeof value === 'string') return value
  if (value === undefined || value === null) return '-'
  return JSON.stringify(value) ?? String(value)
}

function failureStage(run: IngestionRun): string | null {
  const failure = run.stage_failures?.[0]
  if (!failure) return null
  const stage = failure.stage ?? failure.phase
  return typeof stage === 'string' ? stage : null
}

function runStatusDetail(run: IngestionRun): string | null {
  if (run.error_message) return run.error_message
  const stage = failureStage(run)
  return stage ? `失败阶段：${stage}` : null
}

function WeKnoraState({ run }: { run: IngestionRun }) {
  if (run.weknora?.summary === 'disabled') return <Tag type="gray">WeKnora 未启用</Tag>
  if (run.weknora?.summary === 'partial_failure') return <span><Tag type="red">L1 已发布，WeKnora 部分失败</Tag>{run.weknora_error && <span className="subcell">{run.weknora_error}</span>}</span>
  if (run.weknora?.summary === 'pending_or_success') return <Tag type="blue">WeKnora 导入处理中</Tag>
  return <Tag type="cool-gray">未开始</Tag>
}

function EmptyState({ title, body }: { title: string; body: string }) {
  return <div className="empty-state"><Document size={28} /><h3>{title}</h3><p>{body}</p></div>
}

function BackToTopButton() {
  const sentinelRef = useRef<HTMLDivElement>(null)
  const [showButton, setShowButton] = useState(false)

  useEffect(() => {
    const sentinel = sentinelRef.current
    if (!sentinel) return

    let sentinelVisible = true
    const updateVisibility = () => {
      const hasScroll = document.documentElement.scrollHeight > window.innerHeight + 8
      setShowButton(hasScroll && !sentinelVisible)
    }
    const intersectionObserver = new IntersectionObserver(([entry]) => {
      sentinelVisible = entry.isIntersecting
      updateVisibility()
    }, { threshold: 0 })
    intersectionObserver.observe(sentinel)

    const resizeObserver = typeof ResizeObserver === 'undefined' ? null : new ResizeObserver(updateVisibility)
    resizeObserver?.observe(document.documentElement)
    resizeObserver?.observe(document.body)
    window.addEventListener('resize', updateVisibility)
    updateVisibility()

    return () => {
      intersectionObserver.disconnect()
      resizeObserver?.disconnect()
      window.removeEventListener('resize', updateVisibility)
    }
  }, [])

  return <>
    <div ref={sentinelRef} className="scroll-top-sentinel" aria-hidden="true" />
    {showButton && <Button className="back-to-top" kind="primary" size="sm" hasIconOnly renderIcon={ArrowUp} iconDescription="返回顶部" onClick={() => { const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches; window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }) }} />}
  </>
}

function App() {
  const [page, setPage] = useState<Page>('workspace')
  const [status, setStatus] = useState<AdminStatus | null>(null)
  const [batches, setBatches] = useState<Batch[]>([])
  const [runs, setRuns] = useState<IngestionRun[]>([])
  const [selectedBatch, setSelectedBatch] = useState<string | null>(null)
  const [selectedRun, setSelectedRun] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [refreshing, setRefreshing] = useState(false)
  const [directorySeed, setDirectorySeed] = useState<{ rootId: string; relativePath: string } | null>(null)

  const loadOverview = useCallback(async () => {
    setRefreshing(true)
    try {
      const [config, batchPayload, runPayload] = await Promise.all([
        apiFetch<AdminStatus>('/v1/admin/config/status'),
        apiFetch<{ items: Batch[] }>('/v1/admin/ingestion-batches?limit=30'),
        apiFetch<{ items: IngestionRun[] }>('/v1/admin/ingestion-runs?limit=500'),
      ])
      setStatus(config)
      setBatches(batchPayload.items)
      setRuns(runPayload.items.filter(Boolean))
      setError(null)
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : '无法读取管理端状态')
    } finally {
      setRefreshing(false)
    }
  }, [])

  useEffect(() => { void loadOverview() }, [loadOverview])
  useEffect(() => {
    const timer = window.setInterval(() => { void loadOverview() }, 5000)
    return () => window.clearInterval(timer)
  }, [loadOverview])

  const currentRun = runs.find((run) => run.run_id === selectedRun) ?? null
  const openSourceDirectory = (sourceFile: SourceFile) => {
    const separator = sourceFile.relative_path.lastIndexOf('/')
    setDirectorySeed({
      rootId: sourceFile.source_root_id,
      relativePath: separator === -1 ? '' : sourceFile.relative_path.slice(0, separator),
    })
    setPage('workspace')
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand-lockup">
          <span className="brand-mark">E</span>
          <span><strong>Edumeta</strong><small>Markdown Control</small></span>
        </div>
        <div className="topbar-status">
          <span className={`system-led ${status?.import_mode === 'enabled' ? 'is-live' : ''}`} />
          <span>{status?.import_mode === 'enabled' ? 'WeKnora 已连接' : status?.import_mode === 'disabled' ? 'WeKnora 未启用' : '检查配置中'}</span>
          <Button kind="ghost" size="sm" hasIconOnly renderIcon={Renew} iconDescription="刷新" onClick={() => void loadOverview()} className={refreshing ? 'is-spinning' : ''} />
        </div>
      </header>
      <div className="app-body">
        <aside className="side-rail">
          <div className="rail-label">CONTENT OPERATIONS</div>
          <nav aria-label="主导航">
            {NAV_ITEMS.map(({ id, label, icon: Icon }) => (
              <button key={id} className={`nav-item ${page === id ? 'is-active' : ''}`} onClick={() => setPage(id)} aria-current={page === id ? 'page' : undefined}>
                <Icon size={18} /><span>{label}</span>{page === id && <ArrowRight size={16} />}
              </button>
            ))}
          </nav>
          <div className="rail-footnote">
            <span className="rail-label">运行约束</span>
            <p>单文件 ≤ 20 MiB</p>
            <p>普通上传 ≤ 20 个文件</p>
            <p>目录模式进入持久化队列</p>
          </div>
        </aside>
        <main className="main-canvas">
          <BackToTopButton />
          {error && <InlineNotification kind="error" lowContrast title="管理端接口不可用" subtitle={error} onCloseButtonClick={() => setError(null)} />}
          <div className="page-heading">
            <div>
              <p className="eyebrow">MARKDOWN INGESTION</p>
              <h1>{NAV_ITEMS.find((item) => item.id === page)?.label}</h1>
              <p className="heading-copy">把 Markdown 作为唯一源文件，观察每次解析、校验、发布和下游导入。</p>
            </div>
          </div>
          {page === 'workspace' && <Workspace initialDirectory={directorySeed} onBatchCreated={loadOverview} onRunSelected={setSelectedRun} onOpenFiles={() => setPage('files')} />}
          {page === 'files' && <FilesPage runs={runs} onRunSelected={setSelectedRun} onRefresh={loadOverview} onOpenSourceDirectory={openSourceDirectory} />}
          {page === 'batches' && <BatchPage batches={batches} selectedBatch={selectedBatch} onSelectBatch={setSelectedBatch} onRunSelected={setSelectedRun} />}
          {page === 'versions' && <VersionPage onRunSelected={setSelectedRun} />}
          {page === 'docs' && <DocsPage />}
          {page === 'settings' && <SettingsPage status={status} />}
          {currentRun && <RunInspector run={currentRun} onClose={() => setSelectedRun(null)} onChanged={loadOverview} />}
        </main>
      </div>
    </div>
  )
}

function Workspace({ initialDirectory, onBatchCreated, onRunSelected, onOpenFiles }: { initialDirectory: { rootId: string; relativePath: string } | null; onBatchCreated: () => Promise<void>; onRunSelected: (id: string) => void; onOpenFiles: () => void }) {
  const [mode, setMode] = useState<'upload' | 'directory'>('upload')
  const [files, setFiles] = useState<File[]>([])
  const [rootId, setRootId] = useState('')
  const [relativePath, setRelativePath] = useState('')
  const [roots, setRoots] = useState<Array<{ root_id: string; label: string; exists: boolean }>>([])
  const [preview, setPreview] = useState<Preview | null>(null)
  const [working, setWorking] = useState(false)
  const [message, setMessage] = useState<string | null>(null)
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => { void apiFetch<{ items: typeof roots }>('/v1/admin/source-roots').then((payload) => { setRoots(payload.items); if (payload.items[0]) setRootId(payload.items[0].root_id) }).catch(() => undefined) }, [])
  useEffect(() => {
    if (!initialDirectory) return
    setMode('directory')
    setRootId(initialDirectory.rootId)
    setRelativePath(initialDirectory.relativePath)
    setPreview(null)
    setMessage(`已定位到 ${initialDirectory.relativePath || '根目录'}，可以生成预览`)
  }, [initialDirectory])

  const updatePreviewItem = (itemId: string, patch: Partial<PreviewItem>) => {
    setPreview((current) => {
      if (!current) return current
      const items = current.items.map((item) => {
        if (item.item_id !== itemId) return item
        const next = { ...item, ...patch }
        const remainingIssues = item.issues.filter((issue) => !['unmapped_university', 'duplicate_university_id'].includes(issue.code))
        const validId = /^[a-z0-9][a-z0-9_-]{0,127}$/.test(next.university_id)
        next.issues = validId ? remainingIssues : [...remainingIssues, { code: 'unmapped_university', message: '请输入合法的 university_id' }]
        next.ready = next.issues.length === 0
        return next
      })
      const groups = new Map<string, PreviewItem[]>()
      items.forEach((item) => { if (item.university_id) groups.set(item.university_id, [...(groups.get(item.university_id) ?? []), item]) })
      groups.forEach((group) => {
        if (group.length < 2) return
        group.forEach((item) => {
          if (!item.issues.some((issue) => issue.code === 'duplicate_university_id')) item.issues.push({ code: 'duplicate_university_id', message: '同一批次重复映射，提交会产生版本覆盖风险' })
          item.ready = false
        })
      })
      return { ...current, items, ready_count: items.filter((item) => item.ready).length, blocked_count: items.filter((item) => !item.ready).length }
    })
  }

  const createPreview = async () => {
    setWorking(true)
    setMessage(null)
    try {
      const form = new FormData()
      form.set('mode', mode)
      if (mode === 'directory') {
        form.set('source_root_id', rootId)
        form.set('source_relative_path', relativePath)
      } else {
        files.forEach((file) => form.append('files', file))
      }
      setPreview(await apiFetch<Preview>('/v1/admin/ingestion-previews', { method: 'POST', body: form }))
    } catch (caught) {
      setMessage(caught instanceof Error ? caught.message : '无法创建预览')
    } finally { setWorking(false) }
  }

  const commit = async () => {
    if (!preview) return
    const ready = preview.items.filter((item) => item.ready)
    if (!ready.length) { setMessage('当前没有可以提交的文件'); return }
    setWorking(true)
    try {
      const result = await apiFetch<{ batch_id: string; accepted_count: number; rejected_count: number }>('/v1/admin/ingestion-batches', {
        method: 'POST',
        body: JSON.stringify({ preview_id: preview.preview_id, items: ready.map((item) => ({
          item_id: item.item_id,
          university_id: item.university_id,
          university_name: item.university_name,
          country_code: item.country_code,
          region: item.region,
          school_tier: item.school_tier,
          aliases: item.aliases,
        })) }),
      })
      setPreview(null)
      setFiles([])
      setMessage(result.rejected_count ? `批次 ${result.batch_id} 已提交 ${result.accepted_count} 个文件，另有 ${result.rejected_count} 个文件被单项拒绝` : `批次 ${result.batch_id} 已进入队列`)
      await onBatchCreated()
    } catch (caught) {
      setMessage(caught instanceof Error ? caught.message : '批次提交失败')
    } finally { setWorking(false) }
  }

  return <>
    <section className="workbench-section upload-section">
      <div className="section-intro">
        <div><p className="eyebrow">SOURCE INPUT</p><h2>选择要更新的 Markdown</h2><p>普通上传适合小批量校验，服务器目录适合完整数据集更新。两种方式都会先生成预览。</p></div>
        <div className="constraint-line"><span>仅支持 .md</span><span>单文件 20 MiB</span><span>目录递归扫描</span></div>
      </div>
      <Tabs selectedIndex={mode === 'upload' ? 0 : 1} onChange={({ selectedIndex }) => setMode(selectedIndex === 0 ? 'upload' : 'directory')}>
        <TabList aria-label="Markdown 来源模式">
          <Tab renderIcon={CloudUpload}>文件上传</Tab>
          <Tab renderIcon={FolderOpen}>服务器目录</Tab>
        </TabList>
      </Tabs>
      {mode === 'upload' ? <div className="source-form">
        <div className="drop-row" onClick={() => inputRef.current?.click()} role="button" tabIndex={0} onKeyDown={(event) => { if (event.key === 'Enter') inputRef.current?.click() }}>
          <CloudUpload size={28} /><div><strong>选择 Markdown 文件</strong><span>{files.length ? `已选择 ${files.length} 个文件` : '支持单个或批量选择，最多 20 个'}</span></div><Button kind="tertiary" size="sm" onClick={(event) => { event.stopPropagation(); inputRef.current?.click() }}>浏览文件</Button>
          <input ref={inputRef} hidden type="file" accept=".md,text/markdown" multiple onChange={(event) => setFiles(Array.from(event.target.files ?? []))} />
        </div>
      </div> : <div className="source-form directory-form">
        <Dropdown id="source-root" titleText="允许的服务器目录" label="选择目录根" items={roots} itemToString={(item) => item ? `${item.label}${item.exists ? '' : '（不存在）'}` : ''} selectedItem={roots.find((root) => root.root_id === rootId)} onChange={({ selectedItem }) => setRootId(selectedItem?.root_id ?? '')} />
        <TextInput id="relative-path" labelText="子目录路径" placeholder="留空扫描整个根目录，例如 us/" value={relativePath} onChange={(event) => setRelativePath(event.target.value)} helperText="只允许相对于配置根目录的路径，不接受绝对路径。" />
      </div>}
      <div className="section-actions"><Button kind="primary" renderIcon={ArrowRight} disabled={working || (mode === 'upload' ? files.length === 0 : !rootId)} onClick={() => void createPreview()}>{working ? '扫描中...' : '生成预览'}</Button>{message && <span className="action-message">{message}</span>}</div>
    </section>
    {preview && <PreviewSection preview={preview} working={working} onUpdate={updatePreviewItem} onCommit={() => void commit()} onDiscard={() => setPreview(null)} />}
    <section className="workbench-section recent-section"><div className="section-title-row"><div><p className="eyebrow">UPLOADED FILES</p><h2>最近上传的文件</h2><p>每行都可以打开文件详情，查看处理阶段、L1 / WeKnora 状态和在线产物。</p></div><button className="text-action" onClick={onOpenFiles}>查看已上传文件 <ArrowRight size={16} /></button></div><RecentRuns onRunSelected={onRunSelected} /></section>
  </>
}

function PreviewSection({ preview, working, onUpdate, onCommit, onDiscard }: { preview: Preview; working: boolean; onUpdate: (itemId: string, patch: Partial<PreviewItem>) => void; onCommit: () => void; onDiscard: () => void }) {
  const [query, setQuery] = useState('')
  const items = preview.items.filter((item) => item.filename.toLowerCase().includes(query.toLowerCase()) || item.university_id.includes(query.toLowerCase()))
  return <section className="workbench-section preview-section">
    <div className="section-title-row"><div><p className="eyebrow">PREVIEW</p><h2>提交前检查</h2><p>{preview.ready_count} 个可提交，{preview.blocked_count} 个需要处理。异常项不会阻止其他正常文件。</p></div><div className="preview-actions"><Button kind="ghost" onClick={onDiscard}>放弃预览</Button><Button kind="primary" disabled={working || preview.ready_count === 0} onClick={onCommit}>提交 {preview.ready_count} 个文件</Button></div></div>
    <div className="filter-line"><TextInput id="preview-filter" size="sm" labelText="" hideLabel placeholder="按文件名或院校筛选" decorator={<Search size={16} />} value={query} onChange={(event) => setQuery(event.target.value)} /><span className="mono">SHA-256 已计算</span></div>
    <div className="table-scroll"><Table size="lg" useZebraStyles={false}><TableHead><TableRow><TableHeader>文件</TableHeader><TableHeader>院校映射</TableHeader><TableHeader>操作</TableHeader><TableHeader>大小</TableHeader><TableHeader>检查结果</TableHeader></TableRow></TableHead><TableBody>{items.map((item) => <TableRow key={item.item_id}><TableCell><div className="file-cell"><Document size={18} /><div><strong>{item.filename}</strong><span>{item.relative_path}</span></div></div></TableCell><TableCell><div className="mapping-fields"><TextInput id={`${item.item_id}-id`} size="sm" labelText="院校 ID" hideLabel value={item.university_id} onChange={(event) => onUpdate(item.item_id, { university_id: event.target.value.toLowerCase() })} /><TextInput id={`${item.item_id}-name`} size="sm" labelText="名称" hideLabel value={item.university_name} onChange={(event) => onUpdate(item.item_id, { university_name: event.target.value })} /><TextInput id={`${item.item_id}-country`} size="sm" labelText="国家" hideLabel placeholder="国家" value={item.country_code ?? ''} onChange={(event) => onUpdate(item.item_id, { country_code: event.target.value.toUpperCase() })} /><TextInput id={`${item.item_id}-region`} size="sm" labelText="地区" hideLabel placeholder="地区" value={item.region ?? ''} onChange={(event) => onUpdate(item.item_id, { region: event.target.value })} /><Dropdown id={`${item.item_id}-tier`} size="sm" titleText="层级" label="层级" items={['core', 'non_core']} selectedItem={item.school_tier} itemToString={(value) => value === 'core' ? '核心院校' : '非核心院校'} onChange={({ selectedItem }) => onUpdate(item.item_id, { school_tier: selectedItem === 'non_core' ? 'non_core' : 'core' })} /><TextInput id={`${item.item_id}-aliases`} size="sm" labelText="别名" hideLabel placeholder="别名，用逗号分隔" value={(item.aliases ?? []).join(', ')} onChange={(event) => onUpdate(item.item_id, { aliases: event.target.value.split(',').map((alias) => alias.trim()).filter(Boolean) })} /></div></TableCell><TableCell><Tag type="cool-gray">{item.operation === 'update' ? '更新' : '新增'}</Tag></TableCell><TableCell><span className="mono">{formatBytes(item.size_bytes)}</span></TableCell><TableCell>{item.ready ? <Tag type="green" renderIcon={CheckmarkFilled}>可提交</Tag> : <div className="issue-cell"><Tag type="red" renderIcon={ErrorFilled}>需处理</Tag><span>{item.issues[0]?.message}</span></div>}</TableCell></TableRow>)}</TableBody></Table></div>
  </section>
}

function RecentRuns({ onRunSelected }: { onRunSelected: (id: string) => void }) {
  const [runs, setRuns] = useState<IngestionRun[]>([])
  useEffect(() => { const load = () => void apiFetch<{ items: IngestionRun[] }>('/v1/admin/ingestion-runs?limit=12').then((payload) => setRuns(payload.items.filter(Boolean))).catch(() => undefined); load(); const handler = () => load(); window.addEventListener('refresh-runs', handler); return () => window.removeEventListener('refresh-runs', handler) }, [])
  if (!runs.length) return <EmptyState title="还没有运行记录" body="先从上方上传 Markdown 或扫描一个服务器目录。" />
  return <RunTable runs={runs} onRunSelected={onRunSelected} />
}

function FilesPage({ runs, onRunSelected, onRefresh, onOpenSourceDirectory }: { runs: IngestionRun[]; onRunSelected: (id: string) => void; onRefresh: () => Promise<void>; onOpenSourceDirectory: (sourceFile: SourceFile) => void }) {
  const [query, setQuery] = useState('')
  const [filter, setFilter] = useState('全部')
  const [regionFilter, setRegionFilter] = useState('全部')
  const [sourceFiles, setSourceFiles] = useState<SourceFile[]>([])
  const [sourceQuery, setSourceQuery] = useState('')
  const [sourceFilter, setSourceFilter] = useState('全部')
  const [sourceRegionFilter, setSourceRegionFilter] = useState('全部')
  const [sourceLoading, setSourceLoading] = useState(false)
  const [sourceError, setSourceError] = useState<string | null>(null)
  const filterItems = ['全部', '排队中', '解析中', '质量校验', '发布中', 'L1 已发布', '失败']
  const sourceFilterItems = ['全部', '未提交', '排队中', '解析中', '质量校验', '发布中', 'L1 已发布', '已替换', '失败', '内容未变化']
  const loadSourceFiles = useCallback(async () => {
    setSourceLoading(true)
    try {
      const payload = await apiFetch<{ items: SourceFile[] }>('/v1/admin/source-files?limit=500')
      setSourceFiles(payload.items)
      setSourceError(null)
    } catch (caught) {
      setSourceFiles([])
      setSourceError(caught instanceof Error ? caught.message : '无法读取服务器源文件')
    } finally {
      setSourceLoading(false)
    }
  }, [])
  useEffect(() => { void loadSourceFiles() }, [loadSourceFiles])
  const sourceRegionItems = regionFilterItems(sourceFiles)
  const runRegionItems = regionFilterItems(runs)
  const filtered = runs.filter((run) => {
    const haystack = `${run.source_filename ?? ''} ${run.university_id} ${run.university_name ?? ''} ${run.run_id} ${regionLabel(run)}`.toLowerCase()
    const matchesQuery = !query.trim() || haystack.includes(query.trim().toLowerCase())
    const matchesFilter = filter === '全部' || statusLabel(run.status) === filter
    const matchesRegion = regionFilter === '全部' || regionLabel(run) === regionFilter
    return matchesQuery && matchesFilter && matchesRegion
  })
  const filteredSourceFiles = sourceFiles.filter((file) => {
    const haystack = `${file.filename} ${file.relative_path} ${file.university_id} ${file.university_name} ${regionLabel(file)}`.toLowerCase()
    const matchesQuery = !sourceQuery.trim() || haystack.includes(sourceQuery.trim().toLowerCase())
    const matchesFilter = sourceFilter === '全部' || sourceStatusLabel(file.source_status) === sourceFilter
    const matchesRegion = sourceRegionFilter === '全部' || regionLabel(file) === sourceRegionFilter
    return matchesQuery && matchesFilter && matchesRegion
  })
  const sourceGroups = groupByRegion(filteredSourceFiles)
  const runGroups = groupByRegion(filtered)
  const refresh = async () => {
    await Promise.all([onRefresh(), loadSourceFiles()])
  }

  return <div className="files-page">
    <section className="workbench-section source-files-section">
      <div className="section-title-row">
        <div><p className="eyebrow">SERVER SOURCE</p><h2>服务器源文件</h2><p>这里读取配置的宿主机 Markdown 目录。文件已经存在，不代表它已经提交、解析或发布，所以未提交文件也会显示。</p></div>
        <Button kind="ghost" renderIcon={Renew} disabled={sourceLoading} onClick={() => void refresh()}>刷新列表</Button>
      </div>
      {sourceError && <InlineNotification kind="error" lowContrast title="服务器源文件读取失败" subtitle={sourceError} onCloseButtonClick={() => setSourceError(null)} />}
      <div className="files-toolbar">
        <TextInput id="source-files-query" size="sm" labelText="搜索源文件" placeholder="按文件名、路径或院校搜索" value={sourceQuery} onChange={(event) => setSourceQuery(event.target.value)} decorator={<Search size={16} />} />
        <Dropdown id="source-files-status" size="sm" titleText="源文件状态" label="全部" items={sourceFilterItems} selectedItem={sourceFilter} onChange={({ selectedItem }) => setSourceFilter(selectedItem ?? '全部')} />
        <Dropdown id="source-files-region" size="sm" titleText="地区" label="全部" items={sourceRegionItems} selectedItem={sourceRegionFilter} onChange={({ selectedItem }) => setSourceRegionFilter(selectedItem ?? '全部')} />
        <span className="mono files-count">显示 {filteredSourceFiles.length} / {sourceFiles.length}</span>
      </div>
      {sourceGroups.length ? sourceGroups.map((group) => <RegionSection key={group.key} label={group.label} count={group.items.length} noun="文件"><SourceFileTable files={group.items} onRunSelected={onRunSelected} onOpenSourceDirectory={onOpenSourceDirectory} /></RegionSection>) : <EmptyState title={sourceLoading ? '正在读取服务器目录' : '没有可见的服务器源文件'} body={sourceFiles.length ? '换一个文件名、路径、地区或状态筛选条件。' : '请确认 Markdown 位于配置的服务器源目录，或者先刷新列表。'} />}
    </section>
    <section className="workbench-section submitted-files-section">
      <div className="section-title-row">
        <div><p className="eyebrow">INGESTION RUNS</p><h2>已提交运行记录</h2><p>只有提交过预览并进入队列的文件才会有 run。在线查看会打开 raw、JSONL、差异和质量审计。</p></div>
      </div>
      <div className="files-toolbar">
        <TextInput id="files-query" size="sm" labelText="搜索运行记录" placeholder="按文件名、院校或运行 ID 搜索" value={query} onChange={(event) => setQuery(event.target.value)} decorator={<Search size={16} />} />
        <Dropdown id="files-status" size="sm" titleText="运行状态" label="全部" items={filterItems} selectedItem={filter} onChange={({ selectedItem }) => setFilter(selectedItem ?? '全部')} />
        <Dropdown id="files-region" size="sm" titleText="地区" label="全部" items={runRegionItems} selectedItem={regionFilter} onChange={({ selectedItem }) => setRegionFilter(selectedItem ?? '全部')} />
        <span className="mono files-count">显示 {filtered.length} / {runs.length}</span>
      </div>
      {runGroups.length ? runGroups.map((group) => <RegionSection key={group.key} label={group.label} count={group.items.length} noun="运行记录"><RunTable runs={group.items} onRunSelected={onRunSelected} /></RegionSection>) : <EmptyState title="没有匹配的运行记录" body={runs.length ? '换一个文件名、院校、地区或状态筛选条件。' : '服务器源文件需要先生成预览并提交，才会产生运行记录。'} />}
    </section>
  </div>
}

function RegionSection({ label, count, noun, children }: { label: string; count: number; noun: string; children: ReactNode }) {
  return <section className="region-group"><div className="region-group-heading"><div><span className="region-kicker">REGION</span><h3>{label}</h3></div><span className="mono">{count} 个{noun}</span></div>{children}</section>
}

function SourceFileTable({ files, onRunSelected, onOpenSourceDirectory }: { files: SourceFile[]; onRunSelected: (id: string) => void; onOpenSourceDirectory: (sourceFile: SourceFile) => void }) {
  return <div className="table-scroll"><Table size="lg"><TableHead><TableRow><TableHeader>源文件</TableHeader><TableHeader>院校映射</TableHeader><TableHeader>地区</TableHeader><TableHeader>源文件状态</TableHeader><TableHeader>最近运行</TableHeader><TableHeader>修改时间</TableHeader><TableHeader>操作</TableHeader></TableRow></TableHead><TableBody>{files.map((file) => <TableRow key={`${file.source_root_id}:${file.relative_path}`} onClick={() => file.run_id && onRunSelected(file.run_id)} className={file.run_id ? 'clickable-row' : undefined}><TableCell><div className="file-cell"><Document size={18} /><div><strong>{file.filename}</strong><span>{file.relative_path}</span><span className="mono">{formatBytes(file.size_bytes)}</span></div></div></TableCell><TableCell><strong>{file.university_name || file.university_id}</strong><span className="subcell mono">{file.university_id}</span>{file.issues[0] && <span className="run-error">{file.issues[0].message}</span>}</TableCell><TableCell><span className="region-cell">{file.region || file.country_code || '未分区'}</span><span className="subcell mono">{file.country_code || '-'}</span></TableCell><TableCell><Tag type={sourceStatusKind(file.source_status)}>{sourceStatusLabel(file.source_status)}</Tag>{file.is_current && <span className="subcell">当前版本</span>}</TableCell><TableCell>{file.run_id ? <><strong className="mono">{file.run_id}</strong><span className="subcell">{file.run_updated_at ? formatTime(file.run_updated_at) : '-'}</span></> : file.version_id ? <><strong className="mono">{file.version_id}</strong><span className="subcell">版本目录已关联，尚无运行记录</span></> : <span className="subcell">尚未提交</span>}</TableCell><TableCell className="mono">{formatTime(file.modified_at)}</TableCell><TableCell>{file.run_id ? <Button kind="ghost" size="sm" renderIcon={ArrowRight} onClick={(event) => { event.stopPropagation(); onRunSelected(file.run_id as string) }}>在线查看</Button> : <Button kind="tertiary" size="sm" renderIcon={FolderOpen} onClick={(event) => { event.stopPropagation(); onOpenSourceDirectory(file) }}>扫描所在目录</Button>}</TableCell></TableRow>)}</TableBody></Table></div>
}

function RunTable({ runs, onRunSelected }: { runs: IngestionRun[]; onRunSelected: (id: string) => void }) {
  return <div className="table-scroll"><Table size="lg"><TableHead><TableRow><TableHeader>文件</TableHeader><TableHeader>院校</TableHeader><TableHeader>地区</TableHeader><TableHeader>阶段与错误</TableHeader><TableHeader>L1</TableHeader><TableHeader>WeKnora</TableHeader><TableHeader>更新时间</TableHeader><TableHeader>查看</TableHeader></TableRow></TableHead><TableBody>{runs.map((run) => <TableRow key={run.run_id} onClick={() => onRunSelected(run.run_id)} className="clickable-row"><TableCell><div className="file-cell"><Document size={18} /><div><strong>{run.source_filename || run.run_id}</strong><span className="mono">{run.run_id}</span></div></div></TableCell><TableCell><strong>{run.university_name || run.university_id}</strong><span className="subcell">{run.university_id}{run.operation ? ` · ${run.operation}` : ''}{run.source_size_bytes ? ` · ${formatBytes(run.source_size_bytes)}` : ''}</span></TableCell><TableCell><span className="region-cell">{run.region || run.country_code || '未分区'}</span><span className="subcell mono">{run.country_code || '-'}</span></TableCell><TableCell><Tag type={statusKind(run.status)}>{statusLabel(run.status)}</Tag>{run.queue_position && <span className="subcell">队列第 {run.queue_position}</span>}{runStatusDetail(run) && <span className="run-error">{runStatusDetail(run)}</span>}</TableCell><TableCell>{run.opensearch_published || run.status === 'published' || run.status === 'unchanged' ? <Tag type="green">已发布</Tag> : run.status === 'failed' ? <Tag type="red">未发布</Tag> : <Tag type="blue">处理中</Tag>}</TableCell><TableCell><WeKnoraState run={run} /></TableCell><TableCell className="mono">{formatTime(run.updated_at)}</TableCell><TableCell><Button kind="ghost" size="sm" renderIcon={ArrowRight} onClick={(event) => { event.stopPropagation(); onRunSelected(run.run_id) }}>在线查看</Button></TableCell></TableRow>)}</TableBody></Table></div>
}

function publicationStateLabel(state: string): string {
  return ({ current: '当前', superseded: '已替换', failed: '失败', staging: '暂存' }[state] ?? state)
}

function publicationStateKind(state: string): 'green' | 'red' | 'blue' | 'gray' {
  if (state === 'current') return 'green'
  if (state === 'failed') return 'red'
  if (state === 'staging') return 'blue'
  return 'gray'
}

function VersionPage({ onRunSelected }: { onRunSelected: (id: string) => void }) {
  const [versions, setVersions] = useState<UniversityVersion[]>([])
  const [query, setQuery] = useState('')
  const [stateFilter, setStateFilter] = useState('全部')
  const [regionFilter, setRegionFilter] = useState('全部')
  const [loading, setLoading] = useState(false)
  const [loadError, setLoadError] = useState<string | null>(null)
  const stateItems = ['全部', '当前', '已替换', '失败', '暂存']

  const loadVersions = useCallback(async () => {
    setLoading(true)
    try {
      const payload = await apiFetch<{ items: UniversityVersion[] }>('/v1/admin/versions?limit=500')
      setVersions(payload.items)
      setLoadError(null)
    } catch (caught) {
      setVersions([])
      setLoadError(caught instanceof Error ? caught.message : '无法读取 PostgreSQL 版本目录')
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => { void loadVersions() }, [loadVersions])

  const regionItems = regionFilterItems(versions)
  const filtered = versions.filter((version) => {
    const haystack = `${version.university_id ?? ''} ${version.university_name ?? ''} ${version.dataset_version} ${version.version_id} ${version.source_filename ?? ''} ${regionLabel(version)}`.toLowerCase()
    const matchesQuery = !query.trim() || haystack.includes(query.trim().toLowerCase())
    const matchesState = stateFilter === '全部' || publicationStateLabel(version.publication_state) === stateFilter
    const matchesRegion = regionFilter === '全部' || regionLabel(version) === regionFilter
    return matchesQuery && matchesState && matchesRegion
  })
  const groups = groupByRegion(filtered)

  return <div className="versions-page">
    <section className="workbench-section version-catalog-section">
      <div className="section-title-row">
        <div><p className="eyebrow">POSTGRESQL CATALOG</p><h2>版本历史</h2><p>直接读取 PostgreSQL 的 school_versions。这里不依赖文件是否已经提交，也不要求先打开某个运行记录。</p></div>
        <Button kind="ghost" renderIcon={Renew} disabled={loading} onClick={() => void loadVersions()}>刷新列表</Button>
      </div>
      {loadError && <InlineNotification kind="error" lowContrast title="版本目录读取失败" subtitle={loadError} onCloseButtonClick={() => setLoadError(null)} />}
      <div className="files-toolbar">
        <TextInput id="versions-query" size="sm" labelText="搜索版本" placeholder="按院校、版本号或文件名搜索" value={query} onChange={(event) => setQuery(event.target.value)} decorator={<Search size={16} />} />
        <Dropdown id="versions-state" size="sm" titleText="版本状态" label="全部" items={stateItems} selectedItem={stateFilter} onChange={({ selectedItem }) => setStateFilter(selectedItem ?? '全部')} />
        <Dropdown id="versions-region" size="sm" titleText="地区" label="全部" items={regionItems} selectedItem={regionFilter} onChange={({ selectedItem }) => setRegionFilter(selectedItem ?? '全部')} />
        <span className="mono files-count">显示 {filtered.length} / {versions.length}</span>
      </div>
      {groups.length ? groups.map((group) => <RegionSection key={group.key} label={group.label} count={group.items.length} noun="个版本"><VersionCatalogTable versions={group.items} onRunSelected={onRunSelected} /></RegionSection>) : <EmptyState title={loading ? '正在读取 PostgreSQL 版本' : '没有版本记录'} body={versions.length ? '换一个院校、版本号、地区或状态筛选条件。' : loadError ? '接口返回了错误，请先处理上方提示后再刷新。' : '如果数据库中有版本，请检查 Fast Router 是否连接到了同一个 PostgreSQL 实例。'} />}
    </section>
  </div>
}

function VersionCatalogTable({ versions, onRunSelected }: { versions: UniversityVersion[]; onRunSelected: (id: string) => void }) {
  return <div className="table-scroll"><Table size="lg"><TableHead><TableRow><TableHeader>院校</TableHeader><TableHeader>版本</TableHeader><TableHeader>状态</TableHeader><TableHeader>源文件</TableHeader><TableHeader>记录数</TableHeader><TableHeader>创建时间</TableHeader><TableHeader>关联运行</TableHeader></TableRow></TableHead><TableBody>{versions.map((version) => <TableRow key={`${version.university_id ?? 'unknown'}:${version.version_id}`} onClick={() => version.run_id && onRunSelected(version.run_id)} className={version.run_id ? 'clickable-row' : undefined}><TableCell><strong>{version.university_name || version.university_id || '未知院校'}</strong><span className="subcell mono">{version.university_id || '-'}</span></TableCell><TableCell><strong className="mono">{version.dataset_version}</strong><span className="subcell mono">{version.version_id}</span></TableCell><TableCell><Tag type={publicationStateKind(version.publication_state)}>{publicationStateLabel(version.publication_state)}</Tag>{version.rollback_available && <span className="subcell">可回滚</span>}</TableCell><TableCell>{version.source_filename ? <><strong>{version.source_filename}</strong><span className="subcell">{version.source_relative_path || '历史导入未记录路径'}</span></> : <span className="subcell">历史导入未记录源文件名</span>}</TableCell><TableCell><span className="mono">{Object.entries(version.record_counts ?? {}).map(([key, value]) => `${key}:${value}`).join(' · ') || '-'}</span></TableCell><TableCell className="mono">{formatTime(version.published_at || version.created_at)}</TableCell><TableCell>{version.run_id ? <Button kind="ghost" size="sm" renderIcon={ArrowRight} onClick={(event) => { event.stopPropagation(); onRunSelected(version.run_id as string) }}>打开运行</Button> : <Tag type="cool-gray">无运行关联</Tag>}</TableCell></TableRow>)}</TableBody></Table></div>
}

function BatchPage({ batches, selectedBatch, onSelectBatch, onRunSelected }: { batches: Batch[]; selectedBatch: string | null; onSelectBatch: (id: string) => void; onRunSelected: (id: string) => void }) {
  const [detail, setDetail] = useState<Batch | null>(null)
  useEffect(() => { if (!selectedBatch) { setDetail(null); return } void apiFetch<Batch>(`/v1/admin/ingestion-batches/${selectedBatch}`).then(setDetail).catch(() => setDetail(null)) }, [selectedBatch])
  const batchStatus = (value: string) => ({ accepted: '已接收', partial: '部分提交', completed: '已完成', failed: '提交失败' }[value] ?? value)
  const batchTag = (value: string): 'green' | 'red' | 'blue' => value === 'completed' ? 'green' : value === 'failed' ? 'red' : 'blue'
  return <div className="batch-page"><section className="workbench-section batch-list-section"><div className="section-title-row"><div><p className="eyebrow">QUEUE</p><h2>运行批次</h2><p>以批次为单位查看接收、发布和失败范围。点选一行后，下方显示该批次的文件清单。</p></div><Button kind="ghost" renderIcon={Renew} onClick={() => window.location.reload()}>刷新列表</Button></div>{batches.length ? <div className="batch-table"><div className="batch-table-head"><span>批次</span><span>文件</span><span>已接收</span><span>已发布</span><span>失败</span><span>WeKnora 未启用</span><span>状态</span><span>更新时间</span><span aria-hidden="true" /></div>{batches.map((batch) => <button key={batch.batch_id} className={`batch-row ${batch.batch_id === selectedBatch ? 'is-selected' : ''}`} onClick={() => onSelectBatch(batch.batch_id)}><div><strong>{batch.batch_id}</strong><span>{batch.mode === 'directory' ? '服务器目录' : '文件上传'}{batch.source_relative_path ? ` / ${batch.source_relative_path}` : ''}</span></div><div className="batch-metric">{batch.total_count}</div><div className="batch-metric">{batch.accepted_count}</div><div className="batch-metric is-success">{batch.published_count}</div><div className="batch-metric is-failure">{batch.failed_count}</div><div className="batch-metric">{batch.weknora_disabled_count}</div><Tag type={batchTag(batch.status)}>{batchStatus(batch.status)}</Tag><span className="mono">{formatTime(batch.updated_at)}</span><ArrowRight size={16} /></button>)}</div> : <EmptyState title="没有批次" body="从更新院校创建第一个批次。" />}</section>{detail && <section className="workbench-section batch-detail"><div className="section-title-row"><div><p className="eyebrow">BATCH DETAIL</p><h2>{detail.batch_id}</h2><p>{detail.published_count} 个已发布，{detail.failed_count} 个失败，{detail.unchanged_count} 个内容未变化{detail.rejected_count ? `，${detail.rejected_count} 个单项被拒绝` : ''}</p></div><Tag type={batchTag(detail.status)}>{batchStatus(detail.status)}</Tag></div>{detail.rejected_items?.map((item) => <div className="failure-callout" key={item.item_id}><ErrorFilled size={18} /><div><strong>{item.filename}</strong><span>{item.message}</span></div></div>)}<RunTable runs={detail.runs ?? []} onRunSelected={onRunSelected} /></section>}</div>
}

function RunInspector({ run, onClose, onChanged }: { run: IngestionRun; onClose: () => void; onChanged: () => Promise<void> }) {
  const [artifact, setArtifact] = useState('raw_markdown')
  const [artifacts, setArtifacts] = useState<Artifact[]>([])
  const [content, setContent] = useState<ArtifactPage | null>(null)
  const [diff, setDiff] = useState<Record<string, any> | null>(null)
  const [reason, setReason] = useState('')
  const [action, setAction] = useState<'force' | 'rollback' | null>(null)
  const [versions, setVersions] = useState<UniversityVersion[]>([])
  const [rollbackVersionId, setRollbackVersionId] = useState<string | null>(null)
  const [artifactQuery, setArtifactQuery] = useState('')
  const [artifactOffset, setArtifactOffset] = useState(0)
  const [busy, setBusy] = useState(false)
  const [message, setMessage] = useState<string | null>(null)
  const [provenanceTarget, setProvenanceTarget] = useState<{ entity: string; recordId: string } | null>(null)
  const [provenance, setProvenance] = useState<ProvenancePayload | null>(null)
  const [provenanceLoading, setProvenanceLoading] = useState(false)
  const [provenanceError, setProvenanceError] = useState<string | null>(null)
  useEffect(() => {
    void apiFetch<{ items: Artifact[] }>(`/v1/admin/ingestion-runs/${run.run_id}/artifacts`).then((payload) => setArtifacts(payload.items)).catch(() => undefined)
    void apiFetch<Record<string, any>>(`/v1/admin/ingestion-runs/${run.run_id}/diff`).then(setDiff).catch(() => setDiff(null))
    void apiFetch<{ items: UniversityVersion[] }>(`/v1/admin/universities/${encodeURIComponent(run.university_id)}/versions`).then((payload) => setVersions(payload.items)).catch(() => setVersions([]))
  }, [run.run_id, run.university_id])
  useEffect(() => { void apiFetch<ArtifactPage>(`/v1/admin/ingestion-runs/${run.run_id}/artifacts/${artifact}/content?offset=${artifactOffset}&limit=80`).then(setContent).catch(() => setContent(null)) }, [artifact, artifactOffset, run.run_id])
  const forceEligible = run.status === 'failed' && JSON.stringify(run.quality_audits ?? {}).includes('needs_review')
  const runAction = async () => {
    if (!reason.trim()) return
    setBusy(true)
    try {
      if (action === 'force') await apiFetch(`/v1/admin/ingestion-runs/${run.run_id}/force-publish`, { method: 'POST', body: JSON.stringify({ reason }) })
      if (action === 'rollback' && rollbackVersionId) await apiFetch(`/v1/admin/universities/${encodeURIComponent(run.university_id)}/rollback`, { method: 'POST', body: JSON.stringify({ version_id: rollbackVersionId, reason }) })
      setMessage(action === 'force' ? '强制发布已进入队列' : '回滚已提交，L1 正在切换到目标版本')
      setAction(null)
      setRollbackVersionId(null)
      setReason('')
      await onChanged()
    } catch (caught) { setMessage(caught instanceof Error ? caught.message : '操作失败') } finally { setBusy(false) }
  }
  const importCurrent = async () => {
    setBusy(true)
    try {
      const payload = await apiFetch<{ queued_count: number }>(`/v1/admin/universities/${encodeURIComponent(run.university_id)}/weknora/import-current`, { method: 'POST' })
      setMessage(`已显式补导入当前版本，排队 ${payload.queued_count} 个来源`)
      await onChanged()
    } catch (caught) { setMessage(caught instanceof Error ? caught.message : '补导入失败') } finally { setBusy(false) }
  }
  const openProvenance = async (entity: string, recordId: string) => {
    setProvenanceTarget({ entity, recordId })
    setProvenance(null)
    setProvenanceError(null)
    setProvenanceLoading(true)
    try {
      const payload = await apiFetch<ProvenancePayload>(`/v1/admin/ingestion-runs/${encodeURIComponent(run.run_id)}/provenance/${encodeURIComponent(entity)}/${encodeURIComponent(recordId)}`)
      setProvenance(payload)
    } catch (caught) {
      setProvenanceError(caught instanceof Error ? caught.message : '来源映射读取失败')
    } finally {
      setProvenanceLoading(false)
    }
  }
  const selectArtifact = (nextArtifact: string) => {
    setArtifact(nextArtifact)
    setArtifactOffset(0)
    setArtifactQuery('')
    setProvenanceTarget(null)
    setProvenance(null)
    setProvenanceError(null)
  }
  const visibleContent = content && artifact === 'raw_markdown' && artifactQuery.trim() ? { ...content, items: content.items.filter((item) => String(item.text ?? '').toLowerCase().includes(artifactQuery.trim().toLowerCase())) } : content
  const pageEnd = content ? Math.min(content.offset + content.items.length, content.total) : 0
  return (
    <section className="inspector">
      <div className="inspector-header">
        <div><p className="eyebrow">RUN DETAIL</p><h2>{run.source_filename || run.run_id}</h2><p className="mono">{run.run_id} · {run.university_id} · {run.version_id}</p></div>
        <div className="inspector-actions">
          <a className="download-link" href={artifactDownloadUrl(run.run_id, 'all')}><Download size={16} />全部下载</a>
          {run.status === 'published' && run.is_current && <Button kind="tertiary" size="sm" disabled={busy} onClick={() => void importCurrent()}>补导入当前版本</Button>}
          {forceEligible && <Button kind="danger--tertiary" size="sm" onClick={() => setAction('force')}>强制发布</Button>}
          <Button kind="ghost" size="sm" hasIconOnly renderIcon={Undo} iconDescription="关闭" onClick={onClose} />
        </div>
      </div>
      {message && <InlineNotification kind="info" lowContrast title={message} onCloseButtonClick={() => setMessage(null)} />}
      {run.status === 'failed' && <div className="failure-callout"><ErrorFilled size={20} /><div><strong>{run.error_message || '运行失败'}</strong><span>失败阶段和质量审计信息保留在下方。</span></div></div>}
      <div className="inspector-meta">
        <div><span>状态</span><Tag type={statusKind(run.status)}>{statusLabel(run.status)}</Tag></div>
        <div><span>L1</span><strong>{run.opensearch_published ? '已发布' : '未发布'}</strong></div>
        <div><span>WeKnora</span><WeKnoraState run={run} /></div>
        <div><span>更新时间</span><strong>{formatTime(run.updated_at)}</strong></div>
      </div>
      <VersionHistory versions={versions} onRollback={(versionId) => { setRollbackVersionId(versionId); setAction('rollback') }} />
      <Tabs>
        <TabList aria-label="运行详情"><Tab>产物查看</Tab><Tab>差异摘要</Tab><Tab>质量审计</Tab></TabList>
        <TabPanels>
          <TabPanel>
            <div className="artifact-viewer">
              <div className="artifact-rail">
                {artifacts.filter((item) => item.available).map((item) => <button key={item.artifact} className={artifact === item.artifact ? 'is-active' : ''} onClick={() => selectArtifact(item.artifact)}><Document size={16} /><span>{item.artifact === 'raw_markdown' ? 'raw.md' : item.artifact}</span><small>{formatBytes(item.size_bytes)}</small></button>)}
              </div>
              <div className="artifact-content">
                <div className="artifact-heading"><div><strong>在线查看</strong><span>{artifact === 'raw_markdown' ? '原始 Markdown，按行加载' : 'JSONL 记录，按页加载'}</span></div><a href={artifactDownloadUrl(run.run_id, artifact)} className="download-link"><Download size={14} />下载文件</a></div>
                <div className="artifact-toolbar"><span className="mono">{content?.total ?? 0} 行{artifactQuery && visibleContent ? `，当前页命中 ${visibleContent.items.length}` : ''}</span>{artifact === 'raw_markdown' && <TextInput id="artifact-search" size="sm" labelText="搜索 raw" hideLabel placeholder="搜索当前页内容" decorator={<Search size={14} />} value={artifactQuery} onChange={(event) => setArtifactQuery(event.target.value)} />}</div>
                {visibleContent?.items.length ? artifact === 'raw_markdown' ? <pre className="raw-viewer">{visibleContent.items.map((item) => `${String(item.line).padStart(5, ' ')}  ${String(item.text ?? '')}`).join('\n')}</pre> : <div className="jsonl-list">{visibleContent.items.map((item, index) => {
                  const recordId = jsonlRecordId(artifact, item.record)
                  return <div key={index} className="jsonl-record"><span className="line-number">{String(item.line).padStart(4, '0')}</span><div className="jsonl-record-body"><div className="jsonl-record-toolbar"><span className="mono">JSONL 第 {item.line} 行</span>{recordId && <Button kind="ghost" size="sm" onClick={() => void openProvenance(artifact, recordId)}>查看来源映射</Button>}</div><code>{JSON.stringify(item.record ?? item, null, 2)}</code></div></div>
                })}</div> : <EmptyState title="产物不可用" body={artifactQuery ? '没有匹配的行。' : '该运行尚未生成此文件。'} />}
                {artifact !== 'raw_markdown' && provenanceTarget && <ProvenancePanel target={provenanceTarget} payload={provenance} loading={provenanceLoading} error={provenanceError} onClose={() => { setProvenanceTarget(null); setProvenance(null); setProvenanceError(null) }} />}
                <div className="artifact-pagination"><span className="mono">{content?.total ? `${content.offset + 1}-${pageEnd} / ${content.total}` : '暂无内容'}</span><div><Button kind="ghost" size="sm" disabled={artifactOffset === 0} onClick={() => setArtifactOffset(Math.max(0, artifactOffset - 80))}>上一页</Button><Button kind="ghost" size="sm" disabled={!content || pageEnd >= content.total} onClick={() => setArtifactOffset(artifactOffset + 80)}>下一页</Button></div></div>
              </div>
            </div>
          </TabPanel>
          <TabPanel><DiffView diff={diff} /></TabPanel>
          <TabPanel><AuditView run={run} /></TabPanel>
        </TabPanels>
      </Tabs>
      <Modal open={action !== null} modalHeading={action === 'force' ? '确认强制发布' : '确认回滚'} primaryButtonText={busy ? '提交中...' : '确认'} secondaryButtonText="取消" onRequestClose={() => { setAction(null); setRollbackVersionId(null) }} onRequestSubmit={(event) => { event.preventDefault(); void runAction() }}><p className="modal-copy">{action === 'rollback' ? '这会切换 PostgreSQL current、OpenSearch current 和 Fast Router 版本缓存，不会删除 WeKnora 远端文档。请填写操作原因。' : '这会改变当前检索数据。请填写强制发布原因，提交后会留下审计记录。'}</p><TextInput id="action-reason" labelText="操作原因" value={reason} onChange={(event) => setReason(event.target.value)} /></Modal>
    </section>
  )
}

function ProvenancePanel({ target, payload, loading, error, onClose }: { target: { entity: string; recordId: string }; payload: ProvenancePayload | null; loading: boolean; error: string | null; onClose: () => void }) {
  const mapping = payload?.mapping
  const status = mapping?.verification?.status ?? (error ? 'unavailable' : undefined)
  const markdownRange = mapping?.md
  const fields = Object.entries(mapping?.fields ?? {}) as Array<[string, ProvenanceField]>
  const mappingId = mapping?.mapping_id ?? target.recordId
  const statusCopy = status === 'verified' ? '这条记录通过了版本、行号和字段映射检查。' : status === 'review_required' ? '已经找到对应 Markdown，但匹配结果需要人工复核。' : '这条记录暂时没有可用的 Markdown 行级映射，不能把它当作已核验数据。'
  return <section className="provenance-panel" aria-live="polite">
    <div className="provenance-heading"><div><p className="eyebrow">SOURCE MAPPING</p><h3>这条 JSONL 来自哪一行 Markdown？</h3><p>{target.entity} · {target.recordId}</p></div><div className="provenance-heading-actions">{status && <Tag type={provenanceStatusKind(status)}>{provenanceStatusLabel(status)}</Tag>}<Button kind="ghost" size="sm" onClick={onClose}>收起</Button></div></div>
    {loading ? <div className="provenance-loading">正在读取这条记录的来源映射…</div> : error || !payload ? <div className="provenance-unavailable"><strong>暂时无法展示来源映射</strong><span>{error || statusCopy} 老版本运行可能尚未生成 provenance.jsonl。</span></div> : <>
      <p className="provenance-status-copy">{statusCopy}</p>
      <div className="provenance-flow"><span>1. Markdown 原文</span><ArrowRight size={16} /><span>2. 固定解析规则</span><ArrowRight size={16} /><span>3. JSONL 检索记录</span></div>
      <div className="provenance-meta"><span>JSONL 第 <strong>{payload.jsonl.line}</strong> 行</span><span>Markdown 第 <strong>{markdownRange?.line_start}–{markdownRange?.line_end}</strong> 行</span><span>章节：{markdownRange?.section_path || '未标注'}</span><span className="mono">映射 {mappingId}</span></div>
      <div className="provenance-grid">
        <section className="provenance-card"><div className="provenance-card-heading"><div><h4>JSONL（检索用）</h4><span>系统实际返回的结构化记录</span></div><Tag type="blue">第 {payload.jsonl.line} 行</Tag></div><pre>{JSON.stringify(payload.jsonl.record, null, 2)}</pre></section>
        <section className="provenance-card"><div className="provenance-card-heading"><div><h4>Markdown 原文（唯一输入）</h4><span>蓝色行是这条 JSONL 的直接来源</span></div><Tag type="green">第 {markdownRange?.line_start}–{markdownRange?.line_end} 行</Tag></div><div className="provenance-lines">{payload.markdown.items.map((item) => <div key={item.line} className={`provenance-line ${item.highlighted ? 'is-highlighted' : ''}`}><span>{String(item.line).padStart(4, '0')}</span><code>{item.text ?? ''}</code></div>)}</div></section>
      </div>
      <section className="provenance-fields"><div><h4>每个字段是怎么来的</h4><p>“直接来自 Markdown”表示原文能找到；“按固定规则推导”表示不是模型猜的，而是解析规则算出的；“系统运行信息”是版本或状态。</p></div>{fields.length ? <div className="provenance-field-list">{fields.map(([name, field]) => <div className="provenance-field-row" key={name}><code>{name}</code><Tag type={field.kind === 'direct' ? 'green' : field.kind === 'derived' ? 'blue' : 'gray'}>{provenanceFieldKindLabel(field.kind)}</Tag><span className={provenanceFieldKindClass(field.kind)}>{field.kind === 'direct' ? `Markdown 第 ${field.line_start ?? markdownRange?.line_start} 行 · ${field.column ?? name}：${displayValue(field.raw_value)}` : field.rule ? `规则：${field.rule}` : `Markdown 第 ${field.line_start ?? markdownRange?.line_start} 行`}</span></div>)}</div> : <p className="subcell">该映射没有记录字段级说明。</p>}</section>
    </>}
  </section>
}

function VersionHistory({ versions, onRollback }: { versions: UniversityVersion[]; onRollback: (versionId: string) => void }) {
  if (!versions.length) return null
  return <section className="version-history"><div className="section-title-row"><div><p className="eyebrow">VERSION HISTORY</p><h3>历史版本与回滚窗口</h3></div><span className="mono">成功历史保留 90 天</span></div><div className="version-list">{versions.map((version) => <div className="version-row" key={version.version_id}><div><strong>{version.dataset_version}</strong><span className="subcell">{version.publication_state} · {formatTime(version.published_at || version.created_at)} · {version.source_filename || '无源文件名'}</span></div><div className="version-counts">{Object.entries(version.record_counts).slice(0, 2).map(([key, value]) => <span className="mono" key={key}>{key} {value}</span>)}</div>{version.publication_state === 'current' ? <Tag type="green">当前</Tag> : version.rollback_available ? <Button kind="ghost" size="sm" onClick={() => onRollback(version.version_id)}>回滚到此版</Button> : <Tag type="cool-gray">不可回滚</Tag>}</div>)}</div></section>
}

function DiffView({ diff }: { diff: Record<string, any> | null }) {
  if (!diff) return <EmptyState title="差异不可用" body="当前运行没有可比较的标准化产物。" />
  const entities = Object.entries(diff.entities ?? {}) as Array<[string, { counts?: { added?: number; changed?: number; removed?: number }; primary_key?: string }]>
  const affected = diff.affected ?? {}
  const stableIds = ['source_ids', 'entry_ids', 'fact_ids', 'url_ids', 'context_ids'].flatMap((key) => (affected[key] ?? []).map((value: string) => `${key}:${value}`))
  return <div className="diff-view"><div className="diff-summary"><strong>{diff.university_id}</strong><span>{diff.previous_run_id ? `与 ${diff.previous_run_id} 比较` : '没有历史版本'}</span></div><div className="diff-impact"><strong>影响范围</strong><span>{stableIds.length ? `受影响稳定 ID ${stableIds.length} 个` : '暂无稳定 ID 变化'}</span><span>{(affected.source_urls ?? []).length ? `来源 URL ${(affected.source_urls ?? []).length} 个` : '暂无来源 URL 变化'}</span><span>当前检索范围：{diff.impact?.scope ?? '该院校 current'}</span></div>{entities.map(([name, report]) => <div className="diff-row" key={name}><strong>{name}</strong><span className="diff-number added">+{report.counts?.added ?? 0}</span><span className="diff-number changed">~{report.counts?.changed ?? 0}</span><span className="diff-number removed">-{report.counts?.removed ?? 0}</span><span className="mono">{report.primary_key}</span></div>)}</div>
}

function AuditView({ run }: { run: IngestionRun }) {
  const audits = Object.entries(run.quality_audits ?? {})
  if (!audits.length) return <EmptyState title="暂无质量审计" body="解析进入质量校验后会在这里显示报告。" />
  return <div className="audit-view">{audits.map(([key, value]) => <div className="audit-block" key={key}><h3>{key}</h3><pre>{JSON.stringify(value, null, 2)}</pre></div>)}</div>
}

function CopyExample({ text }: { text: string }) {
  const [copied, setCopied] = useState(false)
  const copy = async () => {
    try {
      await navigator.clipboard.writeText(text)
      setCopied(true)
    } catch {
      setCopied(false)
    }
  }
  return <div className="minimum-example"><div className="code-toolbar"><div><strong>MIT 最小结构</strong><span>JSONC 示例，复制后去掉注释即可作为 JSONL 记录</span></div><Button kind="ghost" size="sm" renderIcon={copied ? CheckmarkFilled : Copy} onClick={() => void copy()}>{copied ? '已复制' : '复制示例'}</Button></div><pre>{text}</pre></div>
}

function DocsPage() {
  const [guides, setGuides] = useState<Guide[]>([])
  const [selected, setSelected] = useState<string | null>(null)
  useEffect(() => { void apiFetch<{ items: Guide[] }>('/v1/admin/schema-catalog').then((payload) => { setGuides(payload.items); setSelected(payload.items[0]?.entity ?? null) }).catch(() => undefined) }, [])
  const current = guides.find((guide) => guide.entity === selected) ?? guides[0]
  return <section className="workbench-section docs-section"><div className="section-intro"><div><p className="eyebrow">DATA MODEL</p><h2>五类 JSONL 如何按问题调用</h2><p>拆分是职责分工，不是每个问题都要把五份文件全部检索一遍。先识别问题类型，再只打开能回答它的记录。</p></div></div><SchemaOverview /><div className="docs-layout"><div className="docs-nav">{guides.map((guide) => <button key={guide.entity} className={guide.entity === current?.entity ? 'is-active' : ''} onClick={() => setSelected(guide.entity)}><span className="mono">{guide.entity}</span><strong>{guide.label}</strong></button>)}</div>{current && <div className="docs-content"><h2>{current.label}</h2><p className="lead-copy">{current.purpose}</p><div className="docs-grid"><div><h3>它在检索里的位置</h3><p>{current.role ?? '按职责读取的结构化数据。'}</p><p className="query-rule">{current.query_rule ?? '按问题意图决定是否读取。'}</p></div><div><h3>为什么要拆开</h3><p>{current.why}</p><div className="field-list">{current.links.map((field) => <code key={field}>{field}</code>)}</div></div></div>{(current.entity === 'source_registry' || current.entity === 'url_manifest') && <div className="source-model-note"><strong>MIT 里的实际关系</strong><p>课程页、费用页和索引页的 URL 本身就是来源。MIT 当前两份产物逐条对应同一个 URL，发布到 PostgreSQL 时会折叠到同一张 source_registry 表。url_manifest 只是为了兼容现有产物和 URL 级关联的投影，不需要人工再维护一套官网来源。</p></div>}<h3>最小结构</h3><p className="section-note">下面是以 MIT 为例的最小必需结构。代码块使用 JSONC 注释，方便直接理解每个字段的作用。</p><CopyExample text={MINIMUM_EXAMPLES[current.entity] ?? '{}'} /><h3>字段说明</h3><div className="field-table"><Table size="sm"><TableHead><TableRow><TableHeader>字段</TableHeader><TableHeader>类型</TableHeader><TableHeader>字段描述</TableHeader><TableHeader>MIT 示例</TableHeader></TableRow></TableHead><TableBody>{Object.entries(current.schema.properties ?? {}).map(([field, property]) => { const note = getFieldNote(current.entity, field); return <TableRow key={field}><TableCell className="mono">{field}{current.schema.required?.includes(field) && <span className="required-mark">必填</span>}</TableCell><TableCell>{Array.isArray(property.type) ? property.type.join(' | ') : property.type || (property.enum ? 'enum' : 'object')}</TableCell><TableCell className="field-description">{note.description}{property.enum?.length ? <span className="field-constraint">可选值：{property.enum.join(', ')}</span> : null}</TableCell><TableCell><code className="field-example">{note.example}</code></TableCell></TableRow> })}</TableBody></Table></div></div>}</div><RetrievalGuide /></section>
}

function SchemaOverview() {
  return <section className="schema-overview" aria-labelledby="schema-overview-heading"><div className="schema-overview-heading"><p className="eyebrow">WHY THIS MODEL</p><h2 id="schema-overview-heading">{SCHEMA_OVERVIEW.heading}</h2><p>{SCHEMA_OVERVIEW.lead}</p></div><div className="schema-overview-intro"><div><h3>为什么不合并成一份 JSONL</h3><p>{SCHEMA_OVERVIEW.whyNotSingle}</p></div><div className="schema-overview-reasons">{SCHEMA_OVERVIEW.reasons.map((reason) => <div key={reason.title}><strong>{reason.title}</strong><p>{reason.detail}</p></div>)}</div></div><div className="schema-model-table"><table><caption>五类 JSONL 的记录粒度和必要性</caption><thead><tr><th scope="col">JSONL</th><th scope="col">一行代表什么</th><th scope="col">主要回答什么</th><th scope="col">为什么需要独立</th></tr></thead><tbody>{SCHEMA_OVERVIEW.models.map((model) => <tr key={model.entity}><th scope="row"><code>{model.entity}</code></th><td>{model.grain}</td><td>{model.questions}</td><td>{model.necessity}</td></tr>)}</tbody></table></div><div className="schema-route"><div className="schema-route-heading"><h3>MIT 示例：一个问题不会读取全部五类文件</h3><p>问题是“mit 里有哪些计算机相关的学科”。实际只沿着能产生答案的路径前进。</p></div><div className="schema-route-steps">{SCHEMA_OVERVIEW.mitRoute.map((step, index) => <div className={`schema-route-step ${index === SCHEMA_OVERVIEW.mitRoute.length - 1 ? 'is-skipped' : ''}`} key={step.label}><span>{step.label}</span><strong>{step.detail}</strong>{index < SCHEMA_OVERVIEW.mitRoute.length - 1 && <ArrowRight size={16} aria-hidden="true" />}</div>)}</div></div><div className="source-model-note schema-overview-source-note"><strong>source_registry 和 url_manifest 的关系</strong><p>{SCHEMA_OVERVIEW.sourceNote}</p></div></section>
}

function RetrievalGuide() {
  return <section className="retrieval-guide"><div className="section-title-row"><div><p className="eyebrow">RETRIEVAL FLOW</p><h2>一个问题只走必要的路径</h2><p>例子：用户问“mit里有哪些计算机相关的学科”。下面蓝色路径是本题真正需要的记录，灰色分支是明确跳过的内容。</p></div></div><div className="retrieval-flow" aria-label="MIT 计算机相关学科问题的检索流程">{RETRIEVAL_FLOW.map((step, index) => <div className="flow-step" key={step.label}><div className={`flow-node ${index === 0 ? 'is-query' : index === RETRIEVAL_FLOW.length - 1 ? 'is-result' : ''}`}><span className="flow-label">{step.label}</span><strong>{step.title}</strong><p>{step.detail}</p></div>{index < RETRIEVAL_FLOW.length - 1 && <ArrowRight className="flow-connector" size={20} />}</div>)}</div><div className="retrieval-split"><div className="retrieval-path is-active"><div className="retrieval-path-head"><span className="path-mark">本题查询</span><strong>返回“计算机相关学科”</strong></div><p><code>entity_contexts</code> 只在需要确认范围时使用，核心检索是 <code>catalog_entries</code>，最后沿 <code>source_id</code> 取 <code>source_registry</code> 的官方 URL。</p></div><div className="retrieval-path is-skipped"><div className="retrieval-path-head"><span className="path-mark">本题跳过</span><strong>不查无关事实</strong></div><p><code>quick_facts</code> 只回答学费、截止日期和申请费。<code>url_manifest</code> 在本项目是 URL 关联投影，只有从 URL 反查专业或读取 URL 级导入信息时才单独使用。</p></div></div><div className="retrieval-decisions"><h3>换一个问题，路径会变化</h3>{RETRIEVAL_DECISIONS.map((item) => <div className="retrieval-decision" key={item.question}><div><strong>{item.question}</strong><span>{item.reason}</span></div><div><span className="decision-label">查询</span><code>{item.use}</code></div><div><span className="decision-label">跳过</span><code>{item.skip}</code></div></div>)}</div><div className="retrieval-roles"><div className="retrieval-role-head"><span>JSONL</span><span>主要作用</span><span>它主要回答什么</span></div>{RETRIEVAL_ROLES.map((item) => <div className="retrieval-role" key={item.entity}><code>{item.entity}</code><strong>{item.role}</strong><span>{item.questions}</span></div>)}</div></section>
}

function SettingsPage({ status }: { status: AdminStatus | null }) {
  return <section className="workbench-section settings-section"><div className="section-intro"><div><p className="eyebrow">RUNTIME CONFIGURATION</p><h2>后端配置状态</h2><p>WeKnora 是否导入由后端环境配置决定，管理端只展示状态并提供显式补导入入口。</p></div></div><div className="settings-list"><SettingRow label="导入开关" value={status?.enabled ? 'enabled' : 'disabled'} tone={status?.enabled ? 'green' : 'gray'} /><SettingRow label="服务配置" value={status?.configured ? '已配置' : '未配置'} tone={status?.configured ? 'green' : 'red'} /><SettingRow label="Worker" value={status?.worker_alive ? '运行中' : '未运行'} tone={status?.worker_alive ? 'green' : 'gray'} /><SettingRow label="当前模式" value={status?.import_mode ?? 'unknown'} tone={status?.import_mode === 'enabled' ? 'green' : 'gray'} /><SettingRow label="模板知识库" value={status?.template_knowledge_base_configured ? '已配置' : '未配置'} tone={status?.template_knowledge_base_configured ? 'green' : 'gray'} /><SettingRow label="API Key" value={status?.api_key_configured ? '已配置' : '未配置'} tone={status?.api_key_configured ? 'green' : 'gray'} /></div>{status?.last_error && <InlineNotification kind="error" lowContrast title="Worker 最近错误" subtitle={status.last_error} />}</section>
}

function SettingRow({ label, value, tone }: { label: string; value: string; tone: 'green' | 'red' | 'gray' }) {
  return <div className="setting-row"><span>{label}</span><Tag type={tone}>{value}</Tag></div>
}

export default App
