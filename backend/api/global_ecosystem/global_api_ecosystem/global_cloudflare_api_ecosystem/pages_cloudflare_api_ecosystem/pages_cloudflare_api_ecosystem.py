"""Cloudflare Pages API catalog metadata; not a live connector."""

CLOUDFLARE_PAGES_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "Pages",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Cloudflare Pages projects and deployments.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/pages/",
    "api_boundary": "/accounts/{account_id}/pages/projects",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
