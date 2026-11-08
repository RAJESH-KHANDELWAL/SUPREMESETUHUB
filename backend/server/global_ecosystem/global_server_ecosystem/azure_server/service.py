"""Microsoft Azure SERVER provider adapter; remote execution requires injection."""
from ..provider_base import ServerProviderAdapter

class AzureServerEcosystem(ServerProviderAdapter):
    provider_id = "azure"
    display_name = "Microsoft Azure"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["AzureServerEcosystem"]
