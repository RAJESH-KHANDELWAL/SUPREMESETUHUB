# OPENAI PLUGINS AND MCP API ECOSYSTEM

- **Provider:** OpenAI
- **Product/service:** Plugins and MCP
- **Service ID:** `plugins_mcp`
- **Catalog status:** `active_catalog`
- **Live connection verified:** No

## Scope

Extension and tool integration ecosystem spanning supported ChatGPT/Codex plugin surfaces and Model Context Protocol servers. Distinguish product plugins from MCP protocol integrations.

## Integration boundary

This folder identifies the product/service and records its official reference. It is catalog metadata, not a claim that a production adapter, public API, OAuth flow or user connection screen is implemented. Implement only documented interfaces and mark connection status only after safe deployment-level testing.

Where API credentials apply, use authenticated tenant-scoped access, encrypted secret storage, server-side validation, redacted logs, rate limits and revocation. Do not invent APIs for product surfaces that do not expose them.

## Official reference

https://developers.openai.com/chatgpt
