"""Apple Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "apple"
    display_name = "Apple Security"

__all__ = ["Provider"]
