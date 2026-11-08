"""API-facing service for GLOBAL SERVER ECOSYSTEM.

The API layer exposes validated metadata and local inventory operations. It does
not contain provider SDK code or persist inventory; those responsibilities stay
with ENGINE adapters and DATABASE respectively.
"""
from __future__ import annotations

from typing import Any

from backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM import (
    EcosystemService,
    get_provider,
    get_service_type,
    list_providers,
    list_service_types,
)

_inventory = EcosystemService()


def get_server_ecosystem_status() -> dict[str, Any]:
    return {
        "success": True,
        "ecosystem": "GLOBAL SERVER API ECOSYSTEM",
        "status": "FOUNDATION_READY",
        "provider_count": len(list_providers()),
        "service_type_count": len(list_service_types()),
        "registered_server_count": _inventory.registry.count(),
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
    service_types = list_service_types()
    return {"success": True, "count": len(service_types), "service_types": service_types}


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
    """Register local metadata only; this does not provision a real server."""
    return _inventory.register_server(**dict(payload))


def mark_server_authorized(server_id: str) -> dict[str, Any]:
    """Mark local inventory metadata; this does not authenticate with a provider."""
    result = _inventory.authorize_server(server_id)
    return result


def disable_server(server_id: str) -> dict[str, Any]:
    """Disable a local inventory entry; it does not power off a remote server."""
    return _inventory.disable_server(server_id)
