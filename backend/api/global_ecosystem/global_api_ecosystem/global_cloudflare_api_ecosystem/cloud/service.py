"""Catalog-only Cloudflare CLOUD metadata; no API calls are made."""
from __future__ import annotations

PROVIDER_ID = "cloudflare"
FAMILY = "CLOUD"
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
CAPABILITIES = (
    {"id": "cloud_1", "name": "Cloudflare dashboard and account APIs", "status": "CATALOG_ONLY"},
    {"id": "cloud_2", "name": "Workers", "status": "CATALOG_ONLY"},
    {"id": "cloud_3", "name": "R2", "status": "CATALOG_ONLY"},
    {"id": "cloud_4", "name": "Zones and edge platform", "status": "CATALOG_ONLY"},
    {"id": "cloud_5", "name": "SSL/TLS and network services", "status": "CATALOG_ONLY"},
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
