"""SERVER-owned provider and server-service catalogs."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProviderDescriptor:
    provider_id: str
    display_name: str
    package: str
    alignment: str = "CANONICAL"
    status: str = "NOT_CONFIGURED"
    capabilities: tuple[str, ...] = ("cloud-server-management",)

_PROVIDERS = (
    ProviderDescriptor("abelohost", "Abelohost", "abelohost_server_server_ecosystem"),
    ProviderDescriptor("aws", "Amazon Web Services", "aws_server_server_ecosystem"),
    ProviderDescriptor("cloudflare", "Cloudflare", "cloudflare_server_server_ecosystem"),
    ProviderDescriptor("digitalocean", "DigitalOcean", "digitalocean_server_server_ecosystem"),
    ProviderDescriptor("google", "Google Cloud", "google_server_server_ecosystem"),
    ProviderDescriptor("microsoft", "Microsoft Azure", "microsoft_server_server_ecosystem"),
    ProviderDescriptor("vicetemple", "ViceTemple", "vicetemple_server_server_ecosystem"),
    ProviderDescriptor("azure", "Microsoft Azure (additional integration)", "azure_server_server_ecosystem", "ADDITIONAL"),
    ProviderDescriptor("hostinger", "Hostinger", "hostinger_server_server_ecosystem", "ADDITIONAL"),
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

def get_provider_catalog():
    return tuple(_PROVIDERS)

def list_providers():
    return [{"provider_id": p.provider_id, "name": p.display_name,
             "display_name": p.display_name, "package": p.package,
             "alignment": p.alignment, "status": p.status,
             "capabilities": list(p.capabilities)} for p in _PROVIDERS]

def get_provider(provider_id: str):
    key = str(provider_id or "").strip().lower()
    key = {"azure-cloud":"azure", "gcp":"google", "aws-cloud":"aws"}.get(key, key)
    for item in list_providers():
        if item["provider_id"] == key:
            return item
    raise KeyError(f"Unknown server provider: {provider_id}")

def list_service_types():
    return [{**item, "capabilities": list(item["capabilities"])} for item in _SERVICE_TYPES]

def get_service_type(service_type_id: str):
    key = str(service_type_id or "").strip().lower().replace("_","-").replace(" ","-")
    for item in _SERVICE_TYPES:
        if key == item["service_type_id"] or key.replace("-","") == item["service_type_id"].replace("-",""):
            return {**item, "capabilities": list(item["capabilities"])}
    raise KeyError(f"Unknown server service type: {service_type_id}")

__all__ = ["ProviderDescriptor", "get_provider_catalog", "list_providers",
           "get_provider", "list_service_types", "get_service_type"]
