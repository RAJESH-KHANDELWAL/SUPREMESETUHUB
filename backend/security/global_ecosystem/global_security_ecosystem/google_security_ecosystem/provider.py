"""Google Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "google"
    display_name = "Google Security"

__all__ = ["Provider"]
