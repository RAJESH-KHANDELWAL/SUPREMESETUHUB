"""STORAGE-owned identity, health and object metadata models."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass
class StorageEcosystemIdentity:
    ecosystem_id: str
    name: str
    ecosystem_type: str = "STORAGE_PROVIDER"
    provider_id: str | None = None
    parent_id: str | None = None
    status: str = "REGISTERED"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {"ecosystem_id": self.ecosystem_id, "name": self.name,
                "ecosystem_type": self.ecosystem_type, "provider_id": self.provider_id,
                "parent_id": self.parent_id, "status": self.status, "enabled": self.enabled,
                "capabilities": list(self.capabilities), "metadata": dict(self.metadata),
                "created_at": self.created_at, "updated_at": self.updated_at}

@dataclass
class StorageHealth:
    status: str = "NOT_CONFIGURED"
    configured: bool = False
    connection_verified: bool = False
    read_verified: bool = False
    write_verified: bool = False
    details: dict[str, Any] = field(default_factory=dict)

@dataclass
class StorageObject:
    object_id: str
    provider_id: str
    container: str
    key: str
    size_bytes: int | None = None
    content_type: str | None = None
    checksum: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        for field_name in ("object_id", "provider_id", "container", "key"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} is required")
        if self.size_bytes is not None and self.size_bytes < 0:
            raise ValueError("size_bytes cannot be negative")
