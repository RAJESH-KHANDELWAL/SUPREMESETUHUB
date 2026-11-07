"""IBM provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

IBM_API_ECOSYSTEM = {
    "provider_id": "ibm",
    "name": "IBM API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Enterprise cloud, AI, data, security and infrastructure APIs",
    "platforms_and_api_areas": [
        "IBM Cloud",
        "watsonx and supported enterprise AI APIs",
        "IBM Db2 and data-platform APIs",
        "IBM security and identity services",
        "IBM Cloud infrastructure and VPS-related services"
    ],
    "related_ecosystems": ["AI", "CLOUD", "DATABASE", "BUSINESS", "SECURITY", "VPS"],
    "credential_source": "environment_or_managed_secret_store",
}
