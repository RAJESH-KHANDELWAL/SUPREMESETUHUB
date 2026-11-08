"""Fail-closed operation dispatch for GLOBAL SERVER ECOSYSTEM.

Concrete provider actions remain with provider/ENGINE adapters. SERVER only
routes an explicitly registered adapter and never simulates infrastructure work.
"""
from threading import RLock
from typing import Any
from .operation_catalog import get_capability, list_capabilities

class ServerOperationError(RuntimeError):
    """Base exception for SERVER operational dispatch."""

class UnknownServerCapability(ServerOperationError):
    """Raised when a capability is not part of the SERVER catalog."""

class ServerCapabilityNotConfigured(ServerOperationError):
    """Raised when no adapter has been explicitly registered."""

class ServerOperationService:
    domain = "SERVER"
    ecosystem = "GLOBAL_SERVER_ECOSYSTEM"

    def __init__(self):
        self._adapters: dict[str, Any] = {}
        self._lock = RLock()

    def register_adapter(self, capability: str, adapter: Any, *, replace: bool = False):
        item = get_capability(capability)
        if item is None:
            raise UnknownServerCapability(f"Unknown SERVER capability: {capability}")
        if adapter is None or not callable(getattr(adapter, "execute", None)):
            raise TypeError("Adapter must implement execute(operation, payload)")
        with self._lock:
            if item.key in self._adapters and not replace:
                raise ValueError(f"Adapter already registered: {item.key}")
            self._adapters[item.key] = adapter
        return {"capability": item.key, "status": "REGISTERED"}

    def unregister_adapter(self, capability: str) -> bool:
        item = get_capability(capability)
        if item is None:
            raise UnknownServerCapability(f"Unknown SERVER capability: {capability}")
        with self._lock:
            return self._adapters.pop(item.key, None) is not None

    def execute(self, capability: str, operation: str, payload: dict[str, Any] | None = None):
        item = get_capability(capability)
        if item is None:
            raise UnknownServerCapability(f"Unknown SERVER capability: {capability}")
        operation_name = str(operation or "").strip()
        if not operation_name:
            raise ValueError("operation is required")
        with self._lock:
            adapter = self._adapters.get(item.key)
        if adapter is None:
            raise ServerCapabilityNotConfigured(f"{item.key} adapter is not configured")
        result = adapter.execute(operation_name, dict(payload or {}))
        if result is None:
            normalized_result = {}
        elif isinstance(result, dict):
            normalized_result = result
        else:
            raise TypeError("SERVER adapter result must be a dict or None")
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "capability": item.key,
            "operation": operation_name,
            "status": "COMPLETED",
            "result": normalized_result,
        }

    def status(self):
        with self._lock:
            registered = set(self._adapters)
        return {
            "domain": self.domain,
            "capabilities": [
                {
                    "key": item.key,
                    "responsibility": item.responsibility,
                    "status": "ADAPTER_REGISTERED" if item.key in registered else "NOT_CONFIGURED",
                }
                for item in list_capabilities()
            ],
        }

__all__ = [
    "ServerOperationService", "ServerOperationError",
    "UnknownServerCapability", "ServerCapabilityNotConfigured",
]
