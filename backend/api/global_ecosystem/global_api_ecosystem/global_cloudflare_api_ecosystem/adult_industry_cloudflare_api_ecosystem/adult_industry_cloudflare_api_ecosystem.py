"""Catalog-only mapping of Cloudflare products relevant to adult-industry sites.

This is not a dedicated Cloudflare adult-industry API and does not imply a live
connection to any adult-industry provider. Verify official docs, account access,
terms, eligibility, and applicable law before implementation.
"""

ECOSYSTEM_NAME = "adult_industry_cloudflare_api_ecosystem"
PROVIDER_ID = "cloudflare"
FAMILY = "ADULT_INDUSTRY"
STATUS = "CATALOG_ONLY"
LIVE_CONNECTION_VERIFIED = False
DEDICATED_ADULT_INDUSTRY_API_CONFIRMED = False

PRODUCT_MAPPINGS = {
    "zones_dns": {
        "category": "DOMAIN_DNS",
        "purpose": "Authorized domain-zone and DNS management",
        "module": "zones_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem.py",
        "docs": "https://developers.cloudflare.com/api/",
    },
    "security_waf_api_shield": {
        "category": "SECURITY",
        "purpose": "Available website and API security controls",
        "module": "security_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem.py",
        "docs": "https://developers.cloudflare.com/api/",
    },
    "ssl_tls": {
        "category": "SECURITY",
        "purpose": "Supported TLS and certificate configuration",
        "module": "ssl_tls_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem.py",
        "docs": "https://developers.cloudflare.com/ssl/",
    },
    "r2": {
        "category": "STORAGE",
        "purpose": "Object storage where use is permitted and account access exists",
        "module": "r2_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem.py",
        "docs": "https://developers.cloudflare.com/r2/",
    },
    "stream_images": {
        "category": "MEDIA",
        "purpose": "Media services only where current policies and eligibility permit",
        "modules": [
            "stream_cloudflare_api_ecosystem/stream_cloudflare_api_ecosystem.py",
            "images_cloudflare_api_ecosystem/images_cloudflare_api_ecosystem.py",
        ],
        "docs": "https://developers.cloudflare.com/",
    },
    "workers_pages": {
        "category": "APP_WEB",
        "purpose": "Website/application infrastructure subject to current terms",
        "modules": [
            "workers_cloudflare_api_ecosystem/workers_cloudflare_api_ecosystem.py",
            "pages_cloudflare_api_ecosystem/pages_cloudflare_api_ecosystem.py",
        ],
        "docs": "https://developers.cloudflare.com/",
    },
    "analytics_logpush": {
        "category": "ANALYTICS",
        "purpose": "Supported analytics and log-export capabilities",
        "module": "analytics_logpush_cloudflare_api_ecosystem/analytics_logpush_cloudflare_api_ecosystem.py",
        "docs": "https://developers.cloudflare.com/logs/",
    },
}


def get_ecosystem_info() -> dict[str, object]:
    """Return catalog metadata without making network requests."""
    return {
        "name": ECOSYSTEM_NAME,
        "provider_id": PROVIDER_ID,
        "family": FAMILY,
        "status": STATUS,
        "live_connection_verified": LIVE_CONNECTION_VERIFIED,
        "dedicated_adult_industry_api_confirmed": DEDICATED_ADULT_INDUSTRY_API_CONFIRMED,
        "product_mappings": PRODUCT_MAPPINGS,
    }
