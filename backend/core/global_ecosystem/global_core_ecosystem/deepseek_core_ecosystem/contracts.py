"""Stable provider-level result contract for DeepSeek Core."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class DeepSeekCoreResult:
    success: bool
    ecosystem_id: str = "DEEPSEEK-CORE-ECOSYSTEM"
    status: str = "INTERFACE_ONLY"
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
