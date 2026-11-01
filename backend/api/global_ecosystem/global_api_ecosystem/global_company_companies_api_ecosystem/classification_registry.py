"""Central metadata registry for the three directory classes."""
from .company_legal_entities_api_ecosystem.catalog import CATEGORY as COMPANY
from .business_enterprises_api_ecosystem.catalog import CATEGORY as BUSINESS
from .freelancer_independent_professionals_api_ecosystem.catalog import CATEGORY as FREELANCER
RECORD_CLASSES = (COMPANY, BUSINESS, FREELANCER)
def list_record_classes():
    return [dict(x) for x in RECORD_CLASSES]
def get_record_class(record_type):
    key = (record_type or "").strip().casefold()
    return next((dict(x) for x in RECORD_CLASSES if x["record_type"] == key), None)
def validate_record_class_registry():
    ids = [x["record_type"] for x in RECORD_CLASSES]
    required = {"company", "business", "freelancer"}
    return {"structurally_valid": len(ids) == len(set(ids)) and set(ids) == required, "record_class_count": len(ids), "record_classes": ids, "missing_classes": sorted(required-set(ids)), "unexpected_classes": sorted(set(ids)-required), "registry_status": "classification_metadata_only"}
