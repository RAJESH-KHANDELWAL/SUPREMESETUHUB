"""Stable provider-neutral contracts for Bada Business CORE."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass
class CoreResult:
    success: bool
    ecosystem_id: str = "BADA-BUSINESS-CORE-ECOSYSTEM"
    status: str = "OK"
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    timestamp: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
