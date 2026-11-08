"""Provider-specific ABELOHOST SERVER engine adapter boundary."""
from typing import Any

class ProviderEngine:
    provider = "ABELOHOST SERVER"
    layer = "ENGINE"

    def __init__(self, handler=None):
        self._handler = handler

    def health(self):
        configured = callable(self._handler)
        return {
            "provider": self.provider,
            "layer": self.layer,
            "status": "READY" if configured else "NOT_CONFIGURED",
            "execution_enabled": configured,
        }

    def execute(self, operation: str, payload: dict[str, Any] | None = None):
        if not callable(self._handler):
            raise NotImplementedError(f"{self.provider} adapter is not configured")
        if not operation or not operation.strip():
            raise ValueError("operation is required")
        return self._handler(operation.strip(), dict(payload or {}))

AbelohostServerEngine = ProviderEngine
