"""Machine-readable catalog entry for Alibaba Qwen."""

PROVIDER = {
    "id": "alibaba_qwen",
    "name": "Alibaba Qwen",
    "vendor": "Alibaba Cloud",
    "category": "ai_provider",
    "api_endpoint": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
    "credential_env": "DASHSCOPE_API_KEY",
    "models_or_services": ["Qwen model API","Text and multimodal models"],
    "integration_status": "scaffold",
    "notes": "Alibaba Qwen model family; endpoint and model availability depend on region and account.",
}
