"""Readiness report that distinguishes catalog presence from live connectivity."""
from .catalog import ATLASSIAN_PRODUCTS
from .constants import PROVIDER_ID, STATUS_CATALOG_ONLY

def readiness_report() -> dict:
    return {
        "provider_id": PROVIDER_ID,
        "status": STATUS_CATALOG_ONLY,
        "live_connection_verified": False,
        "credential_configured": None,
        "oauth_token_verified": False,
        "api_transport_registered": None,
        "engine_registered": None,
        "database_persistence": None,
        "product_count": len(ATLASSIAN_PRODUCTS),
        "notes": [
            "This package provides domain catalog, validation and request planning only.",
            "Atlassian product access is tenant-, entitlement-, scope- and permission-dependent.",
            "Configuration presence is not proof of successful authentication or API connectivity.",
            "Report CONNECTED only after product-specific token and API smoke tests succeed.",
        ],
    }
