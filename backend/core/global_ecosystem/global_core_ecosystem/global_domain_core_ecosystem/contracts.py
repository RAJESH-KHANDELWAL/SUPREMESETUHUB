"""Provider-neutral domain Core contracts."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


class DomainCoreStatus(str, Enum):
    CATALOG_ONLY = "CORE_CATALOG_ONLY"
    LIVE_VERIFICATION_REQUIRED = "LIVE_VERIFICATION_REQUIRED"


@dataclass(frozen=True)
class DomainProviderContract:
    provider_id: str
    display_name: str
    scope: str
    official_docs_url: str | None = None
    status: DomainCoreStatus = DomainCoreStatus.CATALOG_ONLY
    live_connection_verified: bool = False
    api_available: bool | None = None


@dataclass(frozen=True)
class DomainOperationRequest:
    provider_id: str
    operation: str
    domain_name: str | None = None
    tenant_id: str | None = None
    metadata: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class DomainReadiness:
    provider_id: str
    catalog_registered: bool
    live_connection_verified: bool
    execution_enabled: bool
    readiness: str

