"""Metadata model for GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM; no personal content is stored."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class CategoryRecord:
    record_id: str
    name: str
    record_type: str = "INDIVIDUAL"
    owner_ref: str = ""
    jurisdiction: str = "GLOBAL"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    consent_ref: str | None = None
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if not self.record_id.strip() or not self.name.strip():
            raise ValueError("record_id and name are required")
        if not self.owner_ref:
            raise ValueError("opaque owner_ref is required")


# Backward-compatible alias for the existing registry interface.
EcosystemRecord = CategoryRecord
