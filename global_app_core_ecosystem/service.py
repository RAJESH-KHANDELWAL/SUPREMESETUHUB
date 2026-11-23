"""CORE-owned application ecosystem catalog, validation and safe reporting."""
from __future__ import annotations

from collections import Counter
from typing import Any

from backend.global_ecosystem.global_app_ecosystem import (
    get_app_provider,
    get_scope_catalog,
    list_app_providers,
    list_app_types,
    validate_app_provider_registry,
)

from .policy import readiness_for_provider, safe_provider_snapshot


class GlobalAppCoreService:
    """Read-only control-plane facade; never calls or executes provider apps."""

    layer = "CORE"
    ecosystem = "GLOBAL_APP_ECOSYSTEM"

    def resolve_provider(self, provider_id: str) -> dict[str, Any]:
        if not isinstance(provider_id, str) or not provider_id.strip():
            raise ValueError("APP_PROVIDER_ID_REQUIRED")
        provider = get_app_provider(provider_id.strip().lower())
        if provider is None:
            raise KeyError(f"Unknown APP provider: {provider_id}")
        return provider

    def validate_app_type(self, app_type_id: str) -> dict[str, Any]:
        if not isinstance(app_type_id, str) or not app_type_id.strip():
            raise ValueError("APP_TYPE_ID_REQUIRED")
        for item in list_app_types():
            if item["id"] == app_type_id.strip().lower():
                return item
        raise KeyError(f"Unknown APP type: {app_type_id}")

    def provider_snapshot(self, provider_id: str) -> dict[str, Any]:
        provider = self.resolve_provider(provider_id)
        return {
            "provider": safe_provider_snapshot(provider),
            "readiness": readiness_for_provider(provider),
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }

    def catalog_snapshot(self) -> dict[str, Any]:
        providers = list_app_providers()
        domains = get_scope_catalog()["domains"]
        statuses = Counter(item.get("integration_status", "unknown") for item in providers)
        live_verified = sum(
            1 for item in providers
            if item.get("integration_status") == "live_verified"
            and item.get("live_connection_verified") is True
        )
        return {
            "layer": self.layer,
            "ecosystem": self.ecosystem,
            "provider_count": len(providers),
            "provider_categories": dict(sorted(Counter(
                item.get("category", "unknown") for item in providers
            ).items())),
            "provider_origins": dict(sorted(Counter(
                item.get("origin", "unknown") for item in providers
            ).items())),
            "integration_status_counts": dict(sorted(statuses.items())),
            "live_verified_provider_count": live_verified,
            "app_type_count": len(list_app_types()),
            "domain_count": len(domains),
            "domains": domains,
            "maturity_levels": get_scope_catalog()["maturity_levels"],
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }

    def health_snapshot(self) -> dict[str, Any]:
        errors = validate_app_provider_registry()
        snapshot = self.catalog_snapshot()
        return {
            "success": not errors,
            "ecosystem": self.ecosystem,
            "registry_valid": not errors,
            "registry_errors": list(errors),
            "provider_count": snapshot["provider_count"],
            "live_verified_provider_count": snapshot["live_verified_provider_count"],
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }


__all__ = ["GlobalAppCoreService"]
