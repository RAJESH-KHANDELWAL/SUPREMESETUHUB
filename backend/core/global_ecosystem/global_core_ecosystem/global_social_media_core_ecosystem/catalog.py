"""Canonical Global Social Media Core catalog."""
from copy import deepcopy
from typing import Any
from .product_catalog import get_social_media_product_index
SOCIAL_MEDIA_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-CORE-ECOSYSTEM",
    "name": "GLOBAL SOCIAL MEDIA CORE ECOSYSTEM",
    "provider": "multi-platform",
    "ecosystem_type": "CROSS_PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED_CORE_CATALOG_ONLY",
    "enabled": true,
    "capabilities": [
        "SOCIAL_PLATFORM_REGISTRY",
        "PLATFORM_DISCOVERY",
        "DOMAIN_CLASSIFICATION",
        "TENANT_SCOPED_CONNECTION_METADATA",
        "CAPABILITY_METADATA",
        "CONTENT_LIFECYCLE_METADATA",
        "MODERATION_AND_SAFETY_POLICY_METADATA",
        "AGE_ASSURANCE_BOUNDARY",
        "CREATOR_ECONOMY_METADATA",
        "FEDERATION_INTEROPERABILITY_METADATA"
    ],
    "platform_count": 113,
    "domain_count": 14,
    "platform_index_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/product_ecosystem_index.json",
    "api_transport_in_core": false,
    "live_connections_verified": false,
    "api_calls_performed": 0,
    "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"
}
def get_social_media_core_catalog() -> dict[str, Any]:
    result=deepcopy(SOCIAL_MEDIA_CORE_ECOSYSTEM)
    result["platforms"]=get_social_media_product_index()["platform_ecosystems"]
    return result
__all__=["SOCIAL_MEDIA_CORE_ECOSYSTEM","get_social_media_core_catalog"]
