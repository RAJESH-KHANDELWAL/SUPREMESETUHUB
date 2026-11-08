"""Structural validation for this independent work-type package."""
from .categories import validate_work_type_definition


def validate_work_type_package() -> dict:
    return validate_work_type_definition()
