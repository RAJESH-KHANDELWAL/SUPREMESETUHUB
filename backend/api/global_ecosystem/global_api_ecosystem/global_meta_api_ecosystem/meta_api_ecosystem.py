"""Meta provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

META_API_ECOSYSTEM = {
    "provider_id": "meta",
    "name": "META API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Social, messaging, identity and AI APIs",
    "platforms_and_api_areas": [
        "Meta for Developers",
        "Graph API",
        "WhatsApp Business Platform",
        "Instagram/Facebook APIs where approved"
    ],
    "related_ecosystems": ["AI", "COMMUNICATION", "SOCIAL_MEDIA"],
    "credential_source": "environment_or_managed_secret_store",
}
