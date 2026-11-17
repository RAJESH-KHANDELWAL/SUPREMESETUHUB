"""Thread-safe registry for explicitly injected SERVER provider adapters."""
from threading import RLock
from typing import Any
from .catalog import get_provider_catalog, get_provider

class ServerProviderRegistry:
    def __init__(self):
        self._providers: dict[str, Any] = {}
        self._lock = RLock()

    @staticmethod
    def _key(provider_id: str) -> str:
        key = str(provider_id).strip().lower()
        if not key:
            raise ValueError("provider_id is required")
        return key

    def register(self, provider_id: str, provider: Any, *, replace: bool = False):
        key = self._key(provider_id)
        get_provider(key)  # Reject misspelled or unlisted provider IDs.
        if provider is None:
            raise ValueError("provider is required")
        declared_id = getattr(provider, "provider_id", key)
        if str(declared_id).strip().lower() != key:
            raise ValueError("provider adapter provider_id does not match registration key")
        if not callable(getattr(provider, "describe", None)):
            raise TypeError("provider adapter must implement describe()")
        with self._lock:
            if key in self._providers and not replace:
                raise ValueError(f"Provider already registered: {key}")
            self._providers[key] = provider
        return provider

    def get(self, provider_id: str):
        with self._lock:
            return self._providers.get(self._key(provider_id))

    def unregister(self, provider_id: str) -> bool:
        with self._lock:
            return self._providers.pop(self._key(provider_id), None) is not None

    def list_registered(self):
        with self._lock:
            return tuple(sorted(self._providers))

    def catalog(self):
        with self._lock:
            registered = dict(self._providers)
        rows = []
        for descriptor in get_provider_catalog():
            adapter = registered.get(descriptor.provider_id)
            row = {
                "provider_id": descriptor.provider_id,
                "display_name": descriptor.display_name,
                "package": descriptor.package,
                "alignment": descriptor.alignment,
                "status": "REGISTERED" if adapter is not None else "NOT_CONFIGURED",
            }
            if adapter is not None:
                row["adapter"] = adapter.describe()
            rows.append(row)
        return tuple(rows)

__all__ = ["ServerProviderRegistry"]
