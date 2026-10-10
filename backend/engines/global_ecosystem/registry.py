"""GLOBAL ECOSYSTEM registry."""

from __future__ import annotations

from typing import Any

from backend.engines.global_ecosystem.models import EcosystemIdentity


class GlobalEcosystemRegistry:
    """Store and retrieve GLOBAL ECOSYSTEM identities."""

    def __init__(self) -> None:
        self._records: dict[str, EcosystemIdentity] = {}

    def register(
        self,
        identity: EcosystemIdentity | dict[str, Any],
    ) -> dict[str, Any]:
        """Register an identity or update an existing identity."""

        if isinstance(identity, dict):
            identity = EcosystemIdentity(
                ecosystem_id=str(identity.get("ecosystem_id", "")).strip(),
                name=str(identity.get("name", "")).strip(),
                ecosystem_type=str(
                    identity.get("ecosystem_type", "GENERAL")
                ).strip(),
                repository_ref=identity.get("repository_ref"),
                status=str(identity.get("status", "REGISTERED")),
                enabled=bool(identity.get("enabled", True)),
                capabilities=list(identity.get("capabilities", [])),
                metadata=dict(identity.get("metadata", {})),
                message=identity.get("message"),
                parent_id=identity.get("parent_id"),
                created_at=identity.get(
                    "created_at",
                    EcosystemIdentity.__dataclass_fields__["created_at"].default_factory(),
                ),
            )

        if not identity.ecosystem_id:
            raise ValueError("ecosystem_id is required")

        if not identity.name:
            raise ValueError("name is required")

        existing = self._records.get(identity.ecosystem_id)

        if existing:
            identity.created_at = existing.created_at

        from datetime import datetime, timezone

        identity.updated_at = datetime.now(timezone.utc).isoformat()
        self._records[identity.ecosystem_id] = identity

        return identity.to_dict()

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        """Retrieve an identity by ID or exact name."""

        search_value = ecosystem_id.strip()

        if not search_value:
            return None

        identity = self._records.get(search_value)

        if identity is None:
            normalized = search_value.casefold()
            identity = next(
                (
                    item
                    for item in self._records.values()
                    if item.name.casefold() == normalized
                ),
                None,
            )

        return identity.to_dict() if identity else None

    def list(self) -> list[dict[str, Any]]:
        """Return all registered identities."""

        return [
            identity.to_dict()
            for identity in self._records.values()
        ]

    def names(self) -> list[str]:
        """Return all registered identity names."""

        return [
            identity.name
            for identity in self._records.values()
        ]

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an identity exists."""

        return self.get(ecosystem_id) is not None

    def count(self) -> int:
        """Return the number of registered identities."""

        return len(self._records)

    def clear(self) -> None:
        """Clear all registered identities."""

        self._records.clear()


# Backward-compatible alias.
EcosystemRegistry = GlobalEcosystemRegistry
