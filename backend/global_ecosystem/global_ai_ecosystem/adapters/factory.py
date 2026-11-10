"""Factory for provider-specific OpenAI-compatible chat adapters."""
from __future__ import annotations

from typing import Any

from ..cerebras_ecosystem.adapter import CerebrasAdapter
from ..fireworks_ai_ecosystem.adapter import FireworksAIAdapter
from ..groq_ecosystem.adapter import GroqAdapter
from ..openrouter_ecosystem.adapter import OpenRouterAdapter
from ..perplexity_ecosystem.adapter import PerplexityAdapter
from ..together_ai_ecosystem.adapter import TogetherAIAdapter
from ..xai_grok_ecosystem.adapter import XaiGrokAdapter
from ..alibaba_qwen_ecosystem.adapter import QwenAdapter
from ..anthropic_claude_ecosystem.adapter import AnthropicClaudeAdapter
from ..deepseek_ecosystem.adapter import DeepSeekAdapter
from ..google_gemini_ecosystem.adapter import GeminiAdapter
from ..mistral_ecosystem.adapter import MistralAdapter
from ..openai_chatgpt_ecosystem.adapter import OpenAIAdapter
from ..ollama_ecosystem.adapter import OllamaAdapter
from ..vllm_ecosystem.adapter import VLLMAdapter

_ADAPTERS = {
    "xai_grok": XaiGrokAdapter,
    "groq": GroqAdapter,
    "cerebras": CerebrasAdapter,
    "together_ai": TogetherAIAdapter,
    "fireworks_ai": FireworksAIAdapter,
    "openrouter": OpenRouterAdapter,
    "perplexity": PerplexityAdapter,
    "ollama": OllamaAdapter,
    "vllm": VLLMAdapter,
    "openai_chatgpt": OpenAIAdapter,
    "google_gemini": GeminiAdapter,
    "anthropic_claude": AnthropicClaudeAdapter,
    "deepseek": DeepSeekAdapter,
    "mistral": MistralAdapter,
    "alibaba_qwen": QwenAdapter,
}


def list_chat_adapter_provider_ids() -> tuple[str, ...]:
    return tuple(sorted(_ADAPTERS))


def create_chat_adapter(
    provider_id: str, *, api_key: str | None = None, base_url: str | None = None,
    http_client: Any = None,
):
    """Create a provider adapter only for an explicitly supported API contract."""
    normalized = provider_id.strip().lower()
    adapter_type = _ADAPTERS.get(normalized)
    if adapter_type is None:
        raise ValueError(f"No chat adapter is registered for: {normalized}")
    kwargs = {"api_key": api_key, "base_url": base_url}
    if http_client is not None:
        kwargs["http_client"] = http_client
    return adapter_type(**kwargs)
