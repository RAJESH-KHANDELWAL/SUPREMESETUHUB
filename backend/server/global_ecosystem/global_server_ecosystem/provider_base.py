"""Provider adapter boundary owned by GLOBAL SERVER.

A provider is operational only when an explicit callable handler is injected.
No network calls, credentials, or simulated infrastructure actions are used.
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
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "configured" if callable(self._handler) else "not_configured",
            "execution_enabled": callable(self._handler),
        }

    def health(self) -> dict[str, Any]:
        return {**self.describe(), "status": "READY" if callable(self._handler) else "NOT_CONFIGURED"}

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
