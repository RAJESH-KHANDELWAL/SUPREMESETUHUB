"""Canonical catalog metadata for the global Agriculture/Food CORE."""
from __future__ import annotations
from .domain_catalog import list_domains

CATALOG = {
    "ecosystem_id": "GLOBAL-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM",
    "name": "GLOBAL AGRICULTURE FOOD & NATURAL RESOURCES HUMAN ANIMAL CORE ECOSYSTEM",
    "version": "1.0.0",
    "status": "REGISTERED",
    "layer": "GLOBAL_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "business_layer_id": "GLOBAL-BADA-BUSINESS-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM",
    "domains": list_domains(),
    "capabilities": ["DOMAIN_TAXONOMY", "METADATA_DISCOVERY", "POLICY_CLASSIFICATION", "DEPENDENCY_METADATA"],
    "live_data_verified": False,
    "provider_connections_verified": False,
}

def get_catalog() -> dict:
    return {**CATALOG, "domains": [dict(item) for item in CATALOG["domains"]], "capabilities": list(CATALOG["capabilities"])}
