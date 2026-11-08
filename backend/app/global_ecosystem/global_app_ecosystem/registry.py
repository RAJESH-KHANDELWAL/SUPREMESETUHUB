"""Thread-safe process-local registry for APP component descriptors."""
from threading import RLock
from .models import AppComponent
from .catalog import get_component_type
class AppComponentRegistry:
    def __init__(self):self._items={};self._lock=RLock()
    def register(self,component,*,replace=False):
        if not isinstance(component,AppComponent):raise TypeError("component must be an APP-owned AppComponent")
        get_component_type(component.component_type)
        with self._lock:
            if component.component_id in self._items and not replace:raise ValueError(f"APP component already registered: {component.component_id}")
            self._items[component.component_id]=component
        return component
    def get(self,component_id):
        with self._lock:return self._items.get(str(component_id).strip())
    def list(self,*,component_type=None,enabled_only=False):
        with self._lock:items=tuple(self._items.values())
        if component_type is not None:
            key=str(component_type).strip().lower().replace("_","-");items=tuple(x for x in items if x.component_type==key)
        return tuple(x for x in items if x.enabled) if enabled_only else items
    def unregister(self,component_id):
        with self._lock:return self._items.pop(str(component_id).strip(),None) is not None
    def count(self):
        with self._lock:return len(self._items)
    def status(self):
        items=self.list();return {"registered_components":len(items),"enabled_components":sum(x.enabled for x in items),"registry_scope":"PROCESS_LOCAL","persistence":"NOT_CONFIGURED"}
__all__=["AppComponentRegistry"]
