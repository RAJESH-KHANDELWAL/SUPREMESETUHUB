"""GLOBAL ECOSYSTEM hierarchy manager under CORE."""

from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.catalog import (
    ROOT_ID,
    get_catalog,
)
from backend.core.global_ecosystem.models import GlobalEcosystemIdentity
from backend.core.global_ecosystem.registry import GlobalEcosystemRegistry


class GlobalEcosystemManager:
    """Initialize and manage the canonical GLOBAL ECOSYSTEM hierarchy."""

    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.registry = GlobalEcosystemRegistry()
        self._initialize()

    @staticmethod
    def _to_identity(record: dict[str, Any]) -> GlobalEcosystemIdentity:
        """Convert a catalog record into the CORE identity model."""
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
        """Register the root first, then categories and registrations."""
        records = get_catalog()

        # The catalog orders records as root, categories, registrations.
        for record in records:
            identity = self._to_identity(record)
            result = self.registry.register(identity)

            if not result.get("success", False):
                raise RuntimeError(
                    "GLOBAL ECOSYSTEM initialization failed for "
                    f"{identity.ecosystem_id}: "
                    f"{result.get('error', 'REGISTRATION_FAILED')}"
                )

    def status(self) -> dict[str, Any]:
        """Return the current registry summary."""
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
        """Check registry structure without claiming external services work."""
        root_exists = self.registry.exists(self.ROOT_ID)
        core_exists = self.registry.exists("GLOBAL-CORE")

        return {
            "success": root_exists and core_exists,
            "root_exists": root_exists,
            "core_exists": core_exists,
            "registry_count": self.registry.count(),
            "status": (
                "FOUNDATION_READY"
                if root_exists and core_exists
                else "FOUNDATION_INCOMPLETE"
            ),
        }

    def list(self) -> dict[str, Any]:
        """List all registered ecosystem records."""
        ecosystems = self.registry.list()

        return {
            "success": True,
            "count": len(ecosystems),
            "ecosystems": ecosystems,
        }

    def names(self) -> dict[str, Any]:
        """List all registered ecosystem names."""
        names = self.registry.names()

        return {
            "success": True,
            "count": len(names),
            "names": names,
        }

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        """Find an ecosystem by its ID or supported name lookup."""
        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        """Return whether an ecosystem ID or supported name exists."""
        return self.registry.exists(ecosystem_id)

    def register(
        self,
        identity: GlobalEcosystemIdentity,
    ) -> dict[str, Any]:
        """Register an additional ecosystem through the CORE registry."""
        if identity.ecosystem_id == self.ROOT_ID:
            return {
                "success": False,
                "error": "ROOT_ALREADY_INITIALIZED",
            }

        if self.registry.exists(identity.ecosystem_id):
            return {
                "success": False,
                "error": "ECOSYSTEM_ALREADY_EXISTS",
                "ecosystem_id": identity.ecosystem_id,
            }

        if identity.parent_id and not self.registry.exists(identity.parent_id):
            return {
                "success": False,
                "error": "PARENT_NOT_FOUND",
                "parent_id": identity.parent_id,
            }

        return self.registry.register(identity)

    def tree(self) -> dict[str, Any]:
        """Return the ecosystem hierarchy as a nested tree."""
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
            if parent_id in by_id:
                by_id[parent_id]["children"].append(
                    by_id[record["ecosystem_id"]]
                )

        root = by_id.get(self.ROOT_ID)

        return {
            "success": root is not None,
            "tree": root,
        }

    def connection_map(self) -> dict[str, Any]:
        """Return parent-child relationships between ecosystem records."""
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
