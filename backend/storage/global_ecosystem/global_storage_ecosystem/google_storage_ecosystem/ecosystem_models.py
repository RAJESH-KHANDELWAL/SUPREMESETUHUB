"""Typed metadata records for Google storage taxonomy categories."""
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
    category_group: str = "UNCLASSIFIED"
    package_name: str = ""
    jurisdiction: str = "GLOBAL"
    status: str = "CATALOG_ONLY"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        for key in ("record_id", "record_type", "name"):
            if not str(getattr(self, key)).strip():
                raise ValueError(f"{key} is required")
