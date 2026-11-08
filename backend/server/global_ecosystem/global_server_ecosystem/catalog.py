"""SERVER-owned layer, provider and server-service catalogs.

The seven canonical provider IDs are aligned with GLOBAL SERVER CORE and ENGINE.
Azure and Hostinger remain available as additional SERVER-specific integrations.
"""
from dataclasses import dataclass
from typing import Any

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
    alignment: str = "CANONICAL"
    status: str = "NOT_CONFIGURED"
    capabilities: tuple[str, ...] = ("cloud-server-management",)

_LAYERS = (
    LayerDescriptor("API", "HTTP routes, schemas and transport", "backend/api/global_ecosystem/global_api_ecosystem/"),
    LayerDescriptor("CORE", "Domain contracts, models, rules and policies", "backend/core/global_ecosystem/global_core_ecosystem/"),
    LayerDescriptor("ENGINE", "Execution and provider adapters", "backend/engine/global_ecosystem/global_engine_ecosystem/"),
    LayerDescriptor("DATABASE", "Durable structured records and database access", "backend/database/global_ecosystem/global_database_ecosystem/"),
    LayerDescriptor("STORAGE", "Files, objects and artifact persistence", "backend/storage/global_ecosystem/global_storage_ecosystem/"),
)
_PROVIDERS = (
    ProviderDescriptor("abelohost", "Abelohost", "abelohost_server"),
    ProviderDescriptor("aws", "Amazon Web Services", "aws_server"),
    ProviderDescriptor("cloudflare", "Cloudflare", "cloudflare_server"),
    ProviderDescriptor("digitalocean", "DigitalOcean", "digitalocean_server"),
    ProviderDescriptor("google", "Google Cloud", "google_server"),
    ProviderDescriptor("microsoft", "Microsoft Azure", "microsoft_server"),
    ProviderDescriptor("vicetemple", "ViceTemple", "vicetemple_server"),
    ProviderDescriptor("azure", "Microsoft Azure (legacy alias)", "azure_server", "ADDITIONAL"),
    ProviderDescriptor("hostinger", "Hostinger", "hostinger_server", "ADDITIONAL"),
)
_SERVICE_TYPES = (
    {"service_type_id":"vpn-server","name":"VPN SERVER","category":"Network Server","status":"catalog_only","capabilities":["vpn","secure-networking"]},
    {"service_type_id":"vps-server","name":"VPS SERVER","category":"Virtual Private Server","status":"catalog_only","capabilities":["virtual-machine","server-management"]},
    {"service_type_id":"cloud-server","name":"CLOUD SERVER","category":"Cloud Compute","status":"catalog_only","capabilities":["cloud-compute","scaling"]},
    {"service_type_id":"web-server","name":"WEB SERVER","category":"Web Infrastructure","status":"catalog_only","capabilities":["web-hosting","http-serving"]},
    {"service_type_id":"cloud-web-server","name":"CLOUD WEB SERVER","category":"Cloud Web Infrastructure","status":"catalog_only","capabilities":["cloud-hosting","web-serving","scaling"]},
    {"service_type_id":"dedicated-server","name":"DEDICATED SERVER","category":"Physical Compute","status":"catalog_only","capabilities":["dedicated-compute","server-management"]},
    {"service_type_id":"edge-server","name":"EDGE SERVER","category":"Edge Compute","status":"catalog_only","capabilities":["edge-compute","low-latency"]},
    {"service_type_id":"application-server","name":"APPLICATION SERVER","category":"Application Runtime","status":"catalog_only","capabilities":["application-runtime","deployment"]},
    {"service_type_id":"database-server","name":"DATABASE SERVER","category":"Database Infrastructure","status":"catalog_only","capabilities":["database-hosting","networking"]},
)

def get_layer_catalog():
    return tuple(_LAYERS)

def get_provider_catalog():
    return tuple(_PROVIDERS)

def list_providers():
    return [{
        "provider_id": p.provider_id, "name": p.display_name,
        "display_name": p.display_name, "package": p.package,
        "alignment": p.alignment, "status": p.status,
        "capabilities": list(p.capabilities),
    } for p in _PROVIDERS]

def get_provider(provider_id: str):
    key = str(provider_id).strip().lower()
    aliases = {"azure-cloud": "azure", "gcp": "google", "aws-cloud": "aws"}
    key = aliases.get(key, key)
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

__all__ = ["LayerDescriptor", "ProviderDescriptor", "get_layer_catalog",
           "get_provider_catalog", "list_providers", "get_provider",
           "list_service_types", "get_service_type"]
