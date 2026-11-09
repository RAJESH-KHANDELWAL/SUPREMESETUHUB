"""API use cases for GLOBAL SERVER ECOSYSTEM.

API owns HTTP orchestration. CORE validates provider-neutral identities.
SERVER owns in-memory server runtime registration. DATABASE and STORAGE
remain descriptive until their inventory and artifact contracts are implemented.
"""
from __future__ import annotations

from dataclasses import asdict
from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem import ServerCoreService
from backend.server.global_ecosystem.global_server_ecosystem import (
    EcosystemService as ServerInventoryService,
    ServerNode,
    get_provider,
    get_service_type,
    list_providers,
    list_service_types,
)
from backend.database.global_ecosystem.global_database_ecosystem import (
    GlobalDatabaseEcosystemManager as GlobalDatabaseEcosystemService,
)

_core = ServerCoreService()
_inventory = ServerInventoryService()
_database = GlobalDatabaseEcosystemService()


def _server_dict(server: ServerNode) -> dict[str, Any]:
    return asdict(server)


def get_server_ecosystem_status() -> dict[str, Any]:
    return {
        "success": True,
        "ecosystem": "GLOBAL SERVER API ECOSYSTEM",
        "status": "FOUNDATION_READY",
        "provider_count": len(list_providers()),
        "service_type_count": len(list_service_types()),
        "registered_server_count": _inventory.registry.count(),
        "core": _core.health(),
        "database": _database.describe(),
        "storage": {"status": "CATALOG_ONLY", "manager_initialized": False},
        "live_connections_verified": False,
        "durable_persistence_enabled": False,
        "binary_storage_enabled": False,
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
    items = [_server_dict(item) for item in _inventory.list_servers()]
    return {"success": True, "count": len(items), "servers": items}


def get_server(server_id: str):
    try:
        server = _inventory.get_server(server_id)
    except ValueError:
        return None
    return {"success": True, "server": _server_dict(server)} if server else None


def register_server(payload: dict[str, Any]):
    validated = _core.validate_identity(payload)
    if not validated["success"]:
        return validated

    data = validated["identity"]
    metadata = dict(data.get("metadata", {}))
    server_name = str(metadata.pop("server_name", None) or data["server_id"])
    endpoint = metadata.pop("endpoint", None)
    protocol = metadata.pop("protocol", None)
    metadata.update({key: value for key, value in {
        "endpoint": endpoint, "protocol": protocol
    }.items() if value is not None})

    try:
        node = ServerNode(
            server_id=data["server_id"],
            name=server_name,
            environment=data["environment"],
            metadata={
                **metadata,
                "provider_id": data["provider_id"],
                "server_type": data["server_type"],
                "server_role": data["server_role"],
                "country": data["country"],
                "region": data["region"],
            },
        )
        created = _inventory.register_server(node)
    except (TypeError, ValueError) as exc:
        return {"success": False, "error": "SERVER_REGISTRATION_FAILED", "message": str(exc)}

    return {
        "success": True,
        "server": _server_dict(created),
        "persistence_backend": "IN_MEMORY_RUNTIME_REGISTRY",
        "durable_persistence_enabled": False,
    }


def mark_server_authorized(server_id: str):
    try:
        server = _inventory.get_server(server_id)
    except ValueError:
        server = None
    if server is None:
        return {"success": False, "error": "SERVER_NOT_FOUND"}
    server.status = "AUTHORIZED"
    return {"success": True, "server": _server_dict(server), "durable_persistence_enabled": False}


def disable_server(server_id: str):
    try:
        server = _inventory.get_server(server_id)
    except ValueError:
        server = None
    if server is None:
        return {"success": False, "error": "SERVER_NOT_FOUND"}
    server.status = "DISABLED"
    return {"success": True, "server": _server_dict(server), "durable_persistence_enabled": False}


def register_server_artifact(payload: dict[str, Any]):
    return {
        "success": False,
        "error": "SERVER_ARTIFACT_STORAGE_CONTRACT_NOT_IMPLEMENTED",
        "message": "Server artifact persistence is not configured.",
    }


def list_server_artifacts(server_id: str):
    return {
        "success": True,
        "count": 0,
        "artifacts": [],
        "server_id": server_id,
        "storage_enabled": False,
    }


__all__ = [
    "get_server_ecosystem_status", "list_server_providers", "get_server_provider",
    "list_server_types", "get_server_type", "list_servers", "get_server",
    "register_server", "mark_server_authorized", "disable_server",
    "register_server_artifact", "list_server_artifacts",
]
