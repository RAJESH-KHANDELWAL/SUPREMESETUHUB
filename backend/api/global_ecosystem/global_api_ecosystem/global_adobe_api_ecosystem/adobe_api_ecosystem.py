"""Adobe provider-owned API ecosystem catalog.

Catalog metadata only. OAuth credentials and API requests belong in the
shared backend integration layer.
"""
from __future__ import annotations

ADOBE_API_ECOSYSTEM = {
    "provider_id": "adobe",
    "name": "GLOBAL ADOBE API ECOSYSTEM",
    "status": "CATALOG_AND_READINESS_ADAPTER",
    "live_connection_verified": False,
    "families": ["CREATIVE", "DOCUMENTS", "PDF", "ASSETS", "EXPERIENCE", "VIDEO", "AI"],
    "scope": "Adobe developer APIs and product integrations subject to product availability, OAuth scopes, account entitlement and developer credentials.",
    "credential_source": "environment_or_managed_secret_store",
    "children": [
        {"id": "pdf_services", "name": "PDF Services API", "folder": "adobe_pdf_services_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "acrobat_sign", "name": "Acrobat Sign API", "folder": "adobe_acrobat_sign_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "firefly", "name": "Firefly Services API", "folder": "adobe_firefly_services_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "creative_cloud", "name": "Creative Cloud and Assets APIs", "folder": "adobe_creative_cloud_assets_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "experience_platform", "name": "Experience Platform APIs", "folder": "adobe_experience_platform_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "commerce", "name": "Adobe Commerce APIs", "folder": "adobe_commerce_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "video", "name": "Video and Frame.io APIs", "folder": "adobe_video_frameio_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "oauth_identity", "name": "Adobe OAuth and Developer Console", "folder": "adobe_oauth_identity_ecosystem", "status": "CATALOG_SCAFFOLD"},
    ],
}


def list_adobe_api_ecosystems() -> list[dict[str, str]]:
    """Return catalog entries without implying live API availability."""
    return [dict(item) for item in ADOBE_API_ECOSYSTEM["children"]]


# Backward-compatible name used by the original catalog file.
PROVIDER_API_ECOSYSTEM = ADOBE_API_ECOSYSTEM

__all__ = [
    "ADOBE_API_ECOSYSTEM",
    "PROVIDER_API_ECOSYSTEM",
    "list_adobe_api_ecosystems",
]
