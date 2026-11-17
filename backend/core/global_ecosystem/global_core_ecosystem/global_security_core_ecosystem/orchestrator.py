"""Security CORE discovery and readiness orchestration; no network operations."""
from __future__ import annotations
from .catalog import get_catalog, get_security_core_catalog, list_security_core_modules
from .constants import ECOSYSTEM_ID, STATUS
from .domain_catalog import get_domains, domain_summary, get_domain
from .jurisdiction_catalog import get_jurisdictions, get_jurisdiction, jurisdiction_summary
from .provider_catalog import get_provider, get_provider_catalog, provider_summary
from .content_safety_policy import content_safety_baseline

class SecurityCoreOrchestrator:
    def catalog(self): return get_catalog()
    def registry(self): return get_security_core_catalog()
    def list_modules(self, enabled_only=False):
        items = list_security_core_modules(include_disabled=not enabled_only)
        return {"success": True, "count": len(items), "modules": items}
    def list_providers(self): return get_provider_catalog()
    def get_provider(self, provider_id): return get_provider(provider_id)
    def list_domains(self): return get_domains()
    def get_domain(self, domain_id): return get_domain(domain_id)
    def list_jurisdictions(self): return get_jurisdictions()
    def get_jurisdiction(self, jurisdiction_id): return get_jurisdiction(jurisdiction_id)
    def content_safety(self): return content_safety_baseline()
    def health(self):
        return {
            "success": True, "ecosystem_id": ECOSYSTEM_ID, "status": STATUS,
            **domain_summary(), **provider_summary(), **jurisdiction_summary(),
            "live_connections_verified": 0, "api_calls_performed": 0,
            "security_enforcement_verified": False,
            "warning": "Catalog registration does not prove provider credentials, API availability, protection coverage, live connectivity or legal compliance.",
        }
    def dependency_map(self):
        return {"success": True, "edges": [{
            "provider_id": x["provider_id"],
            "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem/{x['folder']}",
            "relationship": "PROVIDER_SECURITY_METADATA", "live_connection_verified": False,
        } for x in get_provider_catalog()]}
