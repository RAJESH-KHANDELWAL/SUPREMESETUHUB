"""Thread-safe in-memory catalog registry; production persistence uses central DB."""
from dataclasses import asdict
from threading import RLock

from .ecosystem_models import CloudStorageRecord


class CloudStorageRegistry:
    """Register and read local metadata records only; no provider API operations."""

    def __init__(self) -> None:
        self._records: dict[str, CloudStorageRecord] = {}
        self._lock = RLock()

    def register(self, record: CloudStorageRecord) -> dict:
        if not isinstance(record, CloudStorageRecord):
            raise TypeError("record must be a CloudStorageRecord")
        with self._lock:
            if record.record_id in self._records:
                raise ValueError("DUPLICATE_RECORD_ID")
            self._records[record.record_id] = record
            return asdict(record)

    def get(self, record_id: str) -> dict | None:
        with self._lock:
            record = self._records.get(record_id)
            return asdict(record) if record else None

    def list(self) -> list[dict]:
        with self._lock:
            return [asdict(item) for item in self._records.values()]
