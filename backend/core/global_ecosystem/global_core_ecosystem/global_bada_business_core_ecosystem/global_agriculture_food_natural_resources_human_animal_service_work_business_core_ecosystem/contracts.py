"""Business-layer contracts."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class BusinessCapability:
    capability_id: str
    domain_id: str
    service_work_business: tuple[str, ...] = ("SERVICE", "WORK", "BUSINESS")
    metadata: dict[str, Any] = field(default_factory=dict)
