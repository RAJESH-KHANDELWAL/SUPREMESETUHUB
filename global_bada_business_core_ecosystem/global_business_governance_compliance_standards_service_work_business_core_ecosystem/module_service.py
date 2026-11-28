"""Read-only domain and capability discovery."""
from typing import Any
from .domain_catalog import get_domain, list_capabilities, list_domains
class BusinessGovernanceModuleService:
    def list_domains(self) -> list[dict[str, Any]]: return list_domains()
    def get_domain(self, domain_id: str) -> dict[str, Any] | None: return get_domain(domain_id)
    def list_capabilities(self) -> list[str]: return list_capabilities()
    def status(self) -> dict[str, Any]:
        return {"success": True, "domain_count": len(list_domains()), "capability_count": len(list_capabilities()), "live_connections_verified": False}
