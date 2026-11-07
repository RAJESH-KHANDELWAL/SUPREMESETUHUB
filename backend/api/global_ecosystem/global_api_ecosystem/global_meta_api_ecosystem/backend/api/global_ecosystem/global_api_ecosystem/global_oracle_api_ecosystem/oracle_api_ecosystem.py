"""Oracle provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

ORACLE_API_ECOSYSTEM = {
    "provider_id": "oracle",
    "name": "ORACLE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Cloud infrastructure, database and enterprise APIs",
    "platforms_and_api_areas": [
        "OCI",
        "Autonomous Database",
        "compute",
        "storage and identity APIs"
    ],
    "related_ecosystems": ["AI", "CLOUD", "DATABASE", "BUSINESS"],
    "credential_source": "environment_or_managed_secret_store",
}
