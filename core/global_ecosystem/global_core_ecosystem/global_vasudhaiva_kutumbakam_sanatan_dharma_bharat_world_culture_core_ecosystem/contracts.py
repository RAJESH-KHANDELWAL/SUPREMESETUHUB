"""Stable cultural Core tenant and result contracts."""
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
def utc_now(): return datetime.now(timezone.utc).isoformat()
@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    actor_type: str = "user"
    roles: tuple[str,...] = ()
    request_id: str | None = None
    def validate(self):
        if not self.tenant_id.strip(): raise ValueError("TENANT_ID_REQUIRED")
        if not self.actor_id.strip(): raise ValueError("ACTOR_ID_REQUIRED")
@dataclass
class CulturalCoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str,Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)
    def to_dict(self): return asdict(self)
