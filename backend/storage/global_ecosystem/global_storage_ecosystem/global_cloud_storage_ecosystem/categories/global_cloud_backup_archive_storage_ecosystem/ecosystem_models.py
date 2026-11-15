"""Category metadata model."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class StorageCategoryRecord:
    record_id: str
    name: str
    provider_id: str = "UNASSIGNED"
    metadata: dict[str, Any] = field(default_factory=dict)
