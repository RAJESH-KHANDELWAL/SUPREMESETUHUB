from typing import Any, Dict

from ..base import IntegrationProvider


class AppleProvider(IntegrationProvider):
    """Apple platform integration metadata; not a live Apple account connection."""

    name = "APPLE"
    category = "IDENTITY_DEVICE_SERVICES"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": "Apple Developer APIs",
            "capabilities": ["SIGN_IN_WITH_APPLE", "IOS", "IPADOS", "MACOS", "APP_STORE_CONNECT"],
            "authentication": "APPLE_DEVELOPER_CREDENTIALS_OR_OAUTH_WHERE_SUPPORTED",
            "connection": "NOT_CONNECTED",
        }

    def health(self) -> Dict[str, Any]:
        return {
            "provider": self.name,
            "category": self.category,
            "status": "READY",
            "authentication": "NOT_CONFIGURED",
            "connection": "NOT_CONNECTED",
        }
