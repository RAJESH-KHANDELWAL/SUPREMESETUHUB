"""Models for global connection orchestration."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ConnectionRequest:
    connection_id: str
    provider_id: str
    server_id: str
    connection_type: str
    protocol: str
    endpoint: Optional[str] = None
    namespace: str = "global"


@dataclass(frozen=True)
class ConnectionOperationResult:
    success: bool
    connection_id: str
    status: str
    error: Optional[str] = None

    def as_dict(self):
        return {
            "success": self.success,
            "connection_id": self.connection_id,
            "status": self.status,
            "error": self.error,
        }
