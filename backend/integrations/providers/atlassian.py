"""Atlassian API configuration-readiness adapter.

This module checks server-side OAuth configuration presence only. It does not
exchange tokens, validate credentials, or make live Atlassian API requests.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import present_any, provider_health


class AtlassianProvider(IntegrationProvider):
    """Reports Atlassian OAuth configuration readiness without claiming connectivity."""

    name = "ATLASSIAN"
    category = "BUSINESS_DEVELOPER_TOOLS"

    _oauth_required = [
        "ATLASSIAN_CLIENT_ID",
        "ATLASSIAN_CLIENT_SECRET",
        "ATLASSIAN_REDIRECT_URI",
        "ATLASSIAN_SITE_URL",
    ]
    _bitbucket_required = [
        "BITBUCKET_CLIENT_ID",
        "BITBUCKET_CLIENT_SECRET",
        "BITBUCKET_REDIRECT_URI",
    ]

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_products": [
                "Jira Cloud Platform",
                "Confluence Cloud",
                "Jira Service Management",
                "Bitbucket Cloud",
                "Atlassian Administration and identity APIs",
            ],
            "capabilities": [
                "JIRA_CLOUD",
                "CONFLUENCE_CLOUD",
                "JIRA_SERVICE_MANAGEMENT",
                "BITBUCKET_CLOUD",
                "ATLASSIAN_ADMIN_IDENTITY",
            ],
            "auth_method": (
                "Atlassian OAuth 2.0 (3LO) and product-specific supported "
                "authentication; separate Bitbucket OAuth configuration may apply"
            ),
            "setup_guide": (
                "backend/api/global_ecosystem/global_api_ecosystem/"
                "atlassian_api_ecosystem/README.md"
            ),
        }

    def health(self) -> Dict[str, Any]:
        configured = present_any(
            tuple(self._oauth_required),
            tuple(self._bitbucket_required),
        )
        required = (
            self._oauth_required
            if all(os.getenv(key, "").strip() for key in self._oauth_required)
            else self._bitbucket_required
        )
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Atlassian OAuth 2.0 (3LO) / product-specific OAuth",
            required_configuration=required,
            capabilities=[
                "JIRA_CLOUD",
                "CONFLUENCE_CLOUD",
                "JIRA_SERVICE_MANAGEMENT",
                "BITBUCKET_CLOUD",
                "ATLASSIAN_ADMIN_IDENTITY",
            ],
        )
