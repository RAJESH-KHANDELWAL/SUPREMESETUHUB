"""CORE-owned application ecosystem selection and validation."""
from __future__ import annotations
from typing import Any
from backend.global_ecosystem.global_app_ecosystem import (
    get_app_provider, list_app_providers, list_app_types, get_scope_catalog,
)

class GlobalAppCoreService:
    """Read-only adapter over the canonical Global APP catalog."""
    NAME = "GLOBAL APP CORE ECOSYSTEM"

    def resolve_provider(self, provider_id: str) -> dict[str, Any]:
        provider = get_app_provider(provider_id)
        if provider is None:
            raise KeyError(f"Unknown APP provider: {provider_id}")
        return provider

    def validate_app_type(self, app_type_id: str) -> dict[str, Any]:
        for item in list_app_types():
            if item["id"] == app_type_id:
                return item
        raise KeyError(f"Unknown APP type: {app_type_id}")

    def catalog_snapshot(self) -> dict[str, Any]:
        return {
            "layer": "CORE", "ecosystem": "GLOBAL-APP-CORE-ECOSYSTEM",
            "provider_count": len(list_app_providers()),
            "domains": get_scope_catalog()["domains"],
            "execution": "NOT_PERFORMED", "persistence": "NOT_PERFORMED",
            "live_connection_verified": False,
        }

__all__ = ["GlobalAppCoreService"]
