"""Shared Cloudflare Core contracts; no provider transport or persistence."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class CloudflareTenantContext:
    tenant_id: str
    actor_id: str
    account_id: str | None = None

    def validate(self) -> None:
        if not isinstance(self.tenant_id, str) or not self.tenant_id.strip():
            raise ValueError("tenant_id is required")
        if not isinstance(self.actor_id, str) or not self.actor_id.strip():
            raise ValueError("actor_id is required")
        if self.account_id is not None and (
            not isinstance(self.account_id, str) or not self.account_id.strip()
        ):
            raise ValueError("account_id must be a non-empty string when supplied")


@dataclass(frozen=True)
class CloudflareCoreResult:
    success: bool
    ecosystem_id: str
    data: dict[str, Any] = field(default_factory=dict)
    execution_performed: bool = False
    persistence_performed: bool = False
    live_connection_verified: bool = False


__all__ = ["CloudflareTenantContext", "CloudflareCoreResult"]
