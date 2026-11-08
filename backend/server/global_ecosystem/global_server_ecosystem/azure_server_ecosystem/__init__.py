"""Microsoft Azure (additional integration) provider package in GLOBAL SERVER ECOSYSTEM."""
from ..azure_server import AzureServerEcosystem

PROVIDER_ID = "azure"
DISPLAY_NAME = "Microsoft Azure (additional integration)"
OWNING_DOMAIN = "SERVER"

__all__ = ["AzureServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
