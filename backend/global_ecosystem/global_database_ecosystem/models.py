"""Typed domain records for the global database ecosystem catalog."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class DatabaseCapability:
    capability_id: str
    domain: str
    description: str
    maturity: str = "normal"
    regions: tuple[str, ...] = ("bharat", "global")
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.capability_id.strip():
            raise ValueError("capability_id is required")
        if self.maturity not in {"normal", "standard", "professional", "enterprise", "advanced", "supreme"}:
            raise ValueError("unsupported maturity level")

@dataclass(frozen=True)
class DataWorkload:
    workload_id: str
    industry: str
    description: str
    data_classes: tuple[str, ...] = ()
    compliance_tags: tuple[str, ...] = ()
    safeguards: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.workload_id.strip() or not self.industry.strip():
            raise ValueError("workload_id and industry are required")

@dataclass(frozen=True)
class DatabasePlatform:
    platform_id: str
    name: str
    database_model: str
    deployment_modes: tuple[str, ...] = ("self_hosted", "managed_cloud")
    regions: tuple[str, ...] = ("bharat", "global")
    capabilities: tuple[str, ...] = ()
    integration_status: str = "catalog_only"
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.platform_id.strip() or not self.name.strip():
            raise ValueError("platform_id and name are required")
        if self.integration_status not in {"catalog_only", "adapter_available", "connected", "verified"}:
            raise ValueError("invalid integration_status")
