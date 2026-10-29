"""Adult-industry catalog visible inside the Cloudflare API ecosystem.

This module is a cross-reference/catalog only. It does not imply that Cloudflare
offers a dedicated adult-industry API, that any listed provider uses Cloudflare,
or that Cloudflare products are eligible for every content category or use case.
Verify current Cloudflare terms and each provider's official API documentation.
"""

PROVIDER_ID = "cloudflare"
PROVIDER_NAME = "GLOBAL CLOUDFLARE API ECOSYSTEM"
CATEGORY_ID = "ADULT_INDUSTRY"
CATEGORY_NAME = "GLOBAL ADULT INDUSTRY API ECOSYSTEM"
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
DEDICATED_ADULT_INDUSTRY_API_VERIFIED = False
LIVE_CONNECTION_VERIFIED = False

# Names already listed in the shared AI API ecosystem catalog.
AI_API_ENTRIES = [
    "abelohost", "bangbros", "brazzers", "ccbill", "clips4sale",
    "crakrevenue", "epoch", "evilangel", "exoclick", "fansly",
    "faphouse", "loyalfans", "manyvids", "naughtyamerica", "nsfwinfra",
    "onlyfans", "paxum", "pornhub", "realitykings", "segpay",
    "trafficjunky", "verotel", "vicetemple", "xhamster", "xvideos",
]

# Names already listed in the shared APP API ecosystem catalog.
APP_API_ENTRIES = [
    "bangbros", "brazzers", "clips4sale", "evilangel", "fansly",
    "faphouse", "loyalfans", "manyvids", "naughtyamerica", "onlyfans",
    "pornhub", "realitykings", "xhamster", "xvideos",
]

# Hosting/infrastructure providers already listed in the shared CLOUD API catalog.
CLOUD_API_ENTRIES = [
    "abelohost", "alexhost", "blueangelhost", "flokinet",
    "hostkey", "hostsailor", "shinjiru", "vicetemple",
]

# Potentially relevant general-purpose Cloudflare product modules.
# These are product references, not a promise that all are suitable or enabled.
RELEVANT_CLOUDFLARE_PRODUCT_MODULES = {
    "zones_dns": "zones_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem.py",
    "security_waf_api_shield": "security_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem.py",
    "ssl_tls": "ssl_tls_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem.py",
    "r2_object_storage": "r2_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem.py",
    "stream_video": "stream_cloudflare_api_ecosystem/stream_cloudflare_api_ecosystem.py",
    "images": "images_cloudflare_api_ecosystem/images_cloudflare_api_ecosystem.py",
    "workers": "workers_cloudflare_api_ecosystem/workers_cloudflare_api_ecosystem.py",
    "pages": "pages_cloudflare_api_ecosystem/pages_cloudflare_api_ecosystem.py",
    "analytics_logpush": "analytics_logpush_cloudflare_api_ecosystem/analytics_logpush_cloudflare_api_ecosystem.py",
}

OFFICIAL_REFERENCES = {
    "cloudflare_api_docs": "https://developers.cloudflare.com/api/",
    "cloudflare_service_specific_terms": "https://www.cloudflare.com/en-in/service-specific-terms-application-services/",
}
