"""Configurable, offline-safe ENGINE execution boundary."""
from __future__ import annotations
from typing import Any, Callable

class ProviderEngine:
    """Executes only through an explicitly injected provider handler."""
    provider = __package__.rsplit(".", 1)[-1].replace("_", " ").upper()

    def __init__(self, handler: Callable[[str, dict[str, Any]], Any] | None = None) -> None:
        self._handler = handler

    def health(self) -> dict[str, str]:
        return {"provider": self.provider, "layer": "ENGINE",
                "status": "READY" if callable(self._handler) else "NOT_CONFIGURED"}

    def execute(self, operation: str, payload: dict[str, Any] | None = None) -> Any:
        if not operation or not isinstance(operation, str):
            raise ValueError("ENGINE_OPERATION_REQUIRED")
        if not callable(self._handler):
            raise NotImplementedError(f"{self.provider} ENGINE handler is not configured")
        return self._handler(operation, dict(payload or {}))
