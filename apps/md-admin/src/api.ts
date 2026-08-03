export type AdminStatus = {
  enabled: boolean
  configured: boolean
  worker_alive: boolean
  import_mode: 'enabled' | 'disabled' | 'misconfigured'
  last_error: string | null
  template_knowledge_base_configured: boolean
  api_key_configured: boolean
}

export type PreviewItem = {
  item_id: string
  filename: string
  relative_path: string
  source_root_id: string | null
  storage_name?: string | null
  size_bytes: number
  sha256: string
  operation: 'create' | 'update'
  issues: Array<{ code: string; message: string; impact?: Record<string, unknown> }>
  ready: boolean
  university_id: string
  university_name: string
  country_code: string | null
  region: string | null
  school_tier: 'core' | 'non_core'
  aliases: string[]
}

export type Preview = {
  preview_id: string
  mode: 'upload' | 'directory'
  source_root_id: string | null
  source_relative_path: string | null
  expires_at: string
  total_count: number
  ready_count: number
  blocked_count: number
  items: PreviewItem[]
}

export type IngestionRun = {
  run_id: string
  university_id: string
  university_name?: string | null
  country_code?: string | null
  region?: string | null
  school_tier: string
  operation: string
  version_id: string
  input_hash: string
  status: string
  counts: Record<string, number>
  stage_failures: Array<Record<string, unknown>>
  error_message: string | null
  weknora_error?: string | null
  opensearch_published: boolean
  weknora_jobs: Record<string, number>
  created_at: string
  updated_at: string
  source_filename?: string | null
  source_size_bytes?: number | null
  source_relative_path?: string | null
  source_mode?: string | null
  force_publish_requested?: boolean
  force_publish_reason?: string | null
  queue_position?: number | null
  is_current?: boolean
  weknora?: {
    summary: 'disabled' | 'partial_failure' | 'pending_or_success' | 'not_started'
    failed: number
    has_success: number
    source_count: number
  }
  quality_audits?: Record<string, any>
}

export type Batch = {
  batch_id: string
  mode: 'upload' | 'directory'
  source_root_id: string | null
  source_relative_path: string | null
  status: string
  total_count: number
  accepted_count: number
  published_count: number
  failed_count: number
  unchanged_count: number
  weknora_disabled_count: number
  created_at: string
  updated_at: string
  run_ids: string[]
  runs?: IngestionRun[]
  rejected_count?: number
  rejected_items?: Array<{ item_id: string; filename: string; relative_path: string; message: string }>
}

export type UniversityVersion = {
  university_id?: string
  university_name?: string | null
  country_code?: string | null
  region?: string | null
  version_id: string
  dataset_version: string
  publication_state: 'current' | 'superseded' | 'failed' | 'staging'
  record_counts: Record<string, number>
  created_at: string
  published_at: string | null
  superseded_at: string | null
  run_id: string | null
  run_status: string | null
  source_filename: string | null
  source_relative_path?: string | null
  source_root_id?: string | null
  artifact_available?: boolean
  rollback_available: boolean
}

export type Artifact = {
  artifact: string
  filename: string
  available: boolean
  size_bytes?: number
  sha256?: string
  line_count?: number
}

export type SourceFile = {
  filename: string
  relative_path: string
  source_root_id: string
  size_bytes: number
  modified_at: string
  sha256: string | null
  university_id: string
  university_name: string
  country_code: string | null
  region: string | null
  school_tier: 'core' | 'non_core'
  operation: 'create' | 'update'
  issues: Array<{ code: string; message: string; impact?: Record<string, unknown> }>
  ready: boolean
  source_status: string
  run_id: string | null
  run_university_id: string | null
  run_university_name: string | null
  run_operation: string | null
  run_version_id: string | null
  run_updated_at: string | null
  is_current: boolean
}

const API_BASE = (import.meta.env.VITE_API_BASE_URL ?? '').replace(/\/$/, '')

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  let response: Response
  try {
    response = await fetch(`${API_BASE}${path}`, {
      ...init,
      headers: {
        ...(init?.body instanceof FormData ? {} : { 'Content-Type': 'application/json' }),
        ...init?.headers,
      },
    })
  } catch (caught) {
    const detail = caught instanceof Error ? caught.message : 'network request failed'
    throw new Error(`无法连接 Fast Router（${API_BASE || '开发代理 → http://127.0.0.1:8000'}）：${detail}`)
  }
  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`
    try {
      const contentType = response.headers.get('content-type') ?? ''
      if (contentType.includes('application/json')) {
        const payload = await response.json()
        message = typeof payload.detail === 'string' ? payload.detail : JSON.stringify(payload.detail ?? payload)
      } else {
        const body = await response.text()
        if (/proxy error|econnrefused|connect .* failed/i.test(body)) {
          message = `无法连接 Fast Router（${API_BASE || '开发代理 → http://127.0.0.1:8000'}）`
        } else if (body.trim()) {
          message = `${message}: ${body.trim().slice(0, 240)}`
        }
      }
    } catch {
      // Preserve the HTTP status when the body is not JSON.
    }
    throw new Error(message)
  }
  const contentType = response.headers.get('content-type') ?? ''
  if (!contentType.includes('application/json')) {
    throw new Error(`管理端返回了非 JSON 响应（${response.status}），请检查 API 地址或开发代理配置`)
  }
  return response.json() as Promise<T>
}

export function artifactDownloadUrl(runId: string, artifact: string): string {
  return `${API_BASE}/v1/admin/ingestion-runs/${encodeURIComponent(runId)}/artifacts/${encodeURIComponent(artifact)}/download`
}
