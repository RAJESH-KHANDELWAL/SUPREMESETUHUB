"""Stable contracts for the provider-neutral GLOBAL STORAGE CORE control plane.

CORE describes storage providers and their capabilities. It does not transfer
bytes, call provider APIs, persist operational records, or manage credentials.
Those responsibilities belong to API, ENGINE, DATABASE, and STORAGE runtime
layers respectively.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


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
class SecretReference:
    """Opaque secret-manager pointer; never stores credential material."""
    provider: str
    reference: str
    version: str | None = None

    def __post_init__(self) -> None:
        if not self.provider.strip() or not self.reference.strip():
            raise ValueError("SECRET_REFERENCE_REQUIRED")


@dataclass(frozen=True)
class StorageProvider:
    provider_id: str
    display_name: str
    category: str
    capabilities: tuple[str, ...]
    regions: tuple[str, ...] = ()
    readiness: Readiness = Readiness.CATALOG_ONLY
    api_available: bool | None = None
    connection_verified: bool = False
    credential_reference_required: bool = True

    def __post_init__(self) -> None:
        if not self.provider_id.strip() or not self.display_name.strip():
            raise ValueError("PROVIDER_ID_AND_NAME_REQUIRED")
        if self.api_available is True and not self.connection_verified:
            raise ValueError("API_AVAILABILITY_REQUIRES_VERIFIED_CONNECTION")


@dataclass
class CoreResult:
    success: bool
    ecosystem_id: str = "GLOBAL-STORAGE-CORE-ECOSYSTEM"
    status: str = "CORE_CATALOG_ONLY"
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


__all__ = [
    "Readiness", "TenantContext", "SecretReference", "StorageProvider", "CoreResult",
]
