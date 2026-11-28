"""Stable metadata contracts for the transport CORE layer."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass(frozen=True)
class TransportDomainContext:
    domain_id: str
    tenant_id: str
    request_id: str | None = None

    def validate(self) -> None:
        if not self.domain_id.strip():
            raise ValueError("TRANSPORT_DOMAIN_ID_REQUIRED")
        if not self.tenant_id.strip():
            raise ValueError("TENANT_ID_REQUIRED")

@dataclass
class TransportCoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
