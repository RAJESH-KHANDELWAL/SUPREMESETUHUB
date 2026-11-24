"""Safe lifecycle state transitions for registered server records.

These transitions update SERVER inventory only. They do not power on/off,
create, reboot, or delete remote infrastructure without a separate adapter.
"""
from .exceptions import ServerNotFoundError
from .models import utc_now


class ServerLifecycleService:
    def __init__(self, registry):
        self.registry = registry

    def _transition(self, server_id, status):
        record = self.registry.get(server_id)
        if record is None:
            raise ServerNotFoundError(f"Unknown server: {server_id}")
        record.status = status
        record.updated_at = utc_now()
        self.registry.update(record)
        return record.to_dict()

    def start(self, server_id):
        return self._transition(server_id, "START_REQUESTED")

    def stop(self, server_id):
        return self._transition(server_id, "STOP_REQUESTED")

    def restart(self, server_id):
        return self._transition(server_id, "RESTART_REQUESTED")
