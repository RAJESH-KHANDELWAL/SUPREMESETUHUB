"""API use cases for GLOBAL SERVER ECOSYSTEM.

API owns HTTP orchestration. CORE validates provider-neutral identities.
SERVER owns server identity/catalog orchestration. DATABASE persists structured
inventory. STORAGE owns artifact persistence. Each layer is imported from its
own namespace; no implementation is copied into API or SERVER.
"""
from __future__ import annotations
from typing import Any
from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem import ServerCoreService
from backend.server.global_ecosystem.global_server_ecosystem import (
    EcosystemService as ServerInventoryService,
    get_provider, get_service_type, list_providers, list_service_types,
)
from backend.database.global_ecosystem.global_database_ecosystem import (
    GlobalDatabaseEcosystemService, ServerInventoryRecord,
)
from backend.storage.global_ecosystem.global_storage_ecosystem import (
    EcosystemService as StorageEcosystemService, ServerArtifact,
)
_core = ServerCoreService()
_inventory = ServerInventoryService()
_database = GlobalDatabaseEcosystemService()
_storage = StorageEcosystemService()

def get_server_ecosystem_status() -> dict[str, Any]:
    return {
        "success": True, "ecosystem": "GLOBAL SERVER API ECOSYSTEM",
        "status": "FOUNDATION_READY",
        "provider_count": len(list_providers()),
        "service_type_count": len(list_service_types()),
        "registered_server_count": _inventory.registry.count(),
        "core": _core.health(), "database": _database.describe(),
        "storage": _storage.describe(), "live_connections_verified": False,
        "durable_persistence_enabled": False, "binary_storage_enabled": False,
    }
def list_server_providers():
    items = list_providers()
    return {"success": True, "count": len(items), "providers": items}
def get_server_provider(provider_id: str):
    try: return {"success": True, "provider": get_provider(provider_id)}
    except KeyError: return None
def list_server_types():
    items = list_service_types()
    return {"success": True, "count": len(items), "service_types": items}
def get_server_type(service_type_id: str):
    try: return {"success": True, "service_type": get_service_type(service_type_id)}
    except KeyError: return None
def list_servers():
    records = _database.list_server_inventory()
    if records["count"]:
        return {"success": True, "count": records["count"], "servers": records["records"]}
    return _inventory.list_servers()
def get_server(server_id: str):
    persisted = _database.get_server_inventory(server_id)
    if persisted is not None: return {"success": True, "server": persisted["record"]}
    local = _inventory.get_server(server_id)
    return local if local["success"] else None
def register_server(payload: dict[str, Any]):
    validated = _core.validate_identity(payload)
    if not validated["success"]: return validated
    data = validated["identity"]
    server_name = data.get("metadata", {}).get("server_name") or data["server_id"]
    record = ServerInventoryRecord(
        server_id=data["server_id"], server_name=server_name,
        provider_id=data["provider_id"], server_type=data["server_type"],
        server_role=data["server_role"], country=data["country"],
        region=data["region"], environment=data["environment"],
        metadata=dict(data.get("metadata", {})),
    )
    created = _inventory.register_server(
        server_id=record.server_id, server_name=record.server_name,
        provider_id=record.provider_id, server_type=record.server_type,
        server_role=record.server_role, country=record.country,
        region=record.region, environment=record.environment,
    )
    if not created["success"]: return created
    persisted = _database.create_server_inventory(record)
    return {"success": True, "server": created["server"], "database": persisted,
            "persistence_backend": "IN_MEMORY_REFERENCE_ADAPTER",
            "durable_persistence_enabled": False}
def mark_server_authorized(server_id: str):
    local = _inventory.authorize_server(server_id)
    persisted = _database.update_server_inventory(server_id, authorized=True, status="AUTHORIZED")
    if not local["success"]: return local
    return {"success": True, "server": local["server"], "database": persisted}
def disable_server(server_id: str):
    local = _inventory.disable_server(server_id)
    persisted = _database.update_server_inventory(server_id, enabled=False, status="DISABLED")
    if not local["success"]: return local
    return {"success": True, "server": local["server"], "database": persisted}
def register_server_artifact(payload: dict[str, Any]):
    return _storage.register_server_artifact(ServerArtifact(**dict(payload)))
def list_server_artifacts(server_id: str):
    return _storage.list_server_artifacts(server_id)
