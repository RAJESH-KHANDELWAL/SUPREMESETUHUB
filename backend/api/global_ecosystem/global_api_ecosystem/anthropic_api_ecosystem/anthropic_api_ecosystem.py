"""Anthropic provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

ANTHROPIC_API_ECOSYSTEM = {
    "provider_id": "anthropic",
    "name": "ANTHROPIC API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Claude models and developer APIs",
    "platforms_and_api_areas": [
        "Claude API",
        "Messages API",
        "tool use and supported model capabilities"
    ],
    "related_ecosystems": ["AI", "DEVELOPER"],
    "credential_source": "environment_or_managed_secret_store",
}
