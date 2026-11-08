"""SERVER-owned layer, provider and server-service catalogs."""
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
_SERVICE_TYPES = (
    {"service_type_id": "vpn-server", "name": "VPN SERVER", "category": "Network Server",
     "status": "catalog_only", "capabilities": ["vpn", "secure-networking"]},
    {"service_type_id": "vps-server", "name": "VPS SERVER", "category": "Virtual Private Server",
     "status": "catalog_only", "capabilities": ["virtual-machine", "server-management"]},
    {"service_type_id": "cloud-server", "name": "CLOUD SERVER", "category": "Cloud Compute",
     "status": "catalog_only", "capabilities": ["cloud-compute", "scaling"]},
    {"service_type_id": "web-server", "name": "WEB SERVER", "category": "Web Infrastructure",
     "status": "catalog_only", "capabilities": ["web-hosting", "http-serving"]},
    {"service_type_id": "cloud-web-server", "name": "CLOUD WEB SERVER", "category": "Cloud Web Infrastructure",
     "status": "catalog_only", "capabilities": ["cloud-hosting", "web-serving", "scaling"]},
)
def get_layer_catalog():
    return tuple(_LAYERS)
def get_provider_catalog():
    return tuple(_PROVIDERS)
def list_providers():
    return [{"provider_id": p.provider_id, "name": p.display_name,
             "display_name": p.display_name, "package": p.package,
             "status": "catalog_only", "capabilities": ["cloud-server-management"]}
            for p in _PROVIDERS]
def get_provider(provider_id: str):
    key = str(provider_id).strip().lower()
    for item in list_providers():
        if item["provider_id"] == key:
            return item
    raise KeyError(f"Unknown server provider: {provider_id}")
def list_service_types():
    return [{**item, "capabilities": list(item["capabilities"])} for item in _SERVICE_TYPES]
def get_service_type(service_type_id: str):
    key = str(service_type_id).strip().lower().replace("_", "-").replace(" ", "-")
    compact = key.replace("-", "")
    for item in _SERVICE_TYPES:
        candidate = item["service_type_id"]
        if key == candidate or compact == candidate.replace("-", ""):
            return {**item, "capabilities": list(item["capabilities"])}
    raise KeyError(f"Unknown server service type: {service_type_id}")
__all__ = ["LayerDescriptor", "ProviderDescriptor", "get_layer_catalog", "get_provider_catalog",
           "list_providers", "get_provider", "list_service_types", "get_service_type"]