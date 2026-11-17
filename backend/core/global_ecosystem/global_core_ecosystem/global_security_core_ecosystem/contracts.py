"""Stable contracts shared by Global Security Core modules.

The Core layer owns security identity, taxonomy, capability metadata,
readiness and policy metadata. Authentication, enforcement, evidence
persistence and provider transport remain in their dedicated layers.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


def utc_now() -> str:
    """Return an ISO-8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


class Readiness(str, Enum):
    """Descriptive Core readiness states; none imply live protection."""

    CATALOG_ONLY = "CORE_CATALOG_ONLY"
    CONFIGURATION_REQUIRED = "READY_FOR_CONFIGURATION"
    READY = "READY"
    DISABLED = "DISABLED"
    ERROR = "ERROR"


@dataclass(frozen=True)
class TenantContext:
    """Caller identity supplied by an independently authenticated layer."""

    tenant_id: str
    actor_id: str
    roles: tuple[str, ...] = ()
    request_id: str | None = None
    actor_type: str = "user"

    def validate(self) -> None:
        """Validate required context fields without authenticating the actor."""
        if not isinstance(self.tenant_id, str) or not self.tenant_id.strip():
            raise ValueError("TENANT_ID_REQUIRED")
        if not isinstance(self.actor_id, str) or not self.actor_id.strip():
            raise ValueError("ACTOR_ID_REQUIRED")
        if not isinstance(self.actor_type, str) or not self.actor_type.strip():
            raise ValueError("ACTOR_TYPE_REQUIRED")
        if not isinstance(self.roles, tuple) or any(
            not isinstance(role, str) or not role.strip() for role in self.roles
        ):
            raise ValueError("INVALID_TENANT_ROLES")


@dataclass(frozen=True)
class SecretReference:
    """Opaque pointer to an external secret-manager entry."""

    provider: str
    reference: str
    version: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.provider, str) or not self.provider.strip():
            raise ValueError("SECRET_PROVIDER_REQUIRED")
        if not isinstance(self.reference, str) or not self.reference.strip():
            raise ValueError("SECRET_REFERENCE_REQUIRED")
        if self.version is not None and (
            not isinstance(self.version, str) or not self.version.strip()
        ):
            raise ValueError("INVALID_SECRET_REFERENCE_VERSION")


@dataclass
class CoreResult:
    """Language-neutral result envelope for Security Core consumers."""

    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
