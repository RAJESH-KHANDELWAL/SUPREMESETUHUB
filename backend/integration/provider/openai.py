"""OpenAI API integration readiness adapter."""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class OpenAIProvider(IntegrationProvider):
    """OpenAI API Platform readiness; does not imply a live connection."""

    name = "OPENAI"
    category = "AI_PLATFORM"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": [
                "OPENAI_RESPONSES_API",
                "OPENAI_MODELS",
                "OPENAI_EMBEDDINGS",
                "OPENAI_IMAGES",
                "OPENAI_AUDIO",
                "OPENAI_REALTIME",
                "OPENAI_FILES",
                "OPENAI_BATCH",
                "OPENAI_MODERATION",
                "OPENAI_AGENTS",
            ],
            "auth_method": "OpenAI API key stored server-side in environment or managed secret store",
            "setup_guide": "Configure OPENAI_API_KEY in deployment secrets; never commit it.",
        }

    def health(self) -> Dict[str, Any]:
        configured = bool(os.getenv("OPENAI_API_KEY", "").strip())
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="OpenAI API key",
            required_configuration=["OPENAI_API_KEY"],
            capabilities=[
                "RESPONSES",
                "MODELS",
                "EMBEDDINGS",
                "IMAGES",
                "AUDIO",
                "REALTIME",
                "FILES",
                "BATCH",
                "MODERATION",
                "AGENTS",
            ],
        )
