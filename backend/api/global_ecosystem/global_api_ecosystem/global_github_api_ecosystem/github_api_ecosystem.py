"""GitHub provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

GITHUB_API_ECOSYSTEM = {
    "provider_id": "github",
    "name": "GITHUB API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Source control, repository, CI/CD and developer platform APIs",
    "platforms_and_api_areas": [
        "GitHub REST/Graph APIs",
        "Actions",
        "Apps",
        "webhooks and repository operations"
    ],
    "related_ecosystems": ["DEVELOPER", "SOFTWARE", "TOOLS"],
    "credential_source": "environment_or_managed_secret_store",
}
