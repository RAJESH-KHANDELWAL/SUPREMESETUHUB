"""Independent GLOBAL SERVER ECOSYSTEM public interface."""
from .catalog import (
    get_layer_catalog, get_provider_catalog, list_providers, get_provider,
    list_service_types, get_service_type,
)
from .manager import GlobalServerEcosystemManager
from .service import GlobalServerEcosystemService, EcosystemService
from .registry import ServerLayerRegistry
from .provider_registry import ServerProviderRegistry
from .provider_base import ServerProviderAdapter
from .runtime import runtime_status
from .operation_catalog import ServerCapability, list_capabilities, get_capability
from .operations import (
    ServerOperationService, ServerOperationError,
    UnknownServerCapability, ServerCapabilityNotConfigured,
)
from .abelohost_server import AbelohostServerEcosystem
from .cloudflare_server import CloudflareServerEcosystem
from .microsoft_server import MicrosoftServerEcosystem
from .vicetemple_server import ViceTempleServerEcosystem

__all__ = [
    "get_layer_catalog", "get_provider_catalog", "list_providers", "get_provider",
    "list_service_types", "get_service_type", "GlobalServerEcosystemManager",
    "GlobalServerEcosystemService", "EcosystemService", "ServerLayerRegistry",
    "ServerProviderRegistry", "ServerProviderAdapter", "runtime_status",
    "ServerCapability", "list_capabilities", "get_capability",
    "ServerOperationService", "ServerOperationError", "UnknownServerCapability",
    "ServerCapabilityNotConfigured", "AbelohostServerEcosystem",
    "CloudflareServerEcosystem", "MicrosoftServerEcosystem",
    "ViceTempleServerEcosystem",
]
