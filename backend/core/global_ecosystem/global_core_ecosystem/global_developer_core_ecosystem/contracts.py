"""Provider-neutral contracts for Global Developer Core."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass(frozen=True)
class DeveloperProviderDescriptor:
    provider_id: str
    ecosystem_id: str
    name: str
    core_module: str
    api_catalog_ref: str
    status: str = "CORE_CATALOG_ONLY"
    live_connection_verified: bool = False
    capabilities: tuple[str, ...] = ("PROVIDER_DISCOVERY", "CAPABILITY_METADATA", "LIFECYCLE_METADATA")

@dataclass(frozen=True)
class DeveloperReadiness:
    status: str = "CORE_CATALOG_ONLY"
    connected: bool = False
    live_connection_verified: bool = False
    evidence_ref: str | None = None

@dataclass(frozen=True)
class DeveloperCoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
