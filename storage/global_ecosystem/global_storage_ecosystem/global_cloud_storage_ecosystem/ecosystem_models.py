"""Typed storage catalog records; provider operations live outside this package."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class CloudStorageRecord:
    """Catalog metadata for a provider/service; not a live connection record."""

    record_id: str
    provider_id: str
    storage_type: str
    name: str
    region: str = "UNVERIFIED"
    connection_state: str = "NOT_CONFIGURED"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        for field_name in ("record_id", "provider_id", "storage_type", "name"):
            if not str(getattr(self, field_name)).strip():
                raise ValueError(f"{field_name} is required")
        if self.connection_state != "NOT_CONFIGURED":
            raise ValueError(
                "Provider connection state requires a separately authorized "
                "and verified integration"
            )
