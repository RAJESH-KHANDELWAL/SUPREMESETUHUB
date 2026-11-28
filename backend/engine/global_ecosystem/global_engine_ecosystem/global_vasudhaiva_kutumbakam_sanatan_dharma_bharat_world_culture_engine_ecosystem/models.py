"""Typed metadata contracts for the cultural knowledge ENGINE layer."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class CulturalEngineDomain:
    domain_id: str
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
