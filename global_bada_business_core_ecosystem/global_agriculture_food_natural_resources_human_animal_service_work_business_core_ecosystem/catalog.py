"""Bada Business Agriculture/Food catalog."""
from .domain_catalog import list_business_domains

CATALOG = {
    "ecosystem_id": "GLOBAL-BADA-BUSINESS-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM",
    "name": "GLOBAL BADA BUSINESS AGRICULTURE FOOD & NATURAL RESOURCES HUMAN ANIMAL SERVICE WORK BUSINESS CORE ECOSYSTEM",
    "parent_id": "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM",
    "global_core_id": "GLOBAL-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM",
    "layer": "GLOBAL_BADA_BUSINESS_CORE",
    "status": "REGISTERED",
    "domains": list_business_domains(),
    "capabilities": ["SERVICE_DISCOVERY", "WORK_CLASSIFICATION", "BUSINESS_CAPABILITY_CATALOG", "ENTERPRISE_TAXONOMY"],
    "live_providers_verified": False,
}

def get_catalog():
    return {**CATALOG, "domains": [dict(x) for x in CATALOG["domains"]], "capabilities": list(CATALOG["capabilities"])}
