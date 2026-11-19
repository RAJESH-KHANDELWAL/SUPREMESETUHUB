"""OPENAI CODEX API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "codex",
    "name": "OPENAI CODEX API ECOSYSTEM",
    "display_name": "Codex",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_codex_api_ecosystem",
    "status": "active_catalog",
    "live_connection_verified": False,
    "description": "OpenAI's coding agent across supported app, CLI, IDE and cloud workflows. Codex SDK and app-server surfaces are developer integration options.",
    "official_reference": "https://developers.openai.com/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
