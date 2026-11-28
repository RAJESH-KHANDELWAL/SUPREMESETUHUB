"""Adobe developer API configuration readiness adapter."""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class AdobeProvider(IntegrationProvider):
    """Reports Adobe OAuth configuration; performs no network requests."""

    name = "ADOBE"
    category = "CREATIVE_AND_DOCUMENT_PLATFORM"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": [
                "ADOBE_PDF_SERVICES", "ADOBE_ACROBAT_SIGN",
                "ADOBE_FIREFLY_SERVICES", "ADOBE_CREATIVE_CLOUD_ASSETS",
                "ADOBE_EXPERIENCE_PLATFORM", "ADOBE_COMMERCE",
                "ADOBE_VIDEO_FRAMEIO",
            ],
            "auth_method": "Adobe OAuth 2.0; product-specific scopes and organization access required",
            "setup_guide": "backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/README.md",
        }

    def health(self) -> Dict[str, Any]:
        required = ["ADOBE_CLIENT_ID", "ADOBE_CLIENT_SECRET"]
        configured = all(os.getenv(key, "").strip() for key in required)
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Adobe OAuth 2.0",
            required_configuration=required,
            capabilities=[
                "PDF_SERVICES", "ACROBAT_SIGN", "FIREFLY_SERVICES",
                "CREATIVE_CLOUD_ASSETS", "EXPERIENCE_PLATFORM",
                "COMMERCE", "VIDEO_FRAMEIO",
            ],
        )
