"""Canonical Global Social Media Core registry."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .platform_catalog import PLATFORM_DEFINITIONS

SOCIAL_MEDIA_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-CORE-ECOSYSTEM",
    "name": "GLOBAL SOCIAL MEDIA CORE ECOSYSTEM",
    "ecosystem_type": "DOMAIN_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "provider_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem",
    "capabilities": [
        "SOCIAL_PLATFORM_REGISTRY", "PLATFORM_FAMILY_DISCOVERY",
        "SOCIAL_DOMAIN_CLASSIFICATION", "TENANT_SCOPED_CAPABILITY_METADATA",
        "PUBLISHING_POLICY_BOUNDARY", "COMMUNITY_POLICY_BOUNDARY",
        "LIFECYCLE_AND_READINESS_METADATA", "AGE_RESTRICTION_POLICY_METADATA",
    ],
    "children": [
        {
            "ecosystem_id": f"SOCIAL-{item['id'].upper().replace('_','-')}-CORE-ECOSYSTEM",
            "name": f"{item['name'].upper()} CORE ECOSYSTEM",
            "ecosystem_type": "PLATFORM_FAMILY_CORE" if item["package_type"] == "PLATFORM_FAMILY" else "PLATFORM_CORE",
            "parent_id": "GLOBAL-SOCIAL-MEDIA-CORE-ECOSYSTEM",
            "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/{item['core_folder']}",
            "api_catalog_ref": f"backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem/{item['id']}_social_media_api_ecosystem",
            "category": item["category"],
            "status": "CORE_CATALOG_ONLY",
            "connected": False,
            "age_restricted": item["category"].startswith("adult_") or item["id"] == "adult_community_platforms",
        }
        for item in PLATFORM_DEFINITIONS
    ],
}

def get_social_media_core_catalog() -> dict[str, Any]:
    return deepcopy(SOCIAL_MEDIA_CORE_ECOSYSTEM)
