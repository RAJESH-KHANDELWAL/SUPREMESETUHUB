"""Lookup and serialization for this industry subcategory."""
from .categories import get_subcategory_definition
from .models import IndustrySubcategoryRecord


def get_subcategory() -> IndustrySubcategoryRecord:
    item = get_subcategory_definition()
    return IndustrySubcategoryRecord(item["id"], item["name"], item["category_id"])


def serialize_subcategory() -> dict:
    item = get_subcategory()
    return {"id": item.id, "name": item.name, "category_id": item.category_id, "taxonomy_status": item.taxonomy_status}
