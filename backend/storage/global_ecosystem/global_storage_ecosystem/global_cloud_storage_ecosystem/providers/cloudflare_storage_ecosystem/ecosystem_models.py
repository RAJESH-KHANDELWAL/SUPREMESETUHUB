"""Provider-neutral metadata contracts; no SDK clients."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ProviderStorageMetadata:
    record_id: str
    service_type: str
    name: str
    region: str = "UNVERIFIED"
    metadata: dict[str, Any] = field(default_factory=dict)
