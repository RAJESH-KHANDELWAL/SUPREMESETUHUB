"""Cloudflare provider package in GLOBAL SERVER ECOSYSTEM."""
from ..cloudflare_server import CloudflareServerEcosystem

PROVIDER_ID = "cloudflare"
DISPLAY_NAME = "Cloudflare"
OWNING_DOMAIN = "SERVER"

__all__ = ["CloudflareServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
