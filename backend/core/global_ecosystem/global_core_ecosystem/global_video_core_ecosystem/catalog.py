"""Canonical GLOBAL VIDEO CORE ECOSYSTEM identity and curated provider inventory."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-VIDEO-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL VIDEO CORE ECOSYSTEM"
PARENT_ID = "GLOBAL-CORE-ECOSYSTEM"

PROVIDERS: list[dict[str, Any]] = [
    {"provider_id": "adobe", "name": "Adobe", "directory": "adobe_video_core_ecosystem", "domain_id": "VIDEO_EDITING_AND_POST_PRODUCTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/adobe_video_core_ecosystem"},
    {"provider_id": "aws", "name": "Amazon Web Services", "directory": "aws_video_core_ecosystem", "domain_id": "VIDEO_INFRASTRUCTURE_AND_PROCESSING", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/aws_video_core_ecosystem"},
    {"provider_id": "bangbros", "name": "BangBros", "directory": "bangbros_video_core_ecosystem", "domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/bangbros_video_core_ecosystem"},
    {"provider_id": "brazzers", "name": "Brazzers", "directory": "brazzers_video_core_ecosystem", "domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/brazzers_video_core_ecosystem"},
    {"provider_id": "clips4sale", "name": "Clips4Sale", "directory": "clips4sale_video_core_ecosystem", "domain_id": "CREATOR_AND_SUBSCRIPTION_PLATFORMS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/clips4sale_video_core_ecosystem"},
    {"provider_id": "evilangel", "name": "Evil Angel", "directory": "evilangel_video_core_ecosystem", "domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/evilangel_video_core_ecosystem"},
    {"provider_id": "fansly", "name": "Fansly", "directory": "fansly_video_core_ecosystem", "domain_id": "CREATOR_AND_SUBSCRIPTION_PLATFORMS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/fansly_video_core_ecosystem"},
    {"provider_id": "faphouse", "name": "Faphouse", "directory": "faphouse_video_core_ecosystem", "domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/faphouse_video_core_ecosystem"},
    {"provider_id": "google", "name": "Google", "directory": "google_video_core_ecosystem", "domain_id": "VIDEO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/google_video_core_ecosystem"},
    {"provider_id": "loyalfans", "name": "LoyalFans", "directory": "loyalfans_video_core_ecosystem", "domain_id": "CREATOR_AND_SUBSCRIPTION_PLATFORMS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/loyalfans_video_core_ecosystem"},
    {"provider_id": "manyvids", "name": "ManyVids", "directory": "manyvids_video_core_ecosystem", "domain_id": "CREATOR_AND_SUBSCRIPTION_PLATFORMS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/manyvids_video_core_ecosystem"},
    {"provider_id": "naughtyamerica", "name": "Naughty America", "directory": "naughtyamerica_video_core_ecosystem", "domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/naughtyamerica_video_core_ecosystem"},
    {"provider_id": "nvidia", "name": "NVIDIA", "directory": "nvidia_video_core_ecosystem", "domain_id": "VIDEO_INFRASTRUCTURE_AND_PROCESSING", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/nvidia_video_core_ecosystem"},
    {"provider_id": "onlyfans", "name": "OnlyFans", "directory": "onlyfans_video_core_ecosystem", "domain_id": "CREATOR_AND_SUBSCRIPTION_PLATFORMS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/onlyfans_video_core_ecosystem"},
    {"provider_id": "pornhub", "name": "Pornhub", "directory": "pornhub_video_core_ecosystem", "domain_id": "VIDEO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/pornhub_video_core_ecosystem"},
    {"provider_id": "realitykings", "name": "Reality Kings", "directory": "realitykings_video_core_ecosystem", "domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/realitykings_video_core_ecosystem"},
    {"provider_id": "xhamster", "name": "xHamster", "directory": "xhamster_video_core_ecosystem", "domain_id": "VIDEO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/xhamster_video_core_ecosystem"},
    {"provider_id": "xvideos", "name": "XVideos", "directory": "xvideos_video_core_ecosystem", "domain_id": "VIDEO_SHARING_AND_COMMUNITIES", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/xvideos_video_core_ecosystem"},
    {"provider_id": "zoom", "name": "Zoom", "directory": "zoom_video_core_ecosystem", "domain_id": "VIDEO_COMMUNICATION_AND_MEETINGS", "status": "CORE_CATALOG_ONLY", "enabled": True, "connected": False, "live_connection_verified": False, "core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem/zoom_video_core_ecosystem"}
]
CAPABILITIES = [
    "PROVIDER_IDENTITY_AND_REGISTRATION", "DOMAIN_CLASSIFICATION",
    "CAPABILITY_METADATA", "TENANT_SCOPED_DISCOVERY", "READINESS_METADATA",
    "DEPENDENCY_MAPPING", "RIGHTS_AND_CONSENT_METADATA", "PRIVACY_AND_SAFETY_POLICY",
]

def get_catalog() -> dict[str, Any]:
    return {
        "ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME,
        "category": "VIDEO", "parent_id": PARENT_ID,
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
