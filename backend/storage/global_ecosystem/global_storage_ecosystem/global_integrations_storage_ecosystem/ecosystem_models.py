"""Typed metadata contracts for GLOBAL INTEGRATIONS storage; no secrets or object bytes."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class EcosystemRecord:
    record_id: str
    record_type: str
    name: str
    jurisdiction: str = "GLOBAL"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    provider_ref: str | None = None
    owner_ref: str | None = None
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        for key in ("record_id", "record_type", "name", "jurisdiction", "status"):
            value = getattr(self, key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{key} is required")
        if not isinstance(self.metadata, dict):
            raise ValueError("metadata must be an object")
        for key in ("provider_ref", "owner_ref"):
            value = getattr(self, key)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                raise ValueError(f"{key} must be a non-empty opaque reference when provided")
