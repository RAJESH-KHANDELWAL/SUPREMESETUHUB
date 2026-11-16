"""Bada Business APP composition service with injected layer interfaces."""
from __future__ import annotations
from typing import Any
from .catalog import get_app_catalog
from .components import build_default_components
from .registry import BadaBusinessAppRegistry
from .lifecycle import AppState, BadaBusinessAppLifecycle

class BadaBusinessAppService:
    """Compose APP metadata and injected API/AI facades without owning their logic."""
    def __init__(self, api_service: Any = None, ai_service: Any = None) -> None:
        self.api_service = api_service
        self.ai_service = ai_service
        self.registry = BadaBusinessAppRegistry()
        self.lifecycle = BadaBusinessAppLifecycle()

    def configure(self) -> dict[str, Any]:
        if self.lifecycle.state == AppState.READY:
            return self.status()
        self.registry.register_defaults()
        if self.lifecycle.state == AppState.CREATED:
            self.lifecycle.transition(AppState.REGISTERED)
        self.lifecycle.transition(AppState.READY)
        return self.status()

    def catalog(self) -> dict[str, Any]:
        return get_app_catalog()

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem": "BADA_BUSINESS_APP_ECOSYSTEM",
            "layer": "APP",
            "state": self.lifecycle.state.value,
            "registered_components": [item.component_id for item in self.registry.list()],
            "api_injected": self.api_service is not None,
            "ai_injected": self.ai_service is not None,
            "execution_enabled": False,
        }

    def diagnostics(self) -> dict[str, Any]:
        return {
            "status": "ok",
            "checks": {
                "app_registry": "ready" if self.registry.list() else "empty",
                "api_interface": "injected" if self.api_service is not None else "not_injected",
                "ai_interface": "injected" if self.ai_service is not None else "not_injected",
                "provider_catalog_owner": "backend.global_ecosystem.global_bada_business_ecosystem",
            },
        }
