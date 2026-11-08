"""DigitalOcean SERVER provider adapter; remote execution requires injection."""
from ..provider_base import ServerProviderAdapter

class DigitalOceanServerEcosystem(ServerProviderAdapter):
    provider_id = "digitalocean"
    display_name = "DigitalOcean"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["DigitalOceanServerEcosystem"]
