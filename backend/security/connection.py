"""Explicit, fail-closed security capability connection registry."""

from __future__ import annotations

from dataclasses import dataclass
from threading import RLock
from typing import Any, Protocol


class SecurityAdapter(Protocol):
    """Minimal contract for an explicitly injected security adapter."""

    def health(self) -> dict[str, Any]: ...


@dataclass(frozen=True, slots=True)
class ConnectionSnapshot:
    name: str
    configured: bool
    healthy: bool
    detail: str = ""


class SecurityConnection:
    """Track adapters without importing or silently constructing providers."""

    def __init__(self) -> None:
        self._adapters: dict[str, SecurityAdapter] = {}
        self._lock = RLock()

    def register(self, name: str, adapter: SecurityAdapter) -> None:
        key = self._normalize_name(name)
        if not callable(getattr(adapter, "health", None)):
            raise TypeError("SECURITY_ADAPTER_MUST_EXPOSE_HEALTH")
        with self._lock:
            self._adapters[key] = adapter

    def unregister(self, name: str) -> bool:
        key = self._normalize_name(name)
        with self._lock:
            return self._adapters.pop(key, None) is not None

    def inspect(self, name: str) -> ConnectionSnapshot:
        key = self._normalize_name(name)
        with self._lock:
            adapter = self._adapters.get(key)
        if adapter is None:
            return ConnectionSnapshot(key, False, False, "NOT_CONFIGURED")
        try:
            result = adapter.health()
        except Exception:
            return ConnectionSnapshot(key, True, False, "HEALTH_CHECK_FAILED")
        healthy = isinstance(result, dict) and result.get("healthy") is True
        detail = str(result.get("detail", "")) if isinstance(result, dict) else "INVALID_HEALTH_RESPONSE"
        return ConnectionSnapshot(key, True, healthy, detail)

    def connect(self) -> dict[str, Any]:
        """Return a truthful registry summary; no network connection is implied."""
        with self._lock:
            names = tuple(self._adapters)
        snapshots = [self.inspect(name) for name in names]
        return {
            "security": "SUPREMESETUHUB",
            "status": "CONNECTED" if snapshots and all(x.healthy for x in snapshots) else "NOT_READY",
            "registered_adapters": len(snapshots),
            "healthy_adapters": sum(item.healthy for item in snapshots),
            "connections": [
                {
                    "name": item.name,
                    "configured": item.configured,
                    "healthy": item.healthy,
                    "detail": item.detail,
                }
                for item in snapshots
            ],
        }

    @staticmethod
    def _normalize_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("SECURITY_CONNECTION_NAME_REQUIRED")
        return name.strip().lower().replace(" ", "_")
