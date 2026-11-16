"""AWS Security adapter namespace; no credentials or network calls at import time."""
from ..provider_base import SecurityProviderAdapter

class Provider(SecurityProviderAdapter):
    provider_id = "aws"
    display_name = "AWS Security"

__all__ = ["Provider"]
