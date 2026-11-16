"""Registry for explicitly supplied APP component adapters."""
from threading import RLock
from .component_base import AppComponentAdapter
class AppAdapterRegistry:
    def __init__(self):self._items={};self._lock=RLock()
    def register(self,component_id,adapter,*,replace=False):
        key=str(component_id or "").strip()
        if not key or not isinstance(adapter,AppComponentAdapter):raise TypeError("component_id and AppComponentAdapter are required")
        if adapter.component_id!=key:raise ValueError("adapter component_id must match registry key")
        with self._lock:
            if key in self._items and not replace:raise ValueError(f"APP adapter already registered: {key}")
            self._items[key]=adapter
        return adapter
    def get(self,component_id):
        with self._lock:return self._items.get(str(component_id).strip())
    def list_ids(self):
        with self._lock:return tuple(sorted(self._items))
    def unregister(self,component_id):
        with self._lock:return self._items.pop(str(component_id).strip(),None) is not None
__all__=["AppAdapterRegistry"]
