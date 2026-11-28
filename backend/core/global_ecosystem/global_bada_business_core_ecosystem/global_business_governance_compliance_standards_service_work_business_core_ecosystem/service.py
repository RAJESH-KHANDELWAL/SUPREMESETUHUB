"""Provider-neutral service/work record validation and classification."""
from .catalog import ECOSYSTEM_ID
from .contracts import BusinessContext, ServiceWorkBusinessRecord
from .domain_catalog import get_domain
from .policy import validate_record_policy
class BusinessServiceWorkCoreService:
    def status(self) -> dict:
        return {"success": True, "ecosystem_id": ECOSYSTEM_ID, "status": "CORE_CATALOG_READY", "live_connection_verified": False, "persistence_enabled": False, "external_actions_enabled": False}
    def validate_context(self, context: BusinessContext) -> dict:
        context.validate()
        return {"success": True, "tenant_id_present": True, "actor_id_present": True, "jurisdiction": context.jurisdiction.strip().upper()}
    def validate_record(self, record: ServiceWorkBusinessRecord) -> dict:
        domain = get_domain(record.domain_id)
        if domain is None: return {"success": False, "status": "REJECTED", "errors": ["UNKNOWN_DOMAIN_ID"]}
        errors = validate_record_policy(record)
        return {"success": not errors, "ecosystem_id": ECOSYSTEM_ID, "record_id": record.record_id, "domain": domain, "status": "VALIDATION_PASSED" if not errors else "REVIEW_REQUIRED", "errors": errors, "validated_only": True, "record_persisted": False, "work_executed": False}
    def classify_service(self, domain_id: str, service_type: str) -> dict:
        domain = get_domain(domain_id)
        if domain is None or not isinstance(service_type, str) or not service_type.strip(): return {"success": False, "errors": ["VALID_DOMAIN_AND_SERVICE_TYPE_REQUIRED"]}
        return {"success": True, "domain_id": domain["domain_id"], "service_type": service_type.strip(), "classification_status": "PROVISIONAL_METADATA", "legal_or_regulatory_approval": False}
