"""Shared contracts for Kamasutra Core metadata and policy boundaries."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class Readiness(str, Enum):
    CATALOG_ONLY = "CATALOG_ONLY"
    CONFIGURATION_REQUIRED = "CONFIGURATION_REQUIRED"
    READY = "READY"
    DISABLED = "DISABLED"
    ERROR = "ERROR"


@dataclass(frozen=True)
class TenantContext:
    """Identity supplied by the authenticated application layer."""
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
class AdultAccessAttestation:
    """Trusted upstream verification references; never raw identity documents."""
    age_assured: bool
    consent_confirmed: bool
    rights_confirmed: bool
    verified_by: str

    def validate(self) -> None:
        if not self.age_assured:
            raise ValueError("AGE_ASSURANCE_REQUIRED")
        if not self.consent_confirmed:
            raise ValueError("INFORMED_CONSENT_REQUIRED")
        if not self.rights_confirmed:
            raise ValueError("CONTENT_RIGHTS_VERIFICATION_REQUIRED")
        if not self.verified_by.strip():
            raise ValueError("TRUSTED_VERIFIER_REQUIRED")


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


__all__ = ["Readiness", "TenantContext", "AdultAccessAttestation", "CoreResult", "utc_now"]
