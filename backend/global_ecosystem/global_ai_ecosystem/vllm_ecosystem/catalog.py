"""Machine-readable catalog entry for vLLM."""

PROVIDER = {
    "id": "vllm",
    "name": "vLLM",
    "vendor": "vLLM Project",
    "category": "inference_runtime",
    "api_endpoint": "http://localhost:8000/v1",
    "credential_env": "VLLM_API_KEY",
    "auth_mode": "optional",
    "models_or_services": ["OpenAI-compatible serving","High-throughput inference"],
    "integration_status": "scaffold",
    "notes": "Open-source inference and serving runtime; deployment controls authentication and endpoint.",
}
