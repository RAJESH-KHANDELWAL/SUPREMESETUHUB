"""Stable contracts shared by app-provider adapters."""
from __future__ import annotations
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

@dataclass(frozen=True, slots=True)
class AppOperation:
    name: str
    payload: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("operation name must be non-empty")

@runtime_checkable
class AppProviderAdapter(Protocol):
    provider: Mapping[str, Any]
    @property
    def configured(self) -> bool: ...
    def execute(self, operation: str, payload: Mapping[str, Any] | None = None) -> Any: ...

__all__ = ["AppOperation", "AppProviderAdapter"]
