"""Thread-safe in-process SERVER inventory registry.

This registry is a runtime default, not durable storage. Inject a DATABASE
repository adapter when persistent server inventory is configured.
"""
from threading import RLock
from .exceptions import ServerConflictError
from .models import ServerRecord

class ServerRegistry:
    def __init__(self):
        self._records = {}
        self._lock = RLock()
    def create(self, record: ServerRecord):
        with self._lock:
            if record.server_id in self._records:
                raise ServerConflictError(f"Server already exists: {record.server_id}")
            self._records[record.server_id] = record
            return record
    def get(self, server_id):
        with self._lock: return self._records.get(str(server_id))
    def list(self):
        with self._lock: return list(self._records.values())
    def update(self, record):
        with self._lock:
            if record.server_id not in self._records: return None
            self._records[record.server_id] = record
            return record
    def delete(self, server_id):
        with self._lock: return self._records.pop(str(server_id), None) is not None
    def status(self):
        with self._lock:
            return {"backend": "IN_MEMORY", "durable": False, "count": len(self._records)}
