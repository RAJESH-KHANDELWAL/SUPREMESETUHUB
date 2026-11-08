"""Safe lifecycle state transitions for registered server records.

These operations update the control-plane record only. They do not power on,
power off, create, or delete remote infrastructure.
"""
from .exceptions import ServerNotFoundError
from .models import utc_now

class ServerLifecycleService:
    def __init__(self, registry): self.registry = registry
    def _transition(self, server_id, status):
        record = self.registry.get(server_id)
        if record is None: raise ServerNotFoundError(f"Unknown server: {server_id}")
        record.status, record.updated_at = status, utc_now()
        self.registry.update(record)
        return record.to_dict()
    def start(self, server_id): return self._transition(server_id, "START_REQUESTED")
    def stop(self, server_id): return self._transition(server_id, "STOP_REQUESTED")
