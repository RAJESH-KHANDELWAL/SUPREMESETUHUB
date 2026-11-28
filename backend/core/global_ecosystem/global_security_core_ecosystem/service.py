"""Read-only service facade for GLOBAL SECURITY CORE metadata."""
from __future__ import annotations

from typing import Any
from .orchestrator import SecurityCoreOrchestrator


class SecurityCoreEcosystemService:
    NAME = "GLOBAL SECURITY CORE ECOSYSTEM"

    def __init__(self):
        self.orchestrator = SecurityCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        health = self.orchestrator.health()
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record = GlobalEcosystemManager().get("GLOBAL-SECURITY-CORE-ECOSYSTEM")
            registered = record is not None
            registration = {"success": registered, "registered": registered, "ecosystem": record}
        except Exception as exc:
            registration = {"success": False, "registered": False, "ecosystem": None, "error": type(exc).__name__}
        return {
            "success": True,
            "ecosystem_id": health["ecosystem_id"],
            "name": self.NAME,
            "status": health["status"],
            "domain_count": health["domain_count"],
            "provider_count": health["provider_count"],
            "jurisdiction_profile_count": health["jurisdiction_profile_count"],
            "live_service_connections_verified": False,
            "health": health,
            "manager_registration": registration,
        }

    def catalog(self): return self.orchestrator.catalog()
    def list_modules(self, enabled_only=False): return self.orchestrator.list_modules(enabled_only)
    def list_domains(self): return self.orchestrator.list_domains()
    def get_domain(self, domain_id): return self.orchestrator.get_domain(domain_id)
    def get_domain_manager(self, domain_id): return self.orchestrator.get_domain_manager(domain_id)
    def domain_coverage(self, domain_id): return self.orchestrator.domain_coverage(domain_id)
    def list_providers(self): return self.orchestrator.list_providers()
    def get_provider(self, provider_id): return self.orchestrator.get_provider(provider_id)
    def list_jurisdictions(self): return self.orchestrator.list_jurisdictions()
    def get_jurisdiction(self, jurisdiction_id): return self.orchestrator.get_jurisdiction(jurisdiction_id)
    def list_offerings(self): return self.orchestrator.list_offerings()
    def get_offering(self, domain_id): return self.orchestrator.get_offering(domain_id)
    def service_tiers(self): return self.orchestrator.service_tiers()
    def content_safety(self): return self.orchestrator.content_safety()
    def protected_group_safety(self, group_id=None): return self.orchestrator.protected_group_safety(group_id)
    def health(self): return self.orchestrator.health()
    def dependency_map(self): return self.orchestrator.dependency_map()
