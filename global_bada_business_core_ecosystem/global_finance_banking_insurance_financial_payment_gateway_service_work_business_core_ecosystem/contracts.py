"""Typed, dependency-light contracts for finance commercial metadata."""
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    actor_type: str = "user"
    roles: tuple[str, ...] = ()
    request_id: str | None = None

    def validate(self) -> None:
        if not self.tenant_id.strip():
            raise ValueError("TENANT_ID_REQUIRED")
        if not self.actor_id.strip():
            raise ValueError("ACTOR_ID_REQUIRED")

@dataclass(frozen=True)
class ClassificationRequest:
    domain_id: str
    classification_type: str
    jurisdiction: str | None = None
    business_id: str | None = None

    def validate(self) -> None:
        if not self.domain_id.strip():
            raise ValueError("DOMAIN_ID_REQUIRED")
        if not self.classification_type.strip():
            raise ValueError("CLASSIFICATION_TYPE_REQUIRED")

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
