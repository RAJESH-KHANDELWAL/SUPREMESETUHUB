"""OPENAI CHATGPT HEALTH API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "chatgpt_health",
    "name": "OPENAI CHATGPT HEALTH API ECOSYSTEM",
    "display_name": "ChatGPT Health",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_health_api_ecosystem",
    "status": "availability_dependent_catalog",
    "live_connection_verified": False,
    "description": "Health-focused ChatGPT experience. It is not a diagnostic API; connected-data access and eligibility are subject to official availability and safeguards.",
    "official_reference": "https://chatgpt.com/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
