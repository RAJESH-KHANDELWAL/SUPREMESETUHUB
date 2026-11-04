"""Cloudflare Zones API catalog metadata; not a live connector."""

CLOUDFLARE_ZONES_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "Zones",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Zone listing, details, settings and lifecycle operations where authorized.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/zones/",
    "api_boundary": "/zones",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
