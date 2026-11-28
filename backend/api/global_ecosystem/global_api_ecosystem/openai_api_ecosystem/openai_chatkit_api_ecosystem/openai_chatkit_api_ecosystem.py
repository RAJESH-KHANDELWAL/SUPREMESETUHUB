"""OPENAI CHATKIT API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "chatkit",
    "name": "OPENAI CHATKIT API ECOSYSTEM",
    "display_name": "ChatKit",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatkit_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Developer toolkit for embedding a chat experience into an application using supported OpenAI platform components.",
    "official_reference": "https://developers.openai.com/api/docs/guides/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
