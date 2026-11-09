"""Public interface for the independent Global Company / Companies ecosystem."""
from .routes import router
from .service import (
    get_api_status,
    get_company,
    get_company_alphabet,
    list_country_sources,
    search_companies,
)
from .classification_registry import (
    get_record_class,
    list_record_classes,
    validate_record_class_registry,
)

__all__ = [
    "router",
    "get_api_status",
    "get_company",
    "get_company_alphabet",
    "list_country_sources",
    "search_companies",
    "get_record_class",
    "list_record_classes",
    "validate_record_class_registry",
]
