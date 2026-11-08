"""API layer service for GLOBAL SERVER ECOSYSTEM.

API owns HTTP use cases. CORE validates provider-neutral identity contracts;
ENGINE owns provider execution, DATABASE owns durable persistence, and STORAGE
owns file/object operations. This module invokes no remote provider by itself.
"""
from __future__ import annotations
from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem import (
    ServerCoreService,
)
from backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM import (
    EcosystemService as ServerInventoryService,
    get_provider, get_service_type, list_providers, list_service_types,
)

_core = ServerCoreService()
_inventory = ServerInventoryService()


def get_server_ecosystem_status() -> dict[str, Any]:
    return {
        "success": True, "ecosystem": "GLOBAL SERVER API ECOSYSTEM",
        "status": "FOUNDATION_READY",
        "provider_count": len(list_providers()),
        "service_type_count": len(list_service_types()),
        "registered_server_count": _inventory.registry.count(),
        "core": _core.health(),
        "live_connections_verified": False, "persistence_enabled": False,
    }


def list_server_providers():
    items = list_providers()
    return {"success": True, "count": len(items), "providers": items}


def get_server_provider(provider_id: str):
    try:
        return {"success": True, "provider": get_provider(provider_id)}
    except KeyError:
        return None


def list_server_types():
    items = list_service_types()
    return {"success": True, "count": len(items), "service_types": items}


def get_server_type(service_type_id: str):
    try:
        return {"success": True, "service_type": get_service_type(service_type_id)}
    except KeyError:
        return None


def list_servers():
    return _inventory.list_servers()


def get_server(server_id: str):
    result = _inventory.get_server(server_id)
    return result if result["success"] else None


def register_server(payload: dict[str, Any]):
    """Validate with CORE before storing a transient inventory record."""
    validated = _core.validate_identity(payload)
    if not validated["success"]:
        return validated
    return _inventory.register_server(**validated["identity"])


def mark_server_authorized(server_id: str):
    """Set a local authorization marker; this does not authenticate to a provider."""
    return _inventory.authorize_server(server_id)


def disable_server(server_id: str):
    """Disable a local inventory entry; it does not power off remote compute."""
    return _inventory.disable_server(server_id)
