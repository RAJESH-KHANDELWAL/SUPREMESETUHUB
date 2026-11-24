"""Readiness report separating catalog status from real provider connectivity."""
from .catalog import COHERE_PRODUCTS
from .constants import PROVIDER_ID, STATUS_CATALOG_ONLY

def readiness_report() -> dict:
    return {
        "provider_id": PROVIDER_ID,
        "status": STATUS_CATALOG_ONLY,
        "live_connection_verified": False,
        "credential_configured": None,
        "credential_validated": False,
        "api_transport_registered": None,
        "ai_runtime_registered": None,
        "engine_registered": None,
        "database_persistence": None,
        "product_count": len(COHERE_PRODUCTS),
        "notes": [
            "This domain package provides catalog, validation and request planning only.",
            "The API key belongs in server-side secret storage and must not be embedded in request payloads.",
            "API, AI runtime, ENGINE and DATABASE are separate architecture layers.",
            "Mark connectivity verified only after authenticated provider requests and product-specific smoke tests succeed.",
        ],
    }
