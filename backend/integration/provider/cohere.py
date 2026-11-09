"""Cohere API configuration-readiness adapter.

Checks a server-side API key is present. It does not make live Cohere API
requests, validate the key, or claim connectivity.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class CohereProvider(IntegrationProvider):
    """Reports Cohere API key configuration readiness without network calls."""

    name = "COHERE"
    category = "AI"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api_families": [
                "COMMAND", "EMBED", "RERANK",
                "TOKENIZE_AND_MODEL_METADATA", "CLASSIFICATION_WHERE_SUPPORTED",
            ],
            "capabilities": [
                "COHERE_COMMAND",
                "COHERE_EMBED",
                "COHERE_RERANK",
                "COHERE_TOKENIZE",
                "COHERE_CLASSIFICATION",
            ],
            "auth_method": "Cohere API key via server-side COHERE_API_KEY",
            "setup_guide": (
                "backend/api/global_ecosystem/global_api_ecosystem/"
                "cohere_api_ecosystem/README.md"
            ),
            "connection": "NOT_TESTED",
        }

    def health(self) -> Dict[str, Any]:
        required = ["COHERE_API_KEY"]
        configured = bool(os.getenv("COHERE_API_KEY", "").strip())
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Cohere API key",
            required_configuration=required,
            capabilities=[
                "COHERE_COMMAND",
                "COHERE_EMBED",
                "COHERE_RERANK",
                "COHERE_TOKENIZE",
                "COHERE_CLASSIFICATION",
            ],
        )
