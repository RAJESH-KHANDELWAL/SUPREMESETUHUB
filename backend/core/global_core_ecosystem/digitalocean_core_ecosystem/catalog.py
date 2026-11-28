"""Canonical DigitalOcean Core provider and capability catalog."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

DIGITALOCEAN_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "DIGITALOCEAN-CORE-ECOSYSTEM",
    "name": "DIGITALOCEAN CORE ECOSYSTEM",
    "provider": "digitalocean",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "layer": "CORE",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem",
    "capabilities": {
        "cloud": {
            "package": "digitalocean_cloud_core_ecosystem",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_cloud_api_ecosystem",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "hosting": {
            "package": "digitalocean_hosting_core_ecosystem",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_hosting_api_ecosystem",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "server": {
            "package": "digitalocean_server_core_ecosystem",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_server_api_ecosystem",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "storage": {
            "package": "digitalocean_storage_core_ecosystem",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_storage_api_ecosystem",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "vps": {
            "package": "digitalocean_vps_core_ecosystem",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_vps_api_ecosystem",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
    },
}


def get_catalog() -> dict[str, Any]:
    """Return a defensive copy of the provider catalog."""
    return deepcopy(DIGITALOCEAN_CORE_ECOSYSTEM)


def list_capabilities() -> dict[str, dict[str, Any]]:
    """Return capability metadata keyed by stable capability ID."""
    return deepcopy(DIGITALOCEAN_CORE_ECOSYSTEM["capabilities"])
