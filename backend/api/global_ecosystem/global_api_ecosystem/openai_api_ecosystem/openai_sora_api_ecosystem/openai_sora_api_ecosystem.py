"""OPENAI SORA (RETIRED REFERENCE) API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "sora",
    "name": "OPENAI SORA (RETIRED REFERENCE) API ECOSYSTEM",
    "display_name": "Sora (retired reference)",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_sora_api_ecosystem",
    "status": "retired_reference_only",
    "live_connection_verified": False,
    "description": "Historical reference only. OpenAI discontinued the Sora web/app experience and Sora API in 2026; do not expose this as an active service or connection option.",
    "official_reference": "https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; no external API call is made."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
