"""Thread-safe in-memory metadata registry; production persistence belongs in central DB."""
from threading import RLock
from .models import StorageObjectRecord

class StorageMetadataRegistry:
    def __init__(self) -> None:
        self._records: dict[str, StorageObjectRecord] = {}
        self._lock = RLock()
    def register(self, record: StorageObjectRecord) -> dict:
        with self._lock:
            if record.object_id in self._records:
                raise ValueError("DUPLICATE_OBJECT_ID")
            self._records[record.object_id] = record
            return record.to_dict()
    def get(self, object_id: str) -> dict | None:
        with self._lock:
            item = self._records.get(object_id)
            return item.to_dict() if item else None
    def list(self) -> list[dict]:
        with self._lock:
            return [item.to_dict() for item in self._records.values()]
    def count(self) -> int:
        with self._lock:
            return len(self._records)
