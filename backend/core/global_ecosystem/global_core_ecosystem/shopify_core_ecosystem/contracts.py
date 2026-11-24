"""Shared tenant and result contracts."""
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    request_id: str | None = None
    def validate(self):
        if not self.tenant_id.strip(): raise ValueError("TENANT_ID_REQUIRED")
        if not self.actor_id.strip(): raise ValueError("ACTOR_ID_REQUIRED")

@dataclass
class CoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    def to_dict(self): return asdict(self)
