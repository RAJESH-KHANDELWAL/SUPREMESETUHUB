"""Typed business ecosystem descriptors."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class BusinessEcosystemDescriptor:
    ecosystem_id: str
    name: str
    category: str
    package_path: str
    status: str
    parent_id: str = "global_business_ecosystem"
    metadata: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.ecosystem_id,
            "name": self.name,
            "category": self.category,
            "package_path": self.package_path,
            "status": self.status,
            "parent_id": self.parent_id,
            "metadata": dict(self.metadata or {}),
        }

__all__ = ["BusinessEcosystemDescriptor"]
