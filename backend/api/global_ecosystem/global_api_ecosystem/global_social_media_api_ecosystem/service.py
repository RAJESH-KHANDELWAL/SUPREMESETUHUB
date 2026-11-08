"""Service layer for the global social media provider directory."""
from __future__ import annotations

from .social_media_api_ecosystem import PROVIDERS, get_social_media_api_ecosystem, list_social_media_providers

def get_provider_directory(region: str | None = None, category: str | None = None) -> dict[str, object]:
    """Return provider metadata filtered by region/category."""
    providers = list_social_media_providers(region=region, category=category)
    return {
        "success": True,
        "provider_count": len(providers),
        "providers": providers,
        "live_connections_verified": False,
    }

def get_provider_detail(provider_id: str) -> dict[str, object] | None:
    """Return one provider record by stable provider ID."""
    key = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider["id"] == key:
            return dict(provider)
    return None

def get_ecosystem_overview() -> dict[str, object]:
    """Return ecosystem-level metadata and coverage summary."""
    data = get_social_media_api_ecosystem()
    return {
        "provider_id": data["provider_id"],
        "name": data["name"],
        "regions": data["regions"],
        "provider_count": data["provider_count"],
        "categories": data["categories"],
        "live_connections_verified": False,
    }

__all__ = ["get_provider_directory", "get_provider_detail", "get_ecosystem_overview"]
