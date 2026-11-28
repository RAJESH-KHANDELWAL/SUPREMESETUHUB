"""Microsoft Azure SERVER provider adapter; live operations require explicit injection."""
from ..provider_base import ServerProviderAdapter

class MicrosoftServerEcosystem(ServerProviderAdapter):
    provider_id = "microsoft"
    display_name = "Microsoft Azure"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["MicrosoftServerEcosystem"]
