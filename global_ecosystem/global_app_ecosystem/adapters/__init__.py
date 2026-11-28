"""Shared adapter contracts for provider-specific app integrations."""
from typing import Any, Protocol, runtime_checkable
from collections.abc import Mapping

@runtime_checkable
class AppProviderAdapter(Protocol):
    provider: dict[str, Any]
    @property
    def configured(self) -> bool: ...
    def execute(self, operation: str, payload: Mapping[str, Any] | None = None) -> Any: ...

__all__ = ["AppProviderAdapter"]
