"""Independent ENGINE models for GLOBAL TOOLS."""
from dataclasses import dataclass, field
from typing import Any
@dataclass(frozen=True)
class EngineDescriptor:
    engine_id: str
    name: str
    provider: str
    capabilities: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)
@dataclass
class EngineExecution:
    execution_id: str
    status: str = "PENDING"
    output: Any = None
    error: str | None = None
