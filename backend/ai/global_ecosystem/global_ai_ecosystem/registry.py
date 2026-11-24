"""Explicit in-memory adapter registry; registration never occurs implicitly."""
from __future__ import annotations

from threading import RLock
from typing import Any, Callable

from .schemas import ProviderRegistration


class AIAdapterRegistry:
    def __init__(self) -> None:
        self._lock = RLock()
        self._adapters: dict[str, dict[str, Any]] = {}

    def register(
        self,
        provider_id: str,
        *,
        capabilities: list[str] | tuple[str, ...],
        handler: Callable[..., Any],
        models: list[str] | tuple[str, ...] = (),
    ) -> dict[str, Any]:
        key = provider_id.strip().lower()
        if not key:
            raise ValueError("AI_PROVIDER_ID_REQUIRED")
        if not callable(handler):
            raise ValueError("AI_ADAPTER_HANDLER_REQUIRED")
        caps = tuple(sorted({str(item).strip().lower() for item in capabilities if str(item).strip()}))
        if not caps:
            raise ValueError("AI_CAPABILITIES_REQUIRED")
        registration = ProviderRegistration(
            provider_id=key,
            capabilities=caps,
            models=tuple(str(item).strip() for item in models if str(item).strip()),
        )
        with self._lock:
            self._adapters[key] = {"registration": registration, "handler": handler}
        return self.describe(key)

    def unregister(self, provider_id: str) -> bool:
        key = provider_id.strip().lower()
        with self._lock:
            return self._adapters.pop(key, None) is not None

    def describe(self, provider_id: str) -> dict[str, Any]:
        key = provider_id.strip().lower()
        with self._lock:
            item = self._adapters.get(key)
            if item is None:
                raise KeyError("AI_PROVIDER_NOT_REGISTERED")
            reg = item["registration"]
            return {
                "provider_id": reg.provider_id,
                "capabilities": list(reg.capabilities),
                "models": list(reg.models),
                "status": reg.status,
            }

    def list(self) -> list[dict[str, Any]]:
        with self._lock:
            keys = sorted(self._adapters)
        return [self.describe(key) for key in keys]

    def execute(self, provider_id: str, capability: str, **payload: Any) -> Any:
        key = provider_id.strip().lower()
        cap = capability.strip().lower()
        with self._lock:
            item = self._adapters.get(key)
        if item is None:
            raise KeyError("AI_PROVIDER_NOT_REGISTERED")
        registration = item["registration"]
        if cap not in registration.capabilities:
            raise ValueError("AI_CAPABILITY_NOT_REGISTERED_FOR_PROVIDER")
        return item["handler"](capability=cap, **payload)
