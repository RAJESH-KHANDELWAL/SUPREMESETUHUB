"""Cloudflare Security and WAF API catalog metadata; not a live connector."""

CLOUDFLARE_SECURITY_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "Security and WAF",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Security rules and rulesets exposed by Cloudflare APIs.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/rulesets/",
    "api_boundary": "Rulesets API resources",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
