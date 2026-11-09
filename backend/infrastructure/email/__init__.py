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

from .provider_connector import (
    EmailProviderConnector,
)

from .connector_registry import (
    EmailProviderConnectorRegistry,
    email_provider_connector_registry,
)


__all__ = [
    "EmailAccountInfo",
    "EmailServiceInfo",
    "EmailService",
    "EmailController",
    "EmailProviderInfo",
    "EmailProviderRegistry",
    "email_provider_registry",
    "EmailProviderConnector",
    "EmailProviderConnectorRegistry",
    "email_provider_connector_registry",
]
