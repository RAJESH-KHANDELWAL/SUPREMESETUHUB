"""Abelohost SERVER provider adapter; live operations require explicit injection."""
from ..provider_base import ServerProviderAdapter

class AbelohostServerEcosystem(ServerProviderAdapter):
    provider_id = "abelohost"
    display_name = "Abelohost"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["AbelohostServerEcosystem"]
