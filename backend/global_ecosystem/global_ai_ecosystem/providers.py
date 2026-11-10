"""Provider registry for the Bharat-to-global AI ecosystem.

This registry describes provider packages. It does not imply that credentials,
SDKs, billing, or live network integrations are configured.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .cerebras_ecosystem.catalog import PROVIDER as CEREBRAS
from .fireworks_ai_ecosystem.catalog import PROVIDER as FIREWORKS_AI
from .groq_ecosystem.catalog import PROVIDER as GROQ
from .openrouter_ecosystem.catalog import PROVIDER as OPENROUTER
from .perplexity_ecosystem.catalog import PROVIDER as PERPLEXITY
from .replicate_ecosystem.catalog import PROVIDER as REPLICATE
from .together_ai_ecosystem.catalog import PROVIDER as TOGETHER_AI
from .xai_grok_ecosystem.catalog import PROVIDER as XAI_GROK
from .alibaba_qwen_ecosystem.catalog import PROVIDER as ALIBABA_QWEN
from .ibm_watsonx_ecosystem.catalog import PROVIDER as IBM_WATSONX
from .litellm_ecosystem.catalog import PROVIDER as LITELLM
from .ollama_ecosystem.catalog import PROVIDER as OLLAMA
from .sarvam_ai_ecosystem.catalog import PROVIDER as SARVAM_AI
from .vllm_ecosystem.catalog import PROVIDER as VLLM
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
    ALIBABA_QWEN,
    IBM_WATSONX,
    SARVAM_AI,
    OLLAMA,
    VLLM,
    LITELLM,
    XAI_GROK,
    PERPLEXITY,
    GROQ,
    CEREBRAS,
    TOGETHER_AI,
    FIREWORKS_AI,
    OPENROUTER,
    REPLICATE,
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
