"""GLOBAL ECOSYSTEM MANAGER."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from backend.engines.global_ecosystem.models import EcosystemIdentity
from backend.engines.global_ecosystem.registry import GlobalEcosystemRegistry


class GlobalEcosystemManager:
    """Manage GLOBAL ECOSYSTEM identities and hierarchy."""

    def __init__(self) -> None:
        self.name = "GLOBAL ECOSYSTEM"
        self.version = "1.0.0"
        self.registry = GlobalEcosystemRegistry()
        self._register_default_ecosystems()

    def _register_default_ecosystems(self) -> None:
        """Register the initial ecosystem hierarchy."""

        ecosystems = [
            ("GLOBAL-ECOSYSTEM", "GLOBAL ECOSYSTEM", "ROOT", None),
            ("GLOBAL-SUPREME-ECOSYSTEM", "GLOBAL SUPREME ECOSYSTEM", "CORE", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-PEOPLE-ECOSYSTEM", "GLOBAL PEOPLE ECOSYSTEM", "PEOPLE", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-BUSINESS-ECOSYSTEM", "GLOBAL BUSINESS ECOSYSTEM", "BUSINESS", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-ENTREPRENEUR-ECOSYSTEM", "GLOBAL ENTREPRENEUR ECOSYSTEM", "ENTREPRENEUR", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-CLOUD-ECOSYSTEM", "GLOBAL CLOUD ECOSYSTEM", "CLOUD", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-CLOUD-STORAGE-ECOSYSTEM", "GLOBAL CLOUD STORAGE ECOSYSTEM", "CLOUD_STORAGE", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-STORAGE-ECOSYSTEM", "GLOBAL STORAGE ECOSYSTEM", "STORAGE", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-SERVER-ECOSYSTEM", "GLOBAL SERVER ECOSYSTEM", "SERVER", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-WEB-HOSTING-ECOSYSTEM", "GLOBAL WEB & HOSTING ECOSYSTEM", "WEB_HOSTING", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-SOCIAL-MEDIA-ECOSYSTEM", "GLOBAL SOCIAL MEDIA ECOSYSTEM", "SOCIAL_MEDIA", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-CREATOR-MEDIA-ECOSYSTEM", "GLOBAL CREATOR & MEDIA ECOSYSTEM", "CREATOR_MEDIA", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-ADULT-ENTERTAINMENT-ECOSYSTEM", "GLOBAL ADULT ENTERTAINMENT ECOSYSTEM", "ADULT_ENTERTAINMENT", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-AI-AUTOMATION-ECOSYSTEM", "GLOBAL AI & AUTOMATION ECOSYSTEM", "AI_AUTOMATION", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-PAYMENT-COMMERCE-ECOSYSTEM", "GLOBAL PAYMENT & COMMERCE ECOSYSTEM", "PAYMENT_COMMERCE", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-IDENTITY-SECURITY-ECOSYSTEM", "GLOBAL IDENTITY & SECURITY ECOSYSTEM", "IDENTITY_SECURITY", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-COMMUNICATION-ECOSYSTEM", "GLOBAL COMMUNICATION ECOSYSTEM", "COMMUNICATION", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-DATA-DATABASE-ECOSYSTEM", "GLOBAL DATA & DATABASE ECOSYSTEM", "DATA_DATABASE", "GLOBAL-ECOSYSTEM"),
            ("GLOBAL-DEVELOPER-ECOSYSTEM", "GLOBAL DEVELOPER ECOSYSTEM", "DEVELOPER", "GLOBAL-ECOSYSTEM"),
        ]

        for ecosystem_id, name, ecosystem_type, parent_id in ecosystems:
            self.registry.register(
                EcosystemIdentity(
                    ecosystem_id=ecosystem_id,
                    name=name,
                    ecosystem_type=ecosystem_type,
                    parent_id=parent_id,
                    capabilities=[],
                    metadata={},
                )
            )

    def register(self, ecosystem: dict[str, Any]) -> dict[str, Any]:
        """Register or update an ecosystem."""

        return self.registry.register(ecosystem)

    def status(self) -> dict[str, Any]:
        """Return overall ecosystem status."""

        return {
            "success": True,
            "name": self.name,
            "version": self.version,
            "status": "OPERATIONAL",
            "enabled": True,
            "ecosystem_count": self.registry.count(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def health(self) -> dict[str, Any]:
        """Return manager health."""

        return {
            "success": True,
            "service": self.name,
            "status": "HEALTHY",
            "registry_available": self.registry is not None,
            "ecosystem_count": self.registry.count(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def list(self) -> dict[str, Any]:
        """List registered ecosystems."""

        items = self.registry.list()
        return {
            "success": True,
            "count": len(items),
            "ecosystems": items,
        }

    def names(self) -> dict[str, Any]:
        """List registered ecosystem names."""

        names = self.registry.names()
        return {
            "success": True,
            "count": len(names),
            "names": names,
        }

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        """Get an ecosystem by ID or exact name."""

        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem exists."""

        return self.registry.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        """Build the nested ecosystem hierarchy."""

        items = self.registry.list()
        by_id = {item["ecosystem_id"]: item for item in items}

        def build_node(item: dict[str, Any]) -> dict[str, Any]:
            node = dict(item)
            node["children"] = [
                build_node(child)
                for child in items
                if child.get("parent_id") == item["ecosystem_id"]
            ]
            return node

        roots = [
            item for item in items
            if item.get("parent_id") is None
        ]

        return {
            "success": True,
            "count": len(roots),
            "tree": [build_node(root) for root in roots],
        }

    def connection_map(self) -> dict[str, Any]:
        """Return parent-child ecosystem relationships."""

        items = self.registry.list()
        connections = [
            {
                "parent_id": item.get("parent_id"),
                "ecosystem_id": item["ecosystem_id"],
                "name": item["name"],
            }
            for item in items
        ]

        return {
            "success": True,
            "count": len(connections),
            "connections": connections,
        }


# Backward compatibility.
EcosystemManager = GlobalEcosystemManager
