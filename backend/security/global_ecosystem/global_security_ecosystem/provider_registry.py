"""Registry for explicitly injected SECURITY provider adapters."""
from threading import RLock
from .catalog import get_provider, list_providers

class SecurityProviderRegistry:
    def __init__(self):
        self._items = {}
        self._lock = RLock()

    def register(self, provider_id: str, adapter, *, replace: bool = False):
        key = str(provider_id or "").strip().lower()
        if not key:
            raise ValueError("provider_id is required")
        get_provider(key)
        if adapter is None or not callable(getattr(adapter, "describe", None)) or not callable(getattr(adapter, "execute", None)) or not callable(getattr(adapter, "health", None)):
            raise TypeError("security adapter must implement describe(), execute(), and health()")
        declared = str(getattr(adapter, "provider_id", key)).strip().lower()
        if declared != key:
            raise ValueError("provider adapter provider_id does not match registration key")
        with self._lock:
            if key in self._items and not replace:
                raise ValueError(f"Security provider already registered: {key}")
            self._items[key] = adapter
        return adapter

    def get(self, provider_id: str):
        key = str(provider_id or "").strip().lower()
        if not key:
            raise ValueError("provider_id is required")
        with self._lock:
            return self._items.get(key)

    def list_registered(self):
        with self._lock:
            return tuple(sorted(self._items))

    def catalog(self):
        with self._lock:
            current = dict(self._items)
        return tuple({**row, "status": "REGISTERED" if row["provider_id"] in current else "NOT_CONFIGURED"} for row in list_providers())

__all__ = ["SecurityProviderRegistry"]
