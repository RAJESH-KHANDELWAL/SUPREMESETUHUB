"""Cloudflare provider-to-category mapping for GLOBAL ADULT INDUSTRY API ECOSYSTEM.

This is catalog metadata only. Cloudflare does not expose a dedicated adult-industry
API in this catalog; this mapping points to general Cloudflare services that may be
relevant, subject to current official terms, eligibility, and product rules.
"""

PROVIDER_ID = "cloudflare"
PROVIDER_NAME = "CLOUDFLARE API ECOSYSTEM"
CATEGORY_ID = "ADULT_INDUSTRY"
CATEGORY_NAME = "GLOBAL ADULT INDUSTRY API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_cloudflare_api_ecosystem"
CATEGORY_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_adult_industry_api_ecosystem"
SCOPE = "Provider-to-category mapping for adult-industry sites; only supported Cloudflare products are relevant, and no dedicated adult-industry API is implied."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
API_DOCUMENTATION_VERIFIED = False
LIVE_CONNECTION_VERIFIED = False

RELEVANT_PRODUCT_MODULES = {
    "zones_dns": "global_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem.py",
    "security_waf_api_shield": "global_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem.py",
    "ssl_tls": "global_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem.py",
    "r2": "global_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem.py",
    "stream": "global_cloudflare_api_ecosystem/stream_cloudflare_api_ecosystem/stream_cloudflare_api_ecosystem.py",
    "images": "global_cloudflare_api_ecosystem/images_cloudflare_api_ecosystem/images_cloudflare_api_ecosystem.py",
    "workers": "global_cloudflare_api_ecosystem/workers_cloudflare_api_ecosystem/workers_cloudflare_api_ecosystem.py",
    "pages": "global_cloudflare_api_ecosystem/pages_cloudflare_api_ecosystem/pages_cloudflare_api_ecosystem.py",
    "analytics_logpush": "global_cloudflare_api_ecosystem/analytics_logpush_cloudflare_api_ecosystem/analytics_logpush_cloudflare_api_ecosystem.py",
}

OFFICIAL_REFERENCES = {
    "api": "https://developers.cloudflare.com/api/",
    "developer_directory": "https://developers.cloudflare.com/directory/",
    "service_specific_terms": "https://www.cloudflare.com/en-in/service-specific-terms-application-services/",
}
