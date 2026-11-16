"""Thread-safe in-memory metadata registry; production uses central DB persistence."""
from threading import RLock
from dataclasses import asdict
from .ecosystem_models import EcosystemRecord
class EcosystemRegistry:
    def __init__(self):
        self._records: dict[str, EcosystemRecord] = {}
        self._lock = RLock()
    def register(self, record: EcosystemRecord) -> dict:
        with self._lock:
            if record.record_id in self._records:
                raise ValueError("DUPLICATE_RECORD_ID")
            self._records[record.record_id] = record
            return asdict(record)
    def get(self, record_id: str) -> dict | None:
        with self._lock:
            item = self._records.get(record_id)
            return asdict(item) if item else None
    def list(self) -> list[dict]:
        with self._lock:
            return [asdict(item) for item in self._records.values()]
