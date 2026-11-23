"""Classification-only service API for finance work, services and business models."""
from .domain_catalog import get_domain, list_domains, search_domains, validate_mappings

SUPPORTED_TYPES = {"SERVICE", "WORK", "BUSINESS", "PROJECT", "PRODUCT", "ADVISORY", "EMPLOYMENT", "TRAINING"}

def status():
    validation = validate_mappings()
    return {
        "status": "CATALOG_READY" if validation["valid"] else "MAPPING_VALIDATION_FAILED",
        "business_domain_count": len(list_domains()),
        "mapping_integrity": validation["valid"],
        "mode": "CLASSIFICATION_ONLY",
        "execution_enabled": False,
    }

def classify(domain_id, service_type):
    item = get_domain(domain_id)
    if item is None:
        return {"valid": False, "reason": "UNKNOWN_BUSINESS_DOMAIN", "execution_enabled": False}
    kind = service_type.strip().upper()
    if kind not in SUPPORTED_TYPES:
        return {"valid": False, "reason": "UNSUPPORTED_SERVICE_TYPE", "execution_enabled": False}
    return {
        "valid": True,
        "business_domain": item,
        "service_type": kind,
        "capabilities": ["SERVICE", "WORK", "BUSINESS"],
        "execution_enabled": False,
        "regulatory_review_required": True,
    }

__all__ = ["status", "classify", "list_domains", "get_domain", "search_domains", "validate_mappings"]
