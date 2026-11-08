"""Thread-safe registry for explicitly injected adapters from owned layers."""
from threading import RLock
from typing import Any
LAYER_NAMES = ("API", "CORE", "ENGINE", "DATABASE", "STORAGE")
class ServerLayerRegistry:
    def __init__(self):
        self._adapters: dict[str, Any] = {}
        self._lock = RLock()
    @staticmethod
    def _key(layer: str) -> str:
        key = str(layer).strip().upper()
        if key not in LAYER_NAMES:
            raise ValueError(f"Unsupported SERVER layer: {layer!r}")
        return key
    def register(self, layer: str, adapter: Any, *, replace: bool = False):
        key = self._key(layer)
        if adapter is None:
            raise ValueError("adapter is required")
        with self._lock:
            if key in self._adapters and not replace:
                raise ValueError(f"SERVER layer adapter already registered: {key}")
            self._adapters[key] = adapter
        return adapter
    def get(self, layer: str):
        with self._lock:
            return self._adapters.get(self._key(layer))
    def unregister(self, layer: str) -> bool:
        with self._lock:
            return self._adapters.pop(self._key(layer), None) is not None
    def list_layers(self):
        with self._lock:
            return tuple(name for name in LAYER_NAMES if name in self._adapters)
    def status(self):
        with self._lock:
            registered = list(self.list_layers())
            return {"domain": "SERVER", "registered_layers": registered,
                    "missing_layers": [x for x in LAYER_NAMES if x not in registered],
                    "ready": len(registered) == len(LAYER_NAMES)}
__all__ = ["LAYER_NAMES", "ServerLayerRegistry"]