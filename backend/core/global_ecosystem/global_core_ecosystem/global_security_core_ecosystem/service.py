"""Global Security CORE read-only control-plane service."""
from __future__ import annotations

from typing import Any

from .catalog import get_catalog, get_security_core_catalog
from .orchestrator import SecurityCoreOrchestrator


class SecurityCoreEcosystemService:
    """Public facade for Security Core registry and metadata operations."""

    NAME = "GLOBAL SECURITY CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-SECURITY-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = SecurityCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_catalog()
        health = self.orchestrator.health()
        manager = self.manager_status()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "status": catalog["status"],
            "registry_status": manager["registered"],
            "domain_count": health["domain_count"],
            "provider_count": health["provider_count"],
            "jurisdiction_profile_count": health["jurisdiction_profile_count"],
            "live_service_connections_verified": False,
            "security_enforcement_verified": False,
            "legal_compliance_verified": False,
            "health": health,
            "manager_registration": manager,
        }

    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def registry(self) -> dict[str, Any]:
        return get_security_core_catalog()

    def list_modules(self, enabled_only: bool = False) -> dict[str, Any]:
        return self.orchestrator.list_modules(enabled_only)

    def list_domains(self) -> list[dict[str, Any]]:
        return self.orchestrator.list_domains()

    def list_providers(self) -> list[dict[str, Any]]:
        return self.orchestrator.list_providers()

    def list_jurisdictions(self) -> list[dict[str, Any]]:
        return self.orchestrator.list_jurisdictions()

    def get_jurisdiction(self, jurisdiction_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_jurisdiction(jurisdiction_id)

    def content_safety(self) -> dict[str, Any]:
        return self.orchestrator.content_safety()

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()

    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import (
                GlobalEcosystemManager,
            )

            record = GlobalEcosystemManager().get(self.ECOSYSTEM_ID)
        except Exception as exc:
            return {
                "success": False,
                "registered": False,
                "ecosystem": None,
                "error": type(exc).__name__,
            }

        return {
            "success": record is not None,
            "registered": record is not None,
            "ecosystem": record,
            "live_service_connections_verified": False,
        }
