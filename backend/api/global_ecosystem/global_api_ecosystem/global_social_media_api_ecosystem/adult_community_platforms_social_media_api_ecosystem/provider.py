"""Other lawful age-restricted creator and adult communities provider-family catalog; metadata only, not a live connector."""
SOCIAL_MEDIA_PROVIDER = {
    "provider_id": "adult_community_platforms", "name": "Other lawful age-restricted creator and adult communities",
    "region": "global", "category": "adult_social",
    "api_access": "review_each_provider", "status": "CATALOG_ONLY",
    "live_connection_verified": False, "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem",
    "documentation_review_required": True,
}
def get_provider_catalog():
    return dict(SOCIAL_MEDIA_PROVIDER)
__all__ = ["SOCIAL_MEDIA_PROVIDER", "get_provider_catalog"]
