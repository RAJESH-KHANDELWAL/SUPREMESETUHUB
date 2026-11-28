"""Contracts for domain Core metadata; runtime adapters belong to API/ENGINE layers."""
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class DomainCoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any]
    error: str | None = None
