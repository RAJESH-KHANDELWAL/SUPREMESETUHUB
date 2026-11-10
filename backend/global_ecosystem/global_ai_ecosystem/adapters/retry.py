"""Conservative retry policy for explicitly idempotent provider requests."""
from __future__ import annotations

from dataclasses import dataclass
import random
import time


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    max_attempts: int = 1
    base_delay_seconds: float = 0.5
    max_delay_seconds: float = 8.0

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be at least 1.")
        if self.base_delay_seconds < 0 or self.max_delay_seconds < 0:
            raise ValueError("Retry delays cannot be negative.")

    def wait(self, attempt: int, retry_after: float | None = None) -> None:
        if retry_after is not None:
            delay = min(max(retry_after, 0.0), self.max_delay_seconds)
        else:
            ceiling = min(self.base_delay_seconds * (2 ** max(attempt - 1, 0)), self.max_delay_seconds)
            delay = random.uniform(0.0, ceiling) if ceiling else 0.0
        time.sleep(delay)
