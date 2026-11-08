"""Thread-safe, in-memory registry for Google provider engines."""
from __future__ import annotations

from threading import RLock
from typing import Any

from .models import GoogleEngineIdentity


class GoogleEngineRegistry:
    def __init__(self) -> None:
        self._items: dict[str, GoogleEngineIdentity] = {}
        self._lock = RLock()

    def register(self, item: GoogleEngineIdentity) -> dict[str, Any]:
        key = item.engine_id.strip()
        name = item.name.strip()
        if not key or not name:
            raise ValueError("engine_id and name are required")
        with self._lock:
            if key in self._items:
                raise ValueError(f"Google engine already registered: {key}")
            item.engine_id = key
            item.name = name
            self._items[key] = item
            return item.to_dict()

    def get(self, engine_id: str) -> dict[str, Any] | None:
        key = engine_id.strip()
        if not key:
            return None
        with self._lock:
            item = self._items.get(key)
            if item is None:
                item = next((x for x in self._items.values() if x.name.casefold() == key.casefold()), None)
            return item.to_dict() if item else None

    def list(self) -> list[dict[str, Any]]:
        with self._lock:
            return [item.to_dict() for item in self._items.values()]

    def count(self) -> int:
        with self._lock:
            return len(self._items)
