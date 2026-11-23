"""Typed contracts for the global agriculture and natural-resource CORE."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class CoreContext:
    region: str | None = None
    actor_ref: str | None = None
    tenant_ref: str | None = None
    purpose: str = "DISCOVERY"

@dataclass(frozen=True)
class CoreResult:
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    warnings: tuple[str, ...] = ()
