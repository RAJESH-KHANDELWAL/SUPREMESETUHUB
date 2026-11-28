"""Typed contracts; no persistence, credentials or external execution."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass(frozen=True)
class BusinessContext:
    tenant_id: str
    actor_id: str
    jurisdiction: str
    business_id: str | None = None
    request_id: str | None = None
    def validate(self) -> None:
        for name in ("tenant_id", "actor_id", "jurisdiction"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name.upper()}_REQUIRED")

@dataclass(frozen=True)
class ServiceWorkBusinessRecord:
    record_id: str
    domain_id: str
    record_type: str
    title: str
    jurisdiction: str
    lifecycle_status: str = "DRAFT"
    source_refs: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()
    risk_level: str = "UNASSESSED"
    def validate_shape(self) -> None:
        for name in ("record_id", "domain_id", "record_type", "title", "jurisdiction"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name.upper()}_REQUIRED")

@dataclass
class CoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
