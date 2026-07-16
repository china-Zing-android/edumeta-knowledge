import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { type CallToolResult } from "@modelcontextprotocol/sdk/types.js";

function argumentValue(name: string): string | undefined {
  const index = process.argv.indexOf(name);
  return index >= 0 ? process.argv[index + 1] : undefined;
}

function textContent(result: CallToolResult): string {
  const content = result.content[0];
  return content?.type === "text" ? content.text : JSON.stringify(result);
}

async function main(): Promise<void> {
  const url = argumentValue("--url");
  if (!url) throw new Error("--url is required");

  const client = new Client({ name: "edumeta-sdk-smoke-client", version: "0.2.0" });
  const transport = new StreamableHTTPClientTransport(new URL(url));

  try {
    await client.connect(transport);
    if (process.argv.includes("--list-tools")) {
      console.log(JSON.stringify(await client.listTools()));
      return;
    }

    const argumentsJson = argumentValue("--args-json") ?? "{}";
    const result = (await client.callTool({
      name: "retrieve_university_knowledge",
      arguments: JSON.parse(argumentsJson) as Record<string, unknown>,
    })) as CallToolResult;
    console.log(textContent(result));
    if (result.isError) process.exitCode = 1;
  } finally {
    await client.close();
  }
}

main().catch((error: unknown) => {
  console.error(error instanceof Error ? error.stack ?? error.message : String(error));
  process.exitCode = 1;
});
