"""OPENAI DOTS API ECOSYSTEM child catalog metadata; not a live connector."""

OPENAI_SERVICE_ECOSYSTEM = {
    "provider_id": "openai",
    "service_id": "dots",
    "name": "OPENAI DOTS API ECOSYSTEM",
    "display_name": "Dots",
    "folder": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_dots_api_ecosystem",
    "status": "availability_dependent_catalog",
    "live_connection_verified": False,
    "description": "OpenAI personal agent product for ongoing work. Setup, connected apps, access and availability must be verified against current official documentation.",
    "official_reference": "https://openai.com/",
    "adapter_implemented": False,
}


def get_openai_service_ecosystem() -> dict[str, object]:
    """Return safe catalog metadata; this function does not call external APIs."""
    return dict(OPENAI_SERVICE_ECOSYSTEM)
