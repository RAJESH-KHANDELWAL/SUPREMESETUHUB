"""Metadata-only Behance photo Core package."""
from __future__ import annotations
from typing import Any
PROVIDER_ID = "behance"
PROVIDER_NAME = "Behance"
DOMAIN_ID = "CREATOR_AND_PHOTOGRAPHY_BUSINESS"
def describe() -> dict[str, Any]:
    return {"provider_id": PROVIDER_ID, "provider_name": PROVIDER_NAME, "category": "PHOTO", "domain_id": DOMAIN_ID, "status": "CORE_CATALOG_ONLY", "connected": False, "live_connection_verified": False, "api_transport_in_core": False, "storage_in_core": False}
