"""ViceTemple SERVER provider adapter; live operations require explicit injection."""
from ..provider_base import ServerProviderAdapter

class ViceTempleServerEcosystem(ServerProviderAdapter):
    provider_id = "vicetemple"
    display_name = "ViceTemple"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["ViceTempleServerEcosystem"]
