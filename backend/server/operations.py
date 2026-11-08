"""Explicit-adapter execution boundary for SERVER operational capabilities.

No operation is simulated. A capability runs only when its owning provider or
infrastructure adapter has been explicitly registered by the application.
"""
from threading import RLock
from typing import Any
from .operation_catalog import get_capability, list_capabilities

class ServerOperationError(RuntimeError):
    """Base error for SERVER operational dispatch."""

class UnknownServerCapability(ServerOperationError):
    pass

class ServerCapabilityNotConfigured(ServerOperationError):
    pass

class ServerOperationService:
    domain = "SERVER"

    def __init__(self):
        self._adapters: dict[str, Any] = {}
        self._lock = RLock()

    def register_adapter(self, capability: str, adapter: Any, *, replace: bool = False):
        item = get_capability(capability)
        if item is None:
            raise UnknownServerCapability(f"Unknown SERVER capability: {capability}")
        if adapter is None or not callable(getattr(adapter, "execute", None)):
            raise TypeError("SERVER adapters must implement execute(operation, payload)")
        with self._lock:
            if item.key in self._adapters and not replace:
                raise ValueError(f"Adapter already registered: {item.key}")
            self._adapters[item.key] = adapter
        return {"capability": item.key, "status": "REGISTERED"}

    def unregister_adapter(self, capability: str):
        item = get_capability(capability)
        if item is None:
            raise UnknownServerCapability(f"Unknown SERVER capability: {capability}")
        with self._lock:
            return self._adapters.pop(item.key, None) is not None

    def execute(self, capability: str, operation: str, payload: dict[str, Any] | None = None):
        item = get_capability(capability)
        if item is None:
            raise UnknownServerCapability(f"Unknown SERVER capability: {capability}")
        with self._lock:
            adapter = self._adapters.get(item.key)
        if adapter is None:
            raise ServerCapabilityNotConfigured(f"{item.key} adapter is not configured")
        if not str(operation or "").strip():
            raise ValueError("operation is required")
        result = adapter.execute(str(operation).strip(), dict(payload or {}))
        return {"domain": self.domain, "capability": item.key,
                "operation": str(operation).strip(), "status": "COMPLETED",
                "result": dict(result or {})}

    def status(self):
        with self._lock:
            registered = set(self._adapters)
        return {
            "domain": self.domain,
            "capabilities": [
                {"key": item.key, "responsibility": item.responsibility,
                 "status": "ADAPTER_REGISTERED" if item.key in registered else "NOT_CONFIGURED"}
                for item in list_capabilities()
            ],
        }

__all__ = ["ServerOperationService", "ServerOperationError",
           "UnknownServerCapability", "ServerCapabilityNotConfigured"]
