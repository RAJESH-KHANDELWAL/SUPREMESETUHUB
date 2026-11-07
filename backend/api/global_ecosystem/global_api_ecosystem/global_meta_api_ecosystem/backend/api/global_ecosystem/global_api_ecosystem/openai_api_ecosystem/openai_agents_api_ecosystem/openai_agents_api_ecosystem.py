"""OPENAI AGENTS API API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "agents_api",
    "name": "OPENAI AGENTS API API ECOSYSTEM",
    "display_name": "Agents API",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_agents_api_ecosystem",
    "status": "public_beta_catalog",
    "live_connection_verified": False,
    "description": "Managed agent runtime/API using OpenAI's Codex harness, durable sessions, orchestration and supported execution environments.",
    "official_reference": "https://developers.openai.com/api/docs/guides/agents-api/overview",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
