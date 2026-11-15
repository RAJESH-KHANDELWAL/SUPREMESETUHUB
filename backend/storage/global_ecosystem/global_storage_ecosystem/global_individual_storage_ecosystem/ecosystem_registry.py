"""Thread-safe in-memory metadata registry for local development/tests only."""
from dataclasses import asdict
from threading import RLock

from .ecosystem_models import CategoryRecord


class EcosystemRegistry:
    """Process-local registry; production persistence belongs to the database layer."""

    def __init__(self) -> None:
        self._records: dict[str, CategoryRecord] = {}
        self._lock = RLock()

    def register(self, record: CategoryRecord) -> dict:
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
            return [asdict(record) for record in self._records.values()]
