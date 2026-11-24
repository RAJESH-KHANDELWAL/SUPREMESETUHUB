"""Typed records used by Adobe ecosystem catalog services."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class AdobeCapability:
    key: str
    description: str
    maturity: str = "basic"
    regions: tuple[str, ...] = ("India", "Global")
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AdobeWorkflowRecord:
    workflow_id: str
    product: str
    operation: str
    status: str = "catalog_only"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: dict[str, Any] = field(default_factory=dict)
