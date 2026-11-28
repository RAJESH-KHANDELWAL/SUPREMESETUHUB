"""Meta developer platform configuration-readiness adapter.

This adapter checks server-side Meta app configuration only. It does not
perform OAuth, exchange tokens, call Graph API, or claim live connectivity.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class MetaProvider(IntegrationProvider):
    """Reports Meta app configuration readiness without exposing credentials."""

    name = "META"
    category = "SOCIAL_MEDIA_AND_COMMUNICATION"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": (
                "Meta Graph API, Facebook Pages, Instagram, WhatsApp Business, "
                "Messenger, Threads, Marketing API, Business Management and Webhooks"
            ),
            "capabilities": [
                "META_GRAPH_API",
                "META_FACEBOOK_PAGES",
                "META_INSTAGRAM",
                "META_WHATSAPP_BUSINESS",
                "META_MESSENGER",
                "META_THREADS",
                "META_MARKETING_ADS",
                "META_LOGIN_IDENTITY",
                "META_BUSINESS_MANAGEMENT",
                "META_WEBHOOKS",
                "META_SDK_DEVELOPER_TOOLS",
                "META_AI_DISCOVERY_ONLY",
            ],
            "auth_method": (
                "Meta OAuth 2.0; product-specific permissions, app review, "
                "business verification and asset eligibility may be required"
            ),
            "connection": "NOT_TESTED",
            "setup_guide": (
                "backend/api/global_ecosystem/global_api_ecosystem/"
                "global_meta_api_ecosystem/README.md"
            ),
        }

    def health(self) -> Dict[str, Any]:
        required = [
            "META_APP_ID",
            "META_APP_SECRET",
            "META_REDIRECT_URI",
        ]
        configured = all(os.getenv(key, "").strip() for key in required)
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Meta OAuth 2.0 (configuration readiness only)",
            required_configuration=required,
            capabilities=[
                "GRAPH_API",
                "FACEBOOK_PAGES",
                "INSTAGRAM",
                "WHATSAPP_BUSINESS",
                "MESSENGER",
                "THREADS",
                "MARKETING_ADS",
                "LOGIN_IDENTITY",
                "BUSINESS_MANAGEMENT",
                "WEBHOOKS",
                "SDK_DEVELOPER_TOOLS",
                "META_AI_DISCOVERY_ONLY",
            ],
        )


__all__ = ["MetaProvider"]
