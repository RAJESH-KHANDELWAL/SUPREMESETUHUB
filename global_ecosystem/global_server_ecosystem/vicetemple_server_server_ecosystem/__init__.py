"""ViceTemple provider namespace owned by GLOBAL SERVER."""
from .provider import PROVIDER_ID, DISPLAY_NAME, OWNING_DOMAIN, ADAPTER_CLASS
from .server import LAYER, PACKAGE_KIND, describe_server_provider

__all__ = [
    "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS",
    "LAYER", "PACKAGE_KIND", "describe_server_provider",
]
