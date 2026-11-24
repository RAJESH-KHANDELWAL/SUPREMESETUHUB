"""Structural validation for this industry subcategory package."""
from .categories import validate_subcategory_definition


def validate_subcategory_package() -> dict:
    return validate_subcategory_definition()
