"""Cloudflare Workers API catalog metadata; not a live connector."""

CLOUDFLARE_WORKERS_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "Workers",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Workers scripts, deployments, routes and related developer platform resources.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/workers/",
    "api_boundary": "/accounts/{account_id}/workers/scripts",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
