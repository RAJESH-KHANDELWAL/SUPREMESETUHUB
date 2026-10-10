"""GLOBAL ECOSYSTEM hierarchy manager under CORE."""

from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.catalog import ROOT_ID, get_catalog
from backend.core.global_ecosystem.models import GlobalEcosystemIdentity
from backend.core.global_ecosystem.registry import GlobalEcosystemRegistry


class GlobalEcosystemManager:
    """Manage the canonical GLOBAL ECOSYSTEM hierarchy."""

    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL ECOSYSTEM"
    VERSION = "1.0.0"
    CORE_ID = "GLOBAL-SUPREME-ECOSYSTEM"

    def __init__(self) -> None:
        self.registry = GlobalEcosystemRegistry()
        self._initialize()

    @staticmethod
    def _to_identity(record: dict[str, Any]) -> GlobalEcosystemIdentity:
        return GlobalEcosystemIdentity(
            ecosystem_id=record["ecosystem_id"],
            name=record["name"],
            ecosystem_type=record["ecosystem_type"],
            repository_ref=record.get("repository_ref"),
            status=record.get("status", "REGISTERED"),
            enabled=record.get("enabled", True),
            capabilities=list(record.get("capabilities", [])),
            metadata=dict(record.get("metadata", {})),
            message=record.get("message"),
            parent_id=record.get("parent_id"),
        )

    def _initialize(self) -> None:
        """Register catalog entries in parent-first order."""
        records = get_catalog()

        if not records:
            raise RuntimeError("GLOBAL ECOSYSTEM catalog is empty")

        registered_ids: set[str] = set()

        for record in records:
            identity = self._to_identity(record)
            ecosystem_id = identity.ecosystem_id

            if ecosystem_id in registered_ids:
                raise RuntimeError(
                    f"Duplicate ecosystem ID in catalog: {ecosystem_id}"
                )

            parent_id = identity.parent_id

            if parent_id and parent_id not in registered_ids:
                raise RuntimeError(
                    f"Parent must appear before child: "
                    f"{ecosystem_id} -> {parent_id}"
                )

            try:
                self.registry.register(identity)
            except (ValueError, KeyError) as exc:
                raise RuntimeError(
                    f"Initialization failed for {ecosystem_id}: {exc}"
                ) from exc

            registered_ids.add(ecosystem_id)

        if self.ROOT_ID not in registered_ids:
            raise RuntimeError("GLOBAL ECOSYSTEM root is missing")

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)

        return {
            "success": root is not None,
            "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME,
            "version": self.VERSION,
            "status": "FOUNDATION" if root else "NOT_INITIALIZED",
            "count": self.registry.count(),
        }

    def health(self) -> dict[str, Any]:
        root_exists = self.registry.exists(self.ROOT_ID)
        core_exists = self.registry.exists(self.CORE_ID)
        healthy = root_exists and core_exists

        return {
            "success": healthy,
            "root_exists": root_exists,
            "core_exists": core_exists,
            "registry_count": self.registry.count(),
            "status": (
                "FOUNDATION_READY"
                if healthy
                else "FOUNDATION_INCOMPLETE"
            ),
        }

    def list(self) -> dict[str, Any]:
        ecosystems = self.registry.list()

        return {
            "success": True,
            "count": len(ecosystems),
            "ecosystems": ecosystems,
        }

    def names(self) -> dict[str, Any]:
        names = self.registry.names()

        return {
            "success": True,
            "count": len(names),
            "names": names,
        }

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        return self.registry.exists(ecosystem_id)

    def register(
        self,
        identity: GlobalEcosystemIdentity,
    ) -> dict[str, Any]:
        ecosystem_id = identity.ecosystem_id.strip()

        if not ecosystem_id:
            return {
                "success": False,
                "error": "ECOSYSTEM_ID_REQUIRED",
            }

        if ecosystem_id == self.ROOT_ID:
            return {
                "success": False,
                "error": "ROOT_ALREADY_INITIALIZED",
            }

        if self.registry.exists(ecosystem_id):
            return {
                "success": False,
                "error": "ECOSYSTEM_ALREADY_EXISTS",
                "ecosystem_id": ecosystem_id,
            }

        if not identity.parent_id:
            identity.parent_id = self.ROOT_ID

        if not self.registry.exists(identity.parent_id):
            return {
                "success": False,
                "error": "PARENT_NOT_FOUND",
                "parent_id": identity.parent_id,
            }

        try:
            registered = self.registry.register(identity)
        except (ValueError, KeyError) as exc:
            return {
                "success": False,
                "error": "REGISTRATION_FAILED",
                "message": str(exc),
                "ecosystem_id": ecosystem_id,
            }

        return {
            "success": True,
            "ecosystem": registered,
        }

    def tree(self) -> dict[str, Any]:
        records = self.registry.list()

        by_id = {
            record["ecosystem_id"]: {
                **record,
                "children": [],
            }
            for record in records
        }

        for record in records:
            parent_id = record.get("parent_id")
            ecosystem_id = record["ecosystem_id"]

            if parent_id in by_id:
                by_id[parent_id]["children"].append(
                    by_id[ecosystem_id]
                )

        root = by_id.get(self.ROOT_ID)

        return {
            "success": root is not None,
            "tree": root,
        }

    def connection_map(self) -> dict[str, Any]:
        records = self.registry.list()

        edges = [
            {
                "source": record["parent_id"],
                "target": record["ecosystem_id"],
                "relationship": "CONTAINS",
            }
            for record in records
            if record.get("parent_id")
        ]

        return {
            "success": True,
            "node_count": len(records),
            "edge_count": len(edges),
            "edges": edges,
        }


EcosystemManager = GlobalEcosystemManager
