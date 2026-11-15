"""Thread-safe in-memory capability registry; persistence belongs to DATABASE."""
from threading import RLock
from .models import DeveloperCapability
class DeveloperRegistry:
    def __init__(self):
        self._items = {}; self._lock = RLock()
    def register(self, capability: DeveloperCapability):
        with self._lock:
            if capability.capability_id in self._items: raise ValueError(f"Duplicate capability: {capability.capability_id}")
            self._items[capability.capability_id] = capability
        return capability
    def get(self, capability_id: str):
        with self._lock: return self._items.get(capability_id)
    def list(self, domain=None, geographic_scope=None):
        with self._lock: items = tuple(self._items.values())
        return tuple(x for x in items if (domain is None or x.domain == domain) and (geographic_scope is None or x.geographic_scope == geographic_scope))
    def remove(self, capability_id: str):
        with self._lock: return self._items.pop(capability_id, None) is not None
