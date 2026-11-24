"""Human Language CORE provider and domain discovery orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import (
    get_catalog, get_domain, get_domains, get_human_language_core_catalog,
    get_provider_catalog, get_service_tiers, list_human_language_core_modules,
)
from .constants import ECOSYSTEM_ID, STATUS
from .domain_catalog import human_language_domain_summary
from .provider_catalog import get_provider


class GlobalHumanLanguageCoreOrchestrator:
    """Coordinate catalog discovery and readiness metadata only."""

    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def registry(self) -> dict[str, Any]:
        return get_human_language_core_catalog()

    def list_modules(self, *, enabled_only: bool = False) -> dict[str, Any]:
        modules = list_human_language_core_modules(include_disabled=not enabled_only)
        return {"success": True, "count": len(modules), "modules": modules}

    def list_providers(self) -> list[dict[str, Any]]:
        return get_provider_catalog()

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        return get_provider(provider_id)

    def list_domains(self) -> list[dict[str, Any]]:
        return get_domains("HUMAN")

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def tiers(self) -> list[dict[str, Any]]:
        return get_service_tiers()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        summary = human_language_domain_summary()
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "status": STATUS,
            "provider_count": catalog["provider_count"],
            "domain_count": summary["domain_count"],
            "age_restricted_domain_count": summary["age_restricted_domain_count"],
            "enabled_provider_count": sum(bool(item.get("enabled", True)) for item in catalog["providers"]),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "execution_enabled": False,
            "warning": "Catalog registration does not prove provider credentials, API availability, entitlement or live connectivity.",
        }

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {
                    "provider_id": item["provider_id"],
                    "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/global_human_language_core_ecosystem/{item['folder']}",
                    "relationship": "PROVIDER_METADATA_MODULE",
                    "live_connection_verified": False,
                }
                for item in get_provider_catalog()
            ],
        }
