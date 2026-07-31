import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import {
  Activity,
  ArrowRight,
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
  Preview,
  PreviewItem,
  UniversityVersion,
} from './api'
import './styles.css'

type Page = 'workspace' | 'batches' | 'docs' | 'settings'
type ArtifactPage = { artifact: string; offset: number; limit: number; total: number; items: Array<Record<string, unknown>> }
type Guide = { entity: string; label: string; purpose: string; why: string; minimum: string[]; links: string[]; schema: { required?: string[]; properties?: Record<string, { type?: string | string[]; enum?: string[] }> } }

const NAV_ITEMS: Array<{ id: Page; label: string; icon: typeof Activity }> = [
  { id: 'workspace', label: '更新工作台', icon: CloudUpload },
  { id: 'batches', label: '运行批次', icon: Activity },
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

function WeKnoraState({ run }: { run: IngestionRun }) {
  if (run.weknora?.summary === 'disabled') return <Tag type="gray">WeKnora 未启用</Tag>
  if (run.weknora?.summary === 'partial_failure') return <span><Tag type="red">L1 已发布，WeKnora 部分失败</Tag>{run.weknora_error && <span className="subcell">{run.weknora_error}</span>}</span>
  if (run.weknora?.summary === 'pending_or_success') return <Tag type="blue">WeKnora 导入处理中</Tag>
  return <Tag type="cool-gray">未开始</Tag>
}

function EmptyState({ title, body }: { title: string; body: string }) {
  return <div className="empty-state"><Document size={28} /><h3>{title}</h3><p>{body}</p></div>
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

  const loadOverview = useCallback(async () => {
    setRefreshing(true)
    try {
      const [config, batchPayload, runPayload] = await Promise.all([
        apiFetch<AdminStatus>('/v1/admin/config/status'),
        apiFetch<{ items: Batch[] }>('/v1/admin/ingestion-batches?limit=30'),
        apiFetch<{ items: IngestionRun[] }>('/v1/admin/ingestion-runs?limit=50'),
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
              <button key={id} className={`nav-item ${page === id ? 'is-active' : ''}`} onClick={() => setPage(id)}>
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
          {error && <InlineNotification kind="error" lowContrast title="管理端接口不可用" subtitle={error} onCloseButtonClick={() => setError(null)} />}
          <div className="page-heading">
            <div>
              <p className="eyebrow">MARKDOWN INGESTION</p>
              <h1>{NAV_ITEMS.find((item) => item.id === page)?.label}</h1>
              <p className="heading-copy">把 Markdown 作为唯一源文件，观察每次解析、校验、发布和下游导入。</p>
            </div>
            <div className="heading-meta"><span className="mono">L1 / L2</span><span>内部网络</span></div>
          </div>
          {page === 'workspace' && <Workspace onBatchCreated={loadOverview} onRunSelected={setSelectedRun} />}
          {page === 'batches' && <BatchPage batches={batches} selectedBatch={selectedBatch} onSelectBatch={setSelectedBatch} onRunSelected={setSelectedRun} />}
          {page === 'docs' && <DocsPage />}
          {page === 'settings' && <SettingsPage status={status} />}
          {currentRun && <RunInspector run={currentRun} onClose={() => setSelectedRun(null)} onChanged={loadOverview} />}
        </main>
      </div>
    </div>
  )
}

function Workspace({ onBatchCreated, onRunSelected }: { onBatchCreated: () => Promise<void>; onRunSelected: (id: string) => void }) {
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
    <section className="workbench-section recent-section"><div className="section-title-row"><div><p className="eyebrow">RECENT RUNS</p><h2>最近运行</h2></div><button className="text-action" onClick={() => window.dispatchEvent(new Event('refresh-runs'))}>查看全部 <ArrowRight size={16} /></button></div><RecentRuns onRunSelected={onRunSelected} /></section>
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

function RunTable({ runs, onRunSelected }: { runs: IngestionRun[]; onRunSelected: (id: string) => void }) {
  return <div className="table-scroll"><Table size="lg"><TableHead><TableRow><TableHeader>文件</TableHeader><TableHeader>院校</TableHeader><TableHeader>阶段</TableHeader><TableHeader>L1</TableHeader><TableHeader>WeKnora</TableHeader><TableHeader>更新时间</TableHeader></TableRow></TableHead><TableBody>{runs.map((run) => <TableRow key={run.run_id} onClick={() => onRunSelected(run.run_id)} className="clickable-row"><TableCell><div className="file-cell"><Document size={18} /><div><strong>{run.source_filename || run.run_id}</strong><span className="mono">{run.run_id}</span></div></div></TableCell><TableCell><strong>{run.university_id}</strong><span className="subcell">{run.operation}</span></TableCell><TableCell><Tag type={statusKind(run.status)}>{statusLabel(run.status)}</Tag>{run.queue_position && <span className="subcell">队列第 {run.queue_position}</span>}</TableCell><TableCell>{run.status === 'published' ? <Tag type="green">已发布</Tag> : run.status === 'failed' ? <Tag type="red">失败</Tag> : <Tag type="blue">处理中</Tag>}</TableCell><TableCell><WeKnoraState run={run} /></TableCell><TableCell className="mono">{formatTime(run.updated_at)}</TableCell></TableRow>)}</TableBody></Table></div>
}

function BatchPage({ batches, selectedBatch, onSelectBatch, onRunSelected }: { batches: Batch[]; selectedBatch: string | null; onSelectBatch: (id: string) => void; onRunSelected: (id: string) => void }) {
  const [detail, setDetail] = useState<Batch | null>(null)
  useEffect(() => { if (!selectedBatch) { setDetail(null); return } void apiFetch<Batch>(`/v1/admin/ingestion-batches/${selectedBatch}`).then(setDetail).catch(() => setDetail(null)) }, [selectedBatch])
  return <div className="batch-layout"><section className="workbench-section"><div className="section-title-row"><div><p className="eyebrow">QUEUE</p><h2>运行批次</h2></div><Button kind="ghost" renderIcon={Renew} onClick={() => window.location.reload()}>刷新</Button></div>{batches.length ? <div className="batch-list">{batches.map((batch) => <button key={batch.batch_id} className={`batch-row ${batch.batch_id === selectedBatch ? 'is-selected' : ''}`} onClick={() => onSelectBatch(batch.batch_id)}><div><strong>{batch.batch_id}</strong><span>{batch.mode === 'directory' ? '服务器目录' : '文件上传'} · {formatTime(batch.created_at)}</span></div><div className="batch-count"><strong>{batch.total_count}</strong><span>文件</span></div><Tag type={batch.status === 'completed' ? 'green' : batch.status === 'failed' ? 'red' : 'blue'}>{batch.status}</Tag><ArrowRight size={16} /></button>)}</div> : <EmptyState title="没有批次" body="从更新工作台创建第一个批次。" />}</section>{detail && <section className="workbench-section batch-detail"><div className="section-title-row"><div><p className="eyebrow">BATCH DETAIL</p><h2>{detail.batch_id}</h2><p>{detail.published_count} 已发布 · {detail.failed_count} 失败 · {detail.unchanged_count} 未变化{detail.rejected_count ? ` · ${detail.rejected_count} 项被拒绝` : ''}</p></div><Tag type="blue">{detail.status}</Tag></div>{detail.rejected_items?.map((item) => <div className="failure-callout" key={item.item_id}><ErrorFilled size={18} /><div><strong>{item.filename}</strong><span>{item.message}</span></div></div>)}<RunTable runs={detail.runs ?? []} onRunSelected={onRunSelected} /></section>}</div>
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
  const [busy, setBusy] = useState(false)
  const [message, setMessage] = useState<string | null>(null)
  useEffect(() => {
    void apiFetch<{ items: Artifact[] }>(`/v1/admin/ingestion-runs/${run.run_id}/artifacts`).then((payload) => setArtifacts(payload.items)).catch(() => undefined)
    void apiFetch<Record<string, any>>(`/v1/admin/ingestion-runs/${run.run_id}/diff`).then(setDiff).catch(() => setDiff(null))
    void apiFetch<{ items: UniversityVersion[] }>(`/v1/admin/universities/${encodeURIComponent(run.university_id)}/versions`).then((payload) => setVersions(payload.items)).catch(() => setVersions([]))
  }, [run.run_id, run.university_id])
  useEffect(() => { void apiFetch<ArtifactPage>(`/v1/admin/ingestion-runs/${run.run_id}/artifacts/${artifact}/content?offset=0&limit=80`).then(setContent).catch(() => setContent(null)) }, [artifact, run.run_id])
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
  const visibleContent = content && artifact === 'raw_markdown' && artifactQuery.trim() ? { ...content, items: content.items.filter((item) => String(item.text ?? '').toLowerCase().includes(artifactQuery.trim().toLowerCase())) } : content
  return <section className="inspector"><div className="inspector-header"><div><p className="eyebrow">RUN DETAIL</p><h2>{run.source_filename || run.run_id}</h2><p className="mono">{run.run_id} · {run.university_id} · {run.version_id}</p></div><div className="inspector-actions"><a className="download-link" href={artifactDownloadUrl(run.run_id, 'all')}><Download size={16} />全部下载</a>{run.status === 'published' && run.is_current && <Button kind="tertiary" size="sm" disabled={busy} onClick={() => void importCurrent()}>补导入当前版本</Button>}{forceEligible && <Button kind="danger--tertiary" size="sm" onClick={() => setAction('force')}>强制发布</Button>}<Button kind="ghost" size="sm" hasIconOnly renderIcon={Undo} iconDescription="关闭" onClick={onClose} /></div></div>{message && <InlineNotification kind="info" lowContrast title={message} onCloseButtonClick={() => setMessage(null)} />}{run.status === 'failed' && <div className="failure-callout"><ErrorFilled size={20} /><div><strong>{run.error_message || '运行失败'}</strong><span>失败阶段和质量审计信息保留在下方。</span></div></div>}<div className="inspector-meta"><div><span>状态</span><Tag type={statusKind(run.status)}>{statusLabel(run.status)}</Tag></div><div><span>L1</span><strong>{run.opensearch_published ? '已发布' : '未发布'}</strong></div><div><span>WeKnora</span><WeKnoraState run={run} /></div><div><span>更新时间</span><strong>{formatTime(run.updated_at)}</strong></div></div><VersionHistory versions={versions} onRollback={(versionId) => { setRollbackVersionId(versionId); setAction('rollback') }} /><Tabs><TabList aria-label="运行详情"><Tab>产物查看</Tab><Tab>差异摘要</Tab><Tab>质量审计</Tab></TabList><TabPanels><TabPanel><div className="artifact-viewer"><div className="artifact-rail">{artifacts.filter((item) => item.available).map((item) => <button key={item.artifact} className={artifact === item.artifact ? 'is-active' : ''} onClick={() => setArtifact(item.artifact)}><Document size={16} /><span>{item.artifact === 'raw_markdown' ? 'raw.md' : item.artifact}</span><small>{formatBytes(item.size_bytes)}</small></button>)}</div><div className="artifact-content"><div className="artifact-toolbar"><span className="mono">{content?.total ?? 0} 行{artifactQuery && visibleContent ? ` · 命中 ${visibleContent.items.length}` : ''}</span>{artifact === 'raw_markdown' && <TextInput id="artifact-search" size="sm" labelText="搜索 raw" hideLabel placeholder="搜索 raw 内容" decorator={<Search size={14} />} value={artifactQuery} onChange={(event) => setArtifactQuery(event.target.value)} />}<a href={artifactDownloadUrl(run.run_id, artifact)} className="download-link"><Download size={14} />下载文件</a></div>{visibleContent?.items.length ? artifact === 'raw_markdown' ? <pre className="raw-viewer">{visibleContent.items.map((item) => `${String(item.line).padStart(5, ' ')}  ${String(item.text ?? '')}`).join('\n')}</pre> : <div className="jsonl-list">{visibleContent.items.map((item, index) => <div key={index} className="jsonl-record"><span className="line-number">{String(item.line).padStart(4, '0')}</span><code>{JSON.stringify(item.record ?? item, null, 2)}</code></div>)}</div> : <EmptyState title="产物不可用" body={artifactQuery ? '没有匹配的行。' : '该运行尚未生成此文件。'} />}</div></div></TabPanel><TabPanel><DiffView diff={diff} /></TabPanel><TabPanel><AuditView run={run} /></TabPanel></TabPanels></Tabs><Modal open={action !== null} modalHeading={action === 'force' ? '确认强制发布' : '确认回滚'} primaryButtonText={busy ? '提交中...' : '确认'} secondaryButtonText="取消" onRequestClose={() => { setAction(null); setRollbackVersionId(null) }} onRequestSubmit={(event) => { event.preventDefault(); void runAction() }}><p className="modal-copy">{action === 'rollback' ? '这会切换 PostgreSQL current、OpenSearch current 和 Fast Router 版本缓存，不会删除 WeKnora 远端文档。请填写操作原因。' : '这会改变当前检索数据。请填写强制发布原因，提交后会留下审计记录。'}</p><TextInput id="action-reason" labelText="操作原因" value={reason} onChange={(event) => setReason(event.target.value)} /></Modal></section>
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

function DocsPage() {
  const [guides, setGuides] = useState<Guide[]>([])
  const [selected, setSelected] = useState<string | null>(null)
  useEffect(() => { void apiFetch<{ items: Guide[] }>('/v1/admin/schema-catalog').then((payload) => { setGuides(payload.items); setSelected(payload.items[0]?.entity ?? null) }).catch(() => undefined) }, [])
  const current = guides.find((guide) => guide.entity === selected) ?? guides[0]
  return <section className="workbench-section docs-section"><div className="section-intro"><div><p className="eyebrow">DATA MODEL</p><h2>五类 JSONL 如何协作</h2><p>这些文件不是重复导出，而是把检索、事实、来源、关联和上下文拆成可以独立验证的层。</p></div></div><div className="docs-layout"><div className="docs-nav">{guides.map((guide) => <button key={guide.entity} className={guide.entity === current?.entity ? 'is-active' : ''} onClick={() => setSelected(guide.entity)}><span className="mono">{guide.entity}</span><strong>{guide.label}</strong></button>)}</div>{current && <div className="docs-content"><h2>{current.label}</h2><p className="lead-copy">{current.purpose}</p><div className="docs-grid"><div><h3>为什么要拆开</h3><p>{current.why}</p></div><div><h3>稳定关联字段</h3><div className="field-list">{current.links.map((field) => <code key={field}>{field}</code>)}</div></div></div><h3>最小结构</h3><div className="required-fields">{(current.schema.required ?? current.minimum).map((field) => <span key={field}><CheckmarkFilled size={14} />{field}</span>)}</div><h3>字段类型</h3><div className="field-table"><Table size="sm"><TableHead><TableRow><TableHeader>字段</TableHeader><TableHeader>类型</TableHeader><TableHeader>约束</TableHeader></TableRow></TableHead><TableBody>{Object.entries(current.schema.properties ?? {}).slice(0, 18).map(([field, property]) => <TableRow key={field}><TableCell className="mono">{field}</TableCell><TableCell>{Array.isArray(property.type) ? property.type.join(' | ') : property.type || 'object'}</TableCell><TableCell>{property.enum?.join(', ') || (current.schema.required?.includes(field) ? '必填' : '可选')}</TableCell></TableRow>)}</TableBody></Table></div></div>}</div></section>
}

function SettingsPage({ status }: { status: AdminStatus | null }) {
  return <section className="workbench-section settings-section"><div className="section-intro"><div><p className="eyebrow">RUNTIME CONFIGURATION</p><h2>后端配置状态</h2><p>WeKnora 是否导入由后端环境配置决定，管理端只展示状态并提供显式补导入入口。</p></div></div><div className="settings-list"><SettingRow label="导入开关" value={status?.enabled ? 'enabled' : 'disabled'} tone={status?.enabled ? 'green' : 'gray'} /><SettingRow label="服务配置" value={status?.configured ? '已配置' : '未配置'} tone={status?.configured ? 'green' : 'red'} /><SettingRow label="Worker" value={status?.worker_alive ? '运行中' : '未运行'} tone={status?.worker_alive ? 'green' : 'gray'} /><SettingRow label="当前模式" value={status?.import_mode ?? 'unknown'} tone={status?.import_mode === 'enabled' ? 'green' : 'gray'} /><SettingRow label="模板知识库" value={status?.template_knowledge_base_configured ? '已配置' : '未配置'} tone={status?.template_knowledge_base_configured ? 'green' : 'gray'} /><SettingRow label="API Key" value={status?.api_key_configured ? '已配置' : '未配置'} tone={status?.api_key_configured ? 'green' : 'gray'} /></div>{status?.last_error && <InlineNotification kind="error" lowContrast title="Worker 最近错误" subtitle={status.last_error} />}</section>
}

function SettingRow({ label, value, tone }: { label: string; value: string; tone: 'green' | 'red' | 'gray' }) {
  return <div className="setting-row"><span>{label}</span><Tag type={tone}>{value}</Tag></div>
}

export default App
