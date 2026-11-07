"""Google engine identity models."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class GoogleEngineIdentity:
    engine_id: str
    name: str
    engine_type: str
    status: str = "REGISTERED"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    api_catalog_ref: str | None = None
    core_catalog_ref: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "engine_id": self.engine_id,
            "name": self.name,
            "engine_type": self.engine_type,
            "status": self.status,
            "enabled": self.enabled,
            "capabilities": list(self.capabilities),
            "api_catalog_ref": self.api_catalog_ref,
            "core_catalog_ref": self.core_catalog_ref,
            "metadata": dict(self.metadata),
        }
