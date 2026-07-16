import { performance } from "node:perf_hooks";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

function argument(name: string, fallback: string): string {
  const index = process.argv.indexOf(name);
  return index >= 0 ? process.argv[index + 1] ?? fallback : fallback;
}

function percentile(values: number[], p: number): number {
  const ordered = [...values].sort((a, b) => a - b);
  const index = Math.max(0, Math.min(ordered.length - 1, Math.round((ordered.length - 1) * p)));
  return ordered[index] ?? 0;
}

async function main(): Promise<void> {
  const url = argument("--url", "http://127.0.0.1:8765/mcp");
  const runs = Number.parseInt(argument("--runs", "50"), 10);
  const client = new Client({ name: "edumeta-mcp-benchmark", version: "0.2.0" });
  const transport = new StreamableHTTPClientTransport(new URL(url));
  const timings: number[] = [];
  try {
    await client.connect(transport);
    await client.callTool({ name: "retrieve_university_knowledge", arguments: { query: "MIT Course 6-3", university_id: "mit" } });
    for (let index = 0; index < runs; index += 1) {
      const started = performance.now();
      await client.callTool({ name: "retrieve_university_knowledge", arguments: { query: "MIT Course 6-3", university_id: "mit" } });
      timings.push(performance.now() - started);
    }
  } finally {
    await client.close();
  }
  const p95 = percentile(timings, 0.95);
  const report = { status: p95 < 1000 ? "passed" : "failed", runs, p50_ms: percentile(timings, 0.5), p95_ms: p95, max_ms: Math.max(...timings) };
  console.log(JSON.stringify(report));
  if (report.status !== "passed") process.exitCode = 1;
}

main().catch((error: unknown) => {
  console.error(error instanceof Error ? error.stack ?? error.message : String(error));
  process.exitCode = 1;
});
