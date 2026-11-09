"""Private ENGINE registry for NSFWINFRA."""
from threading import RLock
class EngineRegistry:
    def __init__(self): self._items={}; self._lock=RLock()
    def register(self,key,value):
        key=str(key).strip()
        if not key: raise ValueError("engine_id is required")
        with self._lock:
            if key in self._items: raise ValueError("engine already registered: "+key)
            self._items[key]=value
        return value
    def get(self,key):
        with self._lock: return self._items.get(str(key).strip())
    def list_ids(self):
        with self._lock: return tuple(self._items)
    def count(self):
        with self._lock: return len(self._items)
