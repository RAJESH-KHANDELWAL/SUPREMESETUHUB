"""Provider-wide Cohere CORE event envelope; delivery belongs to ENGINE/runtime."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class CoreEvent:
    name: str
    payload: Mapping[str, Any] = field(default_factory=dict)
    event_id: str | None = None
    occurred_at: str | None = None
    correlation_id: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("event name must be a non-empty string")
        if not isinstance(self.payload, Mapping):
            raise ValueError("event payload must be a mapping")
