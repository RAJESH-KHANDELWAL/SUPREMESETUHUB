"""Company entity-type to record-class mappings."""
from .classification_registry import get_record_class, list_record_classes, validate_record_class_registry
ENTITY_TYPE_TO_RECORD_CLASS = {
 "registered_company":"company","public_company":"company","private_company":"company","limited_company":"company","corporation":"company","private_limited_company":"company","public_limited_company":"company","limited_liability_company":"company",
 "operating_enterprise":"enterprise","micro_enterprise":"enterprise","small_enterprise":"enterprise","medium_enterprise":"enterprise","large_enterprise":"enterprise","startup_enterprise":"enterprise","sole_proprietor":"enterprise","micro_business":"enterprise","small_business":"enterprise","medium_business":"enterprise","large_business":"enterprise","startup":"enterprise","scaleup":"enterprise","franchise":"enterprise",
 "holding_group":"corporate_group","corporate_group":"corporate_group","parent_company_group":"corporate_group","subsidiary_group":"corporate_group",
}
def classify_entity_type(entity_type): return ENTITY_TYPE_TO_RECORD_CLASS.get((entity_type or "").strip().casefold())
def list_entity_type_mappings(): return [{"entity_type":k,"record_type":v} for k,v in sorted(ENTITY_TYPE_TO_RECORD_CLASS.items())]
__all__=["get_record_class","list_record_classes","validate_record_class_registry","classify_entity_type","list_entity_type_mappings"]
