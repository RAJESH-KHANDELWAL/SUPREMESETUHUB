"""Cloudflare Accounts API catalog metadata; not a live connector."""

CLOUDFLARE_ACCOUNTS_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "Accounts",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Cloudflare account listing and account-level settings.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/accounts/",
    "api_boundary": "/accounts",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
