"""SERVER-owned orchestration value objects only."""
from dataclasses import dataclass, field
from typing import Any
@dataclass(frozen=True)
class LayerDescriptor:
    name: str
    responsibility: str
    owner_path: str
@dataclass
class ServerOrchestrationRequest:
    operation: str
    payload: dict[str, Any] = field(default_factory=dict)
    request_id: str | None = None
@dataclass
class ServerOrchestrationResult:
    success: bool
    operation: str
    status: str
    layers: dict[str, Any] = field(default_factory=dict)
    result: dict[str, Any] | None = None
    error: str | None = None
