"""Canonical GLOBAL PHOTO CORE ECOSYSTEM identity and curated provider inventory."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-PHOTO-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL PHOTO CORE ECOSYSTEM"
PARENT_ID = "GLOBAL-CORE-ECOSYSTEM"

PROVIDERS: list[dict[str, Any]] = [

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
