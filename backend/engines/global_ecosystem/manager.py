"""GLOBAL ECOSYSTEM MANAGER."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class GlobalEcosystemManager:
    """Manage identities, status, and connections for the GLOBAL ECOSYSTEM."""

    def __init__(self) -> None:
        self.name = "GLOBAL ECOSYSTEM"
        self.version = "1.0.0"
        self._ecosystems: dict[str, dict[str, Any]] = {}
        self._register_default_ecosystems()

    def _register_default_ecosystems(self) -> None:
        """Register the initial ecosystem hierarchy."""

        ecosystems = [
            {
                "ecosystem_id": "GLOBAL-ECOSYSTEM",
                "name": "GLOBAL ECOSYSTEM",
                "ecosystem_type": "ROOT",
                "parent_id": None,
                "capabilities": ["registry", "status", "health", "hierarchy"],
            },
            {
                "ecosystem_id": "GLOBAL-SUPREME-ECOSYSTEM",
                "name": "GLOBAL SUPREME ECOSYSTEM",
                "ecosystem_type": "CORE",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["ecosystem-management", "coordination"],
            },
            {
                "ecosystem_id": "GLOBAL-PEOPLE-ECOSYSTEM",
                "name": "GLOBAL PEOPLE ECOSYSTEM",
                "ecosystem_type": "PEOPLE",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["people", "profiles"],
            },
            {
                "ecosystem_id": "GLOBAL-BUSINESS-ECOSYSTEM",
                "name": "GLOBAL BUSINESS ECOSYSTEM",
                "ecosystem_type": "BUSINESS",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["business", "organizations"],
            },
            {
                "ecosystem_id": "GLOBAL-ENTREPRENEUR-ECOSYSTEM",
                "name": "GLOBAL ENTREPRENEUR ECOSYSTEM",
                "ecosystem_type": "ENTREPRENEUR",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["entrepreneurship", "business-tools"],
            },
            {
                "ecosystem_id": "GLOBAL-CLOUD-ECOSYSTEM",
                "name": "GLOBAL CLOUD ECOSYSTEM",
                "ecosystem_type": "CLOUD",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["cloud", "provider-management"],
            },
            {
                "ecosystem_id": "GLOBAL-CLOUD-STORAGE-ECOSYSTEM",
                "name": "GLOBAL CLOUD STORAGE ECOSYSTEM",
                "ecosystem_type": "CLOUD_STORAGE",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["cloud-storage", "storage-configuration"],
            },
            {
                "ecosystem_id": "GLOBAL-STORAGE-ECOSYSTEM",
                "name": "GLOBAL STORAGE ECOSYSTEM",
                "ecosystem_type": "STORAGE",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["storage", "file-management"],
            },
            {
                "ecosystem_id": "GLOBAL-SERVER-ECOSYSTEM",
                "name": "GLOBAL SERVER ECOSYSTEM",
                "ecosystem_type": "SERVER",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["server-management"],
            },
            {
                "ecosystem_id": "GLOBAL-WEB-HOSTING-ECOSYSTEM",
                "name": "GLOBAL WEB & HOSTING ECOSYSTEM",
                "ecosystem_type": "WEB_HOSTING",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["web", "hosting", "domains"],
            },
            {
                "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-ECOSYSTEM",
                "name": "GLOBAL SOCIAL MEDIA ECOSYSTEM",
                "ecosystem_type": "SOCIAL_MEDIA",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["social-media", "publishing"],
            },
            {
                "ecosystem_id": "GLOBAL-CREATOR-MEDIA-ECOSYSTEM",
                "name": "GLOBAL CREATOR & MEDIA ECOSYSTEM",
                "ecosystem_type": "CREATOR_MEDIA",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["content-creation", "media"],
            },
            {
                "ecosystem_id": "GLOBAL-ADULT-ENTERTAINMENT-ECOSYSTEM",
                "name": "GLOBAL ADULT ENTERTAINMENT ECOSYSTEM",
                "ecosystem_type": "ADULT_ENTERTAINMENT",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": [
                    "lawful-adult-content",
                    "age-verification",
                    "consent-and-rights-compliance",
                ],
            },
            {
                "ecosystem_id": "GLOBAL-AI-AUTOMATION-ECOSYSTEM",
                "name": "GLOBAL AI & AUTOMATION ECOSYSTEM",
                "ecosystem_type": "AI_AUTOMATION",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["ai", "automation"],
            },
            {
                "ecosystem_id": "GLOBAL-PAYMENT-COMMERCE-ECOSYSTEM",
                "name": "GLOBAL PAYMENT & COMMERCE ECOSYSTEM",
                "ecosystem_type": "PAYMENT_COMMERCE",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["payments", "commerce"],
            },
            {
                "ecosystem_id": "GLOBAL-IDENTITY-SECURITY-ECOSYSTEM",
                "name": "GLOBAL IDENTITY & SECURITY ECOSYSTEM",
                "ecosystem_type": "IDENTITY_SECURITY",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["identity", "security"],
            },
            {
                "ecosystem_id": "GLOBAL-COMMUNICATION-ECOSYSTEM",
                "name": "GLOBAL COMMUNICATION ECOSYSTEM",
                "ecosystem_type": "COMMUNICATION",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["messaging", "communication"],
            },
            {
                "ecosystem_id": "GLOBAL-DATA-DATABASE-ECOSYSTEM",
                "name": "GLOBAL DATA & DATABASE ECOSYSTEM",
                "ecosystem_type": "DATA_DATABASE",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["data", "database"],
            },
            {
                "ecosystem_id": "GLOBAL-DEVELOPER-ECOSYSTEM",
                "name": "GLOBAL DEVELOPER ECOSYSTEM",
                "ecosystem_type": "DEVELOPER",
                "parent_id": "GLOBAL-ECOSYSTEM",
                "capabilities": ["development", "integrations"],
            },
        ]

        for ecosystem in ecosystems:
            self.register(ecosystem)

    def register(self, ecosystem: dict[str, Any]) -> dict[str, Any]:
        """Register an ecosystem or update an existing entry."""

        ecosystem_id = str(ecosystem.get("ecosystem_id", "")).strip()

        if not ecosystem_id:
            raise ValueError("ecosystem_id is required")

        existing = self._ecosystems.get(ecosystem_id, {})

        record = {
            **existing,
            **ecosystem,
            "ecosystem_id": ecosystem_id,
            "status": ecosystem.get("status", existing.get("status", "REGISTERED")),
            "enabled": ecosystem.get("enabled", existing.get("enabled", True)),
            "metadata": ecosystem.get("metadata", existing.get("metadata", {})),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }

        self._ecosystems[ecosystem_id] = record
        return dict(record)

    def status(self) -> dict[str, Any]:
        """Return the overall ecosystem status."""

        return {
            "success": True,
            "name": self.name,
            "version": self.version,
            "status": "OPERATIONAL",
            "enabled": True,
            "ecosystem_count": len(self._ecosystems),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def health(self) -> dict[str, Any]:
        """Return a lightweight health check."""

        return {
            "success": True,
            "service": self.name,
            "status": "HEALTHY",
            "registry_available": isinstance(self._ecosystems, dict),
            "ecosystem_count": len(self._ecosystems),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def list(self) -> dict[str, Any]:
        """List all registered ecosystems."""

        items = [dict(item) for item in self._ecosystems.values()]

        return {
            "success": True,
            "count": len(items),
            "ecosystems": items,
        }

    def names(self) -> dict[str, Any]:
        """Return registered ecosystem names."""

        names = [
            item["name"]
            for item in self._ecosystems.values()
        ]

        return {
            "success": True,
            "count": len(names),
            "names": names,
        }

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        """Find an ecosystem by ID or exact name."""

        search_value = ecosystem_id.strip()

        if not search_value:
            return None

        record = self._ecosystems.get(search_value)

        if record is None:
            normalized = search_value.casefold()
            record = next(
                (
                    item
                    for item in self._ecosystems.values()
                    if item["name"].casefold() == normalized
                ),
                None,
            )

        return dict(record) if record is not None else None

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem exists."""

        return self.get(ecosystem_id) is not None

    def tree(self) -> dict[str, Any]:
        """Return the ecosystem hierarchy as a nested tree."""

        records = list(self._ecosystems.values())

        def build_node(record: dict[str, Any]) -> dict[str, Any]:
            node = dict(record)
            node["children"] = [
                build_node(child)
                for child in records
                if child.get("parent_id") == record["ecosystem_id"]
            ]
            return node

        roots = [
            record
            for record in records
            if record.get("parent_id") is None
        ]

        return {
            "success": True,
            "count": len(roots),
            "tree": [build_node(root) for root in roots],
        }

    def connection_map(self) -> dict[str, Any]:
        """Return parent-child relationships between ecosystems."""

        connections = [
            {
                "parent_id": record.get("parent_id"),
                "ecosystem_id": record["ecosystem_id"],
                "name": record["name"],
            }
            for record in self._ecosystems.values()
        ]

        return {
            "success": True,
            "count": len(connections),
            "connections": connections,
        }


# Backward-compatible class name.
EcosystemManager = GlobalEcosystemManager
