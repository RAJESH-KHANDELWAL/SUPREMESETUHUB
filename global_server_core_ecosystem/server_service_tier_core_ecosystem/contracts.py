"""Provider-neutral service_tier SERVER CORE metadata contract."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any

DOMAIN_ID = "SERVICE_TIER"
CAPABILITY = "SERVICE_TIER"

@dataclass(frozen=True)
class ServiceTierContract:
    """Validated metadata declaration; performs no remote operation."""
    resource_id: str
    status: str = "DECLARED"
    metadata: dict[str, Any] | None = None

    def validate(self) -> None:
        if not self.resource_id or not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if self.status not in {"DECLARED", "REVIEW_REQUIRED", "APPROVED", "RESTRICTED", "RETIRED"}:
            raise ValueError(f"unsupported status: {self.status}")
        if self.metadata is not None and not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)
