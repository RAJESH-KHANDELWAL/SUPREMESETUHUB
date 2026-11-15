"""Structural validation for this category package."""
from .categories import validate_category_definition


def validate_category_package() -> dict:
    return validate_category_definition()
