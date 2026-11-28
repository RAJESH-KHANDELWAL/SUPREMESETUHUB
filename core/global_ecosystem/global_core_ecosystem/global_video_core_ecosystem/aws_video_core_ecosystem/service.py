"""Metadata-only Amazon Web Services video Core package."""
from __future__ import annotations
from typing import Any
PROVIDER_ID = "aws"
PROVIDER_NAME = "Amazon Web Services"
DOMAIN_ID = "VIDEO_INFRASTRUCTURE_AND_PROCESSING"
def describe() -> dict[str, Any]:
    return {"provider_id": PROVIDER_ID, "provider_name": PROVIDER_NAME, "category": "VIDEO", "domain_id": DOMAIN_ID, "status": "CORE_CATALOG_ONLY", "connected": False, "live_connection_verified": False, "api_transport_in_core": False, "storage_in_core": False}
