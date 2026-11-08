"""DATABASE-owned server inventory repository interface.

This is an in-memory reference adapter for tests/development. Replace it with a
configured SQL/NoSQL implementation before relying on persistence across restarts.
"""
from __future__ import annotations
from copy import deepcopy
from threading import RLock
from .models import ServerInventoryRecord

class ServerInventoryRepository:
    def __init__(self):
        self._records = {}
        self._lock = RLock()

    def create(self, record: ServerInventoryRecord):
        record.validate()
        key = record.server_id.strip()
        row = deepcopy(record.__dict__)
        row["server_id"] = key
        with self._lock:
            if key in self._records:
                raise ValueError(f"SERVER_INVENTORY_ALREADY_EXISTS: {key}")
            self._records[key] = row
            return deepcopy(row)

    def get(self, server_id: str):
        with self._lock:
            item = self._records.get(str(server_id).strip())
            return deepcopy(item) if item is not None else None

    def list(self):
        with self._lock:
            return [deepcopy(item) for item in self._records.values()]

    def update(self, server_id: str, **changes):
        allowed = {"status","authorized","enabled","metadata","region","environment"}
        unknown = set(changes) - allowed
        if unknown:
            raise ValueError("Unsupported inventory fields: " + ", ".join(sorted(unknown)))
        with self._lock:
            current = self._records.get(str(server_id).strip())
            if current is None:
                return None
            self._records[str(server_id).strip()] = {**current, **deepcopy(changes)}
            return deepcopy(self._records[str(server_id).strip()])

    def delete(self, server_id: str):
        with self._lock:
            return self._records.pop(str(server_id).strip(), None) is not None

    def count(self):
        with self._lock:
            return len(self._records)
