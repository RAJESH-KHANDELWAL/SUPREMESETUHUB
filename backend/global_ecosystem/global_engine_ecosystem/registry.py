"""Thread-safe registry for the People, Work, and Business Global Engine."""
from __future__ import annotations

from threading import RLock
from typing import Any

from .manager import EcosystemIdentity, ROOT, ROOT_ID, SUPPORTED_DOMAINS, utc_now


class GlobalEcosystemRegistry:
    def __init__(self) -> None:
        self._records: dict[str, EcosystemIdentity] = {}
        self._lock = RLock()

    def register(self, identity: EcosystemIdentity | dict[str, Any]) -> dict[str, Any]:
        if isinstance(identity, dict):
            identity = EcosystemIdentity(**identity)
        key, name = identity.ecosystem_id.strip(), identity.name.strip()
        domain = identity.ecosystem_type.strip().upper()
        if not key or not name:
            raise ValueError("ecosystem_id and name are required")
        if domain not in SUPPORTED_DOMAINS:
            raise ValueError(f"Unsupported domain: {domain}")
        if key == identity.parent_id:
            raise ValueError("An ecosystem cannot be its own parent")
        with self._lock:
            if identity.parent_id not in (None, ROOT_ID) and identity.parent_id not in self._records:
                raise ValueError(f"Parent ecosystem not found: {identity.parent_id}")
            prior = self._records.get(key)
            if prior:
                identity.created_at = prior.created_at
            identity.ecosystem_id = key
            identity.name = name
            identity.ecosystem_type = domain
            identity.updated_at = utc_now()
            self._records[key] = identity
            return identity.to_dict()

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        key = ecosystem_id.strip()
        if key == ROOT_ID:
            return dict(ROOT)
        with self._lock:
            item = self._records.get(key)
            if item is None:
                folded = key.casefold()
                item = next((v for v in self._records.values() if v.name.casefold() == folded), None)
            return item.to_dict() if item else None

    def list(self, domain: str | None = None) -> list[dict[str, Any]]:
        with self._lock:
            items = list(self._records.values())
            if domain is not None:
                selected = domain.strip().upper()
                if selected not in SUPPORTED_DOMAINS:
                    raise ValueError(f"Unsupported domain: {selected}")
                items = [item for item in items if item.ecosystem_type == selected]
            return [item.to_dict() for item in items]

    def count(self, domain: str | None = None) -> int:
        return len(self.list(domain))

    def clear(self) -> None:
        with self._lock:
            self._records.clear()


EcosystemRegistry = GlobalEcosystemRegistry
