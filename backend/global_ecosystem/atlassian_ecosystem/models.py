"""Immutable domain contracts; intentionally free of network and database I/O."""
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class AtlassianProduct:
    product_id: str
    display_name: str
    description: str
    api_family: str
    default_enabled: bool = False
    requires_admin_consent: bool = False

@dataclass(frozen=True)
class AtlassianRequestPlan:
    product_id: str
    operation: str
    resource: str
    payload: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.product_id.strip():
            raise ValueError("product_id is required")
        if not self.operation.strip():
            raise ValueError("operation is required")
        if not self.resource.strip():
            raise ValueError("resource is required")
        if not isinstance(self.payload, Mapping):
            raise TypeError("payload must be a mapping")
        if not isinstance(self.metadata, Mapping):
            raise TypeError("metadata must be a mapping")
