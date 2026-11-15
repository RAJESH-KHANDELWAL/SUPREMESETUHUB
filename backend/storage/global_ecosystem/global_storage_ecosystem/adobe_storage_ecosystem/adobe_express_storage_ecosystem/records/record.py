"""Storage metadata record; does not represent a live provider file."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
@dataclass
class StorageRecord:
    record_id: str
    name: str
    media_type: str = "application/octet-stream"
    provider_reference: str | None = None
    status: str = "METADATA_ONLY"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
