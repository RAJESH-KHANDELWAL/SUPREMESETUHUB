"""Typed metadata models shared by ecosystem domains."""
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
    created_at: str = field(default_factory=utc_now)
    def __post_init__(self):
        for key in ("record_id", "record_type", "name"):
            if not str(getattr(self, key)).strip():
                raise ValueError(f"{key} is required")
