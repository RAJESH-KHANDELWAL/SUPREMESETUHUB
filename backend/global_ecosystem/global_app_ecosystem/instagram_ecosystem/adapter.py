"""Explicit handler boundary for Instagram; no undocumented API calls."""
from __future__ import annotations
from collections.abc import Callable, Mapping
from typing import Any
from .catalog import PROVIDER
from .config import ProviderConfig

Handler = Callable[[str, Mapping[str, Any]], Any]

class InstagramAppAdapter:
    provider = PROVIDER

    def __init__(self, config: ProviderConfig | None = None, handler: Handler | None = None):
        self.config = config or ProviderConfig.from_env()
        self._handler = handler

    @property
    def configured(self) -> bool:
        return self.config.configured and self._handler is not None

    def execute(self, operation: str, payload: Mapping[str, Any] | None = None) -> Any:
        if not isinstance(operation, str) or not operation.strip():
            raise ValueError("operation must be a non-empty string")
        if not self.config.configured:
            raise RuntimeError("Instagram credentials are not configured")
        if self._handler is None:
            raise RuntimeError("Instagram handler is not installed; no live API call was attempted")
        return self._handler(operation, payload or {})

__all__ = ["InstagramAppAdapter"]
