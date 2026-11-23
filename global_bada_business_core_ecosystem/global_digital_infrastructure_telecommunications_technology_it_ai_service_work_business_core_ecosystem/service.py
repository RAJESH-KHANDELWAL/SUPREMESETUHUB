"""Provider-neutral service classification and engagement validation."""
from .catalog import ECOSYSTEM_ID
from .domain_catalog import get_domain, list_domains
from .policy import validate_engagement
from .provider_registry import get_provider, list_providers
class DigitalTechnologyServiceWorkBusinessService:
    def status(self) -> dict:
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"status":"CORE_CATALOG_READY","live_connections_verified":False,"external_actions_enabled":False,"persistence_enabled":False}
    def classify_service(self, domain_id: str, service_type: str) -> dict:
        domain = get_domain(domain_id)
        if domain is None or not isinstance(service_type,str) or not service_type.strip(): return {"success":False,"errors":["VALID_DOMAIN_AND_SERVICE_TYPE_REQUIRED"]}
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"domain":domain,"service_type":service_type.strip(),"classification_status":"METADATA_CLASSIFIED"}
    def validate_engagement(self, record) -> dict:
        errors = validate_engagement(record)
        return {"success":not errors,"record_id":record.record_id,"status":"VALIDATION_PASSED" if not errors else "REVIEW_REQUIRED","errors":errors,"validated_only":True,"record_persisted":False,"work_executed":False}
    def inventory(self) -> dict:
        return {"domains":list_domains(),"providers":list_providers(),"domain_count":len(list_domains()),"provider_count":len(list_providers())}
    def provider(self, provider_id: str) -> dict | None: return get_provider(provider_id)
