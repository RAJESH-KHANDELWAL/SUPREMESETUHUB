"""Compatibility registry backed by the canonical CLOUD provider catalog."""
from __future__ import annotations
from .catalog import CLOUD_PROVIDERS

PROVIDERS = [
    {
        "provider_id": item["provider_id"],
        "name": item["name"],
        "capabilities": list(item["capabilities"]),
        "status": item["status"],
    }
    for item in CLOUD_PROVIDERS
]

def list_providers() -> list[dict[str, object]]:
    """Return a defensive copy of provider metadata."""
    return [
        {**provider, "capabilities": list(provider["capabilities"])}
        for provider in PROVIDERS
    ]

def get_provider(provider_id: str) -> dict[str, object]:
    """Look up provider metadata without creating a cloud connection."""
    normalized = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == normalized:
            return {**provider, "capabilities": list(provider["capabilities"])}
    raise KeyError(f"Unknown CLOUD provider: {provider_id!r}")
