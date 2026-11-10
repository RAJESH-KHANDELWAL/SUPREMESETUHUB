"""Machine-readable catalog entry for NVIDIA AI."""

PROVIDER = {
    "id": "nvidia_ai",
    "name": "NVIDIA AI",
    "vendor": "NVIDIA",
    "category": "ai_provider",
    "api_endpoint": "https://integrate.api.nvidia.com/v1",
    "credential_env": "NVIDIA_API_KEY",
    "models_or_services": ["nvidia-nim","nemotron"],
    "integration_status": "scaffold",
    "notes": "NVIDIA NIM and hosted inference endpoints vary by deployment.",
}
