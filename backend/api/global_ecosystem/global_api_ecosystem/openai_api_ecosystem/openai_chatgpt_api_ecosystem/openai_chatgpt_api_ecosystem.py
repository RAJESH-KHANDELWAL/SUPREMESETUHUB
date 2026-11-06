"""OPENAI CHATGPT API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "chatgpt",
    "name": "OPENAI CHATGPT API ECOSYSTEM",
    "display_name": "ChatGPT",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "OpenAI's primary conversational product. Features such as chat, search, voice, file analysis, projects, custom GPTs and deep research are grouped here as product features.",
    "official_reference": "https://chatgpt.com/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
