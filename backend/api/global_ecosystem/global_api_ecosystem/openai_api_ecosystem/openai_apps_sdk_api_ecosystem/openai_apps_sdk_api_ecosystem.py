"""OPENAI APPS SDK API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "apps_sdk",
    "name": "OPENAI APPS SDK API ECOSYSTEM",
    "display_name": "Apps SDK",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_apps_sdk_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Developer toolkit for building apps and experiences that run within ChatGPT, including supported MCP-based integrations.",
    "official_reference": "https://developers.openai.com/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
