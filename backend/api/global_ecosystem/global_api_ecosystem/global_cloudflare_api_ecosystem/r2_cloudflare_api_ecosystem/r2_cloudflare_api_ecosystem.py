"""Cloudflare R2 Object Storage API catalog metadata; not a live connector."""

CLOUDFLARE_R2_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "R2 Object Storage",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "R2 bucket management through Cloudflare REST API; object data may use S3-compatible API.",
    "official_documentation": "https://developers.cloudflare.com/r2/api/",
    "api_boundary": "Cloudflare REST API + R2 S3-compatible endpoint",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
