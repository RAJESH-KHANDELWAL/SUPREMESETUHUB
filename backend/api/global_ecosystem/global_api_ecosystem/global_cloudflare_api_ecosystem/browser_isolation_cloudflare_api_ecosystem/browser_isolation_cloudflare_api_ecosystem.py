"""Cloudflare Browser Isolation API catalog metadata; no live requests are made here."""

CLOUDFLARE_PRODUCT = {
    "provider_id": "cloudflare",
    "product_id": "browser_isolation",
    "name": "Browser Isolation",
    "scope": "Remote browser isolation for Zero Trust",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "official_documentation": "https://developers.cloudflare.com/cloudflare-one/policies/browser-isolation/",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "credentials": "Use least-privilege API tokens from environment variables or a managed secret store.",
}
