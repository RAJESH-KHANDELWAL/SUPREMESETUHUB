"""Provider directory: descriptive metadata only; no provider clients are created."""
from .schemas import CatalogRecord

PROVIDERS = (
    CatalogRecord("openai", "OpenAI", "foundation_model_provider", "Hosted multimodal and general-purpose model platform."),
    CatalogRecord("anthropic", "Anthropic", "foundation_model_provider", "Claude model platform."),
    CatalogRecord("google", "Google AI", "foundation_model_provider", "Gemini and Google AI model ecosystem."),
    CatalogRecord("microsoft", "Microsoft AI", "cloud_ai_platform", "Azure AI and Microsoft-hosted AI services."),
    CatalogRecord("aws", "Amazon Web Services", "cloud_ai_platform", "AWS AI services and managed model infrastructure."),
    CatalogRecord("meta", "Meta AI", "model_developer", "Open model families and Meta AI services."),
    CatalogRecord("nvidia", "NVIDIA", "accelerator_and_ai_platform", "GPU, inference and AI software platform."),
    CatalogRecord("huggingface", "Hugging Face", "model_hub", "Model, dataset and application hosting ecosystem."),
    CatalogRecord("mistral", "Mistral AI", "foundation_model_provider", "Hosted and open-weight model ecosystem."),
    CatalogRecord("cohere", "Cohere", "foundation_model_provider", "Enterprise language and retrieval models."),
    CatalogRecord("deepseek", "DeepSeek", "foundation_model_provider", "Reasoning and general-purpose model provider."),
    CatalogRecord("ibm", "IBM watsonx", "enterprise_ai_platform", "Enterprise AI platform and governance tooling."),
    CatalogRecord("oracle", "Oracle Cloud AI", "cloud_ai_platform", "Cloud AI and data platform services."),
    CatalogRecord("apple", "Apple Intelligence", "on_device_ai_platform", "On-device and platform-integrated AI capabilities."),
    CatalogRecord("adobe", "Adobe Firefly", "creative_ai_platform", "Creative generation and editing capabilities."),
)
