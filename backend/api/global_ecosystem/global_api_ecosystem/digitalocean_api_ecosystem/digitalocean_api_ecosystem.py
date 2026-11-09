"""DigitalOcean provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

DIGITALOCEAN_API_ECOSYSTEM = {
    "provider_id": "digitalocean",
    "name": "DIGITALOCEAN API ECOSYSTEM",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "purpose": "Cloud compute, managed services and hosting APIs",
    "platforms_and_api_areas": [
        "Droplets",
        "App Platform",
        "managed databases",
        "Spaces and DNS APIs"
    ],
    "related_ecosystems": ["CLOUD", "HOSTING", "SERVER", "STORAGE", "VPS"],
    "provider_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem",
    "credential_source": "environment_or_managed_secret_store",
}
