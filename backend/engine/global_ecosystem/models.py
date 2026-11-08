"""Independent ENGINE ecosystem identity model (no CORE/API imports)."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass
class GlobalEcosystemIdentity:
    ecosystem_id: str
    name: str
    ecosystem_type: str = "GENERAL"
    repository_ref: str | None = None
    status: str = "REGISTERED"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    message: str | None = None
    parent_id: str | None = None
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "ecosystem_id": self.ecosystem_id, "name": self.name,
            "ecosystem_type": self.ecosystem_type, "repository_ref": self.repository_ref,
            "status": self.status, "enabled": self.enabled,
            "capabilities": list(self.capabilities), "metadata": dict(self.metadata),
            "message": self.message, "parent_id": self.parent_id,
            "created_at": self.created_at, "updated_at": self.updated_at,
        }

EcosystemIdentity = GlobalEcosystemIdentity
__all__ = ["EcosystemIdentity", "GlobalEcosystemIdentity", "utc_now"]
