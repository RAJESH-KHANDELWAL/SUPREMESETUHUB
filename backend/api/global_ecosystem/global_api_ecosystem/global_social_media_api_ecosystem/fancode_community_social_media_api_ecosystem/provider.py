"""FanCode community provider-family catalog; metadata only, not a live connector."""
SOCIAL_MEDIA_PROVIDER = {
    "provider_id": "fancode_community", "name": "FanCode community",
    "region": "india", "category": "sports_community",
    "api_access": "verify", "status": "CATALOG_ONLY",
    "live_connection_verified": False, "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem",
    "documentation_review_required": True,
}
def get_provider_catalog():
    return dict(SOCIAL_MEDIA_PROVIDER)
__all__ = ["SOCIAL_MEDIA_PROVIDER", "get_provider_catalog"]
