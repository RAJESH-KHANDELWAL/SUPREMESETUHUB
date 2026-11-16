"""Shared catalog contracts for the Global Infrastructure Ecosystem."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class CatalogRecord:
    """Provider-neutral metadata record; not proof of a live integration."""

    id: str
    name: str
    category: str
    description: str
    status: str = "CATALOG_ONLY"
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
