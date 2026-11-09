"""Bada Business cloud integration request and policy contracts."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class BadaBusinessCloudRequest:
    capability_id: str
    operation: str
    provider_id: str
    resource: str
    parameters: dict[str, Any] = field(default_factory=dict)
    approved: bool = False

    def __post_init__(self) -> None:
        for field_name in ("capability_id", "operation", "provider_id", "resource"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"BADA_BUSINESS_CLOUD_{field_name.upper()}_REQUIRED")
        object.__setattr__(self, "parameters", dict(self.parameters))

@dataclass(frozen=True)
class BadaBusinessCloudResult:
    capability_id: str
    provider_id: str
    operation: str
    status: str
    details: dict[str, Any] = field(default_factory=dict)
