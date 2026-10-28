"""NSFWInfra provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

NSFWINFRA_API_ECOSYSTEM = {
    "provider_id": "nsfwinfra",
    "name": "NSFWINFRA API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Provider-specific AI/image services as configured in this project",
    "platforms_and_api_areas": [
        "Only products and endpoints explicitly documented by the provider and enabled for the account"
    ],
    "related_ecosystems": ["AI", "IMAGE"],
    "credential_source": "environment_or_managed_secret_store",
}
