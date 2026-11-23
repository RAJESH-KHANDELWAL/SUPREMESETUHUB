"""Canonical assembled catalog for GLOBAL WEBSITE CORE ECOSYSTEM."""
from __future__ import annotations
from copy import deepcopy
from .constants import CAPABILITIES, CANONICAL_MASTER_ENTRIES, ECOSYSTEM_ID, ECOSYSTEM_NAME, MASTER_CATALOG_PATH
from .domain_catalog import domain_summary, list_domain_inventory
from .product_catalog import list_product_families, product_summary
from .provider_catalog import list_providers, provider_summary

def get_catalog() -> dict:
    return {
        "ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME, "layer": "CORE",
        "status": "CORE_CATALOG_ONLY", "capabilities": list(CAPABILITIES),
        "providers": list_providers(), **provider_summary(),
        "product_families": list_product_families(), **product_summary(),
        "domains": list_domain_inventory(), **domain_summary(),
        "master_catalog": {
            "source": MASTER_CATALOG_PATH, "access_mode": "READ_ONLY_IMPLEMENTATION_REFERENCE",
            "canonical_entry_ids": list(CANONICAL_MASTER_ENTRIES),
            "taxonomy_entries_added": 0,
        },
        "live_connection_verified": False, "remote_operations_enabled": False,
        "api_calls_performed": 0, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    }

def get_website_core_catalog() -> dict:
    return deepcopy(get_catalog())
