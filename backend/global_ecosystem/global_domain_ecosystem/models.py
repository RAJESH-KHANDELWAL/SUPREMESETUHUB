"""Typed domain records for the global domain catalog."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class DomainProfile:
    domain_id: str
    name: str
    group: str
    geography: str = "bharat_india"
    maturity: str = "basic_normal"
    adult_only: bool = False
    controls: tuple[str, ...] = field(default_factory=tuple)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "domain_id": self.domain_id, "name": self.name, "group": self.group,
            "geography": self.geography, "maturity": self.maturity,
            "adult_only": self.adult_only, "controls": list(self.controls),
            "metadata": dict(self.metadata),
        }

__all__ = ["DomainProfile"]
