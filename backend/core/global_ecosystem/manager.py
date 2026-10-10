
"""GLOBAL ECOSYSTEM hierarchy manager."""

from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.models import (
    GlobalEcosystemIdentity,
)
from backend.core.global_ecosystem.registry import (
    GlobalEcosystemRegistry,
    utc_now,
)


class GlobalEcosystemManager:
    """Manage the root ecosystem and its child modules."""

    ROOT_ID = "GLOBAL-ECOSYSTEM"
    ROOT_NAME = "GLOBAL ECOSYSTEM"
    VERSION = "1.0.0"

    MODULES = [
        ("GLOBAL-CORE", "GLOBAL CORE", "CORE"),
        ("GLOBAL-DATABASE", "GLOBAL DATABASE", "DATABASE"),
        ("GLOBAL-STORAGE", "GLOBAL STORAGE", "STORAGE"),
        ("GLOBAL-IDENTITY-SECURITY", "GLOBAL IDENTITY & SECURITY", "SECURITY"),
        ("GLOBAL-API-INTEGRATION", "GLOBAL API & INTEGRATION", "API"),
        ("GLOBAL-INFRASTRUCTURE", "GLOBAL INFRASTRUCTURE", "INFRASTRUCTURE"),
        ("GLOBAL-CLOUD", "GLOBAL CLOUD", "CLOUD"),
        ("GLOBAL-CLOUD-STORAGE", "GLOBAL CLOUD STORAGE", "CLOUD_STORAGE"),
        ("GLOBAL-SERVER", "GLOBAL SERVER", "SERVER"),
        ("GLOBAL-DOMAIN", "GLOBAL DOMAIN", "DOMAIN"),
        ("GLOBAL-DNS", "GLOBAL DNS", "DNS"),
        ("GLOBAL-IP-ADDRESS", "GLOBAL IP ADDRESS", "NETWORK"),
        ("GLOBAL-SSH", "GLOBAL SSH", "REMOTE_ACCESS"),
        ("GLOBAL-SSL", "GLOBAL SSL", "CERTIFICATES"),
        ("GLOBAL-WEB-HOSTING", "GLOBAL WEB & HOSTING", "HOSTING"),
        ("GLOBAL-PEOPLE", "GLOBAL PEOPLE", "PEOPLE"),
        ("GLOBAL-BUSINESS", "GLOBAL BUSINESS", "BUSINESS"),
        ("GLOBAL-ENTREPRENEUR", "GLOBAL ENTREPRENEUR", "ENTREPRENEUR"),
        ("GLOBAL-PAYMENT-COMMERCE", "GLOBAL PAYMENT & COMMERCE", "PAYMENTS"),
        ("GLOBAL-BILLING", "GLOBAL BILLING", "BILLING"),
        ("GLOBAL-MONITORING-OPERATIONS", "GLOBAL MONITORING & OPERATIONS", "OPERATIONS"),
        ("GLOBAL-AI-AUTOMATION", "GLOBAL AI & AUTOMATION", "AI"),
        ("GLOBAL-SOCIAL-MEDIA", "GLOBAL SOCIAL MEDIA", "SOCIAL"),
        ("GLOBAL-CREATOR-MEDIA", "GLOBAL CREATOR & MEDIA", "MEDIA"),
        ("GLOBAL-COMMUNICATION", "GLOBAL COMMUNICATION", "COMMUNICATION"),
        ("GLOBAL-DEVELOPER", "GLOBAL DEVELOPER", "DEVELOPER"),
    ]

    def __init__(self) -> None:
        self.registry = GlobalEcosystemRegistry()
        self._initialize()

    def _initialize(self) -> None:
        """Register the root before registering its children."""

        self.registry.register(
            GlobalEcosystemIdentity(
                ecosystem_id=self.ROOT_ID,
                name=self.ROOT_NAME,
                ecosystem_type="ROOT",
                status="FOUNDATION",
                enabled=True,
                capabilities=["registry", "hierarchy", "management"],
                metadata={"version": self.VERSION},
            )
        )

        for ecosystem_id, name, ecosystem_type in self.MODULES:
            self.registry.register(
                GlobalEcosystemIdentity(
                    ecosystem_id=ecosystem_id,
                    name=name,
                    ecosystem_type=ecosystem_type,
                    parent_id=self.ROOT_ID,
                    status="REGISTERED",
                    enabled=True,
                    capabilities=["registration"],
                    metadata={"implementation_status": "FOUNDATION"},
                )
            )

    def status(self) -> dict[str, Any]:
        records = self.registry.list()

        return {
            "success": True,
            "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME,
            "status": "FOUNDATION",
            "version": self.VERSION,
            "registered_ecosystems": len(records),
            "enabled_ecosystems": sum(
                1 for record in records if record["enabled"]
            ),
            "message": (
                "Ecosystem modules are registered. "
                "Individual services require implementation and health checks."
            ),
            "checked_at": utc_now(),
        }

    def health(self) -> dict[str, Any]:
        root_exists = self.registry.exists(self.ROOT_ID)
        core_exists = self.registry.exists("GLOBAL-CORE")

        return {
            "success": root_exists and core_exists,
            "ecosystem_id": self.ROOT_ID,
            "status": (
                "FOUNDATION_READY"
                if root_exists and core_exists
                else "NOT_READY"
            ),
            "checks": {
                "root_registered": root_exists,
                "core_registered": core_exists,
                "registry_available": True,
            },
            "checked_at": utc_now(),
        }

    def list(self) -> dict[str, Any]:
        records = self.registry.list()
        return {
            "success": True,
            "count": len(records),
            "ecosystems": records,
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
        if identity.ecosystem_id == self.ROOT_ID:
            raise ValueError("The root ecosystem is already registered")

        if identity.parent_id and not self.registry.exists(
            identity.parent_id
        ):
            raise ValueError(
                f"Parent ecosystem not found: {identity.parent_id}"
            )

        return self.registry.register(identity)

    def tree(self) -> dict[str, Any]:
        records = self.registry.list()
        records_by_id = {
            record["ecosystem_id"]: record
            for record in records
        }

        if self.ROOT_ID not in records_by_id:
            return {
                "success": False,
                "error": "ROOT_ECOSYSTEM_NOT_FOUND",
                "tree": None,
            }

        def build_node(ecosystem_id: str) -> dict[str, Any]:
            node = dict(records_by_id[ecosystem_id])
            child_ids = [
                record["ecosystem_id"]
                for record in records
                if record.get("parent_id") == ecosystem_id
            ]
            node["children"] = [
                build_node(child_id) for child_id in child_ids
            ]
            return node

        return {
            "success": True,
            "root": self.ROOT_ID,
            "tree": build_node(self.ROOT_ID),
        }

    def connection_map(self) -> dict[str, Any]:
        records = self.registry.list()
        connections = [
            {
                "parent_id": record["parent_id"],
                "child_id": record["ecosystem_id"],
                "relationship": "CONTAINS",
            }
            for record in records
            if record.get("parent_id")
        ]

        return {
            "success": True,
            "root": self.ROOT_ID,
            "node_count": len(records),
            "connection_count": len(connections),
            "connections": connections,
        }


EcosystemManager = GlobalEcosystemManager
