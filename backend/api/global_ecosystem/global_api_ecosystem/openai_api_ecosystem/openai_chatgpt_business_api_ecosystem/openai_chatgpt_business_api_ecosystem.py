"""OPENAI CHATGPT BUSINESS API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "chatgpt_business",
    "name": "OPENAI CHATGPT BUSINESS API ECOSYSTEM",
    "display_name": "ChatGPT Business",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_business_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "ChatGPT workspace offering for businesses, with organization collaboration and administrative controls. It is a plan/workspace product, not a separate model API.",
    "official_reference": "https://openai.com/business/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
