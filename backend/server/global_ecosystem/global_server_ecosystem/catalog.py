"""SERVER-owned metadata for layer boundaries and server providers."""
from dataclasses import dataclass
@dataclass(frozen=True)
class LayerDescriptor:
    name: str
    responsibility: str
    owner_path: str
@dataclass(frozen=True)
class ProviderDescriptor:
    provider_id: str
    display_name: str
    package: str
    status: str = "NOT_CONFIGURED"
_LAYERS = (
    LayerDescriptor("API", "HTTP routes, schemas and transport", "backend/api/global_ecosystem/global_api_ecosystem/"),
    LayerDescriptor("CORE", "Domain contracts, models, rules and policies", "backend/core/global_ecosystem/global_core_ecosystem/"),
    LayerDescriptor("ENGINE", "Execution and provider adapters", "backend/engine/global_ecosystem/global_engine_ecosystem/"),
    LayerDescriptor("DATABASE", "Durable structured records and database access", "backend/database/global_ecosystem/global_database_ecosystem/"),
    LayerDescriptor("STORAGE", "Files, objects and artifact persistence", "backend/storage/global_ecosystem/global_storage_ecosystem/"),
)
_PROVIDERS = (
    ProviderDescriptor("aws", "AWS Compute", "aws_server"),
    ProviderDescriptor("azure", "Azure Compute", "azure_server"),
    ProviderDescriptor("digitalocean", "DigitalOcean", "digitalocean_server"),
    ProviderDescriptor("google", "Google Cloud Compute", "google_server"),
    ProviderDescriptor("hostinger", "Hostinger Servers", "hostinger_server"),
)
def get_layer_catalog():
    return tuple(_LAYERS)
def get_provider_catalog():
    return tuple(_PROVIDERS)
__all__ = ["LayerDescriptor", "ProviderDescriptor", "get_layer_catalog", "get_provider_catalog"]