"""Cloudflare SSL/TLS API catalog metadata; not a live connector."""

CLOUDFLARE_SSL_TLS_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "SSL/TLS",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "SSL/TLS settings and certificate-related API resources where available.",
    "official_documentation": "https://developers.cloudflare.com/api/",
    "api_boundary": "Product-specific SSL/TLS endpoints in official API reference",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
