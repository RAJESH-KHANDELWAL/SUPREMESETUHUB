"""Nextdoor provider-family catalog; metadata only, not a live connector."""
from __future__ import annotations

SOCIAL_MEDIA_PROVIDER = {
    "provider_id": "nextdoor",
    "name": "Nextdoor",
    "region": "global",
    "category": "neighborhood_community",
    "api_access": "restricted_or_partner",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem",
    "documentation_review_required": True,
}

def get_provider_catalog() -> dict[str, object]:
    """Return this provider's static discovery metadata."""
    return dict(SOCIAL_MEDIA_PROVIDER)

__all__ = ["SOCIAL_MEDIA_PROVIDER", "get_provider_catalog"]
