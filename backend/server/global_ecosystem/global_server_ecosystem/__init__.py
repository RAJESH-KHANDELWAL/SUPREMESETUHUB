"""Independent GLOBAL SERVER ECOSYSTEM public interface."""
from .catalog import get_provider_catalog, list_providers, get_provider, list_service_types, get_service_type
from .manager import GlobalServerEcosystemManager
from .service import GlobalServerEcosystemService, EcosystemService
from .registry import ServerRegistry
from .provider_registry import ServerProviderRegistry
from .provider_base import ServerProviderAdapter
from .integrations import ServerProviderGateway
from .services import ServerRuntimeService
from .tools import server_diagnostics, server_catalog
from .runtime import runtime_status
from .models import ServerNode, ServerHealth
from .operation_catalog import ServerCapability, list_capabilities, get_capability
from .operations import (ServerOperationService, ServerOperationError,
                         UnknownServerCapability, ServerCapabilityNotConfigured)
from .abelohost_server import AbelohostServerEcosystem
from .abelohost_server_ecosystem import AbelohostServerEcosystem as AbelohostServerProvider
from .aws_server_ecosystem import AWSServerEcosystem
from .azure_server_ecosystem import AzureServerEcosystem as AzureAdditionalServerEcosystem
from .cloudflare_server_ecosystem import CloudflareServerEcosystem as CloudflareServerProvider
from .digitalocean_server_ecosystem import DigitalOceanServerEcosystem
from .google_server_ecosystem import GoogleServerEcosystem
from .hostinger_server_ecosystem import HostingerServerEcosystem
from .microsoft_server_ecosystem import MicrosoftServerEcosystem as MicrosoftServerProvider
from .vicetemple_server_ecosystem import ViceTempleServerEcosystem as ViceTempleServerProvider
from .abelohost_server_server_ecosystem import ADAPTER_CLASS as AbelohostServerLayerAdapter
from .aws_server_server_ecosystem import ADAPTER_CLASS as AWSServerLayerAdapter
from .azure_server_server_ecosystem import ADAPTER_CLASS as AzureServerLayerAdapter
from .cloudflare_server_server_ecosystem import ADAPTER_CLASS as CloudflareServerLayerAdapter
from .digitalocean_server_server_ecosystem import ADAPTER_CLASS as DigitalOceanServerLayerAdapter
from .google_server_server_ecosystem import ADAPTER_CLASS as GoogleServerLayerAdapter
from .hostinger_server_server_ecosystem import ADAPTER_CLASS as HostingerServerLayerAdapter
from .microsoft_server_server_ecosystem import ADAPTER_CLASS as MicrosoftServerLayerAdapter
from .vicetemple_server_server_ecosystem import ADAPTER_CLASS as ViceTempleServerLayerAdapter

SERVER_LAYER_PROVIDER_PACKAGES = {
    "abelohost": AbelohostServerLayerAdapter,
    "aws": AWSServerLayerAdapter,
    "azure": AzureServerLayerAdapter,
    "cloudflare": CloudflareServerLayerAdapter,
    "digitalocean": DigitalOceanServerLayerAdapter,
    "google": GoogleServerLayerAdapter,
    "hostinger": HostingerServerLayerAdapter,
    "microsoft": MicrosoftServerLayerAdapter,
    "vicetemple": ViceTempleServerLayerAdapter,
}
from .cloudflare_server import CloudflareServerEcosystem
from .microsoft_server import MicrosoftServerEcosystem
from .vicetemple_server import ViceTempleServerEcosystem

__all__ = [
    "get_provider_catalog", "list_providers", "get_provider", "list_service_types",
    "get_service_type", "GlobalServerEcosystemManager", "GlobalServerEcosystemService",
    "EcosystemService", "ServerRegistry", "ServerProviderRegistry", "ServerProviderAdapter",
    "ServerProviderGateway", "ServerRuntimeService", "server_diagnostics", "server_catalog",
    "runtime_status", "ServerNode", "ServerHealth", "ServerCapability", "list_capabilities",
    "get_capability", "ServerOperationService", "ServerOperationError",
    "UnknownServerCapability", "ServerCapabilityNotConfigured", "AbelohostServerEcosystem",
    "CloudflareServerEcosystem", "MicrosoftServerEcosystem", "ViceTempleServerEcosystem",
    "AbelohostServerProvider", "AWSServerEcosystem", "AzureAdditionalServerEcosystem",
    "CloudflareServerProvider", "DigitalOceanServerEcosystem", "GoogleServerEcosystem",
    "HostingerServerEcosystem", "MicrosoftServerProvider", "ViceTempleServerProvider",
    "SERVER_LAYER_PROVIDER_PACKAGES", "AbelohostServerLayerAdapter", "AWSServerLayerAdapter",
    "AzureServerLayerAdapter", "CloudflareServerLayerAdapter", "DigitalOceanServerLayerAdapter",
    "GoogleServerLayerAdapter", "HostingerServerLayerAdapter", "MicrosoftServerLayerAdapter",
    "ViceTempleServerLayerAdapter",
]
