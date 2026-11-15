"""Provider-neutral CLOUD layer data contracts."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class CloudProviderDescriptor:
    provider_id: str
    name: str
    category: str
    capabilities: tuple[str, ...]
    status: str = "not_configured"
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.provider_id.strip():
            raise ValueError("CLOUD_PROVIDER_ID_REQUIRED")
        object.__setattr__(self, "capabilities", tuple(self.capabilities))
        object.__setattr__(self, "metadata", dict(self.metadata))

@dataclass(frozen=True)
class CloudOperationRequest:
    provider_id: str
    operation: str
    resource: str
    parameters: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.provider_id.strip() or not self.operation.strip() or not self.resource.strip():
            raise ValueError("CLOUD_OPERATION_FIELDS_REQUIRED")
        object.__setattr__(self, "parameters", dict(self.parameters))

@dataclass(frozen=True)
class CloudOperationResult:
    provider_id: str
    operation: str
    status: str
    resource_id: str | None = None
    details: dict[str, Any] = field(default_factory=dict)
