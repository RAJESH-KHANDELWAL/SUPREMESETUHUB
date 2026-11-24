"""Small in-memory registry for Adobe capability descriptors."""

from __future__ import annotations

from threading import RLock
from .models import AdobeCapability


class AdobeCapabilityRegistry:
    def __init__(self) -> None:
        self._items: dict[str, AdobeCapability] = {}
        self._lock = RLock()

    def register(self, item: AdobeCapability) -> None:
        key = item.key.strip().lower()
        if not key:
            raise ValueError("Capability key cannot be empty")
        with self._lock:
            self._items[key] = item

    def get(self, key: str) -> AdobeCapability | None:
        with self._lock:
            return self._items.get(key.strip().lower())

    def list_all(self) -> tuple[AdobeCapability, ...]:
        with self._lock:
            return tuple(self._items[key] for key in sorted(self._items))
