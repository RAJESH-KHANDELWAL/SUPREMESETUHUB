"""Thread-safe metadata registry; production persistence belongs in central DB."""
from dataclasses import asdict
from threading import RLock
from .ecosystem_models import CloudflareStorageRecord

class CloudflareStorageRegistry:
    def __init__(self):
        self._records = {}
        self._lock = RLock()

    def register(self, record: CloudflareStorageRecord) -> dict:
        with self._lock:
            if record.record_id in self._records:
                raise ValueError("DUPLICATE_RECORD_ID")
            self._records[record.record_id] = record
            return asdict(record)

    def get(self, record_id: str) -> dict | None:
        with self._lock:
            record = self._records.get(record_id)
            return asdict(record) if record else None
