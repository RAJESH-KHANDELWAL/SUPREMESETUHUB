"""Configurable execution boundary for the global Kamasutra ENGINE ecosystem."""
from typing import Any, Callable


class ProviderEngine:
    provider = "GLOBAL KAMASUTRA RELATIONSHIP INTIMACY SEX CHUDAI PORN ADULT HEALTH WELLNESS"
    layer = "ENGINE"

    def __init__(self, handler: Callable | None = None):
        self._handler = handler

    def configure(self, handler: Callable):
        if not callable(handler):
            raise TypeError("handler must be callable")
        self._handler = handler
        return self

    def health(self):
        configured = callable(self._handler)
        return {
            "provider": self.provider,
            "layer": self.layer,
            "configured": configured,
            "status": "READY" if configured else "NOT_CONFIGURED",
        }

    def execute(self, operation: str, payload: dict[str, Any] | None = None):
        if not callable(self._handler):
            raise NotImplementedError(
                self.provider + " engine handler is not configured"
            )
        if not isinstance(operation, str) or not operation.strip():
            raise ValueError("operation is required")
        if payload is not None and not isinstance(payload, dict):
            raise TypeError("payload must be a dictionary")
        return self._handler(operation, dict(payload or {}))
