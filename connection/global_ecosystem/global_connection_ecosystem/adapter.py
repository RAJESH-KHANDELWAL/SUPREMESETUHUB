"""Adapter contract for real provider/server connection operations."""


class ConnectionAdapter:
    """Base adapter. Implementations must perform real provider-specific I/O."""

    def connect(self, connection):
        raise NotImplementedError

    def disconnect(self, connection):
        raise NotImplementedError

    def health(self):
        return {"available": True}
