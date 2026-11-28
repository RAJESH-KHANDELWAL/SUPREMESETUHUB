"""Model-family metadata; availability and access must be checked at runtime."""
from .schemas import CatalogRecord

MODELS = (
    CatalogRecord("gpt-family", "GPT model family", "language_and_multimodal", "OpenAI general-purpose model family.", metadata={"provider_id": "openai"}),
    CatalogRecord("claude-family", "Claude model family", "language_and_reasoning", "Anthropic language and reasoning models.", metadata={"provider_id": "anthropic"}),
    CatalogRecord("gemini-family", "Gemini model family", "multimodal", "Google multimodal model family.", metadata={"provider_id": "google"}),
    CatalogRecord("llama-family", "Llama model family", "open_weight", "Meta open-weight model family.", metadata={"provider_id": "meta"}),
    CatalogRecord("mistral-family", "Mistral model family", "language_and_code", "Mistral open and hosted model families.", metadata={"provider_id": "mistral"}),
    CatalogRecord("deepseek-family", "DeepSeek model family", "reasoning_and_code", "DeepSeek model families.", metadata={"provider_id": "deepseek"}),
    CatalogRecord("command-family", "Command model family", "language_and_retrieval", "Cohere Command family.", metadata={"provider_id": "cohere"}),
    CatalogRecord("phi-family", "Phi model family", "small_language_model", "Microsoft Phi family.", metadata={"provider_id": "microsoft"}),
    CatalogRecord("qwen-family", "Qwen model family", "language_and_multimodal", "Alibaba Qwen model family.", metadata={"provider_id": "alibaba"}),
    CatalogRecord("whisper-family", "Whisper model family", "speech_recognition", "Speech recognition model family.", metadata={"provider_id": "openai"}),
)
