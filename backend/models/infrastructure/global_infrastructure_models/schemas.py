"""Normalized cross-domain infrastructure model contracts."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class GlobalResourceIdentity:
    resource_id: str
    resource_type: str
    provider_id: str | None = None
    external_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GlobalResourceRelationship:
    source_resource_id: str
    target_resource_id: str
    relationship_type: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
