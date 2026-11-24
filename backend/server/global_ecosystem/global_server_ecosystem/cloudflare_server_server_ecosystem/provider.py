"""Cloudflare provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..cloudflare_server_ecosystem import CloudflareServerEcosystem

PROVIDER_ID = "cloudflare"
DISPLAY_NAME = "Cloudflare"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = CloudflareServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
