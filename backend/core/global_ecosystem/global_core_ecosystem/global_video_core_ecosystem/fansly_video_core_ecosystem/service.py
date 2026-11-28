"""Metadata-only Fansly video Core package."""
from __future__ import annotations
from typing import Any
PROVIDER_ID = "fansly"
PROVIDER_NAME = "Fansly"
DOMAIN_ID = "CREATOR_AND_SUBSCRIPTION_PLATFORMS"
def describe() -> dict[str, Any]:
    return {"provider_id": PROVIDER_ID, "provider_name": PROVIDER_NAME, "category": "VIDEO", "domain_id": DOMAIN_ID, "status": "CORE_CATALOG_ONLY", "connected": False, "live_connection_verified": False, "api_transport_in_core": False, "storage_in_core": False}
