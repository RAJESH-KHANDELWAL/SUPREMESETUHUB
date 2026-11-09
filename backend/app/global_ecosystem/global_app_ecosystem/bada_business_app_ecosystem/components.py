"""APP-owned component descriptors for Bada Business modules."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from .catalog import APP_MODULES

@dataclass(frozen=True)
class BadaBusinessAppComponent:
    component_id: str
    name: str
    purpose: str
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "metadata", dict(self.metadata))

def build_default_components() -> tuple[BadaBusinessAppComponent, ...]:
    return tuple(
        BadaBusinessAppComponent(
            component_id=item["id"],
            name=item["name"],
            purpose=item["purpose"],
            metadata={"api_capability": item["api_capability"], "ai_capability": item["ai_capability"]},
        )
        for item in APP_MODULES
    )
