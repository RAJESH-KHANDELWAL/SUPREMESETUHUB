from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class GoogleProvider(IntegrationProvider):
    """Google identity and API integration readiness adapter."""

    name = "GOOGLE"
    category = "PRODUCTIVITY_AND_CLOUD"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": ["GOOGLE_OAUTH", "WORKSPACE_APIS", "GOOGLE_CLOUD_APIS"],
            "auth_method": "Google OAuth 2.0 / service account where supported",
            "setup_guide": "docs/GOOGLE_MICROSOFT_AWS_APPLE_SETUP.md",
        }

    def health(self) -> Dict[str, Any]:
        import os
        required = ["GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI"]
        configured = all(os.getenv(key, "").strip() for key in required)
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Google OAuth 2.0",
            required_configuration=required,
            capabilities=["GMAIL", "DRIVE", "CALENDAR", "WORKSPACE", "GOOGLE_CLOUD"],
        )
