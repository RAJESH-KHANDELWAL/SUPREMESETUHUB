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
from .ai21_ecosystem.catalog import PROVIDER as AI21
from .assemblyai_ecosystem.catalog import PROVIDER as ASSEMBLYAI
from .baidu_ernie_ecosystem.catalog import PROVIDER as BAIDU_ERNIE
from .black_forest_labs_ecosystem.catalog import PROVIDER as BLACK_FOREST_LABS
from .bytedance_doubao_ecosystem.catalog import PROVIDER as BYTEDANCE_DOUBAO
from .elevenlabs_ecosystem.catalog import PROVIDER as ELEVENLABS
from .krutrim_ecosystem.catalog import PROVIDER as KRUTRIM
from .minimax_ecosystem.catalog import PROVIDER as MINIMAX
from .moonshot_kimi_ecosystem.catalog import PROVIDER as MOONSHOT_KIMI
from .runway_ai_ecosystem.catalog import PROVIDER as RUNWAY_AI
from .stability_ai_ecosystem.catalog import PROVIDER as STABILITY_AI
from .suno_ai_ecosystem.catalog import PROVIDER as SUNO_AI
from .tencent_hunyuan_ecosystem.catalog import PROVIDER as TENCENT_HUNYUAN
from .zhipu_glm_ecosystem.catalog import PROVIDER as ZHIPU_GLM
from .adobe_firefly_ecosystem.catalog import PROVIDER as ADOBE_FIREFLY
from .ai4bharat_ecosystem.catalog import PROVIDER as AI4BHARAT
from .bharatgpt_ecosystem.catalog import PROVIDER as BHARATGPT
from .corover_ai_ecosystem.catalog import PROVIDER as COROVER_AI
from .databricks_ai_ecosystem.catalog import PROVIDER as DATABRICKS_AI
from .gnani_ai_ecosystem.catalog import PROVIDER as GNANI_AI
from .hanooman_ecosystem.catalog import PROVIDER as HANOOMAN
from .oracle_cloud_ai_ecosystem.catalog import PROVIDER as ORACLE_CLOUD_AI
from .salesforce_einstein_ecosystem.catalog import PROVIDER as SALESFORCE_EINSTEIN
from .snowflake_cortex_ecosystem.catalog import PROVIDER as SNOWFLAKE_CORTEX
from .apple_intelligence_ecosystem.catalog import PROVIDER as APPLE_INTELLIGENCE
from .autogen_ecosystem.catalog import PROVIDER as AUTOGEN
from .bloom_model_ecosystem.catalog import PROVIDER as BLOOM_MODELS
from .crewai_ecosystem.catalog import PROVIDER as CREWAI
from .dspy_ecosystem.catalog import PROVIDER as DSPY
from .gemma_model_ecosystem.catalog import PROVIDER as GEMMA_MODELS
from .haystack_ecosystem.catalog import PROVIDER as HAYSTACK
from .langchain_ecosystem.catalog import PROVIDER as LANGCHAIN
from .langgraph_ecosystem.catalog import PROVIDER as LANGGRAPH
from .llama_model_ecosystem.catalog import PROVIDER as LLAMA_MODELS
from .llamaindex_ecosystem.catalog import PROVIDER as LLAMAINDEX
from .microsoft_copilot_ecosystem.catalog import PROVIDER as MICROSOFT_COPILOT
from .nemotron_model_ecosystem.catalog import PROVIDER as NEMOTRON_MODELS
from .phi_model_ecosystem.catalog import PROVIDER as PHI_MODELS
from .sap_joule_ecosystem.catalog import PROVIDER as SAP_JOULE
from .semantic_kernel_ecosystem.catalog import PROVIDER as SEMANTIC_KERNEL
from .stable_diffusion_model_ecosystem.catalog import PROVIDER as STABLE_DIFFUSION_MODELS
from .flux_model_ecosystem.catalog import PROVIDER as FLUX_MODELS
from .granite_model_ecosystem.catalog import PROVIDER as GRANITE_MODELS
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
    APPLE_INTELLIGENCE,
    AUTOGEN,
    BLOOM_MODELS,
    CREWAI,
    DSPY,
    GEMMA_MODELS,
    HAYSTACK,
    LANGCHAIN,
    LANGGRAPH,
    LLAMA_MODELS,
    MICROSOFT_COPILOT,
    NEMOTRON_MODELS,
    PHI_MODELS,
    SAP_JOULE,
    SEMANTIC_KERNEL,
    STABLE_DIFFUSION_MODELS,
    FLUX_MODELS,
    GRANITE_MODELS,
    ADOBE_FIREFLY,
    AI4BHARAT,
    BHARATGPT,
    COROVER_AI,
    DATABRICKS_AI,
    GNANI_AI,
    HANOOMAN,
    ORACLE_CLOUD_AI,
    SALESFORCE_EINSTEIN,
    SNOWFLAKE_CORTEX,
    AI21,
    ASSEMBLYAI,
    BAIDU_ERNIE,
    BLACK_FOREST_LABS,
    BYTEDANCE_DOUBAO,
    ELEVENLABS,
    KRUTRIM,
    MINIMAX,
    MOONSHOT_KIMI,
    RUNWAY_AI,
    STABILITY_AI,
    SUNO_AI,
    TENCENT_HUNYUAN,
    ZHIPU_GLM,
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


def list_ai_providers(
    *, category: str | None = None, integration_status: str | None = None
) -> tuple[dict[str, Any], ...]:
    """Return defensive copies, optionally filtered by category or readiness."""
    records = _PROVIDER_CATALOG
    if category is not None:
        records = tuple(item for item in records if item.get("category") == category)
    if integration_status is not None:
        records = tuple(
            item for item in records
            if item.get("integration_status") == integration_status
        )
    return tuple(deepcopy(item) for item in records)


def validate_provider_registry() -> tuple[str, ...]:
    """Return registry integrity errors; an empty tuple means metadata is consistent."""
    errors: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(_PROVIDER_CATALOG):
        provider_id = item.get("id")
        if not isinstance(provider_id, str) or not provider_id.strip():
            errors.append(f"entry[{index}] has no valid id")
            continue
        if provider_id in seen:
            errors.append(f"duplicate provider id: {provider_id}")
        seen.add(provider_id)
        if not item.get("name") or not item.get("category"):
            errors.append(f"{provider_id} is missing name or category")
        if item.get("integration_status") not in {
            "scaffold", "catalog_only", "integration_in_progress", "live",
        }:
            errors.append(f"{provider_id} has an unknown integration_status")
        if item.get("integration_status") == "live" and not item.get("api_endpoint"):
            errors.append(f"{provider_id} is marked live without an API endpoint")
    return tuple(errors)


def get_ai_provider(provider_id: str) -> dict[str, Any] | None:
    """Find one provider by its stable ID; return None when it is unknown."""
    normalized = provider_id.strip().lower()
    for item in _PROVIDER_CATALOG:
        if item["id"] == normalized:
            return deepcopy(item)
    return None
