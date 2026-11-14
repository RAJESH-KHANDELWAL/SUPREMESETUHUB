"""Shared infrastructure model contracts."""
from .global_infrastructure_models import (
    MODEL_FAMILY,
    STATUS,
    MODEL_CATALOG,
    get_model_catalog,
    validate_resource_record,
)

__all__ = [
    "MODEL_FAMILY",
    "STATUS",
    "MODEL_CATALOG",
    "get_model_catalog",
    "validate_resource_record",
]
