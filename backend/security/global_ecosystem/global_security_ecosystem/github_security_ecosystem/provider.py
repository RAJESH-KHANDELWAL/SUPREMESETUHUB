"""GitHub Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "github"
    display_name = "GitHub Security"

__all__ = ["Provider"]
