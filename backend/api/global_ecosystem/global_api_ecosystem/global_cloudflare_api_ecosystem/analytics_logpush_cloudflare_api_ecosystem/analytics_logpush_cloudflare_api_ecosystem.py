"""Cloudflare Analytics and Logpush API catalog metadata; not a live connector."""

CLOUDFLARE_ANALYTICS_LOGPUSH_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "Analytics and Logpush",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Analytics and supported Logpush configuration and observability resources.",
    "official_documentation": "https://developers.cloudflare.com/api/",
    "api_boundary": "Product-specific analytics and Logpush endpoints in official API reference",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
