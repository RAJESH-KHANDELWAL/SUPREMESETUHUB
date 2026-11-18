"""Apple developer API configuration-readiness adapter.

This adapter checks whether one supported credential set is present. It does
not generate tokens, validate private keys, or make live Apple API requests.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class AppleProvider(IntegrationProvider):
    """Reports Apple API credential readiness without claiming connectivity."""

    name = "APPLE"
    category = "IDENTITY_DEVICE_SERVICES"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": "Apple Developer APIs, App Store Connect, Sign in with Apple, APNs and StoreKit",
            "capabilities": [
                "APP_STORE_CONNECT",
                "SIGN_IN_WITH_APPLE",
                "APNS",
                "STOREKIT",
                "APP_STORE_SERVER_API",
                "APPLE_PAY_ELIGIBLE_INTEGRATIONS",
                "APPLE_DEVICE_MANAGEMENT",
                "ICLOUD_CLOUDKIT",
            ],
            "authentication": "API-family-specific Apple credentials; no universal Apple API credential",
            "connection": "NOT_TESTED",
            "setup_guide": "backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/README.md",
        }

    def health(self) -> Dict[str, Any]:
        sign_in_required = [
            "APPLE_SERVICES_ID",
            "APPLE_TEAM_ID",
            "APPLE_KEY_ID",
            "APPLE_PRIVATE_KEY",
            "APPLE_REDIRECT_URI",
        ]
        app_store_required = [
            "APPLE_ISSUER_ID",
            "APPLE_APP_STORE_KEY_ID",
            "APPLE_APP_STORE_PRIVATE_KEY",
        ]
        sign_in_configured = all(os.getenv(key, "").strip() for key in sign_in_required)
        app_store_configured = all(os.getenv(key, "").strip() for key in app_store_required)
        configured = sign_in_configured or app_store_configured
        required = (
            sign_in_required
            if not sign_in_configured and not app_store_configured
            else (app_store_required if app_store_configured else sign_in_required)
        )
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Apple API-family-specific credentials (Sign in with Apple or App Store Connect)",
            required_configuration=required,
            capabilities=[
                "APP_STORE_CONNECT",
                "SIGN_IN_WITH_APPLE",
                "APNS",
                "STOREKIT",
                "APP_STORE_SERVER_API",
                "APPLE_PAY_ELIGIBLE_INTEGRATIONS",
                "APPLE_DEVICE_MANAGEMENT",
                "ICLOUD_CLOUDKIT",
            ],
        )
