"""Typed storage metadata record."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class StorageMetadataRecord:
    record_id: str
    name: str
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
