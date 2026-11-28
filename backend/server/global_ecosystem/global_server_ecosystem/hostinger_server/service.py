"""Hostinger SERVER provider adapter; remote execution requires injection."""
from ..provider_base import ServerProviderAdapter

class HostingerServerEcosystem(ServerProviderAdapter):
    provider_id = "hostinger"
    display_name = "Hostinger"
    capabilities = ("server-management", "server-lifecycle")

__all__ = ["HostingerServerEcosystem"]
