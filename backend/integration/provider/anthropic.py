"""Anthropic Claude API integration readiness adapter."""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class AnthropicProvider(IntegrationProvider):
    """Anthropic API configuration readiness; does not make network requests."""

    name = "ANTHROPIC"
    category = "AI_PLATFORM"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": [
                "ANTHROPIC_MESSAGES", "ANTHROPIC_MESSAGE_BATCHES",
                "ANTHROPIC_MODELS", "ANTHROPIC_TOKEN_COUNTING",
                "ANTHROPIC_FILES", "ANTHROPIC_ADMIN_WORKSPACES",
                "ANTHROPIC_MANAGED_AGENTS", "ANTHROPIC_TOOL_USE",
                "ANTHROPIC_WORKLOAD_IDENTITY_FEDERATION",
            ],
            "auth_method": "Anthropic API key via server-side ANTHROPIC_API_KEY secret",
            "setup_guide": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/README.md",
        }

    def health(self) -> Dict[str, Any]:
        configured = bool(os.getenv("ANTHROPIC_API_KEY", "").strip())
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Anthropic API key",
            required_configuration=["ANTHROPIC_API_KEY"],
            capabilities=[
                "MESSAGES", "MESSAGE_BATCHES", "MODELS", "TOKEN_COUNTING",
                "FILES", "ADMIN_WORKSPACES", "MANAGED_AGENTS", "TOOL_USE",
                "WORKLOAD_IDENTITY_FEDERATION",
            ],
        )
