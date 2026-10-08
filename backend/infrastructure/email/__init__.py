"""Email infrastructure for MAIN BASE FOUNDATION."""

from .model import (
    EmailAccountInfo,
    EmailServiceInfo,
)
from .service import EmailService
from .controller import EmailController
from .providers import (
    EmailProviderInfo,
    EmailProviderRegistry,
    email_provider_registry,
)

__all__ = [
    "EmailAccountInfo",
    "EmailServiceInfo",
    "EmailService",
    "EmailController",
    "EmailProviderInfo",
    "EmailProviderRegistry",
    "email_provider_registry",
]
