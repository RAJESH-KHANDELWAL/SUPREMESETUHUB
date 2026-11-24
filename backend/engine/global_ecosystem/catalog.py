"""Backward-compatible ENGINE ecosystem catalog facade."""
from backend.engine.global_ecosystem.global_engine_ecosystem.catalog import (
    ROOT, ROOT_ID, CATEGORIES, PROVIDER_ECOSYSTEMS,
    get_catalog, get_category_catalog, get_provider_catalog,
)
__all__ = ["ROOT","ROOT_ID","CATEGORIES","PROVIDER_ECOSYSTEMS",
           "get_catalog","get_category_catalog","get_provider_catalog"]
