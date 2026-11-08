"""Fail-closed SECURITY provider adapter boundary."""
from typing import Any, Callable

class SecurityProviderAdapter:
    provider_id = "unknown"
    display_name = "Unknown security provider"

    def __init__(self, *, handler: Callable[[str, dict[str, Any]], dict[str, Any]] | None = None, health_probe: Callable[[], dict[str, Any]] | None = None):
        self._handler = handler
        self._health_probe = health_probe

    def describe(self):
        return {"provider_id": self.provider_id, "display_name": self.display_name, "execution_configured": callable(self._handler), "health_probe_configured": callable(self._health_probe)}

    def health(self):
        if not callable(self._health_probe):
            return {"provider_id": self.provider_id, "status": "NOT_PROBED", "healthy": False, "external_connection": "NOT_ATTEMPTED"}
        try:
            result = self._health_probe()
        except Exception:
            return {"provider_id": self.provider_id, "status": "PROBE_FAILED", "healthy": False, "external_connection": "ATTEMPTED"}
        if not isinstance(result, dict) or result.get("healthy") is not True:
            return {"provider_id": self.provider_id, "status": "UNHEALTHY", "healthy": False, "external_connection": "ATTEMPTED"}
        return {"provider_id": self.provider_id, "status": "HEALTHY", "healthy": True, "external_connection": "VERIFIED"}

    def execute(self, operation: str, payload: dict[str, Any] | None = None):
        name = str(operation or "").strip()
        if not name:
            raise ValueError("operation is required")
        if not callable(self._handler):
            raise NotImplementedError(f"{self.provider_id} security handler is not configured")
        result = self._handler(name, dict(payload or {}))
        if not isinstance(result, dict):
            raise TypeError("security provider handler must return a dictionary")
        return result

__all__ = ["SecurityProviderAdapter"]
