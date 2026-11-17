"""Read-only facade for the global language taxonomy."""
from .catalog import get_catalog,get_domain,get_domains,get_provider_catalog,get_service_tiers
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME,STATUS
from .policy import adult_content_policy,redact_sensitive_metadata

class GlobalLanguageCoreService:
    def describe(self):
        return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"status":STATUS,"layer":"CORE","execution_enabled":False}
    def health(self):
        catalog=get_catalog()
        return {"success":True,"status":STATUS,"division_count":len(catalog["divisions"]),"domain_count":catalog["domain_count"],"live_provider_connections_verified":False}
    def catalog(self):
        return redact_sensitive_metadata(get_catalog())
    def list_domains(self,division=None):
        return get_domains(division)
    def get_domain(self,domain_id):
        return get_domain(domain_id)
    def list_providers(self):
        return get_provider_catalog()
    def list_service_tiers(self):
        return get_service_tiers()
    def adult_policy(self):
        return adult_content_policy()
