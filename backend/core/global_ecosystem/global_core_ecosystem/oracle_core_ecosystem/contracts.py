"""Shared Oracle Core metadata contracts."""
from dataclasses import asdict, dataclass
from typing import Any

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    region: str | None = None

@dataclass(frozen=True)
class SecretReference:
    reference: str
    provider: str = "external-secret-manager"

@dataclass(frozen=True)
class Readiness:
    status: str
    live_connection_verified: bool = False
    blockers: tuple[str, ...] = ()

@dataclass(frozen=True)
class CoreResult:
    ecosystem_id: str
    status: str
    data: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
