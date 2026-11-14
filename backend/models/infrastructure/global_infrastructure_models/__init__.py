"""Provider-neutral Global Infrastructure Models."""
from .catalog import MODEL_CATALOG, get_model_catalog
from .validation import validate_resource_record

MODEL_FAMILY = "GLOBAL_INFRASTRUCTURE_MODELS"
STATUS = "CONTRACT_FOUNDATION"

__all__ = [
    "MODEL_FAMILY",
    "STATUS",
    "MODEL_CATALOG",
    "get_model_catalog",
    "validate_resource_record",
]
