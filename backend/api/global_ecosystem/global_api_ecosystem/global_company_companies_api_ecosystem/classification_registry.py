"""Canonical record-class registry: Company, Enterprise and Corporate Group only."""
RECORD_CLASSES = (
 {"record_type":"company","name":"Company","module":"company_legal_entities_api_ecosystem"},
 {"record_type":"enterprise","name":"Enterprise","module":"business_enterprises_api_ecosystem"},
 {"record_type":"corporate_group","name":"Corporate Group","module":"corporate_groups_api_ecosystem"},
)
def list_record_classes(): return [dict(x) for x in RECORD_CLASSES]
def get_record_class(record_type):
 key=(record_type or "").strip().casefold()
 return next((dict(x) for x in RECORD_CLASSES if x["record_type"]==key),None)
def validate_record_class_registry():
 ids=[x["record_type"] for x in RECORD_CLASSES]
 required={"company","enterprise","corporate_group"}
 duplicates=sorted({x for x in ids if ids.count(x)>1})
 return {"structurally_valid":not duplicates and set(ids)==required,"record_class_count":len(ids),"record_classes":ids,"duplicate_classes":duplicates,"missing_classes":sorted(required-set(ids)),"freelancer_is_company_record_class":False,"registry_status":"classification_metadata_only"}
