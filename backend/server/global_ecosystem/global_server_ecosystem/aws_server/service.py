"""Amazon Web Services SERVER provider adapter; remote execution requires injection."""
from ..provider_base import ServerProviderAdapter

class AWSServerEcosystem(ServerProviderAdapter):
    provider_id = "aws"
    display_name = "Amazon Web Services"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["AWSServerEcosystem"]
