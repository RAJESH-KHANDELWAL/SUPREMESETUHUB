"""Typed domain contracts; no network or persistence side effects."""
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class AnthropicCapability:
    capability_id: str
    display_name: str
    description: str
    api_surface: str
    enabled_by_default: bool = False
    requires_explicit_permission: bool = False
    status: str = "CATALOG_ONLY"

@dataclass(frozen=True)
class AnthropicRequestPlan:
    """Validated intent handed to separately-owned API/engine layers."""
    capability_id: str
    operation: str
    payload: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.capability_id.strip():
            raise ValueError("capability_id is required")
        if not self.operation.strip():
            raise ValueError("operation is required")
        if not isinstance(self.payload, Mapping):
            raise TypeError("payload must be a mapping")
        if not isinstance(self.metadata, Mapping):
            raise TypeError("metadata must be a mapping")
