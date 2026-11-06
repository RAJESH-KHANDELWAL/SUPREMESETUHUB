"""Lookup and serialization for this industry category."""
from .categories import get_category_definition
from .models import IndustryCategoryRecord


def get_category() -> IndustryCategoryRecord:
    item = get_category_definition()
    return IndustryCategoryRecord(item["id"], item["name"], tuple(item["subcategories"]))


def serialize_category() -> dict:
    item = get_category()
    return {"id": item.id, "name": item.name, "subcategories": list(item.subcategories), "taxonomy_status": item.taxonomy_status}
