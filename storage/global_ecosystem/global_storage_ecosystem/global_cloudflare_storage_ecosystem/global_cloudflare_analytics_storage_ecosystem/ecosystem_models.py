"""Metadata-only category record."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class StorageCategoryRecord:
    record_id: str
    name: str
    metadata: dict[str, Any] = field(default_factory=dict)
    provider_id: str = "CLOUDFLARE"
    connection_state: str = "NOT_CONFIGURED"

    def __post_init__(self):
        if not self.record_id.strip() or not self.name.strip():
            raise ValueError("record_id and name are required")
        if self.connection_state != "NOT_CONFIGURED":
            raise ValueError("metadata cannot assert live provider connectivity")
