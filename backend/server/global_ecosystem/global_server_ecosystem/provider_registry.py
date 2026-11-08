"""SERVER registry for provider integration entry points; no live calls."""
from threading import RLock
from typing import Any
from .catalog import get_provider_catalog
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
        if provider is None:
            raise ValueError("provider is required")
        with self._lock:
            if key in self._providers and not replace:
                raise ValueError(f"Provider already registered: {key}")
            self._providers[key] = provider
        return provider
    def get(self, provider_id: str):
        with self._lock:
            return self._providers.get(self._key(provider_id))
    def list_registered(self):
        with self._lock:
            return tuple(sorted(self._providers))
    def catalog(self):
        return tuple({"provider_id": p.provider_id, "display_name": p.display_name,
                      "package": p.package,
                      "status": "REGISTERED" if self.get(p.provider_id) else p.status}
                     for p in get_provider_catalog())
__all__ = ["ServerProviderRegistry"]