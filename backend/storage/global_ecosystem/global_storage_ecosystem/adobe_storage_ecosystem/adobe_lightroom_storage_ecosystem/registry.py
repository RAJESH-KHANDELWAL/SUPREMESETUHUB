"""Thread-safe in-memory metadata registry; production persistence belongs in central DB."""
from threading import RLock
from .models import StorageObjectRecord
class StorageMetadataRegistry:
    def __init__(self):self._records={};self._lock=RLock()
    def register(self,record:StorageObjectRecord)->dict:
        with self._lock:
            if record.object_id in self._records:raise ValueError("DUPLICATE_OBJECT_ID")
            self._records[record.object_id]=record;return record.to_dict()
    def get(self,object_id:str)->dict|None:
        with self._lock:
            x=self._records.get(object_id);return x.to_dict() if x else None
    def list(self)->list[dict]:
        with self._lock:return [x.to_dict() for x in self._records.values()]
    def count(self)->int:
        with self._lock:return len(self._records)
