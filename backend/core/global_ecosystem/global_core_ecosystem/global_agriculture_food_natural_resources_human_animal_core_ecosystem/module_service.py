"""Read-only domain metadata service."""
from __future__ import annotations
from .domain_catalog import get_domain, list_domains

class AgricultureDomainService:
    def list_domains(self):
        return {"success": True, **{"count": len(list_domains()), "domains": list_domains()}}

    def get_domain(self, domain_id: str):
        item = get_domain(domain_id)
        return {"success": item is not None, "domain": item, "error": None if item else "DOMAIN_NOT_FOUND"}
