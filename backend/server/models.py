"""Canonical SERVER domain models."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

def utc_now():
    return datetime.now(timezone.utc).isoformat()

@dataclass
class ServerRecord:
    name: str
    server_type: str
    provider: str = "local"
    region: str = "global"
    server_id: str = field(default_factory=lambda: "SRV-" + uuid4().hex[:12].upper())
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)
    def to_dict(self):
        return {"server_id": self.server_id, "name": self.name, "server_type": self.server_type,
                "provider": self.provider, "region": self.region, "status": self.status,
                "metadata": dict(self.metadata), "created_at": self.created_at,
                "updated_at": self.updated_at}

@dataclass
class ServerCreateRequest:
    name: str
    server_type: str
    provider: str = "local"
    region: str = "global"
    metadata: dict[str, Any] = field(default_factory=dict)
