"""Website capability/product families; listing does not imply vendor entitlement."""
from __future__ import annotations

WEBSITE_PRODUCT_FAMILIES = (
    {"family_id": "DOMAIN_REGISTRATION_DNS", "name": "Domain Registration and DNS", "domain_ids": ("DOMAIN_NAME_MANAGEMENT", "DNS_AND_ZONE_MANAGEMENT")},
    {"family_id": "WEBSITE_HOSTING", "name": "Website Hosting", "domain_ids": ("SHARED_HOSTING", "CLOUD_HOSTING", "MANAGED_HOSTING", "STATIC_HOSTING")},
    {"family_id": "WEBSITE_BUILDING_CMS", "name": "Website Builders and CMS", "domain_ids": ("WEBSITE_BUILDERS", "CONTENT_MANAGEMENT_SYSTEMS", "HEADLESS_CMS")},
    {"family_id": "WEBSITE_RUNTIME_DEPLOYMENT", "name": "Website Runtime and Deployment", "domain_ids": ("WEB_SERVER_RUNTIME", "DEPLOYMENT_RELEASES", "CI_CD_AND_AUTOMATION")},
    {"family_id": "WEBSITE_SECURITY", "name": "Website Security", "domain_ids": ("TLS_CERTIFICATES", "WAF_AND_DDOS", "IDENTITY_ACCESS_AND_SECRETS")},
    {"family_id": "WEBSITE_DELIVERY_PERFORMANCE", "name": "Website Delivery and Performance", "domain_ids": ("CDN_AND_EDGE_DELIVERY", "CACHING_AND_OPTIMIZATION", "AVAILABILITY_AND_RECOVERY")},
    {"family_id": "WEBSITE_GROWTH_ANALYTICS", "name": "Website Search, Analytics and Growth", "domain_ids": ("SEO_AND_INDEXING", "WEB_ANALYTICS_AND_TAGGING", "ACCESSIBILITY_AND_COMPLIANCE")},
)

def list_product_families() -> list[dict]:
    return [{**item, "registration_type": "CAPABILITY_FAMILY", "live_connection_verified": False}
            for item in WEBSITE_PRODUCT_FAMILIES]

def get_product_family(family_id: str) -> dict | None:
    key = str(family_id).strip().upper()
    return next((item for item in list_product_families() if item["family_id"] == key), None)

def product_summary() -> dict:
    items = list_product_families()
    return {"product_family_count": len(items), "product_family_ids": [item["family_id"] for item in items]}
