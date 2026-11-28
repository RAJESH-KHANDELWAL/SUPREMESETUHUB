"""Adobe API ecosystem catalog metadata and adapter status."""
from __future__ import annotations

ADOBE_API_ECOSYSTEM = {
    "provider_id": "adobe",
    "name": "ADOBE API ECOSYSTEM",
    "status": "FAMILY_ADAPTER_SCAFFOLDS_AVAILABLE_NOT_CONNECTED",
    "live_connection_verified": False,
    "family_count": 8,
    "shared_transport": "shared",
    "scope": "Documented Adobe developer APIs only, subject to product entitlement, OAuth scopes and organization permissions.",
    "credential_source": "server_side_secret_store",
    "children": [
        {"id": "pdf_services", "name": "PDF Services API", "folder": "adobe_pdf_services_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "acrobat_sign", "name": "Acrobat Sign API", "folder": "adobe_acrobat_sign_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "firefly", "name": "Firefly Services API", "folder": "adobe_firefly_services_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "creative_cloud", "name": "Creative Cloud and Assets APIs", "folder": "adobe_creative_cloud_assets_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "experience_platform", "name": "Experience Platform APIs", "folder": "adobe_experience_platform_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "commerce", "name": "Adobe Commerce APIs", "folder": "adobe_commerce_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "video", "name": "Video and Frame.io APIs", "folder": "adobe_video_frameio_api_ecosystem", "status": "ADAPTER_SCAFFOLD"},
        {"id": "oauth_identity", "name": "OAuth and Developer Console", "folder": "adobe_oauth_identity_ecosystem", "status": "ADAPTER_SCAFFOLD"},
    ],
}


def list_adobe_api_ecosystems() -> list[dict[str, str]]:
    """Return child catalog entries without claiming live API availability."""
    return [dict(item) for item in ADOBE_API_ECOSYSTEM["children"]]


PROVIDER_API_ECOSYSTEM = ADOBE_API_ECOSYSTEM
__all__ = ["ADOBE_API_ECOSYSTEM", "PROVIDER_API_ECOSYSTEM", "list_adobe_api_ecosystems"]
