"""SERVER-owned runtime and node value objects."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ServerNode:
    server_id: str
    name: str
    host: str = "127.0.0.1"
    port: int | None = None
    environment: str = "development"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self.server_id = str(self.server_id).strip()
        self.name = str(self.name).strip()
        self.host = str(self.host).strip()
        self.environment = str(self.environment).strip().lower()
        self.status = str(self.status).strip().upper()
        if not self.server_id or not self.name or not self.host:
            raise ValueError("server_id, name and host are required")
        if self.port is not None and not 1 <= int(self.port) <= 65535:
            raise ValueError("port must be between 1 and 65535")
        if not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary")

@dataclass(frozen=True)
class ServerHealth:
    status: str
    registered_servers: int
    configured_providers: int
    runtime: dict[str, Any] = field(default_factory=dict)

__all__ = ["ServerNode", "ServerHealth"]
