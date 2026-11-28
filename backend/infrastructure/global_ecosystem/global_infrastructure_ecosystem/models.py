"""Catalog model exports for infrastructure ecosystem metadata."""
from .schemas import CatalogRecord

MODEL_FAMILIES = (
    CatalogRecord("resource", "Infrastructure Resource", "model_family", "Provider-neutral resource identity and metadata."),
    CatalogRecord("provider", "Infrastructure Provider", "model_family", "Provider identity and connection state."),
    CatalogRecord("capability", "Infrastructure Capability", "model_family", "Provider-neutral capability definition."),
    CatalogRecord("relationship", "Resource Relationship", "model_family", "Dependency and topology relationship."),
    CatalogRecord("integration", "Infrastructure Integration", "model_family", "Adapter declaration and verification state."),
)
