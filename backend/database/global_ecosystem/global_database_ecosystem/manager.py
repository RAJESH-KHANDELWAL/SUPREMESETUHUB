"""Independent GLOBAL DATABASE ECOSYSTEM hierarchy manager.

This module owns DATABASE catalog registration, discovery and hierarchy APIs.
It does not import API, CORE, or ENGINE packages and never opens DB connections.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .catalog import ROOT_ID, get_catalog
from .ecosystem_registry import DatabaseEcosystemRegistry
from .models import DatabaseEcosystemIdentity


class GlobalDatabaseEcosystemManager:
    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL DATABASE ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.registry = DatabaseEcosystemRegistry()
        self._initialize()

    def _initialize(self) -> None:
        records = get_catalog()
        if not records or records[0]["ecosystem_id"] != self.ROOT_ID:
            raise RuntimeError("DATABASE root catalog is missing or invalid")
        registered: set[str] = set()
        for record in records:
            identity = DatabaseEcosystemIdentity(**record)
            if identity.ecosystem_id in registered:
                raise RuntimeError(f"Duplicate DATABASE ecosystem ID: {identity.ecosystem_id}")
            if identity.parent_id and identity.parent_id not in registered:
                raise RuntimeError(
                    f"Parent must be registered before child: {identity.ecosystem_id}"
                )
            self.registry.register(identity)
            registered.add(identity.ecosystem_id)

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)
        return {
            "success": root is not None, "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME, "version": self.VERSION,
            "status": "FOUNDATION_READY" if root else "NOT_INITIALIZED",
            "count": self.registry.count(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "layer": "DATABASE", "independent": True,
        }

    def health(self) -> dict[str, Any]:
        ready = self.registry.exists(self.ROOT_ID)
        return {
            "success": ready, "service": self.ROOT_NAME,
            "status": "HEALTHY" if ready else "DEGRADED",
            "registry_available": self.registry is not None,
            "registry_count": self.registry.count(),
            "database_connections_verified": False,
            "migrations_verified": False,
        }

    def list(self) -> dict[str, Any]:
        items = self.registry.list()
        return {"success": True, "count": len(items), "ecosystems": items}

    def names(self) -> dict[str, Any]:
        items = self.registry.names()
        return {"success": True, "count": len(items), "names": items}

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        return self.registry.exists(ecosystem_id)

    def register(self, identity: DatabaseEcosystemIdentity | dict[str, Any]) -> dict[str, Any]:
        item = identity if isinstance(identity, DatabaseEcosystemIdentity) else DatabaseEcosystemIdentity(**identity)
        key = item.ecosystem_id.strip()
        if not key:
            return {"success": False, "error": "ECOSYSTEM_ID_REQUIRED"}
        if self.registry.exists(key):
            return {"success": False, "error": "ECOSYSTEM_ALREADY_EXISTS", "ecosystem_id": key}
        try:
            return {"success": True, "ecosystem": self.registry.register(item)}
        except (ValueError, KeyError) as exc:
            return {"success": False, "error": "REGISTRATION_FAILED", "message": str(exc)}

    def tree(self) -> dict[str, Any]:
        records = self.registry.list()
        by_id = {item["ecosystem_id"]: {**item, "children": []} for item in records}
        for item in records:
            parent = item.get("parent_id")
            if parent in by_id:
                by_id[parent]["children"].append(by_id[item["ecosystem_id"]])
        root = by_id.get(self.ROOT_ID)
        return {"success": root is not None, "tree": root}

    def connection_map(self) -> dict[str, Any]:
        records = self.registry.list()
        edges = [
            {"source": item["parent_id"], "target": item["ecosystem_id"], "relationship": "CONTAINS"}
            for item in records if item.get("parent_id")
        ]
        return {
            "success": True, "node_count": len(records),
            "edge_count": len(edges), "edges": edges,
        }

    def list_providers(self) -> list[dict[str, Any]]:
        from .registry import GlobalDatabaseEcosystemRegistry as ProviderRegistry
        return ProviderRegistry.list_providers()

    def get_provider(self, provider_id: str):
        from .registry import GlobalDatabaseEcosystemRegistry as ProviderRegistry
        return ProviderRegistry.get_provider(provider_id)


EcosystemManager = GlobalDatabaseEcosystemManager
