"""Cloudflare Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "cloudflare"
    display_name = "Cloudflare Security"

__all__ = ["Provider"]
