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
class GlobalProviderReference:
    provider_id: str
    external_id: str

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


@dataclass(frozen=True)
class GlobalResourceLifecycle:
    state: str
    created_at: str | None = None
    updated_at: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GlobalResourceLocation:
    region: str | None = None
    zone: str | None = None
    datacenter: str | None = None
    location: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GlobalResourceCapacity:
    cpu: str | None = None
    memory: str | None = None
    storage: str | None = None
    bandwidth: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
