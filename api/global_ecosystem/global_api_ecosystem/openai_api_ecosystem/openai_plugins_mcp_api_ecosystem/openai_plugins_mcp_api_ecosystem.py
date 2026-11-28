"""OPENAI PLUGINS AND MCP API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "plugins_mcp",
    "name": "OPENAI PLUGINS AND MCP API ECOSYSTEM",
    "display_name": "Plugins and MCP",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_plugins_mcp_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Extension and tool integration ecosystem spanning supported ChatGPT/Codex plugin surfaces and Model Context Protocol servers. Distinguish product plugins from MCP protocol integrations.",
    "official_reference": "https://developers.openai.com/chatgpt",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
