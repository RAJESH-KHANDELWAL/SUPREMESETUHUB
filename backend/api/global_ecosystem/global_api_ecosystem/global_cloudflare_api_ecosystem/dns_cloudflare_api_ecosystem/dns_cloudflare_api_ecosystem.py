"""Cloudflare DNS API catalog metadata; not a live connector."""

CLOUDFLARE_DNS_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "DNS",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "DNS record management for authorized Cloudflare zones.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/dns/",
    "api_boundary": "/zones/{zone_id}/dns_records",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
