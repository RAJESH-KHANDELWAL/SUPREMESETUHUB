"""DigitalOcean provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

DIGITALOCEAN_API_ECOSYSTEM = {
    "provider_id": "digitalocean",
    "name": "DIGITALOCEAN API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "Cloud compute, managed services and hosting APIs",
    "platforms_and_api_areas": [
        "Droplets",
        "App Platform",
        "managed databases",
        "Spaces and DNS APIs"
    ],
    "related_ecosystems": ["CLOUD", "HOSTING", "SERVER", "STORAGE"],
    "credential_source": "environment_or_managed_secret_store",
}
