"""Lifecycle manager for the GLOBAL CLOUD ECOSYSTEM facade."""
from __future__ import annotations
from typing import Any
from .service import GlobalCloudEcosystemService

class GlobalCloudEcosystemManager:
    def __init__(self, adapters: tuple[Any, ...] = ()) -> None:
        self.service = GlobalCloudEcosystemService(adapters=adapters)
        self._initialized = False

    def initialize(self) -> dict[str, Any]:
        self._initialized = True
        return self.status()

    def status(self) -> dict[str, Any]:
        result = self.service.status()
        result["initialized"] = self._initialized
        return result

    def diagnostics(self) -> dict[str, Any]:
        providers = self.service.provider_status()
        configured = [item["provider_id"] for item in providers if item["status"] == "adapter_injected"]
        return {
            "status": "ok",
            "checks": {
                "provider_catalog": "ready",
                "adapter_registry": "ready",
                "configured_adapters": configured,
                "live_connectivity": "not_verified",
            },
        }
