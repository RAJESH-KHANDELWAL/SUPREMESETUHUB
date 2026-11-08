"""Provider adapter boundary owned by GLOBAL SERVER.

An injected handler means execution is configured; it does not prove that an
external provider account is reachable. Health remains unprobed unless a
provider-specific adapter performs an explicit real health check.
"""
from __future__ import annotations
from typing import Any, Callable


class ServerProviderAdapter:
    provider_id = "unknown"
    display_name = "Unknown provider"
    capabilities = ("cloud-server-management",)

    def __init__(self, handler: Callable[[str, dict[str, Any]], Any] | None = None):
        self._handler = handler

    def describe(self) -> dict[str, Any]:
        configured = callable(self._handler)
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "CONFIGURED_NOT_PROBED" if configured else "NOT_CONFIGURED",
            "execution_enabled": configured,
        }

    def health(self) -> dict[str, Any]:
        configured = callable(self._handler)
        return {
            **self.describe(),
            "status": "NOT_PROBED" if configured else "NOT_CONFIGURED",
            "external_connection": "NOT_ATTEMPTED",
        }

    def execute(self, operation: str, payload: dict[str, Any] | None = None):
        name = str(operation or "").strip()
        if not name:
            raise ValueError("operation is required")
        if not callable(self._handler):
            raise NotImplementedError(f"{self.provider_id} provider handler is not configured")
        result = self._handler(name, dict(payload or {}))
        if result is not None and not isinstance(result, dict):
            raise TypeError("provider handler must return a dict or None")
        return dict(result or {})


__all__ = ["ServerProviderAdapter"]
