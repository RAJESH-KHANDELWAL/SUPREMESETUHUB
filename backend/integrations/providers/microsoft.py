from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class MicrosoftProvider(IntegrationProvider):
    """Microsoft Entra ID / Microsoft Graph readiness adapter."""

    name = "MICROSOFT"
    category = "PRODUCTIVITY_AND_CLOUD"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": ["MICROSOFT_ENTRA_ID", "MICROSOFT_GRAPH", "AZURE"],
            "auth_method": "Microsoft Entra ID OAuth 2.0",
            "setup_guide": "docs/GOOGLE_MICROSOFT_AWS_APPLE_SETUP.md",
        }

    def health(self) -> Dict[str, Any]:
        import os
        required = ["MICROSOFT_CLIENT_ID", "MICROSOFT_CLIENT_SECRET", "MICROSOFT_REDIRECT_URI"]
        configured = all(os.getenv(key, "").strip() for key in required) and bool(os.getenv("MICROSOFT_TENANT_ID", "common").strip())
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Microsoft Entra ID OAuth 2.0",
            required_configuration=required,
            capabilities=["MICROSOFT_GRAPH", "OUTLOOK", "ONEDRIVE", "SHAREPOINT", "AZURE"],
        )
