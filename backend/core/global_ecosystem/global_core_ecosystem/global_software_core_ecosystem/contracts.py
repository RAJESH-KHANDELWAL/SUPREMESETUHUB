"""Stable, provider-neutral contracts for software ecosystem metadata."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

ProviderStatus = Literal["CATALOG_ONLY", "CONFIGURED", "CONNECTED", "DEGRADED", "DISABLED"]


@dataclass(frozen=True)
class Capability:
    capability_id: str
    name: str
    domain: str
    description: str = ""
    api_reference: str | None = None


@dataclass(frozen=True)
class Provider:
    provider_id: str
    name: str
    package: str
    domains: tuple[str, ...]
    status: ProviderStatus = "CATALOG_ONLY"
    live_connection_verified: bool = False
    capabilities: tuple[str, ...] = ()
    documentation_url: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class LifecycleRecord:
    provider_id: str
    state: ProviderStatus
    tenant_id: str | None = None
    scopes: tuple[str, ...] = ()
    secret_reference: str | None = None
    verified_at: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
