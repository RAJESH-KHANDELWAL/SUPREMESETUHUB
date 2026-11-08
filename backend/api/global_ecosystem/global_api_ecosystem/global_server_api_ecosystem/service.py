"""API layer service for GLOBAL SERVER ECOSYSTEM.

API owns HTTP-facing use cases and input/output orchestration. Core contracts and
inventory validation are delegated to CORE; engine execution stays in ENGINE;
durable persistence stays in DATABASE; object/file handling stays in STORAGE.
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
        "success": True,
        "ecosystem": "GLOBAL SERVER API ECOSYSTEM",
        "status": "FOUNDATION_READY",
        "provider_count": len(list_providers()),
        "service_type_count": len(list_service_types()),
        "registered_server_count": _inventory.registry.count(),
        "core": _core.health(),
        "live_connections_verified": False,
        "persistence_enabled": False,
    }


def list_server_providers() -> dict[str, Any]:
    providers = list_providers()
    return {"success": True, "count": len(providers), "providers": providers}


def get_server_provider(provider_id: str) -> dict[str, Any] | None:
    try:
        return {"success": True, "provider": get_provider(provider_id)}
    except KeyError:
        return None


def list_server_types() -> dict[str, Any]:
    items = list_service_types()
    return {"success": True, "count": len(items), "service_types": items}


def get_server_type(service_type_id: str) -> dict[str, Any] | None:
    try:
        return {"success": True, "service_type": get_service_type(service_type_id)}
    except KeyError:
        return None


def list_servers() -> dict[str, Any]:
    return _inventory.list_servers()


def get_server(server_id: str) -> dict[str, Any] | None:
    result = _inventory.get_server(server_id)
    return result if result["success"] else None


def register_server(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate identity through CORE before adding a local inventory record."""
    core_result = _core.register_identity(payload)
    if not core_result["success"]:
        return core_result
    return _inventory.register_server(**dict(payload))


def mark_server_authorized(server_id: str) -> dict[str, Any]:
    """Set a local authorization marker only; this is not provider authentication."""
    return _inventory.authorize_server(server_id)


def disable_server(server_id: str) -> dict[str, Any]:
    """Disable the local inventory entry; this does not shut down a remote host."""
    return _inventory.disable_server(server_id)
