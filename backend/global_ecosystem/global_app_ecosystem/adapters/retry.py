"""Bounded retry utility for idempotent provider operations."""
from __future__ import annotations
from dataclasses import dataclass
import time
from typing import Callable, TypeVar
T=TypeVar("T")

@dataclass(frozen=True, slots=True)
class RetryPolicy:
    attempts: int = 3
    base_delay_seconds: float = 0.2
    max_delay_seconds: float = 2.0
    def __post_init__(self):
        if self.attempts < 1 or self.base_delay_seconds < 0 or self.max_delay_seconds < 0:
            raise ValueError("invalid retry policy")

def run_with_retry(operation: Callable[[], T], *, policy: RetryPolicy = RetryPolicy(), retry_on=(TimeoutError,)) -> T:
    for attempt in range(policy.attempts):
        try:
            return operation()
        except retry_on:
            if attempt + 1 >= policy.attempts:
                raise
            time.sleep(min(policy.base_delay_seconds * (2 ** attempt), policy.max_delay_seconds))
    raise RuntimeError("unreachable retry state")

__all__ = ["RetryPolicy", "run_with_retry"]
