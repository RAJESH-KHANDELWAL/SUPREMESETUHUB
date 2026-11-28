"""Conservative retry policy; retries only explicitly idempotent requests."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    backoff_seconds: float = 0.5
    retry_statuses: tuple[int, ...] = (429, 500, 502, 503, 504)

    def __post_init__(self) -> None:
        if self.max_attempts < 1 or self.backoff_seconds < 0:
            raise ValueError("Invalid retry policy")
