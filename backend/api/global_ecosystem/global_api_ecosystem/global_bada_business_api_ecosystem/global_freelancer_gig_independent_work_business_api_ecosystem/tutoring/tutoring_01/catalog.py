"""Lookup and serialization for this work-type package."""
from .categories import SPECIALIZATION_ID, WORK_TYPE_ID, get_work_type_definition
from .models import WorkTypeRecord


def get_work_type() -> WorkTypeRecord:
    item = get_work_type_definition()
    return WorkTypeRecord(
        id=item["id"],
        name=item["name"],
        description=item["description"],
        specialization_id=SPECIALIZATION_ID,
    )


def serialize_work_type() -> dict:
    item = get_work_type()
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "specialization_id": item.specialization_id,
        "taxonomy_status": item.taxonomy_status,
    }
