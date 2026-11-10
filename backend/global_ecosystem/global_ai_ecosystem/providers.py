"""Provider registry for the Bharat-to-global AI ecosystem.

This registry describes provider packages. It does not imply that credentials,
SDKs, billing, or live network integrations are configured.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .anthropic_claude_ecosystem.catalog import PROVIDER as ANTHROPIC_CLAUDE
from .aws_bedrock_ecosystem.catalog import PROVIDER as AWS_BEDROCK
from .cohere_ecosystem.catalog import PROVIDER as COHERE
from .deepseek_ecosystem.catalog import PROVIDER as DEEPSEEK
from .google_gemini_ecosystem.catalog import PROVIDER as GOOGLE_GEMINI
from .huggingface_ecosystem.catalog import PROVIDER as HUGGINGFACE
from .meta_ai_ecosystem.catalog import PROVIDER as META_AI
from .microsoft_azure_ai_ecosystem.catalog import PROVIDER as MICROSOFT_AZURE_AI
from .mistral_ecosystem.catalog import PROVIDER as MISTRAL
from .nvidia_ai_ecosystem.catalog import PROVIDER as NVIDIA_AI
from .openai_chatgpt_ecosystem.catalog import PROVIDER as OPENAI_CHATGPT

_PROVIDER_CATALOG: tuple[dict[str, Any], ...] = (
    GOOGLE_GEMINI,
    OPENAI_CHATGPT,
    AWS_BEDROCK,
    ANTHROPIC_CLAUDE,
    MICROSOFT_AZURE_AI,
    META_AI,
    NVIDIA_AI,
    DEEPSEEK,
    MISTRAL,
    COHERE,
    HUGGINGFACE,
)


def list_ai_providers() -> tuple[dict[str, Any], ...]:
    """Return all registered provider records as defensive copies."""
    return tuple(deepcopy(item) for item in _PROVIDER_CATALOG)


def get_ai_provider(provider_id: str) -> dict[str, Any] | None:
    """Find one provider by its stable ID; return None when it is unknown."""
    normalized = provider_id.strip().lower()
    for item in _PROVIDER_CATALOG:
        if item["id"] == normalized:
            return deepcopy(item)
    return None
