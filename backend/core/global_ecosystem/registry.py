
"""GLOBAL ECOSYSTEM registry."""

from __future__ import annotations

from datetime import datetime, timezone
from threading import RLock
from typing import Any

from backend.core.global_ecosystem.models import (
    GlobalEcosystemIdentity,
)


def utc_now() -> str:
    """Return the current UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


class GlobalEcosystemRegistry:
    """Register and retrieve GLOBAL ECOSYSTEM modules."""

    def __init__(self) -> None:
        self._records: dict[str, GlobalEcosystemIdentity] = {}
        self._lock = RLock()

    def register(
        self,
        identity: GlobalEcosystemIdentity,
    ) -> dict[str, Any]:
        """Register or update an ecosystem identity."""

        ecosystem_id = identity.ecosystem_id.strip()
        name = identity.name.strip()

        if not ecosystem_id:
            raise ValueError("ecosystem_id is required")

        if not name:
            raise ValueError("name is required")

        if ecosystem_id == identity.parent_id:
            raise ValueError("An ecosystem cannot be its own parent")

        with self._lock:
            if identity.parent_id:
                if identity.parent_id not in self._records:
                    raise ValueError(
                        f"Parent ecosystem not found: {identity.parent_id}"
                    )

            existing = self._records.get(ecosystem_id)

            if existing is not None:
                identity.metadata.setdefault(
                    "created_at",
                    existing.metadata.get("created_at", utc_now()),
                )
            else:
                identity.metadata.setdefault("created_at", utc_now())

            identity.metadata["updated_at"] = utc_now()
            identity.ecosystem_id = ecosystem_id
            identity.name = name

            self._records[ecosystem_id] = identity

            return identity.to_dict()

    def get(
        self,
        ecosystem_id: str,
    ) -> dict[str, Any] | None:
        """Find an ecosystem by ID or exact name."""

        key = ecosystem_id.strip()

        if not key:
            return None

        with self._lock:
            record = self._records.get(key)

            if record is None:
                normalized = key.casefold()
                record = next(
                    (
                        item
                        for item in self._records.values()
                        if item.name.casefold() == normalized
                    ),
                    None,
                )

            return record.to_dict() if record else None

    def list(self) -> list[dict[str, Any]]:
        """Return all registered ecosystems."""
        with self._lock:
            return [
                record.to_dict()
                for record in self._records.values()
            ]

    def names(self) -> list[str]:
        """Return all registered ecosystem names."""
        with self._lock:
            return [
                record.name
                for record in self._records.values()
            ]

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem exists."""
        return self.get(ecosystem_id) is not None

    def count(self) -> int:
        """Return the number of registered ecosystems."""
        with self._lock:
            return len(self._records)

    def clear(self) -> None:
        """Clear the in-memory registry."""
        with self._lock:
            self._records.clear()


EcosystemRegistry = GlobalEcosystemRegistry
