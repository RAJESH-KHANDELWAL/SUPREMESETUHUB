"""Independent, thread-safe ENGINE ecosystem registry."""
from __future__ import annotations
from threading import RLock
from typing import Any
from .models import GlobalEcosystemIdentity, utc_now

class GlobalEcosystemRegistry:
    def __init__(self) -> None:
        self._records: dict[str, GlobalEcosystemIdentity] = {}
        self._lock = RLock()

    def register(self, identity: GlobalEcosystemIdentity | dict[str, Any]) -> dict[str, Any]:
        if isinstance(identity, dict):
            identity = GlobalEcosystemIdentity(**{
                key: identity[key] for key in (
                    "ecosystem_id", "name", "ecosystem_type", "repository_ref",
                    "status", "enabled", "capabilities", "metadata", "message",
                    "parent_id", "created_at", "updated_at"
                ) if key in identity
            })
        key, name = identity.ecosystem_id.strip(), identity.name.strip()
        if not key or not name:
            raise ValueError("ecosystem_id and name are required")
        if key == identity.parent_id:
            raise ValueError("An ecosystem cannot be its own parent")
        with self._lock:
            if identity.parent_id and identity.parent_id not in self._records:
                raise ValueError(f"Parent ecosystem not found: {identity.parent_id}")
            prior = self._records.get(key)
            if prior:
                identity.created_at = prior.created_at
            identity.ecosystem_id, identity.name = key, name
            identity.updated_at = utc_now()
            self._records[key] = identity
            return identity.to_dict()

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        key = ecosystem_id.strip()
        with self._lock:
            item = self._records.get(key)
            if item is None:
                folded = key.casefold()
                item = next((v for v in self._records.values() if v.name.casefold() == folded), None)
            return item.to_dict() if item else None

    def list(self) -> list[dict[str, Any]]:
        with self._lock:
            return [item.to_dict() for item in self._records.values()]

    def names(self) -> list[str]:
        with self._lock:
            return [item.name for item in self._records.values()]

    def exists(self, ecosystem_id: str) -> bool:
        return self.get(ecosystem_id) is not None

    def count(self) -> int:
        with self._lock:
            return len(self._records)

    def clear(self) -> None:
        with self._lock:
            self._records.clear()

EcosystemRegistry = GlobalEcosystemRegistry
