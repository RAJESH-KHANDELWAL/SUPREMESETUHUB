"""Google Cloud SERVER provider adapter; remote execution requires injection."""
from ..provider_base import ServerProviderAdapter

class GoogleServerEcosystem(ServerProviderAdapter):
    provider_id = "google"
    display_name = "Google Cloud"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["GoogleServerEcosystem"]
