"""Stable contracts for the provider-neutral GLOBAL SERVER CORE control plane."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Protocol, runtime_checkable


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class Readiness(str, Enum):
    CATALOG_ONLY = "CORE_CATALOG_ONLY"
    METADATA_AVAILABLE = "CORE_METADATA_AVAILABLE"
    CONFIGURATION_REQUIRED = "READY_FOR_CONFIGURATION"
    READY = "READY"
    DISABLED = "DISABLED"
    ERROR = "ERROR"


@dataclass(frozen=True)
class TenantContext:
    """Caller identity supplied by the authenticated application/API layer."""
    tenant_id: str
    actor_id: str
    actor_type: str = "user"
    roles: tuple[str, ...] = ()
    request_id: str | None = None

    def validate(self) -> None:
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
    """Opaque secret-manager pointer; never stores secret bytes."""
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
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@runtime_checkable
class ServerProviderContract(Protocol):
    provider_id: str
    def health(self) -> dict[str, Any]: ...
    def execute(self, operation: str, payload: dict[str, Any] | None = None) -> Any: ...


@runtime_checkable
class ServerInventoryContract(Protocol):
    def register(self, identity: Any) -> dict[str, Any]: ...
    def get(self, server_id: str) -> dict[str, Any] | None: ...
    def list(self) -> list[dict[str, Any]]: ...


@runtime_checkable
class ServerLifecycleContract(Protocol):
    def transition(self, server_id: str, state: Any) -> dict[str, Any] | None: ...
