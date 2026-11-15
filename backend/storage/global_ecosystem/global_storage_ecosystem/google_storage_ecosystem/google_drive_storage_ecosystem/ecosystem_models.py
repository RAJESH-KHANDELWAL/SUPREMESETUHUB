"""Metadata contract for GOOGLE_DRIVE_STORAGE_ECOSYSTEM; no provider content or secrets are stored."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class CategoryRecord:
    record_id: str
    name: str
    record_type: str = "DRIVE"
    owner_ref: str | None = None
    jurisdiction: str = "GLOBAL"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    consent_ref: str | None = None
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if not self.record_id.strip() or not self.name.strip():
            raise ValueError("record_id and name are required")
        if self.owner_ref is not None and not self.owner_ref.strip():
            raise ValueError("owner_ref must be an opaque non-empty reference")


EcosystemRecord = CategoryRecord
