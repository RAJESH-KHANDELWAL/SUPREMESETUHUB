"""People, Work, and Business Global Engine domain contracts.

This package belongs to backend/global_ecosystem and is independent of the
execution-oriented MAIN ENGINE under backend/engine.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

ROOT_ID = "GLOBAL-ENGINE-ECOSYSTEM"
SUPPORTED_DOMAINS = ("PEOPLE", "WORK", "BUSINESS")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class EcosystemIdentity:
    ecosystem_id: str
    name: str
    ecosystem_type: str = "PEOPLE"
    status: str = "REGISTERED"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    parent_id: str | None = ROOT_ID
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "ecosystem_id": self.ecosystem_id,
            "name": self.name,
            "ecosystem_type": self.ecosystem_type,
            "status": self.status,
            "enabled": self.enabled,
            "capabilities": list(self.capabilities),
            "metadata": dict(self.metadata),
            "parent_id": self.parent_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


ROOT = {
    "ecosystem_id": ROOT_ID,
    "name": "PEOPLE WORK BUSINESS GLOBAL ECOSYSTEM",
    "ecosystem_type": "PEOPLE_WORK_BUSINESS",
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": ["PEOPLE", "WORK", "BUSINESS"],
    "parent_id": None,
    "metadata": {"owner_layer": "GLOBAL_ECOSYSTEM"},
}
