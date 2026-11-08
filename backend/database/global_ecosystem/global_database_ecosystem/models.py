"""Independent database ecosystem metadata models; no API/CORE/ENGINE imports."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class DatabaseEcosystemDescriptor:
    ecosystem_id: str
    name: str
    provider_id: str | None = None
    capabilities: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class DatabaseHealth:
    status: str = "NOT_CONFIGURED"
    connection_verified: bool = False
    migration_status: str = "NOT_CHECKED"
    details: dict[str, Any] = field(default_factory=dict)
