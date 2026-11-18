"""Typed contracts for people-life CORE metadata and policy context."""
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
    verified_adult: bool = False
    informed_consent: bool = False
    jurisdiction: str | None = None
    def validate(self) -> None:
        if not isinstance(self.tenant_id, str) or not self.tenant_id.strip():
            raise ValueError("TENANT_ID_REQUIRED")
        if not isinstance(self.actor_id, str) or not self.actor_id.strip():
            raise ValueError("ACTOR_ID_REQUIRED")

@dataclass(frozen=True)
class SecretReference:
    provider: str
    reference: str
    version: str | None = None
    def __post_init__(self) -> None:
        if not self.provider.strip() or not self.reference.strip():
            raise ValueError("SECRET_REFERENCE_REQUIRED")

@dataclass(frozen=True)
class PeopleLifeDomain:
    domain_id: str
    name: str
    folder: str
    scope: str
    age_restricted: bool = False
    status: str = "CORE_CATALOG_ONLY"

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
