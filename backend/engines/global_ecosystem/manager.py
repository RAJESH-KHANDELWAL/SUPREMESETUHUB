
"""GLOBAL ECOSYSTEM manager."""

from __future__ import annotations

from .registry import (
    GLOBAL_ECOSYSTEM_ID,
    GLOBAL_ECOSYSTEM_NAME,
    GlobalEcosystemRegistry,
)


class GlobalEcosystemManager:
    """Manage the GLOBAL ECOSYSTEM hierarchy and registry."""

    def __init__(self) -> None:
        self.registry = GlobalEcosystemRegistry()

    def status(self) -> dict:
        """Return master ecosystem status."""

        registry_status = self.registry.status() if hasattr(
            self.registry, "status"
        ) else {
            "registry_status": "READY",
            "total_ecosystems": len(self.registry.list()),
        }

        return {
            "success": True,
            "ecosystem_id": GLOBAL_ECOSYSTEM_ID,
            "name": GLOBAL_ECOSYSTEM_NAME,
            "status": "REGISTERED",
            "manager": "GlobalEcosystemManager",
            "registry": registry_status,
            "external_connections": "NOT_VERIFIED",
        }

    def health(self) -> dict:
        """Report registry health without claiming external connectivity."""

        entries = self.registry.list()

        return {
            "success": True,
            "ecosystem": GLOBAL_ECOSYSTEM_NAME,
            "healthy": True,
            "registry_available": True,
            "total_ecosystems": len(entries),
            "external_connections_verified": False,
        }

    def list(self) -> list:
        """Return all registered ecosystem records."""

        return [
            identity.to_dict()
            for identity in self.registry.list()
        ]

    def names(self) -> list:
        """Return registered ecosystem names."""

        return self.registry.names()

    def get(self, ecosystem_id: str) -> dict:
        """Return one ecosystem as a dictionary."""

        return self.registry.get(ecosystem_id).to_dict()

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem ID is registered."""

        return self.registry.exists(ecosystem_id)

    def tree(self) -> dict:
        """Return the master hierarchy."""

        if hasattr(self.registry, "tree"):
            return self.registry.tree()

        root = self.registry.get(GLOBAL_ECOSYSTEM_ID).to_dict()
        root["children"] = [
            identity.to_dict()
            for identity in self.registry.list()
            if getattr(identity, "parent_id", None)
            == GLOBAL_ECOSYSTEM_ID
        ]
        return root

    def connection_map(self) -> dict:
        """Return the ecosystem relationship map."""

        entries = self.registry.list()

        return {
            "central_platform": "SUPREMESETUHUB",
            "master_ecosystem": GLOBAL_ECOSYSTEM_NAME,
            "master_ecosystem_id": GLOBAL_ECOSYSTEM_ID,
            "registered_ecosystems": len(entries),
            "connection_status": (
                "STRUCTURE_REGISTERED_EXTERNAL_CONNECTIONS_PENDING"
            ),
            "external_connections_verified": False,
        }


# Backward-compatible class name for existing integrations.
EcosystemManager = GlobalEcosystemManager
