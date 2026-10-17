from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class AppleProvider(IntegrationProvider):
    """Apple Sign in and App Store Connect configuration readiness adapter."""

    name = "APPLE"
    category = "IDENTITY_DEVICE_SERVICES"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": "Sign in with Apple / App Store Connect API",
            "capabilities": ["SIGN_IN_WITH_APPLE", "APP_STORE_CONNECT", "IOS", "IPADOS", "MACOS"],
            "authentication": "Apple Services ID and/or App Store Connect API key, depending on feature",
            "connection": "NOT_TESTED",
            "setup_guide": "docs/GOOGLE_MICROSOFT_AWS_APPLE_SETUP.md",
        }

    def health(self) -> Dict[str, Any]:
        import os
        sign_in_required = [
            "APPLE_SERVICES_ID", "APPLE_TEAM_ID", "APPLE_KEY_ID",
            "APPLE_PRIVATE_KEY", "APPLE_REDIRECT_URI",
        ]
        app_store_required = [
            "APPLE_ISSUER_ID", "APPLE_APP_STORE_KEY_ID", "APPLE_APP_STORE_PRIVATE_KEY",
        ]
        sign_in_configured = all(os.getenv(key, "").strip() for key in sign_in_required)
        app_store_configured = all(os.getenv(key, "").strip() for key in app_store_required)
        configured = sign_in_configured or app_store_configured
        required = sign_in_required if not app_store_configured else app_store_required
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Sign in with Apple or App Store Connect API key",
            required_configuration=required,
            capabilities=["SIGN_IN_WITH_APPLE", "APP_STORE_CONNECT", "APPLE_PLATFORM_APIS"],
        )
