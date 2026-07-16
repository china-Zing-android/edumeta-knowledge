import http, { type IncomingMessage, type ServerResponse } from "node:http";
import { fileURLToPath } from "node:url";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";

const DEFAULT_FAST_ROUTER_BASE_URL = "http://127.0.0.1:8000";
const DEFAULT_FAST_ROUTER_TIMEOUT_MS = 3_500;
const DEFAULT_PORT = 8_765;
const DEFAULT_HOST = "0.0.0.0";

export const MCP_SERVER_INSTRUCTIONS = `
For university-data questions, call retrieve_university_knowledge and pass the user's original question verbatim.
Do not append related topics, requested aspects, keywords, or facts that the user did not ask for.
Preserve university_id, entry_id, program_id, and level from prior tool results when the conversation establishes them.
Present the direct answer first, followed by useful MD context, related entities, and available follow-up topics.
Context is not evidence. Only the evidence field contains WeKnora citations; do not cite context as page evidence.
Do not make unsupported qualitative inference from curriculum or entity relationships. When a bounded interpretation is useful, label it explicitly as an interpretation based only on the returned fields.
If the response asks for clarification or reports missing evidence, do not fill the gap from model memory.
`.trim();

const retrievalInputSchema = z
  .object({
    query: z.string().min(1),
    university_id: z.string().min(1).optional(),
    context: z
      .object({
        level: z.string().nullable().optional(),
        program_id: z.string().nullable().optional(),
        entry_id: z.string().nullable().optional(),
      })
      .catchall(z.unknown())
      .optional(),
    direction: z.enum(["auto", "downward", "range", "upward"]).optional(),
    filters: z
      .object({
        country_codes: z.array(z.string()).optional(),
        regions: z.array(z.string()).optional(),
        degree_levels: z.array(z.string()).optional(),
        levels: z.array(z.string()).optional(),
        school_tiers: z.array(z.enum(["core", "non_core"])).optional(),
      })
      .strict()
      .optional(),
    max_results: z.number().int().positive().max(20).optional(),
  })
  .passthrough();

type RetrievalRequest = z.infer<typeof retrievalInputSchema>;

interface RouterCallResult {
  body: unknown;
  isError: boolean;
}

interface GatewayRuntimeOptions {
  fastRouterBaseUrl: string;
  fastRouterTimeoutMs: number;
}

export interface GatewayServerOptions extends GatewayRuntimeOptions {
  port: number;
  host: string;
}

type CreateServerOptions = Partial<GatewayRuntimeOptions>;

function normalizeBaseUrl(value: string): string {
  return value.replace(/\/+$/, "");
}

function positiveInteger(value: string | undefined, fallback: number): number {
  const parsed = Number.parseInt(value ?? "", 10);
  return Number.isFinite(parsed) && parsed > 0 ? parsed : fallback;
}

function errorMessage(error: unknown): string {
  return error instanceof Error ? error.message : String(error);
}

function emptyContext(): Record<string, unknown> {
  return {
    primary_entities: [],
    highlights: [],
    sample_children: [],
    related_entities: [],
    available_topics: [],
    presentation_hints: {},
    provenance: { origin: "md_projection", dataset_version: null },
  };
}

function gatewayError(code: string, message: string, retryable: boolean): RouterCallResult {
  return {
    isError: true,
    body: {
      trace_id: null,
      mode: "error",
      scope: null,
      matches: [],
      context: emptyContext(),
      evidence: [],
      missing_slots: [],
      warnings: [],
      timings: { total_ms: 0, l1_ms: 0, weknora_ms: 0 },
      error: { code, message, retryable },
    },
  };
}

async function parseResponseBody(response: Response): Promise<unknown> {
  const responseText = await response.text();
  if (responseText.length === 0) return null;

  try {
    return JSON.parse(responseText) as unknown;
  } catch {
    return {
      trace_id: null,
      mode: "error",
      context: emptyContext(),
      error: {
        code: "FAST_ROUTER_INVALID_RESPONSE",
        message: responseText,
        retryable: response.status >= 500,
      },
    };
  }
}

export async function callRetrievalService(
  payload: RetrievalRequest,
  options: GatewayRuntimeOptions,
): Promise<RouterCallResult> {
  try {
    const response = await fetch(`${normalizeBaseUrl(options.fastRouterBaseUrl)}/v1/retrieve`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
      signal: AbortSignal.timeout(options.fastRouterTimeoutMs),
    });
    return {
      body: await parseResponseBody(response),
      isError: !response.ok,
    };
  } catch (error) {
    if (error instanceof DOMException && error.name === "TimeoutError") {
      return gatewayError(
        "FAST_ROUTER_TIMEOUT",
        `Fast Router request timed out after ${options.fastRouterTimeoutMs}ms`,
        true,
      );
    }
    return gatewayError("FAST_ROUTER_UNAVAILABLE", errorMessage(error), true);
  }
}

export function createMcpServer(options: GatewayRuntimeOptions): McpServer {
  const server = new McpServer(
    { name: "edumeta-university-knowledge", version: "0.2.0" },
    {
      capabilities: { tools: { listChanged: false } },
      instructions: MCP_SERVER_INSTRUCTIONS,
    },
  );

  server.registerTool(
    "retrieve_university_knowledge",
    {
      description: "Retrieve university knowledge. Present the direct answer first, then useful MD context, up to two related entities, and available follow-up topics. Explain course codes with readable names. Context is not evidence; only the evidence field contains WeKnora citations. Preserve university and entry scope in multi-turn calls.",
      inputSchema: retrievalInputSchema,
    },
    async (payload) => {
      const result = await callRetrievalService(payload, options);
      return {
        content: [{ type: "text", text: JSON.stringify(result.body) }],
        ...(result.isError ? { isError: true } : {}),
      };
    },
  );

  return server;
}

async function handleMcpRequest(
  request: IncomingMessage,
  response: ServerResponse,
  options: GatewayRuntimeOptions,
): Promise<void> {
  const server = createMcpServer(options);
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });

  try {
    await server.connect(transport);
    await transport.handleRequest(request, response);
  } catch (error) {
    if (!response.headersSent) {
      response.writeHead(500, { "content-type": "application/json" });
      response.end(
        JSON.stringify({
          jsonrpc: "2.0",
          id: null,
          error: { code: -32603, message: errorMessage(error) },
        }),
      );
    }
  } finally {
    await Promise.allSettled([transport.close(), server.close()]);
  }
}

export function createServer(options: CreateServerOptions = {}): http.Server {
  const runtimeOptions: GatewayRuntimeOptions = {
    fastRouterBaseUrl: normalizeBaseUrl(options.fastRouterBaseUrl ?? DEFAULT_FAST_ROUTER_BASE_URL),
    fastRouterTimeoutMs: options.fastRouterTimeoutMs ?? DEFAULT_FAST_ROUTER_TIMEOUT_MS,
  };

  return http.createServer(async (request, response) => {
    const pathname = new URL(request.url ?? "/", "http://localhost").pathname;

    if (pathname === "/health" && request.method === "GET") {
      response.writeHead(200, { "content-type": "application/json" });
      response.end(JSON.stringify({ status: "ok", service: "tool-gateway" }));
      return;
    }

    if (pathname === "/mcp") {
      await handleMcpRequest(request, response, runtimeOptions);
      return;
    }

    response.writeHead(404, { "content-type": "text/plain" });
    response.end("not found");
  });
}

export function resolveServerOptionsFromEnv(
  env: Readonly<Record<string, string | undefined>> = process.env,
): GatewayServerOptions {
  return {
    port: positiveInteger(env.PORT, DEFAULT_PORT),
    host: env.HOST || DEFAULT_HOST,
    fastRouterBaseUrl: normalizeBaseUrl(env.FAST_ROUTER_BASE_URL || DEFAULT_FAST_ROUTER_BASE_URL),
    fastRouterTimeoutMs: positiveInteger(
      env.FAST_ROUTER_TIMEOUT_MS,
      DEFAULT_FAST_ROUTER_TIMEOUT_MS,
    ),
  };
}

export function startServer(options: GatewayServerOptions = resolveServerOptionsFromEnv()): http.Server {
  const server = createServer(options);
  server.listen(options.port, options.host, () => {
    console.log(`Tool Gateway listening on http://${options.host}:${options.port}/mcp`);
  });
  return server;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  startServer();
}
