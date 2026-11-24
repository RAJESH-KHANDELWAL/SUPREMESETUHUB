"""Web capability families; no provider entitlement or API availability is implied."""
from __future__ import annotations
from copy import deepcopy

WEB_PRODUCT_FAMILIES = (
    {"family_id": "WEB_HOSTING", "name": "Web Hosting", "domain_ids": ("WEB_INFRASTRUCTURE", "WEB_HOSTING_AND_DEPLOYMENT")},
    {"family_id": "DOMAIN_DNS", "name": "Domains and DNS", "domain_ids": ("DOMAINS_AND_DNS",)},
    {"family_id": "CDN_EDGE", "name": "CDN and Edge Delivery", "domain_ids": ("CDN_AND_EDGE",)},
    {"family_id": "WEB_SECURITY", "name": "Web Security", "domain_ids": ("WEB_SECURITY_AND_PRIVACY",)},
    {"family_id": "WEB_PLATFORM", "name": "Web Platforms and Applications", "domain_ids": ("WEB_DEVELOPMENT", "CMS_AND_WEBSITE_PLATFORMS", "WEB_APPLICATIONS")},
    {"family_id": "WEB_ANALYTICS", "name": "Web Analytics and Search", "domain_ids": ("WEB_ANALYTICS_AND_OBSERVABILITY", "SEARCH_AND_INDEXING")},
    {"family_id": "WEB_DELIVERY", "name": "Web Deployment and Operations", "domain_ids": ("WEB_HOSTING_AND_DEPLOYMENT", "WEB_PERFORMANCE_AND_RELIABILITY")},
)
def list_product_families() -> list[dict]:
    return [dict(item, registration_type="CAPABILITY_FAMILY", live_connection_verified=False)
            for item in WEB_PRODUCT_FAMILIES]
def get_product_family(family_id: str) -> dict | None:
    key = str(family_id).strip().upper()
    return next((item for item in list_product_families() if item["family_id"] == key), None)
def product_summary() -> dict:
    items = list_product_families()
    return {"product_family_count": len(items), "product_family_ids": [x["family_id"] for x in items]}
