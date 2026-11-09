"""OPENAI CHATGPT ENTERPRISE API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "chatgpt_enterprise",
    "name": "OPENAI CHATGPT ENTERPRISE API ECOSYSTEM",
    "display_name": "ChatGPT Enterprise",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_enterprise_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Enterprise ChatGPT workspace offering with organization-level administration, security and deployment controls subject to contract and workspace settings.",
    "official_reference": "https://openai.com/enterprise/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
