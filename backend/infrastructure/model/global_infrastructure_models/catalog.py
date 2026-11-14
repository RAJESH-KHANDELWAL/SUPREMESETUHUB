"""Catalog of normalized global infrastructure model families."""
from .relationships import RELATIONSHIP_TYPES
from .resources import RESOURCE_CATEGORIES
MODEL_CATALOG = {
    "resource_identity": {"description": "Stable platform identity and optional provider identity.", "required_fields": ("resource_id", "resource_type")},
    "resource_category": {"description": "Provider-neutral category and resource type vocabulary.", "categories": tuple(RESOURCE_CATEGORIES)},
    "resource_relationship": {"description": "Typed relationship between two platform resources.", "relationship_types": RELATIONSHIP_TYPES},
    "provider_reference": {"description": "Provider identifier and external resource identifier; no credentials.", "fields": ("provider_id", "external_id")},
    "lifecycle": {"description": "Normalized lifecycle metadata.", "states": ("PLANNED", "PROVISIONING", "ACTIVE", "DEGRADED", "SUSPENDED", "FAILED", "RETIRED")},
    "location": {"description": "Region, zone, data-center and geographic metadata.", "fields": ("region", "zone", "datacenter", "location")},
    "capacity": {"description": "CPU, memory, storage and bandwidth metadata.", "fields": ("cpu", "memory", "storage", "bandwidth")},
}
def get_model_catalog() -> dict:
    return {key: dict(value) for key, value in MODEL_CATALOG.items()}
