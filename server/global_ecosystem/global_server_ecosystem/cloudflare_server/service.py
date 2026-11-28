"""Cloudflare SERVER provider adapter; live operations require explicit injection."""
from ..provider_base import ServerProviderAdapter

class CloudflareServerEcosystem(ServerProviderAdapter):
    provider_id = "cloudflare"
    display_name = "Cloudflare"
    capabilities = ("cloud-server-management", "server-lifecycle")

__all__ = ["CloudflareServerEcosystem"]
