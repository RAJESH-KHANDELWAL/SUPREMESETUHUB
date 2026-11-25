"""Read-only service/work/business discovery facade."""
from .catalog import get_catalog
from .domain_catalog import list_business_domains, get_business_domain
from .policy import capability_policy

class AgricultureBusinessService:
    def status(self):
        catalog = get_catalog()
        return {"success": True, "ecosystem": catalog, "domain_count": len(catalog["domains"]), "live_providers_verified": False}

    def list_domains(self):
        return {"success": True, "count": len(list_business_domains()), "domains": list_business_domains()}

    def get_domain(self, domain_id: str):
        item = get_business_domain(domain_id)
        return {"success": item is not None, "domain": item, "policy": capability_policy(item) if item else None, "error": None if item else "DOMAIN_NOT_FOUND"}
