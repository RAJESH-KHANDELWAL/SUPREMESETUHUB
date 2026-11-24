"""Provider-neutral contracts for the Global Cloud Core control plane."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CloudReadiness(str, Enum):
    CATALOG_ONLY = "CATALOG_ONLY"
    DOCUMENTED = "DOCUMENTED"
    SCAFFOLD = "SCAFFOLD"
    CONFIGURED = "CONFIGURED"
    LIVE_VERIFIED = "LIVE_VERIFIED"


@dataclass(frozen=True)
class CloudTenantContext:
    """Tenant and actor hints supplied by authenticated application code.

    This is context metadata, not an authorization decision or credential.
    """

    tenant_id: str | None = None
    actor_id: str | None = None
    request_id: str | None = None


@dataclass(frozen=True)
class CloudCoreResult:
    success: bool
    ecosystem: str
    operation: str
    execution_performed: bool = False
    persistence_performed: bool = False
    live_connection_verified: bool = False


__all__ = ["CloudReadiness", "CloudTenantContext", "CloudCoreResult"]
