"""Cloudflare provider-owned API ecosystem metadata.

Catalog metadata only; this module performs no authentication or network requests.
"""
from __future__ import annotations

CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "name": "CLOUDFLARE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "purpose": "DNS, edge networking, security and developer platform APIs",
    "platforms_and_api_areas": [
        "Cloudflare dashboard",
        "DNS",
        "zones",
        "Workers",
        "R2",
        "SSL/TLS and security APIs"
    ],
    "related_ecosystems": ["CLOUD", "DOMAIN", "DNS", "SECURITY", "WEB"],
    "credential_source": "environment_or_managed_secret_store",
}
