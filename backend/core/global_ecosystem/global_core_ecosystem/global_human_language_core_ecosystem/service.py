"""Human Language CORE read-only control-plane service."""
from __future__ import annotations

from typing import Any

from .catalog import (
    get_catalog, get_domain, get_domains, get_provider_catalog,
    get_service_tiers, list_human_language_core_modules,
)
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, STATUS
from .orchestrator import GlobalHumanLanguageCoreOrchestrator
from .policy import adult_content_policy, redact_sensitive_metadata


class GlobalHumanLanguageCoreService:
    NAME = ECOSYSTEM_NAME

    def __init__(self) -> None:
        self.orchestrator = GlobalHumanLanguageCoreOrchestrator()

    def describe(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "name": self.NAME,
            "status": STATUS,
            "layer": "CORE",
            "execution_enabled": False,
            "live_provider_connections_verified": False,
        }

    def status(self) -> dict[str, Any]:
        catalog = get_catalog()
        health = self.orchestrator.health()
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "name": self.NAME,
            "status": STATUS,
            "module_count": catalog["provider_count"],
            "provider_count": catalog["provider_count"],
            "domain_count": catalog["domain_count"],
            "connected_modules": 0,
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": health,
        }

    def health(self) -> dict[str, Any]:
        health = self.orchestrator.health()
        return {
            **health,
            "division_count": get_catalog()["division_count"],
        }

    def catalog(self) -> dict[str, Any]:
        return redact_sensitive_metadata(get_catalog())

    def list_modules(self) -> dict[str, Any]:
        return self.orchestrator.list_modules()

    def list_providers(self) -> list[dict[str, Any]]:
        return get_provider_catalog()

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_provider(provider_id)

    def list_domains(self) -> list[dict[str, Any]]:
        return get_domains("HUMAN")

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def list_service_tiers(self) -> list[dict[str, Any]]:
        return get_service_tiers()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()

    def adult_policy(self) -> dict[str, Any]:
        return adult_content_policy()
