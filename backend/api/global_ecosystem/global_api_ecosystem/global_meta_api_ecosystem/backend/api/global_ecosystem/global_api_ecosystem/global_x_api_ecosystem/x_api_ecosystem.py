"""X provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

X_API_ECOSYSTEM = {
    "provider_id": "x",
    "name": "X API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "X developer platform and social APIs",
    "platforms_and_api_areas": [
        "X API",
        "account/app developer portal and approved post/search endpoints"
    ],
    "related_ecosystems": ["SOCIAL_MEDIA", "DEVELOPER"],
    "credential_source": "environment_or_managed_secret_store",
}
