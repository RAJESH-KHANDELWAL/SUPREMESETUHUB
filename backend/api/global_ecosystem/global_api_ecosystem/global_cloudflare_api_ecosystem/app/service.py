"""Catalog-only Cloudflare APP metadata; no API calls are made."""
from __future__ import annotations

PROVIDER_ID = "cloudflare"
FAMILY = "APP"
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
CAPABILITIES = (
    {"id": "app_1", "name": "Account/application management", "status": "CATALOG_ONLY"},
    {"id": "app_2", "name": "Workers", "status": "CATALOG_ONLY"},
    {"id": "app_3", "name": "Pages", "status": "CATALOG_ONLY"},
    {"id": "app_4", "name": "Application configuration", "status": "CATALOG_ONLY"},
)

def get_status() -> dict[str, object]:
    """Return scaffold status without implying live connectivity."""
    return {
        "provider_id": PROVIDER_ID,
        "family": FAMILY,
        "implementation_status": IMPLEMENTATION_STATUS,
        "live_connection_verified": False,
    }

def get_capabilities() -> list[dict[str, str]]:
    """Return catalogued capabilities for this family."""
    return [dict(item) for item in CAPABILITIES]
