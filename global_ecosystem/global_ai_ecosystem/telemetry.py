"""Privacy-conscious, content-free adapter telemetry event contracts."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class ProviderCallEvent:
    provider_id: str
    operation: str
    outcome: str
    duration_ms: int
    status_code: int | None = None
    request_id: str | None = None
    occurred_at: str = ""

    def __post_init__(self) -> None:
        if self.duration_ms < 0:
            raise ValueError("duration_ms cannot be negative.")
        if not self.occurred_at:
            object.__setattr__(self, "occurred_at", datetime.now(timezone.utc).isoformat())
        if self.outcome not in {"success", "error", "rate_limited", "timeout"}:
            raise ValueError("Unsupported telemetry outcome.")

    def to_dict(self) -> dict[str, str | int | None]:
        """Serialize metadata only; prompts, completions and credentials are excluded."""
        return {
            "provider_id": self.provider_id,
            "operation": self.operation,
            "outcome": self.outcome,
            "duration_ms": self.duration_ms,
            "status_code": self.status_code,
            "request_id": self.request_id,
            "occurred_at": self.occurred_at,
        }
