"""Canonical GLOBAL PHOTO CORE ECOSYSTEM identity and curated provider inventory."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-PHOTO-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL PHOTO CORE ECOSYSTEM"
PARENT_ID = "GLOBAL-CORE-ECOSYSTEM"

PROVIDERS: list[dict[str, Any]] = [
    {"provider_id": "adobe", "name": "Adobe", "directory": "adobe_photo_core_ecosystem", "domain_id": "PHOTO_EDITING_AND_RETOUCHING", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/adobe_photo_core_ecosystem"},
    {"provider_id": "apple", "name": "Apple", "directory": "apple_photo_core_ecosystem", "domain_id": "PHOTO_STORAGE_AND_ASSET_MANAGEMENT", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/apple_photo_core_ecosystem"},
    {"provider_id": "google", "name": "Google", "directory": "google_photo_core_ecosystem", "domain_id": "PHOTO_STORAGE_AND_ASSET_MANAGEMENT", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/google_photo_core_ecosystem"},
    {"provider_id": "flickr", "name": "Flickr", "directory": "flickr_photo_core_ecosystem", "domain_id": "PHOTO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/flickr_photo_core_ecosystem"},
    {"provider_id": "instagram", "name": "Instagram", "directory": "instagram_photo_core_ecosystem", "domain_id": "PHOTO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/instagram_photo_core_ecosystem"},
    {"provider_id": "pinterest", "name": "Pinterest", "directory": "pinterest_photo_core_ecosystem", "domain_id": "PHOTO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/pinterest_photo_core_ecosystem"},
    {"provider_id": "behance", "name": "Behance", "directory": "behance_photo_core_ecosystem", "domain_id": "CREATOR_AND_PHOTOGRAPHY_BUSINESS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/behance_photo_core_ecosystem"},
    {"provider_id": "deviantart", "name": "DeviantArt", "directory": "deviantart_photo_core_ecosystem", "domain_id": "CREATOR_AND_PHOTOGRAPHY_BUSINESS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/deviantart_photo_core_ecosystem"},
    {"provider_id": "artstation", "name": "ArtStation", "directory": "artstation_photo_core_ecosystem", "domain_id": "CREATOR_AND_PHOTOGRAPHY_BUSINESS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/artstation_photo_core_ecosystem"},
    {"provider_id": "pixelfed", "name": "Pixelfed", "directory": "pixelfed_photo_core_ecosystem", "domain_id": "PHOTO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/pixelfed_photo_core_ecosystem"}
]
CAPABILITIES = [
    "PROVIDER_IDENTITY_AND_REGISTRATION", "DOMAIN_CLASSIFICATION",
    "CAPABILITY_METADATA", "TENANT_SCOPED_DISCOVERY", "READINESS_METADATA",
    "DEPENDENCY_MAPPING", "RIGHTS_AND_CONSENT_METADATA", "PRIVACY_AND_SAFETY_POLICY",
]

def get_catalog() -> dict[str, Any]:
    return {
        "ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME,
        "category": "PHOTO", "parent_id": PARENT_ID,
        "status": "FOUNDATION_READY", "enabled": True,
        "provider_count": len(PROVIDERS), "providers": deepcopy(PROVIDERS),
        "capabilities": list(CAPABILITIES),
        "api_transport_in_core": False, "storage_in_core": False,
        "live_connection_verified": False,
    }

def get_provider(provider_id: str) -> dict[str, Any] | None:
    needle = provider_id.strip().casefold()
    if not needle: return None
    item = next((p for p in PROVIDERS if p["provider_id"].casefold() == needle or p["name"].casefold() == needle), None)
    return deepcopy(item) if item else None
