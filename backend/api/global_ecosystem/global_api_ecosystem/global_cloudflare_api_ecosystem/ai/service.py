"""Catalog-only Cloudflare AI metadata; no API calls are made."""
from __future__ import annotations

PROVIDER_ID = "cloudflare"
FAMILY = "AI"
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
CAPABILITIES = (
    {"id": "ai_1", "name": "Workers AI", "status": "CATALOG_ONLY"},
    {"id": "ai_2", "name": "AI Gateway", "status": "CATALOG_ONLY"},
    {"id": "ai_3", "name": "AI-related Workers integrations", "status": "CATALOG_ONLY"},
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
