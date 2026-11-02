"""Metadata registry for GLOBAL STORAGE ECOSYSTEM; it does not make network connections."""

PROVIDERS = [
    {"provider_id": "google_storage", "name": "Google Cloud Storage", "capabilities": ["google-cloud-storage"], "status": "not_configured"},
    {"provider_id": "aws_storage", "name": "Amazon S3", "capabilities": ["object-storage"], "status": "not_configured"},
    {"provider_id": "microsoft_storage", "name": "Azure Blob Storage", "capabilities": ["object-storage"], "status": "not_configured"},
    {"provider_id": "proton_storage", "name": "Proton Drive", "capabilities": ["privacy-aware-file-storage"], "status": "not_configured"},
    {"provider_id": "mega_storage", "name": "MEGA Storage", "capabilities": ["authorized-file-sync"], "status": "not_configured"},
    {"provider_id": "hostinger_storage", "name": "Hostinger Storage", "capabilities": ["hosting-file-storage"], "status": "not_configured"},
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
    raise KeyError(f"Unknown STORAGE provider: {provider_id!r}")
