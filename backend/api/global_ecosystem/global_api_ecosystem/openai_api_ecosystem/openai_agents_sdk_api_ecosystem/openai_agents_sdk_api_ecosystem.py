"""OPENAI AGENTS SDK API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "agents_sdk",
    "name": "OPENAI AGENTS SDK API ECOSYSTEM",
    "display_name": "Agents SDK",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_agents_sdk_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Developer SDK for building agent loops, tools, handoffs and application-managed agent workflows.",
    "official_reference": "https://developers.openai.com/api/docs/guides/agents",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
