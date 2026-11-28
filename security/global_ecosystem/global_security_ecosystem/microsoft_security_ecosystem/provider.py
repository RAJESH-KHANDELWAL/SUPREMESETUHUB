"""Microsoft Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "microsoft"
    display_name = "Microsoft Security"

__all__ = ["Provider"]
