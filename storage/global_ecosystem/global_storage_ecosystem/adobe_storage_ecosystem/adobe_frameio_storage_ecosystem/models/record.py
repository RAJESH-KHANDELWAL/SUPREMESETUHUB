"""Public model exports for ADOBE_FRAMEIO_STORAGE_ECOSYSTEM."""
from ..ecosystem_models import CategoryRecord
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class StorageObjectRecord:
    provider_id: str
    ecosystem_id: str
    object_id: str
    name: str
    object_type: str = "FILE"
    parent_id: str | None = None
    mime_type: str | None = None
    size_bytes: int | None = None
    checksum: str | None = None
    version_id: str | None = None
    owner_id: str | None = None
    lifecycle_state: str = "DISCOVERED"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def __post_init__(self) -> None:
        for key in ("provider_id", "ecosystem_id", "object_id", "name"):
            value = getattr(self, key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{key.upper()}_REQUIRED")
        if self.size_bytes is not None and self.size_bytes < 0:
            raise ValueError("SIZE_BYTES_MUST_BE_NON_NEGATIVE")
        if not isinstance(self.metadata, dict):
            raise ValueError("METADATA_MUST_BE_A_DICTIONARY")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
