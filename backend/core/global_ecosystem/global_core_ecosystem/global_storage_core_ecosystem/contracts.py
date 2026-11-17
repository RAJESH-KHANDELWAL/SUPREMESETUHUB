"""Stable provider-neutral storage CORE contracts."""
from dataclasses import asdict, dataclass, field
from typing import Any, Literal
ProviderStatus = Literal["CATALOG_ONLY","CONFIGURED","CONNECTED","DEGRADED","DISABLED"]
@dataclass(frozen=True)
class StorageProvider:
    provider_id: str
    name: str
    package: str
    domains: tuple[str,...]
    capabilities: tuple[str,...]
    status: ProviderStatus = "CATALOG_ONLY"
    live_connection_verified: bool = False
    metadata: dict[str,Any] = field(default_factory=dict)
    def to_dict(self): return asdict(self)
@dataclass(frozen=True)
class StorageResourceMetadata:
    tenant_id: str
    resource_id: str
    provider_id: str
    resource_type: str
    region: str|None = None
    encryption_at_rest: bool|None = None
    retention_class: str|None = None
    metadata: dict[str,Any] = field(default_factory=dict)
