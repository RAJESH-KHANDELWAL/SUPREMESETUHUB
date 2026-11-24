"""Read-only domain module service."""
from .domain_catalog import get_domain_catalog
class DomainModuleService:
    def __init__(self, domain_id:str): self.domain_id=domain_id
    def status(self):
        domain=get_domain_catalog().get(self.domain_id)
        return {"success":domain is not None,"domain_id":self.domain_id,"status":"CATALOG_ONLY" if domain else "UNKNOWN_DOMAIN","domain":domain}
