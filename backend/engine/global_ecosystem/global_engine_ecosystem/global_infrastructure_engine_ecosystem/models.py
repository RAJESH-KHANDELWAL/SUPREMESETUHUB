"""Typed metadata contracts for the infrastructure ENGINE layer."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class InfrastructureEngineModule:
    module_id: str
    name: str
    metadata: dict[str, Any] = field(default_factory=dict)
