"""Discovery and health orchestration for GLOBAL SECURITY CORE; no network calls."""
from __future__ import annotations

from .manager import (
    ECOSYSTEM_ID, NAME, STATUS, get_catalog, get_security_core_catalog,
    get_domains, get_domain, get_service_tiers, get_protected_group_safety,
    list_security_core_modules, domain_summary, get_manager,
)
from .jurisdiction_catalog import get_jurisdictions, get_jurisdiction, jurisdiction_summary
from .provider_catalog import get_provider, get_provider_catalog, provider_summary
from .content_safety_policy import content_safety_baseline


class SecurityCoreOrchestrator:
    """Google-Core-style discovery, inventory, offering and dependency APIs."""

    def catalog(self):
        return get_catalog()

    def registry(self):
        return get_security_core_catalog()

    def list_modules(self, enabled_only: bool = False):
        modules = list_security_core_modules(include_disabled=not enabled_only)
        return {"success": True, "count": len(modules), "modules": modules}

    def list_domains(self):
        return {"success": True, **domain_summary(), "domains": get_domains()}

    def domain_inventory(self):
        return get_domains()

    def get_domain(self, domain_id):
        return get_domain(domain_id)

    def list_providers(self):
        return {"success": True, **provider_summary(), "providers": get_provider_catalog()}

    def get_provider(self, provider_id):
        return get_provider(provider_id)

    def list_jurisdictions(self):
        return {"success": True, **jurisdiction_summary(), "jurisdictions": get_jurisdictions()}

    def get_jurisdiction(self, jurisdiction_id):
        return get_jurisdiction(jurisdiction_id)

    def list_offerings(self):
        return {"success": True, "count": len(get_domains()), "offerings": get_domains()}

    def get_offering(self, domain_id):
        return get_domain(domain_id)

    def service_tiers(self):
        return get_service_tiers()

    def content_safety(self):
        return content_safety_baseline()

    def protected_group_safety(self, group_id=None):
        return get_protected_group_safety(group_id)

    def health(self):
        manager_status = get_manager().status()
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "name": NAME,
            "status": STATUS,
            **manager_status,
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "security_enforcement_verified": False,
            "warning": "Metadata readiness does not prove live connectivity, deployed security controls, protection coverage, or legal compliance.",
        }

    def dependency_map(self):
        return get_manager().dependency_map()
