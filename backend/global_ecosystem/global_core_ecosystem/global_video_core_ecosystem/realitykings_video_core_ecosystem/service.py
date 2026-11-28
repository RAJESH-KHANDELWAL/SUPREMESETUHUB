"""Metadata-only Reality Kings video Core package."""
from __future__ import annotations
from typing import Any
PROVIDER_ID = "realitykings"
PROVIDER_NAME = "Reality Kings"
DOMAIN_ID = "VIDEO_MARKETPLACES_AND_DISTRIBUTION"
def describe() -> dict[str, Any]:
    return {"provider_id": PROVIDER_ID, "provider_name": PROVIDER_NAME, "category": "VIDEO", "domain_id": DOMAIN_ID, "status": "CORE_CATALOG_ONLY", "connected": False, "live_connection_verified": False, "api_transport_in_core": False, "storage_in_core": False}
