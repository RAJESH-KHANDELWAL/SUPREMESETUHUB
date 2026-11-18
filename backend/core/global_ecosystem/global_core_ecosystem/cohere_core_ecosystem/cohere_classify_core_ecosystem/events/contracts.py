"""Capability event data contract; delivery is owned by runtime."""
from dataclasses import dataclass, field
from typing import Any, Mapping
@dataclass(frozen=True)
class CapabilityEvent:
    name: str
    capability: str = "classify"
    payload: Mapping[str, Any] = field(default_factory=dict)
