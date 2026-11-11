"""DeepSeek ecosystem discovery and safe request planning."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .constants import DEFAULT_MODELS
from .models import DeepSeekRequestPlan
from .validation import validate_request

class DeepSeekEcosystemService:
    """Build metadata and request plans without making provider network calls."""

    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def plan_request(
        self, operation: str, payload: dict[str, Any], model: str = "deepseek-chat"
    ) -> dict[str, Any]:
        validate_request(operation, payload)
        if model not in DEFAULT_MODELS:
            raise ValueError(f"Unsupported catalog model: {model}")
        summary = {
            "input_fields": sorted(str(key) for key in payload),
            "contains_user_content": any(key in payload for key in ("messages", "input", "prompt", "query", "url")),
        }
        return DeepSeekRequestPlan(operation=operation, model=model, input_summary=summary).to_dict()

    def architecture(self) -> dict[str, str]:
        return {
            "transport": "API",
            "provider_capability_contract": "AI",
            "orchestration": "ENGINE",
            "persistence": "DATABASE",
            "credentials_and_access": "SECURITY_IDENTITY",
        }

__all__ = ["DeepSeekEcosystemService"]
