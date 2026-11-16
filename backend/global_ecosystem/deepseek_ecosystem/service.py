"""DeepSeek ecosystem discovery and safe request planning."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .constants import DEFAULT_MODELS
from .models import DeepSeekRequestPlan
from .validation import safe_input_summary, validate_request

class DeepSeekEcosystemService:
    """Build catalog data and request plans without provider network calls."""
    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def plan_request(self, operation: str, payload: dict[str, Any], model: str = "deepseek-chat") -> dict[str, Any]:
        validate_request(operation, payload)
        if model not in DEFAULT_MODELS:
            raise ValueError(f"Unsupported catalog model: {model}")
        return DeepSeekRequestPlan(
            operation=operation, model=model, input_summary=safe_input_summary(payload)
        ).to_dict()

    def architecture(self) -> dict[str, str]:
        """Expose ownership without merging API, CORE, or ENGINE."""
        return {
            "ecosystem": "provider discovery, metadata, request planning",
            "api": "transport, endpoint contracts, authentication middleware",
            "core": "shared domain contracts and policies",
            "engine": "execution orchestration and lifecycle",
            "database": "persistence and data access",
            "security_identity": "authorization, secret storage, audit",
        }

__all__ = ["DeepSeekEcosystemService"]
