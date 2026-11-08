"""SERVER-owned map of layer boundaries; no layer implementation is duplicated."""
from .models import LayerDescriptor

LAYER_CATALOG = (
    LayerDescriptor("API", "HTTP routes, schemas and transport", "backend/api/global_ecosystem/global_api_ecosystem/"),
    LayerDescriptor("CORE", "Domain contracts, models, rules and policies", "backend/core/global_ecosystem/global_core_ecosystem/"),
    LayerDescriptor("ENGINE", "Execution and provider adapters", "backend/engine/global_ecosystem/global_engine_ecosystem/"),
    LayerDescriptor("DATABASE", "Durable structured records and database access", "backend/database/global_ecosystem/global_database_ecosystem/"),
    LayerDescriptor("STORAGE", "Files, objects and artifact persistence", "backend/storage/global_ecosystem/global_storage_ecosystem/"),
)

def get_layer_catalog() -> tuple[LayerDescriptor, ...]:
    return LAYER_CATALOG

__all__ = ["LAYER_CATALOG", "get_layer_catalog"]
