"""Metadata registry for GLOBAL CLOUD ECOSYSTEM; it does not make network connections."""

PROVIDERS = [
    {"provider_id": "google_cloud", "name": "Google Cloud", "capabilities": ["cloud-compute-and-data-services"], "status": "not_configured"},
    {"provider_id": "aws_cloud", "name": "Amazon Web Services", "capabilities": ["cloud-compute-and-data-services"], "status": "not_configured"},
    {"provider_id": "microsoft_azure", "name": "Microsoft Azure", "capabilities": ["cloud-compute-and-data-services"], "status": "not_configured"},
    {"provider_id": "cloudflare_cloud", "name": "Cloudflare", "capabilities": ["edge-network-and-cloud-services"], "status": "not_configured"},
]


def list_providers() -> list[dict[str, object]]:
    """Return a defensive copy of provider metadata."""
    return [dict(provider, capabilities=list(provider["capabilities"])) for provider in PROVIDERS]


def get_provider(provider_id: str) -> dict[str, object]:
    """Get provider metadata by ID, without connecting to the provider."""
    normalized = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == normalized:
            return dict(provider, capabilities=list(provider["capabilities"]))
    raise KeyError(f"Unknown CLOUD provider: {provider_id!r}")
