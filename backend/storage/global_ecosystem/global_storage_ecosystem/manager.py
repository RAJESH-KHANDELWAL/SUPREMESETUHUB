"""Independent GLOBAL STORAGE ECOSYSTEM manager."""
from datetime import datetime, timezone
from typing import Any
from .ecosystem_registry import StorageEcosystemRegistry
from .models import StorageEcosystemIdentity
from .registry import list_providers, get_provider

ROOT_ID = "GLOBAL-STORAGE-ECOSYSTEM"

class GlobalStorageEcosystemManager:
    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL STORAGE ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.registry = StorageEcosystemRegistry()
        self._initialize()

    def _initialize(self) -> None:
        self.registry.register(StorageEcosystemIdentity(
            ecosystem_id=self.ROOT_ID, name=self.ROOT_NAME,
            ecosystem_type="STORAGE_ROOT",
            capabilities=["OBJECT_STORAGE", "FILE_STORAGE", "PROVIDER_DISCOVERY"],
            metadata={"layer": "STORAGE", "independent": True}))
        for provider in list_providers():
            pid = provider["provider_id"]
            self.registry.register(StorageEcosystemIdentity(
                ecosystem_id="GLOBAL-" + pid.upper().replace("_", "-") + "-STORAGE-ECOSYSTEM",
                name="GLOBAL " + provider["name"].upper() + " STORAGE ECOSYSTEM",
                ecosystem_type="STORAGE_PROVIDER", provider_id=pid,
                parent_id=self.ROOT_ID, status="NOT_CONFIGURED",
                capabilities=list(provider["capabilities"]),
                metadata={"connection_state": "NOT_CONFIGURED"}))

    def status(self) -> dict[str, Any]:
        ready = self.registry.exists(self.ROOT_ID)
        return {"success": ready, "ecosystem_id": self.ROOT_ID, "name": self.ROOT_NAME,
                "version": self.VERSION, "status": "FOUNDATION_READY" if ready else "NOT_INITIALIZED",
                "count": self.registry.count(), "timestamp": datetime.now(timezone.utc).isoformat(),
                "layer": "STORAGE", "independent": True}

    def health(self) -> dict[str, Any]:
        ready = self.registry.exists(self.ROOT_ID)
        return {"success": ready, "service": self.ROOT_NAME,
                "status": "HEALTHY" if ready else "DEGRADED",
                "registry_available": self.registry is not None,
                "registry_count": self.registry.count(),
                "provider_connections_verified": False,
                "note": "Live provider health requires configured provider adapters."}

    def list(self) -> dict[str, Any]:
        values = self.registry.list()
        return {"success": True, "count": len(values), "ecosystems": values}

    def names(self) -> dict[str, Any]:
        values = self.registry.names()
        return {"success": True, "count": len(values), "names": values}

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        return self.registry.exists(ecosystem_id)

    def register(self, identity: StorageEcosystemIdentity | dict[str, Any]) -> dict[str, Any]:
        try:
            item = identity if isinstance(identity, StorageEcosystemIdentity) else StorageEcosystemIdentity(**identity)
            return {"success": True, "ecosystem": self.registry.register(item)}
        except (TypeError, ValueError, KeyError) as exc:
            return {"success": False, "error": "REGISTRATION_FAILED", "message": str(exc)}

    def providers(self) -> dict[str, Any]:
        values = list_providers()
        return {"success": True, "count": len(values), "providers": values}

    def get_provider(self, provider_id: str) -> dict[str, Any]:
        return get_provider(provider_id)

    def tree(self) -> dict[str, Any]:
        values = self.registry.list()
        nodes = {item["ecosystem_id"]: {**item, "children": []} for item in values}
        for item in values:
            parent = item.get("parent_id")
            if parent in nodes:
                nodes[parent]["children"].append(nodes[item["ecosystem_id"]])
        root = nodes.get(self.ROOT_ID)
        return {"success": root is not None, "tree": root}

    def connection_map(self) -> dict[str, Any]:
        values = self.registry.list()
        edges = [{"source": item["parent_id"], "target": item["ecosystem_id"],
                  "relationship": "CONTAINS"} for item in values if item.get("parent_id")]
        return {"success": True, "node_count": len(values),
                "edge_count": len(edges), "edges": edges}

StorageEcosystemManager = GlobalStorageEcosystemManager
