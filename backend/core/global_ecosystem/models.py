
"""GLOBAL ECOSYSTEM identity models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class GlobalEcosystemIdentity:
    """Identity and metadata for an ecosystem module."""

    ecosystem_id: str
    name: str
    ecosystem_type: str
    repository_ref: str | None = None
    status: str = "REGISTERED"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    message: str | None = None
    parent_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible representation."""

        return {
            "ecosystem_id": self.ecosystem_id,
            "name": self.name,
            "ecosystem_type": self.ecosystem_type,
            "repository_ref": self.repository_ref,
            "status": self.status,
            "enabled": self.enabled,
            "capabilities": list(self.capabilities),
            "metadata": dict(self.metadata),
            "message": self.message,
            "parent_id": self.parent_id,
        }


EcosystemIdentity = GlobalEcosystemIdentity
