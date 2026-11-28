"""Category domain models."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class StorageRecord:
    record_id: str
    metadata: dict[str, Any] = field(default_factory=dict)
