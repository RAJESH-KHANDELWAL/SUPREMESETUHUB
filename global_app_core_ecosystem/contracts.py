"""Provider-neutral contracts for the Global App Core control plane."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AppReadiness(str, Enum):
    CATALOG_ONLY = "CATALOG_ONLY"
    DOCUMENTED = "DOCUMENTED"
    SCAFFOLD = "SCAFFOLD"
    CONFIGURED = "CONFIGURED"
    LIVE_VERIFIED = "LIVE_VERIFIED"


@dataclass(frozen=True)
class AppTenantContext:
    """Identity hints supplied by the authenticated application layer.

    This value is not an authorization decision and contains no credentials.
    """

    tenant_id: str | None = None
    actor_id: str | None = None
    request_id: str | None = None


@dataclass(frozen=True)
class AppCoreResult:
    success: bool
    ecosystem: str
    operation: str
    execution_performed: bool = False
    persistence_performed: bool = False
    live_connection_verified: bool = False


__all__ = ["AppReadiness", "AppTenantContext", "AppCoreResult"]
