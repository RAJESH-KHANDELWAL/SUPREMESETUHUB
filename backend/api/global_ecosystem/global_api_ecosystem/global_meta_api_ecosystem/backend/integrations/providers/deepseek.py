"""DeepSeek API configuration-readiness adapter.

Checks for a server-side API key. It does not make network requests, validate
credentials, or claim that the DeepSeek service is reachable.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class DeepSeekProvider(IntegrationProvider):
    """Reports DeepSeek API key readiness without network calls."""

    name = "DEEPSEEK"
    category = "AI"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api_families": [
                "CHAT_COMPLETIONS",
                "RESPONSES",
                "SEARCH",
                "FETCH",
            ],
            "models": ["deepseek-flash", "deepseek-v4-pro"],
            "base_url": "https://api.deepseek.com",
            "auth_method": "Bearer API key via server-side DEEPSEEK_API_KEY",
            "setup_guide": (
                "backend/api/global_ecosystem/global_api_ecosystem/"
                "deepseek_api_ecosystem/README.md"
            ),
            "connection": "NOT_TESTED",
            "live_connection_verified": False,
        }

    def health(self) -> Dict[str, Any]:
        configured = bool(os.getenv("DEEPSEEK_API_KEY", "").strip())
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="DeepSeek Bearer API key",
            required_configuration=["DEEPSEEK_API_KEY"],
            capabilities=[
                "CHAT_COMPLETIONS",
                "RESPONSES",
                "SEARCH",
                "FETCH",
            ],
        )
