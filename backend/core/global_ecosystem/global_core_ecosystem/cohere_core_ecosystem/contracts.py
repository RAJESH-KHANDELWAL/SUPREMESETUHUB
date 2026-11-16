"""Stable provider-wide contracts for Cohere CORE.

Identity and authorization context are supplied by the application layer.
Opaque secret references are metadata only; this module never resolves secrets.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Mapping


class Readiness(str, Enum):
    INTERFACE_ONLY = "interface_only"
    CONTRACT_ONLY = "contract_only"
    ADAPTER_SCAFFOLD = "adapter_scaffold_not_live_verified"
    READY = "ready"
    DISABLED = "disabled"
    ERROR = "error"


@dataclass(frozen=True)
class TenantContext:
    """Authenticated caller context passed in by the application boundary."""

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


@dataclass(frozen=True)
class SecretReference:
    """Opaque secret-manager reference; never stores secret material."""

    provider: str
    reference: str
    version: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.provider, str) or not self.provider.strip():
            raise ValueError("SECRET_REFERENCE_PROVIDER_REQUIRED")
        if not isinstance(self.reference, str) or not self.reference.strip():
            raise ValueError("SECRET_REFERENCE_REQUIRED")


@dataclass(frozen=True)
class CapabilityRequest:
    capability: str
    inputs: Mapping[str, Any]
    model: str | None = None
    options: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class CoreResult:
    ok: bool
    capability: str
    data: Mapping[str, Any] = field(default_factory=dict)
    errors: tuple[str, ...] = ()
    status: str = "validated"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
