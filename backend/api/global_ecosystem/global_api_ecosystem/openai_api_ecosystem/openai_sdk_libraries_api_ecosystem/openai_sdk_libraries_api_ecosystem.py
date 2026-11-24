"""OPENAI OPENAI SDK LIBRARIES API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "sdk_libraries",
    "name": "OPENAI OPENAI SDK LIBRARIES API ECOSYSTEM",
    "display_name": "OpenAI SDK Libraries",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_sdk_libraries_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "Official API client libraries and developer SDKs for supported languages. Language-specific clients belong beneath this service.",
    "official_reference": "https://developers.openai.com/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
