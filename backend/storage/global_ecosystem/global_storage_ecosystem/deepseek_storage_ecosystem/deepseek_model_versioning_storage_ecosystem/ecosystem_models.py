"""Metadata model for DEEPSEEK_MODEL_VERSIONING_STORAGE_ECOSYSTEM; no provider data is fetched here."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()
@dataclass
class CategoryRecord:
    record_id: str
    name: str
    record_type: str = "MODEL_VERSIONING"
    jurisdiction: str = "GLOBAL"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)
    def __post_init__(self) -> None:
        if not self.record_id.strip() or not self.name.strip():
            raise ValueError("record_id and name are required")
