"""Shared typed contracts for Cohere CORE."""
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class CapabilityRequest:
    capability: str
    inputs: Mapping[str, Any]
    model: str | None = None
    options: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class CoreResult:
    ok: bool
    capability: str
    data: Mapping[str, Any] = field(default_factory=dict)
    errors: tuple[str, ...] = ()
    status: str = "validated"
