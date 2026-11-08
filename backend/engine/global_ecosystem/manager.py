"""Independent GLOBAL ENGINE ECOSYSTEM manager."""
from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
from .catalog import ROOT_ID, get_catalog
from .models import GlobalEcosystemIdentity
from .registry import GlobalEcosystemRegistry

class GlobalEcosystemManager:
    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL ENGINE ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.name, self.version = self.ROOT_NAME, self.VERSION
        self.registry = GlobalEcosystemRegistry()
        for record in get_catalog():
            self.registry.register(GlobalEcosystemIdentity(**record))

    def register(self, ecosystem: dict[str, Any] | GlobalEcosystemIdentity) -> dict[str, Any]:
        identity = ecosystem if isinstance(ecosystem, GlobalEcosystemIdentity) else GlobalEcosystemIdentity(
            ecosystem_id=str(ecosystem.get("ecosystem_id", "")).strip(),
            name=str(ecosystem.get("name", "")).strip(),
            ecosystem_type=str(ecosystem.get("ecosystem_type", "GENERAL")).strip(),
            repository_ref=ecosystem.get("repository_ref"),
            status=str(ecosystem.get("status", "REGISTERED")),
            enabled=bool(ecosystem.get("enabled", True)),
            capabilities=list(ecosystem.get("capabilities", [])),
            metadata=dict(ecosystem.get("metadata", {})), message=ecosystem.get("message"),
            parent_id=ecosystem.get("parent_id") or self.ROOT_ID)
        if self.registry.exists(identity.ecosystem_id):
            return {"success": False, "error": "ECOSYSTEM_ALREADY_EXISTS",
                    "ecosystem_id": identity.ecosystem_id}
        try:
            return {"success": True, "ecosystem": self.registry.register(identity)}
        except (ValueError, KeyError) as exc:
            return {"success": False, "error": "REGISTRATION_FAILED", "message": str(exc)}

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)
        return {"success": root is not None, "ecosystem_id": self.ROOT_ID,
                "name": self.ROOT_NAME, "version": self.VERSION,
                "status": "OPERATIONAL" if root else "NOT_INITIALIZED",
                "ecosystem_count": self.registry.count(),
                "timestamp": datetime.now(timezone.utc).isoformat()}

    def health(self) -> dict[str, Any]:
        ready = self.registry.exists(self.ROOT_ID)
        return {"success": ready, "service": self.ROOT_NAME,
                "status": "HEALTHY" if ready else "DEGRADED",
                "registry_available": self.registry is not None,
                "ecosystem_count": self.registry.count()}

    def list(self) -> dict[str, Any]:
        items = self.registry.list()
        return {"success": True, "count": len(items), "ecosystems": items}

    def names(self) -> dict[str, Any]:
        items = self.registry.names()
        return {"success": True, "count": len(items), "names": items}

    def get(self, ecosystem_id: str): return self.registry.get(ecosystem_id)
    def exists(self, ecosystem_id: str) -> bool: return self.registry.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        records = self.registry.list()
        nodes = {r["ecosystem_id"]: {**r, "children": []} for r in records}
        for record in records:
            parent = record.get("parent_id")
            if parent in nodes:
                nodes[parent]["children"].append(nodes[record["ecosystem_id"]])
        root = nodes.get(self.ROOT_ID)
        return {"success": root is not None, "tree": root}

    def connection_map(self) -> dict[str, Any]:
        records = self.registry.list()
        edges = [{"source": r["parent_id"], "target": r["ecosystem_id"],
                  "relationship": "CONTAINS"} for r in records if r.get("parent_id")]
        return {"success": True, "node_count": len(records),
                "edge_count": len(edges), "edges": edges}

EcosystemManager = GlobalEcosystemManager
__all__ = ["GlobalEcosystemManager", "EcosystemManager"]
