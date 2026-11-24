"""Provider-owned DeepSeek product and capability catalog."""
from __future__ import annotations
from .constants import API_BASE_URL, API_KEY_ENV, DEFAULT_MODELS, PROVIDER_ID, PROVIDER_NAME, SUPPORTED_API_FAMILIES, STATUS_CATALOG_ONLY

PRODUCTS = (
    {"id": "deepseek-chat", "name": "DeepSeek Chat", "model_family": "chat",
     "capabilities": ("conversation", "text_generation", "structured_response")},
    {"id": "deepseek-reasoner", "name": "DeepSeek Reasoner", "model_family": "reasoning",
     "capabilities": ("reasoning", "multi_step_problem_solving", "text_generation")},
)
CAPABILITIES = ("chat_completion", "reasoning", "model_selection", "request_planning", "provider_readiness_metadata")

def get_catalog() -> dict:
    """Return fresh serializable catalog data without credentials or live claims."""
    return {
        "provider_id": PROVIDER_ID, "provider_name": PROVIDER_NAME,
        "category": "ai_provider", "api_base_url": API_BASE_URL,
        "credential_env": API_KEY_ENV, "models": list(DEFAULT_MODELS),
        "api_families": list(SUPPORTED_API_FAMILIES), "capabilities": list(CAPABILITIES),
        "products": [{**item, "capabilities": list(item["capabilities"])} for item in PRODUCTS],
        "status": STATUS_CATALOG_ONLY, "live_connection_verified": False,
        "architecture_refs": {
            "api": "backend/api/global_ecosystem/global_api_ecosystem/deepseek_api_ecosystem",
            "ai": "backend/global_ecosystem/global_ai_ecosystem/deepseek_ecosystem",
            "engine": "backend/engine/global_ecosystem/global_engine_ecosystem/deepseek_engine_ecosystem",
            "integration": "backend/integration/provider/deepseek.py",
            "database": "backend/database", "security_identity": "backend/security",
        },
    }

__all__ = ["PRODUCTS", "CAPABILITIES", "get_catalog"]
