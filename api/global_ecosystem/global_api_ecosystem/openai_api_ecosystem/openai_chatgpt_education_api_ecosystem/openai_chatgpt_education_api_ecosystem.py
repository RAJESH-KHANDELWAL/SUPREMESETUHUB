"""OPENAI CHATGPT EDUCATION API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "chatgpt_education",
    "name": "OPENAI CHATGPT EDUCATION API ECOSYSTEM",
    "display_name": "ChatGPT Education",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_education_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Education-focused ChatGPT offering for eligible institutions. Access and controls depend on institutional deployment.",
    "official_reference": "https://openai.com/education/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
