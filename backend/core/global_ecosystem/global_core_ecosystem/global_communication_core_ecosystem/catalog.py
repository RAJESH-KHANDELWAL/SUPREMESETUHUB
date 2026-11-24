"""Canonical Global Communication Core catalog; metadata only."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .product_catalog import PROVIDER_DIRECTORY, EXISTING_DIRECTORY_INVENTORY, inventory_summary
from .domain_catalog import DOMAIN_DEFINITIONS

ROOT: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM",
    "name": "GLOBAL COMMUNICATION CORE ECOSYSTEM",
    "provider": "provider_neutral",
    "ecosystem_type": "GLOBAL_DOMAIN_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "CORE_CATALOG_ONLY",
    "enabled": True,
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_communication_core_ecosystem",
    "capabilities": [
        "COMMUNICATION_PROVIDER_IDENTITY",
        "PRODUCT_AND_SERVICE_DISCOVERY",
        "DOMAIN_CLASSIFICATION",
        "CAPABILITY_AND_LIFECYCLE_METADATA",
        "TENANT_AND_AUTHORIZATION_POLICY_BOUNDARIES",
        "PRIVACY_TRUST_AND_SAFETY_METADATA",
        "DEPENDENCY_AND_READINESS_DISCOVERY",
    ],
    "live_connection_verified": False,
    "api_transport_in_core": False,
    "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
}

def get_communication_core_catalog() -> dict[str, Any]:
    """Return a detached canonical root and its provider/platform references."""
    root = deepcopy(ROOT)
    root["provider_reference_count"] = len(PROVIDER_DIRECTORY)
    root["directory_inventory_count"] = len(EXISTING_DIRECTORY_INVENTORY)
    root["domain_count"] = len(DOMAIN_DEFINITIONS)
    root["providers"] = [
        {**deepcopy(item), "ecosystem_id": f"GLOBAL-{item['id'].upper()}-COMMUNICATION-CORE-ECOSYSTEM",
         "parent_id": "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM",
         "capabilities": ["PROVIDER_IDENTITY_METADATA", "COMMUNICATION_PRODUCT_DISCOVERY", "CAPABILITY_CLASSIFICATION"],
         "live_connection_verified": False}
        for item in PROVIDER_DIRECTORY
    ]
    root["directory_inventory"] = deepcopy(list(EXISTING_DIRECTORY_INVENTORY))
    root["domains"] = [
        {"domain_id": key, **deepcopy(value), "status": "CORE_CATALOG_ONLY"}
        for key, value in DOMAIN_DEFINITIONS.items()
    ]
    root["inventory_summary"] = inventory_summary()
    return root

__all__ = ["ROOT", "get_communication_core_catalog"]
