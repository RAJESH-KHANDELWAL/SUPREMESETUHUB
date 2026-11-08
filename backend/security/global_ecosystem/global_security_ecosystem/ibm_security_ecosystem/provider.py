"""IBM Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "ibm"
    display_name = "IBM Security"

__all__ = ["Provider"]
