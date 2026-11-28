"""Unified read-only catalog for infrastructure domains and providers."""
from __future__ import annotations

from .capabilities import CAPABILITIES
from .integrations import INTEGRATIONS
from .models import MODEL_FAMILIES
from .providers import PROVIDERS
from .schemas import CatalogRecord
from .services import SERVICES
from .structure import INFRASTRUCTURE_MODULES

CATALOG: dict[str, tuple[CatalogRecord, ...]] = {
    "providers": PROVIDERS,
    "capabilities": CAPABILITIES,
    "model_families": MODEL_FAMILIES,
    "services": SERVICES,
    "integrations": INTEGRATIONS,
}

def get_catalog() -> dict[str, list[dict]]:
    return {
        category: [record.to_dict() for record in records]
        for category, records in CATALOG.items()
    }

def catalog_counts() -> dict[str, int]:
    return {category: len(records) for category, records in CATALOG.items()}

def get_infrastructure_modules() -> tuple[str, ...]:
    return INFRASTRUCTURE_MODULES
