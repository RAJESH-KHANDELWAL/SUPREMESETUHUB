"""Storage record model."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Record:
    record_id: str
    metadata: dict[str, Any] = field(default_factory=dict)
