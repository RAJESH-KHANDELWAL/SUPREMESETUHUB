
"""GLOBAL ECOSYSTEM data models."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class GlobalEcosystemIdentity:
    """Identity and capabilities of a registered GLOBAL ECOSYSTEM."""

    ecosystem_id: str
    name: str
    ecosystem_type: str

    parent_id: Optional[str] = None
    repository_ref: Optional[str] = None

    status: str = "REGISTERED"
    enabled: bool = True

    capabilities: List[str] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    message: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert identity to a JSON-friendly dictionary."""

        return {
            "ecosystem_id": self.ecosystem_id,
            "name": self.name,
            "ecosystem_type": self.ecosystem_type,
            "parent_id": self.parent_id,
            "repository_ref": self.repository_ref,
            "status": self.status,
            "enabled": self.enabled,
            "capabilities": list(self.capabilities),
            "metadata": dict(self.metadata),
            "message": self.message,
        }


# Backward compatibility for existing registry imports.
EcosystemIdentity = GlobalEcosystemIdentity
