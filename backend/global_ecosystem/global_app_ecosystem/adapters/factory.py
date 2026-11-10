"""Explicit adapter registry; provider modules are injected, never auto-connected."""
from __future__ import annotations
from collections.abc import Callable
from typing import Any
from .errors import ProviderNotRegisteredError

class AppAdapterFactory:
    def __init__(self) -> None:
        self._builders: dict[str, Callable[..., Any]] = {}

    def register(self, provider_id: str, builder: Callable[..., Any]) -> None:
        key = str(provider_id).strip().lower()
        if not key or not callable(builder):
            raise ValueError("provider_id and callable builder are required")
        if key in self._builders:
            raise ValueError(f"adapter already registered: {key}")
        self._builders[key] = builder

    def create(self, provider_id: str, **kwargs: Any) -> Any:
        key = str(provider_id).strip().lower()
        try:
            builder = self._builders[key]
        except KeyError as exc:
            raise ProviderNotRegisteredError(f"no adapter registered for {key!r}") from exc
        return builder(**kwargs)

    def registered(self) -> tuple[str, ...]:
        return tuple(sorted(self._builders))

__all__ = ["AppAdapterFactory"]
