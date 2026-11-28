"""Cloudflare mapping for the shared Adult Industry API ecosystem.

Catalog/routing metadata only. This does not claim Cloudflare has a dedicated
adult-industry API, that any listed platform uses Cloudflare, or that every
product is eligible for every use case. Check current Cloudflare terms and
the provider's official integration documentation before implementation.
"""

PROVIDER_ID = "cloudflare"
PROVIDER_NAME = "CLOUDFLARE API ECOSYSTEM"
CATEGORY_ID = "ADULT_INDUSTRY"
CATEGORY_NAME = "GLOBAL ADULT INDUSTRY API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_cloudflare_api_ecosystem"
CATEGORY_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_adult_industry_api_ecosystem"
SCOPE = "Map adult-industry catalog entries to potentially relevant Cloudflare infrastructure products; this is not a dedicated adult API."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
API_DOCUMENTATION_VERIFIED = False
LIVE_CONNECTION_VERIFIED = False
DEDICATED_ADULT_INDUSTRY_API_VERIFIED = False

# Adult-industry-related entries already represented in the AI API ecosystem.
AI_API_ENTRIES = {
    "abelohost": "global_ai_api_ecosystem/abelohost_ai_api_ecosystem",
    "bangbros": "global_ai_api_ecosystem/bangbros_ai_api_ecosystem",
    "brazzers": "global_ai_api_ecosystem/brazzers_ai_api_ecosystem",
    "ccbill": "global_ai_api_ecosystem/ccbill_ai_api_ecosystem",
    "clips4sale": "global_ai_api_ecosystem/clips4sale_ai_api_ecosystem",
    "crakrevenue": "global_ai_api_ecosystem/crakrevenue_ai_api_ecosystem",
    "epoch": "global_ai_api_ecosystem/epoch_ai_api_ecosystem",
    "evilangel": "global_ai_api_ecosystem/evilangel_ai_api_ecosystem",
    "exoclick": "global_ai_api_ecosystem/exoclick_ai_api_ecosystem",
    "fansly": "global_ai_api_ecosystem/fansly_ai_api_ecosystem",
    "faphouse": "global_ai_api_ecosystem/faphouse_ai_api_ecosystem",
    "loyalfans": "global_ai_api_ecosystem/loyalfans_ai_api_ecosystem",
    "manyvids": "global_ai_api_ecosystem/manyvids_ai_api_ecosystem",
    "naughtyamerica": "global_ai_api_ecosystem/naughtyamerica_ai_api_ecosystem",
    "nsfwinfra": "global_ai_api_ecosystem/nsfwinfra_ai_api_ecosystem",
    "onlyfans": "global_ai_api_ecosystem/onlyfans_ai_api_ecosystem",
    "paxum": "global_ai_api_ecosystem/paxum_ai_api_ecosystem",
    "pornhub": "global_ai_api_ecosystem/pornhub_ai_api_ecosystem",
    "realitykings": "global_ai_api_ecosystem/realitykings_ai_api_ecosystem",
    "segpay": "global_ai_api_ecosystem/segpay_ai_api_ecosystem",
    "trafficjunky": "global_ai_api_ecosystem/trafficjunky_ai_api_ecosystem",
    "verotel": "global_ai_api_ecosystem/verotel_ai_api_ecosystem",
    "vicetemple": "global_ai_api_ecosystem/vicetemple_ai_api_ecosystem",
    "xhamster": "global_ai_api_ecosystem/xhamster_ai_api_ecosystem",
    "xvideos": "global_ai_api_ecosystem/xvideos_ai_api_ecosystem",
}

# Adult-industry-related entries already represented in the APP API ecosystem.
APP_API_ENTRIES = {
    "bangbros": "global_app_api_ecosystem/bangbros_app_api_ecosystem",
    "brazzers": "global_app_api_ecosystem/brazzers_app_api_ecosystem",
    "clips4sale": "global_app_api_ecosystem/clips4sale_app_api_ecosystem",
    "evilangel": "global_app_api_ecosystem/evilangel_app_api_ecosystem",
    "fansly": "global_app_api_ecosystem/fansly_app_api_ecosystem",
    "faphouse": "global_app_api_ecosystem/faphouse_app_api_ecosystem",
    "loyalfans": "global_app_api_ecosystem/loyalfans_app_api_ecosystem",
    "manyvids": "global_app_api_ecosystem/manyvids_app_api_ecosystem",
    "naughtyamerica": "global_app_api_ecosystem/naughtyamerica_app_api_ecosystem",
    "onlyfans": "global_app_api_ecosystem/onlyfans_app_api_ecosystem",
    "pornhub": "global_app_api_ecosystem/pornhub_app_api_ecosystem",
    "realitykings": "global_app_api_ecosystem/realitykings_app_api_ecosystem",
    "xhamster": "global_app_api_ecosystem/xhamster_app_api_ecosystem",
    "xvideos": "global_app_api_ecosystem/xvideos_app_api_ecosystem",
}

# Hosting/infrastructure providers cataloged in the CLOUD API ecosystem as
# adult-friendly or adult-industry-relevant infrastructure; eligibility varies.
CLOUD_API_ENTRIES = {
    "abelohost": "global_cloud_api_ecosystem/abelohost_cloud_api_ecosystem",
    "alexhost": "global_cloud_api_ecosystem/alexhost_cloud_api_ecosystem",
    "blueangelhost": "global_cloud_api_ecosystem/blueangelhost_cloud_api_ecosystem",
    "flokinet": "global_cloud_api_ecosystem/flokinet_cloud_api_ecosystem",
    "hostkey": "global_cloud_api_ecosystem/hostkey_cloud_api_ecosystem",
    "hostsailor": "global_cloud_api_ecosystem/hostsailor_cloud_api_ecosystem",
    "shinjiru": "global_cloud_api_ecosystem/shinjiru_cloud_api_ecosystem",
    "vicetemple": "global_cloud_api_ecosystem/vicetemple_cloud_api_ecosystem",
}

# General Cloudflare products potentially useful for a compliant website or app.
# These are product-module references, not guarantees of account availability.
RELEVANT_PRODUCT_MODULES = {
    "zones_dns": "global_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem.py",
    "security_waf_api_shield": "global_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem.py",
    "ssl_tls": "global_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem.py",
    "r2_object_storage": "global_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem.py",
    "stream_video": "global_cloudflare_api_ecosystem/stream_cloudflare_api_ecosystem/stream_cloudflare_api_ecosystem.py",
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
