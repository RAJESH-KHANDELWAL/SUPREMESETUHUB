"""Typed, secret-free contracts shared by PayPal Core modules."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

class Readiness(str, Enum):
    CATALOG_ONLY = "CORE_CATALOG_ONLY"
    CONFIGURATION_REQUIRED = "READY_FOR_CONFIGURATION"
    READY = "READY"
    DISABLED = "DISABLED"
    ERROR = "ERROR"

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    actor_type: str = "user"
    roles: tuple[str, ...] = ()
    request_id: str | None = None
    def validate(self) -> None:
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
    def to_dict(self) -> dict[str, Any]: return asdict(self)
