"""CORE-owned process-local registry for SERVER resource identity metadata."""
from __future__ import annotations
from copy import deepcopy
from threading import RLock
from typing import Any
from .models import ServerIdentity

class ServerCoreRegistry:
    """Validates and catalogs server identity, not remote compute state."""
    def __init__(self):
        self._items: dict[str, dict[str, Any]] = {}
        self._lock = RLock()

    def register(self, identity: ServerIdentity) -> dict[str, Any]:
        identity.validate()
        key = identity.server_id.strip()
        row = {
            "server_id": key,
            "provider_id": identity.provider_id.strip().lower(),
            "server_type": identity.server_type.strip().lower(),
            "server_role": identity.server_role.strip(),
            "country": identity.country.strip().upper(),
            "region": identity.region.strip(),
            "environment": identity.environment.strip().lower(),
            "metadata": deepcopy(identity.metadata),
        }
        with self._lock:
            if key in self._items:
                raise ValueError(f"Server already registered: {key}")
            self._items[key] = row
            return deepcopy(row)

    def get(self, server_id: str):
        with self._lock:
            row = self._items.get(str(server_id).strip())
            return deepcopy(row) if row is not None else None

    def list(self):
        with self._lock:
            return [deepcopy(row) for row in self._items.values()]

    def count(self) -> int:
        with self._lock:
            return len(self._items)

    def remove(self, server_id: str) -> bool:
        with self._lock:
            return self._items.pop(str(server_id).strip(), None) is not None
