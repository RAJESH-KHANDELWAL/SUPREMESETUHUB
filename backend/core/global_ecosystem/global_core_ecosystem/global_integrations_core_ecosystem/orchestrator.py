"""Read-only discovery, health and dependency orchestration."""
from .catalog import get_catalog,get_integration,get_integrations_catalog,get_provider,get_provider_catalog,search_catalog
from .constants import ECOSYSTEM_ID,STATUS
from .policy import assert_catalog_only_operation,redact_sensitive_metadata
class GlobalIntegrationsCoreOrchestrator:
    def catalog(self):
        assert_catalog_only_operation("DISCOVER")
        return redact_sensitive_metadata(get_catalog())
    def list_integrations(self):
        items=get_integrations_catalog()
        return {"success":True,"count":len(items),"integration_domains":items}
    def get_integration(self,domain_id): return get_integration(domain_id)
    def list_providers(self):
        items=get_provider_catalog()
        return {"success":True,"count":len(items),"provider_families":items}
    def get_provider(self,provider_id): return get_provider(provider_id)
    def search(self,query):
        items=search_catalog(query)
        return {"success":True,"query":query.strip(),"count":len(items),"results":items}
    def health(self):
        domains,providers=get_integrations_catalog(),get_provider_catalog()
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"status":STATUS,
          "integration_domain_count":len(domains),"provider_family_count":len(providers),
          "restricted_domain_count":sum(x["sensitivity"]=="RESTRICTED" for x in domains),
          "age_restricted_domain_count":sum(x["age_restricted"] for x in domains),
          "live_connections_verified":0,"api_calls_performed":0,"execution_enabled":False,
          "warning":"Metadata health does not verify provider accounts, entitlements, adapters or connectivity."}
    def dependency_map(self):
        return {"success":True,"core_owns":["provider_identity_metadata","domain_taxonomy","capability_contracts","policy_metadata","readiness_metadata","read_only_discovery"],
          "delegates_to":{"API":["authentication","request_validation","HTTP_transport","response_normalization"],
          "ADAPTERS":["provider_SDKs","webhooks","provider_translation"],
          "SECURITY_CONFIGURATION":["secret_storage","secret_resolution","authorization","rotation"],
          "DATABASE_STORAGE":["persistence","tenant_isolation","retention","backups"],
          "ENGINE":["execution","scheduling","retries","lifecycle"]},"execution_enabled":False}
    def get_domain_manager(self,domain_id):
        from .domain_runtime import IntegrationDomainManager
        return IntegrationDomainManager(domain_id)
