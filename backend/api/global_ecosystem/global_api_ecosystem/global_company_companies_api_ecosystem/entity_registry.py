"""Shared entity subtype to top-level record class lookup."""
from .classification_registry import get_record_class, list_record_classes, validate_record_class_registry
def classify_entity_type(entity_type):
    needle = (entity_type or "").strip().casefold()
    for item in list_record_classes():
        if needle in {value.casefold() for value in item["entity_types"]}:
            return item["record_type"]
    return None
__all__ = ["get_record_class", "list_record_classes", "validate_record_class_registry", "classify_entity_type"]
