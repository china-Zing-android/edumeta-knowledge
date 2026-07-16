import assert from "node:assert/strict";
import http from "node:http";
import { type AddressInfo } from "node:net";
import { afterEach, test } from "node:test";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { type CallToolResult } from "@modelcontextprotocol/sdk/types.js";

import {
  createServer,
  resolveServerOptionsFromEnv,
  type GatewayServerOptions,
} from "../src/server.js";

const servers = new Set<http.Server>();

afterEach(async () => {
  await Promise.all([...servers].map(close));
  servers.clear();
});

async function listen(server: http.Server): Promise<number> {
  servers.add(server);
  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  return (server.address() as AddressInfo).port;
}

async function close(server: http.Server): Promise<void> {
  if (!server.listening) return;
  await new Promise<void>((resolve, reject) => {
    server.close((error) => (error ? reject(error) : resolve()));
  });
}

async function request(port: number, path: string): Promise<{ statusCode: number; body: string }> {
  return new Promise((resolve, reject) => {
    http
      .get(`http://127.0.0.1:${port}${path}`, (response) => {
        const chunks: Buffer[] = [];
        response.on("data", (chunk: Buffer) => chunks.push(chunk));
        response.on("end", () => {
          resolve({
            statusCode: response.statusCode ?? 0,
            body: Buffer.concat(chunks).toString("utf8"),
          });
        });
      })
      .on("error", reject);
  });
}

async function connectClient(port: number): Promise<Client> {
  const client = new Client({ name: "gateway-test-client", version: "0.1.0" });
  const transport = new StreamableHTTPClientTransport(new URL(`http://127.0.0.1:${port}/mcp`));
  await client.connect(transport);
  return client;
}

test("health endpoint reports the Tool Gateway service", async () => {
  const port = await listen(createServer());
  const response = await request(port, "/health");

  assert.equal(response.statusCode, 200);
  assert.deepEqual(JSON.parse(response.body), { status: "ok", service: "tool-gateway" });
});

test("only /mcp is exposed as the Streamable HTTP MCP endpoint", async () => {
  const port = await listen(createServer());
  const legacyResponse = await request(port, "/mcp-sdk");

  assert.equal(legacyResponse.statusCode, 404);

  const client = await connectClient(port);
  await client.close();
});

test("MCP exposes only retrieve_university_knowledge", async () => {
  const port = await listen(createServer());
  const client = await connectClient(port);

  try {
    const response = await client.listTools();
    assert.deepEqual(response.tools.map((tool) => tool.name), ["retrieve_university_knowledge"]);
    const description = response.tools[0]?.description ?? "";
    assert.match(description, /direct answer/i);
    assert.match(description, /context is not evidence/i);
  } finally {
    await client.close();
  }
});

test("MCP instructs agents to preserve the original question and evidence boundary", async () => {
  const port = await listen(createServer());
  const client = await connectClient(port);

  try {
    const instructions = client.getInstructions() ?? "";
    assert.match(instructions, /original question verbatim/i);
    assert.match(instructions, /do not append.*topics|do not add.*aspects/i);
    assert.match(instructions, /context is not evidence/i);
    assert.match(instructions, /qualitative.*inference/i);
  } finally {
    await client.close();
  }
});

test("MCP retrieval schema exposes direction and range filters", async () => {
  const port = await listen(createServer());
  const client = await connectClient(port);

  try {
    const response = await client.listTools();
    const schema = response.tools[0]?.inputSchema as { properties?: Record<string, unknown> };
    assert.ok(schema.properties?.direction);
    assert.ok(schema.properties?.filters);
  } finally {
    await client.close();
  }
});

test("retrieve_university_knowledge forwards POST /v1/retrieve and preserves its response", async () => {
  const requestBodies: unknown[] = [];
  const router = http.createServer((requestMessage, response) => {
    assert.equal(requestMessage.method, "POST");
    assert.equal(requestMessage.url, "/v1/retrieve");
    assert.equal(requestMessage.headers["content-type"], "application/json");

    const chunks: Buffer[] = [];
    requestMessage.on("data", (chunk: Buffer) => chunks.push(chunk));
    requestMessage.on("end", () => {
      requestBodies.push(JSON.parse(Buffer.concat(chunks).toString("utf8")));
      response.writeHead(200, { "content-type": "application/json" });
      response.end(
        JSON.stringify({
          trace_id: "tr_gateway",
          mode: "l1",
          scope: { university_id: "mit", dataset_version: "mit_v1" },
          matches: [{ entry_id: "mit_course_6_3" }],
          context: {
            primary_entities: [{ entity_type: "program", entity_id: "mit_course_6_3", display_label: "6-3 Computer Science and Engineering" }],
            related_entities: [],
            available_topics: [],
          },
          evidence: [],
          missing_slots: [],
          warnings: [],
          timings: { total_ms: 12, l1_ms: 10, weknora_ms: 0 },
        }),
      );
    });
  });
  const routerPort = await listen(router);
  const gateway = createServer({ fastRouterBaseUrl: `http://127.0.0.1:${routerPort}` });
  const gatewayPort = await listen(gateway);
  const client = await connectClient(gatewayPort);
  const payload = {
    query: "MIT Course 6-3 本科专业是什么？",
    university_id: "mit",
    context: { level: "undergraduate", program_id: null, entry_id: null },
    max_results: 5,
  };

  try {
    const response = (await client.callTool({
      name: "retrieve_university_knowledge",
      arguments: payload,
    })) as CallToolResult;

    assert.deepEqual(requestBodies, [payload]);
    assert.equal(response.isError, undefined);
    assert.equal(response.content.length, 1);
    const content = response.content[0];
    assert.equal(content?.type, "text");
    if (content?.type !== "text") throw new Error("expected text content");
    assert.deepEqual(JSON.parse(content.text), {
      trace_id: "tr_gateway",
      mode: "l1",
      scope: { university_id: "mit", dataset_version: "mit_v1" },
      matches: [{ entry_id: "mit_course_6_3" }],
      context: {
        primary_entities: [{ entity_type: "program", entity_id: "mit_course_6_3", display_label: "6-3 Computer Science and Engineering" }],
        related_entities: [],
        available_topics: [],
      },
      evidence: [],
      missing_slots: [],
      warnings: [],
      timings: { total_ms: 12, l1_ms: 10, weknora_ms: 0 },
    });
  } finally {
    await client.close();
  }
});

test("structured Fast Router errors are preserved", async () => {
  const routerError = {
    trace_id: "tr_error",
    mode: "error",
    scope: { university_id: "mit", dataset_version: null },
    matches: [],
    evidence: [],
    missing_slots: [],
    warnings: ["invalid_request"],
    timings: { total_ms: 1, l1_ms: 0, weknora_ms: 0 },
    error: { code: "INVALID_REQUEST", message: "query is invalid", retryable: false },
  };
  const router = http.createServer((_request, response) => {
    response.writeHead(422, { "content-type": "application/json" });
    response.end(JSON.stringify(routerError));
  });
  const routerPort = await listen(router);
  const gatewayPort = await listen(
    createServer({ fastRouterBaseUrl: `http://127.0.0.1:${routerPort}` }),
  );
  const client = await connectClient(gatewayPort);

  try {
    const response = (await client.callTool({
      name: "retrieve_university_knowledge",
      arguments: { query: "MIT" },
    })) as CallToolResult;
    assert.equal(response.isError, true);
    const content = response.content[0];
    assert.equal(content?.type, "text");
    if (content?.type !== "text") throw new Error("expected text content");
    assert.deepEqual(JSON.parse(content.text), routerError);
  } finally {
    await client.close();
  }
});

test("Fast Router requests honor the configured timeout", async () => {
  const router = http.createServer((_request, response) => {
    setTimeout(() => {
      response.writeHead(200, { "content-type": "application/json" });
      response.end(JSON.stringify({ trace_id: "too_late" }));
    }, 200);
  });
  const routerPort = await listen(router);
  const gatewayPort = await listen(
    createServer({
      fastRouterBaseUrl: `http://127.0.0.1:${routerPort}`,
      fastRouterTimeoutMs: 20,
    }),
  );
  const client = await connectClient(gatewayPort);

  try {
    const response = (await client.callTool({
      name: "retrieve_university_knowledge",
      arguments: { query: "MIT requirements" },
    })) as CallToolResult;
    assert.equal(response.isError, true);
    const content = response.content[0];
    assert.equal(content?.type, "text");
    if (content?.type !== "text") throw new Error("expected text content");
    const body = JSON.parse(content.text) as {
      context: { primary_entities: unknown[] };
      error: { code: string; message: string; retryable: boolean };
    };
    assert.deepEqual(body.context, {
      primary_entities: [],
      highlights: [],
      sample_children: [],
      related_entities: [],
      available_topics: [],
      presentation_hints: {},
      provenance: { origin: "md_projection", dataset_version: null },
    });
    assert.deepEqual(body.error, {
      code: "FAST_ROUTER_TIMEOUT",
      message: "Fast Router request timed out after 20ms",
      retryable: true,
    });
  } finally {
    await client.close();
  }
});

test("resolveServerOptionsFromEnv reads endpoint and timeout configuration", () => {
  const options: GatewayServerOptions = resolveServerOptionsFromEnv({
    PORT: "9999",
    HOST: "127.0.0.1",
    FAST_ROUTER_BASE_URL: "http://router.internal:8000/",
    FAST_ROUTER_TIMEOUT_MS: "4200",
  });

  assert.deepEqual(options, {
    port: 9999,
    host: "127.0.0.1",
    fastRouterBaseUrl: "http://router.internal:8000",
    fastRouterTimeoutMs: 4200,
  });
});
