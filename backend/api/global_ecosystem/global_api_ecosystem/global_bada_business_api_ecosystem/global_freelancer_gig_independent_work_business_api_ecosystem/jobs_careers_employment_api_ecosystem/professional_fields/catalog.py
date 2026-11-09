"""Canonical professional-field catalogue and lookup helpers."""
from __future__ import annotations
from importlib import import_module
from .models import ProfessionalField, ProfessionalSubcategory

FIELD_IDS = ["it_technology","banking_finance","healthcare_medical","education_training","engineering_construction","sales_marketing","legal_compliance","agriculture_food","manufacturing_operations","real_estate_facilities","hospitality_tourism","transport_logistics"]

def _module(field_id: str):
    if field_id not in FIELD_IDS:
        return None
    return import_module(f"{__package__}.{field_id}.categories")

def list_professional_fields() -> list[ProfessionalField]:
    result = []
    for field_id in FIELD_IDS:
        module = _module(field_id)
        subs = tuple(ProfessionalSubcategory(id=item["id"], name=item["name"], description=item["description"], parent_field_id=field_id) for item in module.SUBCATEGORY_DEFINITIONS)
        result.append(ProfessionalField(id=field_id, name=module.FIELD_NAME, description=module.FIELD_DESCRIPTION, subcategories=subs))
    return result

def get_professional_field(field_id: str) -> ProfessionalField | None:
    return next((item for item in list_professional_fields() if item.id == field_id), None)

def list_professional_subcategories(field_id: str) -> list[ProfessionalSubcategory]:
    field = get_professional_field(field_id)
    return list(field.subcategories) if field else []

def get_professional_subcategory(field_id: str, subcategory_id: str) -> ProfessionalSubcategory | None:
    return next((item for item in list_professional_subcategories(field_id) if item.id == subcategory_id), None)

def validate_professional_fields() -> dict:
    fields = list_professional_fields()
    field_ids = [item.id for item in fields]
    duplicates = sorted({value for value in field_ids if field_ids.count(value) > 1})
    invalid = {}
    for field in fields:
        sub_ids = [item.id for item in field.subcategories]
        dupes = sorted({value for value in sub_ids if sub_ids.count(value) > 1})
        if dupes or not field.name or not field.description:
            invalid[field.id] = {"duplicate_subcategory_ids": dupes, "missing_field_metadata": not bool(field.name and field.description)}
    return {"field_count": len(fields), "subcategory_count": sum(len(item.subcategories) for item in fields), "duplicate_field_ids": duplicates, "invalid_fields": invalid, "structurally_valid": not duplicates and not invalid, "taxonomy_status": "taxonomy_only"}
