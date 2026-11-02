"""IBM provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

IBM_API_ECOSYSTEM = {
    "provider_id": "ibm",
    "name": "IBM API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Enterprise cloud, AI and data APIs",
    "platforms_and_api_areas": [
        "IBM Cloud",
        "watsonx and supported enterprise APIs"
    ],
    "related_ecosystems": ["AI", "CLOUD", "DATABASE", "BUSINESS"],
    "credential_source": "environment_or_managed_secret_store",
}
