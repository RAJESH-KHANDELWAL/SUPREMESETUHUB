"""Factory for verified OpenAI-compatible provider adapter contracts."""
from __future__ import annotations

from typing import Any

from .openai_compatible import OpenAICompatibleChatAdapter

# These providers publish an OpenAI-compatible chat endpoint in their API surface.
# This does not imply every feature or parameter is fully interchangeable.
_OPENAI_COMPATIBLE_IDS = frozenset({
    "xai_grok", "groq", "cerebras", "together_ai", "fireworks_ai",
    "openrouter", "perplexity",
})


def list_chat_adapter_provider_ids() -> tuple[str, ...]:
    return tuple(sorted(_OPENAI_COMPATIBLE_IDS))


def create_chat_adapter(
    provider_id: str, *, api_key: str | None = None, base_url: str | None = None,
    http_client: Any = None,
) -> OpenAICompatibleChatAdapter:
    """Create a chat adapter only for providers explicitly allowlisted here."""
    normalized = provider_id.strip().lower()
    if normalized not in _OPENAI_COMPATIBLE_IDS:
        raise ValueError(f"No OpenAI-compatible chat adapter is registered for: {normalized}")
    from ..providers import get_ai_provider

    provider = get_ai_provider(normalized)
    if provider is None:
        raise ValueError(f"Provider is missing from the global registry: {normalized}")
    return OpenAICompatibleChatAdapter(
        provider, api_key=api_key, base_url=base_url, http_client=http_client,
    )
