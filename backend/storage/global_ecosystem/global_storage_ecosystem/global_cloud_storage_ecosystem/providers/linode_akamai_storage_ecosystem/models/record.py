"""Provider storage catalog record."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ProviderStorageRecord:
    record_id: str
    provider_id: str = "LINODE_AKAMAI"
    storage_type: str = "UNSPECIFIED"
    metadata: dict[str, Any] = field(default_factory=dict)
