"""Canonical identity and capability taxonomy for Global Hosting Core."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

HOSTING_CORE_CATALOG: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTING CORE ECOSYSTEM",
    "layer": "CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "CORE_CATALOG_ONLY",
    "enabled": True,
    "capabilities": [
        "HOSTING_PROVIDER_REGISTRY", "CLOUD_INFRASTRUCTURE_METADATA",
        "WEB_AND_MANAGED_HOSTING_METADATA", "PLATFORM_AS_A_SERVICE_METADATA",
        "EDGE_CDN_AND_OBJECT_STORAGE_METADATA", "HOSTING_LIFECYCLE_POLICY",
        "TENANT_SCOPED_HOSTING_METADATA",
    ],
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_hosting_api_ecosystem",
    "live_connection_verified": False,
    "api_calls_performed": 0,
}

HOSTING_CAPABILITY_DOMAINS: tuple[dict[str, str], ...] = (
    {"id": "HOSTING_PROVIDER_REGISTRY", "name": "Provider Registry"},
    {"id": "CLOUD_INFRASTRUCTURE", "name": "Cloud Infrastructure"},
    {"id": "WEB_AND_MANAGED_HOSTING", "name": "Web and Managed Hosting"},
    {"id": "PLATFORM_AS_A_SERVICE", "name": "Platform as a Service"},
    {"id": "EDGE_CDN_AND_OBJECT_STORAGE", "name": "Edge, CDN and Object Storage"},
    {"id": "HOSTING_CONTROL_AND_MANAGEMENT", "name": "Hosting Control and Management"},
    {"id": "HOSTING_LIFECYCLE_POLICY", "name": "Hosting Lifecycle Policy"},
)

def get_hosting_core_catalog() -> dict[str, Any]:
    return deepcopy(HOSTING_CORE_CATALOG)

def list_hosting_capability_domains() -> list[dict[str, str]]:
    return [dict(item) for item in HOSTING_CAPABILITY_DOMAINS]
