"""Catalog of Cloudflare-owned product APIs backed by official documentation.

This file is descriptive metadata only: it does not make network requests and
does not imply that credentials or a live adapter are configured.
"""

CLOUDFLARE_PRODUCT_API_CATALOG = {
    "provider_id": "cloudflare",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "official_api_reference": "https://developers.cloudflare.com/api/",
    "authentication_reference": "https://developers.cloudflare.com/fundamentals/api/get-started/",
    "products": {
        "accounts": {
            "scope": "Account discovery and account-level management",
            "documentation": "https://developers.cloudflare.com/api/resources/accounts/",
        },
        "zones": {
            "scope": "Zone listing and zone lifecycle management",
            "documentation": "https://developers.cloudflare.com/api/resources/zones/",
        },
        "dns_records": {
            "scope": "DNS record management within authorized zones",
            "documentation": "https://developers.cloudflare.com/api/resources/dns/",
        },
        "workers": {
            "scope": "Workers scripts, deployments, routes, and related developer-platform resources",
            "documentation": "https://developers.cloudflare.com/api/resources/workers/",
        },
        "pages": {
            "scope": "Cloudflare Pages projects and deployments",
            "documentation": "https://developers.cloudflare.com/api/resources/pages/",
        },
        "r2": {
            "scope": "R2 object storage management APIs",
            "documentation": "https://developers.cloudflare.com/api/resources/r2/",
        },
        "ai_gateway": {
            "scope": "AI Gateway configuration and gateway resources",
            "documentation": "https://developers.cloudflare.com/api/resources/ai_gateway/",
        },
        "ssl_tls": {
            "scope": "SSL/TLS configuration and certificates where exposed by the API",
            "documentation": "https://developers.cloudflare.com/api/resources/",
        },
        "security_and_waf": {
            "scope": "Security settings and rulesets where exposed by the API",
            "documentation": "https://developers.cloudflare.com/api/resources/rulesets/",
        },
        "analytics_and_logs": {
            "scope": "Analytics, observability, and Logpush configuration where supported",
            "documentation": "https://developers.cloudflare.com/api/resources/",
        },
    },
    "security_requirements": [
        "Use least-privilege API tokens with only required account, zone, and product permissions.",
        "Keep credentials outside source control in environment variables or a managed secret store.",
        "Check the API reference and account/product eligibility before enabling an operation.",
        "Keep live_connection_verified false until authenticated integration tests pass.",
    ],
}
