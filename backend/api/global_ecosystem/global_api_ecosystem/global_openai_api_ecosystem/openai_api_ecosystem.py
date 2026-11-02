"""OpenAI provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

OPENAI_API_ECOSYSTEM = {
    "provider_id": "openai",
    "name": "OPENAI API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "AI models, inference, developer APIs and official platform tooling",
    "platforms_and_api_areas": [
        "API platform",
        "models",
        "Responses/Chat APIs",
        "embeddings",
        "tools and developer console"
    ],
    "related_ecosystems": ["AI", "DEVELOPER", "TOOLS"],
    "credential_source": "environment_or_managed_secret_store",
}
