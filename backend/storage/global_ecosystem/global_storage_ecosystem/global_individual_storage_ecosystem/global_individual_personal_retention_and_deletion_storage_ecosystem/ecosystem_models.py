"""Metadata contract for GLOBAL_INDIVIDUAL_PERSONAL_RETENTION_AND_DELETION_STORAGE_ECOSYSTEM; no personal content, credentials or keys."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class CategoryRecord:
    record_id: str
    name: str
    record_type: str = "PERSONAL_RETENTION_AND_DELETION"
    owner_ref: str = ""
    jurisdiction: str = "GLOBAL"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    consent_ref: str | None = None
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if not self.record_id.strip() or not self.name.strip():
            raise ValueError("record_id and name are required")
        if self.record_type != "PERSONAL_RETENTION_AND_DELETION":
            raise ValueError("record_type must be PERSONAL_RETENTION_AND_DELETION")
        if not self.owner_ref or not self.owner_ref.strip():
            raise ValueError("opaque owner_ref is required")
        if not self.jurisdiction.strip() or not self.status.strip():
            raise ValueError("jurisdiction and status are required")
        if not isinstance(self.metadata, dict):
            raise ValueError("metadata must be an object")


EcosystemRecord = CategoryRecord
