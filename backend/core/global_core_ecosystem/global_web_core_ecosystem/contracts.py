"""Stable metadata contracts for WEB CORE; no network or persistence clients."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    environment: str = "development"

    def validate(self) -> None:
        if not self.tenant_id.strip() or not self.actor_id.strip():
            raise ValueError("TENANT_AND_ACTOR_REQUIRED")
        if self.environment not in {"development", "test", "staging", "production"}:
            raise ValueError("UNSUPPORTED_ENVIRONMENT")

@dataclass(frozen=True)
class SecretReference:
    secret_id: str
    secret_store: str = "EXTERNAL_SECRET_STORE"

    def validate(self) -> None:
        if not self.secret_id.strip():
            raise ValueError("SECRET_REFERENCE_ID_REQUIRED")

@dataclass(frozen=True)
class Readiness:
    ready: bool
    state: str
    blockers: tuple[str, ...] = ()

@dataclass(frozen=True)
class CoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
