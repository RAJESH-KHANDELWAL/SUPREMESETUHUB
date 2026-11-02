"""Global email provider registry for SUPREMESETUHUB.

This module describes supported email providers and their integration
metadata. It does not store credentials or expose provider secrets.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class EmailProviderInfo:
    """Metadata for an email provider."""

    provider_id: str
    name: str
    provider_type: str
    official_domain: str
    auth_methods: tuple[str, ...] = ()
    smtp_supported: bool = False
    imap_supported: bool = False
    api_supported: bool = False
    status: str = "AVAILABLE"

    def to_dict(self) -> dict:
        """Return provider metadata as a dictionary."""
        return {
            "provider_id": self.provider_id,
            "name": self.name,
            "provider_type": self.provider_type,
            "official_domain": self.official_domain,
            "auth_methods": list(self.auth_methods),
            "smtp_supported": self.smtp_supported,
            "imap_supported": self.imap_supported,
            "api_supported": self.api_supported,
            "status": self.status,
        }


class EmailProviderRegistry:
    """Registry of supported global email providers."""

    def __init__(self) -> None:
        self._providers: Dict[str, EmailProviderInfo] = {}

    def register(self, provider: EmailProviderInfo) -> None:
        """Register or replace an email provider."""
        self._providers[provider.provider_id] = provider

    def get(self, provider_id: str) -> EmailProviderInfo | None:
        """Return a provider by ID."""
        return self._providers.get(provider_id)

    def list_all(self) -> List[EmailProviderInfo]:
        """Return all registered providers."""
        return list(self._providers.values())

    def public_list(self) -> List[dict]:
        """Return public provider metadata."""
        return [
            provider.to_dict()
            for provider in self.list_all()
        ]


email_provider_registry = EmailProviderRegistry()


# ============================================================
# SUPREMESETU MAIL
# ============================================================

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="supremesetu",
        name="SUPREMESETU MAIL",
        provider_type="OWN_PROVIDER",
        official_domain="",
        auth_methods=("PASSWORD",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=True,
        status="FOUNDATION",
    )
)


# ============================================================
# EXTERNAL PROVIDERS
# ============================================================

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="google",
        name="GOOGLE / GMAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="google.com",
        auth_methods=("OAUTH2",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=True,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="proton",
        name="PROTON MAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="proton.me",
        auth_methods=("SUPPORTED_AUTH",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=False,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="microsoft",
        name="MICROSOFT / OUTLOOK",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="microsoft.com",
        auth_methods=("OAUTH2",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=True,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="yahoo",
        name="YAHOO MAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="yahoo.com",
        auth_methods=("OAUTH2",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=True,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="apple",
        name="APPLE / ICLOUD MAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="icloud.com",
        auth_methods=("APP_PASSWORD",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=False,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="zoho",
        name="ZOHO MAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="zoho.com",
        auth_methods=("OAUTH2",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=True,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="gmx",
        name="GMX MAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="gmx.com",
        auth_methods=("PASSWORD",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=False,
        status="AVAILABLE",
    )
)

email_provider_registry.register(
    EmailProviderInfo(
        provider_id="fastmail",
        name="FASTMAIL",
        provider_type="EXTERNAL_PROVIDER",
        official_domain="fastmail.com",
        auth_methods=("OAUTH2",),
        smtp_supported=True,
        imap_supported=True,
        api_supported=True,
        status="AVAILABLE",
    )
)
